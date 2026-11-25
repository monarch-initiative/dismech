---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-14T02:54:50.413141'
end_time: '2026-11-14T03:16:45.482587'
duration_seconds: 1315.07
template_file: /tmp/claude-0/-home-user-dismech/af87b187-0587-5061-bf8f-ece7a29644b1/scratchpad/issue_17533_prompt.md
template_sha: "e20521c4acc2fb4cf7bf34c9d415e293a2cf4229"
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    save_artifacts: true
    artifact_max_bytes: 5242880
    artifact_keep_runtime: false
    artifact_extra_extensions: []
    artifact_include_globs: []
    artifact_exclude_globs: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
run_metadata:
  job_id: 01ccbf4c-94c8-48f2-82ad-e92e63dd26dd
citation_count: 3
reference_validation:
  total_references: 5
  verified: 4
  not_found: 0
  unverifiable: 1
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 3
  validator_version: 0.5.1
term_validation:
  total_terms: 6
  verified: 6
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PMID_37686457-paper-review-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PMID_37686457-paper-review-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# NAM mining: iPSC protocols for retinal organoids, RGCs and photoreceptors (PMID:37686457)

🤖 *Written by [Claude Code](https://claude.com/claude-code) for Ginnie Hench.*

Second paper of the Complement-ARIE disease-paper round, tracked in the registry's
[review log](https://github.com/monarch-initiative/nams-registry/blob/main/projects/COMPLEMENT_ARIE_DISEASE_PAPERS.md)
([nams-registry#37](https://github.com/monarch-initiative/nams-registry/issues/37)).
Screened in from the abstract, then read in full. Target for an OpenScientist deep-research run.

- **Reference:** PMID:37686457, DOI [10.3390/ijms241713652](https://doi.org/10.3390/ijms241713652), *International Journal of Molecular Sciences* 24(17):13652 (2023). Open access, PMC10487913, so the full text is quotable.
- **Found in:** the Complement-ARIE Landscape Analysis dashboard, "Disease(s) Examined" = retinitis pigmentosa, glaucoma and age-related macular degeneration.

## What kind of paper this is

A **methods review** of protocols for differentiating three retinal cell products
from human iPSCs. It is not a study of any disease: across the full text, retinitis
pigmentosa is named once, glaucoma twice, AMD three times, and "disease modeling"
three times, always as motivation for the protocols. No patient-derived or
disease-genotype line is described.

That is a different shape from
[#17532](https://github.com/monarch-initiative/dismech/issues/17532) and from most
NAM-mining issues, and it should not be read as settling whether the work supports
any mechanism claim — the run decides that from the paper. Two things make it worth
mining either way:

- The three cell products are the cell populations whose loss defines the named
  diseases: photoreceptors in RP and AMD, retinal ganglion cells in glaucoma.
- The review's comparisons against human fetal retina are unusually good material
  for the `fidelity`, `limitations` and `divergences` fields, which are normally the
  hardest part of a model link to source.

## Models in the paper

Three cell products, each reviewed across a set of published protocols summarized in
its own table:

| Cell product | Protocol variants | Table |
|---|---|---|
| iPSC-derived retinal organoids | chemically defined storable organoids; retinoic acid timing; 9-cis retinal for rod maturation; BMP4 yield and composition; several ways of isolating optic vesicle-like structures | Table 1, 7 studies |
| iPSC-derived retinal ganglion cells | chemically defined conditions; biomaterial scaffolds for neurite outgrowth; dual SMAD plus Wnt inhibition; organoid dissociation with magnetic-activated cell sorting; rapid NGN2 overexpression | Table 2, 9 studies |
| iPSC-derived photoreceptors | defined conditions with signaling modulators; without extrinsic modulators; small-molecule inhibitors; bioreactor culture for yield and maturation | Table 3, 9 studies |

## Characterization and validation methods

These are readouts on the three products, not models in their own right:
immunofluorescence marker panels, qPCR, flow cytometry, single-cell RNA sequencing,
transmission electron microscopy of photoreceptor ultrastructure, patch-clamp
recording, multielectrode arrays, and calcium imaging.

## Fidelity content worth extracting

Verify and quote each against the full text:

- scRNA-seq comparison of hPSC-derived retinal organoids and retinospheres against
  human fetal retina: close in cellular composition and gene expression, with
  differences in the developmental trajectories of some cell types, photoreceptors
  among them.
- iPSC-derived RGCs resemble fetal RGCs more closely than organoid-derived RGCs; the
  review reports fetal and directly differentiated RGCs predominantly expressing
  BRN3A where most organoid RGCs express BRN3B.
- TEM comparison of photoreceptor maturation after 9-cis retinal versus all-trans
  retinoic acid.
- Calcium imaging as a maturation stage marker: immature RGCs depolarize to a GABA
  agonist, mature ones do not.

## Candidate dismech anchors

Each needs checking before anything is curated.

- **`Age_Related_Macular_Degeneration.yaml`, `Glaucoma.yaml` and
  `Inherited_Retinal_Dystrophy.yaml` have no `experimental_models:`,
  `animal_models:` or `computational_models:` at all.** Anything curated from this
  paper would be the first model on those entries.
- **`kb/modules/photoreceptor_degeneration.yaml`** has `Photoreceptor Gene Defect`,
  `Photoreceptor Metabolic and Oxidative Stress`, `Rod Photoreceptor Apoptosis`,
  `Secondary Cone Degeneration and Outer Retinal Thinning` and
  `Progressive Visual Field Loss and Blindness`. The photoreceptor and organoid
  products are candidates here.
- **`kb/modules/retinoid_visual_cycle_disruption.yaml` is probably the wrong anchor,
  and is flagged so a run does not land there by name-matching.** The retinoic acid
  and 9-cis retinal in these protocols are differentiation chemistry, not the RPE
  retinoid recycling the module describes. If the run does link them, it needs to say
  why in its own words.

## Existing records this sits beside

dismech already holds iPSC-derived retinal models, and every one is a patient or
genotype-specific instance:

- `Leber_Congenital_Amaurosis_10.yaml`: CEP290 patient iPSC optic cups and RPE, and
  LCA10 patient organoids treated with sepofarsen.
- `OPTN-related_Open_Angle_Glaucoma.yaml`: isogenic OPTN(E50K) hPSC-derived retinal
  ganglion cells.
- `RDH12-Related_Dominant_Retinopathy.yaml`: RDH12 patient iPSC organoids.
- `Stargardt_Disease.yaml`: patient-derived retinal organoid and an STGD1 iPSC-RPE
  model.

This review supplies the **baseline protocols those instances are built on**, which
makes it a direct test of
[nams-registry#86](https://github.com/monarch-initiative/nams-registry/issues/86),
whether a record describes a canonical model or one lab's instance. Read those
records before writing new ones, so the canonical and the instance descriptions agree
and the OPTN RGC model in particular is cross-referenced rather than duplicated.

## Gaps to record

- **No models on the three named disease entries**, as above.
- **Citing a review for a protocol.** Each protocol here belongs to a primary paper
  the review cites. Whether a record cites this review, the primary paper, or both
  needs deciding; the precedent in `Parkinsons_Disease.yaml` is a generic organoid
  record citing a review (PMID:42727800). Report what was done either way.

## Deliverables

1. One model-to-mechanism row per pairing, verified against the full text with an
   exact quote.
2. For pairings that map to a node, a `ModelMechanismLink` with `relationship`,
   `fidelity`, `model_scale`, `readouts` and `limitations`, drawing the fidelity
   content from the fetal-retina comparisons above.
3. Three NAM records in
   [nams-registry](https://github.com/monarch-initiative/nams-registry), one per cell
   product: the retinal organoid, the retinal ganglion cell, and the photoreceptor.
   The protocol variants in the three tables are described differences on those
   records, not records of their own — but report whether any variant differs enough
   to deserve its own, since that would revisit the granularity rule set for this
   round. Each record names `scientific-literature` and
   `complement-arie-landscape-dashboard` with this paper's DOI, and carries
   `dismech_status`.
4. A line in the review log's row for this paper: the entries changed, the gap issues
   opened, and the pull requests.



## Output

# NAM mining: iPSC protocols for retinal organoids, RGCs and photoreceptors (PMID:37686457)

*OpenScientist deep-research run for the Complement-ARIE disease-paper round
([nams-registry#37](https://github.com/monarch-initiative/nams-registry/issues/37)).*

- **Reference:** PMID:37686457 · DOI [10.3390/ijms241713652](https://doi.org/10.3390/ijms241713652) · *Int J Mol Sci* 24(17):13652 (2023) · open access, PMC10487913.
- **Title:** *Establishing Functional Retina in a Dish: Progress and Promises of Induced Pluripotent Stem Cell-Based Retinal Neuron Differentiation* (Wong, Yip, Huang).
- Full text retrieved and parsed via Europe PMC (62,800 chars); every quote below verified against it.
- dismech assessed at commit `3b9cbe3c4b1374a2631c1d924054535dd062d532` (2026-11-13); nams-registry at `38f81296983cbb71c3f8912a09f793836864bb5a`.

---

## 1. Summary — answer to the research question

PMID:37686457 is a **methods review**, not a disease study. It describes three
canonical, **wild-type** human-iPSC cell products — retinal organoids, retinal
ganglion cells (RGCs) and photoreceptors — across published differentiation
protocols (Tables 1–3), with no patient-derived or disease-genotype line anywhere
in the body. It therefore yields **three canonical NAM records** and **cell-type /
substrate model links**, plus unusually good **fetal-retina fidelity** content — but
it does **not** support any disease-mechanism *recapitulation* claim on its own.
Accordingly, every model-to-mechanism pairing is curated with relationship
**`MEASURES`** (not `RECAPITULATES`), fidelity **`MODERATE`**, and an explicit
**`CAUSE_UNREPRESENTED`** divergence (the disease lesion is not encoded). The
`retinoid_visual_cycle_disruption` module is confirmed to be the **wrong anchor**
(it scopes to RPE chromophore recycling, not differentiation chemistry), and the
canonical RGC record **cross-references** the existing isogenic OPTN(E50K) hPSC-RGC
instance rather than duplicating it.

---

## 2. What kind of paper this is (verified)

- Reviews **exactly three cell products**, each with its own protocol table:
  retinal organoids (Table 1, 7 studies), RGCs (Table 2, 9 studies), photoreceptors
  (Table 3, 9 studies), plus validation methods (IF, qPCR, flow cytometry, scRNA-seq,
  TEM, patch-clamp, MEA, calcium imaging).
- Named diseases appear **only as motivation**: *"various retinal degenerative
  diseases such as retinitis pigmentosa (RP), glaucoma, and age-related macular
  degeneration (AMD) can lead to vision loss or blindness"* (abstract); RP/glaucoma/AMD
  recur in the Introduction and Perspectives as rationale.
- **No disease genotype or patient line** is described. The scope statement is explicit:
  *"This review focuses on the protocols, culture conditions, and techniques employed
  in differentiating retinal neurons from iPSCs."*
- The three products are the cell populations whose loss **defines** the named
  diseases: photoreceptors (RP, AMD) and RGCs (glaucoma).

---

## 3. Deliverable 1 — Model-to-mechanism rows (one per pairing, quote-verified)

Mechanism nodes are from `kb/modules/photoreceptor_degeneration.yaml`. All
relationships are **`MEASURES`** because the models carry no disease lesion (see §5).

| # | Model (cell product) | Mechanism node (module#node) | Relationship | Verbatim support from PMID:37686457 full text |
|---|---|---|---|---|
| 1 | iPSC retinal organoid | `photoreceptor_degeneration#Photoreceptor Gene Defect` (substrate: rod/photoreceptor cell) | MEASURES | *"Mature photoreceptors are identified using specific cell markers such as S opsin (OPN1SW), L/M opsin (OPN1L/MW), RHO, CRX, and NR2E3"* — organoids contain and read out the photoreceptor population the node is situated in. |
| 2 | iPSC retinal organoid | `photoreceptor_degeneration#Secondary Cone Degeneration and Outer Retinal Thinning` (substrate: outer nuclear layer / cones) | MEASURES | *"iPSC-derived retinal cells exhibit the temporal order of embryonic retinal development and replicate the cellular mosaics and lamination of the human retina"* (Introduction) — provides the laminated outer-retinal tissue scale; but the disease lesion is absent. |
| 3 | iPSC photoreceptor | `photoreceptor_degeneration#Photoreceptor Gene Defect` (substrate: rod/photoreceptor cell) | MEASURES | *"OTX2 and recoverin (RCVRN) are used to demonstrate functional photoreceptors after differentiation … The expression of RHO confirms the presence of functional rod cells"* — reads out the phototransduction components whose mutation is the node's trigger, in healthy form. |
| 4 | iPSC photoreceptor | `photoreceptor_degeneration#Photoreceptor Metabolic and Oxidative Stress` (substrate: photoreceptor cell) | MEASURES (maturation/ultrastructure readout only) | *"TEM analysis has also been employed to compare the maturation of photoreceptors differentiated with 9-cis retinal treatment versus ATRA treatment, showing a more advanced stage of maturation in photoreceptors treated with 9-cis retinal"* — reads out outer-segment ultrastructure/maturation, the substrate of oxidative-stress pathology, without inducing it. |
| 5 | iPSC RGC | *(no photoreceptor_degeneration node applies)* — RGC is the glaucoma substrate; see cross-reference to OPTN record | MEASURES | *"co-expression of BRN3A and SNCG is a characteristic feature of mature RGCs"*; functional readout: *"calcium entry in immature RGCs upon depolarization induced by a GABA agonist … Mature RGCs did not demonstrate a depolarization-induced calcium influx."* |

> RGCs do **not** map to a `photoreceptor_degeneration` node. Their disease home is
> glaucoma; the pairing is handled by cross-reference to the existing
> `OPTN-related_Open_Angle_Glaucoma.yaml` instance (§6), not by a new mechanism link
> here.

---

## 4. Deliverable 2 — `ModelMechanismLink` drafts (dismech)

These attach as `experimental_models[].modeled_mechanisms` on the disease entries
(same structure as the existing OPTN record). Three example links are given; the
rest follow the §3 rows. `model_scale: CELLULAR` for the purified cell products;
`TISSUE` for the organoid.

### 4a. On `Inherited_Retinal_Dystrophy.yaml` — photoreceptor product
```yaml
experimental_models:
- name: iPSC-derived photoreceptors (canonical differentiation protocols)
  experimental_model_type: IPSC_DERIVED_MODEL
  cell_source: Human induced pluripotent stem cells; no disease genotype (wild-type reference protocols).
  culture_system: 2D directed differentiation and organoid-derived/bioreactor formats (review of multiple protocols).
  description: >
    Canonical wild-type human iPSC-derived photoreceptors reviewed in PMID:37686457
    (Table 3): signaling-modulator, modulator-free, small-molecule-inhibitor and
    stirred-tank-bioreactor protocols. Models the human photoreceptor cell type and
    its maturation, NOT a disease lesion.
  modeled_mechanisms:
  - target: Photoreceptor Metabolic and Oxidative Stress
    relationship: MEASURES
    fidelity: MODERATE
    model_scale: CELLULAR
    description: >
      Reads out photoreceptor identity, phototransduction-component expression and
      outer-segment ultrastructure/maturation (the substrate of the node), without
      encoding or inducing the oxidative-stress cascade.
    readouts:           # range = ExperimentalReadout; each readout's `target` repeats the link target
    - name: Photoreceptor identity marker panel (OTX2/RCVRN/CRX/NRL/NR2E3, RHO/opsins)
      target: Photoreceptor Metabolic and Oxidative Stress
      direction: UNCHANGED      # wild-type cells; healthy expression, no stress phenotype
      assays: [immunofluorescence, qPCR, flow cytometry]
      interpretation: >
        Confirms the phototransduction/identity substrate is present and healthy; it
        reads out the node's cell type, not an oxidative-stress phenotype.
    - name: Photoreceptor outer-segment ultrastructure (TEM)
      target: Photoreceptor Metabolic and Oxidative Stress
      direction: ALTERED        # maturation advances with 9-cis-retinal vs ATRA
      assays: [transmission electron microscopy]
      interpretation: >
        TEM of outer segment, inner segment, connecting cilium and basal body; 9-cis-retinal
        yields "a more advanced stage of maturation" than ATRA — a maturation readout, not disease.
    limitations: >
      Wild-type cells with no disease allele; developmentally immature relative to
      adult photoreceptors; scRNA-seq shows photoreceptor developmental trajectories
      that diverge from fetal retina.
    divergences:
    - divergence_type: CAUSE_UNREPRESENTED
      description: >
        No retinal-dystrophy lesion (e.g. RHO, PDE6, RPGR, PRPH2, RPE65, ABCA4) is
        present; the model is the healthy cell type, so degeneration is not reproduced,
        only its cellular substrate is measured.
    - divergence_type: CALIBRATION_PROVENANCE
      description: >
        Maturation benchmarked against human fetal (not adult) retina by scRNA-seq,
        and photoreceptor trajectory is the cell type the same comparison flags as divergent.
    evidence:
    - reference: PMID:37686457
      reference_title: "Establishing Functional Retina in a Dish: Progress and Promises of Induced Pluripotent Stem Cell-Based Retinal Neuron Differentiation."
      supports: SUPPORT
      evidence_source: OTHER
      snippet: "TEM analysis has also been employed to compare the maturation of photoreceptors differentiated with 9-cis retinal treatment versus ATRA treatment, showing a more advanced stage of maturation in photoreceptors treated with 9-cis retinal"
      explanation: >
        A review (evidence_source OTHER) documenting the TEM maturation readout the
        link records, with no disease lesion involved.
```

### 4b. On `Age_Related_Macular_Degeneration.yaml` — organoid product
Same shape, `target: Secondary Cone Degeneration and Outer Retinal Thinning`,
`model_scale: TISSUE`, readouts = laminar/outer-nuclear-layer markers + scRNA-seq
composition, with an additional divergence:
```yaml
    divergences:
    - divergence_type: CAUSE_UNREPRESENTED
      description: No AMD-associated lesion (e.g. complement/CFH, drusen biology) is encoded.
    - divergence_type: BOUNDARY_OMISSION
      description: >
        No RPE–photoreceptor–choriocapillaris–immune interface; the review notes
        multifactorial AMD "might require … co-culturing with RPE or the incorporation
        of the vascular network" to recapitulate physiological interactions.
```
Supporting snippet (verified): *"regarding multifactorial traits such as AMD or
diabetic retinopathy, more complicated culture conditions like co-culturing with RPE
or the incorporation of the vascular network might be required to recapitulate
physiological interactions."*

### 4c. On `Glaucoma.yaml` — RGC product
`experimental_model_type: IPSC_DERIVED_MODEL`; **no `photoreceptor_degeneration`
target** (wrong cell type). The RGC product is listed as a glaucoma `experimental_model`
with a narrative cross-reference note to the dismech OPTN(E50K) instance (§6; not a
registry `compared_with`, which must point at an nams-registry record). If a glaucoma
RGC pathophysiology node exists, attach `relationship: MEASURES`, readouts =
BRN3A/SNCG/RBPMS/THY1 identity + patch-clamp + GABA-agonist calcium maturation staging;
`CAUSE_UNREPRESENTED` divergence (no OPTN/MYOC/elevated-IOP lesion).

---

## 5. Deliverable 3 — Three NAM records (nams-registry)

**Augment-vs-create:** `nams/retinal-organoid-pluripotent-stem-cell.yaml`
**already exists** (sourced from the STEMCELL/LSCN-2022 resource; Eiraku 2011 + Zhu
2013). The correct action is to **augment** it with this paper; the **RGC and
photoreceptor records are new**.

**Granularity verdict (per round rule, one record per product):** the protocol
variants in Tables 1–3 are **described differences on one record each**, not
separate records — *except* the **NGN2-overexpression RGC protocol** (Luo et al.,
ref 58), which is transcription-factor forward-programming (*"overexpression of
neurogenin 2 (NGN2) through lentiviral transduction to expedite the differentiation
process"*, *"completed in approximately one week"*) rather than stepwise directed
differentiation. It is the **one borderline case** that could merit its own record,
and notably it is the very protocol whose cells the paper reports as *more* fetal-like
than organoid RGCs. **Recommendation: keep it as a described variant but flag it in
the round's granularity thread for a ruling.**

> Provisional NAMO typing (as the `sh-sy5y` records do): organoid = `Organoid`;
> RGC/photoreceptor purified cultures = `TwoDCellCulture` (direct differentiation) with
> an organoid-dissociation route noted — flag to maintainers, since these products are
> produced both as 2D cultures and by organoid dissociation.

### 5a. AUGMENT `nams/retinal-organoid-pluripotent-stem-cell.yaml`
Add to the existing record:
```yaml
references:              # append
- id: doi:10.3390/ijms241713652
  title: 'Establishing Functional Retina in a Dish: Progress and Promises of Induced Pluripotent Stem Cell-Based Retinal Neuron Differentiation'
  authors: [Wong IYH, Yip WWK, Huang WX]   # verify author initials against record style
  journal: International Journal of Molecular Sciences
  year: 2023
applications:            # append
- description: >-
    In vitro modeling of retinal neuron differentiation and retinal disease, and a
    source of photoreceptors/RGCs for replacement-therapy research. scRNA-seq shows
    organoids and retinospheres "closely resembled the fetal retina in terms of
    cellular composition and gene expression patterns".
  source_urls: [https://doi.org/10.3390/ijms241713652]
  supporting_references: [doi:10.3390/ijms241713652]
limitations:            # add
- description: >-
    "some differences were observed in the developmental trajectories of specific
    cell types, such as photoreceptors, between the organoids and the fetal retina" —
    composition is fetal-like but trajectory is not fully matched; organoids are
    developmentally immature.
  source_urls: [https://doi.org/10.3390/ijms241713652]
  supporting_references: [doi:10.3390/ijms241713652]
- description: >-
    Multifactorial disease modeling (AMD, diabetic retinopathy) "might require …
    co-culturing with RPE or the incorporation of the vascular network"; a bare
    organoid omits the RPE/vascular/immune interface.
  source_urls: [https://doi.org/10.3390/ijms241713652]
  supporting_references: [doi:10.3390/ijms241713652]
source_resources:       # append both
- resource: scientific-literature
  source_urls: [https://doi.org/10.3390/ijms241713652]
  accessed_on: '2026-11-14'
- resource: complement-arie-landscape-dashboard
  source_urls: [https://doi.org/10.3390/ijms241713652]
  accessed_on: '2026-11-14'
dismech_status:
  processed_through_dismech: true
  present_in_dismech: false
  dismech_commit: 3b9cbe3c4b1374a2631c1d924054535dd062d532
  assessed_on: '2026-11-14'
last_modified_date: '2026-11-14'
```

### 5b. NEW `nams/retinal-ganglion-cell-pluripotent-stem-cell.yaml`
```yaml
model:
  id: retinal-ganglion-cell-pluripotent-stem-cell
  type: TwoDCellCulture      # PROVISIONAL; also produced by organoid dissociation. Flag to maintainers.
  name: iPSC-derived retinal ganglion cells
  description: >-
    Human iPSC-derived retinal ganglion cells (RGCs), the inner-retina projection
    neuron lost in glaucoma, reviewed in PMID:37686457 (Table 2) across chemically
    defined conditions, biomaterial scaffolds for neurite outgrowth, dual-SMAD plus
    Wnt inhibition, organoid dissociation with THY1 magnetic-activated cell sorting
    (Rabesandratana et al.), and a rapid ~1-week NGN2-overexpression protocol (Luo
    et al.). Wild-type reference cells; no disease genotype. Directly differentiated
    RGCs resemble fetal RGCs more closely than organoid-derived RGCs.
  organ_modeled: {id: UBERON:0000966, name: retina}
  cell_types: [{id: CL:0000740, name: retinal ganglion cell}]
  cell_source: Human induced pluripotent / pluripotent stem cells; no disease genotype.
  three_d_architecture: MONOLAYER   # PROVISIONAL; organoid-dissociation route is 3D-derived
  culture_conditions: >-
    Multiple protocols: chemically defined medium; dual-SMAD + Wnt inhibition;
    biomaterial scaffolds; organoid dissociation + poly-D-lysine/laminin replating +
    THY1 MACS enrichment; NGN2 lentiviral forward-programming with doxycycline
    induction, GDNF, and Notch inhibition (DAPT).
  references:
  - {id: doi:10.3390/ijms241713652, title: 'Establishing Functional Retina in a Dish …', journal: International Journal of Molecular Sciences, year: 2023}
synonyms: [iPSC-RGC, hPSC-derived retinal ganglion cells, stem-cell-derived RGCs]
species: [{id: NCBITaxon:9606, name: Homo sapiens}]
applications:
- description: >-
    Glaucoma / optic-neuropathy disease modeling and RGC replacement research; a
    platform for RGC electrophysiology (patch-clamp, MEA) and maturation staging.
  source_urls: [https://doi.org/10.3390/ijms241713652]
  supporting_references: [doi:10.3390/ijms241713652]
- description: >-
    Maturation staging by calcium imaging: "calcium entry in immature RGCs upon
    depolarization induced by a GABA agonist … Mature RGCs did not demonstrate a
    depolarization-induced calcium influx."
  source_urls: [https://doi.org/10.3390/ijms241713652]
  supporting_references: [doi:10.3390/ijms241713652]
limitations:
- description: >-
    Organoid-derived and directly-differentiated RGCs differ in identity: directly
    differentiated/fetal RGCs "predominantly expressed BRN3A, whereas most organoid
    RGCs express BRN3B"; the sourcing route changes the product.
  source_urls: [https://doi.org/10.3390/ijms241713652]
  supporting_references: [doi:10.3390/ijms241713652]
- description: >-
    Wild-type reference cells with no glaucoma lesion (OPTN/MYOC/elevated IOP), and
    developmentally immature relative to the adult neurons that degenerate in glaucoma.
  source_urls: [https://doi.org/10.3390/ijms241713652]
  supporting_references: [doi:10.3390/ijms241713652]
source_resources:
- {resource: scientific-literature, source_urls: [https://doi.org/10.3390/ijms241713652], accessed_on: '2026-11-14'}
- {resource: complement-arie-landscape-dashboard, source_urls: [https://doi.org/10.3390/ijms241713652], accessed_on: '2026-11-14'}
compared_with: []
# NOTE: `compared_with.nam` MUST reference an existing nams-registry record. The
# OPTN(E50K) genotype instance (PMID:39425218) lives in *dismech* as an
# experimental_model on OPTN-related_Open_Angle_Glaucoma.yaml, NOT in nams-registry,
# so it cannot be a compared_with target here. That canonical-vs-instance
# cross-reference is handled on the dismech side (§4c, §6). If a registry record is
# ever created for the OPTN(E50K) instance, add it to compared_with then.
dismech_status:
  processed_through_dismech: true
  present_in_dismech: false
  dismech_commit: 3b9cbe3c4b1374a2631c1d924054535dd062d532
  assessed_on: '2026-11-14'
creation_date: '2026-11-14'
last_modified_date: '2026-11-14'
```

### 5c. NEW `nams/photoreceptor-pluripotent-stem-cell.yaml`
```yaml
model:
  id: photoreceptor-pluripotent-stem-cell
  type: TwoDCellCulture      # PROVISIONAL; also produced in organoid/bioreactor formats
  name: iPSC-derived photoreceptors
  description: >-
    Human iPSC-derived photoreceptors (rods and cones), the outer-retina cells lost
    in retinitis pigmentosa and AMD, reviewed in PMID:37686457 (Table 3) across
    signaling-modulator, modulator-free, small-molecule-inhibitor and stirred-tank
    bioreactor protocols. Wild-type reference cells; no disease genotype.
  organ_modeled: {id: UBERON:0000966, name: retina}
  cell_types:
  - {id: CL:0000604, name: retinal rod cell}
  - {id: CL:0000573, name: retinal cone cell}
  - {id: CL:0000210, name: photoreceptor cell}
  cell_source: Human induced pluripotent / pluripotent stem cells; no disease genotype.
  three_d_architecture: MONOLAYER
  culture_conditions: >-
    Multiple protocols: defined conditions with signaling modulators; without
    extrinsic modulators; small-molecule inhibitors; stirred-tank bioreactor
    (Ovando-Roche et al.) for highest yield, enhanced proliferation and reduced
    apoptosis; 9-cis-retinal to advance rod outer-segment maturation.
  references:
  - {id: doi:10.3390/ijms241713652, title: 'Establishing Functional Retina in a Dish …', journal: International Journal of Molecular Sciences, year: 2023}
synonyms: [iPSC-photoreceptors, hPSC-derived photoreceptors, iPSC-derived rods and cones]
species: [{id: NCBITaxon:9606, name: Homo sapiens}]
applications:
- description: >-
    Retinitis pigmentosa / AMD modeling and photoreceptor replacement research;
    ultrastructural validation by TEM (outer segment, inner segment, connecting
    cilium, basal body) and phototransduction-marker readouts.
  source_urls: [https://doi.org/10.3390/ijms241713652]
  supporting_references: [doi:10.3390/ijms241713652]
limitations:
- description: >-
    scRNA-seq flags photoreceptors as a cell type whose "developmental trajectories"
    diverge from fetal retina even when overall composition is fetal-like; cells are
    developmentally immature.
  source_urls: [https://doi.org/10.3390/ijms241713652]
  supporting_references: [doi:10.3390/ijms241713652]
- description: >-
    Wild-type reference cells with no RP/AMD lesion; maturation is protocol-dependent
    (9-cis-retinal advances maturation over ATRA by TEM).
  source_urls: [https://doi.org/10.3390/ijms241713652]
  supporting_references: [doi:10.3390/ijms241713652]
source_resources:
- {resource: scientific-literature, source_urls: [https://doi.org/10.3390/ijms241713652], accessed_on: '2026-11-14'}
- {resource: complement-arie-landscape-dashboard, source_urls: [https://doi.org/10.3390/ijms241713652], accessed_on: '2026-11-14'}
dismech_status:
  processed_through_dismech: true
  present_in_dismech: false
  dismech_commit: 3b9cbe3c4b1374a2631c1d924054535dd062d532
  assessed_on: '2026-11-14'
creation_date: '2026-11-14'
last_modified_date: '2026-11-14'
```

---

## 6. Existing records this sits beside (read before writing)

- **`OPTN-related_Open_Angle_Glaucoma.yaml`** already holds an `experimental_models`
  entry: *"Isogenic OPTN(E50K) human pluripotent stem cell-derived retinal ganglion
  cells"* (`IPSC_DERIVED_MODEL`), `modeled_mechanisms: RECAPITULATES` →
  *"Impaired Autophagic Flux in Retinal Ganglion Cells"*, **fidelity HIGH**, evidence
  PMID:39425218. Its own `limitations` already note *"hPSC-derived retinal ganglion
  cells are developmentally immature relative to the adult neurons that degenerate."*
  **The canonical RGC NAM record is the baseline this dismech instance is built on →
  cross-reference it, do not duplicate.** Note on mechanics: this cross-reference is a
  *narrative/evidence* link, NOT a registry `compared_with` field — `compared_with.nam`
  can only point at another existing *nams-registry* record, and the OPTN(E50K) instance
  lives in dismech, not the registry. So the new canonical RGC record leaves
  `compared_with: []` (§5b), and the OPTN↔canonical relationship is documented here and on
  the dismech side (§4c). The contrast (RECAPITULATES/HIGH for the genotype instance vs
  MEASURES/MODERATE for the canonical product) is exactly the nams-registry#86
  canonical-vs-instance distinction working as intended.
- `Leber_Congenital_Amaurosis_10.yaml` (CEP290 patient iPSC optic cups/RPE + sepofarsen),
  `RDH12-Related_Dominant_Retinopathy.yaml` (RDH12 patient organoids) and
  `Stargardt_Disease.yaml` (patient organoid + STGD1 iPSC-RPE) are all genotype
  instances built on these same baseline protocols; the canonical records give them a
  shared, citable baseline.

---

## 7. Deliverable 4 — Review-log line & gap issues

**Line for `projects/COMPLEMENT_ARIE_DISEASE_PAPERS.md` (this paper's row):**

> PMID:37686457 — methods review, three canonical iPSC products. **nams-registry:**
> augmented `nams/retinal-organoid-pluripotent-stem-cell.yaml` (added this paper,
> fetal-retina fidelity/limitations, `scientific-literature` +
> `complement-arie-landscape-dashboard`, `dismech_status`); added NEW
> `retinal-ganglion-cell-pluripotent-stem-cell` and `photoreceptor-pluripotent-stem-cell`.
> **dismech:** proposed `experimental_models` (MEASURES / MODERATE /
> CAUSE_UNREPRESENTED) as first models on `Inherited_Retinal_Dystrophy`, `AMD` and
> `Glaucoma`; RGC cross-referenced to the OPTN(E50K) instance; **no** link to
> `retinoid_visual_cycle_disruption` (wrong anchor — RA/9-cis here is differentiation
> chemistry, not RPE chromophore recycling). Granularity: protocol variants are
> described differences, NGN2 forward-programming flagged as the one borderline case.

**Gap issues to open:**
1. *No models on three named disease entries* — `AMD.yaml`, `Glaucoma.yaml`,
   `Inherited_Retinal_Dystrophy.yaml` have no `experimental_models`/`animal_models`/
   `computational_models`; these canonical products would be the first.
2. *Review-vs-primary citation* — each protocol belongs to a primary paper the review
   cites; precedent `Parkinsons_Disease.yaml` cites a review (PMID:42727800).
   **Done here:** records cite the review (PMID:37686457) as the source that groups the
   products, with primary authors named in-text (Sridhar, Luo, Rabesandratana,
   Ovando-Roche, Reichman); recommend adding primary DOIs as additional `references`
   where a specific protocol's data is used.
3. *NAMO typing for purified iPSC-derived neurons* (RGC, photoreceptor) produced both
   as 2D cultures and by organoid dissociation — provisional `TwoDCellCulture`; confirm.
4. *NGN2 forward-programming granularity* — ruling on whether it deserves its own record.

---

## 8. Hypotheses: supported / refuted

- **Supported:** Paper is a canonical methods review → three NAM records + fidelity
  content (fetal-retina scRNA-seq, BRN3A/BRN3B, 9-cis-retinal TEM, GABA-calcium).
- **Supported:** Relationship is MEASURES, not RECAPITULATES — no disease lesion is
  encoded (schema `CAUSE_UNREPRESENTED`).
- **Refuted:** `retinoid_visual_cycle_disruption` as an anchor — its own scope is the
  RPE65/LRAT/ABCA4 chromophore relay; the protocols' retinoids are differentiation
  chemistry. No link.
- **Refuted:** a *new* organoid record — one already exists; augment instead.

## 8a. Schema-verification notes (iteration 4)

All identifiers and controlled values were checked against live schemas/ontologies:

- **Cell ontology IDs verified (OLS):** `CL:0000740` retinal ganglion cell ✓,
  `CL:0000604` retinal rod cell ✓, `CL:0000573` retinal cone cell ✓, `CL:0000210`
  photoreceptor cell ✓; `UBERON:0000966` retina (from the existing organoid record).
- **`ModelDivergenceTypeEnum` verified:** only four values exist —
  `BOUNDARY_OMISSION`, `PROXY_QUANTITY`, `CALIBRATION_PROVENANCE`,
  `CAUSE_UNREPRESENTED`. The report uses only valid ones.
- **`readouts` is structured, not free text:** range is `ExperimentalReadout`
  (slots: `name`, `target` [required, must repeat the link target], `phenotype_term`,
  `biomarker_term`, `biological_processes`, `assays`, `direction`
  [`ModelReadoutDirectionEnum`: INCREASED/DECREASED/UNCHANGED/RESTORED/ABOLISHED/ALTERED],
  `interpretation`, `evidence`). §4a was rewritten to this structure.
- **No duplicate records:** a full scan of `nams/` and `partial-nams/` finds only
  `retinal-organoid-pluripotent-stem-cell.yaml`; the RGC and photoreceptor records
  are genuinely new.
- **`resource: complement-arie-landscape-dashboard`** confirmed present at
  `resources/complement-arie-landscape-dashboard.yaml`.

## 9. Limitations & future directions

- No PRs were pushed from this run (no write access in-session); records and links
  above are complete drafts ready to open against nams-registry and dismech.
- NAMO `type`/architecture enum values for the two purified-neuron records are
  provisional and need confirmation against the imported NAMO schema.
- Primary-protocol DOIs (Sridhar, Luo = PMID ref 58, Rabesandratana, Ovando-Roche,
  Reichman) should be resolved and added as additional `references` when each
  protocol's specific data is curated onto a disease node.


## Artifacts

- [OpenScientist final report](PMID_37686457-paper-review-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PMID_37686457-paper-review-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 1 |
| References weighed for topical relevance | 4 |
| On topic | 3 |
| Off topic | 0 |

4 of 5 references resolved; the rest could not be looked up either way.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.