---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T11:03:04.549962'
end_time: '2026-05-08T11:25:50.219834'
duration_seconds: 1365.67
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cervical Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cervical Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Cervical Cancer** covering all of the
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
- **Disease Name:** Cervical Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Cervical Cancer** covering all of the
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


# Cervical Cancer — Disease Characteristics Research Report (Evidence-focused)

## Target Disease
- **Disease name:** Cervical cancer
- **Category:** Malignant neoplasm of cervix uteri
- **MONDO ID:** Not identified in the retrieved sources for this run (insufficient evidence in-tool).

**Scope note (evidence limitation):** This report prioritizes 2023–2024 peer‑reviewed sources retrieved via the toolchain. Standard identifiers (ICD‑10/ICD‑11, MeSH, MONDO) and detailed symptom-frequency tables were not found in the retrieved texts; they are therefore not asserted as sourced facts here.

| Domain | Key finding (with numbers) | Source (author, journal, year) | URL/DOI |
|---|---|---|---|
| Epidemiology | GLOBOCAN 2022 estimated **661,021 new cervical cancer cases** and **348,189 deaths** worldwide; cervical cancer accounted for **3.3% of new cancers** and **3.6% of cancer deaths** globally in 2022. (bray2024globalcancerstatistics pages 5-6) | Bray et al., *CA: A Cancer Journal for Clinicians*, 2024 | https://doi.org/10.3322/caac.21834 |
| Epidemiology | Cervical cancer burden remains disproportionately concentrated in lower-resource settings; one 2024 review summarizes about **660,000 cases** and **350,000 deaths** in 2022, with **~90% of deaths in low-resource settings**. (goldstein2024thefutureof pages 1-2) | Goldstein et al., *International Journal of Women's Health*, 2024 | https://doi.org/10.2147/IJWH.S474571 |
| Etiology | Cervical cancer is strongly linked to persistent **high-risk HPV** infection; **>95% of cases** are attributable to HPV, and **HPV16/18 account for ~71%** of global cases. (goldstein2024thefutureof pages 1-2) | Goldstein et al., *International Journal of Women's Health*, 2024 | https://doi.org/10.2147/IJWH.S474571 |
| Etiology | A major clinical guideline states cervical cancer is strongly associated with high-risk HPV and that oncogenic **HPV16/18 are detected in ~99% of cervical tumors** in the guideline’s cited framing. (manso2024seomgeicoclinicalguidelines pages 1-2) | Manso et al., *Clinical & Translational Oncology*, 2024 | https://doi.org/10.1007/s12094-024-03604-3 |
| Screening/Diagnostics | In the Stockholm real-world cohort (**28,017 women**, **2,377 HPV-positive**), **WID-qCIN + HPV16/18** detected **93.4% of CIN3** and **100% of invasive cervical cancers**. (schreiberhuber2024cervicalcancerscreening pages 1-2, schreiberhuber2024cervicalcancerscreening pages 2-3) | Schreiberhuber et al., *Nature Medicine*, 2024 | https://doi.org/10.1038/s41591-024-03014-6 |
| Screening/Diagnostics | In the same WID-qCIN study, **cytology** required **4.1 colposcopy referrals** to detect one CIN2+, versus **2.4 referrals** for **WID-qCIN/HPV16/18**, indicating improved triage efficiency. (schreiberhuber2024cervicalcancerscreening pages 1-2, schreiberhuber2024cervicalcancerscreening pages 4-5, schreiberhuber2024cervicalcancerscreening media 23da8e40) | Schreiberhuber et al., *Nature Medicine*, 2024 | https://doi.org/10.1038/s41591-024-03014-6 |
| Imaging/Staging | ESGO/ESTRO/ESP 2023 update recommends **transvaginal/transrectal ultrasound or pelvic MRI** for local staging; **ultrasound is a valid alternative to MRI** when performed by an expert. For early-stage **T1a-T2a1 (except T1b3)** with negative nodes on imaging, **surgicopathologic staging** is recommended. (fischerova2024theroleof pages 1-2) | Fischerova et al., *Cancers*, 2024 | https://doi.org/10.3390/cancers16040775 |
| Imaging/Staging | For locally advanced disease or suspicious nodes, the guideline recommends **contrast-enhanced CT or 18F-FDG PET/CT** to assess extrapelvic spread; imaging modalities have **high specificity** for nodal metastases but limited sensitivity for small-volume disease, so negative imaging does **not** exclude nodal metastasis. (fischerova2024theroleof pages 1-2, fischerova2024theroleof pages 26-27) | Fischerova et al., *Cancers*, 2024 | https://doi.org/10.3390/cancers16040775 |
| Treatment | In **KEYNOTE-826**, first-line pembrolizumab plus platinum-taxane chemotherapy ± bevacizumab achieved **median overall survival 26.4 vs 16.8 months** versus control. (nagdev2026advancesinscreening pages 13-15) | Nagdev & Chittilla, *Current Oncology*, 2026 | https://doi.org/10.3390/curroncol33010048 |
| Treatment | In **EMPOWER-Cervical 1**, **cemiplimab** improved **median overall survival to 12.0 vs 8.5 months** after platinum-treated recurrent/metastatic disease; review data also report **ORR 16.4% vs 6.3%**. (martinezcannon2024theevolvingrole pages 1-3, nagdev2026advancesinscreening pages 13-15) | Martinez-Cannon & Colombo, *Cancer Drug Resistance*, 2024; Nagdev & Chittilla, *Current Oncology*, 2026 | https://doi.org/10.20517/cdr.2023.120; https://doi.org/10.3390/curroncol33010048 |
| Treatment | In **innovaTV-301**, **tisotumab vedotin** improved **median OS to 11.5 vs 9.5 months** and **median PFS to 4.2 vs 2.9 months** (HR **0.67**, 95% CI 0.54-0.82; **p<0.0001**) versus chemotherapy. (nagdev2026advancesinscreening pages 13-15) | Nagdev & Chittilla, *Current Oncology*, 2026 | https://doi.org/10.3390/curroncol33010048 |
| Treatment | For recurrent/metastatic disease, current guidelines incorporate immunotherapy into practice: first-line **immunotherapy + chemotherapy with/without bevacizumab** improves OS, and second-line **immunotherapy monotherapy** is established after platinum exposure. (manso2024seomgeicoclinicalguidelines pages 1-2, sznurkowski2024thepolishsociety pages 1-2) | Manso et al., *Clinical & Translational Oncology*, 2024; Sznurkowski et al., *Journal of Clinical Medicine*, 2024 | https://doi.org/10.1007/s12094-024-03604-3; https://doi.org/10.3390/jcm13154351 |
| Implementation | In Brazil’s organized **PREVENTIVO** HPV DNA program, first-round screening covered **58.7%** of the target population (**77.8% excluding pandemic months**) with **99.4% target-age compliance**; **20,551 women** were screened. (teixeira2024transitionfromopportunistic pages 1-2, teixeira2024transitionfromopportunistic pages 2-4) | Teixeira et al., *Scientific Reports*, 2024 | https://doi.org/10.1038/s41598-024-71735-2 |
| Implementation | PREVENTIVO referred **6.2%** to colposcopy with **84.8% colposcopy completion** and detected **258 high-grade precursor lesions** plus **29 cervical cancers**; **83% were Stage I** and **62% were microinvasive FIGO IA**, versus the earlier cytology era where **67% of cancers were advanced stage**. (teixeira2024transitionfromopportunistic pages 1-2, teixeira2024transitionfromopportunistic pages 2-4, teixeira2024transitionfromopportunistic pages 5-5) | Teixeira et al., *Scientific Reports*, 2024 | https://doi.org/10.1038/s41598-024-71735-2 |
| Implementation | Compared with the prior opportunistic cytology program, organized HPV DNA screening detected cancers at a younger mean age (**41.4 vs 52.0 years**) and supported the conclusion that prevalent cervical cancers were detected **about 10 years earlier**. (teixeira2024transitionfromopportunistic pages 1-2, teixeira2024transitionfromopportunistic pages 5-6, teixeira2024transitionfromopportunistic pages 4-5) | Teixeira et al., *Scientific Reports*, 2024 | https://doi.org/10.1038/s41598-024-71735-2 |


