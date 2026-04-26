---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T17:32:00.522127'
end_time: '2026-04-25T17:39:42.565661'
duration_seconds: 462.04
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Coffin-Siris syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 20
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Coffin-Siris syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Coffin-Siris syndrome** covering all of the
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
- **Disease Name:** Coffin-Siris syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Coffin-Siris syndrome** covering all of the
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


# Coffin–Siris syndrome (CSS): Disease characteristics research report (Mendelian)

## Executive summary
Coffin–Siris syndrome (CSS) is a rare multisystem neurodevelopmental disorder most classically defined by the triad of intellectual disability/developmental delay, coarse/dysmorphic facial features, and hypoplasia/aplasia of the fifth digit distal phalanx or nail. It is primarily caused by pathogenic germline variants affecting the SWI/SNF (BAF) chromatin remodeling complex (and closely related factors), with ARID1B as the most common gene. Recent work emphasizes (i) broad clinical heterogeneity across BAF-pathway genes, (ii) the growing role of genome-wide DNA methylation “episignatures” as functional biomarkers to resolve ambiguous cases, and (iii) expanding prenatal and adult phenotypes reported in 2023–2024 publications. (sekiguchi2019geneticabnormalitiesin pages 1-2, lee2021phenotypicandmolecular pages 1-2, milutinovic2023autismspectrumdisorder pages 1-2, arefeshghi2018bafopathies’dnamethylation pages 1-2, keskinen2024prenatalcoffinsirissyndrome pages 5-6)

A structured quantitative summary of key cohort and registry statistics from the evidence gathered is provided in the table artifact below.

| Evidence type | Source (first author year, journal) | Publication date (month/year) | URL/DOI | Key quantitative statistics | Key quoted phrase from abstract |
|---|---|---|---|---|---|
| Cohort | Sekiguchi 2019, *Journal of Human Genetics* | 09/2019 | https://doi.org/10.1038/s10038-019-0667-4 | 78 pathogenic variations in 78 patients; gene counts: **ARID1B 48**, **SMARCB1 8**, **SMARCA4 7**, **ARID1A 6**, **SOX11 4**, **SMARCE1 1**, **PHF6 1**; plus CNVs including **SMARCA2** and partial **SMARCB1** deletion (sekiguchi2019geneticabnormalitiesin pages 1-2) | “confirmed 78 pathogenic variations in 78 patients” (sekiguchi2019geneticabnormalitiesin pages 1-2) |
| Cohort/registry | Vasko 2021, *Genes* | 06/2021 | https://doi.org/10.3390/genes12060937 | **208 individuals** in CSS/BAF complex registry; **ARID1B n=130**, **SMARCA4 n=32** specifically noted; common features included hypotonia, hypertrichosis, sparse scalp hair, distal phalanx hypoplasia (ciliberto2023epilepsyincoffin–siris pages 7-7) | “Genotype-Phenotype Correlations in 208 Individuals with Coffin-Siris Syndrome” (ciliberto2023epilepsyincoffin–siris pages 7-7) |
| Cohort | Lee 2021, *BMC Medical Genomics* | 10/2021 | https://doi.org/10.1186/s12920-021-01104-9 | In **564** neurodevelopmental cases, **12/564 (2.1%)** had SSRIDDs; **10 CSS**; **ARID1B 8/12**; frequent phenotypes: thick eyebrows **10/12**, hypertrichosis **8/12**, coarse face **8/12**, thick lips **8/12**, long eyelashes **8/12**, corpus callosum agenesis/hypoplasia **6/12** (lee2021phenotypicandmolecular pages 1-2) | “ARID1B, found in eight patients, was the most frequently altered gene.” (lee2021phenotypicandmolecular pages 1-2) |
| DNA methylation cohort | Aref-Eshghi 2018, *Nature Communications* | 11/2018 | https://doi.org/10.1038/s41467-018-07193-y | CSS methylation probe sets: **146 CpGs (CSS1/ARID1B)**, **135 CpGs (CSS3/SMARCB1)**, **356 CpGs (NCBRS/SMARCA2)**; **no CpGs** met cutoffs for CSS4 in **n=2**; model used **0.5** probability cutoff and **10-fold cross-validation** (arefeshghi2018bafopathies’dnamethylation pages 1-2, arefeshghi2018bafopathies’dnamethylation pages 14-15) | “Specificity of this epi-signature was confirmed across a wide range of neurodevelopmental conditions” (arefeshghi2018bafopathies’dnamethylation pages 1-2) |
| Case report/literature review | Milutinovic 2023, *Frontiers in Psychiatry* | 08/2023 | https://doi.org/10.3389/fpsyt.2023.1199710 | **ARID1B** abnormalities reported in **68–83%** of CSS cases; index patient had heterozygous de novo **ARID1B c.1638_1647del** (milutinovic2023autismspectrumdisorder pages 1-2) | “being found in 68–83% of cases” (milutinovic2023autismspectrumdisorder pages 1-2) |
| Case report | Huang 2024, *BMC Medical Genomics* | 05/2024 | https://doi.org/10.1186/s12920-024-01904-9 | Estimated incidence **1:10,000–1:100,000**; **ARID1B 51–75%** of cases; de novo heterozygous frameshift **c.3981dup (p.Glu1328ArgfsTer5)**; ARID1B mRNA approximately **30% lower** in proband (huang2024denovovariation pages 1-2) | “a rare autosomal dominant inheritance disorder” (huang2024denovovariation pages 1-2) |
| Registry/review | Ciliberto 2023, *American Journal of Medical Genetics Part A* | 09/2023 | https://doi.org/10.1002/ajmg.a.62979 | Prior ARID1B series: epilepsy in **28.2% of 143** patients; neuroimaging abnormalities in about half of patients: **20/41** and **20/47** in cited series; registry gene distribution: **ARID1B 60%**, **SMARCA4 14%**, **SMARCB1 7%**, **ARID1A 6%**, **ARID2 5%**, **SOX11 3%**, **SMARCE1 2%**, **DPF2 1%**, **SMARCC2/PHF6/ACTL6A <1%** (ciliberto2023epilepsyincoffin–siris pages 1-2, ciliberto2023epilepsyincoffin–siris pages 6-6) | “up to 28% of patients have previously been reported to have seizures” (ciliberto2023epilepsyincoffin–siris pages 1-1) |
| Registry subgroup | Ciliberto 2023, *American Journal of Medical Genetics Part A* | 09/2023 | https://doi.org/10.1002/ajmg.a.62979 | In registry patients with epilepsy, **14** cases reported; Lennox-Gastaut syndrome diagnosed in **1/14 (7%)**; LGS-consistent findings in **3/14 (21%)** (ciliberto2023epilepsyincoffin–siris pages 5-6) | “Epilepsy in these patients tends to be focal or multifocal in origin and usually relatively easy to control” (ciliberto2023epilepsyincoffin–siris pages 5-6) |
| Prenatal case series | Keskinen 2024, *Pediatric and Developmental Pathology* | 11/2024 | https://doi.org/10.1177/10935266231210155 | **2 prenatal cases**; cites broader literature with **208 individuals** and **63 patients**; emphasizes recurrent severe prenatal CNS/cardiac malformations and increased fetal genetic testing (keskinen2024prenatalcoffinsirissyndrome pages 5-6) | “The CNS malformations and serious cardiac malformations are recurrent malformations in prenatal CSS cases.” (keskinen2024prenatalcoffinsirissyndrome pages 5-6) |


