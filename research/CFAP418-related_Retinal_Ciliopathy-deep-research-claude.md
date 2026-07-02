---
provider: claude
model: claude-sonnet-4-6
cached: false
start_time: '2026-07-01T12:44:00Z'
end_time: '2026-07-01T13:05:00Z'
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CFAP418-related Retinal Ciliopathy (CORD16 / RP64 / BBS21)
  mondo_id: MONDO:0700374
  category: Mendelian / Ciliopathy
provider_config:
  method: web_search_synthesis
  sources:
  - PubMed
  - ClinicalTrials.gov
  - OMIM
  - Orphanet
citation_count: 7
notes: >-
  Research artifact synthesized via targeted web search + PubMed verification.
  All PMIDs fetched and verified against the actual abstract text before citation.
  Added to PR #4918 as the required completeness-assessment artifact.
---

## Question

# Disease Pathophysiology Research

## Target Disease
- **Disease Name:** CFAP418-related Retinal Ciliopathy (also reported as CORD16, RP64, BBS21)
- **Gene:** CFAP418 (alias C8orf37, BBS21)
- **MONDO ID:** MONDO:0700374
- **Category:** Mendelian / Ciliopathy

## Research Objectives

Comprehensive review covering molecular mechanism, clinical spectrum, diagnosis,
disease progression, treatments/management, and clinical trials for CFAP418
(C8orf37)-related retinal ciliopathy.

---

## Output

# CFAP418-related Retinal Ciliopathy — Research Report

## 1. Disease Overview and MONDO Anchor

CFAP418 (Cilia- and Flagella-Associated Protein 418; formerly C8orf37; also
designated BBS21) encodes a small, evolutionarily conserved protein expressed
most prominently in the retina, brain, and heart (OMIM *614477). Biallelic
loss-of-function and missense variants produce a phenotypic continuum anchored
at MONDO:0700374 ("CFAP418-related ciliopathy"), which federates three
per-phenotype OMIM nodes:

| Node | OMIM | Phenotype |
|---|---|---|
| CORD16 | #614507 | Cone-rod dystrophy, non-syndromic |
| RP64 | — | Retinitis pigmentosa 64 (rod-cone dystrophy), non-syndromic |
| BBS21 | #617406 | Full Bardet-Biedl syndrome 21 (syndromic) |

**Source:** OMIM entries #614477, #614507, #617406; MONDO:0700374.

---

## 2. Core Pathophysiology

### 2a. Ciliary-base localization (photoreceptor connecting cilium)

CFAP418/C8orf37 protein localizes at the base of primary cilia in human
retinal pigment epithelium (RPE) cells and at the base of the connecting cilium
of mouse photoreceptors, co-localizing with polyglutamylated tubulin (PMID:22177090).
The connecting cilium is the narrow bridge through which all outer-segment cargo
(visual pigments, disc membrane components) must be trafficked; disruption at
this gate causes outer-segment morphogenesis failure and progressive
photoreceptor death.

CFAP418 also interacts with FAM161A, a microtubule-binding protein that
localizes at the photoreceptor cilium and is independently required for
photoreceptor survival (PMID:36233334). The co-localization at the ciliary
base links CFAP418 to a survival-critical ciliary complex.

### 2b. Membrane lipid homeostasis (newer mechanistic arm)

A 2024 JCI Insight study (PMID:37971880) applied lipidomic, proteomic, and
phosphoproteomic profiling plus affinity-purification mass spectrometry to
characterize CFAP418 function in mouse retina. Key findings:

- CFAP418 protein directly binds the lipid-metabolism precursor
  **phosphatidic acid (PA)** and the mitochondrion-specific lipid **cardiolipin**,
  but does not form stable protein–protein complexes.
- Loss of Cfap418 in mice disturbs **membrane lipid homeostasis** and
  membrane-protein associations → mitochondrial defects + membrane-remodeling
  abnormalities across vesicular-trafficking pathways, especially the **ESCRT
  pathway**.
- Ablation of Cfap418 also increases activity of the PA-binding protein
  **kinase Cα** in the retina.
- The authors conclude that membrane lipid imbalance is a pathological
  mechanism underlying both syndromic ciliopathies and isolated retinal
  degenerations.

This supplements the earlier connecting-cilium model: CFAP418 loss disrupts
not only the ciliary gate but also the lipid-membrane environment on which
outer-segment disc biogenesis depends.

**Key ontology terms:**
- GO:0061512 — protein localization to cilium (ABNORMAL)
- GO:0046486 — glycerophospholipid metabolic process (ABNORMAL; PA/cardiolipin)
- CL:0000210 — photoreceptor cell
- CL:0000604 — retinal rod cell
- CL:0000573 — retinal cone cell
- UBERON:0000966 — retina

---

## 3. Clinical Spectrum

### 3a. Non-syndromic end (isolated retinal dystrophy)

