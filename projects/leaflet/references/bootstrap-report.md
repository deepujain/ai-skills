# Leaflet bootstrap report

Snapshot date: 2026-09-09
Snapshot commit: [`3bb9f2bbf897fcfee54c8b1d9bba804297ae7fe4`](https://github.com/Leaflet/Leaflet/commit/3bb9f2bbf897fcfee54c8b1d9bba804297ae7fe4)
Canonical repository: https://github.com/Leaflet/Leaflet

## Observed contribution contract

Leaflet asks contributors to install with npm or Yarn, develop on a topic branch,
run lint before committing, add browser tests, and keep generated API reference
output out of PRs. Indentation is tabs with spaces for alignment. Security reports
go through the private route in `SECURITY.md`.

Sources: [CONTRIBUTING.md](https://github.com/Leaflet/Leaflet/blob/3bb9f2bbf897fcfee54c8b1d9bba804297ae7fe4/CONTRIBUTING.md),
[SECURITY.md](https://github.com/Leaflet/Leaflet/blob/3bb9f2bbf897fcfee54c8b1d9bba804297ae7fe4/SECURITY.md),
[main workflow](https://github.com/Leaflet/Leaflet/blob/3bb9f2bbf897fcfee54c8b1d9bba804297ae7fe4/.github/workflows/main.yml).

No CLA, DCO, or repository signing rule was found in those public policies or
workflows. Recheck if the contribution documents, templates, or branch
protection change.

## GitHub access path

- The local `gh` credential was stale at bootstrap time. GitHub device
  authorization refreshed it successfully as `deepujain` with `repo`,
  `read:org`, and `gist` scopes.
- The connected GitHub integration authenticated as `deepujain` and supports
  live repository, issue, PR, discussion, diff, branch, commit, and PR-creation
  operations. It reports pull access but no direct push access to upstream.
- [`deepujain/Leaflet`](https://github.com/deepujain/Leaflet) was created with
  `gh repo fork`. Authenticated HTTPS push succeeded for all five topic branches.
- The canonical clone uses HTTPS for read access and a separate `fork` remote for
  publication. No token is printed or persisted in the repository.

## Architecture and ownership map

The public export surface is [`src/Leaflet.js`](https://github.com/Leaflet/Leaflet/blob/3bb9f2bbf897fcfee54c8b1d9bba804297ae7fe4/src/Leaflet.js).
[`src/map/Map.js`](https://github.com/Leaflet/Leaflet/blob/3bb9f2bbf897fcfee54c8b1d9bba804297ae7fe4/src/map/Map.js)
coordinates state, panes, layers, handlers, and events. Core event behavior lives
in [`src/core/Events.js`](https://github.com/Leaflet/Leaflet/blob/3bb9f2bbf897fcfee54c8b1d9bba804297ae7fe4/src/core/Events.js),
with DOM event normalization under `src/dom/`. `src/geo/` and `src/geometry/`
own coordinate math and CRS behavior. Layers and controls use explicit lifecycle
hooks; vector paths delegate to SVG or Canvas renderers.

[`build/rollup-config.mjs`](https://github.com/Leaflet/Leaflet/blob/3bb9f2bbf897fcfee54c8b1d9bba804297ae7fe4/build/rollup-config.mjs)
produces ESM and UMD bundles and static assets. Leafdoc generates API material
from source comments. Browser tests mirror source domains in `spec/suites/`.

## Technology and verification map

[`package.json`](https://github.com/Leaflet/Leaflet/blob/3bb9f2bbf897fcfee54c8b1d9bba804297ae7fe4/package.json)
defines an ESM package built by Rollup, linted by ESLint and Stylelint, and tested
in real browsers with Vitest and Playwright. CI uses Node 24 and tests Chromium,
Firefox, retina Chromium, Windows Chromium, macOS WebKit, and touch variants.

Bootstrap baseline:

- `npm ci`: passed; npm reported one moderate and three high audit findings.
- `npm run lint`: passed with nine existing CSS `no-important` warnings.
- `npm run build`: passed with five existing circular-dependency warnings.
- `node ./spec/ssr/ssr_node.js`: passed and printed `2.0.0-alpha.1`.
- `npx vitest --run --project=chromium`: 47 files passed, one skipped; 1084
  tests passed, 14 skipped.

## Merged PR patterns

- [#10361](https://github.com/Leaflet/Leaflet/pull/10361) made a coordinated but
  narrowly scoped documentation update across ten files.
- [#10274](https://github.com/Leaflet/Leaflet/pull/10274) fixed one iOS CSS
  behavior in one line; the author investigated selector inheritance when a
  reviewer raised it.
- [#10250](https://github.com/Leaflet/Leaflet/pull/10250) added reduced-motion
  behavior with source, CSS, and focused browser coverage and superseded an
  earlier proposal.
- [#10066](https://github.com/Leaflet/Leaflet/pull/10066) normalized line endings
  through repository configuration rather than repeated local cleanup.
- [#9665](https://github.com/Leaflet/Leaflet/pull/9665) kept an icon source-owned,
  copied it during build, and narrowed scope after performance investigation.

Durable pattern: accepted changes are cohesive, grounded in current code, and
carry focused proof. Review may expand investigation, but unrelated cleanup is
removed rather than bundled.

## Closed-unmerged PR patterns

- [#10352](https://github.com/Leaflet/Leaflet/pull/10352) was rejected as an
  AI-style drive-by that mixed the requested API with unrelated import and
  declaration changes.
- [#10249](https://github.com/Leaflet/Leaflet/pull/10249) began from an unverified
  deprecation premise and broke desktop behavior; narrowing it did not establish
  a valid need.
- [#10248](https://github.com/Leaflet/Leaflet/pull/10248) became unnecessary after
  issue discussion and another pointer-capture fix removed the scenario.
- [#10251](https://github.com/Leaflet/Leaflet/pull/10251) closed without explanatory
  comments, so no durable reason is inferred.

Durable pattern: reject stale premises, overlapping work, and scope churn before
implementation. A closed state without direct discussion is not evidence of why.

## Initial queue evidence

No authored open Leaflet PRs were found, so the first Maintain pass had no work.
The initial overlap scan eliminated issues already covered by PRs or merged work,
including #10294, #10046, #9775, #8477, #9326, #9878, #9710, #9930, #9773,
#2662, #5442, #6492, #7342, #7116, #9098, #7744, and #8850.

Five candidates survived screening, failed focused regressions before their
patches, and became reviewable upstream PRs after broad validation:

- [#10369](https://github.com/Leaflet/Leaflet/pull/10369) fixes #4484.
- [#10370](https://github.com/Leaflet/Leaflet/pull/10370) fixes #9747.
- [#10371](https://github.com/Leaflet/Leaflet/pull/10371) fixes #7105.
- [#10372](https://github.com/Leaflet/Leaflet/pull/10372) fixes #3800.
- [#10373](https://github.com/Leaflet/Leaflet/pull/10373) fixes #7389.

At the final refresh all five were open, non-draft, mergeable, review-required,
and had no reported CI checks yet. GitHub verified every SSH commit signature.

## Unknowns and refresh triggers

- Refresh open PRs and linked development immediately before selecting and
  publishing each issue.
- Treat absent GitHub checks as volatile. Recheck after maintainers approve CI
  for a first-time contribution or workflows otherwise begin reporting.
- Rebootstrap when contribution policy, package manager, CI runtime or browser
  matrix, public exports, build ownership, or maintainer review patterns change.
