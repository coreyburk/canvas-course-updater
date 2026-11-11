#!/usr/bin/env python3
"""Mechanical and structural HTML linter for Canvas pages and assignments.

Enforces the rules from CLAUDE.md and .claude/skills/canvas-html-lint/SKILL.md
deterministically without burning LLM context tokens.

Checks (all items):
  1. NO_EM_DASH_PROSE: Literal U+2014 in prose (outside <pre>) or HTML entity &mdash;/&#8212;.
  2. EM_DASH_IN_PRE:   Literal U+2014 inside <pre> (warning: check if real command vs prose).
  3. NO_STYLE_TAG:     <style> tags (Canvas strips them silently).
  4. NO_INLINE_SVG:    <svg> tags (Canvas strips them silently; use uploaded <img>).
  5. NO_FONT_WEIGHT:   Inline font-weight in style="" on non-<strong>/<th>/<h1>-<h6> tags.
  6. PRE_WRAP:         <pre> tag missing white-space: pre-wrap in style="".
  7. PRE_BALANCE:      Unbalanced <pre> and </pre> tags.
  8. CSS_TYPO:         Common CSS unit typos like '14py' instead of '14px'.

Additional checks when --type assignment (or auto-detected via Criteria for Success box):
  9. CRITERIA_H3_UL:   <h3>Criteria for Success</h3> immediately followed by <ul> with no <p>.
 10. CRITERIA_POINTS:  Point values (e.g. "5 pts", "10 points") inside the Criteria for Success box.
 11. CRITERIA_FINAL:   Content appearing after the closing </table> of the Criteria for Success box.
 12. CRITERIA_TABLE:   Criteria for Success box built with <div> instead of <table>.

Usage:
  python tools/canvas_lint.py path/to/file.html [--type page|assignment|auto]
  python tools/canvas_lint.py --fix path/to/file.html   # auto-fixes prose em dashes & pre-wrap
"""

import argparse
import io
import re
import sys

EM = "\u2014"
PRE_RE = re.compile(r"<pre\b[^>]*>.*?</pre>", re.S | re.I)
PRE_OPEN_RE = re.compile(r"<pre\b([^>]*)>", re.I)
PRE_CLOSE_RE = re.compile(r"</pre\s*>", re.I)
STYLE_TAG_RE = re.compile(r"<\s*style\b", re.I)
SVG_TAG_RE = re.compile(r"<\s*svg\b", re.I)
MDASH_ENTITY_RE = re.compile(r"&mdash;|&#8212;|&#x2014;", re.I)
CSS_TYPO_RE = re.compile(r"\b\d+py\b", re.I)
FONT_WEIGHT_TAG_RE = re.compile(r"<([a-zA-Z0-9]+)\b([^>]*\bstyle\s*=\s*[\"'][^\"']*font-weight\s*:[^\"']*[\"'][^>]*)>", re.I)

CRITERIA_HEADING_RE = re.compile(r"<h3\b[^>]*>\s*Criteria\s+for\s+Success\s*</h3>", re.I)
POINTS_IN_CRITERIA_RE = re.compile(r"\b\d+\s*(?:pts?\b|points?\b)", re.I)


def in_pre_block(html, idx):
    return html.rfind("<pre", 0, idx) > html.rfind("</pre>", 0, idx)


def snippet(html, idx, radius=45):
    s = html[max(0, idx - radius): min(len(html), idx + radius)]
    return re.sub(r"\s+", " ", s).strip()


def find_enclosing_table_or_div(html, heading_start):
    """Locate the container (<table> or <div>) wrapping Criteria for Success."""
    last_table = html.rfind("<table", 0, heading_start)
    last_table_close = html.rfind("</table", 0, heading_start)
    in_table = last_table != -1 and last_table > last_table_close

    if in_table:
        close_m = re.search(r"</table\s*>", html[heading_start:], re.I)
        if close_m:
            end_idx = heading_start + close_m.end()
            return "table", last_table, end_idx, html[last_table:end_idx]
    # Check if wrapped in a div instead
    last_div = html.rfind("<div", 0, heading_start)
    if last_div != -1:
        close_m = re.search(r"</div\s*>", html[heading_start:], re.I)
        if close_m:
            end_idx = heading_start + close_m.end()
            return "div", last_div, end_idx, html[last_div:end_idx]
    return None, heading_start, len(html), html[heading_start:]


