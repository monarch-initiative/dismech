# Atypical Teratoid/Rhabdoid Tumor Deep Research

## Scope

This note supports curation of a disease-level dismech entry for **Atypical Teratoid/Rhabdoid Tumor (AT/RT)**.

Per the cancer-modeling guidance from issue `#1198`, AT/RT is treated here as the **mechanism-graph unit**. The consensus molecular groups `TYR`, `SHH`, and `MYC` are modeled as **flat subtype facets** within one disease page rather than as separate dismech disorder pages. This is appropriate because the shared core causal program remains **SMARCB1/SMARCA4-driven SWI/SNF deficiency with epigenetic dysregulation**, even though subgroup enhancer programs and treatment sensitivities differ.

## Disease Identity And Ontology Grounding

- Primary disease term: `MONDO:0020560` `atypical teratoid rhabdoid tumor`
- Cancer morphology grounding used in the disease slice: `NCIT:C6906` `Atypical Teratoid/Rhabdoid Tumor`
- Parent concept used for knowledge-base organization: `rhabdoid tumor`

### Modeling choices influenced by issue #1198

- Keep **one AT/RT page**, not separate pages for `AT/RT-TYR`, `AT/RT-SHH`, and `AT/RT-MYC`.
- Use `has_subtypes` as a **flat molecular facet axis**.
- Keep the top-level disease identity **MONDO-first**.
- Add **NCIT grounding at the cancer morphology layer** rather than creating ontology-driven duplicate disorder pages.
- Do **not** treat subtype ontology grounding as implying a separate dismech page or a `Not Yet Curated` child.

## Evidence Inventory

### Disease identity, genetics, and subgrouping

- **PMID:41374972** (`OTHER`)
  - Quote: "Atypical Teratoid/Rhabdoid Tumor (AT/RT) is a highly aggressive neoplasm of the central nervous system (CNS), most commonly affecting infants and young children."
  - Quote: "AT/RT now encompasses CNS tumors characterized by SMARCB1 (INI-1) or SMARCA4 (BRG-1) alterations within the SWI/SNF chromatin-remodeling complex."
  - Quote: "The integration of immunohistochemical markers with advanced molecular diagnostics-including next-generation sequencing, DNA methylation profiling, and gene enrichment analyses-has facilitated robust tumor classification and the identification of three molecular subgroups: TYR, SHH, and MYC."
  - Use in curation: disease description; SMARCB1/SMARCA4-defining lesion; subgroup names.

- **PMID:26923874** (`HUMAN_CLINICAL`)
  - Quote: "Three distinct molecular subgroups of ATRTs, associated with differences in demographics, tumor location, and type of SMARCB1 alterations, were identified."
  - Quote: "Whole-genome bisulfite sequencing and H3K27Ac chromatin-immunoprecipitation sequencing of primary tumors, however, revealed clear differences, leading to the identification of subgroup-specific regulatory networks and potential therapeutic targets."
  - Use in curation: consensus subgroup axis; atomic epigenetic/regulatory-network mechanism node.

- **PMID:37020038** (`IN_VITRO`)
  - Quote: "They are genetically defined by alterations in the SWI/SNF chromatin remodeling complex members SMARCB1 or SMARCA4."
  - Quote: "We demonstrate that ATRT tumoroids retain subgroup-specific epigenetic and gene expression profiles."
  - Quote: "High throughput drug screens on our ATRT tumoroids revealed distinct drug sensitivities between and within ATRT-MYC and ATRT-SHH subgroups."
  - Use in curation: reinforces subgroup-specific epigenetic programs; supports research-only note that targeted vulnerabilities are subgroup-dependent.

### Histopathology and diagnostic markers

- **PMID:10437379** (`HUMAN_CLINICAL`)
  - Quote: "Histologically, atypical teratoid/rhabdoid tumor is defined as a polymorphous neoplasm often featuring rhabdoid, PNET, epithelial, and mesenchymal components."
  - Use in curation: disease-level histopathology entry grounded to NCIT morphology.

- **PMID:26769252** (`HUMAN_CLINICAL`)
  - Quote: "Atypical teratoid/rhabdoid tumors (AT/RT) are rare, aggressive, embryonal brain tumors that occur most frequently in very young children; they are characterized by rhabdoid cells and loss of INI1 protein nuclear expression."
  - Use in curation: INI1 loss as a key biochemical diagnostic marker; rhabdoid cells.

- **PMID:8683283** (`HUMAN_CLINICAL`)
  - Quote: "This tumor is typically misdiagnosed as a primitive neuroectodermal tumor (PNET) primarily because 70% of ATT/RhTs contain fields indistinguishable from classic PNETs."
  - Quote: "Abnormalities of chromosome 22 distinguish ATT/RhTs from PNETs, which typically display an i(17q) abnormality."
  - Use in curation: differential-diagnostic framing and historic pathology context; not all of this was moved into YAML to keep the entry focused.

