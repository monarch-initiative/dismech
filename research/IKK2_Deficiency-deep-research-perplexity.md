---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-03T14:14:00.351408'
end_time: '2026-09-03T14:17:44.225048'
duration_seconds: 223.87
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: IKK2 Deficiency
  mondo_id: ''
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
citation_count: 46
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 11
  validator_version: 0.2.1
term_validation:
  total_terms: 53
  verified: 47
  not_found: 2
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.04
  labels_checked: 28
  labels_matching: 10
  labels_mismatched: 15
  mislabelled_terms:
  - term_id: HP:0002715
    reported_labels:
    - recurrent infections
    ontology_label: Abnormality of the immune system
  - term_id: HP:0005347
    reported_labels:
    - failure to thrive
    ontology_label: Tracheal cartilaginous sleeve
  - term_id: NCIT:C3107
    reported_labels:
    - Severe Combined Immunodeficiency
    ontology_label: Langerhans Cell Histiocytosis
  - term_id: HP:0000028
    reported_labels:
    - agammaglobulinemia
    ontology_label: Cryptorchidism
  - term_id: HP:0002019
    reported_labels:
    - diarrhea
    ontology_label: Constipation
  - term_id: HP:0002104
    reported_labels:
    - hepatosplenomegaly
    ontology_label: Apnea
  - term_id: HP:0000989
    reported_labels:
    - eczema/dermatitis
    ontology_label: Pruritus
  - term_id: NCIT:C15313
    reported_labels:
    - "Anti\u2011infective Agent"
    ontology_label: Radiation Therapy
  - term_id: NCIT:C574
    reported_labels:
    - Immune Globulin
    ontology_label: Immunosuppressant
  - term_id: NCIT:C15206
    reported_labels:
    - Hematopoietic Stem Cell Transplantation
    ontology_label: Clinical Study
  - term_id: NCIT:C15273
    reported_labels:
    - Bone Marrow Transplantation
    ontology_label: Longitudinal Study
  - term_id: NCIT:C28776
    reported_labels:
    - Antibiotic Therapy
    ontology_label: (H115D)VHL35 Peptide
  - term_id: NCIT:C66807
    reported_labels:
    - Antifungal Therapy
    ontology_label: Benign Ciliary Body Medulloepithelioma
  - term_id: NCIT:C28863
    reported_labels:
    - Antiviral Therapy
    ontology_label: Benzonatate
  - term_id: NCIT:C94128
    reported_labels:
    - Prophylactic Antibiotic
    ontology_label: Study Recruitment Status Code
  labels_variant: 3
  unresolved_terms:
  - HP:0004314
  - HP:0003379
  obsolete_terms:
  - term_id: GO:0008341
    ontology_label: obsolete response to cocaine (sensu Insecta)
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
- **Disease Name:** IKK2 Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **IKK2 Deficiency** covering all of the
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

# Severe Combined Immunodeficiency due to IKK2 Deficiency (IKBKB-associated Immunodeficiency)

Severe combined immunodeficiency due to IKK2 deficiency is a rare autosomal recessive primary immunodeficiency caused by biallelic loss-of-function variants in the *IKBKB* gene, encoding the IκB kinase-β (IKK2) subunit of the canonical NF‑κB signaling complex.[3][12][31] Patients present in early infancy with life‑threatening bacterial, viral, fungal, and mycobacterial infections, failure to thrive, profound hypogammaglobulinemia or agammaglobulinemia, and impaired activation of both innate and adaptive immune cells despite near‑normal numbers of T and B lymphocytes.[4][18][25] Functional studies have shown that IKK2 deficiency abrogates NF‑κB activation downstream of antigen receptors, pattern‑recognition receptors, and cytokine receptors, leading to a form of combined immunodeficiency that is at least as severe as classical severe combined immunodeficiency (SCID) but often escapes standard newborn screening based on T‑cell receptor excision circles (TREC).[4][18][20] The most extensively studied founder variant, a homozygous c.1292dupG duplication in exon 13 of *IKBKB*, produces a frameshift (p.Gln432ProfsTer62) with complete loss of IKKβ expression and is associated with high mortality in early infancy unless urgent hematopoietic stem cell transplantation (HSCT) is performed.[14][4][18] This report synthesizes clinical, genetic, mechanistic, and therapeutic knowledge on IKK2 deficiency, integrates ontology annotations (MONDO, HPO, GO, CL, UBERON, NCIT), and contrasts biallelic loss‑of‑function disease with monoallelic gain‑of‑function *IKBKB*–related immunodeficiency to delineate the disease spectrum.

## 1. Disease Information

### 1.1 Definition and Core Description

Severe combined immunodeficiency due to IKK2 deficiency, often referred to as *IKBKB immune deficiency*, *combined immunodeficiency due to IKBKB deficiency*, or *Immunodeficiency‑15B (IMD15B)*, is a Mendelian primary immunodeficiency characterized by profound defects in both innate and adaptive immune activation caused by loss of function of the serine/threonine kinase IKK2, encoded by *IKBKB*.[3][12][25] Orphanet classifies “Combined immunodeficiency due to IKBKB deficiency” as a rare genetic form of primary immunodeficiency with onset in infancy, life‑threatening bacterial, fungal and viral infections, failure to thrive, and hypogammaglobulinemia or agammaglobulinemia despite normal levels of T and B cells.[25][31] MedGen and MalaCards describe Immunodeficiency‑15B (IMD15B; OMIM 615592) as an autosomal recessive primary immunodeficiency with hypo‑ or agammaglobulinemia, relatively normal B and T cell numbers, and impaired differentiation and activation of immune cells.[12][39][40]

The landmark New England Journal of Medicine study by Pannicke et al. (2013, PMID 24369075) defined the human disease entity by identifying a homozygous *IKBKB* frameshift variant in Cree infants with life‑threatening infections, hypogammaglobulinemia, and profoundly naive T‑ and B‑cell phenotypes.[4][14] The authors wrote:

> “All patients carried a homozygous duplication—c.1292dupG in exon 13 of IKBKB, which encodes IκB kinase 2 (IKK2, also known as IKKβ)—leading to loss of expression of IKK2, a component of the IKK–nuclear factor κB (NF‑κB) pathway. Immune cells from the patients had impaired responses to stimulation through T‑cell receptors, B‑cell receptors, toll‑like receptors, inflammatory cytokine receptors, and mitogens.”[4]

This description emphasizes that the core lesion is a signaling defect, not a developmental block, distinguishing IKK2 deficiency from typical SCID entities characterized by lymphopenia or complete absence of T cells.[4][18][31]

### 1.2 Key Identifiers and Ontology Codes

The disease is represented in multiple biomedical ontologies and clinical coding systems:

Orphanet (ORPHA:397787) lists “Combined immunodeficiency due to IKBKB deficiency” as a distinct entity, with prevalence <1/1,000,000, autosomal recessive inheritance, and ICD‑10 code D81.8 (other combined immunodeficiencies).[25] MedGen and Orphanet link the same phenotype to OMIM entry 615592 (“Immunodeficiency‑15B”), which is designated as “Severe combined immunodeficiency due to IKK2 deficiency” in ClinVar.[28][31][41] ClinVar and MedGen explicitly associate this condition with MONDO:0014267 (“severe combined immunodeficiency due to IKK2 deficiency”), providing the requested MONDO identifier for IKK2 deficiency.[28][31]

The *IKBKB* gene itself carries OMIM gene entry 603258, cytogenetic location 8p11.21, and is annotated as “inhibitor of nuclear factor kappa B kinase subunit beta.”[3] Genomics England PanelApp and Gene2Phenotype recognize *IKBKB* as causally associated with “Immunodeficiency 15B” (autosomal recessive) and “Immunodeficiency 15A” (autosomal dominant).[3][15][6] These identifiers support mapping of the disease into Mendelian disease catalogs and variant databases.

Relevant ontology suggestions include MONDO:0014267 (severe combined immunodeficiency due to IKK2 deficiency), HP:0004430 (combined immunodeficiency), HP:0002715 (recurrent infections), HP:0004314 (hypogammaglobulinemia), HP:0005347 (failure to thrive), and NCIT:C3107 (Severe Combined Immunodeficiency).[31][25]

### 1.3 Synonyms and Alternative Names

The condition appears under several overlapping names in different resources and publications, reflecting its dual classification as a combined immunodeficiency and as Immunodeficiency‑15B:

Orphanet and MedGen use “Combined immunodeficiency due to IKBKB deficiency” and “severe combined immunodeficiency due to IKK2 deficiency” to emphasize the clinical severity and molecular cause.[25][31] OMIM entry 615592 and MalaCards use “Immunodeficiency‑15B (IMD15B)” and “Immunodeficiency 15; IMMUNODEFICIENCY 15B” for the autosomal recessive form.[12][12][39] The NEJM article and subsequent case series often refer to “IKBKB immune deficiency” or “IKK2 deficiency” as shorthand.[14][4][18] Genomics Education resources adopt “IKBKB‑associated immunodeficiency” for the broader spectrum including biallelic loss‑of‑function and monoallelic gain‑of‑function variants.[20][20]

Common synonyms therefore include: *IKBKB immune deficiency*, *IKK2 deficiency*, *Immunodeficiency‑15B*, *combined immunodeficiency due to IKBKB deficiency*, and *severe combined immunodeficiency due to IKK2 deficiency*.[12][25][31] These terms should be cross‑referenced in disease knowledge bases to ensure interoperability across datasets.

### 1.4 Nature of Source Information

The current understanding of IKK2 deficiency is derived primarily from aggregated case series and molecular studies in small numbers of patients, rather than from large electronic health record (EHR) cohorts.[14][4][18][18] The original description by Pannicke et al. analyzed four Cree infants extensively at the clinical, immunologic, and genetic levels, including functional studies on patient cells.[4] Subsequent expansions of the cohort to sixteen patients with the same founder mutation provided more detailed natural history, immunologic characterization, and HSCT outcomes.[14][18][18] A recent comprehensive review of *IKBKB* mutations and related immunodeficiencies compiled fifteen distinct variants and summarized their clinical and laboratory features.[7][11][7]

These aggregated disease‑level resources are complemented by curated entries in OMIM, Orphanet, MedGen, ClinVar, and Genomics England PanelApp, which synthesize findings across published reports.[3][12][15][6][25][31] No large administrative or EHR‑based epidemiologic datasets exist for this ultra‑rare disorder, and prevalence estimates (<1/1,000,000) rely on expert opinion and registry‑type data rather than systematic population surveillance.[25] Thus, evidence for disease definition, mechanism, and prognosis is anchored in primary case reports and mechanistic immunology rather than in big‑data clinical analytics.

## 2. Etiology

### 2.1 Genetic Causal Factors

The primary cause of IKK2 deficiency is germline biallelic loss‑of‑function mutations in the *IKBKB* gene on chromosome 8p11.21, inherited in an autosomal recessive pattern.[3][12][15] *IKBKB* encodes IκB kinase‑β (IKK2), a serine/threonine kinase that forms part of the trimeric IKK complex (IKKα/CHUK, IKKβ/IKBKB, and NEMO/IKBKG) responsible for phosphorylating IκB inhibitors of NF‑κB and thereby enabling NF‑κB nuclear translocation.[2][32][34][35] Loss‑of‑function alleles in *IKBKB* abolish or drastically reduce IKK2 protein expression, leading to failure of canonical NF‑κB activation downstream of multiple immune receptors.[4][7][20]

