#!/usr/bin/env python3
"""Compile structured Markdown into Canvas-compliant inline-styled HTML.

Why this exists:
  Canvas strips <style> tags, forcing verbose inline CSS on every HTML element.
  Having an LLM generate 30 KB of raw inline CSS wastes 60-70% of output tokens
  and bloats the conversation context window. Authoring in structured Markdown and
  compiling deterministically to HTML eliminates CSS drift, guarantees lint-clean
  markup, and cuts token usage by ~65%.

Supported templates (--template or frontmatter `template:`):
  * page-f1     - Format 1 (BIT221 canonical student resource page, 860px)
  * page-f2     - Format 2 (Modern Minimal student resource page, 900px)
  * lecture     - Instructor Lecture Notes (v5.0 canonical, 860px, Instructor badge)
  * lab-notes   - Student Lab Notes (v1.0 canonical 5-section left-border boxes)
  * assignment  - Canonical 3-box Assignment (Purpose, Task, Instructions, Deliverables, Criteria)

Markdown conventions:
  Frontmatter (YAML-style key: value between --- lines):
    template: page-f1 | page-f2 | lecture | assignment
    title: Page or Assignment Title
    week: Week 1 - Topic Area          (pages/lectures)
    subtitle: Optional subtitle        (page-f2)

  Special H2 sections (matched by title in pages/lectures):
    ## Learning Objectives             -> renders the purple 2-col checkmark grid (f1/lecture) or blue left-border box (f2)
    ## Key Teaching Points             -> renders the blue KTP box (lecture)
    ## Why This Matters                -> renders the green motivation box (page-f1) or section (page-f2)
    ## Applied: <Title>                -> renders the dark charcoal (#2c2c2a) section box
    ## Discussion: <Title>             -> renders the dark charcoal (#2c2c2a) section box
    ## Common Mistakes to Avoid        -> renders the dark charcoal mistakes box (or table)
    ## What's Current                  -> renders the amber What's Current box (lecture)
    ## Reference Links / ## Resources  -> renders the light-blue Reference Links box
    ## <Any other H2>                  -> renders a standard content section box (f1/lecture) or clean H2 (f2)

  Special H2 sections in `assignment` template:
    ## Purpose                         -> Blue Purpose <table> box (include ### Course Learning Outcomes & ### Program Outcomes)
    ## Task                            -> Yellow Task <table> box
    ## Instructions / ## <Steps>       -> Plain HTML body instructions
    ## Deliverables                    -> Plain HTML Deliverables section (placed before Criteria)
    ## Criteria for Success            -> Green Criteria <table> box (enforces intro <p> before <ul>, placed last)

  Inline / Block Callouts & Markers:
    > **Note:** ... or > **Pro tip:** ... or > **Teaching note:** ... -> Amber callout box
    > **Info:** ...                                                   -> Blue callout box
    [SCREENSHOT]                                                      -> Camera icon <img> tag
    [HINT]                                                            -> Yellow highlighted Hint: span

Usage:
  python tools/canvas_build.py input.md -o scratchpad/output.html [--template page-f1]
"""

import argparse
import html as html_lib
import io
import os
import re
import sys

from canvas_lint import lint_html, format_report

SCREENSHOT_IMG = (
    '<img src="https://img.icons8.com/carbon-copy/2x/camera.png" '
    'alt="Screenshot required" width="25" height="25" loading="lazy">'
)
HINT_SPAN = '<span style="background-color: #ffff00;"><strong>Hint:</strong></span>'


def normalize_text(text):
    """Replace literal em dashes outside code with space-hyphen-space."""
    return re.sub(r"\s*\u2014\s*", " - ", text)


