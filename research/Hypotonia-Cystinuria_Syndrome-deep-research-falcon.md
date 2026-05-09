---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T12:19:05.347729'
end_time: '2026-05-08T12:33:11.471680'
duration_seconds: 846.12
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypotonia-cystinuria syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypotonia-cystinuria syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypotonia-cystinuria syndrome** covering all of the
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
- **Disease Name:** Hypotonia-cystinuria syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypotonia-cystinuria syndrome** covering all of the
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


## Comprehensive Disease Characteristics Research Report: Hypotonia–cystinuria syndrome (HCS)

### Executive summary
Hypotonia–cystinuria syndrome (HCS) is a very rare autosomal recessive contiguous-gene deletion disorder at chromosome 2p21, classically due to biallelic deletions disrupting **SLC3A1** (type I cystinuria) and **PREPL** (neuromuscular/growth phenotype), producing neonatal/infantile hypotonia and biochemical cystinuria with risk of cystine nephrolithiasis. The condition sits on a deletion-size spectrum in 2p21 in which larger deletions (e.g., including **CAMKMT/C2orf34** and/or **PPM1B**) can produce more severe multisystem disease. (eggermann20122p21deletionsin pages 1-2, eggermann2012cystinuriaaninborn pages 6-8, kılıc2018firstcardiacmanifestation pages 1-3, chabrol2008deletionofc2orf34 pages 2-3)

| Item type | Value | Source (author/year/journal) | URL/DOI | Notes |
|---|---|---|---|---|
| Identifier | OMIM 606407 | Eggermann et al., 2012, *European Journal of Medical Genetics* | https://doi.org/10.1016/j.ejmg.2012.06.008 | HCS explicitly cited as “HCS; OMIM 606407”; autosomal recessive condition caused by 2p21 deletions disrupting **SLC3A1** and **PREPL** (eggermann20122p21deletionsin pages 1-2) |
| Identifier | OMIM 606407 | Kılıç et al., 2018, *Metabolic Brain Disease* | https://doi.org/10.1007/s11011-018-0226-2 | Described as a “very rare autosomal recessive contiguous gene deletion disorder” due to combined microdeletions of **SLC3A1** and **PREPL** at chromosome 2p21 (kılıc2018firstcardiacmanifestation pages 1-3) |
| Synonym | Hypotonia-cystinuria syndrome | Jaeken et al., 2006, *American Journal of Human Genetics* | https://doi.org/10.1086/498852 | Foundational naming paper referring to “the hypotonia-cystinuria syndrome”; associated with microdeletion involving 2p21 region and PREPL deletion (eggermann2012cystinuriaaninborn pages 6-8) |
| Synonym | HCS | Eggermann et al., 2012, *European Journal of Medical Genetics* | https://doi.org/10.1016/j.ejmg.2012.06.008 | Common abbreviation used in peer-reviewed literature for hypotonia-cystinuria syndrome (eggermann20122p21deletionsin pages 1-2) |
| Synonym | Hypotonia–cystinuria 2p21 deletion syndrome | Towheed et al., 2021, *Annals of Clinical and Translational Neurology* | https://doi.org/10.1002/acn3.51464 | Used for cases with homozygous 2p21 deletion involving **SLC3A1** and **PREPL**; emphasizes chromosomal-deletion mechanism and intrafamilial variability (eggermann20122p21deletionsin pages 1-2) |
| Definition | Rare autosomal recessive contiguous-gene deletion syndrome characterized by neonatal/infantile hypotonia and type I (type A) cystinuria | Eggermann et al., 2012, *European Journal of Medical Genetics* | https://doi.org/10.1016/j.ejmg.2012.06.008 | Core lesion: chromosome 2p21 deletions disrupting **SLC3A1** and **PREPL**; common features include generalized neonatal hypotonia, failure to thrive, growth retardation, and cystinuria (eggermann20122p21deletionsin pages 1-2) |
| Definition | Syndromic form of cystinuria associated with homozygous contiguous deletions at 2p21 affecting at least **SLC3A1** and **PREPL** | Eggermann et al., 2012, *Orphanet Journal of Rare Diseases* | https://doi.org/10.1186/1750-1172-7-19 | Reported hallmarks: generalized hypotonia at birth, failure to thrive, growth retardation, cystinuria/nephrolithiasis; 13 patients and 5 different HCS deletions noted in review (eggermann2012cystinuriaaninborn pages 6-8) |
| Definition | Very rare autosomal recessive contiguous gene deletion disorder caused by combined microdeletions of **SLC3A1** and **PREPL** on chromosome 2p21 | Kılıç et al., 2018, *Metabolic Brain Disease* | https://doi.org/10.1007/s11011-018-0226-2 | Additional commonly reported features include feeding problems, developmental delay, growth hormone deficiency, nephrolithiasis, and minor dysmorphism (kılıc2018firstcardiacmanifestation pages 1-3) |
| Definition | Contiguous-gene disorder linked to 2p21 deletions disrupting **SLC3A1** and **PREPL**, with phenotype intermediate to larger 2p21 deletion syndromes when only these two genes are involved | Martens et al., 2008, *Current Molecular Medicine* | https://doi.org/10.2174/156652408785747997 | Larger deletions including **PPM1B** and/or **C2orf34/CAMKMT** produce more severe related syndromes; HCS specifically refers to deletions including **SLC3A1** and **PREPL** (martens2008multisystemdisordersyndromes pages 2-3, chabrol2008deletionofc2orf34 pages 2-3) |
| Synonym/Related term | Atypical hypotonia–cystinuria syndrome | Chabrol et al., 2008, *Journal of Medical Genetics* | https://doi.org/10.1136/jmg.2007.055475 | Related but distinct phenotype caused by deletion encompassing **SLC3A1**, **PREPL**, and **C2orf34/CAMKMT**; useful for differential nomenclature, not identical to classic HCS (chabrol2008deletionofc2orf34 pages 2-3) |


