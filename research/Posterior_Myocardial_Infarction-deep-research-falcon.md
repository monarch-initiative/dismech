---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T07:56:46.945875'
end_time: '2026-05-06T08:09:57.128128'
duration_seconds: 790.18
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Posterior Myocardial Infarction
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
- **Disease Name:** Posterior Myocardial Infarction
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Posterior Myocardial Infarction** covering all of the
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
- **Disease Name:** Posterior Myocardial Infarction
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Posterior Myocardial Infarction** covering all of the
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


## Comprehensive Disease Characteristics Report: Posterior Myocardial Infarction (Posterior MI)

### Executive summary (current understanding)
Posterior myocardial infarction (posterior MI) refers to acute myocardial infarction involving the posterior left ventricular wall. It is frequently under-recognized because the standard 12-lead ECG does not directly visualize the posterior wall; instead, posterior injury often appears as reciprocal (“mirror-image”) changes in the anterior precordial leads (V1–V3). Confirmation and improved detection can be achieved by recording posterior leads V7–V9, where small ST-elevation thresholds (≥0.5 mm) are clinically important. Contemporary research emphasizes that a substantial portion of acute coronary occlusions (including many circumflex/posterior occlusions) do not meet classic STEMI criteria and may benefit from an “occlusion MI (OMI)” paradigm and/or AI-assisted ECG interpretation. (garciaarias2024isolatedposterioracute pages 1-3, moskovitz2025aninterestingcase pages 2-3, kola2024ominomitimefor pages 2-4, herman2024internationalevaluationof pages 1-2)

---

## 1. Disease information

### 1.1 What is the disease?
Posterior MI is an acute MI affecting the posterior LV wall, often missed on 12-lead ECG because posterior injury is not directly sampled by standard leads; clinicians rely on reciprocal anterior changes and/or posterior leads V7–V9 to detect posterior ST-elevation patterns. (garciaarias2024isolatedposterioracute pages 1-3, moskovitz2025aninterestingcase pages 2-3)

### 1.2 Key identifiers (OMIM, Orphanet, ICD, MeSH, MONDO)
The retrieved evidence did not include OMIM, Orphanet, MeSH, or MONDO identifiers specific to posterior MI; therefore, these identifiers cannot be confirmed from the retrieved sources. (garciaarias2024isolatedposterioracute pages 1-3, kwok2024structuralcomplicationsfollowing pages 2-4)

ICD-10 coding for acute MI is represented within the I21.* family in administrative datasets; one large US inpatient study identified STEMI admissions using ICD-10 codes I21.0, I21.1, I21.2, and I21.3, illustrating how MI subtypes are operationalized in claims/inpatient datasets (note: this evidence does not establish that I21.2 is posterior-MI-specific). (kwok2024structuralcomplicationsfollowing pages 2-4)

### 1.3 Common synonyms / alternative names
Commonly used labels in the retrieved literature include: “posterior myocardial infarction,” “posterior MI,” “posterior STEMI,” “posterior wall MI,” and “isolated posterior MI.” (garciaarias2024isolatedposterioracute pages 1-3, alsagaff2022isolatedposteriorstelevation pages 8-8)

### 1.4 Provenance (patient-level vs aggregated)
Evidence here is largely aggregated disease-level clinical literature (ECG-focused reviews/case series and OMI-paradigm papers) plus administrative dataset usage of ICD-10 codes in inpatient research. (garciaarias2024isolatedposterioracute pages 1-3, kwok2024structuralcomplicationsfollowing pages 2-4)

