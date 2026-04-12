

# Slot: severity 



URI: [dismech:slot/severity](https://w3id.org/monarch-initiative/dismech/slot/severity)
Alias: severity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Phenotype](../classes/Phenotype.md) |  |  no  |
| [PhenotypeContext](../classes/PhenotypeContext.md) | A context-specific annotation qualifying how a phenotype manifests under part... |  no  |






## Properties

* Range: [String](../types/String.md)





## Examples

| Value |
| --- |
| Severe |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:severity |
| native | dismech:severity |




## LinkML Source

<details>
```yaml
name: severity
examples:
- value: Severe
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: severity
domain_of:
- PhenotypeContext
- Phenotype
range: string

```
</details>