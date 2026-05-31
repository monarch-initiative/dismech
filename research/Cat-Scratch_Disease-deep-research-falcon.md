---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T19:30:14.574177'
end_time: '2026-05-06T19:50:13.335289'
duration_seconds: 1198.76
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cat-scratch Disease
  mondo_id: ''
  category: Infectious
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 56
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cat-scratch Disease
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Cat-scratch Disease** covering all of the
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
- **Disease Name:** Cat-scratch Disease
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Cat-scratch Disease** covering all of the
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


# Cat-scratch disease (CSD) — Comprehensive Disease Characteristics Report (Infectious)

**Target disease:** Cat-scratch disease (CSD)  
**Causal agent (primary):** *Bartonella henselae* (facultative intracellular Gram-negative bacillus) (puspitasari2025uncoveringthetruth pages 1-2, smith2024catscratchdiseasemimicking pages 3-5)  
**Last updated:** 2026-05-06  

## Executive summary
Cat-scratch disease is a zoonotic infection most commonly acquired after contact with cats (often kittens), classically presenting as subacute regional lymphadenopathy, sometimes preceded by an inoculation papule/pustule; a clinically important minority develop atypical/disseminated disease (e.g., hepatosplenic microabscesses, osteomyelitis, ocular disease, neurologic syndromes). Key diagnostic modalities in real-world practice are serology (IFA/ELISA), histopathology of lymph node tissue in selected cases, and nucleic-acid detection (PCR or increasingly metagenomic next-generation sequencing [mNGS] for atypical disease). Treatment is often supportive/observational for uncomplicated disease, with azithromycin commonly used to shorten symptom course; complicated ocular/CNS disease is often treated with doxycycline plus rifampin based on expert recommendations and case-based evidence. (amin2022catscratchdisease pages 1-2, amin2022catscratchdisease pages 2-3, sulaiman2023catscratchdisease pages 4-7, rolain2004recommendationsfortreatment pages 6-7)

---

## 1. Disease information
### 1.1 Definition and overview
CSD is an infectious zoonosis “caused by *Bartonella henselae* infection” and typically presents with “regional lymphadenopathy following a cat scratch or bite.” (smith2024catscratchdiseasemimicking pages 3-5) A recent review similarly defines CSD as a systemic infection due to the intracellular Gram-negative zoonotic bacillus *B. henselae*. (puspitasari2025uncoveringthetruth pages 1-2)

**Direct abstract-supporting quote(s)**
- “Cat-scratch disease (CSD) is caused by a bacterial infection due to *Bartonella henselae*…” (Sulaiman et al., 2023-08, *Cureus*) (sulaiman2023catscratchdisease pages 4-7)
- “Cat-scratch disease (CSD) is caused by *Bartonella henselae* infection.” (Li et al., 2024-04, *J Ophthalmic Inflamm Infect*) (lai2026clinicalandepidemiological pages 1-2)

### 1.2 Key identifiers (ontology/clinical)
**Not fully retrievable from the currently retrieved full-text corpus.** The evidence set did not directly include MONDO, MeSH, or ICD code strings for CSD. (No in-corpus evidence)

**What is available from retrieved clinical literature:** the disease entity is consistently referenced as “cat-scratch disease,” “cat scratch disease,” and “Bartonella henselae infection,” and is discussed in the context of lymphadenitis/lymphadenopathy differentials. (sulaiman2023catscratchdisease pages 4-7, amin2022catscratchdisease pages 2-3, smith2024catscratchdiseasemimicking pages 3-5)

### 1.3 Common synonyms / alternative names
- Cat scratch disease / cat-scratch disease (CSD) (sulaiman2023catscratchdisease pages 4-7, smith2024catscratchdiseasemimicking pages 3-5)
- *Bartonella henselae* lymphadenitis / bartonellosis presenting as lymphadenitis (sulaiman2023catscratchdisease pages 4-7, amin2022catscratchdisease pages 2-3)
- Ocular bartonellosis / ocular CSD (e.g., neuroretinitis) (lai2026clinicalandepidemiological pages 1-2, bush2024neurobartonellosesemergingfrom pages 28-29)

### 1.4 Evidence source types (patient-level vs aggregated)
- **Aggregated cohorts:** large pediatric clinical cohort (Atlanta, 2010–2018; n=304) providing frequencies and imaging/lab distributions (amin2022catscratchdisease pages 1-2, amin2022catscratchdisease pages 2-3, amin2022catscratchdisease pages 3-4)
- **Patient-level case reports/series:** multiple 2023–2024 clinical case reports highlighting atypical presentations and diagnostic pitfalls (sulaiman2023catscratchdisease pages 4-7, smith2024catscratchdiseasemimicking pages 3-5)
- **Mechanistic reviews/experimental studies:** immune evasion and cell biology (Virulence 2024) and neurobartonellosis review (Parasites & Vectors 2024), with supporting in vitro endothelial/erythrocyte tropism and immune-modulation mechanisms (bush2024neurobartonellosesemergingfrom pages 28-29, xi2024sneakytacticsingenious pages 5-6, xi2024sneakytacticsingenious pages 2-4, xi2024sneakytacticsingenious pages 6-7)

---

## 2. Etiology
### 2.1 Disease causal factors
- **Infectious cause:** Predominantly *B. henselae* (puspitasari2025uncoveringthetruth pages 1-2, smith2024catscratchdiseasemimicking pages 3-5).
- **Occasional related agents:** other feline-associated *Bartonella* spp. (e.g., *B. clarridgeiae*, *B. koehlerae*) are discussed as potential causes of similar syndromes in some reviews. (puspitasari2025uncoveringthetruth pages 2-3, puspitasari2025uncoveringthetruth pages 1-2)

### 2.2 Risk factors
**Animal/vector exposure (dominant risk factor class):**
- High association with cat exposure in pediatric series: **92.4% feline exposure (242/262)** in the Atlanta pediatric cohort. (amin2022catscratchdisease pages 1-2)
- Review-level risk factors include kittens, fleas, stray/shelter cats, multicat households, outdoor cats, and hot/humid environments. (puspitasari2025uncoveringthetruth pages 5-6)

**Host factors:**
- Immunocompromised status is associated with more severe complications (e.g., bacillary angiomatosis, severe systemic disease); case reports emphasize broadened differential in people living with HIV. (smith2024catscratchdiseasemimicking pages 3-5, puspitasari2025uncoveringthetruth pages 5-6)

**Direct abstract-supporting quote(s)**
- “B. henselae is transmitted from cats to humans through scratching or biting…” (Sulaiman et al., 2023-08, *Cureus*) (sulaiman2023catscratchdisease pages 4-7)

### 2.3 Protective factors
No specific genetic protective variants or environmental protective factors were identified in the retrieved evidence. Primary preventive measures are behavioral and veterinary (flea control, avoiding bites/scratches). (puspitasari2025uncoveringthetruth pages 6-7, puspitasari2025uncoveringthetruth pages 5-6)

### 2.4 Gene–environment interactions
No human host GxE interactions were identified in the retrieved evidence corpus. (No in-corpus evidence)

---

## 3. Phenotypes
### 3.1 Typical phenotype cluster
**Core syndrome:** inoculation lesion followed by regional lymphadenopathy ± fever.
- In a 304-case pediatric cohort, **lymphadenopathy occurred in 78.8% (234/297)** and **fever in 46.4% (141/304)**. (amin2022catscratchdisease pages 2-3)
- Lymph node site distribution in that cohort included **cervical 52.0%**, **axillary 28.3%**, and **inguinal 13.9%** (site denominators vary by documentation). (amin2022catscratchdisease pages 2-3)

**Timing:**
- Papule/pustule may appear **7–12 days** after inoculation and lymphadenopathy typically appears **1–3 weeks** after inoculation in review literature. (puspitasari2025uncoveringthetruth pages 5-6)
- Case-based discussion cites presentation typically **3–14 days** after scratch or bite. (smith2024catscratchdiseasemimicking pages 3-5)

### 3.2 Atypical/disseminated phenotypes (selected)
**Atypical presentations are common in tertiary-care cohorts:** **20.7% (63/304)** lacked lymphadenopathy and were classified as atypical in the Atlanta pediatric cohort. (amin2022catscratchdisease pages 1-2, amin2022catscratchdisease pages 2-3)

**Hepatosplenic disease (microabscesses/splenomegaly):** among abdominally imaged children (n=55), **38.1%** had splenic and/or hepatic microabscesses and **36.4%** had splenomegaly. (amin2022catscratchdisease pages 1-2, amin2022catscratchdisease pages 3-4)

**Bone involvement:** among those with bone MRI (n=20), **35.0%** had bone MRI involvement. (amin2022catscratchdisease pages 3-4)

**Neuro-ophthalmic / CNS involvement:** among those with neuroimaging (n=29), **27.6%** had optic neuritis and **17.2%** had encephalitis-like findings. (amin2022catscratchdisease pages 3-4)

### 3.3 Suggested HPO terms and phenotype annotations
A structured phenotype-to-ontology mapping with frequencies and timing is provided in **artifact-01**.

