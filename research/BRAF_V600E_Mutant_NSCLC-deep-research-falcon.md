---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T12:59:06.202757'
end_time: '2026-04-05T13:08:22.028353'
duration_seconds: 555.83
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: BRAF V600E-Mutant Non-Small Cell Lung Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** BRAF V600E-Mutant Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **BRAF V600E-Mutant Non-Small Cell Lung Cancer** covering all of the
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
- **Disease Name:** BRAF V600E-Mutant Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **BRAF V600E-Mutant Non-Small Cell Lung Cancer** covering all of the
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


## Comprehensive Research Report: BRAF V600E–Mutant Non-Small Cell Lung Cancer (NSCLC)

### Target disease
- **Disease name:** BRAF V600E–mutant non-small cell lung cancer (typically metastatic lung adenocarcinoma molecular subset)
- **Category:** Molecularly defined subtype of NSCLC (oncogene-driven NSCLC)
- **MONDO ID:** Not identified in the retrieved evidence; recommend mapping via MONDO search term “non-small cell lung carcinoma” + qualifier “BRAF V600E” (no MONDO/MeSH/ICD codes were explicitly provided in the sources retrieved here). (planchard2024brafv600emutantmetastaticnsclc pages 3-4, planchard2024brafv600emutantmetastaticnsclc pages 1-2)

---

## 1. Disease information

### Overview / current definition
BRAF V600E–mutant NSCLC is a molecular subset of NSCLC characterized by an activating missense substitution at codon 600 in **BRAF**, most commonly **p.Val600Glu (V600E)**, leading to constitutive MAPK pathway signaling and oncogenic dependence on the RAF–MEK–ERK cascade. (planchard2024brafv600emutantmetastaticnsclc pages 1-2)

A 2024 review describes the key mechanistic definition directly: the **“BRAFV600E mutation confers constitutive activity of the MAPK pathway”** and thereby promotes tumor cell growth and survival. (planchard2024brafv600emutantmetastaticnsclc pages 1-2)

### Key identifiers (as available from retrieved sources)
- **ICD-10 / ICD-11:** Not explicitly provided in retrieved sources; coding generally follows NSCLC/lung adenocarcinoma primary site and stage plus biomarker annotation. (planchard2024brafv600emutantmetastaticnsclc pages 3-4)
- **MeSH:** Not explicitly provided in retrieved sources. (planchard2024brafv600emutantmetastaticnsclc pages 3-4)
- **MONDO:** Not explicitly provided in retrieved sources. (planchard2024brafv600emutantmetastaticnsclc pages 3-4)

### Common synonyms / alternative names
- “BRAFV600E-mutant metastatic NSCLC” (common in trials and reviews) (planchard2024brafv600emutantmetastaticnsclc pages 1-2)
- “BRAF V600E–positive NSCLC” (used in regulatory documents and trials) (odogwu2018fdaapprovalsummary pages 1-2, planchard2016dabrafenibplustrametinib pages 1-1)
- “BRAF-mutated NSCLC (class I / V600)” when grouped in BRAF mutation class framework (planchard2024brafv600emutantmetastaticnsclc pages 3-4, baik2024apracticalreview pages 1-3)

### Evidence source type
The evidence is primarily aggregated disease-level resources (phase II trials, regulatory approval summaries, and review syntheses), rather than EHR-derived single-patient sources—though case reports and real-world retrospective studies exist. (odogwu2018fdaapprovalsummary pages 1-2, planchard2016dabrafenibplustrametinib pages 1-1, yan2024efficacyofchemoimmunotherapy pages 1-2)

---

## 2. Etiology

### Primary causal factors
- **Somatic oncogenic driver:** Activating **BRAF V600E** (class I BRAF) mutation in tumor cells, usually in lung adenocarcinoma. (planchard2016dabrafenibplustrametinib pages 1-1, planchard2024brafv600emutantmetastaticnsclc pages 1-2)
- **Mechanistic cause:** Constitutive activation of MAPK signaling (RAF→MEK→ERK). (planchard2024brafv600emutantmetastaticnsclc pages 1-2)

### Risk factors (patient-level)
Risk factors largely overlap with NSCLC broadly (e.g., tobacco exposure), but **BRAFV600E is reported to be less associated with smoking history than other BRAF alterations** in NSCLC. (planchard2024brafv600emutantmetastaticnsclc pages 1-2)

Demographic associations are inconsistent across studies, but one study summarized in 2024 reported BRAFV600E being more common in females (not uniformly replicated). (planchard2024brafv600emutantmetastaticnsclc pages 1-2)

### Protective factors
No protective genetic or environmental factors specific to BRAF V600E NSCLC were identified in the retrieved evidence.

### Gene–environment interaction
The retrieved evidence supports heterogeneity in smoking association (BRAFV600E less smoking-associated than other BRAF alterations), consistent with gene–environment patterning in lung cancer; no quantitative GxE interaction models were retrieved here. (planchard2024brafv600emutantmetastaticnsclc pages 1-2)

---

## 3. Phenotypes

