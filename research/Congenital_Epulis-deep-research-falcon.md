---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T09:26:05.123220'
end_time: '2026-05-09T09:42:29.276288'
duration_seconds: 984.15
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Congenital Epulis
  mondo_id: ''
  category: Congenital Oral Soft Tissue Neoplasm
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Epulis
- **MONDO ID:**  (if available)
- **Category:** Congenital Oral Soft Tissue Neoplasm

## Research Objectives

Please provide a comprehensive research report on **Congenital Epulis** covering all of the
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
- **Disease Name:** Congenital Epulis
- **MONDO ID:**  (if available)
- **Category:** Congenital Oral Soft Tissue Neoplasm

## Research Objectives

Please provide a comprehensive research report on **Congenital Epulis** covering all of the
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


# Congenital Epulis (Congenital Granular Cell Epulis; Neumann Tumor): Disease Characteristics Research Report

**Target disease:** Congenital epulis (also called congenital granular cell epulis, congenital gingival granular cell tumor, Neumann tumor) — a rare, benign, neonatal oral soft-tissue tumor-like lesion arising on the gingiva/alveolar ridge, typically present at birth and sometimes detectable prenatally. (han2024fromprenataldiagnosis pages 1-3, mcguire2006pratiqueclinique pages 1-3)

## Executive summary (current understanding)
Congenital epulis/congenital granular cell epulis (CGCE) is a benign lesion exclusive to the newborn period, most often on the anterior maxillary alveolar ridge, with a marked female predominance. Etiology/histogenesis remains uncertain; hypotheses span pericytic/fibroblastic/histiocytic/nerve-related or undifferentiated mesenchymal origins, and many authors discuss potential intrauterine hormonal influence (estrogen exposure) to explain both sex bias and postnatal growth arrest/spontaneous regression. Diagnosis is clinicopathologic, supported by characteristic granular-cell histology and a typical immunophenotype (often vimentin-positive, S-100 negative), though recent cases document immunohistochemical variability (e.g., weak S-100/CD68 positivity) and Ki-67 around 15% in at least one case. Primary management is local surgical excision when feeding/airway function is threatened; prognosis is excellent with negligible recurrence and no malignant transformation reported in the retrieved sources. (qin2024aclinicalobservation pages 1-2, han2024fromprenataldiagnosis pages 1-3, mcguire2006pratiqueclinique pages 1-3)

## 1. Disease information
### 1.1 Definition / overview
- **Definition:** A rare benign lesion of the neonatal gingiva/alveolar ridge, presenting as a sessile or pedunculated oral mass at birth, potentially causing feeding difficulty and (less commonly) airway compromise. (chaudhry2024congenitalepulisreport pages 1-2, mcguire2006pratiqueclinique pages 1-3)
- **Exclusivity to neonatal period:** Described as occurring “exclusively” in newborns in recent reports. (han2024fromprenataldiagnosis pages 1-3)

### 1.2 Key identifiers (controlled vocabularies)
- **MeSH (explicit in retrieved literature):** *gingival neoplasms/complications; gingival neoplasms/congenital; granular cell tumor/congenital; infant, newborn*. (mcguire2006pratiqueclinique pages 1-3)
- **WHO terminology:** A 2024 case report states that **“congenital granular cell epulis”** is the term used by WHO. (oriaifo2024congenitalepulisin pages 1-3)
- **ICD-10/ICD-11 / SNOMED CT / MONDO / Orphanet / OMIM:** No explicit codes/IDs were found in the retrieved sources used for this report (therefore **not assigned here**). (mcguire2006congenitalepulisa pages 3-4, braz2022épuliscongénito pages 1-3)

### 1.3 Synonyms / alternative names
Common synonyms include:
- congenital granular cell epulis (CGCE)
- congenital epulis
- congenital gingival granular cell tumor
- congenital granular cell myoblastoma
- Neumann (Newmann) tumor

These are explicitly used in 2024 case literature. (qin2024aclinicalobservation pages 1-2, chaudhry2024congenitalepulisreport pages 1-2, han2024fromprenataldiagnosis pages 1-3)

### 1.4 Evidence source type
The evidence base is dominated by **case reports/series** and small retrospective pathology datasets; high-quality population registries and mechanistic molecular studies are limited in the retrieved set. (shuhairi2021aretrospectiveanalysis pages 1-2, han2024fromprenataldiagnosis pages 1-3)

## 2. Etiology
### 2.1 Disease causal factors
- **Etiology remains unknown/controversial.** Multiple origin hypotheses are enumerated in 2024 work: *pericyte, fibroblast, histiocyte, nerve-related,* and *undifferentiated mesenchymal cells*. (han2024fromprenataldiagnosis pages 1-3)
- An older peer-reviewed dental report describes histogenesis as uncertain and suggests a “non-neoplastic, degenerative or reactive lesion.” (mcguire2006congenitalepulisa pages 3-4)

### 2.2 Risk factors
- **Sex (female):** Strong female predominance is repeatedly reported (see epidemiology). (han2024fromprenataldiagnosis pages 1-3, braz2022épuliscongénito pages 1-3, mcguire2006pratiqueclinique pages 1-3)
- **In utero hormonal exposure hypothesis:** A 2024 prenatal/postnatal management report states that the “prevailing theory” attributes pathogenesis to **intrauterine exposure to estrogen** and proposes that postpartum hormonal decline may halt growth, with rare spontaneous regression. (qin2024aclinicalobservation pages 1-2)

### 2.3 Protective factors
No genetic or environmental protective factors were identified in the retrieved literature.

### 2.4 Gene–environment interactions
No gene–environment interaction evidence was identified in the retrieved literature.

