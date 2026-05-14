---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T15:16:00.873651'
end_time: '2026-05-08T15:25:56.050868'
duration_seconds: 595.18
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Embryonal Rhabdomyosarcoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Embryonal Rhabdomyosarcoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Embryonal Rhabdomyosarcoma** covering all of the
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
- **Disease Name:** Embryonal Rhabdomyosarcoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Embryonal Rhabdomyosarcoma** covering all of the
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


# Embryonal Rhabdomyosarcoma (ERMS): Disease Characteristics Research Report

## Target Disease
- **Disease name:** Embryonal rhabdomyosarcoma (ERMS)
- **Category:** Malignant pediatric soft-tissue sarcoma (skeletal muscle differentiation)
- **MONDO ID:** Not identified in the retrieved evidence (see “Limitations”)

## Executive summary (current understanding)
Embryonal rhabdomyosarcoma (ERMS) is the most common pediatric rhabdomyosarcoma subtype and largely overlaps with **FOXO1 fusion–negative rhabdomyosarcoma (FN‑RMS)** in modern molecular classification, which is increasingly used for **risk stratification and treatment selection**. Clinically, RMS frequently presents as a mass in the **head/neck**, **genitourinary tract**, or **extremities**. ERMS/FN‑RMS is characterized by recurrent **chromosomal gains**, **11p15 allelic loss/LOH (IGF2 region)**, and frequent **RAS‑pathway** alterations; poor‑prognosis subsets include **TP53** and **MYOD1 (L122R)** altered tumors. Standard-of-care remains multimodal therapy (chemotherapy plus surgery and/or radiotherapy), while contemporary trials incorporate molecular risk markers and emerging biomarkers such as circulating tumor DNA (ctDNA). (vries2023imaginginrhabdomyosarcoma pages 1-3, oberoi2023childrensoncologygroups pages 1-3, oberoi2023childrensoncologygroups pages 3-5)

A compact, evidence-backed fact table is provided below.