The best‑characterized causal variant is a homozygous duplication c.1292dupG in exon 13 of *IKBKB*, causing a frameshift and premature termination (p.Gln432ProfsTer62) with loss of most of the alpha‑helical scaffold dimerization domain.[13][14][4] ClinVar describes this variant in four Cree patients and notes that it results in complete loss of IKKβ expression.[13][4] The NEJM abstract explicitly states:

> “All patients carried a homozygous duplication—c.1292dupG in exon 13 of IKBKB, which encodes IκB kinase 2 (IKK2, also known as IKKβ)—leading to loss of expression of IKK2.”[4]

Additional pathogenic loss‑of‑function variants include nonsense mutations (e.g., c.814C>T, p.R272X), frameshift variants, and splice‑site changes, all leading to markedly reduced or absent IKKβ protein and severe combined immunodeficiency.[7][14] A recent review enumerated fifteen *IKBKB* mutations associated with immune deficiency, of which eight were clearly loss‑of‑function, four had unknown functional status, and three were gain‑of‑function.[7] Biallelic truncating variants are responsible for the prototypical early‑onset, life‑threatening phenotype that constitutes IKK2 deficiency.[20][7][20]

Ontology suggestions for etiology include HGNC:10682 (*IKBKB*), GO:0007249 (I‑kappaB kinase/NF‑kappaB signaling), and MONDO:0014267 (severe combined immunodeficiency due to IKK2 deficiency).[3][32][34][31]

### 2.2 Non‑Genetic Causal Factors and Environmental Modifiers

IKK2 deficiency is fundamentally a monogenic Mendelian disorder; no environmental exposures have been identified as primary causal agents.[12][25][31] However, environmental factors strongly modulate disease expression and clinical course, particularly infectious exposures and social determinants of health. The Genomics Education Knowledge Hub notes that affected infants often develop severe infections with bacterial, viral, fungal, and mycobacterial pathogens, including opportunistic infections and vaccine‑strain disease after live vaccines such as BCG.[20][20] These infections are triggers rather than causes, revealing the underlying immunodeficiency.

The Cree founder cohort described by Pannicke et al. and later expanded by Cardinez and colleagues showed that infection burden and access to specialised care significantly influenced survival and HSCT outcomes.[14][18][18] The case series on HSCT outcomes highlighted that ongoing infections, poor social determinants of health, secondary graft failure, and failure of HSCT to correct non‑hematopoietic NF‑κB–dependent functions contributed to poor prognosis.[18][18][29] Thus, environmental factors such as pathogen exposure, vaccine practices, and healthcare access act as modulators of mortality and morbidity in genetically determined IKK2 deficiency.

No specific chemical toxins, radiation exposures, or lifestyle factors have been implicated as risk factors or protective factors for developing IKK2 deficiency, because the disease arises from inherited biallelic variants and displays ultra‑rare prevalence.[25][31] Nonetheless, standard hygiene, infection control practices, and prophylactic antimicrobial measures may reduce risk of severe infections and thereby partially modify disease trajectory.[20][20]

### 2.3 Genetic Risk Factors Beyond Causal Variants

Within the Mendelian framework, risk is determined largely by carrier status for pathogenic *IKBKB* variants. Autosomal recessive biallelic loss‑of‑function disease (IMD15B) manifests when an individual inherits pathogenic alleles from both parents, whereas heterozygous carriers are typically asymptomatic with respect to severe combined immunodeficiency, although they could be at risk for other NF‑κB–related phenotypes depending on the specific variant.[15][20][7] Founder effects have been documented in Cree populations in Canada, where the c.1292dupG variant shows a high carrier frequency within certain communities.[13][14][18] Pannicke et al. reported four patients of Cree ancestry with this homozygous duplication, and subsequent series extended this to at least sixteen infants, suggesting a significant founder effect in this population.[14][18][18]

Genomics England PanelApp and ClinVar records show that *IKBKB* variants may be inherited in both autosomal recessive and autosomal dominant fashions, reflecting loss‑of‑function versus gain‑of‑function effects.[15][6][44] Heterozygous gain‑of‑function variants, such as c.607G>A (p.V203I) in the kinase domain, are associated with Immunodeficiency‑15A (IMD15A), a distinct phenotype characterized by immune dysregulation, autoimmunity, episodic fevers, and later‑onset combined immunodeficiency.[21][3][44] Although this is not IKK2 deficiency in the strict sense, it illustrates that the same gene contributes to a broader risk landscape for NF‑κB–related disorders.

Other genetic modifiers, such as variants in *IKBKG* (NEMO), *CHUK* (IKKα), or NF‑κB pathway components, may theoretically modulate phenotype severity, but direct evidence in humans with IKK2 deficiency is currently lacking.[2][7][32] Existing data do not support polygenic risk scores or genome‑wide association signals for this ultra‑rare monogenic disease.[25][31]

### 2.4 Protective Factors and Gene–Environment Interactions

Explicit protective genetic factors have not been identified for IKK2 deficiency; heterozygous carriers may simply be non‑affected due to recessive inheritance.[15][20] It is possible that residual expression from hypomorphic alleles, rather than amorphic null alleles, confers partial protection by allowing limited NF‑κB activation, yielding milder phenotypes or survival into later childhood with extensive supportive treatment.[7][20] The review by Ahamad et al. notes that patients with mutations causing reduced but not absent IKKβ expression may live poorly with frequent hospitalization and extensive therapy rather than dying in infancy, implying a gradation of protective effect based on allele functionality.[7][7]

Environmental protective factors are largely inferred rather than systematically studied. Early diagnosis and avoidance of live vaccines such as BCG or measles, combined with rigorous infection prophylaxis (e.g., antimicrobial prophylaxis, immunoglobulin replacement, protective isolation), are presumed to reduce morbidity and mortality.[20][20] In the HSCT case series, early transplantation before overwhelming infections had occurred was associated with better survival, suggesting that timing of intervention is a critical protective factor.[18][18][29] Conversely, high pathogen exposure in resource‑limited environments may exacerbate disease course.

Gene–environment interactions in IKK2 deficiency thus revolve around how the genetically determined signaling defect interacts with infectious exposures and clinical management. For example, vaccine‑strain BCG infection following neonatal vaccination, as described in patients with *IKBKB* loss‑of‑function, demonstrates that the combination of genetic impairment of NF‑κB activation and live attenuated mycobacterial exposure leads to severe disseminated disease.[20][7] This supports counseling against live vaccines in infants suspected of having IKK2 deficiency and highlights GO:0006955 (immune response) and CHEBI identifiers for vaccine components as relevant ontology elements.

## 3. Phenotypes

### 3.1 Overview of Clinical Presentation and Symptom Types

IKK2 deficiency manifests as a severe combined immunodeficiency with predominantly infectious and failure‑to‑thrive phenotypes. Orphanet summarises the clinical picture as life‑threatening bacterial, fungal and viral infections with onset in infancy, failure to thrive, and hypogammaglobulinemia or agammaglobulinemia despite normal T‑ and B‑cell counts.[25] MedGen and MalaCards similarly describe recurrent, severe infections, failure to thrive, impaired immune cell differentiation and activation, and hypo‑ or agammaglobulinemia.[12][12][39]

Ahamad et al. systematically reviewed fifteen reported *IKBKB*‑mutated cases and noted that loss‑of‑function mutations cause severe combined immunodeficiency with early‑onset, life‑threatening infections, broad microbial spectrum (bacterial, viral, fungal, mycobacterial), hypogammaglobulinemia, and defects in T and B cell function despite normal numbers.[7][7] The authors state:

> “The reported immunodeficient cases with mutations in IKBKB were genetically and clinically heterogeneous with loss‑of‑function mutations causing severe CID, displaying common characteristics including absence or reduction of IKKβ, defects in T and B cell function despite normal numbers in most cases, compromised innate and acquired immunity, frequent microbial infections (fungal, viral, bacterial and mycobacterial) and hypogammaglobulinemia… These symptoms occur early in life, and death can occur within months.”[7]

The Cree cohort case series further documented opportunistic infections (e.g., *Pneumocystis jirovecii*), vaccine‑strain BCG disease, chronic diarrhea, hepatosplenomegaly, and dermatitis.[18][20][18] Clinical signs thus include recurrent pneumonia, sepsis, skin infections, lymphadenopathy, organomegaly, and malnutrition. Laboratory abnormalities involve hypogammaglobulinemia or agammaglobulinemia, profoundly naive T‑ and B‑cell phenotypes, absence of regulatory T cells and γδ T cells, impaired lymphocyte proliferation, and reduced NK cell counts.[4][18][20][20]

Ontology suggestions for phenotypes include HP:0002715 (recurrent infections), HP:0005347 (failure to thrive), HP:0004314 (hypogammaglobulinemia), HP:0000028 (agammaglobulinemia), HP:0004430 (combined immunodeficiency), HP:0002090 (pneumonia), HP:0002019 (diarrhea), HP:0002104 (hepatosplenomegaly), HP:0000989 (eczema/dermatitis), and HP:0003379 (opportunistic infections).[25][7][20]

### 3.2 Age of Onset, Severity, and Progression

IKK2 deficiency is invariably an early‑onset disease. Orphanet specifies age of onset in infancy, and MedGen summarises IMD15B as having onset in infancy with life‑threatening infections and failure to thrive.[25][39][40] Ahamad et al. report that symptoms occur early in life, often within the first months, and that death commonly occurs within months if untreated.[7] For instance, a Turkish infant with a nonsense *IKBKB* mutation (p.R272X) developed respiratory and uncontrolled systemic mycobacterial infections after BCG vaccination at five months of age and died at 14 months.[7] The Cree founder patients presented in the first months with severe infections, and the median age at diagnosis in expanded cohorts was well under one year.[14][18][18]

Severity is consistently rated as “severe” or “life‑threatening.” Orphanet and Orphanet‑linked MedGen emphasize life‑threatening bacterial, fungal, and viral infections; the Genomics Education Knowledge Hub describes the autosomal recessive disease as “rare, autosomal recessive life‑threatening primary immunodeficiency.”[20][25][20] Clinical series highlight profound hypogammaglobulinemia, frequent sepsis, disseminated mycobacterial disease, and opportunistic infections, underscoring the severity of immune compromise.[4][18][7]

Symptom progression is typically rapid and progressive rather than stable. Infants accumulate recurrent and severe infections, fail to thrive, and often experience worsening organ dysfunction, including chronic lung disease and enteropathy.[18][18][7] Without curative intervention, most patients die in early infancy from overwhelming infection and complications.[7][7][31] HSCT can alter progression, but even post‑transplant, complications such as graft failure, persistent infections, and non‑hematopoietic NF‑κB–related manifestations may persist.[18][18][29]

### 3.3 Frequency and Spectrum of Phenotypes among Affected Individuals

Because of the small number of reported cases, precise quantitative frequencies of individual phenotypes are difficult to establish, but consistent patterns emerge across case series and reviews.[14][18][18][7] In the sixteen‑patient Cree cohort, early‑onset bacterial, viral, fungal, and mycobacterial infections were universal, suggesting a frequency approaching 100% for severe recurrent infections.[14][18][14] Hypogammaglobulinemia or agammaglobulinemia was documented in most patients; T‑ and B‑cell counts were generally normal but phenotypically naive, implying near‑universal combined functional immunodeficiency.[4][18][14] Regulatory T cells and γδ T cells were absent in all patients studied in detail, indicating a consistent immunophenotypic hallmark.[4]

