
# Class: ~~Qualifier~~ _(deprecated)_

A predicate-value pair for formal post-composition. Allows OWL-like expressivity with controlled predicates and values, both as full Descriptors.

URI: [dismech:Qualifier](https://w3id.org/monarch-initiative/dismech/Qualifier)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Descriptor]<value%200..1-++[Qualifier],[Descriptor]<predicate%200..1-++[Qualifier],[Descriptor]++-%20qualifiers%200..*>[Qualifier],[Descriptor])](https://yuml.me/diagram/nofunky;dir:TB/class/[Descriptor]<value%200..1-++[Qualifier],[Descriptor]<predicate%200..1-++[Qualifier],[Descriptor]++-%20qualifiers%200..*>[Qualifier],[Descriptor])

## Referenced by Class

 *  **None** *[qualifiers](qualifiers.md)*  <sub>0..\*</sub>  **[Qualifier](Qualifier.md)**

## Attributes


### Own

 * [predicate](predicate.md)  <sub>0..1</sub>
     * Description: The relationship/predicate in a qualifier (e.g., RO:0002233 'has input')
     * Range: [Descriptor](Descriptor.md)
 * [value](value.md)  <sub>0..1</sub>
     * Description: The value/filler in a qualifier
     * Range: [Descriptor](Descriptor.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | DEPRECATED - prefer explicit slots (located_in, laterality) for better constraints |
|  | | Use for formal semantic relationships like "has_input some X" |
|  | | Both predicate and value are Descriptors, allowing recursive composition |
|  | | Predicate typically uses RO (Relation Ontology) terms |
