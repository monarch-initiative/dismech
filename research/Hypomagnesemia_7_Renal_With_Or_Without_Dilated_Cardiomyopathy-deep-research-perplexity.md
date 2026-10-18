---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-15T12:34:20.292184'
end_time: '2026-10-15T12:40:48.013447'
duration_seconds: 387.72
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hypomagnesemia 7 Renal With Or Without Dilated Cardiomyopathy
  mondo_id: MONDO:0859328
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 18
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 3
  validator_version: 0.3.0
term_validation:
  total_terms: 60
  verified: 53
  not_found: 3
  obsolete: 4
  unverifiable: 0
  confabulation_rate: 0.05
  labels_checked: 31
  labels_matching: 17
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: HP:0001934
    reported_labels:
    - Hypomagnesemia
    ontology_label: Persistent bleeding after trauma
  - term_id: HP:0004840
    reported_labels:
    - Renal salt wasting
    ontology_label: Hypochromic microcytic anemia
  - term_id: HP:0004695
    reported_labels:
    - Nephrocalcinosis
    ontology_label: Calcaneal epiphyseal stippling
  - term_id: HP:0001939
    reported_labels:
    - Hypokalemia
    ontology_label: Abnormality of metabolism/homeostasis
  - term_id: HP:0003125
    reported_labels:
    - Hypercalciuria
    ontology_label: Reduced factor VIII activity
  - term_id: HP:0005157
    reported_labels:
    - "Increased left ventricular end\u2011diastolic diameter"
    ontology_label: Concentric hypertrophic cardiomyopathy
  - term_id: HP:0001298
    reported_labels:
    - Tetany
    ontology_label: Encephalopathy
  - term_id: GO:0031930
    reported_labels:
    - regulation of TOR signaling
    ontology_label: mitochondria-nucleus signaling pathway
  - term_id: GO:0031932
    reported_labels:
    - positive regulation of TOR signaling
    ontology_label: TORC2 complex
  - term_id: GO:0003227
    reported_labels:
    - cardiac muscle cell apoptosis
    ontology_label: right ventricular trabecular myocardium morphogenesis
  - term_id: GO:0055006
    reported_labels:
    - cardiac muscle tissue morphogenesis
    ontology_label: cardiac cell development
  labels_variant: 3
  unresolved_terms:
  - HP:0004740
  - HP:0005158
  - GO:0038218
  obsolete_terms:
  - term_id: MONDO:0005353
    ontology_label: obsolete marijuana dependence
    replaced_by: MONDO:0005689
  - term_id: MONDO:0005024
    ontology_label: obsolete emphysema
    replaced_by: MONDO:0004849
  - term_id: CHEBI:25112
    ontology_label: CHEBI_25112
    replaced_by: CHEBI:18420
  - term_id: GO:0005887
    ontology_label: GO_0005887
    replaced_by: GO:0005886
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypomagnesemia 7 Renal With Or Without Dilated Cardiomyopathy
- **MONDO ID:** MONDO:0859328 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypomagnesemia 7 Renal With Or Without Dilated Cardiomyopathy** covering all of the
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

# Hypomagnesemia 7, Renal, With or Without Dilated Cardiomyopathy (ADKH‑RRAGD / KICA Syndrome)

Renal hypomagnesemia‑7 with or without dilated cardiomyopathy is a newly recognized Mendelian disorder caused by heterozygous, mTOR‑activating missense variants in the small Rag GTPase D gene *RRAGD*, leading to a combined phenotype of kidney salt‑losing tubulopathy, profound hypomagnesemia, and frequently early‑onset dilated cardiomyopathy.[1][2][11][12][15] The renal manifestations include severe renal magnesium wasting, hypokalemia, salt loss, hypercalciuria, and nephrocalcinosis, typically with preserved glomerular filtration rate, while the cardiac phenotype can be life‑threatening and has required heart transplantation in multiple reported children.[1][7][11][12] Mechanistically, auto‑activating RagD variants cause constitutive activation of mTORC1 signaling and impaired activity of MiT/TFE transcription factors (TFEB/TFE3) in renal tubular and cardiac cells, leading to dysregulated electrolyte transport and cardiomyocyte gene expression.[11][12][13][14][18] The disease is autosomal dominant, often due to de novo variants, and remains extremely rare, with only a small number of families and sporadic cases described worldwide, but it has important implications for the understanding of magnesium homeostasis, Rag GTPase biology, and “ragopathies” as an emerging class of human disorders.[10][11][12][14] Clinically, recognition of this entity is vital because the renal phenotype may be relatively stable and amenable to electrolyte supplementation, whereas the cardiomyopathy can present early and progress rapidly, underscoring the need for integrated nephrology–cardiology management and genetic diagnosis.[1][5][7][11][12][15]  

---

## 1. Disease Information

### Overview and nosology

Hypomagnesemia 7, renal, with or without dilated cardiomyopathy is a monogenic kidney–heart syndrome characterized primarily by renal salt‑wasting tubulopathy with marked hypomagnesemia, and variably by severe dilated cardiomyopathy (DCM).[1][4][5][11][12] MedGen and OMIM describe the disorder as a disease in which “renal hypomagnesemia‑7 with or without dilated cardiomyopathy (HOMG7) is characterized primarily by renal salt wasting resulting in hypomagnesemia with secondary effects such as hypokalemia or hypocalcemia,” with many patients developing nephrocalcinosis yet generally preserved renal function, and with age at onset ranging from infancy to young adulthood.[1][4][5][9] A subset of patients develop “severe dilated cardiomyopathy as early as in infancy, which may require heart transplant.”[1][5][9] The original genetic description by Schlingmann and colleagues established a novel disease they termed “autosomal dominant kidney hypomagnesemia (ADKH‑RRAGD)” combining an electrolyte‑losing tubulopathy and DCM.[11][12][15][17]  

Historically, a father–daughter pair with a Bartter‑like tubulopathy, severe hypermagnesuric hypomagnesemia, hypercalciuria, and dilating cardiomyopathy was reported in 2005 as a “new tubular disorder,” with autosomal dominant inheritance suspected but the genetic mechanism unknown.[7] Subsequently, whole‑exome and genome sequencing in similar patients with profound hypomagnesemia, nephrocalcinosis, salt wasting, and cardiomyopathy identified heterozygous missense variants in *RRAGD*, encoding Rag GTPase D, thereby unifying these phenotypes as a single Mendelian entity.[11][12][15][17] In the broader conceptual framework of RagGTPase‑related diseases (“ragopathies”), this condition is now recognized as the prototypical RRAGD‑associated ragopathy characterized by kidney tubulopathy and cardiomyopathy.[14][18]  

From an ontological perspective, the disease corresponds to a Mendelian disorder class and is catalogued in multiple biomedical knowledge bases. OMIM lists it under entry 620152, “Hypomagnesemia 7, renal, with or without dilated cardiomyopathy; HOMG7,” mapping to cytogenetic location 6q15 and phenotype mapping key 3 (well‑defined Mendelian phenotype).[2][3] MedGen assigns concept ID C5774266 with MedGen UID 1824039, classifying it as a “Disease or Syndrome.”[1][4][5][9] The Human Phenotypic Series for hypomagnesemia in MedGen notes that HOMG7 is one member of OMIM phenotypic series PS602014 for familial primary hypomagnesemia disorders.[4] The MONDO ontology term referenced by the user, MONDO:0859328, corresponds to “renal hypomagnesemia‑7 with or without dilated cardiomyopathy,” aligning this disorder with the MONDO unified disease naming framework. Although Orphanet and ICD‑10/ICD‑11 may not yet have a dedicated entry for this specific subtype, it can be cross‑classified under rare hereditary tubulopathies and cardiomyopathies.  

### Key identifiers and synonyms

