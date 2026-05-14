---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T11:37:58.038441'
end_time: '2026-05-09T11:45:06.277390'
duration_seconds: 428.24
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ludwig's Angina
  mondo_id: ''
  category: Infectious
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ludwig's Angina
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Ludwig's Angina** covering all of the
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
- **Disease Name:** Ludwig's Angina
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Ludwig's Angina** covering all of the
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


# Ludwig’s Angina (Infectious) — Disease Characteristics Research Report

## 1. Disease information

### 1.1 Concise overview (current understanding)
Ludwig’s angina is a rapidly progressive, potentially life‑threatening cellulitis/infection involving the floor of mouth and upper neck that classically affects the **submandibular, sublingual, and submental spaces**, often bilaterally, and can cause **tongue elevation/displacement** and **acute airway compromise**. (ahmed2025ludwig’sanginain pages 8-11, sahoo2024incidenceofmortality pages 1-2, boynton201612–odontogenic pages 13-14)

Older surgical-pathology descriptions emphasize a **“firm, acute, toxic cellulitis”** in these spaces and highlight that tongue displacement can produce a “sensation of choking and suffocation.” (boynton201612–odontogenic pages 13-14)

### 1.2 Key identifiers (ontology/terminology)
The currently retrieved full texts do **not** provide standardized identifiers (MONDO, MeSH, ICD-10/ICD-11, OMIM, Orphanet) directly; this portion should be curated from external ontology portals (e.g., MONDO browser, MeSH, ICD). This report therefore focuses on evidence-backed clinical characteristics from peer‑reviewed/primary literature. (sahoo2024incidenceofmortality pages 1-2, boynton201612–odontogenic pages 13-14, mahbub2024bacteriologicalstudyand pages 1-2)

### 1.3 Synonyms and alternative names
Commonly used clinical terminology in the literature includes:
- “Ludwig’s angina” (standard eponym) (sahoo2024incidenceofmortality pages 1-2)
- “Diffuse cellulitis of the submandibular space extending to the sublingual space” (definition used in pediatric report/review) (benhoummad2023ludwig’sanginain pages 1-3)

### 1.4 Evidence source type
Evidence synthesized here is largely **aggregated disease-level clinical literature** (retrospective/prospective hospital cohorts and narrative reviews) plus selected case reports for special populations (pediatrics). (mahbub2024bacteriologicalstudyand pages 1-2, benhoummad2023ludwig’sanginain pages 1-3, kumari2024diabetesmellitusand pages 2-4)

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** Ludwig’s angina is usually **odontogenic** (originating from infected mandibular molars or dental infections), with polymicrobial oral flora. (sahoo2024incidenceofmortality pages 1-2, boynton201612–odontogenic pages 13-14, sahoo2024incidenceofmortality pages 5-6)

**Causal chain (high-level):** odontogenic infection → spread along fascial planes into submandibular/sublingual/submental spaces → edema/cellulitis ± abscess/necrotizing infection → tongue elevation/posterior displacement → airway compromise and systemic spread (sepsis/mediastinitis). (sahoo2024incidenceofmortality pages 1-2, boynton201612–odontogenic pages 13-14, sahoo2024incidenceofmortality pages 6-7)

### 2.2 Risk factors
**Diabetes mellitus (DM):** Multiple cohorts show high DM comorbidity among Ludwig’s angina/deep neck infection patients and association with worse clinical course.
- Prospective Ludwig’s angina cohort (India, 2022–2023): **50%** had diabetes mellitus. (kumari2024diabetesmellitusand pages 2-4)
- Prospective Ludwig’s angina cohort (Bangladesh): **25%** had diabetes mellitus. (mahbub2024bacteriologicalstudyand pages 2-4)
- Retrospective Ludwig’s angina cohort (n=17): **50%** had DM; **70.5%** had comorbidities. (sahoo2024incidenceofmortality pages 5-6)
- Population-based cohort (Taiwan; deep neck infection broadly, including Ludwig angina ICD coding in methods): Type 1 DM associated with **adjusted hazard ratio 10.71** for deep neck infection and longer hospitalizations (**9.0 ± 6.2 vs 4.1 ± 2.0 days**). (sahoo2024incidenceofmortality pages 5-6)

**Other host risk factors discussed in clinical series/reviews** include immunocompromise (e.g., HIV/AIDS), malnutrition, chronic kidney disease, cirrhosis, COPD, CAD, pregnancy, and older age. (sahoo2024incidenceofmortality pages 1-2, sahoo2024incidenceofmortality pages 5-6)

**Socioeconomic/oral hygiene factors:** In the Bangladesh cohort, many patients were from poor socioeconomic background (70%), rural areas (70%), and had dental infection (70%). (mahbub2024bacteriologicalstudyand pages 2-4)

### 2.3 Protective factors
Direct protective factors are not explicitly quantified in the retrieved evidence; however, prevention-focused statements emphasize oral hygiene and early dental care to prevent odontogenic infections that precipitate Ludwig’s angina. (mahbub2024bacteriologicalstudyand pages 1-2, ahmed2025ludwig’sanginain pages 8-11)