| Phenotype / complication | Suggested HPO term(s) | Frequency / distribution | Typical time to onset | Affected anatomy (suggested UBERON) | Notes / evidence (with URL) |
|---|---|---|---|---|---|
| Inoculation papule / pustule | HP:0011123 Skin papule; HP:0000989 Pustule | Not quantified in Amin 2022 cohort | Papule/pustule typically appears 7–12 days after inoculation; overall symptoms may begin 3–14 days after scratch/bite | UBERON:0001003 skin | Primary inoculation lesion after cat-associated injury; useful early clue before lymphadenopathy. URLs: https://doi.org/10.5455/ovj.2025.v15.i5.5 ; https://doi.org/10.7759/cureus.66840 (puspitasari2025uncoveringthetruth pages 5-6, smith2024catscratchdiseasemimicking pages 3-5) |
| Regional lymphadenopathy (overall) | HP:0002716 Lymphadenopathy | 78.8% (234/297) in Atlanta pediatric cohort | Usually develops 1–3 weeks after inoculation; classic illness often appears 3–14 days after scratch/bite | UBERON:0000029 lymph node | Core phenotype of typical CSD; median lymphadenopathy duration at presentation 9 days (IQR 6–21). URL: https://doi.org/10.1093/ofid/ofac426 ; https://doi.org/10.5455/ovj.2025.v15.i5.5 ; https://doi.org/10.7759/cureus.66840 (amin2022catscratchdisease pages 2-3, puspitasari2025uncoveringthetruth pages 5-6, smith2024catscratchdiseasemimicking pages 3-5) |
| Cervical lymphadenopathy | HP:0007676 Cervical lymphadenopathy | 52.0% (104/200) among cases with site data | As above: usually 1–3 weeks after inoculation | UBERON:0000057 cervical lymph node | Most common nodal site in Amin 2022 pediatric cohort. URL: https://doi.org/10.1093/ofid/ofac426 (amin2022catscratchdisease pages 2-3, amin2022catscratchdisease pages 3-4) |
| Axillary lymphadenopathy | HP:0010780 Axillary lymphadenopathy | 28.3% (67/237) in Amin 2022; 43% cited in Smith 2024 review-style discussion | As above: usually 1–3 weeks after inoculation | UBERON:0001421 axillary lymph node | Common after upper-extremity inoculation; site frequency varies by cohort/source. URL: https://doi.org/10.1093/ofid/ofac426 ; https://doi.org/10.7759/cureus.66840 (amin2022catscratchdisease pages 2-3, smith2024catscratchdiseasemimicking pages 3-5) |
| Inguinal lymphadenopathy | HP:0100765 Inguinal lymphadenopathy | 13.9% (37/266) in Amin 2022 | As above: usually 1–3 weeks after inoculation | UBERON:0011274 inguinal lymph node | Less common than cervical/axillary disease but well-described, including atypical presentations. URL: https://doi.org/10.1093/ofid/ofac426 ; https://doi.org/10.7759/cureus.44280 (amin2022catscratchdisease pages 2-3, sulaiman2023catscratchdisease pages 4-7) |
| Fever | HP:0001945 Fever | 46.4% (141/304) in Amin 2022 | Often accompanies/subsequently follows lymphadenopathy; overall illness may begin 3–14 days after scratch/bite | UBERON:0000178 blood / systemic | Frequent systemic feature; more pronounced in atypical/disseminated disease. URL: https://doi.org/10.1093/ofid/ofac426 ; https://doi.org/10.7759/cureus.66840 (amin2022catscratchdisease pages 2-3, smith2024catscratchdiseasemimicking pages 3-5) |
| Splenomegaly | HP:0001744 Splenomegaly | 8.5% (23/270) clinically in Amin 2022; 36.4% (20/55) among those with abdominal imaging | Usually part of atypical/disseminated hepatosplenic disease | UBERON:0002106 spleen | Suggests systemic spread; in imaged patients, splenomegaly and microabscesses were common. URL: https://doi.org/10.1093/ofid/ofac426 (amin2022catscratchdisease pages 1-2, amin2022catscratchdisease pages 3-4) |
| Hepatic and/or splenic microabscesses (hepatosplenic CSD) | HP:0011962 Abnormality of the spleen; HP:0002240 Hepatomegaly; HP:0002572 Hepatic abscess | 38.1% (21/55) among abdominally imaged patients in Amin 2022 | Atypical/disseminated manifestation; timing not precisely quantified in retrieved cohort | UBERON:0002107 liver; UBERON:0002106 spleen | Important radiologic marker of hepatosplenic involvement; abdominal US/CT can detect lesions. URL: https://doi.org/10.1093/ofid/ofac426 ; https://doi.org/10.7759/cureus.66134 (amin2022catscratchdisease pages 1-2, amin2022catscratchdisease pages 3-4, nguyen2024threemonthhistoryof pages 4-6) |
| Osteomyelitis / bone involvement | HP:0002754 Osteomyelitis | Bone MRI involvement 35.0% (7/20) among those who underwent bone MRI in Amin 2022 | Atypical/disseminated manifestation; specific onset interval not reported in retrieved cohort | UBERON:0001474 bone element | Represents deeper disseminated infection; may mimic malignancy or other chronic inflammatory bone disease. URL: https://doi.org/10.1093/ofid/ofac426 (amin2022catscratchdisease pages 3-4) |
| Ocular neuroretinitis | HP:0012372 Neuroretinitis | Not population-quantified in Amin overall cohort; ocular disease included among atypical presentations | Ocular manifestations tend to arise after systemic illness; exact timing variable | UBERON:0000966 retina; UBERON:0001004 optic nerve | Vision-threatening atypical CSD phenotype; often linked to Bartonella serology and ocular imaging. URL: https://doi.org/10.4274/tjo.galenos.2022.44692 ; https://doi.org/10.1186/s12348-024-00387-0 (lai2026clinicalandepidemiological pages 1-2) |
| Optic neuritis / optic nerve involvement | HP:0000648 Optic neuritis | 27.6% (8/29) among those with neuroimaging in Amin 2022 | Variable; part of neuro-ophthalmic dissemination | UBERON:0001004 optic nerve | Neuroimaging in Amin identified optic neuritis in a substantial subset of imaged patients. URL: https://doi.org/10.1093/ofid/ofac426 (amin2022catscratchdisease pages 3-4) |
| Uveitis | HP:0000554 Uveitis | Not quantified in Amin cohort; ocular series reported anterior uveitis in 13% of affected eyes | Variable; atypical ocular manifestation | UBERON:0001768 uvea | Reported ocular manifestation of CSD alongside neuroretinitis, retinal infiltrates, and vascular occlusions. URL: https://doi.org/10.4274/tjo.galenos.2022.44692 ; https://doi.org/10.1186/s12886-023-03063-4 (lai2026clinicalandepidemiological pages 1-2) |
| Meningoencephalitis / encephalitis | HP:0001298 Encephalopathy; HP:0002383 Encephalitis; HP:0001287 Meningitis | 17.2% (5/29) had encephalitis-like findings among those with neuroimaging in Amin 2022 | Atypical/disseminated complication; timing variable | UBERON:0000955 brain; UBERON:0002050 cerebral cortex; UBERON:000 membranes of brain/spinal cord | Neurologic involvement is uncommon but clinically important; included in the atypical CSD spectrum. URL: https://doi.org/10.1093/ofid/ofac426 ; https://doi.org/10.5455/ovj.2025.v15.i5.5 (amin2022catscratchdisease pages 3-4, puspitasari2025uncoveringthetruth pages 5-6) |


*Table: This table maps major cat-scratch disease phenotypes and complications to suggested HPO and UBERON terms, with quantitative frequencies from the Atlanta pediatric cohort and timing data from recent reviews/case literature. It is useful for ontology-based disease knowledge base population and phenotype annotation.*

---

## 4. Genetic/molecular information (human)
### 4.1 Causal genes and variants
CSD is not a Mendelian genetic disease; **no causal human gene** or pathogenic germline variant set is expected.

### 4.2 Host genetic susceptibility / modifiers
No reproducible host genetic susceptibility loci, modifier genes, or protective variants were identified in the retrieved evidence corpus. (No in-corpus evidence)

### 4.3 Pathogen molecular factors (key virulence determinants)
The retrieved evidence supports multiple molecular determinants of *B. henselae* pathogenicity:
- **BadA (Bartonella adhesin A):** implicated in host cell adhesion and biofilm formation; linked to VEGF induction and angiogenic responses. (xi2024sneakytacticsingenious pages 5-6, xi2024sneakytacticsingenious pages 2-4, gadila2025comparisonoftranscriptomic pages 1-2)
- **Type IV secretion systems:** VirB/D4 and Trw systems contribute to endothelial and erythrocyte interactions (erythrocyte binding/invasion and persistence). (xi2024sneakytacticsingenious pages 5-6, xi2024sneakytacticsingenious pages 6-7)
- **BafA (Bartonella angiogenic factor A):** described as binding VEGFR2 and acting as a VEGF mimic in mechanistic discussion. (xi2024sneakytacticsingenious pages 6-7)

---

