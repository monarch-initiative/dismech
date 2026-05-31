---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T09:37:26.676794'
end_time: '2026-05-09T09:54:04.123162'
duration_seconds: 997.45
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: KRAS G12C-Mutant Non-Small Cell Lung Cancer
  mondo_id: ''
  category: ''
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
- **Disease Name:** KRAS G12C-Mutant Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **KRAS G12C-Mutant Non-Small Cell Lung Cancer** covering all of the
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
- **Disease Name:** KRAS G12C-Mutant Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **KRAS G12C-Mutant Non-Small Cell Lung Cancer** covering all of the
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


# Research Report: KRAS G12C‑Mutant Non‑Small Cell Lung Cancer (NSCLC)

## Target Disease
- **Disease name:** KRAS G12C‑mutant non‑small cell lung cancer (advanced/metastatic setting emphasized)
- **MONDO ID:** Not identified in the retrieved sources as a distinct MONDO term for the molecular subtype; nearest disease entities in retrieved ontology evidence include **“non‑small cell lung carcinoma” (EFO_0003060)** and **“lung adenocarcinoma” (EFO_0000571)** with strong association to **KRAS**. (OpenTargets Search: non-small cell lung carcinoma-KRAS)
- **Category:** Thoracic oncology; molecularly defined subtype of NSCLC (commonly lung adenocarcinoma)

---

## 1. Disease Information

### Concise overview
KRAS G12C‑mutant NSCLC refers to NSCLC (most commonly lung adenocarcinoma) in which tumor cells harbor a **somatic KRAS p.G12C** substitution (glycine→cysteine at codon 12). This is a **driver oncogene** alteration that has become clinically actionable through **covalent “OFF‑state” KRAS G12C inhibitors** such as sotorasib and adagrasib. (mina2025emergingtargetedtherapies pages 2-4, sreter2024resistancetokras pages 1-2)

### Key identifiers and terminologies
- **Disease ontology identifiers available from retrieved evidence:**
  - NSCLC: **EFO_0003060** (Open Targets evidence) (OpenTargets Search: non-small cell lung carcinoma-KRAS)
  - Lung adenocarcinoma: **EFO_0000571** (Open Targets evidence) (OpenTargets Search: non-small cell lung carcinoma-KRAS)
- **MeSH / ICD‑10 / ICD‑11 / Orphanet / OMIM:** Not explicitly provided in the retrieved sources for this molecular subtype; therefore not asserted here.

### Common synonyms / alternative names
- “KRASG12C‑mutant NSCLC”
- “KRAS p.G12C‑positive NSCLC”
- “KRAS G12C‑mutated advanced/metastatic NSCLC”
(Usage and wording in clinical trial reporting and reviews.) (dy2023longtermoutcomesand pages 2-3, langen2023sotorasibversusdocetaxel pages 8-10)

### Evidence provenance (individual vs aggregated)
Most information below is derived from:
- **Aggregated clinical-trial evidence** (CodeBreaK 100/200; KRYSTAL‑1 and later analyses) (dy2023longtermoutcomesand pages 2-3, langen2023sotorasibversusdocetaxel pages 8-10)
- **Real‑world observational datasets** (claims/registry cohorts) (sultan2024realworldevaluationof pages 1-2, gecgel2025krasg12cmutation pages 9-11)
- **Preclinical model studies and mechanistic reviews** (resistance/combination rationale) (sreter2024resistancetokras pages 1-2, shaverdashvili2025advancesinthe pages 2-3)

---

## 2. Etiology

### Disease causal factors
- **Primary causal factor (mechanistic):** An activating, oncogenic **KRAS p.G12C** mutation that dysregulates downstream signaling—classically **MAPK/ERK** and **PI3K/AKT/mTOR**—supporting malignant proliferation and survival. (mina2025emergingtargetedtherapies pages 2-4, sreter2024resistancetokras pages 1-2)

### Risk factors
- **Smoking association:** KRAS mutations are reported as more frequent in smokers than nonsmokers (example values: **30% vs 11%**) and more common in Western vs Asian populations (**26% vs 11%**) in a 2024 overview review. (tenekeci2024anupdatedoverview pages 2-3)

### Protective factors
No protective genetic or environmental factors specific to developing **KRAS G12C‑mutant NSCLC** were identified in the retrieved evidence.

### Gene–environment interactions
The retrieved evidence supports a **correlation between smoking exposure and KRAS mutation frequency**, consistent with a gene–environment relationship; however, specific quantitative interaction models were not captured in the retrieved sources. (tenekeci2024anupdatedoverview pages 2-3)

---

## 3. Phenotypes

### Clinical phenotype (NSCLC context)
The retrieved evidence is focused on molecular stratification and treatment outcomes rather than detailed symptom frequencies. As a molecular subtype of NSCLC, phenotypes are generally those of advanced NSCLC; however, **phenotype frequencies and HPO mappings were not reported** in the retrieved clinical-trial excerpts.

### Suggested HPO terms (knowledge-base suggestions; not extracted from the above trials)
Because the phenotype spectrum is not explicitly described in the retrieved sources, the following are **standard NSCLC‑relevant HPO suggestions** for a knowledge base entry (flagged as suggestions rather than evidence‑extracted):
- Cough (HP:0012735)
- Dyspnea (HP:0002094)
- Chest pain (HP:0100749)
- Hemoptysis (HP:0002105)
- Weight loss (HP:0001824)
- Fatigue (HP:0012378)
- Metastatic lesions (HP:0033006; broad)

---

## 4. Genetic / Molecular Information