Key identifiers include OMIM phenotype number 620152 for HOMG7 and OMIM gene entry 608268 for *RRAGD*.[2][3][11][12] MedGen concept ID C5774266 (HOMG7) and MedGen 1824039 index the clinical entity.[1][4][5][9] NCBI Gene ID 58528 denotes *RRAGD* (Ras related GTP binding D), whose associated condition section explicitly lists “Hypomagnesemia 7, renal, with or without dilated cardiomyopathy MedGen: C5774266 OMIM: 620152.”[6]  

Common synonyms and alternative names in the literature and databases include “Hypomagnesemia 7, renal, with or without dilated cardiomyopathy” (HOMG7), “Autosomal dominant kidney hypomagnesemia (ADKH‑RRAGD),” and “kidney tubulopathy and cardiomyopathy (KICA) syndrome,” the latter term being used in the preprint describing the condition.[11][12][15][17] The 2005 clinical description referred to “a new tubular disorder with hypokalaemic metabolic alkalosis, severe hypermagnesuric hypomagnesaemia, hypercalciuria and cardiomyopathy,” which retrospectively matches the RRAGD‑associated phenotype.[7] Within the emerging ragopathy framework, the condition is sometimes referred to as “RRAGD‑associated kidney tubulopathy and dilated cardiomyopathy.”[14][18]  

Relevant ontology terms include the MONDO term for “renal hypomagnesemia‑7 with or without dilated cardiomyopathy” (MONDO:0859328), and broader classes such as MONDO:0005353 for “hereditary hypomagnesemia” and MONDO:0005024 for “dilated cardiomyopathy.” Human Phenotype Ontology terms for key manifestations include *Hypomagnesemia* (HP:0001934), *Renal salt wasting* (HP:0004840), *Nephrocalcinosis* (HP:0004695), *Dilated cardiomyopathy* (HP:0001644), and *Hypokalemia* (HP:0001939).[1][4][5][9][10][11][12]  

### Source and aggregation level

The information available for hypomagnesemia‑7 is largely derived from aggregated disease‑level resources synthesizing individual case reports and small case series. OMIM, MedGen, and NCBI Gene aggregate data from the seminal clinical and genetic studies (Schlingmann et al. 2021) and from subsequent mechanistic and follow‑up publications.[1][2][4][5][6][11][12][15][17] The initial 2005 report by Konrad and colleagues described two patients from one family, and the 2021 OMIM and MedGen entries summarize data from eight children from unrelated families and eight affected members of a large family.[7][11][12][15][17]  

Thus, the disease characterization is based on human clinical observations (case reports and small cohorts), supported by in vitro functional studies of RagD mutants in cell systems (HEK293T, HeLa, and cardiomyocytes), but not yet on large epidemiological datasets or randomized trials.[11][12][13][15][18] There are no electronic health record–based population estimates, and most knowledge comes from carefully phenotyped patients referred to nephrology and cardiology centers and subsequently subjected to exome or genome sequencing.[11][12][15][17]  

---

## 2. Etiology

### Primary causal factors

The primary cause of hypomagnesemia‑7 renal with or without dilated cardiomyopathy is heterozygous missense variants in *RRAGD*, which encodes Rag GTPase D, a small monomeric Ras‑related GTP‑binding protein involved in amino acid signaling to the mechanistic target of rapamycin complex 1 (mTORC1).[2][6][11][12][15][17] OMIM notes that *RRAGD* is “a monomeric guanine nucleotide‑binding protein, or G protein,” and that heterozygous missense mutations in *RRAGD* were identified in eight unrelated patients and eight affected members of a family with HOMG7.[2] Schlingmann et al. state that “in eight children from unrelated families with a tubulopathy characterized by hypomagnesemia, hypokalemia, salt wasting, and nephrocalcinosis, we identified heterozygous missense variants in RRAGD that mostly occurred de novo,” and that a heterozygous variant segregated with the phenotype in eight members of a large family.[11][12][15][17]  

> “In eight children from unrelated families with a tubulopathy characterized by hypomagnesemia, hypokalemia, salt wasting, and nephrocalcinosis, we identified heterozygous missense variants in RRAGD that mostly occurred de novo. Six of these patients also had dilated cardiomyopathy and three underwent heart transplantation.”[11][12][15][17]  

These variants are gain‑of‑function (“auto‑activating”) mutations that constitutively activate RagD and mTORC1 signaling.[11][12][15][18] The disease is therefore best classified etiologically as a monogenic, autosomal dominant, gain‑of‑function disorder of a signaling GTPase, leading to dysregulated nutrient‑sensing mTORC1 signaling and downstream defects in renal electrolyte transport and cardiac function.[2][10][11][12][14][18] There is no evidence for environmental, infectious, or toxic primary causes; the disease manifests in the context of a normal environment due to intrinsic genetic alterations.  

### Genetic risk factors

The major genetic risk factors are specific pathogenic missense variants in *RRAGD* located at highly conserved residues within the GTP‑binding domains (G1–G5 motifs) of RagD.[11][12][14][15] Schlingmann et al. reported multiple disease‑causing variants, including p.Ser76Leu (S76L), p.Thr97Pro (T97P), p.Pro119Leu (P119L), and p.Ile221Lys (I221K), all heterozygous and mostly de novo, affecting conserved amino acids critical for GTP binding and hydrolysis.[11][12][15] The ragopathy review by Rios‑Perez and colleagues summarizes that “Schlingmann et al. reported several families in which affected individuals showed kidney tubulopathy and dilated cardiomyopathy and carried heterozygous RRAGD missense mutations at conserved residues in GTP‑binding domains (S76L, T97P, P119L, I221K).”[14] A more recent study identified an additional pathogenic variant P88L, further expanding the mutational spectrum.[14][18]  

> “Schlingmann et al. reported several families in which affected individuals showed kidney tubulopathy and dilated cardiomyopathy and carried heterozygous RRAGD missense mutations at conserved residues in GTP-binding domains (S76L, T97P, P119L, I221K). This was the first study to underscore the role of RagD in renal electrolyte handling and cardiac function.”[14]  

ClinVar and NCBI Gene list *RRAGD* variants associated with HOMG7 and ADKH‑RRAGD as pathogenic or likely pathogenic, reflecting strong segregation and functional evidence.[6][18] All described causal variants are germline heterozygous missense substitutions rather than truncating or structural variants, and population databases such as gnomAD report extremely low or absent allele frequencies, consistent with their deleterious nature and rarity in the general population.[11][12][14][15] There is currently no evidence for common susceptibility loci, modifier genes, or polygenic contributions; the disease appears to be fully explained by single highly penetrant *RRAGD* variants in known families.[2][11][12][14][15]  

### Environmental and lifestyle risk factors

No specific environmental risk factors have been formally identified for hypomagnesemia‑7 renal with or without cardiomyopathy, and the reported patients do not share any unusual toxin exposure, infectious history, or lifestyle factors beyond what would be expected for children and young adults with severe chronic illness.[11][12][15][17] The tubulopathy is clearly of renal origin, with laboratory evidence of renal magnesium and salt wasting, and there is no suggestion of dietary magnesium deficiency or malabsorption as primary causes.[7][10][11][12]  

It is reasonable to infer that general environmental stressors such as intercurrent infections, dehydration, or high cardiac workload might exacerbate cardiomyopathy in genetically affected individuals, but this has not been systematically studied or quantified.[11][12][13] Likewise, dietary magnesium intake and adherence to supplementation may modulate biochemical severity but are not causal in the absence of *RRAGD* mutations.[10][11][12] No occupational exposures, smoking, or alcohol consumption patterns have been implicated, and most reported cases are pediatric, precluding adult lifestyle risk factor analysis.[7][11][12][15]  

### Protective factors