| Domain | Item | Summary | Quantitative detail | Citation-year | Primary citation context id |
|---|---|---|---|---|---|
| Identifier/classification | Disease name | Embryonal rhabdomyosarcoma (ERMS) is the embryonal subtype of rhabdomyosarcoma and is a fusion-negative RMS category in most cases | ERMS constitutes 70–80% of RMS in one clinicopathologic review; another review lists ERMS as 57% of RMS | 2025; 2025 | pqac-00000006 |
| Identifier/classification | Synonyms | ERMS; embryonal RMS; fusion-negative RMS (FN-RMS) often used as molecular proxy because most ERMS are FOXO1 fusion-negative | Not quantified | 2025; 2025 | pqac-00000003 |
| Identifier/classification | WHO classification | WHO/2020-era classification lists four RMS subtypes: embryonal, alveolar, pleomorphic, spindle cell/sclerosing | 4 major subtypes | 2025; 2026 | pqac-00000008 |
| Identifier/classification | MeSH / ICD / MONDO / Orphanet | Specific MeSH, ICD-10/11, MONDO, and Orphanet identifiers were not provided in the retrieved evidence; Open Targets lists disease term “embryonal rhabdomyosarcoma” as EFO_0000437 | Not available in provided evidence | 2023–2025 evidence set | pqac-00000000 |
| Epidemiology | Pediatric cancer burden | RMS is the most common pediatric soft tissue sarcoma and accounts for about 3% of pediatric cancers | ~3% of pediatric cancers | 2023 | pqac-00000010 |
| Epidemiology | Annual U.S. cases | Approximate number of U.S. pediatric RMS diagnoses per year | ~350 cases/year | 2023 | pqac-00000010 |
| Epidemiology | Incidence | Pediatric RMS annual incidence | 4.6 per million children (COG blueprint); ~4 per million age 0–19 in European registry summary | 2023; 2023 | pqac-00000010 |
| Epidemiology | Age/sex distribution | RMS median age at diagnosis is early childhood and males are more often affected | Median age 5 years; 72–81% diagnosed before age 10; male:female ratio ~1.4 | 2023 | pqac-00000001 |
| Prognosis | Overall localized vs metastatic RMS | Outcomes vary strongly by risk group and metastatic status | 5-year OS ~80% for localized disease; ~35% for metastatic disease | 2023 | pqac-00000001 |
| Prognosis | COG low/intermediate/high risk | Long-term survival ranges by risk group in COG framework | ~90% / 50–70% / ~20% 5-year survival for low / intermediate / high risk STS/RMS frameworks | 2023 | pqac-00000010 |
| Prognosis | Favorable fusion-negative groups | Excellent survival for selected favorable FN-RMS groups | 5-year EFS/OS 92%/99% for FN Stage 1, Clinical Group I; 87%/97% for FN Stage 1 CG II / Stage 2 CG I-II / orbit CG III | 2023 | pqac-00000010 |
| Prognosis | ctDNA prognostic value in FN-RMS | Detectable baseline ctDNA identifies worse-outcome intermediate-risk FN-RMS | ctDNA detectable in 13/75 FN-RMS sera (17%); EFS 33.3% vs 68.9%, OS 33.3% vs 83.2%, P=.0028 and P<.0001 | 2023 | pqac-00000014 |
| Prognosis | Poor-risk biomarkers | MYOD1 and TP53 mutations worsen prognosis in FN-RMS | MYOD1 L122R associated survival 0–30%; TP53 mutations in ~13% FN-RMS and worse outcomes | 2023 | pqac-00000012 |
| Molecular feature | FOXO1 status | Fusion status has replaced histologic subtype in risk stratification; FOXO1 fusion-negative disease has better prognosis than fusion-positive disease | Qualitative prognostic effect; no single percentage for ERMS itself | 2023 | pqac-00000010 |
| Molecular feature | 11p15 loss | ERMS frequently shows 11p15 loss of heterozygosity involving IGF2 region | ~80% have 11p15 LOH | 2023 | pqac-00000007 |
| Molecular feature | RAS-pathway mutations | Fusion-negative/embryonal RMS is characterized by recurrent RAS-pathway alterations | Frequent, but no single pooled percentage given in retrieved evidence | 2023 | pqac-00000012 |
| Molecular feature | TP53 | TP53 is a recurrent poor-risk alteration in FN-RMS/ERMS | ~13% of FN-RMS | 2023 | pqac-00000012 |
| Molecular feature | MYOD1 | MYOD1 L122R marks biologically aggressive RMS subset and is integrated into modern risk frameworks | Survival 0–30% in MYOD1-mutant disease | 2023 | pqac-00000012 |
| Molecular feature | DICER1 in gynecologic ERMS | DICER1 alterations are enriched in cervical and uterine ERMS and may aid diagnosis | Almost all cervical ERMS and nearly 67% of uterine corpus ERMS carry DICER1 mutations; 4/5 tested gynecologic ERMS in one cohort were DICER1-mutant | 2025 | pqac-00000006 |
| Molecular feature | Chromosomal/copy-number pattern | FN-RMS/ERMS shows whole-chromosome gains; one transcriptomic/genomic analysis highlighted chromosome 8 cytoband amplification/gain in FN-RMS | chr8-related amplification highlighted; exact ERMS frequency not provided in compact evidence set | 2023 | pqac-00000012 |
| Diagnostics | Histology/IHC | ERMS diagnosis relies on morphology plus skeletal muscle markers | Common markers: desmin, myogenin, MyoD1; in one gynecologic ERMS series Myogenin 11/13, Desmin 13/13, MyoD1 12/13, Myoglobin 5/9 | 2025 | pqac-00000006 |


*Table: This table condenses the most actionable evidence from the retrieved sources for embryonal rhabdomyosarcoma, covering classification, epidemiology, prognosis, and molecular features. It is useful as a compact reference for knowledge-base population using only facts directly supported by the available context IDs.*

---