def format_inline(text, dark_bg=False):
    """Convert inline Markdown (**bold**, *italic*, `code`, [link](url), [SCREENSHOT], [HINT])."""
    text = normalize_text(text)
    # Protect inline code spans first
    code_spans = []

    def save_code(m):
        code_spans.append(html_lib.escape(m.group(1)))
        return f"\x00CODE{len(code_spans) - 1}\x00"

    text = re.sub(r"`([^`]+)`", save_code, text)
    text = html_lib.escape(text, quote=False)

    # Restore special tokens
    text = text.replace("[SCREENSHOT]", SCREENSHOT_IMG)
    text = text.replace("[HINT]", HINT_SPAN)

    # Links: [label](url)
    link_color = "#9fe1cb" if dark_bg else "#185fa5"
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a style="color: {link_color};" href="{m.group(2)}" target="_blank">{m.group(1)}</a>',
        text,
    )

    # Bold & italic
    if dark_bg:
        text = re.sub(r"\*\*([^*]+)\*\*", r'<strong style="color: #9FE1CB;">\1</strong>', text)
    else:
        text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)

    # Restore inline code
    code_style = (
        "background-color: #1a1a1a; color: #9fe1cb; padding: 2px 5px; border-radius: 3px; font-family: monospace;"
        if dark_bg
        else "background-color: #eae8e1; color: #2c2c2a; padding: 2px 5px; border-radius: 3px; font-family: monospace;"
    )
    for idx, c in enumerate(code_spans):
        text = text.replace(f"\x00CODE{idx}\x00", f'<code style="{code_style}">{c}</code>')
    return text


def parse_frontmatter(md_text):
    meta = {}
    body = md_text
    if md_text.startswith("---"):
        parts = md_text.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip().lower()] = v.strip().strip('"').strip("'")
            body = parts[2].lstrip("\r\n")
    return meta, body


def split_h2_sections(body):
    """Return list of (h2_title, section_markdown_lines)."""
    sections = []
    cur_title = None
    cur_lines = []
    in_fence = False
    for line in body.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
        if not in_fence and line.startswith("## "):
            if cur_title is not None or cur_lines:
                sections.append((cur_title, "\n".join(cur_lines).strip()))
            cur_title = normalize_text(line[3:].strip())
            cur_lines = []
        else:
            cur_lines.append(line)
    if cur_title is not None or any(l.strip() for l in cur_lines):
        sections.append((cur_title, "\n".join(cur_lines).strip()))
    return sections


def render_table(table_lines, fmt="f1"):
    rows = []
    for line in table_lines:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(re.match(r"^:?-+:?$", c) for c in cells if c):
            continue
        rows.append(cells)
    if not rows:
        return ""
    headers = rows[0]
    data = rows[1:]

    if fmt == "f2":
        out = ['<table style="width: 100%; border-collapse: collapse; background: #ffffff; margin: 16px 0 24px 0;">']
        out.append('  <thead style="background: #f3f4f6; border-bottom: 2px solid #e5e7eb;">')
        out.append("    <tr>")
        for h in headers:
            out.append(f'      <th style="padding: 12px 16px; text-align: left; color: #1a1a1a; border: 1px solid #e5e7eb;"><strong>{format_inline(h)}</strong></th>')
        out.append("    </tr>")
        out.append("  </thead>")
        out.append("  <tbody>")
        for idx, r in enumerate(data):
            bg = "#ffffff" if idx % 2 == 0 else "#f9f9f9"
            out.append(f'    <tr style="background: {bg}; border-bottom: 1px solid #e5e7eb;">')
            for c in r:
                out.append(f'      <td style="padding: 12px 16px; color: #1a1a1a; border: 1px solid #e5e7eb;">{format_inline(c)}</td>')
            out.append("    </tr>")
        out.append("  </tbody>")
        out.append("</table>")
        return "\n".join(out)

    # Default Format 1 / BIT221 table
    out = ['<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">']
    out.append('  <thead style="background-color: #444441; color: #ffffff;">')
    out.append("    <tr>")
    for h in headers:
        out.append(f'      <th style="padding: 10px 12px; text-align: left; border: 1px solid #444441; color: #ffffff;"><strong>{format_inline(h)}</strong></th>')
    out.append("    </tr>")
    out.append("  </thead>")
    out.append("  <tbody>")
    for idx, r in enumerate(data):
        bg = "#ffffff" if idx % 2 == 0 else "#F1EFE8"
        out.append(f'    <tr style="background-color: {bg};">')
        for c in r:
            out.append(f'      <td style="padding: 10px 12px; border: 1px solid #d3d1c7; color: #2c2c2a;">{format_inline(c)}</td>')
        out.append("    </tr>")
    out.append("  </tbody>")
    out.append("</table>")
    return "\n".join(out)


