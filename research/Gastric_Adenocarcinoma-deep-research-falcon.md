---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T06:59:41.381203'
end_time: '2026-08-01T07:09:46.134360'
duration_seconds: 604.77
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Gastric Adenocarcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 43
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Gastric_Adenocarcinoma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Gastric Adenocarcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Gastric Adenocarcinoma** covering all of the
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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
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
- **Disease Name:** Gastric Adenocarcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Gastric Adenocarcinoma** covering all of the
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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


# Gastric Adenocarcinoma: Comprehensive Disease-Characteristics Report

## Executive summary

Gastric adenocarcinoma is a malignant gland-forming epithelial neoplasm of the stomach and constitutes approximately 90% of gastric cancers. It is not one disease biologically: intestinal, diffuse, and mixed histologies coexist with Epstein–Barr virus-positive (EBV+), microsatellite-instability (MSI), genomically stable (GS), and chromosomal-instability (CIN) molecular classes. Its principal preventable cause is chronic *Helicobacter pylori* infection; inherited disease is uncommon but clinically important, particularly autosomal-dominant **CDH1/CTNNA1-associated hereditary diffuse gastric cancer** (HDGC). Contemporary management is stage- and biomarker-dependent and requires HER2, MMR/MSI, PD-L1, and increasingly CLDN18.2 testing. The 2023–2024 literature emphasizes population *H. pylori* eradication, precision systemic therapy, and single-cell/spatial dissection of tumor heterogeneity. (wang2024thechinesesociety pages 7-8, lordick2024systemictherapyof pages 8-10, rivera2024seomgemcadttdclinicalguideline pages 1-2, sluis2024currentadvancesand pages 1-2)

The following table is a compact knowledge-base scaffold; the narrative below provides qualification and evidence.

| Domain | Core facts | Suggested ontology terms | Key evidence |
|---|---|---|---|
| Identity / identifiers | Gastric adenocarcinoma is the dominant histologic form of stomach cancer; ~90% of gastric cancers are adenocarcinomas. MONDO:0005036. Disease-level knowledge here is derived mainly from aggregated literature/guidelines, not individual EHRs. | MONDO:0005036; MeSH: Stomach Neoplasms / Adenocarcinoma; ICD-11 gastric carcinoma terms | (rivera2024seomgemcadttdclinicalguideline pages 1-2) |
| Histology / classification | Lauren types: intestinal, diffuse, mixed. Early gastric cancer is limited to mucosa/submucosa; advanced disease invades muscularis propria or deeper. WHO/Lauren classification remains standard pathology framework. | NCIT gastric adenocarcinoma; HPO: gastric adenocarcinoma; UBERON: stomach | (wang2024thechinesesociety pages 7-8) |
| Molecular classes | TCGA framework: EBV-positive, MSI, genomically stable (GS), chromosomal instability (CIN). EBV/MSI enrich for immune sensitivity; GS often overlaps diffuse-type biology; CIN often associates with RTK amplifications. | NCIT: Epstein-Barr virus positive tumor; MSI-high; chromosomal instability | (OpenTargets Search: gastric adenocarcinoma, lordick2024systemictherapyof pages 8-10) |
| Major etiologies / risks | Major causes/risk factors: Helicobacter pylori, smoking, high-salt/processed meat diets, low fruit/vegetable intake, atrophic gastritis, autoimmune gastritis; obesity/GERD more relevant for proximal/GEJ disease; EBV contributes in a subset. | CHEBI: sodium chloride; NCBITaxon: Helicobacter pylori; HPO: chronic gastritis, intestinal metaplasia | (rivera2024seomgemcadttdclinicalguideline pages 1-2, leja2024wherearewe pages 3-4) |
| Protective / preventive factors | H. pylori eradication lowers gastric cancer incidence; benefit is greatest before advanced precancerous lesions but may still extend later in life. Population “screen-and-treat” is the leading prevention strategy in many regions. | NCIT: Helicobacter pylori eradication therapy; preventive screening | (leja2024wherearewe pages 6-6, leja2024wherearewe pages 3-3) |
| Germline genes | Hereditary diffuse gastric cancer is chiefly due to CDH1 and less often CTNNA1; autosomal dominant. CDH1 loss usually needs a second hit, commonly promoter hypermethylation. APC underlies GAPPS, a distinct hereditary gastric neoplasia syndrome. | HGNC: CDH1, CTNNA1, APC; MONDO hereditary diffuse gastric adenocarcinoma | (sluis2024currentadvancesand pages 1-2, lim2023currentadvancesin pages 2-4, pereira2025hereditarydiffusegastric pages 2-4, OpenTargets Search: gastric adenocarcinoma) |
| Major somatic drivers | Recurrently implicated genes/pathways include TP53, ARID1A, KRAS, RHOA, PIK3CA, RNF43, KMT2D, SMAD4, ERBB2 and angiogenic signaling via KDR/VEGFR2. HER2 amplification is a key actionable alteration; RHOA is enriched in diffuse/GS disease. | HGNC: TP53, ARID1A, KRAS, RHOA, PIK3CA, ERBB2, RNF43, KMT2D, SMAD4, KDR | (OpenTargets Search: gastric adenocarcinoma, lordick2024systemictherapyof pages 8-10) |
| Mechanisms / pathways | Carcinogenesis reflects interaction of microbial inflammation, epithelial injury, stem/progenitor DNA damage, Wnt/MAPK/PI3K signaling, EMT/invasion, and immune evasion. In HDGC, E-cadherin loss disrupts adhesion and spindle orientation; in experimental systems H. pylori plus Apc loss augments DNA damage in gastric stem/progenitor cells. | GO: cell adhesion, Wnt signaling, MAPK cascade, PI3K-AKT signaling, epithelial to mesenchymal transition; CL: gastric epithelial cell, macrophage, CD8-positive T cell | (sluis2024currentadvancesand pages 1-2, lim2023currentadvancesin pages 2-4, deng2023singlecelltranscriptomesequencing pages 4-5) |
| Clinical phenotypes | Common manifestations include dyspepsia, weight loss, early satiety, abdominal pain, iron-deficiency anemia, bleeding, obstruction, and metastatic symptoms. Diffuse/signet-ring cancers may infiltrate the wall with less obvious gland formation. | HPO: Abdominal pain, Early satiety, Weight loss, Iron deficiency anemia, Gastrointestinal hemorrhage, Gastric outlet obstruction | (wang2024thechinesesociety pages 7-8, rivera2024seomgemcadttdclinicalguideline pages 1-2) |
| Anatomy affected | Primary organ: stomach, especially mucosa/glandular epithelium; proximal/GEJ and distal/antral patterns differ epidemiologically. Common secondary sites include lymph nodes, peritoneum, liver, lung, and ovary/adnexa; peritoneal spread is a major complication. | UBERON: stomach, gastric mucosa, lymph node, liver, peritoneum, lung; CL: gastric epithelial cell | (rivera2024seomgemcadttdclinicalguideline pages 1-2) |
| Diagnostics / biomarkers | Diagnostic gold standard: upper endoscopy with biopsy reviewed by experienced pathology; multiple biopsies improve accuracy. Staging uses CT chest/abdomen/pelvis; EUS refines depth/nodes; laparoscopy with peritoneal lavage detects occult peritoneal disease. Core biomarkers: HER2, MMR/MSI, PD-L1 CPS, CLDN18.2; NGS and liquid biopsy are emerging/investigational in guidelines. | NCIT: Endoscopy, Biopsy, Endoscopic ultrasonography, Computed tomography, Diagnostic laparoscopy; HGNC/biomarkers: ERBB2, PD-L1(CD274), CLDN18, MMR genes | (wang2024thechinesesociety pages 4-5, rivera2024seomgemcadttdclinicalguideline pages 1-2, gullo2020precancerouslesionsof pages 6-8) |
| Treatment by stage / biomarker | Very early disease: EMR/ESD in selected superficial lesions. Resectable locally advanced disease: gastrectomy plus perioperative chemotherapy (FLOT in many Western settings) or adjuvant strategies in East Asia. Metastatic disease: fluoropyrimidine-platinum backbone, adding trastuzumab for HER2+, pembrolizumab/nivolumab-based therapy by PD-L1 or MSI status, and zolbetuximab for CLDN18.2+ HER2-negative disease; anti-VEGFR2 strategies are standard in later lines in many regions. | NCIT: Gastrectomy, Endoscopic mucosal resection, Endoscopic submucosal dissection, FLOT regimen, Trastuzumab, Pembrolizumab, Nivolumab, Zolbetuximab, Ramucirumab | (lordick2024systemictherapyof pages 8-10, wang2024thechinesesociety pages 4-5, rivera2024seomgemcadttdclinicalguideline pages 1-2) |
| Prevention / screening | East Asian programs support endoscopic screening; Korea screens adults ≥40 every 2 years and Japan uses endoscopy from age 50. China’s county-level endoscopic program was associated with a 15% mortality decrease. In Europe, organized population H. pylori screen-and-treat is the main currently supportable strategy, while direct endoscopic screening evidence remains less mature. | NCIT: Mass screening, Endoscopy, Helicobacter pylori test-and-treat | (mok2024racialdisparitiesof pages 7-8, leja2024wherearewe pages 6-6, mok2024racialdisparitiesof pages 5-7, leja2024wherearewe pages 6-7) |
| Prognosis | Prognosis depends strongly on stage, TNM class, age, surgery, and treatment response. Advanced/metastatic gastric cancer still has poor median survival, often <12 months with conventional chemotherapy alone, though biomarker-guided immunotherapy/targeted therapy has improved outcomes. In high-risk Chinese older cohorts, 3-year OS declined from 58.5% to 34.4% across 2010-2019, underscoring ongoing mortality burden. | HPO: reduced survival; NCIT: overall survival, progression-free survival | (burz2024prognosisandtreatment pages 2-4, lordick2024systemictherapyof pages 8-10) |
| Epidemiology | Gastric cancer burden is geographically concentrated in East Asia and is higher in males and older adults. In Asia (GLOBOCAN 2020), ASIR was 14.3/100,000 overall, 20.4 in males and 8.7 in females; ASMR was 10.0 overall. | NCIT: incidence, mortality; demographic descriptors | (mok2024racialdisparitiesof pages 7-8, leja2024wherearewe pages 6-6) |
| Model systems | Key translational models include patient-derived organoids, gastric organoid infection systems, PDX models, and genetically engineered mouse/organoid HDGC models. Single-cell/spatial studies profile epithelial, fibroblast, macrophage, B-cell, neutrophil, and CD8 T-cell states; experimentally supported axes include IL1B-IL1R2, CXCL5-CXCR2, and CCL28-CCR10. Main limitations: partial loss of native microenvironment, biomarker heterogeneity, and incomplete capture of long-term evolution. | NCIT: Patient-derived xenograft model, Organoid, Single-cell RNA sequencing, Spatial transcriptomics; CL: macrophage, fibroblast, B cell, neutrophil, CD8-positive T cell | (xu2024singlecellrnasequencing pages 9-11, liang2024theburgeoningspatial pages 19-20, deng2023singlecelltranscriptomesequencing pages 4-5) |


