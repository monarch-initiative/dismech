---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T22:15:10.045447'
end_time: '2026-04-25T22:28:55.674992'
duration_seconds: 825.63
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Friedreich Ataxia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 59
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Friedreich Ataxia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Friedreich Ataxia** covering all of the
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
- **Disease Name:** Friedreich Ataxia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Friedreich Ataxia** covering all of the
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


# Friedreich Ataxia (FRDA) — Comprehensive Disease Characteristics Research Report (2023–2024 prioritized)

## Executive summary
Friedreich ataxia (FRDA) is a life-shortening, autosomal recessive multisystem neurodegenerative disorder primarily caused by biallelic GAA trinucleotide repeat expansions in intron 1 of *FXN* (frataxin), resulting in transcriptional silencing and frataxin deficiency. Frataxin deficiency disrupts mitochondrial iron–sulfur (Fe–S) cluster biogenesis and mitochondrial function, leading to selective vulnerability of dorsal root ganglia (DRG) sensory neurons, spinal cord tracts, cerebellar dentate nucleus, and cardiomyocytes. Natural history studies (notably FA-COMS/FACOMS) show progressive neurologic decline with ambulation loss typically within ~15 years, with faster progression in earlier-onset disease. In February 2023, omaveloxolone (Skyclarys™), an Nrf2 pathway activator, became the first approved therapy; a propensity-score matched analysis comparing the MOXIe extension to FACOMS natural history data suggests ~55% slowing of mFARS progression over 3 years. (scott2024newandemerging pages 1-2, indelicato2024skeletalmuscleinvolvement pages 1-2, rummey2022naturalhistoryof pages 3-5, lynch2024propensitymatchedcomparison pages 1-2)

---

## 1. Disease information
### 1.1 What is the disease?
FRDA is described as an autosomal recessive inherited ataxia with progressive neurologic dysfunction (gait/limb ataxia, dysarthria, areflexia, sensory loss) and systemic involvement including cardiomyopathy, skeletal deformities (e.g., scoliosis, pes cavus), and diabetes/metabolic dysfunction. (scott2024newandemerging pages 1-2, lima2025earlyexperienceon pages 1-2, indelicato2024skeletalmuscleinvolvement pages 1-2)

**Abstract-supported definition (direct quote):** Park et al. (2025) describe FRDA as an “autosomal recessive neurodegenerative disorder characterized by ataxia, sensory loss and pyramidal signs.” (park2025longreadsequencingidentifies pages 1-2)

### 1.2 Key identifiers
* **MONDO:** MONDO_0100339 (Open Targets disease entity for Friedreich ataxia). URL: https://platform.opentargets.org/disease/MONDO_0100339 (scott2024newandemerging pages 1-2)
* **OMIM / Orphanet / ICD-10/ICD-11 / MeSH:** These identifiers were **not explicitly present** in the full-text sources retrieved in this run; therefore they cannot be cited from primary evidence here.

### 1.3 Synonyms and alternative names
Commonly used variants in the literature include “Friedreich’s ataxia” and “Friedreich ataxia (FRDA/FA)”. (scott2024newandemerging pages 1-2, indelicato2024skeletalmuscleinvolvement pages 1-2)

### 1.4 Evidence source type
Most disease-defining statements in this report are derived from:
* **Aggregated disease-level resources**: reviews and systematic reviews (e.g., CNS Drugs 2024; IJMS 2024). (scott2024newandemerging pages 1-2, indelicato2024skeletalmuscleinvolvement pages 1-2)
* **Human clinical cohorts/natural history studies**: FACOMS/FA-COMS. (rummey2022naturalhistoryof pages 3-5, rummey2020predictorsofloss pages 1-2)
* **Human neuropathology**: DRG and dentate nucleus tissue analyses. (koeppen2016dorsalrootganglia pages 1-2, koeppen2012friedreichsataxiacauses pages 1-2)
* **Model organism/cellular models**: conditional mice, repeat-expansion mice, iPSC-derived models. (mercadoayon2022cerebellarpathologyin pages 1-2, mazzara2020frataxingeneediting pages 1-2)

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause (genetic):**
* ~96% of FRDA cases are homozygous for expanded GAA repeats in intron 1 of *FXN*, typically reported as ~56–1300 repeats. (scott2024newandemerging pages 1-2)
* A minority (~4%) are **compound heterozygotes**, with a GAA expansion on one allele and a pathogenic small variant or deletion on the other. (park2025longreadsequencingidentifies pages 1-2, indelicato2024skeletalmuscleinvolvement pages 1-2)

**Mechanistic cause:** expanded repeats induce locus-specific epigenetic changes and transcriptional silencing of *FXN*, resulting in low frataxin. (park2025longreadsequencingidentifies pages 1-2, indelicato2024skeletalmuscleinvolvement pages 1-2)

### 2.2 Risk factors
* **Genotype severity:** longer GAA expansions correlate with earlier onset and faster progression (a key genetic severity determinant). (indelicato2024skeletalmuscleinvolvement pages 1-2, rummey2022naturalhistoryof pages 2-3)
* **Age at onset:** earlier onset groups show faster mFARS progression in FACOMS. (rummey2022naturalhistoryof pages 3-5)

Environmental risk factors as disease initiators are not established for this Mendelian condition in the sources retrieved here.

### 2.3 Protective factors
No validated genetic or environmental protective factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No direct gene–environment interaction evidence was identified in the retrieved sources.

---

## 3. Phenotypes
### 3.1 Core neurologic phenotypes
Common neurologic phenotype includes progressive gait and limb ataxia, dysarthria, areflexia, sensory loss (proprioception/vibration), and pyramidal signs. (scott2024newandemerging pages 1-2, park2025longreadsequencingidentifies pages 1-2, lima2025earlyexperienceon pages 1-2)

