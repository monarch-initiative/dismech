---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-11T09:01:02.097980'
end_time: '2026-05-11T09:24:35.162671'
duration_seconds: 1413.06
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Vogt-Koyanagi-Harada Disease
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 47
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Vogt-Koyanagi-Harada Disease
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Vogt-Koyanagi-Harada Disease** covering all of the
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
- **Disease Name:** Vogt-Koyanagi-Harada Disease
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Vogt-Koyanagi-Harada Disease** covering all of the
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


# Vogt–Koyanagi–Harada (VKH) Disease — Comprehensive Disease Characteristics Report (Autoimmune)

## Target disease
- **Disease name:** Vogt–Koyanagi–Harada disease (VKH)
- **Category:** Autoimmune, multisystem inflammatory disease
- **MONDO ID:** **MONDO_0018092** (OpenTargets disease record) (OpenTargets Search: Vogt-Koyanagi-Harada disease)

## Executive summary
VKH is a T cell–driven autoimmune disorder targeting melanocyte-associated antigens in melanin-containing tissues (uvea/choroid, meninges, inner ear, skin/hair), presenting most prominently as bilateral granulomatous uveitis with characteristic choroidal inflammation and exudative retinal detachment, and variably neurologic/auditory and integumentary manifestations. Contemporary management emphasizes *early, aggressive systemic corticosteroids combined with early immunomodulatory therapy* to prevent progression to chronically evolving disease with “sunset glow fundus” and recurrent inflammation; biologics (e.g., anti‑TNF) and newer small molecules (e.g., JAK inhibitors) are increasingly used for refractory disease. (tugaltutkun2024vogtkoyanagiharadadisease pages 1-3, rahman2023immunosuppressivetherapyfor pages 1-2, vitale2024efficacyandsafety pages 1-2)

---

## 1. Disease information

