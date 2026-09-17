# Quality Control & Compliance Scoring

This document describes the **general QC mechanism** in DisMech: how disorder
entries are scored for completeness, how that scoring is configured and
weighted, and how the scoring system is *extended* with computed metrics that
go beyond what the schema can express. The phenotype-connectivity metric is used
as a worked example, but the mechanism is generic.

For the narrower curator SOPs see
[`frequency-evidence-guidelines.md`](frequency-evidence-guidelines.md) and the
`dismech-references` / `dismech-terms` skills. This page is about the scoring
machinery itself.

## The QC stack at a glance

DisMech layers several independent checks. They answer different questions and
fail independently:

| Layer | Tool | Question it answers |
|-------|------|---------------------|
| Schema validation | `linkml-validate` | Is the YAML structurally valid against the `Disease` class? |
| Term validation | `linkml-term-validator` | Do ontology IDs exist and do labels match? (anti-hallucination) |
| Reference validation | `linkml-reference-validator` | Does each evidence `snippet` actually appear in the cited source? |
| **Compliance scoring** | **`linkml-data-qc`** | **How *complete* is the entry — are recommended fields populated?** |
| Graph integrity | `dismech.graph --validate` | Do causal edges point at real nodes (no orphan targets)? |

### Reading reference-validation output ("Total checks: 0" is not a no-op)

`linkml-reference-validator` prints `Total checks: 0` on **every** clean run,
including entries with hundreds of verified snippets. The counter is mislabeled
upstream: it holds the number of *issues found*, not the number of checks
*performed* (the plugin only emits a result when something fails), so on a
passing file it is 0 by definition. This has already been misdiagnosed as a
silently broken validator — see issue #7252.

As a downstream mitigation, `scripts/run_reference_validator.sh` appends an
affirmative count after every `validate data` run:

```console
$ just validate-kb-references kb/disorders/Vici_Syndrome.yaml
Validation Summary:
  Files validated: 1
  Total checks: 0
  All validations passed!
  Snippets checked: 46/46 verified against cached references
```

That line comes from `dismech.reference_snippet_audit`, which independently
walks the same `reference`/`snippet` pairs (discovered from the schema's
`implements: [linkml:excerpt]` / `[linkml:authoritative_reference]`
annotations) and re-checks each against the body already in
`references_cache/`, reusing the validator's own normalization so "verified"
means the same thing in both places. It is **read-only, offline, and advisory**:
it never fetches, and it never changes the exit code — `linkml-reference-validator`
remains the sole authority on pass/fail. Set `DISMECH_SKIP_SNIPPET_AUDIT=1` to
suppress it, or run it on its own:

```bash
just count-verified-snippets kb/disorders/Asthma.yaml
just count-verified-snippets --strict kb/disorders/Asthma.yaml   # exit 1 on any unverified snippet
```

Pairs whose reference prefix is listed in `skip_prefixes`
(`conf/reference_validator_config.yaml`) or whose reference is not cached
locally are reported separately rather than counted as verified, so the ratio
never overstates what was checked.

### Not-verified is several different diagnoses

A snippet that is not found in its cached reference is not automatically a
misquote — issue #7450 un-skipped the `DOI` prefix across the whole KB, found 86
mismatches, and traced most of them to defects in *our cache* rather than in the
curation. The audit therefore separates the cases:

| State | What it means |
|---|---|
| verified | found in the cached text |
| verified after cache-defect normalization | found only once PDF ligatures (`ﬁ` → `fi`) are folded and markup-stripped word joins (`theANAPC7locus`) are tolerated — the quote is right, the cache is mangled |
| quoted beyond an abstract-only cache | not found, but only an abstract was ever cached, so the full text may well contain it — **unverified, not disproved** |
| not found in cached text | the whole paper is cached and the words are genuinely absent — worth a human |

The relaxed pass only ever runs on a pair that already failed the strict check,
and it still requires the snippet's characters to appear contiguously and in
order, so it merges word boundaries rather than admitting arbitrary text.