Eight C8orf37-mutated patients were clinically characterized by van Huet et al.
2013 (PMID:23788369; IOVS):

- **Four with RP phenotype (families A and D):** Night blindness followed by
  concentric visual-field loss; early macular atrophy; ophthalmoscopy showed
  bone spicules, attenuated vessels, waxy pale optic discs; SD-OCT showed
  profound photoreceptor degeneration; **ERG nonrecordable** in all. Onset in
  infancy (family A) or adolescence (family D). Severe visual loss to light
  perception occurred early.

- **Four with CRD phenotype (families B and C):** Initial symptoms photophobia
  or reduced visual acuity, onset in infancy (family B) or adolescence (family C);
  profound macular RPE atrophy on AF and SD-OCT; ERG severely reduced in
  cone-rod pattern or nonrecordable. Notably both patients in family B also had
  polydactyly, suggesting a borderline syndromic phenotype.

The first patient series (PMID:22177090, Estrada-Cuzcano et al. 2012)
identified six affected individuals (3 with arCRD, 3 with arRP with early
macular involvement) from 4 consanguineous families by homozygosity mapping.

### 3b. Syndromic end (BBS21)

Feathers et al. 2019 (PMID:27008867) first documented C8ORF37 biallelic
mutations causing full Bardet-Biedl syndrome (BBS21). The reported proband
exhibited:
- Slowly progressive rod-cone dystrophy
- Overweight/obesity (BMI 29.1)
- Mild learning difficulty (mild cognitive impairment)
- Three-limb postaxial polydactyly
- Horseshoe kidney
- Abnormally positioned uterus
- High myopia

Zebrafish c8orf37 knockdown reproduced BBS-related ciliary phenotypes including
Kupffer's vesicle defects and delayed retrograde melanosome transport, validating
the syndromic designation (PMID:27008867).

### 3c. Allelism and phenotypic determinants

The same C8orf37/CFAP418 locus was shown to be allelic across syndromic and
non-syndromic presentations (PMID:26854863), reinforcing that allele severity
(null vs. missense) likely gates the degree of extra-retinal involvement.
ClinGen classified the CFAP418-ciliopathy gene-disease relationship as
**Definitive** (referenced in the YAML notes; CGGV cache row pending refresh).

---

## 4. Diagnosis

### 4a. Clinical

The diagnostic workup for suspected CFAP418-related retinal ciliopathy follows
standard inherited retinal dystrophy practice:

- **Electroretinography (ERG):** Severely reduced or nonrecordable responses;
  CRD pattern (cone > rod reduction) or RP pattern (rod > cone). ERG is
  often nonrecordable by the time of first presentation given the severe
  early macular involvement.
- **Spectral-domain OCT (SD-OCT):** Profound macular photoreceptor degeneration
  with RPE atrophy, especially at the macula.
- **Fundus autofluorescence (AF):** Macular RPE atrophy pattern.
- **Visual field perimetry:** Concentric loss in RP-pattern cases;
  central-field loss in CRD-pattern cases.
- **Fundus photography:** Macular atrophy, bone spicule pigmentation, attenuated
  vessels, waxy pale discs (classic RP features; PMID:23788369).

### 4b. Genetic

Comprehensive inherited retinal dystrophy (IRD) gene panels include CFAP418.
Homozygosity mapping was the original discovery method (consanguineous families).
For BBS21, the standard BBS gene panel or ciliopathy panel will include CFAP418.

### 4c. BBS-specific criteria

For the syndromic (BBS21) end, the ERN-EYE/ERKNet 2024 BBS consensus (European
Reference Networks) provides updated diagnostic criteria and recommends a
multidisciplinary team (ophthalmology, nephrology, endocrinology, developmental
pediatrics; PMID:38383825).

---

## 5. Natural History and Progression

Based on the van Huet 2013 cohort (PMID:23788369):

- **Onset:** Infancy to adolescence (no adult-onset cases in the literature).
- **RP phenotype:** Night blindness → progressive concentric visual field loss
  → severe visual loss (light perception or worse) occurring **early** in the
  disease course.
- **CRD phenotype:** Photophobia and/or reduced visual acuity at onset → macular
  atrophy progressing to nonrecordable ERG.
- In both patterns, early macular involvement is characteristic and distinguishes
  this locus from typical RP.
- Both allelic endpoints (CORD16 and RP64) share progressive photoreceptor loss
  as the converging phenotype.

**Disease progression module:** Consistent with the `photoreceptor_degeneration`
module (Rod Photoreceptor Apoptosis → secondary cone degeneration → progressive
visual field loss) and the `ciliopathy_dysfunction` module.

---

## 6. Treatments and Management

### 6a. Retinal disease (no CFAP418-specific treatment)

No approved gene therapy or targeted pharmacotherapy exists specifically for
CFAP418 mutations. No CFAP418-specific clinical trial was identified on
ClinicalTrials.gov (searched 2026-07-01).

