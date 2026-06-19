

# Slot: clinical_course 


_Clinical course qualifier for this descriptor (e.g., progressive, stable)_





URI: [dismech:slot/clinical_course](https://w3id.org/monarch-initiative/dismech/slot/clinical_course)
Alias: clinical_course

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EnvironmentDescriptor](../classes/EnvironmentDescriptor.md) | A descriptor for environmental contexts/settings, bindable to ENVO |  no  |
| [HostDescriptor](../classes/HostDescriptor.md) | A descriptor for hosts in an infectious agent life cycle |  no  |
| [MolecularFunctionDescriptor](../classes/MolecularFunctionDescriptor.md) | A descriptor for molecular functions, bindable to Gene Ontology (GO) |  no  |
| [DiseaseDescriptor](../classes/DiseaseDescriptor.md) | A descriptor for the focal disease, bindable to MONDO |  no  |
| [SubtypeDescriptor](../classes/SubtypeDescriptor.md) | A descriptor for disease subtypes, bindable to MONDO disease terms or NCIT on... |  no  |
| [CellularComponentDescriptor](../classes/CellularComponentDescriptor.md) | A descriptor for cellular components, bindable to GO cellular component |  no  |
| [HistopathologyFindingDescriptor](../classes/HistopathologyFindingDescriptor.md) | A descriptor for histopathologic findings, bindable to NCIT Morphologic Findi... |  no  |
| [FoodDescriptor](../classes/FoodDescriptor.md) | A descriptor for foods, beverages, nutrients, minerals, and supplements, bind... |  no  |
| [CellTypeDescriptor](../classes/CellTypeDescriptor.md) | A descriptor for cell types, bindable to Cell Ontology (CL) |  no  |
| [TreatmentDescriptor](../classes/TreatmentDescriptor.md) | A descriptor for treatments/medical actions, bindable to MAXO or NCIT clinica... |  no  |
| [ModelVariableDescriptor](../classes/ModelVariableDescriptor.md) | A descriptor mapping a model variable to an ontology term (LOINC, CHEBI, HP, ... |  no  |
| [SampleTypeDescriptor](../classes/SampleTypeDescriptor.md) | A descriptor for biological sample types (tissue and/or cell type) |  no  |
| [LifeCycleStageDescriptor](../classes/LifeCycleStageDescriptor.md) | A descriptor for parasite life cycle stages, bindable to OPL |  no  |
| [BiomarkerDescriptor](../classes/BiomarkerDescriptor.md) | A descriptor for biomarkers, bindable to NCIT |  no  |
| [BiologicalProcessDescriptor](../classes/BiologicalProcessDescriptor.md) | A descriptor for biological processes, bindable to Gene Ontology (GO) |  no  |
| [ExposureDescriptor](../classes/ExposureDescriptor.md) | A descriptor for exposure events, bindable to ECTO or XCO |  no  |
| [OrganismDescriptor](../classes/OrganismDescriptor.md) | A descriptor for organisms, bindable to NCBITaxon |  no  |
| [Descriptor](../classes/Descriptor.md) | Base class for structured descriptors that allow a preferred term, optional d... |  no  |
| [CriteriaItem](../classes/CriteriaItem.md) | A criterion element (clinical feature, test result, imaging requirement) |  no  |
| [GeneDescriptor](../classes/GeneDescriptor.md) | A descriptor for genes, bindable to HGNC or other gene databases |  no  |
| [AssayDescriptor](../classes/AssayDescriptor.md) | A descriptor for assays, bindable to OBI |  no  |
| [AnatomicalEntityDescriptor](../classes/AnatomicalEntityDescriptor.md) | A descriptor for anatomical locations, bindable to UBERON |  no  |
| [ProteinComplexDescriptor](../classes/ProteinComplexDescriptor.md) | A descriptor for protein complexes that gene products participate in, bindabl... |  no  |
| [ChemicalEntityDescriptor](../classes/ChemicalEntityDescriptor.md) | A descriptor for chemical entities, bindable to CHEBI |  no  |
| [PhenotypeDescriptor](../classes/PhenotypeDescriptor.md) | A descriptor for phenotypes, bindable to Human Phenotype Ontology (HP) |  no  |
| [GeneProductDescriptor](../classes/GeneProductDescriptor.md) | A descriptor for gene products (proteins, fusion proteins, oncoproteins), bin... |  no  |
| [ConditionDescriptor](../classes/ConditionDescriptor.md) | A descriptor for a condition or disease, optionally bound to MONDO |  no  |
| [RegimenDescriptor](../classes/RegimenDescriptor.md) | A descriptor for treatment regimens, bindable to NCIT |  no  |
| [TriggerDescriptor](../classes/TriggerDescriptor.md) | A descriptor for triggers/causes |  no  |
| [InheritanceDescriptor](../classes/InheritanceDescriptor.md) | A descriptor for inheritance patterns, bindable to HPO mode of inheritance te... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ClinicalCourseEnum](../enums/ClinicalCourseEnum.md) |
| Domain Of | [Descriptor](../classes/Descriptor.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:clinical_course |
| native | dismech:clinical_course |




## LinkML Source

<details>
```yaml
name: clinical_course
description: Clinical course qualifier for this descriptor (e.g., progressive, stable)
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: clinical_course
domain_of:
- Descriptor
range: ClinicalCourseEnum

```
</details>