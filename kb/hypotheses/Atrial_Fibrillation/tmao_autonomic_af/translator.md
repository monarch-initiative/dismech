---
provider: translator
model: ncats-translator-ars
cached: false
start_time: '2026-08-02T22:01:10.017245+00:00'
end_time: '2026-08-02T22:01:42.426802+00:00'
duration_seconds: 32.41
citation_count: 212
template_variables:
  disease_name: Atrial Fibrillation
  hypothesis_group_id: tmao_autonomic_af
  hypothesis_label: Gut microbial TMAO promotes AF via M2 muscarinic receptor autonomic
    dysfunction
  hypothesis_status: EMERGING
provider_config:
  ars_url: https://ars-prod.transltr.io
  ars_pk: 0eac7f2c-b0a7-4bc0-9acd-0e07620e308c
  merged_pk: 217d7c32-fa4c-45cf-9aae-dbeec4dd54c3
  query_graph:
    nodes:
      chem:
        ids:
        - CHEBI:15724
        categories:
        - biolink:ChemicalEntity
      mid:
        categories:
        - biolink:Gene
      disease:
        ids:
        - MONDO:0004981
        categories:
        - biolink:Disease
    edges:
      e1:
        subject: chem
        object: mid
      e2:
        subject: mid
        object: disease
---

# Translator mechanism paths: trimethylamine N-oxide -> atrial fibrillation

- Drug: `CHEBI:15724` (trimethylamine N-oxide)
- Disease: `MONDO:0004981` (atrial fibrillation)
- Intermediate node type: `gene`
- dismech entry: `kb/disorders/Atrial_Fibrillation.yaml`
- Entry does not yet curate this drug.
- ARS pk: `0eac7f2c-b0a7-4bc0-9acd-0e07620e308c`
- Translator UI: https://ui.transltr.io/main/results?q=0eac7f2c-b0a7-4bc0-9acd-0e07620e308c
- Generated: 2026-08-02T22:01:42.426802+00:00
- Paths: 20

> These paths are **machine-generated leads**, not curated mechanism. Each hop is a single knowledge-provider assertion — text-mined co-occurrence (`semmeddb`) sits beside curated pharmacology (`drugcentral`, `dgidb`) with no distinction in the ranking. A path is a hypothesis to check against primary literature, and every PMID below still has to go through `just fetch-reference` + `just validate-references` before it can support anything in an entry.

> :warning: **Entity mismatch.** The knowledge graph labels `CHEBI:15724` as **L-asparagine**, which resolves to `CHEBI:17261` — a different entity from the one queried (`CHEBI:15724`). Answers for this node may mix two chemicals' assertions; check the publications on every edge before using any of it.