Failure to thrive appears in nearly all reported infants, reflecting chronic infection, malabsorption, and systemic illness.[25][7][31] Opportunistic infections, including *Pneumocystis jirovecii* pneumonia and disseminated BCG, are common, though exact prevalence varies by geographic region and vaccination practices.[20][7][20] Chronic diarrhea and hepatosplenomegaly are frequently described, alongside dermatologic manifestations such as dermatitis.[20][18] Neurologic complications are less prominent than in some other primary immunodeficiencies, but can occur secondary to infections or metabolic disturbances.[18][18][29]

Ahamad et al. emphasise that patients with loss‑of‑function *IKBKB* mutations are genetically and clinically heterogeneous but share the core pattern of severe, early‑onset combined immunodeficiency with broad infectious susceptibility and hypogammaglobulinemia.[7] Thus, while there may be variation in specific infections and organ involvement, the hallmark phenotype of life‑threatening infections in infancy and severe humoral and cellular activation defects is consistent.

### 3.4 Quality of Life Impact

Although formal quality‑of‑life measures (e.g., EQ‑5D, SF‑36) have not been systematically applied to infants with IKK2 deficiency, the clinical descriptions clearly indicate profound impairment of daily functioning and well‑being.[14][18][18][7] Infants with severe combined immunodeficiency due to IKK2 deficiency experience repeated hospitalisations, prolonged intensive care stays, invasive procedures (e.g., mechanical ventilation, central venous lines), and chronic exposure to multiple antimicrobials.[18][18][29] Failure to thrive reflects inadequate growth and nutrition, likely impacting neurodevelopment and physical development even in survivors.[25][7]

Families face psychological and socioeconomic burdens arising from repeated life‑threatening episodes, uncertainty about HSCT outcomes, and the need for complex, specialized care.[18][18] Post‑transplant survivors often have chronic health issues, including graft‑related complications, residual immunodeficiency, and potential NF‑κB–related non‑immune manifestations, necessitating ongoing medical follow‑up.[18][18][29] Thus, the disease imposes severe morbidities and disability, aligning with HP:0004430 (combined immunodeficiency) and ICF (International Classification of Functioning) categories of major activity limitation.

Genomics Education notes that patients may have chronic diarrhea, hepatosplenomegaly, dermatitis, and recurrent infections, all of which significantly affect daily functioning.[20][20] The need to avoid environmental exposures, live vaccines, and infections further constrains normal life. In knowledge bases, this disease should be flagged as causing high disability weights and critical quality‑of‑life impact.

## 4. Genetic and Molecular Information

### 4.1 Causal Genes and Loci

The causal gene for IKK2 deficiency is *IKBKB* (HGNC:10682), located on chromosome 8p11.21, with genomic coordinates X:42,271,302–42,332,460 (GRCh38).[3][9] *IKBKB* encodes inhibitor of nuclear factor kappa‑B kinase subunit beta (IKK2/IKKβ), a serine/threonine kinase that forms part of the canonical IKK complex.[8][9] The OMIM gene entry 603258 lists *IKBKB* as causally associated with Immunodeficiency‑15A (autosomal dominant) and Immunodeficiency‑15B (autosomal recessive).[3][15] Genomics England PanelApp and Gene2Phenotype confirm *IKBKB* as implicated in primary immunodeficiency and monogenic inflammatory bowel disease panels.[6][10]

The broader NF‑κB signaling complex includes *CHUK* (IKKα) and *IKBKG* (NEMO), whose mutations cause related but distinct immunodeficiency and ectodermal dysplasia syndromes.[2][5][24][42] However, severe combined immunodeficiency due to IKK2 deficiency is specifically attributable to loss‑of‑function mutations in *IKBKB*.[12][25][31]

### 4.2 Pathogenic Variant Spectrum, Classification, and Functional Consequences

Pathogenic variants causing IKK2 deficiency predominantly consist of truncating alleles—frameshift, nonsense, splice‑site, and untranslated region variants—that lead to absence or drastic reduction of IKKβ protein.[14][4][7][20] The c.1292dupG frameshift variant in exon 13 (p.Gln432ProfsTer62) is the most extensively characterised; ClinVar labels it as pathogenic for Immunodeficiency‑15B based on literature only, and Pannicke et al. demonstrated complete loss of IKK2 expression and NF‑κB activation in patient cells.[13][4] The NEJM abstract reads:

> “This duplication… leading to loss of expression of IKK2, a component of the IKK–nuclear factor κB (NF‑κB) pathway.”[4]

Other loss‑of‑function variants include nonsense mutation c.814C>T (p.R272X) reported in a Turkish infant, which resulted in normal T‑ and B‑cell numbers but impaired functions, hypogammaglobulinemia, and fatal infections.[7][14] Ahamad et al. list at least eight loss‑of‑function mutations, including nonsense, frameshift, and splice‑site changes, with consistent clinical phenotypes.[7]

Variant classification follows ACMG/AMP guidelines in ClinVar and ClinGen. The c.1292dupG variant is curated as pathogenic for IMD15B.[13][7] Conversely, some missense changes, such as c.742G>C (p.Asp248His, mis‑mapped as D184H in some records), currently have insufficient evidence and are classified as variants of uncertain significance (VUS) for severe combined immunodeficiency due to IKK2 deficiency.[28][28] ClinVar explicitly states:

> “In summary, the available evidence is currently insufficient to determine the role of this variant in disease. Therefore, it has been classified as a Variant of Uncertain Significance.”[28]

In contrast to loss‑of‑function variants, heterozygous gain‑of‑function missense mutations, such as c.607G>A (p.Val203Ile) in the kinase domain, are pathogenic for Immunodeficiency‑15A and cause a different phenotype with combined immune deficiency, autoimmunity, and epithelial defects.[21][3][44] Cardinez et al. demonstrated that this missense mutation results in enhanced NF‑κB signaling and T/B‑cell functional defects; experimental studies confirmed gain of function and ClinVar lists this variant as pathogenic for IMD15A.[21][44][45] Thus, functional consequences can be categorised as:

Loss of function (biallelic, autosomal recessive): absence or severe reduction of IKKβ protein, impaired NF‑κB activation, severe combined immunodeficiency.[4][7][31]

Gain of function (monoallelic, autosomal dominant): enhanced NF‑κB signaling, immune dysregulation, autoimmunity, later‑onset combined immunodeficiency.[21][3][36][44]

For IKK2 deficiency, the relevant category is loss‑of‑function, with complete loss of kinase activity and canonical pathway activation.[4][7][20] UniProt and Reactome annotate IKKβ as catalyzing phosphorylation of IκBα on Ser32 and Ser36 and IκBβ on Ser19 and Ser22, leading to ubiquitination and degradation; loss‑of‑function variants abolish this biochemical activity.[34][35]

Allele frequencies for pathogenic *IKBKB* variants are extremely low in population databases such as gnomAD, consistent with their severe phenotypic consequences, though detailed frequency data are not presented in the provided search results.[7] Orphanet estimates prevalence of the disease at <1/1,000,000.[25]

### 4.3 Germline versus Somatic Origin

All reported pathogenic *IKBKB* variants associated with IKK2 deficiency are germline, inherited in an autosomal recessive manner.[12][25][31] ClinVar entries for c.1292dupG and c.607G>A note germline origin and interpret them in the context of primary immunodeficiency, not somatic oncology.[13][44] No somatic or acquired *IKBKB* mutations have been implicated in this disease entity, although *IKBKB* variants may contribute to oncogenesis or inflammatory conditions in other contexts.[8][32][37]

The gain‑of‑function c.607G>A (p.V203I) variant in IMD15A is often de novo germline, arising in probands without family history, but is still a constitutional mutation present in all cells.[21][3][44] There is no evidence of mosaicism or somatic mutational heterogeneity in the published IKK2 deficiency cases.[14][4][7]

### 4.4 Modifier Genes and Epigenetic Information

Direct evidence for modifier genes altering severity or expression of IKK2 deficiency is lacking in current human case series.[7][31] Theoretically, variants in NF‑κB pathway components (e.g., *IKBKG*, *CHUK*, *NFKBIA*, *REL*, *NFKB1*, *NFKB2*) could modulate residual signaling, but no systematic genotype‑modifier correlations have been reported.[32][33][34] The variability in HSCT outcomes among patients with the same *IKBKB* mutation is more plausibly attributed to clinical factors (infection status, conditioning regimen, donor type) than to genetic modifiers.[18][18][29]

Similarly, epigenetic changes (DNA methylation, histone modification) have not been studied specifically in IKK2 deficiency patients. NF‑κB activity influences chromatin accessibility and transcriptional programmes, but the primary lesion in this disease is upstream kinase deficiency rather than downstream epigenetic alteration.[32][34][35] Consequently, knowledge bases should mark epigenetic information as not yet available for this disease.

### 4.5 Chromosomal Abnormalities

No large‑scale chromosomal abnormalities (e.g., aneuploidy, translocations, inversions) have been described as causal or contributory to IKK2 deficiency. The disease arises from sequence‑level variants within *IKBKB* on chromosome 8p11.21.[3][9][12] DECIPHER, dbVar, and similar structural variation databases have not been implicated in this context based on available search results. Thus, chromosomal abnormalities can be categorized as not applicable for the core etiology of IKK2 deficiency.

## 5. Mechanism and Pathophysiology

### 5.1 Ordered Causal Chain from Mutation to Clinical Manifestations

1. Biallelic loss‑of‑function mutations in the *IKBKB* gene lead to absence or severe reduction of IKK2 (IKKβ) kinase protein expression in hematopoietic and non‑hematopoietic cells.[13][4][7]  
2. Loss of IKK2 results in failure of the canonical IKK complex to phosphorylate IκBα and IκBβ at critical serine residues, which normally tag these inhibitors for ubiquitin‑mediated degradation.[32][34][35]  
3. Persistent IκB inhibition prevents nuclear translocation of NF‑κB dimers (primarily p50/p65 and p52/RelB), leading to markedly impaired NF‑κB–dependent transcriptional responses to stimuli from T‑cell receptors, B‑cell receptors, toll‑like receptors, cytokine receptors, and mitogens.[4][32][33]  
4. This failure of NF‑κB activation causes defective activation, differentiation, and effector function of T cells, B cells, NK cells, and myeloid cells, despite largely normal lymphocyte development and cell numbers in the periphery.[4][18][7]  
5. Functionally naive and activation‑deficient lymphocytes result in hypogammaglobulinemia or agammaglobulinemia, absence of memory T and B cells, absence of regulatory T cells and γδ T cells, and compromised innate immune responses to microbial products.[4][18][7]  
6. The combined defects in innate and adaptive immunity lead to broad susceptibility to bacterial, viral, fungal, and mycobacterial infections, including opportunistic pathogens and vaccine‑strain organisms, with early‑onset life‑threatening infections.[4][18][20]  
7. Recurrent and severe infections in infancy cause failure to thrive, organ damage (e.g., chronic lung disease, hepatosplenomegaly, enteropathy), and high mortality, constituting a severe combined immunodeficiency phenotype that is at least as profound as classical SCID.[18][18][31]  
8. HSCT can correct hematopoietic cell NF‑κB signaling by providing donor‑derived IKK2‑expressing immune cells, but non‑hematopoietic tissues (e.g., intestinal epithelium) may retain IKK2 deficiency, potentially contributing to persistent inflammatory manifestations (this step is inferred from analogous *IKBKG* data and limited *IKBKB* experience).[18][18][29][30]  