*Table: This table compiles high-yield, recent cervical cancer findings across epidemiology, causation, diagnostics, staging, treatment, and implementation. It is designed for citation-ready reuse in a research report or disease knowledge base entry.*

---

## 1. Disease Information
### 1.1 Concise overview
Cervical cancer is a malignancy arising from the cervix uteri, typically preceded by detectable precursor lesions (e.g., high-grade CIN) and strongly driven by persistent infection with oncogenic (“high-risk”) human papillomavirus (HPV). Reviews emphasize that the disease is largely preventable through HPV vaccination and effective screening programs. (goldstein2024thefutureof pages 1-2, manso2024seomgeicoclinicalguidelines pages 1-2)

### 1.2 Common synonyms / alternative names (not exhaustive)
Common clinical labels include: “cancer of the cervix,” “cervical carcinoma,” “cervix uteri cancer.” These synonyms were not enumerated in the retrieved sources and are provided as standard clinical terminology (unsourced in-tool).

### 1.3 Evidence provenance
The information presented here is derived from **aggregated disease-level resources and peer‑reviewed studies/guidelines** (GLOBOCAN analyses, international guidelines, and population-based implementation studies), rather than individual patient EHR extracts. (bray2024globalcancerstatistics pages 5-6, teixeira2024transitionfromopportunistic pages 1-2, fischerova2024theroleof pages 1-2, manso2024seomgeicoclinicalguidelines pages 1-2)

