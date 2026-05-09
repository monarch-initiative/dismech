---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T18:56:52.927732'
end_time: '2026-05-08T19:11:49.918148'
duration_seconds: 896.99
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Gitelman syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 20
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Gitelman syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Gitelman syndrome** covering all of the
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
- **Disease Name:** Gitelman syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Gitelman syndrome** covering all of the
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


## Comprehensive disease characteristics report: Gitelman syndrome (Mendelian tubulopathy)

### Executive summary (current understanding)
Gitelman syndrome (GS) is a **rare, recessively inherited salt-losing tubulopathy** characterized by **hypokalemic metabolic alkalosis with hypomagnesemia and hypocalciuria**, caused by **biallelic inactivating variants in SLC12A3**, which encodes the thiazide-sensitive sodium–chloride cotransporter (**NCC/NCCT**) expressed in the distal convoluted tubule (DCT) (blanchard2017gitelmansyndromeconsensus pages 1-2, fujimura2019clinicalandgenetic pages 1-2, thimm2024untanglingtheuncertain pages 1-2). GS is clinically important because chronic potassium and magnesium depletion can substantially reduce quality of life and can precipitate **cardiac arrhythmias**, including rare life-threatening events (blanchard2017gitelmansyndromeconsensus pages 4-5, zieg2023suddencardiacarrest pages 1-2).

A compact evidence-backed summary table is provided below.

| Topic | Summary | Source (year; journal) | DOI/URL | Evidence type |
|---|---|---|---|---|
| Disease name / synonyms | **Gitelman syndrome (GS)**; also referred to as **familial hypokalemia-hypomagnesemia** in KDIGO and review literature (blanchard2017gitelmansyndromeconsensus pages 1-2, thimm2024untanglingtheuncertain pages 1-2) | Blanchard et al. 2017; *Kidney International* (blanchard2017gitelmansyndromeconsensus pages 1-2) | https://doi.org/10.1016/j.kint.2016.09.046 | Guideline / consensus |
| Inheritance | **Autosomal recessive / recessively inherited** salt-losing tubulopathy caused by **biallelic inactivating variants** (blanchard2017gitelmansyndromeconsensus pages 1-2, thimm2024untanglingtheuncertain pages 1-2) | Blanchard et al. 2017; *Kidney International* (blanchard2017gitelmansyndromeconsensus pages 1-2) | https://doi.org/10.1016/j.kint.2016.09.046 | Guideline / consensus |
| Causal gene / protein | **SLC12A3** encodes the **thiazide-sensitive sodium-chloride cotransporter (NCC/NCCT)** in the **apical membrane of distal convoluted tubule cells**; loss of function causes GS (blanchard2017gitelmansyndromeconsensus pages 1-2, thimm2024untanglingtheuncertain pages 1-2, fujimura2019clinicalandgenetic pages 1-2) | Blanchard et al. 2017; *Kidney International* (blanchard2017gitelmansyndromeconsensus pages 1-2) | https://doi.org/10.1016/j.kint.2016.09.046 | Guideline / consensus |
| Key biochemical hallmarks | Core biochemical pattern: **chronic hypokalemia**, **metabolic alkalosis**, **hypomagnesemia**, **hypocalciuria**, often with **hyperreninemic hyperaldosteronism** and normotension; KDIGO notes hypocalciuria and hypomagnesemia are highly predictive though variable (blanchard2017gitelmansyndromeconsensus pages 1-2, blanchard2017gitelmansyndromeconsensus pages 4-5, zieg2023suddencardiacarrest pages 1-2) | Blanchard et al. 2017; *Kidney International* (blanchard2017gitelmansyndromeconsensus pages 1-2) | https://doi.org/10.1016/j.kint.2016.09.046 | Guideline / consensus |
| Prevalence estimate (general / mainly European ancestry) | KDIGO review: prevalence **~1 to 10 per 40,000**; described as arguably the most frequent inherited tubulopathy (blanchard2017gitelmansyndromeconsensus pages 1-2) | Blanchard et al. 2017; *Kidney International* (blanchard2017gitelmansyndromeconsensus pages 1-2) | https://doi.org/10.1016/j.kint.2016.09.046 | Guideline / consensus |
| Prevalence estimate (case report literature) | Pediatric case report/literature review cites prevalence **~25 per million** (zieg2023suddencardiacarrest pages 1-2) | Zieg et al. 2023; *Frontiers in Pediatrics* (zieg2023suddencardiacarrest pages 1-2) | https://doi.org/10.3389/fped.2023.1188098 | Case report / literature review |
| Prevalence estimate (Caucasian / Asian populations) | 2024 review states estimated prevalence **1:40,000 in Caucasian individuals** and **~1.7 per 1000** in an Asian population; review also gives **OMIM 263800** (thimm2024untanglingtheuncertain pages 1-2) | Thimm & Adjaye 2024; *International Journal of Molecular Sciences* (thimm2024untanglingtheuncertain pages 1-2) | https://doi.org/10.3390/ijms25179332 | Review |
| Genetic spectrum | KDIGO: **>350 SLC12A3 mutations** reported; many patients are compound heterozygotes; some clinically diagnosed patients carry only one detected pathogenic variant on routine testing (blanchard2017gitelmansyndromeconsensus pages 1-2). Japanese cohort notes **~500 different mutations** reported, including nonsense, splice-site, and missense (fujimura2019clinicalandgenetic pages 1-2) | Fujimura et al. 2019; *Kidney International Reports* (fujimura2019clinicalandgenetic pages 1-2) | https://doi.org/10.1016/j.ekir.2018.09.015 | Cohort |
| Cohort clinical anchors | In 185 genetically proven Japanese cases, diagnosis followed **chance blood tests (54.7%)**, **tetany (32.6%)**, **short stature (7.2%)**; median **serum K 2.5 mEq/L** and **serum Mg 1.6 mg/dL** (fujimura2019clinicalandgenetic pages 1-2) | Fujimura et al. 2019; *Kidney International Reports* (fujimura2019clinicalandgenetic pages 1-2) | https://doi.org/10.1016/j.ekir.2018.09.015 | Cohort |
| Real-world diagnostic genetics update | Long-read sequencing study found a second likely pathogenic/pathogenic variant in **45/67 (67%)** patients with previously monoallelic/unsolved GS; **16/45** resolved cases involved intronic variants outside canonical splice sites, supporting second-tier long-read testing (blanchard2017gitelmansyndromeconsensus pages 4-5) | Viering et al. 2023; *Journal of the American Society of Nephrology* (blanchard2017gitelmansyndromeconsensus pages 4-5) | https://doi.org/10.1681/ASN.2022050627 | Cohort / diagnostic study |
| Key guideline / consensus source | **KDIGO Controversies Conference consensus** recommends diagnosis based on biochemical phenotype plus genetic testing; management with **liberal salt intake** and **oral magnesium and potassium supplementation**; gene panels should include **SLC12A3, CLCNKB, HNF1B** at minimum (blanchard2017gitelmansyndromeconsensus pages 4-5, blanchard2017gitelmansyndromeconsensus pages 1-2) | Blanchard et al. 2017; *Kidney International* (blanchard2017gitelmansyndromeconsensus pages 4-5) | https://doi.org/10.1016/j.kint.2016.09.046 | Guideline / consensus |
| Additional management source | Modified-release **magnesium lactate** cohort: **89%** preferred the regimen, **68%** reported improved symptom burden, and biochemistry improved in **91%** of continuing patients switched from other preparations (robinson2017magnesiumlactatein pages 2-3) | Robinson & Karet Frankl 2017; *Nephrology Dialysis Transplantation* (robinson2017magnesiumlactatein pages 2-3) | https://doi.org/10.1093/ndt/gfw019 | Cohort / patient-reported outcomes |


