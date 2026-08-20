---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-20T04:17:49.023382'
end_time: '2026-08-20T04:26:19.118031'
duration_seconds: 510.09
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Giant Axonal Neuropathy 1
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 31
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 9
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Giant_Axonal_Neuropathy_1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Giant Axonal Neuropathy 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Giant Axonal Neuropathy 1** covering all of the
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
- **Disease Name:** Giant Axonal Neuropathy 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Giant Axonal Neuropathy 1** covering all of the
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


# Giant Axonal Neuropathy 1 (GAN1): comprehensive disease-characteristics report

**Scope and evidence note.** GAN is ultra-rare, so most clinical knowledge comes from aggregated disease resources, case series, a 2021 natural-history cohort, a 15-person German cohort published online in December 2024/print 2025, and one 14-participant phase 1 trial—not EHR-scale population data. Mechanistic evidence is largely from patient cells, engineered human cells, and animal models. Frequencies below should therefore not be interpreted as population prevalence.

| Topic | Key evidence-based findings | Identifiers / exact numbers | Evidence type | Source |
|---|---|---|---|---|
| Disease identity / inheritance | Giant axonal neuropathy (GAN; GAN1) is a rare pediatric neurodegenerative disorder affecting central and peripheral nervous systems; inheritance is autosomal recessive and due to biallelic loss-of-function variants in **GAN** encoding gigaxonin. Distinct early-onset severe and milder later-onset CMT-like phenotypes are described. | OMIM/MIM **#256850**; **GAN** at **16q23.2** (also reported as 16q24.1 in older literature); MeSH **D056768**; >75 families known to investigators. | Human clinical / disease resource / review | DOI: 10.3390/jpm13010091; DOI: 10.1056/NEJMoa2307952; ClinicalTrials.gov **NCT02362438** (shirakaki2022geneticapproachesfor pages 1-2, gangfuss2025giantaxonalneuropathy pages 1-2, NCT02362438 chunk 1, NCT02362438 chunk 3, bharuchagoebel2024intrathecalgenetherapy pages 1-3) |
| Core phenotype & natural history | Typical onset at **3–5 years** with clumsy or unsteady gait/sensory ataxia, progressive distal>proximal weakness, areflexia, hypotonia, gait disturbance, and characteristic tightly curled/frizzy hair; later features include cerebellar dysfunction, vision loss, contractures, respiratory complications, and loss of ambulation. Most patients become wheelchair dependent by the second decade and often die from pulmonary/respiratory complications by the second to third decade. | German cohort (n=15): gait disturbance **100%**, muscle weakness **100%**, hypotonia **93.3%**, curly/frizzy hair **93.3%**, distal weakness **80%**, abnormal reflexes **80%**, areflexia **73.3%**, frequent falls **66.7%**, joint contractures **53.3%**, respiratory abnormality **53.3%**, intellectual disability **26.7%**. | Human cohort / review / natural history | DOI: 10.1007/s00415-024-12744-z; DOI: 10.3390/jpm13010091; ClinicalTrials.gov **NCT01503125** (gangfuss2025giantaxonalneuropathy pages 5-6, gangfuss2025giantaxonalneuropathy pages 6-8, NCT01503125 chunk 1, shirakaki2022geneticapproachesfor pages 2-4, shirakaki2022geneticapproachesfor pages 4-6, bharuchagoebel2024intrathecalgenetherapy pages 3-5, renganathan2023gigaxoninisrequired pages 1-2) |
| Diagnosis | Diagnosis integrates clinical phenotype plus molecular confirmation. Electrophysiology shows length-dependent sensorimotor neuropathy with markedly reduced or absent CMAP/SNAP amplitudes; EMG shows chronic denervation/neuropathic changes. MRI often shows cerebellar and periventricular white-matter hyperintensities/leukoencephalopathy. Nerve/skin/sural biopsy or EM shows enlarged axons packed with neurofilaments and thin/decreased myelin sheaths. | Trial/natural-history assessments included **NCS, MUNE, SSEP, BAER, PFT**, MRI, nerve biopsy, skin biopsy. Inclusion in interventional trial required pathogenic variants on both GAN alleles. | Human clinical / diagnostic / trial protocol | DOI: 10.3390/jpm13010091; ClinicalTrials.gov **NCT01503125**, **NCT02362438** (NCT01503125 chunk 1, shirakaki2022geneticapproachesfor pages 2-4, NCT02362438 chunk 1, NCT02362438 chunk 2) |
| Molecular mechanism | Gigaxonin is a low-abundance **BTB/BACK/Kelch** adaptor for a **CUL3-RBX1 E3 ubiquitin ligase** complex. Loss of gigaxonin impairs ubiquitination/degradation of intermediate filament proteins, causing IF/neurofilament accumulation, giant axons, axonal dysfunction, and multisystem cytoskeletal pathology. Gigaxonin also regulates autophagosome production via **ATG16L1** turnover and broader proteostasis. | Gigaxonin protein ~**65 kDa**; GAN gene has **11 exons**; variant counts reported as **89** (2022 database summary) and ~**100–150** across broader literature. | Mechanistic review / in vitro / animal | DOI: 10.3390/jpm13010091; DOI: 10.1172/jci.insight.127751 (chen2020gigaxoninglycosylationregulates pages 2-3, shirakaki2022geneticapproachesfor pages 6-7, shirakaki2022geneticapproachesfor pages 1-2) |
| 2023 mechanistic advances | 1) **CRL3^gigaxonin–USP15** pathway shown to govern destruction of **NEFL** and **INA**; Kelch-domain variants **L309R, R545C, C570Y** disrupted substrate binding and caused NF accumulation. 2) Loss of gigaxonin was shown to dramatically inhibit **intermediate-filament transport** along microtubules by **kinesin-1**, with **>20-fold** increase in soluble vimentin oligomers in KO cells. 3) New overt mouse model (**Gan−/−;TgPer**) linked NF disorganization to sensory-motor deficits, cognitive deficits, neuroinflammation, and neuron loss. | PNAS 2023; FASEB J 2023; J Neurosci 2023. Gan−/−;TgPer mice had giant axons **≥160 μm²**. | Mechanistic human-cell / mouse model | DOI: 10.1073/pnas.2306395120; DOI: 10.1096/fj.202202119R; DOI: 10.1523/JNEUROSCI.1959-22.2023 (nath2023anewmouse pages 1-2, park2023thecrl3gigaxoninubiquitin pages 1-2, renganathan2023gigaxoninisrequired pages 1-2) |
| 2024 scAAV9/JeT-GAN gene-therapy trial | First-in-human open-label intrathecal dose-escalation study of **scAAV9/JeT-GAN** in children with genetically confirmed GAN. A single dose was given to **14 participants** across four dose levels. Primary endpoint: safety. Key secondary endpoint: ≥95% posterior probability of slowing decline in **MFM-32 total percent score** at 1 year versus pretreatment slope. | Doses: **3.5×10^13 vg (n=2)**, **1.2×10^14 vg (n=4)**, **1.8×10^14 vg (n=5)**, **3.5×10^14 vg (n=3)**. Median observation **68.7 months** (range **8.6–90.5**). Serious AEs **48**, with **1** possibly treatment-related (fever). Total AEs **682**, with **129** possibly treatment-related. Mean pretreatment MFM-32 slope **−7.17 percentage points/year** (95% credible interval **−8.36 to −5.97**). Posterior mean slope changes at 1 year: **−0.54**, **3.23**, **5.32**, **3.43** percentage points by ascending dose. Posterior probabilities for slowing slope: **44%**, **92%**, **99%**, **90%**; efficacy threshold met at **1.8×10^14 vg**. Sensory-nerve action potentials increased/stabilized/became recordable in **6** participants and remained absent in **8**. | Interventional phase 1 human trial | DOI: 10.1056/NEJMoa2307952; ClinicalTrials.gov **NCT02362438**; PMID **38507752** (NCT02362438 chunk 1, NCT02362438 chunk 2, bharuchagoebel2024intrathecalgenetherapy pages 3-5, bharuchagoebel2024intrathecalgenetherapy pages 1-3, bharuchagoebel2024intrathecalgenetherapy pages 5-7) |
| Current standard care | No approved curative therapy; management is supportive and multidisciplinary. Reported measures include physical therapy, occupational therapy, speech therapy, aquatic therapy, bracing/orthotics, pain control, respiratory monitoring/support, feeding support, and orthopedic management as needed. | Reviews note need for ventilation/tracheostomy and feeding tube in advanced disease; trial exclusion criteria used **FVC ≤50% predicted** or daytime ventilator dependence, reflecting major respiratory involvement in advanced GAN. | Review / supportive care / trial protocol | DOI: 10.3390/jpm13010091; ClinicalTrials.gov **NCT02362438** (shirakaki2022geneticapproachesfor pages 1-2, NCT02362438 chunk 1, NCT02362438 chunk 2, shirakaki2022geneticapproachesfor pages 8-10) |
| Main model systems | Multiple disease models are in use: **Gan knockout mice**, **Gan−/−;TgPer** mice, disease-mutation **GANA49E/A49E** mice, **patient-derived fibroblasts**, **CRISPR GAN−/− SH-SY5Y** cells, **iPSC-derived motor neurons**, and **DRG neuron** models. Preclinical intrathecal AAV9 studies in Gan-knockout rodents supported translation to human trials; rat studies also showed retinal degeneration relevant to disease breadth. | Gan−/−;TgPer model shows early sensory-motor deficits and later cognitive deficits; GANA49E/A49E mouse reportedly recapitulates ataxia, giant axons, demyelination, NF disorganization. iPSC motor-neuron studies showed IF accumulation rescued by gigaxonin restoration. | Mouse / rat / human cell / iPSC / preclinical gene therapy | DOI: 10.1523/JNEUROSCI.1959-22.2023; DOI: 10.1186/s40478-025-02138-1; DOI: 10.1172/jci.insight.127751; ClinicalTrials.gov **NCT02362438** references preclinical AAV work (lienard2026diseasemutationin pages 1-2, nath2023anewmouse pages 1-2, shirakaki2022geneticapproachesfor pages 11-12) |


