---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T17:00:54.141079'
end_time: '2026-04-24T17:23:42.290232'
duration_seconds: 1368.15
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Anorexia Nervosa
  mondo_id: ''
  category: Psychiatric
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Anorexia Nervosa
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Anorexia Nervosa** covering all of the
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
- **Disease Name:** Anorexia Nervosa
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Anorexia Nervosa** covering all of the
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


## Comprehensive Disease Characteristics Research Report: Anorexia Nervosa (Psychiatric)

### Executive Summary (current understanding; 2023–2024 prioritized)
Anorexia nervosa (AN) is a severe eating disorder characterized by persistent restriction of energy intake leading to significantly low body weight, typically accompanied by fear of weight gain and body-image disturbance, with high medical morbidity and elevated mortality relative to peers. Recent work strengthens the view that AN is a *metabo-psychiatric* disorder: genome-wide studies show substantial heritability and risk loci overlapping psychiatric traits and metabolic biology, while clinical studies continue to document multi-system complications (notably cardiovascular risk) and active investigation of biomarkers (endocrine, metabolic, immune) and mechanistic domains (brain network connectivity, microbiome–immune links). (wu2024peripheralbiomarkersof pages 1-2, bang2023genomewideanalysisof pages 1-2, tseng2024incidenceandrisk pages 1-2, chen2024neuroimagingstudiesof pages 1-2)


| Domain | Key finding (quantitative) | Population/study type | Publication (authors, journal) | Year/month | PMID | DOI/URL |
|---|---|---|---|---|---|---|
| Epidemiology / prevalence | Global prevalence reported as 1.4% of women and 0.2% of men worldwide; AN described as having the highest mortality rate among psychiatric disorders (wu2024peripheralbiomarkersof pages 1-2) | Meta-analysis of peripheral biomarker studies in acute AN vs non-AN controls | Wu et al., *Nutrients* (wu2024peripheralbiomarkersof pages 1-2) | 2024/Jun |  | https://doi.org/10.3390/nu16132095 |
| Epidemiology / prevalence | Lifetime prevalence reported as 0.62% among females and 0.04% among males; twin-based heritability ~50–60% (bang2023genomewideanalysisof pages 1-2) | GWAS cross-trait analysis / review background | Bang et al., *Translational Psychiatry* (bang2023genomewideanalysisof pages 1-2) | 2023/Sep |  | https://doi.org/10.1038/s41398-023-02585-1 |
| Mortality | Standardized mortality ratio 5.21 (95% CI 4.10–6.62) (voderholzer2025anorexianervosaanupdate. pages 1-2) | Clinical update / review | Voderholzer et al., *Der Nervenarzt* (voderholzer2025anorexianervosaanupdate. pages 1-2) | 2025/May |  | https://doi.org/10.1007/s00115-025-01820-y |
| Mortality after hospitalization | Among 11,930 AN admissions (mean age 19.9 years; 94.0% female), adjusted all-cause mortality vs other psychiatric admissions was HR 1.04 (95% CI 0.89–1.21); 25% of AN-group deaths were attributed to psychiatric conditions, and 88% of those listed AN itself as underlying cause (22% of all AN-group deaths) (patten2024postdischargemortalityin pages 1-2) | Canadian population-based postdischarge cohort using linked hospital and vital statistics data | Patten et al., *International Journal of Eating Disorders* (patten2024postdischargemortalityin pages 1-2) | 2024/Sep |  | https://doi.org/10.1002/eat.24296 |
| Genetics / risk loci | Conditional FDR analysis identified 58 novel AN loci; 38 unique loci shared with schizophrenia/bipolar disorder/major depression and 45 shared with mood instability/neuroticism/intelligence; functional analyses implicated 65 pathways including “signal by MST1” / Hippo signaling (bang2023genomewideanalysisof pages 1-2) | Cross-trait GWAS analysis using summary statistics from large psychiatric GWAS | Bang et al., *Translational Psychiatry* (bang2023genomewideanalysisof pages 1-2) | 2023/Sep |  | https://doi.org/10.1038/s41398-023-02585-1 |
| Biomarkers / endocrine-metabolic | Meta-analysis found biomarkers significantly higher in AN: acylated ghrelin, ACTH, CTX, cholesterol, cortisol, des-acyl ghrelin, ghrelin, GH, obestatin, soluble leptin receptor; significantly lower: CRP, CD3 positive, CD8, creatinine, estradiol, FSH, free T4, free T3, glucose, insulin, IGF-1, leptin, LH, lymphocyte, prolactin (wu2024peripheralbiomarkersof pages 1-2) | Meta-analysis across 52 peripheral biomarkers | Wu et al., *Nutrients* (wu2024peripheralbiomarkersof pages 1-2) | 2024/Jun |  | https://doi.org/10.3390/nu16132095 |
| Biomarkers / mechanistic interpretation | Review text reports ghrelin and all ghrelin forms higher in AN and leptin lower in AN; discusses hypothesized ghrelin resistance and GH resistance, with high GH but low IGF-1 in AN (wu2024peripheralbiomarkersof pages 9-11) | Discussion section of biomarker meta-analysis | Wu et al., *Nutrients* (wu2024peripheralbiomarkersof pages 9-11) | 2024/Jun |  | https://doi.org/10.3390/nu16132095 |
| Immune / cytokines | In 63 female adolescents with AN vs 41 controls, IL-1β and IL-6 were significantly lower at admission, IL-1β normalized after weight recovery, TNF-α did not differ, and IL-15 was significantly elevated at all time points (kaver2024cytokineandmicrobiome pages 1-2) | Longitudinal adolescent case-control study with admission, discharge, and 1-year follow-up | Käver et al., *Nutrients* (kaver2024cytokineandmicrobiome pages 1-2) | 2024/May |  | https://doi.org/10.3390/nu16111596 |
| Microbiome | Mendelian randomization of 196 gut bacterial taxa identified 9 taxa with potential causal relationships with AN; 5 taxa increased AN risk and 4 taxa were associated with reduced risk, with Lachnospiraceae highlighted as a shared influence across AN and BN (kaver2024cytokineandmicrobiome pages 1-2, wu2024peripheralbiomarkersof pages 1-2) | Mendelian randomization study of gut microbiota and eating disorders | Yu et al., *Frontiers in Microbiology* | 2024/May |  | https://doi.org/10.3389/fmicb.2024.1396932 |
| Cardiovascular complications | In 2,081 patients with AN vs 20,810 controls, 4.8% vs 0.8% had major adverse cardiovascular events (MACE) and 6.0% vs 2.3% had any cardiovascular condition; incidence rates were 9.63 vs 1.65 per 1,000 person-years for MACE and 12.55 vs 4.60 for any cardiovascular condition (tseng2024incidenceandrisk pages 1-2, tseng2024incidenceandrisk pages 4-5) | Matched cohort study | Tseng et al., *JAMA Network Open* (tseng2024incidenceandrisk pages 1-2, tseng2024incidenceandrisk pages 4-5) | 2024/Dec |  | https://doi.org/10.1001/jamanetworkopen.2024.51094 |
| Cardiovascular complications | Adjusted HRs in AN were 3.78 (95% CI 2.83–5.05) for MACE and 1.93 (95% CI 1.54–2.41) for any cardiovascular condition; highest risks included cardiac arrest AHR 34.08 (95% CI 3.40–341.76) and congestive heart failure AHR 4.64 (95% CI 2.62–8.63) (tseng2024incidenceandrisk pages 4-5) | Matched cohort study | Tseng et al., *JAMA Network Open* (tseng2024incidenceandrisk pages 4-5) | 2024/Dec |  | https://doi.org/10.1001/jamanetworkopen.2024.51094 |
| Cardiovascular complications | Five-year cumulative incidence in AN: MACE 4.82% (95% CI 3.85–6.02%) and any cardiovascular condition 6.19% (95% CI 5.19–7.53%); controls: 0.85% and 2.27%, respectively (tseng2024incidenceandrisk pages 4-5) | Matched cohort study | Tseng et al., *JAMA Network Open* (tseng2024incidenceandrisk pages 4-5) | 2024/Dec |  | https://doi.org/10.1001/jamanetworkopen.2024.51094 |
| Treatment / standard FBT outcomes | Recovery rates with standard FBT vary by definition: 50–70% when recovery is defined as maintaining >85% body weight, but 28–50% when both weight restoration and reduction in eating-disorder symptoms are required at end of treatment (pedersen2024modificationstoenhance pages 1-2) | Scoping review of FBT modifications in young people with AN | Pedersen et al., *Psychiatry International* (pedersen2024modificationstoenhance pages 1-2) | 2024/May |  | https://doi.org/10.3390/psychiatryint5020015 |
| Treatment / telehealth FBT | In virtual FBT vs online guided self-help, full remission at end of treatment was 30% vs 11%; at 3-month follow-up, 20% vs 22.2%, respectively. All four reviewed virtual-FBT studies suggested FBT variations can be delivered virtually (pedersen2024modificationstoenhance pages 4-6) | Scoping review; teleconferencing FBT studies in youth with AN | Pedersen et al., *Psychiatry International* (pedersen2024modificationstoenhance pages 4-6) | 2024/May |  | https://doi.org/10.3390/psychiatryint5020015 |
| Treatment / home-based FBT modification | FBT-informed home treatment showed significantly higher weight gain by 3 months with medium effect size; EDE change by 3 months was nonsignificant; hospitalization by 3 months was 0% vs 13.6% (significance not reported) (pedersen2024modificationstoenhance pages 4-6) | Comparative modification study summarized in scoping review | Pedersen et al., *Psychiatry International* (pedersen2024modificationstoenhance pages 4-6) | 2024/May |  | https://doi.org/10.3390/psychiatryint5020015 |
| Treatment / telehealth access review | For medically stable adolescents, outpatient FBT is the recommended and most researched model; telehealth-delivered FBT shows preliminary outcomes comparable to in-person care (hambleton2025advancementsinfamilybased pages 1-2) | Narrative review of access barriers and telehealth solutions | Hambleton et al., *Nutrients* (hambleton2025advancementsinfamilybased pages 1-2) | 2025/Jun |  | https://doi.org/10.3390/nu17132160 |


