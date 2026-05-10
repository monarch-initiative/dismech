---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T23:02:00.710114'
end_time: '2026-05-09T23:16:53.313773'
duration_seconds: 892.6
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Kindler Epidermolysis Bullosa
  mondo_id: ''
  category: Mendelian
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
- **Disease Name:** Kindler Epidermolysis Bullosa
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Kindler Epidermolysis Bullosa** covering all of the
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
- **Disease Name:** Kindler Epidermolysis Bullosa
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Kindler Epidermolysis Bullosa** covering all of the
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


## Comprehensive Research Report: Kindler Epidermolysis Bullosa (Kindler Syndrome)

### Executive summary
Kindler epidermolysis bullosa (KEB), historically termed **Kindler syndrome (KS)**, is a rare **autosomal recessive** inherited skin-fragility disorder caused by **bi-allelic loss-of-function variants in *FERMT1* (KIND1)** encoding **kindlin‑1**, a focal-adhesion adaptor that regulates **integrin activation** and epithelial cell–matrix adhesion. Clinically, it typically presents with **acral blistering in infancy**, **photosensitivity**, and **progressive poikiloderma and cutaneous atrophy**, with frequent **mucosal** (oral/GI/GU/ocular) complications and a clinically important risk of **aggressive squamous cell carcinoma (SCC)**. (has2010mildclinicalphenotype pages 1-1, youssefian2022kindlersyndrome pages 1-1, bhandary2024unusualoralmanifestation pages 1-2)

| Category | Summary | Study/source/date | DOI / URL |
|---|---|---|---|
| Disease name / synonyms | **Kindler syndrome**; **Kindler epidermolysis bullosa (KEB)**; rare inherited epidermolysis bullosa characterized by acral blistering, photosensitivity, progressive poikiloderma, skin atrophy, and mucosal disease (klausegger2025anovelhomozygous pages 12-13, laicheong2015kindlersyndrome pages 5-7, has2010mildclinicalphenotype pages 1-1) | Lai-Cheong & McGrath, *Blistering Diseases*, Jan 2015; Klausegger et al., *Int J Mol Sci*, Apr 2025; Has et al., *Dermatology*, Oct 2010 (klausegger2025anovelhomozygous pages 12-13, laicheong2015kindlersyndrome pages 5-7, has2010mildclinicalphenotype pages 1-1) | https://doi.org/10.1007/978-3-662-45698-9_43 ; https://doi.org/10.3390/ijms26094237 ; https://doi.org/10.1159/000320235 |
| Causal gene / protein | **FERMT1** (also **KIND1**) encodes **kindlin-1**, a focal-adhesion/integrin-associated protein required for keratinocyte adhesion and migration; loss-of-function variants cause KEB (has2011kindlersyndromeextension pages 1-3, dsouza2010kindlersyndromepathogenesis pages 1-3, bhandary2024unusualoralmanifestation pages 1-2) | Has et al., *Hum Mutat*, Nov 2011; D'Souza et al., *Dermatol Clin*, Jan 2010; Bhandary et al., *Front Oral Health*, Sep 2024 (has2011kindlersyndromeextension pages 1-3, dsouza2010kindlersyndromepathogenesis pages 1-3, bhandary2024unusualoralmanifestation pages 1-2) | https://doi.org/10.1002/humu.21576 ; https://doi.org/10.1016/j.det.2009.10.012 ; https://doi.org/10.3389/froh.2024.1430698 |
| Inheritance | **Autosomal recessive (AR)** Mendelian disorder due to bi-allelic FERMT1 pathogenic variants (laicheong2015kindlersyndrome pages 5-7, has2010mildclinicalphenotype pages 1-1, has2020consensusreclassificationof pages 1-2) | Lai-Cheong & McGrath, Jan 2015; Has et al., Oct 2010; Has et al. consensus reclassification, Mar 2020 (laicheong2015kindlersyndrome pages 5-7, has2010mildclinicalphenotype pages 1-1, has2020consensusreclassificationof pages 1-2) | https://doi.org/10.1007/978-3-662-45698-9_43 ; https://doi.org/10.1159/000320235 ; https://doi.org/10.1111/bjd.18921 |
| Key clinical hallmarks | Typical phenotype: **acral blistering in infancy/childhood**, **photosensitivity**, **progressive poikiloderma**, **skin atrophy**, and **mucosal involvement** (oral, ocular, gastrointestinal/genitourinary); blistering often improves with age while poikiloderma/atrophy and fibrosis progress (ahmed2024battlingararity pages 4-5, youssefian2022kindlersyndrome pages 1-1, laicheong2010kindlersyndrome. pages 3-5) | Ahmed et al., *SAGE Open Med Case Rep*, Jan 2024; Youssefian et al., *Indian Pediatrics*, 2022; Lai-Cheong & McGrath, *Dermatol Clin*, Jan 2010 (ahmed2024battlingararity pages 4-5, youssefian2022kindlersyndrome pages 1-1, laicheong2010kindlersyndrome. pages 3-5) | https://doi.org/10.1177/2050313X241231518 ; https://doi.org/10.1007/s13312-018-1239-y ; https://doi.org/10.1016/j.det.2009.10.013 |
| Natural history statistic | **59-patient natural history cohort:** skin blistering occurred in **100% of patients younger than 10 years** and **decreased progressively with age**; adult skin fragility is often milder (has2011kindlersyndromeextension pages 5-6) | Has et al., *Human Mutation*, Nov 2011 (59 patients) (has2011kindlersyndromeextension pages 5-6) | https://doi.org/10.1002/humu.21576 |
| Cancer risk statistic | **91-patient SCC cohort:** **13/91 (14.3%)** developed SCC; **youngest age 29 years**; cumulative SCC risk reached **66.7% in patients >60 years**; **53.8%** of SCC-bearing patients developed metastases; **38.5% (5/13)** died from tumor within **2–7 years** (mean survival **40.8 months**) (guerreroaspizua2019assessmentofthe pages 1-2, guerreroaspizua2019assessmentofthe pages 2-4) | Guerrero-Aspizua et al., *Orphanet J Rare Dis*, Jul 2019 (guerreroaspizua2019assessmentofthe pages 1-2, guerreroaspizua2019assessmentofthe pages 2-4) | https://doi.org/10.1186/s13023-019-1158-6 |
| 2024 China review frequencies | Chinese review of reported KS cases: **skin abnormalities 100%**, **palmoplantar hyperkeratosis 91.70%**, **nail abnormalities 77.78%**, **finger/toe abnormalities 75.00%**, **oral damage 70.00%**, **eye abnormalities 57.14%**, **constipation 50.00%** (zhang2024identificationofa pages 2-3) | Zhang et al., *Frontiers in Pediatrics*, Sep 2024 (zhang2024identificationofa pages 2-3) | https://doi.org/10.3389/fped.2024.1425030 |


