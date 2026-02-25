

# Slot: term 


_Optional structured ontology term reference_





URI: [dismech:term](https://w3id.org/monarch-initiative/dismech/term)
Alias: term

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeneDescriptor](GeneDescriptor.md) | A descriptor for genes, bindable to HGNC or other gene databases |  yes  |
| [PhenotypeDescriptor](PhenotypeDescriptor.md) | A descriptor for phenotypes, bindable to Human Phenotype Ontology (HP) |  yes  |
| [AssayDescriptor](AssayDescriptor.md) | A descriptor for assays, bindable to OBI |  yes  |
| [Descriptor](Descriptor.md) | Base class for structured descriptors that allow a preferred term, optional d... |  no  |
| [ProteinComplexDescriptor](ProteinComplexDescriptor.md) | A descriptor for protein complexes that gene products participate in, bindabl... |  yes  |
| [OrganismDescriptor](OrganismDescriptor.md) | A descriptor for organisms, bindable to NCBITaxon |  yes  |
| [GOEnrichmentTerm](GOEnrichmentTerm.md) | GO term enrichment result with statistical metrics |  no  |
| [LifeCycleStageDescriptor](LifeCycleStageDescriptor.md) | A descriptor for parasite life cycle stages, bindable to OPL |  yes  |
| [RegimenDescriptor](RegimenDescriptor.md) | A descriptor for treatment regimens, bindable to NCIT |  yes  |
| [HistopathologyFindingDescriptor](HistopathologyFindingDescriptor.md) | A descriptor for histopathologic findings, bindable to NCIT Morphologic Findi... |  yes  |
| [GeneProductDescriptor](GeneProductDescriptor.md) | A descriptor for gene products (proteins, fusion proteins, oncoproteins), bin... |  yes  |
| [ICD10CMMapping](ICD10CMMapping.md) | ICD-10-CM diagnosis code mapping |  yes  |
| [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) | A descriptor for anatomical locations, bindable to UBERON |  yes  |
| [DiseaseDescriptor](DiseaseDescriptor.md) | A descriptor for the focal disease, bindable to MONDO |  yes  |
| [TriggerDescriptor](TriggerDescriptor.md) | A descriptor for triggers/causes |  yes  |
| [BiologicalProcessDescriptor](BiologicalProcessDescriptor.md) | A descriptor for biological processes, bindable to Gene Ontology (GO) |  yes  |
| [CellularComponentDescriptor](CellularComponentDescriptor.md) | A descriptor for cellular components, bindable to GO cellular component |  yes  |
| [MondoMapping](MondoMapping.md) | MONDO disease ontology mapping |  yes  |
| [CellTypeDescriptor](CellTypeDescriptor.md) | A descriptor for cell types, bindable to Cell Ontology (CL) |  yes  |
| [EnvironmentDescriptor](EnvironmentDescriptor.md) | A descriptor for environmental contexts/settings, bindable to ENVO |  yes  |
| [ConditionDescriptor](ConditionDescriptor.md) | A descriptor for a condition or disease, optionally bound to MONDO |  yes  |
| [TermMapping](TermMapping.md) | Mapping from this disease entry to an external term or code |  yes  |
| [ChemicalEntityDescriptor](ChemicalEntityDescriptor.md) | A descriptor for chemical entities, bindable to CHEBI |  yes  |
| [ICD11FMapping](ICD11FMapping.md) | ICD-11 Foundation diagnosis code mapping |  yes  |
| [TreatmentDescriptor](TreatmentDescriptor.md) | A descriptor for treatments/medical actions, bindable to Medical Action Ontol... |  yes  |
| [ExposureDescriptor](ExposureDescriptor.md) | A descriptor for exposure events, bindable to ECTO or XCO |  yes  |
| [HostDescriptor](HostDescriptor.md) | A descriptor for hosts in an infectious agent life cycle |  no  |
| [CriteriaItem](CriteriaItem.md) | A criterion element (clinical feature, test result, imaging requirement) |  no  |
| [BiomarkerDescriptor](BiomarkerDescriptor.md) | A descriptor for biomarkers, bindable to NCIT |  yes  |
| [InheritanceDescriptor](InheritanceDescriptor.md) | A descriptor for inheritance patterns, bindable to HPO mode of inheritance te... |  yes  |
| [SampleTypeDescriptor](SampleTypeDescriptor.md) | A descriptor for biological sample types (tissue and/or cell type) |  no  |






## Properties

* Range: [Term](Term.md)

* Recommended: True




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