# Mitochondrial Lipoylation Disorders

## Overview

This project curates the three known disorders of the mitochondrial protein lipoylation pathway. Lipoylation is a post-translational modification essential for the function of four mitochondrial enzyme complexes: pyruvate dehydrogenase (PDH), alpha-ketoglutarate dehydrogenase (OGDH), branched-chain alpha-ketoacid dehydrogenase (BCKDH), and the glycine cleavage system (GCS). The three enzymes of the lipoylation pathway form a linear biosynthetic chain:

```
Octanoyl-ACP → [LIPT2] → Octanoyl-GCSH → [LIAS] → Lipoyl-GCSH → [LIPT1] → Lipoylated E2 subunits (PDH/OGDH/BCKDH)
```

Deficiency of any enzyme in this pathway causes severe neonatal/infantile mitochondrial disease with lactic acidosis and neurological involvement. All three are ultra-rare (<20 patients reported worldwide).

## Goals

- Curate all three lipoylation pathway disorders with evidence-backed pathophysiology
- Map phenotypes to HPO terms with frequency data where available
- Annotate treatments with MAXO terms
- Capture genotype-phenotype distinctions (e.g., LIPT1 spares glycine cleavage)
- Provide PMID-supported evidence for all mechanistic and clinical claims

## Key Biochemical Distinctions

| Feature | LIPT2 (NELABA) | LIAS | LIPT1 |
|---------|----------------|------|-------|
| Step | Octanoyl transfer to GCSH | Sulfur insertion (radical SAM) | Lipoyl transfer to E2 subunits |
| Complexes affected | All (PDH, OGDH, BCKDH, GCS) | All (PDH, OGDH, BCKDH, GCS) | PDH, OGDH, BCKDH only |
| Glycine cleavage | Impaired | Impaired | **Spared** |
| Hyperglycinemia | Yes | Yes | No (key distinguishing feature) |
| OMIM | 617668 | 614462 | 616299 |

## Target Conditions

- [x] NELABA (LIPT2 deficiency) - `NELABA.yaml` - Created 2026-02-10, 89.4% compliance
- [x] Lipoic Acid Synthetase Deficiency (LIAS) - `Lipoic_Acid_Synthetase_Deficiency.yaml` - Created 2026-02-10, 91.7% compliance
- [x] Lipoyl Transferase 1 Deficiency (LIPT1) - `Lipoyl_Transferase_1_Deficiency.yaml` - Created 2026-02-10, 90.9% compliance

## Key References

| PMID | Authors | Year | Relevance |
|------|---------|------|-----------|
| PMID:28757203 | Habarou et al. | 2017 | LIPT2 index paper (3 patients) |
| PMID:39536593 | Sen et al. | 2025 | LIPT2 fourth reported case |
| PMID:22152680 | Mayr et al. | 2011 | LIAS index paper |
| PMID:24334290 | Baker et al. | 2014 | LIAS variant NKH cohort (LIAS/BOLA3/GLRX5) |
| PMID:24341803 | Soreze et al. | 2013 | LIPT1 index paper |
| PMID:24256811 | Tort et al. | 2014 | LIPT1 fatal disease characterization |
| PMID:29681092 | Stowe et al. | 2018 | LIPT1 fifth case |
| PMID:32508887 | Cronan | 2020 | Lipoic acid enzymology review (all 3 disorders) |
| PMID:39199267 | Gómez-Fernández et al. | 2024 | LIPT1 pharmacological rescue in cell models |
| PMID:39547509 | Bick et al. | 2024 | Engineered lplA restores lipoylation (all 3 disorders) |

## Deep Research Summary

Deep research was conducted using falcon and cyberian providers.

### Falcon
- **NELABA**: Returned wrong disease (NAXD/NAXE instead of LIPT2). Unreliable for this ultra-rare disorder.
- **LIAS**: Completed. Found pathway-level papers (Fe-S clusters, ferredoxins) but missed key clinical papers (Baker 2014). Useful for discovering Bick 2024.
- **LIPT1**: Best results. Discovered Bick 2024 (lplA therapy + new patient with sideroblastic anemia) and Gómez-Fernández 2024 (pharmacological cocktail rescue).

### Cyberian
- All 3 jobs failed with server errors (500 / connection refused). No results.

### Assessment
For ultra-rare Mendelian disorders, direct PubMed/OMIM-guided curation was the primary driver of quality. Deep research served as a supplementary discovery tool for newer publications but missed foundational clinical case reports and had disease confusion issues.

## Future Work

- [ ] Add phenotype context blocks with onset and frequency data as more cases are published
- [ ] Monitor for new LIPT2/LIAS/LIPT1 case reports to update patient counts
- [ ] Track progress of lplA gene therapy approach (Bick 2024) through preclinical studies
- [ ] Track Gómez-Fernández 2024 multi-target cocktail approach for LIPT1
- [ ] Consider adding related Fe-S cluster disorders (BOLA3, NFU1, ISCA2) that secondarily affect lipoylation
- [ ] Add cardiomyopathy phenotype to LIAS if verifiable reference found (mentioned in full text of Mayr 2011)

## Curation Workflow

1. Create YAML file in `kb/disorders/`
2. Validate with `just validate` and `just validate-references`
3. Validate terms with `just validate-terms-file`
4. Run `just qc` before committing