| Category | Field | Value | Notes / Resource Type |
|---|---|---|---|
| Disease concept | Brief definition | Posterior myocardial infarction (PMI) is an acute myocardial infarction involving the posterior left ventricular wall, often under-recognized on standard 12-lead ECG because the posterior wall is not directly visualized; posterior leads V7-V9 and reciprocal/anterior mirror changes aid diagnosis. (garciaarias2024isolatedposterioracute pages 1-3, moskovitz2025aninterestingcase pages 2-3) | Primarily disease-level clinical/guideline-style characterization from case series/reviews; not a unique EHR-only construct. |
| Synonyms | Common names | posterior myocardial infarction; posterior MI; posterior STEMI; isolated posterior MI; posterior wall MI. (garciaarias2024isolatedposterioracute pages 1-3, moskovitz2025aninterestingcase pages 2-3, alsagaff2022isolatedposteriorstelevation pages 8-8) | Synonym usage derived from clinical literature and ECG-focused reports/guidance. |
| Standard identifiers | ICD-10 family | Acute myocardial infarction is coded under ICD-10 I21.* / I22.* in claims/EHR validation studies. (kwok2024structuralcomplicationsfollowing pages 2-4) | EHR/claims-oriented coding framework; used for case identification in administrative datasets. |
| Standard identifiers | ICD-10 STEMI subtype example | I21.2 was explicitly included among STEMI ICD-10 codes (I21.0, I21.1, I21.2, I21.3) in a National Inpatient Sample STEMI outcomes study. (kwok2024structuralcomplicationsfollowing pages 2-4) | Administrative/research coding use; evidence supports relevance to STEMI datasets, but retrieved sources do not prove it is posterior-MI-specific. |
| Standard identifiers | MONDO ID | not found in retrieved sources | No MONDO identifier was present in the retrieved evidence. |
| Standard identifiers | MeSH | not found in retrieved sources | No MeSH identifier was present in the retrieved evidence. |
| Resource provenance | Disease-level vs patient-level information | Retrieved PMI information is mostly aggregated disease-level clinical literature/guideline-style evidence; ICD-10 usage comes from EHR/claims and inpatient database studies, while ECG criteria come from guideline/review/case-series literature. (garciaarias2024isolatedposterioracute pages 1-3, moskovitz2025aninterestingcase pages 2-3, kwok2024structuralcomplicationsfollowing pages 2-4) | Mixed provenance: disease-level clinical resources plus patient-level coding/administrative datasets. |
| Coding caution | Specificity of coding for PMI | Retrieved evidence supports AMI/STEMI family coding (I21.*) and inclusion of I21.2 in STEMI analyses, but does not provide a posterior-MI-specific code mapping from an authoritative coding manual. (kwok2024structuralcomplicationsfollowing pages 2-4) | Important for knowledge-base curation: coding evidence here is indirect for PMI localization. |


*Table: This table summarizes how posterior myocardial infarction is defined, named, and represented in the retrieved evidence. It distinguishes disease-level ECG/guideline terminology from ICD-10 coding used in EHR/claims and inpatient database research.*

---

## 2. Etiology

### 2.1 Disease causal factors
Posterior MI is generally caused by acute reduction/cessation of coronary blood flow due to atherosclerotic plaque rupture/erosion with superimposed thrombosis (type 1 MI framework). (młynarska2024fromatheroscleroticplaque pages 1-3, młynarska2024fromatheroscleroticplaque pages 4-6)

In posterior/inferior territories, the culprit vessel is frequently the left circumflex (LCx) or right coronary artery (RCA), and posterior MI may present without classic ST-elevation criteria. (garciaarias2024isolatedposterioracute pages 1-3, bruno2023occlusionofthe pages 2-3)

### 2.2 Risk factors (genetic, environmental/lifestyle)
A 2024 molecular review summarizing type 1 MI pathogenesis lists major predisposing factors including high LDL-C, cigarette smoking, chronic kidney disease, diabetes mellitus, hypertension, obesity/adiposity, and familial hypercholesterolaemia (FH). (młynarska2024fromatheroscleroticplaque pages 1-3)

**Genetic susceptibility (example: FH):** FH is described as autosomal dominant and linked to high LDL-C, with implicated genes including LDLR, APOB, and PCSK9. (młynarska2024fromatheroscleroticplaque pages 3-4)

### 2.3 Protective factors
The retrieved evidence does not provide quantified protective factors (e.g., effect sizes for statins, smoking cessation, exercise) specific to posterior MI or MI generally. This is a limitation of the current retrieved corpus. (młynarska2024fromatheroscleroticplaque pages 1-3)

### 2.4 Gene–environment interactions
No gene–environment interaction data specific to posterior MI was present in the retrieved sources. (młynarska2024fromatheroscleroticplaque pages 3-4)

---

## 3. Phenotypes

### 3.1 Core clinical phenotype (symptoms and signs)
Posterior MI presents as an acute coronary syndrome; because posterior wall injury is “electrically hidden” on standard ECG, presentation is often defined by ECG patterns and biomarker/imaging confirmation rather than unique symptomatology in the retrieved sources. (garciaarias2024isolatedposterioracute pages 1-3)

### 3.2 ECG phenotypes (high-yield posterior MI signatures)
Posterior MI often produces reciprocal changes in V1–V3 rather than anterior ST elevation. Key patterns include:
- Horizontal ST depression in V1–V3 (often maximal in early precordial leads). (garciaarias2024isolatedposterioracute pages 1-3, moskovitz2025aninterestingcase pages 2-3)
- Dominant/tall R waves with R/S ratio >1 (often V2–V4), sometimes with broad R waves (>30 ms). (moskovitz2025aninterestingcase pages 2-3)
- Upright T waves in anterior leads accompanying ST depression. (moskovitz2025aninterestingcase pages 2-3)

**Posterior lead confirmation:** ST-elevation ≥0.5 mm in V7–V9 is described as a confirmatory threshold. (garciaarias2024isolatedposterioracute pages 1-3, moskovitz2025aninterestingcase pages 2-3)

### 3.3 Laboratory abnormalities
In the OMI definition used in a 2024 OMI/NOMI reclassification study, markedly elevated troponin thresholds were part of the operational definition for certain angiographic cases (e.g., cTnI >10.0 ng/mL or hs-cTnI >5000 ng/L when TIMI 3 flow lesions were intervened upon). (kola2024ominomitimefor pages 2-4)

