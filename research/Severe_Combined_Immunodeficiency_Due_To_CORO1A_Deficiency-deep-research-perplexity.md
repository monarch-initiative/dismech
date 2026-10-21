---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-28T21:32:52.239188'
end_time: '2026-09-28T21:37:46.265911'
duration_seconds: 294.03
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Severe Combined Immunodeficiency Due To CORO1A Deficiency
  mondo_id: MONDO:0014168
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: low
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 42
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 12
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 80
  verified: 73
  not_found: 2
  obsolete: 2
  unverifiable: 3
  confabulation_rate: 0.026
  labels_checked: 39
  labels_matching: 11
  labels_mismatched: 22
  mislabelled_terms:
  - term_id: HP:0008069
    reported_labels:
    - "T\u2011cell lymphopenia"
    ontology_label: Neoplasm of the skin
  - term_id: HP:0005308
    reported_labels:
    - "CD4+ T\u2011cell lymphopenia"
    ontology_label: Pulmonary artery vasoconstriction
  - term_id: HP:0031494
    reported_labels:
    - "Naive CD4+ T\u2011cell deficiency"
    ontology_label: Ovarian mucinous tumor
  - term_id: HP:0031520
    reported_labels:
    - "Naive T\u2011cell deficiency"
    ontology_label: Groin pain
  - term_id: HP:0005348
    reported_labels:
    - "NK\u2011cell lymphopenia"
    ontology_label: Inspiratory stridor
  - term_id: HP:0002721
    reported_labels:
    - "Abnormal B\u2011cell count"
    ontology_label: Immunodeficiency
  - term_id: HP:0004430
    reported_labels:
    - Impaired antibody response to vaccination
    ontology_label: Severe combined immunodeficiency
  - term_id: HP:0002729
    reported_labels:
    - Abnormal lymphocyte proliferation
    ontology_label: Follicular hyperplasia
  - term_id: HP:0002725
    reported_labels:
    - Immunodeficiency
    ontology_label: Systemic lupus erythematosus
  - term_id: HP:0002733
    reported_labels:
    - Lymphoproliferative disorder
    ontology_label: Abnormal lymph node morphology
  - term_id: HP:0100085
    reported_labels:
    - Chronic active EBV infection
    ontology_label: Small epiphyses of the 5th toe
  - term_id: HP:0000998
    reported_labels:
    - Epidermodysplasia verruciformis
    ontology_label: Hypertrichosis
  - term_id: HP:0009740
    reported_labels:
    - Molluscum contagiosum
    ontology_label: Aplasia of the parotid gland
  - term_id: HP:0001657
    reported_labels:
    - Recurrent herpes simplex infections
    ontology_label: Prolonged QT interval
  - term_id: HP:0002728
    reported_labels:
    - Opportunistic infections
    ontology_label: Recurrent mucocutaneous candidiasis
  - term_id: HP:0002826
    reported_labels:
    - Leprosy
    ontology_label: Halberd-shaped pelvis
  - term_id: HP:0004370
    reported_labels:
    - "B\u2011cell lymphoma"
    ontology_label: Abnormality of temperature regulation
  - term_id: HP:0002758
    reported_labels:
    - Recurrent bacterial infections
    ontology_label: Osteoarthritis
  - term_id: HP:0001581
    reported_labels:
    - Flat wart
    ontology_label: Recurrent skin infections
  - term_id: HP:0001014
    reported_labels:
    - Pityriasis versicolor
    ontology_label: Angiokeratoma
  - term_id: HP:0002762
    reported_labels:
    - "Non\u2011melanoma skin cancer"
    ontology_label: Multiple exostoses
  - term_id: HP:0000737
    reported_labels:
    - Autism
    ontology_label: Irritability
  labels_variant: 6
  unresolved_terms:
  - HP:0002746
  - HP:0008408
  obsolete_terms:
  - term_id: GO:0051270
    ontology_label: obsolete regulation of cellular component movement
  - term_id: GO:0042089
    ontology_label: GO_0042089
    replaced_by: GO:0001816
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Severe Combined Immunodeficiency Due To CORO1A Deficiency
- **MONDO ID:** MONDO:0014168 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Severe Combined Immunodeficiency Due To CORO1A Deficiency** covering all of the
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

# Severe Combined Immunodeficiency Due To CORO1A Deficiency (Immunodeficiency 8, MONDO:0014168)

Severe combined immunodeficiency due to CORO1A deficiency, also known as immunodeficiency 8 with lymphoproliferation, is a very rare autosomal recessive primary immunodeficiency characterized by profound T‑cell lymphopenia with preservation or relative sparing of B‑cell and natural killer (NK)‑cell numbers, failure of effective adaptive immune responses, and a striking predisposition to severe viral infections and EBV‑associated lymphoproliferative disease.[11][8][40][25] At the molecular level, the disease is caused by biallelic loss‑of‑function or hypomorphic mutations in the CORO1A gene on chromosome 16p11.2, which encodes coronin‑1A, a hematopoietic actin‑regulatory protein that is essential for thymic egress and survival and motility of peripheral T lymphocytes.[17][19][8][9] Since the first human case was described in parallel with a thymic egress‑deficient mouse strain in 2008, fewer than 20 patients worldwide have been reported, spanning a spectrum from classical T^−^B^+^NK^+^ SCID in early infancy to milder combined immunodeficiency phenotypes with late onset, mucocutaneous viral disease such as epidermodysplasia verruciformis, and EBV‑driven B‑cell lymphomas.[19][8][2][38][42] Because of its rarity, much of our knowledge derives from detailed case reports and mechanistic studies in human cells and mouse models, but together these data reveal a coherent pathophysiologic chain from coronin‑1A deficiency to defective actin dynamics at immune synapses, impaired T‑cell survival and migration, and consequent immune failure and viral oncogenesis.[19][8][35][39] This report synthesizes current evidence on disease characteristics, mechanisms, clinical features, diagnostics, and management, with particular emphasis on integrating molecular, cellular, and clinical data into a unified disease ontology entry for MONDO:0014168.

## 1. Disease Information

### Overview and Nosology

Severe combined immunodeficiency due to CORO1A deficiency is classified in OMIM under the phenotype “Immunodeficiency 8 with lymphoproliferation (IMD8)” (MIM 615401) and is explicitly linked to biallelic pathogenic variants in CORO1A (MIM 605000) on chromosome 16p11.2.[11][9][9][11] OMIM notes that IMD8 is “an autosomal recessive primary immunodeficiency characterized by early-childhood onset of recurrent infections and lymphoproliferative disorders, often associated with EBV infection.”[11][11] Orphanet catalogs the disorder under ORPHA:228003 as “T‑B+NK+ severe combined immunodeficiency due to CORO1A deficiency,” describing profoundly decreased T‑cell levels, normal B‑cell counts, low immunoglobulin levels, preserved thymic tissue, and clinical manifestations including recurrent infections, EBV‑associated B‑cell lymphoproliferative syndrome/lymphoma, mucocutaneous immunodeficiency, and sometimes neurocognitive impairment and behavioral dysfunction such as ADHD.[40] MedGen and related terminologies group it under “Severe combined immunodeficiency due to CORO1A deficiency,” synonymized with “Immunodeficiency 8; IMMUNODEFICIENCY 8 WITH LYMPHOPROLIFERATION,” and assign MONDO:0014168.[25][25][25]

From a clinical immunology perspective, CORO1A deficiency is often described as a variant of T^−^B^+^NK^+^ SCID, reflecting the typical immunophenotype of markedly reduced naive CD4^+^ and CD8^+^ T cells, normal or slightly reduced B‑cell numbers, and variably reduced NK cells.[8][8][22][2] However, subsequent reports have broadened the spectrum to include patients with combined immunodeficiency (CID) rather than classic SCID, with some residual T‑cell function and later onset of severe infections, and thus the disease is also framed as “Coronin‑1A deficiency–associated CID” in recent reviews.[8][8][2] Primary immunodeficiency organizations such as the Immune Deficiency Foundation present it as “Coronin 1A deficiency,” emphasizing its similarity to SCID in terms of severe T‑cell dysfunction but noting the unusual presence of a structurally intact thymus.[6][6]

In terms of coding identifiers, SNOMED CT includes “Severe combined immunodeficiency due to coronin 1A deficiency” (1229942009), and MedGen cross‑links to ICD‑10‑CM D81.2 (“Combined immunodeficiencies”) and, in some contexts, D84.8 (“Other specified immunodeficiencies”).[25][25] Disease Ontology assigns DOID:0060019 for “coronin‑1A deficiency,” defined as “a severe combined immunodeficiency that is an actin regulator when mutated results in SCID through inhibition of thymic egress of mature thymocytes into peripheral lymphoid organs.”[5] These nosologic descriptors converge on a core concept: a Mendelian, autosomal recessive immunodeficiency due to an actin‑binding protein defect, primarily affecting T‑cell development, egress, and peripheral homeostasis, with characteristic EBV‑driven lymphoproliferative complications.[5][11][8][40][25]

The information synthesized here arises predominantly from aggregated disease‑level resources—OMIM entries, Orphanet summaries, MedGen concept pages, and Disease Ontology records—combined with primary clinical case series and mechanistic studies rather than individual EHR data.[11][8][25][40][25] Landmark clinical papers include the first description of coronin‑1A deficiency as a thymic egress defect in a human SCID patient paralleling a mouse strain (Shiow et al., Nat Immunol 2008, PMID 18836449), the identification of a compound heterozygous truncating CORO1A mutation and a 16p11.2 deletion in SCID with ADHD (Shiow et al., Clin Immunol 2009, PMID 19027879), and subsequent families with hypomorphic missense mutations and unusual mucocutaneous syndromes (Moshous et al., J Allergy Clin Immunol 2013, PMID 23522482; Stray‑Pedersen et al., J Clin Immunol 2014, PMID 25073507).[19][21][27][39][42] Recent reviews compile these cases and provide consensus descriptions of disease characteristics.[8][34][38][38]

### Synonyms and Alternative Names

Across databases and literature, several synonyms are used:

Orphanet employs “T‑B+NK+ SCID due to CORO1A deficiency,” “T‑B+NK+ SCID due to coronin‑1A deficiency,” and “T‑B+NK+ severe combined immunodeficiency due to coronin‑1A deficiency.”[40] OMIM and MedGen use “Immunodeficiency 8 with lymphoproliferation” and “Severe combined immunodeficiency due to CORO1A deficiency,” while the gene‑based descriptor “Coronin‑1A deficiency” is frequent in immunology literature.[11][25][25][38] Disease Ontology lists “coronin‑1A deficiency” as the primary label for DOID:0060019.[5] Some case reports refer to “Coronin‑1A‑deficient SCID,” “late/hypomorphic‑like SCID due to CORO1A,” or “mucocutaneous‑immunodeficiency syndrome of EV–HPV associated with CORO1A deficiency,” highlighting specific clinical features.[22][42] In EBV‑focused reviews, the entity is subsumed under “primary immunodeficiencies associated with EBV disease,” with coronin actin binding protein 1A listed among proteins whose deficiency predisposes to EBV‑associated B‑cell lymphoma and lymphoproliferation.[12][14][34][34]

