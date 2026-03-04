# Disorder Mechanisms Knowledge Base Schema

Disease Pathophysiology Knowledge Base Schema

URI: https://w3id.org/monarch-initiative/dismech

Name: dismech



## Classes

| Class | Description |
| --- | --- |
| [AgentLifeCycle](AgentLifeCycle.md) |  |
| [AgentLifeCycleStage](AgentLifeCycleStage.md) |  |
| [AnimalModel](AnimalModel.md) |  |
| [Any](Any.md) |  |
| [Assay](Assay.md) |  |
| [AssociationMetric](AssociationMetric.md) | Quantitative association metric and its uncertainty |
| [AssociationSignal](AssociationSignal.md) | An association signal from EHR, registry, or computational sources, optionall... |
| [AssociationStatistics](AssociationStatistics.md) | Statistical summary with evidence for an association signal |
| [Biochemical](Biochemical.md) |  |
| [CausalEdge](CausalEdge.md) | A reference to a downstream effect or consequence in a causal relationship |
| [ClassificationAssignment](ClassificationAssignment.md) | Base class for classification assignments with evidence |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChannelopathyAssignment](ChannelopathyAssignment.md) | Channelopathy organ system classification assignment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HarrisonsChapterAssignment](HarrisonsChapterAssignment.md) | Harrison's internal medicine chapter classification assignment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ICDOMorphologyAssignment](ICDOMorphologyAssignment.md) | ICD-O morphology classification assignment for neoplastic diseases |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IUISAssignment](IUISAssignment.md) | IUIS primary immunodeficiency classification assignment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LysosomalStorageAssignment](LysosomalStorageAssignment.md) | Lysosomal storage disease biochemical classification assignment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MechanisticNosologyAssignment](MechanisticNosologyAssignment.md) | Mechanistic/pathway-based disease classification assignment |
| [ClinicalTrial](ClinicalTrial.md) | A clinical trial relevant to treatment or research of a disease |
| [ComorbidityAssociation](ComorbidityAssociation.md) | An association between two conditions, including directionality, evidence, an... |
| [ComorbidityHypothesis](ComorbidityHypothesis.md) | Mechanistic hypothesis for a comorbidity association, with rich text and embe... |
| [ComputationalModel](ComputationalModel.md) | A computational or in-silico model relevant to understanding disease mechanis... |
| [CriteriaSet](CriteriaSet.md) | A named criteria grouping within a definition |
| [CurationEvent](CurationEvent.md) | A single curation event in the audit trail |
| [Dataset](Dataset.md) | A reference to a publicly available omics or phenotype dataset |
| [Definition](Definition.md) | A diagnostic or phenotype definition for the disease |
| [Demographics](Demographics.md) | Demographic stratification for an association signal |
| [Descriptor](Descriptor.md) | Base class for structured descriptors that allow a preferred term, optional d... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) | A descriptor for anatomical locations, bindable to UBERON |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AssayDescriptor](AssayDescriptor.md) | A descriptor for assays, bindable to OBI |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiologicalProcessDescriptor](BiologicalProcessDescriptor.md) | A descriptor for biological processes, bindable to Gene Ontology (GO) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiomarkerDescriptor](BiomarkerDescriptor.md) | A descriptor for biomarkers, bindable to NCIT |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CellTypeDescriptor](CellTypeDescriptor.md) | A descriptor for cell types, bindable to Cell Ontology (CL) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CellularComponentDescriptor](CellularComponentDescriptor.md) | A descriptor for cellular components, bindable to GO cellular component |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalEntityDescriptor](ChemicalEntityDescriptor.md) | A descriptor for chemical entities, bindable to CHEBI |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ConditionDescriptor](ConditionDescriptor.md) | A descriptor for a condition or disease, optionally bound to MONDO |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CriteriaItem](CriteriaItem.md) | A criterion element (clinical feature, test result, imaging requirement) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiseaseDescriptor](DiseaseDescriptor.md) | A descriptor for the focal disease, bindable to MONDO |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EnvironmentDescriptor](EnvironmentDescriptor.md) | A descriptor for environmental contexts/settings, bindable to ENVO |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExposureDescriptor](ExposureDescriptor.md) | A descriptor for exposure events, bindable to ECTO or XCO |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneDescriptor](GeneDescriptor.md) | A descriptor for genes, bindable to HGNC or other gene databases |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneProductDescriptor](GeneProductDescriptor.md) | A descriptor for gene products (proteins, fusion proteins, oncoproteins), bin... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HistopathologyFindingDescriptor](HistopathologyFindingDescriptor.md) | A descriptor for histopathologic findings, bindable to NCIT Morphologic Findi... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[InheritanceDescriptor](InheritanceDescriptor.md) | A descriptor for inheritance patterns, bindable to HPO mode of inheritance te... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LifeCycleStageDescriptor](LifeCycleStageDescriptor.md) | A descriptor for parasite life cycle stages, bindable to OPL |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OrganismDescriptor](OrganismDescriptor.md) | A descriptor for organisms, bindable to NCBITaxon |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HostDescriptor](HostDescriptor.md) | A descriptor for hosts in an infectious agent life cycle |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PhenotypeDescriptor](PhenotypeDescriptor.md) | A descriptor for phenotypes, bindable to Human Phenotype Ontology (HP) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProteinComplexDescriptor](ProteinComplexDescriptor.md) | A descriptor for protein complexes that gene products participate in, bindabl... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RegimenDescriptor](RegimenDescriptor.md) | A descriptor for treatment regimens, bindable to NCIT |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SampleTypeDescriptor](SampleTypeDescriptor.md) | A descriptor for biological sample types (tissue and/or cell type) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TreatmentDescriptor](TreatmentDescriptor.md) | A descriptor for treatments/medical actions, bindable to Medical Action Ontol... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TriggerDescriptor](TriggerDescriptor.md) | A descriptor for triggers/causes |
| [Diagnosis](Diagnosis.md) |  |
| [DifferentialDiagnosis](DifferentialDiagnosis.md) | A disease or condition that presents similarly to the focal disease and must ... |
| [Disease](Disease.md) |  |
| [DiseaseClassifications](DiseaseClassifications.md) | Container for all classification assignments for a disease |
| [DiseaseCollection](DiseaseCollection.md) |  |
| [DiseaseMappings](DiseaseMappings.md) | Container for external identifier mappings for a disease |
| [Environmental](Environmental.md) | An environmental factor, exposure, or context relevant to disease |
| [EpidemiologyInfo](EpidemiologyInfo.md) |  |
| [EvidenceItem](EvidenceItem.md) |  |
| [Finding](Finding.md) | A key finding or claim extracted from a source (publication or dataset) |
| [FunctionalEffect](FunctionalEffect.md) |  |
| [Genetic](Genetic.md) |  |
| [GeneticContext](GeneticContext.md) | A structured description of a genetic context that modifies phenotype frequen... |
| [GOEnrichment](GOEnrichment.md) | GO enrichment results for an association signal |
| [GOEnrichmentTerm](GOEnrichmentTerm.md) | GO term enrichment result with statistical metrics |
| [HistopathologyFinding](HistopathologyFinding.md) | A histopathologic finding from microscopic examination of tissue |
| [InfectiousAgent](InfectiousAgent.md) |  |
| [Inheritance](Inheritance.md) |  |
| [MappingConsistency](MappingConsistency.md) | Consistency assertion for a mapping relative to another source |
| [Mechanism](Mechanism.md) |  |
| [MechanisticHypothesis](MechanisticHypothesis.md) | Disease-level hypothesis metadata used to organize downstream causal edges in... |
| [ModelingConsideration](ModelingConsideration.md) |  |
| [OnsetDescriptor](OnsetDescriptor.md) | Structured description of age of onset |
| [Pathophysiology](Pathophysiology.md) |  |
| [Phenotype](Phenotype.md) |  |
| [PhenotypeContext](PhenotypeContext.md) | A context-specific annotation qualifying how a phenotype manifests under part... |
| [Prevalence](Prevalence.md) |  |
| [ProgressionInfo](ProgressionInfo.md) |  |
| [PublicationReference](PublicationReference.md) | A reference to a publication with associated findings |
| [Qualifier](Qualifier.md) | A predicate-value pair for formal post-composition |
| [Stage](Stage.md) |  |
| [Subtype](Subtype.md) |  |
| [Term](Term.md) | A structured reference to an ontology term |
| [TermMapping](TermMapping.md) | Mapping from this disease entry to an external term or code |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ICD10CMMapping](ICD10CMMapping.md) | ICD-10-CM diagnosis code mapping |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ICD11FMapping](ICD11FMapping.md) | ICD-11 Foundation diagnosis code mapping |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MondoMapping](MondoMapping.md) | MONDO disease ontology mapping |
| [Transmission](Transmission.md) |  |
| [Treatment](Treatment.md) |  |
| [TreatmentMechanismTarget](TreatmentMechanismTarget.md) | Links a treatment to a specific pathophysiology mechanism node it targets |
| [UpstreamConditionHypothesis](UpstreamConditionHypothesis.md) | Hypothesized upstream condition that may explain both A and B |
| [Variant](Variant.md) |  |