def render_blocks(md_chunk, fmt="f1", dark_bg=False):
    """Render paragraphs, H3/H4, lists, code blocks, callouts, and tables inside a section."""
    lines = md_chunk.splitlines()
    out = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # Code fence
        if stripped.startswith("```"):
            code_lines = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing ```
            escaped_code = html_lib.escape("\n".join(code_lines))
            if fmt == "f2":
                out.append(
                    '<pre style="background: #1e293b; color: #e2e8f0; padding: 18px 20px; border-radius: 6px; '
                    "font-family: 'Courier New', monospace; font-size: 0.85rem; line-height: 1.8; "
                    f'margin: 16px 0 24px 0; overflow-x: auto; white-space: pre-wrap;">{escaped_code}</pre>'
                )
            else:
                out.append(
                    '<pre style="background-color: #2c2c2a; color: #f0ede8; padding: 14px 16px; border-radius: 6px; '
                    "font-family: 'Courier New', monospace; font-size: 0.88rem; line-height: 1.6; "
                    f'margin: 0.75rem 0 1rem 0; overflow-x: auto; white-space: pre-wrap;">{escaped_code}</pre>'
                )
            continue

        # Table
        if stripped.startswith("|") and "|" in stripped[1:]:
            t_lines = []
            while i < n and lines[i].strip().startswith("|"):
                t_lines.append(lines[i])
                i += 1
            out.append(render_table(t_lines, fmt=fmt))
            continue

        # Blockquote callout
        if stripped.startswith(">"):
            q_lines = []
            while i < n and lines[i].strip().startswith(">"):
                q_lines.append(re.sub(r"^>\s?", "", lines[i].strip()))
                i += 1
            q_text = " ".join(q_lines)
            is_blue = bool(re.match(r"^\*\*(?:Info|Note\s*\(Info\)|Reference):", q_text, re.I))
            if fmt == "f2":
                bg, border, txt_c = ("#eff6ff", "#2563eb", "#1e40af") if is_blue else ("#fef3c7", "#d97706", "#92400e")
                out.append(
                    f'<div style="padding: 16px 20px; background: {bg}; border-left: 4px solid {border}; '
                    f'border-radius: 4px; margin: 16px 0;">\n'
                    f'  <p style="margin: 0; font-size: 0.95rem; color: {txt_c};">{format_inline(q_text)}</p>\n'
                    f"</div>"
                )
            else:
                bg, txt_c = ("#E6F1FB", "#185FA5") if is_blue else ("#FAEEDA", "#854F0B")
                q_formatted = format_inline(q_text)
                q_formatted = re.sub(r"^<strong>", f'<strong style="color: {txt_c};">', q_formatted, count=1)
                out.append(
                    f'<div style="background-color: {bg}; padding: 12px 16px; margin: 12px 0; border-radius: 4px;">\n'
                    f'  <p style="margin: 0; font-size: 0.9rem; color: #2c2c2a;">{q_formatted}</p>\n'
                    f"</div>"
                )
            continue

        # Headings H3 / H4
        if stripped.startswith("### "):
            h3_text = format_inline(stripped[4:].strip(), dark_bg=dark_bg)
            if dark_bg:
                out.append(f'<h3 style="color: #9FE1CB; border-top: 1px solid #444441; padding-top: 12px; margin-top: 16px; margin-bottom: 0.75rem;">{h3_text}</h3>')
            elif fmt == "f2":
                out.append(f'<h3 style="color: #1a1a1a; font-size: 1.2rem; margin: 24px 0 12px 0;">{h3_text}</h3>')
            else:
                out.append(f'<h3 style="color: #6b5d4f; margin-top: 1rem; margin-bottom: 0.5rem;">{h3_text}</h3>')
            i += 1
            continue

        if stripped.startswith("#### "):
            h4_text = format_inline(stripped[5:].strip(), dark_bg=dark_bg)
            color = "#9FE1CB" if dark_bg else ("#1a1a1a" if fmt == "f2" else "#2c2c2a")
            out.append(f'<h4 style="color: {color}; margin: 0.75rem 0 0.5rem 0;">{h4_text}</h4>')
            i += 1
            continue

        # Unordered list
        if re.match(r"^[-*]\s+", stripped):
            items = []
            while i < n and re.match(r"^\s*[-*]\s+", lines[i]):
                item_text = re.sub(r"^\s*[-*]\s+", "", lines[i]).strip()
                items.append(f"  <li>{format_inline(item_text, dark_bg=dark_bg)}</li>")
                i += 1
            out.append('<ul style="margin: 0 0 1rem 0; padding-left: 1.5rem;">\n' + "\n".join(items) + "\n</ul>")
            continue

        # Ordered list
        if re.match(r"^\d+\.\s+", stripped):
            items = []
            while i < n and re.match(r"^\s*\d+\.\s+", lines[i]):
                item_text = re.sub(r"^\s*\d+\.\s+", "", lines[i]).strip()
                items.append(f"  <li>{format_inline(item_text, dark_bg=dark_bg)}</li>")
                i += 1
            out.append('<ol style="margin: 0 0 1rem 0; padding-left: 1.5rem;">\n' + "\n".join(items) + "\n</ol>")
            continue

        # Paragraph
        p_lines = []
        while i < n:
            s = lines[i].strip()
            if not s or s.startswith(("```", "|", ">", "### ", "#### ")) or re.match(r"^(?:[-*]|\d+\.)\s+", s):
                break
            p_lines.append(s)
            i += 1
        p_color = " color: #f0ede8;" if dark_bg else ""
        out.append(f'<p style="margin: 0 0 0.75rem 0;{p_color}">{format_inline(" ".join(p_lines), dark_bg=dark_bg)}</p>')

    return "\n".join(out)


