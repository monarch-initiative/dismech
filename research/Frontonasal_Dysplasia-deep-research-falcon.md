---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T12:18:48.780860'
end_time: '2026-05-08T12:34:17.504114'
duration_seconds: 928.72
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Frontonasal Dysplasia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Frontonasal Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Frontonasal Dysplasia** covering all of the
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
- **Disease Name:** Frontonasal Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Frontonasal Dysplasia** covering all of the
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


# Frontonasal Dysplasia (FND): Comprehensive Disease Characteristics Research Report (Mendelian)

## Executive summary
Frontonasal dysplasia (FND) is a rare, congenital craniofacial midline malformation spectrum attributed to abnormal development of the frontonasal process and associated cranial neural crest–derived tissues, producing variable combinations of ocular hypertelorism, nasal clefting/bifidity, and midline facial clefting; in some patients, ocular and brain malformations co-occur. (guo2024prenataldiagnosisof pages 1-3, farlie2016frontonasaldysplasiatowards pages 1-2)

The most evidence-supported Mendelian causes in the retrieved literature are (i) autosomal recessive ALX-family disorders (ALX1, ALX3, ALX4; often labeled FND3/FND1/FND2 respectively) and (ii) X-linked EFNB1-related craniofrontonasal syndrome (CFNS), a closely related frontonasal/craniosynostosis disorder that can overlap clinically but has distinct ectodermal and craniosynostosis features and a characteristic sex-severity paradox. (vargel2022alxrelatedfrontonasaldysplasias pages 1-2, twigg2009frontorhinyadistinctive pages 2-3, kayserili2009alx4dysfunctiondisrupts pages 2-3, farlie2016frontonasaldysplasiatowards pages 4-5)

Recent (2023–2024) literature emphasizes (a) improved prenatal recognition using 3D ultrasound and collation of prenatal-case phenotypic frequencies, (b) new/ongoing delineation of ALX4-related FND2 via case reports, and (c) mechanistic advances connecting upstream neural crest transcriptional regulators (TFAP2) to an ALX genetic pathway essential for midfacial development. (guo2024prenataldiagnosisof pages 1-3, goswami2024ararehomozygous pages 1-2, nguyen2024tfap2paralogsregulate pages 1-3)

---

## 1. Disease information

### 1.1 What is the disease?
FND is a rare congenital anomaly caused by abnormal/insufficient development of the frontonasal process with a broad phenotypic spectrum affecting the eyes, nose, and forehead. (guo2024prenataldiagnosisof pages 1-3)

**Direct abstract quote (prenatal context):** Guo et al. state: “Only approximately 10 cases of prenatally diagnosed nonsyndromic FND have been reported in the past 30 years.” (BMC Pregnancy and Childbirth; 2024-06; https://doi.org/10.1186/s12884-024-06619-4) (guo2024prenataldiagnosisof pages 1-3)

### 1.2 Key identifiers
Evidence in the retrieved sources supports the following OMIM/MIM identifiers:
- **FND (overall)**: **MIM 136760** (vargel2022alxrelatedfrontonasaldysplasias pages 1-2, vargel2022alxrelatedfrontonasaldysplasias pages 2-3)
- **FND1 (ALX3-related / frontorhiny phenotype in some literature)**: **MIM 136760** as used in a genotype-based surgical cohort (vargel2022alxrelatedfrontonasaldysplasias pages 2-3)
- **FND2 (ALX4-related)**: **MIM 613451** (vargel2022alxrelatedfrontonasaldysplasias pages 2-3)
- **FND3 (ALX1-related)**: **MIM 613456** (vargel2022alxrelatedfrontonasaldysplasias pages 2-3)

**Not available from retrieved evidence:** MONDO ID, Orphanet ID, MeSH ID, ICD-10/ICD-11 codes were not found in the retrieved full texts and therefore cannot be asserted here.

### 1.3 Common synonyms / alternative names
Guo et al. explicitly list the following synonyms for FND:
- **Median cleft face syndrome**
- **Frontonasal syndrome**
- **Frontonasal dysostosis** (guo2024prenataldiagnosisof pages 1-3)

### 1.4 Evidence sources (patient-level vs aggregated)
Most actionable information in the retrieved corpus derives from:
- **Individual case reports and families** (e.g., ALX4 case report, prenatal FND case report) (goswami2024ararehomozygous pages 1-2, guo2024prenataldiagnosisof pages 1-3)
- **Aggregated cohorts/case series** (e.g., an 89-patient single-institution clinical/surgical series; prenatal-case literature aggregation) (vargel2022alxrelatedfrontonasaldysplasias pages 2-3, guo2024prenataldiagnosisof pages 3-5)
- **Mechanistic studies using iPSCs and animal models** (zebrafish, mouse) to connect genotype to cellular phenotypes (pini2020alx1‐ pages 1-2, iyyanar2022alx1deficientmice pages 1-2, yoon2022zebrafishmodelsof pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors

#### 2.1.1 Genetic causes (major, evidence-supported)
1) **ALX-related FND subtypes (Mendelian, primarily autosomal recessive)**
- **FND1 (ALX3)**, **FND2 (ALX4)**, **FND3 (ALX1)** are described as distinct genotypic categories in a genotype-informed surgical cohort. (vargel2022alxrelatedfrontonasaldysplasias pages 2-3)
- These genes encode homeobox transcription factors crucial for craniofacial development and neural-crest-derived mesenchyme patterning. (pini2020alx1‐ pages 1-2, iyyanar2022alx1deficientmice pages 1-2)

2) **EFNB1-related craniofrontonasal syndrome (CFNS) (X-linked)**
- EFNB1 mutations cause CFNS, which features frontonasal anomalies plus craniosynostosis and ectodermal findings; females typically have more severe manifestations than males due to mosaic “cellular interference.” (farlie2016frontonasaldysplasiatowards pages 4-5, pachajoa2023casereportcraniofrontonasal pages 1-3)

#### 2.1.2 Developmental mechanism as etiology (frontonasal process biology)
FND is framed as arising from disruption of the **frontonasal process**, which contains ectoderm over **neural-crest-derived mesenchyme** and is influenced by forebrain neuroepithelium—providing a developmental rationale for co-occurring craniofacial and CNS anomalies. (farlie2016frontonasaldysplasiatowards pages 1-2)

### 2.2 Risk factors

