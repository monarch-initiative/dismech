---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-25T10:48:27.655005'
end_time: '2026-07-25T10:54:29.377301'
duration_seconds: 361.72
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pediatric Acute-onset Neuropsychiatric Syndrome
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 36
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Pediatric_Acute-Onset_Neuropsychiatric_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pediatric Acute-onset Neuropsychiatric Syndrome
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Pediatric Acute-onset Neuropsychiatric Syndrome** covering all of the
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
- **Disease Name:** Pediatric Acute-onset Neuropsychiatric Syndrome
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Pediatric Acute-onset Neuropsychiatric Syndrome** covering all of the
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


# Pediatric Acute-onset Neuropsychiatric Syndrome (PANS): research report

## Executive summary

Pediatric acute-onset neuropsychiatric syndrome (PANS) is a **clinical, etiologically heterogeneous syndrome**, not a single proven autoimmune disease. It is defined by an abrupt, dramatic onset—usually within 48 hours—of obsessive-compulsive disorder (OCD) and/or severely restricted food intake, accompanied by acute symptoms in at least two additional neuropsychiatric domains and not better explained by another disorder. PANDAS is the narrower proposed subgroup temporally associated with group A streptococcal infection (GAS). Current evidence supports immune-mediated disease in a subset, but no causal gene, pathogen, autoantibody, imaging signature, or laboratory test establishes the diagnosis. Accordingly, “autoimmune” is best treated as a **proposed mechanism/subcategory**, rather than an established property of every PANS case. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 4-5, trifiletti2022identificationofultrarare pages 1-2, wilbur2019pandaspansinchildhood pages 1-1)

