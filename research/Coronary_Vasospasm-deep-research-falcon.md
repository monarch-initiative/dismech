---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T23:11:18.872737'
end_time: '2026-05-05T23:32:20.489006'
duration_seconds: 1261.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Coronary Vasospasm
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Coronary Vasospasm
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Coronary Vasospasm** covering all of the
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
- **Disease Name:** Coronary Vasospasm
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Coronary Vasospasm** covering all of the
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


# Coronary Vasospasm (Vasospastic Angina) — Comprehensive Disease Characteristics Report (2023–2024 prioritized)

## Executive overview
Coronary vasospasm (CAS) is a transient, often reversible, hyperconstriction of epicardial coronary arteries and/or the coronary microcirculation that can cause myocardial ischemia ranging from angina to acute coronary syndrome (ACS), myocardial infarction with non‑obstructive coronary arteries (MINOCA), malignant arrhythmias, syncope, and sudden cardiac death. Contemporary frameworks treat epicardial vasospastic angina (VSA) and microvascular spasm as related but distinct endotypes within angina/ischemia with non‑obstructive coronary arteries (ANOCA/INOCA). (jenkins2024vasospasticanginaa pages 1-1, lanza2023managementofcoronary pages 1-2, huang2023invasiveevaluationfor pages 3-4)

| Topic | Key data (with numbers and thresholds) | Population/Context | Source (first author, year, journal) | URL | Evidence type |
|---|---|---|---|---|---|
| Prevalence | Epicardial spasm prevalence **43%** (range **16–73%**); microvascular spasm **25%** (range **7–39%**) (woudstra2023metaanalysisandsystematic pages 9-10, woudstra2023metaanalysisandsystematic pages 1-2) | ANOCA patients; 25 studies, **N=14,554**, mean age 58.2 y, 44.2% women (woudstra2023metaanalysisandsystematic pages 1-2, woudstra2023metaanalysisandsystematic pages 2-4) | Woudstra, 2023, *Frontiers in Cardiovascular Medicine* | https://doi.org/10.3389/fcvm.2023.1129159 | Systematic review/meta-analysis |
| Recent-study prevalence | In studies published in the prior 5 years, overall CAS prevalence about **50%** (95% CI **36–64%**) (woudstra2023metaanalysisandsystematic pages 2-4) | Heterogeneous ANOCA/CAS literature with mixed protocols/criteria | Woudstra, 2023, *Frontiers in Cardiovascular Medicine* | https://doi.org/10.3389/fcvm.2023.1129159 | Systematic review/meta-analysis |
| Region differences | Epicardial spasm more frequent in **Asian vs Western** cohorts: **52% vs 33%** (**p=0.014**); microvascular spasm approximately **20% vs 33%**, difference not statistically significant (woudstra2023metaanalysisandsystematic pages 9-10, woudstra2023metaanalysisandsystematic pages 6-8) | ANOCA cohorts undergoing provocative testing | Woudstra, 2023, *Frontiers in Cardiovascular Medicine* | https://doi.org/10.3389/fcvm.2023.1129159 | Systematic review/meta-analysis |
| Sex differences | Men more likely to have epicardial spasm (**61%** of epicardial spasm patients male); women more likely to have microvascular spasm (**64%** female) (woudstra2023metaanalysisandsystematic pages 9-10, woudstra2023metaanalysisandsystematic pages 1-2, woudstra2023metaanalysisandsystematic pages 11-12) | ANOCA/CAS cohorts | Woudstra, 2023, *Frontiers in Cardiovascular Medicine* | https://doi.org/10.3389/fcvm.2023.1129159 | Systematic review/meta-analysis |
| Risk-factor profile | In epicardial spasm cohorts: smoking about **49%**, dyslipidaemia **47%**, diabetes **17%**, hypertension **47%** (woudstra2023metaanalysisandsystematic pages 8-9) | Epicardial spasm patients from pooled ANOCA studies | Woudstra, 2023, *Frontiers in Cardiovascular Medicine* | https://doi.org/10.3389/fcvm.2023.1129159 | Systematic review/meta-analysis |
| Recurrence/prognosis | Recurrent angina reported in **10–53%** during follow-up; examples include **17%** rehospitalisation for repeated angina, **21%** persistent angina, **53%** angina recurrence in one cohort (woudstra2023metaanalysisandsystematic pages 9-10, woudstra2023metaanalysisandsystematic pages 1-2, woudstra2023metaanalysisandsystematic pages 8-9) | Follow-up across CAS/epicardial spasm cohorts | Woudstra, 2023, *Frontiers in Cardiovascular Medicine* | https://doi.org/10.3389/fcvm.2023.1129159 | Systematic review/meta-analysis |
| MACE/MI burden | MACE reported in **268 patients (12%)** with epicardial spasm; one cohort reported **5%** MACE, with **90%** of events due to unstable angina hospitalization; MI incidence reported across **8 studies (n=4,737)** over **1–11.7 years** (woudstra2023metaanalysisandsystematic pages 9-10, woudstra2023metaanalysisandsystematic pages 8-9) | Long-term follow-up in epicardial spasm/CAS cohorts | Woudstra, 2023, *Frontiers in Cardiovascular Medicine* | https://doi.org/10.3389/fcvm.2023.1129159 | Systematic review/meta-analysis |
| Severe complications | CAS-related cardiac arrest reported in **3.5%** (7/202) of one Caucasian variant angina series and **2.4%** (35/1,429) of one Japanese VSA series (lanza2023managementofcoronary pages 6-6) | Variant angina/VSA case series | Lanza, 2023, *European Cardiology Review* | https://doi.org/10.15420/ecr.2022.47 | Narrative review |
| Natural history timing | Up to **75%** of acute events, including sudden death, occur within the first **1–3 months** after symptom onset (lanza2023managementofcoronary pages 2-3) | CAS/VSA natural history | Lanza, 2023, *European Cardiology Review* | https://doi.org/10.15420/ecr.2022.47 | Narrative review |
| Clinical definition/synonyms | VSA = chest pain from myocardial ischemia due to epicardial coronary spasm; synonymous terms include **Prinzmetal angina** and **variant angina**; transient spasm may cause episodic chest pain, persistent spasm may cause MI (jenkins2024vasospasticanginaa pages 1-1, lanza2023managementofcoronary pages 1-2) | Disease overview/clinical practice | Jenkins, 2024, *Therapeutic Advances in Cardiovascular Disease* | https://doi.org/10.1177/17539447241230400 | Review |
| Diagnostic criteria: epicardial spasm | COVADIS/consensus criteria: **nitrate-responsive angina** plus either transient ischemic ECG changes or coronary spasm documentation; definitive epicardial spasm on provocation requires reproduction of symptoms, ischemic ECG changes, and **≥90%** epicardial constriction/total or subtotal occlusion (huang2023invasiveevaluationfor pages 3-4, marchini2024sheddinglighton pages 3-5) | Invasive provocative testing with ACh/ergonovine | Huang, 2023, *US Cardiology Review*; Marchini, 2024, *Cardiovascular Drugs and Therapy* | https://doi.org/10.15420/usc.2022.33 ; https://doi.org/10.1007/s10557-022-07351-x | Review/systematic review |
| Diagnostic criteria: ECG thresholds | Transient ischemic ECG criteria include ST elevation or depression **≥0.1 mV** in **≥2 contiguous leads**; new negative U waves also accepted in COVADIS-based criteria (marchini2024sheddinglighton pages 3-5) | Provoked or spontaneous ischemic episodes | Marchini, 2024, *Cardiovascular Drugs and Therapy* | https://doi.org/10.1007/s10557-022-07351-x | Systematic review |
| Diagnostic criteria: microvascular spasm | Microvascular spasm defined by typical angina and ischemic ECG changes during intracoronary ACh **without epicardial spasm/no overt epicardial constriction** on angiography (huang2023invasiveevaluationfor pages 3-4, gurgoglione2024coronaryspasmtesting pages 5-7, marchini2024sheddinglighton pages 3-5) | Invasive coronary reactivity testing | Huang, 2023, *US Cardiology Review*; Gurgoglione, 2024, *Life* | https://doi.org/10.15420/usc.2022.33 ; https://doi.org/10.3390/life14030292 | Review |
| Diagnostic protocol | Typical ACh protocol: LCA **20–50–100 µg** (some centers add **200 µg**), RCA **20–50 µg**; ECG every **30 s**; angiography **1 min** after each injection or with symptoms/ischemic changes (gurgoglione2024coronaryspasmtesting pages 5-7, gurgoglione2024coronaryspasmtesting media 871e19c7) | Contemporary invasive provocative testing | Gurgoglione, 2024, *Life* | https://doi.org/10.3390/life14030292 | Review |
| Testing enhancement | Adding **200 µg** ACh in the LCA increased positive-test rate **40.9% vs 19.3%**, with specificity still about **90%** and no major complications reported in the cited series (gurgoglione2024coronaryspasmtesting pages 5-7) | High-dose LCA ACh strategy | Gurgoglione, 2024, *Life* | https://doi.org/10.3390/life14030292 | Review |
| Testing safety | Early serious complication rates **0.3–0.4%**; life-threatening arrhythmias **0.5–0.6%** in experienced Eastern centers; systematic review overall ACh side effects about **0.5%**; one meta-analysis found major complications **1.09%** and minor complications **5.87%** with ACh; ACh-related death not reported (gurgoglione2024coronaryspasmtesting pages 9-10) | Intracoronary ACh provocation testing | Gurgoglione, 2024, *Life* | https://doi.org/10.3390/life14030292 | Review |
| Testing safety in real-world trial planning | Additional ACh test after spinal cord stimulator implantation described as having severe cardiac complication risk **0–0.7%**, comparable to coronary angiography with FFR measurement (NCT06176391 chunk 1) | Prospective pilot study in refractory VSA | Wille/Amsterdam UMC, 2023 registry entry, *ClinicalTrials.gov* (NCT06176391) | https://clinicaltrials.gov/study/NCT06176391 | Clinical trial registry |
| Genetics: RNF213 | GWAS identified **RNF213** locus as top VSA signal; overall OR **2.34** (95% CI **1.99–2.74**, **P=4.4×10^-25**); lead variant **rs112735431 p.Arg4810Lys** OR **2.18** (95% CI **1.83–2.59**, **P=2.0×10^-18**); homozygotes OR **18.34** (95% CI **5.15–65.22**) (hikino2024rnf213variantsvasospastic pages 3-4, hikino2024rnf213variantsvasospastic pages 1-2, hikino2024rnf213variantsvasospastic pages 4-4) | Japanese GWAS/meta-analysis; East Asian-specific rare missense allele | Hikino, 2024, *JAMA Cardiology* | https://doi.org/10.1001/jamacardio.2024.1483 | GWAS/genetic association study |
| Genetics and fatal MI risk | Among carriers without baseline CAD, RNF213 rs112735431 associated with acute MI mortality during follow-up: HR **2.71** (95% CI **1.57–4.65**, **P=3.3×10^-4**) (hikino2024rnf213variantsvasospastic pages 1-2) | Registry follow-up linked to genetic study | Hikino, 2024, *JAMA Cardiology* | https://doi.org/10.1001/jamacardio.2024.1483 | GWAS/genetic association study |
| Ongoing real-world implementation | BELmicro registry plans to enroll **650** patients to measure real-world frequency of coronary microvascular dysfunction and/or coronary artery vasospasm and track **1-year** and **3-year** MACE (NCT06089031 chunk 1) | Prospective Belgian multicenter registry of coronary function testing | University Hospital Antwerp, 2023 registry entry, *ClinicalTrials.gov* (NCT06089031) | https://clinicaltrials.gov/study/NCT06089031 | Clinical trial registry |


