---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-04T18:26:49.275409'
end_time: '2026-05-04T18:36:18.807226'
duration_seconds: 569.53
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Arterial Tortuosity Syndrome
  mondo_id: ''
  category: Mendelian
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
- **Disease Name:** Arterial Tortuosity Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Arterial Tortuosity Syndrome** covering all of the
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
- **Disease Name:** Arterial Tortuosity Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Arterial Tortuosity Syndrome** covering all of the
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


# Arterial Tortuosity Syndrome (ATS) — Comprehensive Disease Characteristics Report (Mendelian)

## Target disease
- **Disease name:** Arterial Tortuosity Syndrome (ATS)
- **Category:** Mendelian; heritable connective tissue disorder with primary vascular involvement (beyens2018arterialtortuositysyndrome pages 1-2, esmelvilomara2023arterialtortuositysyndromea pages 1-5)
- **OMIM:** **208050** (esmelvilomara2023arterialtortuositysyndromea pages 1-5)
- **MONDO / Orphanet / ICD-10/ICD-11 / MeSH:** Not verifiable from the retrieved full-text sources in this run; should be filled from OMIM/Orphanet/MONDO directly during curation.

## Executive overview (current understanding)
Arterial Tortuosity Syndrome is an **autosomal recessive** connective tissue disorder caused by **biallelic pathogenic variants in SLC2A10 (GLUT10)** and characterized by **elongation and tortuosity of large- and medium-sized arteries**, often accompanied by **stenoses** and a variable risk of **aneurysm formation** and ischemic complications (beyens2018arterialtortuositysyndrome pages 1-2, esmelvilomara2023arterialtortuositysyndromea pages 1-5). Extra-vascular connective tissue features (craniofacial, skeletal, cutaneous, ocular, and hernia phenotypes) are common and provide diagnostic clues (beyens2018arterialtortuositysyndrome pages 8-9, esmelvilomara2023arterialtortuositysyndromea pages 5-8).