### Core clinical phenotype and presentation
BRAF V600E–mutant NSCLC most commonly presents as advanced/metastatic **lung adenocarcinoma**. A 2024 review notes BRAF mutations are “predominantly found in adenocarcinomas (>85%).” (planchard2024brafv600emutantmetastaticnsclc pages 1-2)

Clinical manifestations are those of NSCLC by stage (e.g., cough, dyspnea, hemoptysis, chest pain, weight loss) and metastasis-related symptoms (bone pain, neurologic symptoms if brain metastases). Specific symptom-frequency data were not present in the retrieved excerpts.

### Suggested HPO terms (examples for NSCLC phenotype capture)
(General NSCLC phenotype ontology suggestions; frequencies not extracted from the retrieved evidence)
- **Cough** (HP:0012735)
- **Dyspnea** (HP:0002094)
- **Hemoptysis** (HP:0002105)
- **Weight loss** (HP:0001824)
- **Chest pain** (HP:0100749)
- **Pleural effusion** (HP:0002202)
- **Bone pain** (HP:0002653)
- **Headache** (HP:0002315) / **Seizure** (HP:0001250) (for brain metastases)

### Quality of life
A 2024 phase II study in Chinese patients explicitly included quality of life and states **“self-reported QoL was improved or maintained during the treatment period”** on dabrafenib+trametinib. (fan2024efficacysafetyand pages 1-2)

---

## 4. Genetic / molecular information

### Causal gene
- **BRAF** (proto-oncogene; serine/threonine kinase in MAPK pathway). (pan2019dabrafenibplustrametinib pages 1-2)

### Pathogenic variant (somatic)
- **BRAF p.Val600Glu (V600E)** (activating missense). A case-based review describes this as “valine substitution for glutamate at position 600 (V600E) within the BRAF kinase.” (pan2019dabrafenibplustrametinib pages 1-2)
- Somatic origin is typical in NSCLC; germline BRAF V600E is not a recognized common cause of lung cancer in these sources.

### Variant classification
In cancer clinical practice, BRAF V600E is treated as an actionable oncogenic driver (pathogenic/oncogenic in somatic context). (planchard2024brafv600emutantmetastaticnsclc pages 1-2)

### Co-mutations and molecular classes
BRAF mutations are categorized into three functional classes; class I includes V600 substitutions (including V600E). (planchard2024brafv600emutantmetastaticnsclc pages 1-2, planchard2024brafv600emutantmetastaticnsclc pages 3-4)

### Population allele frequency
Population germline allele frequency is not directly relevant for a somatic driver; not extracted in the retrieved evidence.

### Resistance mechanisms (molecular)
Resistance to BRAF/MEK inhibition in BRAFV600E NSCLC is frequently mediated by **MAPK pathway reactivation** and/or bypass signaling. A 2024 resistance-focused study notes resistance mechanisms have been described as **“MAPK-dependent, related to the reactivation of the MAPK pathway”** as well as MAPK-independent alterations, and highlights extensive genomic heterogeneity at failure. (mezquita2024resistancetobraf pages 1-2)

A 2024 review summarizes specific recurrent mechanisms (percentages reported in the review): MAPK/ERK reactivation via **BRAF splice variants (16%)**, **BRAF amplification (13%)**, **NRAS/KRAS alterations (20%)**, **MEK1/2 mutations (7%)**, plus PI3K-AKT activation and PTEN alterations. (ibrahim2024navigatingthecomplexity pages 7-8)

---

## 5. Environmental information

No environmental or infectious agent is specific to the BRAF V600E subtype in the retrieved evidence. Environmental factors follow NSCLC broadly (tobacco smoke, radon, air pollution, occupational carcinogens). The key subtype-relevant point extracted is a relative (not absolute) decreased association of BRAFV600E with smoking compared to other BRAF alterations. (planchard2024brafv600emutantmetastaticnsclc pages 1-2)

---

## 6. Mechanism / pathophysiology

### Core pathway
BRAFV600E is a constitutively active class I BRAF mutation that drives persistent RAF–MEK–ERK signaling and tumor proliferation/survival. (planchard2024brafv600emutantmetastaticnsclc pages 1-2)

**Causal chain (simplified):**
1) Somatic BRAF V600E mutation → 2) constitutive MAPK pathway activation → 3) increased tumor cell proliferation/survival → 4) tumor growth, invasion, metastasis and NSCLC clinical manifestations. (planchard2024brafv600emutantmetastaticnsclc pages 1-2)

### Upstream vs downstream
- **Upstream:** RTKs/RAS inputs may be less necessary for class I BRAF activation (oncogenic monomer activity), but can contribute to feedback and resistance. (planchard2024brafv600emutantmetastaticnsclc pages 3-4, mezquita2024resistancetobraf pages 1-2)
- **Downstream:** MEK/ERK activation; resistance frequently involves ERK reactivation. (mezquita2024resistancetobraf pages 1-2)

### Suggested GO biological process terms
- **MAPK cascade** (GO:0000165)
- **ERK1 and ERK2 cascade** (GO:0070371)
- **Positive regulation of cell proliferation** (GO:0008284)
- **Regulation of apoptotic process** (GO:0042981)
- **Response to drug** (GO:0042493)

