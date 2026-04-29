# Clear Cell Ovarian Carcinoma Deep Research Notes

## Modeling choices applied from issue #1198

- The dismech page is the mechanism-graph unit for OCCC, not a page for every ontology subclass.
- The disease anchor is MONDO-first: `MONDO:0000548` (`ovarian clear cell cancer`).
- I treated `MONDO:0006045` (`ovarian clear cell adenocarcinoma`) as a close ontology neighbor rather than creating a second disorder page.
- I used NCIT where it materially improves oncology specificity:
  - `NCIT:C40078` for the adenocarcinoma morphology
- I evaluated NCIT regimen terms for first-line therapy, but the repo's current
  `RegimenTerm` validator closure rejects both `NCIT:C63402` (`Carboplatin/Paclitaxel
  Regimen`) and `NCIT:C63522` (`Regimen Used to Treat Malignant Ovarian Neoplasm`), so
  the validated YAML retains the MAXO chemotherapy action and records the NCIT regimen
  detail in research notes.
- I did not create separate disease files for advanced, recurrent, metastatic, or histology-adjacent NCIT subclasses because they do not represent a distinct causal program for this slice.

## Disease identity and ontology grounding

- MONDO disease anchor: `MONDO:0000548` `ovarian clear cell cancer`
- Close MONDO neighbor: `MONDO:0006045` `ovarian clear cell adenocarcinoma`
- NCIT morphology: `NCIT:C40078` `Ovarian Clear Cell Adenocarcinoma`
- NCIT regimen candidates evaluated: `NCIT:C63402` `Carboplatin/Paclitaxel Regimen`,
  `NCIT:C63522` `Regimen Used to Treat Malignant Ovarian Neoplasm`

## Mechanistic synthesis used in the YAML curation

### 1. Endometriosis-associated precursor context

- PMID:22976498
- Evidence source: `HUMAN_CLINICAL`
- Quote:
  > All of the 31 informative cases showed loss of ARID1A immunoreactivity in the carcinoma and in the endometriotic cyst epithelium in direct continuity with the carcinoma but not in the cyst epithelium that was not adjacent to the tumor.
- Curation implication:
  OCCC is modeled as an endometriosis-associated epithelial ovarian malignancy with a precursor field in contiguous endometriotic cyst epithelium.

### 2. Early ARID1A loss and chromatin remodeling failure

- PMID:22976498
- Evidence source: `HUMAN_CLINICAL`
- Quote:
  > Loss of ARID1A function as shown by loss of expression, presumably due to mutations, is an early molecular event in the development of most ovarian clear cell and endometrioid carcinomas arising in endometriomas.
- PMID:39543535
- Evidence source: `HUMAN_CLINICAL`
- Quote:
  > On analyzing 102 OCCC samples, ARID1A (67%) and PIK3CA (49%) emerged as the most frequently mutated driver genes.
- Curation implication:
  ARID1A loss is represented as an atomic pathophysiology node linked to abnormal chromatin remodeling rather than bundled into a generic "epigenetic dysregulation" block.

### 3. PI3K pathway activation cooperates with ARID1A loss

- PMID:25625625
- Evidence source: `MODEL_ORGANISM`
- Quote:
  > We find that ARID1A inactivation is not sufficient for tumour formation, but requires concurrent activation of the phosphoinositide 3-kinase catalytic subunit, PIK3CA.
- PMID:39543535
- Evidence source: `HUMAN_CLINICAL`
- Quote:
  > Reconstruction of clonal evolution revealed that early genetic events likely driving tumorigenesis included mutations in the ARID1A, PIK3CA, TERT, KRAS, and TP53 genes.
- Curation implication:
  PI3K activation is a separate node downstream of ARID1A loss, grounded to `GO:0043491`.

### 4. IL-6 inflammatory signaling is a mechanistic convergence point

- PMID:25625625
- Evidence source: `MODEL_ORGANISM`
- Quote:
  > Cross-species gene expression comparisons support a role for IL-6 inflammatory cytokine signalling in OCCC pathogenesis. We further show that ARID1A and PIK3CA mutations cooperate to promote tumour growth through sustained IL-6 overproduction.
- PMID:26238017
- Evidence source: `HUMAN_CLINICAL`
- Quote:
  > Patients with advanced OCCC had the highest 2-year cumulative VTE rates ... and the highest median levels of IL-6.