### Causal gene
- **KRAS** (KRAS proto‑oncogene, GTPase) is strongly associated with NSCLC and lung adenocarcinoma in Open Targets evidence. (OpenTargets Search: non-small cell lung carcinoma-KRAS)

### Pathogenic variant
- **KRAS p.G12C** (somatic missense) is a canonical oncogenic driver in lung adenocarcinoma and the key actionable allele for currently approved direct KRAS inhibitors in NSCLC. (sreter2024resistancetokras pages 1-2, mina2025emergingtargetedtherapies pages 2-4)

### Co-mutations / molecular modifiers (prognostic and predictive)
Co‑alterations shape prognosis and response to KRAS G12C inhibitors.
- In a clinico‑genomic analysis of **adagrasib‑treated** KRAS G12C NSCLC (KRYSTAL‑1), **KEAP1** and **STK11** co‑mutations were associated with markedly worse outcomes:
  - KEAP1: PFS **4.1 vs 9.9 months**; OS **5.4 vs 19.0 months** (HRs ~2.7–3.6; P<0.01) (negrao2025impactofcomutations pages 1-2)
  - STK11: PFS **4.2 vs 11.0 months**; OS **9.8 months vs not reached** (HRs ~2.2–2.6; P<0.01) (negrao2025impactofcomutations pages 1-2)
- High **NRF2** signaling (including KEAP1/NRF2 axis activation) correlated with shorter survival on adagrasib even in KEAP1WT tumors. (negrao2025impactofcomutations pages 1-2)
- A favorable molecular group (**KEAP1WT/STK11WT/NRF2LOW**) represented ~**32%** of adagrasib‑treated patients and showed longer PFS and OS than comparison groups in that analysis. (negrao2025impactofcomutations pages 1-2)

### Functional consequence (high-level)
The KRAS G12C mutation yields a KRAS protein state exploitable by covalent inhibitors that bind the cysteine at position 12 and stabilize the GDP‑bound (inactive) form. (mina2025emergingtargetedtherapies pages 2-4, tenekeci2024anupdatedoverview pages 2-3)

### Suggested GO terms (mechanism-oriented; consistent with retrieved pathway statements)
- MAPK cascade (GO:0000165) (sreter2024resistancetokras pages 1-2)
- PI3K/AKT signaling (GO:0014065; broad) (sreter2024resistancetokras pages 1-2)
- Regulation of cell proliferation (GO:0042127; broad)

---

## 5. Environmental Information

### Key environmental/lifestyle factors
- **Tobacco smoke exposure** is the most clearly supported lifestyle association in the retrieved evidence through its association with higher KRAS mutation frequency. (tenekeci2024anupdatedoverview pages 2-3)

No infectious agents specific to this molecular subtype were identified in the retrieved evidence.

---

## 6. Mechanism / Pathophysiology

### Core signaling pathways
KRAS activation drives downstream oncogenic signaling including:
- **MAPK pathway** (RAF–MEK–ERK axis) and
- **PI3K–AKT–mTOR axis**
as summarized in recent reviews of KRAS‑mutant NSCLC and KRAS inhibition resistance. (sreter2024resistancetokras pages 1-2, mina2025emergingtargetedtherapies pages 2-4)

### Therapeutic mechanism of KRAS G12C inhibitors
Covalent KRAS G12C inhibitors exploit the mutant cysteine to bind KRAS in a state that reduces signaling output; nonetheless, clinical activity is often limited by adaptive and acquired resistance. (mina2025emergingtargetedtherapies pages 2-4, shaverdashvili2025advancesinthe pages 2-3)

### Resistance mechanisms (current understanding)
The retrieved evidence emphasizes that resistance to KRAS G12C inhibition is frequent and can be:
- **On‑target** (secondary KRAS alterations preventing drug binding) and
- **Off‑target / bypass** (reactivation via alternative oncogenic nodes or pathways), including RTK‑driven upstream reactivation and downstream pathway rewiring. (shaverdashvili2025advancesinthe pages 2-3)

A high‑impact 2024 preclinical study supports a concrete combination rationale:
- Co‑targeting **SOS1** (using BI‑3406) plus the KRAS G12C inhibitor **adagrasib** produced stronger suppression of RAS–MAPK signaling, delayed acquired resistance, and restored responses in adagrasib‑resistant models; resistance was associated with **MRAS** activity, which SOS1 and SHP2 inhibition can suppress. (sreter2024resistancetokras pages 1-2)

### Cell types (CL) and tissues (UBERON)
The evidence is primarily genotype/therapy focused; histology indicates most cases are **lung adenocarcinoma** (UBERON:0002048 lung; tissue subtype not explicitly curated in retrieved excerpts). (OpenTargets Search: non-small cell lung carcinoma-KRAS)

---

## 7. Anatomical Structures Affected

- **Primary organ:** Lung (NSCLC; often lung adenocarcinoma). (OpenTargets Search: non-small cell lung carcinoma-KRAS)
- **Central nervous system involvement:** CodeBreaK 100 included an intracranial efficacy subset (16 evaluable) with intracranial complete responses and high intracranial disease control on sotorasib, supporting clinically relevant CNS metastatic disease considerations in this population. (dy2023longtermoutcomesand pages 2-3)

Suggested ontology terms:
- UBERON:0002048 (lung)
- UBERON:0000955 (brain) for CNS metastasis context

---

## 8. Temporal Development

KRAS G12C‑mutant NSCLC is typically an **adult-onset malignancy** and frequently diagnosed in advanced stage, but stage-at-diagnosis distributions specific to this genotype were not extracted in the retrieved evidence.

In the therapeutic setting, **acquired resistance typically emerges within months** on KRAS G12C inhibitors, motivating combination strategies; the retrieved evidence emphasizes transience of response and rapid resistance emergence. (shaverdashvili2025advancesinthe pages 2-3)