*Table: This table summarizes the key disease identifiers, accepted names, and core disease definition for hypotonia-cystinuria syndrome using only supported evidence from the retrieved literature. It is useful for normalizing terminology and linking HCS to its characteristic 2p21 contiguous-gene deletion mechanism.*

| Genetic lesion category | Genes involved (HGNC symbols) | Genomic region | Typical zygosity / inheritance | Reported deletion sizes / ranges | Key phenotypic correlates | Key diagnostic methods | Key sources (author/year) with DOI/URL |
|---|---|---|---|---|---|---|---|
| Classic HCS contiguous-gene deletion | **SLC3A1**, **PREPL** | 2p21 | Usually homozygous; autosomal recessive | ~38–127 kb across reported HCS deletions | Generalized neonatal hypotonia, failure to thrive, growth retardation, cystinuria / nephrolithiasis | Urine amino acid analysis; Sanger failure to amplify deleted exons; SNP microarray / molecular karyotyping | Eggermann 2012, *Eur J Med Genet*; DOI: 10.1016/j.ejmg.2012.06.008; https://doi.org/10.1016/j.ejmg.2012.06.008 (eggermann20122p21deletionsin pages 1-2) |
| Classic HCS contiguous-gene deletion (reviewed series) | **SLC3A1**, **PREPL** | 2p21 | Homozygous contiguous deletions; recessive disease mechanism | Five different deletions; approximately ~38–127 kb; 13 reported patients | Hypotonia at birth, failure to thrive, growth retardation, cystinuria / nephrolithiasis | Molecular screening for **SLC3A1** defects; deletion analysis in cystinuria workup | Eggermann 2012, *Orphanet J Rare Dis*; DOI: 10.1186/1750-1172-7-19; https://doi.org/10.1186/1750-1172-7-19 (eggermann2012cystinuriaaninborn pages 6-8) |
| Atypical HCS with larger deletion | **SLC3A1**, **PREPL**, **C2orf34/CAMKMT** | 2p21 | Familial genomic deletion; recessive presentation | Breakpoints mapped from **SLC3A1** intron 4 to **C2orf34** intron 1; exact total size not stated in excerpt | Severe neonatal hypotonia, poor sucking requiring nasogastric feeding, delayed motor milestones, psychomotor/growth retardation, cystinuria with nephrolithiasis | Urinary amino acid chromatography; qPCR breakpoint mapping; junction-fragment sequencing | Chabrol 2008, *J Med Genet*; DOI: 10.1136/jmg.2007.055475; https://doi.org/10.1136/jmg.2007.055475 (chabrol2008deletionofc2orf34 pages 2-3) |
| HCS / related 2p21 deletion spectrum | **SLC3A1**, **PREPL**; larger related deletions may include **PPM1B** and **C2orf34/CAMKMT** | 2p21 | HCS: recessive contiguous-gene disorder; larger deletions associated with more severe related syndromes | Initial HCS series identified recurrent deletions; severe related syndrome reported with ~179 kb homozygous deletion | HCS: neonatal/infantile hypotonia, poor feeding, GH deficiency, type I cystinuria; larger deletions: neonatal seizures, severe developmental delay | Genetic testing for 2p21 deletions and **SLC3A1/PREPL** analysis | Martens 2008, *Curr Mol Med*; DOI: 10.2174/156652408785747997; https://doi.org/10.2174/156652408785747997 (martens2008multisystemdisordersyndromes pages 2-3) |
| Very rare autosomal recessive HCS due to combined microdeletions | **SLC3A1**, **PREPL** (sometimes discussion includes neighboring genes in differential / expanded deletions) | 2p21 | Homozygous combined microdeletion; autosomal recessive | Not quantified in excerpt; deletion detected by chromosomal microarray | Infantile hypotonia, feeding problems, failure to thrive, short stature / GH deficiency, developmental delay, cystinuria type A; cardiac involvement reported as unusual extension | Metabolic testing; urinary amino acid analysis; chromosomal microarray; echocardiography for extrarenal evaluation | Kılıç 2018, *Metab Brain Dis*; DOI: 10.1007/s11011-018-0226-2; https://doi.org/10.1007/s11011-018-0226-2 (kılıc2018firstcardiacmanifestation pages 1-3, kılıc2018firstcardiacmanifestation pages 4-5) |
| Intrafamilial variable HCS with exon-level deletion | **SLC3A1** (exons 2–10), **PREPL** (exons 2–14) | 2p21 | Homozygous deletion; recessive | Exon-level deletion reported; bp size not given in excerpt | Congenital hypotonia, lactic acidosis, failure to thrive in infancy; later divergence to cystinuria/nephrolithiasis vs chronic neurobehavioral disturbance | Whole-exome sequencing revealing homozygous 2p21 deletion; muscle biopsy / respiratory chain studies in differential workup | Towheed 2021, *Ann Clin Transl Neurol*; DOI: 10.1002/acn3.51464; https://doi.org/10.1002/acn3.51464 (eggermann20122p21deletionsin pages 1-2) |
| Rare compound heterozygous mechanism within HCS spectrum | **SLC3A1**, **PREPL** plus separate **SLC3A1** deletion on other allele | 2p21 | Compound heterozygous at locus; functionally biallelic disruption | Not stated | Syndromic cystinuria with HCS phenotype supports need to evaluate CNVs plus single-gene defects | Screening cystinuria patients for **SLC3A1** mutations / deletions; deletion analysis | Eggermann 2012, *Orphanet J Rare Dis*; DOI: 10.1186/1750-1172-7-19; https://doi.org/10.1186/1750-1172-7-19 (eggermann2012cystinuriaaninborn pages 6-8) |
| Mechanistic interpretation of classic HCS | **SLC3A1** loss explains type I cystinuria; **PREPL** loss implicated in hypotonia / growth phenotype | 2p21 | Recessive contiguous-gene loss | Recurrent deletions summarized in reported families | Renal amino acid transport defect with cystinuria from **SLC3A1** deficiency; neuromuscular / growth manifestations linked to **PREPL** deficiency | Combined biochemical and molecular testing; deletion-focused assays when syndromic features coexist with cystinuria | Eggermann 2012; Martens 2008; Kılıç 2018 (eggermann20122p21deletionsin pages 1-2, martens2008multisystemdisordersyndromes pages 2-3, kılıc2018firstcardiacmanifestation pages 1-3) |


