---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T12:23:03.475988'
end_time: '2026-05-08T12:32:46.336847'
duration_seconds: 582.86
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Spondyloepimetaphyseal Dysplasia Bieganski Type
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spondyloepimetaphyseal Dysplasia Bieganski Type
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spondyloepimetaphyseal Dysplasia Bieganski Type** covering all of the
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
- **Disease Name:** Spondyloepimetaphyseal Dysplasia Bieganski Type
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spondyloepimetaphyseal Dysplasia Bieganski Type** covering all of the
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


## Comprehensive Research Report: Spondyloepimetaphyseal Dysplasia, Bieganski Type (SEMD-BT)

### Executive summary and nomenclature clarification
The label **“spondyloepimetaphyseal dysplasia, Bieganski type” (SEMD-BT)** is used inconsistently across the literature and can refer to at least two *genetically distinct* conditions with overlapping historical SEMD terminology: (i) an **X-linked AIFM1-associated** disorder combining **spondylometaphyseal/epimetaphyseal dysplasia and cerebral hypomyelination/neurodegeneration**; and (ii) an **autosomal recessive MBTPS1-associated** disorder commonly called **spondyloepiphyseal dysplasia, Kondo–Fu type (SEDKF)** / SEMD with **elevated plasma lysosomal enzymes** and cataracts. Because knowledge-base entries require unambiguous mapping, this report documents both entities and highlights discriminating features (X-linked hypomyelination vs elevated plasma lysosomal enzymes/cataracts). (mierzewska2017spondyloepimetaphysealdysplasiawith pages 1-2, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 1-4, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 8-11, raggio2024exomesequencingreveals pages 1-2, carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, kondo2018site1proteasedeficiency pages 1-2, OpenTargets Search: spondyloepimetaphyseal dysplasia Bieganski type,spondyloepimetaphyseal dysplasia-MBTPS1)

| Entity often confused under overlapping SEMD terminology | Core identifier(s) | Gene | Inheritance | Hallmark features | Key reported variants / molecular mechanism | Notes / nomenclature warning |
|---|---|---|---|---|---|---|
| X-linked spondylometaphyseal dysplasia with cerebral hypomyelination; also described as SEMD with neurodegeneration / SEMD-MR | OMIM 300232 (as cited in later literature) | **AIFM1** | X-linked recessive | Distinctive facial appearance; short stature; kyphoscoliosis/chest deformity; metaphyseal/spinal/epiphyseal dysplasia; hypomyelination; slowly progressive central and peripheral neurodegeneration; onset around 1 year; reported delayed myelination/small corpus callosum/cortical atrophy; later papers emphasize male infants with hypotonia and marked cerebral hypomyelination, followed by later-emerging skeletal dysplasia (mierzewska2017spondyloepimetaphysealdysplasiawith pages 1-2, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 1-4, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 8-11, temtamy2007geneticheterogeneityin pages 18-20) | **p.Asp237Gly** reported in 2017 as segregating in affected families; disease-associated variants cluster at/near the **intron 6/exon 7 boundary**; exon 7 skipping proposed as a shared mechanism; later reports include intronic and synonymous exon 7 variants causing **exon 7 skipping** (mierzewska2017spondyloepimetaphysealdysplasiawith pages 1-2, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 1-4, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 8-11) | Frequently called **SMD-H** or **X-linked hypomyelination with spondylometaphyseal dysplasia** in the literature; despite historical SEMD/Bieganski linkage, this is a genetically distinct **AIFM1** disorder. Confirm whether the user means the neurodegenerative/hypomyelinating X-linked entity (mierzewska2017spondyloepimetaphysealdysplasiawith pages 1-2, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 1-4, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 8-11, temtamy2007geneticheterogeneityin pages 18-20) |
| MBTPS1-related spondyloepiphyseal dysplasia (Kondo-Fu type); also reported as SEMD / skeletal dysplasia with elevated plasma lysosomal enzymes | OMIM 618392 | **MBTPS1** | Autosomal recessive | Severe growth retardation/short stature; cataracts; dysmorphic features (often retromicrognathia/retrognathia); kyphosis or other vertebral anomalies; osteopenia/low bone mineral density; epiphyseal/metaphyseal irregularities; hernias; some cases with epilepsy, craniosynostosis, sleep apnea; characteristic lab clue is **elevated plasma lysosomal enzymes** with normal leukocyte enzyme activity in several cases (raggio2024exomesequencingreveals pages 1-2, carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, carvalho2020spondyloepimetaphysealdysplasiawith pages 3-4, chen2023casereportrecombinant pages 4-6, kondo2018site1proteasedeficiency pages 1-2, raggio2024exomesequencingreveals pages 2-4, raggio2024exomesequencingreveals pages 4-6) | First reported patient had **biallelic MBTPS1 variants** yielding ~**1% functional transcripts**; later variants include **c.2948G>A p.Trp983Ter**, **c.774C>T** causing **exon 6 skipping**, **c.2355delG p.Met785fs**, **c.1094A>G p.Asp365Gly**, **c.2255G>T p.Gly752Val**, and **c.2831+5G>T** causing **exon 21 skipping**; mechanism involves defective S1P function, impaired BBF2H7 activation, collagen retention in chondrocytes, and partial M6P-trafficking failure with abnormal lysosomal enzyme secretion (carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, carvalho2020spondyloepimetaphysealdysplasiawith pages 3-4, liaqat2024acaseof pages 1-2, kondo2018site1proteasedeficiency pages 1-2, raggio2024exomesequencingreveals pages 4-6) | This is a distinct **MBTPS1** skeletal dysplasia, usually called **SED Kondo-Fu type** or **MBTPS1-related spondyloepiphyseal dysplasia**, but some papers describe it with SEMD-like wording. Confirm whether the user means the **AR lysosomal-enzyme-elevation/cataract** entity rather than the X-linked **AIFM1** hypomyelination syndrome (raggio2024exomesequencingreveals pages 1-2, carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, carvalho2020spondyloepimetaphysealdysplasiawith pages 3-4, chen2023casereportrecombinant pages 4-6, liaqat2024acaseof pages 1-2, kondo2018site1proteasedeficiency pages 1-2, raggio2024exomesequencingreveals pages 2-4, raggio2024exomesequencingreveals pages 4-6) |


