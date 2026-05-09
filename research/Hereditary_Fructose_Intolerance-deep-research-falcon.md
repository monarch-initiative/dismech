---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T19:37:06.346045'
end_time: '2026-05-08T19:53:14.549307'
duration_seconds: 968.2
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hereditary Fructose Intolerance
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Fructose Intolerance
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hereditary Fructose Intolerance** covering all of the
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
- **Disease Name:** Hereditary Fructose Intolerance
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hereditary Fructose Intolerance** covering all of the
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


## Hereditary Fructose Intolerance (HFI): comprehensive disease characteristics report (2023–2024 prioritized)

### Executive summary
Hereditary fructose intolerance (HFI) is a rare **autosomal recessive** inborn error of fructose metabolism caused by **biallelic loss-of-function variants in ALDOB (aldolase B)**, leading to **fructose-1-phosphate (F1P) accumulation** (“phosphate trap”), ATP depletion, and inhibition of glycogenolysis and gluconeogenesis. Clinically, it presents after introduction of fructose/sucrose/sorbitol with **vomiting, abdominal pain/distension, and postprandial hypoglycemia**, and can progress to chronic **hepatic steatosis and renal proximal tubular dysfunction (Fanconi syndrome)** even with treatment. Current standard of care is a **lifelong fructose/sucrose/sorbitol (FSS)-free diet** and avoidance of offending excipients in medicines. Recent mechanistic work (2023–2024) implicates **endogenous fructose generation via the polyol pathway** and a newly highlighted **AMPD2-driven purine degradation axis** as contributors to ongoing liver disease in aldolase B deficiency, while early-phase translational work suggests **ketohexokinase (KHK) inhibition (PF‑06835919)** may increase fructose tolerance and reduce acute toxicity risk. (andreshernando2024activationofampd2 pages 1-2, ubeda2024clinicalpracticeguidelines pages 1-2, ubeda2024clinicalpracticeguidelines pages 2-4, garbowski2024acasestudy pages 9-10, ubeda2024clinicalpracticeguidelines pages 4-5, NCT06089265 chunk 1)

---

## 1. Disease information

### 1.1 Definition and overview
HFI (also called **hereditary fructosemia** and sometimes “**fructosemia**”) is an **autosomal recessive metabolic disorder** due to **aldolase B (ALDOB) deficiency**, with clinical manifestations triggered by exposure to fructose, sucrose, and sorbitol. (ubeda2024clinicalpracticeguidelines pages 1-2, biancalana2024hereditaryfructoseintolerancea pages 36-38, garbowski2024acasestudy pages 5-6)

### 1.2 Key identifiers (with availability in retrieved sources)
- **OMIM:** **229600** (explicitly stated in multiple 2024 sources). (biancalana2024hereditaryfructoseintolerancea pages 36-38, zuriaga2024descriptiveanalysisof pages 1-2)
- **MONDO / Orphanet / ICD-10/ICD-11 / MeSH:** not explicitly stated in the retrieved full-text snippets; therefore not asserted here.

### 1.3 Synonyms and alternative names
- Hereditary fructose intolerance (HFI)
- Hereditary fructosemia
- Fructosemia (used in clinical case-report context) (ubeda2024clinicalpracticeguidelines pages 1-2, biancalana2024hereditaryfructoseintolerancea pages 36-38, garbowski2024acasestudy pages 5-6)

### 1.4 Evidence sources and aggregation level
The information summarized below is derived from: (i) disease-level resources (clinical practice guideline and systematic reviews), (ii) aggregated cohort/case series summaries, and (iii) individual case reports and mechanistic mouse-model studies. (ubeda2024clinicalpracticeguidelines pages 1-2, maines2024theroleof pages 1-2, garbowski2024acasestudy pages 5-6, andreshernando2024activationofampd2 pages 1-2)

**Structured identifiers & epidemiology summary table:**
| Item | Summary | Publication year/source |
|---|---|---|
| Disease name / synonyms | Hereditary fructose intolerance (HFI); also called hereditary fructosemia or fructosemia (ubeda2024clinicalpracticeguidelines pages 1-2, biancalana2024hereditaryfructoseintolerancea pages 36-38, garbowski2024acasestudy pages 5-6) | 2024 — *Diseases* guideline; 2024 adult-management report; 2024 *Journal of Clinical Medicine* case study |
| OMIM | OMIM: 229600 (biancalana2024hereditaryfructoseintolerancea pages 36-38, zuriaga2024descriptiveanalysisof pages 1-2) | 2024 adult-management report; 2024 *Healthcare* pregnancy study |
| Gene | **ALDOB** (aldolase B; NM_000035.3 reported in adult-management report); located on chromosome 9q22.3/9q22.3 region in reviewed sources (ubeda2024clinicalpracticeguidelines pages 1-2, biancalana2024hereditaryfructoseintolerancea pages 36-38, garbowski2024acasestudy pages 5-6) | 2024 — *Diseases* guideline; 2024 adult-management report; 2024 *Journal of Clinical Medicine* case study |
| Inheritance | Autosomal recessive inborn error of metabolism / metabolic disorder (ubeda2024clinicalpracticeguidelines pages 1-2, biancalana2024hereditaryfructoseintolerancea pages 36-38, zuriaga2024descriptiveanalysisof pages 1-2) | 2024 — *Diseases* guideline; 2024 adult-management report; 2024 *Healthcare* pregnancy study |
| Prevalence | Reported estimates vary: ~1 in 10,000 worldwide; ~1 in 20,000 people; around 1 in 26,000 live births in Europe and 1 in 20,000 births in the US (ubeda2024clinicalpracticeguidelines pages 1-2, biancalana2024hereditaryfructoseintolerancea pages 36-38, maines2024theroleof pages 1-2, zuriaga2024descriptiveanalysisof pages 1-2) | 2024 — *Diseases* guideline; 2024 adult-management report; 2024 *Journal of Diabetes & Metabolic Disorders* systematic review; 2024 *Healthcare* pregnancy study |
| Carrier frequency | Predicted heterozygous carrier frequency ranges from 1:55 to 1:122 in the general population (zuriaga2024descriptiveanalysisof pages 1-2) | 2024 — *Healthcare* pregnancy study |
| Common variants | Frequently reported ALDOB variants include p.Ala150Pro / c.448G>C and p.Ala175Asp / c.524C>A; broader review also lists c.178C>T p.Arg60Ter, c.360_363del p.Asn120LysfsTer32, and c.1005C>G p.Asn335Lys. p.Ala150Pro and p.Ala175Asp together account for ~68% of alleles, with p.Ala150Pro alone ~53% worldwide in one summarized review (ubeda2024clinicalpracticeguidelines pages 1-2, biancalana2024hereditaryfructoseintolerancea pages 36-38, garbowski2024acasestudy pages 5-6) | 2024 — *Diseases* guideline; 2024 adult-management report; 2024 *Journal of Clinical Medicine* case study |
| Key tissues affected | Liver, kidney/renal proximal tubules, and small intestine are key tissues expressing aldolase B and affected in HFI; pregnancy study also notes primary effects in liver and renal tubules (ubeda2024clinicalpracticeguidelines pages 1-2, zuriaga2024descriptiveanalysisof pages 1-2) | 2024 — *Diseases* guideline; 2024 *Healthcare* pregnancy study |


