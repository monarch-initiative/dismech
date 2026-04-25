---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T22:33:51.150339'
end_time: '2026-04-05T22:42:15.789930'
duration_seconds: 504.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: ROS1-Rearranged Non-Small Cell Lung Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 21
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ROS1-Rearranged Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **ROS1-Rearranged Non-Small Cell Lung Cancer** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ROS1-Rearranged Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **ROS1-Rearranged Non-Small Cell Lung Cancer** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


# ROS1-Rearranged Non-Small Cell Lung Cancer (ROS1+ NSCLC): Disease Characteristics Report (2023–2024 emphasis)

## Target disease
- **Disease name:** ROS1-rearranged non-small cell lung cancer (ROS1 fusion–positive NSCLC)
- **Category:** Molecularly-defined subtype of lung adenocarcinoma / NSCLC (oncogene-driven thoracic malignancy) (testa2023ros1rearrangedlungadenocarcinoma pages 1-2)
- **MONDO ID:** Not identified in the retrieved sources in this run (information gap).

---

## 1. Disease information

### Overview (current understanding)
ROS1-rearranged NSCLC is a molecular subset of NSCLC characterized by chromosomal rearrangements that create **ROS1 gene fusions** with constitutive kinase activation, conferring sensitivity to **ROS1 tyrosine kinase inhibitors (TKIs)**. Reviews consistently describe ROS1 fusions in ~**1–2.5%** of NSCLC and occurring **predominantly in lung adenocarcinoma** and often in **never-smokers/younger patients** (testa2023ros1rearrangedlungadenocarcinoma pages 1-2).

**Representative abstract quote (definition/epidemiology):**
- “A molecular subset of NSCLC (1–2.5%) harboring molecular rearrangements of the tyrosine kinase gene ROS1 is defined as ROS1-positive and is almost exclusively diagnosed in patients with lung adenocarcinoma histology, predominantly nonsmokers.” (Testa et al., 2023) (testa2023ros1rearrangedlungadenocarcinoma pages 1-2)

### Common synonyms / alternative names
- ROS1+ NSCLC; ROS1 fusion-positive NSCLC; ROS1-positive lung adenocarcinoma; ROS1-rearranged lung adenocarcinoma (janzic2024nonsmallcelllungcancer pages 11-13, testa2023ros1rearrangedlungadenocarcinoma pages 1-2).

### Key identifiers (ontology/code gaps)
The retrieved sources did not provide explicit mappings to **ICD-10/ICD-11**, **MeSH**, **MONDO**, **Orphanet**, or **OMIM** entries for this molecular subtype (information gap for this run). The disease is typically operationalized in oncology practice/guidelines as **NSCLC with a ROS1 fusion** rather than a standalone nosologic code (boulanger2024advancesandfuture pages 2-3).

### Data provenance
The evidence cited here is derived from:
- **Aggregated disease-level resources** (recent reviews and FDA approval summary) (barbato2024fdaapprovalsummary pages 3-4, boulanger2024advancesandfuture pages 1-2)
- **Prospective interventional clinical trial data** (TRIDENT-1; TRUST-I) (drilon2024repotrectinibinros1 pages 1-3, li2024efficacyandsafety pages 1-2)
- **Prospective biomarker-driven platform trial (liquid biopsy selection)** (BFAST Cohort D) (peters2024entrectinibinros1positive pages 5-6, peters2024entrectinibinros1positive pages 3-4)
- **Real-world retrospective cohort** (ROS1REAL) (janzic2024nonsmallcelllungcancer pages 1-2, janzic2024nonsmallcelllungcancer pages 5-7)

---

## 2. Etiology

### Disease causal factors
**Primary causal factor:** acquisition of oncogenic **ROS1 rearrangements/fusions** (somatic driver alteration). The ROS1 kinase domain is fused to an N-terminal partner gene, yielding constitutive signaling and oncogenic dependency on ROS1 kinase activity (testa2023ros1rearrangedlungadenocarcinoma pages 1-2, testa2023ros1rearrangedlungadenocarcinoma pages 4-5).

### Risk factors and demographics (proxy for etiology)
Across multiple sources, ROS1+ NSCLC is enriched in:
- **Never-smokers** and **younger** patients compared with unselected NSCLC (janzic2024nonsmallcelllungcancer pages 1-2, testa2023ros1rearrangedlungadenocarcinoma pages 1-2).

**TRUST-I (China) demographic data (2024):** median age 55; **58% female**; **73% never smoked** (li2024efficacyandsafety pages 1-2, li2024efficacyandsafety pages 3-5).

### Protective factors / gene–environment interactions
No specific protective factors or gene–environment interaction evidence was present in the retrieved texts (information gap).

---

## 3. Phenotypes (clinical presentation) and natural history

### Core clinical phenotype
Clinical features are those of lung cancer/advanced NSCLC; importantly, patients frequently present with advanced stage and CNS involvement.

**Advanced-stage presentation / CNS disease:** A 2024 review reports that ~**85%** present with **stage IV** disease and **20–40%** have **brain metastases at diagnosis** (boulanger2024advancesandfuture pages 1-2).

**Abstract quote (CNS and resistance framing):**
- “The early-generation ROS1 tyrosine kinase inhibitors (TKIs)… have antitumor activity, but resistance develops in tumors, and intracranial activity is suboptimal.” (Drilon et al., 2024) (drilon2024repotrectinibinros1 pages 1-3)

### Quality of life impact
QoL endpoints were not directly reported in the retrieved excerpts (information gap). However, treatment-emergent neurologic AEs (e.g., dizziness, dysgeusia, neuropathy) are common with some ROS1 TKIs and may affect daily functioning (barbato2024fdaapprovalsummary pages 13-15, drilon2024repotrectinibinros1 pages 7-8).

### Suggested HPO terms (examples; to be validated against specific patient-level descriptions)
Given the lung cancer context and CNS involvement emphasis in this subtype:
- **HP:0002094** Dyspnea (relevant in advanced NSCLC; also appears as an AE context in repotrectinib safety listing) (barbato2024fdaapprovalsummary pages 1-3)
- **HP:0001945** Fever (general cancer symptom; not specifically documented in retrieved excerpts—use cautiously)
- **HP:0001250** Seizure / **HP:0002511** Brain metastasis (brain metastasis is a clinical state; HPO mapping often uses neurologic manifestations—evidence supports frequent brain metastases but not specific neurologic symptom frequencies) (boulanger2024advancesandfuture pages 1-2)
- **HP:0001290** Dizziness (also a common repotrectinib AE, can be recorded as a phenotype/adverse event) (drilon2024repotrectinibinros1 pages 7-8)

