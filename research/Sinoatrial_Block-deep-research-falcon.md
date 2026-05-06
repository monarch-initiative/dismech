---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T07:58:41.314252'
end_time: '2026-05-06T08:11:56.897686'
duration_seconds: 795.58
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Sinoatrial Block
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 45
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sinoatrial Block
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Sinoatrial Block** covering all of the
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
- **Disease Name:** Sinoatrial Block
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Sinoatrial Block** covering all of the
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


# Sinoatrial Block (Sinoatrial Exit Block): Comprehensive Disease Characteristics Report

## 1. Disease Information

### 1.1 Overview and current definition
**Sinoatrial (SA) block** (often used interchangeably with **sinoatrial exit block**) is a bradyarrhythmia in which impulses generated in the sinoatrial node (SAN) fail to conduct (“exit”) from the node to surrounding atrial tissue, producing pauses on the surface electrocardiogram (ECG) that reflect missed atrial depolarizations (i.e., missing P waves) rather than failure of impulse generation. SA exit block is commonly discussed under the broader clinical syndrome of **sinus node dysfunction (SND)**, which includes sinus bradycardia, sinus pauses/arrest, chronotropic incompetence, and bradycardia–tachycardia syndrome. (stevenson2021sinusnodedysfunction pages 1-2, romandini2015sinoatrialexitblock pages 3-5)

**Classification (ECG-based, analogous to AV block):**
- **First-degree SA exit block:** conduction delay from SAN to atria; generally not diagnosable on surface ECG. (romandini2015sinoatrialexitblock pages 3-5)
- **Second-degree SA exit block:** intermittent failure of conduction.
  - **Type I (SA Wenckebach):** progressively changing conduction leading to a dropped atrial beat; in one clinical summary, this is described as a pause after *progressive P–P shortening*. (stevenson2021sinusnodedysfunction pages 2-3, romandini2015sinoatrialexitblock pages 3-5)
  - **Type II (SA Mobitz II):** sudden failure without preceding progressive change; described as a *distinct pause after constant P–P intervals*. (stevenson2021sinusnodedysfunction pages 2-3, romandini2015sinoatrialexitblock pages 3-5)
- **Third-degree SA exit block:** complete failure of conduction; pauses may be followed by escape rhythms. (stevenson2021sinusnodedysfunction pages 2-3, romandini2015sinoatrialexitblock pages 3-5)

**Differential concept:** SA exit block (failed conduction) is distinguished from **sinus arrest** (failed impulse formation) using timing relationships between pauses and the underlying P–P interval pattern. (romandini2015sinoatrialexitblock pages 3-5)

### 1.2 Synonyms and alternative names
- Sinoatrial block
- Sinoatrial exit block
- SAN block (sinus node block)
- Often embedded within “sinus node dysfunction” or “sick sinus syndrome” frameworks (stevenson2021sinusnodedysfunction pages 1-2, romandini2015sinoatrialexitblock pages 3-5)

### 1.3 Key identifiers (ICD/MeSH/MONDO)
Within the retrieved evidence set, explicit **ICD-10**, **MeSH**, or **MONDO** identifiers for “sinoatrial block/exit block” were **not found**, so these codes cannot be asserted from primary sources here.

### 1.4 Evidence source type
The information summarized below draws primarily from:
- Aggregated disease-level resources (peer-reviewed narrative reviews, textbook-style clinical chapters, systematic reviews, and cohort/registry analyses) (stevenson2021sinusnodedysfunction pages 1-2, mesirca2021pharmacologicapproachto pages 1-2, patsiou2023epicardialversusendocardial pages 1-2, tan2024feasibilitysafetyand pages 1-2)
- Human observational data (claims databases; familial cohorts), and preclinical animal/in vitro/in silico models for mechanism/genetics (okumus2024threeyearincidenceof pages 1-2, ishikawa2017sicksinussyndrome pages 1-6, wallace2021geneticcomplexityof pages 8-9)


## 2. Etiology

### 2.1 Disease causal factors
SA block/exit block most often arises in the setting of **sinus node dysfunction**, which is conceptualized as intrinsic (structural/degenerative or disease-related) versus extrinsic (potentially reversible) causes. (stevenson2021sinusnodedysfunction pages 1-2)

**Intrinsic causes (examples):**
- **Degenerative/idiopathic fibrosis** of SAN tissue (common age-related substrate) (stevenson2021sinusnodedysfunction pages 1-2, mesirca2021pharmacologicapproachto pages 1-2)
- **Ischemic injury/remodeling**, including post–myocardial infarction remodeling and heart failure-related remodeling (stevenson2021sinusnodedysfunction pages 1-2)
- **Infiltrative disease** (e.g., sarcoidosis, amyloidosis, hemochromatosis) (stevenson2021sinusnodedysfunction pages 2-3)
- **Chagas cardiomyopathy** and **congenital heart disease** contexts are described as contributors in clinical summaries of SND (stevenson2021sinusnodedysfunction pages 2-3)

**Extrinsic causes (examples):**
- **Medications**: beta blockers, non-dihydropyridine calcium channel blockers, digoxin, lithium, antiarrhythmics (stevenson2021sinusnodedysfunction pages 2-3)
- **Metabolic abnormalities** and **endocrine disorders** (stevenson2021sinusnodedysfunction pages 2-3)
- **Autonomic imbalance / increased vagal tone**, including after acute myocardial infarction (stevenson2021sinusnodedysfunction pages 1-2)
- **Toxins** cited in one clinical chapter include nicotine and marijuana (stevenson2021sinusnodedysfunction pages 2-3)

### 2.2 Risk factors
**Age** is a major risk factor, with SND/SA block burden rising in older adults and linked to degenerative remodeling. (stevenson2021sinusnodedysfunction pages 1-2, mesirca2021pharmacologicapproachto pages 1-2)