## Evidence snapshot table
| Knowledge-base field | Summary | Key details / frequencies / examples | Source details |
|---|---|---|---|
| Disease name / identifiers | **Arterial Tortuosity Syndrome (ATS)**; OMIM **#208050** | Rare autosomal recessive connective-tissue disorder with elongation/tortuosity of large- and medium-sized arteries; also termed **ATORS** in some recent literature (beyens2018arterialtortuositysyndrome pages 1-2, butnariu2024identificationofgenetic pages 1-2, esmelvilomara2023arterialtortuositysyndromea pages 1-5) | Beyens et al., *Genetics in Medicine*, published **2018-01-11 online / Oct 2018**; DOI: https://doi.org/10.1038/gim.2017.253 (beyens2018arterialtortuositysyndrome pages 1-2). Butnariu et al., *Int J Mol Sci*, **2024-10-17**; DOI: https://doi.org/10.3390/ijms252011173 (butnariu2024identificationofgenetic pages 1-2) |
| Synonyms / alternative names | **Arterial tortuosity syndrome**, **ATS**, **ATORS** | Some resources/papers use “arterial tortuosity syndrome”; HTAD-focused paper abbreviates as **ATORS** (butnariu2024identificationofgenetic pages 1-2, esmelvilomara2023arterialtortuositysyndromea pages 1-5) | Butnariu et al. 2024 https://doi.org/10.3390/ijms252011173; Esmel-Vilomara et al. preprint posted **2022-12-05** / journal article **2023-08** https://doi.org/10.21203/rs.3.rs-2321263/v1 and https://doi.org/10.1016/j.ejmg.2023.104823 (butnariu2024identificationofgenetic pages 1-2, esmelvilomara2023arterialtortuositysyndromea pages 1-5) |
| Core evidence type | Aggregated disease-level and cohort/case-series evidence | Information in the table is derived from aggregated disease cohorts/reviews and individual case series, not EHR-only data (beyens2018arterialtortuositysyndrome pages 1-2, rahmath2025understandingthespectrum pages 4-6, esmelvilomara2023arterialtortuositysyndromea pages 1-5) | Beyens 2018; Rahmath et al., *Biomedicines*, **2025-01** https://doi.org/10.3390/biomedicines13010159; Esmel-Vilomara 2023 (beyens2018arterialtortuositysyndrome pages 1-2, rahmath2025understandingthespectrum pages 4-6, esmelvilomara2023arterialtortuositysyndromea pages 1-5) |
| Causal gene | **SLC2A10** (encodes **GLUT10**) | Loss-of-function / biallelic pathogenic variants cause ATS; GLUT10 is described as an intracellular transporter involved in dehydroascorbic acid/ascorbate biology and connective-tissue homeostasis (beyens2018arterialtortuositysyndrome pages 1-2, beyens2018arterialtortuositysyndrome pages 2-4, esmelvilomara2023arterialtortuositysyndromea pages 1-5) | Beyens 2018 https://doi.org/10.1038/gim.2017.253; Esmel-Vilomara 2023 https://doi.org/10.1016/j.ejmg.2023.104823 (beyens2018arterialtortuositysyndrome pages 1-2, esmelvilomara2023arterialtortuositysyndromea pages 1-5) |
| Inheritance | **Autosomal recessive** | Frequently associated with parental consanguinity: **24/48 (50%)** in Beyens cohort/review (beyens2018arterialtortuositysyndrome pages 8-9) | Beyens et al. 2018 https://doi.org/10.1038/gim.2017.253 (beyens2018arterialtortuositysyndrome pages 8-9) |
| Epidemiology / rarity | Extremely rare | Reported incidence **<1:1,000,000 live births**; Esmel-Vilomara notes **106 genetically confirmed individuals** identified to date at time of study (esmelvilomara2023arterialtortuositysyndromea pages 1-5) | Esmel-Vilomara preprint/journal 2022/2023 https://doi.org/10.21203/rs.3.rs-2321263/v1 and https://doi.org/10.1016/j.ejmg.2023.104823 (esmelvilomara2023arterialtortuositysyndromea pages 1-5) |
| Key vascular phenotype: aortic tortuosity | Hallmark feature | **37/41 (90%)** in Beyens 2018; **21/21 (100%)** in Qatari cohort with p.Ser81Arg (beyens2018arterialtortuositysyndrome pages 8-9, rahmath2025understandingthespectrum pages 4-6) | Beyens 2018 https://doi.org/10.1038/gim.2017.253; Rahmath 2025 https://doi.org/10.3390/biomedicines13010159 (beyens2018arterialtortuositysyndrome pages 8-9, rahmath2025understandingthespectrum pages 4-6) |
| Key vascular phenotype: tortuosity of other arteries | Very common multisite arterial involvement | **38/42 (90%)** in Beyens; **20/21 (95%)** in Rahmath cohort; severe intracranial tortuosity highlighted in 4-patient 2023 series (beyens2018arterialtortuositysyndrome pages 8-9, rahmath2025understandingthespectrum pages 4-6, esmelvilomara2023arterialtortuositysyndromea pages 1-5, esmelvilomara2023arterialtortuositysyndromea pages 5-8) | Beyens 2018; Rahmath 2025; Esmel-Vilomara 2023 (beyens2018arterialtortuositysyndrome pages 8-9, rahmath2025understandingthespectrum pages 4-6, esmelvilomara2023arterialtortuositysyndromea pages 1-5, esmelvilomara2023arterialtortuositysyndromea pages 5-8) |
| Pulmonary artery involvement | Common and clinically important | Pulmonary artery stenosis **23/42 (55%)** in Beyens; pulmonary artery tortuosity **19/21 (90%)** in Rahmath; severe PAS can cause RV hypertension and need intervention (beyens2018arterialtortuositysyndrome pages 8-9, rahmath2025understandingthespectrum pages 4-6, alshair2024totalpulmonaryarterial pages 1-2, alshair2024totalpulmonaryarterial pages 2-5) | Beyens 2018 https://doi.org/10.1038/gim.2017.253; Rahmath 2025 https://doi.org/10.3390/biomedicines13010159; Alshair 2024 https://doi.org/10.1186/s13019-024-02905-6 (beyens2018arterialtortuositysyndrome pages 8-9, rahmath2025understandingthespectrum pages 4-6, alshair2024totalpulmonaryarterial pages 1-2, alshair2024totalpulmonaryarterial pages 2-5) |
| Aortic root aneurysm / aneurysms | Present in a subset, not universal | Aortic root aneurysm **9/42 (21%)** in Beyens overall table; **2/21 (9%)** in Qatari p.Ser81Arg cohort; 2023 4-patient series found no aneurysms in their cases (beyens2018arterialtortuositysyndrome pages 8-9, rahmath2025understandingthespectrum pages 4-6, esmelvilomara2023arterialtortuositysyndromea pages 5-8) | Beyens 2018; Rahmath 2025; Esmel-Vilomara 2023 (beyens2018arterialtortuositysyndrome pages 8-9, rahmath2025understandingthespectrum pages 4-6, esmelvilomara2023arterialtortuositysyndromea pages 5-8) |
| Arterial dissections | Rare / not documented in major series cited | **0/37 (0%)** in Beyens summary; 2023 series notes no confirmed dissections to date in reviewed ATS literature (beyens2018arterialtortuositysyndrome pages 8-9, esmelvilomara2023arterialtortuositysyndrome pages 8-11) | Beyens 2018 https://doi.org/10.1038/gim.2017.253; Esmel-Vilomara 2023 https://doi.org/10.21203/rs.3.rs-2594978/v1 (beyens2018arterialtortuositysyndrome pages 8-9, esmelvilomara2023arterialtortuositysyndrome pages 8-11) |
| Craniofacial features | Frequent syndromic clues | Long face **32/49 (65%)**, high-arched palate **29/44 (66%)**, micrognathia **23/45 (51%)**, sagging cheeks **27/49 (55%)** in Beyens (beyens2018arterialtortuositysyndrome pages 8-9) | Beyens 2018 https://doi.org/10.1038/gim.2017.253 (beyens2018arterialtortuositysyndrome pages 8-9) |
| Skin / connective tissue features | Common extra-vascular signs | Hyperextensible skin **27/46 (50%)**, cutis laxa **21/41 (51%)**, velvety skin **26/41 (63%)** in Beyens; Rahmath found cutaneous findings in **12/21**, including hyperextensible skin in **8/21** (beyens2018arterialtortuositysyndrome pages 8-9, rahmath2025understandingthespectrum pages 4-6) | Beyens 2018; Rahmath 2025 (beyens2018arterialtortuositysyndrome pages 8-9, rahmath2025understandingthespectrum pages 4-6) |
| Skeletal / musculoskeletal features | Common | Joint laxity **36/42 (86%)** in Beyens; Rahmath reported skeletal abnormalities in **15/21**, including joint hypermobility **8/21**, muscular hypotonia **8/21**, pectus excavatum **3/21**, scoliosis **2/21** (beyens2018arterialtortuositysyndrome pages 8-9, rahmath2025understandingthespectrum pages 4-6) | Beyens 2018; Rahmath 2025 (beyens2018arterialtortuositysyndrome pages 8-9, rahmath2025understandingthespectrum pages 4-6) |
| Ocular features | Important but variably expressed | Myopia **15/36 (42%)** and keratoconus **3/38 (8%)** in Beyens; Rahmath: ocular anomalies **7/21**, including astigmatism **5/21**, myopia **2/21**; ophthalmologic baseline exam with keratometry recommended (beyens2018arterialtortuositysyndrome pages 8-9, rahmath2025understandingthespectrum pages 4-6) | Beyens 2018 https://doi.org/10.1038/gim.2017.253; Rahmath 2025 https://doi.org/10.3390/biomedicines13010159 (beyens2018arterialtortuositysyndrome pages 8-9, rahmath2025understandingthespectrum pages 4-6) |
| Hernias / GI-GU findings | Recurrent nonvascular clues | Diaphragmatic hernia **19/65 (29%)**, inguinal hernia **35/92 (38%)**, urogenital abnormalities **11/56 (20%)** in Beyens; Rahmath: inguinal hernia **8/21**, diaphragmatic hernia **7/21**, GERD **5/21** (beyens2018arterialtortuositysyndrome pages 8-9, rahmath2025understandingthespectrum pages 4-6, esmelvilomara2023arterialtortuositysyndromea pages 5-8) | Beyens 2018; Rahmath 2025; Esmel-Vilomara 2023 detailed GU examples (pyelectasis/megaureter) (beyens2018arterialtortuositysyndrome pages 8-9, rahmath2025understandingthespectrum pages 4-6, esmelvilomara2023arterialtortuositysyndromea pages 5-8) |
| Respiratory manifestations | Clinically relevant in infancy/childhood | Beyens: respiratory symptoms **10/67 (15%)** and frequent attention to IRDS; Rahmath: respiratory manifestations **13/21**, recurrent chest infections **8/21**, respiratory distress syndrome **5/21** (beyens2018arterialtortuositysyndrome pages 1-2, rahmath2025understandingthespectrum pages 4-6, beyens2018arterialtortuositysyndrome pages 8-9) | Beyens 2018 https://doi.org/10.1038/gim.2017.253; Rahmath 2025 https://doi.org/10.3390/biomedicines13010159 (beyens2018arterialtortuositysyndrome pages 1-2, rahmath2025understandingthespectrum pages 4-6, beyens2018arterialtortuositysyndrome pages 8-9) |
| Example pathogenic / likely pathogenic variants | Representative recurrent and novel alleles | **c.510G>A (p.Trp170Ter)** homozygous in 3 siblings; **c.417T>A (p.Tyr139Ter)** pathogenic; **c.899T>G (p.Leu300Trp)** novel/likely deleterious in compound heterozygosity; **c.243C>G (p.Ser81Arg)** in 21-patient Qatari cohort associated with relatively mild outcomes (esmelvilomara2023arterialtortuositysyndromea pages 1-5, esmelvilomara2023arterialtortuositysyndromea pages 5-8, rahmath2025understandingthespectrum pages 4-6) | Esmel-Vilomara 2023 https://doi.org/10.1016/j.ejmg.2023.104823 and preprint https://doi.org/10.21203/rs.3.rs-2321263/v1; Rahmath 2025 https://doi.org/10.3390/biomedicines13010159 (esmelvilomara2023arterialtortuositysyndromea pages 1-5, esmelvilomara2023arterialtortuositysyndromea pages 5-8, rahmath2025understandingthespectrum pages 4-6) |
| Recent HTAD testing implementation | ATS detectable via NGS / WES in broader aortopathy workups | 2024 HTAD study identified **compound heterozygous SLC2A10 pathogenic variants** in a patient with ATS using NGS/WES, reinforcing inclusion of **SLC2A10** in syndromic aortopathy testing (butnariu2024identificationofgenetic pages 1-2) | Butnariu et al., *Int J Mol Sci*, **2024-10-17** https://doi.org/10.3390/ijms252011173 (butnariu2024identificationofgenetic pages 1-2) |
| Recommended baseline diagnostic evaluation | Comprehensive vascular and multisystem baseline work-up | Suggested by Beyens: detailed clinical exam, **echocardiography**, **head-to-pelvis MRA**, **ophthalmologic exam with keratometry**, and **renal artery ultrasound** for every ATS patient (beyens2018arterialtortuositysyndrome pages 8-9) | Beyens 2018 https://doi.org/10.1038/gim.2017.253 (beyens2018arterialtortuositysyndrome pages 8-9) |
| Surveillance / monitoring | Serial vascular surveillance required | Case-based radiology review recommends **echocardiography every 3 months until age 5** and then individualized but annual imaging; serial multimodal imaging (CTA/MRA/US) for progression and complications (alkooheji2025radiologicdiagnosisof pages 5-6) | Alkooheji et al., *Cureus*, **2025-12** https://doi.org/10.7759/cureus.99989 (alkooheji2025radiologicdiagnosisof pages 5-6) |
| Imaging hallmarks in practice | CTA/MRA are central real-world diagnostic tools | Radiologic signs include **meandering vessel sign**, **cluster-of-vessels sign**, **aortic elongation sign**, and pulmonary bifurcation **“V/inverted V” signs**; coronal MIP CTA can show tortuous arch branches and thoracic aorta (alkooheji2025radiologicdiagnosisof pages 5-6, kumar2021arterialtortuositysyndrome media cf1c0f36, kumar2021arterialtortuositysyndrome media 75462c90) | Kumar 2021 https://doi.org/10.22468/cvia.2020.00129; Alkooheji 2025 https://doi.org/10.7759/cureus.99989 (kumar2021arterialtortuositysyndrome media cf1c0f36, kumar2021arterialtortuositysyndrome media 75462c90, alkooheji2025radiologicdiagnosisof pages 5-6) |
| Real-world intervention: medical | Empiric **beta-blocker** use | 2023 4-patient series: beta-adrenergic blocking treatment prescribed to reduce hemodynamic stress; authors note efficacy is unproven and management is largely expert-opinion based (esmelvilomara2023arterialtortuositysyndromea pages 1-5, esmelvilomara2023arterialtortuositysyndrome pages 8-11) | Esmel-Vilomara 2023 https://doi.org/10.1016/j.ejmg.2023.104823 and https://doi.org/10.21203/rs.3.rs-2594978/v1 (esmelvilomara2023arterialtortuositysyndromea pages 1-5, esmelvilomara2023arterialtortuositysyndrome pages 8-11) |
| Real-world intervention: surgery | Pulmonary artery reconstruction for severe PAS | In a 2-year-old with ATS, surgical reconstruction performed for severe PAS: pre-op **LPA gradient 73 mmHg, velocity 4.3 m/s; RPA gradient 46 mmHg, velocity 3.4 m/s**; post-repair both branch PA gradients **20 mmHg** at follow-up (alshair2024totalpulmonaryarterial pages 1-2, alshair2024totalpulmonaryarterial pages 2-5) | Alshair et al., *J Cardiothorac Surg*, **2024-07** https://doi.org/10.1186/s13019-024-02905-6 (alshair2024totalpulmonaryarterial pages 1-2, alshair2024totalpulmonaryarterial pages 2-5) |
| Real-world intervention: catheter-based | Balloon dilation can be used for residual focal stenosis | Same 2024 case: postoperative proximal LPA stenosis treated with **8×40 mm Sterling balloon**, reducing peak gradient from about **25 mmHg to 14 mmHg** (alshair2024totalpulmonaryarterial pages 2-5) | Alshair et al. 2024 https://doi.org/10.1186/s13019-024-02905-6 (alshair2024totalpulmonaryarterial pages 2-5) |
| Prognosis | More variable and often milder than first reports suggested | Historical reports cited mortality up to **40% before age 5**, but larger later cohorts indicate a **milder course** and no mortality in the 21-patient Qatari p.Ser81Arg cohort (beyens2018arterialtortuositysyndrome pages 1-2, esmelvilomara2023arterialtortuositysyndromea pages 1-5, rahmath2025understandingthespectrum pages 4-6) | Beyens 2018; Esmel-Vilomara 2023; Rahmath 2025 (beyens2018arterialtortuositysyndrome pages 1-2, esmelvilomara2023arterialtortuositysyndromea pages 1-5, rahmath2025understandingthespectrum pages 4-6) |


