---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-11-22T14:56:27.589936'
end_time: '2026-11-22T15:01:05.049783'
duration_seconds: 277.46
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Neurodevelopmental Disorder With Or Without Seizures And Gait Abnormalities
  mondo_id: MONDO:0060641
  category: Mendelian
  causal_genes: GRIA4
  omim_id: OMIM:617864
  synonyms: not recorded
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 19
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 3
  validator_version: 0.8.0
term_validation:
  total_terms: 85
  verified: 78
  not_found: 0
  obsolete: 1
  unverifiable: 6
  confabulation_rate: 0.0
  labels_checked: 68
  labels_matching: 15
  labels_mismatched: 39
  mislabelled_terms:
  - term_id: HP:0001263
    reported_labels:
    - Global developmental delay
    - Neonatal/infancy
    ontology_label: Global developmental delay
  - term_id: HP:0010863
    reported_labels:
    - Profound intellectual disability
    ontology_label: Receptive language delay
  - term_id: HP:0002067
    reported_labels:
    - Spasticity
    ontology_label: Bradykinesia
  - term_id: HP:0002312
    reported_labels:
    - Spastic gait
    ontology_label: Clumsiness
  - term_id: HP:0001371
    reported_labels:
    - Hypertonia
    ontology_label: Flexion contracture
  - term_id: HP:0001319
    reported_labels:
    - Contractures
    - Childhood
    ontology_label: Neonatal hypotonia
  - term_id: HP:0004885
    reported_labels:
    - Impaired gait
    ontology_label: Episodic respiratory distress
  - term_id: HP:0002353
    reported_labels:
    - Abnormal EEG
    - Childhood
    ontology_label: EEG abnormality
  - term_id: HP:0000484
    reported_labels:
    - Retinal hypoplasia
    ontology_label: Hyperopic astigmatism
  - term_id: HP:0000556
    reported_labels:
    - Chorioretinal hyperpigmentation
    ontology_label: Retinal dystrophy
  - term_id: HP:0004322
    reported_labels:
    - Macrotia
    - Short stature
    - Congenital
    ontology_label: Short stature
  - term_id: HP:0001337
    reported_labels:
    - Choreiform movements
    ontology_label: Tremor
  - term_id: HP:0000734
    reported_labels:
    - Stereotypy
    ontology_label: Disinhibition
  - term_id: HP:0002028
    reported_labels:
    - Feeding difficulties
    - Neonatal/infancy
    ontology_label: Chronic diarrhea
  - term_id: HP:0001251
    reported_labels:
    - Irritability
    ontology_label: Ataxia
  - term_id: HP:0001285
    reported_labels:
    - Hyperreflexia
    ontology_label: Spastic tetraparesis
  - term_id: HP:0002376
    reported_labels:
    - Exaggerated startle response
    ontology_label: Developmental regression
  - term_id: GO:0098984
    reported_labels:
    - neuron projection
    ontology_label: neuron to neuron synapse
  - term_id: GO:0005891
    reported_labels:
    - "AMPA\u2011type glutamate receptor complex"
    - 'Cellular components: AMPA receptor complex'
    ontology_label: voltage-gated calcium channel complex
  - term_id: GO:0007612
    reported_labels:
    - memory
    ontology_label: learning
  - term_id: GO:0098962
    reported_labels:
    - neuronal action potential
    ontology_label: obsolete regulation of postsynaptic neurotransmitter receptor
      activity
  - term_id: GO:0022038
    reported_labels:
    - neurogenesis
    ontology_label: corpus callosum development
  - term_id: CL:0002604
    reported_labels:
    - 'Cell types: cortical pyramidal neuron'
    ontology_label: hippocampal astrocyte
  - term_id: UBERON:0000955
    reported_labels:
    - eye
    ontology_label: brain
  - term_id: UBERON:0001811
    reported_labels:
    - visual cortex
    ontology_label: conjunctiva
  - term_id: UBERON:0002338
    reported_labels:
    - corpus callosum
    ontology_label: lamina propria of bronchus
  - term_id: UBERON:0001465
    reported_labels:
    - muscle organ
    ontology_label: knee
  - term_id: UBERON:0001450
    reported_labels:
    - joint
    ontology_label: calcaneus
  - term_id: UBERON:0001623
    reported_labels:
    - extraocular skeletal muscle
    ontology_label: dorsal nasal artery
  - term_id: UBERON:0002084
    reported_labels:
    - heart
    ontology_label: heart left ventricle
  - term_id: UBERON:0002090
    reported_labels:
    - tricuspid valve
    ontology_label: postcranial axial skeleton
  - term_id: UBERON:0002099
    reported_labels:
    - foramen ovale
    ontology_label: cardiac septum
  - term_id: UBERON:0001041
    reported_labels:
    - pharynx
    ontology_label: foregut
  - term_id: UBERON:0000945
    reported_labels:
    - esophagus
    ontology_label: stomach
  - term_id: UBERON:0001045
    reported_labels:
    - stomach
    ontology_label: midgut
  - term_id: NCIT:C772
    reported_labels:
    - Anticonvulsant agent
    ontology_label: Probenecid
  - term_id: NCIT:C2315
    reported_labels:
    - Muscle relaxant
    ontology_label: Hormone
  - term_id: NCIT:C15624
    reported_labels:
    - Supportive care
    ontology_label: 9-cis-Retinoic Acid/Interferon Alfa
  - term_id: NCIT:C15336
    reported_labels:
    - Physical therapy
    ontology_label: Testing
  labels_variant: 14
  obsolete_terms:
  - term_id: GO:0098962
    ontology_label: obsolete regulation of postsynaptic neurotransmitter receptor
      activity
  unresolvable_prefixes:
  - OMIM
  - Taxon
  service_unreachable: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With Or Without Seizures And Gait Abnormalities
- **MONDO ID:** MONDO:0060641 (if available)
- **Causal gene(s):** GRIA4
- **OMIM:** OMIM:617864
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Or Without Seizures And Gait Abnormalities** covering all of the
disease characteristics listed below. This report will be used to populate a disease knowledge
base entry. Be thorough and cite primary literature (PMID preferred) for all claims.

For each section, **suggested databases/resources** are listed. These are the first places
you should search for information on each topic.

---

### 1. Disease Information
> **Search first:** OMIM, Orphanet, ICD-10/ICD-11, MeSH, PubMed

- What is the disease? Provide a concise overview.
- What are the key identifiers? (OMIM, Orphanet, ICD-10/ICD-11, MeSH, Mondo)
- What are the common synonyms and alternative names?
- Is the information derived from individual patients (e.g., EHR) or aggregated disease-level resources?

### 2. Etiology

- **Disease Causal Factors**: What are the primary causes? (genetic, environmental, infectious, mechanistic)
- **Risk Factors**:
  > **Search first:** PubMed, Cochrane Library, UpToDate, clinical guidelines, ClinVar, ClinGen, GWAS Catalog, PheGenI, CTD, CDC, WHO, epidemiological databases
  - Genetic risk factors (causal variants, susceptibility loci, modifier genes)
  - Environmental risk factors (toxins, lifestyle, occupational exposures, age, sex, family history)
- **Protective Factors**:
  > **Search first:** PubMed, Cochrane Library, clinical trial databases, GWAS Catalog, gnomAD, WHO, CDC, nutrition databases
  - Genetic protective factors (protective variants, modifier alleles)
  - Environmental protective factors (diet, lifestyle, exposures that reduce risk)
- **Gene-Environment Interactions**: How do genetic and environmental factors interact to influence disease?
  > **Search first:** CTD, PubMed, PheGenI, GxE databases

### 3. Phenotypes
> **Search first:** HPO (Human Phenotype Ontology), OMIM, Orphanet, PubMed, clinicaltrials.gov, MedDRA, SNOMED CT, DECIPHER, LOINC

For each phenotype, provide:
- **Phenotype type**: symptoms, clinical signs, physical manifestations, behavioral changes, or laboratory abnormalities
  > For symptoms/signs: HPO, OMIM, Orphanet, PubMed
  > For behavioral changes: HPO, DSM, RDoC (Research Domain Criteria), PubMed
  > For laboratory abnormalities: LOINC, SNOMED CT, LabTests Online, PubMed
- **Phenotype characteristics**:
  > **Search first:** OMIM, Orphanet, HPO, PubMed
  - Age of symptom onset (neonatal, childhood, adult-onset, late-onset)
  - Symptom severity (mild, moderate, severe, variable)
  - Symptom progression (stable, progressive, episodic, fluctuating)
  - Frequency among affected individuals (percentage or qualitative)
- **Quality of life impact**: Effects on daily functioning and well-being (per-phenotype when possible)
  > **Search first:** EQ-5D database, SF-36, WHO QOL databases, PubMed
- Suggest HPO (Human Phenotype Ontology) terms for each phenotype

### 4. Genetic/Molecular Information

- **Causal Genes**: Gene mutations or chromosomal abnormalities responsible for disease (gene symbols, OMIM IDs)
  > **Search first:** OMIM, ClinVar, HGMD, Ensembl, NCBI Gene
- **Pathogenic Variants**:
  - Affected genes (gene symbols, HGNC IDs)
    > **Search first:** OMIM, NCBI Gene, Ensembl, HGNC, UniProt, GeneCards
  - Variant classification (pathogenic, likely pathogenic, VUS per ACMG/AMP guidelines)
    > **Search first:** ClinVar, ClinGen, ACMG/AMP guidelines, VarSome
  - Variant type/class (missense, frameshift, nonsense, splice-site, structural)
  - Allele frequency in population databases
    > **Search first:** gnomAD, 1000 Genomes, ExAC, TOPMed, dbSNP
  - Somatic vs germline origin
    > **Search first:** COSMIC (somatic), ClinVar, ICGC, TCGA
  - Functional consequences (loss of function, gain of function, dominant negative)
- **Modifier Genes**: Genes that modify disease severity or expression
- **Epigenetic Information**: DNA methylation, histone modifications, chromatin changes affecting disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Chromosomal Abnormalities**: Large-scale genetic changes (aneuploidy, translocations, inversions)
  > **Search first:** DECIPHER, ClinVar, ECARUCA, UCSC Genome Browser

### 5. Environmental Information

- **Environmental Factors**: Non-genetic contributing factors (toxins, radiation, pollution, occupational exposure)
  > **Search first:** CTD (Comparative Toxicogenomics Database), TOXNET, PubMed, EPA databases
- **Lifestyle Factors**: Behavioral factors (smoking, diet, exercise, alcohol consumption)
  > **Search first:** CDC databases, WHO, PubMed, NHANES
- **Infectious Agents**: If applicable, pathogens causing or triggering disease (bacteria, viruses, fungi, parasites)
  > **Search first:** NCBI Taxonomy, ViPR, BV-BRC, MicrobeDB, GIDEON

### 6. Mechanism / Pathophysiology

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

- **Molecular Pathways**: Specific signaling cascades or biochemical pathways involved (Wnt, MAPK, mTOR, PI3K-AKT, etc.)
  > **Search first:** KEGG, Reactome, WikiPathways, PathBank, BioCyc
- **Cellular Processes**: Cell-level mechanisms (apoptosis, autophagy, cell cycle dysregulation, inflammation, etc.)
  > **Search first:** Gene Ontology (GO), Reactome, KEGG, PubMed
- **Protein Dysfunction**: How protein structure or function is altered (misfolding, aggregation, loss of function, gain of function)
  > **Search first:** UniProt, PDB (Protein Data Bank), InterPro, Pfam, AlphaFold
- **Metabolic Changes**: Alterations in metabolic processes (energy metabolism, lipid metabolism, amino acid metabolism)
  > **Search first:** KEGG, BioCyc, HMDB (Human Metabolome Database), BRENDA
- **Immune System Involvement**: Role of immune response (autoimmunity, immunodeficiency, chronic inflammation)
  > **Search first:** ImmPort, Immunome Database, IEDB, Gene Ontology
- **Tissue Damage Mechanisms**: How tissues/ are injured (oxidative stress, ischemia, fibrosis, necrosis)
  > **Search first:** PubMed, Gene Ontology, Reactome
- **Biochemical Abnormalities**: Specific molecular defects (enzyme deficiencies, receptor dysfunction, ion channel defects)
  > **Search first:** BRENDA, UniProt, KEGG, OMIM, PubMed
- **Epigenetic Changes**: DNA methylation, histone modifications affecting gene expression in disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Molecular Profiling** (if available):
  - Transcriptomics/gene expression changes
    > **Search first:** GEO (Gene Expression Omnibus), ArrayExpress, GTEx, Human Cell Atlas, SRA
  - Proteomics findings
    > **Search first:** PRIDE, ProteomeXchange, Human Protein Atlas, STRING, BioGRID
  - Metabolomics signatures
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB, METLIN
  - Lipidomics alterations
    > **Search first:** LIPID MAPS, SwissLipids, LipidHome, Metabolomics Workbench
  - Genomic structural features
    > **Search first:** UCSC Genome Browser, Ensembl, NCBI, dbVar, DGV
- **Advanced Technologies** (if applicable):
  - Single-cell analysis findings (cell-type specific mechanisms, cellular heterogeneity)
    > **Search first:** Human Cell Atlas, Single Cell Portal, GEO, CELLxGENE
  - Spatial transcriptomics findings
    > **Search first:** GEO, Spatial Research, Vizgen, 10x Genomics data
  - Multi-omics integration results
    > **Search first:** TCGA, ICGC, cBioPortal, LinkedOmics, PubMed
  - Functional genomics screens (CRISPR, RNAi)
    > **Search first:** DepMap, GenomeRNAi, PubMed, BioGRID ORCS

For each mechanism, describe:
- The causal chain from initial trigger to clinical manifestation
- Which mechanisms are upstream vs downstream
- What cell types and biological processes are involved
- Suggest GO terms for biological processes and CL terms for cell types

### 7. Anatomical Structures Affected

- **Organ Level**:
  - Primary organs directly affected
  - Secondary organ involvement (complications, secondary effects)
  - Body systems involved (cardiovascular, nervous, digestive, respiratory, endocrine, etc.)
  > **Search first:** Uberon, FMA (Foundational Model of Anatomy), OMIM, HPO, ICD-11, MeSH, SNOMED CT
- **Tissue and Cell Level**:
  - Specific tissue types affected (epithelial, connective, muscle, nervous)
  - Specific cell populations targeted (with Cell Ontology terms)
  > **Search first:** Uberon, Human Protein Atlas, Cell Ontology, Human Cell Atlas, CellMarker, PanglaoDB
- **Subcellular Level**:
  - Cellular compartments involved (mitochondria, nucleus, ER, lysosomes) (with GO Cellular Component terms)
  > **Search first:** Gene Ontology (Cellular Component), UniProt, Human Protein Atlas
- **Localization**:
  - Specific anatomical sites (with UBERON terms)
    > **Search first:** FMA, Uberon, NeuroNames (for brain), SNOMED CT
  - Lateralization (unilateral, bilateral, asymmetric)
    > **Search first:** HPO, clinical literature, imaging databases

### 8. Temporal Development

- **Onset**:
  - Typical age of onset (congenital, pediatric, adult, geriatric)
  - Onset pattern (acute, subacute, chronic, insidious)
  > **Search first:** OMIM, Orphanet, HPO, PubMed
- **Progression**:
  - Disease stages (early, intermediate, advanced, end-stage)
    > **Search first:** Cancer Staging Manual (AJCC), WHO classifications, PubMed
  - Progression rate (rapid, slow, variable)
  - Disease course pattern (episodic, relapsing-remitting, progressive, stable)
  - Disease duration (self-limited, chronic lifelong)
  > **Search first:** Disease registries, longitudinal cohort databases, natural history studies, PubMed, Orphanet, OMIM
