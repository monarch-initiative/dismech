---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-19T23:16:58.757220'
end_time: '2026-08-19T23:23:17.034156'
duration_seconds: 378.28
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Purine nucleoside phosphorylase deficiency
  mondo_id: ''
  category: Inborn Error of Metabolism
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 12
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 0
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Purine_Nucleoside_Phosphorylase_Deficiency-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Purine nucleoside phosphorylase deficiency
- **MONDO ID:**  (if available)
- **Category:** Inborn Error of Metabolism

## Research Objectives

Please provide a comprehensive research report on **Purine nucleoside phosphorylase deficiency** covering all of the
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
- **Disease Name:** Purine nucleoside phosphorylase deficiency
- **MONDO ID:**  (if available)
- **Category:** Inborn Error of Metabolism

## Research Objectives

Please provide a comprehensive research report on **Purine nucleoside phosphorylase deficiency** covering all of the
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


# Purine nucleoside phosphorylase deficiency: comprehensive disease-characteristics report

**Scope and evidence note.** This report integrates disease-level resources, recent reviews, human case-series evidence, and mechanistic mouse/in-vitro studies. Because PNP deficiency is exceptionally rare, many estimates derive from aggregated published cases rather than population registries. Exact variant frequencies, penetrance estimates, quality-of-life scores, and disease-specific survival curves remain unavailable. The most informative recent sources retrieved were Camici et al. (published June 2023; DOI [10.3390/metabo13070787](https://doi.org/10.3390/metabo13070787)) and Abt et al. (published August 2022; JCI 132:e160852; DOI [10.1172/JCI160852](https://doi.org/10.1172/JCI160852)). (camici2023inbornerrorsof pages 24-26, abt2022purinenucleosidephosphorylase pages 1-2)

## Executive summary

Purine nucleoside phosphorylase (PNP) deficiency is an autosomal-recessive inborn error of purine metabolism and inborn error of immunity caused by biallelic loss-of-function variants in **PNP**. Failure to catabolize inosine-, guanosine-, and deoxyguanosine-related substrates causes nucleoside accumulation, intracellular dGTP excess, nucleotide-pool imbalance, and selective injury to developing T cells. Patients consequently develop severe T-cell lymphopenia/combined immunodeficiency, recurrent or opportunistic infection, neurologic impairment, and paradoxical autoimmunity. Neurologic manifestations occur in approximately two-thirds and autoimmune disease in approximately one-third of reported patients; onset is usually between 4 months and 6 years, but expression is highly variable. (camici2023inbornerrorsof pages 24-26)

Biochemical diagnosis rests on elevated inosine/guanosine—and often deoxyguanosine—in blood or urine, low uric acid, and markedly reduced PNP enzyme activity; molecular confirmation requires identifying pathogenic variants on both alleles. Allogeneic hematopoietic stem-cell transplantation (HSCT) is the established definitive treatment for immune disease. It can restore immunity and prevent further infections, but pre-existing neurologic deficits may persist, making presymptomatic diagnosis and early transplantation important. (camici2023inbornerrorsof pages 24-26, camici2023inbornerrorsof pages 45-46)

| domain | high-confidence annotation | suggested ontology/identifier | evidence caveat |
|---|---|---|---|
| Disease entity | Purine nucleoside phosphorylase deficiency; rare inborn error of purine metabolism with immunodeficiency and neurologic/autoimmune manifestations | MONDO:0013171; category suggestion: inborn error of metabolism / inborn error of immunity (OpenTargets Search: purine nucleoside phosphorylase deficiency-PNP, camici2023inbornerrorsof pages 24-26) | MONDO supported by OpenTargets context; some classifications differ between metabolic and immunologic taxonomies |
| Synonyms | PNP deficiency; purine nucleoside phosphorylase defect; PNP-deficient SCID/combined immunodeficiency | MeSH/OMIM/Orphanet mapping suggestion only; exact IDs not confirmed here (camici2023inbornerrorsof pages 24-26, camici2023inbornerrorsof pages 45-46) | Exact synonym lists and external IDs should be verified in OMIM/Orphanet/MeSH |
| Causal gene | Biallelic pathogenic variants in PNP cause disease | PNP; Ensembl: ENSG00000198805; HGNC symbol: PNP (OpenTargets Search: purine nucleoside phosphorylase deficiency-PNP, camici2023inbornerrorsof pages 24-26) | Gene-disease link is high confidence; transcript-level reference not specified here |
| Inheritance | Autosomal recessive loss-of-function disorder | Inheritance suggestion: HP term for autosomal recessive inheritance; gene mechanism suggestion: loss of function (camici2023inbornerrorsof pages 24-26, abt2022purinenucleosidephosphorylase pages 1-2) | Exact HPO inheritance ID not supplied to avoid invention |
| Core biochemical defect | Deficiency of purine nucleoside phosphorylase activity impairs phosphorolysis of inosine/guanosine and deoxy forms, causing toxic purine metabolite accumulation | GO suggestion: purine nucleoside phosphorylase activity; Reactome/KEGG suggestion: purine metabolism / salvage pathway (camici2023inbornerrorsof pages 24-26, shanta2020purinenucleosidephosphorylase pages 1-2) | Exact GO/Reactome IDs not confirmed here |
| Key metabolites/biomarkers | Elevated inosine and guanosine in blood/urine; elevated guanosine and deoxyguanosine reported; reduced uric acid | CHEBI suggestions: inosine, guanosine, deoxyguanosine, uric acid (camici2023inbornerrorsof pages 24-26, abt2022purinenucleosidephosphorylase pages 1-2) | Exact CHEBI IDs not provided; biomarker patterns may vary by assay and timing |
| Mechanistic toxic intermediate | Deoxyguanosine is phosphorylated to dGTP, producing dNTP imbalance and ribonucleotide reductase inhibition with lymphocyte toxicity | GO suggestions: apoptotic process, mitochondrial apoptotic pathway, nucleotide metabolic process (camici2023inbornerrorsof pages 24-26, shanta2020purinenucleosidephosphorylase pages 1-2) | dGTP mechanism is strongly supported, but exact downstream pathways vary by model/system |
| Immune phenotype | Profound T-cell lymphopenia/combined immunodeficiency with recurrent severe infections; B-cell compartment may be less affected than T cells | HPO suggestions: T-cell lymphopenia, combined immunodeficiency, recurrent infections, immunodeficiency; NCIT suggestion: Severe Combined Immunodeficiency (camici2023inbornerrorsof pages 24-26, camici2023inbornerrorsof pages 45-46, shanta2020purinenucleosidephosphorylase pages 1-2) | Exact HPO/NCIT IDs not confirmed; some patients are described as SCID, others as CID/leaky SCID |
| Neurologic phenotype | Neurologic manifestations reported in approximately two-thirds of cases; includes ataxia, developmental delay, intellectual disability, spasticity/paraplegia in some reports | HPO suggestions: ataxia, developmental delay, intellectual disability, spastic paraplegia (camici2023inbornerrorsof pages 24-26, camici2023inbornerrorsof pages 45-46) | Frequency estimate is from review-level synthesis; patient-level prevalence varies |
| Autoimmune phenotype | Autoimmune manifestations reported in approximately one-third of cases; examples include immune thrombocytopenia, thyroiditis, lupus/SLE-like disease, autoimmune hemolytic anemia, inflammatory arthritis/MAS-like presentations | HPO suggestions: autoimmune thrombocytopenia, thyroiditis, systemic lupus erythematosus, autoimmune hemolytic anemia; disease feature suggestion: autoimmunity (camici2023inbornerrorsof pages 24-26, abt2022purinenucleosidephosphorylase pages 1-2, camici2023inbornerrorsof pages 45-46) | Frequency estimate is approximate; specific autoimmune diagnoses are heterogeneous and often case-based |
| Age at onset / course | Typically presents from about 4 months to 6 years; severity is variable | HPO suggestions: infantile onset / childhood onset (camici2023inbornerrorsof pages 24-26) | Exact onset distribution is not well quantified due to rarity |
| Major affected cells | Thymocytes/T-cell progenitors are especially vulnerable; B lymphocytes and macrophages are implicated in autoimmunity/TLR7 signaling | CL suggestions: thymocyte, T-cell progenitor, T lymphocyte, B lymphocyte, macrophage (abt2022purinenucleosidephosphorylase pages 1-2, shanta2020purinenucleosidephosphorylase pages 1-2) | Exact CL IDs not confirmed; evidence spans human, mouse, and mechanistic systems |
| Major anatomy | Primary involvement of immune system, especially thymus and peripheral lymphoid tissues; nervous system involvement is common | UBERON suggestions: thymus, spleen, lymph node, peripheral blood, brain/nervous system (camici2023inbornerrorsof pages 24-26, abt2022purinenucleosidephosphorylase pages 1-2) | Exact UBERON IDs not confirmed; organ involvement is inferred from phenotype and model data |
| Upstream/downstream pathway annotation | Upstream: PNP loss in purine salvage/catabolism. Downstream: purine nucleoside accumulation, dGTP excess, mitochondrial apoptosis, T-cell depletion; separate checkpoint links guanosine metabolites to TLR7-associated autoimmunity | GO suggestions: purine nucleoside metabolic process, intrinsic apoptotic signaling pathway, toll-like receptor signaling pathway, lymphocyte differentiation (abt2022purinenucleosidephosphorylase pages 1-2, shanta2020purinenucleosidephosphorylase pages 1-2) | TLR7 checkpoint evidence is particularly strengthened by 2022 mechanistic work and model systems |
| Diagnosis | Diagnostic workup includes enzyme assay, metabolite profiling, and molecular testing of PNP; dried-blood-spot tandem mass spectrometry has been reported for early diagnosis/newborn detection | Diagnostic test suggestion: PNP enzyme activity assay; metabolomics/MS-MS; single-gene or panel sequencing of PNP (camici2023inbornerrorsof pages 24-26, camici2023inbornerrorsof pages 45-46) | Exact assay thresholds and sensitivity/specificity not available in retrieved evidence |
| Screening | Newborn screening is feasible using DBS tandem mass spectrometry, but not universally routine | Screening program suggestion: newborn screening for SCID/purine disorders (camici2023inbornerrorsof pages 24-26, camici2023inbornerrorsof pages 45-46) | Implementation is jurisdiction-dependent; broad population performance metrics not available here |
| Definitive treatment | Hematopoietic stem cell transplantation (HSCT) is the only established curative therapy for immune reconstitution | NCIT suggestion: Hematopoietic Stem Cell Transplantation / Bone Marrow Transplantation (camici2023inbornerrorsof pages 24-26) | Strong consensus on immune benefit; exact NCIT code not confirmed |
| Treatment outcome caveat | HSCT generally restores immune function and reduces infections, but neurologic recovery is incomplete/variable | Outcome annotation suggestion: immune reconstitution; persistent neurodevelopmental impairment possible (camici2023inbornerrorsof pages 24-26, camici2023inbornerrorsof pages 45-46) | Disease-specific long-term survival percentages were not available in retrieved evidence |
| Residual activity / genotype-phenotype note | Near-normal immune and neurologic development may require roughly 8-11% residual PNP activity | Functional evidence annotation suggestion: residual enzyme activity modifier (camici2023inbornerrorsof pages 24-26) | Review-derived estimate; should be confirmed against original patient series before KB hard-coding |
| Model organism | PNP-deficient/PNP-knockout mice support thymic/T-cell toxicity mechanisms and autoimmune checkpoint biology but incompletely recapitulate human disease | Model suggestion: mouse Pnp knockout / deficient mouse (camici2023inbornerrorsof pages 24-26, abt2022purinenucleosidephosphorylase pages 1-2) | Mouse models show important limitations, including partial mismatch with human thymic/T-cell phenotype |


*Table: This table summarizes high-confidence, knowledge-base-ready annotations for purine nucleoside phosphorylase deficiency, including disease identity, gene, mechanism, phenotypes, diagnostics, and treatment. Ontology mappings are labeled as suggestions where exact identifiers were not confirmed in the available evidence.*

## 1. Disease information

### Definition and classification

PNP deficiency is both an **inborn error of metabolism**—specifically purine salvage/catabolism—and an **inborn error of immunity**, commonly classified clinically as combined immunodeficiency or SCID-like disease. Alternative names include **PNP deficiency**, **purine nucleoside phosphorylase defect**, **PNP-deficient combined immunodeficiency**, and **PNP-deficient SCID**. The historical description emphasized severe T-cell deficiency with relatively preserved B-cell numbers, although B-cell function and immune regulation can also be abnormal. (camici2023inbornerrorsof pages 24-26, camici2023inbornerrorsof pages 45-46)

**Identifiers:**

- **MONDO:** MONDO:0013171, directly linked to PNP/ENSG00000198805 in Open Targets. (OpenTargets Search: purine nucleoside phosphorylase deficiency-PNP)
- **Gene:** PNP; Ensembl **ENSG00000198805**. (OpenTargets Search: purine nucleoside phosphorylase deficiency-PNP)
- **OMIM:** commonly catalogued as PNP gene **164050** and immunodeficiency due to PNP deficiency **613179**; these numbers should be verified directly in OMIM before production ingestion.
- **Orphanet/MeSH:** disease entries exist, but exact identifiers were not independently confirmed in the retrieved full-text evidence.
- **ICD-10/ICD-11:** there is no widely used disease-specific billing code; cases are generally coded under combined/severe combined immunodeficiency or other specified disorders of purine metabolism.

The evidence is predominantly **aggregated disease-level literature**, supplemented by small cohorts and individual cases—not EHR-derived patient-level data.

## 2. Etiology, risk, and protective factors

The sole established primary cause is **biallelic germline loss of PNP function**. Inheritance is autosomal recessive: each sibling of two carrier parents has a 25% probability of being affected, 50% probability of being a carrier, and 25% probability of inheriting neither familial variant. PNP is the only high-confidence associated target in Open Targets for MONDO:0013171. (OpenTargets Search: purine nucleoside phosphorylase deficiency-PNP, camici2023inbornerrorsof pages 24-26)

Reported pathogenic alleles include missense, nonsense, frameshift, and splice-altering variants. Their common consequence is absent or severely reduced enzyme activity. No robust disease-wide genotype–phenotype relationship has been established. Residual activity is biologically important: review-level evidence suggests approximately **8–11% activity** may permit near-normal immune and neurologic development. (camici2023inbornerrorsof pages 24-26)

No environmental, dietary, lifestyle, occupational, infectious, sex-specific, or polygenic factor is known to cause the disorder. Infections are consequences and clinical stressors, not etiologic agents. Consanguinity and an affected family history increase reproductive risk by increasing the probability that both parents carry the same rare allele. No validated protective allele, modifier gene, epigenetic signature, or gene–environment interaction is established. Avoiding infection may reduce morbidity but cannot prevent the biochemical disease.

## 3. Phenotypes

### Immune and infectious manifestations

The central laboratory phenotype is **progressive T-cell lymphopenia with profound T-cell dysfunction**. Clinical manifestations include recurrent bacterial, viral, fungal, and opportunistic infections, chronic respiratory or gastrointestinal infection, and failure to thrive. Severity ranges from SCID in infancy to later-onset combined immunodeficiency. Suggested HPO annotations are *Immunodeficiency*, *Combined immunodeficiency*, *T-cell lymphopenia*, *Recurrent respiratory infections*, *Opportunistic infection*, *Chronic diarrhea*, and *Failure to thrive*. (camici2023inbornerrorsof pages 24-26, shanta2020purinenucleosidephosphorylase pages 1-2)

### Neurologic and developmental manifestations

Approximately **two-thirds** of reported patients have neurologic disease, which can precede recognized infections. Manifestations include global developmental delay, intellectual disability, ataxia, hypotonia or spasticity, motor dysfunction, and occasionally spastic paraplegia. Severity and progression are variable; established injury may not reverse after HSCT. Suggested HPO terms include *Global developmental delay*, *Intellectual disability*, *Ataxia*, *Muscular hypotonia*, *Spasticity*, *Spastic paraplegia*, and *Abnormality of gait*. (camici2023inbornerrorsof pages 24-26, camici2023inbornerrorsof pages 45-46, shanta2020purinenucleosidephosphorylase pages 3-4)

### Autoimmunity, inflammation, and malignancy

Approximately **one-third** develop autoimmune manifestations, including immune thrombocytopenia, autoimmune hemolytic anemia, thyroiditis, lupus/SLE-like disease, inflammatory arthritis, and macrophage-activation-syndrome-like presentations. Lymphoma has been reported in late-onset disease. One mechanistically studied case showed IL-18 more than **400-fold elevated**, with high CXCL9, supporting IFN-γ-linked hyperinflammation, but this is not a validated diagnostic biomarker. Suggested HPO terms include *Autoimmunity*, *Thrombocytopenia*, *Autoimmune hemolytic anemia*, *Thyroiditis*, and *Systemic lupus erythematosus*. (abt2022purinenucleosidephosphorylase pages 1-2, camici2023inbornerrorsof pages 45-46, shanta2020purinenucleosidephosphorylase pages 3-4)

No validated PNP-specific EQ-5D, SF-36, PROMIS, or other quality-of-life dataset was found. Nevertheless, recurrent hospitalization, infection precautions, neurodevelopmental disability, mobility impairment, and transplant morbidity substantially affect schooling, independence, caregiver burden, and well-being.

## 4. Genetic and molecular information

**PNP** encodes purine nucleoside phosphorylase, a cytosolic homotrimeric enzyme that catalyzes reversible phosphorolysis of inosine, guanosine, deoxyinosine, and deoxyguanosine to corresponding purine bases plus ribose-1-phosphate or deoxyribose-1-phosphate. Disease alleles act through loss of function, not gain of function or dominant-negative activity. (shanta2020purinenucleosidephosphorylase pages 1-2)

Variants are constitutionally **germline** and usually inherited from heterozygous parents. Variant interpretation should follow ACMG/AMP criteria using segregation, rarity in gnomAD, enzyme activity, biochemical phenotype, RNA evidence for splice variants, and functional assays. A comprehensive current ClinVar/gnomAD variant table could not be reconstructed from the retrieved documents; therefore, no individual HGVS allele or population frequency should be hard-coded without direct database verification.

No confirmed modifier gene, recurrent chromosomal rearrangement, somatic driver, disease-specific methylation signature, or chromatin abnormality is known. CMA, karyotyping, and FISH are consequently not first-line tests unless a broader syndromic or copy-number diagnosis is suspected.

## 5. Environmental and infectious information

There are no demonstrated toxin, radiation, pollution, diet, smoking, alcohol, exercise, or occupational causes. Dietary purine restriction is not an established disease-modifying treatment because cellular purines derive mainly from de novo synthesis and nucleic-acid turnover, with dietary intake contributing only marginally. (camici2023inbornerrorsof pages 24-26)

Pathogens do not cause PNP deficiency. They exploit the resulting T-cell defect and drive morbidity. Exposure reduction, safe food and water practices, household infection control, and rapid treatment of fever are tertiary-prevention measures rather than etiologic interventions.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** biallelic PNP loss reduces phosphorolysis and recycling of purine nucleosides.
2. **Metabolic block:** inosine, guanosine, deoxyinosine, and especially deoxyguanosine accumulate; conversion toward hypoxanthine/guanine and ultimately uric acid falls.
3. **T-cell-toxic branch:** deoxyguanosine is phosphorylated by deoxycytidine kinase to dGTP, particularly in immature T cells, which have high kinase and relatively low dephosphorylating capacity.
4. **Cellular injury:** dGTP excess disturbs dNTP pools, inhibits ribonucleotide reductase, impairs DNA synthesis/repair, promotes DNA fragmentation and mitochondrial apoptosis.
5. **Tissue phenotype:** progressive thymocyte/T-cell-progenitor loss produces peripheral T-cell lymphopenia and infection susceptibility. (camici2023inbornerrorsof pages 24-26, shanta2020purinenucleosidephosphorylase pages 1-2)

A second checkpoint helps explain the apparent paradox of autoimmunity amid immunodeficiency. Mechanistic mouse and cellular work indicates that PNP restrains guanosine/deoxyguanosine-dependent **TLR7 signaling** in B cells and macrophages. PNP loss can therefore combine T-cell depletion with excessive innate/B-cell nucleic-acid sensing and lupus-like inflammation. Abt et al. summarize the phenotype as “profound T cell immunodeficiency and paradoxical autoimmunity.” (abt2022purinenucleosidephosphorylase pages 1-2)

Suggested GO biological-process terms include *purine nucleoside metabolic process*, *purine-containing compound salvage*, *deoxyribonucleotide metabolic process*, *ribonucleotide reductase regulation*, *intrinsic apoptotic signaling pathway*, *T-cell differentiation*, and *Toll-like receptor 7 signaling pathway*. Suggested cell types are thymocyte, T-cell progenitor, mature T lymphocyte, B lymphocyte, and macrophage. Exact GO and Cell Ontology identifiers should be validated before ingestion.

### Molecular profiling

The clinically useful molecular signature is metabolomic: high inosine/guanosine/deoxyguanosine and low uric acid. No reproducible disease-specific transcriptomic, proteomic, lipidomic, single-cell, spatial-transcriptomic, or integrated multi-omics atlas was identified. Elevated IL-18/CXCL9 is hypothesis-generating rather than validated. (camici2023inbornerrorsof pages 24-26, shanta2020purinenucleosidephosphorylase pages 3-4)

## 7. Anatomical structures affected

The **immune system** is primary, especially thymus, thymocytes/T-cell progenitors, peripheral blood T cells, spleen, lymph nodes, and bone marrow/hematopoietic progenitors. The **central nervous system** is a major nonimmune target, expressed through developmental, motor, cerebellar, and pyramidal abnormalities. Respiratory and gastrointestinal tissues are secondarily injured by recurrent infection; spleen and blood lineages can be affected by immune dysregulation or cytopenias. (camici2023inbornerrorsof pages 24-26, abt2022purinenucleosidephosphorylase pages 1-2)

Suggested UBERON mappings are thymus, bone marrow, spleen, lymph node, blood, brain, cerebellum, and spinal cord. Suggested GO cellular compartments include cytosol—the principal site of soluble PNP activity—and mitochondrion for downstream apoptotic signaling. Disease lateralization is not characteristic.

## 8. Temporal development and natural history

Typical recognized onset is **4 months to 6 years**, although residual-function disease may present later. The course is chronic and generally progressive without immune reconstitution: toxic metabolites accumulate, thymic injury and lymphopenia worsen, infections recur, and neurologic or autoimmune manifestations emerge variably. PNP-knockout mice likewise have relatively preserved T-cell production at birth followed by progressive thymic injury, supporting an early therapeutic window. (camici2023inbornerrorsof pages 24-26)

There are no validated stages. A practical clinical sequence is: presymptomatic biochemical/genetic disease; early lymphopenia or developmental abnormality; recurrent infection/combined immunodeficiency; and advanced multisystem disease with neurologic disability, autoimmunity, chronic infection, or malignancy. Remission without treatment is not expected. HSCT can induce durable immune remission but does not reliably reverse established neurologic damage. (camici2023inbornerrorsof pages 45-46, camici2023inbornerrorsof pages 24-26)

## 9. Inheritance and population

PNP deficiency is autosomal recessive, affects both sexes, and is worldwide. Consanguineous populations and founder families may show local enrichment, but no robust global prevalence, annual incidence, carrier frequency, ethnic distribution, or sex ratio is established. The published literature is too sparse and referral-biased for reliable cases-per-100,000 estimates.

Penetrance of two severe loss-of-function alleles appears high, but expressivity is variable and depends partly on residual activity. Genetic anticipation is not expected. Germline mosaicism has not emerged as a characteristic mechanism, although low-level parental mosaicism is theoretically possible. Carriers are generally asymptomatic because one functional allele supplies adequate activity.

## 10. Diagnostics and screening

### Recommended diagnostic workflow

1. **Suspect PNP deficiency** in a child with T-cell lymphopenia/CID plus developmental delay, ataxia/spasticity, autoimmunity, low uric acid, or consanguinity.
2. Perform CBC/differential, absolute lymphocyte count, CD3/CD4/CD8/CD19/NK enumeration, immunoglobulins, vaccine responses, lymphocyte proliferation, infection testing, and T-cell receptor excision circles where available.
3. Measure plasma/serum and urine purines by HPLC or LC-MS/MS. The characteristic pattern is elevated inosine and guanosine/deoxyguanosine with low serum/urine uric acid.
4. Confirm low or absent PNP enzyme activity in erythrocytes, leukocytes, or another validated specimen.
5. Confirm **biallelic pathogenic/likely pathogenic PNP variants** by sequencing with deletion/duplication analysis. (camici2023inbornerrorsof pages 24-26, camici2023inbornerrorsof pages 45-46)

A single-gene assay or comprehensive SCID/CID panel is appropriate when the phenotype is recognizable. WES/WGS is useful in atypical cases or when panel testing is negative, particularly for deep-intronic or structural variants. CMA, karyotype, FISH, mitochondrial sequencing, and repeat-expansion assays are not routine PNP tests.

### Differential diagnosis

Major alternatives include ADA deficiency, IL2RG/JAK3/IL7R-related SCID, RAG1/RAG2/DCLRE1C defects, AK2-related reticular dysgenesis, DOCK8 deficiency, ataxia-telangiectasia, and other metabolic neurologic disorders. PNP deficiency is distinguished by elevated guanosine/deoxyguanosine and inosine, low uric acid, deficient PNP activity, and biallelic PNP variants. Autoimmunity can misleadingly suggest primary rheumatic disease; recurrent infection or lymphopenia should prompt immunologic testing. (camici2023inbornerrorsof pages 45-46, shanta2020purinenucleosidephosphorylase pages 3-4)

### Screening

Dried-blood-spot tandem mass spectrometry can detect the purine signature and has been proposed for newborn diagnosis, but it is not universally incorporated into routine newborn panels. Standard TREC-based SCID screening may identify marked T-cell lymphopenia, although milder or evolving disease could be missed. Cascade testing of siblings and carrier testing of relatives are strongly indicated. (camici2023inbornerrorsof pages 24-26, camici2023inbornerrorsof pages 45-46)

## 11. Outcome and prognosis

Untreated severe disease carries high risks of life-threatening infection, progressive neurologic disability, autoimmunity, cytopenias, and occasional lymphoma. SCID broadly is fatal without immune reconstitution, but a reliable PNP-specific untreated median survival or 5-/10-year survival rate was not available. (abt2022purinenucleosidephosphorylase pages 1-2)

HSCT can restore immune function and produce infection-free survival, but neurodevelopmental outcome is heterogeneous; persistent delay despite successful transplantation is documented. Favorable prognostic features plausibly include early diagnosis, transplantation before severe infection or neurologic injury, good donor match, low pretransplant organ burden, and some residual enzyme activity. These have not been combined into a validated PNP-specific prognostic model. (camici2023inbornerrorsof pages 24-26, camici2023inbornerrorsof pages 45-46)

## 12. Treatment

### Definitive therapy

**Allogeneic HSCT** is the established curative treatment for the hematopoietic/immune defect. Donor selection, conditioning intensity, graft source, and graft-versus-host-disease prophylaxis should be individualized at an experienced primary-immunodeficiency transplant center. Immune reconstitution and freedom from recurrent infection are expected goals; neurologic recovery cannot be assured. Suggested NCIt interventions are *Hematopoietic Stem Cell Transplantation*, *Bone Marrow Transplantation*, and *Allogeneic Stem Cell Transplantation*. (camici2023inbornerrorsof pages 24-26)

### Supportive management

Before reconstitution, management generally follows SCID/CID principles: antimicrobial prophylaxis, aggressive organism-directed treatment, immunoglobulin replacement when humoral function is inadequate, CMV-safe/irradiated blood products, nutritional support, and physical, occupational, speech, and neurodevelopmental therapies. Live vaccines should be avoided in significantly immunodeficient patients. Autoimmune disease requires specialist-directed immunomodulation balanced against infection risk.

No drug corrects inherited PNP deficiency. **Forodesine and ulodesine are PNP inhibitors**, studied to suppress or modulate immune cells in cancer, psoriasis, or gout; they mechanistically mimic aspects of PNP loss and are not treatments for this deficiency. (shanta2020purinenucleosidephosphorylase pages 1-2)

Gene replacement, gene editing, mRNA/RNA therapy, and enzyme/protein replacement remain experimental concepts. In-vitro delivery of PNP protein and retroviral correction models demonstrate feasibility, but no approved PNP-specific product was identified. No established pharmacogenomic guideline exists.

## 13. Prevention

Primary prevention by lifestyle or vaccination is impossible because the disease is inherited. Effective reproductive prevention includes genetic counseling, parental carrier confirmation, cascade testing, prenatal diagnosis, and preimplantation genetic testing for a known familial genotype.

Secondary prevention consists of newborn/TREC or metabolite screening where available, prompt evaluation of an affected sibling, and early HSCT before infection and neurologic damage. Tertiary prevention includes antimicrobial prophylaxis, immunoglobulin replacement when indicated, avoidance of live vaccines and unsafe blood products, rapid infection treatment, neurologic rehabilitation, and malignancy/autoimmunity surveillance. (camici2023inbornerrorsof pages 24-26, camici2023inbornerrorsof pages 45-46)

Inactivated vaccines may be ineffective before immune reconstitution; vaccination after HSCT should follow transplant-team schedules. Household contacts should be appropriately immunized, with live-vaccine exposure precautions determined by the immunology team.

## 14. Other species and naturally occurring disease

No well-established naturally occurring veterinary analogue in a specific companion-animal breed was identified. PNP orthologues are widely conserved among vertebrates, but experimental knockout/deficient animals should not be confused with spontaneous natural disease. There is no infectious transmission, zoonotic potential, or cross-species contagion.

## 15. Model organisms and experimental systems

**Mouse Pnp-deficiency/knockout models** reproduce toxic purine accumulation and progressive thymocyte abnormalities and have been used to investigate T-cell development, dGTP toxicity, and TLR7-associated autoimmunity. Some models develop pancytopenia, massive splenomegaly, and premature death. However, they incompletely reproduce human disease: one model had only minor thymic defects and largely preserved peripheral T-cell compartments, so therapeutic effects cannot be extrapolated without human confirmation. (camici2023inbornerrorsof pages 24-26, abt2022purinenucleosidephosphorylase pages 1-2)

Cellular systems include PNP-deficient lymphocytes, thymocyte cultures, gene-corrected T-cell lines, and pharmacologic PNP inhibition. They are useful for enzyme kinetics, metabolite flux, synthetic interactions involving deoxycytidine kinase/SAMHD1, apoptosis, and gene-replacement proof of concept, but cannot model neurodevelopment or whole-body immune regulation.

## Recent developments and current implementation

- **2023 metabolic synthesis:** Camici et al. consolidated the estimate that neurologic disease affects about two-thirds and autoimmunity about one-third, highlighted DBS-MS screening, and emphasized that HSCT restores immunity while neurologic benefit remains uncertain. The authors’ abstract states that purine dysmetabolism can be accompanied by “devastating symptoms” and that some manifestations still have “no explanation or therapy.” (camici2023inbornerrorsof pages 24-26)
- **Mechanistic advance:** Abt et al. established dual PNP-dependent checkpoints—dGTP-associated T-cell toxicity and guanosine/TLR7-associated immune activation—providing a coherent explanation for immunodeficiency coexisting with autoimmunity. (abt2022purinenucleosidephosphorylase pages 1-2)
- **Real-world diagnostics:** HPLC/LC-MS/MS metabolite testing, enzyme assays, immunophenotyping, and molecular sequencing are clinically implementable; DBS tandem-MS offers a potential presymptomatic screening route. (camici2023inbornerrorsof pages 24-26, camici2023inbornerrorsof pages 45-46)
- **Clinical research:** A ClinicalTrials.gov search identified the recruiting NIH observational natural-history protocol **NCT06092346**, designed to study clinical, genomic, pharmacologic, laboratory, and dietary determinants across purine and pyrimidine disorders. No active PNP-specific interventional gene- or enzyme-therapy trial was identified in the retrieved registry results.

## Evidence gaps and curation cautions

The field lacks a prospective international registry with standardized genotype, residual enzyme activity, infection burden, neurodevelopmental testing, transplant regimen, and long-term outcome. Published frequencies are vulnerable to survival and ascertainment bias. Exact individual variant classifications and gnomAD frequencies require direct current ClinVar/gnomAD review. Disease-specific QoL instruments, validated prognostic biomarkers, controlled treatment-response rates, and single-cell/spatial multi-omics datasets are absent. Ontology labels in the table are therefore proposed mappings rather than definitive identifier assignments unless explicitly stated.

References

1. (camici2023inbornerrorsof pages 24-26): Marcella Camici, Mercedes Garcia-Gil, Simone Allegrini, Rossana Pesi, Giulia Bernardini, Vanna Micheli, and Maria Grazia Tozzi. Inborn errors of purine salvage and catabolism. Metabolites, 13:787, Jun 2023. URL: https://doi.org/10.3390/metabo13070787, doi:10.3390/metabo13070787. This article has 27 citations.

2. (abt2022purinenucleosidephosphorylase pages 1-2): Evan R. Abt, Khalid Rashid, Thuc M. Le, Suwen Li, Hailey R. Lee, Vincent Lok, Luyi Li, Amanda L. Creech, Amanda N. Labora, Hanna K. Mandl, Alex K. Lam, Arthur Cho, Valerie Rezek, Nanping Wu, Gabriel Abril-Rodriguez, Ethan W. Rosser, Steven D. Mittelman, Willy Hugo, Thomas Mehrling, Shanta Bantia, Antoni Ribas, Timothy R. Donahue, Gay M. Crooks, Ting-Ting Wu, and Caius G. Radu. Purine nucleoside phosphorylase enables dual metabolic checkpoints that prevent t cell immunodeficiency and tlr7-associated autoimmunity. Journal of Clinical Investigation, Aug 2022. URL: https://doi.org/10.1172/jci160852, doi:10.1172/jci160852. This article has 45 citations and is from a highest quality peer-reviewed journal.

3. (camici2023inbornerrorsof pages 45-46): Marcella Camici, Mercedes Garcia-Gil, Simone Allegrini, Rossana Pesi, Giulia Bernardini, Vanna Micheli, and Maria Grazia Tozzi. Inborn errors of purine salvage and catabolism. Metabolites, 13:787, Jun 2023. URL: https://doi.org/10.3390/metabo13070787, doi:10.3390/metabo13070787. This article has 27 citations.

4. (OpenTargets Search: purine nucleoside phosphorylase deficiency-PNP): Open Targets Query (purine nucleoside phosphorylase deficiency-PNP, 8 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (shanta2020purinenucleosidephosphorylase pages 1-2): Bantia Shanta. Purine nucleoside phosphorylase inhibitors as novel immuno-oncology agent and vaccine adjuvant. International Journal of Immunology and Immunotherapy, Apr 2020. URL: https://doi.org/10.23937/2378-3672/1410043, doi:10.23937/2378-3672/1410043. This article has 12 citations.

6. (shanta2020purinenucleosidephosphorylase pages 3-4): Bantia Shanta. Purine nucleoside phosphorylase inhibitors as novel immuno-oncology agent and vaccine adjuvant. International Journal of Immunology and Immunotherapy, Apr 2020. URL: https://doi.org/10.23937/2378-3672/1410043, doi:10.23937/2378-3672/1410043. This article has 12 citations.

## Artifacts

- [Edison artifact artifact-00](Purine_Nucleoside_Phosphorylase_Deficiency-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 0 |
| Off topic | 0 |

All extracted references resolved successfully.