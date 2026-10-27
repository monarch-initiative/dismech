---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-19T19:58:56.774541'
end_time: '2026-08-19T20:09:57.271161'
duration_seconds: 660.5
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: S-Adenosylhomocysteine Hydrolase Deficiency
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 5
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: AHCY_Deficiency-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** S-Adenosylhomocysteine Hydrolase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **S-Adenosylhomocysteine Hydrolase Deficiency** covering all of the
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
- **Disease Name:** S-Adenosylhomocysteine Hydrolase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **S-Adenosylhomocysteine Hydrolase Deficiency** covering all of the
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


# S-Adenosylhomocysteine Hydrolase Deficiency: Disease Characteristics Report

## Executive summary

S-adenosylhomocysteine hydrolase deficiency (SAHHD; AHCY deficiency) is an ultra-rare autosomal-recessive disorder of the methionine/transmethylation cycle caused by biallelic pathogenic variants in **AHCY**. Deficient enzyme activity impairs conversion of S-adenosylhomocysteine (SAH) to adenosine and homocysteine, producing marked SAH and S-adenosylmethionine (SAM) accumulation, hypermethioninemia, and widespread disturbance of methylation-dependent biology. The major affected systems are liver, skeletal muscle, and central nervous system. Severity ranges from fetal hydrops and fatal neonatal encephalomyopathy/liver failure to minimally symptomatic childhood disease and adult-onset myopathy, cirrhosis, and hepatocellular carcinoma (HCC). Only **16 affected individuals had been reported by September 2024**, so frequencies, penetrance, prognosis, and treatment effects remain imprecise (pinto2024asymptomaticpediatricpresentation pages 1-2, pinto2024asymptomaticpediatricpresentation pages 7-7, pinto2024asymptomaticpediatricpresentation pages 2-2).

The most important recent development is recognition of a mild, probably underdiagnosed **p.Arg49His** phenotype in children of Pakistani/South Asian ancestry. In two 2024 cases, methionine restriction corrected hypermethioninemia and reversed mild white-matter abnormalities but did not normalize SAH, SAM, liver enzymes, or muscle biomarkers (pinto2024asymptomaticpediatricpresentation pages 1-2, pinto2024asymptomaticpediatricpresentation pages 9-10, pinto2024asymptomaticpediatricpresentation pages 2-3).

The following table provides a compact knowledge-base summary; the narrative below supplies qualifications and additional ontology annotations.