## 3. Phenotypes
### 3.1 Core phenotype spectrum
- **Oral mass at birth**: typically a smooth, pink/reddish, sessile or pedunculated gingival mass. (chaudhry2024congenitalepulisreport pages 1-2, mcguire2006pratiqueclinique pages 1-3)
- **Location:** usually anterior maxillary alveolar ridge; mandible less common; other sites (e.g., tongue) reported. (chaudhry2024congenitalepulisreport pages 1-2, oriaifo2024congenitalepulisin pages 1-3)
- **Feeding/suckling difficulty:** frequently described when lesions are large or protrude from the mouth, sometimes requiring nasogastric feeding. (oriaifo2024congenitalepulisin pages 1-3, braz2022épuliscongénito pages 1-3, mcguire2006pratiqueclinique pages 1-3)
- **Airway compromise (potential):** large lesions can occupy the oral cavity and pose obstruction risk; many infants are stable but careful airway planning is emphasized. (mcguire2006pratiqueclinique pages 1-3, qin2024aclinicalobservation pages 2-3)

### 3.2 Phenotype timing/severity/progression
- **Onset:** congenital/neonatal; prenatal detection possible in the second/third trimester.
  - Prenatal detection **as early as ~25 weeks** is described in a 2022 case report. (braz2022épuliscongénito pages 1-3)
  - A 2024 case report series detected masses at ~34 weeks gestation by ultrasound. (han2024fromprenataldiagnosis pages 1-3)
- **Progression:** several reports describe rapid growth in late pregnancy and minimal/no growth after birth, with occasional spontaneous regression. (chaudhry2024congenitalepulisreport pages 1-2, mcguire2006pratiqueclinique pages 1-3)

### 3.3 Frequency among affected individuals (when available)
- **Multiple lesions:** approximately **~10%** (or 5–16% in one report) are multifocal in the oral cavity. (qin2024aclinicalobservation pages 1-2, han2024fromprenataldiagnosis pages 1-3)

### 3.4 Quality-of-life / functional impact
Primary impact is **feeding/breastfeeding impairment** in the newborn period and potential airway management complexity. Postoperative functional recovery (return to oral feeding/breastfeeding) is typically rapid in reported cases. (qin2024aclinicalobservation pages 1-2, braz2022épuliscongénito pages 1-3, mcguire2006pratiqueclinique pages 1-3)

### 3.5 Suggested HPO terms (non-exhaustive)
- **Congenital onset** (HP:0003577) (general)
- **Feeding difficulties** (HP:0011968)
- **Poor suck** (HP:0002033)
- **Respiratory distress** (HP:0002098) (if airway compromise)
- **Oral cavity mass / Gingival mass** (suggested; verify exact HPO IDs during curation)

## 4. Genetic / molecular information
### 4.1 Causal genes
No causal gene has been identified or reported in the retrieved evidence.

### 4.2 Pathogenic variants
No germline or somatic pathogenic variants were reported.

### 4.3 Genetic testing evidence in retrieved literature
- A 2024 prenatal management report states **noninvasive prenatal genetic testing was low-risk for trisomies 21/18/13** in an affected pregnancy. This does not imply a genetic cause; it reflects normal aneuploidy screening in that case. (qin2024aclinicalobservation pages 1-2)

### 4.4 Immunophenotype / molecular markers (diagnostic)
- Typical immunophenotype in several recent cases: **vimentin positive**, **S-100 negative**, with **NSE and CD68 negative** in at least one 2024 report. (han2024fromprenataldiagnosis pages 1-3)
- Variability exists: a 2024 report documents **weak S-100 and CD68 positivity**, vimentin positivity, **SOX-10 negative**, **NSE negative**, and **Ki-67 ~15% positive**. (qin2024aclinicalobservation pages 1-2)

**Interpretation:** recent work cautions that S-100 alone may be insufficient to distinguish CGCE from adult granular cell tumor because some CGCE cases may show S-100 positivity. (qin2024aclinicalobservation pages 2-3, qin2024aclinicalobservation pages 1-2)

## 5. Environmental information
No consistent environmental triggers, toxins, infections, or lifestyle associations were identified in the retrieved literature. A 2024 case report explicitly notes absence of familial tendency or teratogen association in its discussion. (haghegh2024congenitalepulisa pages 4-6)

## 6. Mechanism / pathophysiology
### 6.1 Current mechanistic hypotheses
- **Histogenesis is unclear/controversial** with multiple proposed cellular origins (pericyte, fibroblast, histiocyte, nerve-related, undifferentiated mesenchymal). (han2024fromprenataldiagnosis pages 1-3)
- **Hormonal influence model:** intrauterine estrogen exposure is discussed as a prevailing hypothesis; postpartum hormonal decline may halt growth and could explain rare regression. (qin2024aclinicalobservation pages 1-2)

### 6.2 Causal chain (working model; evidence-limited)
1. **In utero trigger** (hypothesized hormonal milieu and/or mesenchymal developmental program) →
2. **Localized proliferation/differentiation of granular cells** in gingival/alveolar mucosa →
3. **Exophytic gingival mass** (pedunculated/sessile) →
4. **Mechanical functional effects** (feeding difficulty, possible airway compromise) in the newborn. (qin2024aclinicalobservation pages 1-2, chaudhry2024congenitalepulisreport pages 1-2, mcguire2006pratiqueclinique pages 1-3)

### 6.3 Suggested GO / CL terms (for curation; evidence-limited)
- **GO (process):** cell proliferation (GO:0008283) (supported indirectly by Ki-67 reporting in at least one case) (qin2024aclinicalobservation pages 1-2)
- **CL (cell type):** undifferentiated mesenchymal cell (candidate; based on hypothesized origins, not proven) (han2024fromprenataldiagnosis pages 1-3)