### 1.1 Definition and current understanding
A recent 2024 editorial defines VKH as “a multisystemic autoimmune disorder that affects the eyes, central nervous system, the auditory system, and the integumentary system,” driven by an autoimmune reaction against melanocyte-associated antigens across these tissues. (Published online **2024‑04‑24**; URL: https://doi.org/10.1080/09273948.2024.2331401) (tugaltutkun2024vogtkoyanagiharadadisease pages 1-3)

A 2023 COVID-era review similarly describes VKH as “a rare multisystem inflammatory autoimmune disease affecting eyes, ears, brain, skin and hair,” and frames the core immunopathology as T‑cell mediated autoimmunity directed against choroidal melanocytes and melanocyte antigens (e.g., tyrosinase, TRP1/2, MART‑1, gp100). (Published **2023‑09**; URL: https://doi.org/10.3390/jcm12196242) (manni2023vogtkoyanagiharadadiseaseand pages 1-2)

### 1.2 Key identifiers
- **MONDO:** MONDO_0018092 (OpenTargets Search: Vogt-Koyanagi-Harada disease)
- **MeSH / ICD‑10 / ICD‑11 / Orphanet:** Not extractable from the retrieved full texts in this run; VKH is present as a MeSH term in ClinicalTrials.gov metadata for VKH-related studies (NCT05590416 chunk 2). 

### 1.3 Synonyms / alternative names
- Vogt–Koyanagi–Harada disease
- Vogt–Koyanagi–Harada syndrome
- Harada disease (often used in ophthalmology contexts)
(Use of “syndrome” is explicit in multiple sources) (tugaltutkun2024vogtkoyanagiharadadisease pages 1-3, vitale2024efficacyandsafety pages 1-2)

### 1.4 Evidence source type
This report is derived from **aggregated disease-level resources** (reviews/editorials, clinical trial registries) and **primary human studies** (genetic case–control, randomized trial, retrospective cohorts), plus **experimental model systems** (rodent and avian models). (zhou2023geneticassociationof pages 1-2, zhong2023arandomizednoninferiority pages 3-4, adamus2002experimentalautoimmuneuveitides pages 1-3, sorrick2022immuneactivitiesin pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors (mechanistic)
**Core concept:** VKH is an autoimmune response against melanocyte-associated antigens.

Human immunology evidence supports antigen-specific T cell reactivity: ocular-infiltrating and peripheral CD4+ T cells from VKH patients recognize melanocyte peptides (tyrosinase and gp100) in an HLA-DR4 (including HLA‑DRB1*0405) restricted manner and produce inflammatory mediators (e.g., IFN‑γ, RANTES). (sugita2006ocularinfiltratingcd4+ pages 1-2, sugita2006ocularinfiltratingcd4+ pages 7-8)

### 2.2 Risk factors

#### 2.2.1 Genetic risk factors
**HLA risk and immunogenetic predisposition**
- In immune checkpoint inhibitor–associated uveitis, VKH-like presentations were strongly associated with **HLA‑DRB1*04:05**: “Four patients with VKH-like uveitis underwent HLA genotyping and were all positive for HLA‑DRB1*04:05… Statistical analysis showed that HLA‑DRB1*04:05 was significantly associated with developing VKH-like ICIU (P = 0.029).” (Published **2023‑08**; URL: https://doi.org/10.1038/s41598-023-40565-z) (takeuchi2023hladrb1*0405isinvolved pages 1-2)

**Non-HLA susceptibility loci (recent primary human genetics, 2023)**
- In a large Chinese Han case–control study (**912 VKH**, **878 controls**), PRKCD and CARD9 polymorphisms were associated with VKH susceptibility. The abstract states: “We found that rs74437127 C allele of PRKCD… and C allele of CARD9 were associated with increased susceptibility of VKH… Functional studies… revealed that CC carriers had significantly higher CARD9 mRNA expression and tumour necrosis factor-α production…” (Published **2023‑02**; URL: https://doi.org/10.1186/s40246-023-00459-7) (zhou2023geneticassociationof pages 1-2)
  - **PRKCD rs74437127 C allele**: Pc=0.020, OR=1.624 (95% CI 1.200–2.199) (zhou2023geneticassociationof pages 1-2)
  - **CARD9 rs3812555 CC genotype**: Pc=2.04×10^-5, OR=1.810 (95% CI 1.418–2.311) (zhou2023geneticassociationof pages 1-2)
  - **Functional correlate:** rs3812555 CC carriers had higher CARD9 mRNA and higher TNF‑α production (P=1.00×10^-4; P=2.00×10^-3) (zhou2023geneticassociationof pages 1-2)

#### 2.2.2 Environmental / infectious / iatrogenic triggers
- Viral triggers and molecular mimicry are repeatedly proposed; in VKH, melanocyte antigen–specific T cells can show cross-reactivity with a CMV peptide, supporting a plausible mimicry mechanism. (sugita2006ocularinfiltratingcd4+ pages 7-8)

**SARS‑CoV‑2 infection and COVID‑19 vaccination (2023–2024 focus)**
- A 2023 review summarizes reported VKH onset/relapse after COVID‑19 infection/vaccination and notes VKH is “one of the most frequently reported uveitic entities after COVID‑19 vaccination,” while emphasizing good response to therapy. (Published **2023‑09**; URL: https://doi.org/10.3390/jcm12196242) (manni2023vogtkoyanagiharadadiseaseand pages 1-2)
- A focused 2023 case-series review of vaccine-associated VKH included **21 patients** and reported a mean onset interval of **7.5 days** (range 12 h to 4 weeks), frequent bilateral involvement (20/21), meningitis symptoms (16/21), and frequent serous retinal detachment (16/21) and choroidal thickening (14/21). (Published **2023‑06**; URL: https://doi.org/10.1080/21645515.2023.2220630) (manni2023vogtkoyanagiharadadiseaseand pages 2-4)
- A 2024 Japanese center study found higher clinic-based prevalence among new patients after the COVID-19 state-of-emergency declaration, but similar visual acuity and recurrence outcomes after pulse steroids. (Published **2024‑06**; URL: https://doi.org/10.1038/s41598-024-63957-1) (muto2024effectofthe pages 6-7)

**Immune checkpoint inhibitors (ICIs)**
- ICI-associated uveitis occurs in ~0.3–1% of ICI-treated patients, and VKH-like posterior/panuveitis can occur with choroidal thickening and serous subretinal fluid. (takeuchi2023hladrb1*0405isinvolved pages 1-2)

### 2.3 Protective factors
No specific genetic or environmental protective factors are established as clinical recommendations; however, specific alleles/genotypes in the PRKCD/CARD9 study were statistically associated with reduced susceptibility (e.g., PRKCD rs74437127 T allele OR=0.616; CARD9 rs3812555 T allele OR=0.589), which may be viewed as candidate protective associations rather than proven protective mechanisms. (zhou2023geneticassociationof pages 1-2)

### 2.4 Gene–environment interaction
The prevailing model is **genetic susceptibility (notably HLA-DR4-related)** plus an environmental/infectious/iatrogenic trigger (e.g., viral infection, vaccination, ICI-mediated immune disinhibition) leading to loss of tolerance to melanocyte antigens. This interaction is explicitly invoked in COVID-era synthesis and in ICI-associated VKH-like uveitis. (manni2023vogtkoyanagiharadadiseaseand pages 1-2, takeuchi2023hladrb1*0405isinvolved pages 1-2)

---

## 3. Phenotypes (clinical spectrum) 

### 3.1 Clinical stages / temporal development
Four phases are classically described: 
1) **Prodromal** (neurologic/auditory symptoms; CSF pleocytosis), 
2) **Acute uveitic** (diffuse choroiditis → papilledema/exudative detachments; may evolve to panuveitis), 
3) **Convalescent** (depigmentation; vitiligo/poliosis/alopecia), 
4) **Chronic recurrent** (chronic recurrent granulomatous anterior uveitis; less commonly recurrent exudative detachments). (tugaltutkun2024vogtkoyanagiharadadisease pages 1-3)

A COVID-era review notes the prodromal phase is often ~3–5 days and the acute uveitic stage lasts weeks with bilateral posterior uveitis and choroidal thickening/serous detachments. (manni2023vogtkoyanagiharadadiseaseand pages 2-4)

### 3.2 Phenotype frequencies from a large cohort (recent primary data)
In the Chinese Han VKH cohort (n=912), reported frequencies included: uveitis 100%, sunset glow fundus 48.7%, headache 49.2%, tinnitus 45.0%, vitiligo 11.4%, alopecia 31.4%. (zhou2023geneticassociationof pages 1-2)

### 3.3 Key phenotype types (examples) and suggested ontology terms
Below are representative phenotype mappings (not exhaustive).

**Ocular**
- Bilateral granulomatous panuveitis / diffuse choroiditis (HPO: *Uveitis*; *Choroiditis*; *Panuveitis*). (tugaltutkun2024vogtkoyanagiharadadisease pages 1-3, manni2023vogtkoyanagiharadadiseaseand pages 2-4)
- Exudative/serous retinal detachment (HPO: *Retinal detachment*; often “serous retinal detachment”) (tugaltutkun2024vogtkoyanagiharadadisease pages 1-3, manni2023vogtkoyanagiharadadiseaseand pages 2-4)
- Choroidal thickening (HPO candidate: *Abnormal choroid morphology* / *Choroidal thickening*). (manni2023vogtkoyanagiharadadiseaseand pages 16-19, tugaltutkun2024vogtkoyanagiharadadisease pages 1-3)
- “Sunset glow fundus” (clinical sign; HPO candidate: *Abnormal fundus pigmentation*). (feng2024predictivefactorsand pages 1-2, zhou2023geneticassociationof pages 1-2)

**Neurologic**
- Headache; aseptic meningitis / meningeal symptoms (HPO: *Headache*; *Meningitis*; *Cerebrospinal fluid pleocytosis*) (manni2023vogtkoyanagiharadadiseaseand pages 2-4, zhou2023geneticassociationof pages 1-2)

**Auditory**
- Tinnitus (HPO: *Tinnitus*) (zhou2023geneticassociationof pages 1-2)

**Integumentary**
- Vitiligo, poliosis, alopecia (HPO: *Vitiligo*; *Poliosis*; *Alopecia*) (tugaltutkun2024vogtkoyanagiharadadisease pages 1-3, zhou2023geneticassociationof pages 1-2)

### 3.4 Anatomical structures affected (UBERON suggestions)
- Eye uvea/choroid (UBERON: *uvea*, *choroid*) (tugaltutkun2024vogtkoyanagiharadadisease pages 1-3)
- Meninges / CNS coverings (UBERON: *meninges*) (tugaltutkun2024vogtkoyanagiharadadisease pages 1-3)
- Inner ear / auditory system (UBERON: *inner ear*) (tugaltutkun2024vogtkoyanagiharadadisease pages 1-3)
- Skin and hair follicles (UBERON: *skin*, *hair follicle*) (tugaltutkun2024vogtkoyanagiharadadisease pages 1-3)

### 3.5 Cell types involved (CL suggestions)
- CD4+ T cell (CL: *T-helper cell*) (sugita2006ocularinfiltratingcd4+ pages 1-2)
- Th1‑polarized effector/memory CD4+ T cells (CL: *effector memory T cell*; functional subtype) (sugita2006ocularinfiltratingcd4+ pages 7-8)
- Macrophage (CL: *macrophage*) (supported by animal-model infiltrates) (sorrick2022immuneactivitiesin pages 1-2)
- B cell (CL: *B cell*) (supported by animal-model infiltrates and B-cell involvement in chronic disease) (sorrick2022immuneactivitiesin pages 1-2, elasrar2021newperspectiveson pages 1-2)

---

## 4. Genetic / molecular information

### 4.1 “Causal” genes
VKH is not a Mendelian disorder with a single causal gene in the retrieved evidence; it is best characterized as **multifactorial/polygenic** with strong HLA associations and multiple immune pathway loci.

### 4.2 Susceptibility variants (recent primary evidence)
- **PRKCD rs74437127**: C allele risk (OR 1.624) and T allele protective (OR 0.616) (zhou2023geneticassociationof pages 1-2)
- **CARD9 rs3812555**: CC genotype risk (OR 1.810), C allele risk (OR 1.698), with functional association to higher CARD9 mRNA and TNF‑α. (zhou2023geneticassociationof pages 1-2)

### 4.3 Molecular pathophysiology (causal chain)
1) **Predisposition** (e.g., HLA‑DRB1*04:05 and other genetic factors) → 
2) **Trigger** (viral infection/vaccination or iatrogenic immune disinhibition with ICIs) → 
3) **Antigen presentation and loss of tolerance** to melanocyte antigens (e.g., tyrosinase/gp100) → 
4) **Effector inflammation in choroid/uvea** with cytokine production (TNF‑α, IFN‑γ; Th1/Th17 signatures) → 
5) **Tissue damage and melanocyte loss** leading to ocular exudation/detachments acutely and depigmentation (sunset glow fundus; vitiligo/poliosis/alopecia) chronically. (tugaltutkun2024vogtkoyanagiharadadisease pages 1-3, sugita2006ocularinfiltratingcd4+ pages 1-2, zhou2023geneticassociationof pages 1-2, manni2023vogtkoyanagiharadadiseaseand pages 1-2)