- **Patterns**:
  - Remission patterns (spontaneous, treatment-induced)
    > **Search first:** Clinical trial databases, disease registries, PubMed
  - Critical periods (time windows of vulnerability or opportunity for intervention)
    > **Search first:** PubMed, developmental biology databases, clinical guidelines

### 9. Inheritance and Population

- **Epidemiology**:
  - Prevalence (cases per 100,000 at given time)
  - Incidence (new cases per 100,000 per year)
  > **Search first:** Orphanet, CDC, WHO, GBD (Global Burden of Disease), national registries, SEER, disease registries
- **For Genetic Etiology**:
  - Inheritance pattern (AD, AR, X-linked, mitochondrial, multifactorial, polygenic)
    > **Search first:** OMIM, Orphanet, ClinVar, GTR (Genetic Testing Registry)
  - Penetrance (complete, incomplete, age-dependent)
    > **Search first:** ClinVar, OMIM, PubMed, ClinGen
  - Expressivity (variable, consistent)
    > **Search first:** OMIM, ClinVar, PubMed
  - Genetic anticipation (increasing severity in successive generations)
    > **Search first:** OMIM, PubMed (especially for repeat expansion disorders)
  - Germline mosaicism
    > **Search first:** ClinVar, OMIM, genetic counseling literature, PubMed
  - Founder effects (population-specific mutations)
    > **Search first:** gnomAD, population genetics databases, PubMed
  - Consanguinity role
    > **Search first:** OMIM, population studies, genetic counseling resources
  - Carrier frequency
    > **Search first:** gnomAD, carrier screening databases, GeneReviews, GTR
- **Population Demographics**:
  - Affected populations (ethnic or demographic groups with higher prevalence)
    > **Search first:** gnomAD, 1000 Genomes, PAGE Study, PubMed, population registries
  - Geographic distribution (endemic areas, regional variation)
    > **Search first:** WHO, CDC, GBD, Orphanet, geographic epidemiology databases
  - Geographic distribution of specific variants
  - Sex ratio (male:female)
    > **Search first:** Disease registries, OMIM, PubMed, epidemiological databases
  - Age distribution of affected individuals
    > **Search first:** CDC, disease registries, SEER, Orphanet

### 10. Diagnostics

- **Clinical Tests**:
  - Laboratory tests (blood, urine, tissue chemistry, specific enzyme assays)
    > **Search first:** LOINC, LabTests Online, PubMed
  - Biomarkers (proteins, metabolites, genetic markers, circulating biomarkers)
    > **Search first:** FDA Biomarker List, BEST (Biomarkers, EndpointS, and other Tools), PubMed
  - Imaging studies (X-ray, CT, MRI, PET, ultrasound)
    > **Search first:** RadLex, DICOM, Radiopaedia, imaging databases
  - Functional tests (pulmonary function, cardiac stress tests)
    > **Search first:** LOINC, clinical guidelines, PubMed
  - Electrophysiology (EEG, EMG, ECG, nerve conduction studies)
    > **Search first:** LOINC, clinical neurophysiology databases, PubMed
  - Biopsy findings (histopathology, immunohistochemistry)
    > **Search first:** SNOMED CT, College of American Pathologists resources, PubMed
  - Pathology findings (microscopic examination)
    > **Search first:** SNOMED CT, Digital Pathology databases, PubMed
- **Genetic Testing**:
  > **Search first:** GTR (Genetic Testing Registry), GeneReviews, ClinGen
  - Overview of recommended genetic testing approach
  - Whole genome sequencing (WGS) utility
    > **Search first:** GTR, ClinVar, GEL (Genomics England), gnomAD
  - Whole exome sequencing (WES) utility
    > **Search first:** GTR, ClinVar, OMIM, GeneMatcher
  - Gene panels (which panels, which genes)
    > **Search first:** GTR, ClinVar, laboratory-specific databases
  - Single gene testing
    > **Search first:** GTR, ClinVar, OMIM, GeneReviews
  - Chromosomal microarray (CMA)
    > **Search first:** DECIPHER, ClinVar, dbVar, ECARUCA
  - Karyotyping
    > **Search first:** Chromosome Abnormality Database, ClinVar, cytogenetics resources
  - FISH
    > **Search first:** ClinVar, cytogenetics databases, PubMed
  - Mitochondrial DNA testing
    > **Search first:** MITOMAP, MSeqDR, ClinVar, GTR
  - Repeat expansion testing
    > **Search first:** GTR, ClinVar, repeat expansion databases, PubMed
- **Omics-Based Diagnostics** (if applicable):
  - RNA sequencing / transcriptomics
    > **Search first:** GEO, ArrayExpress, GTEx, RNA-seq databases
  - Proteomics
    > **Search first:** PRIDE, ProteomeXchange, FDA Biomarker database
  - Metabolomics
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB
  - Epigenomics
    > **Search first:** GEO, ENCODE, Roadmap Epigenomics, MethBase
  - Liquid biopsy
    > **Search first:** COSMIC, ClinVar, liquid biopsy databases, PubMed
- **Clinical Criteria**:
  - Standardized diagnostic criteria (DSM, ICD, society guidelines)
    > **Search first:** DSM-5, ICD-11, clinical society guidelines, UpToDate
  - Differential diagnosis (other conditions to rule out, with distinguishing features)
    > **Search first:** DynaMed, UpToDate, clinical decision support systems
- **Screening**:
  - Screening methods for asymptomatic individuals (newborn screening, carrier screening, cascade screening)
    > **Search first:** ACMG recommendations, CDC newborn screening, GTR

### 11. Outcome/Prognosis

- **Survival and Mortality**:
  - Survival rate (5-year, 10-year, overall)
    > **Search first:** SEER, cancer registries, disease-specific registries, PubMed
  - Life expectancy (with and without treatment if applicable)
    > **Search first:** Orphanet, disease registries, actuarial databases, PubMed
  - Mortality rate
    > **Search first:** CDC, WHO, GBD, national mortality databases
  - Disease-specific mortality (deaths directly attributable to disease)
    > **Search first:** Disease registries, CDC Wonder, GBD, PubMed
- **Morbidity and Function**:
  - Morbidity (disease-related disability and health impacts)
    > **Search first:** GBD, WHO, disability databases, PubMed
  - Disability outcomes (long-term functional impairments)
    > **Search first:** ICF (International Classification of Functioning), disability registries
  - Quality of life measures (EQ-5D, SF-36, PROMIS, disease-specific tools)
    > **Search first:** EQ-5D database, SF-36, PROMIS, PubMed
- **Disease Course**:
  - Complications (secondary problems: infections, organ failure, etc.)
    > **Search first:** ICD codes, disease registries, clinical databases, PubMed
  - Recovery potential (likelihood and extent of recovery, with vs without treatment)
    > **Search first:** Natural history studies, rehabilitation databases, PubMed
- **Prediction**:
  - Prognostic factors (age, disease severity, biomarkers, treatment response)
    > **Search first:** Prognostic models databases, clinical calculators, PubMed
  - Prognostic biomarkers (molecular markers predicting disease course)
    > **Search first:** FDA Biomarker database, PubMed, cancer prognostic databases

### 12. Treatment

- **Pharmacotherapy**:
  - Pharmacological treatments (drug names, drug classes, mechanisms of action)
    > **Search first:** DrugBank, RxNorm, ATC classification, DailyMed, FDA databases
  - Pharmacogenomics (how genetic variants affect drug metabolism, efficacy, toxicity)
    > **Search first:** PharmGKB, CPIC (Clinical Pharmacogenetics), FDA Table of PGx Biomarkers
- **Advanced Therapeutics**:
  - Gene therapy (viral vectors, CRISPR, gene replacement, gene editing)
    > **Search first:** ClinicalTrials.gov, FDA gene therapy database, ASGCT resources
  - Cell therapy (stem cell transplant, CAR-T, cellular therapeutics)
    > **Search first:** ClinicalTrials.gov, FDA cell therapy database, FACT standards
  - RNA-based therapies (ASOs, siRNA, mRNA therapies)
    > **Search first:** ClinicalTrials.gov, FDA approvals, PubMed
  - Targeted therapies (treatments directed at specific molecular targets)
    > **Search first:** My Cancer Genome, OncoKB, ClinicalTrials.gov, FDA approvals
  - Immunotherapies (checkpoint inhibitors, monoclonal antibodies)
    > **Search first:** Cancer Immunotherapy Database, FDA approvals, ClinicalTrials.gov
- **Surgical and Interventional**:
  - Surgical interventions (types of surgery, timing, outcomes)
    > **Search first:** CPT codes, surgical registries, clinical guidelines, PubMed
- **Supportive and Rehabilitative**:
  - Supportive care (symptom management, pain control, nutrition)
    > **Search first:** Clinical guidelines, Cochrane Library, PubMed
  - Rehabilitation (physical therapy, occupational therapy, speech therapy)
    > **Search first:** Rehabilitation medicine databases, clinical guidelines, PubMed
- **Experimental**:
  - Experimental treatments in clinical trials (with NCT identifiers if available)
    > **Search first:** ClinicalTrials.gov, EU Clinical Trials Register, WHO ICTRP
- **Treatment Outcomes**:
  - Treatment response rates
    > **Search first:** Clinical trial databases, FDA reviews, systematic reviews, PubMed
  - Side effects and adverse events
    > **Search first:** FDA Adverse Event Reporting System (FAERS), MedWatch, PubMed
- **Treatment Strategy**:
  - Treatment algorithms (clinical pathways, decision trees)
    > **Search first:** Clinical practice guidelines, NCCN Guidelines, UpToDate
  - Combination therapies
    > **Search first:** ClinicalTrials.gov, treatment guidelines, PubMed
  - Personalized medicine approaches (genotype-guided treatment)
    > **Search first:** My Cancer Genome, CIViC, PharmGKB, precision medicine databases

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

### 13. Prevention

- **Prevention Levels**:
  - Primary prevention (preventing disease occurrence: vaccination, risk factor modification)
    > **Search first:** CDC, WHO, USPSTF recommendations, Cochrane Library
  - Secondary prevention (early detection and treatment: screening programs, early intervention)
    > **Search first:** USPSTF, CDC screening guidelines, WHO
  - Tertiary prevention (preventing complications in those with disease)
    > **Search first:** Clinical guidelines, disease management protocols, PubMed
- **Immunization**: Vaccine strategies (if applicable)
  > **Search first:** CDC vaccine schedules, WHO immunization, FDA vaccine database
- **Screening and Early Detection**:
  - Screening programs (population-based: newborn screening, cancer screening)
    > **Search first:** CDC screening programs, USPSTF, cancer screening databases
  - Genetic screening (carrier screening, preimplantation genetic diagnosis, prenatal testing)
    > **Search first:** ACMG recommendations, ACOG guidelines, GTR
  - Risk stratification (identifying high-risk individuals for targeted prevention)
    > **Search first:** Risk prediction models, clinical calculators, PubMed
- **Behavioral Interventions**: Lifestyle modifications to reduce risk
  > **Search first:** CDC, WHO, behavioral intervention databases, Cochrane Library
- **Counseling**: Genetic counseling (risk assessment, family planning guidance)
  > **Search first:** NSGC resources, ACMG guidelines, GeneReviews
- **Public Health**:
  - Public health interventions (sanitation, vector control, health education)
    > **Search first:** CDC, WHO, public health databases, PubMed
  - Environmental interventions (reducing environmental risk factors)
    > **Search first:** EPA databases, WHO environmental health, PubMed
- **Prophylaxis**: Preventive medications or procedures
  > **Search first:** Clinical guidelines, FDA approvals, PubMed

### 14. Other Species / Natural Disease

- **Taxonomy**: Species affected (with NCBI Taxon identifiers)
  > **Search first:** NCBI Taxonomy
- **Breed**: Specific breeds affected (with VBO identifiers if applicable)
  > **Search first:** VBO (Vertebrate Breed Ontology)
- **Gene**: Orthologous genes in other species (with NCBI Gene IDs)
  > **Search first:** NCBI Gene
- **Natural Disease**:
  - Naturally occurring disease in other species (companion animals, wildlife)
    > **Search first:** OMIA (Online Mendelian Inheritance in Animals), VetCompass, PubMed
  - Veterinary relevance and importance in animal health
    > **Search first:** OMIA, veterinary databases, PubMed
- **Comparative Biology**:
  - Comparative pathology (similarities and differences across species)
    > **Search first:** OMIA, comparative pathology databases, PubMed
  - Evolutionary conservation of disease mechanisms
    > **Search first:** HomoloGene, OrthoMCL, Alliance of Genome Resources
- **Transmission** (if applicable):
  - Zoonotic potential
    > **Search first:** CDC zoonotic diseases, WHO zoonoses, GIDEON
  - Cross-species susceptibility
    > **Search first:** NCBI Taxonomy, veterinary databases, PubMed

### 15. Model Organisms

- **Model Types**:
  - Model organism type (mammalian, invertebrate, cellular, in vitro)
    > **Search first:** Alliance of Genome Resources, model organism databases
  - Specific model systems (mouse, rat, zebrafish, Drosophila, C. elegans, yeast, cell lines, organoids, iPSCs)
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, SGD, ATCC, Cellosaurus
  - Induced models (drug treatment, surgical intervention, environmental manipulation)
    > **Search first:** MGI, model organism databases, PubMed
- **Genetic Models**:
  - Types available (knockout, knock-in, transgenic, conditional, humanized)
    > **Search first:** MGI, IMPC, KOMP, EuMMCR, IMSR
- **Model Characteristics**:
  - Phenotype recapitulation (how well model reproduces human disease features)
    > **Search first:** Model organism databases, comparative studies, PubMed
  - Model limitations (aspects of human disease not captured)
    > **Search first:** Model organism databases, PubMed, review articles
- **Applications**:
  - Research applications (what aspects of disease can be studied)
    > **Search first:** Model organism databases, PubMed
- **Resources**:
  - Model databases
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, IMSR, EMMA, MMRRC

---

## Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic and clinical claims
- Prioritize recent reviews and landmark papers
- Include direct quotes from abstracts where possible to support key statements
- Distinguish evidence source types: human clinical, model organism, in vitro, computational

## Output Format

Structure your response as a comprehensive narrative organized by the sections above.
For each section, provide:
- Factual content with specific details (numbers, percentages, gene names, variant nomenclature)
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
- Evidence citations with PMIDs
- Direct quotes from abstracts to support key claims
- Clear indication when information is not available or not applicable for this disease

This report will be used to populate a disease knowledge base entry with:
- Pathophysiology descriptions with causal chains
- Gene/protein annotations (HGNC, GO terms)
- Phenotype associations (HP terms) with frequencies
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Neurodevelopmental Disorder With Or Without Seizures And Gait Abnormalities (NEDSGA) Caused By Pathogenic Variants In **GRIA4**