---

## 2. Etiology
### 2.1 Primary causal factors
**Persistent high-risk HPV infection** is the dominant causal factor in cervical cancer.
- A 2024 screening-technology review states that **“over 95% of cervical cancer cases are attributable to HPV”** and that **HPV‑16/18 account for ~71% of global cases**. (goldstein2024thefutureof pages 1-2)
- Mechanistically, reviews describe HPV oncogenesis via viral oncoproteins **E6/E7**, including inactivation of tumor suppressors **p53 and Rb**, and note the role of HPV genome integration during progression. (nagdev2026advancesinscreening pages 2-4)

### 2.2 Risk factors and co-factors (evidence available in retrieved sources)
The retrieved evidence emphasizes population-level and biologic drivers rather than a comprehensive quantified list of co-factors.
- **Multi-type HPV infection** is described as clinically relevant; one review reports co-infection prevalence ranges **~18.5–46% among HPV-positive women** (context: HPV infection epidemiology and screening triage). (goldstein2024thefutureof pages 1-2)
- Broader prevention context: the GLOBOCAN 2022 analysis describes HPV as a “necessary (but not sufficient)” cause and highlights elimination-strategy targets and screening ages (35 and 45), implying programmatic focus on preventing persistent infection and progression. (bray2024globalcancerstatistics pages 26-26)

### 2.3 Protective factors
Evidence in retrieved sources supports:
- **HPV vaccination and screening** as key protective interventions; high-income countries with HPV vaccination and screening have experienced “dramatic reductions” in incidence in guideline summaries. (manso2024seomgeicoclinicalguidelines pages 1-2)

### 2.4 Gene–environment interactions
Specific gene–environment interaction findings were not identified in the retrieved sources for this run.

---

## 3. Phenotypes (clinical presentation)
The retrieved sources for this run focus primarily on screening, staging, imaging, and systemic therapy rather than symptom prevalence. As a result:
- **Comprehensive phenotype lists, frequencies, and quality-of-life impacts with primary citations** could not be extracted.
- **HPO term suggestions** are therefore not provided as evidence-backed entries in this run.

---

## 4. Genetic / Molecular Information
### 4.1 Key molecular concepts (HPV-driven carcinogenesis)
Recent reviews reiterate HPV-driven transformation mechanisms and host genomic/epigenetic alterations:
- HPV E6/E7 perturbation of **p53/Rb** is highlighted as a core axis for malignant transformation. (nagdev2026advancesinscreening pages 2-4)
- Reviews summarize that somatic alterations (including **PIK3CA** mutations and APOBEC signatures) are recurrent in cervical cancer, providing a rationale for targeted therapy exploration and biomarker-guided approaches. (nagdev2026advancesinscreening pages 2-4)

### 4.2 Epigenetics and methylation biomarkers (2024 primary research)
A major 2024 real-world screening study evaluated DNA methylation triage:
- **WID-qCIN** assay measures methylation of **DPP6, RALYL, GSX1** in HPV-positive screening samples. (schreiberhuber2024cervicalcancerscreening pages 1-2, schreiberhuber2024cervicalcancerscreening pages 2-3)
- In **28,017 screened women** (Stockholm; ≥30 years; 2,377 HPV-positive), **WID-qCIN + HPV16/18** detected **93.4% of CIN3** and **100% of invasive cervical cancers**. (schreiberhuber2024cervicalcancerscreening pages 1-2, schreiberhuber2024cervicalcancerscreening pages 2-3)

---

## 5. Environmental Information
The retrieved sources emphasize infectious etiology and screening-system factors rather than detailed chemical/toxin exposures. Infectious agent:
- **High-risk HPV** is the principal infectious driver. (goldstein2024thefutureof pages 1-2, manso2024seomgeicoclinicalguidelines pages 1-2)

---

## 6. Mechanism / Pathophysiology
### 6.1 Causal chain (high-level)
1. **High-risk HPV infection** of cervical epithelium; persistent infection over years is a prerequisite for progression. (goldstein2024thefutureof pages 1-2, nagdev2026advancesinscreening pages 2-4)
2. Viral genome integration and expression of **E6/E7** oncoproteins drives dysregulated cell-cycle control (p53/Rb pathway interference) and supports malignant transformation. (nagdev2026advancesinscreening pages 2-4)
3. Accumulation of host genomic/epigenetic alterations and tumor microenvironment remodeling contributes to invasion and metastasis, motivating biomarker-driven and immunotherapy approaches. (nagdev2026advancesinscreening pages 2-4)