*Table: This table summarizes standardized nomenclature, core genetic facts, inheritance, prevalence, carrier frequency, common ALDOB variants, and major affected tissues for hereditary fructose intolerance. It is restricted to details explicitly supported by the cited 2024 sources requested by the user.*

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** germline **biallelic pathogenic ALDOB variants** causing deficiency of aldolase B activity. (ubeda2024clinicalpracticeguidelines pages 1-2, ubeda2024clinicalpracticeguidelines pages 2-4)

**Immediate biochemical trigger:** ingestion of **fructose** and fructose-generating sugars/sugar alcohols (**sucrose, sorbitol**) leading to F1P accumulation. (ubeda2024clinicalpracticeguidelines pages 2-4, garbowski2024acasestudy pages 9-10)

### 2.2 Risk factors
- **Genetic:** autosomal recessive inheritance; risk increases with parental carrier status. (zuriaga2024descriptiveanalysisof pages 1-2)
- **Environmental/dietary:** exposure to fructose/sucrose/sorbitol (including hidden sources in formulas and medications) triggers acute toxicity and chronic injury. (ubeda2024clinicalpracticeguidelines pages 4-5, ubeda2024clinicalpracticeguidelines pages 2-4)

### 2.3 Protective factors
- **Dietary avoidance** of fructose/sucrose/sorbitol is protective against acute crises and prevents many complications. (ubeda2024clinicalpracticeguidelines pages 4-5, ubeda2024clinicalpracticeguidelines pages 2-4)
- **Experimental genetic protection in models:** aldolase B knockout mice are protected from toxic fructose effects when fructokinase/KHK is absent (mechanistic rationale supporting KHK inhibition strategy). (koene2025safetyandefficacy pages 1-3)

### 2.4 Gene–environment interactions
HFI is a prototypical gene–diet interaction: ALDOB deficiency is necessary but clinical toxicity depends on dietary exposure to fructose-containing compounds; however, newer evidence suggests **endogenous fructose generation** can also drive disease. (andreshernando2024activationofampd2 pages 1-2)

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum (acute and chronic)
Acute manifestations typically appear after introduction of fructose-containing foods (often around weaning) and include **vomiting**, **abdominal pain/distension**, and **postprandial hypoglycemia**, with biochemical abnormalities including **lactic/metabolic acidosis**, **hypophosphatemia**, and **hyperuricemia**. (ubeda2024clinicalpracticeguidelines pages 2-4, ubeda2024clinicalpracticeguidelines pages 5-8, garbowski2024acasestudy pages 9-10)

Chronic manifestations can include **hepatic steatosis (fatty liver)**, persistent **transaminase elevation**, **growth deficiency/failure to thrive**, and **renal proximal tubular dysfunction/Fanconi syndrome** with potential progression to chronic kidney disease. (ubeda2024clinicalpracticeguidelines pages 1-2, garbowski2024acasestudy pages 9-10, ubeda2024clinicalpracticeguidelines pages 5-8)

### 3.2 Age of onset and temporal development
- Typical onset is **~6 months** with the introduction of fructose-containing foods. (ubeda2024clinicalpracticeguidelines pages 2-4)
- Disease course is lifelong; prognosis is generally favorable with dietary treatment, but chronic complications may persist. (ubeda2024clinicalpracticeguidelines pages 1-2, ubeda2024clinicalpracticeguidelines pages 2-4)

### 3.3 Phenotype frequencies / statistics from recent literature
- **Hepatic steatosis persistence:** one long-term cohort summary reported steatosis persisted in **93.8%** of patients on a fructose-restricted diet (<1.5 g/day), and **37.5%** had elevated transaminases despite adherence—supporting ongoing morbidity risk. (garbowski2024acasestudy pages 9-10)
- **Adult cohort symptoms:** in one adult cohort, gastrointestinal symptoms occurred in **9/14** and symptomatic hypoglycemia in **7/14**, with universal lifelong aversion to sweets/fruit. (biancalana2024hereditaryfructoseintolerance pages 38-40, biancalana2024hereditaryfructoseintolerancea pages 38-40)

### 3.4 Quality of life impact
While validated QoL instruments are not reported in the retrieved snippets, chronic food avoidance burden, persistent liver disease (steatosis), and renal tubular complications imply significant long-term management impact and need for multidisciplinary follow-up. (garbowski2024acasestudy pages 9-10, ubeda2024clinicalpracticeguidelines pages 2-4)

### 3.5 Suggested HPO terms (selected)
A phenotype-to-HPO mapping table (restricted to explicitly evidenced features) is provided below.