### 2.4 Gene–environment interactions
No gene–environment interaction evidence specific to Ludwig’s angina was found in the retrieved full texts; the condition is typically **not** described as genetically determined but rather driven by **infection + host comorbidity**. (sahoo2024incidenceofmortality pages 1-2, mahbub2024bacteriologicalstudyand pages 1-2)

## 3. Phenotypes (clinical presentation)

### 3.1 Core signs and symptoms (with cohort statistics)
Common phenotypes include neck/floor-of-mouth swelling, pain, fever, dysphagia, trismus, tongue elevation, drooling, muffled voice, and respiratory distress.

Recent cohort examples:
- India prospective cohort (n=40): pain **80%**, neck swelling **75%**, dysphagia **65%**, trismus **55%**, fever **25%**, respiratory distress **22.5%**. (kumari2024diabetesmellitusand pages 2-4)
- Bangladesh prospective cohort (n=100): floor-of-mouth/neck swelling **100%**, pain/tenderness **100%**, fever **100%**, dysphagia **80%**, trismus **15%**, muffled voice **10%**, respiratory distress **3%**. (mahbub2024bacteriologicalstudyand pages 4-5)
- Somalia retrospective cohort (n=90): submandibular swelling + trismus + tongue elevation + difficulty breathing **52.2%**; fever/toothache/submental swelling **35.6%**. (ahmed2025ludwig’sanginain pages 8-11)

### 3.2 Suggested HPO terms (non-exhaustive)
The following HPO mappings are appropriate for knowledge base structuring (ontology suggestions; not claims of frequency unless paired with above statistics):
- Neck swelling (HP:0000474)
- Facial swelling (HP:0000289)
- Fever (HP:0001945)
- Dysphagia (HP:0002015)
- Trismus (HP:0000210)
- Drooling (HP:0002307)
- Dyspnea/Respiratory distress (HP:0002094)
- Stridor (HP:0001618)
- Muffled voice/Hoarseness (HP:0001609)

### 3.3 Quality of life impact
Although validated QoL instrument scores (EQ‑5D/SF‑36) were not reported in the retrieved texts, the symptom complex (pain, dysphagia, trismus, airway threat) implies acute, severe functional impairment requiring urgent care and often hospitalization/ICU-level monitoring. (sahoo2024incidenceofmortality pages 1-2, sahoo2024incidenceofmortality pages 6-7)

## 4. Genetic / molecular information

### 4.1 Causal genes and pathogenic variants
Ludwig’s angina is not primarily characterized as a monogenic disorder in the retrieved evidence and no causal genes/variants are reported. It is best represented as an **acute polymicrobial infection syndrome** influenced by host comorbidity rather than inherited variants. (sahoo2024incidenceofmortality pages 1-2, mahbub2024bacteriologicalstudyand pages 1-2)

### 4.2 Molecular profiling / omics
No transcriptomic/proteomic/metabolomic profiling studies specific to Ludwig’s angina were identified in the retrieved evidence set. (mahbub2024bacteriologicalstudyand pages 1-2)

## 5. Environmental information

### 5.1 Lifestyle and contextual factors
Poor oral hygiene and delayed dental care are repeatedly implicated as upstream factors increasing odontogenic infection burden, which then precipitates Ludwig’s angina/deep neck infection. (mahbub2024bacteriologicalstudyand pages 2-4, ahmed2025ludwig’sanginain pages 8-11)

### 5.2 Infectious agents
Ludwig’s angina is commonly polymicrobial and derived from oral flora; cohorts report frequent isolation of **viridans streptococci**, **Staphylococcus aureus**, and Gram-negative organisms in some settings.
- Bangladesh cohort: *Streptococcus viridans* **40%**, *S. aureus* **23%**, coagulase‑negative staphylococci **20%**, *Klebsiella* **16%**, *E. coli* **13%**, *Pseudomonas* **12%**, *Proteus* **11%**, and mixed organisms **30%** (note: multiple isolates possible). (mahbub2024bacteriologicalstudyand pages 4-5)
- India cohort: *S. viridans* **22.5%**, *S. aureus* **12.5%**, *E. coli* **7.5%**, *Klebsiella* **5%**; “no growth” **52.5%** (likely reflecting pre-treatment/collection limits). (kumari2024diabetesmellitusand pages 2-4)

## 6. Mechanism / pathophysiology

### 6.1 Anatomic–pathophysiologic mechanism (causal chain)
A consistent mechanistic explanation is:
1) odontogenic infection (often mandibular molar) spreads through lingual cortical bone and fascial planes (relationship to mylohyoid region) (sahoo2024incidenceofmortality pages 5-6)
2) cellulitis/edema involves submandibular space and spreads to sublingual/submental spaces, frequently bilaterally (sahoo2024incidenceofmortality pages 1-2, boynton201612–odontogenic pages 13-14)
3) floor-of-mouth induration and edema displace tongue upward/backward → airway compromise (boynton201612–odontogenic pages 13-14, sahoo2024incidenceofmortality pages 5-6)
4) systemic extension may cause sepsis, necrotizing fasciitis, and descending mediastinitis. (sahoo2024incidenceofmortality pages 5-6, mahbub2024bacteriologicalstudyand pages 4-5)