For ontology mapping, the most appropriate MONDO term is MONDO:0014168 “severe combined immunodeficiency due to CORO1A deficiency,” with logical axioms connecting to OMIM 615401, Orphanet ORPHA:228003, DOID:0060019, and SNOMED CT 1229942009.[25][25][40][25] This integrated perspective facilitates consistent cross‑referencing across knowledge bases.

## 2. Etiology

### Genetic Causal Factors

The primary etiologic factor in this disease is biallelic germline mutation in CORO1A, an autosomal recessive inheritance pattern confirmed by multiple kindreds.[11][9][27][39][42] OMIM emphasizes that immunodeficiency‑8 with lymphoproliferation is “caused by homozygous or compound heterozygous mutation in the CORO1A gene on chromosome 16p11.”[11][11] All reported affected individuals have inherited one pathogenic or hypomorphic CORO1A allele from each parent; heterozygous carriers are clinically unaffected, supporting a recessive loss‑of‑function mechanism.[4][8][27]

The CORO1A gene encodes coronin‑1A, also known as p57, coronin 1, or coronin actin‑binding protein 1A, a member of the coronin family of actin‑associated proteins predominantly expressed in hematopoietic cells.[9][9][8][36] In humans, CORO1A resides at 16p11.2 with genomic coordinates 16:30,183,602–30,189,076 (GRCh38).[9][9][9] Coronin‑1A localizes to the plasma membrane and F‑actin–rich regions, including the leading edge of migrating lymphocytes and immunological synapses, and is implicated in regulation of actin filament branching via Arp2/3, T‑cell motility, thymic egress, survival signaling, and formation of effective immune synapses.[19][21][35][36][37]

Clinical variant types include frameshift truncating mutations, splice‑site mutations, large exon deletions, and hypomorphic missense variants. Stray‑Pedersen et al. identified compound heterozygous frameshift variants c.248_249delCT (p.P83RfsX10) and c.1077delC (p.Q360RfsX44) in two siblings presenting with late‑onset mucocutaneous immunodeficiency syndrome and EV‑HPV infection, resulting in complete loss of coronin‑1A protein expression.[22][42] Moshous et al. reported three siblings with a homozygous missense mutation c.717C>A (p.V134M) in the β‑propeller domain, which “abrogates almost completely the protein expression in the patients’ cells” and causes hypomorphic coronin‑1A deficiency.[39][42] Shiow et al. described a girl with SCID and ADHD who was compound heterozygous for a truncating CORO1A mutation and a de novo 600‑kb 16p11.2 deletion encompassing CORO1A.[27][9][8] More recent work has identified a hemizygous c.19C>T (p.Arg7Cys) variant associated with combined immunodeficiency, decreased cellular coronin‑1A protein levels with normal mRNA, impaired NK‑cell cytotoxicity, platelet calcium signaling, and defects in motility of granulocytes and mesenchymal stromal cells.[2][1] ClinVar catalogues large multi‑exon deletions of CORO1A as pathogenic variants underlying SCID phenotypes.[28]

Collectively, these mutations predominantly result in reduced or absent coronin‑1A protein expression and thus are functional loss‑of‑function alleles. Experimental evidence from patient lymphocytes and murine Coro1a‑null lines shows impaired T‑cell migration, survival, and signaling, bolstering the causal link between CORO1A loss and immunodeficiency.[19][8][35][10][39] The disease therefore fits squarely within the Mendelian category of monogenic primary immunodeficiencies with a defined causal gene.

### Environmental and Infectious Factors

Environmental or lifestyle factors are not primary causes of CORO1A deficiency; rather, they modulate clinical expression and complications in affected individuals. There is no evidence that toxins, diet, or occupational exposures increase the risk of developing the genetic defect, as the condition arises from inherited mutations present from conception.[11][8][40] However, infectious exposures play a pivotal role in triggering disease manifestations, particularly EBV and human papillomaviruses (HPV) of the beta‑HPV group.

EBV infection is nearly ubiquitous globally, but in individuals with coronin‑1A deficiency, impaired cytotoxic T‑cell and NK‑cell control of EBV leads to persistent viremia and a spectrum of EBV‑associated lymphoproliferative diseases, ranging from chronic active EBV infection to B‑cell lymphomas.[12][14][34][39][34] Reviews of EBV‑associated primary immunodeficiencies list coronin‑1A deficiency as a recognized cause of EBV‑driven B‑cell lymphoma and lymphoproliferative disease, often in early childhood.[12][14][34][34] Moshous et al. explicitly note “a primary immunodeficiency with increased susceptibility to EBV-induced lymphoproliferation…associated with hypomorphic Coronin‑1A mutation.”[39]

Similarly, HPV infections, typically asymptomatic in immunocompetent individuals, can produce chronic, disseminated plane warts and pityriasis versicolor–like lesions characteristic of epidermodysplasia verruciformis in CORO1A‑deficient patients. Stray‑Pedersen et al. reported siblings with disseminated EV‑like HPV infection (HPV‑5 and 17 by PCR), molluscum contagiosum, oral‑cutaneous HSV‑1 ulcers, and granulomatous tuberculoid leprosy in the context of CORO1A deficiency.[18][22][23][42] Recent dermatologic series regard CORO1A mutations as one of the inborn errors of immunity underlying inherited EV, alongside MST1, RHOH, and TMC6/TMC8 mutations.[15][18][20][24]

Thus, while the etiologic lesion is genetic, common viral infections serve as environmental triggers that reveal and amplify the immunodeficiency, resulting in opportunistic infections and oncogenesis. It is important to distinguish these triggers from causative factors: EBV and HPV are necessary for certain manifestations (lymphoma, EV), but they do not cause the underlying disease state; rather, they exploit the defective immune system created by CORO1A mutations.[12][14][18][34][39][34]

### Risk and Protective Factors

Given the rarity of CORO1A deficiency and its monogenic nature, genetic risk is driven almost entirely by carrier status in parents and consanguinity in affected families. Many reported kindreds arise in consanguineous contexts, such as Moroccan siblings with homozygous V134M mutation described by Moshous et al., reflecting increased probability of homozygous recessive alleles in consanguineous pedigrees.[39][42] There is no evidence of polygenic susceptibility loci or modifier alleles altering penetrance, although phenotypic variability among patients suggests potential genetic modifiers that remain unidentified.[8][2][38][42]

Environmental “risk factors” in the conventional epidemiologic sense—smoking, diet, occupational exposures—have not been systematically linked to disease severity due to the small number of cases. However, early and repeated exposure to EBV, high community prevalence of oncogenic EBV strains, and inadequate infection control may increase the likelihood and severity of EBV‑associated complications in affected children, as inferred from families in high EBV endemic settings.[12][14][34][39][34] Conversely, rigorous prophylactic antibiotic and antiviral strategies, reduction of environmental pathogen exposure, and early hematopoietic stem cell transplantation (HSCT) represent protective factors that can modify disease course by limiting infections and restoring immune function, though they do not alter the underlying genotype.[8][8][26][26]

No specific genetic protective variants have been described that ameliorate CORO1A deficiency. In mouse models, complete Coro1a knockout produces profound T‑cell deficiency without apparent compensation by other coronin family members, suggesting limited redundancy.[35][10] However, the unique case of SCID with 16p11.2 deletion (encompassing 24 genes) illustrates that comorbid copy number variation can modify the phenotype, contributing neurodevelopmental disorders such as ADHD and altering the overall clinical picture.[27][9][32][8] This is an example of a genetic co‑factor worsening rather than protecting the disease state.

Gene–environment interactions are evident in the way CORO1A mutations modulate lymphocyte responses to pathogens. Coronin‑1A deficiency disrupts actin dynamics required for proper immune synapse formation and cytotoxic function, so environmental exposure to viruses that rely heavily on T‑cell and NK‑cell control—EBV, HPV, HSV, mycobacteria—elicits particularly severe disease manifestations.[12][14][18][35][39][42] In vitro studies in coronin‑1A‑deficient macrophages and lymphocytes demonstrate altered phagosome maturation and calcium signaling, which may interact with microbial virulence strategies.[35][36] Nonetheless, current data do not support traditional variable penetrance based on environmental exposures; rather, they highlight ubiquitous pathogens as triggers of manifestations in a genetically determined immunodeficiency.

## 3. Phenotypes

### General Clinical Phenotype Spectrum

Patients with CORO1A deficiency manifest a spectrum of clinical phenotypes that, taken together, define a distinctive primary immunodeficiency with both infectious susceptibility and immune dysregulation. Reviews summarizing all known cases emphasize several recurring themes: recurrent upper respiratory tract infections in infancy and childhood; severe or opportunistic viral infections, notably EBV‑associated lymphoproliferation and B‑cell lymphoma; mucocutaneous infections including EV‑like HPV disease, molluscum contagiosum, HSV‑1 ulcers, and sometimes mycobacterial infections such as tuberculoid leprosy; lymphopenia with profoundly reduced naive CD4^+^ T cells; variably low B and NK cells; hypogammaglobulinemia or non‑protective vaccine responses; and, in some cases, neurocognitive impairment or ADHD.[8][22][34][6][39][42]

The age of onset is typically in infancy or early childhood, consistent with Orphanet’s notation of neonatal, infancy, or childhood onset.[40] The classical SCID phenotype appears within the first months of life, with severe recurrent infections, failure to thrive, and profound T‑cell deficiency detected by newborn screening using T‑cell receptor excision circle (TREC) assays.[7][29][29] On the other end of the spectrum, hypomorphic or compound heterozygous mutations can produce later onset combined immunodeficiency, with mucocutaneous syndromes appearing around school age or later, as in the siblings with EV‑HPV whose disease debuted around age seven.[22][42] In the Moshous kindred, EBV‑associated lymphoproliferative disease may present in early childhood but could be preceded by recurrent ENT and respiratory infections.[39][14]

Symptom severity is generally high, with life‑threatening complications such as EBV‑positive lymphoma, fatal lymphoproliferative syndrome, severe pneumonia, bronchiectasis, and disseminated cutaneous HPV lesions.[18][8][34][39][42] However, the progression is variable: some patients experience rapidly progressive disease requiring urgent HSCT, while others exhibit more chronic, relapsing‑remitting courses of infections and lymphoproliferation, influenced by residual T‑cell function and access to treatment.[8][8][26][26] Quality of life is profoundly affected by frequent hospitalizations, invasive interventions, chronic infections, disfiguring skin lesions, and neurocognitive issues, although formal QOL studies are lacking due to the small numbers; case reports nonetheless describe significant functional impairments and psychosocial burden, particularly in patients with ADHD or neurodevelopmental delay.[27][6][40]

Below, major phenotype domains are discussed with suggested HPO terms and characteristics.

### Immunologic Phenotypes