*Table: This table summarizes core disease-knowledge fields for Arterial Tortuosity Syndrome, including identifiers, genetics, phenotype frequencies, diagnostics, surveillance, and real-world interventions. It is useful as a structured evidence-backed snapshot for populating a rare disease knowledge base entry.*

---

## 1. Disease information
### 1.1 Definition and key concepts
- **Core vascular concept (arterial tortuosity):** abnormal twisting/turning and elongation of arteries leading to altered hemodynamics and potential downstream stenosis/ischemia (beyens2018arterialtortuositysyndrome pages 1-2, esmelvilomara2023arterialtortuositysyndromea pages 1-5).
- **Syndromic context:** ATS is one of the heritable connective tissue/aortopathy syndromes where tortuosity is part of a broader multisystem phenotype (alkooheji2025radiologicdiagnosisof pages 5-6, beyens2018arterialtortuositysyndrome pages 8-9).

### 1.2 Synonyms / alternative names
- **Arterial tortuosity syndrome**, **ATS**.
- **ATORS** is used in some hereditary thoracic aortic disease (HTAD) testing literature to denote arterial tortuosity syndrome (butnariu2024identificationofgenetic pages 1-2).

### 1.3 Evidence provenance (patient-level vs aggregated)
- Aggregated disease-level evidence: large cohort + literature review (2018) (beyens2018arterialtortuositysyndrome pages 1-2, beyens2018arterialtortuositysyndrome pages 8-9).
- Patient-level series enabling HPO mapping and rare feature expansion: 4-patient series (posted 2022-12-05; later journal publication Aug 2023) (esmelvilomara2023arterialtortuositysyndromea pages 1-5, esmelvilomara2023arterialtortuositysyndromea pages 5-8) and cohort of 21 genetically confirmed Qatari patients (2025) (rahmath2025understandingthespectrum pages 4-6).

