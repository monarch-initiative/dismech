---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T16:52:09.856501'
end_time: '2026-04-25T17:04:44.801252'
duration_seconds: 754.94
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cowden Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 46
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cowden Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cowden Syndrome** covering all of the
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
- **Disease Name:** Cowden Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cowden Syndrome** covering all of the
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


# Cowden Syndrome (PTEN Hamartoma Tumor Syndrome, PHTS): Disease Characteristics Research Report

## 1. Disease Information

### 1.1 Concise overview
Cowden syndrome (CS) is a multisystem hamartoma and cancer predisposition disorder within the broader **PTEN hamartoma tumor syndrome (PHTS)** spectrum, characterized by mucocutaneous lesions, macrocephaly, gastrointestinal hamartomatous polyps, and elevated risks of multiple malignancies (notably breast, thyroid, endometrial, colorectal, and renal cancers). It is typically caused by heterozygous **germline pathogenic variants in PTEN**, resulting in dysregulated growth control via PI3K/AKT/mTOR signaling. (pirlog2024insightsintoclinical pages 1-2, takayama2023clinicalguidelinesfor pages 2-4)

### 1.2 Key identifiers (as available from retrieved sources)
- **MONDO**: Cowden syndrome 1 **MONDO_0008021**; Cowden disease **MONDO_0016063** (cummings2023cancerriskassociated pages 1-2)
- **OMIM**: Cowden syndrome **158350** (explicitly stated in a 2023 case review) (jurca2023anewframeshift pages 9-10)
- **Orphanet / ICD-10 / ICD-11 / MeSH**: Not found in retrieved sources in this run (insufficient evidence in retrieved texts to cite).

### 1.3 Synonyms and alternative names
- Cowden syndrome; Cowden disease; PTEN hamartoma tumor syndrome (umbrella term) (takayama2023clinicalguidelinesfor pages 2-4, pilarski2019ptenhamartomatumor pages 1-3)
- Related phenotypes within the PHTS umbrella include **Bannayan–Riley–Ruvalcaba syndrome (BRRS)**, **Proteus syndrome**, **Proteus-like syndrome**, and **adult Lhermitte–Duclos disease** (pilarski2019ptenhamartomatumor pages 1-3, pirlog2024insightsintoclinical pages 1-2).

### 1.4 Evidence provenance (individual-level vs aggregated resources)
Much of the evidence base for CS/PHTS includes (i) **aggregated guideline and cohort estimates** (e.g., lifetime cancer risk ranges across cohorts, surveillance guidelines) and (ii) **clinic-ascertained cohorts** with ascertainment bias concerns. For example, cancer risk estimates vary substantially across studies, and reviews emphasize cautious interpretation because cohorts often include index cases and prevalent cancers. (hendricks2021areviewon pages 1-4, pilarski2019ptenhamartomatumor pages 3-5)


## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** heterozygous germline pathogenic variants in the tumor suppressor **PTEN** (autosomal dominant), leading to loss of PTEN function and downstream pathway dysregulation. (pirlog2024insightsintoclinical pages 1-2, takayama2023clinicalguidelinesfor pages 2-4)

**Pathway consequence:** PTEN normally dephosphorylates PIP3 to PIP2, antagonizing PI3K signaling and limiting AKT/mTOR pathway activation. PTEN loss-of-function therefore permits increased PI3K/AKT/mTOR signaling that promotes overgrowth/hamartomas and cancer predisposition. (yehia2020ptenhamartomatumour pages 5-6, pirlog2024insightsintoclinical pages 1-2)

### 2.2 Risk factors
- **Genetic:** Germline PTEN pathogenic variants drive disease and confer elevated risks of multiple cancers (breast, endometrium, thyroid, colon polyposis/cancer, renal). In a large hereditary cancer panel-testing cohort (727,091 individuals tested), PTEN PV carriers had increased risk (odds ratios) for female breast cancer (OR 7.88), endometrial cancer (OR 13.51), thyroid cancer (OR 4.88), and colon polyposis (OR 31.60), with modest evidence for ovarian cancer (OR 3.77). (cummings2023cancerriskassociated pages 1-2)
- **Phenotype-genotype heterogeneity:** Clinical CS criteria and PTEN-variant status incompletely overlap: reviews note only ~30–35% of individuals meeting clinical CS diagnostic criteria have detectable PTEN variants, underscoring heterogeneity and the role of ascertainment. (pilarski2019ptenhamartomatumor pages 1-3, cummings2023cancerriskassociated pages 1-2)

### 2.3 Protective factors
No specific genetic or environmental protective factors were identified in retrieved sources.

### 2.4 Gene–environment interactions
No explicit gene–environment interaction evidence for CS/PHTS was identified in retrieved sources.


## 3. Phenotypes

The phenotype spectrum is broad and age-dependent, with pediatric presentations often dominated by macrocephaly and neurodevelopmental issues, and adult presentations more often demonstrating classic mucocutaneous lesions, polyposis, and malignancies. (martinvalbuena2024ptenhamartomatumor pages 1-2)