#### 2.2.1 Genetic risk factors
- **ALX3 (FND1/frontorhiny)**: biallelic/homozygous pathogenic variants are associated with affected phenotypes, while heterozygous relatives often lack facial manifestations in reported families. (twigg2009frontorhinyadistinctive pages 2-3)
- **ALX4 (FND2)**: homozygous variants in consanguineous families are strongly associated with FND2; heterozygotes in some families can show milder features. (kayserili2009alx4dysfunctiondisrupts pages 2-3, hussain2020anovelmissense pages 1-2)
- **ALX1 (FND3)**: pathogenic variants are associated with severe craniofacial and ocular malformations and mechanistic neural-crest defects. (pini2020alx1‐ pages 1-2)
- **EFNB1 (CFNS)**: heterozygous females are typically more severely affected than hemizygous males. (farlie2016frontonasaldysplasiatowards pages 4-5, pachajoa2023casereportcraniofrontonasal pages 1-3)

#### 2.2.2 Environmental risk factors / teratogens
A gene–environment interaction relevant to midfacial malformations is suggested by zebrafish: **ethanol exposure increased penetrance of facial/ocular malformations in alx1 mutants**, consistent with a protective role for alx genes against ethanol-induced oxidative stress in neural crest lineages. (yoon2022zebrafishmodelsof pages 1-2)

### 2.3 Protective factors
- In zebrafish models, **alx3 upregulation in alx1 mutants** is interpreted as compensatory/transcriptional adaptation that can reduce penetrance in single mutants relative to double mutants. (yoon2022zebrafishmodelsof pages 1-2)

### 2.4 Gene–environment interactions
- **Ethanol–alx1 interaction (model organism evidence):** ethanol exposure increases malformation penetrance in alx1 mutants; oxidative stress response is implicated as a mechanistic target. (yoon2022zebrafishmodelsof pages 1-2)

---

## 3. Phenotypes

### 3.1 Core clinical phenotype (FND)
Common/defining findings include:
- **True ocular hypertelorism** (HPO: **HP:0000316**) (farlie2016frontonasaldysplasiatowards pages 1-2)
- **Broad nasal bridge/root** (HPO: **HP:0000431**)
- **Bifid nasal tip / nasal bifidity** (HPO: **HP:0005931**) (guo2024prenataldiagnosisof pages 1-3)
- **Median facial cleft** (HPO: **HP:0000280**) (guo2024prenataldiagnosisof pages 1-3)
- **Widow’s peak or V-shaped hairline** (HPO: **HP:0000349** as “widow’s peak”) (guo2024prenataldiagnosisof pages 1-3)

**Onset:** congenital (prenatal/neonatal), by definition of a congenital malformation spectrum. (guo2024prenataldiagnosisof pages 1-3)

### 3.2 Diagnostic criteria (clinical definition)
Farlie et al. present historically derived defining features and note that **a diagnosis generally requires at least two defining features** (e.g., hypertelorism, broad nasal root, nasal tip deficiency/bifidity, median facial cleft, alar clefting, widow’s peak). (farlie2016frontonasaldysplasiatowards pages 1-2)

### 3.3 Subtype-specific phenotype patterns (genotype–phenotype)
From a genotype-informed cohort:
- **ALX1 / FND3:** ocular involvement is striking; severe microphthalmia/anophthalmia, facial clefts, nasal deformities. (vargel2022alxrelatedfrontonasaldysplasias pages 1-2, vargel2022alxrelatedfrontonasaldysplasias pages 2-3)
- **ALX3 / FND1:** widened philtrum and prominent philtral columns/swellings; bifid nasal tip and hypoplastic columella. (vargel2022alxrelatedfrontonasaldysplasias pages 1-2, vargel2022alxrelatedfrontonasaldysplasias pages 2-3)
- **ALX4 / FND2:** severe hypertelorism, brachycephaly, large parietal bone defects, broad nasal dorsum/bridge, alopecia; may include genital and CNS anomalies. (vargel2022alxrelatedfrontonasaldysplasias pages 1-2, farlie2016frontonasaldysplasiatowards pages 4-5, goswami2024ararehomozygous pages 1-2)

### 3.4 Prenatal phenotype frequencies (recent quantitative data; 2024)
Guo et al. summarize prenatally diagnosed **nonsyndromic** cases (literature plus their case):
- **Hypertelorism:** 9/9
- **Deformed nose:** 8/9
- **Cleft lip/palate:** 8/9
- **Hypoplasia of other craniofacial bones:** 6/9
- **Abnormal ears:** 2/9
They also note **CNS malformations were the most commonly observed features** in this prenatal subset (examples include corpus callosum agenesis/hypoplasia, cephalocele, hydrocephalus). (guo2024prenataldiagnosisof pages 3-5)

### 3.5 Quality of life impact
Direct quantitative quality-of-life instruments (EQ-5D/SF-36/PROMIS) were not present in the retrieved evidence. Clinical/surgical literature emphasizes psychosocial and functional motivations for early and staged craniofacial reconstruction, implying substantial potential impact on social function and adaptation. (vargel2022alxrelatedfrontonasaldysplasias pages 5-6)

---

## 4. Genetic / molecular information

### 4.1 Causal genes (major)
- **ALX1** (FND3) (vargel2022alxrelatedfrontonasaldysplasias pages 2-3, pini2020alx1‐ pages 1-2)
- **ALX3** (FND1 / frontorhiny) (twigg2009frontorhinyadistinctive pages 2-3)
- **ALX4** (FND2) (kayserili2009alx4dysfunctiondisrupts pages 2-3, hussain2020anovelmissense pages 1-2)
- **EFNB1** (craniofrontonasal syndrome) (farlie2016frontonasaldysplasiatowards pages 4-5, pachajoa2023casereportcraniofrontonasal pages 1-3)

### 4.2 Pathogenic variants (examples with variant class)

#### ALX3 (frontorhiny / FND1)
Twigg et al. identify “four different mutations of ALX3 (all homozygous)” including:
- Splice-acceptor: **c.595-2A>T**
- Missense: **c.608A>G (p.Asn203Ser)**
- Homeodomain missense: **c.502C>G (p.Leu168Val)**
They report evidence consistent with autosomal recessive inheritance (heterozygous relatives without facial manifestations in their cohort). (twigg2009frontorhinyadistinctive pages 2-3)

