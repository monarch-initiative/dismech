# Disorder Mechanisms Knowledge Base Schema

Disease Pathophysiology Knowledge Base Schema

URI: https://w3id.org/monarch-initiative/dismech

Name: dismech



## Classes

| Class | Description |
| --- | --- |
| [AgentLifeCycle](classes/AgentLifeCycle.md) |  |
| [AgentLifeCycleStage](classes/AgentLifeCycleStage.md) |  |
| [AnimalModel](classes/AnimalModel.md) |  |
| [AntisenseOligonucleotideDetail](classes/AntisenseOligonucleotideDetail.md) | Structured attributes specific to an antisense oligonucleotide (ASO) treatmen... |
| [Any](classes/Any.md) |  |
| [Assay](classes/Assay.md) |  |
| [AssociationMetric](classes/AssociationMetric.md) | Quantitative association metric and its uncertainty |
| [AssociationSignal](classes/AssociationSignal.md) | An association signal from EHR, registry, or computational sources, optionall... |
| [AssociationStatistics](classes/AssociationStatistics.md) | Statistical summary with evidence for an association signal |
| [Biochemical](classes/Biochemical.md) |  |
| [BiomarkerReadout](classes/BiomarkerReadout.md) | Links a biochemical biomarker to a pathograph node that it measures, reflects... |
| [CausalEdge](classes/CausalEdge.md) | A reference to a downstream effect or consequence in a causal relationship |
| [ClassificationAssignment](classes/ClassificationAssignment.md) | Base class for classification assignments with evidence |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChannelopathyAssignment](classes/ChannelopathyAssignment.md) | Channelopathy organ system classification assignment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HarrisonsChapterAssignment](classes/HarrisonsChapterAssignment.md) | Harrison's internal medicine chapter classification assignment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ICDOMorphologyAssignment](classes/ICDOMorphologyAssignment.md) | ICD-O morphology classification assignment for neoplastic diseases |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IUISAssignment](classes/IUISAssignment.md) | IUIS primary immunodeficiency classification assignment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LysosomalStorageAssignment](classes/LysosomalStorageAssignment.md) | Lysosomal storage disease biochemical classification assignment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MechanisticNosologyAssignment](classes/MechanisticNosologyAssignment.md) | Mechanistic/pathway-based disease classification assignment |
| [ClinicalTrial](classes/ClinicalTrial.md) | A clinical trial relevant to treatment or research of a disease |
| [ComorbidityAssociation](classes/ComorbidityAssociation.md) | An association between two conditions, including directionality, evidence, an... |
| [ComorbidityHypothesis](classes/ComorbidityHypothesis.md) | Mechanistic hypothesis for a comorbidity association, with rich text and embe... |
| [ComputationalModel](classes/ComputationalModel.md) | A computational or in-silico model relevant to understanding disease mechanis... |
| [CriteriaSet](classes/CriteriaSet.md) | A named criteria grouping within a definition |
| [CurationEvent](classes/CurationEvent.md) | A single curation event in the audit trail |
| [Dataset](classes/Dataset.md) | A reference to a publicly available omics or phenotype dataset |
| [Definition](classes/Definition.md) | A diagnostic or phenotype definition for the disease |
| [Demographics](classes/Demographics.md) | Demographic stratification for an association signal |
| [Descriptor](classes/Descriptor.md) | Base class for structured descriptors that allow a preferred term, optional d... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AnatomicalEntityDescriptor](classes/AnatomicalEntityDescriptor.md) | A descriptor for anatomical locations, bindable to UBERON |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AssayDescriptor](classes/AssayDescriptor.md) | A descriptor for assays, bindable to OBI |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiologicalProcessDescriptor](classes/BiologicalProcessDescriptor.md) | A descriptor for biological processes, bindable to Gene Ontology (GO) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiomarkerDescriptor](classes/BiomarkerDescriptor.md) | A descriptor for biomarkers, bindable to NCIT |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CellTypeDescriptor](classes/CellTypeDescriptor.md) | A descriptor for cell types, bindable to Cell Ontology (CL) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CellularComponentDescriptor](classes/CellularComponentDescriptor.md) | A descriptor for cellular components, bindable to GO cellular component |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalEntityDescriptor](classes/ChemicalEntityDescriptor.md) | A descriptor for chemical entities, bindable to CHEBI |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ConditionDescriptor](classes/ConditionDescriptor.md) | A descriptor for a condition or disease, optionally bound to MONDO |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CriteriaItem](classes/CriteriaItem.md) | A criterion element (clinical feature, test result, imaging requirement) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiseaseDescriptor](classes/DiseaseDescriptor.md) | A descriptor for the focal disease, bindable to MONDO |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EnvironmentDescriptor](classes/EnvironmentDescriptor.md) | A descriptor for environmental contexts/settings, bindable to ENVO |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExposureDescriptor](classes/ExposureDescriptor.md) | A descriptor for exposure events, bindable to ECTO or XCO |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FoodDescriptor](classes/FoodDescriptor.md) | A descriptor for foods, beverages, nutrients, minerals, and supplements, bind... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneDescriptor](classes/GeneDescriptor.md) | A descriptor for genes, bindable to HGNC or other gene databases |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneProductDescriptor](classes/GeneProductDescriptor.md) | A descriptor for gene products (proteins, fusion proteins, oncoproteins), bin... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HistopathologyFindingDescriptor](classes/HistopathologyFindingDescriptor.md) | A descriptor for histopathologic findings, bindable to NCIT Morphologic Findi... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[InheritanceDescriptor](classes/InheritanceDescriptor.md) | A descriptor for inheritance patterns, bindable to HPO mode of inheritance te... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LifeCycleStageDescriptor](classes/LifeCycleStageDescriptor.md) | A descriptor for parasite life cycle stages, bindable to OPL |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ModelVariableDescriptor](classes/ModelVariableDescriptor.md) | A descriptor mapping a model variable to an ontology term (LOINC, CHEBI, HP, ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MolecularFunctionDescriptor](classes/MolecularFunctionDescriptor.md) | A descriptor for molecular functions, bindable to Gene Ontology (GO) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OrganismDescriptor](classes/OrganismDescriptor.md) | A descriptor for organisms, bindable to NCBITaxon |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HostDescriptor](classes/HostDescriptor.md) | A descriptor for hosts in an infectious agent life cycle |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PhenotypeDescriptor](classes/PhenotypeDescriptor.md) | A descriptor for phenotypes, bindable to Human Phenotype Ontology (HP) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProteinComplexDescriptor](classes/ProteinComplexDescriptor.md) | A descriptor for protein complexes that gene products participate in, bindabl... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RegimenDescriptor](classes/RegimenDescriptor.md) | A descriptor for treatment regimens, bindable to NCIT |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SampleTypeDescriptor](classes/SampleTypeDescriptor.md) | A descriptor for biological sample types (tissue and/or cell type) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SubtypeDescriptor](classes/SubtypeDescriptor.md) | A descriptor for disease subtypes, bindable to MONDO disease terms or NCIT on... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TreatmentDescriptor](classes/TreatmentDescriptor.md) | A descriptor for treatments/medical actions, bindable to MAXO or NCIT clinica... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TriggerDescriptor](classes/TriggerDescriptor.md) | A descriptor for triggers/causes |
| [Diagnosis](classes/Diagnosis.md) |  |
| [DietaryModification](classes/DietaryModification.md) | A structured dietary addition, restriction, avoidance, or substitution used t... |
| [DifferentialDiagnosis](classes/DifferentialDiagnosis.md) | A disease or condition that presents similarly to the focal disease and must ... |
| [DifferentiatingMechanism](classes/DifferentiatingMechanism.md) | A mechanism or feature that distinguishes a grouping member from its siblings... |
| [Discussion](classes/Discussion.md) | A thread-like record of an open question, controversy, curation todo, emergin... |
| [Disease](classes/Disease.md) |  |
| [DiseaseClassifications](classes/DiseaseClassifications.md) | Container for all classification assignments for a disease |
| [DiseaseCollection](classes/DiseaseCollection.md) |  |
| [DiseaseMappings](classes/DiseaseMappings.md) | Container for external identifier mappings for a disease or subtype |
| [Environmental](classes/Environmental.md) | An environmental factor, exposure, or context relevant to disease |
| [EpidemiologyInfo](classes/EpidemiologyInfo.md) |  |
| [EvidenceItem](classes/EvidenceItem.md) |  |
| [Experiment](classes/Experiment.md) | A structured experiment or protocol-level study design that can be proposed t... |
| [ExperimentalControl](classes/ExperimentalControl.md) | A comparator or control condition for an experiment, such as an isogenic wild... |
| [ExperimentalModel](classes/ExperimentalModel.md) | A disease-relevant non-animal experimental model system |
| [ExperimentalPerturbation](classes/ExperimentalPerturbation.md) | A structured perturbation, intervention, or exposure used in an experiment |
| [ExperimentalReadout](classes/ExperimentalReadout.md) | A structured readout or outcome measured in an experiment |
| [ExternalAssertion](classes/ExternalAssertion.md) | An externally curated assertion or registry record relevant to a disease or v... |
| [Finding](classes/Finding.md) | A key finding or claim extracted from a source (publication or dataset) |
| [FunctionalEffect](classes/FunctionalEffect.md) | Describes the functional consequence of a genetic variant, including regulato... |
| [Genetic](classes/Genetic.md) |  |
| [GeneticContext](classes/GeneticContext.md) | A structured description of a genetic context that modifies phenotype frequen... |
| [GOEnrichment](classes/GOEnrichment.md) | GO enrichment results for an association signal |
| [GOEnrichmentTerm](classes/GOEnrichmentTerm.md) | GO term enrichment result with statistical metrics |
| [Grouping](classes/Grouping.md) | An explicit, curated union of distinct Disease entries assembled below the le... |
| [GroupingCriteria](classes/GroupingCriteria.md) | The shared membership criteria for a grouping, pairing a human-readable descr... |
| [GroupingMember](classes/GroupingMember.md) | One member of a grouping, referenced by foreign key, together with the mechan... |
| [HistopathologyFinding](classes/HistopathologyFinding.md) | A histopathologic finding from microscopic examination of tissue |
| [InfectiousAgent](classes/InfectiousAgent.md) |  |
| [Inheritance](classes/Inheritance.md) |  |
| [LogicalCriterion](classes/LogicalCriterion.md) | A node in a nested boolean membership-criteria expression |
| [MappingConsistency](classes/MappingConsistency.md) | Consistency assertion for a mapping relative to another source |
| [Mechanism](classes/Mechanism.md) |  |
| [MechanisticHypothesis](classes/MechanisticHypothesis.md) | Disease-level hypothesis metadata used to organize downstream causal edges in... |
| [ModelingConsideration](classes/ModelingConsideration.md) |  |
| [ModelMechanismLink](classes/ModelMechanismLink.md) | Links an experimental model to a specific pathophysiology mechanism node, wit... |
| [ModelVariable](classes/ModelVariable.md) | A variable in a computational model, identified by a human-readable name, wit... |
| [OnsetDescriptor](classes/OnsetDescriptor.md) | Structured description of age of onset |
| [Pathophysiology](classes/Pathophysiology.md) |  |
| [Phenotype](classes/Phenotype.md) |  |
| [PhenotypeContext](classes/PhenotypeContext.md) | A context-specific annotation qualifying how a phenotype manifests under part... |
| [Prevalence](classes/Prevalence.md) |  |
| [ProgressionInfo](classes/ProgressionInfo.md) |  |
| [ProteinStructure](classes/ProteinStructure.md) | A 3D protein structure from PDB or AlphaFold relevant to understanding a trea... |
| [PublicationReference](classes/PublicationReference.md) | A reference to a publication with associated findings |
| [Qualifier](classes/Qualifier.md) | A predicate-value pair for formal post-composition |
| [ReferenceRange](classes/ReferenceRange.md) | A population reference interval for a clinical laboratory analyte |
| [ReferenceRangeBand](classes/ReferenceRangeBand.md) | A single graded interpretation band within a reference range, mapping a value... |
| [SeverityTier](classes/SeverityTier.md) | A threshold-severity pair defining one tier in a severity scale |
| [Stage](classes/Stage.md) |  |
| [Subtype](classes/Subtype.md) |  |
| [SurrogateEndpoint](classes/SurrogateEndpoint.md) | A regulatory surrogate endpoint assertion curated from FDA's surrogate endpoi... |
| [SurrogateEndpointCollection](classes/SurrogateEndpointCollection.md) | A source-level collection of curated regulatory surrogate endpoint assertions |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FDASurrogateEndpointCollection](classes/FDASurrogateEndpointCollection.md) | FDA surrogate endpoint table import preserving row-level source provenance |
| [Term](classes/Term.md) | A structured reference to an ontology term |
| [TermMapping](classes/TermMapping.md) | Mapping from this disease entry to an external term or code |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ICD10CMMapping](classes/ICD10CMMapping.md) | ICD-10-CM diagnosis code mapping |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ICD11FMapping](classes/ICD11FMapping.md) | ICD-11 Foundation diagnosis code mapping |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MondoMapping](classes/MondoMapping.md) | MONDO disease ontology mapping |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NCITMapping](classes/NCITMapping.md) | NCIT disease, subtype, or disease/finding ontology mapping for cancer entries |
| [TrackedIssue](classes/TrackedIssue.md) | Structured pointer to an external tracker issue (typically a GitHub issue) us... |
| [Transmission](classes/Transmission.md) |  |
| [Treatment](classes/Treatment.md) |  |
| [TreatmentMechanismTarget](classes/TreatmentMechanismTarget.md) | Links a treatment to a specific pathophysiology mechanism node it targets |
| [UpstreamConditionHypothesis](classes/UpstreamConditionHypothesis.md) | Hypothesized upstream condition that may explain both A and B |
| [Variant](classes/Variant.md) | A genetic variant associated with a disease, including coding and non-coding ... |



