---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T15:25:11.562492'
end_time: '2026-04-04T15:38:02.035786'
duration_seconds: 770.47
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Noma
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Noma
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Noma** covering all of the
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
- **Disease Name:** Noma
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Noma** covering all of the
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


# Noma (Cancrum oris) — Comprehensive Disease Characteristics Report (Infectious Disease)

## Executive summary
Noma (cancrum oris) is a rapidly progressive, necrotizing, gangrenous disease of the mouth and face that overwhelmingly affects young children living in extreme poverty and malnutrition, and is characterized by very high untreated mortality and severe lifelong facial and functional sequelae in survivors. Recent global-health developments include WHO’s official recognition of noma as a neglected tropical disease (NTD) in December 2023, which is expected to improve visibility, funding opportunities, surveillance, and research prioritization. (ainsworth2024nomafinallyrecognised pages 1-2, verma2024nomainthe pages 1-2)

## 1. Disease information
### 1.1 Overview / definition
Noma is described as a severe, rapidly progressive **orofacial gangrene** affecting the mouth and facial structures, typically in malnourished, immunocompromised children in resource-poor settings, and is widely considered polymicrobial and multifactorial rather than caused by a single pathogen. (verma2024nomainthe pages 1-2, uzochukwu2023thekeyplayers pages 1-2)

### 1.2 Key identifiers (available in retrieved sources)
- **ICD-10 (WHO)**: Evidence in retrieved literature indicates noma is listed under **A69.0** as “necrotising ulcerative stomatitis,” with synonymous labels including *Cancrum oris*, *Noma*, and *stomatitis gangraenosa*. (dhanjal2021anecroticorofacial pages 2-3, juhasz2006dasverschwindenvon pages 11-16)
- **ICD-11**: Not found in the retrieved full-text evidence in this run.
- **MeSH / Orphanet / MONDO**: Not found in the retrieved full-text evidence in this run; therefore no MeSH descriptor ID, ORPHA code, or MONDO ID can be provided with tool-verifiable citations here.

### 1.3 Synonyms and alternative names
Synonyms used across recent and historical clinical literature include: **cancrum oris**, **necrotising ulcerative stomatitis**, **gangrenous stomatitis**, and related necrotizing periodontal disease terms reflecting the clinical continuum (necrotising ulcerative gingivitis/periodontitis/stomatitis). (maguire2025asystematicreview pages 1-4, dhanjal2021anecroticorofacial pages 2-3)

### 1.4 Evidence provenance (individual vs aggregated)
- Many clinical descriptions come from case reports/series and retrospective hospital/mission records, reflecting limited population-based surveillance. (maguire2025asystematicreview pages 1-4, enbiale2024rapidassessmentof pages 1-2)
- Aggregated synthesis is available via systematic and scoping reviews; however, evidence quality is frequently low and heterogeneous. (maguire2025asystematicreview pages 1-4, maguire2025asystematicreview pages 6-9)

## 2. Etiology
### 2.1 Disease causal factors (infectious, environmental, mechanistic)
Current understanding supports noma as an opportunistic condition emerging from **oral microbiome dysbiosis** in a host rendered vulnerable by malnutrition, immunosuppression, and poverty-related exposures (poor hygiene, unsafe water/sanitation, limited healthcare access). (agost2025nomainmozambique.b pages 36-39, verma2024nomainthe pages 1-2)

### 2.2 Risk factors (with quantitative data where available)
Across a systematic review of the noma evidence landscape (366 publications), the most frequently reported risk factors were:
- **Nutritional deficit** reported in **38.8%** of studies (142/366). (maguire2025asystematicreview pages 4-6)
- **Infectious comorbidities** reported in **56.5%** of risk-factor publications (152/269); **measles** was the leading infectious risk among these (35.5%, 54/152). (maguire2025asystematicreview pages 4-6)
- **Poor oral hygiene** reported in **28%** (75/269) of risk-factor publications. (maguire2025asystematicreview pages 4-6)

Additional commonly cited risk factors in recent reviews include poverty, immunocompromise (including HIV), inadequate sanitation/unsafe water, gingival lesions, diarrhoea and fever, low birth weight, and high parity. (verma2024nomainthe pages 1-2)

### 2.3 Protective factors
Protective factors are less consistently studied, but case-control and synthesis sources report potential protective associations including **colostrum** and caregiving/maternal factors, alongside plausible upstream preventive levers (breastfeeding support, vaccination, improved nutrition, and oral hygiene). (agost2025nomainmozambique.b pages 39-42, verma2024nomainthe pages 2-3)

### 2.4 Gene–environment interactions
No specific gene–environment interactions are established in the retrieved evidence. Some literature suggests multifactorial origins could include host predisposition interacting with environmental and microbial factors, but without identified loci or effect estimates. (braimah2025estimatedincidenceand pages 2-4)

## 3. Phenotypes
### 3.1 Core clinical phenotypes (with staging)
WHO-aligned staging (including a warning stage) is commonly described as:
- **Stage 0 (warning):** simple gingivitis (gum bleeding/inflammation). (agost2025nomainmozambique. pages 28-31)
- **Stage 1:** acute necrotising gingivitis (spontaneous gum bleeding, painful papillary ulceration, fetid breath, salivation). (agost2025nomainmozambique.b pages 28-31)
- **Stage 2:** oedema (facial swelling, fever, painful cheek, mucosal extension, difficulty eating, lymphadenopathy). (agost2025nomainmozambique.b pages 28-31)
- **Stage 3:** gangrene (well-demarcated necrosis that sloughs off, leaving facial/oral defects). (agost2025nomainmozambique.b pages 28-31)
- **Stage 4:** scarring.
- **Stage 5:** sequelae (functional and structural deficits). (verma2024nomainthe pages 1-2)

