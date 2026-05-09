---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T22:04:35.278246'
end_time: '2026-05-06T22:13:21.026109'
duration_seconds: 525.75
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pemphigus Erythematosus
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 19
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pemphigus Erythematosus
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Pemphigus Erythematosus** covering all of the
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
- **Disease Name:** Pemphigus Erythematosus
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Pemphigus Erythematosus** covering all of the
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


## Comprehensive Research Report: Pemphigus Erythematosus (Senear–Usher Syndrome)

### Target disease
- **Disease name:** Pemphigus erythematosus (PE)
- **Synonyms:** Senear–Usher syndrome; (historically/ambiguously) “seborrheic pemphigus” (terminology overlaps with seborrheic pemphigus as a PF variant in some clinical literature). (arasiewicz2024senearushersyndromein pages 1-3, espadas2024seborrheicpemphigusa pages 1-3, hobbs2021pemphiguserythematosusa pages 1-2)
- **Category:** Autoimmune blistering disease (intraepidermal), considered a localized/overlap variant of pemphigus foliaceus with lupus-like features. (hobbs2021pemphiguserythematosusa pages 1-2, onalajaunderwood2024diagnosisandmanagement pages 3-7)
- **MONDO ID:** Not identified from the retrieved evidence set. (hobbs2021pemphiguserythematosusa pages 1-2)

---

## 1. Disease Information

### 1.1 Concise overview (current understanding)
Pemphigus erythematosus is a **rare autoimmune blistering disorder** with **overlapping clinical, histopathologic, and immunologic features of pemphigus foliaceus and lupus erythematosus**, often presenting as **erythematous, scaly/crusted plaques** and/or superficial flaccid blisters on seborrheic and photoexposed sites (especially malar face/scalp/upper trunk). (hobbs2021pemphiguserythematosusa pages 1-2, onalajaunderwood2024diagnosisandmanagement pages 1-3)

A central clinicopathologic concept is that PE demonstrates **pemphigus-type intraepidermal acantholysis** plus a **lupus-band–like direct immunofluorescence pattern along the dermal–epidermal junction (DEJ)**. (chandan2018unusuallyextensivescalp pages 4-5, hobbs2021pemphiguserythematosusa pages 1-2)

### 1.2 Key identifiers (knowledge-base fields)
- **ICD-10 / ICD-11:** Not available in retrieved evidence. (hobbs2021pemphiguserythematosusa pages 1-2)
- **MeSH:** Not available in retrieved evidence. (hobbs2021pemphiguserythematosusa pages 1-2)
- **Orphanet:** Not available in retrieved evidence. (hobbs2021pemphiguserythematosusa pages 1-2)
- **OMIM:** Not available in retrieved evidence. (hobbs2021pemphiguserythematosusa pages 1-2)
- **MONDO:** Not available in retrieved evidence. (hobbs2021pemphiguserythematosusa pages 1-2)

### 1.3 Evidence source type
The disease-specific information in this report is derived mainly from **aggregated disease-level synthesis** (a tertiary-center case series + literature review) and **recent case reports/reviews** rather than EHR-scale datasets. (hobbs2021pemphiguserythematosusa pages 1-2, arasiewicz2024senearushersyndromein pages 1-3, jangid2023acasereport pages 1-4)

---

## 2. Etiology

### 2.1 Disease causal factors (mechanistic)
PE is caused by an autoimmune response against desmosomal adhesion molecules (most prominently desmoglein-1), leading to impaired keratinocyte–keratinocyte adhesion (acantholysis) and superficial intraepidermal blistering. (onalajaunderwood2024diagnosisandmanagement pages 1-3, chandan2018unusuallyextensivescalp pages 1-4)

### 2.2 Risk factors
**Genetic (susceptibility):** A genetic predisposition via HLA haplotypes has been suggested; a pediatric PE report mentions HLA haplotypes including **A10/A26 and DRW6** in the context of susceptibility. (arasiewicz2024senearushersyndromein pages 1-3)