### 5.2 Molecular Pathways: NF‑κB Signaling and IKK2 Function

The central molecular pathway implicated in IKK2 deficiency is the canonical NF‑κB signaling cascade. KEGG describes the NF‑κB pathway (hsa04064) as activated by tumour necrosis factor‑α (TNF‑α), interleukin‑1 (IL‑1), and microbial products, relying on IKK‑mediated phosphorylation of IκBα at Ser32 and Ser36 to trigger its degradation and allow p50/p65 NF‑κB dimers to enter the nucleus and activate gene transcription.[32] Reactome elaborates that the classical NF‑κB pathway involves an IKK complex composed predominantly of IKKβ (IKBKB) and IKKγ (IKBKG/NEMO), which phosphorylates IκBs at these serine sites, leading to ubiquitin‑mediated degradation.[34][35] Loss of IKKβ disrupts this key step, preventing release of NF‑κB from IκB and impairing downstream gene expression.

In T cells, NF‑κB activation downstream of the T‑cell receptor (TCR) involves the CBM (CARD11–BCL10–MALT1) complex, PKCθ, and the IKK complex, with IKKβ as the main catalytic subunit; NF‑κB controls transcription of cytokines, survival factors, and activation markers.[32][33][37] In B cells, B‑cell receptor (BCR) signaling through BTK, BLNK, and CD40 engages NF‑κB, again via IKKβ.[33][32] Innate immune receptors such as toll‑like receptor 4 (TLR4) signal through MyD88 and TRIF to activate NF‑κB via IKKβ.[32][33][37] Cytokine receptors (TNFR, IL‑1R) similarly converge on IKKβ.[32][34][35] Thus, IKK2 deficiency globally impairs NF‑κB activation across immune cell types.

Pannicke et al. demonstrated experimentally that immune cells from IKK2‑deficient patients had impaired responses to stimulation through TCRs, BCRs, toll‑like receptors, inflammatory cytokine receptors, and mitogens.[4] This broad signaling defect explains the combined innate and adaptive immune deficiency, supporting GO terms such as GO:0007249 (I‑kappaB kinase/NF‑kappaB signaling) and GO:0006955 (immune response).[32][34][35]

### 5.3 Cellular Processes: Lymphocyte Activation, Differentiation, and Apoptosis

At the cellular level, IKK2 deficiency affects multiple processes critical for immune function. T‑cell activation depends on NF‑κB‑mediated transcription of IL‑2 and other cytokines, as well as expression of activation markers (CD25, CD69) and costimulatory molecules (CD40L, CD70); loss of IKKβ prevents these transcriptional programmes, resulting in impaired proliferation and differentiation.[4][18][7] B‑cell activation and class‑switch recombination require NF‑κB activation downstream of CD40 and BCR; IKK2 deficiency impairs plasma cell differentiation and immunoglobulin production.[4][18][7][14] NK cell cytotoxicity and innate cytokine production (e.g., TNF‑α, IL‑6) also rely on NF‑κB, leading to defects in innate immune functions.[4][7][30]

Pannicke et al. found that peripheral‑blood B cells and T cells in patients were almost exclusively of naive phenotype, suggesting a block in memory cell generation rather than in lymphocyte development.[4] Regulatory T cells and γδ T cells were absent, indicating specific differentiation defects in these subsets.[4] Functional studies in affected patients showed impaired proliferation of T cells in response to mitogens, reduced antibody responses, and defective activation markers, consistent with GO:0042110 (T cell activation) and GO:0042113 (B cell activation).[18][18][7]

Apoptosis and cell survival are also influenced by NF‑κB, which up‑regulates anti‑apoptotic genes (e.g., BCL2 family, c‑IAPs).[37] While no direct evidence has been presented that IKK2 deficiency leads to increased lymphocyte apoptosis, the failure of NF‑κB–dependent survival signals may contribute to poor persistence of activated and memory cells. However, normal absolute lymphocyte counts suggest that development and baseline survival are preserved, and the dominant defect is activation rather than cell death.[4][18][7] Thus, cellular processes like activation, differentiation, and effector function are primarily compromised.

### 5.4 Protein Dysfunction: IKKβ Structural and Functional Changes

IKKβ is a serine/threonine kinase with an N‑terminal kinase domain, a leucine zipper region, and a C‑terminal helix–loop–helix structure involved in dimerization and complex assembly.[8][7][44] The c.1292dupG frameshift variant truncates the protein and removes most of the alpha‑helical scaffold dimerization domain, abrogating complex formation and kinase function.[13][4][7] Nonsense and frameshift variants similarly produce truncated proteins that are likely degraded via nonsense‑mediated decay, resulting in effective null alleles.[7][14][20]

Cardinez et al. analysed the p.V203I gain‑of‑function variant and showed that the mutant protein assumed an unstable conformation that disrupted tetrameric interaction while retaining kinase activity and even enhancing NF‑κB signaling, illustrating that subtle changes in structural domains can produce opposite functional outcomes.[21][44][45] This underscores the importance of precise residue context in the kinase domain.

In IKK2 deficiency, the functional consequence is loss of kinase activity, reduced phosphorylation of IκB, and failure to activate NF‑κB.[4][32][34] Reactome annotates that active IKBKB phosphorylates NF‑kappa‑B inhibitor (IκB), and the absence of active IKBKB prevents this step.[34][35] Thus, the protein dysfunction is best described as **loss of function**, with absence or severe reduction of enzymatic activity, and a consequent biochemical block in canonical NF‑κB activation.

### 5.5 Metabolic Changes and Biochemical Abnormalities

No specific metabolic derangements (e.g., energy metabolism, lipid metabolism) have been systematically reported as primary features of IKK2 deficiency. NF‑κB regulates a broad array of genes, including those involved in metabolism and cell survival, but the clinical phenotype of IKK2 deficiency centers on immunologic dysfunction.[32][37] Biochemical abnormalities are primarily immunologic (hypogammaglobulinemia, absent vaccine responses) rather than classic metabolic defects.[4][18][25]

Nonetheless, severe infections and failure to thrive may secondarily impair metabolism, leading to malnutrition, anemia, and electrolyte imbalances, though these are complications rather than defining biochemical signatures.[18][18][7] Thus, knowledge bases should note the absence of disease‑specific metabolic markers but highlight immunoglobulin deficiency (CHEBI: immunoglobulin G, A, M) as central biochemical abnormalities.

### 5.6 Immune System Involvement and Tissue Damage Mechanisms

IKK2 deficiency is fundamentally an immune system disease. Immune system involvement spans both innate and adaptive branches. T cells (CL:0000084), B cells (CL:0000236), NK cells (CL:0000623), monocytes (CL:0000576), and dendritic cells (CL:0000451) all show impaired activation and effector function due to defective NF‑κB signaling.[4][18][7] NK‑cell cytotoxicity and TLR‑mediated cytokine production are diminished, compromising innate defenses; T‑cell proliferation, cytokine production, and B‑cell help are impaired, undermining adaptive responses.[4][18][7][30]

Tissue damage occurs primarily as a consequence of recurrent infections and systemic inflammation. Chronic lung infections can lead to bronchiectasis and interstitial lung disease; chronic diarrhea may reflect enteropathy and gut inflammation; hepatosplenomegaly indicates sustained immune activation and infection burden.[18][20][18] Colitis and inflammatory bowel disease‑like pathology have been more prominently described in NEMO (IKBKG) deficiency than in IKK2 deficiency, but NF‑κB signaling in intestinal epithelial cells plays a key role in gut barrier function.[24][30][38] Mouse models where IKK2 is conditionally deleted or constitutively activated in intestinal epithelial cells (IECs) demonstrate that active IKK2 in IECs triggers colitis‑like pathology and bone loss, whereas IEC‑specific deletion attenuates colitis and bone loss in DSS‑induced colitis.[38] These findings suggest that IKK2 in IECs contributes to colitis‑associated osteopenia, and that intrinsic NF‑κB dysregulation in gut epithelium can drive inflammatory tissue damage.[38]

In IKK2 deficiency, the lack of NF‑κB activation in immune cells probably reduces inflammatory damage directly, but recurrent infections and microbial translocation may promote chronic inflammation and tissue injury. The balance between protection from excessive inflammation and susceptibility to infection determines tissue damage patterns.

### 5.7 Epigenetic Changes and Molecular Profiling

Specific epigenetic changes (DNA methylation, histone modifications) have not been described in IKK2 deficiency patients. However, NF‑κB activation normally recruits chromatin remodelers and histone acetyltransferases to target promoters; loss of NF‑κB may alter chromatin states indirectly.[32][34][37] In the absence of direct data, epigenetic mechanisms should be considered hypothetical and downstream rather than primary in disease pathophysiology.

Molecular profiling data (transcriptomics, proteomics, metabolomics) are limited for this rare disease. Pannicke et al. focused on functional assays (cytokine production, proliferation) rather than global -omics.[4] Ahamad et al. summarised biochemical and immunophenotypic data across cases but did not report large‑scale transcriptome or proteome studies.[7] Thus, knowledge bases may note that comprehensive -omics studies are currently unavailable for IKK2 deficiency.

### 5.8 Advanced Technologies and Functional Genomics

The most prominent functional genomics application in this field is the creation of a precise mouse model for the IKK2 V203I gain‑of‑function variant, using CRISPR/Cas9 to introduce the orthologous codon change in *Ikbkb*.[21][22][45] Cardinez et al. showed that mice and humans carrying this missense mutation exhibit remarkably similar cellular and biochemical phenotypes, demonstrating the utility of knock‑in models to validate human disease mechanisms.[21][22][45] While this study pertains to gain‑of‑function rather than deficiency, it highlights how CRISPR‑based functional genomics can interrogate NF‑κB pathway diseases.

No CRISPR or RNAi screens have been reported specifically for IKK2 deficiency patients, nor have single‑cell transcriptomics or spatial transcriptomics studies been conducted. Future applications of single‑cell RNA‑seq could dissect heterogeneity in immune cell activation defects and identify residual NF‑κB activity pockets, but for now, mechanistic data derive from bulk functional assays.[4][18][7]

Suggested GO terms for biological processes include GO:0007249 (I‑kappaB kinase/NF‑kappaB signaling), GO:0006955 (immune response), GO:0042110 (T cell activation), GO:0042113 (B cell activation), and GO:0006952 (defense response).[32][33][34] CL terms for involved cell types include CL:0000084 (T cell), CL:0000236 (B cell), CL:0000623 (NK cell), and CL:0000451 (dendritic cell).[33][38]

## 6. Anatomical Structures Affected

### 6.1 Organ‑Level Involvement

IKK2 deficiency primarily affects organs and systems engaged in immune function and host defense, but recurrent infections lead to multi‑organ involvement. The hematopoietic system (UBERON:0000178, bone marrow; UBERON:0002106, lymph node; UBERON:0001969, spleen) is directly implicated, as lymphoid organs house the defective T and B cells.[33][38] The thymus (UBERON:0002370) supports T‑cell development, which appears normal, but thymic output of naive T cells is increased relative to memory cells; however, specific thymus pathology has not been reported.[4][18][7]