Typical signs and symptoms include **severe pain**, **fever**, **oral ulceration**, **mucosal oedema**, **purulent discharge**, **extreme halitosis**, with progression to **facial tissue loss**, **trismus**, and **feeding/swallowing and speech difficulties** in later stages. (dhanjal2021anecroticorofacial pages 2-3, verma2024nomainthe pages 1-2)

### 3.2 Phenotype frequencies (examples from retrieved evidence)
- In a sequelae/survivor context, one source reports **trismus (13.6%) among sequelae cases**. (verma2024nomainthe pages 3-4)
- A Mozambique survey/case series excerpt reports high frequencies among a small assessed group (N=23) such as halitosis (100% among those assessed), oedema (90%), fever (80%), pain (64%), necrosis (67%), and eating problems (86%), illustrating the symptomatic burden in documented cases. (agost2025nomainmozambique.a pages 76-80)

### 3.3 Quality-of-life impact
Survivors frequently experience lifelong facial disfigurement and functional impairment with substantial stigma and psychosocial harm. (verma2024nomainthe pages 1-2, onu2023psychosocialaspectsof pages 1-2)

### 3.4 Suggested HPO terms (examples; not exhaustive)
Based on the clinical features in retrieved evidence:
- **HP:0000153** (Oral ulcer) (supported by clinical descriptions of oral ulceration) (dhanjal2021anecroticorofacial pages 2-3)
- **HP:0012531** (Halitosis) (fetid breath/extreme halitosis) (agost2025nomainmozambique.b pages 28-31, dhanjal2021anecroticorofacial pages 2-3)
- **HP:0000470** (Facial edema) (agost2025nomainmozambique.b pages 28-31, verma2024nomainthe pages 1-2)
- **HP:0000213** (Trismus) (dhanjal2021anecroticorofacial pages 2-3, verma2024nomainthe pages 1-2)
- **HP:0002014** (Dysphagia) / feeding difficulty (difficulty eating/deglutition) (agost2025nomainmozambique.b pages 28-31, verma2024nomainthe pages 1-2)
- **HP:0001945** (Fever) (agost2025nomainmozambique.b pages 28-31, dhanjal2021anecroticorofacial pages 2-3)

## 4. Genetic/molecular information
### 4.1 Causal genes / pathogenic variants
Noma is not established as a monogenic disorder in the retrieved evidence; no causal genes or pathogenic variants are reported. (agost2025nomainmozambique. pages 36-39, maguire2025asystematicreview pages 4-6)

### 4.2 Modifier genes, epigenetics, chromosomal abnormalities
No modifier genes, epigenetic mechanisms, or chromosomal abnormalities are identified in the retrieved evidence.

## 5. Environmental information
Noma is strongly associated with poverty-related environments: inadequate sanitation/unsafe water, limited access to healthcare, and poor oral hygiene; these factors co-occur with malnutrition and infectious comorbidities. (verma2024nomainthe pages 1-2, maguire2025asystematicreview pages 4-6)

## 6. Mechanism / pathophysiology
### 6.1 Current mechanistic model (causal chain)
A convergent model described in recent etiologic reviews is:
1) **Systemic vulnerability** (severe malnutrition, immunosuppression, intercurrent infections) + **local oral factors** (poor hygiene, gingival injury)
2) → **acute necrotising gingivitis** as immediate precursor
3) → **polymicrobial dysbiosis** and invasive infection
4) → rapid tissue destruction involving **inflammatory vascular injury**, microthrombi and **ischemic necrosis**, producing centrifugal facial tissue loss. (agost2025nomainmozambique.b pages 36-39, agost2025nomainmozambique. pages 36-39)

### 6.2 Microbiological findings (etiology research)
A 2023 systematic review of etiological studies highlights dysbiosis and identifies **spirochaetes** and **Prevotella intermedia** as putative trigger organisms and **Fusobacterium nucleatum** as promoting biofilm formation in later stages, while emphasizing major methodological limitations and the need for longitudinal high-throughput studies. (uzochukwu2023thekeyplayers pages 1-2)

A broader evidence-landscape systematic review reports extreme heterogeneity: **117 microorganisms** were observed across reported noma cases in reviewed publications, consistent with polymicrobial involvement. (maguire2025asystematicreview pages 1-4)

### 6.3 Proposed GO (biological process) and CL (cell type) terms (suggestions)
Given the described mechanisms (inflammation, necrosis, ischemia, polymicrobial infection):
- GO suggestions: **inflammatory response**, **response to bacterium**, **biofilm formation**, **blood vessel occlusion**, **ischemia**, **tissue necrosis** (supported conceptually by vascular injury/ischemic necrosis and bacterial drivers). (agost2025nomainmozambique. pages 36-39)
- CL suggestions: **neutrophil**, **macrophage**, **vascular endothelial cell**, **oral keratinocyte/epithelial cell** (conceptual mapping to described infection/inflammation and vascular injury). (agost2025nomainmozambique. pages 36-39)

### 6.4 Key knowledge gaps
Major gaps include lack of standardized case definitions in practice, sparse population-based surveillance, limited early-stage sampling, and insufficient molecular-level mechanistic evidence (e.g., defined cytokine pathways), motivating calls for longitudinal multi-omics (transcriptomics/metabolomics) and improved microbiology study design. (galli2025definingthenoma pages 2-5, agost2025nomainmozambique.b pages 36-39)

