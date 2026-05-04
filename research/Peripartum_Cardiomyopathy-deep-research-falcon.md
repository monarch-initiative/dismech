---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-04T12:32:15.167005'
end_time: '2026-05-04T12:49:31.719401'
duration_seconds: 1036.55
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Peripartum Cardiomyopathy
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Peripartum Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Peripartum Cardiomyopathy** covering all of the
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
- **Disease Name:** Peripartum Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Peripartum Cardiomyopathy** covering all of the
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


## Comprehensive Disease Characteristics Report: Peripartum Cardiomyopathy (PPCM)

### Executive summary
Peripartum cardiomyopathy (PPCM) is an idiopathic cardiomyopathy presenting as new-onset heart failure (HF) with left-ventricular (LV) systolic dysfunction, typically in late pregnancy or in the months postpartum, and is defined in most contemporary sources by LVEF <45% after exclusion of alternative causes. Incidence varies markedly by geography (from ~1:300 in Haiti to ~1:20,000 in Japan), with strong associations with hypertensive disorders of pregnancy and ancestry-associated disparities. A leading contemporary mechanistic framework is a “two-hit” vasculo-hormonal/angiogenic model implicating oxidative stress–dependent cleavage of prolactin to a pathogenic 16-kDa fragment and placental anti-angiogenic signaling (sFlt-1) with reduced VEGF/PGC-1α signaling. Clinical management largely follows guideline-directed HFrEF therapy tailored to pregnancy/lactation, with bromocriptine as the most widely discussed disease-targeted therapy (evidence suggests improved LVEF and higher odds of recovery but uncertain mortality benefit). Major knowledge gaps remain in standardized biomarker validation, high-quality randomized trials, and comprehensive genetics and epidemiology in diverse populations. (sigauke2024peripartumcardiomyopathya pages 1-2, sigauke2024peripartumcardiomyopathya pages 5-7, iannaccone2024diagnosisandmanagement pages 1-2, kumar2023prolactininhibitionin pages 4-6)

---

## 1. Disease information

### 1.1 What is PPCM?
**Definition (current understanding):** PPCM is an idiopathic cardiomyopathy characterized by de novo HF due to new LV systolic dysfunction occurring toward the end of pregnancy or in the months after delivery, typically defined by **LVEF <45%**, after excluding other causes of cardiomyopathy and HF. (iannaccone2024diagnosisandmanagement pages 1-2, sigauke2024peripartumcardiomyopathya pages 1-2, sigauke2024peripartumcardiomyopathya pages 2-4)

**Common diagnostic criteria referenced in contemporary reviews:**
- **NHLBI (2000) criteria** include (i) HF in last month of pregnancy or within 5 months postpartum, (ii) no identifiable cause, (iii) no recognizable heart disease before last pregnancy month, and (iv) echo evidence of LV dysfunction: **LVEF <45%**, **fractional shortening <30%**, and/or **LVEDD >2.7 cm/m²**. (sigauke2024peripartumcardiomyopathya pages 1-2)
- **ESC simplified definition (used clinically)**: idiopathic cardiomyopathy with HF from LV systolic dysfunction toward the end of pregnancy or months postpartum, typically **LVEF <45%**. (sigauke2024peripartumcardiomyopathya pages 2-4)

**Synonyms/alternate names (used in literature):** peripartum cardiomyopathy, postpartum cardiomyopathy, pregnancy-associated cardiomyopathy (overlapping usage in reviews; operationally PPCM is the dominant term). (sigauke2024peripartumcardiomyopathya pages 1-2, sigauke2024peripartumcardiomyopathya pages 2-4)

### 1.2 Key identifiers (ICD/MeSH/MONDO/Orphanet/OMIM)
The retrieved primary/review texts did **not** contain explicit ICD-10/ICD-11, MeSH, MONDO, Orphanet, or OMIM identifiers in the extracted sections; therefore these identifiers cannot be reliably reported from the present evidence set. (sigauke2024peripartumcardiomyopathya pages 1-2, iannaccone2024diagnosisandmanagement pages 1-2)

### 1.3 Evidence source type
The information synthesized here is derived from **aggregated disease-level resources** (peer-reviewed narrative reviews, systematic reviews/meta-analyses, and registry/trial summaries) and one **retrospective cohort study**. (sigauke2024peripartumcardiomyopathya pages 1-2, iannaccone2024diagnosisandmanagement pages 1-2, noll2024breastfeedinginpatients pages 1-2, kumar2023prolactininhibitionin pages 4-6)

---

## 2. Etiology

### 2.1 Disease causal factors (multifactorial “two-hit” model)
Contemporary sources emphasize that PPCM is **multifactorial**. A widely discussed mechanistic framework is a **vasculo-hormonal/angiogenic “two-hit” model** in which pregnancy-related hormonal/vascular stress triggers HF in susceptible individuals (including genetic susceptibility). (sigauke2024peripartumcardiomyopathya pages 2-4, sigauke2024peripartumcardiomyopathya pages 5-7, sigauke2024peripartumcardiomyopathya pages 4-5)

