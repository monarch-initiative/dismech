---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T20:04:15.615284'
end_time: '2026-04-05T20:14:12.046503'
duration_seconds: 596.43
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Merkel Cell Carcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Merkel Cell Carcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Merkel Cell Carcinoma** covering all of the
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
- **Disease Name:** Merkel Cell Carcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Merkel Cell Carcinoma** covering all of the
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


## Merkel Cell Carcinoma (MCC) — Comprehensive Disease Characteristics Report

### Target Disease
- **Disease name:** Merkel cell carcinoma (MCC) (chang2024theroleof pages 1-2)
- **Category:** Rare, aggressive **cutaneous neuroendocrine carcinoma** (skin cancer of neuroendocrine origin) (chang2024theroleof pages 1-2)
- **MONDO ID:** Not retrieved from the accessed full texts in this run; requires direct lookup in MONDO (explicitly unavailable from gathered sources).

---

## 1. Disease Information

### 1.1 Concise overview
Merkel cell carcinoma (MCC) is a rare, clinically aggressive neuroendocrine malignancy of the skin that often metastasizes early and has a substantial risk of recurrence after initial treatment (chang2024theroleof pages 1-2, akaike2024merkelcellcarcinoma pages 1-2).

### 1.2 Key identifiers and coding
- **MeSH (Medical Subject Headings):** *Carcinoma, Merkel Cell* (**MeSH ID: D015266**) as used in ClinicalTrials.gov MeSH mapping for MCC (NCT03747484 chunk 2, NCT03599713 chunk 3).
- **ICD-10 / ICD-11:** A rare-disease nomenclature analysis notes that in ICD-10 some entities may be “non-coded” or grouped, and that ICD-11 provides more detailed coding, but the MCC-specific ICD-11 code itself is not reliably extractable from the retrieved excerpts here (li2024classificationandepidemiologic pages 2-3). Practical implication: MCC is often captured within broader “skin cancer” categories in legacy ICD-10-based registries, complicating epidemiology and harmonization across datasets (li2024classificationandepidemiologic pages 2-3).
- **Orphanet / OMIM / UMLS:** The accessed Orphanet/OMIM codes for MCC were not present in retrieved full text; a dedicated Orphanet query is needed (not available in current evidence set) (li2024classificationandepidemiologic pages 1-2).

### 1.3 Synonyms and alternative names
Commonly used synonyms/labels in the accessed sources include:
- “Merkel cell carcinoma” and abbreviation “MCC” (chang2024theroleof pages 1-2, akaike2024merkelcellcarcinoma pages 1-2)
- “Cutaneous neuroendocrine carcinoma” (used in rare-disease classification context; mapping to MCC implied but not formally resolved to a code in retrieved excerpt) (li2024classificationandepidemiologic pages 2-3)

### 1.4 Evidence source type (individual vs aggregated)
Most epidemiology and outcomes evidence in this report is derived from aggregated disease-level sources including cancer registries, clinical trials, and meta-analyses (moraes2024efficacyandsafety pages 5-8, stang2024incidenceandrelative pages 3-5, d’angelo2024firstlineavelumabtreatment pages 3-4).

---

## 2. Etiology

### 2.1 Primary causal factors (current understanding)
A central organizing concept in MCC biology is the **dual-etiology model**:
1) **Virus-driven MCC** caused by clonal integration and continued expression of **Merkel cell polyomavirus (MCPyV) T antigens**, and  
2) **UV-associated MCC** characterized by UV mutagenesis and typically higher tumor mutational burden (TMB) (becker2024merkelcellcarcinoma pages 1-2, fojnica2023anupdatedreview pages 2-4).

A recent immunology-focused review states: “**80% of cases are driven by Merkel cell polyomavirus (MCPyV) oncoproteins that must be continually expressed for tumor survival**” (jani2023insightsintoantitumor pages 1-2).

### 2.2 Risk factors
**UV exposure and immunosuppression** are repeatedly cited as major risk factors (chang2024theroleof pages 1-2, cheng2017merkelcellpolyomavirus pages 1-2). A mechanistic paper explicitly notes: “Risk factors for developing MCC include **immunosuppression and UV-induced DNA damage** from excessive exposure to sunlight” (cheng2017merkelcellpolyomavirus pages 1-2).

**Immunosuppression and aging:** Clinical context sources emphasize chronic immunosuppression as a risk factor, and MCC is typically a disease of older adults, with high metastatic propensity (chang2024theroleof pages 1-2, akaike2024merkelcellcarcinoma pages 1-2).

### 2.3 Protective factors
High-quality protective-factor evidence (e.g., quantified effect sizes for sun protection or immunosuppression mitigation) was not present in the retrieved primary texts. However, because UV exposure is a major risk factor, UV avoidance/protection is a biologically plausible primary prevention strategy (see Prevention section) (cheng2017merkelcellpolyomavirus pages 1-2).

### 2.4 Gene–environment interactions
The strongest established interaction is that **immune competence** modulates tumor surveillance in a disease where either (i) viral antigens (MCPyV) or (ii) UV-derived neoantigens provide immunogenic targets; both etiologies are associated with high immunogenicity but differ in antigen source (becker2024merkelcellcarcinoma pages 1-2, jani2023insightsintoantitumor pages 1-2).

