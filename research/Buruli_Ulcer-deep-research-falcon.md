---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:26:36.763826'
end_time: '2026-04-04T12:39:50.242331'
duration_seconds: 793.48
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Buruli ulcer
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 54
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Buruli ulcer
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Buruli ulcer** covering all of the
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
- **Disease Name:** Buruli ulcer
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Buruli ulcer** covering all of the
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


# Buruli Ulcer (Mycobacterium ulcerans disease): Disease Characteristics Research Report

## 1. Disease information

### 1.1 Concise overview (current understanding)
Buruli ulcer (BU) is a necrotizing infection of skin and subcutaneous tissue caused by *Mycobacterium ulcerans*, typically beginning as a painless pre-ulcerative lesion (papule, nodule, plaque, or oedema) that can progress to a necrotic ulcer with undermined edges and substantial tissue loss, scarring, and disability if untreated or treated late (akolgo2024exploringmycolactone—theunique pages 1-3, muhi2023ahumanmodel pages 1-2, anthony2024buruliulcertransmission pages 1-2). BU is categorized by WHO as a neglected tropical disease and is geographically focal, with highest burden in West/Central Africa and important endemic foci in Australia (akolgo2024exploringmycolactone—theunique pages 3-4, muhi2023ahumanmodel pages 1-2).

### 1.2 Key identifiers and classifications
Evidence retrieved in-session supports the following identifiers/classifications:
- **MeSH (condition/descriptor ID):** D054312 “Buruli Ulcer” (ClinicalTrials.gov record) (NCT00321178 chunk 2).
- **WHO clinical lesion categories (severity by size/complexity):** Category I (<5 cm), Category II (5–15 cm), Category III (>15 cm and/or critical sites/complex disease) (anthony2024buruliulcertransmission pages 1-2, obrien2024anoverviewof pages 1-2).

**Not located in retrieved sources:** ICD-10/ICD-11 codes, Orphanet (ORPHA) identifier, and MONDO ID were not present in the retrieved full-text excerpts and therefore cannot be populated from the present evidence set.

### 1.3 Synonyms and alternative names
Synonyms/alternative names include **Mycobacterium ulcerans disease** and historical regional names **Bairnsdale ulcer**, **Searls ulcer**, and **Daintree ulcer** (NCT00321178 chunk 2, akolgo2024exploringmycolactone—theunique pages 3-4).

### 1.4 Evidence source types (individual vs aggregated)
- **Aggregated resources:** Surveillance-style epidemiology and burden estimates are reported as aggregated counts (e.g., WHO notifications) (akolgo2024exploringmycolactone—theunique pages 3-4).
- **Individual-level resources:** ClinicalTrials.gov protocol/records contain participant-level eligibility/outcome structures and MeSH tagging for BU (NCT00321178 chunk 2, NCT01659437 chunk 1).

A compact identifiers/synonyms summary is provided here:

| Item | Value | Source | URL / publication date |
|---|---|---|---|
| Disease name | Buruli ulcer (BU) (akolgo2024exploringmycolactone—theunique pages 1-3, muhi2023ahumanmodel pages 1-2) | Akolgo et al., *Exploring Mycolactone—The Unique Causative Toxin of Buruli Ulcer*; Muhi et al., *A human model of Buruli ulcer* | https://doi.org/10.3390/toxins16120528 (Dec 2024); https://doi.org/10.1371/journal.pntd.0011394 (Jun 2023) |
| Synonyms / alternative names | Mycobacterium ulcerans disease; Bairnsdale ulcer; Searls ulcer; Daintree ulcer (NCT00321178 chunk 2, akolgo2024exploringmycolactone—theunique pages 3-4) | ClinicalTrials.gov BURULICO protocol; Akolgo et al. | NCT00321178 / ClinicalTrials.gov (2006); https://doi.org/10.3390/toxins16120528 (Dec 2024) |
| Causative agent | *Mycobacterium ulcerans* (environmental nontuberculous mycobacterium) (akolgo2024exploringmycolactone—theunique pages 1-3, anthony2024buruliulcertransmission pages 1-2) | Akolgo et al.; Anthony et al., *Buruli ulcer transmission: environmental pathways and implications for dermatologic care* | https://doi.org/10.3390/toxins16120528 (Dec 2024); https://doi.org/10.12788/cutis.1145 (Dec 2024) |
| MeSH condition ID | D054312 (“Buruli Ulcer”) (NCT00321178 chunk 2) | ClinicalTrials.gov BURULICO protocol | NCT00321178 / ClinicalTrials.gov (2006) |
| WHO lesion category I | Lesion diameter <5 cm (anthony2024buruliulcertransmission pages 1-2, obrien2024anoverviewof pages 1-2) | Anthony et al.; O'Brien et al., *An overview of Buruli ulcer in Australia* | https://doi.org/10.12788/cutis.1145 (Dec 2024); https://doi.org/10.31128/ajgp-08-23-6914 (Sep 2024) |
| WHO lesion category II | Lesion diameter 5–15 cm (anthony2024buruliulcertransmission pages 1-2, obrien2024anoverviewof pages 1-2) | Anthony et al.; O'Brien et al. | https://doi.org/10.12788/cutis.1145 (Dec 2024); https://doi.org/10.31128/ajgp-08-23-6914 (Sep 2024) |
| WHO lesion category III | Lesion diameter >15 cm and/or lesions at critical sites or involving bone/joint/other clinically complex disease (anthony2024buruliulcertransmission pages 1-2, obrien2024anoverviewof pages 1-2) | Anthony et al.; O'Brien et al. | https://doi.org/10.12788/cutis.1145 (Dec 2024); https://doi.org/10.31128/ajgp-08-23-6914 (Sep 2024) |
| WHO reported new cases in 2023 | 1,952 total new cases from 12 countries; 1,573 in the African Region; 379 in the Western Pacific Region (akolgo2024exploringmycolactone—theunique pages 3-4) | Akolgo et al. | https://doi.org/10.3390/toxins16120528 (Dec 2024) |


*Table: This table compiles high-yield identifiers, synonyms, classification details, and recent WHO surveillance figures for Buruli ulcer using only evidence retrieved in the session. It is useful as a compact reference for nomenclature and disease-level knowledge base fields.*

## 2. Etiology

### 2.1 Primary causal factor
BU is caused by infection with the environmental, nontuberculous mycobacterium **Mycobacterium ulcerans** (akolgo2024exploringmycolactone—theunique pages 1-3, anthony2024buruliulcertransmission pages 1-2).

### 2.2 Key virulence determinant
A central driver of BU pathology is the **diffusible macrolide toxin mycolactone**, encoded on plasmid pMUM001 (anthony2024buruliulcertransmission pages 1-2, akolgo2024exploringmycolactone—theunique pages 1-3).

### 2.3 Risk factors (recent evidence)
BU acquisition is strongly associated with **water-rich environments** (e.g., swamps, ponds, marshes) and water-contact activities; transmission pathways appear to vary by geography and remain incompletely defined (anthony2024buruliulcertransmission pages 1-2, akolgo2024exploringmycolactone—theunique pages 4-6).