*Table: This compact table summarizes the core disease-knowledge domains for gastric adenocarcinoma, including classification, etiology, genetics, clinical features, diagnostics, treatment, prevention, prognosis, and models. It is designed as a concise scaffold for populating a disease knowledge base with ontology suggestions and evidence anchors.*

## 1. Disease information

**Definition and category.** Gastric adenocarcinoma is a primary malignant epithelial tumor showing glandular differentiation arising in gastric mucosa. It belongs to digestive-system malignancies and epithelial adenocarcinomas. “Gastric cancer” is broader and also includes lymphoma, gastrointestinal stromal tumor, neuroendocrine neoplasm, and rarer nonepithelial tumors; therefore, the terms should not be treated as perfectly synonymous.

**Identifiers and synonyms.** Recommended identifier: **MONDO:0005036**. Useful mappings include MeSH **Stomach Neoplasms** plus **Adenocarcinoma**; ICD-10-CM **C16.0–C16.9**, coded by gastric site; and ICD-11 malignant neoplasm of stomach categories. Synonyms include *gastric adenocarcinoma*, *stomach adenocarcinoma*, *gastric carcinoma, adenocarcinoma type*, and TCGA shorthand **STAD**. More specific MONDO entities include gastric intestinal-type adenocarcinoma, signet-ring-cell gastric adenocarcinoma, and hereditary diffuse gastric adenocarcinoma. Open Targets recognizes MONDO:0005036 and connects it to CDH1, ERBB2, TP53, KDR, ARID1A, KRAS, RHOA, CTNNA1, PIK3CA, RNF43, KMT2D, and SMAD4. (OpenTargets Search: gastric adenocarcinoma)

**Classification.** Lauren classification separates intestinal tumors—atypical gland formation often arising through atrophy and intestinal metaplasia—from diffuse tumors composed of poorly cohesive infiltrating cells, sometimes signet-ring cells, and mixed tumors. “Early gastric cancer” is confined to mucosa or submucosa irrespective of nodes; advanced cancer invades muscularis propria or deeper. Reporting follows WHO histology and AJCC/UICC TNM, eighth edition. (wang2024thechinesesociety pages 7-8)

**Data provenance.** This report represents aggregated disease-level evidence from publications, guidelines, registries, ClinicalTrials.gov, and Open Targets. It is not an extraction from individual EHRs. Some cited studies do analyze patient-level biopsies or trial participants, but only published aggregate findings are presented.

## 2. Etiology, risks, protection, and gene–environment interaction

### Causal and environmental factors