## 7. Anatomical structures affected
- Primary: oral cavity and facial tissues (gingiva/oral mucosa, cheeks, lips, nose, jaw/underlying bone). (verma2024nomainthe pages 3-4, verma2024nomainthe pages 1-2)
- Complications/sequelae: scarring, fistulas, TMJ ankylosis, severe trismus; major functional impacts on feeding and speech. (maguire2025asystematicreview pages 6-9, verma2024nomainthe pages 1-2)

**UBERON suggestions (examples):** oral mucosa, gingiva, cheek, lip, nose, maxilla/mandible.

## 8. Temporal development
Noma can progress extremely rapidly from early necrotizing gingival lesions to facial tissue destruction within a short timeframe (reported as within ~two weeks/“a fortnight” in one description). (agost2025nomainmozambique.b pages 28-31)

Disease course is often conceptualized by stages (0–5) from gingivitis to sequelae, with early stages potentially reversible with prompt care, and late stages dominated by scarring and structural defects. (agost2025nomainmozambique.b pages 28-31, verma2024nomainthe pages 1-2)

## 9. Inheritance and population
### 9.1 Epidemiology (recent synthesis)
Epidemiologic estimates remain highly uncertain and vary widely:
- Recent summaries cite **~30,000–40,000 cases annually** worldwide. (verma2024nomainthe pages 1-2)
- Older WHO-derived estimates cited in recent literature include **~140,000 new cases/year** and **~770,000 people living with sequelae**. (verma2024nomainthe pages 2-3, enbiale2024rapidassessmentof pages 2-4)
- Geographic distribution includes reports from **88 countries (1950–2019)** with concentration in the Sahel “noma belt” (e.g., Nigeria, Niger, Chad). (verma2024nomainthe pages 2-3)

Examples of reported subnational incidence variability include Nigerian states ranging **0.6–3300 per 100,000**, and eastern Ethiopia **1.64–13.4 per 100,000** (children 0–9), illustrating instability of estimates. (verma2024nomainthe pages 2-3)

### 9.2 Demographics
Noma primarily affects **children aged ~2–6 years**; some sources describe that most cases occur before age 10. (uzochukwu2023thekeyplayers pages 1-2, dhanjal2021anecroticorofacial pages 2-3)

## 10. Diagnostics
### 10.1 Clinical diagnosis
Diagnosis is primarily clinical. WHO case definitions quoted in retrieved evidence include:
- **Suspected case:** “Any child with a mouth ulcer and other warning signs such as malnutrition, poor hygiene, recent illness from measles, persistent diarrhoea, or malaria”. (agost2025nomainmozambique. pages 39-42)
- **Confirmed case:** “any person with a gangrenous disease which starts as gingival ulceration and spreads rapidly through the tissues of the mouth and face, destroying the soft and hard tissues”. (agost2025nomainmozambique. pages 39-42)

### 10.2 Differential diagnosis
Differentials include animal bites, burns, cleft lip, cutaneous leishmaniasis, necrotising fasciitis, facial cancers, syphilis, yaws, mucormycosis, noma neonatorum, and herpetic gingivostomatitis. (agost2025nomainmozambique. pages 39-42, dhanjal2021anecroticorofacial pages 2-3)

### 10.3 Supportive tests
Biopsy and microbiology cultures may be used in atypical cases to exclude malignancy and alternative infections; one case report documents biopsy ruling out malignancy with negative cultures, supporting diagnosis by exclusion plus clinical picture. (dhanjal2021anecroticorofacial pages 2-3)

## 11. Outcome / prognosis
### 11.1 Mortality and survival
Untreated mortality is commonly cited as **~80–90%**, while treated cohorts can have substantially lower mortality; one treated-case series reports **8.5% mortality** in Zinder, Niger. (enbiale2024rapidassessmentof pages 1-2, verma2024nomainthe pages 1-2)

### 11.2 Morbidity and disability
Survivors frequently experience severe facial disfigurement, scarring, fistulas, trismus, and functional impairment, contributing to social stigma and disability. (maguire2025asystematicreview pages 6-9, verma2024nomainthe pages 1-2)

## 12. Treatment
### 12.1 Acute management (typical components)
Acute treatment is commonly described as multidisciplinary, combining:
- **Antibiotics** (examples include amoxicillin + metronidazole; ampicillin + gentamicin + metronidazole; amoxicillin/clavulanate + gentamicin + metronidazole; and other regimens reported historically). (verma2024nomainthe pages 4-7, agost2025nomainmozambique. pages 73-76)
- **Local oral/wound care** including debridement and antiseptic mouth care (e.g., chlorhexidine) and wound dressings (e.g., sodium hypochlorite in a documented case pathway). (agost2025nomainmozambique. pages 73-76, maguire2025asystematicreview pages 14-16)
- **Nutrition and supportive care** (rehydration, electrolyte management, high-calorie/high-protein diets, vitamin supplementation such as vitamin A cited in reviews). (verma2024nomainthe pages 4-7, verma2024nomainthe pages 1-2)

### 12.2 Surgical and rehabilitative care
For stages with sequelae, reconstructive surgery (flaps/grafts) is frequently required; systematic evidence indicates many reconstruction approaches are reported but comparative outcomes are sparse and heterogeneous. (maguire2025asystematicreview pages 6-9, maguire2025asystematicreview pages 14-16)

### 12.3 Evidence quality
A systematic review found very heterogeneous treatment reporting (**381 different intervention descriptions** across 352 publications) and **no evidence of superiority of any antibiotic family**, with only **six interventional studies (101 patients)** identified—highlighting the need for higher-quality trials and standardized care pathways. (maguire2025asystematicreview pages 6-9)