### Clinical presentation

- **PMID:16048294** (`HUMAN_CLINICAL`)
  - Quote: "Signs and symptoms began, on average, a little more than 1 month before diagnosis and included the following: headache (36%), nausea and vomiting (46%), lethargy (18%), seizures (27%), cranial nerve findings (46%), ataxia (18%), long tract findings (18%), and hydrocephalus (46%)."
  - Use in curation: ontology-grounded phenotype entries for headache, vomiting, ataxia, and hydrocephalus.

- **PMID:33138347** (`HUMAN_CLINICAL`)
  - Quote: "Atypical teratoid/rhabdoid tumor (ATRT) is a highly aggressive malignancy with peak incidence in children aged less than 3 years."
  - Use in curation: infant-predominant epidemiology and age framing.

### Treatment evidence

- **PMID:32105509** (`HUMAN_CLINICAL`)
  - Quote: "After surgery, they received 2 courses of multiagent chemotherapy, followed by 3 courses of high-dose chemotherapy with peripheral blood stem cell rescue and involved-field radiation therapy."
  - Quote: "The ACNS0333 regimen dramatically improved survival compared with historical therapies for patients with AT/RT."
  - Use in curation: intensive chemotherapy plus focal radiation as validated modern backbone therapy.

- **PMID:33138347** (`HUMAN_CLINICAL`)
  - Quote: "Aggressive therapy including early adjuvant radiotherapy and HDCT could be considered to improve outcomes of ATRT in children under the age of 3 years."
  - Use in curation: early adjuvant radiotherapy and high-dose chemotherapy for infant/young-child disease.

- **PMID:25646852** (`HUMAN_CLINICAL`)
  - Quote: "Maximal safe resection followed by craniospinal irradiation and systemic chemotherapy with ICE or VAC regimen is a reasonable treatment strategy in this uncommon malignancy."
  - Use in curation: surgery, radiation, and systemic chemotherapy entries; emphasizes trimodality treatment.

- **PMID:34350327** (`HUMAN_CLINICAL`)
  - Quote: "Utilization of postoperative radiotherapy and the adoption of trimodal therapy are associated with significant improvement of median survival."
  - Use in curation: research-only support for trimodality treatment emphasis.

## Mechanism Modeling Notes

### Atomic mechanism choices kept in YAML

- `SMARCB1 or SMARCA4 Inactivation`
- `SWI/SNF Chromatin Remodeling Defect`
- `Subtype-Specific Enhancer Dysregulation`
- `Aggressive Tumor Cell Proliferation`

These nodes were kept separate so the graph does not collapse genomic loss, chromatin-remodeling failure, subgroup-specific regulatory wiring, and growth behavior into one bundled statement.

### Mechanism details kept in research only

- **PMID:37863903** mixes human imaging, mouse modeling, and single-cell transcriptomics. It is informative for research synthesis but less clean for a single-source `evidence_source` assignment inside YAML.
  - Quote: "Atypical teratoid rhabdoid tumors (ATRT) are divided into MYC, TYR and SHH subgroups, suggesting diverse lineages of origin."
  - Quote: "Trajectory analyses suggest that SMARCB1 loss induces a de-differentiation process mediated by repressors of the neuronal program such as REST, ID and the NOTCH pathway."
  - Curation decision: keep this paper in the research note to inform future refinement of subgroup-specific mechanism nodes without forcing mixed-source evidence into the current YAML.

## Candidate Ontology Terms Used In YAML

### Disease and morphology

- `MONDO:0020560` `atypical teratoid rhabdoid tumor`
- `NCIT:C6906` `Atypical Teratoid/Rhabdoid Tumor`

### Genes

- `hgnc:11103` `SMARCB1`
- `hgnc:11100` `SMARCA4`

### Mechanism terms

- `GO:0016514` `SWI/SNF complex`
- `GO:0006338` `chromatin remodeling`
- `GO:0010468` `regulation of gene expression`
- `GO:0008283` `cell population proliferation`

### Phenotype terms

- `HP:0002315` `Headache`
- `HP:0002013` `Vomiting`
- `HP:0001251` `Ataxia`
- `HP:0000238` `Hydrocephalus`

### Treatment terms

- `MAXO:0000004` `surgical procedure`
- `MAXO:0000647` `chemotherapy`
- `MAXO:0000014` `radiation therapy`

## Open Curation Judgments

- I did **not** split out `AT/RT-TYR`, `AT/RT-SHH`, or `AT/RT-MYC` into separate disorder files.
- I did **not** create a separate `SMARCA4-deficient AT/RT` page because the current disease-level graph is still unified around the same core SWI/SNF-deficient causal program.
- I used NCIT at the **disease morphology layer** (`NCIT:C6906`) because the current schema does not provide a separate top-level NCIT cancer-disease mapping slot alongside `disease_term`.