Comorbidities often co-occurring with SND include hypertension, chronic kidney disease, diabetes, and coronary disease (described as risk factors in one clinical chapter). (stevenson2021sinusnodedysfunction pages 1-2)

**Genetic susceptibility** is increasingly recognized (see Section 4), including ion-channel and scaffolding/trafficking genes (e.g., HCN4, SCN5A, CACNA1D, ANK2/ANKB). (mesirca2021pharmacologicapproachto pages 5-6, wallace2021geneticcomplexityof pages 8-9)

### 2.3 Protective factors
The retrieved corpus did not provide validated protective genetic variants or protective lifestyle exposures specific to SA block.

### 2.4 Gene–environment interactions
Direct gene–environment interaction studies specific to SA exit block were not captured in the retrieved corpus. However, multiple sources emphasize that acquired substrates (aging, fibrosis, heart failure, ischemia) can unmask or worsen underlying genetic predispositions affecting SAN automaticity and conduction. (stevenson2021sinusnodedysfunction pages 1-2, wallace2021geneticcomplexityof pages 8-9)


## 3. Phenotypes

### 3.1 Core clinical phenotypes (with suggested HPO terms)
SA block/exit block manifests as intermittent dropped atrial depolarizations with resultant bradycardia or pauses, often within the broader SND phenotype.

**Common SND/SA-block-associated phenotypes** (human clinical):
- **Sinus bradycardia** (threshold used clinically in one chapter: **<50 bpm**)  
  - HPO: **Bradycardia (HP:0001662)**; **Sinus bradycardia (HP:0001688)** (suggested) (stevenson2021sinusnodedysfunction pages 1-2)
- **Sinus pause/arrest** (e.g., **pause >3 seconds** used as a diagnostic threshold)  
  - HPO: **Sinus arrest (HP:0001706)**; **Syncope (HP:0001279)** (suggested) (stevenson2021sinusnodedysfunction pages 1-2)
- **Sinoatrial (exit) block** (ECG-defined dropped P waves/pauses)  
  - HPO: **Sinoatrial block (HP:0031643)** (suggested)
- **Chronotropic incompetence** (described as inability to reach **≥80%** of predicted max HR [220–age])  
  - HPO: **Exercise intolerance (HP:0003546)**; **Chronotropic incompetence** (suggested) (stevenson2021sinusnodedysfunction pages 1-2)
- **Bradycardia–tachycardia syndrome** (alternation of atrial tachyarrhythmias and sinus pauses)  
  - HPO: **Atrial fibrillation (HP:0005110)**; **Palpitations (HP:0001962)** (suggested) (john2016sinusnodeand pages 1-2)

### 3.2 Phenotype frequencies and severity
- A clinical chapter reports **syncope occurs in ~50%** of patients with SND and **bradycardia–tachycardia syndrome in ~50%** at diagnosis. (stevenson2021sinusnodedysfunction pages 2-3, stevenson2021sinusnodedysfunction pages 1-2)
- A Circulation review reports atrial arrhythmias (including AF) coexist in **40%–70%** of patients at SND diagnosis. (john2016sinusnodeand pages 1-2)
- In familial SSS enriched for channel variants, HCN4 mutation carriers had **atrial fibrillation in 43.8%** and **left ventricular noncompaction in 50%**. (ishikawa2017sicksinussyndrome pages 1-6)

### 3.3 Age of onset and progression
- **Typical clinical onset** is frequently in older adults for degenerative SND, consistent with age-related remodeling. (stevenson2021sinusnodedysfunction pages 1-2, mesirca2021pharmacologicapproachto pages 1-2)
- **Early-onset familial forms** occur with pathogenic variants (e.g., HCN4, SCN5A), with different age-at-diagnosis and pacemaker timing between genes in one familial cohort analysis. (ishikawa2017sicksinussyndrome pages 1-6)

### 3.4 Quality of life
Specific validated quality-of-life instrument outcomes (e.g., EQ-5D/SF-36) for SA block were not present in the retrieved corpus; however, symptoms of cerebral hypoperfusion, syncope/presyncope, and exercise intolerance are repeatedly emphasized as clinically impactful manifestations of SND. (stevenson2021sinusnodedysfunction pages 1-2)


## 4. Genetic/Molecular Information

### 4.1 Causal and associated genes (human)
Across multiple reviews and cohort studies, **ion channel genes** and **channel-targeting/scaffolding genes** repeatedly arise.

**Key genes implicated in inherited SND/SA block phenotypes** include:
- **HCN4** (If/pacemaker current) (mesirca2021pharmacologicapproachto pages 5-6, ishikawa2017sicksinussyndrome pages 1-6)
- **SCN5A** (cardiac sodium channel Nav1.5; conduction/excitability) (mesirca2021pharmacologicapproachto pages 5-6, ishikawa2017sicksinussyndrome pages 1-6)
- **CACNA1D (Cav1.3)** and other Ca-channel genes (mesirca2021pharmacologicapproachto pages 5-6, wallace2021geneticcomplexityof pages 8-9)
- **ANK2/ANKB (ankyrin-B pathway)** (mesirca2021pharmacologicapproachto pages 5-6, maarel2023geneticsofsinoatrial pages 13-14)
- Other genes highlighted in reviews include **RYR2, CASQ2, TRPM4, GNB5/GNB2**, and myosin genes. (mesirca2021pharmacologicapproachto pages 5-6, wallace2021geneticcomplexityof pages 8-9, maarel2023geneticsofsinoatrial pages 14-15)

A 2023 review emphasizes recurrent candidate loci in human studies including **MYH6, HCN4, SCN5A, CACNA1C, CACNA1D**. (milanesi2015thegeneticbasis pages 1-2)

