---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T14:49:15.906068'
end_time: '2026-04-05T14:57:18.479119'
duration_seconds: 482.57
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: FGFR-Altered Cholangiocarcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** FGFR-Altered Cholangiocarcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **FGFR-Altered Cholangiocarcinoma** covering all of the
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
- **Disease Name:** FGFR-Altered Cholangiocarcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **FGFR-Altered Cholangiocarcinoma** covering all of the
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


# FGFR‑Altered Cholangiocarcinoma (FGFR2 fusion/rearranged iCCA) — Disease Characteristics Research Report

## Target Disease
- **Disease name (working):** FGFR‑altered cholangiocarcinoma, clinically dominated by **FGFR2 fusion/rearrangement–positive intrahepatic cholangiocarcinoma (iCCA)** (gonzalezmedina2024clinicalvalueof pages 1-2, patel2023fdaapprovalsummary pages 1-3).
- **Category:** Molecularly defined subset of **cholangiocarcinoma** (bile‑duct epithelial malignancy) (patel2023fdaapprovalsummary pages 1-3).
- **MONDO ID:** Not established from the retrieved sources for the molecularly defined entity “FGFR‑altered cholangiocarcinoma”; Open Targets returned MONDO IDs for related parent concepts (e.g., **intrahepatic cholangiocarcinoma: EFO_1001961; cholangiocarcinoma: EFO_0005221**) but not a specific MONDO ID for the FGFR‑altered subtype (patel2023fdaapprovalsummary pages 1-3).

---

## 1. Disease Information

### 1.1 Concise overview (definition)
Cholangiocarcinoma (CCA) is a malignant tumor of the biliary epithelium and is commonly classified anatomically into **intrahepatic (iCCA), perihilar, and extrahepatic** forms (patel2023fdaapprovalsummary pages 1-3). The most clinically actionable FGFR‑altered form is **FGFR2 fusion/rearrangement–positive iCCA**, in which oncogenic **FGFR2 gene fusions/rearrangements** (structural variants) define a molecular subtype that can be treated with FGFR tyrosine kinase inhibitors (TKIs) (patel2023fdaapprovalsummary pages 1-3, gonzalezmedina2024clinicalvalueof pages 1-2).

### 1.2 Key identifiers and synonyms
- **Common synonyms / alternative names** (as used in recent clinical literature):
  - “FGFR2 fusion‑positive cholangiocarcinoma” (gonzalezmedina2024clinicalvalueof pages 1-2)
  - “FGFR2‑rearranged intrahepatic cholangiocarcinoma” / “FGFR2 fusion/rearrangement iCCA” (liu2024fgfr2fusionrearrangementis pages 1-2, xin2026fgfr2rearrangedbiliarytract pages 5-6)
  - “FGFR2 gene fusions or other rearrangements” (regulatory language for pemigatinib indication) (patel2023fdaapprovalsummary pages 1-3)
- **Coding note:** The British Society of Gastroenterology (BSG) guideline highlights historical limitations in anatomical subtype coding and notes that “lack of specific coding for pCCA is to be corrected in the latest version of ICD (2021)” (rushbrook2024britishsocietyof pages 5-5).

### 1.3 Evidence source types
Most knowledge for “FGFR‑altered CCA” is derived from aggregated disease‑level resources (clinical trials, cohort studies, guidelines, and translational studies), not single‑patient EHRs; exceptions include case reports (not emphasized here) and small observational cohorts (gonzalezmedina2024clinicalvalueof pages 1-2, kim2024burdenofmortality pages 1-3).

---

## 2. Etiology

### 2.1 Disease causal factors (mechanistic)
FGFR2 fusion/rearrangement in iCCA is best conceptualized as an **oncogenic driver alteration** that results in ligand‑independent FGFR signaling and downstream proliferative/survival pathway activation (MAPK and PI3K axis), creating a therapeutically targetable dependency (xin2026fgfr2rearrangedbiliarytract pages 8-10, diperi2024convergentmapkpathway pages 1-3).

### 2.2 Risk factors (for cholangiocarcinoma overall)
Many established CCA risk factors reflect chronic biliary inflammation, biliary obstruction, chronic liver disease, infections, and carcinogenic exposures.

**Authoritative guideline summary (BSG Gut 2024; published Sep 2024):**
- The guideline provides effect estimates for multiple exposures, including very high relative risks for choledochal cysts and choledocholithiasis, elevated risks for cirrhosis, and increased odds for liver fluke infection (Opisthorchis viverrini/Clonorchis spp.) (rushbrook2024britishsocietyof pages 5-5).
- Example values explicitly stated in the guideline excerpt include:
  - **Choledochal cyst:** meta‑analysis RR **26.7** (and another estimate **34.9** in the same table) (rushbrook2024britishsocietyof pages 5-5).
  - **Choledocholithiasis:** meta‑analysis RR **10.1** (and another estimate **18.6**) (rushbrook2024britishsocietyof pages 5-5).
  - **Cirrhosis:** meta‑analysis RR **15.3** (additional estimate **3.8**) (rushbrook2024britishsocietyof pages 5-5).
  - **Thorotrast** exposure: retrospective study RR **>300** (rushbrook2024britishsocietyof pages 5-5).

**Review summary (Current Oncology 2024; published Jun 2024):** A BTC review lists major risk factors as “**cholelithiasis, biliary flukes in Asia, chronic inflammatory diseases of the bile ducts, metabolic syndrome-associated liver diseases… tobacco use, chronic hepatitis B and C infections, and cirrhosis**” (rosbuxo2024integratingmolecularinsights pages 1-2).

