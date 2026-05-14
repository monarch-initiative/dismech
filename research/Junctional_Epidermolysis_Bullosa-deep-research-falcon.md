---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T09:36:41.614874'
end_time: '2026-05-09T09:51:08.047179'
duration_seconds: 866.43
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Junctional Epidermolysis Bullosa
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 52
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Junctional Epidermolysis Bullosa
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Junctional Epidermolysis Bullosa** covering all of the
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
- **Disease Name:** Junctional Epidermolysis Bullosa
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Junctional Epidermolysis Bullosa** covering all of the
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


## Comprehensive Disease Characteristics Report: Junctional Epidermolysis Bullosa (JEB)

**Target disease:** Junctional Epidermolysis Bullosa (Mendelian genodermatosis)
**MONDO ID:** **MONDO_0017612** (Open Targets/Monarch disease ontology listing) (OpenTargets Search: Junctional epidermolysis bullosa)

### Executive summary (current understanding)
Junctional epidermolysis bullosa (JEB) is a rare, typically **autosomal recessive** inherited epidermolysis bullosa subtype characterized by **skin and mucosal fragility** with tissue separation at the **lamina lucida** of the basement membrane zone, leading to blistering/erosions after minimal trauma and multisystem complications. JEB is most often caused by biallelic pathogenic variants affecting **laminin-332** (LAMA3, LAMB3, LAMC2), **type XVII collagen** (COL17A1), or **integrin α6β4** (ITGA6, ITGB4), with rarer involvement of **ITGA3**. Severity ranges from **generalized severe (formerly Herlitz)**—often fatal in infancy—to **generalized intermediate (formerly non-Herlitz)** with survival into adulthood but substantial morbidity. Recent work (2024–2025) has advanced **genotype–phenotype severity correlations**, clarified the diagnostic role of **genome sequencing for deep intronic variants**, and expanded gene/cell therapy concepts beyond skin to **airway epithelium**. (keith2020leadingedgeemerging pages 1-6, wen2024genotype–phenotypecorrelationin pages 13-17, wen2024genotype–phenotypecorrelationin pages 17-22, chen2025identificationofdeep pages 1-2, lau2024lentiviralexpressionof pages 1-2)

---

## 1. Disease Information

### 1.1 What is the disease?
JEB is an EB subtype defined by cleavage within the **lamina lucida** at the epithelial–subepithelial junction, producing mucocutaneous blistering and erosions. It is a **rare autosomal recessive genodermatosis** with broad phenotypic variability and systemic involvement (e.g., gastrointestinal, renal, respiratory). (keith2020leadingedgeemerging pages 1-6, wen2024genotype–phenotypecorrelationin pages 13-17, wen2024genotype–phenotypecorrelationin pages 17-22)

### 1.2 Key identifiers (available in retrieved evidence)
- **MONDO:** **MONDO_0017612** (junctional epidermolysis bullosa) (OpenTargets Search: Junctional epidermolysis bullosa)
- Related MONDO terms listed in the same ontology context:
  - **JEB, non-Herlitz type:** MONDO_0009180 (OpenTargets Search: Junctional epidermolysis bullosa)
  - **JEB, Herlitz type:** MONDO_0009182 (OpenTargets Search: Junctional epidermolysis bullosa)
  - **JEB with pyloric atresia:** MONDO_0009183 (OpenTargets Search: Junctional epidermolysis bullosa)

**Not retrieved in this tool run (evidence unavailable here):** OMIM numbers, Orphanet IDs, ICD-10/ICD-11 codes, MeSH IDs. (No citeable context in this run.)

### 1.3 Synonyms / alternative names (from retrieved evidence)
- **Generalized severe JEB** ≈ **Herlitz JEB** (historical terminology) (keith2020leadingedgeemerging pages 1-6, wen2024genotype–phenotypecorrelationin pages 13-17, bischof2024emerginggenetherapeutics pages 1-2)
- **Generalized intermediate JEB** ≈ **non-Herlitz JEB** (keith2020leadingedgeemerging pages 1-6, wen2024genotype–phenotypecorrelationin pages 13-17)
- **Laryngo-onycho-cutaneous syndrome (LOC)** is described as a rare JEB variant associated with LAMA3 (laminin-332 α3) involvement and airway manifestations. (wen2024genotype–phenotypecorrelationin pages 13-17, lau2024lentiviralexpressionof pages 1-2)

### 1.4 Evidence source type
This report is based on **aggregated disease-level resources and peer-reviewed literature** (reviews, cohort studies, registry epidemiology, guidelines), supplemented by **clinical trial registry entries** (ClinicalTrials.gov). (wen2024genotype–phenotypecorrelationin pages 13-17, chen2025identificationofdeep pages 1-2, NCT03526159 chunk 1)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** inherited pathogenic variants in genes encoding proteins required for dermal–epidermal adhesion at the basement membrane zone, producing defective adhesion and tissue cleavage in the lamina lucida. (keith2020leadingedgeemerging pages 1-6, wen2024genotype–phenotypecorrelationin pages 13-17, wen2024genotype–phenotypecorrelationin pages 17-22)

### 2.2 Risk factors
- **Genetic (causal) risk:** biallelic pathogenic variants in core JEB genes (below). (wen2024genotype–phenotypecorrelationin pages 13-17, wen2024genotype–phenotypecorrelationin pages 17-22)
- **Consanguinity:** a contributor to higher prevalence of congenital EB in some regions; Russian registry reported high prevalence in Dagestan and noted high consanguineous marriage rates (50%). (murashkin2024congenitalepidermolysisbullosa pages 2-3, murashkin2024congenitalepidermolysisbullosa pages 1-2)

**Environmental risk factors** as causes of JEB are not applicable (monogenic disease); environmental exposures mainly influence **complications** (wound infection, trauma). (keith2020leadingedgeemerging pages 1-6)

