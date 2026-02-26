# Enum: IUISCategoryEnum 




_IUIS classification tables for inborn errors of immunity (IEI). Based on IUIS 2022 phenotypic classification._



URI: [MONDO:0003778](http://purl.obolibrary.org/obo/MONDO_0003778)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| combined immunodeficiency | MONDO:0015131 | Table 1 - Immunodeficiencies affecting cellular and humoral immunity (SCID, C... |
| combined immunodeficiency with syndromic features | None | Table 2 - CID with associated or syndromic features (WAS, AT, DiGeorge, CHARG... |
| predominantly antibody deficiency | None | Table 3 - Predominantly antibody deficiencies (XLA, CVID, selective Ig defici... |
| immune dysregulation | None | Table 4 - Diseases of immune dysregulation (HLH, ALPS, IPEX, APECED) |
| phagocyte defect | None | Table 5 - Congenital defects of phagocyte number or function (SCN, CGD, LAD) |
| innate immunity defect | None | Table 6 - Defects in intrinsic and innate immunity (MSMD, HSE susceptibility,... |
| autoinflammatory syndrome | MONDO:0019751 | Table 7 - Autoinflammatory disorders (FMF, CAPS, TRAPS, HIDS, interferonopath... |
| complement deficiency | MONDO:0003832 | Table 8 - Complement deficiencies (C1-C9, MBL, factor H/I/B, properdin) |
| bone marrow failure | None | Table 9 - Bone marrow failure syndromes (Fanconi, DKC, SDS, DBA) |
| phenocopy of IEI | None | Table 10 - Phenocopies of IEI (somatic mutations, autoantibodies to cytokines... |




## Slots

| Name | Description |
| ---  | --- |
| [classification_value](classification_value.md) |  |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: IUISCategoryEnum
description: IUIS classification tables for inborn errors of immunity (IEI). Based
  on IUIS 2022 phenotypic classification.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
enum_uri: MONDO:0003778
permissible_values:
  combined immunodeficiency:
    text: combined immunodeficiency
    description: Table 1 - Immunodeficiencies affecting cellular and humoral immunity
      (SCID, CID, Omenn)
    meaning: MONDO:0015131
  combined immunodeficiency with syndromic features:
    text: combined immunodeficiency with syndromic features
    description: Table 2 - CID with associated or syndromic features (WAS, AT, DiGeorge,
      CHARGE)
  predominantly antibody deficiency:
    text: predominantly antibody deficiency
    description: Table 3 - Predominantly antibody deficiencies (XLA, CVID, selective
      Ig deficiency, hyper-IgM)
  immune dysregulation:
    text: immune dysregulation
    description: Table 4 - Diseases of immune dysregulation (HLH, ALPS, IPEX, APECED)
  phagocyte defect:
    text: phagocyte defect
    description: Table 5 - Congenital defects of phagocyte number or function (SCN,
      CGD, LAD)
  innate immunity defect:
    text: innate immunity defect
    description: Table 6 - Defects in intrinsic and innate immunity (MSMD, HSE susceptibility,
      CMC)
  autoinflammatory syndrome:
    text: autoinflammatory syndrome
    description: Table 7 - Autoinflammatory disorders (FMF, CAPS, TRAPS, HIDS, interferonopathies)
    meaning: MONDO:0019751
  complement deficiency:
    text: complement deficiency
    description: Table 8 - Complement deficiencies (C1-C9, MBL, factor H/I/B, properdin)
    meaning: MONDO:0003832
  bone marrow failure:
    text: bone marrow failure
    description: Table 9 - Bone marrow failure syndromes (Fanconi, DKC, SDS, DBA)
  phenocopy of IEI:
    text: phenocopy of IEI
    description: Table 10 - Phenocopies of IEI (somatic mutations, autoantibodies
      to cytokines)

```
</details>