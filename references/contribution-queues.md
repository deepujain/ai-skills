# Contribution Queue Policy

A contribution queue keeps a project supplied with independently healthy open
PRs or patches. It is not a license to create duplicate work or ignore a
contributor-actionable problem on an existing branch.

## Project policy

Each project may configure `projects/<slug>/references/queue-policy.md` with:

```markdown
# <Project> contribution queue policy

Target healthy open contributions: <X>
Repository or contributor maximum: <Y or unknown>
Configured by: <policy source or user decision>
Refresh trigger: <when target/limit must be rechecked>
```

The target is a desired number of healthy, non-overlapping contributions. The
maximum is a hard limit verified from current project policy. If no target is
configured, use a default target of **5**, unless current project policy sets a
lower maximum. If target or maximum conflict with live policy, live policy wins.

## Healthy means

A contribution counts toward the target only when it has an open source PR or
patch and no remaining contributor-actionable conflict, review finding,
signature defect, failed in-scope validation, or unaddressed stale state. A
maintainer-only runner gate may be accurately recorded without freezing
independent replenishment, but it is never described as green.

## Independence rule

Treat each open contribution as its own workstream. A failed CI run, review
finding, stale base, merge block, or maintainer-only gate makes that PR
unhealthy and requires its own repair or classification. It does **not** pause
candidate discovery, implementation, validation, or publication for another
independent slot.

Continue replenishing after the affected PR has been handled or accurately
classified. Stop the whole queue below target only when the same blocker applies
to every remaining slot: a verified project or contributor maximum, missing
publication authority, a shared environment failure, or no qualified
non-overlapping candidate after a complete screen.

## Sweep and replenish procedure

1. Reconcile departed contributions. Inspect their final state and source
   evidence before calling a closure a lesson.
2. Maintain every open authored contribution first: reviews, check failures,
   conflicts, signatures, current-head state, and source policy changes.
3. Run the bounded continuous-learning scan for new outcomes that affect the
   next decision.
4. Count healthy open contributions against the configured target, or the
   default target of 5, and the verified maximum.
5. For each missing slot, screen candidates for issue/PR/file overlap and linked
   development, then complete local implementation and validation independently.
6. Immediately before publication, query live authored PRs in that repository,
   including open, merged, and closed states, and record the newest creation
   timestamp. Do not infer cadence from the current open count.
7. Publish at most one new PR per repository in any rolling 24-hour window by
   default. Starting a new sweep does not reset the window. A target count is not
   batch-publication approval. Before publishing again, require both the elapsed
   window and executed CI or maintainer feedback; explicit batch approval backed
   by repository evidence may override the default.
8. Stop when the target or maximum is reached, no qualified non-overlapping
   candidate remains, a concrete external blocker applies, or the sweep's
   publication limit is reached.
9. Record each slot as open, paced continuation, in progress, or unavailable
   with evidence. A candidate list, local branch, or status-only report never
   fills a slot.

## Scheduling

When a client provides a scheduler, use the project-specific target and the
[sweep-and-replenish continuation prompt](../automations/continuation/sweep-and-replenish-prompt.md).
The scheduler replays the task; it does not grant broader authority. It may
maintain and create contributions only within the configured target, project
policy, and user-granted publication authority.
