---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T14:39:24.955528'
end_time: '2026-04-05T14:48:45.719763'
duration_seconds: 560.76
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Essential Thrombocythemia
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Essential Thrombocythemia
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Essential Thrombocythemia** covering all of the
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
- **Disease Name:** Essential Thrombocythemia
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Essential Thrombocythemia** covering all of the
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


# Essential Thrombocythemia (ET) — Comprehensive Disease Characteristics Report (2024-focused)

## Target Disease
- **Disease name:** Essential thrombocythemia (ET) / essential thrombocythaemia
- **Category:** BCR-ABL1–negative (Philadelphia-negative) myeloproliferative neoplasm (MPN) characterized by clonal thrombocytosis and megakaryocytic proliferation (loscocco2024onethousandpatients pages 1-2, ferrer‐marin2024essentialthrombocythaemiaa pages 1-2, tefferi2024essentialthrombocythemia2024 pages 1-2).
- **MONDO ID:** Not captured in retrieved sources (see Identifiers table below) (tefferi2025essentialthrombocythemia pages 1-2, tefferi2024essentialthrombocythemia2024 pages 1-2).

## Key recent sources prioritized (2023–2024)
- Tefferi A, Vannucchi AM, Barbui T. *Essential thrombocythemia: 2024 update on diagnosis, risk stratification, and management.* **Am J Hematol. Jan 2024.** https://doi.org/10.1002/ajh.27216 (tefferi2024essentialthrombocythemia2024 pages 1-2).
- Ferrer‑Marín F, Hernández‑Boluda JC, Alvarez‑Larrán A. *Essential thrombocythaemia: A contemporary approach with new drugs on the horizon.* **Br J Haematol. Apr 2024.** https://doi.org/10.1111/bjh.19403 (ferrer‐marin2024essentialthrombocythaemiaa pages 1-2).
- Gangat N et al. *One thousand patients with essential thrombocythemia: the Mayo Clinic experience.* **Blood Cancer J. Jan 2024.** https://doi.org/10.1038/s41408-023-00972-x (gangat2024onethousandpatients pages 1-2).
- Loscocco GG et al. *One thousand patients with essential thrombocythemia: the Florence-CRIMM experience.* **Blood Cancer J. Jan 2024.** https://doi.org/10.1038/s41408-023-00968-7 (loscocco2024onethousandpatients pages 1-2).
- Venkat RK et al. *Risk of bleeding in patients with essential thrombocythemia and extreme thrombocytosis.* **Blood Adv. Dec 2024.** https://doi.org/10.1182/bloodadvances.2024013777 (venkat2024riskofbleeding pages 1-2).

---

## 1. Disease Information

### 1.1 What is ET? (current understanding)
ET is a **clonal MPN** with **persistent thrombocytosis** and **bone marrow megakaryocytic proliferation**, with clinical complications dominated by **thrombosis, bleeding, and less frequently progression to myelofibrosis (MF) or acute myeloid leukemia (AML)** (tefferi2025essentialthrombocythemia pages 1-2, tefferi2024essentialthrombocythemia2024 pages 1-2).
- A contemporary definition from the AJH 2024 update describes: “**Essential thrombocythemia is a Janus kinase 2 (JAK2) mutation‑prevalent myeloproliferative neoplasm characterized by clonal thrombocytosis**” (tefferi2024essentialthrombocythemia2024 pages 1-2).
- The JAMA review describes ET as a “**clonal myeloproliferative neoplasm characterized by persistent thrombocytosis (platelet count ≥450 × 10^9/L) and increased risks of thrombosis and bleeding**” (tefferi2025essentialthrombocythemia pages 1-2).

### 1.2 Key identifiers and synonyms
The retrieved evidence did not contain explicit ICD-10/ICD-11/MeSH/OMIM/Orphanet/MONDO codes; however, it consistently frames ET as a **Philadelphia-negative/BCR-ABL1–negative** MPN with diagnostic platelet threshold **≥450 ×10^9/L** (tefferi2025essentialthrombocythemia pages 1-2, tefferi2024essentialthrombocythemia2024 pages 1-2).

| Identifier system | Identifier/code | Preferred name | Common synonyms/alternate names | Notes |
|---|---|---|---|---|
| MONDO | Not captured in retrieved sources | Essential thrombocythemia | Essential thrombocythaemia; ET | Clonal myeloproliferative neoplasm characterized by persistent/clonal thrombocytosis; platelet threshold for diagnosis is ≥450 ×10^9/L in current criteria (tefferi2025essentialthrombocythemia pages 1-2, tefferi2024essentialthrombocythemia2024 pages 1-2, tefferi2024essentialthrombocythemia2024 pages 4-5) |
| ICD-10 | Not captured in retrieved sources | Essential thrombocythemia | Essential thrombocythaemia; ET | Specific code not provided in retrieved evidence; disease described as a Philadelphia-negative myeloproliferative neoplasm with thrombotic/bleeding risk (ferrer‐marin2024essentialthrombocythaemiaa pages 1-2, tefferi2025essentialthrombocythemia pages 1-2) |
| ICD-11 | Not captured in retrieved sources | Essential thrombocythemia | Essential thrombocythaemia; ET | Specific code not provided in retrieved evidence; diagnosis requires exclusion of other myeloid neoplasms including CML/BCR::ABL1-positive disease (thiele2025evolutionofwho pages 3-3, tefferi2024essentialthrombocythemia2024 pages 4-5) |
| MeSH | Not captured in retrieved sources | Essential thrombocythemia | Essential thrombocythaemia; ET | Specific controlled-vocabulary identifier not retrieved; disease is BCR-ABL1-negative/Philadelphia-negative and marked by megakaryocytic proliferation with mature hyperlobulated megakaryocytes in loose clusters (allen2022thrombocytosisandessential pages 5-6, tefferi2024essentialthrombocythemia2024 pages 4-5) |
| OMIM | Not captured in retrieved sources | Essential thrombocythemia | Essential thrombocythaemia; ET | Specific OMIM entry not captured; canonical driver mutations are JAK2, CALR, and MPL, supporting clonal disease definition (tefferi2024essentialthrombocythemia2024 pages 1-2, loscocco2024onethousandpatients pages 1-2) |
| Orphanet | Not captured in retrieved sources | Essential thrombocythemia | Essential thrombocythaemia; ET | Specific Orphanet identifier not captured; overview from recent reviews: chronic/clonal thrombocytosis, often indolent course, risk of thrombosis, hemorrhage, and less commonly progression to myelofibrosis or AML (ferrer‐marin2024essentialthrombocythaemiaa pages 1-2, tefferi2024essentialthrombocythemia2024 pages 1-2) |