Genetic protective factors have not been identified for ADKH‑RRAGD. The small number of known families and the rarity of the condition make it difficult to detect modifier alleles that attenuate disease severity. The variability in cardiomyopathy penetrance within families—where some mutation carriers exhibit renal tubulopathy without overt DCM—may reflect stochastic factors, modifier genes, or environmental influences, but no specific protective variants have been reported.[11][12][15][17]  

Environmental or lifestyle protective factors are also poorly defined. Adequate magnesium supplementation, careful management of electrolytes, and early cardiology care plausibly reduce the risk of arrhythmias and heart failure progression, but these are therapeutic rather than intrinsic protective exposures and have not been formally studied in controlled trials.[7][10][11][12] Avoidance of volume depletion and maintenance of euvolemia may help mitigate renal salt‑wasting symptoms, but again, the evidence is circumstantial and based on clinical experience rather than systematic study.[7][11][12]  

### Gene–environment interactions

Given that ADKH‑RRAGD is a monogenic gain‑of‑function disorder, gene–environment interactions likely modulate phenotype expression rather than determine disease occurrence. For example, the same *RRAGD* variant (such as p.Ser76Leu) may cause more severe cardiomyopathy in the setting of high metabolic demand, intercurrent myocarditis, or poor electrolyte control, whereas in other individuals the cardiac phenotype may remain subclinical despite clear biochemical tubulopathy.[11][12][13][14]  

Recent mechanistic work on RagD “ragopathies” emphasizes that auto‑activated RagD is insensitive to upstream nutrient signals and folliculin‑mediated regulation, suggesting that environmental nutrient availability has reduced influence on mTORC1 activity in affected cells.[14] Rios‑Perez et al. note that all reported RRAGD disease‑causing mutations “induce auto‑activation of RagD… which occurred independently of folliculin (FLCN), the GTPase‑activating protein responsible for RagC/D activation,” implying a decoupling of gene function from environmental amino acid levels.[14] This supports the concept that gene–environment interactions are attenuated, with RagD mutants enforcing a constitutively “fed” signal irrespective of environmental nutrient status.  

> “A more recent study reported a new family with a similar phenotype carrying a novel mutation (P88L) in the RRAGD gene and demonstrated that all reported RRAGD disease-causing mutations induce auto-activation of RagD… which occurred independently of folliculin (FLCN), the GTPase-activating protein responsible for RagC/D activation.”[14]  

Overall, ADKH‑RRAGD is best conceptualized etiologically as a rare, autosomal dominant, monogenic gain‑of‑function disease with primary genetic causation and secondary modulation by non‑specific environmental factors, without identified specific risk or protective exposures.  

---

## 3. Phenotypes

### Global clinical picture

The phenotypic spectrum of hypomagnesemia‑7 renal with or without cardiomyopathy spans renal, cardiovascular, neuromuscular, and metabolic manifestations, with variable severity and age of onset.[1][4][5][7][10][11][12][15] MedGen and OMIM summarize the core clinical picture as an electrolyte‑losing tubulopathy characterized by hypomagnesemia, hypokalemia, renal salt wasting, and nephrocalcinosis, with many patients demonstrating hypocalcemia and hyponatremia, and with a subset developing early severe dilated cardiomyopathy.[1][4][5][9][11][12]  

MedGen lists detailed clinical features including “Hypocalcemia,” “Hypokalemia,” “Hypomagnesemia,” “Hyponatremia,” “Metabolic acidosis,” “Elevated left ventricular end‑diastolic diameter,” “Primary dilated cardiomyopathy,” “Reduced left ventricular ejection fraction,” “Tetany,” “Seizure,” “Nephrocalcinosis,” and “Polyuria.”[1] These features reflect metabolic, cardiovascular, neuromuscular, and renal involvement, respectively. The 2005 case report described hypokalaemic metabolic alkalosis, severe hypermagnesuric hypomagnesaemia, hypercalciuria, and dilating cardiomyopathy, underscoring overlapping but not identical acid–base features, with some patients exhibiting metabolic acidosis and others alkalosis depending on tubulopathy profile.[7]  

### Renal phenotypes

Renal manifestations are central to the disease, as it is classified within familial primary hypomagnesemia phenotypic series PS602014.[4][10][11][12] The primary renal phenotype is severe renal magnesium wasting, leading to low serum magnesium levels (hypomagnesemia) with high urinary magnesium excretion (hypermagnesuria), often accompanied by hypercalciuria and nephrocalcinosis.[4][7][10][11][12] In the 2005 father–daughter pair, both patients had “severe hypomagnesaemia due to renal magnesium loss” and “marked hypercalciuria,” with bilateral nephrocalcinosis documented at autopsy in the father.[7] Schlingmann et al. reported “hypomagnesemia, hypokalemia, salt wasting, and nephrocalcinosis” in their cohort, with renal tubulopathy present in all affected individuals.[11][12][15][17]  

> “In eight children from unrelated families with a tubulopathy characterized by hypomagnesemia, hypokalemia, salt wasting, and nephrocalcinosis, we identified heterozygous missense variants in RRAGD…”[11][12][15][17]  

Human Phenotype Ontology terms appropriate for these renal features include *Hypomagnesemia* (HP:0001934), *Renal magnesium wasting* (HP:0004740), *Nephrocalcinosis* (HP:0004695), *Hypercalciuria* (HP:0003125), *Polyuria* (HP:0000103), and *Renal salt wasting* (HP:0004840).[1][4][7][10][11][12] Age of onset for renal features ranges from infancy to young adulthood; some patients present in infancy with failure to thrive and electrolyte disturbances, whereas others are diagnosed in childhood or adolescence when nephrocalcinosis and salt wasting become apparent.[1][5][7][11][12] Severity of hypomagnesemia is generally marked, often requiring high‑dose oral supplementation; hypermagnesuria is described as “severe” in the Bartter‑like phenotype report.[7] These abnormalities are chronic but relatively stable over time, with progression mainly manifesting as nephrocalcinosis rather than overt renal failure; renal function is “generally well‑preserved” in MedGen and OMIM summaries.[1][4][5][9][10][11][12]  

Quality‑of‑life impact of renal manifestations includes chronic fatigue, muscle cramps, and neuromuscular irritability due to hypomagnesemia and hypokalemia, polydipsia and nocturia due to polyuria and salt wasting, and anxiety about kidney calcifications and potential long‑term renal damage.[7][10][11][12] Frequent laboratory monitoring and medication burden (multiple daily electrolyte supplements) also impact daily functioning.  

### Cardiovascular phenotypes

Cardiovascular involvement centers on dilated cardiomyopathy with reduced left ventricular ejection fraction and increased left ventricular end‑diastolic diameter.[1][7][11][12][15] MedGen lists “Primary dilated cardiomyopathy,” “Elevated left ventricular end‑diastolic diameter,” and “Reduced left ventricular ejection fraction” as characteristic features.[1] In Schlingmann’s cohort, six of eight children from unrelated families had early and severe DCM, and three underwent heart transplantation, emphasizing the life‑threatening nature of the cardiac phenotype.[11][12][15][17] Konrad’s 2005 report described dilating cardiomyopathy diagnosed at age 9 in the daughter, with fatal outcome in the father; calcium crystal deposits and extensive nephrocalcinosis were observed at autopsy, suggesting systemic mineral dysregulation.[7]  

> “Six of these patients also had dilated cardiomyopathy and three underwent heart transplantation.”[11][12][15][17]  

Appropriate HPO terms for cardiac features include *Dilated cardiomyopathy* (HP:0001644), *Reduced left ventricular ejection fraction* (HP:0005158), *Increased left ventricular end‑diastolic diameter* (HP:0005157), and *Heart failure* (HP:0001635).[1][7][11][12] Age of onset typically falls in infancy or early childhood, with some patients presenting as early as infancy with heart failure signs, while others develop DCM later in childhood.[1][5][7][11][12][15] Severity is often severe, with some requiring transplantation and others dying of cardiac complications.[7][11][12] Progression appears rapid once DCM manifests, but in mutation carriers without overt cardiomyopathy, cardiac function can remain preserved for years, suggesting incomplete penetrance for the cardiac component.[11][12][15][17]  

