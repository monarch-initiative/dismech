---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-04T15:41:53.856230'
end_time: '2026-05-04T15:59:37.280334'
duration_seconds: 1063.42
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Subacute Inflammatory Demyelinating Polyneuropathy
  mondo_id: ''
  category: Autoimmune
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
- **Disease Name:** Subacute Inflammatory Demyelinating Polyneuropathy
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Subacute Inflammatory Demyelinating Polyneuropathy** covering all of the
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
- **Disease Name:** Subacute Inflammatory Demyelinating Polyneuropathy
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Subacute Inflammatory Demyelinating Polyneuropathy** covering all of the
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


## Comprehensive Disease Characteristics Research Report: Subacute Inflammatory Demyelinating Polyneuropathy (SIDP)

### Executive summary
Subacute inflammatory demyelinating polyneuropathy (SIDP) is an acquired immune-mediated demyelinating peripheral neuropathy defined primarily by **a subacute tempo (nadir 4–8 weeks)** and (in “definite SIDP”) a **monophasic, non-relapsing course** on longitudinal follow-up. It sits in the clinical time-course “gray zone” between Guillain–Barré syndrome/acute inflammatory demyelinating polyradiculoneuropathy (GBS/AIDP; nadir ≤4 weeks) and chronic inflammatory demyelinating polyneuropathy (CIDP; progression >8 weeks or relapsing). SIDP is diagnosed using clinical features plus **electrodiagnostic demyelination**, supported by **elevated CSF protein** and (occasionally) nerve biopsy evidence of demyelination/inflammation. In the foundational SIDP cohort (Neurology 2003), immunotherapy—especially corticosteroids—was associated with high rates of recovery, but a subset initially labeled “probable SIDP” relapsed and was later reclassified as CIDP, underscoring the importance of follow-up. (oh2003subacuteinflammatorydemyelinating pages 1-2, oh2003subacuteinflammatorydemyelinating pages 3-4, bergh2021europeanacademyof pages 4-5)

