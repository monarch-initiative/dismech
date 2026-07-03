

# Class: BiomarkerReadout 


_Links a biochemical biomarker to a pathograph node that it measures, reflects, predicts, or pharmacodynamically reports on. This is an observational readout link, not a causal claim that the biomarker causes the target mechanism or phenotype._





URI: [dismech:class/BiomarkerReadout](https://w3id.org/monarch-initiative/dismech/class/BiomarkerReadout)





```mermaid
 classDiagram
    class BiomarkerReadout
    click BiomarkerReadout href "../../classes/BiomarkerReadout/"
      BiomarkerReadout : description
        
      BiomarkerReadout : direction
        
          
    
        
        
        BiomarkerReadout --> "0..1" BiomarkerReadoutDirectionEnum : direction
        click BiomarkerReadoutDirectionEnum href "../../enums/BiomarkerReadoutDirectionEnum/"
    

        
      BiomarkerReadout : endpoint_context
        
          
    
        
        
        BiomarkerReadout --> "0..1" BiomarkerEndpointContextEnum : endpoint_context
        click BiomarkerEndpointContextEnum href "../../enums/BiomarkerEndpointContextEnum/"
    

        
      BiomarkerReadout : evidence
        
          
    
        
        
        BiomarkerReadout --> "* _recommended_" EvidenceItem : evidence
        click EvidenceItem href "../../classes/EvidenceItem/"
    

        
      BiomarkerReadout : interpretation
        
      BiomarkerReadout : regulatory_endpoint_refs
        
      BiomarkerReadout : relationship
        
          
    
        
        
        BiomarkerReadout --> "1" BiomarkerReadoutRelationshipEnum : relationship
        click BiomarkerReadoutRelationshipEnum href "../../enums/BiomarkerReadoutRelationshipEnum/"
    

        
      BiomarkerReadout : target
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [target](../slots/target.md) | 1 <br/> [String](../types/String.md) | Name of the pathograph node this biomarker reports on | direct |
| [relationship](../slots/relationship.md) | 1 <br/> [BiomarkerReadoutRelationshipEnum](../enums/BiomarkerReadoutRelationshipEnum.md) | How the biomarker relates to the linked pathograph node | direct |
| [direction](../slots/direction.md) | 0..1 <br/> [BiomarkerReadoutDirectionEnum](../enums/BiomarkerReadoutDirectionEnum.md) | Direction of association between biomarker level/presence and the linked even... | direct |
| [endpoint_context](../slots/endpoint_context.md) | 0..1 <br/> [BiomarkerEndpointContextEnum](../enums/BiomarkerEndpointContextEnum.md) | Diagnostic, prognostic, monitoring, pharmacodynamic, or candidate-surrogate u... | direct |
| [regulatory_endpoint_refs](../slots/regulatory_endpoint_refs.md) | * <br/> [String](../types/String.md) | Source-table regulatory endpoint row IDs linked to this readout | direct |
| [interpretation](../slots/interpretation.md) | 0..1 <br/> [String](../types/String.md) | Human-readable interpretation of the link for display and curation review | direct |
| [description](../slots/description.md) | 0..1 <br/> [String](../types/String.md) |  | direct |
| [evidence](../slots/evidence.md) | * _recommended_ <br/> [EvidenceItem](../classes/EvidenceItem.md) | Evidence supporting this biomarker-to-pathograph-node readout link | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Biochemical](../classes/Biochemical.md) | [readouts](../slots/readouts.md) | range | [BiomarkerReadout](../classes/BiomarkerReadout.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:BiomarkerReadout |
| native | dismech:BiomarkerReadout |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BiomarkerReadout
description: Links a biochemical biomarker to a pathograph node that it measures,
  reflects, predicts, or pharmacodynamically reports on. This is an observational
  readout link, not a causal claim that the biomarker causes the target mechanism
  or phenotype.
from_schema: https://w3id.org/monarch-initiative/dismech
slots:
- target
- relationship
- direction
- endpoint_context
- regulatory_endpoint_refs
- interpretation
- description
- evidence
slot_usage:
  target:
    name: target
    description: Name of the pathograph node this biomarker reports on. Prefer a pathophysiology
      entry; phenotype targets are also allowed when the biomarker is explicitly tied
      to a clinical manifestation.
    required: true
  relationship:
    name: relationship
    description: How the biomarker relates to the linked pathograph node.
    required: true
  direction:
    name: direction
    description: Direction of association between biomarker level/presence and the
      linked event or endpoint.
  endpoint_context:
    name: endpoint_context
    description: Diagnostic, prognostic, monitoring, pharmacodynamic, or candidate-surrogate
      use context.
  regulatory_endpoint_refs:
    name: regulatory_endpoint_refs
    description: Source-table regulatory endpoint row IDs linked to this readout.
      Keep regulatory details in the source table; use this field only as a local
      bridge from disease biology to regulatory context.
  interpretation:
    name: interpretation
    description: Human-readable interpretation of the link for display and curation
      review.
  evidence:
    name: evidence
    description: Evidence supporting this biomarker-to-pathograph-node readout link

```
</details>

### Induced

<details>
```yaml
name: BiomarkerReadout
description: Links a biochemical biomarker to a pathograph node that it measures,
  reflects, predicts, or pharmacodynamically reports on. This is an observational
  readout link, not a causal claim that the biomarker causes the target mechanism
  or phenotype.
from_schema: https://w3id.org/monarch-initiative/dismech
slot_usage:
  target:
    name: target
    description: Name of the pathograph node this biomarker reports on. Prefer a pathophysiology
      entry; phenotype targets are also allowed when the biomarker is explicitly tied
      to a clinical manifestation.
    required: true
  relationship:
    name: relationship
    description: How the biomarker relates to the linked pathograph node.
    required: true
  direction:
    name: direction
    description: Direction of association between biomarker level/presence and the
      linked event or endpoint.
  endpoint_context:
    name: endpoint_context
    description: Diagnostic, prognostic, monitoring, pharmacodynamic, or candidate-surrogate
      use context.
  regulatory_endpoint_refs:
    name: regulatory_endpoint_refs
    description: Source-table regulatory endpoint row IDs linked to this readout.
      Keep regulatory details in the source table; use this field only as a local
      bridge from disease biology to regulatory context.
  interpretation:
    name: interpretation
    description: Human-readable interpretation of the link for display and curation
      review.
  evidence:
    name: evidence
    description: Evidence supporting this biomarker-to-pathograph-node readout link
attributes:
  target:
    name: target
    description: Name of the pathograph node this biomarker reports on. Prefer a pathophysiology
      entry; phenotype targets are also allowed when the biomarker is explicitly tied
      to a clinical manifestation.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: target
    owner: BiomarkerReadout
    domain_of:
    - ExperimentalPerturbation
    - ExperimentalReadout
    - CausalEdge
    - TreatmentMechanismTarget
    - ModelMechanismLink
    - BiomarkerReadout
    range: string
    required: true
  relationship:
    name: relationship
    description: How the biomarker relates to the linked pathograph node.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: relationship
    owner: BiomarkerReadout
    domain_of:
    - BiomarkerReadout
    range: BiomarkerReadoutRelationshipEnum
    required: true
  direction:
    name: direction
    description: Direction of association between biomarker level/presence and the
      linked event or endpoint.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: direction
    owner: BiomarkerReadout
    domain_of:
    - ExperimentalReadout
    - BiomarkerReadout
    range: BiomarkerReadoutDirectionEnum
  endpoint_context:
    name: endpoint_context
    description: Diagnostic, prognostic, monitoring, pharmacodynamic, or candidate-surrogate
      use context.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: endpoint_context
    owner: BiomarkerReadout
    domain_of:
    - BiomarkerReadout
    range: BiomarkerEndpointContextEnum
  regulatory_endpoint_refs:
    name: regulatory_endpoint_refs
    description: Source-table regulatory endpoint row IDs linked to this readout.
      Keep regulatory details in the source table; use this field only as a local
      bridge from disease biology to regulatory context.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: regulatory_endpoint_refs
    owner: BiomarkerReadout
    domain_of:
    - BiomarkerReadout
    range: string
    multivalued: true
  interpretation:
    name: interpretation
    description: Human-readable interpretation of the link for display and curation
      review.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: interpretation
    owner: BiomarkerReadout
    domain_of:
    - ExperimentalReadout
    - BiomarkerReadout
    - ReferenceRangeBand
    range: string
  description:
    name: description
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: description
    owner: BiomarkerReadout
    domain_of:
    - Descriptor
    - DietaryModification
    - GeneticContext
    - Dataset
    - ExperimentalModel
    - Experiment
    - ExperimentalPerturbation
    - ExperimentalReadout
    - ExperimentalControl
    - ClinicalTrial
    - ComputationalModel
    - ModelVariable
    - DifferentialDiagnosis
    - Subtype
    - CausalEdge
    - TreatmentMechanismTarget
    - ModelMechanismLink
    - BiomarkerReadout
    - SurrogateEndpointCollection
    - ProteinStructure
    - ExternalAssertion
    - EpidemiologyInfo
    - Pathophysiology
    - Phenotype
    - HistopathologyFinding
    - Environmental
    - Disease
    - Stage
    - AgentLifeCycle
    - AgentLifeCycleStage
    - AnimalModel
    - Treatment
    - InfectiousAgent
    - Transmission
    - Assay
    - Diagnosis
    - Inheritance
    - Variant
    - FunctionalEffect
    - Mechanism
    - ModelingConsideration
    - Definition
    - CriteriaSet
    - ConditionDescriptor
    - GOEnrichment
    - ComorbidityHypothesis
    - UpstreamConditionHypothesis
    - MechanisticHypothesis
    - Grouping
    - GroupingCriteria
    - LogicalCriterion
    - DifferentiatingMechanism
    range: string
  evidence:
    name: evidence
    description: Evidence supporting this biomarker-to-pathograph-node readout link
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: evidence
    owner: BiomarkerReadout
    domain_of:
    - PhenotypeContext
    - Dataset
    - ExperimentalModel
    - Experiment
    - ExperimentalPerturbation
    - ExperimentalReadout
    - ExperimentalControl
    - ClinicalTrial
    - ComputationalModel
    - DifferentialDiagnosis
    - Subtype
    - CausalEdge
    - TreatmentMechanismTarget
    - ModelMechanismLink
    - BiomarkerReadout
    - ReferenceRange
    - SurrogateEndpoint
    - ExternalAssertion
    - Finding
    - Prevalence
    - ProgressionInfo
    - EpidemiologyInfo
    - Pathophysiology
    - Phenotype
    - Biochemical
    - HistopathologyFinding
    - Genetic
    - Environmental
    - Stage
    - AgentLifeCycle
    - AgentLifeCycleStage
    - AnimalModel
    - Treatment
    - InfectiousAgent
    - Transmission
    - Diagnosis
    - Inheritance
    - Variant
    - ModelingConsideration
    - ClassificationAssignment
    - Definition
    - CriteriaSet
    - AssociationSignal
    - AssociationStatistics
    - ComorbidityHypothesis
    - UpstreamConditionHypothesis
    - MechanisticHypothesis
    - Discussion
    - GroupingCriteria
    - GroupingMember
    - DifferentiatingMechanism
    range: EvidenceItem
    recommended: true
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>