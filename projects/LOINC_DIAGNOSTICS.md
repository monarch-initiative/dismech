---
title: LOINC Diagnostics
status: PLANNED
tags:
- loinc
- diagnosis
- biomarkers
- ehr
description: Bind LOINC codes to the diagnostic tests, biomarkers, instruments and staging scores that disease entries already describe in prose, validated against the Monarch KG, so a disease can say which measurement diagnoses, monitors or stages it and an EHR query can find it.
diseases:
- Tay-Sachs_Disease
- CKD-Mineral_Bone_Disorder
- Phenylketonuria
---

# LOINC Diagnostics

## Scope

A LOINC code earns a place on a disease entry when its component names **the
disease, its agent, its gene, or a decision threshold the disease owns**: an
HIV antibody assay, hexosaminidase A activity, a CFTR sequencing panel, the
PHQ-9 total score with its severity cut-offs. That relation is disease-specific,
citable, and has no home in HPO. It is the content this project curates.

What it does **not** curate is the disease-independent map from a test result
to a phenotype class ("potassium high → Hyperkalemia", the loinc2hpo relation).
That is a property of the test, not of any disease; it does not fit the
evidence policy (there is no paper to quote for a definition), and its
consumers are EHR pipelines and the Monarch KG rather than dismech. dismech's
only role there is a gap report feeding whoever maintains that mapping. The
decision is recorded as §17 of `docs/explanation/design-decisions.md`, which
lands with the Phase 1 schema PR (#13636); §12 keeps a row for the LOINC homes
that remain unbound after it.

### Where the content lands

| Relation | Slot | State at scoping (`main`, 2026-10-06) |
|---|---|---|
| diagnostic test for | `diagnosis[].measurements` (new) beside the NCIT `diagnosis_term` — the "thing" beside the "action", as `therapeutic_agent` is to `treatment_term` | 2,413 entries carry `diagnosis:` (6,110 rows); the observables sit in free-text `markers` (129 uses, 57 packing several analytes — #10046) |
| biomarker measured in | `biochemical[].loinc_term` (new; `loinc_term` existed only on `ReferenceRange`) | 54 `loinc_term` blocks in 20 files, all inside a `reference_ranges` interval; **21 more LOINC CURIEs in `biochemical[].mappings_list` (3 files) and 2 in `biochemical[].biomarker_term` (1 file, a slot documented as NCIT-only)** |
| threshold / severity bands | `diagnosis[].reference_ranges` (new) and `biochemical[].reference_ranges` | bands exist only on biochemical markers |
| staged / scored by | instrument codes on the relevant `diagnosis` row, with bands | no code slot |

Counts in this file are dated and come from a parse of `kb/` with
`dismech.kb_cache` (a `term`/`loinc_term` dict whose `id` starts with
`LOINC:`, classified by its parent slot); `grep -rn -B1 'id: LOINC:' kb`
reproduces the LOINC ones. They drift with every merge; read them as the
scoping snapshot, not as live state.

**One marker-level LOINC home, not two.** `Biochemical.loinc_term` is the
identity of the measurement that quantifies a marker. `mappings_list` is the
`ModelVariableDescriptor` crosswalk — a multi-ontology slot (LOINC, CHEBI, HP)
for tying a *computational-model variable* to external identifiers — and it
has been carrying LOINC as marker identity only because nothing else could.
After Phase 1, a marker's LOINC identity lives in `loinc_term`; a
`mappings_list` LOINC entry stays only where the marker genuinely is a model
variable's mapping (the CKD-MBD extension-model species are the case). The two
`biomarker_term` codes move to `loinc_term`; `biomarker_term` is NCIT.

Identity is bound at the **LOINC Part or panel level** (`LOINC:LP…`, or the
panel/total-score code for an instrument). Method- and specimen-specific codes
belong only inside a `definitions[]` phenotype algorithm that needs them. LOINC
has dozens of codes for one assay; binding method codes for identity would put
the same test on different codes in different entries.

## Validation

LOINC codes were unvalidated at project start in two independent ways: no
adapter in `conf/oak_config.yaml`, and `loinc_term` typed as a bare `Term`
with no `bindings:`, so the term validator never looked at it. Both are fixed
in Phase 0–1 below. The source is the Monarch KG, which carries the full LOINC
table (107,791 `biolink:ClinicalMeasurement` nodes, with LOINC's own Part
hierarchy as `subclass_of`), served through OAK's `monarch:` adapter once
[INCATools/ontology-access-kit#920](https://github.com/INCATools/ontology-access-kit/pull/920)
is released. The canonical label is the LOINC Long Common Name, which is what
the KG serves as `name` and what existing bindings already use.

The API serves the last KG release, so a code loaded into the KG is not
validatable until the next release. A miss on a real code is lag, not absence.

**Why `LoincTerm` has no `reachable_from`, measured.** The KG has a LOINC
root, `LOINC:lc0000001`, but at 2026-10-06 only 13,627 of 107,791 LOINC nodes
carry any `subclass_of` edge; 94,164 — including whole instrument families
such as the PROMIS items — have none, and 10,547 of the connected ones hang
directly off the root. A `reachable_from` closure would reject 87% of real
codes. The vocabulary is pinned instead by `LoincCode`, a `Term` subclass whose
`id` must match `^LOINC:(LP|LG)?[0-9]+-[0-9]$` (enforced by `linkml-validate`),
with existence and label from the adapter. If a later KG release connects
every code to the root, switching the enum to `reachable_from` is a one-line
change with no data migration — but OAK's `monarch:` adapter would first need
to map `biolink:subclass_of` to `rdfs:subClassOf` in `relationships()`, since
today its ancestor walk matches nothing and wanders every `related_to` edge.

## Phases

### Phase 0 — unblock validation

- [ ] oaklib: `monarch:` adapter reads labels from `name` (INCATools/ontology-access-kit#920); release
- [ ] dismech: bump the oaklib pin; add `LOINC: "monarch:"` (quoted — a bare `monarch:` is a YAML scanner error) to `conf/oak_config.yaml` with a note on release lag; delete `scripts/seed_loinc_cache.sh` and the `loinc-seed-cache` recipe

Curation does not wait on this phase. Cache-first validation works for a
prefix that is not yet routed, so a curation PR that commits its own rows in
`cache/loinc/terms.csv` is green on `main` today. `just loinc-seed-cache
<files>` (#13636) produces those rows by overlaying the #920 adapter in an
ephemeral environment and writing what the validator returns; nothing types a
label. Tranches that need only existing slots (`reference_ranges.loinc_term`
with bands — A, C, D, I, M and the biochemical half of G) can start on `main`
now; tranches that need `Diagnosis.measurements` (B, E, F, P, Q) are drafted on
branches based on the schema branch and opened against `main` once #13636
merges — additive schema, so the rebase is a no-op.

### Phase 1 — schema (one PR, via `extend-schema`)

- [ ] `LoincTerm` enum (label-match only, the `GeneTerm` pattern) and a `MeasurementDescriptor` whose `term` binds to it
- [ ] retype `loinc_term` from `Term` to `MeasurementDescriptor`; migrate the 68 existing bindings
- [ ] `Diagnosis.measurements` (multivalued) and `Diagnosis.reference_ranges`
- [ ] `Biochemical.loinc_term`, leaving the range-level slot for the interval itself
- [ ] `LoincCode`: a `Term` subclass whose `id` must match `^LOINC:(LP|LG)?[0-9]+-[0-9]$`, so a real NCIT term cannot pass in a LOINC slot (the binding resolves a CURIE through the adapter for its *own* prefix)
- [ ] decision-register §17: loinc2mondo in dismech; loinc2hpo out of scope; Part-level identity convention; §12 row for the unbound homes
- [ ] first validated sweep over the files carrying LOINC codes, fix what it finds, seed `cache/loinc/terms.csv` (done in #13636: 21 files, 43 codes, 2 labels wrong in bound slots, 2 more in `mappings_list`)
- [ ] **follow-up after #13636 merges:** migrate the 21 `mappings_list` LOINC entries — add `loinc_term` on each marker; keep the `mappings_list` row only where the marker is a model-variable mapping — and move the 2 `biomarker_term` LOINC codes in `Isolated_Thyroid-stimulating_Hormone_Deficiency` to `loinc_term`. Until then those 23 codes are unchecked by every gate; two of the `mappings_list` labels were already found wrong by hand and fixed in #13636.

### Phase 2 — tooling (report-only, never autofill)

- [ ] `just list-diagnosis-markers`: free-text `Diagnosis.markers` strings → candidate LOINC Parts via Monarch search, as a worklist. Search recall is incomplete — at scoping, `Hexosaminidase`, `QTc` and `HLA-B*57:01` returned nothing although LOINC has codes for at least the first — so an empty candidate list means "search found nothing", never "LOINC has nothing"; the exact-lookup routes are the `/entity/LOINC:<code>` endpoint and the KG duckdb
- [ ] `just list-lab-phenotype-gaps`: lab-type HP phenotypes with no loinc2hpo edge in the KG, and `biochemical` LOINC codes with no mapped HP — the nomination stream for the external mapping
- [ ] `kgx_export`: emit LOINC → MONDO edges (`biolink:diagnoses`, `biolink:biomarker_for`) with `infores:dismech`
- [ ] `references_cache/LOINC_<code>.md` structured source from the API's `infores:loinc2hpo` associations, so a band's `phenotype_term` can cite a quotable row

### Phase 3 — content tranches

Each tranche is bounded by an external list, which is what makes it finishable.
Representative codes were confirmed in the KG when the project was scoped.

| | Tranche | Lands on | Bounded by | Example codes |
|---|---|---|---|---|
| A | Newborn screening — DBS analytes with cut-offs | `diagnosis` + bands | RUSP core and secondary conditions | `LOINC:29571-7` phenylalanine DBS, `LOINC:32854-2` 17-OHP DBS, `LOINC:51935-5` IRT DBS |
| B | Pathogen-specific assays — serology, NAAT, IGRA | `diagnosis` on infectious entries | CDC notifiable list / CSTE RCTC | `LOINC:11006-4` Borrelia Ab, `LOINC:46217-6` TB IGRA |
| C | Autoantibodies | `diagnosis` + `biochemical` | existing autoimmune entries | `LOINC:53028-7` anti-CCP, `LOINC:43638-6` AQP4 IgG, `LOINC:30192-9` AChR Ab |
| D | Enzyme activity and metabolite assays | `diagnosis` + `biochemical` | lysosomal-storage and IEM groupings | `LOINC:LP15604-9` glucosylceramidase |
| E | Gene-level molecular tests | `diagnosis` on Mendelian entries | every causative gene in `genetic:` | `LOINC:90256-9` CFTR full sequencing, `LOINC:53783-7` HTT panel |
| F | Tumour markers and somatic biomarker tests | cancer entries; makes the §3a "distinct diagnostic pathway" rule checkable | cancer entries with biomarker strata | `LOINC:55149-9` BCR-ABL1, `LOINC:105302-4` PD-L1 IHC |
| G | Functional tests with diagnostic thresholds | organ entries and disease-like-phenotype modules | GOLD, CF Foundation, WHO DXA and hearing grades | `LOINC:19926-5` FEV1/FVC, `LOINC:2077-6` sweat chloride, `LOINC:101804-3` DXA T-score, `LOINC:91372-3` hearing threshold |
| H | Pharmacogenomic tests | treatment-toxicity entries and modules | CPIC guideline list | `LOINC:104669-7` CYP2D6 activity score |
| I | Toxicology with reference thresholds | existing poisoning entries | current `*_Poisoning` entries | `LOINC:17052-2` blood lead |
| J | CSF and fluid biomarkers | neurological entries; criteria in `definitions[]` | McDonald, NIA-AA and similar criteria documents | `LOINC:31989-7` 14-3-3 CSF, `LOINC:LP18182-3` oligoclonal bands |
| K | Prenatal and fetal screening | chromosomal disorders | screening-programme panels | `LOINC:77011-5` cfDNA trisomy 21 |
| L | Allergen-specific IgE | allergy entries | existing allergy entries | `LOINC:61219-2` peanut IgE |
| M | Acute-care biomarkers with cut-offs | MI, sepsis, heart failure, VTE entries | the universal-definition documents | troponin T, procalcitonin |
| N | `kb/surrogate_endpoints` rows → LOINC. **The code lands once, on the dismech `Biochemical` marker** (`loinc_term`) whose `readouts[].regulatory_endpoint_refs` already points at the FDA row; the FDA row itself is a transcription and gets no code, so nothing is recorded twice. An FDA row with no dismech marker gets nothing from this tranche | the FDA surrogate endpoint table | already a bounded table in `kb/` | HbA1c, LDL, viral load, FEV1 |
| O | Lab criteria in existing `definitions[]` algorithms | the 304 entries carrying `definitions:` | the existing algorithms | — |
| P | Cognitive and psychiatric instruments with severity bands. Bind the **panel** code as the test's identity in `measurements` and the **total-score** code in `reference_ranges`, where the cut-off lives (MoCA `72133-2` / `72172-0`; MMSE `72107-6` / `72106-8`; GDS `48542-5` / `48544-1`) | `diagnosis` + bands on dementia, depression, anxiety, bipolar entries | published validation studies for each instrument | `LOINC:72133-2` MoCA, `LOINC:72107-6` MMSE, `LOINC:72088-8` CDR, `LOINC:44249-1` PHQ-9, `LOINC:48542-5` GDS, `LOINC:89210-9` BDI-II, `LOINC:69737-5` GAD-7, `LOINC:93245-9` C-SSRS, `LOINC:71354-5` EPDS, `LOINC:85102-2` MDQ |
| Q | Staging and severity scores (same panel / total-score split as P) | `diagnosis` + bands | the score definitions | `LOINC:44760-7` MELD, `LOINC:98152-2` Child-Pugh total, `LOINC:70182-1` NIHSS, `LOINC:77717-7` UPDRS panel, `LOINC:35088-4` Glasgow coma scale |

**P and Q meet an undecided register row.** The §12 row *Computed indices and
composite endpoints* records that dismech has no representation for a value
computed over other measurements, and MELD, Child-Pugh, NIHSS, a PHQ-9 total
and a MoCA total are exactly that. For this project, **code plus bands is
enough**: the LOINC total-score code gives the composite an identity without
minting a term, and the bands carry the disease-owned thresholds. The scoring
logic — which items, what weights — still has no home, and this project does
not try to give it one; §17 says the same. If a tranche finds it needs the
logic, that is the moment to reopen the §12 row, not to improvise a slot.

Suggested order: **A** first (small, authoritative, LOINC-native in the DBS
system, nearly every condition already curated), then **G**, **B** and **P**,
with **E** as a background worklist and **N**/**O** as the mechanical passes
once the slot exists.

**Tranche J notes.**

- **A tranche J candidate pool must scan `definitions:`, not just `diagnosis:`
  and `biochemical:`.** The tranche's own scope above names "criteria in
  `definitions[]`" for exactly this reason (McDonald, NIA-AA and similar
  documents live there). A noticeable share of this tranche's candidates —
  on the order of a third, counted while building its pool rather than
  measured against the corpus — were reachable only through that section.
- **Open question, not settled: bind a method-specific LOINC code when no
  Part-level identity exists, or decline the binding.** This is an exception
  to the Part-or-panel identity rule stated above under *Where the content
  lands*, taken where no Part code exists. Neurofilament light chain is the
  worked pair, and both sides are in the KB:
  `Early-Onset_Autosomal_Dominant_Alzheimer_Disease` binds `LOINC:100996-8`
  *Neurofilament light chain [Mass/volume] in Cerebrospinal Fluid*, while
  `Hunter_syndrome` declines a binding and records why in `notes` — its
  marker spans CSF and serum, and LOINC codes the analyte per specimen
  (`LOINC:100996-8` in CSF, `LOINC:101281-4` *... in Serum or Plasma by
  Immunoassay* in serum), with no analyte Part found in the Monarch KG.
  Both readings rest on the same facts, so this is a convention choice to
  make once, not a fact to re-derive per entry.
- **An absence claim about a LOINC code needs a date or release, not just a
  search.** A code can exist in the current release that an earlier,
  correctly-performed search found absent, and the release table records
  which: of the seven neurofilament codes in LOINC 2.83, `LOINC:112614-3`
  *Neurofilament light chain [Moles/volume] in Plasma by Immunoassay* was
  first released in 2.83 itself, so a search against any earlier release
  would rightly have reported it missing. That is release drift, not a faulty
  search. State the LOINC release (or a retrieval date) alongside any "no code
  exists" finding.
- **The same analyte can carry different units across specimens, and the
  gap is usually a different analyte rather than a missing unit.** Intact
  human chorionic gonadotropin has a Mass/volume code in serum,
  `LOINC:34670-0` *Choriogonadotropin [Mass/volume] in Serum or Plasma*, but
  in cerebrospinal fluid only a Units/volume one, `LOINC:44001-6`
  *Choriogonadotropin [Units/volume] in Cerebrospinal Fluid*. LOINC 2.83 does
  carry a Mass/volume CSF code, `LOINC:55866-8`, but for the *free beta
  subunit* — a different analyte, not the same measurement in another unit.
  Note also that serum has both units available for intact HCG
  (`LOINC:19080-1` is the Units/volume serum code), so the unit is a property
  of the individual code and not of the specimen. A specimen pair is
  therefore not necessarily a unit pair, and binding the specimen-identity
  match is correct even when the units differ.

Instruments LOINC does not carry — searches for HAM-D, HAM-A, ADOS, PANSS,
Y-BOCS, EDSS, Hoehn and Yahr, Epworth, ADAS-Cog, QIDS and YMRS returned
nothing in the KG at scoping; LOINC includes a copyrighted scale only with
the owner's permission — get an NCIT instrument term in `diagnosis_term` and
no LOINC slot, with the search recorded in `notes`. A search miss in the KG is
not proof of absence from LOINC; confirm against loinc.org before writing
that. `Hexosaminidase`, `QTc` and `HLA-B*57:01` also returned nothing and
look like search-index misses rather than gaps; resolve them by direct entity
lookup before any tranche depends on them.

### Tranche B closing ledger

Tranche B (pathogen-specific assays on infectious-disease entries) is complete.
Of the 211 entries in `kb/disorders/` carrying an `infectious_agent` or
`transmission` block, 119 held no LOINC code and 81 of those carried a
`diagnosis`, `biochemical` or `definitions` section. The remaining free pool is
45 populated entries, and every one has now been assessed: 19 are neoplasms and
belong to tranche F, one is a mycotoxicosis the infectious-disease granularity
ladder puts out of scope, seven are polymicrobial or clinical-diagnosis entries
where no single pathogen assay is the standard, and the rest are declines with
recorded reasons. There is no sixth candidate left to batch, which is why the
tranche closes here rather than at a round number.

**Three sources, answering three different questions.** This was learned the
hard way, by adopting a two-way split and finding it insufficient twice in one
day:

| Question | Source |
|---|---|
| does a code **not** exist | the pinned complete export (`data/loinc/MANIFEST.yaml`, Tuva LOINC 2.83, sha256-verified, 112,405 rows) — no ranking, no cap, version stamped |
| does a code exist **and is it usable** | the live Monarch KG, because the term validator resolves against it |
| is there a **Part** (`LP`/`LG`) code | the KG only — the export contains zero Part rows |

Presence in the export is **necessary but not sufficient**. `LOINC:106041-7`
(*Fungus identified in Ear fluid by Culture*) and `LOINC:107527-4` (*Clue cells
in Vaginal fluid*) are both ACTIVE and non-deprecated in 2.83 and both resolve
in the KG with no name, so neither can be labelled or cached and neither is
bindable today. That is release lag, not a fabricated code: record it and bind
the usable alternative rather than treating the code as absent.

**Enumerate a criteria set by specimen, not by item name.** A four-item bedside
criteria set needs four separate lucky guesses if searched per item, and the
specimen is the one thing the items share. Searching the Amsel criteria by name
returned nothing for vaginal pH or the whiff test, and a draft recorded both as
absent; enumerating all 182 ACTIVE vaginal-system codes found both at once,
each method-less, and the Amsel row went from one measurement to three. The
same move settled Otomycosis (80 ear-specimen codes, exactly one fungal, no KOH
code) and Endophthalmitis (121 vitreous-system codes, none for culture or Gram
stain).

**A row naming several methods wants the method-less code.** Nocardiosis was
declined in an early batch because its molecular row names 16S sequencing,
MLSA, MALDI-TOF, whole-genome and metagenomic sequencing while the only
Nocardia molecular code is a nucleic acid amplification assay — so no code
matched the *method*. That reasoning missed `LOINC:55096-2` *Nocardia sp
identified in Isolate*, which is method-less and is correct **because** the row
names five techniques: binding any one would narrow the row to a single
technique. The decline was reversed in a later batch. Prefer the method-less
code first, as the identity convention above already says, rather than hunting
for whichever method happens to be coded.

The converse holds where the method *is* the instrument's identity. Bacterial
Vaginosis binds the Nugent-qualified score code rather than the generic
bacterial-vaginosis score code, because a score of 7 means nothing without
saying it is Nugent's, while the same entry's Amsel row binds method-less codes
for pH and the whiff test because neither criterion turns on technique. Both
notes say so explicitly, so the opposite choices do not read as inconsistency.

**A site-qualified code can smuggle in a claim the entry does not make.**
Staphylococcal Scalded Skin Syndrome turns on periorificial swabs outperforming
blister fluid, so the site *is* the claim — and LOINC's only plain *S. aureus*
culture code carries no site, while **every** site-qualified *S. aureus* culture
code in 2.83 is methicillin-resistant *S. aureus*, asserting a resistance
phenotype the entry never claims. No code can express that row, so its culture
arm is deliberately unbound. Check what a specimen qualifier brings with it
before preferring it for being more specific.

**`definitions:` has no `measurements` slot.** Six entries in this pool carry
their diagnostic content only there. Where the test is genuinely described and
citable, the remedy is a minimal `diagnosis:` row that reuses an evidence
snippet already verified in the same file, adding no new citation and leaving
the criteria in `definitions:` — Bacterial Vaginosis (two rows) and Otomycosis
(one) are the worked examples. Run `check-title-snippets` and
`check-snippet-grading` when doing this: `evidence_source` cannot change because
a quote moved. Where the entry itself says no laboratory test applies
(Seborrheic Dermatitis, STARI), there is nothing to add.

**Two pool-construction defects worth inheriting.** A section header can be
present and empty — `Polycystic_Echinococcosis` carries `biochemical: []`, which
a header-matching scan counts as populated. And an in-flight set built with
`gh pr list --limit N` truncates silently in a repository with more open PRs
than `N`; enumerate with `gh api --paginate` instead, which is what kept these
batches off three live collisions.

### External loinc→condition artifacts

Several bodies maintain the mapping for their slice. These are candidate
`structured_sources` in the Orphanet/ClinGen mould, to import rather than
re-curate, licensing permitting:

- **CSTE/CDC RCTC** (Reportable Condition Trigger Codes): LOINC lab trigger
  codes → reportable conditions, for electronic case reporting. Covers tranche
  B and cross-checks hand curation there.
- **CPIC** gene–drug pairs: the list for tranche H.
- **RUSP / ACMG ACT sheets**: the list and analytes for tranche A.
- **NLM VSAC value sets**: LOINC lab value sets per condition for eCQMs. UMLS
  licence; check before caching anything.
- **LOINC Groups**: LOINC's own Part-level bundles, the identity level for
  `Diagnosis.measurements`.

### Tranche G closing ledger (batches 25–28)

**Census.** 23 entries, 43 bindings, 34 new `cache/loinc/terms.csv` rows: batch 25
(6 entries / 24 bindings / 18 rows), 26 (6 / 10 / 9), 27 (6 / 6 / 4), 28
(5 / 3 / 3). The yield per entry falls by a factor of eight across the four
batches, which is what exhaustion looks like here — not a shortage of entries
naming a functional test, but a shortage of tests LOINC codes at all. Batch 28
assessed 52 candidates and found five worth touching, three of them bindings.
Earlier batches (1–24) worked the audiometry, spirometry, sweat-chloride, QTc,
DXA and IOP series; 25–28 worked the provocative and dynamic tests, which is
where the coded coverage runs out.

**Two traps that pass every gate.** Both are a right-sounding analyte attached to
the wrong quantity, and neither is visible to schema validation, term validation
or any offline check:

- **A clearance ratio is not a concentration ratio.**
  `Familial_Hypocalciuric_Hypercalcemia_1`'s discriminating test is the
  calcium/creatinine *clearance* ratio, dimensionless and computed from four
  results. Every `Calcium/Creatinine` code in LOINC is a *concentration* ratio
  within a urine specimen, in mg/g or mmol/mol creatinine. No clearance-ratio
  code exists for any analyte pair, in either source.
- **A complement is not the quantity.** Tubular reabsorption of phosphate is the
  *reabsorbed* fraction; LOINC codes the *excreted* fraction. The arithmetic
  relation (TRP = 100 − FEP) is exactly what makes the substitution tempting:
  `Hyperphosphatemic_Familial_Tumoral_Calcinosis` records a patient at 96%, which
  on the available scale reads 4. `X-Linked_Hypophosphatemia` is the same gap with
  the direction reversed. TmP/GFR has no code at all.

The same shape recurs at specimen level — urine trehalase against a mucosal
biopsy assay, exhaled nitric oxide against nasal nitric oxide — and the general
rule it suggests is that when a candidate code's *property* or *system* differs
from the test's, an arithmetic or anatomical near-relation is a reason to decline,
not a reason to approximate.

**The band convention is two-sided, and the two halves fail differently.**
The convention itself is recorded on the schema's `ReferenceRangeBand` — its
`comments` state the half-open `[lower_bound, upper_bound)` partition, and the
`slot_usage` descriptions mark `lower_bound` inclusive and `upper_bound`
exclusive — and restated in CLAUDE.md under *Reference Ranges and
Interpretation Bands*. What follows from it is that no exclusive lower bound is
available, so a source's `> x` cannot be stated, and no inclusive upper bound
is available either, so a source's `≤ x` cannot be stated. Worked cases across the tranche: `Renal_Hypomagnesemia_4` FEMg
"above 2%", `Cushing_Disease` nadir cortisol "at or below 3 mcg/dL". A `< x`
criterion *is* expressed exactly, so the response to an unrepresentable threshold
is to decline the band and record the inequality, never to move the boundary.
The gap itself is recorded as an open decision (*`ReferenceRangeBand` bounds
cannot state a strict `>` or a non-strict `≤` threshold* in
`docs/explanation/design-decisions.md`), which carries these same cases; keep
the two in step rather than restating one from the other.
Distinguish that from having no code to attach a representable threshold to:
`Primary_Ciliary_Dyskinesia` already carries correct 77 nL/min bands with no
`loinc_term`, because LOINC has no nasal nitric oxide measurement — the clearest
case in this project for a LOINC term request.

**Which slot takes a Part and which takes an observation code.** Design
decisions §17 records only the first half, as its *Identity convention*:
`diagnosis[].measurements` is test identity and prefers a Part or panel, with
method- and specimen-specific codes reserved for a `definitions[]` phenotype
algorithm. The complement is **not settled, and this paragraph does not settle
it**: whether a bare Part may fill `biochemical[].loinc_term` is an open
decision in the register (*Whether a bare LOINC Part may fill
`biochemical[].loinc_term`* in `docs/explanation/design-decisions.md`), where
64 merged bindings across 38 entries already use a Part there, several of them
deliberately. These batches read the slot as the measurement that quantifies a
marker, and so preferred an observation code, a Part being a component with no
scale, specimen or method; `Trehalase_Deficiency` is the worked pair under that
reading — the Part binds in `measurements`, nothing binds in the marker's
`loinc_term`. That is the reading this tranche followed, not a convention to
apply elsewhere: the register's row owns the question, and nothing here is a
reason to decline a Part binding or to migrate an existing one. One limit found
in batch 28, independent of that question: a Part is only worth binding when it
carries most of the available specificity. `LOINC:LP15910-0` *Trehalase* sat above
two records and was bound; `LOINC:LP173640-6` *Nitric oxide* sits above twelve
spanning nasal screening, an asthma marker and ventilator therapy, and was
declined.

**Paginate every KG query to its stated `total` before claiming a Part absence.**
The default page of 100 silently truncates exactly where Part claims are decided:
`Testosterone` returns 104 and `Somatotropin` 371. Two claims in batch 26 were
written off truncated pages and corrected before commit. And the two sources
answer different questions — the LOINC release table carries no `LP`/`LG` rows at
all, so "is there a Part" and "which observation codes exist" are separate
searches that a finding should name separately.

**Two defects in this tranche's own pool construction**, recorded because they are
reproducible mistakes rather than bad luck. First, the keyword set shrank between
batches: batch 27 dropped the lung and nitric-oxide terms that batch 26 carried,
which hid a seven-entry nasal-nitric-oxide cluster until batch 28 restored them —
a pool built by narrowing an earlier pool inherits whatever that narrowing
dropped. Second, deriving the in-flight set with `gh pr list --limit 100`
undercounts in a repository with more open PRs than that: the paginated API gave
226 in-flight entries where the capped call gave 134, so entries already being
curated elsewhere looked free.

**Deliberately not padded.** Batch 28 stopped at five entries. What remains in the
pool is repeats of findings already recorded once — five further PCD entries whose
nasal-NO absence is the same fact, `Familial_Hypocalciuric_Hypercalcemia_2` for the
clearance ratio, a fourth forearm-exercise myopathy — plus entries whose test LOINC
does not code (urinary acidification after an acid load: no challenge-qualified
urine pH code; esophageal pH monitoring: a study code but no quantitative pH) and
entries whose rows belong to another tranche's lane (erythrocyte enzyme activity to
D, urea breath tests on neoplasm entries to B and F).

## Out of scope

- The loinc2hpo mapping itself (test result → phenotype class). The existing
  annotation set is stale, its re-curation is a standalone SSSOM effort, and
  dismech contributes only the gap report in Phase 2.
- Therapeutic drug monitoring codes, which describe a treatment rather than a
  disease.
- Population reference intervals as content. Where one is needed to anchor a
  disease-owned band it may be carried, but the interval is not what the
  project adds.