*Table: This table summarizes the main quantitative genetics, registry, cohort, and diagnostic epigenetics findings for Coffin–Siris syndrome from the gathered evidence. It highlights recurring gene distributions, cohort sizes, phenotype frequencies, and key quoted phrases useful for a knowledge-base entry.*

---

## 1. Disease information

### 1.1 What is the disease?
CSS is a congenital/neurodevelopmental syndrome characterized by developmental delay/intellectual disability with recognizable craniofacial and limb/nail anomalies and frequent multisystem involvement. In a large cohort study, CSS is described as “a congenital disorder characterized by coarse facial features, intellectual disability, and hypoplasia of the fifth digit and nails.” (sekiguchi2019geneticabnormalitiesin pages 1-2)

A clinical cohort defining features within SWI/SNF-complex-related intellectual disability disorders (SSRIDDs) describes CSS as “characterized by intellectual disability (ID) and is often accompanied by a coarse face, hypertrichosis, sparse scalp hair, and hypoplasia/aplasia of the distal phalanx or nail of the fifth digit.” (lee2021phenotypicandmolecular pages 1-2)

A 2023 case report reiterates the classic phenotypic core as “aplasia or hypoplasia of the distal phalanx or nail of the fifth and additional digits, developmental or cognitive delay of varying degrees, distinctive facial features, hypotonia, hirsutism/hypertrichosis, and sparse scalp hair.” (milutinovic2023autismspectrumdisorder pages 1-2)

### 1.2 Key identifiers (from available evidence)
The retrieved evidence explicitly references:
- **OMIM/MIM:** CSS “MIM 135900” (lee2021phenotypicandmolecular pages 1-2, ciliberto2023epilepsyincoffin–siris pages 1-1)

Not available in the retrieved evidence set (requires external disease databases not captured in the current document corpus): **Orphanet ID, ICD-10/ICD-11 codes, MeSH ID, and MONDO ID**.

### 1.3 Synonyms / alternative names
From the retrieved evidence, CSS is frequently discussed as part of a broader umbrella:
- **“SWI/SNF complex-related intellectual disability disorders (SSRIDDs)”** (review framing) (lee2021phenotypicandmolecular pages 1-2)
- **“BAFopathies”** (epigenomic/episignature framing across CSS and related disorders) (arefeshghi2018bafopathies’dnamethylation pages 1-2)

### 1.4 Evidence provenance (individual vs aggregated)
- **Aggregated resources/cohorts/registries:** Large gene-ascertained cohorts and registries (e.g., a large genetic cohort confirming 78 pathogenic variants; registry studies with gene distributions) (sekiguchi2019geneticabnormalitiesin pages 1-2, ciliberto2023epilepsyincoffin–siris pages 6-6)
- **Individual patient reports:** Several 2023–2024 papers are case reports expanding phenotype (e.g., ASD association; early-onset high myopia; SOX11 cases; prenatal cases) (milutinovic2023autismspectrumdisorder pages 1-2, huang2024denovovariation pages 1-2, keskinen2024prenatalcoffinsirissyndrome pages 5-6)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** germline pathogenic variants in genes encoding components of the SWI/SNF (BAF) chromatin-remodeling complex and related transcription factors (e.g., SOX11/SOX4). Cohort work notes CSS is “an autosomal dominant developmental disorder” (sekiguchi2019geneticabnormalitiesin pages 1-2) and emphasizes pathogenic variants in BAF-complex components (sekiguchi2019geneticabnormalitiesin pages 1-2, lee2021phenotypicandmolecular pages 1-2).

A genotype–phenotype review/cohort abstract lists multiple causative genes including **ARID1A, ARID1B, ARID2, DPF2, SMARCA4, SMARCB1, SMARCC2, SMARCE1, SOX11, SOX4** (milutinovic2023autismspectrumdisorder pages 1-2), consistent with cohort findings of recurrent pathogenic variants in these genes (sekiguchi2019geneticabnormalitiesin pages 1-2, lee2021phenotypicandmolecular pages 1-2).

