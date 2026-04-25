---
provider: manual_pubmed_review
model: n/a
cached: false
start_time: '2026-04-13T04:25:00Z'
end_time: '2026-04-13T05:23:29Z'
duration_seconds: 3509.0
citation_count: 22
notes: >
  Manual PubMed-grounded synthesis prepared during curation of dismech issue
  #1202. Cancer modeling follows the issue #1198 guidance: Hepatoblastoma is
  kept as one disease-level dismech mechanism graph; subtype schemes are flat
  facets; the disease anchor is MONDO-first; NCIT is used for cancer grounding
  where the schema supports disease, histopathology, biomarker, and regimen-like
  specificity.
---

## Question

Curate Hepatoblastoma as a disease-level dismech cancer entry with faceted
subtype modeling, ontology-grounded cancer terms, atomic pathophysiology nodes,
and exact PMID-backed evidence.

## Output

# Hepatoblastoma: Manual Curation Notes

## Modeling decisions used for the YAML

- The dismech entry was kept at the **Hepatoblastoma** disease-page level rather
  than splitting into separate files for pure fetal, embryonal, SCU, or
  predisposition-associated cases.
- Subtypes were modeled as flat facets rather than page-worthy child diseases:
  histology (`epithelial`, `mixed epithelial and mesenchymal`, `fetal`,
  `embryonal`, `SCU-component-positive`), molecular risk (`C2-signature`), and
  predisposition context (`Beckwith-Wiedemann spectrum`, `familial adenomatous
  polyposis`).
- MONDO remains the disease anchor (`MONDO:0018666 hepatoblastoma`). NCIT is
  used where the current schema supports oncology-grounded descriptors, chiefly
  disease-level histopathology and biomarkers.
- INI1-negative/SMARCB1-deficient small-cell liver tumors were treated as a
  boundary condition for hepatoblastoma curation rather than as a hepatoblastoma
  subtype with its own dismech page.

## Core disease mechanism

The shared disease program is dominated by **CTNNB1/WNT activation**. Clinical
and liquid-biopsy studies consistently identify CTNNB1 as the dominant recurrent
driver in sporadic hepatoblastoma (PMID:32881242; PMID:33125945). This sits
 upstream of a broader developmental cancer program rather than defining several
 separate dismech pages.

Hepatoblastoma also shows frequent **beta-catenin/YAP1 coactivation**. Human
tumor tissue demonstrates concurrent nuclear localization of beta-catenin and
YAP1 in most cases, and model systems show that combined activation is
tumorigenic whereas either pathway alone is insufficient for the same phenotype
(PMID:24837480; PMID:30794807). This justified splitting WNT activation and
YAP1 cooperation into separate but connected pathophysiology nodes.

The tumor preserves a **fetal hepatic progenitor state** rather than completing
 normal hepatocytic differentiation. Pretreatment molecular profiling supports
 clinically relevant subgroups defined by hepatic progenitor markers and
 metabolic programs (PMID:27775819). That developmental-arrest concept was
 modeled separately from the upstream CTNNB1/YAP1 driver nodes.

Aggressive cases show an **oncofetal stem-like program** and **NFE2L2-linked
stress adaptation**. High-risk tumors are enriched for LIN28B, HMGA2, SALL4,
AFP, and NFE2L2 activity, while the C2/NFE2L2-mutant context correlates with
non-fetal histology, vessel invasion, metastasis, and inferior survival
(PMID:27775819; PMID:33125945). Those were split into separate mechanistic nodes
to keep the graph atomic.

Experimental therapy papers also support a downstream **growth-support module**
in beta-catenin/YAP1-driven tumors. In vitro knockdown of either arm reduces
growth, and rapamycin reduces tumor burden in a Yap1/beta-catenin mouse model
(PMID:24837480; PMID:30863496). This was used to support a distinct
proliferation node rather than folding all growth effects into the upstream
signaling nodes.

## Subtype and histopathology notes

Histology remains a major facet axis. Reviews and clinicopathologic series
support broad separation into epithelial versus mixed epithelial-mesenchymal
 tumors, with fetal, embryonal, and SCU morphologies inside the epithelial axis
(PMID:33981680; PMID:19072985).

The key boundary update from the more recent literature is that **SCU does not
by itself define a separate aggressive hepatoblastoma disease program once
rhabdoid tumors are excluded**. Modern COG and CHIC analyses show that
INI1-negative/SMARCB1-deficient small-cell tumors should be treated as malignant
rhabdoid tumor, while SCU component-positive hepatoblastoma without rhabdoid
reclassification does not independently worsen outcome (PMID:34874751;
PMID:36672416; PMID:31835848). That directly affected the final YAML:

- SCU is modeled as a flat histology facet inside Hepatoblastoma.
- INI1-negative liver tumors are described as a classification boundary, not as
  a Hepatoblastoma child page.
- The disease-level histopathology grounding uses NCIT for `Hepatoblastoma` and
  `Embryonal Neoplasm`.

## Predisposition contexts

Two predisposition contexts are strong enough to warrant explicit subtype facets
without separate disease pages.

- **Beckwith-Wiedemann spectrum (BWSp)**: hepatoblastoma arises in the setting
  of 11p15 imprinting abnormalities and epigenotype mosaicism, with frequent
  convergence on CTNNB1 mutation in the tumor (PMID:37174013).
- **Familial adenomatous polyposis (FAP)**: APC mutation confers childhood
  hepatoblastoma risk and motivates infant surveillance in affected families
  (PMID:29719120; PMID:1329510).

These were modeled as `predisposition_context` subtypes instead of separate
dismech entries because the shared tumor mechanism still converges on the same
disease-level beta-catenin/oncofetal program.

## Phenotype and biomarker notes

The most stable disease-level presentation remains **painless abdominal mass**
with tumor-associated **hepatomegaly/abdominal enlargement**
(PMID:33981680; PMID:16458842).

**Alpha-fetoprotein (AFP)** is the core biomarker. Most tumors show elevated
serum AFP, which supports diagnosis and monitoring, while AFP below 100 ng/mL
marks a clinically important context that overlaps with SMARCB1-reclassified
rhabdoid tumors and failed conservative surgery (PMID:33981680;
PMID:16458842; PMID:18166449; PMID:17661341).

**CTNNB1 ctDNA** is an emerging molecular biomarker that tracks tumor burden,
residual disease, and response (PMID:32881242; PMID:38201440).

## Treatment notes

Current management is still organized around **cisplatin-based preoperative
chemotherapy**, **complete surgical resection when feasible**, and **liver
transplantation for unresectable liver-confined disease**
(PMID:28126357; PMID:25349947; PMID:16458842; PMID:12352881;
PMID:34441025; PMID:17661341).

Because the schema’s oncology-specific treatment support is split between MAXO
actions and NCIT regimen descriptors, the YAML keeps generic treatment actions
in MAXO and uses CHEBI agents for the specific cytotoxics. An NCIT regimen term
would only be preferable here if a stable hepatoblastoma-specific regimen term
were already available in the local ontology slice.

## Reference set used in curation

- PMID:1329510
- PMID:12352881
- PMID:16458842
- PMID:17661341
- PMID:18166449
- PMID:19072985
- PMID:24837480
- PMID:25349947
- PMID:27775819
- PMID:28126357
- PMID:29719120
- PMID:30794807
- PMID:30863496
- PMID:31835848
- PMID:32881242
- PMID:33125945
- PMID:33981680
- PMID:34441025
- PMID:34874751
- PMID:36672416
- PMID:37174013
- PMID:38201440