*Table: This table compacts the most actionable disease-level facts for Gitelman syndrome: name/synonyms, inheritance, causal gene and transporter, hallmark biochemistry, prevalence estimates across populations, and the main consensus/guideline and cohort sources supporting diagnosis and management.*

---

## 1. Disease information

### 1.1 What is the disease?
**Definition/overview.** KDIGO consensus defines GS as “a rare, salt-losing tubulopathy characterized by hypokalemic metabolic alkalosis with hypomagnesemia and hypocalciuria” and caused by inactivating SLC12A3 variants encoding NCC (blanchard2017gitelmansyndromeconsensus pages 1-2).

**Typical clinical context.** GS is often detected in adolescence/adulthood, sometimes incidentally or with nonspecific neuromuscular symptoms (fatigue, weakness, cramps), but severe manifestations can occur (blanchard2017gitelmansyndromeconsensus pages 1-2, fujimura2019clinicalandgenetic pages 1-2).

### 1.2 Key identifiers
* **OMIM:** **263800** (explicitly stated in a 2024 review) (thimm2024untanglingtheuncertain pages 1-2).
* **MONDO / Orphanet (Orpha code) / ICD-10/ICD-11 / MeSH:** Not extractable from the retrieved full-text evidence in this run; therefore, no evidence-backed identifiers can be asserted here.

### 1.3 Synonyms / alternative names
* “**familial hypokalemia–hypomagnesemia**” (thimm2024untanglingtheuncertain pages 1-2, blanchard2017gitelmansyndromeconsensus pages 1-2).