---

## 3. Phenotypes (Clinical Presentation) + HPO suggestions

### 3.1 Typical clinical presentation
MCC often presents as a **painless, rapidly growing cutaneous nodule** on sun-exposed skin:
- “painless, flesh-colored, rapidly growing nodule in a sun-exposed area” (chang2024theroleof pages 1-2)
- “rapidly growing, red-to-violet nodule on sun-exposed areas” (mistry2021merkelcellcarcinoma pages 1-2)

### 3.2 Nodal involvement, metastasis, and recurrence
A recent expert commentary summarizes early aggressive behavior: ~**45%** have lymph node involvement and ~**6%** have distant metastases at diagnosis (akaike2024merkelcellcarcinoma pages 1-2). The same source states that “approximately **40%** of patients experience disease recurrence… typically **within 2 years** of initial treatment” (akaike2024merkelcellcarcinoma pages 1-2).

### 3.3 Stage-associated prognosis (temporal/progression phenotype)
In an NCDB-based analysis used for neoadjuvant immunotherapy context, 5-year OS is reported to decline with increasing stage burden: ~40.3% (stage IIIA clinically occult nodes) to ~26.8% (stage IIIB clinically detected nodes) to ~13.5% (stage IV distant metastases) (chang2024theroleof pages 1-2).

### 3.4 HPO term suggestions (non-exhaustive)
Because MCC is a malignancy, many key “phenotypes” are oncology course features rather than congenital traits. Suggested HPO mappings:
- **Cutaneous nodule / skin tumor:** *Skin nodule* (HP:0200149), *Cutaneous neoplasm* (candidate; verify exact HPO label), *Rapidly progressive* (HP:0003678) (clinical rapid growth) (chang2024theroleof pages 1-2, mistry2021merkelcellcarcinoma pages 1-2)
- **Pain phenotype:** *Absent pain / painless lesion* (map to “Pain” HP:0012531 as “not present” in structured phenotyping) (chang2024theroleof pages 1-2)
- **Regional metastasis:** *Lymphadenopathy* (HP:0002716) as a proxy for nodal involvement; “lymph node metastasis” is not a standard HPO term but can be captured via oncology extensions (akaike2024merkelcellcarcinoma pages 1-2)
- **Distant metastasis:** *Metastatic neoplasm* (candidate term; verify) (akaike2024merkelcellcarcinoma pages 1-2)
- **Recurrence:** *Recurrent infections* is inappropriate; instead represent as disease-course annotation (not well captured by core HPO). Use clinical data model fields for recurrence timing (akaike2024merkelcellcarcinoma pages 1-2).

---

## 4. Genetic/Molecular Information (Mechanisms, pathways, ontology mappings)

### 4.1 Molecular subtypes: virus-positive vs virus-negative
Virus-positive MCC is typically characterized by MCPyV integration and lower somatic mutation burden, whereas MCPyV-negative tumors are often UV-driven with higher TMB (fojnica2023anupdatedreview pages 2-4, jani2023insightsintoantitumor pages 1-2).

A 2023 biomarker review provides an illustrative contrast where an MCPyV+ case showed **TMB 7 mut/Mb** vs an MCPyV− case **34 mut/Mb**, with MCPyV status assessed by CM2B4 IHC (fojnica2023anupdatedreview pages 2-4).

### 4.2 Viral oncoprotein dependencies and epigenetic/transcriptional programs
A mechanistic study in MCPyV-positive MCC showed viral small T antigen (ST) recruits **MYCL** to the **EP400** chromatin remodeling/histone acetyltransferase complex, with MYCL and EP400 required for MCC cell viability (cheng2017merkelcellpolyomavirus pages 1-2). This supports a viral-oncoprotein → transcriptional/epigenetic program → tumor maintenance causal chain.

### 4.3 Immune involvement and immune evasion
MCC is a model tumor for anti-viral tumor immunity because antigens are shared across MCPyV-driven tumors. A review summarizes that shared MCPyV oncoproteins enable measurement of MCC-directed immunity, and notes immune evasion mechanisms including “transcriptional downregulation of MHC expression… and upregulation of inhibitory molecules including PD-L1” (jani2023insightsintoantitumor pages 1-2).

### 4.4 Tumor microenvironment (TME) features and biomarkers
Exploratory biomarker analysis from the JAVELIN Merkel 200 avelumab trial describes subtype-associated immune context: MCPyV+ tumors with increased M2 macrophages and PD-L1 correlation; and in MCPyV− tumors, higher CD8+ T-cell density appeared associated with response (d’angelo2024biomarkeranalysesinvestigating pages 2-3).