Quality‑of‑life impact of cardiomyopathy is substantial, involving exercise intolerance, dyspnea, chronic fatigue, hospitalizations, and psychological burden of severe chronic heart disease at a young age. Patients undergoing heart transplantation face the risks and lifelong immunosuppression associated with transplant care, further compounding morbidity.[7][11][12]  

### Neuromuscular and metabolic phenotypes

Hypomagnesemia, hypokalemia, and sometimes hypocalcemia contribute to neuromuscular and metabolic manifestations. MedGen lists “Tetany” and “Seizure” as features, reflecting neuromuscular hyperexcitability and occasional seizure activity due to electrolyte imbalance.[1] Hypocalcemia, hyponatremia, and metabolic acidosis (or alkalosis in some Bartter‑like cases) further complicate metabolic homeostasis.[1][4][7][10][11][12]  

HPO terms such as *Tetany* (HP:0001298), *Seizures* (HP:0001250), *Hypocalcemia* (HP:0002901), *Hyponatremia* (HP:0002902), and *Metabolic acidosis* (HP:0001942) capture these manifestations.[1][4][7][10][11][12] In Konrad’s Bartter‑like family, hypokalaemic metabolic alkalosis dominated the acid–base picture, whereas MedGen and OMIM mention metabolic acidosis, likely reflecting phenotypic heterogeneity across cases.[1][4][7][11][12] Symptom severity can range from mild muscle cramps and fatigue to severe tetany and seizures, especially when electrolyte abnormalities are uncontrolled.  

Quality‑of‑life impacts include chronic muscle pain, weakness, headaches, and the psychological stress associated with recurrent symptomatic episodes requiring urgent medical care. Children may experience school absences and limitations on physical activity due to fatigue and neuromuscular symptoms.  

### Frequency and variability

The limited number of reported cases makes it difficult to precisely quantify phenotype frequencies, but some patterns emerge. Renal hypomagnesemia, hypokalemia, salt wasting, and nephrocalcinosis appear to be near‑universal among genetically confirmed patients.[1][4][7][10][11][12][15] Dilated cardiomyopathy is present in roughly two‑thirds or more of reported individuals, with Schlingmann’s cohort documenting DCM in six of eight sporadic children and several members of the large family; Konrad’s father–daughter pair both had DCM.[7][11][12][15][17] Neuromuscular symptoms and seizures are less systematically reported, but hypomagnesemia‑related tetany and seizure episodes have been noted in some patients.[1][10][11][12]  

Expressivity is clearly variable: within the large family described by Schlingmann, some carriers developed DCM while others exhibited only renal manifestations, and age of onset and severity varied from infancy to young adulthood.[11][12][15][17] This reflects incomplete penetrance for the cardiac phenotype and variable expressivity for both renal and cardiac disease, likely influenced by genetic background and environmental factors.  

---

## 4. Genetic and Molecular Information

### Causal gene and basic properties

The causal gene for hypomagnesemia‑7 renal with or without cardiomyopathy is *RRAGD* (HGNC‑approved symbol RRAGD), encoding Ras‑related GTP binding D, a small Rag GTPase in the Ras superfamily.[2][6][11][12][15][17] OMIM lists *RRAGD* with gene entry 608268, cytogenetic location 6q15, and genomic coordinates (GRCh38) 6:89,364,616–89,412,273.[2] NCBI Gene ID 58528 denotes the human RRAGD locus, and the gene is annotated as “Ras related GTP binding D [Homo sapiens].”[6]  

RRAGD encodes RagD, one of four Rag GTPases (RagA, RagB, RagC, RagD) that form heterodimers (RagA/B–RagC/D) integrating amino acid availability into mTORC1 activation on lysosomal membranes.[10][11][12][14][18] RagD is a small GTP‑binding protein with conserved GTP‑binding domains (G1–G5), and disease‑causing variants cluster at residues within these domains, underscoring the importance of preserved GTPase cycling for normal function.[11][12][14][15] RagD’s expression along the mammalian nephron includes the thick ascending limb (TAL) and distal convoluted tubule (DCT), consistent with the distal tubular electrolyte phenotype.[11][12][15][17]  

### Pathogenic variants

All currently known pathogenic variants for ADKH‑RRAGD are heterozygous missense mutations in *RRAGD* affecting conserved residues in GTP‑binding domains.[2][11][12][14][15] Schlingmann et al. identified multiple variants, including S76L, T97P, P119L, and I221K, which were present in heterozygous state and mostly occurred de novo in sporadic cases, while one variant segregated dominantly in a large family.[11][12][15][17] The ragopathy review notes S76L, T97P, P119L, I221K as prototypical RRAGD disease‑causing mutations, and later work added P88L as a new pathogenic variant.[14][18]  

> “All RagD mutations affect highly conserved amino acid residues in GTP-binding domains conserved in small GTPases (G-domains, G1 to…).”[15]  

These mutations are gain‑of‑function (“auto‑activating”) variants that enhance RagD’s ability to bind mTORC1 components and activate signaling.[11][12][15][18] Functional assays in HEK293T cells showed that all tested RagD mutants exhibited increased binding to Raptor and mTOR (key mTORC1 components) and produced increased phosphorylation of S6K1, a canonical mTORC1 substrate, indicative of constitutive mTORC1 activation.[11][12][15]  

> “All RagD mutants showed increased binding to regulatory associated protein of mTOR (Raptor) and mTOR, the essential components of mTORC1… All human RagD mutants resulted in increased S6K1 phosphorylation in the presence of nutrients, indicative of active mTORC1 signaling.”[12][15]  

ClinVar classifies these variants as pathogenic or likely pathogenic based on segregation data, functional validation, and absence from population databases.[6][18] No loss‑of‑function or truncating *RRAGD* variants have been associated with this phenotype, and it is plausible that complete loss of RagD may produce a different or lethal phenotype not yet described in humans.[10][11][12][14]  

From a variant‑type perspective, all known causal alleles are missense substitutions; no frameshift, nonsense, splice‑site, or structural variants have been reported in ADKH‑RRAGD.[2][11][12][14][15] Allele frequencies in databases such as gnomAD are extremely low or zero, reflecting strong purifying selection against these gain‑of‑function alleles in general populations.[11][12][15][18] The variants are germline and constitutional, present in all tissues, and their dominant nature leads to disease in heterozygotes without requiring biallelic mutation.[11][12][15]  

### Functional consequences and molecular mechanisms

The functional consequence of disease‑causing *RRAGD* variants is gain‑of‑function auto‑activation of RagD, resulting in constitutive activation of mTORC1 signaling and impaired MiT/TFE transcription factor activity.[11][12][13][14][15][18] Schlingmann’s in vitro analyses demonstrated that RagD mutants increase binding to Raptor and mTOR, elevating S6K1 phosphorylation, a downstream effector of mTORC1.[11][12][15] Later work by Rios‑Perez and colleagues and by investigators focusing on the p.Ser76Leu variant showed that auto‑activated RagD impairs TFEB/TFE3 nuclear translocation and activity, thereby downregulating lysosomal and autophagy genes and contributing to kidney tubulopathy and cardiomyopathy.[13][14][18]  

Gene Ontology terms relevant to these functions include *regulation of TOR signaling* (GO:0031930), *positive regulation of protein phosphorylation* (GO:0001934), *cellular response to amino acid stimulus* (GO:0071236), and *mTORC1 signaling* (GO:0038218).[10][11][12][14] UniProt and Pfam annotate RagD as containing canonical P‑loop NTP‑binding domains characteristic of small GTPases, and the disease‑associated mutations disrupt the normal GDP–GTP cycle, favoring persistently GTP‑bound, active states.[10][11][12][14][15]  