### 4.2 Pathogenic variants (examples)
Variant-level examples extracted from reviews and human cohorts:
- **SCN5A**: variants summarized in one genetics review include **E1784K** (with **39% exhibiting SND** in a described cohort), plus other loss-of-function/truncation examples (e.g., L1821fs/10) associated with marked reductions in sodium current in heterologous systems. (wallace2021geneticcomplexityof pages 6-7)
- **HCN4**: truncation **573X** linked to sinus bradycardia/chronotropic incompetence in review summaries; multiple missense variants (e.g., G480R, G482R) are discussed in relation to familial sinus bradycardia and structural phenotypes. (wallace2021geneticcomplexityof pages 6-7)
- **CACNA1D**: Cav1.3 variants **G403_V404insG** and **A376V** linked to “sinoatrial node dysfunction and deafness (SANDD)” in a genetics review. (wallace2021geneticcomplexityof pages 8-9)

### 4.3 Functional consequences (mechanistic themes)
- **HCN4** variants reduce pacemaker current and impair diastolic depolarization/automaticity. (ishikawa2017sicksinussyndrome pages 1-6)
- **SCN5A** variants can cause conduction delay or exit block; a pharmacology review notes that Nav1.5 inhibition can “induce exit block” in intact human SAN preparations. (mesirca2021pharmacologicapproachto pages 5-6)
- **Ankyrin-B pathway** defects alter ion channel/transporter targeting (including Cav1.3 and NCX1), disrupting diastolic depolarization. (mesirca2021pharmacologicapproachto pages 5-6)

### 4.4 Modifier genes and penetrance
Evidence for incomplete penetrance and variable expressivity is repeatedly emphasized in genetic reviews of nodal dysfunction, but quantitative penetrance estimates beyond specific examples (e.g., SCN5A E1784K fraction with SND; MYH-α R721W carrier proportions described in review) were limited in the retrieved excerpts. (wallace2021geneticcomplexityof pages 6-7, wallace2021geneticcomplexityof pages 8-9)

### 4.5 Epigenetics and chromosomal abnormalities
No disease-specific epigenetic signatures or chromosomal abnormalities for SA block were identified in the retrieved corpus.


## 5. Environmental Information

The retrieved corpus emphasized **drug exposures** and **toxins** as reversible contributors (beta blockers, non-DHP calcium channel blockers, digoxin, lithium, antiarrhythmics; nicotine and marijuana as toxins), and **autonomic/vagal** influences (including post-MI) but did not provide detailed pollutant or occupational exposure evidence specific to SA block. (stevenson2021sinusnodedysfunction pages 2-3, stevenson2021sinusnodedysfunction pages 1-2)


## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (conceptual)
A unifying mechanistic framework for SA block as part of SND is:
1) **Upstream triggers/substrates**: aging-related remodeling/fibrosis; ischemia or heart failure remodeling; infiltrative disease; drug/toxin exposure; autonomic imbalance; or inherited channel/trafficking variants. (stevenson2021sinusnodedysfunction pages 1-2, mesirca2021pharmacologicapproachto pages 5-6)
2) **SAN cellular dysfunction**: reduced automaticity (“membrane clock” and “Ca2+ clock” disturbances), altered coupling to atrial tissue, and slowed SAN conduction. (mesirca2021pharmacologicapproachto pages 5-6)
3) **Tissue-level conduction failure**: failure of impulses to exit the SAN into atrial myocardium produces **SA exit block** and pauses. (romandini2015sinoatrialexitblock pages 3-5, mesirca2021pharmacologicapproachto pages 5-6)
4) **Clinical manifestations**: bradycardia, pauses, syncope/presyncope, exercise intolerance, and association with atrial tachyarrhythmias (brady-tachy syndrome). (stevenson2021sinusnodedysfunction pages 1-2, john2016sinusnodeand pages 1-2)

### 6.2 Recent (2024) mechanistic development: inflammation–electrical remodeling link
A notable 2024 mechanistic advance used deep sinus-node proteomics/phosphoproteomics in a murine heart failure model with SND. The study linked **electrical remodeling to inflammation**, highlighting downregulation of **Hcn4**, showing that **experimentally induced inflammation downregulated Hcn4 and slowed pacemaking**, and identifying **galectin-3 signaling** as a candidate mediator: **in vivo suppression of galectin-3 prevented SND** in the model. (kahnert2024proteomicscoupleselectrical pages 1-2)

### 6.3 Suggested ontology terms (examples)
- **GO Biological Process** (suggested): cardiac muscle cell action potential, regulation of heart rate, conduction, response to catecholamine, inflammatory response.
- **Cell Ontology (CL)** (suggested): cardiac pacemaker cell; atrial cardiomyocyte; fibroblast; macrophage.


## 7. Anatomical Structures Affected

### 7.1 Primary structures
- **Sinoatrial node (SAN)** within the right atrium is the primary structure implicated; SA exit block reflects impaired conduction from SAN to atrial myocardium. (romandini2015sinoatrialexitblock pages 3-5)

### 7.2 Tissue/cellular context
- SA node is specialized pacemaker tissue embedded in atrial myocardium and affected by fibrosis/remodeling in intrinsic SND. (john2016sinusnodeand pages 1-2, stevenson2021sinusnodedysfunction pages 1-2)

### 7.3 Suggested anatomy ontology terms
- **UBERON** (suggested): sinoatrial node; right atrium; cardiac conducting system.


## 8. Temporal Development

- **Onset**: often insidious/chronic in degenerative SND of older adults; may be earlier in familial channelopathy-related SND/SA block. (stevenson2021sinusnodedysfunction pages 1-2, ishikawa2017sicksinussyndrome pages 1-6)
- **Course**: can be intermittent/episodic (e.g., paroxysmal SA block) or progressive in fibrotic/degenerative substrates, with increasing need for pacing as symptoms and pauses worsen. (stevenson2021sinusnodedysfunction pages 1-2)


## 9. Inheritance and Population

### 9.1 Epidemiology
- Incidence of SND is reported as **~0.8 per 1,000 person-years**, with highest prevalence in ages **70–89**, and is projected to increase substantially over coming decades. (stevenson2021sinusnodedysfunction pages 1-2)
- Another review-level estimate notes SND is common in those **>65 years (1/600)**. (mesirca2021pharmacologicapproachto pages 1-2)

