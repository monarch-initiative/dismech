# Peripheral T-Cell Lymphoma Deep Research Notes

## Scope and modeling choice

This curation follows the cancer-entry guidance from dismech issue `#1198`.

- The dismech page is treated as the **mechanism-graph unit**, not as one page per ontology subclass.
- `Peripheral T-cell lymphoma` is modeled as a **family-level nodal/systemic PTCL entry** with flat subtype facets rather than separate dismech pages for each histologic entity.
- The subtype axis is intentionally flat and histology-focused:
  - `PTCL-NOS`
  - `TFH Angioimmunoblastic-Type`
  - `TFH Follicular-Type`
  - `TFH NOS`
  - `ALK-Positive ALCL`
  - `ALK-Negative ALCL`
- `disease_term` stays **MONDO-first**, but MONDO does not currently expose an exact family-level PTCL umbrella term. The entry therefore uses the closest MONDO family anchor, `MONDO:0015760` (`T-cell non-Hodgkin lymphoma`), and carries oncology-specific specificity through NCIT subtype-linked histopathology and regimen/procedure terms.
- NCIT is used preferentially where it is materially more specific for oncology:
  - disease/subtype histopathology anchors (`NCIT:C3468`, `C4340`, `C7528`, `C80375`, `C139011`, `C37195`, `C37196`)
  - regimen/procedure/treatment terms (`NCIT:C9549`, `C159558`, `C16039`, `C46089`)

## Disease identity and subtype structure

- `PMID:36010351`
  - "Peripheral T-cell lymphomas (PTCLs) are uncommon neoplasms derived from mature T cells or NK cells."
  - "According to their presentation, PTCLs can be divided into nodal, extranodal or cutaneous, and leukemic types."
  - "Nodal PTCLs include ALK-positive and ALK-negative anaplastic large cell lymphoma; nodal T-cell lymphoma with T follicular helper cell origin; and PTCL, not otherwise specified."
- `PMID:31562134`
  - "Peripheral T-cell lymphoma (PTCL) is a heterogeneous group of mature T-cell malignancies; approximately one-third of cases are designated as PTCL-not otherwise specified (PTCL-NOS)."
- `PMID:36793612`
  - "Three main subtypes of nodal TFH lymphomas have been described: 1) angioimmunoblastic-type, 2) follicular-type, and 3) not otherwise specified (NOS)."

## Key mechanistic branches used in the YAML

### 1. TFH-lineage epigenetic branch

- `PMID:36793612`
  - "These neoplasms feature a characteristic and similar, but not identical, mutational landscape with mutations in epigenetic modifiers (TET2, DNMT3A, IDH2), RHOA, and T-cell receptor signaling genes."
- `PMID:37841428`
  - "Mutations in the epigenetic regulator TET2 are among the most frequent mutations identified in PTCL, with the highest frequency in angioimmunoblastic T cell lymphomas and other nodal T follicular helper (TFH) lymphomas."

### 2. RHOA/VAV1 and TCR signaling branch

- `PMID:28832024`
  - "We found that binding of G17V RHOA to VAV1 augmented its adaptor function through phosphorylation of 174Tyr, resulting in acceleration of T-cell receptor (TCR) signaling."
  - "Enrichment of cytokine and chemokine-related pathways was also evident by the expression of G17V RHOA."

### 3. PTCL-NOS transcriptional-polarization branch

- `PMID:31562134`
  - "Using gene-expression profiling (GEP), we have previously defined 2 major molecular subtypes of PTCL-NOS, PTCL-GATA3 and PTCL-TBX21, which have distinct biological differences in oncogenic pathways and prognosis."
- `PMID:30782609`
  - "PTCL-GATA3 exhibited greater genomic complexity that was characterized by frequent loss or mutation of tumor suppressor genes targeting the CDKN2A /B-TP53 axis and PTEN-PI3K pathways. Co-occurring gains/amplifications of STAT3 and MYC occurred in PTCL-GATA3."
- `PMID:35639959`
  - "Genomewide methylation analysis of DNMT3A-mutant vs wild-type (WT) PTCL-TBX21 cases demonstrated hypomethylation in target genes regulating interferon-γ (IFN-γ), T-cell receptor signaling, and EOMES (eomesodermin), a master transcriptional regulator of cytotoxic effector cells."

### 4. Immune microenvironment branch

- `PMID:38813724`
  - "The PTCL TME contained a larger proportion of regulatory T cells and exhausted CD8+ T cells, with enriched expression of druggable immune checkpoints."

## Clinical phenotype and pathology points used

