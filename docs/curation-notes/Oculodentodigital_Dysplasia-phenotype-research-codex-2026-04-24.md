# Oculodentodigital Dysplasia phenotype curation notes

Date: 2026-04-19
Curator: Codex
Scope: Phenotype section only for `kb/disorders/Oculodentodigital_Dysplasia.yaml`

## PMIDs used

- `PMID:19338053`
  Supports characteristic nasal morphology (`narrow nose`, `hypoplastic alae nasi`) and the broader neurologic spectrum (`dysarthria`, `spastic paraparesis`, `neurogenic bladder disturbances`, `ataxia`, `seizures`), plus conductive hearing loss and generic skin/hair/nail anomalies.
- `PMID:32318302`
  Supports the core ocular phenotype and review-level ocular prominence: `microcornea`, `microphthalmia`, `short palpebral fissures`, and `glaucoma`.
- `PMID:34035645`
  Adds glaucoma-specific severity context from a literature review subset: glaucoma in `31/116` ocularly affected individuals, with most cases in patients `>=10` years old.
- `PMID:36990989`
  Supports the expanded dental phenotype (`enamel hypoplasia`, `enamel hypomineralization`, `microdontia`, `pulp stones`, `curved roots`, `taurodontism`) and provides direct support for `camptodactyly`.
- `PMID:29927410`
  Supports the characteristic digital pattern (`IV-V or III-V finger syndactyly`) and later-life neurologic manifestations (`spastic paraparesis`, `neurogenic bladder/bowel`, `ataxia`, `white matter lesions on MRI`).
- `PMID:31023660`
  Supports neuroimaging evidence for cerebral white matter abnormalities consistent with hypomyelination in neurologically affected ODDD patients.
- `PMID:12457340`
  Retained as phenotype support for non-universal `conductive hearing impairment`.

## Key curation decisions

- Split the previous combined nasal phenotype into separate `Narrow nose` and `Hypoplastic alae nasi` entries to improve HPO specificity.
- Replaced weak ocular support with review-backed ocular phenotype evidence.
- Expanded dental phenotypes using the 2023 systematic dental review rather than retaining broad, weakly supported summary claims.
- Replaced the general finger syndactyly term with `HP:0010705` (`4-5 finger cutaneous syndactyly`) because the published ODDD literature repeatedly emphasizes the fourth/fifth finger pattern.
- Switched the neurologic motor phenotype from `spastic paraplegia` to `spastic paraparesis` to match the exact wording of the phenotype-focused neurologic literature.
- Added `CNS hypomyelination` to capture the clinically important MRI phenotype in neurologically affected cases.

## Claims intentionally removed or softened

- Removed phenotype entries for `Sparse hair` and `Dry skin` because the available abstract-level support was too weak or nonspecific for those exact HPO terms.
- Softened the disease description from specific `sparse hair` to broader `skin/hair/nail anomalies`, which is directly supported by `PMID:19338053`.
- Removed unsupported frequency claims from ocular, neurologic, auditory, and skin phenotypes unless frequency wording was directly supported in the cited abstract.