*Table: This table condenses the most important disease-definition, genetics, inheritance, phenotype, and quantitative cohort data for Kindler epidermolysis bullosa. It highlights the core facts and the best-supported statistics useful for a knowledge-base entry.*

---

## 1. Disease Information

### 1.1 What is the disease? (concise overview)
Kindler syndrome/KEB is a distinct subtype of inherited epidermolysis bullosa characterized by skin fragility with blistering, photosensitivity, and progressive poikiloderma and atrophy, often accompanied by mucosal inflammation and fibrotic stenoses; it is caused by loss-of-function *FERMT1* variants leading to kindlin‑1 deficiency. (laicheong2010kindlersyndrome. pages 3-5, laicheong2015kindlersyndrome pages 5-7, has2010mildclinicalphenotype pages 1-1)

### 1.2 Key identifiers and codes
- **OMIM disease**: **Kindler syndrome / Kindler epidermolysis bullosa**: **OMIM 173650** (explicitly stated in a peer-reviewed KS case report). (has2010mildclinicalphenotype pages 1-1)
- **Other identifiers (Orphanet ORPHA, ICD‑10/ICD‑11, MeSH, MONDO)**: Not extractable from the currently retrieved full-text set using available tools; these codes typically require direct database queries to OMIM/Orphanet/ICD/MeSH/MONDO services, which are not available in the current toolset. (has2010mildclinicalphenotype pages 1-1)

### 1.3 Synonyms and alternative names
- Kindler syndrome (KS)
- Kindler epidermolysis bullosa (KEB) (klausegger2025anovelhomozygous pages 12-13, has2020consensusreclassificationof pages 1-2)
- Historic/legacy: “congenital poikiloderma with traumatic bulla formation and progressive cutaneous atrophy” (1954 description) (dsouza2010kindlersyndromepathogenesis pages 3-4)

### 1.4 Evidence source type
Most disease-level statements (inheritance, gene, canonical features, complications) are derived from **aggregated disease resources and cohorts** (e.g., consensus reclassification; multicenter cohorts) and complemented by **case reports** documenting phenotypic variability and resource-limited diagnostic pathways. (has2020consensusreclassificationof pages 1-2, guerreroaspizua2019assessmentofthe pages 1-2, ahmed2024battlingararity pages 4-5)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause (genetic):** autosomal recessive, bi-allelic *FERMT1* pathogenic variants leading to loss or dysfunction of kindlin‑1. (laicheong2015kindlersyndrome pages 5-7, has2010mildclinicalphenotype pages 1-1, has2011kindlersyndromeextension pages 1-3)

**Mechanistic cause:** kindlin‑1 is a focal-adhesion/integrin-associated adaptor; deficiency impairs integrin activation and epithelial cell adhesion/migration, leading to mechanical fragility and abnormal dermal–epidermal junction integrity. (bhandary2024unusualoralmanifestation pages 1-2, dsouza2010kindlersyndromepathogenesis pages 1-3)

### 2.2 Risk factors
**Genetic risk factors (causal variants):**
- Variant spectrum includes nonsense, frameshift, splice-site, missense, promoter changes, and large deletions; most are predicted to cause premature termination and kindlin‑1 loss. (klausegger2025anovelhomozygous pages 12-13, has2011kindlersyndromeextension pages 1-3)
- A 2024 WES-based diagnostic example identified a novel frameshift variant **c.567_579del (p.Ile190Serfs*10)** interpreted using ACMG/AMP criteria (PVS1/PM2 cited in the report). (zhang2024identificationofa pages 2-3)

**Non-genetic/clinical triggers that exacerbate symptoms:**
- **Mechanical trauma** (skin blistering with minor trauma) and **sunlight/UV exposure** (photosensitivity) are core disease triggers, consistent with a structural adhesion defect. (youssefian2022kindlersyndrome pages 1-1, ahmed2024battlingararity pages 4-5)

### 2.3 Protective factors
No specific genetic protective alleles were identified in the retrieved literature. Clinically, **photoprotection** and **friction/trauma minimization** are protective for lesion prevention, but these are management strategies rather than etiologic protective factors. (youssefian2022kindlersyndrome pages 1-1, laicheong2010kindlersyndrome. pages 3-5)