**Environmental (exacerbating/triggering):**
- **Ultraviolet (UV) exposure/sunlight** is repeatedly described as an exacerbating factor; a PE case report review notes UV can contribute mechanistically (including desmoglein-1 ectodomain cleavage and immune deposition at the DEJ in UV-exposed skin). (chandan2018unusuallyextensivescalp pages 4-5, onalajaunderwood2024diagnosisandmanagement pages 1-3)

**Medication triggers (class effect for pemphigus; PE-specific evidence limited):** A 2024 bullous disease review lists multiple medications associated with pemphigus (e.g., penicillamine, captopril, propranolol) while discussing pemphigus foliaceus and variants including PE, supporting consideration of drug triggers in susceptible individuals, though PE-specific causal attribution is not established in the retrieved PE-focused data. (onalajaunderwood2024diagnosisandmanagement pages 3-7)

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved evidence set. (hobbs2021pemphiguserythematosusa pages 1-2)

### 2.4 Gene–environment interactions
A plausible gene–environment interaction is **HLA-associated susceptibility** combined with **UV exposure** as a clinical and mechanistic aggravator, but direct studies in PE were not available in the retrieved evidence set. (arasiewicz2024senearushersyndromein pages 1-3, chandan2018unusuallyextensivescalp pages 4-5)

---

## 3. Phenotypes

### 3.1 Core clinical phenotype spectrum
Across a tertiary-center case series and literature review (87 literature cases summarized), common anatomic distributions included **trunk (62%), face (51.7%), extremities (39%), scalp (35.6%)**. (hobbs2021pemphiguserythematosusa pages 2-5)

**Mucosal involvement is uncommon**; pooled oral involvement was ~**9.2%**. (hobbs2021pemphiguserythematosusa pages 2-5)

Common morphologies include erythematous scaly/crusted plaques, superficial erosions, and fragile/flaccid blisters that rupture with crusting. (jangid2023acasereport pages 1-4, hobbs2021pemphiguserythematosusa pages 10-11)

**Course:** A 2024 review characterizes PE as generally chronic and localized to malar and other seborrheic areas. (onalajaunderwood2024diagnosisandmanagement pages 3-7)

### 3.2 Suggested HPO terms (mapping suggestions)
(These are ontology suggestions; the retrieved articles do not provide HPO codes.)
- Erythematous scaly plaques / erythema: **HP:0020116 (Erythema)** (suggested) (hobbs2021pemphiguserythematosusa pages 2-5)
- Blistering: **HP:0030057 (Blistering of the skin)** (suggested) (jangid2023acasereport pages 1-4)
- Skin erosions/crusting: **HP:0100717 (Skin erosion)**; **HP:0200042 (Crusting of skin lesions)** (suggested) (arasiewicz2024senearushersyndromein pages 1-3, jangid2023acasereport pages 1-4)
- Photosensitivity: **HP:0000992 (Photosensitivity)** (suggested) (hobbs2021pemphiguserythematosusa pages 10-11, onalajaunderwood2024diagnosisandmanagement pages 3-7)
- Positive Nikolsky sign (clinical sign; HPO mapping may vary): (suggested) (onalajaunderwood2024diagnosisandmanagement pages 1-3)

### 3.3 Quality-of-life impact
Disease-specific QoL instrument data were not identified for PE in the retrieved evidence set; however, PE is described as causing symptomatic, visible lesions and is discussed as requiring integrated assessment in case-report literature. (jangid2023acasereport pages 6-7)

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes
PE is not a monogenic disorder in the retrieved evidence set; no single causal gene/variant is established. Evidence supports **HLA-associated susceptibility** (immunogenetic predisposition) rather than Mendelian inheritance. (arasiewicz2024senearushersyndromein pages 1-3)

### 4.2 Autoantigens / molecular targets (key disease molecules)
- **Desmoglein 1 (DSG1):** Central autoantigen; a 2024 review describes PF (and variants including PE) as mediated by IgG4 autoantibodies against desmoglein-1. (onalajaunderwood2024diagnosisandmanagement pages 1-3)
- **Desmoglein 3 (DSG3):** Some PE cases have anti-Dsg3 antibodies; PE case reports mention Dsg1 and Dsg3 and other desmosomal proteins. (arasiewicz2024senearushersyndromein pages 1-3, jangid2023acasereport pages 1-4)

