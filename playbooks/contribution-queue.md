# Contribution Queue Playbook

Use this playbook when a project has a configured healthy-open-contribution
target or the user requests `sweep`, `sweep and replenish`, or `sweep and
replinish`. These invocations are equivalent: every sweep includes Maintain,
Learn, and Replenish unless the user explicitly requests maintenance only. If
no target is configured, use 5 unless current project policy sets a lower
maximum. Read the canonical
[sweep output contract](../references/sweep-output-contract.md) before work
begins.

## Every tick (all three steps — mandatory)

Each scheduled or manual sweep runs **Maintain → Learn → Replenish** in order.
Do not stop after Maintain. Do not emit a status-only report while any step
remains incomplete.

| Step | Every tick |
| --- | --- |
| **Maintain** | All open authored PRs — rebase if stale, **resolve merge conflicts**, fix CI, address actionable review comments (human and bot), push signed commits, produce project-skill sweep action table (one row per PR) |
| **Learn** | Bounded scan: review threads, CI failure shapes, CodeRabbit/Greptile/pre-commit-ci and other bot feedback; departed and peer PRs (merged and closed-without-merge). Adopt durable lessons → project learning log and/or project skill when evidence-backed |
| **Replenish** | Advance missing slots through the full issue screen and contribution recipe. Publish at most one new PR per repository in any rolling 24-hour window by default; record later qualified slots as paced continuation or record a source-backed blocker. |

Then read the project queue policy, current contributor limit, project skill, and
the latest learning log. Refresh limits from live repository policy before
creating work. Use the GitHub access ladder: integration first, authenticated
`gh` after an integration `403`, then public web pages for read-only evidence
if neither authenticated path works. When device login is authorized, start
and complete it yourself; after the device connects, re-check `gh auth
status` in the execution environment and retry the exact operation. Verify
Git transport independently: configure HTTPS with `gh auth setup-git` when
appropriate, and if an OAuth token rejects a workflow-bearing push, probe
the configured fork SSH remote before requesting broader token scope.

## Multi-project sweep orchestration

For `skippy sweep all` or any sweep spanning more than one project, the main
agent must launch one independent local subagent per project in a single
parallel delegation step. Each project subagent owns its complete ordered
lifecycle:

1. Load the Skippy skill, relevant engineering principles and decision rules,
   this playbook, PR maintenance and continuous-learning guidance, the project
   adapter, queue policy, learning log, and current repository instructions.
2. Create or refresh a project-scoped task artifact with an observable
   completion gate and isolated checkout/worktree boundaries.
3. **Maintain:** reconcile departed PRs and fully maintain every authored open
   PR. Inspect live heads, conflicts, signatures, review bodies, latest inline
   thread replies, human and bot comments, CI checks, and raw failure logs.
   Rebase, resolve conflicts, make code/test changes, run project validation,
   commit and push only to the contributor fork, then reply, react, resolve,
   and re-read the exact new head as project policy permits.
4. **Learn and improve:** scan bounded own and peer outcomes, classify evidence,
   update the narrowest skill/log only for a durable lesson, and validate the
   instruction change.
5. **Replenish:** evaluate every eligible missing slot independently. Perform
   complete issue, linked-development, overlap, policy, and evidence screening;
   publish at most one qualified contribution for this repository in any rolling
   24-hour window, retain later qualified work as paced continuation, and record
   a source-backed blocker for unavailable slots. A new sweep does not reset the
   publication window.
6. Draft and validate the user-facing report required by the
   [sweep output contract](../references/sweep-output-contract.md). Return that
   exact eight-column PR table, the Maintain/Learn/Replenish phase table,
   receipts, and external blockers. Do not substitute prose, a PR-link list, or
   the fixed-width operational log summary.

The main agent is the coordinator and integrator. It must not run a serial
all-project Maintain pass before delegation, because that splits ownership,
duplicates Git operations, and makes the later project agent inherit mutable
state it did not produce. The main agent:

- writes complete delegation briefs and assigns one isolated project boundary
  to each subagent;
- waits for every project receipt, reviewing it against live repository
  evidence and the completion gate;
- resumes or restarts a stopped, failed, or incomplete project subagent instead
  of silently omitting that project;
- performs only cross-project integration and safe repair that cannot remain
  project-local; and
- appends one combined summary after every project lifecycle is complete or has
  a concrete external blocker.

Before delegation, create one run ID and prepare every project runtime with
`scripts/sweep-runtime.sh prepare <run-id> <project>`. Include the run ID in
every brief. Project owners
must write phase checkpoints and use their emitted `TMPDIR` and isolated
`SKIPPY_SWEEP_OUTPUT`; helpers must not write the global summary log.

