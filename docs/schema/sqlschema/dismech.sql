-- # Class: Any
--     * Slot: id
-- # Class: CurationEvent Description: A single curation event in the audit trail
--     * Slot: id
--     * Slot: curation_timestamp Description: ISO 8601 timestamp of the curation event
--     * Slot: curation_model Description: Model identifier used for curation (e.g., claude-opus-4-5-20251101)
--     * Slot: curation_action Description: Type of curation action performed
--     * Slot: curation_description Description: Human-readable description of changes made
--     * Slot: Disease_name Description: Autocreated FK slot
-- # Class: Term Description: A structured reference to an ontology term
--     * Slot: id Description: Ontology term identifier (CURIE)
--     * Slot: label Description: Human-readable label for the ontology term
-- # Abstract Class: Descriptor Description: Base class for structured descriptors that allow a preferred term, optional description, optional ontology term binding, and post-composition via modifier, located_in, and laterality slots.
--     * Slot: id
--     * Slot: preferred_term Description: The preferred human-readable term for this descriptor
--     * Slot: description Description: A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.
--     * Slot: modifier Description: Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)
--     * Slot: laterality Description: Laterality qualifier (left, right, or bilateral)
--     * Slot: term_id Description: Optional structured ontology term reference
--     * Slot: located_in_id Description: Anatomical location where this entity/process occurs or procedure is performed
-- # Class: Qualifier Description: A predicate-value pair for formal post-composition. Allows OWL-like expressivity with controlled predicates and values, both as full Descriptors.
--     * Slot: id
--     * Slot: Descriptor_id Description: Autocreated FK slot
--     * Slot: CellTypeDescriptor_id Description: Autocreated FK slot
--     * Slot: BiologicalProcessDescriptor_id Description: Autocreated FK slot
--     * Slot: AnatomicalEntityDescriptor_id Description: Autocreated FK slot
--     * Slot: ChemicalEntityDescriptor_id Description: Autocreated FK slot
--     * Slot: GeneDescriptor_id Description: Autocreated FK slot
--     * Slot: CellularComponentDescriptor_id Description: Autocreated FK slot
--     * Slot: AssayDescriptor_id Description: Autocreated FK slot
--     * Slot: TriggerDescriptor_id Description: Autocreated FK slot
--     * Slot: DiseaseDescriptor_id Description: Autocreated FK slot
--     * Slot: PhenotypeDescriptor_id Description: Autocreated FK slot
--     * Slot: TreatmentDescriptor_id Description: Autocreated FK slot
--     * Slot: ExposureDescriptor_id Description: Autocreated FK slot
--     * Slot: EnvironmentDescriptor_id Description: Autocreated FK slot
--     * Slot: OrganismDescriptor_id Description: Autocreated FK slot
--     * Slot: SampleTypeDescriptor_id Description: Autocreated FK slot
--     * Slot: predicate_id Description: The relationship/predicate in a qualifier (e.g., RO:0002233 'has input')
--     * Slot: value_id Description: The value/filler in a qualifier
-- # Class: CellTypeDescriptor Description: A descriptor for cell types, bindable to Cell Ontology (CL)
--     * Slot: id
--     * Slot: preferred_term Description: The preferred human-readable term for this descriptor
--     * Slot: description Description: A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.
--     * Slot: modifier Description: Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)
--     * Slot: laterality Description: Laterality qualifier (left, right, or bilateral)
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: Biochemical_name Description: Autocreated FK slot
--     * Slot: term_id Description: Optional Cell Ontology term reference
--     * Slot: located_in_id Description: Anatomical location where this entity/process occurs or procedure is performed
-- # Class: BiologicalProcessDescriptor Description: A descriptor for biological processes, bindable to Gene Ontology (GO)
--     * Slot: id
--     * Slot: preferred_term Description: The preferred human-readable term for this descriptor
--     * Slot: description Description: A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.
--     * Slot: modifier Description: Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)
--     * Slot: laterality Description: Laterality qualifier (left, right, or bilateral)
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: term_id Description: Optional GO biological process term reference
--     * Slot: located_in_id Description: Anatomical location where this entity/process occurs or procedure is performed
-- # Class: AnatomicalEntityDescriptor Description: A descriptor for anatomical locations, bindable to UBERON
--     * Slot: id
--     * Slot: preferred_term Description: The preferred human-readable term for this descriptor
--     * Slot: description Description: A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.
--     * Slot: modifier Description: Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)
--     * Slot: laterality Description: Laterality qualifier (left, right, or bilateral)
--     * Slot: Subtype_name Description: Autocreated FK slot
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: term_id Description: Optional UBERON anatomical entity term reference
--     * Slot: located_in_id Description: Anatomical location where this entity/process occurs or procedure is performed
-- # Class: ChemicalEntityDescriptor Description: A descriptor for chemical entities, bindable to CHEBI
--     * Slot: id
--     * Slot: preferred_term Description: The preferred human-readable term for this descriptor
--     * Slot: description Description: A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.
--     * Slot: modifier Description: Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)
--     * Slot: laterality Description: Laterality qualifier (left, right, or bilateral)
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: term_id Description: Optional CHEBI chemical entity term reference
--     * Slot: located_in_id Description: Anatomical location where this entity/process occurs or procedure is performed
-- # Class: GeneDescriptor Description: A descriptor for genes, bindable to HGNC or other gene databases
--     * Slot: id
--     * Slot: preferred_term Description: The preferred human-readable term for this descriptor
--     * Slot: description Description: A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.
--     * Slot: modifier Description: Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)
--     * Slot: laterality Description: Laterality qualifier (left, right, or bilateral)
--     * Slot: Dataset_accession Description: Autocreated FK slot
--     * Slot: ComputationalModel_name Description: Autocreated FK slot
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: AnimalModel_id Description: Autocreated FK slot
--     * Slot: term_id Description: Optional gene database term reference (e.g., HGNC)
--     * Slot: located_in_id Description: Anatomical location where this entity/process occurs or procedure is performed
-- # Class: CellularComponentDescriptor Description: A descriptor for cellular components, bindable to GO cellular component
--     * Slot: id
--     * Slot: preferred_term Description: The preferred human-readable term for this descriptor
--     * Slot: description Description: A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.
--     * Slot: modifier Description: Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)
--     * Slot: laterality Description: Laterality qualifier (left, right, or bilateral)
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: term_id Description: Optional GO cellular component term reference
--     * Slot: located_in_id Description: Anatomical location where this entity/process occurs or procedure is performed
-- # Class: AssayDescriptor Description: A descriptor for assays, bindable to OBI
--     * Slot: id
--     * Slot: preferred_term Description: The preferred human-readable term for this descriptor
--     * Slot: description Description: A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.
--     * Slot: modifier Description: Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)
--     * Slot: laterality Description: Laterality qualifier (left, right, or bilateral)
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: Biochemical_name Description: Autocreated FK slot
--     * Slot: term_id Description: Optional OBI assay term reference
--     * Slot: located_in_id Description: Anatomical location where this entity/process occurs or procedure is performed
-- # Class: TriggerDescriptor Description: A descriptor for triggers/causes
--     * Slot: id
--     * Slot: preferred_term Description: The preferred human-readable term for this descriptor
--     * Slot: description Description: A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.
--     * Slot: modifier Description: Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)
--     * Slot: laterality Description: Laterality qualifier (left, right, or bilateral)
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: term_id Description: Optional ontology term reference
--     * Slot: located_in_id Description: Anatomical location where this entity/process occurs or procedure is performed
-- # Class: DiseaseDescriptor Description: A descriptor for the focal disease, bindable to MONDO
--     * Slot: id
--     * Slot: preferred_term Description: The preferred human-readable term for this descriptor
--     * Slot: description Description: A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.
--     * Slot: modifier Description: Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)
--     * Slot: laterality Description: Laterality qualifier (left, right, or bilateral)
--     * Slot: term_id Description: Optional MONDO disease term reference
--     * Slot: located_in_id Description: Anatomical location where this entity/process occurs or procedure is performed
-- # Class: PhenotypeDescriptor Description: A descriptor for phenotypes, bindable to Human Phenotype Ontology (HP)
--     * Slot: id
--     * Slot: preferred_term Description: The preferred human-readable term for this descriptor
--     * Slot: description Description: A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.
--     * Slot: modifier Description: Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)
--     * Slot: laterality Description: Laterality qualifier (left, right, or bilateral)
--     * Slot: term_id Description: Optional HP phenotype term reference
--     * Slot: located_in_id Description: Anatomical location where this entity/process occurs or procedure is performed
-- # Class: TreatmentDescriptor Description: A descriptor for treatments/medical actions, bindable to Medical Action Ontology (MAXO)
--     * Slot: id
--     * Slot: preferred_term Description: The preferred human-readable term for this descriptor
--     * Slot: description Description: A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.
--     * Slot: modifier Description: Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)
--     * Slot: laterality Description: Laterality qualifier (left, right, or bilateral)
--     * Slot: term_id Description: Optional MAXO treatment term reference
--     * Slot: located_in_id Description: Anatomical location where this entity/process occurs or procedure is performed
-- # Class: ExposureDescriptor Description: A descriptor for exposure events, bindable to ECTO or XCO
--     * Slot: id
--     * Slot: preferred_term Description: The preferred human-readable term for this descriptor
--     * Slot: description Description: A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.
--     * Slot: modifier Description: Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)
--     * Slot: laterality Description: Laterality qualifier (left, right, or bilateral)
--     * Slot: Dataset_accession Description: Autocreated FK slot
--     * Slot: term_id Description: Optional ECTO/XCO exposure term reference
--     * Slot: located_in_id Description: Anatomical location where this entity/process occurs or procedure is performed
-- # Class: EnvironmentDescriptor Description: A descriptor for environmental contexts/settings, bindable to ENVO
--     * Slot: id
--     * Slot: preferred_term Description: The preferred human-readable term for this descriptor
--     * Slot: description Description: A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.
--     * Slot: modifier Description: Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)
--     * Slot: laterality Description: Laterality qualifier (left, right, or bilateral)
--     * Slot: term_id Description: Optional ENVO environment term reference
--     * Slot: located_in_id Description: Anatomical location where this entity/process occurs or procedure is performed
-- # Class: OrganismDescriptor Description: A descriptor for organisms, bindable to NCBITaxon
--     * Slot: id
--     * Slot: preferred_term Description: The preferred human-readable term for this descriptor
--     * Slot: description Description: A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.
--     * Slot: modifier Description: Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)
--     * Slot: laterality Description: Laterality qualifier (left, right, or bilateral)
--     * Slot: term_id Description: NCBITaxon term reference
--     * Slot: located_in_id Description: Anatomical location where this entity/process occurs or procedure is performed
-- # Class: SampleTypeDescriptor Description: A descriptor for biological sample types (tissue and/or cell type)
--     * Slot: id
--     * Slot: preferred_term Description: The preferred human-readable term for this descriptor
--     * Slot: description Description: A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.
--     * Slot: modifier Description: Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)
--     * Slot: laterality Description: Laterality qualifier (left, right, or bilateral)
--     * Slot: Dataset_accession Description: Autocreated FK slot
--     * Slot: tissue_term_id Description: UBERON term for the tissue
--     * Slot: cell_type_term_id Description: CL term for the cell type
--     * Slot: term_id Description: Optional structured ontology term reference
--     * Slot: located_in_id Description: Anatomical location where this entity/process occurs or procedure is performed
-- # Class: Dataset Description: A reference to a publicly available omics or phenotype dataset
--     * Slot: accession Description: Dataset accession identifier as a CURIE (e.g., geo:GSE67472)
--     * Slot: title Description: Title of the publication
--     * Slot: description Description: A description of the dataset. This may typically be redundant with the `title` slot, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the title slot.
--     * Slot: data_type Description: The type of omics or other data in the dataset
--     * Slot: sample_count Description: Total number of samples in the dataset
--     * Slot: platform Description: Sequencing or array platform used
--     * Slot: publication Description: Associated publication (PMID)
--     * Slot: notes
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: organism_id Description: The organism from which samples were derived
-- # Class: ComputationalModel Description: A computational or in-silico model relevant to understanding disease mechanisms
--     * Slot: name
--     * Slot: description
--     * Slot: model_type Description: Type of computational model
--     * Slot: repository_url Description: URL to model repository (GitHub, BiGG, VMH, BioModels)
--     * Slot: model_id Description: Identifier within the repository (e.g., Recon3D, BIOMD0000000123)
--     * Slot: base_model Description: Parent/base model this is derived from (e.g., Recon3D, Harvey 1.0)
--     * Slot: model_software Description: Software/toolbox for running the model (e.g., COBRApy, COBRA Toolbox)
--     * Slot: model_format Description: File format (e.g., SBML, MATLAB, JSON, ONNX)
--     * Slot: publication Description: Associated publication (PMID)
--     * Slot: notes
--     * Slot: Disease_name Description: Autocreated FK slot
-- # Class: DifferentialDiagnosis Description: A disease or condition that presents similarly to the focal disease and must be differentiated
--     * Slot: name
--     * Slot: description Description: Clinical or mechanistic overlaps, shared presentations, and diagnostic considerations with the focal disease
--     * Slot: notes Description: Additional clinical notes or management considerations
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: disease_term_id Description: The MONDO disease term for this disease
-- # Class: Subtype
--     * Slot: name
--     * Slot: description
--     * Slot: review_notes
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: InfectiousAgent_name Description: Autocreated FK slot
--     * Slot: subtype_term_id Description: The MONDO term for a disease subtype
-- # Class: EvidenceItem
--     * Slot: id
--     * Slot: reference Description: The authoritative reference (publication) for this evidence item
--     * Slot: supports
--     * Slot: snippet Description: An exact excerpt/quote from the referenced publication that supports or refutes the claim
--     * Slot: explanation
--     * Slot: Dataset_accession Description: Autocreated FK slot
--     * Slot: ComputationalModel_name Description: Autocreated FK slot
--     * Slot: DifferentialDiagnosis_name Description: Autocreated FK slot
--     * Slot: Subtype_name Description: Autocreated FK slot
--     * Slot: CausalEdge_id Description: Autocreated FK slot
--     * Slot: Prevalence_id Description: Autocreated FK slot
--     * Slot: ProgressionInfo_id Description: Autocreated FK slot
--     * Slot: EpidemiologyInfo_name Description: Autocreated FK slot
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: Phenotype_name Description: Autocreated FK slot
--     * Slot: Biochemical_name Description: Autocreated FK slot
--     * Slot: Genetic_name Description: Autocreated FK slot
--     * Slot: Environmental_name Description: Autocreated FK slot
--     * Slot: Stage_name Description: Autocreated FK slot
--     * Slot: AnimalModel_id Description: Autocreated FK slot
--     * Slot: Treatment_name Description: Autocreated FK slot
--     * Slot: InfectiousAgent_name Description: Autocreated FK slot
--     * Slot: Transmission_name Description: Autocreated FK slot
--     * Slot: Diagnosis_name Description: Autocreated FK slot
--     * Slot: Inheritance_name Description: Autocreated FK slot
--     * Slot: Variant_name Description: Autocreated FK slot
--     * Slot: ModelingConsideration_name Description: Autocreated FK slot
-- # Class: CausalEdge Description: A reference to a downstream effect or consequence in a causal relationship
--     * Slot: id
--     * Slot: target Description: The name of the target element in a causal relationship
--     * Slot: description
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: Phenotype_name Description: Autocreated FK slot
-- # Class: PublicationReference Description: A reference to a publication with associated findings
--     * Slot: reference Description: The authoritative reference (publication) for this evidence item
--     * Slot: title Description: Title of the publication
--     * Slot: Disease_name Description: Autocreated FK slot
-- # Class: Finding Description: A key finding or claim extracted from a publication
--     * Slot: id
--     * Slot: statement Description: A key finding or claim from the publication
--     * Slot: supporting_text Description: Exact excerpt/quote from the publication supporting the statement
--     * Slot: PublicationReference_reference Description: Autocreated FK slot
-- # Class: Prevalence
--     * Slot: id
--     * Slot: subtype
--     * Slot: population
--     * Slot: notes
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: percentage_id
-- # Class: ProgressionInfo
--     * Slot: id
--     * Slot: phase
--     * Slot: subtype
--     * Slot: age_range
--     * Slot: incubation_days
--     * Slot: review_notes
--     * Slot: incubation_years
--     * Slot: notes
--     * Slot: duration_days
--     * Slot: duration
--     * Slot: Disease_name Description: Autocreated FK slot
-- # Class: EpidemiologyInfo
--     * Slot: name
--     * Slot: description
--     * Slot: minimum_value
--     * Slot: maximum_value
--     * Slot: mean_range
--     * Slot: notes
--     * Slot: unit
--     * Slot: Disease_name Description: Autocreated FK slot
-- # Class: Pathophysiology
--     * Slot: name
--     * Slot: description
--     * Slot: role
--     * Slot: consequence
--     * Slot: notes
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: Stage_name Description: Autocreated FK slot
--     * Slot: gene_id
--     * Slot: frequency_id
-- # Class: Phenotype
--     * Slot: category
--     * Slot: name
--     * Slot: description
--     * Slot: diagnostic
--     * Slot: context
--     * Slot: review_notes
--     * Slot: severity
--     * Slot: notes
--     * Slot: subtype
--     * Slot: DifferentialDiagnosis_name Description: Autocreated FK slot
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: phenotype_term_id Description: The HP term for this phenotype
--     * Slot: frequency_id
-- # Class: Biochemical
--     * Slot: name
--     * Slot: presence
--     * Slot: specificity
--     * Slot: notes
--     * Slot: context
--     * Slot: subtype
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: biomarker_term_id Description: Ontology term for a biomarker (from NCIT, CHEBI, or LOINC)
--     * Slot: frequency_id
-- # Class: Genetic
--     * Slot: name
--     * Slot: presence
--     * Slot: association
--     * Slot: review_notes
--     * Slot: subtype
--     * Slot: features
--     * Slot: notes
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: frequency_id
-- # Class: Environmental Description: An environmental factor, exposure, or context relevant to disease
--     * Slot: name
--     * Slot: presence
--     * Slot: notes
--     * Slot: description
--     * Slot: effect
--     * Slot: review_notes
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: exposure_term_id Description: The ECTO/XCO term for this exposure event
--     * Slot: environment_context_id Description: The ENVO term for the environmental context/setting
-- # Class: Disease
--     * Slot: name
--     * Slot: description
--     * Slot: category
--     * Slot: notes
--     * Slot: review_notes
--     * Slot: DiseaseCollection_id Description: Autocreated FK slot
--     * Slot: disease_term_id Description: The MONDO disease term for this disease
-- # Class: Stage
--     * Slot: name
--     * Slot: description
--     * Slot: notes
--     * Slot: context
--     * Slot: review_notes
--     * Slot: role
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: Stage_name Description: Autocreated FK slot
-- # Class: AnimalModel
--     * Slot: id
--     * Slot: species
--     * Slot: genotype
--     * Slot: background
--     * Slot: category
--     * Slot: description
--     * Slot: Disease_name Description: Autocreated FK slot
-- # Class: Treatment
--     * Slot: name
--     * Slot: description
--     * Slot: notes
--     * Slot: context
--     * Slot: review_notes
--     * Slot: role
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: treatment_term_id Description: The MAXO term for this treatment/medical action
-- # Class: InfectiousAgent
--     * Slot: name
--     * Slot: description
--     * Slot: Disease_name Description: Autocreated FK slot
-- # Class: Transmission
--     * Slot: name
--     * Slot: description
--     * Slot: notes
--     * Slot: effect
--     * Slot: Disease_name Description: Autocreated FK slot
-- # Class: Assay
--     * Slot: name
--     * Slot: description
-- # Class: Diagnosis
--     * Slot: name
--     * Slot: presence
--     * Slot: notes
--     * Slot: results
--     * Slot: markers
--     * Slot: description
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: diagnosis_term_id Description: The MAXO term for this diagnostic procedure
-- # Class: Inheritance
--     * Slot: name
--     * Slot: description
--     * Slot: Genetic_name Description: Autocreated FK slot
--     * Slot: Disease_name Description: Autocreated FK slot
-- # Class: Variant
--     * Slot: name
--     * Slot: description
--     * Slot: sequence_length
--     * Slot: clinical_significance
--     * Slot: type
--     * Slot: Genetic_name Description: Autocreated FK slot
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: gene_id
-- # Class: FunctionalEffect
--     * Slot: id
--     * Slot: function
--     * Slot: description
--     * Slot: type
--     * Slot: Variant_name Description: Autocreated FK slot
-- # Class: Mechanism
--     * Slot: name
--     * Slot: description
--     * Slot: Treatment_name Description: Autocreated FK slot
-- # Class: ModelingConsideration
--     * Slot: name
--     * Slot: description
--     * Slot: Disease_name Description: Autocreated FK slot
-- # Class: DiseaseCollection
--     * Slot: id
-- # Class: Dataset_conditions
--     * Slot: Dataset_accession Description: Autocreated FK slot
--     * Slot: conditions Description: Experimental conditions or disease states represented
-- # Class: DifferentialDiagnosis_distinguishing_features
--     * Slot: DifferentialDiagnosis_name Description: Autocreated FK slot
--     * Slot: distinguishing_features Description: Key clinical, laboratory, imaging, or epidemiological features that help differentiate this condition from the focal disease
-- # Class: Subtype_geography
--     * Slot: Subtype_name Description: Autocreated FK slot
--     * Slot: geography
-- # Class: EpidemiologyInfo_factors
--     * Slot: EpidemiologyInfo_name Description: Autocreated FK slot
--     * Slot: factors
-- # Class: Pathophysiology_examples
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: examples
-- # Class: Pathophysiology_synonyms
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: synonyms
-- # Class: Pathophysiology_consequences
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: consequences
-- # Class: Pathophysiology_subtypes
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: subtypes
-- # Class: Pathophysiology_mechanisms
--     * Slot: Pathophysiology_name Description: Autocreated FK slot
--     * Slot: mechanisms
-- # Class: Biochemical_synonyms
--     * Slot: Biochemical_name Description: Autocreated FK slot
--     * Slot: synonyms
-- # Class: Genetic_examples
--     * Slot: Genetic_name Description: Autocreated FK slot
--     * Slot: examples
-- # Class: Environmental_chemicals
--     * Slot: Environmental_name Description: Autocreated FK slot
--     * Slot: chemicals
-- # Class: Environmental_synonyms
--     * Slot: Environmental_name Description: Autocreated FK slot
--     * Slot: synonyms
-- # Class: Environmental_examples
--     * Slot: Environmental_name Description: Autocreated FK slot
--     * Slot: examples
-- # Class: Disease_parents
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: parents
-- # Class: Disease_categories
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: categories
-- # Class: Disease_synonyms
--     * Slot: Disease_name Description: Autocreated FK slot
--     * Slot: synonyms
-- # Class: Stage_examples
--     * Slot: Stage_name Description: Autocreated FK slot
--     * Slot: examples
-- # Class: AnimalModel_alleles
--     * Slot: AnimalModel_id Description: Autocreated FK slot
--     * Slot: alleles
-- # Class: AnimalModel_associated_phenotypes
--     * Slot: AnimalModel_id Description: Autocreated FK slot
--     * Slot: associated_phenotypes
-- # Class: Treatment_target_phenotypes
--     * Slot: Treatment_name Description: Autocreated FK slot
--     * Slot: target_phenotypes Description: Names of phenotypes that this treatment addresses or targets
-- # Class: Treatment_examples
--     * Slot: Treatment_name Description: Autocreated FK slot
--     * Slot: examples
-- # Class: Variant_synonyms
--     * Slot: Variant_name Description: Autocreated FK slot
--     * Slot: synonyms
-- # Class: Variant_identifiers
--     * Slot: Variant_name Description: Autocreated FK slot
--     * Slot: identifiers

