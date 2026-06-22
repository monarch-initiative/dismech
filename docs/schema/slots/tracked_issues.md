

# Slot: tracked_issues 


_Structured pointers to external tracker issues (e.g., GitHub ontology term requests, schema follow-ups) that provide curation provenance for this entry or nested object. Use this in preference to stashing issue URLs inside free-text `notes` fields so they can be validated, rendered, and queried consistently._





URI: [dismech:slot/tracked_issues](https://w3id.org/monarch-initiative/dismech/slot/tracked_issues)
Alias: tracked_issues

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FDASurrogateEndpointCollection](../classes/FDASurrogateEndpointCollection.md) | FDA surrogate endpoint table import preserving row-level source provenance |  no  |
| [TermMapping](../classes/TermMapping.md) | Mapping from this disease entry to an external term or code |  no  |
| [ICD10CMMapping](../classes/ICD10CMMapping.md) | ICD-10-CM diagnosis code mapping |  no  |
| [ICD11FMapping](../classes/ICD11FMapping.md) | ICD-11 Foundation diagnosis code mapping |  no  |
| [MondoMapping](../classes/MondoMapping.md) | MONDO disease ontology mapping |  no  |
| [SurrogateEndpointCollection](../classes/SurrogateEndpointCollection.md) | A source-level collection of curated regulatory surrogate endpoint assertions |  no  |
| [NCITMapping](../classes/NCITMapping.md) | NCIT disease, subtype, or disease/finding ontology mapping for cancer entries |  no  |
| [Disease](../classes/Disease.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TrackedIssue](../classes/TrackedIssue.md) |
| Domain Of | [SurrogateEndpointCollection](../classes/SurrogateEndpointCollection.md), [Disease](../classes/Disease.md), [TermMapping](../classes/TermMapping.md) |

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
| self | dismech:tracked_issues |
| native | dismech:tracked_issues |




## LinkML Source

<details>
```yaml
name: tracked_issues
description: Structured pointers to external tracker issues (e.g., GitHub ontology
  term requests, schema follow-ups) that provide curation provenance for this entry
  or nested object. Use this in preference to stashing issue URLs inside free-text
  `notes` fields so they can be validated, rendered, and queried consistently.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: tracked_issues
domain_of:
- SurrogateEndpointCollection
- Disease
- TermMapping
range: TrackedIssue
multivalued: true
inlined: true
inlined_as_list: true

```
</details>