*Table: This table compiles the main quantitative findings on epidemiology, prognosis, diagnostic thresholds, safety, and recent genetics for coronary vasospasm/vasospastic angina. It is designed as a quick-reference evidence summary for knowledge-base curation and report writing.*

## 1. Disease information
### 1.1 Definition and current clinical concept
* **Vasospastic angina (VSA)** is chest pain due to **myocardial ischemia caused by epicardial coronary spasm**, described as “a sudden narrowing of the vessels responsible for an inadequate supply of blood and oxygen.” (jenkins2024vasospasticanginaa pages 1-1)
* Synonyms and related terms used in modern reviews include **coronary artery spasm (CAS)**, **Prinzmetal angina**, and **variant angina**. (jenkins2024vasospasticanginaa pages 1-1, lanza2023managementofcoronary pages 1-2, huang2023invasiveevaluationfor pages 7-8)
* CAS can be **focal** or **diffuse**, can occur in angiographically normal segments or coexist with plaques, and can manifest as classic rest angina, exertional angina, or ACS presentations. (lanza2023managementofcoronary pages 1-2, gurgoglione2024coronaryspasmtesting pages 9-10)

### 1.2 Key identifiers and ontology/coding
* **MeSH**
  * *Coronary Vasospasm* — MeSH **D003329** (as used in ClinicalTrials.gov derived condition browse for BELmicro registry). (NCT06089031 chunk 1)
  * *Angina Pectoris, Variant* — MeSH **D000788** (ClinicalTrials.gov condition browse for ReACHallenge). (NCT05618132 chunk 1)
* **EFO (Open Targets)**
  * *Coronary Vasospasm* — **EFO_0004225**; *Prinzmetal’s angina* — **EFO_1000013** (retrieved from Open Targets search; no MONDO mapping was available in the retrieved evidence). (elsabbagh2024coronaryarteryspasm—risk pages 7-8)
