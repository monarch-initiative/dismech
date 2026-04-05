---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T15:38:29.543299'
end_time: '2026-04-04T15:46:25.199445'
duration_seconds: 475.66
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Onchocerciasis
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 55
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Onchocerciasis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Onchocerciasis** covering all of the
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
- **Disease Name:** Onchocerciasis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Onchocerciasis** covering all of the
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


## Comprehensive Disease Characteristics Report: Onchocerciasis (River Blindness)

### Executive summary (current understanding; 2023–2024 emphasis)
Onchocerciasis is a vector-borne filarial disease caused by *Onchocerca volvulus* and transmitted by *Simulium* blackflies. It is classically termed “river blindness” because transmission occurs near fast-flowing rivers where blackflies breed, and ocular inflammation can lead to visual impairment and blindness. Contemporary work emphasizes that the most common clinical burden is often inflammatory/degenerative skin disease (severe pruritus and dermatitis), and that neurological sequelae—especially onchocerciasis-associated epilepsy (OAE) and nodding syndrome—are increasingly recognized as major contributors to disability and premature mortality in high-transmission foci. Recent programmatic advances include large-scale stop–mass drug administration (MDA) decisions using WHO elimination thresholds (Nigeria, effective Jan 2023), while multiple foci show recrudescence or persistent transmission. New tools (more-sensitive Ov16 rapid tests; anti-*Wolbachia* short-course regimens; moxidectin deployment strategies; and late-stage drug candidates such as emodepside) are being developed to accelerate elimination where ivermectin alone is insufficient. (kamgno2025vectorbornehelminthiasesa pages 24-27, stapley2024modellingonchocerciasisassociatedepilepsy pages 1-2, kura2023canmassdrug pages 1-2, ityonzughul2024theinterruptionof pages 2-5, karunakaran2023filariasisresearch– pages 9-10)

---

## 1. Disease information

### 1.1 Concise overview
Onchocerciasis (“river blindness”) is a neglected tropical disease caused by infection with the filarial nematode *Onchocerca volvulus* and transmitted to humans by bites of infected blackflies (*Simulium* spp.). (ouedraogo2024effectsoffive pages 1-2, stapley2024modellingonchocerciasisassociatedepilepsy pages 1-2, kura2023canmassdrug pages 1-2)

Recent expert synthesis stresses that despite the name “river blindness,” “the commonest clinical presentation is an inflammatory, degenerative dermal disease,” with severe itching and diverse skin changes; ocular disease arises from microfilariae and inflammatory responses and can cause blindness. (kamgno2025vectorbornehelminthiasesa pages 24-27)

### 1.2 Key identifiers (ontology and coding)
*Limitation of current tool-retrieved evidence:* none of the retrieved full texts contained explicit ICD-10/ICD-11 codes, MeSH descriptor IDs, Orphanet IDs, or MONDO IDs. Therefore, these identifiers cannot be reliably populated from the current evidence set without direct lookup from the relevant ontology/code systems.

### 1.3 Synonyms / alternative names
- River blindness (common name) (ouedraogo2024effectsoffive pages 1-2, stapley2024modellingonchocerciasisassociatedepilepsy pages 1-2)
- Onchocerciasis (standard medical name) (ouedraogo2024effectsoffive pages 1-2)

### 1.4 Evidence source type
This report is derived from aggregated disease-level resources and peer-reviewed studies (systematic reviews, modelling studies, and field epidemiology/program evaluations), not individual EHR case reports. (ouedraogo2024effectsoffive pages 1-2, stapley2024modellingonchocerciasisassociatedepilepsy pages 1-2, ityonzughul2024theinterruptionof pages 2-5)

---

## 2. Etiology

### 2.1 Disease causal factors
- **Infectious cause:** *Onchocerca volvulus* (filarial nematode). (ouedraogo2024effectsoffive pages 1-2, stapley2024modellingonchocerciasisassociatedepilepsy pages 1-2)
- **Vector:** blackflies (*Simulium* spp.; e.g., *Simulium damnosum* s.l.). (ouedraogo2024effectsoffive pages 1-2, stapley2024modellingonchocerciasisassociatedepilepsy pages 1-2)

### 2.2 Risk factors (human, environmental)
- **Environmental exposure to blackfly breeding sites (riverine/rapids):** strong epidemiologic linkage to fast-flowing rivers where vectors breed; high epilepsy prevalence clusters near rivers in South Sudan foci. (amaral2025highepilepsyprevalence pages 1-2, jada2023effectofonchocerciasis pages 1-3)
- **High microfilarial load:** retrospective cohort evidence incorporated into modelling indicates a dose–response relationship between childhood microfilarial load and later epilepsy risk. (stapley2024modellingonchocerciasisassociatedepilepsy pages 1-2)
- **Programmatic risk factor (continued transmission):** suboptimal MDA coverage and systematic non-adherence are important drivers of ongoing transmission and slower elimination, motivating modelling of coverage/adherence scenarios. (kura2023canmassdrug pages 1-2)

### 2.3 Protective factors
- **High-coverage, sustained preventive chemotherapy (ivermectin MDA/CDTI):** multi-year/decade preventive chemotherapy reduces infection and morbidity and can interrupt transmission under defined criteria in some settings. (ityonzughul2024theinterruptionof pages 2-5, ouedraogo2024effectsoffive pages 1-2)
- **Strengthened elimination programs + vector control:** in Maridi (South Sudan), strengthened control (biannual CDTI plus “Slash and Clear” vector control) was associated with large reductions in epilepsy and nodding syndrome incidence over time. (jada2023effectofonchocerciasis pages 1-3)

### 2.4 Gene–environment interactions
No robust human host genetic susceptibility/protection loci were identified within the retrieved evidence set (2023–2026). The dominant “interaction” described in this literature is environmental exposure (vector biting intensity near breeding sites) modulated by intervention intensity (MDA and vector control). (amaral2025highepilepsyprevalence pages 1-2, jada2023effectofonchocerciasis pages 1-3)

---

## 3. Phenotypes (clinical spectrum)

### 3.1 Core clinical phenotypes
Recent authoritative synthesis describes:
- **Cutaneous disease:** “intolerable itching, papular lesions, pigmentary change, skin thickening and premature skin ageing.” (kamgno2025vectorbornehelminthiasesa pages 24-27)
- **Ocular disease:** microfilariae and inflammation can cause visual impairment and blindness. (kamgno2025vectorbornehelminthiasesa pages 24-27)
- **Neurologic disease:** increasing evidence links onchocerciasis to epilepsy syndromes including nodding syndrome and OAE, with onset typically in childhood/adolescence. (stapley2024modellingonchocerciasisassociatedepilepsy pages 1-2)