### 2.3 Protective factors
No validated protective genetic variants or definitive environmental protective factors specific to FGFR‑altered iCCA were identified in the retrieved sources. Prevention is therefore largely addressed as **risk‑factor reduction** for biliary tract cancers broadly (e.g., metabolic risk) (su2024globalregionaland pages 1-2).

### 2.4 Gene–environment interactions
Direct gene–environment interaction evidence specific to **FGFR2 fusion iCCA** was not identified in the retrieved 2023–2024 sources. Etiology‑stratified genomic reviews suggest that molecular landscapes vary by etiologic background (e.g., fluke‑associated vs non‑fluke CCA) (oura2025chronicliverdisease pages 13-14).

---

## 3. Phenotypes

### 3.1 Core clinical phenotype (CCA/iCCA)
Clinical presentation is often nonspecific and many patients present with advanced disease (rosbuxo2024integratingmolecularinsights pages 1-2, patel2023fdaapprovalsummary pages 1-3). The FGFR2‑fusion iCCA subgroup is clinically important primarily because it predicts benefit from FGFR inhibition rather than because it has unique pathognomonic symptoms.

### 3.2 Suggested phenotype list with HPO mapping (knowledge‑base oriented)
(Phenotypes below reflect common CCA clinical manifestations and treatment‑related effects; frequencies were not consistently provided in retrieved sources.)

**Tumor/location related**
- Abdominal pain — **HP:0002027**
- Jaundice — **HP:0000952** (more typical for extrahepatic obstruction; may occur in iCCA with biliary obstruction)
- Weight loss — **HP:0001824**
- Fatigue — **HP:0012378**

**Laboratory abnormalities (often used clinically)**
- Elevated alkaline phosphatase — **HP:0003155**
- Elevated gamma‑glutamyltransferase — **HP:0003285** (and was lower in FGFR2‑fusion cases in one surgical cohort) (liu2024fgfr2fusionrearrangementis pages 1-2)
- CA19‑9 elevation — **HP:0040217** (common in BTC care pathways; not quantified in retrieved evidence)

**Targeted therapy adverse events (FGFR inhibitors)**
- Hyperphosphatemia — **HP:0002905** (explicitly a common AE and key risk for pemigatinib) (patel2023fdaapprovalsummary pages 1-3, patel2023fdaapprovalsummary pages 3-5)
- Dry eye / ocular toxicity — **HP:0001097** / (ocular AE category) (patel2023fdaapprovalsummary pages 1-3, patel2023fdaapprovalsummary pages 3-5)
- Alopecia — **HP:0001596** (listed among common pemigatinib adverse reactions) (patel2023fdaapprovalsummary pages 1-3)

### 3.3 Quality‑of‑life impact
The retrieved 2023–2024 sources did not provide standardized QoL instrument outcomes (EQ‑5D, SF‑36, PROMIS) specific to FGFR‑altered iCCA.

---

## 4. Genetic / Molecular Information

### 4.1 Causal/driver genes and alteration classes
- **Primary driver gene:** **FGFR2** (fibroblast growth factor receptor 2) (patel2023fdaapprovalsummary pages 1-3, liu2024fgfr2fusionrearrangementis pages 1-2).
- **Pathogenic alteration class:** **Somatic FGFR2 gene fusions/rearrangements** (structural variants; almost exclusively in iCCA) (gonzalezmedina2024clinicalvalueof pages 1-2, liu2024fgfr2fusionrearrangementis pages 1-2).

### 4.2 Frequency / prevalence of FGFR2 fusions in iCCA
- FDA approval summary states: “**FGFR2 fusions occur in an estimated 13–14% of iCCA**” (patel2023fdaapprovalsummary pages 1-3).
- A 2024 liquid biopsy study notes FGFR2 fusions “occur in **10% to 15%** of patients with iCCA” (gonzalezmedina2024clinicalvalueof pages 1-2).
- A surgical cohort (226 ICC samples) found **14.2% (32/226)** FGFR2 fusion/rearrangement by FISH (liu2024fgfr2fusionrearrangementis pages 1-2).

### 4.3 Example fusion partners (and implications)
In FIGHT‑202 Cohort A, FGFR2‑BICC1 was the most common in‑frame fusion (34% of in‑frame fusions) (patel2023fdaapprovalsummary pages 3-5). A broader basket‑trial synthesis similarly highlights BICC1 among common partners (erul2026fibroblastgrowthfactor pages 4-6).

### 4.4 Somatic vs germline
FGFR2 fusions/rearrangements described here are **somatic tumor alterations** detected by tumor testing (tissue and/or plasma) (gonzalezmedina2024clinicalvalueof pages 1-2, patel2023fdaapprovalsummary pages 3-5).

### 4.5 Modifier/co‑alterations influencing response/resistance
Evidence indicates resistance can involve both **on‑target FGFR2 kinase‑domain mutations** and **off‑target bypass alterations** (MAPK; PI3K/mTOR) detected by serial tissue/ctDNA sequencing (facchinetti2024understandingandovercoming pages 1-2, diperi2024convergentmapkpathway pages 1-3).

---

## 5. Environmental Information

No environmental causes are known to specifically predispose to acquisition of FGFR2 fusions, but environmental and infectious exposures contribute to cholangiocarcinoma risk overall (e.g., liver flukes, carcinogenic exposures, metabolic risk), as summarized in guidelines and global burden analyses (rushbrook2024britishsocietyof pages 5-5, su2024globalregionaland pages 1-2).

---

## 6. Mechanism / Pathophysiology