### 9.2 Inheritance
Inherited SND is described as rare relative to acquired degenerative SND, but multiple monogenic causes exist (dominant and recessive syndromic/non-syndromic forms, depending on gene). (mesirca2021pharmacologicapproachto pages 5-6, maarel2023geneticsofsinoatrial pages 14-15)


## 10. Diagnostics

### 10.1 Clinical criteria and ECG thresholds
Diagnosis of clinically significant SA block/SND requires **symptom–rhythm correlation** and exclusion of reversible extrinsic contributors. (stevenson2021sinusnodedysfunction pages 1-2)

Representative thresholds used in clinical summaries:
- **Sinus bradycardia**: HR **<50 bpm** (stevenson2021sinusnodedysfunction pages 1-2)
- **Sinus pause/arrest**: pause **>3 seconds** (stevenson2021sinusnodedysfunction pages 1-2)
- **Chronotropic incompetence**: failure to reach **≥80%** of predicted maximal HR (220–age) (stevenson2021sinusnodedysfunction pages 1-2)

### 10.2 SA block pattern recognition
A clinical chapter provides surface-ECG descriptors for SA exit block types:
- Second-degree type I: pause after progressive P–P shortening
- Second-degree type II: distinct pause after constant P–P
- Third-degree: multiple impulses blocked with pause followed by atrial beat (stevenson2021sinusnodedysfunction pages 2-3)

### 10.3 Electrophysiology study (EPS) parameters
A mechanistic review describes EPS-derived indices:
- **Corrected sinus node recovery time (cSNRT)** and **sinoatrial conduction time (SACT)**; when both significantly prolonged, combined test performance reported as **sensitivity 64%** and **specificity 88%**. (choudhury2015biologyofthe pages 3-4)

### 10.4 Differential diagnosis
Differential considerations include sinus arrest, AV block with dropped beats, and artifact or atrial arrhythmias with pauses. Distinction between sinus arrest and SA exit block is highlighted by timing relationships to baseline P–P intervals in electrophysiology descriptions. (romandini2015sinoatrialexitblock pages 3-5)


## 11. Outcome / Prognosis

### 11.1 Morbidity and complications
- Symptomatic burden is substantial: ~50% may present with cerebral hypoperfusion-type symptoms (including syncope/presyncope), and ~50% have bradycardia–tachycardia syndrome. (stevenson2021sinusnodedysfunction pages 1-2)
- Atrial arrhythmias are common in SND: **40%–70% at diagnosis** in a Circulation review, and are linked to stroke and mortality risk via brady-tachy syndrome and atrial myopathy concepts (as discussed in clinical reviews). (john2016sinusnodeand pages 1-2, stevenson2021sinusnodedysfunction pages 1-2)

### 11.2 Gene-specific prognostic patterns
In one familial SSS study:
- HCN4 carriers had later pacemaker implantation compared with SCN5A carriers (mean **43.5 ± 22.1 years** vs **17.8 ± 16.5 years**) and had frequent AF and LV noncompaction. (ishikawa2017sicksinussyndrome pages 1-6)


## 12. Treatment

### 12.1 Standard of care: pacing
For **symptomatic, confirmed** sinus node dysfunction (including symptomatic SA exit block), first-line therapy is **permanent pacemaker implantation**, typically with **atrial-based pacing** and limited ventricular pacing when needed. (stevenson2021sinusnodedysfunction pages 1-2)

A pharmacology review notes that chronic symptomatic SND is primarily treated with a permanent electronic pacemaker, and that symptomatic SND and AV block account for ~half of pacemaker implantations in the U.S. (mesirca2021pharmacologicapproachto pages 1-2)

**Suggested MAXO terms (examples):**
- **Permanent cardiac pacemaker implantation** (MAXO suggested)
- **Temporary cardiac pacing** (MAXO suggested) for unstable bradycardia (stevenson2021sinusnodedysfunction pages 2-3)

### 12.2 Recent developments and real-world implementation (2023–2024)

#### (A) Conduction system pacing (CSP) vs right ventricular pacing (RVP) in bradycardia (including SND)
A 2024 multicenter prospective observational study of **984** pacemaker recipients (including SND indications) reported that CSP was independently associated with lower hazard of a composite endpoint (HF hospitalization, pacing-induced cardiomyopathy requiring CRT, or all-cause mortality) versus RVP, including in very elderly patients:
- <85 years: adjusted HR **0.63** (95% CI 0.40–0.98)
- ≥85 years: adjusted HR **0.40** (95% CI 0.17–0.94) (tan2024feasibilitysafetyand pages 1-2)

#### (B) Pediatric epicardial vs endocardial pacing in SND/AVB
A 2023 systematic review/meta-analysis (1,348 pediatric patients) found epicardial pacing associated with increased lead failure:
- Epicardial vs endocardial lead failure: pooled OR **3.00** (95% CI 2.05–4.39; I²=0%)
- No significant differences for threshold rise, infection, battery depletion, or mortality (patsiou2023epicardialversusendocardial pages 1-2)

#### (C) AF ablation and pacemaker risk in AF + SND
A 2024 claims-database study (Optum Clinformatics, 2013–2022) compared catheter ablation vs antiarrhythmic drug therapy in patients with AF and SND:
- PPM incidence rate: **55.8** vs **117.8** per 1000 person-years (ablation vs AAD)
- Hazard ratio for PPM after ablation: **0.58** (95% CI 0.46–0.72; p<0.001) (okumus2024threeyearincidenceof pages 1-2)

### 12.3 Experimental / emerging approaches
Mechanism-driven targeting is emerging (e.g., inflammation–galectin-3 axis in preclinical HF-SND) but remains preclinical in the retrieved corpus. (kahnert2024proteomicscoupleselectrical pages 1-2)


## 13. Prevention

