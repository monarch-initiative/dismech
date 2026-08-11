# Enum: GeneDiseaseRelationshipEnum 




_The qualitative relationship between a gene (or locus) and a disease. Use to constrain the free-text `association` slot to a controlled vocabulary aligned with ClinGen gene-disease validity concepts and common cancer/somatic driver classifications. The free-text `association` slot may still be used for narrative detail._



URI: [dismech:enum/GeneDiseaseRelationshipEnum](https://w3id.org/monarch-initiative/dismech/enum/GeneDiseaseRelationshipEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| CAUSATIVE | None | Variants in the gene are sufficient to cause the disease in a mendelian or ne... | Title: Causative<br>|
| RISK_FACTOR | None | Variants in the gene increase risk of disease but are neither necessary nor s... | Title: Risk factor<br>|
| PROTECTIVE | None | Variants in the gene reduce the risk or severity of disease | Title: Protective<br>|
| MODIFIER | None | Variants in the gene modify the severity, age of onset, or expressivity of di... | Title: Modifier<br>|
| SUSCEPTIBILITY | None | Variants in the gene confer susceptibility to disease in combination with oth... | Title: Susceptibility<br>|
| SOMATIC_DRIVER | None | Somatic alterations in the gene drive tumor initiation or progression (e | Title: Somatic driver<br>|
| COOPERATING | None | Co-occurring somatic or germline alterations that cooperate with a primary dr... | Title: Cooperating alteration<br>|
| BIOMARKER | None | Gene whose expression, mutation, or amplification status serves as a diagnost... | Title: Biomarker<br>|
| DISPUTED | None | Reported gene-disease association whose validity is contested (corresponds to... | Title: Disputed<br>|
| UNKNOWN | None | The relationship between the gene and the disease is unclear or not yet class... | Title: Unknown<br>|




## Slots

| Name | Description |
| ---  | --- |
| [relationship_type](../slots/relationship_type.md) | Controlled-vocabulary classification of the gene-disease relationship (e |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: GeneDiseaseRelationshipEnum
description: The qualitative relationship between a gene (or locus) and a disease.
  Use to constrain the free-text `association` slot to a controlled vocabulary aligned
  with ClinGen gene-disease validity concepts and common cancer/somatic driver classifications.
  The free-text `association` slot may still be used for narrative detail.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  CAUSATIVE:
    text: CAUSATIVE
    description: Variants in the gene are sufficient to cause the disease in a mendelian
      or near-mendelian sense (corresponds to ClinGen "Definitive" or "Strong" gene-disease
      validity).
    title: Causative
  RISK_FACTOR:
    text: RISK_FACTOR
    description: Variants in the gene increase risk of disease but are neither necessary
      nor sufficient to cause it. Includes common-variant associations and HLA risk
      alleles.
    title: Risk factor
  PROTECTIVE:
    text: PROTECTIVE
    description: Variants in the gene reduce the risk or severity of disease.
    title: Protective
  MODIFIER:
    text: MODIFIER
    description: Variants in the gene modify the severity, age of onset, or expressivity
      of disease without being a primary driver.
    title: Modifier
  SUSCEPTIBILITY:
    text: SUSCEPTIBILITY
    description: Variants in the gene confer susceptibility to disease in combination
      with other genetic or environmental factors. Used for polygenic susceptibility
      loci such as GWAS hits.
    title: Susceptibility
  SOMATIC_DRIVER:
    text: SOMATIC_DRIVER
    description: Somatic alterations in the gene drive tumor initiation or progression
      (e.g., recurrent oncogenic drivers in cancer).
    title: Somatic driver
  COOPERATING:
    text: COOPERATING
    description: Co-occurring somatic or germline alterations that cooperate with
      a primary driver to shape disease behavior or therapy response.
    title: Cooperating alteration
  BIOMARKER:
    text: BIOMARKER
    description: Gene whose expression, mutation, or amplification status serves as
      a diagnostic, prognostic, or predictive biomarker without a required causal
      role.
    title: Biomarker
  DISPUTED:
    text: DISPUTED
    description: Reported gene-disease association whose validity is contested (corresponds
      to ClinGen "Disputed" or "Refuted").
    title: Disputed
  UNKNOWN:
    text: UNKNOWN
    description: The relationship between the gene and the disease is unclear or not
      yet classified.
    title: Unknown

```
</details>