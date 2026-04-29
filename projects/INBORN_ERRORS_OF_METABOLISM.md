# Inborn Errors of Metabolism Curation Project

## Overview

This project tracks curation of high-priority inborn errors of metabolism (IEMs),
with emphasis on neonatal and early-childhood presentations that are common in
newborn screening workflows and NICU practice.

## Scope

- Create and validate missing disorder YAML files in `kb/disorders/`
- Maintain a running checklist of covered versus missing IEM entities
- Capture mechanistic pathophysiology, phenotype terms, and initial treatment structure

## Existing IEM Entries in KB

- [x] Phenylketonuria - `Phenylketonuria.yaml`
- [x] Maple Syrup Urine Disease - `Maple_Syrup_Urine_Disease.yaml`
- [x] Galactosemia - `Galactosemia.yaml`
- [x] MCAD Deficiency - `MCAD_Deficiency.yaml`
- [x] Peroxisome Biogenesis Disorder - `Peroxisome_Biogenesis_Disorder.yaml`

## Missing IEM Entries Curated in This Project

- [x] Urea Cycle Disorder - `Urea_Cycle_Disorder.yaml`
- [x] Ornithine Carbamoyltransferase Deficiency - `Ornithine_Carbamoyltransferase_Deficiency.yaml`
- [x] Propionic Acidemia - `Propionic_Acidemia.yaml`
- [x] Methylmalonic Acidemia - `Methylmalonic_Acidemia.yaml`
- [x] Isovaleric Acidemia - `Isovaleric_Acidemia.yaml`
- [x] VLCAD Deficiency - `VLCAD_Deficiency.yaml`

## Additional Missing IEM Entries Curated (25)

- [x] Citrullinemia Type I - `Citrullinemia_Type_I.yaml`
- [x] Argininosuccinic Aciduria - `Argininosuccinic_Aciduria.yaml`
- [x] Carbamoyl Phosphate Synthetase I Deficiency - `Carbamoyl_Phosphate_Synthetase_I_Deficiency.yaml`
- [x] Arginase Deficiency - `Arginase_Deficiency.yaml`
- [x] N-acetylglutamate Synthase Deficiency - `N-Acetylglutamate_Synthase_Deficiency.yaml`
- [x] Citrin Deficiency - `Citrin_Deficiency.yaml`
- [x] Glutaric Aciduria - `Glutaric_Aciduria.yaml`
- [x] Multiple Acyl-CoA Dehydrogenase Deficiency - `Multiple_Acyl-CoA_Dehydrogenase_Deficiency.yaml`
- [x] Isobutyryl-CoA Dehydrogenase Deficiency - `Isobutyryl-CoA_Dehydrogenase_Deficiency.yaml`
- [x] 3-Hydroxy-3-Methylglutaric Aciduria - `3-Hydroxy-3-Methylglutaric_Aciduria.yaml`
- [x] Beta-ketothiolase Deficiency - `Beta-Ketothiolase_Deficiency.yaml`
- [x] Biotinidase Deficiency - `Biotinidase_Deficiency.yaml`
- [x] Holocarboxylase Synthetase Deficiency - `Holocarboxylase_Synthetase_Deficiency.yaml`
- [x] Primary Carnitine Deficiency - `Primary_Carnitine_Deficiency.yaml`
- [x] Carnitine Palmitoyltransferase II Deficiency - `Carnitine_Palmitoyltransferase_II_Deficiency.yaml`
- [x] Carnitine-acylcarnitine Translocase Deficiency - `Carnitine-Acylcarnitine_Translocase_Deficiency.yaml`
- [x] Long-chain 3-hydroxyacyl-CoA Dehydrogenase Deficiency - `Long-Chain_3-Hydroxyacyl-CoA_Dehydrogenase_Deficiency.yaml`
- [x] Mitochondrial Trifunctional Protein Deficiency - `Mitochondrial_Trifunctional_Protein_Deficiency.yaml`
- [x] 2-Methylbutyryl-CoA Dehydrogenase Deficiency - `2-Methylbutyryl-CoA_Dehydrogenase_Deficiency.yaml`
- [x] D-2-Hydroxyglutaric Aciduria - `D-2-Hydroxyglutaric_Aciduria.yaml`
- [x] L-2-Hydroxyglutaric Aciduria - `L-2-Hydroxyglutaric_Aciduria.yaml`
- [x] Tyrosinemia Type I - `Tyrosinemia_Type_I.yaml`
- [x] Homocystinuria - `Homocystinuria.yaml`
- [x] Nonketotic Hyperglycinemia - `Nonketotic_Hyperglycinemia.yaml`
- [x] Guanidinoacetate Methyltransferase Deficiency - `Guanidinoacetate_Methyltransferase_Deficiency.yaml`

