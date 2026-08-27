# DisMech Design Decisions

This document is the **decision register** for the Disorder Mechanisms Knowledge Base
(DisMech). It records the deliberate design and scope choices that shape the project.

Both human contributors and AI agents need a single place that answers *"why is it built this way, and what is in or out of scope?"* rather than re-deriving the rationale from source each time.

**How to use this document**

- **Agents**: consult this before making structural, scope, ontology, or evidence
  decisions. When a choice here is relevant to a change, cite it. Do not silently
  contradict a recorded decision. If a decision looks wrong or stale, surface it.
- **Humans**: to change a recorded decision, open an issue describing the change and the
  rationale, and tag a maintainer (e.g. `@cmungall`). This document should be updated in
  the same PR that enacts a decision change.
- This document **describes** decisions. It is not the authoritative source for the data
  itself. Where a decision is enforced by a file (e.g. the ontology list in
  `conf/oak_config.yaml`), that file remains canonical and is linked below.

A human-readable summary of the headline decisions is also published in the
[detailed docs](https://dismech.monarchinitiative.org/details/#design-decisions).

**How to suggest changes to these design decisions**

1. Open a GitHub issue describing the decision change and its rationale.
2. Tag a maintainer (e.g. `@cmungall`) for sign-off on scope/governance changes.
3. Update the canonical source (schema, `oak_config.yaml`, exporter, etc.) **and** this
   document in the same PR.
4. Update the agent instructions in
   [`CLAUDE.md`](https://github.com/monarch-initiative/dismech/blob/main/CLAUDE.md) and
   [`AGENTS.md`](https://github.com/monarch-initiative/dismech/blob/main/AGENTS.md).

## 1. Project scope

**Decision.** DisMech is a *mechanism-first* knowledge base of disease pathophysiology.
Each entry models the causal chain from etiology (genetic, environmental, infectious)
through molecular and cellular dysfunction to clinical phenotypes, with curated,
literature-grounded evidence.

**In scope.** Any disease or disorder with a mechanistic story worth modeling is in scope.
Mendelian, complex/common, infectious, environmental/exposure-related, neoplastic,
and psychiatric conditions are all represented. Rare and common diseases are both in
scope. Though DisMech is primarily intended as a resource for human diseases and disorders,
veterinary and animal-model observations are in scope as *evidence*
(`evidence_source: MODEL_ORGANISM`).

**Out of scope.** DisMech is **not**:

- a clinical-care guideline or treatment protocol authority,
- a diagnostic decision-support tool for individual patients,
- a store of patient-level / individual data (see
  [individual data](individual-data.md)),
- a new ontology. We **reuse** existing ontologies rather than minting terms
  (see *Ontology constraints* below).

**Disease selection and prioritization.**

Which diseases get curated next is driven by:

- the needs of one or more specific research projects,
- the [MONDO Prioritizer](../mondo-prioritizer.md), and
- the compliance/priority dashboard. See `dashboard/priority.json`.

## 2. Schema framework

DisMech is based on a data model represented in the [LinkML](https://linkml.io/linkml/) data modeling language.

**Decision.** The data model is defined in
[`src/dismech/schema/dismech.yaml`](https://github.com/monarch-initiative/dismech/blob/main/src/dismech/schema/dismech.yaml).

**Rationale.** As compared to other schema or data model representations, LinkML supports:

- **Human-friendly authoring** in YAML (curators and AI agents both edit plain YAML),
- **Ontology binding** via `meaning` fields and `reachable_from` dynamic enumerations, so enum
  values are validated against authoritative ontologies,
- **Multi-format generation** (JSON Schema, SHACL, Pydantic, docs, etc.) from a single
  source of truth,
- **Built-in tools** for schema linting, data validation, and other parts of the data management lifecycle, and
- Alignment with the broader Monarch Initiative and OBO tooling ecosystem.

The internal representation uses LinkML with OBO ontology terms directly. Interoperable
knowledge graph concerns (Biolink Model) are handled separately at the export layer (see *Biolink reuse* below).

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
**consistency check**: conforming entries fully duplicate the relevant
content and substitute organ-specific cell types/genes. Modules deliberately do not act
as a base class that disorders inherit from.

**Causal graph / pathograph.** Pathophysiology nodes connect via `downstream` causal
edges with a `causal_link_type`, forming a directed graph from etiology to phenotypes.
This graph backs the rendered pathographs and the computational-model integration
(see [computational models](computational-models.md)).


## 4. Ontology constraints

**Decision.** Term validation is restricted to an explicit, curated set of ontologies.

The canonical list is
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
| Treatments / clinical interventions | NCI Thesaurus | `NCIT:` |
| Exposures | ECTO, ExO, XCO | `ECTO:`, `ExO:`, `XCO:` |
| Environment | ENVO | `ENVO:` |
| Food | FOODON | `FOODON:` |
| Parasite life cycle | OPL | `OPL:` |
| Taxonomy | NCBITaxon | `NCBITaxon:` |

**Rationale.** A constrained, OBO/Monarch-aligned set keeps terms interoperable,
machine-validatable (offline SQLite adapters via OAK), and resistant to AI hallucination
of fake identifiers.

**Selection priority when several ontologies could apply:**

- **Treatments**: use the *most specific* accurate NCIT clinical-intervention term
  (all reachable from `NCIT:C25218`). When NCIT has no suitable clinical-action term,
  omit `term:` and keep a free-text `preferred_term` — never invent an identifier.
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
validation (only a warning), so an unconstrained prefix can pass unchecked — see *Gaps* below.

### 4a. MAXO removed in favour of NCIT (2026-07-31)

**Decision.** The Medical Action Ontology (MAXO) was removed from dismech entirely. All
4,300+ MAXO `treatment_term` / `diagnosis_term` bindings were remapped to NCI Thesaurus
clinical-intervention terms, `MAXO:0000001` was dropped from `TreatmentActionTerm`'s
`source_nodes` (leaving `NCIT:C25218` as the sole root), and the MAXO adapter and term
cache were deleted. This reverses the earlier decision to treat MAXO and NCIT as co-equal
treatment vocabularies. See PR #7228 and the frozen crosswalk
`docs/superpowers/maxo_ncit_final_map.tsv`.

**Rationale.** One treatment vocabulary rather than two removes the recurring "which
ontology has the better term?" judgement call, and NCIT covers the clinical-action space
more completely and more specifically.

**What was traded away.** This is a genuine loss of specificity in places, recorded here so
it is not rediscovered as a bug:

- Some MAXO terms have no exact NCIT counterpart and were mapped to a broader parent
  (e.g. drug-class "X agent therapy" terms → `NCIT:C15986` Pharmacotherapy). Where a drug
  class was lost from the action term it is recovered in `therapeutic_agent`; a tail of
  such bindings still carries no coded agent.
- Seven MAXO terms have no NCIT equivalent at all (orthotic/hearing-aid/glasses usage,
  airway management, emollient application, apoptosis assay, transepithelial nasal
  potential difference). Those entries keep a free-text `preferred_term` with no `term:`.
- Mapping a route- or method-agnostic source term to a route- or method-specific NCIT term
  would assert something the source never said, so defaults are deliberately neutral
  (e.g. corticosteroid therapy → `NCIT:C15370` Steroid Therapy, not the *Systemic* child).

**Cache provenance.** NCIT is served via `ols:ncit` (issue #5160) and the OLS adapter
cannot compute ancestors, so dynamic-enum membership cannot be re-derived from the
committed configuration. `cache/enums/treatmentactionterm_*.csv` was therefore generated
by temporarily pointing the `NCIT:` adapter at a local `sqlite:obo:ncit` build — the same
build the `ncit-edges` structured source already uses — and `conf/oak_config.yaml` was
then reverted to `ols:ncit`. Regenerating that cache requires repeating this; the
committed configuration alone is not sufficient.


## 5. Biolink reuse

**Decision.** [BioLink](https://github.com/biolink/biolink-model)
(`biolink-model>=4.3.1`) is used **only at the export layer**, in the KGX exporter
([`src/dismech/export/kgx_export.py`](https://github.com/monarch-initiative/dismech/blob/main/src/dismech/export/kgx_export.py)).
The internal DisMech schema does **not** use BioLink. Rather, it uses LinkML with OBO terms
directly.

**Rationale.** This deliberately separates the *internal curation model* (optimized for
authoring and mechanism representation) from the *interoperable exchange format*
(optimized for integration into knowledge graphs). Each can evolve without
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

**Known gap:** `differential_diagnoses` and `diagnosis` sections are not yet exported. See *Gaps* below.


## 6. Evidence & provenance policy

**Decision.** Every evidence item must cite a real, resolvable reference and quote it
exactly.

- **Accepted reference types**: PMID, DOI, NCT (ClinicalTrials.gov), structured-source
  IDs `ORPHA:` (Orphanet), `CGGV:`/`CGDS:` (ClinGen), `CIVIC_ASSERTION:`/`CIVIC_EID:`
  (CIViC), `ICEES:`, `NCIT:`, `STRCHIVE:`, and `url:` for sources with no citable
  identifier. `url:` is the widest of these and the least self-describing — it covers
  agency and regulator pages (CDC, FDA, EMA), database endpoints (Orphadata,
  Monarch), preprints, and, under §6b, community sources. The authoritative
  machine-readable list is `ALLOWED_REFERENCE_PREFIXES` in `tests/test_data.py`.
- **Exact-snippet rule**: `snippet` values must be exact substring quotes from the cited
  reference, enforced by `linkml-reference-validator`. Paraphrase fails validation.
- **Cache files are tool-generated**: `references_cache/*.md` are created exclusively by
  `just fetch-reference` or the validator. They are **never** hand-written or hand-edited.
- **`evidence_source` describes the study type** reported in the publication
  (HUMAN_CLINICAL, MODEL_ORGANISM, IN_VITRO, COMPUTATIONAL, OTHER), **not** how curation
  was performed. Model-organism evidence must not be the sole support for a human
  phenotype.
- **Deep-research outputs are leads, not ground truth.** PMIDs, snippets, and ontology
  terms suggested by deep-research tools must be independently verified before commit.
- **Frequency qualifiers need their own evidence**: a phenotype `frequency:` band is a
  separate quantitative claim from the association; when in doubt, omit it. See
  [frequency-evidence-guidelines](../frequency-evidence-guidelines.md).

**Rationale.** The exact-quote-plus-validation pipeline is DisMech's primary defense
against AI hallucination and is core to the project's scientific credibility.

### 6a. Superseded hypotheses are retained and marked, not deleted (2026-08-02)

**Decision.** When a disease-level mechanistic hypothesis has been overturned, it is
curated as a `mechanistic_hypotheses` entry with `status: DEPRECATED` — kept in the entry,
not removed from it — and the rendered page states explicitly that DisMech does **not**
assert it as the current mechanism.

- **Retain rather than delete.** An overturned model that is still circulating in reviews,
  textbooks or older diagnostic criteria is exactly the claim a reader arrives wanting to
  check. Deleting it leaves them with nothing to check against; recording it with a verdict
  and cited refutations is the more useful artifact.
- **Citation volume does not decide standing.** A deprecated hypothesis will often carry
  *more* supporting than refuting citations, because the supporting literature accumulated
  for decades before the refutation landed. Where evidence conflicts, DisMech follows the
  more recent and more direct evidence — a quantitative or orthogonal-method refutation
  outweighs any number of narrative citations asserting the older view.
- **Both sides get cited.** The hypothesis's own `evidence` list carries the founding
  supporting citations (`supports: SUPPORT`) alongside the refutations (`supports: REFUTE`),
  each with a verified snippet, so the assessment is auditable rather than editorial
  assertion. Renderers surface the SUPPORT/PARTIAL/REFUTE split as an evidence-balance row.
- **Disputed nodes are marked, not asserted.** A pathophysiology node that exists only to
  represent a deprecated model carries `mechanism_confidence: HYPOTHETICAL`, and its causal
  edges opt into the deprecated `hypothesis_groups` so the disputed chain stays separable
  from the live models. Hypothesis chips on nodes and edges carry the deprecated status.
- **No conformance on a disputed claim.** Do not add a `conforms_to` edge to a mechanism
  module on the strength of a hypothesis curated as DEPRECATED — that would assert as fact
  precisely what the assessment rejects.

**Rationale.** Mechanism knowledge bases fail readers in two opposite ways: by omitting
retired models (so a reader meeting the claim in the literature has no recourse), and by
listing them undifferentiated alongside live ones (so retired models keep accruing
authority). Recording the model *with* an explicit verdict and a visible evidence balance
avoids both. The worked example is the beta-amyloid hypothesis of sporadic inclusion body
myositis (`amyloid_beta_proteotoxicity` in `kb/disorders/Inclusion_Body_Myositis.yaml`),
whose literature is itself the documented subject of a citation-distortion analysis
(PMID:19622839) — the clearest available case of citation weight outrunning data. See
[the exploration report](../reports/ibm-amyloid-beta-hypothesis-2026-08-02.md).

### 6b. Community sources may corroborate, never carry, a claim (PROPOSED)

**Status: PROPOSED — awaiting a maintainer decision.** Drafted from the pattern worked out
in [#7674](https://github.com/monarch-initiative/dismech/pull/7674) (FSHD), which is
approved on content and held open on exactly this question. Nothing in `kb/` uses these
tags yet, so this section describes what the rule *would* be; it is not yet in force.

**Decision.** Patient-advocacy content and public patient-community content are citable
`url:` references, in two distinct classes with different rules, and neither may be the
sole support for a curated claim.

- **`PatientOrganization`** — published disease-education content from an advocacy
  organization or disease foundation. Institutionally authored, publicly distributed, no
  personal data. It may corroborate a claim and may supply the experiential phrasing a
  community actually uses, which is often what makes an under-reported manifestation
  findable at all.
- **`PatientCommunity`** — user-generated content from a public patient community. It is
  evidence about **salience** — what a community discusses and prioritizes — and never
  evidence about biology.
- **Never sole support.** Every evidence block containing a community-tagged reference
  must also carry at least one non-community reference. Enforced by
  `test_community_sourced_evidence_is_not_sole_support` in `tests/test_data.py`.
- **Adjudicate, don't promote.** A community signal that literature corroborates becomes a
  normal curated entry; one it does not becomes a `discussions` entry recording an
  explicitly unvalidated lead. It does not become a phenotype on community assertion alone.
- **Aggregate only, for `PatientCommunity`.** Cite aggregate topics and listings. Do not
  quote an individual's personal health narrative, and do not commit a raw HTML capture of
  a user-generated page — those carry usernames and self-disclosed health status into git
  permanently. Cache the extracted titles instead.
- **Public and consented.** A closed group (a private Facebook family group) is out of
  scope regardless of technical accessibility: members disclosing health information there
  have not consented to public aggregation. Where a community signal needs quantifying, a
  national patient registry is the consented substitute.
- **Tag it.** Community references carry a `ReferenceTagEnum` tag on their top-level
  `references:` entry, so the sourcing class is filterable and — if this policy is later
  reversed — retractable by query rather than by re-reading every entry.

**Rationale.** Patient communities describe manifestations the primary clinical literature
under-represents: in FSHD, fatigue and pain rank at nearly the prevalence of the weakness
that defines the disease, and the mechanism graph explains neither. Refusing the source
class entirely means those manifestations stay invisible to the KB. Accepting it without
constraint means unreviewed assertion enters a knowledge base whose credibility rests on
the exact-quote pipeline. The corroboration rule takes the useful half — community sources
are good at telling you *where to look* — while keeping every curated claim standing on
something citable.

The two classes are separated because they are not the same risk. An advocacy
organization's symptom page is institutional publishing that happens not to be indexed in
PubMed. A forum is individuals talking about their own health. In #7674 the organization
produced seven of the eight community-sourced evidence items and the forum produced one,
which is also the shape of the yield: organized advocacy content substantially
out-performed the forum as a curation input.


## 7. Curation process & governance

**Decision.** DisMech is **agent-forward**: most curation is performed by AI agents,
initiated either by humans or by GitHub Actions.

- Humans **initiate** work; agents execute and may also author issue/PR comments.
- The default assumption is that issue/PR contents *and comments* are AI-generated; humans
  are **not** assumed to have verified every line their agent produced. Mark human-authored
  content explicitly if desired.
- **Human-in-the-loop is the PR review gate.** Every PR receives an automated
  review and must address its findings. Unresolved disagreements are escalated to a human
  maintainer.

See [`CONTRIBUTING.md`](https://github.com/monarch-initiative/dismech/blob/main/CONTRIBUTING.md)
and the workflow definitions in `.github/workflows/`.


## 8. Prevalence representation

**Decision.** Disease occurrence is modeled with **structured, separated slots** on the
`Prevalence` class rather than the single overloaded `percentage` field that preceded
them. The strategy mirrors how phenotype frequency is banded (`FrequencyEnum`), but at
population scale and without discarding the underlying number.

`Prevalence` now carries:

- **`population`** — cohort / geography only (e.g. "Worldwide", "Ashkenazi Jewish
  population"). Measure-type qualifiers that used to be jammed in here (e.g. "(Orphanet
  point prevalence)") belong in `measure_type`.
- **`measure_type`** (`PrevalenceMeasureEnum`) — which epidemiological measure the record
  reports: `POINT_PREVALENCE`, `BIRTH_PREVALENCE`, `LIFETIME_PREVALENCE`,
  `PERIOD_PREVALENCE`, `ANNUAL_INCIDENCE`, `CARRIER_FREQUENCY`, `CASES_IN_LITERATURE`,
  `UNKNOWN`. This prevents a point prevalence from being silently compared with an
  incidence rate or a literature head-count.
- **`prevalence_class`** (`PrevalenceClassEnum`) — the coarse, always-fillable, queryable
  band. Numeric tiers are the **Orphanet prevalence classes** (`>1/1,000`, `1-5/10,000`,
  `1-9/100,000`, `1-9/1,000,000`, `<1/1,000,000`, `Not yet documented`), so records that
  quote Orphanet (and the `ORPHA:` structured source) map directly; qualitative tiers
  (`COMMON`, `RARE`, `ULTRA_RARE`, `UNKNOWN`) cover prose-only records with no numeric
  estimate. This is the population-rate analog of phenotype `FrequencyEnum`.
- **`rate_per_100000`** (+ **`rate_low`** / **`rate_high`** for ranges) — one normalized,
  machine-comparable number in cases per 100,000. Every source notation (`%`,
  `per 100,000`, `per million`, `1 in N`, Orphanet `N / M`) converts losslessly into it.
- **`notes`** retains the verbatim source phrasing; **`evidence`** is unchanged.
- **`percentage`** is **deprecated** (kept read-only during transition). It was an `Any`
  (float | int | string) field that, across the KB, conflated measure type, rate, unit,
  uncertainty, and a qualitative fallback in ~six mutually incompatible notations
  (audited: of 834 records, only ~5% were an actual percentage; ~18% were unit-ambiguous
  bare numbers, ~18% qualitative prose, the rest split across `per N` / `1 in N` /
  Orphanet bands / explicit `%`). Do not populate `percentage` on new records.

**Migration.** `scripts/migrate_prevalence.py` performs a non-destructive,
idempotent backfill: it parses the deterministic notations into the structured slots and
**leaves genuinely ambiguous records (bare unit-less numbers, free-text head-counts)
unconverted**, listing them for manual resolution in
`research/prevalence_migration_report.md`. Measure type is inferred only from the
`percentage` value and `population` label, never from prose `notes` (which routinely
mention "newborn screening" / "carrier frequency" / "incidence" as background and would
otherwise mislabel ordinary point-prevalence records); auto-defaulted measure types are
flagged for verification in the same report.

**Rationale.** One field cannot be both honest about imprecision and machine-queryable.
Splitting the measure out, banding coarsely (Orphanet-aligned), and keeping one normalized
rate gives a value that is always fillable (the band), precise when the source supports it
(the rate), and never conflates incompatible epidemiological measures. Because prevalence
is not yet rendered on disorder pages, the remodel carries no display-breakage risk.

**Per-gene case fractions (the genetic-spectrum analog).** For a genetically
heterogeneous disease, "what share of cases does each gene explain?" is a *different axis*
from population occurrence — it is cohort/ancestry-dependent (e.g. BBS1 dominates European
Bardet-Biedl cohorts, BBS10 others) and needs its own population + evidence per estimate.
It was previously handled only by the overloaded free-text `Genetic.frequency` field
(qualitative prose such as "one of the most prevalent BBS genes") with the actual numbers
trapped inside evidence `snippet:` text. It now has a structured home: `Genetic.case_fractions`
(multivalued `GeneCaseFraction`), mirroring the Prevalence remodel — `population` (cohort)
+ `case_fraction_percent` (with `case_fraction_low`/`case_fraction_high` and optional
`cohort_size`) + `evidence` + `notes`, while `frequency` is retained as the coarse,
always-fillable qualitative band. This keeps the relative genetic spectrum distinct from
population occurrence (`Prevalence`) and from population allele frequency. Worked example:
`Bardet-Biedl_Syndrome` carries per-cohort case fractions across five genes — BBS1
(24.6% German / 27% metabolic / 7% Indian), BBS10 (32.8% / 30% / 10%), and the minor
genes ARL6/BBS3 (14%), MKKS/BBS6 (10%), and BBS9 (10%) in an Indian cohort — making the
ancestry-dependence of the genetic spectrum explicit (BBS1 falls from ~25% in Europeans
to 7% in the Indian cohort).


## 9. Imaging & detection modality representation

**Decision.** In-vivo imaging findings are modeled with a **dedicated, ontology-bound
`ImagingFinding` class** on the `Disease` entry (slot `imaging_findings`), the macroscopic
/ in-vivo counterpart of `HistopathologyFinding`. The **modality** (the test) and the
**finding** (what is seen) are represented separately, because they answer different
questions and bind to different vocabularies:

- **`modality`** (`ImagingModalityEnum`) — a small closed set (MRI, functional MRI, CT,
  PET, SPECT, ultrasound, X-ray, mammography, angiography, OCT, other), with `meaning:`
  values bound to the **NCI Thesaurus Diagnostic Imaging branch** (e.g. `NCIT:C16809`
  Magnetic Resonance Imaging, `NCIT:C17204` Computed Tomography, `NCIT:C17007` PET).
- **`imaging_finding_term`** (`ImagingFindingDescriptor`) — the imaging appearance, bound
  via `ImagingFindingTerm` to the **NCIT Imaging Finding branch** (`NCIT:C176708` /
  `NCIT:C199145`) and/or the **HP Phenotypic-abnormality branch** (`HP:0000118`), since
  most radiologic observations coincide with a described phenotype (white-matter lesions,
  atrophy, hyperintensity). The term binding is **RECOMMENDED, not REQUIRED**: many
  specific radiologic appearances (e.g. "gadolinium-enhancing lesion") lack a dedicated
  NCIT/HP term and are carried on `preferred_term` alone rather than being forced onto an
  ill-fitting code or fabricated.
- **Body site** reuses the existing `located_in` (UBERON) slot, plus `laterality` and
  `spatial_extent` (focal/multifocal/diffuse), because imaging is inherently spatial. An
  optional `phenotype_term` cross-links the finding to the HP phenotype it also maps to.

**In scope.** Imaging *findings* that are mechanistically- or diagnostically-meaningful
readouts — a lesion, an atrophy pattern, a contrast-enhancement behavior that reflects the
underlying pathophysiology or defines a diagnostic criterion (`diagnostic: true`).

**Out of scope.** Acquisition/protocol parameters, per-patient reads, and radiology
decision support — consistent with §1 (DisMech is not a diagnostic decision-support tool).
`ImagingFinding` is the in-vivo/macroscopic sibling of `HistopathologyFinding` (biopsy/
microscopy) and is distinct from the generic free-text `diagnosis` slot (which records that
a test was ordered / its presence-absence result) and from the molecular `Biomarker*` /
`Biochemical` machinery (lab analytes, unchanged).

**Rationale.** Before this decision, imaging leaked into four places — free-text
`diagnosis` entries (e.g. `"MRI with Gadolinium Contrast"`), free-text `imaging_requirements`
in criteria sets, HP `phenotypes` / UBERON anatomy, and `notes`/`evidence` prose — none of
it queryable by modality or finding. Splitting modality from finding makes "which diseases
show white-matter T2 lesions on MRI?" answerable while keeping the anti-hallucination
guarantee (every attached term must be a real NCIT/HP/UBERON term with a matching label).

**Ontology choice.** RadLex is the natural radiology vocabulary but is **not hosted on EBI
OLS4** (it lives on BioPortal, which needs the `bioportal:` adapter + an API key), so it is
not wired into `conf/oak_config.yaml` today. The grounding therefore uses **NCIT (already
OLS-served) + HP**, which covers modality cleanly and findings adequately; a future
tightening to RadLex-grade finding granularity is a deferred follow-up (see §12). Because
the finding binding is RECOMMENDED, the ontology gap does not block curation.

**Worked example.** `Multiple_Sclerosis` carries two `imaging_findings`: multifocal
periventricular white-matter lesions on MRI (bound to `HP:0007052`, `located_in`
`UBERON:0003544` brain white matter, `spatial_extent: MULTIFOCAL`, `diagnostic: true`) and
a gadolinium-enhancing lesion (modality MRI, `preferred_term`-only — the RECOMMENDED-no-code
case).

## 10. Electrophysiologic findings: phenotype post-composition, *not* a finding class

**Decision.** In-vivo electrophysiologic findings (EEG, and by extension EMG/EKG) are
modeled as **ordinary `phenotypes` post-composed with an optional `electrophysiology:`
sidecar** (`ElectrophysiologyContext`), **not** as a dedicated `ElectrophysiologyFinding`
class. This is a deliberate, principled *asymmetry* with imaging (§9), and it turns on a
single test:

> **If the finding term already lives in the phenotype ontology, it belongs in `phenotypes`
> and needs no separate class. If it doesn't, it needs one.**

Imaging findings bind to the **NCIT Imaging Finding** branch and histopathology to **NCIT
morphology** — vocabularies *outside* HP — so `ImagingFinding` / `HistopathologyFinding`
exist to give those terms a home, and their **modality** axis (MRI vs CT vs PET) is a real,
queryable dimension with its own NCIT branch. **Electrophysiologic findings are different on
both counts**: the terms *are* HP phenotypes (the EEG subtree `HP:0002353`, EMG `HP:0003457`,
EKG `HP:0003115` all descend from `HP:0000118`), so they are already correctly typed as
phenotypes; and the "modality" is near-degenerate (almost always EEG, and implied by the
term itself). Both pillars that justified a dedicated imaging class collapse for EEG, so a
sibling class would only *re-home* terms that were already phenotypes and bolt on a
low-value modality axis.

**The sidecar.** A phenotype whose `phenotype_term` is an EEG/EMG/EKG finding may carry an
optional `electrophysiology:` block (`ElectrophysiologyContext`) with exactly the axes a
flat HP term cannot express:

- **`electrophysiology_modality`** (`ElectrophysiologyModalityEnum`; EEG, video-EEG, ECG,
  EMG, NCS, evoked potential, PSG, MEG) — `meaning:` bound to the NCI Thesaurus
  diagnostic-procedure branch (`NCIT:C38054` EEG, `NCIT:C38053` ECG, `NCIT:C38056` EMG).
- **`ictal_state`** (`IctalStateEnum`: ICTAL / INTERICTAL / POSTICTAL).
- **`recording_state`** (`EEGRecordingStateEnum`: awake / asleep / drowsy / sleep-deprived /
  photic-stimulation / hyperventilation).

This is the same post-composition move dismech already uses for `temporality`,
`clinical_course`, `severity`, and `onset` on descriptors — the EEG-specific qualifiers just
travel in a named sidecar so they don't pollute the generic `PhenotypeDescriptor`.
Localization/laterality/extent reuse the descriptor slots already on `phenotype_term`; the
HP term (e.g. "EEG with focal epileptiform discharges") usually already carries them.

**Preclinical / no-HP-term findings** stay phenotypes too — a `preferred_term`-only
phenotype (no bound `term:`) carrying the sidecar, e.g. an animal-model *electrographic
seizure* (no HP term exists), tagged `evidence_source: MODEL_ORGANISM`. This keeps ictal
model-organism EEG alongside the interictal human findings instead of stranding it in prose.

**Rationale / history.** An `ElectrophysiologyFinding` sibling class was first built by
analogy to §9, then **reverted** once the analogy was checked and found not to hold (EEG
terms are HP phenotypes; imaging terms are not). Recording the reversal here so the register
reflects the corrected reasoning, not the false symmetry.

**Category is already HP-derived — the sidecar does not touch it.** The disorder-page
renderer does *not* group phenotypes by the free-text `phenotypes.category` string; it
derives the broad category from the **`phenotype_term`'s HPO ancestry**, walking
`rdfs:subClassOf` to the 22 top-level children of `HP:0000118` (`HpoCategoryProvider` /
`HPO_TOP_LEVEL_CATEGORIES`, already codified as the `PhenotypeCategoryEnum` in
`schema/classifications/phenotype_category.yaml`). EEG findings roll up to **Nervous
System** (`HP:0000707`), so that is the correct `category` value — *not* a novel
"Electrophysiologic" bucket. **The EEG-ness is carried entirely by the `electrophysiology:`
sidecar, not by the category**, which is exactly why the sidecar exists: it adds the
electrophysiologic axes without disturbing the organ-system categorization.

**No category constraint is wanted here.** A rule of the form *category = X ⇒ `phenotype_term`
under X* would be **circular** — the category is *derived from* the term's HP ancestry, so it
has no independent content to check — and the 22 top-level categories are too coarse to pick
out "EEG finding" anyway (EEG rolls up to the whole Nervous System). The sidecar is an
optional post-composition qualifier exactly like `temporality` / `clinical_course` /
`severity` / `onset`, **none of which are category-gated or rule-enforced**; this one follows
the same convention-over-constraint pattern. The only guardrail that would even type-check is
"sidecar present ⇒ term under `HP:0002353`/`0003457`/`0003115` *or* term-less (the preclinical
`preferred_term`-only case)", and that is at most an advisory lint, not a schema rule.

**Deferred (see §12).** Independently of EEG, the `PhenotypeCategoryEnum` already exists but
is not yet wired to the `phenotypes.category` slot (still `range: string`); binding it, or
deprecating the hand-entered field in favour of the HP-derived value, is a separate cleanup.

**Worked example.** `Dravet_syndrome` carries five EEG phenotypes (`category: Nervous
System`) — the four interictal human patterns (multifocal / focal / generalized epileptiform
discharges and interictal epileptiform activity, HP-bound, sidecar `ictal_state:
INTERICTAL`), plus one preclinical `preferred_term`-only phenotype — ictal electrographic
seizures in the Scn1a+/- mouse model (sidecar `electrophysiology_modality: EEG`,
`ictal_state: ICTAL`, `evidence_source: MODEL_ORGANISM`).

**Linking investigation-readout phenotypes into the pathograph (`reports_on`).** Many HP
terms are *investigation results* rather than states of the organism — an *abnormal
electroretinogram* (`HP:0000512`), an abnormal EEG, an *elevated circulating creatine kinase
concentration*. They are legitimately HP phenotypes and stay in `phenotypes` (per the test
above), but functionally they are **readouts of** an underlying mechanism, not causal
participants in disease progression. As a result they tend to float as disconnected nodes in
the pathograph: nothing lists them as a `downstream` target and they carry no `sequelae`. The
tempting fix — adding a `downstream` edge `mechanism → Abnormal ERG` — is **wrong**, because a
`downstream`/`causes` edge asserts causal disease progression, whereas the test merely
*measures* the mechanism.

**Decision.** A phenotype may carry a `reports_on:` list (`PhenotypeReadout`) linking it to
the pathograph node whose underlying state it measures or reflects, exactly mirroring the
`Biochemical.readouts` (`BiomarkerReadout`) mechanism already used for molecular biomarkers.
It reuses the same `BiomarkerReadoutRelationshipEnum` (`READOUT_OF` / `CORRELATES_WITH` /
`PREDICTS` / `PHARMACODYNAMIC_MARKER_OF`), direction, and endpoint-context vocabularies, and
renders as the **same dashed observational edge** (`mechanism -.-> readout`, `graph.py`
`predicate: readout`) — *not* a solid causal arrow. `PhenotypeReadout` is deliberately the
**lean** counterpart of `BiomarkerReadout`: it omits the surrogate-endpoint/regulatory slots
(`regulatory_endpoint_refs` and the FDA source-table bridge) that belong only to molecular
biomarker readouts. This keeps the term where HPO places it (`phenotypes`), preserves the
"reports-on ≠ caused-by" distinction the schema already encodes for biomarkers, and makes the
otherwise-orphan test-result phenotype a first-class, evidenced pathograph edge.

**Worked example.** `Bardet-Biedl_Syndrome`'s *Abnormal electroretinogram* phenotype now
`reports_on` the *Photoreceptor outer-segment transport defect* pathophysiology node
(`relationship: READOUT_OF`, `direction: NEGATIVE`, `endpoint_context: DIAGNOSTIC`),
replacing the previous — semantically incorrect — `downstream` causal edge from the
mechanism to the ERG. The ~200 `Elevated/Decreased circulating … concentration` lab-readout
phenotypes are candidate backfills (tracked in §12).

## 11. Reader-facing disclaimers (AI curation & not medical advice)

**Decision.** Every reader-facing DisMech page carries a **disclaimer bar** stating two
things: that the resource is AI-curated and AI-maintained, and that it is not medical advice.
A single canonical long-form statement lives in [`docs/disclaimer.md`](../disclaimer.md); the
bar links to it. The bar is shown by default on every page and may be dismissed **for the
browsing session only** — see the "Dismissible for the browsing session" design point below
for the scope and its rationale. *(This paragraph originally read "persistent,
non-dismissible"; revised by
[#7421](https://github.com/monarch-initiative/dismech/issues/7421).)*

**Why page-level rather than documentation-level.** §7 already records that DisMech is
agent-forward, and §6 records the evidence policy — but both are *contributor-facing process
documentation*. The common way a reader encounters DisMech is by landing on a single
disorder page from a search engine or an external link, never seeing the project
documentation at all. Provenance and fitness-for-use therefore have to travel with the page.

**Where it is implemented.**

| Surface | Mechanism |
|---|---|
| Generated KB pages (disorder, module, grouping, comorbidity, classification, project, research, and their index pages) | `src/dismech/templates/_disclaimer.html.j2` + `_disclaimer.css.j2`, `{% include %}`-ed into every full-page template (the same partial pattern already used for `_palette.css.j2`) |
| Hand-maintained site pages (`index.html`, `app/`, `details/`) | The same markup inlined, kept in step with the partial |
| MkDocs documentation site (`elements/`) | `copyright:` footer in `mkdocs.yml`, plus admonitions on `docs/index.md` and `docs/about.md` |
| Repository | Disclaimer section at the top of `README.md` |

**Design points.**

- **Dismissible for the browsing session.** *(Revised by
  [#7421](https://github.com/monarch-initiative/dismech/issues/7421); this decision originally
  read "Not dismissible".)* The bar carries a close button, and the closed state is recorded
  under the `dismech-disclaimer-dismissed` **sessionStorage** key. sessionStorage is scoped to
  a single tab and cleared when that tab closes, so moving between DisMech pages in the same
  tab keeps the bar dismissed, while a fresh tab or a later visit shows it again.

    **Deliberately not localStorage.** Permanent dismissal would let a reader silence the
    statement once and never see it again. Session scope keeps the escape hatch — the bar is a
    banner, and a reader working through twenty disorder pages should not have to see it twenty
    times — without turning "I have read this" into "never tell me again". A test asserts the
    localStorage API is not used *by the disclaimer script* on any surface, so this cannot
    regress by accident. Deliberately scoped to that script rather than to whole files:
    `disorder.html.j2` legitimately uses localStorage elsewhere, for its Q&A answer cache.

    One consequence worth knowing: sessionStorage follows the *tab*, not the page load. A
    reader who dismisses the bar and then types a DisMech URL into that same tab will not see
    it again; it takes a new tab (or a later visit) to bring it back.

    Mechanics worth keeping: the control is a real focusable `<button>` with an accessible
    label and tooltip, not the click-anywhere `.notice-banner` behaviour, which would fight the
    link inside the bar. It is CSS-hidden by default and revealed by the script, so a reader
    without JavaScript is never shown a control that cannot work. The script is inline and
    synchronous directly after the bar, so an already-dismissed bar is hidden before first
    paint instead of flashing. Every `sessionStorage` access is inside a `try`, because the
    property getter itself throws when storage is blocked; the bar then simply stays visible.
    Dismissing moves focus to the page's `main`/`h1` rather than letting it fall back to
    `<body>`, so a keyboard reader keeps their place.

    Layout: the bar is a flex row and the button sits **in flow**, so it cannot overlap the
    text however the bar wraps. The button carries a 28px right margin to clear the
    [Hypothes.is](https://web.hypothes.is/) sidebar, which mounts a toolbar over the right edge
    of every page that embeds the annotation client (`disorder.html.j2`, `module.html.j2`) and
    swallows clicks there. This is not cosmetic: measured in headless Chromium, a button at
    `right: 8px` is unclickable on disorder pages at both 1280px and 375px wide. The clearance
    is therefore **not** dropped on narrow viewports.

- **A dismissed page still carries the statement.** Because the bar can be closed, generated
  disorder and module pages also carry `_disclaimer_footer.html.j2` — a one-line,
  non-dismissible disclaimer in the page footer, worded to match the MkDocs `copyright:`
  footer. Without it, the reader §11 exists for (one disorder page, arrived from a search
  engine) could dismiss the bar and be left on a page with no disclaimer at all: the MkDocs
  `copyright:` footer renders only on `docs/` pages, and `render.py` pages have their own
  footer. **Known gap:** disorder and module are the only full-page templates with a
  `<footer>`, so grouping, comorbidity, classification, project and research pages have no
  footer line; on those, a dismissed bar does leave the page bare until the session ends.
- **Distinct from `.notice-banner`.** The pre-existing `.notice-banner` (pre-alpha content
  warning) is also dismissible, but only for the page view — it just removes itself and
  returns on the next page. The disclaimer is styled neutral grey rather than amber, and holds
  its dismissal for the session, precisely so the two read as different things when they
  appear together.
- **Top of page, not footer.** A reader who leaves after the first screen must still have
  seen it. (The footer line above is an *addition* for the dismissed case, not a relocation.)
- **One canonical wording.** `docs/disclaimer.md` is the source of truth; the banner is its
  summary. `tests/test_disclaimers.py` gates that every full-page template and every
  hand-maintained site page still carries the disclaimer, so a new template cannot silently
  ship without one — and, since #7421, that each of them also carries the dismiss control, the
  shared sessionStorage key (and *not* the localStorage API), and the `[hidden]` rule that
  makes dismissal actually hide the bar (`display: flex` on the bar outranks the user-agent
  rule for the `hidden` attribute).

**Scope.** Internal/derived QC surfaces are excluded — they present curation-completeness
metrics, not disease claims: `dashboard/` (generated by `just gen-dashboard`) and
`frontpage-candidates/` (a design-candidate gallery). `pages/nih-topics/index.html` is
*included* despite being a coverage report, because it sits under `pages/` alongside the
disease surfaces and links out to disease and project pages; it is generated from an inline
template string in `scripts/gen_nih_topics_summary.py` rather than from
`src/dismech/templates/`, so it is covered by its own test rather than by the template glob.

**Origin.** [#7182](https://github.com/monarch-initiative/dismech/issues/7182). Revised by
[#7421](https://github.com/monarch-initiative/dismech/issues/7421) (dismissible for the
browsing session, plus the non-dismissible footer line).

## 12. Gaps

This section details decisions we have **not yet made or formalized**.

| Area | Status | Tracking |
|---|---|---|
| Experiment-grounded evidence (`experiment.design` / `inference.role`) | Design exploration, **not yet a schema change.** The `EvidenceItem` model is a validated citation-pointer (real reference + exact snippet + validator = citation integrity) with a thin appraisal layer — `supports` is polarity, `evidence_source` is a coarse organism bucket, and neither records *what experiment* produced a claim or *how* the mechanistic edge was inferred from it. Proposal: an optional `experiment{design, system, perturbation, readout, result, inference}` block plus two small closed enums — `experiment.design` (*how it was shown*) and `inference.role` (*necessity / sufficiency / rescue / direct-physical / therapeutic-rescue*, what the result licenses about the edge), mutually constraining so strength is *derived, not authored* and `experiment.result.snippet` stays substring-validated. Bespoke enum preferred over ECO (which types entity→term annotations, not causal-graph assertions); SEPIO reserved for the export layer. Worked on the FH PCSK9 sub-graph. | [The Evidence Model](evidence-model.md) · [FH worked example](../reports/fh-experiment-grounded-evidence-2026-07-30.md) |
| Chromosomal-disorder curation guidelines | Not yet written; domain-specific extension of this register | [#3756](https://github.com/monarch-initiative/dismech/issues/3756) |
| Structural `knowledge_gaps:` schema slot | Deferred; knowledge gaps currently modeled via `discussions` (`kind: KNOWLEDGE_GAP`) | schema follow-up |
| `would_support` / `would_refute` range | **ENACTED (#9224).** These two `Experiment` slots hold **entity references only** — the `[<file>:]<kind>#<name>` grammar shared with `attaches_to` — and name *what a result bears on*. A prose statement of *what would be observed* goes in the sibling `supporting_outcome` / `refuting_outcome` slots. The alternative (widen the reference slots to accept both forms and split on whitespace at render time) was rejected: the two are different **types**, not two spellings of one. "No enrichment of these lesions in tissue would indicate that the dominant clinical resistance mechanism lies outside the bypass lesions currently modeled at this node" is a conditional inference with no referent, and a slot whose meaning turns on whether its value contains a space cannot be exported. The ~51 prose values that motivated the issue have been migrated (zero remain across `kb/`), and the anchors now resolve: `render._build_semantic_ref_index` is driven by `entity_refs.SECTION_KEYS` (#9193), so **562 of 564** references in these slots render as live in-page links rather than dead chips — the 2 exceptions name `diagnosis` and `prevalence`, sections the disorder page renders no card for, which is a page-coverage gap rather than a modeling one. Gated by `test_entity_ref_foreign_keys`, which now fails a prose value, an unknown `<kind>`, or a dangling anchor in these slots, with **no baseline** — the backlog is zero, so a finding is always newly introduced. **Not precluded:** if a structural `knowledge_gaps:` slot (#2617) later wants a `ModelMechanismLink`-shaped object carrying a target *plus* qualifying prose *plus* its own evidence, this decision is compatible with it — the prose lives in a named slot either way. | [#9224](https://github.com/monarch-initiative/dismech/issues/9224) · [#9193](https://github.com/monarch-initiative/dismech/issues/9193) |
| Hypothesis-exploration report assessments | **ENACTED (PR #7017).** A focused hypothesis report is a research lead, not disease-level curated evidence. One standalone LinkML-validated YAML sidecar is stored for each `<provider>-assessment-by-<assessor>` pair under `kb/hypotheses/<Disease>/<hypothesis_id>/assessments/`; optional Markdown/PDF files with the same stem are human-readable renderings. The sidecar captures an overall qualitative verdict plus claim-level `RETAINED` / `QUALIFIED` / `REJECTED` / `NEEDS_VERIFICATION` dispositions, each optionally anchored by a verbatim raw-report quote. Validation enforces layout, filename metadata, report-quote anchoring, and artifact links. Literature identifiers in a review are context, not disease-YAML evidence; promotion still requires normal reference-cache and evidence validation. A cross-provider synthesis remains optional and does not replace independent provider-by-assessor reviews. | `src/dismech/schema/hypothesis_assessment.yaml`; `docs/hypothesis-report-assessments.md` |
| Hypothesis-based phenotype algorithms | **ENACTED (2026-07-12, `@cmungall`-approved).** `definition_type: PHENOTYPE_ALGORITHM` previously assumed established/validated grounding. `Definition` now carries an orthogonal `derivation_basis` (`ESTABLISHED_CRITERIA` / `MECHANISTIC_HYPOTHESIS` / `MODEL_SYSTEM_EXTRAPOLATION`); **reuses the existing `attaches_to` slot** to link the pathograph node(s)/edge(s) it is predicated on (so the hypothesis basis is *inferred* from those edges' `hypothesis_groups` → `mechanistic_hypotheses[].status`, not stored as a drift-prone duplicate ID); and a **structured `validation_status` object** (`AlgorithmValidationStatus`: `status` enum `PROPOSED` / `UNVALIDATED` / `VALIDATED_AGAINST_GOLD_STANDARD` + free-text `rationale` + optional `evidence`). Net effect: a mechanism-predicated EHR case-finding query (e.g. fever-triggered arrhythmia surfacing latent CACNA1C carriers) is not conflated with a consensus/OHDSI-validated phenotype. Gated by `test_hypothesis_based_definition_attaches_to_foreign_keys` (a `MECHANISTIC_HYPOTHESIS` definition must have resolving `attaches_to` refs). Worked examples spanning the spectrum: `Timothy_Syndrome` (`fever_exacerbated_cav1.2`; `MECHANISTIC_HYPOTHESIS`/`PROPOSED`, zebrafish), `Brugada_Syndrome` (fever-unmasking of the type-1 ECG; `ESTABLISHED_CRITERIA`/`UNVALIDATED`), `Long_QT_Syndrome` (QT-prolonging-*drug* unmasking of latent congenital LQTS; `ESTABLISHED_CRITERIA`/`UNVALIDATED` — a pharmacological rather than physiological trigger), and `Malignant_Hyperthermia_of_Anesthesia` (*anesthetic* trigger, skeletal-muscle RYR1/CACNA1S; `ESTABLISHED_CRITERIA`/`UNVALIDATED` — the first non-cardiac example, whose definition `attaches_to` the entry's existing trigger node). See [hypothesis-based-phenotype-algorithms.md](../hypothesis-based-phenotype-algorithms.md) and the candidate register in [reports/hypothesis-driven-ehr-case-finding](../reports/hypothesis-driven-ehr-case-finding-2026-07-12.md). **Remaining follow-ups:** advisory declared-vs-inferred consistency lint; renderer badge; KGX/BioLink export treatment (suppress or specially mark). | [#6245](https://github.com/monarch-initiative/dismech/issues/6245) |
| `updated_date` field | Deprecated in favor of git history; legacy entries may retain it pending bulk cleanup | — |
| Deprecated `prevalence.percentage` cleanup | `percentage` superseded by structured prevalence slots (§8) and deprecated. The bare-number unit-ambiguity backlog is effectively resolved: of 199 records, **166 are converted** via `scripts/resolve_bare_prevalence.py` plus reviewed batches — 91 low-value rare-disease prevalences, 47 high-percent population/cohort prevalences (conditional ones qualified by their `population` field), 9 hand-fixed `DISAGREE`, and 19 final records (12 uncorroborated-but-legit + 7 filter false-positives) using the rule **decimal = percent, scientific-notation = proportion** (e.g. CHIME `1e-06` = 1/million; Cockayne `4e-06` = 1/250,000; carrier/birth measures set where stated). All additive; `percentage` preserved. The **33 not converted are not a unit problem**: 32 are records that are *not population prevalence at all* (`MISPLACED_STAT` in `research/prevalence_bare_number_report.md` — metastatic-cancer 5-year survival, staging fractions, complication rates, and fraction-of-category such as "X% of all lymphomas/leukemias/cancers"), which belong in a different slot and need **relocation, not unit-fixing** — a distinct data-quality task pending a schema home for survival/staging/subtype-share data; plus 1 genuinely-ambiguous record (Nephronophthisis `0.1-1.0`, neither a clean percent nor proportion with no corroborating evidence). Plus ~8 free-prose head-counts. `percentage` field removal is deferred until the misplaced-data relocation lands. **Post-migration correction (PR review):** a systematic scan found **19 records across 16 files** where a *fraction-of-category* or *penetrance* value (with the qualifier living in `notes`, so the percentage-only guard missed it) had been wrongly converted to a population `rate_per_100000` — e.g. Osteogenesis_Imperfecta_Type_II `50%` (half of prenatal-onset OI cases → 50,000/100k), HPAH/FXTAS carrier **penetrance** (~40% → 40,000/100k), Minimal_Change_Disease (70–90% of idiopathic NS), Cholesteatoma (419/1710 otitis-media patients). These had their `measure_type`/`prevalence_class`/`rate_*` slots stripped (bare `percentage` preserved). The migration guard was hardened accordingly: `FRACTION_OF_CATEGORY_RE` now also matches cohort head-counts (`N of M`) and `% of <solved/idiopathic/sporadic/typhoidal/…>` categories stated in the percentage, and a new `PENETRANCE_RE` (safe to run against `notes`) catches penetrance/lifetime-risk qualifiers. Bare-percentage cohort fractions whose qualifier is *only* in prose remain inherently ambiguous from the value alone and are corrected by hand rather than by an aggressive notes scan (which would false-positive on records like Lathyrism, whose notes cite a cohort count but whose `percentage` is a genuine population estimate). **Second correction batch (PR review):** a follow-up KB-wide scan surfaced a further class of measure-type/conditional errors on rate-bearing records — (a) **genotype-conditional cumulative incidence / penetrance** stated as "N% diagnosed by age X" (Hemochromatosis male C282Y homozygotes 56.4% by age 80) or "cumulative risk of new cases up to age N" (Oppositional_Defiant_Disorder), which were stripped like the penetrance records; (b) **wrong measure_type** where the type lived only in `notes`/snippet — lifetime prevalence tagged POINT (Anorexia_Nervosa, Migraine_with_Aura → LIFETIME_PREVALENCE) and 12-month prevalence tagged POINT (Obsessive-Compulsive_Disorder → PERIOD_PREVALENCE); (c) **cohort-conditional risk-factor rates** (Furunculosis S. aureus nasal-carriage 60%/36%, Acute_Hypotension 88% intraoperative-event rate in ASA 3–4 surgical patients), stripped; and (d) a **two-figure percentage** where the parser captured the incidence not the prevalence (Systemic_Lupus_Erythematosus North America "23.2/100k incidence; 241/100k prevalence"), split into separate POINT_PREVALENCE (241) and ANNUAL_INCIDENCE (23.2) records. `PENETRANCE_RE` was extended with `cumulative incidence/risk` and `diagnosed by age` (verified against the KB to add no false positives on legitimate rate-bearing records). **Third correction batch (PR review):** a further scan found cohort-conditional / diagnostic-procedure rates whose qualifier lives only in the **`population` label** (not `percentage`/`notes`), which the guards do not parse: e.g. FICUS_syndrome (PICS-F among ICU family members), Coronary_Vasospasm (spasm among ANOCA patients), Refeeding_Syndrome (event rate in hospitalized/PN patients), Aortitis (histology among aortic-surgery patients), Brucellosis (pooled prevalence among included study populations), Silent_Sinus_Syndrome (radiologic finding among head-CT patients), Laryngotracheoesophageal_Cleft (proportion among endoscopy referrals) — structured slots stripped. Plus three `measure_type` corrections to BIRTH_PREVALENCE (Klinefelter_Syndrome, Wolf-Hirschhorn_Syndrome, MECP2_Duplication_Syndrome) where the birth-prevalence language was in the snippet only. Population-label conditionality is deliberately **not** auto-guarded: the label alone cannot separate a selected referral cohort ("adults undergoing head CT") from a legitimate large-scale screening population that approximates the general rate ("Pregnant women undergoing genome-wide NIPS", 333,187 women → 6.9/100,000), so this class stays manual-review. | migration follow-up + schema follow-up (destination for survival/staging/subtype-share) |
| Per-gene `case_fractions` backfill | New structured `Genetic.case_fractions` slot added (§8). `Bardet-Biedl_Syndrome` backfilled for five genes (BBS1, BBS10, ARL6/BBS3, MKKS/BBS6, BBS9) across European, metabolic, and Indian cohorts. **Method/caveat:** dominant-gene fractions (BBS1, BBS10) appear in citable abstracts; minor-gene fractions are recoverable only from **open-access full-text** cohort papers/reviews whose cache is `full_text_xml` (the Indian-cohort figures came from PMID:27853007), since abstracts and the GeneReviews table (NBK1363 T3) and the Niederlová meta-analysis abstract (PMID:31283077) do not carry them. Backfilling the remaining minor genes is gated on finding such full-text-cacheable sources — figures must **not** be filled from memory (anti-hallucination policy, §6). Whether to deprecate the overloaded `frequency` field is also outstanding; no automated extractor yet. | schema follow-up |
| KGX export of `differential_diagnoses` / `diagnosis` | Not yet exported; candidate predicate `biolink:disease_has_differential_diagnosis` | [#2100](https://github.com/monarch-initiative/dismech/issues/2100) |
| RadLex-grade imaging-finding granularity | `ImagingFinding` (§9) grounds findings in NCIT + HP, which is patchy for specific radiologic appearances (e.g. contrast enhancement, T2 hyperintensity resolve to procedures or CTCAE grades). Tightening `ImagingFindingTerm` to a RadLex `reachable_from` (and `finding_term` to REQUIRED) is deferred: RadLex is not on EBI OLS4, so it needs a `bioportal:` adapter + API key in `conf/oak_config.yaml`. | schema/ontology follow-up |
| Non-imaging detection modalities | **Resolved for electrophysiology (§10)** via phenotype post-composition (an `electrophysiology:` sidecar carrying modality + `ictal_state` + `recording_state`), *not* a finding class — because EEG/EMG/EKG terms are already HP phenotypes. `Dravet_syndrome` is the worked example. **Still open:** functional/provocation tests (e.g. tensilon, tilt-table) remain free-text `diagnosis`. | schema follow-up |
| Investigation-readout phenotype backfill (`reports_on`) | New lean `PhenotypeReadout` slot added (§10): investigation-result phenotypes (abnormal ERG/EEG, `Elevated circulating … concentration`) attach to the mechanism they measure via a dashed observational readout edge instead of floating as orphan nodes or being mis-wired as causal `downstream` edges. `Bardet-Biedl_Syndrome` (Abnormal electroretinogram → Photoreceptor outer-segment transport defect) is the worked exemplar. **First batch done** (`scripts/migrate_readout_phenotypes.py`): 69 mis-wired causal edges across 60 files migrated to `reports_on` — restricted to **pure lab/investigation readouts that are never themselves disease drivers** (tissue-leakage enzymes: transaminases/CK/LDH/aldolase/ALP; acute-phase reactants; tumor markers AFP/β-hCG; newborn-screening acylcarnitines; the electroretinogram), HP-verified via descendants of `HP:0032180`/`HP:0034684`/`HP:0010876`/`HP:0003111`/`HP:0030453`. **Deliberately NOT flipped:** ~179 causally-active analytes where the `downstream` edge is *correct* — ammonia (→ encephalopathy), lactate (→ acidosis), vitamins (deficiency → neuropathy/retinopathy), cholesterol, hormones, ions, immunoglobulins — plus any readout carrying its own `sequelae`. **Second batch done** (floating pure readouts): 55 `reports_on` links added across 47 files by a parallel curation pass, each choosing the best-fit existing mechanism node (liver enzymes → hepatocyte-injury node, CK/aldolase/LDH → myofiber-necrosis node, ERG/EOG → photoreceptor-degeneration node, CRP/acute-phase → inflammation node, AFP/β-hCG/tryptase → tumor/mast-cell node, bone ALP → osteoblast node). **~14 deliberately left unlinked** where the disease pathograph has no node the organ-injury lab measures (e.g. transaminases in Graves/Celiac/Stevens-Johnson, the Murine-typhus organ-injury labs) — these are genuine *modeling gaps* (the entry doesn't yet represent that organ's involvement), not readout-link gaps, and were skipped rather than invent a node. **Open:** the ~58 non-pure floating readouts (causally-active analytes) and the modeling-gap skips; causally-active analytes could also optionally gain a *second* `reports_on` link alongside their (correct) causal edge where the value is used diagnostically. | KB migration (batches 1–2 done) |
| Wire the existing `PhenotypeCategoryEnum` to `phenotypes.category` | The renderer already **derives** each phenotype's organ-system category from its HPO ancestry (`HpoCategoryProvider` → the 22 top-levels, codified as `PhenotypeCategoryEnum` in `schema/classifications/phenotype_category.yaml`), so the hand-entered `category` (still `range: string`, ~200 inconsistent values, ~4k blank) is not what drives display. The cleanup is to bind that enum to the slot and/or deprecate the free-text field in favour of the derived value — not to invent new category values. (Note: category-gated *rules* are a non-goal — the category is derived from the term, so such a rule would be circular; see §10.) | schema follow-up / KB migration |
| Histopathology (NCIT) vs phenotype (HP) boundary | **Undecided — maintainer call outstanding.** `HistopathologyFindingTerm` binds the NCIT Histopathology Result branch (`NCIT:C83490`) plus a narrow `HP:0025461` (Abnormal cell morphology) carve-out; HP covers many organ-specific microscopic findings (foot-process effacement, ragged-red fibers) that fall outside both. Four questions are open: (1) should `finding_term` bind HP beyond `HP:0025461`, and what is the NCIT-vs-HP selection rule; (2) HP+NCIT dual-coding, mirroring the HP+MONDO disease-like-phenotype precedent (§4); (3) the authoritative `phenotypes` vs `histopathology` rule for a microscopic observation — §10's test ("if the term already lives in the phenotype ontology it belongs in `phenotypes`") answers the *class-existence* question but not the *slot-choice* one; (4) whether entity-level "findings" (Barrett esophagus, Castleman variants, the DNET glioneuronal element) should move to `disease_term`/subtype — independent of the vocabulary question. **Re-census (2026-08-18)** reframes the options: **325 of 707 findings (46%) across 188 files are unbound** (up from 123/76 at the 2026-07-02 triage), the `HP:0025461` carve-out carries almost no load (14 bound findings vs 368 NCIT), and the unbound tail is **not** a recurring-vocabulary gap — 324 distinct labels for 325 findings, 58% of them post-composed clauses vs 20% of bound ones. So broadening the HP root reaches at most the ~135 single-concept findings. Meanwhile **0 of 707 findings use any of the `located_in`/`modifier`/`laterality`/`spatial_extent`/`severity` slots `HistopathologyFindingDescriptor` already inherits from `Descriptor`** — undocumented on that class, unlike its `ImagingFindingDescriptor` sibling — making "bind the head term, post-compose the rest" a fifth option needing no schema change. | [#5140](https://github.com/monarch-initiative/dismech/issues/5140) · [re-census](../reports/histopathology-binding-recensus-2026-08-18.md) · [2026-07-02 triage](../reports/histopathology_ncit_triage-2026-07-02.md) |
| Obsolete ontology terms | Should fail validation but do not yet | [#712](https://github.com/monarch-initiative/dismech/issues/712) |
| Unlisted ontology prefixes | Silently skipped by term validation (only a warning) — an unconstrained prefix can pass unchecked | — |
| Schema docs vs. script docs separation | Schema element pages currently mix in script docs | [#2737](https://github.com/monarch-initiative/dismech/issues/2737) |
| Abstract (non-disease) comorbidity/trajectory poles | Undecided. `ComorbidityAssociation.disease_a/disease_b` are `ConditionDescriptor`s where `slug` is optional, so a pole need not resolve to a `Disease` entry — e.g. an exposure/state like "accelerated biological aging" expressed via `preferred_term` (optionally MONDO/HP-bound). Schema permits it; whether it is idiomatic (vs. requiring both poles to be bona fide conditions, and modeling the broad mechanism on a module instead) is not yet decided. Convention so far: keep the conserved mechanism on a `kb/modules/` module and reserve trajectory entries for concrete condition pairs, with the module referenced via `conforms_to` from the trajectory's hypothesis nodes. | schema/governance follow-up |
| Structured effect-modifier / life-stage on associations | Deferred. `ComorbidityDirectionEnum` encodes only **temporal precedence** (A_BEFORE_B, BIDIRECTIONAL, …), not the **sign** of an effect, and `AssociationSignal.demographics.age_range` is free text. There is no first-class way to represent a context-dependent **sign reversal** (antagonistic pleiotropy) — e.g. accelerated aging being risk-increasing for early-onset cancer but tumor-suppressive in later life. Today this is recorded only via two stratified `association_signals` (opposite-sign metrics + `age_range` strings) plus prose `hypotheses`, which is legible to humans but not to tooling. Candidate enhancement: an enum-backed `life_stage`/`context` and/or an `effect_direction` (RISK_INCREASING / PROTECTIVE) distinct from temporal `directionality`. **Precedent for the modeling alternative:** for the senescence case the antagonistic pleiotropy was modeled instead as **two complementary precomposed modules** — `cellular_senescence` (deleterious arm) and `senescence_tumor_suppression` (protective arm) — rather than a single effect-reversing edge. This sidesteps the missing construct and is the preferred pattern when the opposing effects are mechanistically separable; the structured effect-modifier remains a candidate only for genuinely single-edge sign reversals. | schema follow-up |