### 2.2 Risk factors (with quantified estimates where available)
Quantified and repeatedly cited risks include:
- **African American/Black ancestry:** “African Americans are **3–16 times** more likely to develop the disease in comparison to white women.” (Iannaccone 2024; publication date Sep 2024; DOI URL: https://doi.org/10.1016/j.ijcchd.2024.100530) (iannaccone2024diagnosisandmanagement pages 1-2). Another review excerpt reports ~**4×** higher frequency among African-American women. (laskowska2026peripartumcardiomyopathy–whatisa pages 3-5)
- **Hypertensive disorders of pregnancy:** gestational hypertension or pre-eclampsia associated with **~3-fold increased risk**. (iannaccone2024diagnosisandmanagement pages 1-2)
- **Advanced maternal age:** one cited estimate reports **10-fold higher risk** for women **>40** vs **<20** years. (iannaccone2024diagnosisandmanagement pages 1-2)
- **Multiple gestation:** present in **7–14.5%** of cases in reported series. (iannaccone2024diagnosisandmanagement pages 1-2)

Additional commonly cited risk factors (often reported qualitatively or without pooled effect size in the retrieved excerpts) include: multiparity, family history, infertility treatment, anemia/malnutrition, obesity/diabetes, smoking/alcohol/drug use, low BMI, selenium deficiency, and prolonged beta-agonist tocolysis. (sigauke2024peripartumcardiomyopathya pages 4-5, iannaccone2024diagnosisandmanagement pages 1-2)

### 2.3 Protective factors
Protective genetic or environmental factors were not identified with quantifiable effect sizes in the retrieved evidence excerpts. (sigauke2024peripartumcardiomyopathya pages 1-2, iannaccone2024diagnosisandmanagement pages 1-2)

### 2.4 Gene–environment interaction
A specific conceptual gene–environment interaction described is that pregnancy-associated vascular/hormonal stress can unmask disease in **genotype-positive/phenotype-negative** women (a “two-hit” hypothesis). The comprehensive review notes that **>90% of variant carriers do not develop PPCM**, supporting the need for additional triggers beyond genotype alone. (sigauke2024peripartumcardiomyopathya pages 5-7)

---

## 3. Phenotypes

### 3.1 Clinical phenotypes (symptoms/signs)
**Typical HF presentation:** fatigue, dyspnea, orthopnea, and congestion/peripheral edema, which may be mistaken for physiologic pregnancy changes—necessitating high suspicion. (yusuf2025advancingourunderstanding pages 1-2, sigauke2024peripartumcardiomyopathya pages 7-8)

**Electrocardiographic phenotype:** ECG abnormalities are common (>90% in the cited review), including sinus tachycardia, LBBB, atrial fibrillation, T-wave inversion, and prolonged QTc. (sigauke2024peripartumcardiomyopathya pages 5-7)

**Time of onset:** most cases are postpartum: ~**75%** in the first month postpartum and ~**45%** in the first week. (sigauke2024peripartumcardiomyopathya pages 2-4)

### 3.2 Phenotype characteristics and frequencies
- **Onset window:** classic definition is last pregnancy month to 5 months postpartum, but broader/time-independent definitions exist. (iannaccone2024diagnosisandmanagement pages 1-2, sigauke2024peripartumcardiomyopathya pages 1-2)
- **Severity/progression:** ranges from mild HF to cardiogenic shock; severe cases can require mechanical circulatory support. (laskowska2026peripartumcardiomyopathycurrent pages 19-20, iannaccone2024diagnosisandmanagement pages 4-5)

### 3.3 Quality of life impact
Quality-of-life (QoL) burden is implicit through HF symptoms and hospitalization risk; specific instrumented QoL statistics were not extracted from the retrieved snippets (though QoL endpoints appear in trial designs). (NCT02590601 chunk 1)

### 3.4 Suggested HPO terms (examples)
A structured list of phenotype ontology suggestions is provided in the ontology artifact. (artifact-01)

---

## 4. Genetic / molecular information

### 4.1 Causal/susceptibility genes and estimated contribution
Genetic predisposition is increasingly recognized; a comprehensive 2024 review states that **genetics may explain up to ~15%** of PPCM cases, with **TTN truncating variants** a predominant contributor; other implicated genes include **MYH**, **MYBPC3**, **LMNA**, and **SCN5A**. (Sigauke 2024; Sep 2024; https://doi.org/10.1007/s10741-024-10435-5) (sigauke2024peripartumcardiomyopathya pages 5-7)

### 4.2 Variant types and functional consequences
The retrieved evidence specifically highlights **TTN truncating variants** as predominant. Detailed PPCM-specific variant nomenclature, allele frequencies (gnomAD), and functional validation results were not present in the extracted PPCM evidence snippets. (sigauke2024peripartumcardiomyopathya pages 5-7)

### 4.3 Modifier genes / epigenetics / chromosomal abnormalities
These were not described with specific loci or validated epigenetic signatures in the extracted evidence. (sigauke2024peripartumcardiomyopathya pages 1-2, sigauke2024peripartumcardiomyopathya pages 5-7)

---

## 5. Environmental information
Environmental/lifestyle contributors are reported largely as risk factor associations (smoking, alcohol/drug use, malnutrition, selenium deficiency, low BMI). Specific toxicant/pathogen triggers were not supported with direct evidence in the extracted texts. (sigauke2024peripartumcardiomyopathya pages 4-5, iannaccone2024diagnosisandmanagement pages 1-2)

---

## 6. Mechanism / pathophysiology

### 6.1 Core mechanistic framework (causal chain)
A leading contemporary mechanism is a **vasculo-hormonal/angiogenic two-hit model**:
1) **Oxidative stress/STAT3 axis:** STAT3-dependent reduction in MnSOD leads to increased ROS, activation of **cathepsin D**, and cleavage of 23-kDa prolactin into a **pathogenic 16-kDa fragment (vasoinhibin)**. This fragment promotes endothelial injury and downstream cardiomyocyte dysfunction, with an emphasized role for **NF-κB** and **endothelial microRNA-146a**. (sigauke2024peripartumcardiomyopathya pages 2-4, sigauke2024peripartumcardiomyopathya pages 4-5)
2) **Placental angiogenic imbalance:** elevation of anti-angiogenic **sFlt-1** with reduced **VEGF** and suppressed **PGC-1α** signaling contributes to impaired angiogenesis/endothelial dysfunction and myocardial injury. sFlt-1 is linked to more severe disease and worse prognosis. (sigauke2024peripartumcardiomyopathya pages 2-4, sigauke2024peripartumcardiomyopathya pages 4-5)

Additional mechanistic themes include inflammation/autoimmunity, altered pregnancy hemodynamics (volume overload), metabolic changes, and other hormonal mediators (e.g., decreased relaxin-2; activin A as an emerging biomarker). (sigauke2024peripartumcardiomyopathya pages 4-5)

### 6.2 Suggested GO terms / CL terms / UBERON structures
Suggested ontology mapping across phenotypes, biological processes, cell types, and anatomical structures is provided in **artifact-01**. (artifact-01)

---

## 7. Anatomical structures affected

### 7.1 Primary organ/system involvement
Primary pathology involves the **heart**, particularly the **left ventricle** and myocardium, with vascular/endothelial involvement as a central mechanistic node. (iannaccone2024diagnosisandmanagement pages 1-2, sigauke2024peripartumcardiomyopathya pages 2-4, sigauke2024peripartumcardiomyopathya pages 7-8)

### 7.2 Pregnancy-associated structure
The **placenta** is implicated in pathophysiology via anti-angiogenic signaling (e.g., sFlt-1). (sigauke2024peripartumcardiomyopathya pages 2-4, iannaccone2024diagnosisandmanagement pages 1-2)

Ontology suggestions for UBERON structures are listed in artifact-01. (artifact-01)

---

## 8. Temporal development

### 8.1 Onset
Classic onset window is last pregnancy month through 5 months postpartum (NHLBI criterion), but more recent discussions broaden timing and may consider earlier or later presentations. (sigauke2024peripartumcardiomyopathya pages 1-2, iannaccone2024diagnosisandmanagement pages 1-2)

### 8.2 Progression and recovery
A 2024 review reports that recovery of LVEF occurs in **most patients (~76%)**, usually within **6 months**. (iannaccone2024diagnosisandmanagement pages 4-5)

---

## 9. Inheritance and population

### 9.1 Epidemiology
Incidence varies markedly by region and ancestry:
- Global incidence is commonly cited around **~1 per 2,000 deliveries**, but can be **~1:300 in Haiti** and **~1:20,000 in Japan**; very high rates have been reported in parts of Nigeria (e.g., **~1:100** in Kano). (sigauke2024peripartumcardiomyopathya pages 1-2, iannaccone2024diagnosisandmanagement pages 1-2)
- South African cohorts report **~1:1,000** and **~1:3,000** live births. (sigauke2024peripartumcardiomyopathya pages 2-4)

### 9.2 Demographic disparities
- African American race has substantially higher risk (3–16× versus White women), and recovery rates may be lower in Afro-American women (~45% recovery in a cited estimate). (iannaccone2024diagnosisandmanagement pages 1-2, iannaccone2024diagnosisandmanagement pages 4-5)

