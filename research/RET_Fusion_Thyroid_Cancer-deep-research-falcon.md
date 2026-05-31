---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T22:01:02.710283'
end_time: '2026-04-05T22:15:49.841136'
duration_seconds: 887.13
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: RET Fusion-Positive Thyroid Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 55
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RET Fusion-Positive Thyroid Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **RET Fusion-Positive Thyroid Cancer** covering all of the
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
- **Disease Name:** RET Fusion-Positive Thyroid Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **RET Fusion-Positive Thyroid Cancer** covering all of the
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


# RET Fusion‑Positive Thyroid Cancer — Disease Characteristics Research Report

**Target disease:** RET fusion‑positive thyroid cancer (molecularly defined subset; most commonly RET fusion‑positive papillary thyroid carcinoma [PTC]) (duke2023fdaapprovalsummary pages 1-3, pekova2023retfusiongenes pages 1-2).  
**Category:** Molecular subtype of differentiated thyroid carcinoma / papillary thyroid carcinoma (duke2023fdaapprovalsummary pages 1-3, pekova2023retfusiongenes pages 1-2).  
**MONDO ID:** A specific MONDO term for “RET fusion‑positive thyroid cancer” was not identified in the retrieved sources; related thyroid cancer MONDO terms exist for other entities (e.g., medullary thyroid gland carcinoma MONDO_0015277, which is typically RET mutation‑driven, not RET fusion‑driven) (parimi2023genomiclandscapeof pages 1-2).

## Executive summary
RET fusion‑positive thyroid cancers are thyroid epithelial malignancies driven by oncogenic RET gene rearrangements (RET/PTC). The fusions typically retain the RET kinase domain and use partner‑derived dimerization motifs to enable ligand‑independent RET activation and downstream MAPK/PI3K pathway signaling. RET fusions are enriched in pediatric PTC and in aggressive histologic variants (e.g., diffuse sclerosing PTC), and are associated with high rates of lymph node metastasis and meaningful distant metastasis risk. Clinically, selective RET inhibitors (selpercatinib, pralsetinib) have produced high objective response rates and durable disease control in advanced RET fusion‑positive thyroid cancer, and have become the key real‑world implementation of precision oncology for this subtype (wirth2024durabilityofresponse pages 1-2, clark2023selectiveretinhibitors pages 4-5, pekova2023retfusiongenes pages 1-2).

## 1. Disease Information

### 1.1 Definition and overview
RET fusion‑positive thyroid cancer refers to thyroid carcinomas harboring in‑frame chromosomal rearrangements involving RET that generate constitutively active RET fusion oncoproteins (duke2023fdaapprovalsummary pages 3-5). These fusions are most commonly observed in papillary thyroid cancer and are rare across most other solid tumors (duke2023fdaapprovalsummary pages 1-3).

### 1.2 Key identifiers and ontology mappings
* **Clinical/diagnostic context:** RET fusions are molecular alterations in thyroid cancer and are used as predictive biomarkers for RET‑directed therapy selection (carneiro2024predictivebiomarkersin pages 8-9).
* **MeSH/ICD/Orphanet:** Specific IDs were not retrieved in the available sources for the molecular subtype.
* **MONDO:** No specific MONDO term for the molecular subtype was retrieved (see above).

### 1.3 Synonyms and alternative names
* **RET‑rearranged thyroid cancer** (desilets2023retalteredcancers—atumoragnostic pages 13-15)  
* **RET fusion‑positive thyroid cancer** (wirth2024durabilityofresponse pages 1-2)  
* **RET/PTC (RET fusion)–positive papillary thyroid carcinoma** (pekova2023retfusiongenes pages 1-2)  
* Specific historical fusion labels: **RET/PTC1 (CCDC6::RET)**, **RET/PTC3 (NCOA4::RET)** (pekova2023retfusiongenes pages 3-5).

### 1.4 Evidence source type
Evidence in this report is derived from aggregated disease‑level resources including multi‑institution cohorts, pan‑tumor NGS datasets, clinical trials (LIBRETTO‑001, ARROW), ClinicalTrials.gov trial records, and FDA regulatory reviews (parimi2023genomiclandscapeof pages 1-2, wirth2024durabilityofresponse pages 1-2, duke2023fdaapprovalsummary pages 1-3, NCT03157128 chunk 1).

## 2. Etiology

### 2.1 Disease causal factors
The primary causal factor is an acquired **somatic RET gene fusion** (RET rearrangement), which creates an oncogenic fusion protein with constitutive kinase activation (desilets2023retalteredcancers—atumoragnostic pages 2-4, pekova2023retfusiongenes pages 11-12).