*Table: This table summarizes the known molecular basis of hypotonia-cystinuria syndrome across classic and atypical 2p21 deletion presentations. It is useful for linking gene content, deletion class, phenotype, and the most informative diagnostic methods in reported cases.*

---

## 1. Disease information

### 1.1 What is the disease?
HCS is described as a “very rare autosomal recessive contiguous gene deletion disorder” caused by combined microdeletions of **SLC3A1** and **PREPL** on chromosome 2p21, characterized by neonatal/infantile hypotonia and cystinuria (type A/type I) with nephrolithiasis risk, alongside growth and neurodevelopmental features. (eggermann20122p21deletionsin pages 1-2, kılıc2018firstcardiacmanifestation pages 1-3)

A key clinical caveat reported in case-based literature is that kidney stones may be absent in early infancy, which can delay diagnosis if clinicians do not recognize the syndromic combination of hypotonia + biochemical cystinuria. (taroni2019acaseof pages 2-3)

### 1.2 Key identifiers (best-available from retrieved sources)
* **OMIM:** 606407 (explicitly used in multiple peer-reviewed sources) (eggermann20122p21deletionsin pages 1-2, kılıc2018firstcardiacmanifestation pages 1-3)
* **ICD-10/ICD-11 / MeSH / MONDO / Orphanet:** Not available in the retrieved corpus using the provided tools; therefore not reported here.

### 1.3 Synonyms / alternative names
* Hypotonia–cystinuria syndrome; HCS (eggermann20122p21deletionsin pages 1-2, kılıc2018firstcardiacmanifestation pages 1-3)
* Hypotonia–cystinuria 2p21 deletion syndrome (used in literature emphasizing exon-level deletions and phenotypic variability) (eggermann20122p21deletionsin pages 1-2)
* Related term (distinct entity): **Atypical hypotonia–cystinuria syndrome** (deletion includes **SLC3A1–PREPL–CAMKMT/C2orf34**) (chabrol2008deletionofc2orf34 pages 2-3)

### 1.4 Evidence provenance (patient-level vs aggregated)
The HCS knowledge base evidence is largely derived from:
* **Patient-level reports and small series** defining deletion structure and clinical spectrum (e.g., atypical deletions; case reports with additional malformations). (chabrol2008deletionofc2orf34 pages 2-3, taroni2019acaseof pages 2-3)
* **Aggregated reviews** summarizing number of reported cases and deletion classes (e.g., 13 reported HCS patients with five deletion classes). (eggermann2012cystinuriaaninborn pages 6-8)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** biallelic disruption of the 2p21 region affecting at least **SLC3A1** and **PREPL** (most often homozygous deletions), causing combined renal amino-acid transport defect (cystinuria type I) and neuromuscular/growth phenotype. (eggermann20122p21deletionsin pages 1-2, eggermann2012cystinuriaaninborn pages 6-8, kılıc2018firstcardiacmanifestation pages 1-3)