def extract_bullets(md_chunk):
    bullets = []
    for line in md_chunk.splitlines():
        m = re.match(r"^\s*(?:[-*]|\d+\.)\s+(.*)", line)
        if m:
            bullets.append(re.sub(r"^[✓✔]\s*", "", m.group(1).strip()))
    return bullets


def build_learning_objectives(md_chunk, fmt="f1"):
    objs = extract_bullets(md_chunk)
    if fmt == "f2":
        items = "\n".join(
            f'    <li style="margin-bottom: 10px; color: #1a1a1a;"><span style="color: #2563eb; margin-right: 8px;">✓</span>{format_inline(o)}</li>'
            for o in objs
        )
        return (
            '<div style="padding: 28px 32px; background: #f9f9f9; border-radius: 8px; border-left: 4px solid #2563eb; margin-bottom: 36px;">\n'
            '  <h2 style="margin: 0 0 16px 0; font-size: 1.25rem; color: #1a1a1a;">Learning Objectives</h2>\n'
            f'  <ul style="list-style: none; padding-left: 0; margin: 0;">\n{items}\n  </ul>\n'
            "</div>"
        )

    cards = "\n".join(
        '    <div style="background-color: #ffffff; border-radius: 6px; padding: 0.75rem 1rem; display: flex; align-items: flex-start; gap: 0.5rem;">\n'
        '      <span style="color: #534ab7; flex-shrink: 0;">✓</span>\n'
        f"      <span>{format_inline(o)}</span>\n"
        "    </div>"
        for o in objs
    )
    return (
        '<div style="background-color: #eeedfe; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #534ab7;">\n'
        '  <div style="background-color: #ddd7f5; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">\n'
        '    <h2 style="margin: 0; font-size: 1.05rem; color: #534ab7;">Learning Objectives</h2>\n'
        "  </div>\n"
        f'  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem;">\n{cards}\n  </div>\n'
        "</div>"
    )