### 6.1 Core pathway biology (FGFR2 fusion oncogenic signaling)
FGFR2 fusions function as actionable oncogenic drivers, and FGFR signaling interfaces strongly with canonical proliferative and survival pathways.
- Translational resistance studies and reviews explicitly implicate **MAPK signaling and PI3K/AKT/mTOR** as key downstream pathways relevant to resistance and bypass signaling (diperi2024convergentmapkpathway pages 1-3, diperi2024convergentmapkpathway pages 3-5).

**Suggested GO Biological Process terms (for annotation):**
- MAPK cascade — **GO:0000165**
- PI3K/AKT signaling — **GO:0014065** (phosphatidylinositol 3‑kinase signaling)
- Positive regulation of cell proliferation — **GO:0008284**
- Receptor tyrosine kinase signaling — **GO:0007169**

### 6.2 Acquired resistance mechanisms (2024–2025 high‑impact evidence)

#### 6.2.1 MAPK pathway convergence (Journal of Hepatology 2024)
A key 2024 mechanistic paper concludes that acquired resistance commonly converges on MAPK re‑activation and/or new FGFR2 mutations.
- In a cohort with repeat sequencing (n=17), **11/17 (64.7%)** developed new FGFR2 mutations and **9/17 (52.9%)** developed new MAPK pathway alterations, with **7** acquiring both (diperi2024convergentmapkpathway pages 1-3).
- Longitudinal ctDNA detected emergent MAPK alterations including **BRAF V600E** and multiple RAS variants in an example patient (diperi2024convergentmapkpathway pages 1-3).

#### 6.2.2 Polyclonal on‑target FGFR2 kinase domain mutations (Clinical Cancer Research 2024)
A prospective resistance program across FGFR2‑driven tumors found polyclonal FGFR2 kinase‑domain mutations are particularly frequent in cholangiocarcinoma.
- “Polyclonal FGFR2 kinase domain mutations were frequent” in cholangiocarcinoma (**14/27 patients**) (facchinetti2024understandingandovercoming pages 1-2).
- The study reports distinct patterns by inhibitor class: at resistance to **reversible inhibitors** many residues can be mutated; after **futibatinib** resistance was restricted to fewer hotspots including the **molecular brake N550** and **gatekeeper V565** (facchinetti2024understandingandovercoming pages 1-2).

#### 6.2.3 Specific acquired resistance residues (functional/preclinical evidence)
- A 2024 preclinical study of an FGFR inhibitor (tasurgratinib) highlights **N549H/K** as “major acquired mutations in CCA” and demonstrates potency against these in cell models and PDX (kawano2024antitumoractivityof pages 1-2).

### 6.3 Cell types and microenvironment
A surgical cohort study suggests FGFR2 fusion/rearrangement can associate with an “immune‑activated” state (lower Tregs and N2 neutrophils, higher N1 neutrophils), supporting prognostic stratification and potential immunotherapy targeting hypotheses (liu2024fgfr2fusionrearrangementis pages 1-2).

**Suggested Cell Ontology (CL) terms (for annotation):**
- Cholangiocyte — **CL:1000427** (primary malignant lineage)
- Regulatory T cell — **CL:0000815** (Treg)
- Neutrophil — **CL:0000775**

---

## 7. Anatomical Structures Affected

### 7.1 Organ and system level
- Primary organ/site: **Liver intrahepatic bile ducts** (iCCA) (patel2023fdaapprovalsummary pages 1-3, gonzalezmedina2024clinicalvalueof pages 1-2).

**Suggested UBERON terms (for annotation):**
- Liver — **UBERON:0002107**
- Intrahepatic bile duct — **UBERON:0003706**
- Biliary tract — **UBERON:0000059**

### 7.2 Tissue/cellular level
- Malignant epithelial tumor arising from biliary epithelium (cholangiocytes) (patel2023fdaapprovalsummary pages 1-3).

### 7.3 Subcellular level
- Core disease mechanism localizes to **FGFR2 receptor tyrosine kinase signaling** at the plasma membrane with downstream cytosolic kinase cascades (MAPK; PI3K) (diperi2024convergentmapkpathway pages 1-3, xin2026fgfr2rearrangedbiliarytract pages 8-10).

---

## 8. Temporal Development

### 8.1 Onset
Typically adult/older adult onset for cholangiocarcinoma overall; guideline excerpt reports **median age at diagnosis 75** (population‑level CCA context) (rushbrook2024britishsocietyof pages 5-5).

### 8.2 Progression
Advanced/metastatic disease at presentation is common and drives reliance on systemic therapy (rosbuxo2024integratingmolecularinsights pages 1-2). FGFR inhibitor benefit is meaningful but limited by acquired resistance, often within months (e.g., resistance observed as progression under therapy with emergent mutations detectable in ctDNA) (gonzalezmedina2024clinicalvalueof pages 1-2, diperi2024convergentmapkpathway pages 1-3).

---

## 9. Inheritance and Population

### 9.1 Inheritance
FGFR2 fusions/rearrangements in iCCA are **somatic cancer alterations**, not inherited Mendelian disorders (patel2023fdaapprovalsummary pages 3-5).

### 9.2 Epidemiology (recent quantitative data)
Because “FGFR‑altered cholangiocarcinoma” is molecularly defined, population incidence is usually inferred as *iCCA incidence × FGFR2 fusion prevalence*. Recent epidemiology sources are mostly for BTC/CCA overall.

**US mortality trends (2018–2023; Clinical and Molecular Hepatology 2024, published Oct 2024):**
- Intrahepatic cholangiocarcinoma mortality increased with **APC 3.1% (95% CI 1.2–4.9%)** (kim2024burdenofmortality pages 1-3).

