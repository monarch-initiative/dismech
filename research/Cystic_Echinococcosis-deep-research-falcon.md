---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T13:35:08.498277'
end_time: '2026-04-04T13:50:11.304993'
duration_seconds: 902.81
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cystic echinococcosis
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 59
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cystic echinococcosis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Cystic echinococcosis** covering all of the
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
- **Disease Name:** Cystic echinococcosis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Cystic echinococcosis** covering all of the
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


## Cystic echinococcosis (CE) — comprehensive disease characteristics report (Infectious disease)

### Executive summary
Cystic echinococcosis (CE) (syn. hydatid disease) is a chronic zoonotic helminth infection caused by the larval (metacestode) stage of *Echinococcus granulosus* sensu lato, in which humans act as accidental intermediate hosts after ingesting eggs shed by canid definitive hosts. Disease is typically slowly progressive and often asymptomatic for years; clinical manifestations depend on cyst location (predominantly liver and lungs) and complications (e.g., rupture with anaphylaxis or secondary seeding). Contemporary management is stage- and anatomy-based using WHO-IWGE cyst staging; inactive cysts are generally observed, while active/transitional cysts are treated with benzimidazoles, percutaneous interventions, and/or surgery depending on stage and complexity. Burden remains substantial and is frequently underestimated due to underreporting and weak surveillance in endemic settings. (akbulut2025hydatiddisease pages 6-8, akbulut2025hydatiddisease pages 8-11, bold2024thediagnosticchallenge pages 1-2)


## 1. Disease Information

### 1.1 Overview and current understanding
CE is defined as human infection by the larval stage of *E. granulosus* s.l. producing unilocular, fluid-filled hydatid cysts that most often localize in liver and lungs; cyst rupture can disseminate protoscolices and trigger allergic/anaphylactic reactions. (jahan2025understandingechinococcosisa pages 3-7, akbulut2025hydatiddisease pages 6-8)

### 1.2 Key identifiers and controlled vocabularies
- **ICD-10:** CE was captured using ICD-10 **B67.1–B67.9** (within the B67.* echinococcosis block) in Mongolia surveillance work. (bold2024thediagnosticchallenge pages 2-4)
- **WHO-IWGE classification (ultrasound-based):** cysts are categorized into **active (CE1, CE2)**, **transitional (CE3a, CE3b)**, and **inactive (CE4, CE5)** stages, which guide treatment selection. (akbulut2025hydatiddisease pages 8-11)
- **MeSH / MONDO / Orphanet:** not explicitly reported in the retrieved full-text evidence and therefore cannot be asserted here without additional targeted retrieval.

### 1.3 Synonyms and alternative names
- **Hydatid disease / hydatid cyst disease** is used interchangeably with CE in recent clinical literature. (akbulut2025hydatiddisease pages 6-8, akbulut2025hydatiddisease pages 11-13)

### 1.4 Evidence source type
Information in this report is derived from aggregated disease-level resources (reviews, burden analyses) and multiple primary clinical/epidemiologic studies; several surveillance estimates explicitly note under-ascertainment when relying on surgical case series alone. (bold2024thediagnosticchallenge pages 5-7, bold2024thediagnosticchallenge pages 1-2)


## 2. Etiology

### 2.1 Disease causal factors
- **Infectious agent:** *Echinococcus granulosus* s.l. (larval stage in humans). (akbulut2025hydatiddisease pages 6-8, jahan2025understandingechinococcosisa pages 3-7)
- **Life cycle context:** transmission is maintained between canid definitive hosts (e.g., dogs) and herbivorous intermediate hosts (e.g., sheep/goats/cattle), with humans as accidental intermediate hosts. (jahan2025understandingechinococcosisa pages 3-7, akbulut2025hydatiddisease pages 6-8)

### 2.2 Risk factors (human)
Evidence from recent reviews and national studies supports the following as key risk factors:
- **Rural residence and dog ownership** (higher exposure probability); drinking commercially sourced water was associated with lower infection risk in pooled evidence summarized in a 2024 review. (hogea2024cysticechinococcosisin pages 6-7)
- **Practices enabling dog infection and environmental egg contamination:** dog access to infected offal and feeding dogs raw offal are repeatedly emphasized as key drivers of transmission; insufficient dog deworming is highlighted as a persistence factor in endemic settings. (jahan2025understandingechinococcosisa pages 7-10, tenzin2024theburdenand pages 2-3)
- **Bhutan risk context:** rural living, dog ownership, feeding dogs, home slaughtering, being a farmer, and unsafe drinking water were identified as relevant risk exposures in Bhutan’s national retrospective assessment. (tenzin2024theburdenand pages 2-3)

### 2.3 Protective factors
Direct quantitative protective-factor evidence was limited in retrieved sources; however, reduced exposure to infected dogs/offal and improved sanitation are consistently framed as protective measures (see Prevention section). (hogea2024cysticechinococcosisin pages 6-7)

### 2.4 Gene–environment interactions
No validated human host genetic susceptibility or explicit gene–environment interaction findings were identified in the retrieved evidence.


## 3. Phenotypes

### 3.1 Core clinical phenotypes (symptoms/signs/lab)
- **Asymptomatic or nonspecific symptoms for years** due to slow cyst growth. (akbulut2025hydatiddisease pages 6-8)
- **Hepatic CE phenotypes:** abdominal discomfort/pain, mass effect, cholestatic/biliary complications; rupture can trigger fever/urticaria/eosinophilia/anaphylaxis. (akbulut2025hydatiddisease pages 8-11)
- **Pulmonary CE phenotypes:** respiratory symptoms varying by size/location; lung is the second most common organ in population data. (tenzin2024theburdenand pages 1-2)

**Suggested HPO terms (non-exhaustive; mapped to typical CE manifestations):**
- Abdominal pain **HP:0002027**
- Hepatomegaly **HP:0002240**
- Liver cysts **HP:0001407**
- Pulmonary cysts **HP:0033149** (or related pulmonary lesion terms depending on ontology version)
- Eosinophilia **HP:0001880**
- Anaphylaxis **HP:0100845**

**Phenotype timing:** disease is typically **chronic/insidious** with prolonged asymptomatic periods. (akbulut2025hydatiddisease pages 6-8)

### 3.2 Frequency and organ distribution (recent data)
- **Bhutan (2015–2019, n=159):** liver **78%**, lungs **13%**; small fractions in other sites; 4 patients had both liver and lung involvement. (tenzin2024theburdenand pages 1-2, tenzin2024theburdenand pages 4-5)
- A 2024 review reiterates that hepatic disease is dominant (>70% in many summaries). (hogea2024cysticechinococcosisin pages 6-7)

### 3.3 Quality-of-life impact
Specific QoL instrument results (e.g., SF-36/EQ-5D) were not present in the retrieved evidence; nevertheless, CE contributes to substantial morbidity and prolonged hospitalization in national series (e.g., >47% hospitalized >4 days in Bhutan). (tenzin2024theburdenand pages 1-2)


## 4. Genetic/Molecular Information

### 4.1 Causal genes (human)
Not applicable in the Mendelian sense: CE is not a human genetic disease.

### 4.2 Parasite genotypes and molecular identification
The retrieved evidence included mention that isolates can be identified as *E. granulosus* s.l. genotypes via PCR-based methods in research settings, but systematic genotype–phenotype associations in humans were not extracted here. (mehdi2025designandevaluation pages 8-9)

### 4.3 Host genetic susceptibility / protective variants
No ClinVar/ClinGen/OMIM-style host causal variants were identified in the retrieved evidence.