* **MONDO**: not retrieved from the accessible texts in this run; would require an ontology lookup outside the retrieved evidence.
* **ICD-10/ICD-11**: not retrieved from accessible texts in this run.

### 1.3 Data provenance
This report integrates (i) **aggregated disease-level evidence** from systematic reviews and narrative reviews and (ii) **clinical trial registry metadata** (ClinicalTrials.gov) describing real-world diagnostic implementation and ongoing trials. (woudstra2023metaanalysisandsystematic pages 1-2, lanza2023managementofcoronary pages 6-6, NCT05618132 chunk 1)

## 2. Etiology
### 2.1 Primary causal factors (mechanistic)
CAS/VSA is generally understood as a **vasomotor disorder** driven by the convergence of:
1) **Endothelial dysfunction** (impaired NO/vasodilator signaling with relative excess of vasoconstrictors), and
2) **Vascular smooth muscle cell (VSMC) hyperreactivity/hypercontraction**, prominently involving **RhoA/Rho‑kinase (ROCK)**–mediated calcium sensitization. (gurgoglione2024coronaryspasmtesting pages 2-4, godo2023coronarymicrovascularspasm pages 3-4, nishimiya2023mechanismsofcoronary pages 2-3)

### 2.2 Risk factors
From ANOCA cohorts undergoing spasm testing, common cardiovascular risk factors in epicardial spasm populations include smoking, dyslipidaemia, diabetes, and hypertension (approximate pooled prevalences listed in the evidence table). (woudstra2023metaanalysisandsystematic pages 8-9)

Common triggers discussed in modern reviews include stress-related autonomic surges and vasoactive exposures (e.g., cocaine, alcohol) and metabolic contributors such as magnesium deficiency. (jenkins2024vasospasticanginaa pages 1-3, huang2023invasiveevaluationfor pages 2-3, elsabbagh2024coronaryarteryspasm—risk pages 5-7)

### 2.3 Protective factors
Protective factors are not well quantified in the retrieved evidence. Mechanistically, preservation of endothelial NO signaling would be expected to be protective, and clinical use of vasodilators (CCBs) is foundational for preventing attacks. (huang2023invasiveevaluationfor pages 7-8, lanza2023managementofcoronary pages 6-6)

### 2.4 Gene–environment interactions
Reviews emphasize that genetic susceptibility (e.g., NO/ALDH2 pathways) may interact with exposures that increase oxidative stress and ROCK activity, notably **smoking** and **stress**, to increase spasm propensity. (gurgoglione2024coronaryspasmtesting pages 2-4, elsabbagh2024coronaryarteryspasm—risk pages 7-8)

## 3. Phenotypes
### 3.1 Core clinical phenotypes
**Symptoms / clinical signs**
* **Angina at rest** often with a circadian pattern (e.g., early morning), classically in variant angina, though exertional or stress-triggered episodes also occur. (lanza2023managementofcoronary pages 1-2, jenkins2024vasospasticanginaa pages 1-3)
* **Transient ischemic ECG changes** during attacks, including ST-segment elevation (classic) but also ST depression and T-wave changes. (jenkins2024vasospasticanginaa pages 1-1, lanza2023managementofcoronary pages 1-2)

**Complications / severe phenotypes**
* **Acute MI / ACS / MINOCA** can occur when spasm is prolonged; reviews explicitly note that persistent spasm can lead to MI. (jenkins2024vasospasticanginaa pages 1-1)
* **Syncope and sudden cardiac death**: VSA is associated with major adverse events including “sudden cardiac death, acute MI and syncope.” (jenkins2024vasospasticanginaa pages 1-1)

### 3.2 Phenotype characteristics
* **Typical onset**: adult; attacks may be episodic and fluctuating. (lanza2023managementofcoronary pages 1-2)
* **Progression/course**: variable; early period after onset may be particularly high risk (see Temporal Development). (lanza2023managementofcoronary pages 2-3)

### 3.3 Frequencies and quality-of-life impact
* In ANOCA populations, recurrent angina during follow-up is common (reported range **10–53%**). (woudstra2023metaanalysisandsystematic pages 1-2)
* A recent review reported substantial psychosocial burden (e.g., “>70% impact on mental health”) in INOCA/VSA contexts. (jenkins2024vasospasticanginaa pages 1-3)

### 3.4 Suggested HPO terms (examples)
* Chest pain/angina: **HP:0100749 (Angina pectoris)**
* Syncope: **HP:0001279**
* Myocardial infarction: **HP:0001658**
* ST segment elevation: **HP:0012252**; ST segment depression: **HP:0012253**
* Ventricular fibrillation: **HP:0001663**

(These HPO identifiers are suggested for knowledge-base normalization; they are not explicitly enumerated in the retrieved papers.)

## 4. Genetic / molecular information
### 4.1 High-confidence genetic association (2024 GWAS)
A 2024 genetic association study identified **RNF213** as a major susceptibility locus for VSA:
* Overall association at RNF213 locus: **OR 2.34 (95% CI 1.99–2.74; P=4.4×10−25)**. (hikino2024rnf213variantsvasospastic pages 1-2)
* Lead variant **rs112735431 (p.Arg4810Lys)**: **OR 2.18 (95% CI 1.83–2.59; P=2.0×10−18)**; homozygotes showed a much larger effect (OR 18.34). (hikino2024rnf213variantsvasospastic pages 3-4, hikino2024rnf213variantsvasospastic pages 1-2)
* Importantly, in follow-up among carriers without baseline CAD, this allele was associated with increased acute MI mortality: **HR 2.71 (95% CI 1.57–4.65; P=3.3×10−4)**. (hikino2024rnf213variantsvasospastic pages 1-2)

### 4.2 Candidate genetic contributors cited in mechanistic reviews
Mechanistic/risk-factor reviews cite associations involving:
* **ALDH2** East Asian variant (associated with coronary spastic angina) (elsabbagh2024coronaryarteryspasm—risk pages 7-8)
* **NOS3/eNOS**: **T−786→C** promoter variant “associated with coronary spasm” (elsabbagh2024coronaryarteryspasm—risk pages 7-8)
* **ACE** variants described as a genetic risk factor for coronary spasm with implication in MI pathogenesis (elsabbagh2024coronaryarteryspasm—risk pages 7-8)
* Paraoxonase polymorphism (Q192R) and PLC-δ1 variant (R257H) noted in review-level summaries (elsabbagh2024coronaryarteryspasm—risk pages 5-7, elsabbagh2024coronaryarteryspasm—risk pages 7-8)

**Variant classification / allele frequencies**: not available from the retrieved texts; curated variant-level annotation would require ClinVar/gnomAD retrieval.