*Table: This table summarizes the disease name, nomenclature, and identifier fields for Essential Thrombocythemia using only retrieved evidence. It is useful for knowledge-base curation because it separates supported definitional features from identifier systems whose exact codes were not captured in the current evidence set.*

### 1.3 Evidence sources (individual vs aggregated)
Most information in this report is derived from aggregated disease-level resources (large cohorts, systematic clinical reviews, and classification updates), including 1,000-patient institutional cohorts and guideline-style reviews (loscocco2024onethousandpatients pages 1-2, gangat2024onethousandpatients pages 1-2, tefferi2024essentialthrombocythemia2024 pages 1-2).

---

## 2. Etiology

### 2.1 Disease causal factors (primary causes)
ET is primarily caused by **somatic (acquired) driver mutations** in **JAK2, CALR, or MPL**, which **upregulate JAK–STAT signaling** and promote clonal megakaryopoiesis/platelet production (tefferi2024essentialthrombocythemia2024 pages 2-2, ferrer‐marin2024essentialthrombocythaemiaa pages 1-2).
- ET driver mutations are typically **mutually exclusive** (JAK2 vs CALR vs MPL) and present in ~80–90% of patients depending on the cohort/definition (tefferi2024essentialthrombocythemia2024 pages 1-2, tefferi2025essentialthrombocythemia pages 1-2).

### 2.2 Risk factors
**Host/clinical risk factors** that increase thrombotic risk include: prior thrombosis, age >60 years, JAK2 mutation, and cardiovascular risk factors (e.g., hypertension) (tefferi2025essentialthrombocythemia pages 1-2, tefferi2024essentialthrombocythemia2024 pages 1-2).
- In a Mayo 1,000-patient cohort (1967–2023), multivariable predictors of outcomes included **hypertension** (HR ~1.7 for overall survival; HR ~1.7 for arterial thrombosis-free survival) and **JAK2 mutation** (HR ~1.8 for arterial thrombosis-free survival) (gangat2024onethousandpatients pages 1-2).

**Genetic risk/prognostic modifiers (co-mutations):** additional somatic mutations are common and influence prognosis.
- AJH 2024 update: ~50% have additional mutations (e.g., **TET2, ASXL1, DNMT3A, SF3B1**), and mutation associations include **JAK2V617F with thrombosis** and **MPL/CALR-1 with increased MF transformation risk** (tefferi2024essentialthrombocythemia2024 pages 1-2).
- The 2024 BJH review notes that “triple-negative” ET may harbor other myeloid mutations including **ASXL1, DNMT3A, TET2, EZH2, IDH1/2, RUNX1, SRSF2, SF3B1, TP53** (ferrer‐marin2024essentialthrombocythaemiaa pages 1-2).

### 2.3 Protective factors
No explicit protective genetic variants or environmental protective factors were captured in the retrieved evidence. However, both large-cohort analyses and expert updates suggest **aspirin therapy** is associated with reduced thrombosis risk in ET populations (a preventive/mitigating factor rather than primary prevention) (gangat2024onethousandpatients pages 1-2).

### 2.4 Gene–environment interactions
Direct gene–environment interaction evidence was not captured in the retrieved sources. Clinically, mutation status and cardiovascular risk factors interact in determining thrombotic risk and antiplatelet strategy (tefferi2025essentialthrombocythemia pages 1-2, ferrer‐marin2024essentialthrombocythaemiaa pages 4-5).

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes (with suggested HPO terms)
ET phenotypes span symptoms, signs, and lab/pathology abnormalities (tefferi2025essentialthrombocythemia pages 1-2, tefferi2024essentialthrombocythemia2024 pages 1-2).

**A. Laboratory / hematologic**
- **Persistent thrombocytosis (platelets ≥450 ×10^9/L)** (diagnostic threshold) (tefferi2025essentialthrombocythemia pages 1-2, tefferi2024essentialthrombocythemia2024 pages 4-5).
  - Suggested HPO: **Thrombocytosis (HP:0001894)**.

**B. Thrombotic manifestations**
- Increased risk of **arterial thrombosis** and **venous thrombosis** (tefferi2025essentialthrombocythemia pages 1-2).
  - JAMA review: increased risk of **arterial thrombosis 11%** and **venous thrombosis 7%** (tefferi2025essentialthrombocythemia pages 1-2).
  - Suggested HPO: **Thrombosis (HP:0001977)**; **Arterial thrombosis (HP:0031048)**; **Venous thrombosis (HP:0004936)**.

**C. Bleeding manifestations**
- **Hemorrhagic complications** reported (JAMA review: **8%**) (tefferi2025essentialthrombocythemia pages 1-2).
- Bleeding risk can be associated with **acquired von Willebrand factor abnormalities**, especially with extreme thrombocytosis (venkat2024riskofbleeding pages 3-4, tefferi2024essentialthrombocythemia2024 pages 11-11).
  - Suggested HPO: **Abnormal bleeding (HP:0001892)**.

**D. Microcirculatory symptoms**
- Microcirculatory symptoms such as “**headaches, lightheadedness, and acral paresthesias**” are noted (tefferi2024essentialthrombocythemia2024 pages 1-2).
  - Suggested HPO: **Headache (HP:0002315)**; **Lightheadedness (HP:0030931)**; **Paresthesia (HP:0003401)**.

**E. Disease evolution**
- Progression to **myelofibrosis** and **AML** occurs in a minority (tefferi2025essentialthrombocythemia pages 1-2, tefferi2024essentialthrombocythemia2024 pages 1-2).
  - Suggested HPO: **Myelofibrosis (HP:0005532)**; **Acute myeloid leukemia (HP:0004808)**.

### 3.2 Frequency and progression (selected recent statistics)
- JAMA review: at median 8.5 years from diagnosis, ~**10% develop MF** and **~3% AML** (tefferi2025essentialthrombocythemia pages 1-2).
- Review estimate: MF at 15 years **4–11%** and AML **2–5%** (lazar2024diagnosisandmanagement pages 1-3).