### 12.4 Suggested MAXO terms (examples)
- Antibiotic therapy; wound debridement; antiseptic oral rinse; nutritional supplementation; reconstructive surgery; rehabilitation/physiotherapy for trismus.

## 13. Prevention
Prevention is largely risk-factor–targeted and integrated public health:
- Improve **nutrition** and address severe malnutrition; support breastfeeding/colostrum where relevant. (agost2025nomainmozambique.b pages 39-42, verma2024nomainthe pages 1-2)
- Strengthen **childhood vaccination** and management of infections such as measles (prominent infectious comorbidity). (maguire2025asystematicreview pages 4-6, verma2024nomainthe pages 1-2)
- Improve **oral hygiene** and early management of necrotizing gingival lesions. (maguire2025asystematicreview pages 4-6, maguire2025asystematicreview pages 14-16)
- Improve **water/sanitation** and access to basic healthcare and early detection/referral systems. (verma2024nomainthe pages 1-2, galli2025definingthenoma pages 6-8)

## 14. Other species / natural disease
No established zoonotic or routine cross-species transmission is described in retrieved evidence. Historical reports describe rare noma-like lesions in nonhuman animals (e.g., a dog report) but these are not established natural reservoirs. (agost2025nomainmozambique. pages 36-39)

## 15. Model organisms
No established animal model exists; historical, nonstandard induction of noma-like lesions has been described in cortisone-treated rats with dental manipulation, but this has not become a validated model. (agost2025nomainmozambique. pages 36-39)

## Recent developments and latest research (prioritizing 2023–2024)
### WHO recognition as NTD (policy milestone)
- WHO officially recognized noma as an NTD in **December 2023**. (ainsworth2024nomafinallyrecognised pages 1-2)
- A 2024 editorial emphasizes that recognition followed “decades of tireless advocacy” and should improve credibility and opportunities for resourcing, while cautioning that listing alone does not guarantee funds. (ainsworth2024nomafinallyrecognised pages 1-2, ainsworth2024nomafinallyrecognised pages 2-3)

### 2024 health-system assessment (Ethiopia)
A 2024 rapid assessment in Ethiopia extracted **69 noma case records (2015–2020)**, with **97%** coming from **two NGOs supporting surgical missions**, and highlighted major policy and primary-care oral-health gaps (“lacks a national policy on noma” and “no formal oral health program within the primary healthcare”). (enbiale2024rapidassessmentof pages 1-2)

### Psychosocial evidence (2023)
- A 2023 scoping review reports: “**one in three persons with Noma has a mental health condition**” and documents stigma, social isolation, and economic harms, with estimated productivity loss costs of **US$13.4–15 million** in one cited analysis. (onu2023psychosocialaspectsof pages 1-2)
- A 2023 Niger cross-sectional study (n=50) quantified social rejection patterns, including **86.7% rejection** associated with cheek lesion site and **60% rejection** among single adults. (issa2023influencingfactorsfor pages 1-3)

## Current applications and real-world implementations
Noma care is often delivered through combinations of local facilities, specialist referral centers, and NGO-supported surgical missions/campaigns. Examples in retrieved evidence include referral to maxillofacial surgical wards and the use of routine antibiotics plus daily wound dressing at district facilities, with later specialist modification of antibiotics and ongoing wound care at local centers. (agost2025nomainmozambique. pages 73-76, agost2025nomainmozambique.a pages 73-76)

## Expert opinions and analysis (authoritative sources)
- WHO recognition is widely framed as a catalyst for integrating noma into NTD systems, improving surveillance and standardized case definitions, and building a research agenda emphasizing early detection and psychosocial impact. (galli2025definingthenoma pages 2-5, galli2025definingthenoma pages 6-8)
- Recent reviews highlight that knowledge gaps—especially inconsistent case definition usage, sparse epidemiologic data, and weak interventional evidence—remain key bottlenecks despite growing global attention. (maguire2025asystematicreview pages 1-4, maguire2025asystematicreview pages 6-9)

## Structured summary table
The following table compiles the most actionable, knowledge-base-ready facts (identifiers, epidemiology, risks, staging, diagnostics, treatments, psychosocial outcomes) from the retrieved evidence.