### 3.2 Neurologic phenotype frequencies and burden (recent field data)
- **South Sudan (5 counties; 2021–2024 surveys):** age-/sex-standardized epilepsy prevalence 4.1% (range 2.3–7.1%); probable nodding syndrome prevalence 1.5% (0.6–2.2%). Anti-Ov16 seroprevalence in children 3–9 years was 23.3% (1.4–44.1%). (amaral2025highepilepsyprevalence pages 1-2)
- **Wulu County, South Sudan (2024):** epilepsy prevalence 4.1% (55/1,355); 20% had nodding seizures; annual incidence 147.6/100,000. Ov16 seroprevalence in children 3–9 years was 15.1% (n=119), reaching 30.9% in the village with 7.1% epilepsy prevalence. (fodjo2024epidemiologyofepilepsy pages 1-3)

### 3.3 Phenotype ontology suggestions (HPO)
*Note:* HPO mappings below are suggested for knowledge-base normalization; they were not explicitly provided in the retrieved articles.
- Pruritus → **HP:0000989**
- Dermatitis/skin rash (papular lesions) → **HP:0000964** (Eczema) / **HP:0000988** (Skin rash)
- Skin hypopigmentation (depigmentation) → **HP:0001010**
- Visual impairment → **HP:0000505**
- Blindness → **HP:0000618**
- Epileptic seizures → **HP:0001250**
- Nodding seizures (nodding syndrome; use as seizure phenotype) → **HP:0001270** (Abnormality of movement) is non-specific; consider custom annotation + seizure subtype in local schema.

### 3.4 Quality of life impact
Direct QoL instrument outcomes (EQ-5D/SF-36) were not captured in the retrieved evidence set. Indirect but strong impact is supported by high epilepsy-associated mortality and young age at death in endemic foci (below). (amaral2025highepilepsyprevalence pages 1-2, fodjo2024epidemiologyofepilepsy pages 1-3)

---

## 4. Genetic / molecular information

### 4.1 Causal genes / pathogenic variants (human)
Not applicable in the Mendelian sense: onchocerciasis is an infectious disease caused by a helminth parasite. No human causal variants were identified in the retrieved evidence set.

### 4.2 Parasite and endosymbiont biology relevant to pathogenesis
**Anti-*Wolbachia* treatment evidence implies key biological dependence of *O. volvulus* on *Wolbachia*** (bacterial endosymbiont) and supports macrofilaricidal strategies by depleting *Wolbachia*.
- Doxycycline regimens (anti-*Wolbachia*) show strong macrofilaricidal/embryogenesis effects: the review reports that 200 mg/day for six weeks produced “~96% Wolbachia loss and 99% microfilaria reduction,” and that “6-week doxycycline followed by a single ivermectin+albendazole dose gave an 89% macrofilaricidal effect at 2 years.” (karunakaran2023filariasisresearch– pages 9-10)

### 4.3 GO / CL suggestions (mechanism annotation)
*Limitations:* detailed cytokine/cellular mechanism text was not captured in the retrieved evidence; therefore, ontology suggestions are conservative.
- Inflammatory response → **GO:0006954**
- Response to bacterium (for *Wolbachia* contributions) → **GO:0009617**
- Eosinophil activation (typical for helminths) → **GO:0043300** (approximate; verify with targeted immunology sources)
- Key immune cell types (CL): T cell **CL:0000084**, B cell **CL:0000236**, macrophage **CL:0000235**, eosinophil **CL:0000771**

---

## 5. Environmental information

### 5.1 Primary environmental driver
- Exposure to blackfly habitats near fast-flowing rivers/rapids; association with epilepsy burden and transmission metrics near breeding sites is repeatedly documented in South Sudan foci. (amaral2025highepilepsyprevalence pages 1-2, jada2023effectofonchocerciasis pages 1-3)

### 5.2 Lifestyle factors
No specific lifestyle risk or protective factors (diet, smoking, etc.) were identified in the retrieved evidence set.

---

## 6. Mechanism / pathophysiology (current understanding)

### 6.1 Causal chain (high-level)
1) Infective blackfly bite → transmission of *O. volvulus* to human host. (ouedraogo2024effectsoffive pages 1-2, stapley2024modellingonchocerciasisassociatedepilepsy pages 1-2)
2) Adult worms establish and produce microfilariae → microfilariae migrate through skin and ocular tissues, provoking inflammatory disease. (kamgno2025vectorbornehelminthiasesa pages 24-27)
3) Clinical outcomes: chronic pruritic dermatoses; ocular inflammation/vision loss; and in high-transmission settings, increased risk of epilepsy syndromes (OAE/nodding syndrome) associated with microfilarial burden in childhood. (kamgno2025vectorbornehelminthiasesa pages 24-27, stapley2024modellingonchocerciasisassociatedepilepsy pages 1-2)

### 6.2 OAE mechanistic framing (evidence level)
- **Epidemiological dose–response evidence:** modelling integrates retrospective cohort data linking childhood microfilarial load to later epilepsy, and reproduces observed epilepsy prevalence/incidence in Cameroon. (stapley2024modellingonchocerciasisassociatedepilepsy pages 1-2)
- **Mechanistic uncertainty:** multiple sources explicitly highlight that the exact pathophysiological mechanism of epilepsy association remains unresolved, despite strong epidemiologic evidence. (stapley2024modellingonchocerciasisassociatedepilepsy pages 1-2)

---

## 7. Anatomical structures affected

### 7.1 Organ level
- Skin (primary): chronic inflammatory/degenerative dermal disease. (kamgno2025vectorbornehelminthiasesa pages 24-27)
- Eye (primary): anterior chamber microfilariae and inflammatory ocular adverse events after treatment; visual impairment/blindness. (kamgno2025vectorbornehelminthiasesa pages 24-27, kanza2024onchocercavolvulusmicrofilariae pages 1-2)
- Nervous system (secondary/complication): epilepsy syndromes (OAE; nodding syndrome). (stapley2024modellingonchocerciasisassociatedepilepsy pages 1-2, amaral2025highepilepsyprevalence pages 1-2)

### 7.2 UBERON suggestions
- Skin → **UBERON:0002097**
- Eye → **UBERON:0000970**
- Brain → **UBERON:0000955**

---

## 8. Temporal development (onset and progression)

### 8.1 OAE onset window
OAE typically begins between ages **3–18 years** in previously healthy children in highly endemic areas. (stapley2024modellingonchocerciasisassociatedepilepsy pages 1-2, bhattacharyya2023onchocerciasisassociatedepilepsyin pages 1-2)

### 8.2 Chronicity
Onchocerciasis is typically a chronic infection requiring sustained interventions (often ≥10–15 years) to interrupt transmission in endemic foci, consistent with field-program knowledge and recent field studies. (ouedraogo2024effectsoffive pages 1-2, fodjo2024epidemiologyofepilepsy pages 1-3)

---

