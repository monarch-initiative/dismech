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

### 3a. "Nothing more specific exists" is a checkable claim — write the query (dismech#7835)

The step above ends in a broad binding often enough that the note explaining it
has become routine, and that is where this failure mode lives: an entry binds an
over-broad term and adds a `notes:` sentence asserting a search was run and found
nothing finer. The binding is wrong **and** its justification is false.

**The defect is in the audit trail, not in the data, so nothing catches it.** The
bound term is real, its label matches, and it is inside the enum root — so
`just validate-terms` passes, and so does every other check in the stack. The note
makes it worse rather than better: a bare over-broad binding is a small error a
reviewer might spot, whereas an over-broad binding plus *"I checked, nothing finer
exists"* hands the reviewer an explicit reason to skip the one check that would
catch it. Only a semantic re-check finds it.

Three confirmed instances came out of a single batch of ten freshly curated
entries. In each, an independent verifier re-ran the search the note claimed had
been run and found an exact match: `UBERON:0014527` posterior limb of internal
capsule (bound as the whole capsule `UBERON:0001887`), `NCIT:C80435` (bound as the
branch root `NCIT:C49236` Therapeutic Procedure), and `HP:0004890` Elevated
pulmonary artery pressure (asserted to be unavailable). All three were corrected
before their PRs merged, so `main` has never carried them.

1. **Write the query you ran, verbatim and re-runnable, plus what it returned** —
   not a bare assertion that searching happened.
   `KLHL24-Related_Hypertrophic_Cardiomyopathy.yaml` is the worked example: it
   names ``runoak -i sqlite:obo:ncit search 't~defibrillator'`` and the term that
   came back, so the next reader re-runs it in one paste instead of guessing what
   was searched for.
   Then **re-run it yourself, immediately before you commit the note.** Naming a
   re-runnable query does not make the note true: the query is the half a reader
   can check, and its reported output is the half that can be false.
   `Digitalis_Poisoning` reached review with a note naming five ECTO searches
   (`l~digitalis`, `l~digoxin`, `l~glycoside`, `l~oleander`, `l~foxglove`) and
   concluding ECTO had no cardiac-glycoside, digitalis or oleander exposure
   class — where `l~glycoside`, one of the five, returns `ECTO:9000436 exposure
   to glycoside`, and `l~digitalin` returns `ECTO:9000003 exposure to digitalin`
   ([#12307](https://github.com/monarch-initiative/dismech/pull/12307)). The
   searches had been written down without being read back.
2. **Prefer no note to an unverified note.** If you did not run the search, silence
   is the honest output. Never write a verification sentence to satisfy the
   instruction to document verification.
3. **State the relation you did check, not the absence you did not.** The strongest
   form of these notes explains the binding *positively* against the alternative —
   as in `CDH2-Related_ACOG_Syndrome.yaml`, which records that `HP:0002092` was
   rejected because OAK shows it descending from `HP:0033578` pre-capillary
   pulmonary hypertension, a haemodynamic category the source does not establish.
   That is a claim a reviewer can falsify; "nothing finer exists" is not.

This does **not** withdraw the instruction to document verification — the same
batch produced genuinely excellent provenance notes, including one naming four
papers it excluded as off-entity, each of which independently checked out. The
rule is about what an *unbacked* verification sentence costs, not about whether to
write notes. Record the reasoning in `notes:` rather than `description:`: the
description says what the entity is, and why a CURIE was chosen is curation
provenance.

No lint covers this. Extracting "no more specific term exists"-shaped sentences
from `notes:` and re-running the OAK search would catch the whole class
mechanically; that is a follow-on rather than done. Until then a reviewer
re-running the search is the only thing that finds it — so treat any
negative-existence sentence in a diff as a prompt to do exactly that.

### 3b. A term suggested by a deep-research report is a lead, not a binding

Reports in `research/` suggest CURIEs because the templates ask them to, and
they get them wrong in ways that look clean: the CMTX report in
[#9729](https://github.com/monarch-initiative/dismech/issues/9729) offered
`MONDO:0010674` (Hunter syndrome) for Charcot-Marie-Tooth X-linked, with 26/26
of its citations verified.

Since `deep-research-client` 0.2.11 those suggestions are checked as the report
is generated. Read the report's `## Term Validation` section, or its
`term_validation:` frontmatter, before lifting any CURIE out of it — and add the
section to an older report with `just validate-research-terms <report>`.

Two things the section does **not** settle, which is the whole of step 3 above:

- whether the term is reachable from the slot's dynamic-enum root, and
- whether it is the right term for the claim, as opposed to a real term named
  consistently.

It *does* flag a near-miss when the report names one — the same CMTX report
writes "areflexia" beside `HP:0001265`, which HPO calls *Hyporeflexia*
(*Areflexia* is `HP:0001284`). Read those entries as granularity findings, not
as paraphrase.

Gene CURIEs are skipped by default there (`HGNC` uppercase does not resolve in
`sqlite:obo:hgnc`, and `ols:` resolves it to an unrelated term), so verify those
yourself. See
[`docs/deep-research-term-validation.md`](../../../docs/deep-research-term-validation.md).

### 3c. A term suggested in a review comment is a lead too

Same footing as 3b, and for the reason the decision register gives: PR comments
are AI-generated by default in this repo ([design decisions
§7](../../../docs/explanation/design-decisions.md)), so a reviewer's CURIE is
another agent's suggestion, not a checked binding. It arrives looking
more authoritative than a report's because it comes attached to a finding that
was right.

Verify it as you would any other candidate, and in particular check the
*relation* it stands in to the term you meant. In
[#12297](https://github.com/monarch-initiative/dismech/pull/12297) a round-1
reviewer supplied `HP:0003324`; it existed, `Generalized muscle weakness` was its
canonical label, and `just validate-terms` passed — while the descriptor's
`preferred_term`, description, snippet and explanation all said *limb*.
`HP:0003324` and `HP:0003690` Limb muscle weakness are siblings under
`HP:0001324` Muscle weakness, not a general and a specific form of one thing, so
the binding asserted a distribution of weakness the source did not support. It
cost the PR a round.

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