CREATE TABLE "Any" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Any_id" ON "Any" (id);
CREATE TABLE "Term" (
	id TEXT NOT NULL,
	label TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Term_id" ON "Term" (id);
CREATE TABLE "AnatomicalEntityDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	modifier VARCHAR(12),
	laterality VARCHAR(9),
	"Subtype_name" TEXT,
	"Pathophysiology_name" TEXT,
	term_id TEXT,
	located_in_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Subtype_name") REFERENCES "Subtype" (name),
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name),
	FOREIGN KEY(term_id) REFERENCES "Term" (id),
	FOREIGN KEY(located_in_id) REFERENCES "AnatomicalEntityDescriptor" (id)
);CREATE INDEX "ix_AnatomicalEntityDescriptor_id" ON "AnatomicalEntityDescriptor" (id);
CREATE TABLE "GeneDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	modifier VARCHAR(12),
	laterality VARCHAR(9),
	"Dataset_accession" TEXT,
	"ComputationalModel_name" TEXT,
	"Pathophysiology_name" TEXT,
	"AnimalModel_id" INTEGER,
	term_id TEXT,
	located_in_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Dataset_accession") REFERENCES "Dataset" (accession),
	FOREIGN KEY("ComputationalModel_name") REFERENCES "ComputationalModel" (name),
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name),
	FOREIGN KEY("AnimalModel_id") REFERENCES "AnimalModel" (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id),
	FOREIGN KEY(located_in_id) REFERENCES "AnatomicalEntityDescriptor" (id)
);CREATE INDEX "ix_GeneDescriptor_id" ON "GeneDescriptor" (id);
CREATE TABLE "DiseaseDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	modifier VARCHAR(12),
	laterality VARCHAR(9),
	term_id TEXT,
	located_in_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id),
	FOREIGN KEY(located_in_id) REFERENCES "AnatomicalEntityDescriptor" (id)
);CREATE INDEX "ix_DiseaseDescriptor_id" ON "DiseaseDescriptor" (id);
CREATE TABLE "OrganismDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	modifier VARCHAR(12),
	laterality VARCHAR(9),
	term_id TEXT,
	located_in_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id),
	FOREIGN KEY(located_in_id) REFERENCES "AnatomicalEntityDescriptor" (id)
);CREATE INDEX "ix_OrganismDescriptor_id" ON "OrganismDescriptor" (id);
CREATE TABLE "Dataset" (
	accession TEXT NOT NULL,
	title TEXT,
	description TEXT,
	data_type VARCHAR(23),
	sample_count INTEGER,
	platform TEXT,
	publication TEXT,
	notes TEXT,
	"Disease_name" TEXT,
	organism_id INTEGER,
	PRIMARY KEY (accession),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name),
	FOREIGN KEY(organism_id) REFERENCES "OrganismDescriptor" (id)
);CREATE INDEX "ix_Dataset_accession" ON "Dataset" (accession);
CREATE TABLE "ComputationalModel" (
	name TEXT NOT NULL,
	description TEXT,
	model_type VARCHAR(23),
	repository_url TEXT,
	model_id TEXT,
	base_model TEXT,
	model_software TEXT,
	model_format TEXT,
	publication TEXT,
	notes TEXT,
	"Disease_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);CREATE INDEX "ix_ComputationalModel_name" ON "ComputationalModel" (name);
CREATE TABLE "Subtype" (
	name TEXT NOT NULL,
	description TEXT,
	review_notes TEXT,
	"Disease_name" TEXT,
	"InfectiousAgent_name" TEXT,
	subtype_term_id INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name),
	FOREIGN KEY("InfectiousAgent_name") REFERENCES "InfectiousAgent" (name),
	FOREIGN KEY(subtype_term_id) REFERENCES "DiseaseDescriptor" (id)
);CREATE INDEX "ix_Subtype_name" ON "Subtype" (name);
CREATE TABLE "Pathophysiology" (
	name TEXT NOT NULL,
	description TEXT,
	role TEXT,
	consequence TEXT,
	notes TEXT,
	"Disease_name" TEXT,
	"Stage_name" TEXT,
	gene_id INTEGER,
	frequency_id INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name),
	FOREIGN KEY("Stage_name") REFERENCES "Stage" (name),
	FOREIGN KEY(gene_id) REFERENCES "GeneDescriptor" (id),
	FOREIGN KEY(frequency_id) REFERENCES "Any" (id)
);CREATE INDEX "ix_Pathophysiology_name" ON "Pathophysiology" (name);
CREATE TABLE "Disease" (
	name TEXT NOT NULL,
	description TEXT,
	category TEXT,
	notes TEXT,
	review_notes TEXT,
	"DiseaseCollection_id" INTEGER,
	disease_term_id INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("DiseaseCollection_id") REFERENCES "DiseaseCollection" (id),
	FOREIGN KEY(disease_term_id) REFERENCES "DiseaseDescriptor" (id)
);CREATE INDEX "ix_Disease_name" ON "Disease" (name);
CREATE TABLE "Stage" (
	name TEXT NOT NULL,
	description TEXT,
	notes TEXT,
	context TEXT,
	review_notes TEXT,
	role TEXT,
	"Disease_name" TEXT,
	"Stage_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name),
	FOREIGN KEY("Stage_name") REFERENCES "Stage" (name)
);CREATE INDEX "ix_Stage_name" ON "Stage" (name);
CREATE TABLE "AnimalModel" (
	id INTEGER NOT NULL,
	species TEXT,
	genotype TEXT,
	background TEXT,
	category TEXT,
	description TEXT,
	"Disease_name" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);CREATE INDEX "ix_AnimalModel_id" ON "AnimalModel" (id);
