# MorPhiC cellular phenotypes

### MorPhiC Cellular Phenotypes

The MorPhiC Consortium (Molecular Phenotypes of Null Alleles in Cells) creates null alleles of human genes in iPSC-derived multicellular systems and measures their molecular and cellular phenotypes. MorPhiC data can enrich dismech entries with `category: Cellular` phenotypes.

**When to add MorPhiC-derived phenotypes:**
- The disorder involves a gene targeted by MorPhiC (check morphic.bio for gene lists)
- iPSC-derived cellular models recapitulate disease-relevant phenotypes
- Evidence source should be `IN_VITRO` for all MorPhiC-derived evidence

**Pattern for cellular phenotypes:**
```yaml
phenotypes:
- category: Cellular
  name: Impaired Cardiomyocyte Differentiation
  description: >
    Gene-null iPSC-derived cardiomyocytes show impaired differentiation...
  phenotype_term:
    preferred_term: Impaired cardiomyocyte differentiation
    term:
      id: HP:0001637
      label: Abnormal myocardium morphology
  evidence:
  - reference: PMID:39939790
    supports: SUPPORT
    evidence_source: IN_VITRO
    snippet: "exact quote from paper"
    explanation: "How MorPhiC data supports this phenotype"
```

**MorPhiC dataset references:**
```yaml
datasets:
- accession: morphic:GENE_SYMBOL
  title: MorPhiC null allele phenotyping of GENE in iPSC-derived cells
  data_type: MULTI_OMICS_PERTURBATION
  organism:
    preferred_term: human
    term:
      id: NCBITaxon:9606
      label: Homo sapiens
  publication: PMID:39939790
```

Key MorPhiC anchor genes: ISL1, EOMES, GCM1, NKX2-1. Data available under CC BY 4.0.