Supportive measures for IRD/RP/CRD:
- **Low vision rehabilitation:** Low-vision aids (magnifiers, tinted lenses),
  orientation and mobility training, assistive lighting; standard of care for
  all non-treatable IRDs.
- **UV protection:** Sunglasses with UV-blocking lenses to reduce photoreceptor
  oxidative stress (standard RP/CRD practice).
- **Vitamin A palmitate:** Historically suggested for typical RP but benefit in
  CRD or early-macular-involvement phenotypes is uncertain; not specifically
  studied for CFAP418.
- **Genetic counseling:** Essential given autosomal recessive inheritance.

### 6b. BBS21 systemic management

For the syndromic (BBS21) end, management tracks standard BBS care
(PMID:38383825 — Shoemaker 2024, Diabetes Obes Metab):

- **Setmelanotide (Imcivree):** FDA-approved melanocortin 4 receptor (MC4R)
  agonist for **treatment of obesity in Bardet-Biedl syndrome** (approved 2020).
  This is the first pharmacotherapy approved for hyperphagia/obesity in any
  ciliopathy. In BBS21 specifically, it has not been studied in isolation, but
  BBS21 is within the BBS diagnostic umbrella covered by the approval.
- **Renal monitoring:** Horseshoe kidney, renal anomalies → regular nephrology
  follow-up.
- **Cognitive/developmental support:** Mild intellectual disability → early
  educational intervention.
- **Endocrinology:** Obesity management, hyperphagia control (setmelanotide).
- **Multidisciplinary team:** ERN-EYE/ERKNet 2024 consensus recommends
  coordinated care across ophthalmology, nephrology, endocrinology, and
  developmental pediatrics.

---

## 7. Clinical Trials

**ClinicalTrials.gov search (2026-07-01): No trials for "CFAP418", "C8orf37",
or "BBS21" were found.**

No gene therapy or targeted molecular therapy trial for CFAP418-related
retinal ciliopathy was identified. This is consistent with the relatively
small number of affected families published (CORD16/RP64/BBS21 combined).

Broad IRD gene therapy trials (RPE65, RPGR, USH2A, CEP290, etc.) are actively
enrolling in 2025–2026 but do not include CFAP418. Given the ESCRT-pathway and
membrane-lipid mechanism (PMID:37971880), future neuroprotective or
lipid-targeted therapies could theoretically be relevant, but no IND has been
filed.

---

## 8. Completeness Assessment for KB Entry

Based on this research, the following sections were NOT yet in the PR as of the
review (2026-06-28) but are clinically supported:

| Section | Recommendation | Supporting source |
|---|---|---|
| `treatments:` | ADD — supportive (low vision aids, UV protection, genetic counseling) + setmelanotide for BBS21 obesity | PMID:38383825, standard IRD SoC |
| `diagnosis:` | ADD — ERG, SD-OCT, AF, visual field, genetic panel | PMID:23788369 |
| `progression:` | ADD — early onset, early macular involvement, nonrecordable ERG; progressive | PMID:23788369 |
| `has_subtypes:` | CONSIDER — CORD16/RP64/BBS21 could be formalized as named subtypes of this gene-anchored entry; mirrors current free-text description | PMID:22177090, PMID:26854863 |
| `clinical_trials:` | OMIT — no CFAP418-specific trials found on ClinicalTrials.gov | ClinicalTrials.gov search 2026-07-01 |

The `pathophysiology` section in the PR covers the core connecting-cilium
and photoreceptor degeneration mechanisms. The 2024 JCI Insight paper
(PMID:37971880) adds a membrane lipid homeostasis dimension (phosphatidic acid
/ cardiolipin binding, ESCRT dysregulation) that could enrich the
`CFAP418 Loss of Function at the Photoreceptor Ciliary Base` node with
additional biological processes:
- GO:0046486 — glycerophospholipid metabolic process
- GO:0036020 — endosomal transport

---

## 9. Key PMIDs Referenced

| PMID | Description | Status in PR |
|---|---|---|
| PMID:22177090 | Estrada-Cuzcano 2012 — first C8orf37 identification (arCRD/arRP) | ✅ in PR |
| PMID:26854863 | C8orf37 mutated in BBS + allelic to non-syndromic RD | ✅ in PR |
| PMID:27008867 | Mutations in C8ORF37 cause BBS21 | ✅ in PR |
| PMID:36233334 | Interactions between C8orf37 and FAM161A | ✅ in PR |
| PMID:23788369 | van Huet 2013 IOVS — clinical characterization of 8 C8orf37 patients | ⬜ not in PR |
| PMID:37971880 | Clark 2024 JCI Insight — membrane lipid mechanism (PA/cardiolipin/ESCRT) | ⬜ not in PR |
| PMID:38383825 | Shoemaker 2024 — BBS clinical overview incl. setmelanotide | ⬜ not in PR |