## 7. Anatomical structures affected
### 7.1 Primary anatomical sites
- **Gingiva / alveolar ridge** (especially anterior **maxillary alveolar ridge**). (han2024fromprenataldiagnosis pages 1-3, mcguire2006pratiqueclinique pages 1-3)

### 7.2 Suggested UBERON terms (examples; verify IDs during curation)
- Gingiva
- Maxillary alveolar ridge
- Mandibular alveolar ridge
- Oral cavity
- Hard palate / upper lip (relevant to lesion proximity on imaging in some cases) (qin2024aclinicalobservation pages 1-2)

## 8. Temporal development
- **Onset:** congenital; often detected at birth; prenatal detection in late pregnancy increasingly reported in 2024 literature. (han2024fromprenataldiagnosis pages 1-3, qin2024aclinicalobservation pages 1-2)
- **Course:** typically does not grow after birth; occasional spontaneous regression is reported; otherwise stable until excision. (chaudhry2024congenitalepulisreport pages 1-2, mcguire2006pratiqueclinique pages 1-3)

## 9. Inheritance and population
### 9.1 Epidemiology (statistics)
Estimates vary across reports:
- **Incidence:** approximately **0.0006%** cited in 2024 literature. (han2024fromprenataldiagnosis pages 1-3, haghegh2024congenitalepulisa pages 1-4)
- Alternative incidence estimate: **~1 per 6,000,000** in a 2022 neonatal report. (braz2022épuliscongénito pages 1-3)
- Another literature-derived estimate: **6–9 cases per million births** in a review-style summary. (vera2026épuliscongénitocaso pages 1-4)

**Sex ratio:** strong female predominance, commonly **8–10:1** or **10:1** female:male. (han2024fromprenataldiagnosis pages 1-3, mcguire2006pratiqueclinique pages 1-3)

**Site distribution:** maxilla predominates over mandible, often cited as ~3× more common in the maxilla (or ratios 2:1–3:1 across reports). (qin2024aclinicalobservation pages 1-2, mcguire2006pratiqueclinique pages 1-3)

**Pathology service-based frequency (not population incidence):** In a 51-year Malaysian oral pathology series (≤2 years old), congenital epulis comprised **11/27 (40.7%)** of *newborn* oral/maxillofacial biopsy diagnoses, showing it is a major neonatal indication for biopsy among rare lesions in that dataset. (shuhairi2021aretrospectiveanalysis pages 4-5)

### 9.2 Inheritance pattern
- Reported as **sporadic** with “no familial tendency” in at least one discussion; family histories without hereditary diseases are described in multiple cases. (haghegh2024congenitalepulisa pages 4-6, qin2024aclinicalobservation pages 1-2, han2024fromprenataldiagnosis pages 1-3)

## 10. Diagnostics
### 10.1 Clinical diagnosis
Clinical suspicion arises from the classic newborn gingival mass, often pedunculated and well circumscribed; diagnosis is typically confirmed histologically. (braz2022épuliscongénito pages 1-3, mcguire2006pratiqueclinique pages 1-3)

### 10.2 Imaging
**Prenatal imaging (2023–2024 emphasis):**
- Prenatal ultrasound can show a mass protruding from the fetal mouth in the third trimester; multidisciplinary planning is used to manage delivery/anesthesia risks. (han2024fromprenataldiagnosis pages 1-3, han2024fromprenataldiagnosis pages 3-4)
- Prenatal MRI complements ultrasound by defining relationships to palate/gingiva and tissue characteristics; one 2024 report details T1/T2 and diffusion-weighted findings and discusses the role of Doppler flow in differential diagnosis. (qin2024aclinicalobservation pages 1-2, qin2024aclinicalobservation pages 2-3)

**Visual evidence (prenatal imaging/IHC panels):** Han et al. include prenatal sonography and immunohistochemistry panels (vimentin staining, S-100 negativity) in figures/tables. (han2024fromprenataldiagnosis media e73f6ade)

### 10.3 Histopathology
Typical histology: sheets/nests/ribbons of granular cells with abundant eosinophilic granular cytoplasm, prominent capillaries/vascular stroma, and thin overlying squamous epithelium without pseudoepitheliomatous hyperplasia. (qin2024aclinicalobservation pages 2-3, mcguire2006pratiqueclinique pages 1-3, chaudhry2024congenitalepulisreport pages 1-2)

### 10.4 Immunohistochemistry
- Typical: **vimentin+**, **S-100−**; **NSE/CD68** may be negative. (han2024fromprenataldiagnosis pages 1-3)
- Documented variation: weak **S-100/CD68** positivity and Ki-67 ~15% (one 2024 case). (qin2024aclinicalobservation pages 1-2)

### 10.5 Differential diagnosis
Differentials include fetal/neonatal oral teratoma/epignathus, hemangioma/vascular malformation, melanotic neuroectodermal tumor of infancy, rhabdomyosarcoma, dermoid cyst, fibroma, and granular cell tumor. (qin2024aclinicalobservation pages 2-3, oriaifo2024congenitalepulisin pages 1-3, mcguire2006pratiqueclinique pages 1-3)

## 11. Outcome / prognosis
- **Excellent prognosis** after complete excision; recurrence is described as negligible/rare and malignant transformation not reported in the retrieved sources. (han2024fromprenataldiagnosis pages 1-3, mcguire2006pratiqueclinique pages 1-3, mcguire2006congenitalepulisa pages 3-4)
- **Recent follow-up examples:**
  - No recurrence at **6 months** after excision of a large lesion in 2024 (Qin et al.). (qin2024aclinicalobservation pages 1-2)
  - No recurrence at **1 year** in two 2024 cases (Chaudhry et al.). (chaudhry2024congenitalepulisreport pages 1-2)