## Slots

| Slot | Description |
| --- | --- |
| [a_before_b](slots/a_before_b.md) | Probability or fraction of A before B in an EHR signal |
| [abnormal_flag](slots/abnormal_flag.md) | Categorical abnormal-result flag for a reference-range band, following HL7/LO... |
| [accession](slots/accession.md) | Dataset accession identifier as a CURIE (e |
| [action](slots/action.md) | The dietary action being applied |
| [action_category](slots/action_category.md) | Optional high-level category for a clinical action in the treatments section |
| [additional_requirements](slots/additional_requirements.md) | Additional requirements used in a criteria set |
| [affected_cell_types](slots/affected_cell_types.md) | Cell types in which gene expression is specifically gained or lost |
| [affected_developmental_stage](slots/affected_developmental_stage.md) | Developmental stage or temporal window in which expression is modularly lost ... |
| [age_range](slots/age_range.md) | Age range or stratification, if applicable |
| [agent_life_cycle](slots/agent_life_cycle.md) |  |
| [allele_type](slots/allele_type.md) | Type of allele or mutation (e |
| [alleles](slots/alleles.md) |  |
| [allelic_events](slots/allelic_events.md) | Event types affecting the allele or locus |
| [allelic_hit_role](slots/allelic_hit_role.md) | Role of the alteration in a multi-hit mechanism, such as first hit, second hi... |
| [animal_models](slots/animal_models.md) |  |
| [applies_to_subtypes](slots/applies_to_subtypes.md) | Disease subtypes for which this hypothesis is intended to apply |
| [approval_type](slots/approval_type.md) | FDA approval pathway context for the surrogate endpoint row |
| [aso_chemistry](slots/aso_chemistry.md) | Backbone / sugar chemistry of an antisense oligonucleotide |
| [aso_details](slots/aso_details.md) | Structured detail specific to antisense oligonucleotide treatments |
| [aso_mechanism](slots/aso_mechanism.md) | Molecular mechanism of action of an antisense oligonucleotide |
| [assays](slots/assays.md) |  |
| [assertion_type](slots/assertion_type.md) | Type/category of the external assertion or registry record |
| [associated_phenotypes](slots/associated_phenotypes.md) |  |
| [association](slots/association.md) | Free-text descriptor of how the gene is associated with the disease |
| [association_signals](slots/association_signals.md) | Association signals from EHR, registry, or computational sources |
| [attaches_to](slots/attaches_to.md) | Multivalued list of entity references pointing at the disease nodes, gaps, ph... |
| [b_before_a](slots/b_before_a.md) | Probability or fraction of B before A in an EHR signal |
| [background](slots/background.md) |  |
| [base_model](slots/base_model.md) | Parent/base model this is derived from (e |
| [biochemical](slots/biochemical.md) |  |
| [biological_processes](slots/biological_processes.md) |  |
| [biomarker_term](slots/biomarker_term.md) | Ontology term for a biomarker (from NCIT) |
| [categories](slots/categories.md) |  |
| [category](slots/category.md) |  |
| [causal_link_type](slots/causal_link_type.md) | Whether this edge is direct or indirect, and whether omitted intermediates ar... |
| [cell_source](slots/cell_source.md) | Source of cells used in the experimental model |
| [cell_type_term](slots/cell_type_term.md) | CL term for the cell type |
| [cell_types](slots/cell_types.md) |  |
| [cellular_components](slots/cellular_components.md) |  |
| [channelopathy_category](slots/channelopathy_category.md) | Channelopathy organ system classification |
| [chemical_entities](slots/chemical_entities.md) |  |
| [chemicals](slots/chemicals.md) |  |
| [children](slots/children.md) | Names of other subtypes in this list that are members/children of this groupi... |
| [classification](slots/classification.md) | Classification scheme this subtype belongs to (e |
| [classification_value](slots/classification_value.md) | The classification value assigned |
| [classifications](slots/classifications.md) | Classification assignments for this disease from various nosologies |
| [clinical_benefit](slots/clinical_benefit.md) | Specific clinical benefit, clinical outcome, or direct endpoint predicted by ... |
| [clinical_benefit_linkage](slots/clinical_benefit_linkage.md) | How the surrogate endpoint is linked to clinical benefit in the regulatory co... |
| [clinical_benefit_linkage_basis](slots/clinical_benefit_linkage_basis.md) | Explanation of how the clinical-benefit linkage was inferred or curated |
| [clinical_course](slots/clinical_course.md) | Clinical course qualifier for this descriptor (e |
| [clinical_significance](slots/clinical_significance.md) |  |
| [clinical_trials](slots/clinical_trials.md) | Clinical trials relevant to disease treatment and research |
| [code](slots/code.md) | Code within the specified code system |
| [code_system](slots/code_system.md) | Code system used for a condition reference (e |
| [combined_score](slots/combined_score.md) | Combined score used by an enrichment method |
| [complementation_group](slots/complementation_group.md) | Complementation group designation (e |
| [components](slots/components.md) | Component conditions that make up a composite descriptor |
| [composition](slots/composition.md) | Composition type for a composite condition descriptor |
| [computational_models](slots/computational_models.md) | Computational models (metabolic, mechanistic, ML, digital twins) for this dis... |
| [conditions](slots/conditions.md) | Experimental conditions or disease states represented |
| [conforms_to](slots/conforms_to.md) | Reference to a mechanism module that this pathophysiology node is an organ-sp... |
| [conjugation](slots/conjugation.md) | Targeting ligand or conjugate attached to an antisense oligonucleotide |
| [consequence](slots/consequence.md) |  |
| [consequences](slots/consequences.md) |  |
| [consistency](slots/consistency.md) | Consistency assertions for this mapping against other sources |
| [consistent](slots/consistent.md) | Consistency status for a mapping relative to a reference source |
| [context](slots/context.md) |  |
| [context_of_use](slots/context_of_use.md) | Concise context-of-use statement combining disease/use, population, endpoint,... |
| [controls](slots/controls.md) | Experimental controls, comparators, or counterfactual arms |
| [core_clinical_characteristics](slots/core_clinical_characteristics.md) | Core clinical characteristics used in a criteria set |
| [creation_date](slots/creation_date.md) | ISO 8601/RFC 3339 timestamp string for when this disease entry was first crea... |
| [criteria_semantics](slots/criteria_semantics.md) | The logical relationship between this criteria block and grouping membership ... |
| [criteria_sets](slots/criteria_sets.md) | Named criteria groupings within a definition |
| [criterion_predicate](slots/criterion_predicate.md) | The constraint kind for a leaf node in a membership-criteria expression |
| [culture_system](slots/culture_system.md) | Culture format or device context used by the experimental model |
| [curation_action](slots/curation_action.md) | Type of curation action performed |
| [curation_description](slots/curation_description.md) | Human-readable description of changes made |
| [curation_history](slots/curation_history.md) | Audit trail of AI-assisted curation events |
| [curation_model](slots/curation_model.md) | Model identifier used for curation (e |
| [curation_status](slots/curation_status.md) | Curation workflow status |
| [curation_timestamp](slots/curation_timestamp.md) | ISO 8601 timestamp of the curation event |
| [data_type](slots/data_type.md) | The type of omics or other data in the dataset |
| [dataset_identifier](slots/dataset_identifier.md) | Native identifier for this variable in the source dataset or model (e |
| [datasets](slots/datasets.md) | Publicly available datasets relevant to disease research |
| [de_novo_rate](slots/de_novo_rate.md) | Estimated percentage of de novo cases (e |
| [decision_criterion](slots/decision_criterion.md) | Pre-specified qualitative or quantitative criterion for interpreting the expe... |
| [definition_type](slots/definition_type.md) | The type of definition or criteria set |
| [definitions](slots/definitions.md) | Definitions or diagnostic criteria for this disease |
| [demographics](slots/demographics.md) | Demographic stratification for an association signal |
| [description](slots/description.md) |  |
| [diagnosis](slots/diagnosis.md) |  |
| [diagnosis_term](slots/diagnosis_term.md) | The MAXO term for this diagnostic procedure |
| [diagnostic](slots/diagnostic.md) |  |
| [dietary_modifications](slots/dietary_modifications.md) | Structured dietary additions, restrictions, avoidances, or substitutions asso... |
| [differential_diagnoses](slots/differential_diagnoses.md) | Differential diagnoses - similar diseases that must be ruled out |
| [differentiating_mechanisms](slots/differentiating_mechanisms.md) | Mechanisms or features that distinguish this member from its siblings in the ... |
| [direction](slots/direction.md) | Direction of association between the biomarker value/presence and the linked ... |
| [directionality](slots/directionality.md) | Direction of a comorbidity/trajectory association |
| [discussion_id](slots/discussion_id.md) | Stable identifier for a Discussion, used as the target of cross-references |
| [discussions](slots/discussions.md) | Open or recently-resolved discussion items attached to this entry |
| [disease_a](slots/disease_a.md) | First disease in a comorbidity pair |
| [disease_b](slots/disease_b.md) | Second disease in a comorbidity pair |
| [disease_or_use](slots/disease_or_use.md) | FDA disease or use text for a surrogate endpoint row |
| [disease_term](slots/disease_term.md) | The MONDO disease term for this disease |
| [diseases](slots/diseases.md) |  |
| [disorder_a_count](slots/disorder_a_count.md) | Number of records/patients carrying disorder A in the source dataset |
| [disorder_b_count](slots/disorder_b_count.md) | Number of records/patients carrying disorder B in the source dataset |
| [display_name](slots/display_name.md) | Human-readable display name for a subtype, used when the name (which serves a... |
| [distinguishing_features](slots/distinguishing_features.md) | Key clinical, laboratory, imaging, or epidemiological features that help diff... |
| [downstream](slots/downstream.md) |  |
| [drug_mechanism_of_action](slots/drug_mechanism_of_action.md) | FDA drug mechanism-of-action context for the surrogate endpoint row |
| [duration](slots/duration.md) |  |
| [duration_days](slots/duration_days.md) |  |
| [effect](slots/effect.md) |  |
| [endpoint_context](slots/endpoint_context.md) | Endpoint or use context for a biomarker readout link |
| [endpoint_validation_level](slots/endpoint_validation_level.md) | BEST-aligned validation level inferred or curated for the surrogate endpoint |
| [environment_context](slots/environment_context.md) | The ENVO term for the environmental context/setting |
| [environmental](slots/environmental.md) |  |
| [epidemiology](slots/epidemiology.md) |  |
| [evidence](slots/evidence.md) |  |
| [evidence_source](slots/evidence_source.md) | Origin of the evidence item (human clinical, model organism, in vitro, or com... |
| [examples](slots/examples.md) |  |
| [exclusion_criteria](slots/exclusion_criteria.md) | Exclusion criteria for a definition or criteria set |
| [experiment_id](slots/experiment_id.md) | Stable identifier for an Experiment within a disease entry |
| [experiment_type](slots/experiment_type.md) | Ontology-backed descriptor for the overall experiment or study design |
| [experimental_model_type](slots/experimental_model_type.md) | Broad category for an experimental model system |
| [experimental_models](slots/experimental_models.md) | Disease-relevant organoids, cell lines, chip systems, cocultures, and related... |
| [explanation](slots/explanation.md) |  |
| [exposure_term](slots/exposure_term.md) | The ECTO/XCO term for this exposure event |
| [exposures](slots/exposures.md) | Environmental exposures studied in the dataset |
| [expressivity](slots/expressivity.md) | Expressivity classification for this inheritance pattern |
| [external_assertions](slots/external_assertions.md) | External curated assertions or registry records relevant to this entity |
| [external_id](slots/external_id.md) | Identifier used by the external resource (e |
| [factors](slots/factors.md) |  |
| [fdr](slots/fdr.md) | FDR-adjusted p-value for an association or enrichment |
| [features](slots/features.md) |  |
| [finding_term](slots/finding_term.md) | Ontology term for a histopathologic finding (from NCIT or HP) |
| [findings](slots/findings.md) | Key findings or claims extracted from this source (publication or dataset) |
| [food](slots/food.md) | The FOODON-bound food or beverage targeted by a dietary modification |
| [food_source](slots/food_source.md) | The FOODON or CHEBI term for a specific food, beverage, nutrient, mineral, or... |
| [footnotes](slots/footnotes.md) | FDA workbook footnote semantics attached to the source row |
| [found_in](slots/found_in.md) | Deep-research output files where this reference was cited |
| [frequency](slots/frequency.md) |  |
| [function](slots/function.md) |  |
| [functional_effects](slots/functional_effects.md) |  |
| [functional_impact](slots/functional_impact.md) | Functional consequence of the genetic variant (e |
| [functional_impact_category](slots/functional_impact_category.md) | Controlled functional impact category for a genetic context |
| [gene](slots/gene.md) |  |
| [gene_products](slots/gene_products.md) | Gene products (proteins, fusion proteins, oncoproteins) involved in this path... |
| [gene_term](slots/gene_term.md) | The HGNC term for this gene |
| [genes](slots/genes.md) |  |
| [genetic](slots/genetic.md) |  |
| [genetic_context](slots/genetic_context.md) | The genetic context under which this qualification applies |
| [genotype](slots/genotype.md) |  |
| [geography](slots/geography.md) |  |
| [go_enrichment](slots/go_enrichment.md) | GO enrichment results associated with a signal |
| [go_terms](slots/go_terms.md) | GO term enrichment results |
| [grouping_basis](slots/grouping_basis.md) | The axis or axes on which this grouping is drawn (records why the members bel... |
| [grouping_rationale](slots/grouping_rationale.md) | Free-text justification for the grouping boundary: why these members are grou... |
| [harrisons_chapter](slots/harrisons_chapter.md) | Harrison's internal medicine chapter classification |
| [has_subtypes](slots/has_subtypes.md) |  |
| [histopathology](slots/histopathology.md) | Histopathologic findings including microscopic morphology, architectural patt... |
| [hosts](slots/hosts.md) |  |
| [hypotheses](slots/hypotheses.md) | Mechanistic or causal hypotheses about the association |
| [hypothesis_group_id](slots/hypothesis_group_id.md) | Stable identifier for a disease-level mechanistic hypothesis grouping |
| [hypothesis_groups](slots/hypothesis_groups.md) | Hypothesis identifiers or grouping labels that this edge belongs to |
| [hypothesis_label](slots/hypothesis_label.md) | Human-readable label/title for a mechanistic hypothesis |
| [icd10cm_mappings](slots/icd10cm_mappings.md) | ICD-10-CM code mappings for this disease |
| [icd11f_mappings](slots/icd11f_mappings.md) | ICD-11 Foundation code mappings for this disease |
| [icdo_morphology](slots/icdo_morphology.md) | ICD-O morphology classification (for neoplastic diseases) |
| [id](slots/id.md) | Ontology term identifier (CURIE) |
| [identifiers](slots/identifiers.md) |  |
| [images](slots/images.md) | Relative paths to image files (figures, charts, micrographs) sourced from dee... |
| [imaging_requirements](slots/imaging_requirements.md) | Imaging requirements used in a criteria set |
| [inclusion_criteria](slots/inclusion_criteria.md) | Inclusion criteria for a definition or criteria set |
| [incubation_days](slots/incubation_days.md) |  |
| [incubation_years](slots/incubation_years.md) |  |
| [infectious_agent](slots/infectious_agent.md) |  |
| [infectious_agent_term](slots/infectious_agent_term.md) | The NCBITaxon term for this infectious agent |
| [inheritance](slots/inheritance.md) |  |
| [inheritance_term](slots/inheritance_term.md) | The HPO mode of inheritance term for this inheritance pattern |
| [intermediate_mechanisms](slots/intermediate_mechanisms.md) | Known or suspected intermediate mechanisms omitted from this edge for graph c... |
| [interpretation](slots/interpretation.md) | Curator-facing explanation of how to interpret the biomarker relative to the ... |
| [interpretation_bands](slots/interpretation_bands.md) | Ordered graded interpretation bands that partition a measurement scale into c... |
| [iuis_category](slots/iuis_category.md) | IUIS primary immunodeficiency classification |
| [kind](slots/kind.md) | Categorical type of a Discussion (narrowed via slot_usage to DiscussionKindEn... |
| [label](slots/label.md) | Human-readable label for the ontology term |
| [laboratory_requirements](slots/laboratory_requirements.md) | Laboratory or serologic requirements used in a criteria set |
| [laterality](slots/laterality.md) | Laterality qualifier (left, right, or bilateral) |
| [life_cycle_stage_term](slots/life_cycle_stage_term.md) | The OPL term for this agent life cycle stage |
| [life_cycle_stages](slots/life_cycle_stages.md) |  |
| [ligand](slots/ligand.md) | Name of bound drug/ligand if this is a co-crystal structure |
| [limited_precision](slots/limited_precision.md) | Whether the signal has limited statistical precision due to small co-occurren... |
| [literature_evidence](slots/literature_evidence.md) | Literature-based evidence items for this association |
| [located_in](slots/located_in.md) | Anatomical location where this entity/process occurs or procedure is performe... |
| [locations](slots/locations.md) |  |
| [logic](slots/logic.md) | Root of the structured (boolean/nested) membership-criteria expression for th... |
| [loinc_term](slots/loinc_term.md) | LOINC code for a measured analyte or clinical observation (e |
| [lower_bound](slots/lower_bound.md) | Lower bound of a reference interval (inclusive) |
| [lysosomal_storage_category](slots/lysosomal_storage_category.md) | Lysosomal storage disease biochemical classification |
| [mapped_disease_files](slots/mapped_disease_files.md) | Relative paths of dismech disease YAML files mapped or candidate-mapped to th... |
| [mapped_diseases](slots/mapped_diseases.md) | Names of dismech disease entries mapped or candidate-mapped to this FDA row |
| [mapping_justification](slots/mapping_justification.md) | Brief rationale or justification for the mapping |
| [mapping_notes](slots/mapping_notes.md) | Notes on code-to-concept mapping decisions for this signal |
| [mapping_predicate](slots/mapping_predicate.md) | Relationship between this disease and the mapped term (e |
| [mapping_source](slots/mapping_source.md) | Source of the mapping (e |
| [mapping_status](slots/mapping_status.md) | Status of mapping the FDA disease/use row to dismech disease entries |
| [mappings](slots/mappings.md) | External identifier mappings for this disease or subtype (SSSOM-inspired) |
| [mappings_list](slots/mappings_list.md) | Ontology term mappings for a model variable (LOINC, CHEBI, HP, etc |
| [markers](slots/markers.md) |  |
| [max_age_years](slots/max_age_years.md) | Maximum (latest) age of onset in years |
| [maximum_value](slots/maximum_value.md) |  |
| [mean_age_years](slots/mean_age_years.md) | Mean age of onset in years, as reported in a cohort study |
| [mean_range](slots/mean_range.md) |  |
| [mechanism](slots/mechanism.md) |  |
| [mechanism_confidence](slots/mechanism_confidence.md) | Level of confidence in this pathophysiology mechanism |
| [mechanisms](slots/mechanisms.md) |  |
| [mechanistic_category](slots/mechanistic_category.md) | Mechanistic/pathway-based disease classification |
| [mechanistic_hypotheses](slots/mechanistic_hypotheses.md) | Disease-level mechanistic hypotheses that group and annotate causal edges |
| [member](slots/member.md) | Foreign key to the grouped entity |
| [member_type](slots/member_type.md) | The kind of entity referenced by this member |
| [members](slots/members.md) | The explicit members of this grouping (the union it groups; points down to in... |
| [membership_criteria](slots/membership_criteria.md) | The shared criteria a Disease must satisfy to belong to this grouping, expres... |
| [method](slots/method.md) | Method or pipeline name |
| [metric_ci_lower](slots/metric_ci_lower.md) | Lower confidence interval bound |
| [metric_ci_upper](slots/metric_ci_upper.md) | Upper confidence interval bound |
| [metric_type](slots/metric_type.md) | Metric type (e |
| [metric_value](slots/metric_value.md) | Metric value |
| [metrics](slots/metrics.md) | Quantitative association metrics |
| [min_age_years](slots/min_age_years.md) | Minimum (earliest) age of onset in years |
| [min_frequency](slots/min_frequency.md) | Minimum phenotype frequency threshold for a HAS_PHENOTYPE criterion; members ... |
| [minimum_required](slots/minimum_required.md) | Minimum number of criteria required in this criteria set |
| [minimum_value](slots/minimum_value.md) |  |
| [model_format](slots/model_format.md) | File format (e |
| [model_id](slots/model_id.md) | Identifier within the repository (e |
| [model_software](slots/model_software.md) | Software/toolbox for running the model (e |
| [model_systems](slots/model_systems.md) | Experimental model systems used or proposed for an experiment, using the Expe... |
| [model_type](slots/model_type.md) | Type of computational model |
| [modeled_mechanisms](slots/modeled_mechanisms.md) | Pathophysiology mechanism nodes/assertions that this experimental model is in... |
| [modeling_considerations](slots/modeling_considerations.md) |  |
| [modifier](slots/modifier.md) | Directional or qualitative modifier for a descriptor (e |
| [module](slots/module.md) | Reference to a mechanism module in kb/modules/ (filename stem, without  |
| [molecular_functions](slots/molecular_functions.md) |  |
| [mondo_mappings](slots/mondo_mappings.md) | MONDO disease ontology mappings for this disease |
| [name](slots/name.md) |  |
| [namo_type](slots/namo_type.md) | Optional mapping to the corresponding NAMO class, such as `namo:Organoid` or ... |
| [ncit_mappings](slots/ncit_mappings.md) | NCIT disease, subtype, or disease/finding mappings |
| [negated](slots/negated.md) | If true, this leaf criterion is negated (the constraint must NOT hold) |
| [notes](slots/notes.md) |  |
| [onset](slots/onset.md) | Structured age of onset descriptor |
| [onset_category](slots/onset_category.md) | HPO onset category (e |
| [operands](slots/operands.md) | Child criteria combined by this branch node's operator |
| [operator](slots/operator.md) | Boolean operator for a branch node in a membership-criteria expression |
| [organism](slots/organism.md) | The organism from which samples were derived |
| [overlap](slots/overlap.md) | Overlap fraction for an enrichment term |
| [p_value](slots/p_value.md) | P-value for an association or enrichment |
| [pair_count](slots/pair_count.md) | Number of records/patients with co-occurrence of disorder A and disorder B in... |
| [parent_of_origin_effect](slots/parent_of_origin_effect.md) | Parent-of-origin effect or bias (e |
| [parents](slots/parents.md) |  |
| [pathophysiology](slots/pathophysiology.md) |  |
| [pathways](slots/pathways.md) |  |
| [patient_population](slots/patient_population.md) | FDA patient population text for a surrogate endpoint row |
| [pdb_id](slots/pdb_id.md) | PDB accession code (e |
| [pdb_structures](slots/pdb_structures.md) | Experimental or predicted 3D protein structures relevant to this treatment's ... |
| [penetrance](slots/penetrance.md) | Penetrance classification for this inheritance pattern |
| [penetrance_percentage](slots/penetrance_percentage.md) | Estimated penetrance percentage or range (e |
| [percentage](slots/percentage.md) |  |
| [perturbations](slots/perturbations.md) | Gene knockouts, reaction deletions, or parameter changes modeling the disease |
| [phase](slots/phase.md) |  |
| [phenotype_contexts](slots/phenotype_contexts.md) | Context-specific qualifications of this phenotype's frequency, severity, or o... |
| [phenotype_term](slots/phenotype_term.md) | The HP term for this phenotype |
| [phenotypes](slots/phenotypes.md) |  |
| [platform](slots/platform.md) | Sequencing or array platform used |
| [population](slots/population.md) | Population or cohort description (e |
| [posed_by](slots/posed_by.md) | Optional attribution for who posed a Discussion |
| [posed_date](slots/posed_date.md) | Date the Discussion was first posed (ISO 8601) |
| [precision_count_threshold](slots/precision_count_threshold.md) | Co-occurrence count threshold used to flag limited precision |
| [predicate](slots/predicate.md) | The relationship/predicate in a qualifier (e |
| [preferred_term](slots/preferred_term.md) | The preferred human-readable term for this descriptor |
| [presence](slots/presence.md) |  |
| [prevalence](slots/prevalence.md) |  |
| [progression](slots/progression.md) |  |
| [prompt](slots/prompt.md) | The unresolved question, controversy, or todo articulated by a Discussion |
| [proposed_experiments](slots/proposed_experiments.md) | Experiments proposed as ways to resolve this Discussion |
| [protein_complexes](slots/protein_complexes.md) | Protein complexes that gene products participate in |
| [protocol_reference](slots/protocol_reference.md) | Optional protocol, methods paper, or registry reference for the experimental ... |
| [publication](slots/publication.md) | Associated publication (PMID) |
| [qualifiers](slots/qualifiers.md) | List of predicate-value pairs for formal post-composition |
| [rationale](slots/rationale.md) | Why this Discussion matters / what hangs on its resolution |
| [readouts](slots/readouts.md) | Links this biomarker to disease pathograph nodes that it measures, reflects, ... |
| [reference](slots/reference.md) | The authoritative reference (publication) for this evidence item |
| [reference_ranges](slots/reference_ranges.md) | Clinical laboratory reference intervals for this biomarker, keyed by LOINC co... |
| [reference_title](slots/reference_title.md) | The title of the referenced publication |
| [references](slots/references.md) | Top-level list of references with their key findings for this disease |
| [regimen_term](slots/regimen_term.md) | The NCIT term for this treatment regimen |
| [regulatory_category](slots/regulatory_category.md) | Functional classification of a variant's impact on gene expression, using the... |
| [regulatory_element_type](slots/regulatory_element_type.md) | Type of gene regulatory element disrupted by a non-coding variant (e |
| [regulatory_endpoint_refs](slots/regulatory_endpoint_refs.md) | Stable row identifiers for source-level regulatory surrogate endpoint asserti... |
| [regulatory_mechanism](slots/regulatory_mechanism.md) | The specific molecular mechanism by which the regulatory variant exerts its e... |
| [relationship](slots/relationship.md) | Controlled relationship between a biomarker and the pathograph node it report... |
| [relationship_type](slots/relationship_type.md) | Controlled-vocabulary classification of the gene-disease relationship (e |
| [repository_url](slots/repository_url.md) | URL to model repository (GitHub, BiGG, VMH, BioModels) |
| [resolution_angstrom](slots/resolution_angstrom.md) | Structure resolution in angstroms (for experimental structures) |
| [resolution_note](slots/resolution_note.md) | Short summary written when a Discussion is marked RESOLVED |
| [resolved_date](slots/resolved_date.md) | Date the Discussion's status moved to RESOLVED (ISO 8601) |
| [results](slots/results.md) |  |
| [retrieved_date](slots/retrieved_date.md) | Date on which the source was retrieved for curation |
| [review_notes](slots/review_notes.md) |  |
| [role](slots/role.md) |  |
| [row_id](slots/row_id.md) | Stable row identifier assigned during source-table curation |
| [same_time](slots/same_time.md) | Probability or fraction of A and B occurring in the same time window |
| [sample_count](slots/sample_count.md) | Total number of samples in the dataset |
| [sample_types](slots/sample_types.md) | Types of biological samples in the dataset |
| [scope](slots/scope.md) | Scope or population for which the definition applies (e |
| [sequelae](slots/sequelae.md) |  |
| [sequence_length](slots/sequence_length.md) |  |
| [severity](slots/severity.md) |  |
| [severity_scale](slots/severity_scale.md) | Ordered list of severity tiers, each a value-label pair |
| [sex](slots/sex.md) | Sex-specific stratum, if applicable |
| [shared_upstream_hypotheses](slots/shared_upstream_hypotheses.md) | Suspected upstream conditions that may explain both A and B |
| [signal_disorder_a_id](slots/signal_disorder_a_id.md) | Original identifier for disorder A in this signal (CURIE, e |
| [signal_disorder_b_id](slots/signal_disorder_b_id.md) | Original identifier for disorder B in this signal (CURIE, e |
| [slug](slots/slug.md) | Canonical slug identifier (Title_Case_With_Underscores) for leaf conditions |
| [snippet](slots/snippet.md) | An exact excerpt/quote from the referenced publication that supports or refut... |
| [source](slots/source.md) | Source dataset or provenance label |
| [source_content_current_as_of](slots/source_content_current_as_of.md) | Date shown by the source as the content-current-as-of date |
| [source_row_number](slots/source_row_number.md) | Row number in the source spreadsheet worksheet |
| [source_sheet](slots/source_sheet.md) | Spreadsheet worksheet name or source table label |
| [source_table](slots/source_table.md) | FDA surrogate endpoint table section from which the row was curated |
| [source_url](slots/source_url.md) | URL of the source page for a curated assertion or source collection |
| [source_workbook_sha256](slots/source_workbook_sha256.md) | SHA-256 checksum of the downloaded source workbook used for import |
| [source_workbook_url](slots/source_workbook_url.md) | URL of the source workbook or downloadable data file |
| [spatial_extent](slots/spatial_extent.md) | The spatial extent or distribution pattern applicable to this descriptor (e |
| [species](slots/species.md) |  |
| [specificity](slots/specificity.md) |  |
| [stages](slots/stages.md) |  |
| [statement](slots/statement.md) | A key finding or claim from the publication |
| [statistics](slots/statistics.md) | Statistical summary for an association signal |
| [status](slots/status.md) | Status or state of a clinical trial or other process |
| [substages](slots/substages.md) |  |
| [subtype](slots/subtype.md) |  |
| [subtype_frequency](slots/subtype_frequency.md) | Frequency of this subtype among all cases of the parent disease (e |
| [subtype_term](slots/subtype_term.md) | The ontology term grounding this subtype or cancer facet value |
| [subtypes](slots/subtypes.md) | Names of subtypes (foreign keys to this disease's `has_subtypes[] |
| [supporting_text](slots/supporting_text.md) | Exact excerpt/quote from the publication supporting the statement |
| [supports](slots/supports.md) |  |
| [surrogate_endpoint](slots/surrogate_endpoint.md) | Surrogate endpoint text from the FDA surrogate endpoint table |
| [surrogate_endpoints](slots/surrogate_endpoints.md) | Curated surrogate endpoint assertions |
| [synonyms](slots/synonyms.md) |  |
| [tags](slots/tags.md) | Authoritative-source tags for a reference (e |
| [target](slots/target.md) | The name of the target element in a causal relationship |
| [target_exon](slots/target_exon.md) | The exon (or exons) modulated by a splice-switching antisense oligonucleotide... |
| [target_gene](slots/target_gene.md) | The gene whose transcript an antisense oligonucleotide targets (bindable to H... |
| [target_mechanisms](slots/target_mechanisms.md) | Pathophysiology mechanism nodes that this treatment targets or modulates |
| [target_phenotypes](slots/target_phenotypes.md) | Phenotypes that this treatment or trial addresses or targets |
| [target_protein](slots/target_protein.md) | Name of the protein target in the structure |
| [target_transcript](slots/target_transcript.md) | The specific transcript, pre-mRNA element, or sequence motif targeted by an a... |
| [temporality](slots/temporality.md) | Temporal qualifier for this descriptor (e |
| [term](slots/term.md) | Optional structured ontology term reference |
| [therapeutic_agent](slots/therapeutic_agent.md) | The drug, chemical, or therapeutic agent used in a treatment |
| [therapeutic_modality](slots/therapeutic_modality.md) | Broad therapeutic platform/modality of a treatment (e |
| [threshold](slots/threshold.md) | Numeric threshold at which this mapping activates (e |
| [threshold_direction](slots/threshold_direction.md) | Whether the threshold activates when the variable goes above or below the val... |
| [tissue_term](slots/tissue_term.md) | UBERON term for the tissue |
| [title](slots/title.md) | Title of the publication |
| [tracked_issue_role](slots/tracked_issue_role.md) | Role this tracked issue plays relative to the dismech content it is attached ... |
| [tracked_issue_status](slots/tracked_issue_status.md) | Last known status of the tracked issue (e |
| [tracked_issues](slots/tracked_issues.md) | Structured pointers to external tracker issues (e |
| [transmission](slots/transmission.md) |  |
| [treatment_effect](slots/treatment_effect.md) | How the treatment affects the targeted mechanism |
| [treatment_term](slots/treatment_term.md) | The MAXO term for this treatment/medical action |
| [treatments](slots/treatments.md) |  |
| [triggers](slots/triggers.md) |  |
| [type](slots/type.md) |  |
| [unit](slots/unit.md) |  |
| [updated_date](slots/updated_date.md) | ISO 8601/RFC 3339 timestamp string for when this disease entry was last updat... |
| [upper_bound](slots/upper_bound.md) | Upper bound of a reference interval (inclusive) |
| [upstream_disorder](slots/upstream_disorder.md) | Upstream disorder referenced in a hypothesis |
| [url](slots/url.md) | URL for the external assertion or registry record |
| [value](slots/value.md) | The value/filler in a qualifier |
| [variables](slots/variables.md) | Variables/outputs of a computational model with ontology mappings |
| [variant_origin](slots/variant_origin.md) | The origin of disease-associated variation in this gene (germline, somatic, d... |
| [variants](slots/variants.md) |  |
| [vectors](slots/vectors.md) |  |
| [would_refute](slots/would_refute.md) | Entity references that would be weakened or refuted if the experiment meets a... |
| [would_support](slots/would_support.md) | Entity references that would be supported if the experiment meets its decisio... |
| [zygosity](slots/zygosity.md) | Zygosity context |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AbnormalFlagEnum](enums/AbnormalFlagEnum.md) | Categorical interpretation flag for a clinical laboratory result band, aligne... |
| [AllelicEventEnum](enums/AllelicEventEnum.md) | Type of genetic or epigenetic event affecting an allele |
| [AllelicHitRoleEnum](enums/AllelicHitRoleEnum.md) | Role of a genetic alteration in a multi-hit disease mechanism |
| [AnatomicalEntityTerm](enums/AnatomicalEntityTerm.md) | A term representing an anatomical entity |
| [AsoChemistryEnum](enums/AsoChemistryEnum.md) | Backbone / sugar chemistry of an antisense oligonucleotide |
| [AsoConjugationEnum](enums/AsoConjugationEnum.md) | Targeting ligand or conjugate attached to an antisense oligonucleotide to dir... |
| [AsoMechanismEnum](enums/AsoMechanismEnum.md) | Molecular mechanism of action of an antisense oligonucleotide, following the ... |
| [AssayTerm](enums/AssayTerm.md) | A term representing an assay |
| [AssociationMetricTypeEnum](enums/AssociationMetricTypeEnum.md) | Type of association metric |
| [AssociationSignalMethodEnum](enums/AssociationSignalMethodEnum.md) | Method used to derive an association signal |
| [AssociationSignalSourceEnum](enums/AssociationSignalSourceEnum.md) | Source of an association signal |
| [BiologicalProcessTerm](enums/BiologicalProcessTerm.md) | A term representing a biological process or pathway |
| [BiomarkerEndpointContextEnum](enums/BiomarkerEndpointContextEnum.md) | Endpoint or use context for a biomarker readout link |
| [BiomarkerReadoutDirectionEnum](enums/BiomarkerReadoutDirectionEnum.md) | Direction of association between biomarker value/presence and the linked even... |
| [BiomarkerReadoutRelationshipEnum](enums/BiomarkerReadoutRelationshipEnum.md) | Relationship between a biomarker and the pathograph node it reports on |
| [BiomarkerTerm](enums/BiomarkerTerm.md) | A biomarker term from NCIT |
| [CausalLinkTypeEnum](enums/CausalLinkTypeEnum.md) | Degree of mechanistic directness represented by a causal edge |
| [CellTypeTerm](enums/CellTypeTerm.md) | A cell type |
| [CellularComponentTerm](enums/CellularComponentTerm.md) | A term representing a cellular component |
| [ChannelopathyOrganSystemEnum](enums/ChannelopathyOrganSystemEnum.md) | Classification categories for channelopathies by affected organ system |
| [ChemicalEntityTerm](enums/ChemicalEntityTerm.md) | A term representing a chemical entity |
| [ClinicalBenefitLinkageEnum](enums/ClinicalBenefitLinkageEnum.md) | How a surrogate endpoint is linked to clinical benefit in the regulatory cont... |
| [ClinicalCourseEnum](enums/ClinicalCourseEnum.md) | Clinical course qualifiers for descriptor post-composition |
| [ClinicalSignificanceEnum](enums/ClinicalSignificanceEnum.md) | The clinical significance of a variant for a condition (ACMG guidelines) |
| [ClinicalTrialPhaseEnum](enums/ClinicalTrialPhaseEnum.md) | Clinical trial phase categories per FDA/NIH standards |
| [ClinicalTrialStatusEnum](enums/ClinicalTrialStatusEnum.md) | Clinical trial recruitment and status categories per ClinicalTrials |
| [ComorbidityDirectionEnum](enums/ComorbidityDirectionEnum.md) | Directionality of a comorbidity/trajectory association |
| [ComputationalModelTypeEnum](enums/ComputationalModelTypeEnum.md) | Type of computational or in-silico model |
| [ConditionCompositionEnum](enums/ConditionCompositionEnum.md) | Composition type for a composite condition descriptor |
| [CriteriaSemanticsEnum](enums/CriteriaSemanticsEnum.md) | The logical direction relating a grouping's membership criteria to its member... |
| [CriterionPredicateEnum](enums/CriterionPredicateEnum.md) | The kind of constraint expressed by a leaf node in a membership-criteria expr... |
| [CurationActionEnum](enums/CurationActionEnum.md) | Simple action types for curation audit trail |
| [CurationStatusEnum](enums/CurationStatusEnum.md) | Curation workflow status for an association |
| [DatasetTypeEnum](enums/DatasetTypeEnum.md) | Type of dataset or data resource |
| [DefinitionTypeEnum](enums/DefinitionTypeEnum.md) | The type of definition or criteria set |
| [DietaryModificationActionEnum](enums/DietaryModificationActionEnum.md) | Action applied to a food or beverage as part of a dietary treatment |
| [DiscussionKindEnum](enums/DiscussionKindEnum.md) | Kind of unresolved/in-progress item captured by a Discussion |
| [DiscussionStatusEnum](enums/DiscussionStatusEnum.md) | Lifecycle status for a Discussion |
| [DiseaseOrSubtypeTerm](enums/DiseaseOrSubtypeTerm.md) | A MONDO disease term or NCIT cancer disease/subtype term used to ground a dis... |
| [DiseaseTerm](enums/DiseaseTerm.md) | A MONDO disease, inherited disease susceptibility, or related medical conditi... |
| [EnvironmentTerm](enums/EnvironmentTerm.md) | A term representing an environmental context, material, or feature (from ENVO... |
| [EvidenceItemSupportEnum](enums/EvidenceItemSupportEnum.md) | The level of support for an evidence item |
| [EvidenceSourceEnum](enums/EvidenceSourceEnum.md) | The provenance/source of the evidence item |
| [ExperimentalModelTypeEnum](enums/ExperimentalModelTypeEnum.md) | Broad disease-centric categories for experimental model systems, primarily no... |
| [ExposureTerm](enums/ExposureTerm.md) | A term representing an exposure event (from ECTO or XCO) |
| [ExpressivityEnum](enums/ExpressivityEnum.md) | Expressivity classification for inheritance |
| [FoodTerm](enums/FoodTerm.md) | A term representing a food, beverage, nutrient, mineral, or supplement source... |
| [FrequencyEnum](enums/FrequencyEnum.md) | The frequency of an event or phenomenon |
| [FunctionalImpactEnum](enums/FunctionalImpactEnum.md) | Directional or qualitative functional consequence of a variant or genetic con... |
| [GeneDiseaseRelationshipEnum](enums/GeneDiseaseRelationshipEnum.md) | The qualitative relationship between a gene (or locus) and a disease |
| [GeneProductTerm](enums/GeneProductTerm.md) | A gene product term from NCIT |
| [GeneTerm](enums/GeneTerm.md) | A gene term from HGNC |
| [GeographyTerm](enums/GeographyTerm.md) | A place or location |
| [GroupingBasisEnum](enums/GroupingBasisEnum.md) | The axis (or axes) on which a disease Grouping is drawn |
| [GroupingMemberTypeEnum](enums/GroupingMemberTypeEnum.md) | The kind of entity referenced by a GroupingMember |
| [HarrisonsChapterEnum](enums/HarrisonsChapterEnum.md) | Harrison's Principles of Internal Medicine classification by Part |
| [HistopathologyFindingTerm](enums/HistopathologyFindingTerm.md) | A histopathologic finding term from NCIT |
| [ICD10CMTerm](enums/ICD10CMTerm.md) | An ICD-10-CM diagnosis code |
| [ICD11FTerm](enums/ICD11FTerm.md) | An ICD-11 Foundation diagnosis code |
| [ICDOMorphologyEnum](enums/ICDOMorphologyEnum.md) | ICD-O morphology axis classification for cancer subtypes |
| [InheritanceTerm](enums/InheritanceTerm.md) | A term representing mode of inheritance |
| [IUISCategoryEnum](enums/IUISCategoryEnum.md) | IUIS classification tables for inborn errors of immunity (IEI) |
| [LateralityEnum](enums/LateralityEnum.md) | Laterality qualifier for anatomical structures or procedures |
| [LifeCycleStageTerm](enums/LifeCycleStageTerm.md) | A parasite life cycle stage term (from OPL) |
| [LogicalOperatorEnum](enums/LogicalOperatorEnum.md) | Boolean operator for a branch node in a nested membership-criteria expression... |
| [LysosomalStorageEnum](enums/LysosomalStorageEnum.md) | Classification of lysosomal storage diseases by accumulated substrate type |
| [MappingConsistencyEnum](enums/MappingConsistencyEnum.md) | Consistency of a mapping relative to another reference source |
| [MechanismConfidenceEnum](enums/MechanismConfidenceEnum.md) | Level of confidence in a pathophysiology mechanism |
| [MechanisticHypothesisStatusEnum](enums/MechanisticHypothesisStatusEnum.md) | Curation/maturity status for a disease-level mechanistic hypothesis |
| [MechanisticNosologyEnum](enums/MechanisticNosologyEnum.md) | Classification of diseases by molecular mechanism or affected cellular system |
| [MedicalActionCategoryEnum](enums/MedicalActionCategoryEnum.md) | Broad functional category for a clinical action currently represented in the ... |
| [ModifierEnum](enums/ModifierEnum.md) | Qualifiers for direction, intensity, or pathological state of a descriptor |
| [MolecularFunctionTerm](enums/MolecularFunctionTerm.md) | A term representing a molecular function |
| [NCITDiseaseOrFindingTerm](enums/NCITDiseaseOrFindingTerm.md) | An NCIT disease-oriented oncology term used for disease-level cancer mappings... |
| [OnsetEnum](enums/OnsetEnum.md) | Age of onset categories from HPO |
| [OrganismTerm](enums/OrganismTerm.md) | A term representing an organism from NCBITaxon |
| [PenetranceEnum](enums/PenetranceEnum.md) | Penetrance classification for inheritance |
| [PhaseTerm](enums/PhaseTerm.md) | A phase or stage |
| [PhenotypeCategoryEnum](enums/PhenotypeCategoryEnum.md) | Broad phenotype categories from the Human Phenotype Ontology |
| [PhenotypeTerm](enums/PhenotypeTerm.md) | A term representing a phenotype or disease manifestation |
| [ProteinComplexTerm](enums/ProteinComplexTerm.md) | A term representing a protein complex |
| [ReferenceTagEnum](enums/ReferenceTagEnum.md) | Controlled vocabulary for tagging top-level references by authoritative sourc... |
| [RegimenTerm](enums/RegimenTerm.md) | A term representing a treatment regimen (from NCIT) |
| [RegulatoryElementTypeEnum](enums/RegulatoryElementTypeEnum.md) | Type of gene regulatory element disrupted by a non-coding variant |
| [RegulatoryVariantCategoryEnum](enums/RegulatoryVariantCategoryEnum.md) | Functional classification of non-coding gene regulatory variants based on the... |
| [SeverityQualifierEnum](enums/SeverityQualifierEnum.md) | Severity qualifiers for descriptor post-composition |
| [SexEnum](enums/SexEnum.md) | Sex-specific stratum |
| [SpatialExtentEnum](enums/SpatialExtentEnum.md) | Qualifiers for the spatial extent or distribution of a phenotype or process |
| [SurrogateEndpointApprovalTypeEnum](enums/SurrogateEndpointApprovalTypeEnum.md) | Regulatory approval pathway context represented in the FDA surrogate endpoint... |
| [SurrogateEndpointFootnoteEnum](enums/SurrogateEndpointFootnoteEnum.md) | Footnotes and symbols used in the FDA surrogate endpoint workbook |
| [SurrogateEndpointMappingStatusEnum](enums/SurrogateEndpointMappingStatusEnum.md) | Status of mapping an FDA disease/use row to dismech disease entries |
| [SurrogateEndpointTableEnum](enums/SurrogateEndpointTableEnum.md) | FDA surrogate endpoint table section from which a row was curated |
| [SurrogateEndpointValidationLevelEnum](enums/SurrogateEndpointValidationLevelEnum.md) | BEST-aligned regulatory validation level inferred or curated for a surrogate ... |
| [TemporalityEnum](enums/TemporalityEnum.md) | Temporal qualifiers for descriptor post-composition |
| [TherapeuticModalityEnum](enums/TherapeuticModalityEnum.md) | Broad therapeutic modality / platform of a treatment, independent of the spec... |
| [ThresholdDirectionEnum](enums/ThresholdDirectionEnum.md) | Whether a threshold activates when the variable goes above or below the value |
| [TreatmentActionTerm](enums/TreatmentActionTerm.md) | A term representing a medical action or treatment (from MAXO or NCIT) |
| [TreatmentEffectEnum](enums/TreatmentEffectEnum.md) | How a treatment affects a pathophysiology mechanism node |
| [TriggerTerm](enums/TriggerTerm.md) | A trigger |
| [VariantOriginEnum](enums/VariantOriginEnum.md) | The origin of variation in a gene with respect to a disease entry |
| [ZygosityEnum](enums/ZygosityEnum.md) | Zygosity categories from GENO |


## Types

| Type | Description |
| --- | --- |
| [Boolean](types/Boolean.md) | A binary (true or false) value |
| [Curie](types/Curie.md) | a compact URI |
| [Date](types/Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](types/DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](types/Datetime.md) | The combination of a date and time |
| [Decimal](types/Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](types/Double.md) | A real number that conforms to the xsd:double specification |
| [Float](types/Float.md) | A real number that conforms to the xsd:float specification |
| [FrequencyQuantity](types/FrequencyQuantity.md) |  |
| [Integer](types/Integer.md) | An integer |
| [Jsonpath](types/Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](types/Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](types/Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](types/Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](types/Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [PMID](types/PMID.md) |  |
| [Sparqlpath](types/Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](types/String.md) | A character string |
| [Time](types/Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](types/Uri.md) | a complete URI |
| [Uriorcurie](types/Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
