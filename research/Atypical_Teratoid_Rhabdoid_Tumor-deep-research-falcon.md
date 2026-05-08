---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T07:31:47.382172'
end_time: '2026-05-08T07:42:05.099940'
duration_seconds: 617.72
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Atypical Teratoid/Rhabdoid Tumor
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 49
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Atypical Teratoid/Rhabdoid Tumor
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Atypical Teratoid/Rhabdoid Tumor** covering all of the
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
- **Disease Name:** Atypical Teratoid/Rhabdoid Tumor
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Atypical Teratoid/Rhabdoid Tumor** covering all of the
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


# Disease Characteristics Research Report: Atypical Teratoid/Rhabdoid Tumor (ATRT)

## Target Disease
- **Disease name:** Atypical teratoid/rhabdoid tumor (ATRT; also written AT/RT) (tran2023currentadvancesin pages 1-2, reddy2020efficacyofhighdose pages 1-2)
- **Category:** Rare pediatric embryonal central nervous system (CNS) malignancy; SWI/SNF-deficient tumor defined by SMARCB1 or (rarely) SMARCA4 inactivation (holdhof2021atypicalteratoidrhabdoidtumors pages 1-2, smith2025atypicalteratoidrhabdoid pages 4-7)
- **MONDO ID / ICD / Orphanet / MeSH / OMIM:** Not retrieved in the current tool evidence set; mapping should be completed from dedicated ontology resources (e.g., Orphanet/MeSH/MONDO) outside of the retrieved papers/trials (no citable context in this run).

## 1. Disease Information