### Immune system involvement
Immune checkpoint inhibitors are used in BRAF-mutant NSCLC, but retrospective evidence is mixed; targeted therapy is often prioritized for BRAF V600E (see Treatment). (yan2024efficacyofchemoimmunotherapy pages 1-2)

### Molecular profiling (recent technology example: CTC profiling)
At failure of dabrafenib+trametinib, single-cell circulating tumor cell sequencing demonstrated substantial heterogeneity and that resistance was not necessarily driven by BRAFV600E-mutant CTCs (BRAFV600E found in only 1/26 CTCs), with alterations affecting cell cycle, DNA repair, and immune response pathways. (mezquita2024resistancetobraf pages 1-2)

---

## 7. Anatomical structures affected

### Organ/system level
- Primary: **Lung** (respiratory system), typically adenocarcinoma. (planchard2024brafv600emutantmetastaticnsclc pages 1-2)
- Metastatic involvement: common NSCLC metastatic sites (brain, bone, liver, adrenal, pleura) are clinically relevant; intracranial activity data for BRAF/MEK therapy indicate brain metastases are a key management issue. (planchard2024brafv600emutantmetastaticnsclc pages 10-11)

### Suggested UBERON terms
- **Lung** (UBERON:0002048)
- **Pulmonary alveolus** (UBERON:0002299)
- **Bronchiole** (UBERON:0002189)

### Suggested Cell Ontology (CL) terms
- **Alveolar type II cell** (CL:0002063) (common cell-of-origin used in mouse models and lung adenocarcinoma studies)
- **Epithelial cell** (CL:0000066)

### Suggested GO cellular component terms
- **Plasma membrane** (GO:0005886) (RTK signaling)
- **Cytosol** (GO:0005829)
- **Nucleus** (GO:0005634)

---

## 8. Temporal development

- **Onset:** Adult-onset malignancy; often detected at advanced stage typical of NSCLC.
- **Progression:** Progressive unless treated; targeted therapy yields rapid responses but resistance commonly develops.

The resistance literature and reviews note progression on BRAF-targeted therapy is common, with many patients progressing within ~1 year in historical experience. (ibrahim2024navigatingthecomplexity pages 7-8)

---

## 9. Inheritance and population

### Epidemiology (frequency)
- FDA review notes **BRAF V600 mutations occur in ~2% of NSCLC**, and “about half” are V600E, implying ~1–1.5% of NSCLC are BRAF V600E. (odogwu2018fdaapprovalsummary pages 1-2)
- A 2024 review estimates BRAFV600E “accounts for ~1–2% of NSCLCs.” (planchard2024brafv600emutantmetastaticnsclc pages 1-2)

### Demographics
- Histology: predominantly adenocarcinoma (>85%). (planchard2024brafv600emutantmetastaticnsclc pages 1-2)
- Smoking: BRAFV600E less associated with smoking than other BRAF. (planchard2024brafv600emutantmetastaticnsclc pages 1-2)
- Sex: potential female enrichment in some datasets, but inconsistent across studies. (planchard2024brafv600emutantmetastaticnsclc pages 1-2)

### Inheritance
BRAF V600E in NSCLC is typically **somatic** (tumor-acquired); inheritance patterns and penetrance are not applicable in the usual presentation.

---

## 10. Diagnostics

### Molecular testing (guideline-level principles)
A 2024 review summarizes guideline direction: **“Guidelines recommend that all patients with advanced non-squamous NSCLC undergo broad-based molecular testing to identify molecular drivers—including but not limited to BRAFV600 mutations.”** (planchard2024brafv600emutantmetastaticnsclc pages 3-4)

#### Assay modalities
- **PCR:** rapid turnaround but “typically limited to detection of V600E mutation” (single-gene). (planchard2024brafv600emutantmetastaticnsclc pages 3-4)
- **Panel-based NGS:** supports simultaneous multi-gene testing and detects both V600E and non-V600 BRAF alterations. (planchard2024brafv600emutantmetastaticnsclc pages 3-4)

#### Liquid biopsy / ctDNA
Single-cell CTC profiling and cfDNA can detect BRAF V600E at resistance; cfDNA detected BRAFV600E in 5/7 samples at failure in a small cohort. (mezquita2024resistancetobraf pages 1-2)

### Biomarkers
- **BRAF V600E** is the defining predictive biomarker for BRAF+MEK inhibitor therapy. (planchard2024brafv600emutantmetastaticnsclc pages 1-2)
- PD-L1 may influence chemo-immunotherapy outcomes; a retrospective study found PD-L1 expression differed between responders and non-responders (p=0.04). (yan2024efficacyofchemoimmunotherapy pages 1-2)

---

## 11. Outcome / prognosis

### Outcomes on targeted therapy
Clinical trial and real-world outcomes are best summarized under Treatment; durable responses occur but acquired resistance is common. (planchard2024brafv600emutantmetastaticnsclc pages 3-4, riely2023phaseiiopenlabel pages 1-2)

