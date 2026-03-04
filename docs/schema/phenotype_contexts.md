

# Slot: phenotype_contexts 


_Context-specific qualifications of this phenotype's frequency, severity, or onset. Each context can optionally specify a genetic context, demographic stratum, or disease subtype. When no context qualifiers are set, provides evidence for the base frequency/severity claim (addressing the frequency-evidence separation problem)._





URI: [dismech:phenotype_contexts](https://w3id.org/monarch-initiative/dismech/phenotype_contexts)
Alias: phenotype_contexts

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Phenotype](Phenotype.md) |  |  no  |






## Properties

* Range: [PhenotypeContext](PhenotypeContext.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:phenotype_contexts |
| native | dismech:phenotype_contexts |




## LinkML Source

<details>
```yaml
name: phenotype_contexts
description: Context-specific qualifications of this phenotype's frequency, severity,
  or onset. Each context can optionally specify a genetic context, demographic stratum,
  or disease subtype. When no context qualifiers are set, provides evidence for the
  base frequency/severity claim (addressing the frequency-evidence separation problem).
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: phenotype_contexts
domain_of:
- Phenotype
range: PhenotypeContext
multivalued: true
inlined: true
inlined_as_list: true

```
</details>