### 6.2 Immune system involvement and implications
Immune checkpoint blockade has become clinically important in advanced disease, indicating that immune evasion and immune contexture are therapeutically actionable in a subset of patients. (martinezcannon2024theevolvingrole pages 1-3, manso2024seomgeicoclinicalguidelines pages 1-2)

---

## 7. Anatomical Structures Affected
**Primary site:** cervix uteri. (Implied throughout cervical-cancer-focused guidelines and imaging papers; explicit ontology mapping not retrieved.) (fischerova2024theroleof pages 1-2)

**Staging spread assessed by imaging:** parametrial extension; invasion of bladder/rectal wall; pelvic and paraaortic nodal metastases; distant metastases (lung, liver, bone, peritoneum). (fischerova2024theroleof pages 7-8, fischerova2024theroleof pages 26-27, fischerova2024theroleof pages 6-7)

---

## 8. Temporal Development
The retrieved sources describe long preclinical windows enabling prevention:
- Screening and prevention frameworks emphasize that effective programs can detect precancers and early cancers and shift stage distribution toward earlier disease. A Brazilian organized HPV DNA screening program reported earlier-stage detection (majority Stage I) compared with prior cytology-era advanced-stage predominance. (teixeira2024transitionfromopportunistic pages 1-2)

---

## 9. Inheritance and Population
### 9.1 Epidemiology (recent authoritative statistics)
**Global burden (GLOBOCAN 2022; published 2024):**
- **661,021 new cases** and **348,189 deaths** worldwide in 2022 (Table 1, cervix uteri). (bray2024globalcancerstatistics pages 5-6)

**Disparities by development level (rates):**
- GLOBOCAN 2022 analysis reports higher incidence and mortality in “transitioning” vs “transitioned” countries (incidence **19.3 vs 12.1 per 100,000**; mortality **12.4 vs 4.8 per 100,000**). (bray2024globalcancerstatistics pages 26-26)

### 9.2 Sex ratio
Cervical cancer occurs in individuals with a cervix; sex ratio data were not extracted from retrieved sources in this run.

---

## 10. Diagnostics
### 10.1 Screening tests and triage (recent advances)
**HPV-based screening (systems and implementation):**
- A 2024 review highlights emerging approaches including **rapid/low-cost HPV testing**, digital colposcopy with **AI interpretation**, **DNA methylation assays**, and **dual-stain cytology**. (goldstein2024thefutureof pages 1-2)

**Real-world methylation triage (Nature Medicine 2024):**
- In HPV-positive samples, **WID-qCIN/HPV16/18** improved triage efficiency: cytology triage would require **4.1 colposcopy referrals per CIN2+** vs **2.4 referrals per CIN2+** for WID-qCIN/HPV16/18 over follow-up. (schreiberhuber2024cervicalcancerscreening pages 1-2, schreiberhuber2024cervicalcancerscreening pages 4-5)
- Visual evidence: Table summarizing colposcopy referral efficiency and detection performance is available from the paper. (schreiberhuber2024cervicalcancerscreening media 23da8e40)

### 10.2 Imaging and staging (ESGO/ESTRO/ESP update 2023; published 2024)
Modern guidelines incorporate imaging into staging and treatment planning:
- **Transvaginal/transrectal ultrasound or pelvic MRI** is recommended for local staging; ultrasound can be a valid alternative to MRI in expert hands. (fischerova2024theroleof pages 1-2)
- For early-stage tumors (T1a–T2a1 excluding T1b3) with negative nodes on ultrasound/MRI, **surgicopathological staging** is recommended because imaging has limited sensitivity for small-volume nodal disease. (fischerova2024theroleof pages 1-2)
- For locally advanced disease or suspicious nodes, **contrast-enhanced CT or FDG PET/CT** is recommended for extrapelvic spread assessment; the guideline emphasizes high specificity but limited sensitivity for micrometastases across modalities. (fischerova2024theroleof pages 26-27)

---

## 11. Outcome / Prognosis
The retrieved evidence base in this run emphasizes stage shift through screening and survival improvements in advanced disease trials.

### 11.1 Screening-associated stage shift (population implementation)
In the PREVENTIVO organized HPV DNA screening program in Brazil:
- 29 cancers were detected with **83% Stage I**; in the prior opportunistic cytology period, **67% were advanced stage**. (teixeira2024transitionfromopportunistic pages 1-2)

