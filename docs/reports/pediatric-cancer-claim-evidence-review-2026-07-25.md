# Pediatric Cancer Entries: Manual Content Review (2026-07-25)

Manual domain review of ten pediatric cancer entries in `kb/disorders/`, reading
the entries as an oncologist would: is the biology right, is the nosology
current, and is the core disease content present? Findings are ordered by how
wrong they are, not by how easy they were to find.

Entries: `Acute_Lymphoblastic_Leukemia`, `Neuroblastoma`, `Wilms_Tumor`,
`Retinoblastoma`, `Hepatoblastoma`, `Medulloblastoma`, `Ewing_Sarcoma`,
`Osteosarcoma`, `Alveolar_Rhabdomyosarcoma`, `Atypical_Teratoid_Rhabdoid_Tumor`.

---

## 1. Outright factual errors

### 1.1 `Medulloblastoma` — the WHO 2021 classification is stated incorrectly

> "WHO 2021 stratifies medulloblastoma into four molecular subgroups — WNT-activated, SHH-activated, Group 3, and Group 4"

This is the **2016 WHO / Heidelberg consensus** scheme, not WHO CNS5 (2021).
WHO 2021 defines the molecularly-defined entities as: **MB WNT-activated**;
**MB SHH-activated and TP53-wildtype**; **MB SHH-activated and TP53-mutant**
(split into two separate entities); and **MB non-WNT/non-SHH**, within which
Group 3 and Group 4 are *provisional subtypes*, not top-level groups. WHO 2021
also carries a parallel **histologically-defined** axis (classic,
desmoplastic/nodular, MBEN, large-cell/anaplastic) that this entry omits
entirely.

The entry is internally inconsistent about this: the SHH subtype description
correctly says "TP53 mutation status further stratifying prognosis under WHO
2021", which only makes sense under the scheme the top-line sentence contradicts.

### 1.2 `Neuroblastoma` — Stage 4S is defined with the wrong age cutoff

> "A special stage occurring in infants under 18 months with primary tumor and metastases limited to skin, liver, and bone marrow."

INSS **Stage 4S is <12 months**. The 18-month threshold belongs to the INRG
**stage MS**, a different staging system. The entry uses the INSS label with the
INRG cutoff. It also omits the criterion that marrow involvement must be
**minimal (<10% of nucleated cells)** — without that limit, 4S is
indistinguishable from stage 4, which is the entire clinical point of the
category.

### 1.3 `Neuroblastoma` — ALK in familial neuroblastoma is understated

> "ALK point mutations occur in 8-10% of sporadic and ~50% of familial neuroblastoma."

The sporadic figure is right. Germline *ALK* mutations account for the large
majority of hereditary neuroblastoma pedigrees — commonly cited at **~75-80%**
(Mossé et al., *Nature* 2008). "~50%" materially understates ALK's role as *the*
neuroblastoma predisposition gene.

### 1.4 `Medulloblastoma` — the cell-type binding contradicts the node's own text

The single pathophysiology node states, correctly, that "WNT tumors derive from
lower-rhombic-lip progenitors and SHH tumors from external-granule-layer
granule-neuron precursors" — then binds `cell_types` to **cerebellar granule
cell** (`CL:0001031`) alone. That is the SHH lineage only. WNT tumors arise from
lower rhombic lip / dorsal brainstem progenitors, and Group 3/4 are now
attributed to **rhombic-lip-derived progenitors and unipolar brush cells**
(Hendrikse et al. and Smith et al., *Nature* 2022). The binding is wrong for
three of the four subgroups the node claims to cover.

### 1.5 `Ewing_Sarcoma` — "pathognomonic" is too strong, and WHO reclassification is missing

> "characterized by the pathognomonic EWS-FLI1 fusion gene, present in approximately 85% of cases"

*EWSR1* rearrangement is not pathognomonic — it occurs in desmoplastic small
round cell tumor, clear cell sarcoma, myxoid liposarcoma, and others. More
importantly, the WHO 2020 soft-tissue classification **split
`CIC`-rearranged sarcoma and `BCOR`-rearranged sarcoma out of the Ewing family**
as separate entities; the entry does not reflect this. And the ~15% of cases that
are not EWS-FLI1 are nowhere modeled — most are **EWSR1-ERG** (t(21;22), ~10%),
with rarer FEV/ETV1/ETV4 partners. For an entry with 16 pathophysiology nodes
devoted to fusion biology, omitting the second-most-common fusion is a
substantive hole.