**Recent developments (2023–2024 emphasis):** New variant reports and expanded phenotype capture via modern sequencing (clinical exome/WES) and systematic imaging were described in 2023, and incorporation of SLC2A10 into broader HTAD NGS/WES workflows was explicitly illustrated in 2024 (esmelvilomara2023arterialtortuositysyndromea pages 1-5, butnariu2024identificationofgenetic pages 1-2).

---

## 2. Etiology
### 2.1 Disease causal factors
- **Primary cause:** biallelic loss-of-function / pathogenic variants in **SLC2A10**, encoding **GLUT10** (beyens2018arterialtortuositysyndrome pages 1-2, esmelvilomara2023arterialtortuositysyndromea pages 1-5).
- **Inheritance:** autosomal recessive; consanguinity is frequent in reported families (24/48; 50% in one large series) (beyens2018arterialtortuositysyndrome pages 8-9).

### 2.2 Risk factors
- **Genetic:** carrying two pathogenic alleles in SLC2A10 is causal (beyens2018arterialtortuositysyndrome pages 1-2, esmelvilomara2023arterialtortuositysyndromea pages 1-5).
- **Family structure:** high frequency of parental consanguinity in cohorts indicates increased recurrence risk in consanguineous families (beyens2018arterialtortuositysyndrome pages 8-9).
- **Environmental/lifestyle:** No validated environmental risk factors or gene–environment interactions were identified in the retrieved ATS-specific sources.

### 2.3 Protective factors
- No established protective genetic or environmental factors were identified in the retrieved sources.

### 2.4 Gene–environment interactions
- Not established in the retrieved ATS literature.

---

## 3. Phenotypes (clinical spectrum)
### 3.1 Typical onset and course
ATS often presents **in infancy/childhood**, including neonatal manifestations such as pulmonary artery stenosis and respiratory distress in some patients (alshair2024totalpulmonaryarterial pages 2-5, beyens2018arterialtortuositysyndrome pages 1-2). Natural history is heterogeneous; early reports described high early mortality, but later cohorts suggest a **milder course in many patients** (beyens2018arterialtortuositysyndrome pages 1-2, esmelvilomara2023arterialtortuositysyndromea pages 1-5).

### 3.2 Vascular phenotypes (with frequencies where available)
From a large cohort/literature synthesis (Beyens 2018):
- **Aortic tortuosity:** 37/41 (90%) (beyens2018arterialtortuositysyndrome pages 8-9)
- **Tortuosity of other arteries:** 38/42 (90%) (beyens2018arterialtortuositysyndrome pages 8-9)
- **Pulmonary artery stenosis:** 23/42 (55%) (beyens2018arterialtortuositysyndrome pages 8-9)
- **Aortic root aneurysm:** 9/42 (21%) (beyens2018arterialtortuositysyndrome pages 8-9)
- **Arterial dissections:** 0/37 (0%) (beyens2018arterialtortuositysyndrome pages 8-9)

From a 21-patient genetically confirmed Qatari cohort (Rahmath 2025; homozygous p.Ser81Arg):
- **Aortic tortuosity:** 21/21 (100%)
- **Other arterial tortuosity:** 20/21 (95%)
- **Pulmonary artery tortuosity:** 19/21 (90%)
- **Aortic root aneurysm:** 2/21 (9%)
- **Cardiovascular interventions:** 2/21 (9%) (rahmath2025understandingthespectrum pages 4-6)

### 3.3 Extra-vascular phenotypes and HPO suggestions
Below are common phenotypes and representative HPO terms (examples; not exhaustive).

**Craniofacial / dysmorphism** (common diagnostic clues)
- Long face **HP:0000276**; hypertelorism **HP:0000316**; downslanted palpebral fissures **HP:0000494**; high arched/narrow palate **HP:0002705**; micrognathia **HP:0000347**; sagging cheeks **HP:0034273** (beyens2018arterialtortuositysyndrome pages 8-9, esmelvilomara2023arterialtortuositysyndromea pages 5-8).

**Cutaneous / connective tissue**
- Hyperextensible skin **HP:0000974**; cutis laxa **HP:0000973**; velvety skin texture (phenotyped in cohort tables) (beyens2018arterialtortuositysyndrome pages 8-9).

**Musculoskeletal**
- Joint hypermobility **HP:0001382**; pectus excavatum **HP:0000767**; scoliosis **HP:0002650**; pes planus **HP:0001763**; pes valgus **HP:0008081** (beyens2018arterialtortuositysyndrome pages 8-9, esmelvilomara2023arterialtortuositysyndromea pages 5-8).

**Ocular**
- Myopia **HP:0000545**; keratoconus **HP:0000563**; keratoglobus (as reported in cohort tables); exotropia **HP:0000577**; myopic astigmatism **HP:0500041** (beyens2018arterialtortuositysyndrome pages 8-9, esmelvilomara2023arterialtortuositysyndromea pages 5-8).

**Hernias / GI**
- Diaphragmatic hernia **HP:0000776**; inguinal hernia **HP:0000023**; gastroesophageal reflux disease (GERD) (reported in cohort summaries) (beyens2018arterialtortuositysyndrome pages 8-9, rahmath2025understandingthespectrum pages 4-6, esmelvilomara2023arterialtortuositysyndromea pages 5-8).

**Genitourinary / renal**
- Dilatation of renal pelvis **HP:0010946**; congenital megaureter **HP:0008676**; cryptorchidism **HP:0000028**; urogenital abnormalities (reported at cohort level) (beyens2018arterialtortuositysyndrome pages 8-9, esmelvilomara2023arterialtortuositysyndromea pages 5-8).

**Neurologic / imaging-associated findings**
- Intracranial/cerebrovascular tortuosity **HP:0005116** (vascular HPO); corpus callosum hypoplasia **HP:0002079**; temporal cortical atrophy **HP:0007112** in individual cases (esmelvilomara2023arterialtortuositysyndromea pages 5-8).

### 3.4 Quality of life impact
No validated QoL instrument outcomes (e.g., SF-36/EQ-5D) were reported in the retrieved ATS-specific sources. However, vascular stenosis (especially pulmonary arteries) can produce major functional limitation via right ventricular hypertension and reduced exercise tolerance (alshair2024totalpulmonaryarterial pages 2-5).