## 9. Inheritance and population

### 9.1 Epidemiology / burden statistics (recent)
- GBD-informed context (as summarized in recent modelling work): ~20 million infected and ~1.26 million DALYs (GBD 2021 attribution) and at least 248 million people in SSA requiring MDA (2024 estimate cited). (dixon2026modellingofonchocerciasisassociated pages 1-5)
- OAE/epilepsy burden in endemic foci: epilepsy prevalence 4.1% (South Sudan multi-county study) with strong association to ongoing transmission (Ov16 seroprevalence). (amaral2025highepilepsyprevalence pages 1-2)

### 9.2 Geographic distribution
- Endemic across many sub-Saharan African countries; some evidence indicates elimination verified in only a small fraction of foci as of 2025 (as summarized in recent modelling context). (dixon2026modellingofonchocerciasisassociated pages 1-5)

---

## 10. Diagnostics

### 10.1 Core diagnostic modalities used in elimination programs
- **Ov16 serology (ELISA and RDTs):** used for mapping/surveillance and stop-MDA decisions in children. (ityonzughul2024theinterruptionof pages 2-5, norman2026assessingdiagnosticaccuracy pages 3-5)
- **Skin snip microscopy / PCR (O-150):** direct detection of microfilariae or parasite DNA; used for confirmation and in some studies as reference/comparator. (ityonzughul2024theinterruptionof pages 1-2, otabil2025usabilityacceptabilityand pages 1-6)
- **Entomological monitoring:** pooled PCR of blackfly heads for O-150 DNA to estimate infective fly prevalence. (ityonzughul2024theinterruptionof pages 1-2)

### 10.2 WHO-aligned stopping-MDA thresholds (programmatic decision rules)
From the Nigeria stop-treatment decision paper:
- Epidemiological criterion: Ov16 seroprevalence in children 5–9 years with **95% UCL <0.1%** using surveys of **≥3,000** children. (ityonzughul2024theinterruptionof pages 1-2)
- Entomological criterion: infective fly prevalence by O-150 PCR **<0.05% with 95% confidence** among **≥6,000** flies, or annual transmission potential (ATP) **<20 with 95% confidence** if fewer flies are analyzed. (ityonzughul2024theinterruptionof pages 1-2)

### 10.3 Diagnostic test performance targets and recent evaluations
A recent latent-class evaluation summarized WHO target product profile (TPP) thresholds for Ov16 RDTs:
- **Mapping:** sensitivity ≥60% and specificity ≥99.8%
- **Stop-MDA:** sensitivity ≥89% and specificity ≥99.8% (norman2026assessingdiagnosticaccuracy pages 3-5)

In the same evaluation, the GADx Ov16 rapid test achieved posterior median sensitivity ~92% but specificities (highest median ~98.8%) remained below the 99.8% benchmark, implying that confirmatory/combined strategies may still be required for high-stakes stop-MDA decisions. (norman2026assessingdiagnosticaccuracy pages 1-3, norman2026assessingdiagnosticaccuracy pages 7-11)

### 10.4 Real-world implementation: usability and cost
In Ghana, an Ov16 SD BIOLINE RDT surveillance study reported substantially higher acceptability than skin snips and a cost model of **US$24/person** for Ov16 RDT vs **US$74/person** for skin-snip microscopy (standardized to testing 400 participants). (otabil2025usabilityacceptabilityand pages 1-6)

---

## 11. Outcomes / prognosis

### 11.1 Epilepsy-associated excess mortality in endemic regions
A large multi-county study in South Sudan reported markedly elevated mortality among persons with suspected epilepsy compared to individuals without epilepsy:
- Standardized mortality rates: **67.6/1,000 person-years** (suspected epilepsy) vs **9.0/1,000 person-years** (without epilepsy)
- Standardized mortality ratio (SMR): **6.9** (95% CI 5.9–8.0)
- Median age at death: **20 years** (epilepsy) vs **38 years** (without epilepsy) (amaral2025highepilepsyprevalence pages 1-2)

### 11.2 Modeled prevention impact
EPIONCHO-IBM modelling calibrated to Cameroon cohort data predicted epilepsy prevalence and incidence consistent with observed data and suggested that long-term intensified ivermectin strategies (e.g., biannual MDA at high coverage) could eliminate OAE in hyperendemic settings. (stapley2024modellingonchocerciasisassociatedepilepsy pages 1-2)

---

## 12. Treatment

### 12.1 Standard of care / programmatic backbone
- **Ivermectin mass drug administration (MDA/CDTI)** remains the backbone strategy for control and elimination. (ouedraogo2024effectsoffive pages 1-2, kanza2024onchocercavolvulusmicrofilariae pages 1-2)

### 12.2 Moxidectin (recent research and applications)
**Rationale and modelling:** A 2023 modelling analysis reports that annual ivermectin alone may not achieve elimination everywhere, while moxidectin’s superiority in prolonged microfilarial clearance could accelerate elimination; projections indicate **biannual moxidectin MDA may halve time-to-elimination in mesoendemic areas and may be necessary in hyperendemic areas**. (kura2023canmassdrug pages 1-2)

**Phase 3 ocular safety outcome detail:** In a randomized double-blind Phase 3 comparison, ocular Mazzotti reactions occurred in **12.4%** of moxidectin-treated vs **10.2%** of ivermectin-treated participants, with similar effects on microfilariae in the anterior chamber. (kanza2024onchocercavolvulusmicrofilariae pages 1-2)

**Loa loa co-endemic safety considerations:** A randomized trial in *Loa loa*–infected individuals (Cameroon; NCT04049851) found no serious/severe adverse events with 2 mg moxidectin vs ivermectin in low microfilaremia strata and suggests further dose exploration. (wafeu2024safetyandshortterm pages 1-2)

### 12.3 Anti-*Wolbachia* therapy (macrofilaricidal strategy)
A 2023 translational review reports doxycycline anti-*Wolbachia* regimens can be macrofilaricidal and profoundly reduce microfilariae (e.g., “~96% Wolbachia loss and 99% microfilaria reduction” with 6 weeks of doxycycline 200 mg/day), but WHO recommends doxycycline for **individual therapy rather than MDA** due to multi-week dosing and contraindications (pregnancy, breastfeeding, children <8). (karunakaran2023filariasisresearch– pages 9-10)

### 12.4 Late-stage / experimental therapeutics and trials (NCT identifiers)
From a 2023 review of pipeline agents (anti-*Wolbachia* and direct-acting candidates):
- ABBV-4083 / flubentylosin (anti-*Wolbachia*), Phase II: **NCT04913610** (karunakaran2023filariasisresearch– pages 9-10)
- AWZ1066S (anti-*Wolbachia*), Phase I: **NCT05084560** (karunakaran2023filariasisresearch– pages 9-10)
- Emodepside (direct-acting), Phase II: **NCT05180461** (karunakaran2023filariasisresearch– pages 9-10)
- Oxfendazole (direct-acting), Phase II: **NCT04713787** (karunakaran2023filariasisresearch– pages 9-10)