### 3.4 Phenotype characteristics
- **Age of onset:** adult-onset (acute presentation). (garciaarias2024isolatedposterioracute pages 1-3)
- **Course:** acute onset with risk of delayed recognition when classic STEMI criteria are absent. (kola2024ominomitimefor pages 2-4, herman2024internationalevaluationof pages 7-8)

### 3.5 Suggested ontology mappings (examples)
These ontology suggestions are provided for knowledge-base structuring; the retrieved sources do not explicitly enumerate ontology IDs.
- **HPO (symptoms/signs):** Chest pain (HP:0100749), ST segment depression (HP:0025315), ST segment elevation (HP:0025320), Elevated cardiac troponin (HP:0030343).
- **LOINC (lab):** high-sensitivity cardiac troponin assays (LOINC varies by platform).

---

## 4. Genetic / molecular information

Posterior MI is not a monogenic disease; it is typically multifactorial, with genetic contributions largely mediated through atherosclerotic risk (e.g., FH). (młynarska2024fromatheroscleroticplaque pages 3-4, młynarska2024fromatheroscleroticplaque pages 1-3)

### 4.1 Causal genes
No “causal gene” for posterior MI was identified in the retrieved evidence; however, genes implicated in familial hypercholesterolaemia (a major MI risk state) include LDLR, APOB, and PCSK9. (młynarska2024fromatheroscleroticplaque pages 3-4)

### 4.2 Pathogenic variants
The retrieved evidence does not provide variant-level nomenclature, allele frequencies (gnomAD), or ACMG classifications for posterior MI. (młynarska2024fromatheroscleroticplaque pages 3-4)

### 4.3 Epigenetics, chromosomal abnormalities
Not found in retrieved sources for posterior MI. (młynarska2024fromatheroscleroticplaque pages 1-3)

---

## 5. Environmental information

The retrieved 2024 type 1 MI review identifies major lifestyle/environmental contributors to atherosclerotic MI risk including cigarette smoking, diet/physical inactivity (via obesity/adiposity), and metabolic risk factors (hypertension, diabetes). No posterior-wall-specific environmental risks were identified. (młynarska2024fromatheroscleroticplaque pages 1-3, młynarska2024fromatheroscleroticplaque pages 17-19)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (trigger → clinical manifestation)
1. **Atherosclerotic plaque progression** with lipid accumulation and inflammatory cell infiltration leads to a vulnerable plaque. (młynarska2024fromatheroscleroticplaque pages 4-6)
2. **Plaque rupture/erosion** exposes subendothelial matrix and tissue factor, promoting platelet adhesion and coagulation cascade activation. (młynarska2024fromatheroscleroticplaque pages 4-6)
3. **Coronary thrombosis/occlusion** reduces perfusion, causing ischemia and myocyte injury/necrosis (MI). (młynarska2024fromatheroscleroticplaque pages 1-3)
4. **ECG manifestation depends on lead orientation.** Posterior LV injury often appears as reciprocal anterior ST depression in V1–V3; posterior leads V7–V9 can show small ST elevations. (garciaarias2024isolatedposterioracute pages 1-3, moskovitz2025aninterestingcase pages 2-3)

### 6.2 Inflammation and systemic signals (outcome relevance)
In a large prospective cohort, LCx occlusion in NSTE-ACS was associated with higher 1-year MACE, and inflammatory markers (hs-CRP, leukocyte indices) were associated with total coronary occlusion in NSTE-ACS, supporting systemic inflammation as a correlating feature of higher-risk occlusion phenotypes. (bruno2023occlusionofthe pages 2-3)

### 6.3 Suggested ontology mappings
- **GO Biological Processes:** platelet activation; blood coagulation; inflammatory response; response to oxidative stress.
- **CL Cell types:** macrophage; vascular smooth muscle cell; endothelial cell; platelet.
- **UBERON anatomy:** myocardium of left ventricle; posterior wall of left ventricle.

---

## 7. Anatomical structures affected

### 7.1 Organ/system level
- Primary organ: heart (myocardium; LV posterior wall). (garciaarias2024isolatedposterioracute pages 1-3)
- Coronary anatomy frequently implicated in “hidden” occlusion phenotypes includes LCx and RCA in NSTE-ACS, with LCx occlusions notable for total occlusion despite absent ST-elevation. (bruno2023occlusionofthe pages 2-3)

### 7.2 Tissue/cell level
Ischemia and necrosis affect cardiomyocytes and the microvasculature; upstream mechanisms involve vascular endothelium, inflammatory cells, and platelets in thrombosis. (młynarska2024fromatheroscleroticplaque pages 4-6)

---

## 8. Temporal development