Quantified modifiable risk factors were identified in a recent matched case-control study in Ghana:
- **Farming without adequate protective clothing:** aOR 3.02 (gohoho2025riskfactorsfor pages 13-15)
- **Living near waterbodies:** aOR 4.45 (gohoho2025riskfactorsfor pages 13-15)

A separate case-control study in Benin (2025) also highlighted elevated odds for specific water-exposure behaviors (e.g., bathing; frequenting irrigation canals) with odds ratios in the ~3–5 range depending on subgroup/territory (johnson2025territorialandgenderlinked pages 9-12).

### 2.4 Protective factors
In the Ghana matched case-control study, the following were associated with reduced odds:
- **Applying alcohol to injuries:** aOR 0.17 (gohoho2025riskfactorsfor pages 13-15)
- **Being married:** aOR 0.32 (gohoho2025riskfactorsfor pages 13-15)

### 2.5 Gene–environment interactions
No robust human genetic susceptibility loci or gene–environment interaction datasets were retrieved in-session. Current evidence emphasizes an environmental reservoir with toxin-mediated pathogenesis rather than a defined Mendelian genetic architecture (muhi2023ahumanmodel pages 1-2, akolgo2024exploringmycolactone—theunique pages 4-6).

## 3. Phenotypes

### 3.1 Clinical phenotype spectrum
Early BU can present as **papule, nodule, plaque, or oedematous lesions**, with eventual ulceration characterized by a **necrotic base** and **undermined edges** (obrien2024anoverviewof pages 1-2, anthony2024buruliulcertransmission pages 1-2, muhi2023ahumanmodel pages 1-2). In Australia, oedematous BU was reported to account for ~**8%** of cases and is described as the most rapidly progressive/destructive form; multiple lesions occur in ~**5%** of cases (obrien2024anoverviewof pages 1-2).

BU lesions are **painless in most cases**, consistent with mycolactone-mediated hypoesthesia/analgesia; pain and fever may suggest secondary bacterial infection (obrien2024anoverviewof pages 1-2, anthony2024buruliulcertransmission pages 1-2).

Severe disease can extend to deeper structures including **bone (osteomyelitis)**, and complications include **scarring**, **joint contractures**, **deformity**, and **functional impairment** (obrien2024anoverviewof pages 1-2, anthony2024buruliulcertransmission pages 1-2, muhi2023ahumanmodel pages 1-2).

A clinical image panel of classic forms (nodule, plaque, oedema, small ulcer) is available from a 2024 review:

- Clinical forms figure (nodule/plaque/oedema/ulcer) (akolgo2024exploringmycolactone—theunique media 536a767e).

### 3.2 Onset and progression (temporal development)
Incubation can be prolonged (reported average **4–5 months** in Victoria, Australia) with slow progression from pre-ulcerative lesions to ulceration (muhi2023ahumanmodel pages 1-2). Progression from nodule to ulcer has been described as ranging from weeks to months (anthony2024buruliulcertransmission pages 1-2).

### 3.3 WHO lesion category framework (staging proxy)
WHO categories are used clinically to stratify severity by lesion size and complexity: category I (<5 cm), II (5–15 cm), III (>15 cm and/or critical sites/complex disease) (anthony2024buruliulcertransmission pages 1-2, obrien2024anoverviewof pages 1-2).

### 3.4 Quality-of-life and disability impact
BU can cause cosmetic deformity, functional impairment, psychological impact, and substantial economic burden, especially when diagnosis/treatment is delayed or when lesions are large/complex (obrien2024anoverviewof pages 1-2, boakyeappiah2023currentprogressand pages 1-5).

### 3.5 Suggested HPO mappings (examples)
Suggested HPO term mappings consistent with the retrieved clinical descriptions:
- Papule; Nodule; Plaque; Localized edema (oedema form) (obrien2024anoverviewof pages 1-2, anthony2024buruliulcertransmission pages 1-2)
- Skin ulcer; Skin necrosis; Undermined ulcer edge (obrien2024anoverviewof pages 1-2, anthony2024buruliulcertransmission pages 1-2)
- Hypoesthesia / decreased pain sensation (painless lesion) (anthony2024buruliulcertransmission pages 1-2)
- Fever (secondary infection context) (obrien2024anoverviewof pages 1-2)
- Osteomyelitis (obrien2024anoverviewof pages 1-2, anthony2024buruliulcertransmission pages 1-2)
- Joint contracture / decreased range of motion; Impaired mobility (muhi2023ahumanmodel pages 1-2)
- Abnormal scarring / disfigurement (akolgo2024exploringmycolactone—theunique pages 1-3, muhi2023ahumanmodel pages 1-2)

## 4. Genetic / molecular information

### 4.1 Human causal genes and pathogenic variants
BU is an infectious disease; no human causal genes/variants were identified in the retrieved evidence.

### 4.2 Pathogen determinants (molecular genetics)
A key pathogen genetic determinant is the plasmid-encoded mycolactone biosynthetic machinery (pMUM001) (anthony2024buruliulcertransmission pages 1-2).

### 4.3 Epigenetics / chromosomal abnormalities
No relevant host epigenetic or chromosomal abnormality evidence was retrieved in-session.

## 5. Environmental information

### 5.1 Environmental reservoirs and exposures
Multiple sources emphasize BU’s association with aquatic and swampy environments and possible involvement of aquatic organisms and insects in ecology/transmission (anthony2024buruliulcertransmission pages 1-2, oseiowusu2023buruliulcerin pages 5-7). *M. ulcerans* DNA has been detected in fish, water insects, and snails; aquatic insects and mosquitoes have been studied as possible vectors (anthony2024buruliulcertransmission pages 1-2).

### 5.2 Lifestyle/behavioral contributors (recent quantified evidence)
Farming without protective clothing and proximity to water bodies are associated with increased odds, while injury cleansing with alcohol is associated with reduced odds (gohoho2025riskfactorsfor pages 13-15).

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (trigger → mechanism → phenotype)
**Environmental exposure and inoculation** (likely through skin breaches in aquatic-associated settings) is followed by local infection with *M. ulcerans* (anthony2024buruliulcertransmission pages 1-2, akolgo2024exploringmycolactone—theunique pages 4-6). Disease progression is driven by **mycolactone**, which mediates:
- **Cytotoxic tissue necrosis** → necrotic ulcers and undermined edges (akolgo2024exploringmycolactone—theunique pages 1-3, anthony2024buruliulcertransmission pages 1-2)
- **Immune suppression** → reduced inflammatory signs and impaired local control (muhi2023ahumanmodel pages 1-2, akolgo2024exploringmycolactone—theunique pages 4-6)
- **Analgesia/hypoesthesia** → typically painless lesions despite extensive tissue damage (anthony2024buruliulcertransmission pages 1-2)

