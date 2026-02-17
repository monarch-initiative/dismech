
# dismech


**metamodel version:** 1.7.0

**version:** None


Disease Pathophysiology Knowledge Base Schema


### Classes

 * [AnimalModel](AnimalModel.md)
 * [Any](Any.md)
 * [Assay](Assay.md)
 * [Biochemical](Biochemical.md)
 * [CausalEdge](CausalEdge.md) - A reference to a downstream effect or consequence in a causal relationship
 * [ComputationalModel](ComputationalModel.md) - A computational or in-silico model relevant to understanding disease mechanisms
 * [CurationEvent](CurationEvent.md) - A single curation event in the audit trail
 * [Dataset](Dataset.md) - A reference to a publicly available omics or phenotype dataset
 * [Descriptor](Descriptor.md) - Base class for structured descriptors that allow a preferred term, optional description, optional ontology term binding, and post-composition via modifier, located_in, and laterality slots.
     * [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) - A descriptor for anatomical locations, bindable to UBERON
     * [AssayDescriptor](AssayDescriptor.md) - A descriptor for assays, bindable to OBI
     * [BiologicalProcessDescriptor](BiologicalProcessDescriptor.md) - A descriptor for biological processes, bindable to Gene Ontology (GO)
     * [CellTypeDescriptor](CellTypeDescriptor.md) - A descriptor for cell types, bindable to Cell Ontology (CL)
     * [CellularComponentDescriptor](CellularComponentDescriptor.md) - A descriptor for cellular components, bindable to GO cellular component
     * [ChemicalEntityDescriptor](ChemicalEntityDescriptor.md) - A descriptor for chemical entities, bindable to CHEBI
     * [DiseaseDescriptor](DiseaseDescriptor.md) - A descriptor for the focal disease, bindable to MONDO
     * [EnvironmentDescriptor](EnvironmentDescriptor.md) - A descriptor for environmental contexts/settings, bindable to ENVO
     * [ExposureDescriptor](ExposureDescriptor.md) - A descriptor for exposure events, bindable to ECTO or XCO
     * [GeneDescriptor](GeneDescriptor.md) - A descriptor for genes, bindable to HGNC or other gene databases
     * [OrganismDescriptor](OrganismDescriptor.md) - A descriptor for organisms, bindable to NCBITaxon
     * [PhenotypeDescriptor](PhenotypeDescriptor.md) - A descriptor for phenotypes, bindable to Human Phenotype Ontology (HP)
     * [SampleTypeDescriptor](SampleTypeDescriptor.md) - A descriptor for biological sample types (tissue and/or cell type)
     * [TreatmentDescriptor](TreatmentDescriptor.md) - A descriptor for treatments/medical actions, bindable to Medical Action Ontology (MAXO)
     * [TriggerDescriptor](TriggerDescriptor.md) - A descriptor for triggers/causes
 * [Diagnosis](Diagnosis.md)
 * [DifferentialDiagnosis](DifferentialDiagnosis.md) - A disease or condition that presents similarly to the focal disease and must be differentiated
 * [Disease](Disease.md)
 * [DiseaseCollection](DiseaseCollection.md)
 * [Environmental](Environmental.md) - An environmental factor, exposure, or context relevant to disease
 * [EpidemiologyInfo](EpidemiologyInfo.md)
 * [EvidenceItem](EvidenceItem.md)
 * [Finding](Finding.md) - A key finding or claim extracted from a publication
 * [FunctionalEffect](FunctionalEffect.md)
 * [Genetic](Genetic.md)
 * [InfectiousAgent](InfectiousAgent.md)
 * [Inheritance](Inheritance.md)
 * [Mechanism](Mechanism.md)
 * [ModelingConsideration](ModelingConsideration.md)
 * [Pathophysiology](Pathophysiology.md)
 * [Phenotype](Phenotype.md)
 * [Prevalence](Prevalence.md)
 * [ProgressionInfo](ProgressionInfo.md)
 * [PublicationReference](PublicationReference.md) - A reference to a publication with associated findings
 * [Qualifier](Qualifier.md) - A predicate-value pair for formal post-composition. Allows OWL-like expressivity with controlled predicates and values, both as full Descriptors.
 * [Stage](Stage.md)
 * [Subtype](Subtype.md)
 * [Term](Term.md) - A structured reference to an ontology term
 * [Transmission](Transmission.md)
 * [Treatment](Treatment.md)
 * [Variant](Variant.md)