Specific primary prevention strategies for SA block are not established as disease-specific interventions in the retrieved evidence. However, preventive concepts implied by etiology include:
- Avoiding/adjusting bradycardia-promoting drugs when clinically feasible
- Treating underlying cardiovascular disease (ischemia, HF) and metabolic abnormalities
- Addressing reversible extrinsic contributors and autonomic triggers
These are consistent with the diagnostic recommendation to exclude reversible causes before labeling intrinsic SND. (stevenson2021sinusnodedysfunction pages 1-2)


## 14. Other Species / Natural Disease

The retrieved corpus contained limited veterinary natural-history information specific to SA exit block. However, multiple core mechanisms and genetic contributors are studied across species (mouse, rabbit, zebrafish), supporting translational relevance (see Section 15). (wallace2021geneticcomplexityof pages 8-9, iop2021inheritedandacquired pages 10-12)


## 15. Model Organisms

### 15.1 Model types and examples
Preclinical modeling of SND/SA exit block includes:
- **Mouse genetic models**: Scn5a haploinsufficiency and other gene disruptions recapitulate SAN bradycardia and exit block; Ca-channel and transcription factor knockouts produce severe nodal phenotypes. (iop2021inheritedandacquired pages 10-12, wallace2021geneticcomplexityof pages 8-9)
- **Zebrafish**: developmental gene models (e.g., Shox2-related) are used to study pacemaker development and dysfunction. (wallace2021geneticcomplexityof pages 8-9)
- **In vitro heterologous expression**: functional studies of HCN4 variants and other channels in cultured cells. (iop2021inheritedandacquired pages 10-12)
- **In silico modeling**: used to connect channel remodeling (e.g., Hcn4 downregulation) to pacemaking changes in recent mechanistic work. (kahnert2024proteomicscoupleselectrical pages 1-2)

### 15.2 Model recapitulation and limitations
Animal models can reproduce bradycardia, prolonged SAN recovery, conduction delay, and exit block phenotypes, but translation is limited when human pathogenic variants are not known (e.g., some HCN1 knockout phenotypes without corresponding human mutation evidence). (iop2021inheritedandacquired pages 10-12)


---

## Visual evidence (open-access review figure/table)
The open-access review **“Biology of the Sinus Node and its Disease”** includes:
- A **table listing genes** associated with inherited or acquired sinus node dysfunction (including **HCN4** and **SCN5A**) and figures summarizing SAN anatomy and SND etiologies. (choudhury2015biologyofthe media a40e8af7, choudhury2015biologyofthe media 3ad3253b, choudhury2015biologyofthe media f26f0745, choudhury2015biologyofthe media ec6963a0)


## Evidence summary table (compiled)
The following table consolidates key definitions, epidemiology, genetics, mechanisms, and recent clinical developments:

