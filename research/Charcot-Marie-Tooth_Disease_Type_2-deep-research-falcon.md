---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-04-11T12:32:46.160076'
end_time: '2026-04-11T12:32:46.161710'
duration_seconds: 0.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Charcot-Marie-Tooth Disease Type 2
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth Disease Type 2
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth Disease Type 2** covering all of the
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
- **Disease Name:** Charcot-Marie-Tooth Disease Type 2
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth Disease Type 2** covering all of the
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


## Comprehensive Research Report: Charcot–Marie–Tooth Disease Type 2 (CMT2)

### Scope and evidence basis
This report synthesizes evidence from (i) aggregated disease resources/ontologies accessed via OpenTargets (for MONDO mapping), (ii) recent peer‑reviewed reviews (2023–2024 prioritized), (iii) primary mechanistic studies (notably 2023–2024), (iv) clinical diagnostic cohort studies, and (v) ClinicalTrials.gov trial records. Where identifiers (e.g., Orphanet codes, MeSH, ICD-10/11) are not present in the retrieved full text, the report explicitly notes this limitation rather than inferring codes. Evidence type (human clinical, model organism, in vitro, registry) is indicated in‑line.


## 1. Disease Information

### 1.1 Disease overview (current understanding)
Charcot–Marie–Tooth disease (CMT) is a genetically heterogeneous inherited peripheral neuropathy characterized by length‑dependent, slowly progressive distal weakness/atrophy and sensory loss (often with pes cavus and reduced reflexes). CMT is traditionally classified by electrophysiology and pathology into demyelinating (CMT1), axonal (CMT2), and intermediate forms. (dong2024currenttreatmentmethods pages 1-2, okamoto2023thecurrentstate pages 1-2)

**CMT2 definition (electrophysiology):**
* Axonal CMT2 is distinguished from demyelinating CMT1 by relatively preserved motor nerve conduction velocities (NCV/MNCV) with evidence of axonal loss (reduced amplitudes). A commonly used discriminator in the arms is **NCV >38 m/s for axonal CMT2 vs <38 m/s for demyelinating CMT1**. (okamoto2023thecurrentstate pages 1-2)
* Alternative framework: demarcation can use ulnar motor nerve ranges: very slow <15 m/s; slow 15–35 m/s; intermediate 35–45 m/s; normal >45 m/s; axonal CMT2 typically lies in the normal/near‑normal range. (dong2024currenttreatmentmethods pages 1-2)

### 1.2 Key identifiers and ontology mapping
* **MONDO:** *Charcot‑Marie‑Tooth disease type 2* = **MONDO:0018993** (via OpenTargets disease mapping evidence). (dong2024currenttreatmentmethods pages 2-4)
* **OMIM:** Specific subtype example from a 2024 review: **CMT2A (MFN2) = OMIM 609260**. (abati2024charcot–marie‐toothtype2a pages 1-2)
* **MeSH / ICD‑10 / ICD‑11 / Orphanet:** Not explicitly provided in retrieved full‑text excerpts for CMT2 as a parent concept; therefore, these identifiers are **not populated here** from primary evidence in this run.

### 1.3 Synonyms and alternative names
* “Axonal CMT”, “axonal Charcot–Marie–Tooth disease”, and the legacy term **hereditary motor and sensory neuropathy type II (HMSN II)** are used in modern reviews as equivalents for CMT2. (dong2024currenttreatmentmethods pages 1-2, okamoto2023thecurrentstate pages 1-2)

### 1.4 Evidence provenance (individual vs aggregated)
* **Aggregated disease‑level resources:** ontology mapping (MONDO via OpenTargets), review articles synthesizing many cohorts. (dong2024currenttreatmentmethods pages 2-4, dong2024currenttreatmentmethods pages 1-2, okamoto2023thecurrentstate pages 1-2)
* **Individual‑level/primary evidence:** mechanistic studies in animal models and patient‑derived cells (e.g., MFN2 mutant fibroblasts; GARS1 mouse). (sleigh2023boostingperipheralbdnf pages 1-2, kumar2024mfn2coordinatesmitochondria pages 1-2)
* **Registry/EHR‑like data:** ClinicalTrials.gov registries and large observational registries collecting patient‑reported and medical records. (NCT05902351 chunk 1)


## 2. Etiology

### 2.1 Primary causal factors
CMT2 is primarily **genetic**: mutations in many genes affecting axonal maintenance, mitochondrial dynamics, axonal transport, cytoskeleton, endolysosomal trafficking, and translation/protein homeostasis. (okamoto2023thecurrentstate pages 1-2, dong2024currenttreatmentmethods pages 2-4)

### 2.2 Genetic risk factors (causal genes; selected major subtypes)
CMT2 is genetically heterogeneous; commonly cited genes/subtypes in the retrieved evidence include:
* **MFN2 (CMT2A)** – dominant in most cases; mitochondrial fusion/transport/ER–mitochondria tethering dysfunction. (abati2024charcot–marie‐toothtype2a pages 1-2, kumar2024mfn2coordinatesmitochondria pages 1-2)
* **GARS1 (CMT2D)** – dominant missense with toxic gain‑of‑function interactions affecting neurotrophin signaling/axonal transport. (sleigh2023boostingperipheralbdnf pages 1-2)
* **NEFL (CMT2E)** – neurofilament/cytoskeleton abnormalities. (dong2024currenttreatmentmethods pages 2-4)
* **HSPB1 (CMT2F)** – mitochondrial and neurofilament transport disruption. (dong2024currenttreatmentmethods pages 2-4)
* **IGHMBP2 (CMT2S)** – biallelic mutations affecting RNA helicase / translation pathways. (dong2024currenttreatmentmethods pages 2-4)
* **SORD‑related axonal neuropathy/CMT2** – biallelic loss‑of‑function; polyol pathway dysregulation with sorbitol accumulation. (estevezarias2022geneticapproachesand pages 13-16)

OpenTargets disease‑target association data support multiple CMT2‑associated targets (e.g., MFN2, MPZ, GDAP1, NEFL, HSPB1, TRPV4, DYNC1H1, AARS1) and links to curation/ClinVar evidence records. (dong2024currenttreatmentmethods pages 2-4)

### 2.3 Variant classes and functional consequences (examples)
* **SORD:** 2022 review notes **14 mutations** identified since initial description (May 2020), “**most are frameshift or splicing mutations causing a loss of function**”; a recurrent **c.757delG** appears in most reported patients. (estevezarias2022geneticapproachesand pages 13-16)
* **MFN2:** CMT2A is commonly caused by dominant MFN2 mutations; a 2024 review describes a likely **dominant‑negative mechanism** as frequent, and highlights both loss‑ and gain‑of‑function behavior in models. (abati2024charcot–marie‐toothtype2a pages 1-2)
* **GARS1:** 2023 mechanistic review/primary evidence frames pathogenicity as toxic gain‑of‑function due to conformational opening and aberrant interactions. (sleigh2023boostingperipheralbdnf pages 1-2)