At the kidney level, gain‑of‑function RagD and hyperactive mTORC1 signaling are hypothesized to downregulate the TRPM6 channel and other transporters in the distal convoluted tubule, leading to reduced reabsorption of magnesium, calcium, sodium, and potassium.[10][11][12] A recent review on magnesium homeostasis notes that the RRAGD mutations in ADKH‑RRAGD “probably [result] from downregulation of TRPM6,” the key apical magnesium entry channel in DCT cells.[10] At the cardiac level, studies of cardiomyocytes carrying p.Ser76Leu show dysregulated expression of muscle development and cytoskeleton genes, consistent with altered mTORC1 and MiT/TFE signaling.[13]  

> “Altogether, our data demonstrate that gain-of-function variants in RRAGD cause mTORC1 activation in T-REx HeLa cells.”[13]  

These functional consequences are gain‑of‑function rather than dominant‑negative, as the mutants enhance normal RagD signaling rather than directly inhibiting wild‑type protein. There is no evidence for haploinsufficiency or loss of function as the mechanism in this disease.[11][12][14][15]  

### Modifier genes and epigenetic information

No specific modifier genes have been identified for ADKH‑RRAGD. However, given the complexity of mTORC1 signaling, it is plausible that variants in other components of the Ragulator complex, folliculin (FLCN), mTOR, or downstream effectors modulate the penetrance and expressivity of renal and cardiac phenotypes.[10][11][12][14][18] For example, ragopathies involving RRAGC variants manifest primarily as cardiomyopathies with TFEB sequestration, hinting that shared MiT/TFE pathway modifiers might influence phenotype across Rag GTPase disorders.[14]  

Epigenetic changes specific to ADKH‑RRAGD have not been characterized. mTORC1 and MiT/TFE signaling converge on chromatin and transcriptional regulation, suggesting that histone modifications and changes in DNA methylation may occur downstream, but no dedicated epigenomic studies in patient tissues have been reported.[13][14] Given the small patient numbers, large‑scale multi‑omics profiling has not yet been undertaken.  

### Chromosomal abnormalities

Large‑scale chromosomal abnormalities, such as aneuploidies, translocations, inversions, or copy‑number variants, have not been implicated in ADKH‑RRAGD. All reported cases involve single‑nucleotide missense variants in *RRAGD* without accompanying structural rearrangements.[2][11][12][14][15] Chromosomal microarray or karyotyping is therefore not expected to be diagnostic in typical cases, unless a rare structural variant affecting *RRAGD* were to be discovered in the future.  

---

## 5. Environmental Information

### Non‑genetic contributing factors

To date, there is no evidence that specific environmental toxins, pollutants, or occupational exposures causally contribute to hypomagnesemia‑7 renal with or without cardiomyopathy. Reported patients are primarily children and adolescents from diverse geographic and socioeconomic backgrounds, without shared environmental exposures beyond normal living conditions.[7][11][12][15][17] The pathophysiology is driven by intrinsic genetic gain‑of‑function in RagD rather than by environmental damage to kidneys or myocardium.  

While environmental factors such as hydration status, dietary magnesium intake, and comorbid illnesses may modulate the severity of electrolyte disturbances and cardiac stress, they serve as modifiers rather than primary etiologic agents. For example, volume depletion or high salt intake could exacerbate renal salt wasting and polyuria, while intercurrent viral infections might precipitate heart failure exacerbations in patients with underlying DCM.[7][11][12] However, these are non‑specific aggravating factors common to other cardiomyopathies and tubulopathies, not unique triggers for this disorder.  

### Lifestyle factors

Lifestyle factors such as smoking, alcohol consumption, and exercise patterns have not been systematically studied in ADKH‑RRAGD due to the pediatric predominance of reported cases. Children and adolescents with this disease generally have limited lifestyle variability, and their renal and cardiac phenotypes manifest despite otherwise typical environments.[7][11][12]  

Dietary magnesium and calcium intake is important for managing hypomagnesemia and hypercalciuria but does not appear to cause disease in individuals without *RRAGD* mutations. In patients with ADKH‑RRAGD, high doses of oral magnesium, often exceeding recommended dietary allowances, are required to maintain serum levels, suggesting that lifestyle‑level dietary manipulation alone is insufficient to fully correct the renal wasting.[7][10][11][12]  

### Infectious agents

No infectious agents have been implicated as causal or necessary cofactors in ADKH‑RRAGD. Unlike some cardiomyopathies that can be triggered by viral myocarditis, the DCM in ADKH‑RRAGD arises on a background of congenital RagD gain‑of‑function and mTORC1 dysregulation.[11][12][13][14] While infections may exacerbate heart failure in affected individuals, they do not constitute a primary etiologic mechanism.  

In summary, environmental, lifestyle, and infectious factors currently play a secondary, modulatory role in ADKH‑RRAGD, with the disease fundamentally driven by germline *RRAGD* mutations.  

---

## 6. Mechanism and Pathophysiology

### Ordered causal chain from mutation to clinical phenotype

The pathophysiology of hypomagnesemia‑7 renal with or without cardiomyopathy can be conceptualized as a multi‑step causal chain linking *RRAGD* gain‑of‑function variants to renal tubulopathy and cardiac dysfunction. The following table outlines the key steps, acknowledging where inferences extend beyond direct experimental demonstration.  

| Step | Causal description |
|------|--------------------|
| 1 | Heterozygous missense variants in *RRAGD* (e.g., S76L, T97P, P88L, P119L, I221K) alter conserved residues in RagD GTP‑binding domains, leading to gain‑of‑function auto‑activation of RagD.[11][12][14][15] |
| 2 | Auto‑activated RagD increases constitutive binding to the mTORC1 components Raptor and mTOR, resulting in nutrient‑independent hyperactivation of mTORC1 signaling on lysosomal membranes in renal tubular cells and cardiomyocytes.[11][12][15][18] |
| 3 | Hyperactive RagD–mTORC1 signaling impairs MiT/TFE transcription factor (TFEB/TFE3) nuclear translocation and activity, leading to reduced expression of lysosomal, autophagy, and stress‑response genes; this mechanism is demonstrated in in vitro and cardiomyocyte models and inferred in patient tissues.[13][14][18] |
| 4 | In distal nephron cells (TAL and DCT), RagD/mTORC1 hyperactivation and MiT/TFE inhibition downregulate TRPM6 and other electrolyte transporters, causing defective reabsorption of magnesium, calcium, sodium, and potassium; TRPM6 downregulation is inferred from human genetics and animal models of mTORC1–TRPM6 regulation.[10][11][12] |
| 5 | Impaired distal tubular reabsorption leads to renal magnesium wasting, hypermagnesuria, hypercalciuria, salt wasting, hypomagnesemia, hypokalemia, hyponatremia, and nephrocalcinosis, producing the observed electrolyte‑losing tubulopathy with preserved glomerular filtration.[1][4][7][10][11][12][15] |
| 6 | Chronic hypomagnesemia and hypokalemia cause neuromuscular hyperexcitability (tetany, seizures) and may contribute to arrhythmogenic substrate in the heart, while nephrocalcinosis reflects chronic calcium precipitation in renal parenchyma.[1][4][7][10][11][12] |
| 7 | In cardiomyocytes, RagD/mTORC1 hyperactivation and MiT/TFE inhibition dysregulate expression of muscle development and cytoskeleton genes, leading to impaired sarcomeric organization, contractile dysfunction, and mitochondrial and autophagic abnormalities; these changes are demonstrated in T‑REx HeLa cells and cardiomyocyte models.[13][14][18] |
| 8 | Cardiac structural and functional defects manifest clinically as dilated cardiomyopathy with increased left ventricular end‑diastolic diameter, reduced ejection fraction, and progressive heart failure, often requiring heart transplantation.[1][7][11][12][15] |
| 9 | Systemic homeostatic responses to renal salt and magnesium loss (e.g., activation of renin–angiotensin–aldosterone system, changes in parathyroid hormone) may further modulate cardiovascular function and bone–mineral metabolism, contributing to complex clinical patterns; these interactions are inferred from general nephrology knowledge rather than directly demonstrated in ADKH‑RRAGD.[7][10][11][12] |

