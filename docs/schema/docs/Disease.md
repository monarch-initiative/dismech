
# Class: Disease



URI: [dismech:Disease](https://w3id.org/monarch-initiative/dismech/Disease)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Variant],[Treatment],[Transmission],[Subtype],[Stage],[PublicationReference],[ProgressionInfo],[Prevalence],[Phenotype],[Pathophysiology],[ModelingConsideration],[Inheritance],[InfectiousAgent],[Genetic],[EpidemiologyInfo],[Environmental],[DiseaseDescriptor],[CurationEvent]<curation_history%200..*-++[Disease&#124;name:string;description:string%20%3F;category:string%20%3F;parents:string%20*;categories:string%20*;synonyms:string%20*;notes:string%20%3F;review_notes:string%20%3F],[ComputationalModel]<computational_models%200..*-++[Disease],[Dataset]<datasets%200..*-++[Disease],[AnimalModel]<animal_models%200..*-++[Disease],[Inheritance]<inheritance%200..*-++[Disease],[DifferentialDiagnosis]<differential_diagnoses%200..*-++[Disease],[Diagnosis]<diagnosis%200..*-++[Disease],[EpidemiologyInfo]<epidemiology%200..*-++[Disease],[ModelingConsideration]<modeling_considerations%200..*-++[Disease],[Transmission]<transmission%200..*-++[Disease],[InfectiousAgent]<infectious_agent%200..*-++[Disease],[Treatment]<treatments%200..*-++[Disease],[Environmental]<environmental%200..*-++[Disease],[Variant]<variants%200..*-++[Disease],[Genetic]<genetic%200..*-++[Disease],[Stage]<stages%200..*-++[Disease],[Biochemical]<biochemical%200..*-++[Disease],[Phenotype]<phenotypes%200..*-++[Disease],[Pathophysiology]<pathophysiology%200..*-++[Disease],[ProgressionInfo]<progression%200..*-++[Disease],[Prevalence]<prevalence%200..*-++[Disease],[Subtype]<has_subtypes%200..*-++[Disease],[PublicationReference]<references%200..*-++[Disease],[DiseaseDescriptor]<disease_term%200..1-++[Disease],[DiseaseCollection]++-%20diseases%200..*>[Disease],[DiseaseCollection],[DifferentialDiagnosis],[Diagnosis],[Dataset],[CurationEvent],[ComputationalModel],[Biochemical],[AnimalModel])](https://yuml.me/diagram/nofunky;dir:TB/class/[Variant],[Treatment],[Transmission],[Subtype],[Stage],[PublicationReference],[ProgressionInfo],[Prevalence],[Phenotype],[Pathophysiology],[ModelingConsideration],[Inheritance],[InfectiousAgent],[Genetic],[EpidemiologyInfo],[Environmental],[DiseaseDescriptor],[CurationEvent]<curation_history%200..*-++[Disease&#124;name:string;description:string%20%3F;category:string%20%3F;parents:string%20*;categories:string%20*;synonyms:string%20*;notes:string%20%3F;review_notes:string%20%3F],[ComputationalModel]<computational_models%200..*-++[Disease],[Dataset]<datasets%200..*-++[Disease],[AnimalModel]<animal_models%200..*-++[Disease],[Inheritance]<inheritance%200..*-++[Disease],[DifferentialDiagnosis]<differential_diagnoses%200..*-++[Disease],[Diagnosis]<diagnosis%200..*-++[Disease],[EpidemiologyInfo]<epidemiology%200..*-++[Disease],[ModelingConsideration]<modeling_considerations%200..*-++[Disease],[Transmission]<transmission%200..*-++[Disease],[InfectiousAgent]<infectious_agent%200..*-++[Disease],[Treatment]<treatments%200..*-++[Disease],[Environmental]<environmental%200..*-++[Disease],[Variant]<variants%200..*-++[Disease],[Genetic]<genetic%200..*-++[Disease],[Stage]<stages%200..*-++[Disease],[Biochemical]<biochemical%200..*-++[Disease],[Phenotype]<phenotypes%200..*-++[Disease],[Pathophysiology]<pathophysiology%200..*-++[Disease],[ProgressionInfo]<progression%200..*-++[Disease],[Prevalence]<prevalence%200..*-++[Disease],[Subtype]<has_subtypes%200..*-++[Disease],[PublicationReference]<references%200..*-++[Disease],[DiseaseDescriptor]<disease_term%200..1-++[Disease],[DiseaseCollection]++-%20diseases%200..*>[Disease],[DiseaseCollection],[DifferentialDiagnosis],[Diagnosis],[Dataset],[CurationEvent],[ComputationalModel],[Biochemical],[AnimalModel])

## Referenced by Class

 *  **None** *[diseases](diseases.md)*  <sub>0..\*</sub>  **[Disease](Disease.md)**

## Attributes


### Own

 * [name](name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
     * Example: Adolescent Nephronophthisis None
 * [disease_term](disease_term.md)  <sub>0..1</sub>
     * Description: The MONDO disease term for this disease
     * Range: [DiseaseDescriptor](DiseaseDescriptor.md)
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [references](references.md)  <sub>0..\*</sub>
     * Description: Top-level list of references with their key findings for this disease
     * Range: [PublicationReference](PublicationReference.md)
 * [category](category.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Hematologic None
 * [parents](parents.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
     * Example: ['Bacterial Infection'] None
 * [has_subtypes](has_subtypes.md)  <sub>0..\*</sub>
     * Range: [Subtype](Subtype.md)
 * [prevalence](prevalence.md)  <sub>0..\*</sub>
     * Range: [Prevalence](Prevalence.md)
 * [progression](progression.md)  <sub>0..\*</sub>
     * Range: [ProgressionInfo](ProgressionInfo.md)
 * [pathophysiology](pathophysiology.md)  <sub>0..\*</sub>
     * Range: [Pathophysiology](Pathophysiology.md)
 * [phenotypes](phenotypes.md)  <sub>0..\*</sub>
     * Range: [Phenotype](Phenotype.md)
 * [biochemical](biochemical.md)  <sub>0..\*</sub>
     * Range: [Biochemical](Biochemical.md)
 * [stages](stages.md)  <sub>0..\*</sub>
     * Range: [Stage](Stage.md)
 * [genetic](genetic.md)  <sub>0..\*</sub>
     * Range: [Genetic](Genetic.md)
 * [variants](variants.md)  <sub>0..\*</sub>
     * Range: [Variant](Variant.md)
 * [environmental](environmental.md)  <sub>0..\*</sub>
     * Range: [Environmental](Environmental.md)
 * [treatments](treatments.md)  <sub>0..\*</sub>
     * Range: [Treatment](Treatment.md)
 * [categories](categories.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
 * [infectious_agent](infectious_agent.md)  <sub>0..\*</sub>
     * Range: [InfectiousAgent](InfectiousAgent.md)
 * [transmission](transmission.md)  <sub>0..\*</sub>
     * Range: [Transmission](Transmission.md)
 * [modeling_considerations](modeling_considerations.md)  <sub>0..\*</sub>
     * Range: [ModelingConsideration](ModelingConsideration.md)
 * [epidemiology](epidemiology.md)  <sub>0..\*</sub>
     * Range: [EpidemiologyInfo](EpidemiologyInfo.md)
     * Example: ['Global'] None
 * [diagnosis](diagnosis.md)  <sub>0..\*</sub>
     * Range: [Diagnosis](Diagnosis.md)
 * [differential_diagnoses](differential_diagnoses.md)  <sub>0..\*</sub>
     * Description: Differential diagnoses - similar diseases that must be ruled out
     * Range: [DifferentialDiagnosis](DifferentialDiagnosis.md)
 * [synonyms](synonyms.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
     * Example: ['CYFRA 21-1'] None
 * [inheritance](inheritance.md)  <sub>0..\*</sub>
     * Range: [Inheritance](Inheritance.md)
     * Example: Autosomal Dominant None
 * [animal_models](animal_models.md)  <sub>0..\*</sub>
     * Range: [AnimalModel](AnimalModel.md)
 * [datasets](datasets.md)  <sub>0..\*</sub>
     * Description: Publicly available datasets relevant to disease research
     * Range: [Dataset](Dataset.md)
 * [computational_models](computational_models.md)  <sub>0..\*</sub>
     * Description: Computational models (metabolic, mechanistic, ML, digital twins) for this disease
     * Range: [ComputationalModel](ComputationalModel.md)
 * [notes](notes.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Contagious stage where symptoms appear and the bacteria can be spread to others. None
 * [review_notes](review_notes.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Added an additional clinically relevant subtype. None
 * [curation_history](curation_history.md)  <sub>0..\*</sub>
     * Description: Audit trail of AI-assisted curation events
     * Range: [CurationEvent](CurationEvent.md)