### 2.4 Environmental risk factors / protective factors / gene–environment interactions
No high‑confidence, CMT2‑specific environmental risk or protective factors were identified in the retrieved sources for this run. Supportive statements focus on **exercise/physical activity benefits** and risks of sedentary behavior at a symptom‑management level (not disease causation). (leale2024telecoachingapotential pages 1-2)


## 3. Phenotypes (clinical manifestations)

### 3.1 Core phenotype spectrum
Common phenotype across CMT (including CMT2) includes:
* **Distal muscle weakness and atrophy** (lower limbs first), **foot drop**, pes cavus/hammertoes. (okamoto2023thecurrentstate pages 1-2, dong2024currenttreatmentmethods pages 1-2)
* **Distal sensory loss** often in a **stocking–glove distribution**. (okamoto2023thecurrentstate pages 1-2)
* **Reduced/absent tendon reflexes**; gait impairment and falls. (okamoto2023thecurrentstate pages 1-2, johnson2016managementofcharcot–marie–tooth pages 4-6)
* In some axonal forms, **pyramidal features** (e.g., extensor plantar responses, mild increased tone, preserved/increased reflexes) have been described in dominantly inherited axonal CMT2 variants. (dong2024currenttreatmentmethods pages 2-4)

### 3.2 Age of onset, severity, progression
* CMT can present at any age; CMT2 severity ranges from severe childhood onset to milder adolescent/adult onset. (stavrou2023charcot–marie–toothneuropathiescurrentgene pages 2-2, okamoto2023thecurrentstate pages 1-2)
* **SORD‑related axonal neuropathy/CMT2:** clinical homogeneity described as onset in the **2nd–3rd decade** with axonal neuropathy and distal weakness/atrophy. (estevezarias2022geneticapproachesand pages 13-16)

### 3.3 Phenotype frequencies (where available)
* Prognosis: “**fewer than 5% of patients affected by CMT1 or CMT2 neuropathies become wheelchair dependent, and the majority have a normal life span**.” (stavrou2023charcot–marie–toothneuropathiescurrentgene pages 2-2)

### 3.4 Quality of life (QoL) and functioning
CMT affects lifelong mobility and daily functioning; functional outcomes used in trials and rehab studies include 6‑minute walk test (6MWT), 10‑meter walk test (10MWT), Berg Balance Scale (BBS), Timed Up and Go (TUG), Overall Neuropathy Limitations Scale (ONLS), SF‑36, and disease‑specific instruments. (NCT06482437 chunk 1, tedeschi2025physicaltherapyinterventions pages 8-10)

### 3.5 Suggested HPO terms (not exhaustive)
Based on the phenotypes described in evidence:
* Pes cavus (HP:0001760)
* Hammer toe (HP:0001838)
* Distal muscle weakness (HP:0002460)
* Muscle atrophy (HP:0003202)
* Foot drop (HP:0001762)
* Hyporeflexia/Areflexia (HP:0001265 / HP:0001284)
* Distal sensory impairment (e.g., Hypoesthesia, HP:0001251)


## 4. Genetic / Molecular Information

### 4.1 Causal genes (selected, evidence-backed in this run)
Key CMT2 genes/subtypes supported in retrieved evidence include **MFN2 (CMT2A), GARS1 (CMT2D), NEFL (CMT2E), HSPB1 (CMT2F), IGHMBP2 (CMT2S), SORD**. (dong2024currenttreatmentmethods pages 2-4, sleigh2023boostingperipheralbdnf pages 1-2, abati2024charcot–marie‐toothtype2a pages 1-2, estevezarias2022geneticapproachesand pages 13-16)

### 4.2 Modifier genes / oligogenicity
Direct modifier genes were not robustly characterized in the retrieved excerpts. However, recent genetics reviews emphasize “missing heritability,” structural variation, and complex inheritance in inherited peripheral neuropathies, implying potential modifiers/oligogenic contributions in some families. (NCT06482437 chunk 1)

### 4.3 Epigenetics and chromosomal abnormalities
No CMT2‑specific epigenetic mechanisms or chromosomal abnormalities were directly supported by the retrieved evidence in this run.


## 5. Environmental Information
No specific infectious or toxin causes are supported for CMT2 (a genetic neuropathy). Environmental/lifestyle considerations primarily relate to **functional management** (exercise, orthotics) rather than etiology. (dong2024currenttreatmentmethods pages 4-6, leale2024telecoachingapotential pages 1-2)


## 6. Mechanism / Pathophysiology

### 6.1 Mechanistic themes across CMT2
Mechanistic themes in CMT and CMT2 include disrupted axonal transport, mitochondrial dynamics, vesicle trafficking, and translation/protein synthesis processes. (okamoto2023thecurrentstate pages 1-2, dong2024currenttreatmentmethods pages 2-4)

### 6.2 MFN2 / CMT2A (mitochondrial dynamics, axonal transport, microtubule acetylation)
**Causal chain (illustrative):** MFN2 mutation → impaired mitochondrial fusion / ER–mitochondria tethering / mitochondrial transport → altered mitochondrial distribution and axonal energy/calcium/lipid homeostasis → distal axonal degeneration (length‑dependent) → distal weakness/sensory loss.

Recent mechanistic advance (2024): MFN2 coordinates mitochondrial motility with **α‑tubulin acetylation** by recruiting the tubulin acetyltransferase **ATAT1** at mitochondria–microtubule contacts; CMT2A‑associated MFN2 mutations (R94W, T105M) alter binding and may cause axonal degeneration via dysregulated ATAT1 release and reduced acetylated tubulin. (kumar2024mfn2coordinatesmitochondria pages 1-2)

A 2024 review summarizes that MFN2 mutations disturb “the equilibrium between mitochondrial fusion and fission, of mitophagy and mitochondrial axonal transport,” and emphasizes lack of approved therapies. (abati2024charcot–marie‐toothtype2a pages 1-2)

### 6.3 GARS1 / CMT2D (toxic mis‑interactions; neurotrophin signaling endosome transport)
A 2023 primary study reports in vivo axonal transport disruption and a muscle‑targeted rescue concept:
* Abstract quote: “**CMT2D mice displayed early and persistent disturbances in axonal transport of neurotrophin-containing signaling endosomes in vivo**” and “**supplementation of muscles with BDNF… completely restored physiological axonal transport in neuropathic mice**.” (sleigh2023boostingperipheralbdnf pages 1-2)
This supports a mechanistic chain where mutant GlyRS disrupts neurotrophin receptor interactions (e.g., TrkB/BDNF axis) leading to impaired retrograde signaling endosome transport and downstream axonal pathology. (sleigh2023boostingperipheralbdnf pages 1-2)

### 6.4 SORD‑related axonal neuropathy (polyol pathway; sorbitol accumulation)
SORD encodes sorbitol dehydrogenase in the polyol pathway. Patient fibroblasts show complete loss of SORD protein and increased intracellular sorbitol; proposed mechanisms include osmotic stress, oxidative stress, and altered NADPH. (estevezarias2022geneticapproachesand pages 13-16)

