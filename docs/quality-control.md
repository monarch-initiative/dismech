# Quality Control & Compliance Scoring

This document describes the **general QC mechanism** in dismech: how disorder
entries are scored for completeness, how that scoring is configured and
weighted, and how the scoring system is *extended* with computed metrics that
go beyond what the schema can express. The phenotype-connectivity metric is used
as a worked example, but the mechanism is generic.

For the narrower curator SOPs see
[`frequency-evidence-guidelines.md`](frequency-evidence-guidelines.md) and the
`dismech-references` / `dismech-terms` skills. This page is about the scoring
machinery itself.

## The QC stack at a glance

dismech layers several independent checks. They answer different questions and
fail independently:

| Layer | Tool | Question it answers |
|-------|------|---------------------|
| Schema validation | `linkml-validate` | Is the YAML structurally valid against the `Disease` class? |
| Term validation | `linkml-term-validator` | Do ontology IDs exist and do labels match? (anti-hallucination) |
| Reference validation | `linkml-reference-validator` | Does each evidence `snippet` actually appear in the cited source? |
| **Compliance scoring** | **`linkml-data-qc`** | **How *complete* is the entry — are recommended fields populated?** |
| Graph integrity | `dismech.graph --validate` | Do causal edges point at real nodes (no orphan targets)? |

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
> system. The plugin layer lives in dismech as a thin wrapper around
> `ComplianceAnalyzer`. The `QCMetricPlugin` protocol is deliberately the same
> minimal shape an upstream hook would use, so the metrics can be lifted into
> `linkml-data-qc` proper later without rewriting them.

## Worked example: phenotype connectivity

`PhenotypeConnectivityPlugin` emits one score, `phenotypes[].causal_inlink`:

- **total** — number of phenotype nodes in the causal graph
  (`build_causal_graph()`), so it matches exactly what the pathograph renders.
- **populated** — phenotype nodes reached by at least one *causal* edge. Only
  `causes` and `leads_to` predicates count (`CAUSAL_PREDICATES`). A `treats`
  edge (treatment → phenotype) or a `models` edge does **not** mechanistically
  explain a phenotype, so those are excluded.

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

`conf/qc_config.yaml` configures it like any other path:

```yaml
paths:
  "phenotypes[].causal_inlink":
    weight: 1.5
    min_compliance: null   # contributes to weighted score; does not gate CI yet
```

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