*Table: This table summarizes key recent evidence across core anorexia nervosa domains, prioritizing 2023–2024 studies where available. It highlights quantitative findings useful for a disease knowledge base, including epidemiology, mortality, genetics, biomarkers, cardiovascular complications, and treatment implementation data.*


---

## 1. Disease Information

### 1.1 Concise overview
AN is “an eating disorder characterized by the restriction of energy intake, fear of gaining weight despite low weight, and disturbances in the perception of body weight or shape and the influence of these factors on self-worth.” (wu2024peripheralbiomarkersof pages 1-2)

### 1.2 Key identifiers (ontology/coding)
- **MONDO**: *anorexia nervosa* = **MONDO_0005351** (Open Targets disease entity; used for disease-target aggregation). (voderholzer2025anorexianervosaanupdate. pages 1-2)
- **ICD-11**: AN = **6B80**. Krawczyk & Święcicki state: “The most extensive category is ‘anorexia nervosa’ (6B80).” (Psychiatria Polska, 2020-02; https://doi.org/10.12740/pp/103876). (krawczyk2020icd11vs.icd10 pages 7-10)
- **ICD-10**: commonly coded as **F50.0** and **F50.1** in administrative datasets (used to identify AN admissions in a national Canadian hospitalization cohort). (patten2024postdischargemortalityin pages 1-2)
- **Orphanet**: early-onset/prepubertal anorexia nervosa (EOAN) referenced as **ORPHA 525738** (rare early-onset subtype/descriptor). (ayrolles2024earlyonsetanorexianervosa pages 1-2)

**Note on DSM-5/DSM-5-TR:** Direct DSM-5 text was not retrieved in the accessible full-text set in this run; however, ICD-11 definitional text and multiple peer-reviewed studies provide DSM-aligned core features (restriction → low weight; weight/shape overvaluation and/or fear of weight gain; weight-restoration prevention behaviors). (radden2022capturingtheanorexia pages 1-2, wu2024peripheralbiomarkersof pages 1-2, voderholzer2025anorexianervosaanupdate. pages 1-2)

### 1.3 Synonyms / alternative names
- **Anorexia nervosa** (standard)
- **Jadłowstręt psychiczny** (Polish ICD discussion) as the AN descriptor in ICD-11 context. (krawczyk2020icd11vs.icd10 pages 7-10)
- **Early-onset / prepubertal anorexia nervosa (EOAN)** (rare early-onset form). (ayrolles2024earlyonsetanorexianervosa pages 1-2)

### 1.4 Evidence source type
This report integrates:
- **Aggregated disease-level resources** (rapid reviews, meta-analyses) (hay2023epidemiologyofeating pages 1-2, wu2024peripheralbiomarkersof pages 1-2)
- **Population registries / administrative health data** (mortality; cardiovascular outcomes) (patten2024postdischargemortalityin pages 1-2, tseng2024incidenceandrisk pages 4-5)
- **Human case-control/longitudinal clinical biomarker studies** (cytokines) (kaver2024cytokineandmicrobiome pages 1-2)
- **GWAS summary-statistics analyses** (genetic architecture) (bang2023genomewideanalysisof pages 1-2)
- **ClinicalTrials.gov trial registry entries** (ongoing/registered interventions). (NCT05918835 chunk 1, NCT05788042 chunk 1)


---

## 2. Etiology

### 2.1 Disease causal factors (multifactorial model)
Recent clinical synthesis emphasizes that AN has a multifactorial etiology including **biological**, **psychological**, and **sociocultural** contributors. (voderholzer2025anorexianervosaanupdate. pages 1-2)

#### Genetic causality / susceptibility
- AN is described as **heritable**, with **twin-based heritability ~50–60%**. (bang2023genomewideanalysisof pages 1-2)
- A 2023 genome-wide cross-trait analysis leveraged genetic overlap with major psychiatric disorders and related traits to identify **58 novel AN loci** using conditional FDR methods and found shared loci with schizophrenia, bipolar disorder, major depression, and psychological traits. (bang2023genomewideanalysisof pages 1-2)

**Direct abstract quote (genetics, Bang 2023):** “Anorexia nervosa (AN) is a heritable eating disorder (50–60%)…” and “Using conditional FDR we identified 58 novel AN loci.” (Translational Psychiatry, 2023-09; https://doi.org/10.1038/s41398-023-02585-1). (bang2023genomewideanalysisof pages 1-2)

#### Environmental / psychosocial causal factors (risk domains)
A recent update summarized risk domains including:
- **Sociocultural**: unrealistic body ideals, social media/screen time, societal pressure, obesogenic environments. (voderholzer2025anorexianervosaanupdate. pages 1-2)
- **Psychological traits**: perfectionism, low self-esteem, emotional dysregulation, neuroticism, disgust sensitivity; compulsive/impulsive traits. (voderholzer2025anorexianervosaanupdate. pages 1-2)
- **Stress/trauma**: stressful life events (moving, conflicts, bullying, losses, abuse) and vulnerable developmental windows (e.g., puberty). (voderholzer2025anorexianervosaanupdate. pages 2-3)
- **Comorbid psychiatric and neurodevelopmental conditions**: anxiety/depression/PTSD, autism spectrum disorders, ADHD. (voderholzer2025anorexianervosaanupdate. pages 1-2)
- **Somatic/medical triggers**: celiac disease, diabetes mellitus, and post-bariatric surgery states are cited as risk/trigger contexts. (voderholzer2025anorexianervosaanupdate. pages 1-2, voderholzer2025anorexianervosaanupdate. pages 2-3)

### 2.2 Protective factors
Specific protective factors were not explicitly enumerated in the retrieved full texts in this run. Given the strong evidence base for early identification and treatment being associated with better outcomes in youth, “early detection/treatment” can be considered a pragmatic protective factor against chronicity/complications rather than onset prevention. (voderholzer2025anorexianervosaanupdate. pages 1-2)

### 2.3 Gene–environment interactions
Direct gene–environment interaction (GxE) analyses were not present in the extracted materials. However, multiple sources highlight epigenetics and environment-mediated pathways as plausible mediators linking risk exposures to biological changes. (kaver2024cytokineandmicrobiome pages 1-2)


---

## 3. Phenotypes

### 3.1 Core clinical phenotypes (symptoms/signs)
Key clinical features include:
- **Self-induced weight loss** via restrictive eating and/or compensatory behaviors (vomiting, laxatives, excessive exercise). (voderholzer2025anorexianervosaanupdate. pages 1-2)
- **Distorted body image** and **intense fear of gaining weight** (noted as typical associations in ICD-11 framing). (voderholzer2025anorexianervosaanupdate. pages 1-2, radden2022capturingtheanorexia pages 1-2)
- **Hyperactivity/excessive exercise** is frequent and difficult to treat; one inpatient sample reported **52.3%** prevalence of compulsive/excessive exercise. (voderholzer2025anorexianervosaanupdate. pages 2-3)

**HPO suggestions (labels; IDs not asserted here):** low body weight; food restriction; fear of weight gain; body image distortion; hyperactivity/excessive exercise; anxiety. (voderholzer2025anorexianervosaanupdate. pages 1-2, voderholzer2025anorexianervosaanupdate. pages 2-3)

### 3.2 Medical complications (major systems)
The syndrome is associated with multi-system complications driven by malnutrition and starvation physiology.

#### Cardiovascular
A large matched cohort study (Taiwanese claims database) reported markedly increased cardiovascular events:
- **MACE** occurred in **4.8%** of AN vs **0.8%** of controls; incidence rates **9.63 vs 1.65 per 1000 person-years**; adjusted HR (AHR) **3.78** (95% CI 2.83–5.05). (tseng2024incidenceandrisk pages 4-5)
- **Any cardiovascular condition**: **6.0%** vs **2.3%**; incidence rates **12.55 vs 4.60 per 1000 person-years**; AHR **1.93** (95% CI 1.54–2.41). (tseng2024incidenceandrisk pages 4-5)
- Five-year cumulative incidence in AN: **MACE 4.82%** (95% CI 3.85–6.02%) and **any cardiovascular condition 6.19%** (95% CI 5.19–7.53%). (tseng2024incidenceandrisk pages 4-5)

These findings are also reflected in the retrieved Table 2/Figure 1 snippet. (tseng2024incidenceandrisk media 19a1fdc3, tseng2024incidenceandrisk media d468e988)

**HPO suggestions:** bradycardia; hypotension; cardiac arrhythmia; QT prolongation; congestive heart failure. (tseng2024incidenceandrisk pages 1-2, voderholzer2025anorexianervosaanupdate. pages 3-4)

#### Electrolyte/renal/bone complications
A clinical update describes complications including electrolyte disturbances (e.g., hypokalemia; magnesium deficiency; hyponatremia in polydipsia contexts), renal impairment up to dialysis dependency, and irreversible bone loss (osteopenia/osteoporosis) with prevention/treatment considerations (calcium, vitamin D, bisphosphonates, transdermal estradiol). (voderholzer2025anorexianervosaanupdate. pages 2-3)

**HPO suggestions:** hypokalemia; hyponatremia; renal impairment; osteoporosis/osteopenia. (voderholzer2025anorexianervosaanupdate. pages 2-3)

### 3.3 Age of onset / severity / progression
- AN “typically manifests during adolescence.” (kaver2024cytokineandmicrobiome pages 1-2)
- Early-onset/prepubertal AN can have onset as early as **8 years**, with operational cutoffs around **≤13 years** (or ≤14 in some studies), but evidence for child-specific treatments remains limited; guidelines often extrapolate from adolescent/young adult strategies with low evidence. (ayrolles2024earlyonsetanorexianervosa pages 1-2)

### 3.4 Quality-of-life impact
Eating disorders substantially reduce health-related quality of life across diagnoses; a meta-analysis cited in a rapid review found similarly low HRQoL across AN, BN, and BED (with some variation by study). (hay2023epidemiologyofeating pages 37-38)


---

## 4. Genetic / Molecular Information

### 4.1 “Causal genes” vs polygenic risk
AN is not established as a monogenic disorder in the retrieved evidence; current genetics support **polygenic inheritance** with many loci of small effect and substantial shared genetic architecture with other psychiatric traits. (bang2023genomewideanalysisof pages 1-2)

### 4.2 GWAS loci and pathways (recent developments)
- **58 novel AN loci** were identified in a 2023 analysis leveraging genetic overlap with major psychiatric disorders and traits via conditional FDR. (bang2023genomewideanalysisof pages 1-2)
- Functional analyses implicated **65 unique pathways**, including “**signal by MST1**” in **Hippo signaling**. (bang2023genomewideanalysisof pages 1-2)

**Ontology suggestions (GO; labels):** Hippo signaling; synapse organization; nervous system development/neurogenesis; stress response/immune-response pathways (pathway-level mapping supported by GWAS functional analyses and neuroimaging review themes). (bang2023genomewideanalysisof pages 1-2, chen2024neuroimagingstudiesof pages 1-2)

### 4.3 Disease-target associations (authoritative aggregation)
Open Targets disease-target aggregation identifies associated targets including (examples): **DRD2, ESR1, NCAM1, CACNA1C, TCF4** with PubMed literature links. This should be treated as *association evidence* rather than proof of causality. (voderholzer2025anorexianervosaanupdate. pages 1-2)

### 4.4 Epigenetics
Direct epigenetic marks were not extracted from the retrieved full texts; however, adolescent immune/microbiome work explicitly frames AN etiology as involving “genetics, epigenetics, neurobiology, cognition, psychosocial” factors. (kaver2024cytokineandmicrobiome pages 1-2)


---

## 5. Environmental Information

### 5.1 Environmental/lifestyle contributing factors
A clinical update describes multiple environmental/lifestyle factors relevant to onset and maintenance:
- exposure to thin-ideal messaging/social media
- restrictive diets, excessive physical activity
- stressors (bullying, conflicts, life events)
- family dynamics and societal reinforcement. (voderholzer2025anorexianervosaanupdate. pages 1-2, voderholzer2025anorexianervosaanupdate. pages 2-3)

### 5.2 Infectious agents
No infectious etiology is implicated in the retrieved evidence (not applicable).


---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (high-level)
A consistent mechanistic framing from recent evidence is:
1) **Predisposition** (polygenic psychiatric + metabolic liability) (bang2023genomewideanalysisof pages 1-2)
2) **Behavioral restriction / compensatory behaviors** → **negative energy balance** (voderholzer2025anorexianervosaanupdate. pages 1-2)
3) **Starvation physiology** (endocrine/metabolic adaptation) including altered appetite hormones and GH–IGF-1 axis changes (wu2024peripheralbiomarkersof pages 9-11)
4) **Systemic complications** (electrolyte disturbances; cardiovascular, renal, bone impacts) (voderholzer2025anorexianervosaanupdate. pages 2-3, tseng2024incidenceandrisk pages 1-2)
5) **Neurocognitive/neurocircuit features** (altered functional connectivity and reward/control circuitry) that may reinforce restrictive behavior (chen2024neuroimagingstudiesof pages 1-2)