### Outcomes on chemo-immunotherapy (BRAF-mutated cohort)
A 2024 retrospective study in BRAF-mutated NSCLC treated with ICI+chemotherapy (n=44 treated) reported:
- **ORR 36.3%**
- **Median PFS 4 months**
- **Median OS 29 months**
and improved OS when used first-line versus later-line (29 vs 9.75 months, p=0.01). (yan2024efficacyofchemoimmunotherapy pages 1-2)

---

## 12. Treatment

### Standard targeted therapy (approved BRAF+MEK combinations)
Two BRAF+MEK combinations are guideline-supported preferred options in metastatic BRAFV600E NSCLC:
- **dabrafenib + trametinib** (FDA approval expanded June 22, 2017) (odogwu2018fdaapprovalsummary pages 1-2)
- **encorafenib + binimetinib** (FDA approval October 11, 2023) (baik2024apracticalreview pages 1-3)

A 2024 review states: **“Current guidelines recommend dabrafenib plus trametinib or encorafenib plus binimetinib as preferred first-line treatment options or as subsequent treatment for BRAFV600E-mutant metastatic NSCLC.”** (planchard2024brafv600emutantmetastaticnsclc pages 1-2)

#### Dabrafenib + trametinib (phase II efficacy)
From the 2016 phase II in previously treated metastatic BRAFV600E NSCLC:
- ORR **63.2%** (95% CI 49.3–75.6) (planchard2016dabrafenibplustrametinib pages 1-1)

From the 2024 review synthesis of phase II cohorts:
- Treatment-naïve: ORR **64%**; median PFS **10.9 months**; OS **24.6 months** (planchard2024brafv600emutantmetastaticnsclc pages 3-4)
- Previously treated: ORR **63.2%**; median PFS **9.7 months** (planchard2024brafv600emutantmetastaticnsclc pages 3-4)

FDA approval summary confirms similar magnitude: ORR 63% (previously treated) and 61% (treatment-naïve), with majority of responses durable ≥6 months. (odogwu2018fdaapprovalsummary pages 1-2, odogwu2018fdaapprovalsummary pages 3-5)

#### Encorafenib + binimetinib (PHAROS phase II)
The JCO 2023 PHAROS phase II trial reported:
- Treatment-naïve: ORR **75%** (95% CI 62–85); median PFS **NE** (95% CI 15.7–NE) (riely2023phaseiiopenlabel pages 1-2)
- Previously treated: ORR **46%** (95% CI 30–63); median PFS **9.3 months** (95% CI 6.2–NE) (riely2023phaseiiopenlabel pages 1-2)

Abstract-level direct quote supporting core result: **“ORR by IRR was 75% (95% CI, 62 to 85) in treatment-naïve and 46% (95% CI, 30 to 63) in previously treated patients.”** (riely2023phaseiiopenlabel pages 1-2)

#### Adverse events (selected)
- Encorafenib+binimetinib common TRAEs: nausea (50%), diarrhea (43%), fatigue (32%); permanent discontinuation due to TRAEs 15%; one grade 5 intracranial hemorrhage. (riely2023phaseiiopenlabel pages 1-2, riely2023phaseiiopenlabel pages 6-8)
- Dabrafenib+trametinib (previously treated cohort): serious AEs occurred in 56%; common grade 3–4 events included neutropenia (9%) and hyponatremia (7%). (planchard2016dabrafenibplustrametinib pages 1-1)

### Immunotherapy and chemo-immunotherapy
Chemo-immunotherapy is a real-world alternative/adjunct when targeted therapy is unavailable, contraindicated, or in later-line settings, but comparative efficacy is heterogeneous across reports. A 2024 retrospective series reported ORR 36.3% and median PFS 4 months on ICI+chemotherapy in BRAF-mutated NSCLC. (yan2024efficacyofchemoimmunotherapy pages 1-2)

### Experimental / emerging applications
- Triplet regimens combining EGFR inhibition with dabrafenib+trametinib have been used in acquired BRAFV600E-mediated resistance in EGFR-mutant NSCLC (case series evidence), illustrating cross-driver resistance management paradigms. (o’leary2019targetingbrafmutations pages 1-2)

### MAXO (Medical Action Ontology) suggestions
(Recommended for knowledge base annotation)
- **Targeted therapy** (e.g., “BRAF inhibitor therapy”, “MEK inhibitor therapy”; combination targeted therapy)
- **Molecular diagnostic testing** (tumor NGS panel testing; plasma ctDNA testing)
- **Immune checkpoint inhibitor therapy** (PD-1/PD-L1 inhibitor therapy)
- **Cytotoxic chemotherapy** (platinum-doublet chemotherapy)