### Mixins


### Slots

 * [accession](accession.md) - Dataset accession identifier as a CURIE (e.g., geo:GSE67472)
 * [age_range](age_range.md)
 * [alleles](alleles.md)
 * [animal_models](animal_models.md)
 * [assays](assays.md)
 * [associated_phenotypes](associated_phenotypes.md)
 * [association](association.md)
 * [background](background.md)
 * [base_model](base_model.md) - Parent/base model this is derived from (e.g., Recon3D, Harvey 1.0)
 * [biochemical](biochemical.md)
 * [biological_processes](biological_processes.md)
 * [biomarker_term](biomarker_term.md) - Ontology term for a biomarker (from NCIT, CHEBI, or LOINC)
 * [categories](categories.md)
 * [category](category.md)
 * [cell_type_term](cell_type_term.md) - CL term for the cell type
 * [cell_types](cell_types.md)
 * [cellular_components](cellular_components.md)
 * [chemical_entities](chemical_entities.md)
 * [chemicals](chemicals.md)
 * [clinical_significance](clinical_significance.md)
 * [computational_models](computational_models.md) - Computational models (metabolic, mechanistic, ML, digital twins) for this disease
 * [conditions](conditions.md) - Experimental conditions or disease states represented
 * [consequence](consequence.md)
 * [consequences](consequences.md)
 * [context](context.md)
 * [curation_action](curation_action.md) - Type of curation action performed
 * [curation_description](curation_description.md) - Human-readable description of changes made
 * [curation_history](curation_history.md) - Audit trail of AI-assisted curation events
 * [curation_model](curation_model.md) - Model identifier used for curation (e.g., claude-opus-4-5-20251101)
 * [curation_timestamp](curation_timestamp.md) - ISO 8601 timestamp of the curation event
     * [CurationEvent➞curation_timestamp](CurationEvent_curation_timestamp.md)
 * [data_type](data_type.md) - The type of omics or other data in the dataset
 * [datasets](datasets.md) - Publicly available datasets relevant to disease research
 * [description](description.md)
     * [Dataset➞description](Dataset_description.md) - A description of the dataset. This may typically be redundant with the `title` slot, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the title slot.
     * [Descriptor➞description](Descriptor_description.md) - A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.
     * [DifferentialDiagnosis➞description](DifferentialDiagnosis_description.md) - Clinical or mechanistic overlaps, shared presentations, and diagnostic considerations with the focal disease
 * [diagnosis](diagnosis.md)
 * [diagnosis_term](diagnosis_term.md) - The MAXO term for this diagnostic procedure
 * [diagnostic](diagnostic.md)
 * [differential_diagnoses](differential_diagnoses.md) - Differential diagnoses - similar diseases that must be ruled out
 * [disease_term](disease_term.md) - The MONDO disease term for this disease
 * [diseases](diseases.md)
 * [distinguishing_features](distinguishing_features.md) - Key clinical, laboratory, imaging, or epidemiological features that help differentiate a related condition from the focal disease
     * [DifferentialDiagnosis➞distinguishing_features](DifferentialDiagnosis_distinguishing_features.md) - Key clinical, laboratory, imaging, or epidemiological features that help differentiate this condition from the focal disease
 * [downstream](downstream.md)
 * [duration](duration.md)
 * [duration_days](duration_days.md)
 * [effect](effect.md)
 * [environment_context](environment_context.md) - The ENVO term for the environmental context/setting
 * [environmental](environmental.md)
 * [epidemiology](epidemiology.md)
 * [evidence](evidence.md)
 * [examples](examples.md)
 * [explanation](explanation.md)
 * [exposure_term](exposure_term.md) - The ECTO/XCO term for this exposure event
 * [exposures](exposures.md) - Environmental exposures studied in the dataset
 * [factors](factors.md)
 * [features](features.md)
 * [findings](findings.md) - Key findings or claims extracted from this reference
 * [frequency](frequency.md)
 * [function](function.md)
 * [functional_effects](functional_effects.md)
 * [gene](gene.md)
 * [genes](genes.md)
 * [genetic](genetic.md)
 * [genotype](genotype.md)
 * [geography](geography.md)
 * [has_subtypes](has_subtypes.md)
 * [id](id.md) - Ontology term identifier (CURIE)
 * [identifiers](identifiers.md)
 * [incubation_days](incubation_days.md)
 * [incubation_years](incubation_years.md)
 * [infectious_agent](infectious_agent.md)
 * [inheritance](inheritance.md)
 * [label](label.md) - Human-readable label for the ontology term
 * [laterality](laterality.md) - Laterality qualifier (left, right, or bilateral)
 * [located_in](located_in.md) - Anatomical location where this entity/process occurs or procedure is performed
 * [locations](locations.md)
 * [markers](markers.md)
 * [maximum_value](maximum_value.md)
 * [mean_range](mean_range.md)
 * [mechanism](mechanism.md)
 * [mechanisms](mechanisms.md)
 * [minimum_value](minimum_value.md)
 * [model_format](model_format.md) - File format (e.g., SBML, MATLAB, JSON, ONNX)
 * [model_id](model_id.md) - Identifier within the repository (e.g., Recon3D, BIOMD0000000123)
 * [model_software](model_software.md) - Software/toolbox for running the model (e.g., COBRApy, COBRA Toolbox)
 * [model_type](model_type.md) - Type of computational model
 * [modeling_considerations](modeling_considerations.md)
 * [modifier](modifier.md) - Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)
 * [name](name.md)
 * [notes](notes.md)
     * [DifferentialDiagnosis➞notes](DifferentialDiagnosis_notes.md) - Additional clinical notes or management considerations
 * [organism](organism.md) - The organism from which samples were derived
 * [parents](parents.md)
 * [pathophysiology](pathophysiology.md)
 * [pathways](pathways.md)
 * [percentage](percentage.md)
 * [perturbations](perturbations.md) - Gene knockouts, reaction deletions, or parameter changes modeling the disease
 * [phase](phase.md)
 * [phenotype_term](phenotype_term.md) - The HP term for this phenotype
 * [phenotypes](phenotypes.md)
 * [platform](platform.md) - Sequencing or array platform used
 * [population](population.md)
 * [predicate](predicate.md) - The relationship/predicate in a qualifier (e.g., RO:0002233 'has input')
 * [preferred_term](preferred_term.md) - The preferred human-readable term for this descriptor
 * [presence](presence.md)
 * [prevalence](prevalence.md)
 * [progression](progression.md)
 * [publication](publication.md) - Associated publication (PMID)
 * [qualifiers](qualifiers.md) - List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.
 * [reference](reference.md) - The authoritative reference (publication) for this evidence item
     * [PublicationReference➞reference](PublicationReference_reference.md)
 * [references](references.md) - Top-level list of references with their key findings for this disease
 * [repository_url](repository_url.md) - URL to model repository (GitHub, BiGG, VMH, BioModels)
 * [results](results.md)
 * [review_notes](review_notes.md)
 * [role](role.md)
 * [sample_count](sample_count.md) - Total number of samples in the dataset
 * [sample_types](sample_types.md) - Types of biological samples in the dataset
 * [sequelae](sequelae.md)
 * [sequence_length](sequence_length.md)
 * [severity](severity.md)
 * [snippet](snippet.md) - An exact excerpt/quote from the referenced publication that supports or refutes the claim
 * [species](species.md)
 * [specificity](specificity.md)
 * [stages](stages.md)
 * [statement](statement.md) - A key finding or claim from the publication
 * [substages](substages.md)
 * [subtype](subtype.md)
 * [subtype_term](subtype_term.md) - The MONDO term for a disease subtype
 * [subtypes](subtypes.md)
 * [supporting_text](supporting_text.md) - Exact excerpt/quote from the publication supporting the statement
 * [supports](supports.md)
 * [synonyms](synonyms.md)
 * [target](target.md) - The name of the target element in a causal relationship
 * [target_phenotypes](target_phenotypes.md) - Names of phenotypes that this treatment addresses or targets
 * [term](term.md) - Optional structured ontology term reference
     * [AnatomicalEntityDescriptor➞term](AnatomicalEntityDescriptor_term.md) - Optional UBERON anatomical entity term reference
     * [AssayDescriptor➞term](AssayDescriptor_term.md) - Optional OBI assay term reference
     * [BiologicalProcessDescriptor➞term](BiologicalProcessDescriptor_term.md) - Optional GO biological process term reference
     * [CellTypeDescriptor➞term](CellTypeDescriptor_term.md) - Optional Cell Ontology term reference
     * [CellularComponentDescriptor➞term](CellularComponentDescriptor_term.md) - Optional GO cellular component term reference
     * [ChemicalEntityDescriptor➞term](ChemicalEntityDescriptor_term.md) - Optional CHEBI chemical entity term reference
     * [DiseaseDescriptor➞term](DiseaseDescriptor_term.md) - Optional MONDO disease term reference
     * [EnvironmentDescriptor➞term](EnvironmentDescriptor_term.md) - Optional ENVO environment term reference
     * [ExposureDescriptor➞term](ExposureDescriptor_term.md) - Optional ECTO/XCO exposure term reference
     * [GeneDescriptor➞term](GeneDescriptor_term.md) - Optional gene database term reference (e.g., HGNC)
     * [OrganismDescriptor➞term](OrganismDescriptor_term.md) - NCBITaxon term reference
     * [PhenotypeDescriptor➞term](PhenotypeDescriptor_term.md) - Optional HP phenotype term reference
     * [TreatmentDescriptor➞term](TreatmentDescriptor_term.md) - Optional MAXO treatment term reference
     * [TriggerDescriptor➞term](TriggerDescriptor_term.md) - Optional ontology term reference
 * [tissue_term](tissue_term.md) - UBERON term for the tissue
 * [title](title.md) - Title of the publication
 * [transmission](transmission.md)
 * [treatment_term](treatment_term.md) - The MAXO term for this treatment/medical action
 * [treatments](treatments.md)
 * [triggers](triggers.md)
 * [type](type.md)
 * [unit](unit.md)
 * [value](value.md) - The value/filler in a qualifier
 * [variants](variants.md)