### 2.2 Risk factors
For CSS (a Mendelian disorder), **the dominant “risk factor” is carrying a pathogenic variant** in a causal gene. Most reported cases are **de novo** in published case reports (e.g., de novo ARID1B deletion variant and de novo frameshift; prenatal de novo examples) (huang2024denovovariation pages 1-2, milutinovic2023autismspectrumdisorder pages 1-2).

No environmental risk factors, lifestyle risk factors, or infectious triggers are described in the retrieved evidence.

### 2.3 Protective factors / Gene–environment interactions
No protective factors or gene–environment interactions were identified in the retrieved evidence.

---

## 3. Phenotypes

### 3.1 Core phenotype domains and suggested HPO terms
Below are phenotype domains supported by the retrieved evidence, with example HPO suggestions (for knowledge-base mapping). Frequencies are included only when explicitly available.

#### Neurodevelopment / behavior
- **Developmental delay / intellectual disability** (near-universal across cohorts) (sekiguchi2019geneticabnormalitiesin pages 1-2, lee2021phenotypicandmolecular pages 1-2)  
  - HPO: **HP:0001263** (Global developmental delay), **HP:0001249** (Intellectual disability)
- **Speech delay (often profound)** (lee2021phenotypicandmolecular pages 1-2)  
  - HPO: **HP:0000750** (Delayed speech and language development)
- **Autism spectrum disorder / autistic traits** reported in ARID1B-related CSS spectrum case report (milutinovic2023autismspectrumdisorder pages 1-2)  
  - HPO: **HP:0000729** (Autistic behavior)

#### Craniofacial / ectodermal
- **Coarse facial features / dysmorphic facial features** (sekiguchi2019geneticabnormalitiesin pages 1-2, lee2021phenotypicandmolecular pages 1-2, huang2024denovovariation pages 1-2)  
  - HPO: **HP:0000280** (Coarse facial features)
- **Hypertrichosis / hirsutism** (frequent) (lee2021phenotypicandmolecular pages 1-2, milutinovic2023autismspectrumdisorder pages 1-2)  
  - HPO: **HP:0000998** (Hypertrichosis)
- **Sparse scalp hair** (lee2021phenotypicandmolecular pages 1-2, milutinovic2023autismspectrumdisorder pages 1-2, huang2024denovovariation pages 1-2)  
  - HPO: **HP:0002200** (Sparse scalp hair)

#### Limbs / nails
- **Hypoplasia/aplasia of distal phalanx or nail of fifth digit** (signature feature) (sekiguchi2019geneticabnormalitiesin pages 1-2, lee2021phenotypicandmolecular pages 1-2, milutinovic2023autismspectrumdisorder pages 1-2, huang2024denovovariation pages 1-2)  
  - HPO: **HP:0001819** (Fifth finger clinodactyly) is not precise; more appropriate: **HP:0001817** (Fifth finger brachydactyly) and nail terms such as **HP:0001800** (Nail dysplasia) may be used depending on the specific finding.

#### Neurologic
- **Hypotonia** (lee2021phenotypicandmolecular pages 1-2, milutinovic2023autismspectrumdisorder pages 1-2, huang2024denovovariation pages 1-2)  
  - HPO: **HP:0001252** (Muscular hypotonia)
- **Brain structural abnormalities/neuroimaging findings** common in series: ~half in two cited cohorts (20/41; 20/47) (ciliberto2023epilepsyincoffin–siris pages 1-2)  
  - HPO example: **HP:0001276** (Brain morphology abnormality)
- **Corpus callosum agenesis/hypoplasia** in 6/12 of a Korean SSRIDD cohort (lee2021phenotypicandmolecular pages 1-2)  
  - HPO: **HP:0001274** (Agenesis of corpus callosum)

#### Seizures / epilepsy
- Epilepsy is a recognized complication, with reported prevalence **28.2%** in an ARID1B cohort (n=143) (ciliberto2023epilepsyincoffin–siris pages 1-2), and registry analysis suggesting variable/possibly lower reporting depending on ascertainment (ciliberto2023epilepsyincoffin–siris pages 5-6).
  - HPO: **HP:0001250** (Seizures), **HP:0002353** (EEG abnormality)

#### Multiorgan congenital anomalies (examples)
- **Cardiac anomalies** are recurrent, including prenatal severe cardiovascular malformations (keskinen2024prenatalcoffinsirissyndrome pages 5-6) and case-level defects such as patent foramen ovale/ventricular septal defect (huang2024denovovariation pages 1-2).
  - HPO: **HP:0001627** (Abnormality of the cardiovascular system)
- **Renal anomalies** (e.g., renal cysts) (huang2024denovovariation pages 1-2)
  - HPO: **HP:0000077** (Kidney abnormality)

### 3.2 Phenotype frequencies / statistics (from cohorts in evidence)
- Korean WES cohort of SSRIDDs (n=12): thick eyebrows **10/12**, hypertrichosis **8/12**, coarse face **8/12**, thick lips **8/12**, long eyelashes **8/12**, corpus callosum agenesis/hypoplasia **6/12**, developmental delay **12/12** (lee2021phenotypicandmolecular pages 1-2).
- Neuroimaging abnormalities: approximately half in two cited CSS cohorts (20/41 and 20/47) (ciliberto2023epilepsyincoffin–siris pages 1-2).
- Epilepsy: 28.2% in an ARID1B cohort (n=143) (ciliberto2023epilepsyincoffin–siris pages 1-2); registry-based epilepsy subgroup analysis included 14 epilepsy cases with Lennox–Gastaut syndrome diagnosed in 1/14 (7%) and LGS-consistent findings in 3/14 (21%) (ciliberto2023epilepsyincoffin–siris pages 5-6).

