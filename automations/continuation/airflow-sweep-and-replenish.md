# Apache Airflow sweep and replenish (scheduled)

Run a complete Skippy sweep and replenish for **apache/airflow**.
Each scheduled tick is one full e2e pass — rebase, maintain, learn, and replenish.

Read:
- `skippy/skippy/SKILL.md`
- `playbooks/contribution-queue.md`
- `references/contribution-quality.md`
- `projects/apache/airflow/SKILL.md`
- `projects/apache/airflow/references/queue-policy.md`
- `projects/apache/airflow/references/learning-log.md`

Local checkout: `/Users/dejain/nvidia/oss/worktrees/apache/airflow` (remotes: `apache`=upstream,
`origin`=fork). Clone or refresh if missing.

Maintain **5 healthy open contributions** for contributor `deepujain` on
[apache/airflow](https://github.com/apache/airflow). Respect maintainer bandwidth
rules in the project skill — fix existing PRs before opening new ones.

Reconcile departed PRs, maintain every authored open PR, run the bounded learning
scan, then advance eligible missing slots with screened, non-overlapping issues.
Publish at most one new Airflow PR in any rolling 24-hour window by default; a
new tick does not reset the window. Record later qualified work as paced
continuation. Update
`projects/apache/airflow/references/queue-policy.md` when queue state changes. Do
not create files under workspace-root `.skippy/`.

**Non-interactive maintenance (required):**
- Rebase stale PR bases onto `apache/main`; push to `origin` with
  `--force-with-lease`.
- Run focused `ruff` and targeted `uv run --project … pytest` when fixing failures.
- Include Gen-AI disclosure in PR bodies when applicable.
- Append summaries via `scripts/sweep-log.sh`.

Complete all three phases. A target count is not batch-publication approval.
Before another PR, require both the elapsed 24-hour window and executed CI or
maintainer feedback. Report paced continuation, source-backed blockers,
completed actions, and exact queue count. Do not stop at a status-only report
while safe local work remains.

Task plan: `.skippy/tasks/airflow-sweep-and-replenish.md`