Ullah et al. report a homozygous nonsense variant:
- **c.604C>T (p.Gln202*)**, predicted LoF via NMD/truncation. (ullah2018exomesequencingrevealed pages 3-4)

#### ALX4 (FND2)
- Kayserili et al. report a **homozygous nonsense** ALX4 variant in consanguineous families (HGVS details not present in the retrieved excerpt) causing craniofacial and epidermal development disruption (including alopecia). (kayserili2009alx4dysfunctiondisrupts pages 2-3)
- Hussain et al. report **NM_021926.4:c.652C>T (p.Arg218Trp)**, homozygous in severely affected individuals and associated with milder phenotypes in heterozygous carriers in the same family. (hussain2020anovelmissense pages 1-2)

#### ALX1 (FND3)
- Pini et al. identify a homeodomain missense variant **p.Leu165Phe (L165F)** and connect it to neural crest cell apoptosis/migration defects and altered BMP2/BMP9 signaling. (pini2020alx1‐ pages 1-2)

#### EFNB1 (craniofrontonasal syndrome)
- Pachajoa et al. report a novel heterozygous EFNB1 variant **c.374A>C (p.Glu125Ala)**. (pachajoa2023casereportcraniofrontonasal pages 1-3)

### 4.3 Functional consequences (current understanding)
ALX-related FND is supported as primarily involving **loss-of-function / impaired transcription factor function** that perturbs neural crest biology; variants frequently affect the **homeodomain**, consistent with disrupted DNA binding and downstream gene regulation. (twigg2009frontorhinyadistinctive pages 2-3, kayserili2009alx4dysfunctiondisrupts pages 2-3)

EFNB1-related CFNS is mechanistically explained by mosaicism from X-inactivation leading to **“cellular interference”** (aberrant cell sorting and ectopic boundaries), disrupting osteogenic differentiation and calvarial development. (farlie2016frontonasaldysplasiatowards pages 4-5)

### 4.4 Modifier genes / epigenetics
No validated human modifier genes or disease-specific epigenetic signatures were identified in the retrieved evidence.

### 4.5 Chromosomal abnormalities
A surgical cohort reports an ALX1-related case with a **homozygous 3.7 Mb deletion** as a causal lesion for FND3. (vargel2022alxrelatedfrontonasaldysplasias pages 2-3)

---

## 5. Environmental information
No specific toxins, occupational exposures, or infectious triggers were identified in the retrieved evidence as causes of FND. The primary non-genetic factor with mechanistic experimental support in retrieved texts is ethanol exposure in zebrafish alx1 mutants (developmental teratogen context). (yoon2022zebrafishmodelsof pages 1-2)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (ALX-related FND; evidence-based)
**Upstream genetic lesion (ALX1/ALX3/ALX4 variant) → neural crest developmental disruption → frontonasal mesenchyme hypoplasia/patterning defects → craniofacial midline malformations.** (pini2020alx1‐ pages 1-2, iyyanar2022alx1deficientmice pages 1-2)

Key mechanistic steps supported by experiments:
- **Neural crest apoptosis and migration defects:** Patient-derived iPSC neural crest cells homozygous for ALX1L165F show increased apoptosis and impaired migration; zebrafish lineage tracing demonstrates defective migration of anterior cranial NCC streams. (pini2020alx1‐ pages 1-2)
- **BMP pathway dysregulation as a mediator:** Altered BMP levels in NCC-conditioned media (low BMP2, high BMP9) with rescue of migration defects by soluble BMP2 or BMP9 antagonism. (pini2020alx1‐ pages 1-2)
- **Patterning identity shifts in craniofacial mesenchyme (mouse):** Alx1 deletion increases periocular mesenchyme apoptosis and alters regional identity (loss of Pax7; ectopic Lhx6/Lhx8), providing a developmental basis for nasal/facial clefts and ocular defects. (iyyanar2022alx1deficientmice pages 1-2, iyyanar2022alx1deficientmice pages 9-11)
- **Oxidative stress and ethanol interaction (zebrafish):** alx genes regulate oxidative stress response; ethanol exposure increases malformation penetrance in alx1 mutants. (yoon2022zebrafishmodelsof pages 1-2)