The abstract-only state is a distinct *diagnosis*, not an exemption: roughly
23,000 cached references are abstract-only, so waving them through would hide far
more than the skip that prompted the investigation. `--strict` still fails on
them unless you pass `--allow-abstract-only`. (Upstream agrees on the substance:
`SupportingTextValidator` appends its "only abstract available" note to a result
whose severity stays `ERROR`.)

To measure what a `skip_prefixes` entry is hiding without changing what the
gating validator does:

```bash
just count-verified-snippets --unskip-prefix DOI kb/disorders/*.yaml
```

### Minimum evidence-snippet length

`just check-snippet-length` (part of `just qc`) rejects **new** evidence snippets
shorter than five words. A bare term carries no propositional content — it cannot
support or refute the claim it is attached to — and in practice these are lifted
from clinical-features tables whose cells never survive text extraction, so they
are unverifiable by construction:

```yaml
phenotypes:
- name: Strabismus
  evidence:
  - reference: DOI:10.1016/j.molcel.2021.11.031
    snippet: 'Strabismus'          # supports nothing
```

The check needs no network and no cache; it is independent of the reference
validator. Pipe-delimited rows quoted from a structured-source cache
(`HP:0001987 | Hyperammonemia | Very frequent (99-80%)`) are exempt — short in
words, but fully propositional. A baseline
(`tests/snippet_length_baseline.txt`) grandfathers the pre-existing backlog, so
the check gates new occurrences only; `just list-short-snippets` shows the whole
backlog and `just update-snippet-length-baseline` regenerates it.

The baseline records an **occurrence count** per `(file, snippet)`, not just the
key, so a snippet also fails when it appears *more often* than the count on
record. That matters because the anti-pattern is reuse: `'Hearing loss'` cited
for a phenotype and two unrelated treatments in the same file. Keys alone would
wave the next paste straight through.

Validation layers are **binary** (pass/fail). Compliance scoring is **graded**:
it produces a percentage per field, per file, and across the whole KB, and is
used to rank curation priorities. This page focuses on that graded layer and its
extension mechanism.

## Layer 1: recommended-slot compliance

### What it measures

`linkml-data-qc` walks every object in an entry and, for each slot the schema
marks `recommended: true`, asks a single question: **is this slot populated on
this instance?** It never inspects values for correctness — that is the job of
the term/reference validators — only presence.

It rolls those per-instance facts up into `AggregatedPathScore` records using
jq-style `[]` path notation, e.g.:

```
phenotypes[].phenotype_term.term   populated=42  total=50  percentage=84.0
pathophysiology[].cell_types[].term populated=18  total=30  percentage=60.0
```

### The scoring data model

Every score — whether from a recommended slot or a plugin (Layer 2) — has the
same shape (`linkml_data_qc.models.AggregatedPathScore`):

| Field | Meaning |
|-------|---------|
| `path` | Aggregated path, e.g. `phenotypes[]` |
| `slot_name` | The slot being scored, e.g. `phenotype_term.term` |
| `populated` | Count of instances where the slot is filled |
| `total` | Count of instances where the slot *could* be filled |
| `percentage` | `populated / total * 100` |
| `weight` | Importance multiplier (from config) |
| `min_compliance` | Optional threshold; below it raises a `ThresholdViolation` |

### Global vs weighted compliance

Two headline numbers come out of a file's scores:

- **Global compliance** — unweighted: populated fields / total recommended
  fields.
- **Weighted compliance** — each path's contribution scaled by its `weight`:

  ```
  weighted_compliance = Σ(populated × weight) / Σ(total × weight) × 100
  ```

A large gap between the two means your *important* (high-weight) fields have
different coverage than your low-priority ones — focus on the high-weight gaps
first.

### Configuration: `conf/qc_config.yaml`

Weights and thresholds are data, not code. Precedence is **path → slot →
default** (most specific wins):

```yaml
default_weight: 1.0
default_min_compliance: null

slots:                     # applies to every occurrence of the slot
  term:
    weight: 2.0
    min_compliance: 80.0
  description:
    weight: 0.5

paths:                     # overrides slot config for a specific path
  "phenotypes[].phenotype_term.term":
    weight: 3.0
    min_compliance: 90.0
  "disease_term.term":
    weight: 5.0
    min_compliance: 95.0
```

