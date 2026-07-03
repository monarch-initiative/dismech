

# Slot: term 


_Optional structured ontology term reference_





URI: [dismech:slot/term](https://w3id.org/monarch-initiative/dismech/slot/term)
Alias: term

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EnvironmentDescriptor](../classes/EnvironmentDescriptor.md) | A descriptor for environmental contexts/settings, bindable to ENVO |  yes  |
| [HostDescriptor](../classes/HostDescriptor.md) | A descriptor for hosts in an infectious agent life cycle |  no  |
| [MolecularFunctionDescriptor](../classes/MolecularFunctionDescriptor.md) | A descriptor for molecular functions, bindable to Gene Ontology (GO) |  yes  |
| [ICD10CMMapping](../classes/ICD10CMMapping.md) | ICD-10-CM diagnosis code mapping |  yes  |
| [DiseaseDescriptor](../classes/DiseaseDescriptor.md) | A descriptor for the focal disease, bindable to MONDO |  yes  |
| [MondoMapping](../classes/MondoMapping.md) | MONDO disease ontology mapping |  yes  |
| [SubtypeDescriptor](../classes/SubtypeDescriptor.md) | A descriptor for disease subtypes, bindable to MONDO disease terms or NCIT on... |  yes  |
| [CellularComponentDescriptor](../classes/CellularComponentDescriptor.md) | A descriptor for cellular components, bindable to GO cellular component |  yes  |
| [HistopathologyFindingDescriptor](../classes/HistopathologyFindingDescriptor.md) | A descriptor for histopathologic findings, bindable to NCIT Morphologic Findi... |  yes  |
| [FoodDescriptor](../classes/FoodDescriptor.md) | A descriptor for foods, beverages, nutrients, minerals, and supplements, bind... |  yes  |
| [NCITMapping](../classes/NCITMapping.md) | NCIT disease, subtype, or disease/finding ontology mapping for cancer entries |  yes  |
| [CellTypeDescriptor](../classes/CellTypeDescriptor.md) | A descriptor for cell types, bindable to Cell Ontology (CL) |  yes  |
| [TreatmentDescriptor](../classes/TreatmentDescriptor.md) | A descriptor for treatments/medical actions, bindable to MAXO or NCIT clinica... |  yes  |
| [ModelVariableDescriptor](../classes/ModelVariableDescriptor.md) | A descriptor mapping a model variable to an ontology term (LOINC, CHEBI, HP, ... |  yes  |
| [SampleTypeDescriptor](../classes/SampleTypeDescriptor.md) | A descriptor for biological sample types (tissue and/or cell type) |  no  |
| [LifeCycleStageDescriptor](../classes/LifeCycleStageDescriptor.md) | A descriptor for parasite life cycle stages, bindable to OPL |  yes  |
| [BiomarkerDescriptor](../classes/BiomarkerDescriptor.md) | A descriptor for biomarkers, bindable to NCIT |  yes  |
| [BiologicalProcessDescriptor](../classes/BiologicalProcessDescriptor.md) | A descriptor for biological processes, bindable to Gene Ontology (GO) |  yes  |
| [TermMapping](../classes/TermMapping.md) | Mapping from this disease entry to an external term or code |  yes  |
| [ExposureDescriptor](../classes/ExposureDescriptor.md) | A descriptor for exposure events, bindable to ECTO or XCO |  yes  |
| [OrganismDescriptor](../classes/OrganismDescriptor.md) | A descriptor for organisms, bindable to NCBITaxon |  yes  |
| [Descriptor](../classes/Descriptor.md) | Base class for structured descriptors that allow a preferred term, optional d... |  no  |
| [CriteriaItem](../classes/CriteriaItem.md) | A criterion element (clinical feature, test result, imaging requirement) |  no  |
| [GeneDescriptor](../classes/GeneDescriptor.md) | A descriptor for genes, bindable to HGNC or other gene databases |  yes  |
| [AssayDescriptor](../classes/AssayDescriptor.md) | A descriptor for assays, bindable to OBI |  yes  |
| [ICD11FMapping](../classes/ICD11FMapping.md) | ICD-11 Foundation diagnosis code mapping |  yes  |
| [AnatomicalEntityDescriptor](../classes/AnatomicalEntityDescriptor.md) | A descriptor for anatomical locations, bindable to UBERON |  yes  |
| [ProteinComplexDescriptor](../classes/ProteinComplexDescriptor.md) | A descriptor for protein complexes that gene products participate in, bindabl... |  yes  |
| [ChemicalEntityDescriptor](../classes/ChemicalEntityDescriptor.md) | A descriptor for chemical entities, bindable to CHEBI |  yes  |
| [PhenotypeDescriptor](../classes/PhenotypeDescriptor.md) | A descriptor for phenotypes, bindable to Human Phenotype Ontology (HP) |  yes  |
| [GOEnrichmentTerm](../classes/GOEnrichmentTerm.md) | GO term enrichment result with statistical metrics |  no  |
| [GeneProductDescriptor](../classes/GeneProductDescriptor.md) | A descriptor for gene products (proteins, fusion proteins, oncoproteins), bin... |  yes  |
| [ConditionDescriptor](../classes/ConditionDescriptor.md) | A descriptor for a condition or disease, optionally bound to MONDO |  yes  |
| [RegimenDescriptor](../classes/RegimenDescriptor.md) | A descriptor for treatment regimens, bindable to NCIT |  yes  |
| [TriggerDescriptor](../classes/TriggerDescriptor.md) | A descriptor for triggers/causes |  yes  |
| [InheritanceDescriptor](../classes/InheritanceDescriptor.md) | A descriptor for inheritance patterns, bindable to HPO mode of inheritance te... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Term](../classes/Term.md) |
| Domain Of | [Descriptor](../classes/Descriptor.md), [TermMapping](../classes/TermMapping.md), [ConditionDescriptor](../classes/ConditionDescriptor.md), [GOEnrichmentTerm](../classes/GOEnrichmentTerm.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:term |
| native | dismech:term |




## LinkML Source

<details>
```yaml
name: term
description: Optional structured ontology term reference
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: term
domain_of:
- Descriptor
- TermMapping
- ConditionDescriptor
- GOEnrichmentTerm
range: Term
recommended: true
inlined: true

```
</details>