---

## 4. Genetic / molecular information
### 4.1 Causal gene
- **SLC2A10** (GLUT10) is the established causal gene for ATS (beyens2018arterialtortuositysyndrome pages 1-2, esmelvilomara2023arterialtortuositysyndromea pages 1-5).

### 4.2 Pathogenic variants (examples from recent and key studies)
- **c.510G>A (p.Trp170Ter)** (homozygous) in a consanguineous sibling set (esmelvilomara2023arterialtortuositysyndromea pages 1-5, esmelvilomara2023arterialtortuositysyndromea pages 5-8).
- **c.417T>A (p.Tyr139Ter)** (pathogenic) with **c.899T>G (p.Leu300Trp)** (novel missense, deleterious prediction) in compound heterozygosity (esmelvilomara2023arterialtortuositysyndromea pages 1-5).
- **c.243C>G (p.Ser81Arg)** (homozygous) in 21 Qatari patients; reported in association with relatively mild outcomes and no mortality in that cohort (rahmath2025understandingthespectrum pages 4-6).

**Variant interpretation framework:** The 2022/2023 series describes ACMG-guideline-based classification and segregation testing (Sanger) after exome sequencing (esmelvilomara2023arterialtortuositysyndromea pages 1-5).

### 4.3 Modifier genes / epigenetics
- No validated modifier genes were identified in the retrieved sources.
- Epigenetic regulation is discussed as a mechanistic hypothesis (via dioxygenases and demethylation biology), but disease-specific epigenomic signatures were not provided (esmelvilomara2023arterialtortuositysyndromea pages 1-5).

### 4.4 Chromosomal abnormalities
- Not a typical feature; ATS is primarily monogenic due to SLC2A10 biallelic variants in the sources reviewed.

---

## 5. Environmental information
ATS is a Mendelian disorder; no specific toxins, lifestyle factors, or infectious triggers were established as causal or modifying factors in the retrieved sources.

---

## 6. Mechanism / pathophysiology (causal chain)
### 6.1 Proposed molecular mechanism (current understanding)
A convergent model from cohort and case-series sources is:
1) **SLC2A10 (GLUT10) deficiency** → perturbed intracellular handling of **dehydroascorbic acid/ascorbate** (hypothesis) (esmelvilomara2023arterialtortuositysyndromea pages 1-5, beyens2018arterialtortuositysyndrome pages 2-4).
2) In the **endoplasmic reticulum**, reduced ascorbate cofactor availability may impair **prolyl/lysyl hydroxylase** activity and **collagen/elastin maturation/crosslinking** (esmelvilomara2023arterialtortuositysyndromea pages 1-5).
3) In **mitochondria**, altered ascorbate biology may impair **redox homeostasis** and reactive oxygen species scavenging (esmelvilomara2023arterialtortuositysyndromea pages 1-5, beyens2018arterialtortuositysyndrome pages 2-4).
4) These perturbations contribute to **extracellular matrix (ECM) homeostasis defects** and elastic lamellar integrity loss, leading to **fragmentation of elastic fibers/lamellae** in arterial walls (beyens2018arterialtortuositysyndrome pages 1-2, beyens2018arterialtortuositysyndrome pages 2-4).
5) Structural arterial wall weakness + abnormal remodeling → **arterial elongation/tortuosity**, **stenosis** (potentially via smooth muscle proliferation), and variable aneurysm risk (beyens2018arterialtortuositysyndrome pages 8-9, beyens2018arterialtortuositysyndrome pages 1-2).

### 6.2 TGF-β signaling
- TGF-β pathway involvement is described as uncertain/complex. One cohort reports that “skin and end-stage diseased vascular tissue do not indicate increased TGF-β signaling” (immunohistochemistry for pSMAD2/CTGF), while other hypotheses link GLUT10/DHA to TGF-β upregulation (beyens2018arterialtortuositysyndrome pages 1-2, esmelvilomara2023arterialtortuositysyndromea pages 1-5).
- A zebrafish morpholino model is referenced as suggesting reduced TGF-β signaling during early development (beyens2018arterialtortuositysyndrome pages 2-4).

### 6.3 Tissue pathology (human)
- Skin and vascular biopsies show **fragmented elastic fibers** and **increased collagen deposition**; EM demonstrates a fragmented elastin core with peripheral microfibrils of random directionality (beyens2018arterialtortuositysyndrome pages 1-2).

### 6.4 Suggested ontology annotations
**GO biological processes (examples):**
- extracellular matrix organization (GO)
- elastic fiber assembly (GO)
- collagen fibril organization (GO)
- response to oxidative stress (GO)
- transforming growth factor beta receptor signaling pathway (GO; mechanistic hypothesis/uncertain directionality)

**Cell types (CL, examples):**
- vascular smooth muscle cell (CL)
- endothelial cell (CL)
- fibroblast (CL)

**Anatomy (UBERON, examples):**
- aorta (UBERON)
- pulmonary artery (UBERON)
- carotid artery / cerebral arteries (UBERON)
- renal artery (UBERON)

**Chemical entities (ChEBI, examples):**
- ascorbic acid (vitamin C) / dehydroascorbic acid (ChEBI)

---

## 7. Anatomical structures affected
### 7.1 Organ/system level
- **Primary system:** cardiovascular (aorta and medium-sized arteries; pulmonary arteries; supra-aortic and cerebrovascular vessels commonly involved) (beyens2018arterialtortuositysyndrome pages 8-9, esmelvilomara2023arterialtortuositysyndromea pages 5-8).
- **Secondary systems:** ocular (myopia/keratoconus/keratoglobus), musculoskeletal (hypermobility, pectus, scoliosis), skin/connective tissue, GI (hernia/GERD), and GU (urogenital anomalies) (beyens2018arterialtortuositysyndrome pages 8-9, rahmath2025understandingthespectrum pages 4-6, esmelvilomara2023arterialtortuositysyndromea pages 5-8).

### 7.2 Imaging-based localization (real-world)
Classic radiologic patterns include markedly tortuous great vessels and pulmonary artery branching signs (“V/inverted V”), visualized by CTA/MRA (kumar2021arterialtortuositysyndrome media cf1c0f36, kumar2021arterialtortuositysyndrome media 75462c90).

---

## 8. Temporal development
- **Onset:** often congenital/neonatal to childhood; pulmonary artery stenosis can present as a newborn and progress to require intervention (alshair2024totalpulmonaryarterial pages 1-2, alshair2024totalpulmonaryarterial pages 2-5).
- **Progression/course:** variable; later cohorts indicate many individuals survive beyond early childhood, but early aneurysm/stenosis surveillance is recommended (beyens2018arterialtortuositysyndrome pages 1-2).

---