### 3.3 Quality-of-life impacts
Formal QoL instruments (EQ-5D/SF-36/PROMIS) were not reported in the retrieved evidence set.

---

## 4. Genetic / molecular information

### 4.1 Causal genes (supported by retrieved evidence)
Multiple sources converge on CSS as a BAF/SWI-SNF chromatin remodeling disorder with genetic heterogeneity:
- Large cohort lists implicated genes including **ARID1A, ARID1B, ARID2, SMARCA4, SMARCB1, SMARCE1, SOX11, PHF6, DPF2** (sekiguchi2019geneticabnormalitiesin pages 1-2).
- SSRIDD cohort emphasizes SWI/SNF complex components (ARID1B, SMARCA4, SMARCB1, ARID2, SMARCA2) (lee2021phenotypicandmolecular pages 1-2).
- Case report review notes ARID1B plus additional genes (**ARID1A/2, DPF2, PHF6, SMARCA2/4, SMARCB1, SMARCC2, SMARCE1, SOX4/11**) (milutinovic2023autismspectrumdisorder pages 1-2).

### 4.2 Gene contribution and registry distributions
- ARID1B is often the leading gene. A 2023 case report/literature review states ARID1B abnormalities are found in **68–83%** of cases (milutinovic2023autismspectrumdisorder pages 1-2).
- A 2024 study reports ARID1B is most commonly implicated in **51–75%** of cases (huang2024denovovariation pages 1-2).
- International registry gene distribution (as reported in an epilepsy-focused registry analysis): **ARID1B 60%**, **SMARCA4 14%**, **SMARCB1 7%**, **ARID1A 6%**, **ARID2 5%**, **SOX11 3%**, **SMARCE1 2%**, **DPF2 1%**, **SMARCC2/PHF6/ACTL6A <1%** (ciliberto2023epilepsyincoffin–siris pages 6-6).

### 4.3 Pathogenic variant classes and functional consequences
Across evidence, CSS is generally consistent with **haploinsufficiency/loss-of-function** for some genes (notably ARID1B), while other SWI/SNF genes often show missense/nontruncating variants in cohorts.
- In the Korean cohort: “All pathogenic variants in ARID1B were truncating, whereas variants in SMARCA2, SMARCB1, and SMARCA4 were nontruncating (missense).” (lee2021phenotypicandmolecular pages 1-2)
- A 2024 ARID1B report states “almost all ARID1B gene variants are non-functional” and includes nonsense/frameshift/splice-site and deletion mechanisms (huang2024denovovariation pages 1-2).
- Large cohort confirmed numerous ARID1B variants (48) and additional variants in SMARCB1, SMARCA4, ARID1A, SOX11, etc., and noted CNVs involving SMARCA2 (sekiguchi2019geneticabnormalitiesin pages 1-2).

**Example pathogenic variants (from 2023–2024 case reports):**
- ARID1B de novo pathogenic deletion **c.1638_1647del** (milutinovic2023autismspectrumdisorder pages 1-2)
- ARID1B de novo frameshift insertion **c.3981dup (p.Glu1328ArgfsTer5)** with ~30% reduced ARID1B mRNA in proband (huang2024denovovariation pages 1-2)

### 4.4 Epigenetic information (DNA methylation episignatures)
A major mechanistic and diagnostic advance for CSS/BAFopathies is the identification of disorder-specific peripheral blood DNA methylation profiles:
- A Nature Communications study reports “overlapping peripheral blood DNA methylation epi-signatures” for CSS subtypes (ARID1B, SMARCB1, SMARCA4) and Nicolaides–Baraitser syndrome (SMARCA2), supporting a functional continuum. (arefeshghi2018bafopathies’dnamethylation pages 1-2)
- The same work demonstrates diagnostic potential: a machine-learning classifier trained on the methylation profile can “resolve ambiguous clinical cases,” “reclassify those with variants of unknown significance,” and identify “previously undiagnosed subjects through targeted population screening.” (arefeshghi2018bafopathies’dnamethylation pages 1-2)
- Specificity testing was “confirmed across a wide range of neurodevelopmental conditions including other chromatin remodeling and epigenetic machinery disorders.” (arefeshghi2018bafopathies’dnamethylation pages 1-2)

**Episignature feature sizes reported:** 146 CpGs for CSS1/ARID1B, 135 CpGs for CSS3/SMARCB1, 356 CpGs for NCBRS/SMARCA2 (arefeshghi2018bafopathies’dnamethylation pages 1-2).

### 4.5 Modifier genes / chromosomal abnormalities
The retrieved evidence supports a role for **copy number variants (CNVs)** including ARID1B microdeletions and CNVs involving SMARCA2 in cohorts (sekiguchi2019geneticabnormalitiesin pages 1-2, arefeshghi2018bafopathies’dnamethylation pages 1-2). However, specific modifier genes were not identified in the retrieved evidence.

---

## 5. Environmental information
No non-genetic environmental, lifestyle, or infectious causal contributors were identified in the retrieved evidence for CSS.

---

## 6. Mechanism / pathophysiology

### 6.1 Current mechanistic understanding
CSS is a disorder of chromatin remodeling and transcriptional regulation through disruption of the SWI/SNF (BAF) complex:
- CSS is repeatedly described as caused by mutations affecting **BAF chromatin remodeling complex** components (sekiguchi2019geneticabnormalitiesin pages 1-2, lee2021phenotypicandmolecular pages 1-2, arefeshghi2018bafopathies’dnamethylation pages 1-2).
- The presence of blood DNA methylation episignatures in CSS/BAFopathies supports that perturbation of chromatin remodeling can lead to **systemic, measurable epigenomic consequences** that correlate with genotype and can aid diagnosis (arefeshghi2018bafopathies’dnamethylation pages 1-2).