*Table: This table condenses high-value evidence for Giant Axonal Neuropathy across disease definition, phenotype, diagnosis, mechanism, recent research, clinical trial results, standard care, and model systems. It is designed as a compact reference for building a disease knowledge-base entry with source-linked quantitative details.*

## 1. Disease information

Giant axonal neuropathy is a childhood-onset, progressive, autosomal-recessive neurodegenerative disorder affecting both the peripheral and central nervous systems. Its defining pathology is axonal swelling caused by densely packed, disorganized intermediate filaments, hence “giant axons.” Two ends of a spectrum are recognized: a severe classical early-onset polysystemic phenotype and a later-onset, slower Charcot–Marie–Tooth (CMT)-like axonal neuropathy. (gangfuss2025giantaxonalneuropathy pages 1-2, bharuchagoebel2024intrathecalgenetherapy pages 3-5)

**Identifiers and terminology**

- **OMIM/MIM:** 256850.
- **MeSH:** D056768, *Giant Axonal Neuropathy*.
- **MONDO:** commonly represented as *giant axonal neuropathy*; the exact MONDO accession should be verified against the current MONDO release before database import because it was not returned directly by the retrieved sources.
- **Orphanet:** an Orphanet entity exists, but the numeric ORPHA identifier was not independently recovered here and should likewise be release-verified.
- **ICD:** no GAN-specific ICD-10-CM code was substantiated. Coding generally falls under hereditary/other specified polyneuropathy; use the current national ICD or ICD-11 browser rather than assigning an unverified disease-specific code.
- **Synonyms:** giant axonal neuropathy; GAN; GAN1; giant axonal neuropathy with curly/kinky hair; giant neuroaxonal neuropathy; severe classical GAN; GAN-related CMT-like neuropathy. “Neuroaxonal dystrophy” is a differential category, not a fully interchangeable name.

The trial registry classifies GAN under hereditary sensory and motor neuropathy, heredodegenerative disease, polyneuropathy, and inborn genetic disease. (NCT02362438 chunk 3)

## 2. Etiology

### Causal and genetic factors

GAN is caused by **biallelic germline loss-of-function variants in GAN**, encoding gigaxonin. Reported variants include missense, nonsense, frameshift/deletion, and splice-altering alleles distributed across the gene. Counts differ by database and publication date: 89 disease-associated variants were summarized in 2022, whereas broader reviews report roughly 100–150 variants. These counts should not be conflated with the number classified as pathogenic under current ACMG/AMP criteria. (lienard2026diseasemutationin pages 1-2, shirakaki2022geneticapproachesfor pages 6-7, shirakaki2022geneticapproachesfor pages 1-2)

Pathogenicity is primarily recessive loss of function through absent or unstable protein, reduced transcript, protein misfolding, or impaired substrate recognition. Kelch-domain variants such as **p.Leu309Arg, p.Arg545Cys, and p.Cys570Tyr** disrupted binding to NEFL and INA experimentally. The 2020 Chinese case identified compound-heterozygous **c.236C>T (p.Ser79Leu)** and **c.1466C>G (p.Thr489Ser)** variants, with the latter then novel. (park2023thecrl3gigaxoninubiquitin pages 1-2)

### Risk, protective, and modifying factors

