---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-07T19:31:23.350005'
end_time: '2026-05-07T19:46:40.208461'
duration_seconds: 916.86
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Primary Cutaneous Aggressive Epidermotropic CD8+ T-cell Lymphoma
  mondo_id: ''
  category: Cancer
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Primary Cutaneous Aggressive Epidermotropic CD8+ T-cell Lymphoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Primary Cutaneous Aggressive Epidermotropic CD8+ T-cell Lymphoma** covering all of the
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
- **Disease Name:** Primary Cutaneous Aggressive Epidermotropic CD8+ T-cell Lymphoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Primary Cutaneous Aggressive Epidermotropic CD8+ T-cell Lymphoma** covering all of the
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


## Comprehensive Disease Characteristics Research Report
### Target disease
**Primary cutaneous aggressive epidermotropic CD8+ T-cell lymphoma** (often written as *primary cutaneous CD8+ aggressive epidermotropic cytotoxic T-cell lymphoma*). This is a rare, highly aggressive **cutaneous T-cell lymphoma (CTCL)** characterized by a cytotoxic CD8+ epidermotropic T-cell infiltrate and rapid progression with propensity for extracutaneous dissemination. (deenen2019pitfallsindiagnosing pages 1-2, geller2018nktcelllymphomanasal pages 1-3)

---

## 1. Disease Information
### 1.1 Overview / definition (current understanding)
The entity is recognized within modern cutaneous lymphoma classifications as a distinct clinicopathologic syndrome of **epidermotropic CD8+ cytotoxic T cells** with aggressive behavior and poor outcomes. (deenen2019pitfallsindiagnosing pages 1-2, geller2018nktcelllymphomanasal pages 1-3)

In the WHO–EORTC 2018 update, it is listed explicitly as **“Primary cutaneous aggressive epidermotropic CD8-positive T-cell lymphoma (provisional)”** and summarized as presenting with **ulcerating plaques, nodules, and tumors**, with a typical immunophenotype **CD3+, CD4−, CD8+**, cytotoxic proteins positive, **CD56−**, and **EBV−**. (willemze2019the2018update pages 13-16, willemze2019the2018update media 461b18ed)

### 1.2 Key identifiers / ontology codes
Within the retrieved full texts, **no MONDO, Orphanet (ORPHA), MeSH, ICD-10/ICD-11, or OMIM identifiers were provided** for this specific disease name, including in the WHO–EORTC update excerpts and multiple case reports/reviews. (willemze2019the2018update pages 13-16, loya2023probableprimarycutaneous pages 4-4, sundram2019cutaneouslymphoproliferativedisorders pages 1-2)

### 1.3 Synonyms and alternative names
Nomenclature varies across clinical, dermatopathology, and molecular literature (e.g., “PCAETCL,” “pcAECyTCL,” and inclusion of “cytotoxic”). A harmonized list of name variants observed in the retrieved sources is provided below.