## 5. Environmental information
### 5.1 Environmental factors
The dominant environmental contributors are zoonotic exposures (cats and cat-associated fleas), rather than classic toxin or pollution exposures. (puspitasari2025uncoveringthetruth pages 2-3, puspitasari2025uncoveringthetruth pages 5-6)

### 5.2 Lifestyle factors
No specific lifestyle factors (diet, smoking, alcohol) were identified in the retrieved evidence as independent risk modifiers. (No in-corpus evidence)

### 5.3 Infectious agent
- *Bartonella henselae* (primary). (puspitasari2025uncoveringthetruth pages 1-2, smith2024catscratchdiseasemimicking pages 3-5)

---

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (high-level)
1) **Inoculation** via scratch/bite/lick introduces *B. henselae* into skin and local tissues. (sulaiman2023catscratchdisease pages 4-7, puspitasari2025uncoveringthetruth pages 5-6)  
2) **Local immune activation** with regional lymph node involvement; inflammatory cytokines including IL-2/IL-6/IL-10 have been reported in CSD patients in mechanistic review. (xi2024sneakytacticsingenious pages 2-4)  
3) **Cell tropism and persistence:** bacteria invade endothelial cells and form Bartonella-containing vacuoles that resist acidification and lysosomal fusion, enabling intracellular survival; erythrocyte invasion provides an “immunological cloak”/sanctuary promoting persistent bacteremia. (xi2024sneakytacticsingenious pages 5-6, xi2024sneakytacticsingenious pages 6-7)  
4) **Dissemination** in some hosts results in hepatosplenic, bone, ocular, and neurologic disease; neurobartonellosis review highlights multiple potential reservoirs and cell types enabling CNS effects. (bush2024neurobartonellosesemergingfrom pages 28-29)

### 6.2 Cellular and immune processes (with ontology suggestions)
**Key processes (GO Biological Process suggestions):**
- Granulomatous inflammation (GO:0006954 inflammatory response; granuloma formation—closest mapping often via inflammatory response terms) supported by lymph node histopathology patterns (necrotizing granulomatous inflammation). (amin2022catscratchdisease pages 2-3, sulaiman2023catscratchdisease pages 4-7)
- Angiogenesis / vasoproliferation (GO:0001525 angiogenesis) via VEGF induction and VEGF-mimic factors (BadA-associated VEGF induction; BafA–VEGFR2 mimicry described). (xi2024sneakytacticsingenious pages 5-6, xi2024sneakytacticsingenious pages 6-7)
- Intracellular survival / evasion of lysosomal fusion (GO:0045087 innate immune response; GO:0045321 leukocyte activation; and processes related to endosome/lysosome trafficking), via BCVs resisting lysosomal fusion/acidification. (xi2024sneakytacticsingenious pages 5-6, xi2024sneakytacticsingenious pages 6-7)
- Immune regulation via IL-10 / STAT3 axis (GO:0006955 immune response; GO:0001817 regulation of cytokine production), enabling anti-inflammatory persistence. (bush2024neurobartonellosesemergingfrom pages 28-29, xi2024sneakytacticsingenious pages 2-4)

**Key cell types (Cell Ontology [CL] suggestions):**
- Vascular endothelial cell (CL:0000115), including HUVEC experimental systems used to assay virulence/angiogenesis. (kondo2025differentialvasoproliferativetraits pages 1-2, xi2024sneakytacticsingenious pages 5-6)
- Erythrocyte (CL:0000232) for intraerythrocytic persistence. (xi2024sneakytacticsingenious pages 6-7)
- Macrophage (CL:0000235), including possible “Trojan-horse” dissemination concept to brain. (bush2024neurobartonellosesemergingfrom pages 28-29)
- Microglial cell (CL:0000129) and pericyte (CL:0000669) noted as in vitro-infected cell types in neurobartonellosis review. (bush2024neurobartonellosesemergingfrom pages 28-29)
- CD34-positive hematopoietic progenitor cell (CL:0000055) as a potential reservoir niche. (xi2024sneakytacticsingenious pages 6-7)

**Anatomy (UBERON suggestions):**
- Skin (UBERON:0001003) inoculation site; lymph node (UBERON:0000029) primary clinical involvement. (puspitasari2025uncoveringthetruth pages 5-6, amin2022catscratchdisease pages 2-3)
- Spleen (UBERON:0002106) and liver (UBERON:0002107) in hepatosplenic CSD. (amin2022catscratchdisease pages 3-4)
- Retina (UBERON:0000966) and optic nerve (UBERON:0001004) in ocular disease. (amin2022catscratchdisease pages 3-4)
- Brain (UBERON:0000955) for CNS manifestations (encephalitis-like findings). (amin2022catscratchdisease pages 3-4)

### 6.3 Recent mechanistic developments (2023–2024 priority)
- **Immune evasion/persistence synthesis (2024, *Virulence*):** review describes endothelial invasion with vacuoles resisting lysosomal fusion, erythrocyte “sanctuaries,” BadA-associated VEGF induction and angiogenic modulation, and immune modulation including IL-10 pathways and biofilm-mediated protection. (xi2024sneakytacticsingenious pages 5-6, xi2024sneakytacticsingenious pages 2-4, xi2024sneakytacticsingenious pages 6-7)
- **Neurobartonellosis conceptual expansion (2024, *Parasites & Vectors*):** review emphasizes intracellular niches (endothelial cells, stromal cells, pericytes, microglia) and macrophage-mediated CNS access (“Trojan-horse”), plus VEGF-driven vascular remodeling/permeability as a plausible contributor to neurologic dysfunction. (bush2024neurobartonellosesemergingfrom pages 28-29)

---

## 7. Anatomical structures affected
**Primary:** lymph nodes (regional), skin at inoculation. (puspitasari2025uncoveringthetruth pages 5-6, amin2022catscratchdisease pages 2-3)

**Secondary (disseminated/atypical):**
- Hepatosplenic: liver and spleen microabscesses/splenomegaly (amin2022catscratchdisease pages 3-4)
- Musculoskeletal: bone involvement/osteomyelitis-like findings (amin2022catscratchdisease pages 3-4)
- Ocular/neuro-ophthalmic: optic nerve involvement/optic neuritis, neuroretinitis (amin2022catscratchdisease pages 3-4, lai2026clinicalandepidemiological pages 1-2)
- CNS: encephalitis-like findings (amin2022catscratchdisease pages 3-4)

---

## 8. Temporal development
**Onset pattern:** typically subacute.
- In review literature, inoculation lesion precedes regional lymphadenopathy by ~1–3 weeks; papule/pustule at ~7–12 days post-inoculation. (puspitasari2025uncoveringthetruth pages 5-6)

**Duration/course:**
- Disease is often self-limited; expert recommendations note regional lymphadenopathy commonly lasts **2–3 months**. (rolain2004recommendationsfortreatment pages 6-7)
- Another clinical summary reports typical CSD is self-limited resolving in **2–6 months**. (nguyen2024threemonthhistoryof pages 4-6)

---

## 9. Inheritance and population
### 9.1 Epidemiology
Structured quantitative epidemiology statistics are provided in **artifact-00**.