The upstream steps (1–3) involve molecular signaling events at the level of RagD and mTORC1, while intermediate steps (4–6) describe renal tubular pathophysiology, and downstream steps (7–9) capture cardiac remodeling and systemic consequences.  

### Molecular pathways: RagD, mTORC1, and MiT/TFE signaling

RagD is part of the Rag GTPase family that integrates amino acid signals to regulate mTORC1, a central kinase complex controlling cell growth, metabolism, and autophagy.[10][11][12][14][18] In nutrient‑replete conditions, RagA/B–RagC/D heterodimers recruit mTORC1 to lysosomal membranes where Rheb activates mTORC1, promoting anabolic processes and suppressing autophagy.[10][11][12][14] Disease‑causing *RRAGD* variants disrupt normal RagD cycling, leading to mimicry of the “amino acid–replete” state regardless of actual extracellular or intracellular nutrient levels.[11][12][14][15][18]  

Gene Ontology pathways involved include *positive regulation of TOR signaling* (GO:0031932), *response to amino acid* (GO:0009314), and *regulation of autophagy* (GO:0010506).[10][11][12][14] Hyperactive mTORC1 in ADKH‑RRAGD leads to increased phosphorylation of downstream targets such as S6K1 and 4E‑BP1, driving protein synthesis and inhibiting autophagy.[11][12][15]  

Recent work has emphasized that RagD auto‑activation not only hyperactivates mTORC1 but also impairs MiT/TFE transcription factor activity. TFEB and TFE3 are key regulators of lysosomal biogenesis and autophagy; under stress, they translocate to the nucleus to upregulate genes involved in lysosomal function and cellular clearance.[14][18] In RagD gain‑of‑function, TFEB/TFE3 are sequestered in the cytoplasm and their transcriptional program is suppressed, leading to decreased lysosomal and autophagy gene expression.[14][18] Rios‑Perez et al. conclude that “in kidney tubulopathy and cardiomyopathy the inhibition of TFEB and TFE3, rather than hyperactivation of mTORC1, is the key driver of the disease phenotype.”[14]  

> “Therefore, it appears that in kidney tubulopathy and cardiomyopathy the inhibition of TFEB and TFE3, rather than hyperactivation of mTORC1, is the key driver of the disease phenotype.”[14]  

In T‑REx HeLa cells expressing RRAGD gain‑of‑function variants, investigators observed robust mTORC1 activation and concomitant MiT/TFE impairment, supporting this mechanistic model.[13][18]  

### Cellular processes: tubular transport, autophagy, and cardiomyocyte remodeling

At the cellular level, ADKH‑RRAGD disrupts both transport processes in renal tubular epithelial cells and structural and metabolic processes in cardiomyocytes.[7][10][11][12][13][14][18] In the nephron, RagD is expressed in the thick ascending limb and distal convoluted tubule, segments critical for magnesium, calcium, and sodium reabsorption.[11][12][15][17] mTORC1 signaling in these cells modulates the expression and function of apical channels and basolateral transporters; excessive mTORC1 (and suppressed TFEB/TFE3) likely reduces TRPM6 and other transporters, impairing reabsorptive capacity.[10][11][12]  

The key cellular processes involved include *transmembrane transport* (GO:0055085), *magnesium ion transmembrane transport* (GO:0015693), *calcium ion transport* (GO:0006816), *sodium ion transport* (GO:0006814), and *potassium ion transport* (GO:0006813), as well as *autophagy* (GO:0006914) and *lysosome organization* (GO:0007040).[10][11][12][14] In distal tubule epithelial cells (Cell Ontology term CL:0000066 for epithelial cell; more specifically CL:0002232 for distal tubule epithelial cell), impaired autophagy and lysosomal function may also contribute to cell stress and altered transporter turnover.  

In cardiomyocytes (CL:0000746), RagD/mTORC1 hyperactivation and MiT/TFE inhibition dysregulate muscle development and cytoskeletal gene expression. The p.Ser76Leu variant study reports “dysregulated expression of muscle development and cytoskeleton genes in cardiomyocytes,” consistent with altered sarcomere assembly and cellular architecture.[13] Autophagy suppression may hinder removal of damaged mitochondria and proteins, promoting cardiomyocyte dysfunction and death.^[13][14][18]  

### Protein dysfunction: RagD auto‑activation

The central protein dysfunction in ADKH‑RRAGD is auto‑activation of RagD due to missense substitutions in GTP‑binding domains. RagD normally cycles between GDP‑bound (inactive) and GTP‑bound (active) states, regulated by GTPase‑activating proteins (GAPs) and guanine nucleotide exchange factors (GEFs), including folliculin (FLCN) for RagC/D.[14][15][18] Disease‑causing variants such as S76L and T97P alter the G1 (P‑loop) and other G domains, favoring a constitutively active conformation that binds Raptor/mTOR strongly and is largely insensitive to nutrient deprivation or FLCN regulation.[14][15][18]  

This auto‑activation shifts the mTORC1 equilibrium toward sustained activity, even when amino acids are limiting, leading to persistent suppression of autophagy and MiT/TFE nuclear translocation.[11][12][13][14] Protein structural models and in vitro assays support the idea that these mutations change GDP/GTP binding kinetics and hydrolysis rates, though detailed biophysical characterization is ongoing.[14][15]  

### Metabolic changes and biochemical abnormalities

The primary metabolic changes in ADKH‑RRAGD involve electrolyte homeostasis rather than classic intermediary metabolism pathways. Magnesium, calcium, sodium, and potassium reabsorption defects in the distal nephron lead to systemic hypomagnesemia, hypermagnesuria, hypercalciuria, and hypokalemia, with variable hyponatremia and acid–base disturbances.[1][4][7][10][11][12][15] Magnesium (CHEBI:25112) is a cofactor for numerous enzymes, and its deficiency affects ATP metabolism, neuromuscular function, and cardiac conduction.[10]  

Magnesium homeostasis is tightly regulated, and the kidney plays a crucial role in determining serum levels by adjusting urinary excretion. In ADKH‑RRAGD, distal tubular magnesium transport, particularly via TRPM6, is impaired, leading to high urinary Mg and low serum Mg.[10][11][12] Calcium (CHEBI:29108) handling is also altered, with hypercalciuria and nephrocalcinosis, possibly due to parallel effects on calcium channels and transporters in TAL and DCT.[7][10][11][12]  

Within cardiomyocytes, mTORC1 hyperactivation affects energy metabolism (favoring glycolysis and protein synthesis), mitochondrial function, and autophagy, contributing to inefficient energy utilization and accumulation of damaged organelles.[13][14][18] However, specific metabolomic signatures for ADKH‑RRAGD have not yet been defined.  

Biochemical abnormalities documented in patients include low serum magnesium, low serum potassium, elevated urinary magnesium and calcium, and sometimes metabolic acidosis or alkalosis.[1][4][7][10][11][12] These laboratory findings correspond to LOINC codes such as “Magnesium [Mass/volume] in Serum or Plasma,” “Potassium [Moles/volume] in Serum or Plasma,” and “Calcium [Moles/volume] in Urine.”  

### Tissue damage mechanisms

In the kidney, chronic hypercalciuria and hypermagnesuria promote calcium crystal deposition in renal interstitium and tubules, leading to nephrocalcinosis (UBERON:0001225 for kidney; HP:0004695 for nephrocalcinosis).[7][10][11][12] Konrad’s autopsy of the affected father revealed “dilating cardiomyopathy with calcium crystal deposits… especially in the kidneys, where bilateral nephrocalcinosis was found,” indicating crystallopathy‑related tissue injury.[7] These deposits cause local inflammation, tubular obstruction, and scarring, but overall glomerular filtration remains relatively preserved in most patients.[1][4][7][10][11][12]  

