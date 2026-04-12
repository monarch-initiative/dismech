---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T20:51:01.132578'
end_time: '2026-04-05T20:59:02.197229'
duration_seconds: 481.06
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: NTRK Fusion-Positive Cancer
  mondo_id: ''
  category: ''
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
- **Disease Name:** NTRK Fusion-Positive Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **NTRK Fusion-Positive Cancer** covering all of the
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
- **Disease Name:** NTRK Fusion-Positive Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **NTRK Fusion-Positive Cancer** covering all of the
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


## Disease Characteristics Research Report: NTRK Fusion-Positive Cancer

### Target Disease
- **Disease name:** NTRK fusion-positive cancer (tumor-agnostic biomarker-defined cancer subset)
- **MONDO ID:** No disease-specific MONDO identifier was found in the retrieved sources. The closest general ontology entry available in the retrieved evidence is **MONDO_0004992 (cancer)** (OpenTargets-derived context; not a disease-specific NTRK-fusion entity).
- **Category:** Neoplastic disease; *molecularly defined / tissue-agnostic (biomarker-driven) cancer subtype*

---

## 1. Disease Information

### Overview (current understanding)
NTRK fusion-positive cancer refers to solid tumors (adult or pediatric) that harbor oncogenic gene fusions involving **NTRK1, NTRK2, or NTRK3**, which encode the TRK receptor tyrosine kinases TRKA/TRKB/TRKC, respectively. These fusions create constitutively active TRK signaling and predict sensitivity to TRK inhibitors in a tumor-agnostic manner. (bungaro2024ntrk123biologydetection pages 5-6, vingiani2023pantrkimmunohistochemistryas pages 1-3)

**Synonyms / alternative names (commonly used):**
- “TRK fusion cancer” (yang2023safetyofcurrent pages 4-6)
- “NTRK-rearranged tumors” / “NTRK fusion–positive solid tumors” (nakata2024prevalenceofneurotrophic pages 2-4, besse2026repotrectinibinntrk pages 1-2)

### Key identifiers
- **ICD-10 / ICD-11 / MeSH / OMIM / Orphanet:** Not identified in the retrieved sources as a single unified disease code, consistent with the fact that NTRK fusion-positive cancer is primarily a **molecular biomarker state across many histologies**, not a single histology-defined disease entity. (bungaro2024ntrk123biologydetection pages 5-6, bungaro2024ntrk123biologydetection pages 2-4)

### Evidence sources
Most information is derived from **aggregated disease-level resources** (pan-cancer cohorts, multi-site clinicogenomic datasets, pooled trial analyses) rather than individual EHR-only sources. (nakata2024prevalenceofneurotrophic pages 2-4, bungaro2024ntrk123biologydetection pages 2-4)

---

## 2. Etiology

### Disease causal factors (mechanistic)
**Primary causal factor:** somatic gene fusions involving NTRK1/2/3, produced by intra- or inter-chromosomal rearrangements, that encode oncogenic fusion proteins. Nakata et al. describe that “**Intra‐ or inter‐chromosomal gene rearrangements produce NTRK gene fusions encoding fusion proteins which are oncogenic drivers in various solid tumors**.” (Cancer Medicine; 2024-06; https://doi.org/10.1002/cam4.7351) (nakata2024prevalenceofneurotrophic pages 1-2)

### Risk factors
Because NTRK fusion-positive cancer is a **genomic alteration** rather than a specific histology, “risk factors” are best framed as **tumor-type and age-group enrichment patterns** rather than traditional exposures:
- Strong enrichment in some rare/pediatric histologies (e.g., infantile fibrosarcoma, secretory breast carcinoma, congenital mesoblastic nephroma), versus very low prevalence in unselected adult solid tumors. (bungaro2024ntrk123biologydetection pages 2-4)
- Pediatric patients show consistently higher NTRK fusion prevalence than adults in large datasets (see Epidemiology). (nakata2024prevalenceofneurotrophic pages 2-4, kubota2025currentmanagementof pages 1-2)

### Protective factors / gene–environment interactions
No protective factors or gene–environment interaction evidence was identified in the retrieved sources.

---

## 3. Phenotypes

### Cross-cutting phenotype concept
Clinical features are largely those of the **underlying tumor histology and site**, rather than a single shared syndrome. However, two cross-cutting clinical patterns emerge:
1) **Age enrichment**: pediatric cancers show higher NTRK fusion prevalence than adults. (nakata2024prevalenceofneurotrophic pages 2-4, kubota2025currentmanagementof pages 1-2)
2) **Testing context**: in large clinicogenomic cohorts, testing tends to occur in **advanced/metastatic disease**; in the Japanese C-CAT cohort, most profiled patients had metastatic disease at the time of comprehensive genomic profiling (CGP). (nakata2024prevalenceofneurotrophic pages 2-4)

### Tumor-type examples and phenotype annotations (illustrative)
**Thyroid carcinoma (NTRK1/NTRK3 fusions):** NTRK fusion-positive thyroid cancers include papillary thyroid carcinoma (PTC), poorly differentiated thyroid carcinoma (PDTC), and anaplastic thyroid carcinoma (ATC). (marczyk2025ntrkfusion–positivethyroid pages 1-2)

**Sarcoma:** NTRK fusions are present in soft tissue sarcomas (STS), with pediatric enrichment and variable histologic distribution by age. (kubota2025currentmanagementof pages 2-2, nakata2024prevalenceofneurotrophic pages 2-4)