### Quick comparative evidence table
| Therapy | Study / setting | Key publication | Cohort size | ORR | DOR | Median PFS | Median OS | FDA approval date | Notes / citation |
|---|---|---:|---:|---|---|---|---|---|---|
| Dabrafenib + trametinib | Phase II, previously treated BRAFV600E-mutant metastatic NSCLC | 2016 | n=57 | 63.2% (95% CI 49.3–75.6) | 9.0 mo | 9.7 mo | NR in initial report | 22-Jun-2017 | Planchard et al., *Lancet Oncology* 2016; basis of later regulatory summary (planchard2016dabrafenibplustrametinib pages 1-1, odogwu2018fdaapprovalsummary pages 1-2) |
| Dabrafenib + trametinib | Phase II, treatment-naive BRAFV600E-mutant metastatic NSCLC | 2017 | n=36 | 64% (95% CI 46–79); FDA summary reports 61% (95% CI 44–77) | 10.4 mo | 10.9 mo | 24.6 mo | 22-Jun-2017 | Planchard et al., *Lancet Oncology* 2017; FDA approval summary confirms June 22, 2017 approval (planchard2024brafv600emutantmetastaticnsclc pages 3-4, odogwu2018fdaapprovalsummary pages 1-2) |
| Dabrafenib + trametinib | Updated 5-year phase II follow-up | 2022 | previously treated n=57; treatment-naive n=36 | — | — | ~10.2 mo (pretreated); ~10.8 mo (naive) | ~18.2 mo (pretreated); ~17.3 mo (naive) | 22-Jun-2017 | Long-term survival update in *J Thorac Oncol* 2022 (summarized in review) (planchard2024brafv600emutantmetastaticnsclc pages 3-4) |
| Encorafenib + binimetinib | PHAROS phase II, treatment-naive BRAFV600E-mutant metastatic NSCLC | 2023 | n=59 | 75% (95% CI 62–85) | NE (95% CI 23.1–NE) | NE (95% CI 15.7–NE) | NE | 11-Oct-2023 | Riely et al., *J Clin Oncol* 2023; FDA approval based on PHAROS (riely2023phaseiiopenlabel pages 1-2, baik2024apracticalreview pages 1-3, baik2024apracticalreview media 088d26fe) |
| Encorafenib + binimetinib | PHAROS phase II, previously treated BRAFV600E-mutant metastatic NSCLC | 2023 | n=39 | 46% (95% CI 30–63) | 16.7 mo (95% CI 7.4–NE) | 9.3 mo (95% CI 6.2–NE) | NE | 11-Oct-2023 | Riely et al., *J Clin Oncol* 2023; second approved BRAF/MEK option in this disease (riely2023phaseiiopenlabel pages 1-2, baik2024apracticalreview pages 3-4, baik2024apracticalreview pages 1-3) |


*Table: This table summarizes the pivotal efficacy results and FDA approval milestones for the two approved BRAF/MEK inhibitor combinations used in BRAF V600E-mutant metastatic NSCLC. It is useful for quickly comparing the clinical trial evidence supporting dabrafenib/trametinib and encorafenib/binimetinib.*

---

## 13. Prevention

### Primary prevention
Subtype-specific primary prevention is not established; prevention follows lung cancer prevention broadly (tobacco cessation, reducing exposures).

### Secondary prevention (screening / early detection)
**USPSTF 2021 lung cancer screening (U.S.)** expanded eligibility for **annual low-dose CT (LDCT)** to:
- **Adults aged 50–80 years**
- **≥20 pack-year smoking history**
- **Current smokers or quit within the past 15 years**
These criteria are explicitly summarized in 2021–2022 analyses/commentaries. (melzer2021expandedaccessto pages 1-2, ritzwoller2021evaluationofpopulationlevel pages 2-4)

These screening recommendations are not BRAF-specific; they aim to reduce lung cancer mortality at a population level. (melzer2021expandedaccessto pages 1-2)

---

## 14. Other species / natural disease

No naturally occurring veterinary “BRAF V600E lung cancer” entity was retrieved in the present evidence set.

---

## 15. Model organisms

### Genetically engineered mouse models (GEMMs)
Evidence supports that conditional lung-specific expression of **BRAF V600E** induces lung tumors and establishes MAPK dependency:
- In a classic mouse model study, lung-specific BRAF V600E expression induced **lung adenocarcinoma with bronchioloalveolar features**, with tumor regression upon transgene deinduction and also tumor regression with MEK inhibition (CI-1040), demonstrating MAPK pathway dependence. (ji2007mutationsinbraf pages 1-2)

A more recent GEMM study emphasized the need for cooperating events:
- Expression of BRAFV600E in distal lung epithelium produces **benign lung adenomas** that undergo a senescence-like proliferative arrest and “typically fail to progress,” but **TP53 silencing bypasses growth arrest** and promotes progression to lung adenocarcinoma. (shai2015tp53silencingbypasses pages 1-3)

These models are used to study tumor initiation, oncogene addiction, and resistance biology in an immunocompetent context.

---

# Notes on evidence limitations
- **Ontology identifiers (MONDO, MeSH, ICD-10/11)** for this biomarker-defined entity were not directly provided in the retrieved excerpts; these should be added via dedicated ontology lookup workflows (e.g., MONDO/MeSH browser). (planchard2024brafv600emutantmetastaticnsclc pages 3-4)
- Several requested areas (e.g., detailed phenotype frequency distributions, large population incidence/prevalence rates per 100,000) were not available in the current retrieved sources and would require cancer registry analyses stratified by BRAF status.