| Topic | Key points (quantitative thresholds or stats) | Source (first author, journal) | Year | PMID | DOI/URL | Evidence quote |
|---|---|---|---|---|---|---|
| Definition / ECG criteria | SND is abnormal impulse initiation/propagation from the sinoatrial node; ECG findings include sinus bradycardia **<50 bpm**, sinus pause/arrest **>3 s**, SA exit block, chronotropic incompetence, and bradycardia–tachycardia syndrome; diagnosis requires symptom–rhythm correlation and exclusion of reversible causes. (stevenson2021sinusnodedysfunction pages 2-3, stevenson2021sinusnodedysfunction pages 1-2) | Stevenson, *Cardiac Pacing for the Clinician* | 2021 |  | https://doi.org/10.1007/978-0-387-72763-9_9 | “sinus bradycardia (**<50 bpm**), sinus pause (**>3 seconds**) or arrest, sinoatrial (SA) exit block, chronotropic incompetence, and alternating bradycardia–tachycardia” (stevenson2021sinusnodedysfunction pages 1-2) |
| ECG criteria / physiology | SA exit block is classified into first, second, and third degree; second-degree SA exit block includes **Type I (SA Wenckebach)** and **Type II (SA Mobitz II)**; first-degree SA exit block is not recognizable on surface ECG. (romandini2015sinoatrialexitblock pages 3-5) | Romandini, *Sinoatrial Exit Block* | 2015 |  | https://doi.org/10.1007/978-3-319-19926-9_22 | “The second-degree exit block is further classified into type I (SA block with Wenckebach conduction) and type II (SA Mobitz II).” (romandini2015sinoatrialexitblock pages 3-5) |
| Etiology / risk factors | Intrinsic causes include degenerative idiopathic fibrosis, ischemic necrosis, remodeling after MI/HF, infiltrative disease; extrinsic causes include medications, metabolic abnormalities, autonomic imbalance/increased vagal tone, and toxins. (stevenson2021sinusnodedysfunction pages 2-3, stevenson2021sinusnodedysfunction pages 1-2) | Stevenson, *Cardiac Pacing for the Clinician* | 2021 |  | https://doi.org/10.1007/978-0-387-72763-9_9 | “Etiologies are categorized as intrinsic (most commonly degenerative idiopathic fibrosis of the SAN; ischemic necrosis, cardiac remodeling) or extrinsic (medications, metabolic abnormalities, increased vagal tone after acute MI).” (stevenson2021sinusnodedysfunction pages 1-2) |
| Epidemiology | Incidence about **0.8 per 1,000 person-years**; prevalence rises with age, highest in **70–89 years**; expected to double by 2060. (stevenson2021sinusnodedysfunction pages 1-2, silva2021conductiondisordersthe pages 1-2) | Stevenson, *Cardiac Pacing for the Clinician* | 2021 |  | https://doi.org/10.1007/978-0-387-72763-9_9 | “incidence **~0.8 per 1,000 person‑years**, highest prevalence in ages **70–89**, expected to double by 2060” (stevenson2021sinusnodedysfunction pages 1-2) |
| Prognosis / clinical associations | About **50%** present with cerebral hypoperfusion/syncope-related symptoms; **~50%** have bradycardia–tachycardia syndrome; AF/atrial arrhythmias coexist in **40%–70%** at diagnosis and are linked to higher stroke/death risk. (john2016sinusnodeand pages 1-2, stevenson2021sinusnodedysfunction pages 2-3, stevenson2021sinusnodedysfunction pages 1-2) | John, *Circulation* | 2016 |  | https://doi.org/10.1161/circulationaha.116.018011 | “atrial arrhythmias [are] present in **40%–70%** of patients at SND diagnosis” (john2016sinusnodeand pages 1-2) |
| Epidemiology / device burden | SND is common in older adults, “**especially among people over age 65 (1/600)**”; symptomatic SND and AV block account for **~half of pacemaker implantations in the U.S.**; permanent pacemaker is standard treatment for chronic symptomatic SND. (mesirca2021pharmacologicapproachto pages 1-2) | Mesirca, *Annual Review of Pharmacology and Toxicology* | 2021 |  | https://doi.org/10.1146/annurev-pharmtox-031120-115815 | “Symptomatic SND and AV block account for **~half of pacemaker implantations in the U.S.**” (mesirca2021pharmacologicapproachto pages 1-2) |
| Genetics / electrophysiology testing | Inherited SND genes named include **HCN4, SCN5A, RYR2, CASQ2, ANKB**; EPS metrics include cSNRT and SACT; when significantly prolonged, combined **sensitivity 64%** and **specificity 88%**. (choudhury2015biologyofthe pages 3-4, choudhury2015biologyofthe media a40e8af7) | Choudhury, *Arrhythmia & Electrophysiology Review* | 2015 |  | https://doi.org/10.15420/aer.2015.4.1.28 | “The combined sensitivity of these two tests is reported as **64%** and combined specificity **88%** when significantly prolonged.” (choudhury2015biologyofthe pages 3-4) |
| Genetics overview | Current genetics reviews highlight recurrent loci/genes in SAN function disorders, especially **MYH6, HCN4, SCN5A, CACNA1C, CACNA1D**; SND has complex etiology with both heritable and acquired contributors. (milanesi2015thegeneticbasis pages 1-2) | van der Maarel, *Disease Models & Mechanisms* | 2023 |  | https://doi.org/10.1242/dmm.050101 | “Notably, candidates such as **MYH6, HCN4, SCN5A, CACNA1C and CACNA1D** frequently surface in these studies” (milanesi2015thegeneticbasis pages 1-2) |
| Signaling / mechanism | Emerging signaling regulation includes altered ion-channel expression and developmental signaling; review notes that “transient Notch activation reduced **Scn5a**” and exercise training can be associated with low **Hcn4** expression, supporting signaling-level control of SAN dysfunction. (milanesi2015thegeneticbasis pages 1-2) | Zheng, *Current Cardiology Reports* | 2023 |  | https://doi.org/10.1007/s11886-023-01885-8 | “transient Notch activation reduced **Scn5a** … Exercise training induced sinus bradycardia with low **Hcn4** expression” (milanesi2015thegeneticbasis pages 1-2) |
| Recent developments / molecular profiling | 2024 proteomics in murine HF-SND linked electrical remodeling to inflammation: downregulated **Hcn4**, inflammation slowed pacemaking, and **galectin-3 suppression prevented SND** in vivo, nominating galectin-3 as a therapeutic target. (kahnert2024proteomicscoupleselectrical pages 1-2) | Kahnert, *Cardiovascular Research* | 2024 |  | https://doi.org/10.1093/cvr/cvae054 | “experimentally induced inflammation downregulated **Hcn4** and slowed pacemaking… in vivo suppression of **galectin-3** in the animal model of heart failure **prevented SND**” (kahnert2024proteomicscoupleselectrical pages 1-2) |
| Treatment / guideline-based pacing | First-line therapy for **symptomatic confirmed SND** is permanent pacemaker implantation, generally **atrial-based pacing with limited ventricular pacing** when needed; unstable patients may require temporary pacing. (stevenson2021sinusnodedysfunction pages 2-3, stevenson2021sinusnodedysfunction pages 1-2, mesirca2021pharmacologicapproachto pages 1-2) | Stevenson, *Cardiac Pacing for the Clinician* | 2021 |  | https://doi.org/10.1007/978-0-387-72763-9_9 | “First‑line therapy for symptomatic, confirmed disease is **permanent pacemaker placement with atrial‑based pacing and limited ventricular pacing** when needed.” (stevenson2021sinusnodedysfunction pages 1-2) |
| Recent developments / real-world implementation | In AF + SND, catheter ablation was associated with lower pacemaker implantation than antiarrhythmic drugs: **55.8 vs 117.8 per 1000 person-years**; **HR 0.58 (95% CI 0.46–0.72)**, with benefit in paroxysmal and persistent AF. (okumus2024threeyearincidenceof pages 1-2) | Okumus, *Journal of Interventional Cardiac Electrophysiology* | 2024 |  | https://doi.org/10.1007/s10840-024-01790-2 | “The incidence rate of PPM implantation… was **55.8** for the CA cohort and **117.8** for the AAD cohort… **HR, 0.58; 95% CI, 0.46–0.72**” (okumus2024threeyearincidenceof pages 1-2) |


*Table: This table compiles core evidence for sinoatrial block/sinoatrial exit block and the broader sinus node dysfunction phenotype. It highlights diagnostic criteria, causes, genetics, epidemiology, prognosis, treatment, and recent 2023–2024 research developments with concise source-linked quotes.*


## Notes on evidence gaps vs requested template
- **MONDO/MeSH/ICD identifiers**: not available in the retrieved source set.
- **PMIDs**: not reliably extractable from the retrieved excerpts; DOIs/URLs and publication months/years are provided.
- **Disease-specific biomarkers/omics diagnostics**: a 2024 murine proteomics study provides mechanistic targets (Hcn4 downregulation; galectin-3 axis) but not validated clinical biomarkers for SA block. (kahnert2024proteomicscoupleselectrical pages 1-2)