### Suggested ontology term scaffolding (for knowledge-base integration)
Because phenotypes are histology-driven, ontology annotation should generally be layered:
- **Primary disease layer (histology/site):** e.g., “papillary thyroid carcinoma”, “soft tissue sarcoma”, “salivary gland carcinoma” (not all codes retrievable here).
- **Molecular feature layer:** “NTRK gene fusion” (molecular abnormality).

**Example HPO (symptom/sign) terms (tumor-generic, for downstream curation):**
- Neoplasm (**HP:0002664**)
- Metastatic neoplasm (**HP:0030800**)

**Example UBERON (anatomy) terms:**
- Thyroid gland (**UBERON:0002046**) (thyroid cases) (marczyk2025ntrkfusion–positivethyroid pages 1-2)
- Salivary gland (**UBERON:0001830**) (head & neck enrichment) (nakata2024prevalenceofneurotrophic pages 2-4)

(These ontology suggestions are provided as standard mappings; specific ontology IDs were not provided in the retrieved primary sources.)

---

## 4. Genetic / Molecular Information

### Causal genes
- **NTRK1, NTRK2, NTRK3** (encode TRKA/TRKB/TRKC). (vingiani2023pantrkimmunohistochemistryas pages 1-3, nakata2024prevalenceofneurotrophic pages 1-2)

### Fusion structure and common partners
NTRK fusions typically involve a 5’ fusion partner joined to the 3’ region of NTRK containing the kinase domain, leading to kinase activation; Vingiani et al. describe fusions as “**3’ regions of NTRK genes… fused with 5’ fusion partners**.” (Cancer Biomarkers; 2023-11; https://doi.org/10.3233/cbm-220357) (vingiani2023pantrkimmunohistochemistryas pages 1-3)

Examples of recurrent fusions in large cohorts include:
- **ETV6::NTRK3** (prominent in head & neck cancers in the Japanese cohort). (nakata2024prevalenceofneurotrophic pages 4-7, nakata2024prevalenceofneurotrophic pages 1-2)
- **LMNA::NTRK1** (noted among STS in Japan). (nakata2024prevalenceofneurotrophic pages 1-2)
- **TPM3::NTRK1** (seen as a rare IHC-negative/NGS-positive case in NSCLC in Vingiani). (vingiani2023pantrkimmunohistochemistryas pages 1-3)

### Somatic vs germline
The retrieved evidence frames NTRK fusions as tumor genomic drivers detected by tumor profiling; germline NTRK fusion predisposition was not described in the retrieved sources. (nakata2024prevalenceofneurotrophic pages 2-4, bungaro2024ntrk123biologydetection pages 2-4)

### Resistance variants (on-target)
Under selective pressure from TRK inhibitors, tumors can acquire on-target kinase domain mutations, including:
- **Solvent-front mutations:** examples **NTRK1 G595R** and **NTRK3 G623R**, observed as emergent resistance in aggressive thyroid cancers treated with larotrectinib. (marczyk2025ntrkfusion–positivethyroid pages 1-2)
- Resistance “via solvent-front, gatekeeper, and xDFG mutations” is described in a 2023 safety-focused review of TRK inhibitors. (yang2023safetyofcurrent pages 4-6)

---

## 5. Environmental Information
No specific environmental toxins, lifestyle factors, or infectious etiologies were identified in the retrieved sources for NTRK fusion-positive cancers as a class.

---

## 6. Mechanism / Pathophysiology

### Core causal chain
1) Chromosomal rearrangement generates an **NTRK fusion gene**. (nakata2024prevalenceofneurotrophic pages 1-2)
2) The fusion encodes an **oncogenic TRK fusion protein**, functioning as an activating driver alteration. (nakata2024prevalenceofneurotrophic pages 1-2)
3) Targeted therapy with TRK inhibitors can induce tumor regression, but prolonged therapy can select for **on-target resistance mutations** (solvent-front, gatekeeper, xDFG). (yang2023safetyofcurrent pages 4-6, marczyk2025ntrkfusion–positivethyroid pages 1-2)

### Suggested GO and CL term scaffolding (for annotation)
- GO biological processes (examples):
  - Protein tyrosine kinase signaling pathway (**GO:0007169**)
  - Positive regulation of MAPK cascade (**GO:0043410**) (common downstream for RTKs; included as standard mapping, not explicitly enumerated in retrieved sources)
- Cell Ontology (CL) examples (depends on tumor):
  - Epithelial cell (**CL:0000066**) for carcinomas (thyroid, salivary)
  - Mesenchymal cell (**CL:0000134**) for sarcomas

(These are suggested scaffolds; explicit GO/CL IDs were not provided in the retrieved sources.)

---

## 7. Anatomical Structures Affected
NTRK fusions occur across many anatomic sites; in the Japanese national clinicogenomic cohort (C-CAT), NTRK fusions were observed across **21 tumor types**. (nakata2024prevalenceofneurotrophic pages 2-4)

**Commonly represented sites in that cohort (adult):** head and neck (including salivary), soft tissue, thyroid. (nakata2024prevalenceofneurotrophic pages 4-7, nakata2024prevalenceofneurotrophic pages 2-4)

---

## 8. Temporal Development

### Onset
NTRK fusions are found in both pediatric and adult cancers, with higher prevalence in pediatric populations. (nakata2024prevalenceofneurotrophic pages 2-4, kubota2025currentmanagementof pages 1-2)

### Progression
Testing is commonly performed in advanced disease. In the C-CAT cohort, most NTRK fusion-positive patients were profiled in the metastatic setting. (nakata2024prevalenceofneurotrophic pages 2-4)

---

## 9. Inheritance and Population

### Epidemiology (recent statistics)
Large series consistently show that NTRK fusions are **rare overall**, but have strong tumor-type and age-group enrichment.

