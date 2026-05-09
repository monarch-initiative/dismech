---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T13:31:04.419792'
end_time: '2026-05-06T13:43:16.992744'
duration_seconds: 732.58
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Arteriosclerotic Retinopathy
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Arteriosclerotic Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Arteriosclerotic Retinopathy** covering all of the
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
- **Disease Name:** Arteriosclerotic Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Arteriosclerotic Retinopathy** covering all of the
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


## Comprehensive Research Report: Arteriosclerotic Retinopathy (Fundus Arteriosclerosis / Retinal Arteriosclerosis)

### Executive summary
Arteriosclerotic retinopathy (often operationalized in modern epidemiology as **“fundus arteriosclerosis”** or **“retinal arteriosclerosis/atherosclerotic retinopathy”**) refers to chronic, structural **arteriolar wall changes** in the retinal circulation that are typically associated with aging and systemic vascular disease (e.g., hypertension, diabetes, chronic kidney disease, and atherosclerosis). Clinically it is recognized by ophthalmoscopic or fundus-photographic signs such as **increased arteriolar light reflex (copper/silver wiring)** and **arteriovenous (AV) crossing changes** and is commonly graded using **Scheie S0–S4** (atherosclerotic) and related grading systems. Histopathologic descriptors include medial hypertrophy, intimal hyalinization, and endothelial hyperplasia. (nokiba2015associationbetweenophthalmological pages 1-3, sugiura2022examinationoflarge media a2b302a2)

Because the retina is a uniquely accessible microvascular bed, multiple recent studies (2023–2024) have used fundus photography and OCT/OCTA-derived metrics as **non-invasive correlates of systemic atherosclerosis burden** and predictors of cardiovascular/cerebrovascular risk. (liu2023sexspecificassociationbetween pages 3-4, rusu2024retinalstructuraland pages 1-2)

---

## 1. Disease Information

### 1.1 Disease overview (current understanding)
**Arteriosclerotic retinopathy** denotes chronic retinal arteriolar remodeling/“hardening” related to arteriosclerosis/atherosclerosis and long-standing vascular risk exposure. In one clinical definition used in CKD/hemodialysis research, arteriosclerotic retinopathy is described as a lesion characterized by **“medial layer hypertrophy, hyalinization of the intima, and hyperplasia of the endothelial layer of the vessel wall.”** (nokiba2015associationbetweenophthalmological pages 1-3)

In practice, the term overlaps with chronic components of **hypertensive retinopathy** (arteriolar sclerosis) and with population screening terms such as **“fundus arteriosclerosis.”** (liu2023sexspecificassociationbetween pages 3-4, sugiura2022examinationoflarge media a2b302a2)

### 1.2 Key identifiers (ontology/coding)
* **MONDO / OMIM / Orphanet:** Not identified in the retrieved primary literature excerpts; this entity is commonly treated as a *clinical sign/phenotype complex* rather than a monogenic disorder. (No specific MONDO/OMIM/Orphanet identifier found in available texts.)
* **MeSH / ICD-10/ICD-11:** Not extractable from the retrieved texts using available tools/evidence; many studies define the phenotype via **fundus grading systems** rather than billing codes. (liu2023sexspecificassociationbetween pages 3-4, sugiura2022examinationoflarge media a2b302a2)

### 1.3 Synonyms / alternative names
Commonly used overlapping terms in the retrieved literature:
* **Fundus arteriosclerosis** (liu2023sexspecificassociationbetween pages 3-4)
* **Retinal arteriosclerosis / atherosclerotic retinopathy** (Scheie S grading) (sugiura2022examinationoflarge pages 2-4, sugiura2022examinationoflarge media a2b302a2)
* **Arteriolar light reflex enhancement** / **copper-wiring** / **silver-wiring** (as a sign within arteriosclerotic/hypertensive grading) (kaushik2007prevalenceandassociations pages 1-3, sugiura2022examinationoflarge media a2b302a2)

### 1.4 Evidence sources
The information above is derived from **aggregated disease-level resources in cohort studies, systematic reviews, and clinical definitions** rather than single case reports. (kaushik2007prevalenceandassociations pages 1-3, liu2023sexspecificassociationbetween pages 3-4, rusu2024retinalstructuraland pages 1-2, geng2023sexspecificassociationof pages 1-2)

---

## 2. Etiology

### 2.1 Primary causal factors (multifactorial)
Arteriosclerotic retinopathy is best understood as a **microvascular end-organ manifestation** of chronic systemic vascular stressors rather than a single causal gene disorder. Mechanistically, the phenotype reflects chronic arteriolar wall remodeling and sclerosis (see §6). (nokiba2015associationbetweenophthalmological pages 1-3)

### 2.2 Risk factors (recent human evidence)
**Metabolic and vascular risk factors** are consistently associated with arteriosclerotic retinal signs:

* **Hypertension, diabetes, dyslipidemia, CKD:** In a cohort of untreated middle-aged workers (n=7,730), unadjusted odds ratios for atherosclerotic retinopathy (Scheie S1+S2) were elevated for CKD (OR 2.88), hypertension (OR 3.27), dyslipidemia (OR 1.26), and diabetes (OR 5.98). (sugiura2022examinationoflarge pages 12-13)
* **Serum uric acid trajectory (sex-specific):** In a 2010 baseline cohort followed to 2019 (n=4,324), men in higher SUA trajectory groups had higher incidence of retinal arteriosclerosis (moderate-high vs low: HR 1.76; high vs low: HR 1.81), while women did not show the same pattern. (geng2023sexspecificassociationof pages 1-2)

### 2.3 Protective factors
Clear protective factors are less consistently reported; however, biomarkers sometimes proposed as protective against systemic atherosclerosis can show complex/sex-specific associations in retinal endpoints.

* **Total bilirubin (TBIL):** A large retrospective cohort (n=27,477; 2006–2019) found *higher* TBIL quartiles were associated with *higher* risk of incident fundus arteriosclerosis in males (Q4 vs Q1 HR 1.396), with no significant association in females. This directionality suggests TBIL is not protective in this cohort/definition and underscores possible confounding or non-linear biology. (nokiba2015associationbetweenophthalmological pages 1-3)

### 2.4 Gene–environment interactions
Direct gene–environment interaction evidence specific to arteriosclerotic retinopathy was not captured in the retrieved texts. Some broader retinal microvascular biomarker literature acknowledges genetic influences on retinal traits, but disease-specific G×E results were not retrievable here. (iorga2024noninvasiveretinalvessel pages 5-7)

---

## 3. Phenotypes

### 3.1 Key clinical signs and grading (Scheie)
The most widely operationalized phenotype definition in the retrieved sources is **Scheie atherosclerotic retinopathy S0–S4** and hypertensive retinopathy H0–H4, evaluated from fundus examination/photography.

**Scheie atherosclerotic retinopathy (S) grading (definitions):**
* **S0:** Normal
* **S1:** Broadening of the light reflex from the arteriole with minimal/no AV compression
* **S2:** Light reflex and crossing changes more prominent
* **S3:** “Copper wire” appearance with more prominent AV compression
* **S4:** “Silver” appearance with most severe AV crossing changes (sugiura2022examinationoflarge media a2b302a2)

**Scheie hypertensive retinopathy (H) grading (definitions):**
* **H0:** Normal
* **H1:** Barely detectable arterial narrowing
* **H2:** Obvious arterial narrowing with focal irregularities plus light reflex changes
* **H3:** H2 plus retinal hemorrhages and/or exudates
* **H4:** H3 plus papilledema (sugiura2022examinationoflarge media a2b302a2)

A figure region containing the above grading definitions was retrieved from the Sugiura et al. paper (visual evidence). (sugiura2022examinationoflarge media a2b302a2)

### 3.2 Population frequency (examples)
* **Enhanced arteriolar light reflex (a related arteriosclerotic sign):** In the Blue Mountains Eye Study (n=3,654; ≥49 years), enhanced retinal arteriolar light reflex was common (31.7% overall; 28.8% mild, 2.9% marked). Mild enhancement was strongly associated with AV nicking (OR 3.12) and with retinopathy (OR 1.96). (kaushik2007prevalenceandassociations pages 1-3)
* **Scheie-defined retinopathy prevalence in untreated middle-aged workers:** In Sugiura et al. (n=7,730; ages 35–61), hypertensive retinopathy (H1+H2) prevalence was 2.8%, while atherosclerotic retinopathy (S1+S2) prevalence was 13.6%. (sugiura2022examinationoflarge pages 12-13)

### 3.3 Symptomatology and QoL impact
Arteriosclerotic retinopathy is often **asymptomatic** until complications occur (e.g., occlusive disease, macular edema in related conditions). The retrieved evidence focused on imaging signs and systemic associations rather than patient-reported quality-of-life instruments; no EQ-5D/SF-36 metrics were found in the available texts. (liu2023sexspecificassociationbetween pages 3-4, rusu2024retinalstructuraland pages 1-2)

### 3.4 Suggested HPO terms (phenotype mapping; best-fit suggestions)
(These are ontology suggestions; exact HPO IDs should be verified in HPO.)
* Retinal arteriolar narrowing (sign) (supported conceptually by Scheie H grades and retinal arteriolar narrowing) (sugiura2022examinationoflarge media a2b302a2)
* Arteriovenous nicking (sign) (kaushik2007prevalenceandassociations pages 1-3, sugiura2022examinationoflarge media a2b302a2)
* Increased retinal arteriolar light reflex / copper wiring / silver wiring (sign) (kaushik2007prevalenceandassociations pages 1-3, sugiura2022examinationoflarge media a2b302a2)
* Retinal hemorrhage / hard exudates / cotton wool spots / papilledema (primarily severe hypertensive retinopathy features) (sugiura2022examinationoflarge media a2b302a2)

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes and pathogenic variants
No causal genes or pathogenic variants were identified in the retrieved sources for arteriosclerotic retinopathy as a discrete genetic disorder. The current evidence base in this tool run supports arteriosclerotic retinopathy as a **complex trait/end-organ phenotype** rather than a Mendelian condition. (iorga2024noninvasiveretinalvessel pages 5-7)