### 2.4 Gene–environment interactions
Evidence is largely clinical/phenomenological: **UV exposure** and **chronic inflammation at high-friction sites** appear to interact with kindlin‑1 deficiency to increase tissue injury and possibly malignancy risk; SCCs cluster at chronically inflamed sites (hands and perioral areas). (guerreroaspizua2019assessmentofthe pages 1-2, guerreroaspizua2019assessmentofthe pages 7-8)

---

## 3. Phenotypes (clinical spectrum)

### 3.1 Core cutaneous phenotype
**Typical onset:** infancy/early childhood with acral blistering. (youssefian2022kindlersyndrome pages 1-1, ahmed2024battlingararity pages 4-5)

**Natural history:** In a 59-patient KS natural history cohort, blistering occurred in **100% of patients younger than 10 years** and **decreased progressively with age**. (has2011kindlersyndromeextension pages 5-6)

**Key manifestations (suggested HPO terms):**
- Acral blistering / skin fragility — *Skin blistering* (HP:0000988)
- Photosensitivity — (HP:0000992)
- Poikiloderma — (HP:0001023)
- Cutaneous atrophy — (HP:0008064)
- Palmoplantar keratoderma/hyperkeratosis — (HP:0000982)
- Nail dystrophy — (HP:0002164)

Frequency data in Chinese KS literature review: **palmoplantar hyperkeratosis 91.70%**, **nail abnormalities 77.78%**, **finger/toe abnormalities 75.00%**, **eye abnormalities 57.14%**, **constipation 50.00%**. (zhang2024identificationofa pages 2-3)

### 3.2 Mucosal/extracutaneous phenotypes
Common extracutaneous involvement includes oral, ocular, gastrointestinal and genitourinary manifestations.

**Oral/periodontal (HPO suggestions):**
- Gingival bleeding/gingivitis/periodontitis — *Gingivitis* (HP:0000230), *Periodontitis* (HP:0000692)
- Oral ulcers — (HP:0000155)

Mechanistic context from a 2024 oral-health-focused KS review: *“These clinical manifestations arise from mutations in the FERMT-1 … that encodes kindlin-1, a protein localized to focal adhesions in keratinocytes… Kindlin-1 plays a crucial role in integrin receptor activation … essential for cell adhesion and migration.”* (Sep 2024). (bhandary2024unusualoralmanifestation pages 1-2)

**GI/GU stenoses (HPO suggestions):**
- Esophageal stenosis/dysphagia — (HP:0002043 / HP:0002015)
- Anal stenosis/constipation — (HP:0002019)
- Urethral stenosis — (HP:0008665)

These complications are repeatedly emphasized in clinical descriptions and management reviews. (youssefian2022kindlersyndrome pages 1-1, laicheong2015kindlersyndrome pages 5-7)

**Ocular (HPO suggestions):**
- Ectropion — (HP:0000656)

### 3.3 Quality of life impact
Direct KS-specific QoL instruments were not identified in the retrieved corpus; however, KS is repeatedly described as requiring lifelong wound care, pain control, nutritional/dental support, and cancer surveillance, all of which plausibly impose substantial QoL burden. (ahmed2024battlingararity pages 4-5, laicheong2010kindlersyndrome. pages 3-5)

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene
- **Gene:** *FERMT1* (aka **KIND1**) (laicheong2015kindlersyndrome pages 5-7, has2011kindlersyndromeextension pages 1-3)
- **Protein:** **kindlin‑1** (focal adhesion adaptor; integrin-binding) (dsouza2010kindlersyndromepathogenesis pages 1-3, bhandary2024unusualoralmanifestation pages 1-2)

### 4.2 Pathogenic variant classes and functional consequences
- **Predominant consequence:** loss of kindlin‑1 expression or function; most reported variants cause premature termination and are expected to lead to absent/truncated protein. (has2011kindlersyndromeextension pages 1-3, guerreroaspizua2019assessmentofthe pages 1-2)
- **Large deletions / CNV-like events:** a 2025 report highlights that routine testing may miss large deletions and used an EB gene panel plus breakpoint mapping and mRNA/protein verification to identify a **~9.4 kb homozygous deletion spanning exons 7–9** predicted to cause frameshift and non-functioning protein. (klausegger2025anovelhomozygous pages 1-2)

### 4.3 Modifier genes / phenotype modifiers
Direct human genetic modifiers were not identified in the retrieved texts. However, inflammatory and profibrotic signaling is implicated in progression (cytokines and TGF‑β-related profibrotic pathways). (has2011kindlersyndromeextension pages 5-6)

### 4.4 Epigenetics and chromosomal abnormalities
No KS-specific epigenetic signatures or recurrent chromosomal abnormalities were identified in the retrieved evidence.

---

## 5. Environmental Information

### 5.1 Environmental and lifestyle factors
No exogenous toxicant/infectious cause is implicated; disease expression is worsened by **UV exposure** (photosensitivity) and **mechanical friction/trauma** (blistering). (youssefian2022kindlersyndrome pages 1-1, ahmed2024battlingararity pages 4-5)

### 5.2 Infectious agents
Infections are secondary complications of skin barrier breakdown (e.g., colonization of erosions and sepsis risk), rather than primary causes. (ahmed2024battlingararity pages 4-5)

---

## 6. Mechanism / Pathophysiology