| Study (first author, year) | Cohort/source | Country | N (denominator) | Overall prevalence of NTRK fusions | Tumor-type-specific prevalences (with denominators) | Adult vs pediatric prevalence | Notes |
|---|---|---|---:|---|---|---|---|
| Nakata, 2024 | C-CAT clinicogenomic cohort of solid tumors profiled by CGP | Japan | 46,621 patients | 91/46,621 = 0.20% (nakata2024prevalenceofneurotrophic pages 2-4, nakata2024prevalenceofneurotrophic pages 1-2) | Head & neck: 22/1,678 = 1.31%; thyroid: 7/534 = 1.31%; soft tissue sarcoma: 19/2,077 = 0.91%; lung cancers: 0.08%; bowel cancers MSI-stable: 3/6,661 = 0.05%; bowel cancers MSI-high: 2/742 = 0.27%; rare types included testis cancer 1/84 and peripheral nervous system cancer 1/78 (nakata2024prevalenceofneurotrophic pages 4-7, nakata2024prevalenceofneurotrophic pages 7-9, nakata2024prevalenceofneurotrophic pages 2-4, nakata2024prevalenceofneurotrophic pages 1-2) | Adults: 74/45,613 = 0.16%; pediatrics: 17/1,008 = 1.69% (nakata2024prevalenceofneurotrophic pages 7-9, nakata2024prevalenceofneurotrophic pages 2-4, nakata2024prevalenceofneurotrophic pages 1-2) | Fusions found across 21 tumor types and 38 partner genes; NTRK1 47/97 (49.5%), NTRK3 42/97 (44.2%), NTRK2 6/97 (6.3%); ETV6::NTRK3 dominated head/neck cancers (22 cases); in STS, recurrent fusions included ETV6::NTRK3 (n=7) and LMNA::NTRK1 (n=5) (nakata2024prevalenceofneurotrophic pages 4-7, nakata2024prevalenceofneurotrophic pages 1-2) |
| Bungaro, 2024 | Review summarizing large pan-cancer sequencing series (Solomon et al., Rosen et al., Westphalen et al.; cited in review) | Multinational / pan-cancer | 33,997; 26,312; 295,676 patients across cited series | 0.26% (33,997-case series); ~0.28% (26,312-case series); 0.30% (295,676-case real-world series) (bungaro2024ntrk123biologydetection pages 2-4, kubota2025currentmanagementof pages 1-2) | Rare enriched tumors: infantile/congenital fibrosarcoma 90.56%; secretory breast carcinoma 92.87%; congenital mesoblastic nephroma 21.52%; common tumors: NSCLC ~0.17%, colorectal adenocarcinoma ~0.26%, cutaneous melanoma ~0.31%, non-secretory breast carcinoma ~0.60% (bungaro2024ntrk123biologydetection pages 2-4) | In the 295,676-patient real-world series cited by the review: adults 0.28% vs children 1.34% (kubota2025currentmanagementof pages 1-2) | Highlights strong enrichment in pediatric/rare histologies versus very low rates in unselected adult solid tumors; ETV6::NTRK3 strongly associated with secretory breast carcinoma (reported in 92% of cases in cited data) (bungaro2024ntrk123biologydetection pages 2-4) |
| Kubota, 2025 | Sarcoma-focused review citing Japanese and meta-analytic datasets | Japan / multinational literature | 46,621-patient Japanese cohort; sarcoma meta-analysis denominators not fully shown in excerpt | In Japanese cohort, 91/46,621 = 0.20% overall NTRK positivity (kubota2025currentmanagementof pages 2-2) | Adult STS: 0.57%; childhood STS: 5.06%; meta-analysis estimates: soft tissue sarcoma 0.69%, bone sarcoma 0.16%; most frequent adult NTRK-positive sarcoma histologies included MPNST 2.97%, fibrosarcoma 2.75%, IMT 2.27%, STS NOS 1.70%, myxofibrosarcoma ~1.31% (kubota2025currentmanagementof pages 2-2) | Adult STS 0.57% vs childhood STS 5.06% in Japanese analysis (kubota2025currentmanagementof pages 2-2) | Pediatric NTRK-positive sarcomas were dominated by fibrosarcoma (~52%), followed by solitary fibrous tumor/hemangiopericytoma (20%), chondrosarcoma (8.3%), undifferentiated STS (5.0%), and MPNST (4.65%); review emphasizes higher prevalence in younger patients (kubota2025currentmanagementof pages 2-2) |


*Table: This table compiles key prevalence estimates for NTRK fusion-positive cancers across large pan-cancer cohorts and sarcoma-focused analyses. It highlights the consistently low overall prevalence in adult solid tumors, contrasted with marked enrichment in pediatric and rare histologic subtypes.*

Key recent datapoints:
- **Japan (C-CAT, 2019–2023; published 2024-06):** 91/46,621 = **0.20%** overall; pediatric **1.69%** vs adult **0.16%**; highest among large adult tumor categories were head & neck and thyroid (~1.31% each) and STS (~0.91%). (nakata2024prevalenceofneurotrophic pages 2-4, nakata2024prevalenceofneurotrophic pages 1-2)
- **Pan-cancer sequencing estimates summarized in 2024 review:** prevalence ~0.26–0.30% in large unselected cohorts, but >90% in certain rare histologies (infantile fibrosarcoma; secretory breast carcinoma). (bungaro2024ntrk123biologydetection pages 2-4)

### Population demographics
Sex ratios and detailed geographic distributions were not reported in the retrieved excerpts.

---

## 10. Diagnostics