### 9.3 Inheritance pattern
PPCM likely spans a spectrum from sporadic to familial susceptibility overlapping with dilated cardiomyopathy genetics; explicit Mendelian inheritance patterns for PPCM per se were not provided in the extracted evidence. (sigauke2024peripartumcardiomyopathya pages 5-7)

---

## 10. Diagnostics

### 10.1 Core diagnostic workflow (real-world)
- **Echocardiography** is the preferred initial imaging modality (safe and widely available in pregnancy/lactation) and is central to diagnosis, risk stratification, and follow-up. (sigauke2024peripartumcardiomyopathya pages 7-8)
- **Natriuretic peptides** are key adjunct diagnostics with strong negative predictive value for HF: BNP <100 pg/mL, NT-proBNP <300 pg/mL, MR-proANP <120 pmol/L (as thresholds with high negative predictive value in a cited review). (sigauke2024peripartumcardiomyopathya pages 5-7)
- **ECG** abnormalities are common and can provide prognostic signals (e.g., sinus tachycardia and prolonged QTc associated with worse prognosis in the cited review). (sigauke2024peripartumcardiomyopathya pages 5-7, sigauke2024peripartumcardiomyopathya pages 7-8)

### 10.2 Biomarkers (investigational)
Multiple candidate biomarkers remain under study (microRNA-146a, cathepsin D, 16-kDa prolactin fragment, interferon-γ, ADMA, sFlt-1, sST2, Gal-3, GDF-15, adrenomedullin, long noncoding RNAs, heat shock proteins), but diagnostic thresholds and clinical specificity are not established in the extracted evidence. (sigauke2024peripartumcardiomyopathya pages 5-7, sigauke2024peripartumcardiomyopathya pages 7-8)

### 10.3 Prognostic biomarker statistic
In one cohort cited by the comprehensive review, **NT-proBNP >900 pg/mL at diagnosis predicted poor LV recovery**. (sigauke2024peripartumcardiomyopathya pages 5-7)

---

## 11. Outcome / prognosis

### 11.1 Maternal outcomes
PPCM has substantial morbidity and mortality.
- Mortality estimates in the comprehensive review include **reported mortality 7–15%**. (sigauke2024peripartumcardiomyopathya pages 1-2)
- Severe disease can require mechanical circulatory support and transplant consideration; LV/BiVAD required in **up to 7%** (per 2024 management review excerpt). (iannaccone2024diagnosisandmanagement pages 4-5)

### 11.2 Subsequent pregnancy outcomes (2024 meta-analysis)
A 2024 systematic review/meta-analysis of subsequent pregnancy (SSP) reported:
- Total **487** subsequent pregnancies. (wijayanto2024outcomesofsubsequent pages 1-1)
- Mortality in SSP ranged from **0% to 55.5%** across studies. (wijayanto2024outcomesofsubsequent pages 1-1, wijayanto2024outcomesofsubsequent pages 3-4)
- Persistent LV dysfunction was associated with increased mortality (**OR 13.17; 95% CI 1.54–112.28; p=0.02**) and lower LVEF (**MD −12.88; 95% CI −21.67 to −4.09; p=0.004**). (Wijayanto 2024; Apr 2024; https://doi.org/10.1136/openhrt-2024-002626) (wijayanto2024outcomesofsubsequent pages 1-1)

### 11.3 Prognostic factors
The extracted evidence emphasizes pre-pregnancy/presentation **LVEF** as a major determinant of outcomes and relapse risk (including in subsequent pregnancies). (laskowska2026peripartumcardiomyopathy–whatisa pages 16-17, iannaccone2024diagnosisandmanagement pages 4-5, wijayanto2024outcomesofsubsequent pages 1-1)

---

## 12. Treatment

### 12.1 Guideline-directed HF therapy (application in practice)
Treatment largely follows HFrEF guidelines, modified for pregnancy and lactation safety. Pregnancy/postpartum medication selection is commonly presented as an algorithm (see Figure in the 2024 comprehensive review). (iannaccone2024diagnosisandmanagement pages 4-5, sigauke2024peripartumcardiomyopathya media 4d9eef0c)

### 12.2 Bromocriptine / prolactin inhibition (evidence and interpretation)
**Evidence base (2023 meta-analysis):** A systematic review/meta-analysis (10 studies; 749 patients; including RCTs and cohorts) found bromocriptine plus GDMT was associated with improved LVEF and higher odds of recovery:
- Follow-up LVEF higher with bromocriptine: pooled mean difference **12.56%** (cohorts; 95% CI 5.84–19.28) and **14.25%** (RCTs; 95% CI 0.61–27.89). (kumar2023prolactininhibitionin pages 4-6)
- Higher odds of LV recovery: pooled OR **3.55** (95% CI 1.39–9.10). (kumar2023prolactininhibitionin pages 4-6)
- No statistically significant mortality reduction in pooled analyses (e.g., RCT pRR 0.53, 95% CI 0.26–1.07). (kumar2023prolactininhibitionin pages 4-6)

**Clinical implementation details (review-level guidance):** Bromocriptine 2.5 mg twice daily is suggested for 8 weeks in moderate/severe PPCM and for 1 week in mild cases; due to prothrombotic concerns, at least prophylactic anticoagulation is advised when bromocriptine is used. (iannaccone2024diagnosisandmanagement pages 4-5)

### 12.3 Anticoagulation
Guidelines summarized in a 2024 management review recommend anticoagulation in severe LV dysfunction (Europe: LVEF <35%; US: LVEF <30%). LMWH is preferred during pregnancy; both LMWH and warfarin may be used during lactation in appropriate contexts; DOACs are contraindicated in pregnancy and breastfeeding. (iannaccone2024diagnosisandmanagement pages 4-5)

### 12.4 Mechanical support and transplant
Severe cases may require ECMO/LVAD/BiVAD as bridge-to-recovery or transplant; the 2024 management review excerpt states LV/BiVAD may be required in up to 7%. (laskowska2026peripartumcardiomyopathycurrent pages 19-20, iannaccone2024diagnosisandmanagement pages 4-5)

### 12.5 Breastfeeding and real-world counseling
A 2024 retrospective cohort study addressing lactation outcomes found no significant association between breastfeeding and recovery:
- Quote (abstract): “**Of 220 patients with confirmed PPCM, lactation status was known definitively in 54 patients; of these, 18 (33%) had breastfed for at least 6 weeks and 36 (67%) did not breastfeed.**” (Noll 2024; Oct 2024; https://doi.org/10.1186/s13006-024-00673-6) (noll2024breastfeedinginpatients pages 1-2)
- Quote (abstract): “**In this retrospective cohort, lactation was not associated with lower rates of myocardial recovery.**” (noll2024breastfeedinginpatients pages 1-2)
- Counseling gap (abstract): “**Of the 34 survey respondents, 62% were told not to breastfeed… and none were encouraged to breastfeed.**” (noll2024breastfeedinginpatients pages 1-2)

### 12.6 MAXO term suggestions
Intervention ontology suggestions (e.g., bromocriptine therapy, anticoagulation, beta-blocker therapy, ACE inhibitor postpartum, diuretic therapy, mechanical circulatory support) are listed in artifact-01. (artifact-01)

---

## 13. Prevention
No validated primary prevention intervention is established in the extracted evidence set; prevention is largely risk-factor recognition (e.g., hypertensive disorders) and early detection in symptomatic patients. (iannaccone2024diagnosisandmanagement pages 1-2, sigauke2024peripartumcardiomyopathya pages 7-8)

---

## 14. Other species / natural disease
No naturally occurring non-human species disease analogs were identified in the extracted evidence set. (sigauke2024peripartumcardiomyopathya pages 1-2)

---

## 15. Model organisms
Mechanistic support for the STAT3/oxidative stress/prolactin model is described in relation to STAT3 knock-out mouse models in the 2024 comprehensive review excerpt, but detailed model descriptions (strain, phenotype penetrance) were not extracted in the provided snippets. (sigauke2024peripartumcardiomyopathya pages 2-4)

---

## Recent developments and latest research (2023–2024 prioritized)

1) **Broader biomarker landscape and diagnostic thresholds:** The 2024 comprehensive review highlights natriuretic peptide thresholds for high negative predictive value (BNP <100 pg/mL; NT-proBNP <300 pg/mL; MR-proANP <120 pmol/L) and reports **NT-proBNP >900 pg/mL** as a predictor of poor LV recovery in one cohort, while cataloging emerging molecular markers (miR-146a, sFlt-1, sST2, Gal-3, GDF-15, etc.). (sigauke2024peripartumcardiomyopathya pages 5-7)

2) **Genetics as an enabling direction for risk prediction:** The same 2024 review emphasizes that genetics may explain **up to ~15%** of PPCM and highlights TTN truncating variants with overlap to dilated cardiomyopathy genes, reinforcing the two-hit pregnancy-trigger model. (sigauke2024peripartumcardiomyopathya pages 5-7)