The most current major source identified was the October 2024 Delphi consensus, which describes itself as providing updated shared clinical guidance but concludes that additional randomized controlled trials are required. Its abstract states: **“Lights and shadows remain upon the management of children with PANS and PANDAS”** and **“more randomized and controlled trials are needed.”** DOI: [10.3389/fimmu.2024.1420663](https://doi.org/10.3389/fimmu.2024.1420663). (grandinetti2024pediatricacuteonsetneuropsychiatric pages 4-5)

| domain | best-supported finding | suggested ontology terms/IDs (only where confident) | evidence type/strength | key citation DOI/PMID or NCT |
|---|---|---|---|---|
| Definition / criteria | PANS is a clinical syndrome defined by abrupt, dramatic onset of OCD or severely restricted food intake, plus at least 2 additional acute neuropsychiatric symptom categories, not better explained by another neurologic/medical disorder. Onset is typically described within 48 hours. | HPO: Obsessive-compulsive behavior; Food refusal / restricted intake; Anxiety; Emotional lability; Irritability; Developmental regression; Decline in school performance; Sensory disturbance; Sleep disturbance; Enuresis/urinary frequency. MAXO: not applicable. | Consensus/guideline and review evidence; moderate for criteria, low for biological specificity because criteria are syndromic and non-pathognomonic (grandinetti2024pediatricacuteonsetneuropsychiatric pages 4-5, wilbur2019pandaspansinchildhood pages 2-3, gagliano2023pediatricacuteonsetneuropsychiatric pages 2-4) | DOI:10.3389/fimmu.2024.1420663; PMID 25325534; DOI:10.2147/NDT.S362202 |
| Identifiers / nosology | MeSH term is present in ClinicalTrials-derived browse data as “Pediatric acute-onset neuropsychiatric syndrome.” MONDO/OMIM/Orphanet identifiers were not established from available evidence. PANS is not formally recognized as a DSM-5-TR standalone disorder. | MeSH: Pediatric acute-onset neuropsychiatric syndrome; MONDO: not established; OMIM: not established; Orphanet: not established. | Moderate for MeSH presence; low/unknown for cross-ontology mapping in available context (gagliano2023pediatricacuteonsetneuropsychiatric pages 1-2, NCT04508530 chunk 2, NCT02889016 chunk 1, NCT04609761 chunk 2) | NCT04508530; NCT02889016; NCT04609761 |
| Synonyms / related entities | Related terms include PANDAS (subset linked to streptococcal infection), Childhood Acute Neuropsychiatric Symptoms/CANS, and acute-onset OCD phenotype. PANDAS is considered a subset of PANS rather than a synonym. | No confident ontology IDs beyond MeSH term above. | Consensus/review; moderate (grandinetti2024pediatricacuteonsetneuropsychiatric pages 4-5, grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16, NCT02190292 chunk 1) | DOI:10.3389/fimmu.2024.1420663; NCT02190292 |
| Core phenotypes | Reported frequencies in one cohort/review summary: obsessions/compulsions 89%, anxiety 78%, emotional lability/depression 71%, sleep disorders 69%, attention deficit 63%, tics 62%, motor abnormalities 60%, school decline 50%, sensory abnormalities 50%, irritability/aggression 44%, urinary frequency 44%, hyperactivity 43%, eating disorders 40%, behavioral regression 40%, pain 38%. | HPO suggestions: Obsessive-compulsive behavior; Anxiety; Depressed mood; Sleep disturbance; Tic; Abnormality of movement; Attention-deficit/hyperactivity; Learning or school difficulty; Sensory disturbance; Irritability; Urinary frequency; Food refusal. | Observational/cohort summarized in review; moderate for phenotype spectrum, low-moderate for exact frequencies across settings (gagliano2023pediatricacuteonsetneuropsychiatric pages 2-4, gagliano2023pediatricacuteonsetneuropsychiatric pages 1-2) | DOI:10.2147/NDT.S362202 |
| Age / sex distribution | Mean onset reported around 7±2 years; peak onset 5–12 years; male predominance around 2:1 has been reported. | HPO: Childhood onset. | Review/consensus; moderate (grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16, gagliano2023pediatricacuteonsetneuropsychiatric pages 1-2) | DOI:10.3389/fimmu.2024.1420663; DOI:10.2147/NDT.S362202 |
| Quality-of-life / functional burden | Symptoms can cause marked functional impairment, school decline, missed activities, and high caregiver burden; one sequencing paper states caregiver burden during first flare exceeds Alzheimer disease caregiving. | HPO: Impaired social/academic functioning; MAXO: supportive educational/psychological interventions. | Observational/review; moderate for substantial burden, low for cross-disease burden comparison generalizability (trifiletti2022identificationofultrarare pages 1-2, NCT04609761 chunk 1) | DOI:10.1038/s41598-022-15279-3; NCT04609761 |
| Epidemiology | True incidence/prevalence remain uncertain; available reviews emphasize lack of rigorous epidemiology, though PANS may account for at least 1 in 20 pediatric-onset OCD cases in some estimates. | Not applicable. | Low-moderate; estimate-based and heterogeneous (grandinetti2024pediatricacuteonsetneuropsychiatric pages 4-5, gagliano2023pediatricacuteonsetneuropsychiatric pages 2-4) | DOI:10.3389/fimmu.2024.1420663; DOI:10.2147/NDT.S362202 |
| Triggers: infectious | Infectious triggers reported include group A streptococcal infection, Mycoplasma pneumoniae, Borrelia burgdorferi, Staphylococcus aureus, and viral infections including Epstein-Barr, influenza, coxsackie, varicella, and SARS-CoV-2. PANDAS specifically requires temporal association with GAS. | CHEBI/NCBI Taxonomy not confidently assigned here. HPO: Postinfectious onset not available from provided evidence. | Review/consensus; moderate for association, low for proof of causality per pathogen (grandinetti2024pediatricacuteonsetneuropsychiatric pages 4-5, grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16, gagliano2023pediatricacuteonsetneuropsychiatric pages 1-2) | DOI:10.3389/fimmu.2024.1420663; DOI:10.2147/NDT.S362202 |
| Triggers: noninfectious | Emotional stress and possible oxidative toxin exposure have been proposed as noninfectious triggers; these remain not established causal factors. | Not established. | Low/speculative (gagliano2023pediatricacuteonsetneuropsychiatric pages 1-2) | DOI:10.2147/NDT.S362202 |
| Genetics | No single causal gene is established for PANS. Candidate ultra-rare variants were reported in 11 genes in 21/396 sequenced cases: PPM1D, SGCE, PLCG2, NLRC4, CACNA1B, SHANK3, CHEK2/CHK2, GRIN2A, RAG1, GABRG2, SYNGAP1. These are candidate susceptibility genes, not diagnostic or causal markers. | HGNC gene symbols: PPM1D, SGCE, PLCG2, NLRC4, CACNA1B, SHANK3, CHEK2, GRIN2A, RAG1, GABRG2, SYNGAP1. | Human sequencing study; moderate for candidate-gene signal, low for causality/clinical validity (trifiletti2022identificationofultrarare pages 1-2) | DOI:10.1038/s41598-022-15279-3 |
| Family history / heritable predisposition | Increased family history of OCD, tics, and acute rheumatic fever has been reported; about 50% of cases may have pre-existing neurodevelopmental disorders, suggesting predisposition rather than monogenic inheritance. | HPO: Obsessive-compulsive behavior; Tic; Neurodevelopmental abnormality (general suggestion only). | Observational/review/consensus; low-moderate (grandinetti2024pediatricacuteonsetneuropsychiatric pages 4-5, trifiletti2022identificationofultrarare pages 1-2) | DOI:10.3389/fimmu.2024.1420663; DOI:10.1038/s41598-022-15279-3 |
| Pathophysiology: immune / autoimmune | Current leading model is infection- or inflammation-triggered neuroimmune dysregulation affecting brain circuits, but definitive autoimmune proof is lacking. Reported serum/CSF-associated markers include antibodies to dopamine D1/D2 receptors, lysoganglioside-GM1, β-tubulin, and elevated CaMKII activity; no biomarker is pathognomonic. | GO suggestions: immune response; inflammatory response; regulation of microglial activation; synaptic signaling. CL: microglial cell. | Review/consensus with inconsistent biomarker studies; low-moderate (grandinetti2024pediatricacuteonsetneuropsychiatric pages 4-5, gagliano2023pediatricacuteonsetneuropsychiatric pages 1-2, gagliano2023pediatricacuteonsetneuropsychiatric pages 22-23, wilbur2019pandaspansinchildhood pages 1-1) | DOI:10.3389/fimmu.2024.1420663; DOI:10.2147/NDT.S362202 |
| Pathophysiology: candidate mechanisms | Sequencing and model-based interpretations suggest convergence on peripheral immune signaling, microglia, synaptic function, and blood-CSF/brain barrier vulnerability. | GO suggestions: synaptic signaling; regulation of cytokine production; blood-brain barrier maintenance. CL: microglial cell; neuron. | Mechanistic hypothesis from human genetics/review; low-moderate (trifiletti2022identificationofultrarare pages 1-2) | DOI:10.1038/s41598-022-15279-3 |
| Anatomy / neuroanatomy | Neuroimaging abnormalities have been reported in thalamus, basal ganglia, amygdala, and putamen; basal ganglia circuitry is a recurrent focus in PANS/PANDAS literature. | UBERON suggestions: brain; basal ganglion; thalamus; amygdala; putamen. | Review/consensus/observational; moderate for implicated regions, low for specificity (grandinetti2024pediatricacuteonsetneuropsychiatric pages 4-5, trifiletti2022identificationofultrarare pages 1-2, NCT02889016 chunk 1, NCT04609761 chunk 1) | DOI:10.3389/fimmu.2024.1420663; DOI:10.1038/s41598-022-15279-3; NCT02889016; NCT04609761 |
| Cell types / tissue level | Microglia are repeatedly implicated in proposed neuroinflammatory models; neuronal synapses are implicated by candidate genes. Specific pathogenic cell type is not established in human tissue. | CL: microglial cell; neuron. GO: microglial activation; synaptic signaling. | Mechanistic/model-informed inference; low-moderate (trifiletti2022identificationofultrarare pages 1-2) | DOI:10.1038/s41598-022-15279-3 |
| Diagnostics: overall approach | Diagnosis is clinical and exclusionary. Recommended workup includes physical, psychiatric, neurologic, and neuropsychological evaluation; targeted laboratory testing; and MRI/EEG/sleep evaluation, with CSF analysis reserved for severe or encephalitic presentations. | MAXO: MRI; EEG; cerebrospinal fluid examination; cognitive behavioral therapy assessment not an ontology certainty here. | Consensus/review; moderate (gagliano2023pediatricacuteonsetneuropsychiatric pages 22-23, NCT02889016 chunk 1, NCT04609761 chunk 1) | DOI:10.2147/NDT.S362202; NCT02889016; NCT04609761 |
| Diagnostics: biomarkers | Infectious parameters have the strongest practical support when infection is suspected. D1/D2 receptor antibodies, lyso-GM1, β-tubulin, and CaMKII activity have been reported, but individual biomarkers lack sufficient sensitivity/specificity for diagnosis; no validated standalone biomarker exists. Cunningham panel utility remains uncertain. | No confident ontology IDs. | Moderate that no validated biomarker exists; low for specific assay clinical utility (grandinetti2024pediatricacuteonsetneuropsychiatric pages 4-5, gagliano2023pediatricacuteonsetneuropsychiatric pages 22-23, NCT02190292 chunk 1) | DOI:10.3389/fimmu.2024.1420663; DOI:10.2147/NDT.S362202; NCT02190292 |
| Differential diagnosis | Important exclusions include Sydenham chorea, autoimmune encephalitis/encephalitis, systemic lupus erythematosus, Tourette disorder, primary OCD, psychotic disorders, autism-related regression, and other neurologic/medical causes. | HPO/ontology not enumerated from evidence. | Consensus/guideline; moderate (wilbur2019pandaspansinchildhood pages 2-3, NCT04508530 chunk 1, NCT04609761 chunk 2) | PMID 25325534; NCT04508530; NCT04609761 |
| Disease course | Often acute/subacute at onset with episodic, relapsing-remitting, or chronic progressive/disintegrative course; stabilization between flares may occur. | HPO: Episodic course; relapsing-remitting course (general suggestions). | Review/consensus; moderate (wilbur2019pandaspansinchildhood pages 2-3, gagliano2023pediatricacuteonsetneuropsychiatric pages 1-2, NCT04508530 chunk 1) | DOI:10.2147/NDT.S362202; NCT04508530 |
| Prognosis / natural history | Long-term natural history is incompletely defined; some children improve substantially over time, but reviews caution that improvement may reflect fluctuating natural course rather than treatment effect alone. | Not applicable. | Low-moderate (wilbur2019pandaspansinchildhood pages 4-4, wilbur2019pandaspansinchildhood pages 5-6, NCT02190292 chunk 1) | DOI:10.1093/pch/pxy145; NCT02190292 |
| First-line symptomatic treatment | CBT/ERP and SSRIs are commonly recommended first-line symptomatic treatments for OCD/anxiety symptoms; consensus advises not delaying psychiatric treatment while etiologic workup proceeds. Medication intolerance/sensitivity may be higher than in typical pediatric psychiatric populations. | MAXO suggestions: cognitive behavioral therapy; selective serotonin reuptake inhibitor therapy. | Consensus plus small studies/observational evidence; moderate for use, low-moderate for disease-specific efficacy (grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16, gagliano2023pediatricacuteonsetneuropsychiatric pages 18-20, gagliano2023pediatricacuteonsetneuropsychiatric pages 20-22, NCT01617083 chunk 2) | DOI:10.3389/fimmu.2024.1420663; DOI:10.2147/NDT.S362202; NCT01617083 |
| Antibiotics | Antibiotics are recommended when active infection is identified. Evidence for disease-modifying benefit without active infection is mixed: a 4-week randomized azithromycin trial exists; long-term prophylaxis is not well supported. | MAXO suggestion: antibiotic therapy. | Moderate for treating documented infection; low-moderate for psychiatric symptom benefit beyond infection control (gagliano2023pediatricacuteonsetneuropsychiatric pages 18-20, wilbur2019pandaspansinchildhood pages 3-4, gagliano2023pediatricacuteonsetneuropsychiatric pages 20-22, NCT01617083 chunk 1, NCT01617083 chunk 2) | NCT01617083; DOI:10.1093/pch/pxy145; DOI:10.2147/NDT.S362202 |
| NSAIDs / corticosteroids | NSAIDs and short corticosteroid courses are used in some protocols, especially mild to moderate inflammatory presentations, but evidence is limited and largely observational/consensus-based. | MAXO suggestions: nonsteroidal anti-inflammatory drug therapy; corticosteroid therapy. | Low-moderate (grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16, wilbur2019pandaspansinchildhood pages 3-4) | DOI:10.3389/fimmu.2024.1420663; DOI:10.1093/pch/pxy145 |
| IVIG | IVIG is frequently used for moderate-to-severe or selected inflammatory PANS in expert protocols. Evidence includes older small controlled studies, observational/open-label studies, and recent/ongoing phase 2-3 trials; benefit remains debated and not definitively established. | MAXO suggestion: intravenous immunoglobulin therapy. | Moderate for clinical use; low-moderate for definitive efficacy due to heterogeneous and limited trials (gagliano2023pediatricacuteonsetneuropsychiatric pages 18-20, wilbur2019pandaspansinchildhood pages 3-4, wilbur2019pandaspansinchildhood pages 4-4, NCT04508530 chunk 1, NCT04609761 chunk 1, NCT04609761 chunk 2) | NCT04508530; NCT04609761; DOI:10.1093/pch/pxy145 |
| Plasma exchange | Therapeutic plasma exchange is reserved in expert guidance for extreme/life-threatening impairment; observational data suggest improvement in severe cases, but controlled evidence is limited. | MAXO suggestion: therapeutic plasma exchange. | Low-moderate (gagliano2023pediatricacuteonsetneuropsychiatric pages 18-20, wilbur2019pandaspansinchildhood pages 4-4) | DOI:10.2147/NDT.S362202; DOI:10.1093/pch/pxy145 |
| Rituximab / other immunomodulators | Rituximab is not routinely recommended for PANS and is generally reserved, if at all, for definite autoimmune encephalitis or highly selected refractory cases. Evidence in PANS specifically is minimal/not established. | MAXO suggestion: rituximab therapy. | Low/not established (gagliano2023pediatricacuteonsetneuropsychiatric pages 18-20, grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16, NCT04508530 chunk 2) | DOI:10.2147/NDT.S362202; NCT04508530 |
| Adverse effects / safety | IVIG adverse effects include nausea, myalgia, fever, chills/rigors, chest discomfort, hypotension, headache. Azithromycin trial protocols monitored hepatic toxicity and QTc prolongation. Psychotropics may require dose changes due to side effects in a high proportion of patients. | MAXO: adverse event monitoring; ECG monitoring; liver function monitoring. | Moderate for expected treatment-related adverse effects from protocols/reviews (gagliano2023pediatricacuteonsetneuropsychiatric pages 18-20, gagliano2023pediatricacuteonsetneuropsychiatric pages 20-22, NCT01617083 chunk 2, NCT04609761 chunk 1) | NCT01617083; NCT04609761; DOI:10.2147/NDT.S362202 |
| Prevention | No established primary prevention exists for PANS. Prevention of recurrent infectious triggers and prompt treatment of active infections are used pragmatically. A 2024 consensus mentions vitamin D prophylaxis suggestion, but this is not established standard-of-care. | MAXO suggestions: infection prevention/treatment; vitamin supplementation (vitamin D) only as low-confidence suggestion. | Low (grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16) | DOI:10.3389/fimmu.2024.1420663 |
| Real-world research implementation | Active real-world studies include biomarker discovery, longitudinal cohort characterization, and interventional trials: Stanford biomarker cohort (500 planned; NCT02889016), Scandinavian cohort (NCT02190292), azithromycin RCT (NCT01617083), IVIG open-label study (NCT04609761), and phase III Panzyga crossover trial (NCT04508530). | Not applicable. | Strong for existence of implementation/trials (NCT01617083 chunk 1, NCT04508530 chunk 1, NCT02889016 chunk 1, NCT04609761 chunk 1, NCT02190292 chunk 1) | NCT02889016; NCT02190292; NCT01617083; NCT04609761; NCT04508530 |
| Evidence gaps / unknowns | Not established: single causal gene, validated diagnostic biomarker, prevalence/incidence, definitive autoimmune mechanism, standardized evidence-based treatment hierarchy, or disease-specific prevention strategy. | MONDO/OMIM/Orphanet IDs not established from available evidence. | Strong agreement across reviews/consensus that major gaps remain (grandinetti2024pediatricacuteonsetneuropsychiatric pages 4-5, gagliano2023pediatricacuteonsetneuropsychiatric pages 22-23, wilbur2019pandaspansinchildhood pages 1-1, wilbur2019pandaspansinchildhood pages 5-6) | DOI:10.3389/fimmu.2024.1420663; DOI:10.2147/NDT.S362202; DOI:10.1093/pch/pxy145 |


*Table: This compact table summarizes the best-supported current findings for Pediatric Acute-onset Neuropsychiatric Syndrome across definition, phenotypes, triggers, candidate genetics, mechanisms, diagnostics, course, and treatment. It explicitly distinguishes established clinical criteria from areas that remain uncertain or unvalidated.*

## 1. Disease information

### Definition and criteria

The working criteria are:

1. Abrupt, dramatic onset of OCD and/or severe restriction of food intake, generally within 48 hours.
2. Concurrent, comparably acute symptoms in at least two domains: anxiety; emotional lability/depression; irritability, aggression, or severe oppositionality; developmental regression; deterioration in school performance; sensory or motor abnormalities; or somatic manifestations such as sleep disturbance, enuresis, or urinary frequency.
3. The presentation is not better explained by another neurologic or medical disorder. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 4-5, trifiletti2022identificationofultrarare pages 1-2, gagliano2023pediatricacuteonsetneuropsychiatric pages 2-4)

