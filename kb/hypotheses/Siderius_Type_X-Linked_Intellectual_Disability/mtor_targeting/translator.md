---
provider: translator
model: ncats-translator-ars
cached: false
start_time: '2026-08-02T01:02:11.924117+00:00'
end_time: '2026-08-02T01:03:47.320177+00:00'
duration_seconds: 95.4
citation_count: 4
template_variables:
  disease_name: Siderius Type X-Linked Intellectual Disability
  hypothesis_group_id: mtor_targeting
  hypothesis_label: mTOR pathway suppression as a disease-modifying strategy
  hypothesis_status: EMERGING
provider_config:
  ars_url: https://ars-prod.transltr.io
  ars_pk: ed4693fb-2ff7-4a3b-9187-b8dede8c7dc4
  merged_pk: 0efd81aa-35cb-422f-a1f3-57fe0b24d1a0
  query_graph:
    nodes:
      chem:
        ids:
        - CHEBI:9168
        categories:
        - biolink:ChemicalEntity
      mid:
        categories:
        - biolink:Gene
      disease:
        ids:
        - MONDO:0010286
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

# Translator mechanism paths: Sirolimus -> syndromic X-linked intellectual disability Siderius type

- Drug: `CHEBI:9168` (Sirolimus)
- Disease: `MONDO:0010286` (syndromic X-linked intellectual disability Siderius type)
- Intermediate node type: `gene`
- dismech entry: `kb/disorders/Siderius_Type_X-Linked_Intellectual_Disability.yaml`
- Entry does not yet curate this drug.
- ARS pk: `ed4693fb-2ff7-4a3b-9187-b8dede8c7dc4`
- Translator UI: https://ui.transltr.io/main/results?q=ed4693fb-2ff7-4a3b-9187-b8dede8c7dc4
- Generated: 2026-08-02T01:03:47.320177+00:00
- Paths: 2

> These paths are **machine-generated leads**, not curated mechanism. Each hop is a single knowledge-provider assertion — text-mined co-occurrence (`semmeddb`) sits beside curated pharmacology (`drugcentral`, `dgidb`) with no distinction in the ranking. A path is a hypothesis to check against primary literature, and every PMID below still has to go through `just fetch-reference` + `just validate-references` before it can support anything in an entry.

| # | Intermediate | In entry? | Score | Path | Sources |
| - | ------------ | --------- | ----- | ---- | ------- |
| 1 | FGD1 (`NCBIGene:2245`) | — | 1.00 | FGD1 --associated_with_resistance_to--> Sirolimus | FGD1 --gene_associated_with_condition--> syndromic X-linked intellectual disability Siderius type | biothings-multiomics-biggim-drugresponse, diseases |
| 2 | UBE2B (`NCBIGene:7320`) | — | 0.50 | UBE2B --associated_with_sensitivity_to--> Sirolimus | UBE2B --gene_associated_with_condition--> syndromic X-linked intellectual disability Siderius type | biothings-multiomics-biggim-drugresponse, diseases |

## Path detail

### 1. via FGD1 (`NCBIGene:2245`) — NEW
- Translator score: 1.000
- FGD1 --associated_with_resistance_to--> Sirolimus  
  - asserted by: biothings-multiomics-biggim-drugresponse  
  - publications: `PMID:27397505`
- FGD1 --gene_associated_with_condition--> syndromic X-linked intellectual disability Siderius type  
  - asserted by: diseases  
  - publications: `PMID:37519318`, `PMID:21124998`
- Verify first: `just fetch-reference PMID:27397505`

### 2. via UBE2B (`NCBIGene:7320`) — NEW
- Translator score: 0.500
- UBE2B --associated_with_sensitivity_to--> Sirolimus  
  - asserted by: biothings-multiomics-biggim-drugresponse  
  - publications: `PMID:27397505`
- UBE2B --gene_associated_with_condition--> syndromic X-linked intellectual disability Siderius type  
  - asserted by: diseases  
  - publications: `PMID:33376353`
- Verify first: `just fetch-reference PMID:27397505`