| Phenotype category | Clinical feature | Trigger/onset | Frequency/statistic (if stated) | Suggested HPO terms | Key sources |
|---|---|---|---|---|---|
| Acute metabolic / gastrointestinal | Postprandial hypoglycemia | Typically after fructose-containing foods are introduced, often around weaning (~6 months); triggered by fructose/sucrose/sorbitol ingestion | Hypoglycemia threshold cited as blood glucose <0.50 g/L (<2.75 mmol/L); neonatal threshold may be ~0.40 g/L | HP:0001943 Hypoglycemia | (ubeda2024clinicalpracticeguidelines pages 2-4, ubeda2024clinicalpracticeguidelines pages 5-8, garbowski2024acasestudy pages 9-10) |
| Acute gastrointestinal | Vomiting / nausea after fructose exposure | After intake of fructose or related sugars; commonly at weaning/after introduction of complementary foods | Not quantified | HP:0002013 Vomiting; HP:0002018 Nausea | (ubeda2024clinicalpracticeguidelines pages 1-2, maines2024theroleof pages 1-2, ubeda2024clinicalpracticeguidelines pages 2-4) |
| Acute gastrointestinal | Abdominal distension / abdominal pain | Postprandial after fructose ingestion; may present in infancy or later with food-triggered symptoms | Not quantified | HP:0003270 Abdominal distension; HP:0002027 Abdominal pain | (ubeda2024clinicalpracticeguidelines pages 1-2, ubeda2024clinicalpracticeguidelines pages 2-4) |
| Acute metabolic | Lactic/metabolic acidosis | Consequence of fructose-1-phosphate accumulation with impaired gluconeogenesis/glycogenolysis after fructose exposure | Not quantified | HP:0001942 Metabolic acidosis; HP:0002151 Increased lactate level | (ubeda2024clinicalpracticeguidelines pages 2-4, biancalana2024hereditaryfructoseintolerancea pages 36-38, garbowski2024acasestudy pages 9-10) |
| Acute biochemical | Hypophosphatemia / phosphate depletion | After fructose ingestion due to intracellular phosphate trapping and ongoing phosphorylation of fructose | Not quantified | HP:0002148 Hypophosphatemia | (ubeda2024clinicalpracticeguidelines pages 2-4, biancalana2024hereditaryfructoseintolerancea pages 36-38, garbowski2024acasestudy pages 9-10, koene2025safetyandefficacy pages 1-3) |
| Acute biochemical | Hyperuricemia | Secondary to ATP depletion and increased AMP degradation after fructose exposure | Not quantified | HP:0003251 Hyperuricemia | (ubeda2024clinicalpracticeguidelines pages 2-4, garbowski2024acasestudy pages 9-10) |
| Renal acute/chronic | Proximal renal tubular dysfunction / Fanconi-type syndrome / renal tubular acidosis | May accompany ongoing fructose exposure; due to aldolase B deficiency in proximal tubules | Tubular bicarbonate reabsorption reduction 15–30% reported | HP:0000114 Renal tubular dysfunction; HP:0001992 Fanconi syndrome; HP:0001941 Renal tubular acidosis | (ubeda2024clinicalpracticeguidelines pages 2-4, ubeda2024clinicalpracticeguidelines pages 5-8) |
| Hepatic acute/chronic | Hepatomegaly / liver dysfunction | Often recognized after introduction of fructose-containing foods; may persist chronically | Not quantified | HP:0002240 Hepatomegaly; HP:0002910 Elevated hepatic transaminases | (ubeda2024clinicalpracticeguidelines pages 1-2, garbowski2024acasestudy pages 9-10, garbowski2024acasestudy pages 7-9) |
| Hepatic chronic | Hepatic steatosis / fatty liver | Chronic complication despite treatment in some patients; can persist on fructose-restricted diets | Hepatic steatosis persisted in 93.8% in one long-term cohort on fructose-restricted diet | HP:0001397 Hepatic steatosis | (ubeda2024clinicalpracticeguidelines pages 1-2, garbowski2024acasestudy pages 9-10, ubeda2024clinicalpracticeguidelines pages 2-4) |
| Hepatic chronic | Elevated transaminases | Chronic residual liver dysfunction despite diet in some patients | Elevated transaminases in 37.5% in one long-term cohort | HP:0002910 Elevated hepatic transaminases | (garbowski2024acasestudy pages 9-10) |
| Growth/nutrition | Failure to thrive / growth retardation | Chronic ingestion after weaning in untreated or incompletely controlled disease | Not quantified | HP:0001508 Failure to thrive; HP:0001510 Growth delay | (maines2024theroleof pages 1-2, ubeda2024clinicalpracticeguidelines pages 1-2, ubeda2024clinicalpracticeguidelines pages 5-8) |
| Behavioral/feeding | Aversion to sweets / fructose-containing foods | Often longstanding from infancy/childhood; key historical clue for diagnosis | In adult cohort, all patients had lifelong aversion to sweet foods/fruit | HP:0033813 Food aversion | (biancalana2024hereditaryfructoseintolerance pages 36-38, biancalana2024hereditaryfructoseintolerance pages 38-40, garbowski2024acasestudy pages 9-10) |
| Chronic multisystem | Kidney damage / chronic kidney disease | Longer-term complication with continued exposure or incomplete control | Not quantified | HP:0000083 Renal insufficiency; HP:0012622 Chronic kidney disease | (andreshernando2024activationofampd2 pages 1-2, maines2024theroleof pages 1-2, garbowski2024acasestudy pages 9-10) |
| Severe acute / neurologic | Seizures, coma, life-threatening decompensation | Severe untreated exposure with profound hypoglycemia/metabolic derangement | Not quantified | HP:0001250 Seizure; HP:0001259 Coma | (biancalana2024hereditaryfructoseintolerancea pages 36-38, andreshernando2024activationofampd2 pages 1-2) |
| Chronic gastrointestinal | Irritable bowel syndrome–like symptoms / chronic abdominal complaints | Reported as chronic complication despite treatment in some patients | Not quantified | HP:0002027 Abdominal pain; HP:0002014 Diarrhea; HP:0012531 Chronic gastrointestinal discomfort | (ubeda2024clinicalpracticeguidelines pages 1-2, ubeda2024clinicalpracticeguidelines pages 11-12) |
| Biomarker / glycosylation | Abnormal carbohydrate-deficient transferrin (CDT) / abnormal sialotransferrin isoforms | Untreated patients; proposed for monitoring dietary fructose/sucrose/sorbitol exposure and individual tolerance | Not quantified in excerpt; described as abnormal Tf glycosylation suggestive of N-hypoglycosylation | HP:0012125 Abnormal transferrin glycosylation | (maines2024theroleof pages 1-2, ubeda2024clinicalpracticeguidelines pages 4-5, garbowski2024acasestudy pages 9-10) |
| Pregnancy-associated observations | Lower infant birth weight in affected mothers; persistent maternal hepatic steatosis/adenomas/hemangiomas after pregnancy | In women with HFI during/after pregnancy | Babies of affected mothers had lower weights than babies of carrier mothers; cohort included 30 women and 45 pregnancies | HP:0001518 Small for gestational age; HP:0001402 Hepatic fibrosis/structural liver abnormality (approximate liver phenotype mapping) | (zuriaga2024descriptiveanalysisof pages 1-2, zuriaga2024descriptiveanalysisof pages 5-7) |
| Emerging complication spectrum / mechanistic model | NASH, cirrhosis, liver inflammation/fibrosis in model systems and reported chronic human complication spectrum | Chronic disease/continued metabolic stress; mechanistic evidence from aldob-deficient mice | Not quantified in excerpt | HP:0001394 Cirrhosis; HP:0012844 Liver fibrosis; HP:0001399 Hepatic failure | (andreshernando2024activationofampd2 pages 1-2) |