### 6.2 Upstream regulators and recent developments (2024)
Nguyen et al. (Development; 2024-01; https://doi.org/10.1242/dev.202095) report that TFAP2 paralogs regulate midfacial development partly by **directly and positively regulating ALX gene expression**, based on bulk/single-cell RNA-seq and ChIP-seq, with cross-species evidence in mouse and zebrafish. (nguyen2024tfap2paralogsregulate pages 1-3)

### 6.3 Suggested ontology terms
**Cell type (CL):**
- Cranial neural crest cell (CL term not provided in retrieved evidence; suggested mapping: “neural crest cell”)

**Anatomy (UBERON):**
- Frontonasal process; frontonasal prominence; periocular mesenchyme; lateral nasal process; anterior neurocranium (concepts supported in mechanism papers). (farlie2016frontonasaldysplasiatowards pages 1-2, iyyanar2022alx1deficientmice pages 9-11)

**Biological processes (GO; suggested based on evidence):**
- Neural crest cell migration
- Regulation of apoptotic process
- Craniofacial morphogenesis
- BMP signaling pathway
- Response to oxidative stress (pini2020alx1‐ pages 1-2, yoon2022zebrafishmodelsof pages 1-2)

---

## 7. Anatomical structures affected
**Primary:** craniofacial midline structures derived from the frontonasal process and cranial neural crest (nose, midface, frontonasal skeleton) (farlie2016frontonasaldysplasiatowards pages 1-2, pini2020alx1‐ pages 1-2)

**Frequent associated structures:**
- **Eyes/orbits** (microphthalmia/anophthalmia, coloboma; especially ALX1/FND3) (vargel2022alxrelatedfrontonasaldysplasias pages 2-3, iyyanar2022alx1deficientmice pages 1-2)
- **Brain/CNS midline structures** (e.g., corpus callosum anomalies in FND2 and in prenatal cases) (farlie2016frontonasaldysplasiatowards pages 4-5, guo2024prenataldiagnosisof pages 3-5)
- **Skull/calvaria** (parietal bone defects/foramina; craniosynostosis in some ALX4 and EFNB1 disorders) (farlie2016frontonasaldysplasiatowards pages 4-5, pachajoa2023casereportcraniofrontonasal pages 1-3)

---

## 8. Temporal development
- **Onset:** congenital; can be detected prenatally by ultrasound in some cases. (guo2024prenataldiagnosisof pages 1-3)
- **Critical periods:** embryonic craniofacial development during neural crest migration and frontonasal prominence formation; model evidence suggests vulnerability to ethanol-induced oxidative stress in this developmental window. (yoon2022zebrafishmodelsof pages 1-2)

---

## 9. Inheritance and population

### 9.1 Epidemiology (available evidence)
Quantitative prevalence/incidence was not available in the retrieved full texts. The strongest “rarity statistic” in retrieved evidence is prenatal ascertainment:
- **“Only approximately 10 cases of prenatally diagnosed nonsyndromic FND have been reported in the past 30 years”** (Guo 2024). (guo2024prenataldiagnosisof pages 1-3)

### 9.2 Inheritance patterns
- **ALX3/frontorhiny (FND1):** autosomal recessive; homozygous affected individuals; heterozygous relatives generally unaffected in Twigg et al. (twigg2009frontorhinyadistinctive pages 2-3)
- **ALX1/FND3:** autosomal recessive forms reported; mechanistic evidence from a missense variant family is consistent with a causal ALX1 defect affecting NCC biology. (pini2020alx1‐ pages 1-2)
- **ALX4/FND2:** often autosomal recessive in consanguineous families (homozygous nonsense/missense); heterozygous mild phenotypes can occur. (kayserili2009alx4dysfunctiondisrupts pages 2-3, hussain2020anovelmissense pages 1-2)
- **EFNB1/CFNS:** X-linked; paradoxically more severe in heterozygous females; mechanistically linked to mosaic cellular interference. (farlie2016frontonasaldysplasiatowards pages 4-5, pachajoa2023casereportcraniofrontonasal pages 1-3)

### 9.3 Population notes
Case evidence includes families/populations from multiple regions (e.g., Turkish consanguineous families with ALX4; Colombian EFNB1 case; Bangladeshi ALX4 case report), supporting broad geographic occurrence rather than a single endemic population (no founder-effect statistics were present in retrieved evidence). (kayserili2009alx4dysfunctiondisrupts pages 2-3, pachajoa2023casereportcraniofrontonasal pages 1-3, goswami2024ararehomozygous pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical criteria
- Clinical diagnosis uses recognition of characteristic craniofacial features; a minimum of **two characteristic findings** is noted as diagnostic in recent prenatal review discussion. (guo2024prenataldiagnosisof pages 1-3)

### 10.2 Imaging
- **Prenatal ultrasound (including 3D ultrasound):** 3D ultrasound is highlighted as useful for detecting facial and limb deformities. (guo2024prenataldiagnosisof pages 1-3)

### 10.3 Genetic testing strategy (as implemented in recent reports)
In a severe prenatal case, a comprehensive genetic workup included:
- **Karyotype analysis**
- **Copy-number variant (CNV) analysis**
- **Trio-WES and trio-WGS**, with no de novo variants detected in the fetus in that report (guo2024prenataldiagnosisof pages 1-3)

In the prenatal nonsyndromic aggregation, genetic testing across cases was often negative (karyotype performed for all; CNV and targeted testing in subsets). (guo2024prenataldiagnosisof pages 3-5)

For postnatal Mendelian diagnosis, evidence supports targeted sequencing/panels covering:
- **ALX1, ALX3, ALX4** (ALX-related FND)
- **EFNB1** (CFNS, especially if coronal craniosynostosis and ectodermal findings are present) (vargel2022alxrelatedfrontonasaldysplasias pages 1-2, farlie2016frontonasaldysplasiatowards pages 4-5)

### 10.4 Differential diagnosis
The retrieved evidence explicitly notes diagnostic complexity in prenatal settings and that additional anomalies can complicate syndrome assignment; a cited example differential is **amniotic band sequence** when limb anomalies accompany craniofacial findings. (guo2024prenataldiagnosisof pages 6-7)

---

## 11. Outcome / prognosis
Quantitative survival/mortality statistics were not found in the retrieved evidence. Prognosis is implied to be dominated by:
- **Severity of craniofacial clefting and ocular malformations (ALX1/FND3 particularly severe)** (vargel2022alxrelatedfrontonasaldysplasias pages 2-3, iyyanar2022alx1deficientmice pages 1-2)
- **Presence of CNS malformations in prenatal cases** (guo2024prenataldiagnosisof pages 3-5)
- **Requirement for multi-stage reconstructive surgery** with craniofacial teams (vargel2022alxrelatedfrontonasaldysplasias pages 5-6)

---

## 12. Treatment (current applications / real-world implementation)
No pharmacologic disease-modifying therapies were identified in the retrieved evidence; treatment is predominantly surgical and supportive.

### 12.1 Surgical and interventional management (evidence-based)
A large single-institution surgical cohort (89 evaluated; 13 genetically confirmed ALX-related cases) proposes genotype-informed management, including:
- **Facial bipartition / bipartition osteotomy** for severe hypertelorism and midface alignment (vargel2022alxrelatedfrontonasaldysplasias pages 5-6, vargel2022alxrelatedfrontonasaldysplasias pages 1-2)
- **Fronto-orbital advancement** (and distraction osteogenesis in severe cases) (vargel2022alxrelatedfrontonasaldysplasias pages 5-6)
- **Cleft lip/palate repair** (vargel2022alxrelatedfrontonasaldysplasias pages 1-2)
- **Nasal reconstruction** and staged craniofacial procedures (vargel2022alxrelatedfrontonasaldysplasias pages 5-6)
- **Eyelid coloboma repair** (vargel2022alxrelatedfrontonasaldysplasias pages 1-2)

### 12.2 Supportive care / complication management
Reported associated issues and supportive interventions include:
- **Serous otitis media requiring tympanostomy tubes** in some patients (vargel2022alxrelatedfrontonasaldysplasias pages 5-6)

### 12.3 Suggested MAXO terms (examples; based on described interventions)
- Craniofacial reconstructive surgery (facial bipartition)
- Fronto-orbital advancement
- Cleft lip repair / cleft palate repair
- Rhinoplasty / nasal reconstruction
- Tympanostomy tube placement (vargel2022alxrelatedfrontonasaldysplasias pages 5-6, vargel2022alxrelatedfrontonasaldysplasias pages 1-2)

### 12.4 Clinical trials
No FND-specific clinical trials were identified in the retrieved ClinicalTrials-like searches (none were retrieved), consistent with the predominantly surgical management paradigm.

---

## 13. Prevention
Primary prevention is limited because most forms are Mendelian congenital malformations.

Evidence-supported prevention/mitigation concepts:
- **Genetic counseling** for families with autosomal recessive ALX-related disease or X-linked EFNB1 disease, given the clear inheritance patterns documented in families. (twigg2009frontorhinyadistinctive pages 2-3, farlie2016frontonasaldysplasiatowards pages 4-5)
- **Avoidance of prenatal ethanol exposure** is biologically plausible and supported by zebrafish alx1 gene–environment evidence linking ethanol to increased malformation penetrance via oxidative stress. (yoon2022zebrafishmodelsof pages 1-2)

---

## 14. Other species / natural disease
A naturally occurring “frontonasal dysplasia” phenotype has been associated with an **ALX1 variant in Burmese cats**, demonstrating cross-species relevance of ALX genes to frontonasal morphology (though detailed phenotype data were not extracted in the gathered evidence snippets). (farlie2016frontonasaldysplasiatowards pages 6-6)

---

## 15. Model organisms
Evidence supports the following models and what they recapitulate:

### 15.1 Zebrafish
- **alx1;alx3 double mutants** develop highly penetrant cranial and ocular defects resembling human ALX1-linked FND; anterior cranial neural crest migration defects and ocular vasculature/anterior segment abnormalities are reported; oxidative stress response implicated; ethanol increases penetrance in alx1 mutants. (yoon2022zebrafishmodelsof pages 1-2)

### 15.2 Mouse
- **Alx1 deletion mice** recapitulate FND-like craniofacial malformations; mechanistic findings include periocular mesenchyme apoptosis, reduced Pitx2/Lmxb1, optic stalk morphogenesis defects, and altered frontonasal mesenchyme identity (Pax7 loss; ectopic Lhx6/8). (iyyanar2022alx1deficientmice pages 1-2, iyyanar2022alx1deficientmice pages 9-11)

### 15.3 Human iPSC-derived neural crest (in vitro)
- Patient iPSC-derived NCC demonstrate apoptosis and migration defects with ALX1L165F; BMP2/BMP9 manipulation rescues migration defects, providing a tractable human cell model for mechanism testing. (pini2020alx1‐ pages 1-2)

---

## High-value structured summary (genes/subtypes/phenotypes)
| Condition/entity | Causal gene(s) | Inheritance pattern (supported by evidence) | Representative pathogenic variants (HGVS if available) | Key distinguishing phenotypes | Key sources |
|---|---|---|---|---|---|
| Frontonasal dysplasia (overall) | Genetically heterogeneous; ALX1, ALX3, ALX4 are major ALX-related causes; EFNB1 causes the related craniofrontonasal syndrome within the broader differential | Heterogeneous: autosomal recessive ALX1/ALX3 forms; ALX4 can be recessive and in some families dominant/vertical transmission; EFNB1 disorder is X-linked (vargel2022alxrelatedfrontonasaldysplasias pages 1-2, farlie2016frontonasaldysplasiatowards pages 4-5, bertola2013verticaltransmissionof pages 5-5) | Not a single recurrent variant across all FND; examples occur in subtype rows below | Midline craniofacial malformation spectrum including true ocular hypertelorism, broad nasal root/bridge, bifid or hypoplastic nasal tip, median facial cleft, alar clefts, and widow’s peak/V-shaped hairline (farlie2016frontonasaldysplasiatowards pages 1-2, guo2024prenataldiagnosisof pages 1-3) | Vargel 2022, DOI:10.1177/10556656211019621; Farlie 2016, DOI:10.1159/000450533; Guo 2024, DOI:10.1186/s12884-024-06619-4 |
| FND1 / frontorhiny | ALX3 | Autosomal recessive; affected individuals homozygous, heterozygous relatives typically unaffected (twigg2009frontorhinyadistinctive pages 2-3, ullah2018exomesequencingrevealed pages 3-4) | c.595-2A>T; c.608A>G (p.Asn203Ser); c.502C>G (p.Leu168Val); c.604C>T (p.Gln202*) (twigg2009frontorhinyadistinctive pages 2-3, ullah2018exomesequencingrevealed pages 3-4) | Widened/long philtrum with prominent bilateral periphiltral swellings or philtral columns, bifid nasal tip, hypoplastic columella, slit-like nares/columellar pit, hypertelorism, ptosis; generally lacks parietal foramina (vargel2022alxrelatedfrontonasaldysplasias pages 1-2, vargel2022alxrelatedfrontonasaldysplasias pages 2-3, kayserili2012mildnasalmalformations pages 7-8) | Twigg 2009, DOI:10.1016/j.ajhg.2009.04.009; Ullah 2018, DOI:10.1038/s10038-017-0358-y; Vargel 2022, DOI:10.1177/10556656211019621 |
| FND2 | ALX4 | Usually autosomal recessive in homozygous cases from consanguineous families; milder heterozygous phenotypes/vertical transmission also reported in some families (kayserili2009alx4dysfunctiondisrupts pages 2-3, el‐ruby2018identificationofa pages 5-5, hussain2020anovelmissense pages 1-2, bertola2013verticaltransmissionof pages 5-5) | c.652C>T (p.Arg218Trp); c.291delG (p.Gln98Serfs*83); c.793C>T; homozygous nonsense ALX4 variant reported in 2009 study but HGVS not provided in gathered evidence (hussain2020anovelmissense pages 1-2, el‐ruby2018identificationofa pages 5-5, vargel2022alxrelatedfrontonasaldysplasias pages 2-3) | Severe hypertelorism, brachycephaly, broad/depressed nasal bridge or dorsum, bifid nose, large parietal skull defects/parietal foramina, alopecia, craniosynostosis, hypogonadism/genital anomalies, brain anomalies including corpus callosum defects (vargel2022alxrelatedfrontonasaldysplasias pages 1-2, farlie2016frontonasaldysplasiatowards pages 4-5, vargel2022alxrelatedfrontonasaldysplasias pages 2-3, goswami2024ararehomozygous pages 1-2) | Kayserili 2009, DOI:10.1093/hmg/ddp391; El-Ruby 2018, DOI:10.1002/ajmg.a.38655; Hussain 2020, DOI:10.1089/gtmb.2019.0203; Goswami 2024, DOI:10.1016/j.heliyon.2024.e34929 |
| FND3 | ALX1 | Autosomal recessive (vargel2022alxrelatedfrontonasaldysplasias pages 7-7, ullah2018exomesequencingrevealed pages 3-4) | c.531+1G>A; homozygous ~3.7 Mb deletion involving ALX1; p.Leu165Phe missense variant linked to defective neural crest cell development/migration (vargel2022alxrelatedfrontonasaldysplasias pages 2-3, pini2020alx1‐ pages 1-2) | Most severe ALX-related subtype: bilateral severe microphthalmia/anophthalmia, upper eyelid colobomata, bilateral facial clefts, complete cleft palate, hypoplastic alae nasi, wide nasal bridge, brachycephaly, absent brows/eyelashes, major ocular involvement (vargel2022alxrelatedfrontonasaldysplasias pages 1-2, vargel2022alxrelatedfrontonasaldysplasias pages 2-3, farlie2016frontonasaldysplasiatowards pages 1-2) | Uz 2010, DOI:10.1016/j.ajhg.2010.04.002; Pini 2020, DOI:10.15252/emmm.202012013; Vargel 2022, DOI:10.1177/10556656211019621 |
| Craniofrontonasal syndrome | EFNB1 | X-linked; paradoxically more severe in heterozygous females than hemizygous males due to cellular interference/X-inactivation mosaicism (farlie2016frontonasaldysplasiatowards pages 4-5, pachajoa2023casereportcraniofrontonasal pages 1-3) | c.374A>C (p.Glu125Ala); broader EFNB1 spectrum includes missense, nonsense, frameshift, and splice variants, many in exons 2–3/Eph-binding domain (pachajoa2023casereportcraniofrontonasal pages 1-3, 12025clinicalandmolecular pages 6-6, pachajoa2023casereportcraniofrontonasal pages 3-4) | Coronal craniosynostosis with facial asymmetry, severe hypertelorism, bifid or hypoplastic nasal tip, nail ridging/splitting, wiry/curly hair, skeletal anomalies; males often milder (farlie2016frontonasaldysplasiatowards pages 4-5, pachajoa2023casereportcraniofrontonasal pages 1-3) | Pachajoa 2023, DOI:10.3389/fgene.2022.1092301; Farlie 2016, DOI:10.1159/000450533 |


*Table: This table summarizes the principal genetic entities relevant to frontonasal dysplasia and closely related craniofrontonasal syndrome, including causal genes, inheritance, representative variants, and distinguishing phenotypes. It is useful as a compact genotype-phenotype reference based only on the gathered evidence.*

---

## Expert synthesis / interpretation (evidence-based)
1) The strongest convergent mechanistic theme across ALX-related FND is **cranial neural crest dysfunction** (apoptosis, migration, and regional identity/patterning), supported across human iPSC models and mouse/zebrafish in vivo studies. (pini2020alx1‐ pages 1-2, iyyanar2022alx1deficientmice pages 1-2, yoon2022zebrafishmodelsof pages 1-2)

2) Recent developmental-genomics work strengthens the concept of an **upstream TFAP2 → ALX transcriptional axis** in midfacial neural crest, suggesting that some “unsolved” FND-like phenotypes (negative for ALX variants) might reflect disruptions in upstream regulators or regulatory elements affecting ALX expression rather than coding variants alone. (nguyen2024tfap2paralogsregulate pages 1-3, guo2024prenataldiagnosisof pages 6-7)