*H. pylori* is the dominant cause of non-cardia intestinal-type disease. The causal chain is chronic infection → active gastritis → multifocal atrophy → intestinal metaplasia → dysplasia → invasive adenocarcinoma, with bacterial virulence factors, host inflammation, diet, and smoking modifying progression. A 2024 European review states that close to 90% of non-cardia cases are related to *H. pylori*. Other established or probable factors include tobacco smoking, high salt and salt-preserved foods, processed meat, low fruit/vegetable intake, older age, male sex, family history, gastric atrophy, pernicious anemia/autoimmune gastritis, prior gastric surgery, and some occupational or socioeconomic exposures. Obesity and gastroesophageal reflux are more strongly linked to cardia/GEJ adenocarcinoma. EBV is a tumor-associated infectious agent in a minority of cancers, rather than a transmissible cancer. (rivera2024seomgemcadttdclinicalguideline pages 1-2, leja2024wherearewe pages 6-6, leja2024wherearewe pages 3-4)

Autoimmune atrophic gastritis damages oxyntic mucosa and creates achlorhydria, hypergastrinemia, iron/B12 deficiency, metaplasia, and increased gastric malignancy risk. Alcohol associations are less consistent than those for smoking, salt, and *H. pylori* and may vary by tumor site.

### Genetic susceptibility

Most cases are sporadic and multifactorial. Approximately 10% show familial clustering, while recognized high-penetrance hereditary syndromes account for roughly 1–3%. Important syndromes include HDGC (**CDH1**, **CTNNA1**), Lynch syndrome (MMR genes), familial adenomatous polyposis and gastric adenocarcinoma and proximal polyposis of the stomach (**APC** promoter 1B variants), Peutz–Jeghers syndrome (**STK11**), juvenile polyposis (**SMAD4/BMPR1A**), and Li–Fraumeni syndrome (**TP53**). Open Targets separately associates APC with GAPPS. (OpenTargets Search: gastric adenocarcinoma, lim2023currentadvancesin pages 1-2)

### Protective factors

The strongest intervention-level protective evidence is eradication of *H. pylori*, preferably before extensive atrophy/metaplasia develops. Smoking cessation, reduced salt-preserved/processed food intake, healthy weight, and diets rich in fresh produce are reasonable risk-reduction measures, although their evidence is less intervention-specific than eradication. No approved vaccine prevents *H. pylori* or gastric cancer. (leja2024wherearewe pages 6-6, leja2024wherearewe pages 3-4, leja2024wherearewe pages 3-3)

### Gene–environment interaction

Inherited or polygenic susceptibility can amplify microbial injury. CDH1 deficiency lowers epithelial cohesion; inflammatory and epigenetic second hits can then promote invasion. Experimentally, *H. pylori* causes transcription-dependent DNA damage and replication stress in LGR5-positive antral and Troy-positive corpus stem/progenitor cells; **Apc** inactivation and constitutive Wnt-driven hyperproliferation aggravate this injury, whereas Trp53 or Smad4 loss did not do so in that model. This is mechanistic mouse-organoid evidence, not proof of an identical quantitative effect in humans.

## 3. Phenotypes and quality-of-life effects

Onset is usually insidious in later adulthood; early disease is often asymptomatic. Frequencies vary strongly by stage and population, so universal percentages are inappropriate.

* **Dyspepsia/epigastric pain**—variable, often mild initially and progressive; suggested HPO **Abdominal pain (HP:0002027)** and dyspepsia term where available.
* **Early satiety, postprandial fullness, nausea/vomiting**—especially with reduced gastric compliance or outlet disease; suggested HPO **Early satiety**, **Nausea (HP:0002018)**, **Vomiting (HP:0002013)**.
* **Unintentional weight loss, anorexia, fatigue/cachexia**—common in advanced disease and major determinants of function; suggested **Weight loss (HP:0001824)**, **Feeding difficulties**, **Fatigue (HP:0012378)**.
* **Occult/overt bleeding and iron-deficiency anemia**—laboratory and clinical phenotypes; suggested **Gastrointestinal hemorrhage (HP:0002239)**, **Iron deficiency anemia (HP:0001891)**.
* **Dysphagia**—particularly cardia/GEJ lesions; suggested **Dysphagia (HP:0002015)**.
* **Gastric outlet obstruction**—late local complication with vomiting/dehydration; suggested HPO gastric outlet obstruction.
* **Metastatic manifestations**—ascites/peritoneal carcinomatosis, hepatomegaly or liver dysfunction, pleural symptoms, nodal disease, and ovarian Krukenberg metastasis. Diffuse cancers often seed the peritoneum.

Cancer symptoms, gastrectomy, chemotherapy toxicity, nutritional deficiencies, altered body image, fear of recurrence, and financial stress impair physical, emotional, and social quality of life. After total gastrectomy, lifelong small frequent meals, weight loss, dumping, reflux, anemia, and B12 replacement may be required. Guidelines consequently support multidisciplinary nutrition, psycho-oncology, symptom control, and palliative care. (burz2024prognosisandtreatment pages 2-4, rivera2024seomgemcadttdclinicalguideline pages 1-2)

## 4. Genetic and molecular information

### Germline disease

**CDH1** encodes E-cadherin and **CTNNA1** encodes α-catenin; both are components of adherens junctions. HDGC is autosomal dominant with incomplete, family-dependent, age-dependent penetrance. Pathogenic CDH1 variants include nonsense, frameshift, splice-site, and deletions; truncating variants are generally easier to classify than missense variants, which often remain VUS without functional/segregation evidence. The second somatic hit is frequently CDH1 promoter hypermethylation (reported in 32.1% of lesions in one synthesis), followed by loss of heterozygosity (25%) or somatic mutation. CTNNA1 accounts for fewer than 2% of HDGC families and appears lower penetrance. (sluis2024currentadvancesand pages 1-2, lim2023currentadvancesin pages 2-4)

Penetrance estimates have changed with ascertainment. Older selected-family estimates were approximately 42% in men and 33% in women, whereas a 2024 review incorporating less selected families estimated lifetime advanced diffuse-gastric-cancer risk at 13–19%. These values are not contradictory measurements of one population; they demonstrate ascertainment and variant-specific uncertainty. Lobular breast-cancer risk is also elevated in female CDH1 carriers. (sluis2024currentadvancesand pages 1-2, gullo2020precancerouslesionsof pages 14-15)

Pathogenic germline alleles are rare in population databases; a true high-penetrance pathogenic variant is generally expected to be absent or extremely rare in gnomAD. Variant classification must use ClinVar/ClinGen expert curation and ACMG/AMP criteria rather than frequency alone. Genetic anticipation and repeat expansions are not characteristic. Founder variants exist in some families/populations, but no single global carrier frequency applies.

### Somatic alterations and chromosomal abnormalities

Prominent alterations include loss-of-function **TP53**, **ARID1A**, **RNF43**, **SMAD4**, and chromatin-regulator mutations; activating or amplifying events in **ERBB2/HER2**, **KRAS**, **PIK3CA**, **MET**, **FGFR2**, and angiogenic pathways; and **RHOA** mutation or CLDN18–ARHGAP fusions in diffuse/GS cancers. CIN tumors show aneuploidy and focal receptor-tyrosine-kinase amplification; MSI tumors accumulate frameshift mutations because of MMR deficiency; EBV+ tumors often show PIK3CA mutation, immune signaling, and extensive promoter methylation. Open Targets provides integrated human genetic, somatic, and therapeutic evidence for the principal targets. (OpenTargets Search: gastric adenocarcinoma)