### 6.2 Endocrine/metabolic adaptations (biomarkers)
A 2024 meta-analysis of peripheral biomarkers reported higher ghrelin forms and lower leptin, and discusses “ghrelin resistance” hypotheses and GH resistance (high GH, low IGF-1) as starvation-adaptation patterns in AN. (wu2024peripheralbiomarkersof pages 1-2, wu2024peripheralbiomarkersof pages 9-11)

**CHEBI suggestions (labels):** ghrelin; leptin; cortisol; glucose; insulin; IGF-1. (wu2024peripheralbiomarkersof pages 1-2)

### 6.3 Immune involvement (recent human data)
In adolescents, cytokine dysregulation may differ from adult low-grade pro-inflammatory assumptions:
- In 63 female adolescents with AN vs 41 controls, IL-1β and IL-6 were lower at admission; IL-1β normalized after weight recovery; IL-15 was elevated at all time points; TNF-α did not differ. (kaver2024cytokineandmicrobiome pages 1-2)

**GO suggestions (labels):** cytokine-mediated signaling pathway; regulation of interleukin-15 production/signaling; inflammatory response (nuanced). (kaver2024cytokineandmicrobiome pages 1-2)

### 6.4 Microbiome–gut–brain axis
- Mendelian randomization suggests potential causal roles of specific gut taxa (e.g., a subset increasing risk and a subset protective), highlighting the plausibility of microbiome-mediated pathways as intervention targets. (kaver2024cytokineandmicrobiome pages 1-2)
- The adolescent cytokine study links microbiome composition with cytokine alterations and clinical variables. (kaver2024cytokineandmicrobiome pages 1-2)