def lint_html(html, item_type="auto", title=""):
    """Return a list of dicts: {'severity': 'ERROR'|'WARN', 'rule': str, 'message': str, 'context': str}."""
    issues = []
    html = html or ""

    if title and EM in title:
        issues.append({
            "severity": "ERROR",
            "rule": "NO_EM_DASH_TITLE",
            "message": "Literal em dash (U+2014) in item title",
            "context": title,
        })

    # 1 & 2. Em dashes in prose vs <pre>
    for m in re.finditer(EM, html):
        idx = m.start()
        if in_pre_block(html, idx):
            issues.append({
                "severity": "WARN",
                "rule": "EM_DASH_IN_PRE",
                "message": "Literal em dash inside <pre> block (verify if prose comment vs command)",
                "context": snippet(html, idx),
            })
        else:
            issues.append({
                "severity": "ERROR",
                "rule": "NO_EM_DASH_PROSE",
                "message": "Literal em dash (U+2014) in prose; use space-hyphen-space (' - ')",
                "context": snippet(html, idx),
            })

    for m in MDASH_ENTITY_RE.finditer(html):
        issues.append({
            "severity": "ERROR",
            "rule": "NO_MDASH_ENTITY",
            "message": "HTML em dash entity (%s) found; use space-hyphen-space (' - ')" % m.group(0),
            "context": snippet(html, m.start()),
        })

    # 3. <style> tag
    for m in STYLE_TAG_RE.finditer(html):
        issues.append({
            "severity": "ERROR",
            "rule": "NO_STYLE_TAG",
            "message": "<style> tag found; Canvas strips <style> silently. Use inline style attributes.",
            "context": snippet(html, m.start()),
        })

    # 4. <svg> tag
    for m in SVG_TAG_RE.finditer(html):
        issues.append({
            "severity": "ERROR",
            "rule": "NO_INLINE_SVG",
            "message": "<svg> tag found; Canvas strips inline SVG silently. Use uploaded image via <img>.",
            "context": snippet(html, m.start()),
        })

    # 5. Inline font-weight on non-<strong>/heading/th tags
    for m in FONT_WEIGHT_TAG_RE.finditer(html):
        tag = m.group(1).lower()
        if tag not in ("strong", "th", "h1", "h2", "h3", "h4", "h5", "h6"):
            issues.append({
                "severity": "WARN",
                "rule": "NO_FONT_WEIGHT",
                "message": "Inline font-weight on <%s>; project convention uses <strong> instead" % tag,
                "context": snippet(html, m.start()),
            })

    # 6 & 7. <pre> balance and white-space: pre-wrap
    opens = list(PRE_OPEN_RE.finditer(html))
    closes = list(PRE_CLOSE_RE.finditer(html))
    if len(opens) != len(closes):
        issues.append({
            "severity": "ERROR",
            "rule": "PRE_BALANCE",
            "message": "Unbalanced <pre> tags: %d opening vs %d closing" % (len(opens), len(closes)),
            "context": "",
        })
    for m in opens:
        attrs = m.group(1) or ""
        if "pre-wrap" not in attrs.lower():
            issues.append({
                "severity": "ERROR",
                "rule": "PRE_WRAP",
                "message": "<pre> tag missing 'white-space: pre-wrap' in style attribute",
                "context": snippet(html, m.start()),
            })

    # 8. CSS unit typos (e.g. 14py)
    for m in CSS_TYPO_RE.finditer(html):
        if not in_pre_block(html, m.start()):
            issues.append({
                "severity": "ERROR",
                "rule": "CSS_TYPO",
                "message": "Probable CSS unit typo '%s' (expected 'px')" % m.group(0),
                "context": snippet(html, m.start()),
            })

    # 9-12. Assignment Criteria for Success checks
    cm = CRITERIA_HEADING_RE.search(html)
    is_assignment = item_type == "assignment" or (item_type == "auto" and cm is not None)
    if is_assignment and cm:
        container_tag, _, end_idx, box_html = find_enclosing_table_or_div(html, cm.start())
        if container_tag == "div":
            issues.append({
                "severity": "ERROR",
                "rule": "CRITERIA_TABLE",
                "message": "Criteria for Success box uses <div> instead of canonical <table>",
                "context": snippet(html, cm.start()),
            })
        after_h3 = html[cm.end():end_idx].lstrip()
        if re.match(r"^<\s*ul\b", after_h3, re.I):
            issues.append({
                "severity": "ERROR",
                "rule": "CRITERIA_H3_UL",
                "message": "<h3>Criteria for Success</h3> immediately followed by <ul> without an intro <p> (breaks border rendering)",
                "context": snippet(html, cm.start(), 70),
            })
        for pm in POINTS_IN_CRITERIA_RE.finditer(box_html):
            issues.append({
                "severity": "ERROR",
                "rule": "CRITERIA_POINTS",
                "message": "Point value ('%s') inside Criteria for Success box; points belong only in the rubric" % pm.group(0),
                "context": snippet(box_html, pm.start()),
            })
        trailing = html[end_idx:].strip()
        # Allow closing wrapper tags like </div> if the whole assignment was wrapped, but flag any text/headings/tables
        trailing_stripped = re.sub(r"^(?:\s*</div\s*>)+$", "", trailing, flags=re.I).strip()
        if trailing_stripped:
            issues.append({
                "severity": "ERROR",
                "rule": "CRITERIA_FINAL",
                "message": "Content found after Criteria for Success box (Criteria box must be the final element)",
                "context": re.sub(r"\s+", " ", trailing_stripped[:90]),
            })

    return issues