*Table: This table summarizes the major acute and chronic phenotypes of hereditary fructose intolerance, their typical triggers or age of onset, key laboratory/biomarker findings, and suggested HPO mappings. It is restricted to points explicitly supported in the cited 2024-focused evidence base and includes quantitative findings where reported.*

---

## 4. Genetic / molecular information

### 4.1 Causal gene
- **Gene:** **ALDOB** (aldolase B), located on **chromosome 9q22.3** in retrieved sources. (ubeda2024clinicalpracticeguidelines pages 1-2, garbowski2024acasestudy pages 5-6)

### 4.2 Pathogenic variants (examples supported by evidence)
A systematic review summarized in a 2024 case report analyzed **1,426 alleles** across **29 countries** and identified **68 distinct ALDOB variants** in **85 genotypic combinations**. Widely distributed pathogenic variants include:
- c.178C>T p.(Arg60Ter)
- c.360_363del p.(Asn120LysfsTer32)
- c.448G>C p.(Ala150Pro)
- c.524C>A p.(Ala175Asp)
- c.1005C>G p.(Asn335Lys)
It further reported that **p.(Ala150Pro) and p.(Ala175Asp) together account for ~68% of alleles**, with **p.(Ala150Pro) alone ~53% worldwide**. (garbowski2024acasestudy pages 5-6)

In a 2024 adult cohort, the most frequent variants were again **p.Ala150Pro** and **p.Ala175Asp**, with additional variants including splice variants, duplications, and large deletions. (biancalana2024hereditaryfructoseintolerance pages 38-40, biancalana2024hereditaryfructoseintolerancea pages 38-40)

### 4.3 Functional consequence
ALDOB deficiency results in inability to cleave F1P, driving accumulation of F1P and secondary metabolic toxicity (phosphate/ATP depletion and impaired gluconeogenesis/glycogenolysis). (ubeda2024clinicalpracticeguidelines pages 2-4, biancalana2024hereditaryfructoseintolerancea pages 36-38)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No modifier genes, epigenetic signatures, or recurrent chromosomal abnormalities were explicitly supported in the retrieved evidence snippets; these remain a knowledge gap in the current evidence set.

---

## 5. Environmental information

### 5.1 Environmental/lifestyle contributors
For HFI, the key non-genetic contributor is **dietary exposure** to fructose-containing ingredients and sugar alcohols.
- Hidden fructose/sorbitol sources in **infant formulas and OTC medicines** are specifically flagged as under-recognized exposure risks in guidelines. (ubeda2024clinicalpracticeguidelines pages 4-5)

### 5.2 Infectious agents
Not applicable; HFI is not infectious.

---

## 6. Mechanism / pathophysiology

### 6.1 Canonical biochemical mechanism (current consensus)
Dietary fructose is phosphorylated by **fructokinase (KHK)** to **fructose-1-phosphate (F1P)**. In normal physiology, aldolase B cleaves F1P; in HFI, aldolase B deficiency causes **F1P accumulation**, which:
- traps inorganic phosphate (Pi) and depletes ATP,
- inhibits glycogenolysis and gluconeogenesis,
- triggers hypoglycemia and metabolic derangements, and
- contributes to liver and kidney toxicity, including proximal tubular dysfunction. (ubeda2024clinicalpracticeguidelines pages 2-4, biancalana2024hereditaryfructoseintolerancea pages 36-38, garbowski2024acasestudy pages 9-10)

### 6.2 Recent mechanistic developments (2023–2024)
**(i) Endogenous fructose hypothesis:** A 2024 mechanistic study emphasizes that even with dietary restriction, symptoms may persist because **fructose can be produced endogenously from glucose** (polyol pathway), which can then feed into the toxic pathway in aldolase B deficiency. (andreshernando2024activationofampd2 pages 1-2)

**(ii) AMPD2/purine degradation axis:** A 2024 Communications Biology study identified **AMPD2 activation** and downstream **purine degradation** as a critical pathway activated by very low fructose exposure “via a phosphate trap,” contributing to metabolic dysregulation and liver disease. Hepatocyte-specific AMPD2 deletion improved hepatic fat/glycogen storage and reduced inflammation/fibrosis in aldob-deficient mice, without preventing F1P accumulation or hypoglycemia risk. (andreshernando2024activationofampd2 pages 1-2)

**Key mechanistic figure (AMPD2 pathway):** The figure below schematizes the phosphate-trap mechanism and the AMPD2-driven purine degradation pathway in aldolase B deficiency.
(andreshernando2024activationofampd2 media 8a89ee1b)

### 6.3 Pathway and ontology suggestions
- **GO (biological process) candidate terms (suggested based on mechanism described in sources):** fructose metabolic process; gluconeogenesis; glycogen catabolic process; purine nucleotide catabolic process; regulation of cellular phosphate ion homeostasis. (ubeda2024clinicalpracticeguidelines pages 2-4, andreshernando2024activationofampd2 pages 1-2)
- **Cell types (Cell Ontology, suggested):** hepatocyte; enterocyte; renal proximal tubule epithelial cell. (koene2025safetyandefficacy pages 1-3)