# Key recent sources prioritized (2023–2024)
- Planchard et al., *NPJ Precision Oncology* (Apr 2024): https://doi.org/10.1038/s41698-024-00552-7 (planchard2024brafv600emutantmetastaticnsclc pages 1-2, planchard2024brafv600emutantmetastaticnsclc pages 3-4)
- Riely et al., *Journal of Clinical Oncology* (Jul 2023): https://doi.org/10.1200/JCO.23.00774 (riely2023phaseiiopenlabel pages 1-2)
- Baik et al., *Advances in Therapy* (May 2024): https://doi.org/10.1007/s12325-024-02839-4 (baik2024apracticalreview pages 1-3, baik2024apracticalreview pages 3-4)
- Mezquita et al., *British Journal of Cancer* (Jan 2024): https://doi.org/10.1038/s41416-023-02535-0 (mezquita2024resistancetobraf pages 1-2)
- Yan et al., *Frontiers in Oncology* (Jan 2024): https://doi.org/10.3389/fonc.2024.1353491 (yan2024efficacyofchemoimmunotherapy pages 1-2)
- Melzer & Wilt, *JAMA Network Open* (Mar 2021): https://doi.org/10.1001/jamanetworkopen.2021.0275 (USPSTF 2021 criteria summary) (melzer2021expandedaccessto pages 1-2)

**Included visual evidence:** PHAROS efficacy table excerpted from Baik et al. (Table 1). (baik2024apracticalreview media 088d26fe)

References

1. (planchard2024brafv600emutantmetastaticnsclc pages 3-4): David Planchard, Rachel E. Sanborn, Marcelo V. Negrao, Aria Vaishnavi, and Egbert F. Smit. Brafv600e-mutant metastatic nsclc: disease overview and treatment landscape. NPJ Precision Oncology, Apr 2024. URL: https://doi.org/10.1038/s41698-024-00552-7, doi:10.1038/s41698-024-00552-7. This article has 45 citations and is from a peer-reviewed journal.

2. (planchard2024brafv600emutantmetastaticnsclc pages 1-2): David Planchard, Rachel E. Sanborn, Marcelo V. Negrao, Aria Vaishnavi, and Egbert F. Smit. Brafv600e-mutant metastatic nsclc: disease overview and treatment landscape. NPJ Precision Oncology, Apr 2024. URL: https://doi.org/10.1038/s41698-024-00552-7, doi:10.1038/s41698-024-00552-7. This article has 45 citations and is from a peer-reviewed journal.

3. (odogwu2018fdaapprovalsummary pages 1-2): Lauretta Odogwu, Luckson Mathieu, Gideon Blumenthal, Erin Larkins, Kirsten B. Goldberg, Norma Griffin, Karen Bijwaard, Eunice Y. Lee, Reena Philip, Xiaoping Jiang, Lisa Rodriguez, Amy E. McKee, Patricia Keegan, and Richard Pazdur. Fda approval summary: dabrafenib and trametinib for the treatment of metastatic non‐small cell lung cancers harboring braf v600e mutations. The Oncologist, 23:740-745, Feb 2018. URL: https://doi.org/10.1634/theoncologist.2017-0642, doi:10.1634/theoncologist.2017-0642. This article has 271 citations.

4. (planchard2016dabrafenibplustrametinib pages 1-1): David Planchard, Benjamin Besse, Harry J M Groen, Pierre-Jean Souquet, Elisabeth Quoix, Christina S Baik, Fabrice Barlesi, Tae Min Kim, Julien Mazieres, Silvia Novello, James R Rigas, Allison Upalawanna, Anthony M D'Amelio, Pingkuan Zhang, Bijoyesh Mookerjee, and Bruce E Johnson. Dabrafenib plus trametinib in patients with previously treated braf(v600e)-mutant metastatic non-small cell lung cancer: an open-label, multicentre phase 2 trial. The Lancet. Oncology, 17 7:984-993, Jul 2016. URL: https://doi.org/10.1016/s1470-2045(16)30146-2, doi:10.1016/s1470-2045(16)30146-2. This article has 1079 citations.

5. (baik2024apracticalreview pages 1-3): Christina Baik, Michael L. Cheng, Martin Dietrich, Jhanelle E. Gray, and Nagla A. Karim. A practical review of encorafenib and binimetinib therapy management in patients with braf v600e-mutant metastatic non-small cell lung cancer. Advances in Therapy, 41:2586-2605, May 2024. URL: https://doi.org/10.1007/s12325-024-02839-4, doi:10.1007/s12325-024-02839-4. This article has 10 citations and is from a peer-reviewed journal.

6. (yan2024efficacyofchemoimmunotherapy pages 1-2): Ningning Yan, Huixian Zhang, Sanxing Guo, Ziheng Zhang, Yingchun Xu, Liang Xu, and Xingya Li. Efficacy of chemo-immunotherapy in metastatic braf-mutated lung cancer: a single-center retrospective data. Frontiers in Oncology, Jan 2024. URL: https://doi.org/10.3389/fonc.2024.1353491, doi:10.3389/fonc.2024.1353491. This article has 6 citations.

