---
provider: translator
model: ncats-translator-ars
cached: false
start_time: '2026-08-02T19:37:00.653881+00:00'
end_time: '2026-08-02T19:37:17.691070+00:00'
duration_seconds: 17.04
citation_count: 9
template_variables:
  disease_name: Gorlin Syndrome
  hypothesis_group_id: gli_bypass_resistance_model
  hypothesis_label: SMO-Inhibitor Resistance via Downstream GLI Bypass
  hypothesis_status: EMERGING
provider_config:
  ars_url: https://ars-prod.transltr.io
  ars_pk: 1db23126-7dc9-447f-ac03-efd0f1ed0693
  merged_pk: 6f545d12-6aba-4bb6-91ab-2216485d3a9e
  query_graph:
    nodes:
      chem:
        ids:
        - CHEBI:66903
        categories:
        - biolink:ChemicalEntity
      mid:
        categories:
        - biolink:Gene
      disease:
        ids:
        - MONDO:0007187
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

# Translator mechanism paths: Vismodegib -> nevoid basal cell carcinoma syndrome

- Drug: `CHEBI:66903` (Vismodegib)
- Disease: `MONDO:0007187` (nevoid basal cell carcinoma syndrome)
- Intermediate node type: `gene`
- dismech entry: `kb/disorders/Gorlin_Syndrome.yaml`
- Entry already curates this drug as: **vismodegib**
  - declared `target_mechanisms`: SMO Constitutive Activation (INHIBITS)
- ARS pk: `1db23126-7dc9-447f-ac03-efd0f1ed0693`
- Translator UI: https://ui.transltr.io/main/results?q=1db23126-7dc9-447f-ac03-efd0f1ed0693
- Generated: 2026-08-02T19:37:17.691070+00:00
- Paths: 3

> These paths are **machine-generated leads**, not curated mechanism. Each hop is a single knowledge-provider assertion — text-mined co-occurrence (`semmeddb`) sits beside curated pharmacology (`drugcentral`, `dgidb`) with no distinction in the ranking. A path is a hypothesis to check against primary literature, and every PMID below still has to go through `just fetch-reference` + `just validate-references` before it can support anything in an entry.

| # | Intermediate | In entry? | Score | Path | Sources |
| - | ------------ | --------- | ----- | ---- | ------- |
| 1 | SUFU (`NCBIGene:51684`) | genetic: SUFU | 1.00 | SUFU --affects--> Vismodegib | SUFU --gene_associated_with_condition--> nevoid basal cell carcinoma syndrome | ctd, genebass |
| 2 | PTCH2 (`NCBIGene:8643`) | genetic: PTCH2 | 0.56 | Vismodegib --affects--> PTCH2 | PTCH2 --related_to--> nevoid basal cell carcinoma syndrome | clingen, orphanet, service-provider-trapi |
| 3 | PTCH1 (`NCBIGene:5727`) | genetic: PTCH1 | 0.56 | Vismodegib --affects--> PTCH1 | PTCH1 --causes--> nevoid basal cell carcinoma syndrome | clingen, dgidb, orphanet |

## Path detail

### 1. via SUFU (`NCBIGene:51684`) — IN ENTRY
- Entry already models this as: **genetic: SUFU**
- Translator score: 1.000
- SUFU --affects--> Vismodegib  
  - asserted by: ctd
- SUFU --gene_associated_with_condition--> nevoid basal cell carcinoma syndrome  
  - asserted by: genebass  
  - publications: `PMID:19533801`, `PMID:22829011`, `PMID:25403219`, `PMID:29892665`, `PMID:29356994`, `PMID:31485359`, `PMID:12068298`, `PMID:16459298`
- Verify first: `just fetch-reference PMID:19533801`

### 2. via PTCH2 (`NCBIGene:8643`) — IN ENTRY
- Entry already models this as: **genetic: PTCH2**
- Translator score: 0.556
- Vismodegib --affects--> PTCH2  
  - asserted by: text-mining-provider-targeted
- PTCH2 --related_to--> nevoid basal cell carcinoma syndrome  
  - asserted by: service-provider-trapi

### 3. via PTCH1 (`NCBIGene:5727`) — IN ENTRY
- Entry already models this as: **genetic: PTCH1**
- Translator score: 0.555
- Vismodegib --affects--> PTCH1  
  - asserted by: dgidb
- PTCH1 --causes--> nevoid basal cell carcinoma syndrome  
  - asserted by: service-provider-trapi