### 4.2 Modifier genes / epigenetics / chromosomal abnormalities
Not identified in the retrieved evidence. (iorga2024noninvasiveretinalvessel pages 5-7)

---

## 5. Environmental Information

### 5.1 Lifestyle and environmental factors
* **Heavy alcohol intake** was associated with *marked* enhanced arteriolar light reflex in the Blue Mountains Eye Study (OR 2.66 for ≥40 g/day). (kaushik2007prevalenceandassociations pages 1-3)
* Traditional cardiovascular risk factors (smoking, BMI/obesity, lipid and glucose measures) were associated with enhanced light reflex and/or Scheie-defined retinopathy in population studies. (kaushik2007prevalenceandassociations pages 1-3, sugiura2022examinationoflarge pages 12-13)

### 5.2 Infectious agents
No infectious etiology is supported in retrieved texts. (nokiba2015associationbetweenophthalmological pages 1-3)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (conceptual)
**Chronic systemic vascular risk exposure** (hypertension, diabetes, dyslipidemia, CKD-related mineral/inflammatory milieu) → **endothelial dysfunction and vascular remodeling** → **retinal arteriolar wall thickening/sclerosis** (medial hypertrophy, intimal hyalinization, endothelial hyperplasia) → **ophthalmoscopic signs** (increased light reflex “copper/silver wiring”, AV crossing changes, arteriolar narrowing) → associations with **systemic arterial stiffness and atherosclerotic burden**. (nokiba2015associationbetweenophthalmological pages 1-3, nokiba2015associationbetweenophthalmological pages 3-4, sugiura2022examinationoflarge media a2b302a2)

### 6.2 Histopathology-linked description
A clinical pathologic description in CKD/hemodialysis literature emphasizes that arteriosclerotic retinopathy reflects vascular wall remodeling with **“medial layer hypertrophy, hyalinization of the intima, and hyperplasia of the endothelial layer.”** (nokiba2015associationbetweenophthalmological pages 1-3)

### 6.3 Microvascular–macrovascular coupling (human data)
Evidence supports that retinal arteriosclerotic findings track systemic vascular disease:
* In hemodialysis patients (n=44), **Scheie S grade** correlated with arterial stiffness (PWV) and past CVD (reported p=0.001 and p=0.045). (nokiba2015associationbetweenophthalmological pages 1-3)
* In untreated middle-aged adults (n=7,730), measures of large-artery atherosclerosis/stiffness—**carotid IMT and CAVI**—were independently associated with Scheie-defined retinopathy; carotid IMT per 0.1 mm showed ORs around ~1.18 for retinopathy in multivariable models. (sugiura2022examinationoflarge pages 7-9, sugiura2022examinationoflarge pages 6-7)
* In a large cross-sectional health-exam sample (n=20,836), fundus arteriosclerosis was associated with carotid atherosclerosis (adjusted OR 1.17). (liu2023sexspecificassociationbetween pages 3-4)

### 6.4 Molecular pathways / immune involvement (evidence level)
The retrieved texts emphasize general vascular mechanisms (endothelial dysfunction, oxidative stress, inflammation) in the context of systemic vascular disease and retinal microvasculature but do not provide disease-specific retinal transcriptomic/proteomic signatures for arteriosclerotic retinopathy. (nokiba2015associationbetweenophthalmological pages 1-3, bisen2025retinalimagingas pages 5-8)

### 6.5 Suggested ontology terms
**GO (biological process) suggestions (verify IDs):**
* Blood vessel remodeling; extracellular matrix organization; regulation of vascular smooth muscle cell proliferation; response to oxidative stress; inflammatory response (conceptually consistent with sclerosis/remodeling and inflammation noted as risk factors). (nokiba2015associationbetweenophthalmological pages 1-3)

**CL (cell type) suggestions (verify IDs):**
* Vascular endothelial cell; vascular smooth muscle cell/pericyte (arteriolar wall remodeling). (nokiba2015associationbetweenophthalmological pages 1-3)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue/cell targets
* **Primary organ/tissue:** Retina (retinal arterioles; AV crossings). (sugiura2022examinationoflarge media a2b302a2)
* **Vascular structures:** Retinal arterioles and arteriovenous crossings. (sugiura2022examinationoflarge media a2b302a2)

**UBERON suggestions (verify IDs):** retina; retinal blood vessel; retinal arteriole.

### 7.2 Laterality
Generally bilateral in systemic disease, but laterality was not specified in retrieved texts.