*Table: This table distinguishes two genetically different skeletal dysplasia entities that are often conflated because of overlapping historical SEMD nomenclature. It helps clarify whether a source is referring to the X-linked AIFM1 hypomyelination/neurodegeneration syndrome or the autosomal recessive MBTPS1 Kondo-Fu/elevated-lysosomal-enzyme disorder.*

---

## 1. Disease Information

### 1.1 Overview
**SEMD-BT** is an ultra-rare Mendelian skeletal dysplasia historically defined by radiographic involvement of the **spine (spondylo-)**, **epiphyses (epimetaphyseal/epiphyseal)**, and **metaphyses**, with short stature and variable extraskeletal features. In modern molecular literature, “Bieganski type” is most consistently tied to a severe **X-linked** disorder with **hypomyelinating leukodystrophy/neurodegeneration** and a skeletal dysplasia phenotype (AIFM1), while a separate **autosomal recessive** SEMD/SED phenotype with **elevated plasma lysosomal enzymes** is caused by MBTPS1. (mierzewska2017spondyloepimetaphysealdysplasiawith pages 1-2, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 1-4, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 8-11, carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, kondo2018site1proteasedeficiency pages 1-2)

### 1.2 Key identifiers
- **MONDO**: Open Targets lists **“spondyloepimetaphyseal dysplasia, Bieganski type” as MONDO_0010275**. URL: https://platform.opentargets.org/ (OpenTargets Search: spondyloepimetaphyseal dysplasia Bieganski type,spondyloepimetaphyseal dysplasia-MBTPS1)
- **OMIM**:
  - For the AIFM1-linked X-linked entity, later sources cite **SEMD-MR as MIM 300232**. (mierzewska2017spondyloepimetaphysealdysplasiawith pages 1-2, temtamy2007geneticheterogeneityin pages 18-20)
  - For the MBTPS1-linked Kondo–Fu skeletal dysplasia entity, multiple sources cite **MIM 618392**. (carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, liaqat2024acaseof pages 1-2)

*ICD-10/ICD-11, MeSH, and Orphanet identifiers were not retrievable from the currently available evidence corpus in this run; therefore, they are not asserted here.*

### 1.3 Common synonyms / alternative names (as used in sources)
- **AIFM1-associated**: “X-linked spondylometaphyseal dysplasia with cerebral hypomyelination (SMD-H)”; “X-linked hypomyelination with spondylometaphyseal dysplasia”; “SEMD with neurodegeneration”; “SEMD-MR”. (mierzewska2017spondyloepimetaphysealdysplasiawith pages 1-2, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 1-4, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 8-11)
- **MBTPS1-associated**: “Spondyloepiphyseal dysplasia, Kondo–Fu type (SEDKF)”; “spondyloepimetaphyseal dysplasia with elevated plasma lysosomal enzymes”; “MBTPS1-related spondyloepiphyseal dysplasia”. (carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, kondo2018site1proteasedeficiency pages 1-2, raggio2024exomesequencingreveals pages 1-2)

