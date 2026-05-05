---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-26T20:04:14.926729'
end_time: '2026-04-26T20:16:30.324743'
duration_seconds: 735.4
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ulnar-Mammary Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ulnar-Mammary Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Ulnar-Mammary Syndrome** covering all of the
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
- **Disease Name:** Ulnar-Mammary Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Ulnar-Mammary Syndrome** covering all of the
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


# Ulnar‑Mammary Syndrome (UMS) — Disease Characteristics Research Report

## Target disease
- **Disease name:** Ulnar‑Mammary Syndrome (UMS)
- **Category:** Mendelian developmental disorder
- **MONDO ID:** Not available in retrieved evidence corpus (not present in accessed full text)

## Executive overview
Ulnar‑mammary syndrome (UMS) is a rare, pleiotropic, typically autosomal dominant developmental disorder primarily affecting posterior (ulnar‑ray) limb development and mammary/apocrine gland development, with frequent genital/endocrine involvement and variable expressivity across and within families. UMS is caused by heterozygous deleterious variants in **TBX3**, a T‑box transcription factor critical for patterning and organogenesis, with haploinsufficiency widely supported as the predominant mechanism (galazzi2018hypogonadotropichypogonadismand pages 1-2, tung2022tbx3andefna4 pages 1-2, bottillo2024aninheritedtbx3 pages 1-2).

## 1. Disease information
### 1.1 Definition and current understanding
UMS is consistently described as a developmental malformation syndrome involving **limb**, **mammary/apocrine**, **dentition**, and **genital** development, with additional endocrine and occasional cardiac/other congenital anomalies reported (galazzi2018hypogonadotropichypogonadismand pages 1-2, tung2022tbx3andefna4 pages 1-2, bottillo2024aninheritedtbx3 pages 1-2).

### 1.2 Key identifiers
- **OMIM (disease):** **181450** (UMS) (zhang2023literaturereviewreport pages 1-3, tung2022tbx3andefna4 pages 1-2)
- **OMIM (gene):** **TBX3 *601621** (tung2022tbx3andefna4 pages 1-2)
- **Orphanet:** referenced as an authoritative rare disease resource and as the basis for the commonly cited count of published cases; disease page URL is cited directly in a 2022 peer‑reviewed report: https://www.orpha.net/consor/cgi-bin/Disease_Search.php?Ing=EN&data_id=2808&Disease_Search_diseaseGroup=Ulnar-mammary-syndrome&Disease_Disease_Search_diseaseType=Pat&Disease(s)/group/group%20of%20diseases=Ulnar-mammary-syndrome&title=Ulnar-mammary%20syndrome&search=Disease_Search_Simple (accessed 31 Aug 2022 as reported) (tung2022tbx3andefna4 pages 1-2)
- **ICD‑10/ICD‑11, MeSH, MONDO:** Not present in retrieved full‑text evidence; therefore not asserted here.

### 1.3 Synonyms / alternative names
- **Schinzel syndrome / Shinzel syndrome** (noted as an alternative name in recent literature) (bottillo2024aninheritedtbx3 pages 1-2)

### 1.4 Evidence source type
The information summarized here is derived from **aggregated disease‑level resources** embedded in peer‑reviewed articles (e.g., Orphanet‑based counts) and **individual patient/family reports and case series/reviews** (e.g., Linden 2009; Galazzi 2018; Zhang 2023; Bottillo 2024; Tung 2022) (zhang2023literaturereviewreport pages 1-3, galazzi2018hypogonadotropichypogonadismand pages 1-2, linden2009ulnarmammarysyndrome pages 1-2, tung2022tbx3andefna4 pages 1-2, bottillo2024aninheritedtbx3 pages 1-2).

## 2. Etiology
### 2.1 Disease causal factors
**Genetic:** Heterozygous deleterious variants in **TBX3** cause UMS (galazzi2018hypogonadotropichypogonadismand pages 1-2, tung2022tbx3andefna4 pages 1-2, bamshad1999thespectrumof pages 1-2).

**Mechanistic framing (current):** UMS is generally framed as a **dosage‑sensitive developmental transcription‑factor disorder**, with haploinsufficiency commonly invoked; however, experimental work in mice supports that not all TBX3 alterations behave as simple nulls (e.g., truncated/mislocalized proteins may contribute) (frank2013mousetbx3mutants pages 1-2, tung2022tbx3andefna4 pages 1-2).

### 2.2 Risk factors
For a Mendelian disorder, the main risk factor is **inheritance of a pathogenic TBX3 variant**. Familial transmission and intrafamilial variability are repeatedly documented (tung2022tbx3andefna4 pages 2-4, linden2009ulnarmammarysyndrome pages 1-2).

### 2.3 Protective factors
Not established in the retrieved evidence.

### 2.4 Gene–environment interactions
Not established in the retrieved evidence.