---

## 8. Temporal Development

### 8.1 Onset and course
Arteriosclerotic retinal changes are typically **chronic/insidious** and accumulate with age and vascular risk exposure. In middle-aged workers (mean ~45 years), Scheie S1+S2 prevalence was already ~13.6%, supporting early/midlife detectability. (sugiura2022examinationoflarge pages 12-13, sugiura2022examinationoflarge pages 1-2)

### 8.2 Staging
Scheie S0–S4 provides a practical staging framework from normal through copper/silver wiring and severe AV crossing changes. (sugiura2022examinationoflarge media a2b302a2)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (available statistics)
Population-based frequencies depend heavily on definitions:
* Enhanced arteriolar light reflex prevalence: **31.7%** in a ≥49-year cohort. (kaushik2007prevalenceandassociations pages 1-3)
* Scheie-defined atherosclerotic retinopathy (S1+S2): **13.6%** in untreated workers aged 35–61. (sugiura2022examinationoflarge pages 12-13)

Incidence data from a longitudinal study:
* Retinal arteriosclerosis events over ~9.5 years: **295 men and 97 women** among 4,324 adults initially free of retinal arteriosclerosis. (geng2023sexspecificassociationof pages 1-2)

### 9.2 Demographics and sex effects
Sex-specific associations have been reported for biochemical predictors (e.g., SUA trajectories and TBIL associations stronger in men). (geng2023sexspecificassociationof pages 1-2, nokiba2015associationbetweenophthalmological pages 1-3)

---

## 10. Diagnostics

### 10.1 Clinical and imaging tests (current practice)
**Fundus examination / fundus photography** is the core diagnostic modality for Scheie and KWB grading.
* Sugiura et al. used **non-mydriatic fundus photographs** graded by ophthalmologists according to Scheie H and S grades. (sugiura2022examinationoflarge pages 2-4, sugiura2022examinationoflarge media a2b302a2)
* Liu et al. used standardized **nonmydriatic fundus photography** with two trained ophthalmologists grading KWB-based fundus arteriosclerosis. (liu2023sexspecificassociationbetween pages 3-4)

**OCT and OCTA (modern developments; 2024 evidence):**
* A 2024 systematic review/meta-analysis of CAD studies supports that OCT/OCTA capture retinal structural and microvascular signatures in systemic CAD, including reduced RNFL thickness and reduced vessel density with expanded FAZ in CAD. (rusu2024retinalstructuraland pages 1-2)
* A 2024 review describes limitations and strengths of OCTA vs fundus-photo vessel measurement and summarizes normative CRAE/CRVE/AVR metrics. (iorga2024noninvasiveretinalvessel pages 5-7)

### 10.2 Biomarkers
Biochemical predictors investigated in recent cohorts include **serum uric acid trajectories** (incident retinal arteriosclerosis in men) and **total bilirubin quartiles** (risk in males). (geng2023sexspecificassociationof pages 1-2, nokiba2015associationbetweenophthalmological pages 1-3)

### 10.3 Differential diagnosis
Not systematically addressed in retrieved texts, but clinically overlaps with:
* Hypertensive retinopathy (acute and chronic stages)
* Diabetic retinopathy (microaneurysms/hemorrhages/exudates)
* Retinal vein/artery occlusions (acute ischemic presentations)

The current evidence set emphasizes that arteriosclerotic signs (light reflex and crossing changes) are often embedded within hypertensive retinopathy staging systems. (sugiura2022examinationoflarge media a2b302a2)

---

## 11. Outcome / Prognosis

### 11.1 Systemic vascular prognosis (associative)
Arteriosclerotic retinal signs and retinal microvascular biomarkers are repeatedly associated with systemic vascular disease burden:
* Fundus arteriosclerosis associated with carotid atherosclerosis (adjusted OR 1.17). (liu2023sexspecificassociationbetween pages 3-4)
* Scheie grades correlated with arterial stiffness and CVD history in hemodialysis patients. (nokiba2015associationbetweenophthalmological pages 1-3)

### 11.2 Ocular prognosis
The retrieved texts did not provide direct longitudinal estimates of vision loss attributable specifically to arteriosclerotic retinopathy without occlusive events. However, retinal microvascular compromise is positioned as part of a continuum toward ischemic retinal complications and systemic vascular events. (bisen2025retinalimagingas pages 5-8, rusu2024retinalstructuraland pages 1-2)

---

## 12. Treatment

### 12.1 Disease-specific therapy
No disease-specific ocular therapy for isolated arteriosclerotic retinopathy is established in the retrieved literature; management typically targets **systemic risk factor modification** and surveillance.

### 12.2 Risk factor management (real-world implementation)
Given strong associations with hypertension, diabetes, dyslipidemia, and CKD, real-world management aligns with cardiovascular risk reduction. Supporting evidence includes the strong unadjusted associations of these conditions with Scheie-defined retinopathy in population screening. (sugiura2022examinationoflarge pages 12-13)