| Domain | Statistic (numeric) | Population/setting | Source (first author year, journal) | URL | Notes |
|---|---:|---|---|---|---|
| Incidence | 4.5–9.3 outpatient diagnoses per 100,000 | United States | Sulaiman 2023, *Cureus* | https://doi.org/10.7759/cureus.44280 | Reported US outpatient diagnosis rate for CSD (sulaiman2023catscratchdisease pages 4-7) |
| Incidence | 0.19–0.86 hospital admissions per 100,000 | United States | Sulaiman 2023, *Cureus* | https://doi.org/10.7759/cureus.44280 | Reported US hospitalization rate for CSD (sulaiman2023catscratchdisease pages 4-7) |
| Incidence | ~13,000 annual cases | United States | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Broader US annual burden cited in pediatric cohort paper (amin2022catscratchdisease pages 1-2) |
| Incidence | 22,000 new cases annually | United States | Puspitasari 2025, *Open Veterinary Journal* | https://doi.org/10.5455/ovj.2025.v15.i5.5 | Review estimate of annual US CSD burden (puspitasari2025uncoveringthetruth pages 2-3) |
| Incidence | 9.4 cases per 100,000 | US children age 5–9 years | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Highest incidence noted for children 5–9 years (amin2022catscratchdisease pages 1-2) |
| Incidence | 6.4 per 100,000 | South Atlantic region, United States | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Regional incidence cited for Georgia/South Atlantic setting (amin2022catscratchdisease pages 4-6) |
| Cohort size | 304 cases | Atlanta pediatric tertiary center, 2010–2018 | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Retrospective pediatric cohort (amin2022catscratchdisease pages 4-6, amin2022catscratchdisease pages 1-2) |
| Age | Median 8.1 years (IQR 5.4–12.1) | Atlanta pediatric cohort | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Typical school-age presentation (amin2022catscratchdisease pages 1-2, amin2022catscratchdisease pages 2-3) |
| Age | 90.1% <14 years | Atlanta pediatric cohort | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Pediatric skew of cases (amin2022catscratchdisease pages 2-3) |
| Age distribution | 20.7% age 0–4; 35.5% age 5–9; 33.9% age 10–14; 9.9% age 15–19 | Atlanta pediatric cohort | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Age-stratified case distribution (amin2022catscratchdisease pages 3-4) |
| Sex | 51.3% female | Atlanta pediatric cohort | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | 156/304 female (amin2022catscratchdisease pages 1-2) |
| Seasonality | August 13.5% (41/304) | Atlanta pediatric cohort | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Late-summer peak (amin2022catscratchdisease pages 1-2, amin2022catscratchdisease media 65029abb) |
| Seasonality | September 15.5% (47/304) | Atlanta pediatric cohort | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Peak month in cohort (amin2022catscratchdisease pages 1-2, amin2022catscratchdisease pages 2-3, amin2022catscratchdisease media 65029abb) |
| Seasonality | October 12.8% (39/304) | Atlanta pediatric cohort | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Fall clustering (amin2022catscratchdisease pages 2-3, amin2022catscratchdisease media 65029abb) |
| Seasonality | November 12.2% (37/304) | Atlanta pediatric cohort | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Fall clustering (amin2022catscratchdisease pages 2-3, amin2022catscratchdisease media 65029abb) |
| Seasonality | June 2.0% (6/304) | Atlanta pediatric cohort | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Lowest month reported (amin2022catscratchdisease pages 2-3, amin2022catscratchdisease media 65029abb) |
| Seasonality | May 3.3% (10/304) | Atlanta pediatric cohort | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Low-prevalence spring month (amin2022catscratchdisease pages 2-3, amin2022catscratchdisease media 65029abb) |
| Seasonality | April 4.6% (14/304) | Atlanta pediatric cohort | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Low-prevalence spring month (amin2022catscratchdisease pages 2-3, amin2022catscratchdisease media 65029abb) |
| Exposure | 92.4% feline exposure (242/262) | Atlanta pediatric cohort with documented exposure history | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Strong cat exposure association (amin2022catscratchdisease pages 1-2) |
| Exposure | 22.0% canine exposure (55/250) | Atlanta pediatric cohort with documented exposure history | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Dog exposure also reported in a minority (amin2022catscratchdisease pages 1-2) |
| Clinical features | 78.8% lymphadenopathy (234/297) | Atlanta pediatric cohort | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Predominant presentation (amin2022catscratchdisease pages 2-3, amin2022catscratchdisease pages 3-4) |
| Clinical features | 46.4% fever (141/304) | Atlanta pediatric cohort | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Common systemic symptom (amin2022catscratchdisease pages 2-3, amin2022catscratchdisease pages 3-4) |
| Clinical features | 20.7% atypical/non-lymphadenopathy presentations (63/304) | Atlanta pediatric cohort | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Included hepatosplenic, osteomyelitis, ocular, CNS disease (amin2022catscratchdisease pages 4-6, amin2022catscratchdisease pages 1-2, amin2022catscratchdisease pages 3-4) |
| Lymph node site | 52.0% cervical (104/200) | Atlanta pediatric cohort with node-site data | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Most frequent nodal site (amin2022catscratchdisease pages 2-3, amin2022catscratchdisease pages 3-4) |
| Lymph node site | 28.3% axillary (67/237) | Atlanta pediatric cohort with node-site data | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Second most frequent nodal site (amin2022catscratchdisease pages 2-3, amin2022catscratchdisease pages 3-4) |
| Lymph node site | 13.9% inguinal (37/266) | Atlanta pediatric cohort with node-site data | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Less common nodal site (amin2022catscratchdisease pages 2-3) |
| Clinical course | Median LAD duration 9 days (IQR 6–21) | Atlanta pediatric cohort | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Duration at presentation (amin2022catscratchdisease pages 2-3) |
| Labs | 26.6% leukocytosis (58/218) | Atlanta pediatric cohort tested for CBC abnormality | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Laboratory abnormality rate (amin2022catscratchdisease pages 2-3) |
| Labs | 49.6% elevated ESR (55/111) | Atlanta pediatric cohort tested for ESR | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Frequent inflammatory marker elevation (amin2022catscratchdisease pages 2-3) |
| Labs | 18.7% elevated CRP (34/184) | Atlanta pediatric cohort tested for CRP | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | CRP elevation less frequent than ESR (amin2022catscratchdisease pages 2-3) |
| Diagnostics | 58.2% had serology available (177/304) | Atlanta pediatric cohort | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Serology was the main diagnostic test (amin2022catscratchdisease pages 2-3) |
| Diagnostics | 63.2% IgM ≥1:20 (110/174) | Atlanta pediatric cohort tested serologically | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Positivity threshold used in cohort (amin2022catscratchdisease pages 2-3) |
| Diagnostics | 95.5% IgG ≥1:128 (169/177) | Atlanta pediatric cohort tested serologically | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | High IgG seropositivity among tested cases (amin2022catscratchdisease pages 2-3) |
| Diagnostics | 11.2% underwent histopathology (36/304) | Atlanta pediatric cohort | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Tissue diagnosis used in a minority (amin2022catscratchdisease pages 2-3) |
| Histopathology | 38.2% necrotizing granulomatous inflammation (13/34) | Atlanta pediatric cohort with pathology result available | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Most common biopsy pattern reported (amin2022catscratchdisease pages 2-3) |
| Histopathology | 8.8% Warthin–Starry positive (3/34) | Atlanta pediatric cohort with pathology result available | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Silver stain positivity was uncommon (amin2022catscratchdisease pages 2-3) |
| Diagnostics | 4.3% had PCR performed (13/304) | Atlanta pediatric cohort | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | PCR used infrequently (amin2022catscratchdisease pages 2-3) |
| Diagnostics | 3 PCR-positive lymph nodes | Atlanta pediatric cohort | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Low absolute PCR yield in this cohort (amin2022catscratchdisease pages 2-3, amin2022catscratchdisease pages 3-4) |
| Imaging | 71.1% had ≥1 radiologic study (216/304) | Atlanta pediatric cohort | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Extensive imaging use in tertiary setting (amin2022catscratchdisease pages 3-4, amin2022catscratchdisease media 65029abb) |
| Imaging | 36.4% splenomegaly (20/55) | Atlanta pediatric cohort with abdominal imaging | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Among those imaged abdominally (amin2022catscratchdisease pages 1-2, amin2022catscratchdisease pages 3-4) |
| Imaging | 38.1% splenic and/or hepatic microabscesses (21/55) | Atlanta pediatric cohort with abdominal imaging | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Important marker of hepatosplenic disease (amin2022catscratchdisease pages 1-2, amin2022catscratchdisease pages 3-4) |
| Imaging | 9.1% abdominal lymphadenopathy (5/55) | Atlanta pediatric cohort with abdominal imaging | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Less common abdominal imaging finding (amin2022catscratchdisease pages 3-4) |
| Imaging | 17.2% encephalitis-like findings (5/29) | Atlanta pediatric cohort with neuroimaging | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | CNS involvement on imaging (amin2022catscratchdisease pages 3-4) |
| Imaging | 27.6% optic neuritis (8/29) | Atlanta pediatric cohort with neuroimaging | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Neuro-ophthalmic manifestation on MRI/neuroimaging (amin2022catscratchdisease pages 3-4, amin2022catscratchdisease media 65029abb) |
| Imaging | 35.0% bone MRI involvement (7/20) | Atlanta pediatric cohort with bone MRI | Amin 2022, *Open Forum Infectious Diseases* | https://doi.org/10.1093/ofid/ofac426 | Suggestive of osteomyelitis/bone disease subset (amin2022catscratchdisease pages 3-4) |


*Table: This table compiles explicit quantitative epidemiology and clinical statistics for cat-scratch disease from the retrieved literature, with emphasis on U.S. burden estimates and the Atlanta pediatric cohort. It is useful as a structured evidence summary for knowledge-base population and citation tracking.*

Key recent/usable estimates from retrieved sources include:
- US outpatient diagnosis rates **4.5–9.3 per 100,000** and hospitalization **0.19–0.86 per 100,000** (sulaiman2023catscratchdisease pages 4-7).
- Pediatric incidence peak cited at **9.4 per 100,000** among US children age 5–9 years (amin2022catscratchdisease pages 1-2).
- Seasonality in a large Atlanta pediatric cohort showed peaks in August–November, with September highest (**15.5%** of diagnoses). (amin2022catscratchdisease pages 2-3, amin2022catscratchdisease media 65029abb)

### 9.2 Demographics
- In Atlanta pediatric cohort: median age 8.1 years (IQR 5.4–12.1) and 51.3% female. (amin2022catscratchdisease pages 1-2)

### 9.3 Genetic inheritance
Not applicable (infectious disease). No inherited transmission pattern.

---

## 10. Diagnostics
A structured diagnostics summary including cutoffs and performance notes is provided in **artifact-02**.