| Domain | Key facts (with numbers) | Key sources |
|---|---|---|
| Identifiers / synonyms | Canonical names: **Noma**, **cancrum oris**, **gangrenous stomatitis**, **necrotising ulcerative stomatitis/stomatitis**. ICD-10 evidence in retrieved sources: **A69.0**, listed as “necrotising ulcerative stomatitis,” with synonyms including Noma and cancrum oris. Formal MeSH/Orphanet/MONDO IDs were **not available in retrieved context**. | (juhasz2006dasverschwindenvon pages 11-16, dhanjal2021anecroticorofacial pages 2-3, verma2024nomainthe pages 1-2) |
| Disease definition | Severe, rapidly progressive **orofacial gangrene/necrotising disease** of the mouth and face, usually affecting children living in extreme poverty with malnutrition and poor sanitation; polymicrobial/multifactorial rather than linked to a single pathogen. | (verma2024nomainthe pages 1-2, maguire2025asystematicreview pages 1-4, uzochukwu2023thekeyplayers pages 1-2) |
| WHO / policy development | WHO officially recognized noma as a **neglected tropical disease in December 2023**. Expected implications: more visibility, funding opportunities, surveillance, standardized case definitions, integrated NTD programming, and research momentum. | (galli2025definingthenoma pages 2-5, ainsworth2024nomafinallyrecognised pages 1-2, association2025nomaasa pages 1-2) |
| Epidemiology / distribution | Burden estimates vary widely: **30,000–40,000 cases/year** in recent summaries; older WHO-derived estimates cite **140,000 new cases/year** and **770,000 people living with sequelae**. Reported in **88 countries (1950–2019)**; concentrated in the Sahel/“noma belt” including **Nigeria, Niger, Chad**. Nigeria state estimates ranged **0.6–3300/100,000**; eastern Ethiopia **1.64–13.4/100,000**; northwest Nigeria up to **640/100,000**. | (verma2024nomainthe pages 1-2, verma2024nomainthe pages 2-3, issa2023influencingfactorsfor pages 1-3) |
| Age / demographics | Primarily affects children **2–6 years** old; some sources say **1–6 years**. One review notes **~90% of global cases develop before age 10**. Adult cases occur but are uncommon and often linked to immunosuppression or severe systemic illness. | (uzochukwu2023thekeyplayers pages 1-2, issa2023influencingfactorsfor pages 1-3, dhanjal2021anecroticorofacial pages 2-3) |
| Mortality / prognosis | Untreated mortality commonly cited as **80–90%**; historical fatality in pre-antibiotic era **63–94%**. Some treated cohorts report lower mortality, e.g. **8.5% in Zinder, Niger**; penicillin/sulphonamide-era reports reduced fatality to about **15%**. Survivors often have lifelong disfigurement and functional impairment. | (enbiale2024rapidassessmentof pages 1-2, verma2024nomainthe pages 1-2, agost2025nomainmozambique.b pages 28-31) |
| Major risk factors | Major reported risks: **malnutrition**, infectious comorbidities, poor oral hygiene, immunosuppression, poverty, inadequate sanitation/unsafe water, low socioeconomic status, gingival lesions, diarrhoea, fever, low birth weight, high parity. In a 2025 review, nutritional deficit appeared in **38.8%** of all included publications; infectious comorbidities in **56.5%** of risk-factor papers; **measles** was the leading infectious risk in **35.5%** of infectious-risk papers; poor oral hygiene in **28%** of risk-factor papers. | (verma2024nomainthe pages 1-2, maguire2025asystematicreview pages 4-6, uzochukwu2023thekeyplayers pages 1-2) |
| Protective factors | Reported protective factors are less well studied; cited factors include **colostrum**, breastfeeding, caregiver being married, mother as primary caretaker (case-control data), plus programmatic prevention targets: childhood **vaccination**, improved oral hygiene, nutrition support, clean water/sanitation, and access to basic healthcare. | (agost2025nomainmozambique.a pages 39-42, agost2025nomainmozambique.b pages 39-42, verma2024nomainthe pages 2-3) |
| Pathophysiology / etiology | Current view favors **polymicrobial dysbiosis + host vulnerability** rather than one causative organism. Reviews highlight **spirochaetes** and **Prevotella intermedia** as putative early trigger organisms, with **Fusobacterium nucleatum** implicated in later biofilm formation. No single microbial cause has been confirmed. | (uzochukwu2023thekeyplayers pages 1-2, agost2025nomainmozambique. pages 36-39) |
| WHO staging / clinical hallmarks | WHO-aligned natural history: **Stage 0** simple gingivitis; **Stage 1** acute necrotising gingivitis (gum bleeding, painful papillae ulceration, fetid breath, excessive salivation); **Stage 2** oedema (facial swelling, painful cheek, fever, difficulty eating, lymphadenopathy); **Stage 3** gangrene (well-demarcated necrosis sloughing off, leaving a hole); **Stage 4** scarring; **Stage 5** sequelae. Hallmarks include pain, halitosis, oedema, necrosis/gangrene, tissue loss, trismus, dysphagia/feeding difficulty, speech impairment. | (agost2025nomainmozambique.b pages 28-31, agost2025nomainmozambique. pages 28-31, verma2024nomainthe pages 1-2) |
| Anatomy affected | Primarily oral and facial soft/hard tissues: gingiva, oral mucosa, cheeks, lips, nose, and jaw/bone. One source notes nose involvement in about **50%** of defects and cheek involvement around **28–32%**; sequelae can include trismus and temporomandibular ankylosis. | (verma2024nomainthe pages 3-4, maguire2025asystematicreview pages 6-9) |
| Diagnostics / case definitions | Diagnosis is mainly **clinical**. WHO suspected case in retrieved text: **“Any child with a mouth ulcer and other warning signs such as malnutrition, poor hygiene, recent illness from measles, persistent diarrhoea, or malaria.”** WHO confirmed case: **“any person with a gangrenous disease which starts as gingival ulceration and spreads rapidly through the tissues of the mouth and face, destroying the soft and hard tissues.”** | (agost2025nomainmozambique. pages 39-42) |
| Differential diagnosis / workup | Differentials include animal bites, burns, cleft lip, cutaneous leishmaniasis, necrotising fasciitis, facial cancers, syphilis, yaws, mucormycosis, noma neonatorum, and acute herpetic gingivostomatitis. Biopsy and microbiology may help exclude malignancy or alternative infection, but are not definitive for classic noma. Imaging/labs may be used for systemic evaluation in case reports. | (agost2025nomainmozambique. pages 39-42, dhanjal2021anecroticorofacial pages 2-3, santos2025nomaina pages 2-4) |
| Treatment | Acute care combines **antibiotics + wound care + nutrition + hydration**. Reported regimens include **amoxicillin + metronidazole**; **ampicillin + gentamicin + metronidazole**; **amoxicillin/clavulanate + gentamicin + metronidazole**; penicillin or clindamycin in older literature. Local care includes debridement, chlorhexidine mouthwash, hydrogen peroxide/oral cleaning, sodium hypochlorite dressings, and sometimes honey dressings. Surgical care includes debridement, tooth extraction when needed, and reconstructive surgery/flaps/grafts for sequelae. | (agost2025nomainmozambique. pages 73-76, verma2024nomainthe pages 4-7, maguire2025asystematicreview pages 14-16) |
| Treatment evidence quality / implementation | Evidence is weak and heterogeneous: **352/366 studies (96%)** reported some treatment detail, but **381 different interventions** were described; antibiotics were reported in **176 studies** with **no evidence that any antibiotic family is superior**. Only **6 interventional studies (101 patients)** were identified. Specialized care settings include the **Noma Children’s Hospital, Sokoto** and NGO-supported surgical missions/campaigns in Ethiopia and Mozambique. | (maguire2025asystematicreview pages 6-9, maguire2025asystematicreview pages 4-6, braimah2025estimatedincidenceand pages 2-4, enbiale2024rapidassessmentof pages 1-2) |
| Psychosocial impact | Severe stigma and social exclusion are common. A 2023 scoping review reported **“one in three”** people with noma has a mental health condition. In a Niger cross-sectional study (**n=50**), cheek lesions had **86.7% social rejection** and single adults **60.0% rejection**; acceptance was higher in younger children and those with earlier/acute care. Estimated indirect productivity losses were **US$13.4–15 million** in one cited analysis. | (onu2023psychosocialaspectsof pages 1-2, issa2023influencingfactorsfor pages 1-3) |