### 6.1 Molecular and cellular mechanism (causal chain)
1) **Bi-allelic *FERMT1* loss-of-function → kindlin‑1 deficiency** (has2011kindlersyndromeextension pages 1-3, has2010mildclinicalphenotype pages 1-1)
2) **Defective integrin activation and focal adhesion function in keratinocytes** (impaired adhesion/migration) (bhandary2024unusualoralmanifestation pages 1-2, dsouza2010kindlersyndromepathogenesis pages 1-3)
3) **Basement membrane zone abnormalities and mechanical fragility** with **multi-plane cleavage** (intra-basal keratinocyte, lamina lucida, below lamina densa) and **lamina densa reduplication** on EM (dsouza2010kindlersyndromepathogenesis pages 3-4, laicheong2010kindlersyndrome. pages 3-5)
4) **Chronic injury → inflammation and profibrotic remodeling**, contributing to mucocutaneous fibrosis/stenoses and cancer-prone chronically inflamed sites. (has2011kindlersyndromeextension pages 5-6, guerreroaspizua2019assessmentofthe pages 7-8)

### 6.2 Representative pathways (ontology suggestions)
- **Integrin-mediated signaling / focal adhesion:** GO:0007229 (integrin-mediated signaling pathway), GO:0005925 (focal adhesion)
- **Cell adhesion and migration:** GO:0007155 (cell adhesion), GO:0016477 (cell migration)
- **TGF‑β signaling / fibrosis (downstream):** GO:0007179 (TGF‑β receptor signaling pathway)

### 6.3 Cell types and tissues involved (ontology suggestions)
- **Basal keratinocytes** (CL:0000312)
- **Intestinal epithelial cells** (CL:0000584)
- **Fibroblasts / myofibroblasts** (CL:0000057 / CL:0000186)

### 6.4 Cancer mechanism insights (recent, 2024)
A 2024 mechanistic cSCC paper states in its abstract: *“Kindler syndrome (KS) is a rare genodermatosis resulting from loss-of-function mutations in FERMT1 … KS patients have a high propensity to develop aggressive and metastatic cutaneous squamous cell carcinoma (cSCC).”* It further reports that kindlin‑1 loss can promote SCC tumor growth in vivo with **hypoxia, increased glycolysis, and MMP13 upregulation driving invasion**. (Jul 2024). (carrasco2024involvementofkindlin1 pages 1-2)

---

## 7. Anatomical Structures Affected

### 7.1 Organ and system level
- **Primary:** skin (epidermis/dermal–epidermal junction), oral mucosa/periodontium (youssefian2022kindlersyndrome pages 1-1, bhandary2024unusualoralmanifestation pages 1-2)
- **Secondary/complications:** gastrointestinal tract (esophagus/colon), genitourinary tract (urethra), eyes (ectropion), and cancer-prone sites (hands, perioral/oral). (youssefian2022kindlersyndrome pages 1-1, laicheong2015kindlersyndrome pages 5-7, guerreroaspizua2019assessmentofthe pages 1-2)

**UBERON suggestions:**
- Skin (UBERON:0002097)
- Oral mucosa (UBERON:0006956)
- Esophagus (UBERON:0001043)
- Colon (UBERON:0001155)
- Urethra (UBERON:0000057)

---

## 8. Temporal Development (onset and course)

- **Onset:** usually congenital/infantile acral blistering (youssefian2022kindlersyndrome pages 1-1)
- **Course:** blistering tends to improve with age, while atrophy/poikiloderma and mucosal complications may progress. (has2011kindlersyndromeextension pages 5-6, youssefian2022kindlersyndrome pages 1-1)
- **Critical periods:** adolescence/early adulthood is often when long-term complications and surveillance planning become central; a KS case report suggests adolescence as an appropriate time to start premalignant screening. (ahmed2024battlingararity pages 4-5)

---

## 9. Inheritance and Population

### 9.1 Inheritance
**Autosomal recessive.** (laicheong2015kindlersyndrome pages 5-7, has2010mildclinicalphenotype pages 1-1)

### 9.2 Epidemiology (recent registry data prioritized)
Because KS/KEB is ultra-rare, most epidemiology comes from registries.

**Romania (registry-based, 2012–2024; point prevalence as of 31 Dec 2023):**
- EB total: 152 cases; point prevalence **6.77 per million**.
- **KEB:** 3 cases (**2%**), point prevalence **0.16 per million**, and incidence **0 per million live births** in 2012–2022 interval. (Jun 2024). (suru2024epidemiologicalcharacteristicsof pages 10-12, suru2024epidemiologicalcharacteristicsof pages 1-2)

**Russian Federation pediatric registry (as of 1 Jan 2024):**
- 491 children with EB registered; pediatric prevalence **15.48 per 1,000,000 children**.
- **Kindler syndrome:** **8 patients**. (Oct 2024). (murashkin2024congenitalepidermolysisbullosa pages 1-2, murashkin2024congenitalepidermolysisbullosa pages 2-3)

---

## 10. Diagnostics

### 10.1 Clinical diagnosis
A key clinical constellation includes acral blistering in infancy/childhood, progressive poikiloderma, skin atrophy, photosensitivity, and gingival fragility; mucosal stenoses may occur. (ahmed2024battlingararity pages 4-5)

### 10.2 Skin biopsy, histopathology, TEM (electron microscopy)
Diagnostic clues include **multi-plane cleavage** at the dermal–epidermal junction and **lamina densa reduplication** on TEM; histopathology may show atrophy, loss of rete ridges, pigmentary incontinence, and melanophages. (laicheong2010kindlersyndrome. pages 3-5, dsouza2010kindlersyndromepathogenesis pages 3-4)

### 10.3 Immunofluorescence mapping / kindlin‑1 staining
Immunofluorescence mapping with anti–kindlin‑1 antibody can show reduced labeling, but labeling can be variable and can appear preserved in some mutation contexts; therefore **molecular confirmation is recommended**. (laicheong2010kindlersyndrome. pages 3-5, laicheong2015kindlersyndrome pages 5-7)