| Knowledge-base field | Concise finding | Ontology / identifier suggestions | Key sources (year, DOI URL) | Evidence |
|---|---|---|---|---|
| Definition / inheritance | Ultra-rare **autosomal recessive** inborn error of methionine-cycle / transmethylation metabolism caused by **biallelic AHCY variants**, producing multisystem disease ranging from lethal neonatal encephalomyopathy/liver failure to mild or asymptomatic childhood presentations with later liver/muscle complications. | MONDO: not confidently confirmed here; OMIM **AHCY gene/protein record reported as 180960 in literature, but disease-specific mapping uncertain**; HPO disease grouping could include hypermethioninemia / myopathy / liver disease terms. | Pinto et al. 2024, https://doi.org/10.1002/jmd2.12449; Barić et al. 2017, https://doi.org/10.1007/s10545-016-9972-7 | (pinto2024asymptomaticpediatricpresentation pages 1-2, pinto2024asymptomaticpediatricpresentation pages 2-2) |
| Gene / protein | **AHCY** encodes **S-adenosylhomocysteine hydrolase** (also SAHH; adenosylhomocysteinase), the key mammalian enzyme clearing SAH. | HGNC symbol: **AHCY**; protein name: S-adenosylhomocysteine hydrolase / adenosylhomocysteinase. | Stender et al. 2015, https://doi.org/10.1016/j.ymgme.2015.10.009; Vizán et al. 2021, https://doi.org/10.3389/fcell.2021.654344 | (stender2015adultonsetliverdisease pages 5-6, vizan2021functionalandpathological pages 4-5) |
| Enzyme reaction | Catalyzes hydrolysis of **S-adenosylhomocysteine (SAH)** to **adenosine + homocysteine**; reduced activity causes SAH accumulation, impaired methyltransferase flux, and disturbed SAM/SAH balance. Residual activity reported around **3%–20% of normal** in affected individuals. | GO suggestion: adenosylhomocysteinase activity; CHEBI suggestions: SAH, adenosine, homocysteine, SAM, methionine. | Stender et al. 2015, https://doi.org/10.1016/j.ymgme.2015.10.009; Motzek et al. 2016, https://doi.org/10.1371/journal.pone.0151261 | (stender2015adultonsetliverdisease pages 6-8, motzek2016abnormalhypermethylationat pages 8-9) |
| Hallmark biomarkers | Core biochemical pattern: **hypermethioninemia**, markedly elevated **SAH** and **SAM**, mild hyperhomocysteinemia in some patients, elevated **CK**, elevated aminotransferases, and low enzyme activity. Example mild pediatric case: **SAM 2426 nmol/L** (ref 55–116), **SAH 1408 nmol/L** (ref 9–45). Example homozygous adult family data: **SAH 3260 nmol/L**, **SAM 1930 nmol/L**, **methionine 528 μmol/L**. | HPO suggestions: Hypermethioninemia, Elevated circulating S-adenosylhomocysteine, Elevated circulating S-adenosylmethionine, Elevated creatine kinase, Elevated hepatic transaminases. | Pinto et al. 2024, https://doi.org/10.1002/jmd2.12449; Stender et al. 2015, https://doi.org/10.1016/j.ymgme.2015.10.009; Barić et al. 2017, https://doi.org/10.1007/s10545-016-9972-7 | (pinto2024asymptomaticpediatricpresentation pages 4-4, stender2015adultonsetliverdisease pages 5-6) |
| Clinical spectrum | Frequent manifestations: neonatal/infantile hypotonia, developmental delay, myopathy, liver dysfunction/failure, coagulopathy, delayed myelination or leukodystrophy, absent reflexes, cognitive/language issues, and in long-term survivors **cirrhosis/hepatocellular carcinoma**. Severity is highly variable, including **asymptomatic children** with biochemical disease. | HPO suggestions: Hypotonia, Global developmental delay, Myopathy, Leukodystrophy, Delayed myelination, Hepatic failure, Coagulopathy, Hepatocellular carcinoma. | Pinto et al. 2024, https://doi.org/10.1002/jmd2.12449; Stender et al. 2015, https://doi.org/10.1016/j.ymgme.2015.10.009; Bas et al. 2020, https://doi.org/10.1002/ajmg.a.61489 | (pinto2024asymptomaticpediatricpresentation pages 1-2, stender2015adultonsetliverdisease pages 6-8) |
| Major organs / systems | Primary organ involvement: **liver, skeletal muscle, central nervous system**. Secondary/late complications include hepatic cirrhosis and **hepatocellular carcinoma**. | UBERON suggestions: liver, skeletal muscle tissue, brain, cerebral white matter; CL suggestions uncertain from current evidence. | Barić et al. 2017, https://doi.org/10.1007/s10545-016-9972-7; Ramadža et al. 2022, https://doi.org/10.3389/fped.2022.847445; Stender et al. 2015, https://doi.org/10.1016/j.ymgme.2015.10.009 | (stender2015adultonsetliverdisease pages 6-8, pinto2024asymptomaticpediatricpresentation pages 8-9) |
| Known reported variants | Reported disease-associated variants include **p.Arg49His**, **p.Arg49Cys**, **p.Tyr143Cys**, **p.Trp112Ter**, **p.Asp86Gly**, **p.Gly71Ser**, **p.Tyr328Asp**, **p.Ala89Val**, and newer presumed pathogenic variants **p.Thr57Ile** and **p.Val217Met**. Most are missense; at least one nonsense variant is reported. | Variant ontology IDs not asserted here; inheritance consistent with biallelic pathogenic / likely pathogenic germline variants. | Stender et al. 2015, https://doi.org/10.1016/j.ymgme.2015.10.009; Bas et al. 2020, https://doi.org/10.1002/ajmg.a.61489; Vugrek et al. 2009, https://doi.org/10.1002/humu.20985 | (stender2015adultonsetliverdisease pages 6-8, stender2015adultonsetliverdisease pages 16-16) |
| Epidemiology / patient count | Extremely rare; **2024 report states 16 patients reported globally**. A mild **South Asian / Pakistani p.Arg49His hotspot** is suggested, with allele frequency cited in the report as about **1/15,300 in South Asia vs 1/83,400 globally**; this should be treated as preliminary case-series/population-database interpretation rather than definitive prevalence. | Orphanet / MONDO IDs not confidently confirmed from current context; prevalence/incidence not established. | Pinto et al. 2024, https://doi.org/10.1002/jmd2.12449 | (pinto2024asymptomaticpediatricpresentation pages 7-7, pinto2024asymptomaticpediatricpresentation pages 2-2) |
| Diagnosis | Recommended workup for unexplained isolated hypermethioninemia or liver-muscle-neurologic syndrome: plasma amino acids plus **SAM and SAH measurement**, CK, liver enzymes, and **molecular testing of AHCY** (single gene, panel, exome/genome depending presentation). Differential diagnosis within inherited methylation disorders is important. Newborn screening is **not currently recommended as a primary target** based on consensus guidance. | HPO / lab ontology suggestions: Hypermethioninemia, Elevated SAM, Elevated SAH; ICD/MeSH not confidently confirmed. | Barić et al. 2017, https://doi.org/10.1007/s10545-016-9972-7; Pinto et al. 2024, https://doi.org/10.1002/jmd2.12449 | (pinto2024asymptomaticpediatricpresentation pages 1-2, pinto2024asymptomaticpediatricpresentation pages 2-3) |
| Treatment | Evidence is case-based. Main management: **methionine-restricted diet** (often with methionine-free amino acid formula). Adjuncts reported/considered: **creatine**, **phosphatidylcholine**, **N-acetylcysteine**. Biochemical and neurologic responses are variable; diet may lower methionine but often does **not normalize SAH/SAM**. **Liver transplantation** has been used in severe disease with reported biochemical and developmental improvement in at least one case. No approved gene/RNA/cell therapy and no disease-specific interventional trial identified from current search. | NCIT suggestions: Dietary modification, creatine supplementation, phosphatidylcholine supplementation, liver transplantation. | Barić et al. 2005, https://doi.org/10.1007/s10545-005-0192-9; Grubbs et al. 2010, https://doi.org/10.1007/s10545-010-9171-x; Barić et al. 2017, https://doi.org/10.1007/s10545-016-9972-7; Pinto et al. 2024, https://doi.org/10.1002/jmd2.12449 | (pinto2024asymptomaticpediatricpresentation pages 8-9, stender2015adultonsetliverdisease pages 6-8) |
| Prognosis | Prognosis is **highly variable**. Severe perinatal/infantile forms can be fatal within months; other patients survive into adulthood but remain at risk for progressive liver disease, myopathy, cognitive effects, and **hepatocellular carcinoma**. Long-term natural history remains poorly defined because of very small case numbers. | HPO suggestions: Early death, Liver cirrhosis, Hepatocellular carcinoma, Progressive myopathy. | Stender et al. 2015, https://doi.org/10.1016/j.ymgme.2015.10.009; Bas et al. 2020, https://doi.org/10.1002/ajmg.a.61489 | (stender2015adultonsetliverdisease pages 6-8, pinto2024asymptomaticpediatricpresentation pages 1-2) |
| Latest 2023–2024 developments | **2024:** two asymptomatic Pakistani siblings expanded the mild phenotype and showed **diet-reversible leukodystrophy**, reinforcing concern for underdiagnosis and adult complications. **2023:** AHCY knockdown RNA-seq/cell work linked deficiency to **Wnt/LEF1-related transcriptional changes**; **C. elegans** partial-deficiency model with human-corresponding variant supported altered SAM/SAH biology and longevity effects. These mechanistic findings are experimental and not yet validated clinically. | GO suggestions: Wnt signaling pathway, regulation of transcription, methylation-related processes; model-organism mappings only. | Pinto et al. 2024, https://doi.org/10.1002/jmd2.12449; Pavičić et al. 2023, https://doi.org/10.3390/ijms242216102; Thapa et al. 2023, https://doi.org/10.1038/s41514-023-00125-1 | (pinto2024asymptomaticpediatricpresentation pages 9-10, pinto2024asymptomaticpediatricpresentation pages 1-2) |
| Evidence gaps | No robust prevalence/incidence estimates; no controlled treatment trials; no validated genotype-specific management algorithm; penetrance and carrier frequency remain uncertain outside limited population-database observations; no established disease-specific QoL metrics; limited longitudinal biomarker-outcome correlation; no clearly documented natural disease in other species; disease identifiers across OMIM/Orphanet/MONDO require separate authoritative confirmation. | Flag as **uncertain / absent data** where noted. | Barić et al. 2017, https://doi.org/10.1007/s10545-016-9972-7; Pinto et al. 2024, https://doi.org/10.1002/jmd2.12449 | (pinto2024asymptomaticpediatricpresentation pages 1-2, pinto2024asymptomaticpediatricpresentation pages 8-9) |


