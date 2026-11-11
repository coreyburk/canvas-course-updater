#!/usr/bin/env python3
"""Unit tests for tools/canvas_lint.py and tools/canvas_build.py."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import canvas_lint
import canvas_build

EM = "\u2014"


class TestCanvasLint(unittest.TestCase):
    def test_clean_page_has_zero_issues(self):
        html = (
            '<div style="max-width: 860px;">'
            "<p>Clean prose - no em dashes here.</p>"
            '<pre style="white-space: pre-wrap;">echo "hello"</pre>'
            "</div>"
        )
        self.assertEqual(canvas_lint.lint_html(html, item_type="page"), [])

    def test_detects_em_dash_in_prose_vs_pre(self):
        html = (
            f"<p>Prose with {EM} em dash.</p>"
            f'<pre style="white-space: pre-wrap;"># comment {EM} inside code</pre>'
        )
        issues = canvas_lint.lint_html(html, item_type="page")
        rules = [i["rule"] for i in issues]
        self.assertIn("NO_EM_DASH_PROSE", rules)
        self.assertIn("EM_DASH_IN_PRE", rules)

    def test_detects_style_svg_and_pre_wrap(self):
        html = "<style>body{}</style><svg></svg><pre>code</pre>"
        rules = {i["rule"] for i in canvas_lint.lint_html(html, item_type="page")}
        self.assertIn("NO_STYLE_TAG", rules)
        self.assertIn("NO_INLINE_SVG", rules)
        self.assertIn("PRE_WRAP", rules)

    def test_detects_assignment_criteria_violations(self):
        bad_assignment = (
            '<table style="background-color: #eafaf1;"><tbody><tr><td>'
            "<h3>Criteria for Success</h3>"
            "<ul><li>Criterion 1 (5 pts)</li></ul>"
            "</td></tr></tbody></table>"
            "<p>Deliverables after criteria box</p>"
        )
        rules = {i["rule"] for i in canvas_lint.lint_html(bad_assignment, item_type="assignment")}
        self.assertIn("CRITERIA_H3_UL", rules)
        self.assertIn("CRITERIA_POINTS", rules)
        self.assertIn("CRITERIA_FINAL", rules)

    def test_auto_fix_preserves_pre_content_and_adds_pre_wrap(self):
        html = f'<p>Hello{EM}world &mdash; test</p><pre style="color: #fff;">cmd {EM} arg</pre>'
        fixed, count = canvas_lint.auto_fix_html(html)
        self.assertEqual(count, 3)
        self.assertIn("<p>Hello - world - test</p>", fixed)
        self.assertIn("white-space: pre-wrap;", fixed)
        self.assertIn(f"cmd {EM} arg</pre>", fixed)


class TestCanvasBuild(unittest.TestCase):
    def test_compile_page_f1_is_lint_clean(self):
        md = f"""---
template: page-f1
title: Network Cabling {EM} Physical Connectivity
week: Week 1 - Networking Fundamentals
---
## Learning Objectives
- Identify fiber and copper cable types
- Verify link status on switches

## Why This Matters
Physical layer issues cause most outages {EM} check Layer 1 first.

## Core Concepts
### Twisted Pair Standards
| Category | Speed | Max Distance |
|---|---|---|
| Cat6 | 10 Gbps | 55m |
| Cat6A | 10 Gbps | 100m |

> **Pro tip:** Always label both ends of a patch cable.

```bash
show interfaces status
```

## Applied: Verifying Interfaces
Run `show ip interface brief` to inspect status.

## Resources
- [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918) - Private Address Allocation
"""
        html, lint_type, title = canvas_build.compile_markdown(md)
        self.assertEqual(lint_type, "page")
        self.assertNotIn(EM, html)
        self.assertEqual(canvas_lint.lint_html(html, item_type=lint_type), [])
        self.assertIn("#eeedfe", html)  # Learning objectives purple
        self.assertIn("#e1f5ee", html)  # Why this matters green
        self.assertIn("#2c2c2a", html)  # Applied dark charcoal

    def test_compile_page_f2_is_lint_clean(self):
        md = """---
template: page-f2
title: Static Routing Fundamentals
week: Week 6 | Page 1
subtitle: Forwarding tables, longest prefix match, and administrative distance
---
## Learning Objectives
- Read `show ip route` output
- Configure next-hop and floating static routes

## Forwarding Sequence
> **Info:** Longest prefix match is evaluated before administrative distance.

```text
Router(config)# ip route 10.0.0.0 255.255.255.0 192.168.1.1
```
"""
        html, lint_type, _ = canvas_build.compile_markdown(md)
        self.assertEqual(canvas_lint.lint_html(html, item_type=lint_type), [])
        self.assertIn("max-width: 900px", html)
        self.assertIn("#2563eb", html)

    def test_compile_assignment_enforces_canonical_order_and_lint_clean(self):
        # Even if Deliverables is placed after Criteria in Markdown, build_assignment orders Criteria last!
        md = """---
template: assignment
title: Lab 1.1: Infrastructure Setup
---
## Purpose
In production environments, engineers validate their scripting toolchains before deploying automation.

### Course Learning Outcomes
- Configure multi-language scripting environments

### Program Outcomes
- Design and implement secure systems

## Task
Install and verify Bash, PowerShell, and Python on your workstation.

## Instructions
1. Open terminal and check versions. [SCREENSHOT]
2. [HINT] Use `python --version` to verify.

## Criteria for Success
- All three scripting environments are installed and verified
- Screenshots are clearly labeled

## Deliverables
- Submit a single PDF document with all required screenshots
"""
        html, lint_type, _ = canvas_build.compile_markdown(md)
        self.assertEqual(lint_type, "assignment")
        issues = canvas_lint.lint_html(html, item_type="assignment")
        self.assertEqual(issues, [])
        # Verify Deliverables appears BEFORE Criteria for Success in output HTML
        self.assertLess(html.index("Deliverables"), html.index("Criteria for Success"))
        self.assertIn("camera.png", html)
        self.assertIn("background-color: #ffff00;", html)


if __name__ == "__main__":
    unittest.main()