3) **Bromocriptine evidence synthesis:** A 2023 systematic review/meta-analysis found improved LVEF and higher odds of recovery with bromocriptine but no clear mortality benefit, highlighting ongoing uncertainty and the need for adequately powered trials. (kumar2023prolactininhibitionin pages 4-6)

4) **Breastfeeding outcomes and counseling (real-world implementation):** 2024 retrospective data suggest lactation is not associated with worse recovery, while documenting a high rate of discouraging counseling (62% told not to breastfeed). (noll2024breastfeedinginpatients pages 1-2)

5) **Subsequent pregnancy outcomes quantified (2024):** persistent LV dysfunction substantially elevates mortality odds in subsequent pregnancy (OR 13.17). (wijayanto2024outcomesofsubsequent pages 1-1)

---

## Current applications and real-world implementations

### Clinical management algorithms
The 2024 comprehensive review includes a pharmacologic management algorithm (Figure 3) that distinguishes therapy during pregnancy versus postpartum and includes modern HFrEF classes and bromocriptine considerations. (sigauke2024peripartumcardiomyopathya media 4d9eef0c)

### Anticoagulation in practice
Anticoagulation thresholds based on LVEF (<35% Europe; <30% US) and contraindications to DOACs in pregnancy/breastfeeding reflect real-world implementation constraints. (iannaccone2024diagnosisandmanagement pages 4-5)

---

## Expert opinions / authoritative analysis (from reviews)
- Reviews emphasize PPCM remains challenging to diagnose because symptoms overlap with normal pregnancy changes, requiring high clinical suspicion and systematic evaluation (echo, ECG, biomarkers). (sigauke2024peripartumcardiomyopathya pages 7-8, sigauke2024peripartumcardiomyopathya pages 5-7)
- Bromocriptine is frequently described as the **only targeted drug** but with insufficient high-quality evidence for universal recommendation; authors note need for better randomized data. (iannaccone2024diagnosisandmanagement pages 1-2, iannaccone2024diagnosisandmanagement pages 5-6)

---

## Relevant clinical trials (ClinicalTrials.gov)

### REBIRTH (NCT05180773) – Recruiting
- Title: Impact of Bromocriptine on Clinical Outcomes for Peripartum Cardiomyopathy
- Start date: 2022-07-27; primary completion: 2026-06-30; study completion: 2028-12-31
- Design: Phase 4, quadruple-masked, randomized placebo-controlled
- Intervention: bromocriptine for 8 weeks (2.5 mg BID ×2 weeks then 2.5 mg daily ×6 weeks) + GDMT; anticoagulation-matching includes rivaroxaban 10 mg daily for 8 weeks in those not otherwise anticoagulated
- Primary endpoint: LVEF at 6 months (echo; adjusted for baseline)
- URL: https://clinicaltrials.gov/study/NCT05180773
(NCT05180773 chunk 1)

### NCT00998556 – Completed
- Start: June 2010; primary completion March 2016; completion August 2016
- Phase 2, randomized, parallel, open-label; n=64
- Eligibility includes LV ejection fraction ≤35% within 5 months postpartum
- Primary endpoint: change in LVEF baseline to 6 months by MRI and echo
- URL: https://clinicaltrials.gov/study/NCT00998556
(NCT00998556 chunk 1)

### BRO-HF (NCT02590601) – Withdrawn
- Phase 3 Bayesian randomized registry trial; withdrawn for insufficient enrollment
- Arms: bromocriptine + GDMT vs GDMT
- Primary endpoint: 1-year MACE composite; secondary includes proportion with LVEF ≥54% at 6 months
- URL: https://clinicaltrials.gov/study/NCT02590601
(NCT02590601 chunk 1)

---

## Structured evidence tables (for knowledge-base population)