*Table: This table summarizes the most actionable disease-knowledge-base facts for S-adenosylhomocysteine hydrolase deficiency, including core biology, clinical features, diagnosis, treatment, and recent developments. It emphasizes evidence-backed details, ontology suggestions where confident, and explicit uncertainty where identifiers or data are not firmly established.*

## 1. Disease information

### Definition and names

Preferred name: **S-adenosylhomocysteine hydrolase deficiency**. Common alternatives are **SAH hydrolase deficiency**, **SAHH deficiency**, **AHCY deficiency**, **adenosylhomocysteinase deficiency**, and **hypermethioninemia due to S-adenosylhomocysteine hydrolase deficiency**. It is an inherited methylation disorder and Mendelian inborn error of methionine metabolism.

The 2024 clinical description states: “Its clinical spectrum spans from severe perinatal encephalomyopathy and liver failure to asymptomatic course in patients with isolated hypermethioninemia.” This is an appropriate concise disease definition (Pinto et al., published September 2024; DOI: https://doi.org/10.1002/jmd2.12449) (pinto2024asymptomaticpediatricpresentation pages 1-2).

### Identifiers

* **Causal gene:** AHCY; the literature cites **OMIM 180960** for AHCY. This appears to be the gene record rather than a confidently verified disease-entry number (stender2015adultonsetliverdisease pages 5-6).
* **MONDO:** a disease-specific MONDO identifier was not reliably recoverable from the evidence searched and should be verified directly in the current MONDO release before database ingestion.
* **Orphanet:** no identifier was reliably established from the retrieved primary literature.
* **ICD-10/ICD-11:** no dedicated code was identified; coding generally falls under other specified disorders of amino-acid metabolism/metabolism.
* **MeSH:** no disease-specific descriptor was verified; broader headings include *Amino Acid Metabolism, Inborn Errors* and *Hypermethioninemia*.

These findings are aggregated from disease-level literature and case reports, not EHR-derived individual-patient records.

## 2. Etiology, risk, and protective factors

The necessary cause is **biallelic germline AHCY dysfunction**. The inheritance pattern is autosomal recessive; heterozygous parents are typically clinically unaffected, although modest SAM/SAH elevations have been observed in carriers. Pathogenic alleles reduce enzyme abundance, stability, catalytic activity, or a combination thereof (stender2015adultonsetliverdisease pages 5-6, stender2015adultonsetliverdisease pages 6-8).

Reported alleles include **p.Arg49His, p.Arg49Cys, p.Gly71Ser, p.Asp86Gly, p.Ala89Val, p.Trp112Ter, p.Tyr143Cys, p.Tyr328Asp**, and the proposed disease-associated **p.Thr57Ile/p.Val217Met** compound-heterozygous genotype. Most are missense; p.Trp112Ter is nonsense. Published classifications predate or do not uniformly apply current ACMG/AMP criteria, so each variant should be re-evaluated in ClinVar/gnomAD using transcript-specific HGVS before clinical reporting (stender2015adultonsetliverdisease pages 6-8, stender2015adultonsetliverdisease pages 16-16).

The best-supported genotype–phenotype observation is that homozygous **c.146G>A (p.Arg49His)** can retain sufficient function to permit an asymptomatic or mild childhood course, although adult liver malignancy and myopathy have occurred in the same extended phenotype. Its reported frequency was approximately 1/15,300 in South Asians versus 1/83,400 globally, suggesting regional enrichment rather than a proven founder effect (pinto2024asymptomaticpediatricpresentation pages 7-7).

No environmental toxin, infection, sex, occupation, smoking, alcohol, or lifestyle exposure is known to cause the disorder. Dietary methionine is a **burden modifier**, not a cause: reducing intake may lower plasma methionine, while excessive restriction risks poor growth and essential-amino-acid deficiency. No validated protective allele, modifier gene, or gene–environment interaction has been demonstrated. Consanguinity and family history increase the probability of homozygosity but do not alter the biochemical mechanism.

## 3. Phenotypes

Because only 16 patients were known by 2024, percentages would be misleading. The following frequencies should be recorded qualitatively.

| Phenotype | Type, onset, course, impact | Suggested HPO term |
|---|---|---|
| Hypermethioninemia | Laboratory hallmark; may be absent or less conspicuous in early infancy; chronic and diet-responsive | **Hyper­methioninemia** |
| Elevated SAH and SAM | Most discriminating laboratory abnormality; often persists despite diet | Increased circulating SAH; increased circulating SAM |
| Hypotonia/weakness | Common in severe neonatal and infantile disease; may progress to proximal myopathy | **HP:0001252 Hypotonia**, muscular weakness |
| Myopathy/CK elevation | Early or subclinical childhood onset through adult progression; proximal/lower-limb predominance; impairs mobility | Myopathy; elevated serum CK |
| Developmental or cognitive impairment | Variable—severe global delay to isolated verbal-processing weakness or normal mainstream schooling | Global developmental delay; intellectual disability; language impairment |
| Delayed myelination/leukodystrophy | Infantile or subtle childhood MRI finding; at least one case was reversible after diet | Delayed myelination; leukodystrophy |
| Hepatic dysfunction | Elevated aminotransferases, synthetic dysfunction, coagulopathy, steatosis, chronic failure or cirrhosis | Elevated transaminases; hepatic failure; liver cirrhosis |
| Fetal hydrops/edema | Severe prenatal/neonatal presentations; associated with high early mortality | Hydrops fetalis; generalized edema |
| HCC | Late complication in adolescent/adult survivors; reported at ages 17 and 32 in one family | Hepatocellular carcinoma |

In the 2024 sibling report, one child had methionine **985 µmol/L** (reference 10–60), ALT approximately sixfold above normal, reversible leukodystrophy, and persistently abnormal liver/muscle markers despite biochemical correction of methionine (pinto2024asymptomaticpediatricpresentation pages 2-3). Another had SAM **2,426 nmol/L** (reference 55–116) and SAH **1,408 nmol/L** (reference 9–45), mild white-matter disease, and low-average verbal reasoning while attending mainstream school (pinto2024asymptomaticpediatricpresentation pages 4-4).

Quality-of-life instruments such as EQ-5D, SF-36, or PROMIS have not been reported. Severe disease compromises feeding, mobility, communication, development, and survival; mild pediatric disease may have little apparent daily effect but requires burdensome diet and lifelong surveillance.

## 4. Genetic and molecular information

**AHCY** encodes the highly conserved, NAD-dependent tetrameric enzyme S-adenosylhomocysteine hydrolase. Reported patients have approximately **3–20% residual activity**, consistent predominantly with partial loss of function; complete loss is probably incompatible with embryonic survival (stender2015adultonsetliverdisease pages 6-8, vizan2021functionalandpathological pages 4-5).

All established patient variants are constitutional/germline. There is no evidence that somatic AHCY variants cause SAHHD, nor is there evidence for dominant-negative or gain-of-function disease, chromosomal rearrangements, repeat expansions, mitochondrial variants, or recurrent copy-number abnormalities. No validated modifier gene is known.

### Epigenetics

SAH is a potent product inhibitor of methyltransferases. Patient blood studies found global DNA hypermethylation in two of three examined patients and abnormal imprinting-control-region methylation in four of seven, but changes were neither universal nor uniform. A proposed explanation is differential methyltransferase sensitivity: under high SAH, DNMT1 activity fell approximately 30%, whereas PRMT7 activity fell approximately 90%; excess SAM may therefore sustain DNA methylation while protein/RNA methylation remains inhibited (motzek2016abnormalhypermethylationat pages 8-9).

The authors’ conclusion is appropriately cautious: DNA hypermethylation is “a frequent but not a constant feature” affecting genomic regions to different degrees (Motzek et al., March 2016; DOI: https://doi.org/10.1371/journal.pone.0151261) (motzek2016abnormalhypermethylationat pages 8-9).

No diagnostic episignature, validated transcriptomic biomarker, structural genomic signature, or clinically actionable modifier has been established.

## 5. Environmental, lifestyle, and infectious information

SAHHD is not infectious and has no zoonotic transmission. No causal toxin, radiation, pollution, occupational exposure, exercise pattern, smoking, or alcohol relationship has been demonstrated. Nutrition affects substrate flux: dietary protein/methionine can alter methionine concentrations but does not reliably correct the primary SAH clearance defect. Environmental “prevention” is therefore not applicable beyond medically supervised dietary management after diagnosis.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic trigger:** biallelic AHCY hypomorphic/loss-of-function variants.
2. **Primary biochemical lesion:** reduced hydrolysis of SAH to adenosine and homocysteine.
3. **Metabolite disturbance:** profound SAH accumulation, elevated SAM, altered SAM:SAH methylation potential, and secondary hypermethioninemia. One reported homozygous case had SAH 3,260 nmol/L, SAM 1,930 nmol/L, and methionine 528 µmol/L (stender2015adultonsetliverdisease pages 5-6).
4. **Cellular consequences:** inhibition or imbalance of DNA, RNA, histone, protein, phospholipid, and small-molecule methyltransferase reactions; altered chromatin and gene expression; probable impairment of creatine and phosphatidylcholine synthesis; and disturbed adenosine/homocysteine handling.
5. **Tissue injury:** myocyte dysfunction and lipid replacement, abnormal myelination/white matter, hepatocellular steatosis and degeneration, synthetic liver failure, fibrosis/cirrhosis, and possibly carcinogenesis.
6. **Clinical manifestations:** hypotonia/myopathy, CK elevation, neurodevelopmental disease, liver failure, and late HCC.

The enzyme reaction is reversible in vitro but is driven toward hydrolysis in vivo by rapid removal of adenosine and homocysteine. SAH elevation may exceed 100-fold in patients (motzek2016abnormalhypermethylationat pages 8-9).

### Human mechanistic evidence

Human evidence directly supports metabolite accumulation, residual enzyme deficiency, altered methylation, delayed myelination, myopathy, and liver disease. The exact pathway from methylation disturbance to organ-selective injury remains unresolved. PRMT7 inhibition has been proposed as relevant to myelin-basic-protein methylation, but this is not proven to be the principal neurological mechanism (motzek2016abnormalhypermethylationat pages 8-9).

### Recent molecular profiling

In 2023, AHCY knockdown in SW480 colorectal cells produced RNA-seq changes involving Wnt signaling, epithelial–mesenchymal transition, proliferation, and increased **LEF1** RNA/protein. This establishes a cell-model link between AHCY depletion and Wnt/LEF1 regulation, not a demonstrated patient mechanism or indication that colorectal cancer is part of SAHHD (DOI: https://doi.org/10.3390/ijms242216102).

Additional experimental work suggests SAH can inhibit autophagy through an AHCYL1–PIK3C3 axis, but direct involvement in human SAHHD organ pathology remains unproven. Likewise, circadian, p53/senescence, and adenosine-depletion effects are biologically plausible but not validated clinical drivers (vizan2021functionalandpathological pages 4-5, vizan2021functionalandpathological pages 7-8).

Suggested GO annotations include **S-adenosylhomocysteine hydrolase activity**, methionine metabolic process, S-adenosylmethionine metabolic process, methylation, chromatin organization, regulation of Wnt signaling, myelination, skeletal-muscle development, and liver development. Candidate cell types are **hepatocyte**, **skeletal muscle fiber/myocyte**, oligodendrocyte, neuron, and glial cell; evidence is strongest for hepatocytes and muscle tissue, not for a uniquely targeted neural cell type.

## 7. Anatomical structures affected

* **Primary:** liver (UBERON: liver), skeletal muscle tissue, brain/cerebral white matter.
* **Secondary:** peripheral neuromuscular system and systemic coagulation through hepatic synthetic failure.
* **Tissue findings:** hepatic macrovesicular lipid droplets/steatosis; skeletal-muscle lipid infiltration and atrophy; delayed or abnormal cerebral myelination.
* **Subcellular context:** AHCY functions in cytosolic and nuclear/chromatin-associated methylation environments. Relevant GO cellular components include cytosol, nucleus, chromatin, and protein-containing complex.
* **Lateralization:** no characteristic unilateral or asymmetric pattern.

Skeletal-muscle MRI/MRS in three brothers aged 8, 11, and 13 years showed age-increasing lipid fraction, greatest in proximal lower-extremity muscles, supporting progressive subclinical muscle replacement and a role for MRI/MRS in longitudinal monitoring.

## 8. Temporal development and natural history

The disease may begin prenatally with hydrops, neonatally with hypotonia/encephalopathy/liver failure, in infancy with delayed motor development and myopathy, or remain clinically silent into childhood/adulthood. Severe infantile cases have died between approximately 3 and 12 months; intermediate cases develop chronic neuromuscular and liver disease; p.Arg49His homozygotes may remain minimally symptomatic for years before adult myopathy, cirrhosis, or HCC (stender2015adultonsetliverdisease pages 5-6, pinto2024asymptomaticpediatricpresentation pages 1-2, stender2015adultonsetliverdisease pages 6-8).

There is no validated staging system. A practical sequence is: biochemical/asymptomatic phase → neurologic, muscle, or hepatic manifestations → chronic progressive myopathy/cirrhosis → hepatic malignancy or organ failure. Course is chronic and lifelong rather than episodic. Treatment-induced biochemical improvement and white-matter reversal are possible, but spontaneous remission is not established (pinto2024asymptomaticpediatricpresentation pages 9-10).

Early childhood is probably an intervention window because myelination and muscle development are ongoing, but the evidence is a single/few cases rather than a controlled study.

## 9. Inheritance and population

Inheritance is autosomal recessive. For two confirmed carrier parents, recurrence risks per pregnancy are 25% affected, 50% heterozygous carrier, and 25% unaffected/non-carrier. Penetrance of severe biallelic variants appears high, but penetrance of mild alleles and age-dependent manifestations is unknown. Expressivity is markedly variable. Anticipation and germline mosaicism have not been reported.

No population prevalence or annual incidence can be calculated reliably. Sixteen published patients worldwide by 2024 indicates extreme rarity but also substantial underdiagnosis (pinto2024asymptomaticpediatricpresentation pages 7-7, pinto2024asymptomaticpediatricpresentation pages 2-2). Cases have been reported from Croatia, the United States, Czech Republic, Türkiye, and Pakistani/South Asian families. No sex predominance is established. Consanguinity has contributed to homozygous cases. Carrier frequency and a definitive founder haplotype are unknown.

## 10. Diagnostics

### Recommended workflow

1. **Clinical suspicion:** unexplained hypermethioninemia, hypotonia/myopathy, persistent CK elevation, liver dysfunction/coagulopathy, delayed myelination, or fetal hydrops.
2. **First-line chemistry:** quantitative plasma amino acids, total homocysteine, liver panel, bilirubin, albumin, coagulation profile, CK, renal profile, glucose, and ammonia as clinically indicated.
3. **Discriminating metabolites:** plasma **SAH and SAM** measured in an experienced biochemical-genetics laboratory. Isolated hypermethioninemia alone is nonspecific; SAM/SAH testing is central to distinguishing inherited methylation disorders (pinto2024asymptomaticpediatricpresentation pages 4-4, pinto2024asymptomaticpediatricpresentation pages 2-3).
4. **Confirmation:** biallelic pathogenic/likely pathogenic AHCY variants plus compatible biochemistry; fibroblast, erythrocyte, or liver AHCY activity can provide functional confirmation where available.
5. **Baseline organ assessment:** neurologic/developmental evaluation; brain MRI; CK and muscle examination, with muscle MRI/MRS if useful; liver ultrasound/elastography, synthetic function, and AFP/HCC surveillance; ECG/echocardiography when clinically indicated.

Single-gene sequencing with deletion/duplication analysis is appropriate when biochemistry is characteristic. A hypermethioninemia, liver-failure, neurometabolic, or myopathy panel is efficient for overlapping presentations. WES/WGS is useful for atypical neonatal disease or unresolved cases, as illustrated by novel-variant discovery, but biochemical confirmation remains important. CMA, karyotype, FISH, mtDNA testing, and repeat-expansion testing are not routine unless another diagnosis is suspected.

### Differential diagnosis

Key alternatives are **MAT1A-related methionine adenosyltransferase I/III deficiency**, glycine N-methyltransferase deficiency, adenosine kinase deficiency, cystathionine beta-synthase deficiency, tyrosinemia, citrin deficiency, generalized liver failure, congenital disorders of glycosylation—especially PMM2-CDG—and primary neuromuscular/leukodystrophy disorders. SAH and SAM profiles, total homocysteine, liver phenotype, CK, and molecular testing distinguish these conditions. SAHHD can clinically resemble PMM2-CDG (pinto2024asymptomaticpediatricpresentation pages 1-2, pinto2024asymptomaticpediatricpresentation pages 2-2).

Consensus authors concluded that inherited methylation disorders did **not qualify as primary biochemical newborn-screening targets**, partly because hypermethioninemia may be absent early and treatment evidence is limited. Genomic newborn screening may eventually detect AHCY variants, but no disease-specific effectiveness data exist.

## 11. Outcomes and prognosis

No 5- or 10-year survival estimates, mortality rates, or life-expectancy tables exist. Prognosis is genotype- and severity-dependent. Severe neonatal disease may be fatal within months; a 2020 infant with compound-heterozygous p.Thr57Ile/p.Val217Met died at 3 months from cardiovascular collapse. Conversely, mild homozygous p.Arg49His patients may survive into adulthood (pinto2024asymptomaticpediatricpresentation pages 1-2, stender2015adultonsetliverdisease pages 6-8).

Major morbidity includes developmental disability, progressive proximal myopathy, chronic liver failure/cirrhosis, and HCC. HCC at ages 17 and 32 suggests that malignancy surveillance is justified in long-term survivors, although the absolute risk cannot be estimated (stender2015adultonsetliverdisease pages 6-8). Residual enzyme activity, genotype, baseline liver synthetic function, CK/muscle imaging, SAM/SAH concentrations, and response to diet are plausible prognostic markers, but none is validated.

## 12. Treatment and real-world implementation

### Methionine restriction

A specialist metabolic diet—with natural-protein/methionine restriction and methionine-free amino-acid formula—is the principal disease-directed intervention. It may lower methionine and sometimes SAM/SAH and improve strength or brain MRI, but responses are inconsistent. In the 2024 children, intake was reduced to approximately **1.6 g protein/kg/day and 32 mg methionine/kg/day**; methionine fell, while SAH/SAM and liver/muscle biomarkers remained abnormal (pinto2024asymptomaticpediatricpresentation pages 7-7, pinto2024asymptomaticpediatricpresentation pages 2-3).

Over-restriction is hazardous because methionine is essential for growth. Diet should therefore be individualized using growth, essential amino acids, methionine, SAH/SAM, liver function, CK, development, and imaging—not methionine concentration alone (pinto2024asymptomaticpediatricpresentation pages 8-9).

### Supplements

Creatine and phosphatidylcholine have been used to bypass high methyl-demand biosynthetic pathways; N-acetylcysteine has been considered to support glutathione/oxidative-stress handling. Evidence consists of small uncontrolled case reports, and long-term benefit or adverse-event rates are unknown. The 2024 family declined these supplements because the children were asymptomatic and evidence was limited (pinto2024asymptomaticpediatricpresentation pages 8-9).

### Liver transplantation

Transplantation replaces a major source of systemic AHCY activity. A severely affected child resistant to diet reportedly showed normalization of metabolites and improvement in growth, psychomotor, and cognitive outcomes after transplantation at approximately 40 months. It remains a high-risk, non-randomized intervention; indications in mild disease are unresolved, and extrahepatic muscle disease may not be fully corrected (stender2015adultonsetliverdisease pages 6-8, vizan2021functionalandpathological pages 7-8).

### Supportive care and surveillance

Management should involve metabolic medicine, hepatology, neurology, dietetics, physiotherapy, occupational/speech therapy, developmental services, and genetic counseling. Treat coagulopathy, nutritional deficiency, seizures, feeding problems, and liver complications conventionally. Monitor growth, neurodevelopment, CK/strength, liver synthetic function, fibrosis, ultrasound and AFP; use brain and muscle MRI selectively.

Suggested NCIT intervention concepts are dietary therapy/methionine restriction, amino-acid formula, creatine supplementation, phosphatidylcholine supplementation, N-acetylcysteine, physical therapy, and liver transplantation. No approved gene replacement, CRISPR, RNA, cell, targeted small-molecule, or immunotherapy exists. The ClinicalTrials.gov search found **no clearly disease-specific interventional trial**; retrieved broad observational/newborn-screening records did not provide explicit AHCY-deficiency enrollment evidence.

## 13. Prevention

There is no lifestyle or vaccine-based primary prevention. Effective genetic prevention consists of carrier testing for relatives, reproductive counseling, partner testing, prenatal diagnosis, and preimplantation genetic testing when familial variants are known. Cascade testing can identify asymptomatic biallelic relatives before irreversible liver, muscle, or white-matter injury.

Secondary prevention is early biochemical/genetic diagnosis followed by monitored dietary intervention and organ surveillance. Tertiary prevention includes rehabilitation, avoidance of malnutrition, management of liver failure, and HCC surveillance. Population biochemical newborn screening is not currently recommended specifically for SAHHD; targeted testing is reasonable in affected families and populations in which p.Arg49His enrichment is confirmed.

## 14. Other species and natural disease

No naturally occurring veterinary syndrome confidently equivalent to human SAHHD was identified, and there is no zoonotic relevance. AHCY is evolutionarily conserved across eukaryotes, and complete loss is developmentally deleterious in several organisms. Suggested taxa for model annotation include *Danio rerio* (NCBI Taxon 7955), *Mus musculus* (10090), and *Caenorhabditis elegans* (6239). Ortholog identifiers should be retrieved directly from current NCBI Gene/Alliance releases before database ingestion.

## 15. Model organisms

* **Zebrafish ahcy/ducttrip mutant:** develops hepatic steatosis, TNF-dependent liver degeneration, and exocrine-pancreas/liver developmental abnormalities. It recapitulates liver injury and methionine-cycle disruption but not the full human neurodevelopmental/myopathy spectrum.
* **Mouse Ahcy knockout:** homozygous deletion is embryonic lethal before approximately E9.5, demonstrating essential developmental function but limiting its utility for postnatal disease; conditional/hypomorphic models are needed (vizan2021functionalandpathological pages 4-5).
* **C. elegans partial deficiency:** a 2023 knock-in **AHCY-1 p.Tyr145Cys**, corresponding to human p.Tyr143Cys, lowered SAM, moderately increased SAH, and extended lifespan through AMPK, VRK-1, and DAF-16. This is a useful methionine/aging model but does not reproduce human liver or muscle anatomy (DOI: https://doi.org/10.1038/s41514-023-00125-1).
* **Cell models:** patient-derived cells and AHCY-knockdown HEK293, HepG2, SW480, and mouse embryonic fibroblasts support studies of methylation, DNA damage, proliferation, Wnt/LEF1 signaling, and adenosine biology. Cancer-cell backgrounds and acute knockdown are important limitations (vizan2021functionalandpathological pages 4-5, vizan2021functionalandpathological pages 7-8).

No validated patient iPSC, organoid, single-cell, spatial-transcriptomic, or CRISPR therapeutic-screen platform was established in the retrieved disease-specific literature.

## Current expert interpretation and evidence gaps

The authoritative consensus view is that SAHHD is a multisystem inherited methylation disorder in which **SAH and SAM measurement is essential**, methionine restriction is biologically rational but incompletely effective, and management must be individualized. The 2024 cases materially broaden this view: apparently well children may harbor severe biochemical abnormalities and subtle reversible brain disease, while adult relatives demonstrate potentially fatal delayed complications (pinto2024asymptomaticpediatricpresentation pages 1-2, pinto2024asymptomaticpediatricpresentation pages 9-10, pinto2024asymptomaticpediatricpresentation pages 2-2).

Principal unresolved questions are true prevalence, penetrance of p.Arg49His, complete variant-level ACMG classification, natural history, optimal methionine targets, benefit of creatine/phosphatidylcholine/N-acetylcysteine, transplantation timing, HCC risk, reliable pharmacodynamic biomarkers, quality of life, and feasibility of gene or mRNA replacement. No controlled trial, registry-scale cohort, validated clinical outcome assessment, or disease-specific multi-omics atlas is available.

### Key cited publications and URLs

* Pinto PL et al. **Asymptomatic pediatric presentation of S-adenosylhomocysteine hydrolase deficiency.** *JIMD Reports*. Published September 2024. https://doi.org/10.1002/jmd2.12449 (pinto2024asymptomaticpediatricpresentation pages 1-2)
* Stender S et al. **Adult-onset liver disease and hepatocellular carcinoma in S-adenosylhomocysteine hydrolase deficiency.** *Molecular Genetics and Metabolism*. December 2015. https://doi.org/10.1016/j.ymgme.2015.10.009 (stender2015adultonsetliverdisease pages 5-6, stender2015adultonsetliverdisease pages 6-8)
* Motzek A et al. **Abnormal hypermethylation at imprinting control regions in patients with AHCY deficiency.** *PLoS ONE*. March 2016. https://doi.org/10.1371/journal.pone.0151261 (motzek2016abnormalhypermethylationat pages 8-9)
* Vizán P et al. **Functional and pathological roles of AHCY.** *Frontiers in Cell and Developmental Biology*. March 2021. https://doi.org/10.3389/fcell.2021.654344 (vizan2021functionalandpathological pages 4-5, vizan2021functionalandpathological pages 7-8)

PMIDs were not consistently present in the retrieved full-text metadata and therefore are not supplied where they could not be verified; DOI URLs are provided to avoid introducing incorrect identifiers.

References

1. (pinto2024asymptomaticpediatricpresentation pages 1-2): Patrícia Lipari Pinto, Marjorie Dixon, Sniya Sudhakar, Ivo Baric, and Julien Baruteau. Asymptomatic pediatric presentation of s‐adenosylhomocysteine hydrolase deficiency. JIMD Reports, 65:371-381, Sep 2024. URL: https://doi.org/10.1002/jmd2.12449, doi:10.1002/jmd2.12449. This article has 2 citations and is from a peer-reviewed journal.

2. (pinto2024asymptomaticpediatricpresentation pages 7-7): Patrícia Lipari Pinto, Marjorie Dixon, Sniya Sudhakar, Ivo Baric, and Julien Baruteau. Asymptomatic pediatric presentation of s‐adenosylhomocysteine hydrolase deficiency. JIMD Reports, 65:371-381, Sep 2024. URL: https://doi.org/10.1002/jmd2.12449, doi:10.1002/jmd2.12449. This article has 2 citations and is from a peer-reviewed journal.

3. (pinto2024asymptomaticpediatricpresentation pages 2-2): Patrícia Lipari Pinto, Marjorie Dixon, Sniya Sudhakar, Ivo Baric, and Julien Baruteau. Asymptomatic pediatric presentation of s‐adenosylhomocysteine hydrolase deficiency. JIMD Reports, 65:371-381, Sep 2024. URL: https://doi.org/10.1002/jmd2.12449, doi:10.1002/jmd2.12449. This article has 2 citations and is from a peer-reviewed journal.

4. (pinto2024asymptomaticpediatricpresentation pages 9-10): Patrícia Lipari Pinto, Marjorie Dixon, Sniya Sudhakar, Ivo Baric, and Julien Baruteau. Asymptomatic pediatric presentation of s‐adenosylhomocysteine hydrolase deficiency. JIMD Reports, 65:371-381, Sep 2024. URL: https://doi.org/10.1002/jmd2.12449, doi:10.1002/jmd2.12449. This article has 2 citations and is from a peer-reviewed journal.

5. (pinto2024asymptomaticpediatricpresentation pages 2-3): Patrícia Lipari Pinto, Marjorie Dixon, Sniya Sudhakar, Ivo Baric, and Julien Baruteau. Asymptomatic pediatric presentation of s‐adenosylhomocysteine hydrolase deficiency. JIMD Reports, 65:371-381, Sep 2024. URL: https://doi.org/10.1002/jmd2.12449, doi:10.1002/jmd2.12449. This article has 2 citations and is from a peer-reviewed journal.

6. (stender2015adultonsetliverdisease pages 5-6): Stefan Stender, Rima S. Chakrabarti, Chao Xing, Garrett Gotway, Jonathan C. Cohen, and Helen H. Hobbs. Adult-onset liver disease and hepatocellular carcinoma in s-adenosylhomocysteine hydrolase deficiency. Molecular genetics and metabolism, 116 4:269-74, Dec 2015. URL: https://doi.org/10.1016/j.ymgme.2015.10.009, doi:10.1016/j.ymgme.2015.10.009. This article has 52 citations and is from a peer-reviewed journal.

7. (vizan2021functionalandpathological pages 4-5): Pedro Vizán, Luciano Di Croce, and Sergi Aranda. Functional and pathological roles of ahcy. Frontiers in Cell and Developmental Biology, Mar 2021. URL: https://doi.org/10.3389/fcell.2021.654344, doi:10.3389/fcell.2021.654344. This article has 119 citations.

8. (stender2015adultonsetliverdisease pages 6-8): Stefan Stender, Rima S. Chakrabarti, Chao Xing, Garrett Gotway, Jonathan C. Cohen, and Helen H. Hobbs. Adult-onset liver disease and hepatocellular carcinoma in s-adenosylhomocysteine hydrolase deficiency. Molecular genetics and metabolism, 116 4:269-74, Dec 2015. URL: https://doi.org/10.1016/j.ymgme.2015.10.009, doi:10.1016/j.ymgme.2015.10.009. This article has 52 citations and is from a peer-reviewed journal.

9. (motzek2016abnormalhypermethylationat pages 8-9): Antje Motzek, Jelena Knežević, Olivier J. Switzeny, Alexis Cooper, Ivo Barić, Robert Beluzić, Kevin A. Strauss, Erik G. Puffenberger, S. Harvey Mudd, Oliver Vugrek, and Ulrich Zechner. Abnormal hypermethylation at imprinting control regions in patients with s-adenosylhomocysteine hydrolase (ahcy) deficiency. PLoS ONE, 11:e0151261, Mar 2016. URL: https://doi.org/10.1371/journal.pone.0151261, doi:10.1371/journal.pone.0151261. This article has 19 citations and is from a peer-reviewed journal.

10. (pinto2024asymptomaticpediatricpresentation pages 4-4): Patrícia Lipari Pinto, Marjorie Dixon, Sniya Sudhakar, Ivo Baric, and Julien Baruteau. Asymptomatic pediatric presentation of s‐adenosylhomocysteine hydrolase deficiency. JIMD Reports, 65:371-381, Sep 2024. URL: https://doi.org/10.1002/jmd2.12449, doi:10.1002/jmd2.12449. This article has 2 citations and is from a peer-reviewed journal.

11. (pinto2024asymptomaticpediatricpresentation pages 8-9): Patrícia Lipari Pinto, Marjorie Dixon, Sniya Sudhakar, Ivo Baric, and Julien Baruteau. Asymptomatic pediatric presentation of s‐adenosylhomocysteine hydrolase deficiency. JIMD Reports, 65:371-381, Sep 2024. URL: https://doi.org/10.1002/jmd2.12449, doi:10.1002/jmd2.12449. This article has 2 citations and is from a peer-reviewed journal.

12. (stender2015adultonsetliverdisease pages 16-16): Stefan Stender, Rima S. Chakrabarti, Chao Xing, Garrett Gotway, Jonathan C. Cohen, and Helen H. Hobbs. Adult-onset liver disease and hepatocellular carcinoma in s-adenosylhomocysteine hydrolase deficiency. Molecular genetics and metabolism, 116 4:269-74, Dec 2015. URL: https://doi.org/10.1016/j.ymgme.2015.10.009, doi:10.1016/j.ymgme.2015.10.009. This article has 52 citations and is from a peer-reviewed journal.

13. (vizan2021functionalandpathological pages 7-8): Pedro Vizán, Luciano Di Croce, and Sergi Aranda. Functional and pathological roles of ahcy. Frontiers in Cell and Developmental Biology, Mar 2021. URL: https://doi.org/10.3389/fcell.2021.654344, doi:10.3389/fcell.2021.654344. This article has 119 citations.

## Artifacts

- [Edison artifact artifact-00](AHCY_Deficiency-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.