**Deletion-size spectrum / mechanistic stratification:**
* **Classic HCS:** SLC3A1 + PREPL deletions (~38–127 kb). (eggermann20122p21deletionsin pages 1-2, eggermann2012cystinuriaaninborn pages 6-8)
* **Atypical HCS:** deletion includes **CAMKMT/C2orf34** in addition to SLC3A1 + PREPL, with severe hypotonia/feeding difficulty and developmental delay. (chabrol2008deletionofc2orf34 pages 2-3)
* **Larger 2p21 deletions:** inclusion of **PPM1B** is associated with more severe phenotypes (e.g., neonatal seizures, severe global developmental delay in related syndromes), consistent with gene-content modifying disease expression. (eggermann20122p21deletionsin pages 1-2, eggermann2012cystinuriaaninborn pages 6-8)

### 2.2 Risk factors
* **Genetic risk:** autosomal recessive inheritance with homozygous or compound-heterozygous disruption at 2p21 involving SLC3A1 and PREPL. (eggermann20122p21deletionsin pages 1-2, eggermann2012cystinuriaaninborn pages 6-8)
* **Family structure:** consanguinity is frequently present in recessive deletion syndromes in general; specific quantitative risk estimates were not extractable from the retrieved corpus.

### 2.3 Protective factors / gene–environment interactions
No HCS-specific protective factors or explicit gene–environment interactions were identified in the retrieved corpus. For the cystinuria component, conservative measures that reduce urinary cystine supersaturation (high urine volume, alkalinization, dietary sodium restriction) are widely described as preventive strategies for stone formation and recurrence. (d’ambrosio2022cystinuriaanupdate pages 1-3, d’ambrosio2022cystinuriaanupdate pages 4-5)

---

## 3. Phenotypes (clinical spectrum)

### 3.1 Core phenotype domains (human)
From clinical series and reviews, the most consistently reported features include:

**Neuromuscular / neurodevelopmental**
* **Generalized neonatal hypotonia** (HP:0001252) (eggermann20122p21deletionsin pages 1-2, eggermann2012cystinuriaaninborn pages 6-8, kılıc2018firstcardiacmanifestation pages 1-3)
* **Feeding difficulties / poor sucking** (HP:0011968 / HP:0002039), sometimes requiring nasogastric feeding in severe presentations (chabrol2008deletionofc2orf34 pages 2-3)
* **Developmental delay** (HP:0001263) (kılıc2018firstcardiacmanifestation pages 1-3, taroni2019acaseof pages 2-3)

**Growth / endocrine**
* **Failure to thrive** (HP:0001508) and **growth retardation/short stature** (HP:0004322) (eggermann20122p21deletionsin pages 1-2, eggermann2012cystinuriaaninborn pages 6-8, kılıc2018firstcardiacmanifestation pages 1-3)
* **Growth hormone deficiency** (HP:0000824) is repeatedly cited as part of the phenotype; growth response to GH therapy is noted in reviews (martens2008multisystemdisordersyndromes pages 2-3, boonen2011preplaprolyl pages 1-3)

**Renal / metabolic (cystinuria type I/type A)**
* **Cystinuria / hyperexcretion of dibasic amino acids in urine** (HP:0003355; also consider “Aminoaciduria” HP:0003354) (eggermann20122p21deletionsin pages 1-2, chabrol2008deletionofc2orf34 pages 2-3)
* **Nephrolithiasis (cystine stones)** (HP:0000787). A case report documented stone analysis as “100% cystine” and provided a markedly elevated cystine/creatinine ratio (676 mMol/mol; normal 4–15). (taroni2019acaseof pages 2-3)

**Other reported/expanded features (case-based)**
* Congenital anomalies of kidney and urinary tract (CAKUT) including **primary obstructed megaureter** (HP:0000079/HP:0002015-related), **cryptorchidism** (HP:0000028), and cardiac findings (e.g., patent foramen ovale with atrial septal aneurysm in one case report). (taroni2019acaseof pages 2-3)
* **Cardiac involvement** (rare): a report described left ventricular non-compaction/dilated cardiomyopathy in HCS. (kılıc2018firstcardiacmanifestation pages 1-3)

**Phenotype frequency / statistics**
Quantitative phenotype frequencies are limited in the retrieved corpus. One review excerpt indicates broad clinical patterns across reported families and notes a finite number of reported deletions and families, but does not provide per-phenotype percentages in the retrieved text. (boonen2011preplaprolyl pages 1-3, eggermann2012cystinuriaaninborn pages 6-8)

### 3.2 Age of onset and progression
* **Onset:** typically **congenital/neonatal** for hypotonia and feeding problems; cystinuria is biochemical and may precede overt stone disease. (eggermann20122p21deletionsin pages 1-2, taroni2019acaseof pages 2-3)
* **Progression:** renal stone disease may emerge later in childhood; intrafamilial variability is described, with divergence in later childhood manifestations even with the same deletion. (eggermann20122p21deletionsin pages 1-2)

### 3.3 Quality of life impact
No standardized QoL instrument results (e.g., PedsQL, PROMIS) were extractable for HCS specifically; however, cystine stone disease is described as requiring chronic prevention and often repeated surgical interventions in cystinuria reviews, implying sustained morbidity. (d’ambrosio2022cystinuriaanupdate pages 1-3)

### 3.4 Suggested ontology mappings
**HPO (examples):**
* HP:0001252 Hypotonia
* HP:0001508 Failure to thrive
* HP:0001263 Global developmental delay
* HP:0000787 Nephrolithiasis
* HP:0003355 Cystinuria (or HP:0003354 Aminoaciduria)
* HP:0000028 Cryptorchidism (reported in one case)