## Workflow

1. Create disorder file with MONDO mapping and initial mechanism blocks
2. Add HPO phenotypes and GO process terms where high confidence exists
3. Validate schema and ontology terms
4. Run compliance and track score in project status

---
# STATUS

## Existing IEM Entries (5/5) ✓

- [x] Phenylketonuria - Existing baseline entry
- [x] Maple Syrup Urine Disease - Existing baseline entry
- [x] Galactosemia - Existing baseline entry
- [x] MCAD Deficiency - Existing baseline entry
- [x] Peroxisome Biogenesis Disorder - Existing baseline entry

## Newly Curated Missing Entries (6/6) ✓

- [x] Urea Cycle Disorder - Created 2026-02-17, 76.0% compliance (78.3% weighted)
- [x] Ornithine Carbamoyltransferase Deficiency - Created 2026-02-17, 96.2% compliance (100.0% weighted)
- [x] Propionic Acidemia - Created 2026-02-17, 96.7% compliance (100.0% weighted)
- [x] Methylmalonic Acidemia - Created 2026-02-17, 96.9% compliance (100.0% weighted)
- [x] Isovaleric Acidemia - Created 2026-02-17, 96.0% compliance (100.0% weighted)
- [x] VLCAD Deficiency - Created 2026-02-17, 96.8% compliance (100.0% weighted)

## Additional Newly Curated Missing Entries (25/25) ✓

- [x] 25 additional missing IEM YAML entries created and schema/term-validated on 2026-02-17.
- [x] PMID-backed evidence enrichment completed for all 25 on 2026-02-17.
- [x] Post-enrichment compliance for all 25 entries: 92.9% global (13/14), 100.0% weighted.

# NOTES

## 2026-02-17

- Started `INBORN_ERRORS_OF_METABOLISM` project.
- Identified six high-priority IEM disorders without existing YAML entries.
- Created and term-annotated six new disorder files.
- Validated all six new files with `just validate` (schema + terms + references in recipe).
- Recorded compliance:
- `Urea_Cycle_Disorder.yaml`: 34.5% (33.3% weighted)
- `Ornithine_Carbamoyltransferase_Deficiency.yaml`: 46.4% (46.2% weighted)
- `Propionic_Acidemia.yaml`: 46.7% (46.4% weighted)
- `Methylmalonic_Acidemia.yaml`: 43.8% (43.3% weighted)
- `Isovaleric_Acidemia.yaml`: 44.0% (43.5% weighted)
- `VLCAD_Deficiency.yaml`: 41.9% (41.4% weighted)
- Added PMID-backed evidence to the first six files and revalidated all:
- `Urea_Cycle_Disorder.yaml`: 76.0% (78.3% weighted)
- `Ornithine_Carbamoyltransferase_Deficiency.yaml`: 96.2% (100.0% weighted)
- `Propionic_Acidemia.yaml`: 96.7% (100.0% weighted)
- `Methylmalonic_Acidemia.yaml`: 96.9% (100.0% weighted)
- `Isovaleric_Acidemia.yaml`: 96.0% (100.0% weighted)
- `VLCAD_Deficiency.yaml`: 96.8% (100.0% weighted)
- Created 25 additional missing IEM disorder files and validated all with `just validate`.
- Baseline compliance for each of the 25 new files is currently 42.9% global and 41.7% weighted.
- Added PMID-backed evidence blocks to pathophysiology, first two phenotypes, genetic/inheritance, and first two treatments for all 25 files.
- Revalidated all 25 files with `just validate`.
- Post-enrichment compliance for each of the 25 new files: 92.9% global (13/14) and 100.0% weighted.
- Tracking artifacts generated:
- `tmp/iem25_search_pmids.tsv` (slug-to-PMID mapping for enrichment)
- `tmp/iem25_compliance_after.tsv` (post-enrichment compliance snapshot)