### 4.3 Mechanistic molecular pathways (key nodes)
Core signaling nodes repeatedly emphasized:
* **NO–cGMP signaling** (endothelium → VSMC) (gurgoglione2024coronaryspasmtesting pages 2-4)
* **Endothelin‑1** and other vasoconstrictors (gurgoglione2024coronaryspasmtesting pages 2-4, huang2023invasiveevaluationfor pages 2-3)
* **RhoA/ROCK → myosin phosphatase inhibition → increased MLC phosphorylation → VSMC hypercontraction** (nishimiya2023mechanismsofcoronary pages 2-3, gurgoglione2024coronaryspasmtesting pages 19-20)

## 5. Environmental information
Environmental/lifestyle contributors commonly referenced include smoking (oxidative stress/inflammation), stress/catecholamine surges, and vasoactive substances (e.g., cocaine, alcohol). (huang2023invasiveevaluationfor pages 2-3, jenkins2024vasospasticanginaa pages 1-3)

## 6. Mechanism / pathophysiology (causal chains)
### 6.1 Upstream triggers
* **Inflammation** (adventitial/perivascular inflammation; cytokines such as IL‑1β) can upregulate ROCK activity and induce reproducible spasm in models. (nishimiya2023mechanismsofcoronary pages 1-2, nishimiya2023mechanismsofcoronary pages 2-3)
* **Oxidative stress** and impaired aldehyde detoxification (e.g., ALDH2 deficiency) may increase susceptibility via ROS-mediated endothelial impairment. (elsabbagh2024coronaryarteryspasm—risk pages 5-7)

### 6.2 Core pathophysiologic cascade (integrated model)
A consistent mechanistic chain described across modern reviews is:
1) **Endothelial dysfunction** → reduced NO bioavailability and impaired ACh-mediated vasodilation, allowing paradoxical vasoconstriction. (gurgoglione2024coronaryspasmtesting pages 2-4, huang2023invasiveevaluationfor pages 2-3)
2) **ROCK-mediated Ca2+ sensitization in VSMCs** → myosin phosphatase inhibition → increased myosin light-chain phosphorylation → **hypercontraction**. (nishimiya2023mechanismsofcoronary pages 2-3, gurgoglione2024coronaryspasmtesting pages 19-20)
3) **Clinical spasm** (epicardial and/or microvascular) → transient ischemia → angina/ECG changes; prolonged or severe episodes → arrhythmia, MI, cardiac arrest. (lanza2023managementofcoronary pages 1-2, jenkins2024vasospasticanginaa pages 1-1)

### 6.3 Suggested GO biological process terms (examples)
* Smooth muscle contraction: **GO:0006939**
* Regulation of blood vessel diameter: **GO:0097746**
* Response to oxidative stress: **GO:0006979**
* Inflammatory response: **GO:0006954**

### 6.4 Suggested Cell Ontology (CL) cell types (examples)
* Vascular smooth muscle cell: **CL:0000192**
* Endothelial cell: **CL:0000115**
* Macrophage: **CL:0000235**; Mast cell: **CL:0000097**

(These ontology terms are suggested for normalization; the reviews describe these cell types but do not enumerate ontology IDs.) (godo2023coronarymicrovascularspasm pages 3-4, nishimiya2023mechanismsofcoronary pages 1-2)

## 7. Anatomical structures affected
### 7.1 Organ/tissue
* Primary: coronary arteries (epicardial segments) and coronary microcirculation. (huang2023invasiveevaluationfor pages 3-4, gurgoglione2024coronaryspasmtesting pages 5-7)

### 7.2 Suggested UBERON terms (examples)
* Heart: **UBERON:0000948**
* Coronary artery: **UBERON:0001621**

## 8. Temporal development
* Episodes are often **episodic**, with a circadian pattern in classic VSA. (jenkins2024vasospasticanginaa pages 1-3)
* A management review emphasized that **up to 75% of acute events (including sudden death) occur within the first 1–3 months after symptom onset**, supporting an early “high-risk” window. (lanza2023managementofcoronary pages 2-3)

## 9. Inheritance and population
### 9.1 Epidemiology in tested ANOCA populations (meta-analysis)
A 2023 systematic review/meta-analysis of ANOCA patients undergoing spasm provocation testing reported:
* **Epicardial spasm** prevalence **43%** (range 16–73%), and **microvascular spasm** prevalence **25%** (range 7–39%). (woudstra2023metaanalysisandsystematic pages 1-2)
* Regional differences: epicardial spasm **52% in Asian** vs **33% in Western** cohorts (p=0.014). (woudstra2023metaanalysisandsystematic pages 1-2)
* Sex differences: men more often epicardial spasm (≈61%); women more often microvascular spasm (≈64%). (woudstra2023metaanalysisandsystematic pages 1-2)

### 9.2 Genetic architecture
RNF213 rs112735431 is an East Asian–enriched risk allele with substantial VSA association and may stratify MI risk in carriers. (hikino2024rnf213variantsvasospastic pages 1-2)

## 10. Diagnostics
### 10.1 Standardized criteria (COVADIS-aligned)
**Epicardial spasm / VSA (definitive evidence)**
* Nitrate-responsive angina plus objective evidence: transient ischemic ECG changes or angiographic documentation of spasm. (huang2023invasiveevaluationfor pages 3-4, marchini2024sheddinglighton pages 3-5)
* During provocation, a **positive test** is defined by reproduction of symptoms, ischemic ECG changes, and **≥90% epicardial constriction** (transient total/subtotal occlusion). (huang2023invasiveevaluationfor pages 3-4, marchini2024sheddinglighton pages 3-5)

**Transient ischemic ECG thresholds (COVADIS-derived)**
* ST elevation ≥0.1 mV or ST depression ≥0.1 mV in ≥2 contiguous leads; negative U waves are also accepted. (marchini2024sheddinglighton pages 3-5)

**Microvascular spasm**
* Typical symptoms and ischemic ECG changes after intracoronary ACh **without epicardial spasm** (no significant epicardial diameter reduction). (huang2023invasiveevaluationfor pages 3-4, marchini2024sheddinglighton pages 3-5)

### 10.2 Provocation testing and real-world implementation
**Acetylcholine (ACh) provocation protocol (typical contemporary regimen)**
* Stepwise intracoronary dosing often uses LCA boluses **20–50–100 μg** (some add **200 μg**) and RCA **20–50 μg**, separated by 2–3 minutes; ECG is monitored frequently and angiography performed after each dose or with symptoms/ECG changes. (gurgoglione2024coronaryspasmtesting pages 5-7)

**Safety and adverse events**
* A 2024 review summarized that ACh testing has low but non-zero complication rates; serious complications and life‑threatening arrhythmias are rare and ACh-related death has not been reported. Quantitative safety figures summarized include early serious complication rates **0.3–0.4%**, life‑threatening arrhythmias **0.5–0.6%**, and meta-analytic estimates of major/minor complication frequencies. (gurgoglione2024coronaryspasmtesting pages 9-10)