---

## 4. Genetic / molecular information

### 4.1 Causal genes and molecular lesion types
**Primary causal genes (contiguous deletion):**
* **SLC3A1** (cystinuria type I) and **PREPL** (hypotonia/growth phenotype contribution) in the classic HCS definition. (eggermann20122p21deletionsin pages 1-2, eggermann2012cystinuriaaninborn pages 6-8, kılıc2018firstcardiacmanifestation pages 1-3)

**Variant class:**
* Predominantly **copy-number losses (microdeletions)** at **2p21**, usually **homozygous**; compound heterozygosity (deletion on one allele plus another deletion in SLC3A1) is also described within the HCS/cystinuria spectrum. (eggermann2012cystinuriaaninborn pages 6-8)

**Deletion size / gene content:**
* Reported HCS deletions range approximately **~38–127 kb** and consistently affect **SLC3A1** and **PREPL** in the retrieved sources. (eggermann20122p21deletionsin pages 1-2, eggermann2012cystinuriaaninborn pages 6-8)
* Larger deletions including additional genes (e.g., **CAMKMT/C2orf34**, **PPM1B**) define related syndromes and can worsen phenotype severity. (eggermann2012cystinuriaaninborn pages 6-8, chabrol2008deletionofc2orf34 pages 2-3)

### 4.2 Functional consequences (current understanding)
* **SLC3A1** encodes the heavy subunit (rBAT) of the renal transporter system responsible for reabsorption of cystine and dibasic amino acids; loss causes cystinuria and cystine stone formation. (d’ambrosio2022cystinuriaanupdate pages 1-3)
* **PREPL** is described as encoding a putative serine oligopeptidase-like protein; loss is implicated in hypotonia and growth issues in HCS, and PREPL enzyme activity testing is being operationalized in clinical research settings. (eggermann20122p21deletionsin pages 1-2, NCT02263781 chunk 1)

### 4.3 Modifier genes, epigenetics
No HCS-specific modifier genes or epigenetic mechanisms were identified in the retrieved corpus; deletion gene-content effects (e.g., inclusion of PPM1B) function as a structural “modifier” via contiguous gene loss. (eggermann2012cystinuriaaninborn pages 6-8)

---

## 5. Environmental information
HCS itself is genetic. No external environmental triggers were identified. For the cystinuria component, dietary sodium/protein and hydration status are recognized modifiers of stone risk in cystinuria reviews and are targeted in management. (d’ambrosio2022cystinuriaanupdate pages 4-5)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (integrated)
1. **Genetic trigger:** homozygous (or compound heterozygous) 2p21 deletion disrupting **SLC3A1** and **PREPL**. (eggermann20122p21deletionsin pages 1-2, eggermann2012cystinuriaaninborn pages 6-8)
2. **Renal transport defect:** SLC3A1 loss impairs proximal tubular reabsorption of cystine/dibasic amino acids → elevated urinary cystine. (d’ambrosio2022cystinuriaanupdate pages 1-3)
3. **Biophysical precipitation:** cystine has low solubility at physiologic urine pH → supersaturation leads to crystal formation and cystine stones. (d’ambrosio2022cystinuriaanupdate pages 1-3)
4. **Clinical renal phenotype:** recurrent nephrolithiasis, potential obstructive uropathy and interventions. (taroni2019acaseof pages 2-3)
5. **Neuromuscular phenotype:** PREPL loss is implicated in congenital/neonatal hypotonia, feeding difficulty, and growth/endocrine issues, though the precise biochemical pathway is incompletely defined in the retrieved corpus. (eggermann20122p21deletionsin pages 1-2, NCT02263781 chunk 1)

### 6.2 Suggested GO / CL terms (best-effort mappings)
**GO biological processes (examples):**
* Amino acid transmembrane transport
* Renal tubule development / kidney development (for CAKUT cases)
* Skeletal muscle contraction / neuromuscular process controlling balance

**Cell Ontology (CL) candidates:**
* Renal proximal tubular epithelial cell
* Skeletal muscle fiber / myocyte

(These ontology suggestions are conceptual mappings; the retrieved corpus did not provide explicit GO/CL term annotations.)

---

## 7. Anatomical structures affected

### Organ/tissue systems (inferred from clinical phenotype)
* **Kidney/urinary tract** (nephrolithiasis; obstructive megaureter in a case) (UBERON:0002113 kidney; UBERON:0000056 ureter) (taroni2019acaseof pages 2-3)
* **Skeletal muscle / neuromuscular system** (hypotonia) (UBERON:0001134 skeletal muscle organ) (eggermann20122p21deletionsin pages 1-2, kılıc2018firstcardiacmanifestation pages 1-3)
* **Endocrine axis** (growth hormone deficiency) (UBERON:0000007 pituitary gland) (kılıc2018firstcardiacmanifestation pages 1-3)
* **Heart** (rare involvement in case reports) (UBERON:0000948 heart) (kılıc2018firstcardiacmanifestation pages 1-3)

---