## 3. Phenotypes
### 3.1 Core phenotype domains (with suggested HPO mappings)
UMS exhibits substantial **variable expressivity** and sometimes subtle signs in carriers (linden2009ulnarmammarysyndrome pages 1-2, tung2022tbx3andefna4 pages 1-2).

#### A) Limb anomalies (posterior/ulnar ray)
- **Typical findings:** posterior upper limb deficiencies ranging from mild fifth‑finger anomalies to severe forearm/hand reduction; may be asymmetric (galazzi2018hypogonadotropichypogonadismand pages 1-2, tung2022tbx3andefna4 pages 1-2).
- **Example patient detail (2023):** absent left ulna and absent 4th/5th metacarpals/phalanges (zhang2023literaturereviewreport pages 1-3).
- **Suggested HPO terms:**
  - Ulnar hypoplasia/aplasia (e.g., **HP:0003048** ulnar hypoplasia; confirm exact HPO ID during curation)
  - Postaxial polydactyly (**HP:0100259**)
  - Fifth finger abnormalities (clinodactyly/camptodactyly; e.g., **HP:0004209**, **HP:0001239**)

#### B) Mammary/nipple and apocrine features
- **Findings:** nipple hypoplasia/inversion/retraction; apocrine hypoplasia manifested as reduced sweating and absent/reduced axillary hair (galazzi2018hypogonadotropichypogonadismand pages 1-2, zhang2023literaturereviewreport pages 1-3).
- **Suggested HPO terms:**
  - Inverted/retracted nipples (e.g., **HP:0002562** inverted nipples)
  - Hypohidrosis (**HP:0000966**)
  - Sparse axillary hair (e.g., **HP:0002230** sparse body hair)

#### C) Genital / reproductive anomalies (often male)
- **Findings:** micropenis, cryptorchidism, delayed puberty; hypogonadotropic hypogonadism may be congenital and persistent (galazzi2018hypogonadotropichypogonadismand pages 1-2, zhang2023literaturereviewreport pages 1-3).
- **Suggested HPO terms:**
  - Micropenis (**HP:0000054**)
  - Cryptorchidism (**HP:0000028**)
  - Delayed puberty (**HP:0000823**)
  - Hypogonadotropic hypogonadism (**HP:0000044**)

#### D) Endocrine / pituitary and growth
- **Pituitary hypoplasia and nIHH:** documented as recurrent features in an endocrine‑focused study (galazzi2018hypogonadotropichypogonadismand pages 1-2, galazzi2018hypogonadotropichypogonadismand pages 5-6).
- **Short stature / growth hormone deficiency:** reported in multiple cases, with pituitary structural abnormalities; one report explicitly proposes routine evaluation (linden2009ulnarmammarysyndrome pages 1-2, zhang2023literaturereviewreport pages 5-6).
- **Suggested HPO terms:**
  - Short stature (**HP:0004322**)
  - Growth hormone deficiency (**HP:0000824**)
  - Pituitary hypoplasia (**HP:0000873**)

#### E) Dental anomalies / midline anomalies
- Midline defects including “nose, teeth and tongue anomalies” are noted in endocrine‑focused familial cases (galazzi2018hypogonadotropichypogonadismand pages 1-2).
- **Suggested HPO terms:**
  - Abnormal dentition (**HP:0006482**)
  - Midline defect (use specific terms depending on phenotype)

### 3.2 Phenotype frequencies/statistics (from recent analyses)
- **Published case count:** approximately **128 cases** reported worldwide (recently reiterated) (zhang2023literaturereviewreport pages 1-3, tung2022tbx3andefna4 pages 1-2).
- **Delayed puberty in males:** **79%** (combined analysis in an endocrine‑focused synthesis) (galazzi2018hypogonadotropichypogonadismand pages 1-2).
- **Other signs of hypogonadism in males:** **37%** (same combined analysis) (galazzi2018hypogonadotropichypogonadismand pages 1-2).
- **Short stature:** reported in about **~16%** of cases in a 2023 literature synthesis (zhang2023literaturereviewreport pages 5-6).

### 3.3 Quality of life impact
Direct quantitative QoL instruments were not reported in the retrieved evidence. However, real‑world impacts are implied by the need for orthopedic interventions for limb malformations, endocrine therapy for pubertal induction/fertility and growth, and cardiac surveillance/management when defects occur (linden2009ulnarmammarysyndrome pages 1-2, galazzi2018hypogonadotropichypogonadismand pages 5-6).

## 4. Genetic / molecular information
### 4.1 Causal gene
- **TBX3** encodes a T‑box transcription factor (DNA‑binding domain) important for embryonic development and organogenesis; heterozygous deleterious variants cause UMS (galazzi2018hypogonadotropichypogonadismand pages 1-2, bamshad1999thespectrumof pages 1-2).

