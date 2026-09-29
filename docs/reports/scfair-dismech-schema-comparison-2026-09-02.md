# scFAIR and dismech: a schema comparison, and what LinkML would buy both

*Analysis date: 2026-09-02. Author: AI-assisted (Claude Code). All schema
structure read from source, not from documentation summaries.*

## Question

The [scFAIR consortium](https://sc-fair.org/) (EPFL Deplancke lab + SIB) publishes
a single-cell metadata schema that extends CZ CELLxGENE's, and — unusually for a
metadata standard — a **structured description of computational analysis
workflows**. dismech independently evolved its own analysis-provenance model for
hypothesis exploration runs. This report compares the two, and asks what LinkML
modeling would give each.

Companion to [`bgee-integration-proposal`](../bgee-integration-proposal.md), which
covers the data-layer question (Bgee expression, ASAP's dataset catalogue)
separately. **This report is about schemas, not data.**

## TL;DR

- The two schemas overlap almost exactly on one thing — **recording how a
  computational result was produced** — and they are complementary rather than
  redundant. scFAIR models *the happy path in mechanical detail* (docker digests,
  conda environments, random seeds, resource usage). dismech models *failure and
  unverifiability* (execution status, auditability, whether a data source was
  actually accessed). Neither has the other's half.
- **Neither side's analysis-provenance model is formally modeled.** scFAIR's
  schema is prose Markdown plus a 1,798-line imperative validator config.
  dismech's `MANIFEST.yaml` is validated by hand-written Python and has no schema
  file at all. dismech's *assessment* sidecar is LinkML; its *execution manifest*
  is not.
- scFAIR's `rules.yaml` contains constructs that are, literally, LinkML features
  written out by hand — a dynamic enum, a conditional rule, a structured pattern,
  a mixin. The clearest case: `assay_ancestor_terms: ['EFO:0030080', …]` plus
  ancestor-checking code **is** `reachable_from`, which dismech already uses for
  its `AssayTerm` enum rooted at `OBI:0000070`.
- The concrete offer to scFAIR is a LinkML rendering of their schema. The
  concrete ask is their environment-capture vocabulary. Neither requires the
  other to adopt the other's model wholesale.

## What each side actually is

### scFAIR

| Artifact | Form | Size |
|---|---|---|
| [`scFAIR_schema`](https://github.com/scFAIR/scFAIR_schema) `schema/7.1.0/schema.md` | prose Markdown, HTML tables | 1,906 lines |
| `schema_analysis_json.md` | prose Markdown | 1,324 lines |
| `schema_atac.md` / `schema_spatial.md` / `schema_perturb.md` | prose Markdown | 510 / 356 / 301 |
| [`asap_web` `config/scfair/7.1.0/rules.yaml`](https://github.com/DeplanckeLab/asap_web/blob/main/src/config/scfair/7.1.0/rules.yaml) | validator rule config | 1,798 lines |

The Markdown is the normative specification; `rules.yaml` is what the ASAP
validator executes. They are two hand-maintained expressions of one model. The
schema is a fork of CELLxGENE single-cell-curation 7.1.0, and is CC0.

### dismech

| Artifact | Form | Notes |
|---|---|---|
| `src/dismech/schema/hypothesis_assessment.yaml` | **LinkML** | 373 lines; classes, slots, enums, `slot_usage` |
| `src/dismech/schema/dismech.yaml` | **LinkML** | the main KB schema, incl. `Dataset` |
| `src/dismech/hypothesis_analysis_run.py` | **imperative Python** | validates `MANIFEST.yaml`; no schema file |

The split matters: dismech's *judgement* layer (what an assessor concluded about
a provider run) is formally modeled, while its *execution record* layer — the
thing scFAIR also models — is not.

## The overlap: analysis provenance

Both schemas describe a computational run. Field-by-field:

| Concept | scFAIR (`schema_analysis_json`) | dismech (`HypothesisAnalysis` / `MANIFEST.yaml`) |
|---|---|---|
| Run identity | `pipeline_name`, `pipeline_version`, `pipeline_url`, `creation_date` | `analysis_id`, report frontmatter |
| Unit of work | `steps[]` with `step_label`, `step_category` | one `HypothesisAnalysis` per analysis |
| Method | `method`, `command` | `method`, `comparison` |
| Software | `software_version`, `programming_language`, `programming_language_version` | `HypothesisAnalysisSoftware` (`software_name`, `software_version`, `software_uri`) |
| Environment | `docker_repo`, `docker_image_url`, `docker_image_name`, **`docker_image_digest`**, `conda_env_url`, `conda_env_file` | `environment_artifact` (a committed file) |
| Parameters | `parameters` | `parameters` |
| Inputs | `inputs[]` with `label`, `type`, `format`, `location`, **`checksum`** (`"<algo>:<hex>"`) | `input_data_source_ids` → `HypothesisDataSource` (`uri`, `checksum`, `byte_count`, `version`, `retrieved_at`) |
| Outputs | `outputs[]`, same shape as inputs | `output_artifacts`, `code_artifacts`; MANIFEST output **roles** `{CODE, ENVIRONMENT, TABULAR_RESULT}` |
| Determinism | **`random_seed`** | — |
| Cost | **`resources`**, **`execution_duration_seconds`** | — |
| Timing | `execution_timestamp` | `retrieved_at`, `assessed_at` |
| **Did it work?** | — | **`status`**: `SUCCEEDED` / `PARTIAL` / `FAILED` / `SKIPPED` / `REPORTED_ONLY` |
| **Can it be audited?** | — | **`auditability`**: `REPRODUCIBLE` / `PARTIALLY_AUDITABLE` / `UNVERIFIABLE` |
| **Was the data really accessed?** | — | **`access_status`**: `ACCESSED` / `SEARCHED_NO_RESULT` / `CITED_NOT_ACCESSED` / `UNVERIFIABLE` |
| Failure lineage | — | `status_reason`, `fallback_from_analysis_id`, `limitations` |

### The asymmetry is the finding

scFAIR's step model has no execution-status field. A step is described as though
it ran. That is entirely reasonable for its use case — a pipeline description
attached to a deposited dataset, written by the person who ran it, where the
artifact's existence is the evidence of execution.

dismech's use case is the opposite and is why those enums exist: it assesses
**reports written by AI research providers**, where the central risk is a report
claiming a computation that never ran. `REPORTED_ONLY` exists precisely to name
"the report says it computed this; nothing establishes that it did."
`CITED_NOT_ACCESSED` names "the provider cited a dataset it never opened."

As single-cell analysis pipelines increasingly get generated or driven by agents,
scFAIR will face the same problem, and the fields it lacks are the ones that
catch it. Conversely, dismech's environment capture is a single
`environment_artifact` file where scFAIR has a container digest and a conda
specification — scFAIR's is straightforwardly better and dismech should adopt it.

## What LinkML would buy scFAIR

`rules.yaml` is a well-organised imperative config. But several of its sections
are LinkML language features written out by hand, which means they need bespoke
validator code, cannot generate anything, and drift from the Markdown spec.

### 1. Dynamic enums (`reachable_from`)

`rules.yaml` carries:

```yaml
cross_field:
  assay_ancestor_terms: ['EFO:0030080', 'EFO:0007045', 'EFO:0002761',
                         'EFO:0008919', 'EFO:0010184', 'EFO:0008994']
```

— a list of ontology roots, plus Ruby that walks ancestors to check membership.
That is exactly LinkML's dynamic enum, which dismech already uses:

```yaml
enums:
  AssayTerm:
    reachable_from:
      source_nodes:
        - OBI:0000070  ## assay
      is_direct: false
      relationship_types:
        - rdfs:subClassOf
```

The declarative form is checkable by `linkml-term-validator` against the live
ontology, cacheable, and generates its own documentation. dismech runs this over
its whole KB today.

### 2. Conditional rules (`rules` / preconditions)

```yaml
organism_cell_type_prefixes:
  NCBITaxon:6239: ['CL', 'WBbt']
  NCBITaxon:7955: ['CL', 'ZFA']
  NCBITaxon:7227: ['CL', 'FBbt']
organism_dev_stage_mapping:
  NCBITaxon:9606: HsapDv
  NCBITaxon:10090: MmusDv
```

"If organism is X, the cell-type term must come from ontology Y" is a LinkML
class-level `rules` block with a `precondition`/`postcondition` pair — expressible
declaratively and compilable into JSON Schema conditionals and SHACL shapes. The
`cross_field` CF-1..CF-9 rules are all of this shape.

### 3. Structured patterns

The `"<algorithm>:<hex>"` checksum format and CURIE formats are `pattern` /
`structured_pattern` slots. dismech enforces the same thing with a hand-written
regex (`^sha256:[0-9a-f]{64}$`) — both sides would benefit.

### 4. Mixins and profiles

`schema_atac.md`, `schema_spatial.md`, `schema_perturb.md` are separate documents
describing additive field sets, with `spatial_extension` and `perturb_extension`
blocks in `rules.yaml`. That is LinkML `mixins` — one class per extension,
composed into a profile, with no document duplication and no risk of the base
spec and the extension drifting.

### 5. One source, many targets

The decisive argument. A LinkML schema generates JSON Schema, SHACL, OWL, SQL
DDL, Python dataclasses, and documentation from one YAML file. scFAIR currently
maintains the Markdown spec and `rules.yaml` in parallel by hand, and the
analysis JSON has **no** machine-readable schema at all despite being JSON — so
nothing validates it. A LinkML rendering would emit the JSON Schema for free.

**Caveat worth stating plainly:** LinkML would not express everything in
`rules.yaml`. The `fix_form` field groups, UI popup text, and the compliance
report's check taxonomy are presentation concerns that belong outside a data
model — LinkML `annotations` can carry some, but the honest answer is that
`rules.yaml` would shrink, not vanish. And a migration is real work on a schema
that currently functions.

## What dismech should take

1. **Model `MANIFEST.yaml` in LinkML.** It is the one dismech provenance
   structure with no schema — validated by ~400 lines of imperative Python that
   re-implements required-field checking, type checking, enum checking, and
   pattern matching that LinkML generates. The output roles
   `{CODE, ENVIRONMENT, TABULAR_RESULT}` are an enum; `sha256:<hex>` is a
   `structured_pattern`; the input/output records are classes. The genuinely
   bespoke parts — checksum *recomputation* against files on disk, symlink
   rejection, sensitive-key redaction — stay in Python, as they should.
2. **Adopt scFAIR's environment vocabulary.** `docker_image_digest` +
   `conda_env_file` is a stronger claim than "an environment file exists",
   and it costs nothing to add alongside `environment_artifact`.
3. **Adopt `random_seed`.** dismech's replay gate checks that saved code
   reproduces committed outputs. For any stochastic method that is
   underdetermined without a seed, and dismech has no slot for one.
4. **Consider `execution_duration_seconds` / `resources`** as weak signals of
   whether a claimed computation plausibly ran — relevant to `REPORTED_ONLY`
   triage, though not decisive.

## What to propose to scFAIR

1. **Offer a LinkML rendering of schema 7.1.0**, starting with the analysis JSON
   because it currently has no machine-readable schema and would gain the most.
   CC0 licensing makes this straightforward. Monarch has deep LinkML expertise
   and this is a natural contribution.
2. **Propose execution-status and auditability fields** for the step model,
   with dismech's enums as a starting vocabulary. Frame it as agent-generated
   pipeline readiness, which is the case that makes it urgent rather than
   theoretical.
3. **Align on SKOS mappings rather than merging.** The two schemas serve
   different scopes and should not converge. `exact_mappings` / `close_mappings`
   between the overlapping slots would let a dismech `HypothesisAnalysis` and a
   scFAIR pipeline step be translated without either adopting the other's model.

## Open questions

- **Does scFAIR want a formal schema language at all?** Forking CELLxGENE means
  inheriting its Markdown-spec convention, and there may be a deliberate reason
  to stay aligned with it. This should be asked, not assumed — the answer decides
  whether the LinkML offer is welcome or an imposition.
- **Is CELLxGENE upstream the better target?** If CELLxGENE's own schema were
  LinkML, scFAIR's fork would inherit it. That is a much larger conversation and
  may be where the leverage actually is.
- **How does this relate to the [Cell Annotation Schema](https://github.com/cellannotation/cell-annotation-schema)?** CAS
  is listed as part of scFAIR and is already partly formalized. It may be the
  precedent for a LinkML rendering, or may already cover some of this ground —
  worth checking before proposing anything.
- **Does dismech's MANIFEST modeling belong in the main schema or a sidecar?**
  It is not KB content, so probably a sidecar alongside
  `hypothesis_assessment.yaml`. That is a design-register question.

## Sources

- [scFAIR_schema](https://github.com/scFAIR/scFAIR_schema) — schema 7.1.0, CC0
- [ASAP validator `rules.yaml`](https://github.com/DeplanckeLab/asap_web/blob/main/src/config/scfair/7.1.0/rules.yaml)
- [scFAIR Consortium preprint (bioRxiv, 2026)](https://www.biorxiv.org/content/10.64898/2026.06.05.730084v1)
- [LinkML: an open data modeling framework, GigaScience](https://academic.oup.com/gigascience/article/doi/10.1093/gigascience/giaf152/8378082)
- dismech: `src/dismech/schema/hypothesis_assessment.yaml`,
  `src/dismech/hypothesis_analysis_run.py`,
  [`docs/hypothesis-report-assessments.md`](../hypothesis-report-assessments.md)