## 8. Temporal development (natural history)
* **Neonatal period:** hypotonia and feeding difficulty often dominate early presentation. (eggermann20122p21deletionsin pages 1-2, chabrol2008deletionofc2orf34 pages 2-3)
* **Infancy/childhood:** cystinuria may be present biochemically; nephrolithiasis can develop later; variable neurobehavioral or other features may become apparent. (eggermann20122p21deletionsin pages 1-2, taroni2019acaseof pages 2-3)

---

## 9. Inheritance and population

### 9.1 Inheritance
HCS is consistently described as **autosomal recessive**, most often due to **homozygous deletions** at 2p21 involving SLC3A1 and PREPL. (eggermann20122p21deletionsin pages 1-2, kılıc2018firstcardiacmanifestation pages 1-3)

### 9.2 Epidemiology (best-available)
Formal prevalence/incidence estimates for HCS are not robust in the retrieved corpus. One report provides a model-based estimate tied to a deletion allele frequency (“reported incidence … 1/1000000 for an allele frequency of 1/1000 for deletion B”). (kılıc2018firstcardiacmanifestation pages 1-3)

A review also summarized that “Thirteen HCS patients have been reported” and “five different HCS deletions have been identified,” indicating extreme rarity and reliance on reported cases. (eggermann2012cystinuriaaninborn pages 6-8)

---

## 10. Diagnostics

### 10.1 Clinical and laboratory diagnosis
Key tests used in case reports and reviews include:
* **Urinary amino acid analysis / chromatography** showing increased cystine, lysine, arginine, ornithine (cystinuria biochemical signature). (eggermann20122p21deletionsin pages 1-2, chabrol2008deletionofc2orf34 pages 2-3)
* **Stone analysis** (when stones are present), e.g., “100% cystine” in one case report. (taroni2019acaseof pages 2-3)

### 10.2 Genetic testing
Given that HCS is a CNV-driven contiguous-gene disorder, informative methods include:
* **Chromosomal microarray / SNP microarray / molecular karyotyping** to detect and size 2p21 deletions. (eggermann20122p21deletionsin pages 1-2, kılıc2018firstcardiacmanifestation pages 1-3)
* **MLPA** targeted to SLC3A1/PREPL deletions (used in a case report). (taroni2019acaseof pages 2-3)
* **qPCR and breakpoint sequencing** for detailed deletion characterization (atypical HCS). (chabrol2008deletionofc2orf34 pages 2-3)

### 10.3 Differential diagnosis
Because early HCS can present with hypotonia and feeding difficulties, differential workups may include neuromuscular disorders or syndromes with hypotonia/FTT; a review notes that overlap may prompt exclusion of Prader–Willi syndrome in practice. (boonen2011preplaprolyl pages 1-3)

---

## 11. Outcome / prognosis
HCS-specific long-term survival and renal outcomes data were not extractable as population statistics from the retrieved corpus. Case-level data indicate that early recognition may influence neurologic and renal outcomes by enabling earlier cystinuria prevention strategies and appropriate supportive therapies. (taroni2019acaseof pages 2-3)

---

## 12. Treatment

### 12.1 Management principles (renal/stone prevention; extrapolated from cystinuria evidence)
Because HCS includes type I cystinuria, standard cystinuria therapy is directly relevant:
* **High urine volume + alkalinization as first-line:** A 2024 systematic review states that first-line therapies “including high fluid intake and urinary alkalinization, increased urine volume to >3 L/day and urinary pH >7.0,” and were associated with reduced urinary cystine levels and cystine stone formation. (bhatt2024pharmacologicalinterventionsfor pages 1-3)
* **Second-line cystine-binding thiol drugs:** The same review reports second-line therapy with “tiopronin and D-penicillamine” reduced urinary cystine and stone formation/recurrence. (bhatt2024pharmacologicalinterventionsfor pages 1-3)

**Example quantitative outcomes (cystinuria literature):** tiopronin-treated adults had lower urinary cystine than untreated (154.3 mg/L vs 422.4 mg/L, p=0.004), and adherence was associated with higher stone-free rates (73% vs 33%). (bhatt2024pharmacologicalinterventionsfor pages 10-11)

### 12.2 HCS case-based implementations
A case report of HCS with CAKUT used:
* **Potassium citrate** (alkalinization) and **tiopronin 15 mg/kg/day**, plus urologic surgeries for obstructive uropathy and stone management (nephrolithotripsy/stone removal). (taroni2019acaseof pages 2-3)

### 12.3 Growth / hypotonia management
Reviews of the HCS phenotype report growth hormone deficiency as a common feature and note that GH therapy can improve growth outcomes (statement summarized in reviews; quantitative effect sizes not extractable from the retrieved corpus). (martens2008multisystemdisordersyndromes pages 2-3, boonen2011preplaprolyl pages 1-3)

### 12.4 Experimental/clinical research (trials)
Two ClinicalTrials.gov studies directly address PREPL deficiency (including HCS):

* **NCT02640443 (Phase 2):** “Sulfamethoxazole for the Treatment of Primary PREPL Deficiency” evaluates whether sulfamethoxazole improves PREPL deficiency symptoms; dosing is oral sulfamethoxazole 60 mg/kg/day (max 3 g) for 3 weeks, with outcomes centered on ptosis/facial indices and broader neuromuscular/neuropsychological and renal ultrasound endpoints. (NCT02640443 chunk 1)

  **Direct quote (registry):** the objective is “to evaluate whether sulfamethoxazole … improves symptoms of PREPL deficiency.” (NCT02640443 chunk 1)