### 2.3 Protective factors
No established genetic or environmental protective factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
Not specifically addressed in the retrieved evidence; clinically, mechanical trauma and infection interact with genetic skin fragility to drive lesion burden. (keith2020leadingedgeemerging pages 1-6)

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum (with HPO suggestions)
Commonly reported features include:
- **Skin and mucosal blistering/erosions** after minor trauma; chronic wounds (HPO: *Skin blistering*; *Erosions*) (keith2020leadingedgeemerging pages 1-6, wen2024genotype–phenotypecorrelationin pages 13-17)
- **Nail dystrophy / anonychia** (HPO: *Nail dystrophy*, *Anonychia*) (wen2024genotype–phenotypecorrelationin pages 13-17, murashkin2024congenitalepidermolysisbullosa pages 1-2)
- **Enamel defects** (HPO: *Enamel hypoplasia*) (wen2024genotype–phenotypecorrelationin pages 13-17)
- **Scarring / alopecia** (HPO: *Scarring*, *Alopecia*) (wen2024genotype–phenotypecorrelationin pages 13-17)
- **Airway/laryngeal involvement** (laryngotracheal stenosis, airway obstruction) (HPO: *Laryngeal stenosis*, *Tracheal stenosis*, *Respiratory distress*) (lau2024lentiviralexpressionof pages 1-2, lau2024lentiviralexpressionof pages 2-4)
- **Ocular involvement** (HPO: *Eye irritation/erosion*—non-quantified here) (wen2024genotype–phenotypecorrelationin pages 13-17)
- **Anemia, failure to thrive, sepsis risk** (HPO: *Anemia*, *Failure to thrive*, *Sepsis*) (wen2024genotype–phenotypecorrelationin pages 13-17, murashkin2024congenitalepidermolysisbullosa pages 1-2)

### 3.2 Phenotype characteristics (onset, severity, progression)
- **Onset:** typically congenital/neonatal or early infancy (widespread blistering and erosions). (wen2024genotype–phenotypecorrelationin pages 13-17, murashkin2024congenitalepidermolysisbullosa pages 1-2)
- **Severe JEB (Herlitz/generalized severe):** often fatal in early childhood, with mortality linked to **sepsis, dehydration, airway obstruction, metabolic disturbances**. (wen2024genotype–phenotypecorrelationin pages 13-17, bischof2024emerginggenetherapeutics pages 1-2)
- **Intermediate JEB:** survival into adulthood, heterogeneous course with chronic wounds and extracutaneous involvement. (wen2024genotype–phenotypecorrelationin pages 13-17)

### 3.3 Quality of life impact
QoL instruments/statistics specific to JEB were not retrieved in the available evidence; however, airway-involved EB patients experience high morbidity and require repeated airway procedures. (lau2024lentiviralexpressionof pages 1-2, lau2024lentiviralexpressionof pages 2-4)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes (human)
From a 2024 genotype–phenotype study and ontology evidence, JEB is caused by pathogenic variants in:
- **LAMA3, LAMB3, LAMC2** (laminin-332 chains)
- **COL17A1** (type XVII collagen)
- **ITGA6, ITGB4** (integrin α6β4)
- **ITGA3** (integrin α3)
(wen2024genotype–phenotypecorrelationin pages 13-17, wen2024genotype–phenotypecorrelationin pages 17-22, OpenTargets Search: Junctional epidermolysis bullosa)

### 4.2 Variant classes and functional consequences
Common variant types include **nonsense, frameshift, splice-site, deletions, and missense** variants. (wen2024genotype–phenotypecorrelationin pages 17-22)

**Genotype–phenotype correlation (severity):**
- **Biallelic premature termination codon (PTC) / loss-of-function variants** in laminin-332 genes often lead to **severe JEB** due to nonsense-mediated decay and absent laminin-332 staining. (wen2024genotype–phenotypecorrelationin pages 17-22)
- Non–loss-of-function alleles (missense/in-frame changes/exon skipping) can preserve partial protein; **~5–10% residual laminin-332** may meaningfully ameliorate severity. (wen2024genotype–phenotypecorrelationin pages 17-22)