*Note:* This run did not retrieve dedicated phenotype frequency tables; additional phenotype-specific sources would be needed for robust HPO frequency annotation.

---

## 4. Genetic / molecular information

### Causal gene and alteration class
- **Causal gene:** **ROS1** (proto-oncogene receptor tyrosine kinase) (testa2023ros1rearrangedlungadenocarcinoma pages 1-2)
- **Alteration type:** Somatic **gene fusion/rearrangement** involving ROS1 kinase domain (structural variant/translocation) (testa2023ros1rearrangedlungadenocarcinoma pages 1-2).

### Common fusion partners (with reported frequencies)
A 2023 review compiled partner frequencies including:
- **CD74–ROS1** ~49.8%
- **EZR–ROS1** ~23.6%
- **SDC4–ROS1** ~9.1%
- **SLC34A2–ROS1** ~5.1% (testa2023ros1rearrangedlungadenocarcinoma pages 4-5)

### Oncogenic mechanisms and pathways
ROS1 fusions signal through canonical RTK pathways including MAPK.
- Example mechanistic detail: EZR–ROS1 and SLC34A2–ROS1 can engage GRB2–SOS1 complexes, activating MAPK signaling (testa2023ros1rearrangedlungadenocarcinoma pages 4-5).

**Suggested GO biological process terms (examples):**
- GO:0007169 **transmembrane receptor protein tyrosine kinase signaling pathway**
- GO:0000165 **MAPK cascade**

### Resistance mechanisms (current understanding)
Resistance emerges under TKI selective pressure and includes:
- **On-target ROS1 kinase domain mutations**, especially **solvent-front ROS1 G2032R**; also gatekeeper and other mutations (e.g., L2026M; S1986F/Y) (barbato2024fdaapprovalsummary pages 4-6, stanzione2023therapeuticaloptionsin pages 7-8).
- **Off-target/bypass mechanisms** (reported in review context) including MAPK pathway activation and MET alterations, among others (testa2023ros1rearrangedlungadenocarcinoma pages 15-16, stanzione2023therapeuticaloptionsin pages 7-8).

**Repotrectinib resistance subgroup results (TRIDENT-1):** 10/17 (59%) responses in baseline **ROS1 G2032R** mutant disease (drilon2024repotrectinibinros1 pages 7-8).

### Epigenetics / multi-omics
No epigenetic or multi-omics profiling results specific to ROS1+ NSCLC were captured in the retrieved excerpts (information gap).

---

## 5. Environmental information
Environmental and lifestyle causal factors specific to developing ROS1 fusions were not described in the retrieved sources. Patient populations are frequently never-smokers (suggesting ROS1 fusions arise in a distinct etiologic context compared with smoking-driven NSCLC), but no specific environmental triggers were identified here (li2024efficacyandsafety pages 1-2).

---

## 6. Mechanism / pathophysiology

### Causal chain (high-level)
1. **Somatic chromosomal rearrangement** generates a **ROS1 fusion** oncoprotein (structural variant). (testa2023ros1rearrangedlungadenocarcinoma pages 1-2)
2. Fusion leads to **constitutive ROS1 kinase signaling** and downstream pathway activation (e.g., MAPK), driving proliferation/survival. (testa2023ros1rearrangedlungadenocarcinoma pages 4-5)
3. Tumor becomes **oncogene addicted** to ROS1 signaling, yielding marked responses to ROS1 TKIs. (boulanger2024advancesandfuture pages 1-2)
4. Under therapy, **acquired resistance** develops (on-target mutations such as **G2032R**, bypass signaling), causing progression; CNS sanctuary sites are clinically important due to variable BBB penetration. (boulanger2024advancesandfuture pages 2-3, stanzione2023therapeuticaloptionsin pages 7-8)

### Cell types (suggested)
- Primary malignant population is typically **lung epithelial tumor cells** (adenocarcinoma lineage) (testa2023ros1rearrangedlungadenocarcinoma pages 1-2).

**Suggested CL terms (examples):**
- CL:0000084 **T cell** (relevance for immunotherapy context; not mechanistically emphasized here)
- CL:0000066 **epithelial cell** (tumor cell-of-origin context)

*Note:* The retrieved sources did not provide single-cell or spatial transcriptomics evidence.

---

## 7. Anatomical structures affected

### Primary organ/system
- **Lung (UBERON:0002048)** as the primary site of malignancy (lung adenocarcinoma predominance) (testa2023ros1rearrangedlungadenocarcinoma pages 1-2).

### Secondary involvement / metastasis
- **Brain/CNS** involvement is common: 20–40% have brain metastases at diagnosis per 2024 review, and intracranial endpoints are central to modern ROS1 TKI development (boulanger2024advancesandfuture pages 1-2, drilon2024repotrectinibinros1 pages 7-8).

---

## 8. Temporal development

### Onset and progression
- Typically adult-onset; many patients present with **advanced (stage IV) disease** (~85% in a 2024 review) (boulanger2024advancesandfuture pages 1-2).
- Disease course in the targeted-therapy era is characterized by **initial response** to ROS1 TKIs and **eventual acquired resistance** with progression, including CNS progression patterns (boulanger2024advancesandfuture pages 1-2, boulanger2024advancesandfuture pages 2-3).

---

## 9. Inheritance and population

### Inheritance
Not inherited in a Mendelian pattern in standard clinical framing; ROS1 fusions are **somatic** tumor alterations (testa2023ros1rearrangedlungadenocarcinoma pages 1-2).

### Epidemiology
- Frequency in NSCLC: typically **~1–2%** (boulanger2024advancesandfuture pages 1-2) and ~**1–2.5%** in another review (testa2023ros1rearrangedlungadenocarcinoma pages 1-2).
- Estimated global annual case count: **~18,500–37,000 new cases worldwide annually** (boulanger2024advancesandfuture pages 1-2).

### Population demographics
- Enrichment in **never-smokers** and **younger** patients (janzic2024nonsmallcelllungcancer pages 1-2, testa2023ros1rearrangedlungadenocarcinoma pages 1-2).
- TRUST-I: 73% never smoked; 58% female (li2024efficacyandsafety pages 1-2).

---

## 10. Diagnostics