---

## 9. Inheritance and Population

### Inheritance pattern
This is overwhelmingly a **somatic** (tumor-acquired) driver alteration in NSCLC; no germline inheritance pattern is implied by the retrieved evidence.

### Epidemiology: frequency of KRAS and KRAS G12C in NSCLC
- KRAS mutations occur in roughly **~29–32%** of lung adenocarcinomas in a 2024 resistance review. (sreter2024resistancetokras pages 1-2)
- Across KRAS point mutations in lung adenocarcinoma, **G12C is the most common (~39%)** in that review. (sreter2024resistancetokras pages 1-2)
- Another 2024 overview reports KRAS mutations in **~20–40%** of lung adenocarcinomas and that G12C comprises **~39–42%** of KRAS variants in lung adenocarcinoma; it also reports higher KRAS mutation frequency in smokers and in Western populations. (tenekeci2024anupdatedoverview pages 2-3)

### Real‑world demographic notes (example cohort)
- In a Finnish real‑world registry cohort of advanced/unresectable or metastatic NSCLC undergoing NGS testing, all KRAS‑mutant patients were previous/current smokers; KRAS G12C was identified in **n=35** (within KRAS‑mutant subgroup) and KRAS G12C was associated with poorer survival in that cohort (pre‑KRAS‑G12C inhibitor era context and access limitations may apply). (sultan2024realworldevaluationof pages 1-2)

---

## 10. Diagnostics

### Molecular testing approaches and implementation
The evidence supports the clinical need for timely identification of KRAS G12C and co‑alterations.

- **Broad NGS testing and reflex workflows:** A real‑world study of squamous NSCLC showed that broad DNA/RNA NGS can identify actionable alterations including **KRAS G12C** and argues for reflex testing across NSCLC histologies rather than restricting by smoking status/age. (mina2025emergingtargetedtherapies pages 2-4)
- **Turnaround time and rapid assays:** A 2023 review notes NGS turnaround can be **12–15 days** and describes the **Idylla** rapid oncology assay (<3 hours) to detect KRAS hotspot mutations from FFPE without DNA extraction, citing high concordance with NGS in studies it summarizes. (o’leary2023targetedtherapiesfor pages 4-5)
- **Tissue and plasma use in trials:** CodeBreaK 200 exploratory analyses used **tissue and/or plasma targeted NGS** for genomic alteration analyses. (alharbi2024codebreak200study pages 2-4)

### Biomarkers beyond KRAS G12C
- Co‑mutation profiling (e.g., **STK11**, **KEAP1**, NRF2 pathway readouts) can stratify expected outcomes to KRAS G12C inhibitors, particularly for adagrasib in KRYSTAL‑1 analyses. (negrao2025impactofcomutations pages 1-2)

### Liquid biopsy for resistance monitoring (expert interpretation supported by retrieved review statement)
A recent review explicitly highlights that **“Tissue and liquid biopsies and genotyping of resistant clinical samples can elucidate resistance mechanisms and guide therapeutic decisions.”** (shaverdashvili2025advancesinthe pages 2-3)

---

## 11. Outcome / Prognosis

### Outcomes under KRAS G12C targeted therapy (key statistics)
Pivotal and long‑term trial outcomes for sotorasib in previously treated advanced KRAS G12C NSCLC:
- **CodeBreaK 200 (phase 3):** sotorasib improved PFS vs docetaxel (median **5.6 vs 4.5 months**, HR **0.66**, p=0.0017), improved ORR (**28.1% vs 13.2%**), but did **not** improve OS (median **10.6 vs 11.3 months**, HR **1.01**). (langen2023sotorasibversusdocetaxel pages 8-10)
- **CodeBreaK 100 (2‑year update):** ORR **41%**, median DOR **12.3 months**, median PFS **6.3 months**, median OS **12.5 months**, and 2‑year OS rate **33%**; long‑term clinical benefit (PFS ≥12 months) in **23%**. (dy2023longtermoutcomesand pages 2-3)

### Prognostic modifiers
Co‑mutations (e.g., **KEAP1**, **STK11**, NRF2 signaling state) define distinct outcome strata under KRAS G12C inhibitor therapy in adagrasib‑treated patients. (negrao2025impactofcomutations pages 1-2)

### Real‑world outcomes / utilization proxies
In a US claims‑based cohort receiving sotorasib (2L+), adherence was high (PDC **94.9%**) and median treatment duration **4.3 months**; median time to next treatment among those with subsequent therapy was **6.8 months**, comparable in magnitude to PFS observed in trials (acknowledging TTNT is not a direct PFS measure). (sultan2024realworldevaluationof pages 1-2)

---

## 12. Treatment

### 12.1 Approved targeted therapies (current standard in previously treated setting)
- **Sotorasib** (KRAS G12C inhibitor)
  - **CodeBreaK 200 (Lancet 2023):** improved PFS and ORR vs docetaxel, no OS difference. (langen2023sotorasibversusdocetaxel pages 8-10)
  - **Key safety signal:** diarrhea and transaminase elevations are characteristic; grade ≥3 TRAEs **33%** with sotorasib vs **40%** with docetaxel. (langen2023sotorasibversusdocetaxel pages 8-10)
- **Adagrasib** (KRAS G12C inhibitor)
  - A 2025 NSCLC targeted-therapy review summarizes KRYSTAL‑1 phase II outcomes: ORR **43% (48/112)**, median PFS **6.5 months**, median OS **12.6 months**, intracranial ORR **42%** in a CNS subset. (mina2025emergingtargetedtherapies pages 2-4)

