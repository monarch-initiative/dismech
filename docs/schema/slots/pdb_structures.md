

# Slot: pdb_structures 


_Experimental or predicted 3D protein structures relevant to this treatment's mechanism of action. Typically co-crystal structures of the drug bound to its target protein, or AlphaFold predictions of the drug target._





URI: [dismech:slot/pdb_structures](https://w3id.org/monarch-initiative/dismech/slot/pdb_structures)
Alias: pdb_structures

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |
| [Treatment](../classes/Treatment.md) |  |  no  |






## Properties

* Range: [ProteinStructure](../classes/ProteinStructure.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:pdb_structures |
| native | dismech:pdb_structures |




## LinkML Source

<details>
```yaml
name: pdb_structures
description: Experimental or predicted 3D protein structures relevant to this treatment's
  mechanism of action. Typically co-crystal structures of the drug bound to its target
  protein, or AlphaFold predictions of the drug target.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: pdb_structures
domain_of:
- Pathophysiology
- Treatment
range: ProteinStructure
multivalued: true
inlined: true
inlined_as_list: true

```
</details>