### 6.5 Neurobiology / neuroimaging
Resting-state fMRI synthesis reports altered large-scale networks in eating disorders; in AN, findings include altered connectivity patterns involving DMN, salience and executive networks and regions tied to social cognition and sensory/aesthetic processing. (chen2024neuroimagingstudiesof pages 1-2)

**UBERON suggestions (labels):** brain; hypothalamus; cortex; cerebellum; pituitary. (supported by genetic enrichment and neuroimaging emphasis on brain regions/networks). (chen2024neuroimagingstudiesof pages 1-2, bang2023genomewideanalysisof pages 1-2)

**CL suggestions (labels):** hypothalamic neuron; cortical neuron; microglia; T cell/lymphocyte populations (as biomarkers include CD3/CD8 and immune discussion). (wu2024peripheralbiomarkersof pages 1-2)


---

## 7. Anatomical Structures Affected

### Organ/system level
- **Central nervous system** (reward, appetite and emotion regulation circuitry; altered functional connectivity). (chen2024neuroimagingstudiesof pages 1-2, voderholzer2025anorexianervosaanupdate. pages 1-2)
- **Cardiovascular system** (MACE and multiple cardiac disorders). (tseng2024incidenceandrisk pages 4-5)
- **Endocrine/metabolic systems** (ghrelin/leptin, cortisol, GH–IGF-1 axis). (wu2024peripheralbiomarkersof pages 1-2, wu2024peripheralbiomarkersof pages 9-11)
- **Skeletal system** (osteopenia/osteoporosis). (voderholzer2025anorexianervosaanupdate. pages 2-3)
- **Renal system** (renal impairment in severe disease). (voderholzer2025anorexianervosaanupdate. pages 2-3)