## 5. Environmental Information

### 5.1 Environmental and lifestyle factors
Environmental contamination with parasite eggs is central; exposures are linked to rural pastoral settings, dog ownership, and slaughter/offal-handling practices. (jahan2025understandingechinococcosisa pages 3-7, tenzin2024theburdenand pages 2-3)

### 5.2 Infectious agent (taxonomy)
- **Agent:** *Echinococcus granulosus* sensu lato (cestode). (akbulut2025hydatiddisease pages 6-8)


## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (from trigger to clinical manifestations)
1. **Exposure/entry:** ingestion of eggs shed in canid feces. (jahan2025understandingechinococcosisa pages 3-7)
2. **Early development:** eggs release oncospheres that penetrate the intestinal wall and disseminate (predominantly to liver via portal circulation; also lungs). (jahan2025understandingechinococcosisa pages 3-7)
3. **Lesion formation:** development of slowly enlarging hydatid cysts; growth has been described around **~1–5 cm/year** and may be clinically silent for years. (akbulut2025hydatiddisease pages 6-8)
4. **Host response and tissue remodeling:** formation of a host-derived pericyst/adventitia and variable immune infiltration; organ dysfunction is mainly from mass effect, biliary/vascular involvement, or complications. (akbulut2025hydatiddisease pages 8-11, petrone2024evaluationofthe pages 1-2)
5. **Complications:** rupture can release antigenic material causing urticaria/eosinophilia/anaphylaxis and can seed secondary echinococcosis. (jahan2025understandingechinococcosisa pages 3-7, akbulut2025hydatiddisease pages 8-11)

### 6.2 Immune system involvement (recent human evidence; 2024)
A 2024 human study analyzing tissue and blood immune responses reported that CE lesions can persist for decades due to immune modulation. In pericyst and adjacent liver tissue, aggregates of **CD3+ T cells (predominantly CD4+)** and **B-cell aggregates** were observed; **monocytes/granulocytes were rare**. Tissue cytokine staining showed **scarce Th2 cytokines (IL-4/IL-13)** but **moderate IFN-γ**. In contrast, peripheral whole-blood stimulation with parasite antigen B (AgB) showed increased **IL-4** responses in CE patients (p=0.003 in larger cohort confirmation), while IFN-γ responses were similar between cases and controls. (petrone2024evaluationofthe pages 1-2, petrone2024evaluationofthe pages 7-9)

**Suggested ontology mappings:**
- **GO biological processes:** immune response (GO:0006955); T cell activation (GO:0042110); cytokine-mediated signaling pathway (GO:0019221); response to interferon-gamma (GO:0034341); type 2 immune response (GO:0042092).
- **Cell Ontology (CL) terms (examples):** CD4-positive, alpha-beta T cell (CL:0000624); B cell (CL:0000236); fibroblast (CL:0000057) (for pericyst/adventitia context).

### 6.3 Molecular profiling / omics
No transcriptomic/proteomic/metabolomic datasets were directly extracted from the retrieved human CE evidence.


## 7. Anatomical Structures Affected

### 7.1 Organ-level involvement
- **Primary:** liver (dominant), lungs (second). (tenzin2024theburdenand pages 1-2)
- **Other possible sites:** wide anatomic range has been described (bone, kidney, spleen, soft tissue, thyroid, breast, adrenal, CNS), though frequencies vary across series; such dissemination supports broad differential consideration in endemic patients. (akbulut2025hydatiddisease pages 6-8)

**Suggested UBERON terms (examples):** liver (UBERON:0002107), lung (UBERON:0002048), spleen (UBERON:0002106).

### 7.2 Tissue/cell level
- Host-derived **pericyst/adventitia** and surrounding parenchyma are key sites of immune infiltration, dominated by CD4+ lymphocytes in examined hepatic cases. (petrone2024evaluationofthe pages 1-2)

### 7.3 Subcellular localization
Not directly addressed in retrieved evidence.


## 8. Temporal Development

### 8.1 Onset and course
- Typically **chronic** and **insidious** with long asymptomatic phases. (akbulut2025hydatiddisease pages 6-8)
- Cyst growth over years contributes to delayed diagnosis and late-stage complications in many endemic settings. (akbulut2025hydatiddisease pages 6-8)

### 8.2 Progression and staging
- WHO-IWGE staging divides cysts into **active**, **transitional**, and **inactive** categories that correspond to viability/activity and guide treatment. (akbulut2025hydatiddisease pages 8-11)


## 9. Inheritance and Population

### 9.1 Epidemiology and burden (recent quantitative data)
Key recent burden statistics include:
- **GBD 2019 analysis (published 2024):** global ASIR changed from **2.65/100,000 (1990)** to **2.60/100,000 (2019)** with EAPC −0.18%; deaths and DALYs declined overall 1990–2019, but projections suggest ASIR declines while ASMR and age-standardized DALY rates may rise 2020–2030. (tian2024globalregionaland pages 1-2)
- **GBD 2021 figures cited in a 2025 textbook chapter:** **148,521 new cases**, **633,404 prevalent cases**, **1,364 deaths**, **105,072 DALYs** with age-standardized incidence **1.82/100,000** and prevalence **7.69/100,000**. (akbulut2025hydatiddisease pages 6-8)
- **Bhutan national retrospective burden (published 2024; 2015–2019):** average annual incidence **4.4/100,000**; estimated **~39 DALYs/year** for treatment-seeking cases and possibly **~80 DALYs/year** including non-treatment-seeking cases; liver **78%**, lungs **13%**. (tenzin2024theburdenand pages 1-2)
- **Mongolia underreporting (published 2024):** predicted diagnosed burden **15.9/100,000** vs surgical-case prevalence **2.2/100,000** (i.e., surgical cases represent ~one-eighth of diagnosed burden). (bold2024thediagnosticchallenge pages 5-7, bold2024thediagnosticchallenge pages 1-2)
- **Population ultrasound screening synthesis (2024 review):** pooled sample **130,093**, **2,077** CE cases, with mean prevalence around **0.0160** (95% CI 0.0153–0.0166) in collated studies. (hogea2024cysticechinococcosisin pages 6-7)

### 9.2 Demographics
- Bhutan data show higher incidence among females vs males (6.11 vs 2.79 per 100,000; p<0.001) and concentration among farmers. (tenzin2024theburdenand pages 3-3)

### 9.3 Genetic inheritance
Not applicable.


## 10. Diagnostics

### 10.1 Imaging
- **Ultrasound:** primary modality for abdominal CE and the basis of WHO-IWGE staging. (akbulut2025hydatiddisease pages 8-11)
- **CT/MRI/MRCP/ERCP:** CT useful for calcification/anatomy; MRI for soft tissue; MRCP/ERCP for biliary involvement. (akbulut2025hydatiddisease pages 8-11)
- **PET/CT:** may correlate with serology and help guide benzimidazole duration in selected settings. (akbulut2025hydatiddisease pages 11-13)

### 10.2 Serology (recent comparative performance)
A 2024 head-to-head evaluation in 74 suspected CE sera reported:
- **ELISA:** sensitivity **85.42%**, specificity **88.46%**.
- **IFA:** sensitivity **83.33%**, specificity **88.46%**.
- **Fumouze IHA:** sensitivity **70.83%**, specificity **96.15%**.
- **Siemens IHA:** sensitivity **66.67%**, specificity reported ~**92.31%** in the study summary.
- **Western blot:** sensitivity **72.92%**, specificity **88.46%**.
These findings support combining tests and interpreting serology alongside imaging due to false negatives/positives. (erganis2024comparisonofmethods pages 4-6)

