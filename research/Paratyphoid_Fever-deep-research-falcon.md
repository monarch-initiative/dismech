---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T09:19:57.190961'
end_time: '2026-05-08T09:45:17.980927'
duration_seconds: 1520.79
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Paratyphoid Fever
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 53
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Paratyphoid Fever
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Paratyphoid Fever** covering all of the
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
- **Disease Name:** Paratyphoid Fever
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Paratyphoid Fever** covering all of the
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


## Comprehensive Research Report: Paratyphoid Fever (Enteric Fever due to *Salmonella enterica* serovar Paratyphi)

### Executive summary
Paratyphoid fever is a systemic invasive infection (enteric fever) caused by human-adapted *Salmonella enterica* serovars Paratyphi A, Paratyphi B, and Paratyphi C, transmitted primarily via the fecal–oral route through contaminated food and water. (rahman2025comparativeepidemiologyof pages 1-2, chakraborty2024typhoid&paratyphoid pages 1-2, liu2025theglobalburden pages 1-2). Recent work (2023–2025) emphasizes: (i) persistent incidence in South Asia (e.g., Dhaka incidence 27/100,000 person-years in 2018–2020), (ii) increasing importance of antimicrobial resistance (AMR), including emergence of XDR *S. Paratyphi B* lineages in East China with plasmid-mediated efflux upregulation (ramAp→AcrAB-TolC), and (iii) the absence of licensed vaccines targeting Paratyphi A, despite active development of O:2 (OSP) glycoconjugate and live-attenuated candidates (rahman2025comparativeepidemiologyof pages 1-2, peng2024emergenceofrarely pages 1-2, peng2024emergenceofrarely pages 11-12, alfini2024designofa pages 1-2, chakraborty2024typhoid&paratyphoid pages 4-5).

| Topic/Study | Setting & dates | Key quantitative results | Notes/Implications | Source (citation id) |
|---|---|---|---|---|
| Comparative epidemiology of *S. Paratyphi* A vs *S. Typhi* | Urban Bangladesh surveillance; Apr 26, 2018–Mar 15, 2020 | Incidence: paratyphoid 27/100,000 person-years (95% CI 23–32) vs typhoid 216/100,000 person-years (95% CI 198–236); *S. Paratyphi* A represented 23.3% of enteric fever in South Asia; MDR prevalence 0.8% in *S. Paratyphi* A vs 20.2% in *S. Typhi* | Shows much lower incidence and MDR burden for *S. Paratyphi* A than *S. Typhi* in this setting, but overlapping clinical presentation means lab confirmation remains essential | (rahman2025comparativeepidemiologyof pages 1-2) |
| Global burden trend for paratyphoid | GBD analysis, global; 1990–2021 | New paratyphoid cases decreased 73.15% (EAPC -4.77); deaths decreased 65.44% (EAPC -3.74); DALYs decreased 68.42% (EAPC -3.87) | Global burden has declined substantially, but burden remains concentrated in South Asia; highest mortality/DALY rates reported in Pakistan, India, Nepal | (liu2025theglobalburden pages 1-2) |
| Pediatric *S. Paratyphi* A resistance profile | North Delhi tertiary center; Oct 2022–Sep 2023 | 161 culture-positive *Salmonella* isolates: *S. Paratyphi* A 40/161 (24.84%); resistance in *S. Paratyphi* A: ciprofloxacin 42.5%, levofloxacin 55%, cefixime 10%, ceftriaxone 5%, ampicillin 0%, azithromycin 0%, chloramphenicol 0%, cotrimoxazole 0%, norfloxacin 0% | Fluoroquinolone resistance remains the main concern, while susceptibility to several older first-line drugs and azithromycin was preserved in this cohort | (kumar2024antimicrobialsusceptibilityof pages 2-3) |
| Emergence of XDR *S. Paratyphi* B | Jiangsu Province, China; isolates from 2013–2022 | 27 *S. Paratyphi* B isolates total; ST42 (11), ST86 (10), ST2814 (5); 5 MDR isolates total; 4/5 ST2814 isolates were XDR; 17/27 isolates were nearly pan-susceptible | XDR strains were linked to plasmid-mediated resistance and efflux regulation; local phylogenetic clustering suggests adaptation under antibiotic pressure | (peng2024emergenceofrarely pages 1-2, peng2024emergenceofrarely pages 2-4) |
| XDR mechanism highlight in *S. Paratyphi* B | Jiangsu/East China; 2013–2022 | All 4 XDR strains carried an IncHI2A plasmid with **ramAp**; ramAp increased **AcrAB-TolC** efflux expression and elevated MICs to chloramphenicol, azithromycin, tigecycline, tetracycline, nalidixic acid, ciprofloxacin, and sulfamethoxazole; MIC testing covered 21 antibiotics | Important recent mechanistic development: plasmid-borne ramAp plus efflux activation is a key XDR driver and a One Health surveillance target | (peng2024emergenceofrarely pages 11-12) |
| Typhidot rapid test performance | Southern Ghana cross-sectional study; samples collected 2022–2023, published 2024 | Stool culture positivity 14.7% vs blood culture 1.6%; Typhidot sensitivity/specificity vs culture: 35% / 45%; vs PCR: 61% / 53% | Typhidot performed poorly, supporting continued reliance on culture/PCR where available and caution against empiric treatment based on serology alone | (sam2024diagnosticperformanceof pages 1-2) |
| qPCR vs culture for enteric fever diagnosis | Egypt cross-sectional study; published 2025 | Enriched blood qPCR positivity: ttr 90%, InvA 85%; direct blood qPCR positivity: ttr 82%, InvA 80%; blood culture positivity 48%; stool culture positivity 32%; stool culture vs blood culture: sensitivity 66.7%, specificity 100%, accuracy 84%; blood qPCR vs enriched qPCR: ttr sensitivity 91.1%, specificity 100%, accuracy 92%; InvA sensitivity 94.1%, specificity 100%, accuracy 95% | Molecular diagnostics substantially outperformed routine cultures in positivity and showed excellent specificity, though Ct thresholds and low blood bacterial load remain practical issues | (elaskary2025validationofstool pages 1-2, elaskary2025validationofstool pages 4-5) |


*Table: This table summarizes high-yield recent quantitative findings on paratyphoid fever burden, antimicrobial resistance, and diagnostics from 2018-2025. It is useful for quickly comparing epidemiology, resistance trends, and diagnostic performance across major recent studies.*