### 4.4 GO biological process suggestions
- **T cell activation**; **antigen processing and presentation (MHC class II)**; **cytokine-mediated signaling**; **inflammatory response**; **leukocyte migration/chemotaxis** (supported by RANTES and IFN‑γ responses) (sugita2006ocularinfiltratingcd4+ pages 7-8, sugita2006ocularinfiltratingcd4+ pages 1-2)

---

## 5. Environmental information
Key non-genetic contributors described in the retrieved evidence include viral infections and vaccinations as plausible triggers, particularly highlighted in COVID-era literature, and iatrogenic triggers such as immune checkpoint inhibitors. (manni2023vogtkoyanagiharadadiseaseand pages 1-2, takeuchi2023hladrb1*0405isinvolved pages 1-2)

---

## 6. Mechanism / pathophysiology (expanded)

### 6.1 Immune system involvement
- VKH is characterized by melanocyte antigen–directed CD4+ T cell responses (Th1-like functional profile) and inflammatory mediator production (e.g., IFN‑γ; RANTES). (sugita2006ocularinfiltratingcd4+ pages 1-2, sugita2006ocularinfiltratingcd4+ pages 7-8)
- CARD9 risk genotype correlates with increased TNF‑α production, linking innate/adaptive signaling nodes to inflammatory cytokine output in VKH susceptibility. (zhou2023geneticassociationof pages 1-2)