### 11.2 Advanced/recurrent metastatic disease outcomes (selected trial outcomes as summarized in authoritative reviews)
- **KEYNOTE-826 (pembrolizumab + platinum-taxane ± bevacizumab, first line):** median OS **26.4 vs 16.8 months** (review table extraction). (nagdev2026advancesinscreening pages 13-15)
- **EMPOWER-Cervical 1 (cemiplimab vs chemotherapy after platinum):** median OS **12.0 vs 8.5 months**; ORR **16.4% vs 6.3%** reported in a 2024 ICI review. (martinezcannon2024theevolvingrole pages 1-3)
- **innovaTV-301 (tisotumab vedotin vs chemotherapy):** median OS **11.5 vs 9.5 months** and median PFS **4.2 vs 2.9 months** (HR 0.67; p<0.0001) as summarized in a comprehensive review table. (nagdev2026advancesinscreening pages 13-15)

---

## 12. Treatment
### 12.1 Guideline-based treatment framework (2024 European/Spanish and national guidance)
- **Early-stage disease:** managed primarily with surgery or radiotherapy; fertility-sparing approaches are used in selected low-risk early disease. (manso2024seomgeicoclinicalguidelines pages 1-2, manso2024seomgeicoclinicalguidelines pages 4-5)
- **Locally advanced disease:** standard backbone is **concurrent chemoradiotherapy (CCRT/CRT) followed by brachytherapy**. (sznurkowski2024thepolishsociety pages 1-2, manso2024seomgeicoclinicalguidelines pages 1-2)

### 12.2 Systemic therapy and immunotherapy integration
- The SEOM-GEICO guideline notes that immunotherapy has significantly improved OS in recurrent/metastatic disease when added to chemotherapy (± bevacizumab) in first line and as monotherapy after platinum in second line. (manso2024seomgeicoclinicalguidelines pages 1-2)
- The Polish PSGO guideline (v2024.0) describes PD‑L1 testing to select pembrolizumab candidates and references immunotherapy incorporation for higher-risk locally advanced disease (pembrolizumab with CCRT and maintenance). (sznurkowski2024thepolishsociety pages 1-2)

### 12.3 Targeted therapy / ADC
- Reviews highlight **tisotumab vedotin** (tissue factor–directed ADC) as a preferred later-line option in recurrent/metastatic disease, with characteristic toxicities including ocular events. (nagdev2026advancesinscreening pages 13-15)

### 12.4 MAXO (Medical Action Ontology) suggestions (non-exhaustive; ontology IDs not retrieved)
- HPV vaccination; cervical cancer screening; HPV DNA testing; colposcopy; conization; hysterectomy; radiotherapy; brachytherapy; concurrent chemoradiotherapy; immune checkpoint inhibitor therapy; antibody–drug conjugate therapy.

---

## 13. Prevention
### 13.1 Primary prevention
- **HPV vaccination** is emphasized across guidelines/reviews as central to prevention and elimination efforts. (goldstein2024thefutureof pages 1-2, manso2024seomgeicoclinicalguidelines pages 1-2)

### 13.2 Secondary prevention (screening)
- HPV-based screening and effective triage are central; a major 2024 review highlights self-sampling, AI-assisted colposcopy, methylation, and other approaches to improve detection and risk stratification. (goldstein2024thefutureof pages 1-2)
- GLOBOCAN-related discussion references elimination-strategy screening targets at ages **35 and 45** and emphasizes improving participation (including self-sampling). (bray2024globalcancerstatistics pages 26-26)

### 13.3 Real-world implementation example (organized screening)
- Brazil’s PREVENTIVO program shows feasibility of switching from opportunistic cytology to organized HPV DNA testing, with coverage **58.7%** (or **77.8% excluding pandemic months**) and improved early-stage detection. (teixeira2024transitionfromopportunistic pages 1-2, teixeira2024transitionfromopportunistic pages 2-4)

---

## 14. Other Species / Natural Disease
Not addressed in the retrieved sources for this run.

---

## 15. Model Organisms
Model-organism and experimental-system details (e.g., HPV transgenic mice, organoids) were not captured in the retrieved sources excerpted in this run; therefore, evidence-backed model summaries are not provided.

---