### Subcellular / processes
Starvation-associated shifts include metabolic pathway changes and immune signaling alterations; refeeding syndrome risk is linked to intracellular phosphate depletion as a key mechanism described in clinical synthesis. (voderholzer2025anorexianervosaanupdate. pages 3-4)


---

## 8. Temporal Development

### Onset
- Peak onset often in adolescence/young adulthood; EOAN can occur in childhood (as early as 8 years). (ayrolles2024earlyonsetanorexianervosa pages 1-2, kaver2024cytokineandmicrobiome pages 1-2)

### Course / remission
- A cited meta-analytic outcome summary in a clinical update reported: **45% recovery**, **24% improvement**, **23% chronicity**, **32% hospitalization rate**, and **0.7% mortality rate** (context: meta-analysis summarized in the update). (voderholzer2025anorexianervosaanupdate. pages 2-3)


---

## 9. Inheritance and Population

### Epidemiology (selected recent quantitative data)
- Global lifetime prevalence of any eating disorder: **0.74–2.2% in males** and **2.58–8.4% in females** (rapid review). (hay2023epidemiologyofeating pages 1-2)
- AN lifetime prevalence varies with definitional strictness: **0.6–2.2% (strict)**; **1.7–4.3% (broad)** (rapid review). (hay2023epidemiologyofeating pages 37-38)
- Another synthesis/meta-analysis context reports global AN prevalence **1.4% (women) and 0.2% (men)**. (wu2024peripheralbiomarkersof pages 1-2)
- Sex ratio: adolescent clinical paper notes male-to-female ratio **1:10–1:20**. (kaver2024cytokineandmicrobiome pages 1-2)

### Heritability / inheritance pattern
- Polygenic/multifactorial inheritance with **~50–60% heritability** estimates. (bang2023genomewideanalysisof pages 1-2)

### High-risk/underserved populations (policy-relevant)
In Australia-focused rapid review, LGBTQI+ individuals—particularly males—were reported to have a **six-fold increase** in prevalence vs the general male population, with limited evidence available for other underserved populations. (hay2023epidemiologyofeating pages 1-2)


---

## 10. Diagnostics

### 10.1 Clinical criteria and ICD-11 definitional specifics
ICD-11 definition details reproduced/analysed by Radden (2022) include:
- “Dangerously low body weight” benchmarks: adult **BMI <18.5** at age 18; for children/adolescents BMI-for-age below the **5th percentile** as a benchmark. (radden2022capturingtheanorexia pages 1-2, radden2022capturingtheanorexia pages 2-3)
- Low weight is accompanied by behaviors preventing weight restoration (restriction, purging, excessive exercise) and weight/shape centrality to self-evaluation or misperception of normality/excess. (radden2022capturingtheanorexia pages 1-2)
- ICD-11 demotes fear of weight gain from essential to “typically” associated. (radden2022capturingtheanorexia pages 2-3)

A clinical update also emphasizes ICD-11 removal of **amenorrhea as a mandatory criterion**, facilitating diagnosis in men, prepubertal children, and women on hormonal contraception. (voderholzer2025anorexianervosaanupdate. pages 1-2)

### 10.2 Biomarkers (not yet established for routine diagnosis)
The 2024 meta-analysis concludes that reliable biomarkers are not yet established but identifies multiple peripheral biomarker differences (e.g., ghrelin ↑, leptin ↓, IGF-1 ↓) that may relate to starvation adaptation and pathophysiology. (wu2024peripheralbiomarkersof pages 1-2)

### 10.3 Differential diagnosis (example explicitly referenced)
A clinical update highlights differentiation from **ARFID** (avoidant/restrictive food intake disorder; ICD-11 6B83) as a key diagnostic distinction. (voderholzer2025anorexianervosaanupdate. pages 2-3)


---

## 11. Outcome / Prognosis

### Mortality
- A recent clinical update reports standardized mortality ratio (SMR) **5.21 (95% CI 4.10–6.62)**. (voderholzer2025anorexianervosaanupdate. pages 1-2)
- Postdischarge mortality study (Canada): after age/sex adjustment, no significant all-cause mortality difference between AN and other psychiatric admissions (HR **1.04**; p=0.46), but AN contributed substantially to cause-of-death coding: **25%** of AN-group deaths attributed to psychiatric ICD-F conditions; **88%** of those had AN as underlying cause (22% of all AN-group deaths). (patten2024postdischargemortalityin pages 1-2)

### Morbidity / complications
Cardiovascular morbidity is strongly supported by a 2024 cohort with increased MACE and multiple cardiac diagnoses. (tseng2024incidenceandrisk pages 4-5)

### Prognostic factors
The FBT modification review notes predictors of poorer response to standard FBT (e.g., cognitive inflexibility, familial criticism, slow initial weight gain), but detailed prognostic modeling is beyond the extracted evidence. (pedersen2024modificationstoenhance pages 1-2)


---

## 12. Treatment

### 12.1 Core treatment modalities (current practice)
- **Psychotherapy** is first-line: clinical update cites **CBT** (adolescents and adults) and **FBT** as most extensively studied for children/adolescents; also references FPT and MANTRA. (voderholzer2025anorexianervosaanupdate. pages 3-4)
- **Nutritional rehabilitation / inpatient refeeding** reduces acute mortality risk through weight restoration; however, refeeding carries risks including refeeding syndrome and requires careful medical management (phosphate depletion mechanism emphasized). (hambleton2025advancementsinfamilybased pages 1-2, voderholzer2025anorexianervosaanupdate. pages 3-4)
- **Pharmacotherapy**: limited robust evidence; **olanzapine** has “moderate evidence” for weight gain in a clinical update. (voderholzer2025anorexianervosaanupdate. pages 1-2)

### 12.2 Treatment outcomes and real-world implementation
**Family-Based Treatment (FBT) outcomes and modifications (2024 scoping review)**
- Standard FBT recovery rates depend on definition: **50–70%** when recovery defined as maintaining **>85% body weight** vs **28–50%** when both weight restoration and symptom reduction required at end of treatment. (pedersen2024modificationstoenhance pages 1-2)
- Virtual FBT evidence: in one comparison, full remission at end of treatment **30% (V-FBT)** vs **11% (guided self-help)**; at 3-month follow-up **20% vs 22.2%**. (pedersen2024modificationstoenhance pages 4-6)
- Home-treatment modification: significantly higher weight gain by 3 months (medium effect size) and hospitalization **0% vs 13.6%** at 3 months (significance not reported). (pedersen2024modificationstoenhance pages 4-6)

