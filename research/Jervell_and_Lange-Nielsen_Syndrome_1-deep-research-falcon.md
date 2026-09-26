---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-17T21:03:12.573649'
end_time: '2026-08-17T21:13:12.923594'
duration_seconds: 600.35
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Jervell and Lange-Nielsen Syndrome 1
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 4
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Jervell_and_Lange-Nielsen_Syndrome_1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Jervell and Lange-Nielsen Syndrome 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Jervell and Lange-Nielsen Syndrome 1** covering all of the
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
- **Disease Name:** Jervell and Lange-Nielsen Syndrome 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Jervell and Lange-Nielsen Syndrome 1** covering all of the
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


# Jervell and Lange-Nielsen Syndrome 1: Disease Characteristics Report

## Scope and evidence conventions

**Jervell and Lange-Nielsen syndrome 1 (JLNS1)** is specifically the **biallelic KCNQ1-related** disorder. It must be distinguished from **JLNS2**, caused by biallelic **KCNE1** variants, and from broader congenital long-QT syndrome (LQTS) evidence. Where subtype-specific data are unavailable, this report labels evidence as applying to **all JLNS** or **general LQTS** rather than assuming it is JLNS1-specific. Most available information is aggregated from disease resources, cohorts, and published families—not individual electronic health records.

A knowledge-base-ready summary is provided below.