Suggested **HPO terms** (non-exhaustive; ontology IDs not cited from sources):
* Ataxia; Gait ataxia; Limb ataxia
* Dysarthria
* Areflexia
* Loss of proprioception / impaired vibration sense
* Babinski sign / pyramidal signs

### 3.2 Non-neurologic/systemic phenotypes
* **Cardiomyopathy** (often hypertrophic) is a major determinant of premature mortality. (indelicato2024skeletalmuscleinvolvement pages 1-2, gavriilaki2024therapeuticbiomarkersin pages 1-2)
* **Scoliosis** and **pes cavus** are frequently described. (lima2025earlyexperienceon pages 1-2)
* **Diabetes** occurs in a subset (systematic review notes 10–30%). (jain2022clinicalevidenceof pages 2-3)

Suggested HPO terms (examples):
* Hypertrophic cardiomyopathy
* Scoliosis
* Pes cavus
* Diabetes mellitus

### 3.3 Age of onset, severity, progression, frequency
* **Typical symptom onset:** average ~10–15 years. (scott2024newandemerging pages 1-2)
* **Wheelchair dependence:** typical-onset patients become wheelchair dependent ~11.5 years after onset (reported in review; FACOMS-aligned). (scott2024newandemerging pages 1-2)
* **Disease progression:** progressive; rates vary strongly by age at onset and ambulation status. (rummey2022naturalhistoryof pages 3-5)

### 3.4 Quality of life impact
Clinical decline impacts ambulation and upright stability, with loss of ambulation as a meaningful functional endpoint. (rummey2020predictorsofloss pages 1-2)

---

## 4. Genetic/molecular information
### 4.1 Causal gene(s)
* **Primary causal gene:** *FXN* (frataxin). (park2025longreadsequencingidentifies pages 1-2, indelicato2024skeletalmuscleinvolvement pages 1-2)

### 4.2 Pathogenic variants
* **Repeat expansion:** GAA trinucleotide repeat expansion in intron 1 of *FXN*. Normal alleles reported as 5–35 repeats; disease-causing typically >66; many affected individuals carry >600, with upper ranges reported up to ~1700. (park2025longreadsequencingidentifies pages 1-2)
* **Compound heterozygosity:** GAA expansion + pathogenic small variant/deletion (~4% of cases). (park2025longreadsequencingidentifies pages 1-2, indelicato2024skeletalmuscleinvolvement pages 1-2)
* **Somatic instability/interruptions:** complex repeat interruptions and mosaicism can complicate detection; long-read genome sequencing can resolve complex expansions. (park2025longreadsequencingidentifies pages 1-2)

**Abstract-supported mechanism (direct quote):** Mazzara et al. (2020) state FRDA occurs “when transcription of the FXN gene is silenced due to an excessive expansion of GAA repeats into its first intron.” (mazzara2020frataxingeneediting pages 1-2)

### 4.3 Functional consequences
Frataxin deficiency leads to impaired Fe–S cluster biosynthesis and mitochondrial dysfunction with downstream oxidative stress and iron dysregulation. (indelicato2024skeletalmuscleinvolvement pages 1-2, osaki2026fromgeneticmutation pages 1-3)

### 4.4 Modifier genes / epigenetics
* **Epigenetic silencing:** GAA expansions induce locus-specific epigenetic changes (including upstream hypermethylation and downstream hypomethylation signatures) that contribute to transcriptional silencing. (park2025longreadsequencingidentifies pages 1-2)
* **DNA repair/chromatin cross-talk as a repeat instability mechanism (2024 development):** Lai et al. (2024) report temozolomide-induced and H3K9 methyltransferase inhibitor-induced GAA repeat contraction in neural cells with increased frataxin protein, proposing crosstalk between chromatin opening (H3K9 methylation inhibition) and base excision repair. (scott2024newandemerging pages 1-2)

Suggested ontology terms (examples):
* **GO (process):** iron–sulfur cluster assembly; mitochondrial ATP synthesis; response to oxidative stress; DNA repair; chromatin organization.

---

## 5. Environmental information
FRDA is primarily genetic. Environmental contributors, infectious triggers, or lifestyle causes were **not supported** as primary etiologic drivers in the retrieved sources.

---

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (high-level)
1. **Biallelic *FXN* GAA expansion** → 2. **Repressive chromatin / transcriptional silencing** → 3. **Frataxin deficiency** → 4. **Impaired Fe–S cluster biogenesis and mitochondrial dysfunction** → 5. **Oxidative stress/iron dysregulation, ETC defects, cellular injury** → 6. **Selective degeneration of DRG/spinal cord/dentate nucleus + cardiomyocyte dysfunction** → 7. **Progressive neurologic disability + cardiomyopathy-related morbidity/mortality.** (indelicato2024skeletalmuscleinvolvement pages 1-2, osaki2026fromgeneticmutation pages 1-3, koeppen2016dorsalrootganglia pages 1-2)

### 6.2 Selective vulnerability and primary tissues
Despite broad frataxin expression, pathology is tissue-selective, prominently affecting DRG sensory neurons and the cerebellar dentate nucleus, with major cardiac involvement. (indelicato2024skeletalmuscleinvolvement pages 1-2, koeppen2012friedreichsataxiacauses pages 1-2)

### 6.3 Cellular processes and neuropathology (human evidence)
**DRG (human tissue):** Koeppen et al. (2016) show DRG pathology includes satellite cell proliferation into multiple perineuronal layers, connexin-43 gap junction upregulation, monocyte infiltration, and ferritin upregulation in satellite cells/monocytes consistent with inflammatory and iron-handling changes. (koeppen2016dorsalrootganglia pages 1-2)