### Testing modalities (current practice)
Methods used for ROS1 fusion detection include:
- **FISH**, **IHC**, **RT-PCR**, **NGS** (tissue-based and, increasingly, liquid biopsy-based) (boulanger2024advancesandfuture pages 2-3).

A 2024 expert review notes **“NGS is a preferred method”** (broad profiling and fusion detection), while **liquid biopsy** is useful when tissue is limited but can be less sensitive than tissue NGS (boulanger2024advancesandfuture pages 2-3).

### Liquid biopsy (real-world implementation and performance implication)
**BFAST Cohort D** operationalized an all-blood (ctDNA) selection approach and demonstrated strong entrectinib activity in a liquid-biopsy identified cohort.

**Abstract quote (liquid biopsy value):**
- “Genomic testing in liquid biopsies can be utilized to overcome the inherent limitations of tissue sampling and identify the most appropriate biomarker-informed treatment option for patients.” (Peters et al., 2024) (peters2024entrectinibinros1positive pages 1-2)

### Diagnostic yield statistic from BFAST screening
- Among **5,220 patients screened**, **92 (1.8%)** were ROS1-positive by blood NGS (peters2024entrectinibinros1positive pages 2-3).

---

## 11. Outcome / prognosis

### Targeted-therapy era outcomes (selected)
Modern next-generation ROS1 TKIs yield prolonged systemic disease control in TKI-naïve patients:
- Repotrectinib (TKI-naïve): median PFS **35.7 months** (drilon2024repotrectinibinros1 pages 1-3)
- Taletrectinib TRUST-I (TKI-naïve): 24-month PFS **70.5%** and DoR **78.6%** (li2024efficacyandsafety pages 3-5)

CNS control is a key outcome dimension; repotrectinib shows high intracranial response rates in measurable CNS disease (drilon2024repotrectinibinros1 pages 7-8).

### Prognostic factors (evidence captured here)
- Co-alterations such as **TP53** are discussed as negatively impacting outcomes in review context (and were associated with numerically shorter outcomes in BFAST post hoc analyses) (testa2023ros1rearrangedlungadenocarcinoma pages 15-16, peters2024entrectinibinros1positive pages 5-6).

*Note:* This run did not retrieve population registry (SEER/GBD) 5-year survival statistics specific to ROS1+ NSCLC.

---

## 12. Treatment

### Current applications (approved and guideline-preferred systemic therapies)
A 2024 expert review describes the **preferred FDA-approved first-line therapies** as:
- **Crizotinib**
- **Entrectinib**
- **Repotrectinib** (boulanger2024advancesandfuture pages 1-2)

**Abstract quote (practice framing):**
- “The preferred Food and Drug Administration-approved first-line therapies include crizotinib, entrectinib, and repotrectinib, and currently, selection amongst these options requires consideration of the systemic and CNS efficacy, tolerability, and access to therapy.” (Boulanger et al., 2024) (boulanger2024advancesandfuture pages 1-2)

### Repotrectinib (next-generation ROS1 TKI; FDA approval; TRIDENT-1)
- FDA approval date: **Nov 15, 2023** for adult locally advanced/metastatic ROS1+ NSCLC, based on TRIDENT-1 (NCT03093116) (barbato2024fdaapprovalsummary pages 1-3).
- TRIDENT-1 (NEJM 2024) systemic efficacy:
  - TKI-naïve (n=71): ORR **79%**, median DoR **34.1 months**, median PFS **35.7 months** (drilon2024repotrectinibinros1 pages 1-3).
  - Prior 1 ROS1 TKI, no chemotherapy (n=56): ORR **38%**, median DoR **14.8 months**, median PFS **9.0 months** (drilon2024repotrectinibinros1 pages 1-3).
- Intracranial activity:
  - FDA summary: measurable CNS disease had intracranial responses in **7/8** TKI-naïve and **5/12** pretreated patients (barbato2024fdaapprovalsummary pages 3-4, barbato2024fdaapprovalsummary pages 4-6).
  - NEJM report: measurable brain metastases intracranial responses **8/9 (89%)** in TKI-naïve and **5/13 (38%)** in one-TKI pretreated; estimated 12-month intracranial PFS **91%** and **82%**, respectively (drilon2024repotrectinibinros1 pages 7-8).
- Resistance mutation activity:
  - Baseline **ROS1 G2032R**: ORR **59%** (10/17) (drilon2024repotrectinibinros1 pages 1-3, drilon2024repotrectinibinros1 pages 7-8).
- Key safety signals: dizziness/dysgeusia/paresthesia are common; discontinuation due to treatment-related AEs 3% in NEJM summary (drilon2024repotrectinibinros1 pages 1-3, drilon2024repotrectinibinros1 pages 7-8).

**Abstract quote (repotrectinib efficacy):**
- “Response occurred in 56 of the 71 patients (79%… ) with ROS1 fusion-positive NSCLC who had not previously received a ROS1 TKI…” (Drilon et al., 2024) (drilon2024repotrectinibinros1 pages 1-3)

### Entrectinib (CNS-active ROS1/ALK/TRK inhibitor; BFAST 2024)
- BFAST Cohort D (Nature Medicine 2024; ctDNA-selected): confirmed ORR **81.5% (95% CI 68.6–90.8)**; median PFS **12.9 months (95% CI 8.7–18.5)**; median DoR **13.0 months (95% CI 6.3–18.4)** (peters2024entrectinibinros1positive pages 5-6, peters2024entrectinibinros1positive pages 3-4).
- CNS control: 12-month CNS progression-free rate **86.4%** (IRF) with median time to CNS progression not reached (peters2024entrectinibinros1positive pages 2-3, peters2024entrectinibinros1positive pages 6-7).

### Taletrectinib (next-generation ROS1 TKI; TRUST-I 2024)
- TRUST-I (JCO 2024; NCT04395677; China):
  - TKI-naïve: confirmed ORR **91%**, intracranial confirmed ORR **88%**; median PFS and DoR **not reached** at ~22–23 month follow-up (li2024efficacyandsafety pages 1-2).
  - Crizotinib-pretreated: ORR **52%**, intracranial ORR **73%**; median PFS **7.6 months**; median DoR **10.6 months** (li2024efficacyandsafety pages 1-2).
  - G2032R: **8/12 (67%)** responded (li2024efficacyandsafety pages 1-2).

### Crizotinib (first-generation ROS1 TKI)
Crizotinib established the targeted-therapy paradigm for ROS1+ NSCLC; PROFILE 1001 outcomes summarized in reviews include ORR **72%** and median PFS ~**19.2–19.3 months** and median OS ~**51.4 months**, but with limited BBB penetration and CNS relapses (boulanger2024advancesandfuture pages 2-3, testa2023ros1rearrangedlungadenocarcinoma pages 4-5).