### 12.5 Treatment ontology suggestions (MAXO) and chemical entities (ChEBI)
*Note:* ontology identifiers below are suggested for knowledge base normalization.
- Ivermectin administration / preventive chemotherapy → **MAXO:0000757** (drug therapy; verify exact MAXO term) (ouedraogo2024effectsoffive pages 1-2)
- Moxidectin therapy → MAXO drug therapy term (kura2023canmassdrug pages 1-2)
- Doxycycline therapy (anti-*Wolbachia*) → MAXO drug therapy term (karunakaran2023filariasisresearch– pages 9-10)

ChEBI suggestions:
- Ivermectin → CHEBI term (not provided in evidence; requires lookup)
- Moxidectin → CHEBI term (not provided in evidence; requires lookup)
- Doxycycline → CHEBI term (not provided in evidence; requires lookup)

---

## 13. Prevention

### 13.1 Primary prevention (public health)
- **Vector exposure reduction and vector control** in breeding sites (e.g., “Slash and Clear” vegetation control around breeding sites) can complement MDA and is supported by modelling and field program experience. (jada2023effectofonchocerciasis pages 1-3)

### 13.2 Secondary prevention
- **Surveillance using Ov16 serology** and **entomological PCR** to detect residual transmission and to support stop-MDA decisions under WHO criteria. (ityonzughul2024theinterruptionof pages 1-2)

### 13.3 Tertiary prevention
- In high OAE burden settings, integrated intervention is advocated combining strengthened onchocerciasis programs and reliable access to antiseizure medications to reduce disability and mortality. (amaral2025highepilepsyprevalence pages 1-2)

---

## 14. Other species / natural disease

### 14.1 Zoonotic potential and other *Onchocerca* species
The retrieved evidence set did not contain primary data on zoonotic transmission for *O. volvulus*; it focuses on human onchocerciasis. A related research context for filarial disease uses animal parasites and comparative models (below). (karunakaran2023filariasisresearch– pages 1-2)

---

## 15. Model organisms and experimental systems

### 15.1 Animal models enabling onchocerciasis research
A 2023 filariasis research review highlights the **Litomosoides sigmodontis** animal model as “extensively useful in elucidating protective immune responses against filariae” and for studying filarial immunomodulation, supporting translational work in onchocerciasis. (karunakaran2023filariasisresearch– pages 1-2)

### 15.2 In vitro / molecular diagnostics development
The same review describes development of “sensitive qPCRs as well as LAMP assays” and ongoing “artificial intelligence based histology analysis for onchocerciasis.” (karunakaran2023filariasisresearch– pages 1-2)

---

## Recent developments and expert analysis (2023–2024 prioritized)

1) **Stop-MDA at unprecedented scale:** Nigeria’s Abia, Anambra, Enugu, and Imo states met WHO epidemiologic and entomological criteria and stopped MDA effective Jan 2023, representing 18.9 million residents eligible for MDA in the “largest global onchocerciasis stop-treatment decision to date.” (ityonzughul2024theinterruptionof pages 1-2)

2) **Diagnostic innovation with persistent specificity gaps:** Bayesian latent-class analysis (field studies in 2023) suggests newer Ov16 RDTs can exceed sensitivity thresholds for stop-MDA decisions, but none met the WHO specificity benchmark of ≥99.8%, reinforcing the need for confirmatory strategies. (norman2026assessingdiagnosticaccuracy pages 1-3, norman2026assessingdiagnosticaccuracy pages 7-11)

3) **Shift to alternative tools where ivermectin is insufficient:** Modelling indicates that moxidectin MDA (especially biannual) may be necessary for elimination in hyperendemic settings, motivating implementation research and policy discussions. (kura2023canmassdrug pages 1-2)

4) **Pipeline maturation:** Anti-*Wolbachia* candidates (e.g., ABBV-4083, AWZ1066S) and direct-acting macrofilaricides (emodepside, oxfendazole) were in Phase I/II development with identified NCT registrations as of 2023. (karunakaran2023filariasisresearch– pages 9-10)

5) **Recognition of neurological burden and mortality:** High epilepsy prevalence and excess mortality in endemic counties (South Sudan) support expert calls to integrate onchocerciasis and epilepsy programs. (amaral2025highepilepsyprevalence pages 1-2)

---

## Evidence tables
The table below compiles key quantitative parameters for burden, elimination thresholds, and therapeutics/trials.

