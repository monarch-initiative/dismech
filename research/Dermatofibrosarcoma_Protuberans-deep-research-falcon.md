---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T12:26:57.999420'
end_time: '2026-05-08T12:36:20.966198'
duration_seconds: 562.97
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dermatofibrosarcoma Protuberans
  mondo_id: ''
  category: ''
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
- **Disease Name:** Dermatofibrosarcoma Protuberans
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Dermatofibrosarcoma Protuberans** covering all of the
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
- **Disease Name:** Dermatofibrosarcoma Protuberans
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Dermatofibrosarcoma Protuberans** covering all of the
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


# Dermatofibrosarcoma Protuberans (DFSP): Disease Characteristics Research Report (2026-05-08)

## Target Disease
- **Disease name:** Dermatofibrosarcoma protuberans (DFSP)
- **MONDO ID:** **MONDO:0011934** (OpenTargets disease entity) (OpenTargets Search: Dermatofibrosarcoma protuberans)
- **Category:** Rare cutaneous/dermal soft-tissue sarcoma (fionda2024theroleof pages 1-2, jozwik2024dermatofibrosarcomaprotuberansan pages 2-4)

## Executive overview (current understanding)
Dermatofibrosarcoma protuberans is a rare, locally aggressive dermal/superficial soft tissue sarcoma characterized by infiltrative growth in the dermis and subcutaneous fat, frequent local recurrence, and typically low metastatic potential (fionda2024theroleof pages 1-2, trinidad2023rarevariantsof pages 1-3, algarin2024cutaneousmalignanciesin pages 2-4). DFSP is molecularly defined in most cases by a **COL1A1::PDGFB** fusion (often arising from t(17;22)) that drives **PDGF/PDGFRβ (PDGFRB)** signaling (trinidad2023rarevariantsof pages 1-3, ono2024establishmentandcharacterization pages 1-5, NCT00122473 chunk 2).

Recent (2023–2024) synthesis papers emphasize: (i) improved fusion detection (including NGS for atypical/cryptic fusions), (ii) more precise surgery (Mohs/slow Mohs and image-guided approaches) to reduce recurrence, and (iii) continued clinical use of **imatinib** for unresectable/metastatic disease, with ongoing focus on mechanisms of resistance and alternative targeted strategies (meng2024hotspotsandfuture pages 10-12, ono2024establishmentandcharacterization pages 1-5, NCT00243191 chunk 1).

---

## 1. Disease information
### 1.1 What is the disease?
DFSP is a **superficial** sarcoma involving **dermis and subcutaneous fat** and rarely muscle/fascia (fionda2024theroleof pages 1-2). It tends to present as a **slow-growing plaque or firm nodule** that may become protuberant over time (algarin2024cutaneousmalignanciesin pages 2-4, jozwik2024dermatofibrosarcomaprotuberansan pages 2-4).