### 6.2 Immune involvement and host factors
Diabetes is repeatedly discussed as contributing to susceptibility and more severe course. The comorbidity burden is emphasized in a 2024 retrospective series where all deaths occurred in patients with comorbidity. (sahoo2024incidenceofmortality pages 1-2)

### 6.3 Suggested GO biological process terms (mechanism structuring)
Ontology suggestions for mechanistic annotation:
- GO:0006954 inflammatory response
- GO:0002682 regulation of immune system process
- GO:0009617 response to bacterium
- GO:0009405 pathogenesis
- GO:0009408 response to heat (fever physiology)

### 6.4 Suggested cell types (CL) implicated
Ontology suggestions:
- Neutrophil (CL:0000775) (consistent with inflammatory marker emphasis and neutrophil predictors in deep neck abscess airway risk modeling) (sahoo2024incidenceofmortality pages 5-6)
- Macrophage (CL:0000235)
- Oral epithelial cell (CL:0000066)

## 7. Anatomical structures affected

### 7.1 Primary sites
Core spaces: submandibular, sublingual, submental spaces (floor of mouth). (ahmed2025ludwig’sanginain pages 8-11, boynton201612–odontogenic pages 13-14)

Suggested UBERON terms (ontology suggestions):
- Floor of mouth (UBERON:0003679)
- Submandibular region (UBERON concept mapping may be required)
- Tongue (UBERON:0001723)

### 7.2 Secondary involvement (complications)
Reported complications include necrotizing fasciitis, septicemia/sepsis, mediastinitis, and airway obstruction. (ahmed2025ludwig’sanginain pages 8-11, mahbub2024bacteriologicalstudyand pages 4-5)

## 8. Temporal development

### 8.1 Onset and course
Ludwig’s angina is typically **acute and rapidly progressive**; delays in presentation are common in some settings (e.g., 77.8% waiting 5–7 days in a Somali ED cohort), which can increase complication risk. (ahmed2025ludwig’sanginain pages 8-11)

### 8.2 Disease stages (practical clinical staging)
Evidence supports a practical progression: odontogenic infection → cellulitis/edema → airway-threatening floor-of-mouth swelling ± abscess/necrotizing infection → systemic complications. (boynton201612–odontogenic pages 13-14, sahoo2024incidenceofmortality pages 6-7)

## 9. Inheritance and population

### 9.1 Epidemiology
High-quality population incidence/prevalence estimates for Ludwig’s angina specifically were not captured in the retrieved texts. Available evidence is predominantly hospital-based series.

Examples of reported demographics:
- Somalia ED cohort: 77.8% male; mean age 39.1 years. (ahmed2025ludwig’sanginaina pages 5-7)
- Bangladesh cohort: 60% male; most common age group 31–45 years (42%). (mahbub2024bacteriologicalstudyand pages 2-4)

## 10. Diagnostics

### 10.1 Clinical diagnosis and labs
Diagnosis is largely clinical, supported by inflammatory markers (WBC, CRP) and cultures where feasible. Pediatric case review notes hyperleukocytosis and very high CRP (CRP=300 in the index case). (benhoummad2023ludwig’sanginain pages 1-3)

### 10.2 Imaging
A 2024 retrospective Ludwig’s angina series reports routine use of **contrast-enhanced CT (CECT)** to define spread. (sahoo2024incidenceofmortality pages 6-7)
Radiographic work-up may begin with dental imaging (OPG) to identify source and chest X‑ray to evaluate thoracic spread. (sahoo2024incidenceofmortality pages 5-6)

### 10.3 Differential diagnosis
Conditions that may mimic floor-of-mouth swelling include **angioneurotic (angioedema) edema** and **sublingual hematoma**, which are explicitly listed as differential diagnoses in a 2024 retrospective report. (sahoo2024incidenceofmortality pages 5-6)

## 11. Outcomes / prognosis

### 11.1 Mortality and severe complications
Mortality varies substantially by setting and comorbidity burden.
- India prospective cohort (n=40): death **7.5%** (3 deaths, attributed to septicemia). (kumari2024diabetesmellitusand pages 2-4)
- Bangladesh cohort (n=100): deaths reported (2 patients died due to mediastinitis in the discussion of complications). (mahbub2024bacteriologicalstudyand pages 4-5)
- Retrospective series (n=17): mortality **23.5%**; all deaths occurred with comorbidity. (sahoo2024incidenceofmortality pages 1-2)
- Somalia ED cohort (n=90): **no mortality** reported, despite **48.9%** complication rate. (ahmed2025ludwig’sanginain pages 8-11)

Complication rates can be high:
- Somalia cohort: any complication **48.9%**; septicemia **36.7%**; necrotizing fasciitis **5.5%**; DIC **3.3%**; laryngeal spasm **3.3%**. (ahmed2025ludwig’sanginain pages 8-11)
- Bangladesh cohort: necrotizing fasciitis **8%**; mediastinitis and septicemia are reported complications (percentages reported in text). (mahbub2024bacteriologicalstudyand pages 4-5)