### 4.3 Pathogenic variants / allele frequencies
Not applicable based on retrieved evidence; PE evidence focuses on autoantibodies and HLA associations rather than pathogenic variants. (hobbs2021pemphiguserythematosusa pages 1-2)

---

## 5. Environmental Information

### Key environmental factor
- **UV exposure / sunlight:** recurrently described as worsening PE, including a mechanistic explanation involving UV-associated effects on desmoglein-1 and deposition at the DEJ. (chandan2018unusuallyextensivescalp pages 4-5, onalajaunderwood2024diagnosisandmanagement pages 3-7)

No specific infectious trigger was identified in the retrieved evidence set for PE. (hobbs2021pemphiguserythematosusa pages 1-2)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (current model)
1) **Autoantibody production** against desmosomal proteins (especially **DSG1**, sometimes DSG3) occurs in susceptible individuals. (onalajaunderwood2024diagnosisandmanagement pages 1-3, jangid2023acasereport pages 1-4)
2) Binding of autoantibodies to keratinocyte adhesion molecules leads to **loss of intercellular adhesion (acantholysis)**, producing superficial intraepidermal blistering and erosions. (chandan2018unusuallyextensivescalp pages 1-4, hobbs2021pemphiguserythematosusa pages 2-5)
3) PE uniquely shows lupus-like immunopathology, commonly featuring **DEJ immune deposits (IgG/C3)** on direct immunofluorescence (“lupus-band”-like), especially in photoexposed skin. (chandan2018unusuallyextensivescalp pages 4-5, hobbs2021pemphiguserythematosusa pages 10-11)
4) Clinically this yields **erythematous scaly/crusted plaques and superficial erosions** in seborrheic/photoexposed distributions with relatively infrequent mucosal involvement. (hobbs2021pemphiguserythematosusa pages 2-5, onalajaunderwood2024diagnosisandmanagement pages 3-7)

### 6.2 Key immune components
- **IgG4-class autoantibodies to DSG1** are emphasized in PF/variant pathogenesis. (onalajaunderwood2024diagnosisandmanagement pages 1-3)
- **Complement (C3)** deposition is a common DIF feature (intercellular and along DEJ). (hobbs2021pemphiguserythematosusa pages 10-11)

### 6.3 Suggested GO and CL ontology terms (mapping suggestions)
(These are ontology suggestions; the retrieved articles do not provide GO/CL codes.)
- **GO biological processes:** keratinocyte cell–cell adhesion; complement activation; humoral immune response; inflammatory response in skin. (suggested) (hobbs2021pemphiguserythematosusa pages 10-11, onalajaunderwood2024diagnosisandmanagement pages 1-3)
- **CL cell types:** keratinocyte; B cell/plasma cell (autoantibody production). (suggested) (onalajaunderwood2024diagnosisandmanagement pages 1-3)

### 6.4 Molecular profiling / omics
No transcriptomic/proteomic/metabolomic PE-specific profiling was identified in the retrieved evidence set. (hobbs2021pemphiguserythematosusa pages 1-2)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue level
- **Primary:** skin, especially seborrheic and photoexposed regions (malar face, scalp, upper trunk). (onalajaunderwood2024diagnosisandmanagement pages 3-7, hobbs2021pemphiguserythematosusa pages 2-5)
- **Mucosa:** uncommon oral involvement (~9.2% in pooled review). (hobbs2021pemphiguserythematosusa pages 2-5)

### 7.2 Suggested UBERON terms (mapping suggestions)
- Skin (UBERON:0002097), face (UBERON:0001456), scalp (UBERON:0001135), trunk (UBERON:0002100), oral mucosa (UBERON:0000344) (suggested). (hobbs2021pemphiguserythematosusa pages 2-5)

### 7.3 Subcellular level
- Desmosomes/cell junctions are implicated via autoantibody targeting of desmosomal cadherins (desmogleins). (onalajaunderwood2024diagnosisandmanagement pages 1-3)

---

## 8. Temporal Development

### 8.1 Onset
In the Hobbs literature review, age ranged from **5–84 years** (mean ~**51.77** years, median **57**), supporting predominantly adult onset but possible pediatric presentation. (hobbs2021pemphiguserythematosusa pages 2-5)