The cardinal immunologic abnormality is T‑cell lymphopenia, particularly of naive CD4^+^ T cells. All coronin‑1A–deficient patients described to date have shown a T(−/low), B(low/+), NK(low/+) phenotype, with markedly reduced naive peripheral T cells and near‑undetectable TRECs on newborn screening where measured.[7][8][22][29][29] Stray‑Pedersen’s siblings demonstrated “absent CD4CD45RA(+) (naïve) T and memory B cells, low NK cells and abnormally increased double‑negative (DN) γδ T‑cells.”[22][42] Moshous et al. similarly reported “significant diminution of naive T-cell numbers, impaired development of a diverse T-cell repertoire, near-to-absent invariant natural killer T cells, and severely diminished mucosal-associated invariant T cell numbers.”[39] Thus, suggested HPO terms include HP:0008069 (T‑cell lymphopenia), HP:0005308 (CD4+ T‑cell lymphopenia), HP:0031494 (Naive CD4+ T‑cell deficiency), HP:0031520 (Naive T‑cell deficiency), HP:0005348 (NK‑cell lymphopenia), and HP:0002721 (Abnormal B‑cell count).

Functionally, lymphocyte proliferative responses to mitogens are impaired but not completely absent, reflecting residual signaling capacity in some patients.[8][34] Serum immunoglobulins are detectable, but specific antibody titers following vaccines are low or absent, except occasionally against tetanus toxoid.[8][34] HPO mapping would include HP:0002715 (Abnormal immunoglobulin level), HP:0004430 (Impaired antibody response to vaccination), and HP:0002729 (Abnormal lymphocyte proliferation). Combined immunodeficiency manifests clinically as recurrent infections, opportunistic pathogens, and poor clearance of viruses, aligning with HP:0002718 (Recurrent infections) and HP:0002725 (Immunodeficiency).

Quality of life impact stems from frequent infections, need for long‑term antibiotic prophylaxis and IVIG, and risk of lymphoma, necessitating intensive medical care and limiting normal childhood activities. Although formal EQ‑5D or SF‑36 data are absent, anecdotal descriptions of hospitalizations, HSCT, and chronic skin disease suggest significant impairment in mobility, self‑care, usual activities, pain/discomfort, and anxiety/depression domains.

### Infectious Phenotypes

Recurrent upper respiratory tract infections, otitis media, and pneumonia are common early manifestations, consistent across case series.[8][8][34][6] For example, coronin‑1A‑deficient patients in Puck and colleagues’ review “all suffered from upper respiratory tract infections; and inability to control EBV was a prominent feature, associated with fatal lymphoproliferative syndrome and lymphoma at a particularly young age.”[8][8] Suggested HPO terms include HP:0002205 (Recurrent upper respiratory tract infections), HP:0002090 (Pneumonia), and HP:0000388 (Recurrent otitis media).

EBV‑associated disease is particularly prominent. Moshous et al. described three siblings in whom “one patient had an EBV-positive lymphoproliferative process and two had EBV lymphomas,” identifying CORO1A mutation as the underlying defect.[14][39] Reviews of EBV in primary immunodeficiency note that at least five coronin‑1A‑deficient patients have developed EBV‑driven B‑cell lymphoma.[34][34] Phenotypically, this corresponds to HP:0002746 (Lymphoma), HP:0002733 (Lymphoproliferative disorder), HP:0008408 (Epstein–Barr virus infection), and HP:0100085 (Chronic active EBV infection).

Mucocutaneous infections are a distinguishing feature in hypomorphic and compound heterozygous cases. Stray‑Pedersen et al. reported siblings with a “mucocutaneous-immunodeficiency syndrome of epidermodysplasia verruciformis-human-papilloma-virus (EV-HPV), molluscum contagiosum and oral-cutaneous herpetic (HSV-1) ulcers; the older female sibling also had a disfiguring granulomatous tuberculoid leprosy.”[22][42] EV‑like HPV disease presents as disseminated flat warts and pityriasis versicolor–like lesions associated with beta‑HPV infection and increased risk of non‑melanoma skin cancer.[18][23][24] Appropriate HPO terms include HP:0000998 (Epidermodysplasia verruciformis), HP:0009740 (Molluscum contagiosum), HP:0001657 (Recurrent herpes simplex infections), HP:0002728 (Opportunistic infections), and HP:0002826 (Leprosy). Bronchiectasis has been reported, reflecting chronic pulmonary damage from recurrent infections (HP:0002110).[18][23][42]

The progression of infectious phenotypes is often chronic and cumulative: repeated respiratory infections can lead to structural lung damage, acute EBV infection can transition to chronic active EBV and lymphoma, and persistent HPV infection can evolve into EV and, later, non‑melanoma skin cancer.[12][18][23][24][34][39] These complications significantly impair quality of life via respiratory insufficiency, skin pain and pruritus, cosmetic disfigurement, cancer risk, and the psychological burden of chronic illness.

### Hematologic and Oncologic Phenotypes

Beyond lymphopenia, coronin‑1A‑deficient patients exhibit a tendency toward EBV‑driven B‑cell lymphomas and lymphoproliferative syndromes. The Moshous siblings exemplify this, with documented EBV‑positive lymphomas.[14][39] Reviews of EBV‑associated primary immunodeficiencies list coronin‑1A deficiency among syndromes predisposing to EBV‑associated B‑cell lymphomas and lymphoproliferative disease.[12][14][34][34] HPO terms include HP:0002746 (Lymphoma), HP:0002733 (Lymphoproliferative disorder), and HP:0004370 (B‑cell lymphoma).

An interesting hematologic feature in some cases is neutropenia. A newborn diagnosed by TREC‑based screening had profound T‑cell deficiency accompanied by neutropenia, an unusual finding for this condition and highlighted as a novel phenotype.[7][29] HPO mapping would include HP:0001875 (Neutropenia). Another reported case displayed IgM‑dominant immunoglobulin profile with hypogammaglobulinemia, suggestive of impaired class‑switch recombination or memory B‑cell defects.[38][38] This aligns with HP:0002715 (Abnormal immunoglobulin level), HP:0002729 (Abnormal lymphocyte proliferation), and HP:0002758 (Recurrent bacterial infections).

From a progression standpoint, oncologic phenotypes such as lymphoma significantly worsen prognosis and require aggressive treatment (chemotherapy, HSCT), further affecting quality of life and survival.[34][39][34] The psychological impact of cancer diagnoses in young children and adolescents, layered on chronic immunodeficiency, is considerable but under‑documented.

### Dermatologic Phenotypes

Dermatologic manifestations are central in CORO1A‑related EV and mucocutaneous immunodeficiency syndromes. Epidermodysplasia verruciformis (EV) is described as “a rare skin disease characterized by persistent disseminated flat warts and pityriasis versicolor-like lesions, associated with a high risk of non-melanoma skin cancer (NMSC).”[18][24] In the CORO1A siblings, lesions were HPV‑5 and HPV‑17 positive by PCR, indicating beta‑HPV infection.[18][22][23][42] HPO terms include HP:0000998 (Epidermodysplasia verruciformis), HP:0001581 (Flat wart), HP:0001014 (Pityriasis versicolor), and HP:0002762 (Non‑melanoma skin cancer).

Molluscum contagiosum and chronic oral‑cutaneous HSV‑1 ulcers add to the dermatologic burden, causing pain, pruritus, and cosmetic disfigurement, especially on exposed areas such as the face and extremities.[22][23][42] Tuberculoid leprosy in one sibling produced disfiguring granulomatous lesions.[22][42] Over time, these lesions can progress, fluctuate, or respond only partially to therapy, resulting in chronic dermatologic disability, psychological distress due to appearance changes, and social stigmatization.

Quality of life impacts are severe in EV, as noted in dermatology literature where patients often face stigma and functional limitations due to extensive lesions.[18][23][24] While formal QOL metrics (e.g., Dermatology Life Quality Index) have not been applied specifically to CORO1A‑related EV, extrapolation from EV cohorts suggests significant impairment across physical, emotional, and social domains.

### Neurological and Behavioral Phenotypes

Neurological and behavioral phenotypes in coronin‑1A deficiency are less consistent but noteworthy in specific contexts. Orphanet notes that “some patients may show developmental delay, neurocognitive impairment, and behavioral dysfunction (in particular attention deficit-hyperactivity disorder).”[40] The clearest example is the SCID patient described by Shiow et al., who had attention deficit hyperactivity disorder (ADHD) due to a de novo 16p11.2 microdeletion encompassing CORO1A and 24 other genes, a region recurrently associated with autism spectrum disorders and ADHD.[27][9][32][8] The authors conclude that “deletion as well as duplication of this same interval on 16p11.2 is well recognized and has been associated with autism spectrum disorder and neurodevelopmental disorders including ADHD…our patient’s 16p11.2 deletion also predisposed her to ADHD.”[27][9][8]

It remains uncertain whether pure CORO1A loss (without broader 16p11.2 CNV) contributes directly to neurobehavioral phenotypes, although coronin‑1A is expressed in the nervous system and involved in nerve growth factor signaling pathways in mice.[35][10][37] Mouse studies show that adult Coro1a knockout animals have no significant gross neuroanatomical abnormalities, but functional behavioral assessments are limited.[10] Therefore, suggested HPO terms in human cases include HP:0001263 (Global developmental delay), HP:0007018 (Attention deficit hyperactivity disorder), HP:0000737 (Autism), and HP:0001250 (Seizures) where applicable, but these should be annotated with caution and linked to co‑occurring genomic alterations when present.

Quality of life consequences of ADHD and developmental delay are substantial, affecting schooling, social integration, and family dynamics, as described in general neurodevelopmental literature. In CORO1A deficiency, these impairments compound the burden of immunodeficiency and chronic illness, necessitating multidisciplinary care.

## 4. Genetic and Molecular Information

### Causal Gene and Gene Ontology

The causal gene CORO1A (HGNC:2252) encodes coronin‑1A, also known as coronin, actin binding protein 1A, CLABP, p57, Lmb3, and coronin 1.[9][10][9][10] NCBI Gene assigns gene ID 11151 in humans; the mouse ortholog Coro1a has gene ID 12721.[10][10][37] Cytogenetically, CORO1A is located at 16p11.2, a region subject to recurrent copy number variations associated with neurodevelopmental disorders.[9][27][9][32][8] OMIM summarizes coronin‑1A as “an actin-regulating protein that is expressed mainly in hematopoietic cells,” highlighting its role in immune cell biology.[9][9]

Gene Ontology (GO) annotations for coronin‑1A include molecular functions such as “actin filament binding activity” and “identical protein binding activity,” biological processes such as “regulation of actin filament polymerization,” “cellular response to interleukin‑4,” “nerve growth factor signaling pathway,” and “positive regulation of T‑cell proliferation,” and cellular components including “cell leading edge,” “early endosome,” “immunological synapse,” and “plasma membrane.”[37] These GO terms capture the protein’s positioning at the interface of actin cytoskeleton regulation, signal transduction, and immune synapse formation, consistent with functional studies demonstrating impaired T‑cell motility and immune synapse assembly in coronin‑1A deficiency.[19][21][35][36][39]

### Pathogenic Variants and ACMG Classification

Reported pathogenic CORO1A variants include:

Frameshift truncations such as c.248_249delCT (p.P83RfsX10) and c.1077delC (p.Q360RfsX44), which create premature stop codons leading to nonsense‑mediated decay and complete loss of protein expression.[22][42] These variants fulfill ACMG criteria for pathogenicity as null alleles in a gene where loss of function is a known disease mechanism (PVS1), segregating in affected siblings (PP1), and absent or extremely rare in population databases (PM2).[22][42][28]