### 11.2 Prognostic factors (expert synthesis grounded in evidence)
Across series, **comorbidities (especially diabetes)** and delayed presentation are repeatedly linked to longer hospitalization and worse outcomes, and multispace disease/airway compromise increases intervention needs. (sahoo2024incidenceofmortality pages 5-6, ahmed2025ludwig’sanginaina pages 5-7, sahoo2024incidenceofmortality pages 1-2)

## 12. Treatment

### 12.1 Current applications and real-world implementation (core algorithm)
Evidence from recent cohorts emphasizes a consistent emergency-management triad:
1) **Airway management** (monitoring, oxygen, escalation to intubation or tracheostomy) (sahoo2024incidenceofmortality pages 6-7)
2) **Broad-spectrum IV antibiotics** with aerobic + anaerobic coverage, tailored to cultures when possible (sahoo2024incidenceofmortality pages 6-7, mahbub2024bacteriologicalstudyand pages 1-2)
3) **Early surgical decompression/drainage and source control (e.g., extraction/drainage)** when indicated. (sahoo2024incidenceofmortality pages 6-7, kumari2024diabetesmellitusand pages 4-5)

A 2024 retrospective series provides quantitative airway management data: **oro-tracheal intubation 88.2%** and **tracheostomy 11.2%**. (sahoo2024incidenceofmortality pages 6-7)
A 2024 prospective series reported **emergency tracheostomy 12.5%** in patients presenting with respiratory distress/stridor. (kumari2024diabetesmellitusand pages 4-5)

### 12.2 Antibiotics and susceptibility (recent microbiology/statistics)
The Bangladesh cohort provides organism-specific susceptibility counts and overall statements including that the “most effective antibiotic was Ceftriaxone (65%)” and ceftazidime 58% (as reported in the results and Table VI). (mahbub2024bacteriologicalstudyand pages 4-5, mahbub2024bacteriologicalstudyand media 459caceb)

### 12.3 MAXO (Medical Action Ontology) suggestions
Ontology suggestions for intervention annotation:
- Airway management / tracheal intubation / tracheostomy (MAXO term mapping required)
- Surgical drainage of abscess / surgical decompression (MAXO mapping required)
- Antibacterial therapy (MAXO mapping required)
- Tooth extraction / dental source control (MAXO mapping required)

## 13. Prevention

Primary prevention centers on preventing odontogenic infection progression via **oral hygiene, regular dental evaluation, and early treatment of dental infections**, which is explicitly recommended in cohort conclusions. (ahmed2025ludwig’sanginain pages 8-11, mahbub2024bacteriologicalstudyand pages 1-2)

Secondary/tertiary prevention in clinical practice includes early recognition, early imaging when needed, and early airway protection to prevent catastrophic airway obstruction and systemic spread. (sahoo2024incidenceofmortality pages 6-7)

## 14. Other species / natural disease
No evidence in the retrieved texts describes Ludwig’s angina as a naturally occurring disease entity in non-human species, or zoonotic transmission; this section is currently **not evidenced** in the available corpus. (sahoo2024incidenceofmortality pages 1-2)

## 15. Model organisms
No animal model or experimental model organism evidence specific to Ludwig’s angina was identified in the retrieved texts; most mechanistic and therapeutic understanding is derived from **human clinical series** of odontogenic and deep neck space infections. (mahbub2024bacteriologicalstudyand pages 1-2)

---

## Recent developments (prioritizing 2023–2024) — synthesis
The strongest “recent” (2023–2024) evidence retrieved here consists of prospective/retrospective cohorts in diverse health systems that quantify:
- High burden of **DM and other comorbidities** among cases and association with longer stays/outcomes. (kumari2024diabetesmellitusand pages 2-4, sahoo2024incidenceofmortality pages 5-6)
- Persistent **polymicrobial** patterns with site-specific Gram-negative representation and substantial “no growth” proportions, emphasizing sampling/treatment effects and the need for empiric broad coverage. (mahbub2024bacteriologicalstudyand pages 4-5, kumari2024diabetesmellitusand pages 2-4)
- Real-world airway intervention rates (intubation vs tracheostomy) and continued emphasis on early decompression plus antibiotics. (sahoo2024incidenceofmortality pages 6-7, kumari2024diabetesmellitusand pages 4-5)

## Key quantitative evidence table
The following table consolidates the most actionable statistics and management details from the retrieved studies.