### Sequencing and resistance management (expert analysis)
- Resistance “invariably develops” and subsequent therapy decisions should account for progression pattern and (when known) resistance mechanism (boulanger2024advancesandfuture pages 1-2).
- Next-generation TKIs aim to broaden resistance mutation coverage and improve CNS penetration (boulanger2024advancesandfuture pages 1-2, stanzione2023therapeuticaloptionsin pages 7-8).

### Real-world implementation: ROS1REAL (2024)
In a multicenter retrospective cohort (n=49 advanced cases), first-line utilization and outcomes were:
- First-line distribution: crizotinib **57%**, entrectinib/repotrectinib **29%**, platinum doublet **14%** (janzic2024nonsmallcelllungcancer pages 5-7).
- ORR/DCR: crizotinib **68%/82%** vs newer agents **86%/93%** (janzic2024nonsmallcelllungcancer pages 1-2).
- Median PFS: **1.6 years** (crizotinib) vs **2.35 years** (entrectinib/repotrectinib) (janzic2024nonsmallcelllungcancer pages 1-2).

### Treatment mapping to MAXO (suggestions)
- **ROS1 tyrosine kinase inhibitor therapy** (e.g., crizotinib, entrectinib, repotrectinib, taletrectinib)
- **Antineoplastic chemotherapy** (e.g., platinum doublet)
- **Molecularly targeted therapy**

*Note:* Exact MAXO IDs were not retrieved in this run.

---

## 13. Prevention
No ROS1-specific primary prevention strategies were described in retrieved sources. Secondary prevention in practice relies on lung cancer detection paradigms and, for patients with advanced NSCLC, **comprehensive biomarker testing** before initiating systemic therapy (as emphasized in BFAST background) (peters2024entrectinibinros1positive pages 1-2).

---

## 14. Other species / natural disease
No naturally occurring ROS1-rearranged NSCLC analogs in non-human species were described in retrieved sources (information gap).

---

## 15. Model organisms
The retrieved excerpts reference that ROS1 fusions can be tumorigenic in **transgenic mouse models** (preclinical evidence for oncogenicity), but no specific strain/model identifiers were captured in the provided excerpts (testa2023ros1rearrangedlungadenocarcinoma pages 4-5).

---

## Key 2023–2024 developments (highlights)
1. **Repotrectinib** demonstrated long PFS in TKI-naïve ROS1+ NSCLC (median PFS 35.7 months) and intracranial activity, supporting its **FDA approval (Nov 2023)** and subsequent FDA approval summary publication (2024) (drilon2024repotrectinibinros1 pages 1-3, barbato2024fdaapprovalsummary pages 1-3).
2. **Liquid biopsy-selected treatment** strategy validated in **BFAST Cohort D** for entrectinib, providing prospective evidence that ctDNA-based ROS1 detection can support effective targeted therapy selection (peters2024entrectinibinros1positive pages 1-2, peters2024entrectinibinros1positive pages 5-6).
3. **Taletrectinib TRUST-I (2024)** reported high systemic and intracranial response rates in both TKI-naïve and crizotinib-pretreated populations, including activity in **G2032R** (li2024efficacyandsafety pages 1-2).

---

## Summary table of key trial and real-world statistics