| Item type | Value | Notes | Supporting source (citation id) |
|---|---|---|---|
| Identifier | Disease name: Paratyphoid fever | Enteric fever caused by *Salmonella enterica* serovars Paratyphi A, B, or C; clinically overlaps with typhoid fever | (rahman2025comparativeepidemiologyof pages 1-2, chakraborty2024typhoid&paratyphoid pages 1-2, liu2025theglobalburden pages 1-2) |
| Identifier | Category: Infectious disease | Human-restricted typhoidal salmonellosis/enteric fever syndrome | (nazir2025combattingsalmonellaa pages 2-3, punchihewagedon2024defensemechanismsof pages 1-2) |
| Identifier | MONDO ID: not found in retrieved sources | Placeholder for knowledge-base curation; no MONDO identifier was recovered in retrieved sources | (rahman2025comparativeepidemiologyof pages 1-2) |
| Identifier | MeSH: not found in retrieved sources | Placeholder for curation; disease-level MeSH identifier not recovered in retrieved sources | (rahman2025comparativeepidemiologyof pages 1-2) |
| Identifier | ICD-10/ICD-11 code: not found in retrieved sources | Placeholder for curation; coding identifier not recovered in retrieved sources | (rahman2025comparativeepidemiologyof pages 1-2) |
| Identifier | Orphanet: not found in retrieved sources | Placeholder for curation; no Orphanet identifier recovered in retrieved sources | (rahman2025comparativeepidemiologyof pages 1-2) |
| Synonym | Enteric fever | Often used for typhoid + paratyphoid together; should be mapped carefully because it is broader than paratyphoid alone | (rahman2025comparativeepidemiologyof pages 1-2, chakraborty2024typhoid&paratyphoid pages 1-2) |
| Synonym | Paratyphoid | Common shorthand form | (liu2025theglobalburden pages 1-2, liao2025paratyphoidfeverand pages 1-7) |
| Synonym | Paratyphoid fever due to *Salmonella* Paratyphi A | Serovar-specific usage in epidemiology and vaccine literature | (rahman2025comparativeepidemiologyof pages 1-2, alfini2024designofa pages 2-4) |
| Synonym | Paratyphoid fever due to *Salmonella* Paratyphi B | Serovar-specific usage, including XDR reports | (peng2024emergenceofrarely pages 1-2, peng2024emergenceofrarely pages 2-4) |
| Synonym | Paratyphoid fever due to *Salmonella* Paratyphi C | Less commonly discussed in retrieved sources but included in disease definition | (rahman2025comparativeepidemiologyof pages 1-2, chakraborty2024typhoid&paratyphoid pages 1-2, liu2025theglobalburden pages 1-2) |
| Ontology term suggestion (HPO) | Fever | Core presenting symptom; suggested HPO label only | (lo2025currentantimicrobialsusceptibility pages 4-5) |
| Ontology term suggestion (HPO) | Diarrhea | Common gastrointestinal symptom in enteric fever | (lo2025currentantimicrobialsusceptibility pages 4-5, sam2024diagnosticperformanceof pages 1-2) |
| Ontology term suggestion (HPO) | Abdominal pain | Common symptom; also relevant to bowel complications | (lo2025currentantimicrobialsusceptibility pages 4-5) |
| Ontology term suggestion (HPO) | Headache | Common constitutional symptom in enteric fever | (lo2025currentantimicrobialsusceptibility pages 4-5) |
| Ontology term suggestion (HPO) | Hepatosplenomegaly | Suggested because hepatosplenomegaly is described in enteric-fever case literature | (han2024infectionbiologyof pages 38-40) |
| Ontology term suggestion (GO) | Bacterial invasion of host epithelial cell | Supported by SPI-1/T3SS-mediated epithelial invasion and membrane ruffling | (ranjan2026salmonellainfectionsglobal pages 7-8, jamil2025emergingantimicrobialresistance pages 3-5) |
| Ontology term suggestion (GO) | Protein secretion by type III secretion system | Central virulence mechanism for SPI-1 and SPI-2 effectors | (ranjan2026salmonellainfectionsglobal pages 7-8, jamil2025emergingantimicrobialresistance pages 3-5) |
| Ontology term suggestion (GO) | Intracellular survival within host cell | Supported by SCV formation and SPI-2-dependent persistence/replication | (ranjan2026salmonellainfectionsglobal pages 7-8, jamil2025emergingantimicrobialresistance pages 3-5) |
| Ontology term suggestion (GO) | Immune evasion | Supported by Vi capsule, complement evasion, reduced neutrophil chemotaxis, altered antigen presentation | (han2024infectionbiologyof pages 32-34, jamil2025emergingantimicrobialresistance pages 9-11) |
| Ontology term suggestion (GO) | Response to bacterium | Broad host-response term appropriate for systemic infection/inflammation | (han2024infectionbiologyof pages 32-34, jamil2025emergingantimicrobialresistance pages 9-11) |
| Ontology term suggestion (CL) | Intestinal epithelial cell | Primary invasion target during early infection | (ranjan2026salmonellainfectionsglobal pages 7-8, jamil2025emergingantimicrobialresistance pages 3-5) |
| Ontology term suggestion (CL) | Microfold cell (M cell) | Entry route across intestinal mucosa | (ranjan2026salmonellainfectionsglobal pages 7-8, jamil2025emergingantimicrobialresistance pages 3-5) |
| Ontology term suggestion (CL) | Macrophage | Major intracellular niche and dissemination cell type | (han2024infectionbiologyof pages 32-34, jamil2025emergingantimicrobialresistance pages 3-5) |
| Ontology term suggestion (CL) | Neutrophil | Relevant to immune evasion; Vi antigen reduces neutrophil recruitment/targeting | (han2024infectionbiologyof pages 32-34) |
| Ontology term suggestion (UBERON) | Terminal ileum | Commonly affected bowel segment in enteric fever imaging/case descriptions | (peng2024emergenceofrarely pages 1-2, jamil2025emergingantimicrobialresistance pages 3-5) |
| Ontology term suggestion (UBERON) | Colon | Gastrointestinal site involved in enteric fever and stool shedding | (sam2024diagnosticperformanceof pages 2-4, lo2025currentantimicrobialsusceptibility pages 4-5) |
| Ontology term suggestion (UBERON) | Liver | Secondary organ involvement during systemic dissemination | (jamil2025emergingantimicrobialresistance pages 3-5) |
| Ontology term suggestion (UBERON) | Spleen | Secondary organ involvement during systemic dissemination | (jamil2025emergingantimicrobialresistance pages 3-5) |
| Ontology term suggestion (UBERON) | Gallbladder | Important site for chronic carriage and biofilm-associated persistence | (jamil2025emergingantimicrobialresistance pages 9-11, jamil2025emergingantimicrobialresistance pages 5-7) |
| Ontology term suggestion (UBERON) | Blood | Key compartment for bacteremia and diagnostic blood culture | (sam2024diagnosticperformanceof pages 2-4, lo2025currentantimicrobialsusceptibility pages 1-2) |
| Ontology term suggestion (MAXO) | Blood culture | Diagnostic gold-standard method in routine care, despite imperfect sensitivity | (sam2024diagnosticperformanceof pages 1-2, sam2024diagnosticperformanceof pages 2-4) |
| Ontology term suggestion (MAXO) | Polymerase chain reaction (PCR) / qPCR | Suggested molecular diagnostic action; includes targets such as *ttr*, *invA*, STY2021 | (elaskary2025validationofstool pages 1-2, sam2024diagnosticperformanceof pages 2-4, elaskary2025validationofstool pages 4-5) |
| Ontology term suggestion (MAXO) | Antibiotic therapy | Mainstay treatment; ceftriaxone/azithromycin/carbapenems used depending on resistance context | (lo2025currentantimicrobialsusceptibility pages 1-2, jamil2025emergingantimicrobialresistance pages 7-9) |
| Ontology term suggestion (MAXO) | Vaccination | No licensed Paratyphi A vaccine yet in retrieved sources, but candidate conjugate/live-attenuated vaccines are in development | (alfini2024designofa pages 2-4, chakraborty2024typhoid&paratyphoid pages 4-5, bansal2024geneticengineeringof pages 3-4) |
| Ontology term suggestion (MAXO) | Water, sanitation, and hygiene intervention (WASH) | Core prevention/public-health action; linked to unsafe water/lack of private toilets | (rahman2025comparativeepidemiologyof pages 1-2, jamil2025emergingantimicrobialresistance pages 7-9) |