*Table: This table compiles the main structured facts on noma (cancrum oris) from the retrieved evidence, including identifiers, burden estimates, risk factors, staging, diagnosis, treatment, and psychosocial burden. It is designed as a compact knowledge-base-ready reference with citation IDs for traceability.*

## Notes on evidence limitations (important for knowledge base curation)
- This tool-assisted run could not retrieve formal **MeSH descriptor IDs**, **Orphanet ORPHA**, or **MONDO** identifiers with citable evidence; ICD-11 codes were also not captured in retrieved texts.
- Epidemiology is highly uncertain and varies by method, case definitions, and under-ascertainment.
- Molecular and cytokine pathway-level mechanisms remain poorly defined in the retrieved evidence and are repeatedly flagged as gaps requiring longitudinal, early-stage sampling and multi-omics studies. (agost2025nomainmozambique.b pages 36-39, galli2025definingthenoma pages 2-5)


References

1. (ainsworth2024nomafinallyrecognised pages 1-2): Stuart Ainsworth. Noma finally recognised as a neglected tropical disease. PLOS Neglected Tropical Diseases, 18:e0012177, May 2024. URL: https://doi.org/10.1371/journal.pntd.0012177, doi:10.1371/journal.pntd.0012177. This article has 5 citations and is from a domain leading peer-reviewed journal.

2. (verma2024nomainthe pages 1-2): Amogh Verma, Amna Zaheer, Areeba Ahsan, Ayush Anand, Hashem Abu Serhan, Mahalaqua Nazli Khatib, Quazi Syed Zahiruddin, Abhay M Gaidhane, Neelima Kukreti, Sarvesh Rustagi, Prakasini Satapathy, Divya Sharma, Mithhil Arora, and Rakesh Kumar Sharma. Noma in the who's list of neglected tropical diseases: a review of its impact on undeveloped and developing tropical regions. Preventive Medicine Reports, 43:102764, Jul 2024. URL: https://doi.org/10.1016/j.pmedr.2024.102764, doi:10.1016/j.pmedr.2024.102764. This article has 11 citations and is from a peer-reviewed journal.

3. (uzochukwu2023thekeyplayers pages 1-2): Ifeanyi Uzochukwu, David Moyes, Gordon Proctor, and Mark Ide. The key players of dysbiosis in noma disease; a systematic review of etiological studies. Frontiers in Oral Health, Mar 2023. URL: https://doi.org/10.3389/froh.2023.1095858, doi:10.3389/froh.2023.1095858. This article has 15 citations and is from a peer-reviewed journal.

4. (dhanjal2021anecroticorofacial pages 2-3): Gagandip Singh Dhanjal, Kelvin David Mizen, and Jerome Nigel Philip. A necrotic orofacial lesion presenting in an immunocompromised patient in the uk: case review with features of noma. Journal of the Irish Dental Association, Oct 2021. URL: https://doi.org/10.58541/001c.71441, doi:10.58541/001c.71441. This article has 0 citations.

5. (juhasz2006dasverschwindenvon pages 11-16): J Juhász. Das verschwinden von noma in europa in der ersten hälfte des 20. jahrhunderts. Unknown journal, 2006.

6. (maguire2025asystematicreview pages 1-4): Brittany J. Maguire, Rujan Shrestha, Prabin Dahal, Roland Ngu, Lionel Nizigama, Sumayyah Rashan, Poojan Shrestha, Elinor Harriss, Paul N. Newton, Yuka Makino, Benoit Varenne, and Philippe J. Guérin. A systematic review of the noma evidence landscape: current knowledge and gaps. MedRxiv, Feb 2025. URL: https://doi.org/10.1101/2025.02.07.24315593, doi:10.1101/2025.02.07.24315593. This article has 3 citations.

7. (enbiale2024rapidassessmentof pages 1-2): Wendemagegn Enbiale. Rapid assessment of noma: reporting on forgotten and neglected disease in ethiopia. PLOS Neglected Tropical Diseases, 18:e0012696, Dec 2024. URL: https://doi.org/10.1371/journal.pntd.0012696, doi:10.1371/journal.pntd.0012696. This article has 0 citations and is from a domain leading peer-reviewed journal.