### 10.4 Genetic testing
- Sequencing-based diagnosis (single-gene or EB panels / WES) is used; WES plus Sanger confirmation is described in a 2024 KS case. (zhang2024identificationofa pages 2-3)
- Copy-number/large deletions may require additional methods (panel design, breakpoint mapping, RNA/protein verification). (klausegger2025anovelhomozygous pages 1-2)

### 10.5 Differential diagnosis
Neonatal/early-life presentation can overlap other EB types (EBS/DEB) and porphyria-like photosensitive disorders; a 2024 KS case report notes initial differential included porphyria cutanea tarda in a pediatric case due to overlapping photosensitivity/fragility. (laicheong2010kindlersyndrome. pages 3-5, ahmed2024battlingararity pages 4-5)

---

## 11. Outcome / Prognosis

### 11.1 Life expectancy
Some reports state generally normal life expectancy but emphasize substantial morbidity and the importance of surveillance for malignancy and strictures. (ahmed2024battlingararity pages 4-5)

### 11.2 Cancer outcomes (high-impact prognosis determinant)
The largest retrieved KS SCC cohort (91 adults) quantified SCC severity and outcomes:
- SCC in **13/91 (14.3%)**, youngest case **29 years**, cumulative SCC risk **66.7%** in those **>60 years**.
- **Metastatic disease in 53.8%** of SCC-bearing patients (7/13).
- **Death from tumor in 38.5%** (5/13) within 2–7 years (mean survival 40.8 months). (Jul 2019). (guerreroaspizua2019assessmentofthe pages 1-2)

---

## 12. Treatment

### 12.1 Standard of care (supportive / multidisciplinary)
No disease-modifying therapy is established; management is largely symptomatic.

**Skin care & wound care (MAXO suggestions):**
- Nonadherent dressings, infection prevention, debridement as needed, and pain control are emphasized in case-based guidance; one report lists dressings (foams, hydrogel sheets, alginates, etc.) and analgesics including acetaminophen and opioids. (MAXO:0000015 Wound care; MAXO:0000046 Pain management) (ahmed2024battlingararity pages 4-5)

**Photoprotection:** broad-spectrum sunscreen and UV avoidance are recommended. (MAXO:0000075 Photoprotection) (youssefian2022kindlersyndrome pages 1-1)

**Oral/dental care:** regular dental care to manage gingivitis/periodontitis. (MAXO: Dental care) (laicheong2010kindlersyndrome. pages 3-5)

**Management of stenoses and complications:** esophageal dilatation for dysphagia; interventions for urethral strictures; nutrition support when needed. (laicheong2010kindlersyndrome. pages 3-5, laicheong2015kindlersyndrome pages 5-7)

**Cancer surveillance:** annual follow-up for premalignant keratoses and early malignancy. (youssefian2022kindlersyndrome pages 1-1, laicheong2015kindlersyndrome pages 5-7)

### 12.2 Experimental / clinical trials relevant to KEB
**Oleogel‑S10 (birch bark extract; Episalvan/Filsuvez) for EB wound healing**
- A completed Phase III trial **explicitly included Kindler EB** among eligible EB subtypes and enrolled **223 participants** (49 sites, 26 countries). Primary endpoint: first complete closure of a target wound within 45 days. ClinicalTrials.gov results were first submitted in 2023. **NCT03068780**. (NCT03068780 chunk 1)

**Cannabinol cream for EB (not Kindler-specific):** a completed Phase 2 EB trial exists (NCT04908215), but Kindler inclusion is not established in the extracted text; therefore it is not interpreted here as KEB-targeted evidence. (No KEB-specific evidence in provided excerpt.)

---

## 13. Prevention

### 13.1 Primary/secondary/tertiary prevention
- **Primary prevention of disease occurrence:** genetic counseling and reproductive planning are central due to autosomal recessive inheritance. (MAXO:0000127 Genetic counseling) (youssefian2022kindlersyndrome pages 1-1)
- **Tertiary prevention:** reduce blistering/injury through friction minimization and photoprotection; prevent complications via infection control, nutritional/dental care, and early treatment of strictures. (youssefian2022kindlersyndrome pages 1-1, laicheong2010kindlersyndrome. pages 3-5)
- **Cancer prevention/early detection:** routine surveillance for premalignant lesions and SCC due to high risk and aggressiveness. (guerreroaspizua2019assessmentofthe pages 1-2, youssefian2022kindlersyndrome pages 1-1)

---

## 14. Other Species / Natural Disease
No naturally occurring non-human Kindler syndrome analogs were identified in the retrieved evidence.

---

## 15. Model Organisms

### 15.1 Mouse models (Fermt1/Kindlin‑1 knockout)
A *Fermt1* (Kindlin‑1) knockout mouse model provides strong mechanistic evidence linking kindlin‑1 deficiency to epithelial barrier failure:
- The PLoS Genetics study states in its abstract: *“deleting Kindlin-1 in mice gives rise to skin atrophy and an intestinal epithelial dysfunction with similarities to human UC.”* (Dec 2008). (ussar2008lossofkindlin1 pages 1-2)
- Homozygous knockout pups die between P3–P5 due to intestinal epithelial detachment and destructive inflammation, attributed to **defective integrin activation** and loss of epithelial adhesion. (ussar2008lossofkindlin1 pages 2-3)

A review of EB animal models reports that Fermt1 knockout mice showed **skin atrophy** but did not show a classic blistering phenotype in that account, underscoring partial recapitulation and model limitations. (natsuga2010animalmodelsof pages 2-4)

