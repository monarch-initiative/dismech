

# Slot: preferred_term 


_The preferred human-readable term for this descriptor. This may be more specific or nuanced than the linked ontology term label when the ontology does not fully capture the desired granularity. Note that postcomposition using the modifier slot may be appropriate for capturing the semantics of the preferred term._





URI: [dismech:slot/preferred_term](https://w3id.org/monarch-initiative/dismech/slot/preferred_term)
Alias: preferred_term

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TriggerDescriptor](../classes/TriggerDescriptor.md) | A descriptor for triggers/causes |  no  |
| [AssayDescriptor](../classes/AssayDescriptor.md) | A descriptor for assays, bindable to OBI |  no  |
| [SampleTypeDescriptor](../classes/SampleTypeDescriptor.md) | A descriptor for biological sample types (tissue and/or cell type) |  no  |
| [CriteriaItem](../classes/CriteriaItem.md) | A criterion element (clinical feature, test result, imaging requirement) |  no  |
| [ModelVariableDescriptor](../classes/ModelVariableDescriptor.md) | A descriptor mapping a model variable to an ontology term (LOINC, CHEBI, HP, ... |  no  |
| [TreatmentDescriptor](../classes/TreatmentDescriptor.md) | A descriptor for treatments/medical actions, bindable to Medical Action Ontol... |  no  |
| [GeneProductDescriptor](../classes/GeneProductDescriptor.md) | A descriptor for gene products (proteins, fusion proteins, oncoproteins), bin... |  no  |
| [ConditionDescriptor](../classes/ConditionDescriptor.md) | A descriptor for a condition or disease, optionally bound to MONDO |  yes  |
| [OrganismDescriptor](../classes/OrganismDescriptor.md) | A descriptor for organisms, bindable to NCBITaxon |  no  |
| [DiseaseDescriptor](../classes/DiseaseDescriptor.md) | A descriptor for the focal disease, bindable to MONDO |  no  |
| [ChemicalEntityDescriptor](../classes/ChemicalEntityDescriptor.md) | A descriptor for chemical entities, bindable to CHEBI |  no  |
| [InheritanceDescriptor](../classes/InheritanceDescriptor.md) | A descriptor for inheritance patterns, bindable to HPO mode of inheritance te... |  no  |
| [ExposureDescriptor](../classes/ExposureDescriptor.md) | A descriptor for exposure events, bindable to ECTO or XCO |  no  |
| [Descriptor](../classes/Descriptor.md) | Base class for structured descriptors that allow a preferred term, optional d... |  no  |
| [GeneDescriptor](../classes/GeneDescriptor.md) | A descriptor for genes, bindable to HGNC or other gene databases |  no  |
| [BiomarkerDescriptor](../classes/BiomarkerDescriptor.md) | A descriptor for biomarkers, bindable to NCIT |  no  |
| [HistopathologyFindingDescriptor](../classes/HistopathologyFindingDescriptor.md) | A descriptor for histopathologic findings, bindable to NCIT Morphologic Findi... |  no  |
| [CellularComponentDescriptor](../classes/CellularComponentDescriptor.md) | A descriptor for cellular components, bindable to GO cellular component |  no  |
| [BiologicalProcessDescriptor](../classes/BiologicalProcessDescriptor.md) | A descriptor for biological processes, bindable to Gene Ontology (GO) |  no  |
| [LifeCycleStageDescriptor](../classes/LifeCycleStageDescriptor.md) | A descriptor for parasite life cycle stages, bindable to OPL |  no  |
| [ProteinComplexDescriptor](../classes/ProteinComplexDescriptor.md) | A descriptor for protein complexes that gene products participate in, bindabl... |  no  |
| [EnvironmentDescriptor](../classes/EnvironmentDescriptor.md) | A descriptor for environmental contexts/settings, bindable to ENVO |  no  |
| [HostDescriptor](../classes/HostDescriptor.md) | A descriptor for hosts in an infectious agent life cycle |  no  |
| [RegimenDescriptor](../classes/RegimenDescriptor.md) | A descriptor for treatment regimens, bindable to NCIT |  no  |
| [PhenotypeDescriptor](../classes/PhenotypeDescriptor.md) | A descriptor for phenotypes, bindable to Human Phenotype Ontology (HP) |  no  |
| [AnatomicalEntityDescriptor](../classes/AnatomicalEntityDescriptor.md) | A descriptor for anatomical locations, bindable to UBERON |  no  |
| [CellTypeDescriptor](../classes/CellTypeDescriptor.md) | A descriptor for cell types, bindable to Cell Ontology (CL) |  no  |






## Properties

* Range: [String](../types/String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:preferred_term |
| native | dismech:preferred_term |




## LinkML Source

<details>
```yaml
name: preferred_term
description: The preferred human-readable term for this descriptor. This may be more
  specific or nuanced than the linked ontology term label when the ontology does not
  fully capture the desired granularity. Note that postcomposition using the modifier
  slot may be appropriate for capturing the semantics of the preferred term.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: preferred_term
domain_of:
- Descriptor
- ConditionDescriptor
range: string
required: true

```
</details>