| Therapy | Setting/cohort | N | ORR (95% CI) | mDoR | mPFS | CNS/intracranial data | Notable AEs | Source (with DOI and year) |
|---|---|---:|---|---|---|---|---|---|
| Crizotinib | PROFILE 1001, ROS1+ advanced NSCLC | NR in provided source | 72% | 24.7 mo | 19.3 mo | CNS limitation noted; poor BBB penetration and frequent CNS relapses described | Not detailed in provided source | PROFILE 1001 values summarized in reviews; DOI: 10.3390/onco3030014 (2023); 10.1093/oncolo/oyae205 (2024) (testa2023ros1rearrangedlungadenocarcinoma pages 4-5, boulanger2024advancesandfuture pages 2-3) |
| Entrectinib | BFAST Cohort D, treatment-naive ROS1+ advanced NSCLC identified by liquid biopsy | 55 treated; 54 measurable | 81.5% (68.6–90.8) | 13.0 mo (investigator); 16.7 mo (IRF) | 12.9 mo (investigator); 14.8 mo (IRF, reported elsewhere in paper summary) | 12-mo CNS progression-free rate 83.5% (investigator) and 86.4% (IRF); median time to CNS progression not reached; baseline CNS metastases uncommon | Safety consistent with prior reports; most TRAEs nonserious; no treatment-related deaths reported | Nature Medicine; DOI: 10.1038/s41591-024-03008-4 (2024) (peters2024entrectinibinros1positive pages 2-3, peters2024entrectinibinros1positive pages 5-6, peters2024entrectinibinros1positive pages 3-4) |
| Repotrectinib | TRIDENT-1, ROS1 TKI-naive ROS1+ NSCLC | 71 | 79% (68–88) | 34.1 mo | 35.7 mo | Intracranial responses in 7/8 measurable CNS lesions by FDA summary; NEJM report noted 8/9 (89%) measurable brain metastasis responses and 12-mo intracranial PFS 91% | Dizziness 58–64%, dysgeusia 48–50%, paresthesia/peripheral neuropathy 30–47%, constipation 36–37%, ataxia 28–29%, cognitive disorders 23% | NEJM DOI: 10.1056/NEJMoa2302299 (2024); FDA summary DOI: 10.1158/1078-0432.CCR-24-0949 (2024) (drilon2024repotrectinibinros1 pages 1-3, barbato2024fdaapprovalsummary pages 3-4, barbato2024fdaapprovalsummary pages 13-15, drilon2024repotrectinibinros1 pages 7-8) |
| Repotrectinib | TRIDENT-1, prior 1 ROS1 TKI and no prior chemotherapy | 56 | 38% (25–52) | 14.8 mo | 9.0 mo | Intracranial responses in 5/12 measurable CNS lesions by FDA summary; NEJM report noted 5/13 (38%) and 12-mo intracranial PFS 82% in one-TKI pretreated patients | Similar AE profile as above; discontinuation for treatment-related AEs low (3% in NEJM summary) | NEJM DOI: 10.1056/NEJMoa2302299 (2024); FDA summary DOI: 10.1158/1078-0432.CCR-24-0949 (2024) (drilon2024repotrectinibinros1 pages 1-3, barbato2024fdaapprovalsummary pages 4-6, barbato2024fdaapprovalsummary pages 1-3, drilon2024repotrectinibinros1 pages 7-8) |
| Repotrectinib | TRIDENT-1, ROS1 G2032R subgroup | 17 | 59% (33–82) | NR | NR | Active in resistance-mutation setting; FDA summary also notes responses in 6/8 with resistance mutations after prior ROS1 TKI | Same class-consistent neurologic/sensory AEs | NEJM DOI: 10.1056/NEJMoa2302299 (2024); FDA summary DOI: 10.1158/1078-0432.CCR-24-0949 (2024) (drilon2024repotrectinibinros1 pages 1-3, barbato2024fdaapprovalsummary pages 4-6, drilon2024repotrectinibinros1 pages 7-8) |
| Taletrectinib | TRUST-I, TKI-naive ROS1+ NSCLC | 106 | 91% | NR | NR | Intracranial cORR 88%; 24-mo DOR 78.6%; 24-mo PFS 70.5% | Increased AST 76%, diarrhea 70%, increased ALT 68%; neurologic TEAEs relatively low: dizziness 23%, dysgeusia 10% | JCO; DOI: 10.1200/JCO.24.00731 (2024) (li2024efficacyandsafety pages 1-2, li2024efficacyandsafety pages 3-5) |
| Taletrectinib | TRUST-I, crizotinib-pretreated ROS1+ NSCLC | 67 | 52% | 10.6 mo (95% CI 6.3–NR) | 7.6 mo (95% CI 5.5–12.0) | Intracranial cORR 73% | Same as above; discontinuations due to TEAEs 5%, dose reductions 19% | JCO; DOI: 10.1200/JCO.24.00731 (2024) (li2024efficacyandsafety pages 1-2, li2024efficacyandsafety pages 6-7) |
| Taletrectinib | TRUST-I, ROS1 G2032R subgroup | 12 | 67% (8/12) | NR | NR | Reported activity against acquired resistance mutations; overall acquired-resistance ORR 60% | Predominantly grade 1–2 TEAEs; grade 3–4 TEAEs 43.9% overall | JCO; DOI: 10.1200/JCO.24.00731 (2024) (li2024efficacyandsafety pages 1-2, li2024efficacyandsafety pages 6-7) |
| Real-world patterns | ROS1REAL first-line crizotinib cohort | 28 | 68% | NR | 1.6 y | CNS progression 20% | Any-grade AEs 57%; common grade 1/2 edema, fatigue, transaminase elevation | Current Oncology; DOI: 10.3390/curroncol31080326 (2024) (janzic2024nonsmallcelllungcancer pages 1-2, janzic2024nonsmallcelllungcancer pages 5-7) |
| Real-world patterns | ROS1REAL first-line newer agents (entrectinib/repotrectinib) | 14 | 86% | NR | 2.35 y | CNS progression 25% | Any-grade AEs 79%; mostly grade 1–2 | Current Oncology; DOI: 10.3390/curroncol31080326 (2024) (janzic2024nonsmallcelllungcancer pages 1-2, janzic2024nonsmallcelllungcancer pages 5-7) |


*Table: This table compares pivotal and real-world efficacy, durability, CNS activity, and adverse-event patterns across major ROS1-targeted therapies in ROS1-positive NSCLC. It is useful for quickly contrasting first-generation and next-generation inhibitors, especially for CNS disease and resistance settings.*

---

## Image-based evidence (key efficacy visualizations)
The TRIDENT-1 NEJM publication includes figures and a results table summarizing systemic and intracranial efficacy for repotrectinib (waterfall plots, Kaplan–Meier PFS, intracranial response/PFS). (drilon2024repotrectinibinros1 media ec1cfcb8, drilon2024repotrectinibinros1 media 29c59cf5, drilon2024repotrectinibinros1 media 7dc28074)

---

## Evidence limitations and gaps for knowledge-base completion
- This run did not retrieve explicit **ontology identifiers** (MONDO/MeSH/ICD) for the molecular subtype.
- Several excerpts lacked **PMIDs**; where absent, **DOIs/URLs and publication months/years** are provided.
- Phenotype frequency (HPO) and QoL outcomes were not systematically captured in available excerpts.
- Prevention, environmental triggers, other species natural disease, and detailed model organism resources require additional targeted searches.


References

1. (testa2023ros1rearrangedlungadenocarcinoma pages 1-2): Ugo Testa, Germana Castelli, and Elvira Pelosi. Ros1-rearranged lung adenocarcinoma: from molecular genetics to target therapy. Onco, 3:189-204, Aug 2023. URL: https://doi.org/10.3390/onco3030014, doi:10.3390/onco3030014. This article has 4 citations.

2. (janzic2024nonsmallcelllungcancer pages 11-13): Urska Janzic, Natalie Maimon Rabinovich, Walid Shalata, Waleed Kian, Katarzyna Szymczak, Rafal Dziadziuszko, Marko Jakopovic, Giannis Mountzios, Adam Pluzanski, Antonio Araujo, Andriani Charpidou, Sameh Daher, and Abed Agbarya. Non-small-cell lung cancer patients harboring ros1 rearrangement: real world testing practices, characteristics and treatment patterns (ros1real study). Current Oncology, 31:4369-4381, Jul 2024. URL: https://doi.org/10.3390/curroncol31080326, doi:10.3390/curroncol31080326. This article has 7 citations.

3. (boulanger2024advancesandfuture pages 2-3): Mary C Boulanger, Jaime L Schneider, and Jessica J Lin. Advances and future directions in ros1 fusion-positive lung cancer. The Oncologist, 29:943-956, Aug 2024. URL: https://doi.org/10.1093/oncolo/oyae205, doi:10.1093/oncolo/oyae205. This article has 28 citations.

4. (barbato2024fdaapprovalsummary pages 3-4): Michael I. Barbato, Diana Bradford, Yi Ren, Stephanie L. Aungst, Claudia P. Miller, Lili Pan, Jeanne F. Zirkelbach, Yangbing Li, Youwei Bi, Jianghong Fan, Manuela Grimstein, Sarah E. Dorff, Anup K. Amatya, Pallavi S. Mishra-Kalyani, Barbara Scepura, Peter Schotland, Opeyemi Udoka, Idara Ojofeitimi, John K. Leighton, Nam A. Rahman, Richard Pazdur, Harpreet Singh, Paul G. Kluetz, and Nicole Drezner. Fda approval summary: repotrectinib for locally advanced or metastatic ros1-positive non-small cell lung cancer. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:3364-3370, Jun 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-0949, doi:10.1158/1078-0432.ccr-24-0949. This article has 19 citations.