### 8.2 Progression/course
PE is described as generally chronic; disease duration in reviewed literature ranged **1–60 months** (mean **18.2** months; median **11** months). (onalajaunderwood2024diagnosisandmanagement pages 3-7, hobbs2021pemphiguserythematosusa pages 5-5)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
Epidemiology is not well established; a recent pediatric report states epidemiology is unknown and cites a prevalence estimate of **4.4 cases/million**. (arasiewicz2024senearushersyndromein pages 1-3)

### 9.2 Demographics
- **Sex distribution:** literature review in Hobbs found **female:male = 45:36**, suggesting mild female predominance. (hobbs2021pemphiguserythematosusa pages 2-5)
- **Race/ethnicity:** Hobbs’ center case series (n=5) had **4/5 Black (80%)**, higher than literature reporting where race was available (~20% Black), though this may reflect referral/catchment characteristics rather than true population risk. (hobbs2021pemphiguserythematosusa pages 1-2)

### 9.3 Genetic etiology (inheritance)
No Mendelian inheritance is supported; risk appears multifactorial with HLA-linked susceptibility reported. (arasiewicz2024senearushersyndromein pages 1-3)

---

## 10. Diagnostics

### 10.1 Clinical criteria and standard diagnostic approach
In Hobbs et al., diagnostic criteria required **(i) pemphigus foliaceus-like histopathology** plus **(ii) DIF evidence of epidermal intercellular IgG** and **(iii) IgG and/or C3 along the DEJ**. (hobbs2021pemphiguserythematosusa pages 1-2)

A 2024 review emphasizes that when a blistering disorder is suspected, clinicians should obtain **a lesional biopsy for H&E** and **a perilesional biopsy for DIF**, with the DIF specimen taken from immediately adjacent uninvolved skin and sent in **Michel medium**. (onalajaunderwood2024diagnosisandmanagement pages 1-3)

### 10.2 Histopathology
Typical histology includes **superficial/subcorneal or intraepidermal acantholysis**, often with dyskeratosis and lymphocytic dermal inflammation. (hobbs2021pemphiguserythematosusa pages 2-5, hobbs2021pemphiguserythematosusa pages 10-11)

### 10.3 Direct immunofluorescence (DIF)
DIF typically demonstrates **intercellular space IgG/C3 deposition** plus a **linear/granular DEJ (lupus-band–like) IgG/C3** pattern. (chandan2018unusuallyextensivescalp pages 4-5, hobbs2021pemphiguserythematosusa pages 10-11)

### 10.4 Serology / biomarkers
- **Anti-DSG1:** frequently elevated in pooled reports; Hobbs notes reported anti-DSG1 levels were elevated in available reports. (hobbs2021pemphiguserythematosusa pages 10-11)
- **ANA:** variable; cited range **30–80%** across literature, with one PE case series showing ANA elevated in **1/5 (20%)**. (jangid2023acasereport pages 1-4, hobbs2021pemphiguserythematosusa pages 2-5)

### 10.5 Differential diagnosis
PE is repeatedly discussed in diagnostic context as overlapping lupus erythematosus and pemphigus foliaceus and may be confused with seborrheic dermatitis and other seborrheic eruptions; accurate diagnosis hinges on histology and immunopathology. (espadas2024seborrheicpemphigusa pages 1-3, hobbs2021pemphiguserythematosusa pages 1-2)

---

## 11. Outcome / Prognosis

PE is often described as **more benign/easier to manage** than pemphigus vulgaris in case literature, but robust survival or long-term morbidity statistics were not available from the retrieved evidence set. (chandan2018unusuallyextensivescalp pages 4-5)

Complications reported/mentioned include secondary infection and severe erythroderma in individual cases. (arasiewicz2024senearushersyndromein pages 1-3)

---

## 12. Treatment

### 12.1 Current applications / real-world implementation
A 2024 review provides practical management framing: **“Localized disease can typically be managed by potent topical steroids”**, while more extensive disease may require systemic therapy including **prednisone** and steroid-sparing agents such as **azathioprine, mycophenolate mofetil, rituximab, or dapsone**. (onalajaunderwood2024diagnosisandmanagement pages 3-7)