In Mongolia’s underreporting analysis, practical diagnostic constraints were emphasized; RDTs for active cysts were reported with sensitivity **74%** and specificity **96%**, contrasted with ELISA **69% sensitivity / 96% specificity** in that local context. (bold2024thediagnosticchallenge pages 7-8)

### 10.3 Molecular diagnostics (recent developments)
Emerging molecular diagnostics include:
- **Multiplex qPCR (QPCR-Echino):** ongoing diagnostic clinical study aims to assess sensitivity of Echinococcus DNA detection in operating specimens/biopsies/puncture fluids and plasma (NCT05824442; start 2023-10-24). (NCT05824442 chunk 1)
- **ddPCR for circulating cfDNA:** exploratory interventional study evaluating ddPCR sensitivity for plasma *E. granulosus* s.l. cfDNA detection in untreated hepatic CE, with sensitivity stratified by cyst stage (NCT05769790; start 2022-03-21; primary completion estimated 2024-03). (NCT05769790 chunk 1)

### 10.4 Differential diagnosis
Detailed differential diagnosis lists were not available in the retrieved evidence; in practice, staging-compatible imaging patterns plus serology/molecular confirmation are used to distinguish CE from non-parasitic cysts and other hepatic/pulmonary lesions.


## 11. Outcome / Prognosis

### 11.1 Mortality and recurrence
- A 2024 GBD-linked review reports post-surgical mortality about **2.2%** and postoperative recurrence about **6.5%** in summarized literature. (tian2024globalregionaland pages 1-2)
- In a hospital series from an endemic area of Peru (2010–2019), post-surgical recurrence was reported as **16.5%** at median **32.3 months** in a setting with advanced/complicated disease and incomplete staging-guided management. (akbulut2025hydatiddisease pages 8-11)

### 11.2 Burden and hospitalization
In Bhutan, >47% of patients were hospitalized for >4 days, and most were treated surgically (>82%). (tenzin2024theburdenand pages 1-2)


## 12. Treatment

### 12.1 Stage-based treatment concepts (WHO-IWGE)
- **CE4–CE5 (inactive):** typically **watch-and-wait** (observation). (akhan2025theroleof pages 2-4, akbulut2025hydatiddisease pages 8-11)
- **CE1, CE3a:** percutaneous techniques such as **PAIR** or **standard catheterization** are recommended options; albendazole is used peri-procedurally. (akhan2025theroleof pages 2-4)
- **CE2, CE3b:** **modified catheterization (Mo-CAT)** is highlighted as effective for multivesicular/daughter-cyst-rich lesions. (akhan2025theroleof pages 6-8)

### 12.2 Pharmacotherapy
- **Albendazole (ABZ):** first-line benzimidazole, typically **10–15 mg/kg/day** with fatty meal; duration varies and lacks global consensus. (akbulut2025hydatiddisease pages 11-13)
- **Real-world outcome (Uruguay, 2024):** among 36 adults completing 5-year follow-up, ABZ-only achieved **93.75%** success; ABZ+PZQ achieved **100%** success in 4 patients; no deaths occurred. (rosa2024followupstudy pages 1-2)

**Suggested MAXO terms (examples):** albendazole therapy (MAXO term for antiparasitic drug therapy), praziquantel therapy.

### 12.3 Interventional radiology (real-world implementation)
A 2025 interventional radiology review emphasizes stage-specific percutaneous management:
- **CE1/CE3a:** PAIR or catheterization; reported success up to **96%** and recurrence as low as **4%** overall. A meta-analysis cited found percutaneous therapy vs surgery for CE1/CE3a had lower mortality (0.1% vs 0.7%), fewer major complications (7.9% vs 25.1%), fewer minor complications (13.1% vs 33%), lower recurrence (1.6% vs 6.3%), and shorter hospital stay (2.4 vs 15 days). (akhan2025theroleof pages 6-8)
- **CE2/CE3b:** Mo-CAT long-term series (132 cysts) reported **0 mortality**, major complications **10%**, recurrence **4.5%**, mean hospital stay **3.8 days**, mean follow-up **52 months**. (akhan2025theroleof pages 6-8)
A table summarizing stage-specific recurrence bands (<5% for CE1/CE3a; <5–7% for CE2/CE3b) is available in the cited review. (akhan2025theroleof media 3452c1f5)

### 12.4 Surgery
Surgery remains necessary for complicated disease (e.g., rupture into peritoneal/pleural cavities, complex biliary communication, infected cysts, or when percutaneous resources are unavailable). (akhan2025theroleof pages 2-4)

### 12.5 Ongoing/recent clinical trials (selected)
- **Adjuvant ABZ after pulmonary hydatid resection:** randomized trial ABZ vs placebo; primary endpoint recurrence at 6 months; start 2024-02-01 (NCT06483880). (NCT06483880 chunk 1)
- **Laparoscopic vs open liver surgery:** randomized non-inferiority trial, n=350, recurrence endpoint at 24 months (NCT01643018). (NCT01643018 chunk 1)
- **Molecular diagnostics trials:** multiplex qPCR (NCT05824442) and ddPCR cfDNA (NCT05769790) as described above. (NCT05824442 chunk 1, NCT05769790 chunk 1)


## 13. Prevention

### 13.1 Primary prevention (One Health)
A 2024 review synthesizing prevention measures emphasizes:
- Preventing canid access to infected offal.
- Controlling stray dogs and discouraging home slaughter.
- Regular deworming of dogs with praziquantel.
- Improved sanitation and public education to reduce fecal–oral exposure.
- Sheep vaccination is described as used in **Argentina and China** (recombinant vaccine) as part of control strategies. (hogea2024cysticechinococcosisin pages 6-7)

### 13.2 Secondary prevention (screening/early detection)
Ultrasound-based population screening is used in endemic programs and can detect early-stage hepatic cysts; this is also relevant for burden estimation given long asymptomatic periods. (hogea2024cysticechinococcosisin pages 6-7)

### 13.3 Tertiary prevention
Long-term follow-up after treatment is emphasized; for example, pharmacologically treated cohorts were followed for **≥5 years** under WHO-IWGE guidance in Uruguay, and percutaneous therapy reviews advocate long-term monitoring (≥10 years). (rosa2024followupstudy pages 1-2, akhan2025theroleof pages 4-6)


## 14. Other species / Natural disease

### 14.1 Species affected and zoonotic cycle
- **Definitive hosts:** canids (not exhaustively enumerated in retrieved evidence).
- **Intermediate hosts:** livestock such as sheep/goats/cattle; other domestic animals implicated in some settings.
- **Humans:** accidental intermediate hosts.
Transmission is driven by egg shedding in canid feces and ingestion by intermediate hosts; dog infection is reinforced by consumption of infected viscera/offal. (jahan2025understandingechinococcosisa pages 3-7, tenzin2024theburdenand pages 2-3)

### 14.2 Veterinary relevance
CE is a One Health problem affecting humans, livestock production, and the food chain; economic burden estimates include treatment and livestock losses. (hogea2024cysticechinococcosisin pages 6-7)


## 15. Model organisms

Specific laboratory model organism systems for CE pathogenesis and therapy testing were not directly described in the retrieved evidence. The literature does reference experimental and animal-model immunology observations (e.g., sheep tissue regulatory cytokines), but detailed model cataloging (mouse strains, in vitro systems, etc.) was not available in the extracted full texts. (petrone2024evaluationofthe pages 2-3)


## Recent developments and expert analysis (2023–2024 prioritized)