**Dentate nucleus (human tissue metal mapping):** Koeppen et al. (2012) report that maximal Fe/Cu/Zn concentrations did not differ between FRDA and controls, but metal redistribution occurs with structural collapse of the dentate nucleus and increased ferritin-positive microglia; reported mean Fe 364±117 vs 344±159 µg/mL (controls vs FRDA) in PEG/DMSO-embedded tissue. (koeppen2012friedreichsataxiacauses pages 1-2)

### 6.4 Mitochondrial dysfunction in DRG (2024 mechanistic development)
Sanz-Alcázar et al. (2024) report frataxin deficiency in DRG neuron cultures and DRG tissue from an *FXN* mouse model causes reduced ETC complex I/II activity and levels, altered mitochondrial morphology, reduced NAD+/NADH ratio, impaired sirtuin activity (SirT3) and increased acetylation of SOD2 (with increased mitochondrial superoxide); honokiol (SirT3 activator) restored respiration and reduced oxidative markers. (sanzalcazar2024mitochondrialimpairmentdecreased pages 1-2)

Suggested ontology terms:
* **CL (cell types):** dorsal root ganglion sensory neuron; satellite glial cell; microglia/monocyte lineage; cardiomyocyte.
* **GO-CC (compartments):** mitochondrion; mitochondrial inner membrane.

---

## 7. Anatomical structures affected
### 7.1 Organ/system level
* **Nervous system:** peripheral sensory system (DRG, dorsal roots), spinal cord tracts, cerebellar dentate nucleus, corticospinal tracts. (koeppen2016dorsalrootganglia pages 1-2, koeppen2013friedreichataxianeuropathology pages 1-1)
* **Heart:** cardiomyopathy is prominent and contributes to mortality risk. (indelicato2024skeletalmuscleinvolvement pages 1-2, gavriilaki2024therapeuticbiomarkersin pages 1-2)
* **Muscle:** skeletal muscle involvement contributes to fatigue/weakness, and restrictive respiratory impairment can occur. (indelicato2024skeletalmuscleinvolvement pages 1-2)

### 7.2 Tissue/cell level
* DRG neuronal loss and accompanying satellite cell/inflammatory changes (human). (koeppen2016dorsalrootganglia pages 1-2)
* Dentate nucleus neuronal atrophy and microglial ferritin positivity (human). (koeppen2012friedreichsataxiacauses pages 1-2)

Suggested **UBERON** examples (names only): dorsal root ganglion; spinal cord; cerebellar dentate nucleus; myocardium.

---

## 8. Temporal development
### 8.1 Onset
* Mean onset ~10–15 years in typical FRDA. (scott2024newandemerging pages 1-2)
* Late-onset forms are recognized (e.g., after age 25 or 40). (lima2025earlyexperienceon pages 1-2)

### 8.2 Progression and staging
**FACOMS natural history (key statistics):**
* 1,115 participants and 5,287 yearly visits. (rummey2022naturalhistoryof pages 1-2)
* Median follow-up ~5 years (IQR ~3–10). (rummey2022naturalhistoryof pages 2-3)
* Annual ambulatory mFARS progression differs by onset group: early-onset ~2.62 points/year vs typical-onset ~1.83 points/year; intermediate ~1.24 points/year; late ~1.18 points/year (approximate as reported with CIs). (rummey2022naturalhistoryof pages 3-5)
* Ambulatory decline is driven primarily by the **Upright Stability Score (USS)** component of mFARS. (rummey2022naturalhistoryof pages 1-2)

**Loss of ambulation:** In a large FA-COMS analysis (n≈1021), early-onset patients had a median of 11.5 years from symptom onset to full wheelchair dependence (FDS=5). (rummey2020predictorsofloss pages 1-2)

---

## 9. Inheritance and population
### 9.1 Epidemiology
A contemporary review reports FRDA affects ~1:40,000 (predominantly European populations) and is about ~1 in 50,000 Europeans in another systematic review/meta-analysis context. (scott2024newandemerging pages 1-2, gavriilaki2024therapeuticbiomarkersin pages 1-2)

### 9.2 Inheritance pattern
Autosomal recessive inheritance is consistently reported. (scott2024newandemerging pages 1-2, park2025longreadsequencingidentifies pages 1-2)

### 9.3 Carrier status
Carriers of one expanded allele are asymptomatic in the cited review and have residual frataxin ~40–68% of normal (vs 4–29% in affected individuals). (scott2024newandemerging pages 1-2)

---

## 10. Diagnostics
### 10.1 Genetic testing (repeat expansion and sequencing)
* Standard diagnostic approach depends on detecting *FXN* intron 1 GAA expansions; molecular diagnosis has been possible since 1996. (scott2024newandemerging pages 1-2)
* **Long-read sequencing** can resolve complex/interruptions/mosaic expansions that may be missed by conventional repeat-primed or long-range PCR assays; Park et al. (2025) highlight that interruptions and somatic instability “complicate molecular diagnosis” and that long-read genome sequencing can detect large expansions and mosaic variation. (park2025longreadsequencingidentifies pages 1-2)

### 10.2 Biomarkers and imaging
A 2024 biomarker systematic review/meta-analysis found only modest pooled improvements in combined FARS/mFARS with mitochondrial-function drugs and reported LV mass index (LVMI) improvement for some interventions, but overall evidence quality was low and the “optimal biomarker…has yet to be identified.” (gavriilaki2024therapeuticbiomarkersin pages 1-2)

Neuroimaging biomarkers (MRI/QSM/MRS) are a focus of contemporary FRDA trial design and natural-history imaging studies. (scott2024newandemerging pages 3-5)

---

## 11. Outcome / prognosis
* Mean survival ≈39 years (review) and reduced life expectancy is commonly attributed to cardiac complications. (scott2024newandemerging pages 1-2, gavriilaki2024therapeuticbiomarkersin pages 1-2)
* Cardiomyopathy is repeatedly emphasized as a major determinant of survival. (indelicato2024skeletalmuscleinvolvement pages 1-2, gavriilaki2024therapeuticbiomarkersin pages 1-2)