## Slots

| Slot | Description |
| --- | --- |
| [a_before_b](a_before_b.md) | Probability or fraction of A before B in an EHR signal |
| [accession](accession.md) | Dataset accession identifier as a CURIE (e |
| [additional_requirements](additional_requirements.md) | Additional requirements used in a criteria set |
| [age_range](age_range.md) | Age range or stratification, if applicable |
| [agent_life_cycle](agent_life_cycle.md) |  |
| [allele_type](allele_type.md) | Type of allele or mutation (e |
| [alleles](alleles.md) |  |
| [animal_models](animal_models.md) |  |
| [applies_to_subtypes](applies_to_subtypes.md) | Disease subtypes for which this hypothesis is intended to apply |
| [assays](assays.md) |  |
| [associated_phenotypes](associated_phenotypes.md) |  |
| [association](association.md) |  |
| [association_signals](association_signals.md) | Association signals from EHR, registry, or computational sources |
| [b_before_a](b_before_a.md) | Probability or fraction of B before A in an EHR signal |
| [background](background.md) |  |
| [base_model](base_model.md) | Parent/base model this is derived from (e |
| [biochemical](biochemical.md) |  |
| [biological_processes](biological_processes.md) |  |
| [biomarker_term](biomarker_term.md) | Ontology term for a biomarker (from NCIT) |
| [categories](categories.md) |  |
| [category](category.md) |  |
| [causal_link_type](causal_link_type.md) | Whether this edge is direct or indirect, and whether omitted intermediates ar... |
| [cell_type_term](cell_type_term.md) | CL term for the cell type |
| [cell_types](cell_types.md) |  |
| [cellular_components](cellular_components.md) |  |
| [channelopathy_category](channelopathy_category.md) | Channelopathy organ system classification |
| [chemical_entities](chemical_entities.md) |  |
| [chemicals](chemicals.md) |  |
| [children](children.md) | Names of other subtypes in this list that are members/children of this groupi... |
| [classification](classification.md) | Classification scheme this subtype belongs to (e |
| [classification_value](classification_value.md) | The classification value assigned |
| [classifications](classifications.md) | Classification assignments for this disease from various nosologies |
| [clinical_significance](clinical_significance.md) |  |
| [clinical_trials](clinical_trials.md) | Clinical trials relevant to disease treatment and research |
| [code](code.md) | Code within the specified code system |
| [code_system](code_system.md) | Code system used for a condition reference (e |
| [combined_score](combined_score.md) | Combined score used by an enrichment method |
| [complementation_group](complementation_group.md) | Complementation group designation (e |
| [components](components.md) | Component conditions that make up a composite descriptor |
| [composition](composition.md) | Composition type for a composite condition descriptor |
| [computational_models](computational_models.md) | Computational models (metabolic, mechanistic, ML, digital twins) for this dis... |
| [conditions](conditions.md) | Experimental conditions or disease states represented |
| [consequence](consequence.md) |  |
| [consequences](consequences.md) |  |
| [consistency](consistency.md) | Consistency assertions for this mapping against other sources |
| [consistent](consistent.md) | Consistency status for a mapping relative to a reference source |
| [context](context.md) |  |
| [core_clinical_characteristics](core_clinical_characteristics.md) | Core clinical characteristics used in a criteria set |
| [creation_date](creation_date.md) | ISO 8601/RFC 3339 timestamp string for when this disease entry was first crea... |
| [criteria_sets](criteria_sets.md) | Named criteria groupings within a definition |
| [curation_action](curation_action.md) | Type of curation action performed |
| [curation_description](curation_description.md) | Human-readable description of changes made |
| [curation_history](curation_history.md) | Audit trail of AI-assisted curation events |
| [curation_model](curation_model.md) | Model identifier used for curation (e |
| [curation_status](curation_status.md) | Curation workflow status |
| [curation_timestamp](curation_timestamp.md) | ISO 8601 timestamp of the curation event |
| [data_type](data_type.md) | The type of omics or other data in the dataset |
| [datasets](datasets.md) | Publicly available datasets relevant to disease research |
| [de_novo_rate](de_novo_rate.md) | Estimated percentage of de novo cases (e |
| [definition_type](definition_type.md) | The type of definition or criteria set |
| [definitions](definitions.md) | Definitions or diagnostic criteria for this disease |
| [demographics](demographics.md) | Demographic stratification for an association signal |
| [description](description.md) |  |
| [diagnosis](diagnosis.md) |  |
| [diagnosis_term](diagnosis_term.md) | The MAXO term for this diagnostic procedure |
| [diagnostic](diagnostic.md) |  |
| [differential_diagnoses](differential_diagnoses.md) | Differential diagnoses - similar diseases that must be ruled out |
| [directionality](directionality.md) | Direction of a comorbidity/trajectory association |
| [disease_a](disease_a.md) | First disease in a comorbidity pair |
| [disease_b](disease_b.md) | Second disease in a comorbidity pair |
| [disease_term](disease_term.md) | The MONDO disease term for this disease |
| [diseases](diseases.md) |  |
| [disorder_a_count](disorder_a_count.md) | Number of records/patients carrying disorder A in the source dataset |
| [disorder_b_count](disorder_b_count.md) | Number of records/patients carrying disorder B in the source dataset |
| [distinguishing_features](distinguishing_features.md) | Key clinical, laboratory, imaging, or epidemiological features that help diff... |
| [downstream](downstream.md) |  |
| [duration](duration.md) |  |
| [duration_days](duration_days.md) |  |
| [effect](effect.md) |  |
| [environment_context](environment_context.md) | The ENVO term for the environmental context/setting |
| [environmental](environmental.md) |  |
| [epidemiology](epidemiology.md) |  |
| [evidence](evidence.md) |  |
| [evidence_source](evidence_source.md) | Origin of the evidence item (human clinical, model organism, in vitro, or com... |
| [examples](examples.md) |  |
| [exclusion_criteria](exclusion_criteria.md) | Exclusion criteria for a definition or criteria set |
| [explanation](explanation.md) |  |
| [exposure_term](exposure_term.md) | The ECTO/XCO term for this exposure event |
| [exposures](exposures.md) | Environmental exposures studied in the dataset |
| [expressivity](expressivity.md) | Expressivity classification for this inheritance pattern |
| [factors](factors.md) |  |
| [fdr](fdr.md) | FDR-adjusted p-value for an association or enrichment |
| [features](features.md) |  |
| [finding_term](finding_term.md) | Ontology term for a histopathologic finding (from NCIT or HP) |
| [findings](findings.md) | Key findings or claims extracted from this source (publication or dataset) |
| [found_in](found_in.md) | Deep-research output files where this reference was cited |
| [frequency](frequency.md) |  |
| [function](function.md) |  |
| [functional_effects](functional_effects.md) |  |
| [functional_impact](functional_impact.md) | Functional consequence of the genetic variant (e |
| [gene](gene.md) |  |
| [gene_products](gene_products.md) | Gene products (proteins, fusion proteins, oncoproteins) involved in this path... |
| [gene_term](gene_term.md) | The HGNC term for this gene |
| [genes](genes.md) |  |
| [genetic](genetic.md) |  |
| [genetic_context](genetic_context.md) | The genetic context under which this qualification applies |
| [genotype](genotype.md) |  |
| [geography](geography.md) |  |
| [go_enrichment](go_enrichment.md) | GO enrichment results associated with a signal |
| [go_terms](go_terms.md) | GO term enrichment results |
| [harrisons_chapter](harrisons_chapter.md) | Harrison's internal medicine chapter classification |
| [has_subtypes](has_subtypes.md) |  |
| [histopathology](histopathology.md) | Histopathologic findings including microscopic morphology, architectural patt... |
| [hosts](hosts.md) |  |
| [hypotheses](hypotheses.md) | Mechanistic or causal hypotheses about the association |
| [hypothesis_group_id](hypothesis_group_id.md) | Stable identifier for a disease-level mechanistic hypothesis grouping |
| [hypothesis_groups](hypothesis_groups.md) | Hypothesis identifiers or grouping labels that this edge belongs to |
| [hypothesis_label](hypothesis_label.md) | Human-readable label/title for a mechanistic hypothesis |
| [icd10cm_mappings](icd10cm_mappings.md) | ICD-10-CM code mappings for this disease |
| [icd11f_mappings](icd11f_mappings.md) | ICD-11 Foundation code mappings for this disease |
| [icdo_morphology](icdo_morphology.md) | ICD-O morphology classification (for neoplastic diseases) |
| [id](id.md) | Ontology term identifier (CURIE) |
| [identifiers](identifiers.md) |  |
| [imaging_requirements](imaging_requirements.md) | Imaging requirements used in a criteria set |
| [inclusion_criteria](inclusion_criteria.md) | Inclusion criteria for a definition or criteria set |
| [incubation_days](incubation_days.md) |  |
| [incubation_years](incubation_years.md) |  |
| [infectious_agent](infectious_agent.md) |  |
| [infectious_agent_term](infectious_agent_term.md) | The NCBITaxon term for this infectious agent |
| [inheritance](inheritance.md) |  |
| [inheritance_term](inheritance_term.md) | The HPO mode of inheritance term for this inheritance pattern |
| [intermediate_mechanisms](intermediate_mechanisms.md) | Known or suspected intermediate mechanisms omitted from this edge for graph c... |
| [iuis_category](iuis_category.md) | IUIS primary immunodeficiency classification |
| [label](label.md) | Human-readable label for the ontology term |
| [laboratory_requirements](laboratory_requirements.md) | Laboratory or serologic requirements used in a criteria set |
| [laterality](laterality.md) | Laterality qualifier (left, right, or bilateral) |
| [life_cycle_stage_term](life_cycle_stage_term.md) | The OPL term for this agent life cycle stage |
| [life_cycle_stages](life_cycle_stages.md) |  |
| [limited_precision](limited_precision.md) | Whether the signal has limited statistical precision due to small co-occurren... |
| [literature_evidence](literature_evidence.md) | Literature-based evidence items for this association |
| [located_in](located_in.md) | Anatomical location where this entity/process occurs or procedure is performe... |
| [locations](locations.md) |  |
| [lysosomal_storage_category](lysosomal_storage_category.md) | Lysosomal storage disease biochemical classification |
| [mapping_justification](mapping_justification.md) | Brief rationale or justification for the mapping |
| [mapping_notes](mapping_notes.md) | Notes on code-to-concept mapping decisions for this signal |
| [mapping_predicate](mapping_predicate.md) | Relationship between this disease and the mapped term (e |
| [mapping_source](mapping_source.md) | Source of the mapping (e |
| [mappings](mappings.md) | External identifier mappings for this disease (SSSOM-inspired) |
| [markers](markers.md) |  |
| [max_age_years](max_age_years.md) | Maximum (latest) age of onset in years |
| [maximum_value](maximum_value.md) |  |
| [mean_age_years](mean_age_years.md) | Mean age of onset in years, as reported in a cohort study |
| [mean_range](mean_range.md) |  |
| [mechanism](mechanism.md) |  |
| [mechanisms](mechanisms.md) |  |
| [mechanistic_category](mechanistic_category.md) | Mechanistic/pathway-based disease classification |
| [mechanistic_hypotheses](mechanistic_hypotheses.md) | Disease-level mechanistic hypotheses that group and annotate causal edges |
| [method](method.md) | Method or pipeline name |
| [metric_ci_lower](metric_ci_lower.md) | Lower confidence interval bound |
| [metric_ci_upper](metric_ci_upper.md) | Upper confidence interval bound |
| [metric_type](metric_type.md) | Metric type (e |
| [metric_value](metric_value.md) | Metric value |
| [metrics](metrics.md) | Quantitative association metrics |
| [min_age_years](min_age_years.md) | Minimum (earliest) age of onset in years |
| [minimum_required](minimum_required.md) | Minimum number of criteria required in this criteria set |
| [minimum_value](minimum_value.md) |  |
| [model_format](model_format.md) | File format (e |
| [model_id](model_id.md) | Identifier within the repository (e |
| [model_software](model_software.md) | Software/toolbox for running the model (e |
| [model_type](model_type.md) | Type of computational model |
| [modeling_considerations](modeling_considerations.md) |  |
| [modifier](modifier.md) | Directional or qualitative modifier for a descriptor (e |
| [mondo_mappings](mondo_mappings.md) | MONDO disease ontology mappings for this disease |
| [name](name.md) |  |
| [notes](notes.md) |  |
| [onset](onset.md) | Structured age of onset descriptor |
| [onset_category](onset_category.md) | HPO onset category (e |
| [organism](organism.md) | The organism from which samples were derived |
| [overlap](overlap.md) | Overlap fraction for an enrichment term |
| [p_value](p_value.md) | P-value for an association or enrichment |
| [pair_count](pair_count.md) | Number of records/patients with co-occurrence of disorder A and disorder B in... |
| [parent_of_origin_effect](parent_of_origin_effect.md) | Parent-of-origin effect or bias (e |
| [parents](parents.md) |  |
| [pathophysiology](pathophysiology.md) |  |
| [pathways](pathways.md) |  |
| [penetrance](penetrance.md) | Penetrance classification for this inheritance pattern |
| [penetrance_percentage](penetrance_percentage.md) | Estimated penetrance percentage or range (e |
| [percentage](percentage.md) |  |
| [perturbations](perturbations.md) | Gene knockouts, reaction deletions, or parameter changes modeling the disease |
| [phase](phase.md) |  |
| [phenotype_contexts](phenotype_contexts.md) | Context-specific qualifications of this phenotype's frequency, severity, or o... |
| [phenotype_term](phenotype_term.md) | The HP term for this phenotype |
| [phenotypes](phenotypes.md) |  |
| [platform](platform.md) | Sequencing or array platform used |
| [population](population.md) | Population or cohort description (e |
| [precision_count_threshold](precision_count_threshold.md) | Co-occurrence count threshold used to flag limited precision |
| [predicate](predicate.md) | The relationship/predicate in a qualifier (e |
| [preferred_term](preferred_term.md) | The preferred human-readable term for this descriptor |
| [presence](presence.md) |  |
| [prevalence](prevalence.md) |  |
| [progression](progression.md) |  |
| [protein_complexes](protein_complexes.md) | Protein complexes that gene products participate in |
| [publication](publication.md) | Associated publication (PMID) |
| [qualifiers](qualifiers.md) | List of predicate-value pairs for formal post-composition |
| [reference](reference.md) | The authoritative reference (publication) for this evidence item |
| [references](references.md) | Top-level list of references with their key findings for this disease |
| [regimen_term](regimen_term.md) | The NCIT term for this treatment regimen |
| [repository_url](repository_url.md) | URL to model repository (GitHub, BiGG, VMH, BioModels) |
| [results](results.md) |  |
| [review_notes](review_notes.md) |  |
| [role](role.md) |  |
| [same_time](same_time.md) | Probability or fraction of A and B occurring in the same time window |
| [sample_count](sample_count.md) | Total number of samples in the dataset |
| [sample_types](sample_types.md) | Types of biological samples in the dataset |
| [scope](scope.md) | Scope or population for which the definition applies (e |
| [sequelae](sequelae.md) |  |
| [sequence_length](sequence_length.md) |  |
| [severity](severity.md) |  |
| [sex](sex.md) | Sex-specific stratum, if applicable |
| [shared_upstream_hypotheses](shared_upstream_hypotheses.md) | Suspected upstream conditions that may explain both A and B |
| [signal_disorder_a_id](signal_disorder_a_id.md) | Original identifier for disorder A in this signal (CURIE, e |
| [signal_disorder_b_id](signal_disorder_b_id.md) | Original identifier for disorder B in this signal (CURIE, e |
| [slug](slug.md) | Canonical slug identifier (Title_Case_With_Underscores) for leaf conditions |
| [snippet](snippet.md) | An exact excerpt/quote from the referenced publication that supports or refut... |
| [source](source.md) | Source dataset or provenance label |
| [species](species.md) |  |
| [specificity](specificity.md) |  |
| [stages](stages.md) |  |
| [statement](statement.md) | A key finding or claim from the publication |
| [statistics](statistics.md) | Statistical summary for an association signal |
| [status](status.md) | Status or state of a clinical trial or other process |
| [substages](substages.md) |  |
| [subtype](subtype.md) |  |
| [subtype_frequency](subtype_frequency.md) | Frequency of this subtype among all cases of the parent disease (e |
| [subtype_term](subtype_term.md) | The MONDO term for a disease subtype |
| [subtypes](subtypes.md) |  |
| [supporting_text](supporting_text.md) | Exact excerpt/quote from the publication supporting the statement |
| [supports](supports.md) |  |
| [synonyms](synonyms.md) |  |
| [target](target.md) | The name of the target element in a causal relationship |
| [target_mechanisms](target_mechanisms.md) | Pathophysiology mechanism nodes that this treatment targets or modulates |
| [target_phenotypes](target_phenotypes.md) | Phenotypes that this treatment or trial addresses or targets |
| [term](term.md) | Optional structured ontology term reference |
| [therapeutic_agent](therapeutic_agent.md) | The drug, chemical, or therapeutic agent used in a treatment |
| [tissue_term](tissue_term.md) | UBERON term for the tissue |
| [title](title.md) | Title of the publication |
| [transmission](transmission.md) |  |
| [treatment_effect](treatment_effect.md) | How the treatment affects the targeted mechanism |
| [treatment_term](treatment_term.md) | The MAXO term for this treatment/medical action |
| [treatments](treatments.md) |  |
| [triggers](triggers.md) |  |
| [type](type.md) |  |
| [unit](unit.md) |  |
| [updated_date](updated_date.md) | ISO 8601/RFC 3339 timestamp string for when this disease entry was last updat... |
| [upstream_disorder](upstream_disorder.md) | Upstream disorder referenced in a hypothesis |
| [value](value.md) | The value/filler in a qualifier |
| [variants](variants.md) |  |
| [vectors](vectors.md) |  |
| [zygosity](zygosity.md) | Zygosity context |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AnatomicalEntityTerm](AnatomicalEntityTerm.md) | A term representing an anatomical entity |
| [AssayTerm](AssayTerm.md) | A term representing an assay |
| [AssociationMetricTypeEnum](AssociationMetricTypeEnum.md) | Type of association metric |
| [AssociationSignalMethodEnum](AssociationSignalMethodEnum.md) | Method used to derive an association signal |
| [AssociationSignalSourceEnum](AssociationSignalSourceEnum.md) | Source of an association signal |
| [BiologicalProcessTerm](BiologicalProcessTerm.md) | A term representing a biological process or pathway |
| [BiomarkerTerm](BiomarkerTerm.md) | A biomarker term from NCIT |
| [CausalLinkTypeEnum](CausalLinkTypeEnum.md) | Degree of mechanistic directness represented by a causal edge |
| [CellTypeTerm](CellTypeTerm.md) | A cell type |
| [CellularComponentTerm](CellularComponentTerm.md) | A term representing a cellular component |
| [ChannelopathyOrganSystemEnum](ChannelopathyOrganSystemEnum.md) | Classification categories for channelopathies by affected organ system |
| [ChemicalEntityTerm](ChemicalEntityTerm.md) | A term representing a chemical entity |
| [ClinicalSignificanceEnum](ClinicalSignificanceEnum.md) | The clinical significance of a variant for a condition (ACMG guidelines) |
| [ClinicalTrialPhaseEnum](ClinicalTrialPhaseEnum.md) | Clinical trial phase categories per FDA/NIH standards |
| [ClinicalTrialStatusEnum](ClinicalTrialStatusEnum.md) | Clinical trial recruitment and status categories per ClinicalTrials |
| [ComorbidityDirectionEnum](ComorbidityDirectionEnum.md) | Directionality of a comorbidity/trajectory association |
| [ComputationalModelTypeEnum](ComputationalModelTypeEnum.md) | Type of computational or in-silico model |
| [ConditionCompositionEnum](ConditionCompositionEnum.md) | Composition type for a composite condition descriptor |
| [CurationActionEnum](CurationActionEnum.md) | Simple action types for curation audit trail |
| [CurationStatusEnum](CurationStatusEnum.md) | Curation workflow status for an association |
| [DatasetTypeEnum](DatasetTypeEnum.md) | Type of dataset or data resource |
| [DefinitionTypeEnum](DefinitionTypeEnum.md) | The type of definition or criteria set |
| [DiseaseTerm](DiseaseTerm.md) | A disease or medical condition |
| [EnvironmentTerm](EnvironmentTerm.md) | A term representing an environmental context, material, or feature (from ENVO... |
| [EvidenceItemSupportEnum](EvidenceItemSupportEnum.md) | The level of support for an evidence item |
| [EvidenceSourceEnum](EvidenceSourceEnum.md) | The provenance/source of the evidence item |
| [ExposureTerm](ExposureTerm.md) | A term representing an exposure event (from ECTO or XCO) |
| [ExpressivityEnum](ExpressivityEnum.md) | Expressivity classification for inheritance |
| [FrequencyEnum](FrequencyEnum.md) | The frequency of an event or phenomenon |
| [GeneProductTerm](GeneProductTerm.md) | A gene product term from NCIT |
| [GeneTerm](GeneTerm.md) | A gene term from HGNC |
| [GeographyTerm](GeographyTerm.md) | A place or location |
| [HarrisonsChapterEnum](HarrisonsChapterEnum.md) | Traditional internal medicine chapter groupings for disease classification |
| [HistopathologyFindingTerm](HistopathologyFindingTerm.md) | A histopathologic finding term from NCIT |
| [ICD10CMTerm](ICD10CMTerm.md) | An ICD-10-CM diagnosis code |
| [ICD11FTerm](ICD11FTerm.md) | An ICD-11 Foundation diagnosis code |
| [ICDOMorphologyEnum](ICDOMorphologyEnum.md) | ICD-O morphology axis classification for cancer subtypes |
| [InheritanceTerm](InheritanceTerm.md) | A term representing mode of inheritance |
| [IUISCategoryEnum](IUISCategoryEnum.md) | IUIS classification tables for inborn errors of immunity (IEI) |
| [LateralityEnum](LateralityEnum.md) | Laterality qualifier for anatomical structures or procedures |
| [LifeCycleStageTerm](LifeCycleStageTerm.md) | A parasite life cycle stage term (from OPL) |
| [LysosomalStorageEnum](LysosomalStorageEnum.md) | Classification of lysosomal storage diseases by accumulated substrate type |
| [MappingConsistencyEnum](MappingConsistencyEnum.md) | Consistency of a mapping relative to another reference source |
| [MechanisticHypothesisStatusEnum](MechanisticHypothesisStatusEnum.md) | Curation/maturity status for a disease-level mechanistic hypothesis |
| [MechanisticNosologyEnum](MechanisticNosologyEnum.md) | Classification of diseases by molecular mechanism or affected cellular system |
| [ModifierEnum](ModifierEnum.md) | Qualifiers for direction, intensity, or pathological state of a descriptor |
| [OnsetEnum](OnsetEnum.md) | Age of onset categories from HPO |
| [OrganismTerm](OrganismTerm.md) | A term representing an organism from NCBITaxon |
| [PenetranceEnum](PenetranceEnum.md) | Penetrance classification for inheritance |
| [PhaseTerm](PhaseTerm.md) | A phase or stage |
| [PhenotypeCategoryEnum](PhenotypeCategoryEnum.md) | Broad phenotype categories from the Human Phenotype Ontology |
| [PhenotypeTerm](PhenotypeTerm.md) | A term representing a phenotype or disease manifestation |
| [ProteinComplexTerm](ProteinComplexTerm.md) | A term representing a protein complex |
| [RegimenTerm](RegimenTerm.md) | A term representing a treatment regimen (from NCIT) |
| [SexEnum](SexEnum.md) | Sex-specific stratum |
| [TreatmentActionTerm](TreatmentActionTerm.md) | A term representing a medical action or treatment (from MAXO) |
| [TreatmentEffectEnum](TreatmentEffectEnum.md) | How a treatment affects a pathophysiology mechanism node |
| [TriggerTerm](TriggerTerm.md) | A trigger |
| [ZygosityEnum](ZygosityEnum.md) | Zygosity categories from GENO |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [FrequencyQuantity](FrequencyQuantity.md) |  |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [PMID](PMID.md) |  |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