| Canonical name | Common abbreviations | Synonyms/variants in literature | Classification status notes (WHO/WHO-EORTC provisional/definitive as supported) | External identifiers (MONDO/Orphanet/MeSH/ICD) | Key supporting citations with PMID/DOI/URL if available |
|---|---|---|---|---|---|
| Primary cutaneous aggressive epidermotropic CD8-positive T-cell lymphoma | CD8+ AECTCL; PCAETCL; PCAE-TCL; pcAECyTCL | Primary cutaneous CD8+ aggressive epidermotropic cytotoxic T-cell lymphoma; Primary cutaneous aggressive epidermotropic cytotoxic CD8 positive T cell lymphoma; Primary cutaneous CD8+ aggressive epidermotropic T-cell lymphoma; Aggressive epidermotropic cutaneous CD8+ lymphoma; Primary cutaneous aggressive epidermotropic CD8+ cytotoxic T-cell lymphoma | Listed as a **provisional** entity in WHO-EORTC 2018 / recent cutaneous lymphoma classifications; described as a rare subtype of cutaneous T-cell lymphoma (CTCL) / primary cutaneous peripheral T-cell lymphoma. WHO-EORTC table lists frequency **<1%** and 5-year DSS **31%**. (willemze2019the2018update pages 13-16, kempf2019cutaneouslymphomas—anupdate pages 1-3, sundram2019cutaneouslymphoproliferativedisorders pages 1-2, willemze2019the2018update media 461b18ed) | MONDO/Orphanet/MeSH/ICD: **not found in retrieved sources**. Retrieved texts explicitly did not provide controlled-vocabulary identifiers. (willemze2019the2018update pages 13-16, loya2023probableprimarycutaneous pages 4-4, lupu2018anunusualpresentation pages 6-6, sundram2019cutaneouslymphoproliferativedisorders pages 1-2) | Willemze et al., *Blood* 2019. DOI: 10.1182/blood-2018-11-881268. URL: https://doi.org/10.1182/blood-2018-11-881268 (willemze2019the2018update pages 13-16, willemze2019the2018update media 461b18ed) |
| Primary cutaneous CD8+ aggressive epidermotropic cytotoxic T-cell lymphoma | PCAECTCL; PCAETL | Primary cutaneous aggressive epidermotropic CD8+ T-cell lymphoma; Primary cutaneous CD8+ aggressive epidermotropic cytotoxic T-cell lymphoma | Used in reviews/case reports as the same disease label; described as **provisional** in WHO-EORTC-based classification discussions. (deenen2019pitfallsindiagnosing pages 1-2, geller2018nktcelllymphomanasal pages 1-3, sundram2019cutaneouslymphoproliferativedisorders pages 1-2) | MONDO/Orphanet/MeSH/ICD: **not found in retrieved sources**. (loya2023probableprimarycutaneous pages 4-4, sundram2019cutaneouslymphoproliferativedisorders pages 1-2) | Deenen et al., *Br J Dermatol* 2019. DOI: 10.1111/bjd.17252. URL: https://doi.org/10.1111/bjd.17252; Geller et al., *Semin Cutan Med Surg* 2018. DOI: 10.12788/j.sder.2018.020. URL: https://doi.org/10.12788/j.sder.2018.020 (deenen2019pitfallsindiagnosing pages 1-2, geller2018nktcelllymphomanasal pages 1-3) |
| Primary cutaneous CD8+ aggressive epidermotropic cytotoxic T-cell lymphoma (molecular-study nomenclature) | pcAECyTCL | pcAETCL; primary cutaneous aggressive epidermotropic T-cell lymphoma | Molecular/genomic study uses this wording for the same rare aggressive CTCL entity; supports disease definition and biology, but retrieved context does not alter its provisional classification status from WHO-EORTC sources. (torres2021deregulationofjak2 pages 1-2, gallardo2022geneticsabnormalitieswith pages 1-2) | MONDO/Orphanet/MeSH/ICD: **not found in retrieved sources**. (willemze2019the2018update pages 13-16, loya2023probableprimarycutaneous pages 4-4) | Torres et al., *Haematologica* 2021. DOI: 10.3324/haematol.2020.274506. URL: https://doi.org/10.3324/haematol.2020.274506 (torres2021deregulationofjak2 pages 1-2, torres2021deregulationofjak2 pages 3-5, torres2021deregulationofjak2 pages 5-7) |


*Table: This table compiles the main disease names, abbreviations, classification notes, and the absence of standardized external identifiers in the retrieved sources for primary cutaneous aggressive epidermotropic CD8+ T-cell lymphoma. It is useful for harmonizing terminology across pathology, clinical, and molecular literature.*

### 1.4 Source type of information
Evidence in the retrieved corpus is predominantly **aggregated disease-level classification/registry summaries** (WHO–EORTC) plus **small case series and case reports**; prospective interventional data are scarce and repeatedly described as limited for this disease. (willemze2019the2018update pages 13-16, stuver2024throughthickand pages 1-2, cyrenne2018transplantationinthe pages 4-5)

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary driver biology (current evidence): JAK2/JAK–STAT pathway deregulation.** A whole-genome and RNA-sequencing study provides evidence that structural and mutational alterations converging on **JAK2 signaling** are central in this lymphoma, including recurrent **JAK2 fusions** and **loss of negative regulation via SH2B3**. (torres2021deregulationofjak2 pages 1-2, torres2021deregulationofjak2 pages 3-5)

