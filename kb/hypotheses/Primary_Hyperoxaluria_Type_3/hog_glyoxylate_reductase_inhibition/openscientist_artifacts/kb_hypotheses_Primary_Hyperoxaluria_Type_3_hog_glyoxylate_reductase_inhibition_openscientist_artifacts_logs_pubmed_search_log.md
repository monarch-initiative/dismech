# PubMed / NCBI E-utilities search & retrieval log
Hypothesis: hog_glyoxylate_reductase_inhibition (PH3)
Search date: 2026-10-15
Tooling: openscientist `search_pubmed` MCP tool + NCBI E-utilities (esearch/esummary/efetch)
and NCBI BioC PMC API, accessed from the sandbox via Python `requests` 2.34.2.

## A. openscientist search_pubmed queries
| # | Query | Usable results |
|---|-------|----------------|
| 1 | primary hyperoxaluria type 3 HOGA1 glyoxylate reductase inhibition 4-hydroxy-2-oxoglutarate | 1 (PMID 39582099) |
| 2 | HOGA1 mutations primary hyperoxaluria type 3 mechanism hydroxyproline | 0 |
| 3 | HOGA1 primary hyperoxaluria type 3 | 14 (incl. 40578401, 39040543, 39582099, 37318624, 34245816) |
| 4 | 4-hydroxy-2-oxoglutarate glyoxylate reductase inhibition | 3 (incl. 22771891) |
| 5 | hydroxyproline Primary Hyperoxaluria Type 3 mouse HOGA | 2 (26428388 seed, 39040543) |
| 6 | 2,4-dihydroxyglutarate biomarker primary hyperoxaluria type 3 urine | 0 |
| 7 | glyoxylate reductase GRHPR cytosol mitochondria oxalate hydroxyproline degradation compartment | 1 (39582099) |
| 8 | primary hyperoxaluria type III model perturbations glyoxylate metabolism compartmentalization cytosolic aldolase | 1 (22729392) |

## B. NCBI E-utilities (direct)
- efetch db=pubmed id=39040543,40578401,39582099,22771891 rettype=abstract -> HTTP 200, full abstracts retrieved.
- esearch "primary hyperoxaluria type 3 oxalate mechanism hydroxyproline glyoxylate" -> 39040543, 21998747.
- esearch "DHDPSL mutations primary hyperoxaluria type III Belostotsky" -> 22729392, 21896830, 20797690.
- efetch db=pubmed id=21998747 (HOGA structure) -> HTTP 200.
- efetch db=pubmed id=22729392,21896830,20797690 -> HTTP 200.

## C. NCBI BioC PMC full text (for kinetic parameters & concentrations)
- GET https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC3418427/unicode
  -> HTTP 200, ~49,675 chars parsed (Riedel 2012).
  Extracted verbatim:
  * "GR inhibition by HOG was tested by pre-incubating 3 nM GR with 0-10 mM HOG..."
  * "resulting in a Ki value of 1.8 +/- 0.9 mM for HOG."
  * "Parameters calculated from the global fit... Ki for HOG, 1.75 +/- 0.85 mM; KM for glyoxylate, 267 +/- 19 uM; kcat, 72.7 +/- 0.01 s-1."
  * "Given the concentration of HOG required for GR inhibition (~1 mM) and the putative physiological concentration of HOG (~10 uM based on the KM value for hHOGA for HOG), one would not expect HOG to inhibit GR under normal physiological conditions."
  * Table 2 (PH3): Urine 47.0+/-35.2 mg/24hr; Serum 0.89+/-0.39 uM; Liver 34.3+/-6.2 pmol/mg protein; non-PH3 groups < LOD (0.06 uM).

## D. Negative / absent-source checks (as of 2026-10-15)
- No dedicated human omics dataset (transcriptomic/metabolomic repository accession)
  specific to GRHPR activity in PH3 liver was located via PubMed queries above.
- No clinical trial of a GR-targeted or HOG-lowering agent in PH3 surfaced in the
  PubMed queries run here (ClinicalTrials.gov was NOT directly queried -> labeled UNVERIFIED).
- GenCC / ClinGen / ClinVar were NOT directly queried in this run (labeled UNVERIFIED).

## E. ClinicalTrials.gov API v2 (added Iteration 5, 2026-10-15)
- GET https://clinicaltrials.gov/api/v2/studies?query.cond=primary+hyperoxaluria+type+3&pageSize=50&countTotal=true
  -> HTTP 200; totalCount=22 (many false hits: oncology "PH III"/"PH3" phase labels).
- GET ...?query.cond=primary+hyperoxaluria&pageSize=50&countTotal=true -> HTTP 200; totalCount=55.
- PH3-relevant interventional studies (all target downstream LDH / siRNA, NOT GR or HOG):
  * NCT04555486  DCR-PHXC (nedosiran) in PH Type 3 — safety/PK/PD
  * NCT05001269  nedosiran, pediatric PH
  * NCT04042402  DCR-PHXC long-term extension
  * NCT06465472  stiripentol (LDH inhibitor) in primary hyperoxaluria
- PH3 natural-history / registries: NCT04542590, NCT02026388 (Rare Kidney Stone Biobank),
  NCT02780297 (ProRKS), NCT06065852 (Rare Kidney Disease Registry).
- RESULT: No registered trial/agent targets glyoxylate reductase restoration or HOG lowering.
  Trial-source gap previously 'UNVERIFIED' is now VERIFIED: PH3 trials exist, none test the GR edge.
- GenCC / ClinGen / ClinVar: still NOT queried this run -> remain UNVERIFIED.