### 6.5 Suggested GO biological process terms (illustrative)
* Mitochondrial fusion (GO:0008053)
* Mitophagy (GO:0000423)
* Axonal transport (GO:0098930)
* Microtubule acetylation (GO:0043473)
* Retrograde axonal transport (GO:0008089)
* Protein translation (GO:0006412)

### 6.6 Suggested Cell Ontology (CL) terms and affected cell types
Evidence emphasizes neuronal primary defects with length‑dependent vulnerability:
* Peripheral motor neurons (e.g., CL:0000100 motor neuron)
* Sensory neurons (e.g., CL:0000101 sensory neuron)
* Schwann cells also contribute across CMT broadly (review context). (dong2024currenttreatmentmethods pages 1-2, stavrou2023charcot–marie–toothneuropathiescurrentgene pages 2-2)


## 7. Anatomical Structures Affected

### 7.1 Organ/system level
* **Peripheral nervous system** (primary) with length‑dependent distal involvement; clinical manifestations reflect degeneration of long peripheral axons. (stavrou2023charcot–marie–toothneuropathiescurrentgene pages 2-2, kumar2024mfn2coordinatesmitochondria pages 1-2)
* **Musculoskeletal system** (secondary consequences): foot deformities (pes cavus/hammertoes), muscle atrophy (tibialis anterior/peroneal muscles, intrinsic hand muscles). (dong2024currenttreatmentmethods pages 1-2)

### 7.2 Tissue/cell level
* Peripheral axons (motor and sensory), neuromuscular junction involvement in some inherited motor neuropathies (overlap). (stavrou2023charcot–marie–toothneuropathiescurrentgene pages 2-2, sleigh2023boostingperipheralbdnf pages 1-2)

### 7.3 Suggested UBERON terms (illustrative)
* Peripheral nerve (UBERON:0001630)
* Sciatic nerve (UBERON:0001323) (model‑system relevance). (sleigh2023boostingperipheralbdnf pages 1-2)
* Skeletal muscle of lower limb (UBERON:0002389) (clinical and therapeutic relevance). (sleigh2023boostingperipheralbdnf pages 1-2)


## 8. Temporal Development

### 8.1 Onset patterns
CMT2 can begin in childhood through adulthood; severity spectrum includes early severe vs later milder disease. (stavrou2023charcot–marie–toothneuropathiescurrentgene pages 2-2)

### 8.2 Progression
Generally slowly progressive length‑dependent neuropathy; disability accumulates over time. (dong2024currenttreatmentmethods pages 1-2, okamoto2023thecurrentstate pages 1-2)


## 9. Inheritance and Population

### 9.1 Epidemiology (recently cited statistics)
* CMT overall prevalence often cited as **~1:2,500**. (dong2024currenttreatmentmethods pages 1-2)
* Another review summarizes more recent prevalence figures of **~1:3,300 worldwide**. (scherrer2025frominvivo pages 1-3)
* A 2023 treatment review reports an “estimated incidence” of **10–40 per 100,000 individuals**. (okamoto2023thecurrentstate pages 1-2)

### 9.2 Proportion of CMT2 and key subtypes
* CMT2 share: one retrieved source states CMT2 is predicted to account for **15–30% of all CMT**. (koenig2025restoringproteinsynthesis pages 21-25)
* CMT2A proportion: “predominant axonal subtype… **~4–7% of all cases**.” (dong2024currenttreatmentmethods pages 2-4)
* Cohort breakdown (Saporta cohort summarized in 2023 review): among genetically defined cases, **CMT2A (MFN2) 4%**. (okamoto2023thecurrentstate pages 1-2)
* Commercial lab cohort summarized in 2023 review: **MFN2 4.3%** of positive genetic findings; 94.9% of positives were in PMP22, GJB1, MPZ, MFN2. (okamoto2023thecurrentstate pages 1-2)

### 9.3 Inheritance
CMT2 includes autosomal dominant and autosomal recessive forms depending on subtype (e.g., MFN2 often dominant; SORD recessive). (dong2024currenttreatmentmethods pages 2-4, estevezarias2022geneticapproachesand pages 13-16)


## 10. Diagnostics

### 10.1 Clinical and electrophysiologic testing
* Key electrophysiology concept: demyelinating vs axonal classification by motor nerve conduction velocities; axonal CMT2 tends toward preserved velocities with axonal loss signatures. (okamoto2023thecurrentstate pages 1-2, johnson2016managementofcharcot–marie–tooth pages 4-6)

### 10.2 Genetic testing strategies (current practice)
High‑impact recent diagnostic evidence:
* **Targeted NGS panels (clinical practice):** In a Neurology (2020) diagnostic cohort of 220 patients, a “definite molecular diagnosis… **30%**” was achieved; an additional **33%** had VUS. (cortese2020targetednextgenerationsequencing pages 1-2)
* **Differential diagnostic yields by subtype:** A Nature Reviews Neurology (2019) review reports genetic diagnosis rates: **CMT1 >85%**, **CMT2 25–35%**, HSN 30–40%, HMN 15–25%. (pipis2019nextgenerationsequencingin pages 1-5)
* **Four‑gene dominance:** A 2020 review reports that analysis of **PMP22, GJB1, MPZ, MFN2** can identify **80–90%** of detectable CMT mutations, but that axonal CMT2 remains less frequently solved (10–30%). (rudnikschoneborn2020charcotmarietoothdiseaseand pages 1-2)

**WES/WGS (next frontier):** A high‑impact review summarizes that WGS offers ~**98.4–100% coding coverage** vs WES up to ~**96%**, and can detect structural variants with non‑exonic breakpoints; the review also notes mitochondrial sequencing should be considered because MT‑ATP6 can present as CMT2. (pipis2019nextgenerationsequencingin pages 10-14)

### 10.3 Differential diagnosis
Reassessment studies highlight that clinically diagnosed hereditary neuropathy can include treatable non‑genetic etiologies (e.g., inflammatory neuropathy) and benefit from comprehensive workup and sequencing, emphasizing the importance of careful differential diagnosis. (NCT06482437 chunk 1)


## 11. Outcomes / Prognosis
* Wheelchair dependence is uncommon: “**fewer than 5%** … become wheelchair dependent” and most have normal lifespan. (stavrou2023charcot–marie–toothneuropathiescurrentgene pages 2-2)
* Functional progression is variable by subtype and onset age, with severe childhood-onset forms and milder adult-onset forms. (stavrou2023charcot–marie–toothneuropathiescurrentgene pages 2-2)


## 12. Treatment

### 12.1 Current standard of care (real‑world implementations)
Recent 2024 treatment review statement: “**Currently, there are no approved disease management methods that can fully cure patients with CMT, and rehabilitation, orthotics, and surgery are the only available treatments to ameliorate symptoms**.” (dong2024currenttreatmentmethods pages 1-2)