The respiratory system (UBERON:0002048, lung) is frequently affected due to recurrent pneumonia, bronchitis, and opportunistic infections like *Pneumocystis jirovecii*.[18][20][7] The gastrointestinal tract (UBERON:0001043, intestine) often exhibits chronic diarrhea and enteropathy, reflecting infection and possibly intrinsic NF‑κB signaling defects in intestinal epithelial cells.[20][18][38] The liver (UBERON:0002107) and spleen (UBERON:0001969) enlarge due to hepatosplenomegaly, representing chronic immune activation and infection burden.[20][18][7]

Skin (UBERON:0002097) may show dermatitis and rashes, partly due to infections and partly due to immune dysregulation.[20][7] The cardiovascular and nervous systems are indirectly affected through sepsis and metabolic complications but are not primary targets of the disease mechanism, unlike some NF‑κB–related syndromes affecting ectodermal organs (e.g., NEMO deficiency).[5][24][42]

### 6.2 Tissue and Cell‑Level Targets

At the tissue level, lymphoid tissues (e.g., lymph nodes, spleen, tonsils) are central sites of pathology due to impaired lymphocyte activation and germinal center formation.[4][18][7] Naive T and B cells accumulate, while memory and effector subsets are absent or severely reduced, reflecting failure of functional maturation.[4][7] Germinal center reactions, essential for antibody affinity maturation and class switching, are defective, leading to hypogammaglobulinemia.[4][18][14] The Human Protein Atlas and NF‑κB pathway maps show high expression of IKKβ in immune cells and tissues.[33][37]

Specific cell populations targeted by the mechanism include CD4+ T helper cells (CL:0000624), CD8+ cytotoxic T lymphocytes (CL:0000625), B cells (CL:0000236), NK cells (CL:0000623), and myeloid cells (monocytes, macrophages, dendritic cells).[4][18][7] Regulatory T cells (FoxP3+ CD4+ Treg; CL:0000815) and γδ T cells (CL:0000798) are notably absent in IKK2‑deficient patients, indicating specialized differentiation defects in these cell lineages.[4] B cells fail to differentiate into plasmablasts and plasma cells (CL:0000980), as shown in gain‑of‑function *IKBKB* studies and inferred in loss‑of‑function disease from hypogammaglobulinemia.[21][23][7]

Intestinal epithelial cells (IECs; CL:0002563), while not directly studied in IKK2 deficiency patients, have been shown in mouse models to exhibit colitis‑like pathology and bone loss when IKK2 is constitutively active, and reduced inflammation when IKK2 is deleted.[38] This suggests that IKK2 in IECs contributes to gut inflammation and bone metabolism, and that loss of IKK2 may alter barrier function and cytokine expression, though this remains to be directly demonstrated in human IKK2 deficiency.

### 6.3 Subcellular Compartments

The key cellular compartments involved in IKK2 deficiency are the cytoplasm and nucleus. IKKβ (IKK2) resides in the cytoplasm as part of the IKK complex (GO:0005829, cytosol; GO:0008341, I‑kappaB kinase complex).[32][34][35] In response to stimuli, the IKK complex phosphorylates IκB in the cytoplasm, leading to its degradation via the ubiquitin–proteasome system (GO:0006511, ubiquitin‑dependent protein catabolic process).[34][35] NF‑κB dimers (p50/p65) then translocate to the nucleus (GO:0005634, nucleus) to regulate gene transcription.[32][34][37]

Loss of IKK2 disrupts this cytoplasmic phosphorylation step, leading to persistent IκB retention of NF‑κB in the cytoplasm and reduced nuclear NF‑κB activity.[4][32][34] Thus, the cytoplasm (site of IKK2 and IκB interaction), proteasome (GO:0000502), and nucleus (site of NF‑κB transcriptional activity) are critical subcellular compartments impacted by the disease.

### 6.4 Localization and Lateralization

IKK2 deficiency is a systemic disease, with bilateral and diffuse involvement of organs rather than localized or lateralized pathology. Infections may sometimes present in unilateral patterns (e.g., unilateral pneumonia), but this is determined by pathogen spread rather than underlying genetic lesions.[18][18][7] Lateralization is not a defining feature and can be considered non‑specific.

Anatomical localization of NF‑κB signaling is broad, encompassing multiple tissues, but the immunodeficiency phenotype reflects systemic immune cell dysfunction. Disease knowledge bases should annotate system‑wide involvement of the immune system (UBERON:0002405, immune system) and its component organs.[33][38]

## 7. Temporal Development

### 7.1 Onset Characteristics

The onset of IKK2 deficiency is congenital, with clinical manifestations appearing in early infancy. Orphanet lists age of onset as infancy, and MedGen emphasises that IMD15B is characterized by onset in infancy of life‑threatening infections and failure to thrive.[25][39][40] Ahamad et al. note that the phenotype is severe, with early‑onset life‑threatening combined immune deficiencies, and that most patients with loss‑of‑function mutations die in early infancy.[7] Specific case reports, such as the Turkish infant with p.R272X, show onset of severe infections at five months.[7] The Cree cohort demonstrates presentation within the first months of life.[14][18][18]

The onset pattern is typically chronic and progressive rather than acute, in the sense that susceptibility is present from birth but becomes clinically apparent with cumulative infections over weeks to months.[18][18][7] However, individual infections may present acutely and life‑threateningly, such as sepsis or pneumonia. Overall, onset can be described as congenital with subacute clinical unmasking.

### 7.2 Disease Progression and Course

Disease progression in IKK2 deficiency is rapid and progressive in the absence of curative intervention. Infants accumulate recurrent and severe infections, fail to thrive, and develop chronic organ involvement (e.g., lung, gut, liver).[18][18][7] Ahamad et al. emphasise that most patients with loss‑of‑function mutations die in early infancy due to overwhelming infections and associated complications.[7] In the sixteen‑patient Cree cohort, urgent HSCT was attempted in eight patients, but only three survivors were documented, indicating a high mortality despite intervention.[18][18][14]

The disease course can be conceptualised in stages:

Early stage (first months): onset of recurrent bacterial, viral, fungal, and mycobacterial infections, failure to thrive, initial immunologic evaluation revealing hypogammaglobulinemia and naive lymphocyte phenotype.[4][18][25]

Intermediate stage (late infancy): escalating infection burden, organ damage, opportunistic infections, and consideration for HSCT or supportive care.[18][18][7]

Advanced stage (later infancy/early childhood): persistent severe infections, multi‑organ failure, and high risk of death without successful transplantation.[7][31]

The rate of progression is rapid, with many patients dying within months to a couple of years if definitive treatment is not achieved.[18][18][7] In treated survivors, the course may stabilize, though residual non‑hematopoietic NF‑κB pathway defects and chronic complications may persist.[18][29][30]

### 7.3 Remission Patterns and Critical Periods

Spontaneous remission does not occur in IKK2 deficiency, as the underlying genetic defect persists. Treatment‑induced remission of immunodeficiency can be achieved through successful HSCT, which replaces defective hematopoietic cells with donor‑derived cells expressing functional IKK2.[18][18][29] However, HSCT outcomes are variable, with some patients experiencing graft failure, persistent infections, or non‑immune manifestations.[29][42][43] Thus, remission patterns are treatment‑dependent and partial.

Critical periods include the neonatal and early infancy window, where early recognition and avoidance of live vaccines like BCG can prevent vaccine‑strain infections.[20][20][7] The period prior to overwhelming infections is a crucial window for HSCT; performing transplantation before severe organ damage or disseminated mycobacterial infection appears to improve survival.[18][18][29][42] The Genomics Education Knowledge Hub emphasises that early diagnosis and urgent HSCT are essential, and that standard newborn TREC screening may miss IKK2 deficiency because TCR excision circles are normal.[18][20][20] This indicates a missed critical period in newborn screening programmes and underscores the need for targeted genetic testing in infants with severe infections.

## 8. Inheritance and Population Characteristics

### 8.1 Epidemiology: Prevalence and Incidence

IKK2 deficiency is exceedingly rare. Orphanet estimates prevalence at <1/1,000,000, consistent with an ultra‑rare primary immunodeficiency.[25] No incidence figures are available from population registries, likely due to under‑diagnosis and the rarity of the disease.[25][31] Large‑scale epidemiologic datasets such as SEER or GBD do not provide specific statistics for this entity.

The known cohorts—four Cree infants in the original NEJM report and sixteen infants in the expanded case series—represent local clusters rather than population‑wide incidence.[14][4][18][18] Other sporadic cases have been reported from Turkey and other regions.[7][14] Given autosomal recessive inheritance and severe phenotype, the disease likely exists in small numbers worldwide, with higher local prevalence in communities with founder mutations and consanguinity.

### 8.2 Inheritance Pattern, Penetrance, and Expressivity

For IKK2 deficiency (IMD15B), the inheritance pattern is autosomal recessive. OMIM and MedGen describe Immunodeficiency‑15B as autosomal recessive, with disease caused by homozygous or compound heterozygous mutations in *IKBKB*.[3][12][15][39] The onset in infancy and severe phenotype indicate high, likely complete penetrance: individuals with biallelic amorphic loss‑of‑function variants consistently develop severe combined immunodeficiency.[7][31]

Expressivity among biallelic loss‑of‑function cases is relatively consistent in severity (early‑onset, life‑threatening infections), though specific infections, organ involvement, and survival vary.[7][31] Patients with hypomorphic variants that allow partial expression of IKK2 may have somewhat milder or protracted courses, living into later childhood with intensive care, but the core immunodeficiency remains severe.[7][20] This reflects variable expressivity based on allele functionality rather than random variability.

For gain‑of‑function Immunodeficiency‑15A (IMD15A), the inheritance pattern is autosomal dominant, often due to de novo missense variants such as p.V203I.[15][17][21][44] Penetrance appears high, with probands consistently showing immune dysregulation, combined T and B cell deficiency, and inflammatory features, but age of onset and severity are more variable than in recessive deficiency.[21][36][44]

Genetic anticipation has not been described, as the disease is not caused by repeat expansions. Germline mosaicism has not been reported but could theoretically occur in de novo gain‑of‑function cases. For recessive deficiency, consanguinity is an important factor increasing risk of biallelic pathogenic variants, as noted in Turkish and Cree families.[13][7]

### 8.3 Founder Effects, Carrier Frequency, and Population Demographics

Founder effects have been documented in Cree populations in Canada. Pannicke et al. and subsequent reports identified the c.1292dupG variant in multiple Cree infants and suggested that this mutation originated from a common ancestor.[13][14][18][18] Carrier frequency within the Cree population is not precisely quantified in the provided sources, but the cluster of cases implies a non‑trivial carrier rate, potentially justifying community‑specific genetic counseling and screening.[13][18]

Consanguinity plays a role in sporadic cases from populations with higher rates of consanguineous marriage, such as Turkey, where a homozygous nonsense mutation was reported in a consanguineous family.[7][14] This pattern is common in autosomal recessive primary immunodeficiencies, exacerbating risk of biallelic loss‑of‑function variants.