# Key 2023–2024 Developments Highlighted by the Retrieved Evidence
1. **Updated global burden quantification (2024 publication of GLOBOCAN 2022 statistics)** with explicit 2022 cervical cancer incidence/mortality counts. (bray2024globalcancerstatistics pages 5-6)
2. **Real-world validation of DNA methylation triage** (WID-qCIN) demonstrating high CIN3 and invasive-cancer detection and improved colposcopy efficiency vs cytology triage (Nature Medicine 2024). (schreiberhuber2024cervicalcancerscreening pages 1-2, schreiberhuber2024cervicalcancerscreening media 23da8e40)
3. **Health-system implementation evidence for organized HPV DNA screening** showing improved coverage, diagnostic follow-through, and earlier-stage cancer detection (Scientific Reports 2024). (teixeira2024transitionfromopportunistic pages 1-2)
4. **Imaging/staging guidance (ESGO/ESTRO/ESP update 2023; published 2024)** reinforcing ultrasound/MRI for local staging and PET/CT/CT for extrapelvic assessment, with explicit discussion of sensitivity limits for micrometastases. (fischerova2024theroleof pages 1-2, fischerova2024theroleof pages 26-27)
5. **Therapy landscape consolidation in guidelines and reviews**: integration of immune checkpoint blockade (pembrolizumab; cemiplimab) and ADCs (tisotumab vedotin) into recurrent/metastatic management frameworks. (manso2024seomgeicoclinicalguidelines pages 1-2, martinezcannon2024theevolvingrole pages 1-3, nagdev2026advancesinscreening pages 13-15)

# URLs and publication dates (where available in retrieved sources)
- Bray et al. “Global cancer statistics 2022…” *CA Cancer J Clin* **Apr 2024**. https://doi.org/10.3322/caac.21834 (bray2024globalcancerstatistics pages 5-6)
- Schreiberhuber et al. “Cervical cancer screening using DNA methylation triage…” *Nature Medicine* **Jun 2024**. https://doi.org/10.1038/s41591-024-03014-6 (schreiberhuber2024cervicalcancerscreening pages 1-2)
- Teixeira et al. “Transition… organized screening… DNA-HPV testing…” *Scientific Reports* **Sep 2024**. https://doi.org/10.1038/s41598-024-71735-2 (teixeira2024transitionfromopportunistic pages 1-2)
- Fischerova et al. “The Role of Imaging in Cervical Cancer Staging: ESGO/ESTRO/ESP Guidelines (Update 2023)” *Cancers* **Feb 2024**. https://doi.org/10.3390/cancers16040775 (fischerova2024theroleof pages 1-2)
- Manso et al. “SEOM-GEICO Clinical Guidelines on cervical cancer (2023)” *Clin Transl Oncol* **Aug 2024**. https://doi.org/10.1007/s12094-024-03604-3 (manso2024seomgeicoclinicalguidelines pages 1-2)
- Goldstein et al. “The Future of Cervical Cancer Screening” *Int J Women’s Health* **Oct 2024**. https://doi.org/10.2147/IJWH.S474571 (goldstein2024thefutureof pages 1-2)


References

1. (bray2024globalcancerstatistics pages 5-6): Freddie Bray, Mathieu Laversanne, Hyuna Sung, Jacques Ferlay, Rebecca L. Siegel, Isabelle Soerjomataram, and Ahmedin Jemal. Global cancer statistics 2022: globocan estimates of incidence and mortality worldwide for 36 cancers in 185 countries. CA: A Cancer Journal for Clinicians, 74:229-263, Apr 2024. URL: https://doi.org/10.3322/caac.21834, doi:10.3322/caac.21834. This article has 35815 citations and is from a domain leading peer-reviewed journal.

2. (goldstein2024thefutureof pages 1-2): Amelia R Goldstein, Mallory Gersh, Gabriela Skovronsky, and Chailee Moss. The future of cervical cancer screening. International Journal of Women's Health, 16:1715-1731, Oct 2024. URL: https://doi.org/10.2147/ijwh.s474571, doi:10.2147/ijwh.s474571. This article has 43 citations and is from a peer-reviewed journal.

3. (manso2024seomgeicoclinicalguidelines pages 1-2): Luis Manso, Avinash Ramchandani-Vaswani, Ignacio Romero, Luisa Sánchez-Lorenzo, María José Bermejo-Pérez, Purificación Estévez-García, Lorena Fariña-Madrid, Yolanda García García, Marta Gil-Martin, and María Quindós. Seom-geico clinical guidelines on cervical cancer (2023). Clinical & Translational Oncology, 26:2771-2782, Aug 2024. URL: https://doi.org/10.1007/s12094-024-03604-3, doi:10.1007/s12094-024-03604-3. This article has 19 citations and is from a peer-reviewed journal.

4. (schreiberhuber2024cervicalcancerscreening pages 1-2): Lena Schreiberhuber, James E. Barrett, Jiangrong Wang, Elisa Redl, Chiara Herzog, Charlotte D. Vavourakis, Karin Sundström, Joakim Dillner, and Martin Widschwendter. Cervical cancer screening using dna methylation triage in a real-world population. Nature Medicine, 30:2251-2257, Jun 2024. URL: https://doi.org/10.1038/s41591-024-03014-6, doi:10.1038/s41591-024-03014-6. This article has 85 citations and is from a highest quality peer-reviewed journal.