| Domain | Finding/Threshold | Study/Source (author-year) | Population/Setting | Date | URL/DOI | Notes |
|---|---|---|---|---|---|---|
| Burden/epidemiology | ~20 million infected; 1.26 million DALYs (95% UI 0.75–1.90 million); ≥248 million people in SSA required MDA | Dixon et al. 2026 | Sub-Saharan Africa / GBD-informed modelling context | 2026-03 | https://doi.org/10.1038/s43856-026-01464-2 | Summarizes recent burden context up to 2024–2025; notes elimination verified in few foci (dixon2026modellingofonchocerciasisassociated pages 1-5) |
| Burden/epidemiology | 1.23 million DALYs attributable to onchocerciasis in 2019 | Stapley et al. 2024 | Global Burden of Disease estimate referenced in OAE model | 2024-07 | https://doi.org/10.1038/s41467-024-50582-9 | Used as burden baseline in modelling OAE prevention impact (stapley2024modellingonchocerciasisassociatedepilepsy pages 1-2) |
| Burden/epidemiology | Epilepsy prevalence 4.1% (range 2.3–7.1%); probable nodding syndrome 1.5% (0.6–2.2%) | Amaral et al. 2025 | 34,019 individuals in 5 onchocerciasis-endemic counties, South Sudan | 2025-06 | https://doi.org/10.1371/journal.pntd.0013244 | Anti-Ov16 seroprevalence in children 3–9 y was 23.3% (1.4–44.1%) (amaral2025highepilepsyprevalence pages 1-2) |
| Burden/epidemiology | Standardized mortality rate 67.6/1,000 PY in persons with suspected epilepsy vs 9.0/1,000 PY in individuals without epilepsy; SMR 6.9 | Amaral et al. 2025 | South Sudan endemic counties | 2025-06 | https://doi.org/10.1371/journal.pntd.0013244 | Median age at death 20 y in epilepsy vs 38 y in controls (amaral2025highepilepsyprevalence pages 1-2) |
| Burden/epidemiology | Epilepsy prevalence 4.1%; annual incidence 147.6/100,000; epilepsy mortality 323.7/100,000 persons | Fodjo et al. 2024 | 1,355 people in Wulu County, South Sudan | 2024-09 | https://doi.org/10.1016/j.heliyon.2024.e37537 | Ov16 seroprevalence in children 3–9 y was 15.1%; nodding seizures in 20% of epilepsy cases (fodjo2024epidemiologyofepilepsy pages 1-3) |
| Burden/epidemiology | Predicted epilepsy prevalence 7.6% and incidence 317/100,000 PY | Stapley et al. 2024 | Cameroon-calibrated EPIONCHO-IBM model | 2024-07 | https://doi.org/10.1038/s41467-024-50582-9 | Closely matched observed 8.2% prevalence and 350/100,000 PY incidence (stapley2024modellingonchocerciasisassociatedepilepsy pages 1-2) |
| Burden/epidemiology | OAE prevalence estimated 4.1%; annual ivermectin MDA with ~70% coverage could reduce OAE incidence by >50% within 5 years | Bhattacharyya et al. 2023 | Maridi, South Sudan modelling | 2023-05 | https://doi.org/10.1371/journal.pntd.0011320 | Combined vector control + MDA projected to outperform either alone (bhattacharyya2023onchocerciasisassociatedepilepsyin pages 1-2) |
| Burden/epidemiology | Epilepsy incidence fell from 348.8 to 41.7/100,000 PY; nodding syndrome from 154.7 to 10.4/100,000 PY after strengthened control | Jada et al. 2023 | Maridi, South Sudan prospective study | 2023-04 | https://doi.org/10.21203/rs.3.rs-2764415/v1 | After biannual CDTI and “Slash and Clear” vector control; ivermectin uptake still only 56.6% in 2021 (jada2023effectofonchocerciasis pages 1-3) |
| Stop-MDA diagnostics | Ov16 criterion: seroprevalence <0.1% in children 5–9 y with 95% confidence (95% UCL <0.1%); survey size ≥3,000 children | Ityonzughul et al. 2024 | WHO-aligned stop-MDA decision, Nigeria | 2024-08 | https://doi.org/10.3390/pathogens13080671 | Four Nigerian states met criterion; largest stop-treatment decision to date (ityonzughul2024theinterruptionof pages 2-5, ityonzughul2024theinterruptionof pages 1-2) |
| Stop-MDA diagnostics | Entomology criterion: infective fly prevalence <0.05% by O-150 PCR with 95% confidence; minimum sample 6,000 flies | Ityonzughul et al. 2024 | WHO-aligned stop-MDA decision, Nigeria | 2024-08 | https://doi.org/10.3390/pathogens13080671 | If fewer flies analyzed, ATP criterion may be used instead (ityonzughul2024theinterruptionof pages 2-5, ityonzughul2024theinterruptionof pages 1-2) |
| Stop-MDA diagnostics | ATP criterion: annual transmission potential <20 with 95% confidence when fly sample size is insufficient | Ityonzughul et al. 2024 | WHO-aligned stop-MDA decision, Nigeria | 2024-08 | https://doi.org/10.3390/pathogens13080671 | Alternative to infective-fly prevalence criterion (ityonzughul2024theinterruptionof pages 2-5, ityonzughul2024theinterruptionof pages 1-2) |
| Stop-MDA diagnostics | WHO TPP thresholds for Ov16 RDTs: sensitivity ≥60% for mapping, ≥89% for stop-MDA; specificity ≥99.8% | Norman et al. 2026 | Bayesian latent class evaluation of Ov16 RDTs | 2026-01 | https://doi.org/10.64898/2026.01.20.26344416 | Current tests generally fail the 99.8% specificity target needed for stand-alone stop-MDA decisions (norman2026assessingdiagnosticaccuracy pages 3-5, norman2026assessingdiagnosticaccuracy pages 1-3, norman2026assessingdiagnosticaccuracy pages 7-11) |
| Stop-MDA diagnostics | GADx Ov16 RDT sensitivity 92.0–92.8%; highest median specificity 98.8% | Norman et al. 2026 | Mozambique, Ghana, Benin pooled data | 2026-01 | https://doi.org/10.64898/2026.01.20.26344416 | Sensitivity exceeds stop-MDA threshold, specificity still below 99.8% benchmark (norman2026assessingdiagnosticaccuracy pages 1-3, norman2026assessingdiagnosticaccuracy pages 7-11) |
| Stop-MDA diagnostics | SD Bioline Ov16 RDT field cost about US$24/person vs US$74/person for skin-snip microscopy | Otabil et al. 2025 | Surveillance costing model, Ghana | 2025-05 | https://doi.org/10.1101/2024.05.07.24306977 | RDT preferred by participants/technicians; more acceptable and less invasive (otabil2025usabilityacceptabilityand pages 31-35, otabil2025usabilityacceptabilityand pages 11-15, otabil2025usabilityacceptabilityand pages 1-6) |
| Intervention/drug | Biannual moxidectin MDA could halve years to elimination in mesoendemic settings and may be only strategy achieving EoT in hyperendemic areas | Kura et al. 2023 | EPIONCHO-IBM modelling, Africa | 2023-08 | https://doi.org/10.1098/rstb.2022.0277 | Based on Phase II/III evidence of longer-lasting microfilarial suppression than ivermectin (kura2023canmassdrug pages 1-2) |
| Intervention/drug | Moxidectin 8 mg FDA-approved for onchocerciasis; ocular Mazzotti reactions 12.4% vs 10.2% with ivermectin in phase 3 comparison | Kanza et al. 2024 | DRC, Ghana, Liberia; ivermectin-naïve adults with ≥10 SmfD | 2024-03 | https://doi.org/10.1186/s13071-023-06087-3 | mf in anterior chamber changed similarly with moxidectin and ivermectin (kanza2024onchocercavolvulusmicrofilariae pages 1-2) |
| Intervention/drug | Moxidectin vs ivermectin phase 3 trial | ClinicalTrials.gov NCT00790998 | Onchocerca volvulus infection | completed; phase 3 | https://clinicaltrials.gov/study/NCT00790998 | Enrollment 1,497; sponsor Medicines Development for Global Health |
| Intervention/drug | Annual or biannual moxidectin vs ivermectin safety/efficacy trial | ClinicalTrials.gov NCT03876262 | Onchocerciasis | active, phase 3 | https://clinicaltrials.gov/study/NCT03876262 | Enrollment 323 |
| Intervention/drug | Large safety study of single-dose moxidectin vs ivermectin (with/without LF co-endemicity/albendazole) | ClinicalTrials.gov NCT04311671 | Endemic-area participants | completed; phase 3 | https://clinicaltrials.gov/study/NCT04311671 | Enrollment 12,979 |
| Intervention/drug | Moxidectin pediatric PK/safety dose-finding | ClinicalTrials.gov NCT03962062 | Children 4–11 years | completed; phase 1 | https://clinicaltrials.gov/study/NCT03962062 | Supports future pediatric registration/use |
| Intervention/drug | Moxidectin MDA implementation study | ClinicalTrials.gov NCT07145736 | Community MDA for onchocerciasis/other NTDs | recruiting; phase 4 | https://clinicaltrials.gov/study/NCT07145736 | Planned enrollment 52,000 |
| Intervention/drug | Doxycycline 200 mg/day x 6 weeks: ~96% Wolbachia depletion and 99% microfilaria reduction; macrofilaricidal effect ~89% at 2 years when followed by ivermectin+albendazole | Karunakaran et al. 2023 | Anti-Wolbachia therapy review | 2023-03 | https://doi.org/10.3389/fitd.2023.1126173 | Recommended by WHO for individual therapy, not MDA; safe in Loa loa co-endemicity because L. loa lacks Wolbachia (karunakaran2023filariasisresearch– pages 9-10) |
| Intervention/drug | ABBV-4083 (flubentylosin), phase 2 | Karunakaran et al. 2023 / ClinicalTrials.gov | Adult participants with O. volvulus infection | 2023 context | https://clinicaltrials.gov/study/NCT04913610 | Anti-Wolbachia candidate; NCT04913610; terminated; enrollment 153 (karunakaran2023filariasisresearch– pages 9-10) |
| Intervention/drug | AWZ1066S, phase 1 | Karunakaran et al. 2023 / ClinicalTrials.gov | Healthy volunteers / anti-Wolbachia development | 2023 context | https://clinicaltrials.gov/study/NCT05084560 | Small-molecule anti-Wolbachia candidate; terminated; enrollment 30 (karunakaran2023filariasisresearch– pages 9-10) |
| Intervention/drug | Emodepside, phase 2 | Karunakaran et al. 2023 / ClinicalTrials.gov | Treatment of onchocerciasis | 2023 context | https://clinicaltrials.gov/study/NCT05180461 | Direct-acting candidate; active not recruiting; enrollment 578 (karunakaran2023filariasisresearch– pages 9-10) |
| Intervention/drug | Oxfendazole, phase 2 | Karunakaran et al. 2023 | Treatment candidate for onchocerciasis | 2023 context | NCT04713787 | Listed as direct-acting candidate in development table (karunakaran2023filariasisresearch– pages 9-10) |
| Intervention/drug | High-dose rifampicin / rifampin studied as anti-Wolbachia approach | Karunakaran et al. 2023 / ClinicalTrials.gov | River blindness treatment development | 2023 context | https://clinicaltrials.gov/study/NCT00127504 | Earlier rifampin+azithromycin trial completed; high-dose rifampicin study was scheduled in review table (karunakaran2023filariasisresearch– pages 9-10) |


