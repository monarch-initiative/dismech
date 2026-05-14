---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T09:51:10.173333'
end_time: '2026-05-09T10:07:48.243912'
duration_seconds: 998.07
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Koolen-de Vries syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Koolen-de Vries syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Koolen-de Vries syndrome** covering all of the
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
- **Disease Name:** Koolen-de Vries syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Koolen-de Vries syndrome** covering all of the
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


## Comprehensive Research Report: Koolen–de Vries Syndrome (KdVS)

### Target Disease
- **Disease name:** Koolen–de Vries syndrome (KdVS)
- **Category:** Mendelian; neurodevelopmental disorder
- **MONDO ID:** Not retrievable from the provided full-text evidence in this run (see “Evidence gaps”).

---

## 1. Disease Information

### 1.1 Concise overview (current understanding)
Koolen–de Vries syndrome is a rare, multisystem **neurodevelopmental disorder** caused by either a recurrent **17q21.31 microdeletion** that includes **KANSL1** or by a heterozygous **intragenic pathogenic variant in KANSL1**. Core features across cohorts include developmental delay, hypotonia, intellectual disability (often moderate), speech/language disorder, and frequent multisystem comorbidities (cardiac, renal/urogenital, musculoskeletal, sensory, sleep, and behavioral features). (colin2023genidaaparticipatory pages 2-3, houser2025neuroimagingofkoolende pages 2-8)

### 1.2 Key identifiers
- **OMIM:** **610443** (colin2023genidaaparticipatory pages 2-3)
- **Orphanet / ICD-10/ICD-11 / MeSH / MONDO:** Not retrievable from the provided full-text evidence in this run (see “Evidence gaps”).

### 1.3 Synonyms and alternative names
Commonly used synonyms in the clinical literature include:
- **17q21.31 microdeletion syndrome** (farne2022koolen‐devriessyndrome pages 10-12)
- **KANSL1-related intellectual disability syndrome** (farne2022koolen‐devriessyndrome pages 10-12)

### 1.4 Evidence source types
The report integrates:
- **Aggregated disease-level resources via cohorts/registries:** e.g., **GenIDA** caregiver-reported cohort (n=237) (colin2023genidaaparticipatory pages 3-4)
- **Clinician-assessed cohort study:** large speech/language and medical phenotype cohort (n=81) (john2023expandingthespeech pages 2-2)
- **Primary mechanistic studies:** mouse model and human iPSC-derived neuronal models (li2022kansl1haploinsufficiencyimpairs pages 1-2, linda2022imbalancedautophagycauses pages 1-3)

---

## 2. Etiology

### 2.1 Disease causal factors
KdVS is a **genetic** disorder caused by **KANSL1 haploinsufficiency**, either from:
- a **17q21.31 deletion** including KANSL1, or
- a **heterozygous pathogenic variant in KANSL1** (houser2025neuroimagingofkoolende pages 2-8, colin2023genidaaparticipatory pages 2-3)

### 2.2 Risk factors
- **Primary genetic risk factor:** de novo heterozygous 17q21.31 deletion or de novo heterozygous pathogenic KANSL1 variant (autosomal dominant) (houser2025neuroimagingofkoolende pages 2-8, saxena2021koolen‐devriessyndrome pages 2-4)
- **Environmental risk factors / protective factors / gene–environment interactions:** No KdVS-specific evidence identified in the retrieved texts.

### 2.3 Inheritance
KdVS is described as **autosomal dominant**, typically arising **de novo** (houser2025neuroimagingofkoolende pages 2-8, saxena2021koolen‐devriessyndrome pages 2-4).

---

## 3. Phenotypes (with frequencies, onset, and suggested HPO terms)

### 3.1 Summary of highest-yield phenotypes (recent large cohorts)
Two major recent data sources provide quantitative phenotype frequencies:
- **GenIDA caregiver registry** (n=237; mean age 14.0 years; 116 males/121 females) (colin2023genidaaparticipatory pages 3-4)
- **St John et al. 2023 clinical cohort** (n=81; mean age 9y10mo; age range 1.5–40.2y) (john2023expandingthespeech pages 2-2)

#### Neurodevelopmental
- **Developmental delay:** 96.3% (78/81) (john2023expandingthespeech pages 2-2)
  - Suggested HPO: *Global developmental delay* (HP:0001263)
- **Intellectual disability (ID):** 89.2% (GenIDA); severity distribution: mild 16.9%, moderate 60.2%, severe 2.4%, profound 20.5% (colin2023genidaaparticipatory pages 3-4)
  - Suggested HPO: *Intellectual disability* (HP:0001249)
- **Hypotonia:** 61.5% (colin2023genidaaparticipatory pages 3-4)
  - Suggested HPO: *Hypotonia* (HP:0001252)

#### Speech/language and communication
- **Speech/language delay:** 73.6% in children >2y; first words mean 2.2 years (colin2023genidaaparticipatory pages 3-4)
  - Suggested HPO: *Speech delay* (HP:0000750), *Delayed speech and language development* (HP:0000750 / HP:0000750-related)
- **Motor speech disorders (verbal subgroup):** apraxia features 63.9% (39/61); dysarthria 45.9% (28/61) (john2023expandingthespeech pages 1-2)
  - Suggested HPO: *Childhood apraxia of speech* (HP:0002465), *Dysarthria* (HP:0001260)
- **Stuttering:** 76.6% of verbal participants (36/47), described as late-onset and fluctuating (john2023expandingthespeech pages 1-2)
  - Suggested HPO: *Stuttering* (HP:0000755)
- **AAC use (implementation):** Minimally verbal communicators used AAC successfully; early AAC recommended (john2023expandingthespeech pages 1-2)

#### Epilepsy and seizures
- **Epilepsy prevalence:** 47.3% (97/204) in GenIDA (colin2023genidaaparticipatory pages 6-7) vs 35.8% (29/81) in St John et al. cohort (john2023expandingthespeech pages 2-2)
  - Suggested HPO: *Seizure* (HP:0001250), *Epilepsy* (HP:0001250)
- **Age at first seizure:** mean 3.4 years; median 2.0 years (colin2023genidaaparticipatory pages 7-9)
- **Seizure-type distribution among epilepsy cases:** tonic-clonic 38.1%, absence 28.9%, complex partial 22.7%, nocturnal 21.6%, febrile convulsions 19.6%, infantile spasms 14.4%, atonic 9.3% (colin2023genidaaparticipatory pages 6-7)

#### Motor development / musculoskeletal
- **Motor milestone delays (GenIDA median):** sit 10.7 mo; stand 17.5 mo; walk 23.4 mo (colin2023genidaaparticipatory pages 3-4)
  - Suggested HPO: *Delayed gross motor development* (HP:0002194)
