

# Slot: attaches_to 


_Multivalued list of entity references pointing at the disease nodes, gaps, phenotypes, or other objects this item is about. Uses a hash-anchor grammar consistent with `conforms_to`: `[<file>:]<kind>#<name>`. Examples: `pathophysiology#Amyloid Plaque Formation`, `phenotype#Memory Loss`, `Liver_Cirrhosis:pathophysiology#Hepatic Stellate Cell Activation`. Range is `string` for now; a custom EntityRef type with parser support can be introduced later without breaking existing data._





URI: [dismech:slot/attaches_to](https://w3id.org/monarch-initiative/dismech/slot/attaches_to)
Alias: attaches_to

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Discussion](../classes/Discussion.md) | A thread-like record of an open question, controversy, curation todo, emergin... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Discussion](../classes/Discussion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:attaches_to |
| native | dismech:attaches_to |




## LinkML Source

<details>
```yaml
name: attaches_to
description: 'Multivalued list of entity references pointing at the disease nodes,
  gaps, phenotypes, or other objects this item is about. Uses a hash-anchor grammar
  consistent with `conforms_to`: `[<file>:]<kind>#<name>`. Examples: `pathophysiology#Amyloid
  Plaque Formation`, `phenotype#Memory Loss`, `Liver_Cirrhosis:pathophysiology#Hepatic
  Stellate Cell Activation`. Range is `string` for now; a custom EntityRef type with
  parser support can be introduced later without breaking existing data.'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: attaches_to
domain_of:
- Discussion
range: string
multivalued: true

```
</details>