In the heart (UBERON:0000948), tissue damage arises from cardiomyocyte dysfunction and death due to mTORC1‑mediated metabolic stress, impaired autophagy, and cytoskeletal disorganization.[13][14][18] DCM is characterized by ventricular dilation, wall thinning, and reduced contractility, reflecting cumulative cell loss and extracellular matrix remodeling. Gene Ontology terms relevant to cardiac tissue damage include *cardiac muscle cell apoptosis* (GO:0003227), *cardiac muscle tissue morphogenesis* (GO:0055006), and *response to oxidative stress* (GO:0006979).  

### Molecular profiling and advanced technologies

The discovery of ADKH‑RRAGD leveraged advanced genomic technologies, specifically whole‑exome sequencing (WES) and whole‑genome sequencing (WGS), applied to patients with unexplained salt‑losing tubulopathies and cardiomyopathies.[11][12][15][17] Schlingmann et al. performed WES and WGS on multiple patients, identifying *RRAGD* as “a single common mutated gene” after excluding known genes for hypomagnesemia and salt wasting.[15][17]  

> “After exclusion of mutations in known genes for hypomagnesemia and salt wasting, we performed whole-exome sequencing (WES) in individuals F1.1 to F4.1, which revealed RRAGD as a single common mutated gene.”[15]  

Transcriptomic profiling has been applied in cardiomyocyte models carrying RRAGD p.Ser76Leu, revealing “dysregulated expression of muscle development and cytoskeleton genes,” though the detailed gene lists and pathways are beyond the scope of the abstract.[13] Proteomics and metabolomics studies specifically focused on ADKH‑RRAGD have not yet been reported. Single‑cell and spatial transcriptomics analyses, multi‑omics integration (e.g., TCGA‑like consortia), and functional genomics screens (CRISPR, RNAi) have not been applied directly to this rare disease but may be used in future research to dissect cell‑type–specific mechanisms.  

### Upstream vs downstream mechanisms and cell types

Upstream mechanisms in ADKH‑RRAGD include the initial genetic lesion (RRAGD missense variants) and the resulting auto‑activation of RagD and mTORC1.[11][12][14][15] Intermediate mechanisms encompass MiT/TFE inhibition, TRPM6 and transporter downregulation, and impaired autophagy and lysosomal function.[10][13][14][18] Downstream mechanisms include renal electrolyte wasting, nephrocalcinosis, cardiomyocyte remodeling, DCM, and systemic neuromuscular and metabolic symptoms.[1][4][7][10][11][12]  

Key cell types involved, with suggested Cell Ontology terms, include distal convoluted tubule epithelial cells (CL:0002232), thick ascending limb epithelial cells (CL:0002242), cardiomyocytes (CL:0000746), and possibly vascular smooth muscle cells (CL:0000746) and fibroblasts (CL:0000057) in cardiac remodeling. Subcellular compartments central to pathophysiology include lysosomes (GO:0005764), the lysosomal membrane (GO:0005765), cytosol (GO:0005829), nucleus (GO:0005634), and mitochondria (GO:0005739).[10][11][12][14][18]  

Collectively, the mechanistic picture of ADKH‑RRAGD integrates gain‑of‑function RagD signaling, mTORC1 hyperactivation, MiT/TFE inhibition, impaired distal tubular transport, and cardiomyocyte gene dysregulation, producing the observed kidney tubulopathy and dilated cardiomyopathy.  

---

## 7. Anatomical Structures Affected

### Organ‑level involvement

The primary organs affected in hypomagnesemia‑7 renal with or without cardiomyopathy are the kidneys and the heart.[1][4][7][10][11][12][15] The kidneys (UBERON:0001225) are the site of distal tubular dysfunction leading to renal magnesium, calcium, sodium, and potassium wasting, as well as nephrocalcinosis.[1][4][7][10][11][12] RagD expression is documented along the nephron, particularly in the thick ascending limb (UBERON:0004203) and distal convoluted tubule (UBERON:0004204).[11][12][15][17]  

The heart (UBERON:0000948), specifically the left ventricle (UBERON:0002084), manifests dilated cardiomyopathy with increased end‑diastolic diameter and reduced ejection fraction.[1][7][11][12] Cardiac imaging in affected patients shows dilated ventricular chambers and global systolic dysfunction, consistent with DCM pathology.[1][7][11][12][15] At autopsy in the 2005 father, dilating cardiomyopathy and calcium crystal deposits were found in the myocardium, highlighting both functional and structural alterations.[7]  

Secondary organ involvement includes the lungs (UBERON:0002048), liver (UBERON:0002107), and kidneys again, where calcium crystal deposits were observed in Konrad’s autopsy, suggesting systemic calcinosis in severe cases.[7] However, clinically the primary organ systems are renal (urinary system, UBERON:0001008) and cardiovascular (UBERON:0004535), with neuromuscular symptoms reflecting systemic electrolyte disturbances rather than direct nervous system lesions.  

### Tissue and cell‑level involvement

At the tissue level, the renal cortex and medulla contain affected tubular segments in TAL and DCT, composed of epithelial cell monolayers specialized for ion transport.[10][11][12] Distal convoluted tubule epithelial cells (CL:0002232) and thick ascending limb epithelial cells (CL:0002242) express RagD and are likely the primary cell types where RRAGD gain‑of‑function disrupts transporter expression and function.[11][12][15][17]  

In the heart, cardiac muscle tissue (UBERON:0001135) composed of cardiomyocytes (CL:0000746) is directly affected by RagD/mTORC1 hyperactivation and downstream gene expression changes.[13][14][18] Cardiomyocytes exhibit altered sarcomere structure, cytoskeletal organization, and contractile function, leading to tissue‑level dilation and reduced systolic performance. Cardiac fibroblasts (CL:0000057) and endothelial cells (CL:0000115) participate in remodeling and fibrosis secondary to cardiomyocyte dysfunction, though specific studies in ADKH‑RRAGD are lacking.  

### Subcellular compartments

At the subcellular level, key compartments involved include lysosomes (GO:0005764), where RagA/B–RagC/D heterodimers recruit mTORC1; lysosomal membranes (GO:0005765); the cytosol (GO:0005829), where RagD resides; and the nucleus (GO:0005634), where TFEB/TFE3 normally translocate under stress.[10][11][12][14][18] In RagD gain‑of‑function, mTORC1 is constitutively active at lysosomes, and TFEB/TFE3 nuclear translocation is inhibited, leading to cytosolic sequestration and impaired transcription of lysosomal/autophagy genes.[14][18]  

Mitochondria (GO:0005739) are also implicated indirectly, as mTORC1 and autophagy dysregulation can impair mitophagy and mitochondrial quality control, contributing to cardiomyocyte energetic failure.[13][14][18] In renal tubular cells, transporter proteins such as TRPM6 (located at the apical membrane, GO:0005887) and basolateral Na^+/K^+‑ATPases and other exchangers are affected, though specific subcellular localization changes have not been exhaustively mapped in ADKH‑RRAGD.  

### Localization and lateralization

Anatomically, the disease affects both kidneys bilaterally, as evidenced by bilateral nephrocalcinosis in autopsy and imaging.[1][4][7][10][11][12] There is no indication of unilateral kidney involvement; the genetic nature of the condition implies symmetric expression of RagD in both kidneys.  

Cardiac involvement is global, primarily affecting the left ventricle but often involving right ventricular function as DCM progresses. There is no lateralization in the sense of left vs right organ differences beyond normal cardiac physiology; the condition is systemic. Nephrocalcinosis and cardiomyopathy are symmetrical manifestations of bilateral organ dysfunction.  