### 1.4 Evidence provenance (patient-level vs aggregated)
Evidence used here includes: an international consensus/guideline document (aggregated expert consensus) (blanchard2017gitelmansyndromeconsensus pages 1-2), a national cohort (aggregated observational clinical data) (fujimura2019clinicalandgenetic pages 1-2), a case report with literature review (patient-level + literature synthesis) (zieg2023suddencardiacarrest pages 1-2), a patient-reported outcomes cohort (robinson2017magnesiumlactatein pages 2-3), and an experimental iPSC-organoid study (in vitro model) (lim2023crisprcas9mediatedcorrectionof pages 2-6).

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause (genetic/mechanistic).** GS is caused by **biallelic inactivating pathogenic variants in SLC12A3**, leading to loss of function of NCC/NCCT in the DCT (blanchard2017gitelmansyndromeconsensus pages 1-2, fujimura2019clinicalandgenetic pages 1-2, thimm2024untanglingtheuncertain pages 1-2).

**Variant spectrum (classes).** A 2024 review summarizes that >350 distinct SLC12A3 mutations have been described and provides approximate distribution: missense/nonsense (~62.1%), splice (~13–14%), and small deletions (~12%), with other/large rearrangements comprising the remainder (thimm2024untanglingtheuncertain pages 2-4). A Japanese cohort paper notes ~500 different SLC12A3 mutations have been reported, including nonsense, splice-site, and missense variants (fujimura2019clinicalandgenetic pages 1-2).

### 2.2 Risk factors
* **Genetic risk:** Having **biallelic** pathogenic variants in SLC12A3 is causal (blanchard2017gitelmansyndromeconsensus pages 1-2, thimm2024untanglingtheuncertain pages 1-2).
* **Non-genetic “mimics” (important diagnostic risk context):** KDIGO notes a GS-like phenotype can occur with mutations in other genes (e.g., CLCNKB for classic Bartter type III), which increases misclassification risk without genetic testing (blanchard2017gitelmansyndromeconsensus pages 1-2).

### 2.3 Protective factors
No evidence-backed protective genetic or environmental factors were identified in the retrieved corpus.

### 2.4 Gene–environment interactions
No direct gene–environment interaction studies were retrieved in the accessible evidence. Clinically, intercurrent illness and/or medication/exposure patterns can unmask or exacerbate electrolyte derangements, but robust GxE evidence is not established in the cited texts.

---

## 3. Phenotypes

### 3.1 Core phenotype types
**Laboratory abnormalities (hallmark).** Chronic hypokalemia, metabolic alkalosis, hypomagnesemia, and hypocalciuria are core, with renin–aldosterone system activation typical; normotension/low blood pressure is common (blanchard2017gitelmansyndromeconsensus pages 1-2, thimm2024untanglingtheuncertain pages 1-2, zieg2023suddencardiacarrest pages 1-2).

**Symptoms/signs.** KDIGO lists salt craving; muscle weakness/fatigue; limited endurance; episodes of fainting; cramps/tetany/paresthesia/carpopedal spasms; growth retardation/puberty delay/short stature; thirst/abnormal drinking; abdominal pain, with dizziness/vertigo/polyuria/nocturia/palpitations/joint pain/visual problems sometimes in adults (blanchard2017gitelmansyndromeconsensus pages 1-2).

### 3.2 Phenotype characteristics (age, severity, frequencies)
**Age at onset.** GS can present in childhood and occasionally neonatally, but often becomes clinically apparent later; a 2023 pediatric case/literature review states typical onset is after age 6 years but neonatal cases exist (zieg2023suddencardiacarrest pages 1-2). KDIGO likewise notes adolescent/adult presentation is common (blanchard2017gitelmansyndromeconsensus pages 1-2).

**Cohort statistics (Japan, n=185 genetically proven).**
* Diagnostic opportunity: **chance blood test 54.7%**, **tetany 32.6%**, **short stature 7.2%** (fujimura2019clinicalandgenetic pages 1-2).
* Complications: **short stature 16.3%**, **febrile convulsion 13.7%**, **thyroid dysfunction 4.3%**, **epilepsy 2.5%**; **QT prolongation detected in one case** (fujimura2019clinicalandgenetic pages 1-2).
* Biochemical medians (same cohort): serum **K 2.5 mEq/L** (range 1.2–3.8), serum **Mg 1.6 mg/dL** (range 0.6–2.7) (fujimura2019clinicalandgenetic pages 1-2).

### 3.3 Quality-of-life impact
KDIGO consensus explicitly states GS is associated with “a significant reduction in the quality of life” (blanchard2017gitelmansyndromeconsensus pages 1-2). A patient-reported outcomes cohort switching to slow-release magnesium lactate found high preference and symptom improvement (see Treatment section) (robinson2017magnesiumlactatein pages 2-3).