### 1.6 `Wilms_Tumor` — TP53 frequency contradicts itself

`genetic[6]` says TP53 mutations occur in "approximately 50-60% of diffuse
anaplastic Wilms tumors"; `histopathology[4]` says "nearly all anaplastic Wilms
tumors harbor TP53 mutations". Both cite the same source, which says "nearly all
… if one looks hard enough". The 50-60% is the outlier and should go — current
understanding is that TP53 alteration is near-universal in diffuse anaplasia when
adequately assayed.

### 1.7 Same drug, two different chemical entities

`Neuroblastoma` binds cyclophosphamide to `CHEBI:4026` — whose label, recorded in
the file itself, is **"cyclophosphamide hydrate"** — while `Medulloblastoma`
binds `CHEBI:4027` "cyclophosphamide". The monohydrate is a different chemical
entity from the drug substance. Both labels are real, so this is invisible to
term validation; it should be `CHEBI:4027` in both.

---

## 2. Nosology / classification problems

### 2.1 `Wilms_Tumor` — the subtype list conflates four orthogonal axes

`has_subtypes` lists as siblings: **histology** (Favorable, Anaplastic,
Blastemal, Epithelial, Stromal, Mixed), **laterality** (Bilateral, Unilateral),
**etiology** (Hereditary, Sporadic), and **age** (Childhood, Adult).