| Phenotype | HPO term suggestion | Typical age / notes | Frequency / statistics from evidence | Key citations |
|---|---|---|---|---|
| Macrocephaly | HP:0000256 Macrocephaly | Often earliest and most consistent pediatric finding; may be the presenting sign in infancy/childhood; adult diagnostic thresholds noted as ≥58 cm in women and ≥60 cm in men | 100% (11/11) in a 2024 pediatric cohort; 85.1% at presentation and 96.3% post-diagnosis in a pediatric cohort of 81; 80–100% in mutation carriers in review data; 98% (46/47) in one pediatric study cited by review (martinvalbuena2024ptenhamartomatumor pages 1-2, baran2021theclinicalspectrum pages 3-4, pilarski2019ptenhamartomatumor pages 5-7, takayama2023clinicalguidelinesfor pages 6-8) | (martinvalbuena2024ptenhamartomatumor pages 1-2, baran2021theclinicalspectrum pages 3-4, pilarski2019ptenhamartomatumor pages 5-7, takayama2023clinicalguidelinesfor pages 6-8) |
| Mucocutaneous lesions (trichilemmomas, oral papillomas/fibromas, acral keratoses) | HP:0010618 Trichilemmoma; HP:0009723 Skin papilloma; HP:0100767 Oral mucosal papillomatosis; HP:0007565 Multiple lipomas | Usually accumulate with age; more prominent in adults, but can occur in childhood; characteristic facial papules and multiple trichilemmomas are considered hallmark findings | Skin/oral lesions in 30.9% at presentation and 68.2% after diagnosis in a pediatric cohort; oral fibromas reported in 14–76% and trichilemmomas in 6–25% across reviewed series; pediatric cohort described thumb hamartoma/lipoma and other cutaneous findings but fewer classic lesions than adults (baran2021theclinicalspectrum pages 3-4, pilarski2019ptenhamartomatumor pages 5-7, takayama2023clinicalguidelinesfor pages 6-8, martinvalbuena2024ptenhamartomatumor pages 2-3) | (baran2021theclinicalspectrum pages 3-4, pilarski2019ptenhamartomatumor pages 5-7, takayama2023clinicalguidelinesfor pages 6-8, martinvalbuena2024ptenhamartomatumor pages 2-3) |
| Gastrointestinal polyps / GI manifestations | HP:0200063 Hamartomatous polyposis; HP:0002242 Constipation; HP:0011473 Feeding difficulties | Polyps may appear in childhood but burden increases with age; adults can have few to hundreds of polyps; symptomatic children may present with constipation/feeding issues | >90% of patients undergoing upper endoscopy/colonoscopy had GI polyps in guideline review; up to 95% of adults with PTEN variants who had colonoscopy had polyps; in 80 children, GI polyps occurred in 28% (22/80), constipation in 51% (41/80), feeding issues in 39% (31/80), eosinophilic GI disorders in 6% (5/80) (takayama2023clinicalguidelinesfor pages 6-8, pilarski2019ptenhamartomatumor pages 5-7, liu2024abiinstitutionalstudy pages 1-2) | (takayama2023clinicalguidelinesfor pages 6-8, pilarski2019ptenhamartomatumor pages 5-7, liu2024abiinstitutionalstudy pages 1-2) |
| Thyroid nodules / thyroid abnormalities / differentiated thyroid carcinoma | HP:0000821 Goiter; HP:0002664 Thyroid carcinoma; HP:0000857 Thyroid nodule; HP:0002716 Autoimmune thyroiditis | Thyroid disease can begin in childhood; some guidelines recommend ultrasound from diagnosis because cancer has been reported as early as age 7; pediatric cancers generally low-invasive | In 43 surveilled children: thyroid abnormalities 84%, nodular disease 74%, goiter 30%, autoimmune thyroiditis 12%, nodular growth 33%, thyroidectomy 16%, DTC 5% (2/43) at ages 12 and 17; prior pediatric estimates for DTC 4–12% with median age ~12 years (range 4–17); another pediatric cohort reported thyroid cancer in 7.4% (6/81), all >10 years old (bormans2024experienceina pages 1-2, baran2021theclinicalspectrum pages 3-4, takayama2023clinicalguidelinesfor pages 6-8) | (bormans2024experienceina pages 1-2, baran2021theclinicalspectrum pages 3-4, takayama2023clinicalguidelinesfor pages 6-8) |
| Neurodevelopmental delay / intellectual disability / autism spectrum disorder | HP:0001263 Developmental delay; HP:0001249 Intellectual disability; HP:0000729 Autism | Often prominent in childhood and can drive referral for testing; neurobehavioral phenotype appears relatively stable over time in longitudinal study | Developmental delay in 5/11 children in one cohort; in 81 children, DD/ID present in 42.0% and ASD in 27.2%; guideline review reports ASD in ~17% of PTEN variant carriers, PTEN variants in 10–20% of ASD with macrocephaly, and intellectual disability in 12–20%; review notes PTEN mutations found in 1–27% of ASD with macrocephaly (martinvalbuena2024ptenhamartomatumor pages 1-2, baran2021theclinicalspectrum pages 3-4, takayama2023clinicalguidelinesfor pages 6-8, pilarski2019ptenhamartomatumor pages 5-7) | (martinvalbuena2024ptenhamartomatumor pages 1-2, baran2021theclinicalspectrum pages 3-4, takayama2023clinicalguidelinesfor pages 6-8, pilarski2019ptenhamartomatumor pages 5-7) |
| Vascular malformations / vascular anomalies | HP:0005306 Vascular malformation | May occur in childhood or adulthood; often part of BRRS/PHTS overlap and may be under-recognized | Guideline review reports multiple vascular malformations in approximately half of patients; pediatric surveillance paper lists vascular malformations among recognized manifestations but does not quantify them in that cohort (takayama2023clinicalguidelinesfor pages 6-8, bormans2024experienceina pages 1-2) | (takayama2023clinicalguidelinesfor pages 6-8, bormans2024experienceina pages 1-2) |
| Lhermitte–Duclos disease (dysplastic cerebellar gangliocytoma) | HP:0006887 Dysplastic cerebellar gangliocytoma | Classically associated with adult disease, often diagnosed in 20s–30s, but cerebellar dysplasia/LDD-compatible imaging can be seen earlier | ~6% prevalence in guideline review; overlap of LDD patients with Cowden syndrome reported at ~50%; one pediatric cohort had a patient with cortical cerebellar dysplasia compatible with LDD (takayama2023clinicalguidelinesfor pages 6-8, martinvalbuena2024ptenhamartomatumor pages 6-7, pilarski2019ptenhamartomatumor pages 3-5) | (takayama2023clinicalguidelinesfor pages 6-8, martinvalbuena2024ptenhamartomatumor pages 6-7, pilarski2019ptenhamartomatumor pages 3-5) |


*Table: This table summarizes major clinical phenotypes reported for Cowden syndrome/PTEN hamartoma tumor syndrome, with suggested HPO terms, timing, and quantitative frequencies from recent and key studies. It is useful for phenotype curation and knowledge base population.*

### Quality-of-life impact (selected)
Direct quality-of-life (EQ-5D/SF-36/PROMIS) statistics were not identified in retrieved sources. However, multiple phenotypes have substantial functional impacts: neurodevelopmental disorders (developmental delay, ASD), obstructive sleep apnea related to tonsillar pathology, and repeated cancer surveillance/surgery burden. (baran2021theclinicalspectrum pages 3-4, bormans2024experienceina pages 1-2)


## 4. Genetic / Molecular Information

### 4.1 Causal gene(s)
- **PTEN** is the primary causal gene for Cowden syndrome/PHTS in the retrieved sources. (pirlog2024insightsintoclinical pages 1-2, takayama2023clinicalguidelinesfor pages 2-4)

### 4.2 Pathogenic variant classes and consequences (high-level)
- PTEN pathogenic variants may be truncating (nonsense/frameshift), missense, splice-site, or structural; functionally, many act via **loss of function** leading to elevated PI3K pathway signaling and impaired genome-stability functions. (yehia2020ptenhamartomatumour pages 5-6, wei2024quantitativeevaluationof pages 1-2)
- In patient-derived lymphoblastoid cell lines, PTEN **nonsense variants** were associated with less efficient DNA damage repair dynamics (higher residual damage at 24 hours after irradiation) compared with missense variants, supporting a genotype-linked difference in genome integrity phenotypes. (wei2024quantitativeevaluationof pages 1-2)

### 4.3 Non-PTEN genetic etiologies / phenocopies
When a patient has a PHTS/CS-like phenotype but lacks a germline PTEN variant, germline activating variants in PI3K-pathway genes (e.g., **AKT1, PIK3CA**) can phenocopy PTEN loss, with increased AKT phosphorylation and increased PIP3 levels observed in patient-derived cells—“mimicking effects of PTEN loss-of-function.” (yehia2020ptenhamartomatumour pages 8-9)

### 4.4 Modifier genes / genomic background
No definitive modifier genes were established from retrieved sources in this run (beyond pathway-related phenocopies above).

### 4.5 Epigenetic information
No epigenetic mechanisms (e.g., methylation signatures) were identified in retrieved sources.

### 4.6 Chromosomal abnormalities
No recurrent chromosomal abnormalities were identified in retrieved sources.


## 5. Environmental Information

### 5.1 Environmental and lifestyle factors
Direct environmental risk factors for CS/PHTS were not identified in retrieved sources. The disease is primarily genetic.


## 6. Mechanism / Pathophysiology

### 6.1 Core molecular pathway mechanism (upstream → downstream)
1) **Trigger:** germline PTEN loss-of-function (heterozygous) (pirlog2024insightsintoclinical pages 1-2)
2) **Molecular effect:** reduced dephosphorylation of PIP3 → increased PIP3 and increased AKT activation → increased downstream growth signaling including mTOR activity (yehia2020ptenhamartomatumour pages 5-6, pirlog2024insightsintoclinical pages 1-2)
3) **Cellular consequences:** increased proliferation/survival and disordered growth leading to hamartomas/overgrowth; tumor predisposition due to growth signaling plus PTEN roles in nuclear genome stability and DNA double-strand break repair (yehia2020ptenhamartomatumour pages 5-6)
4) **Clinical outcomes:** multisystem hamartomas (skin/oral mucosa, GI tract, thyroid, breast, etc.) and increased cancer risks with earlier onset (pirlog2024insightsintoclinical pages 1-2, cummings2023cancerriskassociated pages 1-2)