## 9. Inheritance and population
- **Inheritance:** autosomal recessive (beyens2018arterialtortuositysyndrome pages 1-2, esmelvilomara2023arterialtortuositysyndromea pages 1-5).
- **Consanguinity:** 24/48 (50%) in one large cohort/review; indicates strong enrichment in consanguineous pedigrees (beyens2018arterialtortuositysyndrome pages 8-9).
- **Population/variant distribution:** A homozygous p.Ser81Arg cohort in Qatar suggests a regional/founder contribution (rahmath2025understandingthespectrum pages 4-6).
- **Prevalence/incidence:** incidence cited as **<1:1,000,000 live births** in a recent case series; reliable prevalence estimates are unavailable (esmelvilomara2023arterialtortuositysyndromea pages 1-5).
- **Carrier frequency:** not provided in retrieved texts (requires gnomAD/other population databases).

---

## 10. Diagnostics
### 10.1 Clinical suspicion
Syndromic pattern recognition—arterial tortuosity with characteristic craniofacial/connective tissue findings and hernias—should prompt genetic evaluation (beyens2018arterialtortuositysyndrome pages 8-9, esmelvilomara2023arterialtortuositysyndromea pages 1-5).

### 10.2 Imaging (current applications)
- **CTA/MRA** are central to diagnosis and longitudinal surveillance for tortuosity, stenoses, and aneurysms (alkooheji2025radiologicdiagnosisof pages 5-6).
- **Imaging hallmarks and signs:** meandering vessel sign, cluster-of-vessels sign, aortic elongation sign, and pulmonary artery “V/inverted V” signs are described in radiology-focused case literature; representative CTA figures demonstrating these findings were retrieved (alkooheji2025radiologicdiagnosisof pages 5-6, kumar2021arterialtortuositysyndrome media cf1c0f36, kumar2021arterialtortuositysyndrome media 75462c90).

### 10.3 Recommended baseline evaluation (expert practice from cohort study)
A large ATS cohort recommends baseline evaluation including:
- detailed clinical exam,
- echocardiography,
- “head-to-pelvis” MR angiography,
- ophthalmologic exam with keratometry,
- renal artery ultrasound (beyens2018arterialtortuositysyndrome pages 8-9).

### 10.4 Genetic testing strategy
- **Preferred:** sequencing of **SLC2A10** (single gene or CTD/aortopathy panels) with CNV assessment and segregation testing as needed (esmelvilomara2023arterialtortuositysyndromea pages 1-5).
- **Real-world implementation:** broader aortopathy/HTAD pipelines using **NGS panel testing or WES** can identify compound heterozygous SLC2A10 variants and enable genotype–phenotype correlation workups (butnariu2024identificationofgenetic pages 1-2).

### 10.5 Differential diagnosis
Key differentials for arterial tortuosity with syndromic features include:
- Loeys–Dietz syndrome, Marfan syndrome, vascular Ehlers–Danlos syndrome, cutis laxa, and homocystinuria (alkooheji2025radiologicdiagnosisof pages 5-6).

---

## 11. Outcome / prognosis
- **Mortality and survival:** Early literature cited mortality up to **40% before age 5**, but later cohorts report a milder overall course (beyens2018arterialtortuositysyndrome pages 1-2, esmelvilomara2023arterialtortuositysyndromea pages 1-5). A 21-patient cohort with homozygous p.Ser81Arg reported **no mortality** (rahmath2025understandingthespectrum pages 4-6).
- **Major morbidity drivers:** arterial stenoses (especially pulmonary), aneurysm formation in a subset, and ischemic events; however, a large 2018 cohort observed **0 dissections** among those tabulated (beyens2018arterialtortuositysyndrome pages 8-9).

---

## 12. Treatment
### 12.1 Pharmacotherapy / medical management
- **Beta-adrenergic blockade** is used empirically to reduce hemodynamic stress on arterial walls; efficacy is not established and practice is largely extrapolated from other aortopathies (esmelvilomara2023arterialtortuositysyndromea pages 1-5, esmelvilomara2023arterialtortuositysyndrome pages 8-11).

**MAXO suggestions (examples):** beta-adrenergic antagonist therapy; cardiovascular surveillance.

### 12.2 Surgical and interventional management (real-world implementation)
A 2024 surgical case illustrates management of severe pulmonary artery stenosis in ATS:
- Preoperative echo gradients: **LPA 73 mmHg (4.3 m/s)**; **RPA 46 mmHg (3.4 m/s)** with right ventricular hypertension; surgical reconstruction performed at age 2 (alshair2024totalpulmonaryarterial pages 1-2).
- Postoperative: branch PA gradients ~**20 mmHg** (alshair2024totalpulmonaryarterial pages 1-2).
- Residual proximal LPA stenosis was treated via **balloon angioplasty (8×40 mm)** with peak gradient reduced from ~**25 mmHg to 14 mmHg** (alshair2024totalpulmonaryarterial pages 2-5).

**MAXO suggestions (examples):** pulmonary artery reconstruction; balloon angioplasty; perioperative cardiopulmonary bypass.

### 12.3 Experimental / clinical trials
No ATS-specific interventional trials were retrieved. A large **observational** aortopathy biorepository/genetics study explicitly includes ATS among conditions studied:
- **NCT03440697** (Yale University; first posted **2018-02-22**, last update posted **2026-02-13**; start 2015-12-10; estimated completion 2030-12-31) (NCT03440697 chunk 1).

---

## 13. Prevention
- **Primary prevention:** For autosomal recessive ATS, the practical prevention lever is **genetic counseling** and reproductive risk reduction in high-risk families/communities; the Qatari cohort emphasizes counseling aimed at preventing cousin marriage (consanguinity) to reduce disease occurrence (rahmath2025understandingthespectrum pages 4-6).
- **Secondary/tertiary prevention:** structured imaging surveillance and blood pressure management to prevent complications (expert-opinion driven) (alkooheji2025radiologicdiagnosisof pages 5-6, beyens2018arterialtortuositysyndrome pages 8-9).

---

## 14. Other species / natural disease
No naturally occurring ATS orthologous disease in other species was identified in the retrieved sources.

---

## 15. Model organisms
- A zebrafish morpholino model is referenced as suggesting altered (reduced) TGF-β signaling during early development, but detailed model characterization was not retrievable within the available text excerpts (beyens2018arterialtortuositysyndrome pages 2-4).

---

## Expert opinions and analysis (authoritative synthesis)
- **Guidelines gap:** Multiple sources explicitly note that ATS natural history remains incompletely studied and that **formal clinical practice guidelines are lacking**, so management relies heavily on expert opinion and extrapolation (beyens2018arterialtortuositysyndrome pages 1-2, esmelvilomara2023arterialtortuositysyndromea pages 1-5).
- **Key clinical priority (consensus across sources):** early identification of stenoses/aneurysms and longitudinal imaging surveillance (head-to-pelvis vascular imaging) is repeatedly emphasized (beyens2018arterialtortuositysyndrome pages 1-2, beyens2018arterialtortuositysyndrome pages 8-9, alkooheji2025radiologicdiagnosisof pages 5-6).
- **Mechanistic uncertainty:** authoritative cohort work shows strong tissue-level ECM pathology, while molecular pathway attribution (e.g., directionality of TGF-β signaling changes) remains unresolved and may be context-dependent (beyens2018arterialtortuositysyndrome pages 1-2, esmelvilomara2023arterialtortuositysyndromea pages 1-5).