| Domain | Key finding | Quantitative detail | Source (author, year, journal) | URL/DOI |
|---|---|---|---|---|
| Definition/diagnostic criteria | PPCM is de novo/idiopathic heart failure with new LV systolic dysfunction in late pregnancy or postpartum; diagnosis is by exclusion, and LV dilation may be absent (sigauke2024peripartumcardiomyopathya pages 1-2, iannaccone2024diagnosisandmanagement pages 1-2) | LVEF <45%; older criteria also include M-mode fractional shortening <30% or LV end-diastolic dimension >2.7 cm/m² (sigauke2024peripartumcardiomyopathya pages 1-2, sigauke2024peripartumcardiomyopathya pages 2-4) | Sigauke et al., 2024, *Heart Failure Reviews*; Iannaccone et al., 2024, *Int J Cardiol Congenital Heart Disease* | https://doi.org/10.1007/s10741-024-10435-5; https://doi.org/10.1016/j.ijcchd.2024.100530 |
| Definition/timing | Classic diagnostic window is last month of pregnancy to 5 months postpartum, though broader/time-independent definitions are now discussed (sigauke2024peripartumcardiomyopathya pages 1-2, iannaccone2024diagnosisandmanagement pages 1-2) | ~19% diagnosed in final pregnancy month; ~75% within first month postpartum; ~45% within first postpartum week (sigauke2024peripartumcardiomyopathya pages 2-4) | Sigauke et al., 2024, *Heart Failure Reviews*; Iannaccone et al., 2024, *Int J Cardiol Congenital Heart Disease* | https://doi.org/10.1007/s10741-024-10435-5; https://doi.org/10.1016/j.ijcchd.2024.100530 |
| Incidence/geographic variation | Global incidence is highly variable, with major geographic and ancestry-associated differences (sigauke2024peripartumcardiomyopathya pages 1-2, iannaccone2024diagnosisandmanagement pages 1-2) | Approx. 1:2,000 globally; reported 1:300 in Haiti, 1:20,000 in Japan, ~1:4,025 in the U.S., and up to 1:100 in Kano, Nigeria (sigauke2024peripartumcardiomyopathya pages 1-2) | Sigauke et al., 2024, *Heart Failure Reviews*; Iannaccone et al., 2024, *Int J Cardiol Congenital Heart Disease* | https://doi.org/10.1007/s10741-024-10435-5; https://doi.org/10.1016/j.ijcchd.2024.100530 |
| Incidence/geographic variation | South African cohorts also illustrate substantial regional burden (sigauke2024peripartumcardiomyopathya pages 2-4) | 1:1,000 and 1:3,000 live births in South African cohorts (sigauke2024peripartumcardiomyopathya pages 2-4) | Sigauke et al., 2024, *Heart Failure Reviews* | https://doi.org/10.1007/s10741-024-10435-5 |
| Risk factors | African American/Black race is a major risk factor (iannaccone2024diagnosisandmanagement pages 1-2, laskowska2026peripartumcardiomyopathy–whatisa pages 3-5) | African Americans are 3–16 times more likely to develop PPCM than White women; PPCM is ~4× more common in African-American women in another review (iannaccone2024diagnosisandmanagement pages 1-2, laskowska2026peripartumcardiomyopathy–whatisa pages 3-5) | Iannaccone et al., 2024, *Int J Cardiol Congenital Heart Disease*; Laskowska, 2026, review excerpt | https://doi.org/10.1016/j.ijcchd.2024.100530 |
| Risk factors | Hypertensive disorders of pregnancy are strongly associated with PPCM (iannaccone2024diagnosisandmanagement pages 1-2, sigauke2024peripartumcardiomyopathya pages 4-5) | Gestational hypertension/preeclampsia associated with ~3-fold increased risk; in one meta-analysis cited by Iannaccone et al., preeclampsia was present in 22% and hypertensive disorders in 97% of cases (iannaccone2024diagnosisandmanagement pages 1-2) | Iannaccone et al., 2024, *Int J Cardiol Congenital Heart Disease*; Sigauke et al., 2024, *Heart Failure Reviews* | https://doi.org/10.1016/j.ijcchd.2024.100530; https://doi.org/10.1007/s10741-024-10435-5 |
| Risk factors | Advanced maternal age increases risk (iannaccone2024diagnosisandmanagement pages 1-2, sigauke2024peripartumcardiomyopathya pages 2-4) | 10-fold higher risk for women >40 vs <20 years; registry mean age ~28.9–33 years, with higher risk at <20 and >35 years (iannaccone2024diagnosisandmanagement pages 1-2, sigauke2024peripartumcardiomyopathya pages 2-4) | Iannaccone et al., 2024, *Int J Cardiol Congenital Heart Disease*; Sigauke et al., 2024, *Heart Failure Reviews* | https://doi.org/10.1016/j.ijcchd.2024.100530; https://doi.org/10.1007/s10741-024-10435-5 |
| Risk factors | Multiple gestation is a recurrently reported risk factor (iannaccone2024diagnosisandmanagement pages 1-2, sigauke2024peripartumcardiomyopathya pages 4-5) | Reported in 7–14.5% of cases (iannaccone2024diagnosisandmanagement pages 1-2) | Iannaccone et al., 2024, *Int J Cardiol Congenital Heart Disease*; Sigauke et al., 2024, *Heart Failure Reviews* | https://doi.org/10.1016/j.ijcchd.2024.100530; https://doi.org/10.1007/s10741-024-10435-5 |
| Risk factors | Additional reported risk factors include multiparity, family history, infertility treatment, anemia/malnutrition, obesity/diabetes, smoking, alcohol/drug use, low BMI, and prolonged beta-agonist tocolysis (sigauke2024peripartumcardiomyopathya pages 4-5, laskowska2026peripartumcardiomyopathycurrent pages 4-5, iannaccone2024diagnosisandmanagement pages 1-2) | Quantification not consistently provided in the snippets; risk factor lists recur across reviews (sigauke2024peripartumcardiomyopathya pages 4-5, laskowska2026peripartumcardiomyopathycurrent pages 4-5, iannaccone2024diagnosisandmanagement pages 1-2) | Sigauke et al., 2024, *Heart Failure Reviews*; Laskowska, 2026, review excerpt; Iannaccone et al., 2024, *Int J Cardiol Congenital Heart Disease* | https://doi.org/10.1007/s10741-024-10435-5; https://doi.org/10.1016/j.ijcchd.2024.100530 |
| Biomarkers/diagnostics | Natriuretic peptides are central diagnostic biomarkers with strong rule-out value (sigauke2024peripartumcardiomyopathya pages 5-7) | BNP <100 pg/mL, NT-proBNP <300 pg/mL, MR-proANP <120 pmol/L have high negative predictive value (sigauke2024peripartumcardiomyopathya pages 5-7) | Sigauke et al., 2024, *Heart Failure Reviews* | https://doi.org/10.1007/s10741-024-10435-5 |
| Biomarkers/prognosis | Higher NT-proBNP at diagnosis predicts worse recovery (sigauke2024peripartumcardiomyopathya pages 5-7) | NT-proBNP >900 pg/mL predicted poor LV recovery in one cohort (sigauke2024peripartumcardiomyopathya pages 5-7) | Sigauke et al., 2024, *Heart Failure Reviews* | https://doi.org/10.1007/s10741-024-10435-5 |
| Biomarkers/mechanistic candidates | Candidate molecular biomarkers under study include prolactin-axis, angiogenic, inflammatory, fibrosis, and RNA markers (sigauke2024peripartumcardiomyopathya pages 5-7, sigauke2024peripartumcardiomyopathya pages 7-8) | Reported candidates include microRNA-146a, cathepsin D, 16-kDa prolactin/vasoinhibin, sFlt1, sST2, Gal-3, GDF-15, ADM, interferon-γ, ADMA, long noncoding RNA, and heat-shock proteins; no validated clinical thresholds given in snippets (sigauke2024peripartumcardiomyopathya pages 5-7, sigauke2024peripartumcardiomyopathya pages 7-8) | Sigauke et al., 2024, *Heart Failure Reviews* | https://doi.org/10.1007/s10741-024-10435-5 |
| Genetics | Genetic predisposition likely explains a minority but important subset of PPCM, fitting a “two-hit” model where pregnancy stress unmasks latent susceptibility (sigauke2024peripartumcardiomyopathya pages 5-7, sigauke2024peripartumcardiomyopathya pages 2-4) | Genetics may explain up to ~15% of cases; >90% of variant carriers do not develop PPCM, implying additional triggers (sigauke2024peripartumcardiomyopathya pages 5-7) | Sigauke et al., 2024, *Heart Failure Reviews* | https://doi.org/10.1007/s10741-024-10435-5 |
| Genetics | TTN truncating variants are the predominant implicated genetic contributors; other cardiomyopathy genes are also reported (sigauke2024peripartumcardiomyopathya pages 5-7, sigauke2024peripartumcardiomyopathya pages 4-5) | Genes named in snippets: **TTN** (predominant), **MYH**, **MYBPC3**, **LMNA**, **SCN5A**; broader phrasing also notes sarcomeric/cytoskeletal genes linked to familial DCM/PPCM susceptibility (sigauke2024peripartumcardiomyopathya pages 5-7, sigauke2024peripartumcardiomyopathya pages 4-5) | Sigauke et al., 2024, *Heart Failure Reviews* | https://doi.org/10.1007/s10741-024-10435-5 |