### 3.4 Suggested HPO terms (non-exhaustive)
Evidence-backed phenotype mapping to HPO is not directly provided in the retrieved papers; the following are **suggested** mappings based on the cited clinical descriptions:
* Hypokalemia (**HP:0002900**)
* Hypomagnesemia (**HP:0002917**)
* Metabolic alkalosis (**HP:0001940**)
* Hypocalciuria (**HP:0012073**, if available in your HPO version)
* Muscle weakness (**HP:0001324**)
* Muscle cramps (**HP:0003394**)
* Tetany (**HP:0001285**)
* Paresthesia (**HP:0003401**)
* Salt craving (**HP term may vary; often annotated as abnormal food craving**)
* Short stature (**HP:0004322**)
* Cardiac arrhythmia (**HP:0011675**)
* Prolonged QT interval (**HP:0001657**)

---

## 4. Genetic / molecular information

### 4.1 Causal genes
* **SLC12A3** (encodes NCC/NCCT), expressed at the apical membrane of DCT cells (blanchard2017gitelmansyndromeconsensus pages 1-2, thimm2024untanglingtheuncertain pages 1-2).

### 4.2 Pathogenic variants
**Variant types.** Missense/nonsense are the largest class; splice variants and small deletions are also substantial contributors (thimm2024untanglingtheuncertain pages 2-4). KDIGO notes larger rearrangements/deletions can occur and may require MLPA for detection (blanchard2017gitelmansyndromeconsensus pages 4-5).

**Monoallelic findings and “missing second allele.”** KDIGO states that in **15–20%** of patients, only one pathogenic mutation is found on routine testing, partly due to noncoding/intronic mutations or other mechanisms (blanchard2017gitelmansyndromeconsensus pages 4-5). A large sequencing cohort preprint reported that WGS in monoallelic cases can detect deep intronic splice-gain variants and small exonic deletions missed by WES, while estimating that truly noncoding pathogenic alleles are a small fraction of all SLC12A3 alleles in that referral cohort (aparicio2025mutationsin329 pages 1-3, aparicio2025mutationsin329 pages 14-16). (Note: this specific cohort is 2025 and preprint status.)

**Example pathogenic variants (case-level).** A pediatric sudden cardiac arrest case identified two pathogenic SLC12A3 variants: **c.2633+1G>A** and **c.2221G>A** (zieg2023suddencardiacarrest pages 1-2).

### 4.3 Genotype–phenotype correlations / modifiers
In the Japanese cohort (n=185), carriers of common hotspot variants **p.Arg642Cys and/or p.Leu858His** had significantly higher serum magnesium compared with those without these variants (**1.76 vs 1.43 mg/dL; P<0.001**), supporting variant-dependent phenotypic modulation (fujimura2019clinicalandgenetic pages 1-2).

Strong evidence for independent **modifier genes** was not identified in the retrieved evidence beyond case-level comorbidity reports.

### 4.4 Epigenetic information / chromosomal abnormalities
No GS-specific epigenetic signature or recurrent chromosomal abnormalities were identified in the retrieved evidence. (Epigenetic assays are mainly discussed in differential diagnoses rather than GS itself in available evidence.)

---

## 5. Environmental information
No environmental toxin, infectious, or lifestyle causes are established for GS in the retrieved evidence. Environmental/behavioral factors are primarily important as **phenocopies** (e.g., medication-induced renal wasting) or triggers of symptomatic episodes rather than etiologic causes.

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (gene → transporter defect → biochemical phenotype → symptoms)
1. **Biallelic SLC12A3 loss-of-function** reduces NCC-mediated NaCl reabsorption in DCT cells (blanchard2017gitelmansyndromeconsensus pages 1-2, thimm2024untanglingtheuncertain pages 1-2).
2. Reduced NaCl reabsorption causes **renal salt wasting**, leading to **volume contraction** and compensatory activation of the **renin–angiotensin–aldosterone system (RAAS)** (thimm2024untanglingtheuncertain pages 2-4, thimm2024untanglingtheuncertain pages 1-2).
3. RAAS activation increases distal sodium reabsorption in exchange for **potassium and hydrogen secretion**, causing **hypokalemia and metabolic alkalosis** (zieg2023suddencardiacarrest pages 1-2, thimm2024untanglingtheuncertain pages 1-2).
4. GS features **renal magnesium wasting** with resultant hypomagnesemia; clinically, hypomagnesemia can worsen hypokalemia and contribute to symptoms (blanchard2017gitelmansyndromeconsensus pages 4-5, thimm2024untanglingtheuncertain pages 1-2).
5. Low K/Mg can prolong the cardiac action potential and QT interval; KDIGO notes prolonged QT “in ~50% of the patients” and recommends ECG screening, acknowledging rare ventricular tachycardia/sudden death reports (blanchard2017gitelmansyndromeconsensus pages 4-5). A pediatric case report documents ventricular fibrillation/sudden cardiac arrest in GS without a precipitating event (zieg2023suddencardiacarrest pages 1-2).