---

## 7. Anatomical structures affected

### 7.1 Organ/tissue involvement
Key affected tissues are those expressing mutant aldolase B:
- **Liver** (hepatocyte injury; steatosis; possible progression to NASH/cirrhosis)
- **Small intestine** (enterocytes)
- **Kidney** (proximal tubules; Fanconi-type dysfunction) (koene2025safetyandefficacy pages 1-3, ubeda2024clinicalpracticeguidelines pages 5-8)

**Suggested UBERON terms (examples):** liver; kidney; renal proximal tubule; small intestine. (koene2025safetyandefficacy pages 1-3)

---

## 8. Temporal development

- **Onset:** typically after **weaning (~6 months)** when fructose-containing foods are introduced; can be missed and diagnosed in adulthood due to dietary self-restriction and nonspecific chronic liver findings. (ubeda2024clinicalpracticeguidelines pages 2-4, biancalana2024hereditaryfructoseintolerance pages 38-40)
- **Course:** can be episodic (triggered by accidental ingestion) and/or chronic (fatty liver, renal tubular dysfunction). Prognosis is generally favorable with strict diet, but chronic pathology can persist. (ubeda2024clinicalpracticeguidelines pages 1-2, garbowski2024acasestudy pages 9-10)

---

## 9. Inheritance and population

### 9.1 Inheritance
- **Autosomal recessive.** (ubeda2024clinicalpracticeguidelines pages 1-2, zuriaga2024descriptiveanalysisof pages 1-2)

### 9.2 Epidemiology (recent summaries)
Prevalence estimates vary by source:
- ~**1/10,000** worldwide (adult-management report). (biancalana2024hereditaryfructoseintolerancea pages 36-38)
- ~**1/20,000** and also ~**1/10,000** reported in a 2024 guideline. (ubeda2024clinicalpracticeguidelines pages 1-2)
- ~**1/26,000 live births in Europe** and **1/20,000 births in the US** reported in a 2024 systematic review. (maines2024theroleof pages 1-2)

### 9.3 Carrier frequency
A 2024 pregnancy-focused cohort paper reports predicted heterozygous carrier frequency ranging from **1:55 to 1:122**. (zuriaga2024descriptiveanalysisof pages 1-2)

### 9.4 Population/variant distribution
Common variants p.Ala150Pro and p.Ala175Asp are described as globally distributed with regional patterns in Europe, and a summarized allele study indicates these variants dominate worldwide allele counts. (ubeda2024clinicalpracticeguidelines pages 1-2, garbowski2024acasestudy pages 5-6)

---

## 10. Diagnostics

### 10.1 Clinical suspicion
Key historical clue: lifelong or early childhood **aversion to sweets and fruit**, with symptom onset after fructose exposure; chronic presentations may be unexplained hepatomegaly, elevated aminotransferases, or fatty liver. (biancalana2024hereditaryfructoseintolerancea pages 36-38, garbowski2024acasestudy pages 7-9)

### 10.2 Laboratory abnormalities (supportive)
Supportive findings include:
- hypoglycemia (threshold <0.50 g/L),
- lactic/metabolic acidosis,
- hypophosphatemia,
- hyperuricemia,
- transaminase elevations,
- Fanconi-type proximal tubular dysfunction (e.g., phosphaturia, aminoaciduria, bicarbonate wasting). (ubeda2024clinicalpracticeguidelines pages 5-8, garbowski2024acasestudy pages 9-10, biancalana2024hereditaryfructoseintolerancea pages 36-38)

### 10.3 Genetic testing strategy (recommended)
Clinical guidelines favor **molecular diagnosis**: ALDOB testing (PCR/sequencing on leukocyte DNA) to detect **biallelic pathogenic variants** as the preferred confirmatory test. (ubeda2024clinicalpracticeguidelines pages 2-4)

### 10.4 Historical/confirmatory tests and safety
- **Liver biopsy with aldolase B activity** is historically definitive but invasive; reserved for inconclusive genetic results or uncertain variants. (ubeda2024clinicalpracticeguidelines pages 2-4)
- **Fructose loading/tolerance testing** is now rarely used / discouraged due to risk of severe reactions. (ubeda2024clinicalpracticeguidelines pages 2-4, souza2024intolerânciahereditáriaà pages 4-5)

### 10.5 Adjunct / monitoring biomarkers
- **Urinary fructose by thin-layer chromatography (TLC)** can be used to monitor adherence. (biancalana2024hereditaryfructoseintolerancea pages 36-38)
- **Carbohydrate-deficient transferrin (CDT) / sialotransferrin isoforms**: untreated patients show abnormal transferrin glycosylation (N-hypoglycosylation pattern). Methods include **Tf isoelectric focusing** and **high-resolution MS**; CDT metrics may correlate with fructose intake and support monitoring/personalized tolerability targets. (maines2024theroleof pages 1-2, ubeda2024clinicalpracticeguidelines pages 4-5)

### 10.6 Screening
- **Newborn screening:** generally **not performed** because there is no reliable biomarker in dried blood spots without fructose exposure; normal newborn screens may occur in affected infants. (ubeda2024clinicalpracticeguidelines pages 2-4, garbowski2024acasestudy pages 9-10)
- **Cascade screening:** recommended after proband identification; prenatal and preimplantation genetic testing are advised as options. (souza2024intolerânciahereditáriaà pages 4-5)

---

## 11. Outcome / prognosis

### 11.1 Prognosis with treatment
Guidelines describe **favorable prognosis** with strict diet adherence, including normalization of weight and laboratory abnormalities in many patients; however, chronic complications (notably fatty liver) can persist. (ubeda2024clinicalpracticeguidelines pages 1-2, ubeda2024clinicalpracticeguidelines pages 2-4)

### 11.2 Morbidity (persistent complications)
Long-term cohort summaries indicate persistent **hepatic steatosis** (93.8%) and continued **transaminase elevation** (37.5%) despite stringent dietary restriction (<1.5 g/day), suggesting ongoing liver morbidity risk. (garbowski2024acasestudy pages 9-10)