"Unilateral", "Sporadic", and "Childhood" are not subtypes — they are the
default case, and their descriptions say as much ("Most Wilms tumors present as
unilateral renal masses"). Worse, the histology entries mix **two incompatible
classification systems**: "Favorable/Anaplastic" is the COG system applied at
upfront nephrectomy, while "Blastemal/Epithelial/Stromal-predominant" is the SIOP
system applied *after* preoperative chemotherapy. The entry's own treatment
section correctly explains that COG and SIOP differ in exactly this way, then the
subtype list flattens both into one namespace. Since `has_subtypes[].name` is the
foreign-key target for `subtype:` references elsewhere, this makes the axis
unusable.

### 2.2 `Atypical_Teratoid_Rhabdoid_Tumor` — subgroups named but not modeled

TYR, SHH, and MYC are correctly identified as the three consensus methylation
subgroups, but they carry no mechanism. The distinguishing biology — TYR
(melanosomal/tyrosinase program, infratentorial, youngest), SHH (SHH/NOTCH
signaling, supra- and infratentorial), MYC (MYC/HOX, supratentorial) — is absent,
and the SHH subgroup is not linked to any SHH mechanism module despite the KB
having the machinery for it. The pathograph terminates in a generic "Aggressive
Tumor Cell Proliferation" node that could belong to any cancer.

---

## 3. Missing core disease content

### 3.1 `Osteosarcoma` — no histopathology, no biochemistry, and the key prognostic factor is absent

`histopathology: []` and `biochemical: []` are both **empty**. For osteosarcoma
this is the most serious content gap in the ten entries:

- The **defining diagnostic criterion** — production of malignant osteoid by
  neoplastic cells — is never stated as a pathology finding.
- The histologic subtypes (osteoblastic ~50%, chondroblastic ~25%, fibroblastic
  ~25%) are absent.
- **Percent tumor necrosis after neoadjuvant chemotherapy (Huvos grade; ≥90% =
  good responder)** — the single strongest prognostic factor in localized
  osteosarcoma, and the entire reason chemotherapy is given *before* surgery — is
  absent. The entry describes neoadjuvant MAP without ever explaining what it is
  for.
- **Alkaline phosphatase and LDH**, standard prognostic labs, are absent.
- Radiographic hallmarks (**Codman triangle**, sunburst periosteal reaction) are
  absent.

Subtypes list only Conventional High-Grade, Telangiectatic, and Small Cell —
omitting **parosteal** and **periosteal** surface osteosarcomas (low/intermediate
grade, managed very differently) and **secondary osteosarcoma** (Paget disease,
prior radiation). The entry's own cited source lists "low grade central,
telangiectatic, small-cell, surface and intracortical", so these were available
and dropped.

Predisposition syndromes (Li-Fraumeni, hereditary retinoblastoma,
Rothmund-Thomson, Werner, Bloom, Diamond-Blackfan) appear only inside a quoted
snippet, never as structured content — even though the `Retinoblastoma` entry in
this same KB names osteosarcoma as its principal second malignancy. The
cross-reference is one-directional.

### 3.2 `Neuroblastoma` — the last decade of neuroblastoma biology is missing

The pathograph has three nodes, and **`ALK Signaling Activation` is an orphan**
with no `downstream` edge at all — it connects to nothing. Absent entirely:

- **Telomere maintenance**, the axis that now organizes neuroblastoma risk
  biology: *MYCN* amplification, ***TERT* rearrangement**, and ***ATRX*
  mutation/ALT** (the latter defining the indolent adolescent/young-adult
  subtype). Neither TERT nor ATRX appears anywhere.
- ***PHOX2B*** — a genuine germline predisposition gene (with Hirschsprung
  disease and congenital central hypoventilation) — appears only inside a quoted
  snippet, not as a curated gene.
- **Adrenergic vs mesenchymal cell-state plasticity**, the dominant conceptual
  advance in the field.
- **Spontaneous regression** — called a defining feature in the entry's own
  description, then never modeled, despite being the mechanistically interesting
  thing about neuroblastoma (TrkA/NGF-dependent apoptosis, telomere maintenance
  failure).
- **Opsoclonus-myoclonus syndrome**, the classic paraneoplastic presentation;
  also **Horner syndrome** and **dumbbell-tumor spinal cord compression**. VIP
  diarrhea is present, so the paraneoplastic category was considered.
- **MIBG therapy** and **ALK inhibitors** as treatments — crizotinib is named in
  prose under the ALK node, and lorlatinib is now in frontline COG trials, yet
  no ALK-directed treatment is curated even though ALK is modeled as a mechanism.
- **International Neuroblastoma Pathology Classification (Shimada)** — favorable
  vs unfavorable histology by MKI, differentiation, and stromal content. The
  entire `histopathology` block is one content-free node reading "Neuroblastoma
  is a malignant tumor of neural crest origin."

Notably, the entry's own bottom-of-file `references` list cites papers on
noradrenergic/mesenchymal identity transitions, SWI/SNF and cell plasticity, and
telomere-maintenance copy-number dosage — all with `findings: []`. The entry has
collected the literature for the biology it is missing and never modeled it.

### 3.3 `Retinoblastoma` — the exceptions to the two-hit model are absent

The description asserts flatly that "**Biallelic loss of RB1 function is required
for tumorigenesis**". This is contradicted by the recognized **MYCN-amplified,
RB1-wildtype** retinoblastoma (~2% of cases; unilateral, very early onset,
aggressive histology — Rushlow et al., *Lancet Oncol* 2013). An entry built
entirely around two-hit sufficiency should carry its principal counterexample.

Also missing:

- **Trilateral retinoblastoma** (intracranial pineal/suprasellar tumor in
  germline carriers) — clinically critical, and dismech already has a
  `Pineoblastoma` entry to link to.
- The cell of origin is bound to **retinal progenitor cell**; current evidence
  favors the **maturing cone precursor**.
- That RB1 loss alone is insufficient in humans — progression requires additional
  events (MYCN, MDM4 gain, BCOR, 1q/6p gain).
- **Intravitreal chemotherapy** for vitreous seeds, now standard alongside the
  intra-arterial route the entry does describe.
- 13q14 deletion syndrome.

The entry also cites PMID:41567907 — a paper specifically about *adjuvant
chemotherapy for high-risk histopathologic features after enucleation* — solely
for the throwaway line "retinoblastoma is the most common intraocular
malignancy", while the paper's actual subject (postlaminar optic nerve invasion
and massive choroidal invasion driving adjuvant therapy) goes unused. Those
high-risk features are themselves absent from the entry.

### 3.4 `Alveolar_Rhabdomyosarcoma` — the alveolar architecture is never described

The single `histopathology` node reads, in full: *"Rhabdomyosarcoma is a
malignant tumor of mesenchymal origin."* The disease is **named for** its
histologic pattern — discohesive cells lining fibrovascular septa in an
alveolar-like arrangement, with wreath-like multinucleated giant cells — and that
pattern appears nowhere. Also missing: **primary site** (parameningeal, orbit,
genitourinary), which is among the strongest prognostic variables in
rhabdomyosarcoma, and IRS grouping/stage.

### 3.5 `Medulloblastoma` — no genetics block, no histology, no dissemination

- **No `genetic:` section at all**, for a tumor the entry itself describes as
  molecularly defined. Predisposition is entirely absent: **Gorlin** (PTCH1),
  **Li-Fraumeni** (TP53), **Turcot/FAP** (APC), **Fanconi anemia** (BRCA2/PALB2),
  and ***ELP1*** — the most common medulloblastoma predisposition gene, ~14% of
  SHH-MB.