**Direct quote (abstract evidence):** “*we show that mutually exclusive structural alterations involving JAK2 and SH2B3 predominantly underlie pcAECyTCL… Functional studies confirmed oncogenicity of JAK2 fusions… and their sensitivity to JAK inhibitor treatment*.” (Haematologica; published online 2021; DOI https://doi.org/10.3324/haematol.2020.274506). (torres2021deregulationofjak2 pages 1-2)

### 2.2 Risk factors
No validated environmental, infectious, or inherited germline predisposition factors were identified in the retrieved sources. The current literature base is dominated by somatic tumor profiling and clinicopathologic case descriptions. (torres2021deregulationofjak2 pages 1-2, deenen2019pitfallsindiagnosing pages 1-2)

### 2.3 Protective factors / gene–environment interactions
No protective factors or gene–environment interaction evidence was identified in the retrieved sources. (willemze2019the2018update pages 13-16)

---

## 3. Phenotypes
### 3.1 Clinical phenotypes (signs/symptoms)
Common presentation includes rapidly progressive **papules/plaques/nodules/tumors**, often **ulcerated or necrotic**, with potential extracutaneous spread (reported sites include lung, testis, CNS, oral mucosa in case-based literature). (loya2023probableprimarycutaneous pages 3-4, kempf2021cutaneoust‐celllymphomas—an pages 1-2)

In WHO–EORTC tabulations, the typical presentation is **ulcerating plaques, nodules and tumors**. (willemze2019the2018update media 461b18ed)

### 3.2 Age of onset, severity, and progression
This is generally described as **aggressive and rapidly progressive**, with poor survival. (kempf2021cutaneoust‐celllymphomas—an pages 1-2, loya2023probableprimarycutaneous pages 3-4)

### 3.3 Differential diagnosis / diagnostic pitfalls
It can clinically and histologically mimic inflammatory or indolent lymphoproliferative disorders; a documented pitfall is resemblance to **pyoderma gangrenosum** or **lymphomatoid papulosis (LyP) type D**, necessitating close clinicopathologic correlation and appropriate immunophenotyping. (deenen2019pitfallsindiagnosing pages 1-2)

### 3.4 Suggested HPO terms (for knowledge base annotation; not exhaustive)
- **Skin ulcer** (HP:0001050)
- **Cutaneous nodule** (HP:0100749)
- **Skin plaque** (HP:0200035)
- **Erythematous skin lesion** (HP:0010783)
- **Necrosis** (HP:0000966)
- **Central nervous system involvement** (phenotype depends on manifestation; e.g., seizures HP:0001250)

(These are ontology suggestions; the retrieved sources support the underlying clinical concepts but do not provide HPO mappings.) (loya2023probableprimarycutaneous pages 3-4, willemze2019the2018update media 461b18ed)

---

## 4. Genetic / Molecular Information
### 4.1 Recurrent somatic alterations (primary literature)
**High-resolution genomics (WGS/RNA-seq; n=12 tumors)** identified: (i) recurrent **JAK2 fusions** (e.g., **PCM1::JAK2**, **KHDRBS1::JAK2**, **TFG::JAK2**) and (ii) mutually exclusive focal inactivation of **SH2B3**, a negative regulator of JAK2 signaling. Together, alterations affecting the **JAK2–SH2B3 axis** predominated. (torres2021deregulationofjak2 pages 5-7, torres2021deregulationofjak2 pages 2-3)

Mechanistically, JAK2 fusion architecture is consistent with constitutive activation: the fusions join the JAK2 kinase domain to partner oligomerization domains, predicted to “self-oligo/dimerize and become activated without the need of cytokine-mediated receptor stimulation.” (torres2021deregulationofjak2 pages 3-5)

Additional recurrent cooperating lesions reported include frequent disruption of **CDKN2A/B** (9p21) and deletions of chromatin regulators (e.g., **ARID1A**, **EED**), consistent with cell-cycle checkpoint loss and chromatin dysregulation as cooperating hallmarks. (torres2021deregulationofjak2 pages 3-5, torres2021deregulationofjak2 pages 2-3)

A review summarizing genetic abnormalities across primary cutaneous lymphomas also reports recurrent targetable fusions in this entity, including **CAPRIN1::JAK2** and **SELENOI::ABL1**, reinforcing the theme of kinase-fusion-driven oncogenic signaling. (gallardo2022geneticsabnormalitieswith pages 7-9)

### 4.2 Functional consequences and therapeutic implications
Functional assays showed JAK2 fusions to be oncogenic and **sensitive to JAK inhibition**, supporting biomarker-driven consideration of JAK inhibitors (e.g., ruxolitinib) when an activated JAK2 axis is detected. (torres2021deregulationofjak2 pages 1-2, torres2021deregulationofjak2 pages 5-7)

### 4.3 Suggested GO biological process terms (mechanism annotation)
- **JAK-STAT cascade** (GO:0007259)
- **Regulation of cytokine-mediated signaling pathway** (GO:0001959)
- **Positive regulation of cell population proliferation** (GO:0008284)
- **Cell cycle checkpoint** (GO:0000075)
- **NF-kappaB signaling** (e.g., GO:0043122)

### 4.4 Suggested cell types (Cell Ontology; mechanism annotation)
- **CD8-positive, alpha-beta T cell** (CL:0000625)
- **Cytotoxic T cell** (CL:0000910)

(These are ontology suggestions aligned to the immunophenotype and lineage reported in WHO–EORTC tables and molecular studies.) (willemze2019the2018update media 461b18ed, willemze2019the2018update pages 13-16)

---

## 5. Environmental Information
No specific environmental, lifestyle, occupational, or infectious triggers were identified in the retrieved sources for this entity. (willemze2019the2018update pages 13-16)

---

## 6. Mechanism / Pathophysiology
### 6.1 Causal chain (integrated model)
1. **Initiating oncogenic lesions:** recurrent **JAK2 gene fusions** or loss of negative regulation via **SH2B3** produce persistent JAK2 signaling. (torres2021deregulationofjak2 pages 3-5, torres2021deregulationofjak2 pages 5-7)
2. **Signal transduction and transcriptional programs:** transcriptome analysis shows upregulation of **JAK2 signaling**, **cell-cycle programs**, and **TNF-α/NF-κB signaling**, plus a high inflammatory response signature. (torres2021deregulationofjak2 pages 1-2, torres2021deregulationofjak2 pages 5-7)
3. **Tumor expansion and tissue phenotype:** malignant CD8+ cytotoxic T cells infiltrate the epidermis (marked epidermotropism), producing clinically aggressive ulcerating plaques/tumors with capacity for extracutaneous dissemination. (willemze2019the2018update media 461b18ed, loya2023probableprimarycutaneous pages 3-4)

### 6.2 Molecular profiling technologies
The most disease-specific mechanistic evidence in the retrieved set comes from **whole-genome sequencing and RNA sequencing** in pcAECyTCL tumors. (torres2021deregulationofjak2 pages 1-2, torres2021deregulationofjak2 pages 2-3)

---

## 7. Anatomical Structures Affected
### 7.1 Organ/tissue level
- **Primary site:** skin (cutaneous lymphoma by definition; no extracutaneous disease at diagnosis in classification frameworks). (willemze2019the2018update pages 13-16)
- **Clinical morphology:** ulcerating plaques/nodules/tumors. (willemze2019the2018update media 461b18ed)

### 7.2 Suggested UBERON terms
- **Skin of body** (UBERON:0002097)
- **Epidermis** (UBERON:0001003)

---

## 8. Temporal Development
### 8.1 Onset and progression
The disease is described as having **rapid onset** of necrotic/ulcerated plaques and tumors and an aggressive course. (kempf2021cutaneoust‐celllymphomas—an pages 1-2)

---

## 9. Inheritance and Population
### 9.1 Epidemiology (rarity)
WHO–EORTC tabulated frequency is **<1%** among primary cutaneous lymphomas in registry-based summaries. (willemze2019the2018update media 461b18ed)

A 2023 case report summarizes the rarity as “about 1% of cutaneous T-cell lymphomas” and notes that “slightly more than 30 cases” had been reported in the literature at that time (case-report-level secondary summary). (loya2023probableprimarycutaneous pages 3-4)

### 9.2 Inheritance
No germline inheritance pattern was identified in the retrieved sources; available evidence supports a predominantly **somatic** oncogenic process (e.g., JAK2 fusions, SH2B3 deletions). (torres2021deregulationofjak2 pages 3-5)

---

## 10. Diagnostics
### 10.1 Diagnostic approach (clinicopathologic)
Diagnosis relies on combined clinical and histopathologic evaluation because of overlap with other CD8+ cutaneous lymphomas and inflammatory mimics. (lupu2018anunusualpresentation pages 6-6, deenen2019pitfallsindiagnosing pages 1-2)

**WHO–EORTC immunophenotype snapshot (Table data):** CD3+, CD4−, CD8+, cytotoxic proteins positive, CD56−, EBV−, lineage αβ T-cell. (willemze2019the2018update media 461b18ed)

### 10.2 Biomarkers and molecular tests
Given the recurrent **JAK2 fusions** and SH2B3 alterations, contemporary molecular profiling (e.g., RNA-seq fusion detection and/or DNA-based profiling) can identify actionable lesions and support classification in challenging cases. (torres2021deregulationofjak2 pages 5-7, gallardo2022geneticsabnormalitieswith pages 7-9)

### 10.3 Differential diagnosis (examples supported in retrieved sources)
- Pyoderma gangrenosum (clinical mimic)
- Lymphomatoid papulosis type D
- CD8+ mycosis fungoides
- Cutaneous γδ T-cell lymphoma
- Primary cutaneous peripheral T-cell lymphoma, NOS

(deenen2019pitfallsindiagnosing pages 1-2, loya2023probableprimarycutaneous pages 3-4)

---

## 11. Outcome / Prognosis
### 11.1 Registry-level survival statistics
WHO–EORTC table data report **5-year disease-specific survival (DSS) ~31%** for this provisional entity. (willemze2019the2018update media 461b18ed)

### 11.2 Case-based prognosis estimates
A 2023 case report states a “survival time of 32 months from the commencement of skin lesions” (secondary summary of prior literature). (loya2023probableprimarycutaneous pages 3-4)

---

## 12. Treatment
### 12.1 Current practice patterns and real-world implementations
Because prospective trials are scarce, real-world management often follows aggressive lymphoma paradigms and institutional experience.

**Systemic chemotherapy and radiation:** A multi-institution case series reported use of multiagent regimens (e.g., CHOP, EPOCH, gemcitabine-based regimens, ICE/DHAP), plus radiotherapy including localized XRT and total skin electron beam therapy (TSEBT). (cyrenne2018transplantationinthe pages 4-5, cyrenne2018transplantationinthe pages 7-9)

**Transplantation:** The same series emphasizes that durable responses were observed mainly with **allogeneic stem cell transplantation (allo-SCT)** or **brentuximab vedotin** in selected settings. (cyrenne2018transplantationinthe pages 4-5)

**Targeted / biomarker-driven therapy:** Genomic evidence supporting JAK2 pathway targeting has enabled off-label or investigational use of **JAK inhibitors** (e.g., ruxolitinib), including use after relapse post-transplant in a 2023 case report. (sopena2023hematopoieticstemcell pages 2-3, torres2021deregulationofjak2 pages 1-2)

### 12.2 Expert opinion (2023–2024 priority)
A 2024 ASH Hematology expert review stresses that PCAETCL has “few prospective studies to guide treatment,” and that “recent genomic insights… such as the presence of JAK2 fusions in PCAETCL… have created options for new biomarker-driven strategies.” (Hematology; Dec 2024; DOI https://doi.org/10.1182/hematology.2024000529). (stuver2024throughthickand pages 1-2)

### 12.3 Treatment outcomes and statistics (available)
In the 2018 case series, outcomes included multiple complete responses in individuals receiving allo-SCT and brentuximab; at last follow-up, transplanted patients were alive, with median follow-up around 40 months (range reported). (cyrenne2018transplantationinthe pages 4-5)

A 2023 case report reiterates poor baseline prognosis (“5-year survival rate of less than 40%”) and describes multi-line therapy culminating in allo-HSCT, followed by relapse treated with ruxolitinib. (sopena2023hematopoieticstemcell pages 1-2, sopena2023hematopoieticstemcell pages 2-3)

### 12.4 MAXO terms (treatment action ontology; suggested)
- **Chemotherapy** (NCIT:C15986)
- **Radiation therapy** (MAXO:0000014)
- **Allogeneic hematopoietic stem cell transplantation** (MAXO term; concept supported by clinical text)
- **Janus kinase inhibitor therapy** (MAXO concept)

(These are ontology suggestions; supporting evidence for modalities is in cited clinical series/case reports.) (cyrenne2018transplantationinthe pages 7-9, sopena2023hematopoieticstemcell pages 2-3)

### 12.5 Ongoing clinical trials / registries (not disease-specific but relevant to cytotoxic/T-cell lymphoma populations)
- **NCT05475925** (Phase 1/2; cytotoxic lymphomas / large granular lymphocytic leukemia; recruiting). (tool-retrieved trial record; not PCAETCL-specific) (stuver2024throughthickand pages 1-2)
- **NCT05978141** (Observational registry for people with T-cell lymphoma; recruiting). (stuver2024throughthickand pages 1-2)

---

## 13. Prevention
No primary prevention strategy is supported in the retrieved sources. Secondary prevention is limited to **early recognition and accurate diagnosis**, given frequent diagnostic pitfalls and aggressive progression. (deenen2019pitfallsindiagnosing pages 1-2, lupu2018anunusualpresentation pages 6-6)

---

## 14. Other Species / Natural Disease
No naturally occurring veterinary/other-species analog was identified in the retrieved sources. (willemze2019the2018update pages 13-16)

---

## 15. Model Organisms
No dedicated in vivo model organism systems were identified in the retrieved sources. Mechanistic functional work in the key molecular study used cell-based assays to validate oncogenicity of JAK2 fusions and their inhibitor sensitivity. (torres2021deregulationofjak2 pages 5-7)

---

## Notes on evidence gaps
1. **Standard identifiers (MONDO/Orphanet/ICD/MeSH)** were not present in the retrieved full-text excerpts; mapping will require dedicated queries to those ontology resources using the synonyms listed. (willemze2019the2018update pages 13-16, loya2023probableprimarycutaneous pages 4-4)
2. Many clinical outcome statistics remain based on **registry summaries and small case series**, reflecting the rarity and the limited prospective trial evidence base. (stuver2024throughthickand pages 1-2, cyrenne2018transplantationinthe pages 4-5)


References

1. (deenen2019pitfallsindiagnosing pages 1-2): N. J. Deenen, L. Koens, E. H. Jaspars, M. Vermeer, R. Willemze, M. D. de Rie, and M. Bekkenk. Pitfalls in diagnosing primary cutaneous aggressive epidermotropic cd8+ t‐cell lymphoma. British Journal of Dermatology, 180:411-412, Oct 2019. URL: https://doi.org/10.1111/bjd.17252, doi:10.1111/bjd.17252. This article has 13 citations and is from a highest quality peer-reviewed journal.

2. (geller2018nktcelllymphomanasal pages 1-3): Shamir Geller, Patricia L Myskowski, and Melissa Pulitzer. Nk/t-cell lymphoma, nasal type, γδ t-cell lymphoma, and cd8-positive epidermotropic t-cell lymphoma—clinical and histopathologic features, differential diagnosis, and treatment. Seminars in Cutaneous Medicine and Surgery, 37:30-38, Mar 2018. URL: https://doi.org/10.12788/j.sder.2018.020, doi:10.12788/j.sder.2018.020. This article has 53 citations and is from a peer-reviewed journal.

3. (willemze2019the2018update pages 13-16): Rein Willemze, Lorenzo Cerroni, Werner Kempf, Emilio Berti, Fabio Facchetti, Steven H. Swerdlow, and Elaine S. Jaffe. The 2018 update of the who-eortc classification for primary cutaneous lymphomas. Blood, 133 16:1703-1714, Apr 2019. URL: https://doi.org/10.1182/blood-2018-11-881268, doi:10.1182/blood-2018-11-881268. This article has 1674 citations and is from a highest quality peer-reviewed journal.

4. (willemze2019the2018update media 461b18ed): Rein Willemze, Lorenzo Cerroni, Werner Kempf, Emilio Berti, Fabio Facchetti, Steven H. Swerdlow, and Elaine S. Jaffe. The 2018 update of the who-eortc classification for primary cutaneous lymphomas. Blood, 133 16:1703-1714, Apr 2019. URL: https://doi.org/10.1182/blood-2018-11-881268, doi:10.1182/blood-2018-11-881268. This article has 1674 citations and is from a highest quality peer-reviewed journal.

5. (loya2023probableprimarycutaneous pages 4-4): Marcela Velarde Loya, Monica G Millan Reza, Mariana Olaya Cordova, and Zaira D Chavéz López. Probable primary cutaneous cd8+ aggressive epidermotropic cytotoxic t-cell lymphoma: a case report of a diagnostic challenge. Cureus, Aug 2023. URL: https://doi.org/10.7759/cureus.44375, doi:10.7759/cureus.44375. This article has 1 citations.

6. (sundram2019cutaneouslymphoproliferativedisorders pages 1-2): Uma Sundram. Cutaneous lymphoproliferative disorders: what’s new in the revised 4th edition of the world health organization (who) classification of lymphoid neoplasms. Advances in Anatomic Pathology, 26:93-113, Mar 2019. URL: https://doi.org/10.1097/pap.0000000000000208, doi:10.1097/pap.0000000000000208. This article has 21 citations and is from a domain leading peer-reviewed journal.

7. (kempf2019cutaneouslymphomas—anupdate pages 1-3): Werner Kempf, Anne‐Katrin Zimmermann, and Christina Mitteldorf. Cutaneous lymphomas—an update 2019. Hematological Oncology, 37:43-47, Jun 2019. URL: https://doi.org/10.1002/hon.2584, doi:10.1002/hon.2584. This article has 110 citations and is from a peer-reviewed journal.

8. (lupu2018anunusualpresentation pages 6-6): M Lupu, V Voiculescu, and L Papagheorghe. An unusual presentation of primary cutaneous aggressive epidermotropic cd8+ t cell lymphoma. Unknown journal, 2018.

9. (torres2021deregulationofjak2 pages 1-2): Armando N. Bastidas Torres, Davy Cats, Jacoba J. Out-Luiting, Daniele Fanoni, Hailiang Mei, Luigia Venegoni, Rein Willemze, Maarten H. Vermeer, Emilio Berti, and Cornelis P. Tensen. Deregulation of jak2 signaling underlies primary cutaneous cd8+ aggressive epidermotropic cytotoxic t-cell lymphoma. Haematologica, 107:702-714, Apr 2021. URL: https://doi.org/10.3324/haematol.2020.274506, doi:10.3324/haematol.2020.274506. This article has 61 citations.

10. (gallardo2022geneticsabnormalitieswith pages 1-2): Fernando Gallardo and Ramon M. Pujol. Genetics abnormalities with clinical impact in primary cutaneous lymphomas. Cancers, 14:4972, Oct 2022. URL: https://doi.org/10.3390/cancers14204972, doi:10.3390/cancers14204972. This article has 22 citations.

11. (torres2021deregulationofjak2 pages 3-5): Armando N. Bastidas Torres, Davy Cats, Jacoba J. Out-Luiting, Daniele Fanoni, Hailiang Mei, Luigia Venegoni, Rein Willemze, Maarten H. Vermeer, Emilio Berti, and Cornelis P. Tensen. Deregulation of jak2 signaling underlies primary cutaneous cd8+ aggressive epidermotropic cytotoxic t-cell lymphoma. Haematologica, 107:702-714, Apr 2021. URL: https://doi.org/10.3324/haematol.2020.274506, doi:10.3324/haematol.2020.274506. This article has 61 citations.

12. (torres2021deregulationofjak2 pages 5-7): Armando N. Bastidas Torres, Davy Cats, Jacoba J. Out-Luiting, Daniele Fanoni, Hailiang Mei, Luigia Venegoni, Rein Willemze, Maarten H. Vermeer, Emilio Berti, and Cornelis P. Tensen. Deregulation of jak2 signaling underlies primary cutaneous cd8+ aggressive epidermotropic cytotoxic t-cell lymphoma. Haematologica, 107:702-714, Apr 2021. URL: https://doi.org/10.3324/haematol.2020.274506, doi:10.3324/haematol.2020.274506. This article has 61 citations.

13. (stuver2024throughthickand pages 1-2): Robert Stuver and Steven M. Horwitz. Through thick and thin: confronting the aggressive cutaneous t-cell lymphomas. Hematology, 2024:62-68, Dec 2024. URL: https://doi.org/10.1182/hematology.2024000529, doi:10.1182/hematology.2024000529. This article has 0 citations and is from a peer-reviewed journal.

14. (cyrenne2018transplantationinthe pages 4-5): Benoit M. Cyrenne, Juliet Fraser Gibson, Antonio Subtil, Michael Girardi, Iris Isufi, Stuart Seropian, and Francine Foss. Transplantation in the treatment of primary cutaneous aggressive epidermotropic cytotoxic cd8‐positive t‐cell lymphoma. Clinical Lymphoma, Myeloma & Leukemia, 18:e85–e93, Jan 2018. URL: https://doi.org/10.1016/j.clml.2017.11.004, doi:10.1016/j.clml.2017.11.004. This article has 21 citations.

15. (loya2023probableprimarycutaneous pages 3-4): Marcela Velarde Loya, Monica G Millan Reza, Mariana Olaya Cordova, and Zaira D Chavéz López. Probable primary cutaneous cd8+ aggressive epidermotropic cytotoxic t-cell lymphoma: a case report of a diagnostic challenge. Cureus, Aug 2023. URL: https://doi.org/10.7759/cureus.44375, doi:10.7759/cureus.44375. This article has 1 citations.

16. (kempf2021cutaneoust‐celllymphomas—an pages 1-2): Werner Kempf and Christina Mitteldorf. Cutaneous t‐cell lymphomas—an update 2021. Hematological Oncology, 39:46-51, Jun 2021. URL: https://doi.org/10.1002/hon.2850, doi:10.1002/hon.2850. This article has 106 citations and is from a peer-reviewed journal.

17. (torres2021deregulationofjak2 pages 2-3): Armando N. Bastidas Torres, Davy Cats, Jacoba J. Out-Luiting, Daniele Fanoni, Hailiang Mei, Luigia Venegoni, Rein Willemze, Maarten H. Vermeer, Emilio Berti, and Cornelis P. Tensen. Deregulation of jak2 signaling underlies primary cutaneous cd8+ aggressive epidermotropic cytotoxic t-cell lymphoma. Haematologica, 107:702-714, Apr 2021. URL: https://doi.org/10.3324/haematol.2020.274506, doi:10.3324/haematol.2020.274506. This article has 61 citations.

18. (gallardo2022geneticsabnormalitieswith pages 7-9): Fernando Gallardo and Ramon M. Pujol. Genetics abnormalities with clinical impact in primary cutaneous lymphomas. Cancers, 14:4972, Oct 2022. URL: https://doi.org/10.3390/cancers14204972, doi:10.3390/cancers14204972. This article has 22 citations.

19. (cyrenne2018transplantationinthe pages 7-9): Benoit M. Cyrenne, Juliet Fraser Gibson, Antonio Subtil, Michael Girardi, Iris Isufi, Stuart Seropian, and Francine Foss. Transplantation in the treatment of primary cutaneous aggressive epidermotropic cytotoxic cd8‐positive t‐cell lymphoma. Clinical Lymphoma, Myeloma & Leukemia, 18:e85–e93, Jan 2018. URL: https://doi.org/10.1016/j.clml.2017.11.004, doi:10.1016/j.clml.2017.11.004. This article has 21 citations.

20. (sopena2023hematopoieticstemcell pages 2-3): L Sopena, M Merchante, MA Alcácera, and I Varela. Hematopoietic stem cell transplantation in primary cutaneous aggressive epidermotropic cd8+ t-cell lymphoma: a case report. Journal of Clinical Images and Medical Case Reports, Oct 2023. URL: https://doi.org/10.52768/2766-7820/2646, doi:10.52768/2766-7820/2646. This article has 0 citations.

21. (sopena2023hematopoieticstemcell pages 1-2): L Sopena, M Merchante, MA Alcácera, and I Varela. Hematopoietic stem cell transplantation in primary cutaneous aggressive epidermotropic cd8+ t-cell lymphoma: a case report. Journal of Clinical Images and Medical Case Reports, Oct 2023. URL: https://doi.org/10.52768/2766-7820/2646, doi:10.52768/2766-7820/2646. This article has 0 citations.