| # | Intermediate | In entry? | Score | Path | Sources |
| - | ------------ | --------- | ----- | ---- | ------- |
| 1 | TNF (`NCBIGene:7124`) | — | 0.67 | L-asparagine --affects--> TNF | TNF --related_to--> atrial fibrillation | agrkb, semmeddb, text-mining-provider-targeted |
| 2 | CD36 (`NCBIGene:948`) | — | 0.67 | L-asparagine --affects--> CD36 | CD36 --gene_associated_with_condition--> atrial fibrillation | diseases, text-mining-provider-targeted |
| 3 | IL6 (`NCBIGene:3569`) | — | 0.66 | L-asparagine --affects--> IL6 | IL6 --gene_associated_with_condition--> atrial fibrillation | disgenet, text-mining-provider-targeted |
| 4 | TGFB1 (`NCBIGene:7040`) | — | 0.66 | L-asparagine --affects--> TGFB1 | TGFB1 --related_to--> atrial fibrillation | semmeddb, text-mining-provider-targeted |
| 5 | APP (`NCBIGene:351`) | — | 0.66 | L-asparagine --affects--> APP | APP --gene_associated_with_condition--> atrial fibrillation | diseases, text-mining-provider-targeted |
| 6 | ALB (`NCBIGene:213`) | — | 0.65 | L-asparagine --affects--> ALB | ALB --contributes_to--> atrial fibrillation | text-mining-provider-targeted |
| 7 | NLRP3 (`NCBIGene:114548`) | — | 0.65 | L-asparagine --affects--> NLRP3 | NLRP3 --gene_associated_with_condition--> atrial fibrillation | diseases, text-mining-provider-targeted |
| 8 | SOD1 (`NCBIGene:6647`) | — | 0.65 | L-asparagine --affects--> SOD1 | SOD1 --biomarker_for--> atrial fibrillation | agrkb, text-mining-provider-targeted |
| 9 | SCARB1 (`NCBIGene:949`) | — | 0.64 | L-asparagine --affects--> SCARB1 | SCARB1 --gene_associated_with_condition--> atrial fibrillation | diseases, text-mining-provider-targeted |
| 10 | SIRT1 (`NCBIGene:23411`) | — | 0.64 | L-asparagine --affects--> SIRT1 | SIRT1 --gene_associated_with_condition--> Paroxysmal atrial fibrillation | disgenet, genetics-data-provider, text-mining-provider-targeted |
| 11 | IL1B (`NCBIGene:3553`) | — | 0.64 | L-asparagine --affects--> IL1B | IL1B --gene_associated_with_condition--> atrial fibrillation | diseases, text-mining-provider-targeted |
| 12 | TLR4 (`NCBIGene:7099`) | — | 0.63 | L-asparagine --affects--> TLR4 | TLR4 --gene_associated_with_condition--> atrial fibrillation | diseases, text-mining-provider-targeted |
| 13 | CD69 (`NCBIGene:969`) | — | 0.62 | CD69 --interacts_with--> L-asparagine | CD69 --affects--> atrial fibrillation | semmeddb |
| 14 | MTOR (`NCBIGene:2475`) | — | 0.62 | L-asparagine --affects--> MTOR | MTOR --gene_associated_with_condition--> atrial fibrillation | diseases, text-mining-provider-targeted |
| 15 | ABCA1 (`NCBIGene:19`) | — | 0.61 | L-asparagine --affects--> ABCA1 | ABCA1 --gene_associated_with_condition--> atrial fibrillation | diseases, text-mining-provider-targeted |
| 16 | IL18 (`NCBIGene:3606`) | — | 0.61 | L-asparagine --affects--> IL18 | IL18 --gene_associated_with_condition--> atrial fibrillation | diseases, text-mining-provider-targeted |
| 17 | SMAD3 (`NCBIGene:4088`) | — | 0.61 | L-asparagine --affects--> SMAD3 | SMAD3 --has_phenotype--> atrial fibrillation | hpo-annotations, text-mining-provider-targeted |
| 18 | APOE (`NCBIGene:348`) | — | 0.60 | L-asparagine --affects--> APOE | APOE --gene_associated_with_condition--> atrial fibrillation | diseases, text-mining-provider-targeted |
| 19 | AGT (`NCBIGene:183`) | — | 0.60 | L-asparagine --affects--> AGT | AGT --gene_associated_with_condition--> atrial fibrillation | agrkb, text-mining-provider-targeted |
| 20 | CASP1 (`NCBIGene:834`) | — | 0.60 | L-asparagine --affects--> CASP1 | CASP1 --gene_associated_with_condition--> atrial fibrillation | diseases, text-mining-provider-targeted |

## Path detail

### 1. via TNF (`NCBIGene:7124`) — NEW
- Translator score: 0.670
- L-asparagine --affects--> TNF  
  - asserted by: text-mining-provider-targeted
- TNF --related_to--> atrial fibrillation  
  - asserted by: semmeddb  
  - publications: `PMID:18846342`, `PMID:22001292`, `PMID:22852002`, `PMID:24046510`, `PMID:24095158`, `PMID:25696948`
- Verify first: `just fetch-reference PMID:18846342`

### 2. via CD36 (`NCBIGene:948`) — NEW
- Translator score: 0.667
- L-asparagine --affects--> CD36  
  - asserted by: text-mining-provider-targeted  
  - publications: `PMID:29136772`
- CD36 --gene_associated_with_condition--> atrial fibrillation  
  - asserted by: diseases  
  - publications: `PMID:33195472`, `PMID:37495826`, `PMID:32808366`, `PMID:35739495`, `PMID:22364136`, `PMID:29097705`, `PMID:36441349`, `PMID:36982815`
- Verify first: `just fetch-reference PMID:29136772`

### 3. via IL6 (`NCBIGene:3569`) — NEW
- Translator score: 0.663
- L-asparagine --affects--> IL6  
  - asserted by: text-mining-provider-targeted  
  - publications: `PMID:34788763`
- IL6 --gene_associated_with_condition--> atrial fibrillation  
  - asserted by: disgenet  
  - publications: `PMID:18523031`