| Study (first author, year) | Design/Setting | N | Key etiologies/risk factors (with %) | Key clinical features (with % if available) | Microbiology findings | Interventions (airway/surgery/antibiotics) | Outcomes/complications (with %) | URL/DOI | Publication date |
|---|---|---:|---|---|---|---|---|---|---|
| Kumari, 2024 | Prospective study; ENT department, Government Medical College, Amritsar, India | 40 | Dental infection 85%; tooth extraction 10%; diabetes mellitus 50%; HIV/HCV 15% (kumari2024diabetesmellitusand pages 2-4, kumari2024diabetesmellitusand pages 4-5) | Pain 80%; neck swelling 75%; dysphagia 65%; trismus 55%; fever 25%; respiratory distress 22.5% (kumari2024diabetesmellitusand pages 2-4) | *Streptococcus viridans* 22.5%; *Staphylococcus aureus* 12.5%; *E. coli* 7.5%; *Klebsiella* 5%; no growth 52.5% (kumari2024diabetesmellitusand pages 2-4, kumari2024diabetesmellitusand pages 4-5) | Surgical + medical management 90%; medical only 10%; emergency tracheostomy 12.5%; antibiotics based on culture sensitivity (kumari2024diabetesmellitusand pages 4-5) | Necrotizing fasciitis 5%; peritonsillar abscess 2.5%; respiratory distress/stridor 22.5%; death 7.5%; diabetic hospital stay ~10 days vs 5-7 days in non-diabetics (kumari2024diabetesmellitusand pages 2-4, kumari2024diabetesmellitusand pages 4-5) | https://doi.org/10.18203/2320-6012.ijrms20241233 | Apr 2024 |
| Mahbub, 2024 | Prospective observational study; Dhaka Medical College Hospital/ICDDR,B, Bangladesh | 100 | Dental infection 70%; tooth extraction 10%; diabetes mellitus 25%; rural residence 70%; poor socioeconomic status 70% (mahbub2024bacteriologicalstudyand pages 1-2, mahbub2024bacteriologicalstudyand pages 2-4, mahbub2024bacteriologicalstudyand pages 4-5) | Floor-of-mouth and neck swelling 100%; pain/tenderness 100%; fever 100%; dysphagia 80%; trismus 15%; foul smell 24%; respiratory distress 3%; muffled voice 10% (mahbub2024bacteriologicalstudyand pages 2-4, mahbub2024bacteriologicalstudyand pages 4-5) | *Streptococcus viridans* 40%; *S. aureus* 23%; coagulase-negative staphylococci 20%; *Klebsiella* 16%; *E. coli* 13%; *Pseudomonas* 12%; *Proteus* 11%; mixed organisms 30%; no organism 5% (mahbub2024bacteriologicalstudyand pages 4-5, mahbub2024bacteriologicalstudyand media 024e80f3, mahbub2024bacteriologicalstudyand media 459caceb) | Incision and drainage performed for included cases; empiric IV penicillin G/clindamycin/metronidazole discussed; ceftriaxone most effective antibiotic 65%; ceftazidime 58%; ciprofloxacin 56% (mahbub2024bacteriologicalstudyand pages 1-2, mahbub2024bacteriologicalstudyand pages 2-4, mahbub2024bacteriologicalstudyand pages 4-5, mahbub2024bacteriologicalstudyand media 459caceb) | Necrotizing fasciitis 8%; septicemia 7%; mediastinitis 6%; death 2% (2 patients, due to mediastinitis); discharged within 1-2 weeks 36% (mahbub2024bacteriologicalstudyand pages 4-5) | https://doi.org/10.3329/mumcj.v6i2.71369 | Feb 2024 |
| Sahoo, 2024 | Retrospective study; maxillofacial/oral surgery setting | 17 | Comorbidities 70.5%; diabetes mellitus 50%; all patients had infected lower molar source; risk factors discussed: malnutrition, immunocompromise, old age, obesity, pregnancy, CKD, cirrhosis, COPD, CAD (sahoo2024incidenceofmortality pages 1-2, sahoo2024incidenceofmortality pages 5-6) | Painful neck swelling; drooling; tooth pain; dysphagia; shortness of breath; fever; trismus; muffled voice; impending airway crisis signs include cyanosis/stridor (percentages NR) (sahoo2024incidenceofmortality pages 5-6) | Polymicrobial; native streptococci, staphylococci, *Bacteroides*, mixed aerobic/anaerobic oral flora (sahoo2024incidenceofmortality pages 1-2) | Oro-tracheal intubation 88.2%; tracheostomy 11.2%; CECT for all cases; OPG and chest X-ray recommended; institutional empiric regimen ceftriaxone-sulbactam + amikacin + metronidazole; early decompression mainstay (sahoo2024incidenceofmortality pages 1-2, sahoo2024incidenceofmortality pages 5-6, sahoo2024incidenceofmortality pages 6-7) | Mortality 23.5%; all deaths had comorbidity; necrotizing fasciitis 29.4% with 100% recovery in that subgroup; historical overall mortality cited as 0.3% in a 5,855-patient representative study; cervical necrotizing fasciitis mortality rises to 41% with descending necrotizing mediastinitis and 64% with sepsis (sahoo2024incidenceofmortality pages 5-6, sahoo2024incidenceofmortality pages 1-2, sahoo2024incidenceofmortality pages 6-7) | https://doi.org/10.1007/s12663-024-02116-5 | Feb 2024 |
| Benhoummad, 2023 | Case report and literature review; pediatric emergency/ENT | 1 | Pediatric case; no dental/systemic etiology in index case; literature notes adult cases usually secondary to oral infections (benhoummad2023ludwig’sanginain pages 1-3) | Firm submental/submandibular swelling; pain; fever; respiratory discomfort in supine position; no dysphagia/respiratory distress initially; hyperleukocytosis; CRP 300 (benhoummad2023ludwig’sanginain pages 1-3) | Gram-positive cocci in chains; culture grew *Staphylococcus aureus* (benhoummad2023ludwig’sanginain pages 1-3) | Percutaneous drainage of 15 mL pus; broad-spectrum IV antibiotics; wound care; airway control emphasized in review (benhoummad2023ludwig’sanginain pages 1-3) | Clinical and biological improvement; discharged after 7 days; no complication at 6-month follow-up (benhoummad2023ludwig’sanginain pages 1-3) | https://doi.org/10.1186/s43163-023-00431-1 | Apr 2023 |
| Ahmed, 2025 | Retrospective emergency department study; Mogadishu Somali Turkey Training and Research Hospital, Somalia | 90 | Odontogenic infection 65.5%; periodontal abscess 34.4%; post-extraction abscess 21.1%; dental caries 16.7%; diabetes mellitus 5.6%; severe anaemia 13.3%; chronic liver disease 4.4%; no underlying conditions 41.1%; symptom delay 5-7 days in 77.8% (ahmed2025ludwig’sanginain pages 5-8, ahmed2025ludwig’sanginain pages 8-11, ahmed2025ludwig’sanginaina pages 5-7) | Submandibular swelling, trismus, tongue elevation, difficulty breathing 52.2%; fever/toothache/submental swelling 35.6%; bilateral swelling 12.2% (ahmed2025ludwig’sanginain pages 8-11) | Species breakdown NR in available excerpt (ahmed2025ludwig’sanginain pages 8-11) | Airway support for all (oropharyngeal airway + intranasal oxygen); ceftriaxone + metronidazole empirically, then tailored; surgical decompression 38.9%; incision and drainage 14.4%; antibiotics/targeted therapy 46.7%; source removal in 53.3% of operated cases; ICU 4.4% (ahmed2025ludwig’sanginain pages 5-8, ahmed2025ludwig’sanginaina pages 5-7) | Complications 48.9%; septicemia 36.7%; sepsis ~30%; necrotizing fasciitis 5.5-5.6%; DIC 3.3%; laryngeal spasm 3.3%; no mortality; hospital stay 3-5 days in 52.3% (ahmed2025ludwig’sanginain pages 5-8, ahmed2025ludwig’sanginain pages 8-11, ahmed2025ludwig’sanginaina pages 5-7) | https://doi.org/10.21203/rs.3.rs-7314800/v1 | Aug 2025 |
| Chang, 2018 | Nationwide population-based cohort study; Taiwan NHIRD; deep neck infection risk in T1DM | 5,741 T1DM vs 22,964 matched controls | Type 1 diabetes mellitus associated with higher DNI risk; adjusted hazard ratio 10.71 (95% CI 6.02-19.05) (sahoo2024incidenceofmortality pages 5-6) | NR for Ludwig-specific presentation in excerpt | NR | Therapeutic methods did not differ significantly between T1DM and non-DM DNI cohorts (sahoo2024incidenceofmortality pages 5-6) | Longer hospitalization for DNI in T1DM: 9.0 ± 6.2 vs 4.1 ± 2.0 days; younger age at DNI in T1DM (sahoo2024incidenceofmortality pages 5-6) | https://doi.org/10.3390/jcm7110385 | Oct 2018 |
| Lin, 2021 | Multicenter retrospective cohort study; 9 hospitals, Guangdong Province; deep neck space abscess airway-risk model | 440 | Predictors of airway management: multispace involvement OR 6.42; gas formation OR 4.95; dyspnea OR 10.35; neutrophil percentage OR 1.10; platelet/lymphocyte ratio OR 1.01; albumin OR 0.86; diabetes noted in cohort characteristics (sahoo2024incidenceofmortality pages 5-6) | Dyspnea used as predictor; other Ludwig-specific symptom percentages NR in excerpt | NR | Outcome modeled was need for airway management (intubation/tracheostomy); internal validation AUC 0.951, external AUC 0.947 (sahoo2024incidenceofmortality pages 5-6) | 60/363 in training cohort and 13/77 in validation cohort required airway management (sahoo2024incidenceofmortality pages 5-6) | https://doi.org/10.1186/s40560-021-00554-8 | May 2021 |
| Kataria, 2015 | Retrospective study of deep neck space infections | 76 | Odontogenic infection 34.21%; diabetes comorbidity 10.52%; rural background common; poor oral hygiene/smoking/chewing tobacco highlighted (sahoo2024incidenceofmortality pages 5-6) | Neck pain 89.47%; Ludwig's angina was the most common presentation 28.94% (sahoo2024incidenceofmortality pages 5-6) | Streptococcus/Staphylococcus in 50% of cases (sahoo2024incidenceofmortality pages 5-6) | Surgical intervention 89.47%; emergency tracheotomy 5.26%; IV antibiotics recommended for all (sahoo2024incidenceofmortality pages 5-6) | Airway obstruction, jugular vein thrombosis, and sepsis noted as DNSI complications (sahoo2024incidenceofmortality pages 5-6) | https://doi.org/10.22038/ijorl.2015.4520 | Jul 2015 |