### Overview / current understanding
ATRT is a rare, highly aggressive embryonal tumor of the CNS that predominantly affects infants and very young children. A 2023 review summarizes: “Atypical teratoid rhabdoid tumors (ATRT) are rare and aggressive embryonal tumors of central nervous system that typically affect children younger than 3 years of age.” (Tran 2023-01, Neuro-Oncology Practice; https://doi.org/10.1093/nop/npad005) (tran2023currentadvancesin pages 1-2).

ATRT is now understood as a molecularly defined, epigenetically driven tumor entity with marked subgroup heterogeneity despite relatively low recurrent mutational burden beyond SWI/SNF genes (SMARCB1/SMARCA4). The tumor is genetically “defined by alterations in the SWI/SNF chromatin remodeling complex members SMARCB1 or SMARCA4” (Paassen 2023-04, Oncogene; https://doi.org/10.1038/s41388-023-02681-y) (reddy2020efficacyofhighdose pages 1-2).

### Synonyms / alternative names
- Atypical teratoid/rhabdoid tumor; AT/RT; ATRT (tran2023currentadvancesin pages 1-2, reddy2020efficacyofhighdose pages 1-2)
- Extracranial counterpart: malignant rhabdoid tumor (MRT) (holdhof2021atypicalteratoidrhabdoidtumors pages 1-2)
- Predisposition context: rhabdoid tumor predisposition syndrome (RTPS) (childress2025thecurrentlandscape pages 7-8, tomita2025histogenesisofatypical pages 14-15)

### Evidence type note
Most information here is aggregated from cooperative-group clinical trials, multicenter molecular cohorts, and contemporary reviews (reddy2020efficacyofhighdose pages 1-2, tran2023currentadvancesin pages 1-2, holdhof2021atypicalteratoidrhabdoidtumors pages 1-2). Case reports exist but are not the basis for the core disease definition in this report.

## 2. Etiology

### Primary causal factors (genetic/mechanistic)
**Core genetic cause:** biallelic inactivation of SWI/SNF chromatin-remodeling genes.
- SMARCB1 loss is the dominant lesion; SMARCA4 loss is rare. A 2021 Acta Neuropathologica study states: “The underlying genetic cause are inactivating bi-allelic mutations in SMARCB1 or (rarely) in SMARCA4.” (Holdhof 2021-12; https://doi.org/10.1007/s00401-020-02250-7) (holdhof2021atypicalteratoidrhabdoidtumors pages 1-2).
- A 2024 review reiterates: “The only characteristic, recurrent genetic aberration of AT/RTs is biallelic inactivation of SMARCB1 (or SMARCA4).” (Huhtala 2024-09, Neuro-Oncology Advances; https://doi.org/10.1093/noajnl/vdae162) (huhtala2024developmentandepigenetic pages 1-2).

**Epigenetic dysregulation as an etiologic driver:** ATRT biology is dominated by epigenetic and chromatin consequences of SWI/SNF disruption. In ATRT, “aberrant DNA methylation–driven epigenetic regulation…maintains the malignant, low differentiation cell state” (Pekkarinen 2024-03, Life Science Alliance; https://doi.org/10.26508/lsa.202302088) (huhtala2024developmentandepigenetic pages 1-2).

### Risk factors
- **Age:** infancy/early childhood is the main demographic risk factor. ATRT comprises ~1–2% of childhood CNS tumors but is enriched in children <3 years (Tran 2023-01) (tran2023currentadvancesin pages 1-2).
- **Germline predisposition (RTPS):** germline SMARCB1 or SMARCA4 alterations predispose to ATRT and other rhabdoid tumors (childress2025thecurrentlandscape pages 7-8, tomita2025histogenesisofatypical pages 14-15). A 2024 genetic-cancer paper notes: “RTPS1 confers an increased risk of developing rhabdoid tumors and is caused by germline mutations in SMARCB1… RTPS1 should be evaluated in all individuals with rhabdoid tumor…” (Blackburn 2024-08, Genes Chromosomes Cancer; https://doi.org/10.1002/gcc.23195) (childress2025thecurrentlandscape pages 7-8).

### Protective factors / gene–environment interactions
No protective factors or gene–environment interactions were identified in the retrieved evidence set; ATRT is predominantly driven by genetic/epigenetic mechanisms (huhtala2024developmentandepigenetic pages 1-2, holdhof2021atypicalteratoidrhabdoidtumors pages 1-2).

## 3. Phenotypes (clinical presentation)

### Typical presenting features (symptoms/signs)
ATRT presentation reflects rapid tumor growth, mass effect, and location-dependent neurologic deficits. A 2020 cooperative-group trial paper describes ATRT as “an aggressive, early-childhood brain tumor” (Reddy 2020-04, J Clin Oncol; https://doi.org/10.1200/JCO.19.01776) (reddy2020efficacyofhighdose pages 1-2).

The 2026 case series (not required by the user’s priority years but consistent with core phenotype) describes intracranial hypertension and seizures in lateral-ventricle ATRT (not cited here because not extracted as evidence in this run).

### Phenotype frequency / metastatic dissemination
- Metastatic disease at diagnosis is commonly reported at ~20–40% (review summary) (childress2025thecurrentlandscape pages 7-8).
- One review described M1 (tumor cells in CSF) at diagnosis around ~38% (smith2025atypicalteratoidrhabdoid pages 2-4).

### Suggested HPO terms (examples; for curation)
The following HPO mappings are suggested based on typical CNS tumor presentation; precise frequency-by-term was not available in the retrieved evidence:
- **HP:0001298** Encephalopathy / impaired consciousness (mass effect)
- **HP:0002315** Headache
- **HP:0002013** Vomiting
- **HP:0001250** Seizures
- **HP:0001263** Developmental regression (common in infant brain tumors)
- **HP:0001270** Motor delay / weakness
- **HP:0000252** Microcephaly (treatment-related; not extracted here)

(These HPO codes are suggested for structuring and should be validated against clinical series for ATRT-specific frequencies; no citable evidence in this run provides per-HPO frequencies.)

## 4. Genetic / molecular information

### Causal genes
- **SMARCB1** (INI1/BAF47/SNF5): defining tumor suppressor gene; loss is a diagnostic hallmark (smith2025atypicalteratoidrhabdoid pages 4-7, holdhof2021atypicalteratoidrhabdoidtumors pages 1-2).
- **SMARCA4** (BRG1): rare ATRT subset; molecularly distinct and often very early onset (holdhof2021atypicalteratoidrhabdoidtumors pages 1-2, tomita2025histogenesisofatypical pages 14-15).

### Pathogenic variants (general classes)
Commonly involve loss-of-function events: deletions, truncating variants, copy-number loss, and structural events.
- Structural-variant etiology in predisposition: constitutional balanced translocations disrupting SMARCB1 were reported as a rare RTPS1 cause (Blackburn 2024-08) (childress2025thecurrentlandscape pages 7-8).

### Epigenetic subgrouping
A widely accepted methylation/transcriptomic stratification includes:
- **ATRT-TYR, ATRT-SHH, ATRT-MYC** (SMARCB1-mutant majority) (tran2023currentadvancesin pages 1-2, holdhof2021atypicalteratoidrhabdoidtumors pages 1-2)
- **ATRT-SMARCA4** as a distinct methylation-defined group (holdhof2021atypicalteratoidrhabdoidtumors pages 1-2, johann2023recurrentatypicalteratoidrhabdoid pages 1-2)

Clinical correlates include distinct age and anatomic predilections (Tran 2023-01; Holdhof 2021-12) (tran2023currentadvancesin pages 1-2, holdhof2021atypicalteratoidrhabdoidtumors pages 1-2).

### Suggested GO terms (mechanistically relevant)
Based on SWI/SNF and epigenetic-differentiation blockade (conceptual mapping; validate in GO):
- **GO:0016585** chromatin remodeling
- **GO:0006355** regulation of transcription, DNA-templated
- **GO:0045893** positive regulation of transcription, DNA-templated (developmental programs suppressed)
- **GO:0045165** cell fate commitment / differentiation processes (blocked) (huhtala2024developmentandepigenetic pages 1-2)

## 5. Environmental information
No environmental, lifestyle, or infectious causal factors were identified in the retrieved evidence set; ATRT is primarily a genetically and epigenetically driven pediatric cancer (huhtala2024developmentandepigenetic pages 1-2, holdhof2021atypicalteratoidrhabdoidtumors pages 1-2).

## 6. Mechanism / pathophysiology

### Core mechanism: SWI/SNF loss → epigenetic dysregulation → differentiation blockade → aggressive embryonal tumor
- ATRT’s recurrent genetic lesion is SWI/SNF disruption: “biallelic inactivation of SMARCB1 (or SMARCA4)” (Huhtala 2024-09) (huhtala2024developmentandepigenetic pages 1-2).
- A 2024 study links ATRT malignancy to hypermethylation and PRC2-associated repression, concluding: “These results highlight and characterize the role of DNA hypermethylation in AT/RT malignancy and halted neural cell differentiation.” (Pekkarinen 2024-03) (huhtala2024developmentandepigenetic pages 1-2).

### Recurrence biology (2023)
A matched primary–recurrence cohort found progression-associated but relatively subtle molecular changes. Key reported recurrence-associated copy-number alterations included chromosome 1q gains and chromosome 10 losses, enriched in recurrences compared with primaries (Johann 2023-07, Acta Neuropathologica; https://doi.org/10.1007/s00401-023-02608-7) (johann2023recurrentatypicalteratoidrhabdoid pages 1-2).

### Preclinical models and subgroup-specific vulnerabilities (2023)
A 2023 organoid/tumoroid model paper reported subgroup-specific vulnerabilities: “High throughput drug screens…revealed distinct drug sensitivities… Whereas ATRT-MYC universally displayed high sensitivity to multi-targeted tyrosine kinase inhibitors, ATRT-SHH showed a more heterogeneous response with a subset showing high sensitivity to NOTCH inhibitors…” (Paassen 2023-04) (reddy2020efficacyofhighdose pages 1-2). This supports subgroup-aware treatment development.

### Immune microenvironment (2023 review)
ATRT immune profiles differ by subgroup; ATRT-MYC is described as having higher CD8+ tumor-infiltrating lymphocytes and possible immunogenic potential (Tran 2023-01) (tran2023currentadvancesin pages 1-2).

### Suggested Cell Ontology (CL) terms (conceptual)
No single-cell dataset was retrieved in this run; however, based on immune infiltration discussions:
- **CL:0000623** CD8-positive, alpha-beta T cell (ATRT-MYC enriched) (tran2023currentadvancesin pages 1-2)
- **CL:0000540** neuron / **CL:0000127** astrocyte lineage cells (developmental programs implicated) (huhtala2024developmentandepigenetic pages 1-2)

## 7. Anatomical structures affected

### Organ/tissue level
ATRT arises throughout the neuraxis, including supratentorial, infratentorial, pineal, and spinal compartments. A 50-patient cohort reported: 36% infratentorial, 30% supratentorial, 22% pineal region, and 12% spinal (Tomita 2025-12, Cancers; https://doi.org/10.3390/cancers18010008) (tomita2025histogenesisofatypical pages 1-2).

### Suggested UBERON terms (examples)
- **UBERON:0000955** brain
- **UBERON:0002037** cerebellum (posterior fossa/infratentorial)
- **UBERON:0001954** spinal cord
- **UBERON:0002421** pineal gland / pineal region

(UBERON IDs are suggested for structuring; the retrieved evidence supports the anatomic compartments but does not provide ontology IDs.)

## 8. Temporal development (onset/progression)

### Onset
Typical onset is pediatric, commonly <3 years; ATRT is described as most common malignant brain tumor manifesting in infancy (Johann 2023-07) (johann2023recurrentatypicalteratoidrhabdoid pages 1-2) and “typically affect[s] children younger than 3 years of age” (Tran 2023-01) (tran2023currentadvancesin pages 1-2).

### Progression
ATRT is characterized by rapid progression and high recurrence risk. In ACNS0333, “91% of relapses occurred by 2 years from enrollment” (Reddy 2020-04) (reddy2020efficacyofhighdose pages 1-2).

## 9. Inheritance and population

### Epidemiology
- Incidence estimate cited in Germany: 1.4 per million (Holdhof 2021-12) (holdhof2021atypicalteratoidrhabdoidtumors pages 1-2).
- Proportion of pediatric CNS tumors: ~1–2% overall, but much higher among very young children (Tran 2023-01) (tran2023currentadvancesin pages 1-2).

### Inheritance (predisposition)
RTPS is inherited via germline pathogenic variants in SMARCB1 (RTPS1) or SMARCA4 (RTPS2) and confers risk for multiple rhabdoid tumors (Blackburn 2024-08; Geethadevi 2024-09) (childress2025thecurrentlandscape pages 7-8, reddy2020efficacyofhighdose media 822317c7). Structural variants such as constitutional balanced translocations can be an RTPS1 cause and may be missed without SV analysis (Blackburn 2024-08) (childress2025thecurrentlandscape pages 7-8).

## 10. Diagnostics

### Histopathology and immunohistochemistry
A key routine diagnostic principle is nuclear loss of INI1 and/or BRG1:
- “INI-1 (SMARCB1) and BRG-1 (SMARCA4) are routine surrogates — ‘As all nucleated cells should express INI-1 and BRG-1,’ and loss of nuclear expression of either should prompt AT/RT diagnosis.” (Smith 2025-11, Cancers; https://doi.org/10.3390/cancers17233768) (smith2025atypicalteratoidrhabdoid pages 4-7).

### Molecular diagnostics
- DNA methylation profiling is central for classification/subgrouping and is used for methylation-based CNS tumor classification (Johann 2023-07; Holdhof 2021-12) (johann2023recurrentatypicalteratoidrhabdoid pages 1-2, holdhof2021atypicalteratoidrhabdoidtumors pages 1-2).
- NGS should detect SMARCB1/SMARCA4 variants; SMARCB1 copy-number loss (22q11.2) can be assessed by CN plots or FISH (Smith 2025-11) (smith2025atypicalteratoidrhabdoid pages 4-7).

### Imaging
MRI features include restricted diffusion, cystic/necrotic change, and hemorrhage; CT lesions can be hyperdense with calcifications (Smith 2025-11) (smith2025atypicalteratoidrhabdoid pages 2-4).

### Differential diagnosis
Not fully extracted in this run; however, diagnostic challenge is recognized and motivates multimodal diagnostic integration (smith2025atypicalteratoidrhabdoid pages 4-7).

## 11. Outcome / prognosis

### Survival statistics (key data)
**Children’s Oncology Group ACNS0333 (prospective cooperative-group trial):**
- “Four-year EFS and overall survival for the entire cohort were 37%… and 43%…” (Reddy 2020-04) (reddy2020efficacyofhighdose pages 1-2).
- Regimen significantly reduced EFS events in patients <36 months vs historical cohort (hazard rate 0.43; P<.0005) (Reddy 2020-04) (reddy2020efficacyofhighdose pages 1-2).

**Clinical prognostic factors** (from reviews): metastatic disease at diagnosis is common (~20–40%) and often adverse; extent of resection and radiotherapy are variably associated with better outcomes (Childress 2025-06) (childress2025thecurrentlandscape pages 7-8).

## 12. Treatment

### Standard-of-care backbone (current real-world implementation)
ATRT is treated with intensive multimodal therapy including maximal safe surgical resection, multiagent chemotherapy, radiotherapy (often focal; CSI for select metastatic cases/age contexts), and high-dose chemotherapy with autologous stem cell rescue in many protocols.

**ACNS0333 protocol (widely used backbone):**
- Induction chemotherapy, consolidation with high-dose chemotherapy and PBSC rescue, plus involved-field radiation; reported 4-year OS 43% (Reddy 2020-04) (reddy2020efficacyofhighdose pages 1-2).
- Visual evidence from the ACNS0333 paper locates regimen schema (Figure 1) and survival curves/table with the 4-year EFS/OS (Figures/Table) (reddy2020efficacyofhighdose media 8fddb41f, reddy2020efficacyofhighdose media 822317c7, reddy2020efficacyofhighdose media 8125c790).

**Suggested MAXO terms (examples; validate):**
- Surgical tumor resection (MAXO: surgical excision)
- Antineoplastic chemotherapy (multiagent chemotherapy; high-dose chemotherapy)
- Radiotherapy (involved-field radiotherapy; craniospinal irradiation)
- Autologous hematopoietic stem cell transplantation / stem cell rescue

### Targeted/epigenetic and immunotherapy developments (2023–2024 emphasis)
**Immunotherapy landscape:** A 2023 review highlights immunotherapy as a response to poor outcomes and toxicity: “there is an urgent need for more novel approaches to treat ATRT, one such approach being immunotherapy.” (Tran 2023-01) (tran2023currentadvancesin pages 1-2).

**EZH2 inhibition (tazemetostat) and combinations:**
- **NCT02601937** (Phase 1; COMPLETED; results first posted 2024-10-03): pediatric tazemetostat in relapsed/refractory INI1-negative tumors including ATRT; ATRT expansion cohort regimen reported as 1200 mg/m^2 BID continuous 28-day cycles (ClinicalTrials.gov; https://clinicaltrials.gov/study/NCT02601937) (NCT02601937 chunk 1, NCT02601937 chunk 2).
- **NCT05407441** (Phase I/II; ACTIVE_NOT_RECRUITING; start 2023-08-10): tazemetostat + nivolumab + ipilimumab for INI1-negative/SMARCA4-deficient tumors including ATRT (ClinicalTrials.gov; https://clinicaltrials.gov/study/NCT05407441) (NCT05407441 chunk 1).
- **NCT03838042** (Phase I/II; RECRUITING): nivolumab + entinostat in biomarker-defined cohorts including ATRT-MYC (ClinicalTrials.gov; https://clinicaltrials.gov/study/NCT03838042) (NCT03838042 chunk 1).

**HDAC inhibition (panobinostat):**
- **NCT04897880** (Phase 2; TERMINATED due to drug supply): panobinostat in pediatric solid tumors including MRT/ATRT (ClinicalTrials.gov; https://clinicaltrials.gov/study/NCT04897880) (NCT04897880 chunk 1).

## 13. Prevention

### Primary prevention
No established primary prevention is known for sporadic ATRT, given its early-life onset and tumor-suppressor loss mechanism.

### Genetic counseling / surveillance (secondary/tertiary prevention in RTPS)
RTPS is a key context where prevention-oriented strategies are discussed. A 2024 review states: “Patients with rhabdoid tumor predisposition syndrome (RTPS) harbor germline alterations in… SMARCB1 or SMARCA4.” and proposes “maintenance or secondary prevention” approaches to reduce recurrence or additional tumors (Geethadevi 2024-09, Neuro-Oncology Advances; https://doi.org/10.1093/noajnl/vdae158) (reddy2020efficacyofhighdose media 822317c7).

## 14. Other species / natural disease
No naturally occurring ATRT analogs in non-human species were identified in the retrieved evidence set.

## 15. Model organisms / model systems

### In vitro / organoid models (recent)
A 2023 study established ATRT “tumoroid models” from ATRT-MYC and ATRT-SHH that retained subgroup epigenetic/transcriptomic profiles and enabled high-throughput drug screening, revealing subgroup-specific sensitivities (Paassen 2023-04) (reddy2020efficacyofhighdose pages 1-2). This is a concrete real-world implementation of preclinical modeling for therapeutic discovery.

## Expert synthesis (authoritative analysis)

1. **Definition has shifted from histology-first to molecularly anchored diagnosis.** Contemporary ATRT practice relies on INI1/BRG1 immunohistochemistry and DNA methylation profiling to confirm SWI/SNF deficiency and assign molecular subgroup, as emphasized by diagnostic evolution reviews (smith2025atypicalteratoidrhabdoid pages 4-7, johann2023recurrentatypicalteratoidrhabdoid pages 1-2).
2. **Outcomes improved with intensive multimodal regimens but remain poor, especially after relapse.** ACNS0333 demonstrates improved survival compared with historical cohorts but still yields ~43% 4-year OS, with most relapses within 2 years (reddy2020efficacyofhighdose pages 1-2).
3. **Subgroup heterogeneity is not academic; it is translational.** Evidence of subgroup-specific immune features (ATRT-MYC CD8+ infiltration) and subgroup-specific drug vulnerabilities in tumoroids suggests rational stratified trials and combination approaches (tran2023currentadvancesin pages 1-2, reddy2020efficacyofhighdose pages 1-2).
4. **RTPS is a critical clinical-management axis.** Germline SMARCB1/SMARCA4 alterations, including rare structural variants, support systematic germline testing and consideration of surveillance/maintenance strategies (childress2025thecurrentlandscape pages 7-8, reddy2020efficacyofhighdose media 822317c7).

## Summary table
The following table consolidates core definitions, subgroups, diagnostics, treatments, outcomes, and 2023–2024 developments:

| Topic | Key details | Evidence / source |
|---|---|---|
| Definition / classification | Atypical teratoid/rhabdoid tumor (ATRT; also AT/RT) is a rare, highly aggressive embryonal CNS tumor, predominantly of infancy/early childhood; WHO-classified as an embryonal CNS neoplasm. It accounts for ~1–2% of pediatric CNS tumors overall, but ~20% of CNS tumors in children <3 years; median age at diagnosis ~16–30 months. ATRT is now understood as a molecularly heterogeneous SWI/SNF-deficient tumor family rather than a single homogeneous entity. | Tran 2023, *Neuro-Oncology Practice*, Jan 2023, https://doi.org/10.1093/nop/npad005; Tomita 2025, *Cancers*, Dec 2025, https://doi.org/10.3390/cancers18010008 (tran2023currentadvancesin pages 1-2, tomita2025histogenesisofatypical pages 2-4) |
| Hallmark genes / protein surrogates | Defining event: biallelic loss/inactivation of **SMARCB1** in ~95% of cases; rare **SMARCA4**-mutant cases (~0.5–2%, some series up to ~4%). Routine diagnostic protein surrogates are loss of nuclear **INI1/BAF47** for SMARCB1-deficient tumors and loss of **BRG1** for SMARCA4-deficient tumors; all nucleated cells should normally express both. Germline pathogenic variants underlie rhabdoid tumor predisposition syndrome (RTPS1: SMARCB1; RTPS2: SMARCA4). | Holdhof 2021, *Acta Neuropathologica*, Dec 2021, https://doi.org/10.1007/s00401-020-02250-7; Smith 2025, *Cancers*, Nov 2025, https://doi.org/10.3390/cancers17233768; Blackburn 2024, *Genes Chromosomes Cancer*, Aug 2024, https://doi.org/10.1002/gcc.23195 (holdhof2021atypicalteratoidrhabdoidtumors pages 1-2, smith2025atypicalteratoidrhabdoid pages 4-7, childress2025thecurrentlandscape pages 7-8) |
| Molecular subgroup: ATRT-TYR | TYR subgroup: tends to occur in the youngest patients (often 0–1 year), commonly infratentorial, with overexpression of melanocytic / melanosomal genes (**TYR, TYRP1, MITF, OTX2**). Imaging/pathology correlations include more peripheral cysts and stronger contrast enhancement than SHH in some series. | Tran 2023, https://doi.org/10.1093/nop/npad005; Smith 2025, https://doi.org/10.3390/cancers17233768 (tran2023currentadvancesin pages 1-2, smith2025atypicalteratoidrhabdoid pages 2-4) |
| Molecular subgroup: ATRT-SHH | SHH subgroup: mixed supra- and infratentorial distribution overall; enriched for SHH/NOTCH-related programs and genes such as **GLI2, BOC, PTCHD2, MYCN**. Some subclass analyses show SHH-1A/1B predominantly supratentorial, while SHH-2 is largely infratentorial/pineal and enriched for germline SMARCB1 variants. Dissemination may be relatively more frequent in SHH-associated disease in some cohorts. | Tran 2023, https://doi.org/10.1093/nop/npad005; Tomita 2025, https://doi.org/10.3390/cancers18010008; Smith 2025, https://doi.org/10.3390/cancers17233768 (tran2023currentadvancesin pages 1-2, tomita2025histogenesisofatypical pages 14-15, smith2025atypicalteratoidrhabdoid pages 2-4) |
| Molecular subgroup: ATRT-MYC | MYC subgroup: often supratentorial; overexpresses **MYC** and HOX-related programs; a subset arises extra-axially, including along cranial nerves. Compared with other subgroups, ATRT-MYC has been reported to show higher **CD8+ tumor-infiltrating lymphocytes**, supporting relative immunogenicity. | Tran 2023, https://doi.org/10.1093/nop/npad005; Smith 2025, https://doi.org/10.3390/cancers17233768 (tran2023currentadvancesin pages 1-2, smith2025atypicalteratoidrhabdoid pages 2-4) |
| Molecular subgroup: ATRT-SMARCA4 | Rare, molecularly distinct subgroup defined by **SMARCA4** loss rather than SMARCB1 loss; retains INI1 expression but loses BRG1. Associated with very young age, frequent germline events, and inferior prognosis versus SMARCB1-deficient ATRT. DNA methylation and RNA-seq support separation from TYR/SHH/MYC and from other SMARCA4-deficient tumors. | Holdhof 2021, https://doi.org/10.1007/s00401-020-02250-7; Tomita 2025, https://doi.org/10.3390/cancers18010008 (holdhof2021atypicalteratoidrhabdoidtumors pages 1-2, tomita2025histogenesisofatypical pages 14-15) |
| Typical anatomy / presentation | ATRT can arise anywhere along the neuraxis. In one 50-patient pediatric cohort: **36% infratentorial, 30% supratentorial, 22% pineal region, 12% spinal**. Posterior fossa is common, often off-midline. Presentation often reflects rapid growth and intracranial hypertension; MRI may show restricted diffusion, cystic/necrotic change, hemorrhage, and CSF dissemination. Metastatic disease is present in ~20–40% at diagnosis; one review cited M1 CSF positivity around **38%**. | Tomita 2025, https://doi.org/10.3390/cancers18010008; Childress 2025, https://doi.org/10.3390/jmp6020013; Smith 2025, https://doi.org/10.3390/cancers17233768; Hoffman 2020, https://doi.org/10.1093/neuonc/noaa046 (tomita2025histogenesisofatypical pages 1-2, childress2025thecurrentlandscape pages 7-8, smith2025atypicalteratoidrhabdoid pages 2-4, hoffman2020advancingbiologybased pages 4-5) |
| Diagnostic modalities | Modern diagnosis integrates histology + IHC + molecular testing. Core methods: (1) histopathology showing rhabdoid morphology with variable epithelial/mesenchymal/neuroectodermal elements; (2) IHC for **INI1/SMARCB1** and **BRG1/SMARCA4** loss; (3) genome-wide **DNA methylation profiling**, now considered highly informative / WHO-essential in difficult cases for subgroup assignment; (4) sequencing / CNV analysis for **SMARCB1** or **SMARCA4** alterations; (5) FISH / copy-number methods for 22q11.2 SMARCB1 loss when needed. | Smith 2025, https://doi.org/10.3390/cancers17233768; Holdhof 2021, https://doi.org/10.1007/s00401-020-02250-7; Childress 2025, https://doi.org/10.3390/jmp6020013 (smith2025atypicalteratoidrhabdoid pages 4-7, holdhof2021atypicalteratoidrhabdoidtumors pages 1-2, childress2025thecurrentlandscape pages 10-12) |
| Standard therapy backbone (ACNS0333) | Contemporary backbone is aggressive multimodal therapy: maximal safe resection, intensive induction chemotherapy, focal/involved-field radiotherapy, then high-dose chemotherapy with autologous stem-cell rescue. **ACNS0333** schema: 2 induction cycles including vincristine, methotrexate, etoposide, cyclophosphamide, cisplatin; then 3 consolidation cycles with **thiotepa + carboplatin** and PBSC rescue; focal RT timing adapted by age/disease status. Gross total resection is achieved in ~30–68% across series. | Reddy 2020, *JCO*, Apr 2020, https://doi.org/10.1200/JCO.19.01776; figure/table locations summarized from ACNS0333 visual review (reddy2020efficacyofhighdose pages 1-2, reddy2020efficacyofhighdose media 8fddb41f, childress2025thecurrentlandscape pages 7-8) |
| Key outcome statistics | **ACNS0333** (65 evaluable patients): 4-year **EFS 37%** (95% CI 25–49) and 4-year **OS 43%** (95% CI 31–55); for patients <36 months, EFS hazard ratio vs historical cohort **0.43** (P<.0005). **91% of relapses occurred within 2 years**; treatment-related deaths: 4. Other cited multimodal results: Dana-Farber regimen 2-year EFS/OS **53%/70%**; Head Start HDCT/ASCR 3-year EFS/OS **21%/26%**. | Reddy 2020, https://doi.org/10.1200/JCO.19.01776; Childress 2025, https://doi.org/10.3390/jmp6020013 (reddy2020efficacyofhighdose pages 1-2, childress2025thecurrentlandscape pages 7-8) |
| Representative mechanistic findings (2023–2024) | **Recurrence biology:** recurrent ATRTs show increased mitotic activity, occasional subgroup switching, and enrichment of **chromosome 1q gain** and **chromosome 10 loss**; primary and relapse usually remain close by methylation/transcriptome, implying relative epigenetic stability with selected progression-associated changes. **Epigenetic differentiation blockade:** AT/RT-specific DNA hypermethylation is linked to **PRC2**, suppression of neural differentiation genes, impaired NEUROG/NEUROD pioneer-factor activity, and maintenance of a low-differentiation malignant state. **Model systems / vulnerabilities:** 2023 tumoroid models retained subgroup-specific epigenetic states; ATRT-MYC showed broad sensitivity to multi-targeted tyrosine kinase inhibitors, while a subset of ATRT-SHH was sensitive to **NOTCH inhibitors**. | Johann 2023, *Acta Neuropathologica*, Jul 2023, https://doi.org/10.1007/s00401-023-02608-7; Pekkarinen 2024, *Life Science Alliance*, Mar 2024, https://doi.org/10.26508/lsa.202302088; Paassen 2023, *Oncogene*, Apr 2023, https://doi.org/10.1038/s41388-023-02681-y; Huhtala 2024, *Neuro-Oncology Advances*, Sep 2024, https://doi.org/10.1093/noajnl/vdae162 (johann2023recurrentatypicalteratoidrhabdoid pages 1-2, huhtala2024developmentandepigenetic pages 1-2, reddy2020efficacyofhighdose pages 1-2) |
| Immune microenvironment / translational rationale | ATRT is epigenetically driven but immunologically nonuniform across subgroups; ATRT-MYC has relatively higher CD8+ infiltration, motivating immune-based strategies. Reviews emphasize combining immune profiling with subgrouping and epigenetic therapy to refine treatment selection. | Tran 2023, https://doi.org/10.1093/nop/npad005; Childress 2025, https://doi.org/10.3390/jmp6020013 (tran2023currentadvancesin pages 1-2, childress2025thecurrentlandscape pages 10-12) |
| Representative clinical trials | **NCT02601937** — tazemetostat (EZH2 inhibitor), Phase 1, completed, pediatric relapsed/refractory INI1-negative tumors including ATRT; results posted 2024-10-03; ATRT cohort used **1200 mg/m² BID** continuous 28-day cycles. **NCT05407441** — tazemetostat + nivolumab + ipilimumab, Phase I/II, Active not recruiting, ATRT / INI1-negative / SMARCA4-deficient tumors. **NCT04416568** — nivolumab + ipilimumab in INI1-negative cancers, Phase 2, Active not recruiting. **NCT04897880** — panobinostat in pediatric solid tumors including MRT/ATRT, Phase 2, Terminated (drug supply). **NCT03838042** — INFORM2 Nivolumab + entinostat, Phase I/II, Recruiting; includes biomarker-defined cohorts including **ATRT-MYC**. | ClinicalTrials.gov records summarized from extracted trial evidence (NCT02601937, NCT05407441, NCT04416568, NCT04897880, NCT03838042) (NCT04897880 chunk 1, NCT02601937 chunk 2, NCT05407441 chunk 1, NCT02601937 chunk 1, NCT03838042 chunk 1) |


*Table: This table condenses the most clinically and biologically relevant facts about ATRT, including defining molecular features, subgroup correlates, diagnostics, standard therapy, outcomes, and representative recent research and trials. It is designed as a compact reference for knowledge-base curation or rapid expert review.*

## Key URLs (retrieved sources)
- ACNS0333 trial publication (JCO; 2020-04): https://doi.org/10.1200/JCO.19.01776 (reddy2020efficacyofhighdose pages 1-2)
- Immunotherapy review (Neuro-Oncology Practice; 2023-01): https://doi.org/10.1093/nop/npad005 (tran2023currentadvancesin pages 1-2)
- Recurrence biology (Acta Neuropathologica; 2023-07): https://doi.org/10.1007/s00401-023-02608-7 (johann2023recurrentatypicalteratoidrhabdoid pages 1-2)
- ATRT tumoroids (Oncogene; 2023-04): https://doi.org/10.1038/s41388-023-02681-y (reddy2020efficacyofhighdose pages 1-2)
- DNA methylation differentiation blockade (Life Science Alliance; 2024-03): https://doi.org/10.26508/lsa.202302088 (huhtala2024developmentandepigenetic pages 1-2)
- RTPS balanced translocations (Genes Chromosomes Cancer; 2024-08): https://doi.org/10.1002/gcc.23195 (childress2025thecurrentlandscape pages 7-8)
- RTPS prevention/maintenance review (Neuro-Oncology Advances; 2024-09): https://doi.org/10.1093/noajnl/vdae158 (reddy2020efficacyofhighdose media 822317c7)
- ClinicalTrials.gov tazemetostat pediatric INI1-negative tumors (NCT02601937; results posted 2024-10-03): https://clinicaltrials.gov/study/NCT02601937 (NCT02601937 chunk 1)
- ClinicalTrials.gov tazemetostat + nivo/ipi (NCT05407441; started 2023-08-10): https://clinicaltrials.gov/study/NCT05407441 (NCT05407441 chunk 1)
- ClinicalTrials.gov nivolumab + entinostat INFORM2 (NCT03838042): https://clinicaltrials.gov/study/NCT03838042 (NCT03838042 chunk 1)
- ClinicalTrials.gov panobinostat (NCT04897880; terminated): https://clinicaltrials.gov/study/NCT04897880 (NCT04897880 chunk 1)


References

1. (tran2023currentadvancesin pages 1-2): Son Tran, Ashley S Plant-Fox, Susan N Chi, and Aru Narendran. Current advances in immunotherapy for atypical teratoid rhabdoid tumor (atrt). Neuro-oncology practice, 10 4:322-334, Jan 2023. URL: https://doi.org/10.1093/nop/npad005, doi:10.1093/nop/npad005. This article has 21 citations and is from a peer-reviewed journal.

2. (reddy2020efficacyofhighdose pages 1-2): Alyssa T. Reddy, Douglas R. Strother, Alexander R. Judkins, Peter C. Burger, Ian F. Pollack, Mark D. Krailo, Allen B. Buxton, Chris Williams-Hughes, Maryam Fouladi, Anita Mahajan, Thomas E. Merchant, Ben Ho, Claire M. Mazewski, Victor A. Lewis, Amar Gajjar, Louis-Gilbert Vezina, Timothy N. Booth, Kerry W. Parsons, Vicky L. Poss, Tianni Zhou, Jaclyn A. Biegel, and Annie Huang. Efficacy of high-dose chemotherapy and three-dimensional conformal radiation for atypical teratoid/rhabdoid tumor: a report from the children’s oncology group trial acns0333. Journal of Clinical Oncology, 38:1175-1185, Apr 2020. URL: https://doi.org/10.1200/jco.19.01776, doi:10.1200/jco.19.01776. This article has 238 citations and is from a highest quality peer-reviewed journal.

3. (holdhof2021atypicalteratoidrhabdoidtumors pages 1-2): Dörthe Holdhof, Pascal D. Johann, Michael Spohn, Michael Bockmayr, Sepehr Safaei, Piyush Joshi, Julien Masliah-Planchon, Ben Ho, Mamy Andrianteranagna, Franck Bourdeaut, Annie Huang, Marcel Kool, Santhosh A. Upadhyaya, Anne E. Bendel, Daniela Indenbirken, William D. Foulkes, Jonathan W. Bush, David Creytens, Uwe Kordes, Michael C. Frühwald, Martin Hasselblatt, and Ulrich Schüller. Atypical teratoid/rhabdoid tumors (atrts) with smarca4 mutation are molecularly distinct from smarcb1-deficient cases. Acta Neuropathologica, 141:291-301, Dec 2021. URL: https://doi.org/10.1007/s00401-020-02250-7, doi:10.1007/s00401-020-02250-7. This article has 110 citations and is from a highest quality peer-reviewed journal.

4. (smith2025atypicalteratoidrhabdoid pages 4-7): Heather L. Smith, Pascale Aouad, and Nitin R. Wadhwani. Atypical teratoid rhabdoid tumor: how tumor diagnostic methods in the laboratory have evolved over the past 40 years. Cancers, 17:3768, Nov 2025. URL: https://doi.org/10.3390/cancers17233768, doi:10.3390/cancers17233768. This article has 1 citations.

5. (childress2025thecurrentlandscape pages 7-8): Ashley Childress, Alayna Koch, Emma Vallee, Alyssa Steller, and Scott Raskin. The current landscape of molecular pathology for the diagnosis and treatment of atypical teratoid rhabdoid tumor. Journal of Molecular Pathology, 6:13, Jun 2025. URL: https://doi.org/10.3390/jmp6020013, doi:10.3390/jmp6020013. This article has 0 citations.

6. (tomita2025histogenesisofatypical pages 14-15): Tadanori Tomita. Histogenesis of atypical teratoid rhabdoid tumors: anatomical and embryological perspectives. Cancers, 18:8, Dec 2025. URL: https://doi.org/10.3390/cancers18010008, doi:10.3390/cancers18010008. This article has 0 citations.

7. (huhtala2024developmentandepigenetic pages 1-2): Laura Huhtala, Goktug Karabiyik, and Kirsi J Rautajoki. Development and epigenetic regulation of atypical teratoid/rhabdoid tumors in the context of cell-of-origin and halted cell differentiation. Neuro-Oncology Advances, Sep 2024. URL: https://doi.org/10.1093/noajnl/vdae162, doi:10.1093/noajnl/vdae162. This article has 9 citations and is from a peer-reviewed journal.

8. (smith2025atypicalteratoidrhabdoid pages 2-4): Heather L. Smith, Pascale Aouad, and Nitin R. Wadhwani. Atypical teratoid rhabdoid tumor: how tumor diagnostic methods in the laboratory have evolved over the past 40 years. Cancers, 17:3768, Nov 2025. URL: https://doi.org/10.3390/cancers17233768, doi:10.3390/cancers17233768. This article has 1 citations.

9. (johann2023recurrentatypicalteratoidrhabdoid pages 1-2): Pascal D. Johann, Lea Altendorf, Emma-Maria Efremova, Till Holsten, Mona Steinbügl, Karolina Nemes, Alicia Eckhardt, Catena Kresbach, Michael Bockmayr, Arend Koch, Christine Haberler, Manila Antonelli, John DeSisto, Martin U. Schuhmann, Peter Hauser, Reiner Siebert, Susanne Bens, Marcel Kool, Adam L. Green, Martin Hasselblatt, Michael C. Frühwald, and Ulrich Schüller. Recurrent atypical teratoid/rhabdoid tumors (at/rt) reveal discrete features of progression on histology, epigenetics, copy number profiling, and transcriptomics. Acta Neuropathologica, 146:527-541, Jul 2023. URL: https://doi.org/10.1007/s00401-023-02608-7, doi:10.1007/s00401-023-02608-7. This article has 20 citations and is from a highest quality peer-reviewed journal.

10. (tomita2025histogenesisofatypical pages 1-2): Tadanori Tomita. Histogenesis of atypical teratoid rhabdoid tumors: anatomical and embryological perspectives. Cancers, 18:8, Dec 2025. URL: https://doi.org/10.3390/cancers18010008, doi:10.3390/cancers18010008. This article has 0 citations.

11. (reddy2020efficacyofhighdose media 822317c7): Alyssa T. Reddy, Douglas R. Strother, Alexander R. Judkins, Peter C. Burger, Ian F. Pollack, Mark D. Krailo, Allen B. Buxton, Chris Williams-Hughes, Maryam Fouladi, Anita Mahajan, Thomas E. Merchant, Ben Ho, Claire M. Mazewski, Victor A. Lewis, Amar Gajjar, Louis-Gilbert Vezina, Timothy N. Booth, Kerry W. Parsons, Vicky L. Poss, Tianni Zhou, Jaclyn A. Biegel, and Annie Huang. Efficacy of high-dose chemotherapy and three-dimensional conformal radiation for atypical teratoid/rhabdoid tumor: a report from the children’s oncology group trial acns0333. Journal of Clinical Oncology, 38:1175-1185, Apr 2020. URL: https://doi.org/10.1200/jco.19.01776, doi:10.1200/jco.19.01776. This article has 238 citations and is from a highest quality peer-reviewed journal.

12. (reddy2020efficacyofhighdose media 8fddb41f): Alyssa T. Reddy, Douglas R. Strother, Alexander R. Judkins, Peter C. Burger, Ian F. Pollack, Mark D. Krailo, Allen B. Buxton, Chris Williams-Hughes, Maryam Fouladi, Anita Mahajan, Thomas E. Merchant, Ben Ho, Claire M. Mazewski, Victor A. Lewis, Amar Gajjar, Louis-Gilbert Vezina, Timothy N. Booth, Kerry W. Parsons, Vicky L. Poss, Tianni Zhou, Jaclyn A. Biegel, and Annie Huang. Efficacy of high-dose chemotherapy and three-dimensional conformal radiation for atypical teratoid/rhabdoid tumor: a report from the children’s oncology group trial acns0333. Journal of Clinical Oncology, 38:1175-1185, Apr 2020. URL: https://doi.org/10.1200/jco.19.01776, doi:10.1200/jco.19.01776. This article has 238 citations and is from a highest quality peer-reviewed journal.

13. (reddy2020efficacyofhighdose media 8125c790): Alyssa T. Reddy, Douglas R. Strother, Alexander R. Judkins, Peter C. Burger, Ian F. Pollack, Mark D. Krailo, Allen B. Buxton, Chris Williams-Hughes, Maryam Fouladi, Anita Mahajan, Thomas E. Merchant, Ben Ho, Claire M. Mazewski, Victor A. Lewis, Amar Gajjar, Louis-Gilbert Vezina, Timothy N. Booth, Kerry W. Parsons, Vicky L. Poss, Tianni Zhou, Jaclyn A. Biegel, and Annie Huang. Efficacy of high-dose chemotherapy and three-dimensional conformal radiation for atypical teratoid/rhabdoid tumor: a report from the children’s oncology group trial acns0333. Journal of Clinical Oncology, 38:1175-1185, Apr 2020. URL: https://doi.org/10.1200/jco.19.01776, doi:10.1200/jco.19.01776. This article has 238 citations and is from a highest quality peer-reviewed journal.

14. (NCT02601937 chunk 1):  EZH2 Inhibitor Tazemetostat in Pediatric Subjects With Relapsed or Refractory INI1-Negative Tumors or Synovial Sarcoma. Epizyme, Inc.. 2016. ClinicalTrials.gov Identifier: NCT02601937

15. (NCT02601937 chunk 2):  EZH2 Inhibitor Tazemetostat in Pediatric Subjects With Relapsed or Refractory INI1-Negative Tumors or Synovial Sarcoma. Epizyme, Inc.. 2016. ClinicalTrials.gov Identifier: NCT02601937

16. (NCT05407441 chunk 1): Susan Chi, MD. Tazemetostat+Nivo/Ipi in INI1-Neg/SMARCA4-Def Tumors. Susan Chi, MD. 2023. ClinicalTrials.gov Identifier: NCT05407441

17. (NCT03838042 chunk 1): Olaf Witt, MD. INFORM2 Study Uses Nivolumab and Entinostat in Children and Adolescents With High-risk Refractory Malignancies. University Hospital Heidelberg. 2020. ClinicalTrials.gov Identifier: NCT03838042

18. (NCT04897880 chunk 1):  A Study of Panobinostat in Pediatric Patients With Solid Tumors Including MRT/ATRT. Australian & New Zealand Children's Haematology/Oncology Group. 2019. ClinicalTrials.gov Identifier: NCT04897880

19. (tomita2025histogenesisofatypical pages 2-4): Tadanori Tomita. Histogenesis of atypical teratoid rhabdoid tumors: anatomical and embryological perspectives. Cancers, 18:8, Dec 2025. URL: https://doi.org/10.3390/cancers18010008, doi:10.3390/cancers18010008. This article has 0 citations.

20. (hoffman2020advancingbiologybased pages 4-5): Lindsey M Hoffman, Elizabeth Anne Richardson, Ben Ho, Ashley Margol, Alyssa Reddy, Lucie Lafay-Cousin, Susan Chi, Irene Slavc, Alexander Judkins, Martin Hasselblatt, Franck Bourdeaut, Michael C Frühwald, Rajeev Vibhakar, Eric Bouffet, and Annie Huang. Advancing biology based therapeutic approaches for atypical teratoid rhabdoid tumors. Neuro-oncology, 22:944-954, Mar 2020. URL: https://doi.org/10.1093/neuonc/noaa046, doi:10.1093/neuonc/noaa046. This article has 39 citations and is from a domain leading peer-reviewed journal.

21. (childress2025thecurrentlandscape pages 10-12): Ashley Childress, Alayna Koch, Emma Vallee, Alyssa Steller, and Scott Raskin. The current landscape of molecular pathology for the diagnosis and treatment of atypical teratoid rhabdoid tumor. Journal of Molecular Pathology, 6:13, Jun 2025. URL: https://doi.org/10.3390/jmp6020013, doi:10.3390/jmp6020013. This article has 0 citations.