**Global burden patterns (GBD 2019 analysis; Frontiers in Medicine 2024, published Apr 2024):**
- From 1990 to 2019, incident cases increased **1.85‑fold** and deaths **1.82‑fold**, while age‑standardized rates generally decreased (su2024globalregionaland pages 1-2).
- High BMI was identified as a leading attributable risk factor, accounting for **15.2% of deaths** and **15.7% of DALYs** globally in 2019 (su2024globalregionaland pages 1-2).

---

## 10. Diagnostics

### 10.1 Molecular diagnostics are essential (FGFR2)
A key operational requirement in FGFR‑altered iCCA is robust molecular testing to identify FGFR2 fusions.

**Regulatory companion diagnostic:** The FDA approval summary for pemigatinib states FDA “also approved the **FoundationOne CDX**… as a companion diagnostic for patient selection” (patel2023fdaapprovalsummary pages 1-3).

### 10.2 Tissue testing (standard of care)
FIGHT‑202 defined eligibility by presence of “FGFR2 fusion or other rearrangement… as detected by an FDA‑approved test” (patel2023fdaapprovalsummary pages 1-3). Practical implication: **tissue NGS** (DNA and/or RNA fusion detection) is commonly used, with attention to tissue stewardship.

### 10.3 Liquid biopsy / ctDNA (2024 development)
A major 2024 study in *Clinical Cancer Research* evaluated plasma detection and longitudinal monitoring:
- Quote (Purpose): “**FGFR2 fusions occur in 10% to 15% of patients with intrahepatic cholangiocarcinoma (iCCA)**…” (gonzalezmedina2024clinicalvalueof pages 1-2).
- Detection performance: **16/18 patients (88.9%)** had FGFR2 fusion events detectable in plasma (gonzalezmedina2024clinicalvalueof pages 1-2).
- Clinical management utility: increased ctDNA or emerging resistance mutations enabled “earlier detection of disease progression compared with standard radiologic imaging methods” (gonzalezmedina2024clinicalvalueof pages 1-2).

**Implementation interpretation:** Plasma ctDNA can complement tissue testing, especially for monitoring resistance evolution and anticipating progression, but tissue remains important for initial diagnosis and comprehensive profiling (gonzalezmedina2024clinicalvalueof pages 1-2, diperi2024convergentmapkpathway pages 1-3).

### 10.4 Imaging and pathology (CCA general)
Detailed imaging algorithms were not extracted in the evidence snippets used here; however, CCA diagnosis generally requires radiologic and histopathologic confirmation, and is addressed in major guidelines (rushbrook2024britishsocietyof pages 5-5).

---

## 11. Outcome / Prognosis

### 11.1 General BTC/CCA prognosis (population context)
A 2024 precision management review reports poor relative survival in BTC: “**1, 3, and 5 years post‑diagnosis estimated at 25%, 10%, and 7%, respectively**” (rosbuxo2024integratingmolecularinsights pages 1-2). The same review states: “**Approximately 65% of patients receive only the best supportive care at the time of diagnosis**” (rosbuxo2024integratingmolecularinsights pages 1-2).

### 11.2 Prognosis associated with FGFR2 fusion/rearrangement (surgical cohort)
A 2024 surgical cohort study reports FGFR2 fusion/rearrangement as an “independent protective factor” for overall and relapse‑free survival and associates it with an immune‑activated microenvironment (liu2024fgfr2fusionrearrangementis pages 1-2).

---

## 12. Treatment

### 12.1 Targeted FGFR inhibition (core application)
Two FDA‑approved FGFR inhibitors—pemigatinib and futibatinib—are central real‑world implementations for previously treated advanced FGFR2 fusion/rearranged cholangiocarcinoma (patel2023fdaapprovalsummary pages 1-3, gonzalezmedina2024clinicalvalueof pages 1-2).

| Therapy (drug; reversible vs irreversible) | Target/eligible alteration | Trial (name; NCT) | Setting/line | Key efficacy | Key safety signals | Regulatory/implementation note |
|---|---|---|---|---|---|---|
| **Pemigatinib**; selective FGFR1–3, **reversible/ATP-competitive** | Unresectable locally advanced or metastatic cholangiocarcinoma with **FGFR2 fusion or other rearrangement**; Cohort A included 107 patients, 98% with iCCA; FGFR2-BICC1 was the most common in-frame fusion partner (34%) | **FIGHT-202**; **NCT02924376** | Previously treated; disease progressed on or after ≥1 prior therapy | ORR **35.5%** (95% CI **26.5–45.3%**); **3 CRs (2.8%)** and **35 PRs (32.7%)**; median **DOR 9.1 months** (95% CI **6.0–13.5**); 63% of responders had DOR ≥6 months and 18% ≥12 months. FDA summary also reports ORR **36%** (95% CI **27–45**) and median DOR **9.1 months**; later update reported median **PFS 7.0 months** and **OS 17.5 months** (patel2023fdaapprovalsummary pages 3-5, patel2023fdaapprovalsummary pages 1-3, erul2026fibroblastgrowthfactor pages 4-6) | Hyperphosphatemia was a key/common AE; ocular toxicity was an important risk; common ocular events included dry eye. In 146 treated CCA patients, 99% had ≥1 AE, grade 3–4 ADRs occurred in 64%, fatal adverse reactions in 4.1% (patel2023fdaapprovalsummary pages 1-3, patel2023fdaapprovalsummary pages 3-5, erul2026fibroblastgrowthfactor pages 4-6) | **FDA accelerated approval: 2020-04-17** for adults with previously treated unresectable locally advanced or metastatic CCA with FGFR2 fusion/rearrangement. **FoundationOne CDX** approved as companion diagnostic (patel2023fdaapprovalsummary pages 1-3) |
| **Futibatinib**; pan-FGFR1–4, **irreversible/covalent** | Previously treated unresectable, locally advanced or metastatic **intrahepatic cholangiocarcinoma** with **FGFR2 gene fusions or other rearrangements** | **FOENIX-CCA2**; NCT not provided in available context | Previously treated; unresectable locally advanced or metastatic iCCA | ORR **42%** (95% CI **32–52%**); reported median **PFS ~9.0 months** and median **OS 21.7 months** in review synthesis of phase II data (crolley2024…locally pages 2-3, xin2026fgfr2rearrangedbiliarytract pages 5-6) | Hyperphosphatemia reported among the most common treatment-emergent adverse events; ocular toxicity not explicitly quantified in available context (xin2026fgfr2rearrangedbiliarytract pages 5-6) | Received regulatory approval based on FOENIX-CCA2 phase II data; implementation note in available context emphasizes use in previously treated FGFR2-rearranged iCCA and potential activity after resistance to reversible FGFR inhibitors, but no companion diagnostic was specified in the available context (crolley2024…locally pages 2-3, gonzalezmedina2024clinicalvalueof pages 1-2) |