- **Established risk:** two pathogenic GAN alleles; consanguinity increases the probability of homozygosity. In the German series, parental relatedness was reported in five of ten families. (gangfuss2025giantaxonalneuropathy pages 1-2, gangfuss2025giantaxonalneuropathy pages 6-8)
- **Family history:** may be absent because recessive disease can occur in a single sibship.
- **Environmental/infectious risk:** none established. GAN is not caused by toxins, infection, lifestyle, or occupational exposure.
- **Protective variants/factors:** no validated protective GAN allele, diet, drug, or lifestyle intervention is known.
- **Potential gene–environment/metabolic interaction:** gigaxonin is O-GlcNAcylated in a nutrient-responsive manner. Mass spectrometry identified nine candidate sites, with Ser272 and Thr277 important for intermediate-filament turnover. Because O-GlcNAc depends on glucose, glutamine, acetyl-CoA, uridine, and ATP availability, this provides a plausible metabolic modifier mechanism, but it is **cellular evidence**, not proof that diet changes human disease severity. (chen2020gigaxoninglycosylationregulates pages 2-3)

No replicated modifier gene or clinically actionable epigenetic signature has been established.

## 3. Phenotypes

The phenotype is progressive and multisystemic. Suggested HPO mappings should be validated against the current HPO release.

| Phenotype | Character/course | Frequency evidence | Suggested HPO term |
|---|---|---:|---|
| Gait disturbance/sensory ataxia | Usually first recognized at 3–5 years; chronic progressive | 100% in German n=15 cohort | Abnormal gait **HP:0001288**; sensory ataxia **HP:0002066** |
| Muscle weakness | Distal before proximal; severe and progressive | 100%; distal weakness 80% | Muscle weakness **HP:0001324**; distal muscle weakness **HP:0002460** |
| Hypotonia | Childhood onset, usually progressive with neuropathy | 93.3% | Hypotonia **HP:0001252** |
| Areflexia/abnormal reflexes | Length-dependent peripheral neuropathy | Areflexia 73.3%; abnormal reflexes 80% | Areflexia **HP:0001284** |
| Curly/kinky/frizzy hair | Characteristic but not obligatory | 93.3% | Kinky hair **HP:0002224** |
| Frequent falls | Early functional manifestation | 66.7% | Frequent falls **HP:0002527** |
| Contractures | Secondary to weakness/immobility | 53.3% | Joint contracture **HP:0034392** |
| Respiratory abnormality | Later-stage weakness/pulmonary complications | 53.3% | Respiratory insufficiency **HP:0002093** |
| Cerebellar dysfunction | Ataxia, dysmetria; progressive CNS disease | Common qualitatively | Cerebellar ataxia **HP:0001251** |
| Pyramidal signs | CNS tract involvement; variable | Variable | Babinski sign **HP:0003487** / spasticity **HP:0001257** |
| Cognitive/developmental involvement | Developmental delay, intellectual decline; variable | Intellectual disability and gross-motor delay each 26.7% in one cohort | Intellectual disability **HP:0001249**; gross motor delay **HP:0002194** |
| Cranial/ocular involvement | Facial weakness, ophthalmoplegia and later visual loss | Variable | Facial weakness **HP:0002058**; ophthalmoplegia **HP:0000602**; visual impairment **HP:0000505** |
| Skeletal deformity | Pes planus, kyphoscoliosis, muscle wasting | Variable | Pes planus **HP:0001763**; scoliosis **HP:0002650**; muscle atrophy **HP:0003202** |

The German cohort reported gait disturbance and weakness in all 15 patients, hypotonia and frizzy hair in 14/15, distal weakness in 12/15, areflexia in 11/15, falls in 10/15, and respiratory abnormalities and contractures in 8/15. (gangfuss2025giantaxonalneuropathy pages 5-6)

**Quality of life.** No validated GAN-specific EQ-5D, SF-36, PROMIS, or utility-value dataset was identified. Nevertheless, progressive falls, loss of independent ambulation, upper-limb impairment, communication/swallowing difficulty, respiratory support, and caregiver dependence imply profound mobility, self-care, educational, and psychosocial burden. Trial investigators use the MFM-32, modified Friedreich Ataxia Rating Scale, and Neuropathy Impairment Score rather than a GAN-specific quality-of-life instrument. (bharuchagoebel2024intrathecalgenetherapy pages 5-7)

## 4. Genetic and molecular information

**GAN/gigaxonin.** GAN contains 11 exons and encodes an approximately 65-kDa BTB/BACK/Kelch protein. The N-terminal BTB domain binds CUL3/RBX1; BACK contributes complex architecture and ATG16L1 interaction; the C-terminal Kelch repeats recognize substrates. Published cytogenetic notation varies between older 16q24.1 and current 16q23.2 annotation; contemporary genome-build coordinates should be used for implementation. (shirakaki2022geneticapproachesfor pages 6-7, bharuchagoebel2024intrathecalgenetherapy pages 3-5, renganathan2023gigaxoninisrequired pages 1-2)

**Variant interpretation.** Variants are constitutional/germline, not somatic cancer drivers. Clinical classification requires ACMG/AMP evaluation using segregation, population frequency, predicted loss of function, functional evidence, and phenotype specificity. Disease-causing alleles are generally absent or extremely rare in population databases, but no comprehensive per-variant gnomAD table was available from the retrieved literature. Therefore, a blanket numerical allele frequency should not be assigned. In the German cohort, eight homozygous variants were found; the paper’s classifications included pathogenic, likely pathogenic, and VUS alleles. Molecular diagnosis should not treat a VUS alone as definitive without additional evidence. (gangfuss2025giantaxonalneuropathy pages 6-8)

**Genotype–phenotype relationship.** Earlier literature found weak or absent global correlation. Some cohorts suggest truncating/nonsense alleles more often produce classical severe disease and selected missense alleles milder CMT-like disease, but exceptions occur; this is not yet a reliable individual prognostic rule. (gangfuss2025giantaxonalneuropathy pages 6-8, lienard2026diseasemutationin pages 1-2)

**Chromosomal, epigenetic, and modifier findings.** No recurrent aneuploidy, translocation, inversion, pathogenic repeat expansion, mitochondrial-DNA defect, or disease-specific methylation signature is established. O-GlcNAcylation is a post-translational metabolic regulator, not a validated epigenetic diagnostic marker. (chen2020gigaxoninglycosylationregulates pages 2-3)

## 5. Environmental information