CREATE TABLE "InfectiousAgent" (
	name TEXT NOT NULL,
	description TEXT,
	"Disease_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);CREATE INDEX "ix_InfectiousAgent_name" ON "InfectiousAgent" (name);
CREATE TABLE "Assay" (
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_Assay_name" ON "Assay" (name);
CREATE TABLE "DiseaseCollection" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_DiseaseCollection_id" ON "DiseaseCollection" (id);
CREATE TABLE "CurationEvent" (
	id INTEGER NOT NULL,
	curation_timestamp DATETIME NOT NULL,
	curation_model TEXT,
	curation_action VARCHAR(7),
	curation_description TEXT,
	"Disease_name" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);CREATE INDEX "ix_CurationEvent_id" ON "CurationEvent" (id);
CREATE TABLE "Descriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	modifier VARCHAR(12),
	laterality VARCHAR(9),
	term_id TEXT,
	located_in_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id),
	FOREIGN KEY(located_in_id) REFERENCES "AnatomicalEntityDescriptor" (id)
);CREATE INDEX "ix_Descriptor_id" ON "Descriptor" (id);
CREATE TABLE "BiologicalProcessDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	modifier VARCHAR(12),
	laterality VARCHAR(9),
	"Pathophysiology_name" TEXT,
	term_id TEXT,
	located_in_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name),
	FOREIGN KEY(term_id) REFERENCES "Term" (id),
	FOREIGN KEY(located_in_id) REFERENCES "AnatomicalEntityDescriptor" (id)
);CREATE INDEX "ix_BiologicalProcessDescriptor_id" ON "BiologicalProcessDescriptor" (id);
CREATE TABLE "ChemicalEntityDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	modifier VARCHAR(12),
	laterality VARCHAR(9),
	"Pathophysiology_name" TEXT,
	term_id TEXT,
	located_in_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name),
	FOREIGN KEY(term_id) REFERENCES "Term" (id),
	FOREIGN KEY(located_in_id) REFERENCES "AnatomicalEntityDescriptor" (id)
);CREATE INDEX "ix_ChemicalEntityDescriptor_id" ON "ChemicalEntityDescriptor" (id);
CREATE TABLE "CellularComponentDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	modifier VARCHAR(12),
	laterality VARCHAR(9),
	"Pathophysiology_name" TEXT,
	term_id TEXT,
	located_in_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name),
	FOREIGN KEY(term_id) REFERENCES "Term" (id),
	FOREIGN KEY(located_in_id) REFERENCES "AnatomicalEntityDescriptor" (id)
);CREATE INDEX "ix_CellularComponentDescriptor_id" ON "CellularComponentDescriptor" (id);
CREATE TABLE "TriggerDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	modifier VARCHAR(12),
	laterality VARCHAR(9),
	"Pathophysiology_name" TEXT,
	term_id TEXT,
	located_in_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name),
	FOREIGN KEY(term_id) REFERENCES "Term" (id),
	FOREIGN KEY(located_in_id) REFERENCES "AnatomicalEntityDescriptor" (id)
);CREATE INDEX "ix_TriggerDescriptor_id" ON "TriggerDescriptor" (id);
CREATE TABLE "PhenotypeDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	modifier VARCHAR(12),
	laterality VARCHAR(9),
	term_id TEXT,
	located_in_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id),
	FOREIGN KEY(located_in_id) REFERENCES "AnatomicalEntityDescriptor" (id)
);CREATE INDEX "ix_PhenotypeDescriptor_id" ON "PhenotypeDescriptor" (id);
CREATE TABLE "TreatmentDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	modifier VARCHAR(12),
	laterality VARCHAR(9),
	term_id TEXT,
	located_in_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id),
	FOREIGN KEY(located_in_id) REFERENCES "AnatomicalEntityDescriptor" (id)
);CREATE INDEX "ix_TreatmentDescriptor_id" ON "TreatmentDescriptor" (id);
CREATE TABLE "ExposureDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	modifier VARCHAR(12),
	laterality VARCHAR(9),
	"Dataset_accession" TEXT,
	term_id TEXT,
	located_in_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Dataset_accession") REFERENCES "Dataset" (accession),
	FOREIGN KEY(term_id) REFERENCES "Term" (id),
	FOREIGN KEY(located_in_id) REFERENCES "AnatomicalEntityDescriptor" (id)
);CREATE INDEX "ix_ExposureDescriptor_id" ON "ExposureDescriptor" (id);
CREATE TABLE "EnvironmentDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	modifier VARCHAR(12),
	laterality VARCHAR(9),
	term_id TEXT,
	located_in_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id),
	FOREIGN KEY(located_in_id) REFERENCES "AnatomicalEntityDescriptor" (id)
);CREATE INDEX "ix_EnvironmentDescriptor_id" ON "EnvironmentDescriptor" (id);
CREATE TABLE "DifferentialDiagnosis" (
	name TEXT NOT NULL,
	description TEXT,
	notes TEXT,
	"Disease_name" TEXT,
	disease_term_id INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name),
	FOREIGN KEY(disease_term_id) REFERENCES "DiseaseDescriptor" (id)
);CREATE INDEX "ix_DifferentialDiagnosis_name" ON "DifferentialDiagnosis" (name);
CREATE TABLE "PublicationReference" (
	reference TEXT NOT NULL,
	title TEXT,
	"Disease_name" TEXT,
	PRIMARY KEY (reference),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);CREATE INDEX "ix_PublicationReference_reference" ON "PublicationReference" (reference);