**Rehabilitation and exercise**
* A 2025 scoping review (search through March 2024) identified 11 studies (including 2 RCTs) of gait/balance rehab; reported improvements included, for example, **6MWT 513 m → 580 m** over 8 months and **10MWT 9.2±2.1 s → 7.8±1.9 s** after a 3‑week intensive program (p<0.05). (tedeschi2025physicaltherapyinterventions pages 8-10)
* Orthotics: a 2024 review recommends escalation from shoe inserts to **ankle‑foot orthoses (AFOs)** for foot drop/calf weakness to stabilize gait and reduce pain/deformity. (dong2024currenttreatmentmethods pages 4-6)

**Telecoaching / digital rehabilitation**
A 2024 systematic review of telecoaching in CMT screened 382 records and included 7 studies (170 patients age 11–45). It reports improvements in strength, cardiovascular ability, gait, and fatigue but emphasizes small samples and moderate study quality. Quantitative protocol details include resistance‑training intensities (e.g., 50%→70% 1RM in one study) and pediatric 24‑week programs with reported dorsiflexion benefit. (leale2024telecoachingapotential pages 2-3)

### 12.2 Emerging / experimental therapies relevant to CMT2

**(i) Genotype‑targeted small molecule / metabolic strategy: SORD‑CMT2**
* **Epalrestat (aldose reductase inhibitor)** is being studied in genetically confirmed SORD‑CMT2 in a Phase 2 interventional trial (China): **NCT05777226** (not yet recruiting). Primary endpoints include **serum sorbitol** and **ONLS** changes over 36 months; dosing is **50 mg orally three times daily** in the treatment group. (NCT05777226 chunk 1)

**(ii) ASO therapy: CMT2S (IGHMBP2)**
* **VCA‑894A intrathecal antisense oligonucleotide** is being tested as an N‑of‑1 Phase 1/2 study: **NCT07223632** (active not recruiting). Endpoints include safety plus functional scales (RULM, HFMSE) and a molecular endpoint (IGHMBP2 mRNA in CSF/blood). (NCT07223632 chunk 1)

**(iii) Non–gene-specific symptomatic/modulator trial including CMT2**
* **NMD670** (SYNAPSE‑CMT; Phase 2a, randomized triple‑masked; completed): **NCT06482437**, with primary endpoint change in **6MWT distance** after 21 days; includes genetically confirmed CMT1 or CMT2. (NCT06482437 chunk 1)

**(iv) MFN2/CMT2A gene therapy concepts (preclinical)**
* A 2024 review emphasizes no approved therapy for CMT2A and the need for robust models. (abati2024charcot–marie‐toothtype2a pages 1-2)
* A combined **RNA interference + gene replacement** strategy is described (patient iPSC‑derived motor neurons and mouse model delivery). Quoted from the retrieved mechanistic summary: the approach “**effectively silenced the mutant MFN2 and restored functional wild-type MFN2 levels**” and corrected mitochondrial distribution/mitophagy in vitro; in vivo molecular correction was shown but early toxicity in some models motivates dosing/capsid optimization. (abati2024invivoanda pages 111-114)

### 12.3 MAXO term suggestions (illustrative)
* Physical therapy (MAXO:0000011)
* Orthotic device therapy (MAXO:0000756)
* Genetic counseling (MAXO:0000071)
* Antisense oligonucleotide therapy (MAXO:—; depends on MAXO version)


## 13. Prevention
CMT2 is not preventable in the primary prevention sense (genetic etiology). Prevention is largely:
* **Secondary prevention:** early detection via family history and genetic testing; cascade testing.
* **Tertiary prevention:** preventing complications via orthotics, rehabilitation, fall prevention, and long‑term multidisciplinary care. (dong2024currenttreatmentmethods pages 4-6, tedeschi2025physicaltherapyinterventions pages 8-10)


## 14. Other Species / Natural Disease
No naturally occurring non‑human disease analogs were directly supported in the retrieved evidence for this run. However, mechanistic understanding relies heavily on engineered models and comparative biology of conserved pathways (mitochondrial dynamics, axonal transport). (abati2024charcot–marie‐toothtype2a pages 1-2)


## 15. Model Organisms
CMT2 mechanistic and translational work uses diverse models:
* **Mouse models** (prominent for CMT2A) emphasized as “most versatile” for mechanistic dissection and translational studies. (abati2024charcot–marie‐toothtype2a pages 1-2)
* **Drosophila** and **zebrafish** models are described for MFN2/CMT2A in vivo phenotyping and mechanism. (abati2024charcot–marie‐toothtype2a pages 1-2)
* **Patient‑derived iPSC motor neurons** are used for genotype‑specific phenotyping and therapy testing (MFN2 RNAi+replacement approach). (abati2024invivoanda pages 111-114)


## Figures and Tables (evidence-supported visuals)
* A CMT classification/gene table and a schematic of molecular mechanisms were extracted from Dong et al., 2024 (Table 1 and Figure 2). These visuals consolidate subtype–gene mapping and the mechanistic categories relevant to axonal CMT2 (including MFN2/CMT2A). (dong2024currenttreatmentmethods media 63deef45, dong2024currenttreatmentmethods media 098aab8b)


## Expert synthesis / analysis (authoritative perspectives)
Recent authoritative reviews converge on several points:
1. **Genetic heterogeneity is the central barrier** to universal CMT therapies; most treatment development is subtype‑targeted or pathway‑targeted (e.g., mitochondrial dynamics, axonal transport, translation). (okamoto2023thecurrentstate pages 1-2, dong2024currenttreatmentmethods pages 2-4)
2. **Axonal CMT2 is systematically harder to genetically solve** than demyelinating CMT1 in clinical practice (CMT2 ~25–35% vs CMT1 >85% genetic diagnosis in some series), motivating reanalysis, better SV detection, and WGS adoption. (pipis2019nextgenerationsequencingin pages 1-5, pipis2019nextgenerationsequencingin pages 10-14)
3. The **treatment landscape for CMT2 is transitioning** from purely supportive care toward **genotype‑specific interventions** (ASOs for CMT2S, metabolic pathway targeting for SORD‑CMT2, preclinical MFN2 gene therapy concepts), but clinical evidence remains early-stage. (NCT05777226 chunk 1, NCT07223632 chunk 1, abati2024invivoanda pages 111-114)


## Key abstract-supported quotes (for knowledge base evidence items)
* CMT2 (axonal) diagnostic definition: “**A consistent slow NCV of < 38 m/s… represents the demyelinating form of CMT1, whereas a value >38 m/s is distinctive of the axonal form of CMT2.**” (Genes 2023). (okamoto2023thecurrentstate pages 1-2)
* CMT2D mechanism/therapy hypothesis: “**CMT2D mice displayed early and persistent disturbances in axonal transport of neurotrophin-containing signaling endosomes in vivo**” and “**supplementation of muscles with BDNF… completely restored physiological axonal transport**.” (JCI Insight 2023). (sleigh2023boostingperipheralbdnf pages 1-2)
* MFN2/CMT2A mechanism: “**MFN2 coordinates mitochondria motility with α-tubulin acetylation and this regulation is disrupted in CMT2A**.” (iScience 2024). (kumar2024mfn2coordinatesmitochondria pages 1-2)