No causal toxin, radiation exposure, pollutant, occupational factor, smoking pattern, alcohol exposure, diet, or infectious agent has been demonstrated. Accordingly, CTD-style chemical causation and NCBI Taxonomy pathogen annotations are **not applicable**. Activity, nutrition, and respiratory-infection avoidance affect general health and complication burden, but do not prevent the underlying Mendelian disorder.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic trigger:** biallelic GAN loss-of-function variants reduce functional gigaxonin.
2. **E3-ligase failure:** defective CUL3–RBX1–gigaxonin substrate recognition/ubiquitylation decreases turnover of intermediate-filament proteins and other substrates.
3. **Proteostasis/cytoskeletal disruption:** NEFL, INA, peripherin, vimentin, desmin and related filaments accumulate; the CRL3-gigaxonin pathway also targets actin-associated TPM1, TPM2, TAGLN and CNN2. (lienard2026diseasemutationin pages 1-2, park2023thecrl3gigaxoninubiquitin pages 1-2)
4. **Transport failure:** loss of gigaxonin inhibits kinesin-1-mediated intermediate-filament transport. GAN-knockout cells showed a **greater than 20-fold increase** in soluble vimentin oligomers; direct coupling of kinesin to filaments rescued abnormal distribution, supporting transport failure as causal rather than merely secondary. (renganathan2023gigaxoninisrequired pages 1-2)
5. **Autophagy impairment:** gigaxonin normally governs ATG16L1 turnover and autophagosome production. Neurofilament aggregates subsequently disturb autophagic-organelle distribution and lysosome fusion and sequester 14-3-3, impairing TFEB localization—creating a feed-forward proteostasis defect. (paumier2024neurofilamentaccumulationdisrupts pages 1-5, shirakaki2022geneticapproachesfor pages 6-7)
6. **Organelle/metabolic stress:** aggregates impede mitochondrial motility and increase energetic demand. This is strongest in cellular and mouse-neuron evidence, not yet a validated circulating metabolomic signature. (israeli2016intermediatefilamentaggregates pages 6-7)
7. **Tissue pathology:** densely packed filaments enlarge axons, thin/disrupt myelin, impair conduction and promote axonal and neuronal loss; neuroinflammation appears downstream in overt mouse models. (shirakaki2022geneticapproachesfor pages 2-4, nath2023anewmouse pages 1-2)
8. **Clinical expression:** length-dependent sensorimotor neuropathy produces distal weakness, sensory ataxia and areflexia; cerebellar/white-matter and cranial involvement produces ataxia, cognitive, ocular and bulbar features; respiratory neuromuscular decline contributes to death.

**Recent 2023 mechanistic advances.** Park et al. identified a CRL3-gigaxonin–USP15 axis controlling NEFL and INA and a NEFL degron, while Renganathan et al. demonstrated the intermediate-filament transport defect. These extend the model beyond passive accumulation to active defects in substrate destruction and spatial cytoskeletal trafficking. (park2023thecrl3gigaxoninubiquitin pages 1-2, renganathan2023gigaxoninisrequired pages 1-2)

**Molecular profiling.** White-blood-cell proteomics from four German patients identified 111 dysregulated proteins—22 increased and 89 decreased—including proteins involved in synaptic function, filament organization, autophagosome maturation, endosome–lysosome transport, actin organization, translation, muscle contraction, SNARE/sortilin/VAMP trafficking and HYOU1/GRP170. This is exploratory, small-sample proteomics, not a validated diagnostic biomarker. (gangfuss2025giantaxonalneuropathy pages 5-6, gangfuss2025giantaxonalneuropathy pages 6-8)

No robust disease-specific single-cell atlas, spatial transcriptomic map, human CNS multi-omic integration, lipidomic signature, or clinical CRISPR-screen result was identified.

**Suggested GO biological-process terms:** protein ubiquitination (GO:0016567); proteasome-mediated ubiquitin-dependent protein catabolic process (GO:0043161); intermediate filament organization (GO:0045109); neurofilament bundle assembly (GO:0033693); microtubule-based transport (GO:0099111); autophagosome assembly (GO:0000045); autophagy (GO:0006914); axonal transport (GO:0098930); regulation of mitochondrial transport; neuron death (GO:0070997).

**Suggested GO cellular components:** intermediate filament cytoskeleton (GO:0045111); neurofilament (GO:0005883); axon (GO:0030424); autophagosome (GO:0005776); lysosome (GO:0005764); mitochondrion (GO:0005739); Cul3-RING ubiquitin ligase complex.

**Suggested CL terms:** neuron **CL:0000540**; motor neuron **CL:0000100**; sensory neuron **CL:0000101**; Schwann cell **CL:0002573**; oligodendrocyte **CL:0000128**; astrocyte **CL:0000127**; skeletal muscle cell **CL:0000188**; fibroblast **CL:0000057**; leukocyte **CL:0000738**.

## 7. Anatomical structures affected

- **Primary organ/system:** peripheral nerves, spinal roots, spinal cord, brain white matter, cerebellum, and long central tracts.
- **Cells:** long motor and sensory axons are especially vulnerable; neuronal cell bodies, Schwann cells, glia, fibroblasts, muscle and hair-associated cells show broader intermediate-filament pathology. AAV treatment was designed to reach anterior-horn motor neurons and dorsal-root-ganglion sensory neurons. (bharuchagoebel2024intrathecalgenetherapy pages 3-5)
- **Secondary involvement:** skeletal muscle atrophy from denervation; respiratory muscles and swallowing apparatus; optic/retinal pathways and ocular lens; autonomic pathways; skin/hair.
- **Subcellular sites:** cytoplasmic intermediate-filament networks, axon cytoskeleton, microtubule transport machinery, ubiquitin–proteasome system, autophagosomes, lysosomes, and mitochondria.
- **Localization/lateralization:** typically bilateral and relatively symmetric, with length-dependent distal predominance; no characteristic unilateral pattern.

**Suggested UBERON terms:** peripheral nerve **UBERON:0001021**; spinal cord **UBERON:0002240**; brain white matter **UBERON:0002316**; cerebellum **UBERON:0002037**; dorsal root ganglion **UBERON:0000044**; skeletal muscle organ **UBERON:0001630**; sural nerve (use current UBERON/FMA release mapping); retina **UBERON:0000966**.

## 8. Temporal development

Typical onset is insidious at approximately 3–5 years, often as clumsiness, falls, sensory ataxia, or distal weakness. Classical disease progresses continuously from distal sensorimotor neuropathy to proximal and upper-limb weakness, cerebellar/bulbar and visual involvement, loss of ambulation around 8–10 years in older descriptions or later in some contemporary patients, and ventilatory/feeding dependence during the second decade. Death commonly occurs in the second or third decade. (NCT02362438 chunk 1, bharuchagoebel2024intrathecalgenetherapy pages 3-5, renganathan2023gigaxoninisrequired pages 1-2)

A slower CMT-like form preserves ambulation longer and may show less extensive MRI disease. There is no established remission or relapsing-remitting course. GAN is lifelong and progressive. The likely therapeutic window is **before extensive irreversible axonal loss**; trial materials explicitly prioritized younger, milder, independently ambulant patients as having greater potential to benefit. (NCT02362438 chunk 1)

## 9. Inheritance and population

Inheritance is autosomal recessive. For two carrier parents, each pregnancy has a 25% probability of an affected child, 50% of an unaffected carrier, and 25% of an unaffected non-carrier. Penetrance for confirmed biallelic pathogenic loss-of-function genotypes appears high, but expressivity and progression vary. Anticipation is not expected. Germline mosaicism is theoretically possible but not established as a recurrent feature.