*Table: This table summarizes the core clinical evidence for the two leading FGFR-targeted therapies used in FGFR-altered cholangiocarcinoma, focusing on pivotal trial outcomes, safety, and implementation details. It is useful for quickly comparing pemigatinib and futibatinib in the molecularly defined FGFR2-rearranged setting.*

#### 12.1.1 Pemigatinib (PEMAZYRE) — pivotal evidence
**FDA accelerated approval language (Clinical Cancer Research 2023; published Oct 2023):**
- Quote: “**On April 17, 2020, the FDA granted accelerated approval to pemigatinib… for… cholangiocarcinoma with an FGFR2 fusion or other rearrangement**…” (patel2023fdaapprovalsummary pages 1-3).
- Efficacy basis: ORR **36% (95% CI 27–45)**; median DOR **9.1 months** (patel2023fdaapprovalsummary pages 1-3). A detailed breakdown reports ORR **35.5%** with **2.8% CR** and median DOR **9.1 months** (patel2023fdaapprovalsummary pages 3-5).
- Key toxicities: hyperphosphatemia and ocular toxicity highlighted as important risks (patel2023fdaapprovalsummary pages 1-3, patel2023fdaapprovalsummary pages 3-5).

**Suggested MAXO terms:**
- FGFR inhibitor therapy — **MAXO:0000758** (term name may vary by implementation; use as a targeted small‑molecule therapy action)
- Molecular targeted therapy — **MAXO:0000010**

#### 12.1.2 Futibatinib (LYTGOBI) — pivotal evidence synthesis
A 2026 synthesis reports FOENIX‑CCA2 outcomes (used here only for quantitative endpoints): ORR **42%**, median PFS **9.0 months**, median OS **21.7 months** (xin2026fgfr2rearrangedbiliarytract pages 5-6). A 2024 review excerpt also reports FOENIX‑CCA2 ORR **42% (95% CI 32–52%)** (crolley2024…locally pages 2-3).

**Clinical positioning and sequencing:** A 2024 liquid biopsy study notes futibatinib “has shown to be effective in some patients with acquired resistance to other FGFRi” (gonzalezmedina2024clinicalvalueof pages 1-2), consistent with the mechanistic rationale that irreversible inhibitors may retain activity against subsets of resistance mutations (facchinetti2024understandingandovercoming pages 1-2).

### 12.2 Managing and anticipating resistance (current expert analysis)
A 2024 resistance program supports a sequential, molecularly guided strategy:
- Polyclonal FGFR2 kinase‑domain mutations are common in cholangiocarcinoma (14/27), and off‑target MAPK/PI3K alterations can co‑occur (facchinetti2024understandingandovercoming pages 1-2).
- Longitudinal ctDNA and/or re‑biopsy can inform whether switching to an irreversible inhibitor is plausible, or whether bypass pathway inhibition (e.g., PI3K/mTOR) is rational in a subset (e.g., everolimus benefit in selected cases) (facchinetti2024understandingandovercoming pages 1-2).

### 12.3 Combination strategies (research frontier)
Preclinical and translational evidence indicates MAPK pathway co‑activation can drive resistance and that MEK inhibition can be synergistic with FGFR inhibition in vitro, though not universally effective (diperi2024convergentmapkpathway pages 1-3).

### 12.4 Ongoing / recent clinical trials (ClinicalTrials.gov; selected)
(Representative examples from retrieved trials list)
- **FIGHT‑202 (pemigatinib): NCT02924376** — completed (patel2023fdaapprovalsummary pages 1-3).
- **Infigratinib phase 3 first‑line iCCA with FGFR2 fusions: NCT03773302** — terminated (trial registry evidence retrieved).
- **Futibatinib advanced CCA with FGFR2 fusion/rearrangement: NCT05727176** — recruiting phase 2 (trial registry evidence retrieved).

---

## 13. Prevention

### 13.1 Primary prevention (BTC/CCA context)
Global burden analysis identifies **high BMI** as a major attributable risk factor for gallbladder and biliary tract cancers (15.2% of deaths; 15.7% DALYs in 2019), supporting metabolic risk reduction as a plausible population‑level prevention strategy (su2024globalregionaland pages 1-2).

### 13.2 Secondary prevention / screening
Specific screening recommendations for FGFR‑altered iCCA were not identified in the retrieved evidence excerpts. For CCA broadly, guideline efforts focus on risk factor identification and diagnostic pathways (rushbrook2024britishsocietyof pages 5-5).

---

## 14. Other Species / Natural Disease

No naturally occurring non‑human species entity specifically corresponding to “FGFR2 fusion iCCA” was identified from the retrieved sources. This section remains **not well characterized** in the current evidence set.