### 6.2 Causal chain (high-level)
1) Germline pathogenic variant in a BAF/SWI-SNF gene →  
2) altered chromatin remodeling / DNA accessibility →  
3) dysregulated developmental gene expression programs (neurodevelopment, craniofacial, limb/nail, organogenesis) →  
4) multisystem congenital anomalies and neurodevelopmental phenotype (developmental delay/ID, hypotonia, fifth digit/nail hypoplasia, dysmorphisms, brain/cardiac anomalies). (sekiguchi2019geneticabnormalitiesin pages 1-2, lee2021phenotypicandmolecular pages 1-2, arefeshghi2018bafopathies’dnamethylation pages 1-2)

### 6.3 Suggested ontology terms
Because the retrieved evidence does not provide pathway-specific GO enrichments, suggestions are conservative and align with SWI/SNF/BAF biology:
- GO Biological Process: **chromatin remodeling**, **regulation of transcription**, **nervous system development** (supported conceptually by SWI/SNF roles; disease–mechanism link supported by CSS being BAF-related) (lee2021phenotypicandmolecular pages 1-2, arefeshghi2018bafopathies’dnamethylation pages 1-2)
- GO Cellular Component: **SWI/SNF complex / BAF complex** (lee2021phenotypicandmolecular pages 1-2, arefeshghi2018bafopathies’dnamethylation pages 1-2)

Cell Ontology (CL) terms were not directly supported by evidence in the retrieved corpus.

---

## 7. Anatomical structures affected
Evidence supports involvement of multiple systems:
- **Central nervous system (UBERON:0001017)**: brain structural abnormalities and corpus callosum involvement; prenatal CNS malformations recurrent (keskinen2024prenatalcoffinsirissyndrome pages 5-6, ciliberto2023epilepsyincoffin–siris pages 1-2, lee2021phenotypicandmolecular pages 1-2)
- **Cardiovascular system (UBERON:0004535)**: congenital heart defects, including severe prenatal cardiovascular malformations (keskinen2024prenatalcoffinsirissyndrome pages 5-6, huang2024denovovariation pages 1-2)
- **Integument/hair and nails**: sparse scalp hair, hypertrichosis, nail dysplasia (lee2021phenotypicandmolecular pages 1-2, milutinovic2023autismspectrumdisorder pages 1-2)
- **Limbs/digits**: fifth digit distal phalanx/nail hypoplasia/aplasia (sekiguchi2019geneticabnormalitiesin pages 1-2, lee2021phenotypicandmolecular pages 1-2)

Subcellular localization: disease mechanism centers on **nuclear chromatin regulation** (supported by chromatin-remodeling complex etiology) (lee2021phenotypicandmolecular pages 1-2, arefeshghi2018bafopathies’dnamethylation pages 1-2).

---

## 8. Temporal development

### 8.1 Onset
- Typically **congenital/early childhood**, consistent with congenital anomalies and neurodevelopmental delay described across cohorts (sekiguchi2019geneticabnormalitiesin pages 1-2, lee2021phenotypicandmolecular pages 1-2).
- **Prenatal presentations** are increasingly recognized, with recurrent prenatal CNS and cardiac malformations noted and molecular diagnosis in pregnancy becoming more common (keskinen2024prenatalcoffinsirissyndrome pages 5-6).

### 8.2 Progression/course
- Longitudinal/natural history staging is not provided in the retrieved evidence.
- Epilepsy phenotype in registry cases is described as often “relatively easy to control,” suggesting some aspects may be medically manageable, but systematic long-term outcome data are limited in the retrieved excerpts (ciliberto2023epilepsyincoffin–siris pages 5-6).

---

## 9. Inheritance and population

### 9.1 Inheritance
Multiple sources describe CSS as **autosomal dominant**, with many cases arising **de novo**:
- Cohort: CSS is “an autosomal dominant developmental disorder” (sekiguchi2019geneticabnormalitiesin pages 1-2).
- 2024 ARID1B-focused report: CSS is “a rare autosomal dominant inheritance disorder” (huang2024denovovariation pages 1-2).
- Case reports document **de novo heterozygous** pathogenic variants (huang2024denovovariation pages 1-2, milutinovic2023autismspectrumdisorder pages 1-2).

### 9.2 Epidemiology
The retrieved evidence provides limited population-level epidemiology:
- A 2024 ARID1B/CSS report gives an incidence estimate of **1:10,000–1:100,000** (huang2024denovovariation pages 1-2).

No prevalence per 100,000 and no geographic/ethnic prevalence differences were available in the evidence set.

### 9.3 Penetrance/expressivity
While systematic penetrance estimates are not provided in the retrieved evidence, multiple studies emphasize broad phenotypic variability and overlap across SWI/SNF disorders, implying **variable expressivity** (lee2021phenotypicandmolecular pages 1-2, keskinen2024prenatalcoffinsirissyndrome pages 5-6).

---

## 10. Diagnostics

### 10.1 Genetic testing (real-world implementation)
**Current standard diagnostic approach is genomic sequencing (often WES) with confirmatory testing**, supported by multiple contemporary case reports and cohorts:
- A Korean SSRIDD study used whole-exome sequencing of 564 NDD patients to identify 12 SSRIDD cases (including CSS) (lee2021phenotypicandmolecular pages 1-2).
- 2024 ARID1B case report used whole-exome sequencing with Sanger confirmation and functional follow-up (RT-qPCR) (huang2024denovovariation pages 1-2).
- 2023 ASD+CSS case report emphasizes genetic testing for diagnosis confirmation and provides a de novo ARID1B pathogenic variant (milutinovic2023autismspectrumdisorder pages 1-2).