### 6.2 Genome integrity / DNA damage response as a contributor to pleiotropy
PTEN has non-canonical roles relevant to “maintenance of genome integrity,” and quantitative DNA damage response modeling in PTEN-variant patient cell lines showed variant-class and phenotype associations (e.g., less efficient repair in nonsense variants; different repair dynamics in ASD/DD vs cancer phenotypic subgroups), providing a mechanistic framework for pleiotropic outcomes. (wei2024quantitativeevaluationof pages 1-2)

### 6.3 Immune dysregulation (emerging/variable evidence)
Immune dysregulation is increasingly reported in PHTS. A 2024 case report links PTEN mutation and immune dysregulation in the context of systemic lupus erythematosus (SLE), emphasizing PTEN’s regulation of PI3K/AKT/mTOR signaling relevant to immune function. (drozdz2024severelupusnephritis pages 1-2)

### Suggested ontology terms
- **GO Biological Process (examples):** PI3K signaling (e.g., “phosphatidylinositol 3-kinase signaling”); regulation of cell proliferation; DNA repair / double-strand break repair; regulation of apoptosis (mechanistically supported by PTEN roles described in retrieved sources) (yehia2020ptenhamartomatumour pages 5-6, wei2024quantitativeevaluationof pages 1-2)
- **Cell types (CL suggestions, examples):** epithelial cells (breast/thyroid/endometrium), colonic epithelial cells; endothelial cells (vascular malformations noted clinically); lymphocytes (immune dysregulation discussions) (takayama2023clinicalguidelinesfor pages 6-8, drozdz2024severelupusnephritis pages 1-2)


## 7. Anatomical Structures Affected

### 7.1 Organ-level involvement (primary)
Commonly involved organs/systems include:
- **Skin and mucous membranes** (mucocutaneous lesions) (takayama2023clinicalguidelinesfor pages 2-4, pilarski2019ptenhamartomatumor pages 5-7)
- **Gastrointestinal tract** (hamartomatous polyps; constipation/feeding issues in children) (takayama2023clinicalguidelinesfor pages 6-8, liu2024abiinstitutionalstudy pages 1-2)
- **Thyroid** (nodules, goiter, autoimmune thyroiditis, differentiated thyroid carcinoma) (bormans2024experienceina pages 1-2)
- **Breast, endometrium, kidney, colon** (cancer predisposition) (cummings2023cancerriskassociated pages 1-2, hendricks2021areviewon pages 1-4)
- **Central nervous system** (macrocephaly; MRI abnormalities; Lhermitte–Duclos disease) (pilarski2019ptenhamartomatumor pages 5-7, takayama2023clinicalguidelinesfor pages 6-8)

### 7.2 Tissue/cell-level and subcellular notes
At a mechanistic level, PTEN functions at the **plasma membrane** (PIP3→PIP2 dephosphorylation) and in the **nucleus** (genomic stability/cell cycle regulation), providing plausible cross-tissue impact on growth and tumor suppression. (yehia2020ptenhamartomatumour pages 5-6)

### 7.3 UBERON term suggestions (examples)
- Thyroid gland; breast; endometrium; colon; kidney; cerebellum; skin; oral mucosa; gastrointestinal tract (supported by multisystem involvement described in guidelines/reviews) (takayama2023clinicalguidelinesfor pages 2-4, takayama2023clinicalguidelinesfor pages 6-8)


## 8. Temporal Development

### 8.1 Onset and progression
- Many individuals demonstrate early manifestations such as macrocephaly and neurodevelopmental concerns in childhood, whereas mucocutaneous lesions and some cancer manifestations often become more apparent in adolescence/adulthood. (martinvalbuena2024ptenhamartomatumor pages 1-2, baran2021theclinicalspectrum pages 3-4)
- Median age at cancer diagnosis has been reported around **36 years** in CS/PHTS cohorts summarized in reviews. (pirlog2024insightsintoclinical pages 1-2, hendricks2021areviewon pages 1-4)


## 9. Inheritance and Population

### 9.1 Inheritance
CS/PHTS is **autosomal dominant** due to heterozygous germline PTEN pathogenic variants. (pirlog2024insightsintoclinical pages 1-2, takayama2023clinicalguidelinesfor pages 2-4)

### 9.2 Penetrance and expressivity
CS/PHTS shows high penetrance with variable expressivity; one pediatric cohort report cites penetrance approaching ~100% by the fourth decade for pathogenic PTEN variants and reports de novo rates from ~10.7% to 47.6% (range across literature). (martinvalbuena2024ptenhamartomatumor pages 1-2)

### 9.3 Epidemiology
A commonly cited prevalence/incidence estimate for Cowden syndrome/PHTS in reviews is approximately **1 in 200,000**, while multiple sources emphasize that true incidence is uncertain and likely under-recognized. (pirlog2024insightsintoclinical pages 1-2, hendricks2021areviewon pages 1-4)

### 9.4 Recent population-level genetic testing statistic
In a large hereditary cancer panel-testing cohort (testing 2013–2022), **PTEN pathogenic variants were detected in 0.027% (193/727,091)** of tested individuals. (cummings2023cancerriskassociated pages 1-2)


## 10. Diagnostics

### 10.1 Clinical criteria and diagnostic framework
- Contemporary clinical diagnosis commonly uses frameworks aligned with **NCCN criteria** for CS/PHTS; the Japanese 2023 guideline explicitly adopted an NCCN-based framework (noting 8 major and 10 minor criteria) and provides a diagnostic flowchart. (takayama2023clinicalguidelinesfor pages 2-4)
- Because clinical criteria and PTEN variant detection incompletely overlap (only a subset meeting CS criteria have PTEN variants), diagnosis may be made clinically even if genetic testing is negative/unavailable, but this complicates gene-informed risk assessment. (pilarski2019ptenhamartomatumor pages 1-3, yehia2020ptenhamartomatumour pages 8-9)

### 10.2 Genetic testing approach (current understanding)
Multigene cancer predisposition panels and targeted PTEN testing are used in clinical practice and can identify PTEN PVs even in individuals not previously recognized clinically as having CS. The panel-testing cohort study emphasizes that risk estimates derived purely from clinically diagnosed CS cohorts may be biased, motivating genotype-based risk modeling. (cummings2023cancerriskassociated pages 1-2)

### 10.3 Differential diagnosis (selected)
PTEN-wildtype CS-like phenotypes may be due to variants in PI3K-pathway genes (e.g., AKT1, PIK3CA), which can mimic PTEN loss, reinforcing the need for differential genetic evaluation in PTEN-negative cases. (yehia2020ptenhamartomatumour pages 8-9)


## 11. Outcome / Prognosis

### 11.1 Cancer risk burden (statistics from cohorts)
Aggregated cohort data summarized in a 2021 review report **cumulative lifetime risk for any cancer of 81%–90%** in PHTS, with wide ranges by cancer site (female breast 67%–85% by age 60–70; endometrium 19%–28%; thyroid 6%–38%; renal 2%–24%; colorectal 9%–32%; melanoma 0%–6%). (hendricks2021areviewon pages 1-4)

### 11.2 Surveillance yield (real-world implementation data)
In a PHTS expertise center cohort (children screened by thyroid ultrasound before 18 years), **2/43 (5%)** had differentiated thyroid carcinoma (ages 12 and 17), and **84%** had thyroid abnormalities (mostly benign), illustrating high surveillance burden and nontrivial detection yield. (bormans2024experienceina pages 1-2)