### 6.2 Molecular targets and pathways (current consensus and proposed mechanisms)
A major mechanism is mycolactone binding and inhibition of the **Sec61 translocon**, blocking protein translocation into the endoplasmic reticulum and suppressing cytokine production including IL-2 and IFN-γ (muhi2023ahumanmodel pages 1-2, muhi2023ahumanmodel pages 12-13). Additional proposed targets/mechanisms include WASP/N-WASP inhibition, angiotensin II type 2 receptor (AT2R) signaling in analgesia, and mTOR inhibition (akolgo2024exploringmycolactone—theunique pages 1-3, anthony2024buruliulcertransmission pages 1-2).

### 6.3 Cell types involved (CL suggestions)
Mycolactone affects multiple mammalian cell types including macrophages, fibroblasts, keratinocytes, dendritic cells, and T cells (akolgo2024exploringmycolactone—theunique pages 4-6). Suggested Cell Ontology (CL) mappings include macrophage; fibroblast; keratinocyte; dendritic cell; T cell.

### 6.4 Suggested GO Biological Process terms (examples)
Based on described mechanisms:
- Immune effector process / cytokine production
- Protein targeting to ER / protein translocation
- Apoptotic process
- Inflammatory response regulation

### 6.5 Omics profiling
No transcriptomic/proteomic/metabolomic profiling datasets were retrieved in-session.

## 7. Anatomical structures affected

### 7.1 Organ/tissue level
Primary involvement is **skin and subcutaneous tissue**, often on distal limbs around joints; severe disease can involve **bone** (osteomyelitis) and joints (obrien2024anoverviewof pages 1-2, anthony2024buruliulcertransmission pages 1-2). Suggested UBERON mappings: skin; subcutaneous adipose tissue; lower limb; upper limb; bone tissue.

### 7.2 Subcellular localization (mechanistic)
The Sec61 target localizes to the endoplasmic reticulum membrane, consistent with an ER protein translocation blockade mechanism (muhi2023ahumanmodel pages 1-2).

## 8. Temporal development

- **Onset pattern:** insidious/subacute with long incubation reported in Australian setting (average 4–5 months) (muhi2023ahumanmodel pages 1-2).
- **Course:** progressive local necrosis and ulceration if untreated, with potential spontaneous healing in some cases but risk of contractures/disability (muhi2023ahumanmodel pages 1-2).

## 9. Inheritance and population

### 9.1 Epidemiology and distribution (recent statistics prioritized)
WHO-reported notifications for 2023 were **1,952 new cases from 12 countries**, with **1,573** in the African Region and **379** in the Western Pacific Region (akolgo2024exploringmycolactone—theunique pages 3-4). Burden remains concentrated in West/Central Africa, with notable endemicity in Ghana, Benin, Côte d’Ivoire, and DRC (akolgo2024exploringmycolactone—theunique pages 3-4). Australia has an important endemic focus with older median age at diagnosis (**66 years**) and increasing recognition/spread to new areas (obrien2024anoverviewof pages 1-2).

Historical global estimates cited in a 2023 review were about **5,000–6,000 cases/year** during 2004–2010 (muhi2023ahumanmodel pages 1-2).

### 9.2 Demographics
BU affects all ages, but age patterns differ by geography (children often affected in Africa; adults more frequently in Australia) (akolgo2024exploringmycolactone—theunique pages 1-3, obrien2024anoverviewof pages 1-2).

## 10. Diagnostics

### 10.1 Current diagnostic workflow (routine practice)
PCR is emphasized as the preferred confirmatory test. In Australia-specific guidance, PCR on an ulcer swab is considered the diagnostic test of choice, while tissue biopsy is recommended when disease is non-ulcerated because swabs from non-ulcerative lesions can be falsely negative (obrien2024anoverviewof pages 1-2).

An Australian consensus statement further specifies **IS2404-targeted PCR** on ulcer swabs as the primary confirmatory test, provides swab/biopsy technique guidance, and notes culture can take up to **12 weeks** and is less sensitive than PCR (muhi2025managementofmycobacterium pages 2-3).

A structured diagnostics summary is provided here:

| Diagnostic modality | Typical specimen type(s) | What it detects / target | Practical notes | Quantitative / performance details | Source URL / date |
|---|---|---|---|---|---|
| Real-time PCR (preferred confirmatory test) | Ulcer swab; tissue biopsy for non-ulcerative lesions | *M. ulcerans* DNA; IS2404 is the primary confirmatory target in recent guidance | Diagnostic test of choice because of speed and accuracy; specifically request *M. ulcerans* PCR. Swabs from non-ulcerative lesions have a high false-negative rate, so biopsy is recommended for early/pre-ulcerative or PCR-negative suspicious lesions. Optimal ulcer swab technique is around the undermined edge with visible material; saline may improve yield. (obrien2024anoverviewof pages 1-2, muhi2025managementofmycobacterium pages 2-3, anthony2024buruliulcertransmission pages 1-2) | WHO reports about 70% of notified cases are PCR-confirmed. False negatives are particularly noted in early/pre-ulcerative lesions and in children. (muhi2025managementofmycobacterium pages 2-3, anthony2024buruliulcertransmission pages 1-2) | https://doi.org/10.31128/ajgp-08-23-6914 (Sep 2024); https://doi.org/10.5694/mja2.52591 (Feb 2025); https://doi.org/10.12788/cutis.1145 (Dec 2024) |
| Ulcer swab PCR workflow | Ulcer swab | Same as above | Best for open ulcers; easy, rapid, field-practical. For ulcers, swab the undermined edge rather than superficial debris. (obrien2024anoverviewof pages 1-2, muhi2025managementofmycobacterium pages 2-3) | No sensitivity value provided in retrieved texts, but repeatedly described as primary/most accurate routine confirmatory approach for ulcers. (obrien2024anoverviewof pages 1-2, muhi2025managementofmycobacterium pages 2-3) | https://doi.org/10.31128/ajgp-08-23-6914 (Sep 2024); https://doi.org/10.5694/mja2.52591 (Feb 2025) |
| Biopsy PCR | Punch or skin biopsy from center of non-ulcerated lesions or ulcer margin | *M. ulcerans* DNA; IS2404-targeted PCR in recent consensus guidance | Recommended when lesions are non-ulcerative, early, or when swab PCR is negative but suspicion remains. Fresh tissue should not be placed in preservative; transport in saline-moistened gauze/drops of saline to avoid dehydration. (muhi2025managementofmycobacterium pages 2-3, lim2025mycobacteriumulceransulcer pages 7-9) | No formal sensitivity value provided in retrieved texts; emphasized as necessary to reduce false negatives in pre-ulcerative disease. (muhi2025managementofmycobacterium pages 2-3, lim2025mycobacteriumulceransulcer pages 7-9) | https://doi.org/10.5694/mja2.52591 (Feb 2025); https://doi.org/10.3390/life15071096 (Jul 2025) |
| Fine-needle aspirate (FNA) / punch biopsy qPCR | FNA or 3 mm punch biopsy | IS2404 and KR qPCR used in reported series | Useful in non-ulcerative disease and in some research/diagnostic series. (combe2020areallburuli pages 4-6, lim2025mycobacteriumulceransulcer pages 19-20) | Example qPCR-positive lesion: IS2404 Ct ~23.64, KR Ct ~25 with culture positivity; high Ct values (~41 and ~38.87) associated with culture negativity and absence of *M. ulcerans* by metabarcoding. (combe2020areallburuli pages 4-6) | https://doi.org/10.1111/bjd.19260 (Jul 2020); https://doi.org/10.3390/life15071096 (Jul 2025) |
| Microscopy / acid-fast smear | Swab smear; tissue material | Acid-fast bacilli (Ziehl-Neelsen / BAAR) | Available and historically used, but less emphasized than PCR in current practice. (combe2020areallburuli pages 4-6, anthony2024buruliulcertransmission pages 1-2) | No sensitivity/specificity values provided in retrieved texts. (combe2020areallburuli pages 4-6, anthony2024buruliulcertransmission pages 1-2) | https://doi.org/10.1111/bjd.19260 (Jul 2020); https://doi.org/10.12788/cutis.1145 (Dec 2024) |
| Mycobacterial culture | Swab- or biopsy-derived material; Lowenstein-Jensen medium commonly cited | Viable *M. ulcerans* growth | Definitive but slow and less sensitive than PCR; useful for confirmation and research/isolate recovery. (obrien2024anoverviewof pages 1-2, muhi2025managementofmycobacterium pages 2-3, combe2020areallburuli pages 4-6) | Results may take up to 12 weeks in recent consensus guidance; one report incubated cultures up to 9 months at 30°C. (muhi2025managementofmycobacterium pages 2-3, combe2020areallburuli pages 4-6) | https://doi.org/10.31128/ajgp-08-23-6914 (Sep 2024); https://doi.org/10.5694/mja2.52591 (Feb 2025); https://doi.org/10.1111/bjd.19260 (Jul 2020) |
| Histopathology | Tissue biopsy | Tissue changes of BU: necrosis/chronic inflammation; granuloma formation may be seen | Supports diagnosis and helps exclude alternatives, especially when PCR is negative or lesion is atypical. (muhi2025managementofmycobacterium pages 2-3, siirin2024towardsaburuli pages 1-5) | No sensitivity values provided; consensus notes granuloma formation is seen more often in ulcers than in pre-ulcerative lesions. (muhi2025managementofmycobacterium pages 2-3) | https://doi.org/10.5694/mja2.52591 (Feb 2025); https://doi.org/10.1101/2024.01.23.24301643 (Jan 2024 preprint) |
| Mass spectrometry for mycolactone | Tissue extracts / lesion-derived material | Mycolactone biomarker | Attractive because mycolactone is unique to *M. ulcerans*, but cost and instrumentation limit point-of-care use in endemic settings. (akolgo2024exploringmycolactone—theunique pages 18-20) | Detects mycolactone with observed [M+Na]+ at m/z 765.6. (akolgo2024exploringmycolactone—theunique pages 18-20) | https://doi.org/10.3390/toxins16120528 (Dec 2024) |
| Anti-mycolactone monoclonal antibody ELISA | Lesion-associated material / research assay formats | Mycolactone via competitive immunoassay | Demonstrates feasibility of toxin detection; translation to simple field LFA is technically difficult because mycolactone is light-sensitive, amphiphilic, aggregates, and binds serum proteins. (akolgo2024exploringmycolactone—theunique pages 18-20) | Competitive ELISAs reached low-nanogram sensitivity. (akolgo2024exploringmycolactone—theunique pages 18-20) | https://doi.org/10.3390/toxins16120528 (Dec 2024) |
| Mycolactone lateral flow immunoassay (early/prototype reports) | Lesion material | Mycolactone | Conceptually promising for point-of-care use, but older prototype LFIA evidence was very limited. (akolgo2024exploringmycolactone—theunique pages 18-20) | Review notes only a single case-report prototype in earlier literature. (akolgo2024exploringmycolactone—theunique pages 18-20) | https://doi.org/10.3390/toxins16120528 (Dec 2024) |
| Aptamer-based mycolactone assay | Swab-based samples in pilot study | Mycolactone-binding nucleic acid aptamers | Experimental and not yet adequate as a stand-alone clinical test. (akolgo2024exploringmycolactone—theunique pages 18-20) | Pilot case-control study on swabs (n=41 suspected BU patients) showed 50% sensitivity. (akolgo2024exploringmycolactone—theunique pages 18-20) | https://doi.org/10.3390/toxins16120528 (Dec 2024) |
| Prototype rapid mycolactone lateral flow test with immunomagnetic concentration | Swab-collected wound exudate from open lesions | Mycolactone using anti-mycolactone monoclonal antibody + magnetic gold nanoshells | Designed as a low-infrastructure rapid test; requires only a magnetic rack and no powered instrumentation. Procedure can be completed in about 2 hours. Particularly aimed at point-of-care use from wound swabs. (siirin2024towardsaburuli pages 1-5) | Detection limit 3.5-7 ng of mycolactone collected on a swab. (siirin2024towardsaburuli pages 1-5) | https://doi.org/10.1101/2024.01.23.24301643 (Jan 2024 preprint) |
| Other emerging assays | Variable | LAMP, antigen detection, mycolactone TLC-based methods | LAMP is highlighted as a promising point-of-care nucleic-acid alternative; antigen detection and TLC-based mycolactone assays remain under development. (anthony2024buruliulcertransmission pages 1-2, siirin2024towardsaburuli pages 1-5) | No robust field performance metrics provided in retrieved texts. (anthony2024buruliulcertransmission pages 1-2, siirin2024towardsaburuli pages 1-5) | https://doi.org/10.12788/cutis.1145 (Dec 2024); https://doi.org/10.1101/2024.01.23.24301643 (Jan 2024 preprint) |


*Table: This table summarizes routine and emerging diagnostic approaches for Buruli ulcer, including specimen selection, confirmatory PCR practices, conventional pathology/microbiology, and new mycolactone-based assays. It is useful for quickly comparing test targets, practical limitations, and the most clinically relevant workflow notes.*

### 10.2 Emerging diagnostics (2023–2024)
Mycolactone is increasingly positioned as a biomarker for point-of-care diagnostics; a 2024 prototype rapid test uses immunomagnetic concentration plus lateral flow detection and can detect **3.5–7 ng** of mycolactone on a swab in ~**2 hours** without powered instrumentation (siirin2024towardsaburuli pages 1-5).

## 11. Outcome / prognosis

With effective antibiotic therapy, BU cure rates are high; a recent review reports cure rates **exceeding 90% in patients completing therapy** (lim2025mycobacteriumulceransulcer pages 4-6). Delayed diagnosis/treatment is associated with higher risk of extensive necrosis, scarring, contractures, deformity, and long-term disability (muhi2023ahumanmodel pages 1-2, obrien2024anoverviewof pages 1-2).

## 12. Treatment