Sex ratio in IKK2 deficiency appears approximately equal, as autosomal recessive inheritance affects both males and females. The NEJM and Cree cohorts include both sexes, and no sex bias is mentioned.[14][4][18][18] Age distribution is skewed to infancy, with very few survivors into later childhood, reflecting high mortality in early life.[7][31]

Geographically, cases have been reported in Canada (Cree), Turkey, and other regions, but precise distribution is unknown.[14][18][7] Public health registries for rare diseases, such as Orphanet, classify the disease as pan‑European but extremely rare.[25] gnomAD and population genetics databases are expected to show extremely low allele frequencies for pathogenic *IKBKB* variants outside founder populations.[7]

## 9. Diagnostics

### 9.1 Clinical and Laboratory Tests

Diagnostic evaluation of suspected IKK2 deficiency involves a combination of clinical assessment, immunologic laboratory tests, and genetic analysis. Clinically, infants present with recurrent severe infections, failure to thrive, and signs of combined immunodeficiency (e.g., opportunistic infections, vaccine‑strain disease).[18][20][25] Laboratory tests focus on quantifying immunoglobulins, lymphocyte subsets, and functional responses.

Hypogammaglobulinemia or agammaglobulinemia is a hallmark, detected by serum IgG, IgA, and IgM measurements (LOINC codes for immunoglobulin assays).[18][20][25] T‑ and B‑cell counts, measured by flow cytometry, are typically within normal ranges but show naive phenotypes, with reduced memory subsets.[4][18][7] Regulatory T cells (CD4+CD25+FoxP3+) and γδ T cells are absent.[4] NK cell counts may be reduced.[20][20] Functional tests, such as lymphocyte proliferation in response to mitogens (PHA, ConA) and antigens, are profoundly impaired.[4][18][7] Cytokine production after TLR stimulation and NK‑cell cytotoxicity are reduced.[4][30]

Genomics Education notes that loss‑of‑function biallelic disease may show normal T‑ and B‑cell counts, impaired T‑cell proliferation, hypogammaglobulinemia, and reduced NK cell count.[20][20] These functional abnormalities distinguish IKK2 deficiency from purely quantitative lymphopenic SCID entities and justify classification as combined immunodeficiency.

Imaging studies (e.g., chest X‑ray, CT) may reveal pneumonia, bronchiectasis, or lymphadenopathy, but are not specific for IKK2 deficiency.[18][18] Biopsies, such as intestinal biopsies, may show chronic inflammatory changes, but specific histopathologic signatures are more developed in related NEMO deficiency than in IKK2 deficiency.[24][30][42] Pathology findings primarily reflect associated infections rather than intrinsic morphological abnormalities.

### 9.2 Genetic Testing Strategies

Genetic testing is essential to confirm IKK2 deficiency, as clinical and immunologic features overlap with other primary immunodeficiencies. The Genetic Testing Registry (GTR), OMIM, and Genomics England PanelApp highlight *IKBKB* as a gene included in primary immunodeficiency and monogenic inflammatory bowel disease panels.[10][6][17] Recommended approaches include:

Whole‑exome sequencing (WES): Effective in identifying pathogenic *IKBKB* variants in infants with severe infections and combined immunodeficiency, as demonstrated by Pannicke et al. and Cardinez et al.[4][21][45] WES allows detection of both loss‑of‑function and gain‑of‑function alleles and can distinguish IKBKB‑related immunodeficiency from other NF‑κB pathway disorders.

Targeted gene panels: Many diagnostic laboratories offer primary immunodeficiency panels covering *IKBKB* alongside other genes (e.g., *IKBKG*, *CHUK*, *CARD11*, *BTK*).[10][6][20] Panel testing is particularly useful in suspected NF‑κB pathway defects.

Single‑gene testing: For known founder mutations (e.g., c.1292dupG in Cree population), targeted Sanger sequencing or high‑sensitivity PCR assays for *IKBKB* exon 13 may suffice.[13][18][18]

Chromosomal microarray, karyotyping, FISH, and mitochondrial DNA testing are not indicated, as the disease is caused by sequence‑level mutations in a nuclear gene.[3][12] Repeat expansion testing is also irrelevant.

ClinVar and ClinGen provide variant interpretations for *IKBKB*, indicating pathogenic, likely pathogenic, and VUS classifications for specific changes such as c.1292dupG and c.607G>A.[13][44][46] This facilitates genotype–phenotype correlations and variant curation under ACMG/AMP guidelines.

### 9.3 Omics‑Based Diagnostics and Biomarkers

No dedicated omics‑based diagnostic biomarkers (e.g., transcriptomics signatures, proteomics patterns, metabolomics markers) have been validated for IKK2 deficiency. The rarity of the disease and the robustness of genetic diagnosis preclude reliance on omics for primary diagnosis. However, NF‑κB pathway activation can be assessed by phosphoflow cytometry, measuring phosphorylation of IκB or p65 after stimulation.[36] Amsterdam UMC’s report on *IKBKB* gain‑of‑function variants showed altered NF‑κB signaling evidenced by phosphoflow experiments, indicating that such assays could be adapted to test for loss‑of‑function as well.[23][36]

Potential biomarkers include absence of IKKβ protein expression (assessed by Western blot in patient cells), absence of nuclear NF‑κB translocation after stimulation, and impaired up‑regulation of activation markers (CD25, CD69, CD40L).[4][18][7][36] These functional metrics can complement genetic data in uncertain cases.

### 9.4 Clinical Criteria, Differential Diagnosis, and Screening

Formal standardized diagnostic criteria (e.g., society guidelines) specific to IKK2 deficiency have not yet been published; however, the International Union of Immunological Societies (IUIS) classification lists IKBKB defects among combined immunodeficiencies.[6][6][20] Clinicians generally diagnose IKK2 deficiency based on severe early‑onset infections, hypogammaglobulinemia, naive lymphocyte phenotype, impaired lymphocyte activation, and pathogenic *IKBKB* variants.

Differential diagnosis includes other combined immunodeficiencies with normal or near‑normal T‑cell counts, such as ZAP‑70 deficiency, CD40L deficiency, NEMO (IKBKG) deficiency, and CBM complex defects.[20][29][42] NEMO deficiency overlaps mechanistically, as both involve NF‑κB signaling, but has additional ectodermal dysplasia, colitis, and distinct genetic features (X‑linked hypohydrotic ectodermal dysplasia with immunodeficiency).[5][24][42] HSCT outcomes also differ; in NEMO deficiency, HSCT can correct immune defects but may not cure colitis due to non‑hematopoietic NF‑κB defects.[24][30][42] Wiskott–Aldrich syndrome, CD25 deficiency, and IL‑7R deficiency must also be considered.

Screening currently relies on clinical suspicion rather than population programmes. Newborn TREC screening for SCID does not detect IKK2 deficiency, because TCR excision circles are normal and lymphocyte development is preserved.[18][18][31] The Cree cohort case series explicitly states that “T‑cell receptor excision circles were normal, meaning newborn screening by TREC analysis would miss IKBKB cases.”[18] This highlights a gap in screening strategies and supports targeted genetic testing in infants with severe infections and failure to thrive, even if newborn SCID screening is negative.

Carrier screening and cascade genetic testing in families and founder populations may be considered as secondary preventive measures, but formal programmes have not been described in the literature.[13][18][20]

## 10. Outcome and Prognosis

### 10.1 Survival, Mortality, and Life Expectancy

The prognosis for IKK2 deficiency is poor without transplantation. Orphanet notes that combined immunodeficiency due to IKBKB deficiency is a life‑threatening condition with onset in infancy.[25] Ahamad et al. state that most patients with loss‑of‑function mutations die in early infancy due to overwhelming and wide‑ranging recurrent infections and other associated complications.[7] Many reported cases, such as the Turkish infant with p.R272X, died within the first 1–2 years of life.[7][14] In the Cree cohort, eight patients underwent HSCT and only three survived, indicating high mortality even with attempted curative therapy.[18][18][14]

Quantitative survival statistics are limited by small sample sizes, but the overall impression is that untreated survival beyond early childhood is rare. Life expectancy in the absence of HSCT is measured in months to a few years, depending on infection burden and supportive care.[7][31] With successful HSCT, life expectancy can approach normal, though long‑term data are sparse and complications remain.[18][18][29]

Mortality rates in published cohorts are high: in the sixteen‑patient Cree series, thirteen deaths were recorded, resulting in a survival rate of approximately 19% among those transplanted or managed.[18][18][14] A broader literature review by LymphoSign on HSCT for NF‑κB defects noted that only three patients with IKBKB deficiency survived, with the longest follow‑up at 24 months, and concluded that assessment of HSCT benefits and management recommendations are premature.[29] This underscores the gravity of the disease and the challenges in management.

### 10.2 Morbidity, Disability, and Quality of Life

Morbidity in IKK2 deficiency is severe. Infants suffer repeated infections, hospitalisations, invasive interventions, and prolonged antibiotic, antifungal, and antiviral therapies.[18][18][7] Complications include chronic lung disease, enteropathy, hepatosplenomegaly, malnutrition, and anemia, contributing to substantial disability and reduced quality of life.[20][18][7] Survivors of HSCT face risks of graft‑versus‑host disease (GVHD), graft failure, secondary malignancies, and persistent or de novo inflammatory bowel disease.[29][42][43]

Quality of life assessment tools have not been systematically applied, but the disease likely imposes high disability weights in global burden studies, akin to other severe primary immunodeficiencies.[7][31] The necessity of protective isolation, frequent hospital care, and avoidance of infections restricts normal life and developmental experiences for affected children and families.

### 10.3 Disease Course, Complications, and Recovery Potential

The disease course is typically progressive and life‑threatening, with limited spontaneous recovery potential. Complications include recurrent severe infections (pneumonia, sepsis, meningitis), opportunistic infections (*Pneumocystis jirovecii*, disseminated BCG), chronic diarrhea and malabsorption, hepatosplenomegaly, dermatitis, and, in some cases, inflammatory bowel disease in related NF‑κB disorders.[18][20][24][18][7]

HSCT offers a potential cure for hematopoietic immunodeficiency, and successful transplantation can correct many immune defects and improve survival.[18][18][29] However, HSCT carries risks of graft failure, GVHD, conditioning regimen toxicity, and infection complications. In NEMO deficiency, HSCT did not cure colitis, suggesting that non‑hematopoietic NF‑κB defects persist.[24][30][42] In IKK2 deficiency, similar concerns arise, as intestinal epithelial IKK2 may be important for gut barrier function.[38] Thus, recovery potential is contingent on the ability of HSCT to reconstitute immune function without causing excessive morbidity and on the absence of critical non‑hematopoietic NF‑κB–dependent complications.

### 10.4 Prognostic Factors and Biomarkers

Prognostic factors in IKK2 deficiency include age at diagnosis and treatment, infection burden, organ function, HSCT timing, donor type, and conditioning regimen.[18][18][29] Miot et al.’s analysis of HSCT in NEMO deficiency revealed that preexisting mycobacterial infection and colitis were associated with poor HSCT outcome, a finding likely relevant to IKK2 deficiency as well.[42][43] The editorial “Transplant for NEMO: this and much, much more” echoes that preexisting infections and colitis worsen outcomes and that nonmyeloablative conditioning may trend toward better disease‑free survival.[43] In IKK2 deficiency, similar prognostic patterns are suggested by the high mortality in heavily infected patients undergoing HSCT.[18][18][29]