| Feature | SIDP (4–8 weeks) evidence | GBS/AIDP comparator | CIDP/A-CIDP comparator | Notes/implications | Key citations |
|---|---|---|---|---|---|
| Core definition / time to nadir | Distinct subacute inflammatory demyelinating neuropathy with progression to nadir in **4–8 weeks**; Oh et al. proposed definite/probable SIDP criteria. Mean progression in their cohort was ~1.6–1.7 months. | AIDP/GBS usually reaches nadir within **≤4 weeks** and is typically monophasic. | Typical CIDP progresses **>8 weeks**; A-CIDP may begin acutely but later continues beyond 8 weeks or relapses repeatedly. | SIDP occupies the temporal “gray zone” between acute GBS and chronic CIDP. | (oh2003subacuteinflammatorydemyelinating pages 1-2, oh2003subacuteinflammatorydemyelinating pages 4-5, bergh2021europeanacademyof pages 4-5, lewis2017chronicinflammatorydemyelinating pages 1-4) |
| Course pattern | **Definite SIDP is monophasic by definition** and requires no relapse on adequate follow-up (Oh used ≥2 years). | GBS is also classically monophasic, though treatment-related fluctuations can occur. | CIDP is progressive or relapsing; A-CIDP may relapse or deteriorate after week 8 and/or have ≥3 relapses after initial improvement. | Longitudinal follow-up is essential; early cases may be reclassified. | (oh2003subacuteinflammatorydemyelinating pages 1-2, oh2003subacuteinflammatorydemyelinating pages 4-5, bergh2021europeanacademyof pages 4-5, alessandro2018differencesbetweenacute‐onset pages 1-8) |
| Relapse frequency | In Oh 2003, **17% of probable SIDP** relapsed and were reclassified; **0% of definite SIDP** relapsed. | Some GBS patients fluctuate after treatment, but persistent chronic evolution is not typical. | CIDP relapse rate in Oh cohort was **50%**; guideline notes up to **13%** of CIDP can present as acute-onset CIDP. | Relapse after the subacute window strongly favors CIDP/A-CIDP over true SIDP. | (oh2003subacuteinflammatorydemyelinating pages 3-4, bergh2021europeanacademyof pages 4-5, alessandro2018differencesbetweenacute‐onset pages 1-8) |
| Typical clinical phenotype | Often symmetric motor-sensory or pure motor neuropathy; cranial nerve and respiratory involvement were **rare** in Oh series. Antecedent infection occurred in **38%**. | GBS more often has antecedent infection (>70% in review context) and may have more cranial/autonomic/respiratory involvement. | A-CIDP/CIDP more often has sensory signs/proprioceptive deficits and less cranial/respiratory/autonomic involvement than GBS; antecedent infection less common than SIDP in Oh cohort. | Clinical phenotype overlaps broadly; tempo plus follow-up is more discriminating than symptoms alone. | (oh2003subacuteinflammatorydemyelinating pages 1-2, oh2003subacuteinflammatorydemyelinating pages 3-4, bergh2021europeanacademyof pages 4-5, lewis2017chronicinflammatorydemyelinating pages 1-4) |
| Sensory ataxia / proprioception | Not a defining SIDP marker, but overlap with CIDP sensory features exists. | Less frequent in AIDP than A-CIDP in Alessandro et al. | In Alessandro 2018, A-CIDP had more **proprioceptive disturbance (83% vs 28%)** and **sensory ataxia (46% vs 16%)** than AIDP. | Prominent proprioceptive loss during an acute-subacute presentation should raise suspicion for CIDP-spectrum disease rather than pure GBS. | (alessandro2018differencesbetweenacute‐onset pages 1-8) |
| Electrophysiology | Demyelination required in ≥2 nerves for diagnosis; documented in nearly all SIDP cases, with latency prolongation and slowed motor NCV particularly helpful; conduction block/dispersion in ~50%. | AIDP is also demyelinating electrophysiologically, so early distinction from SIDP may be difficult. | CIDP diagnosis likewise depends on demyelinating NCS criteria; 2021 EAN/PNS refined motor and sensory criteria for typical and variant CIDP. | NCS is central but not fully disease-specific; serial studies may help if classification remains uncertain. | (oh2003subacuteinflammatorydemyelinating pages 1-2, oh2003subacuteinflammatorydemyelinating pages 3-4, doorn2024challengesinthe media a605ddf1) |
| CSF findings | CSF protein usually elevated; Oh reported **93%** high protein in definite SIDP. | Albuminocytologic dissociation is common in GBS as well. | CSF protein elevation is also common in CIDP; supportive, not specific. | CSF supports inflammatory demyelinating neuropathy but does not cleanly separate SIDP from GBS/CIDP. | (oh2003subacuteinflammatorydemyelinating pages 1-2, oh2003subacuteinflammatorydemyelinating pages 2-3, stino2021chronicinflammatorydemyelinating pages 1-3) |
| Nerve biopsy / pathology | Supportive only; demyelination commonly seen, inflammatory cells in a minority, onion bulbs generally absent in SIDP series. | Biopsy is not routine for GBS. | Chronic CIDP may show more chronic changes such as onion bulbs/remyelination. | Biopsy can support an acquired inflammatory neuropathy when NCS are equivocal, but is not first-line. | (oh2003subacuteinflammatorydemyelinating pages 2-3, oh2003subacuteinflammatorydemyelinating pages 3-4, ramchandren2009chronicneuropathieschronicinflammatory pages 3-6) |
| Response to immunotherapy | Oh reported high treatment responsiveness, mainly to prednisone; complete recovery in **69%** of definite SIDP. | GBS usually treated with IVIg or plasma exchange; corticosteroids are not standard effective therapy. | CIDP responds to IVIg, corticosteroids, and plasma exchange, but often needs maintenance therapy; A-CIDP often requires chronic immunotherapy. | Steroid responsiveness in a 4–8 week demyelinating neuropathy can point away from GBS and toward SIDP/CIDP spectrum. | (oh2003subacuteinflammatorydemyelinating pages 3-4, oh2003subacuteinflammatorydemyelinating pages 4-5, bergh2021europeanacademyof pages 4-5, doorn2024challengesinthe pages 1-2) |
| Recovery / prognosis | Better short- to medium-term outcome than CIDP in Oh study; overall high full-recovery rate. | GBS outcome varies widely; severe respiratory/autonomic disease can occur. | CIDP carries higher risk of chronic disability and treatment dependence if not recognized early. | SIDP may be a relatively favorable monophasic inflammatory demyelinating neuropathy if it does not relapse. | (oh2003subacuteinflammatorydemyelinating pages 3-4, doorn2024challengesinthe pages 1-2) |
| Early diagnostic pitfall | By definition, SIDP cannot be fully confirmed immediately because relapse exclusion needs follow-up; some cases first labeled GBS later prove SIDP or A-CIDP. | Onset **<4 weeks** is a red flag for GBS in CIDP workup. | 2024 review emphasizes mis/underdiagnosis in CIDP and need to reassess when phenotype, NCS, or treatment response are atypical. | In real-world practice, SIDP is often a **working diagnosis** pending longitudinal evolution. | (oh2003subacuteinflammatorydemyelinating pages 4-5, doorn2024challengesinthe pages 2-3, doorn2024challengesinthe pages 1-2, bergh2021europeanacademyof pages 4-5) |
| Biomarkers / recent research | Evidence remains limited specifically for SIDP; in a 2023 biomarker study, only **3 SIDP cases** were included, and SIDP patients had higher CSF IL-8 than CIDP in a small exploratory comparison. | IL-8 is elevated in GBS and correlates with severity/outcome. | IL-8 is also elevated in CIDP vs healthy/non-inflammatory controls, but no validated SIDP-specific biomarker exists. | Recent biomarker work is promising for the broader inflammatory demyelinating neuropathy spectrum, but **not yet SIDP-specific or practice-defining**. | (kmezic2023validationofelevated pages 1-2, kmezic2023validationofelevated pages 3-4) |


*Table: This table compares subacute inflammatory demyelinating polyneuropathy with GBS/AIDP and CIDP/A-CIDP using the most clinically useful differentiators: timing, relapse pattern, symptoms, electrophysiology, CSF, treatment response, and recent biomarker evidence.*

---

## 1. Disease information

