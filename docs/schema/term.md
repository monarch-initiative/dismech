

# Slot: term 


_Optional structured ontology term reference_





URI: [dismech:term](https://w3id.org/monarch-initiative/dismech/term)
Alias: term

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SampleTypeDescriptor](SampleTypeDescriptor.md) | A descriptor for biological sample types (tissue and/or cell type) |  no  |
| [OrganismDescriptor](OrganismDescriptor.md) | A descriptor for organisms, bindable to NCBITaxon |  yes  |
| [EnvironmentDescriptor](EnvironmentDescriptor.md) | A descriptor for environmental contexts/settings, bindable to ENVO |  yes  |
| [ICD10CMMapping](ICD10CMMapping.md) | ICD-10-CM diagnosis code mapping |  yes  |
| [MondoMapping](MondoMapping.md) | MONDO disease ontology mapping |  yes  |
| [TriggerDescriptor](TriggerDescriptor.md) | A descriptor for triggers/causes |  yes  |
| [TermMapping](TermMapping.md) | Mapping from this disease entry to an external term or code |  yes  |
| [ExposureDescriptor](ExposureDescriptor.md) | A descriptor for exposure events, bindable to ECTO or XCO |  yes  |
| [Descriptor](Descriptor.md) | Base class for structured descriptors that allow a preferred term, optional d... |  no  |
| [RegimenDescriptor](RegimenDescriptor.md) | A descriptor for treatment regimens, bindable to NCIT |  yes  |
| [HistopathologyFindingDescriptor](HistopathologyFindingDescriptor.md) | A descriptor for histopathologic findings, bindable to NCIT Morphologic Findi... |  yes  |
| [GeneDescriptor](GeneDescriptor.md) | A descriptor for genes, bindable to HGNC or other gene databases |  yes  |
| [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) | A descriptor for anatomical locations, bindable to UBERON |  yes  |
| [InheritanceDescriptor](InheritanceDescriptor.md) | A descriptor for inheritance patterns, bindable to HPO mode of inheritance te... |  yes  |
| [CellTypeDescriptor](CellTypeDescriptor.md) | A descriptor for cell types, bindable to Cell Ontology (CL) |  yes  |
| [GOEnrichmentTerm](GOEnrichmentTerm.md) | GO term enrichment result with statistical metrics |  no  |
| [ChemicalEntityDescriptor](ChemicalEntityDescriptor.md) | A descriptor for chemical entities, bindable to CHEBI |  yes  |
| [HostDescriptor](HostDescriptor.md) | A descriptor for hosts in an infectious agent life cycle |  no  |
| [BiomarkerDescriptor](BiomarkerDescriptor.md) | A descriptor for biomarkers, bindable to NCIT |  yes  |
| [ConditionDescriptor](ConditionDescriptor.md) | A descriptor for a condition or disease, optionally bound to MONDO |  yes  |
| [ProteinComplexDescriptor](ProteinComplexDescriptor.md) | A descriptor for protein complexes that gene products participate in, bindabl... |  yes  |
| [CriteriaItem](CriteriaItem.md) | A criterion element (clinical feature, test result, imaging requirement) |  no  |
| [GeneProductDescriptor](GeneProductDescriptor.md) | A descriptor for gene products (proteins, fusion proteins, oncoproteins), bin... |  yes  |
| [DiseaseDescriptor](DiseaseDescriptor.md) | A descriptor for the focal disease, bindable to MONDO |  yes  |
| [LifeCycleStageDescriptor](LifeCycleStageDescriptor.md) | A descriptor for parasite life cycle stages, bindable to OPL |  yes  |
| [TreatmentDescriptor](TreatmentDescriptor.md) | A descriptor for treatments/medical actions, bindable to Medical Action Ontol... |  yes  |
| [CellularComponentDescriptor](CellularComponentDescriptor.md) | A descriptor for cellular components, bindable to GO cellular component |  yes  |
| [ICD11FMapping](ICD11FMapping.md) | ICD-11 Foundation diagnosis code mapping |  yes  |
| [PhenotypeDescriptor](PhenotypeDescriptor.md) | A descriptor for phenotypes, bindable to Human Phenotype Ontology (HP) |  yes  |
| [AssayDescriptor](AssayDescriptor.md) | A descriptor for assays, bindable to OBI |  yes  |
| [BiologicalProcessDescriptor](BiologicalProcessDescriptor.md) | A descriptor for biological processes, bindable to Gene Ontology (GO) |  yes  |






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