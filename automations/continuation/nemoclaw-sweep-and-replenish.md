# NemoClaw sweep and replenish (scheduled)

Run a complete Skippy sweep and replenish for **nemoclaw**.
Each scheduled tick is one full e2e pass — rebase, maintain, learn, and replenish.

Read:
- `skippy/skippy/SKILL.md`
- `playbooks/contribution-queue.md`
- `references/contribution-quality.md`
- `projects/nemoclaw/SKILL.md`
- `projects/nemoclaw/references/queue-policy.md`

Local checkout: `/Users/dejain/nvidia/oss/worktrees/nvidia/nemoclaw` (clone or refresh if missing).

Maintain **5 healthy open contributions** for contributor `deepujain` on
`NVIDIA/NemoClaw`. Follow the full NemoClaw PR recipe for maintenance and
replenishment, including the sweep table format in the project skill.

Reconcile departed PRs, maintain every authored open PR, run the bounded learning
scan, then advance each eligible missing slot. Publish at most one new NemoClaw
PR in any rolling 24-hour window by default; a new tick does not reset the
window. Record later qualified work as paced continuation. Update
`projects/nemoclaw/references/queue-policy.md` when queue state changes.
Do not create files under workspace-root `.skippy/`.

**Non-interactive maintenance (required for scheduled runs):**
- Rebase stale PR bases with `gh pr update-branch --rebase` first; only fall back
  to local worktree rebase + SSH `--force-with-lease` when GitHub rebasing fails.
- Do not modify global git config; use existing NemoClaw signing setup in the
  checkout/worktree.
- Run all status, CI, and maintenance commands without asking for approval.

Complete all three phases. A target count is not batch-publication approval.
Before another PR, require both the elapsed 24-hour window and executed CI or
maintainer feedback. Report paced continuation, source-backed blockers,
completed actions, and exact queue count. Do not stop at a status-only report
while safe local work remains.

Task plan: `.skippy/tasks/nemoclaw-sweep-and-replenish.md`
