

# Slot: images 


_Relative paths to image files (figures, charts, micrographs) sourced from deep-research artifacts that directly support this specific evidence claim. Paths are relative to the research/ directory and must correspond to an artifact file committed to the repository. Only include images that are directly relevant to the claim being evidenced — do not include images for general illustrative purposes._





URI: [dismech:slot/images](https://w3id.org/monarch-initiative/dismech/slot/images)
Alias: images

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EvidenceItem](../classes/EvidenceItem.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [EvidenceItem](../classes/EvidenceItem.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| Feingold_Syndrome-deep-research-falcon_artifacts/image-1.png |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:images |
| native | dismech:images |




## LinkML Source

<details>
```yaml
name: images
description: Relative paths to image files (figures, charts, micrographs) sourced
  from deep-research artifacts that directly support this specific evidence claim.
  Paths are relative to the research/ directory and must correspond to an artifact
  file committed to the repository. Only include images that are directly relevant
  to the claim being evidenced — do not include images for general illustrative purposes.
examples:
- value: Feingold_Syndrome-deep-research-falcon_artifacts/image-1.png
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: images
domain_of:
- EvidenceItem
range: string
multivalued: true

```
</details>