### 11.3 Pregnancy outcomes
In a 2024 cohort of Spanish women (30 women; 45 pregnancies), affected mothers had lower infant birth weights compared with carrier mothers and persistent hepatic issues (steatosis/adenomas/hemangiomas) were noted after pregnancy, supporting need for monitoring. (zuriaga2024descriptiveanalysisof pages 1-2)

---

## 12. Treatment

### 12.1 Standard of care (real-world implementation)
**Dietary treatment** is the only established effective therapy in current clinical guidance:
- Lifelong **FSS-free** diet (avoid fructose, sucrose, sorbitol); glucose/maltose/starch are suitable substitutes. (ubeda2024clinicalpracticeguidelines pages 4-5, ubeda2024clinicalpracticeguidelines pages 2-4)
- Avoid medications/products containing fructose or sorbitol excipients; hidden sources in infant formulas and OTC baby medicines are specifically highlighted. (ubeda2024clinicalpracticeguidelines pages 4-5)

**Quantitative diet thresholds reported:**
- Restrict total fructose to **<40 mg/kg/day** (reported in pregnancy cohort context). (zuriaga2024descriptiveanalysisof pages 1-2)
- Advice not to exceed **2 g/day fructose** (adult cohort recommendation) and some adults may tolerate **<6 g/day** (guideline). (biancalana2024hereditaryfructoseintolerancea pages 38-40, ubeda2024clinicalpracticeguidelines pages 2-4)

### 12.2 Acute decompensation management
After accidental ingestion and acute metabolic crisis, recommended management includes hospitalization (ICU if severe) with **intravenous glucose (dextrose)**, treatment of metabolic acidosis if present, and supportive care. (garbowski2024acasestudy pages 6-7)

### 12.3 Monitoring and supportive care
- Periodic follow-up from childhood to adulthood is recommended; chronic liver fat can persist and warrants surveillance. (ubeda2024clinicalpracticeguidelines pages 11-12)
- Vitamin deficiency risk (e.g., vitamin C) is noted and supplementation may be needed. (ubeda2024clinicalpracticeguidelines pages 2-4)

### 12.4 Experimental / advanced therapeutics
**KHK inhibition** (pharmacologic fructokinase inhibition) aims to block fructose phosphorylation and prevent F1P formation.
- A clinical trial record describes an open-label pilot in HFI using **PF‑06835919** (300 mg daily × 9 days), with endpoints assessing intestinal symptoms, serum glucose/phosphate, urine markers, liver fat by 1H‑MRS, and glycosylated transferrin (ClinicalTrials.gov **NCT06089265**, registry year 2023). (NCT06089265 chunk 1)
- A clinical study report (JCI, Feb 2025; doi:10.1172/jci187376) describes graded fructose challenges in 3 HFI patients after PF‑06835919, with reported short-term tolerability and absence of proximal tubular dysfunction during challenges. (koene2025safetyandefficacy pages 1-3)

**Mechanism-guided targets (preclinical):** AMPD2/purine degradation axis and phosphate homeostasis interventions are proposed based on mouse-model work. (andreshernando2024activationofampd2 pages 5-7, andreshernando2024activationofampd2 pages 1-2)

### 12.5 MAXO term suggestions (examples)
- Dietary fructose restriction / dietary sucrose restriction / dietary sorbitol restriction (FSS-free diet)
- Intravenous dextrose administration (acute crisis)
- Genetic counseling / carrier testing / prenatal genetic testing

*(MAXO identifiers are not provided in the retrieved sources; the above are term suggestions for ontology mapping.)*

### 12.6 CHEBI term suggestions (examples)
- Fructose; sucrose; sorbitol; glucose; uric acid; fructose-1-phosphate

---

## 13. Prevention

Primary prevention is largely genetic/dietary:
- **Avoidance of fructose/sucrose/sorbitol exposure** in diagnosed individuals, including careful checking of drug excipients and infant formula composition. (ubeda2024clinicalpracticeguidelines pages 4-5)
- **Genetic counseling** and cascade carrier testing for families after identification of an affected proband; prenatal and preimplantation genetic testing are suggested options. (souza2024intolerânciahereditáriaà pages 4-5)

Secondary prevention:
- Early diagnosis through recognition of weaning-associated symptoms and immediate withdrawal of fructose/sucrose with rapid improvement (2–3 days) supports early case finding. (ubeda2024clinicalpracticeguidelines pages 2-4)

Tertiary prevention:
- Long-term monitoring for liver steatosis and renal tubular complications even with dietary adherence. (garbowski2024acasestudy pages 9-10, ubeda2024clinicalpracticeguidelines pages 5-8)

---

## 14. Other species / natural disease
No naturally occurring non-human HFI cases were identified in the retrieved evidence set.

---

## 15. Model organisms
Mechanistic studies in **aldolase B–deficient (aldob−/−) mice** recapitulate key features of HFI and are used to investigate drivers of liver disease and metabolic dysregulation.
- A 2024 study shows very low fructose activates AMPD2 via phosphate trapping, and hepatocyte-specific AMPD2 deletion reduces liver pathology in aldolase B deficiency. (andreshernando2024activationofampd2 pages 1-2)

**Model utility:** mechanistic dissection of hepatic fat/glycogen dysregulation and identification of drug targets (AMPD2 axis; phosphate homeostasis; fructose metabolism inhibition). (andreshernando2024activationofampd2 pages 1-2)

---

## Direct abstract quotes supporting key claims (from retrieved abstracts)

- **AMPD2 mechanism (2024):** “Very low amounts of fructose are sufficient to activate AMPD2 in these mice via a phosphate trap.” (Communications Biology, Jul 2024; doi:10.1038/s42003-024-06539-1) (andreshernando2024activationofampd2 pages 1-2)
- **Sialotransferrin/CDT review (2024):** “Subjects with HFI usually present at the time of weaning with episodes of hypoglycaemia and vomiting after the intake of fructose or related sugars,” and management is “fructose-, sucrose-, and sorbitol (FSS)-restrictive life-long diet.” (J Diabetes Metab Disord, online 2024-12-27; doi:10.1007/s40200-024-01527-y) (maines2024theroleof pages 1-2)
- **Guideline definition (2024):** HFI is “an autosomal recessive metabolic disorder caused by a loss of function in the aldolase B gene.” (Diseases, published 2024-02-23; doi:10.3390/diseases12030044) (ubeda2024clinicalpracticeguidelines pages 1-2)