### 4.3 Modifier genes
Mouse-model genetic evidence supports strong **modifier effects**:
- **Col17a1** identified as a **major genetic modifier** of Lamc2 hypomorphic JEB severity in mice; 1–3 amino-acid differences in the NC4 domain of collagen XVII altered dermal–epidermal adhesion and disease severity. (Sproule et al., 2014; https://doi.org/10.1371/journal.pgen.1004068) (sproule2014molecularidentificationof pages 1-2)
- Additional modifier loci/QTL reported in Lamc2jeb mice include intervals containing **Dst-e/Bpag1-e** and candidate metabolic/nuclear receptor pathways (Ppargc1a, Pparg, Igf1). (Sproule et al., 2023; https://doi.org/10.1371/journal.pone.0288263) (sproule2023sevennaturallyvariant pages 1-2)

### 4.4 Deep intronic variants and diagnostic “missing heritability”
A 2025 study highlights that exome sequencing can miss causative alleles:
- Among **69 recessive JEB cases**, **13.0%** remained genetically undiagnosed after initial exome sequencing; among COL17A1-associated cases, unresolved proportion reached **31.6%**. (Chen et al., 2025; https://doi.org/10.1038/s41525-025-00466-8) (chen2025identificationofdeep pages 1-2)
- Deep intronic variants identified: **COL17A1 c.4156+117G>A, c.2039-104G>A, c.1267+237dupC** and **LAMB3 c.-38+2T>C** in six cases; splicing assays showed exon skipping/pseudoexon insertion **in HaCaT cells** but not HEK293, emphasizing cell-context dependence of transcript assays. (chen2025identificationofdeep pages 1-2)

---

## 5. Environmental Information
JEB is monogenic; no specific toxins/lifestyle/infectious agents were identified as causes. Environmental factors (mechanical trauma, wound colonization/infection) act as downstream exacerbators of disease burden and complications. (keith2020leadingedgeemerging pages 1-6)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (molecular → clinical)
1. **Biallelic pathogenic variants** in laminin-332 / COL17A1 / integrin genes reduce/abolish functional adhesion complexes at the basement membrane zone. (keith2020leadingedgeemerging pages 1-6, wen2024genotype–phenotypecorrelationin pages 17-22)
2. **Defective hemidesmosomes / dermal–epidermal adhesion** at the lamina lucida causes mechanical fragility. (keith2020leadingedgeemerging pages 1-6, NCT03526159 chunk 1)
3. Minimal trauma leads to **blistering and erosions**, evolving into chronic wounds. (keith2020leadingedgeemerging pages 1-6, wen2024genotype–phenotypecorrelationin pages 13-17)
4. Chronic wounds promote **inflammation**, infection risk, fluid/protein loss, and systemic complications including failure to thrive, anemia, and sepsis. (wen2024genotype–phenotypecorrelationin pages 13-17, murashkin2024congenitalepidermolysisbullosa pages 1-2)

### 6.2 Cell types and processes (ontology suggestions)
- **Key cell types (CL):** basal keratinocytes; airway epithelial basal stem cells (supported by Human Lung Cell Atlas expression context and primary basal-cell experiments). (lau2024lentiviralexpressionof pages 2-4)
- **Biological processes (GO suggestions):** cell–substrate adhesion; hemidesmosome assembly; basement membrane organization; wound healing; epithelial cell differentiation. Mechanistic relevance is supported by the central role of laminin-332 and by gene-restoration phenotypes in airway basal cells. (lau2024lentiviralexpressionof pages 1-2, lau2024lentiviralexpressionof pages 4-5)

### 6.3 Molecular profiling / advanced technologies
Direct multi-omics profiling for JEB was not retrieved in available evidence; however, Lau et al. performed RNA-seq after LAMA3A transduction in EB airway basal cells and observed **373 differentially expressed transcripts** (149 up, 224 down), consistent with broad epithelial phenotype shifts. (lau2024lentiviralexpressionof pages 4-5)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system involvement
- **Skin and mucous membranes** (primary) (UBERON: skin; mucosa) (wen2024genotype–phenotypecorrelationin pages 13-17, keith2020leadingedgeemerging pages 1-6)
- **Upper and lower airway** (larynx/trachea) in severe JEB/LOC and some intermediate cases; airway stenosis requiring endoscopic management is documented. (lau2024lentiviralexpressionof pages 1-2, lau2024lentiviralexpressionof pages 2-4)
- **Eyes** (ocular involvement) (wen2024genotype–phenotypecorrelationin pages 13-17)

### 7.2 Tissue/cell level
- Basement membrane zone of stratified epithelia; basal epithelial attachment structures are central. (keith2020leadingedgeemerging pages 1-6, wen2024genotype–phenotypecorrelationin pages 17-22)

---

## 8. Temporal Development

### 8.1 Onset
Typically at birth or in the first months of life. (murashkin2024congenitalepidermolysisbullosa pages 1-2, wen2024genotype–phenotypecorrelationin pages 13-17)

### 8.2 Progression/course
- Severe forms show rapid decline in infancy due to infections/sepsis and airway complications. (wen2024genotype–phenotypecorrelationin pages 13-17, murashkin2024congenitalepidermolysisbullosa pages 1-2)
- Chronic course in survivors includes persistent wounds and extracutaneous complications. (keith2020leadingedgeemerging pages 1-6, wen2024genotype–phenotypecorrelationin pages 13-17)

---

## 9. Inheritance and Population

### 9.1 Inheritance
JEB is primarily **autosomal recessive**. (wen2024genotype–phenotypecorrelationin pages 13-17, chandrasekaran2025cutaneoussquamouscell pages 1-2)

### 9.2 Epidemiology (statistics)
From Wen et al. (2024, J Invest Dermatol; https://doi.org/10.1016/j.jid.2023.11.021):
- Incidence ~**2.68 per million live births**
- Prevalence ~**0.49 per million** (wen2024genotype–phenotypecorrelationin pages 13-17, wen2024genotype–phenotypecorrelationin pages 17-22)

Russian pediatric registry paper (Murashkin et al., 2024; https://doi.org/10.15690/vsp.v23i5.2808; accepted 16 Oct 2024):
- **491** children with congenital EB in registry (all EB types)
- **31 (6%)** were junctional
- Registry recorded **22 deaths**, with **JEB comprising 59.1%** (13/22) and mean age at death **0.40 ± 0.22 years**
- Survival probability for JEB reportedly drops to **almost 0% in the first 100 days** (murashkin2024congenitalepidermolysisbullosa pages 2-3, murashkin2024congenitalepidermolysisbullosa pages 1-2)

Airway EB cohort (Lau et al., 2024; https://doi.org/10.1016/j.ymthe.2024.02.032):
- **16** EB patients with airway disease; **8** had died at time of writing (lau2024lentiviralexpressionof pages 2-4)

---

## 10. Diagnostics

### 10.1 Recommended diagnostic modalities (laboratory and genetic)
Wen et al. (2024) describes a combined approach:
- **Genetic testing** (Sanger, targeted NGS panels, WES/WGS)
- **Immunofluorescence mapping (IFM/antigen mapping)** to localize cleavage plane and infer missing proteins
- **Transmission electron microscopy (TEM)** for ultrastructural defects in selected cases (wen2024genotype–phenotypecorrelationin pages 13-17)

International laboratory guideline (Has et al., 2019; BJD; https://doi.org/10.1111/bjd.18128):
- Genetic testing is **“always recommended”** and should include the index case and, if possible, parents for reliable counseling.
- IFM is recommended for rapid diagnosis/prognosis and to prioritize genetics; TEM is reserved for limited inconclusive cases.
- States: **“DNA-based prenatal diagnosis is technically feasible for all EB subtypes”** and should be considered upon family request/national regulations. (has2019clinicalpracticeguidelines pages 1-2, has2019clinicalpracticeguidelines pages 2-3)

### 10.2 Diagnostic yield improvements (WGS + splicing assays)
Genome sequencing can identify deep intronic alleles missed by exome; splicing assays require a relevant cell model (HaCaT vs HEK293) (chen2025identificationofdeep pages 1-2).

### 10.3 Differential diagnosis
Not comprehensively retrievable from the provided evidence in this run.

---

## 11. Outcome / Prognosis

### 11.1 Mortality and survival
- Severe JEB is often fatal in early childhood; one recent review states severe JEB is generally lethal within **6–24 months** and that ~70% of JEB cases are associated with LAMB3 mutations (review context). (bischof2024emerginggenetherapeutics pages 1-2)
- Registry data demonstrate very high early mortality for JEB within the first months of life (Murashkin et al., 2024). (murashkin2024congenitalepidermolysisbullosa pages 1-2)

### 11.2 Prognostic factors
Severity correlates with degree of residual protein (e.g., laminin-332) and mutation type (biallelic PTC/LoF vs residual expression). (wen2024genotype–phenotypecorrelationin pages 17-22)

---

## 12. Treatment

### 12.1 Standard-of-care (current real-world implementation)
Supportive multidisciplinary care remains foundational, including wound care, infection control, and systemic support (nutrition, pain management), as emphasized in both JEB-focused and EB-wide reviews. (keith2020leadingedgeemerging pages 1-6, danescu2024treatmentofepidermolysis pages 1-4)

### 12.2 Recently approved/marketed therapies (context)
A 2024 review notes that **“the first drugs for the treatment of EB wounds in dystrophic and junctional EB have recently achieved US FDA and EMA approval”** but does not specify product names in the excerpt. It also notes B-VEC licensing approval on May 19, 2023 for dystrophic EB as a milestone of in vivo gene therapy reaching clinical application. (Danescu et al., published online Aug 2, 2024; https://doi.org/10.1007/s13555-024-01227-8) (danescu2024treatmentofepidermolysis pages 1-4, danescu2024treatmentofepidermolysis pages 4-5)

### 12.3 Advanced therapeutics (gene/cell/RNA)

**Ex vivo gene therapy for LAMB3-related JEB (skin):**
- Danescu et al. describes de Luca group’s “groundbreaking” life-saving transplantation of transgenic keratinocytes (80% TBSA) in intermediate JEB with LAMB3 mutations and notes that 5-year follow-up showed genetically repaired stem cells continued to regenerate near-normal epidermis. (danescu2024treatmentofepidermolysis pages 4-5)
- A formal phase II/III protocol (Hologene 5; EudraCT 2018-000261-36; https://doi.org/10.3389/fgene.2021.705019) describes autologous keratinocytes corrected with γ-retroviral LAMB3 cDNA on fibrin support with 12-month efficacy endpoints and 15-year follow-up. (rosa2021hologene5a pages 1-2)

**Nonsense suppression (gentamicin readthrough):**
- ClinicalTrials.gov pilot study: **NCT03526159** (first posted 2018-05-16; last update posted 2020-04-07) evaluates topical (0.5% ointment BID ×14 days) and IV (7.5 mg/kg daily ×14 days) gentamicin in JEB patients with LAMB3 nonsense mutations; primary endpoints include laminin-332 immunofluorescence and EM hemidesmosomes; safety monitoring includes ototoxicity/nephrotoxicity and anti-laminin-332 antibodies. URL: https://clinicaltrials.gov/study/NCT03526159 (NCT03526159 chunk 1)
- Optimization study: **NCT04140786** (first posted 2019-10-28; last update posted 2022-11-03) tests IV gentamicin 10 mg/kg regimens and includes EB Disease Activity and Scarring Index (EBDASI) outcomes. URL: https://clinicaltrials.gov/study/NCT04140786 (NCT04140786 chunk 1)

**Airway-directed combined cell/gene therapy proof-of-concept (2024):**
- Lau et al. (Molecular Therapy; accepted 27 Feb 2024; https://doi.org/10.1016/j.ymthe.2024.02.032) report airway disease in EB and show in vitro rescue of EB patient-derived airway basal cells by lentiviral **LAMA3A** expression. LAMA3 variants were found in **10/15** genotyped airway EB patients; basal cells showed adhesion defects. After transduction, LAMA3 mRNA increased **45.5-fold** and **79.6-fold** in two independent cultures; ALI cultures showed TEER within normal range (>250 Ω) and ciliary beat frequency within expected non-EB range (7–16 Hz); adhesion restored to near control. (lau2024lentiviralexpressionof pages 4-5, lau2024lentiviralexpressionof pages 1-2, lau2024lentiviralexpressionof pages 2-4)

### 12.4 MAXO suggestions (treatment action ontology; illustrative)
- **Wound care / dressing management** (supportive wound management) (keith2020leadingedgeemerging pages 1-6)
- **Infection prophylaxis/treatment** (topical/systemic antimicrobial therapy) (keith2020leadingedgeemerging pages 1-6)
- **Ex vivo gene therapy / autologous gene-corrected epidermal grafting** (rosa2021hologene5a pages 1-2, danescu2024treatmentofepidermolysis pages 4-5)
- **Aminoglycoside nonsense suppression therapy (gentamicin)** (NCT03526159 chunk 1, NCT04140786 chunk 1)

---

## 13. Prevention

### 13.1 Primary prevention
For Mendelian JEB, primary prevention focuses on **reproductive options**:
- Has et al. (2019 guideline) states accurate EB diagnosis enables informed genetic counseling and prenatal/PGT options and that **“DNA-based prenatal diagnosis is technically feasible for all EB subtypes”**; prenatal diagnosis requires a known familial mutation. (has2019clinicalpracticeguidelines pages 1-2, has2019clinicalpracticeguidelines pages 2-3)

### 13.2 Secondary/tertiary prevention
- Avoiding skin trauma, meticulous wound care, and infection control reduce complications (sepsis) and improve outcomes. (keith2020leadingedgeemerging pages 1-6, murashkin2024congenitalepidermolysisbullosa pages 1-2)

---

## 14. Other Species / Natural Disease
Naturally occurring JEB has been reported in multiple domestic species and can inform genotype–phenotype correlations.
- **Cats (COL17A1):** Two unrelated cats with homozygous COL17A1 splice(-region) variants showed marked severity differences; transcript analysis demonstrated residual wildtype splicing in the milder case, supporting a molecular basis for severity variation. (Genes, 2023; https://doi.org/10.3390/genes14101835) (natsuga2010animalmodelsof pages 1-2)
- **Dogs (LAMA3):** A litter with severe mucocutaneous ulcers and upper airway obstruction had a novel LAMA3 missense variant with AR inheritance; EM confirmed lamina-lucida splitting. (Vet Dermatol, 2021; https://doi.org/10.1111/vde.12972) (not extracted as evidence snippet in gather_evidence, but paper is in state; no citeable context id provided beyond tool results)

**Note:** dog/horse/cat models are also referenced in EB animal-model reviews. (natsuga2010animalmodelsof pages 1-2)

---

## 15. Model Organisms
- A 2010 review reports **12 JEB animal models** and lists multiple gene KO/hypomorphic models; most are perinatally lethal. The authors’ **Col17a1 KO mouse** survived ~12 months, with ~**20%** showing long survival enabling therapy experiments; transgenic rescue with human COL17A1 cDNA restored normal skin and fertility. (Dermatol Clin, 2010; https://doi.org/10.1016/j.det.2009.10.016) (natsuga2010animalmodelsof pages 1-2)
- **Mouse modifier models:** Lamc2jeb hypomorphic JEB model used to map modifiers including Col17a1 and additional QTL, demonstrating strong epistasis and potential therapeutic modifier pathways. (sproule2014molecularidentificationof pages 1-2, sproule2023sevennaturallyvariant pages 1-2)

---

## Recent developments (prioritizing 2023–2025 evidence retrieved here)
1. **Genotype–phenotype “signposts to severity” (2024):** detailed correlation between LoF/PTC alleles and severe disease; residual laminin-332 (~5–10%) associated with milder/intermediate disease. (Wen et al., 2024; https://doi.org/10.1016/j.jid.2023.11.021) (wen2024genotype–phenotypecorrelationin pages 17-22)
2. **Airway gene therapy concepts (2024):** first detailed pediatric airway cohort + in vitro LAMA3A lentiviral functional correction in airway basal cells, expanding the therapeutic target tissue beyond skin. (Lau et al., 2024; https://doi.org/10.1016/j.ymthe.2024.02.032) (lau2024lentiviralexpressionof pages 4-5, lau2024lentiviralexpressionof pages 1-2, lau2024lentiviralexpressionof pages 2-4)
3. **Genome sequencing resolves ES-negative JEB (2025):** deep intronic COL17A1/LAMB3 variants and cell-type–specific splicing assay considerations. (Chen et al., 2025; https://doi.org/10.1038/s41525-025-00466-8) (chen2025identificationofdeep pages 1-2)

---

## Evidence gaps in this tool run (explicit)
- OMIM, Orphanet, ICD-10/ICD-11, and MeSH identifiers were not available in retrieved citeable evidence.
- Detailed differential diagnosis tables and validated QoL statistics/instruments specific to JEB were not retrieved.
- Human protective factors and gene–environment interaction datasets were not retrieved.

---

### Structured summary table

| Topic | Key details |
|---|---|
| Disease / identifiers | **Junctional epidermolysis bullosa (JEB)**; MONDO: **MONDO_0017612**. Open Targets also lists related subtype MONDO terms including **JEB, non-Herlitz type (MONDO_0009180)**, **JEB Herlitz type (MONDO_0009182)**, and **JEB with pyloric atresia (MONDO_0009183)**. OMIM identifiers are not directly provided in the extracted evidence here. Disease is defined as an EB subtype with tissue cleavage in the **lamina lucida** / epithelial-subepithelial junction, usually inherited as **autosomal recessive** (https://platform.opentargets.org/disease/MONDO_0017612; 2026 access context) (OpenTargets Search: Junctional epidermolysis bullosa, wen2024genotype–phenotypecorrelationin pages 13-17, wen2024genotype–phenotypecorrelationin pages 17-22) |
| Main causal genes | Core JEB genes repeatedly identified across recent evidence: **LAMA3, LAMB3, LAMC2** (laminin-332 chains), **COL17A1** (type XVII collagen), **ITGA6, ITGB4** (integrin α6β4), and **ITGA3**. Open Targets disease-target evidence supports these as the principal disease-associated genes for JEB (https://platform.opentargets.org/disease/MONDO_0017612; context accessed 2026) (OpenTargets Search: Junctional epidermolysis bullosa, wen2024genotype–phenotypecorrelationin pages 13-17, wen2024genotype–phenotypecorrelationin pages 17-22) |
| Inheritance / molecular basis | JEB is described as a **rare autosomal recessive genodermatosis** caused by loss or dysfunction of proteins required for dermal-epidermal adhesion. Laminin-332 deficiency, type XVII collagen deficiency, or integrin α6β4 dysfunction are major molecular categories (Wen et al., *J Invest Dermatol*, published Jun 2024, https://doi.org/10.1016/j.jid.2023.11.021; Keith et al., Mar 2020, https://doi.org/10.1080/14712598.2020.1740678) (keith2020leadingedgeemerging pages 1-6, wen2024genotype–phenotypecorrelationin pages 13-17, wen2024genotype–phenotypecorrelationin pages 17-22) |
| Subtypes / severity correlation | Recent literature distinguishes **severe/generalized severe (formerly Herlitz)** versus **intermediate/generalized intermediate (formerly non-Herlitz)** JEB. **Biallelic premature termination codon / loss-of-function variants** in laminin-332 genes usually correlate with **severe JEB**, often with absent laminin-332 staining and early lethality; **missense, splice-altering, in-frame, or exon-skipping alleles with residual protein expression (~5–10%)** more often correlate with **intermediate/milder disease**. Severe JEB is often fatal in infancy/early childhood; intermediate JEB can survive into adulthood but remains multisystemic (Wen et al., Jun 2024, https://doi.org/10.1016/j.jid.2023.11.021; Bischof et al., Feb 2024, https://doi.org/10.3390/ijms25042243) (wen2024genotype–phenotypecorrelationin pages 13-17, wen2024genotype–phenotypecorrelationin pages 17-22, bischof2024emerginggenetherapeutics pages 1-2) |
| Clinical phenotype highlights | Typical manifestations include **widespread skin and mucosal blistering/erosions**, **chronic wounds**, **nail dystrophy/anonychia**, **enamel defects**, **scarring**, **alopecia**, **airway/laryngeal involvement**, **ocular involvement**, **anemia**, and in severe forms **failure to thrive, sepsis, and airway obstruction**. Airway disease is especially linked to **LAMA3-associated JEB severe / LOC-like disease** (Wen et al., Jun 2024, https://doi.org/10.1016/j.jid.2023.11.021; Lau et al., May 2024, https://doi.org/10.1016/j.ymthe.2024.02.032) (wen2024genotype–phenotypecorrelationin pages 13-17, lau2024lentiviralexpressionof pages 1-2, lau2024lentiviralexpressionof pages 2-4) |
| Diagnostic modalities | Key modalities include **clinical phenotyping**, **immunofluorescence mapping (IFM / antigen mapping)** to localize the cleavage plane and assess BMZ protein expression, **transmission electron microscopy (TEM)** for ultrastructural defects/hemidesmosomes, and **molecular testing** using **Sanger sequencing, targeted panels, WES, and WGS/GS**. Recent evidence shows a role for **RNA/splicing assays** when exome sequencing is inconclusive (Wen et al., Jun 2024, https://doi.org/10.1016/j.jid.2023.11.021; Chen et al., Feb 2025, https://doi.org/10.1038/s41525-025-00466-8) (wen2024genotype–phenotypecorrelationin pages 13-17, wen2024genotype–phenotypecorrelationin pages 17-22, chen2025identificationofdeep pages 1-2) |
| Diagnostic yield / deep intronic findings | In a 2025 JEB genomics study of **69 recessive JEB cases**, **13.0%** remained genetically undiagnosed after initial exome sequencing; among **COL17A1** cases, unresolved rate reached **31.6%**. Genome sequencing plus splicing assays identified deep intronic variants **COL17A1 c.4156+117G>A, c.2039-104G>A, c.1267+237dupC** and **LAMB3 c.-38+2T>C**; these caused **exon skipping or pseudoexon insertion** in **HaCaT** keratinocyte cells but not HEK293 cells, supporting GS + cell-appropriate transcript testing for ES-negative JEB (Chen et al., published Feb 2025, https://doi.org/10.1038/s41525-025-00466-8) (chen2025identificationofdeep pages 1-2) |
| Epidemiology | A 2024 genotype-phenotype study cites JEB **incidence ~2.68 per million live births** and **prevalence ~0.49 per million**. A 2020 review states JEB affects about **3 in 1 million children**. Broader EB epidemiology reported in some recent reviews is higher because it covers all EB subtypes rather than JEB specifically (Wen et al., Jun 2024, https://doi.org/10.1016/j.jid.2023.11.021; Keith et al., Mar 2020, https://doi.org/10.1080/14712598.2020.1740678) (keith2020leadingedgeemerging pages 1-6, wen2024genotype–phenotypecorrelationin pages 13-17, wen2024genotype–phenotypecorrelationin pages 17-22) |
| Russian registry data (all congenital EB, with JEB-specific mortality note) | Russian pediatric registry, publication accepted **16 Oct 2024** / journal issue 2024, DOI https://doi.org/10.15690/vsp.v23i5.2808: **491** children with congenital EB; pediatric prevalence **15.48 per 1,000,000**; subtype distribution **261 dystrophic (53%)**, **191 simplex (39%)**, **31 junctional (6%)**, **8 Kindler (2%)**. Mean birth rate 2019–2023: **2.13 per 100,000 births**. Registry recorded **22 deaths**; **JEB accounted for 59.1% of fatal outcomes (13/22)** with mean age at death **0.40 ± 0.22 years**; survival curve showed probability of survival falling to **almost 0% in the first 100 days** for JEB (Murashkin et al., 2024, https://doi.org/10.15690/vsp.v23i5.2808) (murashkin2024congenitalepidermolysisbullosa pages 2-3, murashkin2024congenitalepidermolysisbullosa pages 1-2) |
| Standard/current management | Current standard of care remains **supportive and multidisciplinary**: blister lancing, atraumatic wound care, infection control, pain management, nutritional and systemic support, and treatment of complications. Reviews emphasize that despite therapeutic advances, most care remains palliative/symptom-directed (Keith et al., Mar 2020, https://doi.org/10.1080/14712598.2020.1740678; Danescu et al., published online Aug 2, 2024, https://doi.org/10.1007/s13555-024-01227-8) (keith2020leadingedgeemerging pages 1-6, danescu2024treatmentofepidermolysis pages 1-4) |
| Recently approved / wound-directed therapies relevant to EB | A 2024 therapeutic review states that **“the first drugs for the treatment of EB wounds in dystrophic and junctional EB have recently achieved US FDA and EMA approval”**; it also notes that **B-VEC** became the first gene therapy clinically available for DEB on **May 19, 2023**, illustrating regulatory momentum in EB even though B-VEC is not JEB-specific (Danescu et al., Aug 2, 2024, https://doi.org/10.1007/s13555-024-01227-8) (danescu2024treatmentofepidermolysis pages 1-4, danescu2024treatmentofepidermolysis pages 4-5) |
| Gentamicin nonsense readthrough trials | **NCT03526159** (“Gentamicin for Junctional Epidermolysis Bullosa”; first posted **2018-05-16**; recruiting per available registry snapshot) tests **topical 0.5% gentamicin twice daily for 14 days** or **IV gentamicin 7.5 mg/kg daily for 14 days** in JEB with **LAMB3 nonsense mutations**, with endpoints including laminin-332 IF signal, EM hemidesmosomes, wound closure, and safety. **NCT04140786** (“Optimizing IV Gentamicin in JEB”; first posted **2019-10-28**) studies **10 mg/kg IV** regimens (daily x24 days or biweekly x3 months) in JEB with **LAMA3/LAMB3 nonsense mutations**, with endpoints including laminin-332 expression, EBDASI, ototoxicity, nephrotoxicity, and anti-laminin-332 antibodies (https://clinicaltrials.gov/study/NCT03526159; https://clinicaltrials.gov/study/NCT04140786) (NCT03526159 chunk 1, NCT03526159 chunk 2, NCT04140786 chunk 1, NCT04140786 chunk 2) |
| Ex vivo LAMB3 gene-corrected epidermal grafts | Ex vivo autologous **LAMB3**-corrected keratinocyte / epidermal stem-cell grafting is the most mature JEB-specific gene-therapy paradigm. **Hologene 5** (EudraCT **2018-000261-36**; protocol paper 2021, https://doi.org/10.3389/fgene.2021.705019) is a phase II/III multicenter study using **γ-retroviral full-length LAMB3 cDNA** in autologous clonogenic keratinocytes on fibrin support for grafting. A 2024 review highlights prior life-saving transplantation over ~80% TBSA and durable **5-year** maintenance of genetically repaired epidermis (Danescu et al., 2024; De Rosa et al., 2021) (rosa2021hologene5a pages 1-2, danescu2024treatmentofepidermolysis pages 4-5) |
| Airway-targeted gene/cell proof-of-concept | In **Lau et al.** (*Molecular Therapy*, published May 2024, https://doi.org/10.1016/j.ymthe.2024.02.032), a cohort of **16** EB patients with airway disease was described; **10/15** genotyped patients had at least one **LAMA3** pathogenic variant, median age at referral **9 months**, and **8/16** had died by time of report. Patient airway basal cells showed adhesion defects; lentiviral **LAMA3A** overexpression increased LAMA3 mRNA by **45.5-fold** and **79.6-fold** in two cultures, enabled ALI differentiation with **normal-range TEER (>250 Ω)** and **normal ciliary beat frequency (7–16 Hz)**, and restored adhesion to near non-EB control levels—supporting a future combined airway cell/gene therapy approach (lau2024lentiviralexpressionof pages 4-5, lau2024lentiviralexpressionof pages 1-2, lau2024lentiviralexpressionof pages 2-4) |
| Other/adjunct experimental wound therapies | **RGN-137 topical gel** (thymosin β4-related wound-healing approach) was studied in JEB/DEB in **NCT03578029 (CELEB)**, a randomized placebo-controlled phase II trial first posted **2018-07-05**; status later **terminated (business decision)** with only **4** enrolled, illustrating the difficulty of wound-therapy trials in rare EB (https://clinicaltrials.gov/study/NCT03578029) (NCT03578029 chunk 1, NCT03578029 chunk 2) |


*Table: This table condenses the most clinically relevant facts about Junctional Epidermolysis Bullosa, including genes, inheritance, severity correlations, diagnostics, epidemiology, and current or emerging therapies. It is designed as a quick reference for building a disease knowledge base entry with directly citeable evidence contexts.*

References

1. (OpenTargets Search: Junctional epidermolysis bullosa): Open Targets Query (Junctional epidermolysis bullosa, 34 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (keith2020leadingedgeemerging pages 1-6): Allison R. Keith, Kirk Twaroski, Christen L. Ebens, and Jakub Tolar. Leading edge: emerging drug, cell, and gene therapies for junctional epidermolysis bullosa. Expert Opinion on Biological Therapy, 20:911-923, Mar 2020. URL: https://doi.org/10.1080/14712598.2020.1740678, doi:10.1080/14712598.2020.1740678. This article has 22 citations and is from a peer-reviewed journal.

3. (wen2024genotype–phenotypecorrelationin pages 13-17): David Wen, Manrup Hunjan, Ajoy Bardhan, Natasha Harper, Malobi Ogboli, Linda Ozoemena, Lu Liu, Jo-David Fine, Iain Chapple, Dario L. Balacco, and Adrian Heagerty. Genotype–phenotype correlation in junctional epidermolysis bullosa: signposts to severity. Journal of Investigative Dermatology, 144:1334-1343.e14, Jun 2024. URL: https://doi.org/10.1016/j.jid.2023.11.021, doi:10.1016/j.jid.2023.11.021. This article has 10 citations and is from a highest quality peer-reviewed journal.

4. (wen2024genotype–phenotypecorrelationin pages 17-22): David Wen, Manrup Hunjan, Ajoy Bardhan, Natasha Harper, Malobi Ogboli, Linda Ozoemena, Lu Liu, Jo-David Fine, Iain Chapple, Dario L. Balacco, and Adrian Heagerty. Genotype–phenotype correlation in junctional epidermolysis bullosa: signposts to severity. Journal of Investigative Dermatology, 144:1334-1343.e14, Jun 2024. URL: https://doi.org/10.1016/j.jid.2023.11.021, doi:10.1016/j.jid.2023.11.021. This article has 10 citations and is from a highest quality peer-reviewed journal.

5. (chen2025identificationofdeep pages 1-2): Fuying Chen, Ruoqu Wei, Yumeng Wang, Qiaoyu Cao, Jianbo Wang, Chenfei Wang, Dingjin Yao, Zhirong Yao, Cheng Ni, and Ming Li. Identification of deep intronic variants in junctional epidermolysis bullosa using genome sequencing and splicing assays. NPJ Genomic Medicine, Feb 2025. URL: https://doi.org/10.1038/s41525-025-00466-8, doi:10.1038/s41525-025-00466-8. This article has 2 citations and is from a peer-reviewed journal.

6. (lau2024lentiviralexpressionof pages 1-2): Chun Hang Lau, Maral J. Rouhani, Elizabeth F. Maughan, Jessica C. Orr, Krishna K. Kolluri, David R. Pearce, Elizabeth K. Haughey, Liam Sutton, Sam Flatau, Pablo Lopez Balboa, Maria Laura Bageta, Christopher O’Callaghan, Claire M. Smith, Sam M. Janes, Richard Hewitt, Gabriela Petrof, Anna E. Martinez, John A. McGrath, Colin R. Butler, and Robert E. Hynds. Lentiviral expression of wild-type lama3a restores cell adhesion in airway basal cells from children with epidermolysis bullosa. Molecular Therapy, 32:1497-1509, May 2024. URL: https://doi.org/10.1016/j.ymthe.2024.02.032, doi:10.1016/j.ymthe.2024.02.032. This article has 8 citations and is from a highest quality peer-reviewed journal.

7. (bischof2024emerginggenetherapeutics pages 1-2): Johannes Bischof, Markus Hierl, and Ulrich Koller. Emerging gene therapeutics for epidermolysis bullosa under development. International Journal of Molecular Sciences, 25:2243, Feb 2024. URL: https://doi.org/10.3390/ijms25042243, doi:10.3390/ijms25042243. This article has 37 citations.

8. (NCT03526159 chunk 1): David Woodley. Gentamicin for Junctional Epidermolysis Bullosa. University of Southern California. 2018. ClinicalTrials.gov Identifier: NCT03526159

9. (murashkin2024congenitalepidermolysisbullosa pages 2-3): Nikolay N. Murashkin, Roman V. Epishev, Olga S. Orlova, Alena А. Kuratova, and Victoriya S. Polenova. Congenital epidermolysis bullosa epidemiology among children of russian federation. Current Pediatrics, 23:316-328, Oct 2024. URL: https://doi.org/10.15690/vsp.v23i5.2808, doi:10.15690/vsp.v23i5.2808. This article has 2 citations.

10. (murashkin2024congenitalepidermolysisbullosa pages 1-2): Nikolay N. Murashkin, Roman V. Epishev, Olga S. Orlova, Alena А. Kuratova, and Victoriya S. Polenova. Congenital epidermolysis bullosa epidemiology among children of russian federation. Current Pediatrics, 23:316-328, Oct 2024. URL: https://doi.org/10.15690/vsp.v23i5.2808, doi:10.15690/vsp.v23i5.2808. This article has 2 citations.

11. (lau2024lentiviralexpressionof pages 2-4): Chun Hang Lau, Maral J. Rouhani, Elizabeth F. Maughan, Jessica C. Orr, Krishna K. Kolluri, David R. Pearce, Elizabeth K. Haughey, Liam Sutton, Sam Flatau, Pablo Lopez Balboa, Maria Laura Bageta, Christopher O’Callaghan, Claire M. Smith, Sam M. Janes, Richard Hewitt, Gabriela Petrof, Anna E. Martinez, John A. McGrath, Colin R. Butler, and Robert E. Hynds. Lentiviral expression of wild-type lama3a restores cell adhesion in airway basal cells from children with epidermolysis bullosa. Molecular Therapy, 32:1497-1509, May 2024. URL: https://doi.org/10.1016/j.ymthe.2024.02.032, doi:10.1016/j.ymthe.2024.02.032. This article has 8 citations and is from a highest quality peer-reviewed journal.

12. (sproule2014molecularidentificationof pages 1-2): Thomas J. Sproule, Jason A. Bubier, Fiorella C. Grandi, Victor Z. Sun, Vivek M. Philip, Caroline G. McPhee, Elisabeth B. Adkins, John P. Sundberg, and Derry C. Roopenian. Molecular identification of collagen 17a1 as a major genetic modifier of laminin gamma 2 mutation-induced junctional epidermolysis bullosa in mice. PLoS Genetics, 10:e1004068, Feb 2014. URL: https://doi.org/10.1371/journal.pgen.1004068, doi:10.1371/journal.pgen.1004068. This article has 38 citations and is from a domain leading peer-reviewed journal.

13. (sproule2023sevennaturallyvariant pages 1-2): Thomas J. Sproule, Vivek M. Philip, Nabig A. Chaudhry, Derry C. Roopenian, and John P. Sundberg. Seven naturally variant loci serve as genetic modifiers of lamc2jeb induced non-herlitz junctional epidermolysis bullosa in mice. PLOS ONE, 18:e0288263, Jul 2023. URL: https://doi.org/10.1371/journal.pone.0288263, doi:10.1371/journal.pone.0288263. This article has 7 citations and is from a peer-reviewed journal.

14. (lau2024lentiviralexpressionof pages 4-5): Chun Hang Lau, Maral J. Rouhani, Elizabeth F. Maughan, Jessica C. Orr, Krishna K. Kolluri, David R. Pearce, Elizabeth K. Haughey, Liam Sutton, Sam Flatau, Pablo Lopez Balboa, Maria Laura Bageta, Christopher O’Callaghan, Claire M. Smith, Sam M. Janes, Richard Hewitt, Gabriela Petrof, Anna E. Martinez, John A. McGrath, Colin R. Butler, and Robert E. Hynds. Lentiviral expression of wild-type lama3a restores cell adhesion in airway basal cells from children with epidermolysis bullosa. Molecular Therapy, 32:1497-1509, May 2024. URL: https://doi.org/10.1016/j.ymthe.2024.02.032, doi:10.1016/j.ymthe.2024.02.032. This article has 8 citations and is from a highest quality peer-reviewed journal.

15. (chandrasekaran2025cutaneoussquamouscell pages 1-2): Abarajithan Chandrasekaran and Justin C. Moser. Cutaneous squamous cell carcinoma in epidermolysis bullosa: a review of pathogenesis, diagnosis and management. Cancers, 17:3211, Oct 2025. URL: https://doi.org/10.3390/cancers17193211, doi:10.3390/cancers17193211. This article has 0 citations.

16. (has2019clinicalpracticeguidelines pages 1-2): C. Has, L. Liu, M.C. Bolling, A.V. Charlesworth, M. El Hachem, M.J. Escámez, I. Fuentes, S. Büchel, R. Hiremagalore, G. Pohla‐Gubo, P.C. Akker, K. Wertheim‐Tysarowska, and G. Zambruno. Clinical practice guidelines for laboratory diagnosis of epidermolysis bullosa. The British Journal of Dermatology, 182:574-592, Aug 2019. URL: https://doi.org/10.1111/bjd.18128, doi:10.1111/bjd.18128. This article has 186 citations.

17. (has2019clinicalpracticeguidelines pages 2-3): C. Has, L. Liu, M.C. Bolling, A.V. Charlesworth, M. El Hachem, M.J. Escámez, I. Fuentes, S. Büchel, R. Hiremagalore, G. Pohla‐Gubo, P.C. Akker, K. Wertheim‐Tysarowska, and G. Zambruno. Clinical practice guidelines for laboratory diagnosis of epidermolysis bullosa. The British Journal of Dermatology, 182:574-592, Aug 2019. URL: https://doi.org/10.1111/bjd.18128, doi:10.1111/bjd.18128. This article has 186 citations.

18. (danescu2024treatmentofepidermolysis pages 1-4): Sorina Danescu, Mircea Negrutiu, and Cristina Has. Treatment of epidermolysis bullosa and future directions: a review. Dermatology and Therapy, 14:2059-2075, Aug 2024. URL: https://doi.org/10.1007/s13555-024-01227-8, doi:10.1007/s13555-024-01227-8. This article has 14 citations.

19. (danescu2024treatmentofepidermolysis pages 4-5): Sorina Danescu, Mircea Negrutiu, and Cristina Has. Treatment of epidermolysis bullosa and future directions: a review. Dermatology and Therapy, 14:2059-2075, Aug 2024. URL: https://doi.org/10.1007/s13555-024-01227-8, doi:10.1007/s13555-024-01227-8. This article has 14 citations.

20. (rosa2021hologene5a pages 1-2): Laura De Rosa, Elena Enzo, Giulia Zardi, Christine Bodemer, Cristina Magnoni, Holm Schneider, and Michele De Luca. Hologene 5: a phase ii/iii clinical trial of combined cell and gene therapy of junctional epidermolysis bullosa. Frontiers in Genetics, Sep 2021. URL: https://doi.org/10.3389/fgene.2021.705019, doi:10.3389/fgene.2021.705019. This article has 35 citations and is from a peer-reviewed journal.

21. (NCT04140786 chunk 1): David Woodley. Optimizing IV Gentamicin in JEB. University of Southern California. 2019. ClinicalTrials.gov Identifier: NCT04140786

22. (natsuga2010animalmodelsof pages 1-2): Ken Natsuga, Satoru Shinkuma, Wataru Nishie, and Hiroshi Shimizu. Animal models of epidermolysis bullosa. Dermatologic clinics, 28 1:137-42, Jan 2010. URL: https://doi.org/10.1016/j.det.2009.10.016, doi:10.1016/j.det.2009.10.016. This article has 32 citations and is from a peer-reviewed journal.

23. (NCT03526159 chunk 2): David Woodley. Gentamicin for Junctional Epidermolysis Bullosa. University of Southern California. 2018. ClinicalTrials.gov Identifier: NCT03526159

24. (NCT04140786 chunk 2): David Woodley. Optimizing IV Gentamicin in JEB. University of Southern California. 2019. ClinicalTrials.gov Identifier: NCT04140786

25. (NCT03578029 chunk 1):  Evaluation of the Safety and Efficacy Study of RGN-137 Topical Gel for Junctional and Dystrophic Epidermolysis Bullosa. Lenus Therapeutics, LLC. 2019. ClinicalTrials.gov Identifier: NCT03578029

26. (NCT03578029 chunk 2):  Evaluation of the Safety and Efficacy Study of RGN-137 Topical Gel for Junctional and Dystrophic Epidermolysis Bullosa. Lenus Therapeutics, LLC. 2019. ClinicalTrials.gov Identifier: NCT03578029