Missense variants such as c.717C>A (p.V134M) in the β‑propeller domain, which severely reduce protein expression and function. Moshous et al. demonstrated abrogated coronin‑1A expression in patient cells, providing strong functional evidence (PS3) and evolutionary conservation of the affected residue (PP3), supporting classification as pathogenic or likely pathogenic.[39][42]

Hemizygous missense c.19C>T (p.Arg7Cys) variants, which decrease coronin‑1A protein levels but leave mRNA intact, cause combined immunodeficiency with impaired NK cytotoxicity and platelet calcium signaling.[2][1] Functional assays showing reduced protein and cellular defects support pathogenicity (PS3), though full ACMG classification may be “likely pathogenic” pending segregation and population frequency data.[2][31]

Gross deletions encompassing exons 1–10 of CORO1A, including the initiator codon, are classified as pathogenic in ClinVar, as they are predicted to result in absent protein and have been observed in individuals with SCID whose genotype is consistent with trans configuration of another pathogenic variant.[28][9] Such multi‑exon deletions also often extend beyond CORO1A to neighboring genes within the 16p11.2 interval, complicating phenotypic interpretation.[27][9][8]

ClinVar entries include variants like NM_007074.4(CORO1A):c.885T>C (p.Phe295=), classified as likely benign for severe combined immunodeficiency due to CORO1A deficiency, illustrating that synonymous variants without functional impact should not be over‑interpreted.[33][31] This underscores the need for careful ACMG evaluation integrating functional studies.

Allele frequencies of pathogenic CORO1A variants in gnomAD and other population databases are extremely low or absent, consistent with the rarity of the disease and strong purifying selection against complete coronin‑1A deficiency.[38][38] Hypomorphic alleles may exist at slightly higher frequencies in certain populations but are not common. No somatic CORO1A mutations have been linked to cancer or other diseases in COSMIC or TCGA to date; coronin‑1A dysfunction appears predominantly germline and immunologic.[31][33]

The functional consequences of these variants are uniformly loss‑of‑function at the protein level, whether by truncation, nonsense‑mediated decay, protein misfolding and degradation, or impaired translation. There is no evidence of gain‑of‑function or dominant negative effects; heterozygotes are clinically unaffected and mice with one functional Coro1a allele display normal T‑cell counts.[4][8][10] This fits a recessive null model where coronin‑1A activity is reduced below a critical threshold only when both alleles are affected.

### Modifier Genes and Epigenetic Information

To date, no specific modifier genes have been systematically demonstrated to alter severity or expression of CORO1A deficiency. However, the co‑occurrence of 16p11.2 microdeletions, which encompass multiple genes including CORO1A, raises the possibility that other genes in the interval, such as those implicated in neurodevelopmental disorders, modify neurobehavioral phenotypes or broader systemic features.[27][9][32][8] For example, genes within 16p11.2 have been linked to autism spectrum disorders and language delay, and their deletion in combination with CORO1A truncation may account for ADHD and developmental issues in the SCID patient described by Shiow et al.[27][9][8]

Epigenetic changes specifically associated with CORO1A deficiency have not been reported. Given coronin‑1A’s role in actin dynamics and signal transduction at immune synapses, it is conceivable that downstream transcriptional programs are altered in T cells lacking coronin‑1A, potentially affecting chromatin states and epigenetic marks at immune genes. However, no dedicated epigenomics or DNA methylation studies in CORO1A‑deficient lymphocytes have been published to date. The absence of data should be explicitly noted in ontology records.

### Chromosomal Abnormalities and Copy Number Variation

Besides single‑gene mutations, large copy number variations involving 16p11.2 have been documented in coronin‑1A deficiency. Shiow et al. identified a de novo 600‑kb interstitial deletion of chromosome 16p11.2 in a girl with SCID and ADHD, encompassing 25 genes including CORO1A; on the other allele, she carried a 2‑bp deletion in CORO1A, resulting in compound heterozygosity and complete coronin‑1A loss.[27][9][8] Genome‑wide oligonucleotide array analysis demonstrated hemizygosity across the 16p11.2 region, confirming the CNV and linking it to both immunodeficiency and neurodevelopmental phenotypes.[27][9][32][8]

ClinVar notes similar multi‑exon deletions of CORO1A that may extend beyond the gene’s coding region, potentially affecting neighboring genes and complicating genotype–phenotype correlations.[28] Rarechromo and other CNV resources indicate that loss or gain of material from 16p11.2 is among the most common structural chromosome disorders, associated with autism, ADHD, and language or psychiatric conditions.[32] Thus, in some patients, coronin‑1A deficiency exists within a broader CNV syndrome, necessitating careful clinical and molecular interpretation.