---

## Notes on evidence gaps vs. requested template
- **MONDO, Orphanet, ICD, and MeSH identifiers** were not present in the retrieved text chunks; these should be pulled from dedicated ontologies/databases (e.g., MONDO/Orphanet/MeSH/ICD) in a subsequent retrieval pass.
- **PMIDs:** Several 2024 MDPI articles and the adult-management report excerpts did not include PMIDs in the retrieved text snippets; DOIs/URLs and publication dates are provided where available.
- **Multi-omics (transcriptomics/proteomics/metabolomics) in humans:** not covered in the retrieved excerpts.

---

## Key recent sources (URLs and dates)
- Úbeda F, et al. *Diseases* (published 2024-02-23). “Clinical Practice Guidelines for the Diagnosis and Management of Hereditary Fructose Intolerance.” https://doi.org/10.3390/diseases12030044 (ubeda2024clinicalpracticeguidelines pages 1-2)
- Andres-Hernando A, et al. *Communications Biology* (Jul 2024). “Activation of AMPD2 drives metabolic dysregulation and liver disease in mice with hereditary fructose intolerance.” https://doi.org/10.1038/s42003-024-06539-1 (andreshernando2024activationofampd2 pages 1-2)
- Maines E, et al. *J Diabetes Metab Disord* (online 2024-12-27). “The role of the analysis of sialotransferrin isoforms in the management of hereditary fructose intolerance: a systematic review.” https://doi.org/10.1007/s40200-024-01527-y (maines2024theroleof pages 1-2)
- Garbowski L, et al. *J Clin Med* (published 2024-06-10). “A Case Study of a Rare Disease (Fructosemia) Diagnosed in a Patient with Abdominal Pain.” https://doi.org/10.3390/jcm13123394 (garbowski2024acasestudy pages 1-2)
- Zuriaga E, et al. *Healthcare* (Feb 2024). “Descriptive Analysis of Carrier and Affected Hereditary Fructose Intolerance in Women during Pregnancy.” https://doi.org/10.3390/healthcare12050573 (zuriaga2024descriptiveanalysisof pages 1-2)
- ClinicalTrials.gov (registry record 2023). “Ketohexokinase Inhibition in Hereditary Fructose Intolerance.” NCT06089265. https://clinicaltrials.gov/study/NCT06089265 (NCT06089265 chunk 1)


References

1. (andreshernando2024activationofampd2 pages 1-2): Ana Andres-Hernando, David J. Orlicky, Masanari Kuwabara, Mehdi A. Fini, Dean R. Tolan, Richard J. Johnson, and Miguel A. Lanaspa. Activation of ampd2 drives metabolic dysregulation and liver disease in mice with hereditary fructose intolerance. Communications Biology, Jul 2024. URL: https://doi.org/10.1038/s42003-024-06539-1, doi:10.1038/s42003-024-06539-1. This article has 2 citations and is from a peer-reviewed journal.

2. (ubeda2024clinicalpracticeguidelines pages 1-2): Félix Úbeda, Sonia Santander, and María José Luesma. Clinical practice guidelines for the diagnosis and management of hereditary fructose intolerance. Diseases, 12:44, Feb 2024. URL: https://doi.org/10.3390/diseases12030044, doi:10.3390/diseases12030044. This article has 11 citations.

3. (ubeda2024clinicalpracticeguidelines pages 2-4): Félix Úbeda, Sonia Santander, and María José Luesma. Clinical practice guidelines for the diagnosis and management of hereditary fructose intolerance. Diseases, 12:44, Feb 2024. URL: https://doi.org/10.3390/diseases12030044, doi:10.3390/diseases12030044. This article has 11 citations.

4. (garbowski2024acasestudy pages 9-10): Leszek Garbowski, Marzena Walasek, Rafał Firszt, Ewelina Chilińska-Kopko, Paulina Błażejewska-Gała, Daniel Popielnicki, and Zofia Dzięcioł-Anikiej. A case study of a rare disease (fructosemia) diagnosed in a patient with abdominal pain. Journal of Clinical Medicine, 13:3394, Jun 2024. URL: https://doi.org/10.3390/jcm13123394, doi:10.3390/jcm13123394. This article has 3 citations.

5. (ubeda2024clinicalpracticeguidelines pages 4-5): Félix Úbeda, Sonia Santander, and María José Luesma. Clinical practice guidelines for the diagnosis and management of hereditary fructose intolerance. Diseases, 12:44, Feb 2024. URL: https://doi.org/10.3390/diseases12030044, doi:10.3390/diseases12030044. This article has 11 citations.

6. (NCT06089265 chunk 1):  Ketohexokinase Inhibition in Hereditary Fructose Intolerance. Maastricht University Medical Center. 2023. ClinicalTrials.gov Identifier: NCT06089265

7. (biancalana2024hereditaryfructoseintolerancea pages 36-38): E BIANCALANA and C PISTOLESI. Hereditary fructose intolerance in adults: from differential diagnosis to long-term management. a report from the …. Unknown journal, 2024.

8. (garbowski2024acasestudy pages 5-6): Leszek Garbowski, Marzena Walasek, Rafał Firszt, Ewelina Chilińska-Kopko, Paulina Błażejewska-Gała, Daniel Popielnicki, and Zofia Dzięcioł-Anikiej. A case study of a rare disease (fructosemia) diagnosed in a patient with abdominal pain. Journal of Clinical Medicine, 13:3394, Jun 2024. URL: https://doi.org/10.3390/jcm13123394, doi:10.3390/jcm13123394. This article has 3 citations.

9. (zuriaga2024descriptiveanalysisof pages 1-2): Estefanía Zuriaga, Sonia Santander, Laura Lomba, Elsa Izquierdo-García, and María José Luesma. Descriptive analysis of carrier and affected hereditary fructose intolerance in women during pregnancy. Healthcare, 12:573, Feb 2024. URL: https://doi.org/10.3390/healthcare12050573, doi:10.3390/healthcare12050573. This article has 1 citations.