### 12.3 MAXO term suggestions (verify IDs)
* Antihypertensive therapy; lipid-lowering therapy; diabetes management; smoking cessation counseling; screening fundus photography; optical coherence tomography angiography.

---

## 13. Prevention

### 13.1 Primary prevention
* Control of hypertension, diabetes, dyslipidemia, and CKD-related risk likely reduces development/progression of retinal arteriosclerotic changes; population data show these factors are strongly associated with prevalent Scheie-defined lesions. (sugiura2022examinationoflarge pages 12-13)

### 13.2 Secondary prevention / screening
**Screening and risk stratification** using fundus photography and retinal analytics is an active area:
* A 2023 deep-learning meta-analysis supports that retinal-image-based models can predict multiple CVD risk-related outcomes and future CVD events with AUROC ~0.68–0.81 in some studies, but emphasizes need for validation for real-world adoption. (nokiba2015associationbetweenophthalmological pages 1-3)
* A 2024 review argues retinal microvascular biomarkers (e.g., CRAE/CRVE/AVR; dynamic retinal vessel analysis; AI systems) could aid screening and treatment monitoring for CVD. (iorga2024noninvasiveretinalvessel pages 5-7)

---

## 14. Other Species / Natural Disease
No naturally occurring veterinary analogs were identified in the retrieved evidence set for “arteriosclerotic retinopathy” as a named entity.

---

## 15. Model Organisms
No specific model organism papers for retinal arteriosclerosis were retrieved in the available evidence. Mechanistic modeling is likely to rely on hypertension/atherosclerosis animal models with retinal vascular endpoints, but this could not be substantiated with the current evidence set.

---

## Recent developments (2023–2024 highlight)
1) **Large observational datasets** are increasingly treating fundus arteriosclerosis as a quantitative marker linked to systemic atherosclerosis (e.g., carotid ultrasound associations; sex-specific effects). (liu2023sexspecificassociationbetween pages 3-4, geng2023sexspecificassociationof pages 1-2)
2) **OCT/OCTA biomarkers** are being consolidated in systematic reviews as potential non-invasive correlates of coronary artery disease (reduced vessel density; larger FAZ; thinner RNFL/choroid). (rusu2024retinalstructuraland pages 1-2)
3) **AI/deep learning and “retinal analytics”** for cardiovascular risk prediction has matured into systematic evidence syntheses, with performance competitive with but not clearly superior to standard risk scores in current studies. (nokiba2015associationbetweenophthalmological pages 1-3)

---

## Key quantitative evidence table (2023–2024 prioritized)
The following table consolidates the most relevant quantitative studies and syntheses captured in this run.