8. (maguire2025asystematicreview pages 6-9): Brittany J. Maguire, Rujan Shrestha, Prabin Dahal, Roland Ngu, Lionel Nizigama, Sumayyah Rashan, Poojan Shrestha, Elinor Harriss, Paul N. Newton, Yuka Makino, Benoit Varenne, and Philippe J. Guérin. A systematic review of the noma evidence landscape: current knowledge and gaps. MedRxiv, Feb 2025. URL: https://doi.org/10.1101/2025.02.07.24315593, doi:10.1101/2025.02.07.24315593. This article has 3 citations.

9. (agost2025nomainmozambique.b pages 36-39): M Ribes Agost. Noma in mozambique. epidemiological efforts to uncover a neglected disease. Unknown journal, 2025.

10. (maguire2025asystematicreview pages 4-6): Brittany J. Maguire, Rujan Shrestha, Prabin Dahal, Roland Ngu, Lionel Nizigama, Sumayyah Rashan, Poojan Shrestha, Elinor Harriss, Paul N. Newton, Yuka Makino, Benoit Varenne, and Philippe J. Guérin. A systematic review of the noma evidence landscape: current knowledge and gaps. MedRxiv, Feb 2025. URL: https://doi.org/10.1101/2025.02.07.24315593, doi:10.1101/2025.02.07.24315593. This article has 3 citations.

11. (agost2025nomainmozambique.b pages 39-42): M Ribes Agost. Noma in mozambique. epidemiological efforts to uncover a neglected disease. Unknown journal, 2025.

12. (verma2024nomainthe pages 2-3): Amogh Verma, Amna Zaheer, Areeba Ahsan, Ayush Anand, Hashem Abu Serhan, Mahalaqua Nazli Khatib, Quazi Syed Zahiruddin, Abhay M Gaidhane, Neelima Kukreti, Sarvesh Rustagi, Prakasini Satapathy, Divya Sharma, Mithhil Arora, and Rakesh Kumar Sharma. Noma in the who's list of neglected tropical diseases: a review of its impact on undeveloped and developing tropical regions. Preventive Medicine Reports, 43:102764, Jul 2024. URL: https://doi.org/10.1016/j.pmedr.2024.102764, doi:10.1016/j.pmedr.2024.102764. This article has 11 citations and is from a peer-reviewed journal.

13. (braimah2025estimatedincidenceand pages 2-4): Ramat Oyebunmi Braimah, John Adeoye, Abdurrazaq Olanrewaju Taiwo, Seidu Bello, Mujtaba Bala, Azeez Butali, Bruno Oludare Ile-Ogedengbe, and Abubakar Abdullahi Bello. Estimated incidence and clinical presentation of noma in northern nigeria (1999–2024). PLOS Neglected Tropical Diseases, 19:e0012818, May 2025. URL: https://doi.org/10.1371/journal.pntd.0012818, doi:10.1371/journal.pntd.0012818. This article has 5 citations and is from a domain leading peer-reviewed journal.

14. (agost2025nomainmozambique. pages 28-31): M Ribes Agost. Noma in mozambique. epidemiological efforts to uncover a neglected disease. Unknown journal, 2025.

15. (agost2025nomainmozambique.b pages 28-31): M Ribes Agost. Noma in mozambique. epidemiological efforts to uncover a neglected disease. Unknown journal, 2025.

16. (verma2024nomainthe pages 3-4): Amogh Verma, Amna Zaheer, Areeba Ahsan, Ayush Anand, Hashem Abu Serhan, Mahalaqua Nazli Khatib, Quazi Syed Zahiruddin, Abhay M Gaidhane, Neelima Kukreti, Sarvesh Rustagi, Prakasini Satapathy, Divya Sharma, Mithhil Arora, and Rakesh Kumar Sharma. Noma in the who's list of neglected tropical diseases: a review of its impact on undeveloped and developing tropical regions. Preventive Medicine Reports, 43:102764, Jul 2024. URL: https://doi.org/10.1016/j.pmedr.2024.102764, doi:10.1016/j.pmedr.2024.102764. This article has 11 citations and is from a peer-reviewed journal.

17. (agost2025nomainmozambique.a pages 76-80): M Ribes Agost. Noma in mozambique. epidemiological efforts to uncover a neglected disease. Unknown journal, 2025.

18. (onu2023psychosocialaspectsof pages 1-2): Justus U. Onu, Deborah O. Aluh, and Charles N. Ononiwu. Psychosocial aspects of noma (cancrum oris) in sub-saharan africa: a scoping review. Tropical Doctor, 53:470-474, May 2023. URL: https://doi.org/10.1177/00494755231175529, doi:10.1177/00494755231175529. This article has 8 citations and is from a peer-reviewed journal.

19. (agost2025nomainmozambique. pages 36-39): M Ribes Agost. Noma in mozambique. epidemiological efforts to uncover a neglected disease. Unknown journal, 2025.

20. (galli2025definingthenoma pages 2-5): Anaïs Galli, Marianne Comparet, Daniel Argaw Dagne, Denise Baratti-Mayer, Thi H. Cao, Philippe J. Guérin, Maria Guevara, Manuel W. Hetzel, Claire Jeantet, Emmanuel Kabengele Mpinga, Valter Muendane, Mulikat Okanlawon, Erika Placella, Marta Ribes, Mark Sherlock, Jürg Utzinger, and Peter Steinmann. Defining the noma research agenda. PLOS Neglected Tropical Diseases, 19:e0012940, Apr 2025. URL: https://doi.org/10.1371/journal.pntd.0012940, doi:10.1371/journal.pntd.0012940. This article has 3 citations and is from a domain leading peer-reviewed journal.

