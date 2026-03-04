

# Slot: hosts 



URI: [dismech:hosts](https://w3id.org/monarch-initiative/dismech/hosts)
Alias: hosts

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AgentLifeCycle](AgentLifeCycle.md) |  |  no  |






## Properties

* Range: [HostDescriptor](HostDescriptor.md)

* Multivalued: True




## Comments

* Use NCBITaxon terms for host organisms
* Use the role slot to indicate definitive, intermediate, reservoir, or accidental host

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:hosts |
| native | dismech:hosts |




## LinkML Source

<details>
```yaml
name: hosts
comments:
- Use NCBITaxon terms for host organisms
- Use the role slot to indicate definitive, intermediate, reservoir, or accidental
  host
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: hosts
domain_of:
- AgentLifeCycle
range: HostDescriptor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>