---

## Statistics and data highlights (recent and landmark)
- **Consanguinity:** 24/48 (50%) in Beyens cohort/review (2018) (beyens2018arterialtortuositysyndrome pages 8-9).
- **Aortic tortuosity:** 37/41 (90%) in Beyens (2018) and 21/21 (100%) in Qatari cohort (2025) (beyens2018arterialtortuositysyndrome pages 8-9, rahmath2025understandingthespectrum pages 4-6).
- **Pulmonary artery stenosis:** 23/42 (55%) in Beyens (2018) (beyens2018arterialtortuositysyndrome pages 8-9).
- **Aortic root aneurysm:** 9/42 (21%) in Beyens (2018) vs 2/21 (9%) in Qatari cohort (2025) (beyens2018arterialtortuositysyndrome pages 8-9, rahmath2025understandingthespectrum pages 4-6).
- **Arterial dissections:** 0/37 in Beyens tabulated cohort (2018) (beyens2018arterialtortuositysyndrome pages 8-9).
- **Intervention outcomes (case data, 2024):** marked reduction in pulmonary artery gradients after reconstruction and ballooning (alshair2024totalpulmonaryarterial pages 1-2, alshair2024totalpulmonaryarterial pages 2-5).

---

## Notes on citation requirements (PMID availability)
The retrieved full-text sources in this run provided DOIs/URLs and detailed data but did not expose PubMed IDs within the accessible text. For knowledge-base ingestion requiring PMIDs, the recommended next step is to map these DOIs to PMIDs via PubMed/NCBI records during curation.


References

1. (beyens2018arterialtortuositysyndrome pages 1-2): Aude Beyens, Juliette Albuisson, Annekatrien Boel, Mazen Al-Essa, Waheed Al-Manea, Damien Bonnet, Ozlem Bostan, Odile Boute, Tiffany Busa, Nathalie Canham, Ergun Cil, Paul J. Coucke, Margot A. Cousin, Majed Dasouki, Julie De Backer, Anne De Paepe, Sofie De Schepper, Deepthi De Silva, Koenraad Devriendt, Inge De Wandele, David R. Deyle, Harry Dietz, Sophie Dupuis-Girod, Eudice Fontenot, Björn Fischer-Zirnsak, Alper Gezdirici, Jamal Ghoumid, Fabienne Giuliano, Neus Baena Diéz, Mohammed Z. Haider, Joshua S. Hardin, Xavier Jeunemaitre, Eric W. Klee, Uwe Kornak, Manuel F. Landecho, Anne Legrand, Bart Loeys, Stanislas Lyonnet, Helen Michael, Pamela Moceri, Shehla Mohammed, Laura Muiño-Mosquera, Sheela Nampoothiri, Karin Pichler, Katrina Prescott, Anna Rajeb, Maria Ramos-Arroyo, Massimiliano Rossi, Mustafa Salih, Mohammed Z. Seidahmed, Elise Schaefer, Elisabeth Steichen-Gersdorf, Sehime Temel, Fahrettin Uysal, Marine Vanhomwegen, Lut Van Laer, Lionel Van Maldergem, David Warner, Andy Willaert, Tom R. Collins, Andrea Taylor, Elaine C. Davis, Yuri Zarate, and Bert Callewaert. Arterial tortuosity syndrome: 40 new families and literature review. Genetics in Medicine, 20:1236-1245, Oct 2018. URL: https://doi.org/10.1038/gim.2017.253, doi:10.1038/gim.2017.253. This article has 113 citations and is from a highest quality peer-reviewed journal.

2. (esmelvilomara2023arterialtortuositysyndromea pages 1-5): Roger Esmel-Vilomara, Irene Valenzuela, Lucía Riaza, Benjamín Rodríguez-Santiago, Ferran Rosés-Noguer, Susana Boronat, and Anna Sabaté-Rotés. Arterial tortuosity syndrome: phenotypic features and cardiovascular manifestations in 4 newly identified patients. European journal of medical genetics, pages 104823, Aug 2023. URL: https://doi.org/10.1016/j.ejmg.2023.104823, doi:10.1016/j.ejmg.2023.104823. This article has 1 citations and is from a peer-reviewed journal.

3. (beyens2018arterialtortuositysyndrome pages 8-9): Aude Beyens, Juliette Albuisson, Annekatrien Boel, Mazen Al-Essa, Waheed Al-Manea, Damien Bonnet, Ozlem Bostan, Odile Boute, Tiffany Busa, Nathalie Canham, Ergun Cil, Paul J. Coucke, Margot A. Cousin, Majed Dasouki, Julie De Backer, Anne De Paepe, Sofie De Schepper, Deepthi De Silva, Koenraad Devriendt, Inge De Wandele, David R. Deyle, Harry Dietz, Sophie Dupuis-Girod, Eudice Fontenot, Björn Fischer-Zirnsak, Alper Gezdirici, Jamal Ghoumid, Fabienne Giuliano, Neus Baena Diéz, Mohammed Z. Haider, Joshua S. Hardin, Xavier Jeunemaitre, Eric W. Klee, Uwe Kornak, Manuel F. Landecho, Anne Legrand, Bart Loeys, Stanislas Lyonnet, Helen Michael, Pamela Moceri, Shehla Mohammed, Laura Muiño-Mosquera, Sheela Nampoothiri, Karin Pichler, Katrina Prescott, Anna Rajeb, Maria Ramos-Arroyo, Massimiliano Rossi, Mustafa Salih, Mohammed Z. Seidahmed, Elise Schaefer, Elisabeth Steichen-Gersdorf, Sehime Temel, Fahrettin Uysal, Marine Vanhomwegen, Lut Van Laer, Lionel Van Maldergem, David Warner, Andy Willaert, Tom R. Collins, Andrea Taylor, Elaine C. Davis, Yuri Zarate, and Bert Callewaert. Arterial tortuosity syndrome: 40 new families and literature review. Genetics in Medicine, 20:1236-1245, Oct 2018. URL: https://doi.org/10.1038/gim.2017.253, doi:10.1038/gim.2017.253. This article has 113 citations and is from a highest quality peer-reviewed journal.