**Visual evidence (protocol/algorithm and protocol table)**
* ACh testing protocol flowchart and protocol comparison table are available from the retrieved figures/tables. (gurgoglione2024coronaryspasmtesting media 871e19c7, gurgoglione2024coronaryspasmtesting media ac042141)

### 10.3 Differential diagnosis (high-level)
In ANOCA/INOCA contexts, VSA must be distinguished from microvascular angina/CMD endotypes; invasive testing can clarify endotype for stratified therapy. (huang2023invasiveevaluationfor pages 3-4, woudstra2023metaanalysisandsystematic pages 11-12)

## 11. Outcomes / prognosis
### 11.1 Recurrent symptoms and MACE composition
In ANOCA cohorts with CAS, recurrent angina is common (10–53% across studies), and MACE is often dominated by rehospitalization/unstable angina rather than death/MI in many cohorts. (woudstra2023metaanalysisandsystematic pages 1-2, woudstra2023metaanalysisandsystematic pages 9-10)

### 11.2 Severe outcomes
Cardiac arrest due to CAS-related ventricular tachyarrhythmias is emphasized as “the most severe complication,” with reported prevalence in illustrative cohorts (≈2–4%). (lanza2023managementofcoronary pages 6-6)

## 12. Treatment
### 12.1 Pharmacotherapy (current practice pattern)
* **First-line**: **Calcium channel blockers (CCBs)** are first-line for CAS/VSA. (lanza2023managementofcoronary pages 6-6)
* **Second-line/add-on**: **Long-acting nitrates** (and where available **nicorandil**) can be added if symptoms are not controlled by CCBs. (lanza2023managementofcoronary pages 6-6)
* **Nitrate strategy caution**: long-acting nitrates may have drawbacks (tolerance, endothelial dysfunction concerns) and are recommended as adjuncts when CCBs are insufficient. (huang2023invasiveevaluationfor pages 7-8)

### 12.2 Refractory disease and device therapy
For refractory CAS, multiple alternative interventions have been proposed, including **ROCK inhibition (fasudil)**, anti-adrenergic approaches, neural therapies, and in select cases device therapy (ICD/pacemaker) when syncope/cardiac arrest is attributable to CAS-related arrhythmias. (lanza2023managementofcoronary pages 6-6)

### 12.3 Mechanism-based therapy insight (expert synthesis)
Across mechanistic reviews, the centrality of **ROCK-mediated VSMC hypercontraction** supports investigation and selective use (where available) of ROCK inhibitors and other strategies that restore endothelial NO signaling or reduce inflammation/oxidative stress as mechanistically aligned approaches. (nishimiya2023mechanismsofcoronary pages 2-3, godo2023coronarymicrovascularspasm pages 3-4, gurgoglione2024coronaryspasmtesting pages 19-20)

### 12.4 Ongoing trials / real-world implementations (selected)
* **ReACHallenge (NCT05618132)** — “Stepwise Treatment and Acetylcholine Rechallenge…to guide patient-tailored treatment,” testing intracoronary verapamil ± nitroglycerin with ACh rechallenge in proven ACh-induced VSA; start date 2023‑01‑09. URL: https://clinicaltrials.gov/study/NCT05618132 (NCT05618132 chunk 1)
* **BELmicro registry (NCT06089031)** — multicenter registry of real-world coronary function testing (including ACh vasoreactivity testing) to quantify frequencies of CMD and vasospasm and track 1- and 3-year MACE; first posted 2023‑10‑18. URL: https://clinicaltrials.gov/study/NCT06089031 (NCT06089031 chunk 1)
* **Spinal cord stimulation for refractory VSA (NCT06176391)** — pilot study in refractory VSA, includes repeat ACh test at 6 months in consenting participants; first posted 2023‑12‑19. URL: https://clinicaltrials.gov/study/NCT06176391 (NCT06176391 chunk 1)
* **Vericiguat in VSA (NCT06415227; ViVA)** — randomized crossover phase 2 study targeting NO–sGC signaling; first posted 2024‑05‑16. URL: https://clinicaltrials.gov/study/NCT06415227 (NCT06415227 chunk 1)

### 12.5 Suggested MAXO terms (examples)
* Calcium channel blocker therapy; Nitrate therapy; Coronary angiography; Provocation testing; Implantable cardioverter-defibrillator implantation; Pacemaker implantation; Spinal cord stimulation. (These MAXO identifiers are suggested at the concept level; specific MAXO IDs were not present in the retrieved evidence.) (lanza2023managementofcoronary pages 6-6, NCT06176391 chunk 1)

## 13. Prevention
Evidence-based prevention in retrieved texts is mainly **risk-factor and trigger management** consistent with mechanistic drivers (e.g., smoking avoidance, stress reduction, adherence to vasodilator therapy). Stopping vasodilator therapy can provoke recurrence; early post-onset window is high risk. (lanza2023managementofcoronary pages 2-3, gurgoglione2024coronaryspasmtesting pages 2-4)

## 14. Other species / natural disease
No naturally occurring non-human disease model evidence was retrieved in this run.

## 15. Model organisms
Mechanistic understanding is supported by animal model literature (e.g., inflammatory IL‑1β adventitial exposure inducing spasm; ROCK inhibition suppressing spasm physiology), but explicit model-system metadata (strain, organism IDs) was not fully captured in the retrieved excerpts. (nishimiya2023mechanismsofcoronary pages 2-3)

---

## Notes on evidence quality and gaps
* The strongest quantitative epidemiology in this run is for **CAS prevalence in ANOCA cohorts undergoing provocation testing**, not population-wide incidence/prevalence; heterogeneity in protocols/definitions is a major limitation emphasized by the meta-analysis. (woudstra2023metaanalysisandsystematic pages 1-2, woudstra2023metaanalysisandsystematic pages 2-4)
* The strongest genetic evidence in this run is the **2024 RNF213 GWAS**, whereas ALDH2/NOS3/ACE findings are presented largely as prior association literature within review summaries in the retrieved excerpts (effect sizes not available here). (hikino2024rnf213variantsvasospastic pages 1-2, elsabbagh2024coronaryarteryspasm—risk pages 7-8)

## Key recent sources (URLs; publication dates)
* Woudstra et al., 2023-03, *Frontiers in Cardiovascular Medicine* (systematic review/meta-analysis): https://doi.org/10.3389/fcvm.2023.1129159 (woudstra2023metaanalysisandsystematic pages 1-2)
* Jenkins et al., 2024-01, *Therapeutic Advances in Cardiovascular Disease* (review): https://doi.org/10.1177/17539447241230400 (jenkins2024vasospasticanginaa pages 1-1)
* Gurgoglione et al., 2024-02, *Life* (review; ACh testing protocols/safety; includes figures/tables): https://doi.org/10.3390/life14030292 (gurgoglione2024coronaryspasmtesting pages 5-7, gurgoglione2024coronaryspasmtesting pages 9-10, gurgoglione2024coronaryspasmtesting media 871e19c7)
* Hikino et al., 2024-08, *JAMA Cardiology* (GWAS/genetic association): https://doi.org/10.1001/jamacardio.2024.1483 (hikino2024rnf213variantsvasospastic pages 1-2)
* Lanza & Shimokawa, 2023-05, *European Cardiology Review* (management review): https://doi.org/10.15420/ecr.2022.47 (lanza2023managementofcoronary pages 6-6)
* Marchini et al., 2024-06, *Cardiovascular Drugs and Therapy* (systematic review): https://doi.org/10.1007/s10557-022-07351-x (marchini2024sheddinglighton pages 3-5)