## 12. Treatment

### 12.1 Standard treatments
Cancers in CS/PHTS are generally treated according to standard organ-specific oncology/surgical care pathways; no PHTS-specific renal cancer treatment evidence was found in the retrieved guideline excerpt, which notes following sporadic RCC management. (takayama2023clinicalguidelinesfor pages 8-11)

### 12.2 Targeted/experimental therapeutics (mechanism-informed)
Guidelines and reviews note that **PI3K/AKT/mTOR pathway inhibitors** are being investigated clinically because PTEN inactivation converges on this pathway. (takayama2023clinicalguidelinesfor pages 8-11)

**MAXO term suggestions (examples):** cancer surveillance; breast MRI screening; thyroid ultrasound screening; colonoscopy; nephrologic imaging surveillance; prophylactic mastectomy (consideration) (tischkowitz2020cancersurveillanceguideline pages 2-4, takayama2023clinicalguidelinesfor pages 8-11)


## 13. Prevention

Because CS/PHTS is Mendelian, prevention focuses on **secondary prevention (early cancer detection via surveillance)** rather than primary prevention.

### 13.1 Surveillance (secondary prevention): key guideline recommendations
The ERN GENTURIS guideline provides organ-specific surveillance with evidence-strength grading.

Key schedule elements (also shown in the guideline’s table image):
- **Breast:** annual MRI from age 30; mammography every 2 years from age 40 (tischkowitz2020cancersurveillanceguideline pages 2-4, tischkowitz2020cancersurveillanceguideline media 2ffc24d6)
- **Thyroid:** annual ultrasound from ~age 18 (tischkowitz2020cancersurveillanceguideline pages 2-4, tischkowitz2020cancersurveillanceguideline media 2ffc24d6)
- **Renal:** ultrasound every 2 years from age ~40 (tischkowitz2020cancersurveillanceguideline pages 2-4, tischkowitz2020cancersurveillanceguideline media 2ffc24d6)
- **Colon:** baseline colonoscopy at 35–40 to assess polyp load (tischkowitz2020cancersurveillanceguideline pages 2-4, tischkowitz2020cancersurveillanceguideline media 2ffc24d6)
- **Endometrium:** routine screening not recommended; consider within trials (tischkowitz2020cancersurveillanceguideline pages 2-4)

The Japanese guideline (NCCN-aligned) recommends earlier surveillance for some sites:
- **Breast:** self-exam from 18; clinical exams from 25; annual mammography + contrast MRI from 30 (or 5–10 years earlier than the youngest family diagnosis) (takayama2023clinicalguidelinesfor pages 8-11)
- **Thyroid:** annual ultrasound from diagnosis, including in children, motivated by pediatric thyroid cancer reports (earliest age 7; ~5% risk <20 years cited) (takayama2023clinicalguidelinesfor pages 11-12, takayama2023clinicalguidelinesfor pages 8-11)

| Cancer site | Reported risk estimates | ERN GENTURIS / European guideline start age & modality | NCCN / Japanese guideline start age & modality | Evidence strength (if stated) | Notes / controversies |
|---|---|---|---|---|---|
| Breast | Female breast cancer CLTR 67%–85% by age 60–70 in prior cohorts; PTEN PVs associated with OR 7.88 (95% CI 5.57–11.16) in a panel-testing cohort (hendricks2021areviewon pages 1-4, cummings2023cancerriskassociated pages 1-2) | Annual breast MRI from age 30; mammography every 2 years from age 40; risk-reducing surgery may be offered (tischkowitz2020cancersurveillanceguideline pages 2-4, tischkowitz2020cancersurveillanceguideline pages 4-5, tischkowitz2020cancersurveillanceguideline media 2ffc24d6) | Monthly self-exam from 18; clinical breast exam/interview from 25 or 5–10 years before youngest family cancer; annual mammography plus gadolinium-enhanced breast MRI from 30 or 5–10 years before youngest familial onset (takayama2023clinicalguidelinesfor pages 8-11) | MRI: Strong; mammography/risk-reducing surgery: Moderate (tischkowitz2020cancersurveillanceguideline pages 2-4, tischkowitz2020cancersurveillanceguideline pages 4-5) | Lifetime risk estimates vary widely across cohorts because of ascertainment bias; Takayama notes no evidence that prophylactic mastectomy improves overall survival (hendricks2021areviewon pages 1-4, takayama2023clinicalguidelinesfor pages 8-11) |
| Thyroid | Thyroid cancer CLTR 6%–38% in review cohorts; historical/literature estimates often 10%–35%; PTEN PVs associated with OR 4.88 (95% CI 2.64–9.01); pediatric DTC estimates 4%–12%; in one pediatric surveillance cohort, 2/43 (5%) had DTC and 84% had thyroid abnormalities (hendricks2021areviewon pages 1-4, pilarski2019ptenhamartomatumor pages 3-5, cummings2023cancerriskassociated pages 1-2, bormans2024experienceina pages 1-2) | Annual thyroid ultrasound from about age 18 (table lists 18a) (tischkowitz2020cancersurveillanceguideline pages 2-4, tischkowitz2020cancersurveillanceguideline pages 4-5, tischkowitz2020cancersurveillanceguideline media 2ffc24d6) | Annual thyroid ultrasonography at diagnosis, including childhood; rationale includes thyroid cancer reported at age 7 and ~5% risk in patients <20 years (takayama2023clinicalguidelinesfor pages 11-12, takayama2023clinicalguidelinesfor pages 8-11) | Strong (tischkowitz2020cancersurveillanceguideline pages 2-4, tischkowitz2020cancersurveillanceguideline pages 4-5) | Major divergence between guidelines: ERN starts around 18, while NCCN/Japanese guidance starts in childhood/at diagnosis; pediatric series support earlier surveillance in expertise centers, sometimes from age 12 (pirlog2024insightsintoclinical pages 11-12, takayama2023clinicalguidelinesfor pages 11-12, bormans2024experienceina pages 1-2) |
| Endometrial | Endometrial cancer CLTR 19%–28%; PTEN PVs associated with OR 13.51 (95% CI 8.77–20.83) (hendricks2021areviewon pages 1-4, pilarski2019ptenhamartomatumor pages 3-5, cummings2023cancerriskassociated pages 1-2) | Routine screening not recommended; if surveillance is offered, guideline suggests this should preferably be in clinical trials, and if offered probably at least annually (tischkowitz2020cancersurveillanceguideline pages 2-4, tischkowitz2020cancersurveillanceguideline pages 4-5) | Yearly transvaginal ultrasound or endometrial biopsy beginning at age 30 (Japanese guideline) (takayama2023clinicalguidelinesfor pages 11-12) | Weak (tischkowitz2020cancersurveillanceguideline pages 2-4, tischkowitz2020cancersurveillanceguideline pages 4-5) | Substantial controversy: ERN does not recommend routine endometrial surveillance outside trials, whereas Japanese/NCCN-derived guidance is more proactive; evidence base remains limited (pirlog2024insightsintoclinical pages 11-12, takayama2023clinicalguidelinesfor pages 11-12) |
| Colorectal | Colorectal cancer CLTR 9%–32% in review cohorts; prevalence in cohorts often 9%–13%; one estimate 9% lifetime and another 16%; PTEN PVs strongly associated with colon polyposis OR 31.60 (95% CI 15.60–64.02) (hendricks2021areviewon pages 1-4, pilarski2019ptenhamartomatumor pages 3-5, cummings2023cancerriskassociated pages 1-2) | Baseline colonoscopy at age 35–40 to assess polyp load; if normal, follow general-population screening, with further surveillance as required (tischkowitz2020cancersurveillanceguideline pages 2-4, tischkowitz2020cancersurveillanceguideline pages 4-5, tischkowitz2020cancersurveillanceguideline media 2ffc24d6) | Total colonoscopy 5–10 years before age 35 or before youngest family cancer onset; interval depends on degree of polyposis; adenomatous polyps ≥6 mm should be resected (takayama2023clinicalguidelinesfor pages 11-12) | Moderate for baseline colonoscopy (tischkowitz2020cancersurveillanceguideline pages 2-4, tischkowitz2020cancersurveillanceguideline pages 4-5) | Risk may be lower than historically estimated; a surveillance cohort found no CRCs over 67 follow-up years, supporting personalized intervals rather than uniformly intensive screening (tischkowitz2020cancersurveillanceguideline pages 1-2, takayama2023clinicalguidelinesfor pages 11-12) |
| Renal | Renal cancer CLTR 2%–24% in review cohorts; some small studies projected up to ~34% lifetime risk, likely overestimated (hendricks2021areviewon pages 1-4, pilarski2019ptenhamartomatumor pages 3-5) | Renal ultrasound every 2 years starting about age 40 (tischkowitz2020cancersurveillanceguideline pages 2-4, tischkowitz2020cancersurveillanceguideline pages 4-5, tischkowitz2020cancersurveillanceguideline media 2ffc24d6) | Annual renal ultrasonography from age 40; some sources mention CT or preferably MRI if needed (takayama2023clinicalguidelinesfor pages 11-12, jurca2023anewframeshift pages 9-10) | Moderate (tischkowitz2020cancersurveillanceguideline pages 2-4, tischkowitz2020cancersurveillanceguideline pages 4-5) | ERN notes insufficient data to recommend renal MRI routinely; early-onset RCC case reports have prompted debate about lowering surveillance age, but this is not standardized (tischkowitz2020cancersurveillanceguideline pages 4-5, jurca2023anewframeshift pages 9-10) |
| Melanoma / skin | Melanoma CLTR 0%–6%; evidence for increased melanoma risk remains limited, with some cohorts showing ~1% prevalence and others projecting 6% lifetime (hendricks2021areviewon pages 1-4, pilarski2019ptenhamartomatumor pages 3-5) | Baseline skin examination around age 30; no strong recommendation for additional routine surveillance beyond this (tischkowitz2020cancersurveillanceguideline pages 2-4, tischkowitz2020cancersurveillanceguideline pages 4-5, tischkowitz2020cancersurveillanceguideline media 2ffc24d6) | No explicit melanoma screening schedule retrieved in Takayama 2023; strong recommendation for dermatology referral to assess mucocutaneous lesions (takayama2023clinicalguidelinesfor pages 11-12) | Weak (tischkowitz2020cancersurveillanceguideline pages 2-4, tischkowitz2020cancersurveillanceguideline pages 4-5) | Skin surveillance is limited by uncertain melanoma risk, but dermatologic evaluation remains clinically valuable because mucocutaneous lesions are prominent and may support diagnosis (tischkowitz2020cancersurveillanceguideline pages 4-5, takayama2023clinicalguidelinesfor pages 11-12) |