PANS is therefore a **syndrome of presentation and exclusion**. PANDAS additionally requires childhood onset, an episodic course, temporal association with GAS, and neurologic abnormalities such as motor hyperactivity or choreiform movements. It should be represented as a PANS-related subset, not as an exact synonym. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 4-5, NCT04508530 chunk 1)

### Identifiers and synonyms

- **Preferred name:** Pediatric acute-onset neuropsychiatric syndrome
- **Abbreviation:** PANS
- **MeSH:** “Pediatric acute-onset neuropsychiatric syndrome,” identifier shown in trial-derived MeSH data as **C000631768**. (NCT04508530 chunk 2, NCT02889016 chunk 1)
- **MONDO:** no confidently verified MONDO identifier was found in the retrieved authoritative material; Open Targets also did not resolve the disease name. Do not assign an inferred identifier without direct MONDO verification.
- **OMIM/Orphanet:** no established disease entry was verified. This is consistent with PANS not being a monogenic Mendelian disorder.
- **DSM-5-TR:** not a standalone diagnosis; the 2023 review suggests coding a qualifying case under “Obsessive-Compulsive and Related Disorder Due to Another Medical Condition” (294.8) when appropriate. (gagliano2023pediatricacuteonsetneuropsychiatric pages 1-2)
- **Related names:** PANDAS; childhood acute neuropsychiatric symptoms (CANS); acute-onset OCD phenotype. CANS is related historical terminology, while PANDAS is a proposed etiologic subset. (NCT02190292 chunk 1)

