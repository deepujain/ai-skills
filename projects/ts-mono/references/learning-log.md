# ts-mono learning log

## 2026-09-10: distinguish worktree serialization from package concurrency

Sources: `/Users/dejain/nvidia/oss/.skippy/tasks/ts-mono-sweep-20260910-172611.md`
and https://github.com/meridianlabs-ai/ts-mono/pull/632
Classification: repeated local validation behavior with a pending peer repair
Observation: After sibling worktree suites were serialized, the first cold
root runs on #569 and #570 still timed out in Scout
`useColumnSizing.test.ts` because one Turbo graph runs package tests
concurrently. The exact file passed 10/10 in isolation and each unchanged
branch then passed all 9 root tasks. Open peer PR #632 independently replaces
the dynamic hook import, but that repair is not yet accepted on `main`.
Adopted rule: Serialize full graphs across worktrees, but classify this exact
current-main timeout with an isolated-file proof and one branch rerun. Do not
transplant the pending fixture change into unrelated PRs.
Next action: Remove the baseline-workaround guidance if the fixture repair
lands on `main`; until then, require both rerun proofs and exact-head hosted CI.

## 2026-09-10: serialize full-workspace tests across local worktrees

Sources: `/Users/dejain/nvidia/oss/.skippy/tasks/ts-mono-sweep.md` and
`/Users/dejain/nvidia/oss/.skippy/tasks/ts-mono-sweep-20260910-102212.md`
Classification: repeated local validation behavior
Observation: Two parallel multi-worktree root test passes produced unrelated
Scout hook timeouts. In the latest pass,
`useColumnSizing.test.ts` timed out during the #628 root run, then passed 10/10
in isolation and the unchanged branch passed all 9 root test tasks when rerun
alone.
Adopted rule: Run full `pnpm test` graphs serially across local worktrees. If a
hook timeout appears under shared-host contention, rerun the exact test file in
isolation and then rerun that branch alone before treating it as a code defect.
Next action: Keep focused tests parallel when safe, but serialize full workspace
test graphs during future ts-mono sweeps.

## 2026-09-09: defend log-authored input at shared boundaries

Sources: https://github.com/meridianlabs-ai/ts-mono/pull/621 and
https://github.com/meridianlabs-ai/ts-mono/pull/622
Classification: accepted peer outcomes
Observation: Two recent security fixes were accepted by filtering dangerous
prototype keys at the normalization boundary and hardening the shared rendered
HTML and link sanitizer, with focused boundary regressions.
Adopted rule: When log-authored data can reach several consumers, enforce the
security invariant at the earliest shared normalization or consumption seam
and exercise alternate representations in tests rather than patching one UI.
Next action: Apply this rule to future log, journal, URL, and rendered-content
work, while preserving transport-specific behavior at the boundary.

## 2026-09-04: refresh the owning seam before reviving stale work

Source: https://github.com/meridianlabs-ai/ts-mono/pull/373#issuecomment-5516404723
Classification: authoritative maintainer direction
Observation: A security-hardening PR was closed after the viewer bootstrap and
data layer moved; 23 of 36 files conflicted. The maintainer preserved the goal
as issue #615 and explicitly requested a smaller implementation at
`app_config/resolveAppConfig()`.
Adopted rule: Re-trace current ownership before reviving an old implementation;
when architecture moved, implement the preserved contract at the new seam
instead of rebasing a broad stale diff.
Next action: Screen issue #615 from current `main` and use the old PR only as
policy and test-design evidence.

## 2026-09-04: generated API work must be current and coordinated

Source: https://github.com/meridianlabs-ai/ts-mono/pull/477#issuecomment-5134712465
Classification: verified duplicate outcome
Observation: A generated-type PR became empty after equivalent work landed on
`main`; the accepted change also updated the other generated copy and fixtures
that the stale PR omitted.
Adopted rule: Immediately before generated API work, diff current `main` and
check both app-specific generated surfaces plus their fixtures and parent
repository schema state.
Next action: Close or avoid a generated-only candidate when current `main`
already contains the schema output.

## 2026-09-04: distinguish dependency updates from migrations

Source: https://github.com/meridianlabs-ai/ts-mono/pull/535#issuecomment-5327866807
Classification: authoritative maintainer direction and verified CI failure
Observation: A routine major-version Dependabot PR broke the API across both
apps and was closed with an ignore instruction because the update required a
deliberate migration.
Adopted rule: If a major dependency bump changes public APIs across workspaces,
screen it as a migration with explicit direction and both app e2e lanes, not as
a routine lockfile update.
Next action: Reject unattended major-bump candidates whose required code
migration is not separately approved.
