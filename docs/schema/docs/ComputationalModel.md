
# Class: ComputationalModel

A computational or in-silico model relevant to understanding disease mechanisms

URI: [dismech:ComputationalModel](https://w3id.org/monarch-initiative/dismech/ComputationalModel)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneDescriptor],[EvidenceItem],[EvidenceItem]<evidence%200..*-++[ComputationalModel&#124;name:string;description:string%20%3F;model_type:ComputationalModelTypeEnum%20%3F;repository_url:uri%20%3F;model_id:string%20%3F;base_model:string%20%3F;model_software:string%20%3F;model_format:string%20%3F;publication:PMID%20%3F;notes:string%20%3F],[GeneDescriptor]<perturbations%200..*-++[ComputationalModel],[Disease]++-%20computational_models%200..*>[ComputationalModel],[Disease])](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneDescriptor],[EvidenceItem],[EvidenceItem]<evidence%200..*-++[ComputationalModel&#124;name:string;description:string%20%3F;model_type:ComputationalModelTypeEnum%20%3F;repository_url:uri%20%3F;model_id:string%20%3F;base_model:string%20%3F;model_software:string%20%3F;model_format:string%20%3F;publication:PMID%20%3F;notes:string%20%3F],[GeneDescriptor]<perturbations%200..*-++[ComputationalModel],[Disease]++-%20computational_models%200..*>[ComputationalModel],[Disease])

## Referenced by Class

 *  **None** *[computational_models](computational_models.md)*  <sub>0..\*</sub>  **[ComputationalModel](ComputationalModel.md)**

## Attributes


### Own

 * [name](name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
     * Example: Adolescent Nephronophthisis None
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [model_type](model_type.md)  <sub>0..1</sub>
     * Description: Type of computational model
     * Range: [ComputationalModelTypeEnum](ComputationalModelTypeEnum.md)
 * [repository_url](repository_url.md)  <sub>0..1</sub>
     * Description: URL to model repository (GitHub, BiGG, VMH, BioModels)
     * Range: [Uri](types/Uri.md)
 * [model_id](model_id.md)  <sub>0..1</sub>
     * Description: Identifier within the repository (e.g., Recon3D, BIOMD0000000123)
     * Range: [String](types/String.md)
 * [base_model](base_model.md)  <sub>0..1</sub>
     * Description: Parent/base model this is derived from (e.g., Recon3D, Harvey 1.0)
     * Range: [String](types/String.md)
 * [perturbations](perturbations.md)  <sub>0..\*</sub>
     * Description: Gene knockouts, reaction deletions, or parameter changes modeling the disease
     * Range: [GeneDescriptor](GeneDescriptor.md)
 * [model_software](model_software.md)  <sub>0..1</sub>
     * Description: Software/toolbox for running the model (e.g., COBRApy, COBRA Toolbox)
     * Range: [String](types/String.md)
 * [model_format](model_format.md)  <sub>0..1</sub>
     * Description: File format (e.g., SBML, MATLAB, JSON, ONNX)
     * Range: [String](types/String.md)
 * [publication](publication.md)  <sub>0..1</sub>
     * Description: Associated publication (PMID)
     * Range: [PMID](types/PMID.md)
 * [evidence](evidence.md)  <sub>0..\*</sub>
     * Range: [EvidenceItem](EvidenceItem.md)
 * [notes](notes.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Contagious stage where symptoms appear and the bacteria can be spread to others. None

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | Covers genome-scale metabolic models, FBA, kinetic models, digital twins, and ML models |
|  | | Perturbations track gene knockouts or parameter changes used to simulate the disease |