### 4.2 Pathogenic variant classes and examples
UMS‑associated variants include truncating (frameshift/nonsense), splice‑site, and missense variants, including variants downstream of the T‑box domain; missense variants in the T‑box domain are highlighted as functionally impactful in a 2024 functional study (bottillo2024aninheritedtbx3 pages 1-2, bamshad1999thespectrumof pages 1-2).

Representative recent variants:
- **Frameshift (pathogenic):** TBX3 **c.1121_1124delAGAG (p.Glu374fs)** (WES + Sanger; ACMG pathogenic) (zhang2023literaturereviewreport pages 1-3).
- **Missense (likely pathogenic, functional follow‑up):** TBX3 **c.400C>T (p.P134S)**, prenatally ascertained; functional characterization performed using a humanized Drosophila model (bottillo2024aninheritedtbx3 pages 1-2, bottillo2024aninheritedtbx3 pages 2-4).
- **Splice‑site (likely pathogenic):** TBX3 **c.804+1G>A**, identified by NGS; marked intrafamilial variability reported (tung2022tbx3andefna4 pages 1-2, tung2022tbx3andefna4 pages 2-4).

Population frequency statements:
- The p.P134S variant is reported as **absent from gnomAD** in the 2024 report (bottillo2024aninheritedtbx3 pages 2-4).

### 4.3 Functional consequences
- Haploinsufficiency is widely discussed as the prevailing mechanism (galazzi2018hypogonadotropichypogonadismand pages 1-2, bottillo2024aninheritedtbx3 pages 1-2).
- Experimental mouse genetics show that some engineered “null” alleles can generate truncated/mislocalized TBX3 proteins and yield phenotypes different from a true null allele, supporting that **not all TBX3 variants are functionally equivalent** (frank2013mousetbx3mutants pages 1-2).

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
- **Modifier genes:** not established in the retrieved evidence; variable expressivity is emphasized (bottillo2024aninheritedtbx3 pages 1-2, tung2022tbx3andefna4 pages 1-2).
- **Epigenetic information:** not directly described for UMS in retrieved evidence.
- **Chromosomal abnormalities:** not systematically reviewed in the retrieved evidence corpus; however, TBX3 can be interrogated by methods beyond sequencing (e.g., genomic testing strategies discussed for broader diagnostic workups) (tung2022tbx3andefna4 pages 1-2).

## 5. Environmental information
UMS is not presented as environmentally caused. No consistent environmental contributors were identified in the retrieved evidence.

## 6. Mechanism / pathophysiology
UMS is best understood as a **developmental gene regulatory network disorder** due to reduced TBX3 function during embryogenesis, disrupting patterning and epithelial–mesenchymal interactions in multiple organ systems.

### 6.1 Limb patterning (2024 mechanistic advance)
A 2024 mouse developmental genomics study places TBX3 directly in early limb‑bud anteroposterior patterning:
- TBX3 is required to establish the **posterior boundary of anterior genes** by repression that excludes factors such as **Gli3, Alx4, Hand1 and Irx3/5** from posterior limb‑bud mesenchyme, thereby delineating a posterior territory competent to establish the SHH organizer (soussi2024tbx3isessential pages 1-2).
- HAND2 cooperates with TBX3 to upregulate posterior identity targets and is required for SHH activation (soussi2024tbx3isessential pages 1-2).

**Suggested GO biological process terms (examples):** limb development; anterior/posterior pattern specification; regulation of transcription by RNA polymerase II. 
**Suggested cell types (CL):** limb bud mesenchymal cell (map to appropriate CL term during curation).

### 6.2 Retinoic acid signaling as an upstream regulator of TBX3 in limb development
A mechanistic cell/developmental biology study demonstrates that Tbx3 is a **direct target of retinoic acid signaling**:
- “retinoic acid (RA) activates endogenous TBX3 expression… mediated by an RA–receptor complex directly binding and activating the TBX3 promoter” with evidence for relevance in mouse embryonic limb development (ballim2012theulnarmammarysyndrome pages 1-2).

**Pathway suggestions:** retinoic acid signaling; transcriptional regulation.

### 6.3 Mammary/apocrine development and dosage sensitivity
Mouse developmental work indicates TBX3 dosage sensitivity in mammary development:
- Tbx3 is “essential for induction of the mammary placodes” and shows a **haploinsufficiency effect** on maintenance of mammary placodes and ductal branching; genetic interaction with Tbx2 is described, with effects not clearly mediated by p19Arf/p53 in that context (jerome‐majewska2005tbx3theulnar‐mammary pages 1-2).

### 6.4 Endocrine/pituitary mechanism (clinical inference)
Endocrine case series data show that congenital normosmic hypogonadotropic hypogonadism (nIHH) can be associated with pituitary hypoplasia in UMS and can persist into adulthood, supporting TBX3 involvement in hypothalamic–pituitary development/function (galazzi2018hypogonadotropichypogonadismand pages 1-2).