def build_page_or_lecture(meta, sections, template):
    title = normalize_text(meta.get("title", "Untitled Page"))
    week = normalize_text(meta.get("week", ""))
    subtitle = normalize_text(meta.get("subtitle", ""))
    is_f2 = template == "page-f2"
    is_lecture = template == "lecture"
    fmt = "f2" if is_f2 else "f1"

    max_w = "900px" if is_f2 else "860px"
    txt_c = "#1a1a1a" if is_f2 else "#2C2C2A"
    lh = "1.65" if is_f2 else "1.6"

    out = [
        f'<div style="max-width: {max_w}; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, sans-serif; color: {txt_c}; line-height: {lh};">'
    ]

    # Header
    if is_f2:
        week_html = f'  <div style="font-size: 0.85rem; color: #2563eb; margin-bottom: 8px;"><strong>{html_lib.escape(week)}</strong></div>\n' if week else ""
        sub_html = f'  <p style="margin: 8px 0 0 0; font-size: 1.05rem; color: #6b6b6b;">{format_inline(subtitle)}</p>\n' if subtitle else ""
        out.append(
            '<div style="padding: 32px 0 28px 0; border-bottom: 1px solid #e5e7eb; margin-bottom: 36px;">\n'
            f"{week_html}"
            f'  <h1 style="margin: 0; font-size: 2.0rem; color: #1a1a1a;">{html_lib.escape(title)}</h1>\n'
            f"{sub_html}"
            "</div>"
        )
    else:
        week_html = f'  <div style="font-size: 0.8rem; color: #6b6960; margin-bottom: 0.25rem;">{html_lib.escape(week)}</div>\n' if week else ""
        badge_html = (
            '  <div style="margin-top: 0.75rem; font-size: 0.85rem; color: #854f0b; background-color: #faeeda; '
            'display: inline-block; padding: 0.25rem 0.75rem; border-radius: 4px;">Instructor Use Only - Not Published</div>\n'
            if is_lecture
            else ""
        )
        out.append(
            '<div style="background-color: #f1efe8; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #b4b2a9;">\n'
            f"{week_html}"
            f'  <h1 style="margin: 0 0 0.5rem 0; font-size: 1.6rem; color: #2c2c2a;">{html_lib.escape(title)}</h1>\n'
            f"{badge_html}"
            "</div>"
        )

    for sec_title, sec_md in sections:
        if not sec_title:
            if sec_md:
                out.append(render_blocks(sec_md, fmt=fmt))
            continue

        low = sec_title.lower()

        if low == "learning objectives":
            out.append(build_learning_objectives(sec_md, fmt=fmt))

        elif low == "key teaching points":
            bullets = "\n".join(f"    <li>{format_inline(b)}</li>" for b in extract_bullets(sec_md))
            out.append(
                '<div style="background-color: #E6F1FB; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #2980b9;">\n'
                '  <div style="background-color: #d6e0f0; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">\n'
                '    <h2 style="margin: 0; font-size: 1.05rem; color: #185FA5;">Key Teaching Points</h2>\n'
                "  </div>\n"
                f'  <ul style="margin: 0; padding-left: 1.25rem;">\n{bullets}\n  </ul>\n'
                "</div>"
            )

        elif low in ("why this matters", "course intro notes"):
            if is_f2:
                out.append(
                    f'<h2 style="font-size: 1.5rem; color: #1a1a1a; margin: 40px 0 16px 0;">{html_lib.escape(sec_title)}</h2>\n'
                    + render_blocks(sec_md, fmt="f2")
                )
            else:
                out.append(
                    '<div style="background-color: #e1f5ee; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #0F6E56;">\n'
                    '  <div style="background-color: #c8ddd5; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">\n'
                    f'    <h2 style="margin: 0; font-size: 1.05rem; color: #0f6e56;">{html_lib.escape(sec_title)}</h2>\n'
                    "  </div>\n"
                    f"{render_blocks(sec_md, fmt='f1')}\n"
                    "</div>"
                )

        elif low.startswith(("applied:", "discussion:", "common mistakes")) and not is_f2:
            out.append(
                '<div style="background-color: #2c2c2a; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; margin-top: 2rem; color: #f0ede8; border: 1px solid #5DCAA5;">\n'
                '  <div style="background-color: #1a1a1a; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">\n'
                f'    <h2 style="margin: 0; font-size: 1.05rem; color: #9fe1cb;">{html_lib.escape(sec_title)}</h2>\n'
                "  </div>\n"
                f"{render_blocks(sec_md, fmt='f1', dark_bg=True)}\n"
                "</div>"
            )

        elif low == "what's current":
            bullets = "\n".join(f"    <li>{format_inline(b)}</li>" for b in extract_bullets(sec_md))
            out.append(
                '<div style="background-color: #faeeda; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #854F0B;">\n'
                '  <div style="background-color: #f0d4b8; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">\n'
                '    <p style="margin: 0; font-size: 0.8rem; color: #854f0b;"><strong>What\'s Current</strong></p>\n'
                "  </div>\n"
                f'  <ul style="margin: 0; padding-left: 1.25rem; font-size: 0.9rem;">\n{bullets}\n  </ul>\n'
                "</div>"
            )

        elif low in ("reference links", "resources", "references"):
            bullets = "\n".join(f"    <li>{format_inline(b)}</li>" for b in extract_bullets(sec_md))
            label = "Reference Links" if is_lecture else "Resources"
            out.append(
                '<div style="background-color: #e6f0f8; border-radius: 8px; padding: 1.5rem 2rem; border: 1px solid #a8c5db;">\n'
                '  <div style="background-color: #d6e0e8; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">\n'
                f'    <p style="margin: 0; font-size: 0.8rem; color: #5a6f7f;"><strong>{label}</strong></p>\n'
                "  </div>\n"
                f'  <ul style="margin: 0; padding-left: 1.25rem; font-size: 0.9rem;">\n{bullets}\n  </ul>\n'
                "</div>"
            )

        else:
            if is_f2:
                out.append(
                    f'<h2 style="font-size: 1.5rem; color: #1a1a1a; margin: 40px 0 16px 0;">{html_lib.escape(sec_title)}</h2>\n'
                    + render_blocks(sec_md, fmt="f2")
                )
            else:
                out.append(
                    '<div style="background-color: #f5f0e8; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #d4a76a;">\n'
                    '  <div style="background-color: #e5dcc8; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">\n'
                    f'    <h2 style="margin: 0; font-size: 1.05rem; color: #6b5d4f;">{html_lib.escape(sec_title)}</h2>\n'
                    "  </div>\n"
                    f"{render_blocks(sec_md, fmt='f1')}\n"
                    "</div>"
                )

    out.append("</div>")
    return "\n\n".join(out)