7. (fan2024efficacysafetyand pages 1-2): Yun Fan, Jianying Zhou, Yuanyuan Zhao, Yan Yu, Nong Yang, Juan Li, Jialei Wang, Jun Zhao, Zhehai Wang, Jun Chen, Tong Zhu, Haifu Li, Vanessa Q. Passos, Denise Bury-Maynard, and Li Zhang. Efficacy, safety, and quality of life of dabrafenib plus trametinib treatment in chinese patients with brafv600e mutation-positive metastatic non-small cell lung cancer. Translational Lung Cancer Research, 13:3382-3391, Dec 2024. URL: https://doi.org/10.21037/tlcr-24-494, doi:10.21037/tlcr-24-494. This article has 2 citations and is from a peer-reviewed journal.

8. (pan2019dabrafenibplustrametinib pages 1-2): Janet Pan. Dabrafenib plus trametinib for braf v600e-mutant non-small cell lung cancer: a patient case report. Clinical Drug Investigation, 39:1003-1007, Jun 2019. URL: https://doi.org/10.1007/s40261-019-00823-3, doi:10.1007/s40261-019-00823-3. This article has 12 citations and is from a peer-reviewed journal.

9. (mezquita2024resistancetobraf pages 1-2): Laura Mezquita, Marianne Oulhen, Agathe Aberlenc, Marc Deloger, Mihaela Aldea, Aurélie Honore, Yann Lecluse, Karen Howarth, Luc Friboulet, Benjamin Besse, David Planchard, and Françoise Farace. Resistance to braf inhibition explored through single circulating tumour cell molecular profiling in braf-mutant non-small-cell lung cancer. British Journal of Cancer, 130:682-693, Jan 2024. URL: https://doi.org/10.1038/s41416-023-02535-0, doi:10.1038/s41416-023-02535-0. This article has 8 citations and is from a domain leading peer-reviewed journal.

10. (ibrahim2024navigatingthecomplexity pages 7-8): Sufyan Ibrahim, Smita Shenoy, Ramya Kateel, Shreya Hegde, Amrita Parida, and Lipsita Samantaray. Navigating the complexity of braf mutations in non-small cell lung cancer: current insights and future prospects. Multidisciplinary Respiratory Medicine, Nov 2024. URL: https://doi.org/10.5826/mrm.2024.992, doi:10.5826/mrm.2024.992. This article has 3 citations and is from a peer-reviewed journal.

11. (planchard2024brafv600emutantmetastaticnsclc pages 10-11): David Planchard, Rachel E. Sanborn, Marcelo V. Negrao, Aria Vaishnavi, and Egbert F. Smit. Brafv600e-mutant metastatic nsclc: disease overview and treatment landscape. NPJ Precision Oncology, Apr 2024. URL: https://doi.org/10.1038/s41698-024-00552-7, doi:10.1038/s41698-024-00552-7. This article has 45 citations and is from a peer-reviewed journal.

12. (riely2023phaseiiopenlabel pages 1-2): Gregory J. Riely, Egbert F. Smit, Myung-Ju Ahn, Enriqueta Felip, Suresh S. Ramalingam, Anne Tsao, Melissa Johnson, Francesco Gelsomino, Raymond Esper, Ernest Nadal, Michael Offin, Mariano Provencio, Jeffrey Clarke, Maen Hussain, Gregory A. Otterson, Ibiayi Dagogo-Jack, Jonathan W. Goldman, Daniel Morgensztern, Ann Alcasid, Tiziana Usari, Paul Wissel, Keith Wilner, Nuzhat Pathan, Svitlana Tonkovyd, and Bruce E. Johnson. Phase ii, open-label study of encorafenib plus binimetinib in patients with <i>braf</i><sup>v600</sup>-mutant metastatic non–small-cell lung cancer. Journal of Clinical Oncology, 41:3700-3711, Jul 2023. URL: https://doi.org/10.1200/jco.23.00774, doi:10.1200/jco.23.00774. This article has 130 citations and is from a highest quality peer-reviewed journal.

13. (odogwu2018fdaapprovalsummary pages 3-5): Lauretta Odogwu, Luckson Mathieu, Gideon Blumenthal, Erin Larkins, Kirsten B. Goldberg, Norma Griffin, Karen Bijwaard, Eunice Y. Lee, Reena Philip, Xiaoping Jiang, Lisa Rodriguez, Amy E. McKee, Patricia Keegan, and Richard Pazdur. Fda approval summary: dabrafenib and trametinib for the treatment of metastatic non‐small cell lung cancers harboring braf v600e mutations. The Oncologist, 23:740-745, Feb 2018. URL: https://doi.org/10.1634/theoncologist.2017-0642, doi:10.1634/theoncologist.2017-0642. This article has 271 citations.

