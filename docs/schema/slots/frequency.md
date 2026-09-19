

# Slot: frequency 



URI: [dismech:slot/frequency](https://w3id.org/monarch-initiative/dismech/slot/frequency)
Alias: frequency

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |
| [Genetic](../classes/Genetic.md) |  |  no  |
| [Biochemical](../classes/Biochemical.md) |  |  no  |
| [HistopathologyFinding](../classes/HistopathologyFinding.md) | A histopathologic finding from microscopic examination of tissue |  yes  |
| [Phenotype](../classes/Phenotype.md) |  |  no  |
| [PhenotypeContext](../classes/PhenotypeContext.md) | A context-specific annotation qualifying how a phenotype manifests under part... |  no  |
| [ImagingFinding](../classes/ImagingFinding.md) | A finding detected by in-vivo medical imaging (MRI, CT, PET, ultrasound, etc |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FrequencyEnum](../enums/FrequencyEnum.md)&nbsp;or&nbsp;<br />[FrequencyQuantity](../types/FrequencyQuantity.md)&nbsp;or&nbsp;<br />[Any](../classes/Any.md) |
| Domain Of | [PhenotypeContext](../classes/PhenotypeContext.md), [Pathophysiology](../classes/Pathophysiology.md), [Phenotype](../classes/Phenotype.md), [Biochemical](../classes/Biochemical.md), [HistopathologyFinding](../classes/HistopathologyFinding.md), [ImagingFinding](../classes/ImagingFinding.md), [Genetic](../classes/Genetic.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'FrequencyEnum'})
- AnonymousSlotExpression({'range': 'FrequencyQuantity'})

</details>










## Examples

| Value |
| --- |
| Occasional |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:frequency |
| native | dismech:frequency |




## LinkML Source

<details>
```yaml
name: frequency
examples:
- value: Occasional
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: frequency
domain_of:
- PhenotypeContext
- Pathophysiology
- Phenotype
- Biochemical
- HistopathologyFinding
- ImagingFinding
- Genetic
range: Any
any_of:
- range: FrequencyEnum
- range: FrequencyQuantity

```
</details>