def render_purpose_box(sec_md):
    """Render canonical Blue Purpose <table> box with scenario, CLOs, and POs."""
    inner_lines = []
    cur_list = []

    def flush_list():
        if cur_list:
            inner_lines.append("<ul>\n" + "\n".join(f"  <li>{format_inline(x)}</li>" for x in cur_list) + "\n</ul>")
            cur_list.clear()

    for line in sec_md.splitlines():
        s = line.strip()
        if not s:
            flush_list()
            continue
        if s.startswith("### "):
            flush_list()
            heading = normalize_text(s[4:].strip()).rstrip(":")
            inner_lines.append(f"<p><strong>{html_lib.escape(heading)}:</strong></p>")
        elif re.match(r"^[-*]\s+", s):
            cur_list.append(re.sub(r"^[-*]\s+", "", s))
        else:
            flush_list()
            inner_lines.append(f"<p>{format_inline(s)}</p>")
    flush_list()

    body_html = "\n                ".join(inner_lines)
    return (
        '<table style="background-color: #eaf4fb; width: 100%; border-collapse: collapse; border: 2px solid #2980b9;">\n'
        "    <tbody>\n"
        "        <tr>\n"
        '            <td style="padding: 20px;">\n'
        '                <h3 style="color: #1a5276; margin-top: 0;">Purpose</h3>\n'
        f"                {body_html}\n"
        "            </td>\n"
        "        </tr>\n"
        "    </tbody>\n"
        "</table>"
    )


def render_task_box(sec_md):
    paragraphs = [f"<p>{format_inline(p.strip())}</p>" for p in sec_md.split("\n\n") if p.strip()]
    body_html = "\n                ".join(paragraphs)
    return (
        '<table style="background-color: #fef9e7; width: 100%; border-collapse: collapse; margin-top: 15px; border: 2px solid #d4ac0d;">\n'
        "    <tbody>\n"
        "        <tr>\n"
        '            <td style="padding: 20px;">\n'
        '                <h3 style="color: #9a7d0a; margin-top: 0;">Task</h3>\n'
        f"                {body_html}\n"
        "            </td>\n"
        "        </tr>\n"
        "    </tbody>\n"
        "</table>"
    )


def render_criteria_box(sec_md):
    """Render Green Criteria for Success <table> box, guaranteeing an intro <p> before <ul>."""
    intro_lines = []
    bullets = []
    for line in sec_md.splitlines():
        s = line.strip()
        if not s:
            continue
        if re.match(r"^[-*]\s+", s):
            bullets.append(re.sub(r"^[-*]\s+", "", s))
        elif not bullets:
            intro_lines.append(s)

    intro_text = format_inline(" ".join(intro_lines)) if intro_lines else "Your submission will be evaluated on the following criteria:"
    ul_items = "\n".join(f"                    <li>{format_inline(b)}</li>" for b in bullets)
    return (
        '<table style="background-color: #eafaf1; width: 100%; border-collapse: collapse; margin-top: 15px; border: 2px solid #27ae60;">\n'
        "    <tbody>\n"
        "        <tr>\n"
        '            <td style="padding: 20px;">\n'
        '                <h3 style="color: #1e8449; margin-top: 0;">Criteria for Success</h3>\n'
        f"                <p>{intro_text}</p>\n"
        "                <ul>\n"
        f"{ul_items}\n"
        "                </ul>\n"
        "            </td>\n"
        "        </tr>\n"
        "    </tbody>\n"
        "</table>"
    )