5. (boulanger2024advancesandfuture pages 1-2): Mary C Boulanger, Jaime L Schneider, and Jessica J Lin. Advances and future directions in ros1 fusion-positive lung cancer. The Oncologist, 29:943-956, Aug 2024. URL: https://doi.org/10.1093/oncolo/oyae205, doi:10.1093/oncolo/oyae205. This article has 28 citations.

6. (drilon2024repotrectinibinros1 pages 1-3): Alexander Drilon, D. Ross Camidge, Jessica J. Lin, Sang-We Kim, Benjamin J. Solomon, Rafal Dziadziuszko, Benjamin Besse, Koichi Goto, Adrianus Johannes de Langen, Jürgen Wolf, Ki Hyeong Lee, Sanjay Popat, Christoph Springfeld, Misako Nagasaka, Enriqueta Felip, Nong Yang, Vamsidhar Velcheti, Shun Lu, Steven Kao, Christophe Dooms, Matthew G. Krebs, Wenxiu Yao, Muhammad Shaalan Beg, Xiufeng Hu, Denis Moro-Sibilot, Parneet Cheema, Shanna Stopatschinskaja, Minal Mehta, Denise Trone, Armin Graber, Gregory Sims, Yong Yuan, and Byoung Chul Cho. Repotrectinib in ros1 fusion-positive non-small-cell lung cancer. The New England journal of medicine, 390 2:118-131, Jan 2024. URL: https://doi.org/10.1056/nejmoa2302299, doi:10.1056/nejmoa2302299. This article has 248 citations and is from a highest quality peer-reviewed journal.

7. (li2024efficacyandsafety pages 1-2): Wei Li, Anwen Xiong, Nong Yang, Huijie Fan, Qitao Yu, Yanqiu Zhao, Yongsheng Wang, Xue Meng, Jingxun Wu, Ziping Wang, Yunpeng Liu, Xicheng Wang, Xintian Qin, Kaihua Lu, Wu Zhuang, Yizhong Ren, Xianyu Zhang, Bing Yan, Christine M. Lovly, and Caicun Zhou. Efficacy and safety of taletrectinib in chinese patients with <i>ros1+</i> non–small cell lung cancer: the phase ii trust-i study. Journal of Clinical Oncology, 42:2660-2670, Aug 2024. URL: https://doi.org/10.1200/jco.24.00731, doi:10.1200/jco.24.00731. This article has 50 citations and is from a highest quality peer-reviewed journal.

8. (peters2024entrectinibinros1positive pages 5-6): Solange Peters, Shirish M. Gadgeel, Tony Mok, Ernest Nadal, Saadettin Kilickap, Aurélie Swalduz, Jacques Cadranel, Shunichi Sugawara, Chao-Hua Chiu, Chong-Jen Yu, Mor Moskovitz, Tomohiro Tanaka, Rhea Nersesian, Sarah M. Shagan, Margaret Maclennan, Michael Mathisen, Vijay Bhagawati-Prasad, Cheick Diarra, Zoe June Assaf, Venice Archer, and Rafal Dziadziuszko. Entrectinib in ros1-positive advanced non-small cell lung cancer: the phase 2/3 bfast trial. Nature Medicine, 30:1923-1932, Jun 2024. URL: https://doi.org/10.1038/s41591-024-03008-4, doi:10.1038/s41591-024-03008-4. This article has 32 citations and is from a highest quality peer-reviewed journal.

9. (peters2024entrectinibinros1positive pages 3-4): Solange Peters, Shirish M. Gadgeel, Tony Mok, Ernest Nadal, Saadettin Kilickap, Aurélie Swalduz, Jacques Cadranel, Shunichi Sugawara, Chao-Hua Chiu, Chong-Jen Yu, Mor Moskovitz, Tomohiro Tanaka, Rhea Nersesian, Sarah M. Shagan, Margaret Maclennan, Michael Mathisen, Vijay Bhagawati-Prasad, Cheick Diarra, Zoe June Assaf, Venice Archer, and Rafal Dziadziuszko. Entrectinib in ros1-positive advanced non-small cell lung cancer: the phase 2/3 bfast trial. Nature Medicine, 30:1923-1932, Jun 2024. URL: https://doi.org/10.1038/s41591-024-03008-4, doi:10.1038/s41591-024-03008-4. This article has 32 citations and is from a highest quality peer-reviewed journal.

10. (janzic2024nonsmallcelllungcancer pages 1-2): Urska Janzic, Natalie Maimon Rabinovich, Walid Shalata, Waleed Kian, Katarzyna Szymczak, Rafal Dziadziuszko, Marko Jakopovic, Giannis Mountzios, Adam Pluzanski, Antonio Araujo, Andriani Charpidou, Sameh Daher, and Abed Agbarya. Non-small-cell lung cancer patients harboring ros1 rearrangement: real world testing practices, characteristics and treatment patterns (ros1real study). Current Oncology, 31:4369-4381, Jul 2024. URL: https://doi.org/10.3390/curroncol31080326, doi:10.3390/curroncol31080326. This article has 7 citations.

11. (janzic2024nonsmallcelllungcancer pages 5-7): Urska Janzic, Natalie Maimon Rabinovich, Walid Shalata, Waleed Kian, Katarzyna Szymczak, Rafal Dziadziuszko, Marko Jakopovic, Giannis Mountzios, Adam Pluzanski, Antonio Araujo, Andriani Charpidou, Sameh Daher, and Abed Agbarya. Non-small-cell lung cancer patients harboring ros1 rearrangement: real world testing practices, characteristics and treatment patterns (ros1real study). Current Oncology, 31:4369-4381, Jul 2024. URL: https://doi.org/10.3390/curroncol31080326, doi:10.3390/curroncol31080326. This article has 7 citations.

12. (testa2023ros1rearrangedlungadenocarcinoma pages 4-5): Ugo Testa, Germana Castelli, and Elvira Pelosi. Ros1-rearranged lung adenocarcinoma: from molecular genetics to target therapy. Onco, 3:189-204, Aug 2023. URL: https://doi.org/10.3390/onco3030014, doi:10.3390/onco3030014. This article has 4 citations.