*Table: This table summarizes key disease identifiers, synonyms, and ontology term suggestions for a paratyphoid fever knowledge base entry. It also flags missing identifiers in the retrieved sources and links each suggested annotation to supporting evidence.*

### Evidence note on identifiers (ICD/MeSH/MONDO/Orphanet)
Within the retrieved full-text corpus for this run, authoritative identifier codes (ICD-10/ICD-11, MeSH, MONDO, Orphanet) were **not located**; accordingly, they are flagged as “not found in retrieved sources” rather than inferred (artifact-01). This report focuses on evidence-backed clinical and mechanistic content.

---

## 1. Disease Information

### 1.1 Definition and overview (current understanding)
Paratyphoid fever is part of “enteric fever,” a clinically similar syndrome to typhoid fever, but caused by *Salmonella enterica* serovars **Paratyphi A, Paratyphi B, or Paratyphi C** (as opposed to typhoid fever caused by *S. Typhi*) (rahman2025comparativeepidemiologyof pages 1-2, chakraborty2024typhoid&paratyphoid pages 1-2). A GBD-based analysis states that paratyphoid “shares similar clinical characteristics with typhoid fever but is usually milder with a shorter incubation period” (liu2025theglobalburden pages 1-2).

### 1.2 Synonyms and alternate names
Commonly used terms include **enteric fever** (broader umbrella including typhoid + paratyphoid), and serovar-specific labels (e.g., “paratyphoid fever due to *S. Paratyphi A*”) (rahman2025comparativeepidemiologyof pages 1-2, chakraborty2024typhoid&paratyphoid pages 1-2).

### 1.3 Data provenance (individual vs aggregated)
The evidence base combines (i) aggregated global burden modeling (GBD 1990–2021), (ii) prospective or surveillance cohorts (Dhaka 2018–2020 incidence), and (iii) hospital-based microbiology datasets and genomic surveillance (North Delhi pediatric isolates; Jiangsu genomic AMR study) (liu2025theglobalburden pages 1-2, rahman2025comparativeepidemiologyof pages 1-2, kumar2024antimicrobialsusceptibilityof pages 2-3, peng2024emergenceofrarely pages 1-2).

---

## 2. Etiology

### 2.1 Causal factors
Paratyphoid fever is caused by infection with *Salmonella enterica* serovars Paratyphi A/B/C via contaminated food and water (fecal–oral transmission) (chakraborty2024typhoid&paratyphoid pages 1-2, rahman2025comparativeepidemiologyof pages 1-2).

### 2.2 Risk factors (recent emphasis)
**WASH-related exposures:** Lack of safe drinking water and private toilets were associated with enteric fever risk in Dhaka surveillance (rahman2025comparativeepidemiologyof pages 1-2).

**Travel exposure:** In British Columbia (Fraser Health, 2018–2024), 96% of typhoidal Salmonella bacteremias were travel-associated, predominantly to South Asia (lo2025currentantimicrobialsusceptibility pages 2-4).

**Host factors (broader Salmonella/enteric fever literature in retrieved corpus):** Dose-dependence and host susceptibility factors such as gastric hypochlorhydria, age, and immunosuppression are highlighted in a 2024 prevention-focused review, relevant as modifiers of infection risk and severity (zizza2024foodborneinfectionsand pages 6-8).

### 2.3 Protective factors
Direct protective-factor evidence specific to paratyphoid (e.g., immune correlates conferring reduced acquisition risk) was not identified in the retrieved 2023–2025 corpus. Indirectly, prevention strategies (WASH and vaccination against *S. Typhi*) reduce overall enteric fever burden but typhoid vaccines do not reliably protect against paratyphoid (lo2025currentantimicrobialsusceptibility pages 7-8, jamil2025emergingantimicrobialresistance pages 7-9).

### 2.4 Gene–environment interactions
No robust human germline gene–environment interaction evidence specific to paratyphoid fever was identified in the retrieved sources.

---

## 3. Phenotypes

### 3.1 Clinical phenotypes (signs/symptoms)
Clinical presentation overlaps strongly with typhoid fever, requiring laboratory confirmation (rahman2025comparativeepidemiologyof pages 1-2). In a large Canadian cohort of typhoidal Salmonella bacteremia cases, fever (97.8%) and gastrointestinal symptoms (73.5%) were common, illustrating the nonspecific febrile–GI syndrome relevant to paratyphoid (lo2025currentantimicrobialsusceptibility pages 4-5).

**Suggested HPO terms (examples)** are provided in artifact-01; core concepts include fever and diarrhea, with broader systemic manifestations consistent with enteric fever.

### 3.2 Laboratory abnormalities
Specific paratyphoid-focused lab abnormality frequencies were not extracted from the retrieved corpus. The general enteric fever literature and clinical series emphasize the need for microbiological confirmation and susceptibility testing (rahman2025comparativeepidemiologyof pages 1-2, lo2025currentantimicrobialsusceptibility pages 4-5).

### 3.3 Quality-of-life impact
Direct QoL instruments (EQ-5D/SF-36) data specific to paratyphoid were not identified in the retrieved sources.

---

## 4. Genetic/Molecular Information