The evidence summarized here is **aggregated disease-level evidence** from consensus statements, cohorts, trials, and reviews. Clinical recognition in practice is based on individual history, examination, records, and targeted testing—not an EHR-derived computable phenotype alone.

## 2. Etiology, risk, and protective factors

### Causal and triggering factors

No single cause is established. The leading framework is a susceptible child plus an infectious, inflammatory, or other stressor, followed by neuroimmune and circuit dysfunction. Reported infectious associations include GAS, *Mycoplasma pneumoniae*, *Borrelia burgdorferi*, *Staphylococcus aureus*, Epstein–Barr virus, influenza, coxsackievirus, varicella-zoster virus, and SARS-CoV-2. Temporal association does not prove microbial causation, and PANS does not require infection. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16, gagliano2023pediatricacuteonsetneuropsychiatric pages 1-2)

Emotional stress and possible oxidative/toxic exposures have been proposed, but evidence is sparse and insufficient for causal attribution. Lifestyle factors such as diet, exercise, smoking, or alcohol have no established disease-specific role. Proposed streptococcal-associated gut dysbiosis is mechanistically plausible but remains investigational. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 4-5, gagliano2023pediatricacuteonsetneuropsychiatric pages 1-2)

### Susceptibility and gene–environment interaction

Family histories reportedly contain excess OCD, tic disorders, and acute rheumatic fever. Pre-existing neurodevelopmental disorders occur in substantial fractions of clinical cohorts; the 2024 consensus cites approximately 50%, while 12 of 21 genetically selected cases with candidate variants had a neurodevelopmental disorder. These observations support susceptibility but not Mendelian inheritance. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 4-5, trifiletti2022identificationofultrarare pages 1-2)

A plausible gene–environment chain is: immune/synaptic/barrier susceptibility → infection or inflammatory stress → peripheral immune activation and altered barrier function → microglial, antibody, or cytokine effects on cortico-striato-thalamo-cortical circuits → OCD, eating restriction, tics, affective symptoms, and cognitive dysfunction. Each intermediate step remains incompletely validated in human PANS. (trifiletti2022identificationofultrarare pages 1-2, gagliano2023pediatricacuteonsetneuropsychiatric pages 22-23)

### Protective factors

No reproducible genetic protective variant, diet, behavior, exposure, or prophylactic intervention is established. A 2024 Delphi statement suggested vitamin D prophylaxis, but this is consensus-level rather than trial-supported evidence and should not be encoded as proven prevention. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16)

## 3. Phenotypes

One review’s cohort summary reported obsessions/compulsions in 89%, anxiety 78%, emotional lability/depression 71%, sleep disorders 69%, attention deficit 63%, tics 62%, motor abnormalities 60%, decline in school performance 50%, sensory abnormalities 50%, urinary frequency 44%, irritability/aggression 44%, hyperactivity 43%, eating disorders 40%, developmental regression 40%, and pain 38%. These frequencies are cohort-dependent and should not be generalized as population prevalence. (gagliano2023pediatricacuteonsetneuropsychiatric pages 2-4)

Suggested HPO annotations include obsessive-compulsive behavior, anxiety, depressed mood, emotional lability, irritability, aggression, tic, abnormal involuntary movement, attention deficit/hyperactivity, developmental regression, sleep disturbance, urinary frequency, enuresis, food refusal/restricted intake, sensory disturbance, pain, and childhood onset. Exact HPO identifiers should be validated against the current HPO release before database loading.

Severity ranges from mild impairment to extreme or life-threatening illness, including inability to eat, suicidality, severe aggression, or profound functional collapse. The course is commonly fluctuating or episodic. School participation, family functioning, adaptive behavior, and quality of life can be markedly impaired; one genetics paper reported caregiver burden during the first flare exceeding that reported for Alzheimer-disease caregiving, although this comparison requires replication. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 4-5, trifiletti2022identificationofultrarare pages 1-2, NCT02889016 chunk 1)

## 4. Genetic and molecular information

PANS has **no validated causal gene, pathogenic variant set, inheritance pattern, penetrance estimate, carrier frequency, founder mutation, or diagnostic genetic test**. Therefore, ClinVar-style pathogenic classification for “PANS variants” is not currently appropriate.

A 2022 human WES/WGS study examined 386 US cases and 10 severe European cases. Twenty-one cases carried candidate de novo or ultra-rare variants (minor-allele frequency <0.001) in 11 genes: **PPM1D, SGCE, PLCG2, NLRC4, CACNA1B, SHANK3, CHEK2, GRIN2A, RAG1, GABRG2, and SYNGAP1**. The authors grouped these into immune/microglial genes and neuronal/synaptic genes. These are hypothesis-generating susceptibility candidates—not clinically validated PANS genes or ACMG-pathogenic variants for this syndrome. DOI: [10.1038/s41598-022-15279-3](https://doi.org/10.1038/s41598-022-15279-3). (trifiletti2022identificationofultrarare pages 1-2)

No reproducible PANS-specific epigenetic signature, chromosomal abnormality, somatic mutation, repeat expansion, mitochondrial defect, or modifier gene has been established. WES/WGS may be appropriate when an alternative neurodevelopmental, epileptic, metabolic, or immunologic disorder is suspected, but it is not a confirmatory PANS test.

## 5. Environmental and infectious information

The principal non-genetic evidence concerns infections and inflammatory stressors. GAS is specifically relevant to PANDAS, whereas PANS can follow multiple infections or no identified infection. Testing and treatment should therefore be directed by symptoms and exposure history rather than indiscriminate pathogen panels. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 4-5, gagliano2023pediatricacuteonsetneuropsychiatric pages 1-2, NCT01617083 chunk 1)