CREATE TABLE "Prevalence" (
	id INTEGER NOT NULL,
	subtype TEXT,
	population TEXT,
	notes TEXT,
	"Disease_name" TEXT,
	percentage_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name),
	FOREIGN KEY(percentage_id) REFERENCES "Any" (id)
);CREATE INDEX "ix_Prevalence_id" ON "Prevalence" (id);
CREATE TABLE "ProgressionInfo" (
	id INTEGER NOT NULL,
	phase VARCHAR,
	subtype TEXT,
	age_range TEXT,
	incubation_days TEXT,
	review_notes TEXT,
	incubation_years TEXT,
	notes TEXT,
	duration_days TEXT,
	duration TEXT,
	"Disease_name" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);CREATE INDEX "ix_ProgressionInfo_id" ON "ProgressionInfo" (id);
CREATE TABLE "EpidemiologyInfo" (
	name TEXT NOT NULL,
	description TEXT,
	minimum_value FLOAT,
	maximum_value FLOAT,
	mean_range TEXT,
	notes TEXT,
	unit TEXT,
	"Disease_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);CREATE INDEX "ix_EpidemiologyInfo_name" ON "EpidemiologyInfo" (name);
CREATE TABLE "Genetic" (
	name TEXT NOT NULL,
	presence TEXT,
	association TEXT,
	review_notes TEXT,
	subtype TEXT,
	features TEXT,
	notes TEXT,
	"Disease_name" TEXT,
	frequency_id INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name),
	FOREIGN KEY(frequency_id) REFERENCES "Any" (id)
);CREATE INDEX "ix_Genetic_name" ON "Genetic" (name);
CREATE TABLE "Transmission" (
	name TEXT NOT NULL,
	description TEXT,
	notes TEXT,
	effect TEXT,
	"Disease_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);CREATE INDEX "ix_Transmission_name" ON "Transmission" (name);
CREATE TABLE "ModelingConsideration" (
	name TEXT NOT NULL,
	description TEXT,
	"Disease_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);CREATE INDEX "ix_ModelingConsideration_name" ON "ModelingConsideration" (name);
CREATE TABLE "Dataset_conditions" (
	"Dataset_accession" TEXT,
	conditions TEXT,
	PRIMARY KEY ("Dataset_accession", conditions),
	FOREIGN KEY("Dataset_accession") REFERENCES "Dataset" (accession)
);CREATE INDEX "ix_Dataset_conditions_conditions" ON "Dataset_conditions" (conditions);CREATE INDEX "ix_Dataset_conditions_Dataset_accession" ON "Dataset_conditions" ("Dataset_accession");
CREATE TABLE "Subtype_geography" (
	"Subtype_name" TEXT,
	geography VARCHAR,
	PRIMARY KEY ("Subtype_name", geography),
	FOREIGN KEY("Subtype_name") REFERENCES "Subtype" (name)
);CREATE INDEX "ix_Subtype_geography_geography" ON "Subtype_geography" (geography);CREATE INDEX "ix_Subtype_geography_Subtype_name" ON "Subtype_geography" ("Subtype_name");
CREATE TABLE "Pathophysiology_examples" (
	"Pathophysiology_name" TEXT,
	examples TEXT,
	PRIMARY KEY ("Pathophysiology_name", examples),
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name)
);CREATE INDEX "ix_Pathophysiology_examples_Pathophysiology_name" ON "Pathophysiology_examples" ("Pathophysiology_name");CREATE INDEX "ix_Pathophysiology_examples_examples" ON "Pathophysiology_examples" (examples);
CREATE TABLE "Pathophysiology_synonyms" (
	"Pathophysiology_name" TEXT,
	synonyms TEXT,
	PRIMARY KEY ("Pathophysiology_name", synonyms),
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name)
);CREATE INDEX "ix_Pathophysiology_synonyms_Pathophysiology_name" ON "Pathophysiology_synonyms" ("Pathophysiology_name");CREATE INDEX "ix_Pathophysiology_synonyms_synonyms" ON "Pathophysiology_synonyms" (synonyms);
CREATE TABLE "Pathophysiology_consequences" (
	"Pathophysiology_name" TEXT,
	consequences TEXT,
	PRIMARY KEY ("Pathophysiology_name", consequences),
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name)
);CREATE INDEX "ix_Pathophysiology_consequences_Pathophysiology_name" ON "Pathophysiology_consequences" ("Pathophysiology_name");CREATE INDEX "ix_Pathophysiology_consequences_consequences" ON "Pathophysiology_consequences" (consequences);
CREATE TABLE "Pathophysiology_subtypes" (
	"Pathophysiology_name" TEXT,
	subtypes TEXT,
	PRIMARY KEY ("Pathophysiology_name", subtypes),
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name)
);CREATE INDEX "ix_Pathophysiology_subtypes_subtypes" ON "Pathophysiology_subtypes" (subtypes);CREATE INDEX "ix_Pathophysiology_subtypes_Pathophysiology_name" ON "Pathophysiology_subtypes" ("Pathophysiology_name");
CREATE TABLE "Pathophysiology_mechanisms" (
	"Pathophysiology_name" TEXT,
	mechanisms TEXT,
	PRIMARY KEY ("Pathophysiology_name", mechanisms),
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name)
);CREATE INDEX "ix_Pathophysiology_mechanisms_mechanisms" ON "Pathophysiology_mechanisms" (mechanisms);CREATE INDEX "ix_Pathophysiology_mechanisms_Pathophysiology_name" ON "Pathophysiology_mechanisms" ("Pathophysiology_name");
CREATE TABLE "Disease_parents" (
	"Disease_name" TEXT,
	parents TEXT,
	PRIMARY KEY ("Disease_name", parents),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);CREATE INDEX "ix_Disease_parents_parents" ON "Disease_parents" (parents);CREATE INDEX "ix_Disease_parents_Disease_name" ON "Disease_parents" ("Disease_name");