### 6.2 Molecular pathways and processes (suggested ontology mappings)
Evidence emphasizes renal electrolyte transport and RAAS physiology (thimm2024untanglingtheuncertain pages 1-2, thimm2024untanglingtheuncertain pages 2-4). Suggested GO terms:
* **GO:0006811 ion transport**
* **GO:0006814 sodium ion transport**
* **GO:0071436 sodium ion transmembrane transport**
* **GO:0006820 anion transport / chloride transport**
* **GO:0006874 cellular calcium ion homeostasis** (downstream DCT effects)
* **GO:0008202 steroid metabolic process** (aldosterone physiology; contextual)

Cell types (suggested CL terms):
* **Distal convoluted tubule epithelial cell** (kidney tubule epithelial cell subtype; CL term depends on ontology version) (blanchard2017gitelmansyndromeconsensus pages 1-2, thimm2024untanglingtheuncertain pages 1-2).

### 6.3 Immune system involvement
A 2024 review (aging/RAAS framing) states in its abstract that “Individuals with sodium deficiency-associated diseases such as Gitelman syndrome (GS) and Bartter syndrome (BS) show **downregulation of inflammation-related processes** and have **reduced oxidative stress and ROS**,” and that GS/BS patients sustain higher SIRT1 activity (thimm2024untanglingtheuncertain pages 1-2). These are mechanistic hypotheses from review-level synthesis rather than GS-specific causal immune pathology.

### 6.4 Molecular profiling / advanced technologies (latest research)
**Patient-derived iPSC kidney organoids + CRISPR correction (2023).** A 2023 study generated patient-derived hiPSCs with SLC12A3 mutations and differentiated them into kidney organoids, then used CRISPR/Cas9 to correct the mutation and assess phenotype rescue. Quantitatively, the “number of matured kidney organoids” was lower in patient organoids than control (**3.7 ± 0.2/cm² vs 16.7 ± 1.3/cm²**), and was partially restored after correction (**12.2 ± 0.7/cm² vs 3.7 ± 0.2/cm²**) (lim2023crisprcas9mediatedcorrectionof pages 2-6). This provides an in vitro platform for functional validation and potential future therapeutic exploration.

---

## 7. Anatomical structures affected

### 7.1 Primary organs / systems
* **Kidney**, especially the **distal convoluted tubule (DCT)**, is the primary affected structure (blanchard2017gitelmansyndromeconsensus pages 1-2, thimm2024untanglingtheuncertain pages 1-2).
* Secondary system impacts include **neuromuscular** (cramps, tetany, weakness), **cardiac electrophysiology** (QT prolongation/arrhythmias), and endocrine/other complications (short stature, thyroid dysfunction) (blanchard2017gitelmansyndromeconsensus pages 1-2, fujimura2019clinicalandgenetic pages 1-2, blanchard2017gitelmansyndromeconsensus pages 4-5).

### 7.2 Suggested UBERON terms
* Kidney (**UBERON:0002113**)
* Distal convoluted tubule (**UBERON:0001285**, depending on ontology version)

### 7.3 Subcellular localization (suggested GO Cellular Component)
NCC/NCCT is localized to the **apical membrane** of DCT epithelial cells (blanchard2017gitelmansyndromeconsensus pages 1-2, thimm2024untanglingtheuncertain pages 1-2). Suggested GO CC term: **GO:0016324 apical plasma membrane**.

---

## 8. Temporal development

### Onset
Typically adolescent/adult detection, but childhood and even neonatal presentation can occur (blanchard2017gitelmansyndromeconsensus pages 1-2, zieg2023suddencardiacarrest pages 1-2).

### Progression / course
GS is generally chronic and lifelong, requiring ongoing management. KDIGO highlights high phenotypic variability and potential severity; long-term monitoring is implied by consensus follow-up recommendations, including cardiac monitoring in relevant patients (blanchard2017gitelmansyndromeconsensus pages 1-2, blanchard2017gitelmansyndromeconsensus pages 4-5).

---

## 9. Inheritance and population

### 9.1 Inheritance
**Autosomal recessive** (biallelic SLC12A3 pathogenic variants) (blanchard2017gitelmansyndromeconsensus pages 1-2, thimm2024untanglingtheuncertain pages 1-2).