21. (enbiale2024rapidassessmentof pages 2-4): Wendemagegn Enbiale. Rapid assessment of noma: reporting on forgotten and neglected disease in ethiopia. PLOS Neglected Tropical Diseases, 18:e0012696, Dec 2024. URL: https://doi.org/10.1371/journal.pntd.0012696, doi:10.1371/journal.pntd.0012696. This article has 0 citations and is from a domain leading peer-reviewed journal.

22. (agost2025nomainmozambique. pages 39-42): M Ribes Agost. Noma in mozambique. epidemiological efforts to uncover a neglected disease. Unknown journal, 2025.

23. (verma2024nomainthe pages 4-7): Amogh Verma, Amna Zaheer, Areeba Ahsan, Ayush Anand, Hashem Abu Serhan, Mahalaqua Nazli Khatib, Quazi Syed Zahiruddin, Abhay M Gaidhane, Neelima Kukreti, Sarvesh Rustagi, Prakasini Satapathy, Divya Sharma, Mithhil Arora, and Rakesh Kumar Sharma. Noma in the who's list of neglected tropical diseases: a review of its impact on undeveloped and developing tropical regions. Preventive Medicine Reports, 43:102764, Jul 2024. URL: https://doi.org/10.1016/j.pmedr.2024.102764, doi:10.1016/j.pmedr.2024.102764. This article has 11 citations and is from a peer-reviewed journal.

24. (agost2025nomainmozambique. pages 73-76): M Ribes Agost. Noma in mozambique. epidemiological efforts to uncover a neglected disease. Unknown journal, 2025.

25. (maguire2025asystematicreview pages 14-16): Brittany J. Maguire, Rujan Shrestha, Prabin Dahal, Roland Ngu, Lionel Nizigama, Sumayyah Rashan, Poojan Shrestha, Elinor Harriss, Paul N. Newton, Yuka Makino, Benoit Varenne, and Philippe J. Guérin. A systematic review of the noma evidence landscape: current knowledge and gaps. MedRxiv, Feb 2025. URL: https://doi.org/10.1101/2025.02.07.24315593, doi:10.1101/2025.02.07.24315593. This article has 3 citations.

26. (galli2025definingthenoma pages 6-8): Anaïs Galli, Marianne Comparet, Daniel Argaw Dagne, Denise Baratti-Mayer, Thi H. Cao, Philippe J. Guérin, Maria Guevara, Manuel W. Hetzel, Claire Jeantet, Emmanuel Kabengele Mpinga, Valter Muendane, Mulikat Okanlawon, Erika Placella, Marta Ribes, Mark Sherlock, Jürg Utzinger, and Peter Steinmann. Defining the noma research agenda. PLOS Neglected Tropical Diseases, 19:e0012940, Apr 2025. URL: https://doi.org/10.1371/journal.pntd.0012940, doi:10.1371/journal.pntd.0012940. This article has 3 citations and is from a domain leading peer-reviewed journal.

27. (ainsworth2024nomafinallyrecognised pages 2-3): Stuart Ainsworth. Noma finally recognised as a neglected tropical disease. PLOS Neglected Tropical Diseases, 18:e0012177, May 2024. URL: https://doi.org/10.1371/journal.pntd.0012177, doi:10.1371/journal.pntd.0012177. This article has 5 citations and is from a domain leading peer-reviewed journal.

28. (issa2023influencingfactorsfor pages 1-3): Abdou Hassane Issa, Kadre Alio Kadre Ousmane, Elhadj Ousmane Hamady Issa, Jiahao Shen, Maiga Djibo Douma, Alkassoum Salifou Ibrahim, Moeng Eva, and Ying Guan. Influencing factors for social acceptance of noma (cancrum oris) patients in niger: a hospital-based cross-sectional study. Health, 15:326-348, Jan 2023. URL: https://doi.org/10.4236/health.2023.154023, doi:10.4236/health.2023.154023. This article has 6 citations and is from a peer-reviewed journal.

29. (agost2025nomainmozambique.a pages 73-76): M Ribes Agost. Noma in mozambique. epidemiological efforts to uncover a neglected disease. Unknown journal, 2025.

30. (association2025nomaasa pages 1-2): Elysium Noma Survivors Association, Dan Izzett, Barbara Izzett, Alice Trotter, João Nunes, Ioana Cismas, Claire Jeantet, Emmanuel Kabengele, Habib Benzian, Heron Gebretsadik, Laura Merrill, Marta Ribes, Marianne Comparet, Mark Sherlock, and Himani Bhakuni. Noma as a neglected tropical disease: an opportunity to reconsider neglect in global health. BMJ Global Health, 10:e019152, Aug 2025. URL: https://doi.org/10.1136/bmjgh-2025-019152, doi:10.1136/bmjgh-2025-019152. This article has 0 citations and is from a peer-reviewed journal.

31. (agost2025nomainmozambique.a pages 39-42): M Ribes Agost. Noma in mozambique. epidemiological efforts to uncover a neglected disease. Unknown journal, 2025.

32. (santos2025nomaina pages 2-4): Vinícius Cezak Santos, Rafael Ferreira, Gleyson Kleber do Amaral Silva, Gustavo Silva Pelissaro, Elerson Gaetti-Jardim Júnior, and Ellen Cristina Gaetti-Jardim. Noma in a pacient whitout sistemic involvement. Research, Society and Development, 14:e4014148022, Jan 2025. URL: https://doi.org/10.33448/rsd-v14i1.48022, doi:10.33448/rsd-v14i1.48022. This article has 0 citations.