---

## 15. Model Organisms / Experimental Models

### 15.1 Preclinical resistance modeling and translational platforms (2024)
Multiple model classes are actively used to study FGFR2 fusion iCCA biology and resistance.

- **Ba/F3 FGFR2::BICC1 models and PDX** were used in a prospective resistance study to functionally validate kinase‑domain mutations and evaluate inhibitor classes (facchinetti2024understandingandovercoming pages 2-3, facchinetti2024understandingandovercoming pages 1-2).
- **Engineered biliary epithelial cell models with FGFR2‑BICC1** and induced MAPK alterations (KRAS G12D; BRAF V600E) were used to demonstrate MAPK‑mediated resistance mechanisms and test combinations (diperi2024convergentmapkpathway pages 3-5).
- **NIH/3T3 cells expressing FGFR2 fusions** plus **CCA patient‑derived xenograft (PDX)** were used to test an FGFR inhibitor and activity against acquired mutations including **N549H/K** (kawano2024antitumoractivityof pages 1-2).

**Suggested model‑related ontology hooks:**
- Patient‑derived xenograft model (PDX) — model type annotation
- Organoid model — not directly evidenced in the extracted snippets for FGFR2 fusion iCCA here; however, organoids are broadly discussed as relevant CCA preclinical systems in recent methodological reviews (not used as primary evidence in this report).

---

# Expert Synthesis (2023–2024 emphasis)

1. **FGFR2 fusions/rearrangements are frequent (≈10–15%) and largely iCCA‑restricted**, providing a clear precision‑oncology target with FDA‑approved therapies (pemigatinib; futibatinib) (patel2023fdaapprovalsummary pages 1-3, gonzalezmedina2024clinicalvalueof pages 1-2, liu2024fgfr2fusionrearrangementis pages 1-2).
2. **Clinical benefit is substantial but time‑limited**, with pemigatinib ORR ~36% and median DOR ~9 months in the pivotal accelerated‑approval dataset (patel2023fdaapprovalsummary pages 1-3, patel2023fdaapprovalsummary pages 3-5).
3. **Resistance is heterogeneous and often polyclonal**, involving on‑target FGFR2 kinase‑domain mutations and bypass pathway alterations (MAPK; PI3K/mTOR), motivating serial molecular monitoring and rational sequencing/combination strategies (facchinetti2024understandingandovercoming pages 1-2, diperi2024convergentmapkpathway pages 1-3).
4. **Liquid biopsy moved from concept to clinical utility in 2024**: plasma NGS detected FGFR2 fusions in 88.9% of tissue‑confirmed cases and enabled earlier progression detection than imaging in a longitudinal study, supporting real‑world implementation for monitoring (gonzalezmedina2024clinicalvalueof pages 1-2).

---

## Key abstract quotes (verbatim) supporting major claims
- FDA accelerated approval statement for pemigatinib: “**On April 17, 2020, the FDA granted accelerated approval to pemigatinib… for… cholangiocarcinoma with an FGFR2 fusion or other rearrangement**…” (Clinical Cancer Research; Oct 2023) (patel2023fdaapprovalsummary pages 1-3).
- FGFR2 fusion prevalence and plasma detection rationale: “**FGFR2 fusions occur in 10% to 15% of patients with intrahepatic cholangiocarcinoma (iCCA)**…” (Clinical Cancer Research; Jul 2024) (gonzalezmedina2024clinicalvalueof pages 1-2).

---

## URLs and publication dates (selected high‑authority sources used)
- Patel TH et al. **FDA Approval Summary: Pemigatinib…** *Clinical Cancer Research* (published **Oct 2023**). https://doi.org/10.1158/1078-0432.CCR-22-2036 (patel2023fdaapprovalsummary pages 1-3)
- González‑Medina A et al. **Clinical Value of Liquid Biopsy…** *Clinical Cancer Research* (published **Jul 2024**). https://doi.org/10.1158/1078-0432.CCR-23-3780 (gonzalezmedina2024clinicalvalueof pages 1-2)
- Rushbrook S et al. **BSG guidelines…** *Gut* (published **Sep 2024**). https://doi.org/10.1136/gutjnl-2023-330029 (rushbrook2024britishsocietyof pages 5-5)
- DiPeri TP et al. **Convergent MAPK pathway alterations…** *Journal of Hepatology* (published **Feb 2024**). https://doi.org/10.1016/j.jhep.2023.10.041 (diperi2024convergentmapkpathway pages 1-3)
- Facchinetti F et al. **Understanding and Overcoming Resistance…** *Clinical Cancer Research* (published **Sep 2024**). https://doi.org/10.1158/1078-0432.CCR-24-1834 (facchinetti2024understandingandovercoming pages 1-2)
- Kim D et al. **Burden of mortality… in US, 2018–2023** *Clinical and Molecular Hepatology* (published **Oct 2024**). https://doi.org/10.3350/cmh.2024.0318 (kim2024burdenofmortality pages 1-3)



References

1. (gonzalezmedina2024clinicalvalueof pages 1-2): Alberto González-Medina, Maria Vila-Casadesús, Marina Gomez-Rey, Carles Fabregat-Franco, Alexandre Sierra, Tian V. Tian, Florian Castet, Gloria Castillo, Judit Matito, Paola Martinez, Josep M. Miquel, Paolo Nuciforo, Raquel Pérez-López, Teresa Macarulla, and Ana Vivancos. Clinical value of liquid biopsy in patients with <i>fgfr2</i> fusion–positive cholangiocarcinoma during targeted therapy. Clinical Cancer Research, 30:4491-4504, Jul 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-3780, doi:10.1158/1078-0432.ccr-23-3780. This article has 25 citations and is from a highest quality peer-reviewed journal.