### 9.2 Epidemiology (statistics)
Reported prevalence estimates vary by source/population:
* KDIGO (2017): “prevalence at ~1 to 10 per 40,000, and potentially higher in Asia” (blanchard2017gitelmansyndromeconsensus pages 1-2).
* Review (2024): “estimated prevalence of **1:40,000** Caucasian individuals” and “estimated at around **1.7 per 1000** people” in an Asian population (thimm2024untanglingtheuncertain pages 1-2).
* Pediatric case/literature review (2023): ~“**25 per million**” (zieg2023suddencardiacarrest pages 1-2).

Carrier frequency and founder effects were not extractable from Orphanet/gnomAD-like sources in this run; therefore they are not asserted.

---

## 10. Diagnostics

### 10.1 Clinical and laboratory evaluation
KDIGO proposes biochemical criteria for suspecting GS (Table 2), which include chronic hypokalemia and associated features. The consensus emphasizes that hypocalciuria plus hypomagnesemia is “highly predictive” though both can be variable (blanchard2017gitelmansyndromeconsensus pages 1-2). A cropped image of this diagnostic criteria table is included as visual evidence (blanchard2017gitelmansyndromeconsensus media 4476f44a).

### 10.2 Genetic testing (real-world workflows)
KDIGO recommends next-generation sequencing (NGS) diagnostic approaches, noting gene panels should include **SLC12A3, CLCNKB, and HNF1B** at minimum to address phenotypic overlap and differential diagnosis (blanchard2017gitelmansyndromeconsensus pages 4-5). KDIGO also notes that routine genetic testing can miss noncoding/intronic variants and larger rearrangements, supporting extended analyses (e.g., MLPA) when only one allele is found (blanchard2017gitelmansyndromeconsensus pages 4-5).

### 10.3 Differential diagnosis (key mimics)
GS-like phenotypes can be caused by **CLCNKB** variants (classic Bartter syndrome type III) due to overlap at the DCT; other tubulopathies and genetic disorders can mimic GS clinically and biochemically, making molecular testing important for resolution in ambiguous cases (blanchard2017gitelmansyndromeconsensus pages 1-2).

---

## 11. Outcome / prognosis

### 11.1 Survival and mortality
No cohort-derived survival curves or life expectancy estimates were retrieved in accessible evidence.

### 11.2 Morbidity and complications
* **Cardiac electrophysiology risk.** KDIGO states K/Mg depletion can prolong action potential duration and QT interval (noting prolonged QT in ~50% of patients), with isolated reports of ventricular tachycardia and sudden death, motivating ECG surveillance (blanchard2017gitelmansyndromeconsensus pages 4-5).
* **Severe arrhythmia case evidence (2023).** A 10-year-old child experienced ventricular fibrillation and sudden cardiac arrest attributed to severe hypokalemia, with subsequent ICD placement and stabilization with electrolyte therapy (zieg2023suddencardiacarrest pages 1-2).
* **Extrarenal complications (cohort).** Short stature, febrile convulsions, thyroid dysfunction, epilepsy, and QT prolongation are documented with frequencies in the Japanese cohort (fujimura2019clinicalandgenetic pages 1-2).

---

## 12. Treatment

### 12.1 Standard management (real-world implementation)
KDIGO consensus indicates GS is “usually managed by a **liberal salt intake** together with **oral magnesium and potassium supplements**” (blanchard2017gitelmansyndromeconsensus pages 1-2). KDIGO further notes that hypomagnesemia can aggravate and render hypokalemia refractory, supporting combined replacement strategies (blanchard2017gitelmansyndromeconsensus pages 4-5).

**Arrhythmia risk management.** KDIGO recommends resting ECG, with further cardiology evaluation for symptoms or high-risk features (blanchard2017gitelmansyndromeconsensus pages 4-5).

### 12.2 Evidence on magnesium formulation: patient-reported outcomes
A specialist-clinic cohort study evaluated slow-release magnesium lactate in genetically proven GS (n=28). Key statistics reported include:
* “almost **90%** (n=25) choosing to continue long term” (robinson2017magnesiumlactatein pages 2-3).
* Side effects vs prior Mg: **59%** reported fewer side effects, **32%** same, **9%** worse (robinson2017magnesiumlactatein pages 2-3).
The authors’ abstract further reports preference and symptom/biochemical improvement rates (89% preference; 68% symptom improvement among those preferring; biochemical improvement in 91% of continuing patients switched from other preparations) (robinson2017magnesiumlactatein pages 2-3).

### 12.3 MAXO (Medical Action Ontology) suggestions (non-exhaustive)
* Oral potassium supplementation
* Oral magnesium supplementation
* Dietary sodium chloride supplementation (liberal salt intake)
* Electrocardiographic monitoring
* Genetic testing / gene panel testing

(These are ontology mapping suggestions; MAXO IDs were not provided in the retrieved evidence.)