### 4.1 “Causal genes” and variants
Paratyphoid fever is an infectious disease; there are no human “causal genes” in the Mendelian sense.

### 4.2 Pathogen genomic determinants (AMR and lineages)
**Paratyphi A (Taiwan, 2001–2024 surveillance):** 223 cases were reported; among 88 sequenced isolates, 76.1% were resistant to nalidixic acid and non-susceptible to ciprofloxacin, attributed to **gyrA codon 83** mutations (S83F/S83Y). Domestically acquired infections became predominant after 2022, with genomic relatedness suggesting introduction from Indonesia (liao2025paratyphoidfeverand pages 1-7).

**Paratyphi B (Jiangsu, China, 2013–2022):** Among 27 isolates, predominant STs were ST42 (11), ST86 (10), and ST2814 (5). Four of five ST2814 isolates were **XDR** (peng2024emergenceofrarely pages 1-2). XDR was strongly linked to an IncHI2A plasmid carrying **ramAp**, which increased expression of **AcrAB-TolC efflux** genes and elevated MICs across multiple antibiotic classes (peng2024emergenceofrarely pages 11-12).

---

## 5. Environmental Information

### 5.1 Environmental and lifestyle factors
Transmission is strongly linked to contaminated food and water and poor sanitation (chakraborty2024typhoid&paratyphoid pages 1-2, rahman2025comparativeepidemiologyof pages 1-2). Food safety and safe handling of foods/water are repeatedly highlighted as primary prevention measures, including in travel medicine contexts (lo2025currentantimicrobialsusceptibility pages 7-8, lo2025currentantimicrobialsusceptibility pages 4-5).

### 5.2 Infectious agent
Pathogens: *Salmonella enterica* serovars Paratyphi A, B, C (rahman2025comparativeepidemiologyof pages 1-2, chakraborty2024typhoid&paratyphoid pages 1-2).

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (exposure → disease)
1) **Ingestion and intestinal entry:** Contaminated food/water leads to intestinal exposure; invasion proceeds via epithelial interactions, including M-cell routes (jamil2025emergingantimicrobialresistance pages 3-5, ranjan2026salmonellainfectionsglobal pages 7-8).
2) **Epithelial invasion (upstream):** SPI-1–encoded Type III secretion system (T3SS-1) mediates “trigger” invasion by manipulating host actin (SipA/SipC/SopB/SopE/SopE2) (ranjan2026salmonellainfectionsglobal pages 7-8).
3) **Intracellular survival and systemic spread (downstream):** Following uptake, Salmonella establishes a Salmonella-containing vacuole (SCV) and uses SPI-2/T3SS-2 for intracellular survival/replication and dissemination (ranjan2026salmonellainfectionsglobal pages 7-8, jamil2025emergingantimicrobialresistance pages 3-5).
4) **Immune modulation/evasion:** Typhoidal Salmonella immune-evasion features include the Vi capsule (for certain serovars) that reduces complement/neutrophil recruitment and can target macrophages via DC-SIGN, plus SPI-encoded effectors that modulate NF-κB/MAPK/JNK and antigen presentation (han2024infectionbiologyof pages 32-34, ranjan2026salmonellainfectionsglobal pages 7-8).
5) **AMR as a treatment-modifying mechanism:** Plasmids and mobile elements drive acquisition of AMR; in XDR Paratyphi B, ramAp-mediated efflux upregulation is a key contributor to multi-class resistance (peng2024emergenceofrarely pages 11-12, punchihewagedon2024defensemechanismsof pages 1-2).

### 6.2 Pathways and processes (ontology-ready suggestions)
Suggested GO biological process concepts and relevant immune/epithelial cell types are summarized in artifact-01; key process themes include bacterial invasion, type III secretion, intracellular survival, and immune evasion (ranjan2026salmonellainfectionsglobal pages 7-8, jamil2025emergingantimicrobialresistance pages 3-5, han2024infectionbiologyof pages 32-34).

---

## 7. Anatomical Structures Affected
Primary involvement is gastrointestinal with systemic dissemination (liver, spleen, blood) implied by invasion and macrophage-associated spread; gallbladder involvement is relevant for chronic carriage (jamil2025emergingantimicrobialresistance pages 3-5, jamil2025emergingantimicrobialresistance pages 9-11). Suggested UBERON mappings are provided in artifact-01.

---

## 8. Temporal Development
Paratyphoid typically presents as an acute febrile illness; relative to typhoid, paratyphoid is described as often milder with shorter incubation (liu2025theglobalburden pages 1-2). Detailed stage models specific to paratyphoid were not identified in the retrieved sources.

---

## 9. Inheritance and Population

### 9.1 Epidemiology (recent quantitative data)
**Urban Dhaka, Bangladesh (2018–2020):** incidence for paratyphoid was 27/100,000 person-years (95% CI 23–32), compared with typhoid 216/100,000 person-years (95% CI 198–236), with highest incidence in children age 2–4 (rahman2025comparativeepidemiologyof pages 1-2).

**GBD 1990–2021 trend:** global paratyphoid new cases decreased 73.15% and deaths decreased 65.44% (liu2025theglobalburden pages 1-2).

### 9.2 Population and geography
The burden remains concentrated in South Asia (including Pakistan, India, Nepal for paratyphoid mortality/DALYs in GBD) (liu2025theglobalburden pages 1-2).

---

## 10. Diagnostics

### 10.1 Culture (reference standard, limitations)
Culture remains the diagnostic gold standard but sensitivity is limited and performance varies by specimen type and timing (sam2024diagnosticperformanceof pages 1-2, sam2024diagnosticperformanceof pages 2-4). In Ghana (2022–2023 sampling; published 2024), recovery from stool (14.7%) greatly exceeded blood (1.6%) in a clinically suspected cohort, consistent with shedding dynamics (sam2024diagnosticperformanceof pages 1-2).

### 10.2 Molecular diagnostics (PCR/qPCR)
In Egypt (published 2025), blood-based qPCR targeting **ttr** and **invA** showed far higher positivity than routine cultures: enriched blood qPCR positivity 90% (ttr) and 85% (invA) vs blood culture 48% and stool culture 32% (elaskary2025validationofstool pages 1-2). Compared with enriched qPCR as reference, direct blood qPCR had sensitivity 91.1% (ttr) and 94.1% (invA), with 100% specificity reported in both comparisons (elaskary2025validationofstool pages 4-5).

### 10.3 Rapid serology (RDTs)
Typhidot performed poorly in the Ghana study: sensitivity/specificity vs culture 35%/45%, and vs PCR 61%/53%, implying risk of misdiagnosis and inappropriate antibiotic use in endemic settings if used alone (sam2024diagnosticperformanceof pages 1-2).