*Table: This table summarizes evidence-supported facts on peripartum cardiomyopathy definition, epidemiology, risk factors, biomarkers, and genetics. It is designed as a compact, citable artifact for rapid knowledge-base population.*

| Category | Suggested term label | Ontology (HPO/GO/CL/UBERON/MAXO) | Term ID (if known; otherwise leave blank) | Evidence/justification (brief) | Cited sources |
|---|---|---|---|---|---|
| Phenotype | Dyspnea | HPO | HP:0002094 | PPCM commonly presents with heart-failure symptoms including dyspnea in late pregnancy/postpartum. | (yusuf2025advancingourunderstanding pages 1-2, iannaccone2024diagnosisandmanagement pages 1-2) |
| Phenotype | Orthopnea | HPO | HP:0002092 | Orthopnea is listed among typical HF manifestations in PPCM reviews. | (yusuf2025advancingourunderstanding pages 1-2) |
| Phenotype | Edema | HPO | HP:0000969 | Peripheral edema/congestion is a frequent presenting sign of PPCM-related HF. | (yusuf2025advancingourunderstanding pages 1-2, sigauke2024peripartumcardiomyopathya pages 7-8) |
| Phenotype | Left ventricular systolic dysfunction | HPO | HP:0005162 | Core diagnostic feature of PPCM is new LV systolic dysfunction. | (iannaccone2024diagnosisandmanagement pages 1-2, sigauke2024peripartumcardiomyopathya pages 1-2) |
| Phenotype | Reduced left ventricular ejection fraction | HPO |  | PPCM is generally defined by LVEF <45%; reduced LVEF is central to diagnosis/prognosis. | (iannaccone2024diagnosisandmanagement pages 1-2, sigauke2024peripartumcardiomyopathya pages 1-2, sigauke2024peripartumcardiomyopathya pages 2-4) |
| Phenotype | Arrhythmia | HPO | HP:0011675 | ECG abnormalities and arrhythmias, including atrial fibrillation and QTc prolongation, are common in PPCM. | (sigauke2024peripartumcardiomyopathya pages 5-7, sigauke2024peripartumcardiomyopathya pages 7-8) |
| Phenotype | Cardiogenic shock | HPO | HP:0031970 | Severe PPCM may present with decompensated HF/cardiogenic shock and is a major cause of death. | (laskowska2026peripartumcardiomyopathycurrent pages 19-20, laskowska2026peripartumcardiomyopathy–whatisa pages 16-17) |
| Phenotype | Thromboembolism | HPO | HP:0001907 | PPCM is associated with thromboembolic complications, especially in the hypercoagulable peripartum period. | (laskowska2026peripartumcardiomyopathycurrent pages 19-20, laskowska2026peripartumcardiomyopathy–whatisa pages 16-17, iannaccone2024diagnosisandmanagement pages 4-5) |
| Biological process | Response to oxidative stress | GO | GO:0006979 | Oxidative stress is a central upstream mechanism linked to prolactin cleavage and endothelial/cardiomyocyte injury. | (laskowska2026peripartumcardiomyopathycurrent pages 4-5, sigauke2024peripartumcardiomyopathya pages 2-4, sigauke2024peripartumcardiomyopathya pages 4-5) |
| Biological process | Angiogenesis | GO | GO:0001525 | Anti-angiogenic imbalance with elevated sFlt1 and reduced VEGF/PGC1α signaling is implicated in PPCM. | (laskowska2026peripartumcardiomyopathycurrent pages 4-5, sigauke2024peripartumcardiomyopathya pages 2-4, sigauke2024peripartumcardiomyopathya pages 4-5) |
| Biological process | Regulation of angiogenesis | GO | GO:0045765 | Reviews emphasize dysregulated angiogenic signaling rather than simply angiogenesis itself. | (laskowska2026peripartumcardiomyopathycurrent pages 4-5, sigauke2024peripartumcardiomyopathya pages 4-5) |
| Biological process | Endothelial cell apoptotic process / endothelial dysfunction | GO |  | 16-kDa prolactin/vasoinhibin and sFlt1 promote endothelial damage and vascular dysfunction in PPCM. | (laskowska2026peripartumcardiomyopathycurrent pages 4-5, sigauke2024peripartumcardiomyopathya pages 2-4, sigauke2024peripartumcardiomyopathya pages 4-5) |
| Biological process | Apoptotic process in cardiac muscle cells | GO | GO:0006915 | Pathogenic prolactin fragment and vasculo-hormonal stress contribute to cardiomyocyte apoptosis. | (laskowska2026peripartumcardiomyopathycurrent pages 4-5, sigauke2024peripartumcardiomyopathya pages 4-5) |
| Biological process | Inflammatory response | GO | GO:0006954 | Inflammation/autoimmunity is repeatedly cited as part of PPCM pathophysiology. | (sigauke2024peripartumcardiomyopathya pages 4-5) |
| Biological process | microRNA-mediated gene silencing / miRNA-mediated regulation | GO |  | miR-146a is a recurrent mechanistic marker linking endothelial stress to cardiomyocyte dysfunction. | (sigauke2024peripartumcardiomyopathya pages 2-4, sigauke2024peripartumcardiomyopathya pages 5-7) |
| Cell type | Cardiac muscle cell | CL | CL:0000746 | Cardiac muscle cells are the main injured contractile cells underlying LV dysfunction. | (laskowska2026peripartumcardiomyopathycurrent pages 4-5, sigauke2024peripartumcardiomyopathya pages 4-5) |
| Cell type | Cardiomyocyte | CL |  | Reviews specifically refer to cardiomyocyte dysfunction/apoptosis as a downstream effect. | (laskowska2026peripartumcardiomyopathycurrent pages 4-5, sigauke2024peripartumcardiomyopathya pages 2-4, sigauke2024peripartumcardiomyopathya pages 4-5) |
| Cell type | Endothelial cell | CL | CL:0000115 | Endothelial dysfunction is a key mechanistic node in the prolactin/sFlt1 model of PPCM. | (laskowska2026peripartumcardiomyopathycurrent pages 4-5, sigauke2024peripartumcardiomyopathya pages 2-4, sigauke2024peripartumcardiomyopathya pages 4-5) |
| Cell type | Trophoblast cell | CL | CL:0000351 | Placental anti-angiogenic factor sFlt1 is implicated; trophoblast lineage is the likely placental source annotation. | (laskowska2026peripartumcardiomyopathycurrent pages 4-5, iannaccone2024diagnosisandmanagement pages 1-2, sigauke2024peripartumcardiomyopathya pages 2-4) |
| Anatomical structure | Left ventricle | UBERON | UBERON:0002084 | LV structure/function is central to diagnosis, imaging, and outcome assessment in PPCM. | (iannaccone2024diagnosisandmanagement pages 1-2, sigauke2024peripartumcardiomyopathya pages 1-2, sigauke2024peripartumcardiomyopathya pages 7-8) |
| Anatomical structure | Myocardium | UBERON | UBERON:0002349 | PPCM is a myocardial disease causing ventricular systolic dysfunction. | (yusuf2025advancingourunderstanding pages 1-2, sigauke2024peripartumcardiomyopathya pages 1-2) |
| Anatomical structure | Cardiac vasculature | UBERON |  | Vascular/endothelial injury and anti-angiogenic signaling are core mechanistic themes. | (laskowska2026peripartumcardiomyopathycurrent pages 4-5, sigauke2024peripartumcardiomyopathya pages 2-4, sigauke2024peripartumcardiomyopathya pages 4-5) |
| Anatomical structure | Placenta | UBERON | UBERON:0001987 | Placenta is implicated as the source of circulating anti-angiogenic factors such as sFlt1. | (laskowska2026peripartumcardiomyopathycurrent pages 4-5, iannaccone2024diagnosisandmanagement pages 1-2, sigauke2024peripartumcardiomyopathya pages 2-4) |
| Intervention | Beta-blocker therapy | MAXO |  | Standard HF pharmacotherapy in PPCM includes beta-blockers when appropriate. | (yusuf2025advancingourunderstanding pages 1-2, iannaccone2024diagnosisandmanagement pages 4-5, sigauke2024peripartumcardiomyopathya media 4d9eef0c) |
| Intervention | ACE inhibitor therapy postpartum | MAXO |  | ACE inhibitors are part of postpartum HFrEF management; avoided during pregnancy but used after delivery. | (yusuf2025advancingourunderstanding pages 1-2, iannaccone2024diagnosisandmanagement pages 4-5, sigauke2024peripartumcardiomyopathya media 4d9eef0c) |
| Intervention | Diuretic therapy | MAXO |  | Diuretics are used for symptomatic congestion/acute HF in PPCM. | (yusuf2025advancingourunderstanding pages 1-2, sigauke2024peripartumcardiomyopathya media 4d9eef0c) |
| Intervention | Anticoagulation | MAXO |  | Guidelines recommend anticoagulation in severe LV dysfunction and when bromocriptine is used. | (iannaccone2024diagnosisandmanagement pages 4-5, NCT05180773 chunk 1, NCT02590601 chunk 1) |
| Intervention | Bromocriptine therapy | MAXO |  | Bromocriptine is the main disease-targeted therapy under study, based on prolactin inhibition. | (iannaccone2024diagnosisandmanagement pages 1-2, kumar2023prolactininhibitionin pages 4-6, kumar2023prolactininhibitionin pages 1-3, NCT05180773 chunk 1) |
| Intervention | Mechanical circulatory support | MAXO |  | Severe PPCM may require ECMO/LVAD/BiVAD as bridge to recovery or transplant. | (laskowska2026peripartumcardiomyopathycurrent pages 19-20, iannaccone2024diagnosisandmanagement pages 4-5) |