### 12.4 Experimental/advanced therapeutics (research stage)
The iPSC kidney organoid + CRISPR correction study demonstrates proof-of-concept **gene correction rescuing organoid phenotype metrics**, providing “therapeutic insight” at a preclinical stage (lim2023crisprcas9mediatedcorrectionof pages 2-6).

### 12.5 Clinical trials
ClinicalTrials.gov entries were retrieved by the tool, but the trial text chunks returned were not added to the evidence store with citable context IDs in this run; therefore, trial identifiers and outcomes are not cited here.

---

## 13. Prevention
Primary prevention of an autosomal recessive monogenic disorder is not generally feasible outside reproductive genetics.

**Genetic counseling and reproductive options.** KDIGO notes genetic counseling is recommended and that prenatal/preimplantation testing is technically feasible when two pathogenic variants are identified (blanchard2017gitelmansyndromeconsensus pages 4-5).

**Secondary/tertiary prevention.** Early identification and electrolyte management aim to prevent complications such as arrhythmias (blanchard2017gitelmansyndromeconsensus pages 4-5, zieg2023suddencardiacarrest pages 1-2).

---

## 14. Other species / natural disease
No naturally occurring GS in non-human species was identified in the retrieved evidence.

---

## 15. Model organisms and in vitro models

### 15.1 In vitro patient-derived models (2023 development)
The patient-derived iPSC kidney organoid system with CRISPR correction provides a human-cell-based model for GS, including quantitative phenotypes (organoid maturation counts) that respond to gene correction (lim2023crisprcas9mediatedcorrectionof pages 2-6).

### 15.2 Suggested model utility
* Functional validation of candidate SLC12A3 variants
* Testing strategies to restore NCC expression/function in DCT-like compartments

---

## Evidence excerpt quotes (as requested; from abstracts/full text)
* KDIGO opening definition: “Gitelman syndrome (GS) is a rare, salt-losing tubulopathy characterized by hypokalemic metabolic alkalosis with hypomagnesemia and hypocalciuria.” (blanchard2017gitelmansyndromeconsensus pages 1-2)
* 2024 review abstract statement: “Individuals with sodium deficiency-associated diseases such as Gitelman syndrome (GS) and Bartter syndrome (BS) show downregulation of inflammation-related processes and have reduced oxidative stress and ROS.” (thimm2024untanglingtheuncertain pages 1-2)
* Magnesium lactate cohort (full text): “patient responses were very positive regarding SRMgL, with almost 90% (n = 25) choosing to continue long term” (robinson2017magnesiumlactatein pages 2-3).

---

## Limitations of this report (evidence availability)
* **Orphanet (Orpha code), ICD-10/ICD-11, MeSH, MONDO IDs** were not present in the retrieved full-text evidence; they therefore cannot be asserted with citations here.
* Cohort-level **incidence**, **mortality**, and robust **carrier-frequency** estimates from population databases were not available in the cited sources.
* Clinical trial identifiers were retrieved by the tools, but not in a way that produced citable context IDs for this final report.


References

1. (blanchard2017gitelmansyndromeconsensus pages 1-2): Anne Blanchard, Detlef Bockenhauer, Davide Bolignano, Lorenzo A Calò, Etienne Cosyns, Olivier Devuyst, David H Ellison, Fiona E Karet Frankl, Nine VAM Knoers, Martin Konrad, Shih-Hua Lin, and Rosa Vargas-Poussou. Gitelman syndrome: consensus and guidance from a kidney disease: improving global outcomes (kdigo) controversies conference. Kidney international, 91 1:24-33, Feb 2017. URL: https://doi.org/10.1016/j.kint.2016.09.046, doi:10.1016/j.kint.2016.09.046. This article has 443 citations and is from a highest quality peer-reviewed journal.

2. (fujimura2019clinicalandgenetic pages 1-2): Junya Fujimura, Kandai Nozu, Tomohiko Yamamura, Shogo Minamikawa, Keita Nakanishi, Tomoko Horinouchi, China Nagano, Nana Sakakibara, Koichi Nakanishi, Yuko Shima, Kenichi Miyako, Yoshimi Nozu, Naoya Morisada, Hiroaki Nagase, Takeshi Ninchoji, Hiroshi Kaito, and Kazumoto Iijima. Clinical and genetic characteristics in patients with gitelman syndrome. Kidney International Reports, 4:119-125, Jan 2019. URL: https://doi.org/10.1016/j.ekir.2018.09.015, doi:10.1016/j.ekir.2018.09.015. This article has 98 citations and is from a peer-reviewed journal.

3. (thimm2024untanglingtheuncertain pages 1-2): Chantelle Thimm and James Adjaye. Untangling the uncertain role of overactivation of the renin–angiotensin–aldosterone system with the aging process based on sodium wasting human models. International Journal of Molecular Sciences, 25:9332, Aug 2024. URL: https://doi.org/10.3390/ijms25179332, doi:10.3390/ijms25179332. This article has 6 citations.