**Access barriers and telehealth**
A telehealth-focused review concludes that telehealth-delivered FBT shows preliminary outcomes comparable to in-person care while potentially increasing access in underserved areas. (hambleton2025advancementsinfamilybased pages 1-2)

### 12.3 Experimental/advanced therapeutics (clinical trials)
Neuromodulation is actively studied:
- **NCT05918835** (registered 2023; recruiting; n=72): HF-rTMS vs sham for adults with AN, targeting individualized right DLPFC region functionally connected to dorsal striatum. (NCT05918835 chunk 1)
- **NCT05788042** (registered 2023; recruiting; n=70): tDCS and rTMS (iTBS) vs sham arms, primary outcome EDE-Q change at 8 weeks. (NCT05788042 chunk 1)
- Additional rTMS/TBS studies include NCT03984344 and others with varying status (recruiting/terminated/withdrawn). (NCT03984344 chunk 1, NCT04061304 chunk 1)

**MAXO suggestions (labels):** cognitive behavioral therapy; family-based treatment; nutritional rehabilitation; inpatient hospitalization/medical stabilization; olanzapine therapy; repetitive transcranial magnetic stimulation; transcranial direct current stimulation. (voderholzer2025anorexianervosaanupdate. pages 3-4, NCT05788042 chunk 1)


---

## 13. Prevention

### Primary/secondary/tertiary prevention (evidence-based framing)
Specific preventive interventions were not detailed in retrieved guideline-level sources. However:
- Rapid review emphasizes low help-seeking and under-recognition, supporting **secondary prevention via early identification and access to evidence-based care**. (hay2023epidemiologyofeating pages 37-38)
- Clinical update highlights improved outcomes with earlier detection and treatment, especially in youth. (voderholzer2025anorexianervosaanupdate. pages 1-2)


---

## 14. Other Species / Natural Disease
No naturally occurring veterinary anorexia nervosa analogs were identified in the retrieved evidence (not addressed in this run).


---

## 15. Model Organisms
In this run, retrieved evidence did not include a primary model-organism paper suitable for detailed mapping. Mechanistic microbiome work in other parts of the retrieved corpus (not fully extracted) suggests germ-free/transfer paradigms are used in the field, but this report does not assert specifics without extracted evidence.


---

## Notes on Evidence Quality and Gaps
- **DSM-5-TR diagnostic criteria, MeSH identifier, and OMIM/Orphanet entries for AN (general)** were not directly retrieved as primary documents in the accessible full texts; the report therefore anchors identifiers to ICD-11/ICD-10 and MONDO/OpenTargets plus peer-reviewed definitional text. (krawczyk2020icd11vs.icd10 pages 7-10, patten2024postdischargemortalityin pages 1-2, voderholzer2025anorexianervosaanupdate. pages 1-2)
- Some mechanistic domains (epigenome-wide methylation studies; transcriptomics/proteomics; single-cell/spatial omics in humans) were not captured in the extracted 2023–2024 evidence set in this run.


---