---

## 12. Treatment
### 12.1 Approved pharmacotherapy: Omaveloxolone (Skyclarys™)
**Regulatory status:** FDA approval February 2023 for patients aged ≥16 years; EC approval February 2024. (scott2024newandemerging pages 3-5)

**Efficacy (trial + external comparator):**
A propensity-score matched comparison of MOXIe extension (omaveloxolone-treated) vs FACOMS natural history controls reported:
* At Year 3, matched FACOMS progressed **6.61** mFARS points vs **3.00** points in MOXIe extension; difference **3.61** points; nominal p=0.0001. (lynch2024propensitymatchedcomparison pages 7-8)
* This corresponds to **~55% slowing** of mFARS progression. (lynch2024propensitymatchedcomparison pages 1-2, scott2024newandemerging pages 3-5)

**Visual evidence (trial outcome trajectories):** Figure 3 and Table 5 from Lynch et al. (2024) summarize the 3-year separation in mFARS trajectories and the Year-3 difference used in the main result. (lynch2024propensitymatchedcomparison media 7250a862, lynch2024propensitymatchedcomparison media d049e362)

**Safety and real-world implementation:**
Expert guidance and post-approval experience emphasize that aminotransferase elevations are common and usually transient and asymptomatic:
* In the MOXIe program, ALT increases occurred in ~37% and AST in ~22% of treated patients (placebo ~2%); >3× ULN ALT/AST elevations ~31%, >5× ULN ~16%, >10× ULN ~4%; no Hy’s law cases. (perlman2025managingaminotransferaseelevations pages 7-9)
* Label- and expert-opinion monitoring: baseline ALT/AST/total bilirubin; monitor monthly for first 3 months; reduce frequency thereafter if stable; temporarily discontinue if >5× ULN or >3× ULN with liver dysfunction; consider conservative interruption at ≥3× ULN even without dysfunction in real-world settings; reinitiate with stepwise titration (e.g., 50→100→150 mg) and q2-week labs for ~3 months. (perlman2025managingaminotransferaseelevations pages 1-3, perlman2025managingaminotransferaseelevations pages 11-14)

**Real-world observational data:** a single-center cohort (n=20; ~24 weeks) reported no discontinuations and transient asymptomatic transaminase elevations (ALT 45%); mFARS mean changed from 59.1 to 60.5 over 24 weeks (P=0.15). (lima2025earlyexperienceon pages 4-5)

Suggested **MAXO terms** (names only): pharmacotherapy; liver function monitoring; dose adjustment; treatment interruption/rechallenge; rehabilitation therapy.

### 12.2 Supportive/rehabilitative care
Multidisciplinary, symptomatic management remains central (mobility aids, therapy, cardiology and endocrinology management). (osaki2026fromgeneticmutation pages 11-12)

### 12.3 Experimental / emerging therapies (2024 focus)
A 2024 therapeutic landscape review emphasizes development across:
* oxidative stress/mitochondrial function modulators,
* frataxin-controlled metabolic pathway modulation,
* gene replacement/editing approaches. (scott2024newandemerging pages 3-5)

**Active or recent clinical trials (ClinicalTrials.gov):**
* **Omaveloxolone pivotal trial:** NCT02255435 (completed). (scott2024newandemerging pages 1-2)
* **Pediatric omaveloxolone trials:** NCT06953583 (BRAVE; Phase 3), NCT06054893 (PK/safety, ages 2–15). (clinical-trials tool output)
* **Gene therapy for FRDA cardiomyopathy:** NCT05302271 (AAVrh.10hFXN), NCT05445323, NCT07180355. (clinical-trials tool output)
* **Post-marketing/real-world safety follow-up:** NCT06623890 (observational, 300 participants). (clinical-trials tool output)

---

## 13. Prevention
No primary prevention exists for a Mendelian recessive disorder aside from reproductive options and family-based risk management. Formal guideline statements were not retrieved in this run.

**Applicable prevention concepts (knowledge-base oriented):**
* **Carrier testing / cascade testing** in families with known *FXN* expansions.
* **Genetic counseling**.

---

## 14. Other species / natural disease
No naturally occurring FRDA-equivalent disease in non-human species was identified in the retrieved evidence.

---

## 15. Model organisms
FRDA modeling requires balancing genetic fidelity (GAA repeat silencing/instability) vs phenotype severity.

### 15.1 Mouse models
* **Conditional Cre-based models:** MCK-driven cardiac/skeletal muscle knockouts model cardiomyopathy with early death; Pvalb-driven models target proprioceptive/cerebellar systems and yield severe, rapid neurologic disease. (bouchard2023findinganappropriate pages 1-2, pandolfo2025friedreichataxia pages 5-6)
* **Repeat-expansion and humanized models:** KIKO and YG8 lines capture the repeat biology and epigenetic silencing context, with YG8–800 producing stronger ataxic phenotypes and repeat instability. (pandolfo2025friedreichataxia pages 5-6, bouchard2023findinganappropriate pages 1-2)
* **Inducible knockdown:** FRDAkd (doxycycline-inducible) partially recapitulates DRG neuronal loss, cardiomyopathy, and ataxia; shows dentate nucleus and Purkinje neuron loss and synaptic marker declines; AAV8 frataxin restoration partially rescues synaptic markers. (mercadoayon2022cerebellarpathologyin pages 1-2)

### 15.2 Human cellular/iPSC models
* **DRG organoids (iPSC-derived):** show DRG-like transcriptional signatures and peripheral sensory neuronal/glial subtypes; FRDA deficits are rescued by removing the entire *FXN* intron 1 (not just the GAA tract), implicating flanking repressed chromatin in silencing. (mazzara2020frataxingeneediting pages 1-2)

---