Case-based evidence includes use of **hydroxychloroquine + systemic prednisone + dapsone** with clinical response in pediatric PE, supporting real-world use of antimalarial and anti-neutrophil/anti-inflammatory adjunct approaches in overlap-like presentations. (arasiewicz2024senearushersyndromein pages 1-3)

### 12.2 Treatment outcomes (data points)
- Case-series summaries cited in recent case-report literature describe remission outcomes (e.g., “three of four complete remission at mean six months” in one small series summary), though these are not controlled studies and likely heterogeneous in severity and therapy. (jangid2023acasereport pages 4-6)
- Hobbs literature review notes cases treated with **rituximab** achieving prolonged resolution (example: 3-year complete resolution reported). (hobbs2021pemphiguserythematosusa pages 10-11)

### 12.3 MAXO terms (mapping suggestions)
- Topical corticosteroid therapy; systemic glucocorticoid therapy; immunosuppressive therapy (azathioprine, mycophenolate); anti-CD20 monoclonal antibody therapy (rituximab); dapsone therapy; antimalarial therapy (hydroxychloroquine); photoprotection counseling (suggested). (onalajaunderwood2024diagnosisandmanagement pages 3-7, arasiewicz2024senearushersyndromein pages 1-3)

### 12.4 Expert opinion / guideline-like synthesis
- The geriatric bullous disease review serves as an expert synthesis emphasizing biopsy + DIF as core diagnostics and stratifying therapy by extent (topical for localized; systemic immunosuppression/biologics for extensive). (onalajaunderwood2024diagnosisandmanagement pages 1-3, onalajaunderwood2024diagnosisandmanagement pages 3-7)

---

## 13. Prevention

Evidence-based PE-specific prevention strategies were not identified beyond **avoidance of known aggravating factors**, especially **sunlight/UV exposure** given repeated associations with photosensitivity and worsening. (onalajaunderwood2024diagnosisandmanagement pages 3-7, chandan2018unusuallyextensivescalp pages 4-5)

---

## 14. Other Species / Natural Disease

No natural disease reports in non-human species specific to pemphigus erythematosus were identified in the retrieved evidence set. (hobbs2021pemphiguserythematosusa pages 1-2)

---

## 15. Model Organisms

No PE-specific model organism systems were identified in the retrieved evidence set. Mechanistic work in pemphigus broadly often uses antibody transfer/ex vivo skin systems, but such details were not retrieved here for PE specifically. (hobbs2021pemphiguserythematosusa pages 1-2)

---

## Recent developments and latest research (prioritizing 2023–2024)

1) **Clinical recognition and pediatric presentations:** Recent case reports highlight that PE can occur in children (e.g., a 2024 report in a 5-year-old), reinforcing that the age range includes pediatric-onset disease even if adult-onset is more typical. (arasiewicz2024senearushersyndromein pages 1-3)

2) **Refined diagnostic workflows in bullous disease practice:** A 2024 expert review reinforces practical details for DIF sampling (perilesional biopsy, Michel medium) and emphasizes ELISA availability for desmoglein autoantibodies, reflecting continuing standardization and accessibility of serologic testing in clinical practice. (onalajaunderwood2024diagnosisandmanagement pages 1-3)

3) **Therapeutic positioning:** A 2024 review frames PE management within modern pemphigus care, including topical steroids for localized disease and systemic immunosuppression and biologics (including rituximab) for more extensive disease, consistent with current real-world practice patterns. (onalajaunderwood2024diagnosisandmanagement pages 3-7)

---

## Evidence-backed statistics (selected)
- Common site distribution (pooled literature review): trunk 62%, face 51.7%, extremities 39%, scalp 35.6%. (hobbs2021pemphiguserythematosusa pages 2-5)
- Oral involvement (pooled): ~9.2%. (hobbs2021pemphiguserythematosusa pages 2-5)
- Sex ratio (pooled): female:male 45:36. (hobbs2021pemphiguserythematosusa pages 2-5)
- Age distribution (pooled): range 5–84; mean ~51.77; median 57. (hobbs2021pemphiguserythematosusa pages 2-5)
- ANA positivity: widely cited 30–80% in literature; one center series 1/5 (20%). (jangid2023acasereport pages 1-4, hobbs2021pemphiguserythematosusa pages 2-5)
- Prevalence estimate (single cited figure): 4.4 cases/million. (arasiewicz2024senearushersyndromein pages 1-3)