| Domain | JLNS1 (KCNQ1) summary | JLNS2 distinction / caveat | Key supported numbers | Ontology suggestions | Evidence |
|---|---|---|---|---|---|
| Identity / identifiers | Jervell and Lange-Nielsen syndrome 1 is the KCNQ1-related form of autosomal-recessive cardioauditory long-QT syndrome with congenital sensorineural deafness and marked QT prolongation; disease-level resources support MONDO:0024540 for JLNS1, while the broader syndrome is MONDO:0002441. | JLNS2 is the KCNE1-related subtype; do not merge subtype-specific assertions when a source discusses broader JLNS. | None subtype-specific beyond MONDO assignment in retrieved evidence. | MONDO:0024540; MeSH: Jervell-Lange Nielsen Syndrome; HP:0000365; HP:0001649 | (OpenTargets Search: Jervell and Lange-Nielsen syndrome-KCNQ1, oertli2021molecularmechanismof pages 1-2, oertli2021molecularmechanismof pages 12-13, oertli2021molecularmechanismof pages 2-4) |
| Causal gene and inheritance | Primary causal gene is KCNQ1; inheritance is autosomal recessive / biallelic with loss-of-function mechanism. Both truncating and missense variants leading to loss of function are relevant for LQTS/JLNS. | KCNE1 causes JLNS2; KCNE1 cases appear less common and may have a less severe clinical course than KCNQ1-associated JLNS. | Approximately 90% of JLNS cases are due to KCNQ1 mutations in one review/case-based source. | HGNC:6294 (KCNQ1); GO:0006813; GO:0005267 | (qiu2020jervellandlangenielsen pages 1-2, josephs2023beyondgenediseasevalidity pages 9-10, crotti2008congenitallongqt pages 4-5) |
| Cardinal phenotypes and frequencies | Core phenotype is profound congenital bilateral sensorineural hearing loss plus prolonged QTc, often with syncope/seizures and risk of torsades/ventricular fibrillation/sudden death. Onset is often congenital/early childhood. | Severity appears worse in JLNS1/KCNQ1 than JLNS2/KCNE1 in cohort/review evidence. | In a cooperative study of 187 J-LN patients, almost 90% had cardiac events, 50% were symptomatic by age 3 years, mean QTc was 557 ± 65 ms; JLNS is commonly defined by QTc >500 ms. | HP:0000365; HP:0001649; HP:0001279; HP:0002133; HP:0011675 | (uysal2017“homozygousandcompound pages 1-2, qiu2020jervellandlangenielsen pages 1-2, crotti2008congenitallongqt pages 4-5) |
| Triggers / natural history | Events are precipitated by adrenergic or physiologic stressors; misdiagnosis as epilepsy can occur because arrhythmic syncope may present with seizure-like episodes. | Trigger data are largely reported for broader JLNS rather than subtype-exclusive JLNS1 cohorts. | Reported triggers include exercise, emotion, swimming, auditory stimuli, anesthesia, and fever; >25% sudden cardiac death reported in one review/case-based source. | HP:0001250; NCIT:C50595 (Syncope) | (uysal2017“homozygousandcompound pages 6-7, qiu2020jervellandlangenielsen pages 1-2, qiu2020jervellandlangenielsen pages 5-7) |
| Molecular mechanism | KCNQ1 encodes Kv7.1, which with KCNE1 forms the IKs channel. In heart, loss of IKs delays repolarization and prolongs action potential duration/QT. In inner ear stria vascularis, impaired K+ secretion/endocochlear potential disrupts potassium homeostasis causing deafness; severe loss can also associate with vestibular dysfunction and hair-cell loss in models. Residual function may explain atypical recessive LQT1 without deafness. | JLNS2 shares pathway logic through KCNE1 but subtype-specific gene/protein defect differs. | One mechanistic review notes JLNS can occur when KCNQ1 protein level falls below about 10% of normal. | GO:0002027; GO:1903779; GO:0060088; UBERON:0002046; CL:0000586 | (oertli2021molecularmechanismof pages 1-2, oertli2021molecularmechanismof pages 2-4, qiu2020jervellandlangenielsen pages 1-2, qiu2020jervellandlangenielsen pages 5-7) |
| Pathogenic variant spectrum / modifiers | Reported JLNS1 variants include homozygous missense, nonsense/frameshift, splice-site, and compound heterozygous combinations; examples include p.Arg243His, c.477+1G>A, p.Arg174Cys, p.Arg366Gln, c.1741A>T (p.Lys581Ter), and c.477+5G>A. Additional variants in other arrhythmia genes (for example RYR2, NKX2-5 in one case) were proposed as possible severity modifiers. | Modifier evidence is limited and case-based, not established as routine causal annotation. | Exact example QTc values in case reports included 520 ms and 530 ms. | SO:0001583; SO:0001587; SO:0001627; SO:0001578 | (uysal2017“homozygousandcompound pages 2-5, uysal2017“homozygousandcompound pages 5-6, uysal2017“homozygousandcompound pages 1-2, qiu2020jervellandlangenielsen pages 5-7) |
| Diagnostics | Diagnosis is based on ECG plus congenital deafness phenotype and confirmatory molecular testing. Suggested workup: 12-lead ECG/QTc, hearing evaluation/audiology, family history, and targeted sequencing/panel testing; exome/genome sequencing can support diagnosis in rare disease workflows. | Subtype resolution requires genetic testing because both KCNQ1 and KCNE1 can cause JLNS. | QTc >500 ms is a common diagnostic clue; one report used a 127-gene deafness panel/NGS, and another emphasized broad targeted cardiac panels. | LOINC/ECG concept; HP:0001649; HP:0000365; NCIT:C47891 (Genetic Testing) | (uysal2017“homozygousandcompound pages 1-2, uysal2017“homozygousandcompound pages 6-7, qiu2020jervellandlangenielsen pages 1-2, yu2023precisionmedicinefor pages 1-2) |
| Treatment / real-world management | First-line therapy is beta-blockade, with non-selective agents such as nadolol or propranolol generally preferred in LQTS guidance. ICD is used for cardiac arrest survivors or persistent breakthrough events; LCSD is used in refractory/intolerant high-risk cases. Cochlear implantation can substantially improve hearing but requires peri-anesthetic arrhythmia precautions. | JLNS1 often has particularly high arrhythmic risk, so escalation beyond beta-blockers is common; KCNE1-associated JLNS may be milder. | In general LQTS guidance, arrhythmic recurrence after cardiac arrest is about 14% within 5 years despite therapy; one review states LCSD can reduce cardiac events by about 90% in high-risk LQTS; in a JLNS cohort/review, beta-blockers had limited efficacy and LCSD appeared ineffective. | NCIT:C945 (Beta Adrenergic Receptor Blocker Therapy); NCIT:C27996 (Implantable Cardioverter Defibrillator); NCIT:C80466 (Sympathectomy); NCIT:C15220 (Cochlear Implantation) | (uysal2017“homozygousandcompound pages 5-6, uysal2017“homozygousandcompound pages 6-7, qiu2020jervellandlangenielsen pages 5-7, balestra2024congenitallongqt pages 8-9, hauwanga2024managementoflong pages 5-6, crotti2008congenitallongqt pages 4-5) |
| Prognosis | Prognosis remains guarded relative to many other LQTS forms because events begin early and treatment may be less protective; however outcomes improve with recognition, arrhythmia prevention, and hearing intervention. | Worse prognosis is particularly associated with KCNQ1-mutant J-LN in expert review. | Untreated LQTS mortality within 1 year was cited as 21% in one case-based review; >25% sudden cardiac death reported for JLNS in another source. | HP:0001699; NCIT:C28554 (Sudden Cardiac Death) | (uysal2017“homozygousandcompound pages 5-6, qiu2020jervellandlangenielsen pages 1-2, crotti2008congenitallongqt pages 4-5) |
| Model organisms / systems | Kcnq1-null mice recapitulate major JLNS traits including deafness, vestibular dysfunction, altered cardiac repolarization, collapsed Reissner membrane, and massive hair-cell loss. Human iPSC-cardiomyocyte models are being used to study KCNQ1-related LQTS/JLNS mechanisms and therapeutic screening; CRISPR correction and gene-replacement concepts are preclinical. | No established naturally occurring veterinary JLNS1 model was identified in retrieved evidence. | None beyond qualitative recapitulation. | NCBITaxon:10090; CL:0000746 (cardiomyocyte); UBERON:0001851 (stria vascularis) | (qiu2020jervellandlangenielsen pages 1-2, yu2023precisionmedicinefor pages 1-2) |
| 2023-2024 developments | 2023 CardiacG2P provided structured curation that specifically states both PTCs and missense KCNQ1 loss-of-function variants are relevant to LQTS/JLNS and improves variant prioritization. 2023-2024 reviews highlight patient-specific iPSC models, CRISPR-enabled precision-medicine workflows, and updated pediatric/ESC-aligned management. A phase 4 single-subject trial tested acute IV diltiazem QT effects in genetically confirmed JLNS (NCT06534671; first posted 2024-08-02; completed 2024-10-23). | These are emerging or platform-level advances; none constitute an approved JLNS1 molecular therapy. | CardiacG2P sensitivity for retained P/LP variants was 281/285 (98.6%) in benchmark testing; the diltiazem study enrolled 1 participant. | NCIT:C15206 (Clinical Trial); NCIT:C129000 (Induced Pluripotent Stem Cell) | (NCT06534671 chunk 1, josephs2023beyondgenediseasevalidity pages 1-2, josephs2023beyondgenediseasevalidity pages 9-10, balestra2024congenitallongqt pages 8-9, hauwanga2024managementoflong pages 5-6, yu2023precisionmedicinefor pages 1-2) |


*Table: This table condenses subtype-specific knowledge for Jervell and Lange-Nielsen syndrome 1 into knowledge-base-ready rows covering identity, mechanism, phenotypes, diagnosis, treatment, prognosis, models, and recent developments. It emphasizes the distinction between KCNQ1-related JLNS1 and KCNE1-related JLNS2 and includes ontology suggestions for downstream annotation.*

## 1. Disease information

### Definition

JLNS1 is a rare, severe, congenital **cardioauditory ion-channel disorder** characterized by profound bilateral sensorineural hearing loss and markedly prolonged ventricular repolarization, usually QTc >500 ms, with susceptibility to torsades de pointes, ventricular fibrillation, syncope, seizure-like episodes, cardiac arrest, and sudden death. It results from two pathogenic alleles in **KCNQ1**, whereas JLNS2 is attributable to **KCNE1**. Open Targets associates JLNS1 (MONDO:0024540) most strongly with KCNQ1; its weaker KCNE1 association likely reflects cross-mapping of the broader JLNS concept and should not redefine subtype 1. (OpenTargets Search: Jervell and Lange-Nielsen syndrome-KCNQ1, oertli2021molecularmechanismof pages 1-2, qiu2020jervellandlangenielsen pages 1-2)

