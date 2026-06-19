

# Slot: discussions 


_Open or recently-resolved discussion items attached to this entry. Each Discussion is a thread-like object with a `prompt`, a `kind` (OPEN_QUESTION, KNOWLEDGE_GAP, CONTROVERSY, etc.), a `status`, optional `attaches_to` pointers to specific nodes/gaps, an optional `proposed_experiments` block, and an `evidence` block reusing the standard EvidenceItem shape for citing primary literature, community commentary (e.g., Alzforum), and forum/issue threads._





URI: [dismech:slot/discussions](https://w3id.org/monarch-initiative/dismech/slot/discussions)
Alias: discussions

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Disease](../classes/Disease.md) |  |  no  |
| [Grouping](../classes/Grouping.md) | An explicit, curated union of distinct Disease entries assembled below the le... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Discussion](../classes/Discussion.md) |
| Domain Of | [Disease](../classes/Disease.md), [Grouping](../classes/Grouping.md) |

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
| self | dismech:discussions |
| native | dismech:discussions |




## LinkML Source

<details>
```yaml
name: discussions
description: Open or recently-resolved discussion items attached to this entry. Each
  Discussion is a thread-like object with a `prompt`, a `kind` (OPEN_QUESTION, KNOWLEDGE_GAP,
  CONTROVERSY, etc.), a `status`, optional `attaches_to` pointers to specific nodes/gaps,
  an optional `proposed_experiments` block, and an `evidence` block reusing the standard
  EvidenceItem shape for citing primary literature, community commentary (e.g., Alzforum),
  and forum/issue threads.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: discussions
domain_of:
- Disease
- Grouping
range: Discussion
multivalued: true
inlined: true
inlined_as_list: true

```
</details>