The coordinator must distinguish queued from running work. No startup
checkpoint within three minutes means the owner never started and is replaced
once. Do not describe it as "still running." A started owner gets a 90-minute
hard handoff, one retry per no-progress operation, and at most five minutes of
waiting for external CI or review. On expiry, integrate its partial receipt or
resume token rather than waiting indefinitely.

Run `scripts/sweep-watchdog.py <run-id> --root .skippy/runs` after the startup
window and again before integration. `REPLACE` means the project owner never
started; `HANDOFF` means the active budget expired. Neither state is a reason
for the coordinator to wait.

Routine cleanup follows the selected platform contract. Clean only verified
sweep-owned paths through the runtime adapter; if cleanup is unavailable,
checkpoint `cleanup_deferred`, retain the ignored artifact, and continue.

Do not call `scripts/sweep-all-projects.sh` as the implementation of a full
sweep. It is a maintenance-only compatibility helper and cannot perform review
repair, learning, replenishment, or subagent orchestration.

1. **Maintain:** Reconcile departed contributions and maintain every authored open PR or
   patch. Resolve every contributor-actionable review, CI, conflict, signature,
   and stale-state item for that contribution. If a safe rebase is needed,
   perform it in an isolated worktree, preserve both the current upstream
   structure and the PR's intended behavior, rerun focused proof, and push with
   `--force-with-lease`. Do not rewrite history while a reviewer is requesting
   an unresolved design decision. An active CI run or external
   review on one PR affects only that PR's health; it must not serially block
   independent work in other available slots.

### Rebase conflicts are maintain work (not external blockers)

When `mergeable=CONFLICTING`, GitHub shows a conflict banner, or
`sweep-maintain-pr.sh` logs `REBASE CONFLICT`, the sweep is **not done** for
that PR until you resolve it:

1. Check out the PR branch in an isolated worktree (never the only checkout of
   that branch if the main clone already holds it).
