---
provider: translator
model: ncats-translator-ars
cached: false
start_time: '2026-08-02T19:36:59.654519+00:00'
end_time: '2026-08-02T19:37:48.041265+00:00'
duration_seconds: 48.39
citation_count: 4
template_variables:
  disease_name: Tuberous Sclerosis Complex
  hypothesis_group_id: canonical_tsc1_tsc2_mtorc1_hyperactivation_model
  hypothesis_label: Canonical TSC1 / TSC2 / mTORC1 Hyperactivation Model
  hypothesis_status: CANONICAL
provider_config:
  ars_url: https://ars-prod.transltr.io
  ars_pk: 331b29a2-cc04-44fc-a48e-6cc09665d366
  merged_pk: 0a05e598-3792-4725-a68d-670214f9e9f7
  query_graph:
    nodes:
      chem:
        ids:
        - CHEBI:68478
        categories:
        - biolink:ChemicalEntity
      mid:
        categories:
        - biolink:Gene
      disease:
        ids:
        - MONDO:0001734
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

# Translator mechanism paths: Everolimus -> tuberous sclerosis

- Drug: `CHEBI:68478` (Everolimus)
- Disease: `MONDO:0001734` (tuberous sclerosis)
- Intermediate node type: `gene`
- dismech entry: `kb/disorders/Tuberous_Sclerosis_Complex.yaml`
- Entry already curates this drug as: **everolimus**
  - declared `target_mechanisms`: Constitutive mTORC1 Hyperactivation (INHIBITS); mTOR-Driven Multisystem Hamartoma Growth (INHIBITS); Renal Angiomyolipoma Growth (INHIBITS); Subependymal Glioneuronal Tumor Growth (INHIBITS); Pulmonary Lymphangioleiomyomatosis Growth (INHIBITS)
- ARS pk: `331b29a2-cc04-44fc-a48e-6cc09665d366`
- Translator UI: https://ui.transltr.io/main/results?q=331b29a2-cc04-44fc-a48e-6cc09665d366
- Generated: 2026-08-02T19:37:48.041265+00:00
- Paths: 3

> These paths are **machine-generated leads**, not curated mechanism. Each hop is a single knowledge-provider assertion — text-mined co-occurrence (`semmeddb`) sits beside curated pharmacology (`drugcentral`, `dgidb`) with no distinction in the ranking. A path is a hypothesis to check against primary literature, and every PMID below still has to go through `just fetch-reference` + `just validate-references` before it can support anything in an entry.

| # | Intermediate | In entry? | Score | Path | Sources |
| - | ------------ | --------- | ----- | ---- | ------- |
| 1 | TSC1 (`NCBIGene:7248`) | pathophysiology: TSC1/TSC2 Loss of Function (Germline First Hit) | 0.56 | Everolimus --interacts_with--> TSC1 | TSC1 --gene_associated_with_condition--> tuberous sclerosis | clingen, dgidb, orphanet |
| 2 | TSC2 (`NCBIGene:7249`) | pathophysiology: TSC1/TSC2 Loss of Function (Germline First Hit) | 0.49 | Everolimus --interacts_with--> TSC2 | TSC2 --gene_associated_with_condition--> tuberous sclerosis | clingen, clinvar, dgidb |
| 3 | IFNG (`NCBIGene:3458`) | — | 0.44 | Everolimus --affects--> IFNG | IFNG --contributes_to--> tuberous sclerosis | automat-robokop, orphanet, service-provider-trapi |

## Path detail

### 1. via TSC1 (`NCBIGene:7248`) — IN ENTRY
- Entry already models this as: **pathophysiology: TSC1/TSC2 Loss of Function (Germline First Hit)**
- Translator score: 0.556
- Everolimus --interacts_with--> TSC1  
  - asserted by: dgidb  
  - publications: `PMID:22923433`, `PMID:23158522`
- TSC1 --gene_associated_with_condition--> tuberous sclerosis  
  - asserted by: clingen
- Verify first: `just fetch-reference PMID:22923433`

### 2. via TSC2 (`NCBIGene:7249`) — IN ENTRY
- Entry already models this as: **pathophysiology: TSC1/TSC2 Loss of Function (Germline First Hit)**
- Translator score: 0.491
- Everolimus --interacts_with--> TSC2  
  - asserted by: dgidb  
  - publications: `PMID:23158522`, `PMID:25295501`
- TSC2 --gene_associated_with_condition--> tuberous sclerosis  
  - asserted by: clingen
- Verify first: `just fetch-reference PMID:23158522`

### 3. via IFNG (`NCBIGene:3458`) — NEW
- Translator score: 0.444
- Everolimus --affects--> IFNG  
  - asserted by: text-mining-provider-targeted
- IFNG --contributes_to--> tuberous sclerosis  
  - asserted by: automat-robokop