1. **Burden quantification and forecasting:** A 2024 GBD 2019-based analysis provides updated global incidence trends and projections to 2030, highlighting persistent burden in low-SDI regions and among women/older adults. (tian2024globalregionaland pages 1-2)
2. **Surveillance and underreporting:** A 2024 Mongolia analysis shows surgical-case reporting captures only ~1/8 of diagnosed burden and identifies operational weaknesses (laboratory capacity, reporting workflows, insufficient albendazole supply, limited percutaneous availability). This supports expert consensus that CE burden is often underestimated. (bold2024thediagnosticchallenge pages 5-7, bold2024thediagnosticchallenge pages 7-8)
3. **Human immunopathology:** A 2024 study comparing local tissue vs peripheral immune responses indicates discordant local (Th1-leaning/low Th2) vs peripheral (AgB-specific IL-4) signatures and emphasizes the adventitia/pericyst as an immunopathogenic interface. (petrone2024evaluationofthe pages 7-9)
4. **Treatment effectiveness of percutaneous interventions:** Stage-stratified percutaneous outcomes compiled in 2025 (with cited meta-analysis) show lower recurrence, complications, and hospital stay compared with surgery in selected CE1/CE3a cysts, and strong Mo-CAT outcomes for CE2/CE3b—supporting ongoing practice shift toward minimally invasive management when expertise is available. (akhan2025theroleof pages 6-8)


## Evidence excerpts (abstract-quotable statements)
- Mongolia underreporting estimate: “**the prevalence could be approximately 16 cases per 100,000 people, which is eight times higher than the number of reported surgical cases**.” (bold2024thediagnosticchallenge pages 7-8)
- Bhutan incidence and burden: average annual incidence **4.4 per 100,000** and estimated **~39 DALYs/year** (treatment-seeking), **~80 DALYs/year** including non-treatment-seeking. (tenzin2024theburdenand pages 1-2)


## Summary artifacts
The following structured tables are provided for knowledge-base ingestion.

| Category | Item | Details | Study/Source | Setting | Years | Quantitative metrics | Publication year | URL | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| Identifier / classification | ICD-10 | Echinococcosis is classified under ICD-10 code block **B67.***; Mongolia study used **B67.1–B67.9** for case capture | Bold et al. | Mongolia hospital reporting / surveillance methods | 2006–2016 case capture; published 2024 | ICD-10 range B67.1–B67.9 used to identify CE records | 2024 | https://doi.org/10.3390/tropicalmed9070163 | (bold2024thediagnosticchallenge pages 2-4) |
| Identifier / classification | Disease name / synonym | **Cystic echinococcosis (CE)**; related common name **hydatid disease / hydatid cyst disease** | Akbulut; Govindasamy et al. | General disease overview | Published 2023–2025 | CE described as hydatid disease caused by larval Echinococcus | 2025; 2023 | https://doi.org/10.1007/978-3-031-97277-5; https://doi.org/10.1177/20499361231171478 | (akbulut2025hydatiddisease pages 6-8, akbulut2025hydatiddisease pages 11-13) |
| Identifier / classification | Causative agent | **Echinococcus granulosus sensu lato** (larval/metacestode stage in humans) | Akbulut; Jahan et al. | General disease overview | Published 2025 | Humans are accidental intermediate hosts infected by eggs from canid feces | 2025 | https://doi.org/10.1007/978-3-031-97277-5; https://doi.org/10.3329/bjz.v53i1.82673 | (akbulut2025hydatiddisease pages 6-8, jahan2025understandingechinococcosisa pages 3-7) |
| Identifier / classification | MeSH / controlled vocabulary related term | Closely aligned controlled-vocabulary term used in literature: **Echinococcosis / Hydatid Disease**; exact MeSH identifier not extracted in retrieved evidence | Recent reviews/books | General | Published 2023–2025 | Controlled-vocabulary style naming consistent across sources, but MeSH ID not directly reported in retrieved context | 2023–2025 | https://doi.org/10.3390/tropicalmed9020036; https://doi.org/10.1177/20499361231171478 | (hogea2024cysticechinococcosisin pages 16-17, akbulut2025hydatiddisease pages 11-13) |
| Classification | WHO-IWGE cyst stage groups | **Active:** CE1, CE2; **Transitional:** CE3a, CE3b; **Inactive:** CE4, CE5 | Akbulut | General clinical classification | Published 2025 | WHO-IWGE stage grouping guides treatment selection | 2025 | https://doi.org/10.1007/978-3-031-97277-5 | (akbulut2025hydatiddisease pages 8-11) |
| Epidemiology / burden | Global burden (GBD 2019) | Human CE burden remained high globally with only slight ASIR decline | Tian et al. | Global | 1990–2019 | **ASIR 2.65/100,000 (1990)** to **2.60/100,000 (2019)**; EAPC **−0.18%**; deaths, DALYs, ASMR declined overall; projected ASIR decline but ASMR and age-standardized DALY rise through 2030 | 2024 | https://doi.org/10.3390/tropicalmed9040087 | (tian2024globalregionaland pages 1-2) |
| Epidemiology / burden | Global burden (GBD 2021 figures cited in book excerpt) | Updated global CE burden from GBD 2021 | Akbulut | Global | 2021 | **148,521 new cases**, **633,404 prevalent cases**, **1,364 deaths**, **105,072 DALYs**; age-standardized incidence **1.82/100,000** and prevalence **7.69/100,000** | 2025 | https://doi.org/10.1007/978-3-031-97277-5 | (akbulut2025hydatiddisease pages 6-8, akbulut2025hydatiddisease pages 8-11) |
| Epidemiology / burden | Global pooled ultrasound prevalence | Population-based ultrasound data compiled across continents | Hogea et al. | Multi-continent pooled survey data | Not uniform; review published 2024 | **130,093** individuals screened; **2,077** CE patients; mean prevalence **~0.0160** (95% CI **0.0153–0.0166**) | 2024 | https://doi.org/10.3390/tropicalmed9020036 | (hogea2024cysticechinococcosisin pages 6-7) |
| Epidemiology / burden | Bhutan national retrospective study | First burden/distribution estimate from hospital data | Tenzin et al. | Bhutan | 2015–2019 | **159 cases**; average annual incidence **4.4/100,000**; estimated burden **~39 DALYs/year** for treatment-seeking cases and **~80 DALYs/year** including non-treatment-seeking cases; liver **78%**, lungs **13%** | 2024 | https://doi.org/10.1017/s0031182024001069 | (tenzin2024theburdenand pages 1-2) |
| Epidemiology / burden | Bhutan demographic/risk pattern | Higher incidence in women and farmers; central/western districts most affected | Tenzin et al. | Bhutan | 2015–2019 | Female incidence **6.11/100,000** vs male **2.79/100,000**; majority farmers; >82% surgical treatment | 2024 | https://doi.org/10.1017/s0031182024001069 | (tenzin2024theburdenand pages 3-3, tenzin2024theburdenand pages 4-5) |
| Epidemiology / burden | Mongolia underreporting estimate | Surgical reporting captures only a fraction of diagnosed CE | Bold et al. | Mongolia | Surgical data 2006–2016; extrapolated prevalence for 2018 / diagnosed burden | Predicted diagnosed burden **15.9/100,000** vs surgical **2.2/100,000**; non-surgical **13.6/100,000**; surgical cases represent about **one-eighth** of diagnosed cases | 2024 | https://doi.org/10.3390/tropicalmed9070163 | (bold2024thediagnosticchallenge pages 5-7, bold2024thediagnosticchallenge pages 1-2) |
| Epidemiology / burden | Mongolia management gaps | Underreporting linked to weak reporting and low staging use | Bold et al. | Mongolia | Published 2024 | Cyst classification usage and disease monitoring scored **1.86–1.95**; ultrasound availability relatively strong (**3.60–3.97**) | 2024 | https://doi.org/10.3390/tropicalmed9070163 | (bold2024thediagnosticchallenge pages 7-8, bold2024thediagnosticchallenge pages 5-7) |
| Epidemiology / burden | Endemic community burden | In highly exposed rural communities CE incidence/prevalence can be much higher than global averages | Jahan et al.; Tian et al. | Endemic rural hotspots globally | Various; published 2024–2025 | Incidence may range from **<1 to >200/100,000** in highly exposed rural communities; hotspot prevalence may reach **5–10%** | 2025; 2024 | https://doi.org/10.3329/bjz.v53i1.82673; https://doi.org/10.3390/tropicalmed9040087 | (jahan2025understandingechinococcosisa pages 3-7, tian2024globalregionaland pages 1-2) |