* **NCT02263781 (diagnostic/physiology):** “PREPL in Health and Disease” measures PREPL enzyme activity in blood (and in a subset, muscle) to establish normal pediatric values and compare PREPL activity across controls, Prader–Willi syndrome, and primary PREPL deficiency. (NCT02263781 chunk 1)

  **Direct quote (registry content paraphrase):** primary outcomes focus on PREPL activity expressed as “ng active PREPL/g protein” and comparisons between groups. (NCT02263781 chunk 1)

### 12.5 MAXO suggestions (examples)
* MAXO: high fluid intake therapy (for nephrolithiasis prevention)
* MAXO: urinary alkalinization therapy (e.g., potassium citrate)
* MAXO: cystine-binding thiol therapy (tiopronin / D-penicillamine)
* MAXO: growth hormone replacement therapy
* MAXO: physical therapy / feeding support

---

## 13. Prevention
No primary prevention exists for the genetic cause, but **secondary/tertiary prevention** targets the cystinuria component:
* Maintain high urine volume and urinary alkalinization to prevent cystine precipitation and reduce recurrence. (bhatt2024pharmacologicalinterventionsfor pages 1-3, d’ambrosio2022cystinuriaanupdate pages 4-5)
* Monitor urinary pH/cystine-related measures and imaging for stones (review emphasizes regular monitoring; specific schedules vary). (bhatt2024pharmacologicalinterventionsfor pages 1-3, d’ambrosio2022cystinuriaanupdate pages 5-6)

---

## 14. Other species / natural disease
No naturally occurring non-human HCS analogs were identified in the retrieved corpus.

---

## 15. Model organisms
No dedicated HCS model organism evidence was successfully retrieved in the current tool runs; therefore, model organism section is incomplete.

---

## Figures/tables from retrieved primary case report
A schematic of reported 2p21 deletions and a clinical-feature table were retrieved from the HCS case report and can support KB curation of deletion boundaries and phenotypic fields. (taroni2019acaseof media 9faf13df, taroni2019acaseof media d28b2f89)

---

## Notes on evidence limitations (PMID requirement)
Several key sources in the retrieved corpus are peer-reviewed and include DOI/URLs, but PMIDs were not available in the extracted text for many items. Where PMID is required, manual PubMed crosswalk would be needed beyond current tool outputs. This report therefore provides DOI/URLs and publication metadata for traceability.


References

1. (eggermann20122p21deletionsin pages 1-2): Thomas Eggermann, Sabrina Spengler, Andreas Venghaus, Bernd Denecke, Klaus Zerres, Michael Baudis, and Regina Ensenauer. 2p21 deletions in hypotonia-cystinuria syndrome. European journal of medical genetics, 55 10:561-3, Oct 2012. URL: https://doi.org/10.1016/j.ejmg.2012.06.008, doi:10.1016/j.ejmg.2012.06.008. This article has 18 citations and is from a peer-reviewed journal.

2. (eggermann2012cystinuriaaninborn pages 6-8): Thomas Eggermann, Andreas Venghaus, and Klaus Zerres. Cystinuria: an inborn cause of urolithiasis. Orphanet Journal of Rare Diseases, 7:19-19, Apr 2012. URL: https://doi.org/10.1186/1750-1172-7-19, doi:10.1186/1750-1172-7-19. This article has 160 citations and is from a peer-reviewed journal.

3. (kılıc2018firstcardiacmanifestation pages 1-3): Mustafa Kılıç, Ahmet Cevdet Ceylan, Utku Arman Örün, and Esra Kılıç. First cardiac manifestation of hypotonia-cystinuria syndrome. Metabolic Brain Disease, 33:1375-1379, Apr 2018. URL: https://doi.org/10.1007/s11011-018-0226-2, doi:10.1007/s11011-018-0226-2. This article has 5 citations and is from a peer-reviewed journal.

4. (chabrol2008deletionofc2orf34 pages 2-3): B. Chabrol, Katrin Martens, S. Meulemans, Aline Cano, Jaak Jaeken, G. Matthijs, and John W. M. Creemers. Deletion of c2orf34, prepl and slc3a1 causes atypical hypotonia–cystinuria syndrome. Journal of Medical Genetics, 45:314-318, Jan 2008. URL: https://doi.org/10.1136/jmg.2007.055475, doi:10.1136/jmg.2007.055475. This article has 62 citations and is from a domain leading peer-reviewed journal.

5. (martens2008multisystemdisordersyndromes pages 2-3): Kevin Martens, Jaak Jaeken, Gert Matthijs, and John Creemers. Multi-system disorder syndromes associated with cystinuria type i. Current Molecular Medicine, 8:544-550, Sep 2008. URL: https://doi.org/10.2174/156652408785747997, doi:10.2174/156652408785747997. This article has 31 citations and is from a peer-reviewed journal.