---

## Summary table
| Domain | Key finding | Supporting citations |
|---|---|---|
| Definition / disease concept | Pemphigus erythematosus (PE), also called Senear–Usher syndrome, is a rare autoimmune blistering disorder generally regarded as a localized variant of pemphigus foliaceus with clinical, histologic, and immunologic overlap with cutaneous lupus erythematosus. | (arasiewicz2024senearushersyndromein pages 1-3, jangid2023acasereport pages 1-4, hobbs2021pemphiguserythematosusa pages 1-2, onalajaunderwood2024diagnosisandmanagement pages 3-7) |
| Typical clinical distribution | Lesions are usually erythematous, scaly or crusted plaques / superficial flaccid bullae in seborrheic and photoexposed areas, especially the malar face, scalp, upper trunk, and back; face involvement was 80% in one center series and 51.7% in the pooled literature review. | (arasiewicz2024senearushersyndromein pages 1-3, hobbs2021pemphiguserythematosusa pages 1-2, hobbs2021pemphiguserythematosusa pages 2-5, onalajaunderwood2024diagnosisandmanagement pages 3-7, onalajaunderwood2024diagnosisandmanagement pages 1-3) |
| Mucosal involvement | Mucosal disease is uncommon; oral/pharyngeal/vulvar mucosa are often spared, and pooled oral involvement was ~9.2% in Hobbs et al. | (arasiewicz2024senearushersyndromein pages 1-3, hobbs2021pemphiguserythematosusa pages 2-5, onalajaunderwood2024diagnosisandmanagement pages 1-3) |
| Key autoantigens | Main autoantigen is desmoglein 1 (Dsg1); some reports also describe Dsg3 and other desmosomal adhesion proteins / plakins. PF-variant pathogenesis is linked to IgG4 against Dsg1. | (arasiewicz2024senearushersyndromein pages 1-3, jangid2023acasereport pages 1-4, chandan2018unusuallyextensivescalp pages 1-4, onalajaunderwood2024diagnosisandmanagement pages 1-3) |
| Histology | Characteristic pathology is superficial/subcorneal or intraepidermal acantholysis, often with dyskeratosis; inflammatory infiltrates may be lymphocytic or mixed, with papillary dermal edema/perivascular infiltrates in some cases. | (arasiewicz2024senearushersyndromein pages 1-3, chandan2018unusuallyextensivescalp pages 1-4, hobbs2021pemphiguserythematosusa pages 2-5, hobbs2021pemphiguserythematosusa pages 10-11) |
| Direct immunofluorescence (DIF) | Classic DIF shows intercellular epidermal IgG/C3 deposition plus IgG and/or C3 along the dermal–epidermal junction ("lupus-band"-like pattern). PE diagnostic criteria in Hobbs et al. required PF histology plus these DIF findings. | (chandan2018unusuallyextensivescalp pages 4-5, hobbs2021pemphiguserythematosusa pages 1-2, hobbs2021pemphiguserythematosusa pages 10-11, jangid2023acasereport pages 4-6) |
| ANA / lupus serology | ANA positivity is variably reported, commonly cited as ~30%–80% of cases; in the Hobbs center series ANA was elevated in 1/5 patients (20%). Additional lupus-associated serologies reported in case literature include anti-dsDNA, anti-Ro/SSA, anti-Sm, and anti-RNP. | (jangid2023acasereport pages 1-4, hobbs2021pemphiguserythematosusa pages 1-2, hobbs2021pemphiguserythematosusa pages 2-5) |
| Epidemiology | Epidemiology is poorly defined. One cited prevalence estimate is 4.4 cases/million. In Hobbs et al., the literature review found mean age 51.77 years (median 57; range 5–84) and female:male ratio 45:36; the center series had mean age 43.8 years and 3/5 female. Oral involvement in the pooled review was ~9.2%. | (arasiewicz2024senearushersyndromein pages 1-3, hobbs2021pemphiguserythematosusa pages 1-2, hobbs2021pemphiguserythematosusa pages 2-5) |
| Triggers / exacerbating factors | Ultraviolet exposure / sunlight is a recognized exacerbating factor; photosensitivity is a recurring clinical feature and UV may contribute to DEJ immune deposition in PE. Medication-associated pemphigus triggers are also discussed in broader reviews, though PE-specific evidence is limited. | (chandan2018unusuallyextensivescalp pages 4-5, hobbs2021pemphiguserythematosusa pages 10-11, onalajaunderwood2024diagnosisandmanagement pages 3-7, onalajaunderwood2024diagnosisandmanagement pages 1-3) |
| Common treatments | Localized disease can often be treated with potent topical corticosteroids. More extensive disease is treated with systemic corticosteroids plus steroid-sparing agents such as azathioprine, mycophenolate mofetil, dapsone, methotrexate, cyclophosphamide, or rituximab; hydroxychloroquine has also been used in overlap-style cases. | (arasiewicz2024senearushersyndromein pages 1-3, chandan2018unusuallyextensivescalp pages 4-5, hobbs2021pemphiguserythematosusa pages 10-11, onalajaunderwood2024diagnosisandmanagement pages 3-7, jangid2023acasereport pages 1-4) |


