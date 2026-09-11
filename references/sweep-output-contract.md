# Sweep Output Contract

Use this contract for every manual or scheduled Skippy contribution-queue
sweep. It is the single source of truth for both command meaning and the final
user-facing report.

## Command meaning

`skippy sweep`, `sweep` in an active project thread, `skippy sweep and
replenish`, and the common misspelling `skippy sweep and replinish` all mean one
complete ordered pass:

1. Maintain every authored open contribution.
2. Learn from bounded current evidence.
3. Replenish every eligible missing queue slot under current project policy and
   publication pacing.

Replenishment is the default, not an optional follow-up. If the queue is
already at its target, record a verified no-op. Skip replenishment only when
the user explicitly requests a maintenance-only run. Never stop after Maintain
and wait for the user to say `continue`.

## Mandatory final response

Draft the final response in a Markdown file, validate it with
`python3 scripts/verify_sweep_output.py <file>`, and return the validated content
without changing its headings or table columns.

Use exactly this structure:

```markdown
# <Project> Skippy Sweep

Queue: <open>/<target> open; <healthy>/<target> healthy.
Observed: <ISO-8601 timestamp>; base: <upstream revision or unavailable with reason>.

| PR | Requested Action Found | CI / Failures | Review Comments | Stale / Merge State | Greptile | Action Taken | Final State |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <PR link or None> | <action or none> | <exact state> | <reviewers and disposition> | <behind/conflict/merge state> | <result or none> | <completed action> | <terminal or external state> |

| Phase | Result |
| --- | --- |
| Maintain | <concrete completed maintenance and remaining external state> |
| Learn | <durable lesson and exact skill/log update, or why no update was warranted> |
| Replenish | <opened contribution, verified no-op at target, paced continuation, or blocker for each missing slot> |

## Validation and receipts

- <focused and broad validation, signatures, remote receipts, and artifact links>

## External blockers

- <exact external blocker and owner, or None.>
```

## Reporting rules

- Include one row for every authored open PR. Use a single `None` row only when
  there are no open PRs.
- Keep the eight PR-table headings exact and in order. `Greptile` remains its
  own column even when the result is `None` or `Unavailable`.
- In `Review Comments`, identify each human or bot reviewer and state whether
  its feedback is addressed, informational, stale, unresolved, or externally
  blocked. A count alone is insufficient.
- Distinguish local validation from hosted CI. Do not call pending, skipped,
  unavailable, or approval-gated checks green.
- Report both current behind/conflict state and GitHub merge state. A review
  requirement is not a merge conflict.
- `Action Taken` reports completed work, not planned work. `Final State` reports
  the remaining public state without claiming maintainer-owned completion.
- The phase table is required even when a phase made no changes. It prevents a
  maintenance-only result from masquerading as a complete sweep.
- Put task artifacts, graph receipts, commits, and other evidence under
  `Validation and receipts`; do not replace the PR table with an artifact list.
- Put only genuine external dependencies under `External blockers`. If none
  remain, write `- None.`

The fixed-width project summary written to `.skippy/sweep-output.log` is an
operational log artifact. It does not replace this user-facing report.
