# Leaflet contribution queue policy

Target healthy open contributions: 5
Repository or contributor maximum: no lower public cap found at the 2026-09-09 snapshot
Configured by: Skippy default target plus live Leaflet policy scan
Refresh trigger: before every replenishment run and whenever repository policy changes
Default publication cadence: one new PR per rolling 24 hours, followed by executed CI or maintainer feedback; a new sweep does not reset the window

Read the shared `references/contribution-queues.md` policy before acting.

Maintain owned open PRs first. Count only open, reviewable PRs with no unanswered
feedback, avoidable failing checks, merge conflict, or stale branch. For each new
candidate, inspect issue comments and linked development, then search open and
merged PRs by issue number, distinctive title text, error text, and affected
paths. Old accepted or help-wanted labels do not override current-code evidence.

Stop below target when remaining work is duplicated, already fixed, unreproducible,
blocked on API design, too broad for a reviewable contribution, or unsupported by
a focused browser regression. Record the exact blocker and source link rather
than creating quota-driven work. Also stop public publication after the first
new PR in a rolling 24-hour window; retain later qualified work as paced
continuation until the window has elapsed and an executed CI result or
maintainer response supplies a new signal.