### 3.3 Quality of life impact
Formal QoL instrument results were not captured directly, but symptom burden is a recurring treatment target; ruxolitinib is noted to be superior mainly for symptom control in hydroxyurea-resistant/intolerant ET in MAJIC-ET-related summaries (gunawan2018ruxolitinibforthe pages 1-2, ferrer‐marin2024essentialthrombocythaemiaa pages 7-8).

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes (driver genes)
- **JAK2**, **CALR**, **MPL** are canonical ET driver genes that activate JAK–STAT signaling (tefferi2024essentialthrombocythemia2024 pages 1-2, tefferi2024essentialthrombocythemia2024 pages 2-2).

### 4.2 Driver mutation frequencies (recent large cohorts)
Large 2024 real-world cohorts provide high-confidence mutation frequency estimates:
- **Mayo cohort (n=1000):** JAK2/CALR/MPL **62%/27%/3%**, triple-negative **8%** (gangat2024onethousandpatients pages 1-2).
- **Florence-CRIMM cohort (n=1000):** JAK2/CALR/MPL **66%/19%/4%**, triple-negative **11%** (loscocco2024onethousandpatients pages 1-2).
- JAMA review: approximately 90% have JAK–STAT-activating variants: **JAK2 64%, CALR 23%, MPL 4%** (tefferi2025essentialthrombocythemia pages 1-2).

| Metric | Value | Population/Study | Year | Notes | Source (citation id) |
|---|---:|---|---:|---|---|
| Annual incidence | 1.5 per 100,000 persons | US population; JAMA review | 2025 | Explicitly stated as annual incidence in the US | (tefferi2025essentialthrombocythemia pages 1-2) |
| Annual incidence | 0.6–2.5 per 100,000/year | General population; contemporary review | 2024 | Review estimate for ET incidence | (ferrer‐marin2024essentialthrombocythaemiaa pages 1-2) |
| Incidence | 1–5 per 100,000 | Review article population estimate | 2024 | Reported as incidence; unit phrasing in source not explicitly annual | (lazar2024diagnosisandmanagement pages 1-3) |
| Prevalence | 38–57 per 100,000 | Review article population estimate | 2024 | Reported prevalence range | (lazar2024diagnosisandmanagement pages 1-3) |
| Median age at diagnosis | 59 years | General ET population; JAMA review | 2025 | Median age at diagnosis | (tefferi2025essentialthrombocythemia pages 1-2) |
| Median age | 58 years | Mayo Clinic ET cohort (n=1000) | 2024 | Range 18–90 years | (gangat2024onethousandpatients pages 1-2) |
| Female sex | 63% | Mayo Clinic ET cohort (n=1000) | 2024 | Cohort sex distribution | (gangat2024onethousandpatients pages 1-2) |
| Median age | 59 years | Florence-CRIMM ET cohort (n=1000) | 2024 | Range 18–95 years | (loscocco2024onethousandpatients pages 1-2) |
| Female sex | 65% | Florence-CRIMM ET cohort (n=1000) | 2024 | Cohort sex distribution | (loscocco2024onethousandpatients pages 1-2) |
| JAK2 mutation frequency | 62% | Mayo Clinic ET cohort (n=1000) | 2024 | Driver mutation distribution | (gangat2024onethousandpatients pages 1-2) |
| CALR mutation frequency | 27% | Mayo Clinic ET cohort (n=1000) | 2024 | Driver mutation distribution | (gangat2024onethousandpatients pages 1-2) |
| MPL mutation frequency | 3% | Mayo Clinic ET cohort (n=1000) | 2024 | Driver mutation distribution | (gangat2024onethousandpatients pages 1-2) |
| Triple-negative frequency | 8% | Mayo Clinic ET cohort (n=1000) | 2024 | Driver mutation distribution | (gangat2024onethousandpatients pages 1-2) |
| JAK2 mutation frequency | 66% | Florence-CRIMM ET cohort (n=1000) | 2024 | Driver mutation distribution | (loscocco2024onethousandpatients pages 1-2) |
| CALR mutation frequency | 19% | Florence-CRIMM ET cohort (n=1000) | 2024 | Driver mutation distribution | (loscocco2024onethousandpatients pages 1-2) |
| MPL mutation frequency | 4% | Florence-CRIMM ET cohort (n=1000) | 2024 | Driver mutation distribution | (loscocco2024onethousandpatients pages 1-2) |
| Triple-negative frequency | 11% | Florence-CRIMM ET cohort (n=1000) | 2024 | Driver mutation distribution | (loscocco2024onethousandpatients pages 1-2) |
| JAK2 mutation frequency | 64% | General ET population; JAMA review | 2025 | Approximately 90% of patients had JAK-STAT-activating variants overall | (tefferi2025essentialthrombocythemia pages 1-2) |
| CALR mutation frequency | 23% | General ET population; JAMA review | 2025 | Approximately 90% of patients had JAK-STAT-activating variants overall | (tefferi2025essentialthrombocythemia pages 1-2) |
| MPL mutation frequency | 4% | General ET population; JAMA review | 2025 | Approximately 90% of patients had JAK-STAT-activating variants overall | (tefferi2025essentialthrombocythemia pages 1-2) |
| Triple-negative frequency | ~10% | General ET population; JAMA review | 2025 | Inferred from “approximately 90%” having JAK2/CALR/MPL variants | (tefferi2025essentialthrombocythemia pages 1-2) |
| Arterial thrombosis risk | 11% | General ET population; JAMA review | 2025 | Reported increased risk in ET | (tefferi2025essentialthrombocythemia pages 1-2) |
| Venous thrombosis risk | 7% | General ET population; JAMA review | 2025 | Reported increased risk in ET | (tefferi2025essentialthrombocythemia pages 1-2) |
| Hemorrhagic complication risk | 8% | General ET population; JAMA review | 2025 | Reported increased risk in ET | (tefferi2025essentialthrombocythemia pages 1-2) |
| Arterial thrombosis after diagnosis | 9% | Cohort cited in JAMA review | 2025 | Reported alongside 6% venous thrombosis after diagnosis | (tefferi2025essentialthrombocythemia pages 3-4) |
| Venous thrombosis after diagnosis | 6% | Cohort cited in JAMA review | 2025 | Reported alongside 9% arterial thrombosis after diagnosis | (tefferi2025essentialthrombocythemia pages 3-4) |
| Hemorrhagic events | 7.3% | Review article population estimate | 2024 | Predominantly cutaneous/mucosal or gastrointestinal | (lazar2024diagnosisandmanagement pages 1-3) |
| Myelofibrosis transformation | ~10% | General ET population; JAMA review | 2025 | At median 8.5 years from diagnosis | (tefferi2025essentialthrombocythemia pages 1-2) |
| Acute myeloid leukemia transformation | ~3% | General ET population; JAMA review | 2025 | At median 8.5 years from diagnosis | (tefferi2025essentialthrombocythemia pages 1-2) |
| Myelofibrosis transformation | 4%–11% | Long-term review estimate | 2024 | At 15 years | (lazar2024diagnosisandmanagement pages 1-3) |
| AML transformation | 2%–5% | Long-term review estimate | 2024 | Long-term progression estimate | (lazar2024diagnosisandmanagement pages 1-3) |
| Leukemic transformation | <1% | General ET population; AJH update | 2024 | At 10 years; higher in select JAK2-mutated or karyotype-abnormal cases | (tefferi2024essentialthrombocythemia2024 pages 1-2) |
| Median overall survival | ~18 years | General ET population; AJH update | 2024 | Review estimate | (tefferi2024essentialthrombocythemia2024 pages 1-2) |
| Median overall survival | >35 years | Patients diagnosed at age ≤40 years; JAMA review | 2025 | Survival exceeds 35 years in younger patients | (tefferi2025essentialthrombocythemia pages 1-2) |
| Median survival range | 10 years to not reached | Mayo Clinic ET cohort risk models | 2024 | HR-based risk models | (gangat2024onethousandpatients pages 1-2) |
| 20-year leukemia incidence | 3% to 12.8% | Mayo Clinic ET cohort risk models | 2024 | Across model-defined risk groups | (gangat2024onethousandpatients pages 1-2) |
| 20-year myelofibrosis incidence | 21% to 49% | Mayo Clinic ET cohort risk models | 2024 | Across model-defined risk groups | (gangat2024onethousandpatients pages 1-2) |