3) The 2024 prenatal literature compilation underscores that **prenatal diagnosis of nonsyndromic FND remains uncommon** and that a major practical barrier is phenotypic heterogeneity with often negative standard cytogenetic and exome/genome testing—highlighting ongoing needs for improved prenatal phenotype ontologies and noncoding/regulatory variant assessment. (guo2024prenataldiagnosisof pages 1-3, guo2024prenataldiagnosisof pages 3-5)


References

1. (guo2024prenataldiagnosisof pages 1-3): Cui-Xia Guo, Tiejuan Zhang, Ying Ma, Song Yue, and Lijuan Sun. Prenatal diagnosis of a severe form of frontonasal dysplasia with severe limb anomalies, hydrocephaly, a hypoplastic corpus callosum, and a ventricular septal defect using 3d ultrasound: a case report and literature review. BMC Pregnancy and Childbirth, Jun 2024. URL: https://doi.org/10.1186/s12884-024-06619-4, doi:10.1186/s12884-024-06619-4. This article has 7 citations and is from a peer-reviewed journal.

2. (farlie2016frontonasaldysplasiatowards pages 1-2): Peter G. Farlie, Naomi L. Baker, Patrick Yap, and Tiong Y. Tan. Frontonasal dysplasia: towards an understanding of molecular and developmental aetiology. Molecular Syndromology, 7:312-321, Oct 2016. URL: https://doi.org/10.1159/000450533, doi:10.1159/000450533. This article has 62 citations and is from a peer-reviewed journal.