*Table: This table compiles key disease identifiers, terminology, classification, and recent epidemiology/burden estimates for cystic echinococcosis. It is useful as a quick reference for mapping the disease concept and anchoring a knowledge-base entry with current quantitative data.*

| Domain | Modality / strategy | WHO-IWGE stage / indication | When used | Key performance / outcomes | Source (year) | URL | Evidence |
|---|---|---|---|---|---|---|---|
| Diagnosis | Ultrasound (US) | All suspected abdominal/hepatic CE; staging into CE1–CE5 | First-line imaging; classification and treatment planning | Primary imaging modality for CE; pooled population screening review compiled **130,093** screened individuals with **2,077** CE cases; WHO-IWGE staging used for management decisions rather than a single sensitivity estimate (hogea2024cysticechinococcosisin pages 6-7, akbulut2025hydatiddisease pages 8-11) | Hogea et al. 2024; Akbulut 2025 | https://doi.org/10.3390/tropicalmed9020036 ; https://doi.org/10.1007/978-3-031-97277-5 | (hogea2024cysticechinococcosisin pages 6-7, akbulut2025hydatiddisease pages 8-11) |
| Diagnosis | CT | Complex hepatic CE; calcified cysts; preoperative mapping; complications | Second-line / complementary imaging | Useful for calcified walls (especially CE5), anatomy, and complications; Yemen retrospective CT series found CE1 **38.56%** and CE3 **34.02%** among 1,669 cysts, with mass effect **38%**, intrabiliary rupture **4%**, intraperitoneal rupture **1.4%** (akbulut2025hydatiddisease pages 8-11) | Akbulut 2025; Al-Shehari et al. 2025 | https://doi.org/10.1007/978-3-031-97277-5 ; https://doi.org/10.1007/s44197-025-00429-3 | (akbulut2025hydatiddisease pages 8-11) |
| Diagnosis | MRI / MRCP | Soft-tissue definition; biliary tree involvement | Complementary imaging when US/CT insufficient | Superior soft-tissue characterization; MRCP/ERCP useful for biliary communication assessment (akbulut2025hydatiddisease pages 8-11) | Akbulut 2025 | https://doi.org/10.1007/978-3-031-97277-5 | (akbulut2025hydatiddisease pages 8-11) |
| Diagnosis | PET/CT | Selected cases to assess lesion activity / treatment follow-up | Specialized follow-up, especially activity assessment | PET/CT metabolic activity correlates with serology and may help guide benzimidazole duration; negative PET/CT plus low serology may support stopping therapy (akbulut2025hydatiddisease pages 11-13) | Akbulut 2025 | https://doi.org/10.1007/978-3-031-97277-5 | (akbulut2025hydatiddisease pages 11-13) |
| Diagnosis | ELISA (IgG) serology | Adjunct across stages; best interpreted with imaging | Supportive diagnosis, especially liver CE; screening/confirmation workflows | In comparative study of 74 sera: positivity **58.1% (43/74)**; sensitivity **85.42%**; specificity **88.46%**. Highest sensitivity among compared assays in that study (erganis2024comparisonofmethods pages 4-6, erganis2024comparisonofmethods pages 1-2) | Erganis et al. 2024 | https://doi.org/10.1007/s11686-024-00840-z | (erganis2024comparisonofmethods pages 4-6, erganis2024comparisonofmethods pages 1-2) |
| Diagnosis | Indirect fluorescent antibody (IFA) | Adjunct serology | Alternative serology / confirmatory combination | Positivity **56.7% (42/74)**; sensitivity **83.33%**; specificity **88.46%** (erganis2024comparisonofmethods pages 4-6) | Erganis et al. 2024 | https://doi.org/10.1007/s11686-024-00840-z | (erganis2024comparisonofmethods pages 4-6) |
| Diagnosis | Indirect hemagglutination assay (IHA) – Fumouze | Adjunct serology | Practical routine serology | Positivity **47.3% (35/74)**; sensitivity **70.83%**; specificity **96.15%**; highest specificity in the comparison study (erganis2024comparisonofmethods pages 4-6, erganis2024comparisonofmethods pages 1-2) | Erganis et al. 2024 | https://doi.org/10.1007/s11686-024-00840-z | (erganis2024comparisonofmethods pages 4-6, erganis2024comparisonofmethods pages 1-2) |
| Diagnosis | Indirect hemagglutination assay (IHA) – Siemens | Adjunct serology | Practical routine serology | Positivity **44.6% (33/74)**; sensitivity **66.67%**; specificity reported inconsistently in excerpts, likely ~**92.31%** in full study; lower sensitivity than ELISA/IFA (erganis2024comparisonofmethods pages 4-6, erganis2024comparisonofmethods pages 6-8) | Erganis et al. 2024 | https://doi.org/10.1007/s11686-024-00840-z | (erganis2024comparisonofmethods pages 4-6, erganis2024comparisonofmethods pages 6-8) |
| Diagnosis | Western blot (WB) | Confirmatory serology | Confirmation of equivocal serology / species banding | Positivity **51.3% (38/74)**; sensitivity **72.92%**; specificity **88.46%**; near-100% specificity is cited in review/book context for confirmatory use, but head-to-head study showed lower real-world specificity (erganis2024comparisonofmethods pages 4-6, akbulut2025hydatiddisease pages 11-13) | Erganis et al. 2024; Akbulut 2025 | https://doi.org/10.1007/s11686-024-00840-z ; https://doi.org/10.1007/978-3-031-97277-5 | (erganis2024comparisonofmethods pages 4-6, akbulut2025hydatiddisease pages 11-13) |
| Diagnosis | Rapid diagnostic test (RDT) for active cysts | Active cysts, especially field/rural use | Point-of-care option where access is limited | Mongolia review context reported sensitivity **74%** and specificity **96%** for active cyst RDTs; contrasted with ELISA **69% sensitivity / 96% specificity** in the cited local context (bold2024thediagnosticchallenge pages 7-8) | Bold et al. 2024 | https://doi.org/10.3390/tropicalmed9070163 | (bold2024thediagnosticchallenge pages 7-8) |
| Diagnosis | Sandwich ELISA for circulating antigen | Investigational / research-supported serodiagnosis | Serum antigen detection | Human sensitivity **98.25% (56/57)** and specificity **100%** in a human/camel study; requires further external validation before routine adoption (mehdi2025designandevaluation pages 8-9) | Maher et al. 2024 | https://doi.org/10.1007/s11259-024-10375-3 | (mehdi2025designandevaluation pages 8-9) |
| Diagnosis | Multiplex quantitative PCR (QPCR-Echino) | Confirmed CE/AE; tissue, puncture fluid, plasma | Investigational molecular diagnosis | Prospective diagnostic study, enrollment **43**; designed to evaluate sensitivity of Echinococcus DNA detection in tissue/plasma, especially useful when routine diagnosis is difficult or immunocompromise present (NCT05824442 chunk 1) | NCT05824442 (2023 record) | https://clinicaltrials.gov/study/NCT05824442 | (NCT05824442 chunk 1) |
| Diagnosis | ddPCR for circulating cell-free DNA | Untreated hepatic CE, stage-stratified | Investigational liquid biopsy | Exploratory multicenter study, enrollment ~**20**; primary endpoint is ddPCR sensitivity for plasma cfDNA detection, including stratification by active vs inactive cyst stage (NCT05769790 chunk 1) | NCT05769790 (2022 record) | https://clinicaltrials.gov/study/NCT05769790 | (NCT05769790 chunk 1) |
| Treatment | Watch-and-wait | **CE4–CE5** (inactive cysts) | Observation for inactive uncomplicated cysts | Standard stage-based strategy; inactive cysts are generally managed with observation rather than intervention (akbulut2025hydatiddisease pages 8-11, akhan2025theroleof pages 2-4) | Akbulut 2025; Akhan & Ciftci 2025 | https://doi.org/10.1007/978-3-031-97277-5 ; https://doi.org/10.1159/000547623 | (akbulut2025hydatiddisease pages 8-11, akhan2025theroleof pages 2-4) |
| Treatment | Albendazole (ABZ) monotherapy | Mainly small uncomplicated **CE1 / CE3a**; adjunct peri-procedurally | First-line benzimidazole; also pre/post surgery or percutaneous treatment | First-line dose **10–15 mg/kg/day** with fatty meal; in Uruguay cohort of adults completing 5-year follow-up, ABZ-alone achieved **93.75%** success (32 patients), **0 deaths** (akbulut2025hydatiddisease pages 11-13, rosa2024followupstudy pages 1-2) | Akbulut 2025; Rosa et al. 2024 | https://doi.org/10.1007/978-3-031-97277-5 ; https://doi.org/10.1186/s12879-024-09539-y | (akbulut2025hydatiddisease pages 11-13, rosa2024followupstudy pages 1-2) |
| Treatment | Albendazole + praziquantel (PZQ) | Selected difficult / multi-cyst or perioperative cases | Combination pharmacotherapy when surgery impractical or adjunct desired | Uruguay cohort: **100%** success in **4** patients receiving ABZ/PZQ, with 5-year follow-up; evidence is small and non-randomized (rosa2024followupstudy pages 1-2) | Rosa et al. 2024 | https://doi.org/10.1186/s12879-024-09539-y | (rosa2024followupstudy pages 1-2) |
| Treatment | PAIR (puncture–aspiration–injection–reaspiration) | **CE1, CE3a** | Preferred percutaneous therapy for uncomplicated active/transitional liver cysts | Review reports percutaneous success rates up to **96%** and recurrence as low as **4%** overall for liver CE; meta-analysis for CE1/CE3a found mortality **0.1% vs 0.7%** for surgery, major complications **7.9% vs 25.1%**, minor complications **13.1% vs 33%**, recurrence **1.6% vs 6.3%**, hospital stay **2.4 vs 15 days** (percutaneous vs surgery) (akhan2025theroleof pages 1-2, akhan2025theroleof pages 6-8) | Akhan & Ciftci 2025 | https://doi.org/10.1159/000547623 | (akhan2025theroleof pages 1-2, akhan2025theroleof pages 6-8) |
| Treatment | Standard catheterization (S-CAT) | **CE1, CE3a**, especially giant cysts >10 cm or when PAIR inadequate | Percutaneous drainage alternative / modification | Used when membranes obstruct aspiration or cystobiliary communication develops; recurrence for CE1/3a in table reported **<5%**; catheter left until drainage **<10 mL/day** (akhan2025theroleof pages 4-6, akhan2025theroleof pages 2-4, akhan2025theroleof media 3452c1f5) | Akhan & Ciftci 2025 | https://doi.org/10.1159/000547623 | (akhan2025theroleof pages 4-6, akhan2025theroleof pages 2-4, akhan2025theroleof media 3452c1f5) |
| Treatment | Modified catheterization (Mo-CAT) | **CE2, CE3b** | Preferred percutaneous option for multivesicular / daughter-cyst-rich lesions | Long-term series of **132** cysts: **0 mortality**, major complications **10%** (managed non-surgically), recurrence **4.5%**, mean hospital stay **3.8 days**, mean follow-up **52 months**; table summary gives CE2/3b recurrence roughly **<5–7%** (akhan2025theroleof pages 6-8, akhan2025theroleof pages 4-6, akhan2025theroleof media 3452c1f5) | Akhan & Ciftci 2025 | https://doi.org/10.1159/000547623 | (akhan2025theroleof pages 6-8, akhan2025theroleof pages 4-6, akhan2025theroleof media 3452c1f5) |
| Treatment | Surgery (open or laparoscopic; radical or conservative depending case) | Large, complicated, superficial, ruptured, infected, biliary-communicating, multi-daughter cysts; extrahepatic or non-percutaneous candidates | Definitive treatment when complications/anatomy preclude medical or percutaneous options | Historical mainstay; global review cites post-surgical mortality about **2.2%** and postoperative recurrence about **6.5%** (GBD review context). In Peru hospital series, post-surgical recurrence **16.5%** at median **32.3 months** in advanced/complicated disease (tian2024globalregionaland pages 1-2, akbulut2025hydatiddisease pages 8-11) | Tian et al. 2024; Akbulut 2025; Peru medRxiv 2024 | https://doi.org/10.3390/tropicalmed9040087 ; https://doi.org/10.1007/978-3-031-97277-5 ; https://doi.org/10.1101/2024.09.12.24313559 | (tian2024globalregionaland pages 1-2, akbulut2025hydatiddisease pages 8-11) |
| Treatment | Laparoscopic vs open liver surgery | Adults with limited hepatic CE amenable to conservative surgery | Comparative operative strategy | Registered randomized non-inferiority trial enrolled **350** participants; primary outcome was recurrence at **24 months** with secondary outcomes including mortality, complications, pain, hospital stay, operation time, QoL. Results not provided in retrieved chunk (NCT01643018 chunk 1) | NCT01643018 (2006 record) | https://clinicaltrials.gov/study/NCT01643018 | (NCT01643018 chunk 1) |
| Treatment | Adjuvant albendazole after pulmonary hydatid cyst resection | Completely resected pulmonary hydatid disease | Postoperative recurrence prevention | Randomized trial with planned enrollment **24**; ABZ **15 mg/kg/day** in two 15-day postoperative cycles vs placebo; primary outcome recurrence at **6 months** by imaging; includes AST/ALT safety monitoring (NCT06483880 chunk 1) | NCT06483880 (2024 record) | https://clinicaltrials.gov/study/NCT06483880 | (NCT06483880 chunk 1) |