## 7. Anatomical structures affected
### 7.1 Organ and system level
- **Musculoskeletal/limb:** posterior upper limb/ulnar ray; digits; forearm bones (zhang2023literaturereviewreport pages 1-3, galazzi2018hypogonadotropichypogonadismand pages 1-2).
- **Integumentary/apocrine:** axillary hair and sweat glands (apocrine involvement inferred clinically by reduced perspiration) (galazzi2018hypogonadotropichypogonadismand pages 1-2).
- **Breast/nipple:** nipple/breast development and potentially lactation (galazzi2018hypogonadotropichypogonadismand pages 1-2).
- **Reproductive system:** external male genitalia and testes; pubertal development (galazzi2018hypogonadotropichypogonadismand pages 1-2).
- **Endocrine (pituitary):** pituitary size/structure and hypothalamic–pituitary axis function (galazzi2018hypogonadotropichypogonadismand pages 1-2, linden2009ulnarmammarysyndrome pages 1-2).
- **Cardiac (subset):** congenital heart defect and conduction abnormalities are reported; a clinical report recommends screening (linden2009ulnarmammarysyndrome pages 1-2).

### 7.2 Suggested UBERON mappings (examples)
- Upper limb (UBERON:0002101)
- Mammary gland (UBERON:0001911)
- Pituitary gland (UBERON:0000007)
- Testis (UBERON:0000473)

## 8. Temporal development
- **Onset:** congenital (limb, nipple/apocrine anomalies present from birth), with endocrine manifestations often recognized in childhood/adolescence via growth failure or delayed puberty (zhang2023literaturereviewreport pages 1-3, galazzi2018hypogonadotropichypogonadismand pages 1-2).
- **Course:** structural anomalies are lifelong; endocrine deficiencies may require long‑term management and can persist into adulthood (nIHH persistence reported) (galazzi2018hypogonadotropichypogonadismand pages 1-2).

## 9. Inheritance and population
### 9.1 Inheritance
- **Autosomal dominant** inheritance is consistently stated (zhang2023literaturereviewreport pages 1-3, tung2022tbx3andefna4 pages 1-2).
- **Variable expressivity** is emphasized (linden2009ulnarmammarysyndrome pages 1-2, tung2022tbx3andefna4 pages 1-2).
- **Incomplete penetrance** is stated in a 2023 report (zhang2023literaturereviewreport pages 3-4).

### 9.2 Epidemiology
- UMS is extremely rare; a commonly repeated literature‑based estimate is **~128 published cases worldwide** (zhang2023literaturereviewreport pages 1-3, tung2022tbx3andefna4 pages 1-2). Prevalence/incidence rates were not provided in retrieved full text.

## 10. Diagnostics
### 10.1 Clinical suspicion
Clues supporting diagnosis include posterior limb defects (ulnar ray), nipple/apocrine anomalies (inverted nipples, reduced sweating, absent axillary hair), and genital/endocrine findings (micropenis, cryptorchidism, delayed puberty), with high phenotypic variability (galazzi2018hypogonadotropichypogonadismand pages 1-2, zhang2023literaturereviewreport pages 1-3).

### 10.2 Genetic testing (real‑world implementations)
Documented approaches include:
- **Whole‑exome sequencing (WES)** with **Sanger confirmation** and ACMG classification (example: pathogenic frameshift) (zhang2023literaturereviewreport pages 1-3).
- **Targeted NGS panels** (example: CLIA panel used in a UMS/craniosynostosis context; also endocrine gene panels including TBX3) (tung2022tbx3andefna4 pages 2-4, galazzi2018hypogonadotropichypogonadismand pages 1-2).
- **Whole‑genome sequencing (WGS)** as a follow‑up in complex/overlapping phenotypes (tung2022tbx3andefna4 pages 2-4).

### 10.3 Endocrine and imaging workup
- The endocrine‑focused paper emphasizes that UMS should be suspected in patients with **delayed puberty and midline defects including pituitary hypoplasia**, even without obvious limb malformations, and that TBX3 should be included in candidate gene lists for congenital nIHH (galazzi2018hypogonadotropichypogonadismand pages 1-2).
- A clinical report suggests offering **brain imaging, growth hormone testing, and cardiac arrhythmia screening** because these findings may be under‑ascertained (linden2009ulnarmammarysyndrome pages 1-2).

### 10.4 Differential diagnosis
Not systematically enumerated in the retrieved evidence; however, overlap with other “heart–hand” and limb malformation syndromes is implied by the need for careful genetic workup and variable presentations (tung2022tbx3andefna4 pages 1-2).

## 11. Outcome / prognosis
UMS outcomes are driven by the severity of congenital malformations and endocrine/cardiac complications. No disease‑specific survival statistics were identified in retrieved evidence. Severe cardiac conduction disease can be clinically significant when present, supporting surveillance (linden2009ulnarmammarysyndrome pages 1-2).

## 12. Treatment
No disease‑modifying molecular therapy is described in retrieved evidence; management is supportive and complication‑directed.