**Direct abstract-supported quote (Typhidot performance):** The Ghana study concludes a “sub-optimal performance of the Typhidot RDT… with a higher chance for misdiagnosis and misapplication of antibiotics” (sam2024diagnosticperformanceof pages 1-2).

---

## 11. Outcome / Prognosis
In a large Canadian cohort (2018–2024), outcomes were favorable with effective care: 0% 30-day mortality, 97% clinical cure within 30 days, 3% relapse within 30 days, and median hospitalization 1 day (IQR 1–4) (lo2025currentantimicrobialsusceptibility pages 5-7). Complications included sepsis/septic shock and rare intestinal perforation, indicating potential severity even in high-resource settings (lo2025currentantimicrobialsusceptibility pages 4-5).

---

## 12. Treatment

### 12.1 Antibiotic therapy (real-world practice and resistance constraints)
Modern management is dominated by AMR constraints, especially reduced fluoroquinolone susceptibility. In British Columbia, ciprofloxacin resistance was 96% in 2024 and the authors recommend avoiding empiric ciprofloxacin; ceftriaxone remained ~96–100% susceptible for Typhi and 100% for Paratyphi across years, and azithromycin susceptibility was high with rare nonsusceptible isolates (lo2025currentantimicrobialsusceptibility pages 1-2, lo2025currentantimicrobialsusceptibility pages 5-7). Median effective antibiotic duration was 12 days (IQR 10–14) (lo2025currentantimicrobialsusceptibility pages 4-5).

In Bangladesh surveillance, MDR was far less common in Paratyphi A (0.8%) than Typhi (20.2%), but fluoroquinolone non-susceptibility and rising azithromycin resistance were noted as threats in some settings (rahman2025comparativeepidemiologyof pages 1-2).

### 12.2 MAXO suggestions
Key action ontology suggestions include blood culture, PCR/qPCR, antibiotic therapy, vaccination, and WASH interventions (artifact-01) (lo2025currentantimicrobialsusceptibility pages 1-2, elaskary2025validationofstool pages 1-2, rahman2025comparativeepidemiologyof pages 1-2).

---

## 13. Prevention
Primary prevention is based on **WASH** and safe food/water handling (chakraborty2024typhoid&paratyphoid pages 1-2, rahman2025comparativeepidemiologyof pages 1-2). Travel-focused prevention stresses pre-travel counselling, food/water precautions, and typhoid vaccination (lo2025currentantimicrobialsusceptibility pages 7-8). However, typhoid vaccines “do not protect against paratyphoid” (lo2025currentantimicrobialsusceptibility pages 7-8). This gap is a principal driver of current paratyphoid vaccine development (alfini2024designofa pages 1-2, chakraborty2024typhoid&paratyphoid pages 4-5).

---

## 14. Other Species / Natural Disease
Typhoidal Salmonella (including Paratyphi) are described as **human-restricted** (host range confined to humans), implying **no animal reservoir** for paratyphoid fever transmission in the same way as non-typhoidal Salmonella (nazir2025combattingsalmonellaa pages 2-3, ranjan2026salmonellainfectionsglobal pages 19-20). This contrasts with NTS reservoirs in domestic and wild animals (zizza2024foodborneinfectionsand pages 6-8).

---

## 15. Model Organisms
A key constraint in paratyphoid research is the human restriction of typhoidal Salmonella. Nevertheless, multiple experimental systems are used:

**Rodent models (adapted):** A 2024 review describes a physiological mouse model enabling oral *S. Typhi* infection in wild-type BALB/c mice by co-administering iron (0.32 mg/g body weight) with desferrioxamine (25 mg/kg), achieving liver/spleen/bone marrow involvement similar to humans (chakraborty2024typhoid&paratyphoid pages 6-7). This approach is used for studying pathogenesis and vaccine immunogenicity, and informs paratyphoid modeling strategies.

**In vitro models:** Human intestinal epithelial cell cultures and macrophage/immune-cell assays are widely used to dissect SPI-1 invasion, SCV survival, and immune modulation by effectors such as SteE/SteD/SpvD (ranjan2026salmonellainfectionsglobal pages 7-8).

**Human studies:** Live-attenuated Paratyphi A candidate **CVD 1902 (ΔguaBA ΔclpX)** has been evaluated in Phase 1 humans (single dose ~10^9–10^10 CFU) and elicited CD4+ and CD8+ T-cell responses (bansal2024geneticengineeringof pages 3-4).

---

# Recent developments and latest research highlights (2023–2024 prioritized)

1) **Emergence of XDR Paratyphi B with mechanistic resolution (2024):** East China genomic analysis identifies plasmid-borne **ramAp** as a driver of broad resistance via AcrAB-TolC efflux upregulation, underscoring One Health surveillance needs (peng2024emergenceofrarely pages 11-12).

2) **Paratyphi A vaccine R&D maturation (2024):** A rational-design glycoconjugate study shows immunogenicity depends on O:2 size, saccharide:protein ratio, cross-linking, and O-acetylation, guiding product development (alfini2024designofa pages 1-2). Table/Figure evidence from this paper is shown in the retrieved cropped table/figure regions (alfini2024designofa media c76829e9, alfini2024designofa media 5fca7cec, alfini2024designofa media 6729a2bb).

3) **Diagnostics reality-check in endemic settings (2024):** Typhidot RDT performed poorly versus culture and PCR in Ghana, supporting policy emphasis on validated diagnostics to reduce misapplication of antibiotics (sam2024diagnosticperformanceof pages 1-2).

---

# Expert interpretation / analysis (evidence-based)

* AMR is now a first-order determinant of clinical management strategy. Even in low-MDR settings (e.g., British Columbia), ciprofloxacin resistance levels can be sufficiently high that empiric use is discouraged; third-generation cephalosporins remain highly active in that dataset (lo2025currentantimicrobialsusceptibility pages 1-2, lo2025currentantimicrobialsusceptibility pages 5-7).
* The paratyphoid vaccine gap is increasingly salient because typhoid conjugate vaccines do not protect against Paratyphi A, while Paratyphi A constitutes a meaningful fraction of enteric fever in South Asia and can rise as a proportional contributor (lo2025currentantimicrobialsusceptibility pages 7-8, alfini2024designofa pages 1-2, chakraborty2024typhoid&paratyphoid pages 1-2).
* Diagnostics are not merely confirmatory but stewardship-critical: low-specificity RDTs risk driving unnecessary antibiotic exposure, which can accelerate AMR selection pressure (sam2024diagnosticperformanceof pages 1-2, punchihewagedon2024defensemechanismsof pages 1-2).

---

# Key URLs and publication dates (examples from retrieved sources)