- **No `histopathology:`** — classic / desmoplastic-nodular / MBEN /
  large-cell-anaplastic are WHO entities with real prognostic weight (MBEN
  favorable in infants; LCA adverse).
- **Leptomeningeal dissemination / M-stage** is the dominant prognostic factor
  and the reason craniospinal irradiation exists. It appears only as a
  justification inside the CSI treatment description — no phenotype, no
  mechanism node.
- **SHH-pathway inhibitors** (vismodegib, sonidegib) are named in the description
  as an active area but not curated as a treatment, despite being the flagship
  targeted therapy in this disease.

### 3.6 `Hepatoblastoma` — strong entry, epidemiologic and clinical gaps

The mechanism graph is the best in the set (see §5). What is missing is clinical:

- **Very low birth weight / extreme prematurity** is the strongest established
  risk factor for hepatoblastoma — absent. **Trisomy 18** likewise.
- **AFP interpretation in infancy**: physiologic AFP is very high in neonates and
  declines over the first 6-8 months. Without that, "elevated AFP" as a
  biomarker is not interpretable in the exact age group this tumor affects.
- **PRETEXT staging** appears only inside a treatment description.
- Only two phenotypes (abdominal mass, hepatomegaly). Missing precocious puberty
  from β-hCG-secreting tumors, thrombocytosis, anemia, failure to thrive.

### 3.7 `Acute_Lymphoblastic_Leukemia` — excellent, with clinical omissions

- **Down syndrome-associated ALL** — a major epidemiologic subgroup with distinct
  biology (CRLF2, JAK2) and markedly different treatment toxicity.
- **Infant KMT2A-rearranged ALL** — KMT2A-r exists as a subtype but the infant
  context (dismal prognosis, distinct biology) is prose only.
- **Tumor lysis syndrome** and **hyperleukocytosis** — the defining acute
  complications at presentation.
- **TPMT / NUDT15 pharmacogenomics** — the flagship pediatric-oncology
  pharmacogenetic, governing 6-mercaptopurine dosing through two-plus years of
  maintenance.
- **CNS status (CNS1/2/3)**, which drives the intrathecal therapy the entry does
  curate.

### 3.8 `Atypical_Teratoid_Rhabdoid_Tumor` — predisposition syndrome unstructured

**Rhabdoid tumor predisposition syndrome (RTPS1/RTPS2)** — germline SMARCB1 or
SMARCA4 alterations in roughly 25-35% of AT/RT, driving genetic counseling and
surveillance — appears only in a `SMARCB1` gene note and in two unused
deep-research reference stubs. No link to the sibling `Rhabdoid_Tumor` entry for
synchronous/metachronous renal disease.

---

## 4. Claim–evidence mismatches found by reading snippets against their claims

These are cases where a real, correctly-quoted source does not support the
statement it is attached to.

**Frequency bands contradicted by their own cited numbers:**

- `Alveolar_Rhabdomyosarcoma` — Metastatic Disease is `FREQUENT` (30-79%); the
  cited snippet reads "Seventeen (**13.3%**) patients had metastatic disease at
  diagnosis". That is the `OCCASIONAL` band.