*Table: This table compiles key quantitative epidemiology, mutation frequency, thrombosis/bleeding risk, transformation, and survival data for essential thrombocythemia from the retrieved evidence. It is useful for quickly comparing population-level estimates with large real-world Mayo and Florence 1000-patient cohorts.*

### 4.3 Pathogenic variant classes (high-level)
- **JAK2V617F** is a gain-of-function driver in ET and is “JAK2 mutation-prevalent” in ET (tefferi2024essentialthrombocythemia2024 pages 2-2, tefferi2024essentialthrombocythemia2024 pages 1-2).
- **CALR** mutations in ET are typically **frameshift variants in exon 9** (type 1/type 2) that activate MPL/JAK–STAT (tefferi2024essentialthrombocythemia2024 pages 2-2).
- **MPL** mutations include W515 variants and other activating lesions (tefferi2024essentialthrombocythemia2024 pages 2-2).

### 4.4 Modifier/co-mutations and prognostic implications
- The AJH 2024 update reports frequent additional mutations (e.g., TET2 9–11%, ASXL1 7–20%, DNMT3A 7%, SF3B1 5%) and links certain lesions to clinical trajectories (e.g., TP53 with leukemic transformation; spliceosome mutations with inferior survival; MPL/CALR-1 with MF transformation risk) (tefferi2024essentialthrombocythemia2024 pages 1-2).

### 4.5 Epigenetic and chromosomal abnormalities
- Abnormal karyotype appears in **<10%** of patients in the AJH 2024 update (tefferi2024essentialthrombocythemia2024 pages 1-2), and **6%** in the Mayo 1,000 cohort (gangat2024onethousandpatients pages 1-2).

---

## 5. Environmental Information

No specific environmental toxins, lifestyle exposures, or infectious triggers were captured as causal contributors in the retrieved ET-focused evidence. ET risk/complications are clinically influenced by cardiovascular risk factors (e.g., hypertension, diabetes), but these are generally modeled as modifiers of thrombotic risk rather than etiologic exposures (tefferi2025essentialthrombocythemia pages 1-2, gangat2024onethousandpatients pages 1-2).

---

## 6. Mechanism / Pathophysiology

### 6.1 Core causal chain (driver mutation → signaling → megakaryopoiesis → clinical events)
1. **Somatic driver mutation** in JAK2/CALR/MPL occurs in a hematopoietic stem/progenitor clone (clonal hematopoiesis) (tefferi2024essentialthrombocythemia2024 pages 2-2).
2. Driver mutations **activate JAK–STAT signaling** and increase megakaryocyte/platelet production.
   - JAMA review: driver variants “**upregulate the JAK-STAT**” pathway and “**bypass[] the need for growth factor ligands… which stimulate myeloproliferation and megakaryocyte production**” (tefferi2025essentialthrombocythemia pages 1-2).
   - AJH 2024 update: JAK2V617F exerts “**a primary effect on platelet production**” and “**development of the ET phenotype**” (tefferi2024essentialthrombocythemia2024 pages 2-2).
3. Clinical manifestations arise from:
   - **Thrombosis** (arterial/venous), influenced by mutation status (especially JAK2), age, and cardiovascular risk factors (tefferi2025essentialthrombocythemia pages 1-2, tefferi2024essentialthrombocythemia2024 pages 1-2).
   - **Bleeding**, particularly when extreme thrombocytosis is associated with **acquired von Willebrand factor defects** (venkat2024riskofbleeding pages 3-4).
   - **Long-term clonal evolution** with additional mutations leading to MF/AML transformation in a minority (tefferi2025essentialthrombocythemia pages 1-2, tefferi2024essentialthrombocythemia2024 pages 1-2).

### 6.2 Mechanistic notes: CALR and MPL
- AJH 2024 update summarizes a mechanism for mutant CALR: mutant CALR can bind MPL, promote MPL dimerization/trafficking, and activate JAK–STAT (tefferi2024essentialthrombocythemia2024 pages 2-2).

### 6.3 Inflammation and non-driver mutations
- AJH 2024 update notes “**co-existence of an inflammatory state with aberrant cytokine expression**” and that phenotype is modified by “**other co-occurring mutations, including those of epigenetic regulators and their order of acquisition**” (tefferi2024essentialthrombocythemia2024 pages 2-2).
- It also cautions that “**activated JAK–STAT is a non-specific phenomenon in cancer**,” and that JAK inhibitors have not selectively suppressed the ET clone in general, reflecting biologic complexity (tefferi2024essentialthrombocythemia2024 pages 2-2).