* Rahman et al. (Emerging Infectious Diseases), **Oct 2025**: https://doi.org/10.3201/eid3110.241601 (rahman2025comparativeepidemiologyof pages 1-2)
* Chakraborty & Das (Indian J Med Res), **Nov 2024**: https://doi.org/10.25259/ijmr_1382_2024 (chakraborty2024typhoid&paratyphoid pages 1-2)
* Peng et al. (Antibiotics), **Jun 2024**: https://doi.org/10.3390/antibiotics13060519 (peng2024emergenceofrarely pages 1-2)
* Alfini et al. (Vaccines), **Nov 2024**: https://doi.org/10.3390/vaccines12111272 (alfini2024designofa pages 1-2)
* Sam et al. (BMC Infectious Diseases), **Nov 2024**: https://doi.org/10.1186/s12879-024-10160-2 (sam2024diagnosticperformanceof pages 1-2)
* Lo et al. (Trop Med Infect Dis), **Apr 2025**: https://doi.org/10.3390/tropicalmed10040108 (lo2025currentantimicrobialsusceptibility pages 1-2)

---

## Limitations of this report
* Disease identifier codes (ICD/MeSH/MONDO/Orphanet) were not recovered in the retrieved full texts; this report does not guess them.
* Some template areas (QoL instruments; detailed paratyphoid-specific laboratory abnormality frequencies; controlled human infection model details for paratyphoid) were not available from the retrieved sources in this run.



References

1. (rahman2025comparativeepidemiologyof pages 1-2): Sadia Isfat Ara Rahman, Md Golam Firoj, Se Eun Park, Farhana Khanam, Suneth Agampodi, Kassa Haile, Edilawit Mesfin, Faisal Ahmmed, Md Taufiqul Islam, Ashraful Islam Khan, Fahima Chowdhury, Afroza Akter, Martin Bundi Mwebia, Justin Im, Natasha Y. Rickett, Cecilia Kathure Mbae, Asma Binte Aziz, Beatrice Ongadi, Moses Mwangi, Benjamin Ngugi, Meseret Gebre Behute, Kelvin Kering, Suman Kanungo, Xinxue Liu, Deok Ryun Kim, Andrew J. Pollard, K Zaman, Samuel Kariuki, Firdausi Qadri, and John D. Clemens. Comparative epidemiology of <i>salmonella</i> paratyphi a and <i>salmonella</i> typhi causing enteric fever, bangladesh, 2018–2020. Emerging Infectious Diseases, 31:1922-1934, Oct 2025. URL: https://doi.org/10.3201/eid3110.241601, doi:10.3201/eid3110.241601. This article has 1 citations and is from a domain leading peer-reviewed journal.

2. (chakraborty2024typhoid&paratyphoid pages 1-2): Suparna Chakraborty and Santasabuj Das. Typhoid & paratyphoid vaccine development in the laboratory: a review & in-country experience. The Indian Journal of Medical Research, 160:379-390, Nov 2024. URL: https://doi.org/10.25259/ijmr\_1382\_2024, doi:10.25259/ijmr\_1382\_2024. This article has 3 citations.

3. (liu2025theglobalburden pages 1-2): Guihong Liu, Xin Zhang, Qian Cao, Tao Chen, Binbin Hu, and Huashan Shi. The global burden of typhoid and paratyphoid fever from 1990 to 2021 and the impact on prevention and control. BMC Infectious Diseases, Jul 2025. URL: https://doi.org/10.1186/s12879-025-11223-8, doi:10.1186/s12879-025-11223-8. This article has 18 citations and is from a peer-reviewed journal.

4. (peng2024emergenceofrarely pages 1-2): Jiefu Peng, Jingchao Feng, Hong Ji, Xiaoxiao Kong, Jie Hong, Liguo Zhu, and Huimin Qian. Emergence of rarely reported extensively drug-resistant salmonella enterica serovar paratyphi b among patients in east china. Antibiotics, 13:519, Jun 2024. URL: https://doi.org/10.3390/antibiotics13060519, doi:10.3390/antibiotics13060519. This article has 5 citations.

5. (peng2024emergenceofrarely pages 11-12): Jiefu Peng, Jingchao Feng, Hong Ji, Xiaoxiao Kong, Jie Hong, Liguo Zhu, and Huimin Qian. Emergence of rarely reported extensively drug-resistant salmonella enterica serovar paratyphi b among patients in east china. Antibiotics, 13:519, Jun 2024. URL: https://doi.org/10.3390/antibiotics13060519, doi:10.3390/antibiotics13060519. This article has 5 citations.

6. (alfini2024designofa pages 1-2): Renzo Alfini, Martina Carducci, Luisa Massai, Daniele De Simone, Marco Mariti, Omar Rossi, Simona Rondini, Francesca Micoli, and Carlo Giannelli. Design of a glycoconjugate vaccine against salmonella paratyphi a. Vaccines, 12:1272, Nov 2024. URL: https://doi.org/10.3390/vaccines12111272, doi:10.3390/vaccines12111272. This article has 10 citations.

7. (chakraborty2024typhoid&paratyphoid pages 4-5): Suparna Chakraborty and Santasabuj Das. Typhoid & paratyphoid vaccine development in the laboratory: a review & in-country experience. The Indian Journal of Medical Research, 160:379-390, Nov 2024. URL: https://doi.org/10.25259/ijmr\_1382\_2024, doi:10.25259/ijmr\_1382\_2024. This article has 3 citations.

8. (kumar2024antimicrobialsusceptibilityof pages 2-3): Arvind Kumar, Shekhar Biswas, Sulagna Tripathy, and Sanjay Chattree. Antimicrobial susceptibility of salmonella typhi and paratyphi among pediatric population at tertiary care center of north delhi: a retrospective study. Pediatric Infectious Disease, 6:88-91, Jul 2024. URL: https://doi.org/10.5005/jp-journals-10081-1428, doi:10.5005/jp-journals-10081-1428. This article has 0 citations.

9. (peng2024emergenceofrarely pages 2-4): Jiefu Peng, Jingchao Feng, Hong Ji, Xiaoxiao Kong, Jie Hong, Liguo Zhu, and Huimin Qian. Emergence of rarely reported extensively drug-resistant salmonella enterica serovar paratyphi b among patients in east china. Antibiotics, 13:519, Jun 2024. URL: https://doi.org/10.3390/antibiotics13060519, doi:10.3390/antibiotics13060519. This article has 5 citations.

10. (sam2024diagnosticperformanceof pages 1-2): Emmanuel Kweku Sam, Johnson Alagbo, Avis Asamoah, Felix Ansah, Kwesi Zandoh Tandoh, Lucas N. Amenga-Etego, and Samuel Duodu. Diagnostic performance of typhidot rdt in diagnosis of typhoid fever and antibiotic resistance characterisation in a cross-sectional study in southern ghana. BMC Infectious Diseases, Nov 2024. URL: https://doi.org/10.1186/s12879-024-10160-2, doi:10.1186/s12879-024-10160-2. This article has 6 citations and is from a peer-reviewed journal.