**CNV detection / microdeletions:** Large cohort work included CNVs (e.g., SMARCA2 CNVs) (sekiguchi2019geneticabnormalitiesin pages 1-2), and BAFopathy methylation work notes 6q25 microdeletion syndrome with ARID1B deletions shares a CSS/NCBRS methylation profile (arefeshghi2018bafopathies’dnamethylation pages 1-2), supporting inclusion of CNV assessment in diagnostic workups.

### 10.2 DNA methylation episignatures (advanced diagnostics)
Genome-wide DNA methylation episignatures provide an additional diagnostic layer for CSS/BAFopathies:
- The 2018 Nature Communications paper demonstrates that disease-associated episignatures can “resolve ambiguous clinical cases” and “reclassify those with variants of unknown significance.” (arefeshghi2018bafopathies’dnamethylation pages 1-2)

In practice, this supports incorporation of episignature testing when sequencing yields VUS or when phenotype-genotype fit is uncertain, although the retrieved evidence does not include a CSS-specific 2023–2024 clinical guideline excerpt.

### 10.3 Differential diagnosis
The retrieved evidence indicates notable phenotypic overlap among chromatinopathies and recommends broad surveillance. A 2024 prenatal CSS paper and overlap study emphasize overlap with other epigenetic machinery disorders and that craniofacial/skeletal features may be less detectable prenatally (keskinen2024prenatalcoffinsirissyndrome pages 5-6). (Differential diagnosis lists are not explicitly enumerated in the provided excerpts.)

---

## 11. Outcome / prognosis

### 11.1 Neurologic outcomes (epilepsy)
- Epilepsy prevalence varies by cohort; one ARID1B cohort reported **28.2%** epilepsy (ciliberto2023epilepsyincoffin–siris pages 1-2), while registry-based analyses suggest ascertainment/reporting effects and describe epilepsy as often focal/multifocal and “usually relatively easy to control” (ciliberto2023epilepsyincoffin–siris pages 5-6).

### 11.2 Prenatal outcomes
Prenatal CSS can present with **serious CNS and cardiovascular malformations** and may be associated with severe outcomes including intrauterine death in some reported cases (keskinen2024prenatalcoffinsirissyndrome pages 5-6).

No survival curves, life expectancy estimates, or systematic mortality data were available in the retrieved evidence.

---

## 12. Treatment

### 12.1 Disease-modifying therapy
No disease-modifying pharmacologic therapy for CSS was identified in the retrieved evidence.

### 12.2 Supportive and symptomatic management (current practice)
Direct, detailed multidisciplinary management guidelines were not present in the retrieved excerpt set; however, the syndrome’s multisystem nature and reported complications imply typical real-world management includes:
- developmental therapies (speech/OT/PT),
- management of seizures when present,
- screening and treatment for congenital anomalies (cardiac, CNS, etc.),
- hearing/vision evaluation.

Epilepsy treatment: registry-based review notes that responsiveness data are limited overall but that epilepsy “tends to be focal or multifocal… and usually relatively easy to control” in their series (ciliberto2023epilepsyincoffin–siris pages 5-6).

### 12.3 MAXO term suggestions (non-exhaustive; not directly enumerated in evidence)
Because explicit action ontology mapping was not provided in the evidence, suggestions are generic:
- **MAXO:0001175** (Genetic testing) (for WES/CNV analysis; concept supported) (lee2021phenotypicandmolecular pages 1-2, huang2024denovovariation pages 1-2)
- **MAXO:0000127** (Seizure management) (supported by epilepsy discussion) (ciliberto2023epilepsyincoffin–siris pages 5-6)
- **MAXO:0000013** (Physical therapy), **MAXO:0000014** (Occupational therapy), **MAXO:0000015** (Speech therapy) (consistent with developmental delay; not explicitly mentioned in excerpts)

### 12.4 Clinical trials
A clinical-trials search did not retrieve CSS-specific interventional trials in the current evidence set; trials returned were largely oncology or broad genetic/autism registries rather than CSS-targeted therapeutic studies.

---

## 13. Prevention
Primary prevention is not applicable for most de novo Mendelian CSS cases. Secondary/tertiary prevention in practice involves:
- early genetic diagnosis and anticipatory screening for associated anomalies,
- prenatal diagnosis when a causal variant is detected (noting increasing fetal genetic testing) (keskinen2024prenatalcoffinsirissyndrome pages 5-6).

No vaccine, chemoprophylaxis, or modifiable environmental prevention strategies were identified.

---

## 14. Other species / natural disease
No naturally occurring CSS analogs in non-human species were identified in the retrieved evidence.

---

## 15. Model organisms
The retrieved evidence set did not contain specific model-organism studies of CSS genes; therefore, no model details can be cited from this corpus.

---

## Recent developments and latest research (prioritizing 2023–2024)

### 2023–2024 phenotype expansion and implementation themes
- **Expanded phenotypes and variable presentations:** 2023–2024 case reports highlight diagnostic challenges and expansion into ophthalmologic (early-onset high myopia) and neuropsychiatric (ASD traits) presentations, reinforcing that CSS can initially be recognized outside genetics clinics and requires interdisciplinary assessment plus molecular testing. (milutinovic2023autismspectrumdisorder pages 1-2, huang2024denovovariation pages 1-2)
- **Registry-based quantification of complications:** 2023 registry-based epilepsy work provides gene distribution statistics and characterizes epilepsy subtypes (including a small proportion with Lennox–Gastaut syndrome diagnosis/phenotype), while emphasizing limitations of caregiver-reported registries. (ciliberto2023epilepsyincoffin–siris pages 5-6, ciliberto2023epilepsyincoffin–siris pages 6-6)
- **Prenatal recognition:** 2024 prenatal reports and reviews emphasize recurrent severe prenatal CNS/cardiac malformations and recommend detailed molecular, radiologic, and pathologic examinations, reflecting increasing fetal genetic testing uptake. (keskinen2024prenatalcoffinsirissyndrome pages 5-6)

