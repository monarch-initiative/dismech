# Achondrogenesis Type II phenotype curation notes

Date: 2026-04-18
Target file: `kb/disorders/Achondrogenesis_Type_II.yaml`
Scope: phenotype section only

Validated phenotype-supporting PMIDs used in this pass:
- `PMID:15054848` supports severe micromelia and early fetal hygroma.
- `PMID:12124695` supports absent vertebral body ossification as a key prenatal finding.
- `PMID:17994563` supports short limbs, fetal hygroma, and fetal hydrops with septated cystic hygroma.
- `PMID:20387359` supports extreme micromelia, small thorax, macrocephaly/large head, polyhydramnios, short neck, and prominent abdomen.
- `PMID:36376277` supports cystic hygroma with severe limb shortening at 14 weeks.
- `PMID:41373627` supports micrognathia and hydrops.

Phenotype claims removed or softened in this pass:
- `Flat face` removed because no validator-backed PMID abstract located in this pass stated a flat facial profile directly.
- `Cleft palate` removed because no validator-backed PMID abstract located in this pass stated cleft palate directly.
- `Short ribs` and `Pulmonary hypoplasia` were not retained as phenotype entries because the locally cached PubMed abstracts available to `validate-references` did not provide direct quotable support for those claims in this pass; the main disease description was softened to avoid overclaiming beyond the phenotype evidence.

Note on `PMID:31523626`:
- The cached abstract created by `just fetch-reference PMID:31523626` is too short to support phenotype-specific snippets, so it was not used for validated phenotype evidence even though the PubMed web view surfaces richer descriptive text.