There is no established association with occupational exposure, radiation, air pollution, smoking, alcohol, or a specific dietary pattern. No zoonotic transmission or person-to-person transmission of PANS exists; transmissible infections may act as triggers, but the syndrome itself is noncommunicable.

## 6. Mechanism and pathophysiology

### Working causal model

1. **Upstream:** infection or inflammatory stress in a susceptible child.
2. **Peripheral response:** innate/adaptive immune activation, cytokine production, and possibly molecular mimicry.
3. **Interface:** altered blood–brain or blood–CSF barrier function may permit antibody or immune-cell effects in the CNS.
4. **CNS response:** microglial activation, neuroinflammation, and altered dopaminergic and synaptic signaling.
5. **Circuit dysfunction:** basal ganglia, thalamic, limbic, and cortico-striatal network disturbance.
6. **Downstream phenotype:** abrupt OCD/restricted eating, tics or motor abnormalities, anxiety, lability, regression, sleep and urinary symptoms. (trifiletti2022identificationofultrarare pages 1-2, gagliano2023pediatricacuteonsetneuropsychiatric pages 1-2, gagliano2023pediatricacuteonsetneuropsychiatric pages 22-23)

Reported antibody-related signals include dopamine D1/D2 receptor, lysoganglioside-GM1, β-tubulin antibodies, and CaMKII activation. However, studies are inconsistent, these findings are not specific to PANS, and no antibody is pathognomonic. The 2019 critical review states that **“definitive proof of the autoimmune hypothesis of PANDAS is lacking.”** (gagliano2023pediatricacuteonsetneuropsychiatric pages 22-23, wilbur2019pandaspansinchildhood pages 1-1)

Suggested biological-process annotations are immune response, inflammatory response, cytokine production, microglial activation, regulation of blood–brain barrier permeability, dopaminergic receptor signaling, synaptic signaling, and learning/memory. Suggested cell types are microglial cell, neuron, brain microvascular endothelial cell, T lymphocyte, B lymphocyte, monocyte/macrophage, and choroid-plexus epithelial cell; only microglial and neuronal involvement has substantial support in the retrieved PANS literature. (trifiletti2022identificationofultrarare pages 1-2)

Human transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, and CRISPR-screen signatures are not sufficiently replicated for clinical annotation. The Stanford prospective cohort plans PBMC collection for GWAS, CyTOF, T-cell-receptor analysis, antibody profiling, and monocyte characterization, illustrating current real-world multi-omic research rather than validated diagnostics. [NCT02889016](https://clinicaltrials.gov/study/NCT02889016). (NCT02889016 chunk 1)

## 7. Anatomical structures affected

The primary system is the CNS. Imaging and mechanistic studies implicate the **basal ganglia/putamen, thalamus, and amygdala**, although findings are neither universal nor diagnostic. Suggested UBERON concepts are brain, basal ganglion, putamen, thalamus, amygdala, cerebral cortex, choroid plexus, and brain microvasculature. No consistent lateralization is established. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 4-5, trifiletti2022identificationofultrarare pages 1-2)

At the tissue/cellular level, proposed sites include neural synapses, microglia, neurovascular endothelium, and the blood–CSF interface. No characteristic biopsy pathology or subcellular lesion is established; brain biopsy is not part of routine diagnosis.

## 8. Temporal development

Mean onset has been reported near 7±2 years, with a peak around 5–12 years; boys may outnumber girls approximately 2:1. The defining onset is abrupt, often within 48 hours. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16, gagliano2023pediatricacuteonsetneuropsychiatric pages 1-2)

Subsequent courses include monophasic improvement, episodic flares, relapsing-remitting disease, and chronic or progressive/disintegrative patterns. There is no accepted stage system. Long-term duration and remission probabilities remain uncertain, and apparent therapeutic response must be interpreted against spontaneous fluctuation. Early recognition is important for safety, nutrition, restoration of school/family function, and treatment of identifiable infection or inflammatory disease, but a formally validated therapeutic window has not been established. (wilbur2019pandaspansinchildhood pages 2-3, gagliano2023pediatricacuteonsetneuropsychiatric pages 1-2, wilbur2019pandaspansinchildhood pages 4-4)

## 9. Inheritance and population

No reliable incidence or prevalence per 100,000 is available. A review suggested PANS might represent at least 1 in 20 pediatric-onset OCD cases, but rigorous population ascertainment is lacking. Thus, this is not an appropriate substitute for population prevalence. (gagliano2023pediatricacuteonsetneuropsychiatric pages 2-4)

Reported demographics include childhood onset and male predominance. No robust ethnic, founder, geographic, consanguinity, anticipation, mosaicism, or carrier-frequency pattern is known. Inheritance is best classified as **unknown/multifactorial susceptibility**, not autosomal dominant, recessive, X-linked, or mitochondrial.

## 10. Diagnostics

### Clinical assessment

Diagnosis requires a detailed timeline documenting the abrupt onset; psychiatric assessment including CY-BOCS where OCD is present; neurologic and pediatric examination; nutritional and safety assessment; and exclusion of alternative causes. Neuropsychological, school, sleep, and functional evaluation may quantify impairment. (gagliano2023pediatricacuteonsetneuropsychiatric pages 22-23, NCT02889016 chunk 1)

Laboratory testing should be hypothesis-driven: throat culture or rapid testing when GAS is suspected; paired streptococcal serology where clinically informative; CBC, metabolic profile, inflammatory markers, urinalysis, and testing for other infection, autoimmune disease, immunodeficiency, endocrinopathy, or metabolic disease as indicated. A positive infectious marker documents exposure/infection, not PANS causation. (gagliano2023pediatricacuteonsetneuropsychiatric pages 22-23, NCT01617083 chunk 1)

MRI, EEG, polysomnography, or CSF examination are not routine confirmatory tests but may be warranted for focal neurologic findings, seizures, altered consciousness, psychosis, severe motor disorder, encephalitic features, or atypical progression. The Swedish IVIG protocol specifically required CSF evaluation when encephalitis could not otherwise be excluded. (NCT04609761 chunk 1, NCT04609761 chunk 2)

### Biomarkers and genetics