### 6.4 Suggested pathway / ontology terms
- **GO (biological process):** JAK-STAT cascade (e.g., “JAK-STAT signaling pathway”); “megakaryocyte differentiation”; “platelet production”; “inflammatory response”. (Ontology suggestions; not directly asserted by retrieved evidence.)
- **CL (cell types):** hematopoietic stem cell; megakaryocyte; megakaryocyte progenitor. (Ontology suggestions.)

---

## 7. Anatomical Structures Affected

### 7.1 Primary
- **Bone marrow**: characteristic megakaryocytic proliferation and clustering on biopsy (tefferi2024essentialthrombocythemia2024 pages 4-5, loscocco2024onethousandpatients pages 1-2).

### 7.2 Secondary (complication targets)
- Vascular beds and organs affected by thrombosis/bleeding (brain, coronary circulation, venous system) are clinically relevant (stroke/thrombotic events are referenced as manifestations) (lazar2024diagnosisandmanagement pages 1-3, tefferi2025essentialthrombocythemia pages 1-2).

### 7.3 Suggested anatomy ontology terms
- **UBERON:** bone marrow; blood; vasculature. (Ontology suggestions.)

---

## 8. Temporal Development

- **Onset:** typically adult; median age at diagnosis ~59 years (tefferi2025essentialthrombocythemia pages 1-2).
- **Course:** often indolent, interrupted by thrombotic/hemorrhagic events; transformation to MF/AML occurs in a minority (tefferi2024essentialthrombocythemia2024 pages 1-2).
- **Progression statistics:** JAMA review reports ~10% MF and ~3% AML at median 8.5 years (tefferi2025essentialthrombocythemia pages 1-2).

---

## 9. Inheritance and Population

### 9.1 Inheritance
ET is principally a **somatic clonal hematopoietic** disease driven by acquired mutations in hematopoietic stem/progenitor cells; a Mendelian inheritance pattern was not supported by the retrieved evidence (tefferi2024essentialthrombocythemia2024 pages 2-2, tefferi2024essentialthrombocythemia2024 pages 1-2).

### 9.2 Epidemiology (recent statistics)
- Annual incidence estimates:
  - **US annual incidence 1.5/100,000** (JAMA review) (tefferi2025essentialthrombocythemia pages 1-2).
  - Review estimate **0.6–2.5/100,000/year** (BJH 2024 review) (ferrer‐marin2024essentialthrombocythaemiaa pages 1-2).
- Prevalence estimate (review): **38–57/100,000** (lazar2024diagnosisandmanagement pages 1-3).
- Sex distribution: ~63–65% female in two large 2024 cohorts (gangat2024onethousandpatients pages 1-2, loscocco2024onethousandpatients pages 1-2).

---

## 10. Diagnostics

### 10.1 Diagnostic criteria (WHO/ICC-aligned core elements)
The AJH 2024 update reproduces the ICC framework: diagnosis requires “**meeting all four major criteria or meeting the first three major criteria plus one minor criterion**” (tefferi2024essentialthrombocythemia2024 pages 4-5). Major criteria elements include:
1. **Platelets ≥450 ×10^9/L** (tefferi2024essentialthrombocythemia2024 pages 4-5).
2. Bone marrow: **megakaryocyte proliferation with mature cytology/hyperlobulated nuclei**, **loose clustering**, and **absent or ≤ grade 1 fibrosis** (tefferi2024essentialthrombocythemia2024 pages 4-5).
3. Exclusion of other myeloid neoplasms (including PV, prefibrotic MF, CML) (tefferi2024essentialthrombocythemia2024 pages 4-5).
4. Presence of driver mutation **JAK2/CALR/MPL** (tefferi2024essentialthrombocythemia2024 pages 4-5).

Bone marrow morphology emphasized in practice includes normocellularity for age, increased mature megakaryocytes in loose clusters, and reticulin fibrosis < grade 1 (loscocco2024onethousandpatients pages 1-2).

### 10.2 Differential diagnosis (key exclusions)
Differential diagnoses include other MPNs and reactive thrombocytosis:
- JAMA review lists PV, primary myelofibrosis, CML, inflammatory conditions, infections, splenectomy, iron deficiency anemia, and solid tumors among differentials (tefferi2025essentialthrombocythemia pages 1-2).

### 10.3 Recommended molecular testing
WHO/ICC-aligned approaches emphasize driver mutation testing for JAK2/CALR/MPL (thiele2025evolutionofwho pages 3-4, tefferi2024essentialthrombocythemia2024 pages 4-5).

### 10.4 Suggested diagnostic ontology terms
- **LOINC/measurement:** platelet count; vWF activity/antigen when assessing bleeding/AvWS (venkat2024riskofbleeding pages 3-4).

---

## 11. Outcome / Prognosis

### 11.1 Survival and transformation
- AJH 2024 update: median survival ~**18 years**, and notes survival “**>>35 years in younger patients**” (tefferi2024essentialthrombocythemia2024 pages 1-2).
- JAMA review: “**The median overall survival exceeds 35 years in those diagnosed at 40 years or younger**” (tefferi2025essentialthrombocythemia pages 1-2).
- JAMA review: at median 8.5 years, **~10% MF** and **~3% AML** (tefferi2025essentialthrombocythemia pages 1-2).
- AJH 2024 update: leukemic transformation at 10 years is **<1%** overall (tefferi2024essentialthrombocythemia2024 pages 1-2).

### 11.2 Thrombosis and bleeding burden (recently summarized)
- JAMA review reports ET patients are at increased risk of **arterial thrombosis (11%)**, **venous thrombosis (7%)**, and **hemorrhagic complications (8%)** (tefferi2025essentialthrombocythemia pages 1-2).
- Cohort-based risk models in Mayo 1,000-patient series delineated 20-year leukemia/myelofibrosis incidences ranging **3%/21% to 12.8%/49%** across risk groups (gangat2024onethousandpatients pages 1-2).

---

## 12. Treatment

### 12.1 Treatment goals and strategy (risk-adapted, real-world)
The AJH 2024 update frames ET therapy around **thrombosis prevention**, using risk groups incorporating thrombosis history, age, and JAK2 status (tefferi2024essentialthrombocythemia2024 pages 1-2).

**Figure-based algorithm (visual evidence)**
- The AJH 2024 update provides a treatment algorithm stratifying “very low / low / intermediate / high” risk and selecting observation vs aspirin vs cytoreduction (tefferi2024essentialthrombocythemia2024 media 9b23e152).