When a path's aggregated `percentage` drops below its `min_compliance`, a
`ThresholdViolation` is recorded (path, actual, required, shortfall). Leaving
`min_compliance: null` means "contribute to the weighted score but never gate
CI".

### Commands

```bash
just compliance kb/disorders/Asthma.yaml   # single file
just compliance-all                        # whole KB, text report
just compliance-report                     # JSON  -> compliance_report.json
just compliance-csv                        # CSV   -> compliance_report.csv
just compliance-weighted                   # apply qc_config weights + thresholds
just gen-dashboard                          # dashboard/index.html, priority targets
```

## Layer 2: computed QC metrics (the plugin mechanism)

### Why recommended slots are not enough

`recommended: true` can only assert **"slot X is populated on object Y."** It is
structurally blind to anything that depends on *relationships between objects*.
The canonical example is **pathograph connectivity**: whether a phenotype is
wired into the causal graph. The edge that connects a phenotype lives on a
*different* object — a pathophysiology node's `downstream` list — so no
`recommended` flag on the phenotype can see it. A phenotype can carry a perfect
HPO `term`, evidence, and a description (full recommended-slot credit) and still
float as a disconnected node in the rendered pathograph.

Trying to force this into `recommended` fails: marking the source-side
`downstream` slot recommended only checks that a node has *some* outgoing edge
(it could point only at other mechanisms, leaving the phenotype orphaned); and
phenotypes have no inbound slot to mark. The honest fix is to **compute** the
metric from the graph and feed it into the same scoring model.

### The `QCMetricPlugin` contract

`src/dismech/qc_plugins.py` defines a small protocol. A plugin takes the parsed
disorder dict plus the active `QCConfig`, and returns extra `AggregatedPathScore`
records — the *same* shape Layer 1 emits:

```python
@runtime_checkable
class QCMetricPlugin(Protocol):
    def evaluate(
        self, data: dict[str, Any], config: QCConfig
    ) -> list[AggregatedPathScore]: ...
```

Because the output is an `AggregatedPathScore`, a computed metric automatically:

- is **graded coverage**, not a binary gate (a file with 9/12 phenotypes wired
  scores 75%, not pass/fail);
- reads its `weight` and `min_compliance` from `conf/qc_config.yaml` via the
  same path/slot precedence as every schema field;
- folds into `weighted_compliance` and raises `ThresholdViolation`s through the
  identical arithmetic.

### Integration seam: `augment_report`

`augment_report(report, data, config, plugins)` runs the plugins, appends their
scores to a `linkml-data-qc` `ComplianceReport`, recomputes
`weighted_compliance` over the union, and appends any new threshold violations.
Base recommended-slot scores and their violations are preserved unchanged. This
is how computed metrics ride alongside schema-driven ones in a single report
(e.g. for the dashboard).

> **Design note.** `linkml-data-qc` (v0.1.0) has no upstream plugin/entry-point
> system. The plugin layer lives in DisMech as a thin wrapper around
> `ComplianceAnalyzer`. The `QCMetricPlugin` protocol is deliberately the same
> minimal shape an upstream hook would use, so the metrics can be lifted into
> `linkml-data-qc` proper later without rewriting them.

## Worked example: phenotype connectivity

`PhenotypeConnectivityPlugin` emits one score, `phenotypes[].causal_inlink`:

- **total** — number of phenotype nodes in the causal graph
  (`build_causal_graph()`), so it matches exactly what the pathograph renders.
- **populated** — phenotype nodes reached by at least one *causal* edge. Only
  the `CAUSAL_PREDICATES` count: `causes`, `leads_to`, and the two
  environmental predicates that make a genuine causal claim, `triggers` and
  `exacerbates`. A `treats` edge (treatment → phenotype), a `readout` edge
  (`phenotypes[].reports_on`), a `models` edge, and the non-committal
  environmental predicates (`predisposes_to`, `protects_against`, `modulates`,
  `influences`) do **not** mechanistically explain a phenotype, so those are
  excluded.

