#!/usr/bin/env python3
"""
Tests for emdash_sweep.fix().

The thing worth protecting is simple: course content lives in Canvas, and a
bad substitution inside a <pre> block silently corrupts a command students are
meant to copy. These tests pin down that <pre> content survives byte-for-byte
unless --include-pre is explicitly requested.

Run:
    python tools/test_emdash_sweep.py
"""

import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "sweep", os.path.join(HERE, "emdash_sweep.py"))
sweep = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sweep)

EM = "—"
failures = []


def check(name, got, want):
    if got == want:
        print("  %-52s PASS" % name)
    else:
        failures.append(name)
        print("  %-52s FAIL" % name)
        print("     got : %r" % (got,))
        print("     want: %r" % (want,))


def main():
    print("emdash_sweep.fix()")

    check("prose only is fixed",
          sweep.fix("alpha " + EM + " beta")[:2], ("alpha - beta", 1))

    body = "<p>intro</p><pre>grep " + EM + " foo</pre><p>outro</p>"
    new, fixed, left = sweep.fix(body)
    check("pre-only content preserved byte-for-byte", new, body)
    check("pre-only hit counted as left behind", (fixed, left), (0, 1))

    body = ("<p>a " + EM + " b</p><pre>cmd " + EM + " x</pre><p>c" + EM + "d</p>")
    new, fixed, left = sweep.fix(body)
    check("mixed: code blocks unchanged",
          sweep.pre_blocks(new), sweep.pre_blocks(body))
    check("mixed: counts", (fixed, left), (2, 1))
    check("mixed: nothing left outside pre",
          sum(1 for i, ch in enumerate(new)
              if ch == EM and not sweep.in_code_block(new, i)), 0)

    new, fixed, left = sweep.fix(body, include_pre=True)
    check("include_pre rewrites everything", (new.count(EM), left), (0, 0))

    body = ('<pre style="x">a' + EM + '</pre>mid ' + EM + ' <pre>b' + EM + '</pre>')
    new, fixed, left = sweep.fix(body)
    check("multiple pre blocks with attributes preserved",
          sweep.pre_blocks(new), sweep.pre_blocks(body))
    check("multiple pre blocks: counts", (fixed, left), (1, 2))

    check("None is safe", sweep.fix(None), (None, 0, 0))
    check("empty string is safe", sweep.fix(""), ("", 0, 0))

    # whitespace around the dash collapses to exactly one space-hyphen-space
    check("newline-hugging dash collapses",
          sweep.fix("a\n" + EM + "\nb")[0], "a - b")

    print("\nFAILURES: %d" % len(failures))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