### 1.1 Overview / definition
Oh et al. (Neurology, 2003-12; DOI URL: https://doi.org/10.1212/01.wnl.0000096166.28131.4c) proposed SIDP as a distinct inflammatory demyelinating polyneuropathy with **time to nadir between 4 and 8 weeks**, and for “definite SIDP” a **monophasic course with no relapse** during “adequate follow-up” (≥2 years in the study). (oh2003subacuteinflammatorydemyelinating pages 1-2, oh2003subacuteinflammatorydemyelinating pages 4-5)

### 1.2 Key identifiers (OMIM, Orphanet, ICD-10/11, MeSH, MONDO)
Within the tool-retrieved primary literature set used here, SIDP appears mainly as a **clinical descriptive term** and was **not successfully mapped** to a disease identifier in OpenTargets; I could not verify a MONDO/Orphanet/ICD/MeSH identifier from the retrieved evidence alone. (oh2003subacuteinflammatorydemyelinating pages 1-2)

**Knowledge base note:** For coding, SIDP is often represented in practice as part of the acquired immune-mediated demyelinating polyneuropathy spectrum (GBS/AIDP vs CIDP vs A-CIDP) rather than as a widely standardized standalone ontology entry in the sources retrieved here. (ramchandren2009chronicneuropathieschronicinflammatory pages 1-3, bergh2021europeanacademyof pages 4-5)

### 1.3 Synonyms / alternative names
* “Subacute inflammatory demyelinating polyneuropathy (SIDP)” (oh2003subacuteinflammatorydemyelinating pages 1-2)
* Sometimes described conceptually as “subacute GBS” in rare cases where progression extends to 6–8 weeks (kmezic2025biomarkerandpathogenic pages 29-35)
* “Gray zone between 4 and 8 weeks” between GBS and CIDP (ramchandren2009chronicneuropathieschronicinflammatory pages 1-3)

### 1.4 Source type of information
Evidence in this report is derived from:
* **Aggregated disease-level resources** (CIDP guideline/review) (bergh2021europeanacademyof pages 4-5, doorn2024challengesinthe pages 1-2)
* **Primary cohort/series evidence for SIDP** (Oh et al., 2003) (oh2003subacuteinflammatorydemyelinating pages 1-2)
* **Biomarker primary research** in inflammatory neuropathies including a small number of SIDP cases (Kmezic et al., 2023) (kmezic2023validationofelevated pages 3-4)

---

## 2. Etiology

### 2.1 Disease causal factors
SIDP is best supported as an **acquired immune-mediated demyelinating neuropathy**, within the broader CIDP/GBS spectrum. (oh2003subacuteinflammatorydemyelinating pages 1-2, dyck2018historydiagnosisand pages 2-3)

### 2.2 Risk factors / triggers
**Antecedent infection:** In the Oh et al. SIDP cohort, antecedent infection/events were reported in **38%** of cases. (oh2003subacuteinflammatorydemyelinating pages 1-2)

**Metabolic comorbidity as a differentiator in acute-onset CIDP (not SIDP-specific):** In a retrospective comparison of AIDP vs acute-onset CIDP (A-CIDP), diabetes mellitus was more frequent in A-CIDP (29% vs 8%). (alessandro2018differencesbetweenacute‐onset pages 1-8)

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved SIDP-specific evidence set. (oh2003subacuteinflammatorydemyelinating pages 2-3)

### 2.4 Gene–environment interactions
No SIDP-specific gene–environment interaction evidence was identified in the retrieved set.

---

## 3. Phenotypes

### 3.1 Core clinical features (SIDP cohort)
Oh et al. reported that SIDP commonly presents as **symmetric motor–sensory polyneuropathy** or **pure motor** subtype; cranial nerve deficits and respiratory failure were **rare**. (oh2003subacuteinflammatorydemyelinating pages 1-2, oh2003subacuteinflammatorydemyelinating pages 2-3)

### 3.2 Laboratory / electrophysiology phenotypes
* **Electrophysiologic demyelination** on nerve conduction studies is central (see Diagnostics). (oh2003subacuteinflammatorydemyelinating pages 3-4, oh2003subacuteinflammatorydemyelinating pages 1-2)
* **CSF albuminocytologic dissociation / elevated protein** is common (see Diagnostics). (oh2003subacuteinflammatorydemyelinating pages 2-3)

### 3.3 Temporal phenotype
**Tempo is defining:** nadir **4–8 weeks**. (oh2003subacuteinflammatorydemyelinating pages 1-2)

### 3.4 Suggested HPO terms (examples)
(These are ontology mappings for knowledge base use; not claims of prevalence.)
* Areflexia — **HP:0001284**
* Muscle weakness — **HP:0001324**
* Distal muscle weakness — **HP:0002460**
* Sensory neuropathy — **HP:0009830**
* Hypoesthesia — **HP:0001251**
* Paresthesia — **HP:0003401**
* Gait ataxia / sensory ataxia (if prominent) — **HP:0002066**
* Elevated CSF protein — **HP:0030208** (term naming may vary across releases)

### 3.5 Quality-of-life impact
SIDP-specific QoL instrument data were not identified in the retrieved SIDP cohort excerpt; however, CIDP-spectrum disease can cause disability affecting walking and activities of daily living. (stino2021chronicinflammatorydemyelinating pages 1-3)

---

## 4. Genetic / molecular information

### 4.1 Causal genes
No monogenic causal genes for SIDP were identified in the retrieved evidence set; SIDP is treated as **acquired autoimmune**. (oh2003subacuteinflammatorydemyelinating pages 2-3)

### 4.2 Pathogenic variants
Not established for SIDP in the retrieved evidence set.

### 4.3 Autoantibodies (molecular immune markers)
In Oh et al. (SIDP), a broad autoantibody panel (GM1, GQ1b, GD1a/1b, MAG, etc.) was largely negative; **only one** sensory definite SIDP case had positive **IgG GM1/asialo-GM1/sulfatide** antibodies. (oh2003subacuteinflammatorydemyelinating pages 2-3)

In CIDP-spectrum disease more broadly, autoantibodies to paranodal targets (eg, **NF155**) occur in a subset (reported ~**4–18%** in a high-citation review). (bunschoten2019progressindiagnosis pages 3-5)

---

## 5. Environmental information

### 5.1 Environmental and lifestyle factors
The most consistently reported “environmental” antecedent in SIDP is **preceding infection/illness** (38% in the Neurology 2003 cohort). (oh2003subacuteinflammatorydemyelinating pages 1-2)

Other environmental/lifestyle risk factors were not established from the retrieved evidence set.

### 5.2 Infectious agents
Specific pathogens were not identified in the retrieved SIDP cohort excerpt; the evidence is at the level of “antecedent infection” rather than a defined organism. (oh2003subacuteinflammatorydemyelinating pages 1-2)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (current understanding)
The best-supported mechanistic model for SIDP uses CIDP-spectrum immunopathology as the closest framework:
1. **Immune activation** → autoreactive cellular and humoral immunity (T cells and antibodies) (mathey2015chronicinflammatorydemyelinating pages 3-4)
2. **Blood–nerve barrier (BNB) dysfunction** enabling immune cell trafficking and access of humoral factors to endoneurium (mathey2015chronicinflammatorydemyelinating pages 3-4)
3. **Macrophage-mediated demyelination** and segmental demyelination/remyelination causing conduction slowing/block and sensorimotor deficits (dyck2018historydiagnosisand pages 2-3, mathey2015chronicinflammatorydemyelinating pages 3-4)
4. In subgroups, **autoantibodies to nodal/paranodal proteins** and **complement-mediated injury** may contribute in CIDP-spectrum disease (bunschoten2019progressindiagnosis pages 3-5, mathey2015chronicinflammatorydemyelinating pages 3-4)

### 6.2 Tissue damage mechanisms and pathology (SIDP-specific)
In the SIDP cohort, nerve biopsy criteria included demyelination/remyelination features and “mononuclear cell infiltration” in some cases; CSF protein elevation is consistent with barrier dysfunction. (oh2003subacuteinflammatorydemyelinating pages 2-3)

### 6.3 Immune system involvement (CIDP-spectrum)
CIDP pathology is characterized by **segmental demyelination/remyelination**, **onion-bulb formation**, and **mononuclear inflammatory infiltrates** (often perivascular). (dyck2018historydiagnosisand pages 2-3)

### 6.4 Suggested GO biological process terms (examples)
(For knowledge base annotation; not disease-specific claims of enrichment.)
* Myelination — **GO:0042552**
* Demyelination — **GO:0032291**
* Axon ensheathment — **GO:0008366**
* Leukocyte migration — **GO:0050900**
* Regulation of immune response — **GO:0050776**
* Complement activation — **GO:0006956**

### 6.5 Suggested Cell Ontology (CL) terms (examples)
* Macrophage — **CL:0000235**
* T cell — **CL:0000084** (CD4+ T cell **CL:0000624**, CD8+ T cell **CL:0000625**)
* B cell — **CL:0000236**
* Schwann cell — **CL:0000218**

---

## 7. Anatomical structures affected

### 7.1 Organ/system level
Primary system: **Peripheral nervous system** (peripheral nerves, roots) consistent with inflammatory demyelinating polyneuropathy. (oh2003subacuteinflammatorydemyelinating pages 1-2)

### 7.2 Tissue/cell level
* Myelinated peripheral nerve fibers (large motor and proprioceptive fibers emphasized in CIDP-spectrum) (dyck2018historydiagnosisand pages 2-3)
* Schwann cells/myelin, with inflammatory infiltrates (macrophages, T cells) (dyck2018historydiagnosisand pages 2-3, mathey2015chronicinflammatorydemyelinating pages 3-4)

### 7.3 Suggested UBERON terms (examples)
* Peripheral nerve — **UBERON:0001021**
* Spinal nerve root — **UBERON:0009010**
* Sural nerve — **UBERON:0011823**

---

## 8. Temporal development

### 8.1 Onset
SIDP is defined by **subacute progression** to maximal deficit (nadir) between **4 and 8 weeks**. (oh2003subacuteinflammatorydemyelinating pages 1-2)

### 8.2 Progression and remission
* Definite SIDP: **monophasic**, with no relapse during adequate follow-up (≥2 years). (oh2003subacuteinflammatorydemyelinating pages 1-2)
* A subset initially labeled probable SIDP may relapse and evolve into CIDP. (oh2003subacuteinflammatorydemyelinating pages 3-4)

---

## 9. Inheritance and population

### 9.1 Epidemiology
SIDP-specific population incidence/prevalence estimates were not identified in the retrieved SIDP-focused evidence.

Proxy epidemiology from CIDP reviews:
* CIDP incidence reported as **0.5–3.3 per 100,000** (2024 review). (doorn2024challengesinthe pages 1-2)
* CIDP prevalence estimates **0.8–1.9 per 100,000** (review context). (lewis2017chronicinflammatorydemyelinating pages 1-4)

### 9.2 Inheritance
Not applicable as a primary model; SIDP is acquired immune-mediated in the retrieved evidence. (oh2003subacuteinflammatorydemyelinating pages 2-3)

---

## 10. Diagnostics

### 10.1 Clinical criteria (SIDP)
Oh et al. proposed criteria for **definite SIDP** including: (i) progressive motor/sensory dysfunction in >1 limb with **time to nadir 4–8 weeks**, (ii) **electrophysiologic demyelination in ≥2 nerves**, (iii) no other etiology, and (iv) **no relapse** on adequate follow-up (≥2 years). Supportive criteria included CSF protein ≥55 mg/dL and inflammatory cells on nerve biopsy. (oh2003subacuteinflammatorydemyelinating pages 1-2)

### 10.2 Electrodiagnostics
SIDP requires demyelinating features on NCS/EMG; in the Oh cohort, demyelination in ≥2 nerves was documented in **93%** of probable and **all** definite cases; key helpful measures included distal latency prolongation and slowed motor conduction velocity, with conduction block/temporal dispersion in ~50%. (oh2003subacuteinflammatorydemyelinating pages 3-4, oh2003subacuteinflammatorydemyelinating pages 2-3)

### 10.3 CSF
In Oh et al., CSF protein >55 mg/dL was present in **89%** (probable) and **93%** (definite) SIDP; CSF protein range 35–800 mg/dL, mean 124 mg/dL; cell counts were generally low. (oh2003subacuteinflammatorydemyelinating pages 2-3)

### 10.4 Imaging and biopsy
In CIDP diagnostic workflows, supportive tests include imaging and biopsy; the 2024 review provides a diagnostic algorithm and practical red flags and supportive investigations. (doorn2024challengesinthe media 1489a645)

### 10.5 Differential diagnosis and “red flags” (real-world implementation)
The 2024 CIDP review highlights that onset **<4 weeks** is a red flag suggestive of GBS rather than CIDP, and provides a structured approach to reduce misdiagnosis. (doorn2024challengesinthe pages 2-3, doorn2024challengesinthe media a605ddf1)

### 10.6 Visual evidence (algorithm and criteria tables)
* Diagnostic algorithm / process figure (doorn2024challengesinthe media 1489a645)
* Nerve conduction criteria table based on EAN/PNS 2021 guideline summarized in 2024 review (doorn2024challengesinthe media be7d2bb3)

---

## 11. Outcome / prognosis

### 11.1 SIDP outcomes (Oh 2003)
Oh et al. reported **complete recovery in 69%** of definite SIDP; overall improvement was high, with most recovery occurring within 2 years, motivating their ≥2-year follow-up requirement. (oh2003subacuteinflammatorydemyelinating pages 1-2, oh2003subacuteinflammatorydemyelinating pages 3-4)

### 11.2 Prognostic factors
Robust SIDP-specific prognostic markers were not identified in the retrieved set; however, distinguishing monophasic SIDP from evolving CIDP requires follow-up, and relapse strongly suggests CIDP-spectrum disease. (oh2003subacuteinflammatorydemyelinating pages 3-4)

---

## 12. Treatment

### 12.1 SIDP treatment (primary cohort evidence)
In the Neurology 2003 cohort, **prednisone (corticosteroids)** was the main therapy, with IVIg and plasma exchange used in some; most treated patients improved, and complete recovery was frequent. A subset of “probable SIDP” relapsed and required longer-term maintenance immunotherapy (suggesting those cases were CIDP). (oh2003subacuteinflammatorydemyelinating pages 4-5, oh2003subacuteinflammatorydemyelinating pages 3-4)

### 12.2 Guideline-aligned treatment principles (CIDP-spectrum; applied in practice to SIDP when CIDP cannot yet be excluded)
The EAN/PNS 2021 guideline states principal recommendations including: initial treatment with **IVIg or corticosteroids**, and **plasma exchange** if ineffective, with maintenance treatment including IVIg/SCIg/corticosteroids. (bergh2021europeanacademyof pages 4-5)

The 2024 review provides a practical table of **first-line treatment options**, including dosage and side effects, and emphasizes objective monitoring and reassessment if response is poor. (doorn2024challengesinthe media b86e8bf0, doorn2024challengesinthe media 87bdfab1)

### 12.3 Recent developments (2023–2024): biomarkers enabling improved diagnosis/monitoring
A 2023 Frontiers in Immunology study validated **CSF IL-8** as a diagnostic biomarker for **GBS and CIDP** and prognostic in GBS; it included **3 SIDP cases** in the cohort, highlighting how rare SIDP is in biomarker datasets and that SIDP-specific biomarker validation remains incomplete. The paper also explicitly notes IL-8 biology: “*The main function of IL8 is the recruitment of neutrophils, but also T cells, and dendritic cells to the site of inflammation.*” (2023-11-23; DOI URL: https://doi.org/10.3389/fimmu.2023.1241199). (kmezic2023validationofelevated pages 3-4, kmezic2023validationofelevated pages 2-3)

### 12.4 Suggested MAXO terms (examples)
* Intravenous immunoglobulin therapy — **MAXO:0000749** (concept mapping)
* Plasma exchange — **MAXO:0000509**
* Corticosteroid therapy — **MAXO:0000647**
* Immunosuppressive agent therapy (eg, azathioprine) — **MAXO:0000648**
* Physical therapy — **MAXO:0000011**
* Occupational therapy — **MAXO:0000013**

---

## 13. Prevention
No established primary prevention is supported in the retrieved SIDP evidence. Practical prevention is primarily **secondary/tertiary**: early recognition of treatable immune-mediated neuropathy and timely initiation of effective therapy to reduce irreversible axonal damage, as emphasized for CIDP in 2024. (doorn2024challengesinthe pages 1-2)

---

## 14. Other species / natural disease
No naturally occurring SIDP analog in non-human species was identified in the retrieved evidence set.

---

## 15. Model organisms
No SIDP-specific model organism was identified in the retrieved evidence set. Mechanistic insights in the broader immune-mediated neuropathy field often use experimental autoimmune neuritis models (GBS-like), but these were not SIDP-specific in the retrieved 2023–2024 evidence. (kmezic2025biomarkerandpathogenic pages 41-44)

---

## Expert synthesis / implementation notes (authoritative consensus)
* **Time course is necessary but insufficient early:** The EAN/PNS CIDP guideline notes typical CIDP develops over “at least 8 weeks,” yet **acute-onset CIDP can occur** (up to 13%), and “distinguishing A-CIDP from GBS can be challenging,” with **5%** of initial GBS diagnoses later reclassified as A-CIDP; critically, “there are no specific clinical features or laboratory tests” to distinguish them in the acute stage. This frames SIDP as a *working diagnosis* until relapse/non-relapse is observed. (bergh2021europeanacademyof pages 4-5)
* **Real-world diagnostic algorithms matter:** The 2024 CIDP review provides a structured diagnostic process, red flags, and guideline-based NCS criteria in tabular/figure form, supporting consistent implementation in neuromuscular clinics. (doorn2024challengesinthe media a605ddf1, doorn2024challengesinthe media be7d2bb3, doorn2024challengesinthe media 1489a645)

---

## URLs and publication dates (key sources)
* Oh SJ et al. *Neurology* — “Subacute inflammatory demyelinating polyneuropathy” — **2003-12** — https://doi.org/10.1212/01.wnl.0000096166.28131.4c (oh2003subacuteinflammatorydemyelinating pages 1-2)
* Van den Bergh PYK et al. EAN/PNS CIDP guideline (2nd revision) — *J Peripher Nerv Syst* — **2021-07** — https://doi.org/10.1111/jns.12455 (bergh2021europeanacademyof pages 4-5)
* van Doorn I et al. “Challenges in the Early Diagnosis and Treatment of CIDP in Adults” — *Therapeutics and Clinical Risk Management* — **2024-02** — https://doi.org/10.2147/tcrm.s360249 (doorn2024challengesinthe pages 1-2)
* Kmezic I et al. “Validation of elevated levels of interleukin-8 in the CSF…” — *Frontiers in Immunology* — **2023-11-23** — https://doi.org/10.3389/fimmu.2023.1241199 (kmezic2023validationofelevated pages 1-2)

---

## Evidence gaps and limitations (explicit)
* **Ontology identifiers (MONDO/Orphanet/MeSH/ICD):** not verified from the retrieved evidence set; additional targeted searches in Orphanet/MeSH/MONDO would be required.
* **SIDP-specific epidemiology:** population incidence/prevalence remains unclear in the retrieved set; only CIDP incidence/prevalence estimates were available.
* **SIDP-specific biomarkers and trials:** current biomarker research largely targets GBS/CIDP; SIDP cases are rare (eg, 3 cases in Kmezic 2023), limiting SIDP-specific validation.


References

1. (oh2003subacuteinflammatorydemyelinating pages 1-2): S. J. Oh, K. Kurokawa, D. F. de Almeida, H. F. Ryan, and G. C. Claussen. Subacute inflammatory demyelinating polyneuropathy. Neurology, 61:1507-1512, Dec 2003. URL: https://doi.org/10.1212/01.wnl.0000096166.28131.4c, doi:10.1212/01.wnl.0000096166.28131.4c. This article has 137 citations and is from a highest quality peer-reviewed journal.

2. (oh2003subacuteinflammatorydemyelinating pages 3-4): S. J. Oh, K. Kurokawa, D. F. de Almeida, H. F. Ryan, and G. C. Claussen. Subacute inflammatory demyelinating polyneuropathy. Neurology, 61:1507-1512, Dec 2003. URL: https://doi.org/10.1212/01.wnl.0000096166.28131.4c, doi:10.1212/01.wnl.0000096166.28131.4c. This article has 137 citations and is from a highest quality peer-reviewed journal.

3. (bergh2021europeanacademyof pages 4-5): Peter Y. K. Van den Bergh, Pieter A. van Doorn, Robert D. M. Hadden, Bert Avau, Patrik Vankrunkelsven, Jeffrey A. Allen, Shahram Attarian, Patricia H. Blomkwist‐Markens, David R. Cornblath, Filip Eftimov, H. Stephan Goedee, Thomas Harbo, Satoshi Kuwabara, Richard A. Lewis, Michael P. Lunn, Eduardo Nobile‐Orazio, Luis Querol, Yusuf A. Rajabally, Claudia Sommer, and Haluk A. Topaloglu. European academy of neurology/peripheral nerve society guideline on diagnosis and treatment of chronic inflammatory demyelinating polyradiculoneuropathy: report of a joint task force—second revision. Journal of the Peripheral Nervous System, 26:242-268, Jul 2021. URL: https://doi.org/10.1111/jns.12455, doi:10.1111/jns.12455. This article has 1091 citations and is from a peer-reviewed journal.

4. (oh2003subacuteinflammatorydemyelinating pages 4-5): S. J. Oh, K. Kurokawa, D. F. de Almeida, H. F. Ryan, and G. C. Claussen. Subacute inflammatory demyelinating polyneuropathy. Neurology, 61:1507-1512, Dec 2003. URL: https://doi.org/10.1212/01.wnl.0000096166.28131.4c, doi:10.1212/01.wnl.0000096166.28131.4c. This article has 137 citations and is from a highest quality peer-reviewed journal.

5. (lewis2017chronicinflammatorydemyelinating pages 1-4): Richard A. Lewis. Chronic inflammatory demyelinating polyneuropathy. Current Opinion in Neurology, 30:508-512, Oct 2017. URL: https://doi.org/10.1097/wco.0000000000000481, doi:10.1097/wco.0000000000000481. This article has 83 citations and is from a peer-reviewed journal.

6. (alessandro2018differencesbetweenacute‐onset pages 1-8): Lucas Alessandro, José M. Pastor Rueda, Miguel Wilken, Luis Querol, Mariano Marrodán, Julián N. Acosta, Alberto Rivero, Fabio Barroso, and Mauricio F. Farez. Differences between acute‐onset chronic inflammatory demyelinating polyneuropathy and acute inflammatory demyelinating polyneuropathy in adult patients. Journal of the Peripheral Nervous System, 23:154-158, Jun 2018. URL: https://doi.org/10.1111/jns.12266, doi:10.1111/jns.12266. This article has 49 citations and is from a peer-reviewed journal.

7. (doorn2024challengesinthe media a605ddf1): Iris van Doorn, Filip Eftimov, Luuk Wieske, Ivo van Schaik, and Camiel Verhamme. Challenges in the early diagnosis and treatment of chronic inflammatory demyelinating polyradiculoneuropathy in adults: current perspectives. Therapeutics and Clinical Risk Management, 20:111-126, Feb 2024. URL: https://doi.org/10.2147/tcrm.s360249, doi:10.2147/tcrm.s360249. This article has 17 citations and is from a peer-reviewed journal.

8. (oh2003subacuteinflammatorydemyelinating pages 2-3): S. J. Oh, K. Kurokawa, D. F. de Almeida, H. F. Ryan, and G. C. Claussen. Subacute inflammatory demyelinating polyneuropathy. Neurology, 61:1507-1512, Dec 2003. URL: https://doi.org/10.1212/01.wnl.0000096166.28131.4c, doi:10.1212/01.wnl.0000096166.28131.4c. This article has 137 citations and is from a highest quality peer-reviewed journal.

9. (stino2021chronicinflammatorydemyelinating pages 1-3): Amro M. Stino, Elie Naddaf, Peter J. Dyck, and P. James B. Dyck. Chronic inflammatory demyelinating polyradiculoneuropathy—diagnostic pitfalls and treatment approach. Muscle & Nerve, 63:157-169, Sep 2021. URL: https://doi.org/10.1002/mus.27046, doi:10.1002/mus.27046. This article has 91 citations and is from a peer-reviewed journal.

10. (ramchandren2009chronicneuropathieschronicinflammatory pages 3-6): S Ramchandren and RA Lewis. Chronic neuropathies-chronic inflammatory demyelinating neuropathy and its variants. Unknown journal, 2009.

11. (doorn2024challengesinthe pages 1-2): Iris van Doorn, Filip Eftimov, Luuk Wieske, Ivo van Schaik, and Camiel Verhamme. Challenges in the early diagnosis and treatment of chronic inflammatory demyelinating polyradiculoneuropathy in adults: current perspectives. Therapeutics and Clinical Risk Management, 20:111-126, Feb 2024. URL: https://doi.org/10.2147/tcrm.s360249, doi:10.2147/tcrm.s360249. This article has 17 citations and is from a peer-reviewed journal.

12. (doorn2024challengesinthe pages 2-3): Iris van Doorn, Filip Eftimov, Luuk Wieske, Ivo van Schaik, and Camiel Verhamme. Challenges in the early diagnosis and treatment of chronic inflammatory demyelinating polyradiculoneuropathy in adults: current perspectives. Therapeutics and Clinical Risk Management, 20:111-126, Feb 2024. URL: https://doi.org/10.2147/tcrm.s360249, doi:10.2147/tcrm.s360249. This article has 17 citations and is from a peer-reviewed journal.

13. (kmezic2023validationofelevated pages 1-2): Ivan Kmezic, Rasmus Gustafsson, Katharina Fink, Anders Svenningsson, Kristin Samuelsson, Caroline Ingre, Tomas Olsson, Magnus Hansson, Ingrid Kockum, Milena Z. Adzemovic, and Rayomand Press. Validation of elevated levels of interleukin-8 in the cerebrospinal fluid, and discovery of new biomarkers in patients with gbs and cidp using a proximity extension assay. Frontiers in Immunology, Nov 2023. URL: https://doi.org/10.3389/fimmu.2023.1241199, doi:10.3389/fimmu.2023.1241199. This article has 11 citations and is from a peer-reviewed journal.

14. (kmezic2023validationofelevated pages 3-4): Ivan Kmezic, Rasmus Gustafsson, Katharina Fink, Anders Svenningsson, Kristin Samuelsson, Caroline Ingre, Tomas Olsson, Magnus Hansson, Ingrid Kockum, Milena Z. Adzemovic, and Rayomand Press. Validation of elevated levels of interleukin-8 in the cerebrospinal fluid, and discovery of new biomarkers in patients with gbs and cidp using a proximity extension assay. Frontiers in Immunology, Nov 2023. URL: https://doi.org/10.3389/fimmu.2023.1241199, doi:10.3389/fimmu.2023.1241199. This article has 11 citations and is from a peer-reviewed journal.

15. (ramchandren2009chronicneuropathieschronicinflammatory pages 1-3): S Ramchandren and RA Lewis. Chronic neuropathies-chronic inflammatory demyelinating neuropathy and its variants. Unknown journal, 2009.

16. (kmezic2025biomarkerandpathogenic pages 29-35): Ivan Kmezic. Biomarker and pathogenic study of immune-mediated neuropathies. Apr 2025. URL: https://doi.org/10.69622/28457924.v1, doi:10.69622/28457924.v1.

17. (dyck2018historydiagnosisand pages 2-3): P. James B. Dyck and Jennifer A. Tracy. History, diagnosis, and management of chronic inflammatory demyelinating polyradiculoneuropathy. Mayo Clinic Proceedings, 93:777–793, Jun 2018. URL: https://doi.org/10.1016/j.mayocp.2018.03.026, doi:10.1016/j.mayocp.2018.03.026. This article has 161 citations and is from a domain leading peer-reviewed journal.

18. (bunschoten2019progressindiagnosis pages 3-5): Carina Bunschoten, Bart C Jacobs, Peter Y K Van den Bergh, David R Cornblath, and Pieter A van Doorn. Progress in diagnosis and treatment of chronic inflammatory demyelinating polyradiculoneuropathy. The Lancet Neurology, 18:784-794, Aug 2019. URL: https://doi.org/10.1016/s1474-4422(19)30144-9, doi:10.1016/s1474-4422(19)30144-9. This article has 288 citations and is from a highest quality peer-reviewed journal.

19. (mathey2015chronicinflammatorydemyelinating pages 3-4): Emily K Mathey, Susanna B Park, Richard A C Hughes, John D Pollard, Patricia J Armati, Michael H Barnett, Bruce V Taylor, P James B Dyck, Matthew C Kiernan, and Cindy S-Y Lin. Chronic inflammatory demyelinating polyradiculoneuropathy: from pathology to phenotype. Journal of Neurology, Neurosurgery &amp; Psychiatry, 86:973-985, Feb 2015. URL: https://doi.org/10.1136/jnnp-2014-309697, doi:10.1136/jnnp-2014-309697. This article has 561 citations.

20. (doorn2024challengesinthe media 1489a645): Iris van Doorn, Filip Eftimov, Luuk Wieske, Ivo van Schaik, and Camiel Verhamme. Challenges in the early diagnosis and treatment of chronic inflammatory demyelinating polyradiculoneuropathy in adults: current perspectives. Therapeutics and Clinical Risk Management, 20:111-126, Feb 2024. URL: https://doi.org/10.2147/tcrm.s360249, doi:10.2147/tcrm.s360249. This article has 17 citations and is from a peer-reviewed journal.

21. (doorn2024challengesinthe media be7d2bb3): Iris van Doorn, Filip Eftimov, Luuk Wieske, Ivo van Schaik, and Camiel Verhamme. Challenges in the early diagnosis and treatment of chronic inflammatory demyelinating polyradiculoneuropathy in adults: current perspectives. Therapeutics and Clinical Risk Management, 20:111-126, Feb 2024. URL: https://doi.org/10.2147/tcrm.s360249, doi:10.2147/tcrm.s360249. This article has 17 citations and is from a peer-reviewed journal.

22. (doorn2024challengesinthe media b86e8bf0): Iris van Doorn, Filip Eftimov, Luuk Wieske, Ivo van Schaik, and Camiel Verhamme. Challenges in the early diagnosis and treatment of chronic inflammatory demyelinating polyradiculoneuropathy in adults: current perspectives. Therapeutics and Clinical Risk Management, 20:111-126, Feb 2024. URL: https://doi.org/10.2147/tcrm.s360249, doi:10.2147/tcrm.s360249. This article has 17 citations and is from a peer-reviewed journal.

23. (doorn2024challengesinthe media 87bdfab1): Iris van Doorn, Filip Eftimov, Luuk Wieske, Ivo van Schaik, and Camiel Verhamme. Challenges in the early diagnosis and treatment of chronic inflammatory demyelinating polyradiculoneuropathy in adults: current perspectives. Therapeutics and Clinical Risk Management, 20:111-126, Feb 2024. URL: https://doi.org/10.2147/tcrm.s360249, doi:10.2147/tcrm.s360249. This article has 17 citations and is from a peer-reviewed journal.

24. (kmezic2023validationofelevated pages 2-3): Ivan Kmezic, Rasmus Gustafsson, Katharina Fink, Anders Svenningsson, Kristin Samuelsson, Caroline Ingre, Tomas Olsson, Magnus Hansson, Ingrid Kockum, Milena Z. Adzemovic, and Rayomand Press. Validation of elevated levels of interleukin-8 in the cerebrospinal fluid, and discovery of new biomarkers in patients with gbs and cidp using a proximity extension assay. Frontiers in Immunology, Nov 2023. URL: https://doi.org/10.3389/fimmu.2023.1241199, doi:10.3389/fimmu.2023.1241199. This article has 11 citations and is from a peer-reviewed journal.

25. (kmezic2025biomarkerandpathogenic pages 41-44): Ivan Kmezic. Biomarker and pathogenic study of immune-mediated neuropathies. Apr 2025. URL: https://doi.org/10.69622/28457924.v1, doi:10.69622/28457924.v1.