*Table: This table summarizes evidence-based diagnostic and treatment options for cystic echinococcosis, organized by modality and WHO-IWGE cyst stage. It highlights recent quantitative performance and outcome data, plus ongoing molecular and therapeutic clinical studies.*


## Limitations of this report (evidence gaps)
- MONDO, Orphanet, and exact MeSH identifiers were not found in the retrieved full-text evidence and therefore are not asserted.
- Differential diagnosis and standardized QoL instrument outcomes were not extracted from the retrieved sources.
- Model organism details were limited in available evidence.



References

1. (akbulut2025hydatiddisease pages 6-8): S Akbulut. Hydatid Disease. Springer Nature Switzerland, Jan 2025. ISBN 9783031972775. URL: https://doi.org/10.1007/978-3-031-97277-5, doi:10.1007/978-3-031-97277-5. This article has 0 citations.

2. (akbulut2025hydatiddisease pages 8-11): S Akbulut. Hydatid Disease. Springer Nature Switzerland, Jan 2025. ISBN 9783031972775. URL: https://doi.org/10.1007/978-3-031-97277-5, doi:10.1007/978-3-031-97277-5. This article has 0 citations.

3. (bold2024thediagnosticchallenge pages 1-2): Bolor Bold, Christian Schindler, Uranshagai Narankhuu, Agiimaa Shagj, Erdenebileg Bavuujav, Sonin Sodov, Tsogbadrakh Nyamdorj, and Jakob Zinsstag. The diagnostic challenge of cystic echinococcosis in humans: first assessment of underreporting rates in mongolia. Tropical Medicine and Infectious Disease, Jul 2024. URL: https://doi.org/10.3390/tropicalmed9070163, doi:10.3390/tropicalmed9070163. This article has 6 citations.