Potential prognostic biomarkers include degree of hypogammaglobulinemia, functional assays of lymphocyte activation, residual IKK2 expression, and presence of opportunistic infections or organ dysfunction. However, formal prognostic models have not been developed, and small case numbers limit quantitative risk prediction.

## 11. Treatment

### 11.1 Pharmacotherapy and Supportive Management

Supportive therapy is central to the management of IKK2 deficiency. This includes aggressive antimicrobial treatment for acute infections (antibiotics, antifungals, antivirals), prophylactic antimicrobials (e.g., trimethoprim–sulfamethoxazole for *Pneumocystis jirovecii*, azole antifungals), and immunoglobulin replacement therapy (IVIG or SCIG) to compensate for hypogammaglobulinemia.[18][20][18][20] These interventions align with NCIT terms such as NCIT:C15313 (Anti‑infective Agent) and NCIT:C574 (Immune Globulin).

Genomics Education emphasises that autosomal recessive *IKBKB*‑associated immunodeficiency requires early diagnosis and urgent HSCT, but until transplantation, patients need broad infection prophylaxis, avoidance of live vaccines, and nutritional support.[20][20] Corticosteroids or other immunomodulators are generally avoided except when treating GVHD or inflammatory complications, given the underlying immunodeficiency.

Pharmacologic inhibition of IKK2 has been studied in mouse models of colitis‑associated bone loss and gut inflammation, where IKK2 inhibitors reduced inflammatory cytokines and ILC1/ILC3 frequencies, attenuating bone loss and colitis.[38] However, such inhibitors are contraindicated in IKK2 deficiency, where IKK2 activity is already absent. These preclinical data highlight potential therapeutic targets for inflammatory complications in NF‑κB–active diseases but are not applicable to loss‑of‑function IKK2 deficiency.

### 11.2 Advanced Therapeutics: Hematopoietic Stem Cell Transplantation

Hematopoietic stem cell transplantation (HSCT) is currently the only known curative therapy for IKK2 deficiency, as highlighted in the Cree cohort case series and subsequent reviews.[18][18][29][14] By replacing the patient’s hematopoietic system with donor stem cells expressing functional IKK2, HSCT can restore NF‑κB signaling in immune cells and correct combined immunodeficiency.

The Cree cohort paper notes:

> “Urgent HSCT, performed in eight patients, remains the only known curative therapy, although only three patients are survivors… Ongoing infections after transplant remain a concern, and may be due to combinations of poor social determinants of health, secondary graft failure, and failure of HSCT to replace non‑hematopoietic cells important in immune function and dependent upon IKK/NF‑κB pathways.”[18][18][14]

LymphoSign’s review of HSCT for NF‑κB defects reported that only two long‑term survivors with IKBKB defects were available, and that assessment of HSCT benefits and management recommendations remain premature.[29] Conditioning regimens (myeloablative vs reduced intensity) and donor types (matched related, matched unrelated, haploidentical) influence outcomes, but no consensus guidelines exist specifically for IKK2 deficiency.[29][42][43] The NEMO HSCT series (Miot et al.) suggested that preexisting mycobacterial infection and colitis worsened outcomes and that nonmyeloablative regimens might trend toward better survival, offering general guidance for NF‑κB pathway HSCT.[42][43]

NCIT terms such as NCIT:C15206 (Hematopoietic Stem Cell Transplantation) and NCIT:C15273 (Bone Marrow Transplantation) are appropriate annotations for these interventions.

### 11.3 Experimental and Emerging Therapies

Gene therapy and genome editing are conceptual possibilities for IKK2 deficiency but have not yet reached clinical trials. In theory, ex vivo gene therapy using viral vectors to deliver normal *IKBKB* to hematopoietic stem cells could mimic HSCT without the need for donor cells, while CRISPR/Cas9 editing could correct the causative mutations.[21][22][45] However, the complexity of NF‑κB pathway regulation and safety concerns regarding insertional mutagenesis and off‑target editing require careful preclinical testing.

RNA‑based therapies (e.g., antisense oligonucleotides, siRNA) are unlikely to be beneficial in loss‑of‑function IKK2 deficiency, as the problem is absence of functional protein rather than toxic gain of function. For gain‑of‑function IMD15A, RNA‑based silencing or small molecule IKK2 inhibitors could theoretically dampen hyperactive NF‑κB signaling, but such strategies remain experimental.[21][36][38]

Targeted immunotherapies, such as monoclonal antibodies or checkpoint inhibitors, are generally contraindicated or of limited use in IKK2 deficiency due to underlying immunodeficiency. CAR‑T cells, cellular therapeutics, and biologics are more relevant to malignancies and autoimmune conditions than to primary immunodeficiency correction.

### 11.4 Treatment Outcomes, Side Effects, and Strategy

Treatment outcomes hinge on HSCT success and infection control. As noted, survival rates are low among transplanted IKK2 deficiency patients, with only a minority surviving long term.[18][18][29][14] Side effects of HSCT include GVHD, graft failure, infections, and conditioning toxicity.[29][42][43] Supportive therapies such as IVIG and antimicrobials carry their own risks, such as allergic reactions, renal toxicity, and antimicrobial resistance.

Treatment strategies emphasize early detection, immediate infection control, immunoglobulin replacement, avoidance of live vaccines, and rapid referral to transplant centers for HSCT evaluation.[20][20][20] Personalized medicine approaches involve tailoring conditioning regimens and donor selection based on patient condition, infection status, and NF‑κB pathway considerations. NF‑κB pathway inhibitors are avoided in loss‑of‑function disease but may be considered in hyperinflammatory NF‑κB–active syndromes.

NCIT clinical‑intervention terms that can be suggested include NCIT:C28776 (Antibiotic Therapy), NCIT:C66807 (Antifungal Therapy), NCIT:C28863 (Antiviral Therapy), NCIT:C574 (Immune Globulin), and NCIT:C15206 (Hematopoietic Stem Cell Transplantation).

## 12. Prevention

### 12.1 Primary, Secondary, and Tertiary Prevention

Primary prevention of IKK2 deficiency at the population level is challenging due to its monogenic autosomal recessive nature and ultra‑rare prevalence. However, in founder populations or families with known pathogenic *IKBKB* variants, primary prevention can involve carrier screening and reproductive counseling to reduce risk of affected offspring.[13][18][20] Genetic counseling resources such as GeneReviews and NSGC guidelines (not in provided search results but relevant) would support such interventions.

Secondary prevention focuses on early detection and prompt treatment to prevent severe complications. Since newborn TREC screening does not detect IKK2 deficiency, targeted genetic testing in infants with severe infections and failure to thrive is essential.[18][18][20] Avoidance of live vaccines such as BCG, oral polio, and rotavirus in suspected cases can prevent vaccine‑strain infections.[20][7][20] Rapid initiation of antimicrobial prophylaxis and IVIG when immunodeficiency is suspected can reduce morbidity.

Tertiary prevention aims to prevent complications and disability in those with established disease. This includes ongoing infection prophylaxis, nutritional support, physical therapy for chronic lung disease, and careful management of HSCT complications.[18][18][29] For related NF‑κB disorders like NEMO deficiency, tertiary prevention also involves monitoring for colitis, bone disease, and ectodermal manifestations.[24][30][42]

### 12.2 Immunization and Screening

Immunization strategies for infants with IKK2 deficiency require modification of standard schedules. Live attenuated vaccines (BCG, measles, MMR, varicella) should be avoided due to risk of disseminated infection.[20][7][20] Inactivated vaccines may provide limited benefit due to hypogammaglobulinemia and poor antibody responses, but can be administered under careful monitoring; passive immunization via IVIG provides some protective antibodies.[18][20][20] CDC and WHO immunization guidelines for children with primary immunodeficiencies recommend avoiding live vaccines, a principle applicable here.

Screening programmes for IKK2 deficiency are not yet in place, but newborn screening for SCID via TREC analysis fails to detect this disease because T‑cell development and TREC counts are normal.[18][18][31] This underscores the need for expanded newborn screening strategies incorporating genetic panels or functional assays for combined immunodeficiencies with normal lymphocyte numbers. Carrier screening in founder populations and cascade testing among relatives of affected patients are key screening methods for family‑based prevention.[13][18][20]

### 12.3 Behavioral and Public Health Interventions, Counseling, and Prophylaxis

Behavioral interventions for families with IKK2‑deficient infants include meticulous infection control practices (hand hygiene, avoidance of sick contacts), environmental modifications (clean water, safe food), and adherence to prophylactic medication regimens.[20][20] Public health interventions may involve community education in high‑risk populations regarding signs of severe immunodeficiency and the need for early medical evaluation.

Genetic counseling is essential for parents and extended family, explaining autosomal recessive inheritance, carrier risks, and options for prenatal or preimplantation genetic diagnosis.[13][18][20] Counseling can guide family planning and inform decisions about early testing of siblings.

Prophylactic strategies include antimicrobial prophylaxis (e.g., trimethoprim–sulfamethoxazole, azole antifungals), IVIG replacement, and, where feasible, protective isolation or reduced exposure to pathogens.[18][20][18] NCIT terms such as NCIT:C94128 (Prophylactic Antibiotic) and NCIT:C66807 (Antifungal Therapy) fit these interventions.

## 13. Other Species and Natural Disease

### 13.1 Species, Orthologous Genes, and Comparative Biology

Orthologous *IKBKB* genes exist in multiple species, including mice (MGI:1338071), reflecting evolutionary conservation of NF‑κB signaling.[8][33] Alliance of Genome Resources and HomoloGene list *IKBKB* orthologs across mammals and vertebrates, though specific OMIA entries for naturally occurring veterinary IKK2 deficiency are not reported in the provided search results. No companion animal or livestock species have been described with natural *IKBKB*‑related immunodeficiency, suggesting either extreme rarity or underdiagnosis.[7][31]

Comparative pathology studies of NF‑κB pathway disorders in animals often focus on experimental models rather than spontaneous disease. The evolutionary conservation of NF‑κB signaling and IKK complex structure indicates that loss‑of‑function *Ikbkb* mutations in animals would likely cause severe immunodeficiency, but such cases have not been documented outside engineered models.[33][37][38]

Zoonotic transmission is not relevant, as IKK2 deficiency is not caused by infectious agents and does not spread between individuals. Cross‑species susceptibility pertains to infections in IKK2‑deficient hosts rather than to the genetic disease itself.

### 13.2 Natural Disease in Other Species

Natural disease due to *IKBKB* deficiency has not been described in animals, based on the current literature.[7][31] OMIA and VetCompass databases likely lack entries for IKK2 deficiency, reflecting its monogenic and severe nature, which would cause early mortality and limit detection in veterinary practice.

However, NF‑κB pathway dysfunction has been implicated in inflammatory and immune disorders in animals, and similarities in pathway components suggest that insights from human IKK2 deficiency could inform understanding of animal diseases with analogous mechanisms, even if specific *Ikbkb* mutations are not identified.[37][38]

## 14. Model Organisms

### 14.1 Mouse Models of IKK2 Function and NF‑κB Pathway

Mouse models have been instrumental in dissecting IKK2 function and NF‑κB signaling. Global *Ikbkb* knockout in mice is embryonic lethal, indicating a more essential role in murine development than in humans.[4][7][38] This lethality complicates direct modeling of human IKK2 deficiency, but conditional knockouts and tissue‑specific manipulations have been used.