2. (patel2023fdaapprovalsummary pages 1-3): Timil H. Patel, Leigh Marcus, M. Naomi Horiba, Martha Donoghue, Somak Chatterjee, Pallavi S. Mishra-Kalyani, Robert N. Schuck, Yangbing Li, Xinyuan Zhang, Jeanne Fourie Zirkelbach, Rosane Charlab, Jiang Liu, Yuching Yang, Steven J. Lemery, Richard Pazdur, Marc R. Theoret, and Lola A. Fashoyin-Aje. Fda approval summary: pemigatinib for previously treated, unresectable locally advanced or metastatic cholangiocarcinoma with fgfr2 fusion or other rearrangement. Clinical Cancer Research, 29:838-842, Oct 2023. URL: https://doi.org/10.1158/1078-0432.ccr-22-2036, doi:10.1158/1078-0432.ccr-22-2036. This article has 65 citations and is from a highest quality peer-reviewed journal.

3. (liu2024fgfr2fusionrearrangementis pages 1-2): Shaoqing Liu, Jialei Weng, Manqing Cao, Qiang Zhou, Minghao Xu, Wenxin Xu, Zhiqiu Hu, Minghao Xu, Qiongzhu Dong, Xia Sheng, Chenhao Zhou, and Ning Ren. Fgfr2 fusion/rearrangement is associated with favorable prognosis and immunoactivation in patients with intrahepatic cholangiocarcinoma. The Oncologist, 29:e1734-e1747, Jul 2024. URL: https://doi.org/10.1093/oncolo/oyae170, doi:10.1093/oncolo/oyae170. This article has 6 citations.

4. (xin2026fgfr2rearrangedbiliarytract pages 5-6): Xin Xin and Ruoyu Miao. Fgfr2-rearranged biliary tract cancer: biology, resistance mechanisms, and emerging therapeutic strategies. Cancers, 18:531, Feb 2026. URL: https://doi.org/10.3390/cancers18030531, doi:10.3390/cancers18030531. This article has 0 citations.

5. (rushbrook2024britishsocietyof pages 5-5): S. Rushbrook, Timothy J. Kendall, Yoh Zen, R. Albazaz, Prakash Manoharan, Stephen P Pereira, R. Sturgess, Brian R Davidson, Hassan Z. Malik, Derek Manas, Nigel Heaton, K. R. Prasad, John Bridgewater, Juan W Valle, Rebecca Goody, Maria A. Hawkins, Wendy Prentice, H. Morement, Martine Walmsley, Shahid A. Khan, and Hepatology Gastroenterology Section Shahid A Khan. British society of gastroenterology guidelines for the diagnosis and management of cholangiocarcinoma. Gut, 73:16-46, Sep 2024. URL: https://doi.org/10.1136/gutjnl-2023-330029, doi:10.1136/gutjnl-2023-330029. This article has 98 citations and is from a highest quality peer-reviewed journal.

6. (kim2024burdenofmortality pages 1-3): Donghee Kim, Richie Manikat, Karn Wijarnpreecha, George Cholankeril, and Aijaz Ahmed. Burden of mortality from hepatocellular carcinoma and biliary tract cancers by race and ethnicity and sex in us, 2018–2023. Clinical and Molecular Hepatology, 30:756-770, Oct 2024. URL: https://doi.org/10.3350/cmh.2024.0318, doi:10.3350/cmh.2024.0318. This article has 22 citations.

7. (xin2026fgfr2rearrangedbiliarytract pages 8-10): Xin Xin and Ruoyu Miao. Fgfr2-rearranged biliary tract cancer: biology, resistance mechanisms, and emerging therapeutic strategies. Cancers, 18:531, Feb 2026. URL: https://doi.org/10.3390/cancers18030531, doi:10.3390/cancers18030531. This article has 0 citations.

8. (diperi2024convergentmapkpathway pages 1-3): Timothy P. DiPeri, Ming Zhao, Kurt W. Evans, Kaushik Varadarajan, Tyler Moss, Stephen Scott, Michael P. Kahle, Charnel C. Byrnes, Huiqin Chen, Sunyoung S. Lee, Abdel-Baset Halim, Hiroshi Hirai, Volker Wacheck, Lawrence N. Kwong, Jordi Rodon, Milind Javle, and Funda Meric-Bernstam. Convergent mapk pathway alterations mediate acquired resistance to fgfr inhibitors in fgfr2 fusion-positive cholangiocarcinoma. Journal of Hepatology, 80:322-334, Feb 2024. URL: https://doi.org/10.1016/j.jhep.2023.10.041, doi:10.1016/j.jhep.2023.10.041. This article has 36 citations and is from a highest quality peer-reviewed journal.

9. (rosbuxo2024integratingmolecularinsights pages 1-2): Mar Ros-Buxó, Ezequiel Mauro, Tamara Sauri, Gemma Iserte, Carla Fuster-Anglada, Alba Díaz, Laura Sererols-Viñas, Silvia Affo, and Alejandro Forner. Integrating molecular insights into biliary tract cancer management: a review of personalized therapeutic strategies. Current Oncology, 31:3615-3629, Jun 2024. URL: https://doi.org/10.3390/curroncol31070266, doi:10.3390/curroncol31070266. This article has 5 citations.

10. (su2024globalregionaland pages 1-2): Jiao Su, Yuanhao Liang, and Xiaofeng He. Global, regional, and national burden and trends analysis of gallbladder and biliary tract cancer from 1990 to 2019 and predictions to 2030: a systematic analysis for the global burden of disease study 2019. Frontiers in Medicine, Apr 2024. URL: https://doi.org/10.3389/fmed.2024.1384314, doi:10.3389/fmed.2024.1384314. This article has 40 citations.

