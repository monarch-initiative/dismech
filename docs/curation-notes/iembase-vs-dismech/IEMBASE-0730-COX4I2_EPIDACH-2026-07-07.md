# IEMbase 0730: COX4I2-related cytochrome c oxidase subunit 4I2 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 730 |
| Nosology | 7.4.04.02 |
| Nosology code | IEM0465 |
| Gene | COX4I2 |
| External IDs | OMIM:612714; ORPHA:199337 |
| Generated mapping | MAPPED to `COX4I2-Related_Pancreatic_Insufficiency-Anemia-Hyperostosis_Syndrome.yaml` |
| Candidate DisMech targets | `COX4I2-Related_Pancreatic_Insufficiency-Anemia-Hyperostosis_Syndrome.yaml` is exact local coverage |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive COX4I2-related cytochrome c oxidase
subunit 4I2 deficiency. The alternate name is exocrine pancreatic insufficiency,
dyserythropoietic anemia, and calvarial hyperostosis. The cached phenotype rows
are concise: neonatal through childhood exocrine pancreatic insufficiency,
hepatomegaly, splenomegaly, and failure to thrive.

## DisMech phenotype coverage

DisMech has exact local coverage in
`COX4I2-Related_Pancreatic_Insufficiency-Anemia-Hyperostosis_Syndrome.yaml`.
The entry resolves to MONDO:0012992 and describes EPIDACH as a tissue-biased
complex IV structural-subunit disorder caused by biallelic COX4I2 variants.

Local phenotype coverage is broader than the IEMbase rows: congenital exocrine
pancreatic insufficiency, steatorrhea, malabsorption of lipid-soluble vitamins,
dyserythropoietic anemia, anemia, and calvarial hyperostosis.

## Concordance and completeness

Judgement: correct exact mapping with high identity.

The IEMbase alternate name and local disease identity are the same EPIDACH
entity. IEMbase adds hepatomegaly, splenomegaly, and age-banded failure to
thrive, while DisMech is much richer for the defining anemia, hyperostosis,
malabsorption, and COX4I2 tissue-biased mechanism.

## Curation actions

- Keep `COX4I2-Related_Pancreatic_Insufficiency-Anemia-Hyperostosis_Syndrome.yaml`
  as the canonical target.
- Consider reviewing local EPIDACH phenotypes for hepatomegaly, splenomegaly,
  and age-banded failure to thrive.
- Preserve local dyserythropoietic anemia and calvarial hyperostosis even though
  they are not in the cached IEMbase phenotype rows.
- Keep COX4I2 distinct from the ubiquitous COX4I1 structural-subunit disease.