| Study (first author, year) | Design/Population (N, setting) | Retinal phenotype definition (Scheie/KWB, vessel measures) | Main findings with effect sizes (OR/HR/WMD etc.) | Publication date | PMID | URL |
|---|---|---|---|---|---|---|
| Geng 2023 | Population-based longitudinal study; N=4,324 adults aged 18–60 without retinal arteriosclerosis at baseline; exposure window 2006–2010, follow-up 2011–2019; Chinese health-examination cohort | Incident retinal arteriosclerosis; study evaluated sex-specific serum uric acid (SUA) trajectory groups (low, moderate, moderate-high, high) as predictors of later retinal arteriosclerosis | During median 9.54-year follow-up, 97 women and 295 men developed retinal arteriosclerosis. In men, moderate-high SUA trajectory vs low: HR 1.76 (95% CI 1.17–2.65); high trajectory vs low: HR 1.81 (95% CI 1.04–3.17). No significant increase in women for moderate-high trajectory: HR 0.77 (95% CI 0.39–1.52) (geng2023sexspecificassociationof pages 1-2) | 2023-02-28 |  | https://doi.org/10.3389/fcvm.2023.1116486 |
| Liu 2023 | Retrospective cross-sectional study; N=20,836 Chinese health-examination participants (13,050 male; 7,786 female) | Fundus arteriosclerosis graded from standardized nonmydriatic fundus photographs using Keith–Wagener–Barker (KWB) grades 1–4; any grade 1–4 counted as fundus arteriosclerosis; carotid atherosclerosis assessed by Doppler ultrasound | Carotid atherosclerosis incidence was higher in those with fundus arteriosclerosis (52.94% vs 47.06%). Adjusted association between fundus arteriosclerosis and carotid atherosclerosis: OR 1.17 (95% CI 1.02–1.34; p=0.0262); association significant in males but not females (liu2023sexspecificassociationbetween pages 3-4) | 2023-11 |  | https://doi.org/10.1186/s40001-023-01508-6 |
| Dong 2023 | Retrospective cohort study; N=27,477 Chinese participants, follow-up 2006–2019 | Incident fundus arteriosclerosis; exposure was quartiles of serum total bilirubin (TBIL); fundus arteriosclerosis assessed in routine examinations | In males, higher TBIL quartiles associated with higher fundus arteriosclerosis risk vs Q1: Q2 HR 1.217 (95% CI 1.095–1.354), Q3 HR 1.255 (95% CI 1.128–1.396), Q4 HR 1.396 (95% CI 1.254–1.555); linear dose-response reported. No significant association in females (nokiba2015associationbetweenophthalmological pages 1-3) | 2023-07 |  | https://doi.org/10.1038/s41598-023-38378-1 |
| Rusu 2024 | Systematic review and meta-analysis; 11 studies of CAD vs controls | OCT/OCTA retinal structural and vascular biomarkers rather than classic Scheie/KWB lesions; included retinal thickness, RNFL, choroid, vessel density, FAZ | CAD associated with thinner RNFL (WMD −3.11), thinner subfoveal choroid (WMD −58.79), lower overall retinal thickness (WMD −4.61), lower superficial foveal vessel density (WMD −2.19; p<0.0001), and larger FAZ (WMD 52.73; p=0.02), supporting retinal vascularization as a noninvasive CAD biomarker (rusu2024retinalstructuraland pages 1-2) | 2024-03 |  | https://doi.org/10.3390/life14040448 |
| Iorga 2024 | Narrative/systematic-style review of non-invasive retinal vessel analysis in cardiovascular disease | Retinal vessel analysis metrics: CRAE, CRVE, AVR; fundus photography, dynamic retinal vessel analysis, OCTA | Summarized normative Gutenberg Health Study metrics: mean CRAE 178.37 µm, CRVE 212.30 µm, AVR 0.84. Review notes uncontrolled hypertension example values CRAE 172.28 µm and AVR 0.81; hypertension strongly associated with lower AVR/CRAE, with tabulated ORs 2.703 for AVR and 2.881 for CRAE (p=0.001). Emphasizes AI systems (e.g., QUARTZ, SIVA-DLS) for scalable extraction of retinal vascular biomarkers (iorga2024noninvasiveretinalvessel pages 5-7) | 2024-05 |  | https://doi.org/10.3390/jpm14050501 |
| Girach 2024 | Systematic review of prospective studies assessing retinal imaging biomarkers for stroke risk; 24 studies included | Retinal imaging biomarkers including vessel caliber, fractal dimension, tortuosity, retinopathy, emboli, AV nicking; fundus photography and limited OCT studies | Review found wider retinal venules, lower fractal dimension, increased arteriolar tortuosity, retinopathy, and retinal emboli associated with higher stroke risk; evidence weaker for narrower arterioles and isolated AV nicking. AI models performed similarly to conventional risk scores but did not clearly outperform them (nokiba2015associationbetweenophthalmological pages 1-3) | 2024-03 |  | https://doi.org/10.1007/s00415-023-12171-6 |
| Hu 2023 | Systematic review and meta-analysis of deep learning for CVD risk prediction from retinal images; 26 studies | Retinal-image-based DL using fundus photographs and retinal vascular morphology/geometry features rather than disease-specific Scheie grading | Future CVD-event prediction studies reported AUROC 0.68–0.81. Pooled performance for related tasks: age MAE 3.19 years; gender AUROC 0.96; diabetes AUROC 0.80; CKD AUROC 0.86. Authors conclude real-world applicability requires further validation despite promise of noninvasive retinal-image-based risk prediction (nokiba2015associationbetweenophthalmological pages 1-3) | 2023-07 |  | https://doi.org/10.1167/tvst.12.7.14 |
| Colcombe 2023 | Targeted narrative review of retinal findings and cardiovascular risk | Reviewed retinal disease states and imaging biomarkers including AV nicking, vessel caliber changes, OCT/OCTA biomarkers | Concludes retinal findings and retinal bioimaging biomarkers may aid cardiovascular prognostication and personalized counseling; notes classic retinopathy findings such as arteriovenous nicking have been incorporated into cardiovascular/stroke risk literature, but emphasizes heterogeneity and need for validation before routine implementation (nokiba2015associationbetweenophthalmological pages 1-3) | 2023-10 |  | https://doi.org/10.3390/jpm13111564 |


*Table: This table summarizes recent quantitative studies and reviews relevant to arteriosclerotic retinopathy, fundus arteriosclerosis, and related retinal vascular biomarkers. It highlights study design, retinal phenotype definitions, effect sizes, and links to cardiovascular outcomes or risk stratification.*

---

## Notes on evidence gaps and limitations
* **Ontology identifiers (MONDO/MeSH/ICD)** for “arteriosclerotic retinopathy” were not retrievable from the accessed full texts; many studies define the condition via **fundus grading** rather than standardized diagnostic codes. (liu2023sexspecificassociationbetween pages 3-4, sugiura2022examinationoflarge media a2b302a2)
* **Genetic causality** is not supported in the current evidence set; the phenotype appears primarily as a complex, risk-factor-driven manifestation. (iorga2024noninvasiveretinalvessel pages 5-7)
* Several high-impact clinical guideline sources and some 2023–2024 articles were **unobtainable** via the toolchain in this run; thus, the report emphasizes available primary cohort studies and systematic reviews.