GAN has been reported across diverse ancestries and regions; consanguinity and founder alleles can elevate local occurrence, but no ethnicity-specific population prevalence is robustly quantified. Approximately 75–80 families worldwide were cited in recent research. There are **no defensible incidence or prevalence rates per 100,000**, carrier-frequency estimates, or sex-ratio estimates from population registries. Both sexes are affected, consistent with autosomal inheritance. (gangfuss2025giantaxonalneuropathy pages 1-2, lienard2026diseasemutationin pages 1-2, bharuchagoebel2024intrathecalgenetherapy pages 3-5)

## 10. Diagnostics

### Recommended approach

1. Recognize childhood progressive, length-dependent sensorimotor neuropathy—especially with sensory ataxia, areflexia, CNS/cerebellar signs, and tightly curled hair.
2. Perform neurologic, developmental, ophthalmologic, respiratory, swallowing, nutritional, and orthopedic assessment.
3. Obtain nerve-conduction studies and EMG. Typical findings include very low/absent SNAPs, reduced CMAPs, chronic denervation and initially normal-to-moderately reduced conduction velocity, sometimes reaching demyelinating ranges later. (shirakaki2022geneticapproachesfor pages 1-2, shirakaki2022geneticapproachesfor pages 2-4)
4. Brain/spinal MRI may show periventricular and cerebellar white-matter T2 hyperintensity, including around the dentate nuclei, internal capsule and spinal pathways. Magnetic-resonance spectroscopy may show reduced N-acetylaspartate. (shirakaki2022geneticapproachesfor pages 2-4, shirakaki2022geneticapproachesfor pages 4-6)
5. Confirm with **biallelic pathogenic/likely pathogenic GAN variants** and parental segregation where possible. Trial eligibility required pathogenic variants on both copies. (NCT02362438 chunk 2)
6. Biopsy is now supportive rather than mandatory when molecular results are definitive. Sural nerve/skin/muscle electron microscopy shows giant axons packed with disorganized neurofilaments, reduced microtubules and thin myelin. (shirakaki2022geneticapproachesfor pages 2-4)

### Genetic testing

- **Preferred:** inherited-neuropathy/neurodegeneration panel containing GAN, with deletion/duplication analysis, or WES/WGS when the phenotype is atypical or the panel is negative.
- **Single-gene GAN sequencing:** appropriate for a highly characteristic phenotype or familial cascade testing.
- **WGS:** useful for noncoding, structural, or difficult-to-detect alleles after negative conventional testing, although disease-specific diagnostic-yield statistics are unavailable.
- **RNA sequencing:** potentially helpful for suspected splice variants, but not routine or validated as a GAN biomarker.
- **CMA/karyotype/FISH:** low yield unless syndromic copy-number or cytogenetic disease is independently suspected.
- **Mitochondrial-DNA and repeat-expansion testing:** not GAN tests; reserve for differential diagnosis.

### Differential diagnosis

Consider CMT and other hereditary motor-sensory neuropathies, infantile neuroaxonal dystrophy/PLA2G6-associated neurodegeneration, hereditary spastic paraplegias, Friedreich ataxia, metachromatic leukodystrophy, Krabbe disease, mitochondrial neuropathies, neurofilament-related neuropathies, and acquired inflammatory/toxic neuropathies. GAN is distinguished by biallelic GAN variants plus combined PNS/CNS disease and giant-axon/intermediate-filament pathology.

No population or newborn-screening program exists. Cascade testing of relatives is appropriate after molecular confirmation.

## 11. Outcome and prognosis

Classical GAN causes major lifelong disability, usually wheelchair dependence in the second decade, progressive arm, bulbar and respiratory dysfunction, and premature mortality—often from pulmonary complications—by the third decade. Milder CMT-like cases can survive and walk longer. No reliable 5- or 10-year survival curves, mortality rate, or validated prognostic calculator exists. (shirakaki2022geneticapproachesfor pages 1-2, bharuchagoebel2024intrathecalgenetherapy pages 3-5)

The pivotal trial quantified untreated motor decline at a mean **−7.17 MFM-32 percentage points/year** (95% credible interval −8.36 to −5.97). This is valuable as a trial benchmark but comes from a small selected cohort rather than a population registry. (bharuchagoebel2024intrathecalgenetherapy pages 1-3)

Potential adverse prognostic features include early severe weakness, rapid MFM-32 decline, extensive CNS/MRI disease, respiratory compromise, and null/CRIM-negative genotypes, but none forms a validated multivariable model. There is no validated prognostic blood, CSF, proteomic, or imaging biomarker.

## 12. Treatment

### Current care

There is no approved disease-modifying therapy. Management is multidisciplinary and individualized: physical/aquatic therapy; range-of-motion work and contracture prevention; orthotics, mobility devices and wheelchair/seating support; occupational and speech therapy; pain management; nutritional and swallowing assessment; feeding-tube support where required; cough assistance, pulmonary-function surveillance and noninvasive/invasive ventilation; scoliosis and orthopedic management; ophthalmologic care; and psychosocial/palliative support. (shirakaki2022geneticapproachesfor pages 1-2, NCT02362438 chunk 1, shirakaki2022geneticapproachesfor pages 8-10)

Suggested NCIt concepts include Physical Therapy, Occupational Therapy, Speech Therapy, Orthotic Device, Noninvasive Ventilation, Mechanical Ventilation, Gastrostomy, Nutritional Support, Genetic Counseling, and Palliative Care; exact NCIt codes should be resolved against the current NCIt release.

### Intrathecal GAN gene replacement—2024 pivotal development

The open-label, nonrandomized phase 1 **NCT02362438** study administered one intrathecal dose of **scAAV9/JeT-GAN**, containing a codon-optimized GAN transgene under the JeT promoter, to 14 participants. Doses were 3.5×10^13 vg (n=2), 1.2×10^14 (n=4), 1.8×10^14 (n=5), and 3.5×10^14 (n=3). (NCT02362438 chunk 1, bharuchagoebel2024intrathecalgenetherapy pages 1-3)

Over a median 68.7 months, 48 serious adverse events occurred; one—fever—was considered possibly treatment-related. Of 682 total adverse events, 129 were possibly treatment-related. Posterior probabilities of slowing one-year MFM-32 decline were 44%, 92%, 99%, and 90% across ascending doses; only the 1.8×10^14-vg group crossed the prespecified 95% efficacy threshold. Sensory-nerve action potentials improved, stabilized, or became recordable in six participants but remained absent in eight. The authors concluded that treatment produced a **possible**, dose-dependent motor and electrophysiological benefit and explicitly called for further safety and efficacy studies—not that efficacy was proven. (bharuchagoebel2024intrathecalgenetherapy pages 3-5, bharuchagoebel2024intrathecalgenetherapy pages 1-3)

