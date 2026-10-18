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

Instruments LOINC does not carry — searches for HAM-D, HAM-A, ADOS, PANSS,
Y-BOCS, EDSS, Hoehn and Yahr, Epworth, ADAS-Cog, QIDS and YMRS returned
nothing in the KG at scoping; LOINC includes a copyrighted scale only with
the owner's permission — get an NCIT instrument term in `diagnosis_term` and
no LOINC slot, with the search recorded in `notes`. A search miss in the KG is
not proof of absence from LOINC; confirm against loinc.org before writing
that. `Hexosaminidase`, `QTc` and `HLA-B*57:01` also returned nothing and
look like search-index misses rather than gaps; resolve them by direct entity
lookup before any tranche depends on them.

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

## Out of scope

- The loinc2hpo mapping itself (test result → phenotype class). The existing
  annotation set is stale, its re-curation is a standalone SSSOM effort, and
  dismech contributes only the gap report in Phase 2.
- Therapeutic drug monitoring codes, which describe a treatment rather than a
  disease.
- Population reference intervals as content. Where one is needed to anchor a
  disease-owned band it may be carried, but the interval is not what the
  project adds.