3. (vargel2022alxrelatedfrontonasaldysplasias pages 1-2): Ibrahim Vargel, Halil Ibrahim Canter, Arda Kucukguven, Asim Aydin, and Figen Ozgur. Alx-related frontonasal dysplasias: clinical characteristics and surgical management. The Cleft Palate-Craniofacial Journal, 59:637-643, Jun 2022. URL: https://doi.org/10.1177/10556656211019621, doi:10.1177/10556656211019621. This article has 6 citations.

4. (twigg2009frontorhinyadistinctive pages 2-3): Stephen R.F. Twigg, Sarah L. Versnel, Gudrun Nürnberg, Melissa M. Lees, Meenakshi Bhat, Peter Hammond, Raoul C.M. Hennekam, A. Jeannette M. Hoogeboom, Jane A. Hurst, David Johnson, Alexis A. Robinson, Peter J. Scambler, Dianne Gerrelli, Peter Nürnberg, Irene M.J. Mathijssen, and Andrew O.M. Wilkie. Frontorhiny, a distinctive presentation of frontonasal dysplasia caused by recessive mutations in the alx3 homeobox gene. American journal of human genetics, 84 5:698-705, May 2009. URL: https://doi.org/10.1016/j.ajhg.2009.04.009, doi:10.1016/j.ajhg.2009.04.009. This article has 154 citations and is from a highest quality peer-reviewed journal.