### 4.5 Pathway ontology suggestions
- **GO Biological Process (examples):** *immune response*; *negative regulation of T cell activation*; *antigen processing and presentation*; *chromatin remodeling*; *histone acetylation*; *PI3K signaling* (MCC frequently engages PI3K/AKT/mTOR per preclinical review context) (d’angelo2024biomarkeranalysesinvestigating pages 2-3, pedersen2024merkelcellcarcinoma pages 13-14, cheng2017merkelcellpolyomavirus pages 1-2).
- **Cell Ontology (CL) candidates:** *CD8-positive, alpha-beta T cell*; *macrophage* (including M2-like macrophage states); *dendritic cell* (activated dendritic cells noted in response context) (d’angelo2024biomarkeranalysesinvestigating pages 2-3).
- **CHEBI suggestions (therapeutic chemicals):** avelumab, pembrolizumab, nivolumab, retifanlimab (biologics; CHEBI may not include all mAbs; use appropriate drug ontologies if needed) (moraes2024efficacyandsafety pages 5-8, d’angelo2024firstlineavelumabtreatment pages 3-4).

---

## 5. Environmental Information

### 5.1 UV radiation
UV-associated DNA damage is a repeatedly cited etiologic component (cheng2017merkelcellpolyomavirus pages 1-2, fojnica2023anupdatedreview pages 2-4).

### 5.2 Infectious agents
MCPyV is the key infectious agent in a large fraction of MCC cases, and viral oncoproteins must be persistently expressed for tumor survival in virus-driven MCC (jani2023insightsintoantitumor pages 1-2).

---

## 6. Mechanism / Pathophysiology (causal chains)

### 6.1 Virus-driven chain (conceptual)
MCPyV infection → clonal integration and expression of T antigens → perturbation of cell-cycle control (e.g., RB pathway via LT) and activation of epigenetic/transcriptional programs (e.g., ST–MYCL–EP400 complex) → immune evasion (MHC downregulation, PD-L1 upregulation) → tumor persistence and progression (jani2023insightsintoantitumor pages 1-2, cheng2017merkelcellpolyomavirus pages 1-2).

### 6.2 UV-driven chain (conceptual)
Chronic UV exposure → UV-induced DNA damage → high mutational burden / neoantigen landscape → selection for immune evasion phenotypes and aggressive neuroendocrine carcinoma phenotype → early metastasis/recurrence (cheng2017merkelcellpolyomavirus pages 1-2, fojnica2023anupdatedreview pages 2-4).

---

## 7. Anatomical Structures Affected (UBERON suggestions)

### 7.1 Primary sites
Primary tumor arises in **skin** (UBERON:0002097) (mistry2021merkelcellcarcinoma pages 1-2).

### 7.2 Regional and distant spread
- **Regional lymph nodes** (UBERON:0000029) (nodal involvement common) (akaike2024merkelcellcarcinoma pages 1-2).
- Distant metastasis can involve multiple organs; specific organ distributions were not quantified in the retrieved texts.

### 7.3 Cell type
Neuroendocrine carcinoma phenotype; cell-of-origin remains debated, with evidence for lineage reprogramming models (ATOH1) in preclinical systems (pedersen2024merkelcellcarcinoma pages 14-15).

---

## 8. Temporal Development

### 8.1 Onset
Predominantly affects older adults; aggressive growth is typical (akaike2024merkelcellcarcinoma pages 1-2, chang2024theroleof pages 1-2).

### 8.2 Progression and recurrence
- Early metastasis at diagnosis is common (nodal ~45%, distant ~6%) (akaike2024merkelcellcarcinoma pages 1-2).
- Recurrence is frequent: ~40% recurrence, with many distant recurrences within ~2 years (akaike2024merkelcellcarcinoma pages 1-2).

---

## 9. Inheritance and Population

### 9.1 Epidemiology (recent data)
A population-based German registry analysis (North Rhine–Westphalia; 18 million population coverage) reported:
- Age-standardized incidence **5.2 per million person-years (men)** and **3.8 per million person-years (women)** (2008–2021) (stang2024incidenceandrelative pages 3-5).
- 5-year relative survival **58.8% in men** and **70.7% in women**, and “the first two years are particularly critical” (stang2024incidenceandrelative pages 3-5).

A 2024 commentary notes MCC incidence has risen to approximately **3,000 cases annually in the USA** (akaike2024merkelcellcarcinoma pages 1-2).

### 9.2 Germline genetics / inheritance
No Mendelian inheritance pattern is established for typical MCC; most molecular discussion in retrieved sources concerns **somatic** and **viral** carcinogenesis rather than germline inheritance.

---

## 10. Diagnostics

### 10.1 Histopathology and immunohistochemistry
A 2023 review describes classic morphology and a practical diagnostic IHC panel:
- Morphology: “small, round, and blue undifferentiated cells with high mitotic rate…” (fojnica2023anupdatedreview pages 2-4).
- Typical IHC: **CK20 positive** and neuroendocrine markers **synaptophysin** and **chromogranin-A**; usually negative for melanoma markers (S-100, Melan-A, HMB-45), lymphoid markers (LCA), and **TTF-1** (helpful vs metastatic small-cell lung carcinoma) (fojnica2023anupdatedreview pages 2-4).

### 10.2 Imaging and staging
Staging evaluation commonly includes nodal assessment (including SLNB when feasible), and cross-sectional imaging (CT/MRI) and/or PET as clinically indicated (mistry2021merkelcellcarcinoma pages 1-2, chang2024theroleof pages 1-2).

