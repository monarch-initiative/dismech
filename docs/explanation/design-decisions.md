# Dismech Design Decisions

This document is the **decision register** for the Disorder Mechanisms Knowledge Base
(dismech). It records the deliberate design and scope choices that shape the project —
choices that otherwise live only in scattered config files, code, and the heads of
maintainers.

It exists because dismech runs in a heavily agent-forward mode. Both human contributors
and AI agents need a single place that answers *"why is it built this way, and what is
in or out of scope?"* rather than re-deriving the rationale from source each time.

**How to use this document**

- **Agents**: consult this before making structural, scope, ontology, or evidence
  decisions. When a choice here is relevant to a change, cite it. Do not silently
  contradict a recorded decision — if a decision looks wrong or stale, surface it.
- **Humans**: to change a recorded decision, open an issue describing the change and the
  rationale, and tag a maintainer (e.g. `@cmungall`). This document should be updated in
  the same PR that enacts a decision change.
- This document **describes** decisions; it is not the authoritative source for the data
  itself. Where a decision is enforced by a file (e.g. the ontology list in
  `conf/oak_config.yaml`), that file remains canonical and is linked below. Keep this
  document in sync with those files; do not let it become a source of drift.

A human-readable summary of the headline decisions is also published in the
[detailed docs](https://dismech.monarchinitiative.org/details/#design-decisions).

---

## 1. Project scope

**Decision.** Dismech is a *mechanism-first* knowledge base of disease pathophysiology.
Each entry models the causal chain from etiology (genetic, environmental, infectious)
through molecular and cellular dysfunction to clinical phenotypes, with curated,
literature-grounded evidence.

**In scope.** Any disease or disorder with a mechanistic story worth modeling —
Mendelian, complex/common, infectious, environmental/exposure-related, neoplastic,
and psychiatric conditions are all represented. Rare and common diseases are both in
scope. Veterinary and animal-model observations are in scope only as *evidence*
(`evidence_source: MODEL_ORGANISM`), not as standalone disease entries.

**Out of scope.** Dismech is **not**:

- a clinical-care guideline or treatment protocol authority,
- a diagnostic decision-support tool for individual patients,
- a store of patient-level / individual data (see
  [individual data](individual-data.md)),
- a new ontology. We **reuse** existing ontologies rather than minting terms
  (see §4).

**Disease selection / prioritization.** Which diseases get curated next is driven by a
MONDO-based prioritizer and the compliance/priority dashboard, not ad hoc. See
[MONDO Prioritizer](../mondo-prioritizer.md) and `dashboard/priority.json`.

---

## 2. Schema framework: LinkML

**Decision.** The data model is defined in
[`src/dismech/schema/dismech.yaml`](https://github.com/monarch-initiative/dismech/blob/main/src/dismech/schema/dismech.yaml)
using [LinkML](https://linkml.io/linkml/).

**Rationale.** LinkML was chosen over plain JSON Schema, OWL, or hand-rolled RDF
because it gives us, in one artifact:

- **Human-friendly authoring** in YAML (curators and agents edit plain YAML),
- **Ontology binding** via `meaning` fields and `reachable_from` dynamic enums, so enum
  values are validated against authoritative ontologies,
- **Multi-format generation** (JSON Schema, SHACL, Pydantic, docs, etc.) from a single
  source of truth,
- Alignment with the broader Monarch / OBO tooling ecosystem.

The internal representation uses LinkML with OBO ontology terms directly. Interoperable
knowledge-graph concerns (BioLink) are handled separately at the export layer (see §5).

---

## 3. Knowledge-representation principles

**One `Disease` class, one file per disorder.** Each disorder is a single YAML file in
[`kb/disorders/`](https://github.com/monarch-initiative/dismech/tree/main/kb/disorders)
that validates against the `Disease` class. Comorbidity and module files reuse the same
schema.

**Subtypes vs. separate entries.** Closely related variants of one diagnosis are modeled
as `has_subtypes` within a single file, using the subtype `name` as a foreign key that
other sections (`phenotypes`, `genetic_basis`, etc.) reference via their `subtype` slot
(enforced by `test_subtype_foreign_keys`). Create a **separate disorder file** only when
the condition has a distinct MONDO identity and a substantially independent mechanism;
otherwise prefer a subtype. See the subtype naming conventions in
[`CLAUDE.md`](https://github.com/monarch-initiative/dismech/blob/main/CLAUDE.md).

**Mechanism modules are conformance, not inheritance.** Modules in
[`kb/modules/`](https://github.com/monarch-initiative/dismech/tree/main/kb/modules)
capture conserved pathological processes (e.g. the fibrotic response) that recur across
disorders. A disorder node declares `conforms_to: "module_name#Node Name"`. This is a
**consistency check, not DRY reuse**: conforming entries fully duplicate the relevant
content and substitute organ-specific cell types/genes. Modules deliberately do not act
as a base class that disorders inherit from.

**Causal graph / pathograph.** Pathophysiology nodes connect via `downstream` causal
edges with a `causal_link_type`, forming a directed graph from etiology to phenotypes.
This graph backs the rendered pathographs and the computational-model integration
(see [computational models](computational-models.md)).

---

## 4. Ontology constraints

**Decision.** Term validation is restricted to an explicit, curated set of ontologies —
one authoritative ontology per domain. The canonical list is
[`conf/oak_config.yaml`](https://github.com/monarch-initiative/dismech/blob/main/conf/oak_config.yaml);
the table below mirrors it.

| Domain | Ontology | Prefix(es) |
|---|---|---|
| Disease | MONDO, ICD-10-CM, ICD-11 foundation | `MONDO:`, `ICD10CM:`, `icd11f:` |
| Phenotype | Human Phenotype Ontology | `HP:` |
| Cell types | Cell Ontology | `CL:` |
| Biological process / function / component | Gene Ontology | `GO:` |
| Anatomy | UBERON | `UBERON:` |
| Chemicals / drugs | ChEBI | `CHEBI:` |
| Genes | HGNC | `hgnc:` (canonical lowercase), `HGNC:` (legacy) |
| Inheritance / variant effects | Genotype Ontology | `GENO:` |
| Treatments / medical actions | MAXO, NCI Thesaurus | `MAXO:`, `NCIT:` |
| Exposures | ECTO, ExO, XCO | `ECTO:`, `ExO:`, `XCO:` |
| Environment | ENVO | `ENVO:` |
| Food | FOODON | `FOODON:` |
| Parasite life cycle | OPL | `OPL:` |
| Taxonomy | NCBITaxon | `NCBITaxon:` |

**Rationale.** A constrained, OBO/Monarch-aligned set keeps terms interoperable,
machine-validatable (offline SQLite adapters via OAK), and resistant to AI hallucination
of fake identifiers.

**Selection priority when several ontologies could apply:**

- **Treatments**: use whichever of MAXO or NCIT has the *most specific* accurate term.
  NCIT often has more specific procedure/therapy terms; MAXO for generic medical actions.
- **Therapeutic agents**: prefer **CHEBI** for specific small-molecule drugs; use **NCIT**
  for drug classes and for biologics/newer drugs lacking a CHEBI term.
- **Disease-like phenotypes** (phenotypes that are also diseases, e.g. osteoporosis,
  glaucoma): dual-code with both an `HP:` and a `MONDO:` identifier where appropriate.

**Conventions.**

- **HGNC casing**: gene CURIEs use **lowercase** `hgnc:` (e.g. `hgnc:746`). This is the
  canonical form that passes validation; do not flag it as an error.
- **`preferred_term` vs `term.label`**: `term.label` must exactly match the canonical
  ontology label (OAK-verified); `preferred_term` may be more specific/clinical when the
  ontology term is too broad.

**How to add an ontology.** Add the prefix → OAK adapter mapping in
`conf/oak_config.yaml`, ensure the SQLite adapter is available, and re-run term
validation. **Known gap:** prefixes *not* listed there are silently skipped during
validation (only a warning), so an unconstrained prefix can pass unchecked — see §8.

---

## 5. BioLink reuse (export layer only)

**Decision — the headline interoperability choice.** [BioLink](https://github.com/biolink/biolink-model)
(`biolink-model>=4.3.1`) is used **only at the export layer**, in the KGX exporter
([`src/dismech/export/kgx_export.py`](https://github.com/monarch-initiative/dismech/blob/main/src/dismech/export/kgx_export.py)).
The internal dismech schema does **not** use BioLink — it uses LinkML with OBO terms
directly.

**Rationale.** This deliberately separates the *internal curation model* (optimized for
authoring and mechanism representation) from the *interoperable exchange format*
(optimized for integration into the Monarch knowledge graph). Each can evolve without
forcing churn on the other.

The KGX exporter emits typed, directed edges with the knowledge source identifier
`infores:dismech`. Mapping currently used:

**Entity categories:** `biolink:Disease`, `biolink:PhenotypicFeature`, `biolink:Cell`,
`biolink:AnatomicalEntity`, `biolink:BiologicalProcess`, `biolink:Treatment`,
`biolink:Gene`, `biolink:ExposureEvent`, `biolink:OrganismTaxon`,
`biolink:GeneticInheritance`, `biolink:MolecularActivity`, `biolink:CellularComponent`,
`biolink:ChemicalEntity`, `biolink:Pathway`, `biolink:MacromolecularComplex`,
`biolink:MolecularEntity`.

**Predicates:**

| Predicate | Edge (subject → object) |
|---|---|
| `biolink:has_phenotype` | Disease → PhenotypicFeature |
| `biolink:associated_with` | Disease → Disease |
| `biolink:has_participant` | Disease → Cell / CellularComponent / ChemicalEntity / MacromolecularComplex |
| `biolink:disease_has_location` | Disease → AnatomicalEntity |
| `biolink:affects` | Disease → BiologicalProcess / MolecularActivity / Pathway (with INCREASED/DECREASED direction qualifiers) |
| `biolink:treats_or_applied_or_studied_to_treat` | Treatment → Disease |
| `biolink:contributes_to` | Gene → Disease; ExposureEvent → Disease |
| `biolink:associated_with_decreased_likelihood_of` | ExposureEvent → Disease (protective) |
| `biolink:has_mode_of_inheritance` | Disease → GeneticInheritance |
| `biolink:causes` | OrganismTaxon → Disease |
| `biolink:has_biomarker` | Disease → MolecularEntity |

**Known gap:** `differential_diagnoses` and `diagnosis` sections are not yet exported
(issue #2100) — see §8.

---

## 6. Evidence & provenance policy

**Decision.** Every evidence item must cite a real, resolvable reference and quote it
exactly.

- **Accepted reference types**: PMID, DOI, NCT (ClinicalTrials.gov), and structured-source
  IDs `ORPHA:` (Orphanet), `CGGV:`/`CGDS:` (ClinGen), `CIVIC_ASSERTION:`/`CIVIC_EID:`
  (CIViC).
- **Exact-snippet rule**: `snippet` values must be exact substring quotes from the cited
  reference, enforced by `linkml-reference-validator`. Paraphrase fails validation.
- **Cache files are tool-generated**: `references_cache/*.md` are created exclusively by
  `just fetch-reference` / the validator. They are **never** hand-written or hand-edited —
  this is the single most common agent error.
- **`evidence_source` describes the study type** reported in the publication
  (HUMAN_CLINICAL, MODEL_ORGANISM, IN_VITRO, COMPUTATIONAL, OTHER), **not** how curation
  was performed. Model-organism evidence must not be the sole support for a human
  phenotype.
- **Deep-research outputs are leads, not ground truth.** PMIDs, snippets, and ontology
  terms suggested by deep-research tools must be independently verified before commit
  (historically ~1% hallucination rate).
- **Frequency qualifiers need their own evidence**: a phenotype `frequency:` band is a
  separate quantitative claim from the association; when in doubt, omit it. See
  [frequency-evidence-guidelines](../frequency-evidence-guidelines.md).

**Rationale.** The exact-quote-plus-validation pipeline is dismech's primary defense
against AI hallucination and is core to the project's scientific credibility.

---

## 7. Curation process & governance

**Decision.** Dismech is **agent-forward**: most curation is performed by AI agents,
initiated either by humans or by GitHub Actions.

- Humans **initiate** work; agents execute and may also author issue/PR comments.
- The default assumption is that issue/PR contents *and comments* are AI-generated; humans
  are **not** assumed to have verified every line their agent produced (mark human-authored
  content explicitly if desired).
- **Human-in-the-loop is the PR review gate.** Every PR receives an automated Claude
  review and must address its findings; unresolved disagreements are escalated to a human
  maintainer rather than litigated in back-and-forth.
- Contributors should use top-tier models/harnesses; lower-quality models create wasteful
  review churn.
- Curation effort is prioritized by weighted compliance scoring (the priority dashboard).

See [`CONTRIBUTING.md`](https://github.com/monarch-initiative/dismech/blob/main/CONTRIBUTING.md)
and the workflow definitions in `.github/workflows/`.

---

## 8. Open / deferred decisions (gaps)

Decisions we have **not yet made or formalized**. Listed here so they are tracked rather
than rediscovered. Each should carry a tracking issue.

| Area | Status | Tracking |
|---|---|---|
| Chromosomal-disorder curation guidelines | Not yet written; domain-specific extension of this register | #3756 |
| Structural `knowledge_gaps:` schema slot | Deferred; knowledge gaps currently modeled via `discussions` (`kind: KNOWLEDGE_GAP`) | schema follow-up |
| `updated_date` field | Deprecated in favor of git history; legacy entries may retain it pending bulk cleanup | — |
| KGX export of `differential_diagnoses` / `diagnosis` | Not yet exported; candidate predicate `biolink:disease_has_differential_diagnosis` | #2100 |
| Obsolete ontology terms | Should fail validation but do not yet | #712 |
| Unlisted ontology prefixes | Silently skipped by term validation (only a warning) — an unconstrained prefix can pass unchecked | — |
| Schema docs vs. script docs separation | Schema element pages currently mix in script docs | #2737 |

---

## 9. Changing a decision

1. Open a GitHub issue describing the decision change and its rationale.
2. Tag a maintainer (e.g. `@cmungall`) for sign-off on scope/governance changes.
3. Update the canonical source (schema, `oak_config.yaml`, exporter, etc.) **and** this
   document in the same PR.
4. If the change affects agents, update the pointers in
   [`CLAUDE.md`](https://github.com/monarch-initiative/dismech/blob/main/CLAUDE.md) and
   [`AGENTS.md`](https://github.com/monarch-initiative/dismech/blob/main/AGENTS.md).

This register supersedes the previously tacit, scattered rationale for these choices.