*Table: This table compiles the main quantitative findings and clinical takeaways for Ludwig’s angina from the currently available evidence in the conversation. It highlights etiology, risk factors, microbiology, interventions, and outcomes to support rapid synthesis for a disease knowledge base.*

## Visual evidence from recent study tables
Cropped tables from the 2024 Bangladesh prospective study show bacterial isolate distributions and antibiotic sensitivity counts (Tables IV and VI). (mahbub2024bacteriologicalstudyand media 024e80f3, mahbub2024bacteriologicalstudyand media 459caceb)

---

## Abstract-supported quotes (selected)
- Definition/anatomy: Ludwig’s angina in a pediatric report is described as “a diffuse cellulitis in the sub-mandibular space, which extends to the sublingual space.” (benhoummad2023ludwig’sanginain pages 1-3)
- Cohort microbiology/antibiogram relevance: “The knowledge of the local pattern of infection and antibacterial sensitivity in Ludwig’s angina is essential to enable efficacious treatment for it.” (mahbub2024bacteriologicalstudyand pages 1-2)

---

## Limitations of this report
- Standard identifiers (MONDO/MeSH/ICD/Orphanet/OMIM) and PMID-level indexing were not available in the retrieved full texts; URLs and DOIs are provided where present in the evidence, and identifier curation should be performed using dedicated ontology resources. (sahoo2024incidenceofmortality pages 1-2, mahbub2024bacteriologicalstudyand pages 1-2)
- Some data (e.g., incidence/prevalence) are not well represented in the retrieved set and may require targeted epidemiology database queries beyond the current corpus.