## 12. Treatment
### 12.1 Standard of care: surgery
- **Local surgical excision** is the primary treatment when feeding/airway function is compromised; recent cases use general anesthesia with tracheal intubation and electrocautery/ligation for hemostasis. (qin2024aclinicalobservation pages 1-2, han2024fromprenataldiagnosis pages 3-4, mcguire2006pratiqueclinique pages 1-3)
- Wide excision is generally unnecessary because recurrence after incomplete excision is described as not reported in one review-oriented source. (mcguire2006congenitalepulisa pages 3-4)

### 12.2 Supportive management
- Nasogastric feeding/IV fluids may be used temporarily if oral feeding is impaired until definitive management. (oriaifo2024congenitalepulisin pages 1-3, mcguire2006pratiqueclinique pages 1-3)

### 12.3 Observation/spontaneous regression
- Spontaneous regression is described as **rare**, but reported in the literature and discussed in both older and recent sources. (mcguire2006pratiqueclinique pages 1-3, chaudhry2024congenitalepulisreport pages 1-2)

### 12.4 Clinical trials
A clinical trials registry search in the current tool environment did **not identify relevant interventional trials** for congenital epulis/CGCE. (shuhairi2021aretrospectiveanalysis pages 1-2)

### 12.5 Suggested MAXO terms (examples; verify IDs during curation)
- Surgical excision (oral lesion)
- Airway management / endotracheal intubation (perioperative)
- Enteral feeding via nasogastric tube
- Prenatal multidisciplinary care planning

## 13. Prevention
- **Primary prevention:** none established (unknown etiology; non-genetic sporadic pattern). (mcguire2006congenitalepulisa pages 3-4, haghegh2024congenitalepulisa pages 4-6)
- **Secondary prevention / risk mitigation:** prenatal detection (ultrasound ± MRI) enables delivery planning and early postnatal management to prevent feeding/airway complications. (qin2024aclinicalobservation pages 1-2, han2024fromprenataldiagnosis pages 1-3)

## 14. Other species / natural disease
No naturally occurring non-human cases or veterinary relevance were identified in the retrieved evidence.

## 15. Model organisms
No established animal or experimental model organism systems were identified in the retrieved evidence.

---

## Key evidence tables (for knowledge-base population)

| Identifier system | Term/code (if present) | Notes | Key supporting citation IDs |
|---|---|---|---|
| MeSH | `gingival neoplasms/complications`; `gingival neoplasms/congenital`; `granular cell tumor/congenital`; `infant, newborn` | Explicit MeSH indexing reported in a peer-reviewed dental article on congenital epulis. | (mcguire2006pratiqueclinique pages 1-3, mcguire2006congenitalepulisa pages 1-3) |
| WHO naming | `congenital granular cell epulis` | A 2024 case report states this is the term used by WHO; literature also uses `congenital epulis`. | (oriaifo2024congenitalepulisin pages 1-3) |
| ICD-10 / ICD-11 | No specific code identified in retrieved sources | Available texts did not provide an explicit ICD-10 or ICD-11 code for congenital epulis; coding remains unresolved in this evidence set. | (mcguire2006congenitalepulisa pages 3-4, qin2024aclinicalobservation pages 1-2, braz2022épuliscongénito pages 1-3, lacerda2025congenitalepulidisa pages 10-10) |
| Synonym / terminology | `congenital epulis` | Most commonly used umbrella term in clinical literature; refers to a rare benign neonatal gingival/alveolar lesion. | (mcguire2006congenitalepulisa pages 3-4, qin2024aclinicalobservation pages 1-2, chaudhry2024congenitalepulisreport pages 1-2, han2024fromprenataldiagnosis pages 1-3) |
| Synonym / terminology | `congenital granular cell epulis (CGCE)` | Common recent preferred term, especially in 2024 prenatal-management and pathology reports. | (qin2024aclinicalobservation pages 1-2, han2024fromprenataldiagnosis pages 1-3) |
| Synonym / terminology | `Neumann tumor` / `Newmann’s tumor` | Historical eponym tracing to the first description in 1871. | (mcguire2006congenitalepulisa pages 3-4, chaudhry2024congenitalepulisreport pages 1-2, han2024fromprenataldiagnosis pages 1-3, braz2022épuliscongénito pages 1-3) |
| Synonym / terminology | `congenital gingival granular cell tumor` | Frequently used pathology/clinical synonym emphasizing gingival origin. | (chaudhry2024congenitalepulisreport pages 1-2, oriaifo2024congenitalepulisin pages 1-3) |
| Synonym / terminology | `congenital granular cell myoblastoma` | Older synonym still encountered in case reports and reviews. | (mcguire2006congenitalepulisa pages 3-4, chaudhry2024congenitalepulisreport pages 1-2) |
| Incidence estimate | `0.0006%` | Reported in 2024/2025 case literature and review-style discussion. | (haghegh2024congenitalepulisa pages 1-4, han2024fromprenataldiagnosis pages 1-3) |
| Incidence estimate | `~1/6,000,000` | Alternative estimate reported in a 2022 Spanish-language neonatal case report. | (braz2022épuliscongénito pages 1-3) |
| Incidence estimate | `6–9 cases per million births` | Reported in review-style summary evidence; should be treated as literature-derived estimate rather than registry-based incidence. | (vera2026épuliscongénitocaso pages 1-4) |
| Sex ratio | Female predominance `8–10:1` | Strong and consistent female excess across modern and older case literature. | (chaudhry2024congenitalepulisreport pages 1-2, han2024fromprenataldiagnosis pages 1-3, oriaifo2024congenitalepulisin pages 1-3, braz2022épuliscongénito pages 1-3) |
| Sex ratio | Female predominance `10:1` | Commonly cited estimate in reviews/case discussions. | (haghegh2024congenitalepulisa pages 1-4, mcguire2006congenitalepulisa pages 1-3, mcguire2006pratiqueclinique pages 1-3) |
| Site distribution | Maxilla:mandible `2:1` | One recent prenatal/postnatal management report gives an approximate 2:1 maxillary predominance. | (qin2024aclinicalobservation pages 1-2) |
| Site distribution | Maxilla:mandible `2–3:1` | 2022 case report describes upper-jaw predominance in a 2–3:1 ratio. | (braz2022épuliscongénito pages 1-3) |
| Site distribution | Maxilla:mandible `3:1` / maxilla `3×` mandible | Frequently cited distribution in 2006 and 2024 literature; lesion usually arises on anterior maxillary alveolar ridge. | (haghegh2024congenitalepulisa pages 4-6, haghegh2024congenitalepulisa pages 1-4, mcguire2006congenitalepulisa pages 1-3, han2024fromprenataldiagnosis pages 1-3, mcguire2006pratiqueclinique pages 1-3) |
| Multiplicity | Multiple lesions in `~5%–16%` or `~10%` of cases | Most cases are solitary; multifocal lesions are uncommon but well documented. | (qin2024aclinicalobservation pages 1-2, chaudhry2024congenitalepulisreport pages 1-2, han2024fromprenataldiagnosis pages 1-3) |