### 12.1 Endocrine management (documented real‑world practice)
- **Growth hormone replacement** was instituted for growth hormone deficiency with pituitary abnormalities (clinical report) (linden2009ulnarmammarysyndrome pages 1-2).
- Management regimens for hypogonadotropic hypogonadism/delayed puberty include **testosterone for pubertal induction** and gonadotropin‑based regimens (FSH priming and hCG) described as applied in UMS patients with nIHH (galazzi2018hypogonadotropichypogonadismand pages 2-3, galazzi2018hypogonadotropichypogonadismand pages 5-6).

### 12.2 Surgical/interventional
- **Cryptorchidism** may be treated with **orchidopexy** (clinical report) (linden2009ulnarmammarysyndrome pages 1-2).
- Orthopedic/rehabilitative care is implied for limb malformations; specific protocols are not detailed in retrieved evidence.

### 12.3 MAXO suggestions (examples)
- Growth hormone therapy (MAXO term to be assigned during ontology curation)
- Testosterone replacement / pubertal induction
- Orchidopexy
- Genetic counseling

## 13. Prevention
Primary prevention is not applicable for an inherited dominant developmental disorder, but **reproductive and familial risk reduction** approaches apply:
- **Genetic counseling** is indicated given autosomal dominant inheritance and intrafamilial variability (tung2022tbx3andefna4 pages 1-2, linden2009ulnarmammarysyndrome pages 1-2).
- **Prenatal diagnosis** can occur when a familial variant is known; a 2024 report describes prenatal ascertainment and subsequent family re‑evaluation (bottillo2024aninheritedtbx3 pages 1-2).

## 14. Other species / natural disease
No naturally occurring veterinary syndrome directly analogous to human UMS was identified in the retrieved evidence. However, TBX3 has conserved roles across species.

## 15. Model organisms
### 15.1 Drosophila (2024)
A 2024 study developed a **humanized Drosophila model** expressing TBX3 variants (including p.P134S) to assess developmental consequences and variant functional impact; the work argues this model can dissect TBX3‑dependent developmental pathways relevant to UMS (bottillo2024aninheritedtbx3 pages 1-2, bottillo2024aninheritedtbx3 pages 2-4).

### 15.2 Mouse developmental models
Mechanistic and phenotypic mouse evidence underpins UMS understanding:
- RA regulation of Tbx3 in limb development (ballim2012theulnarmammarysyndrome pages 1-2).
- Early limb‑bud patterning role of Tbx3 (2024 ChIP‑seq and expression studies) (soussi2024tbx3isessential pages 1-2).
- Mammary placode induction/maintenance and branching morphogenesis dosage sensitivity (jerome‐majewska2005tbx3theulnar‐mammary pages 1-2).

## Recent developments (emphasis 2023–2024)
1. **2023 clinical genetics expansion:** a novel pathogenic TBX3 frameshift (c.1121_1124delAGAG; p.Glu374fs) was reported, with detailed endocrine and pituitary imaging phenotyping and reiteration of rarity (~128 cases) (zhang2023literaturereviewreport pages 1-3).
2. **2024 functional variant interpretation:** prenatal case with a novel TBX3 missense (p.P134S) and functional characterization using a humanized Drosophila model, alongside an updated constitutional variant spectrum emphasizing the importance of the T‑box domain for missense pathogenicity (bottillo2024aninheritedtbx3 pages 1-2, bottillo2024aninheritedtbx3 pages 2-4).
3. **2024 mechanistic limb‑bud genomics:** TBX3 positioned as a key repressor establishing anterior gene boundaries in posterior mesenchyme and cooperating with HAND2 to promote posterior identity and SHH organizer formation (soussi2024tbx3isessential pages 1-2).

## Direct quotes (for evidence traceability)
- Galazzi et al. 2018 (abstract): “The combined analysis of these findings and of the previous UMS reports showed **delayed puberty and other signs of hypogonadism in 79 and 37% of UMS males**, respectively.” (galazzi2018hypogonadotropichypogonadismand pages 1-2)
- Zhang et al. 2023 (background): “To date, **approximately 128 cases have been reported worldwide**, and only 2 cases have been reported in China (including this case).” (zhang2023literaturereviewreport pages 1-3)
- Ballim et al. 2012 (abstract): “retinoic acid (RA) activates endogenous TBX3 expression, which is mediated by an RA–receptor complex directly binding and activating the TBX3 promoter…” (ballim2012theulnarmammarysyndrome pages 1-2)

## Summary artifact
Key identifiers, variant examples, and phenotype statistics are summarized here:

| Item type | Detail | Source (first author year) | URL/DOI |
|---|---|---|---|
| Identifier / nomenclature | Ulnar-mammary syndrome (UMS); OMIM **#181450**; described as a rare autosomal dominant disorder with marked clinical heterogeneity (zhang2023literaturereviewreport pages 1-3, tung2022tbx3andefna4 pages 1-2) | Zhang 2023 | https://doi.org/10.3389/fped.2023.1052931 |
| Identifier / nomenclature | Alternative eponym: **Schinzel syndrome**; UMS also referenced in Orphanet disease listings and case summaries (bottillo2024aninheritedtbx3 pages 1-2, tung2022tbx3andefna4 pages 1-2) | Bottillo 2024 | https://doi.org/10.1002/jcp.31440 |
| Causal gene / mechanism | **TBX3** (OMIM ***601621**) is the causal gene; UMS results from heterozygous TBX3 variants, usually via **haploinsufficiency** (galazzi2018hypogonadotropichypogonadismand pages 1-2, bottillo2024aninheritedtbx3 pages 1-2) | Galazzi 2018 | https://doi.org/10.1530/EC-18-0486 |
| Causal gene / mechanism | TBX3 is a developmental T-box transcription factor required for limb, mammary/apocrine, genital and pituitary-related development; 2024 mechanistic data show TBX3 helps establish posterior limb-bud identity and cooperates with HAND2 in early limb patterning (soussi2024tbx3isessential pages 1-2, ballim2012theulnarmammarysyndrome pages 1-2) | Soussi 2024 | https://doi.org/10.1242/dev.202722 |
| Variant (representative) | **c.804+1G>A** (TBX3 intron 3 canonical splice-site); novel **likely pathogenic splice variant** in a family with UMS and marked intrafamilial variability (tung2022tbx3andefna4 pages 2-4, tung2022tbx3andefna4 pages 1-2) | Tung 2022 | https://doi.org/10.3390/genes13091649 |
| Variant (representative) | **c.1121_1124delAGAG (p.Glu374fs)**; **pathogenic frameshift** identified by exome sequencing/Sanger confirmation in a Chinese boy with short stature, ulnar hypoplasia, hypohidrosis, retracted nipples, micropenis, and cryptorchidism (zhang2023literaturereviewreport pages 1-3) | Zhang 2023 | https://doi.org/10.3389/fped.2023.1052931 |
| Variant (representative) | **c.400C>T (p.P134S)**; novel **likely pathogenic missense** variant in the T-box domain, absent from gnomAD in the report, functionally assessed in a Drosophila humanized model (bottillo2024aninheritedtbx3 pages 2-4, bottillo2024aninheritedtbx3 pages 1-2) | Bottillo 2024 | https://doi.org/10.1002/jcp.31440 |
| Variant spectrum | Constitutional TBX3 variant spectrum includes truncating, splice-site, missense, insertion/deletion, and downstream-of-T-box variants; pathogenic missense variants are enriched in the **T-box domain** (bottillo2024aninheritedtbx3 pages 2-4, bamshad1999thespectrumof pages 1-2) | Bottillo 2024 | https://doi.org/10.1002/jcp.31440 |
| Phenotype statistic | Approximately **128 cases** of UMS had been published/reported worldwide in recent reviews/case summaries (zhang2023literaturereviewreport pages 1-3, tung2022tbx3andefna4 pages 1-2) | Zhang 2023 | https://doi.org/10.3389/fped.2023.1052931 |
| Phenotype statistic | In combined analysis of prior reports, **delayed puberty** occurred in **79% of UMS males** (galazzi2018hypogonadotropichypogonadismand pages 1-2) | Galazzi 2018 | https://doi.org/10.1530/EC-18-0486 |
| Phenotype statistic | In combined analysis of prior reports, **other signs of hypogonadism** occurred in **37% of UMS males** (galazzi2018hypogonadotropichypogonadismand pages 1-2) | Galazzi 2018 | https://doi.org/10.1530/EC-18-0486 |
| Phenotype statistic | **Short stature** has been reported in about **16%** of cases in literature summarized by recent review (zhang2023literaturereviewreport pages 5-6) | Zhang 2023 | https://doi.org/10.3389/fped.2023.1052931 |
| Phenotype statistic | Core prepubertal recognition features emphasized in 2024 review/function study: **ulnar/ulnar-ray defects**, **hypoplastic nipples/areolae**, and less often **male genital anomalies** (bottillo2024aninheritedtbx3 pages 1-2) | Bottillo 2024 | https://doi.org/10.1002/jcp.31440 |


*Table: This table compacts the key disease identifiers, causal gene/mechanism, representative recent TBX3 variants, and the main phenotype statistics reported for ulnar-mammary syndrome. It is useful as a quick reference for knowledge-base curation and report drafting.*

## Key limitations of this report
- **PMIDs** were not available in the retrieved full‑text snippets; therefore this report cites **DOIs/URLs** and publication dates from the accessed articles.
- **MONDO/MeSH/ICD codes, prevalence/incidence estimates, and population allele frequency tables** were not present in the retrieved corpus; these should be supplemented by direct queries to MONDO, MeSH, ICD, ClinVar, and gnomAD in a future update.


References

