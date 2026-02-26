

# Slot: qualifiers  <span style="color: red;"><strong> (DEPRECATED) </strong></span> 


_List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values._





URI: [dismech:qualifiers](https://w3id.org/monarch-initiative/dismech/qualifiers)
Alias: qualifiers

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeneDescriptor](GeneDescriptor.md) | A descriptor for genes, bindable to HGNC or other gene databases |  no  |
| [PhenotypeDescriptor](PhenotypeDescriptor.md) | A descriptor for phenotypes, bindable to Human Phenotype Ontology (HP) |  no  |
| [AssayDescriptor](AssayDescriptor.md) | A descriptor for assays, bindable to OBI |  no  |
| [Descriptor](Descriptor.md) | Base class for structured descriptors that allow a preferred term, optional d... |  no  |
| [ProteinComplexDescriptor](ProteinComplexDescriptor.md) | A descriptor for protein complexes that gene products participate in, bindabl... |  no  |
| [OrganismDescriptor](OrganismDescriptor.md) | A descriptor for organisms, bindable to NCBITaxon |  no  |
| [LifeCycleStageDescriptor](LifeCycleStageDescriptor.md) | A descriptor for parasite life cycle stages, bindable to OPL |  no  |
| [RegimenDescriptor](RegimenDescriptor.md) | A descriptor for treatment regimens, bindable to NCIT |  no  |
| [HistopathologyFindingDescriptor](HistopathologyFindingDescriptor.md) | A descriptor for histopathologic findings, bindable to NCIT Morphologic Findi... |  no  |
| [GeneProductDescriptor](GeneProductDescriptor.md) | A descriptor for gene products (proteins, fusion proteins, oncoproteins), bin... |  no  |
| [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) | A descriptor for anatomical locations, bindable to UBERON |  no  |
| [DiseaseDescriptor](DiseaseDescriptor.md) | A descriptor for the focal disease, bindable to MONDO |  no  |
| [TriggerDescriptor](TriggerDescriptor.md) | A descriptor for triggers/causes |  no  |
| [BiologicalProcessDescriptor](BiologicalProcessDescriptor.md) | A descriptor for biological processes, bindable to Gene Ontology (GO) |  no  |
| [CellularComponentDescriptor](CellularComponentDescriptor.md) | A descriptor for cellular components, bindable to GO cellular component |  no  |
| [CellTypeDescriptor](CellTypeDescriptor.md) | A descriptor for cell types, bindable to Cell Ontology (CL) |  no  |
| [EnvironmentDescriptor](EnvironmentDescriptor.md) | A descriptor for environmental contexts/settings, bindable to ENVO |  no  |
| [ConditionDescriptor](ConditionDescriptor.md) | A descriptor for a condition or disease, optionally bound to MONDO |  no  |
| [ChemicalEntityDescriptor](ChemicalEntityDescriptor.md) | A descriptor for chemical entities, bindable to CHEBI |  no  |
| [TreatmentDescriptor](TreatmentDescriptor.md) | A descriptor for treatments/medical actions, bindable to Medical Action Ontol... |  no  |
| [ExposureDescriptor](ExposureDescriptor.md) | A descriptor for exposure events, bindable to ECTO or XCO |  no  |
| [HostDescriptor](HostDescriptor.md) | A descriptor for hosts in an infectious agent life cycle |  no  |
| [CriteriaItem](CriteriaItem.md) | A criterion element (clinical feature, test result, imaging requirement) |  no  |
| [BiomarkerDescriptor](BiomarkerDescriptor.md) | A descriptor for biomarkers, bindable to NCIT |  no  |
| [InheritanceDescriptor](InheritanceDescriptor.md) | A descriptor for inheritance patterns, bindable to HPO mode of inheritance te... |  no  |
| [SampleTypeDescriptor](SampleTypeDescriptor.md) | A descriptor for biological sample types (tissue and/or cell type) |  no  |






## Properties

* Range: [Qualifier](Qualifier.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:qualifiers |
| native | dismech:qualifiers |




## LinkML Source

<details>
```yaml
name: qualifiers
description: List of predicate-value pairs for formal post-composition. Allows OWL-like
  expressivity with controlled predicates (e.g., RO relations) and values.
deprecated: Prefer explicit slots like located_in and laterality instead of generic
  qualifiers
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: qualifiers
domain_of:
- Descriptor
range: Qualifier
multivalued: true
inlined: true
inlined_as_list: true

```
</details>