### 6.2 Expert synthesis (therapeutic window concept)
A 2021 mechanistic treatment review argues that early high-dose corticosteroids alone may be insufficient to prevent chronic evolution and emphasizes early combination therapy (e.g., corticosteroids + mycophenolate mofetil) as a “window of opportunity” to prevent chronically evolving disease; it also highlights B cell involvement in chronic disease, supported by responsiveness to rituximab in refractory cases. (URL: https://doi.org/10.3389/fmed.2021.705796; publication **2021‑11**) (elasrar2021newperspectiveson pages 1-2)

---

## 7. Anatomical structures affected
Primary involved structures include the uveal tract (notably choroid), with systemic involvement in meninges, inner ear, and integumentary tissues (skin/hair) as described in modern reviews and classification discussions. (tugaltutkun2024vogtkoyanagiharadadisease pages 1-3, manni2023vogtkoyanagiharadadiseaseand pages 1-2)

---

## 8. Temporal development
- **Typical onset:** Most commonly in adults (2nd–5th decades), with prodromal systemic symptoms possible before ocular disease. (manni2023vogtkoyanagiharadadiseaseand pages 1-2, manni2023vogtkoyanagiharadadiseaseand pages 2-4)
- **Course:** May resolve with early therapy or evolve into chronically recurrent disease with anterior granulomatous uveitis and depigmentation. (tugaltutkun2024vogtkoyanagiharadadisease pages 1-3)

---

## 9. Inheritance and population

### 9.1 Inheritance
Best classified as **multifactorial/polygenic**, with strong HLA class II associations and additional immune gene contributions (PRKCD/CARD9). (zhou2023geneticassociationof pages 1-2, takeuchi2023hladrb1*0405isinvolved pages 1-2)

### 9.2 Population demographics / geographic distribution
- VKH is more frequent in pigmented populations (e.g., Asians, Middle Easterners, Hispanics, Native Americans) and relatively rare in Europe; women often predominate and onset is typically in the 2nd–5th decades. (manni2023vogtkoyanagiharadadiseaseand pages 1-2, li2023bibliometricanalysisof pages 1-2)

### 9.3 Recent epidemiology statistics available in retrieved literature
- Puerto Rico cohort (n=24) suggested seasonality: 50% onset in fall vs 12.5% in spring (P=0.043). (Published **2023‑02**; URL: https://doi.org/10.1080/09273948.2022.2029499) (amaral2023; retrieved but not fully evidence-scanned in this run)
- True population incidence/prevalence per 100,000 for VKH specifically was **not** obtained from the retrieved full texts; available numbers in retrieved COVID-era review include *vaccine-induced uveitis* incidence (8–13/100,000/year) but this is not VKH-specific. (manni2023vogtkoyanagiharadadiseaseand pages 2-4)

---

## 10. Diagnostics

### 10.1 Clinical diagnostic criteria and recent comparisons
Diagnosis is clinical with multimodal imaging support; multiple criteria sets are discussed. In a Chinese case–control comparison summarized in 2024, sensitivities differed substantially: **CDCV 92.2%**, **RDC 66.7%**, **SUN-C 54.3%**, with high specificity across sets. (tugaltutkun2024vogtkoyanagiharadadisease pages 1-3, tugaltutkun2024vogtkoyanagiharadadisease media 234f6a18, tugaltutkun2024vogtkoyanagiharadadisease media dc9f8533)

### 10.2 Imaging and laboratory findings (real-world implementation)
**Imaging hallmarks in acute disease** include choroidal thickening and subretinal fluid on OCT/EDI‑OCT, pinpoint hyperfluorescence/leakage patterns on fluorescein angiography, and hypocfluorescent dots/patches on ICGA. (manni2023vogtkoyanagiharadadiseaseand pages 16-19)

**OCTA monitoring (recent development)**
- In an acute VKH series summarized in 2024, **93.8%** of eyes had “dark foci”/flow voids in choriocapillaris and Sattler’s layer at presentation, decreasing with therapy and reduced choroidal thickness, supporting OCTA as a noninvasive monitoring tool. (tugaltutkun2024vogtkoyanagiharadadisease pages 1-3, tugaltutkun2024vogtkoyanagiharadadisease media 234f6a18, tugaltutkun2024vogtkoyanagiharadadisease media dc9f8533)

**CSF pleocytosis** may be present in prodromal/neurologic phase and was reported in vaccine-associated cases (CSF pleocytosis in 7/21 in one review). (manni2023vogtkoyanagiharadadiseaseand pages 2-4)

### 10.3 Differential diagnosis
Not systematically extracted in the retrieved texts; the 2024 editorial notes OCTA patterns may help differentiate atypical VKH from entities such as APMPPE in some contexts. (tugaltutkun2024vogtkoyanagiharadadisease pages 1-3)

---

## 11. Outcome / prognosis

### 11.1 Prognostic factors (2024 cohort data)
A 2024 retrospective cohort (Beijing Tongren Hospital; 62 patients, 2020–2023) identified factors associated with chronic recurrence:
- Chronic-recurrent group had worse initial BCVA (1.38±0.54 vs 0.64±0.29 logMAR; P=0.002) and higher sunset glow fundus prevalence (64.3% vs 23.5%; P=0.001). (Published **2024‑06**; URL: https://doi.org/10.1186/s12886-024-03511-9) (feng2024predictivefactorsand pages 1-2)
- Logistic regression predictors included **older age at onset (P=0.042)** and **sunset glow fundus (P=0.037)**. (feng2024predictivefactorsand pages 1-2)

### 11.2 COVID/vaccine-associated prognosis
A 2023 synthesis reports favorable short-term outcomes in reported COVID infection/vaccination-associated cases, with high corticosteroid responsiveness and mean visual acuity ~20/32 in short-term follow-up. (manni2023vogtkoyanagiharadadiseaseand pages 20-22)

---

## 12. Treatment (current practice, evidence, and trials)

### 12.1 Standard pharmacotherapy and strategy
A 2023 retrospective series abstract states: “Treatment is usually initiated with corticosteroids followed by an early introduction of immunosuppressive treatment (IMT).” (URL: https://doi.org/10.1186/s12348-023-00333-6; publication **2023‑05**) (rahman2023immunosuppressivetherapyfor pages 1-2)

**Evidence for early combination IMT**
- In 26 patients (20-year retrospective), **81% (21/26)** treated with combined IMT/low-dose steroids achieved disease stability with improved median VA from 0.3 logMAR to 0.0 logMAR at 24 months (p=0.0001). MMF was commonly used but 50% of MMF-treated patients did not achieve disease control. (rahman2023immunosuppressivetherapyfor pages 1-2)

### 12.2 Biologics and comparative effectiveness (high-impact 2023 randomized trial)
A 26-week randomized non-inferiority trial (ChiCTR2100043061; **110 randomized**) compared a cyclosporine-based immunosuppressant strategy vs an adalimumab-based biologic strategy (both with corticosteroids). The abstract states: “we assigned 110 patients… to cyclosporine-based immunosuppressant strategy… or adalimumab-based biologic strategy… The primary outcome is change from baseline in best-corrected visual acuity at week 26… P < 0.001 for non-inferiority.” (Published **2023‑06**; URL: https://doi.org/10.1038/s41467-023-39483-5) (zhong2023arandomizednoninferiority pages 1-2)
Key quantitative outcomes:
- BCVA improvement: 11.2 letters (95% CI 7.5–14.9) vs 6.3 letters (3.1–9.6); difference 4.9 (0.2–9.5) with one-sided P<0.001 for non-inferiority. (zhong2023arandomizednoninferiority pages 1-2)
- Serious adverse events: 0.70 vs 1.21 events per patient-year (lower in cyclosporine strategy). (zhong2023arandomizednoninferiority pages 1-2)

### 12.3 Adalimumab in chronic-recurrent VKH (2024 observational evidence)
Adalimumab significantly reduced anterior chamber and vitreous inflammatory cells and reduced recurrence rate (P=0.009) in a 2024 retrospective cohort of chronic-recurrent VKH. (feng2024predictivefactorsand pages 1-2)

### 12.4 JAK inhibitors (recent real-world prospective registry cohort, 2024)
A prospective AIDA network cohort (n=12; included **1 VKH** case) found complete ocular control in 12/12 after starting JAK inhibitors and a marked reduction in flare incidence from 125 to 28.6 episodes per 1,000 person-months (incidence rate ratio 4.37; 95% CI 1.3–14.7; p=0.02). (Published **2024‑08‑23**; URL: https://doi.org/10.3389/fmed.2024.1439338) (vitale2024efficacyandsafety pages 1-2)

### 12.5 Clinical trials (real-world implementations and ongoing studies)
- **NCT03399175** (University of São Paulo; recruiting): early high-dose corticosteroid + immunosuppressive therapy with multimodal imaging and functional testing; primary outcome includes scotopic ERG variation (6–12 months). (NCT03399175 chunk 1)
  - URL: https://clinicaltrials.gov/study/NCT03399175 (NCT03399175 chunk 1)
- **NCT05590416** (Tianjin Medical University; recruiting): prospective cohort comparing adalimumab + glucocorticoids vs traditional therapy in acute VKH (onset <1 month); primary outcomes include logMAR BCVA change and recurrence rate at 24 weeks. (NCT05590416 chunk 1)
  - URL: https://clinicaltrials.gov/study/NCT05590416 (NCT05590416 chunk 1)

### 12.6 MAXO (Medical Action Ontology) term suggestions (representative)
- Systemic glucocorticoid therapy
- Immunosuppressive therapy / immunomodulatory therapy (e.g., mycophenolate mofetil, azathioprine, cyclosporine)
- Tumor necrosis factor inhibitor therapy (adalimumab)
- Janus kinase inhibitor therapy (baricitinib, tofacitinib, upadacitinib)
- Multimodal ocular imaging (OCT, ICGA, FA, OCTA) for monitoring
(these actions are supported as real-world implementations in the cited studies) (rahman2023immunosuppressivetherapyfor pages 1-2, vitale2024efficacyandsafety pages 1-2, tugaltutkun2024vogtkoyanagiharadadisease pages 1-3)

---

## 13. Prevention

### 13.1 Primary prevention
No established primary prevention exists for VKH in the retrieved evidence.

### 13.2 Secondary/tertiary prevention (preventing chronic evolution and complications)
The actionable prevention strategy is early recognition and prompt systemic therapy to prevent chronic recurrence and sunset glow fundus; multiple sources emphasize early treatment improves outcomes. (rahman2023immunosuppressivetherapyfor pages 1-2, manni2023vogtkoyanagiharadadiseaseand pages 8-10)

### 13.3 Vaccination considerations (COVID era)
Despite case reports of VKH onset/relapse after vaccination, expert synthesis emphasizes that good therapeutic response and benefit–risk considerations should not discourage vaccination, while recommending vigilance and early treatment in predisposed subjects. (manni2023vogtkoyanagiharadadiseaseand pages 1-2, manni2023vogtkoyanagiharadadiseaseand pages 20-22)

---

## 14. Other species / natural disease
A spontaneous autoimmune pigmentation disorder model (Smyth line chicken) shows systemic melanocyte autoimmunity with ocular involvement resembling VKH and sympathetic ophthalmia; infiltrating leukocytes include CD4+, CD8+ T cells, B cells, and macrophages, and cytokine profiles suggest Th1 polarization. (Published **2022‑04**; URL: https://doi.org/10.3389/fmed.2022.846100) (sorrick2022immuneactivitiesin pages 1-2)

---

## 15. Model organisms

### 15.1 Induced experimental VKH-like uveitis models
- Experimental melanin-protein induced uveitis (EMIU) and related models show that immunization with tyrosinase-related proteins 1 and 2 in rats can produce VKH-like inflammatory changes, supporting melanocyte antigens as mechanistic drivers and providing a platform for antigen-specific therapy concepts. (adamus2002experimentalautoimmuneuveitides pages 1-3)

### 15.2 Spontaneous model relevant to VKH mechanisms
- Smyth line chicken autoimmune vitiligo with uveitis/vision impairment offers a spontaneous model to interrogate systemic anti-melanocyte immunity and timing of immune infiltration preceding overt disease. (sorrick2022immuneactivitiesin pages 1-2)

---

## Recent developments and latest research highlights (2023–2024 prioritized)
1) **Diagnostic criteria modernization and imaging-based definition of choroidal involvement**: CDCV criteria sensitivity 92.2% vs RDC 66.7% vs SUN-C 54.3% in a Chinese case-control comparison summarized in 2024, with explicit incorporation of EDI-OCT/ICGA in some modern criteria. (2024‑04‑24; https://doi.org/10.1080/09273948.2024.2331401) (tugaltutkun2024vogtkoyanagiharadadisease pages 1-3)
2) **COVID-19 era trigger literature**: systematic compilation of post-infection and post-vaccine VKH, with rapid onset intervals and high corticosteroid responsiveness, supporting continued surveillance rather than a change in standard management. (2023‑09; https://doi.org/10.3390/jcm12196242) (manni2023vogtkoyanagiharadadiseaseand pages 1-2)
3) **Head-to-head strategy trial evidence**: cyclosporine-based strategy non-inferior to adalimumab-based strategy for 26-week visual improvement, informing real-world decision-making when selecting conventional immunosuppression vs biologics. (2023‑06; https://doi.org/10.1038/s41467-023-39483-5) (zhong2023arandomizednoninferiority pages 1-2)
4) **Newer therapeutics**: prospective registry evidence supporting JAK inhibitors for refractory non-infectious ocular inflammation including VKH. (2024‑08‑23; https://doi.org/10.3389/fmed.2024.1439338) (vitale2024efficacyandsafety pages 1-2)

---

## Data table of high-yield facts
| Domain | Specific finding (with numbers where available) | Source (first author year journal) | Publication date | URL | Evidence context ID |
|---|---|---|---|---|---|
| Identifiers/Definition | VKH is a multisystem autoimmune disorder affecting the eyes, central nervous system, auditory system, and integumentary system; disease course includes prodromal, acute uveitic, convalescent, and chronic recurrent phases. | Tugal-Tutkun 2024 *Ocular Immunology and Inflammation* | 2024-04-24 | https://doi.org/10.1080/09273948.2024.2331401 | (tugaltutkun2024vogtkoyanagiharadadisease pages 1-3) |
| Genetics | In 912 VKH cases vs 878 controls, **PRKCD rs74437127 C allele** increased susceptibility (**Pc=0.020, OR=1.624, 95% CI 1.200–2.199**), while **T allele** was protective (**Pc=0.020, OR=0.616, 95% CI 0.455–0.833**). | Zhou 2023 *Human Genomics* | 2023-02 | https://doi.org/10.1186/s40246-023-00459-7 | (zhou2023geneticassociationof pages 1-2) |
| Genetics | **CARD9 rs3812555 CC genotype** and **C allele** increased VKH susceptibility (**Pc=2.04×10^-5, OR=1.810, 95% CI 1.418–2.311**; **Pc=2.76×10^-5, OR=1.698, 95% CI 1.362–2.118**), whereas **TC genotype** and **T allele** were protective (**Pc=7.85×10^-5, OR=0.559**; **Pc=2.76×10^-5, OR=0.589**). CC carriers had higher **CARD9 mRNA** and **TNF-α** production (**P=1.00×10^-4; P=2.00×10^-3**). | Zhou 2023 *Human Genomics* | 2023-02 | https://doi.org/10.1186/s40246-023-00459-7 | (zhou2023geneticassociationof pages 1-2) |
| Phenotypes & staging | In the 912-patient VKH cohort, phenotype frequencies were: **uveitis 100%**, **sunset glow fundus 48.7%**, **headache 49.2%**, **tinnitus 45.0%**, **vitiligo 11.4%**, **alopecia 31.4%**. | Zhou 2023 *Human Genomics* | 2023-02 | https://doi.org/10.1186/s40246-023-00459-7 | (zhou2023geneticassociationof pages 1-2) |
| Genetics / Triggers | In immune checkpoint inhibitor-associated uveitis, 5/9 cases were VKH-like and 4/9 non-VKH-like; among genotyped patients, **4/4 VKH-like** were **HLA-DRB1*04:05 positive** vs **0/3 non-VKH-like**, with significant association (**P=0.029**). Uveitis incidence in ICI-treated patients is reported as **~0.3–1%**. | Takeuchi 2023 *Scientific Reports* | 2023-08 | https://doi.org/10.1038/s41598-023-40565-z | (takeuchi2023hladrb1*0405isinvolved pages 1-2) |
| Triggers | Proposed triggers include viral infection and vaccination; review identified **4 young post-COVID infection VKH cases** (all female; mean age **30 ± 5.43** years; mean onset **~19.8 days** after infection), and summarized **33 new-onset post-vaccine cases**. | Manni 2023 *Journal of Clinical Medicine* | 2023-09 | https://doi.org/10.3390/jcm12196242 | (manni2023vogtkoyanagiharadadiseaseand pages 8-10, manni2023vogtkoyanagiharadadiseaseand pages 16-19) |
| Triggers | For COVID-19 vaccine-associated VKH review, **21 patients** were identified (9 male, 12 female; median age **45** years, range 19–78); **14/21** after first dose, **8/21** after second; mean interval to symptoms **7.5 days**; **20/21 bilateral**; **16** had meningitis symptoms; **16** serous retinal detachment; **14** choroidal thickening; all received corticosteroids; mean recovery time **2 months**. | Xu 2023 *Human Vaccines & Immunotherapeutics* | 2023-06 | https://doi.org/10.1080/21645515.2023.2220630 | (manni2023vogtkoyanagiharadadiseaseand pages 2-4) |
| Phenotypes & staging | Typical acute features include bilateral choroiditis/panuveitis, exudative retinal detachment, meningismus/CSF pleocytosis, auditory and integumentary signs. Prodromal phase lasts **~3–5 days** before acute uveitic stage developing over weeks. | Manni 2023 *Journal of Clinical Medicine* | 2023-09 | https://doi.org/10.3390/jcm12196242 | (manni2023vogtkoyanagiharadadiseaseand pages 2-4) |
| Diagnostics/Imaging | Comparison of criteria in Chinese case-control study: **Chinese Diagnostic Criteria for VKH (CDCV) sensitivity 92.2%**, vs **Revised Diagnostic Criteria (RDC) 66.7%** and **SUN classification criteria 54.3%**; all three had high specificity without significant differences. | Tugal-Tutkun 2024 *Ocular Immunology and Inflammation* | 2024-04-24 | https://doi.org/10.1080/09273948.2024.2331401 | (tugaltutkun2024vogtkoyanagiharadadisease pages 1-3) |
| Diagnostics/Imaging | For acute VKH monitoring with OCTA, **93.8%** of eyes had scattered dark foci in choriocapillaris and Sattler’s layer at presentation; follow-up in **30 eyes** showed reduction in dark foci with decreasing choroidal thickness after treatment. | Tugal-Tutkun 2024 *Ocular Immunology and Inflammation* | 2024-04-24 | https://doi.org/10.1080/09273948.2024.2331401 | (tugaltutkun2024vogtkoyanagiharadadisease pages 1-3) |
| Treatment | In a 26-patient retrospective VKH series, treatment shifted from steroid monotherapy to combined immunosuppressive therapy (IMT)/low-dose steroid. **81% (21/26)** treated with combined IMT/steroid achieved disease stability with improved median VA from **0.3 logMAR to 0.0 logMAR** at 24 months (**p=0.0001**). | Rahman 2023 *Journal of Ophthalmic Inflammation and Infection* | 2023-05 | https://doi.org/10.1186/s12348-023-00333-6 | (rahman2023immunosuppressivetherapyfor pages 1-2) |
| Treatment | In the same series, **MMF monotherapy** was most common (**13/19 IMT-treated; 68%**) and was well tolerated, but **50%** of MMF-treated patients did **not** achieve disease control. Average time from diagnosis to IMT initiation was **2.1 months**; average time to steroid-sparing effect was **5 months**. | Rahman 2023 *Journal of Ophthalmic Inflammation and Infection* | 2023-05 | https://doi.org/10.1186/s12348-023-00333-6 | (rahman2023immunosuppressivetherapyfor pages 1-2) |
| Prognosis / Prognostic factors | In 62 VKH patients (34 acute-resolved, 28 chronic-recurrent), chronic-recurrent patients were older (**49.00 ± 16.43** vs **38.29 ± 15.46** years) and had worse initial BCVA (**1.38 ± 0.54** vs **0.64 ± 0.29 logMAR; P=0.002**). Complications occurred in **41.7%** vs **29.4%** (**P=0.006**), and sunset glow fundus in **64.3%** vs **23.5%** (**P=0.001**). | Feng 2024 *BMC Ophthalmology* | 2024-06 | https://doi.org/10.1186/s12886-024-03511-9 | (feng2024predictivefactorsand pages 1-2) |
| Prognosis / Prognostic factors | Predictors of progression to chronic-recurrent VKH included poor initial BCVA (**P=0.046**) and sunset glow fundus (**P=0.040**); logistic regression identified **older age at onset (P=0.042)** and **sunset glow fundus (P=0.037)** as significant predictors. | Feng 2024 *BMC Ophthalmology* | 2024-06 | https://doi.org/10.1186/s12886-024-03511-9 | (feng2024predictivefactorsand pages 1-2) |
| Treatment | In chronic-recurrent VKH, **adalimumab** significantly reduced **anterior chamber inflammatory cells (P=0.000)**, **vitreous inflammatory cells (P=0.001)**, and **recurrence rate (P=0.009)**. | Feng 2024 *BMC Ophthalmology* | 2024-06 | https://doi.org/10.1186/s12886-024-03511-9 | (feng2024predictivefactorsand pages 1-2) |
| Treatment | In a prospective AIDA network cohort of **12** adults with non-infectious ocular inflammatory disease (including **1 VKH** case), **4** received baricitinib, **1** tofacitinib, and **7** upadacitinib; mean treatment duration was **8.6 ± 5.5 months**. | Vitale 2024 *Frontiers in Medicine* | 2024-08-23 | https://doi.org/10.3389/fmed.2024.1439338 | (vitale2024efficacyandsafety pages 1-2) |
| Treatment | With JAK inhibitors, ocular disease control was complete in **12/12** patients; flare incidence fell from **125** to **28.6 episodes per 1,000 person-months**, incidence rate ratio **4.37** (95% CI **1.3–14.7**, **p=0.02**) for pre- vs post-JAK periods. | Vitale 2024 *Frontiers in Medicine* | 2024-08-23 | https://doi.org/10.3389/fmed.2024.1439338 | (vitale2024efficacyandsafety pages 1-2) |
| Prognosis / Prognostic factors | Early corticosteroid use is associated with better outcomes; rapid early visual acuity improvement predicts better final VA, while greater relapse number is associated with more complications and worse visual prognosis. | Manni 2023 *Journal of Clinical Medicine* | 2023-09 | https://doi.org/10.3390/jcm12196242 | (manni2023vogtkoyanagiharadadiseaseand pages 8-10) |
| Clinical trials | **NCT03399175**: single-group interventional prospective study, University of São Paulo; **40** participants; started **2015-03-23**; recruiting. Tests **early high-dose systemic corticosteroid + immunosuppressive therapy** in acute VKH with ≥12-month follow-up using FA, ICGA, EDI-OCT, ERG, autofluorescence, perimetry, contrast sensitivity, and QoL. Primary outcome: **scotopic ERG variation between 6 and 12 months**. | Yamamoto 2015 *ClinicalTrials.gov* | 2015-03-23 start; recruiting | https://clinicaltrials.gov/study/NCT03399175 | (NCT03399175 chunk 1) |
| Clinical trials | **NCT05590416**: single-center prospective observational cohort, Tianjin Medical University; **15** participants; recruiting; compares **adalimumab** (80 mg loading, then 40 mg every 2 weeks) + glucocorticoids vs traditional therapy in **acute VKH onset <1 month**. Primary outcomes: **change in logMAR BCVA** and **recurrence rate at 24 weeks**; secondary outcomes include SUN anterior chamber cell grade and prednisone exposure. | Zhang 2021 *ClinicalTrials.gov* | 2021-06-01 start; recruiting | https://clinicaltrials.gov/study/NCT05590416 | (NCT05590416 chunk 1) |


*Table: This table compiles high-yield, citable findings on Vogt-Koyanagi-Harada disease across genetics, triggers, phenotypes, diagnostics, treatment, prognosis, and ongoing trials. It is designed to support rapid evidence-backed drafting of a comprehensive disease report.*

---

## Limitations of this report (evidence gaps from this run)
- **ICD‑10/ICD‑11 and MeSH descriptor IDs** were not retrieved from dedicated ontology sources (e.g., ICD/MeSH browsers) within the accessible full texts; the report therefore provides MONDO and trial-level MeSH categorization only. (OpenTargets Search: Vogt-Koyanagi-Harada disease, NCT05590416 chunk 2)
- **True population-based VKH incidence/prevalence** (per 100,000) was not captured in the retrieved full texts; additional targeted epidemiology sources would be required.
- **Quality-of-life instrument outcomes** (e.g., NEI-VFQ, SF-36) were not available in retrieved papers; only trial registry mentions QoL questionnaires. (NCT03399175 chunk 1)


References

1. (OpenTargets Search: Vogt-Koyanagi-Harada disease): Open Targets Query (Vogt-Koyanagi-Harada disease, 0 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (tugaltutkun2024vogtkoyanagiharadadisease pages 1-3): Ilknur Tugal-Tutkun, Derrick P. Smit, Ahmed M. Abu El-Asrar, Carl P. Herbort, and Jennifer E. Thorne. Vogt-koyanagi-harada disease. Ocular Immunology and Inflammation, 32:363-366, Apr 2024. URL: https://doi.org/10.1080/09273948.2024.2331401, doi:10.1080/09273948.2024.2331401. This article has 12 citations and is from a peer-reviewed journal.

3. (rahman2023immunosuppressivetherapyfor pages 1-2): Najiha Rahman, Jose Carlo M Artiaga, Konstantinos Bouras, Joshua Luis, Angela Rees, and Mark Westcott. Immunosuppressive therapy for vogt-koyanagi-harada disease: a retrospective study and review of literature. Journal of Ophthalmic Inflammation and Infection, May 2023. URL: https://doi.org/10.1186/s12348-023-00333-6, doi:10.1186/s12348-023-00333-6. This article has 24 citations and is from a peer-reviewed journal.

4. (vitale2024efficacyandsafety pages 1-2): Antonio Vitale, Judith Palacios-Olid, Valeria Caggiano, Gaafar Ragab, José Hernández-Rodríguez, Laura Pelegrín, Germán Mejía-Salgado, Laura Zarate-Pinzón, Stefano Gentileschi, Jurgen Sota, Alex Fonollosa, Ester Carreño, Carla Gaggiano, Rana Hussein Amin, Alberto Balistreri, Javier Narváez, Gian Marco Tosi, Bruno Frediani, Luca Cantarini, Alejandra de-la-Torre, and Claudia Fabiani. Efficacy and safety of janus kinase inhibitors in non-infectious inflammatory ocular diseases: a prospective cohort study from the international aida network registries. Frontiers in Medicine, Aug 2024. URL: https://doi.org/10.3389/fmed.2024.1439338, doi:10.3389/fmed.2024.1439338. This article has 29 citations.

5. (manni2023vogtkoyanagiharadadiseaseand pages 1-2): Priscilla Manni, Maria Carmela Saturno, and Massimo Accorinti. Vogt-koyanagi-harada disease and covid. Journal of Clinical Medicine, 12:6242, Sep 2023. URL: https://doi.org/10.3390/jcm12196242, doi:10.3390/jcm12196242. This article has 8 citations.

6. (NCT05590416 chunk 2): Xiaomin Zhang. A Study of Adalimumab in Acute Vogt-Koyanagi-Harada Disease. Tianjin Medical University. 2021. ClinicalTrials.gov Identifier: NCT05590416

7. (zhou2023geneticassociationof pages 1-2): Chunya Zhou, Shiya Cai, Yuhong Xie, Zhen Zeng, Jun Zhang, Guannan Su, Qiuying Wu, Xingsheng Ye, Qingfeng Cao, Peizeng Yang, and Jianmin Hu. Genetic association of prkcd and card9 polymorphisms with vogt–koyanagi–harada disease in the chinese han population. Human Genomics, Feb 2023. URL: https://doi.org/10.1186/s40246-023-00459-7, doi:10.1186/s40246-023-00459-7. This article has 3 citations and is from a peer-reviewed journal.

8. (zhong2023arandomizednoninferiority pages 3-4): Zhenyu Zhong, Lingyu Dai, Qiuying Wu, Yu Gao, Yanlin Pu, Guannan Su, Xiaorong Lu, Fuxiang Zhang, Chong Tang, Yao Wang, Chunjiang Zhou, and Peizeng Yang. A randomized non-inferiority trial of therapeutic strategy with immunosuppressants versus biologics for vogt-koyanagi-harada disease. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-39483-5, doi:10.1038/s41467-023-39483-5. This article has 16 citations and is from a highest quality peer-reviewed journal.

9. (adamus2002experimentalautoimmuneuveitides pages 1-3): GRAZYNA ADAMUS and CHI-CHAO CHAN. Experimental autoimmune uveitides: multiple antigens, diverse diseases. International Reviews of Immunology, 21:209-229, Jan 2002. URL: https://doi.org/10.1080/08830180212068, doi:10.1080/08830180212068. This article has 85 citations and is from a peer-reviewed journal.

10. (sorrick2022immuneactivitiesin pages 1-2): Jordan Sorrick, Wilson Huett, Kristen A. Byrne, and Gisela F. Erf. Immune activities in choroids of visually impaired smyth chickens with autoimmune vitiligo. Frontiers in Medicine, Apr 2022. URL: https://doi.org/10.3389/fmed.2022.846100, doi:10.3389/fmed.2022.846100. This article has 4 citations.

11. (sugita2006ocularinfiltratingcd4+ pages 1-2): Sunao Sugita, Hiroshi Takase, Chikako Taguchi, Yasuhisa Imai, Koju Kamoi, Tatsushi Kawaguchi, Yoshiharu Sugamoto, Yuri Futagami, Kyogo Itoh, and Manabu Mochizuki. Ocular infiltrating cd4+ t cells from patients with vogt-koyanagi-harada disease recognize human melanocyte antigens. Investigative ophthalmology & visual science, 47 6:2547-54, Jun 2006. URL: https://doi.org/10.1167/iovs.05-1547, doi:10.1167/iovs.05-1547. This article has 202 citations and is from a domain leading peer-reviewed journal.

12. (sugita2006ocularinfiltratingcd4+ pages 7-8): Sunao Sugita, Hiroshi Takase, Chikako Taguchi, Yasuhisa Imai, Koju Kamoi, Tatsushi Kawaguchi, Yoshiharu Sugamoto, Yuri Futagami, Kyogo Itoh, and Manabu Mochizuki. Ocular infiltrating cd4+ t cells from patients with vogt-koyanagi-harada disease recognize human melanocyte antigens. Investigative ophthalmology & visual science, 47 6:2547-54, Jun 2006. URL: https://doi.org/10.1167/iovs.05-1547, doi:10.1167/iovs.05-1547. This article has 202 citations and is from a domain leading peer-reviewed journal.

13. (takeuchi2023hladrb1*0405isinvolved pages 1-2): Masaki Takeuchi, Akira Meguro, Jutaro Nakamura, Rei Chikagawa, Raiga Osada, Etsuko Shibuya, Yukiko Hasumi, Norihiro Yamada, Mami Ishihara, and Nobuhisa Mizuki. Hla-drb1*04:05 is involved in the development of vogt–koyanagi–harada disease-like immune-related adverse events in patients receiving immune checkpoint inhibitors. Scientific Reports, Aug 2023. URL: https://doi.org/10.1038/s41598-023-40565-z, doi:10.1038/s41598-023-40565-z. This article has 17 citations and is from a peer-reviewed journal.

14. (manni2023vogtkoyanagiharadadiseaseand pages 2-4): Priscilla Manni, Maria Carmela Saturno, and Massimo Accorinti. Vogt-koyanagi-harada disease and covid. Journal of Clinical Medicine, 12:6242, Sep 2023. URL: https://doi.org/10.3390/jcm12196242, doi:10.3390/jcm12196242. This article has 8 citations.

15. (muto2024effectofthe pages 6-7): Tetsuya Muto, Masaaki Sakamoto, Shoichiro Kusuda, Yasuo Haruyama, Shigeki Machida, Shinichiro Imaizumi, and Tetsuju Sekiryu. Effect of the covid-19 pandemic on vogt–koyanagi–harada disease. Scientific Reports, Jun 2024. URL: https://doi.org/10.1038/s41598-024-63957-1, doi:10.1038/s41598-024-63957-1. This article has 5 citations and is from a peer-reviewed journal.

16. (manni2023vogtkoyanagiharadadiseaseand pages 16-19): Priscilla Manni, Maria Carmela Saturno, and Massimo Accorinti. Vogt-koyanagi-harada disease and covid. Journal of Clinical Medicine, 12:6242, Sep 2023. URL: https://doi.org/10.3390/jcm12196242, doi:10.3390/jcm12196242. This article has 8 citations.

17. (feng2024predictivefactorsand pages 1-2): Hui Feng, Weixin Chen, Jianzhu Yang, Haorong Kong, Hongyu Li, Yuan He, and Hong Wang. Predictive factors and adalimumab efficacy in managing chronic recurrence vogt-koyanagi-harada disease. BMC Ophthalmology, Jun 2024. URL: https://doi.org/10.1186/s12886-024-03511-9, doi:10.1186/s12886-024-03511-9. This article has 9 citations and is from a peer-reviewed journal.

18. (elasrar2021newperspectiveson pages 1-2): Ahmed M. Abu El-Asrar, Jo Van Damme, Sofie Struyf, and Ghislain Opdenakker. New perspectives on the immunopathogenesis and treatment of uveitis associated with vogt-koyanagi-harada disease. Frontiers in Medicine, Nov 2021. URL: https://doi.org/10.3389/fmed.2021.705796, doi:10.3389/fmed.2021.705796. This article has 34 citations.

19. (li2023bibliometricanalysisof pages 1-2): Liangpin Li, Liyun Yuan, Xueyan Zhou, Xia Hua, and Xiaoyong Yuan. Bibliometric analysis of the vogt‒koyanagi‒harada disease literature. International Ophthalmology, 43:4137-4150, Aug 2023. URL: https://doi.org/10.1007/s10792-023-02815-x, doi:10.1007/s10792-023-02815-x. This article has 2 citations and is from a peer-reviewed journal.

20. (tugaltutkun2024vogtkoyanagiharadadisease media 234f6a18): Ilknur Tugal-Tutkun, Derrick P. Smit, Ahmed M. Abu El-Asrar, Carl P. Herbort, and Jennifer E. Thorne. Vogt-koyanagi-harada disease. Ocular Immunology and Inflammation, 32:363-366, Apr 2024. URL: https://doi.org/10.1080/09273948.2024.2331401, doi:10.1080/09273948.2024.2331401. This article has 12 citations and is from a peer-reviewed journal.

21. (tugaltutkun2024vogtkoyanagiharadadisease media dc9f8533): Ilknur Tugal-Tutkun, Derrick P. Smit, Ahmed M. Abu El-Asrar, Carl P. Herbort, and Jennifer E. Thorne. Vogt-koyanagi-harada disease. Ocular Immunology and Inflammation, 32:363-366, Apr 2024. URL: https://doi.org/10.1080/09273948.2024.2331401, doi:10.1080/09273948.2024.2331401. This article has 12 citations and is from a peer-reviewed journal.

22. (manni2023vogtkoyanagiharadadiseaseand pages 20-22): Priscilla Manni, Maria Carmela Saturno, and Massimo Accorinti. Vogt-koyanagi-harada disease and covid. Journal of Clinical Medicine, 12:6242, Sep 2023. URL: https://doi.org/10.3390/jcm12196242, doi:10.3390/jcm12196242. This article has 8 citations.

23. (zhong2023arandomizednoninferiority pages 1-2): Zhenyu Zhong, Lingyu Dai, Qiuying Wu, Yu Gao, Yanlin Pu, Guannan Su, Xiaorong Lu, Fuxiang Zhang, Chong Tang, Yao Wang, Chunjiang Zhou, and Peizeng Yang. A randomized non-inferiority trial of therapeutic strategy with immunosuppressants versus biologics for vogt-koyanagi-harada disease. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-39483-5, doi:10.1038/s41467-023-39483-5. This article has 16 citations and is from a highest quality peer-reviewed journal.

24. (NCT03399175 chunk 1): Joyce Hisae Yamamoto. Early Immunosuppressive Therapy on the Course of Vogt-Koyanagi-Harada Disease. University of Sao Paulo. 2015. ClinicalTrials.gov Identifier: NCT03399175

25. (NCT05590416 chunk 1): Xiaomin Zhang. A Study of Adalimumab in Acute Vogt-Koyanagi-Harada Disease. Tianjin Medical University. 2021. ClinicalTrials.gov Identifier: NCT05590416

26. (manni2023vogtkoyanagiharadadiseaseand pages 8-10): Priscilla Manni, Maria Carmela Saturno, and Massimo Accorinti. Vogt-koyanagi-harada disease and covid. Journal of Clinical Medicine, 12:6242, Sep 2023. URL: https://doi.org/10.3390/jcm12196242, doi:10.3390/jcm12196242. This article has 8 citations.