1. (galazzi2018hypogonadotropichypogonadismand pages 1-2): Elena Galazzi, Paolo Duminuco, Mirella Moro, Fabiana Guizzardi, Nicoletta Marazzi, Alessandro Sartorio, Sabrina Avignone, Marco Bonomi, Luca Persani, and Maria Teresa Bonati. Hypogonadotropic hypogonadism and pituitary hypoplasia as recurrent features in ulnar-mammary syndrome. Endocrine Connections, 7:1432-1441, Dec 2018. URL: https://doi.org/10.1530/ec-18-0486, doi:10.1530/ec-18-0486. This article has 15 citations and is from a peer-reviewed journal.

2. (tung2022tbx3andefna4 pages 1-2): Moon Ley Tung, Bharatendu Chandra, Jaclyn Kotlarek, Marcelo Melo, Elizabeth Phillippi, Cristina M. Justice, Anthony Musolf, Simeon A. Boyadijev, Paul A. Romitti, Benjamin Darbro, and Hatem El-Shanti. Tbx3 and efna4 variant in a family with ulnar-mammary syndrome and sagittal craniosynostosis. Genes, 13:1649, Sep 2022. URL: https://doi.org/10.3390/genes13091649, doi:10.3390/genes13091649. This article has 5 citations.

3. (bottillo2024aninheritedtbx3 pages 1-2): Irene Bottillo, Andrea D'Alessandro, Maria Pia Ciccone, Gianluca Cestra, Gianluca Di Giacomo, Evelina Silvestri, Marco Castori, Francesco Brancati, Andrea Lenzi, Alessandro Paiardini, Silvia Majore, Giovanni Cenci, and Paola Grammatico. An inherited tbx3 alteration in a prenatal case of ulnar‐mammary syndrome: clinical assessment and functional characterization in drosophila melanogaster. Journal of Cellular Physiology, Sep 2024. URL: https://doi.org/10.1002/jcp.31440, doi:10.1002/jcp.31440. This article has 3 citations and is from a peer-reviewed journal.

4. (zhang2023literaturereviewreport pages 1-3): Xiwen Zhang, Lifen Chen, Lin Li, Jingjing An, Qinyu He, Xuelei Zhang, Wenli Lu, Yuan Xiao, and Zhiya Dong. Literature review, report, and analysis of genotype and clinical phenotype of a rare case of ulnar-mammary syndrome. Frontiers in Pediatrics, Mar 2023. URL: https://doi.org/10.3389/fped.2023.1052931, doi:10.3389/fped.2023.1052931. This article has 6 citations.

5. (linden2009ulnarmammarysyndrome pages 1-2): Helen Linden, Rosy Williams, Janet King, Edward Blair, and Usha Kini. Ulnar mammary syndrome and tbx3: expanding the phenotype. American Journal of Medical Genetics Part A, 149A:2809-2812, Dec 2009. URL: https://doi.org/10.1002/ajmg.a.33096, doi:10.1002/ajmg.a.33096. This article has 87 citations.

6. (bamshad1999thespectrumof pages 1-2): M. Bamshad, M. Bamshad, Trung Le, W. Watkins, Missy Dixon, Bridget E. Kramer, Amy D. Roeder, John C. Carey, S. Root, A. Schinzel, L. V. Maldergem, R. Gardner, R. Lin, Christine E. Seidman, J. G. Seidman, R. Wallerstein, Ellen Moran, R. Sutphen, Christine E. Campbell, and L. Jorde. The spectrum of mutations in tbx3: genotype/phenotype relationship in ulnar-mammary syndrome. American journal of human genetics, 64 6:1550-62, Jun 1999. URL: https://doi.org/10.1086/302417, doi:10.1086/302417. This article has 234 citations and is from a highest quality peer-reviewed journal.

7. (frank2013mousetbx3mutants pages 1-2): Deborah U. Frank, Uchenna Emechebe, Kirk R. Thomas, and Anne M. Moon. Mouse tbx3 mutants suggest novel molecular mechanisms for ulnar-mammary syndrome. PLoS ONE, 8:e67841, Jul 2013. URL: https://doi.org/10.1371/journal.pone.0067841, doi:10.1371/journal.pone.0067841. This article has 56 citations and is from a peer-reviewed journal.

8. (tung2022tbx3andefna4 pages 2-4): Moon Ley Tung, Bharatendu Chandra, Jaclyn Kotlarek, Marcelo Melo, Elizabeth Phillippi, Cristina M. Justice, Anthony Musolf, Simeon A. Boyadijev, Paul A. Romitti, Benjamin Darbro, and Hatem El-Shanti. Tbx3 and efna4 variant in a family with ulnar-mammary syndrome and sagittal craniosynostosis. Genes, 13:1649, Sep 2022. URL: https://doi.org/10.3390/genes13091649, doi:10.3390/genes13091649. This article has 5 citations.

