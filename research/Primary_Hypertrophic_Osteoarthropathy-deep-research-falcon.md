---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-22T22:20:36.084580'
end_time: '2026-04-22T22:29:27.397850'
duration_seconds: 531.31
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Primary Hypertrophic Osteoarthropathy
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Primary Hypertrophic Osteoarthropathy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Primary Hypertrophic Osteoarthropathy** covering all of the
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
- **Disease Name:** Primary Hypertrophic Osteoarthropathy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Primary Hypertrophic Osteoarthropathy** covering all of the
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


# Primary Hypertrophic Osteoarthropathy (PHO) / Pachydermoperiostosis (PDP): Comprehensive Research Report

## Executive summary
Primary hypertrophic osteoarthropathy (PHO), also known as pachydermoperiostosis (PDP) or Touraine–Solente–Golé syndrome, is a rare inherited disorder with a characteristic triad of digital clubbing, pachydermia, and periostosis, driven by impaired prostaglandin E2 (PGE2) clearance due to pathogenic variants in **HPGD** and/or **SLCO2A1**. The most actionable current therapeutic axis is suppression of prostaglandin synthesis (notably COX-2 inhibition), with evidence of improvement in soft-tissue/joint manifestations and biochemical markers but limited effect on established periostosis. (lu2023primaryhypertrophicosteoarthropathy pages 1-2, li2025twocasesof pages 1-2, lu2023primaryhypertrophicosteoarthropathy pages 7-8)

| Domain | Summary |
|---|---|
| Disease names / synonyms | **Primary hypertrophic osteoarthropathy (PHO)**; also **pachydermoperiostosis (PDP)** and **Touraine–Solente–Golé syndrome**. Clinical forms: **complete**, **incomplete**, and **forme fruste/fruste** (lu2023primaryhypertrophicosteoarthropathy pages 1-2, nicolau2023tourainesolentegolesyndromepathogenic pages 1-2, joshi2019pachydermoperiostosis(touraine–solente–golesyndrome) pages 1-2, cai2025distinctfeaturesof pages 1-2) |
| Key identifiers | Genetic subtypes: **PHOAR1 MIM 259100**, **PHOAR2 MIM 614441**, **PHOAD MIM 167100**. Causal gene IDs: **HPGD MIM 601688**, **SLCO2A1 MIM 601460**. MeSH from ClinicalTrials.gov: **Osteoarthropathy, Primary Hypertrophic (D010004)** (lu2023primaryhypertrophicosteoarthropathy pages 1-2, xu2021monoallelicmutationsin pages 1-2, NCT02438709 chunk 1) |
| Causal genes & inheritance | **HPGD** loss-of-function causes **PHOAR1**, classically **autosomal recessive**; **SLCO2A1** biallelic variants cause **PHOAR2** (**autosomal recessive**), and **monoallelic SLCO2A1** variants can cause **PHOAD** (**autosomal dominant**) with generally milder phenotype and incomplete/sex-skewed penetrance (lu2023primaryhypertrophicosteoarthropathy pages 1-2, xu2021monoallelicmutationsin pages 1-2, li2025twocasesof pages 1-2) |
| Core mechanism | Disease results from impaired **PGE2 catabolism**: **SLCO2A1/OATP2A1 (PGT)** mediates cellular uptake of prostaglandins, and **15-PGDH (HPGD)** oxidizes PGE2 to **PGE-M**. Deficiency of either step elevates PGE2, promoting angiogenesis, fibroblast activity, endothelial changes, and abnormal bone remodeling/periostosis (lu2023primaryhypertrophicosteoarthropathy pages 2-4, lu2023primaryhypertrophicosteoarthropathy pages 4-6, li2025twocasesof pages 1-2) |
| Key biomarkers | **Urinary PGE2 is elevated across PHO subtypes**. In **HPGD deficiency (PHOAR1)**, **urinary PGE-M usually decreases** and the **PGE2/PGE-M ratio rises**; in **SLCO2A1 deficiency (PHOAR2)**, **urinary PGE-M usually increases** and the **PGE2/PGE-M ratio is near normal**. Reported median urinary **PGE2:creatinine** in HPGD-related literature review: **627.1 ng/mmol** versus **61.49 ng/mmol** normal. In one comparison, urinary PGE2 median was **277.58 ng/mmol creatinine** in PHOAD vs **473.19 ng/mmol** in PHOAR2 (**p=0.038**) (lu2023primaryhypertrophicosteoarthropathy pages 4-6, li2025twocasesof pages 1-2, xu2021monoallelicmutationsin pages 1-2) |
| Hallmark clinical triad | **Digital clubbing + pachydermia + periostosis** are the hallmark triad. Clubbing occurs in **almost all PHO patients** and is often the initial symptom. Periostosis is typically **symmetric** and often affects long bones (radius, ulna, tibia, metacarpals, metatarsals) (lu2023primaryhypertrophicosteoarthropathy pages 4-6, lu2023primaryhypertrophicosteoarthropathy pages 1-2, nicolau2023tourainesolentegolesyndromepathogenic pages 1-2) |
| Common additional features | Frequent additional manifestations include **hyperhidrosis**, **seborrhea/acne**, **cutis verticis gyrata**, **joint swelling/stiffness/arthralgia**, **acro-osteolysis**, **anemia**, and occasional **gastrointestinal involvement**. Quantitative data from an HPGD review/case series: **hyperhidrosis 60.1%**, **joint pain 46.1%**, **joint swelling 37.1%**, **osteolysis 30.3%**, **delayed cranial suture closure 16.9%**, **patent ductus arteriosus 15.7%**; median symptom onset **5.1 years**, median diagnosis **22.1 years**, male:female **2.2:1** (li2025twocasesof pages 4-7, li2025twocasesof pages 1-2, lu2023primaryhypertrophicosteoarthropathy pages 4-6) |
| GI / systemic complications | GI disease is especially linked to **SLCO2A1**-related PHO. In a Chinese review of **158** patients, **17.2%** had gastrointestinal involvement; among those with GI disease, **anemia 40.0% vs 4.5%**, **hypoalbuminemia 16.7% vs 0.9%**, **myelofibrosis 19.0% vs 0.9%** compared with PHO patients without GI involvement; **86.7% (13/15)** with GI complications had **SLCO2A1** variants (rodriguez2009primaryhypertrophicosteoarthropathy pages 3-4) |
| Epidemiologic notes | PHO is rare; secondary hypertrophic osteoarthropathy accounts for the large majority of HOA overall (**~95%**), so exclusion of secondary causes is essential. Sex skew varies by subtype: **PHOAR1 ~1:1 male:female**, whereas **PHOAR2/PHOAD are predominantly male**; some older reports cite male predominance around **7:1** or **9:1** in clinically defined PDP/PHO cohorts (nicolau2023tourainesolentegolesyndromepathogenic pages 2-5, rodriguez2009primaryhypertrophicosteoarthropathy pages 3-4, lu2023primaryhypertrophicosteoarthropathy pages 4-6, nicolau2023tourainesolentegolesyndromepathogenic pages 1-2, joshi2019pachydermoperiostosis(touraine–solente–golesyndrome) pages 1-2) |
| Etoricoxib / COX-2 inhibitors | Best-supported targeted symptomatic therapy because **COX-2** is rate-limiting for prostaglandin synthesis. A **6-month** intervention in **41 PHO patients** showed significant reduction in urinary PGE2 and **clinical remission/improvement of digital clubbing, pachydermia, and arthritic symptoms**, but **periostosis and anemia did not improve**; GI ulcer/bleeding may persist or worsen. A ClinicalTrials.gov study (**NCT02438709**) evaluated **etoricoxib 60 mg daily**, enrollment **30**, with outcomes including **PGE2 at 3 and 6 months**, pain VAS, finger volume, and knee circumference (lu2023primaryhypertrophicosteoarthropathy pages 7-8, NCT02438709 chunk 1) |
| NSAIDs (nonselective) | Commonly used for pain and arthritis-related symptoms; can improve joint pain/swelling, morning stiffness, and inflammatory markers, but are **palliative** and limited by **gastrointestinal toxicity**, especially problematic in PHO with GI involvement. Some reports note poor response in individual cases (nicolau2023tourainesolentegolesyndromepathogenic pages 2-5, almalki2024pachydermoperiostosisdueto pages 1-2, rodriguez2009primaryhypertrophicosteoarthropathy pages 3-4) |
| Bisphosphonates | Reported as adjunctive treatment for **musculoskeletal pain** and high bone turnover; evidence is limited to case reports/small series (e.g., pamidronate mentioned in review literature), with rationale to reduce increased bone remodeling rather than correct the upstream prostaglandin defect (li2025twocasesof pages 4-7, li2025twocasesof pages 8-9, rodriguez2009primaryhypertrophicosteoarthropathy pages 3-4) |
| Lanreotide | Evidence limited to a 2024 HPGD splice-variant case report initially mistaken for acromegaly: symptoms responded poorly to NSAIDs but showed **excellent response to lanreotide autogel** used for **~1 year**. This is anecdotal and not established standard therapy (almalki2024pachydermoperiostosisdueto pages 1-2) |
| Other reported therapies | Refractory or supportive options reported in case literature include **hydroxychloroquine, tamoxifen, octreotide, colchicine, botulinum toxin A, intra-articular steroids, synovectomy/radiosynoviorthesis**, and **plastic surgery** for severe ptosis/skin changes. Evidence remains low-level and case-based (nicolau2023tourainesolentegolesyndromepathogenic pages 2-5, li2025twocasesof pages 8-9, rodriguez2009primaryhypertrophicosteoarthropathy pages 3-4) |