## 1. Disease information
### 1.1 Definition/overview
Rhabdomyosarcoma (RMS) is described as the **most frequent pediatric soft tissue sarcoma**, with major subtypes including **embryonal** and **alveolar**; ERMS is typically **fusion-negative** and is described as being driven by oncogenic driver mutations such as **RAS and TP53** in the imaging-focused review by de Vries et al. (Pediatric Radiology, **2023‑02**, URL: https://doi.org/10.1007/s00247-023-05596-8). (vries2023imaginginrhabdomyosarcoma pages 1-3)

### 1.2 Key identifiers and classifications
- **WHO classification:** Reviews in the retrieved set summarize the WHO approach as including four main RMS subtypes (embryonal, alveolar, pleomorphic, spindle cell/sclerosing). (nakano2026thedevelopmentof pages 1-2)
- **Fusion status classification:** COG and other cooperative groups increasingly classify RMS into **FOXO1 fusion‑positive** vs **FOXO1 fusion‑negative**, with fusion status replacing histology as a key risk classifier. (oberoi2023childrensoncologygroups pages 1-3)
- **Open Targets disease concept:** “Embryonal rhabdomyosarcoma” appears as **EFO_0000437** in Open Targets outputs. (OpenTargets Search: embryonal rhabdomyosarcoma)

**Not found in the retrieved evidence:** ICD‑10/ICD‑11, MeSH identifier, Orphanet (ORPHA) code, MONDO ID.

### 1.3 Synonyms and alternative names
- Embryonal rhabdomyosarcoma (ERMS)
- Embryonal RMS
- Fusion‑negative rhabdomyosarcoma (FN‑RMS) (used as a molecular proxy in many contemporary sources because most ERMS are FOXO1 fusion‑negative) (wasti2025childhoodadolescentand pages 2-4, oberoi2023childrensoncologygroups pages 1-3)

### 1.4 Evidence provenance
This report is derived from **aggregated disease-level resources** (COG blueprint review; imaging guideline review; multi-institutional clinical study; trial registry) and selected clinicopathologic series. (vries2023imaginginrhabdomyosarcoma pages 1-3, oberoi2023childrensoncologygroups pages 1-3, abbou2023circulatingtumordna pages 1-2)

---

## 2. Etiology
### 2.1 Primary causal factors (molecular/genetic)
ERMS/FN‑RMS is characterized by:
- **Chromosomal alterations:** Whole-chromosome gains and **11p15.5 allelic loss** are described as characteristic genomic features in the COG blueprint review. (oberoi2023childrensoncologygroups pages 3-5)
- **11p15 loss of heterozygosity (LOH):** A 2023 review reports that **~80%** of ERMS have **LOH at 11p15** involving the **IGF‑2/IGF2** region. (zarrabi2023rhabdomyosarcomacurrenttherapy pages 3-5)
- **RAS pathway alterations:** The COG blueprint describes frequent RAS‑pathway and point mutations (e.g., **NRAS, KRAS, HRAS**) in fusion-negative disease. (oberoi2023childrensoncologygroups pages 3-5)

### 2.2 Risk factors
#### 2.2.1 Genetic predisposition syndromes
Multiple cancer predisposition syndromes are reported as increasing RMS risk in a 2023 imaging guideline review, including:
- **Neurofibromatosis type 1 (NF1)**
- **Li–Fraumeni syndrome (TP53 germline)**
- **DICER1 syndrome**
- **Noonan syndrome**
- **Beckwith–Wiedemann syndrome**
- **Costello syndrome** (vries2023imaginginrhabdomyosarcoma pages 1-3)

#### 2.2.2 Environmental/lifestyle risk factors
No specific environmental or lifestyle risk factors were identified in the retrieved evidence.

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No ERMS-specific gene–environment interaction evidence was identified in the retrieved set.

---

## 3. Phenotypes (clinical presentation)
### 3.1 Typical phenotypes and presentation
RMS “can present as a mass at nearly any site in the body,” with most common presentations in **head and neck**, **genitourinary tract**, and **extremities**. (vries2023imaginginrhabdomyosarcoma pages 1-3)

### 3.2 Age of onset and sex ratio
European registry–summarized epidemiology in the imaging review reports:
- **Median age at diagnosis:** ~5 years
- **Proportion <10 years:** ~72–81%
- **Male:female ratio:** ~1.4 (95% CI 1.2–1.6) (vries2023imaginginrhabdomyosarcoma pages 1-3)

### 3.3 Suggested HPO terms (examples)
Evidence in the retrieved set is not granular enough to assign frequencies per phenotype; the following HPO terms are consistent with common presentations noted (mass lesion by site):
- **Mass of head and neck** (e.g., *HP:0000235* Abnormality of head or neck [broad parent]; site-specific “mass” terms may be used in implementation)
- **Pelvic mass** (*HP:0002681*) / **Abdominal mass** (*HP:0003270*) for genitourinary presentations
- **Soft tissue mass** (*HP:0030832* [soft-tissue abnormality/mass terms])

**Note:** HPO IDs above are provided as ontology suggestions; confirm exact term mapping during curation.

---

## 4. Genetic / molecular information
### 4.1 Causal genes and recurrent somatic alterations (ERMS/FN‑RMS)
From the COG blueprint review, fusion‑negative disease is described as having frequent point mutations including **NRAS, KRAS, HRAS, TP53, MYOD1, PIK3CA, FGFR4** and characteristic chromosomal events including **11p15.5 allelic loss**. (oberoi2023childrensoncologygroups pages 3-5)

### 4.2 Clinically important poor-risk biomarkers
- **MYOD1 L122R:** Reported to predict **very poor survival (0–30%)** in the COG blueprint summary. (oberoi2023childrensoncologygroups pages 3-5)
- **TP53:** TP53 mutations are reported in **~13%** of FN‑RMS and are associated with worse outcomes. (oberoi2023childrensoncologygroups pages 3-5)

### 4.3 DICER1 (site-associated enrichment)
A clinicopathological series of female reproductive system ERMS highlights enrichment for **DICER1** alterations, stating: “Almost all cervical ERMS and nearly **67%** of uterine corpus ERMS carry DICER1 mutations,” and in their cohort **4/5** tested cases had DICER1 mutations. (Frontiers in Oncology, **2025‑03**, URL: https://doi.org/10.3389/fonc.2025.1546607) (bai2025clinicopathologicalanalysisof pages 1-2)

### 4.4 Epigenetics and omics
The retrieved evidence set did not provide ERMS-specific quantitative epigenetic signatures; however, the COG blueprint emphasizes that molecular profiling (including fusion status and specific mutations) is increasingly incorporated into risk stratification and prospective trials. (oberoi2023childrensoncologygroups pages 1-3)

### 4.5 Suggested GO and CL terms (mechanism-relevant)
Based on evidence-supported biology (RAS pathway activation; differentiation blockade implied by MYOD1 axis and RMS myogenic markers):
- **GO (Biological Process) suggestions:**
  - Ras protein signal transduction (e.g., *GO:0007265*)
  - Regulation of cell proliferation (*GO:0042127*)
  - Myoblast differentiation / skeletal muscle cell differentiation (myogenic program dysregulation; use appropriate child terms during curation)
- **CL (Cell Ontology) suggestions:**
  - Skeletal muscle cell / myoblast lineages (tumor shows skeletal muscle differentiation markers)

---

## 5. Environmental information
No ERMS-specific environmental, lifestyle, or infectious causal contributors were identified in the retrieved evidence.

---

## 6. Mechanism / pathophysiology (causal chain)
### 6.1 Upstream initiating events
In ERMS/FN‑RMS, recurrent **genomic alterations** include **11p15.5 allelic loss/LOH** (IGF2 locus region) and frequent **RAS pathway mutations** (NRAS/KRAS/HRAS), with subsets harboring **TP53** or **MYOD1** alterations that confer poor prognosis. (zarrabi2023rhabdomyosarcomacurrenttherapy pages 3-5, oberoi2023childrensoncologygroups pages 3-5)

### 6.2 Downstream cellular consequences and clinical manifestation
A mechanistic chain supported by the retrieved evidence:
1. **Genetic alterations** (e.g., 11p15 LOH; RAS-pathway mutations; TP53/MYOD1 in poor-risk subsets) (zarrabi2023rhabdomyosarcomacurrenttherapy pages 3-5, oberoi2023childrensoncologygroups pages 3-5)
2. Promote **oncogenic signaling and tumor growth** in mesenchymal lineage cells with skeletal muscle differentiation, producing a **soft-tissue mass** presentation at diverse sites (head/neck, GU tract, extremity) (vries2023imaginginrhabdomyosarcoma pages 1-3)
3. Disease aggressiveness and treatment resistance are increased in molecularly defined high-risk subsets (TP53, MYOD1), reflected in poorer survival outcomes. (oberoi2023childrensoncologygroups pages 3-5)

---

## 7. Anatomical structures affected
### 7.1 Organ/system level (common sites)
Most common presentations: **head and neck**, **genitourinary tract**, **extremities**. (vries2023imaginginrhabdomyosarcoma pages 1-3)

### 7.2 Suggested UBERON terms (examples)
- Head and neck region (e.g., UBERON:0000033 [head])
- Urinary bladder (UBERON:0001255)
- Prostate gland (UBERON:0002367)
- Skeletal muscle of limb/extremity (use appropriate limb muscle terms)

---

## 8. Temporal development
- **Onset:** Predominantly pediatric with early childhood peak (median ~5 years; most diagnosed before age 10). (vries2023imaginginrhabdomyosarcoma pages 1-3)
- **Course/progression:** Variable; outcomes depend strongly on risk group and metastatic status. (vries2023imaginginrhabdomyosarcoma pages 1-3, oberoi2023childrensoncologygroups pages 1-3)

---

## 9. Inheritance and population
### 9.1 Epidemiology
- **Incidence (children):** 4.6 per million children (COG blueprint). (oberoi2023childrensoncologygroups pages 1-3)
- **Annual U.S. cases:** ~350 children diagnosed with RMS per year (COG blueprint). (oberoi2023childrensoncologygroups pages 1-3)
- **European registry summary:** ~4 per million (age 0–19), ~400 new patients per year (age 0–19) (as summarized in the imaging review). (vries2023imaginginrhabdomyosarcoma pages 1-3)

### 9.2 Sex ratio and age distribution
- Male predominance: male:female ratio ~1.4. (vries2023imaginginrhabdomyosarcoma pages 1-3)

### 9.3 Inheritance pattern
Most ERMS appears sporadic; however, multiple **germline cancer predisposition syndromes** increase risk (NF1, Li–Fraumeni/TP53, DICER1, Noonan, Beckwith–Wiedemann, Costello). (vries2023imaginginrhabdomyosarcoma pages 1-3)

---

## 10. Diagnostics
### 10.1 Pathology and immunohistochemistry (IHC)
A 2023 RMS review notes use of IHC muscle markers including **alpha-actin, MyoD1, myogenin, and desmin** to distinguish RMS from other small round blue cell tumors. (zarrabi2023rhabdomyosarcomacurrenttherapy pages 3-5)

In a 13‑patient gynecologic ERMS series, IHC positivity rates were:
- **Desmin:** 13/13
- **MyoD1:** 12/13
- **Myogenin:** 11/13
- **Myoglobin:** 5/9 (bai2025clinicopathologicalanalysisof pages 1-2)

### 10.2 Molecular testing and risk stratification
COG emphasizes fusion status as central: **FOXO1 fusion status has replaced histologic subtype** in risk stratification, with FOXO1 fusion-positive conferring worse prognosis than fusion-negative. (oberoi2023childrensoncologygroups pages 1-3)

### 10.3 Imaging and staging (real-world implementation)
The imaging guideline review highlights multidisciplinary management and notes European collaborative imaging guidance (EpSSG/CWS/ESPR collaboration) spanning clinical suspicion, biopsy, staging, response assessment, and follow-up. (vries2023imaginginrhabdomyosarcoma pages 1-3)

### 10.4 Liquid biopsy / ctDNA (emerging diagnostic/prognostic tool)
In intermediate-risk RMS, baseline ctDNA detection is feasible and prognostic.
- Cohort: **124** intermediate-risk RMS patients (75 FN‑RMS; 49 FP‑RMS)
- FN‑RMS ctDNA detection at diagnosis: **13/75 (17%)**
- FN‑RMS outcomes with detectable ctDNA vs not detectable:
  - **EFS:** 33.3% vs 68.9% (P = .0028)
  - **OS:** 33.3% vs 83.2% (P < .0001)
- Similar adverse associations were reported for FP‑RMS. (Journal of Clinical Oncology, **2023‑05**, URL: https://doi.org/10.1200/JCO.22.00409) (abbou2023circulatingtumordna pages 1-2)

Additional quantitative details from the same study (alternate excerpt) include: CNAs in tumors 71%, translocations in tumors 93%, and overall ctDNA detection 57% using combined approaches. (abbou2023circulatingtumordna pages 6-7)

---

## 11. Outcome / prognosis
### 11.1 Risk-group outcome ranges
In the imaging-focused review, 5-year overall survival is summarized as:
- **Localized disease:** ~80%
- **Metastatic disease:** ~35%
- Broad risk-group range: **~50.6% (very high-risk) to 100% (low-risk)** (vries2023imaginginrhabdomyosarcoma pages 1-3)

COG blueprint examples for favorable fusion-negative groups include:
- **FN Stage 1, Clinical Group I:** 5‑year EFS/OS **92% / 99%**
- Other favorable groups: EFS/OS **87% / 97%** (oberoi2023childrensoncologygroups pages 1-3)

### 11.2 Prognostic biomarkers
Poorer prognosis is associated with **FOXO1 fusion positivity**, and within FN‑RMS, **MYOD1** and **TP53** mutations are noted as adverse factors. (oberoi2023childrensoncologygroups pages 1-3, oberoi2023childrensoncologygroups pages 3-5)

---

## 12. Treatment
### 12.1 Standard multimodal therapy
The imaging review describes standard management as multimodal: **systemic chemotherapy plus local therapy (surgery and/or radiotherapy)**. (vries2023imaginginrhabdomyosarcoma pages 1-3)

COG blueprint specifies typical chemotherapy backbones:
- **VA** (vincristine + dactinomycin) ± cyclophosphamide (**VAC**)
- **VAC/VI** (VAC with irinotecan-containing components) (oberoi2023childrensoncologygroups pages 1-3)

COG-reported comparative outcomes in intermediate-risk trials:
- ARST0531: **4-year EFS 63% vs 59%** and **OS 73% vs 72%** for VAC vs VAC/VI strategies (with different cumulative cyclophosphamide exposure). (oberoi2023childrensoncologygroups pages 1-3)

### 12.2 Current applications: molecularly informed treatment intensification
COG notes that patients meeting very-low/low-risk clinical criteria but with **TP53 or MYOD1** mutations are treated with **42 weeks VAC** (cumulative cyclophosphamide 16.6 g/m²) and not considered very-low/low risk. (oberoi2023childrensoncologygroups pages 19-20)

### 12.3 Ongoing / recent clinical trials (selected)
#### COG ARST2032: very low/low-risk FN-RMS (real-world implementation: enrolling)
- **Trial:** NCT05304585 (ClinicalTrials.gov)
- **Title:** “Chemotherapy for the Treatment of Patients With Newly Diagnosed Very Low-Risk and Low Risk Fusion Negative Rhabdomyosarcoma”
- **Sponsor/Group:** Children’s Oncology Group
- **Status:** Recruiting (per retrieved registry snippet)
- **Key regimens:** Regimen VA (very low-risk), VAC/VA (low-risk), and a regimen for mutation-positive patients (“Regimen M”) that includes radiotherapy; uses vincristine, dactinomycin, cyclophosphamide (and imaging/staging procedures).
- **Primary endpoint:** 3‑year failure‑free survival (Kaplan–Meier)
- **Feasibility endpoint:** central molecular risk stratification feasible if ≥80% results returned by 6 weeks. (NCT05304585 chunk 2)

### 12.4 Suggested MAXO terms (examples)
- Multiagent chemotherapy (MAXO term for antineoplastic chemotherapy)
- Tumor resection / surgical excision
- Radiotherapy
- Molecular diagnostic procedure (for fusion testing)

---

## 13. Prevention
No primary prevention strategies specific to ERMS were identified in the retrieved evidence. Secondary prevention in practice centers on **timely recognition, imaging workup, and standardized staging/risk stratification** within multidisciplinary pediatric oncology pathways. (vries2023imaginginrhabdomyosarcoma pages 1-3)

---

## 14. Other species / natural disease
The retrieved evidence did not provide specific naturally occurring veterinary ERMS epidemiology.

---

## 15. Model organisms
A 2023 RMS review notes that in vivo **mouse and zebrafish** models are used to screen future therapeutic approaches and study mechanisms. (zarrabi2023rhabdomyosarcomacurrenttherapy pages 3-5)

A 2026 review emphasizes that advances in **animal models** and tissue acquisition have improved understanding of RMS biology, though the provided excerpt does not enumerate specific engineered ERMS models. (hebron2026biologicaladvancesand pages 22-23)

---

## Visual evidence: COG RMS prognostic groups
The COG rhabdomyosarcoma prognostic group table (risk stratification schema with associated long-term EFS ranges) is provided in the retrieved cropped table image. (oberoi2023childrensoncologygroups media 44b370af)

---

## Limitations of the current evidence set
- **Ontology identifiers** (MONDO, Orphanet/ORPHA, ICD‑10/11, MeSH) were not present in the retrieved texts; additional targeted retrieval (Orphanet/MONDO/MeSH/ICD sources) would be required for a fully populated identifier section.
- Several topics requested in the template (environmental modifiers, epigenomic signatures, metabolomics, detailed differential diagnosis lists, and cross-species natural disease frequency) were not covered with ERMS-specific primary data in the retrieved evidence.

---

## Key sources (with publication dates and URLs)
- de Vries ISA et al. **Imaging in rhabdomyosarcoma: a patient journey.** Pediatric Radiology. **2023‑02**. https://doi.org/10.1007/s00247-023-05596-8 (vries2023imaginginrhabdomyosarcoma pages 1-3)
- Oberoi S et al. **Children’s Oncology Group’s 2023 blueprint for research: Soft tissue sarcomas.** Pediatric Blood & Cancer. **2023‑07**. https://doi.org/10.1002/pbc.30556 (oberoi2023childrensoncologygroups pages 1-3, oberoi2023childrensoncologygroups pages 3-5)
- Abbou S et al. **Circulating tumor DNA is prognostic in intermediate-risk rhabdomyosarcoma.** Journal of Clinical Oncology. **2023‑05**. https://doi.org/10.1200/JCO.22.00409 (abbou2023circulatingtumordna pages 1-2)
- Zarrabi A et al. **Rhabdomyosarcoma: Current Therapy, Challenges, and Future Approaches to Treatment Strategies.** Cancers (preprint version listed). **2023‑11**. https://doi.org/10.20944/preprints202309.0846.v1 (zarrabi2023rhabdomyosarcomacurrenttherapy pages 3-5)
- ClinicalTrials.gov. **NCT05304585 / COG ARST2032.** First posted year shown in excerpt: **2022**. https://clinicaltrials.gov/study/NCT05304585 (NCT05304585 chunk 2)


References

1. (vries2023imaginginrhabdomyosarcoma pages 1-3): Isabelle S. A. de Vries, Roelof van Ewijk, Laura M. E. Adriaansen, Anneloes E. Bohte, Arthur J. A. T. Braat, Raquel Dávila Fajardo, Laura S. Hiemcke-Jiwa, Marinka L. F. Hol, Simone A. J. ter Horst, Bart de Keizer, Rutger R. G. Knops, Michael T. Meister, Reineke A. Schoot, Ludi E. Smeele, Sheila Terwisscha van Scheltinga, Bas Vaarwerk, Johannes H. M. Merks, and Rick R. van Rijn. Imaging in rhabdomyosarcoma: a patient journey. Pediatric Radiology, 53:788-812, Feb 2023. URL: https://doi.org/10.1007/s00247-023-05596-8, doi:10.1007/s00247-023-05596-8. This article has 37 citations and is from a peer-reviewed journal.

2. (oberoi2023childrensoncologygroups pages 1-3): Sapna Oberoi, Jacquelyn N. Crane, Josephine H. Haduong, Erin R. Rudzinski, Suzanne L. Wolden, Roshni Dasgupta, Corinne M. Linardic, Aaron R. Weiss, and Rajkumar Venkatramani. Children's oncology group's 2023 blueprint for research: soft tissue sarcomas. Pediatric Blood & Cancer, Jul 2023. URL: https://doi.org/10.1002/pbc.30556, doi:10.1002/pbc.30556. This article has 26 citations and is from a peer-reviewed journal.

3. (oberoi2023childrensoncologygroups pages 3-5): Sapna Oberoi, Jacquelyn N. Crane, Josephine H. Haduong, Erin R. Rudzinski, Suzanne L. Wolden, Roshni Dasgupta, Corinne M. Linardic, Aaron R. Weiss, and Rajkumar Venkatramani. Children's oncology group's 2023 blueprint for research: soft tissue sarcomas. Pediatric Blood & Cancer, Jul 2023. URL: https://doi.org/10.1002/pbc.30556, doi:10.1002/pbc.30556. This article has 26 citations and is from a peer-reviewed journal.

4. (nakano2026thedevelopmentof pages 1-2): Kenji Nakano. The development of novel treatment strategies for rhabdomyosarcoma. Cancers, 18:690, Feb 2026. URL: https://doi.org/10.3390/cancers18040690, doi:10.3390/cancers18040690. This article has 0 citations.

5. (OpenTargets Search: embryonal rhabdomyosarcoma): Open Targets Query (embryonal rhabdomyosarcoma, 20 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (wasti2025childhoodadolescentand pages 2-4): Ajla T. Wasti, Gianni Bisogno, Raquel Hladun, Anne-Sophie Defachelles, Michela Casanova, Willemijn B. Breunis, Susanne A. Gatz, Reineke A. Schoot, Andrea Ferrari, Meriel Jenney, Rita Alaggio, Raquel Davila Fajardo, Sheila Terwisscha van Scheltinga, Janet Shipley, Michael Torsten Meister, Rick R. van Rijn, John Anderson, Monika Sparber-Sauer, Julia C. Chisholm, and Johannes H. M. Merks. Childhood, adolescent and young adult poor-prognosis rhabdomyosarcoma. Cancers, 17:3100, Sep 2025. URL: https://doi.org/10.3390/cancers17193100, doi:10.3390/cancers17193100. This article has 1 citations.

7. (abbou2023circulatingtumordna pages 1-2): Samuel Abbou, Kelly Klega, Junko Tsuji, Mohammad Tanhaemami, David Hall, Donald A. Barkauskas, Mark D. Krailo, Carrie Cibulskis, Anwesha Nag, Aaron R. Thorner, Samuel Pollock, Alma Imamovic-Tuco, Jack F. Shern, Steven G. DuBois, Rajkumar Venkatramani, Douglas S. Hawkins, and Brian D. Crompton. Circulating tumor dna is prognostic in intermediate-risk rhabdomyosarcoma: a report from the children's oncology group. Journal of Clinical Oncology, 41:2382-2393, May 2023. URL: https://doi.org/10.1200/jco.22.00409, doi:10.1200/jco.22.00409. This article has 37 citations and is from a highest quality peer-reviewed journal.

8. (zarrabi2023rhabdomyosarcomacurrenttherapy pages 3-5): Ali Zarrabi, David Perrin, Mahboubeh Kavoosi, Micah Sommer, Serap Sezen, Parvaneh Mehrbod, Bhavya Bhushan, Filip Machaj, Jakub Rosik, Philip Kawalec, Saba Afifi, Seyed Mohammadreza Bolandi, Peyman Koleini, Mohsen Taheri, Tayyebeh Madrakian, Marek Jan Łos, Benjamin Lindsey, Nilufer Cakir, Atefeh Zarepour, Kiavash Hushmandi, Ali Fallah, Bahattin Koc, Mazaher Ahmadi, Susan E. Logue, Gorka Orive, Stevan Pecic, Joseph W. Gordon, and Saeid Ghavami. Rhabdomyosarcoma: current therapy, challenges, and future approaches to treatment strategies. Cancers, Nov 2023. URL: https://doi.org/10.20944/preprints202309.0846.v1, doi:10.20944/preprints202309.0846.v1. This article has 90 citations.

9. (bai2025clinicopathologicalanalysisof pages 1-2): Liping Bai, Ling Han, Liang Sun, Juan Zou, and Ya-li Chen. Clinicopathological analysis of 13 patients with embryonal rhabdomyosarcoma of the female reproductive system in the chinese population. Frontiers in Oncology, Mar 2025. URL: https://doi.org/10.3389/fonc.2025.1546607, doi:10.3389/fonc.2025.1546607. This article has 2 citations.

10. (abbou2023circulatingtumordna pages 6-7): Samuel Abbou, Kelly Klega, Junko Tsuji, Mohammad Tanhaemami, David Hall, Donald A. Barkauskas, Mark D. Krailo, Carrie Cibulskis, Anwesha Nag, Aaron R. Thorner, Samuel Pollock, Alma Imamovic-Tuco, Jack F. Shern, Steven G. DuBois, Rajkumar Venkatramani, Douglas S. Hawkins, and Brian D. Crompton. Circulating tumor dna is prognostic in intermediate-risk rhabdomyosarcoma: a report from the children's oncology group. Journal of Clinical Oncology, 41:2382-2393, May 2023. URL: https://doi.org/10.1200/jco.22.00409, doi:10.1200/jco.22.00409. This article has 37 citations and is from a highest quality peer-reviewed journal.

11. (oberoi2023childrensoncologygroups pages 19-20): Sapna Oberoi, Jacquelyn N. Crane, Josephine H. Haduong, Erin R. Rudzinski, Suzanne L. Wolden, Roshni Dasgupta, Corinne M. Linardic, Aaron R. Weiss, and Rajkumar Venkatramani. Children's oncology group's 2023 blueprint for research: soft tissue sarcomas. Pediatric Blood & Cancer, Jul 2023. URL: https://doi.org/10.1002/pbc.30556, doi:10.1002/pbc.30556. This article has 26 citations and is from a peer-reviewed journal.

12. (NCT05304585 chunk 2):  Chemotherapy for the Treatment of Patients With Newly Diagnosed Very Low-Risk and Low Risk Fusion Negative Rhabdomyosarcoma. Children's Oncology Group. 2022. ClinicalTrials.gov Identifier: NCT05304585

13. (hebron2026biologicaladvancesand pages 22-23): Katie E. Hebron, Patience Odeniyide, Yun Wei, Berkley E. Gryder, Frederic G. Barr, Dana L. Casey, Eleanor Y. Chen, Brian D. Crompton, Filemon S. Dela Cruz, Adam D. Durbin, Heide L. Ford, Susanne A. Gatz, Mark E. Hatley, Anton G. Henssen, Simone Hettmer, Peter J. Houghton, Genevieve C. Kendall, Javed Khan, Philip J. Lupo, Anand G. Patel, Silvia Pomella, Rossella Rota, Marco Schito, Reineke A. Schoot, Jack F. Shern, Benjamin Z. Stanton, Elizabeth A. Stewart, Cathy A. Swindlehurst, Craig J. Thomas, Christopher R. Vakoc, Angelina V. Vaseva, Rajkumar Venkatramani, Leonard H. Wexler, Jason T. Yustein, Sharon Hammond, Christine M. Heske, David M. Langenau, Corinne M. Linardic, Myron S. Ignatius, and Marielle E. Yohe. Biological advances and current challenges for pediatric rhabdomyosarcoma. Cancers, 18:888, Mar 2026. URL: https://doi.org/10.3390/cancers18060888, doi:10.3390/cancers18060888. This article has 0 citations.

14. (oberoi2023childrensoncologygroups media 44b370af): Sapna Oberoi, Jacquelyn N. Crane, Josephine H. Haduong, Erin R. Rudzinski, Suzanne L. Wolden, Roshni Dasgupta, Corinne M. Linardic, Aaron R. Weiss, and Rajkumar Venkatramani. Children's oncology group's 2023 blueprint for research: soft tissue sarcomas. Pediatric Blood & Cancer, Jul 2023. URL: https://doi.org/10.1002/pbc.30556, doi:10.1002/pbc.30556. This article has 26 citations and is from a peer-reviewed journal.