### Enums

 * [AnatomicalEntityTerm](AnatomicalEntityTerm.md) - A term representing an anatomical entity
 * [AssayTerm](AssayTerm.md) - A term representing an assay
 * [BiologicalProcessTerm](BiologicalProcessTerm.md) - A term representing a biological process or pathway
 * [CellTypeTerm](CellTypeTerm.md) - A cell type
 * [CellularComponentTerm](CellularComponentTerm.md) - A term representing a cellular component
 * [ChemicalEntityTerm](ChemicalEntityTerm.md) - A term representing a chemical entity
 * [ClinicalSignificanceEnum](ClinicalSignificanceEnum.md) - The clinical significance of a variant for a condition (ACMG guidelines)
 * [ComputationalModelTypeEnum](ComputationalModelTypeEnum.md) - Type of computational or in-silico model
 * [CurationActionEnum](CurationActionEnum.md) - Simple action types for curation audit trail
 * [DatasetTypeEnum](DatasetTypeEnum.md) - Type of dataset or data resource
 * [DiseaseTerm](DiseaseTerm.md) - A disease or medical condition
 * [EnvironmentTerm](EnvironmentTerm.md) - A term representing an environmental context, material, or feature (from ENVO)
 * [EvidenceItemSupportEnum](EvidenceItemSupportEnum.md) - The level of support for an evidence item
 * [ExposureTerm](ExposureTerm.md) - A term representing an exposure event (from ECTO or XCO)
 * [FrequencyEnum](FrequencyEnum.md) - The frequency of an event or phenomenon
 * [GeneTerm](GeneTerm.md) - A gene
 * [GeographyTerm](GeographyTerm.md) - A place or location
 * [LateralityEnum](LateralityEnum.md) - Laterality qualifier for anatomical structures or procedures
 * [ModifierEnum](ModifierEnum.md) - Qualifiers for direction, intensity, or pathological state of a descriptor
 * [OrganismTerm](OrganismTerm.md) - A term representing an organism from NCBITaxon
 * [PhaseTerm](PhaseTerm.md) - A phase or stage
 * [PhenotypeTerm](PhenotypeTerm.md) - A term representing a phenotype or disease manifestation
 * [TreatmentActionTerm](TreatmentActionTerm.md) - A term representing a medical action or treatment (from MAXO)
 * [TriggerTerm](TriggerTerm.md) - A trigger

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [FrequencyQuantity](types/FrequencyQuantity.md)  ([String](types/String.md))
 * [PMID](types/PMID.md)  ([String](types/String.md))
 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