*Table: This table condenses the main identifiers, genetics, biomarkers, phenotype spectrum, and treatment evidence for primary hypertrophic osteoarthropathy/pachydermoperiostosis. It is designed for quick knowledge-base population using only the cited context IDs.*

---

## 1. Disease information

### 1.1 Definition / overview
PHO is an inherited disorder of skeletal and skin abnormalities, classically presenting with **digital clubbing, pachydermia, and periostosis**. (lu2023primaryhypertrophicosteoarthropathy pages 1-2, li2025twocasesof pages 1-2)

**Recent authoritative definition (2023 review, Frontiers in Endocrinology; published 29 Aug 2023; URL: https://doi.org/10.3389/fendo.2023.1235040):** The abstract states: *“Primary hypertrophic osteoarthropathy (PHO) is a genetic disorder mainly characterized by clubbing fingers, pachydermia and periostosis.”* (lu2023primaryhypertrophicosteoarthropathy pages 1-2)

### 1.2 Key identifiers (with evidence available in retrieved sources)
* **OMIM/MIM (genetic subtypes):** PHOAR1 **MIM 259100**, PHOAR2 **MIM 614441**, PHOAD **MIM 167100**. (lu2023primaryhypertrophicosteoarthropathy pages 1-2, xu2021monoallelicmutationsin pages 1-2)
* **OMIM/MIM (genes):** **HPGD MIM 601688**, **SLCO2A1 MIM 601460**. (xu2021monoallelicmutationsin pages 1-2)
* **MeSH:** “Osteoarthropathy, Primary Hypertrophic” **MeSH ID D010004** is present in the ClinicalTrials.gov record for PHO. (NCT02438709 chunk 1)

**Not available in retrieved evidence:** MONDO ID, ICD-10/ICD-11 codes, and a verified Orphanet ORPHA code were not explicitly present in the retrieved full-text evidence; they therefore cannot be asserted here without external database verification. (shahin2025theroleof pages 5-5)

### 1.3 Synonyms / alternative names
* Primary hypertrophic osteoarthropathy (PHO) (lu2023primaryhypertrophicosteoarthropathy pages 1-2)
* Pachydermoperiostosis (PDP) (xu2021monoallelicmutationsin pages 1-2)
* Touraine–Solente–Golé syndrome (lu2023primaryhypertrophicosteoarthropathy pages 1-2, joshi2019pachydermoperiostosis(touraine–solente–golesyndrome) pages 1-2)

### 1.4 Evidence source type
The information synthesized here is derived from **aggregated disease-level review literature** (notably a 2023 review) plus **primary patient-level evidence** (case reports/series and a 2025 systematic review of HPGD-related cases), and a **trial registry record** (ClinicalTrials.gov). (lu2023primaryhypertrophicosteoarthropathy pages 1-2, li2025twocasesof pages 1-2, almalki2024pachydermoperiostosisdueto pages 1-2, NCT02438709 chunk 1)

---

## 2. Etiology

### 2.1 Disease causal factors
PHO is primarily **genetic**, caused by impaired PGE2 degradation/transport:
* **HPGD** encodes **15-hydroxyprostaglandin dehydrogenase (15-PGDH)**, the key enzyme that oxidizes (inactivates) PGE2. (lu2023primaryhypertrophicosteoarthropathy pages 2-4)
* **SLCO2A1** encodes **OATP2A1 / prostaglandin transporter (PGT)**, which mediates cellular prostaglandin uptake needed for intracellular degradation. (lu2023primaryhypertrophicosteoarthropathy pages 1-2, lu2023primaryhypertrophicosteoarthropathy pages 2-4)

A two-step clearance model is described: (1) selective uptake across the plasma membrane and (2) oxidation in the cell; deficiency of either elevates prostaglandins. (lu2023primaryhypertrophicosteoarthropathy pages 2-4)

### 2.2 Genetic risk factors (causal genes, inheritance)
**Genetic subtypes/inheritance:**
* **PHOAR1 (AR):** caused by **HPGD** mutation. (lu2023primaryhypertrophicosteoarthropathy pages 1-2)
* **PHOAR2 (AR):** caused by **SLCO2A1** biallelic mutation. (lu2023primaryhypertrophicosteoarthropathy pages 1-2)
* **PHOAD (AD):** caused by **SLCO2A1 monoallelic** pathogenic variants. (lu2023primaryhypertrophicosteoarthropathy pages 1-2, xu2021monoallelicmutationsin pages 1-2)

**Authoritative 2021 primary genetics paper (Journal of Bone and Mineral Research; Apr 2021; URL: https://doi.org/10.1002/jbmr.4310):** abstract states: *“Monoallelic mutations in SLCO2A1 cause autosomal dominant primary hypertrophic osteoarthropathy.”* (xu2021monoallelicmutationsin pages 1-2)

### 2.3 Examples of pathogenic variants (recent/illustrative)
* **HPGD** splicing variant: **NM_000860.6: c.662+5_662+8del**, shown by RT-PCR to cause exon skipping, frameshift, and truncation; case masquerading as acromegaly. (JCEM Case Reports; Nov 2024; URL: https://doi.org/10.1210/jcemcr/luae215) (almalki2024pachydermoperiostosisdueto pages 1-2)
* **HPGD** loss-of-function variants in pediatric cases: **c.189C>A (p.C63*)**, **c.310_311delCT (p.L104Afs*3)**, **c.324+5G>A** (BMC Pediatrics; Mar 2025; URL: https://doi.org/10.1186/s12887-025-05590-z) (li2025twocasesof pages 4-7, li2025twocasesof pages 1-2)
* **SLCO2A1** PHOAD variants (examples from families): **c.1660G>A (p.G554R)**, **c.664G>A (p.G222R)**, **c.1106G>A (p.G369D)**, **c.1065dupA (p.Q356TfsX77)**, **c.1293delT (p.S432AfsX48)**, **c.1807C>T (p.R603X)**. (xu2021monoallelicmutationsin pages 1-2)

### 2.4 Environmental risk/protective factors
No robust, disease-specific environmental risk or protective factors were identified in the retrieved evidence; PHO is primarily a monogenic prostaglandin-metabolism disorder. Secondary hypertrophic osteoarthropathy (not PHO) is associated with underlying systemic disease (e.g., malignancy, infections, lung disease), which must be excluded diagnostically. (lu2023primaryhypertrophicosteoarthropathy pages 7-8, rodriguez2009primaryhypertrophicosteoarthropathy pages 3-4)

### 2.5 Gene–environment interactions
No explicit gene–environment interaction evidence was present in the retrieved texts.

---

## 3. Phenotypes

### 3.1 Core phenotype triad (clinical signs)
* **Digital clubbing** (often initial and “almost all” patients in a large clinical perspective review) (lu2023primaryhypertrophicosteoarthropathy pages 4-6)
* **Pachydermia** (skin thickening/furrowing; may include cutis verticis gyrata) (lu2023primaryhypertrophicosteoarthropathy pages 4-6)
* **Periostosis** (symmetric involvement of long bones; radiographic new bone formation) (lu2023primaryhypertrophicosteoarthropathy pages 4-6)

### 3.2 Additional phenotypes (with quantitative data where available)
A 2025 systematic literature review of **89 HPGD-related PHO cases** reported frequencies including: **hyperhidrosis 60.1%**, **joint pain 46.1%**, **joint swelling 37.1%**, **osteolysis 30.3%**, **delayed cranial suture closure 16.9%**, and **patent ductus arteriosus 15.7%**. (li2025twocasesof pages 4-7)

Other commonly described manifestations include seborrhea/acne, cutis verticis gyrata, arthropathy, acro-osteolysis, anemia and GI abnormalities. (lu2023primaryhypertrophicosteoarthropathy pages 4-6, xu2021monoallelicmutationsin pages 1-2)

### 3.3 Onset and progression (temporal development)
* Onset is often described with peaks **postnatally and at puberty**, and differs by subtype: PHOAR1 tends to begin earlier (after birth), whereas PHOAR2/PHOAD typically begin in adolescence. (lu2023primaryhypertrophicosteoarthropathy pages 4-6)
* In the 2025 review of HPGD cases, **median symptom onset was 5.1 years** but **median age at diagnosis was 22.1 years**, indicating substantial diagnostic delay. (li2025twocasesof pages 4-7)

### 3.4 Quality of life impact
Direct quality-of-life instrument data (e.g., SF-36, EQ-5D) were not found in the retrieved evidence. Functional impact is inferred from pain, joint swelling/stiffness, and disfiguring skin changes (including ptosis/cutis verticis gyrata), and from delays in correct diagnosis. (lu2023primaryhypertrophicosteoarthropathy pages 4-6, rodriguez2009primaryhypertrophicosteoarthropathy pages 3-4)

### 3.5 Suggested HPO terms (non-exhaustive)
Based on described manifestations:
* Digital clubbing — HP:0100759
* Pachydermia / skin thickening — HP:0001067 (general) / HP:0008066 (thickened skin; depends on exact mapping)
* Periostosis — HP:0002758
* Hyperhidrosis — HP:0000975
* Acne — HP:0001061
* Cutis verticis gyrata — HP:0007539
* Acro-osteolysis — HP:0006046
* Arthralgia — HP:0002829
* Joint swelling — HP:0001386
* Anemia — HP:0001903
* Patent ductus arteriosus — HP:0001643

(li2025twocasesof pages 4-7, lu2023primaryhypertrophicosteoarthropathy pages 4-6, xu2021monoallelicmutationsin pages 1-2)

---

## 4. Genetic / molecular information

### 4.1 Causal genes
* **HPGD** (15-PGDH) (lu2023primaryhypertrophicosteoarthropathy pages 1-2)
* **SLCO2A1** (OATP2A1/PGT) (lu2023primaryhypertrophicosteoarthropathy pages 1-2)

### 4.2 Molecular mechanism (current understanding)
**Upstream defect:** impaired prostaglandin clearance due to loss of PGT-mediated uptake (SLCO2A1) and/or 15-PGDH-mediated oxidation (HPGD). (lu2023primaryhypertrophicosteoarthropathy pages 2-4)

**Biochemical consequence:** elevated PGE2; 2023 review states it is “generally accepted” that PGE2 plays important roles in PHO development, and that mutations in either gene impair degradation and elevate PGE2. (lu2023primaryhypertrophicosteoarthropathy pages 4-6)

**Downstream signaling:** PGE2 signals via EP1–EP4 receptors (GPCRs). The 2023 review highlights EP receptor biology and notes EP4 signaling in particular in skeletal biology (including a proposed sensory nerve EP4 axis). (lu2023primaryhypertrophicosteoarthropathy pages 2-4, lu2023primaryhypertrophicosteoarthropathy pages 4-6)

**Cell/tissue-level effects:** PGE2 is linked to cell proliferation and angiogenesis seen in histology of clubbing/skin; VEGF is discussed as a mediator whose expression can be stimulated by PGE2. (lu2023primaryhypertrophicosteoarthropathy pages 2-4, lu2023primaryhypertrophicosteoarthropathy pages 4-6)

### 4.3 Modifier genes / epigenetics / chromosomal abnormalities
No modifier genes, epigenetic mechanisms, or chromosomal abnormalities were identified in the retrieved evidence.

### 4.4 Suggested GO biological process terms (examples)
* Prostaglandin metabolic process — GO:0006693
* Prostaglandin biosynthetic process — GO:0001516
* Inflammatory response — GO:0006954
* Angiogenesis — GO:0001525
* Bone remodeling — GO:0046849

(lu2023primaryhypertrophicosteoarthropathy pages 2-4, lu2023primaryhypertrophicosteoarthropathy pages 4-6)

### 4.5 Suggested Cell Ontology (CL) terms (examples)
Based on described receptor/pathology targets:
* Osteoblast — CL:0000062
* Osteoclast — CL:0000092
* Endothelial cell — CL:0000115
* Fibroblast — CL:0000057

(lu2023primaryhypertrophicosteoarthropathy pages 4-6, lu2023primaryhypertrophicosteoarthropathy pages 2-4)

---

## 5. Environmental information
PHO is a primary genetic disorder; the retrieved evidence did not identify specific toxins, lifestyle risks, or infectious triggers. Key “environmental” considerations are iatrogenic—e.g., NSAID-related GI risk is clinically relevant, particularly when GI involvement exists. (rodriguez2009primaryhypertrophicosteoarthropathy pages 3-4, lu2023primaryhypertrophicosteoarthropathy pages 7-8)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (high-level)
1. **HPGD or SLCO2A1 pathogenic variants** → 2. **impaired PGE2 uptake/oxidation (two-step clearance defect)** → 3. **elevated PGE2 (and altered PGE-M patterns depending on gene)** → 4. **EP receptor signaling, angiogenesis/VEGF association, fibroblast/endothelial changes, altered bone turnover** → 5. **digital clubbing, pachydermia, periostosis; joint symptoms and systemic complications in subsets**. (lu2023primaryhypertrophicosteoarthropathy pages 2-4, lu2023primaryhypertrophicosteoarthropathy pages 4-6)

### 6.2 Upstream vs downstream
* **Upstream:** COX-2 mediated synthesis (targetable), PGT uptake, 15-PGDH oxidation. (lu2023primaryhypertrophicosteoarthropathy pages 2-4, lu2023primaryhypertrophicosteoarthropathy pages 1-2)
* **Downstream:** EP receptor signaling, VEGF/PDGF-associated angiogenic/fibrotic changes; periosteal new bone formation and arthropathy. (lu2023primaryhypertrophicosteoarthropathy pages 2-4, lu2023primaryhypertrophicosteoarthropathy pages 4-6)

### 6.3 Suggested pathway/therapeutic targets
The 2023 review notes COX-2 as the rate-limiting enzyme for prostaglandin production and discusses future possibilities including targeting PGES or blocking prostaglandin action (e.g., EP4 antagonists). (lu2023primaryhypertrophicosteoarthropathy pages 7-8, lu2023primaryhypertrophicosteoarthropathy pages 2-4)

---

## 7. Anatomical structures affected

### 7.1 Organ/system level
* **Skeletal system:** periosteum and long bones (radius/ulna/tibia/metacarpals/metatarsals), phalanges; acro-osteolysis can occur. (lu2023primaryhypertrophicosteoarthropathy pages 4-6)
* **Skin and adnexa:** facial/scalp skin thickening, sebaceous gland changes, hyperhidrosis; cutis verticis gyrata in severe cases. (lu2023primaryhypertrophicosteoarthropathy pages 4-6)
* **Joints:** knees commonly involved; joint swelling/stiffness; typically non-erosive but can mimic inflammatory arthritis clinically. (lu2023primaryhypertrophicosteoarthropathy pages 4-6, nicolau2023tourainesolentegolesyndromepathogenic pages 1-2)
* **Gastrointestinal tract (subset, especially SLCO2A1):** diarrhea, chronic gastritis, peptic ulcer/bleeding, intestinal stenosis; anemia/hypoproteinemia may result. (rodriguez2009primaryhypertrophicosteoarthropathy pages 3-4, lu2023primaryhypertrophicosteoarthropathy pages 4-6)

### 7.2 Suggested UBERON terms (examples)
* Long bone of upper limb — UBERON:0001463
* Tibia — UBERON:0000979
* Skin of face — UBERON:0001456
* Periosteum — UBERON:0001424
* Knee joint — UBERON:0001465
* Small intestine — UBERON:0002108

(lu2023primaryhypertrophicosteoarthropathy pages 4-6, rodriguez2009primaryhypertrophicosteoarthropathy pages 3-4)

---

## 8. Temporal development

### 8.1 Onset
* PHO onset can occur after birth or at puberty with subtype-specific patterns; median onset age for PHOAR1 reported as **2 years** in one cohort cited within the 2023 review context. (lu2023primaryhypertrophicosteoarthropathy pages 4-6)

### 8.2 Progression/course
The condition generally progresses slowly, with symptoms often evolving over years and diagnosis frequently delayed into adulthood; substantial diagnostic delay is quantified in the 2025 review (median diagnosis 22.1 years vs onset 5.1 years). (li2025twocasesof pages 4-7)

---

## 9. Inheritance and population

### 9.1 Epidemiology
Robust population prevalence/incidence is not established in the retrieved evidence base. A case report cites “estimated prevalence ~0.16%” and male:female ~7:1, but this estimate is not corroborated by an epidemiologic study in the retrieved set and should be treated cautiously. (joshi2019pachydermoperiostosis(touraine–solente–golesyndrome) pages 1-2)

### 9.2 Sex ratio and subtype differences
Subtype-specific sex patterns are emphasized:
* PHOAR1: male:female ~1:1 (lu2023primaryhypertrophicosteoarthropathy pages 4-6)
* PHOAR2/PHOAD: predominantly male in reported series (lu2023primaryhypertrophicosteoarthropathy pages 4-6)

In the HPGD-focused systematic review of 89 cases, male predominance was quantified as **male:female 2.2:1**. (li2025twocasesof pages 4-7)

### 9.3 Penetrance/expressivity
PHO shows variable expressivity and can follow recessive or irregular dominant patterns; autosomal dominant familial transmission in 54.4% of families (historical review) is referenced in both the 2023 review and 2021 genetics paper. (lu2023primaryhypertrophicosteoarthropathy pages 2-4, xu2021monoallelicmutationsin pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical criteria
A specific diagnostic rule (attributed to Borochowitz et al. in a case report) states that PHO/PDP diagnosis should be made when **≥2** of the following are present: **(i) family history, (ii) clubbing, (iii) hypertrophic skin changes, (iv) bone pain/radiographic changes**. (joshi2019pachydermoperiostosis(touraine–solente–golesyndrome) pages 1-2)

### 10.2 Laboratory biomarkers
**Key biomarkers (urine):**
* Urinary **PGE2** is a key biological indicator and is elevated across subtypes. (lu2023primaryhypertrophicosteoarthropathy pages 4-6)
* **PGE-M** patterns help subtype discrimination: typically decreased in HPGD deficiency and increased in SLCO2A1 deficiency; the urinary **PGE2/PGE-M ratio** differs by genetic subtype. (lu2023primaryhypertrophicosteoarthropathy pages 4-6)

A 2025 HPGD-case systematic review reported a median urinary **PGE2-to-creatinine ratio 627.1 ng/mmol** vs **61.49 ng/mmol** normal. (li2025twocasesof pages 1-2)

### 10.3 Imaging
Plain radiographs show periosteal ossification/cortical thickening and may show acro-osteolysis. (nicolau2023tourainesolentegolesyndromepathogenic pages 1-2, lu2023primaryhypertrophicosteoarthropathy pages 4-6)

### 10.4 Genetic testing approach (real-world implementation)
* Sequencing of **HPGD** and **SLCO2A1** is confirmatory and supports counseling; WES and Sanger confirmation are used in case workups. (almalki2024pachydermoperiostosisdueto pages 1-2, li2025twocasesof pages 1-2)

### 10.5 Differential diagnosis
Secondary hypertrophic osteoarthropathy is more common (~95% of HOA overall) and must be excluded; additional differentials include acromegaly, thyroid acropachy, rheumatoid/psoriatic arthritis, and juvenile idiopathic arthritis. (rodriguez2009primaryhypertrophicosteoarthropathy pages 3-4, nicolau2023tourainesolentegolesyndromepathogenic pages 1-2)

---

## 11. Outcome / prognosis
Mortality and life expectancy data were not identified in the retrieved evidence. Morbidity is driven by chronic pain, joint symptoms, disfigurement, anemia, and GI complications in subsets. Anemia is described as a major complication, potentially related to GI hemorrhage or myelofibrosis. (lu2023primaryhypertrophicosteoarthropathy pages 4-6, rodriguez2009primaryhypertrophicosteoarthropathy pages 3-4)

---

## 12. Treatment

### 12.1 Pharmacotherapy (current practice)
**COX-2 inhibition (etoricoxib; highest-quality evidence in retrieved set):**
* The 2023 review reports that in a **6-month clinical intervention in 41 PHO patients**, **urinary PGE2 significantly decreased** and patients experienced **clinical remission** of clubbing, pachydermia, and arthritic symptoms, but **periostosis was not relieved**; anemia and GI issues may not improve. (lu2023primaryhypertrophicosteoarthropathy pages 7-8)

**Clinical trial registry evidence (real-world implementation):**
* ClinicalTrials.gov **NCT02438709** (“Application of COX-2 Inhibitor for Treatment of Primary Hypertrophic Osteoarthropathy”; first posted 08 May 2015; sponsor Peking Union Medical College Hospital) describes **etoricoxib 60 mg daily** with primary outcomes measuring **serum PGE2 change at 3 and 6 months**, and secondary outcomes including pain VAS and distal finger volume. (NCT02438709 chunk 1)

**NSAIDs:** commonly used for symptomatic relief; however GI toxicity is an important limitation, especially in those with GI involvement. (nicolau2023tourainesolentegolesyndromepathogenic pages 2-5, rodriguez2009primaryhypertrophicosteoarthropathy pages 3-4)

**Bisphosphonates:** reported for musculoskeletal pain/high bone turnover, but evidence is largely case-based and not definitive. (li2025twocasesof pages 4-7, rodriguez2009primaryhypertrophicosteoarthropathy pages 3-4)

### 12.2 Other/experimental or case-based therapies
* **Lanreotide autogel**: a 2024 HPGD splicing case report notes poor NSAID response but “excellent response” to lanreotide for ~1 year. (almalki2024pachydermoperiostosisdueto pages 1-2)
* Additional reported therapies include hydroxychloroquine, tamoxifen, octreotide, colchicine, botulinum toxin A, intra-articular steroids, synovectomy/radiosynoviorthesis, and plastic surgery for severe ptosis/skin. (nicolau2023tourainesolentegolesyndromepathogenic pages 2-5, rodriguez2009primaryhypertrophicosteoarthropathy pages 3-4, li2025twocasesof pages 8-9)

### 12.3 Suggested MAXO terms (examples)
* Cyclooxygenase-2 inhibitor therapy (e.g., etoricoxib)
* Nonsteroidal anti-inflammatory drug therapy
* Bisphosphonate therapy
* Genetic counseling
* Whole-exome sequencing / molecular genetic testing

(lu2023primaryhypertrophicosteoarthropathy pages 7-8, NCT02438709 chunk 1, li2025twocasesof pages 4-7)

---

## 13. Prevention
No primary prevention (in the sense of preventing disease occurrence) is established for monogenic PHO in the retrieved evidence. Practical prevention focuses on:
* **Genetic counseling**, cascade testing in families, and reproductive counseling given recessive/dominant forms. (xu2021monoallelicmutationsin pages 2-3, lu2023primaryhypertrophicosteoarthropathy pages 1-2)
* **Tertiary prevention:** mitigating complications (e.g., monitoring/avoiding GI harms from NSAIDs/COX-2 inhibitors in patients with GI disease; multidisciplinary management to reduce diagnostic delays). (rodriguez2009primaryhypertrophicosteoarthropathy pages 3-4, li2025twocasesof pages 4-7)

---

## 14. Other species / natural disease
No naturally occurring veterinary analogs or cross-species susceptibility data were identified in the retrieved evidence.

---

## 15. Model organisms
The 2023 review notes major limitations of animal models: **HPGD−/− and SLCO2A1−/− mice are not viable postnatally**, and pharmacologic modulation of 15-PGDH affects bone/muscle but does not reproduce PHO skeletal phenotype; better models are needed. (lu2023primaryhypertrophicosteoarthropathy pages 7-8)

---

## Recent developments (prioritizing 2023–2024)
1. **2023 synthesis of genetics, biomarkers, and management**: Lu et al. (Frontiers in Endocrinology; 29 Aug 2023; https://doi.org/10.3389/fendo.2023.1235040) provides an updated mechanistic view linking PHO to the prostaglandin metabolic pathway and emphasizes urinary PGE2 and PGE-M profiles for subtype discrimination and monitoring. (lu2023primaryhypertrophicosteoarthropathy pages 2-4, lu2023primaryhypertrophicosteoarthropathy pages 4-6)
2. **2024 novel HPGD splice variant and nonstandard therapy experience**: Almalki et al. (JCEM Case Reports; Nov 2024; https://doi.org/10.1210/jcemcr/luae215) describes a novel splice variant with molecular confirmation and reports clinical improvement on lanreotide autogel. (almalki2024pachydermoperiostosisdueto pages 1-2)

---

## Notes on evidence gaps
* This report cannot supply a verified **MONDO ID**, **ICD-10/ICD-11 codes**, or a confirmed **Orphanet ORPHA code**, because they were not explicitly present in the retrieved evidence snippets. (shahin2025theroleof pages 5-5)
* No high-quality epidemiologic prevalence/incidence studies were retrieved; frequency data are therefore drawn mainly from genotype-focused systematic reviews and case series. (li2025twocasesof pages 4-7, joshi2019pachydermoperiostosis(touraine–solente–golesyndrome) pages 1-2)

---

## Key sources (URLs, dates)
* Lu Q et al. **Primary hypertrophic osteoarthropathy: genetics, clinical features and management**. Frontiers in Endocrinology. **Published 29 Aug 2023**. https://doi.org/10.3389/fendo.2023.1235040 (lu2023primaryhypertrophicosteoarthropathy pages 1-2)
* Almalki MH et al. **Pachydermoperiostosis Due to a Novel HPGD Splicing Site Mutation Masquerading as Acromegaly**. JCEM Case Reports. **Nov 2024**. https://doi.org/10.1210/jcemcr/luae215 (almalki2024pachydermoperiostosisdueto pages 1-2)
* Xu Y et al. **Monoallelic mutations in SLCO2A1 cause autosomal dominant primary hypertrophic osteoarthropathy**. Journal of Bone and Mineral Research. **Apr 2021**. https://doi.org/10.1002/jbmr.4310 (xu2021monoallelicmutationsin pages 1-2)
* Li J et al. **Two cases of primary hypertrophic osteoarthropathy caused by HPGD variants: a case report and literature review**. BMC Pediatrics. **Mar 2025**. https://doi.org/10.1186/s12887-025-05590-z (li2025twocasesof pages 1-2)
* Nicolau R et al. **Touraine-Solente-Gole syndrome: pathogenic variant in SLCO2A1…** Pediatric Rheumatology. **May 2023**. https://doi.org/10.1186/s12969-023-00831-w (nicolau2023tourainesolentegolesyndromepathogenic pages 2-5)
* ClinicalTrials.gov: **NCT02438709**. First posted **08 May 2015**. (NCT02438709 chunk 1)


References

1. (lu2023primaryhypertrophicosteoarthropathy pages 1-2): Q. Lu, Yang Xu, Zeng Zhang, Shan-shan Li, and Zhenlin Zhang. Primary hypertrophic osteoarthropathy: genetics, clinical features and management. Frontiers in Endocrinology, Aug 2023. URL: https://doi.org/10.3389/fendo.2023.1235040, doi:10.3389/fendo.2023.1235040. This article has 51 citations.

2. (li2025twocasesof pages 1-2): Jun Li, Shilei Jia, Jianqun Guo, Wenhui Xie, Yijiao Ma, Xiaojie Gao, and Meihao Gao. Two cases of primary hypertrophic osteoarthropathy caused by hpgd variants: a case report and literature review. BMC Pediatrics, Mar 2025. URL: https://doi.org/10.1186/s12887-025-05590-z, doi:10.1186/s12887-025-05590-z. This article has 1 citations and is from a peer-reviewed journal.

3. (lu2023primaryhypertrophicosteoarthropathy pages 7-8): Q. Lu, Yang Xu, Zeng Zhang, Shan-shan Li, and Zhenlin Zhang. Primary hypertrophic osteoarthropathy: genetics, clinical features and management. Frontiers in Endocrinology, Aug 2023. URL: https://doi.org/10.3389/fendo.2023.1235040, doi:10.3389/fendo.2023.1235040. This article has 51 citations.

4. (nicolau2023tourainesolentegolesyndromepathogenic pages 1-2): Rafaela Nicolau, Tiago Beirão, Francisca Guimarães, Francisca Aguiar, Sara Ganhão, Mariana Rodrigues, Ana Grangeia, and Iva Brito. Touraine-solente-gole syndrome: pathogenic variant in slco2a1 presented with polyarthralgia and digital clubbing. Pediatric Rheumatology Online Journal, May 2023. URL: https://doi.org/10.1186/s12969-023-00831-w, doi:10.1186/s12969-023-00831-w. This article has 6 citations.

5. (joshi2019pachydermoperiostosis(touraine–solente–golesyndrome) pages 1-2): Amir Joshi, Gaurav Nepal, Yow Ka Shing, Hari Prasad Panthi, and Suman Baral. Pachydermoperiostosis (touraine–solente–gole syndrome): a case report. Journal of Medical Case Reports, Feb 2019. URL: https://doi.org/10.1186/s13256-018-1961-z, doi:10.1186/s13256-018-1961-z. This article has 24 citations and is from a peer-reviewed journal.

6. (cai2025distinctfeaturesof pages 1-2): Xilei Cai, Xiujuan Yang, Pengyue Zhang, Ziyue Dou, Zilian Chen, Chongzhi Zhu, Weiwei Xu, Xinchen Wang, Xiaodan Hong, and Zhenhua Zhang. Distinct features of three clinical subtypes in 533 patients with primary hypertrophic osteoarthropathy. Orphanet Journal of Rare Diseases, Apr 2025. URL: https://doi.org/10.1186/s13023-025-03722-3, doi:10.1186/s13023-025-03722-3. This article has 1 citations and is from a peer-reviewed journal.

7. (xu2021monoallelicmutationsin pages 1-2): Yang Xu, Zeng Zhang, Hua Yue, Shanshan Li, and Zhenlin Zhang. Monoallelic mutations in slco2a1 cause autosomal dominant primary hypertrophic osteoarthropathy. Journal of Bone and Mineral Research, 36:1459-1468, Apr 2021. URL: https://doi.org/10.1002/jbmr.4310, doi:10.1002/jbmr.4310. This article has 39 citations and is from a highest quality peer-reviewed journal.

8. (NCT02438709 chunk 1):  Effect Observation Study of COX-2 Inhibitor to Treat Primary Hypertrophic Osteoarthropathy. Peking Union Medical College Hospital. 2012. ClinicalTrials.gov Identifier: NCT02438709

9. (lu2023primaryhypertrophicosteoarthropathy pages 2-4): Q. Lu, Yang Xu, Zeng Zhang, Shan-shan Li, and Zhenlin Zhang. Primary hypertrophic osteoarthropathy: genetics, clinical features and management. Frontiers in Endocrinology, Aug 2023. URL: https://doi.org/10.3389/fendo.2023.1235040, doi:10.3389/fendo.2023.1235040. This article has 51 citations.

10. (lu2023primaryhypertrophicosteoarthropathy pages 4-6): Q. Lu, Yang Xu, Zeng Zhang, Shan-shan Li, and Zhenlin Zhang. Primary hypertrophic osteoarthropathy: genetics, clinical features and management. Frontiers in Endocrinology, Aug 2023. URL: https://doi.org/10.3389/fendo.2023.1235040, doi:10.3389/fendo.2023.1235040. This article has 51 citations.

11. (li2025twocasesof pages 4-7): Jun Li, Shilei Jia, Jianqun Guo, Wenhui Xie, Yijiao Ma, Xiaojie Gao, and Meihao Gao. Two cases of primary hypertrophic osteoarthropathy caused by hpgd variants: a case report and literature review. BMC Pediatrics, Mar 2025. URL: https://doi.org/10.1186/s12887-025-05590-z, doi:10.1186/s12887-025-05590-z. This article has 1 citations and is from a peer-reviewed journal.

12. (rodriguez2009primaryhypertrophicosteoarthropathy pages 3-4): Norberto Gómez Rodríguez, Jesús Ibáñez Ruán, and Marisol González Pérez. Primary hypertrophic osteoarthropathy (pachydermoperiostosis). report of 2 familial cases and literature review. Reumatología Clínica, 5:259-263, Nov 2009. URL: https://doi.org/10.1016/s2173-5743(09)70134-0, doi:10.1016/s2173-5743(09)70134-0. This article has 19 citations.

13. (nicolau2023tourainesolentegolesyndromepathogenic pages 2-5): Rafaela Nicolau, Tiago Beirão, Francisca Guimarães, Francisca Aguiar, Sara Ganhão, Mariana Rodrigues, Ana Grangeia, and Iva Brito. Touraine-solente-gole syndrome: pathogenic variant in slco2a1 presented with polyarthralgia and digital clubbing. Pediatric Rheumatology Online Journal, May 2023. URL: https://doi.org/10.1186/s12969-023-00831-w, doi:10.1186/s12969-023-00831-w. This article has 6 citations.

14. (almalki2024pachydermoperiostosisdueto pages 1-2): Mussa H. Almalki, B. Alghamdi, Allianah D. Benito, Ahmed Alfares, and A. S. Alzahrani. Pachydermoperiostosis due to a novel hpgd splicing site mutation masquerading as acromegaly. JCEM Case Reports, Nov 2024. URL: https://doi.org/10.1210/jcemcr/luae215, doi:10.1210/jcemcr/luae215. This article has 1 citations.

15. (li2025twocasesof pages 8-9): Jun Li, Shilei Jia, Jianqun Guo, Wenhui Xie, Yijiao Ma, Xiaojie Gao, and Meihao Gao. Two cases of primary hypertrophic osteoarthropathy caused by hpgd variants: a case report and literature review. BMC Pediatrics, Mar 2025. URL: https://doi.org/10.1186/s12887-025-05590-z, doi:10.1186/s12887-025-05590-z. This article has 1 citations and is from a peer-reviewed journal.

16. (shahin2025theroleof pages 5-5): Asadi Shahin, Zare Arezo, and Koohestani Sima. The role of genetic mutations in the hpgd &amp; slco2a1 genes in pachydermoperiostosis syndrome. Journal of Genetic Medicine and Gene Therapy, 8:001-005, May 2025. URL: https://doi.org/10.29328/journal.jgmgt.1001013, doi:10.29328/journal.jgmgt.1001013. This article has 0 citations.

17. (xu2021monoallelicmutationsin pages 2-3): Yang Xu, Zeng Zhang, Hua Yue, Shanshan Li, and Zhenlin Zhang. Monoallelic mutations in slco2a1 cause autosomal dominant primary hypertrophic osteoarthropathy. Journal of Bone and Mineral Research, 36:1459-1468, Apr 2021. URL: https://doi.org/10.1002/jbmr.4310, doi:10.1002/jbmr.4310. This article has 39 citations and is from a highest quality peer-reviewed journal.