

# Slot: variants 



URI: [dismech:variants](https://w3id.org/monarch-initiative/dismech/variants)
Alias: variants

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Genetic](Genetic.md) |  |  no  |
| [Disease](Disease.md) |  |  no  |






## Properties

* Range: [Variant](Variant.md)

* Multivalued: True




## Comments

* can currently be used at gene or disease level, TODO - decide the best level

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:variants |
| native | dismech:variants |




## LinkML Source

<details>
```yaml
name: variants
comments:
- can currently be used at gene or disease level, TODO - decide the best level
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: variants
domain_of:
- Genetic
- Disease
range: Variant
multivalued: true
inlined: true
inlined_as_list: true

```
</details>