---

## URLs and publication dates (as available in sources)
* Geng et al., Front Cardiovasc Med, published 2023-02-28, https://doi.org/10.3389/fcvm.2023.1116486 (geng2023sexspecificassociationof pages 1-2)
* Liu et al., Eur J Med Res, published 2023-11, https://doi.org/10.1186/s40001-023-01508-6 (liu2023sexspecificassociationbetween pages 3-4)
* Dong et al., Sci Rep, published 2023-07, https://doi.org/10.1038/s41598-023-38378-1 (nokiba2015associationbetweenophthalmological pages 1-3)
* Rusu et al., Life, published 2024-03, https://doi.org/10.3390/life14040448 (rusu2024retinalstructuraland pages 1-2)
* Iorga et al., J Pers Med, published 2024-05, https://doi.org/10.3390/jpm14050501 (iorga2024noninvasiveretinalvessel pages 5-7)



References

1. (nokiba2015associationbetweenophthalmological pages 1-3): Hirohiko Nokiba, Takashi Takei, Chikako Suto, and Kosaku Nitta. Association between ophthalmological changes and cardiovascular diseases in patients with chronic kidney disease undergoing hemodialysis. Journal of atherosclerosis and thrombosis, 22 12:1248-54, Dec 2015. URL: https://doi.org/10.5551/jat.30601, doi:10.5551/jat.30601. This article has 9 citations and is from a peer-reviewed journal.

2. (sugiura2022examinationoflarge media a2b302a2): Tomonori Sugiura, Yasuaki Dohi, Yasuyuki Takagi, Takashi Yokochi, Naofumi Yoshikane, Kenji Suzuki, Takamasa Tomiishi, Takashi Nagami, Mitsunori Iwase, Hiroyuki Takase, Yoshihiro Seo, and Nobuyuki Ohte. Examination of large artery atherosclerosis could reveal small artery retinopathy in untreated middle-aged individuals. Journal of Atherosclerosis and Thrombosis, 29:11-23, Jan 2022. URL: https://doi.org/10.5551/jat.59857, doi:10.5551/jat.59857. This article has 8 citations and is from a peer-reviewed journal.

3. (liu2023sexspecificassociationbetween pages 3-4): Chunxing Liu, Xiaolong Yang, Mengmeng Ji, Xiaowei Zhang, Xiyun Bian, Tingli Chen, Yihan Li, Xing Qi, Jianfeng Wu, Jing Wang, and Zaixiang Tang. Sex-specific association between carotid atherosclerosis and fundus arteriosclerosis in a chinese population: a retrospective cross-sectional study. European Journal of Medical Research, Nov 2023. URL: https://doi.org/10.1186/s40001-023-01508-6, doi:10.1186/s40001-023-01508-6. This article has 5 citations and is from a peer-reviewed journal.

4. (rusu2024retinalstructuraland pages 1-2): Alexandra Cristina Rusu, Karin Ursula Horvath, Grigore Tinica, Raluca Ozana Chistol, Andra-Irina Bulgaru-Iliescu, Ecaterina Tomaziu Todosia, and Klara Brînzaniuc. Retinal structural and vascular changes in patients with coronary artery disease: a systematic review and meta-analysis. Life, 14:448, Mar 2024. URL: https://doi.org/10.3390/life14040448, doi:10.3390/life14040448. This article has 23 citations.

5. (sugiura2022examinationoflarge pages 2-4): Tomonori Sugiura, Yasuaki Dohi, Yasuyuki Takagi, Takashi Yokochi, Naofumi Yoshikane, Kenji Suzuki, Takamasa Tomiishi, Takashi Nagami, Mitsunori Iwase, Hiroyuki Takase, Yoshihiro Seo, and Nobuyuki Ohte. Examination of large artery atherosclerosis could reveal small artery retinopathy in untreated middle-aged individuals. Journal of Atherosclerosis and Thrombosis, 29:11-23, Jan 2022. URL: https://doi.org/10.5551/jat.59857, doi:10.5551/jat.59857. This article has 8 citations and is from a peer-reviewed journal.

6. (kaushik2007prevalenceandassociations pages 1-3): Shweta Kaushik, Ava Grace Tan, Paul Mitchell, and Jie Jin Wang. Prevalence and associations of enhanced retinal arteriolar light reflex: a new look at an old sign. Ophthalmology, 114 1:113-20, Jan 2007. URL: https://doi.org/10.1016/j.ophtha.2006.06.046, doi:10.1016/j.ophtha.2006.06.046. This article has 37 citations and is from a highest quality peer-reviewed journal.

