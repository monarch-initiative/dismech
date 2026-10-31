# Database query log (Iteration 4, 2026-10-16)

All queries executed via Python `requests` in the OpenScientist sandbox.

## GenCC — gene-disease validity
- Source: https://search.thegencc.org/download/action/submissions-export-tsv
- Snapshot retrieved: 2026-10-16; total rows = 30,345; MYH7/MYH2 rows = 32
- Filter: gene_symbol in {MYH7, MYH2}
- Output: `data/gencc_myh7_myh2.csv`
- Key results (skeletal-myopathy relevant):
  - **MYH7-related skeletal myopathy**: ClinGen = **Definitive** (AD); Ambry/Labcorp = Strong; Orphanet = Supportive.
  - MYH7 myosin storage myopathy (AD & AR): Moderate–Strong.
  - **MYH2 "myopathy, proximal, and ophthalmoplegia"**: ClinGen = **Definitive (autosomal recessive)**, Moderate (AD); Ambry = Strong (Semidominant); Labcorp/LMM/PanelApp = Strong (AR and AD).
  - MYH2 hereditary inclusion-body-myopathy / ophthalmoplegia: Limited–Supportive (AD).
- Interpretation: both genes are bona fide Mendelian skeletal-myopathy entities with
  distinct dominant and recessive allelic series (relevant to subtype restriction).

## NCBI ClinVar — variant landscape (E-utilities esearch)
- Endpoint: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi (db=clinvar, retmode=json)
- Retrieved 2026-10-16:
  - term `MYH7[gene]` -> count = **6011**
  - term `MYH2[gene]` -> count = **1795**
- Note: counts are whole-gene (not LMM-restricted); not further stratified this run.

## ClinicalTrials.gov API v2 — SRX-modulator / myopathy trials
- Endpoint: https://clinicaltrials.gov/api/v2/studies (countTotal=true, format=json)
- Retrieved 2026-10-16:
  - `query.term="MYH2 myopathy"` -> totalCount = **0**
  - `query.term="mavacamten myopathy"` -> totalCount = **0**
  - `query.term="super-relaxed state myopathy"` -> totalCount = **0**
  - `query.term="MYH7 distal myopathy"` -> totalCount = **1** -> NCT04572893 "Exploratory Study of
    Danicamtiv in Patients With Primary Dilated Cardiomyopathy" = **NOT a skeletal myopathy / NOT an
    SRX stabilizer trial in the target disease** (false-positive text match).
- **Verified NULL**: no registered trial of an SRX stabilizer (e.g., mavacamten) in MYH2 or MYH7
  **skeletal** myopathy as of the search date. This converts the previously "unverified" trial gap
  into a checked source-level absence.

## Outcome labels
GenCC fetch: succeeded | ClinVar esearch: succeeded | ClinicalTrials.gov: succeeded (incl. verified null).
No silent fallback to literature was used for any failed query.