### 12.1 Standard-of-care antimicrobial therapy
WHO-preferred treatment is an **8-week all-oral regimen** of **rifampicin plus clarithromycin** combined with wound care, with dosing summarized in recent reviews (rifampicin 10 mg/kg daily; clarithromycin 7.5 mg/kg twice daily) (lim2025mycobacteriumulceransulcer pages 2-4, saezlopez2024amoxicillinclavulanateincombination pages 1-2).

### 12.2 Clinical trials and emerging regimens (2023–2024 prioritized)
- **Treatment shortening via beta-lactam add-on:** In vitro evidence supports rifampicin/clarithromycin plus amoxicillin-clavulanate combinations being bactericidal and more effective than rifampicin/clarithromycin alone, supporting an ongoing Phase II trial **NCT05169554** testing 4-week therapy vs standard 8 weeks (saezlopez2024amoxicillinclavulanateincombination pages 1-2, NCT05169554 chunk 1).
- **Dose optimization/high-dose rifampicin:** A 2023 Phase 3 trial protocol in Ghana evaluates high-dose vs standard-dose rifampicin combined with **DACC dressings**, with primary endpoint mean time to clearance of viable mycobacteria (PACTR202011867644311) (amoako2023burulirifdaccevaluationof pages 1-3).
- **Next-generation antibiotics:** Telacebec (Q203) shows strong preclinical promise and is in a Phase 2 recruiting study (**NCT06481163**) (lim2025mycobacteriumulceransulcer pages 6-7).

A structured treatment and trials summary is provided here:

| Treatment / implementation | Regimen or intervention | Real-world use / status | Key evidence / outcomes | Trial ID / endpoint | URL / publication date |
|---|---|---|---|---|---|
| Standard first-line all-oral therapy | Rifampicin 10 mg/kg once daily (max 600 mg) + clarithromycin 7.5 mg/kg twice daily (max 500 mg BID) for 8 weeks | Current WHO-preferred regimen; widely used in endemic settings and Australia; often combined with wound dressings and selective surgery | Oral RC8 largely replaced streptomycin-containing regimens because of non-inferior healing and less injection toxicity; cure rates exceed 90% in patients completing therapy; shorter 6-week courses may be considered for small lesions in selected settings (lim2025mycobacteriumulceransulcer pages 2-4, lim2025mycobacteriumulceransulcer pages 6-7, lim2025mycobacteriumulceransulcer pages 4-6) | Historical phase II/III non-inferiority evidence vs SR8; endpoint: healing without recurrence and without excision surgery at 12 months (NCT01659437 chunk 1) | https://doi.org/10.3390/life15071096 (Jul 2025); https://clinicaltrials.gov/study/NCT01659437 (2012) |
| Historical injectable regimen | Rifampicin 10 mg/kg oral daily + streptomycin 15 mg/kg IM daily for 8 weeks | Former standard since 2004; now largely replaced where all-oral therapy is available | Effective but limited by injection logistics and streptomycin-associated ototoxicity; used as comparator in WHO-sponsored trial (lim2025mycobacteriumulceransulcer pages 2-4, NCT01659437 chunk 1) | NCT01659437; primary endpoint: healing without recurrence and without excision surgery at 12 months (NCT01659437 chunk 1) | https://clinicaltrials.gov/study/NCT01659437 (2012); https://doi.org/10.3390/life15071096 (Jul 2025) |
| Adjunct wound care and selective surgery | Standard wound cleaning, moist dressings, possible grafting/debridement; surgery for extensive, function-threatening, or reconstructive indications | Real-world routine supportive care across endemic programs and Australian practice | Wound care remains integral to management; surgery is now adjunctive rather than primary therapy, but still important for large lesions, tissue loss, or function-preserving reconstruction (lim2025mycobacteriumulceransulcer pages 4-6, saezlopez2024amoxicillinclavulanateincombination pages 1-2) | NCT05169554 defines cure as lesion healing without recurrence and without excision surgery at 12 months (NCT05169554 chunk 1) | https://doi.org/10.3390/life15071096 (Jul 2025); https://clinicaltrials.gov/study/NCT05169554 (2021) |
| Pharmacokinetic consideration | Rifampicin + clarithromycin, including clarithromycin extended-release evaluation | Important for dose optimization in clinical practice and trials | Rifampicin induces CYP3A4 and lowers clarithromycin exposure; extended-release clarithromycin did not clearly improve PK advantage; higher failure risk has been noted in heavier patients, supporting ongoing dose-optimization work (klis2024pharmacokineticsofextendedrelease pages 5-6, lim2025mycobacteriumulceransulcer pages 4-6) | NCT01659437 PK substudy; endpoints included Cmax, AUC0-24, t1/2, CL/F, V/F (klis2024pharmacokineticsofextendedrelease pages 5-6) | https://doi.org/10.1038/s41598-024-70890-w (Aug 2024); https://doi.org/10.3390/life15071096 (Jul 2025) |
| Beta-lactam add-on to shorten therapy | Rifampicin + clarithromycin + amoxicillin/clavulanate; investigational 4-week regimen vs standard 8-week RC8 | Active multicenter phase II trial in West Africa | In vitro time-kill assays showed RIF+AMX/CLV and RIF+CLA+AMX/CLV were bactericidal and more effective than RIF+CLA alone, supporting treatment-shortening strategy (saezlopez2024amoxicillinclavulanateincombination pages 1-2) | NCT05169554; endpoint: cure (healing without recurrence and without excision surgery) at 12 months; PK and bacterial clearance substudies included (NCT05169554 chunk 1) | https://doi.org/10.1371/journal.pntd.0011867 (Apr 2024); https://clinicaltrials.gov/study/NCT05169554 (2021) |
| High-dose rifampicin + DACC dressings | Higher-than-standard rifampicin dose + dialkylcarbamoyl chloride-coated dressings | Phase 3 protocol in Ghana; implementation-focused strategy aiming at faster bacterial clearance and cost-effectiveness | Rationale is that rifampicin is the key drug and higher doses may improve healing; DACC dressings irreversibly bind bacteria on wound surfaces and may improve wound management (amoako2023burulirifdaccevaluationof pages 1-3) | PACTR202011867644311; primary endpoint: mean time to clearance of viable mycobacteria (amoako2023burulirifdaccevaluationof pages 1-3) | https://doi.org/10.3310/nihropenres.13332.1 (Nov 2023) |
| Telacebec (Q203) | Oral telacebec monotherapy or Q203-containing ultrashort regimens | Emerging experimental therapy; active phase 2 trial in Australia | Preclinical studies show extraordinary potency, with Q203-containing regimens rendering nearly all mouse footpads culture-negative after 2 weeks and suggesting potential 1-2 week oral cures (lim2025mycobacteriumulceransulcer pages 6-7) | NCT06481163; phase 2 recruiting trial of telacebec in adults with Buruli ulcer (lim2025mycobacteriumulceransulcer pages 6-7) | https://clinicaltrials.gov/study/NCT06481163 (2024); https://doi.org/10.3390/life15071096 (Jul 2025) |
| Thermotherapy | Local heat therapy integrated with wound management | Investigated as adjunct/alternative in field and community programs | Reported phase II cure rates >80% in one trial/reviewed experience; evidence remains less mature than antibiotic regimens (lim2025mycobacteriumulceransulcer pages 4-6) | NCT03969940 (withdrawn community-level thermotherapy study); NCT03957447 (observational integrated thermotherapy program) (lim2025mycobacteriumulceransulcer pages 4-6) | https://doi.org/10.3390/life15071096 (Jul 2025); https://clinicaltrials.gov/study/NCT03969940 (2019); https://clinicaltrials.gov/study/NCT03957447 (2019) |
| Topical clarithromycin formulation | 1% clarithromycin skin cream | Experimental formulation; not standard of care | Stable for at least 60 days, including at 40°C, supporting feasibility for low-resource settings and future topical treatment development (amoako2023burulirifdaccevaluationof pages 1-3) | No NCT provided in retrieved evidence (amoako2023burulirifdaccevaluationof pages 1-3) | https://doi.org/10.3390/ph17060691 (May 2024) |