### 1.4 Evidence sources
Most information is from **aggregated disease-level literature (case reports/series and reviews)**, not EHR-derived cohort studies. (edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 1-4, carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, kondo2018site1proteasedeficiency pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors (genetic)
Two primary genetic etiologies appear in the literature under overlapping SEMD terminology:

#### (A) AIFM1-related X-linked SEMD with cerebral hypomyelination/neurodegeneration
- **Gene**: *AIFM1* (apoptosis-inducing factor mitochondria-associated 1). (mierzewska2017spondyloepimetaphysealdysplasiawith pages 1-2, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 1-4)
- **Inheritance**: **X-linked recessive** (male predominance, no male-to-male transmission). (temtamy2007geneticheterogeneityin pages 18-20)
- **Abstract quote (supporting definition and gene-region mechanism)**: “Spondylometaphyseal dysplasia with cerebral hypomyelination (SMD‐H) is a very rare but distinctive phenotype, unusually combining spondylometaphyseal dysplasia with hypomyelinating leukodystrophy. Recently, SMD‐H has been associated with variants confined to a specific intra‐genic locus involving Exon 7…”. (American Journal of Medical Genetics Part A; Jan 2021; https://doi.org/10.1002/ajmg.a.62072) (edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 1-4)

#### (B) MBTPS1-related autosomal recessive SEMD/SED with elevated plasma lysosomal enzymes (SED Kondo–Fu type)
- **Gene**: *MBTPS1* (membrane bound transcription factor peptidase, site 1), encoding **Site-1 protease (S1P)**. (carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, kondo2018site1proteasedeficiency pages 1-2)
- **Inheritance**: **Autosomal recessive** (biallelic loss-of-function / compound heterozygosity / homozygosity). (carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, liaqat2024acaseof pages 1-2, raggio2024exomesequencingreveals pages 4-6)
- **Abstract quote (causal claim and key biochemical phenotype)**: “Here, we report a pediatric patient with an amorphic and a severely hypomorphic mutation in MBTPS1… a frequency of functional MBTPS1 transcripts of approximately 1%, a finding that is associated with skeletal dysplasia and elevated blood lysosomal enzymes.” (JCI Insight; Jul 2018; https://doi.org/10.1172/jci.insight.121596) (kondo2018site1proteasedeficiency pages 1-2)

### 2.2 Risk factors / protective factors / gene–environment interactions
For both entities, the available evidence supports **monogenic causation** and does not identify validated environmental risk factors, protective factors, or gene–environment interactions beyond standard Mendelian recurrence risks. (temtamy2007geneticheterogeneityin pages 18-20, kondo2018site1proteasedeficiency pages 1-2)

---

## 3. Phenotypes (clinical and radiographic)

### 3.1 AIFM1-associated X-linked SEMD with hypomyelination (SMD-H)
**Phenotype types**: developmental/neurologic signs, skeletal dysplasia, characteristic neuroimaging.

Key reported phenotypes (with suggested HPO terms):
- **Hypomyelinating leukodystrophy / delayed myelination** (HP:0003432 Abnormal myelination; HP:0002188 Hypomyelination). (edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 1-4, temtamy2007geneticheterogeneityin pages 18-20)
- **Progressive neurodegeneration involving CNS/PNS** (HP:0002344 Progressive neurologic deterioration; HP:0003324 Generalized hypotonia; HP:0001263 Global developmental delay). (mierzewska2017spondyloepimetaphysealdysplasiawith pages 1-2, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 1-4)
- **Microcephaly** (HP:0000252 Microcephaly) and **intellectual disability** (HP:0001249 Intellectual disability) noted in historical descriptions. (temtamy2007geneticheterogeneityin pages 18-20)
- **Skeletal dysplasia involving spine/metaphyses/epiphyses** (HP:0002650 Spondyloepimetaphyseal dysplasia; HP:0000925 Abnormality of the vertebral column; HP:0002758 Abnormal metaphysis morphology; HP:0002657 Abnormal epiphysis morphology). (mierzewska2017spondyloepimetaphysealdysplasiawith pages 1-2, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 8-11, temtamy2007geneticheterogeneityin pages 18-20)
- **Kyphoscoliosis / thoracolumbar deformity** (HP:0002751 Kyphoscoliosis; HP:0005619 Thoracolumbar kyphosis) and **joint contractures** (HP:0001371 Flexion contracture). (mierzewska2017spondyloepimetaphysealdysplasiawith pages 1-2, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 8-11, temtamy2007geneticheterogeneityin pages 18-20)

**Temporal pattern**: onset around infancy with progressive neurologic decline; skeletal findings may be more apparent later in childhood. (mierzewska2017spondyloepimetaphysealdysplasiawith pages 1-2, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 1-4)

**Radiographic and imaging descriptors (examples)**: “irregular, flared and cupped metaphyses with metaphyseal striations,” small irregular epiphyses, platyspondyly/hyperkyphosis, and brain MRI “diffuse supratentorial hypomyelination”. (edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 8-11)

### 3.2 MBTPS1-associated SEDKF / SEMD with elevated plasma lysosomal enzymes
**Phenotype types**: disproportionate growth failure, ophthalmologic findings, skeletal radiographic findings, and characteristic laboratory abnormalities.

Key phenotypes (with suggested HPO terms):
- **Severe short stature / growth retardation** (HP:0004322 Short stature). (raggio2024exomesequencingreveals pages 1-2, carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, raggio2024exomesequencingreveals pages 2-4)
- **Early-onset cataracts** (HP:0000518 Cataract). (carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, liaqat2024acaseof pages 1-2, raggio2024exomesequencingreveals pages 2-4)
- **Spondyloepiphyseal/epimetaphyseal dysplasia on X-ray** (HP:0002650 Spondyloepimetaphyseal dysplasia; HP:0000925 Abnormality of the vertebral column; HP:0002808 Kyphosis). (carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, kondo2018site1proteasedeficiency pages 1-2, raggio2024exomesequencingreveals pages 4-6)
- **Low bone mineral density / osteopenia** (HP:0004349 Low bone mineral density; HP:0000938 Osteopenia). (carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, chen2023casereportrecombinant pages 4-6, raggio2024exomesequencingreveals pages 1-2)
- **Hernias** (HP:0000023 Inguinal hernia; HP:0001537 Umbilical hernia). (chen2023casereportrecombinant pages 4-6, liaqat2024acaseof pages 1-2, raggio2024exomesequencingreveals pages 2-4)
- **Craniosynostosis** (HP:0001363 Craniosynostosis) and **epilepsy/seizures** (HP:0001250 Seizures) in some cases. (carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3)
- **Elevated plasma lysosomal enzymes with normal leukocyte enzyme activity** (laboratory phenotype; map to LOINC/SNOMED locally). (carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, carvalho2020spondyloepimetaphysealdysplasiawith pages 3-4, kondo2018site1proteasedeficiency pages 1-2)

**Recent quantitative statistics (2024)**: A 2024 case report summarizing previous cases reported that **“80% had low stature, 70% low weight, 80% had bilateral cataracts and 70% showed Spondyloepiphyseal dysplasia on X-rays.”** (Diagnostics; Jan 2024; https://doi.org/10.3390/diagnostics14030313) (raggio2024exomesequencingreveals pages 1-2)

**Example laboratory values (2020 case report)**: multiple plasma lysosomal enzymes were markedly elevated; e.g., total plasma beta-hexosaminidases **3,975 nmol/h/ml (reference 400–1,400)**; iduronate-2-sulfatase **1,080 nmol/4 h/ml (reference 167–475)**; alpha-N-acetylgalactosaminidase **648 nmol/17 h/ml (reference 60–240)**. (carvalho2020spondyloepimetaphysealdysplasiawith pages 3-4)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes
- *AIFM1* (X-linked disorder with hypomyelination + skeletal dysplasia). (mierzewska2017spondyloepimetaphysealdysplasiawith pages 1-2, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 1-4)
- *MBTPS1* (autosomal recessive SEDKF/SEMD with elevated plasma lysosomal enzymes). (carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, kondo2018site1proteasedeficiency pages 1-2)

### 4.2 Pathogenic variants and variant classes

#### AIFM1 entity (X-linked)
- **p.Asp237Gly in AIFM1** identified by WES as the single plausible candidate segregating with disease in two families; reported as novel and predicted pathogenic in silico. (mierzewska2017spondyloepimetaphysealdysplasiawith pages 1-2)
- Multiple families show variants clustered at/near **AIFM1 intron 6/exon 7 boundary**, with evidence supporting **exon 7 skipping** as a shared pathogenic mechanism. (edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 1-4, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 8-11)

#### MBTPS1 entity (autosomal recessive)
Primary literature variants include:
- **Homozygous nonsense**: **p.Trp983Ter** (NM_003791.2 c.2948G>A; exon 22) (2020 case report). (carvalho2020spondyloepimetaphysealdysplasiawith pages 3-4)
- **Compound heterozygous** (2024): **c.2355delG p.Met785fs** (frameshift, predicted NMD) and **c.1094A>G p.Asp365Gly** (missense). (raggio2024exomesequencingreveals pages 4-6)
- **Splice-altering synonymous**: **c.774C>T (p.A258=) causing exon 6 skipping** (validated by transcript analysis/minigene assay; 2023). Abstract quote: “The transcript analysis in vivo exhibited that the synonymous variant c.774C > T caused exon 6 skipping. The minigene splice assay in vitro confirmed the alteration of MBTPS1 mRNA splicing…”. (Frontiers in Pediatrics; Jan 2023; https://doi.org/10.3389/fped.2022.1056141) (raggio2024exomesequencingreveals pages 1-2)
- **Compound heterozygous** (2024): **c.2255G>T p.(Gly752Val)** and **c.2831+5G>T** with RNA-seq showing exon 21 skipping and predicted frameshift **p.(Ser901fs28*)** with nonsense-mediated decay. (liaqat2024acaseof pages 1-2)
- **First described S1P deficiency (2018)**: biallelic variants resulting in **~1% functional MBTPS1 transcripts**. (kondo2018site1proteasedeficiency pages 1-2)

**Population allele frequencies / ClinVar classifications** were not directly retrievable from the current evidence set; therefore, ACMG category assertions are not made here.

### 4.3 Modifier genes / epigenetics / chromosomal abnormalities
No validated modifier genes, epigenetic signatures, or recurrent chromosomal abnormalities specific to SEMD-BT were identified in the retrieved primary literature in this run. (mierzewska2017spondyloepimetaphysealdysplasiawith pages 1-2, kondo2018site1proteasedeficiency pages 1-2)

---

## 5. Environmental Information
No non-genetic environmental contributors are established for these monogenic skeletal dysplasias in the retrieved evidence. (kondo2018site1proteasedeficiency pages 1-2)

---

## 6. Mechanism / Pathophysiology

### 6.1 MBTPS1 (Site-1 protease) deficiency: ER stress, collagen trafficking, and lysosomal enzyme mistargeting
**Upstream trigger**: biallelic MBTPS1 variants reduce functional S1P activity. (kondo2018site1proteasedeficiency pages 1-2)

**Causal chain (proposed in primary literature)**:
1. Residual S1P activity may be sufficient for some systemic lipid homeostasis, but **insufficient for ER and lysosomal functions in chondrocytes**. (kondo2018site1proteasedeficiency pages 1-2)
2. Defective S1P impairs activation of the ER stress transducer **BBF2H7**, causing **ER retention of collagen in chondrocytes**. (kondo2018site1proteasedeficiency pages 1-2)
3. S1P deficiency partially impairs **mannose-6-phosphate (M6P)-dependent delivery to lysosomes**, resulting in **abnormal secretion/elevation of lysosomal enzymes in blood**. (kondo2018site1proteasedeficiency pages 1-2)
4. These combined defects contribute to **chondrocyte apoptosis** and **lysosomal enzyme-mediated degradation of bone matrix**, producing the skeletal dysplasia phenotype. (kondo2018site1proteasedeficiency pages 1-2)

**Abstract quote (mechanistic)**: “The defective S1P function specifically impairs activation of the ER stress transducer BBF2H7, leading to ER retention of collagen in chondrocytes. S1P deficiency also causes abnormal secretion of lysosomal enzymes due to partial impairment of mannose-6-phosphate-dependent delivery to lysosomes.” (JCI Insight; Jul 2018; https://doi.org/10.1172/jci.insight.121596) (kondo2018site1proteasedeficiency pages 1-2)

**Ontology suggestions**:
- GO Biological Process (examples): ER stress response; protein folding; collagen fibril organization; lysosomal transport; glycoprotein trafficking; chondrocyte apoptosis.
- CL cell types (examples): **chondrocyte** (CL:0000138); osteoblast (CL:0000062).
- UBERON (examples): cartilage (UBERON:0002416); growth plate cartilage (UBERON:0002597); vertebral column (UBERON:0001137).

### 6.2 AIFM1 exon 7-region variants: hypomyelination + skeletal dysplasia via tissue-specific AIFM1 effects
Primary literature supports a genotype–phenotype pattern in which **variants near exon 7** (often splice-affecting) associate with the combined **skeletal + hypomyelination** syndrome, with evidence that **exon 7 skipping** is a common mechanism. (edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 1-4, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 8-11)

**Mechanistic interpretation (from authors)**: exon 7 of AIFM1 is proposed to be “integral to its functional role in cells involved in cartilage and bone development and turnover,” and RNA evidence supports aberrant splicing with exon 7 loss. (edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 8-11)

**Ontology suggestions**:
- GO BP: myelination; mitochondrial respiratory chain complex assembly; apoptosis regulation.
- CL: oligodendrocyte (CL:0000128); chondrocyte (CL:0000138).
- UBERON: cerebral white matter (UBERON:0004706); cartilage; vertebral column.

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
- **Skeletal system** (spine, epiphyses/metaphyses; kyphosis/kyphoscoliosis; osteopenia). (edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 8-11, carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, raggio2024exomesequencingreveals pages 4-6)
- **Central nervous system white matter** (hypomyelination in AIFM1-associated entity). (edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 1-4, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 8-11)
- **Eye lens** (cataracts in MBTPS1-associated entity). (raggio2024exomesequencingreveals pages 1-2, carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, liaqat2024acaseof pages 1-2)

### 7.2 Tissue/cell level
- Growth plate cartilage and **chondrocytes** are highlighted as especially vulnerable in MBTPS1 deficiency. (kondo2018site1proteasedeficiency pages 1-2)

### 7.3 Subcellular level (MBTPS1 mechanism)
- Endoplasmic reticulum (collagen retention) and Golgi/lysosome trafficking axis (M6P pathway) are implicated. (kondo2018site1proteasedeficiency pages 1-2)

---

## 8. Temporal Development
- **AIFM1 entity**: infancy onset (~1 year) with progressive neurodegeneration; skeletal findings may be recognized as the child develops. (mierzewska2017spondyloepimetaphysealdysplasiawith pages 1-2, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 1-4)
- **MBTPS1 entity**: congenital/early-childhood onset with severe growth failure, early cataracts, and evolving spinal/epiphyseal findings; some later complications (sleep apnea, back pain, etc.) noted in case summaries. (raggio2024exomesequencingreveals pages 1-2, chen2023casereportrecombinant pages 4-6, raggio2024exomesequencingreveals pages 4-6)

---

## 9. Inheritance and Population

### 9.1 Inheritance
- **AIFM1-associated**: **X-linked recessive**. (temtamy2007geneticheterogeneityin pages 18-20)
- **MBTPS1-associated**: **autosomal recessive**. (carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, liaqat2024acaseof pages 1-2, raggio2024exomesequencingreveals pages 4-6)

### 9.2 Epidemiology
Formal prevalence/incidence estimates were not identified in the retrieved evidence; available data are case-based.
- A 2021 review-style case expansion states **“To date 19 patients from 8 families have been reported”** for SMD-H (AIFM1 exon 7–region). (American Journal of Medical Genetics Part A; Jan 2021; https://doi.org/10.1002/ajmg.a.62072) (edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 1-4)
- A 2024 MBTPS1 case report states it is (to their knowledge) the **7th molecularly confirmed SEDKF case worldwide (2018–2023)** and the **10th case with MBTPS1-related phenotypes**. (Diagnostics; Jan 2024; https://doi.org/10.3390/diagnostics14030313) (raggio2024exomesequencingreveals pages 4-6)

---

## 10. Diagnostics

### 10.1 Clinical and imaging diagnosis
- **Skeletal survey / X-ray**: used to identify spondyloepiphyseal/epimetaphyseal dysplasia, metaphyseal irregularity, vertebral body changes, osteopenia, and craniosynostosis-related skull changes (e.g., “copper-beaten skull”). (edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 8-11, carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, carvalho2020spondyloepimetaphysealdysplasiawith pages 3-4, raggio2024exomesequencingreveals pages 4-6)
- **Brain MRI**: essential in suspected AIFM1-associated SMD-H, showing diffuse hypomyelination and reduced white matter volume. (edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 8-11)
- **Ophthalmologic exam**: cataracts are common in MBTPS1-associated disease. (raggio2024exomesequencingreveals pages 1-2, carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, liaqat2024acaseof pages 1-2)

### 10.2 Laboratory biomarkers
- **Plasma lysosomal enzymes**: a key clue for MBTPS1 deficiency; elevation in plasma with normal leukocyte enzyme activity is repeatedly described. (carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, carvalho2020spondyloepimetaphysealdysplasiawith pages 3-4, kondo2018site1proteasedeficiency pages 1-2)

### 10.3 Genetic testing approach
- **Exome/genome sequencing** is repeatedly used to diagnose both AIFM1- and MBTPS1-related disorders. (mierzewska2017spondyloepimetaphysealdysplasiawith pages 1-2, kondo2018site1proteasedeficiency pages 1-2, raggio2024exomesequencingreveals pages 4-6)
- **RNA studies / splice assays** can be required, since synonymous or intronic variants may act through exon skipping (AIFM1 exon 7; MBTPS1 exon 6 or exon 21). (edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 8-11, raggio2024exomesequencingreveals pages 1-2, liaqat2024acaseof pages 1-2)

### 10.4 Differential diagnosis
Differential considerations include other SEMD/SMD subtypes and lysosomal-storage-disorder-like phenocopies; an older SEMD radiologic review emphasizes distinguishing SEMD forms from Dyggve–Melchior–Clausen (DMC) by features such as the iliac crest “lacy” appearance, which was absent in the Bieganski-described neurocognitive SEMD form. (temtamy2007geneticheterogeneityin pages 18-20)

---

## 11. Outcomes / Prognosis
- **AIFM1 entity**: primary literature describes **progressive neurodegeneration** with severe disability and death in adolescence in historical families (as summarized in later genetic work). (mierzewska2017spondyloepimetaphysealdysplasiawith pages 1-2)
- **MBTPS1 entity**: outcomes appear variable; complications include severe growth failure, orthopedic morbidity (kyphosis, spinal changes), sleep apnea, seizures in some, and ectodermal findings in newer reports; robust survival statistics are not available due to limited case numbers. (carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, liaqat2024acaseof pages 1-2, raggio2024exomesequencingreveals pages 4-6)

---

## 12. Treatment / Management

### 12.1 Disease-modifying / targeted therapy
No approved disease-modifying therapy was identified for either entity in the retrieved evidence.

### 12.2 Supportive and symptomatic management (real-world implementations)
- **Orthopedic monitoring and management** for kyphosis/kyphoscoliosis, hip dysplasia, and osteopenia/low bone mineral density are implicit in reported care; specific surgical outcome series were not retrieved. (carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3, raggio2024exomesequencingreveals pages 4-6)
- **Cataract surgery** has been performed (e.g., congenital lamellar cataract surgically removed). (carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3)
- **Sleep apnea management** is reported as a clinical feature requiring recognition (MBTPS1 case). (raggio2024exomesequencingreveals pages 1-2)
- **Seizure management** is required in cases with epilepsy. (carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3)

### 12.3 Growth hormone (GH) therapy (reported application)
A 2023 case report describes **recombinant human growth hormone (rhGH)** treatment in MBTPS1-associated SEDKF, with the authors concluding: “Growth hormone therapy can repair growth retardation in patients with spondyloepiphyseal dysplasia, Kondo-Fu type; however, more evidence of such patient cases is required to support this hypothesis.” (Frontiers in Pediatrics; Feb 2023; https://doi.org/10.3389/fped.2023.1068718) (chen2023casereportrecombinant pages 4-6)

### 12.4 MAXO term suggestions (examples)
- Cataract extraction (MAXO term for cataract surgery)
- Treatment with recombinant human growth hormone (MAXO term for GH therapy)
- Physical therapy / orthopedic surveillance
- Antiseizure medication therapy

### 12.5 Clinical trials
A clinical trials registry search in this run did not yield clearly relevant interventional trials specifically for SEMD-BT/MBTPS1/AIFM1 skeletal dysplasia. (OpenTargets Search: spondyloepimetaphyseal dysplasia Bieganski type,spondyloepimetaphyseal dysplasia-MBTPS1)

---

## 13. Prevention
Primary prevention is not applicable for established Mendelian disorders, but **genetic counseling** and **reproductive options** (carrier testing in X-linked families; carrier testing and prenatal/preimplantation diagnosis in autosomal recessive MBTPS1 families) are the standard prevention framework; specific guidelines were not retrieved in the current evidence set. (temtamy2007geneticheterogeneityin pages 18-20, raggio2024exomesequencingreveals pages 4-6)

---

## 14. Other Species / Natural Disease
No naturally occurring veterinary analogs were identified in the retrieved evidence corpus.

---

## 15. Model Organisms
The retrieved primary mechanism paper emphasizes **chondrocyte-specific vulnerability** and includes experimental correction of variants and ER stress reduction to mitigate collagen-trafficking defects, implying utility of **cellular models** (patient-derived cells/chondrocytes) for mechanism and therapeutic screening. (kondo2018site1proteasedeficiency pages 1-2)

---

## 16. Recent developments and latest research (prioritize 2023–2024)

### 2023: Synonymous MBTPS1 variant proven pathogenic via splicing assays
A 2023 report provides direct functional evidence that a **synonymous MBTPS1 variant (c.774C>T)** is pathogenic by causing **exon 6 skipping**, validated in vivo and with a minigene assay, and notes partial restoration of exon inclusion with an antisense oligonucleotide in vitro. (Frontiers in Pediatrics; Jan 2023; https://doi.org/10.3389/fped.2022.1056141) (raggio2024exomesequencingreveals pages 1-2)

### 2024: Expanded MBTPS1 phenotype and variant spectrum
- A 2024 diagnostics case report adds new compound heterozygous variants (**c.2355delG p.Met785fs** and **c.1094A>G p.Asp365Gly**) and provides cross-case feature frequencies (e.g., cataracts and SED on imaging). (Diagnostics; Jan 2024; https://doi.org/10.3390/diagnostics14030313) (raggio2024exomesequencingreveals pages 1-2, raggio2024exomesequencingreveals pages 4-6)
- A 2024 AJMG-A report describes additional systemic/ectodermal features and uses RNA-seq to confirm exon skipping and predicted NMD for a splice variant (Dec 2024; https://doi.org/10.1002/ajmg.a.63499). (liaqat2024acaseof pages 1-2)

### Expert perspective / authoritative synthesis
A key expert mechanistic statement from the 2018 JCI Insight paper is that these findings “define a new congenital human skeletal disorder” and “reveal that S1P is particularly required for skeletal development in humans.” (JCI Insight; Jul 2018; https://doi.org/10.1172/jci.insight.121596) (kondo2018site1proteasedeficiency pages 1-2)

---

## Limitations of this report
- Several requested identifiers (Orphanet, ICD-10/ICD-11, MeSH) and population allele frequency statistics (gnomAD) could not be confirmed from the retrievable evidence in this tool run; they are therefore not asserted.
- Because the name “Bieganski type” is ambiguous across sources, a definitive single-entity KB entry should be anchored to one gene/OMIM/MONDO axis after curation; this report provides the evidence needed to make that disambiguation. (OpenTargets Search: spondyloepimetaphyseal dysplasia Bieganski type,spondyloepimetaphyseal dysplasia-MBTPS1, edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 1-4, raggio2024exomesequencingreveals pages 1-2, kondo2018site1proteasedeficiency pages 1-2)

References

1. (mierzewska2017spondyloepimetaphysealdysplasiawith pages 1-2): H. Mierzewska, M. Rydzanicz, T. Biegański, J. Kosinska, M. Mierzewska‐Schmidt, A. Ługowska, A. Pollak, P. Stawiński, A. Walczak, A. Kędra, E. Obersztyn, E. Szczepanik, and R. Płoski. Spondyloepimetaphyseal dysplasia with neurodegeneration associated with aifm1 mutation – a novel phenotype of the mitochondrial disease. Clinical Genetics, 91:30-37, Jan 2017. URL: https://doi.org/10.1111/cge.12792, doi:10.1111/cge.12792. This article has 62 citations and is from a peer-reviewed journal.

2. (edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 1-4): Katharine Edgerley, Angela Barnicoat, Amaka C. Offiah, Alistair D. Calder, Kshitij Mankad, Nicholas Simon Thomas, David J. Bunyan, Maggie Williams, Chris Buxton, Arniban Majumdar, Kayal Vijayakumar, Tom Hilliard, James Turner, Christine P. Burren, Fergal Monsell, and Sarah F. Smithson. Aifm1‐associated x‐linked spondylometaphyseal dysplasia with cerebral hypomyelination. American Journal of Medical Genetics Part A, 185:1228-1235, Jan 2021. URL: https://doi.org/10.1002/ajmg.a.62072, doi:10.1002/ajmg.a.62072. This article has 7 citations.

3. (edgerley2021aifm1‐associatedx‐linkedspondylometaphyseal pages 8-11): Katharine Edgerley, Angela Barnicoat, Amaka C. Offiah, Alistair D. Calder, Kshitij Mankad, Nicholas Simon Thomas, David J. Bunyan, Maggie Williams, Chris Buxton, Arniban Majumdar, Kayal Vijayakumar, Tom Hilliard, James Turner, Christine P. Burren, Fergal Monsell, and Sarah F. Smithson. Aifm1‐associated x‐linked spondylometaphyseal dysplasia with cerebral hypomyelination. American Journal of Medical Genetics Part A, 185:1228-1235, Jan 2021. URL: https://doi.org/10.1002/ajmg.a.62072, doi:10.1002/ajmg.a.62072. This article has 7 citations.

4. (raggio2024exomesequencingreveals pages 1-2): Víctor Raggio, Soledad Rodríguez, Sandra Feder, Rosario Gueçaimburú, and Lucía Spangenberg. Exome sequencing reveals biallelic mutations in mbtps1 gene in a girl with a very rare skeletal dysplasia. Diagnostics, 14:313, Jan 2024. URL: https://doi.org/10.3390/diagnostics14030313, doi:10.3390/diagnostics14030313. This article has 3 citations.

5. (carvalho2020spondyloepimetaphysealdysplasiawith pages 1-3): Daniel R. Carvalho, Carlos E. Speck‐Martins, Jaime M. Brum, Carlos R. Ferreira, and Nara L. M. Sobreira. Spondyloepimetaphyseal dysplasia with elevated plasma lysosomal enzymes caused by homozygous variant in mbtps1. American Journal of Medical Genetics Part A, 182:1796-1800, May 2020. URL: https://doi.org/10.1002/ajmg.a.61614, doi:10.1002/ajmg.a.61614. This article has 23 citations.

6. (kondo2018site1proteasedeficiency pages 1-2): Yuji Kondo, Jianxin Fu, Hua Wang, Christopher Hoover, J. Michael McDaniel, Richard Steet, Debabrata Patra, Jianhua Song, Laura Pollard, Sara Cathey, Tadayuki Yago, Graham Wiley, Susan Macwana, Joel Guthridge, Samuel McGee, Shibo Li, Courtney Griffin, Koichi Furukawa, Judith A. James, Changgeng Ruan, Rodger P. McEver, Klaas J. Wierenga, Patrick M. Gaffney, and Lijun Xia. Site-1 protease deficiency causes human skeletal dysplasia due to defective inter-organelle protein trafficking. JCI insight, Jul 2018. URL: https://doi.org/10.1172/jci.insight.121596, doi:10.1172/jci.insight.121596. This article has 68 citations and is from a domain leading peer-reviewed journal.

7. (OpenTargets Search: spondyloepimetaphyseal dysplasia Bieganski type,spondyloepimetaphyseal dysplasia-MBTPS1): Open Targets Query (spondyloepimetaphyseal dysplasia Bieganski type,spondyloepimetaphyseal dysplasia-MBTPS1, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

8. (temtamy2007geneticheterogeneityin pages 18-20): SA Temtamy, MS Aglan, and MA El-Gammal. Genetic heterogeneity in spondylo-epimetaphyseal dysplasias: a clinical and radiological study. Unknown journal, 2007.

9. (carvalho2020spondyloepimetaphysealdysplasiawith pages 3-4): Daniel R. Carvalho, Carlos E. Speck‐Martins, Jaime M. Brum, Carlos R. Ferreira, and Nara L. M. Sobreira. Spondyloepimetaphyseal dysplasia with elevated plasma lysosomal enzymes caused by homozygous variant in mbtps1. American Journal of Medical Genetics Part A, 182:1796-1800, May 2020. URL: https://doi.org/10.1002/ajmg.a.61614, doi:10.1002/ajmg.a.61614. This article has 23 citations.

10. (chen2023casereportrecombinant pages 4-6): Congli Chen, Jin Wu, and Ying Liu. Case report: recombinant human growth hormone therapy in a patient with spondyloepiphyseal dysplasia, kondo-fu type. Frontiers in Pediatrics, Feb 2023. URL: https://doi.org/10.3389/fped.2023.1068718, doi:10.3389/fped.2023.1068718. This article has 8 citations.

11. (raggio2024exomesequencingreveals pages 2-4): Víctor Raggio, Soledad Rodríguez, Sandra Feder, Rosario Gueçaimburú, and Lucía Spangenberg. Exome sequencing reveals biallelic mutations in mbtps1 gene in a girl with a very rare skeletal dysplasia. Diagnostics, 14:313, Jan 2024. URL: https://doi.org/10.3390/diagnostics14030313, doi:10.3390/diagnostics14030313. This article has 3 citations.

12. (raggio2024exomesequencingreveals pages 4-6): Víctor Raggio, Soledad Rodríguez, Sandra Feder, Rosario Gueçaimburú, and Lucía Spangenberg. Exome sequencing reveals biallelic mutations in mbtps1 gene in a girl with a very rare skeletal dysplasia. Diagnostics, 14:313, Jan 2024. URL: https://doi.org/10.3390/diagnostics14030313, doi:10.3390/diagnostics14030313. This article has 3 citations.

13. (liaqat2024acaseof pages 1-2): Khurram Liaqat, Kayla Treat, Lili Mantcheva, Abdul Nasir, David D. Weaver, Erin Conboy, and Francesco Vetrini. A case of mbtps1‐related disorder due to compound heterozygous variants in mbtps1 gene: genotype–phenotype expansion and the emergence of a novel syndrome. American Journal of Medical Genetics Part A, Dec 2024. URL: https://doi.org/10.1002/ajmg.a.63499, doi:10.1002/ajmg.a.63499. This article has 4 citations.