## Embedded structured summary artifacts
The following tables provide a compact, knowledge‑base‑friendly summary of identifiers/definitions and the most relevant quantitative statistics and trials.

| Section | Item | Details | Key evidence |
|---|---|---|---|
| Disease ID/definition | Preferred name | Charcot-Marie-Tooth disease type 2 (CMT2), an axonal form of inherited peripheral neuropathy affecting peripheral axons/neurons more than myelin (stavrou2023charcot–marie–toothneuropathiescurrentgene pages 2-2, dong2024currenttreatmentmethods pages 1-2, okamoto2023thecurrentstate pages 1-2) | Axonal hereditary neuropathy with distal weakness, sensory loss, and length-dependent degeneration (stavrou2023charcot–marie–toothneuropathiescurrentgene pages 2-2, dong2024currenttreatmentmethods pages 1-2, okamoto2023thecurrentstate pages 1-2) |
| Disease ID/definition | MONDO ID | MONDO:0018993 (dong2024currenttreatmentmethods pages 2-4) | Open Targets disease mapping to Charcot-Marie-Tooth disease type 2 (dong2024currenttreatmentmethods pages 2-4) |
| Disease ID/definition | One-line definition | Genetically heterogeneous inherited sensorimotor neuropathy in which primary pathology is axonal degeneration, typically causing slowly progressive distal weakness/atrophy, sensory loss, pes cavus, and reduced reflexes (dong2024currenttreatmentmethods pages 1-2, okamoto2023thecurrentstate pages 1-2) | Broad modern review definition of CMT with CMT2 as the axonal subgroup (dong2024currenttreatmentmethods pages 1-2, okamoto2023thecurrentstate pages 1-2) |
| Disease ID/definition | Key synonyms | Axonal CMT; axonal Charcot-Marie-Tooth disease; hereditary motor and sensory neuropathy type II / HMSN II (legacy terminology); inherited axonal peripheral neuropathy (dong2024currenttreatmentmethods pages 1-2, okamoto2023thecurrentstate pages 1-2) | Reviews classify CMT2 as the axonal subtype of CMT/HMSN (dong2024currenttreatmentmethods pages 1-2, okamoto2023thecurrentstate pages 1-2) |
| Distinguishing diagnostics | Electrophysiology threshold | Arm/forearm motor NCV/MNCV typically >38 m/s supports axonal CMT2 versus <38 m/s for demyelinating CMT1 (okamoto2023thecurrentstate pages 1-2) | “A consistent slow NCV of < 38 m/s… CMT1, whereas a value >38 m/s is distinctive of the axonal form of CMT2” (okamoto2023thecurrentstate pages 1-2) |
| Distinguishing diagnostics | Alternative electrophysiology framework | Ulnar motor nerve ranges: very slow <15 m/s; slow 15–35 m/s; intermediate 35–45 m/s; normal >45 m/s; CMT2 generally falls in normal/near-normal axonal range while intermediate CMT overlaps 35–45 m/s (dong2024currenttreatmentmethods pages 1-2) | Modern classification framework for inherited neuropathies (dong2024currenttreatmentmethods pages 1-2) |
| Distinguishing diagnostics | Clinical distinction vs CMT1 | CMT2 is primarily axonal, often with preserved or only mildly slowed conduction velocities relative to CMT1, but reduced amplitudes and length-dependent distal weakness/sensory loss; CMT1 is primarily demyelinating with markedly slowed velocities (stavrou2023charcot–marie–toothneuropathiescurrentgene pages 2-2, dong2024currenttreatmentmethods pages 1-2, okamoto2023thecurrentstate pages 1-2) | Disease classification based on NCV plus primary defect (stavrou2023charcot–marie–toothneuropathiescurrentgene pages 2-2, dong2024currenttreatmentmethods pages 1-2, okamoto2023thecurrentstate pages 1-2) |
| Common CMT2 genes/subtypes | CMT2A / MFN2 | Usually AD or de novo dominant; rarer recessive or semidominant cases reported; most common axonal subtype / predominant CMT2 subtype (abati2024charcot–marie‐toothtype2a pages 1-2, dong2024currenttreatmentmethods pages 2-4, okamoto2023thecurrentstate pages 2-4) | Mitochondrial fusion/fission imbalance, mitophagy defects, impaired axonal mitochondrial transport, ER-mitochondria contact dysfunction, mtDNA/OXPHOS impairment (abati2024charcot–marie‐toothtype2a pages 1-2, dong2024currenttreatmentmethods pages 2-4, kumar2024mfn2coordinatesmitochondria pages 1-2) |
| Common CMT2 genes/subtypes | CMT2D / GARS1 | AD dominant missense neuropathy (dong2024currenttreatmentmethods pages 2-4, sleigh2023boostingperipheralbdnf pages 1-2) | Toxic gain-of-function GlyRS conformational opening; aberrant Nrp1/VEGF signaling; TrkB/BDNF pathway disruption; impaired axonal transport; protein synthesis stress/ISR activation (dong2024currenttreatmentmethods pages 2-4, sleigh2023boostingperipheralbdnf pages 1-2) |
| Common CMT2 genes/subtypes | CMT2E / NEFL | Usually AD (gene repeatedly curated as a CMT2 gene) (dong2024currenttreatmentmethods pages 2-4) | Reduced neurofilament expression in cutaneous nerve fibers, altered axonal caliber, reduced conduction velocity / cytoskeletal dysfunction (dong2024currenttreatmentmethods pages 2-4) |
| Common CMT2 genes/subtypes | CMT2F / HSPB1 | Usually AD (gene repeatedly curated as a CMT2 gene) (dong2024currenttreatmentmethods pages 2-4) | Mutant HSP27/HSPB1 lowers mitochondrial ceramide, alters mitochondrial structure/function, causes neurofilament hyperphosphorylation and impaired anterograde NF transport (dong2024currenttreatmentmethods pages 2-4) |
| Common CMT2 genes/subtypes | CMT2S / IGHMBP2 | AR, biallelic variants (dong2024currenttreatmentmethods pages 2-4, NCT07223632 chunk 1) | ATP-dependent 5′→3′ RNA helicase dysfunction; disturbed association with ribosomal proteins, pre-rRNA processing factors, and tRNA-related species; transcription/translation defects (dong2024currenttreatmentmethods pages 2-4) |
| Common CMT2 genes/subtypes | SORD-related axonal neuropathy | AR, biallelic loss-of-function variants; SORD-related CMT2/dHMN (estevezarias2022geneticapproachesand pages 13-16, NCT05777226 chunk 1) | Polyol-pathway defect with sorbitol dehydrogenase loss, intracellular sorbitol accumulation, proposed osmotic/oxidative stress and NADPH depletion; c.757delG common founder-like recurrent variant (estevezarias2022geneticapproachesand pages 13-16, NCT05777226 chunk 1) |
| Common CMT2 genes/subtypes | Other recurrent genes highlighted in evidence | MPZ, GDAP1, MME, TRPV4, RAB7A, MORC2, DYNC1H1, AARS1 also appear among curated/associated CMT2 genes (dong2024currenttreatmentmethods pages 2-4) | Mechanistic themes across CMT2: axonal transport failure, mitochondrial dysfunction, endolysosomal trafficking defects, cytoskeletal disruption, translation defects (dong2024currenttreatmentmethods pages 2-4, okamoto2023thecurrentstate pages 1-2) |