# Embedded structured summary
| Item | Value | Notes | Source (include URL if available) |
|---|---|---|---|
| Disease title | Friedreich ataxia: key identifiers and genetics | Mendelian inherited ataxia; disease-level aggregated knowledge. | https://doi.org/10.1007/s40263-024-01113-z |
| MONDO ID | MONDO_0100339 | Disease association returned by Open Targets for Friedreich ataxia (scott2024newandemerging pages 1-2). | https://platform.opentargets.org/disease/MONDO_0100339 |
| Inheritance | Autosomal recessive | Consistently described as autosomal recessive in recent reviews and diagnostic literature (scott2024newandemerging pages 1-2, park2025longreadsequencingidentifies pages 1-2). | https://doi.org/10.1007/s40263-024-01113-z ; https://doi.org/10.3390/ijms26114969 |
| Causal gene | FXN (frataxin) | FXN encodes frataxin, a nuclear-encoded mitochondrial protein required for iron-sulfur cluster biogenesis (park2025longreadsequencingidentifies pages 1-2, osaki2026fromgeneticmutation pages 1-3). | https://doi.org/10.3390/ijms26114969 ; https://doi.org/10.20944/preprints202604.1108.v1 |
| Primary pathogenic variant | Biallelic GAA trinucleotide repeat expansion in intron 1 of FXN | Normal alleles: 5–35 repeats; disease-causing: >66 repeats; many affected individuals carry ~56–1300+ repeats, often >600 in typical disease; expansion causes transcriptional silencing and reduced FXN expression (scott2024newandemerging pages 1-2, park2025longreadsequencingidentifies pages 1-2). | https://doi.org/10.1007/s40263-024-01113-z ; https://doi.org/10.3390/ijms26114969 |
| Percent of cases | ~96% homozygous GAA expansion; ~4% compound heterozygous | Minority of patients carry one GAA expansion plus a pathogenic small variant or deletion in FXN (scott2024newandemerging pages 1-2, park2025longreadsequencingidentifies pages 1-2, indelicato2024skeletalmuscleinvolvement pages 1-2). | https://doi.org/10.1007/s40263-024-01113-z ; https://doi.org/10.3390/ijms26114969 ; https://doi.org/10.3390/ijms25189915 |
| Frataxin levels | Affected individuals: ~4–29% of normal; carriers: ~40–68% of normal | Residual frataxin tracks with genotype severity; carriers are typically asymptomatic despite reduced protein levels (scott2024newandemerging pages 1-2). | https://doi.org/10.1007/s40263-024-01113-z |
| Major affected tissues | Dorsal root ganglia (DRG), dentate nucleus of cerebellum, spinal cord pathways, cardiomyocytes | Tissue vulnerability is selective despite broad FXN expression; neurologic and cardiac involvement drive major morbidity and mortality (indelicato2024skeletalmuscleinvolvement pages 1-2, osaki2026fromgeneticmutation pages 1-3). | https://doi.org/10.3390/ijms25189915 ; https://doi.org/10.20944/preprints202604.1108.v1 |


*Table: This table summarizes the core identifiers, inheritance, causal gene, variant class, case distribution, frataxin levels, and major affected tissues for Friedreich ataxia. It is useful as a compact knowledge-base seed for disease definition and molecular annotation.*

---

## Notes on evidence gaps
* **OMIM/Orphanet/ICD/MeSH identifiers** were not present in retrieved papers during this run; therefore they are not provided with citations.
* Many ontology IDs (HPO/GO/CL/UBERON/MAXO) are suggested by term name to support knowledge-base construction, but the sources retrieved here did not explicitly list ontology identifiers.

---

## Key cited sources (with dates and URLs)
* Scott V et al. *CNS Drugs*. Aug 2024. https://doi.org/10.1007/s40263-024-01113-z (scott2024newandemerging pages 1-2, scott2024newandemerging pages 3-5)
* Lynch DR et al. *Ann Clin Transl Neurol*. Sep 2024. https://doi.org/10.1002/acn3.51897 (lynch2024propensitymatchedcomparison pages 1-2, lynch2024propensitymatchedcomparison pages 7-8, lynch2024propensitymatchedcomparison pages 8-10)
* Indelicato E et al. *Int J Mol Sci*. Sep 2024. https://doi.org/10.3390/ijms25189915 (indelicato2024skeletalmuscleinvolvement pages 1-2)
* Gavriilaki M et al. *Cerebellum*. Oct 2024. https://doi.org/10.1007/s12311-023-01621-6 (gavriilaki2024therapeuticbiomarkersin pages 1-2)
* Perlman S et al. *Neurol Ther*. Jun 2025. https://doi.org/10.1007/s40120-025-00752-8 (perlman2025managingaminotransferaseelevations pages 7-9, perlman2025managingaminotransferaseelevations pages 11-14)
* Park J et al. *Int J Mol Sci*. May 2025. https://doi.org/10.3390/ijms26114969 (park2025longreadsequencingidentifies pages 1-2)
* Rummey C et al. *Neurology*. Oct 2022. https://doi.org/10.1212/WNL.0000000000200913 (rummey2022naturalhistoryof pages 1-2, rummey2022naturalhistoryof pages 3-5)
* Rummey C et al. *EClinicalMedicine*. Jan 2020. https://doi.org/10.1016/j.eclinm.2019.11.006 (rummey2020predictorsofloss pages 1-2)
* Koeppen AH et al. *Acta Neuropathol Commun*. May 2016. https://doi.org/10.1186/s40478-016-0288-5 (koeppen2016dorsalrootganglia pages 1-2)
* Koeppen AH et al. *Cerebellum*. May 2012. https://doi.org/10.1007/s12311-012-0383-5 (koeppen2012friedreichsataxiacauses pages 1-2)



References