### 8.1 Onset and progression
Posterior MI is an acute presentation within ACS. A critical temporal feature is the **diagnostic delay** when patients do not meet classic STEMI criteria, leading to later catheterization/reperfusion for occlusive infarctions that are STEMI-negative. (kola2024ominomitimefor pages 2-4, herman2024internationalevaluationof pages 7-8)

---

## 9. Inheritance and population

### 9.1 Epidemiology
- Isolated posterior MI is uncommon, with estimates in retrieved sources around ~3.3% and ~4% (and one source noting 3–7% in prior reports). (garciaarias2024isolatedposterioracute pages 1-3, moskovitz2025aninterestingcase pages 2-3)
- Posterior involvement may occur with inferior or lateral infarctions; one 2024 clinical letter cites posterior involvement in ~20% of lateral or inferior infarctions. (garciaarias2024isolatedposterioracute pages 1-3)

### 9.2 Genetic etiology and inheritance
- Posterior MI: multifactorial/polygenic risk through atherosclerosis risk.
- FH: autosomal dominant inheritance; LDLR/APOB/PCSK9 implicated. (młynarska2024fromatheroscleroticplaque pages 3-4)

---

## 10. Diagnostics

### 10.1 Clinical tests: ECG criteria and extended leads
Posterior MI is commonly suspected based on 12-lead ECG reciprocal patterns and confirmed with posterior leads.

Key practical criteria and quantitative thresholds are summarized here:
- **Posterior lead criterion:** ST-elevation ≥0.5 mm in V7–V9 is described as confirmatory. (garciaarias2024isolatedposterioracute pages 1-3, moskovitz2025aninterestingcase pages 2-3)
- **Mirror-image 12-lead pattern:** horizontal ST depression V1–V3 with dominant R waves (R/S >1) and upright T waves. (moskovitz2025aninterestingcase pages 2-3)
- **High-specificity marker:** “suspected ischemic” ST depression maximal in V1–V4 had 97% specificity and 37% sensitivity for OMI in a high-risk ACS cohort (a posterior/lateral-occlusion enrichment pattern). (meyers2021ischemicst‐segmentdepression pages 13-14)

### 10.2 Posterior lead threshold optimization (data)
One cited dataset noted that only ~53% of circumflex-related posterior MI showed ≥1.0 mm posterior-lead ST elevation, while lowering the ST-elevation threshold to 0.5 mm increased detection to 94% (with ~6% still missed). (ramjaun2021ecgchangesin pages 3-4)

### 10.3 Real-world implementation: synthesized posterior leads
A 2024 Sensors review describes synthesized 18-lead ECG (syn18-ECG) that computationally derives posterior leads V7–V9 from a standard 12-lead recording, avoiding patient repositioning and additional electrode placement; ST elevation in V7–V9 is highlighted as a mechanism to reduce missed posterior ACS. (yamamoto2024clinicalutilityof pages 1-3, yamamoto2024clinicalutilityof pages 3-4)

**Lead placement visualization:** posterior electrode placement for V7–V9 (useful for protocol implementation) is shown in the extracted figure. (yamamoto2024clinicalutilityof media 15a08389)

### 10.4 Diagnostic paradigm shift: STEMI/NSTEMI vs OMI/NOMI and AI
**Expert/opinion-driven and data-supported analysis:**
- A 2024 reclassification study found that 40% of angiographic OMI did not fulfill STEMI criteria and that STEMI-negative OMI was associated with major PCI delays (only 11% within 12 h vs 77% for STEMI-positive OMI). (kola2024ominomitimefor pages 2-4)
- A 2024 international evaluation of an AI ECG model reported markedly higher sensitivity for detecting OMI than STEMI criteria (80.6% vs 32.5%) with high specificity (93.7%). (herman2024internationalevaluationof pages 1-2)
- In that AI study, STEMI criteria missed 67.5% of OMI patients; only 33.9% of those missed received revascularization within 2 hours, illustrating time-sensitive consequences of STEMI-only activation logic. (herman2024internationalevaluationof pages 7-8)