**Exact abstract wording:** “JLNS is a rare but severe autosomal recessive disease characterized by profound congenital deafness and a prolonged QTc interval (greater than 500 milliseconds).” Qiu et al., published **16 May 2020**, DOI: [10.1155/2020/3569359](https://doi.org/10.1155/2020/3569359). (qiu2020jervellandlangenielsen pages 1-2)

### Identifiers and synonyms

- **MONDO:** **MONDO:0024540**, Jervell and Lange-Nielsen syndrome 1. Broader JLNS: MONDO:0002441. (OpenTargets Search: Jervell and Lange-Nielsen syndrome-KCNQ1)
- **OMIM:** commonly represented as **JLNS1, 220400**; KCNQ1 gene entry **607542**. These identifiers should be verified against the current OMIM release before automated ingestion because OMIM itself was not directly retrieved.
- **MeSH:** **D029593**, Jervell-Lange Nielsen Syndrome. (NCT06534671 chunk 1)
- **Orphanet:** broader JLNS is generally catalogued as **ORPHA:90647**; subtype-specific resolution should be checked in the live Orphanet release.
- **ICD-10:** no reliable JLNS1-specific billable code; it is generally represented under congenital long-QT syndrome/cardiac conduction or congenital-malformation categories according to national modification.
- **ICD-11:** no subtype-specific code was established from retrieved material; use the current ICD-11 browser rather than inferring one.
- **Synonyms:** JLNS type 1; Jervell–Lange-Nielsen syndrome type 1; KCNQ1-related JLNS; autosomal-recessive long-QT syndrome with congenital deafness; cardioauditory long-QT syndrome; surdocardiac syndrome.

## 2. Etiology

### Causal factors and genetic risk

JLNS1 is a **Mendelian autosomal-recessive disorder caused by germline biallelic loss-of-function KCNQ1 variants**, either homozygous or compound heterozygous. Disease-relevant classes include missense variants that impair channel function or trafficking, nonsense and frameshift variants, splice-altering variants, and less commonly exon-level copy-number changes. A 2023 expert-curated CardiacG2P analysis explicitly concluded that both protein-truncating and missense loss-of-function KCNQ1 variants cause LQTS/JLNS. (josephs2023beyondgenediseasevalidity pages 1-2, josephs2023beyondgenediseasevalidity pages 9-10)

Reported JLNS1 genotypes include:

- homozygous **c.728G>A (p.Arg243His)**;
- compound heterozygous **c.477+1G>A / c.520C>T (p.Arg174Cys)**;
- homozygous **c.1097G>A (p.Arg366Gln)**;
- compound heterozygous **c.1741A>T (p.Lys581Ter) / c.477+5G>A**. (uysal2017“homozygousandcompound pages 2-5, uysal2017“homozygousandcompound pages 1-2, qiu2020jervellandlangenielsen pages 1-2)

These examples are not a substitute for current ClinVar assertions. Variant classification should use ACMG/AMP criteria, segregation, population frequency, phenotype specificity, RNA evidence for splice variants, and functional electrophysiology. Pathogenic alleles are expected to be individually rare in gnomAD; no universal allele-frequency value applies. The variants are **germline**, not somatic.

### Modifiers and protective factors

Residual Kv7.1/IKs activity is a major biological modifier: severe reduction tends to produce cardioauditory disease, whereas partial function can produce recessive LQT1 without deafness. In vitro work on homozygous **c.1892_1893insC (p.Pro631fs*20)** showed loss of IKs only in homomeric mutant complexes, while wild-type-containing complexes were rescued by KCNE1, explaining unaffected heterozygotes and atypical recessive LQTS. (oertli2021molecularmechanismof pages 1-2, oertli2021molecularmechanismof pages 2-4)

One severe case also carried **RYR2 p.Ile449Arg** and **NKX2-5 p.Cys270Tyr**, proposed as modifiers; this remains a single-family hypothesis, not a validated modifier panel. (uysal2017“homozygousandcompound pages 2-5, uysal2017“homozygousandcompound pages 1-2)

No reproducible **protective allele**, diet, supplement, or environmental exposure preventing JLNS1 occurrence has been established. Clinically protective measures instead reduce arrhythmic risk after disease is present.

### Gene–environment interaction

The genotype creates reduced repolarization reserve. Adrenergic stimulation and physiological stress—exercise, swimming, emotion, sudden sound, fever—and peri-anesthetic factors can then trigger ventricular arrhythmia. QT-prolonging drugs, hypokalemia, hypomagnesemia, bradycardia, and poor medication adherence can further erode repolarization reserve. A KCNQ1-JLNS child developed life-threatening arrhythmia after cochlear-implant anesthesia, directly illustrating this interaction. (qiu2020jervellandlangenielsen pages 1-2, qiu2020jervellandlangenielsen pages 5-7)

Smoking, alcohol, diet, infection, occupation, pollution, and toxins are **not causal factors** for this Mendelian syndrome. Fever or electrolyte loss can nevertheless act as event triggers.

## 3. Phenotypes

| Phenotype | Type and characteristics | Frequency/onset | Suggested HPO |
|---|---|---|---|
| Bilateral sensorineural hearing loss | Congenital or very early, usually severe-to-profound and persistent; impairs speech/language without intervention | Cardinal phenotype, although rare residual-function exceptions occur | **HP:0000365**, **HP:0000407** |
| Long QT interval | ECG sign; typically marked, persistent QTc prolongation | Mean QTc **557±65 ms** in a 187-patient JLNS cohort; commonly >500 ms | **HP:0001657** / long QT interval |
| Syncope | Episodic, often exertional or emotion-triggered; may be recurrent | Almost 90% of the cohort experienced cardiac events | **HP:0001279** |
| Seizure-like episodes/anoxic seizures | Behavioral/neurologic manifestation secondary to cerebral hypoperfusion; frequently mistaken for epilepsy | Variable; often childhood | **HP:0001250** |
| Torsades/ventricular tachyarrhythmia | Episodic, severe, potentially degenerating to ventricular fibrillation | High-risk defining complication | **HP:0001664**, **HP:0004756** |
| Sudden cardiac arrest/death | Catastrophic complication | One review reported >25% sudden cardiac death | **HP:0001699** |
| Congenital/fetal or neonatal bradycardia | Clinical/ECG sign in some severe cases | Variable | **HP:0001662** |
| Vestibular dysfunction/balance impairment | Inner-ear manifestation supported strongly by knockout models and clinical reports | Frequency not robustly quantified here | **HP:0001751**, **HP:0001288** |

Cohort evidence indicates a severe early course: **almost 90%** of 187 JLNS patients had cardiac events, **50% were symptomatic by age three**, and mean QTc was **557±65 ms**. This cohort combined KCNQ1- and KCNE1-related JLNS, but KCNQ1 disease had the more severe course. (crotti2008congenitallongqt pages 4-5)

Quality-of-life burdens include communication and educational disability from deafness, activity restrictions, medication burden, anxiety concerning sudden death, recurrent hospitalization, ICD shocks, and family/caregiver stress. No JLNS1-specific EQ-5D, SF-36, or PROMIS dataset was identified.

## 4. Genetic and molecular information

### Gene and protein

- **Gene:** KCNQ1, potassium voltage-gated channel subfamily Q member 1; **HGNC:6294**.
- **Location:** chromosome **11p15.5**; 16 coding exons were described in the retrieved source.
- **Protein:** Kv7.1/KvLQT1, a six-transmembrane voltage-gated potassium-channel α-subunit.
- **Complex:** Kv7.1 coassembles with KCNE1/minK to generate the slowly activating delayed rectifier current **IKs**. (oertli2021molecularmechanismof pages 1-2, qiu2020jervellandlangenielsen pages 1-2)

### Functional consequences

Pathogenic variants can cause defective voltage sensing/gating, pore conductance, tetramer assembly, KCNE1 interaction, protein stability, trafficking, or cell-surface expression. The p.Lys581Ter variant removes part of the C-terminal A-domain needed for normal channel trafficking/assembly. (qiu2020jervellandlangenielsen pages 1-2, qiu2020jervellandlangenielsen pages 5-7)

The predominant mechanism is **loss of function**, not gain of function. Dominant-negative effects may occur for particular alleles, but JLNS1 requires a disease-causing allele on each homolog. Large chromosomal abnormalities are not the usual mechanism; deletion/duplication analysis remains relevant when sequencing finds only one allele. No consistent disease-specific DNA-methylation, histone, or chromatin signature is established. KCNQ1 resides within an imprinted region, but JLNS1 itself is not ordinarily classified as an imprinting disorder.

## 5. Environmental information

There is no infectious, toxic, nutritional, radiation, pollution, occupational, or lifestyle cause. Relevant acquired **arrhythmia modifiers** include:

- QT-prolonging medication exposure;
- hypokalemia and hypomagnesemia;
- dehydration or illness causing electrolyte loss;
- fever;
- intense adrenergic stimulation;
- anesthesia and perioperative sympathetic/electrolyte shifts;
- missed β-blocker doses.

Exercise, emotion, swimming, auditory stimuli, anesthesia, and fever are specifically reported event triggers in children with JLNS. (qiu2020jervellandlangenielsen pages 1-2)

## 6. Mechanism and pathophysiology

### Cardiac causal chain

**Biallelic KCNQ1 loss of function → reduced Kv7.1/KCNE1 IKs → impaired phase-3 repolarizing K+ current and reduced adaptation to faster heart rates → prolonged cardiomyocyte action-potential duration → prolonged QTc and increased dispersion of repolarization → early afterdepolarizations/torsades de pointes → syncope, anoxic seizure, ventricular fibrillation, or sudden death.** (oertli2021molecularmechanismof pages 1-2, oertli2021molecularmechanismof pages 2-4, yu2023precisionmedicinefor pages 1-2)

Relevant cell type: ventricular cardiomyocyte (**CL:0000746**). Suggested GO terms include potassium-ion transmembrane transport (**GO:0071805**), regulation of cardiac muscle-cell action potential (**GO:0098901**), cardiac muscle-cell action-potential repolarization (**GO:0086009**), and voltage-gated potassium-channel complex (**GO:0008076**).

### Auditory/vestibular causal chain

**Loss of Kv7.1/KCNE1 in stria-vascularis marginal cells → impaired K+ secretion into endolymph → loss of endocochlear potential and endolymph homeostasis → collapse of cochlear structures and secondary sensory-hair-cell degeneration → congenital severe-to-profound sensorineural deafness.** Vestibular dark-cell dysfunction can similarly disturb vestibular endolymph. Kcnq1-null mice show collapsed Reissner membrane, massive hair-cell loss, and malformed saccule, utricle, and semicircular ducts. (qiu2020jervellandlangenielsen pages 1-2, qiu2020jervellandlangenielsen pages 5-7)

Suggested terms: sensory epithelial cell of cochlea/hair cell (**CL:0000202**), marginal cell of stria vascularis, potassium-ion homeostasis (**GO:0055075**), sensory perception of sound (**GO:0007605**), cochlea (**UBERON:0001844**), stria vascularis (**UBERON:0001851**), and vestibular apparatus (**UBERON:0004681**).

### Other molecular profiling

No validated JLNS1-specific clinical transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omic signature was identified. Patient-specific iPSC-cardiomyocytes are increasingly used for mechanistic phenotyping and drug testing, but their immaturity and cellular heterogeneity limit direct clinical extrapolation. (yu2023precisionmedicinefor pages 1-2)

## 7. Anatomical structures affected

1. **Heart:** ventricular myocardium/cardiac conduction physiology; the heart is generally structurally normal. Primary defect is electrical rather than inflammatory, ischemic, fibrotic, or metabolic.
2. **Inner ear:** bilateral cochlea, especially stria vascularis and scala media/endolymph compartment; secondary organ-of-Corti hair-cell injury. Vestibular labyrinth may also be affected.
3. **Subcellular site:** plasma membrane voltage-gated potassium-channel complex; trafficking defects can involve biosynthetic processing before surface expression.

Suggested anatomy terms include heart (**UBERON:0000948**), myocardium (**UBERON:0002349**), cochlea (**UBERON:0001844**), stria vascularis (**UBERON:0001851**), organ of Corti (**UBERON:0002227**), and plasma membrane (**GO:0005886**). Hearing loss is bilateral; cardiac disease has no meaningful lateralization.

## 8. Temporal development

JLNS1 is congenital and lifelong. Hearing loss is present at birth or recognized in infancy; cardiac manifestations may begin prenatally with bradycardia or during early childhood with syncope/seizures. Half of patients in the mixed-JLNS cohort were symptomatic by age three. (crotti2008congenitallongqt pages 4-5)

The course is **chronic with episodic acute arrhythmias**, not conventionally staged and not relapsing-remitting. Deafness generally does not remit spontaneously. Arrhythmic risk persists lifelong but is modifiable by treatment and avoidance of triggers. Critical windows include fetal/neonatal detection, infancy before a first cardiac event, cochlear-implant timing for language acquisition, medication initiation, and all anesthetic procedures.

## 9. Inheritance and population

### Epidemiology

Worldwide prevalence has been estimated at approximately **1 per 1,000,000 to 1 per 200,000**. Approximately **90% of all JLNS** was attributed to KCNQ1 in the 2020 report, making JLNS1 the major molecular subtype. These estimates are uncertain because the disorder is exceptionally rare, can be misdiagnosed as epilepsy, and may be enriched in founder or consanguineous populations. (qiu2020jervellandlangenielsen pages 1-2)

No robust annual incidence, sex ratio, or age-stratified population estimate was identified. Both sexes are genetically affected equally; sex and hormonal state can modify arrhythmic risk in LQTS generally.

### Recurrence and penetrance

For two heterozygous carrier parents, each pregnancy has a theoretical **25% affected, 50% carrier, and 25% non-carrier** probability. Penetrance of the classic cardioauditory phenotype is high but not absolute: residual-function biallelic genotypes can cause recessive LQTS without deafness, demonstrating variable expressivity. Heterozygous relatives may be asymptomatic or manifest dominant LQT1 depending on the allele’s functional effect. (uysal2017“homozygousandcompound pages 5-6, oertli2021molecularmechanismof pages 1-2)

Consanguinity increases the probability that both parents carry the same rare allele. Founder effects are reported in Scandinavian populations, but no precise founder-variant frequency was adequately retrieved. Anticipation is not expected; germline mosaicism is theoretically possible but not a recognized major mechanism.

## 10. Diagnostics

### Clinical and functional evaluation

Recommended evaluation comprises:

1. **12-lead ECG** with manually verified QT/QTc; repeat ECGs because measurement and rate correction can vary.
2. Holter monitoring and exercise testing where useful for rhythm burden and repolarization behavior.
3. Detailed history of exertional/emotional syncope, seizures, cardiac arrest, medications, and sudden deaths.
4. Formal audiology—auditory brainstem response in infants and age-appropriate pure-tone/speech testing.
5. Serum potassium, magnesium, calcium, and thyroid assessment to identify acquired aggravators, not to diagnose the genetic disease.
6. Device interrogation where an ICD/pacemaker is present.

Profound congenital deafness plus QTc >500 ms is highly suggestive, but molecular confirmation is required to assign JLNS1 rather than JLNS2. (uysal2017“homozygousandcompound pages 1-2, qiu2020jervellandlangenielsen pages 1-2)

### Genetic testing

- Begin with a validated congenital LQTS/cardioauditory panel including **KCNQ1 and KCNE1**, with sequence and exon-level deletion/duplication analysis.
- A combined deafness/arrhythmia panel is useful when deafness is the presenting feature; one study used a 127-gene deafness panel, while another advocated broad cardiac panels when severity was unexplained. (uysal2017“homozygousandcompound pages 1-2, uysal2017“homozygousandcompound pages 6-7, qiu2020jervellandlangenielsen pages 1-2)
- If only one KCNQ1 allele is found, pursue CNV analysis, splice/RNA studies where available, and exome or genome reanalysis.
- WES/WGS can identify atypical or blended diagnoses but may miss repeat expansions or poorly covered structural/noncoding variants. CMA, karyotype, FISH, mitochondrial testing, and repeat-expansion testing are not first-line unless another phenotype indicates them.
- Functional patch-clamp studies are research/variant-resolution tools, not routine clinical assays.

### Differential diagnosis

Differentials include Romano-Ward LQT1; JLNS2/KCNE1; acquired long QT; Timothy syndrome; Andersen-Tawil syndrome; catecholaminergic polymorphic ventricular tachycardia; epilepsy; vasovagal syncope; and nonsyndromic congenital deafness such as GJB2- or SLC26A4-related disease. The combination of profound congenital deafness, marked QT prolongation, and biallelic KCNQ1 variants distinguishes JLNS1.

### Screening

All first-degree relatives should receive ECG and targeted familial-variant testing. Hearing screening alone is insufficient because a child can pass newborn screening and later be recognized as hearing impaired, as occurred in the reported KCNQ1 family. (qiu2020jervellandlangenielsen pages 1-2)

Population ECG/genomic newborn screening remains investigational; cascade screening is the established high-yield approach.

## 11. Outcome and prognosis

JLNS is among the most malignant LQTS forms. In the 187-patient cohort, almost 90% experienced cardiac events and half were symptomatic by age three. KCNQ1-associated disease had a substantially more severe course than KCNE1-associated disease. (crotti2008congenitallongqt pages 4-5)

A separate review reported sudden cardiac death in **>25%**, although this is historical/mixed-management evidence and should not be interpreted as a contemporary treated JLNS1 mortality rate. (qiu2020jervellandlangenielsen pages 1-2)

Poor prognostic factors include very long QTc, early symptoms, prior cardiac arrest, recurrent events despite β-blockade, KCNQ1 rather than KCNE1 etiology, nonadherence, and exposure to avoidable triggers. No validated JLNS1-specific five- or ten-year survival estimate or prognostic molecular biomarker was identified.

Hearing generally does not recover medically, but cochlear implantation can produce good auditory performance. ICD shocks and activity restrictions may cause substantial psychosocial morbidity. Recovery from the genetic disorder is not expected; risk management is lifelong.

## 12. Treatment

### Standard strategy

1. **Nonselective β-blocker therapy:** nadolol or propranolol is generally preferred over metoprolol for congenital LQTS. β-blockade is foundational but is less completely protective in JLNS than in typical LQT1. (uysal2017“homozygousandcompound pages 5-6, hauwanga2024managementoflong pages 5-6, crotti2008congenitallongqt pages 4-5)
2. **ICD:** indicated after resuscitated cardiac arrest and considered for recurrent syncope/ventricular arrhythmia despite optimized medication. General 2022 ESC-aligned guidance reports approximately **14% five-year recurrence** after cardiac arrest despite therapy. Pediatric device complications include infection, lead failure/displacement, inappropriate shocks, and psychological burden. (balestra2024congenitallongqt pages 8-9)
3. **Left cardiac sympathetic denervation:** considered for breakthrough events, β-blocker intolerance, recurrent ICD shocks, or when ICD implantation is declined/contraindicated. General LQTS literature reports major event reduction, but historical JLNS cohort evidence suggested limited protection; it is not curative. (balestra2024congenitallongqt pages 8-9, hauwanga2024managementoflong pages 5-6, crotti2008congenitallongqt pages 4-5)
4. **Cochlear implantation:** standard hearing rehabilitation for profound loss when hearing aids are inadequate; published cases show substantial hearing benefit. Surgery requires electrophysiology/cardiology and anesthesia planning, continued β-blockade, electrolyte optimization, avoidance of QT-prolonging agents, continuous ECG, and immediately available defibrillation. (uysal2017“homozygousandcompound pages 6-7, qiu2020jervellandlangenielsen pages 5-7)
5. **Supportive care:** speech/language therapy, educational accommodation, family CPR training, emergency action plans, medical-alert identification, and psychological support.

Suggested NCIt intervention concepts: beta-adrenergic receptor blocker therapy; implantable cardioverter-defibrillator; sympathectomy/LCSD; cochlear implantation; genetic counseling.

### Experimental therapy and trials

No gene, RNA, or cell therapy is approved for JLNS1. Preclinical approaches include KCNQ1 gene replacement, CRISPR correction, patient-specific iPSC drug screening, and suppression-and-replacement constructs. Kcnq1 replacement in immature mouse scala media improved hearing, cochlear morphology, and vestibular function, but this has not established human safety or efficacy. (qiu2020jervellandlangenielsen pages 1-2, yu2023precisionmedicinefor pages 1-2)

**NCT06534671**, first posted **2 August 2024**, was a completed phase-4, open-label, single-group study of acute IV **diltiazem** in genetically confirmed adult JLNS. It enrolled **one participant** and measured short-term QT effects after 0.25 mg/kg, with a possible 0.35 mg/kg second dose. This is exploratory single-subject evidence and does not support routine diltiazem treatment. [ClinicalTrials.gov record](https://clinicaltrials.gov/study/NCT06534671). (NCT06534671 chunk 1)

## 13. Prevention

Primary prevention of de novo disease in an individual is not possible after conception, but reproductive options include carrier testing, partner testing, prenatal diagnosis, and preimplantation genetic testing when familial variants are known.

Secondary prevention consists of early ECG/genetic diagnosis in deaf infants, cascade testing, and immediate treatment before a first arrhythmia. Tertiary prevention includes strict β-blocker adherence; avoidance of QT-prolonging drugs; prompt correction of potassium, magnesium, and calcium abnormalities; fever/dehydration management; individualized exercise/swimming precautions; supervised anesthesia; and ICD/LCSD escalation when indicated. There is no JLNS-specific vaccine or infectious prophylaxis.

## 14. Other species and natural disease

No well-established naturally occurring companion-animal or wildlife disease directly equivalent to human KCNQ1-JLNS1 was identified. Therefore, breed ontology, veterinary prevalence, transmission, and zoonotic potential are **not applicable/unknown**. The disorder is genetic and noncommunicable.

Orthologous Kcnq1/Kcne1 channel biology is evolutionarily conserved in mammals. Relevant taxa include human (**NCBI Taxon 9606**) and laboratory mouse (**NCBI Taxon 10090**).

## 15. Model organisms and experimental systems

### Mouse

**Kcnq1-null mice** reproduce major disease components: deafness, vestibular dysfunction, and abnormal cardiac repolarization. Their inner ears show collapsed Reissner membrane, extensive hair-cell loss, and abnormalities of the saccule, utricle, and semicircular ducts. This provides strong mechanistic support for KCNQ1-dependent endolymph homeostasis. Limitations include species-specific cardiac electrophysiology and differences in developmental timing and arrhythmic susceptibility. (qiu2020jervellandlangenielsen pages 1-2)

### Heterologous cellular models

Xenopus oocytes and mammalian expression systems permit voltage-clamp measurement of IKs, trafficking, assembly, and dominant-negative or recessive behavior. Such work demonstrated that KCNE1 could rescue function in complexes containing wild-type KCNQ1 for an atypical recessive variant. (oertli2021molecularmechanismof pages 1-2)

### Human iPSC models

Patient-specific iPSC-derived cardiomyocytes reproduce prolonged action potentials and allow isogenic CRISPR correction, mechanistic study, and high-throughput drug testing. A 2023 review described WGS, CRISPR editing, machine learning, and iPSC cardiomyocytes as converging platforms for LQTS precision medicine. These remain research systems because iPSC cardiomyocytes are relatively immature and do not fully reproduce whole-heart autonomic, conduction, pharmacokinetic, or developmental physiology. (yu2023precisionmedicinefor pages 1-2)

## Recent developments and expert assessment

The most consequential 2023–2024 developments were not new approved treatments but improvements in **variant interpretation, risk-adapted management, and human disease modeling**. CardiacG2P formally encoded biallelic requirement and KCNQ1 loss-of-function variant classes for scalable genomic interpretation; across its benchmark set it retained 281/285 pathogenic/likely pathogenic variants (**98.6% sensitivity**), although that benchmark was not JLNS1-specific. (josephs2023beyondgenediseasevalidity pages 1-2, josephs2023beyondgenediseasevalidity pages 9-10)

The 2024 pediatric synthesis of ESC guidance reinforced nonselective β-blockade, selective use of ICD and LCSD, and careful reassessment of risk after therapy. Meanwhile, iPSC/CRISPR work supports eventual genotype-specific treatment but remains preclinical. (balestra2024congenitallongqt pages 8-9, yu2023precisionmedicinefor pages 1-2)

### Overall expert interpretation

JLNS1 should be treated as a **medical emergency in genetic deafness evaluation**: every child with severe congenital sensorineural hearing loss should have a careful history for syncope/seizures and consideration of ECG, especially before anesthesia. Molecular confirmation matters because KCNQ1-related JLNS has greater arrhythmic severity than KCNE1-related disease. The strongest current intervention is coordinated early care—expert β-blockade, trigger avoidance, rapid escalation to device or denervation therapy when warranted, and cochlear rehabilitation—not an experimental molecular therapy. (qiu2020jervellandlangenielsen pages 1-2, qiu2020jervellandlangenielsen pages 5-7, crotti2008congenitallongqt pages 4-5)

## Evidence gaps

Reliable JLNS1-specific estimates remain unavailable for annual incidence, modern treated survival, sex ratio, individual phenotype frequencies, quantitative quality-of-life scores, carrier frequency, penetrance by variant class, validated modifier genes, epigenomic or multi-omic signatures, and naturally occurring veterinary disease. Many published outcome statistics combine JLNS1 and JLNS2 or derive from historical cohorts; database ingestion should preserve those evidence-scope qualifiers.

References

1. (OpenTargets Search: Jervell and Lange-Nielsen syndrome-KCNQ1): Open Targets Query (Jervell and Lange-Nielsen syndrome-KCNQ1, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (oertli2021molecularmechanismof pages 1-2): Annemarie Oertli, Susanne Rinné, Robin Moss, Stefan Kääb, Gunnar Seemann, Britt-Maria Beckmann, and Niels Decher. Molecular mechanism of autosomal recessive long qt-syndrome 1 without deafness. International Journal of Molecular Sciences, 22:1112, Jan 2021. URL: https://doi.org/10.3390/ijms22031112, doi:10.3390/ijms22031112. This article has 13 citations.

3. (oertli2021molecularmechanismof pages 12-13): Annemarie Oertli, Susanne Rinné, Robin Moss, Stefan Kääb, Gunnar Seemann, Britt-Maria Beckmann, and Niels Decher. Molecular mechanism of autosomal recessive long qt-syndrome 1 without deafness. International Journal of Molecular Sciences, 22:1112, Jan 2021. URL: https://doi.org/10.3390/ijms22031112, doi:10.3390/ijms22031112. This article has 13 citations.

4. (oertli2021molecularmechanismof pages 2-4): Annemarie Oertli, Susanne Rinné, Robin Moss, Stefan Kääb, Gunnar Seemann, Britt-Maria Beckmann, and Niels Decher. Molecular mechanism of autosomal recessive long qt-syndrome 1 without deafness. International Journal of Molecular Sciences, 22:1112, Jan 2021. URL: https://doi.org/10.3390/ijms22031112, doi:10.3390/ijms22031112. This article has 13 citations.

5. (qiu2020jervellandlangenielsen pages 1-2): Yue Qiu, Sen Chen, Xia Wu, Wen-Juan Zhang, Wen Xie, Yuan Jin, Le Xie, Kai Xu, Xue Bai, Hui-Min Zhang, Xiao-Zhou Liu, Xiao-Hui Wang, Yu Sun, and Wei-Jia Kong. Jervell and lange-nielsen syndrome due to a novel compound heterozygous kcnq1 mutation in a chinese family. Neural Plasticity, 2020:1-8, May 2020. URL: https://doi.org/10.1155/2020/3569359, doi:10.1155/2020/3569359. This article has 14 citations and is from a peer-reviewed journal.

6. (josephs2023beyondgenediseasevalidity pages 9-10): Katherine S. Josephs, Angharad M. Roberts, Pantazis Theotokis, Roddy Walsh, Philip J. Ostrowski, Matthew Edwards, Andrew Fleming, Courtney Thaxton, Jason D. Roberts, Melanie Care, Wojciech Zareba, Arnon Adler, Amy C. Sturm, Rafik Tadros, Valeria Novelli, Emma Owens, Lucas Bronicki, Olga Jarinova, Bert Callewaert, Stacey Peters, Tom Lumbers, Elizabeth Jordan, Babken Asatryan, Neesha Krishnan, Ray E. Hershberger, C. Anwar A. Chahal, Andrew P. Landstrom, Cynthia James, Elizabeth M. McNally, Daniel P. Judge, Peter van Tintelen, Arthur Wilde, Michael Gollob, Jodie Ingles, and James S. Ware. Beyond gene-disease validity: capturing structured data on inheritance, allelic requirement, disease-relevant variant classes, and disease mechanism for inherited cardiac conditions. Genome Medicine, Oct 2023. URL: https://doi.org/10.1186/s13073-023-01246-8, doi:10.1186/s13073-023-01246-8. This article has 35 citations and is from a highest quality peer-reviewed journal.

7. (crotti2008congenitallongqt pages 4-5): Lia Crotti, Giuseppe Celano, Federica Dagradi, and Peter J Schwartz. Congenital long qt syndrome. Orphanet Journal of Rare Diseases, Jul 2008. URL: https://doi.org/10.1186/1750-1172-3-18, doi:10.1186/1750-1172-3-18. This article has 457 citations and is from a peer-reviewed journal.

8. (uysal2017“homozygousandcompound pages 1-2): Fahrettin Uysal, Burcu Turkgenc, Guven Toksoy, Ozlem M. Bostan, Elif Evke, Oya Uyguner, Cengiz Yakicier, Hulya Kayserili, Ergun Cil, and Sehime G. Temel. “homozygous, and compound heterozygous mutation in 3 turkish family with jervell and lange-nielsen syndrome: case reports”. BMC Medical Genetics, Oct 2017. URL: https://doi.org/10.1186/s12881-017-0474-8, doi:10.1186/s12881-017-0474-8. This article has 11 citations and is from a peer-reviewed journal.

9. (uysal2017“homozygousandcompound pages 6-7): Fahrettin Uysal, Burcu Turkgenc, Guven Toksoy, Ozlem M. Bostan, Elif Evke, Oya Uyguner, Cengiz Yakicier, Hulya Kayserili, Ergun Cil, and Sehime G. Temel. “homozygous, and compound heterozygous mutation in 3 turkish family with jervell and lange-nielsen syndrome: case reports”. BMC Medical Genetics, Oct 2017. URL: https://doi.org/10.1186/s12881-017-0474-8, doi:10.1186/s12881-017-0474-8. This article has 11 citations and is from a peer-reviewed journal.

10. (qiu2020jervellandlangenielsen pages 5-7): Yue Qiu, Sen Chen, Xia Wu, Wen-Juan Zhang, Wen Xie, Yuan Jin, Le Xie, Kai Xu, Xue Bai, Hui-Min Zhang, Xiao-Zhou Liu, Xiao-Hui Wang, Yu Sun, and Wei-Jia Kong. Jervell and lange-nielsen syndrome due to a novel compound heterozygous kcnq1 mutation in a chinese family. Neural Plasticity, 2020:1-8, May 2020. URL: https://doi.org/10.1155/2020/3569359, doi:10.1155/2020/3569359. This article has 14 citations and is from a peer-reviewed journal.

11. (uysal2017“homozygousandcompound pages 2-5): Fahrettin Uysal, Burcu Turkgenc, Guven Toksoy, Ozlem M. Bostan, Elif Evke, Oya Uyguner, Cengiz Yakicier, Hulya Kayserili, Ergun Cil, and Sehime G. Temel. “homozygous, and compound heterozygous mutation in 3 turkish family with jervell and lange-nielsen syndrome: case reports”. BMC Medical Genetics, Oct 2017. URL: https://doi.org/10.1186/s12881-017-0474-8, doi:10.1186/s12881-017-0474-8. This article has 11 citations and is from a peer-reviewed journal.

12. (uysal2017“homozygousandcompound pages 5-6): Fahrettin Uysal, Burcu Turkgenc, Guven Toksoy, Ozlem M. Bostan, Elif Evke, Oya Uyguner, Cengiz Yakicier, Hulya Kayserili, Ergun Cil, and Sehime G. Temel. “homozygous, and compound heterozygous mutation in 3 turkish family with jervell and lange-nielsen syndrome: case reports”. BMC Medical Genetics, Oct 2017. URL: https://doi.org/10.1186/s12881-017-0474-8, doi:10.1186/s12881-017-0474-8. This article has 11 citations and is from a peer-reviewed journal.

13. (yu2023precisionmedicinefor pages 1-2): Yang Yu, Isabelle Deschenes, and Ming-Tao Zhao. Precision medicine for long qt syndrome: patient-specific ipscs take the lead. Expert Reviews in Molecular Medicine, Jan 2023. URL: https://doi.org/10.1017/erm.2022.43, doi:10.1017/erm.2022.43. This article has 23 citations and is from a peer-reviewed journal.

14. (balestra2024congenitallongqt pages 8-9): Elia Balestra, Marco Bobbo, Marco Cittar, Daniela Chicco, Biancamaria D’Agata Mottolese, Egidio Barbi, and Thomas Caiffa. Congenital long qt syndrome in children and adolescents: a general overview. Children, 11:582, May 2024. URL: https://doi.org/10.3390/children11050582, doi:10.3390/children11050582. This article has 20 citations.

15. (hauwanga2024managementoflong pages 5-6): Wilhelmina N Hauwanga, Ryan Chun Chien Yau, Kang Suen Goh, Jose Ittay Castro Ceron, Berley Alphonse, Gurinder Singh, Sara Elamin, Vaishnavi Jamched, Aaron A Abraham, Joshi Purvil, Jeshua N Devan, Gabriella Valentim, Billy McBenedict, Bruno Lima Pessôa, and Evandro T Mesquita. Management of long qt syndrome: a systematic review. Cureus, Jun 2024. URL: https://doi.org/10.7759/cureus.62592, doi:10.7759/cureus.62592. This article has 10 citations.

16. (NCT06534671 chunk 1): Prince Joseph Kannankeril. Diltiazem in Jervell and Lange-Nielsen Syndrome. Vanderbilt University Medical Center. 2024. ClinicalTrials.gov Identifier: NCT06534671

17. (josephs2023beyondgenediseasevalidity pages 1-2): Katherine S. Josephs, Angharad M. Roberts, Pantazis Theotokis, Roddy Walsh, Philip J. Ostrowski, Matthew Edwards, Andrew Fleming, Courtney Thaxton, Jason D. Roberts, Melanie Care, Wojciech Zareba, Arnon Adler, Amy C. Sturm, Rafik Tadros, Valeria Novelli, Emma Owens, Lucas Bronicki, Olga Jarinova, Bert Callewaert, Stacey Peters, Tom Lumbers, Elizabeth Jordan, Babken Asatryan, Neesha Krishnan, Ray E. Hershberger, C. Anwar A. Chahal, Andrew P. Landstrom, Cynthia James, Elizabeth M. McNally, Daniel P. Judge, Peter van Tintelen, Arthur Wilde, Michael Gollob, Jodie Ingles, and James S. Ware. Beyond gene-disease validity: capturing structured data on inheritance, allelic requirement, disease-relevant variant classes, and disease mechanism for inherited cardiac conditions. Genome Medicine, Oct 2023. URL: https://doi.org/10.1186/s13073-023-01246-8, doi:10.1186/s13073-023-01246-8. This article has 35 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Jervell_and_Lange-Nielsen_Syndrome_1-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.