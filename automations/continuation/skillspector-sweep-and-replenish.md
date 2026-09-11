# SkillSpector sweep and replenish (scheduled)

Run a complete Skippy sweep and replenish for **skillspector**.
Each scheduled tick is one full e2e pass — rebase, maintain, learn, and replenish.

Read:
- `skippy/skippy/SKILL.md`
- `playbooks/contribution-queue.md`
- `references/contribution-quality.md`
- `projects/skillspector/SKILL.md`
- `projects/skillspector/references/queue-policy.md`
- `projects/skillspector/references/learning-log.md`

Local checkout: `/Users/dejain/nvidia/oss/worktrees/nvidia/skillspector` (clone or refresh if missing).

Maintain **5 healthy open contributions** for contributor `deepujain` on
`NVIDIA/SkillSpector`. Use the GitHub access ladder; prefer `gh` when authenticated.

Reconcile departed PRs, maintain every authored open PR, run the bounded learning
scan, then advance each eligible missing slot. Publish at most one new
SkillSpector PR in any rolling 24-hour window by default; a new tick does not
reset the window. Record later qualified work as paced continuation. Update only
`projects/skillspector/references/queue-policy.md` for durable queue state.
Do not create files under workspace-root `.skippy/`.

**Non-interactive maintenance (required for scheduled runs):**
- Rebase stale PR bases with `gh pr update-branch --rebase` first; do not open
  local worktrees or force-push unless GitHub rebasing fails.
- Do not modify global git config; rely on existing repo/worktree signing setup.
- Run all status, CI, and maintenance commands without asking for approval.

Complete all three phases. A target count is not batch-publication approval.
Before another PR, require both the elapsed 24-hour window and executed CI or
maintainer feedback. Report paced continuation, source-backed blockers,
completed actions, and exact queue count. Do not stop at a status-only report
while safe local work remains.

Task plan: `.skippy/tasks/skillspector-sweep-and-replenish.md`