- Verify first: `just fetch-reference PMID:34788763`

### 4. via TGFB1 (`NCBIGene:7040`) — NEW
- Translator score: 0.660
- L-asparagine --affects--> TGFB1  
  - asserted by: text-mining-provider-targeted
- TGFB1 --related_to--> atrial fibrillation  
  - asserted by: semmeddb  
  - publications: `PMID:17689021`, `PMID:18194448`, `PMID:18322650`, `PMID:20235205`, `PMID:21069358`, `PMID:25402477`, `PMID:32516780`, `PMID:33000676`
- Verify first: `just fetch-reference PMID:17689021`

### 5. via APP (`NCBIGene:351`) — NEW
- Translator score: 0.656
- L-asparagine --affects--> APP  
  - asserted by: text-mining-provider-targeted
- APP --gene_associated_with_condition--> atrial fibrillation  
  - asserted by: diseases  
  - publications: `PMID:33824766`, `PMID:32395893`, `PMID:33584340`, `PMID:27165517`, `PMID:37435554`, `PMID:29464022`, `PMID:32827351`, `PMID:33411695`
- Verify first: `just fetch-reference PMID:33824766`

### 6. via ALB (`NCBIGene:213`) — NEW
- Translator score: 0.653
- L-asparagine --affects--> ALB  
  - asserted by: text-mining-provider-targeted
- ALB --contributes_to--> atrial fibrillation  
  - asserted by: text-mining-provider-targeted

### 7. via NLRP3 (`NCBIGene:114548`) — NEW
- Translator score: 0.646
- L-asparagine --affects--> NLRP3  
  - asserted by: text-mining-provider-targeted
- NLRP3 --gene_associated_with_condition--> atrial fibrillation  
  - asserted by: diseases  
  - publications: `PMID:37113690`, `PMID:27993379`, `PMID:36090853`, `PMID:31920933`, `PMID:35865524`, `PMID:33544152`, `PMID:31295805`, `PMID:34680365`
- Verify first: `just fetch-reference PMID:37113690`

### 8. via SOD1 (`NCBIGene:6647`) — NEW
- Translator score: 0.645
- L-asparagine --affects--> SOD1  
  - asserted by: text-mining-provider-targeted
- SOD1 --biomarker_for--> atrial fibrillation  
  - asserted by: agrkb

### 9. via SCARB1 (`NCBIGene:949`) — NEW
- Translator score: 0.639
- L-asparagine --affects--> SCARB1  
  - asserted by: text-mining-provider-targeted  
  - publications: `PMID:29136772`
- SCARB1 --gene_associated_with_condition--> atrial fibrillation  
  - asserted by: diseases  
  - publications: `PMID:33195472`, `PMID:37495826`, `PMID:32808366`, `PMID:35739495`, `PMID:22364136`, `PMID:25949827`, `PMID:35330552`, `PMID:36441349`
- Verify first: `just fetch-reference PMID:29136772`

### 10. via SIRT1 (`NCBIGene:23411`) — NEW
- Translator score: 0.638
- L-asparagine --affects--> SIRT1  
  - asserted by: text-mining-provider-targeted  
  - publications: `PMID:29325896`
- SIRT1 --gene_associated_with_condition--> Paroxysmal atrial fibrillation  
  - asserted by: disgenet  
  - publications: `PMID:29892015`
- Verify first: `just fetch-reference PMID:29325896`

### 11. via IL1B (`NCBIGene:3553`) — NEW
- Translator score: 0.636
- L-asparagine --affects--> IL1B  
  - asserted by: text-mining-provider-targeted
- IL1B --gene_associated_with_condition--> atrial fibrillation  
  - asserted by: diseases  
  - publications: `PMID:34512975`, `PMID:30858628`, `PMID:34314823`, `PMID:29982222`, `PMID:27678347`, `PMID:32808366`, `PMID:30354202`, `PMID:33204097`
- Verify first: `just fetch-reference PMID:34512975`

### 12. via TLR4 (`NCBIGene:7099`) — NEW
- Translator score: 0.633
- L-asparagine --affects--> TLR4  
  - asserted by: text-mining-provider-targeted
- TLR4 --gene_associated_with_condition--> atrial fibrillation  
  - asserted by: diseases  
  - publications: `PMID:37137812`, `PMID:33584340`, `PMID:32808366`, `PMID:32691301`, `PMID:33544152`, `PMID:35739495`, `PMID:35788564`, `PMID:31295805`