- `PMID:20702104`
  - "In the lymph node, PTCL-NOS shows paracortical or diffuse infiltrates with effacement of the normal architecture, with a broad cytological spectrum and a frequently observed inflammatory background."
  - "Patients often have B symptoms, generalized lymphadenopathy, bone marrow infiltration, and extranodal involvement, with high or high-intermediate IPI score in 50-70% of cases."
- `PMID:29302559`
  - "Patients can experience night sweats, fever, lymphadenopathy, weight loss, splenomegaly, and/or skin changes."
  - "Common laboratory tests reveal that patients have anemia, thrombocytosis, lymphocytosis, eosinophilia, hypergammaglobulinemia, or increased lactate dehydrogenase."

## Treatment evidence carried into the YAML

- `PMID:30914464`
  - "The median PFS was 48.2 months with BV+CHP versus 20.8 months with CHOP, resulting in a hazard ratio (HR) of 0.71 (95% confidence interval [CI]: 0.54-0.93)."
  - "The trial also demonstrated improvement in overall survival (HR 0.66; 95% CI: 0.46-0.95), complete response rate (68% vs. 56%), and overall response rate (83% vs. 72%) with BV+CHP."
  - "Improvement in progression-free and overall survival over cyclophosphamide, doxorubicin, vincristine, and prednisone chemotherapy, which has been the standard of care for decades, is unprecedented."
- `PMID:21245435`
  - "The response rate in 109 evaluable patients was 29% (32 of 109), including 12 complete responses (11%) and 20 partial responses (18%), with a median DoR of 10.1 months."
- `PMID:21355097`
  - "Complete responses were observed in 8 and partial responses in 9 of 45 patients, for an overall response rate of 38% (95% confidence interval 24%-53%)."
  - "The histone deacetylase inhibitor romidepsin has single agent clinical activity associated with durable responses in patients with relapsed PTCL."
- `PMID:20359581`
  - "Studies show that autologous transplant is feasible in relapsed and previously untreated patients, and efficacy is comparable to results in aggressive B-cell lymphomas."
  - "Allogeneic transplant may also have a role in relapsed PTCL, especially in the context of reduced-intensity conditioning, which has decreased nonrelapse mortality."

## Outcome and epidemiology anchors

- `PMID:21138864`
  - "Peripheral T-cell lymphomas (PTCL) constitute a group of heterogeneous diseases that are uncommon, representing, in Western countries, only approximately 10% of all non-Hodgkin lymphomas."
- `PMID:38532575`
  - "The overall response rate to first-line therapy was 68%, while 5- and 10-year overall survival estimates were 49% and 40% respectively."
  - "Most deaths occurred prior to 5 years, and for patients alive at 5 years, the chance of surviving to 10 years was 84%."

## Ontology terms selected

### Disease and subtype grounding

- Disease anchor: `MONDO:0015760` `T-cell non-Hodgkin lymphoma`
- PTCL-NOS: `MONDO:0004964`
- TFH angioimmunoblastic-type: `MONDO:0004977`
- TFH follicular-type: `MONDO:0958095`
- ALK-positive ALCL: `MONDO:0017602`
- ALK-negative ALCL: `MONDO:0017603`

### NCIT subtype and oncology anchors

- PTCL family: `NCIT:C3468` `Mature T-Cell and NK-Cell Non-Hodgkin Lymphoma`
- PTCL-NOS: `NCIT:C4340`
- TFH lymphoma, angioimmunoblastic-type: `NCIT:C7528`
- TFH lymphoma, follicular-type: `NCIT:C80375`
- TFH lymphoma, NOS: `NCIT:C139011`
- Systemic ALCL, ALK-positive: `NCIT:C37195`
- Systemic ALCL, ALK-negative: `NCIT:C37196`

### Core GO / CL / HP terms used

- `CL:0002038` `T follicular helper cell`
- `CL:0000815` `regulatory T cell`
- `CL:0011025` `exhausted T cell`
- `CL:0000794` `CD8-positive, alpha-beta cytotoxic T cell`
- `GO:0006325` `chromatin organization`
- `GO:0050852` `T cell receptor signaling pathway`
- `GO:0001819` `positive regulation of cytokine production`
- `GO:0045580` `regulation of T cell differentiation`
- `GO:0007259` `cell surface receptor signaling pathway via JAK-STAT`
- `GO:0050777` `negative regulation of immune response`
- `HP:0002716` `Lymphadenopathy`
- `HP:0001945` `Fever`
- `HP:0030166` `Night sweats`
- `HP:0001824` `Weight loss`
- `HP:0001744` `Splenomegaly`
- `HP:0001903` `Anemia`
