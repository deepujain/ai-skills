# Leaflet learning log

## 2026-09-09 bootstrap scan

- Scope discipline is unusually explicit. PR #10352 shows that maintainers may
  close otherwise relevant work when it includes unrelated import, declaration,
  or cleanup churn. Apply this to every Leaflet diff.
- Labels and old issue checklists can be stale. Issue #8477 remained open after
  PR #10227 completed its remaining browser-language updates, and issue #10046
  remained discoverable after PR #10072 merged its deduplication. Verify current
  source and merged history before claiming work.
- Browser compatibility claims require specification evidence. PR #10249 shows
  that a documentation deprecation banner is not sufficient grounds for changing
  behavior.
- Source asset ownership and build copying matter. PR #9665 kept the SVG in the
  source tree and taught the build to copy it; proposed extra asset changes were
  removed after measurement did not justify them.
- Closed status alone is not a lesson. PR #10251 had no explanatory discussion,
  so its closure reason remains unknown.

Sources: [#10352](https://github.com/Leaflet/Leaflet/pull/10352),
[#8477](https://github.com/Leaflet/Leaflet/issues/8477),
[#10227](https://github.com/Leaflet/Leaflet/pull/10227),
[#10046](https://github.com/Leaflet/Leaflet/issues/10046),
[#10072](https://github.com/Leaflet/Leaflet/pull/10072),
[#10249](https://github.com/Leaflet/Leaflet/pull/10249),
[#9665](https://github.com/Leaflet/Leaflet/pull/9665),
[#10251](https://github.com/Leaflet/Leaflet/pull/10251).

## 2026-09-09 sweep

- An empty check rollup is not evidence that CI never matched a PR. The five
  fork PRs #10369 through #10373 each have a completed Actions run with
  conclusion `action_required`, while the checks page reports `Workflow runs
  completed with no jobs`. Treat this shape as an external workflow gate: it is
  neither a contributor code failure nor green CI. Inspect Actions runs by head
  SHA before classifying an empty check rollup.
- No reviewer or code lesson was adopted. All five heads had no human reviews,
  bot reviews, inline comments, or issue comments, and upstream `main` had not
  moved since the bootstrap snapshot.

Sources: [#10369 run](https://github.com/Leaflet/Leaflet/actions/runs/34417692542),
[#10370 run](https://github.com/Leaflet/Leaflet/actions/runs/34417693348),
[#10371 run](https://github.com/Leaflet/Leaflet/actions/runs/34417692509),
[#10372 run](https://github.com/Leaflet/Leaflet/actions/runs/34417694948),
[#10373 run](https://github.com/Leaflet/Leaflet/actions/runs/34417695684).

## 2026-09-10 sweep

- Maintainer feedback on PR #10373 explicitly connected five PRs submitted in
  a short period, each with the same two-paragraph narrative shape, to an
  authenticity concern. Treat the configured queue target as paced inventory,
  not a burst quota: publish at most one new Leaflet PR in any rolling 24-hour
  window, which a new sweep does not reset, and require executed CI or
  maintainer feedback before the next.
- Do not respond by cosmetically varying paragraph counts. Compare prospective
  bodies with recent authored PRs and make each description follow its distinct
  failure, root cause, owning change, preserved behavior, proof, and risk.

Source: [PR #10373 maintainer comment](https://github.com/Leaflet/Leaflet/pull/10373#issuecomment-5619108743).