| Finding/criterion | Quantitative threshold or statistic | Clinical implication | Source |
|---|---|---|---|
| 12-lead ECG “mirror” signs of posterior MI/posterior OMI | Horizontal ST depression in V1-V3; dominant/tall R wave with R/S >1 (often V2-V4); upright anterior T waves; broad R wave >30 ms | Standard 12-lead ECG may show reciprocal posterior-wall ischemia rather than classic ST elevation; should prompt suspicion for posterior MI and consideration of posterior leads or urgent angiography | (garciaarias2024isolatedposterioracute pages 1-3, moskovitz2025aninterestingcase pages 2-3, moskovitz2025aninterestingcase pages 3-3) |
| Posterior leads V7-V9 diagnostic threshold | ST-segment elevation >=0.5 mm in V7-V9 | Confirms posterior infarction pattern that may be missed on standard 12-lead ECG; supports emergent reperfusion pathway as STEMI-equivalent/OMI pattern | (garciaarias2024isolatedposterioracute pages 1-3, moskovitz2025aninterestingcase pages 2-3) |
| ST depression maximal in V1-V4 (STDmaxV1-4) | Specificity 97%; sensitivity 37% for OMI; 90% of patients with suspected ischemic STDmaxV1-4 had an acute culprit lesion, 84% had OMI | Highly specific but not sensitive marker; useful for recognizing posterior/lateral occlusion MI, especially circumflex-related events that fail STEMI criteria | (meyers2021ischemicst‐segmentdepression pages 13-14) |
| Lowering posterior lead threshold from 1.0 mm to 0.5 mm | Detection increased from ~53% to 94% | Supports the modern lower V7-V9 STE cutoff because many posterior infarctions have only small-amplitude STE in posterior leads | (ramjaun2021ecgchangesin pages 3-4) |
| Incidence/prevalence: isolated posterior MI | ~3.3%; ~4%; 3-7% of acute MIs/ACS presentations depending on series | Isolated posterior MI is uncommon and therefore frequently under-recognized, contributing to delayed diagnosis | (garciaarias2024isolatedposterioracute pages 1-3, moskovitz2025aninterestingcase pages 2-3) |
| Posterior involvement with other infarct territories | Posterior involvement occurs in ~20% of lateral or inferior infarctions | Posterior extension is not rare in inferior/lateral MI and should be actively sought with posterior leads when anterior ST depression is present | (garciaarias2024isolatedposterioracute pages 1-3) |
| OMI paradigm misclassification (Kola 2024) | 98/334 ACS patients (29.3%) were STEMI(-)OMI; 96/241 OMI patients (40%) did not fulfill STEMI criteria; only 11% of STEMI(-)OMI underwent PCI within 12 h vs 77% of STEMI(+)OMI | Reliance on STEMI criteria misses a substantial fraction of occlusive infarctions and is associated with major reperfusion delay | (kola2024ominomitimefor pages 2-4) |
| AI/OMI triage performance vs STEMI criteria (Herman 2024) | AI AUC 0.938, sensitivity 80.6%, specificity 93.7% vs STEMI criteria sensitivity 32.5%, specificity 97.7%; OMI prevalence 21.6% in test set | AI-enhanced ECG interpretation can improve detection of occult occlusion MI, including posterior/inferior territory occlusions that do not meet STEMI criteria | (herman2024internationalevaluationof pages 2-3, herman2024internationalevaluationof pages 1-2, herman2024internationalevaluationof pages 7-8) |
| OMI delays and false negatives on STEMI criteria (Herman 2024) | STEMI criteria missed 330 OMI patients (67.5% of all OMI); only 112/330 (33.9%) received revascularization <2 h; AI identified 133/218 STEMI-criteria false-negative OMI patients (61.0%) on first ECG | Highlights real-world treatment delay caused by STEMI-based classification and the potential benefit of OMI-focused or AI-supported recognition pathways | (herman2024internationalevaluationof pages 7-8) |


*Table: This table summarizes the main electrocardiographic criteria and high-yield quantitative statistics for posterior myocardial infarction/posterior OMI. It is useful for contrasting classic posterior ECG findings with newer OMI-era evidence on missed occlusions and diagnostic delay.*

---

## 11. Outcome / prognosis

### 11.1 Location-specific outcome signal (LCx occlusion in NSTE-ACS)
In a prospective real-world cohort (SPUM-ACS), among NSTE-ACS patients, total coronary occlusion was more frequent for LCx (27%) and RCA (24%) than for LAD (9%), and **LCx involvement independently predicted higher 1-year MACE** (adjusted HR 1.68, 95% CI 1.10–2.59). (bruno2023occlusionofthe pages 2-3)

### 11.2 Systems-level outcome concern: missed occlusions and delayed reperfusion
Evidence from OMI/AI literature indicates that STEMI criteria miss a large fraction of occlusive infarctions, with substantial delays to catheterization/revascularization for those missed, which is mechanistically consistent with worse outcomes in untreated/delayed occlusion states. (kola2024ominomitimefor pages 2-4, herman2024internationalevaluationof pages 7-8)

---

## 12. Treatment

### 12.1 Acute management (reperfusion emphasis)
The retrieved evidence supports that posterior MI patterns represent clinically important occlusion phenotypes where timely reperfusion is critical; however, detailed pharmacotherapy algorithms (dual antiplatelet therapy, anticoagulation, beta-blockers, statins) are not described in the retrieved excerpts. (moskovitz2025aninterestingcase pages 2-3, kola2024ominomitimefor pages 2-4)

### 12.2 Interventional treatment and outcomes
In case-based reports, posterior MI due to LCx occlusion was treated with PCI and associated with rapid ECG improvement. (moskovitz2025aninterestingcase pages 3-3)

### 12.3 Suggested MAXO mappings (examples)
- Percutaneous coronary intervention (PCI)
- Coronary angiography
- Electrocardiography with posterior leads