---

## Recent developments (2023–2024 highlights)
1) **Epidemiology updates from national registries:** Romania (KEB prevalence 0.16/million; 3 KEB cases) and Russia (8 pediatric Kindler cases) provide contemporary, registry-derived denominators useful for health-system planning. (suru2024epidemiologicalcharacteristicsof pages 10-12, murashkin2024congenitalepidermolysisbullosa pages 2-3)
2) **Mechanistic cancer biology advances:** 2024 work links kindlin‑1 loss to hypoxic, glycolytic tumor environments and MMP13-driven invasion in SCC models, addressing why KS-associated SCC can be particularly aggressive. (carrasco2024involvementofkindlin1 pages 1-2)
3) **Clinical phenotyping refinement:** 2024 Chinese KS review provides updated phenotype frequencies (e.g., palmoplantar hyperkeratosis 91.70%; oral involvement 70%). (zhang2024identificationofa pages 2-3)

---

## Limitations of this report (tooling / evidence availability)
- Orphanet ORPHA, ICD‑10/ICD‑11, MeSH, and MONDO identifiers were not retrievable using the current tools because direct ontology/database lookup services are not available in the toolset; only OMIM disease number could be extracted from accessible full text. (has2010mildclinicalphenotype pages 1-1)
- Many KS publications are case reports; for several sections (epigenetics, specific modifier genes, KS-specific QoL instruments) the retrieved literature did not provide high-confidence, quantitative evidence.

---

## Key URLs (most used sources)
- 2024 Romania EB registry epidemiology (includes KEB): https://doi.org/10.3390/jcm13133742 (Jun 2024). (suru2024epidemiologicalcharacteristicsof pages 10-12)
- 2024 Kindlin-1 and SCC mechanism: https://doi.org/10.1038/s41389-024-00526-1 (Jul 2024). (carrasco2024involvementofkindlin1 pages 1-2)
- 2019 KS SCC cohort (91 patients): https://doi.org/10.1186/s13023-019-1158-6 (Jul 2019). (guerreroaspizua2019assessmentofthe pages 1-2)
- 2008 *Fermt1* knockout mouse model: https://doi.org/10.1371/journal.pgen.1000289 (Dec 2008). (ussar2008lossofkindlin1 pages 1-2)
- EB wound trial including Kindler EB: https://clinicaltrials.gov/study/NCT03068780 (results first submitted 2023 per registry record). (NCT03068780 chunk 1)


References

1. (has2010mildclinicalphenotype pages 1-1): C. Has, Bettina Burger, A. Volz, J. Kohlhase, Leena Bruckner-Tuderman, and P. Itin. Mild clinical phenotype of kindler syndrome associated with late diagnosis and skin cancer. Dermatology, 221:309-312, Oct 2010. URL: https://doi.org/10.1159/000320235, doi:10.1159/000320235. This article has 31 citations and is from a peer-reviewed journal.

2. (youssefian2022kindlersyndrome pages 1-1): L Youssefian, H Vahidnezhad, and J Uitto. Kindler syndrome. Indian Pediatrics, 55:85, 2022. URL: https://doi.org/10.1007/s13312-018-1239-y, doi:10.1007/s13312-018-1239-y. This article has 66 citations and is from a peer-reviewed journal.

3. (bhandary2024unusualoralmanifestation pages 1-2): Rahul Bhandary, Geethu Venugopalan, and Padmaraj Hegde. Unusual oral manifestation of kindler syndrome: a case report and review of literature. Frontiers in Oral Health, Sep 2024. URL: https://doi.org/10.3389/froh.2024.1430698, doi:10.3389/froh.2024.1430698. This article has 2 citations and is from a peer-reviewed journal.

4. (klausegger2025anovelhomozygous pages 12-13): Alfred Klausegger, Fabian Leditzky, Susanne Krämer, Francis Palisson, María Joao Yubero, Sebastián Véliz, Mark Jean Aan Koh, Ene-Choo Tan, Martin Laimer, Johann Wolfgang Bauer, and Ignacia Fuentes. A novel homozygous 9385 bp deletion in the fermt1 (kind1) gene in a malaysian family with kindler epidermolysis bullosa and a review of large deletions. International Journal of Molecular Sciences, 26:4237, Apr 2025. URL: https://doi.org/10.3390/ijms26094237, doi:10.3390/ijms26094237. This article has 0 citations.

5. (laicheong2015kindlersyndrome pages 5-7): Joey E. Lai-Cheong and John A. McGrath. Kindler syndrome. Blistering Diseases, pages 433-439, Jan 2015. URL: https://doi.org/10.1007/978-3-662-45698-9\_43, doi:10.1007/978-3-662-45698-9\_43. This article has 2 citations.

6. (has2011kindlersyndromeextension pages 1-3): Cristina Has, Daniele Castiglia, Marcela del Rio, Marta Garcia Diez, Eugenia Piccinni, Dimitra Kiritsi, Jürgen Kohlhase, Peter Itin, Ludovic Martin, Judith Fischer, Giovanna Zambruno, and Leena Bruckner-Tuderman. Kindler syndrome: extension of fermt1 mutational spectrum and natural history. Human Mutation, 32:1204-1212, Nov 2011. URL: https://doi.org/10.1002/humu.21576, doi:10.1002/humu.21576. This article has 167 citations and is from a domain leading peer-reviewed journal.