Ontology entries should capture that chromosomal microdeletions of 16p11.2 (e.g., dbVar nsv####, DECIPHER records) can cause CORO1A deficiency when combined with another CORO1A allele mutation, and that such CNVs may introduce additional phenotypes beyond immunodeficiency.

## 5. Environmental Information

### Non‑Genetic Contributing Factors

As a monogenic, autosomal recessive disease, CORO1A deficiency arises independent of classical environmental exposures. There is no evidence that toxins, radiation, pollution, or other non‑infectious environmental factors directly induce CORO1A mutations or significantly alter penetrance. Most patients come from varied geographic and socioeconomic backgrounds, and no clustering around specific environmental exposures has been reported.[11][8][40]

However, the immunodeficiency renders patients highly susceptible to environmental pathogens, particularly respiratory viruses and bacteria, herpesviruses, and HPV. In resource‑limited settings or environments with high pathogen burden, the frequency and severity of infections may be greater, leading to earlier and more severe clinical manifestations than in settings with robust infection control measures.[18][8][34][39] For ontology purposes, environmental factors should be annotated as modulators of clinical course rather than etiologic agents.

Lifestyle factors such as smoking, diet, exercise, or alcohol consumption have not been systematically studied in this tiny patient population. Nonetheless, general immunology principles suggest that smoking or malnutrition could further impair respiratory defenses and immune function, worsening infection outcomes, although these would be generic and not disease‑specific risk factors. Given the lack of direct data, such relationships should be flagged as inferred rather than demonstrated.

### Infectious Agents as Triggers

EBV (Human herpesvirus 4; NCBI Taxon ID 10376) is a central infectious agent interacting with CORO1A deficiency. In healthy individuals, EBV infection is typically controlled by cytotoxic CD8^+^ T cells and NK cells; in coronin‑1A deficiency, impaired cytoskeletal rearrangements at immune synapses, defective calcium signaling, and T‑cell lymphopenia compromise immune control, resulting in chronic EBV viremia and lymphoproliferative diseases.[12][14][34][39][34] EBV‑associated pathologies include chronic active EBV, fulminant hemophagocytic lymphohistiocytosis (HLH), infectious mononucleosis, and B‑cell lymphomas.[12][14][34][34] Coronin‑1A deficiency is specifically linked to EBV‑associated non‑Hodgkin lymphomas and lymphoproliferative syndromes.[12][14][34][39][34]

HPV, particularly beta‑HPV types such as HPV‑5 and HPV‑17 (NCBI Taxon ID group 333752), causes EV‑like cutaneous lesions in CORO1A‑deficient patients. These manifestations depend on chronic infection with beta‑HPVs, which are otherwise asymptomatic in immunocompetent hosts.[18][23][24][42] The presence of disseminated EV‑like lesions and increased risk of non‑melanoma skin cancer underscores the interplay between CORO1A‑mediated T‑cell immunity and viral oncogenesis.[18][23][24]

Other infectious agents include HSV‑1 (Human herpesvirus 1; NCBI Taxon ID 10298), causing chronic oral‑cutaneous ulcers; Mycobacterium leprae (Taxon ID 1769), leading to tuberculoid leprosy in one sibling; and various respiratory bacteria and viruses contributing to bronchiectasis.[18][22][23][34][42] These pathogens exploit the impaired T‑cell responses in coronin‑1A deficiency, but they are not etiologic for the genetic disease itself.

For ontology mapping, EBV and HPV should be linked as environmental triggers or co‑morbid infections (CHEBI:5522 for viral entities, IEDB epitope records for EBV antigens), with annotation that their pathologies are significantly amplified in CORO1A deficiency.

## 6. Mechanism and Pathophysiology

### Ordered Causal Chain from Mutation to Clinical Manifestation

1. Biallelic loss‑of‑function or hypomorphic mutations in CORO1A lead to reduced or absent coronin‑1A protein expression in hematopoietic cells, particularly T lymphocytes.[11][8][22][39]

2. Reduced coronin‑1A protein leads to impaired regulation of Arp2/3‑mediated actin branching and defective localization of coronin‑1A to the leading edge and immunological synapses of T cells, resulting in abnormal actin dynamics.[19][21][35][36]

3. Defective actin dynamics and coronin‑1A mislocalization lead to impaired T‑cell motility within thymus and lymph nodes, causing a block in thymic egress of mature thymocytes into the circulation and peripheral lymphoid organs.[19][21][35][10]

4. Blocked thymic egress leads to profound peripheral T‑cell lymphopenia, particularly of naive CD4^+^ and CD8^+^ T cells, with near‑absent TRECs and altered TCR repertoire diversity, while thymic tissue remains structurally present.[7][19][8][22][29][39]

5. In parallel, coronin‑1A deficiency leads to impaired immune synapse formation, defective TCR signaling, abnormal calcium flux, and increased F‑actin accumulation at synapses, resulting in increased T‑cell apoptosis and reduced survival of peripheral T cells.[34][35][39]

6. Combined deficits in T‑cell egress, motility, and survival lead to a T(−/low), B(low/+), NK(low/+) immunophenotype with profoundly reduced naive T cells, impaired T‑cell proliferation to mitogens, reduced invariant NKT and MAIT cells, and variably low memory B and NK cells.[8][22][35][39][42]

7. This severe T‑cell dysfunction leads to impaired cell‑mediated immune responses against viruses and intracellular pathogens, resulting in recurrent infections, chronic viral persistence (especially EBV and HPV), and opportunistic infections such as HSV‑1 and mycobacteria.[12][14][18][8][34][39][42]

8. Chronic EBV infection in the setting of impaired cytotoxic T‑cell and NK‑cell control leads to EBV‑driven B‑cell lymphoproliferation and lymphoma, with loss of NKT cells and altered cytoskeletal rearrangement at immune synapses further predisposing to EBV‑associated malignancies.[12][14][16][34][39][34]

9. Chronic beta‑HPV infection in skin in the setting of defective T‑cell surveillance leads to EV‑like cutaneous lesions, persistent EV‑HPV infection, and increased risk of non‑melanoma skin cancer.[18][22][23][24][42]

10. Recurrent respiratory infections and chronic inflammation lead to secondary tissue damage such as bronchiectasis, while systemic immune dysregulation contributes to elevated IgE, hypogammaglobulinemia, and shortened telomeres in some patients.[18][22][38][42]

11. The cumulative effect of severe immunodeficiency, opportunistic infections, and lymphoproliferative malignancies leads to high morbidity and mortality in early childhood unless corrected by HSCT, which restores donor T‑cell function and resolves immunologic defects.[8][8][26][26]

Where explicit mechanisms have not been experimentally demonstrated in human cells (e.g., telomere shortening), they are inferred from observations of shortened telomeres and generalized immune stress rather than direct mechanistic assays.[22][42]

### Molecular Pathways and Cellular Processes

At the molecular level, coronin‑1A participates in actin cytoskeleton regulation through interactions with Arp2/3 complex and F‑actin. Shiow et al. showed that a point substitution in coronin‑1A (lysine for glutamic acid at position 26 in the mouse Ptcd strain) enhanced coronin‑1A’s inhibition of Arp2/3, mislocalized the protein from the leading edge of migrating T cells, and resulted in irregularly shaped protrusions and intrinsic migration defects.[19][21] Two‑photon microscopy revealed that Coro1A‑deficient T cells had abnormal motility within lymph nodes, establishing coronin‑1A as a regulator of T‑cell egress and trafficking in response to sphingosine‑1‑phosphate (S1P) signaling.[19][21]

Gene Ontology processes relevant here include GO:0030036 (actin cytoskeleton organization), GO:0030833 (regulation of actin filament polymerization), GO:0007015 (actin filament organization), and GO:0051270 (regulation of T‑cell migration).[37] Coronin‑1A’s role in S1P‑dependent thymic egress is linked to pathways involving S1P receptor 1 (S1P1) and downstream Rho GTPases that coordinate actin rearrangement.[19][21] mDia1, a formin family actin nucleator promoting unbranched actin filaments, is also required for thymic egress, highlighting the balance between Arp2/3‑mediated branching and formin‑mediated elongation.[19][21]

Cellular processes affected include T‑cell migration (GO:0072678), T‑cell survival (GO:0042089), immune synapse formation (GO:0001772), TCR signaling (GO:0050852), and calcium‑dependent signaling (GO:0007165). Föger et al. and subsequent reviews report that coronin‑1A deficiency impacts “development, survival, TCR signaling, immune synapse formation and migration” across lymphocyte lineages.[34][8] Impaired calcium flux and F‑actin accumulation at the immune synapse result in increased T‑cell apoptosis and CD4^+^ lymphopenia, as documented in coronin‑1A–deficient human patients.[34][8]

Coronin‑1A also interacts with pathways in macrophages. Early work suggested coronin‑1A recruited to mycobacterial phagosomes prevented their transfer to lysosomes, aiding Mycobacterium tuberculosis survival; coronin‑1A deficiency in mice led to enhanced lysosomal delivery and mycobacterial killing.[35] However, later studies indicate that coronin‑1A‑deficient macrophages retain intact motility and phagocytosis, suggesting that T cells are more critically dependent on coronin‑1A than macrophages in vivo.[35][36]

### Protein Dysfunction and Biochemical Abnormalities

Coronin‑1A is a WD40‑repeat protein forming a β‑propeller structure that binds actin and other partners at the plasma membrane and immunological synapses.[36][39] Missense mutations such as V134M likely alter this β‑propeller’s stability, leading to protein misfolding and degradation, as evidenced by abrogated coronin‑1A expression in patient cells.[39] Frameshift and large deletions result in truncated, nonfunctional proteins or complete loss of translation, extinguishing coronin‑1A activity.[22][28][42]

Biochemically, coronin‑1A deficiency leads to abnormal F‑actin dynamics at the immune synapse, with excessive accumulation and impaired turnover, which in turn disrupts assembly of signaling complexes and the spatial organization of TCR, co‑receptors, and adhesion molecules.[34][35][36] Calcium signaling defects have been documented in coronin‑1A‑deficient T cells and platelets, reflecting impaired coupling between receptor engagement and calcium influx.[2][34] These abnormalities compromise activation thresholds, cytokine production, and effector functions.

Coronin‑1A’s role in S1P1 signaling suggests that its absence may alter downstream signaling cascades including RhoA, Rac1, and Cdc42 pathways, though detailed biochemical mapping in human T cells is incomplete. Nonetheless, the net effect is a failure of T cells to properly respond to chemotactic gradients, exit thymus and lymph nodes, and home to sites of infection.

### Immune System Involvement and Tissue Damage

Coronin‑1A deficiency primarily affects T cells (CL:0000084), including naive CD4^+^ T cells (CL:0000895), naive CD8^+^ T cells (CL:0000900), invariant NKT cells (CL:0000815), and MAIT cells (CL:0001054).[35][39][42] NK cells (CL:0000623) and B cells (CL:0000236) are variably affected, with reduced NK counts and memory B cells in some patients.[8][22][39][42] Macrophages (CL:0000235) and dendritic cells (CL:0000451) appear less directly impacted, though coronin‑1A is expressed and functional in these cells as well.[35][36][37]

The immune consequences include reduced thymic egress, peripheral T‑cell depletion, impaired effector functions, and failure to control chronic viral infections. Tissue damage arises indirectly from infections and chronic inflammation: recurrent pneumonia leads to bronchiectasis (UBERON:0000397 for lung, HP:0002110 for bronchiectasis), chronic EV lesions increase risk of cutaneous squamous cell carcinoma and basal cell carcinoma, and EBV lymphoproliferation can infiltrate lymphoid tissues, bone marrow, and other organs.[18][8][34][39][42]

Biochemical abnormalities such as elevated IgE (HP:0004429) and hypogammaglobulinemia reflect dysregulated B‑cell maturation and class switching under impaired T‑cell help.[8][22][38][42] Shortened telomeres observed in some patients suggest accelerated replicative stress in lymphocytes, though causality between coronin‑1A and telomere maintenance remains unclear and requires further study.[22][42]

### Molecular Profiling and Advanced Technologies

No large‑scale transcriptomic, proteomic, metabolomic, or lipidomic profiling studies focused specifically on CORO1A‑deficient human lymphocytes have been published. Some mechanistic papers use flow cytometry, immunoblotting, and imaging to assess protein expression and cell migration but not genome‑wide or proteome‑wide approaches.[19][21][35][39] Single‑cell analyses, spatial transcriptomics, and multi‑omics integration data are lacking, reflecting the rarity of the disease and limited sample sizes.

Functional genomics screens (CRISPR, RNAi) have not targeted CORO1A in human T‑cell lines within large datasets such as DepMap, though coronin‑1A’s role in mycobacterial survival has been explored with RNAi knockdown in macrophages.[35] This gap presents an opportunity for future mechanistic studies to apply single‑cell RNA‑seq and CRISPR screens to better understand coronin‑1A’s network of interacting pathways.

Given the absence of such data, ontology annotations should explicitly note that advanced molecular profiling evidence is currently unavailable for this disease and that mechanistic understanding is derived chiefly from focused studies in mice and human primary cells.

## 7. Anatomical Structures Affected

### Organ‑Level Involvement

The primary organ system affected is the immune system, particularly lymphoid organs such as thymus (UBERON:0002384), lymph nodes (UBERON:0000029), spleen (UBERON:0002106), and bone marrow (UBERON:0002371). Coronin‑1A deficiency impairs thymic egress of mature thymocytes, resulting in T‑cell paucity in peripheral lymphoid organs despite a structurally present thymus.[19][8][21][40] Imaging and autopsy studies in coronin‑1A–deficient patients reveal thymic tissue but few circulating T cells and small peripheral lymph nodes.[8][40]

Secondary organ involvement includes lungs (UBERON:0002048) with recurrent infections and bronchiectasis, skin (UBERON:0002097) with EV lesions and other mucocutaneous infections, liver (UBERON:0002107) and spleen with hepatosplenomegaly from EBV lymphoproliferation, and central nervous system structures in cases with 16p11.2 CNVs and neurodevelopmental disorders.[18][8][27][34][39][42] The hematopoietic system (UBERON:0001969) broadly is impacted via lymphopenia and altered leukocyte subsets.

Body systems involved span the immune system (MeSH D007154), integumentary system, respiratory system, and nervous system, reflecting both primary and secondary effects. Cardiovascular, digestive, and endocrine systems are less prominently affected, though systemic infections can impact multiple organs.

### Tissue and Cell‑Level Targets

At the tissue level, lymphoid tissues including thymic cortex and medulla, lymph node paracortex, and splenic white pulp are key sites where coronin‑1A acts in T‑cell development and egress.[19][21][10] Histological studies in mice show reduced T‑cell zones and altered architecture in Coro1a‑null animals.[35][10] Cutaneous epidermis and dermis are tissue sites for EV lesions and HPV infection.[18][23][24][42]

Within these tissues, specific cell populations affected include:

Naive CD4^+^ and CD8^+^ T cells (CL:0000895; CL:0000900) in peripheral blood and lymphoid organs, which are profoundly depleted.[8][22][39][42] Invariant NKT cells (CL:0000815) and MAIT cells (CL:0001054), which are nearly absent in some patients.[39] Double‑negative γδ T cells (CL:0000798), which are abnormally increased, representing a limited‑diversity T‑cell subpopulation.[22][42] B cells (CL:0000236), particularly memory B cells (CL:0000813), which can be reduced or absent.[22][39][42] NK cells (CL:0000623), which are variably low and exhibit impaired cytotoxicity.[2][8][22][39] Platelets (CL:0000233), where coronin‑1A deficiency leads to altered calcium signaling.[2]

Epithelial keratinocytes (CL:0000312) in skin are indirectly affected through impaired immune surveillance, allowing beta‑HPV infection and EV lesion development.[18][23][24][42] Macrophages (CL:0000235) and dendritic cells are less prominently impacted but may have altered phagosome maturation in mycobacterial infection contexts.[35][36]

### Subcellular Localization

Coronin‑1A localizes to the cell leading edge, early endosomes, immunological synapses, and plasma membrane, consistent with GO cellular components such as GO:0031252 (cell leading edge), GO:0001772 (immunological synapse), GO:0005737 (cytoplasm), and GO:0005886 (plasma membrane).[37] In migrating T cells, coronin‑1A accumulates at F‑actin–rich protrusions, coordinating actin depolymerization and Arp2/3 regulation.[19][21][36] At the immune synapse, coronin‑1A helps organize actin networks underlying TCR clustering and signaling.

In macrophages, coronin‑1A is recruited to phagosomal membranes, where it modulates phagosome–lysosome fusion in the context of mycobacterial infection.[35] Early endosomal localization suggests roles in receptor trafficking and signaling. There is no evidence of nuclear localization or direct transcriptional regulation.

Subcellular compartments involved in pathophysiology therefore include actin cytoskeleton (GO:0015629), cell cortex (GO:0005938), plasma membrane, immunological synapse, and endosomal system. These locations underscore coronin‑1A’s function in dynamic cell shape changes, migration, and synapse assembly.

### Localization and Lateralization

Anatomically, disease manifestations are generally systemic rather than lateralized. T‑cell lymphopenia affects the entire immune system; EBV lymphoproliferation can be diffuse; EV lesions typically appear symmetrically on sun‑exposed areas such as face, neck, and extremities.[18][23][24][42] Bronchiectasis may be more pronounced in specific lung lobes depending on infection patterns, but lateralization is not a defining feature.

For ontology, tissues such as thymus, lymph nodes, spleen, lungs, skin, and bone marrow should be annotated as affected sites, with “bilateral” or “diffuse” descriptors where appropriate.

## 8. Temporal Development

### Age of Onset and Onset Pattern

CORO1A deficiency is congenital, with mutations present from birth, but clinical onset varies across a spectrum from neonatal to late childhood. Orphanet lists age of onset as childhood, infancy, and neonatal.[40] Classical SCID presentations occur in the first months of life, with severe infections, failure to thrive, and detection via TREC‑based newborn screening.[7][29][29] The infant described by newborn screening exhibited profound T‑cell deficiency and neutropenia shortly after birth.[7][29]

Hypomorphic or compound heterozygous cases can show later onset. Stray‑Pedersen’s siblings developed EV‑HPV mucocutaneous syndrome at around seven years of age, with bronchiectasis and leprosy evolving over subsequent years.[22][42][18][23] Moshous’s siblings presented in early childhood with EBV‑associated lymphoproliferative disease and lymphomas but may have had preceding recurrent infections.[39][14]

Onset pattern is typically insidious rather than acute, with recurrent infections accumulating over months to years before catastrophic events like lymphoma or severe pneumonia. EBV‑driven lymphoproliferation may appear as an acute severe illness superimposed on chronic immunodeficiency.[12][14][34][39][34]

### Disease Progression and Course

Disease progression can be conceptualized in stages:

An early stage marked by recurrent infections and failure to thrive. Infants with severe T‑cell deficiency experience frequent respiratory, ENT, and gastrointestinal infections, often requiring hospitalization and prophylactic therapy.[8][8][34][6]

An intermediate stage with opportunistic infections and mucocutaneous disease. As children age, chronic EV‑HPV lesions, molluscum contagiosum, HSV‑1 ulcers, and possibly mycobacterial infections emerge in those with residual T‑cell function.[18][22][23][42]

An advanced stage characterized by EBV‑driven lymphoproliferation and lymphoma, bronchiectasis, and multi‑organ complications. EBV‑positive lymphomas occur in early childhood or adolescence, often with poor outcomes without HSCT.[14][8][34][39][34] Bronchiectasis develops over years of recurrent pneumonia.[18][23]

Without curative treatment, disease course is progressive and often fatal in childhood due to severe infections, respiratory failure, or lymphoma. With successful HSCT, immune defects can be corrected, altering progression to a stable post‑transplant course, though residual organ damage and neurodevelopmental issues may persist.[8][8][26][26]

The progression rate varies with mutation type and residual protein function. Null alleles produce rapid, severe SCID; hypomorphic alleles yield slower, combined immunodeficiency with later complications. This variability should be reflected in ontology as “variable expressivity.”

### Remission Patterns and Critical Periods

Spontaneous remission of immunodeficiency does not occur; the genetic lesion is permanent. However, EBV lymphoproliferation and skin lesions may partially respond to therapy, producing periods of clinical remission. HSCT can induce durable remission of immunologic defects by reconstituting donor‑derived T cells.[8][26][26]

Critical periods include the first year of life, when early diagnosis and HSCT confer the best chance of survival and normal immune function, and early childhood, when EBV infection typically occurs and can trigger lymphoproliferative disease in immunodeficient hosts.[12][14][34][39][34] Newborn screening for SCID using TRECs represents a critical opportunity to identify coronin‑1A deficiency before severe infections occur.[7][29][29] For ontology, time windows such as “neonatal,” “early childhood,” and “pre‑EBV seroconversion” could be annotated as periods of vulnerability.

## 9. Inheritance and Population

### Inheritance Pattern, Penetrance, and Expressivity

CORO1A deficiency follows an autosomal recessive inheritance pattern with high penetrance for immunodeficiency in individuals who are homozygous or compound heterozygous for pathogenic variants. OMIM, Orphanet, and MedGen all identify the mode of inheritance as autosomal recessive.[4][11][25][40][11] Heterozygous carriers, including parents and unaffected siblings, have normal immune function, confirming recessivity.[4][8][27][39][42]

Penetrance appears complete for immunologic abnormalities, as all reported biallelic mutation carriers exhibit T‑cell lymphopenia and combined immunodeficiency, though clinical severity and age of onset vary with mutation type (null versus hypomorphic).[8][2][38][42] Variable expressivity is evident in the spectrum from early‑onset SCID with profound T‑cell deficiency to later‑onset CID with EV mucocutaneous syndromes, EBV lymphomas, and partial immune function.[8][22][39][42] There is no evidence of genetic anticipation or germline mosaicism, given the recessive nature and limited generational data.

Consanguinity plays a significant role in some families, particularly those with homozygous missense or truncating mutations, as in the Moroccan siblings with V134M mutation described by Moshous et al.[39][42] This suggests that carrier frequency may be higher in certain populations with high rates of consanguineous marriage, though specific frequencies have not been quantified.

Founder effects have not been documented, but the recurrence of specific mutations (e.g., V134M) in geographically clustered families hints at possible founder alleles. Population genetic data from gnomAD and similar resources show extremely low allele frequencies of pathogenic CORO1A variants, consistent with strong selection against homozygous loss‑of‑function and the rarity of reported cases.[38][38]

### Epidemiology and Population Demographics

Coronin‑1A deficiency is exceedingly rare, with Orphanet estimating prevalence at <1 per 1,000,000.[40] Less than 10–20 patients have been reported in the literature worldwide, and no population‑based incidence figures are available.[8][2][38][38] Cases have arisen in diverse geographic regions, including North America, Europe, North Africa, and Inuit populations in Canada, indicating no strong geographic confinement.[8][26][39][42]

Sex ratio appears roughly balanced between male and female patients, reflecting autosomal inheritance, though small numbers preclude firm conclusions. Age distribution of affected individuals is skewed toward infancy and childhood, as severe immunodeficiency and EBV‑associated complications manifest early; survival into adolescence and adulthood may occur in milder cases or post‑HSCT.[8][26][26][39][42]

Carrier frequency is unknown but presumed to be extremely low in the general population, consistent with the lethal nature of the untreated phenotype and the rarity of identified cases. Genetic counseling resources emphasize autosomal recessive recurrence risks (25% affected, 50% carrier in each pregnancy) for known carrier couples.[40][25]

## 10. Diagnostics

### Clinical and Laboratory Tests

Diagnostic evaluation of suspected CORO1A deficiency begins with recognition of a combined immunodeficiency phenotype and characteristic immunologic findings. Laboratory tests include complete blood count with differential (revealing lymphopenia), quantitative immunoglobulins, lymphocyte subset analysis by flow cytometry, and T‑cell proliferation assays. All coronin‑1A–deficient patients show markedly reduced naive CD4^+^ and CD8^+^ T cells, often with increased double‑negative γδ T cells and variably reduced B and NK cells.[8][22][39][42] Lymphocyte proliferative responses to mitogens are impaired but not absent, and vaccine‑specific antibody titers are low or absent except occasionally against tetanus toxoid.[8][34] TRECs measured by PCR in dried blood spots can be nearly undetectable, allowing detection by newborn SCID screening.[7][29][29]

Biomarkers include reduced coronin‑1A protein expression in lymphocytes, assessable by Western blot or flow cytometry, and decreased TRECs. EBV viral load measured by PCR often shows chronic viremia, while EBV serology and lymph node biopsy may reveal lymphoproliferative disease or lymphoma.[14][34][39][34] Imaging such as chest CT can demonstrate bronchiectasis; PET/CT may show lymphomatous involvement of lymph nodes and extranodal sites.[18][34][39][34]

Functional tests such as NK‑cell cytotoxicity assays may reveal impaired killing of target cells, as described in the hemizygous Arg7Cys case.[2] Platelet function tests can detect altered calcium signaling, though these are not routinely performed.[2]

Biopsy findings in EV lesions show hyperkeratosis, acanthosis, and characteristic histological features of EV, often with detection of beta‑HPV DNA by PCR.[18][23][24][42] Lymph node biopsies in EBV lymphoma reveal clonal B‑cell proliferation with EBV‑positive cells on immunohistochemistry and in situ hybridization.[14][39][34]

### Genetic Testing Approaches

Genetic confirmation is essential for definitive diagnosis. Strategies include:

Single‑gene testing of CORO1A, using Sanger sequencing or targeted NGS panels for primary immunodeficiencies. GTR and Orphanet list laboratories offering “Diagnosis of Severe Combined Immunodeficiency due to Coronin‑1A Deficiency (CORO1A gene)” using such methods.[41][40]

Whole‑exome sequencing (WES), which has proven valuable in identifying novel CORO1A mutations in families with unexplained immunodeficiency and EBV lymphoproliferation (Moshous et al.) or mucocutaneous syndromes (Stray‑Pedersen et al.).[39][42] WES allows discovery of rare hypomorphic or compound heterozygous variants and can reveal additional genes contributing to phenotype.

Chromosomal microarray (CMA) or genome‑wide copy number analysis, which detected the 600‑kb 16p11.2 deletion encompassing CORO1A in the SCID+ADHD patient described by Shiow et al.[27][9][8] CMA should be considered when immunodeficiency co‑occurs with neurodevelopmental disorders or dysmorphic features.

Whole‑genome sequencing (WGS) could theoretically identify both single‑nucleotide variants and structural variants in CORO1A and neighboring genes, but specific WGS cases have not yet been reported in the published literature.

Karyotyping and FISH are less informative for small gene‑level mutations but may be used to characterize large chromosomal deletions involving 16p11.2. Mitochondrial DNA and repeat expansion testing are not relevant to CORO1A deficiency.

Gene panels for SCID and CID often include CORO1A in their gene lists, alongside other actin‑regulatory and signaling genes implicated in primary immunodeficiencies.[34][2] This facilitates targeted NGS diagnosis in clinically suspected cases without resorting immediately to WES.

### Omics‑Based Diagnostics and Clinical Criteria

Omics‑based diagnostics beyond genomic testing are not yet standard for CORO1A deficiency. RNA sequencing could reveal reduced CORO1A transcripts in null alleles and altered expression of downstream immune genes, but such data are not routinely utilized. Proteomics could identify absence of coronin‑1A and changes in cytoskeletal proteins at immune synapses. Metabolomics and epigenomics have not been applied.

Clinical diagnostic criteria for coronin‑1A deficiency are not formalized in society guidelines, but recognition relies on the combination of T(−/low), B(low/+), NK(low/+) phenotype with profoundly reduced naive CD4^+^ T cells, presence of thymic tissue, recurrent infections, EBV‑associated lymphoproliferation or lymphoma, EV‑like skin disease, and exclusion of other causes of SCID/CID.[8][34][8][40] Differential diagnoses include other forms of T‑B+ SCID such as IL7R, CD3 subunit, and JAK3 deficiencies, as well as combined immunodeficiencies affecting actin regulation (Wiskott–Aldrich syndrome, DOCK8 deficiency).[34][8] Distinguishing features of coronin‑1A deficiency include intact thymus, specific EV phenotype, and characteristic EBV lymphoproliferation with loss of NKT cells.[18][8][34][39]

### Screening

Newborn screening for SCID using TREC assays can detect coronin‑1A deficiency when TRECs are low or undetectable. A Canadian case report describes detection of coronin‑1A deficiency after birth by TREC‑based newborn screening, with subsequent WES confirming a novel homozygous mutation.[7][29][29] This highlights the utility of population‑based SCID screening in identifying CORO1A deficiency early.

Carrier screening in families with known mutations can be performed via targeted CORO1A sequencing. Preimplantation genetic diagnosis and prenatal testing are theoretically feasible but not widely documented, given the rarity of the disease. Risk stratification for EBV‑related complications may involve monitoring EBV viral load and lymphocyte counts, but no formal models exist.

## 11. Outcome and Prognosis

### Survival, Mortality, and Life Expectancy

Without treatment, coronin‑1A deficiency carries high mortality, largely due to severe infections and EBV‑associated lymphomas in childhood. Puck et al. noted that coronin‑1A–deficient patients “all suffered from upper respiratory tract infections; and inability to control EBV was a prominent feature, associated with fatal lymphoproliferative syndrome and lymphoma at a particularly young age.”[8][8] Case reports document deaths from EBV‑positive lymphoma in siblings with EV‑HPV mucocutaneous syndrome and bronchiectasis.[18][22][23][42] Life expectancy without curative therapy is therefore markedly reduced, often into early childhood or adolescence.

HSCT has emerged as a curative option, with at least two documented cases of successful transplantation resulting in long‑term engraftment and solid immune reconstitution.[26][26][8] In a Canadian Inuit patient, HSCT using an HLA‑matched unrelated donor led to restoration of T‑cell counts and function, resolution of infection susceptibility, and long‑term survival.[26][26] Post‑HSCT life expectancy may approach that of the general population, though long‑term data are limited.

Quantitative survival rates (5‑year, 10‑year) are not available due to the small number of patients. Prognosis is highly dependent on timely diagnosis, access to HSCT, and management of EBV and other infections.

### Morbidity, Disability, and Quality of Life

Morbidity in coronin‑1A deficiency is substantial. Patients experience chronic infections, bronchiectasis, EV lesions, lymphoma, and the side effects of chemotherapy and HSCT. Disability outcomes include chronic respiratory impairment from bronchiectasis, dermatologic disability from EV, and neurocognitive impairments in those with 16p11.2 CNVs.[18][8][27][34][39][42]

Quality of life measurements specific to coronin‑1A deficiency have not been systematically collected, but extrapolation from similar primary immunodeficiencies suggests significant impairments in physical functioning, social participation, emotional well‑being, and school/work performance. For instance, SCID survivors post‑HSCT often require ongoing medical monitoring and may have residual organ damage, while EV patients struggle with cosmetic and functional impacts of skin lesions.[8][18][23][26]

Caregiver burden is also high, with frequent hospitalizations, complex treatment regimens, and psychological stress. These factors should be acknowledged in disease knowledge bases even in the absence of formal EQ‑5D or SF‑36 data.

### Disease Course, Complications, and Recovery Potential

Complications include chronic EBV viremia, B‑cell lymphoma, bronchiectasis, EV‑associated non‑melanoma skin cancer, granulomatous leprosy, and treatment‑related side effects from chemotherapy and HSCT.[18][8][34][39][42] Recovery potential depends on the ability to perform HSCT and manage infections. HSCT can correct immunologic defects, reduce infection rates, and prevent EBV lymphomas, but pre‑existing organ damage may persist.[8][26][26]

Prognostic factors include age at diagnosis, mutation type (null versus hypomorphic), severity of T‑cell lymphopenia, presence of EBV lymphoproliferation at diagnosis, and access to specialized immunology and transplant services.[8][2][38][42] Patients diagnosed via newborn screening before severe infections may have the best outcomes. EBV viral load and lymphocyte subset profiles could serve as prognostic biomarkers; for example, persistent high EBV load and severe CD4^+^ lymphopenia predict risk of lymphoma.[12][14][34][39][34]

## 12. Treatment

### Pharmacotherapy and Supportive Care

Pharmacologic management focuses on infection prophylaxis and treatment. This includes broad‑spectrum antibiotics for bacterial infections, antiviral drugs (e.g., acyclovir for HSV, ganciclovir or rituximab‑combined regimens for EBV), and antifungals as needed. For EBV lymphomas, standard chemotherapy regimens combined with anti‑CD20 monoclonal antibody rituximab (NCIT:C61938) are used, though specific protocols vary.[12][14][34][39][34] Intravenous immunoglobulin (IVIG; NCIT:C20450) is often administered to provide passive immunity and reduce infection risk, particularly in patients with hypogammaglobulinemia and poor vaccine responses.[8][38][38]

Pharmacogenomics data specific to CORO1A deficiency are not available, but general immunodeficiency practice suggests careful dosing and monitoring of chemotherapeutic agents in patients with organ dysfunction.

Supportive care includes nutritional support, physiotherapy for bronchiectasis, dermatologic treatments for EV lesions (topical retinoids, interferon‑α, cryotherapy), and pain management for mucocutaneous ulcers.[18][23][24][42] Rehabilitation services may be needed for neurodevelopmental impairments.[27][40]

### Advanced Therapeutics: HSCT and Gene Therapy

Allogeneic HSCT (NCIT:C15206) is the main advanced therapeutic approach with curative potential. Puck et al. reported immunologic cure of coronin‑1A–deficient patients by allogeneic hematopoietic cell transplantation, demonstrating that the defect is T‑cell intrinsic and correctable with donor hematopoietic stem cells.[8][8] Subsequent case reports have documented successful HSCT with HLA‑matched unrelated donors, resulting in long‑term engraftment and reconstitution of T‑cell numbers and function.[26][26] HSCT outcomes suggest that the immunodeficiency aspect of the disease can be effectively ameliorated, though mucocutaneous lesions and organ damage require ongoing management.[8][26][26]

Gene therapy has not yet been applied to CORO1A deficiency, but conceptual frameworks from other SCID forms (ADA, IL2RG) suggest that lentiviral or retroviral vector–mediated CORO1A gene transfer into autologous hematopoietic stem cells could theoretically restore T‑cell function. CRISPR‑based gene editing to correct CORO1A mutations in patient HSCs is also conceivable. However, no clinical trials (NCT identifiers) exist to date, and preclinical safety and efficacy studies would be needed.

Cellular therapies beyond HSCT, such as CAR‑T cells, are not directly applicable to correcting the primary defect, though they could be used to treat EBV lymphomas in CORO1A‑deficient patients if immune reconstitution is sufficient.

### Surgical and Interventional Therapies

Surgical interventions may be required to manage complications such as bronchiectasis (lobectomy), cutaneous malignancies (excision of non‑melanoma skin cancers), and lymph node biopsies for lymphoma diagnosis.[18][23][34][39][42] These procedures follow standard surgical oncology and thoracic surgery protocols but are performed within the context of immunodeficiency, requiring careful infection prophylaxis.

### Experimental and Personalized Approaches

Experimental treatments are limited due to the rarity of the disease. Clinical trial databases currently do not list CORO1A‑specific interventional trials. However, general primary immunodeficiency trials (e.g., new HSCT protocols, gene therapy for SCID) could potentially enroll coronin‑1A–deficient patients under broader inclusion criteria.

Personalized medicine approaches involve tailoring HSCT timing and conditioning regimens based on genotype, T‑cell counts, and organ function. For example, patients with hypomorphic mutations and residual T‑cell function might undergo reduced‑intensity conditioning to minimize toxicity, while neonates diagnosed via newborn screening could receive early HSCT before severe infections occur.[7][29][26][26] Pharmacogenomic assessments of transplant drugs (e.g., calcineurin inhibitors) may optimize immunosuppression.

Combination therapies include using rituximab and chemotherapy for EBV lymphoma, followed by HSCT to correct the underlying immunodeficiency. IVIG, prophylactic antibiotics, and antivirals are combined with HSCT to reduce pre‑ and post‑transplant infection risks.

## 13. Prevention

### Primary, Secondary, and Tertiary Prevention

Primary prevention of CORO1A deficiency is challenging due to its genetic nature, but genetic counseling and carrier screening in families with known mutations can inform reproductive decisions, including preimplantation genetic diagnosis and prenatal testing.[40][25] Public health interventions do not alter disease incidence.

Secondary prevention focuses on early detection and treatment. Newborn screening for SCID using TREC assays provides a powerful tool to identify coronin‑1A deficiency before severe infections occur, allowing timely HSCT and reduced morbidity.[7][29][29] Cascade screening of relatives can identify carriers and additional affected individuals.

Tertiary prevention aims to prevent complications in diagnosed patients. This includes prophylactic antibiotics, antivirals, and IVIG to reduce infections; regular monitoring of EBV viral load and early treatment of lymphoproliferation; dermatologic surveillance for EV lesions and skin cancer; pulmonary physiotherapy to prevent bronchiectasis progression; and multidisciplinary care for neurodevelopmental issues.[18][8][34][39][42] These measures reduce morbidity and improve quality of life.

### Immunization and Behavioral Interventions

Vaccination strategies in coronin‑1A deficiency require careful consideration. Live attenuated vaccines (e.g., MMR, varicella) are generally contraindicated in SCID and severe CID due to risk of disseminated infection. Inactivated vaccines may be administered but often elicit poor protective responses; nonetheless, they could provide some benefit, particularly post‑HSCT when immune function is reconstituted.[8][6][40] EBV and HPV vaccines are not widely available for EBV and have limited efficacy in immunodeficient populations, but prophylactic HPV vaccines might reduce infection risk in EV‑prone patients.

Behavioral interventions include minimizing exposure to infectious agents through hygiene, avoiding crowded settings during outbreaks, and maintaining nutrition. Smoking avoidance reduces respiratory infection risk. These interventions, while generic, are important in tertiary prevention.

### Genetic Counseling and Public Health

Genetic counseling for families with CORO1A mutations emphasizes autosomal recessive inheritance, recurrence risk, carrier testing, and reproductive options such as preimplantation genetic diagnosis. Counseling also addresses psychosocial aspects of caring for a child with severe immunodeficiency.[40][25]

Public health interventions specific to coronin‑1A deficiency are limited due to its rarity, but SCID newborn screening programs represent a major policy measure that indirectly benefits these patients. Environmental interventions such as reducing air pollution or improving sanitation have generic benefits for infection control but are not disease‑specific.

Prophylactic medications such as trimethoprim–sulfamethoxazole for Pneumocystis jirovecii prophylaxis, antivirals for HSV, and IVIG for broad infection protection are standard in primary immunodeficiency care and constitute tertiary prophylaxis.[8][34][6]

## 14. Other Species and Natural Disease

### Species and Orthologous Genes

Mouse is the primary model organism for coronin‑1A deficiency. The mouse ortholog Coro1a (MGI:1345961) encodes coronin, actin binding protein 1A, with multiple allelic variants used in research.[10][10][37] NCBI Taxon ID for Mus musculus is 10090. Coro1a orthologs exist in other mammals and vertebrates, but natural disease analogous to human CORO1A deficiency has not been widely reported in companion animals or livestock.

### Natural Disease and Veterinary Relevance

There is no documentation of naturally occurring coronin‑1A deficiency in animals such as dogs or cats in OMIA or veterinary literature, suggesting that if such cases exist, they are extremely rare or underdiagnosed. Therefore, veterinary relevance is currently limited to comparative immunology and use of mouse models rather than clinical veterinary practice.

### Comparative Biology and Evolutionary Conservation

Coronin‑1A is evolutionarily conserved across vertebrates, reflecting its fundamental role in actin regulation and immune function. Comparative pathology in mice and humans shows striking similarities: Coro1a‑null mice are “profoundly deficient in T cells,” while other cell types are relatively unaffected.[35][10] This indicates that coronin‑1A’s role in T‑cell survival and migration is conserved, making mouse models highly relevant for understanding human disease and testing therapies.[19][35][10]

Cross‑species susceptibility to infections such as M. tuberculosis and EBV differs, but the mechanisms of immune synapse formation and actin dynamics are similar, supporting extrapolation of findings. There is no zoonotic transmission of CORO1A deficiency; it is a non‑infectious genetic disease.

## 15. Model Organisms

### Mouse Models of Coro1a Deficiency

Multiple mouse models with Coro1a mutations have been developed and are catalogued in MGI. These include Coro1a^ptcd^ (peripheral T cell deficiency), Coro1a^koy^ (knockout), and Coro1a^tm1Achn^ (targeted mutation).[10][10][21] Homozygous null or hypomorph alleles produce lower peripheral T‑cell counts due to defects in T‑cell migration and increased apoptosis, mirroring the human phenotype.[10]

Shiow et al. used the Ptcd strain to identify a point substitution in coronin‑1A that enhanced its inhibition of Arp2/3 and mislocalized the protein, resulting in T‑cell migration defects and thymic egress block.[19][21] Coro1a‑null mice show profound T‑cell deficiency, with minimal impact on other cell types, corroborating coronin‑1A’s T‑cell specificity.[35][10] Adult Coro1a knockout mice exhibit no significant brain neuroanatomical phenotypes, suggesting that neurodevelopmental issues in humans are likely due to broader 16p11.2 CNVs rather than coronin‑1A alone.[10][27][9][32][8]

These models recapitulate key aspects of human CORO1A deficiency: T‑cell lymphopenia, impaired thymic egress, and defective T‑cell motility. They provide platforms for studying S1P1 signaling, actin regulation, immune synapse formation, and response to infections such as M. tuberculosis.[19][35][10]

### Model Limitations and Applications

While mouse models faithfully reproduce T‑cell defects, they do not naturally develop EBV‑associated lymphoproliferation or EV‑like HPV disease, as EBV and human beta‑HPVs are human‑specific viruses. Thus, models cannot fully capture the infection‑driven oncologic and dermatologic aspects of human disease. This limitation should be acknowledged in ontology entries.

Applications of mouse models include:

Elucidating coronin‑1A’s molecular interactions with Arp2/3 and F‑actin, using imaging and biochemical assays.[19][21][36] Studying thymic egress and lymph node trafficking via two‑photon microscopy and flow cytometry.[19][21] Investigating T‑cell survival pathways and apoptosis under coronin‑1A deficiency.[35][10] Exploring macrophage responses to mycobacteria in Coro1a‑null mice, including phagosome maturation and lysosomal delivery.[35] Testing potential gene therapy or small‑molecule interventions that modulate actin dynamics or S1P signaling.

Other model systems, such as in vitro T‑cell lines with CORO1A knockdown or knockout, could complement mouse data, but such models are less documented in the literature.

## Conclusion

Severe combined immunodeficiency due to CORO1A deficiency (Immunodeficiency 8; MONDO:0014168) is a paradigmatic example of a Mendelian primary immunodeficiency rooted in defects of actin cytoskeleton regulation in T cells. Biallelic loss‑of‑function or hypomorphic mutations in CORO1A abrogate or severely diminish coronin‑1A protein expression, leading to impaired Arp2/3‑mediated actin branching, mislocalization of coronin‑1A at the leading edge and immune synapse, and consequent defects in thymic egress, T‑cell motility, immune synapse formation, and survival.[11][19][8][21][35][39] These cellular abnormalities produce a characteristic T(−/low), B(low/+), NK(low/+) immunophenotype, with profoundly reduced naive CD4^+^ T cells, impaired T‑cell proliferation, variably reduced memory B and NK cells, and deficient NKT and MAIT cells.[8][22][39][42]

Clinically, coronin‑1A deficiency manifests as a spectrum from classical T^−^B^+^NK^+^ SCID in infancy to milder combined immunodeficiency phenotypes with later onset, EV‑HPV mucocutaneous syndromes, EBV‑associated B‑cell lymphomas, bronchiectasis, and in some cases neurodevelopmental disorders associated with broader 16p11.2 CNVs.[18][8][27][34][39][42] Inability to control EBV is a hallmark, resulting in chronic viremia and lymphoproliferative disease; EV‑like lesions and HPV‑driven non‑melanoma skin cancer are prominent in hypomorphic or compound heterozygous mutations.[12][14][18][8][34][39][34][42] The thymus is structurally present, distinguishing coronin‑1A deficiency from other SCID forms with thymic aplasia, but peripheral T‑cell pools are severely depleted.[8][40]

Diagnosis rests on recognizing the immunologic signature, performing lymphocyte subset and proliferation analyses, measuring TRECs, and confirming biallelic CORO1A mutations via single‑gene sequencing, SCID gene panels, WES, or CMA for 16p11.2 deletions.[7][8][27][29][39][42] Newborn screening for SCID using TREC assays provides an avenue for early detection and intervention.[7][29][29] HSCT is currently the only curative therapy, with documented cases of successful immune reconstitution and long‑term survival, though mucocutaneous lesions and organ damage require ongoing management.[8][8][26][26] Supportive care, infection prophylaxis, and vigilant monitoring for EBV and HPV complications are essential to reduce morbidity and mortality.

From an ontology perspective, CORO1A deficiency should be annotated as an autosomal recessive, monogenic primary immunodeficiency with high penetrance, variable expressivity, and profound impact on T‑cell biology. Key HPO terms include T‑cell lymphopenia, naive CD4^+^ T‑cell deficiency, recurrent infections, EBV‑associated lymphoproliferation, epidermodysplasia verruciformis, bronchiectasis, and neurodevelopmental disorders in CNV contexts. GO terms capture coronin‑1A’s roles in actin filament binding, regulation of actin polymerization, immune synapse formation, T‑cell migration, and survival. CL terms highlight affected cell types (naive T cells, NKT, MAIT, B cells, NK cells), and UBERON terms delineate involved organs (thymus, lymph nodes, spleen, lungs, skin).

Despite substantial mechanistic insight from mouse models and human case series, gaps remain, particularly in large‑scale molecular profiling, epigenetic characterization, and long‑term outcome studies. Future research should extend single‑cell transcriptomics, proteomics, and functional genomics to coronin‑1A–deficient lymphocytes, explore gene therapy approaches, and better define prognostic biomarkers and treatment algorithms. As SCID newborn screening becomes universal and genomic medicine more accessible, early identification and intervention for CORO1A deficiency will improve, transforming this once‑fatal immunodeficiency into a manageable condition with curative potential for many patients.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 80 |
| Resolved | 73 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 2 |
| Unverifiable | 3 |
| Terms whose name was checked | 39 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 22 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0008069` (1 mention) - the report calls it "T‑cell lymphopenia"; HP calls it **Neoplasm of the skin**
- `HP:0005308` (1 mention) - the report calls it "CD4+ T‑cell lymphopenia"; HP calls it **Pulmonary artery vasoconstriction**
- `HP:0031494` (1 mention) - the report calls it "Naive CD4+ T‑cell deficiency"; HP calls it **Ovarian mucinous tumor**
- `HP:0031520` (1 mention) - the report calls it "Naive T‑cell deficiency"; HP calls it **Groin pain**
- `HP:0005348` (1 mention) - the report calls it "NK‑cell lymphopenia"; HP calls it **Inspiratory stridor**
- `HP:0002721` (1 mention) - the report calls it "Abnormal B‑cell count"; HP calls it **Immunodeficiency**
- `HP:0004430` (1 mention) - the report calls it "Impaired antibody response to vaccination"; HP calls it **Severe combined immunodeficiency**
- `HP:0002729` (2 mentions) - the report calls it "Abnormal lymphocyte proliferation"; HP calls it **Follicular hyperplasia**
- `HP:0002725` (1 mention) - the report calls it "Immunodeficiency"; HP calls it **Systemic lupus erythematosus**
- `HP:0002733` (2 mentions) - the report calls it "Lymphoproliferative disorder"; HP calls it **Abnormal lymph node morphology**
- `HP:0100085` (1 mention) - the report calls it "Chronic active EBV infection"; HP calls it **Small epiphyses of the 5th toe**
- `HP:0000998` (2 mentions) - the report calls it "Epidermodysplasia verruciformis"; HP calls it **Hypertrichosis**
- `HP:0009740` (1 mention) - the report calls it "Molluscum contagiosum"; HP calls it **Aplasia of the parotid gland**
- `HP:0001657` (1 mention) - the report calls it "Recurrent herpes simplex infections"; HP calls it **Prolonged QT interval**
- `HP:0002728` (1 mention) - the report calls it "Opportunistic infections"; HP calls it **Recurrent mucocutaneous candidiasis**
- `HP:0002826` (1 mention) - the report calls it "Leprosy"; HP calls it **Halberd-shaped pelvis**
- `HP:0004370` (1 mention) - the report calls it "B‑cell lymphoma"; HP calls it **Abnormality of temperature regulation**
- `HP:0002758` (1 mention) - the report calls it "Recurrent bacterial infections"; HP calls it **Osteoarthritis**
- `HP:0001581` (1 mention) - the report calls it "Flat wart"; HP calls it **Recurrent skin infections**
- `HP:0001014` (1 mention) - the report calls it "Pityriasis versicolor"; HP calls it **Angiokeratoma**
- `HP:0002762` (1 mention) - the report calls it "Non‑melanoma skin cancer"; HP calls it **Multiple exostoses**
- `HP:0000737` (1 mention) - the report calls it "Autism"; HP calls it **Irritability**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0002746` (2 mentions), reported as "Lymphoma" - HP does not contain this term
- `HP:0008408` (1 mention), reported as "Epstein–Barr virus infection" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0051270` (obsolete regulation of cellular component movement) (1 mention)
- `GO:0042089` (GO_0042089) (1 mention) - replaced by `GO:0001816`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002715` (2 mentions) - the report calls it "Abnormal immunoglobulin level"; HP calls it **Abnormality of the immune system**
- `HP:0002718` (1 mention) - the report calls it "Recurrent infections"; HP calls it **Recurrent bacterial infections**, and lists "Recurrent pyogenic infections" among its other names
- `HP:0002205` (1 mention) - the report calls it "Recurrent upper respiratory tract infections"; HP calls it **Recurrent respiratory infections**
- `HP:0000388` (1 mention) - the report calls it "Recurrent otitis media"; HP calls it **Otitis media**
- `HP:0001875` (1 mention) - the report calls it "Neutropenia"; HP calls it **Decreased total neutrophil count**, and lists "Neutropenia" among its other names
- `GO:0051270` (1 mention) - the report calls it "regulation of T‑cell migration"; GO calls it **obsolete regulation of cellular component movement**, and lists "regulation of cell movement" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.