*Table: This table summarizes core identifiers, diagnostic electrophysiology criteria, and the major CMT2 genes/subtypes highlighted in the evidence base. It is useful as a compact reference for disease definition, differential diagnosis from demyelinating CMT, and mechanism-oriented subtype mapping.*

| Item | Statistic/Design | Population | Key endpoints/outcomes | Source (include DOI/URL and year where available) | Evidence type |
|---|---|---|---|---|---|
| CMT prevalence estimate | ~1:2,500 prevalence | General CMT population | Widely cited prevalence estimate for inherited CMT overall; useful upper-bound benchmark when contextualizing CMT2 burden (dong2024currenttreatmentmethods pages 1-2, scherrer2025frominvivo pages 1-3) | Biomolecules 2024, DOI: https://doi.org/10.3390/biom14091138 (2024); Journal of Tissue Engineering, DOI: https://doi.org/10.1177/20417314241310508 (2025) | Review |
| CMT prevalence estimate | ~1:3,300 worldwide | General CMT population | More recent global prevalence estimate reported in review literature; complements older 1:2,500 estimate (scherrer2025frominvivo pages 1-3) | Journal of Tissue Engineering, DOI: https://doi.org/10.1177/20417314241310508 (2025) | Review |
| CMT incidence estimate | 10–40 per 100,000 individuals | General CMT population | Review reports population frequency/incidence-style estimate for CMT overall; often cited in modern treatment reviews (okamoto2023thecurrentstate pages 1-2) | Genes 2023, DOI: https://doi.org/10.3390/genes14071391 (2023) | Review |
| CMT2 proportion among CMT | 15–30% of all CMT cases | General CMT/CMT2 | Axonal CMT2 estimated share of overall CMT burden (koenig2025restoringproteinsynthesis pages 21-25) | Koenig 2025, unpublished/unknown journal in retrieved context (2025) | Mechanistic study/review background |
| CMT2A proportion among all CMT | ~4–7% of all CMT cases | General CMT; CMT2A | CMT2A identified as predominant axonal subtype; useful for subtype prioritization in diagnostics and trials (dong2024currenttreatmentmethods pages 2-4) | Biomolecules 2024, DOI: https://doi.org/10.3390/biom14091138 (2024) | Review |
| CMT2A proportion in genetically defined clinical cohort | 4% of genetically defined CMT cases | Saporta cohort: 787/1024 diagnosed with CMT; 527 genetically defined | Among genetically defined cases: CMT1A 55%, CMTX1 15.2%, HNPP 9.2%, CMT1B 8.5%, CMT2A 4% (okamoto2023thecurrentstate pages 1-2) | Genes 2023, DOI: https://doi.org/10.3390/genes14071391 (2023) | Review citing cohort |
| MFN2 share among positive commercial genetic tests | 4.3% of positive genetic findings | 17,880 patients tested in commercial lab; 3,312 positive | PMP22 duplication/deletion predominated; MFN2 accounted for 4.3% of positive findings (okamoto2023thecurrentstate pages 1-2) | Genes 2023, DOI: https://doi.org/10.3390/genes14071391 (2023) | Review citing cohort |
| Gene panel diagnostic yield | 30% definite molecular diagnosis | 220 patients from 2 tertiary centers after targeted NGS panel | Definite diagnosis in 30%; VUS in 33%; mutations in GJB1, MFN2, MPZ comprised 39% of solved cases; CNVs in PMP22/MPZ/MFN2/SH3TC2/FDG4 also detected (cortese2020targetednextgenerationsequencing pages 1-2) | Neurology 2020, DOI: https://doi.org/10.1212/WNL.0000000000008672 (2020) | Clinical diagnostic cohort |
| Mutation detection rates by subtype | CMT1 >85%; CMT2 25–35%; HSN 30–40%; HMN 15–25% | Clinically diagnosed inherited neuropathy subgroups | Demonstrates markedly lower solve rate in axonal CMT2 than demyelinating CMT1, supporting broader sequencing and reanalysis (pipis2019nextgenerationsequencingin pages 1-5) | Nat Rev Neurol 2019, DOI: https://doi.org/10.1038/s41582-019-0254-5 (2019) | Review |
| Mutation detection rates by subtype (alternative summary) | CMT1 up to ~80%; CMT2 ~10–30% | CMT subgroups | Four-gene testing (PMP22, GJB1, MPZ, MFN2) identifies 80–90% of detectable mutations overall, but axonal CMT2 remains much harder to solve genetically (rudnikschoneborn2020charcotmarietoothdiseaseand pages 1-2) | Medizinische Genetik 2020, DOI: https://doi.org/10.1515/medgen-2020-2038 (2020) | Review |
| WES/WGS strategy | WES yield 19–45% in previously negative cases; WGS offers ~98.4–100% coding coverage vs WES up to ~96% | Unsolved CMT cohorts | WGS can detect structural variants and improve coverage; mitochondrial sequencing should be considered because MT-ATP6 can present as CMT2 (pipis2019nextgenerationsequencingin pages 10-14, pipis2019nextgenerationsequencingin pages 5-10) | Nat Rev Neurol 2019, DOI: https://doi.org/10.1038/s41582-019-0254-5 (2019) | Review |
| NCT05777226: epalrestat in SORD-CMT2 | Phase 2; multicenter; non-randomized; parallel; open-label; estimated n=30 | Genetically confirmed SORD-CMT2, age >14 to ≤50 years | Epalrestat 50 mg orally three times daily for 36 months vs no intervention; primary endpoints: serum sorbitol and ONLS change; secondary: 10MWRT (NCT05777226 chunk 1) | ClinicalTrials.gov NCT05777226, https://clinicaltrials.gov/study/NCT05777226 (posted 2023-03-21; updated 2023-04-18) | Clinical trial registry |
| NCT06482437: NMD670 in CMT1/CMT2 | Phase 2a; randomized; triple-masked; placebo-controlled; completed; n=81 | Ambulatory adults with genetically confirmed CMT type 1 or 2 | NMD670 tablets twice daily for 21 days; primary endpoint: change in 6MWT distance; secondary endpoints include CMT-FOM, 10MW/RT, fatigue index, ONLS, CMT-HI, SF-36, jitter/blocking, safety (NCT06482437 chunk 1) | ClinicalTrials.gov NCT06482437, https://clinicaltrials.gov/study/NCT06482437 (2024) | Clinical trial registry |
| NCT07223632: VCA-894A in CMT2S | Phase 1/2; N-of-1; open-label; single-center; active-not-recruiting; n=1 | Genetically confirmed CMT2S with IGHMBP2 c.1235+894C>A | Intrathecal ASO VCA-894A; primary endpoints: safety, RULM change, HFMSE change; secondary: IGHMBP2 mRNA rescue in CSF/blood (NCT07223632 chunk 1) | ClinicalTrials.gov NCT07223632, https://clinicaltrials.gov/study/NCT07223632 (first posted 2025-11-03) | Clinical trial registry |
| MFN2/CMT2A RNAi + gene replacement | Preclinical combined RNAi + gene replacement; AAV9 CSF delivery in mouse model; iPSC motor neurons in vitro | CMT2A patient-specific iPSC-derived motor neurons; MitoCharc1 mouse / MFN2 models | Silenced endogenous mutant MFN2 and restored WT MFN2; rescued altered axonal mitochondrial distribution and abnormal mitophagy in vitro; molecular correction confirmed in vivo, but toxicity concerns noted in some models (abati2024invivoanda pages 111-114, abati2024invivoand pages 111-114) | Cell Mol Life Sci 2023, DOI: https://doi.org/10.1007/s00018-023-05018-w (2023); Abati thesis/context 2024 | Mechanistic study |
| Rehabilitation / supportive management relevant to CMT2 | Multimodal rehab; orthotics; no approved curative pharmacotherapy | Broad CMT population including CMT2 | Reviews emphasize rehabilitation, orthotics, and surgery as current mainstay symptom management; tailored exercise may improve gait, balance, fatigue, and QoL (dong2024currenttreatmentmethods pages 1-2, tedeschi2025physicaltherapyinterventions pages 8-10, dong2024currenttreatmentmethods pages 4-6) | Biomolecules 2024, DOI: https://doi.org/10.3390/biom14091138 (2024); Life 2025, DOI: https://doi.org/10.3390/life15071036 (2025) | Review / scoping review |