*Table: This table summarizes site-specific cancer risk estimates and surveillance recommendations for Cowden syndrome/PTEN hamartoma tumor syndrome. It contrasts ERN GENTURIS and NCCN/Japanese approaches and highlights where evidence is strong versus where recommendations remain controversial.*


## 14. Other Species / Natural Disease

No naturally occurring CS/PHTS analogs in non-human species were identified in retrieved sources in this run.


## 15. Model Organisms

Model organism evidence was not deeply extracted in this run; however, multiple reviews highlight that PTEN function and tumor suppression mechanisms are conserved across species and have been studied in zebrafish and Drosophila models (e.g., for tumorigenesis and variant functional assays), supporting mechanistic inference for PTEN loss. (yehia2020ptenhamartomatumour pages 5-6)


# Recent developments and latest research (prioritizing 2023–2024)

## 2023–2024 high-value sources retrieved in this run
- **Japanese clinical guideline (2023-10-XX)** providing English secondary publication and emphasizing NCCN-aligned diagnosis/management and the need for surveillance across breast/thyroid/endometrium/colon/kidney (Takayama et al., 2023; URL: https://doi.org/10.23922/jarc.2023-028). (takayama2023clinicalguidelinesfor pages 2-4, takayama2023clinicalguidelinesfor pages 8-11)
- **Large-scale panel-testing risk quantification (2023-01-XX)** providing genotype-based ORs for major cancers and colon polyposis (Cummings et al., 2023; URL: https://doi.org/10.1200/po.22.00415). (cummings2023cancerriskassociated pages 1-2)
- **Pediatric GI/hepatic bi-institutional cohort (2024-01-XX)** quantifying constipation, feeding issues, and pediatric polyp frequency in 80 children (Liu et al., 2024; URL: https://doi.org/10.1016/j.gastha.2023.10.012). (liu2024abiinstitutionalstudy pages 1-2)
- **Pediatric thyroid surveillance implementation study (2024-08-XX)** describing high detection of benign thyroid abnormalities and DTC yield (Bormans et al., 2024; URL: https://doi.org/10.4274/jcrpe.galenos.2024.2024-3-14). (bormans2024experienceina pages 1-2)
- **Mechanistic DDR phenotyping + modeling (2024-10-XX)** linking PTEN variant class to DNA repair dynamics and exploring phenotype prediction (Wei et al., 2024; URL: https://doi.org/10.1371/journal.pcbi.1012449). (wei2024quantitativeevaluationof pages 1-2)
- **Comprehensive CS clinical review (2024-05-XX)** summarizing multisystem manifestations and describing inter-guideline differences (Pîrlog et al., 2024; URL: https://doi.org/10.3390/medicina60050767). (pirlog2024insightsintoclinical pages 2-4, pirlog2024insightsintoclinical pages 11-12)


# Embedded summary artifacts

| Concept | MONDO ID | OMIM | Key synonyms/related syndromes | Causal gene | Inheritance | Notes on ascertainment |
|---|---|---|---|---|---|---|
| Cowden syndrome | MONDO_0008021 (Cowden syndrome 1); MONDO_0016063 (Cowden disease) | 158350 | Cowden disease; Cowden syndrome (CS); related PTEN-spectrum entities include Bannayan–Riley–Ruvalcaba syndrome (BRRS), Proteus syndrome, Proteus-like syndrome, adult Lhermitte–Duclos disease | PTEN | Autosomal dominant | Clinical and molecular diagnosis do not fully overlap: only ~30–35% of individuals meeting clinical CS criteria have a detectable PTEN variant in cited reviews; diagnosis may be made clinically and/or by multigene panel testing (pilarski2019ptenhamartomatumor pages 1-3, pirlog2024insightsintoclinical pages 1-2, takayama2023clinicalguidelinesfor pages 2-4) |
| PTEN hamartoma tumor syndrome (PHTS) umbrella | Not found in retrieved sources | Not found in retrieved sources | PTEN hamartoma tumour/tumor syndrome; umbrella including Cowden syndrome, BRRS, Proteus syndrome, Proteus-like syndrome, and adult Lhermitte–Duclos disease; autism spectrum disorder with macrocephaly is also described within the PTEN-related spectrum | PTEN | Autosomal dominant | PHTS is an umbrella term for PTEN-related disorders; PTEN pathogenic variants were found in only a subset of clinically diagnosed phenotypes (e.g., ~30–35% of CS/CS-like and ~60% of BRRS in cited reviews), underscoring phenotype–genotype heterogeneity and ascertainment differences between clinically defined and genetically confirmed cohorts (cummings2023cancerriskassociated pages 1-2, pilarski2019ptenhamartomatumor pages 1-3, pirlog2024insightsintoclinical pages 1-2) |


*Table: This table summarizes the key identifiers, synonyms, causal gene, and inheritance for Cowden syndrome and the broader PTEN hamartoma tumor syndrome umbrella. It also highlights the important distinction between clinical diagnosis and genetically confirmed PTEN-associated disease.*


# Key guideline table image (visual evidence)

The extracted table image from the ERN GENTURIS surveillance guideline (European Journal of Human Genetics, 2020) summarizes screening start ages and modalities across organ sites. (tischkowitz2020cancersurveillanceguideline media 2ffc24d6)


# Notes on evidence gaps (from retrieved sources in this run)
- **ICD-10/ICD-11, Orphanet, MeSH identifiers** were not present in retrieved sources in this run; inclusion would require targeted retrieval from OMIM/Orphanet/WHO/NCBI MeSH.
- **Quality-of-life instruments**, **formal epidemiologic incidence**, and **long-term survival statistics** were not directly retrieved.
- **Animal model and comparative disease** sections were not fully supported by extracted evidence in this run; additional targeted model-organism papers could strengthen this component.


References

1. (pirlog2024insightsintoclinical pages 1-2): Lorin-Manuel Pîrlog, Andrada-Adelaida Pătrășcanu, Mariela Sanda Militaru, and Andreea Cătană. Insights into clinical disorders in cowden syndrome: a comprehensive review. Medicina, 60:767, May 2024. URL: https://doi.org/10.3390/medicina60050767, doi:10.3390/medicina60050767. This article has 10 citations.

2. (takayama2023clinicalguidelinesfor pages 2-4): Tetsuji Takayama, Naoki Muguruma, Masahiro Igarashi, Shozo Ohsumi, Shiro Oka, Fumihiko Kakuta, Yoshiaki Kubo, Hideki Kumagai, Mika Sasaki, Tamotsu Sugai, Kokichi Sugano, Yuko Takeda, Hisashi Doyama, Kouji Banno, Suguru Fukahori, Yoichi Furukawa, Takahiro Horimatsu, Hideki Ishikawa, Takeo Iwama, Yasushi Okazaki, Yutaka Saito, Nariaki Matsuura, Michihiro Mutoh, Naohiro Tomita, Takashi Akiyama, Toshiki Yamamoto, Hideyuki Ishida, and Yoshiko Nakayama. Clinical guidelines for diagnosis and management of cowden syndrome/pten hamartoma tumor syndrome in children and adults―secondary publication. Journal of the Anus, Rectum and Colon, 7:284-300, Oct 2023. URL: https://doi.org/10.23922/jarc.2023-028, doi:10.23922/jarc.2023-028. This article has 43 citations.

3. (cummings2023cancerriskassociated pages 1-2): Shelly Cummings, Andrew Alfonso, Elisha Hughes, Matt Kucera, Brent Mabey, Nanda Singh, and Charis Eng. Cancer risk associated with pten pathogenic variants identified using multigene hereditary cancer panel testing. JCO Precision Oncology, Jan 2023. URL: https://doi.org/10.1200/po.22.00415, doi:10.1200/po.22.00415. This article has 29 citations and is from a peer-reviewed journal.

4. (jurca2023anewframeshift pages 9-10): Claudia Maria Jurca, Ovidiu Frățilă, Tiberia Iliaș, Aurora Jurca, Andreea Cătana, Corina Moisa, and Alexandru Daniel Jurca. A new frameshift mutation of pten gene associated with cowden syndrome—case report and brief review of the literature. Genes, 14:1909, Oct 2023. URL: https://doi.org/10.3390/genes14101909, doi:10.3390/genes14101909. This article has 9 citations.

5. (pilarski2019ptenhamartomatumor pages 1-3): Robert Pilarski. Pten hamartoma tumor syndrome: a clinical overview. Cancers, 11:844, Jun 2019. URL: https://doi.org/10.3390/cancers11060844, doi:10.3390/cancers11060844. This article has 232 citations.

6. (hendricks2021areviewon pages 1-4): Linda A.J. Hendricks, Nicoline Hoogerbrugge, Janneke H.M. Schuurs‐Hoeijmakers, and Janet R. Vos. A review on age‐related cancer risks in <scp>pten</scp> hamartoma tumor syndrome. Clinical Genetics, 99:219-225, Nov 2021. URL: https://doi.org/10.1111/cge.13875, doi:10.1111/cge.13875. This article has 93 citations and is from a peer-reviewed journal.

7. (pilarski2019ptenhamartomatumor pages 3-5): Robert Pilarski. Pten hamartoma tumor syndrome: a clinical overview. Cancers, 11:844, Jun 2019. URL: https://doi.org/10.3390/cancers11060844, doi:10.3390/cancers11060844. This article has 232 citations.

8. (yehia2020ptenhamartomatumour pages 5-6): Lamis Yehia and Charis Eng. Pten hamartoma tumour syndrome: what happens when there is no pten germline mutation? Human molecular genetics, 29:R150-R157, Jun 2020. URL: https://doi.org/10.1093/hmg/ddaa127, doi:10.1093/hmg/ddaa127. This article has 23 citations and is from a domain leading peer-reviewed journal.

9. (martinvalbuena2024ptenhamartomatumor pages 1-2): Jesús Martín-Valbuena, Nerea Gestoso-Uzal, María Justel-Rodríguez, María Isidoro-García, Elena Marcos-Vadillo, Sandra Milagros Lorenzo-Hernández, M. Carla Criado-Muriel, and Pablo Prieto-Matos. Pten hamartoma tumor syndrome: clinical and genetic characterization in pediatric patients. Child's Nervous System, 40:1689-1697, Feb 2024. URL: https://doi.org/10.1007/s00381-024-06301-2, doi:10.1007/s00381-024-06301-2. This article has 9 citations.

10. (baran2021theclinicalspectrum pages 3-4): Julia A. Baran, Steven D. Tsai, Amber Isaza, Garrett M. Brodeur, Suzanne P. MacFarland, Kristin Zelley, Denise M. Adams, Aime T. Franco, and Andrew J. Bauer. The clinical spectrum of pten hamartoma tumor syndrome: exploring the value of thyroid surveillance. Hormone Research in Paediatrics, 93:634-642, Apr 2021. URL: https://doi.org/10.1159/000515731, doi:10.1159/000515731. This article has 21 citations and is from a peer-reviewed journal.

11. (pilarski2019ptenhamartomatumor pages 5-7): Robert Pilarski. Pten hamartoma tumor syndrome: a clinical overview. Cancers, 11:844, Jun 2019. URL: https://doi.org/10.3390/cancers11060844, doi:10.3390/cancers11060844. This article has 232 citations.

12. (takayama2023clinicalguidelinesfor pages 6-8): Tetsuji Takayama, Naoki Muguruma, Masahiro Igarashi, Shozo Ohsumi, Shiro Oka, Fumihiko Kakuta, Yoshiaki Kubo, Hideki Kumagai, Mika Sasaki, Tamotsu Sugai, Kokichi Sugano, Yuko Takeda, Hisashi Doyama, Kouji Banno, Suguru Fukahori, Yoichi Furukawa, Takahiro Horimatsu, Hideki Ishikawa, Takeo Iwama, Yasushi Okazaki, Yutaka Saito, Nariaki Matsuura, Michihiro Mutoh, Naohiro Tomita, Takashi Akiyama, Toshiki Yamamoto, Hideyuki Ishida, and Yoshiko Nakayama. Clinical guidelines for diagnosis and management of cowden syndrome/pten hamartoma tumor syndrome in children and adults―secondary publication. Journal of the Anus, Rectum and Colon, 7:284-300, Oct 2023. URL: https://doi.org/10.23922/jarc.2023-028, doi:10.23922/jarc.2023-028. This article has 43 citations.

13. (martinvalbuena2024ptenhamartomatumor pages 2-3): Jesús Martín-Valbuena, Nerea Gestoso-Uzal, María Justel-Rodríguez, María Isidoro-García, Elena Marcos-Vadillo, Sandra Milagros Lorenzo-Hernández, M. Carla Criado-Muriel, and Pablo Prieto-Matos. Pten hamartoma tumor syndrome: clinical and genetic characterization in pediatric patients. Child's Nervous System, 40:1689-1697, Feb 2024. URL: https://doi.org/10.1007/s00381-024-06301-2, doi:10.1007/s00381-024-06301-2. This article has 9 citations.

14. (liu2024abiinstitutionalstudy pages 1-2): Darren Liu, Suzanne P. MacFarland, Lamis Yehia, Melani M. Duvall, Petar Mamula, Jacob A. Kurowski, Colleen S. Greene, Kadakkal Radhakrishnan, and Charis Eng. A bi-institutional study of gastrointestinal and hepatic manifestations in children with pten hamartoma tumor syndrome. Gastro Hep Advances, 3:250-259, Jan 2024. URL: https://doi.org/10.1016/j.gastha.2023.10.012, doi:10.1016/j.gastha.2023.10.012. This article has 4 citations and is from a peer-reviewed journal.

15. (bormans2024experienceina pages 1-2): Esther M.G. Bormans, Janneke H.M. Schuurs-Hoeijmakers, Petra van Setten, Linda A.J. Hendricks, Meggie M.C.M. Drissen, Martin Gotthardt, Hedi L. Claahsen-van der Grinten, Nicoline Hoogerbrugge, and Jolanda H. Schieving. Experience in a pten hamartoma tumor syndrome expertise centre: yield of thyroid ultrasound surveillance in children with pten hamartoma tumor syndrome. Journal of Clinical Research in Pediatric Endocrinology, 17:46-57, Aug 2024. URL: https://doi.org/10.4274/jcrpe.galenos.2024.2024-3-14, doi:10.4274/jcrpe.galenos.2024.2024-3-14. This article has 2 citations.

16. (martinvalbuena2024ptenhamartomatumor pages 6-7): Jesús Martín-Valbuena, Nerea Gestoso-Uzal, María Justel-Rodríguez, María Isidoro-García, Elena Marcos-Vadillo, Sandra Milagros Lorenzo-Hernández, M. Carla Criado-Muriel, and Pablo Prieto-Matos. Pten hamartoma tumor syndrome: clinical and genetic characterization in pediatric patients. Child's Nervous System, 40:1689-1697, Feb 2024. URL: https://doi.org/10.1007/s00381-024-06301-2, doi:10.1007/s00381-024-06301-2. This article has 9 citations.

17. (wei2024quantitativeevaluationof pages 1-2): Ruipeng Wei, Masahiro Hitomi, Tammy Sadler, Lamis Yehia, Daniela Calvetti, Jacob Scott, and Charis Eng. Quantitative evaluation of dna damage repair dynamics to elucidate predictors of autism vs. cancer in individuals with germline pten variants. PLOS Computational Biology, 20:e1012449, Oct 2024. URL: https://doi.org/10.1371/journal.pcbi.1012449, doi:10.1371/journal.pcbi.1012449. This article has 4 citations and is from a highest quality peer-reviewed journal.

18. (yehia2020ptenhamartomatumour pages 8-9): Lamis Yehia and Charis Eng. Pten hamartoma tumour syndrome: what happens when there is no pten germline mutation? Human molecular genetics, 29:R150-R157, Jun 2020. URL: https://doi.org/10.1093/hmg/ddaa127, doi:10.1093/hmg/ddaa127. This article has 23 citations and is from a domain leading peer-reviewed journal.

19. (drozdz2024severelupusnephritis pages 1-2): Wiktoria Drozdz, Daniel Joller, Philipp Grosse, and Thomas Fehr. Severe lupus nephritis in a young adult with pten hamartoma tumour syndrome. BMJ Case Reports, 17:e258400, Sep 2024. URL: https://doi.org/10.1136/bcr-2023-258400, doi:10.1136/bcr-2023-258400. This article has 2 citations and is from a peer-reviewed journal.

20. (takayama2023clinicalguidelinesfor pages 8-11): Tetsuji Takayama, Naoki Muguruma, Masahiro Igarashi, Shozo Ohsumi, Shiro Oka, Fumihiko Kakuta, Yoshiaki Kubo, Hideki Kumagai, Mika Sasaki, Tamotsu Sugai, Kokichi Sugano, Yuko Takeda, Hisashi Doyama, Kouji Banno, Suguru Fukahori, Yoichi Furukawa, Takahiro Horimatsu, Hideki Ishikawa, Takeo Iwama, Yasushi Okazaki, Yutaka Saito, Nariaki Matsuura, Michihiro Mutoh, Naohiro Tomita, Takashi Akiyama, Toshiki Yamamoto, Hideyuki Ishida, and Yoshiko Nakayama. Clinical guidelines for diagnosis and management of cowden syndrome/pten hamartoma tumor syndrome in children and adults―secondary publication. Journal of the Anus, Rectum and Colon, 7:284-300, Oct 2023. URL: https://doi.org/10.23922/jarc.2023-028, doi:10.23922/jarc.2023-028. This article has 43 citations.

21. (tischkowitz2020cancersurveillanceguideline pages 2-4): M. Tischkowitz, C. Colas, Sjaak Pouwels, N. Hoogerbrugge, Tanya Virginie Frederic Nathalie Chrystelle Sophie Marti Bisseling Bubien Caux Chabbert-Buffet Colas Da Mot, T. Bisseling, V. Bubien, F. Caux, N. Chabbert-Buffet, Sophie Da Mota Gomes, M. Gotthardt, M. Kets, K. Lachlan, T. Links, M. Longy, R. Mann, L. S. Kool, R. Semple, Ian Stock, M. Tischkowitz, J. Vos, Nicoline Marjolijn Rianne Rolf Gareth Emma Marc Eamonn Rosa Hoogerbrugge Ligtenberg Oostenbrink Sijmons Evans, M. Ligtenberg, R. Oostenbrink, R. Sijmons, G. Evans, E. Woodward, E. Maher, R. Ferner, S. Aretz, I. Spier, V. Steinke-Lange, E. Holinski-Feder, E. Schröck, T. Frebourg, C. Houdayer, P. Wolkenstein, V. Bours, E. Legius, B. Poppe, K. Claes, Robin de Putter, I. Guillermo, G. Capellá, J. B. Vidal, C. Lázaro, J. Balmaña, Héctor Salvador Hernández, Carla Oliveira, M. Teixeira, S. Bajalica-Lagercrantz, E. Tham, J. Lubiński, K. Ertmańska, B. Melegh, M. Krajc, A. Blatnik, S. Peltonen, and M. Hietala. Cancer surveillance guideline for individuals with pten hamartoma tumour syndrome. European Journal of Human Genetics, 28:1387-1393, Jun 2020. URL: https://doi.org/10.1038/s41431-020-0651-7, doi:10.1038/s41431-020-0651-7. This article has 146 citations and is from a domain leading peer-reviewed journal.

22. (tischkowitz2020cancersurveillanceguideline media 2ffc24d6): M. Tischkowitz, C. Colas, Sjaak Pouwels, N. Hoogerbrugge, Tanya Virginie Frederic Nathalie Chrystelle Sophie Marti Bisseling Bubien Caux Chabbert-Buffet Colas Da Mot, T. Bisseling, V. Bubien, F. Caux, N. Chabbert-Buffet, Sophie Da Mota Gomes, M. Gotthardt, M. Kets, K. Lachlan, T. Links, M. Longy, R. Mann, L. S. Kool, R. Semple, Ian Stock, M. Tischkowitz, J. Vos, Nicoline Marjolijn Rianne Rolf Gareth Emma Marc Eamonn Rosa Hoogerbrugge Ligtenberg Oostenbrink Sijmons Evans, M. Ligtenberg, R. Oostenbrink, R. Sijmons, G. Evans, E. Woodward, E. Maher, R. Ferner, S. Aretz, I. Spier, V. Steinke-Lange, E. Holinski-Feder, E. Schröck, T. Frebourg, C. Houdayer, P. Wolkenstein, V. Bours, E. Legius, B. Poppe, K. Claes, Robin de Putter, I. Guillermo, G. Capellá, J. B. Vidal, C. Lázaro, J. Balmaña, Héctor Salvador Hernández, Carla Oliveira, M. Teixeira, S. Bajalica-Lagercrantz, E. Tham, J. Lubiński, K. Ertmańska, B. Melegh, M. Krajc, A. Blatnik, S. Peltonen, and M. Hietala. Cancer surveillance guideline for individuals with pten hamartoma tumour syndrome. European Journal of Human Genetics, 28:1387-1393, Jun 2020. URL: https://doi.org/10.1038/s41431-020-0651-7, doi:10.1038/s41431-020-0651-7. This article has 146 citations and is from a domain leading peer-reviewed journal.

23. (takayama2023clinicalguidelinesfor pages 11-12): Tetsuji Takayama, Naoki Muguruma, Masahiro Igarashi, Shozo Ohsumi, Shiro Oka, Fumihiko Kakuta, Yoshiaki Kubo, Hideki Kumagai, Mika Sasaki, Tamotsu Sugai, Kokichi Sugano, Yuko Takeda, Hisashi Doyama, Kouji Banno, Suguru Fukahori, Yoichi Furukawa, Takahiro Horimatsu, Hideki Ishikawa, Takeo Iwama, Yasushi Okazaki, Yutaka Saito, Nariaki Matsuura, Michihiro Mutoh, Naohiro Tomita, Takashi Akiyama, Toshiki Yamamoto, Hideyuki Ishida, and Yoshiko Nakayama. Clinical guidelines for diagnosis and management of cowden syndrome/pten hamartoma tumor syndrome in children and adults―secondary publication. Journal of the Anus, Rectum and Colon, 7:284-300, Oct 2023. URL: https://doi.org/10.23922/jarc.2023-028, doi:10.23922/jarc.2023-028. This article has 43 citations.

24. (tischkowitz2020cancersurveillanceguideline pages 4-5): M. Tischkowitz, C. Colas, Sjaak Pouwels, N. Hoogerbrugge, Tanya Virginie Frederic Nathalie Chrystelle Sophie Marti Bisseling Bubien Caux Chabbert-Buffet Colas Da Mot, T. Bisseling, V. Bubien, F. Caux, N. Chabbert-Buffet, Sophie Da Mota Gomes, M. Gotthardt, M. Kets, K. Lachlan, T. Links, M. Longy, R. Mann, L. S. Kool, R. Semple, Ian Stock, M. Tischkowitz, J. Vos, Nicoline Marjolijn Rianne Rolf Gareth Emma Marc Eamonn Rosa Hoogerbrugge Ligtenberg Oostenbrink Sijmons Evans, M. Ligtenberg, R. Oostenbrink, R. Sijmons, G. Evans, E. Woodward, E. Maher, R. Ferner, S. Aretz, I. Spier, V. Steinke-Lange, E. Holinski-Feder, E. Schröck, T. Frebourg, C. Houdayer, P. Wolkenstein, V. Bours, E. Legius, B. Poppe, K. Claes, Robin de Putter, I. Guillermo, G. Capellá, J. B. Vidal, C. Lázaro, J. Balmaña, Héctor Salvador Hernández, Carla Oliveira, M. Teixeira, S. Bajalica-Lagercrantz, E. Tham, J. Lubiński, K. Ertmańska, B. Melegh, M. Krajc, A. Blatnik, S. Peltonen, and M. Hietala. Cancer surveillance guideline for individuals with pten hamartoma tumour syndrome. European Journal of Human Genetics, 28:1387-1393, Jun 2020. URL: https://doi.org/10.1038/s41431-020-0651-7, doi:10.1038/s41431-020-0651-7. This article has 146 citations and is from a domain leading peer-reviewed journal.

25. (pirlog2024insightsintoclinical pages 11-12): Lorin-Manuel Pîrlog, Andrada-Adelaida Pătrășcanu, Mariela Sanda Militaru, and Andreea Cătană. Insights into clinical disorders in cowden syndrome: a comprehensive review. Medicina, 60:767, May 2024. URL: https://doi.org/10.3390/medicina60050767, doi:10.3390/medicina60050767. This article has 10 citations.

26. (tischkowitz2020cancersurveillanceguideline pages 1-2): M. Tischkowitz, C. Colas, Sjaak Pouwels, N. Hoogerbrugge, Tanya Virginie Frederic Nathalie Chrystelle Sophie Marti Bisseling Bubien Caux Chabbert-Buffet Colas Da Mot, T. Bisseling, V. Bubien, F. Caux, N. Chabbert-Buffet, Sophie Da Mota Gomes, M. Gotthardt, M. Kets, K. Lachlan, T. Links, M. Longy, R. Mann, L. S. Kool, R. Semple, Ian Stock, M. Tischkowitz, J. Vos, Nicoline Marjolijn Rianne Rolf Gareth Emma Marc Eamonn Rosa Hoogerbrugge Ligtenberg Oostenbrink Sijmons Evans, M. Ligtenberg, R. Oostenbrink, R. Sijmons, G. Evans, E. Woodward, E. Maher, R. Ferner, S. Aretz, I. Spier, V. Steinke-Lange, E. Holinski-Feder, E. Schröck, T. Frebourg, C. Houdayer, P. Wolkenstein, V. Bours, E. Legius, B. Poppe, K. Claes, Robin de Putter, I. Guillermo, G. Capellá, J. B. Vidal, C. Lázaro, J. Balmaña, Héctor Salvador Hernández, Carla Oliveira, M. Teixeira, S. Bajalica-Lagercrantz, E. Tham, J. Lubiński, K. Ertmańska, B. Melegh, M. Krajc, A. Blatnik, S. Peltonen, and M. Hietala. Cancer surveillance guideline for individuals with pten hamartoma tumour syndrome. European Journal of Human Genetics, 28:1387-1393, Jun 2020. URL: https://doi.org/10.1038/s41431-020-0651-7, doi:10.1038/s41431-020-0651-7. This article has 146 citations and is from a domain leading peer-reviewed journal.

27. (pirlog2024insightsintoclinical pages 2-4): Lorin-Manuel Pîrlog, Andrada-Adelaida Pătrășcanu, Mariela Sanda Militaru, and Andreea Cătană. Insights into clinical disorders in cowden syndrome: a comprehensive review. Medicina, 60:767, May 2024. URL: https://doi.org/10.3390/medicina60050767, doi:10.3390/medicina60050767. This article has 10 citations.