*Table: This table condenses the main disease-characteristics evidence for pemphigus erythematosus (Senear–Usher syndrome), including defining overlap features, phenotype, diagnostics, epidemiology, triggers, and treatment. It is useful as a quick-reference summary mapped directly to the gathered citation IDs.*

---

## Key direct quotes (from retrieved sources)
- 2024 review statement: **“Localized disease can typically be managed by potent topical steroids.”** (onalajaunderwood2024diagnosisandmanagement pages 3-7)
- 2024 review epidemiologic framing: **“Represents 10% of all cases of pemphigus foliaceus, with features of lupus erythematosus.”** (onalajaunderwood2024diagnosisandmanagement pages 1-3)

---

## Limitations of this report (data gaps)
- Curated identifiers (ICD/MeSH/Orphanet/MONDO/OMIM) were not found in the retrieved full-text evidence set, so they cannot be provided with citations here. (hobbs2021pemphiguserythematosusa pages 1-2)
- PE-specific controlled trial data and PE-specific QoL instruments/statistics were not identified in the retrieved evidence; most treatment/outcome information is case-based and extrapolated from broader pemphigus management frameworks. (hobbs2021pemphiguserythematosusa pages 10-11, onalajaunderwood2024diagnosisandmanagement pages 3-7)


References

1. (arasiewicz2024senearushersyndromein pages 1-3): Hubert Arasiewicz, Joanna Czuwara, Michał Dec, and Lilianna Leśniak-Jakubiec. Senear-usher syndrome in a 5-year-old girl. Advances in Dermatology and Allergology/Postȩpy Dermatologii i Alergologii, 41:242-244, Apr 2024. URL: https://doi.org/10.5114/ada.2024.139233, doi:10.5114/ada.2024.139233. This article has 1 citations.

2. (espadas2024seborrheicpemphigusa pages 1-3): Diana Gallegos Espadas, Arely Gissell Ramirez Cibrian, and Jesús Iván Martínez-Ortega. Seborrheic pemphigus: a misunderstood variant of pemphigus foliaceus. Cureus, Apr 2024. URL: https://doi.org/10.7759/cureus.59389, doi:10.7759/cureus.59389. This article has 2 citations.

3. (hobbs2021pemphiguserythematosusa pages 1-2): Landon K. Hobbs, Mary‐Margaret B. Noland, Shyam S. Raghavan, and Alejandro A. Gru. Pemphigus erythematosus: a case series from a tertiary academic center and literature review. Journal of Cutaneous Pathology, 48:1038-1050, Mar 2021. URL: https://doi.org/10.1111/cup.13992, doi:10.1111/cup.13992. This article has 12 citations and is from a peer-reviewed journal.

