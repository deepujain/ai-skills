---
name: leaflet
description: Evidence-backed contribution workflow for Leaflet. Use for issue selection, implementation, validation, PR maintenance, and queue replenishment in Leaflet/Leaflet.
---

# Leaflet Contribution Skill

Canonical repository: https://github.com/Leaflet/Leaflet
Bootstrap snapshot: `3bb9f2bbf897fcfee54c8b1d9bba804297ae7fe4` (2026-09-09)

Read [the shared contribution protocol](../../references/contribution-quality.md),
[the bootstrap report](references/bootstrap-report.md), and
[the queue policy](references/queue-policy.md) before selecting or changing an
issue. Add durable outcome evidence to
[the learning log](references/learning-log.md).
Every Leaflet `sweep` includes Maintain, Learn, and Replenish and must use the
shared [sweep output contract](../../references/sweep-output-contract.md).

## Contribution contract

- Work from a topic branch based on upstream `main`. Never develop on a fork's
  `main` branch. Keep commits narrow and use imperative commit subjects.
- Screen every candidate against the issue discussion, linked development, open
  PRs, and recent merged PRs. Leaflet has many old issues whose requested work
  is already fixed, superseded, or under active review.
- Make the smallest related change. Do not mix import cleanup, declaration
  rewrites, formatting churn, or speculative refactors into a bug fix.
- Use tabs for indentation and spaces only for alignment. Preserve modern ESM
  imports, current `const`/`let` usage, and existing public API conventions.
- Put source changes under `src/` and browser regressions in the matching
  `spec/suites/` area. Do not edit generated `dist/` output or
  `docs/reference.html` in a contribution.
- Treat source comments as API documentation. Run `npm run docs` when a public
  API comment changes, but do not commit the generated reference HTML.
- Report security vulnerabilities privately as directed by `SECURITY.md`.
- No repository DCO, CLA, or commit-signing requirement was found in the
  contributor docs or workflows at this snapshot. The shared Skippy workflow
  still requires signed, signed-off commits when the local identity supports it.

## Architecture map

- `src/Leaflet.js` is the public ESM export surface. It joins control, core, DOM,
  geometry, geographic, layer, and map modules.
- `src/map/Map.js` owns the map lifecycle and coordinates handlers, layers,
  panes, view state, and events. Optional interactions live under
  `src/map/handler/`.
- Layers implement map add/remove lifecycle hooks; controls implement control
  add/remove hooks. Event behavior is rooted in `src/core/Events.js` and DOM
  normalization in `src/dom/DomEvent.js`.
- `src/geo/` and `src/geometry/` own projections, CRS behavior, coordinates,
  points, bounds, and transformations. `src/layer/vector/` renders through SVG
  or Canvas backends.
- Rollup builds ESM and UMD distributions and copies source-owned static assets.
  Leafdoc consumes source comments for API docs. Browser tests mirror source
  domains under `spec/suites/`.

## Toolchain and verification

- Use Node 24, the CI runtime, with the committed npm lockfile: `npm ci`.
- Focused browser regression:
  `npx vitest --run --project=chromium <spec-file>`.
- Broad browser suite: `npx vitest --run --project=chromium`. CI also covers
  Firefox, Chromium retina, Windows Chromium, macOS WebKit, and touch mode.
- For a new contributor's fork PR, do not infer green CI from an empty PR check
  rollup. Inspect the matching Actions run by head SHA. A completed
  `action_required` run whose checks page says `Workflow runs completed with no
  jobs` is an external workflow gate, not a test failure or a passing run.
- Required static and build checks: `npm run lint` and `npm run build`.
- SSR smoke check: `node ./spec/ssr/ssr_node.js` after building.
- Documentation changes may also need `npm run docs`; site changes use the Ruby
  version in `docs/.ruby-version`, `bundle install`, and `npm run serve`.
- Baseline at the snapshot passed lint (nine existing CSS `no-important`
  warnings), build (five existing circular-dependency warnings), Node SSR, and
  Chromium (47 files passed, one skipped; 1084 tests passed, 14 skipped).

## Review expectations

- Explain the current failure, the root cause, and why the patch is minimal.
- Include a focused browser regression for behavioral fixes and list exact
  validation commands in the PR body.
- Investigate reviewer concerns against current code rather than defending the
  first implementation. Performance-sensitive asset or renderer work needs
  measurement.
- Never describe a browser API as deprecated from a documentation banner alone;
  verify the governing specification and actual compatibility impact.
- Avoid generic or AI-styled drive-by language. GitHub prose must not contain an
  em dash.

## Queue operation

- Maintain owned open PRs before taking new work.
- Target five healthy open contributions unless live repository policy or the
  user sets a lower cap. Fill only with independently validated, non-overlapping
  work; record evidence-backed blockers instead of manufacturing quota work.
- Publish at most one new Leaflet PR in any rolling 24-hour window. Starting a
  new sweep does not reset the window. Before publishing another, require both
  the elapsed window and an executed CI result or maintainer response. An
  `action_required` run with no jobs is not a meaningful signal.
- Check creation timestamps for recent authored Leaflet PRs in open, merged, and
  closed states immediately before publication; the open queue count alone does
  not prove that the 24-hour window elapsed.
- Compare every prospective title and body with recent authored Leaflet PRs.
  Repeated paragraph order or interchangeable sentence scaffolding is a stop
  signal. Write from the distinct failure, root cause, owning change, preserved
  behavior, focused regression, and risk; do not use cosmetic paraphrasing to
  make a shared template look different.
- Refresh issue and PR state immediately before implementation and again before
  push or PR creation.

## Trigger phrases

- bootstrap leaflet
- contribute to leaflet
- sweep leaflet
- replenish leaflet