5. (schreiberhuber2024cervicalcancerscreening pages 2-3): Lena Schreiberhuber, James E. Barrett, Jiangrong Wang, Elisa Redl, Chiara Herzog, Charlotte D. Vavourakis, Karin Sundström, Joakim Dillner, and Martin Widschwendter. Cervical cancer screening using dna methylation triage in a real-world population. Nature Medicine, 30:2251-2257, Jun 2024. URL: https://doi.org/10.1038/s41591-024-03014-6, doi:10.1038/s41591-024-03014-6. This article has 85 citations and is from a highest quality peer-reviewed journal.

6. (schreiberhuber2024cervicalcancerscreening pages 4-5): Lena Schreiberhuber, James E. Barrett, Jiangrong Wang, Elisa Redl, Chiara Herzog, Charlotte D. Vavourakis, Karin Sundström, Joakim Dillner, and Martin Widschwendter. Cervical cancer screening using dna methylation triage in a real-world population. Nature Medicine, 30:2251-2257, Jun 2024. URL: https://doi.org/10.1038/s41591-024-03014-6, doi:10.1038/s41591-024-03014-6. This article has 85 citations and is from a highest quality peer-reviewed journal.

7. (schreiberhuber2024cervicalcancerscreening media 23da8e40): Lena Schreiberhuber, James E. Barrett, Jiangrong Wang, Elisa Redl, Chiara Herzog, Charlotte D. Vavourakis, Karin Sundström, Joakim Dillner, and Martin Widschwendter. Cervical cancer screening using dna methylation triage in a real-world population. Nature Medicine, 30:2251-2257, Jun 2024. URL: https://doi.org/10.1038/s41591-024-03014-6, doi:10.1038/s41591-024-03014-6. This article has 85 citations and is from a highest quality peer-reviewed journal.

8. (fischerova2024theroleof pages 1-2): Daniela Fischerova, Filip Frühauf, Andrea Burgetova, Ingfrid S. Haldorsen, Elena Gatti, and David Cibula. The role of imaging in cervical cancer staging: esgo/estro/esp guidelines (update 2023). Cancers, 16:775, Feb 2024. URL: https://doi.org/10.3390/cancers16040775, doi:10.3390/cancers16040775. This article has 50 citations.

9. (fischerova2024theroleof pages 26-27): Daniela Fischerova, Filip Frühauf, Andrea Burgetova, Ingfrid S. Haldorsen, Elena Gatti, and David Cibula. The role of imaging in cervical cancer staging: esgo/estro/esp guidelines (update 2023). Cancers, 16:775, Feb 2024. URL: https://doi.org/10.3390/cancers16040775, doi:10.3390/cancers16040775. This article has 50 citations.

10. (nagdev2026advancesinscreening pages 13-15): Priyanka Nagdev and Mythri Chittilla. Advances in screening, immunotherapy, targeted agents, and precision surgery in cervical cancer: a comprehensive clinical review (2018–2025). Current Oncology, Jan 2026. URL: https://doi.org/10.3390/curroncol33010048, doi:10.3390/curroncol33010048. This article has 1 citations.

11. (martinezcannon2024theevolvingrole pages 1-3): Bertha Alejandra Martinez-Cannon and Ilaria Colombo. The evolving role of immune checkpoint inhibitors in cervical and endometrial cancer. Cancer Drug Resistance, Jun 2024. URL: https://doi.org/10.20517/cdr.2023.120, doi:10.20517/cdr.2023.120. This article has 18 citations.

12. (sznurkowski2024thepolishsociety pages 1-2): Jacek J. Sznurkowski, Lubomir Bodnar, Łukasz Szylberg, Agnieszka Zołciak-Siwinska, Anna Dańska-Bidzińska, Dagmara Klasa-Mazurkiewicz, Agnieszka Rychlik, Artur Kowalik, Joanna Streb, Mariusz Bidziński, and Włodzimierz Sawicki. The polish society of gynecological oncology guidelines for the diagnosis and treatment of cervical cancer (v2024.0). Journal of Clinical Medicine, 13:4351, Jul 2024. URL: https://doi.org/10.3390/jcm13154351, doi:10.3390/jcm13154351. This article has 10 citations.

13. (teixeira2024transitionfromopportunistic pages 1-2): Julio Cesar Teixeira, Diama Bhadra Vale, Cirbia Silva Campos, Ilana Polegatto, Joana Froes Bragança, Michelle Garcia Discacciati, and Luiz Carlos Zeferino. Transition from opportunistic cytological to organized screening program with dna-hpv testing detected prevalent cervical cancers 10 years in advance. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-71735-2, doi:10.1038/s41598-024-71735-2. This article has 22 citations and is from a peer-reviewed journal.