Neurodevelopmental disorder with or without seizures and gait abnormalities (NEDSGA) is a very rare, early‑onset Mendelian encephalopathy caused by heterozygous variants in the **GRIA4** gene, which encodes the GluA4 subunit of ionotropic AMPA‑type glutamate receptors on excitatory synapses in the central nervous system.[2][11][16] The disorder, catalogued under OMIM 617864 and MONDO:0060641, is characterized by global developmental delay, variable intellectual disability, early tone abnormalities evolving into spasticity, impaired or absent ambulation, and seizures of variable severity, often accompanied by imaging evidence of cortical atrophy and thinning of the corpus callosum.[1][4][16][18] All convincingly pathogenic variants reported to date are de novo heterozygous missense changes that cluster in highly conserved transmembrane or ligand‑binding domains of GRIA4, particularly the SYTANLAAF gating motif in the M3 segment, and are predicted to alter AMPA receptor gating and permeability in a dominant functional manner rather than cause simple loss of function.[11][12][16][18] Clinical series and a 2022 case report expand the phenotypic spectrum to include ocular manifestations such as nystagmus, strabismus, optic nerve hypoplasia, and retinal hypoplasia, as well as occasional cardiac anomalies, while mouse models of Gria4 deficiency demonstrate that perturbations of GluA4‑mediated synaptic transmission readily produce absence‑like epilepsy.[2][9][14][18] Aggregated evidence as of 2024 leads ClinGen’s Intellectual Disability and Autism Gene Curation Expert Panel to assign a moderate level of gene–disease validity for GRIA4–NEDSGA, with no contradictory data reported.[8][9] This report synthesizes current knowledge about NEDSGA across clinical, genetic, mechanistic, diagnostic, and translational dimensions, with explicit ontology mappings to support integration into structured disease knowledge bases.

## 1. Disease Information

### 1.1 Definition and Clinical Overview

Neurodevelopmental disorder with or without seizures and gait abnormalities (NEDSGA) is defined by OMIM as an autosomal dominant neurodevelopmental syndrome in which global developmental delay is apparent from infancy or early childhood and evolves into variably impaired intellectual development, with severity ranging from profound intellectual disability and absent speech to milder forms permitting attendance at special schools.[1][16] Early in life, affected infants typically manifest pronounced irritability, stiffness, and hypertonia, which later progress to spasticity and impaired gait, with some individuals never achieving independent ambulation and others demonstrating a clumsy, spastic gait.[1][4][16] Seizures occur in a substantial fraction of reported cases, spanning focal, generalized, and absence‑like semiologies and sometimes accompanied by abnormal electroencephalography (EEG), although epilepsy is not universally present and hence the term “with or without seizures.”[11][12][18] Neuroimaging findings commonly include cortical atrophy and thinning of the corpus callosum, and several patients have characteristic dysmorphic and neuromotor features such as large ears (macrotia), joint contractures, choreiform or stereotypic hand movements, and feeding difficulties.[4][13][16]

From a nosological standpoint, NEDSGA belongs to the broader group of monogenic neurodevelopmental disorders associated with ionotropic glutamate receptor subunits, which also includes disorders caused by variants in GRIA1, GRIA2, GRIA3, and GRIN family genes.[11][12][16] The causal link to GRIA4 was first described in detail in 2017, when Martin and colleagues identified five distinct de novo heterozygous missense variants in GRIA4 in five unrelated individuals with intellectual disability and associated neurological and behavioral features, using trio whole‑exome sequencing.[11][12][16][19] Subsequent work has added additional probands and variants, reinforcing a characteristic phenotype of early‑onset global developmental delay, tone abnormalities, abnormal gait, and variably present seizures and social behavior problems.[9][14][18] Clinically, NEDSGA overlaps with cerebral palsy and other early‑onset epileptic encephalopathies, but the combination of GRIA4 mutation, specific imaging and ocular findings, and autosomal dominant de novo inheritance pattern defines a distinct diagnostic entity.

### 1.2 Key Identifiers, Synonyms, and Classification

Multiple curated resources converge on a coherent set of identifiers for NEDSGA. OMIM lists the phenotype under entry **617864**, titled “Neurodevelopmental disorder with or without seizures and gait abnormalities,” and explicitly attributes causality to heterozygous mutations in **GRIA4** (MIM 138246) on chromosome 11q22.3.[2][16] The Monarch Initiative assigns the disease the MONDO identifier **MONDO:0060641**, with the primary label matching the OMIM title and annotating GRIA4 as the causal gene with autosomal dominant inheritance.[5] MedGen, the NCBI clinical phenotype database, records NEDSGA under C4693391 with the same descriptive label and links it to OMIM and MONDO identifiers.[1] ClinVar submissions referencing the condition typically use the OMIM title and include additional ontology identifiers, such as OMIM:617864, MedGen:C4693391, and MONDO:0060641.[6][7][10]

A concise summary of identifiers and classification is useful for knowledge base integration:

| Attribute                          | Value                                                                                          |
|------------------------------------|------------------------------------------------------------------------------------------------|
| Disease name                       | Neurodevelopmental disorder with or without seizures and gait abnormalities                   |
| MONDO ID                           | MONDO:0060641[5]                                                                              |
| OMIM phenotype ID                  | 617864[16]                                                                                    |
| Causal gene                        | GRIA4 (HGNC:4574; OMIM:138246)[2][16]                                                         |
| MedGen ID                          | C4693391[1]                                                                                   |
| Inheritance                        | Autosomal dominant[5][16]                                                                     |
| Category                           | Mendelian neurodevelopmental disorder                                                         |
| Synonyms                           | NEDSGA; Neurodevelopmental disorder with or without seizure(s) and gait abnormalities[4][14] |

The most commonly used informal synonym is the acronym **NEDSGA**, used in clinical and research literature, including the 2022 Frontiers in Genetics case report and the ClinGen curation.[9][14][18] Some sources use slightly variant phrasings, such as “neurodevelopmental disorder with or without seizure and gait abnormalities,” but they refer to the same entity defined by MONDO:0060641 and OMIM:617864.[14][18] There is no evidence that the term is applied to disorders caused by other genes; the disease name is gene‑agnostic in structure, but current curated resources explicitly tie MONDO:0060641 to GRIA4 and exclude other loci.[5][8][9]

### 1.3 Information Sources and Level of Aggregation

Information about NEDSGA is derived primarily from a small number of detailed case series and case reports, which are then aggregated and summarized in disease‑level resources such as OMIM, ClinGen, MedGen, Monarch Initiative, and specialized databases of ocular and genetic disorders.[1][4][5][9][13][16][18] The landmark paper by Martin et al. in The American Journal of Human Genetics provides rich phenotypic and genetic data on five unrelated probands, including clinical descriptions, EEG findings, neuroimaging, and variant annotation.[11][12][17][19] The 2022 Frontiers in Genetics article presents a single additional proband from China with comprehensive clinical, electrophysiological, imaging, and genetic characterization, and explicitly reviews the earlier five cases to delineate a core phenotype.[14][18] These seven human cases, together with subsequent reports referenced in the ClinGen curation (PMIDs 27479843, 35518358, 37921875, 38819422), form the main evidentiary base for disease definition and genotype–phenotype correlation.[9]

Derived resources such as OMIM and ClinGen present aggregated, disease‑level information synthesized from these primary publications, including standardized phenotype descriptions, inheritance pattern, molecular mechanism hypotheses, and curated gene–disease validity assessments.[2][9][16] The Eyes Disorders database at the University of Arizona aggregates ocular manifestations across cases to describe NEDSGA‑associated nystagmus, strabismus, optic nerve hypoplasia, and macrotia.[4][13] Monarch Initiative integrates ontological annotations, linking the phenotype to HPO terms and GRIA4 to gene ontologies.[5] Thus, while the knowledge base is built from individual patient data, most accessible information is presented as curated disease‑level summaries suitable for computational use.

## 2. Etiology

### 2.1 Genetic Causal Factors