A phenotype is fixed by adding its `name` as a `downstream` target on the
upstream pathophysiology node:

```yaml
pathophysiology:
- name: Airway Inflammation
  downstream:
  - target: Wheezing        # wires the "Wheezing" phenotype into the graph
```

### Commands

```bash
# Per-file coverage across the KB (lists files with gaps)
just compliance-connectivity

# Also print the floating phenotype node names
just compliance-connectivity --list-unconnected

# Fail (exit 1) if aggregate coverage drops below a percent (for CI)
just compliance-connectivity --fail-under 30
```

### Triage view: `just list-disconnected-phenotypes`

The recipe above is the compliance view, and a gate: both metric halves, the
aggregate percentages, and the `min_compliance` floor it enforces over the
corpus. Issue #11935 asked for the **per-entry triage** of the phenotype half,
filed next to `just list-causal-targets` and `just list-cancer-origin` rather
than under compliance. The two are complementary rather than redundant — a
corpus ratchet no single entry can trip, and a worklist for wiring one disease. It is a thin wrapper
around the same `causal_inlink_coverage` function, so the two can never
disagree on a number:

```bash
just list-disconnected-phenotypes                        # census + ranked worklist
just list-disconnected-phenotypes --format tsv           # one row per phenotype
just list-disconnected-phenotypes --zero-only            # only 0-connected entries
just list-disconnected-phenotypes kb/disorders/Asthma.yaml
```