(These ontology suggestions are not explicitly mapped in the retrieved sources.)

---

## 13. Prevention

Primary and secondary prevention strategies for atherosclerotic MI are not quantified in the retrieved excerpts; however, the etiologic risk factors enumerated (LDL-C, smoking, hypertension, diabetes, CKD, obesity/FH) imply standard prevention targets in clinical practice. Quantified preventive effect sizes and guideline thresholds were not present in the retrieved evidence and therefore are not asserted here. (młynarska2024fromatheroscleroticplaque pages 1-3)

---

## 14. Other species / natural disease
No comparative veterinary or cross-species posterior MI information was found in retrieved sources. (młynarska2024fromatheroscleroticplaque pages 1-3)

---

## 15. Model organisms
No posterior MI-specific model organism evidence was found in retrieved sources. (młynarska2024fromatheroscleroticplaque pages 1-3)

---

## Recent developments and “latest research” highlights (2023–2024 prioritized)
1. **Posterior lead thresholding and under-recognition:** A 2024 clinical letter reiterates that standard 12-lead ECG may miss posterior MI and highlights posterior leads (V7–V9) with STE ≥0.5 mm as confirmatory. Publication date: Apr 2024. URL: https://doi.org/10.24875/acme.m24000477. (garciaarias2024isolatedposterioracute pages 1-3)
2. **Synthesized posterior leads and workflow:** A 2024 Sensors review summarizes synthesized 18-lead ECG that computationally reconstructs V7–V9 and can reduce missed posterior ACS without the time/positioning burden of true 18-lead acquisition. Publication date: Sep 2024. URL: https://doi.org/10.3390/s24185947. (yamamoto2024clinicalutilityof pages 1-3, yamamoto2024clinicalutilityof pages 3-4)
3. **OMI/NOMI reclassification and reperfusion delay:** A 2024 OMI/NOMI paper reports that 40% of OMI did not meet STEMI criteria and STEMI(-)OMI patients experienced major PCI delays. Publication date: Sep 2024. URL: https://doi.org/10.3390/jcm13175201. (kola2024ominomitimefor pages 2-4)
4. **AI ECG detection of occlusive infarction:** A 2024 European Heart Journal–Digital Health study reported AI detection of OMI with AUC 0.938 and sensitivity 80.6% vs STEMI sensitivity 32.5%, supporting real-world ACS triage applications. Publication date: Nov 2024 (online publish-ahead-of-print noted 28 Nov 2023 in the excerpt). URL: https://doi.org/10.1093/ehjdh/ztad074. (herman2024internationalevaluationof pages 1-2)
5. **Outcomes of “hidden” occlusions in NSTE-ACS:** A 2023 prospective cohort found LCx occlusion in NSTE-ACS is associated with higher 1-year MACE (HR 1.68). Publication date: May 2023. URL: https://doi.org/10.1093/ehjqcco/qcad027. (bruno2023occlusionofthe pages 2-3)

---

## Evidence and citation notes (important limitations)
- **PMIDs:** The retrieved full-text excerpts generally did **not** include PubMed IDs; therefore, PMID-preferred citation formatting cannot be fully satisfied from the current tool-retrieved context.
- **Ontology IDs (MONDO/MeSH/Orphanet/OMIM):** Not present in retrieved evidence for posterior MI specifically.
- **Treatment/prevention effect sizes:** Not available in retrieved excerpts; the report avoids asserting un-cited guideline classes/doses.

---

## Appendix: Visual evidence (posterior lead placement)
The extracted image demonstrates posterior electrode placement for V7, V8, and V9 on the left posterior thorax, supporting practical implementation of posterior lead acquisition protocols. (yamamoto2024clinicalutilityof media 15a08389)

References

1. (garciaarias2024isolatedposterioracute pages 1-3): Mario R. García-Arias, Cesar Y. Salinas-Ulloa, Luis R. Maravilla-Jiménez, and Raúl Pinales-Salas. Isolated posterior acute myocardial infarction: the responsible for subtle changes in the electrocardiogram. Archivos de cardiolog�a de M�xico (English ed. Internet), Apr 2024. URL: https://doi.org/10.24875/acme.m24000477, doi:10.24875/acme.m24000477. This article has 2 citations.

2. (moskovitz2025aninterestingcase pages 2-3): K Moskovitz, V Saggar, and JA Giordano. An interesting case of an isolated posterior mi from both complete right coronary and left circumflex artery occlusions. Annals of Cardiology, Jul 2025. URL: https://doi.org/10.52768/anncardiology/1009, doi:10.52768/anncardiology/1009. This article has 0 citations.

3. (kola2024ominomitimefor pages 2-4): Martiola Kola, Naltin Shuka, Harvey Pendell Meyers, Elizana Zaimi (Petrela), and Stephen W. Smith. Omi/nomi: time for a new classification of acute myocardial infarction. Journal of Clinical Medicine, Sep 2024. URL: https://doi.org/10.3390/jcm13175201, doi:10.3390/jcm13175201. This article has 20 citations.