References

1. (ahmed2025ludwig’sanginain pages 8-11): Abdullahi Ahmed Ahmed, Ismail Mohamoud Abdullahi, Nasteho Mohamed Sheikh Omar, Abdishakur Mohamed Abdirahman, Resul Nusretoğlu, and Sahra Ali Yusuf. Ludwig’s angina in the emergency department: epidemiology, diagnosis, and outcomes: a retrospective study in somalia. Unknown journal, Aug 2025. URL: https://doi.org/10.21203/rs.3.rs-7314800/v1, doi:10.21203/rs.3.rs-7314800/v1.

2. (sahoo2024incidenceofmortality pages 1-2): N. K. Sahoo, Ankur Thakral, Swati Pandey, Himani Vaswani, Sahil Vashisht, and Isha Maheshwari. Incidence of mortality and its relation to comorbidity in ludwig's angina: a retrospective study. Journal of maxillofacial and oral surgery, 23 3:581-588, Feb 2024. URL: https://doi.org/10.1007/s12663-024-02116-5, doi:10.1007/s12663-024-02116-5. This article has 3 citations.

3. (boynton201612–odontogenic pages 13-14): Tyler T. Boynton, Elie M. Ferneini, and Morton H. Goldberg. 12 – odontogenic infections of the fascial spaces. ArXiv, pages 203-221, Jan 2016. URL: https://doi.org/10.1016/b978-0-323-28945-0.00012-0, doi:10.1016/b978-0-323-28945-0.00012-0. This article has 7 citations.

4. (mahbub2024bacteriologicalstudyand pages 1-2): AHM Rashid E Mahbub, Abdullah Al Mamun, Rokhsana Sarmin, Syed Sanaul Islam, Rashedul Islam, AHM Noor E As Sayeed, and Md Asif Anowar. Bacteriological study and antibacterial susceptibility in ludwig’s angina in a tertiary level hospital in dhaka, bangladesh. Mugda Medical College Journal, 6:71-76, Feb 2024. URL: https://doi.org/10.3329/mumcj.v6i2.71369, doi:10.3329/mumcj.v6i2.71369. This article has 0 citations.

5. (benhoummad2023ludwig’sanginain pages 1-3): Othmane Benhoummad, Kaoutar Cherrabi, Najib El Orfi, Zineb Mortaji, and Mehdi El Fakiri. Ludwig’s angina in a child: a case report and literature review. The Egyptian Journal of Otolaryngology, Apr 2023. URL: https://doi.org/10.1186/s43163-023-00431-1, doi:10.1186/s43163-023-00431-1. This article has 5 citations.

6. (kumari2024diabetesmellitusand pages 2-4): Anjana Kumari, Arvinder Singh Maan, Satinderpal Singh, and Simerpreet Kaur Saran. Diabetes mellitus and odontogenic infections: a life threatening combination in ludwig's angina. International Journal of Research in Medical Sciences, 12:1502-1506, Apr 2024. URL: https://doi.org/10.18203/2320-6012.ijrms20241233, doi:10.18203/2320-6012.ijrms20241233. This article has 4 citations.