### Diagnostic strategy (current implementation)
A common real-world approach is:
1) **Screen** with pan-TRK immunohistochemistry (IHC), especially in tumor types where NTRK fusions are rare, to enrich candidates.
2) **Confirm** with nucleic-acid assays—preferably **RNA-based NGS**; DNA-based NGS may miss fusions due to intronic complexity.

Bungaro & Garbo note that DNA-based NGS can miss NTRK fusions “**due to large intronic regions**,” motivating panels “capable of detecting all NTRK rearrangements.” (Precision Cancer Medicine; 2024-09; https://doi.org/10.21037/pcm-23-19) (bungaro2024ntrk123biologydetection pages 5-6)

### Test performance and pitfalls (recent data)
Vingiani et al. (2023) evaluated VENTANA pan-TRK IHC vs an RNA fusion panel in 117 evaluable cases and found:
- sensitivity **91.7%**, specificity **81.9%**, NPV **98.8%**, PPV **36.7%**. (vingiani2023pantrkimmunohistochemistryas pages 1-3, vingiani2023pantrkimmunohistochemistryas media 404d7635)
- among 30 IHC-positive cases, only 11 (37%) were NGS-confirmed, emphasizing the need for confirmatory testing. (vingiani2023pantrkimmunohistochemistryas pages 1-3)

| Modality | Typical role | Strengths | Limitations / pitfalls | Key performance metrics / notes |
|---|---|---|---|---|
| pan-TRK IHC | Screening (especially low-prevalence tumors); reflex to molecular confirmation | Widely available, relatively fast and inexpensive; high negative predictive value makes it useful to enrich cases for downstream testing; aligns with ESMO-style two-step workflows in low-prevalence settings | False positives from physiologic/non-specific TRK expression; performance is tumor-type dependent; lower specificity in breast and salivary carcinomas; in sarcomas both sensitivity and specificity can be poor; some false negatives occur, including occasional NTRK1-rearranged NSCLC | In Vingiani 2023, sensitivity 91.7%, specificity 81.9%, NPV 98.8%, PPV 36.7%; among 30 IHC-positive cases, only 11 (37%) were NGS-confirmed; 1 of 87 IHC-negative cases (1.1%) was NGS-positive for TPM3::NTRK1 (vingiani2023pantrkimmunohistochemistryas pages 1-3, vingiani2023pantrkimmunohistochemistryas media 404d7635, bungaro2024ntrk123biologydetection pages 5-6) |
| RNA-NGS | Confirmatory / preferred comprehensive fusion detection | Preferred assay for expressed fusion transcripts; can detect diverse/novel fusion partners; strong sensitivity and specificity after IHC enrichment; directly confirms transcribed fusions | More expensive and slower than IHC; requires adequate RNA quality from FFPE, which can be challenging | In MSI-high mCRC after IHC enrichment, sensitivity 90% and specificity 100%; guideline-preferred confirmatory approach in many settings (vingiani2023pantrkimmunohistochemistryas pages 1-3, demols2023atwostepdiagnostic pages 6-6) |
| DNA-NGS | Confirmatory / broad genomic profiling, often paired with RNA | Enables simultaneous assessment of multiple biomarkers and broad tumor profiling; useful when integrated into comprehensive genomic profiling workflows; FDA-approved companion diagnostics exist for some platforms | May miss actionable NTRK fusions because large intronic regions and complex breakpoints are hard to cover; less reliable than RNA alone for some rearrangements, so RNA add-on is often needed | Bungaro 2024 notes DNA-based NGS can miss fusions due to large intronic regions; panels capable of detecting all NTRK rearrangements and/or RNA confirmation are advised (bungaro2024ntrk123biologydetection pages 5-6) |
| FISH | Confirmatory in selected contexts; useful when a specific recurrent fusion is strongly suspected or for discordant cases | Can be effective for highly recurrent canonical rearrangements (for example, tumor types enriched for specific fusions); useful orthogonal method when IHC/NGS disagree | Limited breadth for novel partners; lower sensitivity/robustness in some tumor types; not recommended as a universal stand-alone method; labor-intensive and may require multiple probes | In MSI-high mCRC, sensitivity 78%, specificity 100%, robustness 70%; Schraa 2023 concluded FISH was not recommended for routine NTRK fusion detection in mCRC because of limited sensitivity and robustness (demols2023atwostepdiagnostic pages 6-6) |
| RT-PCR / qRT-PCR (including 5'/3' imbalance assays) | Confirmatory in restricted settings with known recurrent fusions; niche use after screening | Fast and potentially highly sensitive when the target fusion/rearrangement pattern is known; practical for tumors with stereotyped fusions | Limited to known fusions or known imbalance patterns; poor fit for pan-cancer discovery because many NTRK fusion partners are diverse/novel | Bungaro 2024 states RT-PCR is mainly suitable for tumors with high prevalence of a specific known fusion (e.g., ETV6::NTRK3 in secretory tumors); in MSI-high mCRC, qRT-PCR sensitivity 100% and specificity 100%, but robustness was 70% (bungaro2024ntrk123biologydetection pages 5-6, demols2023atwostepdiagnostic pages 6-6) |


*Table: This table compares the main laboratory approaches used to detect NTRK fusions, summarizing their clinical role, advantages, and known pitfalls. It is useful for selecting testing strategies and understanding why screening with pan-TRK IHC is often paired with confirmatory RNA-based sequencing.*

**Visual evidence (diagnostic performance):** tables containing the IHC vs NGS correlation and derived sensitivity/specificity/NPV/PPV were extracted from Vingiani et al. (2023). (vingiani2023pantrkimmunohistochemistryas media 404d7635)

### Differential diagnosis
False-positive pan-TRK staining can occur due to physiologic/non-specific expression; in some tumor classes, IHC sensitivity/specificity are poor, particularly in sarcomas. (bungaro2024ntrk123biologydetection pages 5-6)

---

## 11. Outcome / Prognosis

### Prognosis with targeted therapy (selected real-world statistic)
In a single-institution thyroid cancer cohort (n=8; published 2024-08), larotrectinib was associated with a median PFS of **24.7 months** and median OS of **43.8 months**. (Journal of the Endocrine Society; 2024-08; https://doi.org/10.1210/jendso/bvae158) (elghawy2024singleinstitutionexperienceof pages 1-2)

Because NTRK fusion-positive cancer spans many histologies, prognosis is highly tumor-type and stage dependent; broad, tumor-agnostic OS benchmarks were not extractable from the retrieved excerpts.

---

## 12. Treatment

### Current approved/standard targeted therapies
Two first-generation TRK inhibitors are widely used as tissue-agnostic therapies:
- **Larotrectinib** (highly selective TRK inhibitor)
- **Entrectinib** (TRK/ROS1/ALK inhibitor with CNS penetration)

A 2023 safety review summarized pooled larotrectinib outcomes and reported: ORR **69% (95% CI 63–75)** and median DOR **32.9 months (95% CI 27.3–41.7)**. (Expert Opinion on Drug Safety; 2023-10; https://doi.org/10.1080/14740338.2023.2274426) (yang2023safetyofcurrent pages 4-6)

Entrectinib integrated adult outcomes summarized in the same review include ORR **61%** and median DOR **13.8 months** (with intracranial ORR **63.6%** noted). (yang2023safetyofcurrent pages 4-6)

### Next-generation TRK inhibitors (post-resistance)
- **Repotrectinib (TRIDENT-1 phase 1/2):** In NTRK fusion-positive solid tumors, ORR was **59% (44–72)** in TRK TKI–naive patients (n=51) and **48% (36–60)** in TRK TKI–pretreated patients (n=69). Median PFS was **30.3 months** (TKI-naive) and **7.4 months** (TKI-pretreated). Among pretreated patients with solvent-front mutations, ORR was **53% (34–72)**. (Nature Medicine; 2026-02; https://doi.org/10.1038/s41591-025-04079-7) (besse2026repotrectinibinntrk pages 1-2)
- **Selitrectinib:** In thyroid carcinoma with acquired solvent-front mutations after larotrectinib, 3 patients treated with selitrectinib had partial responses (but durability in ATC was limited). (marczyk2025ntrkfusion–positivethyroid pages 1-2)

| Agent | Approval / tissue-agnostic indication | Key trial(s) / setting | N | ORR (95% CI) | CR / PR | Median DOR | Median PFS | OS notes | Intracranial activity | Common adverse events | Citation |
|---|---|---|---:|---|---|---|---|---|---|---|---|
| Larotrectinib | FDA tissue-agnostic approval in 2018 for adult and pediatric patients with unresectable or metastatic solid tumors harboring an NTRK gene fusion and no satisfactory alternative treatments; EMA tissue-agnostic approval also noted in reviews | Pooled phase I/II studies: LOXO-TRK-14001, SCOUT, NAVIGATE; additional single-institution thyroid cohort | 244 pooled; thyroid cohort n=8 | 69% (63–75) in pooled analysis; earlier pooled estimates 75% (61–85) and 79% reported in reviews; thyroid cohort responses 87.5% overall (1 CR, 6 PR, 1 SD) | Pooled: 26% CR, 43% PR; thyroid cohort: 12% CR, 75% PR | 32.9 months (27.3–41.7); review also cites ~34 months in pooled dataset | Thyroid cohort: 24.7 months (11.3–38.1); earlier thyroid pooled analysis cited 44.0 months | Pooled mOS not reached at 39.8 months in thyroid-focused review; thyroid cohort mOS 43.8 months (29.8–56.8) | CNS cohort ORR 30%; 24-week disease control rate 73% | Generally grade 1–2; anemia, neutrophil decrease, transaminase elevation, weight gain; dizziness and fatigue also reported; grade 3–4 AEs uncommon, ~2% discontinued for toxicity in one review | (yang2023safetyofcurrent pages 4-6, theik2024ntrktherapyamong pages 4-6, elghawy2024singleinstitutionexperienceof pages 1-2, vingiani2023pantrkimmunohistochemistryas pages 1-3) |
| Entrectinib | FDA tissue-agnostic approval in 2019/2020 for NTRK fusion-positive solid tumors; EMA approval also noted | Integrated adult analyses from STARTRK-1, STARTRK-2, ALKA-372-001; thyroid subgroup discussed in reviews | 54 adults in integrated analysis | 57% (43.2–70.8) in one review; 61% in another integrated adult summary; 63.5% reported in diagnostic review summary | 7% CR, 50% PR in one review; 7% CR noted in integrated analysis | 13.8 months in integrated summary; 12.9 months in review summary | Not consistently reported in available excerpts | Thyroid-focused review notes approval and activity; detailed OS not reported in available excerpts | Intracranial ORR 63.6% in one review; BBB penetration emphasized | Dizziness, cognitive changes, weight gain; broader pharmacovigilance signals include nervous system disorders, cardiac disorders, metabolism/nutrition disorders | (yang2023safetyofcurrent pages 4-6, theik2024ntrktherapyamong pages 4-6, vingiani2023pantrkimmunohistochemistryas pages 1-3) |
| Repotrectinib | FDA-approved next-generation ROS1/TRK inhibitor; 2024 review describes tissue-agnostic use in NTRK fusion-positive cancers, with later phase 1/2 trial providing fuller efficacy dataset | TRIDENT-1 phase 1/2 in advanced NTRK fusion-positive solid tumors; includes TKI-naive and TRK TKI-pretreated cohorts | 51 TKI-naive; 69 TKI-pretreated; safety population 565 | TKI-naive: 59% (44–72); TKI-pretreated: 48% (36–60); solvent-front mutation subgroup: 53% (34–72) | Not fully reported in available excerpts | TKI-naive: not estimable; TKI-pretreated: 9.8 months (7.4–13.0) | TKI-naive: 30.3 months (9.0–NE); TKI-pretreated: 7.4 months (3.9–9.7) | Mature OS not summarized in available excerpts | Intracranial responses in 2/3 TKI-naive and 4/6 TKI-pretreated patients with measurable brain disease; no intracranial progression reported in some NSCLC subsets | Dizziness most common (57% treatment-related; 63% overall), dysgeusia, anemia, paresthesia, dyspnea, fatigue; mostly low-grade; 4% treatment-related discontinuation | (besse2026repotrectinibinntrk pages 1-2, besse2026repotrectinibinntrk pages 5-7, bungaro2024ntrk123biologydetection pages 8-9, theik2024ntrktherapyamong pages 4-6) |
| Selitrectinib (LOXO-195/BAY2731954) | Investigational / expanded-access next-generation TRK inhibitor designed to overcome acquired on-target resistance; not described as broadly approved in available excerpts | Phase I/expanded-access studies; case-based and small-series use after resistance to first-generation TRK inhibitors; thyroid resistance cases | Phase I trial enrollment 81 in registry context; efficacy details limited in provided evidence; thyroid rescue cases n=3 | Numeric pooled ORR not available in provided excerpts | Thyroid resistance series: 3/3 partial responses after emergent solvent-front mutations | Not available in provided excerpts | Not available in provided excerpts | In thyroid ATC/PDTC resistance cases, responses occurred but ATC progressed within a year | No pooled intracranial dataset available in provided excerpts | Safety not quantified in provided excerpts; review states second-generation TRK inhibitors generally manageable | (marczyk2025ntrkfusion–positivethyroid pages 1-2, yang2023safetyofcurrent pages 4-6, theik2024ntrktherapyamong pages 4-6) |


*Table: This table summarizes currently available efficacy, safety, and regulatory information for first- and next-generation TRK inhibitors used in NTRK fusion-positive cancers. It is useful for comparing approved therapies with emerging resistance-directed agents across pooled trials and thyroid-specific real-world data.*

### Resistance mechanisms (clinically important)
Acquired on-target mutations—especially **solvent-front mutations**—are recurrent resistance mechanisms:
- NTRK3 **G623R** and NTRK1 **G595R** were observed after larotrectinib in PDTC/ATC and were associated with progression. (marczyk2025ntrkfusion–positivethyroid pages 1-2)

### Adverse events / real-world safety signals
- Repotrectinib: dizziness was the most common treatment-related adverse event (57%), and discontinuation due to TRAE occurred in 4%. (besse2026repotrectinibinntrk pages 1-2)
- Larotrectinib pooled safety summary reported low rates of grade ≥3 events and commonly noted hematologic and hepatic laboratory abnormalities. (bungaro2024ntrk123biologydetection pages 5-6, yang2023safetyofcurrent pages 4-6)

### MAXO (treatment action) suggestions
- TRK inhibitor therapy (targeted therapy; tumor-agnostic)
- Molecular tumor profiling / NGS-guided therapy selection

(MAXO term IDs were not available in the retrieved sources.)

---

## 13. Prevention

### Primary prevention
No established primary prevention exists for NTRK fusion formation in cancers as a class (not addressed in retrieved sources).

### Secondary prevention (early detection / screening)
The principal prevention-like strategy is **secondary prevention through systematic molecular testing**, enabling earlier deployment of effective targeted therapy. International practice patterns support screening (often IHC) and confirmatory sequencing workflows, particularly in low-prevalence tumors. (vingiani2023pantrkimmunohistochemistryas pages 1-3, bungaro2024ntrk123biologydetection pages 5-6)

---

## 14. Other Species / Natural Disease
No veterinary or cross-species naturally occurring NTRK fusion-positive cancer evidence was identified in the retrieved sources.

---

## 15. Model Organisms
No specific animal model organisms or engineered in vivo models were described in the retrieved excerpts. This is a gap in the currently retrieved evidence set; additional targeted searches in model-organism databases (MGI/IMPC) and translational NTRK fusion modeling literature would be required.

---

## Recent Developments and Real-World Implementations (2023–2024 emphasis)

1) **National-scale prevalence estimates with pediatric enrichment:** Nakata et al. (2024-06) quantified low overall prevalence (0.20%) but substantially higher pediatric prevalence (1.69%) in a national clinicogenomic cohort. (nakata2024prevalenceofneurotrophic pages 2-4, nakata2024prevalenceofneurotrophic pages 1-2)
2) **Operational diagnostic workflows and performance metrics:** Vingiani et al. (2023-11) provided real-world screening performance for pan-TRK IHC with high NPV but low PPV, reinforcing reflex NGS confirmation. (vingiani2023pantrkimmunohistochemistryas pages 1-3, vingiani2023pantrkimmunohistochemistryas media 404d7635)
3) **Growing emphasis on resistance-aware sequencing and next-generation inhibitors:** 2023–2024 expert reviews emphasize acquired resistance mechanisms (solvent-front/gatekeeper/xDFG) and newer agents designed to overcome them. (yang2023safetyofcurrent pages 4-6, bungaro2024ntrk123biologydetection pages 5-6)

---

## Notes on PMID requirement
Several of the retrieved sources are indexed by DOI and journal metadata, but PMIDs were not available in the retrieved excerpts for most of the key 2023–2024 papers. Where PMIDs are required for knowledge-base ingestion, an additional PubMed-specific retrieval step would be needed.


References

1. (bungaro2024ntrk123biologydetection pages 5-6): Maristella Bungaro and Edoardo Garbo. Ntrk1/2/3: biology, detection and therapy. Precision Cancer Medicine, 6:3-3, Sep 2024. URL: https://doi.org/10.21037/pcm-23-19, doi:10.21037/pcm-23-19. This article has 11 citations.

2. (vingiani2023pantrkimmunohistochemistryas pages 1-3): Andrea Vingiani, Daniele Lorenzini, Elena Conca, Chiara Costanza Volpi, Desirè Viola Trupia, Annunziata Gloghini, Federica Perrone, Elena Tamborini, Gian Paolo Dagrada, Luca Agnelli, Iolanda Capone, Adele Busico, and Giancarlo Pruneri. Pan-trk immunohistochemistry as screening tool for ntrk fusions: a diagnostic workflow for the identification of positive patients in clinical practice. Cancer Biomarkers, 38:301-309, Nov 2023. URL: https://doi.org/10.3233/cbm-220357, doi:10.3233/cbm-220357. This article has 10 citations and is from a peer-reviewed journal.

3. (yang2023safetyofcurrent pages 4-6): Adeline T. Yang and Theodore Willis Laetsch. Safety of current treatment options for ntrk fusion-positive cancers. Expert Opinion on Drug Safety, 22:1073-1089, Oct 2023. URL: https://doi.org/10.1080/14740338.2023.2274426, doi:10.1080/14740338.2023.2274426. This article has 9 citations and is from a peer-reviewed journal.

4. (nakata2024prevalenceofneurotrophic pages 2-4): Eiji Nakata, Tatsunori Osone, Toru Ogawa, Tomoyuki Taguchi, Kana Hattori, and Shinji Kohsaka. Prevalence of neurotrophic tropomyosin receptor kinase (ntrk) fusion gene positivity in patients with solid tumors in japan. Cancer Medicine, Jun 2024. URL: https://doi.org/10.1002/cam4.7351, doi:10.1002/cam4.7351. This article has 13 citations and is from a peer-reviewed journal.

5. (besse2026repotrectinibinntrk pages 1-2): Benjamin Besse, Jessica J. Lin, Lyudmila Bazhenova, Koichi Goto, Adrianus Johannes de Langen, Dong-Wan Kim, Jürgen Wolf, Christoph Springfeld, Sanjay Popat, Darren W. T. Lim, Misako Nagasaka, Jung Yong Hong, Christina S. Baik, Alice Hervieu, Victor Moreno, Nong Yang, Kanthi Kollengode, Haisu Yang, Yuanfang Xu, Christophe Y. Calvet, Yong Yuan, Amy B. Hammell, Alexander Drilon, and Benjamin J. Solomon. Repotrectinib in ntrk fusion–positive advanced solid tumors: a phase 1/2 trial. Nature Medicine, 32:682-689, Feb 2026. URL: https://doi.org/10.1038/s41591-025-04079-7, doi:10.1038/s41591-025-04079-7. This article has 1 citations and is from a highest quality peer-reviewed journal.

6. (bungaro2024ntrk123biologydetection pages 2-4): Maristella Bungaro and Edoardo Garbo. Ntrk1/2/3: biology, detection and therapy. Precision Cancer Medicine, 6:3-3, Sep 2024. URL: https://doi.org/10.21037/pcm-23-19, doi:10.21037/pcm-23-19. This article has 11 citations.

7. (nakata2024prevalenceofneurotrophic pages 1-2): Eiji Nakata, Tatsunori Osone, Toru Ogawa, Tomoyuki Taguchi, Kana Hattori, and Shinji Kohsaka. Prevalence of neurotrophic tropomyosin receptor kinase (ntrk) fusion gene positivity in patients with solid tumors in japan. Cancer Medicine, Jun 2024. URL: https://doi.org/10.1002/cam4.7351, doi:10.1002/cam4.7351. This article has 13 citations and is from a peer-reviewed journal.

8. (kubota2025currentmanagementof pages 1-2): Yuta Kubota, Masanori Kawano, Tatsuya Iwasaki, Ichiro Itonaga, Nobuhiro Kaku, Toshifumi Ozaki, and Kazuhiro Tanaka. Current management of neurotrophic receptor tyrosine kinase fusion-positive sarcoma: an updated review. Japanese Journal of Clinical Oncology, 55:313-326, Feb 2025. URL: https://doi.org/10.1093/jjco/hyaf015, doi:10.1093/jjco/hyaf015. This article has 6 citations and is from a peer-reviewed journal.

9. (marczyk2025ntrkfusion–positivethyroid pages 1-2): Vicente R. Marczyk, Sasan Fazeli, Ramona Dadu, Naifa L. Busaidy, Priyanka Iyer, Mimi I. Hu, Steven I. Sherman, Sarah Hamidi, Sayed Mohsen Hosseini, Michelle D. Williams, Salmaan Ahmed, Mark J. Routbort, Raja Luthra, Sinchita Roy-Chowdhuri, Francis Anthony San Lucas, Keyur P. Patel, David S. Hong, Mark Zafereo, Jennifer R. Wang, Anastasios Maniakas, Steven G. Waguespack, and Maria E. Cabanillas. Ntrk fusion–positive thyroid carcinoma: from diagnosis to targeted therapy. JCO Precision Oncology, Jan 2025. URL: https://doi.org/10.1200/po.24.00321, doi:10.1200/po.24.00321. This article has 10 citations and is from a peer-reviewed journal.

10. (kubota2025currentmanagementof pages 2-2): Yuta Kubota, Masanori Kawano, Tatsuya Iwasaki, Ichiro Itonaga, Nobuhiro Kaku, Toshifumi Ozaki, and Kazuhiro Tanaka. Current management of neurotrophic receptor tyrosine kinase fusion-positive sarcoma: an updated review. Japanese Journal of Clinical Oncology, 55:313-326, Feb 2025. URL: https://doi.org/10.1093/jjco/hyaf015, doi:10.1093/jjco/hyaf015. This article has 6 citations and is from a peer-reviewed journal.

11. (nakata2024prevalenceofneurotrophic pages 4-7): Eiji Nakata, Tatsunori Osone, Toru Ogawa, Tomoyuki Taguchi, Kana Hattori, and Shinji Kohsaka. Prevalence of neurotrophic tropomyosin receptor kinase (ntrk) fusion gene positivity in patients with solid tumors in japan. Cancer Medicine, Jun 2024. URL: https://doi.org/10.1002/cam4.7351, doi:10.1002/cam4.7351. This article has 13 citations and is from a peer-reviewed journal.

12. (nakata2024prevalenceofneurotrophic pages 7-9): Eiji Nakata, Tatsunori Osone, Toru Ogawa, Tomoyuki Taguchi, Kana Hattori, and Shinji Kohsaka. Prevalence of neurotrophic tropomyosin receptor kinase (ntrk) fusion gene positivity in patients with solid tumors in japan. Cancer Medicine, Jun 2024. URL: https://doi.org/10.1002/cam4.7351, doi:10.1002/cam4.7351. This article has 13 citations and is from a peer-reviewed journal.

13. (vingiani2023pantrkimmunohistochemistryas media 404d7635): Andrea Vingiani, Daniele Lorenzini, Elena Conca, Chiara Costanza Volpi, Desirè Viola Trupia, Annunziata Gloghini, Federica Perrone, Elena Tamborini, Gian Paolo Dagrada, Luca Agnelli, Iolanda Capone, Adele Busico, and Giancarlo Pruneri. Pan-trk immunohistochemistry as screening tool for ntrk fusions: a diagnostic workflow for the identification of positive patients in clinical practice. Cancer Biomarkers, 38:301-309, Nov 2023. URL: https://doi.org/10.3233/cbm-220357, doi:10.3233/cbm-220357. This article has 10 citations and is from a peer-reviewed journal.

14. (demols2023atwostepdiagnostic pages 6-6): Anne Demols, Laureen Rocq, Luis Perez-Casanova, Manon Charry, Nancy De Nève, Ali Ramadhan, Claude Van Campenhout, Sarah De Clercq, Calliope Maris, Jean Closset, Valerio Lucidi, Isabelle Salmon, and Nicky D’Haene. A two-step diagnostic approach for ntrk gene fusion detection in biliary tract and pancreatic adenocarcinomas. The Oncologist, 28:e520-e525, Mar 2023. URL: https://doi.org/10.1093/oncolo/oyad075, doi:10.1093/oncolo/oyad075. This article has 16 citations.

15. (elghawy2024singleinstitutionexperienceof pages 1-2): Omar Elghawy, Adam Barsouk, A. Heidlauf, Simon Chen, Roger B. Cohen, and Lova L. Sun. Single-institution experience of larotrectinib therapy for patients with ntrk fusion-positive thyroid carcinoma. Journal of the Endocrine Society, Aug 2024. URL: https://doi.org/10.1210/jendso/bvae158, doi:10.1210/jendso/bvae158. This article has 6 citations and is from a peer-reviewed journal.

16. (theik2024ntrktherapyamong pages 4-6): Nyein Wint Yee Theik, Meri Muminovic, Andres M. Alvarez-Pinzon, Ahmed Shoreibah, Atif M. Hussein, and Luis E. Raez. Ntrk therapy among different types of cancers, review and future perspectives. International Journal of Molecular Sciences, 25:2366, Feb 2024. URL: https://doi.org/10.3390/ijms25042366, doi:10.3390/ijms25042366. This article has 28 citations.

17. (besse2026repotrectinibinntrk pages 5-7): Benjamin Besse, Jessica J. Lin, Lyudmila Bazhenova, Koichi Goto, Adrianus Johannes de Langen, Dong-Wan Kim, Jürgen Wolf, Christoph Springfeld, Sanjay Popat, Darren W. T. Lim, Misako Nagasaka, Jung Yong Hong, Christina S. Baik, Alice Hervieu, Victor Moreno, Nong Yang, Kanthi Kollengode, Haisu Yang, Yuanfang Xu, Christophe Y. Calvet, Yong Yuan, Amy B. Hammell, Alexander Drilon, and Benjamin J. Solomon. Repotrectinib in ntrk fusion–positive advanced solid tumors: a phase 1/2 trial. Nature Medicine, 32:682-689, Feb 2026. URL: https://doi.org/10.1038/s41591-025-04079-7, doi:10.1038/s41591-025-04079-7. This article has 1 citations and is from a highest quality peer-reviewed journal.

18. (bungaro2024ntrk123biologydetection pages 8-9): Maristella Bungaro and Edoardo Garbo. Ntrk1/2/3: biology, detection and therapy. Precision Cancer Medicine, 6:3-3, Sep 2024. URL: https://doi.org/10.21037/pcm-23-19, doi:10.21037/pcm-23-19. This article has 11 citations.