### 12.2 Antiplatelet therapy (aspirin)
- AJH 2024 update: aspirin is a baseline therapy and should be monitored closely when extreme thrombocytosis/AvWS is present (tefferi2024essentialthrombocythemia2024 pages 11-11, tefferi2024essentialthrombocythemia2024 pages 10-11).
- Aspirin dosing considerations: increased platelet turnover may lead to incomplete inhibition with once-daily dosing; AJH 2024 reports BID/TID regimens reduce platelet activation more than QD (tefferi2024essentialthrombocythemia2024 pages 11-12).
- In the Mayo 1,000 cohort, aspirin therapy “**appeared to mitigate both arterial (HR 0.4) and venous (HR 0.4) thrombosis risk**” (gangat2024onethousandpatients pages 1-2).

**MAXO suggestion:** antiplatelet therapy.

### 12.3 Cytoreductive therapy (standard of care in high-risk ET)
- AJH 2024 update: **hydroxyurea** is current **first-line cytoreduction** in high-risk ET (tefferi2024essentialthrombocythemia2024 pages 10-11).
- Second-line: “**pegylated IFN‑α or busulfan**” in hydroxyurea-intolerant/refractory patients (tefferi2024essentialthrombocythemia2024 pages 11-11).
- AJH 2024 update reports randomized comparisons with **anagrelide**, noting different profiles: hydroxyurea reduced arterial thrombosis/major bleeding/fibrotic progression, while anagrelide was better at preventing venous thrombosis but had higher adverse-event dropout (tefferi2024essentialthrombocythemia2024 pages 12-13).

**MAXO suggestions:** cytoreductive therapy; interferon therapy.

### 12.4 Managing extreme thrombocytosis and bleeding risk (2024 evidence update)
A key 2024 development is more granular evidence on bleeding in ET with extreme thrombocytosis (ExT).
- Venkat et al. (Blood Adv. Dec 2024) concludes: “**There is no clear indication for cytoreduction to decrease bleeding risk based on a platelet threshold of 1 million alone**” (abstract key points) (venkat2024riskofbleeding pages 1-2).
- The same study reports ExT is associated with lower vWF antigen/activity, consistent with acquired vWF abnormalities (venkat2024riskofbleeding pages 3-4).
- AJH 2024 emphasizes that platelet extremes alone do not necessarily increase thrombosis/hemorrhage risk, and that therapy modification is mainly warranted when ExT is accompanied by AvWS (tefferi2024essentialthrombocythemia2024 pages 11-12).

### 12.5 Targeted and emerging therapies (2023–2024 landscape)

**Ruxolitinib (JAK1/2 inhibitor; selected settings)**
- 2024 BJH review summarizes that in hydroxyurea-resistant/intolerant ET, ruxolitinib improved some symptoms but did **not** reduce thrombosis/bleeding/transformation and did not show superiority over best available therapy (MAJIC-ET) (ferrer‐marin2024essentialthrombocythaemiaa pages 7-8).
- Earlier ET-specific review similarly notes superiority mainly in symptom control vs conventional therapy (gunawan2018ruxolitinibforthe pages 1-2).

**Bomedemstat (LSD1 inhibitor; emerging therapy)**
- AJH 2024 update: bomedemstat is “**an orally active LSD1 inhibitor**” and in a phase 2 study (NCT04254978) achieved platelet response (≤400×10^9/L) in **94%** with median time to response **8 weeks**; common AEs included dysgeusia (43%), constipation (27%), fatigue (23%), thrombocytopenia (23%), and discontinuation ~20% (tefferi2024essentialthrombocythemia2024 pages 17-17).
- Phase 3 registry trial: **NCT06079879** compares bomedemstat vs best available therapy in HU inadequate response/intolerant ET; start date 2023‑12‑31; planned enrollment 340; primary endpoint durable clinicohematologic response by week 52 (NCT06079879 chunk 1).

**Ropeginterferon alfa-2b (phase 3 trial in ET)**
- SURPASS-ET registry trial: **NCT04285086** is an open-label, randomized, phase 3 study comparing ropeginterferon alfa‑2b vs anagrelide in HU-resistant/intolerant ET; enrollment 174; primary outcomes include blood count remission, symptom improvement, and absence of thrombotic/hemorrhagic events (NCT04285086 chunk 1).

**MAXO suggestions:** interferon therapy; JAK inhibitor therapy; histone demethylase inhibitor therapy.

---

## 13. Prevention

No primary-prevention interventions were captured (ET is primarily somatic clonal disease). Secondary/tertiary prevention focuses on prevention of thrombosis/bleeding complications via risk-adapted antiplatelet therapy and cytoreduction (tefferi2024essentialthrombocythemia2024 pages 1-2, ferrer‐marin2024essentialthrombocythaemiaa pages 3-4).

---

## 14. Other Species / Natural Disease

No naturally occurring animal disease evidence for ET was captured in the retrieved sources for this report.

---

## 15. Model Organisms

While mechanistic statements reference preclinical support for mutant CALR/MPL biology, specific model organism systems and phenotypes were not captured in the retrieved evidence excerpts (tefferi2024essentialthrombocythemia2024 pages 2-2).

---

# Notes on evidence gaps and curation constraints
- **Ontology codes** (MONDO/MeSH/ICD/OMIM/Orphanet) were **not present in the retrieved excerpts**, so this report explicitly flags them as “not captured in retrieved sources” rather than guessing (artifact-00).
- **PMIDs** were not provided in the retrieved text snippets; therefore, the report cites DOI/URL-bearing sources as retrieved by the tool. Where the user requires PMIDs, additional database-specific retrieval would be needed.

# Visual evidence (treatment algorithm)
- ET treatment algorithm figure from the AJH 2024 update: (tefferi2024essentialthrombocythemia2024 media 9b23e152).

References

1. (loscocco2024onethousandpatients pages 1-2): Giuseppe G. Loscocco, Francesca Gesullo, Giulio Capecchi, Alessandro Atanasio, Chiara Maccari, Francesco Mannelli, Alessandro M. Vannucchi, and Paola Guglielmelli. One thousand patients with essential thrombocythemia: the florence-crimm experience. Blood Cancer Journal, Jan 2024. URL: https://doi.org/10.1038/s41408-023-00968-7, doi:10.1038/s41408-023-00968-7. This article has 43 citations and is from a domain leading peer-reviewed journal.