6. (kılıc2018firstcardiacmanifestation pages 4-5): Mustafa Kılıç, Ahmet Cevdet Ceylan, Utku Arman Örün, and Esra Kılıç. First cardiac manifestation of hypotonia-cystinuria syndrome. Metabolic Brain Disease, 33:1375-1379, Apr 2018. URL: https://doi.org/10.1007/s11011-018-0226-2, doi:10.1007/s11011-018-0226-2. This article has 5 citations and is from a peer-reviewed journal.

7. (taroni2019acaseof pages 2-3): Francesca Taroni, Valentina Capone, Alfredo Berrettini, Erika Adalgisa De Marco, Gian Antonio Manzoni, and Giovanni Montini. A case of hypotonia-cystinuria syndrome with genito-urinary malformations and extrarenal involvement. Frontiers in Pediatrics, Apr 2019. URL: https://doi.org/10.3389/fped.2019.00127, doi:10.3389/fped.2019.00127. This article has 4 citations.

8. (d’ambrosio2022cystinuriaanupdate pages 1-3): Viola D’Ambrosio, Giovanna Capolongo, David Goldfarb, Giovanni Gambaro, and Pietro Manuel Ferraro. Cystinuria: an update on pathophysiology, genetics, and clinical management. Pediatric Nephrology, 37:1705-1711, Nov 2022. URL: https://doi.org/10.1007/s00467-021-05342-y, doi:10.1007/s00467-021-05342-y. This article has 55 citations and is from a domain leading peer-reviewed journal.

9. (d’ambrosio2022cystinuriaanupdate pages 4-5): Viola D’Ambrosio, Giovanna Capolongo, David Goldfarb, Giovanni Gambaro, and Pietro Manuel Ferraro. Cystinuria: an update on pathophysiology, genetics, and clinical management. Pediatric Nephrology, 37:1705-1711, Nov 2022. URL: https://doi.org/10.1007/s00467-021-05342-y, doi:10.1007/s00467-021-05342-y. This article has 55 citations and is from a domain leading peer-reviewed journal.

10. (boonen2011preplaprolyl pages 1-3): Kurt Boonen, Luc Regal, Jaak Jaeken, and John W.M. Creemers. Prepl, a prolyl endopeptidase-like enzyme by name only? – lessons from patients. CNS &amp; Neurological Disorders - Drug Targets, 10:355-360, May 2011. URL: https://doi.org/10.2174/187152711794653760, doi:10.2174/187152711794653760. This article has 21 citations.

11. (NCT02263781 chunk 1):  PREPL in Health and Disease. Universitaire Ziekenhuizen KU Leuven. 2014. ClinicalTrials.gov Identifier: NCT02263781

12. (bhatt2024pharmacologicalinterventionsfor pages 1-3): Nirmal Prasad Bhatt, Aniruddh Vijay Deshpande, and Malcolm Ronald Starkey. Pharmacological interventions for the management of cystinuria: a systematic review. Journal of Nephrology, 37:293-308, Nov 2024. URL: https://doi.org/10.1007/s40620-023-01795-6, doi:10.1007/s40620-023-01795-6. This article has 21 citations and is from a peer-reviewed journal.

13. (bhatt2024pharmacologicalinterventionsfor pages 10-11): Nirmal Prasad Bhatt, Aniruddh Vijay Deshpande, and Malcolm Ronald Starkey. Pharmacological interventions for the management of cystinuria: a systematic review. Journal of Nephrology, 37:293-308, Nov 2024. URL: https://doi.org/10.1007/s40620-023-01795-6, doi:10.1007/s40620-023-01795-6. This article has 21 citations and is from a peer-reviewed journal.

14. (NCT02640443 chunk 1):  Sulfamethoxazole for the Treatment of Primary PREPL Deficiency. Universitair Ziekenhuis Brussel. 2015. ClinicalTrials.gov Identifier: NCT02640443

15. (d’ambrosio2022cystinuriaanupdate pages 5-6): Viola D’Ambrosio, Giovanna Capolongo, David Goldfarb, Giovanni Gambaro, and Pietro Manuel Ferraro. Cystinuria: an update on pathophysiology, genetics, and clinical management. Pediatric Nephrology, 37:1705-1711, Nov 2022. URL: https://doi.org/10.1007/s00467-021-05342-y, doi:10.1007/s00467-021-05342-y. This article has 55 citations and is from a domain leading peer-reviewed journal.

16. (taroni2019acaseof media 9faf13df): Francesca Taroni, Valentina Capone, Alfredo Berrettini, Erika Adalgisa De Marco, Gian Antonio Manzoni, and Giovanni Montini. A case of hypotonia-cystinuria syndrome with genito-urinary malformations and extrarenal involvement. Frontiers in Pediatrics, Apr 2019. URL: https://doi.org/10.3389/fped.2019.00127, doi:10.3389/fped.2019.00127. This article has 4 citations.

17. (taroni2019acaseof media d28b2f89): Francesca Taroni, Valentina Capone, Alfredo Berrettini, Erika Adalgisa De Marco, Gian Antonio Manzoni, and Giovanni Montini. A case of hypotonia-cystinuria syndrome with genito-urinary malformations and extrarenal involvement. Frontiers in Pediatrics, Apr 2019. URL: https://doi.org/10.3389/fped.2019.00127, doi:10.3389/fped.2019.00127. This article has 4 citations.