| Section | Test / Clinical scenario | Specimen / setting | Positivity criteria / regimen | Performance / evidence notes | MAXO suggestion | Key citations / URLs |
|---|---|---|---|---|---|---|
| Diagnostics | Serology (IFA / ELISA) | Serum | In the Atlanta pediatric cohort, seropositivity was defined as **IgM >1:20** and **IgG ≥1:128**; another clinical source notes **IFA/EIA >1:64** as positive, and a **fourfold rise** in paired sera as definitive | Mainstay diagnostic approach because culture is difficult; in the Atlanta cohort, **IgM ≥1:20 in 63.2% (110/174)** and **IgG ≥1:128 in 95.5% (169/177)**; ELISA/IFA described as the “best initial test” in review literature (amin2022catscratchdisease pages 1-2, amin2022catscratchdisease pages 2-3, nguyen2024threemonthhistoryof pages 4-6, puspitasari2025uncoveringthetruth pages 6-7) | MAXO:0000014 serological test | Amin 2022 https://doi.org/10.1093/ofid/ofac426; Nguyen 2024 https://doi.org/10.7759/cureus.66134; Puspitasari 2025 https://doi.org/10.5455/ovj.2025.v15.i5.5 (amin2022catscratchdisease pages 1-2, amin2022catscratchdisease pages 2-3, nguyen2024threemonthhistoryof pages 4-6, puspitasari2025uncoveringthetruth pages 6-7) |
| Diagnostics | Serology examples from individual cases | Serum | Reported high titers include **IgM >1:20, IgG 1:4096** and **IgG >1:1024, IgM 1:640** | Illustrates that markedly elevated titers may support diagnosis even when PCR is negative; useful in atypical or malignancy-mimicking presentations (sulaiman2023catscratchdisease pages 4-7, smith2024catscratchdiseasemimicking pages 3-5) | MAXO:0000014 serological test | Sulaiman 2023 https://doi.org/10.7759/cureus.44280; Smith 2024 https://doi.org/10.7759/cureus.66840 (sulaiman2023catscratchdisease pages 4-7, smith2024catscratchdiseasemimicking pages 3-5) |
| Diagnostics | PCR | Lymph node tissue; blood/tissue in selected cases | No universal cutoff reported in retrieved evidence; positivity is pathogen DNA detection | Lymph node PCR sensitivity reported as **30–60%**, increasing to **~87% when combined with histology and serology**; in the Atlanta cohort, PCR was used in **4.3% (13/304)** and only **3 lymph nodes** were PCR-positive; PCR described as **lower sensitivity but very high specificity** than serology (sulaiman2023catscratchdisease pages 4-7, amin2022catscratchdisease pages 2-3, puspitasari2025uncoveringthetruth pages 6-7) | MAXO:0000127 polymerase chain reaction assay | Sulaiman 2023 https://doi.org/10.7759/cureus.44280; Amin 2022 https://doi.org/10.1093/ofid/ofac426; Puspitasari 2025 https://doi.org/10.5455/ovj.2025.v15.i5.5 (sulaiman2023catscratchdisease pages 4-7, amin2022catscratchdisease pages 2-3, puspitasari2025uncoveringthetruth pages 6-7) |
| Diagnostics | Histopathology | Lymph node biopsy / aspirate | Characteristic features: **stellate granulomas with central necrosis**, **neutrophilic infiltration**, **palisading histiocytes**; other reports describe **granulomatous inflammation with multiple microabscesses** | Helpful when diagnosis is uncertain or malignancy must be excluded; in the Atlanta cohort, histopathology was done in **11.2% (36/304)**, with **necrotizing granulomatous inflammation in 38.2% (13/34)** and **Warthin–Starry positive in 8.8% (3/34)**; Warthin–Starry may show bacilli but a negative stain does not exclude CSD (sulaiman2023catscratchdisease pages 4-7, nguyen2024threemonthhistoryof pages 4-6, puspitasari2025uncoveringthetruth pages 5-6, amin2022catscratchdisease pages 2-3) | MAXO:0000373 biopsy of lymph node | Sulaiman 2023 https://doi.org/10.7759/cureus.44280; Nguyen 2024 https://doi.org/10.7759/cureus.66134; Puspitasari 2025 https://doi.org/10.5455/ovj.2025.v15.i5.5; Amin 2022 https://doi.org/10.1093/ofid/ofac426 (sulaiman2023catscratchdisease pages 4-7, nguyen2024threemonthhistoryof pages 4-6, puspitasari2025uncoveringthetruth pages 5-6, amin2022catscratchdisease pages 2-3) |
| Diagnostics | mNGS | Blood, tissue biopsy, drainage fluid; aqueous humor in ocular disease | Positive when **B. henselae sequence reads** are identified; ocular case reported **521 reads** in aqueous humor | Valuable for atypical disease and when history/serology are equivocal; in the pediatric mNGS-confirmed series, **B. henselae was detected in all 20 specimens**; review notes blood culture sensitivity around **~20%**, supporting molecular testing (lai2026clinicalandepidemiological pages 1-2, lai2026clinicalandepidemiological pages 3-4) | MAXO:0000140 metagenomic sequencing assay | Li 2024 https://doi.org/10.1186/s12348-024-00387-0; Lai 2026 https://doi.org/10.3389/fpubh.2025.1743423 (lai2026clinicalandepidemiological pages 1-2, lai2026clinicalandepidemiological pages 3-4) |
| Treatment | Typical lymphadenitis / uncomplicated regional CSD | Immunocompetent patient with localized disease | **Azithromycin 10 mg/kg on day 1, then 5 mg/kg on days 2–5** | Most uncomplicated disease is self-limited; antibiotics are often not required, but azithromycin is the best-supported short regimen for reducing node size/pain; review/case sources cite this as standard for typical disease (sulaiman2023catscratchdisease pages 4-7, puspitasari2025uncoveringthetruth pages 6-7, rolain2004recommendationsfortreatment pages 6-7) | MAXO:0001298 azithromycin therapy | Sulaiman 2023 https://doi.org/10.7759/cureus.44280; Puspitasari 2025 https://doi.org/10.5455/ovj.2025.v15.i5.5; Rolain 2004 https://doi.org/10.1128/AAC.48.6.1921-1933.2004 (sulaiman2023catscratchdisease pages 4-7, puspitasari2025uncoveringthetruth pages 6-7, rolain2004recommendationsfortreatment pages 6-7) |
| Treatment | Observation / supportive care for uncomplicated disease | Immunocompetent patient with mild-to-moderate lymphadenitis | No antibiotic regimen | Multiple sources state disease is usually **self-limited**, often resolving over **weeks to months**; one report notes typical CSD resolves in **2–6 months**, and another that lymphadenopathy commonly lasts **2–3 months** (sulaiman2023catscratchdisease pages 4-7, rolain2004recommendationsfortreatment pages 6-7, nguyen2024threemonthhistoryof pages 4-6, puspitasari2025uncoveringthetruth pages 5-6) | MAXO:0000011 clinical observation | Sulaiman 2023 https://doi.org/10.7759/cureus.44280; Rolain 2004 https://doi.org/10.1128/AAC.48.6.1921-1933.2004; Nguyen 2024 https://doi.org/10.7759/cureus.66134; Puspitasari 2025 https://doi.org/10.5455/ovj.2025.v15.i5.5 (sulaiman2023catscratchdisease pages 4-7, rolain2004recommendationsfortreatment pages 6-7, nguyen2024threemonthhistoryof pages 4-6, puspitasari2025uncoveringthetruth pages 5-6) |
| Treatment | Suppurative / painful lymph node | Suppurated node, painful adenitis | Needle aspiration for decompression; surgical management in selected persistent cases | Needle aspiration may relieve pain within **24–48 h**; persistent/worsening nodes may need biopsy or excision to exclude malignancy; intranodal gentamicin and surgery have been reported in the literature, but evidence is limited (rolain2004recommendationsfortreatment pages 6-7, sulaiman2023catscratchdisease pages 4-7) | NCIT:C15986 needle aspiration; MAXO:0001175 surgical excision | Rolain 2004 https://doi.org/10.1128/AAC.48.6.1921-1933.2004; Sulaiman 2023 https://doi.org/10.7759/cureus.44280 (rolain2004recommendationsfortreatment pages 6-7, sulaiman2023catscratchdisease pages 4-7) |
| Treatment | Hepatosplenic / systemic disease | Disseminated disease, prolonged fever, organ involvement | Pediatric mNGS series used **azithromycin alone (1/20)**, **azithromycin + rifampicin (8/20)**, **doxycycline alone (1/20)**, **doxycycline + rifampicin (10/20)** | In the 20-case pediatric series, **all improved and were discharged**, though one child with hepatic/renal involvement had progression on CT at ~1 month; systemic disease often prompts combination therapy despite limited trial evidence (lai2026clinicalandepidemiological pages 3-4) | MAXO:0001298 azithromycin therapy; MAXO:0000574 doxycycline therapy; MAXO:0000096 rifampicin therapy | Lai 2026 https://doi.org/10.3389/fpubh.2025.1743423 (lai2026clinicalandepidemiological pages 3-4) |
| Treatment | Ocular disease / neuroretinitis / CNS involvement | Neuroretinitis, optic neuritis, encephalopathy/CNS disease | **Doxycycline 100 mg twice daily + rifampin 300 mg twice daily** is the classic recommended adult combination for ocular/CNS Bartonella disease | Frequently used for complicated ocular/CNS disease because of tissue penetration; case reports describe good visual recovery after doxycycline + rifampin; Rolain recommends this combination for CNS involvement (rolain2004recommendationsfortreatment pages 6-7, lai2026clinicalandepidemiological pages 1-2, smith2024catscratchdiseasemimicking pages 3-5) | MAXO:0000574 doxycycline therapy; MAXO:0000096 rifampicin therapy | Rolain 2004 https://doi.org/10.1128/AAC.48.6.1921-1933.2004; Li 2024 https://doi.org/10.1186/s12348-024-00387-0; Avaylon 2023 https://doi.org/10.7759/cureus.45866 (via retrieved paper list); Smith 2024 https://doi.org/10.7759/cureus.66840 (rolain2004recommendationsfortreatment pages 6-7, lai2026clinicalandepidemiological pages 1-2, smith2024catscratchdiseasemimicking pages 3-5) |
| Treatment | Ocular disease with inflammatory involvement | Uveitis / neuroretinitis with optic disc inflammation | Systemic antibiotics plus corticosteroids used in ocular series; one pediatric case received **doxycycline + methylprednisolone** for **6 months** with improvement | Ocular case series reported improvement in visual acuity and lesions with systemic antibiotics; corticosteroids are often reserved for marked optic nerve or inflammatory involvement and should accompany antimicrobial treatment (lai2026clinicalandepidemiological pages 1-2) | MAXO:0000574 doxycycline therapy; MAXO:0000016 corticosteroid therapy | Hong 2023 https://doi.org/10.1186/s12886-023-03063-4; Acar 2023 https://doi.org/10.4274/tjo.galenos.2022.44692 (lai2026clinicalandepidemiological pages 1-2) |
| Treatment | Immunocompromised disease / bacillary angiomatosis | HIV/immunosuppression, disseminated Bartonella | **Doxycycline or erythromycin for 10 days to 2 months** cited in case-review literature | Complicated and immunocompromised disease is more likely to require prolonged therapy; evidence is largely case-based and expert review rather than trials (sulaiman2023catscratchdisease pages 4-7, puspitasari2025uncoveringthetruth pages 6-7) | MAXO:0000574 doxycycline therapy; MAXO:0000100 erythromycin therapy | Sulaiman 2023 https://doi.org/10.7759/cureus.44280; Puspitasari 2025 https://doi.org/10.5455/ovj.2025.v15.i5.5 (sulaiman2023catscratchdisease pages 4-7, puspitasari2025uncoveringthetruth pages 6-7) |
| Treatment | Alternative antibiotics reported in retrospective literature | Selected systemic or refractory cases | Retrospective effectiveness rates reported for **rifampin 87%**, **ciprofloxacin 84%**, **gentamicin 73%**, **TMP-SMX 58%** | These data come from non-randomized retrospective literature and should be interpreted cautiously; they are useful mainly when standard regimens cannot be used or in refractory disease (nguyen2024threemonthhistoryof pages 4-6) | MAXO:0000096 rifampicin therapy; MAXO:0000085 ciprofloxacin therapy; MAXO:0000111 gentamicin therapy; MAXO:0000154 trimethoprim-sulfamethoxazole therapy | Nguyen 2024 https://doi.org/10.7759/cureus.66134 (nguyen2024threemonthhistoryof pages 4-6) |