**Direct abstract quote (primary pathology review, 2023):**
- “**Dermatofibrosarcoma protuberans (DFSP) is a dermal malignant mesenchymal tumor. Most variants are associated with a high risk of local recurrence and a low risk of metastasis.**” (Trinidad et al., *Dermatopathology*, 2023-01-29; DOI: 10.3390/dermatopathology10010008; URL: https://doi.org/10.3390/dermatopathology10010008) (trinidad2023rarevariantsof pages 1-3)

### 1.2 Key identifiers
Evidence retrieved in this run supports:
- **MONDO:** MONDO:0011934 (OpenTargets Search: Dermatofibrosarcoma protuberans)
- **MeSH concept used by ClinicalTrials.gov browsing:** “Dermatofibrosarcoma” (MeSH term) (NCT00243191 chunk 1, NCT00122473 chunk 2)

Not available in the retrieved evidence set (therefore not asserted here): OMIM, Orphanet, ICD-10/ICD-11 codes, MeSH tree identifiers.

### 1.3 Synonyms and alternative names
- **Bednar tumor**: pigmented DFSP variant (fionda2024theroleof pages 1-2, felix2024dermatofibrosarcomaprotuberansthe pages 3-4)
- **Fibrosarcomatous DFSP (FS-DFSP)**: DFSP with fibrosarcomatous transformation (higher-grade behavior) (trinidad2023rarevariantsof pages 1-3, jozwik2024dermatofibrosarcomaprotuberansan pages 2-4)
- **Giant-cell fibroblastoma**: often considered a juvenile form of DFSP (jozwik2024dermatofibrosarcomaprotuberansan pages 2-4)

### 1.4 Evidence sources represented
The information in this report is derived from:
- Aggregated disease-level resources and analyses (e.g., SEER population-based registry) (kreicher2016incidenceandsurvival pages 4-6)
- Systematic reviews and narrative reviews (2023–2024 prioritized) (meng2024hotspotsandfuture pages 10-12, fionda2024theroleof pages 1-2, trinidad2023rarevariantsof pages 1-3)
- ClinicalTrials.gov trial records (interventional trials of imatinib) (NCT00243191 chunk 1, NCT00084630 chunk 1)
- Preclinical model development (patient-derived DFSP cell line) (ono2024establishmentandcharacterization pages 1-5)

---

## 2. Etiology
### 2.1 Primary causal factors (genetic/mechanistic)
The dominant etiologic driver is a tumor-specific rearrangement that places **PDGFB** under control of the **COL1A1** promoter, generating **COL1A1::PDGFB**, producing functional PDGF ligand and enabling autocrine signaling (trinidad2023rarevariantsof pages 1-3, NCT00122473 chunk 2, ono2024establishmentandcharacterization pages 1-5). This supports PDGFR pathway dependence and explains sensitivity to PDGFR inhibition in fusion-positive disease (ono2024establishmentandcharacterization pages 1-5, meng2024hotspotsandfuture pages 10-12).

**Direct abstract quote (clinical trial background citation in record):**
- “**The dermatofibrosarcoma protuberans-associated collagen type Ialpha1/platelet-derived growth factor (PDGF) B-chain fusion gene generates a transforming protein that is processed to functional PDGF-BB.**” (Shimizu et al., *Cancer Research*, 1999; cited within the ClinicalTrials.gov record) (NCT00122473 chunk 2)

### 2.2 Risk factors
High-quality, exposure-based risk factors (environmental/occupational) were not identified in the retrieved evidence set. Population patterns (sex/race/age) are addressed in Epidemiology below.

### 2.3 Protective factors / gene–environment interactions
No protective factors or gene–environment interactions were identified in the retrieved evidence set.

---

## 3. Phenotypes
### 3.1 Core clinical phenotypes and course (with suggested HPO)
- **Initial lesion:** asymptomatic, flesh-colored indurated firm nodule; progression can lead to pain/ulceration and protuberant growth (algarin2024cutaneousmalignanciesin pages 2-4).
- **Preprotuberant phase:** nonprotuberant plaques for a mean of ~7 years before nodularity in a subset (jozwik2024dermatofibrosarcomaprotuberansan pages 2-4).
- **Local recurrence:** hallmark due to infiltrative growth and margin definition difficulty; recurrence depends strongly on modality (algarin2024cutaneousmalignanciesin pages 2-4, meng2024hotspotsandfuture pages 10-12).

Suggested phenotype mappings are provided in the injected artifact below.

| Feature | Description (include age of onset/course/frequency when available) | Suggested HPO term(s) | Suggested UBERON term(s) for anatomical site | Notes | Citation (pqac IDs) |
|---|---|---|---|---|---|
| Slow-growing plaque or firm nodule | Typical presentation is a slow-growing, firm, flesh-colored to red plaque or multilobular nodule; most often diagnosed in young to middle-aged adults, especially ages 20–59 years, with peak incidence between the 2nd and 5th decades | Slow-growing cutaneous nodule; Skin plaque; HP:0001482 Nodular skin lesion; best-effort: Slow progression | UBERON:0002097 skin of trunk; UBERON:0000974 integumental system | Common first clinical manifestation; often initially asymptomatic | (fionda2024theroleof pages 1-2, jozwik2024dermatofibrosarcomaprotuberansan pages 2-4, algarin2024cutaneousmalignanciesin pages 2-4, ono2024establishmentandcharacterization pages 1-5) |
| Protuberant tumor mass | Classic DFSP presents as an indurated tumor nodule that protrudes above the skin surface; lesions may evolve from plaque-like to bulky protuberant masses over years | HP:0001482 Nodular skin lesion; best-effort: Protruding skin mass | UBERON:0001003 skin | “Protuberans” refers to the raised/exophytic morphology | (trinidad2023rarevariantsof pages 1-3, jozwik2024dermatofibrosarcomaprotuberansan pages 2-4) |
| Preprotuberant non-bulging plaque stage | Some cases remain nonprotuberant plaques for a mean of ~7 years before becoming nodular/protuberant | Skin plaque; best-effort: Insidious onset; best-effort: Delayed progression | UBERON:0001003 skin | Important source of delayed diagnosis/misdiagnosis | (jozwik2024dermatofibrosarcomaprotuberansan pages 2-4) |
| Pain and ulceration in progressive lesions | Although often asymptomatic initially, progression can lead to pain and ulceration | HP:0012531 Pain; HP:0001070 Skin ulcer | UBERON:0001003 skin | Pain is more typical of advanced/progressive lesions rather than early disease | (algarin2024cutaneousmalignanciesin pages 2-4) |
| Local recurrence | DFSP is locally aggressive and recurrence is a hallmark; reported overall recurrence ranges from 0–60% depending on treatment modality; local recurrence common after incomplete margin control, median time reported as 34 months in one review/model paper | HP:0033677 Neoplasm recurrence; best-effort: Local recurrence | UBERON:0001003 skin; UBERON:0001474 dermis; UBERON:0003568 subcutaneous tissue | Core disease-course phenotype; long-term follow-up needed | (algarin2024cutaneousmalignanciesin pages 2-4, fionda2024theroleof pages 1-2, ono2024establishmentandcharacterization pages 1-5) |
| Low metastatic potential | Distant spread is uncommon; reviews cite metastatic potential as low, often <1–5%, but risk rises with fibrosarcomatous transformation | best-effort: Rare metastasis; best-effort: Low metastatic potential | UBERON:0001003 skin | Distinguishes classic DFSP from FS-DFSP | (algarin2024cutaneousmalignanciesin pages 2-4, trinidad2023rarevariantsof pages 1-3, fionda2024theroleof pages 1-2) |
| Fibrosarcomatous transformation with worse behavior | FS-DFSP shows higher local recurrence and greater metastatic potential than classic DFSP; associated with progression and increased proliferation | best-effort: Sarcoma progression; best-effort: Increased metastatic risk | UBERON:0001474 dermis; UBERON:0003568 subcutaneous tissue | Aggressive histologic subtype; adverse prognostic factor | (trinidad2023rarevariantsof pages 1-3, jozwik2024dermatofibrosarcomaprotuberansan pages 2-4, ono2024establishmentandcharacterization pages 1-5) |
| Honeycomb subcutaneous fat infiltration | Pathology classically shows infiltration of subcutis in a diffuse “honeycomb” pattern, reflecting tentacle-like spread through fat lobules/septa | best-effort: Subcutaneous tissue infiltration | UBERON:0003568 subcutaneous tissue; UBERON:0001474 dermis | Useful diagnostic microscopic clue and reason margins are difficult to assess | (trinidad2023rarevariantsof pages 1-3, jozwik2024dermatofibrosarcomaprotuberansan pages 2-4) |
| Storiform spindle-cell neoplasm | Histology shows uniform spindle-shaped cells arranged in storiform/cartwheel pattern with low atypia and low mitotic activity in classic DFSP | best-effort: Spindle cell neoplasm; best-effort: Storiform histology | UBERON:0001474 dermis | Foundational pathology phenotype for diagnosis | (trinidad2023rarevariantsof pages 1-3, jozwik2024dermatofibrosarcomaprotuberansan pages 2-4, fionda2024theroleof pages 1-2) |
| Diffuse CD34 positivity | Classic DFSP usually demonstrates strong diffuse CD34 immunopositivity on IHC | best-effort: Abnormal CD34 expression positive | UBERON:0001474 dermis | Key diagnostic pathology finding; helps distinguish from dermatofibroma | (trinidad2023rarevariantsof pages 1-3, jozwik2024dermatofibrosarcomaprotuberansan pages 2-4, fionda2024theroleof pages 1-2) |
| Reduced or absent CD34 in fibrosarcomatous areas | CD34 expression may be lost in FS-DFSP; one review notes only ~50% positivity in fibrosarcomatous component in one study and as low as 45% in another; CD34-negative DFSP overall reported in 9.1%, especially FS-DFSP | best-effort: Loss of CD34 expression | UBERON:0001474 dermis; UBERON:0003568 subcutaneous tissue | Important pitfall in diagnosis of high-grade transformation | (jozwik2024dermatofibrosarcomaprotuberansan pages 2-4, meng2024hotspotsandfuture pages 10-12) |
| Trunk predominance | Most common primary site is trunk; examples include ~41.7% in SEER and ~50% in review literature | best-effort: Neoplasm of trunk skin | UBERON:0002097 skin of trunk | Principal anatomic predilection | (kreicher2016incidenceandsurvival pages 1-2, fionda2024theroleof pages 1-2, ono2024establishmentandcharacterization pages 1-5) |
| Extremity involvement | Upper and lower extremities are common sites after trunk; SEER and review data place extremities collectively in roughly one-third or more of cases | best-effort: Neoplasm of limb skin | UBERON:0002101 forelimb; UBERON:0002102 hindlimb | Common anatomic distribution pattern | (kreicher2016incidenceandsurvival pages 1-2, fionda2024theroleof pages 1-2, ono2024establishmentandcharacterization pages 1-5) |
| Head and neck involvement | Head/neck tumors are less common than trunk/extremities but clinically important because margins are harder to obtain; reported around 10–16% in several series | best-effort: Neoplasm of head skin; best-effort: Neoplasm of neck skin | UBERON:0000033 head; UBERON:0000974 neck | Higher recurrence risk in anatomically constrained areas | (fionda2024theroleof pages 1-2, ono2024establishmentandcharacterization pages 1-5, kreicher2016incidenceandsurvival pages 4-6) |
| Pediatric/congenital occurrence | Most cases occur in adults, but 10–15% may arise in children/adolescents; pediatric DFSP estimated at ~6% of cases in one source; giant-cell fibroblastoma is considered a juvenile form | best-effort: Childhood onset; best-effort: Adolescent onset | UBERON:0001003 skin | Pediatric disease is uncommon but recognized | (fionda2024theroleof pages 1-2, ono2024establishmentandcharacterization pages 1-5, jozwik2024dermatofibrosarcomaprotuberansan pages 2-4) |
| Long interval to recurrence / chronic course | Very delayed local recurrence can occur; longest interval from excision to local recurrence reported as 16 years | HP:0033677 Neoplasm recurrence; best-effort: Chronic relapsing course | UBERON:0001003 skin | Supports prolonged surveillance after treatment | (jozwik2024dermatofibrosarcomaprotuberansan pages 2-4) |
| Black patients present with larger tumors more often | Review of disparities literature notes Black patients often present with larger tumors (>3 cm) and more advanced stage at diagnosis | best-effort: Large skin neoplasm | UBERON:0001003 skin | Likely reflects delayed diagnosis/access differences rather than a distinct biologic phenotype alone | (algarin2024cutaneousmalignanciesin pages 2-4) |
| Female predominance in some registry datasets | SEER 2000–2010 showed 53.1% female and incidence 1.14 times higher than men, though some other series report slight male predominance | best-effort: Female predominance | not applicable | Population characteristic rather than patient phenotype, but useful for disease knowledge base | (kreicher2016incidenceandsurvival pages 1-2, kreicher2016incidenceandsurvival pages 4-6) |


*Table: This table maps common clinical, pathologic, and disease-course features of dermatofibrosarcoma protuberans to suggested HPO and UBERON terms using recent reviews and key epidemiologic sources. It is intended as a knowledge-base ready artifact for phenotype annotation and structured curation.*

### 3.2 Quality-of-life impact
While formal QoL instruments were not extracted from the retrieved texts, DFSP management has functional and cosmetic implications due to wide excision requirements and need for complex reconstruction, particularly in anatomically constrained sites (e.g., head/neck) (meng2024hotspotsandfuture pages 10-12).

---

## 4. Genetic / molecular information
### 4.1 Causal genes and chromosomal abnormalities
- **Canonical fusion:** **COL1A1::PDGFB**; cytogenetic patterns include supernumerary ring chromosomes containing chromosome 22 centromere and material from chromosomes 17 and 22, and **t(17;22)(q21.3;q13.1)** (with pediatric enrichment) (trinidad2023rarevariantsof pages 1-3).
- **Mechanistic consequence:** excessive PDGFB production and constitutive activation of PDGFB signaling (ono2024establishmentandcharacterization pages 1-5).

### 4.2 Less common / fusion-negative DFSP and novel fusions (recent developments)
A 2024 review highlights that **~4%–10%** of DFSP cases may not show detectable **COL1A1–PDGFB** by standard methods; among these, some may have cryptic COL1A1–PDGFB and others may be associated with **PDGFD** (meng2024hotspotsandfuture pages 10-12). The same review discusses newer fusions discovered via sequencing approaches (e.g., **COL6A3–PDGFD**, **MAP3K7CL–ERG**, **SLC2A5–BTBD7**) (meng2024hotspotsandfuture pages 10-12), motivating use of **RNA-seq/NGS** in diagnostically difficult cases.

### 4.3 Pathways (current mechanistic model)
Causal chain (simplified):
1. Structural rearrangement → **COL1A1 promoter drives PDGFB** expression (trinidad2023rarevariantsof pages 1-3).
2. PDGFB ligand production → autocrine/paracrine **PDGFRβ (PDGFRB)** activation (NCT00243191 chunk 1, ono2024establishmentandcharacterization pages 1-5).
3. Sustained growth signaling → locally infiltrative spindle-cell tumor with “finger-like” extensions into subcutis (honeycomb infiltration), producing high local recurrence risk if margins are incomplete (meng2024hotspotsandfuture pages 10-12, trinidad2023rarevariantsof pages 1-3).

OpenTargets disease–target associations include **PDGFRB** and **PDGFB** among top associated targets for DFSP (supporting centrality of PDGF axis in disease biology and therapeutics) (OpenTargets Search: Dermatofibrosarcoma protuberans).

---

## 5. Environmental information
No validated environmental, lifestyle, or infectious causal factors were identified in the retrieved evidence set.

---

## 6. Mechanism / pathophysiology
### 6.1 Tissue-level and cellular behavior
DFSP is characterized by a **storiform spindle-cell proliferation** with **subclinical tentacle-like infiltration** into subcutaneous fat yielding a **honeycomb** pattern (trinidad2023rarevariantsof pages 1-3, jozwik2024dermatofibrosarcomaprotuberansan pages 2-4). This invasive growth pattern is the pathologic basis for:
- difficulty in defining true tumor boundaries (meng2024hotspotsandfuture pages 10-12)
- frequent local recurrence without complete margin control (meng2024hotspotsandfuture pages 10-12, algarin2024cutaneousmalignanciesin pages 2-4)

### 6.2 Immune system involvement
Immune-specific mechanistic data were not extracted from the currently retrieved evidence set.

### 6.3 Suggested GO (biological process) and CL (cell type) terms (best-effort)
Direct GO/CL annotations were not contained in the retrieved texts. Based on described biology, plausible candidates include:
- **GO (best-effort):** “platelet-derived growth factor receptor signaling pathway”; “positive regulation of cell proliferation”; “extracellular matrix organization”.
- **CL (best-effort):** “fibroblast” / “myofibroblast” lineage (supported by fibroblastic/myofibroblastic differentiation statements) (trinidad2023rarevariantsof pages 1-3).

---

## 7. Anatomical structures affected
### 7.1 Organ/tissue level
DFSP primarily involves:
- **Dermis and subcutaneous fat**, and rarely muscle/fascia (fionda2024theroleof pages 1-2).

Common locations in SEER (2000–2010): trunk most common, followed by upper and lower limbs; head/neck less frequent but clinically significant (kreicher2016incidenceandsurvival pages 4-6).

### 7.2 Localization (population-based statistics)
From SEER-18 (2000–2010): trunk 33.6%, upper limb 28.1%, lower limb 28.9%, head 8.6% in one excerpted breakdown (kreicher2016incidenceandsurvival pages 4-6).

---

## 8. Temporal development
- **Onset pattern:** chronic/insidious; some lesions remain as plaques for years before protuberant phase (mean ~7 years described for a preprotuberant stage) (jozwik2024dermatofibrosarcomaprotuberansan pages 2-4).
- **Late recurrence:** the longest reported interval from excision to local recurrence cited in a 2024 review was **16 years**, supporting long follow-up (jozwik2024dermatofibrosarcomaprotuberansan pages 2-4).

---

## 9. Inheritance and population
### 9.1 Inheritance pattern
DFSP is not described as a germline inherited disorder in the retrieved evidence; the defining COL1A1::PDGFB alteration is a **somatic** rearrangement in tumor tissue (trinidad2023rarevariantsof pages 1-3).

### 9.2 Epidemiology (statistics)
#### Incidence
A population-based U.S. SEER-18 analysis (2000–2010) reported:
- “**Overall annual incidence rate of DFSP from 2000 to 2010 was 4.1 persons per million person-years.**” (Kreicher et al., *Dermatologic Surgery*, 2016-01; DOI: 10.1097/DSS.0000000000000300; URL: https://doi.org/10.1097/dss.0000000000000300) (kreicher2016incidenceandsurvival pages 4-6)
- Time trend: “**Age-adjusted annual incidence of primary DFSP dropped from 4.1 in 2000 to 3.1 in 2010, but time-trend analysis showed that there was no significant change in incidence over the decade.**” (kreicher2016incidenceandsurvival pages 4-6)

A 2024 systematic review of postoperative radiotherapy provides a broader range estimate: “**The incidence is 0.8–4.5 cases per one million persons**” (Fionda et al., *Journal of Clinical Medicine*, 2024-03-21; DOI: 10.3390/jcm13061798; URL: https://doi.org/10.3390/jcm13061798) (fionda2024theroleof pages 1-2).

#### Sex and race disparities (SEER)
Kreicher et al. (SEER-18, 2000–2010) reported:
- “**Incidence among women from 2000 to 2010 was 1.14 times higher than men**” (kreicher2016incidenceandsurvival pages 4-6).
- “**Overall incidence rates were 3.6 for all whites … and 7.1 for all blacks …**” (kreicher2016incidenceandsurvival pages 4-6).
- Age-specific peak: peak incidence 7.0 per million ages 35–44 overall; among Black individuals, peak 10.4 ages 45–49 (kreicher2016incidenceandsurvival pages 4-6).

### 9.3 Survival (registry-derived)
Kreicher et al. reported:
- “**Five-year observed survival was 96.2%… Ten-year relative survival rate was 99.1%**” (kreicher2016incidenceandsurvival pages 4-6).
- DFSP-attributed deaths in SEER cause-specific analysis: 92 deaths (kreicher2016incidenceandsurvival pages 4-6).

---

## 10. Diagnostics
### 10.1 Clinical and pathology diagnosis
A definitive diagnosis requires skin biopsy and histology/IHC showing spindle-cell storiform tumor with CD34 positivity (fionda2024theroleof pages 1-2, trinidad2023rarevariantsof pages 1-3). Trinidad et al. (2023) explicitly summarize diagnostic hallmarks and variant spectrum in the abstract (quote shown above) (trinidad2023rarevariantsof pages 1-3).

### 10.2 Molecular diagnostics
Molecular assays used/mentioned in reviews include:
- **FISH** and **multiplex RT-PCR** for COL1A1::PDGFB/PDGFB rearrangements (trinidad2023rarevariantsof pages 1-3, NCT00084630 chunk 1).
- **NGS/RNA sequencing** for unusual or fusion-negative cases; 2024 review notes fusion-negative fraction and new fusions found via WGS/RNA-seq approaches (meng2024hotspotsandfuture pages 10-12).

### 10.3 Differential diagnostic considerations
Immunophenotypic pitfalls include that CD34 is not fully specific and can be negative in a subset (particularly FS-DFSP): one review notes “**9.1% of DFSP patients were CD34 negative, especially FS-DFSP**” (meng2024hotspotsandfuture pages 10-12). This motivates confirmatory molecular testing where morphology/IHC is ambiguous (meng2024hotspotsandfuture pages 10-12, trinidad2023rarevariantsof pages 1-3).

---

## 11. Outcome / prognosis
### 11.1 Key outcome themes
- **Excellent long-term survival** in population registries (10-year relative survival ~99%) despite significant local morbidity risk (kreicher2016incidenceandsurvival pages 4-6).
- **Recurrence** is the dominant clinical problem; risk rises with incomplete margins and with FS-DFSP (meng2024hotspotsandfuture pages 10-12, trinidad2023rarevariantsof pages 1-3).
- **Metastasis** is generally uncommon (<1–5% in a 2024 disparities review), but increased in FS-DFSP (algarin2024cutaneousmalignanciesin pages 2-4, trinidad2023rarevariantsof pages 1-3).

---

## 12. Treatment
### 12.1 Surgery (real-world standard of care)
Surgery is first-line treatment (fionda2024theroleof pages 1-2). Two major strategies are wide local excision (WLE) and Mohs micrographic surgery (MMS).

A 2024 review synthesizing recurrence data reports:
- Overall: “**local recurrence after tumor resection ranges from 26% to 60%. WLE can reduce this to 0%-41%, while MMS can control it to 0%-8.3%.**” (Meng et al., *Frontiers in Oncology*, 2024-11; DOI: 10.3389/fonc.2024.1399486; URL: https://doi.org/10.3389/fonc.2024.1399486) (meng2024hotspotsandfuture pages 10-12)
- Meta-analysis (684 patients): “**recurrence rates of 9.10% after WLE and 2.72% after MMS**” (meng2024hotspotsandfuture pages 10-12).

A 2024 review focused on people of color also summarizes comparative recurrence: “**Mohs micrographic surgery in DFSP shows a recurrence rate of only 1%, compared to 6.3–8.8% with wide local excision.**” (Algarin et al., *Current Dermatology Reports*, 2024-06; DOI: 10.1007/s13671-024-00432-0; URL: https://doi.org/10.1007/s13671-024-00432-0) (algarin2024cutaneousmalignanciesin pages 2-4).

### 12.2 Postoperative radiotherapy
A 2024 multidisciplinary systematic review (papers 1989–2023) reports typical dosing and control:
- “**most authors reported using standard fractionation (2 Gy/die) with a wide total dose ranging from 50 to 70 Gy. The local control after postoperative radiotherapy was excellent (75–100%), with a median follow-up time of 69 months.**” (Fionda et al., 2024-03-21; URL: https://doi.org/10.3390/jcm13061798) (fionda2024theroleof pages 1-2)

It concludes postoperative radiotherapy may be considered adjuvantly for risk factors (close margins, recurrence, aggressive histology) or as salvage for positive margins in multidisciplinary context (fionda2024theroleof pages 1-2).

### 12.3 Targeted therapy: imatinib and other TKIs
#### Imatinib (PDGFR inhibitor)
A 2024 patient-derived DFSP cell line study summarizes real-world clinical positioning and a quantitative resistance/progression statistic:
- “**Although PDGF receptor inhibitor imatinib mesylate was approved for the treating patients with unresectable or metastatic DFSP, disease progression was shown in 9.2% of the patients.**” (Ono et al., *Human Cell*, 2024-02-19 online; DOI: 10.1007/s13577-024-01030-9; URL: https://doi.org/10.1007/s13577-024-01030-9) (ono2024establishmentandcharacterization pages 1-5).

ClinicalTrials.gov records support practical implementation and biomarker integration in DFSP trials:
- **Neoadjuvant imatinib trial (Phase 2):** NCT00243191 (completed; started 2006-05). Primary outcome included comparing phosphorylated PDGFRB pre/post short imatinib exposure (ClinicalTrials.gov; URL in record: http://www.sarctrials.org) (NCT00243191 chunk 1).
- **Advanced/recurrent/metastatic DFSP imatinib Phase 2 trial:** NCT00084630 (completed; started 2004-05) includes objectives to measure response rate, 1-year PFS, toxicity, and correlation with PDGFB rearrangement by RT-PCR/FISH (NCT00084630 chunk 1).

A 2024 review emphasizes a key clinical caveat: “**cases without fusion genes may not respond to imatinib**,” motivating genetic confirmation before therapy (meng2024hotspotsandfuture pages 10-12).

#### Other TKIs / approaches
A 2024 review discusses resistance and alternative targets/agents, including pazopanib and sunitinib as potential options in selected contexts, but high-quality comparative outcome evidence was not extracted in the retrieved text set (meng2024hotspotsandfuture pages 10-12, felix2024dermatofibrosarcomaprotuberansthe pages 3-4).

### 12.4 MAXO (Medical Action Ontology) term suggestions (best-effort)
MAXO IDs were not present in the retrieved texts. Best-effort action labels:
- Surgical excision of tumor (WLE)
- Mohs micrographic surgery
- Adjuvant radiotherapy
- Tyrosine kinase inhibitor therapy (imatinib)
- Molecular diagnostic testing (FISH/RT-PCR/NGS)

A structured summary of treatments/outcomes is provided below.

| Domain | Modality | Key details/outcomes | Evidence type | Citation |
|---|---|---|---|---|
| Diagnosis | Histology + immunohistochemistry | Definitive diagnosis is based on biopsy showing uniform spindle cells in a storiform/cartwheel pattern with diffuse dermal and subcutaneous infiltration in a honeycomb pattern; tumor cells are typically strongly CD34-positive and usually negative for factor XIIIa, desmin, D2-40, and CD163. CD34 loss is more common in fibrosarcomatous DFSP. | Review, pathology review | (trinidad2023rarevariantsof pages 1-3, jozwik2024dermatofibrosarcomaprotuberansan pages 2-4, fionda2024theroleof pages 1-2) |
| Diagnosis | Molecular fusion testing: FISH, multiplex RT-PCR, RNA in situ hybridization | COL1A1::PDGFB rearrangement is the canonical molecular lesion; FISH and multiplex RT-PCR are established assays, and PDGFB RNA chromogenic in situ hybridization can serve as a surrogate marker. Fusion-gene detection is diagnostically useful because ~4%–10% of DFSP lack detectable canonical COL1A1::PDGFB by routine testing; some have cryptic COL1A1::PDGFB or PDGFD-associated fusions. | Review, molecular pathology | (trinidad2023rarevariantsof pages 1-3, meng2024hotspotsandfuture pages 10-12) |
| Diagnosis | NGS / RNA-seq / genomic profiling | Recent molecular work identified additional rare fusions including COL6A3-PDGFD, MAP3K7CL-ERG, and SLC2A5-BTBD7, supporting NGS/RNA-seq in diagnostically challenging or fusion-negative cases. | Review | (meng2024hotspotsandfuture pages 10-12) |
| Diagnosis | Imaging | MRI is used to define extent, especially for larger or recurrent lesions; case/model reports describe homogeneously low T2 signal with heterogeneous enhancement. Imaging is supportive rather than diagnostic. | Review, case/preclinical model report | (acosta2017dermatofibrosarcomaprotuberans pages 1-3, ono2024establishmentandcharacterization pages 1-5) |
| Treatment | Wide local excision (WLE) | Standard surgical option for localized DFSP; commonly recommended margins are 2–3 cm. Reported post-resection recurrence after WLE ranges from 0%–41%; 2023 NCCN-cited range ~1.7%–30.8%. One meta-analysis cited in review reported 9.10% recurrence after WLE. | Review, meta-analytic summary | (meng2024hotspotsandfuture pages 10-12, acosta2017dermatofibrosarcomaprotuberans pages 1-3, felix2024dermatofibrosarcomaprotuberansthe pages 3-4) |
| Treatment | Mohs micrographic surgery (MMS) | Margin-controlled surgery that examines essentially the full peripheral/deep margin and preserves tissue; recurrence is consistently lower than WLE. Reported recurrence ranges 0%–8.3%, with 2023 NCCN-cited range ~0%–6.6%; meta-analysis reported 2.72% recurrence after MMS. | Review, meta-analytic summary | (meng2024hotspotsandfuture pages 10-12, algarin2024cutaneousmalignanciesin pages 2-4, acosta2017dermatofibrosarcomaprotuberans pages 1-3) |
| Treatment | Surgery choice by site | Head/neck tumors have higher recurrence risk because adequate margins are harder to achieve; MMS or modified slow MMS is often favored in anatomically constrained areas, including face/neck and pediatric cases. | Review | (felix2024dermatofibrosarcomaprotuberansthe pages 3-4, meng2024hotspotsandfuture pages 10-12) |
| Treatment | Postoperative radiotherapy | Used adjuvantly for close margins, recurrent tumors, or aggressive histology, and as salvage for positive margins. Most reports used standard fractionation of 2 Gy/day to total 50–70 Gy; local control after postoperative RT was 75%–100% with median follow-up 69 months. | Systematic review | (fionda2024theroleof pages 1-2) |
| Treatment | Imatinib (PDGFR inhibitor) | Approved for unresectable or metastatic DFSP and rationally targeted to PDGFR signaling driven by COL1A1::PDGFB. Clinical activity is best in fusion-positive tumors; fusion-negative tumors may not respond. Across nine studies totaling 152 patients, disease progression occurred in 9.2% (14/152). Neoadjuvant and advanced-disease phase II trials are completed. | Clinical trials, review, preclinical rationale | (ono2024establishmentandcharacterization pages 1-5, NCT00243191 chunk 1, NCT00084630 chunk 1, NCT00122473 chunk 2) |
| Treatment | Other TKIs / salvage targeted therapy | Sunitinib and pazopanib are discussed as potential options in imatinib-resistant or advanced DFSP; evidence is limited and largely non-randomized or review-based. Pazopanib has antiangiogenic and PDGFR-targeting activity; sunitinib is mentioned as salvage in refractory cases. | Review, limited clinical evidence | (meng2024hotspotsandfuture pages 10-12, felix2024dermatofibrosarcomaprotuberansthe pages 3-4) |
| Treatment | Preclinical drug discovery models | New DFSP cell line NCC-DFSP5-C1 retains COL1A1::PDGFB, forms spheroids, is invasive, and enabled drug-library screening to identify anti-cancer agents inhibiting DFSP proliferation, expanding preclinical testing capacity. | Preclinical model study | (ono2024establishmentandcharacterization pages 1-5) |
| Prognosis | Local recurrence | DFSP is locally aggressive with recurrence strongly influenced by margin status and treatment modality. Reviews cite overall local recurrence after tumor resection from 26%–60%, while treatment-specific recurrence falls substantially with WLE or MMS. Fibrosarcomatous transformation increases recurrence risk. | Review, pathology review | (meng2024hotspotsandfuture pages 10-12, trinidad2023rarevariantsof pages 1-3, algarin2024cutaneousmalignanciesin pages 2-4) |
| Prognosis | Metastatic risk | Metastatic potential is low, generally reported as <1%–5% overall, but is higher in fibrosarcomatous DFSP. | Review | (algarin2024cutaneousmalignanciesin pages 2-4, trinidad2023rarevariantsof pages 1-3) |
| Prognosis | SEER survival | In SEER-18 (2000–2010), 5-year observed survival was 96.2%, 5-year relative survival 99.8%, 10-year observed survival 91.1%, and 10-year relative survival 99.1%. DFSP-specific deaths identified in SEER were 92 cases. | Registry study | (kreicher2016incidenceandsurvival pages 4-6) |
| Prognosis | Adverse prognostic factors | Worse outcomes are associated with increasing age, male sex, black race in some registry analyses, larger tumor size, limb/head location, positive or narrow margins, and fibrosarcomatous transformation. | Registry study, review | (kreicher2016incidenceandsurvival pages 4-6, criscito2016prognosticfactorstreatment pages 1-2, jozwik2024dermatofibrosarcomaprotuberansan pages 2-4) |
| Prognosis | Surveillance / follow-up | Long preprotuberant phases and very late local recurrence are documented; reviews note nonprotuberant plaques may persist for a mean of 7 years before becoming nodular, and recurrence has been reported up to 16 years after excision, supporting long-term surveillance. | Review | (jozwik2024dermatofibrosarcomaprotuberansan pages 2-4) |


*Table: This table summarizes key diagnostic approaches, treatments, and prognostic data for dermatofibrosarcoma protuberans, emphasizing quantitative outcomes such as recurrence, radiotherapy local control, and survival. It is useful as a compact evidence map linking practical management choices to the underlying literature.*

---

## 13. Prevention
Primary prevention strategies are not established in the retrieved evidence. Secondary prevention is effectively **early recognition and complete excision with margin control** to prevent repeated recurrences and morbidity (meng2024hotspotsandfuture pages 10-12, jozwik2024dermatofibrosarcomaprotuberansan pages 2-4). No population screening programs were identified in the retrieved evidence.

---

## 14. Other species / natural disease
No naturally occurring DFSP-equivalent veterinary disease was established from the retrieved evidence set in this run.

---

## 15. Model organisms / experimental models
A major 2024 development is expansion of DFSP preclinical resources:
- Ono et al. report establishment of a patient-derived DFSP cell line (NCC-DFSP5-C1) retaining COL1A1::PDGFB and enabling drug screening (published 2024-02; DOI: 10.1007/s13577-024-01030-9; URL: https://doi.org/10.1007/s13577-024-01030-9) (ono2024establishmentandcharacterization pages 1-5).

**Direct abstract quote:** “**Here, we successfully established a novel DFSP cell line (NCC-DFSP5-C1) using surgically resected tumor tissue from a patient with DFSP. NCC-DFSP5-C1 cells were confirmed to carry the COL1A1-PDGFB translocation…**” (ono2024establishmentandcharacterization pages 1-5).

---

## Structured identifiers and key epidemiology (artifact)
| Item | Value | Evidence/Citation |
|---|---|---|
| Disease name | Dermatofibrosarcoma protuberans (DFSP) | (trinidad2023rarevariantsof pages 1-3, jozwik2024dermatofibrosarcomaprotuberansan pages 2-4) |
| MONDO ID | MONDO:0011934 | (OpenTargets Search: Dermatofibrosarcoma protuberans) |
| Disease class / brief nomenclature note | Rare dermal/superficial soft-tissue sarcoma; described as the most common dermal sarcoma and about 1% of soft-tissue sarcomas | (fionda2024theroleof pages 1-2, jozwik2024dermatofibrosarcomaprotuberansan pages 2-4) |
| Canonical molecularly defined form | COL1A1::PDGFB fusion-positive DFSP is the classic molecular form | (acosta2017dermatofibrosarcomaprotuberans pages 1-3, trinidad2023rarevariantsof pages 1-3) |
| Variant / synonym | Bednar tumor (pigmented DFSP variant) | (felix2024dermatofibrosarcomaprotuberansthe pages 3-4, fionda2024theroleof pages 1-2) |
| Variant / synonym | Fibrosarcomatous DFSP (FS-DFSP), an aggressive histologic variant with higher recurrence/metastatic risk | (trinidad2023rarevariantsof pages 1-3, jozwik2024dermatofibrosarcomaprotuberansan pages 2-4) |
| Related juvenile form | Giant-cell fibroblastoma, described as a juvenile form occurring predominantly in the first decade of life | (jozwik2024dermatofibrosarcomaprotuberansan pages 2-4) |
| Other named variants | Myxoid, myoid, granular cell, sclerosing, and atrophic DFSP variants | (trinidad2023rarevariantsof pages 1-3) |
| US incidence estimate | 4.1 per million person-years overall in SEER-18 (2000-2010) | (kreicher2016incidenceandsurvival pages 4-6, kreicher2016incidenceandsurvival pages 1-2) |
| Broader reported incidence range | Approximately 0.8-4.5 cases per million across reviews/population datasets | (fionda2024theroleof pages 1-2, jozwik2024dermatofibrosarcomaprotuberansan pages 1-2) |
| Higher-incidence registry examples | Alberta Cancer Registry 9.3 per million; Denmark 5.3 per million; Sweden about 4.4 in men vs 4.0 in women per million/year | (jozwik2024dermatofibrosarcomaprotuberansan pages 1-2, jozwik2024dermatofibrosarcomaprotuberansan pages 2-4) |
| Sex disparity | Slight female excess in SEER-18: 53.1% female; incidence 1.14 times that of males in one large US study, though some other series report slight male predominance | (kreicher2016incidenceandsurvival pages 1-2, kreicher2016incidenceandsurvival pages 4-6, jozwik2024dermatofibrosarcomaprotuberansan pages 2-4) |
| Race disparity | Black individuals have roughly twice the incidence of White individuals in US SEER analyses; example rates 7.1 vs 3.6 per million and 6.5 vs 3.9 per million in cited datasets | (kreicher2016incidenceandsurvival pages 4-6, jozwik2024dermatofibrosarcomaprotuberansan pages 1-2) |
| Age distribution | Can occur at any age, but peaks in young to middle-aged adults; largest SEER age group 20-39 years, with peak incidence around the 4th-5th decades | (kreicher2016incidenceandsurvival pages 2-4, jozwik2024dermatofibrosarcomaprotuberansan pages 1-2) |


*Table: This table summarizes the currently available standardized identifier, key names and variants, and the main epidemiologic patterns for dermatofibrosarcoma protuberans using only evidence already gathered. It is useful as a compact knowledge-base ready reference for nomenclature and population context.*

---

## Limitations of this report (evidence availability)
- Several template-requested identifiers (ICD-10/ICD-11, OMIM, Orphanet, MeSH tree IDs) and formal QoL instrument outcomes were not present in the retrieved full texts/records in this run and therefore are not reported.
- Many mechanistic details (e.g., specific downstream signaling nodes, multi-omics, immune profiling) and pharmacogenomics are discussed in the broader literature but were not extractable from the current evidence set without additional document retrieval.

---

## Key references (with dates and URLs)
- Trinidad CM et al. *Dermatopathology* (Published 2023-01-29). “Rare Variants of Dermatofibrosarcoma Protuberans…” URL: https://doi.org/10.3390/dermatopathology10010008 (trinidad2023rarevariantsof pages 1-3)
- Fionda B et al. *Journal of Clinical Medicine* (Published 2024-03-21). “The Role of Postoperative Radiotherapy…” URL: https://doi.org/10.3390/jcm13061798 (fionda2024theroleof pages 1-2)
- Meng Z et al. *Frontiers in Oncology* (Published 2024-11). “Hotspots and future trends of DFSP.” URL: https://doi.org/10.3389/fonc.2024.1399486 (meng2024hotspotsandfuture pages 10-12)
- Kreicher KL et al. *Dermatologic Surgery* (2016-01). “Incidence and Survival…” URL: https://doi.org/10.1097/dss.0000000000000300 (kreicher2016incidenceandsurvival pages 4-6)
- Ono T et al. *Human Cell* (Published 2024-02-19 online; Version of record). “Establishment and characterization of NCC-DFSP5-C1…” URL: https://doi.org/10.1007/s13577-024-01030-9 (ono2024establishmentandcharacterization pages 1-5)
- ClinicalTrials.gov NCT00243191 (results posted 2012-03-29): “Neoadjuvant Imatinib in DFSP.” (NCT00243191 chunk 1)
- ClinicalTrials.gov NCT00084630 (last update posted 2013-02-28): “Imatinib Mesylate in Locally Recurrent or Metastatic DFSP.” (NCT00084630 chunk 1)


References

1. (OpenTargets Search: Dermatofibrosarcoma protuberans): Open Targets Query (Dermatofibrosarcoma protuberans, 8 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (fionda2024theroleof pages 1-2): Bruno Fionda, Antonella Loperfido, Alessandro Di Stefani, Valentina Lancellotta, Andrea Paradisi, Martina De Angeli, Simone Cappilli, Ernesto Rossi, Anna Amelia Caretto, Tiziano Zinicola, Giovanni Schinzari, Stefano Gentileschi, Alessio Giuseppe Morganti, Agata Rembielak, Ketty Peris, and Luca Tagliaferri. The role of postoperative radiotherapy in the management of dermatofibrosarcoma protuberans: a multidisciplinary systematic review. Journal of Clinical Medicine, 13:1798, Mar 2024. URL: https://doi.org/10.3390/jcm13061798, doi:10.3390/jcm13061798. This article has 29 citations.

3. (jozwik2024dermatofibrosarcomaprotuberansan pages 2-4): Marcin Jozwik, Katarzyna Bednarczuk, and Zofia Osierda. Dermatofibrosarcoma protuberans: an updated review of the literature. Cancers, 16:3124, Sep 2024. URL: https://doi.org/10.3390/cancers16183124, doi:10.3390/cancers16183124. This article has 31 citations.

4. (trinidad2023rarevariantsof pages 1-3): Celestine M. Trinidad, Sintawat Wangsiricharoen, Victor G. Prieto, and Phyu P. Aung. Rare variants of dermatofibrosarcoma protuberans: clinical, histologic, and molecular features and diagnostic pitfalls. Dermatopathology, 10:54-62, Jan 2023. URL: https://doi.org/10.3390/dermatopathology10010008, doi:10.3390/dermatopathology10010008. This article has 37 citations.

5. (algarin2024cutaneousmalignanciesin pages 2-4): Yanci A. Algarin, Anika Pulumati, Jiali Tan, and Nathalie C. Zeitouni. Cutaneous malignancies in people of color: a review of dermatofibrosarcoma protuberans and kaposi sarcoma. Current Dermatology Reports, 13:217-225, Jun 2024. URL: https://doi.org/10.1007/s13671-024-00432-0, doi:10.1007/s13671-024-00432-0. This article has 1 citations.

6. (ono2024establishmentandcharacterization pages 1-5): Takuya Ono, Rei Noguchi, Julia Osaki, Taro Akiyama, Yuki Adachi, Naoki Kojima, Yu Toda, Suguru Fukushima, Yuki Yoshimatsu, Akihiko Yoshida, Akira Kawai, and Tadashi Kondo. Establishment and characterization of ncc-dfsp5-c1: a novel patient-derived dermatofibrosarcoma protuberans cell line. Human cell, 37:854-864, Feb 2024. URL: https://doi.org/10.1007/s13577-024-01030-9, doi:10.1007/s13577-024-01030-9. This article has 2 citations and is from a peer-reviewed journal.

7. (NCT00122473 chunk 2):  Imatinib in Dermatofibrosarcoma Protuberans (DFSP). Dermatologic Cooperative Oncology Group. 2004. ClinicalTrials.gov Identifier: NCT00122473

8. (meng2024hotspotsandfuture pages 10-12): Zhen Meng, Rui Zhang, Zhihong Sun, Cong Fu, Zhiyu Li, Luying Wang, Ran Huo, and Feng Xue. Hotspots and future trends of dermatofibrosarcoma protuberans. Frontiers in Oncology, Nov 2024. URL: https://doi.org/10.3389/fonc.2024.1399486, doi:10.3389/fonc.2024.1399486. This article has 3 citations.

9. (NCT00243191 chunk 1):  Neoadjuvant Imatinib in Dermatofibrosarcoma Protuberans. Sarcoma Alliance for Research through Collaboration. 2006. ClinicalTrials.gov Identifier: NCT00243191

10. (felix2024dermatofibrosarcomaprotuberansthe pages 3-4): Bryan Felix and Suma Kaza. Dermatofibrosarcoma protuberans: the impact of the surgical incision site in relation to tumor recurrence. Cureus, Dec 2024. URL: https://doi.org/10.7759/cureus.75591, doi:10.7759/cureus.75591. This article has 5 citations.

11. (kreicher2016incidenceandsurvival pages 4-6): Kathryn L. Kreicher, David E. Kurlander, Haley R. Gittleman, Jill S. Barnholtz-Sloan, and Jeremy S. Bordeaux. Incidence and survival of primary dermatofibrosarcoma protuberans in the united states. Dermatologic Surgery, 42:S24–S31, Jan 2016. URL: https://doi.org/10.1097/dss.0000000000000300, doi:10.1097/dss.0000000000000300. This article has 260 citations and is from a peer-reviewed journal.

12. (NCT00084630 chunk 1):  Imatinib Mesylate in Treating Patients With Locally Recurrent or Metastatic Dermatofibrosarcoma Protuberans. National Cancer Institute (NCI). 2004. ClinicalTrials.gov Identifier: NCT00084630

13. (kreicher2016incidenceandsurvival pages 1-2): Kathryn L. Kreicher, David E. Kurlander, Haley R. Gittleman, Jill S. Barnholtz-Sloan, and Jeremy S. Bordeaux. Incidence and survival of primary dermatofibrosarcoma protuberans in the united states. Dermatologic Surgery, 42:S24–S31, Jan 2016. URL: https://doi.org/10.1097/dss.0000000000000300, doi:10.1097/dss.0000000000000300. This article has 260 citations and is from a peer-reviewed journal.

14. (acosta2017dermatofibrosarcomaprotuberans pages 1-3): Alvaro E. Acosta and Catalina Santa Vélez. Dermatofibrosarcoma protuberans. Current Treatment Options in Oncology, 18:1-14, Aug 2017. URL: https://doi.org/10.1007/s11864-017-0498-5, doi:10.1007/s11864-017-0498-5. This article has 119 citations and is from a peer-reviewed journal.

15. (criscito2016prognosticfactorstreatment pages 1-2): Maressa C. Criscito, Kathryn J. Martires, and Jennifer A. Stein. Prognostic factors, treatment, and survival in dermatofibrosarcoma protuberans. JAMA Dermatology, 152:1365, Dec 2016. URL: https://doi.org/10.1001/jamadermatol.2016.1886, doi:10.1001/jamadermatol.2016.1886. This article has 104 citations and is from a domain leading peer-reviewed journal.

16. (jozwik2024dermatofibrosarcomaprotuberansan pages 1-2): Marcin Jozwik, Katarzyna Bednarczuk, and Zofia Osierda. Dermatofibrosarcoma protuberans: an updated review of the literature. Cancers, 16:3124, Sep 2024. URL: https://doi.org/10.3390/cancers16183124, doi:10.3390/cancers16183124. This article has 31 citations.

17. (kreicher2016incidenceandsurvival pages 2-4): Kathryn L. Kreicher, David E. Kurlander, Haley R. Gittleman, Jill S. Barnholtz-Sloan, and Jeremy S. Bordeaux. Incidence and survival of primary dermatofibrosarcoma protuberans in the united states. Dermatologic Surgery, 42:S24–S31, Jan 2016. URL: https://doi.org/10.1097/dss.0000000000000300, doi:10.1097/dss.0000000000000300. This article has 260 citations and is from a peer-reviewed journal.