Direct abstract quote (published **21 March 2024**, PMID **38507752**, DOI/URL: https://doi.org/10.1056/NEJMoa2307952): “Intrathecal gene transfer with scAAV9/JeT-GAN for giant axonal neuropathy was associated with adverse events and resulted in a possible benefit in motor function scores and other measures at some vector doses over a year.” (bharuchagoebel2024intrathecalgenetherapy pages 3-5)

Participants received glucocorticoid immunomodulation; CRIM-negative participants also received rapamycin and tacrolimus to reduce anti-transgene T-cell responses. AAV-associated dorsal-root-ganglion toxicity remains an expert concern, and the study was small, uncontrolled, dose-escalating, and compared post-treatment slopes with within-cohort pretreatment natural history. It therefore does not establish approval-level efficacy. (bharuchagoebel2024intrathecalgenetherapy pages 5-7, shirakaki2022geneticapproachesfor pages 8-10)

No validated small molecule, ASO, siRNA, mRNA, CRISPR editing, cell therapy, immunotherapy, or pharmacogenomic treatment is available. Experimental substrate-directed approaches—potentially targeting USP15, filament accumulation, autophagy or transport—remain preclinical.

## 13. Prevention

The disorder cannot currently be prevented through vaccination, diet, exposure avoidance, or prophylactic medication.

- **Primary prevention/reproductive options:** carrier testing for relatives after the familial variants are known; partner testing; preimplantation genetic testing for monogenic disease; and prenatal diagnosis by chorionic-villus sampling or amniocentesis.
- **Secondary prevention:** early molecular diagnosis and cascade testing permit surveillance and potentially earlier trial enrollment, but no newborn screening is available.
- **Tertiary prevention:** respiratory vaccination according to routine schedules, prompt infection care, pulmonary surveillance, aspiration-risk management, contracture prevention, nutrition, mobility support, pressure-injury prevention and orthopedic monitoring can reduce complications but do not alter the genotype.
- **Counseling:** explain autosomal-recessive recurrence risks, variable expressivity, limitations of VUS interpretation, and the experimental status and immune/toxicity uncertainties of gene therapy.

## 14. Other species and natural disease

No well-substantiated naturally occurring, breed-associated veterinary GAN caused by orthologous GAN variants was identified in the retrieved evidence; therefore no VBO breed term or zoonotic annotation should be assigned. GAN is neither infectious nor transmissible, and zoonotic potential is not applicable.

Orthologous gigaxonin biology is highly conserved in vertebrates, enabling engineered mouse, rat and zebrafish systems. Natural disease evidence should be kept separate from induced models. Taxa commonly used include *Mus musculus* (NCBI Taxon 10090), *Rattus norvegicus* (10116), *Danio rerio* (7955), and human cellular systems (9606).

## 15. Model organisms and experimental systems

### Mouse

Conventional **Gan-knockout mice** reproduce intermediate-filament accumulation, Schwann-cell and peripheral-nerve pathology, transport/autonomic abnormalities and provide gene-transfer proof of concept, but early models often lacked the dramatic giant axons and severe clinical course of human GAN. Intrathecal scAAV9/JeT-GAN transduced dorsal-root ganglia, reduced filament aggregates and nerve pathology, and rescued rotarod deficits, supporting clinical translation. (bharuchagoebel2024intrathecalgenetherapy pages 3-5, shirakaki2022geneticapproachesfor pages 8-10)

The 2023 **Gan−/−;TgPer** model combines Gan deletion with peripherin overexpression. It developed early sensorimotor deficits, spinal-neuron swelling and brain inclusions; by 12 months it had cognitive and severe motor/sensory deficits, neuroinflammation, cortical/spinal neuron loss, and dorsal/ventral-root giant axons at least 160 μm². This supports neurofilament disorganization as a driver, but peripherin overexpression is an artificial sensitizing lesion and may exaggerate one pathway. (nath2023anewmouse pages 1-2)

Direct abstract quote (published **31 May 2023**, DOI/URL: https://doi.org/10.1523/JNEUROSCI.1959-22.2023): “These results, obtained with both sexes, support the view that the disorganization of IFs can drive some neurodegenerative changes caused by gigaxonin deficiency.” (nath2023anewmouse pages 1-2)

A disease-allele **GANA49E/A49E** mouse reported sensorimotor deficits, ataxia, giant axons, demyelination and neurofilament disorganization and may model human missense disease more faithfully than a complete knockout. (lienard2026diseasemutationin pages 1-2)

### Rat and other vertebrate models

Gan-deficient rats demonstrate extensive rod and cone photoreceptor degeneration and early ocular-lens pathology, broadening recognition of ocular disease and informing whether CNS-directed treatment alone is sufficient. PMID **33955818** and PMID **30709364** are cited in the clinical-trial record. (NCT02362438 chunk 2)

Zebrafish knockdown/mutant systems have been used to study gigaxonin-dependent motility and nervous-system development, but detailed quantitative phenotype evidence was not recovered here; they are best considered rapid developmental and screening models rather than complete natural-history replicas.

### Human cellular models

Patient fibroblasts, CRISPR GAN-null neuroblastoma/fibroblast lines, dorsal-root-ganglion neurons, and patient-derived iPSC motor neurons reproduce intermediate-filament accumulation. Restoration of gigaxonin rescues filament pathology, providing target validation and platforms for vector, substrate and small-molecule testing. CRISPR GAN-null cells were also used to study O-GlcNAc regulation, and live-cell photoconversion systems resolved kinesin-dependent filament transport. (chen2020gigaxoninglycosylationregulates pages 2-3, renganathan2023gigaxoninisrequired pages 1-2, shirakaki2022geneticapproachesfor pages 11-12)

Direct abstract quote from the 2023 transport study (DOI/URL: https://doi.org/10.1096/fj.202202119R): “The loss of gigaxonin dramatically inhibited transport of IFs along microtubules by the microtubule motor kinesin-1.” (renganathan2023gigaxoninisrequired pages 1-2)

## Knowledge-base conclusions

GAN1 is a high-penetrance recessive axonopathy caused by loss of gigaxonin-dependent cytoskeletal proteostasis. The strongest current causal chain is **GAN loss of function → defective CRL3 substrate ubiquitylation and filament transport/autophagy → intermediate-filament accumulation → giant axons, impaired organelle transport and axonal degeneration → progressive peripheral and central neurologic disability**. Human evidence supports characteristic early childhood onset, severe functional decline and premature pulmonary mortality, but population epidemiology, standardized quality-of-life data, validated biomarkers, protective factors, modifier genes, and definitive genotype–prognosis rules remain absent. The 2024 intrathecal AAV9 trial is the principal translational advance: it demonstrated feasibility, long follow-up and a possible motor benefit at selected doses, while leaving efficacy, optimal dose, durability, immune management and dorsal-root-ganglion safety unresolved. (park2023thecrl3gigaxoninubiquitin pages 1-2, bharuchagoebel2024intrathecalgenetherapy pages 3-5, bharuchagoebel2024intrathecalgenetherapy pages 1-3, renganathan2023gigaxoninisrequired pages 1-2)

References

1. (shirakaki2022geneticapproachesfor pages 1-2): Satomi Shirakaki, Rohini Roy Roshmi, and Toshifumi Yokota. Genetic approaches for the treatment of giant axonal neuropathy. Journal of Personalized Medicine, 13:91, Dec 2022. URL: https://doi.org/10.3390/jpm13010091, doi:10.3390/jpm13010091. This article has 4 citations.

2. (gangfuss2025giantaxonalneuropathy pages 1-2): Andrea Gangfuß, Guido Goj, Silke Polz, Adela Della Marina, Andreas Hentschel, Katja Ahlbory, Timo Deba, Urania Kotzaeridou, Elisabeth Schuler, Astrid Pechmann, Uta Diebold, Gerhard Kurlemann, Lucas Heinzkyll, Dirk Schmitt, Kevin Rostasy, Tobias Ruck, Johann Böhm, Andreas Roos, and Ulrike Schara-Schmidt. Giant axonal neuropathy (gan): cross-sectional data on phenotypes, genotypes, and proteomic signature from a german cohort. Journal of Neurology, Dec 2025. URL: https://doi.org/10.1007/s00415-024-12744-z, doi:10.1007/s00415-024-12744-z. This article has 4 citations and is from a domain leading peer-reviewed journal.

3. (NCT02362438 chunk 1):  Intrathecal Administration of scAAV9/JeT-GAN for the Treatment of Giant Axonal Neuropathy. National Institute of Neurological Disorders and Stroke (NINDS). 2015. ClinicalTrials.gov Identifier: NCT02362438

4. (NCT02362438 chunk 3):  Intrathecal Administration of scAAV9/JeT-GAN for the Treatment of Giant Axonal Neuropathy. National Institute of Neurological Disorders and Stroke (NINDS). 2015. ClinicalTrials.gov Identifier: NCT02362438

5. (bharuchagoebel2024intrathecalgenetherapy pages 1-3): Diana X. Bharucha-Goebel, Joshua J. Todd, Dimah Saade, Gina Norato, Minal Jain, Tanya Lehky, Rachel M. Bailey, Jessica A. Chichester, Roberto Calcedo, Diane Armao, A. Reghan Foley, Payam Mohassel, Eshetu Tesfaye, Bradley P. Carlin, Beth Seremula, Melissa Waite, Wadih M. Zein, Laryssa A. Huryn, Thomas O. Crawford, Charlotte J. Sumner, Ahmet Hoke, John D. Heiss, Lawrence Charnas, Jody E. Hooper, Thomas W. Bouldin, Elizabeth M. Kang, Denis Rybin, Steven J. Gray, and Carsten G. Bönnemann. Intrathecal gene therapy for giant axonal neuropathy. The New England journal of medicine, 390 12:1092-1104, Mar 2024. URL: https://doi.org/10.1056/nejmoa2307952, doi:10.1056/nejmoa2307952. This article has 69 citations and is from a highest quality peer-reviewed journal.

6. (gangfuss2025giantaxonalneuropathy pages 5-6): Andrea Gangfuß, Guido Goj, Silke Polz, Adela Della Marina, Andreas Hentschel, Katja Ahlbory, Timo Deba, Urania Kotzaeridou, Elisabeth Schuler, Astrid Pechmann, Uta Diebold, Gerhard Kurlemann, Lucas Heinzkyll, Dirk Schmitt, Kevin Rostasy, Tobias Ruck, Johann Böhm, Andreas Roos, and Ulrike Schara-Schmidt. Giant axonal neuropathy (gan): cross-sectional data on phenotypes, genotypes, and proteomic signature from a german cohort. Journal of Neurology, Dec 2025. URL: https://doi.org/10.1007/s00415-024-12744-z, doi:10.1007/s00415-024-12744-z. This article has 4 citations and is from a domain leading peer-reviewed journal.

7. (gangfuss2025giantaxonalneuropathy pages 6-8): Andrea Gangfuß, Guido Goj, Silke Polz, Adela Della Marina, Andreas Hentschel, Katja Ahlbory, Timo Deba, Urania Kotzaeridou, Elisabeth Schuler, Astrid Pechmann, Uta Diebold, Gerhard Kurlemann, Lucas Heinzkyll, Dirk Schmitt, Kevin Rostasy, Tobias Ruck, Johann Böhm, Andreas Roos, and Ulrike Schara-Schmidt. Giant axonal neuropathy (gan): cross-sectional data on phenotypes, genotypes, and proteomic signature from a german cohort. Journal of Neurology, Dec 2025. URL: https://doi.org/10.1007/s00415-024-12744-z, doi:10.1007/s00415-024-12744-z. This article has 4 citations and is from a domain leading peer-reviewed journal.

8. (NCT01503125 chunk 1):  Giant Axonal Neuropathy Natural History Study. Columbia University. 2011. ClinicalTrials.gov Identifier: NCT01503125

9. (shirakaki2022geneticapproachesfor pages 2-4): Satomi Shirakaki, Rohini Roy Roshmi, and Toshifumi Yokota. Genetic approaches for the treatment of giant axonal neuropathy. Journal of Personalized Medicine, 13:91, Dec 2022. URL: https://doi.org/10.3390/jpm13010091, doi:10.3390/jpm13010091. This article has 4 citations.

10. (shirakaki2022geneticapproachesfor pages 4-6): Satomi Shirakaki, Rohini Roy Roshmi, and Toshifumi Yokota. Genetic approaches for the treatment of giant axonal neuropathy. Journal of Personalized Medicine, 13:91, Dec 2022. URL: https://doi.org/10.3390/jpm13010091, doi:10.3390/jpm13010091. This article has 4 citations.

11. (bharuchagoebel2024intrathecalgenetherapy pages 3-5): Diana X. Bharucha-Goebel, Joshua J. Todd, Dimah Saade, Gina Norato, Minal Jain, Tanya Lehky, Rachel M. Bailey, Jessica A. Chichester, Roberto Calcedo, Diane Armao, A. Reghan Foley, Payam Mohassel, Eshetu Tesfaye, Bradley P. Carlin, Beth Seremula, Melissa Waite, Wadih M. Zein, Laryssa A. Huryn, Thomas O. Crawford, Charlotte J. Sumner, Ahmet Hoke, John D. Heiss, Lawrence Charnas, Jody E. Hooper, Thomas W. Bouldin, Elizabeth M. Kang, Denis Rybin, Steven J. Gray, and Carsten G. Bönnemann. Intrathecal gene therapy for giant axonal neuropathy. The New England journal of medicine, 390 12:1092-1104, Mar 2024. URL: https://doi.org/10.1056/nejmoa2307952, doi:10.1056/nejmoa2307952. This article has 69 citations and is from a highest quality peer-reviewed journal.

12. (renganathan2023gigaxoninisrequired pages 1-2): Bhuvanasundar Renganathan, James P Zewe, Yuan Cheng, Mark Kittisopikul, Puneet Opal, Karen M Ridge, and Vladimir I. Gelfand. Gigaxonin is required for intermediate filament transport. The FASEB Journal, Aug 2023. URL: https://doi.org/10.1096/fj.202202119r, doi:10.1096/fj.202202119r. This article has 20 citations.

13. (NCT02362438 chunk 2):  Intrathecal Administration of scAAV9/JeT-GAN for the Treatment of Giant Axonal Neuropathy. National Institute of Neurological Disorders and Stroke (NINDS). 2015. ClinicalTrials.gov Identifier: NCT02362438

14. (chen2020gigaxoninglycosylationregulates pages 2-3): Po-Han Chen, Jimin Hu, Jianli Wu, Duc T. Huynh, Timothy J. Smith, Samuel Pan, Brittany J. Bisnett, Alexander B. Smith, Annie Lu, Brett M. Condon, Jen-Tsan Chi, and Michael Boyce. Gigaxonin glycosylation regulates intermediate filament turnover and may impact giant axonal neuropathy etiology or treatment. JCI insight, Jan 2020. URL: https://doi.org/10.1172/jci.insight.127751, doi:10.1172/jci.insight.127751. This article has 21 citations and is from a domain leading peer-reviewed journal.

15. (shirakaki2022geneticapproachesfor pages 6-7): Satomi Shirakaki, Rohini Roy Roshmi, and Toshifumi Yokota. Genetic approaches for the treatment of giant axonal neuropathy. Journal of Personalized Medicine, 13:91, Dec 2022. URL: https://doi.org/10.3390/jpm13010091, doi:10.3390/jpm13010091. This article has 4 citations.

16. (nath2023anewmouse pages 1-2): Banshi Nath and Jean-Pierre Julien. A new mouse model of giant axonal neuropathy with overt phenotypes and neurodegeneration driven by neurofilament disorganization. The Journal of Neuroscience, 43:4174-4189, May 2023. URL: https://doi.org/10.1523/jneurosci.1959-22.2023, doi:10.1523/jneurosci.1959-22.2023. This article has 6 citations.

17. (park2023thecrl3gigaxoninubiquitin pages 1-2): Hyoung-Min Park, Ly Le, Thao T. Nguyen, Ki Hong Nam, Alban Ordureau, J. Eugene Lee, and Thang Van Nguyen. The crl3gigaxonin ubiquitin ligase–usp15 pathway governs the destruction of neurofilament proteins. Proceedings of the National Academy of Sciences of the United States of America, Oct 2023. URL: https://doi.org/10.1073/pnas.2306395120, doi:10.1073/pnas.2306395120. This article has 11 citations and is from a highest quality peer-reviewed journal.

18. (bharuchagoebel2024intrathecalgenetherapy pages 5-7): Diana X. Bharucha-Goebel, Joshua J. Todd, Dimah Saade, Gina Norato, Minal Jain, Tanya Lehky, Rachel M. Bailey, Jessica A. Chichester, Roberto Calcedo, Diane Armao, A. Reghan Foley, Payam Mohassel, Eshetu Tesfaye, Bradley P. Carlin, Beth Seremula, Melissa Waite, Wadih M. Zein, Laryssa A. Huryn, Thomas O. Crawford, Charlotte J. Sumner, Ahmet Hoke, John D. Heiss, Lawrence Charnas, Jody E. Hooper, Thomas W. Bouldin, Elizabeth M. Kang, Denis Rybin, Steven J. Gray, and Carsten G. Bönnemann. Intrathecal gene therapy for giant axonal neuropathy. The New England journal of medicine, 390 12:1092-1104, Mar 2024. URL: https://doi.org/10.1056/nejmoa2307952, doi:10.1056/nejmoa2307952. This article has 69 citations and is from a highest quality peer-reviewed journal.

19. (shirakaki2022geneticapproachesfor pages 8-10): Satomi Shirakaki, Rohini Roy Roshmi, and Toshifumi Yokota. Genetic approaches for the treatment of giant axonal neuropathy. Journal of Personalized Medicine, 13:91, Dec 2022. URL: https://doi.org/10.3390/jpm13010091, doi:10.3390/jpm13010091. This article has 4 citations.

20. (lienard2026diseasemutationin pages 1-2): Caroline Liénard, Nicolas Pradeilles, Elisabeth Cortier, Cedric Hassen-Khodja, Leticia Arias, Maria Ceprian-Costoso, Antoine Picot, Anne-Laure Mausset-Bonnefont, Chantal Cazevieille, Frederic Fiore, and Pascale Bomont. Disease mutation in gigaxonin-e3 ligase recapitulates giant axonal neuropathy in mice. Acta Neuropathologica Communications, Dec 2025. URL: https://doi.org/10.1186/s40478-025-02138-1, doi:10.1186/s40478-025-02138-1. This article has 0 citations and is from a peer-reviewed journal.

21. (shirakaki2022geneticapproachesfor pages 11-12): Satomi Shirakaki, Rohini Roy Roshmi, and Toshifumi Yokota. Genetic approaches for the treatment of giant axonal neuropathy. Journal of Personalized Medicine, 13:91, Dec 2022. URL: https://doi.org/10.3390/jpm13010091, doi:10.3390/jpm13010091. This article has 4 citations.

22. (paumier2024neurofilamentaccumulationdisrupts pages 1-5): Jean-Michel Paumier, James Zewe, Melissa R Pergande, Meghana Venkatesan, Eitan Israeli, Chiranjit Panja, Natasha Snider, Jeffrey Savas, and Puneet Opal. Neurofilament accumulation disrupts autophagy in giant axonal neuropathy. JCI Insight, Mar 2025. URL: https://doi.org/10.1101/2024.03.29.587353, doi:10.1101/2024.03.29.587353. This article has 6 citations and is from a domain leading peer-reviewed journal.

23. (israeli2016intermediatefilamentaggregates pages 6-7): Eitan Israeli, Dilyan I. Dryanovski, Paul T. Schumacker, Navdeep S. Chandel, Jeffrey D. Singer, Jean P. Julien, Robert D. Goldman, and Puneet Opal. Intermediate filament aggregates cause mitochondrial dysmotility and increase energy demands in giant axonal neuropathy. Human molecular genetics, 25 11:2143-2157, Mar 2016. URL: https://doi.org/10.1093/hmg/ddw081, doi:10.1093/hmg/ddw081. This article has 61 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Giant_Axonal_Neuropathy_1-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.