4. (jahan2025understandingechinococcosisa pages 3-7): Nusrat Jahan, Priyanka Barua, Shahela Alam, Tamanna Akter, and Hamida Khanum. Understanding echinococcosis: a review of its epidemiological outlook. Bangladesh Journal of Zoology, 53:3-18, Jun 2025. URL: https://doi.org/10.3329/bjz.v53i1.82673, doi:10.3329/bjz.v53i1.82673. This article has 1 citations.

5. (bold2024thediagnosticchallenge pages 2-4): Bolor Bold, Christian Schindler, Uranshagai Narankhuu, Agiimaa Shagj, Erdenebileg Bavuujav, Sonin Sodov, Tsogbadrakh Nyamdorj, and Jakob Zinsstag. The diagnostic challenge of cystic echinococcosis in humans: first assessment of underreporting rates in mongolia. Tropical Medicine and Infectious Disease, Jul 2024. URL: https://doi.org/10.3390/tropicalmed9070163, doi:10.3390/tropicalmed9070163. This article has 6 citations.

6. (akbulut2025hydatiddisease pages 11-13): S Akbulut. Hydatid Disease. Springer Nature Switzerland, Jan 2025. ISBN 9783031972775. URL: https://doi.org/10.1007/978-3-031-97277-5, doi:10.1007/978-3-031-97277-5. This article has 0 citations.

7. (bold2024thediagnosticchallenge pages 5-7): Bolor Bold, Christian Schindler, Uranshagai Narankhuu, Agiimaa Shagj, Erdenebileg Bavuujav, Sonin Sodov, Tsogbadrakh Nyamdorj, and Jakob Zinsstag. The diagnostic challenge of cystic echinococcosis in humans: first assessment of underreporting rates in mongolia. Tropical Medicine and Infectious Disease, Jul 2024. URL: https://doi.org/10.3390/tropicalmed9070163, doi:10.3390/tropicalmed9070163. This article has 6 citations.

8. (hogea2024cysticechinococcosisin pages 6-7): Mihai-Octav Hogea, Bogdan-Florin Ciomaga, Mădălina-Maria Muntean, Andrei-Alexandru Muntean, Mircea Ioan Popa, and Gabriela Loredana Popa. Cystic echinococcosis in the early 2020s: a review. Tropical Medicine and Infectious Disease, 9:36, Jan 2024. URL: https://doi.org/10.3390/tropicalmed9020036, doi:10.3390/tropicalmed9020036. This article has 74 citations.

9. (jahan2025understandingechinococcosisa pages 7-10): Nusrat Jahan, Priyanka Barua, Shahela Alam, Tamanna Akter, and Hamida Khanum. Understanding echinococcosis: a review of its epidemiological outlook. Bangladesh Journal of Zoology, 53:3-18, Jun 2025. URL: https://doi.org/10.3329/bjz.v53i1.82673, doi:10.3329/bjz.v53i1.82673. This article has 1 citations.

10. (tenzin2024theburdenand pages 2-3): Chador Tenzin, Tashi Dendup, P. R. Torgerson, Peter Deplazes, Sonam Zangmo, Chador Wangmo, Tsheten Tsheten, and Tandin Zangpo. The burden and distribution of cystic echinococcosis in bhutan: a retrospective study. Parasitology, pages 1-9, Nov 2024. URL: https://doi.org/10.1017/s0031182024001069, doi:10.1017/s0031182024001069. This article has 1 citations and is from a peer-reviewed journal.

11. (tenzin2024theburdenand pages 1-2): Chador Tenzin, Tashi Dendup, P. R. Torgerson, Peter Deplazes, Sonam Zangmo, Chador Wangmo, Tsheten Tsheten, and Tandin Zangpo. The burden and distribution of cystic echinococcosis in bhutan: a retrospective study. Parasitology, pages 1-9, Nov 2024. URL: https://doi.org/10.1017/s0031182024001069, doi:10.1017/s0031182024001069. This article has 1 citations and is from a peer-reviewed journal.

12. (tenzin2024theburdenand pages 4-5): Chador Tenzin, Tashi Dendup, P. R. Torgerson, Peter Deplazes, Sonam Zangmo, Chador Wangmo, Tsheten Tsheten, and Tandin Zangpo. The burden and distribution of cystic echinococcosis in bhutan: a retrospective study. Parasitology, pages 1-9, Nov 2024. URL: https://doi.org/10.1017/s0031182024001069, doi:10.1017/s0031182024001069. This article has 1 citations and is from a peer-reviewed journal.

13. (mehdi2025designandevaluation pages 8-9): Abolfazl Masoumi Koushk Mehdi, H. Motedayyen, M. Fasihi Harandi, Hossein Akbari, Amin Moradi Hasan-Abad, and Mohsen Arbabi. Design and evaluation of a novel direct hemagglutination test based on a recombinant protein for diagnosis of cystic echinococcosis. Parasites & Vectors, Jul 2025. URL: https://doi.org/10.1186/s13071-025-06900-1, doi:10.1186/s13071-025-06900-1. This article has 1 citations and is from a peer-reviewed journal.

14. (petrone2024evaluationofthe pages 1-2): Linda Petrone, Saeid Najafi-Fard, Laura Falasca, Settimia Sbarra, Antonella Teggi, Emanuele Nicastri, Lucia Rosalba Grillo, Mirco Burocchi, Giuseppe Maria Ettorre, Alessandra Ludovisi, Daniele Colombo, Franca Del Nonno, and Delia Goletti. Evaluation of the local and peripheral immune responses in patients with cystic echinococcosis. Pathogens, 13:477, Jun 2024. URL: https://doi.org/10.3390/pathogens13060477, doi:10.3390/pathogens13060477. This article has 2 citations.

15. (petrone2024evaluationofthe pages 7-9): Linda Petrone, Saeid Najafi-Fard, Laura Falasca, Settimia Sbarra, Antonella Teggi, Emanuele Nicastri, Lucia Rosalba Grillo, Mirco Burocchi, Giuseppe Maria Ettorre, Alessandra Ludovisi, Daniele Colombo, Franca Del Nonno, and Delia Goletti. Evaluation of the local and peripheral immune responses in patients with cystic echinococcosis. Pathogens, 13:477, Jun 2024. URL: https://doi.org/10.3390/pathogens13060477, doi:10.3390/pathogens13060477. This article has 2 citations.