### 2.2 Risk factors
**Age / pediatric enrichment:** In a large cohort (n=993 PTC), RET fusions were detected in **11.4%** of PTC overall, and were **threefold more frequent** in pediatric/adolescent patients (**29.8%**) than adults (**8.7%**) (Pekova 2023; published Sep 2023; https://doi.org/10.1530/ERC-23-0117) (pekova2023retfusiongenes pages 1-2).  
**Radiation exposure:** RET/PTC events have been linked to ionizing radiation exposure and radiation‑associated subtypes in thyroid cancer literature (e.g., post‑Chernobyl series and “short radiation latency” associations noted in a 2023 Thai PTC study) (Khonrak 2023; published Apr 2023; https://doi.org/10.3389/pore.2023.1611138) (khonrak2023retrearrangementsare pages 1-2, khonrak2023retrearrangementsare pages 13-13).  

### 2.3 Protective factors
No clear protective genetic or environmental factors specific to acquiring RET fusions were identified in the retrieved sources. One cohort cited an association between coexisting chronic lymphocytic thyroiditis and lower recurrence rates in PTC broadly, but this is not a proven protective factor for RET‑fusion initiation (pekova2023retfusiongenes pages 12-13).

### 2.4 Gene–environment interactions
The strongest candidate interaction is DNA damage (e.g., radiation) contributing to chromosomal rearrangements that generate RET/PTC fusions, as discussed in the radiation‑associated literature summarized in Thai PTC data and cited post‑Chernobyl series (khonrak2023retrearrangementsare pages 13-13).

## 3. Phenotypes

### 3.1 Clinical presentation and phenotype spectrum
RET fusion‑positive thyroid cancer is most often PTC and is frequently associated with aggressive locoregional features.

**Aggressive metastatic phenotype (large cohort):** In a large Czech cohort of RET fusion‑positive PTC, **lymph node metastasis occurred in 75.2%** and **distant metastasis in 18.6%**; metastases were also reported even among microcarcinomas (Pekova 2023; https://doi.org/10.1530/ERC-23-0117) (pekova2023retfusiongenes pages 1-2).  

**Diffuse sclerosing PTC enrichment and recurrence risk:** In diffuse sclerosing PTC (DSPTC), RET fusions were the most common alteration (**32% [13/41]**), and RET fusion status predicted worse recurrence‑free survival (**5‑year RFS 46% vs 84%** for other drivers; HR **7.69**, p=0.017) (Scholfield 2024; published Jun 2024; https://doi.org/10.1245/s10434-024-15500-9) (scholfield2024definingthegenomic pages 1-3).  

**Small descriptive cohort:** In a retrospective series of operated nodules, RET/PTC fusion‑positive nodules were all malignant (**100%**) and had a high nodal metastasis rate (**80% [4/5]**), with **60%** diffuse sclerosing variant histology (Tali 2023; published Jun 2023; https://doi.org/10.3390/cancers15133394) (tali2023thedifferencein pages 1-2).

### 3.2 Suggested HPO terms (examples)
* Cervical lymph node metastasis — **HP:0005981** (suggested; aligns with frequent LNM) (pekova2023retfusiongenes pages 1-2)  
* Distant metastasis — **HP:0002664** (suggested) (pekova2023retfusiongenes pages 1-2)  
* Extrathyroidal extension (locally invasive tumor) — **HP:0100836** (suggested; observed in subsets) (tali2023thedifferencein pages 4-6)

### 3.3 Quality of life impact
Direct thyroid‑specific QoL metrics for RET fusion‑positive thyroid cancer were not extracted from the retrieved texts. QoL preservation/improvement under selpercatinib was reported across RET‑driven cancers in LIBRETTO‑001, but thyroid‑specific quantitative QoL outcomes were not available in the extracted evidence (wirth2024durabilityofresponse pages 7-7).

## 4. Genetic / Molecular Information

### 4.1 Causal genes
* **RET** (ret proto‑oncogene), acting as an oncogenic driver via fusion/rearrangement (desilets2023retalteredcancers—atumoragnostic pages 2-4).

### 4.2 Pathogenic variant class
The defining alteration is a **structural rearrangement (gene fusion)** producing an in‑frame **RET fusion** (RET/PTC). Key fusions retain the RET kinase domain (3′ RET) and incorporate a 5′ partner providing dimerization capability (desilets2023retalteredcancers—atumoragnostic pages 2-4, pekova2023retfusiongenes pages 11-12).

### 4.3 Common fusion partners and frequencies
In a large RET fusion‑positive PTC cohort (n=113 RET+ PTCs):  
* **CCDC6::RET**: **59.3% (67/113)**  
* **NCOA4::RET**: **22.1% (25/113)**  
Other partners included FBXO41, SSBP2, ZMYM2 (Pekova 2023; https://doi.org/10.1530/ERC-23-0117) (pekova2023retfusiongenes pages 3-5).

In a pan‑tumor NGS dataset, thyroid papillary carcinoma had RET fusion prevalence **9.09% (109/1199)**, and across the overall RET fusion cohort common partners included **NCOA4 (32.6%)** and **CCDC6 (29.9%)** (Parimi 2023; published Jan 2023; https://doi.org/10.1038/s41698-023-00347-2) (parimi2023genomiclandscapeof pages 1-2).

### 4.4 Mechanism / functional consequences
RET fusions:
1) retain the **RET tyrosine kinase domain** in the 3′ fusion portion;  
2) are placed under control of a transcriptionally active partner; and  
3) often acquire partner‑derived **dimerization motifs**, enabling **ligand‑independent dimerization**, phosphorylation, and constitutive signaling (carneiro2024predictivebiomarkersin pages 8-9, desilets2023retalteredcancers—atumoragnostic pages 2-4).

Downstream pathways include **MAPK‑ERK**, **PI3K‑AKT**, and **JAK‑STAT** signaling, supporting proliferative/survival programs (carneiro2024predictivebiomarkersin pages 8-9, chen2024retinhibitorsin pages 1-3).

### 4.5 Suggested GO biological process terms (examples)
* ERK1/ERK2 cascade — **GO:0070371** (suggested; aligns with MAPK activation) (carneiro2024predictivebiomarkersin pages 8-9)  
* Phosphatidylinositol 3‑kinase signaling — **GO:0014065** (suggested; aligns with PI3K‑AKT) (carneiro2024predictivebiomarkersin pages 8-9)

### 4.6 Suggested Cell Ontology (CL) terms (examples)
* Thyroid follicular cell — **CL:0002262** (suggested; PTC cell of origin)  
* Neoplastic thyroid epithelial cell — not a standard CL term; would be represented as thyroid follicular cell with “neoplastic” context.

## 5. Environmental Information

### 5.1 Environmental factors
Ionizing radiation exposure has a longstanding association with RET/PTC rearrangements (notably pediatric and post‑radiation clusters), summarized in contemporary PTC literature and referenced in 2023 Thai PTC analysis (khonrak2023retrearrangementsare pages 1-2, khonrak2023retrearrangementsare pages 13-13).

### 5.2 Lifestyle factors / infectious agents
No specific lifestyle or infectious etiologies were identified in the retrieved sources.

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (driver → pathway → phenotype)
**Trigger/event:** Somatic chromosomal rearrangement generating an in‑frame RET fusion (RET/PTC).  
**Upstream mechanism:** Fusion retains the RET kinase domain and partner‑derived interaction motifs → ligand‑independent dimerization and RET autophosphorylation (desilets2023retalteredcancers—atumoragnostic pages 2-4, pekova2023retfusiongenes pages 11-12).  
**Downstream signaling:** Activation of MAPK‑ERK and PI3K‑AKT (and JAK‑STAT) cascades promotes proliferation, survival, migration, and oncogenic transformation (carneiro2024predictivebiomarkersin pages 8-9, chen2024retinhibitorsin pages 1-3).  
**Clinical phenotype:** Higher probability of nodal metastasis and clinically aggressive variants (DSPTC association), with high disease‑specific survival in intensively treated cohorts but higher recurrence risk in certain subtypes (scholfield2024definingthegenomic pages 1-3, pekova2023retfusiongenes pages 1-2).

### 6.2 Immune system involvement
Evidence linking RET alterations to immune microenvironment changes in PTC exists (RET variation associated with immune infiltration patterns), but this was not specific to RET fusions and is not used here as defining evidence for RET fusion‑positive disease (pekova2023retfusiongenes pages 1-2).

### 6.3 Molecular profiling
Comprehensive multi‑omics signatures specific to RET fusion‑positive thyroid cancer were not extracted in the available sources.

## 7. Anatomical Structures Affected

### 7.1 Organ and tissue level
* Primary organ: **thyroid gland** (UBERON:0002046; suggested).  
* Frequent regional spread: cervical lymph nodes (supported by high LNM rates) (pekova2023retfusiongenes pages 1-2).

### 7.2 Suggested UBERON terms (examples)
* Thyroid gland — **UBERON:0002046**  
* Cervical lymph node — **UBERON:0002509** (suggested)  

## 8. Temporal Development

### 8.1 Onset
RET fusion‑positive PTC is enriched in younger patients, including pediatric and adolescent presentations (pekova2023retfusiongenes pages 1-2, khonrak2023retrearrangementsare pages 1-2).

### 8.2 Progression and course
In a large cohort, metastases (nodal and distant) were frequent, but “true recurrences” were rare (**2.4%**, adults only) and disease‑specific survival remained high (**10‑year 95%**) (pekova2023retfusiongenes pages 1-2). In DSPTC, RET fusions identified a higher recurrence‑risk subgroup (5‑year RFS 46%) (scholfield2024definingthegenomic pages 1-3).

## 9. Inheritance and Population

### 9.1 Epidemiology
RET fusions are most commonly found in PTC.

**Reported prevalence ranges (study‑dependent):**
* FDA review: RET fusions are observed most commonly in papillary thyroid cancer (**5–10%**) (Duke 2023; published Sep 15, 2023; https://doi.org/10.1158/1078-0432.CCR-23-0459) (duke2023fdaapprovalsummary pages 1-3).  
* DNA‑NGS cohort: thyroid papillary carcinoma RET fusion prevalence **9.09% (109/1199)** (Parimi 2023; Jan 2023; https://doi.org/10.1038/s41698-023-00347-2) (parimi2023genomiclandscapeof pages 1-2).  
* Czech cohort: RET fusions **11.4% (113/993)** of PTC; **29.8% pediatric/adolescent** vs **8.7% adult** (Pekova 2023; Sep 2023; https://doi.org/10.1530/ERC-23-0117) (pekova2023retfusiongenes pages 1-2).

### 9.2 Inheritance
RET fusions in thyroid cancer are generally **somatic** driver events rather than inherited. (Germline RET alterations are relevant to MEN2 and medullary thyroid carcinoma, not the RET‑fusion PTC subtype.) (alzumaili2023updateonmolecular pages 5-7).

## 10. Diagnostics

### 10.1 Recommended testing approach (current understanding)
**Preferred approach:** Comprehensive **NGS**, ideally including **DNA and RNA interrogation** for fusions, is emphasized as the best method to identify RET fusions and concomitant alterations (desilets2023retalteredcancers—atumoragnostic pages 1-2, desilets2023retalteredcancers—atumoragnostic pages 8-9).

**Alternatives/adjuncts:** RT‑PCR and FISH may be used when NGS is unavailable, with known limitations (partner dependence, inability to identify partners/breakpoints for FISH) (desilets2023retalteredcancers—atumoragnostic pages 8-9, chen2024retinhibitorsin pages 3-5).

### 10.2 Test performance and key data
**IHC:** Sensitivity/specificity for RET IHC reported as **87%/82%**, but performance is partner dependent and it is “not recommended as a clinical screening assay for oncogenic RET alterations” (desilets2023retalteredcancers—atumoragnostic pages 8-9).  

**FISH:** Break‑apart FISH sensitivity is fusion‑partner dependent; in one series, thyroid cancer sensitivity was **88%**, and partner‑specific sensitivity examples included 100% for KIF5B/CCDC6 but 67% for NCOA4 (desilets2023retalteredcancers—atumoragnostic pages 8-9).

**ddPCR (CCDC6::RET):** ddPCR improved analytical sensitivity over qRT‑PCR with LoD **128.0 copies/reaction** vs **430.7 copies/reaction**; in 112 clinical PTC samples ddPCR detected **13.4% (15/112)** positives vs **9.8% (11/112)** by qRT‑PCR (Chen 2023; Apr 2023; https://doi.org/10.1186/s12885-023-10852-z) (chen2023highlysensitivedroplet pages 1-2, chen2023highlysensitivedroplet pages 2-4).

**Commercial thyroid nodule platforms:** ThyroSeq v3 (DNA+RNA panel) reports overall performance for nodule classification of **94% sensitivity**, **89% specificity**, **92% accuracy**, and includes RET fusions; Afirma XA uses whole‑transcriptome RNA sequencing and enumerates fusions including CCDC6::RET and NCOA4::RET (Alzumaili 2023; Jun 2023; https://doi.org/10.3390/genes14071314) (alzumaili2023updateonmolecular pages 5-7).

### 10.3 Differential diagnosis
RET fusions overlap with other fusion‑driven thyroid cancers (e.g., NTRK fusions) and mutation‑driven PTC (BRAF, RAS). Molecular testing distinguishes these entities for targeted therapy selection (alzumaili2023updateonmolecular pages 5-7, pekova2023retfusiongenes pages 1-2).

## 11. Outcome / Prognosis

**Disease‑specific survival (large cohort):** In RET fusion‑positive PTC, **2‑, 5‑, 10‑year disease‑specific survival** were **99%, 96%, 95%**, despite high metastatic burden, suggesting aggressive biology but potentially favorable survival with intensive multimodal management (pekova2023retfusiongenes pages 1-2).

**Subtype‑specific recurrence risk:** In DSPTC, RET fusions predicted **worse recurrence‑free survival** (5‑year RFS 46%) and were the only independent recurrence predictor (HR 7.69) (scholfield2024definingthegenomic pages 1-3).

## 12. Treatment

### 12.1 Targeted therapy (current standard for advanced RET fusion‑positive disease)

#### Selpercatinib (RET inhibitor)
**Regulatory indication (FDA):** FDA accelerated approval (May 8, 2020) includes adult and pediatric (≥12 years) patients with advanced/metastatic RET fusion‑positive thyroid cancer requiring systemic therapy and RAI‑refractory (if RAI appropriate) (Duke 2023; https://doi.org/10.1158/1078-0432.CCR-23-0459) (duke2023fdaapprovalsummary pages 1-3).  

**Dose concept (FDA review):** 120 mg orally BID if <50 kg; 160 mg orally BID if ≥50 kg (duke2023fdaapprovalsummary pages 3-5).

**Efficacy (LIBRETTO‑001 long‑term update):** At **January 2023** cutoff, RET fusion‑positive thyroid cancer cohort (n=66) demonstrated:  
* ORR **95.8%** in treatment‑naïve patients (n=24) and **85.4%** in previously treated patients (n=41) (Wirth 2024; published Sep 2024; https://doi.org/10.1200/JCO.23.02503) (wirth2024durabilityofresponse pages 7-7).  
* Median PFS: **not reached** (treatment‑naïve) and **27.4 months** (pretreated) (wirth2024durabilityofresponse pages 1-2, wirth2024durabilityofresponse pages 7-7).  

#### Pralsetinib (RET inhibitor)
**ARROW trial efficacy (previously treated RET fusion+ thyroid cancer):** ORR **90.9% (95% CI 70.8–98.9)** in **22** previously treated patients (review summary; Chen 2024; published Oct 2024; https://doi.org/10.3389/fendo.2024.1346476) (chen2024systemictreatmentsfor pages 7-8).  
Another synthesis reports ORR **89% (95% CI 52–100)** in RET fusion‑positive thyroid cancer cohorts (Clark 2023; published Dec 2023; https://doi.org/10.3390/cancers16010031) (clark2023selectiveretinhibitors pages 4-5).

**Key toxicities (grade ≥3 TRAEs, thyroid cancer population in summary):** hypertension **17%**, neutropenia **13%**, lymphopenia **12%**, anemia **10%**; pneumonitis **4%**; discontinuation **4%**; treatment‑related death **1%** (clark2023selectiveretinhibitors pages 4-5).

### 12.2 Treatment resistance (mechanisms and emerging strategies)
Acquired resistance to selective RET inhibitors may involve:
* **On‑target RET mutations**, especially solvent‑front **RET G810 substitutions (G810X)**; also RET **L730V/I**, **Y806**, **V738** alterations (desilets2023retalteredcancers—atumoragnostic pages 15-16).  
* **Bypass mechanisms**, including **MET amplification** and MAPK reactivation via emergent **KRAS/NRAS/BRAF** alterations (desilets2023retalteredcancers—atumoragnostic pages 15-16).  
Next‑generation RET inhibitors are being developed with activity against solvent‑front and gatekeeper mutants (e.g., preclinical development described in 2023 review; APS03118 potency against G810 and V804 mutants, with PDX/intracranial models) (clark2023selectiveretinhibitors pages 9-11).

### 12.3 Suggested MAXO terms (examples)
* Targeted therapy — **MAXO:0000058** (suggested)  
* Tyrosine kinase inhibitor therapy — **MAXO:0000647** (suggested)  
* Molecularly targeted therapy based on gene fusion — (suggested; if available in MAXO)

### 12.4 Suggested CHEBI entities
The CHEBI IDs for selpercatinib and pralsetinib were not retrieved in the available sources.

## 13. Prevention
Primary prevention for RET fusion acquisition is not established. Secondary prevention consists of early detection and appropriate molecular testing to enable precision therapy. Specific screening strategies for RET fusions in the general population are not described in the retrieved sources.

## 14. Other species / natural disease
Not identified in retrieved sources.

## 15. Model organisms / experimental models
**Selpercatinib preclinical models:** FDA review notes selpercatinib activity in in vitro/in vivo models with **CCDC6‑RET**, **KIF5B‑RET**, and RET resistance/driver mutations (RET **V804M**, **M918T**), and in a **mouse intracranial model** with a patient‑derived RET fusion‑positive tumor (Duke 2023; https://doi.org/10.1158/1078-0432.CCR-23-0459) (duke2023fdaapprovalsummary pages 3-5).  

**Engineered resistance models:** Engineered Ba/F3 fusion models (e.g., Ba/F3 KIF5B‑RET) and derived resistant lines have been used to characterize on‑target resistance mutations under RET inhibitor pressure (Spitaleri 2024; published Aug 2024; https://doi.org/10.3390/cancers16162877) (spitaleri2024nonsmallcelllungcancers pages 11-12).  

**PDX and intracranial orthotopic models for next‑gen inhibitors:** A 2023 review describes PDX and intracranial orthotopic models including **CCDC6‑RET** and **CCDC6‑RET V804M**, demonstrating feasibility of brain‑penetrant next‑generation RET inhibition strategies aimed at resistance (clark2023selectiveretinhibitors pages 9-11).

## Evidence table (structured summary)

| Study (first author, year) | Population/cohort | Method | Key findings (with exact numbers) | URL/DOI |
|---|---|---|---|---|
| Parimi, 2023 | Pan-tumor cohort of 891 RET fusion-positive advanced solid tumors; thyroid papillary carcinoma subset | Tissue-based DNA hybrid-capture NGS; subset with liquid biopsy hybrid-capture NGS | RET fusions were most frequent in lung adenocarcinoma and thyroid papillary carcinoma; thyroid papillary carcinoma prevalence was **9.09% (109/1199)**. In the pan-tumor RET+ cohort, common partners included **NCOA4 32.6%** and **CCDC6 29.9%**. Tissue-liquid concordance for RET fusion detection was **100% (8/8)** when composite tumor fraction was **>1%** (parimi2023genomiclandscapeof pages 1-2) | https://doi.org/10.1038/s41698-023-00347-2 |
| Pekova, 2023 | 1,564 thyroid tissue samples including 1,164 carcinomas and 993 PTCs; pediatric and adult patients | Driver testing followed by extensive RET fusion analysis using NGS and real-time PCR | RET fusions were detected **exclusively in PTC**, in **113/993 (11.4%)** patients; prevalence was **29.8%** in pediatric/adolescent patients vs **8.7%** in adults. **20 RET fusion types** were identified. Aggressiveness: **lymph node metastasis 75.2%**, **distant metastasis 18.6%**, **true recurrences 2.4%**. Disease-specific survival: **2-year 99%**, **5-year 96%**, **10-year 95%** (pekova2023retfusiongenes pages 1-2) | https://doi.org/10.1530/ERC-23-0117 |
| Pekova, 2023 | RET fusion-positive PTC subset from the above cohort (**n=113**) | Targeted RNA sequencing panels with real-time PCR confirmation | Fusion partners: **CCDC6 67/113 (59.3%)**, **NCOA4 25/113 (22.1%)**; additional recurrent/novel partners included **FBXO41, SSBP2, ZMYM2**. Cohort characteristics: **75.2% female**, mean age **32.6 ± 17.4 years**, mean tumor size **21.8 ± 12.6 mm** (pekova2023retfusiongenes pages 3-5) | https://doi.org/10.1530/ERC-23-0117 |
| Chen, 2023 | TCGA PTC cohort (**402**) and clinical PTC samples (**112**) | ddPCR assay for **CCDC6::RET** vs qRT-PCR; Sanger confirmation | In TCGA, RET fusions were present in **25/402 (6.2%)** PTCs; **CCDC6::RET** accounted for **15/25 (60%)** of RET-positive cases. In clinical samples, qRT-PCR detected **11/112 (9.8%)** CCDC6::RET-positive cases, while ddPCR detected **15/112 (13.4%)**, adding **4** extra positives. Limit of detection: **128.0 copies/reaction** for ddPCR vs **430.7 copies/reaction** for qRT-PCR (chen2023highlysensitivedroplet pages 1-2, chen2023highlysensitivedroplet pages 2-4) | https://doi.org/10.1186/s12885-023-10852-z |
| Khonrak, 2023 | Thai PTC cohort (**n=83**) | qRT-PCR on FFPE samples for **CCDC6::RET** and **NCOA4::RET** | Background prevalence noted as ~**10–40%** of adult PTC and **45–60%** of pediatric/adolescent sporadic PTC; **CCDC6** and **NCOA4** together account for ~**90%** of RET::PTC fusions. Phenotype: **CCDC6::RET** associated with classic subtype and **absence** of angio/lymphatic invasion; **NCOA4::RET** associated with **tall-cell subtype**, **angio/lymphatic invasion**, and **lymph node metastasis** (khonrak2023retrearrangementsare pages 1-2) | https://doi.org/10.3389/pore.2023.1611138 |
| Tali, 2023 | Molecularly tested operated thyroid nodules; RET/PTC-positive nodules (**n=5**) | Retrospective single-center study using preoperative molecular testing and final pathology | All **5/5 (100%)** RET/PTC nodules were malignant and Bethesda **V/VI**. Histology: **60% (3/5)** diffuse sclerosing variant, **40% (2/5)** classical PTC. Aggressiveness: **80% (4/5)** lymph node metastasis, **20% (1/5)** extrathyroidal extension; one nodal metastasis case had extranodal spread (tali2023thedifferencein pages 4-6, tali2023thedifferencein pages 1-2) | https://doi.org/10.3390/cancers15133394 |
| Scholfield, 2024 | Diffuse sclerosing papillary thyroid carcinoma (DSPTC) tumors (**n=41**) | MSK-IMPACT 505-gene panel sequencing | RET fusions were the most common alteration: **32% (13/41)**. RET fusion-positive tumors occurred at younger age and had more aggressive features and higher T-stage. Outcome: **5-year recurrence-free survival 46% vs 84%** for other drivers; multivariable analysis: RET fusion status independent predictor of recurrence (**HR 7.69**, **p=0.017**) (scholfield2024definingthegenomic pages 1-3) | https://doi.org/10.1245/s10434-024-15500-9 |
| Selpercatinib (LIBRETTO-001), Wirth, 2024 | RET fusion-positive thyroid cancer in LIBRETTO-001; treatment-naïve (**n=24**) and pretreated (**n=41**) | Phase I/II clinical trial long-term update | At January 2023 cutoff, ORR was **95.8% (95% CI 78.9–99.9)** in treatment-naïve patients and **85.4% (95% CI 70.8–94.4)** in pretreated patients; complete responses **20.8%** and **12.2%**, respectively. Median follow-up: **24.9 months** (naïve) and **30.4 months** (pretreated). Median PFS: **not reached** (naïve) and **27.4 months** (pretreated). **3-year PFS 87.3%** in treatment-naïve TC; **3-year overall survival 94.4%** (naïve) and **65.5%** (pretreated) (wirth2024durabilityofresponse pages 1-2, wirth2024durabilityofresponse pages 7-7, wirth2024durabilityofresponse media 08850bf1) | https://doi.org/10.1200/JCO.23.02503 |
| Selpercatinib (regulatory summary), Duke, 2023 | FDA summary referencing prior thyroid approval and broader RET fusion-positive solid tumor activity | FDA review of LIBRETTO-001 | FDA notes RET fusions are seen most commonly in papillary thyroid cancer at **5–10%**. For thyroid cancer, prior approval covered adult and pediatric patients ≥12 years with advanced/metastatic RET fusion-positive thyroid cancer requiring systemic therapy and **RAI-refractory** if RAI appropriate. Selpercatinib activity supported by preclinical models including **CCDC6-RET** (duke2023fdaapprovalsummary pages 3-5, duke2023fdaapprovalsummary pages 1-3) | https://doi.org/10.1158/1078-0432.CCR-23-0459 |
| Pralsetinib (ARROW), Clark, 2023 | RET fusion-positive thyroid cancer cohort in ARROW (**n=20** enrolled; efficacy summarized across thyroid cohorts) | Phase I/II multicohort trial summary | Reported ORR in RET fusion-positive thyroid cancer was **89% (95% CI 52–100)**. Safety in RET-altered thyroid cancer: grade ≥3 TRAEs included **hypertension 17%**, **neutropenia 13%**, **lymphopenia 12%**, **anemia 10%**; serious TRAEs in **15%**; pneumonitis in **4%**; discontinuation due to TRAEs **4%**; treatment-related death **1%** (clark2023selectiveretinhibitors pages 4-5) | https://doi.org/10.3390/cancers16010031 |
| Pralsetinib (ARROW), Chen, 2024 | Previously treated RET fusion-positive thyroid cancer patients (**n=22**) | Review summarizing ARROW (NCT03037385) | ORR was **90.9% (95% CI 70.8–98.9)** in **22** previously treated RET fusion-positive thyroid cancer patients; review notes FDA approval for RET fusion-positive thyroid cancer in **December 2020** (chen2024systemictreatmentsfor pages 7-8) | https://doi.org/10.3389/fendo.2024.1346476 |
| Pralsetinib (ARROW), Desilets, 2023 | Previously treated RET fusion-positive thyroid cancer cohort | Tumor-agnostic review summarizing ARROW | Reported ORR for previously treated RET fusion-positive thyroid cancer was **89%**. Common grade 3–4 adverse events across studies included **neutropenia 13–31%**, **hypertension 7–17%**, **anemia 10–14%**, **lymphopenia 9–12%**, increased **creatine phosphokinase 6%**, and treatment-emergent **pneumonitis 4%** (desilets2023retalteredcancers—atumoragnostic pages 13-15) | https://doi.org/10.3390/cancers15164146 |


*Table: This table compiles key cohort-level evidence on RET fusion prevalence, dominant fusion partners, clinicopathologic aggressiveness, and selective RET inhibitor outcomes in RET fusion-positive thyroid cancer. It is useful as a compact evidence map for diagnosis, prognosis, and treatment selection.*

## Key “expert opinion” synthesis (from authoritative sources)
* **Testing:** Comprehensive NGS (preferably DNA+RNA) is emphasized as the best way to identify RET fusions and concurrent alterations; IHC is not recommended as a screening assay due to variable performance (desilets2023retalteredcancers—atumoragnostic pages 8-9, chen2024retinhibitorsin pages 3-5).  
* **Clinical importance:** RET fusions are common enough in PTC to justify systematic testing strategies, especially in advanced disease where selective RET inhibitors provide high response rates (duke2023fdaapprovalsummary pages 1-3, wirth2024durabilityofresponse pages 1-2).  
* **Therapeutic landscape:** Selective RET inhibitors are now standard precision options, but resistance via RET solvent‑front mutations and bypass pathways motivates development of next‑generation inhibitors and combination approaches (desilets2023retalteredcancers—atumoragnostic pages 15-16, clark2023selectiveretinhibitors pages 9-11).

## Notable gaps / limitations of retrieved evidence
* A specific MONDO/MeSH/ICD identifier for the **fusion‑positive molecular subtype** was not retrieved.  
* Some requested items (thyroid‑specific QoL outcomes; pralsetinib DoR/PFS; detailed treatment algorithms from society guidelines) were not present in the accessible text segments and would require targeted retrieval of the primary ARROW thyroid manuscript and thyroid cancer clinical guidelines.


References

1. (duke2023fdaapprovalsummary pages 1-3): Elizabeth S. Duke, Diana Bradford, Michelle Marcovitz, Anup K. Amatya, Pallavi S. Mishra-Kalyani, Emily Nguyen, Lauren S.L. Price, Jeanne Fourie Zirkelbach, Yangbing Li, Youwei Bi, Jeffrey Kraft, Sarah E. Dorff, Barbara Scepura, Maritsa Stephenson, Idara Ojofeitimi, Abhilasha Nair, Yu Han, Zivana Tezak, Steven J. Lemery, Richard Pazdur, Erin Larkins, and Harpreet Singh. Fda approval summary: selpercatinib for the treatment of advanced ret fusion-positive solid tumors. Clinical cancer research : an official journal of the American Association for Cancer Research, 29:3573-3578, May 2023. URL: https://doi.org/10.1158/1078-0432.ccr-23-0459, doi:10.1158/1078-0432.ccr-23-0459. This article has 87 citations.

2. (pekova2023retfusiongenes pages 1-2): Barbora Bulanova Pekova, Vlasta Sykorova, Karolina Mastnikova, Eliska Vaclavikova, Jitka Moravcova, Petr Vlcek, Lucie Lancova, Petr Lastuvka, Rami Katra, Petr Bavor, Daniela Kodetova, Martin Chovanec, Jana Drozenova, Radoslav Matej, Jaromir Astl, Jiri Hlozek, Petr Hrabal, Josef Vcelak, and Bela Bendlova. Ret fusion genes in pediatric and adult thyroid carcinomas: cohort characteristics and prognosis. Endocrine-Related Cancer, Sep 2023. URL: https://doi.org/10.1530/erc-23-0117, doi:10.1530/erc-23-0117. This article has 29 citations and is from a domain leading peer-reviewed journal.

3. (parimi2023genomiclandscapeof pages 1-2): Vamsi Parimi, Khaled Tolba, Natalie Danziger, Zheng Kuang, Daokun Sun, Douglas I. Lin, Matthew C. Hiemenz, Alexa B. Schrock, Jeffrey S. Ross, Geoffrey R. Oxnard, and Richard S. P. Huang. Genomic landscape of 891 ret fusions detected across diverse solid tumor types. NPJ Precision Oncology, Jan 2023. URL: https://doi.org/10.1038/s41698-023-00347-2, doi:10.1038/s41698-023-00347-2. This article has 67 citations and is from a peer-reviewed journal.

4. (wirth2024durabilityofresponse pages 1-2): Lori J. Wirth, Marcia S. Brose, Vivek Subbiah, Francis Worden, Ben Solomon, Bruce Robinson, Julien Hadoux, Pascale Tomasini, Daniela Weiler, Barbara Deschler-Baier, Daniel S.W. Tan, Patricia Maeda, Yan Lin, Ravinder Singh, Theresa Bayt, Alexander Drilon, and Philippe A. Cassier. Durability of response with selpercatinib in patients with <i>ret</i>-activated thyroid cancer: long-term safety and efficacy from libretto-001. Journal of Clinical Oncology, 42:3187-3195, Sep 2024. URL: https://doi.org/10.1200/jco.23.02503, doi:10.1200/jco.23.02503. This article has 39 citations and is from a highest quality peer-reviewed journal.

5. (clark2023selectiveretinhibitors pages 4-5): Lisa Clark, Geoff Fisher, Sue Brook, Sital Patel, and Hendrik-Tobias Arkenau. Selective ret inhibitors (sris) in cancer: a journey from multi-kinase inhibitors to the next generation of sris. Cancers, 16:31, Dec 2023. URL: https://doi.org/10.3390/cancers16010031, doi:10.3390/cancers16010031. This article has 10 citations.

6. (duke2023fdaapprovalsummary pages 3-5): Elizabeth S. Duke, Diana Bradford, Michelle Marcovitz, Anup K. Amatya, Pallavi S. Mishra-Kalyani, Emily Nguyen, Lauren S.L. Price, Jeanne Fourie Zirkelbach, Yangbing Li, Youwei Bi, Jeffrey Kraft, Sarah E. Dorff, Barbara Scepura, Maritsa Stephenson, Idara Ojofeitimi, Abhilasha Nair, Yu Han, Zivana Tezak, Steven J. Lemery, Richard Pazdur, Erin Larkins, and Harpreet Singh. Fda approval summary: selpercatinib for the treatment of advanced ret fusion-positive solid tumors. Clinical cancer research : an official journal of the American Association for Cancer Research, 29:3573-3578, May 2023. URL: https://doi.org/10.1158/1078-0432.ccr-23-0459, doi:10.1158/1078-0432.ccr-23-0459. This article has 87 citations.

7. (carneiro2024predictivebiomarkersin pages 8-9): Humberto Carvalho Carneiro, Rodrigo de Andrade Natal, Evelin Cavalcante Farias, Aline Almeida Bastos, Leila Guastapaglia, Alanna Mara Pinheiro Sobreira Bezerra, and Ana Amélia Fialho de Oliveira Hoff. Predictive biomarkers in thyroid cancer in the current molecular-morphology paradigm. Surgical and Experimental Pathology, Aug 2024. URL: https://doi.org/10.1186/s42047-024-00157-1, doi:10.1186/s42047-024-00157-1. This article has 5 citations.

8. (desilets2023retalteredcancers—atumoragnostic pages 13-15): Antoine Desilets, Matteo Repetto, Soo-Ryum Yang, Eric J. Sherman, and Alexander Drilon. Ret-altered cancers—a tumor-agnostic review of biology, diagnosis and targeted therapy activity. Cancers, 15:4146, Aug 2023. URL: https://doi.org/10.3390/cancers15164146, doi:10.3390/cancers15164146. This article has 41 citations.

9. (pekova2023retfusiongenes pages 3-5): Barbora Bulanova Pekova, Vlasta Sykorova, Karolina Mastnikova, Eliska Vaclavikova, Jitka Moravcova, Petr Vlcek, Lucie Lancova, Petr Lastuvka, Rami Katra, Petr Bavor, Daniela Kodetova, Martin Chovanec, Jana Drozenova, Radoslav Matej, Jaromir Astl, Jiri Hlozek, Petr Hrabal, Josef Vcelak, and Bela Bendlova. Ret fusion genes in pediatric and adult thyroid carcinomas: cohort characteristics and prognosis. Endocrine-Related Cancer, Sep 2023. URL: https://doi.org/10.1530/erc-23-0117, doi:10.1530/erc-23-0117. This article has 29 citations and is from a domain leading peer-reviewed journal.

10. (NCT03157128 chunk 1):  A Study of Selpercatinib (LOXO-292) in Participants With Advanced Solid Tumors, RET Fusion-Positive Solid Tumors, and Medullary Thyroid Cancer (LIBRETTO-001). Eli Lilly and Company. 2017. ClinicalTrials.gov Identifier: NCT03157128

11. (desilets2023retalteredcancers—atumoragnostic pages 2-4): Antoine Desilets, Matteo Repetto, Soo-Ryum Yang, Eric J. Sherman, and Alexander Drilon. Ret-altered cancers—a tumor-agnostic review of biology, diagnosis and targeted therapy activity. Cancers, 15:4146, Aug 2023. URL: https://doi.org/10.3390/cancers15164146, doi:10.3390/cancers15164146. This article has 41 citations.

12. (pekova2023retfusiongenes pages 11-12): Barbora Bulanova Pekova, Vlasta Sykorova, Karolina Mastnikova, Eliska Vaclavikova, Jitka Moravcova, Petr Vlcek, Lucie Lancova, Petr Lastuvka, Rami Katra, Petr Bavor, Daniela Kodetova, Martin Chovanec, Jana Drozenova, Radoslav Matej, Jaromir Astl, Jiri Hlozek, Petr Hrabal, Josef Vcelak, and Bela Bendlova. Ret fusion genes in pediatric and adult thyroid carcinomas: cohort characteristics and prognosis. Endocrine-Related Cancer, Sep 2023. URL: https://doi.org/10.1530/erc-23-0117, doi:10.1530/erc-23-0117. This article has 29 citations and is from a domain leading peer-reviewed journal.

13. (khonrak2023retrearrangementsare pages 1-2): Thitima Khonrak, Sasithorn Watcharadetwittaya, Yaovalux Chamgramol, Piyapharom Intarawichian, and Raksawan Deenonpoe. Ret rearrangements are relevant to histopathologic subtypes and clinicopathological features in thai papillary thyroid carcinoma patients. Pathology and Oncology Research, Apr 2023. URL: https://doi.org/10.3389/pore.2023.1611138, doi:10.3389/pore.2023.1611138. This article has 10 citations.

14. (khonrak2023retrearrangementsare pages 13-13): Thitima Khonrak, Sasithorn Watcharadetwittaya, Yaovalux Chamgramol, Piyapharom Intarawichian, and Raksawan Deenonpoe. Ret rearrangements are relevant to histopathologic subtypes and clinicopathological features in thai papillary thyroid carcinoma patients. Pathology and Oncology Research, Apr 2023. URL: https://doi.org/10.3389/pore.2023.1611138, doi:10.3389/pore.2023.1611138. This article has 10 citations.

15. (pekova2023retfusiongenes pages 12-13): Barbora Bulanova Pekova, Vlasta Sykorova, Karolina Mastnikova, Eliska Vaclavikova, Jitka Moravcova, Petr Vlcek, Lucie Lancova, Petr Lastuvka, Rami Katra, Petr Bavor, Daniela Kodetova, Martin Chovanec, Jana Drozenova, Radoslav Matej, Jaromir Astl, Jiri Hlozek, Petr Hrabal, Josef Vcelak, and Bela Bendlova. Ret fusion genes in pediatric and adult thyroid carcinomas: cohort characteristics and prognosis. Endocrine-Related Cancer, Sep 2023. URL: https://doi.org/10.1530/erc-23-0117, doi:10.1530/erc-23-0117. This article has 29 citations and is from a domain leading peer-reviewed journal.

16. (scholfield2024definingthegenomic pages 1-3): Daniel W. Scholfield, Conall W. R. Fitzgerald, Lillian A. Boe, Alana Eagan, Helena Levyn, Bin Xu, R. Michael Tuttle, James A. Fagin, Ashok R. Shaha, Jatin P. Shah, Richard J. Wong, Snehal G. Patel, Ronald Ghossein, and Ian Ganly. Defining the genomic landscape of diffuse sclerosing papillary thyroid carcinoma: prognostic implications of ret fusions. Annals of surgical oncology, 31:5525-5536, Jun 2024. URL: https://doi.org/10.1245/s10434-024-15500-9, doi:10.1245/s10434-024-15500-9. This article has 8 citations and is from a domain leading peer-reviewed journal.

17. (tali2023thedifferencein pages 1-2): George Tali, Alexandra E. Payne, Thomas J. Hudson, Sabrina Daniela da Silva, Marc Pusztaszeri, Michael Tamilia, and Véronique-Isabelle Forest. The difference in clinical behavior of gene fusions involving ret/ptc fusions and thada/igf2bp3 fusions in thyroid nodules. Cancers, 15:3394, Jun 2023. URL: https://doi.org/10.3390/cancers15133394, doi:10.3390/cancers15133394. This article has 7 citations.

18. (tali2023thedifferencein pages 4-6): George Tali, Alexandra E. Payne, Thomas J. Hudson, Sabrina Daniela da Silva, Marc Pusztaszeri, Michael Tamilia, and Véronique-Isabelle Forest. The difference in clinical behavior of gene fusions involving ret/ptc fusions and thada/igf2bp3 fusions in thyroid nodules. Cancers, 15:3394, Jun 2023. URL: https://doi.org/10.3390/cancers15133394, doi:10.3390/cancers15133394. This article has 7 citations.

19. (wirth2024durabilityofresponse pages 7-7): Lori J. Wirth, Marcia S. Brose, Vivek Subbiah, Francis Worden, Ben Solomon, Bruce Robinson, Julien Hadoux, Pascale Tomasini, Daniela Weiler, Barbara Deschler-Baier, Daniel S.W. Tan, Patricia Maeda, Yan Lin, Ravinder Singh, Theresa Bayt, Alexander Drilon, and Philippe A. Cassier. Durability of response with selpercatinib in patients with <i>ret</i>-activated thyroid cancer: long-term safety and efficacy from libretto-001. Journal of Clinical Oncology, 42:3187-3195, Sep 2024. URL: https://doi.org/10.1200/jco.23.02503, doi:10.1200/jco.23.02503. This article has 39 citations and is from a highest quality peer-reviewed journal.

20. (chen2024retinhibitorsin pages 1-3): Monica F. Chen, Matteo Repetto, Clare Wilhelm, and Alexander Drilon. Ret inhibitors in ret fusion-positive lung cancers: past, present, and future. Drugs, 84:1035-1053, Jul 2024. URL: https://doi.org/10.1007/s40265-024-02040-5, doi:10.1007/s40265-024-02040-5. This article has 13 citations and is from a domain leading peer-reviewed journal.

21. (alzumaili2023updateonmolecular pages 5-7): Bayan Alzumaili and Peter M. Sadow. Update on molecular diagnostics in thyroid pathology: a review. Genes, 14:1314, Jun 2023. URL: https://doi.org/10.3390/genes14071314, doi:10.3390/genes14071314. This article has 40 citations.

22. (desilets2023retalteredcancers—atumoragnostic pages 1-2): Antoine Desilets, Matteo Repetto, Soo-Ryum Yang, Eric J. Sherman, and Alexander Drilon. Ret-altered cancers—a tumor-agnostic review of biology, diagnosis and targeted therapy activity. Cancers, 15:4146, Aug 2023. URL: https://doi.org/10.3390/cancers15164146, doi:10.3390/cancers15164146. This article has 41 citations.

23. (desilets2023retalteredcancers—atumoragnostic pages 8-9): Antoine Desilets, Matteo Repetto, Soo-Ryum Yang, Eric J. Sherman, and Alexander Drilon. Ret-altered cancers—a tumor-agnostic review of biology, diagnosis and targeted therapy activity. Cancers, 15:4146, Aug 2023. URL: https://doi.org/10.3390/cancers15164146, doi:10.3390/cancers15164146. This article has 41 citations.

24. (chen2024retinhibitorsin pages 3-5): Monica F. Chen, Matteo Repetto, Clare Wilhelm, and Alexander Drilon. Ret inhibitors in ret fusion-positive lung cancers: past, present, and future. Drugs, 84:1035-1053, Jul 2024. URL: https://doi.org/10.1007/s40265-024-02040-5, doi:10.1007/s40265-024-02040-5. This article has 13 citations and is from a domain leading peer-reviewed journal.

25. (chen2023highlysensitivedroplet pages 1-2): Meng-ke Chen, Junyu Xue, Ye Sang, Wenting Jiang, Weiman He, Shubin Hong, Weiming Lv, Haipeng Xiao, and Rengyun Liu. Highly sensitive droplet digital pcr for detection of ret fusion in papillary thyroid cancer. BMC Cancer, Apr 2023. URL: https://doi.org/10.1186/s12885-023-10852-z, doi:10.1186/s12885-023-10852-z. This article has 3 citations and is from a peer-reviewed journal.

26. (chen2023highlysensitivedroplet pages 2-4): Meng-ke Chen, Junyu Xue, Ye Sang, Wenting Jiang, Weiman He, Shubin Hong, Weiming Lv, Haipeng Xiao, and Rengyun Liu. Highly sensitive droplet digital pcr for detection of ret fusion in papillary thyroid cancer. BMC Cancer, Apr 2023. URL: https://doi.org/10.1186/s12885-023-10852-z, doi:10.1186/s12885-023-10852-z. This article has 3 citations and is from a peer-reviewed journal.

27. (chen2024systemictreatmentsfor pages 7-8): Piaohong Chen, Yu Yao, Huiwen Tan, and Jianwei Li. Systemic treatments for radioiodine-refractory thyroid cancers. Frontiers in Endocrinology, Oct 2024. URL: https://doi.org/10.3389/fendo.2024.1346476, doi:10.3389/fendo.2024.1346476. This article has 15 citations.

28. (desilets2023retalteredcancers—atumoragnostic pages 15-16): Antoine Desilets, Matteo Repetto, Soo-Ryum Yang, Eric J. Sherman, and Alexander Drilon. Ret-altered cancers—a tumor-agnostic review of biology, diagnosis and targeted therapy activity. Cancers, 15:4146, Aug 2023. URL: https://doi.org/10.3390/cancers15164146, doi:10.3390/cancers15164146. This article has 41 citations.

29. (clark2023selectiveretinhibitors pages 9-11): Lisa Clark, Geoff Fisher, Sue Brook, Sital Patel, and Hendrik-Tobias Arkenau. Selective ret inhibitors (sris) in cancer: a journey from multi-kinase inhibitors to the next generation of sris. Cancers, 16:31, Dec 2023. URL: https://doi.org/10.3390/cancers16010031, doi:10.3390/cancers16010031. This article has 10 citations.

30. (spitaleri2024nonsmallcelllungcancers pages 11-12): Gianluca Spitaleri, Pamela Trillo Aliaga, Ilaria Attili, Ester Del Signore, Carla Corvaja, Gloria Pellizzari, Jalissa Katrini, Antonio Passaro, and Filippo de Marinis. Non-small-cell lung cancers (nsclcs) harboring ret gene fusion, from their discovery to the advent of new selective potent ret inhibitors: “shadows and fogs”. Cancers, 16:2877, Aug 2024. URL: https://doi.org/10.3390/cancers16162877, doi:10.3390/cancers16162877. This article has 7 citations.

31. (wirth2024durabilityofresponse media 08850bf1): Lori J. Wirth, Marcia S. Brose, Vivek Subbiah, Francis Worden, Ben Solomon, Bruce Robinson, Julien Hadoux, Pascale Tomasini, Daniela Weiler, Barbara Deschler-Baier, Daniel S.W. Tan, Patricia Maeda, Yan Lin, Ravinder Singh, Theresa Bayt, Alexander Drilon, and Philippe A. Cassier. Durability of response with selpercatinib in patients with <i>ret</i>-activated thyroid cancer: long-term safety and efficacy from libretto-001. Journal of Clinical Oncology, 42:3187-3195, Sep 2024. URL: https://doi.org/10.1200/jco.23.02503, doi:10.1200/jco.23.02503. This article has 39 citations and is from a highest quality peer-reviewed journal.