7. (dsouza2010kindlersyndromepathogenesis pages 1-3): Maria-Anna M.A. D'Souza, Roy M. Kimble, and James R. McMillan. Kindler syndrome pathogenesis and fermitin family homologue 1 (kindlin-1) function. Dermatologic clinics, 28 1:115-8, Jan 2010. URL: https://doi.org/10.1016/j.det.2009.10.012, doi:10.1016/j.det.2009.10.012. This article has 40 citations and is from a peer-reviewed journal.

8. (has2020consensusreclassificationof pages 1-2): C. Has, J.W. Bauer, C. Bodemer, M.C. Bolling, L. Bruckner‐Tuderman, A. Diem, J.‐D. Fine, A. Heagerty, A. Hovnanian, M.P. Marinkovich, A.E. Martinez, J.A. McGrath, C. Moss, D.F. Murrell, F. Palisson, A. Schwieger‐Briel, E. Sprecher, K. Tamai, J. Uitto, D.T. Woodley, G. Zambruno, and J.E. Mellerio. Consensus reclassification of inherited epidermolysis bullosa and other disorders with skin fragility. British Journal of Dermatology, 183:614-627, Mar 2020. URL: https://doi.org/10.1111/bjd.18921, doi:10.1111/bjd.18921. This article has 908 citations and is from a highest quality peer-reviewed journal.

9. (ahmed2024battlingararity pages 4-5): Alina Ahmed, Tasheen Zehra, Alina Moin, and Shajie Ur Rehman Usmani. Battling a rarity: a case of kindler syndrome from a developing country. SAGE Open Medical Case Reports, Jan 2024. URL: https://doi.org/10.1177/2050313x241231518, doi:10.1177/2050313x241231518. This article has 8 citations and is from a peer-reviewed journal.

10. (laicheong2010kindlersyndrome. pages 3-5): Joey E. Lai-Cheong and John A. McGrath. Kindler syndrome. Dermatologic clinics, 28 1:119-24, Jan 2010. URL: https://doi.org/10.1016/j.det.2009.10.013, doi:10.1016/j.det.2009.10.013. This article has 111 citations and is from a peer-reviewed journal.

11. (has2011kindlersyndromeextension pages 5-6): Cristina Has, Daniele Castiglia, Marcela del Rio, Marta Garcia Diez, Eugenia Piccinni, Dimitra Kiritsi, Jürgen Kohlhase, Peter Itin, Ludovic Martin, Judith Fischer, Giovanna Zambruno, and Leena Bruckner-Tuderman. Kindler syndrome: extension of fermt1 mutational spectrum and natural history. Human Mutation, 32:1204-1212, Nov 2011. URL: https://doi.org/10.1002/humu.21576, doi:10.1002/humu.21576. This article has 167 citations and is from a domain leading peer-reviewed journal.

12. (guerreroaspizua2019assessmentofthe pages 1-2): Sara Guerrero-Aspizua, Claudio J. Conti, Maria Jose Escamez, Daniele Castiglia, Giovanna Zambruno, Leila Youssefian, Hassan Vahidnezhad, Luis Requena, Peter Itin, Gianluca Tadini, Ivelina Yordanova, Ludovic Martin, Jouni Uitto, Cristina Has, and Marcela Del Rio. Assessment of the risk and characterization of non-melanoma skin cancer in kindler syndrome: study of a series of 91 patients. Orphanet Journal of Rare Diseases, Jul 2019. URL: https://doi.org/10.1186/s13023-019-1158-6, doi:10.1186/s13023-019-1158-6. This article has 37 citations and is from a peer-reviewed journal.

13. (guerreroaspizua2019assessmentofthe pages 2-4): Sara Guerrero-Aspizua, Claudio J. Conti, Maria Jose Escamez, Daniele Castiglia, Giovanna Zambruno, Leila Youssefian, Hassan Vahidnezhad, Luis Requena, Peter Itin, Gianluca Tadini, Ivelina Yordanova, Ludovic Martin, Jouni Uitto, Cristina Has, and Marcela Del Rio. Assessment of the risk and characterization of non-melanoma skin cancer in kindler syndrome: study of a series of 91 patients. Orphanet Journal of Rare Diseases, Jul 2019. URL: https://doi.org/10.1186/s13023-019-1158-6, doi:10.1186/s13023-019-1158-6. This article has 37 citations and is from a peer-reviewed journal.

14. (zhang2024identificationofa pages 2-3): Qiang Zhang, Qi Yang, Fei Shen, Linlin Wang, and Jingsi Luo. Identification of a novel fermt1 variant causing kindler syndrome and a review of the clinical and molecular genetic features in chinese patients. Frontiers in Pediatrics, Sep 2024. URL: https://doi.org/10.3389/fped.2024.1425030, doi:10.3389/fped.2024.1425030. This article has 3 citations.

15. (dsouza2010kindlersyndromepathogenesis pages 3-4): Maria-Anna M.A. D'Souza, Roy M. Kimble, and James R. McMillan. Kindler syndrome pathogenesis and fermitin family homologue 1 (kindlin-1) function. Dermatologic clinics, 28 1:115-8, Jan 2010. URL: https://doi.org/10.1016/j.det.2009.10.012, doi:10.1016/j.det.2009.10.012. This article has 40 citations and is from a peer-reviewed journal.

16. (guerreroaspizua2019assessmentofthe pages 7-8): Sara Guerrero-Aspizua, Claudio J. Conti, Maria Jose Escamez, Daniele Castiglia, Giovanna Zambruno, Leila Youssefian, Hassan Vahidnezhad, Luis Requena, Peter Itin, Gianluca Tadini, Ivelina Yordanova, Ludovic Martin, Jouni Uitto, Cristina Has, and Marcela Del Rio. Assessment of the risk and characterization of non-melanoma skin cancer in kindler syndrome: study of a series of 91 patients. Orphanet Journal of Rare Diseases, Jul 2019. URL: https://doi.org/10.1186/s13023-019-1158-6, doi:10.1186/s13023-019-1158-6. This article has 37 citations and is from a peer-reviewed journal.