Conditional expression of constitutively active IKK2 in intestinal epithelial cells (IECs) triggers colitis‑like pathology and significant bone loss, mimicking dextran sodium sulfate (DSS)‑induced colitis.[38] Conversely, conditional deletion of IKK2 from IECs significantly attenuates inflammation and bone loss in DSS‑induced colitis.[38] Pharmacologic inhibition of IKK2 in this model also reduces inflammatory cytokines and ILC1/ILC3 cells, halting colitis‑associated bone loss.[38] These data reveal IKK2 in IECs as a therapeutic target for colitis‑associated osteopenia and highlight tissue‑specific roles of NF‑κB signaling.

Cardinez et al. generated a knock‑in mouse model of the human gain‑of‑function V203I variant, introducing the precise orthologous codon change in *Ikbkb* using CRISPR/Cas9.[21][22][45] Mice carrying this mutation exhibited similar cellular and biochemical phenotypes to human IMD15A patients, including enhanced NF‑κB signaling, T and B cell functional defects, inflammation, and epithelial abnormalities.[21][22][45] This validates the pathogenicity of the variant and demonstrates translational utility of mouse models in NF‑κB pathway disease.

### 14.2 Phenotype Recapitulation and Limitations

Mouse models recapitulate many aspects of NF‑κB pathway dysfunction but have limitations in modeling human IKK2 deficiency. Embryonic lethality of full *Ikbkb* knockout prevents direct observation of postnatal severe combined immunodeficiency analogous to human IMD15B.[4][7][38] Conditional knockouts in hematopoietic cells could circumvent this, but such models are not described in the provided search results. IEC‑specific manipulations reveal gut‑specific roles but not systemic immunodeficiency.[38]

The V203I gain‑of‑function knock‑in model recapitulates combined immune deficiency and immune dysregulation rather than pure loss‑of‑function deficiency.[21][22][45] This model accurately reflects IMD15A but not IMD15B. Thus, while mouse models allow mechanistic study of NF‑κB signaling, they do not fully reproduce the human phenotype of IKK2 loss‑of‑function combined immunodeficiency due to developmental constraints.

Applications of these models include studying tissue‑specific NF‑κB roles (e.g., in gut, bone, immune cells), testing IKK2 inhibitors in inflammatory disorders, and validating gain‑of‑function variant pathogenicity. However, caution is needed when extrapolating from mice to humans, given species differences in NF‑κB pathway essentiality and immune architecture.[4][7][38]

### 14.3 Other Model Systems

No zebrafish, Drosophila, or C. elegans models of *IKBKB* deficiency are mentioned in the provided search results. Cellular models, such as patient‑derived lymphocytes or engineered cell lines lacking IKK2, have been used to study signaling defects, but detailed descriptions are limited.[4][7][36] Organoid or iPSC models of IKK2 deficiency have not yet been reported but could be developed to study non‑hematopoietic NF‑κB roles.

Model organism databases such as MGI, IMPC, and EuMMCR likely contain entries for *Ikbkb* knockout and conditional models, but specific phenotype annotations are beyond the scope of the provided sources.[38] Overall, model organisms provide valuable mechanistic insights but only partial phenotypic recapitulation of human IKK2 deficiency.

## 15. Conclusion and Synthesis

Severe combined immunodeficiency due to IKK2 deficiency (IKBKB‑associated immunodeficiency, Immunodeficiency‑15B, MONDO:0014267) is a rare, life‑threatening Mendelian disorder rooted in biallelic loss‑of‑function mutations in the *IKBKB* gene, encoding the IκB kinase‑β subunit of the canonical NF‑κB signaling complex.[3][12][25][31] The initiating lesion—absence or severe reduction of IKK2—disrupts phosphorylation and degradation of IκB inhibitors, preventing NF‑κB nuclear translocation and transcriptional responses to stimuli across T‑cell receptors, B‑cell receptors, toll‑like receptors, and cytokine receptors.[4][32][34][35] This molecular block leads to profound defects in activation, differentiation, and effector function of T cells, B cells, NK cells, and myeloid cells, despite near‑normal lymphocyte numbers, producing a characteristic phenotype of early‑onset life‑threatening infections, hypogammaglobulinemia or agammaglobulinemia, naive lymphocyte phenotypes, absence of regulatory and γδ T cells, and failure to thrive.[4][18][25][7]

Clinical evidence from the landmark NEJM study by Pannicke et al. and expanded Cree cohorts, complemented by additional case reports and systematic reviews, defines IKK2 deficiency as a severe combined immunodeficiency at least as profound as classical SCID but often missed by newborn TREC screening.[14][4][18][18][31] The most common pathogenic variant, c.1292dupG in exon 13 of *IKBKB*, exemplifies the loss‑of‑function truncating alleles that cause complete absence of IKK2 protein and canonical pathway failure.[13][4][7] Other loss‑of‑function variants, including nonsense and frameshift alleles, produce similar severe phenotypes.[7][14][20] In contrast, heterozygous gain‑of‑function variants such as p.V203I cause Immunodeficiency‑15A, a distinct autosomal dominant syndrome of immune dysregulation and later‑onset combined immunodeficiency, underscoring the bidirectional disease spectrum of *IKBKB*.[15][21][3][36][44]

Mechanistically, IKK2 deficiency illustrates the centrality of NF‑κB signaling in immune activation and host defense. Mouse models of conditional IKK2 expression in intestinal epithelium and CRISPR knock‑in of gain‑of‑function variants demonstrate tissue‑specific roles and validate human pathogenicity, although embryonic lethality of global *Ikbkb* knockout limits direct modeling of human loss‑of‑function disease.[21][22][38][45] Non‑hematopoietic NF‑κB functions, particularly in intestinal epithelial cells, may contribute to chronic inflammatory manifestations that are not fully corrected by HSCT, as shown in analogous NEMO deficiency and inferred for IKK2 deficiency.[24][30][38][42]

Diagnosis requires a combination of clinical suspicion, immunologic laboratory evaluation (hypogammaglobulinemia, naive lymphocyte phenotype, impaired proliferation and cytokine responses), and genetic testing for *IKBKB* variants.[4][18][20][20] Whole‑exome sequencing and targeted primary immunodeficiency panels effectively identify pathogenic alleles, while functional assays confirm NF‑κB signaling defects.[4][21][7][36] Standard newborn SCID screening via TREC analysis fails to detect IKK2 deficiency, demanding enhanced screening strategies in infants with severe infections and failure to thrive.[18][18][31]

Prognosis without HSCT is poor, with most patients dying in early infancy from overwhelming infections and complications.[7][31] HSCT remains the only known curative therapy for hematopoietic immunodeficiency, but outcomes are variable and influenced by infection status, conditioning regimen, donor type, and non‑hematopoietic NF‑κB functions.[18][18][29][42][43] Supportive therapies (aggressive antimicrobials, IVIG replacement, infection prophylaxis, avoidance of live vaccines) are essential to stabilize patients and prevent infections prior to transplantation.[18][20][18][20] Preventive strategies include genetic counseling, carrier screening in founder populations, and targeted early testing of symptomatic infants, though population‑level screening is limited by rarity.[13][18][20][25]

Ontologically, IKK2 deficiency should be annotated as MONDO:0014267 (severe combined immunodeficiency due to IKK2 deficiency), with HGNC:10682 (*IKBKB*), GO:0007249 (I‑kappaB kinase/NF‑kappaB signaling), HP:0004430 (combined immunodeficiency), HP:0002715 (recurrent infections), HP:0004314 (hypogammaglobulinemia), CL:0000084 (T cell), CL:0000236 (B cell), UBERON:0002405 (immune system), and NCIT:C15206 (Hematopoietic Stem Cell Transplantation).[3][25][31][32][33][34] Evidence items should include PMIDs 24369075 (Pannicke et al., NEJM 2013), 30391351/7106064 (Cree cohort HSCT outcomes), 42238289/13227448 (Ahamad et al. review), 30337470/6219745 (Cardinez et al. gain‑of‑function), and 28679735/6141239/5609338 (NEMO HSCT and editorial).[4][14][18][18][7][21][22][42][43]

In summary, IKK2 deficiency represents a paradigmatic NF‑κB pathway–related combined immunodeficiency, defined by loss‑of‑function *IKBKB* variants, severe early‑onset infections, and profound defects in immune activation. Continued research into tissue‑specific NF‑κB roles, optimized HSCT strategies, and potential gene therapy approaches will be crucial to improving outcomes for affected infants. At the same time, expansion of genetic screening and awareness among clinicians can facilitate earlier diagnosis and intervention, reducing mortality and morbidity in this ultra‑rare but devastating disease.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 53 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 28 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 15 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002715` (3 mentions) - the report calls it "recurrent infections"; HP calls it **Abnormality of the immune system**
- `HP:0005347` (2 mentions) - the report calls it "failure to thrive"; HP calls it **Tracheal cartilaginous sleeve**
- `NCIT:C3107` (1 mention) - the report calls it "Severe Combined Immunodeficiency"; NCIT calls it **Langerhans Cell Histiocytosis**
- `HP:0000028` (1 mention) - the report calls it "agammaglobulinemia"; HP calls it **Cryptorchidism**
- `HP:0002019` (1 mention) - the report calls it "diarrhea"; HP calls it **Constipation**
- `HP:0002104` (1 mention) - the report calls it "hepatosplenomegaly"; HP calls it **Apnea**
- `HP:0000989` (1 mention) - the report calls it "eczema/dermatitis"; HP calls it **Pruritus**
- `NCIT:C15313` (1 mention) - the report calls it "Anti‑infective Agent"; NCIT calls it **Radiation Therapy**
- `NCIT:C574` (2 mentions) - the report calls it "Immune Globulin"; NCIT calls it **Immunosuppressant**
- `NCIT:C15206` (3 mentions) - the report calls it "Hematopoietic Stem Cell Transplantation"; NCIT calls it **Clinical Study**
- `NCIT:C15273` (1 mention) - the report calls it "Bone Marrow Transplantation"; NCIT calls it **Longitudinal Study**
- `NCIT:C28776` (1 mention) - the report calls it "Antibiotic Therapy"; NCIT calls it **(H115D)VHL35 Peptide**
- `NCIT:C66807` (2 mentions) - the report calls it "Antifungal Therapy"; NCIT calls it **Benign Ciliary Body Medulloepithelioma**
- `NCIT:C28863` (1 mention) - the report calls it "Antiviral Therapy"; NCIT calls it **Benzonatate**
- `NCIT:C94128` (1 mention) - the report calls it "Prophylactic Antibiotic"; NCIT calls it **Study Recruitment Status Code**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0004314` (3 mentions), reported as "hypogammaglobulinemia" - HP does not contain this term
- `HP:0003379` (1 mention), reported as "opportunistic infections" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0008341` (obsolete response to cocaine (sensu Insecta)) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0004430` (4 mentions) - the report calls it "combined immunodeficiency"; HP calls it **Severe combined immunodeficiency**
- `GO:0007249` (4 mentions) - the report calls it "I‑kappaB kinase/NF‑kappaB signaling"; GO calls it **canonical NF-kappaB signal transduction**, and lists "I-kappaB kinase/NF-kappaB signaling" among its other names
- `CL:0000623` (3 mentions) - the report calls it "NK cell"; CL calls it **natural killer cell**, and lists "NK cell" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.