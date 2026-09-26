# Clinical-trial status auditing

## The problem

A dismech `ClinicalTrial` entry records the trial's `status:` (`RECRUITING`,
`COMPLETED`, `TERMINATED`, …) and `phase:`. Both are a **snapshot taken at
curation time**, and until now nothing re-checked them.

ClinicalTrials.gov is the one *live-API* reference source in the repo — Orphanet,
ClinGen, CIViC, ICEES and NCIT are all pinned bulk snapshots with a `*-refresh`
recipe, and their manifests record what was pinned. Trials had neither:

- no `clinicaltrials-refresh` recipe, and
- no retrieval timestamp in `references_cache/clinicaltrials_*.md` (the
  frontmatter carries only `reference_id`, `title`, `content_type` and
  `full_text_attempted`),

so trial-status drift was not merely unfixed, it was **not measurable offline**.
A trial curated as `RECRUITING` stays `RECRUITING` in the KB indefinitely.

## The audit

```bash
just clinicaltrials-status-audit                  # full report
just clinicaltrials-status-audit --only-drift     # just the worklist
just clinicaltrials-status-audit --format json    # machine-readable
just clinicaltrials-status-audit --format markdown
just clinicaltrials-status-audit --strict         # exit 1 if drift found
just clinicaltrials-status-audit --limit 50       # bounded sweep
just clinicaltrials-status-audit kb/disorders/Asthma.yaml   # specific files
```

It reads every `clinical_trials[]` entry in `kb/`, resolves each to an NCT id,
fetches the current `overallStatus`/`phases` from the ClinicalTrials.gov **v2
API**, and reports disagreements.

Requests are **batched** through `filter.ids` (100 ids per call), so the whole KB
is ~8 requests rather than ~800.

### Findings it reports

| Kind | Meaning |
|---|---|
| `status_drift` | curated `status:` disagrees with the registry |
| `phase_drift` | curated `phase:` disagrees with the registry |
| `missing_status` | no curated `status:`, but the registry has one |
| `missing_phase` | no curated `phase:`, but the registry has one |
| `not_found` | NCT id not returned by the registry |
| `unresolvable_id` | trial has no NCT id in `name` or its evidence references |
| `unmappable_status` | registry status has no `ClinicalTrialStatusEnum` equivalent |

Findings whose new status is `TERMINATED`, `WITHDRAWN` or `SUSPENDED` are tagged
`[review]` — see "Why it does not auto-fix" below.

### Identifier resolution

The NCT id is taken from `name` first (the schema's documented home for it), then
from any `clinicaltrials:` evidence reference. That fallback matters: a handful of
KB trials are named by acronym or by a non-NCT registry id (`EMERALD`,
`BESTCILIA`, `ML-DS 2006 (EudraCT 2007-006219-2)`, `ChiCTR-2100045397`) and would
otherwise be silently unauditable. Trials that resolve to no NCT id are reported
as `unresolvable_id` rather than dropped.

## Why it does not auto-fix

The audit reports; it never rewrites the KB. That is deliberate:

- A status change is frequently **not** a one-field edit. A trial that reached
  `COMPLETED` may now have results worth citing; one that went `TERMINATED`
  usually needs its `description` and `evidence` revisited, and *why* it stopped
  can itself be curation-relevant.
- Some drift is not staleness at all but an **error at curation time**. In the
  first full run, 14 trials moved `COMPLETED → ACTIVE_NOT_RECRUITING` — backwards
  in the trial lifecycle, so the curated value was most likely wrong when written
  rather than overtaken by events. Blind overwriting would hide that signal.
- `UNKNOWN` in the registry means *the sponsor stopped updating the record*, not
  that the trial's state is unknowable. Overwriting a curated `RECRUITING` with
  `UNKNOWN` would often lose information rather than refresh it.

So the audit produces the worklist and a curator applies it.

## Enum mapping

ClinicalTrials.gov values are mapped onto the dismech enums:

| Registry `overallStatus` | dismech `ClinicalTrialStatusEnum` |
|---|---|
| `RECRUITING` | `RECRUITING` |
| `NOT_YET_RECRUITING` | `NOT_RECRUITING` |
| `ACTIVE_NOT_RECRUITING` | `ACTIVE_NOT_RECRUITING` |
| `COMPLETED` | `COMPLETED` |
| `ENROLLING_BY_INVITATION` | `ENROLLING_BY_INVITATION` |
| `SUSPENDED` | `SUSPENDED` |
| `TERMINATED` | `TERMINATED` |
| `WITHDRAWN` | `WITHDRAWN` |
| `UNKNOWN` / `UNKNOWN_STATUS` / `WITHHELD` | `UNKNOWN` |

Expanded-access states (`AVAILABLE`, `NO_LONGER_AVAILABLE`, …) have no dismech
equivalent and are reported as `unmappable_status` rather than silently coerced
into `UNKNOWN`.

| Registry `phases` | dismech `ClinicalTrialPhaseEnum` |
|---|---|
| `EARLY_PHASE1` | `PHASE_I` (approximate — dismech has no Early Phase 1 value) |
| `PHASE1` / `PHASE2` / `PHASE3` / `PHASE4` | `PHASE_I` / `PHASE_II` / `PHASE_III` / `PHASE_IV` |
| `NA` | `NOT_APPLICABLE` |

A registry record listing several phases (`PHASE1|PHASE2`) matches a curated value
equal to **any** of them, so multi-phase trials do not produce spurious drift.
Tests assert that every mapping target is a real permissible value in
`dismech.yaml`, so the tables cannot drift away from the schema unnoticed.

## Why it is advisory and not in `just qc`

It needs the network and depends on state outside the repo, so it can never be
deterministic. `just qc` stays offline and reproducible. Run this on demand, or on
a schedule, and treat its output as a curation worklist. `--strict` exists for
callers that do want to gate on it.

Exit codes: `0` advisory/clean, `1` drift found under `--strict`, `2` the registry
fetch failed outright (distinguishable from "no drift").

## Baseline

First full run against the KB (810 curated trials, 763 with a resolvable NCT id):

| | count |
|---|---|
| `status_drift` | 104 |
| `phase_drift` | 28 |
| `missing_status` | 57 |
| `missing_phase` | 32 |
| `unresolvable_id` | 5 |
| `unmappable_status` | 2 |

132 of 763 auditable trial records (**17%**) disagreed with the registry, across
102 disorder files; 14 had moved to a `[review]` status.