References

1. (jenkins2024vasospasticanginaa pages 1-1): Kenny Jenkins, Graziella Pompei, Nandine Ganzorig, Sarah Brown, John Beltrame, and Vijay Kunadian. Vasospastic angina: a review on diagnostic approach and management. Therapeutic Advances in Cardiovascular Disease, Jan 2024. URL: https://doi.org/10.1177/17539447241230400, doi:10.1177/17539447241230400. This article has 56 citations and is from a peer-reviewed journal.

2. (lanza2023managementofcoronary pages 1-2): Gaetano Antonio Lanza and Hiroaki Shimokawa. Management of coronary artery spasm. European Cardiology Review, May 2023. URL: https://doi.org/10.15420/ecr.2022.47, doi:10.15420/ecr.2022.47. This article has 33 citations.

3. (huang2023invasiveevaluationfor pages 3-4): Jingwen Huang, Rebecca Steinberg, Matthew J Brown, Stéphane Rinfret, and Olga Toleva. Invasive evaluation for coronary vasospasm. US Cardiology Review, Jun 2023. URL: https://doi.org/10.15420/usc.2022.33, doi:10.15420/usc.2022.33. This article has 5 citations.

4. (woudstra2023metaanalysisandsystematic pages 9-10): Janneke Woudstra, Caitlin E. M. Vink, Diantha J. M. Schipaanboord, Etto C. Eringa, Hester M. den Ruijter, Rutger G. T. Feenstra, Coen K. M. Boerhout, Marcel A. M. Beijk, Guus A. de Waard, Peter Ong, Andreas Seitz, Udo Sechtem, Jan J. Piek, Tim P. van de Hoef, and Yolande Appelman. Meta-analysis and systematic review of coronary vasospasm in anoca patients: prevalence, clinical features and prognosis. Frontiers in Cardiovascular Medicine, Mar 2023. URL: https://doi.org/10.3389/fcvm.2023.1129159, doi:10.3389/fcvm.2023.1129159. This article has 26 citations and is from a peer-reviewed journal.

5. (woudstra2023metaanalysisandsystematic pages 1-2): Janneke Woudstra, Caitlin E. M. Vink, Diantha J. M. Schipaanboord, Etto C. Eringa, Hester M. den Ruijter, Rutger G. T. Feenstra, Coen K. M. Boerhout, Marcel A. M. Beijk, Guus A. de Waard, Peter Ong, Andreas Seitz, Udo Sechtem, Jan J. Piek, Tim P. van de Hoef, and Yolande Appelman. Meta-analysis and systematic review of coronary vasospasm in anoca patients: prevalence, clinical features and prognosis. Frontiers in Cardiovascular Medicine, Mar 2023. URL: https://doi.org/10.3389/fcvm.2023.1129159, doi:10.3389/fcvm.2023.1129159. This article has 26 citations and is from a peer-reviewed journal.

6. (woudstra2023metaanalysisandsystematic pages 2-4): Janneke Woudstra, Caitlin E. M. Vink, Diantha J. M. Schipaanboord, Etto C. Eringa, Hester M. den Ruijter, Rutger G. T. Feenstra, Coen K. M. Boerhout, Marcel A. M. Beijk, Guus A. de Waard, Peter Ong, Andreas Seitz, Udo Sechtem, Jan J. Piek, Tim P. van de Hoef, and Yolande Appelman. Meta-analysis and systematic review of coronary vasospasm in anoca patients: prevalence, clinical features and prognosis. Frontiers in Cardiovascular Medicine, Mar 2023. URL: https://doi.org/10.3389/fcvm.2023.1129159, doi:10.3389/fcvm.2023.1129159. This article has 26 citations and is from a peer-reviewed journal.

7. (woudstra2023metaanalysisandsystematic pages 6-8): Janneke Woudstra, Caitlin E. M. Vink, Diantha J. M. Schipaanboord, Etto C. Eringa, Hester M. den Ruijter, Rutger G. T. Feenstra, Coen K. M. Boerhout, Marcel A. M. Beijk, Guus A. de Waard, Peter Ong, Andreas Seitz, Udo Sechtem, Jan J. Piek, Tim P. van de Hoef, and Yolande Appelman. Meta-analysis and systematic review of coronary vasospasm in anoca patients: prevalence, clinical features and prognosis. Frontiers in Cardiovascular Medicine, Mar 2023. URL: https://doi.org/10.3389/fcvm.2023.1129159, doi:10.3389/fcvm.2023.1129159. This article has 26 citations and is from a peer-reviewed journal.

8. (woudstra2023metaanalysisandsystematic pages 11-12): Janneke Woudstra, Caitlin E. M. Vink, Diantha J. M. Schipaanboord, Etto C. Eringa, Hester M. den Ruijter, Rutger G. T. Feenstra, Coen K. M. Boerhout, Marcel A. M. Beijk, Guus A. de Waard, Peter Ong, Andreas Seitz, Udo Sechtem, Jan J. Piek, Tim P. van de Hoef, and Yolande Appelman. Meta-analysis and systematic review of coronary vasospasm in anoca patients: prevalence, clinical features and prognosis. Frontiers in Cardiovascular Medicine, Mar 2023. URL: https://doi.org/10.3389/fcvm.2023.1129159, doi:10.3389/fcvm.2023.1129159. This article has 26 citations and is from a peer-reviewed journal.

9. (woudstra2023metaanalysisandsystematic pages 8-9): Janneke Woudstra, Caitlin E. M. Vink, Diantha J. M. Schipaanboord, Etto C. Eringa, Hester M. den Ruijter, Rutger G. T. Feenstra, Coen K. M. Boerhout, Marcel A. M. Beijk, Guus A. de Waard, Peter Ong, Andreas Seitz, Udo Sechtem, Jan J. Piek, Tim P. van de Hoef, and Yolande Appelman. Meta-analysis and systematic review of coronary vasospasm in anoca patients: prevalence, clinical features and prognosis. Frontiers in Cardiovascular Medicine, Mar 2023. URL: https://doi.org/10.3389/fcvm.2023.1129159, doi:10.3389/fcvm.2023.1129159. This article has 26 citations and is from a peer-reviewed journal.