References

1. (stevenson2021sinusnodedysfunction pages 1-2): Irene H. Stevenson, Paul B. Sparks, and Jonathan M. Kalman. Sinus node dysfunction. Cardiac Pacing for the Clinician, pages 377-405, Jan 2021. URL: https://doi.org/10.1007/978-0-387-72763-9\_9, doi:10.1007/978-0-387-72763-9\_9. This article has 63 citations.

2. (romandini2015sinoatrialexitblock pages 3-5): Andrea Romandini and Lorena Scappini. Sinoatrial exit block. ArXiv, pages 255-264, Jan 2015. URL: https://doi.org/10.1007/978-3-319-19926-9\_22, doi:10.1007/978-3-319-19926-9\_22. This article has 0 citations.

3. (stevenson2021sinusnodedysfunction pages 2-3): Irene H. Stevenson, Paul B. Sparks, and Jonathan M. Kalman. Sinus node dysfunction. Cardiac Pacing for the Clinician, pages 377-405, Jan 2021. URL: https://doi.org/10.1007/978-0-387-72763-9\_9, doi:10.1007/978-0-387-72763-9\_9. This article has 63 citations.

4. (mesirca2021pharmacologicapproachto pages 1-2): Pietro Mesirca, Vadim V. Fedorov, Thomas J. Hund, Angelo G. Torrente, Isabelle Bidaud, Peter J. Mohler, and Matteo E. Mangoni. Pharmacologic approach to sinoatrial node dysfunction. Annual Review of Pharmacology and Toxicology, 61:757-778, Jan 2021. URL: https://doi.org/10.1146/annurev-pharmtox-031120-115815, doi:10.1146/annurev-pharmtox-031120-115815. This article has 54 citations and is from a highest quality peer-reviewed journal.

5. (patsiou2023epicardialversusendocardial pages 1-2): Vasiliki Patsiou, Anna-Bettina Haidich, Amalia Baroutidou, Andreas Giannopoulos, and George Giannakoulas. Epicardial versus endocardial pacing in paediatric patients with atrioventricular block or sinus node dysfunction: a systematic review and meta-analysis. Pediatric Cardiology, 44:1641-1648, Jul 2023. URL: https://doi.org/10.1007/s00246-023-03213-x, doi:10.1007/s00246-023-03213-x. This article has 18 citations and is from a peer-reviewed journal.

6. (tan2024feasibilitysafetyand pages 1-2): Eugene S. J. Tan, Rodney Soh, Jie-Ying Lee, Elaine Boey, Siew-Pang Chan, Swee-Chong Seow, Lisa J. T. Teo, Colin Yeo, Vern Hsen Tan, and Pipin Kojodjojo. Feasibility, safety and outcomes of conduction system pacing for bradycardia amongst the very elderly. Scientific Reports, Aug 2024. URL: https://doi.org/10.1038/s41598-024-69388-2, doi:10.1038/s41598-024-69388-2. This article has 4 citations and is from a peer-reviewed journal.

7. (okumus2024threeyearincidenceof pages 1-2): Nazli Kubra Okumus, Emily P. Zeitler, Abdelmoniem Moustafa, Maximiliano Iglesias, Rahul Khanna, Yiran Rong, and Saima Karim. Three-year incidence of pacemaker implantation in patients with atrial fibrillation and sinus node dysfunction receiving ablation versus antiarrhythmic drugs. Journal of Interventional Cardiac Electrophysiology, 67:1593-1602, Apr 2024. URL: https://doi.org/10.1007/s10840-024-01790-2, doi:10.1007/s10840-024-01790-2. This article has 5 citations and is from a peer-reviewed journal.

8. (ishikawa2017sicksinussyndrome pages 1-6): Taisuke Ishikawa, Seiko Ohno, Takashi Murakami, Kentaro Yoshida, Hiroyuki Mishima, Tetsuya Fukuoka, Hiroki Kimoto, Risa Sakamoto, Takafumi Ohkusa, Takeshi Aiba, Akihiko Nogami, Naokata Sumitomo, Wataru Shimizu, Koh-ichiro Yoshiura, Hitoshi Horigome, Minoru Horie, and Naomasa Makita. Sick sinus syndrome with hcn4 mutations shows early onset and frequent association with atrial fibrillation and left ventricular noncompaction. Heart rhythm, 14 5:717-724, May 2017. URL: https://doi.org/10.1016/j.hrthm.2017.01.020, doi:10.1016/j.hrthm.2017.01.020. This article has 64 citations and is from a peer-reviewed journal.

9. (wallace2021geneticcomplexityof pages 8-9): Michael J. Wallace, Mona El Refaey, Pietro Mesirca, Thomas J. Hund, Matteo E. Mangoni, and Peter J. Mohler. Genetic complexity of sinoatrial node dysfunction. Frontiers in Genetics, Apr 2021. URL: https://doi.org/10.3389/fgene.2021.654925, doi:10.3389/fgene.2021.654925. This article has 46 citations and is from a peer-reviewed journal.

10. (mesirca2021pharmacologicapproachto pages 5-6): Pietro Mesirca, Vadim V. Fedorov, Thomas J. Hund, Angelo G. Torrente, Isabelle Bidaud, Peter J. Mohler, and Matteo E. Mangoni. Pharmacologic approach to sinoatrial node dysfunction. Annual Review of Pharmacology and Toxicology, 61:757-778, Jan 2021. URL: https://doi.org/10.1146/annurev-pharmtox-031120-115815, doi:10.1146/annurev-pharmtox-031120-115815. This article has 54 citations and is from a highest quality peer-reviewed journal.