*Table: This table summarizes the main diagnostic modalities and treatment approaches for cat-scratch disease, including practical cutoff values, performance notes, commonly used regimens, and ontology-ready MAXO action suggestions. It is useful for translating the literature into a structured disease knowledge-base entry.*

### 10.1 Common diagnostic approaches (current practice)
- **Serology (IFA/ELISA):** commonly first-line; in the Atlanta cohort, IFA positivity thresholds were IgM >1:20 and IgG ≥1:128. (amin2022catscratchdisease pages 1-2, puspitasari2025uncoveringthetruth pages 6-7)
- **Histopathology:** used in selected cases (e.g., malignancy work-up or persistent/suppurative nodes) with necrotizing granulomatous inflammation patterns. (amin2022catscratchdisease pages 2-3, sulaiman2023catscratchdisease pages 4-7)
- **PCR:** useful but imperfect sensitivity; reported lymph node PCR sensitivity 30–60% in a case-based review, improving with multimodal evidence. (sulaiman2023catscratchdisease pages 4-7)
- **mNGS:** increasingly used for atypical disease or unusual specimens (e.g., aqueous humor); an ocular case reported 521 *B. henselae* reads in aqueous humor (lai2026clinicalandepidemiological pages 1-2), and a pediatric series detected *B. henselae* in all 20 mNGS-tested specimens (lai2026clinicalandepidemiological pages 3-4).

### 10.2 Differential diagnosis (high-yield)
CSD can mimic neoplastic causes of lymphadenopathy (e.g., lymphoma) and granulomatous infections (e.g., tuberculosis), motivating biopsy and/or molecular testing in atypical presentations. (smith2024catscratchdiseasemimicking pages 3-5, lai2026clinicalandepidemiological pages 3-4)

---

## 11. Outcome / prognosis
- **Typical/uncomplicated disease:** generally favorable and self-limited over weeks to months, often without antibiotics. (sulaiman2023catscratchdisease pages 4-7, rolain2004recommendationsfortreatment pages 6-7, puspitasari2025uncoveringthetruth pages 5-6)
- **Atypical/disseminated disease:** can involve hepatosplenic, ocular, bone, or neurologic manifestations; outcomes are usually good with appropriate recognition and management in contemporary cohorts/case series, but can be severe in immunocompromised hosts. (amin2022catscratchdisease pages 3-4, smith2024catscratchdiseasemimicking pages 3-5)
- **Real-world pediatric cohort finding:** in the Atlanta cohort, ~20% received no antibiotics and retrospective analyses found no significant outcome differences between treated and untreated groups (interpretation limited by confounding by indication). (amin2022catscratchdisease pages 4-6)

---

## 12. Treatment
Treatment and MAXO action suggestions are summarized in **artifact-02**.

### 12.1 Uncomplicated lymphadenitis
- Many cases are self-limited (rolain2004recommendationsfortreatment pages 6-7, puspitasari2025uncoveringthetruth pages 5-6).
- A commonly cited regimen for severe lymphadenopathy is azithromycin **10 mg/kg day 1 then 5 mg/kg days 2–5**. (puspitasari2025uncoveringthetruth pages 6-7)

### 12.2 Complicated disease (ocular/CNS; disseminated)
- For ocular or CNS involvement, expert recommendations include **doxycycline 100 mg twice daily + rifampin 300 mg twice daily**. (rolain2004recommendationsfortreatment pages 6-7)
- Contemporary practice patterns in an mNGS-confirmed pediatric series included combinations such as azithromycin + rifampicin and doxycycline + rifampicin, with all hospitalized children improving and being discharged. (lai2026clinicalandepidemiological pages 3-4)

### 12.3 Evidence quality note (expert analysis)
The treatment literature remains heterogeneous; classic expert recommendations note limited antibiotic benefit in typical lymphadenitis, while complicated disease is often treated with combination regimens based on pathophysiology (intracellular niches) and case-series experience rather than high-quality randomized trials. (rolain2004recommendationsfortreatment pages 6-7, nguyen2024threemonthhistoryof pages 4-6)

---

## 13. Prevention
Primary prevention is focused on interrupting zoonotic transmission:
- **Flea control on cats** and **avoiding scratches/bites/licks that break skin** are consistently recommended. (puspitasari2025uncoveringthetruth pages 6-7, puspitasari2025uncoveringthetruth pages 5-6, nemade2023catscratchdisease pages 1-3)
- Human-to-human transmission has **not been documented**, supporting zoonotic prevention emphasis. (puspitasari2025uncoveringthetruth pages 2-3)

---

## 14. Other species / natural disease (One Health)
### 14.1 Reservoirs and vectors
- **Primary reservoir:** domestic cats (especially kittens); cats frequently have asymptomatic bacteremia and can remain bacteremic for prolonged periods (weeks to years). (puspitasari2025uncoveringthetruth pages 2-3, nemade2023catscratchdisease pages 3-6)
- **Vector maintaining infection among cats:** cat flea *Ctenocephalides felis*. (puspitasari2025uncoveringthetruth pages 2-3, puspitasari2025uncoveringthetruth pages 5-6)

### 14.2 Zoonotic transmission routes
- Infection is typically acquired via scratches/bites, including contamination with flea feces and/or cat oral flora (bites/licks that breach skin). (nemade2023catscratchdisease pages 3-6, puspitasari2025uncoveringthetruth pages 5-6)
- Human-to-human transmission is not documented. (puspitasari2025uncoveringthetruth pages 2-3)

### 14.3 Other species relevance
Reviews note broader *Bartonella* host ranges and occasional discussion of dogs/other mammals/ticks in the ecology of bartonellosis, though CSD in humans remains most strongly associated with feline exposure. (puspitasari2025uncoveringthetruth pages 2-3, puspitasari2025uncoveringthetruth pages 5-6)

---