- Curation implication:
  I split IL-6 signaling into its own atomic node and linked it downstream to the thrombosis biology rather than hiding it inside a broader "inflammation" label.

### 5. HNF1B-driven glycolytic and antioxidant rewiring

- PMID:26318292
- Evidence source: `IN_VITRO`
- Quote:
  > HNF1β drastically alters intracellular metabolism, especially in direction to enhance aerobic glycolysis, so called the "Warburg effect".
- PMID:26318292
- Evidence source: `IN_VITRO`
- Quote:
  > Augmented cell survival was based on the reduced ROS activity derived from metabolic alteration such as shift from oxidative phosphorylation to glycolysis and increased intracellular anti-oxidant, glutathione (GSH).
- Curation implication:
  I separated glycolytic rewiring from glutathione/oxidative-stress buffering so the graph keeps the metabolic nodes atomic.

### 6. Intrinsic carboplatin resistance

- PMID:26520442
- Evidence source: `IN_VITRO`
- Quote:
  > ovarian clear cell carcinoma (OCCC) is intrinsically resistant.
- PMID:26520442
- Evidence source: `IN_VITRO`
- Quote:
  > ES2 cells are more resistant to carboplatin than OVCAR3 and the abrogation of GSH production by BSO sensitizes ES2 to carboplatin.
- PMID:26404183
- Evidence source: `HUMAN_CLINICAL`
- Quote:
  > Women with advanced OCCC have poor survival and are often chemotherapy resistant/refractory.
- Curation implication:
  Chemoresistance is represented as its own disease mechanism node and connected to glutathione metabolism rather than treated only as a treatment failure note.

### 7. OCCC-associated hypercoagulability

- PMID:24041880
- Evidence source: `HUMAN_CLINICAL`
- Quote:
  > Among 74 patients with OCCC, VTE was diagnosed in 11 (15%) during primary treatment and 7 (9%) at time of cancer recurrence.
- PMID:24041880
- Evidence source: `HUMAN_CLINICAL`
- Quote:
  > This increased risk is not attributable to VTE-related mortality and raises the possibility that a paracrine circuit involving thrombosis might contribute to a more aggressive tumor biology.
- PMID:37104696
- Evidence source: `HUMAN_CLINICAL`
- Quote:
  > The pooled prevalence of VTE among OCCC patients was 21.32% (95%CI=(17.38-25.87)).
- Curation implication:
  Thrombosis is modeled as part of disease biology with an atomic coagulation node and an HPO phenotype, not as unrelated supportive-care noise.

## Histopathology and phenotype evidence

### Histopathology

- PMID:2469661
- Evidence source: `HUMAN_CLINICAL`
- Quote:
  > Microscopically, three architectural patterns (papillary, tubulocystic, and solid) and four cell types (clear, hobnail, eosinophilic, and flattened) were seen.
- Use in curation:
  Grounds the NCIT morphology node `NCIT:C40078`.

### Stage distribution and clinical phenotype

- PMID:26404183
- Evidence source: `HUMAN_CLINICAL`
- Quote:
  > OCCC often presents in early stage.
- Use in curation:
  Supports the disease summary and the choice to treat stage as a flat clinical axis rather than a separate disease page.

## Treatment evidence incorporated

- PMID:20169667
- Evidence source: `HUMAN_CLINICAL`
- Quote:
  > Paclitaxel plus carboplatin (TC) is generally considered to be the "gold standard" regimen for treatment of epithelial ovarian carcinomas.
- PMID:20169667
- Evidence source: `HUMAN_CLINICAL`
- Quote:
  > Progression-free survival (PFS) showed no significant difference between the 2 treatment groups.
- Curation implication:
  The YAML uses the validated MAXO chemotherapy action, while the research note records
  the blocked NCIT regimen candidates and still captures that standard
  carboplatin/paclitaxel-based therapy remains an imperfect solution for OCCC.

## Additional high-value human genomic evidence retained in notes

- PMID:28611940
- Evidence source: `HUMAN_CLINICAL`
- Quote:
  > Gene expression analyses revealed a distinct OCCC profile compared to other histological subtypes.
- PMID:28611940
- Evidence source: `HUMAN_CLINICAL`
- Quote:
  > Genes involved in chromatin remodeling, including ARID1A, SPOP, and KMT2D were frequently mutated across OCCC tumors.
- Use in curation:
  These findings informed the summary and reinforced the choice to keep chromatin-remodeling defects central to the mechanism graph.
