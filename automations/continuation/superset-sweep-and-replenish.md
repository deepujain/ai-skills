# Apache Superset sweep and replenish (scheduled)

Run a complete Skippy sweep and replenish for **apache/superset**.
Each scheduled tick is one full e2e pass — rebase, maintain, learn, and replenish.

Read:
- `skippy/skippy/SKILL.md`
- `playbooks/contribution-queue.md`
- `references/contribution-quality.md`
- `projects/apache/superset/SKILL.md`
- `projects/apache/superset/references/queue-policy.md`

Local checkout: `/Users/dejain/nvidia/oss/worktrees/apache/superset` (remotes: `apache`=upstream,
`origin`=fork). Clone or refresh if missing.

Maintain **5 healthy open contributions** for contributor `deepujain` on
[apache/superset](https://github.com/apache/superset).

Reconcile departed PRs, maintain every authored open PR, run the bounded learning
scan, then advance eligible missing slots with screened, non-overlapping issues.
Publish at most one new Superset PR in any rolling 24-hour window by default; a
new tick does not reset the window. Record later qualified work as paced
continuation. Update
`projects/apache/superset/references/queue-policy.md` when queue state changes.

**Non-interactive maintenance (required):**
- Rebase stale PR bases onto `apache/master`; push to `origin` with
  `--force-with-lease`.
- Run `pre-commit run` on changed files before push; targeted pytest or Jest
  when fixing failures.
- Append summaries via `scripts/sweep-log.sh superset`.

Complete all three phases. A target count is not batch-publication approval.
Before another PR, require both the elapsed 24-hour window and executed CI or
maintainer feedback. Report paced continuation, source-backed blockers,
completed actions, and exact queue count. Do not stop at a status-only report
while safe local work remains.

Task plan: `.skippy/tasks/superset-sweep-and-replenish.md`