2. (ferrer‐marin2024essentialthrombocythaemiaa pages 1-2): Francisca Ferrer‐Marín, Juan Carlos Hernández‐Boluda, and Alberto Alvarez‐Larrán. Essential thrombocythaemia: a contemporary approach with new drugs on the horizon. British Journal of Haematology, 204:1605-1616, Apr 2024. URL: https://doi.org/10.1111/bjh.19403, doi:10.1111/bjh.19403. This article has 7 citations and is from a domain leading peer-reviewed journal.

3. (tefferi2024essentialthrombocythemia2024 pages 1-2): Ayalew Tefferi, Alessandro Maria Vannucchi, and Tiziano Barbui. Essential thrombocythemia: 2024 update on diagnosis, risk stratification, and management. American Journal of Hematology, 99:697-718, Jan 2024. URL: https://doi.org/10.1002/ajh.27216, doi:10.1002/ajh.27216. This article has 141 citations and is from a domain leading peer-reviewed journal.

4. (tefferi2025essentialthrombocythemia pages 1-2): Ayalew Tefferi, Naseema Gangat, Giuseppe Gaetano Loscocco, Paola Guglielmelli, Natasha Szuber, Animesh Pardanani, Attilio Orazi, Tiziano Barbui, and Alessandro Maria Vannucchi. Essential thrombocythemia. JAMA, 333:701, Feb 2025. URL: https://doi.org/10.1001/jama.2024.25349, doi:10.1001/jama.2024.25349. This article has 22 citations.

5. (gangat2024onethousandpatients pages 1-2): Naseema Gangat, Omer Karrar, Aref Al-Kali, Kebede H. Begna, Michelle A. Elliott, Alexandra P. Wolanskyj-Spinner, Animesh Pardanani, Curtis A. Hanson, Rhett P. Ketterling, and Ayalew Tefferi. One thousand patients with essential thrombocythemia: the mayo clinic experience. Blood Cancer Journal, Jan 2024. URL: https://doi.org/10.1038/s41408-023-00972-x, doi:10.1038/s41408-023-00972-x. This article has 57 citations and is from a domain leading peer-reviewed journal.

6. (venkat2024riskofbleeding pages 1-2): Rathnam K. Venkat, Robert A. Redd, Amyah C. Harris, Martin J. Aryee, Anna E. Marneth, Baransel Kamaz, Chulwoo J. Kim, Mohammed Wazir, Lachelle D. Weeks, Maximilian Stahl, Daniel J. DeAngelo, R. Coleman Lindsley, Marlise R. Luskin, Gabriela S. Hobbs, and Joan How. Risk of bleeding in patients with essential thrombocythemia and extreme thrombocytosis. Blood Advances, 8:6043-6054, Dec 2024. URL: https://doi.org/10.1182/bloodadvances.2024013777, doi:10.1182/bloodadvances.2024013777. This article has 10 citations and is from a peer-reviewed journal.

7. (tefferi2024essentialthrombocythemia2024 pages 4-5): Ayalew Tefferi, Alessandro Maria Vannucchi, and Tiziano Barbui. Essential thrombocythemia: 2024 update on diagnosis, risk stratification, and management. American Journal of Hematology, 99:697-718, Jan 2024. URL: https://doi.org/10.1002/ajh.27216, doi:10.1002/ajh.27216. This article has 141 citations and is from a domain leading peer-reviewed journal.

8. (thiele2025evolutionofwho pages 3-3): Jürgen Thiele, Hans Michael Kvasnicka, Umberto Gianelli, Daniel A. Arber, Ayalew Tefferi, Alessandro M. Vannucchi, Tiziano Barbui, and Attilio Orazi. Evolution of who diagnostic criteria in “classical myeloproliferative neoplasms” compared with the international consensus classification. Blood Cancer Journal, Mar 2025. URL: https://doi.org/10.1038/s41408-025-01235-7, doi:10.1038/s41408-025-01235-7. This article has 9 citations and is from a domain leading peer-reviewed journal.

9. (allen2022thrombocytosisandessential pages 5-6): Julie Allen and Tracy Stokol. Thrombocytosis and essential thrombocythemia. Schalm's Veterinary Hematology, pages 721-730, Mar 2022. URL: https://doi.org/10.1002/9781119500537.ch82, doi:10.1002/9781119500537.ch82. This article has 7 citations.

10. (tefferi2024essentialthrombocythemia2024 pages 2-2): Ayalew Tefferi, Alessandro Maria Vannucchi, and Tiziano Barbui. Essential thrombocythemia: 2024 update on diagnosis, risk stratification, and management. American Journal of Hematology, 99:697-718, Jan 2024. URL: https://doi.org/10.1002/ajh.27216, doi:10.1002/ajh.27216. This article has 141 citations and is from a domain leading peer-reviewed journal.

11. (ferrer‐marin2024essentialthrombocythaemiaa pages 4-5): Francisca Ferrer‐Marín, Juan Carlos Hernández‐Boluda, and Alberto Alvarez‐Larrán. Essential thrombocythaemia: a contemporary approach with new drugs on the horizon. British Journal of Haematology, 204:1605-1616, Apr 2024. URL: https://doi.org/10.1111/bjh.19403, doi:10.1111/bjh.19403. This article has 7 citations and is from a domain leading peer-reviewed journal.

12. (venkat2024riskofbleeding pages 3-4): Rathnam K. Venkat, Robert A. Redd, Amyah C. Harris, Martin J. Aryee, Anna E. Marneth, Baransel Kamaz, Chulwoo J. Kim, Mohammed Wazir, Lachelle D. Weeks, Maximilian Stahl, Daniel J. DeAngelo, R. Coleman Lindsley, Marlise R. Luskin, Gabriela S. Hobbs, and Joan How. Risk of bleeding in patients with essential thrombocythemia and extreme thrombocytosis. Blood Advances, 8:6043-6054, Dec 2024. URL: https://doi.org/10.1182/bloodadvances.2024013777, doi:10.1182/bloodadvances.2024013777. This article has 10 citations and is from a peer-reviewed journal.

13. (tefferi2024essentialthrombocythemia2024 pages 11-11): Ayalew Tefferi, Alessandro Maria Vannucchi, and Tiziano Barbui. Essential thrombocythemia: 2024 update on diagnosis, risk stratification, and management. American Journal of Hematology, 99:697-718, Jan 2024. URL: https://doi.org/10.1002/ajh.27216, doi:10.1002/ajh.27216. This article has 141 citations and is from a domain leading peer-reviewed journal.