It adds a ranked zero-connectivity worklist (entries where *no* phenotype is
connected, ordered by how many are stranded — every phenotype stranded is one
sitting's work, a single gap is a different signal), `--format tsv`/`json`, and
an **attachment class** per stranded phenotype:

| Class | Meaning |
|---|---|
| `ISOLATED` | no edge in the graph touches the node at all |
| `TREATED` | a `treats`/`targets` edge from a treatment reaches it |
| `READOUT` | a `reports_on`/biomarker `readout` edge involves it |
| `NONCAUSAL_INBOUND` | a non-committal environmental or other non-causal edge reaches it |
| `SEQUELA_SOURCE` | it explains something downstream, but nothing explains it |

None of those counts as connected — that is the strict reading, and it follows
from the predicate rather than from a special case. They are reported so that
"nothing in the graph knows this node exists" reads differently from "something
points at it, but not a mechanism"; both are unexplained, and they are not the
same curation job.

It is report-only (exit 0), with `--strict` and `--fail-under` opt-in. That is
about *this view*, not about the metric: the aggregate is gated by
`compliance-connectivity`, while a per-entry gate would need a baseline file the
size of the problem. Connecting a phenotype is real curation: the edge asserts
which mechanism produces which clinical feature, which is often exactly what the
literature does not settle. Some phenotypes legitimately have no upstream node in the entry — a
laboratory readout, a feature whose mechanism is genuinely unknown. An edge
added to clear a report is worse than no edge.

This check is the **complement** of `just check-causal-targets`, which finds
edges whose target resolves to nothing. An entry can pass that check perfectly
and still leave every phenotype unexplained; the motivating instance,
`SLC35A1-Congenital_Disorder_of_Glycosylation`, has 7 cleanly resolving edges,
none of which reaches a phenotype.

`conf/qc_config.yaml` configures it like any other path:

```yaml
paths:
  "phenotypes[].causal_inlink":
    weight: 1.5
    min_compliance: 50.0   # gates: `just compliance-connectivity` fails below it
```

**That floor is live and applies to the KB-wide aggregate, not per file**, so no
single entry can trip it and a red build means sustained drift across the
corpus. `test_committed_causal_inlink_floor_is_set_and_never_lowered` blocks
lowering it, and `null` there silently disables the gate. The sibling
`genetic[].mechanism_outlink` is deliberately still advisory. CLAUDE.md's
*A resolving target is not a connected phenotype* carries the current figure and
how to read a failure; this page deliberately does not restate it.


## Granularity ladder: `just check-granularity`

Design decisions §3e fixes how finely an infectious disease is split — the
default entry is the named clinical entity, strata below it are `has_subtypes`
only when documented to differ, promotion to a separate entry needs two
differentiating axes, and a phase is never an entry. Some of those rules are
judgement and some are not, and the check draws that line rather than blurring
it:

```bash
just check-granularity                          # census + worklist, exit 0
just check-granularity --format list            # one line per finding
just check-granularity --format tsv             # one row per entry (the computed columns)
just check-granularity kb/disorders/Cholera.yaml
just check-granularity --strict                 # exit 1 on any deterministic finding
just check-granularity --fail-on TAXON_LUMP     # gate on one class, advisory or not
just check-granularity --scope all              # cross-entry classes over every entry
```

| Class | Rule | Gates under `--strict` |
|---|---|---|
| `MISSING_AGENT`, `UNBOUND_AGENT`, `MISSING_TRANSMISSION` | R25 — every microbial entry names a NCBITaxon-bound agent and a transmission route | yes |
| `ROOT_AS_ENTRY` | R2 — anchored to *infectious disease* or one of its four kingdom-level children | yes |
| `DOUBLE_MODELLED`, `DANGLING_POINTER` | R20 — a subtype that is also another entry carries `curated_in`, and the pointer resolves | yes |
| `DUPLICATE_ANCHOR` | R18/R28 — two entries on one `disease_term` with no `skos:narrowMatch` | yes |
| `PATHOTYPE_COLLAPSE` | R15 — two agents bound to the same taxon | yes |
| `TAXON_LUMP` → `LUMP_RECORDED` | R7–R9 — three or more agents, no subtypes, and no `Deliberately lumped.` paragraph in `review_notes` | no |
| `UNBOUND_SUBTYPE`, `UNBOUND_AGENT_STRATUM` | R12 — may have no honest term to bind | no |
| `NO_PROGRESSION` | R21 — only matters where the disease has phases | no |
| `MISSING_LIFECYCLE` | R26 — heuristic: transmission text names a vector or reservoir | no |
| `POINTER` | informational — a pointer subtype, working as designed | no |

**Report-only, and the advisory half is not a number to drive up.** An
undifferentiated lump is the ladder's default state under R9, so `TAXON_LUMP`
means "no decision recorded", and the right output of looking at one is as
likely a recorded lump as a new subtype. It runs inside `just qc` at exit 0;
`--strict` exists for when the deterministic backlog (the `infectious_agent`
and `transmission` backfills on #10115) is cleared.

**Scope follows the ladder's own exclusions.** A carcinoma with an HPV agent
block is a cancer whose pathogen is an annotation (R23); a Mendelian
susceptibility disorder, a post-infectious sequela and a mycotoxicosis are
likewise not microbial entries. They are counted in the summary and not
assessed. The cross-entry classes (`DOUBLE_MODELLED`, `DUPLICATE_ANCHOR`) are
the mechanical half of #10113 and #10116 as much as of this ladder; `--scope
all` runs them KB-wide, where the umbrella-entry pattern (`Epilepsy` listing
`Juvenile Myoclonic Epilepsy`, which has its own entry) makes them a backlog in
the hundreds.

## Adding a new computed metric

1. Implement a class with an `evaluate(self, data, config) -> list[AggregatedPathScore]`
   method in `src/dismech/qc_plugins.py` (or a sibling module). Derive
   `populated`/`total` from the data — typically via `build_causal_graph()` for
   graph properties — and read `weight`/`min_compliance` from
   `config.get_weight(path, slot)` / `config.get_min_compliance(path, slot)`.
2. Choose a synthetic `path`/`slot_name` that does **not** collide with a real
   schema slot (e.g. `phenotypes[].causal_inlink`).
3. Add the plugin to `DEFAULT_PLUGINS`.
4. Add a `paths:` entry in `conf/qc_config.yaml` for its weight/threshold.
5. Add tests under `tests/test_qc_plugins.py`.

Candidate metrics the same seam supports: orphan-target rate (referential
integrity as coverage), gene-to-mechanism wiring, dead-end pathophysiology nodes
(mechanisms that reach no phenotype), and module-conformance completeness.
