# Neuronal Ceroid Lipofuscinosis 7 Manual Research Notes

## Provider status

- Falcon deep research was attempted twice from the worktree. Both attempts stayed alive without creating the requested report or citations file, so they were stopped.
- The required cyberian fallback was attempted after Falcon failed to make progress. It exited with code 137 and produced no report or citations file.
- The YAML curation was completed directly from PubMed abstracts fetched with `just fetch-reference` and ontology terms checked with local OAK adapters.

## Evidence sources used

- PMID:17564970 identifies MFSD8 as the CLN7 gene, describes the 2-7 year late-infantile presentation, and reports lysosomal localization of MFSD8.
- PMID:19177532 expands the MFSD8/CLN7 mutation spectrum in Italian v-LINCL patients.
- PMID:25270050 reports MFSD8-related vLINCL clinical-pathologic findings, including intractable seizures, severe cognitive and motor decline, progressive retinal degeneration, storage material, and severe disease course.
- PMID:21990111 summarizes NCL mutation/phenotype correlations, including MFSD8/CLN7 and the common NCL clinical pattern.
- PMID:35087090 provides model-system evidence for impaired autophagy, damaged neuronal mitochondria, reactive oxygen species signaling, and PFKFB3 activation in CLN7 disease.
- PMID:35025759 reports preclinical AAV/MFSD8 rescue in CLN7 patient fibroblasts and Mfsd8-deficient mice.
- PMID:35154277 supports autosomal recessive MFSD8 causation and copy-number-aware molecular diagnosis.
- PMID:39555201 documents progressive visual loss/retinal degeneration as an early presentation of NCL7.

## Ontology checks

- `MONDO:0012588` label: neuronal ceroid lipofuscinosis 7.
- `hgnc:28486` label: MFSD8.
- HPO terms used: `HP:0000007`, `HP:0001250`, `HP:0002376`, `HP:0001268`, `HP:0001336`, `HP:0000546`, `HP:0000505`.
- GO terms used: `GO:0007041`, `GO:0006914`, `GO:0007005`, `GO:0000302`.
- MAXO term used: `MAXO:0001001`.