*Table: This table compacts recent onchocerciasis evidence across burden, stop-MDA diagnostics, and therapeutic development. It is designed as a quick-reference artifact for knowledge-base population and programmatic decision support.*

---

## Direct quotes from abstracts (selected)
- Nigeria stop-MDA decision: “Each state therefore met the World Health Organization epidemiological and entomological criteria for stopping MDA effective January 2023.” (ityonzughul2024theinterruptionof pages 1-2)
- OAE modelling: “EPIONCHO-IBM predicted 7.6% epilepsy prevalence (compared to 8.2% in the Cameroon study) and incidence of 317 cases/100,000 person-years (compared to 350).” (stapley2024modellingonchocerciasisassociatedepilepsy pages 1-2)
- Moxidectin modelling: “EPIONCHO-IBM's projections indicate that biannual (six-monthly) moxidectin MDA can reduce by half the number of years necessary to achieve EoT in mesoendemic areas and might be the only strategy that can achieve EoT in hyperendemic areas.” (kura2023canmassdrug pages 1-2)

---

## Key limitations and recommended next steps for knowledge-base completion
1) **Ontology identifiers (MONDO/ICD/MeSH/Orphanet)** were not present in retrieved texts; populate these via direct lookup from the respective databases.
2) **Detailed immunopathogenesis** (cytokines, cell-specific pathways, ocular lesion subtypes) and **validated QoL instruments** were not covered in the retrieved evidence; targeted searches in immunology/ophthalmology literature and WHO/CDC clinical guidance would be required.
3) **Genetic susceptibility/protective loci** were not identified here; if needed, dedicated GWAS/host-genetics searches should be performed.


References

1. (kamgno2025vectorbornehelminthiasesa pages 24-27): Joseph Kamgno, Monsuru Adeleke, María-Gloria Basáñez, Yaya Coulibaly, Dziedzom K de Souza, Linda Batsa Debrah, Alexander Yaw Debrah, Peter J Diggle, Hugues C Nana-Djeunga, André Domché, Katherine Gass, Achim Hoerauf, Adrian Hopkins, Amy Klion, Charles D Mackenzie, Upendo Mwingira, Sammy M Njenga, Thomas B Nutman, Philippe Nwane, Wilma A Stolk, Thomas R Unnasch, and Louise A Kelly-Hope. Vector-borne helminthiases: a road map for current and future research to support control and elimination in sub-saharan africa. The Lancet. Infectious diseases, Jun 2025. URL: https://doi.org/10.1016/s1473-3099(25)00084-2, doi:10.1016/s1473-3099(25)00084-2. This article has 9 citations.

2. (stapley2024modellingonchocerciasisassociatedepilepsy pages 1-2): Jacob N. Stapley, Jonathan I. D. Hamley, Martin Walker, Matthew A. Dixon, Robert Colebunders, and Maria-Gloria Basáñez. Modelling onchocerciasis-associated epilepsy and the impact of ivermectin treatment on its prevalence and incidence. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50582-9, doi:10.1038/s41467-024-50582-9. This article has 8 citations and is from a highest quality peer-reviewed journal.

3. (kura2023canmassdrug pages 1-2): Klodeta Kura, Philip Milton, Jonathan I. D. Hamley, Martin Walker, Didier K. Bakajika, Eric M. Kanza, Nicholas O. Opoku, Hayford Howard, Maurice M. Nigo, Sampson Asare, George Olipoh, Simon K. Attah, Germain L. Mambandu, Kambale Kasonia Kennedy, Kambale Kataliko, Mupenzi Mumbere, Christine M. Halleux, Adrian Hopkins, Annette C. Kuesel, Sally Kinrade, and Maria-Gloria Basáñez. Can mass drug administration of moxidectin accelerate onchocerciasis elimination in africa? Philosophical Transactions of the Royal Society B: Biological Sciences, Aug 2023. URL: https://doi.org/10.1098/rstb.2022.0277, doi:10.1098/rstb.2022.0277. This article has 32 citations and is from a domain leading peer-reviewed journal.