11. (elaskary2025validationofstool pages 1-2): Shymaa A. Elaskary, Hanem Mohamed Badawy, Doaa S. Elgendy, Amany Mohammed Abdelmaksoud, and Rasha G. Mostafa. Validation of stool and blood analysis compared to inv a and ttr based direct blood qpcr assay as diagnostic tools for typhoid fever. BMC Microbiology, Jul 2025. URL: https://doi.org/10.1186/s12866-025-04127-9, doi:10.1186/s12866-025-04127-9. This article has 1 citations and is from a peer-reviewed journal.

12. (elaskary2025validationofstool pages 4-5): Shymaa A. Elaskary, Hanem Mohamed Badawy, Doaa S. Elgendy, Amany Mohammed Abdelmaksoud, and Rasha G. Mostafa. Validation of stool and blood analysis compared to inv a and ttr based direct blood qpcr assay as diagnostic tools for typhoid fever. BMC Microbiology, Jul 2025. URL: https://doi.org/10.1186/s12866-025-04127-9, doi:10.1186/s12866-025-04127-9. This article has 1 citations and is from a peer-reviewed journal.

13. (nazir2025combattingsalmonellaa pages 2-3): Junaid Nazir, Tasaduq Manzoor, Afnan Saleem, Ubaid Gani, Sahar Saleem Bhat, Shabir Khan, Zulfqarul Haq, Priyanka Jha, and Syed Mudasir Ahmad. Combatting salmonella: a focus on antimicrobial resistance and the need for effective vaccination. BMC Infectious Diseases, Jan 2025. URL: https://doi.org/10.1186/s12879-025-10478-5, doi:10.1186/s12879-025-10478-5. This article has 80 citations and is from a peer-reviewed journal.

14. (punchihewagedon2024defensemechanismsof pages 1-2): Anuradha Jeewantha Punchihewage-Don, Priyanka Nilmini Ranaweera, and Salina Parveen. Defense mechanisms of salmonella against antibiotics: a review. Frontiers in Antibiotics, Sep 2024. URL: https://doi.org/10.3389/frabi.2024.1448796, doi:10.3389/frabi.2024.1448796. This article has 44 citations.

15. (liao2025paratyphoidfeverand pages 1-7): Ying-Shu Liao, Yu-Ping Hong, Bo-Han Chen, You-Wun Wan, Ru-Hsiou Teng, Shiu-Yun Liang, Hsiao Lun Wei, Jui-Hsien Chang, Ming-Hao Yang, Chi-Sen Tsao, and Chien-Shun Chiou. Paratyphoid fever and the genomics of salmonella enterica serovar paratyphi a in taiwan. MedRxiv, Apr 2025. URL: https://doi.org/10.1101/2025.04.11.25325632, doi:10.1101/2025.04.11.25325632. This article has 1 citations.

16. (alfini2024designofa pages 2-4): Renzo Alfini, Martina Carducci, Luisa Massai, Daniele De Simone, Marco Mariti, Omar Rossi, Simona Rondini, Francesca Micoli, and Carlo Giannelli. Design of a glycoconjugate vaccine against salmonella paratyphi a. Vaccines, 12:1272, Nov 2024. URL: https://doi.org/10.3390/vaccines12111272, doi:10.3390/vaccines12111272. This article has 10 citations.

17. (lo2025currentantimicrobialsusceptibility pages 4-5): Calvin Ka-Fung Lo, Merisa Mok, Cole Schonhofer, Kevin Afra, and Shazia Masud. Current antimicrobial susceptibility trends and clinical outcomes of typhoidal salmonella in a large health authority in british columbia, canada. Tropical Medicine and Infectious Disease, Apr 2025. URL: https://doi.org/10.3390/tropicalmed10040108, doi:10.3390/tropicalmed10040108. This article has 1 citations.

18. (han2024infectionbiologyof pages 38-40): Jing Han, Nesreen Aljahdali, Shaohua Zhao, Hailin Tang, Heather Harbottle, Maria Hoffmann, Jonathan G. Frye, and Steven L. Foley. Infection biology of <i>salmonella enterica</i>. EcoSal Plus, Dec 2024. URL: https://doi.org/10.1128/ecosalplus.esp-0001-2023, doi:10.1128/ecosalplus.esp-0001-2023. This article has 88 citations.

19. (ranjan2026salmonellainfectionsglobal pages 7-8): Adishi Ranjan, Mahek Chandna, Nicole J. Stevens, Jana Kandil, Brianna Dinh, Macy Kuhn, Noor Mian, Bach Tran, Abdullah Hamid, Peter Kim, and Taseen S. Desin. Salmonella infections: global trends and emerging challenges. Microorganisms, 14:816, Apr 2026. URL: https://doi.org/10.3390/microorganisms14040816, doi:10.3390/microorganisms14040816. This article has 0 citations.

20. (jamil2025emergingantimicrobialresistance pages 3-5): Iqra Jamil, Dr Asad Ur Rehman, Dr Fayyaz Ur Rehman, and Dr Farhan Rasheed. Emerging antimicrobial resistance in typhoid fever: challenges in diagnosis and treatment. Journal of Medical &amp; Health Sciences Review, Jun 2025. URL: https://doi.org/10.62019/a1v2gq57, doi:10.62019/a1v2gq57. This article has 2 citations.

21. (han2024infectionbiologyof pages 32-34): Jing Han, Nesreen Aljahdali, Shaohua Zhao, Hailin Tang, Heather Harbottle, Maria Hoffmann, Jonathan G. Frye, and Steven L. Foley. Infection biology of <i>salmonella enterica</i>. EcoSal Plus, Dec 2024. URL: https://doi.org/10.1128/ecosalplus.esp-0001-2023, doi:10.1128/ecosalplus.esp-0001-2023. This article has 88 citations.

22. (jamil2025emergingantimicrobialresistance pages 9-11): Iqra Jamil, Dr Asad Ur Rehman, Dr Fayyaz Ur Rehman, and Dr Farhan Rasheed. Emerging antimicrobial resistance in typhoid fever: challenges in diagnosis and treatment. Journal of Medical &amp; Health Sciences Review, Jun 2025. URL: https://doi.org/10.62019/a1v2gq57, doi:10.62019/a1v2gq57. This article has 2 citations.

