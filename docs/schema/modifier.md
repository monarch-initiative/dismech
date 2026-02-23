

# Slot: modifier 


_Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)_





URI: [dismech:modifier](https://w3id.org/monarch-initiative/dismech/modifier)
Alias: modifier

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SampleTypeDescriptor](SampleTypeDescriptor.md) | A descriptor for biological sample types (tissue and/or cell type) |  no  |
| [OrganismDescriptor](OrganismDescriptor.md) | A descriptor for organisms, bindable to NCBITaxon |  no  |
| [EnvironmentDescriptor](EnvironmentDescriptor.md) | A descriptor for environmental contexts/settings, bindable to ENVO |  no  |
| [TriggerDescriptor](TriggerDescriptor.md) | A descriptor for triggers/causes |  no  |
| [ExposureDescriptor](ExposureDescriptor.md) | A descriptor for exposure events, bindable to ECTO or XCO |  no  |
| [Descriptor](Descriptor.md) | Base class for structured descriptors that allow a preferred term, optional d... |  no  |
| [RegimenDescriptor](RegimenDescriptor.md) | A descriptor for treatment regimens, bindable to NCIT |  no  |
| [HistopathologyFindingDescriptor](HistopathologyFindingDescriptor.md) | A descriptor for histopathologic findings, bindable to NCIT Morphologic Findi... |  no  |
| [GeneDescriptor](GeneDescriptor.md) | A descriptor for genes, bindable to HGNC or other gene databases |  no  |
| [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) | A descriptor for anatomical locations, bindable to UBERON |  no  |
| [InheritanceDescriptor](InheritanceDescriptor.md) | A descriptor for inheritance patterns, bindable to HPO mode of inheritance te... |  no  |
| [CellTypeDescriptor](CellTypeDescriptor.md) | A descriptor for cell types, bindable to Cell Ontology (CL) |  no  |
| [ChemicalEntityDescriptor](ChemicalEntityDescriptor.md) | A descriptor for chemical entities, bindable to CHEBI |  no  |
| [HostDescriptor](HostDescriptor.md) | A descriptor for hosts in an infectious agent life cycle |  no  |
| [BiomarkerDescriptor](BiomarkerDescriptor.md) | A descriptor for biomarkers, bindable to NCIT |  no  |
| [ConditionDescriptor](ConditionDescriptor.md) | A descriptor for a condition or disease, optionally bound to MONDO |  no  |
| [ProteinComplexDescriptor](ProteinComplexDescriptor.md) | A descriptor for protein complexes that gene products participate in, bindabl... |  no  |
| [CriteriaItem](CriteriaItem.md) | A criterion element (clinical feature, test result, imaging requirement) |  no  |
| [GeneProductDescriptor](GeneProductDescriptor.md) | A descriptor for gene products (proteins, fusion proteins, oncoproteins), bin... |  no  |
| [DiseaseDescriptor](DiseaseDescriptor.md) | A descriptor for the focal disease, bindable to MONDO |  no  |
| [LifeCycleStageDescriptor](LifeCycleStageDescriptor.md) | A descriptor for parasite life cycle stages, bindable to OPL |  no  |
| [TreatmentDescriptor](TreatmentDescriptor.md) | A descriptor for treatments/medical actions, bindable to Medical Action Ontol... |  no  |
| [CellularComponentDescriptor](CellularComponentDescriptor.md) | A descriptor for cellular components, bindable to GO cellular component |  no  |
| [PhenotypeDescriptor](PhenotypeDescriptor.md) | A descriptor for phenotypes, bindable to Human Phenotype Ontology (HP) |  no  |
| [AssayDescriptor](AssayDescriptor.md) | A descriptor for assays, bindable to OBI |  no  |
| [BiologicalProcessDescriptor](BiologicalProcessDescriptor.md) | A descriptor for biological processes, bindable to Gene Ontology (GO) |  no  |






## Properties

* Range: [ModifierEnum](ModifierEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:modifier |
| native | dismech:modifier |




## LinkML Source

<details>
```yaml
name: modifier
description: Directional or qualitative modifier for a descriptor (e.g., increased,
  decreased, abnormal)
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: modifier
domain_of:
- Descriptor
range: ModifierEnum

```
</details>