Approximate actionable frequencies vary by assay, geography, and stage: HER2 5–25%; MSI-H/dMMR 8–25% overall but lower in metastatic cohorts; FGFR1/3 amplification ~2%; homologous-recombination-deficiency signatures 7–12%; KRAS G12C ~1%; MET amplification 2–11%; and PIK3CA alteration ~3.5% in one contemporary summary. These are cohort estimates, not universal prevalence. (lordick2024systemictherapyof pages 8-10, rivera2024seomgemcadttdclinicalguideline pages 1-2)

### Epigenetics and modifiers

Key epigenetic events include CpG-island methylation induced by chronic inflammation, CDH1 promoter methylation, MLH1 methylation in sporadic MSI cancer, and EBV-associated hypermethylation. ARID1A/KMT2D disruption remodels chromatin. Putative modifier effects from inflammatory, detoxification, and DNA-repair polymorphisms have been reported, but few are clinically actionable.

## 5. Environmental and infectious information

Relevant non-genetic exposures comprise *H. pylori*; smoking; high dietary sodium/nitrosated or preserved food; low produce intake; obesity/GERD for proximal tumors; chronic gastric inflammation; and healthcare disparities that delay detection. Ionizing radiation is not a dominant population cause, although prior radiotherapy can rarely contribute. *H. pylori* is NCBI Taxonomy **210**; EBV/human gammaherpesvirus 4 is NCBI Taxonomy **10376**. Neither gastric adenocarcinoma nor its EBV-associated subtype is contagious or zoonotic.

## 6. Mechanism and pathophysiology

### Causal chains

1. **Intestinal pathway:** *H. pylori* and diet/smoking → epithelial injury and NF-κB/cytokine inflammation → atrophy/hypochlorhydria → intestinal metaplasia/dysplasia → TP53/CIN or MSI evolution → invasion and metastasis.
2. **Diffuse/HDGC pathway:** germline plus somatic loss of CDH1/CTNNA1 → defective adherens junctions, polarity, spindle orientation, and anoikis control → microscopic signet-ring foci → additional Wnt/Notch/RHOA and stromal changes → infiltrative linitis-plastica-like cancer. Tiny pT1a signet-ring foci occur in most prophylactic gastrectomies, but which foci progress is unpredictable. (sluis2024currentadvancesand pages 1-2, lim2023currentadvancesin pages 2-4, gullo2020precancerouslesionsof pages 15-17)
3. **EBV pathway:** latent viral infection → epigenetic reprogramming and immune-checkpoint-rich microenvironment → EBV+ adenocarcinoma.
4. **Metastatic pathway:** EMT-like programs, extracellular-matrix remodeling, angiogenesis through VEGF–VEGFR2, immune escape, and peritoneal survival promote dissemination.

Suggested GO terms include cell–cell adhesion (**GO:0098609**), canonical Wnt signaling (**GO:0060070**), MAPK cascade (**GO:0000165**), PI3K signaling, inflammatory response (**GO:0006954**), DNA-damage response (**GO:0006974**), angiogenesis (**GO:0001525**), EMT (**GO:0001837**), apoptosis, and immune-response regulation. Relevant CL concepts include gastric epithelial cell, mucous neck/foveolar cell, chief cell, parietal cell, LGR5+ epithelial stem cell, fibroblast, endothelial cell, macrophage, neutrophil, B/plasma cell, and CD8+ T cell.

### Molecular profiling and advanced technologies

Single-cell and spatial work demonstrates that bulk “gastric cancer” averages over malignant epithelial states, fibroblasts/myofibroblasts, endothelial cells, macrophages, neutrophils, B/plasma cells, and heterogeneous T cells. Approximately 200,000 cells from 48 samples in 31 patients were combined with spatial profiling of 156 regions in one landmark program; another 2023 analysis integrated spatial transcriptomics, metabolomics, and lipidomics from seven male patients. (liang2024theburgeoningspatial pages 19-20)

Recent findings include protumor neutrophil recruitment through **CXCL5–CXCR2**, CD8 exhaustion associated with **LAG3**, chemotherapy-associated expansion of fibroblast/myofibroblast states, tumor–macrophage **IL1B–IL1R2** signaling, and strong immune sensitivity in some MSI-H tumors with high TMB, diverse TCR repertoires, and abundant T-cell infiltration. A gastric-cancer cell/B-cell analysis implicated **CCL28–CCR10** recruitment of IgA plasma cells. These findings are promising biological hypotheses, but most are not yet validated clinical tests. (xu2024singlecellrnasequencing pages 9-11, deng2023singlecelltranscriptomesequencing pages 4-5, xu2024singlecellrnasequencing pages 13-14)