10. (lanza2023managementofcoronary pages 6-6): Gaetano Antonio Lanza and Hiroaki Shimokawa. Management of coronary artery spasm. European Cardiology Review, May 2023. URL: https://doi.org/10.15420/ecr.2022.47, doi:10.15420/ecr.2022.47. This article has 33 citations.

11. (lanza2023managementofcoronary pages 2-3): Gaetano Antonio Lanza and Hiroaki Shimokawa. Management of coronary artery spasm. European Cardiology Review, May 2023. URL: https://doi.org/10.15420/ecr.2022.47, doi:10.15420/ecr.2022.47. This article has 33 citations.

12. (marchini2024sheddinglighton pages 3-5): Federico Marchini, Graziella Pompei, Emanuele D’Aniello, Andrea Marrone, Serena Caglioni, Simone Biscaglia, Gianluca Campo, and Matteo Tebaldi. Shedding light on treatment options for coronary vasomotor disorders: a systematic review. Cardiovascular Drugs and Therapy, 38:151-161, Jun 2024. URL: https://doi.org/10.1007/s10557-022-07351-x, doi:10.1007/s10557-022-07351-x. This article has 10 citations and is from a peer-reviewed journal.

13. (gurgoglione2024coronaryspasmtesting pages 5-7): Filippo Luca Gurgoglione, Luigi Vignali, Rocco Antonio Montone, Riccardo Rinaldi, Giorgio Benatti, Emilia Solinas, Antonio Maria Leone, Domenico Galante, Gianluca Campo, Simone Biscaglia, Italo Porto, Stefano Benenati, and Giampaolo Niccoli. Coronary spasm testing with acetylcholine: a powerful tool for a personalized therapy of coronary vasomotor disorders. Life, 14:292, Feb 2024. URL: https://doi.org/10.3390/life14030292, doi:10.3390/life14030292. This article has 16 citations.

14. (gurgoglione2024coronaryspasmtesting media 871e19c7): Filippo Luca Gurgoglione, Luigi Vignali, Rocco Antonio Montone, Riccardo Rinaldi, Giorgio Benatti, Emilia Solinas, Antonio Maria Leone, Domenico Galante, Gianluca Campo, Simone Biscaglia, Italo Porto, Stefano Benenati, and Giampaolo Niccoli. Coronary spasm testing with acetylcholine: a powerful tool for a personalized therapy of coronary vasomotor disorders. Life, 14:292, Feb 2024. URL: https://doi.org/10.3390/life14030292, doi:10.3390/life14030292. This article has 16 citations.

15. (gurgoglione2024coronaryspasmtesting pages 9-10): Filippo Luca Gurgoglione, Luigi Vignali, Rocco Antonio Montone, Riccardo Rinaldi, Giorgio Benatti, Emilia Solinas, Antonio Maria Leone, Domenico Galante, Gianluca Campo, Simone Biscaglia, Italo Porto, Stefano Benenati, and Giampaolo Niccoli. Coronary spasm testing with acetylcholine: a powerful tool for a personalized therapy of coronary vasomotor disorders. Life, 14:292, Feb 2024. URL: https://doi.org/10.3390/life14030292, doi:10.3390/life14030292. This article has 16 citations.

16. (NCT06176391 chunk 1): Frank Wille, MD. SCS for Vasospastic Angina Vasospastic Angina Pectoris - a Prospective Study. Amsterdam UMC, location VUmc. 2024. ClinicalTrials.gov Identifier: NCT06176391

17. (hikino2024rnf213variantsvasospastic pages 3-4): Keiko Hikino, Satoshi Koyama, Kaoru Ito, Yoshinao Koike, Masaru Koido, Takayoshi Matsumura, Ryo Kurosawa, Kohei Tomizuka, Shuji Ito, Xiaoxi Liu, Yuki Ishikawa, Yukihide Momozawa, Takayuki Morisaki, Yoichiro Kamatani, Taisei Mushiroda, Chikashi Terao, Yuji Yamanashi, Yoichi Furukawa, Yoshinori Murakami, Kaori Muto, Akiko Nagai, Wataru Obara, Ken Yamaji, Kazuhisa Takahashi, Satoshi Asai, Yasuo Takahashi, Takao Suzuki, Nobuaki Sinozaki, Hiroki Yamaguchi, Shiro Minami, Shigeo Murayama, Kozo Yoshimori, Satoshi Nagayama, Daisuke Obata, Masahiko Higashiyama, Akihide Matsumoto, and Yukihiro Koretsune. <i>rnf213</i> variants, vasospastic angina, and risk of fatal myocardial infarction. JAMA Cardiology, 9:723, Aug 2024. URL: https://doi.org/10.1001/jamacardio.2024.1483, doi:10.1001/jamacardio.2024.1483. This article has 21 citations and is from a highest quality peer-reviewed journal.

18. (hikino2024rnf213variantsvasospastic pages 1-2): Keiko Hikino, Satoshi Koyama, Kaoru Ito, Yoshinao Koike, Masaru Koido, Takayoshi Matsumura, Ryo Kurosawa, Kohei Tomizuka, Shuji Ito, Xiaoxi Liu, Yuki Ishikawa, Yukihide Momozawa, Takayuki Morisaki, Yoichiro Kamatani, Taisei Mushiroda, Chikashi Terao, Yuji Yamanashi, Yoichi Furukawa, Yoshinori Murakami, Kaori Muto, Akiko Nagai, Wataru Obara, Ken Yamaji, Kazuhisa Takahashi, Satoshi Asai, Yasuo Takahashi, Takao Suzuki, Nobuaki Sinozaki, Hiroki Yamaguchi, Shiro Minami, Shigeo Murayama, Kozo Yoshimori, Satoshi Nagayama, Daisuke Obata, Masahiko Higashiyama, Akihide Matsumoto, and Yukihiro Koretsune. <i>rnf213</i> variants, vasospastic angina, and risk of fatal myocardial infarction. JAMA Cardiology, 9:723, Aug 2024. URL: https://doi.org/10.1001/jamacardio.2024.1483, doi:10.1001/jamacardio.2024.1483. This article has 21 citations and is from a highest quality peer-reviewed journal.

19. (hikino2024rnf213variantsvasospastic pages 4-4): Keiko Hikino, Satoshi Koyama, Kaoru Ito, Yoshinao Koike, Masaru Koido, Takayoshi Matsumura, Ryo Kurosawa, Kohei Tomizuka, Shuji Ito, Xiaoxi Liu, Yuki Ishikawa, Yukihide Momozawa, Takayuki Morisaki, Yoichiro Kamatani, Taisei Mushiroda, Chikashi Terao, Yuji Yamanashi, Yoichi Furukawa, Yoshinori Murakami, Kaori Muto, Akiko Nagai, Wataru Obara, Ken Yamaji, Kazuhisa Takahashi, Satoshi Asai, Yasuo Takahashi, Takao Suzuki, Nobuaki Sinozaki, Hiroki Yamaguchi, Shiro Minami, Shigeo Murayama, Kozo Yoshimori, Satoshi Nagayama, Daisuke Obata, Masahiko Higashiyama, Akihide Matsumoto, and Yukihiro Koretsune. <i>rnf213</i> variants, vasospastic angina, and risk of fatal myocardial infarction. JAMA Cardiology, 9:723, Aug 2024. URL: https://doi.org/10.1001/jamacardio.2024.1483, doi:10.1001/jamacardio.2024.1483. This article has 21 citations and is from a highest quality peer-reviewed journal.