4. (ityonzughul2024theinterruptionof pages 2-5): Cephas Ityonzughul, Adamu Sallau, Emmanuel Miri, Emmanuel Emukah, Barminas Kahansim, Solomon Adelamo, George Chiedo, Samuel Ifeanyichukwu, Jenna E. Coalson, Lindsay Rakers, Emily Griswold, Chukwuemeka Makata, Fatai Oyediran, Stella Osuji, Solomon Offor, Emmanuel Obikwelu, Ifeoma Otiji, Frank O. Richards, and Gregory S. Noland. The interruption of transmission of onchocerciasis in abia, anambra, enugu, and imo states, nigeria: the largest global onchocerciasis stop-treatment decision to date. Pathogens, 13:671, Aug 2024. URL: https://doi.org/10.3390/pathogens13080671, doi:10.3390/pathogens13080671. This article has 1 citations.

5. (karunakaran2023filariasisresearch– pages 9-10): Indulekha Karunakaran, Manuel Ritter, Kenneth Pfarr, Ute Klarmann-Schulz, Alexander Yaw Debrah, Linda Batsa Debrah, Gnatoulma Katawa, Samuel Wanji, Sabine Specht, Tomabu Adjobimey, Marc Peter Hübner, and Achim Hoerauf. Filariasis research – from basic research to drug development and novel diagnostics, over a decade of research at the institute for medical microbiology, immunology and parasitology, bonn, germany. Frontiers in Tropical Diseases, Mar 2023. URL: https://doi.org/10.3389/fitd.2023.1126173, doi:10.3389/fitd.2023.1126173. This article has 9 citations.

6. (ouedraogo2024effectsoffive pages 1-2): Micheline O. Ouedraogo, Ivlabèhirè Bertrand Meda, Karifa Kourouma, Fanny Yago Wienne, Dieudonné Nare, Clarisse Bougouma, Justin Compaore, and Seni Kouanda. Effects of five years of treatment of onchocerciasis with ivermectin under community guidelines in resurgent areas of burkina faso: a before-and-after analysis. Tropical Medicine and Infectious Disease, 9:207, Sep 2024. URL: https://doi.org/10.3390/tropicalmed9090207, doi:10.3390/tropicalmed9090207. This article has 1 citations.

7. (amaral2025highepilepsyprevalence pages 1-2): Luís-Jorge Amaral, Stephen Raimon Jada, Jane Y. Carter, Yak Yak Bol, María-Gloria Basáñez, Charles R. Newton, Joseph N. Siewe Fodjo, and Robert Colebunders. High epilepsy prevalence and excess mortality in onchocerciasis-endemic counties of south sudan: a call for integrated interventions. PLOS Neglected Tropical Diseases, 19:e0013244, Jun 2025. URL: https://doi.org/10.1371/journal.pntd.0013244, doi:10.1371/journal.pntd.0013244. This article has 3 citations and is from a domain leading peer-reviewed journal.

8. (jada2023effectofonchocerciasis pages 1-3): Stephen Raimon Jada, Luís-Jorge Amaral, Thomas Lakwo, Jane Y Carter, Jacopo Rovarini, Yak Yak Bol, Makoy Yibi Logora, Amber Hadermann, Adrian Hopkins, Joseph N Siewe Fodjo, and Robert Colebunders. Effect of onchocerciasis elimination measures on the incidence of epilepsy in maridi, south sudan: a three-year prospective study. Apr 2023. URL: https://doi.org/10.21203/rs.3.rs-2764415/v1, doi:10.21203/rs.3.rs-2764415/v1.

9. (fodjo2024epidemiologyofepilepsy pages 1-3): Joseph Nelson Siewe Fodjo, Stephen Raimon Jada, Abraham Taban, John Bebe, Yak Yak Bol, Jane Y. Carter, and Robert Colebunders. Epidemiology of epilepsy in wulu county, an onchocerciasis-endemic area in south sudan. Heliyon, 10:e37537, Sep 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e37537, doi:10.1016/j.heliyon.2024.e37537. This article has 2 citations.

10. (kanza2024onchocercavolvulusmicrofilariae pages 1-2): Eric M. Kanza, Amos Nyathirombo, Jemmah P. Larbelee, Nicholas O. Opoku, Didier K. Bakajika, Hayford M. Howard, Germain L. Mambandu, Maurice M. Nigo, Deogratias Ucima Wonyarossi, Françoise Ngave, Kambale Kasonia Kennedy, Kambale Kataliko, Kpehe M. Bolay, Simon K. Attah, George Olipoh, Sampson Asare, Mupenzi Mumbere, Michel Vaillant, Christine M. Halleux, and Annette C. Kuesel. Onchocerca volvulus microfilariae in the anterior chambers of the eye and ocular adverse events after a single dose of 8 mg moxidectin or 150 µg/kg ivermectin: results of a randomized double-blind phase 3 trial in the democratic republic of the congo, ghana and liberia. Parasites &amp; Vectors, Mar 2024. URL: https://doi.org/10.1186/s13071-023-06087-3, doi:10.1186/s13071-023-06087-3. This article has 4 citations and is from a peer-reviewed journal.

11. (bhattacharyya2023onchocerciasisassociatedepilepsyin pages 1-2): Samit Bhattacharyya, Natalie V. S. Vinkeles Melchers, Joseph N. Siewe Fodjo, Amit Vutha, Luc E. Coffeng, Makoy Y. Logora, Robert Colebunders, and Wilma A. Stolk. Onchocerciasis-associated epilepsy in maridi, south sudan: modelling and exploring the impact of control measures against river blindness. PLOS Neglected Tropical Diseases, 17:e0011320, May 2023. URL: https://doi.org/10.1371/journal.pntd.0011320, doi:10.1371/journal.pntd.0011320. This article has 12 citations and is from a domain leading peer-reviewed journal.

12. (dixon2026modellingofonchocerciasisassociated pages 1-5): Matthew A. Dixon, Aditya Ramani, Martin Walker, Jacob N. Stapley, Michele E. Murdoch, Ian E. Murdoch, Gladys A. Ozoh, Jonathan F. Mosser, and Maria-Gloria Basáñez. Modelling of onchocerciasis-associated skin and ocular disease and the impact of ivermectin treatment. Communications Medicine, Mar 2026. URL: https://doi.org/10.1038/s43856-026-01464-2, doi:10.1038/s43856-026-01464-2. This article has 0 citations and is from a peer-reviewed journal.

13. (norman2026assessingdiagnosticaccuracy pages 3-5): Jayla Norman, N’Deye-Marie Bassabi-Alladjie, Pelagie M Boko-Collins, Dziedzom K. de Souza, Katherine Gass, Louise Hamill, Jerónimo Langa, Carson Moore, Rassul Nala, Sarah Sullivan, and Emanuele Giorgi. Assessing diagnostic accuracy of ov16 rapid diagnostic tests for onchocerciasis using bayesian latent class models. Unknown journal, Jan 2026. URL: https://doi.org/10.64898/2026.01.20.26344416, doi:10.64898/2026.01.20.26344416.