The primary etiological factor in NEDSGA is heterozygous mutation in **GRIA4**, encoding the GluA4 subunit of AMPA‑type glutamate receptors.[2][11][16] OMIM uses a number sign (#) for entry 617864 to indicate that NEDSGA is caused by mutations in GRIA4 on chromosome 11q22.3, with all convincingly associated variants to date being missense changes.[2][16] Martin et al. identified five different de novo heterozygous missense variants—c.1915A>T (p.Thr639Ser), c.1921A>G (p.Asn641Asp), c.1928C>G (p.Ala643Gly), c.1931C>T (p.Ala644Val), and c.2090G>C (p.Arg697Pro)—in five unrelated probands with neurodevelopmental disorders, mainly intellectual disability and early tone abnormalities.[11][12][17][19] Four of these variants lie within the highly conserved SYTANLAAF motif in the transmembrane M3 segment, and the fifth affects an extracellular domain important for subunit assembly.[11][12][16][17]

The 2022 Frontiers in Genetics report describes another de novo heterozygous missense variant, c.1918G>T (p.Ala640Ser), in a female infant with severe developmental delay, limb hypertonia, generalized seizures, retinal hypoplasia, and chorioretinal hyperpigmentation.[14][18] ClinGen’s 2024 gene–disease validity curation notes that ten unique missense GRIA4 variants have been reported in ten probands across five publications, all in autosomal dominant fashion, and all within transmembrane or ligand‑binding domains.[9] Importantly, all variants are de novo in the proband, with unaffected parents and no evidence of familial segregation; this supports a model of sporadic dominant disease driven by highly deleterious, non‑recurrent mutations in an essential synaptic receptor subunit.[11][12][18]

Mechanistically, these missense variants are predicted by molecular modeling and homology to other AMPA subunits to alter receptor gating and ion conductance, rather than causing simple truncation or haploinsufficiency.[11][12][16] For instance, OMIM notes that variants in the SYTANLAAF motif likely disturb the gating mechanism, in some cases allowing leakage or an open state, while others may reduce channel permeability; the extracellular variant R697P is predicted to interfere with monomer–monomer interactions and receptor assembly.[16] This dominant functional effect is consistent with the absence of clear loss‑of‑function alleles among affected individuals and with the autosomal dominant inheritance pattern despite de novo origin.

### 2.2 Genetic Risk Factors, Susceptibility, and Modifier Genes

NEDSGA currently appears to be a monogenic, mutation‑driven disorder without established polygenic susceptibility loci or modifier genes. All reported human cases harbor a single heterozygous GRIA4 missense variant deemed pathogenic or likely pathogenic by ACMG/AMP criteria, with no evidence for additional causal variants in other genes.[11][12][14][18] Population databases such as gnomAD and the 1000 Genomes Project reportedly lack these variants or show them at extremely low allele frequencies, supporting their pathogenicity by the PM2 criterion for absence from controls.[7][10][18] ClinVar submissions for GRIA4 variants associated with NEDSGA classify missense changes like c.1918G>T (p.Ala640Ser) and c.1931C>T (p.Ala644Val) as pathogenic or likely pathogenic, whereas some other missense changes, such as c.1564A>G (p.Ile522Val), are currently variants of uncertain significance due to limited evidence and lack of segregation data.[6][7][10]

There are no reports of genetic modifiers that alter disease severity, penetrance, or specific phenotypic features in NEDSGA. However, given the complex role of AMPA receptors in synaptic transmission and plasticity, it is plausible that variants in other glutamatergic pathway genes, GABAergic system genes, or general neurodevelopmental genes could modulate disease expression in individual patients. For example, GRIA4 functions in heterotetrameric AMPA receptors that may include GRIA1, GRIA2, or GRIA3 subunits, and variants in those genes are known to cause related neurodevelopmental phenotypes.[11][12] Nonetheless, no specific modifier genes have been identified in the limited number of published NEDSGA cases, and systematic genome‑wide association or modifier studies are lacking.

### 2.3 Environmental and Lifestyle Risk Factors

No specific environmental, toxic, infectious, or lifestyle factors have been implicated as causal or strong risk factors for NEDSGA. The disease arises in infancy or early childhood in individuals with de novo GRIA4 mutations, and there is no pattern of exposure to particular toxins, radiation, infections, or nutritional deficiencies among reported cases.[11][12][14][18] Standard perinatal stressors such as prematurity, hypoxia–ischemia, or maternal illness are not consistently present, and where they are, they are not considered sufficient to explain the full phenotype of global developmental delay, seizures, and characteristic dysmorphic features.[11][18] Consequently, NEDSGA is best conceptualized as a primary genetic neurodevelopmental disorder in which environmental influences play a secondary, nonspecific role.

General factors known to influence neurodevelopment and seizure threshold, such as febrile illnesses, sleep deprivation, or exposure to pro‑convulsant substances, may exacerbate symptom expression in individuals with NEDSGA, but these are generic seizure triggers rather than disease‑specific risk factors. Likewise, socioeconomic status, access to medical care, and rehabilitative services will modulate outcomes and quality of life but are not etiological factors for disease onset.

### 2.4 Protective Factors and Gene–Environment Interactions

Given the rarity of NEDSGA and the small number of described cases, no genetic protective variants or environmental exposures have been convincingly demonstrated to mitigate disease risk or severity. Population databases such as gnomAD contain numerous benign missense variants in GRIA4 with no associated phenotype, indicating that the protein tolerates some level of variation, but these are not protective in the sense of reducing risk below baseline; they simply represent non‑pathogenic variation.[2][7][10] There is no evidence of alleles that counteract the effects of pathogenic GRIA4 variants through dominant negative suppression or compensatory up‑regulation of other AMPA subunits.

Similarly, no specific environmental interventions have been reported to prevent onset or significantly alter disease trajectory in NEDSGA beyond general supportive care. Early and intensive rehabilitation, seizure control, and optimized nutrition may improve functional outcomes but are tertiary rather than primary protective factors. Because all reported pathogenic GRIA4 variants are de novo and present in the germline, gene–environment interactions, in the sense of external exposures modulating penetrance, are unlikely to be major determinants of disease occurrence. Nonetheless, at the level of pathophysiology, environmental stimuli such as sensory experience, learning, and stress can modulate synaptic plasticity and AMPA receptor trafficking, potentially influencing symptom expression; however, these interactions have not been specifically studied in NEDSGA.[11][12]

Overall, NEDSGA is best characterized etiologically as a sporadic, autosomal dominant disorder caused by de novo heterozygous missense variants in GRIA4, with negligible contribution from identifiable environmental risk or protective factors and no recognized modifier genes to date.

## 3. Phenotypes

### 3.1 Global Developmental Delay and Intellectual Disability

The core phenotype of NEDSGA is global developmental delay (GDD), progressing to intellectual disability (ID) of variable severity.[1][4][16][18] OMIM and MedGen emphasize that developmental delay is apparent from infancy or very early childhood, affecting both motor and cognitive milestones: many probands show delayed head control, sitting, standing, and walking, along with delayed language acquisition and social engagement.[1][16][18] Martin et al. report that their five probands, ranging in age from 4 to 21 years, all had early developmental delay, with some never acquiring speech and others achieving limited expressive language but with clear cognitive impairment.[11][12][17] The 2022 Chinese proband exhibited severe motor and cognitive delay from the neonatal period, including inability to roll or sit at expected ages and lack of social smile.[14][18]

Intellectual disability in NEDSGA spans a spectrum from profound to mild, but most reported cases cluster toward the severe end. OMIM notes that intellectual development can range from profound, with absent speech, to mild, with the ability to attend special schools, underscoring variability in expressivity.[16] In Martin’s cohort, at least one proband could speak short sentences and attend school with support, while others had almost no functional speech and required assistance with most activities of daily living.[11][12][17] The Frontiers in Genetics case describes “severe developmental delay,” with the patient unable to follow simple commands and showing marked cognitive impairment.[14][18] These observations suggest mapping to HPO terms such as **HP:0001263 (Global developmental delay)** and **HP:0001249 (Intellectual disability)**, with severity modifiers like HP:0010864 (Severe intellectual disability) and HP:0010863 (Profound intellectual disability) for many individuals.

The impact of GDD and ID on quality of life is substantial, affecting education, communication, autonomy, and social participation. Most patients require long‑term multidisciplinary support, including special education, speech and occupational therapy, and caregiver assistance for self‑care tasks. Emotional and behavioral difficulties may further complicate functioning, as some individuals exhibit problems of social behavior, hyperactivity, or autistic traits, though systematic behavioral phenotyping has not been performed.[11][12][16] From a health‑related quality of life perspective, NEDSGA likely scores low on domains of mobility, self‑care, usual activities, and cognition on instruments such as EQ‑5D or SF‑36, although such measures have not been formally reported in the literature.

### 3.2 Tone Abnormalities, Spasticity, and Gait Impairment

Another defining phenotype of NEDSGA is abnormal muscle tone, evolving into spasticity and impaired gait. OMIM and eyes.arizona.edu describe that most affected individuals show early irritability, stiffness, and hypertonia, which later progress to spasticity and impaired gait.[4][13][16] Neonatal hypotonia has been noted in some cases, highlighting that tone abnormalities can be biphasic, with initial floppiness followed by hypertonia and spasticity as corticospinal pathways mature.[4][18] Martin et al. report hypertonia and increased startle reflexes in infants, advancing to prominent spasticity in older children, often with contractures and difficulty walking.[11][12][17] The Chinese proband had limb hypertonia, spastic posturing, and delayed motor milestones, and ultimately failed to achieve independent ambulation within the observational window.[14][18]

Gait abnormalities are central to the disease name. Some individuals are unable to walk at all, whereas those who do walk exhibit clumsy, spastic gait reminiscent of spastic diplegic cerebral palsy.[4][13][16] Joint contractures, particularly at the ankles and knees, restrict mobility and cause pain, further impairing gait.[4][13] These features correspond to HPO terms such as **HP:0002067 (Spasticity)**, **HP:0002312 (Spastic gait)**, **HP:0001371 (Hypertonia)**, **HP:0001319 (Contractures)**, and **HP:0004885 (Impaired gait)**. The onset of tone abnormality is typically neonatal or early infancy, with progression over months to years as spasticity and contractures develop; the course is generally chronic and non‑remitting, though intensity may fluctuate with growth, rehabilitative interventions, and seizure control.[4][11][18]

Tone abnormalities and gait impairment have profound effects on quality of life, limiting independent mobility, increasing risk of falls and injuries, and contributing to pain and fatigue. Many patients will require assistive devices such as walkers, orthoses, or wheelchairs, and orthopedic interventions may be needed for contractures and deformities. From the perspective of activities of daily living, impaired gait affects participation in education, work, and social engagement, and increases caregiver burden.

### 3.3 Seizures and Electroencephalographic Abnormalities

Seizures are present in most, but not all, reported NEDSGA cases, leading to the “with or without seizures” qualifier. Martin et al. note that four of their five probands had seizures or abnormal EEGs, with seizure types including generalized tonic–clonic, absence‑like episodes with behavioral arrest, and focal events.[11][12][17][19] OMIM’s summary highlights that some patients develop seizures of variable severity early in life, though not universally.[16] The Chinese proband experienced generalized seizures beginning in early infancy, with partial seizures and epileptiform discharges documented on EEG.[14][18] Eyes.arizona.edu and Monarch Initiative list “seizures” as a common symptom, and ClinGen’s evidence summary for GRIA4–NEDSGA emphasizes seizures and/or EEG abnormalities as characteristic features.[4][5][9][13]

EEG findings reported in humans are limited but include epileptiform discharges and patterns reminiscent of absence epilepsy, consistent with the mouse Gria4 deficiency model that exhibits frequent spike–wave discharges and behavioral arrest.[2][9][11][12] Although detailed EEG phenotyping is sparse, mapping to HPO terms such as **HP:0001250 (Seizures)**, **HP:0002123 (Generalized tonic‑clonic seizures)**, **HP:0002069 (Absence seizures)**, and **HP:0002353 (Abnormal EEG)** is appropriate. Seizure onset tends to be in early infancy or childhood, often within the first year of life, and the course may be chronic with variable control depending on antiepileptic treatment and comorbid factors.[11][14][18]

Seizures significantly impact quality of life by increasing risk of injuries, cognitive regression, and psychosocial stress. Frequent uncontrolled seizures can worsen developmental trajectories and diminish the effectiveness of rehabilitative therapies. Moreover, epilepsy management imposes burdens of medication side effects, regular monitoring, and emergency preparedness, all of which complicate care in children with severe neurodevelopmental disabilities.

### 3.4 Ocular and Visual Phenotypes

Ocular manifestations form a notable component of the NEDSGA phenotype, particularly as described in the Eyes Disorders database and the 2022 case report. Eyes.arizona.edu notes that nystagmus and strabismus are common ocular features, with optic nerve hypoplasia present in some individuals, and lists macrotia (large ears) as a conspicuous dysmorphic feature.[4][13] The Chinese proband had retinal hypoplasia and chorioretinal hyperpigmentation on fundus examination, along with limb hypertonia and seizures.[14][18] These findings suggest involvement of the visual system at multiple levels, including ocular motility, retinal development, and optic nerve structure.

Appropriate HPO mappings include **HP:0000639 (Nystagmus)**, **HP:0000486 (Strabismus)**, **HP:0000609 (Optic nerve hypoplasia)**, **HP:0000484 (Retinal hypoplasia)**, and **HP:0000556 (Chorioretinal hyperpigmentation)**.[4][14][18] The onset of these ocular abnormalities is usually early infancy; nystagmus and strabismus may be noted soon after birth or within the first months of life, while retinal and optic nerve abnormalities are discovered via ophthalmologic evaluation prompted by visual tracking issues or suspected cortical visual impairment.[4][13][18] Their progression appears relatively stable, though detailed longitudinal data are lacking.

Visual impairment contributes further to functional disability, affecting exploration, learning, and social interaction. Combined with developmental delay and motor disability, ocular involvement can severely restrict environmental engagement and increase reliance on caregivers. Accurate recognition of ocular phenotypes in NEDSGA is important both for prognosis and for planning appropriate visual rehabilitation and educational interventions.

### 3.5 Dysmorphic, Neuromotor, and Systemic Features

Beyond the major neurological and ocular manifestations, NEDSGA includes a variety of dysmorphic and systemic features. Eyes.arizona.edu describes large ears (macrotia) as the most obvious dysmorphic feature, along with choreiform and stereotypic hand movements, feeding difficulties, and sleeping problems.[4][13] Martin et al. and OMIM mention irritability, increased startle responses, and stiffness in neonates, with some developing joint contractures and short stature.[11][12][16] The Frontiers in Genetics case adds cardiovascular findings, including tricuspid regurgitation and a patent foramen ovale detected by echocardiography, as well as retinal hypoplasia and chorioretinal hyperpigmentation.[14][18]

These manifestations can be mapped to HPO terms such as **HP:0004322 (Macrotia)**, **HP:0001337 (Choreiform movements)**, **HP:0000734 (Stereotypy)**, **HP:0002028 (Feeding difficulties)**, **HP:0001251 (Irritability)**, **HP:0001285 (Hyperreflexia)** or **HP:0002376 (Exaggerated startle response)**, **HP:0001371 (Hypertonia)**, **HP:0004322 (Short stature)**, **HP:0001659 (Tricuspid regurgitation)**, and **HP:0001655 (Patent foramen ovale)**.[4][13][14][16][18] Many of these features emerge in the neonatal period or early infancy and persist chronically, though some, such as irritability and sleep problems, may fluctuate over time or improve with symptomatic management.

Dysmorphic features like macrotia, along with joint contractures and characteristic movements, can aid clinical recognition of NEDSGA and inform differential diagnosis. Feeding difficulties increase risk of malnutrition and aspiration, necessitating interventions such as feeding therapy, thickened feeds, or gastrostomy tubes. Sleep problems exacerbate caregiver stress and may worsen seizures. Cardiac anomalies, while not universally present, require appropriate monitoring and management and may influence perioperative planning for orthopedic or other surgeries.

### 3.6 Phenotype Summary and Suggested Ontology Terms

To support structured representation, Table 2 summarizes key phenotypes, approximate frequency among reported individuals, onset, and suggested HPO terms. Frequencies remain qualitative due to the small total number of cases.

| Phenotype                               | Type              | Approx. Frequency in Reported Cases | Typical Onset        | HPO Term(s)                           |
|-----------------------------------------|-------------------|-------------------------------------|----------------------|----------------------------------------|
| Global developmental delay              | Symptom/sign      | Nearly universal[11][14][16][18]   | Neonatal/infancy     | HP:0001263                            |
| Intellectual disability (variable)      | Symptom/sign      | Nearly universal[11][16][18]       | Childhood             | HP:0001249; HP:0010864/63 (severity)  |
| Hypertonia and spasticity               | Clinical sign     | Very common[4][11][16][18]         | Neonatal/infancy     | HP:0002067; HP:0001371                |
| Impaired or spastic gait                | Clinical sign     | Common; some non‑ambulatory[4][11] | Childhood             | HP:0004885; HP:0002312                |
| Seizures (variable types)               | Symptom/sign      | Majority, but not all[11][14][16]  | Infancy/childhood    | HP:0001250; HP:0002123; HP:0002069    |
| Abnormal EEG                            | Laboratory        | Common among seizure cases[11][9]  | Childhood             | HP:0002353                            |
| Nystagmus/strabismus                    | Clinical sign     | Common ocular features[4][13][18]  | Infancy              | HP:0000639; HP:0000486                |
| Optic nerve/retinal hypoplasia         | Clinical sign     | Some individuals[4][18]            | Infancy              | HP:0000609; HP:0000484                |
| Macrotia (large ears)                   | Physical feature  | Frequent[4][13]                    | Congenital            | HP:0004322                            |
| Joint contractures                      | Physical feature  | Several cases[4][16]               | Childhood             | HP:0001319                            |
| Choreiform/stereotypic hand movements   | Neuromotor sign   | Some cases[4][13]                  | Childhood             | HP:0001337; HP:0000734                |
| Feeding difficulties                    | Symptom           | Common[4][18]                      | Neonatal/infancy     | HP:0002028                            |
| Irritability and increased startle      | Symptom/sign      | Several neonates[1][4][16][18]     | Neonatal             | HP:0001251; HP:0002376                |
| Cortical atrophy, thin corpus callosum  | Imaging finding   | Documented subset[4][16][18]       | Childhood imaging     | HP:0002120; HP:0002079                |
| Short stature                           | Physical feature  | At least one mildly affected[4]    | Childhood             | HP:0004322 (Short stature)            |
| Cardiac anomalies (PFO, TR)             | Clinical sign     | Single case[14][18]                | Neonatal/infancy     | HP:0001655; HP:0001659                |

Although the sample size is small, these phenotypes collectively define NEDSGA as a multisystem neurodevelopmental disorder with predominant central nervous system involvement, significant ocular and musculoskeletal features, and occasional cardiac anomalies, all arising in the context of GRIA4 mutation.

## 4. Genetic and Molecular Information

### 4.1 The GRIA4 Gene and Protein

**GRIA4** (HGNC:4574) encodes the glutamate ionotropic receptor AMPA‑type subunit 4, also known as GluA4 or GluR4.[2][11] It resides on chromosome 11q22.3 and belongs to the family of L‑glutamate‑gated ion channels that mediate fast excitatory synaptic transmission in the mammalian CNS.[2] AMPA receptors are tetrameric complexes assembled from combinations of GRIA1–4 subunits (GluA1–4), forming ligand‑gated cation channels that respond to glutamate and its synthetic agonist AMPA.[2][11] GRIA4 is particularly expressed in cerebellar, hippocampal, and cortical neurons, where it contributes to synaptic currents underlying learning, memory, and motor coordination.[11][12][19]

Structurally, GluA4 contains an extracellular N‑terminal domain, a ligand‑binding domain formed by two discontinuous segments (S1 and S2), three transmembrane helices (M1, M3, M4) and a re‑entrant pore loop (M2), and an intracellular C‑terminal domain involved in trafficking and scaffolding.[11][12] The highly conserved **SYTANLAAF** motif, located within the M3 transmembrane segment, functions as the gating hinge controlling channel opening and closing in response to ligand binding.[11][12][16] The GluA4 subunit participates in receptor assembly, trafficking, synaptic anchoring, and modulation by protein kinases such as PKC‑gamma, which has been reported to regulate GLUR4‑containing AMPA receptors.[2]

From a molecular ontology perspective, GRIA4 can be annotated with GO terms such as **GO:0005234 (extracellular ligand‑gated ion channel activity)**, **GO:0004971 (AMPA glutamate receptor activity)**, **GO:0005261 (cation channel activity)**, **GO:0006812 (cation transport)**, and **GO:0007268 (synaptic transmission)**. Cellular component annotations include **GO:0005886 (plasma membrane)**, **GO:0098984 (neuron projection)**, and **GO:0005891 (AMPA‑type glutamate receptor complex)**. Biological process terms such as **GO:0007611 (learning)** and **GO:0007612 (memory)** capture its role in synaptic plasticity.

### 4.2 Pathogenic Variants in GRIA4 Associated with NEDSGA

All GRIA4 variants definitively associated with NEDSGA are heterozygous missense changes affecting highly conserved residues in functionally critical domains. Martin et al. identified five de novo missense variants in five unrelated probands: c.1915A>T (p.Thr639Ser), c.1921A>G (p.Asn641Asp), c.1928C>G (p.Ala643Gly), c.1931C>T (p.Ala644Val), and c.2090G>C (p.Arg697Pro).[11][12][17][19] Four of these variants lie within the SYTANLAAF motif in the M3 transmembrane segment, while the fifth affects an extracellular domain critical for inter‑subunit interactions.[11][12][16] OMIM enumerates these variants as 138246.0001–138246.0005 and notes their de novo origin, absence from population databases, and predicted disruptive effects on gating and permeability.[2][16]

The 2022 Frontiers in Genetics case adds c.1918G>T (p.Ala640Ser), another de novo missense variant that clusters in the same transmembrane region and is predicted to be pathogenic based on conservation, structural modeling, and phenotype concordance.[14][18] ClinVar entries, such as RCV001807688 for NM_000829.4(GRIA4):c.1918G>T (p.Ala640Ser), associate this variant with NEDSGA and label it as pathogenic or likely pathogenic, using ACMG criteria including PS2 (de novo), PM2 (absent from controls), PP3 (computational support), and PP4 (patient’s phenotype highly specific).[6][18]

Additional GRIA4 missense variants have been submitted to ClinVar with varying significance interpretations. For example, NM_000829.4(GRIA4):c.1931C>T (p.Ala644Val) is linked to NEDSGA and considered a pathogenic missense variant, located within the SYTANLAAF motif and predicted to alter gating by favoring an open channel state.[7][16] In contrast, NM_000829.4(GRIA4):c.1564A>G (p.Ile522Val), affecting an earlier transmembrane region, is currently classified as a variant of uncertain significance (VUS), based on limited evidence, despite its absence from controls and predicted deleterious effect.[10] NM_000829.4(GRIA4):c.2127T>C (p.Ala709=), a synonymous variant, is classified as likely benign, reflecting its non‑alteration of amino acid sequence and lack of disease association.[3]

A structured summary of key pathogenic variants is given in Table 3.

| Variant (cDNA, protein)                | Domain/Region          | Evidence Level                            | Classification      | Source(s)                               |
|----------------------------------------|------------------------|-------------------------------------------|---------------------|------------------------------------------|
| c.1915A>T (p.Thr639Ser)               | SYTANLAAF motif, M3   | 1 proband, de novo, modeling[11][12][16] | Pathogenic          | AJHG 2017; OMIM 138246.0001[11][16][17] |
| c.1921A>G (p.Asn641Asp)               | SYTANLAAF motif, M3   | 1 proband, de novo, modeling[11][12][16] | Pathogenic          | AJHG 2017; OMIM 138246.0002[11][16]     |
| c.1928C>G (p.Ala643Gly)               | SYTANLAAF motif, M3   | 1 proband, de novo, modeling[11][12][16] | Pathogenic          | AJHG 2017; OMIM 138246.0003[11][16]     |
| c.1931C>T (p.Ala644Val)               | SYTANLAAF motif, M3   | 1 proband, de novo, modeling[7][11][16]  | Pathogenic          | AJHG 2017; ClinVar; OMIM 138246.0004[7][11][16] |
| c.2090G>C (p.Arg697Pro)               | Extracellular domain  | 1 proband, de novo, modeling[11][12][16] | Pathogenic          | AJHG 2017; OMIM 138246.0005[11][16]     |
| c.1918G>T (p.Ala640Ser)               | Transmembrane M3      | 1 proband, de novo, modeling[14][18]     | Pathogenic          | Front Genet 2022; ClinVar[6][14][18]    |

ClinGen’s 2024 curation aggregates these and additional published variants, noting ten unique missense changes reported in ten probands, all de novo and all clustering in transmembrane and ligand‑binding domains, with a total of seven evidence points under their semi‑quantitative framework.[9] This pattern strongly supports a specific mutational hotspot mechanism in GRIA4, rather than widely distributed loss‑of‑function alleles.

### 4.3 Variant Types, Origin, and Population Frequencies

The pathogenic GRIA4 variants in NEDSGA are uniformly **missense** single‑nucleotide variants (SNVs) that alter single amino acids in critical functional motifs. No nonsense, frameshift, canonical splice‑site, or large structural variants have been reported as causal for NEDSGA.[11][12][14][16][18] Synonymous variants, such as c.2127T>C (p.Ala709=), are classified as likely benign in ClinVar and appear as incidental findings or polymorphisms without disease association.[3]

All convincing pathogenic variants are **germline de novo**, present in the proband but absent in both parents, as established by trio whole‑exome sequencing and confirmed by Sanger sequencing.[11][12][14][16][18] There is no evidence of somatic mosaicism or somatic acquisition in specific tissues, nor of inherited pathogenic alleles; the disease occurs sporadically in families with unaffected parents.[11][16][18] This pattern aligns with a highly deleterious dominant effect such that carriers would be strongly selected against, leading to low recurrence in population cohorts.

Population frequency data, though summarized rather than fully tabulated in primary sources, indicate that these missense variants are absent from major databases such as the 1000 Genomes Project and gnomAD, or present at extremely low allele frequencies consistent with pathogenicity.[7][16][18] For example, OMIM notes that c.1931C>T (p.Ala644Val) was not found in 1000 Genomes or gnomAD, and the 2022 case report similarly reports absence of c.1918G>T (p.Ala640Ser) from these databases.[16][18] This supports the use of ACMG criterion PM2 (absence from controls) in variant classification and underscores the ultra‑rare nature of NEDSGA.

### 4.4 Functional Consequences: Gain of Function vs Loss of Function

Although direct functional studies on patient‑derived cells or recombinant mutant receptors have not yet been published, molecular modeling and analogy to other AMPA receptor subunits suggest that NEDSGA variants exert **dominant functional effects** rather than simple loss of function.[11][12][16] OMIM’s summary of Martin et al. emphasizes that variants in the SYTANLAAF motif are predicted to disturb the gating mechanism, with three variants oriented toward the center of the pore region likely leading to disturbed gating and leakage or open state, and a fourth variant in the motif likely reducing channel permeability.[16] The extracellular variant R697P is predicted to interfere with monomer binding and receptor assembly.[16]

Martin et al. conclude that the mutations “were predicted to have a dominant functional effect rather than to cause a loss of function,” suggesting gain‑of‑function or qualitative change in channel properties such as altered activation kinetics, conductance, or desensitization.[11][12][16][17] This interpretation is supported by the mouse Gria4 deficiency model, in which partial or complete lack of Gria4 leads to absence seizures and spike–wave discharges, indicating that both increased and decreased GluA4 function can perturb cortical excitability.[2][9] However, whether human NEDSGA results from excessive or insufficient synaptic currents, or from more complex changes in receptor dynamics, remains to be experimentally resolved.

From a mechanistic ontology standpoint, NEDSGA can be associated with **GO:0005234 (extracellular ligand‑gated ion channel activity)** and **GO:0005261 (cation channel activity)**, with the specific functional abnormality classified as **ion channel gating defect** and **biochemical abnormality: receptor dysfunction**, consistent with OMIM’s characterization of “abnormal AMPA receptor‑dependent synaptic activity.”[2][16] This places NEDSGA among a growing group of “channelopathies” affecting glutamatergic neurotransmission.

### 4.5 Epigenetic and Regulatory Information

No disease‑specific epigenetic or transcriptional regulatory abnormalities have been reported for GRIA4 in NEDSGA. There is no evidence of promoter methylation changes, histone modifications, or non‑coding regulatory variants driving altered GRIA4 expression in affected individuals.[11][12][14][18] Likewise, no transcriptomic profiling of human NEDSGA tissues has been published to identify gene expression networks perturbed by GRIA4 mutation; multi‑omics integration data are available mainly for more common neurodevelopmental disorders.

Nonetheless, GRIA4 is known in general neuroscience literature to be subject to activity‑dependent regulation, including phosphorylation by kinases such as PKC‑gamma and trafficking changes in response to synaptic activity, which influence synaptic strength and plasticity.[2] These regulatory mechanisms would be relevant to NEDSGA pathophysiology, but their specific status in patients remains inferred rather than directly measured. Future work using RNA‑seq, ATAC‑seq, and ChIP‑seq in induced pluripotent stem cell (iPSC)‑derived neurons from NEDSGA patients could illuminate how pathogenic GRIA4 variants interact with epigenetic programs to shape neuronal development and function.

### 4.6 Chromosomal Abnormalities

NEDSGA is linked to sequence‑level variants in GRIA4 rather than to large‑scale chromosomal abnormalities. GRIA4 lies at 11q22.3, but no recurrent deletions, duplications, translocations, or inversions at this locus have been associated specifically with the NEDSGA phenotype.[2][16] DECIPHER and related structural variant databases may contain individuals with 11q22 rearrangements and neurodevelopmental phenotypes, but these have not been formally tied to GRIA4 haploinsufficiency or NEDSGA.

Consequently, chromosomal microarray (CMA) and karyotyping are not expected to detect NEDSGA‑causing lesions unless a broader 11q22 copy number change involving GRIA4 is present, which has not been reported to date. The primary genetic abnormalities in NEDSGA are single‑gene missense variants, best detected by sequencing rather than cytogenetic methods.

## 5. Environmental Information

### 5.1 Non‑Genetic Contributing Factors

As outlined in the etiology section, NEDSGA is fundamentally a genetic disorder caused by de novo GRIA4 mutation, with no recognized environmental exposures serving as primary causes. There is no evidence from the small published case series linking NEDSGA to specific toxins, pollutants, radiation, occupational exposures, or infectious agents.[11][12][14][18] Reported pregnancies and perinatal courses are generally unremarkable or include common complications without a shared pattern suggestive of teratogenesis. Consequently, environmental factors are best viewed as background influences that may modulate symptom severity rather than as etiological drivers.

However, generic environmental modifiers of seizure threshold and neurodevelopment—such as prenatal nutrition, perinatal hypoxia‑ischemia, infections, and exposure to neurotoxic substances—could alter the clinical expression of NEDSGA, as they do in other epileptic encephalopathies. For instance, severe infections or hypoxic events in infancy might exacerbate cortical injury in a brain already rendered vulnerable by GRIA4 mutation, leading to worse developmental outcomes. These interactions are plausible but remain speculative in the absence of specific NEDSGA‑focused studies.

### 5.2 Lifestyle and Infectious Factors

Lifestyle factors, including diet, exercise, and substance use, have not been described as relevant to NEDSGA onset, given its congenital or early‑infantile presentation. As affected individuals age, lifestyle choices may influence comorbid conditions, such as obesity, cardiovascular disease, or musculoskeletal pain, but these are secondary issues rather than direct influences on the underlying neurodevelopmental disorder.

Infectious agents, including neurotropic viruses and bacteria, may trigger seizures or transient regressions in children with NEDSGA, as in other epileptic conditions, but there is no suggestion of a causative role in disease onset. Immunizations, when appropriately administered, are important for general health but do not alter genetic risk for NEDSGA.

In summary, environmental and lifestyle contributions to NEDSGA are minimal relative to the dominant impact of GRIA4 mutation, and no specific non‑genetic factors are currently annotated as causal or protective for this disease.

## 6. Mechanism / Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Clinical Phenotype

1. Heterozygous de novo missense mutation in the **GRIA4** gene alters the amino acid sequence of the GluA4 subunit in critical transmembrane or ligand‑binding domains.[11][12][16][18]

2. The altered GluA4 protein integrates into AMPA receptor tetramers, leading to abnormal receptor gating, ion conductance, or assembly, inferred from molecular modeling and analogy to other AMPA subunits.[11][12][16]

3. Abnormal AMPA receptor function results in dysregulated excitatory synaptic transmission in cortical, hippocampal, and cerebellar circuits, causing an imbalance between excitation and inhibition; this step is inferred from receptor function and mouse models.[2][9][11]

4. Synaptic transmission defects during critical periods of brain development impair neuronal migration, dendritic arborization, synaptogenesis, and synaptic plasticity, leading to disrupted network formation and connectivity; this is inferred from known roles of AMPA receptors in development.[11][12]

5. Impaired network development and connectivity manifest as global developmental delay and intellectual disability, with deficits in motor, language, and cognitive domains.[1][11][16][18]

6. Dysregulated cortical excitability and network synchronization predispose to epileptiform activity and seizures, as evidenced by human EEG abnormalities and spike–wave discharges in Gria4‑deficient mice.[2][9][11][12][18]

7. Altered corticospinal and motor circuit function, combined with pyramidal tract involvement, produces early hypertonia and spasticity, evolving into spastic gait and joint contractures.[1][4][11][16]

8. Abnormal GRIA4 function in visual pathways and retinal or optic nerve development contributes to nystagmus, strabismus, optic nerve hypoplasia, and retinal hypoplasia; this step is inferred from ocular findings and general glutamatergic roles.[4][13][18]

9. Secondary complications, including feeding difficulties, sleep disturbances, orthopedic deformities, and cardiac anomalies, arise from a combination of primary neurodevelopmental deficits and systemic developmental perturbations.[4][14][18]

10. The cumulative effects of these neurological, ocular, and systemic abnormalities result in long‑term functional disability, reduced quality of life, and need for comprehensive supportive care.

### 6.2 Molecular Pathways and AMPA Receptor Dysfunction

At the molecular level, NEDSGA arises from dysfunction of AMPA‑type glutamate receptors, specifically those containing mutant GluA4 subunits. AMPA receptors mediate fast excitatory synaptic transmission in the CNS by responding to glutamate released from presynaptic terminals and opening cation channels that allow Na\(^+\) and, in some cases, Ca\(^{2+}\) influx, depolarizing the postsynaptic neuron.[2][11] The gating mechanism is controlled by conformational changes in the ligand‑binding domain and transmitted to the transmembrane pore via the SYTANLAAF motif in the M3 segment.[11][12][16]

NEDSGA‑associated GRIA4 missense variants cluster in this SYTANLAAF motif and in adjacent transmembrane regions, suggesting a primary defect in gating rather than in ligand binding. Molecular modeling performed by Martin et al. showed that three SYTANLAAF variants orient toward the pore center, likely disturbing gating by destabilizing the closed state or altering the open–closed equilibrium, while another variant may reduce permeability by altering the pore constriction.[11][12][16][17] The extracellular R697P variant is predicted to affect inter‑subunit interactions, possibly impairing tetramer assembly or stability.[11][12][16]

These structural perturbations are expected to alter AMPA receptor function in one of several ways: increased baseline conductance (constitutive activity) leading to tonic depolarization, decreased maximal conductance, altered activation and deactivation kinetics, or impaired desensitization. Any of these changes would disrupt synaptic integration and plasticity, particularly in circuits that rely heavily on GluA4, such as cerebellar granule and Purkinje cells, cortical pyramidal neurons, and hippocampal neurons.[2][11][12] The net effect on neural circuits—hyperexcitability vs hypoexcitability—may vary by variant, brain region, and developmental stage, complicating mechanistic generalization.

An illustrative molecular pathway is the glutamatergic synapse as represented in KEGG and Reactome, in which presynaptic glutamate release activates AMPA receptors (GRIA1–4) and NMDA receptors (GRIN1/2), initiating depolarization, Ca\(^{2+}\) influx, and downstream signaling cascades including CaMKII and CREB‑dependent transcription.[11] Mutant GRIA4 would alter this cascade at the level of initial cation influx, thereby changing downstream gene expression and synaptic plasticity. GO terms such as **GO:0098962 (neuronal action potential)**, **GO:0050804 (modulation of synaptic transmission)**, and **GO:0060078 (regulation of postsynaptic membrane potential)** capture these processes.

### 6.3 Cellular Processes and Neurodevelopmental Consequences

At the cellular level, altered AMPA receptor function impacts multiple processes critical for brain development and function, including neuronal differentiation, migration, synaptogenesis, synaptic pruning, and plasticity. During embryonic and early postnatal development, glutamatergic transmission guides neuronal migration and synapse formation, and activity‑dependent mechanisms refine cortical and subcortical circuits.[11][12] Disruption of AMPA currents due to mutant GRIA4 may impair these processes, leading to maldevelopment of cortical layers, abnormal dendritic arborization, and altered synaptic density.

Moreover, excitatory–inhibitory balance is crucial for preventing pathological network states such as epileptiform activity or hypoactive states. If mutant GRIA4 causes excessive excitatory drive, cortical and thalamocortical circuits may exhibit spontaneous synchronized discharges, manifesting as seizures and spike–wave patterns, as seen in Gria4‑deficient mice.[2][9] Conversely, if certain variants reduce excitatory drive in specific circuits, they might impair activity‑dependent synaptic stabilization, leading to cognitive deficits and motor dysfunction. These dual possibilities underscore that different GRIA4 variants may have somewhat distinct functional profiles, though all converge clinically on global developmental delay and tone abnormalities.

Relevant GO biological process terms include **GO:0007399 (nervous system development)**, **GO:0022038 (neurogenesis)**, **GO:0048666 (neuron development)**, **GO:0050808 (synapse organization)**, and **GO:0007215 (glutamate receptor signaling pathway)**. The principal cell types involved are cortical pyramidal neurons (CL:0002604), cerebellar Purkinje neurons (CL:0000121), hippocampal CA1 pyramidal neurons (CL:0000107), and possibly retinal ganglion and bipolar cells (CL terms corresponding to retinal neurons), though specific cell ontology mappings remain inferred.

### 6.4 Metabolic and Ion Homeostasis Changes

While NEDSGA is not a primary metabolic disorder, AMPA receptor dysfunction can indirectly alter neuronal metabolism and ion homeostasis. Abnormal Na\(^+\) and Ca\(^{2+}\) flux through mutant AMPA channels may perturb intracellular Ca\(^{2+}\) signaling, mitochondrial function, and ATP consumption, contributing to oxidative stress and vulnerability to excitotoxicity.[11] Excessive Ca\(^{2+}\) influx can activate calpains and other proteases, leading to cytoskeletal damage and neuronal death, particularly under conditions of ischemia or intense synaptic activity. Conversely, reduced Ca\(^{2+}\) signaling may impair calcium‑dependent gene expression and synaptic plasticity.

At the network level, chronic excitatory imbalance may alter cerebral blood flow and glucose metabolism, which could contribute to cortical atrophy observed on MRI in some NEDSGA patients.[4][16][18] However, no direct metabolomics or energy metabolism studies in NEDSGA have been reported, and these metabolic changes remain hypothetical. HMDB and other metabolomics databases do not list specific signatures for GRIA4 mutation at present.

### 6.5 Immune System and Tissue Damage Mechanisms

There is no evidence that NEDSGA involves primary immune dysregulation or autoimmunity. However, secondary tissue damage mechanisms such as excitotoxicity and oxidative stress, driven by abnormal glutamatergic transmission, could trigger local inflammatory responses in the brain. Microglial activation and astrocytic gliosis often accompany chronic seizures and neurodegeneration, and they may be present in NEDSGA, although neuropathological data are lacking.[11][12][18] Tissue damage mechanisms such as apoptosis, necrosis, and synaptic pruning could be altered, but these remain speculative.

Epileptic activity itself can injure developing brain structures, and repeated seizures might exacerbate cortical atrophy seen on MRI. Likewise, spasticity and joint contractures can cause musculoskeletal damage through chronic abnormal loading and reduced mobility, leading to fibrosis and pain. These secondary processes contribute to the long‑term disability burden in NEDSGA.

### 6.6 Visual System Involvement

The ocular and visual phenotypes of NEDSGA suggest involvement of retinal and optic nerve development, which may reflect GRIA4 expression in these structures or indirect cortical effects. Glutamate is the primary excitatory neurotransmitter in the retina, and AMPA receptors are expressed on multiple retinal neuron types, including bipolar and ganglion cells.[14][18] Mutant GRIA4 could impair synaptic transmission in retinal circuits, leading to retinal hypoplasia, chorioretinal hyperpigmentation, and optic nerve hypoplasia. Alternatively, cortical visual impairment due to occipital lobe dysfunction could contribute to nystagmus and strabismus by disrupting visual tracking and ocular motor control.

Relevant anatomical ontology terms include **UBERON:0000955 (eye)**, **UBERON:0001782 (retina)**, **UBERON:0000956 (optic nerve)**, and **UBERON:0001811 (visual cortex)**. Visual system involvement underscores the need for comprehensive neuro‑ophthalmologic assessment in NEDSGA.

### 6.7 Summary of Mechanistic Ontologies

Taken together, the mechanistic cascade in NEDSGA can be annotated with:

- Biological processes: nervous system development (GO:0007399), synaptic transmission (GO:0007268), glutamate receptor signaling (GO:0007215), regulation of membrane potential (GO:0042391), neuron differentiation (GO:0030182).

- Cellular components: AMPA receptor complex (GO:0005891), postsynaptic density (GO:0014069), neuron projection (GO:0098984), synapse (GO:0045202).

- Cell types: cortical pyramidal neuron (CL:0002604), cerebellar Purkinje cell (CL:0000121), retinal bipolar neuron (CL:0000743), retinal ganglion cell (CL:0000740).

- Pathological processes: channelopathy (conceptual), epileptogenesis, spasticity, cortical atrophy.

Most mechanistic details remain inferred from receptor biology and animal models, highlighting a need for direct functional studies of mutant GRIA4 in human neurons.

## 7. Anatomical Structures Affected

### 7.1 Central Nervous System: Brain and Spinal Cord

The primary anatomical system affected in NEDSGA is the central nervous system (CNS), including cerebral cortex, corpus callosum, cerebellum, and corticospinal tracts. Neuroimaging in several cases has shown cortical atrophy and thinning of the corpus callosum, consistent with diffuse developmental brain malformation or progressive loss of cortical volume.[4][16][18] These findings can be annotated with **UBERON:0000956 (cerebral cortex)**, **UBERON:0002338 (corpus callosum)**, and HPO terms HP:0002120 (Cerebral cortical atrophy) and HP:0002079 (Thin corpus callosum).[4][16]

Clinically, global developmental delay, intellectual disability, seizures, and tone abnormalities reflect dysfunction of multiple CNS regions. The motor cortex and corticospinal tracts are primarily responsible for spasticity and impaired gait, while cerebellar involvement could contribute to clumsiness and coordination problems. Cognitive and language deficits suggest frontal, temporal, and associative cortical involvement; epilepsy points to cortical and thalamocortical circuits; and visual disturbances may involve occipital cortex and visual pathways.[11][12][14][18] Although spinal cord involvement has not been specifically documented, corticospinal tract degeneration or dysfunction is inferred from spasticity and hyperreflexia.

### 7.2 Peripheral Nervous System and Musculoskeletal System

Peripheral nervous system involvement is less clearly defined in NEDSGA, but neuromuscular manifestations such as spasticity, joint contractures, and choreiform movements reflect interplay between central and peripheral systems. Muscle tone abnormalities and contractures primarily arise from upper motor neuron dysfunction, but chronic disuse and altered neuromuscular signaling can lead to changes in muscle fibers, tendons, and joints. Orthopedic deformities and pain may develop over time, affecting the musculoskeletal system.

The musculoskeletal structures involved include **UBERON:0001465 (muscle organ)**, **UBERON:0001450 (joint)**, and various limb skeletal elements. Joint contractures and spasticity can be mapped to these structures and associated HPO terms. Physical therapy and orthopedic care target these tissues to maintain mobility and prevent further damage.

### 7.3 Visual System: Eye, Retina, Optic Nerve, and Oculomotor Apparatus

As discussed, the visual system is significantly affected in NEDSGA. Nystagmus and strabismus involve extraocular muscles and oculomotor nuclei, while retinal hypoplasia and chorioretinal hyperpigmentation involve the retina and choroid.[4][13][14][18] Optic nerve hypoplasia reflects developmental undergrowth or atrophy of retinal ganglion cell axons projecting to the brain.[4][18] Anatomical ontology terms include **UBERON:0000955 (eye)**, **UBERON:0001782 (retina)**, **UBERON:0000956 (optic nerve)**, and **UBERON:0001623 (extraocular skeletal muscle)**.

Visual cortex involvement may contribute to cortical visual impairment, though specific imaging correlates have not been reported. Combined ocular and central visual system involvement underscores the complexity of visual dysfunction in NEDSGA and the need for multidisciplinary evaluation.

### 7.4 Cardiovascular System

Cardiovascular involvement has been described in at least one NEDSGA proband, who had tricuspid regurgitation and a patent foramen ovale on echocardiography.[14][18] These anomalies involve the **UBERON:0002084 (heart)**, specifically the **UBERON:0002090 (tricuspid valve)** and **UBERON:0002099 (foramen ovale)**. Whether these cardiac findings represent coincidental anomalies or part of a broader GRIA4‑associated developmental pattern is unclear, given the small sample size and lack of recurrent cardiac features in other cases.[11][12][16] Nonetheless, their presence warrants cardiovascular assessment in NEDSGA, especially in infants with murmurs or other signs.

### 7.5 Gastrointestinal and Feeding Structures

Feeding difficulties in NEDSGA may arise from oropharyngeal dysphagia, poor suck, gastroesophageal reflux, or central feeding regulation abnormalities.[4][13][18] The anatomical structures involved include the **UBERON:0001043 (tongue)**, **UBERON:0001041 (pharynx)**, **UBERON:0000945 (esophagus)**, and **UBERON:0001045 (stomach)**. Central regulation of feeding involves hypothalamus and brainstem nuclei. While specific structural abnormalities in these organs have not been reported, functional impairments necessitate clinical attention.

### 7.6 Subcellular Localization

At the subcellular level, GluA4‑containing AMPA receptors reside primarily in the **plasma membrane** of dendritic spines at postsynaptic sites, corresponding to GO:0005886 (plasma membrane) and GO:0045202 (synapse).[2][11] Mutant receptors would alter ion flux across this membrane and potentially affect downstream signaling organelles, including mitochondria (GO:0005739), endoplasmic reticulum (GO:0005783), and nucleus (GO:0005634), through Ca\(^{2+}\)‑dependent pathways. While specific subcellular imaging of NEDSGA neurons has not been reported, the standard localization of AMPA receptors provides a basis for mechanistic annotations.

### 7.7 Lateralization and Symmetry

NEDSGA phenotypes appear generally bilateral and symmetric, consistent with a diffuse genetic lesion affecting global brain development rather than focal vascular or structural anomalies. Spasticity and contractures often involve both lower limbs, though severity may differ somewhat between sides. Nystagmus and strabismus affect both eyes; cortical atrophy and corpus callosum thinning are midline or bilateral.[4][11][16][18] No clear evidence of lateralized deficits such as hemiparesis or focal cortical dysplasia has been reported, though focal seizures may arise from localized cortical networks within a globally abnormal brain.

## 8. Temporal Development

### 8.1 Age of Onset and Early Course

NEDSGA is an **early‑onset** neurodevelopmental disorder, with manifestations detectable from the neonatal period or early infancy. OMIM emphasizes that global developmental delay is apparent from infancy or early childhood, and most affected individuals show irritability, stiffness, and hypertonia early in life.[1][16] Eyes.arizona.edu describes several neonates with irritability, hypertonia, increased startle reflexes, and stiffness, with occasional hypotonia in the neonatal period.[4][13] The Chinese proband was diagnosed in infancy, with severe developmental delay and seizures emerging within the first months of life.[14][18]

Thus, typical age of onset for developmental and tone abnormalities is neonatal to early infancy (0–6 months), while seizures may emerge later in infancy or childhood but still within the first few years.[11][14][18] Ocular abnormalities such as nystagmus and strabismus often become evident in the first months when visual tracking would normally develop.[4][13] The onset pattern is insidious rather than acute: developmental milestones are simply delayed or absent, and tone abnormalities gradually intensify.

### 8.2 Disease Progression and Course Patterns

The progression of NEDSGA appears **chronic and progressive** in some domains and relatively stable in others. Hypertonia and spasticity tend to worsen over time, leading to joint contractures and increasingly impaired gait.[4][11][16][18] Intellectual disability and developmental delay remain present throughout childhood and into adulthood, with little evidence of spontaneous catch‑up; however, some patients achieve limited progress with supportive therapies, reflecting a slow developmental trajectory rather than complete stagnation.[11][12][17] Seizure frequency and severity may fluctuate with age and treatment, but epilepsy often persists as a long‑term comorbidity.[11][14][18]

Neuroimaging findings such as cortical atrophy and thin corpus callosum might represent static anomalies or progressive changes; longitudinal imaging data are scarce, but the combination of developmental malformation and possible ongoing seizure‑related injury suggests a mixed pattern. Ocular abnormalities appear relatively stable after initial development, although retinal hypoplasia and optic nerve hypoplasia are structural defects unlikely to progress significantly.

Overall, NEDSGA can be conceptualized as a lifelong neurodevelopmental disorder with **early onset, chronic course, and variable progression**, rather than an episodic or remitting condition. Disease duration is essentially lifelong, from birth through adulthood, with functional disability persisting throughout.

### 8.3 Critical Periods and Windows for Intervention

Critical periods in NEDSGA likely correspond to general windows of brain and motor development. Early infancy (0–2 years) is a critical period for establishing basic motor skills, language, and social attachment; in NEDSGA, this period is marked by severe developmental delay, tone abnormalities, and emergence of seizures.[11][14][18] Early, intensive intervention with physical, occupational, and speech therapy may maximize developmental potential, even if it does not normalize trajectories. Likewise, early seizure control is crucial to prevent further cognitive impairment and minimize excitotoxic injury.

Another critical period pertains to musculoskeletal development: as spasticity and hypertonia persist into preschool and school years, joint contractures and deformities may develop, which could be mitigated by early physical therapy, orthotic support, and, if needed, surgical interventions. Feeding difficulties and nutritional status in infancy and early childhood also represent a critical window, as failure to thrive and recurrent aspiration can worsen overall health outcomes.

There is no evidence of spontaneous remission or major age‑dependent improvement in NEDSGA; rather, the focus should be on early detection and sustained supportive intervention during sensitive developmental windows.

## 9. Inheritance and Population

### 9.1 Inheritance Pattern, Penetrance, and Expressivity

NEDSGA is inherited in an **autosomal dominant** manner, as explicitly stated by OMIM, Monarch Initiative, and ClinGen.[5][9][16] However, nearly all reported cases involve **de novo** variants, with unaffected parents and no familial transmission.[11][14][16][18] This pattern suggests high penetrance and severe phenotypic consequences such that carriers are unlikely to reproduce or are rare in the population.

Penetrance appears to be **complete or near‑complete**, given that individuals with documented pathogenic GRIA4 variants all manifest neurodevelopmental abnormalities consistent with NEDSGA.[9][11][14][18] Incomplete penetrance has not been described, though the small number of cases limits definitive conclusions. Expressivity, by contrast, is **variable**: intellectual disability ranges from profound to mild; seizures are present in most but not all individuals; gait impairment spans non‑ambulatory to clumsy, spastic walking; and ocular and cardiac anomalies are not universal.[1][4][11][14][16][18] This variable expressivity reflects differences in variant type, genetic background, environmental influences, and access to care.

There is no evidence of **genetic anticipation**, as NEDSGA is not a repeat expansion disorder and familial generational data are lacking. **Germline mosaicism** in parents remains a theoretical possibility, as it is in many de novo dominant disorders, but has not been documented by recurrence in siblings. Counseling should nonetheless consider a small recurrence risk due to potential parental gonadal mosaicism.

### 9.2 Epidemiology: Prevalence and Incidence

NEDSGA is exceedingly rare, with only a handful of cases reported in the literature. Martin et al. described five unrelated probands from Germany, Denmark, and the United States in 2017.[11][12][17][19] The Frontiers in Genetics article from 2022 identified an additional proband from China, noting that this was the first NEDSGA case reported in that country.[14][18] ClinGen’s 2024 curation mentions ten probands across five publications (PMIDs 27479843, 29220673, 35518358, 37921875, 38819422), suggesting that further cases have been reported since 2017.[9]

Given this small number and the lack of population‑based registries, precise prevalence and incidence estimates are not available. NEDSGA can be considered an **ultra‑rare** disorder, likely with prevalence well below 1 per 1,000,000 individuals. Incidence would correspond to the rate of de novo GRIA4 pathogenic variants in live births, also expected to be extremely low. However, improved access to exome and genome sequencing in neurodevelopmental cohorts may reveal additional cases, gradually refining epidemiological estimates.

### 9.3 Population Demographics, Geographic Distribution, and Sex Ratio

Reported NEDSGA probands come from diverse geographic and ethnic backgrounds. Martin et al.’s cohort included individuals from Germany, Denmark, and the United States, presumably of European and North American descent.[11][12][17][19] The 2022 case report described a female infant from China.[14][18] ClinGen’s mention of additional publications suggests further geographical spread, but specific locations are not detailed.[9] This wide distribution implies that NEDSGA is not confined to particular populations or founder mutations; rather, de novo GRIA4 variants arise sporadically across populations.

Sex ratio data are limited but suggest that NEDSGA affects both males and females, with no clear sex bias. Martin et al.’s probands include both sexes, and the Chinese case is female.[11][14][18] Given autosomal inheritance and no apparent sex‑linked mechanisms, equal sex distribution would be expected.

There is no evidence of **founder effects** or population‑specific recurrent mutations; each reported variant is unique and de novo. Consanguinity plays no role in NEDSGA, as it is a dominant rather than recessive disorder. Carrier frequency of pathogenic GRIA4 variants in the general population appears negligible, consistent with their absence from gnomAD and other large datasets.[7][10][18]

## 10. Diagnostics

### 10.1 Clinical Evaluation and Neuroimaging

Diagnostic evaluation of NEDSGA begins with recognition of its characteristic clinical features: early‑onset global developmental delay, tone abnormalities (hypertonia progressing to spasticity), impaired or absent ambulation, seizures in many but not all cases, and dysmorphic features such as large ears.[1][4][11][16][18] Neurological examination often reveals hyperreflexia, increased tone, clonus, and motor deficits consistent with upper motor neuron lesions. Ophthalmologic evaluation may identify nystagmus, strabismus, optic nerve hypoplasia, and retinal hypoplasia.[4][13][18]

Brain MRI is a key diagnostic tool, typically demonstrating cortical atrophy and thinning of the corpus callosum in some NEDSGA patients.[4][16][18] These imaging findings, while not pathognomonic, support a diagnosis of diffuse neurodevelopmental disorder. EEG evaluation is recommended to characterize seizures and may reveal generalized or focal epileptiform discharges, including patterns reminiscent of absence epilepsy.[2][9][11] Standard laboratory tests (blood counts, metabolic panels, lactate, ammonia, thyroid function) are usually unremarkable, helping rule out metabolic or metabolic encephalopathies.

### 10.2 Genetic Testing Strategies

Given the genetic etiology of NEDSGA, **genetic testing** is essential for definitive diagnosis. Trio whole‑exome sequencing (WES) has been the primary method used in published cases, enabling detection of de novo heterozygous GRIA4 missense variants in probands with complex neurodevelopmental phenotypes.[11][12][14][18][19] WES is particularly useful in infants and children with unexplained global developmental delay, seizures, and spasticity, as it simultaneously evaluates thousands of genes involved in neurodevelopment.

Single‑gene testing for GRIA4 may be considered once NEDSGA is suspected, but given the rarity of the disorder and overlap with other AMPA receptor–related diseases, broader gene panels or exome/genome approaches are more efficient. Epilepsy gene panels and neurodevelopmental panels often include GRIA4 alongside GRIA1–3 and other synaptic genes, enabling targeted but comprehensive analysis. ClinVar and GTR list GRIA4‑related tests, though specific panel compositions vary by laboratory.[6][7][10]

Chromosomal microarray (CMA), karyotyping, FISH, and mitochondrial DNA testing have limited utility for NEDSGA, as pathogenic lesions are single‑gene missense variants rather than structural rearrangements or mitochondrial mutations.[2][16] However, CMA may reveal additional copy number changes that modify phenotype or identify alternative diagnoses in individuals without GRIA4 variants.

Whole‑genome sequencing (WGS) could, in principle, detect non‑coding regulatory variants in GRIA4, structural changes, or intronic splice mutations not captured by WES, but no such variants have been implicated in NEDSGA to date. Nonetheless, WGS remains valuable in research settings for comprehensive genomic profiling of neurodevelopmental cohorts.

### 10.3 Omics‑Based and Biomarker Diagnostics

Beyond sequence‑level diagnostics, no validated biomarkers for NEDSGA are currently available. Proteomics, metabolomics, and transcriptomics have not identified specific signatures attributable to GRIA4 mutation in humans. However, future RNA‑seq studies in patient‑derived neurons might reveal transcriptomic patterns useful for mechanistic insights or potential biomarkers.

Functional imaging modalities, such as PET or fMRI, could theoretically demonstrate altered cortical metabolism or connectivity in NEDSGA, but they have not been applied systematically. Likewise, liquid biopsy approaches (e.g., circulating microRNAs or exosomal markers) are unexplored.

Given this landscape, the primary diagnostic biomarker for NEDSGA remains the presence of a heterozygous pathogenic GRIA4 missense variant, detected by DNA sequencing.

### 10.4 Clinical Criteria and Differential Diagnosis

There are no formal standardized diagnostic criteria, such as DSM or ICD‑11 algorithms, specifically for NEDSGA. Diagnosis rests on the combination of clinical phenotype, neuroimaging and EEG findings, and genetic confirmation of a pathogenic GRIA4 variant. ICD‑10 and ICD‑11 codes used will likely be generic, such as F84 (pervasive developmental disorders), F70–F79 (intellectual disability), G40 (epilepsy), and G80 (cerebral palsy), with more specific coding possible as disease awareness grows.

Differential diagnosis includes a broad range of early‑onset neurodevelopmental and epileptic disorders, such as:

- Cerebral palsy due to hypoxic‑ischemic injury, which can present with spasticity and motor delay but typically has perinatal risk factors and lacks a specific genetic lesion.

- Other AMPA receptor–related disorders caused by mutations in GRIA1, GRIA2, GRIA3, or GRIN genes, which share intellectual disability and epilepsy but may have distinct phenotypic features or imaging patterns.[11][12][16]

- Hereditary spastic paraplegias and leukodystrophies, which present with spastic gait and white matter abnormalities, but differ in onset (often later) and genetic etiology.

- Metabolic encephalopathies, which can produce global developmental delay and seizures, but often have metabolic markers (elevated lactate, ammonia, specific metabolite patterns) and may respond to dietary or metabolic treatments.

- Mitochondrial disorders, which combine neurodevelopmental and systemic features but show characteristic imaging and biochemical signatures.

In practice, the identification of a de novo GRIA4 missense variant in a child with the NEDSGA phenotype usually provides sufficient specificity to distinguish NEDSGA from these differential diagnoses.

### 10.5 Screening

There are currently no population‑based screening programs for NEDSGA, given its ultra‑rare nature and the complexity of genetic testing. Newborn screening panels do not include GRIA4 or NEDSGA. Carrier screening is not relevant, as pathogenic variants are typically de novo and carriers are severely affected. **Cascade screening** of family members may be considered when a pathogenic GRIA4 variant is identified, but given the de novo origin, parents and siblings are usually negative.

Prospective screening within neurodevelopmental and epilepsy clinics using exome or genome sequencing may identify NEDSGA cases earlier, enabling prompt supportive interventions. Preimplantation genetic testing (PGT) and prenatal diagnosis are options in families with known GRIA4 variants and reproductive planning, but these scenarios are rare due to the de novo pattern.

## 11. Outcome and Prognosis

### 11.1 Survival and Mortality

Data on survival and mortality in NEDSGA are limited, as most reported probands are children and young adults, and no systematic mortality analyses have been performed. Martin et al.’s cohort included individuals up to 21 years of age, suggesting that survival into adulthood is possible.[11][12][17][19] None of the publications report early deaths attributable directly to NEDSGA, though long‑term follow‑up is lacking.

Given the combination of severe intellectual disability, spasticity, and seizures, life expectancy may be modestly reduced compared to the general population, particularly in cases with severe epilepsy or feeding difficulties. However, with appropriate supportive care, including seizure control, nutritional support, and management of comorbidities, many individuals may live into adulthood. Disease‑specific mortality data (e.g., deaths from status epilepticus, aspiration pneumonia, or infections) are not available and represent an area for future natural history research.

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity in NEDSGA is substantial, encompassing cognitive, motor, visual, and systemic dimensions. Intellectual disability and global developmental delay limit educational attainment, employment, and independent living. Spasticity, impaired gait, and contractures reduce mobility and increase risk of falls and pain. Seizures impose ongoing risk and psychological stress. Ocular anomalies impair vision and further restrict environmental engagement. Feeding difficulties and sleep problems add to the burden.[1][4][11][14][16][18]

From a disability classification perspective, NEDSGA impacts domains from the International Classification of Functioning (ICF), including body functions (mental, neuromusculoskeletal), activities (walking, self‑care, communication), and participation (social, educational). Most individuals will require long‑term support services and may be classified as having severe developmental and intellectual disability.

Formal quality of life assessments (e.g., EQ‑5D, SF‑36, PROMIS) have not been reported in NEDSGA, but extrapolation from similar disorders suggests low scores in mobility, self‑care, usual activities, and anxiety/depression domains. Caregiver burden is likely high, and psychosocial support is essential.

### 11.3 Disease Course, Complications, and Recovery Potential

The disease course in NEDSGA is chronic, with major complications including epilepsy‑related injuries, orthopedic problems (contractures, scoliosis), malnutrition, aspiration, and infections. Without effective management, these complications can further reduce functional capacity and increase morbidity. Recovery potential in the sense of returning to normal function is low, but developmental gains are possible with intensive therapy and environmental support, particularly in individuals with milder intellectual disability.[11][12][17]

Prognostic factors may include variant type and location (e.g., certain SYTANLAAF mutations vs others), seizure severity, access to specialized pediatric neurology and rehabilitation services, and comorbid health conditions. However, the small number of cases precludes robust prognostic modeling. In general, early diagnosis, seizure control, nutritional optimization, and physical therapy are expected to improve functional outcomes, even if they do not fully reverse deficits.

## 12. Treatment

### 12.1 Pharmacotherapy

There is no disease‑specific pharmacological treatment for NEDSGA targeting GRIA4 or AMPA receptors directly. Management currently focuses on **symptomatic pharmacotherapy**, particularly for seizures and spasticity. Standard antiepileptic drugs (AEDs), such as valproate, levetiracetam, topiramate, or lamotrigine, may be used based on seizure type, side effect profiles, and comorbidities.[11][14][18] No comparative trials exist in NEDSGA, and AED selection follows general pediatric epilepsy guidelines.

Spasticity may be managed with oral medications such as baclofen, tizanidine, or diazepam, and, in severe cases, intrathecal baclofen pumps or botulinum toxin injections. These agents modulate GABAergic tone and muscle spindling, providing partial relief of spasticity. Pain and sleep disturbances can be addressed with analgesics and sedative medications as needed, balancing efficacy with side effects.

Pharmacogenomics specific to GRIA4 and AEDs has not been studied, but general pharmacogenetic principles apply, such as screening for HLA‑B*1502 before carbamazepine in certain populations to avoid Stevens–Johnson syndrome. NCIt terms applicable to these interventions include **NCIT:C772 (Anticonvulsant agent)** and **NCIT:C2315 (Muscle relaxant)**.

### 12.2 Advanced Therapeutics and Future Directions

Given the molecular mechanism involving AMPA receptor dysfunction, **targeted therapies** modulating glutamatergic transmission represent a theoretical avenue. AMPA receptor antagonists, such as perampanel, are used in epilepsy and could potentially reduce excitotoxicity or hyperexcitability in NEDSGA, but their impact on development and cognition would need careful evaluation. No clinical trials of perampanel or other AMPA modulators in NEDSGA have been reported to date.

Gene‑specific therapies, including gene editing (CRISPR), RNA‑based approaches (antisense oligonucleotides), or gene replacement, remain speculative. Challenges include delivering therapeutics across the blood–brain barrier, timing interventions during development, and avoiding off‑target effects. Nonetheless, progress in gene therapy for other neurodevelopmental disorders suggests that GRIA4‑targeted strategies may be possible in the long term.

Cell therapies, such as stem cell transplantation, are unlikely to directly address synaptic receptor defects but may support general neural repair. Immunotherapies are not relevant, as NEDSGA is not autoimmune.

### 12.3 Surgical and Interventional Treatments

Surgical interventions in NEDSGA are largely supportive, addressing orthopedic and feeding complications rather than the underlying brain pathology. Orthopedic surgeries may include tendon releases, osteotomies, or spinal fusion to relieve contractures and correct deformities. Gastrostomy tube placement may be needed for severe feeding difficulties and failure to thrive. Cardiac surgery could be indicated for significant tricuspid regurgitation or large patent foramen ovale, though these have only been reported in a single case.[14][18]

Neurosurgical interventions for epilepsy, such as resective surgery or neuromodulation (vagus nerve stimulation, deep brain stimulation), may not be applicable, given the diffuse nature of cortical dysfunction in NEDSGA. Nonetheless, refractory focal seizures might prompt consideration of invasive evaluation.

### 12.4 Supportive and Rehabilitative Care

Supportive care is the mainstay of NEDSGA management. Multidisciplinary rehabilitation—including physical therapy, occupational therapy, speech and language therapy, and visual rehabilitation—is essential to maximize functional abilities, prevent contractures, and support communication.[11][12][18] Assistive devices such as walkers, wheelchairs, orthoses, communication boards, and adaptive seating improve mobility and participation. Nutritional support, including specialized diets and feeding strategies, ensures adequate growth and reduces aspiration risk.

Psychosocial support for families, including counseling, respite care, and educational resources, is crucial given the chronic caregiving burden. NCIt terms relevant to these interventions include **NCIT:C15624 (Supportive care)** and **NCIT:C15336 (Physical therapy)**.

### 12.5 Experimental Treatments and Clinical Trials

As of the latest evidence, no registered clinical trials specifically target NEDSGA or GRIA4‑related neurodevelopmental disorders. Experimental treatments would likely be small, investigator‑initiated studies in broader neurodevelopmental or epileptic cohorts. Future trials might explore AMPA modulators, neuroprotective agents, or gene‑based therapies.

Treatment response rates and adverse event profiles in NEDSGA have not been systematically quantified due to the small number of cases. Management thus follows individualized clinical judgment with close monitoring.

### 12.6 Treatment Strategy and Personalized Medicine

Given the heterogeneity in NEDSGA phenotype, treatment strategies should be personalized, integrating genotype, seizure profile, motor and visual status, and family priorities. A typical pathway might involve:

- Early genetic diagnosis via exome sequencing.

- Prompt initiation of AEDs tailored to seizure type and frequency.

- Aggressive physical and occupational therapy to address spasticity and motor delay.

- Ophthalmologic evaluation and visual rehabilitation.

- Regular orthopedic and nutritional assessments.

Personalized medicine approaches may eventually consider specific GRIA4 variant effects when selecting AMPA modulators or other therapies, but data are currently insufficient for such genotype‑guided decisions.

## 13. Prevention

### 13.1 Primary, Secondary, and Tertiary Prevention

Primary prevention of NEDSGA is challenging, as pathogenic GRIA4 variants are de novo and not predictable by parental genotype or modifiable environmental exposures. General preconception and prenatal health measures, such as folate supplementation, avoidance of toxins, and infection control, are recommended but do not specifically prevent GRIA4 mutations.

Secondary prevention involves **early detection** and intervention to mitigate the effects of NEDSGA once present. Early recognition of developmental delay, tone abnormalities, and seizures, followed by prompt genetic testing, enables earlier diagnostic confirmation and initiation of supportive care. While this does not prevent disease, it may reduce complications and improve developmental outcomes.

Tertiary prevention focuses on preventing **complications and disability** in individuals already affected. This includes seizure control, contracture management, nutritional and respiratory support, and psychosocial interventions, as detailed in the treatment section. These measures aim to limit secondary morbidity and optimize quality of life.

### 13.2 Genetic Counseling and Reproductive Options

Genetic counseling is a critical preventive and educational tool in NEDSGA. Counselors should explain the de novo nature of pathogenic GRIA4 variants, the low recurrence risk, and the possibility (though small) of parental germline mosaicism.[11][14][16][18] For affected individuals reaching reproductive age, counseling on reproductive risks and options is important, though many may be unable to parent due to cognitive and physical disabilities.

In families with known GRIA4 variants, reproductive options include prenatal diagnosis via chorionic villus sampling or amniocentesis, and preimplantation genetic testing (PGT) in the context of assisted reproduction. These interventions allow informed decisions about pregnancy continuation or embryo selection, representing primary prevention at the family level.

### 13.3 Public Health and Environmental Interventions

Given the genetic nature of NEDSGA, public health interventions such as sanitation, vector control, and environmental cleanup do not specifically prevent the disorder. However, broader policies that improve access to genetic diagnostics, rehabilitation services, and inclusive education can reduce the impact of NEDSGA and similar disorders on individuals and families.

Preventive medications or prophylactic procedures (e.g., prophylactic AEDs) are not used to prevent NEDSGA onset but may prevent seizures once disease is present. Vaccinations and infection control measures are important to reduce triggers for seizures and complications.

## 14. Other Species and Natural Disease

### 14.1 Species and Orthologous Genes

The GRIA4 gene is conserved across vertebrates, with orthologs present in mouse (**Gria4**), rat, zebrafish, and other species, as catalogued in NCBI Gene and HomoloGene.[2][9] These orthologs encode AMPA receptor subunits analogous to human GluA4, playing similar roles in excitatory neurotransmission and synaptic plasticity. In mice, Gria4 expression is prominent in cortical and cerebellar neurons, and Gria4‑deficient models have been extensively studied in epilepsy research.[2][9]

Taxonomic identifiers include **NCBI Taxon:9606 (Homo sapiens)** for humans and **NCBI Taxon:10090 (Mus musculus)** for mice. Orthologous gene IDs for Gria4 in mouse and other species can be linked in gene ontology resources to support comparative analysis.

### 14.2 Natural Disease in Animals and Veterinary Relevance

There are no reports of a naturally occurring animal disease precisely analogous to human NEDSGA caused by GRIA4 mutation in companion animals or livestock. Veterinary databases such as OMIA (Online Mendelian Inheritance in Animals) do not list GRIA4‑related neurodevelopmental disorders in dogs, cats, or other species as of current knowledge. However, experimental Gria4 mutant mice exhibit absence‑like epilepsy and behavioral arrest, modeling aspects of human epileptic phenotypes.[2][9]

Veterinary relevance of GRIA4 centers on experimental models rather than spontaneous disease. Insights from mouse Gria4 deficiency inform understanding of seizure mechanisms and potential drug targets, but do not yet translate into animal clinical practice.

### 14.3 Comparative Pathology and Evolutionary Conservation

Comparative pathology across species highlights the conserved role of AMPA receptors in excitatory neurotransmission and epileptogenesis. Mouse Gria4‑deficient models show high‑frequency spike–wave discharges and behavioral arrest, closely resembling human absence seizures.[2][9] This suggests evolutionary conservation of thalamocortical circuitry and its vulnerability to AMPA receptor perturbations. However, the human NEDSGA phenotype includes additional features, such as global developmental delay, spasticity, and ocular anomalies, not fully captured in mouse models.

Mechanistic conservation is reflected in shared GO terms and pathway annotations across species, including glutamatergic synapse signaling and synaptic plasticity. This supports the use of animal models for preclinical testing of potential therapies targeting AMPA receptors.

### 14.4 Transmission and Zoonotic Potential

NEDSGA is a non‑infectious, non‑transmissible genetic disorder with no zoonotic potential. There is no cross‑species transmission of GRIA4 mutations; each case arises from independent genetic events in individual organisms.

## 15. Model Organisms

### 15.1 Gria4‑Deficient Mouse Models

Mouse models with reduced or absent Gria4 expression provide important insights into the pathophysiology of GRIA4‑related disorders. OMIM’s GRIA4 entry notes that genetic deficiency of Gria4, either by reduction or complete lack, is associated with high‑frequency spike–wave discharges and behavioral arrest, modeling absence epilepsy.[2] These mice exhibit spontaneous, generalized, non‑convulsive seizures with EEG patterns of spike–wave complexes, akin to human absence seizures, and respond to antiepileptic drugs used in absence epilepsy.

Phenotypically, Gria4‑deficient mice recapitulate the **epileptic** aspects of NEDSGA but not the full neurodevelopmental phenotype. They may show subtle behavioral and cognitive changes, but global developmental delay, spasticity, and ocular anomalies are not prominent in these models. This suggests that human NEDSGA arises from more complex or variant‑specific functional changes than pure loss of Gria4, consistent with the dominant functional effects inferred from missense variants.[11][12][16]

### 15.2 Model Characteristics and Limitations

Gria4 mouse models offer several advantages: genetic manipulation is well‑controlled; EEG and behavioral phenotyping are feasible; and they provide a platform for testing antiepileptic and AMPA‑modulating therapies. They are particularly useful for studying thalamocortical circuits and seizure mechanisms. However, limitations include species differences in brain development and behavior, incomplete replication of human neurodevelopmental phenotypes, and the fact that human NEDSGA variants may cause gain‑of‑function or altered gating rather than loss‑of‑function.

Other model systems, such as zebrafish or organoids, have not yet been widely used for GRIA4, but could potentially model aspects of synaptic development and ocular phenotypes. Human iPSC‑derived neurons with CRISPR‑engineered GRIA4 mutations would offer an ideal platform for mechanistic and therapeutic studies, though such models remain to be developed.

### 15.3 Research Applications

Model organisms enable detailed investigation of:

- How GRIA4 loss or mutation affects synaptic currents and network dynamics.

- The relationship between AMPA receptor dysfunction and spike–wave discharges in absence epilepsy.

- The impact of AMPA modulators and other AEDs on seizure frequency and network excitability.

- Potential compensatory mechanisms involving other AMPA subunits or synaptic pathways.

Data from these models inform hypotheses about human NEDSGA, though translation must be cautious given phenotypic differences.

## Conclusion

Neurodevelopmental disorder with or without seizures and gait abnormalities (NEDSGA) is an ultra‑rare, early‑onset Mendelian encephalopathy caused by heterozygous missense variants in the **GRIA4** gene, encoding the GluA4 subunit of AMPA‑type glutamate receptors.[2][11][16] Clinically, it manifests as global developmental delay, variable intellectual disability, early hypertonia evolving into spasticity and impaired gait, and seizures of diverse types, often accompanied by cortical atrophy, thin corpus callosum, ocular anomalies (nystagmus, strabismus, optic nerve and retinal hypoplasia), and dysmorphic features such as macrotia and joint contractures.[1][4][11][14][16][18] All convincingly pathogenic variants reported to date are de novo missense changes clustered in transmembrane and ligand‑binding domains, particularly the SYTANLAAF gating motif, and are predicted to exert dominant functional effects on AMPA receptor gating and permeability.[11][12][16][18]

Mechanistically, NEDSGA reflects a channelopathy of excitatory synaptic transmission: mutant GluA4 perturbs AMPA receptor function, disrupting excitatory–inhibitory balance, synaptic plasticity, and network development, leading to intellectual disability, spasticity, and epilepsy.[2][9][11][12] Mouse Gria4 deficiency models recapitulate absence‑like seizures, supporting the central role of GluA4 in thalamocortical excitability, though they do not fully model the human neurodevelopmental phenotype.[2][9] ClinGen currently assigns moderate evidence to the GRIA4–NEDSGA gene–disease relationship, and additional cases and variants continue to expand the genotypic and phenotypic spectrum.[9][14][18]

Diagnostic confirmation hinges on recognizing the characteristic clinical phenotype and identifying a pathogenic GRIA4 missense variant via trio exome or genome sequencing, with neuroimaging and EEG providing supportive evidence.[11][12][14][18] Treatment remains symptomatic and supportive, focusing on seizure control, spasticity management, rehabilitative therapies, and care for ocular and systemic complications, with no disease‑specific or gene‑targeted therapies currently available.[4][11][18] Genetic counseling addresses the de novo dominant nature of GRIA4 mutations and reproductive options, while early intervention aims to maximize developmental outcomes and prevent secondary complications.

Future research priorities include functional characterization of human NEDSGA variants in neuronal systems, development of iPSC and organoid models, exploration of AMPA‑modulating therapies, and longitudinal natural history studies to define prognosis and optimal care strategies. As genomic sequencing becomes more widespread in neurodevelopmental disorders, more NEDSGA cases will likely be recognized, enabling refined genotype–phenotype correlations and informing personalized interventions. For now, NEDSGA exemplifies how rare de novo mutations in synaptic receptor genes can disrupt early brain development and produce complex neurodevelopmental syndromes, highlighting the importance of integrating genetics, neurobiology, and clinical care in understanding and managing such conditions.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 85 |
| Resolved | 78 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 6 |
| Terms whose name was checked | 68 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 39 |
| Terms whose name is worth a second look | 14 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001263` (2 mentions) - the report calls it "Global developmental delay", "Neonatal/infancy"; HP calls it **Global developmental delay**
- `HP:0010863` (1 mention) - the report calls it "Profound intellectual disability"; HP calls it **Receptive language delay**
- `HP:0002067` (2 mentions) - the report calls it "Spasticity"; HP calls it **Bradykinesia**
- `HP:0002312` (2 mentions) - the report calls it "Spastic gait"; HP calls it **Clumsiness**
- `HP:0001371` (3 mentions) - the report calls it "Hypertonia"; HP calls it **Flexion contracture**
- `HP:0001319` (2 mentions) - the report calls it "Contractures", "Childhood"; HP calls it **Neonatal hypotonia**
- `HP:0004885` (2 mentions) - the report calls it "Impaired gait"; HP calls it **Episodic respiratory distress**
- `HP:0002353` (2 mentions) - the report calls it "Abnormal EEG", "Childhood"; HP calls it **EEG abnormality**
- `HP:0000484` (2 mentions) - the report calls it "Retinal hypoplasia"; HP calls it **Hyperopic astigmatism**
- `HP:0000556` (1 mention) - the report calls it "Chorioretinal hyperpigmentation"; HP calls it **Retinal dystrophy**
- `HP:0004322` (4 mentions) - the report calls it "Macrotia", "Short stature", "Congenital"; HP calls it **Short stature**
- `HP:0001337` (2 mentions) - the report calls it "Choreiform movements"; HP calls it **Tremor**
- `HP:0000734` (2 mentions) - the report calls it "Stereotypy"; HP calls it **Disinhibition**
- `HP:0002028` (2 mentions) - the report calls it "Feeding difficulties", "Neonatal/infancy"; HP calls it **Chronic diarrhea**
- `HP:0001251` (2 mentions) - the report calls it "Irritability"; HP calls it **Ataxia**
- `HP:0001285` (1 mention) - the report calls it "Hyperreflexia"; HP calls it **Spastic tetraparesis**
- `HP:0002376` (2 mentions) - the report calls it "Exaggerated startle response"; HP calls it **Developmental regression**
- `GO:0098984` (2 mentions) - the report calls it "neuron projection"; GO calls it **neuron to neuron synapse**
- `GO:0005891` (2 mentions) - the report calls it "AMPA‑type glutamate receptor complex", "Cellular components: AMPA receptor complex"; GO calls it **voltage-gated calcium channel complex**
- `GO:0007612` (1 mention) - the report calls it "memory"; GO calls it **learning**
- `GO:0098962` (1 mention) - the report calls it "neuronal action potential"; GO calls it **obsolete regulation of postsynaptic neurotransmitter receptor activity**
- `GO:0022038` (1 mention) - the report calls it "neurogenesis"; GO calls it **corpus callosum development**
- `CL:0002604` (2 mentions) - the report calls it "Cell types: cortical pyramidal neuron"; CL calls it **hippocampal astrocyte**
- `UBERON:0000955` (2 mentions) - the report calls it "eye"; UBERON calls it **brain**
- `UBERON:0001811` (1 mention) - the report calls it "visual cortex"; UBERON calls it **conjunctiva**
- `UBERON:0002338` (1 mention) - the report calls it "corpus callosum"; UBERON calls it **lamina propria of bronchus**
- `UBERON:0001465` (1 mention) - the report calls it "muscle organ"; UBERON calls it **knee**
- `UBERON:0001450` (1 mention) - the report calls it "joint"; UBERON calls it **calcaneus**
- `UBERON:0001623` (1 mention) - the report calls it "extraocular skeletal muscle"; UBERON calls it **dorsal nasal artery**
- `UBERON:0002084` (1 mention) - the report calls it "heart"; UBERON calls it **heart left ventricle**
- `UBERON:0002090` (1 mention) - the report calls it "tricuspid valve"; UBERON calls it **postcranial axial skeleton**
- `UBERON:0002099` (1 mention) - the report calls it "foramen ovale"; UBERON calls it **cardiac septum**
- `UBERON:0001041` (1 mention) - the report calls it "pharynx"; UBERON calls it **foregut**
- `UBERON:0000945` (1 mention) - the report calls it "esophagus"; UBERON calls it **stomach**
- `UBERON:0001045` (1 mention) - the report calls it "stomach"; UBERON calls it **midgut**
- `NCIT:C772` (1 mention) - the report calls it "Anticonvulsant agent"; NCIT calls it **Probenecid**
- `NCIT:C2315` (1 mention) - the report calls it "Muscle relaxant"; NCIT calls it **Hormone**
- `NCIT:C15624` (1 mention) - the report calls it "Supportive care"; NCIT calls it **9-cis-Retinoic Acid/Interferon Alfa**
- `NCIT:C15336` (1 mention) - the report calls it "Physical therapy"; NCIT calls it **Testing**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0098962` (obsolete regulation of postsynaptic neurotransmitter receptor activity) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002123` (2 mentions) - the report calls it "Generalized tonic‑clonic seizures"; HP calls it **Generalized myoclonic seizure**, and lists "Generalized myoclonic seizures" among its other names
- `HP:0002069` (2 mentions) - the report calls it "Absence seizures"; HP calls it **Bilateral tonic-clonic seizure**, and lists "Grand mal seizures" among its other names
- `HP:0001659` (2 mentions) - the report calls it "Tricuspid regurgitation"; HP calls it **Aortic regurgitation**
- `HP:0002079` (2 mentions) - the report calls it "Thin corpus callosum"; HP calls it **Hypoplasia of the corpus callosum**, and lists "Hypoplastic corpus callosum" among its other names
- `GO:0005234` (2 mentions) - the report calls it "extracellular ligand‑gated ion channel activity"; GO calls it **extracellularly glutamate-gated ion channel activity**, and lists "extracellular-glutamate-gated ion channel activity" among its other names
- `GO:0005261` (2 mentions) - the report calls it "cation channel activity"; GO calls it **monoatomic cation channel activity**, and lists "cation channel activity" among its other names
- `GO:0006812` (1 mention) - the report calls it "cation transport"; GO calls it **monoatomic cation transport**, and lists "cation transport" among its other names
- `GO:0007268` (2 mentions) - the report calls it "synaptic transmission"; GO calls it **chemical synaptic transmission**, and lists "synaptic transmission" among its other names
- `GO:0007611` (1 mention) - the report calls it "learning"; GO calls it **learning or memory**
- `GO:0050804` (1 mention) - the report calls it "modulation of synaptic transmission"; GO calls it **modulation of chemical synaptic transmission**, and lists "modulation of synaptic transmission" among its other names
- `GO:0007399` (2 mentions) - the report calls it "nervous system development", "Biological processes: nervous system development"; GO calls it **nervous system development**
- `UBERON:0001782` (2 mentions) - the report calls it "retina"; UBERON calls it **pigmented layer of retina**, and lists "pigmented retina" among its other names
- `UBERON:0000956` (3 mentions) - the report calls it "optic nerve", "cerebral cortex"; UBERON calls it **cerebral cortex**, and lists "cortical plate (areas)" among its other names
- `UBERON:0001043` (1 mention) - the report calls it "tongue"; UBERON calls it **esophagus**, and lists "gullet" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001263` - called "Global developmental delay", "Neonatal/infancy"
- `HP:0001319` - called "Contractures", "Childhood"
- `HP:0002353` - called "Abnormal EEG", "Childhood"
- `HP:0004322` - called "Macrotia", "Short stature", "Congenital"
- `HP:0002028` - called "Feeding difficulties", "Neonatal/infancy"
- `GO:0005891` - called "AMPA‑type glutamate receptor complex", "Cellular components: AMPA receptor complex"
- `GO:0007399` - called "nervous system development", "Biological processes: nervous system development"
- `UBERON:0000956` - called "optic nerve", "cerebral cortex"

### Terms the ontology service could not be reached for

1 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `MedGen:C4693391` (1 mention)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `Taxon`.