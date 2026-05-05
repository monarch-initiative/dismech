---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T17:32:49.126493'
end_time: '2026-04-25T17:44:48.771122'
duration_seconds: 719.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cushing's Syndrome
  mondo_id: MONDO:0018912
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cushing's Syndrome
- **MONDO ID:** MONDO:0018912 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cushing's Syndrome** covering all of the
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
- **Disease Name:** Cushing's Syndrome
- **MONDO ID:** MONDO:0018912 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cushing's Syndrome** covering all of the
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


# Comprehensive Research Report: Cushing’s Syndrome (MONDO:0018912)

## Executive overview
Cushing’s syndrome (CS) is **prolonged cortisol excess** that is not a physiologic response to stress. The most common cause overall is **exogenous glucocorticoid exposure**, but clinically critical disease also occurs from **endogenous tumor-driven hypercortisolism**. Endogenous CS is rare yet high-impact, with estimated incidence **~2–8 per million per year**. (reincke2023cushingsyndromea pages 1-2, reincke2023cushingsyndromea pages 2-3)

---

## 1. Disease Information
### 1.1 Definition and current understanding
Cushing’s syndrome is defined as a **“prolonged increase in plasma cortisol levels that is not due to a physiological etiology.”** (Reincke & Fleseriu, *JAMA*, published **2023-07**, URL: https://doi.org/10.1001/jama.2023.11305) (reincke2023cushingsyndromea pages 1-2)

### 1.2 Key identifiers and synonyms
Only identifiers explicitly available in the retrieved evidence are included here.

| Concept | Definition (1-line) | Common synonyms | Key codes/IDs | Key citation |
|---|---|---|---|---|
| Cushing's syndrome | Prolonged increase in plasma cortisol not due to a physiological etiology; overall most commonly caused by exogenous glucocorticoid exposure. | CS; hypercortisolism; Cushing syndrome | MONDO:0018912 | (reincke2023cushingsyndromea pages 1-2, reincke2023cushingsyndromea pages 2-3) |
| Endogenous Cushing's syndrome | Cushing's syndrome caused by endogenous overproduction of cortisol rather than exogenous steroids. | endogenous CS; endogenous hypercortisolism | NA | (reincke2023cushingsyndromea pages 1-2, m.c.2025hypertensionandcushing’s pages 1-2) |
| Cushing disease | ACTH-dependent endogenous Cushing syndrome caused by an ACTH-secreting pituitary adenoma/corticotrophinoma. | pituitary Cushing; pituitary ACTH-dependent Cushing syndrome; CD | NA | (reincke2023cushingsyndromea pages 1-2, loughrey2024insightsonepidemiology pages 1-2) |
| Ectopic ACTH syndrome | ACTH-dependent Cushing syndrome caused by non-pituitary ACTH-secreting tumors. | ectopic Cushing syndrome; ectopic ACTH-dependent Cushing syndrome; EAS | NA | (reincke2023cushingsyndromea pages 1-2, reincke2023cushingsyndromea pages 2-3) |
| Adrenal Cushing | ACTH-independent Cushing syndrome due to autonomous adrenal cortisol production from adrenal tumors or hyperplasia. | adrenal Cushing syndrome; ACTH-independent Cushing syndrome; adrenal hypercortisolism | NA | (reincke2023cushingsyndromea pages 1-2, reincke2023cushingsyndromea pages 2-3) |


*Table: This table summarizes the core disease concept and major clinical subtypes of Cushing's syndrome, with concise definitions, common synonyms, and only those IDs explicitly supported in the available evidence. It is useful for knowledge-base normalization and concept mapping without introducing unsupported coding terms.*

**Notes on missing identifiers:** ICD-10/ICD-11 codes, MeSH IDs, OMIM/Orphanet identifiers were not extractable from the retrieved full-text evidence in this run and are therefore not reported.

### 1.3 Evidence source types
The synthesis below draws predominantly from:
- Aggregated disease-level resources (high-citation review and cohorts) (reincke2023cushingsyndromea pages 1-2, loughrey2024insightsonepidemiology pages 1-2)
- Registry/cohort observational studies (human clinical) (loughrey2024insightsonepidemiology pages 1-2)
- Interventional and real-world pharmacotherapy studies (human clinical) (gadelha2023longtermefficacyand pages 1-2, feelders2023longtermefficacyand pages 1-2)
- Systematic review evidence for iatrogenic pediatric CS (human clinical) (abdalla2024cushingssyndromeand pages 1-2)

---

## 2. Etiology
### 2.1 Primary causes
**Endogenous CS etiologic distribution (current clinical framing):**
- **ACTH-dependent (pituitary) Cushing disease:** ~60–70% of endogenous CS (reincke2023cushingsyndromea pages 1-2, reincke2023cushingsyndromea pages 2-3)
- **ACTH-independent adrenal cortisol production:** ~20–30% (reincke2023cushingsyndromea pages 2-3)
- **Ectopic ACTH-dependent CS:** ~6–10% (reincke2023cushingsyndromea pages 2-3)

**Key mechanistic statement (authoritative review):** evaluation “begins with **ruling out exogenous steroid use**.” (reincke2023cushingsyndromea pages 1-2)

### 2.2 Risk factors
**Clinical risk enrichment groups (examples):**
In the context of hypertension work-up, a targeted screening phenotype includes **younger age (<40 years), rapidly evolving hypertension, adrenal adenomas/incidentalomas, or pituitary lesions**. (De Martino et al., *J Endocrinol Invest*, published **2025-03**, URL: https://doi.org/10.1007/s40618-024-02453-9) (m.c.2025hypertensionandcushing’s pages 1-2)

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved evidence for CS.

### 2.4 Gene–environment or drug–drug interactions
A dominant “environmental” driver of CS is **exogenous glucocorticoid exposure**, including non-oral routes; prevention therefore includes correct prescribing/monitoring and avoiding unrecognized exposure sources. (reincke2023cushingsyndromea pages 1-2, abdalla2024cushingssyndromeand pages 1-2)

---

## 3. Phenotypes
### 3.1 Core phenotype pattern
CS presents with a **multisystem phenotype** combining:
- **Cutaneous findings** (e.g., facial plethora, easy bruising, purple striae) (reincke2023cushingsyndromea pages 1-2)
- **Cardiometabolic findings** (e.g., hypertension, hyperglycemia/diabetes, dyslipidemia, central adiposity) (reincke2023cushingsyndromea pages 1-2, reincke2023cushingsyndromea pages 4-5)
- **Neuropsychiatric manifestations** (neurocognitive changes, mood disorders) (reincke2023cushingsyndromea pages 1-2, reincke2023cushingsyndromea pages 3-4)
- **Muscle/bone catabolism** (proximal weakness, osteopenia/osteoporosis) (reincke2023cushingsyndromea pages 3-4)

### 3.2 Phenotype frequencies and HPO mapping
The 2023 *JAMA* review reports a range of symptom frequencies (e.g., weight gain 70–95%, hypertension 60–90%, depression 50–80%, hirsutism 50–75%; purple striae <50%), emphasizing that **no single symptom is pathognomonic**. (reincke2023cushingsyndromea pages 4-5, reincke2023cushingsyndromea pages 3-4)

| Feature (plain language) | Suggested HPO term (ID and label) | Frequency/notes | Evidence citation |
|---|---|---|---|
| Recent weight gain / central weight gain | HP:0001824 Weight gain | Reported in 70–95% of patients with endogenous Cushing syndrome; often accompanies central fat redistribution | (reincke2023cushingsyndromea pages 3-4) |
| Facial plethora | HP:0012368 Facial plethora | Reported in 70–90%; one of the more characteristic cutaneous signs | (reincke2023cushingsyndromea pages 3-4, reincke2023cushingsyndromea pages 1-2) |
| High blood pressure | HP:0000822 Hypertension | Reported in 60–90% in JAMA review; other review notes hypertension around 80% overall in endogenous CS | (reincke2023cushingsyndromea pages 3-4, m.c.2025hypertensionandcushing’s pages 1-2) |
| Depression / depressed mood | HP:0000716 Depression | Reported in 50–80%; mood disorders are part of the neuropsychiatric burden | (reincke2023cushingsyndromea pages 3-4, reincke2023cushingsyndromea pages 1-2) |
| Excess body/facial hair in women | HP:0001007 Hirsutism | Reported in 50–75% | (reincke2023cushingsyndromea pages 3-4, reincke2023cushingsyndromea pages 4-5) |
| Proximal muscle weakness / myopathy | HP:0003701 Proximal muscle weakness | Reported in 60–80%; reflects protein catabolism and muscle wasting | (reincke2023cushingsyndromea pages 3-4, reincke2023cushingsyndromea pages 9-10) |
| Round face / moon face | HP:0000340 Round face | Reported in up to 90% | (reincke2023cushingsyndromea pages 3-4) |
| Dorsocervical fat pad (“buffalo hump”) | HP:0030867 Dorsocervical fat pad | Approximately 50% | (reincke2023cushingsyndromea pages 3-4, reincke2023cushingsyndromea pages 4-5) |
| Purple/violaceous striae | HP:0033677 Abdominal striae | Reported in less than 50%; highly suggestive when wide and violaceous | (reincke2023cushingsyndromea pages 3-4, reincke2023cushingsyndromea pages 1-2) |
| Easy bruising | HP:0000978 Easy bruising | Approximately 50% | (reincke2023cushingsyndromea pages 4-5, reincke2023cushingsyndromea pages 1-2) |
| Thin skin / skin atrophy | HP:0000963 Thin skin | Approximately 40% | (reincke2023cushingsyndromea pages 4-5) |
| Oligomenorrhea or amenorrhea | HP:0000858 Menstrual irregularity | Reported in 70–80% of affected women in JAMA review | (reincke2023cushingsyndromea pages 3-4) |
| Osteopenia / osteoporosis / bone fragility | HP:0000939 Osteoporosis | Reported in up to 80%; fracture burden is substantial in overt CS | (reincke2023cushingsyndromea pages 3-4) |
| Diabetes / hyperglycemia | HP:0005978 Hyperglycemia | Diabetes reported in about 30%; hyperglycemia is a common metabolic manifestation | (reincke2023cushingsyndromea pages 4-5, reincke2023cushingsyndromea pages 1-2) |
| Dyslipidemia | HP:0003119 Hypercholesterolemia | Reported in 40–70%; contributes to cardiometabolic risk | (reincke2023cushingsyndromea pages 4-5) |
| Sleep disturbance | HP:0002360 Sleep disturbance | Approximately 60% | (reincke2023cushingsyndromea pages 4-5) |
| Reduced libido | HP:0012873 Decreased libido | Reported in 25–90%; broad range reflects ascertainment variability | (reincke2023cushingsyndromea pages 4-5) |
| Acne | HP:0001061 Acne | Reported in less than 50% | (reincke2023cushingsyndromea pages 4-5) |
| Kidney stones | HP:0000787 Nephrolithiasis | Reported in up to 50% | (reincke2023cushingsyndromea pages 4-5) |
| Hypokalemia | HP:0002900 Hypokalemia | Common laboratory abnormality; especially prominent in ectopic ACTH syndrome | (stachowska2020etiologybaselineclinical pages 1-2, reincke2023cushingsyndromea pages 1-2) |


*Table: This table maps major clinical features of Cushing syndrome to suggested Human Phenotype Ontology terms, with frequency ranges drawn from the 2023 JAMA review and supporting recent evidence. It is useful for structuring phenotype annotations in a disease knowledge base.*

### 3.3 Laboratory abnormalities
Typical laboratory abnormalities include **hyperglycemia/insulin changes, dyslipidemia, leukocytosis with relative lymphopenia**, and **hypokalemia** (especially prominent in ectopic ACTH syndrome). (reincke2023cushingsyndromea pages 4-5, stachowska2020etiologybaselineclinical pages 1-2)

### 3.4 Quality-of-life impact
While QoL is widely recognized as impaired in CS and treatment trials include patient-reported outcomes, quantitative QoL instrument values (e.g., SF-36, CushingQoL) were not extractable from the retrieved evidence excerpts in this run. Trials and extension studies explicitly track HRQoL as outcomes. (gadelha2023longtermefficacyand pages 1-2)

---

## 4. Genetic / Molecular Information
### 4.1 Causal genes and variant classes (selected, evidence-supported)
CS is often tumor-driven and therefore commonly involves **somatic** drivers (pituitary or adrenal lesions), but several **germline** syndromic etiologies exist.

| Etiology category | Typical source lesion | Approx proportion | Key genes/variants (somatic vs germline) | Key pathways | Evidence citation |
|---|---|---:|---|---|---|
| Pituitary ACTH-dependent Cushing disease | ACTH-secreting pituitary corticotroph adenoma / corticotrophinoma | ~60–70% of endogenous CS; registry example 64% | **USP8** somatic activating variants are the most common genetic defect in corticotroph tumors; reported in ~35–41% overall, enriched in females. Other less common somatic alterations in corticotroph tumors: **USP48** (~6%), **TP53** (rare, associated with aggressive tumors/poor outcome), rare **BRAF** reports; germline defects linked to some cases include **MEN1**, **CDKN1B**, **DICER1** | **EGFR/MAPK** activation downstream of USP8; altered somatostatin receptor trafficking/signaling; pituitary tumorigenesis pathways | (reincke2023cushingsyndromea pages 1-2, reincke2023cushingsyndromea pages 2-3, reincke2023cushingsyndromea pages 3-4, loughrey2024insightsonepidemiology pages 1-2, reincke2023cushingsyndromea pages 9-10) |
| Ectopic ACTH-dependent Cushing syndrome | Non-pituitary ACTH-secreting tumors, especially lung carcinoids/small cell and other neuroendocrine tumors | ~6–10% (review); single-center cohort ~11% | No recurrent single germline driver established in provided evidence for all ectopic cases; tumor genetics are heterogeneous and depend on underlying neuroendocrine neoplasm | Ectopic **ACTH/CRH** secretion driving adrenal cortisol excess | (reincke2023cushingsyndromea pages 2-3, reincke2023cushingsyndromea pages 3-4, stachowska2020etiologybaselineclinical pages 1-2) |
| Adrenal ACTH-independent Cushing syndrome (overall) | Cortisol-producing adrenal adenoma, bilateral adrenal hyperplasia, rare adrenocortical carcinoma | ~20–30% (review); registry example 30%; single-center cohort 25% | Genetic causes vary by lesion type. In cortisol-producing adrenal tumors/hyperplasias, provided evidence supports involvement of **PRKACA**, **PRKAR1A**, **PDE11A**, **PDE8B**, **ARMC5**, **CTNNB1**, **GNAS** (lesion-specific; somatic and/or germline depending on disorder) | Dysregulated adrenal steroidogenesis, especially **cAMP/PKA** signaling | (reincke2023cushingsyndromea pages 2-3, reincke2023cushingsyndromea pages 3-4, reincke2023cushingsyndromea pages 8-9) |
| Primary pigmented nodular adrenocortical disease (PPNAD) / micronodular adrenal disease | Bilateral pigmented micronodular adrenal hyperplasia; often Carney complex-associated | Rare adrenal subtype; within reviewed PPNAD cases, 31.43% had Carney complex | Predominantly **PRKAR1A** pathogenic variants (most common; 79.47% of genetically tested PPNAD cases in 2024 systematic review), usually **germline**; additional reported genes in PPNAD/micronodular disease: **PDE11A**, **PRKACA** (including germline amplification/copy gain), **CTNNB1**, **PDE8B**, **ARMC5** | **cAMP/PKA** pathway dysregulation in adrenal cortex | (reincke2023cushingsyndromea pages 8-9) |
| Primary bilateral macronodular adrenal hyperplasia (PBMAH) / bilateral nodular adrenal disease | Bilateral macronodular adrenal hyperplasia with autonomous cortisol secretion | Rare adrenal subtype | **ARMC5** germline mutations reported in 25–50% of PBMAH; additional familial associations noted with **APC**, **MEN1**, **FH**; aberrant GPCR expression also implicated | Aberrant receptor signaling converging on **cAMP/PKA** | (reincke2023cushingsyndromea pages 8-9) |
| Carney complex-associated adrenal Cushing syndrome | PPNAD in the setting of multisystem Carney complex | Subset of PPNAD; in one review 31.43% of PPNAD cases had Carney complex | **PRKAR1A** germline inactivating variants are the canonical cause; rare **PRKACA** constitutional amplification/copy gain also reported in Carney-complex-like PPNAD presentations | **cAMP/PKA** signaling | (reincke2023cushingsyndromea pages 8-9) |
| Exogenous/iatrogenic Cushing syndrome (not endogenous; important exclusion) | Chronic glucocorticoid exposure by oral, inhaled, topical, ocular, or interacting-drug routes | Most common cause of Cushing syndrome overall, but excluded from endogenous CS classification | Not a primary genetic etiology of endogenous CS; drug interactions can precipitate phenotype | HPA-axis suppression from exogenous glucocorticoids | (reincke2023cushingsyndromea pages 1-2) |


*Table: This table summarizes the main endogenous Cushing syndrome etiologies, their approximate frequencies, and the best-supported genes and pathways from the cited evidence. It is useful for linking disease subtypes to lesion source, inheritance context, and molecular mechanisms.*

### 4.2 Recent developments (2024)
Recent molecular work continues to refine corticotroph tumorigenesis. For example, an analysis/systematic review of **USP8** highlights that activating USP8 alterations are implicated in ACTH secretion and cell proliferation in corticotroph adenomas and motivates **EGFR and USP8 pathway targeting** as a research direction. (Hashemi‑Madani et al., *BMC Endocr Disord*, published **2024-06**, URL: https://doi.org/10.1186/s12902-024-01619-z) (reincke2023cushingsyndromea pages 9-10)

---

## 5. Environmental Information
### 5.1 Exogenous/iatrogenic CS
Exogenous glucocorticoids are the most common cause of CS overall, and iatrogenic CS can occur via multiple routes. (reincke2023cushingsyndromea pages 1-2)

A pediatric systematic review of **topical corticosteroid-associated iatrogenic CS** reported (n=63): **81% recovered**, **3.2% partially recovered**, and **6.3% died**, with a mean exposure duration of **25.4 weeks**; discontinuation of the offending steroid was universal, and oral hydrocortisone replacement was commonly used. (Abdalla et al., published **2024-09**, URL: https://doi.org/10.58742/bmj.v2i3.104) (abdalla2024cushingssyndromeand pages 1-2)

---

## 6. Mechanism / Pathophysiology
### 6.1 Causal chain (high-level)
1. **Upstream trigger:** autonomous cortisol secretion (adrenal tumor/hyperplasia) or **ACTH excess** (pituitary/ectopic tumor) (reincke2023cushingsyndromea pages 1-2, reincke2023cushingsyndromea pages 2-3)
2. **Hormonal state:** sustained hypercortisolemia (reincke2023cushingsyndromea pages 1-2)
3. **Downstream systemic effects:** protein catabolism (myopathy), insulin resistance/hyperglycemia, immunosuppression (infection risk), neuropsychiatric effects, and cardiovascular remodeling (hypertension, atherosclerotic risk). (reincke2023cushingsyndromea pages 1-2, reincke2023cushingsyndromea pages 3-4)

### 6.2 Hypertension mechanism (example of downstream pathway)
Excess cortisol can overwhelm **11β-HSD2** protection, allowing mineralocorticoid receptor activation with sodium retention and hypokalemia, and can amplify vascular pressor responses, contributing to the ~80% hypertension prevalence reported in endogenous CS. (m.c.2025hypertensionandcushing’s pages 1-2)

### 6.3 Adrenal genetic pathway theme
Multiple adrenal etiologies converge on **cAMP/PKA signaling dysregulation** (e.g., PRKAR1A in PPNAD; ARMC5 in PBMAH; other lesion-specific genes), consistent with endocrine control of adrenal steroidogenesis. (reincke2023cushingsyndromea pages 8-9)

**Suggested ontology terms (mechanism; not evidence-derived):**
- GO:0006954 *inflammatory response* (downstream infection susceptibility context)
- GO:0008283 *cell population proliferation* (pituitary/adrenal tumor growth)
- GO:0010817 *regulation of hormone levels*

---

## 7. Anatomical Structures Affected
### 7.1 Primary organs and systems
- **Hypothalamic–pituitary–adrenal (HPA) axis**, including pituitary corticotroph tumors (Cushing disease) and adrenal cortisol-producing lesions (reincke2023cushingsyndromea pages 1-2, loughrey2024insightsonepidemiology pages 1-2)
- **Cardiovascular system** (hypertension, myocardial infarction risk) (reincke2023cushingsyndromea pages 9-10)
- **Skeletal system** (osteopenia/osteoporosis, fractures) (reincke2023cushingsyndromea pages 9-10, stachowska2020etiologybaselineclinical pages 11-12)
- **Immune system** (immunosuppression/infection) (reincke2023cushingsyndromea pages 1-2, reincke2023cushingsyndromea pages 9-10)

**Suggested anatomy ontology terms (not evidence-derived):**
- UBERON:0000007 *pituitary gland*
- UBERON:0002369 *adrenal gland*

---

## 8. Temporal Development
### 8.1 Onset and course
CS is typically subacute-to-chronic and often underdiagnosed; cohort data highlight diagnostic challenges (e.g., microadenomas frequently occult on imaging). (reincke2023cushingsyndromea pages 2-3, loughrey2024insightsonepidemiology pages 1-2)

### 8.2 Post-cure recovery dynamics
After curative treatment, the median time to normalization of the HPA axis differs by etiology: **0.6 years (ectopic), 1.4 years (Cushing disease), 2.5 years (adrenal CS)**. (reincke2023cushingsyndromea pages 8-9)

---

## 9. Inheritance and Population
### 9.1 Epidemiology
- Endogenous CS incidence: **2–8 per million per year** (reincke2023cushingsyndromea pages 1-2, reincke2023cushingsyndromea pages 9-10)
- In a Northern Ireland cohort (2000–2019), annual incidence of Cushing disease was **1.39–1.57 per million per year**, and **72%** were female. (Loughrey et al., published **2024-06**, URL: https://doi.org/10.1530/erc-24-0028) (loughrey2024insightsonepidemiology pages 1-2)

### 9.2 Inheritance patterns (selected)
While most pituitary/adrenal tumors are sporadic, **germline** causes are important in specific subtypes:
- PPNAD/Carney complex: commonly **PRKAR1A** germline pathogenic variants (reincke2023cushingsyndromea pages 8-9)

---

## 10. Diagnostics
### 10.1 Evidence-based diagnostic strategy
The diagnostic process requires biochemical confirmation; elevated cortisol alone is insufficient and most patients require more than one screening test. The recommended first-line screening tests are:
- **24-hour UFC**
- **Late-night salivary cortisol**
- **1-mg overnight dexamethasone suppression test (DST)**
with **2–3 samples** recommended for UFC and late-night salivary cortisol due to intrapatient variability. (reincke2023cushingsyndromea pages 4-5, reincke2023cushingsyndromea pages 2-3)

After biochemical confirmation, **plasma ACTH** separates ACTH-independent adrenal causes (suppressed ACTH) from ACTH-dependent causes (midnormal/elevated ACTH). Localization may require pituitary MRI and/or **bilateral inferior petrosal sinus sampling (IPSS)**; these are not screening tools. (reincke2023cushingsyndromea pages 1-2, reincke2023cushingsyndromea pages 2-3)

### 10.2 Diagnostic algorithm figure (real-world implementation)
A stepwise diagnostic algorithm for suspected CS, including screening tests and subsequent etiologic classification/localization, is shown in the JAMA review (Figure 2). (reincke2023cushingsyndromea media 4775d5aa)

### 10.3 Test performance examples
Assay-specific LNSC cutoffs vary; in one prospective study, a cutoff of **10.1 nmol/L** yielded **94% sensitivity** and **84% specificity** for hypercortisolism. (reincke2023cushingsyndromea pages 4-5)

DST false positives can arise from inadequate dexamethasone exposure; measuring dexamethasone and using method-specific cortisol thresholds improved clinical specificity **from 67.5% to 92.4%** while preserving **100% sensitivity** in one LC–MS/MS-based evaluation. (reincke2023cushingsyndromea pages 4-5)

| Test | Specimen | Purpose (screen vs etiology vs localization) | Notes | Performance metrics if present | Evidence citation |
|---|---|---|---|---|---|
| 24-hour urinary free cortisol (UFC) | 24-hour urine | Screen | One of 3 standard first-line screening tests for suspected hypercortisolism; most patients require more than 1 test; 2-3 samples are recommended because of intrapatient variability | NA in provided evidence | (reincke2023cushingsyndromea pages 1-2, reincke2023cushingsyndromea pages 4-5, reincke2023cushingsyndromea pages 2-3) |
| Late-night salivary cortisol (LNSC) | Saliva collected late at night | Screen | Noninvasive first-line screening test; 2-3 samples recommended; considered highly discriminatory in selected hypertensive patients | Assay-specific cutoff 10.1 nmol/L with sensitivity 94% and specificity 84% for hypercortisolism; ectopic ACTH-production cutoff 109.0 nmol/L with sensitivity 50% and specificity 92% | (reincke2023cushingsyndromea pages 1-2, reincke2023cushingsyndromea pages 4-5, m.c.2025hypertensionandcushing’s pages 1-2) |
| 1-mg overnight dexamethasone suppression test (DST) | Serum cortisol after dexamethasone; dexamethasone exposure may also be measured | Screen | Standard first-tier screening test; false positives can occur with missed/insufficient dexamethasone exposure; in adrenal incidentaloma, 1-mg DST is the preferred screening test; post-DST cortisol >50 nmol/L (>1.8 μg/dL) indicates mild autonomous cortisol secretion in 2023 adrenal incidentaloma guidance | Method-specific approach: excluding samples with dexamethasone <1.8 ng/mL and using cortisol cutoff 2.4 μg/dL (66 nmol/L) increased clinical specificity from 67.5% to 92.4% while preserving 100% sensitivity | (reincke2023cushingsyndromea pages 1-2, m.c.2025hypertensionandcushing’s pages 1-2, reincke2023cushingsyndromea pages 2-3) |
| Plasma ACTH | Plasma | Etiology | Used after biochemical confirmation to distinguish adrenal causes (suppressed ACTH) from ACTH-dependent causes (midnormal/elevated ACTH) | Morning ACTH cutoffs referenced in review: <10 pg/mL suggests ACTH-independent; >20 pg/mL suggests ACTH-dependent; 10-20 pg/mL indeterminate | (reincke2023cushingsyndromea pages 1-2, reincke2023cushingsyndromea pages 4-5) |
| Repeat/confirmatory biochemical testing | Mixed: urine, saliva, serum | Screen / confirmation | Diagnosis requires biochemical confirmation; elevated plasma cortisol alone is insufficient; if initial results are inconclusive, second-line dynamic tests may be used | NA | (reincke2023cushingsyndromea pages 4-5) |
| Desmopressin stimulation test | Blood | Etiology / second-line confirmation | Mentioned as a second-line test when first-line studies are inconclusive | NA | (reincke2023cushingsyndromea pages 4-5) |
| 2-day DST-CRH combined test | Blood | Etiology / second-line confirmation | Mentioned as a second-line test for inconclusive cases and for separating neoplastic hypercortisolism from physiologic/non-neoplastic hypercortisolism | NA | (reincke2023cushingsyndromea pages 4-5) |
| Pituitary MRI | MRI imaging | Localization | Used after biochemical confirmation and ACTH-based classification to identify pituitary source; microadenomas may be occult on MRI in a substantial fraction of Cushing disease cases | NA | (reincke2023cushingsyndromea pages 1-2, reincke2023cushingsyndromea pages 2-3, loughrey2024insightsonepidemiology pages 1-2, reincke2023cushingsyndromea media 4775d5aa) |
| Bilateral inferior petrosal sinus sampling (IPSS/BIPSS) | Central venous sampling | Localization | Used to distinguish pituitary ACTH secretion from ectopic ACTH secretion after biochemical confirmation; should not be used for screening | NA | (reincke2023cushingsyndromea pages 1-2, reincke2023cushingsyndromea pages 2-3, loughrey2024insightsonepidemiology pages 1-2, reincke2023cushingsyndromea media 4775d5aa) |
| Adrenal CT/MRI or adrenal imaging | Imaging | Localization | Used when ACTH is suppressed or adrenal source suspected | NA | (reincke2023cushingsyndromea pages 1-2, reincke2023cushingsyndromea media 4775d5aa) |
| Whole-body imaging for ectopic source | Cross-sectional and/or functional imaging | Localization | Used when ACTH-dependent hypercortisolism is confirmed and pituitary source is not established, to search for ectopic ACTH-producing tumors | NA | (reincke2023cushingsyndromea pages 1-2, reincke2023cushingsyndromea media 4775d5aa) |


*Table: This table summarizes the main diagnostic tests used in Cushing syndrome, separating first-line screening from etiology and localization studies. It also includes assay-specific performance values when they were available in the evidence.*

---

## 11. Outcome / Prognosis
### 11.1 Mortality
Endogenous CS is associated with persistent excess mortality. A meta-analysis reported **standardized mortality ratio (SMR) 3.0 (95% CI 2.3–3.9)**, and pooled data attribute many deaths to atherosclerotic disease, thromboembolism, and infection. (reincke2023cushingsyndromea pages 9-10)

In a regional neurosurgical cohort of Cushing disease in Northern Ireland, mortality was substantially elevated versus the general population (**SMR 8.10, 95% CI 3.3–16.7**). (loughrey2024insightsonepidemiology pages 1-2)

### 11.2 Major complications and temporal signal
Registry data indicate markedly elevated standardized incidence rates for complications in the **3 years before diagnosis**, including myocardial infarction, fractures, and deep vein thrombosis (values reported as 4.4, 4.9, and 13.8, respectively). (reincke2023cushingsyndromea pages 9-10)

### 11.3 Recurrence and remission patterns
Recurrence after transsphenoidal surgery for Cushing disease can occur in **up to 35%** of patients. (reincke2023cushingsyndromea pages 8-9)

---

## 12. Treatment
### 12.1 First-line and escalation strategy (authoritative view)
For endogenous CS, **“first-line therapy… is surgery to remove the underlying tumor”**, with additional medical therapy, radiation, or bilateral adrenalectomy used when needed. (reincke2023cushingsyndromea pages 9-10)

### 12.2 Current applications and real-world implementations (selected quantitative data)
| Modality/drug | Mechanism/class | Typical use case | Key quantitative outcomes | Key safety issues | Evidence citation |
|---|---|---|---|---|---|
| Transsphenoidal pituitary surgery | Surgical removal of ACTH-secreting pituitary adenoma | First-line for Cushing disease when lesion is resectable | In a Northern Ireland population-based surgical cohort, immediate postoperative remission was 53% using serum cortisol ≤ 50 nmol/L and 66% using ≤ 138 nmol/L in the first postoperative week; ~70% achieved longer-term remission after a single pituitary surgery | Surgical failure/non-remission; recurrence can occur; requires specialized pituitary center expertise | (loughrey2024insightsonepidemiology pages 1-2, reincke2023cushingsyndromea pages 9-10) |
| Surgery for endogenous Cushing syndrome overall | Surgery to remove causative pituitary, adrenal, or ectopic tumor | First-line therapy for endogenous tumor-driven Cushing syndrome | Authoritative review states first-line therapy is surgery to remove the underlying tumor; many patients subsequently require medication, radiation, or bilateral adrenalectomy | Procedure- and site-specific perioperative risks; persistent disease may require multimodal care | (reincke2023cushingsyndromea pages 1-2, reincke2023cushingsyndromea pages 9-10) |
| Osilodrostat | Adrenal steroidogenesis inhibitor; oral 11β-hydroxylase (CYP11B1) inhibitor | Persistent/recurrent Cushing disease; bridge or alternative when surgery is not feasible/curative; increasingly used across etiologies in practice | LINC 4 extension: 72.4% had normalized mean urinary free cortisol (mUFC) at end-of-trial; 60 entered extension, 53 completed, median treatment duration 87.1 weeks; real-world ILLUSTRATE: UFC fell below ULN in 14/20 (70.0%) with elevated pretreatment UFC; Spanish real-world cohort: 33/37 (89.2%) complete responders, median time to UFC normalization 4 weeks, and 67% normalized by month 1 | Adrenal insufficiency/hypocortisolism; glucocorticoid withdrawal syndrome/adrenal insufficiency in 12/42 (28.6%) in ILLUSTRATE; edema, fatigue, nausea; QT prolongation risk noted in review literature | (gadelha2023longtermefficacyand pages 1-2, araujocastro2025realworlddataon pages 12-13) |
| Osilodrostat (clinical manifestations data) | Same as above | Longer-term medical control of hypercortisolism with monitoring of biochemical and clinical response | In LINC 3, mUFC was controlled in 67.9% at week 24 and 66.4% at week 48; improvements in cardiometabolic parameters, physical manifestations, and QoL generally accompanied mUFC reduction | Requires dose titration and monitoring for adrenal insufficiency and steroid precursor-related effects | (araujocastro2025realworlddataon pages 12-13) |
| Pasireotide-LAR | Pituitary-directed somatostatin receptor ligand (SSTR-targeted) | Persistent/recurrent Cushing disease, especially when pituitary-directed medical therapy is desired | Real-world 12-month study: sustained mUFC reduction, greatest decline in first 3 months (p=0.007); systolic blood pressure decreased during first 6 months (p=0.005); cited phase 3 benchmark mUFC normalization 41% at month 7 | Hyperglycemia was the most common adverse event; fasting glucose and HbA1c increased, with HbA1c significantly higher at last follow-up (p=0.04) | (dzialach2025realworldexperiencewith pages 1-2) |
| Pasireotide subcutaneous ± cabergoline | Pituitary-directed SRL alone or combined with dopamine agonist | Patients with active Cushing disease not adequately controlled on pasireotide alone | Phase II study: 34/68 (50.0%; 95% CI 37.6–62.4) achieved mUFC ≤ ULN at week 35; control remained stable through week 99; responders split evenly between pasireotide monotherapy (17) and pasireotide+cabergoline (17) | Hyperglycemia 51.5%, nausea 51.5%, diarrhea 44.1%, cholelithiasis 33.8% | (feelders2023longtermefficacyand pages 1-2) |
| Pasireotide real-life monotherapy/combination | Same as above; combination with cabergoline or metyrapone in practice | Real-world escalation strategy when UFC remains elevated on monotherapy | Monotherapy normalized UFC in 59% and LNSC in 38%; adding a second cortisol-lowering agent increased overall UFC normalization to 67%; >5% weight loss in 47%; half showed improved blood-pressure profile | Clinically significant hyperglycemia in 61%; circadian rhythm control remained difficult | (mondin2025reallifedataon pages 1-2) |
| Cabergoline add-on | Dopamine agonist | Add-on to pasireotide in incompletely controlled Cushing disease | In the phase II pasireotide study, cabergoline add-on contributed to the 50% overall week-35 mUFC control rate and sustained control to week 99 in combination-treated patients | Add-on tolerability considered acceptable in study; agent-specific risks not quantified in the provided evidence | (feelders2023longtermefficacyand pages 1-2) |
| Metyrapone add-on | Adrenal steroidogenesis inhibitor (11β-hydroxylase inhibition) | Add-on to pituitary-directed therapy in real-life regimens | In the 2025 real-life pasireotide cohort, add-on therapy (including metyrapone) increased overall UFC normalization from 59% on pasireotide alone to 67% overall | Add-on treatment was described as generally well tolerated in this cohort | (mondin2025reallifedataon pages 1-2) |
| Steroidogenesis inhibitors as a class | Adrenal cortisol synthesis blockade | Alternative to surgery when surgery is infeasible/contraindicated; rapid control for severe hypercortisolism; bridge therapy | 2024 review states these drugs are a therapeutic alternative when surgery is not feasible and are particularly important when rapid cortisol control is needed; evidence base has expanded, but head-to-head comparative studies remain limited | Drug-specific toxicities vary; careful individualized selection and monitoring required | (m.c.2025hypertensionandcushing’s pages 1-2) |
| Radiation therapy / stereotactic radiosurgery | Delayed local pituitary tumor control | Second-line for persistent/recurrent Cushing disease after surgery or with residual tumor | Review reports stereotactic radiation is highly effective (~92%) for tumor control, with 5-year biochemical remission 50%–65% | New hypopituitarism in ~20%; delayed onset of biochemical effect | (reincke2023cushingsyndromea pages 9-10) |
| Bilateral adrenalectomy | Definitive surgical ablation of adrenal cortisol production | Severe persistent hypercortisolism despite other therapy or when rapid normalization is needed | Expert review describes it as an option for patients not responsive to surgery/medication and for urgent cortisol control; specific quantitative outcomes not provided in the available evidence | Lifelong adrenal insufficiency and need for steroid replacement; procedure-related risks | (reincke2023cushingsyndromea pages 1-2, reincke2023cushingsyndromea pages 9-10) |


*Table: This table summarizes major treatment modalities for endogenous Cushing syndrome and Cushing disease, including real-world implementation patterns and quantitative outcomes where available. It is useful for comparing first-line surgery with newer medical therapies such as osilodrostat and pasireotide, alongside key safety considerations.*

Key recent quantitative examples:
- **Osilodrostat (LINC 4 extension, 2023):** **72.4%** achieved normal mean UFC at end-of-trial, with sustained clinical improvements over long-term therapy. (Gadelha et al., published **2023-08**, URL: https://doi.org/10.3389/fendo.2023.1236465) (gadelha2023longtermefficacyand pages 1-2)
- **Pasireotide ± cabergoline (Phase II, 2023):** **50.0%** achieved mean UFC ≤ ULN at week 35; hyperglycemia occurred in **51.5%**. (Feelders et al., published **2023-10**, URL: https://doi.org/10.3389/fendo.2023.1165681) (feelders2023longtermefficacyand pages 1-2)

### 12.3 MAXO term suggestions (not evidence-derived)
- MAXO:0000605 *Surgical excision*
- MAXO:0000504 *Drug therapy*
- MAXO:0000647 *Radiation therapy*

---

## 13. Prevention
### 13.1 Primary prevention (iatrogenic disease prevention)
Because exogenous glucocorticoids are the most common overall cause, a core preventive step is to **identify and avoid unnecessary glucocorticoid exposure**, including non-oral preparations. (reincke2023cushingsyndromea pages 1-2)

In pediatric topical-steroid iatrogenic CS, prevention recommendations include **specialist supervision of topical corticosteroid administration** and caregiver education on correct use and side effects. (abdalla2024cushingssyndromeand pages 1-2)

### 13.2 Secondary prevention (targeted screening)
Screening is recommended in selected high-risk clinical contexts (e.g., adrenal adenomas; hypertensive patients with red-flag phenotype), using UFC, DST, or LNSC rather than indiscriminate testing. (reincke2023cushingsyndromea pages 2-3, m.c.2025hypertensionandcushing’s pages 1-2)

---

## 14. Other Species / Natural Disease
Veterinary or cross-species data were not retrieved in evidence suitable for synthesis in this run.

---

## 15. Model Organisms
Model-organism evidence was not retrieved in evidence suitable for synthesis in this run.

---

## Key gaps and limitations of this report
- ICD-10/ICD-11, MeSH, OMIM/Orphanet identifiers were not accessible from the retrieved evidence and are therefore not reported.
- Many primary sources in the retrieved evidence do not expose PMIDs in the accessible text; this report provides **DOIs/URLs and publication months/years** where available.
- Quantitative QoL instrument scores and detailed test sensitivity/specificity across multiple assays were not fully extractable beyond the included examples.


References

1. (reincke2023cushingsyndromea pages 1-2): Martin Reincke and Maria Fleseriu. Cushing syndrome: a review. JAMA, 330 2:170-181, Jul 2023. URL: https://doi.org/10.1001/jama.2023.11305, doi:10.1001/jama.2023.11305. This article has 229 citations.

2. (reincke2023cushingsyndromea pages 2-3): Martin Reincke and Maria Fleseriu. Cushing syndrome: a review. JAMA, 330 2:170-181, Jul 2023. URL: https://doi.org/10.1001/jama.2023.11305, doi:10.1001/jama.2023.11305. This article has 229 citations.

3. (m.c.2025hypertensionandcushing’s pages 1-2): De Martino M.C., L. Canu, I. Bonaventura, C. Vitiello, C. Sparano, and A. Cozzolino. Hypertension and cushing’s syndrome: hunt for the red flag. Journal of Endocrinological Investigation, 48:1909-1918, Mar 2025. URL: https://doi.org/10.1007/s40618-024-02453-9, doi:10.1007/s40618-024-02453-9. This article has 6 citations and is from a peer-reviewed journal.

4. (loughrey2024insightsonepidemiology pages 1-2): Paul Benjamin Loughrey, Brian Herron, Stephen Cooke, Philip Weir, Jayna Elizabeth Smyth, Karen R Mullan, Estelle G Healy, Jane Evanson, Stephanie G Craig, Jacqueline A James, Márta Korbonits, and Steven J Hunter. Insights on epidemiology, morbidity and mortality of cushing’s disease in northern ireland. Endocrine-Related Cancer, Jun 2024. URL: https://doi.org/10.1530/erc-24-0028, doi:10.1530/erc-24-0028. This article has 9 citations and is from a domain leading peer-reviewed journal.

5. (gadelha2023longtermefficacyand pages 1-2): Mônica Gadelha, Peter J. Snyder, Przemysław Witek, Marie Bex, Zhanna Belaya, Adina F. Turcu, Richard A. Feelders, Anthony P. Heaney, Michaela Paul, Alberto M. Pedroncelli, and Richard J. Auchus. Long-term efficacy and safety of osilodrostat in patients with cushing’s disease: results from the linc 4 study extension. Frontiers in Endocrinology, Aug 2023. URL: https://doi.org/10.3389/fendo.2023.1236465, doi:10.3389/fendo.2023.1236465. This article has 44 citations.

6. (feelders2023longtermefficacyand pages 1-2): Richard A. Feelders, Maria Fleseriu, Pinar Kadioglu, Marie Bex, Deyanira González-Devia, Cesar Luiz Boguszewski, Dilek Gogas Yavuz, Heather Patino, Alberto M. Pedroncelli, Ricardo Maamari, Arghya Chattopadhyay, Beverly M. K. Biller, and Rosario Pivonello. Long-term efficacy and safety of subcutaneous pasireotide alone or in combination with cabergoline in cushing’s disease. Frontiers in Endocrinology, Oct 2023. URL: https://doi.org/10.3389/fendo.2023.1165681, doi:10.3389/fendo.2023.1165681. This article has 26 citations.

7. (abdalla2024cushingssyndromeand pages 1-2): Berun A. Abdalla, Maria A. Rasool, Goran J. Baiz, Zanyar Kh. Hama, Karokh K. Mohammed, Yousif M. Mahmood, Ronak S. Ahmed, Wirya N. Sabr, Khdir Hussein Hamad Khoshnaw, Soran M. Ahmed, Karzan M. Hasan, Bilal A. Mohammed, Honar O. Kareem, and Dyari Q. Hamad. Cushing's syndrome and topical corticosteroids in pediatrics: a systematic review. Barw Medical Journal, Sep 2024. URL: https://doi.org/10.58742/bmj.v2i3.104, doi:10.58742/bmj.v2i3.104. This article has 3 citations.

8. (reincke2023cushingsyndromea pages 4-5): Martin Reincke and Maria Fleseriu. Cushing syndrome: a review. JAMA, 330 2:170-181, Jul 2023. URL: https://doi.org/10.1001/jama.2023.11305, doi:10.1001/jama.2023.11305. This article has 229 citations.

9. (reincke2023cushingsyndromea pages 3-4): Martin Reincke and Maria Fleseriu. Cushing syndrome: a review. JAMA, 330 2:170-181, Jul 2023. URL: https://doi.org/10.1001/jama.2023.11305, doi:10.1001/jama.2023.11305. This article has 229 citations.

10. (reincke2023cushingsyndromea pages 9-10): Martin Reincke and Maria Fleseriu. Cushing syndrome: a review. JAMA, 330 2:170-181, Jul 2023. URL: https://doi.org/10.1001/jama.2023.11305, doi:10.1001/jama.2023.11305. This article has 229 citations.

11. (stachowska2020etiologybaselineclinical pages 1-2): Barbara Stachowska, Justyna Kuliczkowska-Płaksej, Marcin Kałużny, Jędrzej Grzegrzółka, Maja Jończyk, and Marek Bolanowski. Etiology, baseline clinical profile and comorbidities of patients with cushing’s syndrome at a single endocrinological center. Endocrine, 70:616-628, Sep 2020. URL: https://doi.org/10.1007/s12020-020-02468-1, doi:10.1007/s12020-020-02468-1. This article has 9 citations and is from a peer-reviewed journal.

12. (reincke2023cushingsyndromea pages 8-9): Martin Reincke and Maria Fleseriu. Cushing syndrome: a review. JAMA, 330 2:170-181, Jul 2023. URL: https://doi.org/10.1001/jama.2023.11305, doi:10.1001/jama.2023.11305. This article has 229 citations.

13. (stachowska2020etiologybaselineclinical pages 11-12): Barbara Stachowska, Justyna Kuliczkowska-Płaksej, Marcin Kałużny, Jędrzej Grzegrzółka, Maja Jończyk, and Marek Bolanowski. Etiology, baseline clinical profile and comorbidities of patients with cushing’s syndrome at a single endocrinological center. Endocrine, 70:616-628, Sep 2020. URL: https://doi.org/10.1007/s12020-020-02468-1, doi:10.1007/s12020-020-02468-1. This article has 9 citations and is from a peer-reviewed journal.

14. (reincke2023cushingsyndromea media 4775d5aa): Martin Reincke and Maria Fleseriu. Cushing syndrome: a review. JAMA, 330 2:170-181, Jul 2023. URL: https://doi.org/10.1001/jama.2023.11305, doi:10.1001/jama.2023.11305. This article has 229 citations.

15. (araujocastro2025realworlddataon pages 12-13): Marta Araujo-Castro, Rogelio García-Centeno, Laura González, Felicia A. Hanzu, Aida Orois, Rosa Camara, María Dolores Ollero García, Ana Irigaray Echarri, Paola Gracia Gimeno, Eider Pascual-Corrales, Betina Biagetti, Andrés Cardona, Inmaculada González Molero, Andreu Simo-Servat, Fernando Guerrero Pérez, Rocío Villar-Taibo, Ignacio Bernabéu, Carmen Fajardo-Montañana, Cristina Novo-Rodríguez, Carmen Tenorio Jimenéz, María Calatayud, María Dolores Moure Rodríguez, Fernando Cordido, Ana Castro, Lucía Manzano Valero, Miguel Paja Fano, Jessica Goi, Anna Aulinas, Pablo Abellán, Pedro Iglesias, and Alfonso Soto-Moreno. Real-world data on the efficacy and safety of osilodrostat in patients with cushing’s disease in spain. Journal of Clinical Medicine, 14:7575, Oct 2025. URL: https://doi.org/10.3390/jcm14217575, doi:10.3390/jcm14217575. This article has 2 citations.

16. (dzialach2025realworldexperiencewith pages 1-2): Lukasz Dzialach, Wioleta Respondek, and Przemyslaw Witek. Real-world experience with pasireotide-lar in cushing’s disease: single-center 12-month observational study. Journal of Clinical Medicine, 14:2794, Apr 2025. URL: https://doi.org/10.3390/jcm14082794, doi:10.3390/jcm14082794. This article has 3 citations.

17. (mondin2025reallifedataon pages 1-2): Alessandro Mondin, Filippo Ceccato, Carla Scaroni, Luca Denaro, Renzo Manara, Umberto Maria Robertazzo, and Mattia Barbot. Real-life data on pasireotide in monotherapy or combined in active cushing’s disease. Frontiers in Endocrinology, Nov 2025. URL: https://doi.org/10.3389/fendo.2025.1695342, doi:10.3389/fendo.2025.1695342. This article has 0 citations.