---

## 8. Temporal Development

### Onset

The age of onset in hypomagnesemia‑7 renal with or without cardiomyopathy is variable, ranging from infancy to young adulthood.[1][4][5][7][11][12][15] MedGen notes that “the age at onset is highly variable, ranging from infancy to young adulthood,” and that a subset of patients develop severe DCM “as early as in infancy.”[1][5][9] In Schlingmann’s cohort, some children presented in infancy with severe hypomagnesemia and salt‑losing tubulopathy, while others were diagnosed later in childhood when nephrocalcinosis or cardiomyopathy surfaced.[11][12][15][17] Konrad’s daughter was diagnosed with DCM at age 9, illustrating pediatric onset for cardiac disease.[7]  

The onset pattern for renal manifestations tends to be chronic and insidious, with early biochemical abnormalities (low magnesium, high urinary magnesium) that may be detected incidentally or through symptoms such as muscle cramps, tetany, or seizures.[1][4][7][10][11][12] Cardiomyopathy onset can be more acute in presentation, with sudden heart failure symptoms in infancy or childhood, though the underlying myocardial remodeling likely develops gradually before clinical recognition.[7][11][12][15]  

Thus, ADKH‑RRAGD can be classified as a congenital/pediatric‑onset disorder with chronic, insidious renal involvement and a variable, sometimes acute‑presenting cardiac component.  

### Progression and disease course

Renal disease course in ADKH‑RRAGD is generally chronic and relatively stable, with nephrocalcinosis developing over time but glomerular filtration remaining preserved in most patients.[1][4][7][10][11][12] MedGen and OMIM emphasize that “renal function is generally well‑preserved,” and there are no reports of end‑stage renal disease in the published cohorts.[1][4][5][9][10][11][12] Electrolyte‑losing tubulopathy remains chronic and lifelong, requiring ongoing supplementation and monitoring.  

Cardiac disease course is more variable and potentially progressive. In Schlingmann’s series, six patients had early and severe DCM; three underwent heart transplantation, indicating progression to end‑stage heart failure in childhood.[11][12][15][17] Konrad’s father died of dilating cardiomyopathy, while the daughter required transplantation, illustrating a progressive, potentially fatal course.[7] In other mutation carriers, cardiomyopathy may be subclinical or absent, suggesting incomplete penetrance and variable progression.[11][12][15][17]  

The overall pattern is therefore a chronic, lifelong renal tubulopathy with a cardiac component that may range from absent to rapidly progressive DCM. There are no formally defined disease stages, but one might conceptually distinguish an “early stage” of isolated renal manifestations, an “intermediate stage” with subclinical cardiac dysfunction, and an “advanced stage” with overt DCM and heart failure.  

### Remission and critical periods

Spontaneous remission of renal or cardiac manifestations has not been reported in ADKH‑RRAGD. Electrolyte abnormalities persist despite supplementation, and nephrocalcinosis does not regress.[1][4][7][10][11][12] Cardiac function may improve temporarily with medical therapy or after transplantation, but underlying genetic susceptibility remains.  

Critical periods include infancy and early childhood, when severe hypomagnesemia and DCM may manifest; timely diagnosis and intervention in this window are crucial for preventing sudden cardiac death and irreversible organ damage.[1][5][7][11][12][15] Another critical period is adolescence and young adulthood, when mutation carriers may present with late‑onset cardiomyopathy; family screening can identify at‑risk individuals during this window, enabling surveillance and early management.[11][12][15][17]  

Given the rarity of the disease and limited longitudinal data, detailed natural history studies are lacking, and much of the temporal understanding is derived from case series rather than large cohorts.  

---

## 9. Inheritance and Population

### Inheritance pattern

Hypomagnesemia‑7 renal with or without cardiomyopathy is inherited in an autosomal dominant pattern.[2][7][11][12][15][17] OMIM explicitly lists the inheritance as autosomal dominant in its phenotype table for HOMG7 (phenotype MIM 620152, inheritance “Autosomal dominant”).[2][3] Schlingmann et al. describe heterozygous missense variants in *RRAGD* that mostly occur de novo in sporadic cases, and a heterozygous variant that segregates dominantly with the phenotype in eight members of a large family.[11][12][15][17] Konrad’s 2005 report of a father–daughter pair with Bartter‑like tubulopathy and cardiomyopathy also suggested autosomal dominant inheritance.[7]  

> “We identified a heterozygous variant in RRAGD that segregated with the phenotype in eight members of a large family with similar kidney manifestations.”[11][12][15][17]  

Penetrance for the renal tubulopathy appears high: all mutation carriers described in the large family had some degree of renal electrolyte‑losing phenotype.[11][12][15][17] Penetrance for cardiomyopathy is incomplete, as some carriers have preserved cardiac function, while others develop severe DCM.[11][12][15][17] Expressivity is variable across individuals, encompassing differences in age of onset, severity of hypomagnesemia, degree of nephrocalcinosis, and presence or absence of cardiomyopathy.[1][4][7][11][12][15]  

There is no evidence for genetic anticipation (

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 60 |
| Resolved | 53 |
| Unresolved (possible confabulation) | 3 |
| Obsolete | 4 |
| Unverifiable | 0 |
| Terms whose name was checked | 31 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001934` (2 mentions) - the report calls it "Hypomagnesemia"; HP calls it **Persistent bleeding after trauma**
- `HP:0004840` (2 mentions) - the report calls it "Renal salt wasting"; HP calls it **Hypochromic microcytic anemia**
- `HP:0004695` (3 mentions) - the report calls it "Nephrocalcinosis"; HP calls it **Calcaneal epiphyseal stippling**
- `HP:0001939` (1 mention) - the report calls it "Hypokalemia"; HP calls it **Abnormality of metabolism/homeostasis**
- `HP:0003125` (1 mention) - the report calls it "Hypercalciuria"; HP calls it **Reduced factor VIII activity**
- `HP:0005157` (1 mention) - the report calls it "Increased left ventricular end‑diastolic diameter"; HP calls it **Concentric hypertrophic cardiomyopathy**
- `HP:0001298` (1 mention) - the report calls it "Tetany"; HP calls it **Encephalopathy**
- `GO:0031930` (1 mention) - the report calls it "regulation of TOR signaling"; GO calls it **mitochondria-nucleus signaling pathway**
- `GO:0031932` (1 mention) - the report calls it "positive regulation of TOR signaling"; GO calls it **TORC2 complex**
- `GO:0003227` (1 mention) - the report calls it "cardiac muscle cell apoptosis"; GO calls it **right ventricular trabecular myocardium morphogenesis**
- `GO:0055006` (1 mention) - the report calls it "cardiac muscle tissue morphogenesis"; GO calls it **cardiac cell development**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0004740` (1 mention), reported as "Renal magnesium wasting" - HP does not contain this term
- `HP:0005158` (1 mention), reported as "Reduced left ventricular ejection fraction" - HP does not contain this term
- `GO:0038218` (1 mention), reported as "mTORC1 signaling" - GO does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `MONDO:0005353` (obsolete marijuana dependence) (1 mention) - replaced by `MONDO:0005689`
- `MONDO:0005024` (obsolete emphysema) (1 mention) - replaced by `MONDO:0004849`
- `CHEBI:25112` (CHEBI_25112) (1 mention) - replaced by `CHEBI:18420`
- `GO:0005887` (GO_0005887) (1 mention) - replaced by `GO:0005886`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0071236` (1 mention) - the report calls it "cellular response to amino acid stimulus"; GO calls it **cellular response to antibiotic**
- `GO:0009314` (1 mention) - the report calls it "response to amino acid"; GO calls it **response to radiation**
- `GO:0015693` (1 mention) - the report calls it "magnesium ion transmembrane transport"; GO calls it **magnesium ion transport**