13. (li2024efficacyandsafety pages 3-5): Wei Li, Anwen Xiong, Nong Yang, Huijie Fan, Qitao Yu, Yanqiu Zhao, Yongsheng Wang, Xue Meng, Jingxun Wu, Ziping Wang, Yunpeng Liu, Xicheng Wang, Xintian Qin, Kaihua Lu, Wu Zhuang, Yizhong Ren, Xianyu Zhang, Bing Yan, Christine M. Lovly, and Caicun Zhou. Efficacy and safety of taletrectinib in chinese patients with <i>ros1+</i> non–small cell lung cancer: the phase ii trust-i study. Journal of Clinical Oncology, 42:2660-2670, Aug 2024. URL: https://doi.org/10.1200/jco.24.00731, doi:10.1200/jco.24.00731. This article has 50 citations and is from a highest quality peer-reviewed journal.

14. (barbato2024fdaapprovalsummary pages 13-15): Michael I. Barbato, Diana Bradford, Yi Ren, Stephanie L. Aungst, Claudia P. Miller, Lili Pan, Jeanne F. Zirkelbach, Yangbing Li, Youwei Bi, Jianghong Fan, Manuela Grimstein, Sarah E. Dorff, Anup K. Amatya, Pallavi S. Mishra-Kalyani, Barbara Scepura, Peter Schotland, Opeyemi Udoka, Idara Ojofeitimi, John K. Leighton, Nam A. Rahman, Richard Pazdur, Harpreet Singh, Paul G. Kluetz, and Nicole Drezner. Fda approval summary: repotrectinib for locally advanced or metastatic ros1-positive non-small cell lung cancer. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:3364-3370, Jun 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-0949, doi:10.1158/1078-0432.ccr-24-0949. This article has 19 citations.

15. (drilon2024repotrectinibinros1 pages 7-8): Alexander Drilon, D. Ross Camidge, Jessica J. Lin, Sang-We Kim, Benjamin J. Solomon, Rafal Dziadziuszko, Benjamin Besse, Koichi Goto, Adrianus Johannes de Langen, Jürgen Wolf, Ki Hyeong Lee, Sanjay Popat, Christoph Springfeld, Misako Nagasaka, Enriqueta Felip, Nong Yang, Vamsidhar Velcheti, Shun Lu, Steven Kao, Christophe Dooms, Matthew G. Krebs, Wenxiu Yao, Muhammad Shaalan Beg, Xiufeng Hu, Denis Moro-Sibilot, Parneet Cheema, Shanna Stopatschinskaja, Minal Mehta, Denise Trone, Armin Graber, Gregory Sims, Yong Yuan, and Byoung Chul Cho. Repotrectinib in ros1 fusion-positive non-small-cell lung cancer. The New England journal of medicine, 390 2:118-131, Jan 2024. URL: https://doi.org/10.1056/nejmoa2302299, doi:10.1056/nejmoa2302299. This article has 248 citations and is from a highest quality peer-reviewed journal.

16. (barbato2024fdaapprovalsummary pages 1-3): Michael I. Barbato, Diana Bradford, Yi Ren, Stephanie L. Aungst, Claudia P. Miller, Lili Pan, Jeanne F. Zirkelbach, Yangbing Li, Youwei Bi, Jianghong Fan, Manuela Grimstein, Sarah E. Dorff, Anup K. Amatya, Pallavi S. Mishra-Kalyani, Barbara Scepura, Peter Schotland, Opeyemi Udoka, Idara Ojofeitimi, John K. Leighton, Nam A. Rahman, Richard Pazdur, Harpreet Singh, Paul G. Kluetz, and Nicole Drezner. Fda approval summary: repotrectinib for locally advanced or metastatic ros1-positive non-small cell lung cancer. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:3364-3370, Jun 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-0949, doi:10.1158/1078-0432.ccr-24-0949. This article has 19 citations.

17. (barbato2024fdaapprovalsummary pages 4-6): Michael I. Barbato, Diana Bradford, Yi Ren, Stephanie L. Aungst, Claudia P. Miller, Lili Pan, Jeanne F. Zirkelbach, Yangbing Li, Youwei Bi, Jianghong Fan, Manuela Grimstein, Sarah E. Dorff, Anup K. Amatya, Pallavi S. Mishra-Kalyani, Barbara Scepura, Peter Schotland, Opeyemi Udoka, Idara Ojofeitimi, John K. Leighton, Nam A. Rahman, Richard Pazdur, Harpreet Singh, Paul G. Kluetz, and Nicole Drezner. Fda approval summary: repotrectinib for locally advanced or metastatic ros1-positive non-small cell lung cancer. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:3364-3370, Jun 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-0949, doi:10.1158/1078-0432.ccr-24-0949. This article has 19 citations.

18. (stanzione2023therapeuticaloptionsin pages 7-8): Brigida Stanzione, Alessandro Del Conte, Elisa Bertoli, Elisa De Carlo, Alberto Revelant, Michele Spina, and Alessandra Bearz. Therapeutical options in ros1—rearranged advanced non small cell lung cancer. International Journal of Molecular Sciences, 24:11495, Jul 2023. URL: https://doi.org/10.3390/ijms241411495, doi:10.3390/ijms241411495. This article has 23 citations.

19. (testa2023ros1rearrangedlungadenocarcinoma pages 15-16): Ugo Testa, Germana Castelli, and Elvira Pelosi. Ros1-rearranged lung adenocarcinoma: from molecular genetics to target therapy. Onco, 3:189-204, Aug 2023. URL: https://doi.org/10.3390/onco3030014, doi:10.3390/onco3030014. This article has 4 citations.

20. (peters2024entrectinibinros1positive pages 1-2): Solange Peters, Shirish M. Gadgeel, Tony Mok, Ernest Nadal, Saadettin Kilickap, Aurélie Swalduz, Jacques Cadranel, Shunichi Sugawara, Chao-Hua Chiu, Chong-Jen Yu, Mor Moskovitz, Tomohiro Tanaka, Rhea Nersesian, Sarah M. Shagan, Margaret Maclennan, Michael Mathisen, Vijay Bhagawati-Prasad, Cheick Diarra, Zoe June Assaf, Venice Archer, and Rafal Dziadziuszko. Entrectinib in ros1-positive advanced non-small cell lung cancer: the phase 2/3 bfast trial. Nature Medicine, 30:1923-1932, Jun 2024. URL: https://doi.org/10.1038/s41591-024-03008-4, doi:10.1038/s41591-024-03008-4. This article has 32 citations and is from a highest quality peer-reviewed journal.