*Table: This table summarizes the key numerical burden estimates, diagnostic yields, and active or recent therapy studies most relevant to Charcot-Marie-Tooth disease type 2. It is useful for quickly comparing population statistics, genetic testing performance, and the current interventional landscape for CMT2 subtypes.*


References

1. (dong2024currenttreatmentmethods pages 1-2): Hongxian Dong, Boquan Qin, Hui Zhang, Lei Lei, and Shizhou Wu. Current treatment methods for charcot–marie–tooth diseases. Biomolecules, 14:1138, Sep 2024. URL: https://doi.org/10.3390/biom14091138, doi:10.3390/biom14091138. This article has 9 citations.

2. (okamoto2023thecurrentstate pages 1-2): Yuji Okamoto and Hiroshi Takashima. The current state of charcot–marie–tooth disease treatment. Genes, 14:1391, Jul 2023. URL: https://doi.org/10.3390/genes14071391, doi:10.3390/genes14071391. This article has 56 citations.

3. (dong2024currenttreatmentmethods pages 2-4): Hongxian Dong, Boquan Qin, Hui Zhang, Lei Lei, and Shizhou Wu. Current treatment methods for charcot–marie–tooth diseases. Biomolecules, 14:1138, Sep 2024. URL: https://doi.org/10.3390/biom14091138, doi:10.3390/biom14091138. This article has 9 citations.

4. (abati2024charcot–marie‐toothtype2a pages 1-2): Elena Abati, Mafalda Rizzuti, Alessia Anastasia, Giacomo Pietro Comi, Stefania Corti, and Federica Rizzo. Charcot–marie‐tooth type 2a in vivo models: current updates. Journal of Cellular and Molecular Medicine, May 2024. URL: https://doi.org/10.1111/jcmm.18293, doi:10.1111/jcmm.18293. This article has 6 citations and is from a peer-reviewed journal.

5. (sleigh2023boostingperipheralbdnf pages 1-2): James N. Sleigh, David Villarroel-Campos, Sunaina Surana, Tahmina Wickenden, Yao Tong, Rebecca L. Simkin, Jose Norberto S. Vargas, Elena R. Rhymes, Andrew P. Tosolini, Steven J. West, Qian Zhang, Xiang-Lei Yang, and Giampietro Schiavo. Boosting peripheral bdnf rescues impaired in vivo axonal transport in cmt2d mice. JCI Insight, May 2023. URL: https://doi.org/10.1172/jci.insight.157191, doi:10.1172/jci.insight.157191. This article has 24 citations and is from a domain leading peer-reviewed journal.

6. (kumar2024mfn2coordinatesmitochondria pages 1-2): Atul Kumar, Delfina Larrea, Maria Elena Pero, Paola Infante, Marilisa Conenna, Grace J. Shin, Vincent Van Elias, Wesley B. Grueber, Lucia Di Marcotullio, Estela Area-Gomez, and Francesca Bartolini. Mfn2 coordinates mitochondria motility with α-tubulin acetylation and this regulation is disrupted in cmt2a. iScience, 27:109994, Jun 2024. URL: https://doi.org/10.1016/j.isci.2024.109994, doi:10.1016/j.isci.2024.109994. This article has 13 citations and is from a peer-reviewed journal.

7. (NCT05902351 chunk 1):  Natural History Study for Charcot Marie Tooth Disease. Hereditary Neuropathy Foundation. 2013. ClinicalTrials.gov Identifier: NCT05902351

8. (estevezarias2022geneticapproachesand pages 13-16): Berta Estévez-Arias, Laura Carrera-García, Andrés Nascimento, Lara Cantarero, Janet Hoenicka, and Francesc Palau. Genetic approaches and pathogenic pathways in the clinical management of charcot-marie-tooth disease. Journal of Translational Genetics and Genomics, 6:333-352, Jan 2022. URL: https://doi.org/10.20517/jtgg.2022.04, doi:10.20517/jtgg.2022.04. This article has 11 citations.

9. (leale2024telecoachingapotential pages 1-2): Ignazio Leale, Vincenzo Di Stefano, Carola Costanza, Filippo Brighina, Michele Roccella, Antonio Palma, and Giuseppe Battaglia. Telecoaching: a potential new training model for charcot-marie-tooth patients: a systematic review. Frontiers in Neurology, May 2024. URL: https://doi.org/10.3389/fneur.2024.1359091, doi:10.3389/fneur.2024.1359091. This article has 12 citations and is from a peer-reviewed journal.

10. (johnson2016managementofcharcot–marie–tooth pages 4-6): Nicholas Johnson, Donald McCorquodale, and Evan Pucillo. Management of charcot–marie–tooth disease: improving long-term care with a multidisciplinary approach. Journal of Multidisciplinary Healthcare, 9:7-19, Jan 2016. URL: https://doi.org/10.2147/jmdh.s69979, doi:10.2147/jmdh.s69979. This article has 101 citations and is from a peer-reviewed journal.

11. (stavrou2023charcot–marie–toothneuropathiescurrentgene pages 2-2): Marina Stavrou, Alexia Kagiava, Irene Sargiannidou, Elena Georgiou, and Kleopas A. Kleopa. <scp>charcot–marie–tooth</scp>neuropathies: current gene therapy advances and the route toward translation. Journal of the Peripheral Nervous System, 28:150-168, Apr 2023. URL: https://doi.org/10.1111/jns.12543, doi:10.1111/jns.12543. This article has 27 citations and is from a peer-reviewed journal.