10. (maines2024theroleof pages 1-2): Evelina Maines, Giorgia Gugelmo, Arianna Maiorana, Diego Martinelli, Nicola Vitturi, Livia Lenzini, Giovanni Piccoli, Massimo Soffiati, and Roberto Franceschi. The role of the analysis of sialotransferrin isoforms in the management of hereditary fructose intolerance: a systematic review. Journal of diabetes and metabolic disorders, 24 1:27, Dec 2024. URL: https://doi.org/10.1007/s40200-024-01527-y, doi:10.1007/s40200-024-01527-y. This article has 0 citations and is from a peer-reviewed journal.

11. (koene2025safetyandefficacy pages 1-3): Evi J.C. Koene, Amée M. Buziau, David Cassiman, Timothy M. Cox, Judith Bons, Jean L. J. M. Scheijen, Casper G. Schalkwijk, Steven J.R. Meex, Aditi R. Saxena, William P. Esler, Vera B. Schrauwen-Hinderling, Patrick Schrauwen, and Martijn C.G.J. Brouwers. Safety and efficacy of pharmacological inhibition of ketohexokinase in hereditary fructose intolerance. The Journal of Clinical Investigation, Feb 2025. URL: https://doi.org/10.1172/jci187376, doi:10.1172/jci187376. This article has 7 citations.

12. (ubeda2024clinicalpracticeguidelines pages 5-8): Félix Úbeda, Sonia Santander, and María José Luesma. Clinical practice guidelines for the diagnosis and management of hereditary fructose intolerance. Diseases, 12:44, Feb 2024. URL: https://doi.org/10.3390/diseases12030044, doi:10.3390/diseases12030044. This article has 11 citations.

13. (biancalana2024hereditaryfructoseintolerance pages 38-40): E BIANCALANA and C PISTOLESI. Hereditary fructose intolerance in adults: from differential diagnosis to long-term management. a report from the …. Unknown journal, 2024.

14. (biancalana2024hereditaryfructoseintolerancea pages 38-40): E BIANCALANA and C PISTOLESI. Hereditary fructose intolerance in adults: from differential diagnosis to long-term management. a report from the …. Unknown journal, 2024.

15. (garbowski2024acasestudy pages 7-9): Leszek Garbowski, Marzena Walasek, Rafał Firszt, Ewelina Chilińska-Kopko, Paulina Błażejewska-Gała, Daniel Popielnicki, and Zofia Dzięcioł-Anikiej. A case study of a rare disease (fructosemia) diagnosed in a patient with abdominal pain. Journal of Clinical Medicine, 13:3394, Jun 2024. URL: https://doi.org/10.3390/jcm13123394, doi:10.3390/jcm13123394. This article has 3 citations.

16. (biancalana2024hereditaryfructoseintolerance pages 36-38): E BIANCALANA and C PISTOLESI. Hereditary fructose intolerance in adults: from differential diagnosis to long-term management. a report from the …. Unknown journal, 2024.

17. (ubeda2024clinicalpracticeguidelines pages 11-12): Félix Úbeda, Sonia Santander, and María José Luesma. Clinical practice guidelines for the diagnosis and management of hereditary fructose intolerance. Diseases, 12:44, Feb 2024. URL: https://doi.org/10.3390/diseases12030044, doi:10.3390/diseases12030044. This article has 11 citations.

18. (zuriaga2024descriptiveanalysisof pages 5-7): Estefanía Zuriaga, Sonia Santander, Laura Lomba, Elsa Izquierdo-García, and María José Luesma. Descriptive analysis of carrier and affected hereditary fructose intolerance in women during pregnancy. Healthcare, 12:573, Feb 2024. URL: https://doi.org/10.3390/healthcare12050573, doi:10.3390/healthcare12050573. This article has 1 citations.

19. (andreshernando2024activationofampd2 media 8a89ee1b): Ana Andres-Hernando, David J. Orlicky, Masanari Kuwabara, Mehdi A. Fini, Dean R. Tolan, Richard J. Johnson, and Miguel A. Lanaspa. Activation of ampd2 drives metabolic dysregulation and liver disease in mice with hereditary fructose intolerance. Communications Biology, Jul 2024. URL: https://doi.org/10.1038/s42003-024-06539-1, doi:10.1038/s42003-024-06539-1. This article has 2 citations and is from a peer-reviewed journal.

20. (souza2024intolerânciahereditáriaà pages 4-5): RF de Souza, RP Erdmann, and NB Ferreira. Intolerância hereditária à frutose: etiologia e principais características clínicas. Unknown journal, 2024.

21. (garbowski2024acasestudy pages 6-7): Leszek Garbowski, Marzena Walasek, Rafał Firszt, Ewelina Chilińska-Kopko, Paulina Błażejewska-Gała, Daniel Popielnicki, and Zofia Dzięcioł-Anikiej. A case study of a rare disease (fructosemia) diagnosed in a patient with abdominal pain. Journal of Clinical Medicine, 13:3394, Jun 2024. URL: https://doi.org/10.3390/jcm13123394, doi:10.3390/jcm13123394. This article has 3 citations.

22. (andreshernando2024activationofampd2 pages 5-7): Ana Andres-Hernando, David J. Orlicky, Masanari Kuwabara, Mehdi A. Fini, Dean R. Tolan, Richard J. Johnson, and Miguel A. Lanaspa. Activation of ampd2 drives metabolic dysregulation and liver disease in mice with hereditary fructose intolerance. Communications Biology, Jul 2024. URL: https://doi.org/10.1038/s42003-024-06539-1, doi:10.1038/s42003-024-06539-1. This article has 2 citations and is from a peer-reviewed journal.

23. (garbowski2024acasestudy pages 1-2): Leszek Garbowski, Marzena Walasek, Rafał Firszt, Ewelina Chilińska-Kopko, Paulina Błażejewska-Gała, Daniel Popielnicki, and Zofia Dzięcioł-Anikiej. A case study of a rare disease (fructosemia) diagnosed in a patient with abdominal pain. Journal of Clinical Medicine, 13:3394, Jun 2024. URL: https://doi.org/10.3390/jcm13123394, doi:10.3390/jcm13123394. This article has 3 citations.