## 15. Model organisms and experimental systems
### 15.1 In vitro models
- **Human umbilical vein endothelial cells (HUVECs)** are used to quantify strain-level differences in vasoproliferative traits and to study endothelial interactions relevant to angiogenic pathology. (kondo2025differentialvasoproliferativetraits pages 1-2)

### 15.2 Natural-host / in vivo models
- Experimental inoculation studies in cats (natural reservoir) are discussed in review literature, typically showing asymptomatic or mild/transient signs, supporting cats as a reservoir model relevant to One Health. (puspitasari2025uncoveringthetruth pages 5-6)

---

## Visual evidence from a key cohort paper
The Atlanta pediatric cohort paper includes figures/tables summarizing month-by-month seasonality and radiologic findings; these were retrieved as images and support the quantitative seasonality and multi-organ involvement described above. (amin2022catscratchdisease media 65029abb, amin2022catscratchdisease media 4aebcb1f, amin2022catscratchdisease media 79399fa7, amin2022catscratchdisease media 3ce93ca4)

---

## Recent developments (2023–2024 emphasis)
1) **Expanded molecular diagnostics for atypical disease:** mNGS has been used to confirm ocular bartonellosis from intraocular fluid (aqueous humor), enabling diagnosis even when classic history or serology is limited. (Li et al., 2024-04; https://doi.org/10.1186/s12348-024-00387-0) (lai2026clinicalandepidemiological pages 1-2)  
2) **Mechanistic consolidation of immune-evasion/persistence:** 2024 mechanistic review emphasizes intracellular vacuoles resisting lysosomal fusion, erythrocyte sanctuaries, immune modulation (IL-10), and biofilm-mediated persistence—concepts that explain culture-negativity and chronic/recurrent manifestations. (Xi et al., 2024-03; https://doi.org/10.1080/21505594.2024.2322961) (xi2024sneakytacticsingenious pages 5-6, xi2024sneakytacticsingenious pages 2-4, xi2024sneakytacticsingenious pages 6-7)  
3) **Broadened neurologic phenotype framing (“neurobartonelloses”):** 2024 review highlights the breadth of reported neurologic syndromes and plausible vascular/immune mechanisms (VEGF-driven remodeling, intracellular niches, macrophage shuttling). (Bush et al., 2024-10; https://doi.org/10.1186/s13071-024-06491-3) (bush2024neurobartonellosesemergingfrom pages 28-29)

---

## Limitations of this report (evidence gaps in retrieved corpus)
- **Ontology identifiers (MONDO/MeSH/ICD-10/ICD-11/Orphanet/OMIM)** were not directly available in the retrieved full-text set, so they are not populated here.
- **Human genetic susceptibility** evidence (GWAS/ClinVar/ClinGen) was not identified in the retrieved set.
- Some frequently cited classic RCTs (e.g., 1998 azithromycin trial) were not obtainable as full text in this run; key regimen details were nonetheless captured via other authoritative sources in-corpus. (rolain2004recommendationsfortreatment pages 6-7, puspitasari2025uncoveringthetruth pages 6-7)


References

1. (puspitasari2025uncoveringthetruth pages 1-2): Yulianna Puspitasari, Aswin Khairullah, Hartanto Raharjo, Ima Fauziah, Wiwiek Tyasningsih, Dea Kurniasih, Muhammad Kusala, Ikechukwu Moses, Bantari Wardhani, Kartika Fauzia, Katty Riwu, Riza Ahmad, Sheila Yanestria, Syahputra Wibowo, Arif Ansori, and Ilma ruf. Uncovering the truth about cat-scratch disease. Open Veterinary Journal, 15:1895-1906, May 2025. URL: https://doi.org/10.5455/ovj.2025.v15.i5.5, doi:10.5455/ovj.2025.v15.i5.5. This article has 6 citations.

2. (smith2024catscratchdiseasemimicking pages 3-5): E Smith, R Lawless, A Hoellein, and RR Lawless. Cat-scratch disease mimicking neoplastic etiology in a complex clinical presentation: a case report. Cureus, Aug 2024. URL: https://doi.org/10.7759/cureus.66840, doi:10.7759/cureus.66840. This article has 1 citations.

3. (amin2022catscratchdisease pages 1-2): Omayma Amin, Christina A Rostad, Mark Gonzalez, Bradley S Rostad, Shelley Caltharp, Elizabeth Quincer, Briana A Betke, Nicole L Gottdenker, Jonathan J Wilson, Andi L Shane, Mohnd Elmontser, Andres Camacho-Gonzalez, Tal Senior, Oliver Smith, Evan J Anderson, and Inci Yildirim. Cat scratch disease: 9 years of experience at a pediatric center. Open Forum Infectious Diseases, Aug 2022. URL: https://doi.org/10.1093/ofid/ofac426, doi:10.1093/ofid/ofac426. This article has 33 citations and is from a peer-reviewed journal.

4. (amin2022catscratchdisease pages 2-3): Omayma Amin, Christina A Rostad, Mark Gonzalez, Bradley S Rostad, Shelley Caltharp, Elizabeth Quincer, Briana A Betke, Nicole L Gottdenker, Jonathan J Wilson, Andi L Shane, Mohnd Elmontser, Andres Camacho-Gonzalez, Tal Senior, Oliver Smith, Evan J Anderson, and Inci Yildirim. Cat scratch disease: 9 years of experience at a pediatric center. Open Forum Infectious Diseases, Aug 2022. URL: https://doi.org/10.1093/ofid/ofac426, doi:10.1093/ofid/ofac426. This article has 33 citations and is from a peer-reviewed journal.

5. (sulaiman2023catscratchdisease pages 4-7): Zoheb I Sulaiman, Hasan Samra, and Gina Askar. Cat scratch disease: an unusual case of right inguinal lymphadenitis due to bartonella henselae. Cureus, Aug 2023. URL: https://doi.org/10.7759/cureus.44280, doi:10.7759/cureus.44280. This article has 5 citations.

6. (rolain2004recommendationsfortreatment pages 6-7): J. M. Rolain, P. Brouqui, J. E. Koehler, C. Maguina, M. J. Dolan, and D. Raoult. Recommendations for treatment of human infections caused by bartonella species. Antimicrobial Agents and Chemotherapy, 48:1921-1933, Jun 2004. URL: https://doi.org/10.1128/aac.48.6.1921-1933.2004, doi:10.1128/aac.48.6.1921-1933.2004. This article has 718 citations and is from a highest quality peer-reviewed journal.

7. (lai2026clinicalandepidemiological pages 1-2): Shu-yu Lai, Li Chang, Jia-xin Duan, Guang-lu Che, Qiu-xia Yang, Jie Teng, Hui Jian, Xiao-juan Liu, and Fang Liu. Clinical and epidemiological characteristics of cat scratch disease in children from southwestern china: a retrospective analysis of mngs-confirmed cases. Frontiers in Public Health, Jan 2026. URL: https://doi.org/10.3389/fpubh.2025.1743423, doi:10.3389/fpubh.2025.1743423. This article has 0 citations.

8. (bush2024neurobartonellosesemergingfrom pages 28-29): Janice C. Bush, Cynthia Robveille, Ricardo G. Maggi, and Edward B. Breitschwerdt. Neurobartonelloses: emerging from obscurity! Parasites & Vectors, Oct 2024. URL: https://doi.org/10.1186/s13071-024-06491-3, doi:10.1186/s13071-024-06491-3. This article has 25 citations and is from a peer-reviewed journal.

9. (amin2022catscratchdisease pages 3-4): Omayma Amin, Christina A Rostad, Mark Gonzalez, Bradley S Rostad, Shelley Caltharp, Elizabeth Quincer, Briana A Betke, Nicole L Gottdenker, Jonathan J Wilson, Andi L Shane, Mohnd Elmontser, Andres Camacho-Gonzalez, Tal Senior, Oliver Smith, Evan J Anderson, and Inci Yildirim. Cat scratch disease: 9 years of experience at a pediatric center. Open Forum Infectious Diseases, Aug 2022. URL: https://doi.org/10.1093/ofid/ofac426, doi:10.1093/ofid/ofac426. This article has 33 citations and is from a peer-reviewed journal.

10. (xi2024sneakytacticsingenious pages 5-6): Yixuan Xi, Xinru Li, Lu Liu, Feichen Xiu, Xinchao Yi, Hongliang Chen, and Xiaoxing You. Sneaky tactics: ingenious immune evasion mechanisms of bartonella. Virulence, Mar 2024. URL: https://doi.org/10.1080/21505594.2024.2322961, doi:10.1080/21505594.2024.2322961. This article has 20 citations and is from a peer-reviewed journal.

11. (xi2024sneakytacticsingenious pages 2-4): Yixuan Xi, Xinru Li, Lu Liu, Feichen Xiu, Xinchao Yi, Hongliang Chen, and Xiaoxing You. Sneaky tactics: ingenious immune evasion mechanisms of bartonella. Virulence, Mar 2024. URL: https://doi.org/10.1080/21505594.2024.2322961, doi:10.1080/21505594.2024.2322961. This article has 20 citations and is from a peer-reviewed journal.

12. (xi2024sneakytacticsingenious pages 6-7): Yixuan Xi, Xinru Li, Lu Liu, Feichen Xiu, Xinchao Yi, Hongliang Chen, and Xiaoxing You. Sneaky tactics: ingenious immune evasion mechanisms of bartonella. Virulence, Mar 2024. URL: https://doi.org/10.1080/21505594.2024.2322961, doi:10.1080/21505594.2024.2322961. This article has 20 citations and is from a peer-reviewed journal.

13. (puspitasari2025uncoveringthetruth pages 2-3): Yulianna Puspitasari, Aswin Khairullah, Hartanto Raharjo, Ima Fauziah, Wiwiek Tyasningsih, Dea Kurniasih, Muhammad Kusala, Ikechukwu Moses, Bantari Wardhani, Kartika Fauzia, Katty Riwu, Riza Ahmad, Sheila Yanestria, Syahputra Wibowo, Arif Ansori, and Ilma ruf. Uncovering the truth about cat-scratch disease. Open Veterinary Journal, 15:1895-1906, May 2025. URL: https://doi.org/10.5455/ovj.2025.v15.i5.5, doi:10.5455/ovj.2025.v15.i5.5. This article has 6 citations.

14. (puspitasari2025uncoveringthetruth pages 5-6): Yulianna Puspitasari, Aswin Khairullah, Hartanto Raharjo, Ima Fauziah, Wiwiek Tyasningsih, Dea Kurniasih, Muhammad Kusala, Ikechukwu Moses, Bantari Wardhani, Kartika Fauzia, Katty Riwu, Riza Ahmad, Sheila Yanestria, Syahputra Wibowo, Arif Ansori, and Ilma ruf. Uncovering the truth about cat-scratch disease. Open Veterinary Journal, 15:1895-1906, May 2025. URL: https://doi.org/10.5455/ovj.2025.v15.i5.5, doi:10.5455/ovj.2025.v15.i5.5. This article has 6 citations.

15. (puspitasari2025uncoveringthetruth pages 6-7): Yulianna Puspitasari, Aswin Khairullah, Hartanto Raharjo, Ima Fauziah, Wiwiek Tyasningsih, Dea Kurniasih, Muhammad Kusala, Ikechukwu Moses, Bantari Wardhani, Kartika Fauzia, Katty Riwu, Riza Ahmad, Sheila Yanestria, Syahputra Wibowo, Arif Ansori, and Ilma ruf. Uncovering the truth about cat-scratch disease. Open Veterinary Journal, 15:1895-1906, May 2025. URL: https://doi.org/10.5455/ovj.2025.v15.i5.5, doi:10.5455/ovj.2025.v15.i5.5. This article has 6 citations.

16. (nguyen2024threemonthhistoryof pages 4-6): Martin Nguyen, Sheraj Singh, Bevan Sam, Richard Llerena, Abigail Frank, and Marinella Mabalot. Three-month history of lymphadenopathy caused by bartonella henselae in a 13-year-old following a dog scratch. Cureus, Aug 2024. URL: https://doi.org/10.7759/cureus.66134, doi:10.7759/cureus.66134. This article has 1 citations.

17. (gadila2025comparisonoftranscriptomic pages 1-2): Shiva Kumar Goud Gadila, John R. Caskey, Edward B. Breitschwerdt, Ricardo G. Maggi, and Monica E. Embers. Comparison of transcriptomic profiles between intracellular and extracellular bartonella henselae. Communications Biology, Jan 2025. URL: https://doi.org/10.1038/s42003-025-07535-9, doi:10.1038/s42003-025-07535-9. This article has 2 citations and is from a peer-reviewed journal.

18. (kondo2025differentialvasoproliferativetraits pages 1-2): Yuka Kondo, Masahiro Suzuki, Shingo Sato, Soichi Maruyama, Akiko Sei, Xingyan Ma, Kota Nakano, Yohei Doi, and Kentaro Tsukamoto. Differential vasoproliferative traits of <i>bartonella henselae</i> strains associated with autotransporter bafa variants. Microbiology Spectrum, Jan 2025. URL: https://doi.org/10.1128/spectrum.01925-24, doi:10.1128/spectrum.01925-24. This article has 1 citations and is from a domain leading peer-reviewed journal.

19. (amin2022catscratchdisease pages 4-6): Omayma Amin, Christina A Rostad, Mark Gonzalez, Bradley S Rostad, Shelley Caltharp, Elizabeth Quincer, Briana A Betke, Nicole L Gottdenker, Jonathan J Wilson, Andi L Shane, Mohnd Elmontser, Andres Camacho-Gonzalez, Tal Senior, Oliver Smith, Evan J Anderson, and Inci Yildirim. Cat scratch disease: 9 years of experience at a pediatric center. Open Forum Infectious Diseases, Aug 2022. URL: https://doi.org/10.1093/ofid/ofac426, doi:10.1093/ofid/ofac426. This article has 33 citations and is from a peer-reviewed journal.

20. (amin2022catscratchdisease media 65029abb): Omayma Amin, Christina A Rostad, Mark Gonzalez, Bradley S Rostad, Shelley Caltharp, Elizabeth Quincer, Briana A Betke, Nicole L Gottdenker, Jonathan J Wilson, Andi L Shane, Mohnd Elmontser, Andres Camacho-Gonzalez, Tal Senior, Oliver Smith, Evan J Anderson, and Inci Yildirim. Cat scratch disease: 9 years of experience at a pediatric center. Open Forum Infectious Diseases, Aug 2022. URL: https://doi.org/10.1093/ofid/ofac426, doi:10.1093/ofid/ofac426. This article has 33 citations and is from a peer-reviewed journal.

21. (lai2026clinicalandepidemiological pages 3-4): Shu-yu Lai, Li Chang, Jia-xin Duan, Guang-lu Che, Qiu-xia Yang, Jie Teng, Hui Jian, Xiao-juan Liu, and Fang Liu. Clinical and epidemiological characteristics of cat scratch disease in children from southwestern china: a retrospective analysis of mngs-confirmed cases. Frontiers in Public Health, Jan 2026. URL: https://doi.org/10.3389/fpubh.2025.1743423, doi:10.3389/fpubh.2025.1743423. This article has 0 citations.

22. (nemade2023catscratchdisease pages 1-3): Sanjana Vijay Nemade and Kiran Jaywant Shinde. Cat scratch disease. Granulomatous diseases in Otorhinolaryngology, Head and Neck, pages 79-85, Jan 2023. URL: https://doi.org/10.1007/978-981-16-4047-6\_9, doi:10.1007/978-981-16-4047-6\_9. This article has 0 citations.

23. (nemade2023catscratchdisease pages 3-6): Sanjana Vijay Nemade and Kiran Jaywant Shinde. Cat scratch disease. Granulomatous diseases in Otorhinolaryngology, Head and Neck, pages 79-85, Jan 2023. URL: https://doi.org/10.1007/978-981-16-4047-6\_9, doi:10.1007/978-981-16-4047-6\_9. This article has 0 citations.

24. (amin2022catscratchdisease media 4aebcb1f): Omayma Amin, Christina A Rostad, Mark Gonzalez, Bradley S Rostad, Shelley Caltharp, Elizabeth Quincer, Briana A Betke, Nicole L Gottdenker, Jonathan J Wilson, Andi L Shane, Mohnd Elmontser, Andres Camacho-Gonzalez, Tal Senior, Oliver Smith, Evan J Anderson, and Inci Yildirim. Cat scratch disease: 9 years of experience at a pediatric center. Open Forum Infectious Diseases, Aug 2022. URL: https://doi.org/10.1093/ofid/ofac426, doi:10.1093/ofid/ofac426. This article has 33 citations and is from a peer-reviewed journal.

25. (amin2022catscratchdisease media 79399fa7): Omayma Amin, Christina A Rostad, Mark Gonzalez, Bradley S Rostad, Shelley Caltharp, Elizabeth Quincer, Briana A Betke, Nicole L Gottdenker, Jonathan J Wilson, Andi L Shane, Mohnd Elmontser, Andres Camacho-Gonzalez, Tal Senior, Oliver Smith, Evan J Anderson, and Inci Yildirim. Cat scratch disease: 9 years of experience at a pediatric center. Open Forum Infectious Diseases, Aug 2022. URL: https://doi.org/10.1093/ofid/ofac426, doi:10.1093/ofid/ofac426. This article has 33 citations and is from a peer-reviewed journal.

26. (amin2022catscratchdisease media 3ce93ca4): Omayma Amin, Christina A Rostad, Mark Gonzalez, Bradley S Rostad, Shelley Caltharp, Elizabeth Quincer, Briana A Betke, Nicole L Gottdenker, Jonathan J Wilson, Andi L Shane, Mohnd Elmontser, Andres Camacho-Gonzalez, Tal Senior, Oliver Smith, Evan J Anderson, and Inci Yildirim. Cat scratch disease: 9 years of experience at a pediatric center. Open Forum Infectious Diseases, Aug 2022. URL: https://doi.org/10.1093/ofid/ofac426, doi:10.1093/ofid/ofac426. This article has 33 citations and is from a peer-reviewed journal.