4. (herman2024internationalevaluationof pages 1-2): Robert Herman, Harvey Pendell Meyers, Stephen W Smith, Dario T Bertolone, Attilio Leone, Konstantinos Bermpeis, Michele M Viscusi, Marta Belmonte, Anthony Demolder, Vladimir Boza, Boris Vavrik, Viera Kresnakova, Andrej Iring, Michal Martonak, Jakub Bahyl, Timea Kisova, Dan Schelfaut, Marc Vanderheyden, Leor Perl, Emre K Aslanger, Robert Hatala, Wojtek Wojakowski, Jozef Bartunek, and Emanuele Barbato. International evaluation of an artificial intelligence–powered electrocardiogram model detecting acute coronary occlusion myocardial infarction. European Heart Journal. Digital Health, 5:123-133, Nov 2024. URL: https://doi.org/10.1093/ehjdh/ztad074, doi:10.1093/ehjdh/ztad074. This article has 155 citations.

5. (kwok2024structuralcomplicationsfollowing pages 2-4): Chun Shing Kwok, Adnan I. Qureshi, Maximillian Will, Konstantin Schwarz, Gregory Y. H. Lip, and Josip A. Borovac. Structural complications following st-elevation myocardial infarction: an analysis of the national inpatient sample 2016 to 2020. Journal of Cardiovascular Development and Disease, 11:59, Feb 2024. URL: https://doi.org/10.3390/jcdd11020059, doi:10.3390/jcdd11020059. This article has 4 citations.

6. (alsagaff2022isolatedposteriorstelevation pages 8-8): Mochamad Yusuf Alsagaff, Rizki Amalia, Budi Baktijasa Dharmadjati, and Yolande Appelman. Isolated posterior st-elevation myocardial infarction: the necessity of routine 15-lead electrocardiography: a case series. Journal of Medical Case Reports, Aug 2022. URL: https://doi.org/10.1186/s13256-022-03570-w, doi:10.1186/s13256-022-03570-w. This article has 14 citations and is from a peer-reviewed journal.

7. (młynarska2024fromatheroscleroticplaque pages 1-3): Ewelina Młynarska, Witold Czarnik, Piotr Fularski, Joanna Hajdys, Gabriela Majchrowicz, Magdalena Stabrawa, Jacek Rysz, and Beata Franczyk. From atherosclerotic plaque to myocardial infarction—the leading cause of coronary artery occlusion. International Journal of Molecular Sciences, 25:7295, Jul 2024. URL: https://doi.org/10.3390/ijms25137295, doi:10.3390/ijms25137295. This article has 125 citations.

8. (młynarska2024fromatheroscleroticplaque pages 4-6): Ewelina Młynarska, Witold Czarnik, Piotr Fularski, Joanna Hajdys, Gabriela Majchrowicz, Magdalena Stabrawa, Jacek Rysz, and Beata Franczyk. From atherosclerotic plaque to myocardial infarction—the leading cause of coronary artery occlusion. International Journal of Molecular Sciences, 25:7295, Jul 2024. URL: https://doi.org/10.3390/ijms25137295, doi:10.3390/ijms25137295. This article has 125 citations.

9. (bruno2023occlusionofthe pages 2-3): Francesco Bruno, Boris Adjibodou, Slayman Obeid, Simon C Kraler, Florian A Wenzl, M Majid Akhtar, Andrea Denegri, Marco Roffi, Olivier Muller, Arnold von Eckardstein, Lorenz Räber, Christian Templin, and Thomas F Lüscher. Occlusion of the infarct-related coronary artery presenting as acute coronary syndrome with and without st-elevation: impact of inflammation and outcomes in a real-world prospective cohort. European Heart Journal - Quality of Care and Clinical Outcomes, 9:564-574, May 2023. URL: https://doi.org/10.1093/ehjqcco/qcad027, doi:10.1093/ehjqcco/qcad027. This article has 19 citations.

10. (młynarska2024fromatheroscleroticplaque pages 3-4): Ewelina Młynarska, Witold Czarnik, Piotr Fularski, Joanna Hajdys, Gabriela Majchrowicz, Magdalena Stabrawa, Jacek Rysz, and Beata Franczyk. From atherosclerotic plaque to myocardial infarction—the leading cause of coronary artery occlusion. International Journal of Molecular Sciences, 25:7295, Jul 2024. URL: https://doi.org/10.3390/ijms25137295, doi:10.3390/ijms25137295. This article has 125 citations.