---

## Limitations of this report (evidence coverage)
- **Identifiers (MONDO/Orphanet/ICD/MeSH)** could not be extracted from the current retrieved literature corpus.
- **Model organism and molecular pathway details** (e.g., specific downstream signaling pathways) were not captured in the available excerpts.
- **Formal management guidelines, QoL measures, and long-term survival statistics** were not present in the retrieved evidence snippets.

---

## Source URLs (as retrieved) and publication dates
Key sources used in the evidence:
- Sekiguchi et al., *Journal of Human Genetics* (Sep 2019). DOI/URL: https://doi.org/10.1038/s10038-019-0667-4 (sekiguchi2019geneticabnormalitiesin pages 1-2)
- Aref-Eshghi et al., *Nature Communications* (Nov 2018). DOI/URL: https://doi.org/10.1038/s41467-018-07193-y (arefeshghi2018bafopathies’dnamethylation pages 1-2)
- Lee et al., *BMC Medical Genomics* (Oct 2021). DOI/URL: https://doi.org/10.1186/s12920-021-01104-9 (lee2021phenotypicandmolecular pages 1-2)
- Ciliberto et al., *American Journal of Medical Genetics Part A* (Sep 2023). DOI/URL: https://doi.org/10.1002/ajmg.a.62979 (ciliberto2023epilepsyincoffin–siris pages 1-2)
- Milutinovic et al., *Frontiers in Psychiatry* (Aug 2023). DOI/URL: https://doi.org/10.3389/fpsyt.2023.1199710 (milutinovic2023autismspectrumdisorder pages 1-2)
- Huang et al., *BMC Medical Genomics* (May 2024). DOI/URL: https://doi.org/10.1186/s12920-024-01904-9 (huang2024denovovariation pages 1-2)
- Keskinen et al., *Pediatric and Developmental Pathology* (Nov 2024). DOI/URL: https://doi.org/10.1177/10935266231210155 (keskinen2024prenatalcoffinsirissyndrome pages 5-6)


References

1. (sekiguchi2019geneticabnormalitiesin pages 1-2): Futoshi Sekiguchi, Yoshinori Tsurusaki, Nobuhiko Okamoto, Keng Wee Teik, Seiji Mizuno, Hiroshi Suzumura, Bertrand Isidor, Winnie Peitee Ong, Muzhirah Haniffa, Susan M. White, Mari Matsuo, Kayoko Saito, Shubha Phadke, Tomoki Kosho, Patrick Yap, Manisha Goyal, Lorne A. Clarke, Rani Sachdev, George McGillivray, Richard J. Leventer, Chirag Patel, Takanori Yamagata, Hitoshi Osaka, Yoshiya Hisaeda, Hirofumi Ohashi, Kenji Shimizu, Keisuke Nagasaki, Junpei Hamada, Sumito Dateki, Takashi Sato, Yasutsugu Chinen, Tomonari Awaya, Takeo Kato, Kougoro Iwanaga, Masahiko Kawai, Takashi Matsuoka, Yoshikazu Shimoji, Tiong Yang Tan, Seema Kapoor, Nerine Gregersen, Massimiliano Rossi, Mathieu Marie-Laure, Lesley McGregor, Kimihiko Oishi, Lakshmi Mehta, Greta Gillies, Paul J. Lockhart, Kate Pope, Anju Shukla, Katta Mohan Girisha, Ghada M. H. Abdel-Salam, David Mowat, David Coman, Ok Hwa Kim, Marie-Pierre Cordier, Kate Gibson, Jeff Milunsky, Jan Liebelt, Helen Cox, Salima El Chehadeh, Annick Toutain, Ken Saida, Hiromi Aoi, Gaku Minase, Naomi Tsuchida, Kazuhiro Iwama, Yuri Uchiyama, Toshifumi Suzuki, Kohei Hamanaka, Yoshiteru Azuma, Atsushi Fujita, Eri Imagawa, Eriko Koshimizu, Atsushi Takata, Satomi Mitsuhashi, Satoko Miyatake, Takeshi Mizuguchi, Noriko Miyake, and Naomichi Matsumoto. Genetic abnormalities in a large cohort of coffin–siris syndrome patients. Journal of Human Genetics, 64:1173-1186, Sep 2019. URL: https://doi.org/10.1038/s10038-019-0667-4, doi:10.1038/s10038-019-0667-4. This article has 86 citations and is from a peer-reviewed journal.

2. (lee2021phenotypicandmolecular pages 1-2): Yena Lee, Yunha Choi, Go Hun Seo, Gu-Hwan Kim, Changwon Keum, Yoo-Mi Kim, Hyo-Sang Do, Jeongmin Choi, In Hee Choi, Han-Wook Yoo, and Beom Hee Lee. Phenotypic and molecular spectra of patients with switch/sucrose nonfermenting complex-related intellectual disability disorders in korea. BMC Medical Genomics, Oct 2021. URL: https://doi.org/10.1186/s12920-021-01104-9, doi:10.1186/s12920-021-01104-9. This article has 6 citations and is from a peer-reviewed journal.

3. (milutinovic2023autismspectrumdisorder pages 1-2): Luka Milutinovic, Roberto Grujicic, Vanja Mandic Maravic, Ivana Joksic, Natasa Ljubomirovic, and Milica Pejovic Milovancevic. Autism spectrum disorder and coffin–siris syndrome—case report. Frontiers in Psychiatry, Aug 2023. URL: https://doi.org/10.3389/fpsyt.2023.1199710, doi:10.3389/fpsyt.2023.1199710. This article has 5 citations.