4. (onalajaunderwood2024diagnosisandmanagement pages 3-7): Amanda A. Onalaja-Underwood, Maria Yadira Hurley, and Olayemi Sokumbi. Diagnosis and management of bullous disease. Clinics in Geriatric Medicine, 40:37-74, Feb 2024. URL: https://doi.org/10.1016/j.cger.2023.09.002, doi:10.1016/j.cger.2023.09.002. This article has 4 citations and is from a peer-reviewed journal.

5. (onalajaunderwood2024diagnosisandmanagement pages 1-3): Amanda A. Onalaja-Underwood, Maria Yadira Hurley, and Olayemi Sokumbi. Diagnosis and management of bullous disease. Clinics in Geriatric Medicine, 40:37-74, Feb 2024. URL: https://doi.org/10.1016/j.cger.2023.09.002, doi:10.1016/j.cger.2023.09.002. This article has 4 citations and is from a peer-reviewed journal.

6. (chandan2018unusuallyextensivescalp pages 4-5): Neha Chandan, Eden P Lake, and Lawrence S Chan. Unusually extensive scalp ulcerations manifested in pemphigus erythematosus. Dermatology Online Journal, Feb 2018. URL: https://doi.org/10.5070/d3241037928, doi:10.5070/d3241037928. This article has 7 citations and is from a peer-reviewed journal.

7. (jangid2023acasereport pages 1-4): Shivani D Jangid, Bhushan Madke, Adarshlata Singh, Drishti M Bhatt, and Arshiya Khan. A case report on senear-usher syndrome. Cureus, Nov 2023. URL: https://doi.org/10.7759/cureus.49268, doi:10.7759/cureus.49268. This article has 1 citations.

8. (chandan2018unusuallyextensivescalp pages 1-4): Neha Chandan, Eden P Lake, and Lawrence S Chan. Unusually extensive scalp ulcerations manifested in pemphigus erythematosus. Dermatology Online Journal, Feb 2018. URL: https://doi.org/10.5070/d3241037928, doi:10.5070/d3241037928. This article has 7 citations and is from a peer-reviewed journal.

9. (hobbs2021pemphiguserythematosusa pages 2-5): Landon K. Hobbs, Mary‐Margaret B. Noland, Shyam S. Raghavan, and Alejandro A. Gru. Pemphigus erythematosus: a case series from a tertiary academic center and literature review. Journal of Cutaneous Pathology, 48:1038-1050, Mar 2021. URL: https://doi.org/10.1111/cup.13992, doi:10.1111/cup.13992. This article has 12 citations and is from a peer-reviewed journal.

10. (hobbs2021pemphiguserythematosusa pages 10-11): Landon K. Hobbs, Mary‐Margaret B. Noland, Shyam S. Raghavan, and Alejandro A. Gru. Pemphigus erythematosus: a case series from a tertiary academic center and literature review. Journal of Cutaneous Pathology, 48:1038-1050, Mar 2021. URL: https://doi.org/10.1111/cup.13992, doi:10.1111/cup.13992. This article has 12 citations and is from a peer-reviewed journal.

11. (jangid2023acasereport pages 6-7): Shivani D Jangid, Bhushan Madke, Adarshlata Singh, Drishti M Bhatt, and Arshiya Khan. A case report on senear-usher syndrome. Cureus, Nov 2023. URL: https://doi.org/10.7759/cureus.49268, doi:10.7759/cureus.49268. This article has 1 citations.

12. (hobbs2021pemphiguserythematosusa pages 5-5): Landon K. Hobbs, Mary‐Margaret B. Noland, Shyam S. Raghavan, and Alejandro A. Gru. Pemphigus erythematosus: a case series from a tertiary academic center and literature review. Journal of Cutaneous Pathology, 48:1038-1050, Mar 2021. URL: https://doi.org/10.1111/cup.13992, doi:10.1111/cup.13992. This article has 12 citations and is from a peer-reviewed journal.

13. (jangid2023acasereport pages 4-6): Shivani D Jangid, Bhushan Madke, Adarshlata Singh, Drishti M Bhatt, and Arshiya Khan. A case report on senear-usher syndrome. Cureus, Nov 2023. URL: https://doi.org/10.7759/cureus.49268, doi:10.7759/cureus.49268. This article has 1 citations.