*Table: This table summarizes current standard, historical, adjunctive, and emerging Buruli ulcer treatments, including dosing, real-world implementation, and active/recent clinical trials. It is useful for comparing established care with treatment-shortening and next-generation strategies.*

### 12.3 Suggested MAXO terms (examples)
- Antibiotic therapy (rifampicin + clarithromycin)
- Wound care management / wound dressing
- Surgical debridement / skin grafting (selected cases)
- Thermotherapy (adjunct)

## 13. Prevention

### 13.1 Current prevention practices
No licensed BU vaccine is available; prevention currently emphasizes **early detection and treatment**, plus reducing high-risk exposures and addressing skin injury care in endemic settings (boakyeappiah2023currentprogressand pages 1-5, gohoho2025riskfactorsfor pages 13-15). Epidemiological evidence supports public health messaging about protective clothing and safer water-contact practices in high-risk agricultural/wetland settings (johnson2025territorialandgenderlinked pages 9-12).

### 13.2 Vaccines (status and latest research)
BCG provides partial/transient protection and remains a baseline comparator in animal studies; no experimental strategy has clearly surpassed BCG in the cited vaccine review chapter (boakyeappiah2023currentprogressand pages 1-5). Vaccine development is complicated by mycolactone-mediated immunosuppression, but mycolactone-directed strategies are under investigation (boakyeappiah2023currentprogressand pages 14-17).

## 14. Other species / natural disease

Australian data implicate native **possums** as natural hosts, with geographic linkage to human cases (muhi2023ahumanmodel pages 1-2). Environmental and animal-associated evidence includes *M. ulcerans* DNA detection in aquatic organisms and insects (anthony2024buruliulcertransmission pages 1-2, oseiowusu2023buruliulcerin pages 5-7). A broader set of mycolactone-producing mycobacteria includes amphibian-associated strains (e.g., frog pathogen ecovar liflandii) referenced in ecology reviews (oseiowusu2023buruliulcerin pages 20-21).

## 15. Model organisms

Mouse models are used for immunologic mechanism and therapeutic evaluation. For example, IFN-γ knockout mice show reduced capacity to control infection and more rapid progression, supporting a role for IFN-γ-mediated immunity in BU (muhi2023ahumanmodel pages 1-2). Mycolactone alone can reproduce BU-like lesions in animal models, supporting toxin-driven pathology (akolgo2024exploringmycolactone—theunique pages 4-6).

## Expert opinions and authoritative analyses (selected)
A vaccine-focused expert review emphasizes that mycolactone “is cytotoxic and immunosuppressive and causes vascular dysfunction in infected skin,” and that its Sec61 targeting is a major advance in pathogenesis understanding (boakyeappiah2023currentprogressand pages 1-5). A clinical overview for Australian primary care stresses that PCR is central for diagnosis and that non-ulcerative disease requires biopsy due to swab false negatives (obrien2024anoverviewof pages 1-2).

## Key quantitative statistics (recently reported in retrieved sources)
- WHO 2023 notified BU cases: **1,952 total**, **1,573 Africa**, **379 Western Pacific** (akolgo2024exploringmycolactone—theunique pages 3-4).
- Australia: median age at diagnosis **66 years**; oedematous form ~**8%**; multiple lesions ~**5%** (obrien2024anoverviewof pages 1-2).
- Risk/protective factors (Ghana case-control): farming without protective clothing aOR **3.02**; living near waterbodies aOR **4.45**; injury alcohol cleansing aOR **0.17** (protective) (gohoho2025riskfactorsfor pages 13-15).
- Prototype mycolactone rapid test detection limit: **3.5–7 ng** from a swab; ~**2 h** workflow (siirin2024towardsaburuli pages 1-5).

## Limitations of this evidence package
Several required ontology identifiers (ICD-10/ICD-11, Orphanet ORPHA, MONDO) and GBD-style incidence/prevalence per 100,000 and DALYs were not found within the retrieved in-session texts. These fields should be completed via direct ontology/registry lookups or additional targeted literature retrieval outside the present evidence set.


References

1. (akolgo2024exploringmycolactone—theunique pages 1-3): Gideon Atinga Akolgo, Kingsley Bampoe Asiedu, and Richard Kwamla Amewu. Exploring mycolactone—the unique causative toxin of buruli ulcer: biosynthetic, synthetic pathways, biomarker for diagnosis, and therapeutic potential. Toxins, 16:528, Dec 2024. URL: https://doi.org/10.3390/toxins16120528, doi:10.3390/toxins16120528. This article has 3 citations.

2. (muhi2023ahumanmodel pages 1-2): Stephen Muhi, Joshua Osowicki, Daniel O’Brien, Paul D. R. Johnson, Sacha Pidot, Marcel Doerflinger, Julia L. Marshall, Marc Pellegrini, James McCarthy, and Timothy P. Stinear. A human model of buruli ulcer: the case for controlled human infection and considerations for selecting a mycobacterium ulcerans challenge strain. PLOS Neglected Tropical Diseases, 17:e0011394, Jun 2023. URL: https://doi.org/10.1371/journal.pntd.0011394, doi:10.1371/journal.pntd.0011394. This article has 8 citations and is from a domain leading peer-reviewed journal.

3. (anthony2024buruliulcertransmission pages 1-2): Michelle R. Anthony, Christopher Farkouh, P. Abdi, and Qasiar Ali Khan. Buruli ulcer transmission: environmental pathways and implications for dermatologic care. Cutis, 114 6:184-186, Dec 2024. URL: https://doi.org/10.12788/cutis.1145, doi:10.12788/cutis.1145. This article has 1 citations and is from a peer-reviewed journal.

