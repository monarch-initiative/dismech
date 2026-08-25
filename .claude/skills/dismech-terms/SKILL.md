---
name: dismech-terms
description: >
  Select, add, validate, review, or repair ontology bindings and derived term
  caches in dismech. Use when changing term IDs, canonical labels,
  preferred_term values, enum meaning mappings, phenotype, cell-type,
  biological-process, disease, anatomy, exposure, or treatment annotations;
  choosing an OAK adapter; resolving label or dynamic-enum failures; handling
  ECTO/XCO terms; or diagnosing cache integrity and ordering problems.
---

# Curate Ontology Terms

Follow the session-wide ontology and cache contract in `CLAUDE.md`. Use this
workflow for each concrete term decision.

## Core workflow

### 1. Inspect the field and its range

Read the relevant slot or class in `src/dismech/schema/dismech.yaml`. Determine:

- which descriptor or term field owns the binding;
- which ontology prefixes the schema permits;
- whether the field is constrained by a dynamic enum and `reachable_from`;
- whether a dedicated qualifier or category slot already captures part of the
  intended meaning.

Do not infer validity from similar-looking entries alone. Nearby entries are
useful examples, but the schema and ontology remain authoritative.

### 2. Choose the validator's ontology source

Check `conf/oak_config.yaml` before looking up a term. Automated validation uses
the adapter configured there and is cache-first.

For prefixes configured with OLS, use OLS for a lightweight search or a local
SQLite build when definitions, relationships, or `-O obo` output are needed:

```bash
uv run runoak -i ols:hp search "cognitive impairment"
uv run runoak -i ols:hp info HP:0002014
uv run runoak -i sqlite:obo:hp info HP:0002014 -O obo
```

`-O obo` is not implemented by OLS adapters. A local inspection adapter may
differ from the configured validation adapter, so never mechanically replace
one with the other.

ECTO and XCO are pinned local exceptions. Read
[Exposure-term decisions](references/exposure-terms.md) before selecting or
changing those bindings.

### 3. Search, inspect, and choose

Search broadly enough to find synonyms, then inspect candidate definitions and
ancestry:

```bash
uv run runoak -i ols:cl search "regulatory T cell"
uv run runoak -i sqlite:obo:cl info CL:0000815 -O obo
uv run runoak -i sqlite:obo:cl ancestors CL:0000815 -p i
```

Choose the most specific term that accurately represents the curated claim.
Do not choose a narrow term merely because it is available. If only a broad
ontology term fits, bind that term and use `preferred_term` for justified
human-readable specificity.

### 4. Write the descriptor correctly

Keep canonical and display labels distinct:

```yaml
cell_types:
- preferred_term: CD4+ regulatory T cell
  term:
    id: CL:0000815
    label: regulatory T cell
```

- `term.id` is the ontology CURIE.
- `term.label` exactly matches the canonical ontology label.
- `preferred_term` is the display label and may preserve clinically or
  biologically useful nuance not represented by the ontology.

Prefer the canonical label as `preferred_term` when no extra nuance is needed.
Use lowercase `hgnc:` for HGNC gene CURIEs in this repository.

For common clinical post-composition, follow `Descriptor Qualifier Slots` in
`CLAUDE.md`; do not recreate temporality, course, severity, or onset in a generic
`qualifiers` list. Follow the root treatment and gain/loss-of-function sections
for those schema-modeling decisions.

### 5. Validate immediately

```bash
just validate-terms kb/disorders/YourDisease.yaml
```

Also run the normal schema validation and the final batched disorder validation
required by `CLAUDE.md`. Treat `just validate-terms` as authoritative for the
configured ontology source and the current cache state.

## Interpret failures

### Label mismatch

Confirm the identifier against the configured ontology, then update
`term.label` to the canonical label. Do not change `preferred_term` unless the
human-facing wording is also wrong.
### XCO terms flagged `Not4Curation`

RGD keeps XCO terms for hierarchy that it does **not** want annotated with, and
marks them with a related synonym reading `Not4Curation` — a synonym, not an
obsoletion axiom. Such a term exists, has a matching label, and is reachable
from `XCO:0000000` (the XCO root among the `ExposureTerm` enum's `source_nodes`;
`ExO:0000002` is the ECTO one), so `just validate-terms` passes it. Twenty-four XCO terms
carry the marker, and three of them (`XCO:0000294` estrogen/estrogen analog,
`XCO:0000950` anticonvulsant, `XCO:0000561` antidepressant) got into the #8430
tranches before a reviewer noticed (#8472).

`just check-not4curation` gates this in `just qc` and CI, so you do not have to
remember — but if you are choosing an XCO term by hand, check it first, because
the flagged ones are exactly the broad drug-class terms an exposure binding
reaches for:

```bash
just check-not4curation --list-flagged --prefix XCO   # the whole deny-list
uv run runoak -i sqlite:obo:xco info XCO:0000294      # synonyms include Not4Curation
```

All three found so far had proper ECTO equivalents (`XCO:0000294` →
`ECTO:9000010` exposure to estrogens), so a flag is a prompt to look in ECTO
rather than a dead end.

## Specificity Guidelines

### Identifier not found

Check the prefix, numeric identifier, obsolescence, and configured adapter. A
term found in a newer or different ontology service may still be unavailable to
the validator. Select a term visible to the configured source or deliberately
update the pinned source through the repository's maintenance workflow.

### Dynamic-enum failure

Term existence and enum membership are different checks. A valid ontology term
may fall outside the field's allowed ancestor closure. Inspect the field's
dynamic enum and its `reachable_from` root rather than adding the CURIE directly
to `cache/enums/*.csv`.

Use the full OAK-backed audit only when refreshing or investigating membership:

```bash
just check-enum-cache
```

Normal validation uses the faster offline structural check.

### Cache integrity or ordering failure

Never type a replacement label, timestamp, or membership row. Read
[Term-cache recovery](references/cache-recovery.md), remove only the corrupt
derived row when required, re-derive it through validation, and normalize with
the sanctioned command.

## Common binding patterns

### Phenotype

```yaml
phenotype_term:
  preferred_term: Seizure
  term:
    id: HP:0001250
    label: Seizure
```

### Biological process

```yaml
biological_processes:
- preferred_term: transforming growth factor beta receptor signaling
  term:
    id: GO:0007179
    label: transforming growth factor beta receptor signaling pathway
  modifier: INCREASED
```

### Disease mapping and coverage

For MONDO coverage and epic-checklist synchronization, the primary
`disease_term` and `has_subtypes` terms count as curated. A term under
`mappings.mondo_mappings` counts only with `skos:exactMatch` or
`skos:narrowMatch`; broad, close, and related matches remain cross-references.

## Specialized guidance

- Read [Exposure-term decisions](references/exposure-terms.md) for ECTO/XCO
  adapter constraints and the smoking-versus-cigarette and
  alcohol-consumption-versus-ethanol binding rules.
- Read [Term-cache recovery](references/cache-recovery.md) when an integrity,
  ordering, duplicate, malformed-row, or suspicious-label problem appears.