No validated diagnostic biomarker exists. The Cunningham panel and D1/D2, lysoganglioside-GM1, β-tubulin, and CaMKII assays lack sufficient demonstrated sensitivity, specificity, and external validation for standalone diagnosis. A Scandinavian study was expressly designed to evaluate Cunningham-panel sensitivity and specificity, reflecting unresolved clinical utility. [NCT02190292](https://clinicaltrials.gov/study/NCT02190292). (grandinetti2024pediatricacuteonsetneuropsychiatric pages 4-5, gagliano2023pediatricacuteonsetneuropsychiatric pages 22-23, NCT02190292 chunk 1)

WES, WGS, panels, CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion testing are not PANS tests. They should be selected only to evaluate a plausible alternative genetic diagnosis.

### Differential diagnosis

Key exclusions include primary OCD/eating disorder, tic or Tourette disorder, Sydenham chorea, autoimmune encephalitis, acute disseminated encephalomyelitis, epilepsy, systemic lupus erythematosus or CNS vasculitis, infectious encephalitis, Wilson disease, thyroid/metabolic disease, medication or substance effects, psychotic/bipolar disorders, functional neurologic disorder, and neurodevelopmental regression. Red flags—altered consciousness, seizures, focal deficits, autonomic instability, frank chorea, catatonia, or progressive cognitive decline—warrant urgent neurologic/encephalitis evaluation. (wilbur2019pandaspansinchildhood pages 2-3, NCT04508530 chunk 1, NCT04609761 chunk 2)

There is no asymptomatic population, newborn, carrier, prenatal, or cascade screening program.

## 11. Outcome and prognosis

PANS is not generally considered a primary fatal disorder, and disease-specific survival or mortality estimates are unavailable. Serious morbidity can arise from malnutrition/dehydration, suicidality, aggression, medication or immunotherapy complications, school loss, family disruption, and chronic psychiatric disability.

Recovery can be substantial, but the proportion achieving durable remission is uncertain. Studies have reported 60–80% symptom reduction over time in some cohorts, yet critical reviewers caution that this can reflect natural fluctuation, concurrent psychiatric treatment, or regression to the mean. Reliable prognostic biomarkers do not exist. Plausible adverse prognostic features include severe functional impairment, prolonged untreated symptoms, recurrent triggers, comorbid neurodevelopmental disease, and inability to restore nutrition or participation, but validated prediction models are absent. (wilbur2019pandaspansinchildhood pages 4-4, wilbur2019pandaspansinchildhood pages 5-6)

## 12. Treatment

Treatment should be individualized along three parallel tracks: **(1) safety and symptom-directed psychiatric/behavioral care; (2) identification and standard treatment of active infection or another medical cause; and (3) anti-inflammatory/immunomodulatory treatment only for carefully selected cases with credible inflammatory or autoimmune disease.** Neuropsychiatric treatment should not be delayed while etiologic testing proceeds. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16)

### Symptomatic and supportive care

CBT with exposure and response prevention (ERP) and cautious SSRI use are first-line approaches for OCD/anxiety. One small study reported response in all 8 participants and remission in 6; another reported significant OCD reduction in 33/62 after one year, without improvement in tic severity. These uncontrolled/small studies support feasibility rather than PANS-specific superiority. Suggested MAXO mappings: cognitive behavioral therapy, exposure-and-response prevention, psychiatric assessment, nutritional support, occupational therapy, and educational intervention. (gagliano2023pediatricacuteonsetneuropsychiatric pages 18-20, wilbur2019pandaspansinchildhood pages 3-3)

Psychotropics should be started low and titrated slowly. In one observational series, 54% experienced side effects requiring medication changes; rates were 38% for antidepressants and 49% for antipsychotics. (gagliano2023pediatricacuteonsetneuropsychiatric pages 20-22)

### Antimicrobials