11. (oura2025chronicliverdisease pages 13-14): Kyoko Oura, Asahiro Morishita, Mai Nakahara, Tomoko Tadokoro, Koji Fujita, Joji Tani, Tsutomu Masaki, and Hideki Kobara. Chronic liver disease associated cholangiocarcinoma: genomic insights and precision therapeutic strategies. Cancers, 17:3052, Sep 2025. URL: https://doi.org/10.3390/cancers17183052, doi:10.3390/cancers17183052. This article has 2 citations.

12. (patel2023fdaapprovalsummary pages 3-5): Timil H. Patel, Leigh Marcus, M. Naomi Horiba, Martha Donoghue, Somak Chatterjee, Pallavi S. Mishra-Kalyani, Robert N. Schuck, Yangbing Li, Xinyuan Zhang, Jeanne Fourie Zirkelbach, Rosane Charlab, Jiang Liu, Yuching Yang, Steven J. Lemery, Richard Pazdur, Marc R. Theoret, and Lola A. Fashoyin-Aje. Fda approval summary: pemigatinib for previously treated, unresectable locally advanced or metastatic cholangiocarcinoma with fgfr2 fusion or other rearrangement. Clinical Cancer Research, 29:838-842, Oct 2023. URL: https://doi.org/10.1158/1078-0432.ccr-22-2036, doi:10.1158/1078-0432.ccr-22-2036. This article has 65 citations and is from a highest quality peer-reviewed journal.

13. (erul2026fibroblastgrowthfactor pages 4-6): Enes Erul, Sergio Cifuentes-Canaval, Akhil Santhosh, Emir Sokolović, Mario Della Mura, Gerardo Cazzato, Pınar Kubilay Tolunay, and Alessandro Rizzo. Fibroblast growth factor receptor (fgfr) inhibitors for the treatment of cholangiocarcinoma: key therapeutic developments and knowledge gaps. Drug Design, Development and Therapy, Volume 20:1-21, Feb 2026. URL: https://doi.org/10.2147/dddt.s559328, doi:10.2147/dddt.s559328. This article has 0 citations.

14. (facchinetti2024understandingandovercoming pages 1-2): Francesco Facchinetti, Yohann Loriot, Floriane Brayé, Damien Vasseur, Rastislav Bahleda, Ludovic Bigot, Rémy Barbé, Catline Nobre, David Combarel, Stefan Michiels, Antoine Italiano, Cristina Smolenschi, Lambros Tselikas, Jean-Yves Scoazec, Santiago Ponce-Aix, Benjamin Besse, Fabrice André, Ken A. Olaussen, Antoine Hollebecque, and Luc Friboulet. Understanding and overcoming resistance to selective fgfr inhibitors across fgfr2-driven malignancies. Clinical Cancer Research, 30:4943-4956, Sep 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-1834, doi:10.1158/1078-0432.ccr-24-1834. This article has 33 citations and is from a highest quality peer-reviewed journal.

15. (diperi2024convergentmapkpathway pages 3-5): Timothy P. DiPeri, Ming Zhao, Kurt W. Evans, Kaushik Varadarajan, Tyler Moss, Stephen Scott, Michael P. Kahle, Charnel C. Byrnes, Huiqin Chen, Sunyoung S. Lee, Abdel-Baset Halim, Hiroshi Hirai, Volker Wacheck, Lawrence N. Kwong, Jordi Rodon, Milind Javle, and Funda Meric-Bernstam. Convergent mapk pathway alterations mediate acquired resistance to fgfr inhibitors in fgfr2 fusion-positive cholangiocarcinoma. Journal of Hepatology, 80:322-334, Feb 2024. URL: https://doi.org/10.1016/j.jhep.2023.10.041, doi:10.1016/j.jhep.2023.10.041. This article has 36 citations and is from a highest quality peer-reviewed journal.

16. (kawano2024antitumoractivityof pages 1-2): SATOSHI KAWANO, MEGUMI IKEMORI KAWADA, SAYO FUKUSHIMA, YASUHITO ARAI, TATSUHIRO SHIBATA, and SAORI WATANABE MIYANO. Antitumor activity of tasurgratinib as an orally available fgfr1-3 inhibitor in cholangiocarcinoma models with fgfr2-fusion. AntiCancer Research, 44:2393-2406, May 2024. URL: https://doi.org/10.21873/anticanres.17046, doi:10.21873/anticanres.17046. This article has 7 citations and is from a peer-reviewed journal.

17. (crolley2024…locally pages 2-3): V Crolley and J Bridgewater. … , locally advanced or metastatic intrahepatic cholangiocarcinoma with fibroblast growth factor receptor 2 (fgfr2) gene fusions or other rearrangements. Unknown journal, 2024.

18. (facchinetti2024understandingandovercoming pages 2-3): Francesco Facchinetti, Yohann Loriot, Floriane Brayé, Damien Vasseur, Rastislav Bahleda, Ludovic Bigot, Rémy Barbé, Catline Nobre, David Combarel, Stefan Michiels, Antoine Italiano, Cristina Smolenschi, Lambros Tselikas, Jean-Yves Scoazec, Santiago Ponce-Aix, Benjamin Besse, Fabrice André, Ken A. Olaussen, Antoine Hollebecque, and Luc Friboulet. Understanding and overcoming resistance to selective fgfr inhibitors across fgfr2-driven malignancies. Clinical Cancer Research, 30:4943-4956, Sep 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-1834, doi:10.1158/1078-0432.ccr-24-1834. This article has 33 citations and is from a highest quality peer-reviewed journal.