- `Ewing_Sarcoma` — Metastatic Disease is `FREQUENT`, supported by three snippets
  that all report **survival in** metastatic disease ("five-year survival rate to
  20% to 30%", "10-30% 5-year event-free survival", "3-year EFS 37.4%"). None
  reports how often metastasis occurs. Survival percentages were read as
  frequency percentages.
- `Wilms_Tumor` — one snippet ("up to 35% of patients can present with either
  hematuria, hypertension, fever, or flank pain") is read as `FREQUENT` (30-79%)
  for hematuria and hypertension but `OCCASIONAL` (5-29%) for fever and flank
  pain. A ≤35% ceiling on the union of four symptoms cannot give 30-79% to two of
  them.

**Numbers with no numeric source:**

- `Wilms_Tumor` — CTNNB1 "~15%" and WTX/AMER1 "15-20%" both rest on the aggregate
  "WT1, β-catenin, and WTX **together** account for about one-third of Wilms
  tumor cases". IGF2 loss of imprinting "approximately 70%" rests on "closely
  associated with … **many** Wilms tumors".
- `Neuroblastoma` — MYCN "~20%" and ALK "8-10% / ~50%" rest on snippets
  containing no percentage at all.

**Evidence that argues the opposite of its explanation:**

- `Wilms_Tumor` `genetic[5]` — the explanation reads "Confirms frequency and
  prognostic relevance"; the snippet reads "Combined LOH 1p and 16q has **limited
  impact as a prognostic marker**".
- `Wilms_Tumor` `genetic[7]` asserts sensitization to ferroptosis via GPX4
  inhibition; the cited snippet mentions neither ferroptosis nor GPX4.

**Model-system evidence carrying human clinical claims:**

- `Neuroblastoma` — PMID:41560679 (human iPSC-derived neural crest cells
  transplanted into immunodeficient mice; the abstract calls it "an *in vitro*
  model") is the sole support for five claims, including MYCN's ~20% frequency,
  its status as "the strongest independent adverse prognostic factor", and
  1p/11q/17q risk stratification. For that last one the snippet reports **NF1 loss
  and 17q gain acquired in the cell model** — it says nothing about 1p, 11q, or
  prognosis. Two of the five carry no `evidence_source`, so they default to
  `HUMAN_CLINICAL` for a cell-culture paper.

**Unusable snippets in `Ewing_Sarcoma`:** a large share of snippets are clipped
mid-clause — `"It is associated in 85% of cases with the"`, `"recruited by the
EWS-FLI1 fusion protein to tumor-specific enhancers and"`, `"had longer alleles
(>135"`, `"depletion promoted a pro-metastatic phenotype"` (no subject named).
I checked several against the source abstracts: **the underlying science is
correct** — this is a quoting defect, not fabrication. But a reader cannot
confirm support without re-fetching the paper, which is what the snippet exists
to prevent.

---

## 5. What is genuinely well done

- **`Hepatoblastoma`** has the best mechanism graph: CTNNB1 → β-catenin/YAP1
  coactivation → fetal hepatic progenitor state → oncofetal program → NFE2L2
  stress adaptation, with the C2 molecular-risk signature and the low-AFP /
  SMARCB1-rhabdoid diagnostic boundary handled explicitly. It also splits a
  single paper's evidence into human, mouse, and in-vitro items according to
  which experiment supports which claim — the correct reading of
  `evidence_source`.
- **`Acute_Lymphoblastic_Leukemia`** is the most epistemically careful entry in
  the KB. Nodes scope their own claims ("does not generalize kinase dependence to
  every B-ALL subtype"), indirect causal edges are marked `PARTIAL`, and
  percentages are deliberately left inside quotations rather than promoted to
  fields — the exact discipline whose absence causes the §4 errors elsewhere.
- **`Ewing_Sarcoma`** has the deepest mechanistic content in the KB — EWS-FLI1
  dosage-sensitive hubs, GGAA microsatellite enhancer creation, germline repeat
  architecture as a susceptibility modifier, ETV6 counter-regulation, NuRD/CHD4
  repression, DHX9/SLFN11 replication-fork biology, STAG2 modification. This is
  research-grade curation; the defects are at the edges (fusion diversity,
  snippet quoting), not the core.
- **`Alveolar_Rhabdomyosarcoma`** models drug mechanisms properly, with
  `target_mechanisms` linking each agent to the node it acts on, plus
  `discussions` carrying open questions and proposed experiments.

---

## 6. Suggested priority

1. Fix the WHO 2021 medulloblastoma classification (§1.1) and its cell-type
   binding (§1.4)
2. Fix Stage 4S (§1.2) and familial ALK (§1.3) in `Neuroblastoma`
3. Give `Osteosarcoma` a histopathology block, notably percent-necrosis response
   grading (§3.1)
4. Resolve the Wilms TP53 self-contradiction (§1.6) and untangle the subtype axes
   (§2.1)
5. Add the two-hit exceptions to `Retinoblastoma` (§3.3) and telomere
   maintenance / ATRX / TERT to `Neuroblastoma` (§3.2)
6. Correct the three frequency bands contradicted by their own evidence (§4)
7. Re-quote the clipped `Ewing_Sarcoma` snippets at sentence boundaries (§4)

## Method

Every entry was read in full and assessed against current pediatric-oncology
knowledge (WHO CNS5 2021, WHO soft tissue 2020, INSS/INRG staging, COG and SIOP
protocols). Each evidence item was read together with the claim it is attached
to. Cached abstracts were consulted where a snippet's meaning was unclear. No KB
files were modified.