14. (teixeira2024transitionfromopportunistic pages 2-4): Julio Cesar Teixeira, Diama Bhadra Vale, Cirbia Silva Campos, Ilana Polegatto, Joana Froes Bragança, Michelle Garcia Discacciati, and Luiz Carlos Zeferino. Transition from opportunistic cytological to organized screening program with dna-hpv testing detected prevalent cervical cancers 10 years in advance. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-71735-2, doi:10.1038/s41598-024-71735-2. This article has 22 citations and is from a peer-reviewed journal.

15. (teixeira2024transitionfromopportunistic pages 5-5): Julio Cesar Teixeira, Diama Bhadra Vale, Cirbia Silva Campos, Ilana Polegatto, Joana Froes Bragança, Michelle Garcia Discacciati, and Luiz Carlos Zeferino. Transition from opportunistic cytological to organized screening program with dna-hpv testing detected prevalent cervical cancers 10 years in advance. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-71735-2, doi:10.1038/s41598-024-71735-2. This article has 22 citations and is from a peer-reviewed journal.

16. (teixeira2024transitionfromopportunistic pages 5-6): Julio Cesar Teixeira, Diama Bhadra Vale, Cirbia Silva Campos, Ilana Polegatto, Joana Froes Bragança, Michelle Garcia Discacciati, and Luiz Carlos Zeferino. Transition from opportunistic cytological to organized screening program with dna-hpv testing detected prevalent cervical cancers 10 years in advance. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-71735-2, doi:10.1038/s41598-024-71735-2. This article has 22 citations and is from a peer-reviewed journal.

17. (teixeira2024transitionfromopportunistic pages 4-5): Julio Cesar Teixeira, Diama Bhadra Vale, Cirbia Silva Campos, Ilana Polegatto, Joana Froes Bragança, Michelle Garcia Discacciati, and Luiz Carlos Zeferino. Transition from opportunistic cytological to organized screening program with dna-hpv testing detected prevalent cervical cancers 10 years in advance. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-71735-2, doi:10.1038/s41598-024-71735-2. This article has 22 citations and is from a peer-reviewed journal.

18. (nagdev2026advancesinscreening pages 2-4): Priyanka Nagdev and Mythri Chittilla. Advances in screening, immunotherapy, targeted agents, and precision surgery in cervical cancer: a comprehensive clinical review (2018–2025). Current Oncology, Jan 2026. URL: https://doi.org/10.3390/curroncol33010048, doi:10.3390/curroncol33010048. This article has 1 citations.

19. (bray2024globalcancerstatistics pages 26-26): Freddie Bray, Mathieu Laversanne, Hyuna Sung, Jacques Ferlay, Rebecca L. Siegel, Isabelle Soerjomataram, and Ahmedin Jemal. Global cancer statistics 2022: globocan estimates of incidence and mortality worldwide for 36 cancers in 185 countries. CA: A Cancer Journal for Clinicians, 74:229-263, Apr 2024. URL: https://doi.org/10.3322/caac.21834, doi:10.3322/caac.21834. This article has 35815 citations and is from a domain leading peer-reviewed journal.

20. (fischerova2024theroleof pages 7-8): Daniela Fischerova, Filip Frühauf, Andrea Burgetova, Ingfrid S. Haldorsen, Elena Gatti, and David Cibula. The role of imaging in cervical cancer staging: esgo/estro/esp guidelines (update 2023). Cancers, 16:775, Feb 2024. URL: https://doi.org/10.3390/cancers16040775, doi:10.3390/cancers16040775. This article has 50 citations.

21. (fischerova2024theroleof pages 6-7): Daniela Fischerova, Filip Frühauf, Andrea Burgetova, Ingfrid S. Haldorsen, Elena Gatti, and David Cibula. The role of imaging in cervical cancer staging: esgo/estro/esp guidelines (update 2023). Cancers, 16:775, Feb 2024. URL: https://doi.org/10.3390/cancers16040775, doi:10.3390/cancers16040775. This article has 50 citations.

22. (manso2024seomgeicoclinicalguidelines pages 4-5): Luis Manso, Avinash Ramchandani-Vaswani, Ignacio Romero, Luisa Sánchez-Lorenzo, María José Bermejo-Pérez, Purificación Estévez-García, Lorena Fariña-Madrid, Yolanda García García, Marta Gil-Martin, and María Quindós. Seom-geico clinical guidelines on cervical cancer (2023). Clinical & Translational Oncology, 26:2771-2782, Aug 2024. URL: https://doi.org/10.1007/s12094-024-03604-3, doi:10.1007/s12094-024-03604-3. This article has 19 citations and is from a peer-reviewed journal.