*Table: This table summarizes the main identifiers, synonyms, and core epidemiologic estimates for congenital epulis from the retrieved evidence. It is useful for harmonizing disease terminology and for quickly comparing commonly cited incidence, sex-ratio, and site-distribution figures.*

| Domain | Finding | Typical timing/onset | Quantitative stats (if available) | Ontology term suggestions (HPO/GO/CL/UBERON/MAXO as appropriate) | Key citations |
|---|---|---|---|---|---|
| Phenotype | Benign congenital oral/alveolar soft-tissue mass; usually smooth, pink/red, sessile or pedunculated, often lobulated | Congenital; present at birth or detected in late 3rd trimester prenatally | Size ranges from millimeters to ~9 cm in literature; examples 3×2×2 cm, 3×4×3 cm, 5.0×4.5×3.0 cm | HPO: Congenital onset (HP:0003577), Gingival mass/oral cavity mass (suggested); UBERON: gingiva, maxillary alveolar ridge, mandibular alveolar ridge | (qin2024aclinicalobservation pages 1-2, chaudhry2024congenitalepulisreport pages 1-2, han2024fromprenataldiagnosis pages 1-3, oriaifo2024congenitalepulisin pages 1-3, braz2022épuliscongénito pages 1-3, mcguire2006pratiqueclinique pages 1-3) |
| Phenotype | Predominant location is anterior maxillary alveolar ridge; mandibular gingiva less common; tongue rare | Present at birth; prenatal detection possible from ~25–26 weeks | Maxilla more common than mandible by ~2:1, 2–3:1, or 3:1 across reports | UBERON: maxillary alveolar ridge, mandibular alveolar ridge, gingiva, tongue | (qin2024aclinicalobservation pages 1-2, han2024fromprenataldiagnosis pages 1-3, oriaifo2024congenitalepulisin pages 1-3, braz2022épuliscongénito pages 1-3, mcguire2006pratiqueclinique pages 1-3) |
| Phenotype | Strong female predominance | Congenital/neonatal | Female:male ratio ~8–10:1 or 10:1 | HPO: Female-limited/sex-biased occurrence (suggested epidemiologic annotation) | (chaudhry2024congenitalepulisreport pages 1-2, han2024fromprenataldiagnosis pages 1-3, oriaifo2024congenitalepulisin pages 1-3, braz2022épuliscongénito pages 1-3, mcguire2006pratiqueclinique pages 1-3) |
| Phenotype | Usually solitary lesion, but multifocal disease occurs | Congenital/neonatal | Multiple lesions reported in ~5–16% or ~10% of cases | HPO: Multiple oral masses (suggested) | (qin2024aclinicalobservation pages 1-2, chaudhry2024congenitalepulisreport pages 1-2, han2024fromprenataldiagnosis pages 1-3) |
| Phenotype | Feeding/suckling impairment due to oral mass | Immediate neonatal period | Common functional consequence in large lesions; case reports required NG feeds/support | HPO: Feeding difficulties (HP:0011968), Poor suck (HP:0002033) | (chaudhry2024congenitalepulisreport pages 1-2, han2024fromprenataldiagnosis pages 3-4, oriaifo2024congenitalepulisin pages 1-3, braz2022épuliscongénito pages 1-3, mcguire2006pratiqueclinique pages 1-3) |
| Phenotype | Respiratory compromise/airway obstruction can occur with large tumors, though many neonates remain stable | Immediate neonatal period | Qualitative risk; no pooled percentage in retrieved evidence | HPO: Respiratory distress (HP:0002098), Airway obstruction (suggested) | (qin2024aclinicalobservation pages 2-3, chaudhry2024congenitalepulisreport pages 1-2, oriaifo2024congenitalepulisin pages 1-3, mcguire2006pratiqueclinique pages 1-3) |
| Phenotype | Growth pattern: prenatal enlargement in 3rd trimester; usually stops growing after birth; rare spontaneous regression reported | Late pregnancy to neonatal period | Prenatal diagnosis as early as 25–26 weeks; spontaneous regression uncommon but documented | HPO: Congenital onset (HP:0003577) | (qin2024aclinicalobservation pages 1-2, chaudhry2024congenitalepulisreport pages 1-2, han2024fromprenataldiagnosis pages 1-3, braz2022épuliscongénito pages 1-3, mcguire2006pratiqueclinique pages 1-3) |
| Phenotype | Newborn oral pathology series shows congenital epulis is an important neonatal biopsy diagnosis | Newborn period | In a 51-year Malaysian series, congenital epulis accounted for 11/27 (40.7%) of newborn oral/maxillofacial biopsy diagnoses; 13 total cases (4.5% of all specimens ≤2 years) | Disease annotation / epidemiology field | (shuhairi2021aretrospectiveanalysis pages 1-2, shuhairi2021aretrospectiveanalysis pages 4-5) |
| Diagnosis | Prenatal ultrasound can identify protruding oral mass; MRI helps define relation to palate/gingiva and plan delivery/airway management | 25–39 weeks gestation | Prenatal detection reported from ~25–26 weeks; cases detected at 34–34.5 and 39 weeks | UBERON: oral cavity, palate, upper lip; Diagnostic imaging annotation | (qin2024aclinicalobservation pages 2-3, qin2024aclinicalobservation pages 1-2, han2024fromprenataldiagnosis pages 3-4, han2024fromprenataldiagnosis pages 1-3, braz2022épuliscongénito pages 1-3) |
| Diagnosis | Gross pathology: well-circumscribed/polypoid lesion with smooth mucosal covering; yellow-white to gray-yellow cut surface possible | At birth / post-excision | Qualitative | UBERON: gingiva, oral mucosa | (qin2024aclinicalobservation pages 2-3, chaudhry2024congenitalepulisreport pages 1-2, han2024fromprenataldiagnosis pages 3-4, oriaifo2024congenitalepulisin pages 1-3, mcguire2006pratiqueclinique pages 1-3) |
| Diagnosis | Histology: sheets/nests/ribbons of large polygonal granular cells with abundant eosinophilic granular cytoplasm and small central/eccentric nuclei; rich vascular stroma; thin squamous epithelium without pseudoepitheliomatous hyperplasia | Postnatal biopsy/excision specimen | No mitoses typically reported; PAS positivity reported in one case | GO: cytoplasmic granule; CL: mesenchymal cell (suggested); Tissue: stratified squamous epithelium, stromal capillaries | (qin2024aclinicalobservation pages 2-3, qin2024aclinicalobservation pages 1-2, chaudhry2024congenitalepulisreport pages 1-2, oriaifo2024congenitalepulisin pages 1-3, braz2022épuliscongénito pages 1-3, mcguire2006pratiqueclinique pages 1-3, mcguire2006congenitalepulisa pages 3-4) |
| Diagnosis | Immunohistochemistry typically supports mesenchymal/non-neural profile | Postnatal tissue diagnosis | Common pattern: vimentin+, S-100−; Han 2024 also NSE− and CD68− | GO: vimentin intermediate filament organization (suggested); CL: undifferentiated mesenchymal cell (suggested) | (han2024fromprenataldiagnosis pages 1-3, han2024fromprenataldiagnosis media e73f6ade) |
| Diagnosis | IHC variability exists; weak S-100 and CD68 positivity can occur | Postnatal tissue diagnosis | Qin 2024: S100(+), CD68(+), vimentin(+), CR(+), SOX10−, NSE−, HMB45−, CK−, CEA−, SMA−, desmin−, Ki-67 ~15%+ | GO: cell proliferation (GO:0008283) for Ki-67 context | (qin2024aclinicalobservation pages 1-2, qin2024aclinicalobservation pages 2-3) |
| Diagnosis | Differential diagnosis includes teratoma/epignathus, hemangioma, lymphangioma, melanotic neuroectodermal tumor of infancy, rhabdomyosarcoma, dermoid cyst, fibroma, granular cell tumor | Prenatal and neonatal diagnostic workup | Qualitative | HPO/diagnostic differential field; UBERON: oral cavity, maxilla | (qin2024aclinicalobservation pages 2-3, oriaifo2024congenitalepulisin pages 1-3, mcguire2006pratiqueclinique pages 1-3) |
| Diagnosis | Genetic findings are not established; no causal gene identified in retrieved evidence | N/A | Prenatal NIPT low-risk for trisomies 21/18/13 in one 2024 case; no familial pattern in reported cases | No established causal gene/variant annotation | (qin2024aclinicalobservation pages 1-2, han2024fromprenataldiagnosis pages 1-3) |
| Treatment | Primary treatment is complete local surgical excision, typically under general anesthesia; electrocautery or pedicle ligation may be used | Neonatal period, often within first days of life when feeding/airway affected | Surgery at day 1–3 in several cases; minimal bleeding reported | MAXO: Surgical excision of oral lesion (suggested), Airway management (suggested), Enteral feeding support (suggested) | (qin2024aclinicalobservation pages 1-2, chaudhry2024congenitalepulisreport pages 1-2, han2024fromprenataldiagnosis pages 3-4, oriaifo2024congenitalepulisin pages 1-3, braz2022épuliscongénito pages 1-3, mcguire2006pratiqueclinique pages 1-3) |
| Treatment | Multidisciplinary prenatal/postnatal management is increasingly reported for prenatally diagnosed cases | Late pregnancy through neonatal care | Teams included obstetrics, pediatricians, anesthesiology, oral/maxillofacial surgery; cesarean selected in some large lesions | MAXO: Multidisciplinary care planning (suggested), Cesarean delivery when indicated (suggested) | (qin2024aclinicalobservation pages 2-3, qin2024aclinicalobservation pages 1-2, han2024fromprenataldiagnosis pages 3-4, han2024fromprenataldiagnosis pages 1-3) |
| Treatment | Supportive care may include nasogastric feeding, IV fluids, and oral wound care before/after surgery | Immediate neonatal period | Qualitative | MAXO: Nasogastric tube feeding, Intravenous fluid administration, Postoperative wound care (suggested) | (chaudhry2024congenitalepulisreport pages 1-2, oriaifo2024congenitalepulisin pages 1-3, braz2022épuliscongénito pages 1-3, mcguire2006pratiqueclinique pages 1-3) |
| Prognosis | Prognosis is excellent; lesion is benign with no malignant transformation reported in retrieved sources | Short- and long-term after excision | Qualitative; literature consistently describes negligible recurrence/malignant transformation | Prognosis field | (han2024fromprenataldiagnosis pages 1-3, oriaifo2024congenitalepulisin pages 1-3, mcguire2006pratiqueclinique pages 1-3, mcguire2006congenitalepulisa pages 3-4) |
| Prognosis | Recurrence after excision is very uncommon/not reported in cited case literature | Follow-up months to 1 year and literature summaries | No recurrence at 6 months (Qin 2024); no recurrence at 1 year in both Chaudhry 2024 cases; no recurrence reported in review-style summaries | Outcome annotation | (qin2024aclinicalobservation pages 1-2, chaudhry2024congenitalepulisreport pages 1-2) |
| Prognosis | Functional recovery after treatment is usually rapid, with restoration of feeding/breastfeeding | Hours to days after surgery | Postoperative feeding resumed within hours to 2 days in case reports | HPO improvement: Feeding difficulties resolved (suggested) | (qin2024aclinicalobservation pages 1-2, han2024fromprenataldiagnosis pages 3-4, oriaifo2024congenitalepulisin pages 1-3, braz2022épuliscongénito pages 1-3, mcguire2006pratiqueclinique pages 1-3) |