23. (sam2024diagnosticperformanceof pages 2-4): Emmanuel Kweku Sam, Johnson Alagbo, Avis Asamoah, Felix Ansah, Kwesi Zandoh Tandoh, Lucas N. Amenga-Etego, and Samuel Duodu. Diagnostic performance of typhidot rdt in diagnosis of typhoid fever and antibiotic resistance characterisation in a cross-sectional study in southern ghana. BMC Infectious Diseases, Nov 2024. URL: https://doi.org/10.1186/s12879-024-10160-2, doi:10.1186/s12879-024-10160-2. This article has 6 citations and is from a peer-reviewed journal.

24. (jamil2025emergingantimicrobialresistance pages 5-7): Iqra Jamil, Dr Asad Ur Rehman, Dr Fayyaz Ur Rehman, and Dr Farhan Rasheed. Emerging antimicrobial resistance in typhoid fever: challenges in diagnosis and treatment. Journal of Medical &amp; Health Sciences Review, Jun 2025. URL: https://doi.org/10.62019/a1v2gq57, doi:10.62019/a1v2gq57. This article has 2 citations.

25. (lo2025currentantimicrobialsusceptibility pages 1-2): Calvin Ka-Fung Lo, Merisa Mok, Cole Schonhofer, Kevin Afra, and Shazia Masud. Current antimicrobial susceptibility trends and clinical outcomes of typhoidal salmonella in a large health authority in british columbia, canada. Tropical Medicine and Infectious Disease, Apr 2025. URL: https://doi.org/10.3390/tropicalmed10040108, doi:10.3390/tropicalmed10040108. This article has 1 citations.

26. (jamil2025emergingantimicrobialresistance pages 7-9): Iqra Jamil, Dr Asad Ur Rehman, Dr Fayyaz Ur Rehman, and Dr Farhan Rasheed. Emerging antimicrobial resistance in typhoid fever: challenges in diagnosis and treatment. Journal of Medical &amp; Health Sciences Review, Jun 2025. URL: https://doi.org/10.62019/a1v2gq57, doi:10.62019/a1v2gq57. This article has 2 citations.

27. (bansal2024geneticengineeringof pages 3-4): Garima Bansal, Mostafa Ghanem, Khandra T. Sears, James E. Galen, and Sharon M. Tennant. Genetic engineering of <i>salmonella</i> spp. for novel vaccine strategies and therapeutics. EcoSal Plus, Dec 2024. URL: https://doi.org/10.1128/ecosalplus.esp-0004-2023, doi:10.1128/ecosalplus.esp-0004-2023. This article has 11 citations.

28. (lo2025currentantimicrobialsusceptibility pages 2-4): Calvin Ka-Fung Lo, Merisa Mok, Cole Schonhofer, Kevin Afra, and Shazia Masud. Current antimicrobial susceptibility trends and clinical outcomes of typhoidal salmonella in a large health authority in british columbia, canada. Tropical Medicine and Infectious Disease, Apr 2025. URL: https://doi.org/10.3390/tropicalmed10040108, doi:10.3390/tropicalmed10040108. This article has 1 citations.

29. (zizza2024foodborneinfectionsand pages 6-8): Antonella Zizza, Alessandra Fallucca, Marcello Guido, Vincenzo Restivo, Marco Roveta, and Cecilia Trucchi. Foodborne infections and salmonella: current primary prevention tools and future perspectives. Vaccines, 13:29, Dec 2024. URL: https://doi.org/10.3390/vaccines13010029, doi:10.3390/vaccines13010029. This article has 30 citations.

30. (lo2025currentantimicrobialsusceptibility pages 7-8): Calvin Ka-Fung Lo, Merisa Mok, Cole Schonhofer, Kevin Afra, and Shazia Masud. Current antimicrobial susceptibility trends and clinical outcomes of typhoidal salmonella in a large health authority in british columbia, canada. Tropical Medicine and Infectious Disease, Apr 2025. URL: https://doi.org/10.3390/tropicalmed10040108, doi:10.3390/tropicalmed10040108. This article has 1 citations.

31. (lo2025currentantimicrobialsusceptibility pages 5-7): Calvin Ka-Fung Lo, Merisa Mok, Cole Schonhofer, Kevin Afra, and Shazia Masud. Current antimicrobial susceptibility trends and clinical outcomes of typhoidal salmonella in a large health authority in british columbia, canada. Tropical Medicine and Infectious Disease, Apr 2025. URL: https://doi.org/10.3390/tropicalmed10040108, doi:10.3390/tropicalmed10040108. This article has 1 citations.

32. (ranjan2026salmonellainfectionsglobal pages 19-20): Adishi Ranjan, Mahek Chandna, Nicole J. Stevens, Jana Kandil, Brianna Dinh, Macy Kuhn, Noor Mian, Bach Tran, Abdullah Hamid, Peter Kim, and Taseen S. Desin. Salmonella infections: global trends and emerging challenges. Microorganisms, 14:816, Apr 2026. URL: https://doi.org/10.3390/microorganisms14040816, doi:10.3390/microorganisms14040816. This article has 0 citations.

33. (chakraborty2024typhoid&paratyphoid pages 6-7): Suparna Chakraborty and Santasabuj Das. Typhoid & paratyphoid vaccine development in the laboratory: a review & in-country experience. The Indian Journal of Medical Research, 160:379-390, Nov 2024. URL: https://doi.org/10.25259/ijmr\_1382\_2024, doi:10.25259/ijmr\_1382\_2024. This article has 3 citations.

34. (alfini2024designofa media c76829e9): Renzo Alfini, Martina Carducci, Luisa Massai, Daniele De Simone, Marco Mariti, Omar Rossi, Simona Rondini, Francesca Micoli, and Carlo Giannelli. Design of a glycoconjugate vaccine against salmonella paratyphi a. Vaccines, 12:1272, Nov 2024. URL: https://doi.org/10.3390/vaccines12111272, doi:10.3390/vaccines12111272. This article has 10 citations.

35. (alfini2024designofa media 5fca7cec): Renzo Alfini, Martina Carducci, Luisa Massai, Daniele De Simone, Marco Mariti, Omar Rossi, Simona Rondini, Francesca Micoli, and Carlo Giannelli. Design of a glycoconjugate vaccine against salmonella paratyphi a. Vaccines, 12:1272, Nov 2024. URL: https://doi.org/10.3390/vaccines12111272, doi:10.3390/vaccines12111272. This article has 10 citations.

36. (alfini2024designofa media 6729a2bb): Renzo Alfini, Martina Carducci, Luisa Massai, Daniele De Simone, Marco Mariti, Omar Rossi, Simona Rondini, Francesca Micoli, and Carlo Giannelli. Design of a glycoconjugate vaccine against salmonella paratyphi a. Vaccines, 12:1272, Nov 2024. URL: https://doi.org/10.3390/vaccines12111272, doi:10.3390/vaccines12111272. This article has 10 citations.