**Key practical safety consideration:** hepatotoxicity risk can be higher when sotorasib is started soon after prior immunotherapy; pooled and comparative summaries highlight this clinically relevant sequencing issue. (higgins2025sotorasibforthe pages 3-4, speranza2025sexrelatedsafetysignals pages 9-11)

### 12.2 Treatment sequencing and guideline‑adjacent expert framing
The retrieved evidence emphasizes that KRAS G12C inhibitors are widely positioned **after progression** on standard first‑line regimens (often immunotherapy‑based), with ongoing trials moving them into earlier lines and combinations. (tenekeci2024anupdatedoverview pages 2-3, o’leary2023targetedtherapiesfor pages 10-11)

### 12.3 Combination strategies (research frontier; mechanistic rationale)
- **KRAS G12C inhibitor + SOS1 inhibitor:** stronger RAS–MAPK suppression and delayed resistance in preclinical KRAS G12C lung cancer models. (sreter2024resistancetokras pages 1-2)
- Co‑mutation–informed combinations: adagrasib plus **mTOR inhibition** showed enhanced efficacy in STK11/KEAP1 co‑mutant preclinical models and is proposed as a rational approach for poor‑prognosis genomics. (negrao2025impactofcomutations pages 1-2)

### 12.4 Selected ongoing clinical trials (real‑world implementation pipeline)
From retrieved ClinicalTrials.gov records:
- **NCT06497556 (Phase 3):** divarasib vs sotorasib or adagrasib in previously treated KRAS G12C‑positive advanced/metastatic NSCLC. (NCT06936644 chunk 1)
- **NCT05074810 (Phase 1/2):** avutometinib (VS‑6766) + sotorasib with/without defactinib; includes KRAS G12C inhibitor‑naïve and previously exposed cohorts. (NCT05074810 chunk 1)
- **NCT06936644 (Phase 2, 1L):** fulzerasib (IBI351) + ivonescimab (AK‑112) for first‑line advanced/metastatic KRAS G12C NSCLC. (NCT06936644 chunk 1)
- **NCT07198841 (Phase 2, 1L):** IBI351 + cetuximab β in untreated advanced/metastatic KRAS G12C NSCLC. (NCT07198841 chunk 1)
- **NCT05504278 (Phase Ib/III, 1L):** IBI351 monotherapy and combinations (with sintilimab; with pemetrexed/platinum; with cetuximab) in advanced/metastatic KRAS G12C nonsquamous NSCLC. (NCT05504278 chunk 1)
- **NCT05840510 (KRYSTAL‑19, Phase 1/2):** adagrasib + nab‑sirolimus (terminated; enrolled 6). (NCT05840510 chunk 1)

### Suggested MAXO terms (treatment actions; suggestions)
- Targeted molecular therapy (NCIT:C15986; broad suggestion)
- Antineoplastic agent therapy (MAXO:0000011)
- Drug combination therapy (MAXO:0000747)

---

## 13. Prevention

No KRAS G12C‑specific primary prevention interventions were identified in the retrieved evidence. Prevention aligns with lung cancer prevention more generally (e.g., smoking reduction) and with **secondary prevention via screening** in eligible high‑risk populations, but guideline details were not retrieved here.

---

## 14. Other Species / Natural Disease
Not addressed in the retrieved evidence.

---