- **Musculoskeletal anomalies:** 75.5% overall; joint laxity 50.0%; scoliosis 25.5%; hip dysplasia/dislocation 18.0%; pes planus 22.0% (colin2023genidaaparticipatory pages 7-9, colin2023genidaaparticipatory pages 3-4)
  - Suggested HPO: *Joint hypermobility* (HP:0001382), *Scoliosis* (HP:0002650), *Developmental dysplasia of the hip* (HP:0001374), *Pes planus* (HP:0001763)

#### Congenital anomalies and organ involvement
- **Cardiac defects:** ASD 18.9%; VSD 10.9% (GenIDA) (colin2023genidaaparticipatory pages 3-4)
  - Suggested HPO: *Atrial septal defect* (HP:0001631), *Ventricular septal defect* (HP:0001629)
- **Renal/urogenital issues:** ~38.3%; male cryptorchidism 22.6% (GenIDA) and 45.7% among males in St John cohort (colin2023genidaaparticipatory pages 3-4, john2023expandingthespeech pages 2-2)
  - Suggested HPO: *Cryptorchidism* (HP:0000028)

#### Sleep, dental, sensory, behavior
- **Sleep disorders:** 42.6% (GenIDA) and 40.7% (St John cohort) (colin2023genidaaparticipatory pages 3-4, john2023expandingthespeech pages 2-2)
  - Suggested HPO: *Sleep disturbance* (HP:0002360)
- **Dental problems:** 65.1% (GenIDA); 50% (36/72) in St John cohort (colin2023genidaaparticipatory pages 3-4, john2023expandingthespeech pages 2-2)
  - Suggested HPO: *Abnormality of dentition* (HP:0006482)
- **Vision/hearing:** hypermetropia 38.8%, strabismus 34.7%, hearing problems 40.8% (colin2023genidaaparticipatory pages 6-7)
  - Suggested HPO: *Hyperopia* (HP:0000540), *Strabismus* (HP:0000486), *Hearing impairment* (HP:0000365)
- **Behavior:** behavioral problems 54.8%; repetitive behaviors 35.2%; attention deficit 32.7%; anxiety 31.2%; hyperactivity 27.6%; sociability high with familiar adults 98.1% and children 88.6% (colin2023genidaaparticipatory pages 6-7)
  - Suggested HPO: *Stereotypy* (HP:0000733), *Attention deficit hyperactivity disorder* (HP:0007018), *Anxiety* (HP:0000739)

### 3.2 Quality of life and adaptive function
The 2023 speech/language cohort reported relative strengths in social competence and behavioral/emotional control, but communication difficulties impacted daily living skills (john2023expandingthespeech pages 1-2).

---

## 4. Genetic/Molecular Information

### 4.1 Causal gene(s)
- **KANSL1** (haploinsufficiency) is central to KdVS pathogenesis; causal by deletion or intragenic variant (colin2023genidaaparticipatory pages 2-3, houser2025neuroimagingofkoolende pages 2-8).

### 4.2 Variant spectrum (examples and classes)
- **Recurrent CNV:** typical **500–650 kb** 17q21.31 deletion (houser2025neuroimagingofkoolende pages 2-8, john2023expandingthespeech pages 2-2)
- **Intragenic KANSL1 variants:** predominately truncating/frameshift/splice; exon deletions also observed in a large cohort (john2023expandingthespeech pages 3-4)
- **Missense/VUS interpretation:** 2024 episignature work provides a framework for classifying missense variants (p.Thr887Met vs p.Gly900Glu) using blood methylation signatures (awamleh2024anewblood pages 3-5)

### 4.3 Genotype–phenotype correlations
- Large cohorts reported **no significant clinical differences** between 17q21.31 deletion and KANSL1 intragenic variant groups (colin2023genidaaparticipatory pages 2-3, john2023expandingthespeech pages 3-4).

### 4.4 Epigenetic information (2024–key development)
A 2024 European Journal of Human Genetics study identified a **blood DNA methylation episignature** of **456 CpG sites** for KdVS and used an SVM classifier to support diagnosis and classify KANSL1 VUS (awamleh2024anewblood pages 1-2, awamleh2024anewblood pages 2-3).

---

## 5. Environmental Information
No specific environmental contributors, protective factors, or infectious triggers were supported by the retrieved KdVS-focused evidence.

---

## 6. Mechanism / Pathophysiology

### 6.1 Core mechanistic chain (evidence-backed)
**KANSL1 haploinsufficiency → dysregulated chromatin/NSL complex function and H4K16 acetylation → transcriptional dysregulation of autophagy machinery and cellular homeostasis → oxidative stress, impaired lysosomal/autophagic clearance and synaptic dysfunction → neurodevelopmental phenotype; plus cardiac dysfunction in mouse models.** (linda2022imbalancedautophagycauses pages 1-3, li2022kansl1haploinsufficiencyimpairs pages 1-2)

### 6.2 Autophagy/lysosome and oxidative stress (human neuronal models)
In KANSL1-deficient human iPSC-derived neurons, decreased **SOD1** leads to increased oxidative stress and autophagosome accumulation; autophagosomes accumulate at excitatory synapses with reduced synaptic density and reduced AMPA receptor-mediated transmission, impairing network activity. Antioxidant/oxidative stress reduction rescued autophagosomes and neuronal function. (linda2022imbalancedautophagycauses pages 1-3)

**Direct abstract quotes (primary literature):**
- “In KANSL1-deficient neurons, autophagosome accumulation at excitatory synapses resulted in reduced synaptic density, reduced GRIA/AMPA receptor-mediated transmission and impaired neuronal network activity.” (linda2022imbalancedautophagycauses pages 1-3)
- “By pharmacologically reducing oxidative stress, we could rescue the aberrant autophagosome formation as well as synaptic and neuronal network activity in KANSL1-deficient neurons.” (linda2022imbalancedautophagycauses pages 1-3)

### 6.3 Autophagosome–lysosome fusion and mitophagy (mouse model)
A Nature Communications mouse study identified KANSL1 as essential for autophagy and showed KANSL1 modulates **autophagosome–lysosome fusion** via transcriptional regulation of **STX17**. Kansl1+/− mice show impaired clearance of damaged mitochondria, increased ROS, and neuronal/cardiac dysfunction; **13-cis retinoic acid** reversed mitophagic defects and neurobehavioral abnormalities. (li2022kansl1haploinsufficiencyimpairs pages 1-2)