def auto_fix_html(html):
    """Deterministically fix prose em dashes, &mdash; entities, and <pre> missing pre-wrap."""
    if not html:
        return html, 0
    changes = 0

    def sub_prose(seg):
        nonlocal changes
        n1 = seg.count(EM)
        n2 = len(MDASH_ENTITY_RE.findall(seg))
        changes += n1 + n2
        seg = re.sub(r"\s*" + EM + r"\s*", " - ", seg)
        seg = re.sub(r"\s*(?:&mdash;|&#8212;|&#x2014;)\s*", " - ", seg, flags=re.I)
        return seg

    out, last = [], 0
    for m in PRE_RE.finditer(html):
        out.append(sub_prose(html[last:m.start()]))
        pre_block = m.group(0)
        # Ensure white-space: pre-wrap on <pre> opening tag
        open_m = PRE_OPEN_RE.match(pre_block)
        if open_m and "pre-wrap" not in open_m.group(1).lower():
            attrs = open_m.group(1)
            if re.search(r"\bstyle\s*=\s*\"", attrs, re.I):
                new_attrs = re.sub(r"(\bstyle\s*=\s*\")([^\"]*)\"",
                                   lambda sm: sm.group(1) + sm.group(2).rstrip("; ") + "; white-space: pre-wrap;\"",
                                   attrs, count=1, flags=re.I)
            elif re.search(r"\bstyle\s*=\s*'", attrs, re.I):
                new_attrs = re.sub(r"(\bstyle\s*=\s*')([^']*)'",
                                   lambda sm: sm.group(1) + sm.group(2).rstrip("; ") + "; white-space: pre-wrap;'",
                                   attrs, count=1, flags=re.I)
            else:
                new_attrs = attrs + ' style="white-space: pre-wrap;"'
            pre_block = "<pre" + new_attrs + ">" + pre_block[open_m.end():]
            changes += 1
        out.append(pre_block)
        last = m.end()
    out.append(sub_prose(html[last:]))
    return "".join(out), changes


def format_report(issues, label=""):
    errors = [i for i in issues if i["severity"] == "ERROR"]
    warns = [i for i in issues if i["severity"] == "WARN"]
    prefix = f"[{label}] " if label else ""
    if not issues:
        return f"{prefix}LINT OK (0 errors, 0 warnings)"
    lines = [f"{prefix}LINT: {len(errors)} error(s), {len(warns)} warning(s)"]
    for i in issues:
        lines.append(f"  [{i['severity']}] {i['rule']}: {i['message']}")
        if i.get("context"):
            lines.append(f"          context: ...{i['context']}...")
    return "\n".join(lines)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("files", nargs="+", help="HTML file(s) to lint")
    ap.add_argument("--type", choices=("auto", "page", "assignment"), default="auto")
    ap.add_argument("--fix", action="store_true",
                    help="Auto-fix prose em dashes, &mdash; entities, and missing pre-wrap in place")
    args = ap.parse_args()

    any_errors = False
    for path in args.files:
        with io.open(path, "r", encoding="utf-8") as f:
            html = f.read()
        if args.fix:
            html, n_fixed = auto_fix_html(html)
            if n_fixed:
                with io.open(path, "w", encoding="utf-8") as f:
                    f.write(html)
                print(f"[{path}] Auto-fixed {n_fixed} violation(s).")
        issues = lint_html(html, item_type=args.type)
        print(format_report(issues, label=path))
        if any(i["severity"] == "ERROR" for i in issues):
            any_errors = True

    sys.exit(1 if any_errors else 0)


if __name__ == "__main__":
    main()