5. (kayserili2009alx4dysfunctiondisrupts pages 2-3): Hulya Kayserili, Elif Uz, Carien Niessen, Ibrahim Vargel, Yasemin Alanay, Gokhan Tuncbilek, Gokhan Yigit, Oya Uyguner, Sukru Candan, Hamza Okur, Serkan Kaygin, Sevim Balci, Emin Mavili, Mehmet Alikasifoglu, Ingo Haase, Bernd Wollnik, and Nurten Ayse Akarsu. Alx4 dysfunction disrupts craniofacial and epidermal development. Human molecular genetics, 18 22:4357-66, Nov 2009. URL: https://doi.org/10.1093/hmg/ddp391, doi:10.1093/hmg/ddp391. This article has 158 citations and is from a domain leading peer-reviewed journal.

6. (farlie2016frontonasaldysplasiatowards pages 4-5): Peter G. Farlie, Naomi L. Baker, Patrick Yap, and Tiong Y. Tan. Frontonasal dysplasia: towards an understanding of molecular and developmental aetiology. Molecular Syndromology, 7:312-321, Oct 2016. URL: https://doi.org/10.1159/000450533, doi:10.1159/000450533. This article has 62 citations and is from a peer-reviewed journal.

7. (goswami2024ararehomozygous pages 1-2): Barna Goswami, Asifur Rahman, Iffat Jahan, Shahina Akter, Tanjina Akhtar Banu, Eshrar Osman, Mohammad Samir Uzzaman, Ahashan Habib, Md Shamsul Alam, Abu Saleh Mohammad Abu Obaida, Md Murshed Hasan Sarkar, and Salim Khan. A rare homozygous alx4 mutation in a bangladeshi girl with frontonasal dysplasia type-2 (fnd2). Heliyon, 10:e34929, Aug 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e34929, doi:10.1016/j.heliyon.2024.e34929. This article has 2 citations.

8. (nguyen2024tfap2paralogsregulate pages 1-3): Timothy T. Nguyen, Jennyfer M. Mitchell, Michaela D. Kiel, Colin P. Kenny, Hong Li, Kenneth L. Jones, Robert A. Cornell, Trevor J. Williams, James T. Nichols, and Eric Van Otterloo. Tfap2 paralogs regulate midfacial development in part through a conserved alx genetic pathway. Development, Jan 2024. URL: https://doi.org/10.1242/dev.202095, doi:10.1242/dev.202095. This article has 15 citations and is from a domain leading peer-reviewed journal.

9. (vargel2022alxrelatedfrontonasaldysplasias pages 2-3): Ibrahim Vargel, Halil Ibrahim Canter, Arda Kucukguven, Asim Aydin, and Figen Ozgur. Alx-related frontonasal dysplasias: clinical characteristics and surgical management. The Cleft Palate-Craniofacial Journal, 59:637-643, Jun 2022. URL: https://doi.org/10.1177/10556656211019621, doi:10.1177/10556656211019621. This article has 6 citations.

10. (guo2024prenataldiagnosisof pages 3-5): Cui-Xia Guo, Tiejuan Zhang, Ying Ma, Song Yue, and Lijuan Sun. Prenatal diagnosis of a severe form of frontonasal dysplasia with severe limb anomalies, hydrocephaly, a hypoplastic corpus callosum, and a ventricular septal defect using 3d ultrasound: a case report and literature review. BMC Pregnancy and Childbirth, Jun 2024. URL: https://doi.org/10.1186/s12884-024-06619-4, doi:10.1186/s12884-024-06619-4. This article has 7 citations and is from a peer-reviewed journal.

11. (pini2020alx1‐ pages 1-2): Jonathan Pini, Janina Kueper, Yiyuan David Hu, Kenta Kawasaki, Pan Yeung, Casey Tsimbal, Baul Yoon, Nikkola Carmichael, Richard L Maas, Justin Cotney, Yevgenya Grinblat, and Eric C Liao. <i> <scp>alx</scp> 1‐ </i> related frontonasal dysplasia results from defective neural crest cell development and migration. EMBO Molecular Medicine, Sep 2020. URL: https://doi.org/10.15252/emmm.202012013, doi:10.15252/emmm.202012013. This article has 34 citations and is from a highest quality peer-reviewed journal.

12. (iyyanar2022alx1deficientmice pages 1-2): Paul P. R. Iyyanar, Zhaoming Wu, Yu Lan, Yueh-Chiang Hu, and Rulang Jiang. Alx1 deficient mice recapitulate craniofacial phenotype and reveal developmental basis of alx1-related frontonasal dysplasia. Frontiers in Cell and Developmental Biology, Jan 2022. URL: https://doi.org/10.3389/fcell.2022.777887, doi:10.3389/fcell.2022.777887. This article has 32 citations.

13. (yoon2022zebrafishmodelsof pages 1-2): Baul Yoon, Pan Yeung, Nicholas Santistevan, Lauren E. Bluhm, Kenta Kawasaki, Janina Kueper, Richard Dubielzig, Jennifer VanOudenhove, Justin Cotney, Eric C. Liao, and Yevgenya Grinblat. Zebrafish models of <i>alx</i>-linked frontonasal dysplasia reveal a role for alx1 and alx3 in the anterior segment and vasculature of the developing eye. Biology Open, May 2022. URL: https://doi.org/10.1242/bio.059189, doi:10.1242/bio.059189. This article has 6 citations and is from a peer-reviewed journal.

14. (pachajoa2023casereportcraniofrontonasal pages 1-3): Harry Pachajoa, Diana Marcela Vasquez-Forero, and Sebastian Giraldo-Ocampo. Case report: craniofrontonasal syndrome caused by a novel variant in the efnb1 gene in a colombian woman. Frontiers in Genetics, Jan 2023. URL: https://doi.org/10.3389/fgene.2022.1092301, doi:10.3389/fgene.2022.1092301. This article has 2 citations and is from a peer-reviewed journal.