20. (NCT06089031 chunk 1):  Belgian Registry on Coronary Function Testing. University Hospital, Antwerp. 2021. ClinicalTrials.gov Identifier: NCT06089031

21. (huang2023invasiveevaluationfor pages 7-8): Jingwen Huang, Rebecca Steinberg, Matthew J Brown, Stéphane Rinfret, and Olga Toleva. Invasive evaluation for coronary vasospasm. US Cardiology Review, Jun 2023. URL: https://doi.org/10.15420/usc.2022.33, doi:10.15420/usc.2022.33. This article has 5 citations.

22. (NCT05618132 chunk 1):  ReACHallenge Trial: Acetylcholine Rechallenge After Pretreatment With Vasoactive Drugs. University Hospital, Antwerp. 2023. ClinicalTrials.gov Identifier: NCT05618132

23. (elsabbagh2024coronaryarteryspasm—risk pages 7-8): Farah El-Sabbagh, Noha M. Mesbah, Dina M Abo-El-Matty, and Tarek A. Abdelaziz. Coronary artery spasm—risk factors and pathophysiological mechanisms. Records of Pharmaceutical and Biomedical Sciences, 8:191-198, May 2024. URL: https://doi.org/10.21608/rpbs.2024.327931.1332, doi:10.21608/rpbs.2024.327931.1332. This article has 0 citations.

24. (gurgoglione2024coronaryspasmtesting pages 2-4): Filippo Luca Gurgoglione, Luigi Vignali, Rocco Antonio Montone, Riccardo Rinaldi, Giorgio Benatti, Emilia Solinas, Antonio Maria Leone, Domenico Galante, Gianluca Campo, Simone Biscaglia, Italo Porto, Stefano Benenati, and Giampaolo Niccoli. Coronary spasm testing with acetylcholine: a powerful tool for a personalized therapy of coronary vasomotor disorders. Life, 14:292, Feb 2024. URL: https://doi.org/10.3390/life14030292, doi:10.3390/life14030292. This article has 16 citations.

25. (godo2023coronarymicrovascularspasm pages 3-4): Shigeo Godo, Jun Takahashi, Takashi Shiroto, Satoshi Yasuda, and Hiroaki Shimokawa. Coronary microvascular spasm: clinical presentation and diagnosis. European Cardiology Review, Mar 2023. URL: https://doi.org/10.15420/ecr.2022.50, doi:10.15420/ecr.2022.50. This article has 14 citations.

26. (nishimiya2023mechanismsofcoronary pages 2-3): Kensuke Nishimiya, Jun Takahashi, Kazuma Oyama, Yasuharu Matsumoto, Satoshi Yasuda, and Hiroaki Shimokawa. Mechanisms of coronary artery spasm. European Cardiology Review, May 2023. URL: https://doi.org/10.15420/ecr.2022.55, doi:10.15420/ecr.2022.55. This article has 18 citations.

27. (jenkins2024vasospasticanginaa pages 1-3): Kenny Jenkins, Graziella Pompei, Nandine Ganzorig, Sarah Brown, John Beltrame, and Vijay Kunadian. Vasospastic angina: a review on diagnostic approach and management. Therapeutic Advances in Cardiovascular Disease, Jan 2024. URL: https://doi.org/10.1177/17539447241230400, doi:10.1177/17539447241230400. This article has 56 citations and is from a peer-reviewed journal.

28. (huang2023invasiveevaluationfor pages 2-3): Jingwen Huang, Rebecca Steinberg, Matthew J Brown, Stéphane Rinfret, and Olga Toleva. Invasive evaluation for coronary vasospasm. US Cardiology Review, Jun 2023. URL: https://doi.org/10.15420/usc.2022.33, doi:10.15420/usc.2022.33. This article has 5 citations.

29. (elsabbagh2024coronaryarteryspasm—risk pages 5-7): Farah El-Sabbagh, Noha M. Mesbah, Dina M Abo-El-Matty, and Tarek A. Abdelaziz. Coronary artery spasm—risk factors and pathophysiological mechanisms. Records of Pharmaceutical and Biomedical Sciences, 8:191-198, May 2024. URL: https://doi.org/10.21608/rpbs.2024.327931.1332, doi:10.21608/rpbs.2024.327931.1332. This article has 0 citations.

30. (gurgoglione2024coronaryspasmtesting pages 19-20): Filippo Luca Gurgoglione, Luigi Vignali, Rocco Antonio Montone, Riccardo Rinaldi, Giorgio Benatti, Emilia Solinas, Antonio Maria Leone, Domenico Galante, Gianluca Campo, Simone Biscaglia, Italo Porto, Stefano Benenati, and Giampaolo Niccoli. Coronary spasm testing with acetylcholine: a powerful tool for a personalized therapy of coronary vasomotor disorders. Life, 14:292, Feb 2024. URL: https://doi.org/10.3390/life14030292, doi:10.3390/life14030292. This article has 16 citations.

31. (nishimiya2023mechanismsofcoronary pages 1-2): Kensuke Nishimiya, Jun Takahashi, Kazuma Oyama, Yasuharu Matsumoto, Satoshi Yasuda, and Hiroaki Shimokawa. Mechanisms of coronary artery spasm. European Cardiology Review, May 2023. URL: https://doi.org/10.15420/ecr.2022.55, doi:10.15420/ecr.2022.55. This article has 18 citations.

32. (gurgoglione2024coronaryspasmtesting media ac042141): Filippo Luca Gurgoglione, Luigi Vignali, Rocco Antonio Montone, Riccardo Rinaldi, Giorgio Benatti, Emilia Solinas, Antonio Maria Leone, Domenico Galante, Gianluca Campo, Simone Biscaglia, Italo Porto, Stefano Benenati, and Giampaolo Niccoli. Coronary spasm testing with acetylcholine: a powerful tool for a personalized therapy of coronary vasomotor disorders. Life, 14:292, Feb 2024. URL: https://doi.org/10.3390/life14030292, doi:10.3390/life14030292. This article has 16 citations.

33. (NCT06415227 chunk 1): Jan J. Piek, MD, PhD. The Impact of Vericiguat on Microvascular Function in Patients with Documented Vasospastic Angina Pectoris. Academisch Medisch Centrum - Universiteit van Amsterdam (AMC-UvA). 2025. ClinicalTrials.gov Identifier: NCT06415227