### 10.3 Biomarkers and liquid biopsy (real-world implementation)
**AMERK (MCPyV oncoprotein antibodies):** A ctDNA-focused review states: “In these virus-positive cases, MCPyV oncoprotein antibody (AMERK) titers can be used to monitor disease progression, recurrence risk, and response to therapy” and recommends establishing baseline titers within ~3 months of surgery because titers decline after clinically evident disease is eliminated (prakash2023evolvingapplicationsof pages 2-4).

**ctDNA (tumor-informed) for MRD/surveillance:** The same review summarizes prospective evidence that ctDNA can precede clinically evident recurrence and provides near-term recurrence-risk estimates. In one cited prospective dataset (125 patients; 328 blood samples), recurrence risk within **60 days** of a positive ctDNA test was estimated at **57%**, while risk after a negative test was **0%** within 60 days and **3%** from 60–90 days (prakash2023evolvingapplicationsof pages 4-5).

### 10.4 Differential diagnosis
MCC must be distinguished from metastatic small-cell lung carcinoma; CK20+/TTF-1− pattern supports MCC in appropriate clinical context (fojnica2023anupdatedreview pages 2-4).

---

## 11. Outcomes / Prognosis

Key quantitative survival outcomes from recent evidence are summarized in the table artifact below.

| Domain | Finding (with numbers) | Population/setting | Study design | Year | DOI/URL | Evidence type | Citation ID |
|---|---|---|---|---|---|---|---|
| Epidemiology / incidence | Age-standardized incidence: **5.2 per million person-years in men** and **3.8 per million person-years in women** | North Rhine-Westphalia, Germany; **2,164** newly diagnosed MCC cases (2008–2021) | Population-based cancer registry analysis | 2024 | https://doi.org/10.3390/cancers16112158 | Human registry | (stang2024incidenceandrelative pages 3-5) |
| Survival / prognosis | **5-year relative survival**: **58.8% men** vs **70.7% women**; first **2 years** after diagnosis were most critical | North Rhine-Westphalia, Germany; MCC registry cohort | Population-based cancer registry analysis | 2024 | https://doi.org/10.3390/cancers16112158 | Human registry | (stang2024incidenceandrelative pages 3-5) |
| Checkpoint inhibitor outcomes (avelumab, first-line) | **4-year OS rate 38%**; median **OS 20.3 months**; **62.1%** had died by data cutoff; no treatment-related deaths reported | Metastatic MCC, JAVELIN Merkel 200 part B, first-line avelumab | Phase II trial, long-term follow-up | 2024 | https://doi.org/10.1016/j.esmoop.2024.103461 | Human clinical trial | (d’angelo2024firstlineavelumabtreatment pages 3-4, d’angelo2024firstlineavelumabtreatment pages 4-6) |
| Checkpoint inhibitor outcomes (meta-analysis) | Pooled **ORR 53.79%** (95% CI 47.80–59.68); **DCR 61.65%** (54.85–68.03) | **563** patients for ORR; **552** for DCR across PD-1/PD-L1 studies in MCC | Systematic review and meta-analysis | 2024 | https://doi.org/10.1186/s12885-024-13129-1 | Human meta-analysis | (moraes2024efficacyandsafety pages 5-8) |
| Checkpoint inhibitor outcomes (meta-analysis) | Pooled **OS 24 months 65.05%** (44.04–81.49); **OS 36 months 59.58%** (39.62–76.81) | PD-1/PD-L1 blockade studies in MCC | Systematic review and meta-analysis | 2024 | https://doi.org/10.1186/s12885-024-13129-1 | Human meta-analysis | (moraes2024efficacyandsafety pages 5-8) |
| Checkpoint inhibitor outcomes (meta-analysis) | Pooled **PFS 6 months 51.78%** (37.83–65.45); **12 months 46.12%** (29.44–63.72); **36 months 28.73%** (16.57–45.02) | PD-1/PD-L1 blockade studies in MCC | Systematic review and meta-analysis | 2024 | https://doi.org/10.1186/s12885-024-13129-1 | Human meta-analysis | (moraes2024efficacyandsafety pages 5-8) |
| Checkpoint inhibitor safety (meta-analysis) | Any-grade **TRAEs 61.72%**; grade **≥3 TRAEs 17.60%**; immune-related AEs **22.76%**; discontinuation due to TRAEs **12.74%**; treatment-related death **3.45%** | PD-1/PD-L1 blockade studies in MCC | Systematic review and meta-analysis | 2024 | https://doi.org/10.1186/s12885-024-13129-1 | Human meta-analysis | (moraes2024efficacyandsafety pages 5-8) |
| Real-world avelumab | Real-world **response rate 59%**; **disease-control rate 70%**; **37% complete response**; any-grade toxicity **34%**; grade **3–4 toxicity 14%**; discontinuation due to toxicity **6%** | Israel multicenter cohort; **62** MCC patients, including **22% immunosuppressed** | Retrospective multicenter real-world study | 2023 | https://doi.org/10.1002/cam4.5890 | Human real-world cohort | (averbuch2023avelumabforthe pages 4-5) |
| Neoadjuvant immunotherapy | **19.7%** received NIO; primary tumor **ypT0 45.2%**; nodal **ypN0 17.9%**; combined **ypT0 ypN0 16/223**; matched **5-year OS 57% vs 44%** (NIO vs no NIO) | NCDB MCC patients with clinically detected regional lymph node metastasis; **1,809** selected, **356** received NIO | National database retrospective comparative study | 2024 | https://doi.org/10.1245/s10434-024-15478-4 | Human registry/observational comparative study | (chang2024theroleof pages 1-2) |
| PD(L)1-refractory salvage therapy | Aggregate retrospective **response rate 32% (13/41)** with **4 CR** and **9 PR**; prospective study **31% (8/26)** with **4 CR** and **4 PR** | Advanced MCC refractory to anti-PD(L)1; ipilimumab added, often with nivolumab | Review/commentary synthesizing prospective + retrospective salvage data | 2024 | https://doi.org/10.1136/jitc-2024-009396 | Human evidence synthesis | (akaike2024merkelcellcarcinoma pages 1-2) |
| PD(L)1-refractory salvage toxicity | Grade **≥III irAEs 29%** in retrospective cohort (**N=41**) and **36%** in prospective cohort (**N=50**); ~**70%** did not benefit | PD(L)1-refractory advanced MCC treated with CTLA-4 add-on approaches | Review/commentary synthesizing salvage studies | 2024 | https://doi.org/10.1136/jitc-2024-009396 | Human evidence synthesis | (akaike2024merkelcellcarcinoma pages 1-2) |