*Table: This table proposes ontology-linked annotations for peripartum cardiomyopathy across phenotypes, mechanisms, cell types, anatomy, and interventions. It is useful as a compact starting point for disease knowledge-base curation grounded in the extracted evidence.*

---

## Visual evidence: management algorithm
A treatment flowchart for PPCM pharmacologic management (pregnancy vs postpartum) was retrieved from the 2024 comprehensive review. (sigauke2024peripartumcardiomyopathya media 4d9eef0c)

---

## Limitations of this evidence package (important for curation)
- Many template elements (ICD/MeSH/MONDO/Orphanet IDs; ClinVar variant-level annotations; gnomAD frequencies; robust protective factors; detailed animal model descriptions) were **not present in the retrieved evidence excerpts** and cannot be safely inferred here.
- Several key sources used are narrative reviews; while they summarize primary literature, they are not themselves primary trials/registries. Where possible, this report emphasizes quantitative findings and direct abstract quotes from 2023–2024 systematic reviews and cohort studies.



References

1. (sigauke2024peripartumcardiomyopathya pages 1-2): Farai Russell Sigauke, Hopewell Ntsinjana, and Nqoba Tsabedze. Peripartum cardiomyopathy: a comprehensive and contemporary review. Heart Failure Reviews, 29:1261-1278, Sep 2024. URL: https://doi.org/10.1007/s10741-024-10435-5, doi:10.1007/s10741-024-10435-5. This article has 36 citations and is from a peer-reviewed journal.

2. (sigauke2024peripartumcardiomyopathya pages 5-7): Farai Russell Sigauke, Hopewell Ntsinjana, and Nqoba Tsabedze. Peripartum cardiomyopathy: a comprehensive and contemporary review. Heart Failure Reviews, 29:1261-1278, Sep 2024. URL: https://doi.org/10.1007/s10741-024-10435-5, doi:10.1007/s10741-024-10435-5. This article has 36 citations and is from a peer-reviewed journal.

3. (iannaccone2024diagnosisandmanagement pages 1-2): Giulia Iannaccone, Francesca Graziani, Polona Kacar, Pietro Paolo Tamborrino, Rosa Lillo, Claudia Montanaro, Francesco Burzotta, and Michael A. Gatzoulis. Diagnosis and management of peripartum cardiomyopathy and recurrence risk. International Journal of Cardiology Congenital Heart Disease, 17:100530, Sep 2024. URL: https://doi.org/10.1016/j.ijcchd.2024.100530, doi:10.1016/j.ijcchd.2024.100530. This article has 11 citations.

4. (kumar2023prolactininhibitionin pages 4-6): Amudha Kumar, Ramya Ravi, Ranjith K. Sivakumar, Vignesh Chidambaram, Marie G. Majella, Shashank Sinha, Luigi Adamo, Emily S. Lau, Subhi J. Al'Aref, Aarti Asnani, Garima Sharma, and Jawahar L. Mehta. Prolactin inhibition in peripartum cardiomyopathy: systematic review and meta-analysis. Current Problems in Cardiology, 48:101461, Feb 2023. URL: https://doi.org/10.1016/j.cpcardiol.2022.101461, doi:10.1016/j.cpcardiol.2022.101461. This article has 38 citations and is from a peer-reviewed journal.

5. (sigauke2024peripartumcardiomyopathya pages 2-4): Farai Russell Sigauke, Hopewell Ntsinjana, and Nqoba Tsabedze. Peripartum cardiomyopathy: a comprehensive and contemporary review. Heart Failure Reviews, 29:1261-1278, Sep 2024. URL: https://doi.org/10.1007/s10741-024-10435-5, doi:10.1007/s10741-024-10435-5. This article has 36 citations and is from a peer-reviewed journal.

