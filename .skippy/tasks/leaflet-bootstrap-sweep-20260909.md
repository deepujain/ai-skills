# Bootstrap Leaflet and replenish its contribution queue

## Playbook

bootstrap project -> contribution queue

## Done means

- [x] `projects/leaflet/SKILL.md` and its bootstrap references contain source-linked, current repository evidence and pass `./scripts/verify-skill-layout.sh`.
- [x] The Leaflet checkout and GitHub access paths are established without modifying upstream history.
- [x] Maintain, Learn, and Replenish are completed: every authored open Leaflet PR is maintained; durable lessons are recorded only when evidence-backed; each slot up to the live permitted target is filled by a validated non-overlapping PR or has a source-backed blocker.
- [x] Final local and live GitHub state is refreshed after the last mutation and recorded truthfully.

## Constraints to preserve

- [x] Preserve existing uncommitted Skippy changes and add only Leaflet-specific files and task/run evidence.
- [x] Do not modify the canonical Leaflet repository; publish only through the contributor fork.
- [x] Follow Leaflet's live contribution policy, contributor maximum, validation requirements, and maintainer ownership boundaries.
- [x] Do not create duplicate, overlapping, speculative, or low-evidence PRs merely to reach the default target.
- [x] Keep GitHub-facing prose free of U+2014 em dashes and do not expose credentials.

## Task list

- [x] Read Skippy Mode, the engineering decision system, execution/verification contracts, Bootstrap Project, Contribution Queue, PR Maintenance, Continuous Learning, and shared OSS contribution guidance.
- [x] Select `Bootstrap Project -> Contribution Queue` and initialize the executable delivery graph.
- [x] Confirm canonical repository identity, default branch, license, access boundary, authenticated GitHub path, and fork transport.
- [x] Scaffold the Leaflet adapter without overwriting or modifying unrelated Skippy work.
- [x] Read contribution/security/governance policy, templates, CI, manifests, architecture, toolchain, and repository instructions.
- [x] Inspect representative recent merged and closed-unmerged PRs; extract only recurring, source-backed rules.
- [x] Complete `projects/leaflet/SKILL.md`, bootstrap report, queue policy, and learning log; validate the Skippy layout.
- [x] Establish a clean Leaflet checkout and run focused environment/toolchain proof.
- [x] Maintain: inspect every authored open Leaflet PR, including heads, checks, reviews, conflicts, signatures, and linked issue state; perform every safe contributor action.
- [x] Learn: scan bounded own/peer outcomes and update the narrowest Leaflet instruction only when durable evidence warrants it.
- [x] Replenish: refresh live target/maximum, screen candidates and linked development comprehensively, then implement, validate, sign, push, and open each qualified independent PR; retain a concrete disqualifier for every unfilled slot.
- [x] Verify each changed boundary with focused and proportional broad checks, then review every diff for behavior, compatibility, cleanup, generated artifacts, and scope.
- [x] Re-read volatile PR/queue state after the final mutation and record the final summary/receipts.

## Evidence and decisions

| Time | Phase | Decision | Evidence | Result |
| --- | --- | --- | --- | --- |
| 2026-09-09 | Frame | Use the default target of five only if Leaflet's live policy sets no lower maximum. | Skippy contribution-queue policy and user request. | Active |
| 2026-09-09 | Safety | Keep existing dirty Skippy files untouched; confine adapter edits to `projects/leaflet` plus this task/run evidence. | Initial `git status --short`. | Active |
| 2026-09-09 | Method | Use executable graph control because Python is available and the task is non-trivial. | `skippy-graph.py validate` passed for canonical workflow digest `c01072...`. | Initialized |
| 2026-09-09 | Bootstrap | Adopt source-linked Leaflet policy, architecture, toolchain, merged, and closed-unmerged evidence. | Pinned snapshot `3bb9f2bb`; `verify-skill-layout.sh` passed. | Complete |
| 2026-09-09 | Maintain | No authored open Leaflet PRs existed before replenishment. | Connected integration and final `gh` refresh. | No action needed |
| 2026-09-09 | Replenish | Select #4484, #9747, #7105, #3800, and #7389 after current-code and overlap screening. | Every regression failed before its patch and passed afterward; broad checks passed. | Five signed PRs opened |
| 2026-09-09 | Delivery | PRs #10369 through #10373 are open, non-draft, mergeable, and review-required. | GitHub reports all commit signatures valid; no CI checks reported yet. | Target 5 reached |