21. (peters2024entrectinibinros1positive pages 2-3): Solange Peters, Shirish M. Gadgeel, Tony Mok, Ernest Nadal, Saadettin Kilickap, Aurélie Swalduz, Jacques Cadranel, Shunichi Sugawara, Chao-Hua Chiu, Chong-Jen Yu, Mor Moskovitz, Tomohiro Tanaka, Rhea Nersesian, Sarah M. Shagan, Margaret Maclennan, Michael Mathisen, Vijay Bhagawati-Prasad, Cheick Diarra, Zoe June Assaf, Venice Archer, and Rafal Dziadziuszko. Entrectinib in ros1-positive advanced non-small cell lung cancer: the phase 2/3 bfast trial. Nature Medicine, 30:1923-1932, Jun 2024. URL: https://doi.org/10.1038/s41591-024-03008-4, doi:10.1038/s41591-024-03008-4. This article has 32 citations and is from a highest quality peer-reviewed journal.

22. (peters2024entrectinibinros1positive pages 6-7): Solange Peters, Shirish M. Gadgeel, Tony Mok, Ernest Nadal, Saadettin Kilickap, Aurélie Swalduz, Jacques Cadranel, Shunichi Sugawara, Chao-Hua Chiu, Chong-Jen Yu, Mor Moskovitz, Tomohiro Tanaka, Rhea Nersesian, Sarah M. Shagan, Margaret Maclennan, Michael Mathisen, Vijay Bhagawati-Prasad, Cheick Diarra, Zoe June Assaf, Venice Archer, and Rafal Dziadziuszko. Entrectinib in ros1-positive advanced non-small cell lung cancer: the phase 2/3 bfast trial. Nature Medicine, 30:1923-1932, Jun 2024. URL: https://doi.org/10.1038/s41591-024-03008-4, doi:10.1038/s41591-024-03008-4. This article has 32 citations and is from a highest quality peer-reviewed journal.

23. (li2024efficacyandsafety pages 6-7): Wei Li, Anwen Xiong, Nong Yang, Huijie Fan, Qitao Yu, Yanqiu Zhao, Yongsheng Wang, Xue Meng, Jingxun Wu, Ziping Wang, Yunpeng Liu, Xicheng Wang, Xintian Qin, Kaihua Lu, Wu Zhuang, Yizhong Ren, Xianyu Zhang, Bing Yan, Christine M. Lovly, and Caicun Zhou. Efficacy and safety of taletrectinib in chinese patients with <i>ros1+</i> non–small cell lung cancer: the phase ii trust-i study. Journal of Clinical Oncology, 42:2660-2670, Aug 2024. URL: https://doi.org/10.1200/jco.24.00731, doi:10.1200/jco.24.00731. This article has 50 citations and is from a highest quality peer-reviewed journal.

24. (drilon2024repotrectinibinros1 media ec1cfcb8): Alexander Drilon, D. Ross Camidge, Jessica J. Lin, Sang-We Kim, Benjamin J. Solomon, Rafal Dziadziuszko, Benjamin Besse, Koichi Goto, Adrianus Johannes de Langen, Jürgen Wolf, Ki Hyeong Lee, Sanjay Popat, Christoph Springfeld, Misako Nagasaka, Enriqueta Felip, Nong Yang, Vamsidhar Velcheti, Shun Lu, Steven Kao, Christophe Dooms, Matthew G. Krebs, Wenxiu Yao, Muhammad Shaalan Beg, Xiufeng Hu, Denis Moro-Sibilot, Parneet Cheema, Shanna Stopatschinskaja, Minal Mehta, Denise Trone, Armin Graber, Gregory Sims, Yong Yuan, and Byoung Chul Cho. Repotrectinib in ros1 fusion-positive non-small-cell lung cancer. The New England journal of medicine, 390 2:118-131, Jan 2024. URL: https://doi.org/10.1056/nejmoa2302299, doi:10.1056/nejmoa2302299. This article has 248 citations and is from a highest quality peer-reviewed journal.

25. (drilon2024repotrectinibinros1 media 29c59cf5): Alexander Drilon, D. Ross Camidge, Jessica J. Lin, Sang-We Kim, Benjamin J. Solomon, Rafal Dziadziuszko, Benjamin Besse, Koichi Goto, Adrianus Johannes de Langen, Jürgen Wolf, Ki Hyeong Lee, Sanjay Popat, Christoph Springfeld, Misako Nagasaka, Enriqueta Felip, Nong Yang, Vamsidhar Velcheti, Shun Lu, Steven Kao, Christophe Dooms, Matthew G. Krebs, Wenxiu Yao, Muhammad Shaalan Beg, Xiufeng Hu, Denis Moro-Sibilot, Parneet Cheema, Shanna Stopatschinskaja, Minal Mehta, Denise Trone, Armin Graber, Gregory Sims, Yong Yuan, and Byoung Chul Cho. Repotrectinib in ros1 fusion-positive non-small-cell lung cancer. The New England journal of medicine, 390 2:118-131, Jan 2024. URL: https://doi.org/10.1056/nejmoa2302299, doi:10.1056/nejmoa2302299. This article has 248 citations and is from a highest quality peer-reviewed journal.

26. (drilon2024repotrectinibinros1 media 7dc28074): Alexander Drilon, D. Ross Camidge, Jessica J. Lin, Sang-We Kim, Benjamin J. Solomon, Rafal Dziadziuszko, Benjamin Besse, Koichi Goto, Adrianus Johannes de Langen, Jürgen Wolf, Ki Hyeong Lee, Sanjay Popat, Christoph Springfeld, Misako Nagasaka, Enriqueta Felip, Nong Yang, Vamsidhar Velcheti, Shun Lu, Steven Kao, Christophe Dooms, Matthew G. Krebs, Wenxiu Yao, Muhammad Shaalan Beg, Xiufeng Hu, Denis Moro-Sibilot, Parneet Cheema, Shanna Stopatschinskaja, Minal Mehta, Denise Trone, Armin Graber, Gregory Sims, Yong Yuan, and Byoung Chul Cho. Repotrectinib in ros1 fusion-positive non-small-cell lung cancer. The New England journal of medicine, 390 2:118-131, Jan 2024. URL: https://doi.org/10.1056/nejmoa2302299, doi:10.1056/nejmoa2302299. This article has 248 citations and is from a highest quality peer-reviewed journal.