2. Rebase onto upstream default (`main` / `trunk` / `master` per project skill).
3. Resolve every conflict hunk — preserve upstream structure **and** the PR's
   intended behavior (typical: keep both upstream changelog bullets and the PR's
   `## Unreleased` entry; keep upstream refactors plus the PR's fix).
4. Continue the rebase (`GIT_EDITOR=true git rebase --continue` when non-interactive).
5. Run the project skill's focused validation (tests, lint) on the rebased head.
6. Force-push with lease to the fork branch; re-read CI and review state.

Do **not** treat `MAINTAIN #NNNN FAILED` or `gh rebase failed: conflicts` as
"nothing to do on our side." Those mean the bash pre-step stopped; **Skippy
must finish the rebase manually** before reporting the maintain step complete.
Only stop on conflicts when a maintainer has an open unresolved design decision
on the same hunk.

**Push stale info** after a successful local rebase is also maintain work. Retry
with the fork ref captured before rebase (`--force-with-lease`), refetch and
retry once, then `gh pr update-branch --rebase`. Verify with
`gh api repos/OWNER/REPO/compare/<base>...<fork>:<repo>:<branch> --jq .behind_by`
equals `0` before treating a PR as done. Do not report final failure while
GitHub already shows `behind_by=0`.

### Maintain failure recovery (mandatory — fix then continue)

`sweep-maintain.sh` runs a bash pre-step per PR. **Any line below is a work order,
not a sweep stop signal.** Finish the fix, verify on GitHub, then continue the
same tick (other PRs, Learn, Replenish).

| Log signal | Meaning | Skippy must |
| --- | --- | --- |
| `REBASE CONFLICT` / `CONFLICT` | Upstream moved; hunks need manual merge | Worktree → rebase → resolve → validate → push → confirm `mergeable≠CONFLICTING` |
| `PUSH FAILED` / `stale info` | Local rebase OK; lease/push race | Refetch fork OID, retry lease push, then `gh pr update-branch --rebase`; confirm `behind_by=0` |
| `push stale — trying gh pr update-branch` | Script is recovering | Wait for outcome; if still stuck, push manually with fresh lease |
| `gh rebase failed: conflicts` | GitHub agrees there are conflicts | Same as REBASE CONFLICT — manual resolution required |
| `FAILED` (generic) | Pre-step exited non-zero | Read the lines **above** it in `sweep-output.log` for the real cause; fix; re-run maintain for that PR if needed |
| `SKIP` / `clone lock busy` | Parallel maintain on same clone | Serialize: clear stale lock under `.skippy/maintain-locks/` if pid dead, retry |
| `merge=UNKNOWN` in status | GitHub merge state inconclusive | Use `mergeable` + `behind_by` + CI — do not treat as unhealthy by itself |

**Continue rule:** One PR's maintain failure must not end the project sweep.
Fix it (or record a maintainer-design blocker on that PR only), verify, then
proceed to the next PR and to Learn → Replenish.

**Operational sweep log summary:** At the end of a single-project tick, append
its summary directly. This log artifact is separate from and cannot replace the
user-facing report in the
[sweep output contract](../references/sweep-output-contract.md). During a
multi-project sweep, each project subagent returns its row to the main agent
without writing the global table; the main agent appends one combined table
only after reviewing every receipt. Use
`scripts/sweep-log-summary.sh` (fixed-width box table in the log) with columns:
Project, Open, Healthy, Maintain, Action, Self Learning.

For the combined table, pass each reviewed project receipt through
`--verified-row "project|open|target|healthy|maintain|action|lesson"`. This
preserves stricter project evidence such as maintainer-approval-gated workflow
suites that GitHub omits from the ordinary PR status rollup.

- **Maintain:** state the number of rebases, pushes, conflicts resolved, or that
  no branch update was required. Never append `see tick` or another pointer.
- **Action:** use one or two concrete lines covering work actually completed:
  code/test changes, CI diagnosis or retrigger, human/bot review fixes plus
  replies/reactions, rebases, and replenishment outcomes. Never write
  `see SWEEP line` or make the reader inspect another log entry.
- **Self Learning:** use one or two lines stating the durable lesson and the
  exact skill or learning log updated. If no update was warranted, say
  `No skill update:` followed by the evidence-based reason. Do not point to a
  queue policy in place of the lesson.

Do not append this final table after Maintain alone. Complete Learn and
Replenish first so Action and Self Learning describe the whole sweep.

2. **Learn:** Run the bounded continuous-learning scan (see
   [continuous-learning.md](continuous-learning.md)): inspect review comments,
   CI failures, and automated review bots on your open PRs; inspect departed
   PRs (merged and closed-without-merge) and a bounded peer sample. Update the
   project skill or learning log only when the evidence is durable and
   project-specific.
3. **Replenish:** Count only healthy open contributions. Compare the count to the configured
   target, or default target of 5, and the hard maximum. For every missing slot, independently screen issues and linked development:
   read each issue body and comments for explicit PR links; search open PRs by
   issue number, distinctive title phrases, error text, and affected paths; and
   inspect any likely match's state, files, and reviews. Then implement the
   narrow qualified candidate and validate it. By default, select at most one
   candidate per repository for signing and public publication in a rolling
   24-hour window. Immediately before publishing, query live authored PRs in
   open, merged, and closed states and record the newest creation timestamp;
   current open count does not prove the window elapsed. Then inspect the new
   head's review and CI state. Resume another publication only after both the
   window has elapsed and executed CI or maintainer feedback supplies a
   meaningful signal. Explicit batch approval supported by repository evidence
   may override the default. A target count alone is not batch approval. Report
   remaining validated work as paced continuation and exact blockers for
   unavailable slots; do not present local work as an open contribution.

## Replenishment invariants

- A rejected, stale, duplicate, ambiguous, or maintainer-owned candidate is
  evidence about that candidate only. Immediately screen the next candidate;
  it is never a reason to end a sweep while slots remain.
- Do not wait for CI, review, or merge of one contribution before researching,
  implementing, or validating another independent contribution. Do pace public
  publication: one new PR per repository in any rolling 24-hour window by
  default, followed by a meaningful CI or maintainer signal before the next PR.
  Starting a new sweep does not reset the window.
- A failing, rerunning, conflicted, or review-blocked authored PR is its own
  maintenance workstream, not evidence that the whole queue is unhealthy.
  Continue filling independent slots after its safe maintenance action is done.
- Before ending below target, record the complete candidate set screened in
  this run, each concrete disqualifier, and any qualified work deferred by
  publication pacing. "Need maintainer direction" is not a queue-wide blocker;
  continue with local work without creating a burst of public PRs.
- Stop below target only for a verified project/contributor maximum, no
  remaining qualified non-overlapping candidates after the complete screen, or
  a blocking authority/environment condition that prevents every candidate,
  or the default rolling publication limit.

Do not create an additional PR merely to hit a number. The quality bar,
overlap screen, project policy, and truthful evidence gate remain in force.