## 15. Model Organisms / Model Systems
The retrieved evidence base in this run contains limited KRAS G12C‑specific model system detail (beyond resistance/combination preclinical studies). However:
- A high‑impact preclinical study used KRAS G12C mutant lung cancer models to demonstrate benefit of **SOS1 inhibitor + adagrasib** and implicated **MRAS**/**SHOC2** biology in resistance and combination response. (sreter2024resistancetokras pages 1-2)

General model types referenced across evidence include cell lines and xenograft models used in clinico‑genomic correlates and resistance studies. (negrao2025impactofcomutations pages 1-2, sreter2024resistancetokras pages 1-2)

---

## Key statistics (2023–2024 anchored) and evidence table
The following table compiles the major quantitative benchmarks used in contemporary practice and research:

| Study (year, journal) | Population/line | Treatment | Key efficacy | Key safety notes | URL / PMID if mentioned |
|---|---|---|---|---|---|
| CodeBreaK 200 (2023, *The Lancet*) | Previously treated KRAS G12C-mutant advanced NSCLC; randomized phase 3; n=171 sotorasib, n=174 docetaxel | Sotorasib 960 mg daily vs docetaxel 75 mg/m² | ORR 28.1% vs 13.2%; median PFS 5.6 vs 4.5 mo; PFS HR 0.66 (95% CI 0.51–0.86; p=0.0017); 12-mo PFS 24.8% vs 10.1%; median OS 10.6 vs 11.3 mo; OS HR 1.01 (95% CI 0.77–1.33); DOR 8.6 vs 6.8 mo; time to response 1.4 vs 2.8 mo (langen2023sotorasibversusdocetaxel pages 8-10, higgins2025sotorasibforthe pages 3-4, langen2023sotorasibversusdocetaxel media 446eaaec) | Grade ≥3 TRAEs 33% vs 40%; serious TRAEs 11% vs 23%; common grade ≥3 with sotorasib: diarrhea 12%, ALT increase 8%, AST increase 5%; fatal TRAEs: 1 (<1%) vs 2 (1%); hepatotoxicity risk higher when started soon after prior immunotherapy (langen2023sotorasibversusdocetaxel pages 8-10, higgins2025sotorasibforthe pages 3-4, speranza2025sexrelatedsafetysignals pages 9-11) | https://doi.org/10.1016/S0140-6736(23)00221-0 |
| CodeBreaK 100 long-term update (2023, *Journal of Clinical Oncology*) | Pretreated KRAS G12C-mutant advanced NSCLC; phase I/II; n=174 | Sotorasib 960 mg daily | ORR 41% (95% CI 33.3–48.4); DCR 84%; median DOR 12.3 mo; median PFS 6.3 mo; median OS 12.5 mo; 2-year OS 33%; long-term clinical benefit (PFS ≥12 mo) in 23% (dy2023longtermoutcomesand pages 1-2, dy2023longtermoutcomesand pages 2-3) | Any-grade TRAEs 70%; grade 3 20%, grade 4 1%, no grade 5 new-onset TRAEs in long-term follow-up; common AEs: diarrhea 30%, ALT increase 18%, AST increase 18%; among >1-year treated patients, few late-onset toxicities (dy2023longtermoutcomesand pages 1-2, dy2023longtermoutcomesand pages 2-3) | https://doi.org/10.1200/JCO.22.02524 |
| KRYSTAL-1 phase II (2025 review summarizing trial data) | Advanced KRAS G12C-mutant NSCLC; previously treated | Adagrasib | ORR 43% (48/112); median DOR 8.5 mo (95% CI 6.2–13.8); median PFS 6.5 mo; median OS 12.6 mo; intracranial ORR 42% (95% CI 20.3–66.5) (mina2025emergingtargetedtherapies pages 2-4) | Signature AEs included nausea, diarrhea, fatigue, musculoskeletal pain, hepatotoxicity, renal impairment; separate review notes high-grade toxicity burden but exact phase II grade ≥3 rate not provided in the evidence snippet used here (mina2025emergingtargetedtherapies pages 2-4) | https://doi.org/10.3390/cancers17030353 |
| Real-world sotorasib claims study (2024, *Advances in Therapy*) | US claims-based cohort; KRAS G12C-mutant NSCLC receiving sotorasib; 2L+ subset n=140 | Sotorasib in routine practice | Mean adherence (PDC) 94.9%; median treatment duration 4.3 mo; among those with subsequent treatment (n=31), median time to next treatment 6.8 mo; mean monthly costs US$23,063 during treatment vs US$25,541 pre-index (sultan2024realworldevaluationof pages 1-2) | Resource utilization during treatment: mean 3.87 outpatient, 0.09 inpatient, 0.11 emergency visits/month; this study did not report trial-style grade ≥3 TRAEs (sultan2024realworldevaluationof pages 1-2) | https://doi.org/10.1007/s12325-024-03020-7 |


*Table: This table compacts the main quantitative clinical evidence for KRAS G12C-mutant NSCLC across pivotal sotorasib and adagrasib studies plus an early real-world sotorasib analysis. It highlights efficacy benchmarks, comparative outcomes, and the most clinically relevant safety signals for rapid reference.*

---

## Expert analysis (synthesis grounded in retrieved authoritative sources)
1. **Clinical benefit is real but modest in randomized evidence:** CodeBreaK 200 demonstrates statistically significant PFS and ORR improvements versus docetaxel but no OS benefit, likely influenced by subsequent KRAS G12C inhibitor exposure and crossover. (langen2023sotorasibversusdocetaxel pages 8-10, langen2023sotorasibversusdocetaxel pages 37-39)
2. **Durable benefit occurs in a subset:** Long‑term CodeBreaK 100 follow‑up shows a clinically meaningful tail with a 2‑year OS rate of 33% and 23% achieving PFS ≥12 months, supporting continued use while optimizing patient selection. (dy2023longtermoutcomesand pages 2-3)
3. **Co‑mutations are central to precision medicine for this subtype:** KEAP1/STK11/NRF2 status stratifies outcomes with adagrasib and provides a rational basis for intensified or alternative strategies. (negrao2025impactofcomutations pages 1-2)
4. **Implementation requires robust molecular testing infrastructure:** Real‑world testing gaps (e.g., community NGS rates and regional reimbursement variability) and the potential role of rapid assays highlight that access to genotyping is a rate‑limiting step for equitable delivery of KRAS G12C targeted therapy. (alharbi2024codebreak200study pages 2-4, o’leary2023targetedtherapiesfor pages 4-5)

---

## Visual evidence from pivotal trial publication
Cropped figures/tables from the CodeBreaK 200 Lancet trial show the key efficacy summaries (PFS HR/medians; OS; ORR) and are consistent with the numeric endpoints cited above. (langen2023sotorasibversusdocetaxel media 446eaaec, langen2023sotorasibversusdocetaxel media 3169850c, langen2023sotorasibversusdocetaxel media 9b269017, langen2023sotorasibversusdocetaxel media f94b5c79)

References

1. (OpenTargets Search: non-small cell lung carcinoma-KRAS): Open Targets Query (non-small cell lung carcinoma-KRAS, 7 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (mina2025emergingtargetedtherapies pages 2-4): Syeda A. Mina, Mohamed Shanshal, Konstantinos Leventakos, and Kaushal Parikh. Emerging targeted therapies in non-small-cell lung cancer (nsclc). Cancers, 17:353, Jan 2025. URL: https://doi.org/10.3390/cancers17030353, doi:10.3390/cancers17030353. This article has 28 citations.

3. (sreter2024resistancetokras pages 1-2): Katherina Bernadette Sreter, Maria Joana Catarata, Maximilian von Laffert, and Armin Frille. Resistance to kras inhibition in advanced non-small cell lung cancer. Frontiers in Oncology, May 2024. URL: https://doi.org/10.3389/fonc.2024.1357898, doi:10.3389/fonc.2024.1357898. This article has 8 citations.

4. (dy2023longtermoutcomesand pages 2-3): Grace K. Dy, Ramaswamy Govindan, Vamsidhar Velcheti, Gerald S. Falchook, Antoine Italiano, Jürgen Wolf, Adrian G. Sacher, Toshiaki Takahashi, Suresh S. Ramalingam, Christophe Dooms, Dong-Wan Kim, Alfredo Addeo, Jayesh Desai, Martin Schuler, Pascale Tomasini, David S. Hong, Piro Lito, Qui Tran, Simon Jones, Abraham Anderson, Antreas Hindoyan, Wendy Snyder, Ferdinandos Skoulidis, and Bob T. Li. Long-term outcomes and molecular correlates of sotorasib efficacy in patients with pretreated <i>kras</i> g12c-mutated non–small-cell lung cancer: 2-year analysis of codebreak 100. Journal of Clinical Oncology, 41:3311-3317, Jun 2023. URL: https://doi.org/10.1200/jco.22.02524, doi:10.1200/jco.22.02524. This article has 175 citations and is from a highest quality peer-reviewed journal.

5. (langen2023sotorasibversusdocetaxel pages 8-10): Adrianus Johannes de Langen, Melissa L Johnson, Julien Mazieres, Anne-Marie C Dingemans, Giannis Mountzios, Miklos Pless, Jürgen Wolf, Martin Schuler, Hervé Lena, Ferdinandos Skoulidis, Yasuto Yoneshima, Sang-We Kim, Helena Linardou, Silvia Novello, Anthonie J van der Wekken, Yuanbin Chen, Solange Peters, Enriqueta Felip, Benjamin J Solomon, Suresh S. Ramalingam, Christophe Dooms, Colin R Lindsay, Carlos Gil Ferreira, Normand Blais, Cynthia C Obiozor, Yang Wang, Bhakti Mehta, Tracy Varrieur, Gataree Ngarmchamnanrith, Björn Stollenwerk, David Waterhouse, and Luis Paz-Ares. Sotorasib versus docetaxel for previously treated non-small-cell lung cancer with krasg12c mutation: a randomised, open-label, phase 3 trial. The Lancet, 401:733-746, Mar 2023. URL: https://doi.org/10.1016/s0140-6736(23)00221-0, doi:10.1016/s0140-6736(23)00221-0. This article has 650 citations and is from a highest quality peer-reviewed journal.

6. (sultan2024realworldevaluationof pages 1-2): Ihtisham Sultan, David M. Waterhouse, Divyan Chopra, Alexander Lonshteyn, Derek Weycker, Thomas E. Delea, and Björn Stollenwerk. Real-world evaluation of treatment patterns, healthcare costs, and healthcare resource utilization among patients with non-small cell lung cancer in the us receiving sotorasib. Advances in Therapy, 41:4648-4659, Oct 2024. URL: https://doi.org/10.1007/s12325-024-03020-7, doi:10.1007/s12325-024-03020-7. This article has 4 citations and is from a peer-reviewed journal.

7. (gecgel2025krasg12cmutation pages 9-11): Aslı Geçgel, Buket Şahin Çelik, Pınar Peker, Zeynep Sıla Gökdere, Didem Koca, Burçak Karaca, Deniz Nart, and Erdem Göker. Kras g12c mutation predicts improved survival in nsclc patients receiving immunotherapy: insights from a real-world cohort. Journal of Clinical Medicine, 14:6826, Sep 2025. URL: https://doi.org/10.3390/jcm14196826, doi:10.3390/jcm14196826. This article has 2 citations.

8. (shaverdashvili2025advancesinthe pages 2-3): Khvaramze Shaverdashvili and Timothy F. Burns. Advances in the treatment of kras g12c mutant non–small cell lung cancer. Cancer, Mar 2025. URL: https://doi.org/10.1002/cncr.35783, doi:10.1002/cncr.35783. This article has 21 citations and is from a domain leading peer-reviewed journal.

9. (tenekeci2024anupdatedoverview pages 2-3): Ates Kutay Tenekeci, Ahmet Arda Unal, Furkan Ceylan, and Mehmet Ali Nahit Sendur. An updated overview of k-ras g12c inhibitors in advanced stage non-small cell lung cancer. Future oncology, 20:1-20, Oct 2024. URL: https://doi.org/10.1080/14796694.2024.2407280, doi:10.1080/14796694.2024.2407280. This article has 13 citations and is from a peer-reviewed journal.

10. (negrao2025impactofcomutations pages 1-2): Marcelo V. Negrao, Alvaro G. Paula, David Molkentine, Laura Hover, Monique Nilsson, Natalie Vokes, Lars Engstrom, Andrew Calinisan, David M. Briere, Laura Waters, Jill Hallin, Lixia Diao, Mehmet Altan, George R. Blumenschein, Ferdinandos Skoulidis, Jing Wang, Scott E. Kopetz, David S. Hong, Don L. Gibbons, Peter Olson, James G. Christensen, and John V. Heymach. Impact of co-mutations and transcriptional signatures in non–small cell lung cancer patients treated with adagrasib in the krystal-1 trial. Clinical Cancer Research, pages OF1-OF13, Feb 2025. URL: https://doi.org/10.1158/1078-0432.ccr-24-2310, doi:10.1158/1078-0432.ccr-24-2310. This article has 28 citations and is from a highest quality peer-reviewed journal.

11. (o’leary2023targetedtherapiesfor pages 4-5): Cian O’Leary, Grace Murphy, Yong Yeung, Ming Tang, Vikram Jain, and Connor G O’Leary. Targeted therapies for kirsten rat sarcoma (kras) g12c mutant metastatic non-small-cell lung cancers. Cancers, 15:5582, Nov 2023. URL: https://doi.org/10.3390/cancers15235582, doi:10.3390/cancers15235582. This article has 3 citations.

12. (alharbi2024codebreak200study pages 2-4): Malak Alharbi, Muhammad Awidi, and Grace K. Dy. Codebreak 200: study limitations, and future directions. Translational Cancer Research, 13:15-21, Jan 2024. URL: https://doi.org/10.21037/tcr-23-1477, doi:10.21037/tcr-23-1477. This article has 8 citations.

13. (higgins2025sotorasibforthe pages 3-4): Jordyn P. Higgins, Jennifer W. Carlisle, Nader H. Moniri, Shruti Gupta, Eziafa I. Oduah, and Ticiana Leal. Sotorasib for the treatment of locally advanced/metastatic non-small cell lung cancer. Future oncology, 21:1-9, Nov 2025. URL: https://doi.org/10.1080/14796694.2024.2430172, doi:10.1080/14796694.2024.2430172. This article has 1 citations and is from a peer-reviewed journal.

14. (speranza2025sexrelatedsafetysignals pages 9-11): Desirèe Speranza, Mariapia Marafioti, Martina Musarra, Vincenzo Cianci, Fausto Omero, Calogera Claudia Spagnolo, Marco Calabrò, Nicola Silvestris, Natasha Irrera, and Mariacarmela Santarpia. Sex-related safety signals of sotorasib in non-small cell lung cancer: a real-world, pharmacovigilance study from the eudravigilance database. Pharmaceuticals, 18:1574, Oct 2025. URL: https://doi.org/10.3390/ph18101574, doi:10.3390/ph18101574. This article has 0 citations.

15. (o’leary2023targetedtherapiesfor pages 10-11): Cian O’Leary, Grace Murphy, Yong Yeung, Ming Tang, Vikram Jain, and Connor G O’Leary. Targeted therapies for kirsten rat sarcoma (kras) g12c mutant metastatic non-small-cell lung cancers. Cancers, 15:5582, Nov 2023. URL: https://doi.org/10.3390/cancers15235582, doi:10.3390/cancers15235582. This article has 3 citations.

16. (NCT06936644 chunk 1): Zhong Runbo. A Multicenter, Single-arm Phase II Study to Evaluate the Efficacy and Safety of Fulzerasib (IBI351) in Combination With Ivonescimab (AK-112) in First-line Treatment of Advanced or Metastatic Non-small Cell Lung Cancer Patients With KRAS G12C Mutation. Shanghai Chest Hospital. 2025. ClinicalTrials.gov Identifier: NCT06936644

17. (NCT05074810 chunk 1):  Phase 1/2 Study of Avutometinib (VS-6766) + Sotorasib With or Without Defactinib in KRAS G12C NSCLC Patients. Verastem, Inc.. 2022. ClinicalTrials.gov Identifier: NCT05074810

18. (NCT07198841 chunk 1):  IBI351 Plus Cetuximab β in Untreated Advanced Non-small Cell Lung Cancer With KRAS G12C Mutation. Guangdong Association of Clinical Trials. 2025. ClinicalTrials.gov Identifier: NCT07198841

19. (NCT05504278 chunk 1):  Efficacy and Safety of IBI351 in Combination With Chemotherapy in Advanced Non-squamous Non-small Cell Lung Cancer Subjects With KRAS G12C Mutation. Innovent Biologics (Suzhou) Co. Ltd.. 2022. ClinicalTrials.gov Identifier: NCT05504278

20. (NCT05840510 chunk 1):  Adagrasib in Combination With Nab-Sirolimus in Patients With Advanced Solid Tumors and Non-Small Cell Lung Cancer With a KRAS G12C Mutation (KRYSTAL -19). Mirati Therapeutics Inc.. 2023. ClinicalTrials.gov Identifier: NCT05840510

21. (langen2023sotorasibversusdocetaxel media 446eaaec): Adrianus Johannes de Langen, Melissa L Johnson, Julien Mazieres, Anne-Marie C Dingemans, Giannis Mountzios, Miklos Pless, Jürgen Wolf, Martin Schuler, Hervé Lena, Ferdinandos Skoulidis, Yasuto Yoneshima, Sang-We Kim, Helena Linardou, Silvia Novello, Anthonie J van der Wekken, Yuanbin Chen, Solange Peters, Enriqueta Felip, Benjamin J Solomon, Suresh S. Ramalingam, Christophe Dooms, Colin R Lindsay, Carlos Gil Ferreira, Normand Blais, Cynthia C Obiozor, Yang Wang, Bhakti Mehta, Tracy Varrieur, Gataree Ngarmchamnanrith, Björn Stollenwerk, David Waterhouse, and Luis Paz-Ares. Sotorasib versus docetaxel for previously treated non-small-cell lung cancer with krasg12c mutation: a randomised, open-label, phase 3 trial. The Lancet, 401:733-746, Mar 2023. URL: https://doi.org/10.1016/s0140-6736(23)00221-0, doi:10.1016/s0140-6736(23)00221-0. This article has 650 citations and is from a highest quality peer-reviewed journal.

22. (dy2023longtermoutcomesand pages 1-2): Grace K. Dy, Ramaswamy Govindan, Vamsidhar Velcheti, Gerald S. Falchook, Antoine Italiano, Jürgen Wolf, Adrian G. Sacher, Toshiaki Takahashi, Suresh S. Ramalingam, Christophe Dooms, Dong-Wan Kim, Alfredo Addeo, Jayesh Desai, Martin Schuler, Pascale Tomasini, David S. Hong, Piro Lito, Qui Tran, Simon Jones, Abraham Anderson, Antreas Hindoyan, Wendy Snyder, Ferdinandos Skoulidis, and Bob T. Li. Long-term outcomes and molecular correlates of sotorasib efficacy in patients with pretreated <i>kras</i> g12c-mutated non–small-cell lung cancer: 2-year analysis of codebreak 100. Journal of Clinical Oncology, 41:3311-3317, Jun 2023. URL: https://doi.org/10.1200/jco.22.02524, doi:10.1200/jco.22.02524. This article has 175 citations and is from a highest quality peer-reviewed journal.

23. (langen2023sotorasibversusdocetaxel pages 37-39): Adrianus Johannes de Langen, Melissa L Johnson, Julien Mazieres, Anne-Marie C Dingemans, Giannis Mountzios, Miklos Pless, Jürgen Wolf, Martin Schuler, Hervé Lena, Ferdinandos Skoulidis, Yasuto Yoneshima, Sang-We Kim, Helena Linardou, Silvia Novello, Anthonie J van der Wekken, Yuanbin Chen, Solange Peters, Enriqueta Felip, Benjamin J Solomon, Suresh S. Ramalingam, Christophe Dooms, Colin R Lindsay, Carlos Gil Ferreira, Normand Blais, Cynthia C Obiozor, Yang Wang, Bhakti Mehta, Tracy Varrieur, Gataree Ngarmchamnanrith, Björn Stollenwerk, David Waterhouse, and Luis Paz-Ares. Sotorasib versus docetaxel for previously treated non-small-cell lung cancer with krasg12c mutation: a randomised, open-label, phase 3 trial. The Lancet, 401:733-746, Mar 2023. URL: https://doi.org/10.1016/s0140-6736(23)00221-0, doi:10.1016/s0140-6736(23)00221-0. This article has 650 citations and is from a highest quality peer-reviewed journal.

24. (langen2023sotorasibversusdocetaxel media 3169850c): Adrianus Johannes de Langen, Melissa L Johnson, Julien Mazieres, Anne-Marie C Dingemans, Giannis Mountzios, Miklos Pless, Jürgen Wolf, Martin Schuler, Hervé Lena, Ferdinandos Skoulidis, Yasuto Yoneshima, Sang-We Kim, Helena Linardou, Silvia Novello, Anthonie J van der Wekken, Yuanbin Chen, Solange Peters, Enriqueta Felip, Benjamin J Solomon, Suresh S. Ramalingam, Christophe Dooms, Colin R Lindsay, Carlos Gil Ferreira, Normand Blais, Cynthia C Obiozor, Yang Wang, Bhakti Mehta, Tracy Varrieur, Gataree Ngarmchamnanrith, Björn Stollenwerk, David Waterhouse, and Luis Paz-Ares. Sotorasib versus docetaxel for previously treated non-small-cell lung cancer with krasg12c mutation: a randomised, open-label, phase 3 trial. The Lancet, 401:733-746, Mar 2023. URL: https://doi.org/10.1016/s0140-6736(23)00221-0, doi:10.1016/s0140-6736(23)00221-0. This article has 650 citations and is from a highest quality peer-reviewed journal.

25. (langen2023sotorasibversusdocetaxel media 9b269017): Adrianus Johannes de Langen, Melissa L Johnson, Julien Mazieres, Anne-Marie C Dingemans, Giannis Mountzios, Miklos Pless, Jürgen Wolf, Martin Schuler, Hervé Lena, Ferdinandos Skoulidis, Yasuto Yoneshima, Sang-We Kim, Helena Linardou, Silvia Novello, Anthonie J van der Wekken, Yuanbin Chen, Solange Peters, Enriqueta Felip, Benjamin J Solomon, Suresh S. Ramalingam, Christophe Dooms, Colin R Lindsay, Carlos Gil Ferreira, Normand Blais, Cynthia C Obiozor, Yang Wang, Bhakti Mehta, Tracy Varrieur, Gataree Ngarmchamnanrith, Björn Stollenwerk, David Waterhouse, and Luis Paz-Ares. Sotorasib versus docetaxel for previously treated non-small-cell lung cancer with krasg12c mutation: a randomised, open-label, phase 3 trial. The Lancet, 401:733-746, Mar 2023. URL: https://doi.org/10.1016/s0140-6736(23)00221-0, doi:10.1016/s0140-6736(23)00221-0. This article has 650 citations and is from a highest quality peer-reviewed journal.

26. (langen2023sotorasibversusdocetaxel media f94b5c79): Adrianus Johannes de Langen, Melissa L Johnson, Julien Mazieres, Anne-Marie C Dingemans, Giannis Mountzios, Miklos Pless, Jürgen Wolf, Martin Schuler, Hervé Lena, Ferdinandos Skoulidis, Yasuto Yoneshima, Sang-We Kim, Helena Linardou, Silvia Novello, Anthonie J van der Wekken, Yuanbin Chen, Solange Peters, Enriqueta Felip, Benjamin J Solomon, Suresh S. Ramalingam, Christophe Dooms, Colin R Lindsay, Carlos Gil Ferreira, Normand Blais, Cynthia C Obiozor, Yang Wang, Bhakti Mehta, Tracy Varrieur, Gataree Ngarmchamnanrith, Björn Stollenwerk, David Waterhouse, and Luis Paz-Ares. Sotorasib versus docetaxel for previously treated non-small-cell lung cancer with krasg12c mutation: a randomised, open-label, phase 3 trial. The Lancet, 401:733-746, Mar 2023. URL: https://doi.org/10.1016/s0140-6736(23)00221-0, doi:10.1016/s0140-6736(23)00221-0. This article has 650 citations and is from a highest quality peer-reviewed journal.