16. (tian2024globalregionaland pages 1-2): Tian Tian, Liyuan Miao, Wei Wang, and Xiaonong Zhou. Global, regional and national burden of human cystic echinococcosis from 1990 to 2019: a systematic analysis for the global burden of disease study 2019. Tropical Medicine and Infectious Disease, 9:87, Apr 2024. URL: https://doi.org/10.3390/tropicalmed9040087, doi:10.3390/tropicalmed9040087. This article has 29 citations.

17. (tenzin2024theburdenand pages 3-3): Chador Tenzin, Tashi Dendup, P. R. Torgerson, Peter Deplazes, Sonam Zangmo, Chador Wangmo, Tsheten Tsheten, and Tandin Zangpo. The burden and distribution of cystic echinococcosis in bhutan: a retrospective study. Parasitology, pages 1-9, Nov 2024. URL: https://doi.org/10.1017/s0031182024001069, doi:10.1017/s0031182024001069. This article has 1 citations and is from a peer-reviewed journal.

18. (erganis2024comparisonofmethods pages 4-6): Sidre Erganis, Fakhriddin Sarzhanov, Funda Doğruman Al, and Kayhan Cağlar. Comparison of methods in the serologic diagnosis of cystic echinococcosis. Acta Parasitologica, 69:1122-1131, Mar 2024. URL: https://doi.org/10.1007/s11686-024-00840-z, doi:10.1007/s11686-024-00840-z. This article has 18 citations and is from a peer-reviewed journal.

19. (bold2024thediagnosticchallenge pages 7-8): Bolor Bold, Christian Schindler, Uranshagai Narankhuu, Agiimaa Shagj, Erdenebileg Bavuujav, Sonin Sodov, Tsogbadrakh Nyamdorj, and Jakob Zinsstag. The diagnostic challenge of cystic echinococcosis in humans: first assessment of underreporting rates in mongolia. Tropical Medicine and Infectious Disease, Jul 2024. URL: https://doi.org/10.3390/tropicalmed9070163, doi:10.3390/tropicalmed9070163. This article has 6 citations.

20. (NCT05824442 chunk 1):  Evaluation of a New Multiplex Quantitative PCR Technique for the Diagnosis of Echinococcosis. Centre Hospitalier Universitaire de Besancon. 2023. ClinicalTrials.gov Identifier: NCT05824442

21. (NCT05769790 chunk 1):  Droplet-digital PCR for the Detection of Circulating Cell-free DNA in Patients With Cystic Echinococcosis: an Exploratory Study. IRCCS Sacro Cuore Don Calabria di Negrar. 2022. ClinicalTrials.gov Identifier: NCT05769790

22. (akhan2025theroleof pages 2-4): Okan Akhan and Turkmen Ciftci. The role of interventional radiology for the treatment of liver ce and ae lesions: current concepts. Visceral Medicine, pages 1-22, Jul 2025. URL: https://doi.org/10.1159/000547623, doi:10.1159/000547623. This article has 1 citations and is from a peer-reviewed journal.

23. (akhan2025theroleof pages 6-8): Okan Akhan and Turkmen Ciftci. The role of interventional radiology for the treatment of liver ce and ae lesions: current concepts. Visceral Medicine, pages 1-22, Jul 2025. URL: https://doi.org/10.1159/000547623, doi:10.1159/000547623. This article has 1 citations and is from a peer-reviewed journal.

24. (rosa2024followupstudy pages 1-2): Daniel Da Rosa, Elisa Figueredo, Michel Rosas, and Fernando Goñi. Follow up study of symptomatic human cystic echinococcosis treatment with albendazole and praziquantel, in uruguay. BMC Infectious Diseases, Jul 2024. URL: https://doi.org/10.1186/s12879-024-09539-y, doi:10.1186/s12879-024-09539-y. This article has 8 citations and is from a peer-reviewed journal.

25. (akhan2025theroleof media 3452c1f5): Okan Akhan and Turkmen Ciftci. The role of interventional radiology for the treatment of liver ce and ae lesions: current concepts. Visceral Medicine, pages 1-22, Jul 2025. URL: https://doi.org/10.1159/000547623, doi:10.1159/000547623. This article has 1 citations and is from a peer-reviewed journal.

26. (NCT06483880 chunk 1):  The Role of Adjuvant Albendazole After Pulmonary Hydatid Cyst Resection. Ain Shams University. 2024. ClinicalTrials.gov Identifier: NCT06483880

27. (NCT01643018 chunk 1): Mehmet Kaplan. Laparoscopic Versus Open Surgery for the Management of Cystic Echinococcosis of the Liver. Medical Park Gaziantep Hospital. 2006. ClinicalTrials.gov Identifier: NCT01643018

28. (akhan2025theroleof pages 4-6): Okan Akhan and Turkmen Ciftci. The role of interventional radiology for the treatment of liver ce and ae lesions: current concepts. Visceral Medicine, pages 1-22, Jul 2025. URL: https://doi.org/10.1159/000547623, doi:10.1159/000547623. This article has 1 citations and is from a peer-reviewed journal.

29. (petrone2024evaluationofthe pages 2-3): Linda Petrone, Saeid Najafi-Fard, Laura Falasca, Settimia Sbarra, Antonella Teggi, Emanuele Nicastri, Lucia Rosalba Grillo, Mirco Burocchi, Giuseppe Maria Ettorre, Alessandra Ludovisi, Daniele Colombo, Franca Del Nonno, and Delia Goletti. Evaluation of the local and peripheral immune responses in patients with cystic echinococcosis. Pathogens, 13:477, Jun 2024. URL: https://doi.org/10.3390/pathogens13060477, doi:10.3390/pathogens13060477. This article has 2 citations.

30. (hogea2024cysticechinococcosisin pages 16-17): Mihai-Octav Hogea, Bogdan-Florin Ciomaga, Mădălina-Maria Muntean, Andrei-Alexandru Muntean, Mircea Ioan Popa, and Gabriela Loredana Popa. Cystic echinococcosis in the early 2020s: a review. Tropical Medicine and Infectious Disease, 9:36, Jan 2024. URL: https://doi.org/10.3390/tropicalmed9020036, doi:10.3390/tropicalmed9020036. This article has 74 citations.

31. (erganis2024comparisonofmethods pages 1-2): Sidre Erganis, Fakhriddin Sarzhanov, Funda Doğruman Al, and Kayhan Cağlar. Comparison of methods in the serologic diagnosis of cystic echinococcosis. Acta Parasitologica, 69:1122-1131, Mar 2024. URL: https://doi.org/10.1007/s11686-024-00840-z, doi:10.1007/s11686-024-00840-z. This article has 18 citations and is from a peer-reviewed journal.

32. (erganis2024comparisonofmethods pages 6-8): Sidre Erganis, Fakhriddin Sarzhanov, Funda Doğruman Al, and Kayhan Cağlar. Comparison of methods in the serologic diagnosis of cystic echinococcosis. Acta Parasitologica, 69:1122-1131, Mar 2024. URL: https://doi.org/10.1007/s11686-024-00840-z, doi:10.1007/s11686-024-00840-z. This article has 18 citations and is from a peer-reviewed journal.

33. (akhan2025theroleof pages 1-2): Okan Akhan and Turkmen Ciftci. The role of interventional radiology for the treatment of liver ce and ae lesions: current concepts. Visceral Medicine, pages 1-22, Jul 2025. URL: https://doi.org/10.1159/000547623, doi:10.1159/000547623. This article has 1 citations and is from a peer-reviewed journal.