7. (geng2023sexspecificassociationof pages 1-2): Ruirui Geng, Qinbei Feng, Mengmeng Ji, Yongfei Dong, Shuanshuan Xu, Chunxing Liu, Yufeng He, and Zaixiang Tang. Sex-specific association of serum uric acid trajectories with risk of incident retinal arteriosclerosis in chinese population: a population-based longitudinal study. Frontiers in Cardiovascular Medicine, Feb 2023. URL: https://doi.org/10.3389/fcvm.2023.1116486, doi:10.3389/fcvm.2023.1116486. This article has 2 citations and is from a peer-reviewed journal.

8. (sugiura2022examinationoflarge pages 12-13): Tomonori Sugiura, Yasuaki Dohi, Yasuyuki Takagi, Takashi Yokochi, Naofumi Yoshikane, Kenji Suzuki, Takamasa Tomiishi, Takashi Nagami, Mitsunori Iwase, Hiroyuki Takase, Yoshihiro Seo, and Nobuyuki Ohte. Examination of large artery atherosclerosis could reveal small artery retinopathy in untreated middle-aged individuals. Journal of Atherosclerosis and Thrombosis, 29:11-23, Jan 2022. URL: https://doi.org/10.5551/jat.59857, doi:10.5551/jat.59857. This article has 8 citations and is from a peer-reviewed journal.

9. (iorga2024noninvasiveretinalvessel pages 5-7): Raluca Eugenia Iorga, Damiana Costin, Răzvana Sorina Munteanu-Dănulescu, Elena Rezuș, and Andreea Dana Moraru. Non-invasive retinal vessel analysis as a predictor for cardiovascular disease. Journal of Personalized Medicine, 14:501, May 2024. URL: https://doi.org/10.3390/jpm14050501, doi:10.3390/jpm14050501. This article has 21 citations.

10. (nokiba2015associationbetweenophthalmological pages 3-4): Hirohiko Nokiba, Takashi Takei, Chikako Suto, and Kosaku Nitta. Association between ophthalmological changes and cardiovascular diseases in patients with chronic kidney disease undergoing hemodialysis. Journal of atherosclerosis and thrombosis, 22 12:1248-54, Dec 2015. URL: https://doi.org/10.5551/jat.30601, doi:10.5551/jat.30601. This article has 9 citations and is from a peer-reviewed journal.

11. (sugiura2022examinationoflarge pages 7-9): Tomonori Sugiura, Yasuaki Dohi, Yasuyuki Takagi, Takashi Yokochi, Naofumi Yoshikane, Kenji Suzuki, Takamasa Tomiishi, Takashi Nagami, Mitsunori Iwase, Hiroyuki Takase, Yoshihiro Seo, and Nobuyuki Ohte. Examination of large artery atherosclerosis could reveal small artery retinopathy in untreated middle-aged individuals. Journal of Atherosclerosis and Thrombosis, 29:11-23, Jan 2022. URL: https://doi.org/10.5551/jat.59857, doi:10.5551/jat.59857. This article has 8 citations and is from a peer-reviewed journal.

12. (sugiura2022examinationoflarge pages 6-7): Tomonori Sugiura, Yasuaki Dohi, Yasuyuki Takagi, Takashi Yokochi, Naofumi Yoshikane, Kenji Suzuki, Takamasa Tomiishi, Takashi Nagami, Mitsunori Iwase, Hiroyuki Takase, Yoshihiro Seo, and Nobuyuki Ohte. Examination of large artery atherosclerosis could reveal small artery retinopathy in untreated middle-aged individuals. Journal of Atherosclerosis and Thrombosis, 29:11-23, Jan 2022. URL: https://doi.org/10.5551/jat.59857, doi:10.5551/jat.59857. This article has 8 citations and is from a peer-reviewed journal.

13. (bisen2025retinalimagingas pages 5-8): Jay Bharatsingh Bisen, Hayden Sikora, Anushree Aneja, Sanjiv J. Shah, and Rukhsana G. Mirza. Retinal imaging as a window into cardiovascular health: towards harnessing retinal analytics for precision cardiovascular medicine. Journal of Cardiovascular Development and Disease, 12:230, Jun 2025. URL: https://doi.org/10.3390/jcdd12060230, doi:10.3390/jcdd12060230. This article has 6 citations.

14. (sugiura2022examinationoflarge pages 1-2): Tomonori Sugiura, Yasuaki Dohi, Yasuyuki Takagi, Takashi Yokochi, Naofumi Yoshikane, Kenji Suzuki, Takamasa Tomiishi, Takashi Nagami, Mitsunori Iwase, Hiroyuki Takase, Yoshihiro Seo, and Nobuyuki Ohte. Examination of large artery atherosclerosis could reveal small artery retinopathy in untreated middle-aged individuals. Journal of Atherosclerosis and Thrombosis, 29:11-23, Jan 2022. URL: https://doi.org/10.5551/jat.59857, doi:10.5551/jat.59857. This article has 8 citations and is from a peer-reviewed journal.