11. (herman2024internationalevaluationof pages 7-8): Robert Herman, Harvey Pendell Meyers, Stephen W Smith, Dario T Bertolone, Attilio Leone, Konstantinos Bermpeis, Michele M Viscusi, Marta Belmonte, Anthony Demolder, Vladimir Boza, Boris Vavrik, Viera Kresnakova, Andrej Iring, Michal Martonak, Jakub Bahyl, Timea Kisova, Dan Schelfaut, Marc Vanderheyden, Leor Perl, Emre K Aslanger, Robert Hatala, Wojtek Wojakowski, Jozef Bartunek, and Emanuele Barbato. International evaluation of an artificial intelligence–powered electrocardiogram model detecting acute coronary occlusion myocardial infarction. European Heart Journal. Digital Health, 5:123-133, Nov 2024. URL: https://doi.org/10.1093/ehjdh/ztad074, doi:10.1093/ehjdh/ztad074. This article has 155 citations.

12. (młynarska2024fromatheroscleroticplaque pages 17-19): Ewelina Młynarska, Witold Czarnik, Piotr Fularski, Joanna Hajdys, Gabriela Majchrowicz, Magdalena Stabrawa, Jacek Rysz, and Beata Franczyk. From atherosclerotic plaque to myocardial infarction—the leading cause of coronary artery occlusion. International Journal of Molecular Sciences, 25:7295, Jul 2024. URL: https://doi.org/10.3390/ijms25137295, doi:10.3390/ijms25137295. This article has 125 citations.

13. (meyers2021ischemicst‐segmentdepression pages 13-14): H. Pendell Meyers, Alexander Bracey, Daniel Lee, Andrew Lichtenheld, Wei J. Li, Daniel D. Singer, Zach Rollins, Jesse A. Kane, Kenneth W. Dodd, Kristen E. Meyers, Gautam R. Shroff, Adam J. Singer, and Stephen W. Smith. Ischemic st‐segment depression maximal in v1–v4 (versus v5–v6) of any amplitude is specific for occlusion myocardial infarction (versus nonocclusive ischemia). Journal of the American Heart Association, Dec 2021. URL: https://doi.org/10.1161/jaha.121.022866, doi:10.1161/jaha.121.022866. This article has 55 citations.

14. (ramjaun2021ecgchangesin pages 3-4): Aliya Ramjaun, Ankit Garg, Marlee Klaiman, Matthew Sibbald, and Junghwan (Kevin) Dong. Ecg changes in a case of posterior myocardial infarction in the presence of right bundle branch block. Cureus, Feb 2021. URL: https://doi.org/10.7759/cureus.13281, doi:10.7759/cureus.13281. This article has 2 citations.

15. (yamamoto2024clinicalutilityof pages 1-3): Tetsushi Yamamoto, Hiroyuki Awano, Shuichiro Ogawa, and Masafumi Matsuo. Clinical utility of synthesized 18-lead electrocardiography. Sensors, 24:5947, Sep 2024. URL: https://doi.org/10.3390/s24185947, doi:10.3390/s24185947. This article has 1 citations and is from a peer-reviewed journal.

16. (yamamoto2024clinicalutilityof pages 3-4): Tetsushi Yamamoto, Hiroyuki Awano, Shuichiro Ogawa, and Masafumi Matsuo. Clinical utility of synthesized 18-lead electrocardiography. Sensors, 24:5947, Sep 2024. URL: https://doi.org/10.3390/s24185947, doi:10.3390/s24185947. This article has 1 citations and is from a peer-reviewed journal.

17. (yamamoto2024clinicalutilityof media 15a08389): Tetsushi Yamamoto, Hiroyuki Awano, Shuichiro Ogawa, and Masafumi Matsuo. Clinical utility of synthesized 18-lead electrocardiography. Sensors, 24:5947, Sep 2024. URL: https://doi.org/10.3390/s24185947, doi:10.3390/s24185947. This article has 1 citations and is from a peer-reviewed journal.

18. (moskovitz2025aninterestingcase pages 3-3): K Moskovitz, V Saggar, and JA Giordano. An interesting case of an isolated posterior mi from both complete right coronary and left circumflex artery occlusions. Annals of Cardiology, Jul 2025. URL: https://doi.org/10.52768/anncardiology/1009, doi:10.52768/anncardiology/1009. This article has 0 citations.

19. (herman2024internationalevaluationof pages 2-3): Robert Herman, Harvey Pendell Meyers, Stephen W Smith, Dario T Bertolone, Attilio Leone, Konstantinos Bermpeis, Michele M Viscusi, Marta Belmonte, Anthony Demolder, Vladimir Boza, Boris Vavrik, Viera Kresnakova, Andrej Iring, Michal Martonak, Jakub Bahyl, Timea Kisova, Dan Schelfaut, Marc Vanderheyden, Leor Perl, Emre K Aslanger, Robert Hatala, Wojtek Wojakowski, Jozef Bartunek, and Emanuele Barbato. International evaluation of an artificial intelligence–powered electrocardiogram model detecting acute coronary occlusion myocardial infarction. European Heart Journal. Digital Health, 5:123-133, Nov 2024. URL: https://doi.org/10.1093/ehjdh/ztad074, doi:10.1093/ehjdh/ztad074. This article has 155 citations.