1. (scott2024newandemerging pages 1-2): Varlli Scott, Martin B. Delatycki, Geneieve Tai, and Louise A. Corben. New and emerging drug and gene therapies for friedreich ataxia. CNS Drugs, 38:791-805, Aug 2024. URL: https://doi.org/10.1007/s40263-024-01113-z, doi:10.1007/s40263-024-01113-z. This article has 15 citations and is from a peer-reviewed journal.

2. (indelicato2024skeletalmuscleinvolvement pages 1-2): Elisabetta Indelicato, Julia Wanschitz, Wolfgang Löscher, and Sylvia Boesch. Skeletal muscle involvement in friedreich ataxia. International Journal of Molecular Sciences, 25:9915, Sep 2024. URL: https://doi.org/10.3390/ijms25189915, doi:10.3390/ijms25189915. This article has 4 citations.

3. (rummey2022naturalhistoryof pages 3-5): Christian Rummey, Louise A. Corben, Martin Delatycki, George Wilmot, Sub H. Subramony, Manuela Corti, Khalaf Bushara, Antoine Duquette, Christopher Gomez, J. Chad Hoyle, Richard Roxburgh, Lauren Seeberger, Grace Yoon, Katherine Mathews, Theresa Zesiewicz, Susan Perlman, and David R. Lynch. Natural history of friedreich ataxia. Neurology, Oct 2022. URL: https://doi.org/10.1212/wnl.0000000000200913, doi:10.1212/wnl.0000000000200913. This article has 74 citations and is from a highest quality peer-reviewed journal.

4. (lynch2024propensitymatchedcomparison pages 1-2): David R. Lynch, Angie Goldsberry, Christian Rummey, Jennifer Farmer, Sylvia Boesch, Martin B. Delatycki, Paola Giunti, J. Chad Hoyle, Caterina Mariotti, Katherine D. Mathews, Wolfgang Nachbauer, Susan Perlman, S.H. Subramony, George Wilmot, Theresa Zesiewicz, Lisa Weissfeld, and Colin Meyer. Propensity matched comparison of omaveloxolone treatment to friedreich ataxia natural history data. Annals of Clinical and Translational Neurology, 11:4-16, Sep 2024. URL: https://doi.org/10.1002/acn3.51897, doi:10.1002/acn3.51897. This article has 56 citations and is from a peer-reviewed journal.

5. (lima2025earlyexperienceon pages 1-2): Salvatore Maria Lima, Marta Caltagirone, Christian Messina, Umberto Quartetti, Nicasio Rini, Flora D’Amico, Filippo Brighina, and Vincenzo Di Stefano. Early experience on omaveloxolone in adult patients with friedreich’s ataxia: a real-world observational study. Journal of Neurology, Nov 2025. URL: https://doi.org/10.1007/s00415-025-13487-1, doi:10.1007/s00415-025-13487-1. This article has 1 citations and is from a domain leading peer-reviewed journal.

6. (park2025longreadsequencingidentifies pages 1-2): Joohyun Park, Claudia Dufke, Zofia Fleszar, Michael Schlotterbek, Elena Buena-Atienza, Lara G. Stühn, Caspar Gross, Marc Sturm, Stephan Ossowski, Ludger Schöls, Olaf Riess, and Tobias B. Haack. Long-read sequencing identifies mosaic sequence variations in friedreich’s ataxia-gaa repeats. International Journal of Molecular Sciences, 26:4969, May 2025. URL: https://doi.org/10.3390/ijms26114969, doi:10.3390/ijms26114969. This article has 2 citations.

7. (rummey2020predictorsofloss pages 1-2): Christian Rummey, Jennifer M. Farmer, and David R. Lynch. Predictors of loss of ambulation in friedreich's ataxia. EClinicalMedicine, 18:100213, Jan 2020. URL: https://doi.org/10.1016/j.eclinm.2019.11.006, doi:10.1016/j.eclinm.2019.11.006. This article has 68 citations and is from a peer-reviewed journal.

8. (koeppen2016dorsalrootganglia pages 1-2): Arnulf H. Koeppen, R. Liane Ramirez, Alyssa B. Becker, and Joseph E. Mazurkiewicz. Dorsal root ganglia in friedreich ataxia: satellite cell proliferation and inflammation. Acta Neuropathologica Communications, May 2016. URL: https://doi.org/10.1186/s40478-016-0288-5, doi:10.1186/s40478-016-0288-5. This article has 77 citations and is from a peer-reviewed journal.

9. (koeppen2012friedreichsataxiacauses pages 1-2): Arnulf H. Koeppen, R. Liane Ramirez, Devin Yu, Sarah E. Collins, Jiang Qian, Patrick J. Parsons, Karl X. Yang, Zewu Chen, Joseph E. Mazurkiewicz, and Paul J. Feustel. Friedreich's ataxia causes redistribution of iron, copper, and zinc in the dentate nucleus. The Cerebellum, 11:845-860, May 2012. URL: https://doi.org/10.1007/s12311-012-0383-5, doi:10.1007/s12311-012-0383-5. This article has 95 citations.

10. (mercadoayon2022cerebellarpathologyin pages 1-2): Elizabeth Mercado-Ayón, Nathan Warren, Sarah Halawani, Layne N. Rodden, Lucie Ngaba, Yi Na Dong, Joshua C. Chang, Carlos Fonck, Fulvio Mavilio, David R. Lynch, and Hong Lin. Cerebellar pathology in an inducible mouse model of friedreich ataxia. Frontiers in Neuroscience, Mar 2022. URL: https://doi.org/10.3389/fnins.2022.819569, doi:10.3389/fnins.2022.819569. This article has 17 citations and is from a peer-reviewed journal.