*Table: This table consolidates the main phenotype, diagnostic, treatment, and prognosis findings for congenital epulis/congenital granular cell epulis from the retrieved case reports and retrospective study. It is useful for rapid disease knowledge base curation, including ontology suggestions and directly traceable citation support.*

---

## Recent developments (2023–2024 prioritized) and real-world implementations
1. **Prenatal detection and multidisciplinary perinatal planning** is a recurring theme in 2024 reports, supporting real-world implementation of fetal imaging (ultrasound/MRI) to guide delivery route and neonatal airway/feeding readiness. (qin2024aclinicalobservation pages 1-2, han2024fromprenataldiagnosis pages 1-3)
2. **Immunohistochemistry variability** (weak S-100/CD68 positivity in CGCE) is emphasized in 2024 literature, refining diagnostic practice away from relying on S-100 alone. (qin2024aclinicalobservation pages 1-2)
3. **Post-excision outcomes** (rapid return to feeding and no recurrence at 6–12 months) are reiterated in 2024 case reports, supporting early functional restoration as a practical clinical goal. (qin2024aclinicalobservation pages 1-2, chaudhry2024congenitalepulisreport pages 1-2)

## Direct quotes from abstracts (where available in retrieved texts)
- **Han et al., 2024 (Pathology and Oncology Research; published 10 Jul 2024; https://doi.org/10.3389/pore.2024.1611834):** “Herein, we detail a multidisciplinary approach and sequential treatment for two infants with congenital granular cell epulis (CGCE).” (han2024fromprenataldiagnosis pages 1-3)
- **Oriaifo et al., 2024 (European Journal of Clinical and Experimental Medicine; published 30 Dec 2024; https://doi.org/10.15584/ejcem.2024.4.6):** “Congenital epulis is a rare benign tumor that affects the oral cavity of newborns which typically presents as a solitary mass on the maxillary alveolar bridge at birth, with a predilection for the female gender.” (oriaifo2024congenitalepulisin pages 1-3)
- **Chaudhry et al., 2024 (Journal of Pediatric and Adolescent Surgery; https://doi.org/10.46831/jpas.v1i2.99):** “Congenital epulis is a rare benign… mass… commonly occurring at the anterior alveolar ridge of the maxilla.” (chaudhry2024congenitalepulisreport pages 1-2)

## Evidence limitations
- The retrieved evidence set did not contain MONDO/Orphanet/OMIM/ICD-11 codes or a definitive ICD-10 mapping for congenital epulis, nor did it provide causal genes or population-based incidence estimates from registries; most numeric estimates are literature-derived and may vary by source. (mcguire2006congenitalepulisa pages 3-4, vera2026épuliscongénitocaso pages 1-4, braz2022épuliscongénito pages 1-3)


References

1. (han2024fromprenataldiagnosis pages 1-3): Yibing Han, Wen Qiu, Yu Zhang, Mengmeng Hua, Shaohua Liu, and Zuoqing Dong. From prenatal diagnosis to surgical treatment: two case reports of congenital granular cell epulis. Pathology and Oncology Research, Jul 2024. URL: https://doi.org/10.3389/pore.2024.1611834, doi:10.3389/pore.2024.1611834. This article has 5 citations.

2. (mcguire2006pratiqueclinique pages 1-3): TP McGuire, PP Gomes, MM Freilich, and GKB Sándor. Pratiqueclinique. Unknown journal, 2006.

3. (qin2024aclinicalobservation pages 1-2): Feng Qin, Xiaochuan Xu, Yong Yang, Qiong Li, Ting Huang, Xiaoyan Chen, Xiaolan Chen, Yamin Liu, and Gongli Chen. A clinical observation report on prenatal management and postnatal treatment of congenital granular cell epulis. Maternal-Fetal Medicine, 6:102-105, Apr 2024. URL: https://doi.org/10.1097/fm9.0000000000000225, doi:10.1097/fm9.0000000000000225. This article has 1 citations.

4. (chaudhry2024congenitalepulisreport pages 1-2): Ali Raza Chaudhry, Rumaisaa Saman, Muhammad Umar Nisar, Khawar Abbas, and Samer Sikander. Congenital epulis: report of two cases. Journal of Pediatric and Adolescent Surgery, 1:117-119, Jul 2024. URL: https://doi.org/10.46831/jpas.v1i2.99, doi:10.46831/jpas.v1i2.99. This article has 3 citations.

5. (oriaifo2024congenitalepulisin pages 1-3): Sylvester Oriaifo, Osasere Andrew Eweka, and Kenneth Atoe. Congenital epulis in a newborn – a case report in benin city, nigeria. European Journal of Clinical and Experimental Medicine, 22:965-968, Dec 2024. URL: https://doi.org/10.15584/ejcem.2024.4.6, doi:10.15584/ejcem.2024.4.6. This article has 1 citations.

6. (mcguire2006congenitalepulisa pages 3-4): TP McGuire, PP Gomes, and MM Freilich. Congenital epulis: a surprise in the neonate. Unknown journal, 2006.

7. (braz2022épuliscongénito pages 1-3): Juliana Braz, Helena Sobrero, Jennise De los Santos, Mario Moraes, and Sheila Jacobsen. Épulis congénito. Archivos de Pediatría del Uruguay, May 2022. URL: https://doi.org/10.31134/ap.93.1.15, doi:10.31134/ap.93.1.15. This article has 0 citations.

8. (shuhairi2021aretrospectiveanalysis pages 1-2): Nadia Najwa Binti Shuhairi, Ajura Bt Abdul Jalil, Shin‐Hin Lau, Sumarni Bt Mohd Ghazali, and Chee Cheong Kee. A retrospective analysis of oral and maxillofacial biopsied specimens in malaysian newborns and infants. International Journal of Paediatric Dentistry, 31:496-503, Sep 2021. URL: https://doi.org/10.1111/ipd.12719, doi:10.1111/ipd.12719. This article has 6 citations and is from a domain leading peer-reviewed journal.

9. (qin2024aclinicalobservation pages 2-3): Feng Qin, Xiaochuan Xu, Yong Yang, Qiong Li, Ting Huang, Xiaoyan Chen, Xiaolan Chen, Yamin Liu, and Gongli Chen. A clinical observation report on prenatal management and postnatal treatment of congenital granular cell epulis. Maternal-Fetal Medicine, 6:102-105, Apr 2024. URL: https://doi.org/10.1097/fm9.0000000000000225, doi:10.1097/fm9.0000000000000225. This article has 1 citations.

10. (haghegh2024congenitalepulisa pages 4-6): Khadija Haghegh and Mohammed Almughrabi. Congenital epulis: a case report. Journal, Jul 2024. URL: https://doi.org/10.60692/z0ew7-7n257, doi:10.60692/z0ew7-7n257. This article has 0 citations.

11. (haghegh2024congenitalepulisa pages 1-4): Khadija Haghegh and Mohammed Almughrabi. Congenital epulis: a case report. Journal, Jul 2024. URL: https://doi.org/10.60692/z0ew7-7n257, doi:10.60692/z0ew7-7n257. This article has 0 citations.

12. (vera2026épuliscongénitocaso pages 1-4): RMCV Vera, TLP Mawyin, and RFA Bajaña. Épulis congénito: caso clínico y revisión de la literatura. Unknown journal, 2026.

13. (shuhairi2021aretrospectiveanalysis pages 4-5): Nadia Najwa Binti Shuhairi, Ajura Bt Abdul Jalil, Shin‐Hin Lau, Sumarni Bt Mohd Ghazali, and Chee Cheong Kee. A retrospective analysis of oral and maxillofacial biopsied specimens in malaysian newborns and infants. International Journal of Paediatric Dentistry, 31:496-503, Sep 2021. URL: https://doi.org/10.1111/ipd.12719, doi:10.1111/ipd.12719. This article has 6 citations and is from a domain leading peer-reviewed journal.

14. (han2024fromprenataldiagnosis pages 3-4): Yibing Han, Wen Qiu, Yu Zhang, Mengmeng Hua, Shaohua Liu, and Zuoqing Dong. From prenatal diagnosis to surgical treatment: two case reports of congenital granular cell epulis. Pathology and Oncology Research, Jul 2024. URL: https://doi.org/10.3389/pore.2024.1611834, doi:10.3389/pore.2024.1611834. This article has 5 citations.

15. (han2024fromprenataldiagnosis media e73f6ade): Yibing Han, Wen Qiu, Yu Zhang, Mengmeng Hua, Shaohua Liu, and Zuoqing Dong. From prenatal diagnosis to surgical treatment: two case reports of congenital granular cell epulis. Pathology and Oncology Research, Jul 2024. URL: https://doi.org/10.3389/pore.2024.1611834, doi:10.3389/pore.2024.1611834. This article has 5 citations.

16. (mcguire2006congenitalepulisa pages 1-3): TP McGuire, PP Gomes, and MM Freilich. Congenital epulis: a surprise in the neonate. Unknown journal, 2006.

17. (lacerda2025congenitalepulidisa pages 10-10): ACR Lacerda, KAF Cruz, and EHBS Lima. Congenital epulidis: a literature review-from diagnosis to treatment. Unknown journal, 2025.