4. (arefeshghi2018bafopathies’dnamethylation pages 1-2): Erfan Aref-Eshghi, Eric G. Bend, Rebecca L. Hood, Laila C. Schenkel, Deanna Alexis Carere, Rana Chakrabarti, Sandesh C. S. Nagamani, Sau Wai Cheung, Philippe M. Campeau, Chitra Prasad, Victoria Mok Siu, Lauren Brady, Mark A. Tarnopolsky, David J. Callen, A. Micheil Innes, Susan M. White, Wendy S. Meschino, Andrew Y. Shuen, Guillaume Paré, Dennis E. Bulman, Peter J. Ainsworth, Hanxin Lin, David I. Rodenhiser, Raoul C. Hennekam, Kym M. Boycott, Charles E. Schwartz, and Bekim Sadikovic. Bafopathies’ dna methylation epi-signatures demonstrate diagnostic utility and functional continuum of coffin–siris and nicolaides–baraitser syndromes. Nature Communications, Nov 2018. URL: https://doi.org/10.1038/s41467-018-07193-y, doi:10.1038/s41467-018-07193-y. This article has 156 citations and is from a highest quality peer-reviewed journal.

5. (keskinen2024prenatalcoffinsirissyndrome pages 5-6): Sini Keskinen, Teija Paakkola, Mirjami Mattila, Marja Hietala, Hannele Koillinen, Jukka Laine, and Maria K. Haanpää. Prenatal coffin-siris syndrome: expanding the phenotypic and genotypic spectrum of the disease. Pediatric and Developmental Pathology, 27:181-186, Nov 2024. URL: https://doi.org/10.1177/10935266231210155, doi:10.1177/10935266231210155. This article has 10 citations and is from a peer-reviewed journal.

6. (ciliberto2023epilepsyincoffin–siris pages 7-7): Michael Ciliberto, Karen Skjei, Ashley Vasko, and Samantha Schrier Vergano. Epilepsy in coffin–siris syndrome: a report from the international css registry and review of the literature. American Journal of Medical Genetics Part A, 191:22-28, Sep 2023. URL: https://doi.org/10.1002/ajmg.a.62979, doi:10.1002/ajmg.a.62979. This article has 13 citations.

7. (arefeshghi2018bafopathies’dnamethylation pages 14-15): Erfan Aref-Eshghi, Eric G. Bend, Rebecca L. Hood, Laila C. Schenkel, Deanna Alexis Carere, Rana Chakrabarti, Sandesh C. S. Nagamani, Sau Wai Cheung, Philippe M. Campeau, Chitra Prasad, Victoria Mok Siu, Lauren Brady, Mark A. Tarnopolsky, David J. Callen, A. Micheil Innes, Susan M. White, Wendy S. Meschino, Andrew Y. Shuen, Guillaume Paré, Dennis E. Bulman, Peter J. Ainsworth, Hanxin Lin, David I. Rodenhiser, Raoul C. Hennekam, Kym M. Boycott, Charles E. Schwartz, and Bekim Sadikovic. Bafopathies’ dna methylation epi-signatures demonstrate diagnostic utility and functional continuum of coffin–siris and nicolaides–baraitser syndromes. Nature Communications, Nov 2018. URL: https://doi.org/10.1038/s41467-018-07193-y, doi:10.1038/s41467-018-07193-y. This article has 156 citations and is from a highest quality peer-reviewed journal.

8. (huang2024denovovariation pages 1-2): Xiaoyu Huang, Huiping Li, Shangying Yang, Meijiao Ma, Yuanyuan Lian, Xueli Wu, Xiaolong Qi, Xuhui Wang, Weining Rong, and Xunlun Sheng. De novo variation in arid1b gene causes coffin-siris syndrome 1 in a chinese family with excessive early-onset high myopia. BMC Medical Genomics, May 2024. URL: https://doi.org/10.1186/s12920-024-01904-9, doi:10.1186/s12920-024-01904-9. This article has 4 citations and is from a peer-reviewed journal.

9. (ciliberto2023epilepsyincoffin–siris pages 1-2): Michael Ciliberto, Karen Skjei, Ashley Vasko, and Samantha Schrier Vergano. Epilepsy in coffin–siris syndrome: a report from the international css registry and review of the literature. American Journal of Medical Genetics Part A, 191:22-28, Sep 2023. URL: https://doi.org/10.1002/ajmg.a.62979, doi:10.1002/ajmg.a.62979. This article has 13 citations.

10. (ciliberto2023epilepsyincoffin–siris pages 6-6): Michael Ciliberto, Karen Skjei, Ashley Vasko, and Samantha Schrier Vergano. Epilepsy in coffin–siris syndrome: a report from the international css registry and review of the literature. American Journal of Medical Genetics Part A, 191:22-28, Sep 2023. URL: https://doi.org/10.1002/ajmg.a.62979, doi:10.1002/ajmg.a.62979. This article has 13 citations.

11. (ciliberto2023epilepsyincoffin–siris pages 1-1): Michael Ciliberto, Karen Skjei, Ashley Vasko, and Samantha Schrier Vergano. Epilepsy in coffin–siris syndrome: a report from the international css registry and review of the literature. American Journal of Medical Genetics Part A, 191:22-28, Sep 2023. URL: https://doi.org/10.1002/ajmg.a.62979, doi:10.1002/ajmg.a.62979. This article has 13 citations.

12. (ciliberto2023epilepsyincoffin–siris pages 5-6): Michael Ciliberto, Karen Skjei, Ashley Vasko, and Samantha Schrier Vergano. Epilepsy in coffin–siris syndrome: a report from the international css registry and review of the literature. American Journal of Medical Genetics Part A, 191:22-28, Sep 2023. URL: https://doi.org/10.1002/ajmg.a.62979, doi:10.1002/ajmg.a.62979. This article has 13 citations.