17. (klausegger2025anovelhomozygous pages 1-2): Alfred Klausegger, Fabian Leditzky, Susanne Krämer, Francis Palisson, María Joao Yubero, Sebastián Véliz, Mark Jean Aan Koh, Ene-Choo Tan, Martin Laimer, Johann Wolfgang Bauer, and Ignacia Fuentes. A novel homozygous 9385 bp deletion in the fermt1 (kind1) gene in a malaysian family with kindler epidermolysis bullosa and a review of large deletions. International Journal of Molecular Sciences, 26:4237, Apr 2025. URL: https://doi.org/10.3390/ijms26094237, doi:10.3390/ijms26094237. This article has 0 citations.

18. (carrasco2024involvementofkindlin1 pages 1-2): Giovana Carrasco, Ifigeneia Stavrou, Mairi Treanor-Taylor, Henry Beetham, Martin Lee, Roza Masalmeh, Artur Carreras-Soldevila, David Hardman, Miguel O. Bernabeu, Alex von Kriegsheim, Gareth J. Inman, Adam Byron, and Valerie G. Brunton. Involvement of kindlin-1 in cutaneous squamous cell carcinoma. Oncogenesis, Jul 2024. URL: https://doi.org/10.1038/s41389-024-00526-1, doi:10.1038/s41389-024-00526-1. This article has 3 citations and is from a domain leading peer-reviewed journal.

19. (suru2024epidemiologicalcharacteristicsof pages 10-12): Alina Suru, Sorina Dănescu, Alina Călinescu-Stîncanu, Denis Iorga, Mihai Dascălu, Adrian Baican, George-Sorin Țiplica, and Carmen Maria Sălăvăstru. Epidemiological characteristics of inherited epidermolysis bullosa in an eastern european population. Journal of Clinical Medicine, 13:3742, Jun 2024. URL: https://doi.org/10.3390/jcm13133742, doi:10.3390/jcm13133742. This article has 6 citations.

20. (suru2024epidemiologicalcharacteristicsof pages 1-2): Alina Suru, Sorina Dănescu, Alina Călinescu-Stîncanu, Denis Iorga, Mihai Dascălu, Adrian Baican, George-Sorin Țiplica, and Carmen Maria Sălăvăstru. Epidemiological characteristics of inherited epidermolysis bullosa in an eastern european population. Journal of Clinical Medicine, 13:3742, Jun 2024. URL: https://doi.org/10.3390/jcm13133742, doi:10.3390/jcm13133742. This article has 6 citations.

21. (murashkin2024congenitalepidermolysisbullosa pages 1-2): Nikolay N. Murashkin, Roman V. Epishev, Olga S. Orlova, Alena А. Kuratova, and Victoriya S. Polenova. Congenital epidermolysis bullosa epidemiology among children of russian federation. Current Pediatrics, 23:316-328, Oct 2024. URL: https://doi.org/10.15690/vsp.v23i5.2808, doi:10.15690/vsp.v23i5.2808. This article has 2 citations.

22. (murashkin2024congenitalepidermolysisbullosa pages 2-3): Nikolay N. Murashkin, Roman V. Epishev, Olga S. Orlova, Alena А. Kuratova, and Victoriya S. Polenova. Congenital epidermolysis bullosa epidemiology among children of russian federation. Current Pediatrics, 23:316-328, Oct 2024. URL: https://doi.org/10.15690/vsp.v23i5.2808, doi:10.15690/vsp.v23i5.2808. This article has 2 citations.

23. (NCT03068780 chunk 1):  Phase III Efficacy and Safety Study of Oleogel-S10 in Epidermolysis Bullosa. Amryt Research Limited. 2017. ClinicalTrials.gov Identifier: NCT03068780

24. (ussar2008lossofkindlin1 pages 1-2): Siegfried Ussar, Markus Moser, Moritz Widmaier, Emanuel Rognoni, Christian Harrer, Orsolya Genzel-Boroviczeny, and Reinhard Fässler. Loss of kindlin-1 causes skin atrophy and lethal neonatal intestinal epithelial dysfunction. PLoS Genetics, 4:e1000289, Dec 2008. URL: https://doi.org/10.1371/journal.pgen.1000289, doi:10.1371/journal.pgen.1000289. This article has 257 citations and is from a domain leading peer-reviewed journal.

25. (ussar2008lossofkindlin1 pages 2-3): Siegfried Ussar, Markus Moser, Moritz Widmaier, Emanuel Rognoni, Christian Harrer, Orsolya Genzel-Boroviczeny, and Reinhard Fässler. Loss of kindlin-1 causes skin atrophy and lethal neonatal intestinal epithelial dysfunction. PLoS Genetics, 4:e1000289, Dec 2008. URL: https://doi.org/10.1371/journal.pgen.1000289, doi:10.1371/journal.pgen.1000289. This article has 257 citations and is from a domain leading peer-reviewed journal.

26. (natsuga2010animalmodelsof pages 2-4): Ken Natsuga, Satoru Shinkuma, Wataru Nishie, and Hiroshi Shimizu. Animal models of epidermolysis bullosa. Dermatologic clinics, 28 1:137-42, Jan 2010. URL: https://doi.org/10.1016/j.det.2009.10.016, doi:10.1016/j.det.2009.10.016. This article has 32 citations and is from a peer-reviewed journal.