9. (galazzi2018hypogonadotropichypogonadismand pages 5-6): Elena Galazzi, Paolo Duminuco, Mirella Moro, Fabiana Guizzardi, Nicoletta Marazzi, Alessandro Sartorio, Sabrina Avignone, Marco Bonomi, Luca Persani, and Maria Teresa Bonati. Hypogonadotropic hypogonadism and pituitary hypoplasia as recurrent features in ulnar-mammary syndrome. Endocrine Connections, 7:1432-1441, Dec 2018. URL: https://doi.org/10.1530/ec-18-0486, doi:10.1530/ec-18-0486. This article has 15 citations and is from a peer-reviewed journal.

10. (zhang2023literaturereviewreport pages 5-6): Xiwen Zhang, Lifen Chen, Lin Li, Jingjing An, Qinyu He, Xuelei Zhang, Wenli Lu, Yuan Xiao, and Zhiya Dong. Literature review, report, and analysis of genotype and clinical phenotype of a rare case of ulnar-mammary syndrome. Frontiers in Pediatrics, Mar 2023. URL: https://doi.org/10.3389/fped.2023.1052931, doi:10.3389/fped.2023.1052931. This article has 6 citations.

11. (bottillo2024aninheritedtbx3 pages 2-4): Irene Bottillo, Andrea D'Alessandro, Maria Pia Ciccone, Gianluca Cestra, Gianluca Di Giacomo, Evelina Silvestri, Marco Castori, Francesco Brancati, Andrea Lenzi, Alessandro Paiardini, Silvia Majore, Giovanni Cenci, and Paola Grammatico. An inherited tbx3 alteration in a prenatal case of ulnar‐mammary syndrome: clinical assessment and functional characterization in drosophila melanogaster. Journal of Cellular Physiology, Sep 2024. URL: https://doi.org/10.1002/jcp.31440, doi:10.1002/jcp.31440. This article has 3 citations and is from a peer-reviewed journal.

12. (soussi2024tbx3isessential pages 1-2): Geoffrey Soussi, Ausra Girdziusaite, Shalu Jhanwar, Victorio Palacio, Marco Notaro, Rushikesh Sheth, Rolf Zeller, and Aimée Zuniga. Tbx3 is essential for establishment of the posterior boundary of anterior genes and upregulation of posterior genes together with hand2 during the onset of limb bud development. Development, Jun 2024. URL: https://doi.org/10.1242/dev.202722, doi:10.1242/dev.202722. This article has 7 citations and is from a domain leading peer-reviewed journal.

13. (ballim2012theulnarmammarysyndrome pages 1-2): Reyna Deeya Ballim, Cathy Mendelsohn, Virginia E. Papaioannou, and Sharon Prince. The ulnar-mammary syndrome gene, tbx3, is a direct target of the retinoic acid signaling pathway, which regulates its expression during mouse limb development. Molecular Biology of the Cell, 23:2362-2372, Jun 2012. URL: https://doi.org/10.1091/mbc.e11-09-0790, doi:10.1091/mbc.e11-09-0790. This article has 29 citations and is from a domain leading peer-reviewed journal.

14. (jerome‐majewska2005tbx3theulnar‐mammary pages 1-2): Loydie A. Jerome‐Majewska, Gerard P. Jenkins, Elana Ernstoff, Frederique Zindy, Charles J. Sherr, and Virginia E. Papaioannou. Tbx3, the ulnar‐mammary syndrome gene, and tbx2 interact in mammary gland development through a p19arf/p53‐independent pathway. Developmental Dynamics, 234:922-933, Dec 2005. URL: https://doi.org/10.1002/dvdy.20575, doi:10.1002/dvdy.20575. This article has 117 citations and is from a peer-reviewed journal.

15. (zhang2023literaturereviewreport pages 3-4): Xiwen Zhang, Lifen Chen, Lin Li, Jingjing An, Qinyu He, Xuelei Zhang, Wenli Lu, Yuan Xiao, and Zhiya Dong. Literature review, report, and analysis of genotype and clinical phenotype of a rare case of ulnar-mammary syndrome. Frontiers in Pediatrics, Mar 2023. URL: https://doi.org/10.3389/fped.2023.1052931, doi:10.3389/fped.2023.1052931. This article has 6 citations.

16. (galazzi2018hypogonadotropichypogonadismand pages 2-3): Elena Galazzi, Paolo Duminuco, Mirella Moro, Fabiana Guizzardi, Nicoletta Marazzi, Alessandro Sartorio, Sabrina Avignone, Marco Bonomi, Luca Persani, and Maria Teresa Bonati. Hypogonadotropic hypogonadism and pituitary hypoplasia as recurrent features in ulnar-mammary syndrome. Endocrine Connections, 7:1432-1441, Dec 2018. URL: https://doi.org/10.1530/ec-18-0486, doi:10.1530/ec-18-0486. This article has 15 citations and is from a peer-reviewed journal.