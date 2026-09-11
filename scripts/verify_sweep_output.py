#!/usr/bin/env python3
"""Validate the mandatory user-facing Skippy sweep report structure."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PR_HEADER = (
    "| PR | Requested Action Found | CI / Failures | Review Comments | "
    "Stale / Merge State | Greptile | Action Taken | Final State |"
)
PR_SEPARATOR = "| --- | --- | --- | --- | --- | --- | --- | --- |"
PHASE_HEADER = "| Phase | Result |"
PHASE_SEPARATOR = "| --- | --- |"
REQUIRED_PHASES = ("Maintain", "Learn", "Replenish")
REQUIRED_SECTIONS = ("## Validation and receipts", "## External blockers")


def validate_report(text: str) -> list[str]:
    """Return human-readable contract violations."""
    lines = [line.rstrip() for line in text.splitlines()]
    errors: list[str] = []

    if not lines or not re.fullmatch(r"# .+ Skippy Sweep", lines[0]):
        errors.append("first line must be '# <Project> Skippy Sweep'")
    count = r"(?:\d+|unknown)"
    if not any(
        re.fullmatch(rf"Queue: {count}/\d+ open; {count}/\d+ healthy\.", line)
        for line in lines
    ):
        errors.append("missing exact queue summary")
    if not any(line.startswith("Observed: ") and "; base: " in line for line in lines):
        errors.append("missing observed timestamp and base revision")

    if lines.count(PR_HEADER) != 1:
        errors.append("PR table must contain the exact eight-column header once")
    elif lines.index(PR_HEADER) + 1 >= len(lines) or lines[lines.index(PR_HEADER) + 1] != PR_SEPARATOR:
        errors.append("PR table separator does not match the eight-column contract")
    else:
        row_index = lines.index(PR_HEADER) + 2
        if row_index >= len(lines) or not lines[row_index].startswith("|"):
            errors.append("PR table must contain at least one row")
        else:
            pr_rows = []
            while row_index < len(lines) and lines[row_index].startswith("|"):
                pr_rows.append(lines[row_index])
                row_index += 1
            if any(len(row.split("|")[1:-1]) != 8 for row in pr_rows):
                errors.append("every PR table row must contain exactly eight columns")

    if lines.count(PHASE_HEADER) != 1:
        errors.append("phase table must contain the exact header once")
    elif lines.index(PHASE_HEADER) + 1 >= len(lines) or lines[lines.index(PHASE_HEADER) + 1] != PHASE_SEPARATOR:
        errors.append("phase table separator is invalid")

    for phase in REQUIRED_PHASES:
        if not any(re.match(rf"\| {re.escape(phase)} \| .+ \|$", line) for line in lines):
            errors.append(f"missing {phase} phase result")
    for section in REQUIRED_SECTIONS:
        if lines.count(section) != 1:
            errors.append(f"missing required section: {section}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", help="Markdown report path, or - for stdin")
    args = parser.parse_args()
    text = sys.stdin.read() if args.report == "-" else Path(args.report).read_text(encoding="utf-8")
    errors = validate_report(text)
    if errors:
        for error in errors:
            print(f"sweep output contract: {error}", file=sys.stderr)
        return 1
    print("Skippy sweep output verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