**Direct abstract-level conclusion:** a 2024 single-cell review states that scRNA-seq provides “unprecedented insights into the complicated biological composition and characteristics of TME,” while spatial transcriptomics captures local communication networks. (Publication: September 2024; https://doi.org/10.1007/s00262-024-03820-4.) (xu2024singlecellrnasequencing pages 9-11)

## 7. Anatomical structures affected

The primary site is the stomach—cardia, fundus, body, antrum, pylorus, lesser/greater curvature, or overlapping/unspecified sites—with origin in glandular mucosal epithelium. Suggested anatomy terms are UBERON **stomach**, gastric mucosa, gastric gland, cardia, fundus, body, antrum, and pylorus. Disease is not lateralized.

Local progression crosses submucosa, muscularis propria, subserosa, and serosa and may invade esophagus, duodenum, pancreas, spleen, colon, or abdominal wall. Secondary sites include perigastric and distant lymph nodes, peritoneum/omentum, liver, lung, bone, and ovaries. Subcellular compartments implicated include plasma-membrane adherens/tight junctions, nucleus/chromatin, mitochondria, ER, and extracellular matrix.

## 8. Temporal development

Onset is generally adult/geriatric, chronic, and insidious; young-onset cases are enriched for diffuse histology and hereditary evaluation. The Correa sequence may evolve over years to decades. TNM stage I–IV is the principal clinical course framework. Progression is variable but untreated invasive disease is progressive, with lymphatic, hematogenous, or transcoelomic spread.

The critical intervention windows are: eradicate *H. pylori* before advanced atrophy; detect and endoscopically remove eligible intramucosal lesions; undertake curative gastrectomy before metastatic spread; and identify actionable biomarkers before systemic therapy. Remission is treatment-induced rather than reliably spontaneous. Recurrence after curative-intent therapy is most often locoregional, peritoneal, or distant and generally occurs in the first several years, although late relapse is possible.

## 9. Inheritance and population epidemiology

HDGC is autosomal dominant with variable expressivity and incomplete, age-dependent penetrance. Germline mosaicism is not a common defining feature; consanguinity has no special role in this dominant syndrome. Cascade testing is appropriate after a pathogenic familial variant is identified. (sluis2024currentadvancesand pages 1-2, gullo2020precancerouslesionsof pages 14-15)

Population burden is highest in East Asia, parts of Eastern Europe, and Latin America; incidence rises steeply with age and is approximately twice as high in men in many populations. Asian GLOBOCAN 2020 estimates were an age-standardized incidence rate of 14.3/100,000 overall—20.4 in men and 8.7 in women—and mortality of 10.0/100,000 overall. Disease burden peaks after age 70. In a very-high-risk Chinese older population, incidence declined from 439.65 to 330.40 per 100,000 during 2010–2019, but hospital-cohort three-year OS declined from 58.5% to 34.4%, illustrating that regional registry estimates should not be generalized globally.

## 10. Diagnostics

**Standard work-up.** Upper endoscopy with multiple biopsies and expert WHO-based histopathology is the diagnostic gold standard; multiple samples can raise accuracy from about 70% to 98%. CT chest/abdomen/pelvis stages distant disease; EUS improves depth and regional-node assessment; MRI or FDG-PET/CT is selective. Diagnostic laparoscopy with washings is recommended for potentially resectable stage IB–III or cT3–4 disease at meaningful risk of occult peritoneal spread. Positive cytology is metastatic disease in major staging systems. (wang2024thechinesesociety pages 4-5, rivera2024seomgemcadttdclinicalguideline pages 1-2)

Pathology should report histotype, grade, Lauren type, depth, margins, lymphovascular/perineural invasion, regression after neoadjuvant therapy, and nodes—at least 16, preferably more than 30 for robust staging. (wang2024thechinesesociety pages 7-8)

**Biomarkers.** Test advanced disease for:

* **HER2/ERBB2:** IHC followed by ISH for equivocal cases; obtain adequate tissue because expression is heterogeneous.
* **MMR/MSI:** MLH1, PMS2, MSH2, MSH6 IHC and/or PCR/NGS.
* **PD-L1:** combined positive score, assay- and jurisdiction-specific thresholds.
* **CLDN18.2:** validated IHC for zolbetuximab eligibility.
* Consider EBV-encoded RNA ISH, broad NGS, NTRK fusion, TMB, MET/FGFR2, and ctDNA in selected advanced cases/trials.

HER2 occurs in roughly 5–25% and MSI-H/dMMR in 8–25%, but prevalence depends on site, histology, ancestry, and stage. In a 536-patient advanced cohort, CLDN18.2 positivity was 57.6% at a ≥40% 2+ cutoff and 48.9% at a ≥70% cutoff; co-expression with PD-L1 was much less common. (lordick2024systemictherapyof pages 8-10, rivera2024seomgemcadttdclinicalguideline pages 1-2)

Routine serum CEA, CA19-9, and CA72-4 lack sufficient sensitivity/specificity for diagnosis or population screening, though trends may aid monitoring. ctDNA, extracellular-vesicle, proteomic, metabolomic, and AI-radiomic assays remain adjunctive or investigational. Guidelines explicitly describe NGS and liquid biopsy as emerging rather than replacements for tissue diagnosis. (wang2024thechinesesociety pages 4-5)

**Genetic testing.** Refer for counseling when HDGC criteria, young diffuse cancer, bilateral/familial lobular breast cancer, Lynch-compatible MSI, polyposis, or a strong family history is present. Start with a germline hereditary gastric-cancer panel including **CDH1, CTNNA1**, MMR genes, **APC, STK11, SMAD4, BMPR1A, TP53** and other phenotype-directed genes; deletion/duplication analysis is essential. WES/WGS may help unresolved families but can increase VUS burden. CMA, karyotype, mitochondrial testing, and repeat-expansion testing are not routine diagnostic tests for gastric adenocarcinoma.

**Differential diagnosis.** Exclude gastric lymphoma, GIST, neuroendocrine neoplasm, metastatic breast/lung/melanoma, pancreaticobiliary invasion, benign ulcer, gastritis, and signet-ring mimics. In HDGC biopsies, globoid/vacuolated cells, xanthomatous cells, and autolysis can mimic signet-ring carcinoma. (gullo2020precancerouslesionsof pages 15-17)

## 11. Outcome and prognosis

Stage is the dominant predictor. Early mucosal cancers treated completely can have excellent long-term survival; metastatic disease remains usually incurable. Poor prognostic features include advanced T/N/M stage, peritoneal metastasis, poor performance status, malnutrition, diffuse/signet-ring phenotype in relevant settings, lymphovascular/perineural invasion, incomplete resection, and treatment resistance. MSI-H and EBV+ biology may predict immunotherapy sensitivity, while biomarker expression can vary spatially and over time.

Advanced gastric cancer historically had median survival under 12 months with conventional chemotherapy; HER2-, PD-1/PD-L1-, VEGFR2-, and CLDN18.2-directed therapies have incrementally improved outcomes in selected groups. Survivorship morbidity includes malnutrition, sarcopenia, dumping, B12/iron deficiency, neuropathy, fatigue, anxiety, and impaired social function. (burz2024prognosisandtreatment pages 2-4, lordick2024systemictherapyof pages 8-10)

## 12. Treatment

### Localized disease

* **Very early eligible lesions:** endoscopic mucosal resection or endoscopic submucosal dissection with en-bloc negative margins (**NCIT: Endoscopic Mucosal Resection; Endoscopic Submucosal Dissection**).
* **Resectable invasive disease:** subtotal or total gastrectomy with appropriate lymphadenectomy, usually D2 in experienced centers (**NCIT: Gastrectomy; Lymphadenectomy**).
* **Western practice:** perioperative FLOT—5-FU, leucovorin, oxaliplatin, docetaxel—for fit locally advanced patients.
* **East Asian practice:** surgery followed by S-1 or platinum–fluoropyrimidine regimens is common after D2 resection.
* **Chemoradiation:** principally for selected GEJ disease, positive margins, or inadequate nodal surgery rather than universally after optimal D2 surgery.

A 2024 guideline abstract summarizes the current standard directly: “Endoscopic resection in very early stage, perioperative chemotherapy in locally advanced tumors” with biomarker profiling in metastatic disease. (Publication: July 2024; https://doi.org/10.1007/s12094-024-03600-7.) (rivera2024seomgemcadttdclinicalguideline pages 1-2)

### Unresectable/metastatic disease

A fluoropyrimidine–platinum doublet is the backbone. Add treatment according to biomarkers and jurisdiction:

* **HER2-positive:** trastuzumab plus chemotherapy; pembrolizumab is added in eligible PD-L1-positive first-line disease. Trastuzumab deruxtecan is an important later-line antibody–drug conjugate after trastuzumab exposure.
* **HER2-negative, PD-L1-positive or MSI-H/dMMR:** nivolumab or pembrolizumab plus chemotherapy; MSI-H tumors are particularly immunotherapy-sensitive.
* **CLDN18.2-positive, HER2-negative:** zolbetuximab plus an oxaliplatin/fluoropyrimidine regimen. Zolbetuximab binds exposed CLDN18.2 and induces antibody- and complement-dependent cytotoxicity.
* **Second line:** paclitaxel plus ramucirumab or alternatives; irinotecan/taxanes as appropriate.
* **Later line:** trifluridine/tipiracil, trastuzumab deruxtecan for HER2 disease, checkpoint blockade in qualifying biomarker groups, or trial enrollment.

Current guidance therefore treats HER2, PD-L1 CPS, MSI/MMR, and CLDN18.2 as mandatory decision variables rather than merely prognostic assays. (lordick2024systemictherapyof pages 8-10, wang2024thechinesesociety pages 4-5)

Toxicities include cytopenias, neuropathy, mucositis/diarrhea, nausea, cardiotoxicity with HER2-directed agents, immune-related events with checkpoint blockade, hypertension/proteinuria/bleeding with antiangiogenic therapy, interstitial lung disease with trastuzumab deruxtecan, and prominent nausea/vomiting with zolbetuximab. No CPIC gastric-cancer-specific genotype-guided regimen is standard; DPYD and UGT1A1 testing may inform fluoropyrimidine or irinotecan safety according to regional pharmacogenomic practice.

### Supportive, rehabilitative, and experimental treatment

Nutrition assessment, enteral support when feasible, B12 after total gastrectomy, iron/folate replacement, antiemetics, analgesia, management of obstruction/bleeding/ascites, exercise rehabilitation, and early palliative care are integral. Gene therapy and RNA therapy are not established. CLDN18.2 CAR-T is experimental; one 2024 report described a target-lesion complete response and an eight-month overall partial response after CT041 in a patient refractory to four lines, with ctDNA decline and no severe toxicity—important proof of concept, not population-level efficacy.

Representative recruiting or planned studies identified in ClinicalTrials.gov include perioperative FLOT versus adjuvant XELOX (**NCT05264896**), cadonilimab plus nab-paclitaxel after PD-(L)1 resistance (**NCT06118645**), sentinel-node magnetic mapping (**NCT05038098**), and a phase III CLDN18.2-directed antibody/PD-1/chemotherapy program (**NCT07584135**). Registry status and identifiers should be rechecked before reuse because trial records change.

## 13. Prevention

**Primary prevention:** detect and eradicate *H. pylori*; confirm cure; reduce tobacco and high-salt/preserved-food exposure; support healthy weight and diet. There is no licensed prophylactic *H. pylori* vaccine. Eradication is most effective before advanced precancerous lesions but also prevents ulcer disease, MALT lymphoma, iron deficiency, and B12 deficiency. (leja2024wherearewe pages 3-4)

**Secondary prevention:** Japan uses endoscopic screening from age 50; Korea offers endoscopy or upper-GI series every two years from age 40, although endoscopy is superior. Reported sensitivity and detection were 69.0% and 2.61/1,000 for endoscopy versus 36.7% and 0.68/1,000 for radiographic series. A Chinese program across 110 counties was associated with a 15% reduction in gastric-cancer mortality. (mok2024racialdisparitiesof pages 7-8, mok2024racialdisparitiesof pages 5-7)

Europe had no organized gastric-cancer screening program as of 2024; expert analysis judged population *H. pylori* “screen and treat” the most supportable strategy in intermediate/high-incidence regions while EUROHELICAN, TOGAS, GISTAR, and EUCanScreen generate implementation evidence. General-population endoscopy is not cost-effective in the United States, but risk-targeted screening may be reasonable for immigrants from high-incidence regions, high-risk racial/ethnic groups, premalignant gastric conditions, and first-degree family history. (leja2024wherearewe pages 6-6, leja2024wherearewe pages 6-7, mok2024racialdisparitiesof pages 8-9)

**Hereditary prevention:** offer genetic counseling, cascade testing, and management in expert centers. Risk-reducing total gastrectomy remains the most definitive intervention for appropriate pathogenic CDH1 carriers; expert endoscopic surveillance is an alternative for selected carriers who defer surgery, recognizing imperfect sensitivity. Female CDH1 carriers require lobular-breast-cancer surveillance. (sluis2024currentadvancesand pages 1-2, gullo2020precancerouslesionsof pages 15-17)

**Tertiary prevention:** postoperative surveillance, nutritional replacement, smoking cessation, rehabilitation, treatment of *H. pylori*, and prompt management of recurrence and treatment complications.

## 14. Other species and natural disease

Naturally occurring gastric adenocarcinoma occurs in dogs (**NCBI Taxon 9615**), cats (**9685**), and occasionally other mammals, but is uncommon relative to human disease. Certain dog breeds have reported predisposition, making canine gastric carcinoma a potential comparative-oncology resource; robust VBO mappings and universally accepted breed-specific penetrance estimates are not available from the evidence assembled here. Comparative pathology may reproduce glandular, diffuse/signet-ring, invasive, and metastatic features, while species differences in incidence, anatomy, microbiota, exposures, and driver spectra limit direct translation.

Orthologues of **CDH1, CTNNA1, APC, TP53, ERBB2, ARID1A**, and **RHOA** are conserved in mouse, dog, zebrafish, and other vertebrates. Gastric adenocarcinoma itself is neither zoonotic nor transmissible; *Helicobacter* species can cross host boundaries in selected settings, but human gastric cancer is not acquired from an animal tumor.

## 15. Model organisms and experimental systems

* **Cell lines/2D culture:** scalable for signaling and drug screens, but lose architecture and clonal/TME complexity.
* **Patient-derived organoids:** preserve epithelial genetics and three-dimensional organization and enable drug testing, CRISPR editing, and *H. pylori* microinjection. They incompletely retain immune, vascular, neural, microbial, and stromal components.
* **Genetically engineered organoids:** CDH1 knockout models reproduce disrupted organization/spindle dynamics; Apc-deficient infected organoids demonstrate Wnt–*H. pylori* synergy.
* **Mouse models:** chemical carcinogenesis, *Helicobacter felis/pylori* infection, conditional **Cdh1, Apc, Trp53, Smad4** alteration, and transgenic oncogene systems investigate initiation and progression. No single mouse model reproduces human latency, histologic diversity, immune ecology, and metastasis.
* **Patient-derived xenografts:** retain major tumor architecture/genomics and support drug testing but select for engrafting clones, replace human stroma over time, and usually require immunodeficient hosts.
* **Humanized mice, organ-on-chip, and co-culture:** improve immune/microbial/biophysical modeling but remain costly and technically variable.
* **Zebrafish xenografts:** rapid imaging and screening, with limitations in gastric anatomy and mammalian immunity.

A recent spatial study emphasizes the scale of heterogeneity: 64 tumor subregions showed expression differences between superficial tumor, deep tumor, and nodal metastasis. Consequently, models and clinical biopsies should be interpreted as samples of an evolving ecosystem rather than complete representations of the disease. (liang2024theburgeoningspatial pages 19-20, deng2023singlecelltranscriptomesequencing pages 4-5)

## Evidence limitations and interpretation

The strongest evidence in this report comes from human guidelines, pathology series, randomized screening/treatment evidence summarized in those guidelines, and large molecular cohorts. Single-cell, spatial, organoid, CAR-T case, and animal findings are mechanistically informative but not yet routine standards. Biomarker frequencies vary by assay and population. HDGC penetrance is especially sensitive to family ascertainment; older high-risk-family estimates should not be combined naively with newer population-based estimates. Exact PMID values were not available for every retrieved 2023–2024 source, so DOI URLs and publication dates are supplied rather than inventing PMIDs. Core recent sources include the CSCO guideline (December 2024, https://doi.org/10.1002/cac2.12516), SEOM guideline (July 2024, https://doi.org/10.1007/s12094-024-03600-7), systemic-therapy review (September 2024, https://doi.org/10.3390/cancers16193337), European screening review (September 2024, https://doi.org/10.1136/gutjnl-2024-332705), and HDGC review (October 2024, https://doi.org/10.1186/s13053-024-00293-5). (lordick2024systemictherapyof pages 8-10, leja2024wherearewe pages 6-6, sluis2024currentadvancesand pages 1-2, wang2024thechinesesociety pages 4-5, rivera2024seomgemcadttdclinicalguideline pages 1-2)

References

1. (wang2024thechinesesociety pages 7-8): Feng‐Hua Wang, Xiao‐Tian Zhang, Lei Tang, Qi Wu, Mu‐Yan Cai, Yuan‐Fang Li, Xiu‐Juan Qu, Hong Qiu, Yu‐Jing Zhang, Jie‐Er Ying, Jun Zhang, Ling‐Yu Sun, Rong‐Bo Lin, Chang Wang, Hao Liu, Miao‐Zhen Qiu, Wen‐Long Guan, Sheng‐Xiang Rao, Jia‐Fu Ji, Yan Xin, Wei‐Qi Sheng, Hui‐Mian Xu, Zhi‐Wei Zhou, Ai‐Ping Zhou, Jing Jin, Xiang‐Lin Yuan, Feng Bi, Tian‐Shu Liu, Han Liang, Yan‐Qiao Zhang, Guo‐Xin Li, Jun Liang, Bao‐Rui Liu, Lin Shen, Jin Li, and Rui‐Hua Xu. The chinese society of clinical oncology (csco): clinical guidelines for the diagnosis and treatment of gastric cancer, 2023. Cancer Communications, 44:127-172, Dec 2024. URL: https://doi.org/10.1002/cac2.12516, doi:10.1002/cac2.12516. This article has 406 citations.

2. (lordick2024systemictherapyof pages 8-10): Florian Lordick, Sun Young Rha, Kei Muro, Wei Peng Yong, and Radka Lordick Obermannová. Systemic therapy of gastric cancer—state of the art and future perspectives. Cancers, 16:3337, Sep 2024. URL: https://doi.org/10.3390/cancers16193337, doi:10.3390/cancers16193337. This article has 26 citations.

3. (rivera2024seomgemcadttdclinicalguideline pages 1-2): Fernando Rivera, Federico Longo, Marta Martín Richard, Paula Richart, Maria Alsina, Alberto Carmona, Ana Belén Custodio, Ana Fernández Montes, Javier Gallego, and Tania Fleitas Kanonnikoff. Seom-gemcad-ttd clinical guideline for the diagnosis and treatment of gastric cancer (2023). Clinical & Translational Oncology, 26:2826-2840, Jul 2024. URL: https://doi.org/10.1007/s12094-024-03600-7, doi:10.1007/s12094-024-03600-7. This article has 9 citations and is from a peer-reviewed journal.

4. (sluis2024currentadvancesand pages 1-2): L. van der Sluis, J.M. van Dieren, R.S. van der Post, and T.M. Bisseling. Current advances and challenges in managing hereditary diffuse gastric cancer (hdgc): a narrative review. Hereditary Cancer in Clinical Practice, Oct 2024. URL: https://doi.org/10.1186/s13053-024-00293-5, doi:10.1186/s13053-024-00293-5. This article has 13 citations and is from a peer-reviewed journal.

5. (OpenTargets Search: gastric adenocarcinoma): Open Targets Query (gastric adenocarcinoma, 27 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (leja2024wherearewe pages 3-4): Mārcis Leja. Where are we with gastric cancer screening in europe in 2024? Gut, 73:2074-2082, Sep 2024. URL: https://doi.org/10.1136/gutjnl-2024-332705, doi:10.1136/gutjnl-2024-332705. This article has 59 citations and is from a highest quality peer-reviewed journal.

7. (leja2024wherearewe pages 6-6): Mārcis Leja. Where are we with gastric cancer screening in europe in 2024? Gut, 73:2074-2082, Sep 2024. URL: https://doi.org/10.1136/gutjnl-2024-332705, doi:10.1136/gutjnl-2024-332705. This article has 59 citations and is from a highest quality peer-reviewed journal.

8. (leja2024wherearewe pages 3-3): Mārcis Leja. Where are we with gastric cancer screening in europe in 2024? Gut, 73:2074-2082, Sep 2024. URL: https://doi.org/10.1136/gutjnl-2024-332705, doi:10.1136/gutjnl-2024-332705. This article has 59 citations and is from a highest quality peer-reviewed journal.

9. (lim2023currentadvancesin pages 2-4): Hui Jun Lim, Lizhe Zhuang, and Rebecca C. Fitzgerald. Current advances in understanding the molecular profile of hereditary diffuse gastric cancer and its clinical implications. Journal of Experimental & Clinical Cancer Research : CR, Mar 2023. URL: https://doi.org/10.1186/s13046-023-02622-3, doi:10.1186/s13046-023-02622-3. This article has 25 citations.

10. (pereira2025hereditarydiffusegastric pages 2-4): Joana Pereira, Luísa Carvalho, Soraia Melo, Patrícia Carneiro, Maria Sofia Fernandes, Raquel Seruca, and Joana Figueiredo. Hereditary diffuse gastric cancer in progress: comparative lessons from lynch syndrome. European Journal of Human Genetics, Dec 2025. URL: https://doi.org/10.1038/s41431-025-01992-w, doi:10.1038/s41431-025-01992-w. This article has 0 citations and is from a domain leading peer-reviewed journal.

11. (deng2023singlecelltranscriptomesequencing pages 4-5): Gaohua Deng, Xu Zhang, Yonglan Chen, Sicheng Liang, Sha Liu, Zehui Yu, and Muhan Lü. Single-cell transcriptome sequencing reveals heterogeneity of gastric cancer: progress and prospects. Frontiers in Oncology, May 2023. URL: https://doi.org/10.3389/fonc.2023.1074268, doi:10.3389/fonc.2023.1074268. This article has 29 citations.

12. (wang2024thechinesesociety pages 4-5): Feng‐Hua Wang, Xiao‐Tian Zhang, Lei Tang, Qi Wu, Mu‐Yan Cai, Yuan‐Fang Li, Xiu‐Juan Qu, Hong Qiu, Yu‐Jing Zhang, Jie‐Er Ying, Jun Zhang, Ling‐Yu Sun, Rong‐Bo Lin, Chang Wang, Hao Liu, Miao‐Zhen Qiu, Wen‐Long Guan, Sheng‐Xiang Rao, Jia‐Fu Ji, Yan Xin, Wei‐Qi Sheng, Hui‐Mian Xu, Zhi‐Wei Zhou, Ai‐Ping Zhou, Jing Jin, Xiang‐Lin Yuan, Feng Bi, Tian‐Shu Liu, Han Liang, Yan‐Qiao Zhang, Guo‐Xin Li, Jun Liang, Bao‐Rui Liu, Lin Shen, Jin Li, and Rui‐Hua Xu. The chinese society of clinical oncology (csco): clinical guidelines for the diagnosis and treatment of gastric cancer, 2023. Cancer Communications, 44:127-172, Dec 2024. URL: https://doi.org/10.1002/cac2.12516, doi:10.1002/cac2.12516. This article has 406 citations.

13. (gullo2020precancerouslesionsof pages 6-8): Irene Gullo, Federica Grillo, Luca Mastracci, Alessandro Vanoli, Fatima Carneiro, Luca Saragoni, Francesco Limarzi, Jacopo Ferro, Paola Parente, and Matteo Fassan. Precancerous lesions of the stomach, gastric cancer and hereditary gastric cancer syndromes. Pathologica, 112:166-185, Sep 2020. URL: https://doi.org/10.32074/1591-951x-166, doi:10.32074/1591-951x-166. This article has 233 citations.

14. (mok2024racialdisparitiesof pages 7-8): Jean Woo Mok, Yeong Ha Oh, Deepa Magge, and Sekhar Padmanabhan. Racial disparities of gastric cancer in the usa: an overview of epidemiology, global screening guidelines, and targeted screening in a heterogeneous population. Gastric cancer : official journal of the International Gastric Cancer Association and the Japanese Gastric Cancer Association, 27:426-438, Mar 2024. URL: https://doi.org/10.1007/s10120-024-01475-9, doi:10.1007/s10120-024-01475-9. This article has 37 citations.

15. (mok2024racialdisparitiesof pages 5-7): Jean Woo Mok, Yeong Ha Oh, Deepa Magge, and Sekhar Padmanabhan. Racial disparities of gastric cancer in the usa: an overview of epidemiology, global screening guidelines, and targeted screening in a heterogeneous population. Gastric cancer : official journal of the International Gastric Cancer Association and the Japanese Gastric Cancer Association, 27:426-438, Mar 2024. URL: https://doi.org/10.1007/s10120-024-01475-9, doi:10.1007/s10120-024-01475-9. This article has 37 citations.

16. (leja2024wherearewe pages 6-7): Mārcis Leja. Where are we with gastric cancer screening in europe in 2024? Gut, 73:2074-2082, Sep 2024. URL: https://doi.org/10.1136/gutjnl-2024-332705, doi:10.1136/gutjnl-2024-332705. This article has 59 citations and is from a highest quality peer-reviewed journal.

17. (burz2024prognosisandtreatment pages 2-4): Claudia Burz, Vlad Pop, Ciprian Silaghi, Iulia Lupan, and Gabriel Samasca. Prognosis and treatment of gastric cancer: a 2024 update. Cancers, 16:1708, Apr 2024. URL: https://doi.org/10.3390/cancers16091708, doi:10.3390/cancers16091708. This article has 75 citations.

18. (xu2024singlecellrnasequencing pages 9-11): Jiao Xu, Bixin Yu, Fan Wang, and Jin Yang. Single-cell rna sequencing to map tumor heterogeneity in gastric carcinogenesis paving roads to individualized therapy. Cancer Immunology, Immunotherapy : CII, Sep 2024. URL: https://doi.org/10.1007/s00262-024-03820-4, doi:10.1007/s00262-024-03820-4. This article has 23 citations.

19. (liang2024theburgeoningspatial pages 19-20): Weizheng Liang, Zhenpeng Zhu, Dandan Xu, Peng Wang, Fei Guo, Haoshan Xiao, Chenyang Hou, Jun Xue, Xuejun Zhi, and Rensen Ran. The burgeoning spatial multi-omics in human gastrointestinal cancers. PeerJ, 12:e17860, Sep 2024. URL: https://doi.org/10.7717/peerj.17860, doi:10.7717/peerj.17860. This article has 14 citations and is from a peer-reviewed journal.

20. (lim2023currentadvancesin pages 1-2): Hui Jun Lim, Lizhe Zhuang, and Rebecca C. Fitzgerald. Current advances in understanding the molecular profile of hereditary diffuse gastric cancer and its clinical implications. Journal of Experimental & Clinical Cancer Research : CR, Mar 2023. URL: https://doi.org/10.1186/s13046-023-02622-3, doi:10.1186/s13046-023-02622-3. This article has 25 citations.

21. (gullo2020precancerouslesionsof pages 14-15): Irene Gullo, Federica Grillo, Luca Mastracci, Alessandro Vanoli, Fatima Carneiro, Luca Saragoni, Francesco Limarzi, Jacopo Ferro, Paola Parente, and Matteo Fassan. Precancerous lesions of the stomach, gastric cancer and hereditary gastric cancer syndromes. Pathologica, 112:166-185, Sep 2020. URL: https://doi.org/10.32074/1591-951x-166, doi:10.32074/1591-951x-166. This article has 233 citations.

22. (gullo2020precancerouslesionsof pages 15-17): Irene Gullo, Federica Grillo, Luca Mastracci, Alessandro Vanoli, Fatima Carneiro, Luca Saragoni, Francesco Limarzi, Jacopo Ferro, Paola Parente, and Matteo Fassan. Precancerous lesions of the stomach, gastric cancer and hereditary gastric cancer syndromes. Pathologica, 112:166-185, Sep 2020. URL: https://doi.org/10.32074/1591-951x-166, doi:10.32074/1591-951x-166. This article has 233 citations.

23. (xu2024singlecellrnasequencing pages 13-14): Jiao Xu, Bixin Yu, Fan Wang, and Jin Yang. Single-cell rna sequencing to map tumor heterogeneity in gastric carcinogenesis paving roads to individualized therapy. Cancer Immunology, Immunotherapy : CII, Sep 2024. URL: https://doi.org/10.1007/s00262-024-03820-4, doi:10.1007/s00262-024-03820-4. This article has 23 citations.

24. (mok2024racialdisparitiesof pages 8-9): Jean Woo Mok, Yeong Ha Oh, Deepa Magge, and Sekhar Padmanabhan. Racial disparities of gastric cancer in the usa: an overview of epidemiology, global screening guidelines, and targeted screening in a heterogeneous population. Gastric cancer : official journal of the International Gastric Cancer Association and the Japanese Gastric Cancer Association, 27:426-438, Mar 2024. URL: https://doi.org/10.1007/s10120-024-01475-9, doi:10.1007/s10120-024-01475-9. This article has 37 citations.

## Artifacts

- [Edison artifact artifact-00](Gastric_Adenocarcinoma-deep-research-falcon_artifacts/artifact-00.md)