11. (john2016sinusnodeand pages 1-2): Roy M. John and Saurabh Kumar. Sinus node and atrial arrhythmias. Circulation, 133 19:1892-900, May 2016. URL: https://doi.org/10.1161/circulationaha.116.018011, doi:10.1161/circulationaha.116.018011. This article has 257 citations and is from a highest quality peer-reviewed journal.

12. (maarel2023geneticsofsinoatrial pages 13-14): Lieve E. van der Maarel, Alex V. Postma, and Vincent M. Christoffels. Genetics of sinoatrial node function and heart rate disorders. Disease Models & Mechanisms, May 2023. URL: https://doi.org/10.1242/dmm.050101, doi:10.1242/dmm.050101. This article has 20 citations and is from a domain leading peer-reviewed journal.

13. (maarel2023geneticsofsinoatrial pages 14-15): Lieve E. van der Maarel, Alex V. Postma, and Vincent M. Christoffels. Genetics of sinoatrial node function and heart rate disorders. Disease Models & Mechanisms, May 2023. URL: https://doi.org/10.1242/dmm.050101, doi:10.1242/dmm.050101. This article has 20 citations and is from a domain leading peer-reviewed journal.

14. (milanesi2015thegeneticbasis pages 1-2): Raffaella Milanesi, Annalisa Bucchi, and Mirko Baruscotti. The genetic basis for inherited forms of sinoatrial dysfunction and atrioventricular node dysfunction. Journal of Interventional Cardiac Electrophysiology, 43:121-134, Apr 2015. URL: https://doi.org/10.1007/s10840-015-9998-z, doi:10.1007/s10840-015-9998-z. This article has 40 citations and is from a peer-reviewed journal.

15. (wallace2021geneticcomplexityof pages 6-7): Michael J. Wallace, Mona El Refaey, Pietro Mesirca, Thomas J. Hund, Matteo E. Mangoni, and Peter J. Mohler. Genetic complexity of sinoatrial node dysfunction. Frontiers in Genetics, Apr 2021. URL: https://doi.org/10.3389/fgene.2021.654925, doi:10.3389/fgene.2021.654925. This article has 46 citations and is from a peer-reviewed journal.

16. (kahnert2024proteomicscoupleselectrical pages 1-2): Konstantin Kahnert, Luca Soattin, Robert W Mills, Claire Wilson, Svetlana Maurya, Andrea Sorrentino, Sami Al-Othman, Roman Tikhomirov, Yordi J van de Vegte, Finn B Hansen, Jonathan Achter, Wei Hu, Min Zi, Matthew Smith, Pim van der Harst, Morten S Olesen, Kristine Boisen Olsen, Jytte Banner, Thomas H L Jensen, Henggui Zhang, Mark R Boyett, Alicia D’Souza, and Alicia Lundby. Proteomics couples electrical remodelling to inflammation in a murine model of heart failure with sinus node dysfunction. Cardiovascular Research, 120:927-942, Apr 2024. URL: https://doi.org/10.1093/cvr/cvae054, doi:10.1093/cvr/cvae054. This article has 16 citations and is from a domain leading peer-reviewed journal.

17. (choudhury2015biologyofthe pages 3-4): Moinuddin Choudhury, Mark R Boyett, and Gwilym M Morris. Biology of the sinus node and its disease. Arrhythmia &amp; Electrophysiology Review, 4:28, Jan 2015. URL: https://doi.org/10.15420/aer.2015.4.1.28, doi:10.15420/aer.2015.4.1.28. This article has 148 citations and is from a peer-reviewed journal.

18. (iop2021inheritedandacquired pages 10-12): Laura Iop, Sabino Iliceto, Giovanni Civieri, and Francesco Tona. Inherited and acquired rhythm disturbances in sick sinus syndrome, brugada syndrome, and atrial fibrillation: lessons from preclinical modeling. Cells, 10:3175, Nov 2021. URL: https://doi.org/10.3390/cells10113175, doi:10.3390/cells10113175. This article has 18 citations.

19. (choudhury2015biologyofthe media a40e8af7): Moinuddin Choudhury, Mark R Boyett, and Gwilym M Morris. Biology of the sinus node and its disease. Arrhythmia &amp; Electrophysiology Review, 4:28, Jan 2015. URL: https://doi.org/10.15420/aer.2015.4.1.28, doi:10.15420/aer.2015.4.1.28. This article has 148 citations and is from a peer-reviewed journal.

20. (choudhury2015biologyofthe media 3ad3253b): Moinuddin Choudhury, Mark R Boyett, and Gwilym M Morris. Biology of the sinus node and its disease. Arrhythmia &amp; Electrophysiology Review, 4:28, Jan 2015. URL: https://doi.org/10.15420/aer.2015.4.1.28, doi:10.15420/aer.2015.4.1.28. This article has 148 citations and is from a peer-reviewed journal.

21. (choudhury2015biologyofthe media f26f0745): Moinuddin Choudhury, Mark R Boyett, and Gwilym M Morris. Biology of the sinus node and its disease. Arrhythmia &amp; Electrophysiology Review, 4:28, Jan 2015. URL: https://doi.org/10.15420/aer.2015.4.1.28, doi:10.15420/aer.2015.4.1.28. This article has 148 citations and is from a peer-reviewed journal.

22. (choudhury2015biologyofthe media ec6963a0): Moinuddin Choudhury, Mark R Boyett, and Gwilym M Morris. Biology of the sinus node and its disease. Arrhythmia &amp; Electrophysiology Review, 4:28, Jan 2015. URL: https://doi.org/10.15420/aer.2015.4.1.28, doi:10.15420/aer.2015.4.1.28. This article has 148 citations and is from a peer-reviewed journal.

23. (silva2021conductiondisordersthe pages 1-2): Rose M.F.L. da Silva and Alessandra de Souza Maciel. Conduction disorders: the value of surface ecg. Current Cardiology Reviews, 17:173-181, May 2021. URL: https://doi.org/10.2174/1573403x16666200511090151, doi:10.2174/1573403x16666200511090151. This article has 11 citations.