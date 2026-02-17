# Lynch Syndrome Review

## Scope
Remaining findings after iterative evidence and modeling cleanup of `kb/disorders/Lynch_Syndrome.yaml`.

## Resolved in Current Iteration

1. Removed all `WRONG_STATEMENT` / `NO_EVIDENCE` evidence tags.
2. Consolidated duplicate phenotypes (`Urinary Tract Cancer`, `Sebaceous Adenomas`).
3. Improved cell type term specificity in pathophysiology:
- `CL:0011108` colon epithelial cell
- `CL:0002656` glandular endometrial unciliated epithelial cell
4. Upgraded key pathophysiology process term from generic DNA repair to:
- `GO:0006298` mismatch repair
- `GO:0045005` DNA-templated DNA replication maintenance of fidelity
5. Added explicit subcellular and complex-level annotations:
- `cellular_components`: `GO:0005654` nucleoplasm
- `protein_complexes`: `GO:0032300` mismatch repair complex
6. Expanded pathophysiology causal chain with evidence-backed `downstream` edges:
- DNA MMR deficiency -> Microsatellite instability
- Microsatellite instability -> Accelerated tumor development
- Microsatellite instability -> Neoantigen generation and immune activation
- Neoantigen generation and immune activation -> Immune checkpoint blockade sensitivity
7. Added mechanistic pathophysiology node:
- `Immune Checkpoint Blockade Sensitivity` with supporting dMMR/MSI immunotherapy evidence.
8. Added missing phenotype ontology mappings across all major Lynch-associated cancers:
- `MONDO:0005575` colorectal cancer
- `MONDO:0011962` endometrial cancer
- `HP:0012126` stomach cancer
- `MONDO:0020654` renal pelvis/ureter urothelial carcinoma
- `MONDO:0005140` ovarian carcinoma
- `MONDO:0002375` sebaceous adenoma
9. Removed weak title-only phenotype evidence rows.
10. Updated chemoprevention treatment modeling to `MAXO:0000058` and added aspirin agent `CHEBI:15365`.
11. Aligned dataset description with `sample_count` by clarifying 566 tumor + 19 non-tumoral samples.
12. Added prevalence evidence explicitly documenting high general-population carrier frequency (≥1:300).
13. Added inheritance evidence for `MLH1 -> Autosomal Dominant`.
14. Added dataset-level evidence and publication linkage for both GEO datasets, plus `sample_types[].term` annotations.
15. Maintained 100% compliance score for this disorder file after graph/term expansion.

## Findings

1. **High** - Reference validation is not effectively running snippet matching for this file in current environment (`Total checks: 0`).

2. **Residual Risk** - Manual curation quality is now strong, but snippet verification remains dependent on fixing the reference-validator execution behavior in this repository environment.

## Validation note
`just validate-references kb/disorders/Lynch_Syndrome.yaml` currently reports `Total checks: 0` in this repository environment, so snippet-level verification is effectively not being exercised for this file.