6. (noll2024breastfeedinginpatients pages 1-2): Angelina Noll, Kris R. Kawamoto, Maya T. Dassanayake, Laura Leuenberger, Stephanie M. Spehar, Jenny Wu, Elizabeth Langen, and Melinda B. Davis. Breastfeeding in patients with peripartum cardiomyopathy: clinical outcomes and physician counseling. International Breastfeeding Journal, Oct 2024. URL: https://doi.org/10.1186/s13006-024-00673-6, doi:10.1186/s13006-024-00673-6. This article has 7 citations and is from a peer-reviewed journal.

7. (sigauke2024peripartumcardiomyopathya pages 4-5): Farai Russell Sigauke, Hopewell Ntsinjana, and Nqoba Tsabedze. Peripartum cardiomyopathy: a comprehensive and contemporary review. Heart Failure Reviews, 29:1261-1278, Sep 2024. URL: https://doi.org/10.1007/s10741-024-10435-5, doi:10.1007/s10741-024-10435-5. This article has 36 citations and is from a peer-reviewed journal.

8. (laskowska2026peripartumcardiomyopathy–whatisa pages 3-5): M Laskowska. Peripartum cardiomyopathy–what is worth knowing when a young mother's heart is diseased? a review. Unknown journal, 2026.

9. (yusuf2025advancingourunderstanding pages 1-2): I Yusuf, A Enenche, and R Adefila. Advancing our understanding of peripartum cardiomyopathy: current evidence and future directions. Unknown journal, 2025.

10. (sigauke2024peripartumcardiomyopathya pages 7-8): Farai Russell Sigauke, Hopewell Ntsinjana, and Nqoba Tsabedze. Peripartum cardiomyopathy: a comprehensive and contemporary review. Heart Failure Reviews, 29:1261-1278, Sep 2024. URL: https://doi.org/10.1007/s10741-024-10435-5, doi:10.1007/s10741-024-10435-5. This article has 36 citations and is from a peer-reviewed journal.

11. (laskowska2026peripartumcardiomyopathycurrent pages 19-20): Marzena Laskowska. Peripartum cardiomyopathy: current insights into pathogenesis and clinical management: a narrative review. Journal of Clinical Medicine, 15:2974, Apr 2026. URL: https://doi.org/10.3390/jcm15082974, doi:10.3390/jcm15082974. This article has 0 citations.

12. (iannaccone2024diagnosisandmanagement pages 4-5): Giulia Iannaccone, Francesca Graziani, Polona Kacar, Pietro Paolo Tamborrino, Rosa Lillo, Claudia Montanaro, Francesco Burzotta, and Michael A. Gatzoulis. Diagnosis and management of peripartum cardiomyopathy and recurrence risk. International Journal of Cardiology Congenital Heart Disease, 17:100530, Sep 2024. URL: https://doi.org/10.1016/j.ijcchd.2024.100530, doi:10.1016/j.ijcchd.2024.100530. This article has 11 citations.

13. (NCT02590601 chunk 1): Marc Jolicoeur. Bromocriptine in the Treatment of Peripartum Cardiomyopathy. Montreal Heart Institute. 2017. ClinicalTrials.gov Identifier: NCT02590601

14. (wijayanto2024outcomesofsubsequent pages 1-1): Matthew Aldo Wijayanto, Risalina Myrtha, Graciella Angelica Lukas, Annisa Aghnia Rahma, Shafira Nur Hanifa, Hadiqa Almas Zahira, and Muhana Fawwazy Ilyas. Outcomes of subsequent pregnancy in women with peripartum cardiomyopathy: a systematic review and meta-analysis. Open Heart, 11:e002626, Apr 2024. URL: https://doi.org/10.1136/openhrt-2024-002626, doi:10.1136/openhrt-2024-002626. This article has 17 citations and is from a peer-reviewed journal.

15. (wijayanto2024outcomesofsubsequent pages 3-4): Matthew Aldo Wijayanto, Risalina Myrtha, Graciella Angelica Lukas, Annisa Aghnia Rahma, Shafira Nur Hanifa, Hadiqa Almas Zahira, and Muhana Fawwazy Ilyas. Outcomes of subsequent pregnancy in women with peripartum cardiomyopathy: a systematic review and meta-analysis. Open Heart, 11:e002626, Apr 2024. URL: https://doi.org/10.1136/openhrt-2024-002626, doi:10.1136/openhrt-2024-002626. This article has 17 citations and is from a peer-reviewed journal.

16. (laskowska2026peripartumcardiomyopathy–whatisa pages 16-17): M Laskowska. Peripartum cardiomyopathy–what is worth knowing when a young mother's heart is diseased? a review. Unknown journal, 2026.

17. (sigauke2024peripartumcardiomyopathya media 4d9eef0c): Farai Russell Sigauke, Hopewell Ntsinjana, and Nqoba Tsabedze. Peripartum cardiomyopathy: a comprehensive and contemporary review. Heart Failure Reviews, 29:1261-1278, Sep 2024. URL: https://doi.org/10.1007/s10741-024-10435-5, doi:10.1007/s10741-024-10435-5. This article has 36 citations and is from a peer-reviewed journal.

18. (iannaccone2024diagnosisandmanagement pages 5-6): Giulia Iannaccone, Francesca Graziani, Polona Kacar, Pietro Paolo Tamborrino, Rosa Lillo, Claudia Montanaro, Francesco Burzotta, and Michael A. Gatzoulis. Diagnosis and management of peripartum cardiomyopathy and recurrence risk. International Journal of Cardiology Congenital Heart Disease, 17:100530, Sep 2024. URL: https://doi.org/10.1016/j.ijcchd.2024.100530, doi:10.1016/j.ijcchd.2024.100530. This article has 11 citations.

19. (NCT05180773 chunk 1): Dennis M. McNamara, MD, MS. Impact of Bromocriptine on Clinical Outcomes for Peripartum Cardiomyopathy. Dennis M. McNamara, MD, MS. 2022. ClinicalTrials.gov Identifier: NCT05180773

20. (NCT00998556 chunk 1): Denise Hilfiker-Kleiner, PhD. Effect of Bromocriptine on Left Ventricular Function in Women With Peripartum Cardiomyopathy. Hannover Medical School. 2010. ClinicalTrials.gov Identifier: NCT00998556

21. (laskowska2026peripartumcardiomyopathycurrent pages 4-5): Marzena Laskowska. Peripartum cardiomyopathy: current insights into pathogenesis and clinical management: a narrative review. Journal of Clinical Medicine, 15:2974, Apr 2026. URL: https://doi.org/10.3390/jcm15082974, doi:10.3390/jcm15082974. This article has 0 citations.

22. (kumar2023prolactininhibitionin pages 1-3): Amudha Kumar, Ramya Ravi, Ranjith K. Sivakumar, Vignesh Chidambaram, Marie G. Majella, Shashank Sinha, Luigi Adamo, Emily S. Lau, Subhi J. Al'Aref, Aarti Asnani, Garima Sharma, and Jawahar L. Mehta. Prolactin inhibition in peripartum cardiomyopathy: systematic review and meta-analysis. Current Problems in Cardiology, 48:101461, Feb 2023. URL: https://doi.org/10.1016/j.cpcardiol.2022.101461, doi:10.1016/j.cpcardiol.2022.101461. This article has 38 citations and is from a peer-reviewed journal.