4. (akolgo2024exploringmycolactone—theunique pages 3-4): Gideon Atinga Akolgo, Kingsley Bampoe Asiedu, and Richard Kwamla Amewu. Exploring mycolactone—the unique causative toxin of buruli ulcer: biosynthetic, synthetic pathways, biomarker for diagnosis, and therapeutic potential. Toxins, 16:528, Dec 2024. URL: https://doi.org/10.3390/toxins16120528, doi:10.3390/toxins16120528. This article has 3 citations.

5. (NCT00321178 chunk 2):  BURULICO Drug Trial Study Protocol: RCT SR8/SR4+CR4, GHANA. University Medical Center Groningen. 2006. ClinicalTrials.gov Identifier: NCT00321178

6. (obrien2024anoverviewof pages 1-2): Daniel P O'Brien, Christopher Chun Wen Wong, and Stephen Muhi. An overview of buruli ulcer in australia. Australian journal of general practice, 53 9:671-674, Sep 2024. URL: https://doi.org/10.31128/ajgp-08-23-6914, doi:10.31128/ajgp-08-23-6914. This article has 5 citations.

7. (NCT01659437 chunk 1): Tjip van der Werf. WHO Drug Study for Buruli Ulcer - Comparison of SR8 and CR8. University Medical Center Groningen. 2012. ClinicalTrials.gov Identifier: NCT01659437

8. (akolgo2024exploringmycolactone—theunique pages 4-6): Gideon Atinga Akolgo, Kingsley Bampoe Asiedu, and Richard Kwamla Amewu. Exploring mycolactone—the unique causative toxin of buruli ulcer: biosynthetic, synthetic pathways, biomarker for diagnosis, and therapeutic potential. Toxins, 16:528, Dec 2024. URL: https://doi.org/10.3390/toxins16120528, doi:10.3390/toxins16120528. This article has 3 citations.

9. (gohoho2025riskfactorsfor pages 13-15): Mawuli Gohoho, Samuel Adolf Bosoka, George Sarpong Agyemang, Sorengmen Amos Ziema, James Alorwu, Hudatu Ahmed, Christian Atsu Gohoho, Isaac Annobil, Nana Konama Kotey, and John Owusu Gyapong. Risk factors for buruli ulcer disease in ghana: a matched case-control study in four selected endemic districts of eastern and oti regions. PLOS Neglected Tropical Diseases, 19:e0013684, Nov 2025. URL: https://doi.org/10.1371/journal.pntd.0013684, doi:10.1371/journal.pntd.0013684. This article has 0 citations and is from a domain leading peer-reviewed journal.

10. (johnson2025territorialandgenderlinked pages 9-12): Harvey Johnson, Alexandra Boccarossa, Esai Anagonou, Télésphore Brou, Perin Catraye, Sébastien Fleuret, Estelle Marion, and Matthieu Eveillard. Territorial and gender-linked risk factors for buruli ulcer in southern benin: a case-control study using geographic and behavioral surveying. PLOS Neglected Tropical Diseases, 19:e0013509, Sep 2025. URL: https://doi.org/10.1371/journal.pntd.0013509, doi:10.1371/journal.pntd.0013509. This article has 2 citations and is from a domain leading peer-reviewed journal.

11. (akolgo2024exploringmycolactone—theunique media 536a767e): Gideon Atinga Akolgo, Kingsley Bampoe Asiedu, and Richard Kwamla Amewu. Exploring mycolactone—the unique causative toxin of buruli ulcer: biosynthetic, synthetic pathways, biomarker for diagnosis, and therapeutic potential. Toxins, 16:528, Dec 2024. URL: https://doi.org/10.3390/toxins16120528, doi:10.3390/toxins16120528. This article has 3 citations.

12. (boakyeappiah2023currentprogressand pages 1-5): Justice Boakye-Appiah, Belinda Hall, Rajko Reljic, and Rachel E. Simmonds. Current progress and prospects for a buruli ulcer vaccine. Vaccines for Neglected Pathogens: Strategies, Achievements and Challenges, pages 71-95, Jan 2023. URL: https://doi.org/10.1007/978-3-031-24355-4\_5, doi:10.1007/978-3-031-24355-4\_5. This article has 5 citations.

13. (oseiowusu2023buruliulcerin pages 5-7): Jonathan Osei-Owusu, Owusu Fordjour Aidoo, Fatima Eshun, David Sewordor Gaikpa, Aboagye Kwarteng Dofuor, Bright Yaw Vigbedor, Bernard Kofi Turkson, Kingsley Ochar, John Opata, Maxwell Jnr. Opoku, Kodwo Dadzie Ninsin, and Christian Borgemeister. Buruli ulcer in africa: geographical distribution, ecology, risk factors, diagnosis, and indigenous plant treatment options – a comprehensive review. Heliyon, 9:e22018, Nov 2023. URL: https://doi.org/10.1016/j.heliyon.2023.e22018, doi:10.1016/j.heliyon.2023.e22018. This article has 8 citations.

14. (muhi2023ahumanmodel pages 12-13): Stephen Muhi, Joshua Osowicki, Daniel O’Brien, Paul D. R. Johnson, Sacha Pidot, Marcel Doerflinger, Julia L. Marshall, Marc Pellegrini, James McCarthy, and Timothy P. Stinear. A human model of buruli ulcer: the case for controlled human infection and considerations for selecting a mycobacterium ulcerans challenge strain. PLOS Neglected Tropical Diseases, 17:e0011394, Jun 2023. URL: https://doi.org/10.1371/journal.pntd.0011394, doi:10.1371/journal.pntd.0011394. This article has 8 citations and is from a domain leading peer-reviewed journal.

15. (muhi2025managementofmycobacterium pages 2-3): Stephen Muhi, Victoria RV Cox, Matthew O'Brien, Jonathan T Priestley, Jodie Hill, Adrian Murrie, Anthony McDonald, Peter Callan, Grant A Jenkin, N Deborah Friedman, Kasha P Singh, Callum Maggs, Peter Kelley, Eugene Athan, Paul DR Johnson, and Daniel P O'Brien. Management of mycobacterium ulcerans infection (buruli ulcer) in australia: consensus statement. The Medical Journal of Australia, 222:571-578, Feb 2025. URL: https://doi.org/10.5694/mja2.52591, doi:10.5694/mja2.52591. This article has 6 citations.

16. (lim2025mycobacteriumulceransulcer pages 7-9): Bryan Lim, Omar Shadid, Jennifer Novo, Yi Mon, Ishith Seth, Gianluca Marcaccini, Roberto Cuomo, Daniel P. O’Brien, and Warren M. Rozen. Mycobacterium ulcerans ulcer: current trends in antimicrobial management and reconstructive surgical strategies. Life, 15:1096, Jul 2025. URL: https://doi.org/10.3390/life15071096, doi:10.3390/life15071096. This article has 1 citations.

17. (combe2020areallburuli pages 4-6): M. Combe, P. Couppié, R. Blaizot, A. Valentini, and R.E. Gozlan. Are all buruli ulcers caused by <i>mycobacterium ulcerans</i> ? British Journal of Dermatology, 183:968-970, Jul 2020. URL: https://doi.org/10.1111/bjd.19260, doi:10.1111/bjd.19260. This article has 5 citations and is from a highest quality peer-reviewed journal.