4. (blanchard2017gitelmansyndromeconsensus pages 4-5): Anne Blanchard, Detlef Bockenhauer, Davide Bolignano, Lorenzo A Calò, Etienne Cosyns, Olivier Devuyst, David H Ellison, Fiona E Karet Frankl, Nine VAM Knoers, Martin Konrad, Shih-Hua Lin, and Rosa Vargas-Poussou. Gitelman syndrome: consensus and guidance from a kidney disease: improving global outcomes (kdigo) controversies conference. Kidney international, 91 1:24-33, Feb 2017. URL: https://doi.org/10.1016/j.kint.2016.09.046, doi:10.1016/j.kint.2016.09.046. This article has 443 citations and is from a highest quality peer-reviewed journal.

5. (zieg2023suddencardiacarrest pages 1-2): Jakub Zieg, Terezia Tavačová, Miroslava Balaščáková, Petra Peldová, Filip Fencl, and Peter Kubuš. Sudden cardiac arrest in a child with gitelman syndrome: a case report and literature review. Frontiers in Pediatrics, Jun 2023. URL: https://doi.org/10.3389/fped.2023.1188098, doi:10.3389/fped.2023.1188098. This article has 2 citations.

6. (robinson2017magnesiumlactatein pages 2-3): Caroline M. Robinson and Fiona E. Karet Frankl. Magnesium lactate in the treatment of gitelman syndrome: patient-reported outcomes. Nephrology Dialysis Transplantation, 32:508-512, Mar 2017. URL: https://doi.org/10.1093/ndt/gfw019, doi:10.1093/ndt/gfw019. This article has 31 citations and is from a domain leading peer-reviewed journal.

7. (lim2023crisprcas9mediatedcorrectionof pages 2-6): Sun Woo Lim, Xianying Fang, Sheng Cui, Hanbi Lee, Yoo Jin Shin, Eun Jeong Ko, Kang In Lee, Jae Young Lee, Byung Ha Chung, and Chul Woo Yang. Crispr-cas9-mediated correction of slc12a3 gene mutation rescues the gitelman’s disease phenotype in a patient-derived kidney organoid system. International Journal of Molecular Sciences, 24:3019, Feb 2023. URL: https://doi.org/10.3390/ijms24033019, doi:10.3390/ijms24033019. This article has 12 citations.

8. (thimm2024untanglingtheuncertain pages 2-4): Chantelle Thimm and James Adjaye. Untangling the uncertain role of overactivation of the renin–angiotensin–aldosterone system with the aging process based on sodium wasting human models. International Journal of Molecular Sciences, 25:9332, Aug 2024. URL: https://doi.org/10.3390/ijms25179332, doi:10.3390/ijms25179332. This article has 6 citations.

9. (aparicio2025mutationsin329 pages 1-3): Renan Eduardo Aparicio, Sheng Chih Jin, Weilai Dong, Samir Zaidi, Michael C Sierant, James Knight, Robert D Bjornson, Christopher Castaldi, Shrikant M Mane, Thomas M. Kaneko, Carol Nelson-Williams, and Richard P. Lifton. Mutations in 329 probands with suspected renal electrolyte disorders. MedRxiv, May 2025. URL: https://doi.org/10.1101/2025.04.28.25326317, doi:10.1101/2025.04.28.25326317. This article has 0 citations.

10. (aparicio2025mutationsin329 pages 14-16): Renan Eduardo Aparicio, Sheng Chih Jin, Weilai Dong, Samir Zaidi, Michael C Sierant, James Knight, Robert D Bjornson, Christopher Castaldi, Shrikant M Mane, Thomas M. Kaneko, Carol Nelson-Williams, and Richard P. Lifton. Mutations in 329 probands with suspected renal electrolyte disorders. MedRxiv, May 2025. URL: https://doi.org/10.1101/2025.04.28.25326317, doi:10.1101/2025.04.28.25326317. This article has 0 citations.

11. (blanchard2017gitelmansyndromeconsensus media 4476f44a): Anne Blanchard, Detlef Bockenhauer, Davide Bolignano, Lorenzo A Calò, Etienne Cosyns, Olivier Devuyst, David H Ellison, Fiona E Karet Frankl, Nine VAM Knoers, Martin Konrad, Shih-Hua Lin, and Rosa Vargas-Poussou. Gitelman syndrome: consensus and guidance from a kidney disease: improving global outcomes (kdigo) controversies conference. Kidney international, 91 1:24-33, Feb 2017. URL: https://doi.org/10.1016/j.kint.2016.09.046, doi:10.1016/j.kint.2016.09.046. This article has 443 citations and is from a highest quality peer-reviewed journal.