12. (NCT06482437 chunk 1):  Safety and Efficacy of NMD670 in Adult Patients With Type 1 and Type 2 Charcot-Marie-Tooth Disease. NMD Pharma A/S. 2024. ClinicalTrials.gov Identifier: NCT06482437

13. (tedeschi2025physicaltherapyinterventions pages 8-10): Roberto Tedeschi, Danilo Donati, and Federica Giorgi. Physical therapy interventions for gait and balance in charcot-marie-tooth disease: a scoping review. Life, 15:1036, Jun 2025. URL: https://doi.org/10.3390/life15071036, doi:10.3390/life15071036. This article has 2 citations.

14. (dong2024currenttreatmentmethods pages 4-6): Hongxian Dong, Boquan Qin, Hui Zhang, Lei Lei, and Shizhou Wu. Current treatment methods for charcot–marie–tooth diseases. Biomolecules, 14:1138, Sep 2024. URL: https://doi.org/10.3390/biom14091138, doi:10.3390/biom14091138. This article has 9 citations.

15. (scherrer2025frominvivo pages 1-3): Camille Scherrer, Camille Loret, Nicolas Védrenne, Colman Buckley, Anne-Sophie Lia, Vincent Kermene, Franck Sturtz, Frédéric Favreau, Amandine Rovini, and Pierre-Antoine Faye. From in vivo models to in vitro bioengineered neuromuscular junctions for the study of charcot-marie-tooth disease. Journal of Tissue Engineering, Mar 2025. URL: https://doi.org/10.1177/20417314241310508, doi:10.1177/20417314241310508. This article has 0 citations and is from a domain leading peer-reviewed journal.

16. (koenig2025restoringproteinsynthesis pages 21-25): J Koenig. Restoring protein synthesis in a neuronal model of charcot-marie-tooth disease. Unknown journal, 2025.

17. (cortese2020targetednextgenerationsequencing pages 1-2): Andrea Cortese, Janel E. Wilcox, James M. Polke, Roy Poh, Mariola Skorupinska, Alexander M. Rossor, Matilde Laura, Pedro J. Tomaselli, Henry Houlden, Michael E. Shy, and Mary M. Reilly. Targeted next-generation sequencing panels in the diagnosis of charcot-marie-tooth disease. Neurology, Jan 2020. URL: https://doi.org/10.1212/wnl.0000000000008672, doi:10.1212/wnl.0000000000008672. This article has 125 citations and is from a highest quality peer-reviewed journal.

18. (pipis2019nextgenerationsequencingin pages 1-5): Menelaos Pipis, Alexander M. Rossor, Matilde Laura, and Mary M. Reilly. Next-generation sequencing in charcot–marie–tooth disease: opportunities and challenges. Nature Reviews Neurology, 15:644-656, Oct 2019. URL: https://doi.org/10.1038/s41582-019-0254-5, doi:10.1038/s41582-019-0254-5. This article has 243 citations and is from a highest quality peer-reviewed journal.

19. (rudnikschoneborn2020charcotmarietoothdiseaseand pages 1-2): Sabine Rudnik-Schöneborn, Michaela Auer-Grumbach, and Jan Senderek. Charcot-marie-tooth disease and hereditary motor neuropathies – update 2020. Medizinische Genetik, 32:207-219, Sep 2020. URL: https://doi.org/10.1515/medgen-2020-2038, doi:10.1515/medgen-2020-2038. This article has 37 citations.

20. (pipis2019nextgenerationsequencingin pages 10-14): Menelaos Pipis, Alexander M. Rossor, Matilde Laura, and Mary M. Reilly. Next-generation sequencing in charcot–marie–tooth disease: opportunities and challenges. Nature Reviews Neurology, 15:644-656, Oct 2019. URL: https://doi.org/10.1038/s41582-019-0254-5, doi:10.1038/s41582-019-0254-5. This article has 243 citations and is from a highest quality peer-reviewed journal.

21. (leale2024telecoachingapotential pages 2-3): Ignazio Leale, Vincenzo Di Stefano, Carola Costanza, Filippo Brighina, Michele Roccella, Antonio Palma, and Giuseppe Battaglia. Telecoaching: a potential new training model for charcot-marie-tooth patients: a systematic review. Frontiers in Neurology, May 2024. URL: https://doi.org/10.3389/fneur.2024.1359091, doi:10.3389/fneur.2024.1359091. This article has 12 citations and is from a peer-reviewed journal.

22. (NCT05777226 chunk 1): Ruxu Zhang. Research of SORD-CMT Natural History and Epalrestat Treatment. The Third Xiangya Hospital of Central South University. 2023. ClinicalTrials.gov Identifier: NCT05777226

23. (NCT07223632 chunk 1):  Treatment of Charcot-Marie-Tooth Disease, Axonal, Type 2S (CMT2S) in an Individual Patient. Vanda Pharmaceuticals. 2025. ClinicalTrials.gov Identifier: NCT07223632

24. (abati2024invivoanda pages 111-114): E Abati. In vivo and in vitro evaluation of the combination of rna interfering and gene therapy for treating mitofusin2-related diseases. Unknown journal, 2024.

25. (dong2024currenttreatmentmethods media 63deef45): Hongxian Dong, Boquan Qin, Hui Zhang, Lei Lei, and Shizhou Wu. Current treatment methods for charcot–marie–tooth diseases. Biomolecules, 14:1138, Sep 2024. URL: https://doi.org/10.3390/biom14091138, doi:10.3390/biom14091138. This article has 9 citations.

26. (dong2024currenttreatmentmethods media 098aab8b): Hongxian Dong, Boquan Qin, Hui Zhang, Lei Lei, and Shizhou Wu. Current treatment methods for charcot–marie–tooth diseases. Biomolecules, 14:1138, Sep 2024. URL: https://doi.org/10.3390/biom14091138, doi:10.3390/biom14091138. This article has 9 citations.

27. (okamoto2023thecurrentstate pages 2-4): Yuji Okamoto and Hiroshi Takashima. The current state of charcot–marie–tooth disease treatment. Genes, 14:1391, Jul 2023. URL: https://doi.org/10.3390/genes14071391, doi:10.3390/genes14071391. This article has 56 citations.

28. (pipis2019nextgenerationsequencingin pages 5-10): Menelaos Pipis, Alexander M. Rossor, Matilde Laura, and Mary M. Reilly. Next-generation sequencing in charcot–marie–tooth disease: opportunities and challenges. Nature Reviews Neurology, 15:644-656, Oct 2019. URL: https://doi.org/10.1038/s41582-019-0254-5, doi:10.1038/s41582-019-0254-5. This article has 243 citations and is from a highest quality peer-reviewed journal.

29. (abati2024invivoand pages 111-114): E Abati. In vivo and in vitro evaluation of the combination of rna interfering and gene therapy for treating mitofusin2-related diseases. Unknown journal, 2024.