Treat documented infections according to ordinary pediatric infectious-disease standards. A four-week randomized azithromycin study of 31 PANS children showed greater OCD-severity reduction than placebo but not broad improvement across other neuropsychiatric outcomes. The registered phase 2 study enrolled 47 participants aged 4–14 and monitored liver toxicity and QTc prolongation. [NCT01617083](https://clinicaltrials.gov/study/NCT01617083). (wilbur2019pandaspansinchildhood pages 3-3, NCT01617083 chunk 1, NCT01617083 chunk 2)

Evidence for prophylaxis is conflicting: one placebo-controlled penicillin study (n=37) did not reduce exacerbations or tic/OCD severity, whereas a small azithromycin/penicillin study (n=23) reported 96% fewer GAS infections and 61% fewer exacerbations. Routine long-term antibiotics without documented infection are therefore not supported by strong evidence. (wilbur2019pandaspansinchildhood pages 3-4, gagliano2023pediatricacuteonsetneuropsychiatric pages 20-22, wilbur2019pandaspansinchildhood pages 5-6)

### Anti-inflammatory and immunomodulatory therapy

NSAIDs and short corticosteroid bursts are used by specialty programs, but evidence is mostly retrospective. In one observational corticosteroid study (n=98), flares were approximately 3.5 weeks shorter; confounding and indication bias limit inference. (wilbur2019pandaspansinchildhood pages 3-4, grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16)

IVIG is used in selected moderate-to-severe inflammatory cases, but older controlled studies showed substantial placebo response and inconsistent separation from placebo. Open-label reports have described 50–55% mean CY-BOCS reduction and 67–80% responder rates by 24 weeks in a 24-patient series, but uncontrolled design and fluctuating disease course weaken causal interpretation. Common infusion reactions include headache, nausea, myalgia, fever, chills/rigors, chest discomfort, and hypotension; rare serious risks include thrombosis, renal injury, hemolysis, aseptic meningitis, and anaphylaxis. (gagliano2023pediatricacuteonsetneuropsychiatric pages 18-20, wilbur2019pandaspansinchildhood pages 3-4, wilbur2019pandaspansinchildhood pages 4-4)

A phase III randomized, quadruple-masked crossover trial of Panzyga 10% IVIG versus placebo enrolled 71 patients aged 6–17; the primary endpoint was percentage CY-BOCS change at week 9. It completed in 2024, but the retrieved 2024 evidence did not provide peer-reviewed outcome data, so no efficacy conclusion should be inferred here. [NCT04508530](https://clinicaltrials.gov/study/NCT04508530). (NCT04508530 chunk 1, NCT04508530 chunk 2)

An open-label Swedish phase 2 study administered IVIG 2 g/kg every four weeks for six months and assessed PANS severity, CY-BOCS, adaptive function, quality of life, cognition, school absence, and caregiver burden; its nonrandomized design limits causal inference. [NCT04609761](https://clinicaltrials.gov/study/NCT04609761); related publication PMID **35933358**. (NCT04609761 chunk 1, NCT04609761 chunk 2)

Therapeutic plasma exchange is reserved by some experts for extreme/life-threatening cases. A 35-patient severe-case series reported approximately 65% improvement at six months and 78% at longer follow-up, but this is observational. Rituximab, mycophenolate, and other sustained immunosuppression lack adequate PANS-specific evidence; Nordic guidance cited in the review advises against rituximab except where definite autoimmune encephalitis warrants it. (gagliano2023pediatricacuteonsetneuropsychiatric pages 18-20, wilbur2019pandaspansinchildhood pages 5-6)

Tonsillectomy/adenoidectomy is not supported as PANS/PANDAS therapy: studies comparing 20 surgical with 23 nonsurgical patients and a prospective cohort of 120 found no meaningful advantage in remission, relapse, symptom severity, or antibody titers. (wilbur2019pandaspansinchildhood pages 4-4)

No gene therapy, cell therapy, RNA therapeutic, surgery, or genotype-guided pharmacotherapy is established. Pharmacogenomic recommendations are the same as for the medication being used; there is no PANS-specific CPIC pathway.

## 13. Prevention

No proven primary prevention exists. Standard vaccination and prompt, guideline-concordant diagnosis and treatment of infections remain appropriate; evidence does not justify withholding routine immunization. Antibiotic prophylaxis is not routinely recommended because controlled evidence is inconsistent and risks include adverse reactions, microbiome disruption, *C. difficile*, and antimicrobial resistance. (wilbur2019pandaspansinchildhood pages 3-4, wilbur2019pandaspansinchildhood pages 5-6)

Secondary/tertiary prevention consists of early recognition of abrupt symptoms, safety and nutritional assessment, rapid treatment of confirmed infection, restoration of sleep and school participation, family education, relapse planning, and maintenance CBT/ERP skills. There is no validated genetic counseling or reproductive-risk protocol because no Mendelian inheritance is established.

## 14. Other species and natural disease

No naturally occurring veterinary disease has been established as a direct PANS homolog, and no breed, VBO identifier, cross-species transmission pattern, or zoonotic PANS risk is recognized. Animal neurobehavioral syndromes following infection may offer analogies, but they should not be encoded as spontaneous PANS.

## 15. Model organisms

The principal experimental analog is a GAS-exposure/immunization rodent model developed to study Sydenham chorea/PANDAS-like mechanisms. Streptococcal exposure in rats produced behavioral, pharmacologic, and immunologic abnormalities; the relevant primary publication is Brimberg et al., 2012, PMID **22534626**, DOI: [10.1038/npp.2012.56](https://doi.org/10.1038/npp.2012.56). (NCT02190292 chunk 1)

Passive-transfer and immunization studies support the possibility that anti-streptococcal antibodies can bind neural targets and alter behavior when CNS access is permitted. Their principal applications are molecular mimicry, blood–brain-barrier entry, basal-ganglia antibody binding, dopaminergic signaling, and microglial activation. Limitations are substantial: induced exposure is not equivalent to clinically heterogeneous PANS; rodent behaviors are imperfect proxies for OCD, regression, and restricted eating; and these models do not establish that the same mechanism operates in most human cases. (trifiletti2022identificationofultrarare pages 1-2, wilbur2019pandaspansinchildhood pages 1-1)

## Evidence assessment and authoritative interpretation

The most defensible current interpretation is that PANS is a useful **acute-onset clinical phenotype** requiring urgent, multidisciplinary evaluation. Evidence is strongest for the reproducibility of its symptom pattern, functional burden, and need for standard psychiatric and medical care. Evidence is intermediate for infection/inflammation as triggers in a subset. Evidence remains weak or inconsistent for a unitary autoimmune mechanism, commercial autoantibody panels, chronic antibiotic prophylaxis, and routine immunotherapy. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 4-5, gagliano2023pediatricacuteonsetneuropsychiatric pages 22-23, wilbur2019pandaspansinchildhood pages 1-1, wilbur2019pandaspansinchildhood pages 5-6)

Key recent sources are Gagliano et al., May 2023, DOI [10.2147/NDT.S362202](https://doi.org/10.2147/NDT.S362202), and Grandinetti et al., October 2024, DOI [10.3389/fimmu.2024.1420663](https://doi.org/10.3389/fimmu.2024.1420663). The latter is expert consensus, not a replacement for randomized evidence. Major knowledge-base fields that should remain explicitly **unknown/not established** are MONDO/OMIM/Orphanet mapping, incidence and prevalence, causal genes and variants, validated biomarker, definitive autoimmune mechanism, formal staging, survival estimates, prognostic biomarkers, and proven primary prevention. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 4-5, gagliano2023pediatricacuteonsetneuropsychiatric pages 2-4, gagliano2023pediatricacuteonsetneuropsychiatric pages 22-23)

References

1. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 4-5): Roberto Grandinetti, Nicole Mussi, Simone Pilloni, Greta Ramundo, Angela Miniaci, Emanuela Turco, Benedetta Piccolo, Maria Elena Capra, Roberta Forestiero, Serena Laudisio, Giovanni Boscarino, Laura Pedretti, Martina Menoni, Giuditta Pellino, Silvia Tagliani, Andrea Bergomi, Francesco Antodaro, Maria Cristina Cantù, Maria Teresa Bersini, Sandra Mari, Franco Mazzini, Giacomo Biasucci, Agnese Suppiej, and Susanna Esposito. Pediatric acute-onset neuropsychiatric syndrome and pediatric autoimmune neuropsychiatric disorder associated with streptococcal infections: a delphi study and consensus document about definition, diagnostic criteria, treatment and follow-up. Frontiers in Immunology, Oct 2024. URL: https://doi.org/10.3389/fimmu.2024.1420663, doi:10.3389/fimmu.2024.1420663. This article has 15 citations and is from a peer-reviewed journal.

2. (trifiletti2022identificationofultrarare pages 1-2): Rosario Trifiletti, Herbert M. Lachman, Olivia Manusama, Deyou Zheng, Alberto Spalice, Pietro Chiurazzi, Allan Schornagel, Andreea M. Serban, Rogier van Wijck, Janet L. Cunningham, Sigrid Swagemakers, and Peter J. van der Spek. Identification of ultra-rare genetic variants in pediatric acute onset neuropsychiatric syndrome (pans) by exome and whole genome sequencing. Scientific Reports, Jun 2022. URL: https://doi.org/10.1038/s41598-022-15279-3, doi:10.1038/s41598-022-15279-3. This article has 44 citations and is from a peer-reviewed journal.

3. (wilbur2019pandaspansinchildhood pages 1-1): Colin Wilbur, Ari Bitnun, Sefi Kronenberg, Ronald M Laxer, Deborah M Levy, William J Logan, Michelle Shouldice, and E Ann Yeh. Pandas/pans in childhood: controversies and evidence. Paediatrics & child health, 24 2:85-91, Dec 2019. URL: https://doi.org/10.1093/pch/pxy145, doi:10.1093/pch/pxy145. This article has 117 citations and is from a peer-reviewed journal.

4. (wilbur2019pandaspansinchildhood pages 2-3): Colin Wilbur, Ari Bitnun, Sefi Kronenberg, Ronald M Laxer, Deborah M Levy, William J Logan, Michelle Shouldice, and E Ann Yeh. Pandas/pans in childhood: controversies and evidence. Paediatrics & child health, 24 2:85-91, Dec 2019. URL: https://doi.org/10.1093/pch/pxy145, doi:10.1093/pch/pxy145. This article has 117 citations and is from a peer-reviewed journal.

5. (gagliano2023pediatricacuteonsetneuropsychiatric pages 2-4): Antonella Gagliano, Alessandra Carta, Marcello G Tanca, and Stefano Sotgiu. Pediatric acute-onset neuropsychiatric syndrome: current perspectives. Neuropsychiatric Disease and Treatment, 19:1221-1250, May 2023. URL: https://doi.org/10.2147/ndt.s362202, doi:10.2147/ndt.s362202. This article has 60 citations and is from a peer-reviewed journal.

6. (gagliano2023pediatricacuteonsetneuropsychiatric pages 1-2): Antonella Gagliano, Alessandra Carta, Marcello G Tanca, and Stefano Sotgiu. Pediatric acute-onset neuropsychiatric syndrome: current perspectives. Neuropsychiatric Disease and Treatment, 19:1221-1250, May 2023. URL: https://doi.org/10.2147/ndt.s362202, doi:10.2147/ndt.s362202. This article has 60 citations and is from a peer-reviewed journal.

7. (NCT04508530 chunk 2):  Phase III Study To Compare The Effect of Panzyga Versus Placebo in Patients With Pediatric Acute-onset Neuropsychiatric Syndrome (PANS/PANDAS). Octapharma. 2021. ClinicalTrials.gov Identifier: NCT04508530

8. (NCT02889016 chunk 1): Jennifer Frankovich. Neurobiologic, Immunologic, and Rheumatologic Markers in Youth With PANS. Stanford University. 2013. ClinicalTrials.gov Identifier: NCT02889016

9. (NCT04609761 chunk 2):  Open-label Trial of IVIG in Children With PANS. Göteborg University. 2021. ClinicalTrials.gov Identifier: NCT04609761

10. (grandinetti2024pediatricacuteonsetneuropsychiatric pages 16-16): Roberto Grandinetti, Nicole Mussi, Simone Pilloni, Greta Ramundo, Angela Miniaci, Emanuela Turco, Benedetta Piccolo, Maria Elena Capra, Roberta Forestiero, Serena Laudisio, Giovanni Boscarino, Laura Pedretti, Martina Menoni, Giuditta Pellino, Silvia Tagliani, Andrea Bergomi, Francesco Antodaro, Maria Cristina Cantù, Maria Teresa Bersini, Sandra Mari, Franco Mazzini, Giacomo Biasucci, Agnese Suppiej, and Susanna Esposito. Pediatric acute-onset neuropsychiatric syndrome and pediatric autoimmune neuropsychiatric disorder associated with streptococcal infections: a delphi study and consensus document about definition, diagnostic criteria, treatment and follow-up. Frontiers in Immunology, Oct 2024. URL: https://doi.org/10.3389/fimmu.2024.1420663, doi:10.3389/fimmu.2024.1420663. This article has 15 citations and is from a peer-reviewed journal.

11. (NCT02190292 chunk 1): Susanne Bejerot. PANS - A Detailed Study of the Patients, Their Symptoms, Biomarkers and Treatment Offered in a Scandinavian Cohort. Karolinska Institutet. 2014. ClinicalTrials.gov Identifier: NCT02190292

12. (NCT04609761 chunk 1):  Open-label Trial of IVIG in Children With PANS. Göteborg University. 2021. ClinicalTrials.gov Identifier: NCT04609761

13. (gagliano2023pediatricacuteonsetneuropsychiatric pages 22-23): Antonella Gagliano, Alessandra Carta, Marcello G Tanca, and Stefano Sotgiu. Pediatric acute-onset neuropsychiatric syndrome: current perspectives. Neuropsychiatric Disease and Treatment, 19:1221-1250, May 2023. URL: https://doi.org/10.2147/ndt.s362202, doi:10.2147/ndt.s362202. This article has 60 citations and is from a peer-reviewed journal.

14. (NCT04508530 chunk 1):  Phase III Study To Compare The Effect of Panzyga Versus Placebo in Patients With Pediatric Acute-onset Neuropsychiatric Syndrome (PANS/PANDAS). Octapharma. 2021. ClinicalTrials.gov Identifier: NCT04508530

15. (wilbur2019pandaspansinchildhood pages 4-4): Colin Wilbur, Ari Bitnun, Sefi Kronenberg, Ronald M Laxer, Deborah M Levy, William J Logan, Michelle Shouldice, and E Ann Yeh. Pandas/pans in childhood: controversies and evidence. Paediatrics & child health, 24 2:85-91, Dec 2019. URL: https://doi.org/10.1093/pch/pxy145, doi:10.1093/pch/pxy145. This article has 117 citations and is from a peer-reviewed journal.

16. (wilbur2019pandaspansinchildhood pages 5-6): Colin Wilbur, Ari Bitnun, Sefi Kronenberg, Ronald M Laxer, Deborah M Levy, William J Logan, Michelle Shouldice, and E Ann Yeh. Pandas/pans in childhood: controversies and evidence. Paediatrics & child health, 24 2:85-91, Dec 2019. URL: https://doi.org/10.1093/pch/pxy145, doi:10.1093/pch/pxy145. This article has 117 citations and is from a peer-reviewed journal.

17. (gagliano2023pediatricacuteonsetneuropsychiatric pages 18-20): Antonella Gagliano, Alessandra Carta, Marcello G Tanca, and Stefano Sotgiu. Pediatric acute-onset neuropsychiatric syndrome: current perspectives. Neuropsychiatric Disease and Treatment, 19:1221-1250, May 2023. URL: https://doi.org/10.2147/ndt.s362202, doi:10.2147/ndt.s362202. This article has 60 citations and is from a peer-reviewed journal.

18. (gagliano2023pediatricacuteonsetneuropsychiatric pages 20-22): Antonella Gagliano, Alessandra Carta, Marcello G Tanca, and Stefano Sotgiu. Pediatric acute-onset neuropsychiatric syndrome: current perspectives. Neuropsychiatric Disease and Treatment, 19:1221-1250, May 2023. URL: https://doi.org/10.2147/ndt.s362202, doi:10.2147/ndt.s362202. This article has 60 citations and is from a peer-reviewed journal.

19. (NCT01617083 chunk 2):  Antibiotic Treatment Trial for the PANDAS/PANS Phenotype. University of South Florida. 2012. ClinicalTrials.gov Identifier: NCT01617083

20. (wilbur2019pandaspansinchildhood pages 3-4): Colin Wilbur, Ari Bitnun, Sefi Kronenberg, Ronald M Laxer, Deborah M Levy, William J Logan, Michelle Shouldice, and E Ann Yeh. Pandas/pans in childhood: controversies and evidence. Paediatrics & child health, 24 2:85-91, Dec 2019. URL: https://doi.org/10.1093/pch/pxy145, doi:10.1093/pch/pxy145. This article has 117 citations and is from a peer-reviewed journal.

21. (NCT01617083 chunk 1):  Antibiotic Treatment Trial for the PANDAS/PANS Phenotype. University of South Florida. 2012. ClinicalTrials.gov Identifier: NCT01617083

22. (wilbur2019pandaspansinchildhood pages 3-3): Colin Wilbur, Ari Bitnun, Sefi Kronenberg, Ronald M Laxer, Deborah M Levy, William J Logan, Michelle Shouldice, and E Ann Yeh. Pandas/pans in childhood: controversies and evidence. Paediatrics & child health, 24 2:85-91, Dec 2019. URL: https://doi.org/10.1093/pch/pxy145, doi:10.1093/pch/pxy145. This article has 117 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Pediatric_Acute-Onset_Neuropsychiatric_Syndrome-deep-research-falcon_artifacts/artifact-00.md)