### 6.4 Suggested ontology terms
- **GO Biological Process (examples):** autophagy (GO:0006914), mitophagy (GO:0000422), autophagosome maturation (GO:0097352), lysosome organization (GO:0007040), oxidative stress response (GO:0006979), synapse organization (GO:0050808)
- **Cell Ontology (CL) (examples):** excitatory neuron (CL:0008030), neural progenitor cell (CL:0000047), cardiomyocyte (CL:0000746)
- **UBERON (examples):** brain (UBERON:0000955), hippocampus (UBERON:0001954), heart (UBERON:0000948)

---

## 7. Anatomical Structures Affected
From cohort data, the primary impacted system is the nervous system, with frequent multisystem involvement:
- **CNS/neurodevelopment:** developmental delay, ID, seizures; imaging anomalies in a subset (john2023expandingthespeech pages 2-2)
- **Cardiac:** ASD/VSD and other defects in substantial fractions (colin2023genidaaparticipatory pages 3-4, john2023expandingthespeech pages 2-2)
- **Renal/urogenital:** relatively common (colin2023genidaaparticipatory pages 3-4)
- **Musculoskeletal:** hypermobility/scoliosis, etc. (colin2023genidaaparticipatory pages 7-9)

---

## 8. Temporal Development
- **Onset:** typically congenital/early childhood, reflected in early hypotonia and feeding difficulties (colin2023genidaaparticipatory pages 3-4)
- **Motor milestone timing (median):** sitting 10.7 mo, standing 17.5 mo, walking 23.4 mo (colin2023genidaaparticipatory pages 3-4)
- **Seizure onset:** mean 3.4y; median 2.0y (colin2023genidaaparticipatory pages 7-9)
- **Developmental course:** registry modeling indicates positive trajectory for speech/language and relatively good reading ability over time (colin2023genidaaparticipatory pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
- **Estimated prevalence:** approximately **1:55,000 births** for the 17q21.31 deletion (houser2025neuroimagingofkoolende pages 2-8, prat2021ocularmanifestationsand pages 4-4)

### 9.2 Population demographics
- No sex predilection suggested by near-equal male/female distribution in GenIDA and other sources (colin2023genidaaparticipatory pages 3-4)

---

## 10. Diagnostics

### 10.1 Genetic testing (current practice)
Diagnosis is molecular and includes:
- **Chromosomal microarray (CMA)** to detect 17q21.31 deletions
- **Single-gene testing / multigene panels** for KANSL1 variants
- Broader genomic approaches when phenotype is atypical (houser2025neuroimagingofkoolende pages 2-8)

### 10.2 Omics-based diagnostics (major 2024 development)
A 2024 study developed a **blood DNA methylation episignature** (456 CpGs) and demonstrated diagnostic utility for classification of KANSL1 VUS and atypical cases, with validation case scores 75–92% vs controls 0–13%. (awamleh2024anewblood pages 2-3, awamleh2024anewblood pages 1-2)

**Direct abstract quote (Awamleh 2024):** “In this study, we identified a robust DNAm signature of 456 significant CpG sites…” (awamleh2024anewblood pages 1-2)

### 10.3 Differential diagnosis
Differential diagnoses are not systematically enumerated in the retrieved evidence; however, KdVS is placed among syndromic neurodevelopmental disorders with overlapping features, and facial/speech phenotyping tools are used in the broader field (e.g., NDD cohorts referenced indirectly). Evidence in this run is insufficient to list a complete differential.

---

## 11. Outcome/Prognosis
- **Natural history:** improvements in speech/language over time and continuing gains beyond childhood are supported by registry modeling and cohort interpretation (colin2023genidaaparticipatory pages 1-2, john2023expandingthespeech pages 1-2).
- **Life expectancy / mortality:** Not found in retrieved evidence.

---

## 12. Treatment

### 12.1 Current standard management (real-world implementation)
There is no curative therapy described in clinical summaries; management is symptomatic and multidisciplinary, including physiotherapy for motor delays, speech/feeding therapy, and educational supports, with multispecialty monitoring (houser2025neuroimagingofkoolende pages 2-8).

Speech/language recommendations (2023 cohort) emphasize early AAC and ongoing targeted therapy across development. (john2023expandingthespeech pages 1-2)

### 12.2 Epilepsy management (real-world observational data)
Caregiver-reported medication effectiveness in GenIDA suggested reported efficacy for **valproate (83%)** and **levetiracetam (67% good efficacy among reporters)**, with additional reported effectiveness of valproate and oxcarbazepine at cohort level. (colin2023genidaaparticipatory pages 7-9, colin2023genidaaparticipatory pages 1-2)

### 12.3 Experimental / translational therapeutic leads
- **Mouse model pharmacologic rescue:** FDA-approved **13-cis retinoic acid** reversed mitophagic defects and neurobehavioral abnormalities in Kansl1+/− mice (li2022kansl1haploinsufficiencyimpairs pages 1-2).
- **Human neuronal model rescue:** pharmacologic reduction of oxidative stress rescued autophagosome accumulation and synaptic/network activity (linda2022imbalancedautophagycauses pages 1-3).

### 12.4 Trial readiness and research infrastructure (expert/authoritative perspective)
A 2024 review describing the KdVS Foundation’s strategy emphasizes models, registries, natural history, and translational funding, with a stated goal of a first clinical trial in late 2026. (pfalzer2024koolendevriessyndrome pages 2-3)

### 12.5 MAXO term suggestions (examples)
- Physical therapy (MAXO:0000011)
- Speech therapy (MAXO:0000016)
- Feeding therapy / nutritional support (MAXO:0000082; descriptive)
- Anticonvulsant therapy (MAXO:0000749)

---

## 13. Prevention
Primary prevention is not applicable to the de novo genetic cause, but **genetic counseling** is relevant given the autosomal dominant, typically de novo etiology. (houser2025neuroimagingofkoolende pages 2-8, saxena2021koolen‐devriessyndrome pages 2-4)

---

## 14. Other Species / Natural Disease
No evidence of naturally occurring KdVS-equivalent disease in non-human species was retrieved. KANSL1 is conserved and studied in model organisms, but veterinary natural disease evidence is not available in the retrieved texts.

---

## 15. Model Organisms
- **Mouse model (Kansl1+/−):** links KANSL1 to autophagosome–lysosome fusion, mitophagy/ROS, and neuronal/cardiac dysfunction; provides a preclinical pharmacologic rescue (13-cis retinoic acid). (li2022kansl1haploinsufficiencyimpairs pages 1-2)
- **Human iPSC-derived neuron models:** show oxidative stress/autophagy imbalance and synaptic transmission/network deficits with rescue by reducing oxidative stress. (linda2022imbalancedautophagycauses pages 1-3)

---

## Evidence Gaps (limitations of this run)
- **MONDO, Orphanet, MeSH, ICD-10/11 codes** were not extractable from the retrieved full-text chunks and thus cannot be cited here.
- **Mortality/life expectancy statistics** and **formal clinical diagnostic criteria** (beyond molecular testing) were not found in the retrieved evidence.
- **Comprehensive differential diagnosis lists** and **environmental modifiers** were not supported by the current evidence set.

---

## High-utility Summary Table
The following artifact condenses the key actionable facts (identifiers, genetics, prevalence, phenotype frequencies, and 2024 diagnostic episignature metrics) with URLs and publication dates.

| Category | Data point | Value/description | Source (author/year/journal) | URL | Pub date |
|---|---|---|---|---|---|
| Disease information | Primary disease name | Koolen-de Vries syndrome (KdVS); rare multisystem neurodevelopmental disorder caused by 17q21.31 deletion including **KANSL1** or heterozygous intragenic **KANSL1** pathogenic variant (colin2023genidaaparticipatory pages 2-3, houser2025neuroimagingofkoolende pages 2-8) | Colin et al. 2023, *Genetics in Medicine Open*; Houser et al. 2025, *Cureus* | https://doi.org/10.1016/j.gimo.2023.100817; https://doi.org/10.7759/cureus.79194 | 2023-01; 2025-02 |
| Disease information | Key identifier | OMIM **610443** (reported in GenIDA KdVS cohort excerpt) (colin2023genidaaparticipatory pages 2-3) | Colin et al. 2023, *Genetics in Medicine Open* | https://doi.org/10.1016/j.gimo.2023.100817 | 2023-01 |
| Disease information | Common synonyms | 17q21.31 microdeletion syndrome; KANSL1-related intellectual disability syndrome (colin2023genidaaparticipatory pages 2-3, farne2022koolen‐devriessyndrome pages 10-12) | Colin et al. 2023, *Genetics in Medicine Open*; Farnè et al. 2022, *Am J Med Genet A* | https://doi.org/10.1016/j.gimo.2023.100817; https://doi.org/10.1002/ajmg.a.62536 | 2023-01; 2022-10 |
| Genetic etiology | Typical recurrent deletion | Typical recurrent **17q21.31 deletion ~500–650 kb**; cohort wording also notes recurrent deletion spanning ~43.7–44.25 Mb region (john2023expandingthespeech pages 3-4, houser2025neuroimagingofkoolende pages 2-8) | St John et al. 2023, *Eur J Hum Genet*; Houser et al. 2025, *Cureus* | https://doi.org/10.1038/s41431-022-01230-7; https://doi.org/10.7759/cureus.79194 | 2023-12; 2025-02 |
| Genetic etiology | Deletion vs sequence variant proportion | About **60%** due to heterozygous 17q21.31 deletion and **40%** due to **KANSL1** sequence variants in one review excerpt (houser2025neuroimagingofkoolende pages 2-8) | Houser et al. 2025, *Cureus* | https://doi.org/10.7759/cureus.79194 | 2025-02 |
| Genetic etiology | GenIDA genotype counts | In GenIDA cohort, **157** individuals with 17q21.31 deletion and **40** with pathogenic **KANSL1** variant; no major clinical differences detected between groups (colin2023genidaaparticipatory pages 2-3) | Colin et al. 2023, *Genetics in Medicine Open* | https://doi.org/10.1016/j.gimo.2023.100817 | 2023-01 |
| Genetic etiology | 2023 speech cohort genotype counts | In speech/language cohort (n=81), **56/81 (69.1%)** had typical 17q21.31 deletion and **19/81** had KANSL1-only sequence variants; no group score differences reported between deletion and KANSL1-variant groups (john2023expandingthespeech pages 2-2, john2023expandingthespeech pages 3-4) | St John et al. 2023, *Eur J Hum Genet* | https://doi.org/10.1038/s41431-022-01230-7 | 2023-12 |
| Genetic etiology | Variant classes observed | Predominantly loss-of-function intragenic variants: truncating, frameshift, splice-site, small intragenic exon deletion; 2024 episignature study also discusses missense/nonsense/frameshift/deletion-insertion/mosaic variants for classification (john2023expandingthespeech pages 3-4, awamleh2024anewblood pages 3-5) | St John et al. 2023, *Eur J Hum Genet*; Awamleh et al. 2024, *Eur J Hum Genet* | https://doi.org/10.1038/s41431-022-01230-7; https://doi.org/10.1038/s41431-024-01538-6 | 2023-12; 2024-01 |
| Inheritance/epidemiology | Inheritance pattern | Autosomal dominant; typically de novo disease mechanism highlighted in KdVS descriptions (houser2025neuroimagingofkoolende pages 2-8, prat2021ocularmanifestationsand pages 4-4, saxena2021koolen‐devriessyndrome pages 2-4) | Houser et al. 2025, *Cureus*; Prat et al. 2021, *Ophthalmic Genetics*; Saxena et al. 2021, *Am J Med Genet A* | https://doi.org/10.7759/cureus.79194; https://doi.org/10.1080/13816810.2020.1868012; https://doi.org/10.1002/ajmg.a.62008 | 2025-02; 2021-01; 2021-12 |
| Inheritance/epidemiology | Estimated prevalence | Estimated prevalence for 17q21.31 deletion approximately **1:55,000 births** (houser2025neuroimagingofkoolende pages 2-8, prat2021ocularmanifestationsand pages 4-4) | Houser et al. 2025, *Cureus*; Prat et al. 2021, *Ophthalmic Genetics* | https://doi.org/10.7759/cureus.79194; https://doi.org/10.1080/13816810.2020.1868012 | 2025-02; 2021-01 |
| Epidemiology | Sex distribution in GenIDA | **116 males / 121 females**; mean age **14.0 years** in GenIDA cohort (colin2023genidaaparticipatory pages 3-4) | Colin et al. 2023, *Genetics in Medicine Open* | https://doi.org/10.1016/j.gimo.2023.100817 | 2023-01 |
| Epidemiology | Sex/age in speech cohort | **35 female / 46 male**; age **1.5–40.2 years**, mean **9 years 10 months** (john2023expandingthespeech pages 2-2) | St John et al. 2023, *Eur J Hum Genet* | https://doi.org/10.1038/s41431-022-01230-7 | 2023-12 |
| Phenotypes (GenIDA 2023) | Prenatal/perinatal problems | **77.9%** (colin2023genidaaparticipatory pages 3-4) | Colin et al. 2023, *Genetics in Medicine Open* | https://doi.org/10.1016/j.gimo.2023.100817 | 2023-01 |
| Phenotypes (GenIDA 2023) | Hypotonia | **61.5%** (colin2023genidaaparticipatory pages 3-4) | Colin et al. 2023, *Genetics in Medicine Open* | https://doi.org/10.1016/j.gimo.2023.100817 | 2023-01 |
| Phenotypes (GenIDA 2023) | Feeding difficulties | **60.2%** (colin2023genidaaparticipatory pages 3-4) | Colin et al. 2023, *Genetics in Medicine Open* | https://doi.org/10.1016/j.gimo.2023.100817 | 2023-01 |
| Phenotypes (GenIDA 2023) | Intellectual disability | Formal ID diagnosis in **89.2%**; severity: mild **16.9%**, moderate **60.2%**, severe **2.4%**, profound **20.5%** (colin2023genidaaparticipatory pages 3-4) | Colin et al. 2023, *Genetics in Medicine Open* | https://doi.org/10.1016/j.gimo.2023.100817 | 2023-01 |
| Phenotypes (GenIDA 2023) | Epilepsy | **47.3% (97/204)** with epilepsy/seizures (colin2023genidaaparticipatory pages 6-7, colin2023genidaaparticipatory pages 3-4) | Colin et al. 2023, *Genetics in Medicine Open* | https://doi.org/10.1016/j.gimo.2023.100817 | 2023-01 |
| Phenotypes (GenIDA 2023) | Seizure types among seizure cases | Tonic-clonic **38.1%**, absence **28.9%**, complex partial **22.7%**, nocturnal **21.6%**, febrile convulsions **19.6%**, infantile spasms **14.4%**, atonic **9.3%** (colin2023genidaaparticipatory pages 6-7) | Colin et al. 2023, *Genetics in Medicine Open* | https://doi.org/10.1016/j.gimo.2023.100817 | 2023-01 |
| Phenotypes (GenIDA 2023) | Age at first seizure | Average **3.4 years**, median **2.0 years** (colin2023genidaaparticipatory pages 7-9) | Colin et al. 2023, *Genetics in Medicine Open* | https://doi.org/10.1016/j.gimo.2023.100817 | 2023-01 |
| Phenotypes (GenIDA 2023) | Speech/language delay | **73.6%** in children >2 years; first words average **2.2 years** (colin2023genidaaparticipatory pages 3-4) | Colin et al. 2023, *Genetics in Medicine Open* | https://doi.org/10.1016/j.gimo.2023.100817 | 2023-01 |
| Phenotypes (GenIDA 2023) | Motor milestone delay | Median sit **10.7 mo**, stand **17.5 mo**, walk **23.4 mo** (colin2023genidaaparticipatory pages 3-4) | Colin et al. 2023, *Genetics in Medicine Open* | https://doi.org/10.1016/j.gimo.2023.100817 | 2023-01 |
| Phenotypes (GenIDA 2023) | Musculoskeletal findings | Joint laxity **50.0%**, scoliosis **25.5%**, hip dislocation/dysplasia **18.0%**, pes planus **22.0%**; musculoskeletal anomalies overall **75.5%** in later excerpt (colin2023genidaaparticipatory pages 3-4, colin2023genidaaparticipatory pages 7-9) | Colin et al. 2023, *Genetics in Medicine Open* | https://doi.org/10.1016/j.gimo.2023.100817 | 2023-01 |
| Phenotypes (GenIDA 2023) | Sleep disorders | **42.6%** (colin2023genidaaparticipatory pages 3-4) | Colin et al. 2023, *Genetics in Medicine Open* | https://doi.org/10.1016/j.gimo.2023.100817 | 2023-01 |
| Phenotypes (GenIDA 2023) | Dental problems | **65.1%** (colin2023genidaaparticipatory pages 3-4) | Colin et al. 2023, *Genetics in Medicine Open* | https://doi.org/10.1016/j.gimo.2023.100817 | 2023-01 |
| Phenotypes (GenIDA 2023) | Cardiac anomalies | Atrial septal defect **18.9%**; ventricular septal defect **10.9%** (colin2023genidaaparticipatory pages 3-4, colin2023genidaaparticipatory pages 6-7) | Colin et al. 2023, *Genetics in Medicine Open* | https://doi.org/10.1016/j.gimo.2023.100817 | 2023-01 |
| Phenotypes (GenIDA 2023) | Renal/urogenital issues | Approximately **38.3%**; male cryptorchidism **22.6%** (colin2023genidaaparticipatory pages 3-4, colin2023genidaaparticipatory pages 7-9) | Colin et al. 2023, *Genetics in Medicine Open* | https://doi.org/10.1016/j.gimo.2023.100817 | 2023-01 |
| Phenotypes (GenIDA 2023) | Vision/hearing | Hypermetropia **38.8%**, strabismus **34.7%**; hearing problems **40.8%**, deafness **12.2%** (colin2023genidaaparticipatory pages 6-7) | Colin et al. 2023, *Genetics in Medicine Open* | https://doi.org/10.1016/j.gimo.2023.100817 | 2023-01 |
| Phenotypes (GenIDA 2023) | Respiratory issues | Respiratory issues **39.8%**; laryngomalacia **15.4%**; tracheomalacia **8.5%**; asthma **16.4%**; recurrent pneumonia noted in 13 persons (colin2023genidaaparticipatory pages 6-7, colin2023genidaaparticipatory pages 7-9, colin2023genidaaparticipatory pages 1-2) | Colin et al. 2023, *Genetics in Medicine Open* | https://doi.org/10.1016/j.gimo.2023.100817 | 2023-01 |
| Phenotypes (GenIDA 2023) | Behavioral profile | Behavioral problems **54.8%**; repetitive behaviors **35.2%**, attention deficit **32.7%**, anxiety **31.2%**, obsessive behavior **29.6%**, hyperactivity **27.6%**; sociable with familiar adults **98.1%** and children **88.6%** (colin2023genidaaparticipatory pages 6-7, colin2023genidaaparticipatory pages 7-9) | Colin et al. 2023, *Genetics in Medicine Open* | https://doi.org/10.1016/j.gimo.2023.100817 | 2023-01 |
| Phenotypes (EJHG speech cohort 2023) | Developmental delay | **78/81 (96.3%)** (john2023expandingthespeech pages 2-2) | St John et al. 2023, *Eur J Hum Genet* | https://doi.org/10.1038/s41431-022-01230-7 | 2023-12 |
| Phenotypes (EJHG speech cohort 2023) | Dysmorphic features | **73/81 (90.1%)**; pear-shaped bulbous nose **48/81 (59.3%)** (john2023expandingthespeech pages 2-2) | St John et al. 2023, *Eur J Hum Genet* | https://doi.org/10.1038/s41431-022-01230-7 | 2023-12 |
| Phenotypes (EJHG speech cohort 2023) | Intellectual disability | Among assessed individuals (n=56), **49/56 (87.5%)** had ID; **51.8% moderate**, **19.6% severe** (john2023expandingthespeech pages 2-2) | St John et al. 2023, *Eur J Hum Genet* | https://doi.org/10.1038/s41431-022-01230-7 | 2023-12 |
| Phenotypes (EJHG speech cohort 2023) | Structural brain anomalies | **33/62 (53.2%)** with imaging had structural brain anomalies (john2023expandingthespeech pages 2-2) | St John et al. 2023, *Eur J Hum Genet* | https://doi.org/10.1038/s41431-022-01230-7 | 2023-12 |
| Phenotypes (EJHG speech cohort 2023) | Epilepsy/seizures | **29/81 (35.8%)** (john2023expandingthespeech pages 2-2) | St John et al. 2023, *Eur J Hum Genet* | https://doi.org/10.1038/s41431-022-01230-7 | 2023-12 |
| Phenotypes (EJHG speech cohort 2023) | Hearing loss | **24/81 (29.6%)**, often moderate and conductive (john2023expandingthespeech pages 2-2) | St John et al. 2023, *Eur J Hum Genet* | https://doi.org/10.1038/s41431-022-01230-7 | 2023-12 |
| Phenotypes (EJHG speech cohort 2023) | Cardiac/musculoskeletal/sleep | Cardiac defects **32/81 (39.5%)**; musculoskeletal problems **32/81 (39.5%)**; sleep disturbances **33/81 (40.7%)** (john2023expandingthespeech pages 2-2) | St John et al. 2023, *Eur J Hum Genet* | https://doi.org/10.1038/s41431-022-01230-7 | 2023-12 |
| Phenotypes (EJHG speech cohort 2023) | Other systemic features | Dental problems **36/72 (50.0%)**; renal/urogenital complications **25/81 (30.9%)**; GI concerns **24/81 (29.6%)**; mental health problems **23/81 (28.4%)**; cryptorchidism **21/46 (45.7%)** of males (john2023expandingthespeech pages 2-2) | St John et al. 2023, *Eur J Hum Genet* | https://doi.org/10.1038/s41431-022-01230-7 | 2023-12 |
| Phenotypes (EJHG speech cohort 2023) | Verbal status | **62/81 (76.5%)** verbal; minimally verbal participants used AAC successfully (john2023expandingthespeech pages 1-2) | St John et al. 2023, *Eur J Hum Genet* | https://doi.org/10.1038/s41431-022-01230-7 | 2023-12 |
| Phenotypes (EJHG speech cohort 2023) | Motor speech disorders | Apraxia in **39/61 (63.9%)** verbal participants; dysarthria in **28/61 (45.9%)** (john2023expandingthespeech pages 1-2) | St John et al. 2023, *Eur J Hum Genet* | https://doi.org/10.1038/s41431-022-01230-7 | 2023-12 |
| Phenotypes (EJHG speech cohort 2023) | Stuttering | **36/47 (76.6%)** of verbal participants; described as late-onset and fluctuating (john2023expandingthespeech pages 1-2) | St John et al. 2023, *Eur J Hum Genet* | https://doi.org/10.1038/s41431-022-01230-7 | 2023-12 |
| Diagnostics / omics | 2024 blood DNAm episignature cohort | Whole-blood DNAm profiled in **13** individuals with KANSL1 variants, **4** with 17q21.31 microdeletions, and **21** controls using Illumina EPIC array (awamleh2024anewblood pages 1-2) | Awamleh et al. 2024, *Eur J Hum Genet* | https://doi.org/10.1038/s41431-024-01538-6 | 2024-01 |
| Diagnostics / omics | 2024 episignature size | Robust blood DNA methylation signature of **456 significant CpG sites** (awamleh2024anewblood pages 1-2, awamleh2024anewblood pages 2-3) | Awamleh et al. 2024, *Eur J Hum Genet* | https://doi.org/10.1038/s41431-024-01538-6 | 2024-01 |
| Diagnostics / omics | Discovery and validation | Discovery cohort **n=8** KdVS cases; independent validation cohort **n=8**; validation SVM scores for KdVS cases **75–92%** vs controls **0–13%** (awamleh2024anewblood pages 5-7, awamleh2024anewblood pages 2-3, awamleh2024anewblood pages 7-8) | Awamleh et al. 2024, *Eur J Hum Genet* | https://doi.org/10.1038/s41431-024-01538-6 | 2024-01 |
| Diagnostics / omics | Variant classification utility | Used to classify **2 KANSL1 VUS** and **4 atypical-presentation variants**; one missense p.Thr887Met scored KdVS-like (~**72%**), while p.Gly900Glu scored control-like (~**4.7%**) (awamleh2024anewblood pages 3-5, awamleh2024anewblood pages 1-2, awamleh2024anewblood pages 7-8) | Awamleh et al. 2024, *Eur J Hum Genet* | https://doi.org/10.1038/s41431-024-01538-6 | 2024-01 |
| Diagnostics / omics | Microdeletion vs sequence variant DNAm difference | No significant DNAm difference between 17q21.31 microdeletion carriers and KANSL1 sequence-variant carriers (**adjusted p = 0.34**) (awamleh2024anewblood pages 2-3) | Awamleh et al. 2024, *Eur J Hum Genet* | https://doi.org/10.1038/s41431-024-01538-6 | 2024-01 |


*Table: This table condenses the most actionable disease-level facts for Koolen-de Vries syndrome, including identifiers, causal genetics, prevalence, major 2023 cohort phenotype frequencies, and the 2024 DNA methylation episignature findings. It is useful as a quick-reference artifact for knowledge-base population and evidence-backed summarization.*

References

1. (colin2023genidaaparticipatory pages 2-3): Florent Colin, Pauline Burger, Timothée Mazzucotelli, Axelle Strehle, Joost Kummeling, Nicole Collot, Elyette Broly, Angela T. Morgan, Kenneth A. Myers, Agnès Bloch-Zupan, Charlotte W. Ockeloen, Bert B.A. de Vries, Tjitske Kleefstra, Pierre Parrend, David A. Koolen, and Jean-Louis Mandel. Genida, a participatory patient registry for genetic forms of intellectual disability provides detailed caregiver-reported information on 237 individuals with koolen-de vries syndrome. Genetics in Medicine Open, 1:100817, Jan 2023. URL: https://doi.org/10.1016/j.gimo.2023.100817, doi:10.1016/j.gimo.2023.100817. This article has 9 citations and is from a peer-reviewed journal.

2. (houser2025neuroimagingofkoolende pages 2-8): Karis Houser, Sara C Esteves, and Michael S. Kuwabara. Neuroimaging of koolen-de vries syndrome: a rare genetic disorder. Cureus, Feb 2025. URL: https://doi.org/10.7759/cureus.79194, doi:10.7759/cureus.79194. This article has 1 citations.

3. (farne2022koolen‐devriessyndrome pages 10-12): Marianna Farnè, Laura Bernardini, Anna Capalbo, Giusy Cavarretta, Barbara Torres, Mariabeatrice Sanchini, Sergio Fini, Alessandra Ferlini, and Stefania Bigoni. Koolen‐de vries syndrome in a 63‐year‐old woman: report of the oldest patient and a review of the adult phenotype. American Journal of Medical Genetics. Part a, 188:692-707, Oct 2022. URL: https://doi.org/10.1002/ajmg.a.62536, doi:10.1002/ajmg.a.62536. This article has 10 citations and is from a peer-reviewed journal.

4. (colin2023genidaaparticipatory pages 3-4): Florent Colin, Pauline Burger, Timothée Mazzucotelli, Axelle Strehle, Joost Kummeling, Nicole Collot, Elyette Broly, Angela T. Morgan, Kenneth A. Myers, Agnès Bloch-Zupan, Charlotte W. Ockeloen, Bert B.A. de Vries, Tjitske Kleefstra, Pierre Parrend, David A. Koolen, and Jean-Louis Mandel. Genida, a participatory patient registry for genetic forms of intellectual disability provides detailed caregiver-reported information on 237 individuals with koolen-de vries syndrome. Genetics in Medicine Open, 1:100817, Jan 2023. URL: https://doi.org/10.1016/j.gimo.2023.100817, doi:10.1016/j.gimo.2023.100817. This article has 9 citations and is from a peer-reviewed journal.

5. (john2023expandingthespeech pages 2-2): Miya St John, Olivia van Reyk, David Koolen, Bert de Vries, David Amor, and Angela Morgan. Expanding the speech and language phenotype in koolen-de vries syndrome: late onset and periodic stuttering a novel feature. European Journal of Human Genetics, 31:531-540, Dec 2023. URL: https://doi.org/10.1038/s41431-022-01230-7, doi:10.1038/s41431-022-01230-7. This article has 18 citations and is from a domain leading peer-reviewed journal.

6. (li2022kansl1haploinsufficiencyimpairs pages 1-2): Tingting Li, Dingyi Lu, C. Yao, Tingting Li, Hua Dong, Zhanqi Li, Guang Xu, Jiayi Chen, Hao Zhang, Xiaoyu Yi, Haizhen Zhu, Guangqin Liu, Kaiqing Wen, Haixin Zhao, Jun Gao, Yakun Zhang, Qiu-Ying Han, Teng Li, Weina Zhang, Jie Zhao, Tao Li, Zhaofang Bai, Moshi Song, Xin Hua He, Tao Zhou, Qing Xia, Ai-ling Li, and Xin Pan. Kansl1 haploinsufficiency impairs autophagosome-lysosome fusion and links autophagic dysfunction with koolen-de vries syndrome in mice. Nature Communications, Feb 2022. URL: https://doi.org/10.1038/s41467-022-28613-0, doi:10.1038/s41467-022-28613-0. This article has 52 citations and is from a highest quality peer-reviewed journal.

7. (linda2022imbalancedautophagycauses pages 1-3): Katrin Linda, Elly I. Lewerissa, Anouk H. A. Verboven, Michele Gabriele, Monica Frega, Teun M. Klein Gunnewiek, Lynn Devilee, Edda Ulferts, Marina Hommersom, Astrid Oudakker, Chantal Schoenmaker, Hans van Bokhoven, Dirk Schubert, Giuseppe Testa, David A. Koolen, Bert B.A. de Vries, and Nael Nadif Kasri. Imbalanced autophagy causes synaptic deficits in a human model for neurodevelopmental disorders. Autophagy, 18:423-442, Jul 2022. URL: https://doi.org/10.1080/15548627.2021.1936777, doi:10.1080/15548627.2021.1936777. This article has 88 citations and is from a domain leading peer-reviewed journal.

8. (saxena2021koolen‐devriessyndrome pages 2-4): Deepti Saxena, Amita Moirangthem, Arya Shambhavi, and Shubha R. Phadke. Koolen‐de vries syndrome: first report of two unrelated indian patients. American Journal of Medical Genetics Part A, 185:982-985, Dec 2021. URL: https://doi.org/10.1002/ajmg.a.62008, doi:10.1002/ajmg.a.62008. This article has 0 citations.

9. (john2023expandingthespeech pages 1-2): Miya St John, Olivia van Reyk, David Koolen, Bert de Vries, David Amor, and Angela Morgan. Expanding the speech and language phenotype in koolen-de vries syndrome: late onset and periodic stuttering a novel feature. European Journal of Human Genetics, 31:531-540, Dec 2023. URL: https://doi.org/10.1038/s41431-022-01230-7, doi:10.1038/s41431-022-01230-7. This article has 18 citations and is from a domain leading peer-reviewed journal.

10. (colin2023genidaaparticipatory pages 6-7): Florent Colin, Pauline Burger, Timothée Mazzucotelli, Axelle Strehle, Joost Kummeling, Nicole Collot, Elyette Broly, Angela T. Morgan, Kenneth A. Myers, Agnès Bloch-Zupan, Charlotte W. Ockeloen, Bert B.A. de Vries, Tjitske Kleefstra, Pierre Parrend, David A. Koolen, and Jean-Louis Mandel. Genida, a participatory patient registry for genetic forms of intellectual disability provides detailed caregiver-reported information on 237 individuals with koolen-de vries syndrome. Genetics in Medicine Open, 1:100817, Jan 2023. URL: https://doi.org/10.1016/j.gimo.2023.100817, doi:10.1016/j.gimo.2023.100817. This article has 9 citations and is from a peer-reviewed journal.

11. (colin2023genidaaparticipatory pages 7-9): Florent Colin, Pauline Burger, Timothée Mazzucotelli, Axelle Strehle, Joost Kummeling, Nicole Collot, Elyette Broly, Angela T. Morgan, Kenneth A. Myers, Agnès Bloch-Zupan, Charlotte W. Ockeloen, Bert B.A. de Vries, Tjitske Kleefstra, Pierre Parrend, David A. Koolen, and Jean-Louis Mandel. Genida, a participatory patient registry for genetic forms of intellectual disability provides detailed caregiver-reported information on 237 individuals with koolen-de vries syndrome. Genetics in Medicine Open, 1:100817, Jan 2023. URL: https://doi.org/10.1016/j.gimo.2023.100817, doi:10.1016/j.gimo.2023.100817. This article has 9 citations and is from a peer-reviewed journal.

12. (john2023expandingthespeech pages 3-4): Miya St John, Olivia van Reyk, David Koolen, Bert de Vries, David Amor, and Angela Morgan. Expanding the speech and language phenotype in koolen-de vries syndrome: late onset and periodic stuttering a novel feature. European Journal of Human Genetics, 31:531-540, Dec 2023. URL: https://doi.org/10.1038/s41431-022-01230-7, doi:10.1038/s41431-022-01230-7. This article has 18 citations and is from a domain leading peer-reviewed journal.

13. (awamleh2024anewblood pages 3-5): Zain Awamleh, Sanaa Choufani, Wendy Wu, Dmitrijs Rots, Alexander J. M. Dingemans, Nael Nadif Kasri, Susana Boronat, Salvador Ibañez-Mico, Laura Cuesta Herraiz, Irene Ferrer, Antonio Martínez Carrascal, Luis A. Pérez-Jurado, Gemma Aznar Lain, Juan Dario Ortigoza-Escobar, Bert B. A. de Vries, David A. Koolen, and Rosanna Weksberg. A new blood dna methylation signature for koolen-de vries syndrome: classification of missense kansl1 variants and comparison to fibroblast cells. European Journal of Human Genetics, 32:324-332, Jan 2024. URL: https://doi.org/10.1038/s41431-024-01538-6, doi:10.1038/s41431-024-01538-6. This article has 13 citations and is from a domain leading peer-reviewed journal.

14. (awamleh2024anewblood pages 1-2): Zain Awamleh, Sanaa Choufani, Wendy Wu, Dmitrijs Rots, Alexander J. M. Dingemans, Nael Nadif Kasri, Susana Boronat, Salvador Ibañez-Mico, Laura Cuesta Herraiz, Irene Ferrer, Antonio Martínez Carrascal, Luis A. Pérez-Jurado, Gemma Aznar Lain, Juan Dario Ortigoza-Escobar, Bert B. A. de Vries, David A. Koolen, and Rosanna Weksberg. A new blood dna methylation signature for koolen-de vries syndrome: classification of missense kansl1 variants and comparison to fibroblast cells. European Journal of Human Genetics, 32:324-332, Jan 2024. URL: https://doi.org/10.1038/s41431-024-01538-6, doi:10.1038/s41431-024-01538-6. This article has 13 citations and is from a domain leading peer-reviewed journal.

15. (awamleh2024anewblood pages 2-3): Zain Awamleh, Sanaa Choufani, Wendy Wu, Dmitrijs Rots, Alexander J. M. Dingemans, Nael Nadif Kasri, Susana Boronat, Salvador Ibañez-Mico, Laura Cuesta Herraiz, Irene Ferrer, Antonio Martínez Carrascal, Luis A. Pérez-Jurado, Gemma Aznar Lain, Juan Dario Ortigoza-Escobar, Bert B. A. de Vries, David A. Koolen, and Rosanna Weksberg. A new blood dna methylation signature for koolen-de vries syndrome: classification of missense kansl1 variants and comparison to fibroblast cells. European Journal of Human Genetics, 32:324-332, Jan 2024. URL: https://doi.org/10.1038/s41431-024-01538-6, doi:10.1038/s41431-024-01538-6. This article has 13 citations and is from a domain leading peer-reviewed journal.

16. (colin2023genidaaparticipatory pages 1-2): Florent Colin, Pauline Burger, Timothée Mazzucotelli, Axelle Strehle, Joost Kummeling, Nicole Collot, Elyette Broly, Angela T. Morgan, Kenneth A. Myers, Agnès Bloch-Zupan, Charlotte W. Ockeloen, Bert B.A. de Vries, Tjitske Kleefstra, Pierre Parrend, David A. Koolen, and Jean-Louis Mandel. Genida, a participatory patient registry for genetic forms of intellectual disability provides detailed caregiver-reported information on 237 individuals with koolen-de vries syndrome. Genetics in Medicine Open, 1:100817, Jan 2023. URL: https://doi.org/10.1016/j.gimo.2023.100817, doi:10.1016/j.gimo.2023.100817. This article has 9 citations and is from a peer-reviewed journal.

17. (prat2021ocularmanifestationsand pages 4-4): Daphna Prat, William R. Katowitz, Alanna Strong, and James A. Katowitz. Ocular manifestations and surgical interventions in pediatric patients with koolen-de-vries syndrome. Ophthalmic Genetics, 42:186-188, Jan 2021. URL: https://doi.org/10.1080/13816810.2020.1868012, doi:10.1080/13816810.2020.1868012. This article has 7 citations and is from a peer-reviewed journal.

18. (pfalzer2024koolendevriessyndrome pages 2-3): Anna C. Pfalzer, Blake Ivers, Alayna Haynam, Barbara Drake, David A. Koolen, Nael Nadif Kasri, Bert B. A. de Vries, Heather C. Mefford, Angela Morgan, Terry Jo Bichell, Elijah Simon, Ananya Terala, Kenneth A. Myers, and Ashley Point. Koolen-de vries syndrome: a journey from diagnosis to treatments. Therapeutic Advances in Rare Disease, Jan 2024. URL: https://doi.org/10.1177/26330040241265414, doi:10.1177/26330040241265414. This article has 1 citations.

19. (awamleh2024anewblood pages 5-7): Zain Awamleh, Sanaa Choufani, Wendy Wu, Dmitrijs Rots, Alexander J. M. Dingemans, Nael Nadif Kasri, Susana Boronat, Salvador Ibañez-Mico, Laura Cuesta Herraiz, Irene Ferrer, Antonio Martínez Carrascal, Luis A. Pérez-Jurado, Gemma Aznar Lain, Juan Dario Ortigoza-Escobar, Bert B. A. de Vries, David A. Koolen, and Rosanna Weksberg. A new blood dna methylation signature for koolen-de vries syndrome: classification of missense kansl1 variants and comparison to fibroblast cells. European Journal of Human Genetics, 32:324-332, Jan 2024. URL: https://doi.org/10.1038/s41431-024-01538-6, doi:10.1038/s41431-024-01538-6. This article has 13 citations and is from a domain leading peer-reviewed journal.

20. (awamleh2024anewblood pages 7-8): Zain Awamleh, Sanaa Choufani, Wendy Wu, Dmitrijs Rots, Alexander J. M. Dingemans, Nael Nadif Kasri, Susana Boronat, Salvador Ibañez-Mico, Laura Cuesta Herraiz, Irene Ferrer, Antonio Martínez Carrascal, Luis A. Pérez-Jurado, Gemma Aznar Lain, Juan Dario Ortigoza-Escobar, Bert B. A. de Vries, David A. Koolen, and Rosanna Weksberg. A new blood dna methylation signature for koolen-de vries syndrome: classification of missense kansl1 variants and comparison to fibroblast cells. European Journal of Human Genetics, 32:324-332, Jan 2024. URL: https://doi.org/10.1038/s41431-024-01538-6, doi:10.1038/s41431-024-01538-6. This article has 13 citations and is from a domain leading peer-reviewed journal.