14. (ityonzughul2024theinterruptionof pages 1-2): Cephas Ityonzughul, Adamu Sallau, Emmanuel Miri, Emmanuel Emukah, Barminas Kahansim, Solomon Adelamo, George Chiedo, Samuel Ifeanyichukwu, Jenna E. Coalson, Lindsay Rakers, Emily Griswold, Chukwuemeka Makata, Fatai Oyediran, Stella Osuji, Solomon Offor, Emmanuel Obikwelu, Ifeoma Otiji, Frank O. Richards, and Gregory S. Noland. The interruption of transmission of onchocerciasis in abia, anambra, enugu, and imo states, nigeria: the largest global onchocerciasis stop-treatment decision to date. Pathogens, 13:671, Aug 2024. URL: https://doi.org/10.3390/pathogens13080671, doi:10.3390/pathogens13080671. This article has 1 citations.

15. (otabil2025usabilityacceptabilityand pages 1-6): Kenneth Bentum Otabil, María-Gloria Basáñez, Ameyaa Elizabeth, Michael Oppong, Prince Mensah, Richmond Gyasi-Ampofo, Emmanuel John Bart-Plange, Theophilus Nti Babae, Lydia Datsa, Andrews Agyapong Boakye, Michael Tawiah Yeboah, Prince Nyarko, Prince Charles Kudzordzi, Anabel Acheampong, Edwina Twum Blay, Henk D.F.H. Schallig, and Robert Colebunders. Usability, acceptability and cost of the sd bioline ov16 rapid diagnostic test for onchocerciasis surveillance in endemic communities in the middle belt of ghana. MedRxiv, May 2025. URL: https://doi.org/10.1101/2024.05.07.24306977, doi:10.1101/2024.05.07.24306977. This article has 2 citations.

16. (norman2026assessingdiagnosticaccuracy pages 1-3): Jayla Norman, N’Deye-Marie Bassabi-Alladjie, Pelagie M Boko-Collins, Dziedzom K. de Souza, Katherine Gass, Louise Hamill, Jerónimo Langa, Carson Moore, Rassul Nala, Sarah Sullivan, and Emanuele Giorgi. Assessing diagnostic accuracy of ov16 rapid diagnostic tests for onchocerciasis using bayesian latent class models. Unknown journal, Jan 2026. URL: https://doi.org/10.64898/2026.01.20.26344416, doi:10.64898/2026.01.20.26344416.

17. (norman2026assessingdiagnosticaccuracy pages 7-11): Jayla Norman, N’Deye-Marie Bassabi-Alladjie, Pelagie M Boko-Collins, Dziedzom K. de Souza, Katherine Gass, Louise Hamill, Jerónimo Langa, Carson Moore, Rassul Nala, Sarah Sullivan, and Emanuele Giorgi. Assessing diagnostic accuracy of ov16 rapid diagnostic tests for onchocerciasis using bayesian latent class models. Unknown journal, Jan 2026. URL: https://doi.org/10.64898/2026.01.20.26344416, doi:10.64898/2026.01.20.26344416.

18. (wafeu2024safetyandshortterm pages 1-2): G. S. Wafeu, Tristan M. Lepage, Jérémy T. Campillo, Arnauld Efon-Ekangouo, H. Nana-Djeunga, Narcisse Nzune-Toche, A. Domché, Laurentine Sumo, G. Njitchouang, M. A. Tsasse, J. Bopda, Yves Aubin Balog, Yannick Niamsi-Emalio, Stève Mbickmen-Tchana, Gervais Kamga Talla, Yannick Sédrick Nguedia Kana, Félicité Diane Maga Messina, S. Pion, A. Kuesel, J. Kamgno, M. Boussinesq, and C. Chesnais. Safety and short-term efficacy of a single dose of 2 mg moxidectin in loa loa–infected individuals: a double-blind, randomized ivermectin-controlled trial with ascending microfilarial densities. Open Forum Infectious Diseases, Apr 2024. URL: https://doi.org/10.1093/ofid/ofae240, doi:10.1093/ofid/ofae240. This article has 6 citations and is from a peer-reviewed journal.

19. (karunakaran2023filariasisresearch– pages 1-2): Indulekha Karunakaran, Manuel Ritter, Kenneth Pfarr, Ute Klarmann-Schulz, Alexander Yaw Debrah, Linda Batsa Debrah, Gnatoulma Katawa, Samuel Wanji, Sabine Specht, Tomabu Adjobimey, Marc Peter Hübner, and Achim Hoerauf. Filariasis research – from basic research to drug development and novel diagnostics, over a decade of research at the institute for medical microbiology, immunology and parasitology, bonn, germany. Frontiers in Tropical Diseases, Mar 2023. URL: https://doi.org/10.3389/fitd.2023.1126173, doi:10.3389/fitd.2023.1126173. This article has 9 citations.

20. (otabil2025usabilityacceptabilityand pages 31-35): Kenneth Bentum Otabil, María-Gloria Basáñez, Ameyaa Elizabeth, Michael Oppong, Prince Mensah, Richmond Gyasi-Ampofo, Emmanuel John Bart-Plange, Theophilus Nti Babae, Lydia Datsa, Andrews Agyapong Boakye, Michael Tawiah Yeboah, Prince Nyarko, Prince Charles Kudzordzi, Anabel Acheampong, Edwina Twum Blay, Henk D.F.H. Schallig, and Robert Colebunders. Usability, acceptability and cost of the sd bioline ov16 rapid diagnostic test for onchocerciasis surveillance in endemic communities in the middle belt of ghana. MedRxiv, May 2025. URL: https://doi.org/10.1101/2024.05.07.24306977, doi:10.1101/2024.05.07.24306977. This article has 2 citations.

21. (otabil2025usabilityacceptabilityand pages 11-15): Kenneth Bentum Otabil, María-Gloria Basáñez, Ameyaa Elizabeth, Michael Oppong, Prince Mensah, Richmond Gyasi-Ampofo, Emmanuel John Bart-Plange, Theophilus Nti Babae, Lydia Datsa, Andrews Agyapong Boakye, Michael Tawiah Yeboah, Prince Nyarko, Prince Charles Kudzordzi, Anabel Acheampong, Edwina Twum Blay, Henk D.F.H. Schallig, and Robert Colebunders. Usability, acceptability and cost of the sd bioline ov16 rapid diagnostic test for onchocerciasis surveillance in endemic communities in the middle belt of ghana. MedRxiv, May 2025. URL: https://doi.org/10.1101/2024.05.07.24306977, doi:10.1101/2024.05.07.24306977. This article has 2 citations.