11. (mazzara2020frataxingeneediting pages 1-2): Pietro Giuseppe Mazzara, Sharon Muggeo, Mirko Luoni, Luca Massimino, Mattia Zaghi, Parisa Tajalli-Tehrani Valverde, Simone Brusco, Matteo Jacopo Marzi, Cecilia Palma, Gaia Colasante, Angelo Iannielli, Marianna Paulis, Chiara Cordiglieri, Serena Gea Giannelli, Paola Podini, Cinzia Gellera, Franco Taroni, Francesco Nicassio, Marco Rasponi, and Vania Broccoli. Frataxin gene editing rescues friedreich’s ataxia pathology in dorsal root ganglia organoid-derived sensory neurons. Nature Communications, Aug 2020. URL: https://doi.org/10.1038/s41467-020-17954-3, doi:10.1038/s41467-020-17954-3. This article has 102 citations and is from a highest quality peer-reviewed journal.

12. (rummey2022naturalhistoryof pages 2-3): Christian Rummey, Louise A. Corben, Martin Delatycki, George Wilmot, Sub H. Subramony, Manuela Corti, Khalaf Bushara, Antoine Duquette, Christopher Gomez, J. Chad Hoyle, Richard Roxburgh, Lauren Seeberger, Grace Yoon, Katherine Mathews, Theresa Zesiewicz, Susan Perlman, and David R. Lynch. Natural history of friedreich ataxia. Neurology, Oct 2022. URL: https://doi.org/10.1212/wnl.0000000000200913, doi:10.1212/wnl.0000000000200913. This article has 74 citations and is from a highest quality peer-reviewed journal.

13. (gavriilaki2024therapeuticbiomarkersin pages 1-2): Maria Gavriilaki, Evangelia Chatzikyriakou, Maria Moschou, Marianthi Arnaoutoglou, Ioanna Sakellari, and Vasilios K. Kimiskidis. Therapeutic biomarkers in friedreich’s ataxia: a systematic review and meta-analysis. Cerebellum (London, England), 23:1184-1203, Oct 2024. URL: https://doi.org/10.1007/s12311-023-01621-6, doi:10.1007/s12311-023-01621-6. This article has 15 citations.

14. (jain2022clinicalevidenceof pages 2-3): Paridhi Jain, Lohit Badgujar, Jelle Spoorendonk, and Katharina Buesch. Clinical evidence of interventions assessed in friedreich ataxia: a systematic review. Therapeutic Advances in Rare Disease, Jan 2022. URL: https://doi.org/10.1177/26330040221139872, doi:10.1177/26330040221139872. This article has 13 citations.

15. (osaki2026fromgeneticmutation pages 1-3): Yuta Osaki, Umme Sabrina Haque, and Toshifumi Yokota. From genetic mutation to therapy in friedreich ataxia: molecular mechanisms, therapeutic advances, and translational challenges. Unknown journal, Apr 2026. URL: https://doi.org/10.20944/preprints202604.1108.v1, doi:10.20944/preprints202604.1108.v1.

16. (sanzalcazar2024mitochondrialimpairmentdecreased pages 1-2): Arabela Sanz-Alcázar, Elena Britti, Fabien Delaspre, Marta Medina-Carbonero, Maria Pazos-Gil, Jordi Tamarit, Joaquim Ros, and Elisa Cabiscol. Mitochondrial impairment, decreased sirtuin activity and protein acetylation in dorsal root ganglia in friedreich ataxia models. Cellular and Molecular Life Sciences: CMLS, Dec 2024. URL: https://doi.org/10.1007/s00018-023-05064-4, doi:10.1007/s00018-023-05064-4. This article has 20 citations.

17. (koeppen2013friedreichataxianeuropathology pages 1-1): Arnulf H. Koeppen and Joseph E. Mazurkiewicz. Friedreich ataxia: neuropathology revised. Journal of neuropathology and experimental neurology, 72 2:78-90, Feb 2013. URL: https://doi.org/10.1097/nen.0b013e31827e5762, doi:10.1097/nen.0b013e31827e5762. This article has 313 citations and is from a peer-reviewed journal.

18. (rummey2022naturalhistoryof pages 1-2): Christian Rummey, Louise A. Corben, Martin Delatycki, George Wilmot, Sub H. Subramony, Manuela Corti, Khalaf Bushara, Antoine Duquette, Christopher Gomez, J. Chad Hoyle, Richard Roxburgh, Lauren Seeberger, Grace Yoon, Katherine Mathews, Theresa Zesiewicz, Susan Perlman, and David R. Lynch. Natural history of friedreich ataxia. Neurology, Oct 2022. URL: https://doi.org/10.1212/wnl.0000000000200913, doi:10.1212/wnl.0000000000200913. This article has 74 citations and is from a highest quality peer-reviewed journal.

19. (scott2024newandemerging pages 3-5): Varlli Scott, Martin B. Delatycki, Geneieve Tai, and Louise A. Corben. New and emerging drug and gene therapies for friedreich ataxia. CNS Drugs, 38:791-805, Aug 2024. URL: https://doi.org/10.1007/s40263-024-01113-z, doi:10.1007/s40263-024-01113-z. This article has 15 citations and is from a peer-reviewed journal.

20. (lynch2024propensitymatchedcomparison pages 7-8): David R. Lynch, Angie Goldsberry, Christian Rummey, Jennifer Farmer, Sylvia Boesch, Martin B. Delatycki, Paola Giunti, J. Chad Hoyle, Caterina Mariotti, Katherine D. Mathews, Wolfgang Nachbauer, Susan Perlman, S.H. Subramony, George Wilmot, Theresa Zesiewicz, Lisa Weissfeld, and Colin Meyer. Propensity matched comparison of omaveloxolone treatment to friedreich ataxia natural history data. Annals of Clinical and Translational Neurology, 11:4-16, Sep 2024. URL: https://doi.org/10.1002/acn3.51897, doi:10.1002/acn3.51897. This article has 56 citations and is from a peer-reviewed journal.