CREATE TABLE "Disease_categories" (
	"Disease_name" TEXT,
	categories TEXT,
	PRIMARY KEY ("Disease_name", categories),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);CREATE INDEX "ix_Disease_categories_Disease_name" ON "Disease_categories" ("Disease_name");CREATE INDEX "ix_Disease_categories_categories" ON "Disease_categories" (categories);
CREATE TABLE "Disease_synonyms" (
	"Disease_name" TEXT,
	synonyms TEXT,
	PRIMARY KEY ("Disease_name", synonyms),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);CREATE INDEX "ix_Disease_synonyms_Disease_name" ON "Disease_synonyms" ("Disease_name");CREATE INDEX "ix_Disease_synonyms_synonyms" ON "Disease_synonyms" (synonyms);
CREATE TABLE "Stage_examples" (
	"Stage_name" TEXT,
	examples TEXT,
	PRIMARY KEY ("Stage_name", examples),
	FOREIGN KEY("Stage_name") REFERENCES "Stage" (name)
);CREATE INDEX "ix_Stage_examples_examples" ON "Stage_examples" (examples);CREATE INDEX "ix_Stage_examples_Stage_name" ON "Stage_examples" ("Stage_name");
CREATE TABLE "AnimalModel_alleles" (
	"AnimalModel_id" INTEGER,
	alleles TEXT,
	PRIMARY KEY ("AnimalModel_id", alleles),
	FOREIGN KEY("AnimalModel_id") REFERENCES "AnimalModel" (id)
);CREATE INDEX "ix_AnimalModel_alleles_AnimalModel_id" ON "AnimalModel_alleles" ("AnimalModel_id");CREATE INDEX "ix_AnimalModel_alleles_alleles" ON "AnimalModel_alleles" (alleles);
CREATE TABLE "AnimalModel_associated_phenotypes" (
	"AnimalModel_id" INTEGER,
	associated_phenotypes TEXT,
	PRIMARY KEY ("AnimalModel_id", associated_phenotypes),
	FOREIGN KEY("AnimalModel_id") REFERENCES "AnimalModel" (id)
);CREATE INDEX "ix_AnimalModel_associated_phenotypes_AnimalModel_id" ON "AnimalModel_associated_phenotypes" ("AnimalModel_id");CREATE INDEX "ix_AnimalModel_associated_phenotypes_associated_phenotypes" ON "AnimalModel_associated_phenotypes" (associated_phenotypes);
CREATE TABLE "Finding" (
	id INTEGER NOT NULL,
	statement TEXT NOT NULL,
	supporting_text TEXT,
	"PublicationReference_reference" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("PublicationReference_reference") REFERENCES "PublicationReference" (reference)
);CREATE INDEX "ix_Finding_id" ON "Finding" (id);
CREATE TABLE "Phenotype" (
	category TEXT,
	name TEXT NOT NULL,
	description TEXT,
	diagnostic BOOLEAN,
	context TEXT,
	review_notes TEXT,
	severity TEXT,
	notes TEXT,
	subtype TEXT,
	"DifferentialDiagnosis_name" TEXT,
	"Disease_name" TEXT,
	phenotype_term_id INTEGER,
	frequency_id INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("DifferentialDiagnosis_name") REFERENCES "DifferentialDiagnosis" (name),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name),
	FOREIGN KEY(phenotype_term_id) REFERENCES "PhenotypeDescriptor" (id),
	FOREIGN KEY(frequency_id) REFERENCES "Any" (id)
);CREATE INDEX "ix_Phenotype_name" ON "Phenotype" (name);
CREATE TABLE "Biochemical" (
	name TEXT NOT NULL,
	presence TEXT,
	specificity TEXT,
	notes TEXT,
	context TEXT,
	subtype TEXT,
	"Disease_name" TEXT,
	biomarker_term_id INTEGER,
	frequency_id INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name),
	FOREIGN KEY(biomarker_term_id) REFERENCES "Descriptor" (id),
	FOREIGN KEY(frequency_id) REFERENCES "Any" (id)
);CREATE INDEX "ix_Biochemical_name" ON "Biochemical" (name);
CREATE TABLE "Environmental" (
	name TEXT NOT NULL,
	presence TEXT,
	notes TEXT,
	description TEXT,
	effect TEXT,
	review_notes TEXT,
	"Disease_name" TEXT,
	exposure_term_id INTEGER,
	environment_context_id INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name),
	FOREIGN KEY(exposure_term_id) REFERENCES "ExposureDescriptor" (id),
	FOREIGN KEY(environment_context_id) REFERENCES "EnvironmentDescriptor" (id)
);CREATE INDEX "ix_Environmental_name" ON "Environmental" (name);
CREATE TABLE "Treatment" (
	name TEXT NOT NULL,
	description TEXT,
	notes TEXT,
	context TEXT,
	review_notes TEXT,
	role TEXT,
	"Disease_name" TEXT,
	treatment_term_id INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name),
	FOREIGN KEY(treatment_term_id) REFERENCES "TreatmentDescriptor" (id)
);CREATE INDEX "ix_Treatment_name" ON "Treatment" (name);
CREATE TABLE "Diagnosis" (
	name TEXT NOT NULL,
	presence TEXT,
	notes TEXT,
	results TEXT,
	markers TEXT,
	description TEXT,
	"Disease_name" TEXT,
	diagnosis_term_id INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name),
	FOREIGN KEY(diagnosis_term_id) REFERENCES "TreatmentDescriptor" (id)
);CREATE INDEX "ix_Diagnosis_name" ON "Diagnosis" (name);
CREATE TABLE "Inheritance" (
	name TEXT NOT NULL,
	description TEXT,
	"Genetic_name" TEXT,
	"Disease_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("Genetic_name") REFERENCES "Genetic" (name),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name)
);CREATE INDEX "ix_Inheritance_name" ON "Inheritance" (name);
CREATE TABLE "Variant" (
	name TEXT NOT NULL,
	description TEXT,
	sequence_length INTEGER,
	clinical_significance VARCHAR(22),
	type TEXT,
	"Genetic_name" TEXT,
	"Disease_name" TEXT,
	gene_id INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("Genetic_name") REFERENCES "Genetic" (name),
	FOREIGN KEY("Disease_name") REFERENCES "Disease" (name),
	FOREIGN KEY(gene_id) REFERENCES "GeneDescriptor" (id)
);CREATE INDEX "ix_Variant_name" ON "Variant" (name);
CREATE TABLE "DifferentialDiagnosis_distinguishing_features" (
	"DifferentialDiagnosis_name" TEXT,
	distinguishing_features TEXT,
	PRIMARY KEY ("DifferentialDiagnosis_name", distinguishing_features),
	FOREIGN KEY("DifferentialDiagnosis_name") REFERENCES "DifferentialDiagnosis" (name)
);CREATE INDEX "ix_DifferentialDiagnosis_distinguishing_features_DifferentialDiagnosis_name" ON "DifferentialDiagnosis_distinguishing_features" ("DifferentialDiagnosis_name");CREATE INDEX "ix_DifferentialDiagnosis_distinguishing_features_distinguishing_features" ON "DifferentialDiagnosis_distinguishing_features" (distinguishing_features);
CREATE TABLE "EpidemiologyInfo_factors" (
	"EpidemiologyInfo_name" TEXT,
	factors TEXT,
	PRIMARY KEY ("EpidemiologyInfo_name", factors),
	FOREIGN KEY("EpidemiologyInfo_name") REFERENCES "EpidemiologyInfo" (name)
);CREATE INDEX "ix_EpidemiologyInfo_factors_EpidemiologyInfo_name" ON "EpidemiologyInfo_factors" ("EpidemiologyInfo_name");CREATE INDEX "ix_EpidemiologyInfo_factors_factors" ON "EpidemiologyInfo_factors" (factors);
CREATE TABLE "Genetic_examples" (
	"Genetic_name" TEXT,
	examples TEXT,
	PRIMARY KEY ("Genetic_name", examples),
	FOREIGN KEY("Genetic_name") REFERENCES "Genetic" (name)
);CREATE INDEX "ix_Genetic_examples_Genetic_name" ON "Genetic_examples" ("Genetic_name");CREATE INDEX "ix_Genetic_examples_examples" ON "Genetic_examples" (examples);
CREATE TABLE "CellTypeDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	modifier VARCHAR(12),
	laterality VARCHAR(9),
	"Pathophysiology_name" TEXT,
	"Biochemical_name" TEXT,
	term_id TEXT,
	located_in_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name),
	FOREIGN KEY("Biochemical_name") REFERENCES "Biochemical" (name),
	FOREIGN KEY(term_id) REFERENCES "Term" (id),
	FOREIGN KEY(located_in_id) REFERENCES "AnatomicalEntityDescriptor" (id)
);CREATE INDEX "ix_CellTypeDescriptor_id" ON "CellTypeDescriptor" (id);
CREATE TABLE "AssayDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	modifier VARCHAR(12),
	laterality VARCHAR(9),
	"Pathophysiology_name" TEXT,
	"Biochemical_name" TEXT,
	term_id TEXT,
	located_in_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name),
	FOREIGN KEY("Biochemical_name") REFERENCES "Biochemical" (name),
	FOREIGN KEY(term_id) REFERENCES "Term" (id),
	FOREIGN KEY(located_in_id) REFERENCES "AnatomicalEntityDescriptor" (id)
);CREATE INDEX "ix_AssayDescriptor_id" ON "AssayDescriptor" (id);
CREATE TABLE "CausalEdge" (
	id INTEGER NOT NULL,
	target TEXT NOT NULL,
	description TEXT,
	"Pathophysiology_name" TEXT,
	"Phenotype_name" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name),
	FOREIGN KEY("Phenotype_name") REFERENCES "Phenotype" (name)
);CREATE INDEX "ix_CausalEdge_id" ON "CausalEdge" (id);
CREATE TABLE "FunctionalEffect" (
	id INTEGER NOT NULL,
	function TEXT,
	description TEXT,
	type TEXT,
	"Variant_name" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Variant_name") REFERENCES "Variant" (name)
);CREATE INDEX "ix_FunctionalEffect_id" ON "FunctionalEffect" (id);
CREATE TABLE "Mechanism" (
	name TEXT NOT NULL,
	description TEXT,
	"Treatment_name" TEXT,
	PRIMARY KEY (name),
	FOREIGN KEY("Treatment_name") REFERENCES "Treatment" (name)
);CREATE INDEX "ix_Mechanism_name" ON "Mechanism" (name);
CREATE TABLE "Biochemical_synonyms" (
	"Biochemical_name" TEXT,
	synonyms TEXT,
	PRIMARY KEY ("Biochemical_name", synonyms),
	FOREIGN KEY("Biochemical_name") REFERENCES "Biochemical" (name)
);CREATE INDEX "ix_Biochemical_synonyms_synonyms" ON "Biochemical_synonyms" (synonyms);CREATE INDEX "ix_Biochemical_synonyms_Biochemical_name" ON "Biochemical_synonyms" ("Biochemical_name");
CREATE TABLE "Environmental_chemicals" (
	"Environmental_name" TEXT,
	chemicals TEXT,
	PRIMARY KEY ("Environmental_name", chemicals),
	FOREIGN KEY("Environmental_name") REFERENCES "Environmental" (name)
);CREATE INDEX "ix_Environmental_chemicals_Environmental_name" ON "Environmental_chemicals" ("Environmental_name");CREATE INDEX "ix_Environmental_chemicals_chemicals" ON "Environmental_chemicals" (chemicals);
CREATE TABLE "Environmental_synonyms" (
	"Environmental_name" TEXT,
	synonyms TEXT,
	PRIMARY KEY ("Environmental_name", synonyms),
	FOREIGN KEY("Environmental_name") REFERENCES "Environmental" (name)
);CREATE INDEX "ix_Environmental_synonyms_synonyms" ON "Environmental_synonyms" (synonyms);CREATE INDEX "ix_Environmental_synonyms_Environmental_name" ON "Environmental_synonyms" ("Environmental_name");
CREATE TABLE "Environmental_examples" (
	"Environmental_name" TEXT,
	examples TEXT,
	PRIMARY KEY ("Environmental_name", examples),
	FOREIGN KEY("Environmental_name") REFERENCES "Environmental" (name)
);CREATE INDEX "ix_Environmental_examples_examples" ON "Environmental_examples" (examples);CREATE INDEX "ix_Environmental_examples_Environmental_name" ON "Environmental_examples" ("Environmental_name");
CREATE TABLE "Treatment_target_phenotypes" (
	"Treatment_name" TEXT,
	target_phenotypes TEXT,
	PRIMARY KEY ("Treatment_name", target_phenotypes),
	FOREIGN KEY("Treatment_name") REFERENCES "Treatment" (name)
);CREATE INDEX "ix_Treatment_target_phenotypes_target_phenotypes" ON "Treatment_target_phenotypes" (target_phenotypes);CREATE INDEX "ix_Treatment_target_phenotypes_Treatment_name" ON "Treatment_target_phenotypes" ("Treatment_name");
CREATE TABLE "Treatment_examples" (
	"Treatment_name" TEXT,
	examples TEXT,
	PRIMARY KEY ("Treatment_name", examples),
	FOREIGN KEY("Treatment_name") REFERENCES "Treatment" (name)
);CREATE INDEX "ix_Treatment_examples_Treatment_name" ON "Treatment_examples" ("Treatment_name");CREATE INDEX "ix_Treatment_examples_examples" ON "Treatment_examples" (examples);
CREATE TABLE "Variant_synonyms" (
	"Variant_name" TEXT,
	synonyms TEXT,
	PRIMARY KEY ("Variant_name", synonyms),
	FOREIGN KEY("Variant_name") REFERENCES "Variant" (name)
);CREATE INDEX "ix_Variant_synonyms_Variant_name" ON "Variant_synonyms" ("Variant_name");CREATE INDEX "ix_Variant_synonyms_synonyms" ON "Variant_synonyms" (synonyms);
CREATE TABLE "Variant_identifiers" (
	"Variant_name" TEXT,
	identifiers TEXT,
	PRIMARY KEY ("Variant_name", identifiers),
	FOREIGN KEY("Variant_name") REFERENCES "Variant" (name)
);CREATE INDEX "ix_Variant_identifiers_Variant_name" ON "Variant_identifiers" ("Variant_name");CREATE INDEX "ix_Variant_identifiers_identifiers" ON "Variant_identifiers" (identifiers);
CREATE TABLE "SampleTypeDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	modifier VARCHAR(12),
	laterality VARCHAR(9),
	"Dataset_accession" TEXT,
	tissue_term_id INTEGER,
	cell_type_term_id INTEGER,
	term_id TEXT,
	located_in_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Dataset_accession") REFERENCES "Dataset" (accession),
	FOREIGN KEY(tissue_term_id) REFERENCES "AnatomicalEntityDescriptor" (id),
	FOREIGN KEY(cell_type_term_id) REFERENCES "CellTypeDescriptor" (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id),
	FOREIGN KEY(located_in_id) REFERENCES "AnatomicalEntityDescriptor" (id)
);CREATE INDEX "ix_SampleTypeDescriptor_id" ON "SampleTypeDescriptor" (id);
CREATE TABLE "EvidenceItem" (
	id INTEGER NOT NULL,
	reference TEXT,
	supports VARCHAR(15),
	snippet TEXT,
	explanation TEXT,
	"Dataset_accession" TEXT,
	"ComputationalModel_name" TEXT,
	"DifferentialDiagnosis_name" TEXT,
	"Subtype_name" TEXT,
	"CausalEdge_id" INTEGER,
	"Prevalence_id" INTEGER,
	"ProgressionInfo_id" INTEGER,
	"EpidemiologyInfo_name" TEXT,
	"Pathophysiology_name" TEXT,
	"Phenotype_name" TEXT,
	"Biochemical_name" TEXT,
	"Genetic_name" TEXT,
	"Environmental_name" TEXT,
	"Stage_name" TEXT,
	"AnimalModel_id" INTEGER,
	"Treatment_name" TEXT,
	"InfectiousAgent_name" TEXT,
	"Transmission_name" TEXT,
	"Diagnosis_name" TEXT,
	"Inheritance_name" TEXT,
	"Variant_name" TEXT,
	"ModelingConsideration_name" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Dataset_accession") REFERENCES "Dataset" (accession),
	FOREIGN KEY("ComputationalModel_name") REFERENCES "ComputationalModel" (name),
	FOREIGN KEY("DifferentialDiagnosis_name") REFERENCES "DifferentialDiagnosis" (name),
	FOREIGN KEY("Subtype_name") REFERENCES "Subtype" (name),
	FOREIGN KEY("CausalEdge_id") REFERENCES "CausalEdge" (id),
	FOREIGN KEY("Prevalence_id") REFERENCES "Prevalence" (id),
	FOREIGN KEY("ProgressionInfo_id") REFERENCES "ProgressionInfo" (id),
	FOREIGN KEY("EpidemiologyInfo_name") REFERENCES "EpidemiologyInfo" (name),
	FOREIGN KEY("Pathophysiology_name") REFERENCES "Pathophysiology" (name),
	FOREIGN KEY("Phenotype_name") REFERENCES "Phenotype" (name),
	FOREIGN KEY("Biochemical_name") REFERENCES "Biochemical" (name),
	FOREIGN KEY("Genetic_name") REFERENCES "Genetic" (name),
	FOREIGN KEY("Environmental_name") REFERENCES "Environmental" (name),
	FOREIGN KEY("Stage_name") REFERENCES "Stage" (name),
	FOREIGN KEY("AnimalModel_id") REFERENCES "AnimalModel" (id),
	FOREIGN KEY("Treatment_name") REFERENCES "Treatment" (name),
	FOREIGN KEY("InfectiousAgent_name") REFERENCES "InfectiousAgent" (name),
	FOREIGN KEY("Transmission_name") REFERENCES "Transmission" (name),
	FOREIGN KEY("Diagnosis_name") REFERENCES "Diagnosis" (name),
	FOREIGN KEY("Inheritance_name") REFERENCES "Inheritance" (name),
	FOREIGN KEY("Variant_name") REFERENCES "Variant" (name),
	FOREIGN KEY("ModelingConsideration_name") REFERENCES "ModelingConsideration" (name)
);CREATE INDEX "ix_EvidenceItem_id" ON "EvidenceItem" (id);
CREATE TABLE "Qualifier" (
	id INTEGER NOT NULL,
	"Descriptor_id" INTEGER,
	"CellTypeDescriptor_id" INTEGER,
	"BiologicalProcessDescriptor_id" INTEGER,
	"AnatomicalEntityDescriptor_id" INTEGER,
	"ChemicalEntityDescriptor_id" INTEGER,
	"GeneDescriptor_id" INTEGER,
	"CellularComponentDescriptor_id" INTEGER,
	"AssayDescriptor_id" INTEGER,
	"TriggerDescriptor_id" INTEGER,
	"DiseaseDescriptor_id" INTEGER,
	"PhenotypeDescriptor_id" INTEGER,
	"TreatmentDescriptor_id" INTEGER,
	"ExposureDescriptor_id" INTEGER,
	"EnvironmentDescriptor_id" INTEGER,
	"OrganismDescriptor_id" INTEGER,
	"SampleTypeDescriptor_id" INTEGER,
	predicate_id INTEGER,
	value_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Descriptor_id") REFERENCES "Descriptor" (id),
	FOREIGN KEY("CellTypeDescriptor_id") REFERENCES "CellTypeDescriptor" (id),
	FOREIGN KEY("BiologicalProcessDescriptor_id") REFERENCES "BiologicalProcessDescriptor" (id),
	FOREIGN KEY("AnatomicalEntityDescriptor_id") REFERENCES "AnatomicalEntityDescriptor" (id),
	FOREIGN KEY("ChemicalEntityDescriptor_id") REFERENCES "ChemicalEntityDescriptor" (id),
	FOREIGN KEY("GeneDescriptor_id") REFERENCES "GeneDescriptor" (id),
	FOREIGN KEY("CellularComponentDescriptor_id") REFERENCES "CellularComponentDescriptor" (id),
	FOREIGN KEY("AssayDescriptor_id") REFERENCES "AssayDescriptor" (id),
	FOREIGN KEY("TriggerDescriptor_id") REFERENCES "TriggerDescriptor" (id),
	FOREIGN KEY("DiseaseDescriptor_id") REFERENCES "DiseaseDescriptor" (id),
	FOREIGN KEY("PhenotypeDescriptor_id") REFERENCES "PhenotypeDescriptor" (id),
	FOREIGN KEY("TreatmentDescriptor_id") REFERENCES "TreatmentDescriptor" (id),
	FOREIGN KEY("ExposureDescriptor_id") REFERENCES "ExposureDescriptor" (id),
	FOREIGN KEY("EnvironmentDescriptor_id") REFERENCES "EnvironmentDescriptor" (id),
	FOREIGN KEY("OrganismDescriptor_id") REFERENCES "OrganismDescriptor" (id),
	FOREIGN KEY("SampleTypeDescriptor_id") REFERENCES "SampleTypeDescriptor" (id),
	FOREIGN KEY(predicate_id) REFERENCES "Descriptor" (id),
	FOREIGN KEY(value_id) REFERENCES "Descriptor" (id)
);CREATE INDEX "ix_Qualifier_id" ON "Qualifier" (id);