*Table: This table compiles key quantitative results for Merkel cell carcinoma across epidemiology, prognosis, immunotherapy efficacy, safety, and real-world implementation. It is useful as a compact evidence summary for knowledge-base population and citation tracking.*

Additionally, the 2024 JAVELIN Merkel 200 part B report shows overall survival curves (first-line avelumab) and OS stratified by PD-L1 status; these figures support the long-term survival claims and are included as visual evidence (d’angelo2024firstlineavelumabtreatment media 30169c3d, d’angelo2024firstlineavelumabtreatment media a5f140c8).

---

## 12. Treatment

### 12.1 Standard local therapy (locoregional disease)
Local control commonly relies on surgery (wide local excision) and radiotherapy; systemic therapy is driven by stage and recurrence/metastasis risk (chang2024theroleof pages 1-2, fojnica2023anupdatedreview pages 2-4).

### 12.2 Checkpoint inhibitors (current standard for advanced disease)
Recent evidence strongly supports PD-1/PD-L1 blockade as a mainstay of advanced MCC management:
- **First-line avelumab** (JAVELIN Merkel 200 part B, 4-year follow-up): “4-year OS rate of **38%**” and median OS **20.3 months** were reported (ESMO Open; May 2024; https://doi.org/10.1016/j.esmoop.2024.103461) (d’angelo2024firstlineavelumabtreatment pages 3-4, d’angelo2024firstlineavelumabtreatment pages 4-6). OS curves are shown in the retrieved figure (d’angelo2024firstlineavelumabtreatment media 30169c3d).
- **Meta-analysis (2024, BMC Cancer)** of PD-1/PD-L1 inhibitors in MCC reported pooled ORR **53.79%** and grade ≥3 TRAEs **17.60%** (https://doi.org/10.1186/s12885-024-13129-1) (moraes2024efficacyandsafety pages 5-8).
- **Real-world avelumab (Israel multicenter)**: real-world response rate **59%**, disease-control rate **70%**, complete response **37%**, and grade 3–4 toxicity **14%** (https://doi.org/10.1002/cam4.5890; Apr 2023) (averbuch2023avelumabforthe pages 4-5).

**Retifanlimab regulatory note:** A 2023 review states retifanlimab-dlwr (anti-PD-1) is FDA-approved (2023) among ICI options for MCC (fojnica2023anupdatedreview pages 2-4).

### 12.3 Neoadjuvant immunotherapy (emerging real-world uptake)
In an NCDB analysis of MCC with clinically detected regional lymph node metastasis, neoadjuvant immunotherapy use was ~19.7%, with ypT0 in 45.2% and improved overall survival in matched analysis (5-year OS 57% vs 44%) (https://doi.org/10.1245/s10434-024-15478-4; published online June 2024) (chang2024theroleof pages 1-2).

### 12.4 PD-(L)1 refractory disease (salvage strategies)
A 2024 commentary synthesizing prospective and retrospective data reports that adding ipilimumab (CTLA-4 blockade, often with nivolumab) after PD-(L)1 failure yields ~31–32% response rates, with grade ≥III irAEs in ~29–36%, and that ~70% will not benefit—supporting a major unmet need (https://doi.org/10.1136/jitc-2024-009396; July 2024) (akaike2024merkelcellcarcinoma pages 1-2).

### 12.5 MAXO term suggestions
- Wide local excision: MAXO:0000004 (Surgical excision; verify exact MAXO label)
- Radiotherapy: MAXO:0000114 (Radiation therapy; verify)
- PD-1/PD-L1 inhibitor therapy: MAXO term for “immune checkpoint inhibitor therapy” (verify exact MAXO term)
- Sentinel lymph node biopsy: MAXO term for staging biopsy (verify)

---

## 13. Prevention

### 13.1 Primary prevention
Because UV-induced DNA damage is a documented risk factor for MCC, UV exposure reduction (sun-protective behaviors) is mechanistically justified, though MCC-specific intervention effect sizes were not available in the retrieved sources (cheng2017merkelcellpolyomavirus pages 1-2).

### 13.2 Secondary prevention (surveillance / early recurrence detection)
Secondary prevention is an active translational area:
- MCPyV oncoprotein antibody (AMERK) titers for virus-positive MCC surveillance (prakash2023evolvingapplicationsof pages 2-4).
- Tumor-informed ctDNA for minimal residual disease and early relapse detection; one synthesized prospective estimate suggests a 57% risk of clinically relevant recurrence within 60 days of a positive ctDNA test vs near-zero short-term risk after a negative test (prakash2023evolvingapplicationsof pages 4-5).

---

## 14. Other Species / Natural Disease
No naturally occurring, well-characterized MCC analog across non-human species was retrieved in the accessed texts. Veterinary/cross-species MCC-like neuroendocrine tumors may exist but would require targeted veterinary oncology searches.

---

## 15. Model Organisms (Preclinical models)

A 2024 review of MCC biology and models highlights:
- Strong reliance on **transplantable models** (cell line xenografts; emerging patient-derived xenografts) for drug testing (pedersen2024merkelcellcarcinoma pages 14-15).
- Difficulty generating faithful GEMMs for MCC due to uncertain cell-of-origin; early MCPyV T antigen mouse models often produced epidermal hyperplasia/papillomas rather than neuroendocrine MCC (pedersen2024merkelcellcarcinoma pages 14-15).
- ATOH1-driven lineage reprogramming plus sTAg in embryos can generate “small blue cell tumors resembling” MCC and expressing markers including K20 in the clumped/dot-like pattern typical of MCC (pedersen2024merkelcellcarcinoma pages 14-15).
- No syngeneic immunocompetent MCC mouse model is currently available per this review, limiting immunotherapy preclinical modeling (pedersen2024merkelcellcarcinoma pages 14-15).

---

## Expert synthesis (2023–2024 emphasis)
Recent literature converges on MCC as an immunogenic cancer with dual etiologies (viral antigens vs UV neoantigens) and a treatment paradigm dominated by immune checkpoint blockade, yet with a substantial fraction of patients (~50%) lacking durable benefit and therefore a persistent need for biomarkers and effective salvage regimens (jani2023insightsintoantitumor pages 1-2, akaike2024merkelcellcarcinoma pages 1-2, d’angelo2024biomarkeranalysesinvestigating pages 2-3). The most practice-changing real-world implementations in 2023–2024 are the expansion of PD-1/PD-L1 inhibitors as standard systemic therapy and the rapid maturation of blood-based surveillance (AMERK in virus-positive disease; ctDNA MRD surveillance particularly valuable for virus-negative disease) (prakash2023evolvingapplicationsof pages 2-4, prakash2023evolvingapplicationsof pages 4-5, d’angelo2024firstlineavelumabtreatment pages 3-4).

---

## Notes on evidence gaps (for knowledge-base completeness)
- **MONDO and Orphanet identifiers** were not extractable from the retrieved full texts; populate these fields via direct ontology lookup (e.g., MONDO, Orphanet portals).
- Several mechanistic and clinical claims in reviews cite primary PMIDs, but PMIDs were not consistently present in the retrieved excerpts; use DOI-linked PubMed records to backfill PMIDs where required by the downstream knowledge base.


References

1. (chang2024theroleof pages 1-2): Jenny H. Chang, Daphne Remulla, Chase Wehrle, Kimberly P. Woo, Fadi S. Dahdaleh, Daniel Joyce, and Samer A. Naffouje. The role of neoadjuvant immunotherapy in the management of merkel cell carcinoma with clinically detected regional lymph node metastasis. Annals of Surgical Oncology, 31:6079-6087, Jun 2024. URL: https://doi.org/10.1245/s10434-024-15478-4, doi:10.1245/s10434-024-15478-4. This article has 11 citations and is from a domain leading peer-reviewed journal.

2. (akaike2024merkelcellcarcinoma pages 1-2): Tomoko Akaike, Austin J Jabbour, Peter H Goff, Song Y Park, Shailender Bhatia, and Paul Nghiem. Merkel cell carcinoma refractory to anti-pd(l)1: utility of adding ipilimumab for salvage therapy. Journal for ImmunoTherapy of Cancer, 12:e009396, Jul 2024. URL: https://doi.org/10.1136/jitc-2024-009396, doi:10.1136/jitc-2024-009396. This article has 4 citations and is from a domain leading peer-reviewed journal.

3. (NCT03747484 chunk 2): Joshua Veatch. Gene-Modified Immune Cells (FH-MCVA2TCR) in Treating Patients With Metastatic or Unresectable Merkel Cell Cancer. Fred Hutchinson Cancer Center. 2019. ClinicalTrials.gov Identifier: NCT03747484

4. (NCT03599713 chunk 3):  A Study of INCMGA00012 in Metastatic Merkel Cell Carcinoma (POD1UM-201). Incyte Corporation. 2019. ClinicalTrials.gov Identifier: NCT03599713

5. (li2024classificationandepidemiologic pages 2-3): Junfeng Li, Meilin Liu, Han Li, Xin Zhang, Xufei Xiang, Yiping Wang, Shuyi Wang, Jinxiang Han, and Yanqin Lu. Classification and epidemiologic analysis of 86 diseases in china's second list of rare diseases. Intractable & rare diseases research, 13 4:213-226, Nov 2024. URL: https://doi.org/10.5582/irdr.2024.01061, doi:10.5582/irdr.2024.01061. This article has 6 citations.

6. (li2024classificationandepidemiologic pages 1-2): Junfeng Li, Meilin Liu, Han Li, Xin Zhang, Xufei Xiang, Yiping Wang, Shuyi Wang, Jinxiang Han, and Yanqin Lu. Classification and epidemiologic analysis of 86 diseases in china's second list of rare diseases. Intractable & rare diseases research, 13 4:213-226, Nov 2024. URL: https://doi.org/10.5582/irdr.2024.01061, doi:10.5582/irdr.2024.01061. This article has 6 citations.

7. (moraes2024efficacyandsafety pages 5-8): Francisco Cezar Aquino de Moraes, Michele Kreuz, Isabella Christina Amaral de Lara, Artur de Oliveira Macena Lôbo, and Rommel Mario Rodríguez Burbano. Efficacy and safety of pd-1/pd-l1 inhibitors in patients with merkel cell carcinoma: a systematic review and meta-analysis. BMC Cancer, Nov 2024. URL: https://doi.org/10.1186/s12885-024-13129-1, doi:10.1186/s12885-024-13129-1. This article has 15 citations and is from a peer-reviewed journal.

8. (stang2024incidenceandrelative pages 3-5): Andreas Stang, Lennart Möller, Ina Wellmann, Kevin Claaßen, Hiltraud Kajüter, Selma Ugurel, and Jürgen C. Becker. Incidence and relative survival of patients with merkel cell carcinoma in north rhine-westphalia, germany, 2008–2021. Cancers, 16:2158, Jun 2024. URL: https://doi.org/10.3390/cancers16112158, doi:10.3390/cancers16112158. This article has 4 citations.

9. (d’angelo2024firstlineavelumabtreatment pages 3-4): S.P. D’Angelo, C. Lebbé, L. Mortier, A.S. Brohl, N. Fazio, J.-J. Grob, N. Prinzi, G.J. Hanna, J.C. Hassel, F. Kiecker, A. von Heydebreck, G. Güzel, and P. Nghiem. First-line avelumab treatment in patients with metastatic merkel cell carcinoma: 4-year follow-up from part b of the javelin merkel 200 study. ESMO Open, 9:103461, May 2024. URL: https://doi.org/10.1016/j.esmoop.2024.103461, doi:10.1016/j.esmoop.2024.103461. This article has 29 citations and is from a domain leading peer-reviewed journal.

10. (becker2024merkelcellcarcinoma pages 1-2): Jürgen C. Becker, Andreas Stang, David Schrama, and Selma Ugurel. Merkel cell carcinoma: integrating epidemiology, immunology, and therapeutic updates. American Journal of Clinical Dermatology, 25:541-557, Apr 2024. URL: https://doi.org/10.1007/s40257-024-00858-z, doi:10.1007/s40257-024-00858-z. This article has 38 citations and is from a peer-reviewed journal.

11. (fojnica2023anupdatedreview pages 2-4): Adnan Fojnica, Kenana Ljuca, Saghir Akhtar, Zoran Gatalica, and Semir Vranic. An updated review of the biomarkers of response to immune checkpoint inhibitors in merkel cell carcinoma: merkel cell carcinoma and immunotherapy. Cancers, 15:5084, Oct 2023. URL: https://doi.org/10.3390/cancers15205084, doi:10.3390/cancers15205084. This article has 26 citations.

12. (jani2023insightsintoantitumor pages 1-2): Saumya Jani, Candice D. Church, and Paul Nghiem. Insights into anti-tumor immunity via the polyomavirus shared across human merkel cell carcinomas. Frontiers in Immunology, May 2023. URL: https://doi.org/10.3389/fimmu.2023.1172913, doi:10.3389/fimmu.2023.1172913. This article has 9 citations and is from a peer-reviewed journal.

13. (cheng2017merkelcellpolyomavirus pages 1-2): Jingwei Cheng, Donglim Esther Park, Christian Berrios, Elizabeth A. White, Reety Arora, Rosa Yoon, Timothy Branigan, Tengfei Xiao, Thomas Westerling, Alexander Federation, Rhamy Zeid, Benjamin Strober, Selene K. Swanson, Laurence Florens, James E. Bradner, Myles Brown, Peter M. Howley, Megha Padi, Michael P. Washburn, and James A. DeCaprio. Merkel cell polyomavirus recruits mycl to the ep400 complex to promote oncogenesis. PLOS Pathogens, 13:e1006668, Oct 2017. URL: https://doi.org/10.1371/journal.ppat.1006668, doi:10.1371/journal.ppat.1006668. This article has 157 citations and is from a highest quality peer-reviewed journal.

14. (mistry2021merkelcellcarcinoma pages 1-2): K. Mistry, N. J. Levell, P. Craig, N. M. Steven, and Z. C. Venables. Merkel cell carcinoma. Skin Health and Disease, Jun 2021. URL: https://doi.org/10.1002/ski2.55, doi:10.1002/ski2.55. This article has 22 citations and is from a peer-reviewed journal.

15. (d’angelo2024biomarkeranalysesinvestigating pages 2-3): Sandra P. D’Angelo, Céleste Lebbé, Paul Nghiem, Andrew S. Brohl, Thomas Mrowiec, Trent Leslie, Sara Georges, Gülseren Güzel, and Parantu Shah. Biomarker analyses investigating disease biology and associations with outcomes in the javelin merkel 200 trial of avelumab in metastatic merkel cell carcinoma. Clinical Cancer Research, 30:4352-4362, Jul 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-0395, doi:10.1158/1078-0432.ccr-23-0395. This article has 9 citations and is from a highest quality peer-reviewed journal.

16. (pedersen2024merkelcellcarcinoma pages 13-14): Elisabeth A. Pedersen, Monique E. Verhaegen, Mallory K. Joseph, Kelly L. Harms, and Paul W. Harms. Merkel cell carcinoma: updates in tumor biology, emerging therapies, and preclinical models. Frontiers in Oncology, Jul 2024. URL: https://doi.org/10.3389/fonc.2024.1413793, doi:10.3389/fonc.2024.1413793. This article has 21 citations.

17. (pedersen2024merkelcellcarcinoma pages 14-15): Elisabeth A. Pedersen, Monique E. Verhaegen, Mallory K. Joseph, Kelly L. Harms, and Paul W. Harms. Merkel cell carcinoma: updates in tumor biology, emerging therapies, and preclinical models. Frontiers in Oncology, Jul 2024. URL: https://doi.org/10.3389/fonc.2024.1413793, doi:10.3389/fonc.2024.1413793. This article has 21 citations.

18. (prakash2023evolvingapplicationsof pages 2-4): Varsha Prakash, Ling Gao, and Soo-Jeong Park. Evolving applications of circulating tumor dna in merkel cell carcinoma. Cancers, 15:609, Jan 2023. URL: https://doi.org/10.3390/cancers15030609, doi:10.3390/cancers15030609. This article has 13 citations.

19. (prakash2023evolvingapplicationsof pages 4-5): Varsha Prakash, Ling Gao, and Soo-Jeong Park. Evolving applications of circulating tumor dna in merkel cell carcinoma. Cancers, 15:609, Jan 2023. URL: https://doi.org/10.3390/cancers15030609, doi:10.3390/cancers15030609. This article has 13 citations.

20. (d’angelo2024firstlineavelumabtreatment pages 4-6): S.P. D’Angelo, C. Lebbé, L. Mortier, A.S. Brohl, N. Fazio, J.-J. Grob, N. Prinzi, G.J. Hanna, J.C. Hassel, F. Kiecker, A. von Heydebreck, G. Güzel, and P. Nghiem. First-line avelumab treatment in patients with metastatic merkel cell carcinoma: 4-year follow-up from part b of the javelin merkel 200 study. ESMO Open, 9:103461, May 2024. URL: https://doi.org/10.1016/j.esmoop.2024.103461, doi:10.1016/j.esmoop.2024.103461. This article has 29 citations and is from a domain leading peer-reviewed journal.

21. (averbuch2023avelumabforthe pages 4-5): Itamar Averbuch, Ronen Stoff, Mor Miodovnik, Shlomit Fennig, Gil Bar‐Sela, Alexander Yakobson, Jonathan Daliot, Nethanel Asher, and Eyal Fenig. Avelumab for the treatment of locally advanced or metastatic merkel cell carcinoma—a multicenter real‐world experience in israel. Cancer Medicine, 12:12065-12070, Apr 2023. URL: https://doi.org/10.1002/cam4.5890, doi:10.1002/cam4.5890. This article has 16 citations and is from a peer-reviewed journal.

22. (d’angelo2024firstlineavelumabtreatment media 30169c3d): S.P. D’Angelo, C. Lebbé, L. Mortier, A.S. Brohl, N. Fazio, J.-J. Grob, N. Prinzi, G.J. Hanna, J.C. Hassel, F. Kiecker, A. von Heydebreck, G. Güzel, and P. Nghiem. First-line avelumab treatment in patients with metastatic merkel cell carcinoma: 4-year follow-up from part b of the javelin merkel 200 study. ESMO Open, 9:103461, May 2024. URL: https://doi.org/10.1016/j.esmoop.2024.103461, doi:10.1016/j.esmoop.2024.103461. This article has 29 citations and is from a domain leading peer-reviewed journal.

23. (d’angelo2024firstlineavelumabtreatment media a5f140c8): S.P. D’Angelo, C. Lebbé, L. Mortier, A.S. Brohl, N. Fazio, J.-J. Grob, N. Prinzi, G.J. Hanna, J.C. Hassel, F. Kiecker, A. von Heydebreck, G. Güzel, and P. Nghiem. First-line avelumab treatment in patients with metastatic merkel cell carcinoma: 4-year follow-up from part b of the javelin merkel 200 study. ESMO Open, 9:103461, May 2024. URL: https://doi.org/10.1016/j.esmoop.2024.103461, doi:10.1016/j.esmoop.2024.103461. This article has 29 citations and is from a domain leading peer-reviewed journal.