18. (lim2025mycobacteriumulceransulcer pages 19-20): Bryan Lim, Omar Shadid, Jennifer Novo, Yi Mon, Ishith Seth, Gianluca Marcaccini, Roberto Cuomo, Daniel P. O’Brien, and Warren M. Rozen. Mycobacterium ulcerans ulcer: current trends in antimicrobial management and reconstructive surgical strategies. Life, 15:1096, Jul 2025. URL: https://doi.org/10.3390/life15071096, doi:10.3390/life15071096. This article has 1 citations.

19. (siirin2024towardsaburuli pages 1-5): Marina Siirin, Bijan Pedram, Maria J. Gonzalez-Moa, Louisa Warryn, Rie Yotsu, Jean M. Saunders, Aaron E. Saunders, Richard K. Baldwin, Jessica L. Porter, Timothy P. Stinear, Israel Cruz-Mata, Dziedzom Komi de Souza, Gerd Pluschke, and Marco A. Biamonte. Towards a buruli ulcer rapid diagnostic test that targets mycolactone. MedRxiv, Jan 2024. URL: https://doi.org/10.1101/2024.01.23.24301643, doi:10.1101/2024.01.23.24301643. This article has 1 citations.

20. (akolgo2024exploringmycolactone—theunique pages 18-20): Gideon Atinga Akolgo, Kingsley Bampoe Asiedu, and Richard Kwamla Amewu. Exploring mycolactone—the unique causative toxin of buruli ulcer: biosynthetic, synthetic pathways, biomarker for diagnosis, and therapeutic potential. Toxins, 16:528, Dec 2024. URL: https://doi.org/10.3390/toxins16120528, doi:10.3390/toxins16120528. This article has 3 citations.

21. (lim2025mycobacteriumulceransulcer pages 4-6): Bryan Lim, Omar Shadid, Jennifer Novo, Yi Mon, Ishith Seth, Gianluca Marcaccini, Roberto Cuomo, Daniel P. O’Brien, and Warren M. Rozen. Mycobacterium ulcerans ulcer: current trends in antimicrobial management and reconstructive surgical strategies. Life, 15:1096, Jul 2025. URL: https://doi.org/10.3390/life15071096, doi:10.3390/life15071096. This article has 1 citations.

22. (lim2025mycobacteriumulceransulcer pages 2-4): Bryan Lim, Omar Shadid, Jennifer Novo, Yi Mon, Ishith Seth, Gianluca Marcaccini, Roberto Cuomo, Daniel P. O’Brien, and Warren M. Rozen. Mycobacterium ulcerans ulcer: current trends in antimicrobial management and reconstructive surgical strategies. Life, 15:1096, Jul 2025. URL: https://doi.org/10.3390/life15071096, doi:10.3390/life15071096. This article has 1 citations.

23. (saezlopez2024amoxicillinclavulanateincombination pages 1-2): Emma Sáez-López, Ana Cristina Millán Placer, A. Quintana, and Santiago Ramón-García. Amoxicillin/clavulanate in combination with rifampicin/clarithromycin is bactericidal against mycobacterium ulcerans. PLOS Neglected Tropical Diseases, 18:e0011867, Apr 2024. URL: https://doi.org/10.1371/journal.pntd.0011867, doi:10.1371/journal.pntd.0011867. This article has 5 citations and is from a domain leading peer-reviewed journal.

24. (NCT05169554 chunk 1):  Beta-Lactam Containing Regimen for the Shortening of Buruli Ulcer Disease Therapy. Fundacion Agencia Aragonesa para la Investigacion y Desarrollo (ARAID). 2021. ClinicalTrials.gov Identifier: NCT05169554

25. (amoako2023burulirifdaccevaluationof pages 1-3): Yaw Ampem Amoako, Abigail Agbanyo, Jacob Novignon, Lucy Owusu, Joseph Tuffour, Adwoa Asante-Poku, Yohannes Hailemichael, Iris Mosweu, Ruth Canter, Charles Opondo, Elizabeth Allen, Catherine Pitt, Dorothy Yeboah-Manu, Stephen L. Walker, Michael Marks, and Richard Odame Phillips. Buruli-rifdacc: evaluation of the efficacy and cost-effectiveness of high-dose versus standard-dose rifampicin on outcomes in mycobacterium ulcerans disease, a protocol for a randomised controlled trial in ghana. NIHR Open Research, 2:59, Nov 2023. URL: https://doi.org/10.3310/nihropenres.13332.1, doi:10.3310/nihropenres.13332.1. This article has 4 citations.

26. (lim2025mycobacteriumulceransulcer pages 6-7): Bryan Lim, Omar Shadid, Jennifer Novo, Yi Mon, Ishith Seth, Gianluca Marcaccini, Roberto Cuomo, Daniel P. O’Brien, and Warren M. Rozen. Mycobacterium ulcerans ulcer: current trends in antimicrobial management and reconstructive surgical strategies. Life, 15:1096, Jul 2025. URL: https://doi.org/10.3390/life15071096, doi:10.3390/life15071096. This article has 1 citations.

27. (klis2024pharmacokineticsofextendedrelease pages 5-6): Sandor-Adrian Klis, Ymkje Stienstra, Kabiru M. Abass, Justice Abottsi, Samuel O. Mireku, Jan-Willem Alffenaar, and Tjip S. van der Werf. Pharmacokinetics of extended-release clarithromycin in patients with mycobacterium ulcerans infection. Scientific Reports, Aug 2024. URL: https://doi.org/10.1038/s41598-024-70890-w, doi:10.1038/s41598-024-70890-w. This article has 1 citations and is from a peer-reviewed journal.

28. (boakyeappiah2023currentprogressand pages 14-17): Justice Boakye-Appiah, Belinda Hall, Rajko Reljic, and Rachel E. Simmonds. Current progress and prospects for a buruli ulcer vaccine. Vaccines for Neglected Pathogens: Strategies, Achievements and Challenges, pages 71-95, Jan 2023. URL: https://doi.org/10.1007/978-3-031-24355-4\_5, doi:10.1007/978-3-031-24355-4\_5. This article has 5 citations.

29. (oseiowusu2023buruliulcerin pages 20-21): Jonathan Osei-Owusu, Owusu Fordjour Aidoo, Fatima Eshun, David Sewordor Gaikpa, Aboagye Kwarteng Dofuor, Bright Yaw Vigbedor, Bernard Kofi Turkson, Kingsley Ochar, John Opata, Maxwell Jnr. Opoku, Kodwo Dadzie Ninsin, and Christian Borgemeister. Buruli ulcer in africa: geographical distribution, ecology, risk factors, diagnosis, and indigenous plant treatment options – a comprehensive review. Heliyon, 9:e22018, Nov 2023. URL: https://doi.org/10.1016/j.heliyon.2023.e22018, doi:10.1016/j.heliyon.2023.e22018. This article has 8 citations.