7. (sahoo2024incidenceofmortality pages 5-6): N. K. Sahoo, Ankur Thakral, Swati Pandey, Himani Vaswani, Sahil Vashisht, and Isha Maheshwari. Incidence of mortality and its relation to comorbidity in ludwig's angina: a retrospective study. Journal of maxillofacial and oral surgery, 23 3:581-588, Feb 2024. URL: https://doi.org/10.1007/s12663-024-02116-5, doi:10.1007/s12663-024-02116-5. This article has 3 citations.

8. (sahoo2024incidenceofmortality pages 6-7): N. K. Sahoo, Ankur Thakral, Swati Pandey, Himani Vaswani, Sahil Vashisht, and Isha Maheshwari. Incidence of mortality and its relation to comorbidity in ludwig's angina: a retrospective study. Journal of maxillofacial and oral surgery, 23 3:581-588, Feb 2024. URL: https://doi.org/10.1007/s12663-024-02116-5, doi:10.1007/s12663-024-02116-5. This article has 3 citations.

9. (mahbub2024bacteriologicalstudyand pages 2-4): AHM Rashid E Mahbub, Abdullah Al Mamun, Rokhsana Sarmin, Syed Sanaul Islam, Rashedul Islam, AHM Noor E As Sayeed, and Md Asif Anowar. Bacteriological study and antibacterial susceptibility in ludwig’s angina in a tertiary level hospital in dhaka, bangladesh. Mugda Medical College Journal, 6:71-76, Feb 2024. URL: https://doi.org/10.3329/mumcj.v6i2.71369, doi:10.3329/mumcj.v6i2.71369. This article has 0 citations.

10. (mahbub2024bacteriologicalstudyand pages 4-5): AHM Rashid E Mahbub, Abdullah Al Mamun, Rokhsana Sarmin, Syed Sanaul Islam, Rashedul Islam, AHM Noor E As Sayeed, and Md Asif Anowar. Bacteriological study and antibacterial susceptibility in ludwig’s angina in a tertiary level hospital in dhaka, bangladesh. Mugda Medical College Journal, 6:71-76, Feb 2024. URL: https://doi.org/10.3329/mumcj.v6i2.71369, doi:10.3329/mumcj.v6i2.71369. This article has 0 citations.

11. (ahmed2025ludwig’sanginaina pages 5-7): Abdullahi Ahmed Ahmed, Ismail Mohamoud Abdullahi, Hussein Hassan Mohamud, Nasteho Mohamed Sheikh Omar, Abdishakur Mohamed Abdirahman, Resul Nusretoğlu, and Sahra Ali Yusuf. Ludwig’s angina in somalia: clinical characteristics, management, and outcomes from a tertiary emergency department retrospective study. first report of ludwig’s angina in somalia. Unknown journal, Dec 2025. URL: https://doi.org/10.21203/rs.3.rs-8062782/v1, doi:10.21203/rs.3.rs-8062782/v1.

12. (kumari2024diabetesmellitusand pages 4-5): Anjana Kumari, Arvinder Singh Maan, Satinderpal Singh, and Simerpreet Kaur Saran. Diabetes mellitus and odontogenic infections: a life threatening combination in ludwig's angina. International Journal of Research in Medical Sciences, 12:1502-1506, Apr 2024. URL: https://doi.org/10.18203/2320-6012.ijrms20241233, doi:10.18203/2320-6012.ijrms20241233. This article has 4 citations.

13. (mahbub2024bacteriologicalstudyand media 459caceb): AHM Rashid E Mahbub, Abdullah Al Mamun, Rokhsana Sarmin, Syed Sanaul Islam, Rashedul Islam, AHM Noor E As Sayeed, and Md Asif Anowar. Bacteriological study and antibacterial susceptibility in ludwig’s angina in a tertiary level hospital in dhaka, bangladesh. Mugda Medical College Journal, 6:71-76, Feb 2024. URL: https://doi.org/10.3329/mumcj.v6i2.71369, doi:10.3329/mumcj.v6i2.71369. This article has 0 citations.

14. (mahbub2024bacteriologicalstudyand media 024e80f3): AHM Rashid E Mahbub, Abdullah Al Mamun, Rokhsana Sarmin, Syed Sanaul Islam, Rashedul Islam, AHM Noor E As Sayeed, and Md Asif Anowar. Bacteriological study and antibacterial susceptibility in ludwig’s angina in a tertiary level hospital in dhaka, bangladesh. Mugda Medical College Journal, 6:71-76, Feb 2024. URL: https://doi.org/10.3329/mumcj.v6i2.71369, doi:10.3329/mumcj.v6i2.71369. This article has 0 citations.

15. (ahmed2025ludwig’sanginain pages 5-8): Abdullahi Ahmed Ahmed, Ismail Mohamoud Abdullahi, Nasteho Mohamed Sheikh Omar, Abdishakur Mohamed Abdirahman, Resul Nusretoğlu, and Sahra Ali Yusuf. Ludwig’s angina in the emergency department: epidemiology, diagnosis, and outcomes: a retrospective study in somalia. Unknown journal, Aug 2025. URL: https://doi.org/10.21203/rs.3.rs-7314800/v1, doi:10.21203/rs.3.rs-7314800/v1.