15. (hussain2020anovelmissense pages 1-2): Shabir Hussain, Umm-e-Kalsoom, Irfan Ullah, Khurram Liaqat, Shoaib Nawaz, and Wasim Ahmad. A novel missense variant in the<i>alx4</i>gene underlies mild to severe frontonasal dysplasia in a consanguineous family. Genetic Testing and Molecular Biomarkers, 24:217-223, Apr 2020. URL: https://doi.org/10.1089/gtmb.2019.0203, doi:10.1089/gtmb.2019.0203. This article has 6 citations and is from a peer-reviewed journal.

16. (vargel2022alxrelatedfrontonasaldysplasias pages 5-6): Ibrahim Vargel, Halil Ibrahim Canter, Arda Kucukguven, Asim Aydin, and Figen Ozgur. Alx-related frontonasal dysplasias: clinical characteristics and surgical management. The Cleft Palate-Craniofacial Journal, 59:637-643, Jun 2022. URL: https://doi.org/10.1177/10556656211019621, doi:10.1177/10556656211019621. This article has 6 citations.

17. (ullah2018exomesequencingrevealed pages 3-4): Asmat Ullah, Muhammad Umair, Umm e-Kalsoom, Shaheen Shahzad, Sulman Basit, and Wasim Ahmad. Exome sequencing revealed a novel nonsense variant in alx3 gene underlying frontorhiny. Journal of Human Genetics, 63:97-100, Nov 2018. URL: https://doi.org/10.1038/s10038-017-0358-y, doi:10.1038/s10038-017-0358-y. This article has 11 citations and is from a peer-reviewed journal.

18. (iyyanar2022alx1deficientmice pages 9-11): Paul P. R. Iyyanar, Zhaoming Wu, Yu Lan, Yueh-Chiang Hu, and Rulang Jiang. Alx1 deficient mice recapitulate craniofacial phenotype and reveal developmental basis of alx1-related frontonasal dysplasia. Frontiers in Cell and Developmental Biology, Jan 2022. URL: https://doi.org/10.3389/fcell.2022.777887, doi:10.3389/fcell.2022.777887. This article has 32 citations.

19. (guo2024prenataldiagnosisof pages 6-7): Cui-Xia Guo, Tiejuan Zhang, Ying Ma, Song Yue, and Lijuan Sun. Prenatal diagnosis of a severe form of frontonasal dysplasia with severe limb anomalies, hydrocephaly, a hypoplastic corpus callosum, and a ventricular septal defect using 3d ultrasound: a case report and literature review. BMC Pregnancy and Childbirth, Jun 2024. URL: https://doi.org/10.1186/s12884-024-06619-4, doi:10.1186/s12884-024-06619-4. This article has 7 citations and is from a peer-reviewed journal.

20. (farlie2016frontonasaldysplasiatowards pages 6-6): Peter G. Farlie, Naomi L. Baker, Patrick Yap, and Tiong Y. Tan. Frontonasal dysplasia: towards an understanding of molecular and developmental aetiology. Molecular Syndromology, 7:312-321, Oct 2016. URL: https://doi.org/10.1159/000450533, doi:10.1159/000450533. This article has 62 citations and is from a peer-reviewed journal.

21. (bertola2013verticaltransmissionof pages 5-5): Débora R Bertola, Melina G. Rodrigues, Caio R.D.C. Quaio, Chong A. Kim, and Maria Rita Passos‐Bueno. Vertical transmission of a frontonasal phenotype caused by a novel alx4 mutation. American Journal of Medical Genetics Part A, 161:600-604, Mar 2013. URL: https://doi.org/10.1002/ajmg.a.35762, doi:10.1002/ajmg.a.35762. This article has 33 citations.

22. (kayserili2012mildnasalmalformations pages 7-8): Hülya Kayserili, U. Altunoglu, H. Ozgur, S. Basaran, and Z.O. Uyguner. Mild nasal malformations and parietal foramina caused by homozygous alx4 mutations. American Journal of Medical Genetics Part A, 158A:236-244, Jan 2012. URL: https://doi.org/10.1002/ajmg.a.34390, doi:10.1002/ajmg.a.34390. This article has 35 citations.

23. (el‐ruby2018identificationofa pages 5-5): Mona El‐Ruby, Alaa El‐Din Fayez, Sara H. El‐Dessouky, Mona S. Aglan, Inas Mazen, Nora Ismail, Hanan H. Afifi, Maha M. Eid, Mostafa I. Mostafa, Mennat I. Mehrez, Yasmin Khalil, Maha S. Zaki, Khaled R. Gaber, Mohamed S. Abdel‐Hamid, and Ghada M. H. Abdel‐Salam. Identification of a novel homozygous alx4 mutation in two unrelated patients with frontonasal dysplasia type‐2. American Journal of Medical Genetics Part A, 176:1190-1194, May 2018. URL: https://doi.org/10.1002/ajmg.a.38655, doi:10.1002/ajmg.a.38655. This article has 13 citations.

24. (vargel2022alxrelatedfrontonasaldysplasias pages 7-7): Ibrahim Vargel, Halil Ibrahim Canter, Arda Kucukguven, Asim Aydin, and Figen Ozgur. Alx-related frontonasal dysplasias: clinical characteristics and surgical management. The Cleft Palate-Craniofacial Journal, 59:637-643, Jun 2022. URL: https://doi.org/10.1177/10556656211019621, doi:10.1177/10556656211019621. This article has 6 citations.

25. (12025clinicalandmolecular pages 6-6): Umut Altunoglu 1, Birsen Karaman 1, Yasemin Alanay, Ferda Perçin, Zehra Oya Uyguner, and Hülya Kayserili 1. Clinical and molecular analyses in 8 new craniofrontonasal syndrome families: revisiting the mild end of the phenotypic spectrum in females. Turkish Archives of Pediatrics, 60:191-199, Mar 2025. URL: https://doi.org/10.5152/turkarchpediatr.2025.24336, doi:10.5152/turkarchpediatr.2025.24336. This article has 1 citations.

26. (pachajoa2023casereportcraniofrontonasal pages 3-4): Harry Pachajoa, Diana Marcela Vasquez-Forero, and Sebastian Giraldo-Ocampo. Case report: craniofrontonasal syndrome caused by a novel variant in the efnb1 gene in a colombian woman. Frontiers in Genetics, Jan 2023. URL: https://doi.org/10.3389/fgene.2022.1092301, doi:10.3389/fgene.2022.1092301. This article has 2 citations and is from a peer-reviewed journal.