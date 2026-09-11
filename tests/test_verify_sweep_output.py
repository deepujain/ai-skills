from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "verify_sweep_output", ROOT / "scripts" / "verify_sweep_output.py"
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


VALID_REPORT = """# Example Skippy Sweep

Queue: 5/5 open; 4/5 healthy.
Observed: 2026-09-10T12:00:00Z; base: abc123.

| PR | Requested Action Found | CI / Failures | Review Comments | Stale / Merge State | Greptile | Action Taken | Final State |
| --- | --- | --- | --- | --- | --- | --- | --- |
| #1 | None | Passed | coder: informational | Behind 0; mergeable | None | Refreshed | Review required |

| Phase | Result |
| --- | --- |
| Maintain | Refreshed one PR. |
| Learn | No skill update: no durable evidence. |
| Replenish | Verified no-op at target. |

## Validation and receipts

- Receipt.

## External blockers

- None.
"""


class VerifySweepOutputTests(unittest.TestCase):
    def test_valid_report(self) -> None:
        self.assertEqual(MODULE.validate_report(VALID_REPORT), [])

    def test_rejects_different_pr_columns(self) -> None:
        report = VALID_REPORT.replace(" | Greptile", "")
        self.assertIn(
            "PR table must contain the exact eight-column header once",
            MODULE.validate_report(report),
        )

    def test_requires_replenish_result(self) -> None:
        report = VALID_REPORT.replace("| Replenish | Verified no-op at target. |\n", "")
        self.assertIn("missing Replenish phase result", MODULE.validate_report(report))

    def test_requires_eight_cells_in_each_pr_row(self) -> None:
        report = VALID_REPORT.replace(
            "| #1 | None | Passed | coder: informational | Behind 0; mergeable | None | Refreshed | Review required |",
            "| #1 | None | Passed | Review required |",
        )
        self.assertIn(
            "every PR table row must contain exactly eight columns",
            MODULE.validate_report(report),
        )


if __name__ == "__main__":
    unittest.main()