14. (riely2023phaseiiopenlabel pages 6-8): Gregory J. Riely, Egbert F. Smit, Myung-Ju Ahn, Enriqueta Felip, Suresh S. Ramalingam, Anne Tsao, Melissa Johnson, Francesco Gelsomino, Raymond Esper, Ernest Nadal, Michael Offin, Mariano Provencio, Jeffrey Clarke, Maen Hussain, Gregory A. Otterson, Ibiayi Dagogo-Jack, Jonathan W. Goldman, Daniel Morgensztern, Ann Alcasid, Tiziana Usari, Paul Wissel, Keith Wilner, Nuzhat Pathan, Svitlana Tonkovyd, and Bruce E. Johnson. Phase ii, open-label study of encorafenib plus binimetinib in patients with <i>braf</i><sup>v600</sup>-mutant metastatic non–small-cell lung cancer. Journal of Clinical Oncology, 41:3700-3711, Jul 2023. URL: https://doi.org/10.1200/jco.23.00774, doi:10.1200/jco.23.00774. This article has 130 citations and is from a highest quality peer-reviewed journal.

15. (o’leary2019targetingbrafmutations pages 1-2): Connor Gerard O’Leary, Vladamir Andelkovic, Rahul Ladwa, Nick Pavlakis, Caicun Zhou, Fred Hirsch, Derek Richard, and Kenneth O’Byrne. Targeting braf mutations in non-small cell lung cancer. Translational lung cancer research, 8 6:1119-1124, Dec 2019. URL: https://doi.org/10.21037/tlcr.2019.10.22, doi:10.21037/tlcr.2019.10.22. This article has 127 citations and is from a peer-reviewed journal.

16. (baik2024apracticalreview media 088d26fe): Christina Baik, Michael L. Cheng, Martin Dietrich, Jhanelle E. Gray, and Nagla A. Karim. A practical review of encorafenib and binimetinib therapy management in patients with braf v600e-mutant metastatic non-small cell lung cancer. Advances in Therapy, 41:2586-2605, May 2024. URL: https://doi.org/10.1007/s12325-024-02839-4, doi:10.1007/s12325-024-02839-4. This article has 10 citations and is from a peer-reviewed journal.

17. (baik2024apracticalreview pages 3-4): Christina Baik, Michael L. Cheng, Martin Dietrich, Jhanelle E. Gray, and Nagla A. Karim. A practical review of encorafenib and binimetinib therapy management in patients with braf v600e-mutant metastatic non-small cell lung cancer. Advances in Therapy, 41:2586-2605, May 2024. URL: https://doi.org/10.1007/s12325-024-02839-4, doi:10.1007/s12325-024-02839-4. This article has 10 citations and is from a peer-reviewed journal.

18. (melzer2021expandedaccessto pages 1-2): Anne C. Melzer and Timothy J. Wilt. Expanded access to lung cancer screening—implementing wisely to optimize health. JAMA Network Open, 4:e210275, Mar 2021. URL: https://doi.org/10.1001/jamanetworkopen.2021.0275, doi:10.1001/jamanetworkopen.2021.0275. This article has 24 citations and is from a peer-reviewed journal.

19. (ritzwoller2021evaluationofpopulationlevel pages 2-4): Debra P. Ritzwoller, Rafael Meza, Nikki M. Carroll, Erica Blum-Barnett, Andrea N. Burnett-Hartman, Robert T. Greenlee, Stacey A. Honda, Christine Neslund-Dudas, Katharine A. Rendle, and Anil Vachani. Evaluation of population-level changes associated with the 2021 us preventive services task force lung cancer screening recommendations in community-based health care systems. JAMA Network Open, 4:e2128176, Oct 2021. URL: https://doi.org/10.1001/jamanetworkopen.2021.28176, doi:10.1001/jamanetworkopen.2021.28176. This article has 62 citations and is from a peer-reviewed journal.

20. (ji2007mutationsinbraf pages 1-2): Hongbin Ji, Zhenxiong Wang, Samanthi A. Perera, Danan Li, Mei-Chih Liang, Sara Zaghlul, Kate McNamara, Liang Chen, Mitchell Albert, Yanping Sun, Ruqayyah Al-Hashem, Lucian R. Chirieac, Robert Padera, Roderick T. Bronson, Roman K. Thomas, Levi A. Garraway, Pasi A. Jänne, Bruce E. Johnson, Lynda Chin, and Kwok-Kin Wong. Mutations in braf and kras converge on activation of the mitogen-activated protein kinase pathway in lung cancer mouse models. Cancer research, 67 10:4933-9, May 2007. URL: https://doi.org/10.1158/0008-5472.can-06-4592, doi:10.1158/0008-5472.can-06-4592. This article has 224 citations and is from a highest quality peer-reviewed journal.

21. (shai2015tp53silencingbypasses pages 1-3): Anny Shai, David Dankort, Joseph Juan, Shon Green, and Martin McMahon. Tp53 silencing bypasses growth arrest of brafv600e-induced lung tumor cells in a two-switch model of lung tumorigenesis. Cancer research, 75 15:3167-80, Aug 2015. URL: https://doi.org/10.1158/0008-5472.can-14-3701, doi:10.1158/0008-5472.can-14-3701. This article has 24 citations and is from a highest quality peer-reviewed journal.