## Direct Abstract Quotes (for knowledge-base evidence items)
1) Biomarker meta-analysis definition: “an eating disorder characterized by the restriction of energy intake, fear of gaining weight despite low weight, and disturbances in the perception of body weight or shape…” (Wu et al., *Nutrients*, 2024-06; https://doi.org/10.3390/nu16132095). (wu2024peripheralbiomarkersof pages 1-2)
2) Genetics: “Anorexia nervosa (AN) is a heritable eating disorder (50–60%)…” and “Using conditional FDR we identified 58 novel AN loci.” (Bang et al., *Translational Psychiatry*, 2023-09; https://doi.org/10.1038/s41398-023-02585-1). (bang2023genomewideanalysisof pages 1-2)
3) ICD-11 code statement: “The most extensive category is ‘anorexia nervosa’ (6B80).” (Krawczyk & Święcicki, *Psychiatria Polska*, 2020-02; https://doi.org/10.12740/pp/103876). (krawczyk2020icd11vs.icd10 pages 7-10)


---

## Key Figure/Table Evidence (visual)
Tseng et al. (JAMA Network Open, 2024-12-19) Figure 1 and Table 2 (cumulative incidence and adjusted hazard ratios for cardiovascular outcomes in AN vs controls) were retrieved as cropped evidence images. (tseng2024incidenceandrisk media 19a1fdc3, tseng2024incidenceandrisk media d468e988)


References

1. (wu2024peripheralbiomarkersof pages 1-2): Ya-Ke Wu, Hunna J. Watson, Aaron C. Del Re, Jody E. Finch, Sabrina L. Hardin, Alexis S. Dumain, Kimberly A. Brownley, and Jessica H. Baker. Peripheral biomarkers of anorexia nervosa: a meta-analysis. Nutrients, 16:2095, Jun 2024. URL: https://doi.org/10.3390/nu16132095, doi:10.3390/nu16132095. This article has 22 citations.

2. (bang2023genomewideanalysisof pages 1-2): Lasse Bang, Shahram Bahrami, Guy Hindley, Olav B. Smeland, Linn Rødevand, Piotr P. Jaholkowski, Alexey Shadrin, Kevin S. O’ Connell, Oleksandr Frei, Aihua Lin, Zillur Rahman, Weiqiu Cheng, Nadine Parker, Chun C. Fan, Anders M. Dale, Srdjan Djurovic, Cynthia M. Bulik, and Ole A. Andreassen. Genome-wide analysis of anorexia nervosa and major psychiatric disorders and related traits reveals genetic overlap and identifies novel risk loci for anorexia nervosa. Translational Psychiatry, Sep 2023. URL: https://doi.org/10.1038/s41398-023-02585-1, doi:10.1038/s41398-023-02585-1. This article has 36 citations and is from a peer-reviewed journal.

3. (tseng2024incidenceandrisk pages 1-2): Mei-Chih Meg Tseng, Kuan-Rau Chiou, Joni Yu-Hsuan Shao, and Hung-Yi Liu. Incidence and risk of cardiovascular outcomes in patients with anorexia nervosa. JAMA Network Open, 7:e2451094, Dec 2024. URL: https://doi.org/10.1001/jamanetworkopen.2024.51094, doi:10.1001/jamanetworkopen.2024.51094. This article has 13 citations and is from a peer-reviewed journal.

4. (chen2024neuroimagingstudiesof pages 1-2): Xiong Chen, Chunqi Ai, Zhongchun Liu, and Gang Wang. Neuroimaging studies of resting-state functional magnetic resonance imaging in eating disorders. BMC Medical Imaging, Oct 2024. URL: https://doi.org/10.1186/s12880-024-01432-z, doi:10.1186/s12880-024-01432-z. This article has 29 citations and is from a peer-reviewed journal.

5. (voderholzer2025anorexianervosaanupdate. pages 1-2): Ulrich Voderholzer, Silke Naab, Ulrich Cuntz, and Sandra Schlegl. Anorexia nervosa-an update. Der Nervenarzt, May 2025. URL: https://doi.org/10.1007/s00115-025-01820-y, doi:10.1007/s00115-025-01820-y. This article has 5 citations.

6. (patten2024postdischargemortalityin pages 1-2): Scott B. Patten, Gina Dimitropoulos, Julia Hews‐Girard, Amelia Austin, Vandad Sharifi, Jeanne Williams, Anees Bahji, and Andrew Bulloch. Postdischarge mortality in a cohort hospitalized with anorexia nervosa. The International Journal of Eating Disorders, 57:2482-2486, Sep 2024. URL: https://doi.org/10.1002/eat.24296, doi:10.1002/eat.24296. This article has 3 citations.

7. (wu2024peripheralbiomarkersof pages 9-11): Ya-Ke Wu, Hunna J. Watson, Aaron C. Del Re, Jody E. Finch, Sabrina L. Hardin, Alexis S. Dumain, Kimberly A. Brownley, and Jessica H. Baker. Peripheral biomarkers of anorexia nervosa: a meta-analysis. Nutrients, 16:2095, Jun 2024. URL: https://doi.org/10.3390/nu16132095, doi:10.3390/nu16132095. This article has 22 citations.

8. (kaver2024cytokineandmicrobiome pages 1-2): Larissa Käver, Clara Voelz, Hannah E Specht, Anna C Thelen, Lara Keller, Brigitte Dahmen, Nadia Andrea Andreani, Klaus Tenbrock, Ronald Biemann, Katrin Borucki, Astrid Dempfle, John F Baines, Cordian Beyer, Beate Herpertz-Dahlmann, Stefanie Trinh, and Jochen Seitz. Cytokine and microbiome changes in adolescents with anorexia nervosa at admission, discharge, and one-year follow-up. Nutrients, May 2024. URL: https://doi.org/10.3390/nu16111596, doi:10.3390/nu16111596. This article has 12 citations.

9. (tseng2024incidenceandrisk pages 4-5): Mei-Chih Meg Tseng, Kuan-Rau Chiou, Joni Yu-Hsuan Shao, and Hung-Yi Liu. Incidence and risk of cardiovascular outcomes in patients with anorexia nervosa. JAMA Network Open, 7:e2451094, Dec 2024. URL: https://doi.org/10.1001/jamanetworkopen.2024.51094, doi:10.1001/jamanetworkopen.2024.51094. This article has 13 citations and is from a peer-reviewed journal.

10. (pedersen2024modificationstoenhance pages 1-2): Signe Holm Pedersen, Lasse Carlsson, and Mette Bentz. Modifications to enhance outcomes of family-based treatment for anorexia nervosa: a scoping review. Psychiatry International, 5:217-230, May 2024. URL: https://doi.org/10.3390/psychiatryint5020015, doi:10.3390/psychiatryint5020015. This article has 5 citations.

11. (pedersen2024modificationstoenhance pages 4-6): Signe Holm Pedersen, Lasse Carlsson, and Mette Bentz. Modifications to enhance outcomes of family-based treatment for anorexia nervosa: a scoping review. Psychiatry International, 5:217-230, May 2024. URL: https://doi.org/10.3390/psychiatryint5020015, doi:10.3390/psychiatryint5020015. This article has 5 citations.

12. (hambleton2025advancementsinfamilybased pages 1-2): Ashlea Hambleton, Daniel Le Grange, Stephen Touyz, and Sarah Maguire. Advancements in family-based treatment of adolescent anorexia nervosa: a review of access barriers and telehealth solutions. Nutrients, 17:2160, Jun 2025. URL: https://doi.org/10.3390/nu17132160, doi:10.3390/nu17132160. This article has 4 citations.

13. (krawczyk2020icd11vs.icd10 pages 7-10): Piotr Krawczyk and Łukasz Święcicki. Icd-11 vs. icd-10 – a review of updates and novelties introduced in the latest version of the who international classification of diseases. Psychiatria Polska, 54:7-20, Feb 2020. URL: https://doi.org/10.12740/pp/103876, doi:10.12740/pp/103876. This article has 93 citations.

14. (ayrolles2024earlyonsetanorexianervosa pages 1-2): Anaël Ayrolles, Julia Clarke, Nathalie Godart, Céline André-Carletti, Clémentine Barbe, Anne Bargiacchi, Corinne Blanchet, Florence Bergametti, Valérie Bertrand, Emmanuelle Caldagues, Marylene Caquard, Danielle Castellotti, Richard Delorme, Laurence Dreno, Dominique Feneon Landou, Priscille Gerardin, Selim Guessoum, Ludovic Gicquel, Juliane Léger, Stéphanie Legras, Lucile Noel, Anne Fjellestad-Paulsen, Hélène Poncet-Kalifa, Flora Bat-Pitault, and Coline Stordeur. Early-onset anorexia nervosa: a scoping review and management guidelines. Journal of Eating Disorders, Nov 2024. URL: https://doi.org/10.1186/s40337-024-01130-9, doi:10.1186/s40337-024-01130-9. This article has 12 citations and is from a peer-reviewed journal.

15. (radden2022capturingtheanorexia pages 1-2): Jennifer Radden. Capturing the anorexia nervosa phenotype: conceptual and normative issues in icd-11. Journal of evaluation in clinical practice, 28:807-813, Jun 2022. URL: https://doi.org/10.1111/jep.13586, doi:10.1111/jep.13586. This article has 8 citations and is from a peer-reviewed journal.

16. (hay2023epidemiologyofeating pages 1-2): Phillipa Hay, Phillip Aouad, Anvi Le, Peta Marks, Danielle Maloney, Sarah Barakat, Robert Boakes, Leah Brennan, Emma Bryant, Susan Byrne, Belinda Caldwell, Shannon Calvert, Bronny Carroll, David Castle, Ian Caterson, Belinda Chelius, Lyn Chiem, Simon Clarke, Janet Conti, Lexi Crouch, Genevieve Dammery, Natasha Dzajkovski, Jasmine Fardouly, John Feneley, Nasim Foroughi, Mathew Fuller-Tyszkiewicz, Anthea Fursland, Veronica Gonzalez-Arce, Bethanie Gouldthorp, Kelly Griffin, Scott Griffiths, Ashlea Hambleton, Amy Hannigan, Mel Hart, Susan Hart, Ian Hickie, Francis Kay-Lambkin, Ross King, Michael Kohn, Eyza Koreshe, Isabel Krug, Jake Linardon, Randall Long, Amanda Long, Sloane Madden, Siân McLean, Thy Meddick, Jane Miskovic-Wheatley, Deborah Mitchison, Richard O’Kearney, Roger Paterson, Susan Paxton, Melissa Pehlivan, Genevieve Pepin, Andrea Phillipou, Judith Piccone, Rebecca Pinkus, Bronwyn Raykos, Paul Rhodes, Elizabeth Rieger, Karen Rockett, Sarah Rodan, Janice Russell, Haley Russell, Fiona Salter, Susan Sawyer, Beth Shelton, Urvashnee Singh, Sophie Smith, Evelyn Smith, Karen Spielman, Sarah Squire, Juliette Thomson, Marika Tiggemann, Ranjani Utpala, Lenny Vartanian, Andrew Wallis, Warren Ward, Sarah Wells, Eleanor Wertheim, Simon Wilksch, Michelle Williams, Stephen Touyz, and Sarah Maguire. Epidemiology of eating disorders: population, prevalence, disease burden and quality of life informing public policy in australia—a rapid review. Journal of Eating Disorders, Feb 2023. URL: https://doi.org/10.1186/s40337-023-00738-7, doi:10.1186/s40337-023-00738-7. This article has 189 citations and is from a peer-reviewed journal.

17. (NCT05918835 chunk 1): Alexandra F Muratore, PhD. Effects of rTMS on Food Choice in Anorexia Nervosa. New York State Psychiatric Institute. 2023. ClinicalTrials.gov Identifier: NCT05918835

18. (NCT05788042 chunk 1):  Trial of Enhanced Neurostimulation for Anorexia. The George Institute. 2023. ClinicalTrials.gov Identifier: NCT05788042

19. (voderholzer2025anorexianervosaanupdate. pages 2-3): Ulrich Voderholzer, Silke Naab, Ulrich Cuntz, and Sandra Schlegl. Anorexia nervosa-an update. Der Nervenarzt, May 2025. URL: https://doi.org/10.1007/s00115-025-01820-y, doi:10.1007/s00115-025-01820-y. This article has 5 citations.

20. (tseng2024incidenceandrisk media 19a1fdc3): Mei-Chih Meg Tseng, Kuan-Rau Chiou, Joni Yu-Hsuan Shao, and Hung-Yi Liu. Incidence and risk of cardiovascular outcomes in patients with anorexia nervosa. JAMA Network Open, 7:e2451094, Dec 2024. URL: https://doi.org/10.1001/jamanetworkopen.2024.51094, doi:10.1001/jamanetworkopen.2024.51094. This article has 13 citations and is from a peer-reviewed journal.

21. (tseng2024incidenceandrisk media d468e988): Mei-Chih Meg Tseng, Kuan-Rau Chiou, Joni Yu-Hsuan Shao, and Hung-Yi Liu. Incidence and risk of cardiovascular outcomes in patients with anorexia nervosa. JAMA Network Open, 7:e2451094, Dec 2024. URL: https://doi.org/10.1001/jamanetworkopen.2024.51094, doi:10.1001/jamanetworkopen.2024.51094. This article has 13 citations and is from a peer-reviewed journal.

22. (voderholzer2025anorexianervosaanupdate. pages 3-4): Ulrich Voderholzer, Silke Naab, Ulrich Cuntz, and Sandra Schlegl. Anorexia nervosa-an update. Der Nervenarzt, May 2025. URL: https://doi.org/10.1007/s00115-025-01820-y, doi:10.1007/s00115-025-01820-y. This article has 5 citations.

23. (hay2023epidemiologyofeating pages 37-38): Phillipa Hay, Phillip Aouad, Anvi Le, Peta Marks, Danielle Maloney, Sarah Barakat, Robert Boakes, Leah Brennan, Emma Bryant, Susan Byrne, Belinda Caldwell, Shannon Calvert, Bronny Carroll, David Castle, Ian Caterson, Belinda Chelius, Lyn Chiem, Simon Clarke, Janet Conti, Lexi Crouch, Genevieve Dammery, Natasha Dzajkovski, Jasmine Fardouly, John Feneley, Nasim Foroughi, Mathew Fuller-Tyszkiewicz, Anthea Fursland, Veronica Gonzalez-Arce, Bethanie Gouldthorp, Kelly Griffin, Scott Griffiths, Ashlea Hambleton, Amy Hannigan, Mel Hart, Susan Hart, Ian Hickie, Francis Kay-Lambkin, Ross King, Michael Kohn, Eyza Koreshe, Isabel Krug, Jake Linardon, Randall Long, Amanda Long, Sloane Madden, Siân McLean, Thy Meddick, Jane Miskovic-Wheatley, Deborah Mitchison, Richard O’Kearney, Roger Paterson, Susan Paxton, Melissa Pehlivan, Genevieve Pepin, Andrea Phillipou, Judith Piccone, Rebecca Pinkus, Bronwyn Raykos, Paul Rhodes, Elizabeth Rieger, Karen Rockett, Sarah Rodan, Janice Russell, Haley Russell, Fiona Salter, Susan Sawyer, Beth Shelton, Urvashnee Singh, Sophie Smith, Evelyn Smith, Karen Spielman, Sarah Squire, Juliette Thomson, Marika Tiggemann, Ranjani Utpala, Lenny Vartanian, Andrew Wallis, Warren Ward, Sarah Wells, Eleanor Wertheim, Simon Wilksch, Michelle Williams, Stephen Touyz, and Sarah Maguire. Epidemiology of eating disorders: population, prevalence, disease burden and quality of life informing public policy in australia—a rapid review. Journal of Eating Disorders, Feb 2023. URL: https://doi.org/10.1186/s40337-023-00738-7, doi:10.1186/s40337-023-00738-7. This article has 189 citations and is from a peer-reviewed journal.

24. (radden2022capturingtheanorexia pages 2-3): Jennifer Radden. Capturing the anorexia nervosa phenotype: conceptual and normative issues in icd-11. Journal of evaluation in clinical practice, 28:807-813, Jun 2022. URL: https://doi.org/10.1111/jep.13586, doi:10.1111/jep.13586. This article has 8 citations and is from a peer-reviewed journal.

25. (NCT03984344 chunk 1):  Theta Burst Stimulation in Anorexia Nervosa. King's College London. 2020. ClinicalTrials.gov Identifier: NCT03984344

26. (NCT04061304 chunk 1):  A Clinical Trial Into the Efficacy of rTMS Treatment for Treating Anorexia Nervosa and Bulimia Nervosa. University of Manitoba. 2020. ClinicalTrials.gov Identifier: NCT04061304