14. (lazar2024diagnosisandmanagement pages 1-3): Sandra LAZAR, Despina Calamar POPOVICI, Oana SARAU, Hortensia IONITA, Claudiu Octavian IONITA, Dacian Nicolae OROS, and Ioana IONITA. Diagnosis and management of essential thrombocythemia: a comprehensive review. Documenta Haematologica - Revista Romana de Hematologie, 2:125-134, Oct 2024. URL: https://doi.org/10.59854/dhrrh.2024.2.3.125, doi:10.59854/dhrrh.2024.2.3.125. This article has 1 citations.

15. (gunawan2018ruxolitinibforthe pages 1-2): Arief Gunawan, Patrick Harrington, Natalia Garcia‐Curto, Donal McLornan, Deepti Radia, and Claire Harrison. Ruxolitinib for the treatment of essential thrombocythemia. HemaSphere, Aug 2018. URL: https://doi.org/10.1097/hs9.0000000000000056, doi:10.1097/hs9.0000000000000056. This article has 29 citations and is from a peer-reviewed journal.

16. (ferrer‐marin2024essentialthrombocythaemiaa pages 7-8): Francisca Ferrer‐Marín, Juan Carlos Hernández‐Boluda, and Alberto Alvarez‐Larrán. Essential thrombocythaemia: a contemporary approach with new drugs on the horizon. British Journal of Haematology, 204:1605-1616, Apr 2024. URL: https://doi.org/10.1111/bjh.19403, doi:10.1111/bjh.19403. This article has 7 citations and is from a domain leading peer-reviewed journal.

17. (tefferi2025essentialthrombocythemia pages 3-4): Ayalew Tefferi, Naseema Gangat, Giuseppe Gaetano Loscocco, Paola Guglielmelli, Natasha Szuber, Animesh Pardanani, Attilio Orazi, Tiziano Barbui, and Alessandro Maria Vannucchi. Essential thrombocythemia. JAMA, 333:701, Feb 2025. URL: https://doi.org/10.1001/jama.2024.25349, doi:10.1001/jama.2024.25349. This article has 22 citations.

18. (thiele2025evolutionofwho pages 3-4): Jürgen Thiele, Hans Michael Kvasnicka, Umberto Gianelli, Daniel A. Arber, Ayalew Tefferi, Alessandro M. Vannucchi, Tiziano Barbui, and Attilio Orazi. Evolution of who diagnostic criteria in “classical myeloproliferative neoplasms” compared with the international consensus classification. Blood Cancer Journal, Mar 2025. URL: https://doi.org/10.1038/s41408-025-01235-7, doi:10.1038/s41408-025-01235-7. This article has 9 citations and is from a domain leading peer-reviewed journal.

19. (tefferi2024essentialthrombocythemia2024 media 9b23e152): Ayalew Tefferi, Alessandro Maria Vannucchi, and Tiziano Barbui. Essential thrombocythemia: 2024 update on diagnosis, risk stratification, and management. American Journal of Hematology, 99:697-718, Jan 2024. URL: https://doi.org/10.1002/ajh.27216, doi:10.1002/ajh.27216. This article has 141 citations and is from a domain leading peer-reviewed journal.

20. (tefferi2024essentialthrombocythemia2024 pages 10-11): Ayalew Tefferi, Alessandro Maria Vannucchi, and Tiziano Barbui. Essential thrombocythemia: 2024 update on diagnosis, risk stratification, and management. American Journal of Hematology, 99:697-718, Jan 2024. URL: https://doi.org/10.1002/ajh.27216, doi:10.1002/ajh.27216. This article has 141 citations and is from a domain leading peer-reviewed journal.

21. (tefferi2024essentialthrombocythemia2024 pages 11-12): Ayalew Tefferi, Alessandro Maria Vannucchi, and Tiziano Barbui. Essential thrombocythemia: 2024 update on diagnosis, risk stratification, and management. American Journal of Hematology, 99:697-718, Jan 2024. URL: https://doi.org/10.1002/ajh.27216, doi:10.1002/ajh.27216. This article has 141 citations and is from a domain leading peer-reviewed journal.

22. (tefferi2024essentialthrombocythemia2024 pages 12-13): Ayalew Tefferi, Alessandro Maria Vannucchi, and Tiziano Barbui. Essential thrombocythemia: 2024 update on diagnosis, risk stratification, and management. American Journal of Hematology, 99:697-718, Jan 2024. URL: https://doi.org/10.1002/ajh.27216, doi:10.1002/ajh.27216. This article has 141 citations and is from a domain leading peer-reviewed journal.

23. (tefferi2024essentialthrombocythemia2024 pages 17-17): Ayalew Tefferi, Alessandro Maria Vannucchi, and Tiziano Barbui. Essential thrombocythemia: 2024 update on diagnosis, risk stratification, and management. American Journal of Hematology, 99:697-718, Jan 2024. URL: https://doi.org/10.1002/ajh.27216, doi:10.1002/ajh.27216. This article has 141 citations and is from a domain leading peer-reviewed journal.

24. (NCT06079879 chunk 1):  A Study of Bomedemstat (IMG-7289/MK-3543) Compared to Best Available Therapy (BAT) in Participants With Essential Thrombocythemia and an Inadequate Response or Intolerance of Hydroxyurea (MK-3543-006). Merck Sharp & Dohme LLC. 2023. ClinicalTrials.gov Identifier: NCT06079879

25. (NCT04285086 chunk 1):  Ropeginterferon Alfa-2b (P1101) vs. Anagrelide in Essential Thrombocythemia Patients With Hydroxyurea Resistance or Intolerance. PharmaEssentia. 2020. ClinicalTrials.gov Identifier: NCT04285086

26. (ferrer‐marin2024essentialthrombocythaemiaa pages 3-4): Francisca Ferrer‐Marín, Juan Carlos Hernández‐Boluda, and Alberto Alvarez‐Larrán. Essential thrombocythaemia: a contemporary approach with new drugs on the horizon. British Journal of Haematology, 204:1605-1616, Apr 2024. URL: https://doi.org/10.1111/bjh.19403, doi:10.1111/bjh.19403. This article has 7 citations and is from a domain leading peer-reviewed journal.