21. (lynch2024propensitymatchedcomparison media 7250a862): David R. Lynch, Angie Goldsberry, Christian Rummey, Jennifer Farmer, Sylvia Boesch, Martin B. Delatycki, Paola Giunti, J. Chad Hoyle, Caterina Mariotti, Katherine D. Mathews, Wolfgang Nachbauer, Susan Perlman, S.H. Subramony, George Wilmot, Theresa Zesiewicz, Lisa Weissfeld, and Colin Meyer. Propensity matched comparison of omaveloxolone treatment to friedreich ataxia natural history data. Annals of Clinical and Translational Neurology, 11:4-16, Sep 2024. URL: https://doi.org/10.1002/acn3.51897, doi:10.1002/acn3.51897. This article has 56 citations and is from a peer-reviewed journal.

22. (lynch2024propensitymatchedcomparison media d049e362): David R. Lynch, Angie Goldsberry, Christian Rummey, Jennifer Farmer, Sylvia Boesch, Martin B. Delatycki, Paola Giunti, J. Chad Hoyle, Caterina Mariotti, Katherine D. Mathews, Wolfgang Nachbauer, Susan Perlman, S.H. Subramony, George Wilmot, Theresa Zesiewicz, Lisa Weissfeld, and Colin Meyer. Propensity matched comparison of omaveloxolone treatment to friedreich ataxia natural history data. Annals of Clinical and Translational Neurology, 11:4-16, Sep 2024. URL: https://doi.org/10.1002/acn3.51897, doi:10.1002/acn3.51897. This article has 56 citations and is from a peer-reviewed journal.

23. (perlman2025managingaminotransferaseelevations pages 7-9): Susan Perlman, Mathieu Anheim, Sylvia Boesch, James H. Lewis, and David R. Lynch. Managing aminotransferase elevations in patients with friedreich ataxia treated with omaveloxolone: a review and expert opinion on use considerations. Neurology and Therapy, 14:1209-1227, Jun 2025. URL: https://doi.org/10.1007/s40120-025-00752-8, doi:10.1007/s40120-025-00752-8. This article has 8 citations and is from a domain leading peer-reviewed journal.

24. (perlman2025managingaminotransferaseelevations pages 1-3): Susan Perlman, Mathieu Anheim, Sylvia Boesch, James H. Lewis, and David R. Lynch. Managing aminotransferase elevations in patients with friedreich ataxia treated with omaveloxolone: a review and expert opinion on use considerations. Neurology and Therapy, 14:1209-1227, Jun 2025. URL: https://doi.org/10.1007/s40120-025-00752-8, doi:10.1007/s40120-025-00752-8. This article has 8 citations and is from a domain leading peer-reviewed journal.

25. (perlman2025managingaminotransferaseelevations pages 11-14): Susan Perlman, Mathieu Anheim, Sylvia Boesch, James H. Lewis, and David R. Lynch. Managing aminotransferase elevations in patients with friedreich ataxia treated with omaveloxolone: a review and expert opinion on use considerations. Neurology and Therapy, 14:1209-1227, Jun 2025. URL: https://doi.org/10.1007/s40120-025-00752-8, doi:10.1007/s40120-025-00752-8. This article has 8 citations and is from a domain leading peer-reviewed journal.

26. (lima2025earlyexperienceon pages 4-5): Salvatore Maria Lima, Marta Caltagirone, Christian Messina, Umberto Quartetti, Nicasio Rini, Flora D’Amico, Filippo Brighina, and Vincenzo Di Stefano. Early experience on omaveloxolone in adult patients with friedreich’s ataxia: a real-world observational study. Journal of Neurology, Nov 2025. URL: https://doi.org/10.1007/s00415-025-13487-1, doi:10.1007/s00415-025-13487-1. This article has 1 citations and is from a domain leading peer-reviewed journal.

27. (osaki2026fromgeneticmutation pages 11-12): Yuta Osaki, Umme Sabrina Haque, and Toshifumi Yokota. From genetic mutation to therapy in friedreich ataxia: molecular mechanisms, therapeutic advances, and translational challenges. Unknown journal, Apr 2026. URL: https://doi.org/10.20944/preprints202604.1108.v1, doi:10.20944/preprints202604.1108.v1.

28. (bouchard2023findinganappropriate pages 1-2): Camille Bouchard, Catherine Gérard, Solange Gni-fiene Yanyabé, Nathalie Majeau, Malek Aloui, Gabrielle Buisson, Pouiré Yameogo, Vanessa Couture, and Jacques P. Tremblay. Finding an appropriate mouse model to study the impact of a treatment for friedreich ataxia on the behavioral phenotype. Genes, 14:1654, Aug 2023. URL: https://doi.org/10.3390/genes14081654, doi:10.3390/genes14081654. This article has 8 citations.

29. (pandolfo2025friedreichataxia pages 5-6): Massimo Pandolfo. Friedreich ataxia. Neurology Genetics, Feb 2025. URL: https://doi.org/10.1212/nxg.0000000000200236, doi:10.1212/nxg.0000000000200236. This article has 6 citations.

30. (lynch2024propensitymatchedcomparison pages 8-10): David R. Lynch, Angie Goldsberry, Christian Rummey, Jennifer Farmer, Sylvia Boesch, Martin B. Delatycki, Paola Giunti, J. Chad Hoyle, Caterina Mariotti, Katherine D. Mathews, Wolfgang Nachbauer, Susan Perlman, S.H. Subramony, George Wilmot, Theresa Zesiewicz, Lisa Weissfeld, and Colin Meyer. Propensity matched comparison of omaveloxolone treatment to friedreich ataxia natural history data. Annals of Clinical and Translational Neurology, 11:4-16, Sep 2024. URL: https://doi.org/10.1002/acn3.51897, doi:10.1002/acn3.51897. This article has 56 citations and is from a peer-reviewed journal.