4. (esmelvilomara2023arterialtortuositysyndromea pages 5-8): Roger Esmel-Vilomara, Irene Valenzuela, Lucía Riaza, Benjamín Rodríguez-Santiago, Ferran Rosés-Noguer, Susana Boronat, and Anna Sabaté-Rotés. Arterial tortuosity syndrome: phenotypic features and cardiovascular manifestations in 4 newly identified patients. European journal of medical genetics, pages 104823, Aug 2023. URL: https://doi.org/10.1016/j.ejmg.2023.104823, doi:10.1016/j.ejmg.2023.104823. This article has 1 citations and is from a peer-reviewed journal.

5. (butnariu2024identificationofgenetic pages 1-2): Lăcrămioara Ionela Butnariu, Georgiana Russu, Alina-Costina Luca, Constantin Sandu, Laura Mihaela Trandafir, Ioana Vasiliu, Setalia Popa, Gabriela Ghiga, Laura Bălănescu, and Elena Țarcă. Identification of genetic variants associated with hereditary thoracic aortic diseases (htads) using next generation sequencing (ngs) technology and genotype–phenotype correlations. International Journal of Molecular Sciences, 25:11173, Oct 2024. URL: https://doi.org/10.3390/ijms252011173, doi:10.3390/ijms252011173. This article has 4 citations.

6. (rahmath2025understandingthespectrum pages 4-6): Muhammed Riyas K. Rahmath, Haytham Ibrahim, Muhammad Faiyaz-Ul-Haque, Zafar Nawaz, Ahmad Zitoun, Ahmed Hussein, Ahmed Sadek, Ayman El-Menyar, Reema Kamal, Hassan Al-Thani, and Gulab Sher. Understanding the spectrum of mild clinical outcomes and novel findings in arterial tortuosity syndrome among qatari patients: implications of slc2a10 mutation. Biomedicines, 13:159, Jan 2025. URL: https://doi.org/10.3390/biomedicines13010159, doi:10.3390/biomedicines13010159. This article has 2 citations.

7. (beyens2018arterialtortuositysyndrome pages 2-4): Aude Beyens, Juliette Albuisson, Annekatrien Boel, Mazen Al-Essa, Waheed Al-Manea, Damien Bonnet, Ozlem Bostan, Odile Boute, Tiffany Busa, Nathalie Canham, Ergun Cil, Paul J. Coucke, Margot A. Cousin, Majed Dasouki, Julie De Backer, Anne De Paepe, Sofie De Schepper, Deepthi De Silva, Koenraad Devriendt, Inge De Wandele, David R. Deyle, Harry Dietz, Sophie Dupuis-Girod, Eudice Fontenot, Björn Fischer-Zirnsak, Alper Gezdirici, Jamal Ghoumid, Fabienne Giuliano, Neus Baena Diéz, Mohammed Z. Haider, Joshua S. Hardin, Xavier Jeunemaitre, Eric W. Klee, Uwe Kornak, Manuel F. Landecho, Anne Legrand, Bart Loeys, Stanislas Lyonnet, Helen Michael, Pamela Moceri, Shehla Mohammed, Laura Muiño-Mosquera, Sheela Nampoothiri, Karin Pichler, Katrina Prescott, Anna Rajeb, Maria Ramos-Arroyo, Massimiliano Rossi, Mustafa Salih, Mohammed Z. Seidahmed, Elise Schaefer, Elisabeth Steichen-Gersdorf, Sehime Temel, Fahrettin Uysal, Marine Vanhomwegen, Lut Van Laer, Lionel Van Maldergem, David Warner, Andy Willaert, Tom R. Collins, Andrea Taylor, Elaine C. Davis, Yuri Zarate, and Bert Callewaert. Arterial tortuosity syndrome: 40 new families and literature review. Genetics in Medicine, 20:1236-1245, Oct 2018. URL: https://doi.org/10.1038/gim.2017.253, doi:10.1038/gim.2017.253. This article has 113 citations and is from a highest quality peer-reviewed journal.

8. (alshair2024totalpulmonaryarterial pages 1-2): Fahad M. Alshair, Amal S. Alsulami, Mohammad S. Shihata, Osman O. Alradi, Ragab S. Debis, Abdullah H. Baghaffar, and Mazin A. Fatani. Total pulmonary arterial reconstruction in a patient with arterial tortuosity syndrome affecting the pulmonary artery: a case report and review of the literature. Journal of Cardiothoracic Surgery, Jul 2024. URL: https://doi.org/10.1186/s13019-024-02905-6, doi:10.1186/s13019-024-02905-6. This article has 2 citations and is from a peer-reviewed journal.

9. (alshair2024totalpulmonaryarterial pages 2-5): Fahad M. Alshair, Amal S. Alsulami, Mohammad S. Shihata, Osman O. Alradi, Ragab S. Debis, Abdullah H. Baghaffar, and Mazin A. Fatani. Total pulmonary arterial reconstruction in a patient with arterial tortuosity syndrome affecting the pulmonary artery: a case report and review of the literature. Journal of Cardiothoracic Surgery, Jul 2024. URL: https://doi.org/10.1186/s13019-024-02905-6, doi:10.1186/s13019-024-02905-6. This article has 2 citations and is from a peer-reviewed journal.

10. (esmelvilomara2023arterialtortuositysyndrome pages 8-11): Roger Esmel-Vilomara, Irene Valenzuela, Lucia Riaza, Benjamin Rodriguez-Santiago, Ferran Roses-Noguer, Susana Boronat, and Anna Sabate-Rotes. Arterial tortuosity syndrome: phenotypic and cardiovascular features in 4 newly identified patients. Feb 2023. URL: https://doi.org/10.21203/rs.3.rs-2594978/v1, doi:10.21203/rs.3.rs-2594978/v1.

11. (alkooheji2025radiologicdiagnosisof pages 5-6): Amina Salah Alkooheji, Neale Nicola Kalis, G. Koç, Suad R. Alamer, and Vimalarani Arulselvam. Radiologic diagnosis of arterial tortuosity syndrome in a pediatric patient: a case report. Cureus, Dec 2025. URL: https://doi.org/10.7759/cureus.99989, doi:10.7759/cureus.99989. This article has 0 citations.

12. (kumar2021arterialtortuositysyndrome media cf1c0f36): Parveen Kumar. Arterial tortuosity syndrome: a case report and literature review. Cardiovascular Imaging Asia, 5:9, Jan 2021. URL: https://doi.org/10.22468/cvia.2020.00129, doi:10.22468/cvia.2020.00129. This article has 4 citations.

13. (kumar2021arterialtortuositysyndrome media 75462c90): Parveen Kumar. Arterial tortuosity syndrome: a case report and literature review. Cardiovascular Imaging Asia, 5:9, Jan 2021. URL: https://doi.org/10.22468/cvia.2020.00129, doi:10.22468/cvia.2020.00129. This article has 4 citations.

14. (NCT03440697 chunk 1):  Pathogenetic Basis of Aortopathy and Aortic Valve Disease. Yale University. 2015. ClinicalTrials.gov Identifier: NCT03440697