- Verify first: `just fetch-reference PMID:37137812`

### 13. via CD69 (`NCBIGene:969`) — NEW
- Translator score: 0.622
- CD69 --interacts_with--> L-asparagine  
  - asserted by: semmeddb  
  - publications: `PMID:32572979`, `PMID:34681805`, `PMID:35871952`, `PMID:36012119`, `PMID:36888764`
- CD69 --affects--> atrial fibrillation  
  - asserted by: semmeddb  
  - publications: `PMID:32079431`, `PMID:32465646`, `PMID:32705232`, `PMID:33092711`, `PMID:34308873`, `PMID:34807977`, `PMID:37893526`, `PMID:37979794`
- Verify first: `just fetch-reference PMID:32572979`

### 14. via MTOR (`NCBIGene:2475`) — NEW
- Translator score: 0.621
- L-asparagine --affects--> MTOR  
  - asserted by: text-mining-provider-targeted
- MTOR --gene_associated_with_condition--> atrial fibrillation  
  - asserted by: diseases  
  - publications: `PMID:34334080`, `PMID:31295805`, `PMID:29984246`, `PMID:37623876`, `PMID:34809830`, `PMID:31587779`, `PMID:33379359`, `PMID:37692846`
- Verify first: `just fetch-reference PMID:34334080`

### 15. via ABCA1 (`NCBIGene:19`) — NEW
- Translator score: 0.612
- L-asparagine --affects--> ABCA1  
  - asserted by: text-mining-provider-targeted
- ABCA1 --gene_associated_with_condition--> atrial fibrillation  
  - asserted by: diseases  
  - publications: `PMID:25368670`, `PMID:31811572`, `PMID:25404125`, `PMID:34765025`, `PMID:26425994`, `PMID:32821437`, `PMID:26301254`, `PMID:36580204`
- Verify first: `just fetch-reference PMID:25368670`

### 16. via IL18 (`NCBIGene:3606`) — NEW
- Translator score: 0.609
- L-asparagine --affects--> IL18  
  - asserted by: text-mining-provider-targeted  
  - publications: `PMID:34788763`
- IL18 --gene_associated_with_condition--> atrial fibrillation  
  - asserted by: diseases  
  - publications: `PMID:34512975`, `PMID:35391945`, `PMID:32450165`, `PMID:32808366`, `PMID:30354202`, `PMID:35893226`, `PMID:36610670`, `PMID:35747748`
- Verify first: `just fetch-reference PMID:34788763`

### 17. via SMAD3 (`NCBIGene:4088`) — NEW
- Translator score: 0.608
- L-asparagine --affects--> SMAD3  
  - asserted by: text-mining-provider-targeted
- SMAD3 --has_phenotype--> atrial fibrillation  
  - asserted by: hpo-annotations  
  - publications: `PMID:29392890`, `PMID:22167769`
- Verify first: `just fetch-reference PMID:29392890`

### 18. via APOE (`NCBIGene:348`) — NEW
- Translator score: 0.605
- L-asparagine --affects--> APOE  
  - asserted by: text-mining-provider-targeted
- APOE --gene_associated_with_condition--> atrial fibrillation  
  - asserted by: diseases  
  - publications: `PMID:33403740`, `PMID:37805670`, `PMID:32808366`, `PMID:19663669`, `PMID:25671766`, `PMID:35258387`, `PMID:34204735`, `PMID:26876501`
- Verify first: `just fetch-reference PMID:33403740`

### 19. via AGT (`NCBIGene:183`) — NEW
- Translator score: 0.602
- L-asparagine --affects--> AGT  
  - asserted by: text-mining-provider-targeted
- AGT --gene_associated_with_condition--> atrial fibrillation  
  - asserted by: agrkb
- Verify first: `just fetch-reference PMID:7288818`

### 20. via CASP1 (`NCBIGene:834`) — NEW
- Translator score: 0.601
- L-asparagine --affects--> CASP1  
  - asserted by: text-mining-provider-targeted
- CASP1 --gene_associated_with_condition--> atrial fibrillation  
  - asserted by: diseases  
  - publications: `PMID:28300845`, `PMID:36610670`, `PMID:36071720`, `PMID:36600995`, `PMID:36361791`, `PMID:37762839`, `PMID:32808940`, `PMID:36003518`
- Verify first: `just fetch-reference PMID:28300845`