def build_assignment(sections):
    """Build canonical 3-box assignment in strict element order:
    1. Purpose -> 2. Task -> 3. Instructions -> 4. Deliverables -> 5. Criteria for Success.
    """
    purpose_html = ""
    task_html = ""
    instructions_parts = []
    deliverables_html = ""
    criteria_html = ""

    for sec_title, sec_md in sections:
        if not sec_title:
            if sec_md:
                instructions_parts.append(render_blocks(sec_md, fmt="f1"))
            continue
        low = sec_title.lower()
        if low == "purpose":
            purpose_html = render_purpose_box(sec_md)
        elif low == "task":
            task_html = render_task_box(sec_md)
        elif low == "deliverables":
            deliverables_html = f'<h3 style="color: #2c2c2a; margin-top: 20px;">Deliverables</h3>\n{render_blocks(sec_md, fmt="f1")}'
        elif low.startswith("criteria"):
            criteria_html = render_criteria_box(sec_md)
        else:
            heading = "" if low == "instructions" else f'<h3 style="color: #2c2c2a; margin-top: 20px;">{html_lib.escape(sec_title)}</h3>\n'
            instructions_parts.append(heading + render_blocks(sec_md, fmt="f1"))

    ordered = [x for x in (purpose_html, task_html, "\n\n".join(instructions_parts), deliverables_html, criteria_html) if x]
    return "\n\n".join(ordered)


def build_lab_notes(meta, sections):
    """Build BIT281/BIT320 5-section left-border Lab Notes page."""
    palette = [
        ("#eaf4fb", "#2980b9", "#1a5276"),  # 1. Why This Matters (Blue)
        ("#eeedfe", "#534AB7", "#534ab7"),  # 2. Core Concept (Purple)
        ("#e6f1fb", "#185FA5", "#185FA5"),  # 3. HOW-TO Guidance (Light Blue)
        ("#fef9e7", "#854F0B", "#854F0B"),  # 4. Key Challenge (Amber)
        ("#eafaf1", "#27ae60", "#1e8449"),  # 5. Workflow / Next Steps (Green)
    ]
    out = [
        '<div style="max-width: 860px; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, sans-serif; color: #2C2C2A; line-height: 1.6;">'
    ]
    idx = 0
    for sec_title, sec_md in sections:
        if not sec_title:
            if sec_md:
                out.append(render_blocks(sec_md, fmt="f1"))
            continue
        bg, border, h_color = palette[min(idx, len(palette) - 1)]
        idx += 1
        out.append(
            f'<div style="background-color: {bg}; border-left: 4px solid {border}; padding: 1.5rem; margin-bottom: 2.5rem;">\n'
            f'  <h2 style="color: {h_color}; margin-top: 0;">{html_lib.escape(sec_title)}</h2>\n'
            f"{render_blocks(sec_md, fmt='f1')}\n"
            "</div>"
        )
    out.append("</div>")
    return "\n\n".join(out)


def compile_markdown(md_text, template_override=None):
    meta, body = parse_frontmatter(md_text)
    template = (template_override or meta.get("template") or "page-f1").lower()
    sections = split_h2_sections(body)
    if template == "assignment":
        return build_assignment(sections), "assignment", meta.get("title", "")
    if template == "lab-notes":
        return build_lab_notes(meta, sections), "page", meta.get("title", "")
    return build_page_or_lecture(meta, sections, template), "page", meta.get("title", "")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("input", help="Input Markdown file")
    ap.add_argument("-o", "--output", required=True, help="Output HTML file")
    ap.add_argument("--template", choices=("page-f1", "page-f2", "lecture", "lab-notes", "assignment"),
                    help="Override template from frontmatter")
    args = ap.parse_args()

    with io.open(args.input, "r", encoding="utf-8") as f:
        md_text = f.read()

    html, lint_type, title = compile_markdown(md_text, args.template)
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with io.open(args.output, "w", encoding="utf-8") as f:
        f.write(html)

    issues = lint_html(html, item_type=lint_type, title=title)
    print(f"BUILT {args.input} -> {args.output} ({len(html):,} chars HTML from {len(md_text):,} chars Markdown)")
    print("  " + format_report(issues))
    if any(i["severity"] == "ERROR" for i in issues):
        sys.exit(1)


if __name__ == "__main__":
    main()
