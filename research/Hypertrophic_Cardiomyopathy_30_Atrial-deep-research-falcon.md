---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-19T09:06:36.396060'
end_time: '2026-08-19T09:13:43.178911'
duration_seconds: 426.78
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypertrophic Cardiomyopathy 30, Atrial
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 13
reference_validation:
  total_references: 7
  verified: 6
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.143
  relevance_assessed: 6
  on_topic: 4
  unresolved_references:
  - DOI:10.3390/biomedicines12030682](https://doi.org/10.3390/biomedicines12030682
  needs_review: true
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hypertrophic_Cardiomyopathy_30_Atrial-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypertrophic Cardiomyopathy 30, Atrial
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 30, Atrial** covering all of the
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
- **Disease Name:** Hypertrophic Cardiomyopathy 30, Atrial
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 30, Atrial** covering all of the
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


# Hypertrophic Cardiomyopathy 30, Atrial: Disease-Characteristics Report

## Executive summary and evidence boundary

**Hypertrophic cardiomyopathy 30, atrial** is an exceptionally rare, recently delineated Mendelian cardiomyopathy associated with **CORIN**, the gene encoding the cardiac transmembrane serine protease corin. Its defining clinical spectrum is better described as **left-atrial cardiomyopathy with hypertension, atrial arrhythmia, and fibrosis** than as conventional sarcomeric, left-ventricular hypertrophic cardiomyopathy. Open Targets maps the entity to **MONDO:0958241**, CORIN/ENSG00000145244, PMID **37913506**, and ClinVar records **RCV003882741** and **RCV005234881**. (OpenTargets Search: Hypertrophic cardiomyopathy 30, atrial)

The evidence base is extremely small. The pivotal human report is Feldman et al., *New England Journal of Medicine*, published **2 November 2023**, PMID 37913506, DOI: [10.1056/NEJMoa2301908](https://doi.org/10.1056/NEJMoa2301908). Its full text and detailed pedigree tables were not retrievable through the available tools. Consequently, exact family size, nucleotide/protein variant, allele frequency, segregation, penetrance, and patient-level frequencies should be curated directly from that article and its ClinVar submissions rather than inferred. The strongest accessible mechanistic evidence comes from CORIN-null mice, pressure-overload models, fibroblast experiments, and human cardiomyopathy transcriptomic analyses. (OpenTargets Search: Hypertrophic cardiomyopathy 30, atrial, niu2023corindeficiencyimpairs pages 12-13, kan2024progressionfromcardiomyopathy pages 1-2)

The following table distinguishes disease-specific observations from broader CORIN biology and general-HCM extrapolation.

| Field | Disease-specific / extrapolated | Knowledge-base-ready summary | Suggested ontology terms | Evidence |
|---|---|---|---|---|
| Canonical name | Disease-specific | Hypertrophic cardiomyopathy 30, atrial; also represented as cardiomyopathy, familial hypertrophic, 30, atrial | MONDO:0958241 | (OpenTargets Search: Hypertrophic cardiomyopathy 30, atrial) |
| MONDO ID | Disease-specific | MONDO:0958241 | MONDO:0958241 | (OpenTargets Search: Hypertrophic cardiomyopathy 30, atrial) |
| Causal gene / protein | Disease-specific | CORIN encodes corin, a cardiac transmembrane serine protease involved in natriuretic peptide activation | Gene: CORIN; Protein: corin, serine peptidase | (OpenTargets Search: Hypertrophic cardiomyopathy 30, atrial, niu2023corindeficiencyimpairs pages 1-2) |
| Key disease-specific evidence | Disease-specific | Open Targets links MONDO:0958241 to CORIN with literature support including PMID 37913506 and ClinVar submissions; exact family-level variant and pedigree details were not accessible in the retrieved text and should be curated directly from the primary report/ClinVar before database finalization | Disease entity to gene association | (OpenTargets Search: Hypertrophic cardiomyopathy 30, atrial) |
| Inheritance / penetrance | Disease-specific | Familial/inherited disease label supports Mendelian inheritance, but exact mode of inheritance, penetrance, and expressivity could not be verified from accessible full-text evidence; record as unknown pending direct review of PMID 37913506/ClinVar | Inheritance: unknown; Penetrance: unknown; Expressivity: unknown | (OpenTargets Search: Hypertrophic cardiomyopathy 30, atrial) |
| Core phenotypes | Disease-specific | Left atrial cardiomyopathy/atrial remodeling with arrhythmia, hypertension, and fibrosis are implicated by the disease association and title-level evidence; exact frequencies and ventricular involvement remain incompletely accessible | HPO label suggestions: atrial arrhythmia, atrial fibrillation, cardiac fibrosis, hypertension, cardiomyopathy, abnormality of the left atrium | (OpenTargets Search: Hypertrophic cardiomyopathy 30, atrial) |
| Mechanism | Disease-specific with strong support from related CORIN biology | CORIN deficiency impairs conversion of pro-ANP to ANP, lowering downstream cGMP signaling and permitting maladaptive RAAS activation, sodium-retention/pressure-load effects, hypertrophy, fibrosis, and heart failure progression; direct atrial-human mechanism is plausible but incompletely resolved for this named disease | GO label suggestions: atrial natriuretic peptide processing, cGMP-mediated signaling, regulation of blood pressure, negative regulation of cardiac muscle hypertrophy, extracellular matrix organization, cardiac muscle fibrosis | (kan2024progressionfromcardiomyopathy pages 17-17, niu2023corindeficiencyimpairs pages 12-13, niu2023corindeficiencyimpairs pages 1-2) |
| Anatomy / cell types / subcellular localization | Mixed: disease-specific cardiac focus; mechanistic details from related CORIN studies | Primary anatomy: heart, especially left atrium; likely secondary involvement via hypertension/heart failure. Cell types: cardiomyocytes, cardiac fibroblasts. Subcellular/localization: plasma membrane/cell surface for corin; extracellular space for ANP signaling | UBERON label suggestions: heart, left atrium, myocardium; CL label suggestions: cardiomyocyte, cardiac fibroblast; GO-CC label suggestions: plasma membrane, cell surface, extracellular region | (kan2024progressionfromcardiomyopathy pages 1-2, niu2023corindeficiencyimpairs pages 1-2) |
| Diagnostic approach | Mostly extrapolated from general HCM/cardiomyopathy practice; gene-specific confirmation is disease-specific | For suspected cases: cardiac phenotyping with ECG/rhythm monitoring, echocardiography, consider CMR, blood pressure assessment, family history, and molecular testing including CORIN within cardiomyopathy/arrhythmia panels or exome/genome approaches if panel-negative; cascade testing depends on confirmation of a pathogenic familial variant | HPO label suggestions relevant to workup: atrial fibrillation, cardiomyopathy, hypertension | (OpenTargets Search: Hypertrophic cardiomyopathy 30, atrial) |
| Management evidence status | Mostly extrapolated from general HCM/atrial cardiomyopathy; no disease-specific treatment trials identified | No disease-specific therapy established from accessible evidence. Management should currently follow phenotype-directed care for HCM/atrial arrhythmia/hypertension/heart failure, while noting experimental rationale for restoring corin/ANP signaling from animal studies. Emerging general HCM therapies such as myosin inhibitors are not validated for CORIN-mediated atrial disease specifically | NCIT label suggestions: genetic counseling, electrocardiographic monitoring, echocardiography, cardiac MRI, antiarrhythmic therapy, anticoagulation, antihypertensive therapy | (niu2023corindeficiencyimpairs pages 12-13, niu2023corindeficiencyimpairs pages 1-2) |
| Epidemiology | Disease-specific | Ultra-rare; no prevalence or incidence estimates were recovered for this named entity from accessible evidence | Rare disease | (OpenTargets Search: Hypertrophic cardiomyopathy 30, atrial) |
| Animal / experimental models | Related CORIN biology, not exact human atrial disease replica | Corin knockout mice develop salt-sensitive hypertension and progressive cardiac dysfunction, hypertrophy, and fibrosis after aging; pressure-overload (TAC) accelerates dysfunction in young KO mice; recombinant soluble corin ameliorates dysfunction, fibrosis, hypertrophy markers, RAAS activation, and lung edema. Fibroblast studies show CORIN overexpression can blunt profibrotic activation | GO label suggestions: response to pressure overload, regulation of cardiac muscle hypertrophy, fibrosis, fibroblast activation; CL: cardiac fibroblast | (niu2023corindeficiencyimpairs pages 12-13, kan2024progressionfromcardiomyopathy pages 1-2, niu2023corindeficiencyimpairs pages 1-2) |
| Major evidence gaps | Disease-specific | Missing or inaccessible in retrieved evidence: exact pathogenic variant(s), ACMG classification, segregation data, patient counts, age/sex distribution, penetrance, quantitative phenotype frequencies, natural history, prognosis, and whether ventricular hypertrophy is obligatory or secondary. These should be abstracted directly from PMID 37913506, ClinVar records, and any follow-up correspondence before structured curation | Evidence gap annotation | (OpenTargets Search: Hypertrophic cardiomyopathy 30, atrial) |


*Table: This table condenses the currently recoverable knowledge-base-ready facts for Hypertrophic Cardiomyopathy 30, Atrial and clearly separates disease-specific evidence from inferences based on broader CORIN biology and general HCM practice.*

## 1. Disease information

### Definition

This is a familial cardiac disorder attributed to impaired CORIN function and characterized principally by structural and electrical disease of the atrium, including atrial remodeling/fibrosis, atrial arrhythmia, and associated hypertension. The nomenclature “hypertrophic cardiomyopathy 30, atrial” should **not** be assumed to mean that conventional unexplained left-ventricular hypertrophy is obligatory; the accessible disease-specific evidence instead emphasizes a left-atrial phenotype. (OpenTargets Search: Hypertrophic cardiomyopathy 30, atrial)

### Identifiers and synonyms

- **MONDO:** MONDO:0958241.
- **Preferred database label:** cardiomyopathy, familial hypertrophic, 30, atrial.
- **Synonyms:** hypertrophic cardiomyopathy 30, atrial; HCM30, atrial; CORIN-related atrial cardiomyopathy; familial left-atrial cardiomyopathy associated with CORIN.
- **Gene:** CORIN; Ensembl **ENSG00000145244**; approved protein name “corin, serine peptidase.”
- **ClinVar disease records surfaced:** RCV003882741 and RCV005234881.
- **OMIM, Orphanet, MeSH, ICD-10/ICD-11:** a distinct code could not be verified from retrieved evidence. Until confirmed, use broader cardiomyopathy/atrial-cardiomyopathy codes and preserve MONDO:0958241 as the specific computational identifier. (OpenTargets Search: Hypertrophic cardiomyopathy 30, atrial)

The source is an **aggregated disease-level entity built from a family report and variant databases**, not an EHR-derived population phenotype.

## 2. Etiology

### Causal factor

The nominated cause is a **germline CORIN defect**. Corin normally converts pro-atrial natriuretic peptide (pro-ANP) to active ANP. Reduced activity therefore weakens natriuretic-peptide signaling, favors sodium retention and hypertension, and removes anti-hypertrophic and anti-fibrotic restraint. (kan2024progressionfromcardiomyopathy pages 17-17, niu2023corindeficiencyimpairs pages 1-2)

### Risk factors and modifiers

- **Genetic:** a disease-associated CORIN variant is the primary risk factor. Exact HGVS nomenclature, ACMG/AMP classification, zygosity, population frequency, and segregation require direct ClinVar/PMID 37913506 review.
- **Family history:** relevant because the disorder is familial, but penetrance and age dependence are not yet quantifiable.
- **Environmental/physiologic:** high sodium intake, uncontrolled blood pressure, and chronic pressure load are biologically plausible aggravators, not proven human modifiers of this exact subtype. In mice, Corin loss produces salt-sensitive hypertension, while transverse aortic constriction markedly accelerates dysfunction. (niu2023corindeficiencyimpairs pages 12-13, niu2023corindeficiencyimpairs pages 1-2)
- **Age:** aging unmasks disease in CORIN-null mice; hypertrophy and fibrosis become evident after approximately nine months, with dysfunction prominent by 12 months. Human age-specific risk is unknown. (niu2023corindeficiencyimpairs pages 12-13, niu2023corindeficiencyimpairs pages 1-2)

No validated protective allele, modifier gene, sex-specific risk, occupational exposure, toxin, infection, diet, or pharmacogenomic association has been established for the named disorder. Blood-pressure control and avoidance of excessive sodium are reasonable phenotype-directed precautions, not demonstrated primary prevention.

## 3. Phenotypes

Disease-specific quantitative frequencies are unavailable. Suggested phenotypes are therefore separated into **reported/core**, **mechanistically supported**, and **possible complications**.

- **Left-atrial cardiomyopathy/remodeling:** core structural manifestation; likely chronic and progressive. Suggested HPO labels: *abnormality of the left atrium*, *left atrial enlargement*, and *cardiomyopathy*.
- **Atrial arrhythmia, particularly atrial fibrillation:** core electrical manifestation; potentially episodic initially and persistent later. HPO: *atrial arrhythmia*, *atrial fibrillation*.
- **Cardiac fibrosis:** core tissue manifestation and probable arrhythmogenic substrate. HPO: *myocardial fibrosis/cardiac fibrosis*.
- **Hypertension:** prominent associated systemic sign. HPO: *systemic arterial hypertension*.
- **Cardiac hypertrophy:** supported by the disease name and CORIN-deficiency models, but the relative atrial versus ventricular distribution in human carriers must not be inferred without the primary report. HPO: *cardiac hypertrophy* or *left ventricular hypertrophy* only if documented in the individual.
- **Heart failure, pulmonary edema, reduced ejection fraction:** plausible advanced consequences supported by models and broader cardiomyopathy data, but not established as universal disease-specific findings. (OpenTargets Search: Hypertrophic cardiomyopathy 30, atrial, niu2023corindeficiencyimpairs pages 12-13, kan2024progressionfromcardiomyopathy pages 1-2)

Potential quality-of-life effects include palpitations, exertional intolerance, anxiety concerning arrhythmia/stroke, medication burden, and limitations from heart failure. No disease-specific EQ-5D, SF-36, PROMIS, or functional-outcome study is available.

## 4. Genetic and molecular information

### Gene and protein

**CORIN** encodes a type-II transmembrane serine protease expressed predominantly on cardiomyocyte surfaces. It activates pro-ANP; related literature also implicates corin in pro-BNP processing, sodium homeostasis, vascular remodeling, and blood-pressure regulation. (kan2024progressionfromcardiomyopathy pages 17-17, niu2023corindeficiencyimpairs pages 13-13, niu2023corindeficiencyimpairs pages 1-2)

### Variant evidence

Open Targets links CORIN to the disease through PMID 37913506 and two ClinVar records. However, the accessible evidence does not safely establish the exact variant, transcript, HGVS expression, ACMG class, molecular consequence, or gnomAD/TOPMed frequency. Those fields should be marked **pending primary-source verification**, not populated from secondary inference. The disorder should be treated as germline/familial; no somatic etiology is implicated. (OpenTargets Search: Hypertrophic cardiomyopathy 30, atrial)

No validated modifier genes, epigenetic signature, recurrent structural variant, chromosomal rearrangement, anticipation, germline mosaicism, founder effect, or consanguinity association is known.

## 5. Environmental and lifestyle information

No environmental agent or infection causes this Mendelian disease. Physiologic stressors could nevertheless alter expression:

1. Increased sodium/volume burden may amplify hypertension when ANP activation is impaired.
2. Chronic hypertension raises atrial and ventricular wall stress.
3. Pressure overload promotes hypertrophy, fibroblast activation, and fibrosis.
4. Fibrosis creates an arrhythmogenic substrate and may impair filling and pump function.

This gene–environment chain is strongly supported in CORIN-null mice but remains unquantified in affected humans. Corin-null mice have impaired sodium handling and a systolic pressure around **118 mmHg versus 107 mmHg** in wild-type controls. (niu2023corindeficiencyimpairs pages 1-2)

Smoking, alcohol, obesity, sleep apnea, and extreme exercise should be assessed because they affect atrial fibrillation and cardiomyopathy generally, but they have not been demonstrated as CORIN-specific modifiers.

## 6. Mechanism and pathophysiology

### Proposed causal chain

**Upstream:** deleterious CORIN variation → reduced cell-surface corin abundance, activation, or protease function → deficient pro-ANP cleavage.

**Intermediate:** reduced mature ANP → reduced natriuretic-peptide receptor-A/cGMP/PKG signaling → diminished natriuresis and vasodilation plus inadequate suppression of renin–angiotensin–aldosterone signaling.

**Downstream:** sodium/volume retention and hypertension → atrial wall stress and pressure loading → cardiomyocyte hypertrophy and cardiac-fibroblast activation → extracellular-matrix deposition/fibrosis → atrial electrical remodeling and arrhythmia; prolonged disease may progress to ventricular dysfunction, heart failure, and pulmonary edema. (kan2024progressionfromcardiomyopathy pages 17-17, niu2023corindeficiencyimpairs pages 12-13, niu2023corindeficiencyimpairs pages 1-2)

A direct experimental quote from the 2023 mouse study summarizes the rescue evidence: **“Corin deficiency impairs cardiac function and exacerbates HF development in mice.”** Recombinant soluble corin increased plasma cGMP, reduced N-terminal pro-ANP, angiotensin II, and aldosterone, and ameliorated hypertrophy, fibrosis, dysfunction, and lung edema after pressure overload. (niu2023corindeficiencyimpairs pages 12-13, niu2023corindeficiencyimpairs pages 1-2)

### Molecular profiling

A 2024 analysis integrated bulk transcriptomic data from **106 HCM** and **184 dilated-cardiomyopathy** patients with single-nucleus RNA sequencing and Mendelian-randomization analyses. A low-CORIN/high-fibroblast-activation cluster was associated with lower ejection fraction and poorer prognosis. In neonatal-rat cardiac fibroblasts, CORIN overexpression reduced TGF-β1-induced **COL1A1** and **α-SMA** expression. These results support an anti-fibrotic role but are not specific to MONDO:0958241; clinical covariates and independent subtype validation were limited. (kan2024progressionfromcardiomyopathy pages 1-2)

Suggested annotations:

- **GO biological processes:** proteolytic activation of peptide hormone; natriuretic peptide signaling; cGMP-mediated signaling; regulation of systemic arterial blood pressure; sodium-ion homeostasis; negative regulation of cardiac-muscle hypertrophy; extracellular-matrix organization; cardiac fibrosis.
- **Cell Ontology:** cardiomyocyte; atrial cardiomyocyte; cardiac fibroblast; vascular endothelial cell.
- **GO cellular components:** plasma membrane; cell surface; extracellular region.
- **Chemical entities:** ANP, cGMP, sodium ion, angiotensin II, aldosterone; CHEBI identifiers should be validated during ontology ingestion.

No disease-specific methylome, proteome, metabolome, lipidome, spatial-transcriptomic, CRISPR-screen, or patient-derived single-cell atlas was identified.

## 7. Anatomical structures affected

- **Primary organ:** heart.
- **Principal site:** left atrium/atrial myocardium; suggested UBERON labels: *heart*, *left atrium*, *myocardium*.
- **Cells:** atrial cardiomyocytes and cardiac fibroblasts.
- **Subcellular site:** cardiomyocyte plasma membrane/cell surface, where corin processes extracellular pro-ANP.
- **Secondary systems:** systemic vasculature and kidney through blood-pressure, volume, and sodium regulation; lungs may be involved secondarily through heart-failure pulmonary edema.
- **Lateralization:** not applicable beyond specific left-atrial predominance; unilateral/bilateral terminology is inappropriate. (kan2024progressionfromcardiomyopathy pages 17-17, niu2023corindeficiencyimpairs pages 12-13, niu2023corindeficiencyimpairs pages 1-2)

## 8. Temporal development

Human onset, median diagnostic age, and progression rate are unknown. The familial phenotype is most reasonably regarded as **chronic, potentially age-dependent, and variably expressive** pending longitudinal study.

The model-organism trajectory is clearer: CORIN-null mice develop hypertension first, then hypertrophy and fibrosis after about nine months, and progressive dysfunction by roughly 12 months. Pressure overload at **10–12 weeks** precipitates more rapid deterioration than in wild-type mice. This suggests a latent compensated phase followed by stress- or age-associated decompensation, but mouse timing cannot be directly translated to patients. (niu2023corindeficiencyimpairs pages 12-13, niu2023corindeficiencyimpairs pages 1-2)

No spontaneous remission, treatment-induced molecular remission, or critical pediatric intervention window has been demonstrated.

## 9. Inheritance and population

The disease is familial and Mendelian, but the precise inheritance mode and penetrance could not be verified from accessible primary text. An autosomal-dominant model may be plausible for a multigenerational familial cardiomyopathy, but it should remain **unconfirmed** until the pedigree and ClinVar records are reviewed.

There are no reliable estimates of prevalence, incidence, carrier frequency, sex ratio, ethnic enrichment, geographic distribution, founder effect, or age distribution. It should be classified as **ultra-rare** rather than assigned a numerical prevalence. General HCM prevalence must not be substituted for CORIN-related atrial cardiomyopathy.

## 10. Diagnostics

### Clinical evaluation

A rational work-up is:

1. Three-generation pedigree, blood-pressure history, symptoms, and medication/exposure review.
2. Resting 12-lead ECG and ambulatory rhythm monitoring to detect atrial fibrillation or other atrial arrhythmias.
3. Transthoracic echocardiography, emphasizing atrial size/function, ventricular wall thickness, diastolic function, ejection fraction, and outflow obstruction.
4. Cardiac MRI for atrial/ventricular morphology and late-gadolinium-enhancement fibrosis where technically appropriate.
5. Biomarkers such as NT-proBNP/BNP, renal function, electrolytes, and troponin when clinically indicated. Pro-ANP processing or soluble corin is mechanistically attractive but **not a validated disease-specific diagnostic assay**.
6. Exclude secondary hypertrophy/remodeling: long-standing hypertension, valve disease, athlete’s heart, infiltrative/storage disorders, sarcomeric HCM, congenital structural disease, and tachycardia-mediated remodeling.

### Genetic testing

Use a validated cardiomyopathy/arrhythmia panel that includes **CORIN**, with deletion/duplication analysis as appropriate. If negative despite a compelling family phenotype, consider exome or genome sequencing and periodic reanalysis. A confirmed familial pathogenic/likely pathogenic variant enables cascade testing; relatives without definitive molecular clarification require longitudinal ECG and imaging surveillance.

General-HCM data indicate that targeted testing yields a causal variant in about **30% of sporadic cases** and up to **60% of familial or younger, typical cases**, but these figures cannot be applied to this CORIN entity. A 2024 review recommends disease-focused next-generation-sequencing panels and cascade testing when a decisively pathogenic familial variant is found. [Abbas et al., 20 March 2024, DOI 10.3390/biomedicines12030682](https://doi.org/10.3390/biomedicines12030682). No evidence supports routine karyotyping, FISH, mitochondrial sequencing, repeat-expansion testing, liquid biopsy, or diagnostic proteomics for this disorder.

## 11. Outcome and prognosis

No disease-specific survival curve, mortality rate, life-expectancy estimate, stroke rate, heart-failure rate, or quality-of-life dataset exists in accessible evidence. Plausible complications include persistent atrial fibrillation, thromboembolism/stroke, progressive fibrosis, hypertension-mediated organ damage, heart failure, and—if ventricular disease is present—ventricular arrhythmia or sudden cardiac death. These require individual risk assessment rather than assumed attribution.

In broader cardiomyopathy datasets, reduced CORIN expression is associated with lower ejection fraction and worse prognosis, while CORIN-null mice develop progressive dysfunction and fibrosis. These observations establish biological concern but not patient-level prognostic calibration for HCM30. (kan2024progressionfromcardiomyopathy pages 17-17, kan2024progressionfromcardiomyopathy pages 1-2)

Potential prognostic measurements include atrial size and strain, atrial-fibrillation burden, fibrosis on MRI, blood-pressure control, ventricular thickness/function, NT-proBNP, and clinical heart-failure status. None is yet validated specifically for CORIN-related disease.

## 12. Treatment

There is **no approved CORIN-genotype-specific therapy** and no disease-specific clinical trial identified. Current care should be phenotype-directed at a cardiomyopathy center.

- **Hypertension/volume control:** individualized antihypertensive therapy and avoidance of excessive sodium; avoid abrupt preload reduction if significant obstructive ventricular physiology exists.
- **Atrial fibrillation:** rhythm/rate control as appropriate and thromboembolic-risk management. In established HCM with clinical AF, contemporary guidelines generally favor anticoagulation irrespective of conventional CHA₂DS₂-VASc thresholds, but whether every isolated CORIN atrial phenotype meets that HCM rule requires specialist judgment.
- **Heart failure:** guideline-directed therapy matched to ejection fraction and hemodynamics.
- **Obstructive ventricular HCM, if independently documented:** non-vasodilating beta-blocker first; verapamil/diltiazem when appropriate; disopyramide, septal reduction, or a cardiac-myosin inhibitor in eligible patients. These interventions target ventricular sarcomeric hypercontractility and are **not validated for isolated CORIN-mediated atrial disease**.
- **Devices/ablation:** catheter ablation, pacemaker, or ICD only for standard rhythm and sudden-death indications, not genotype alone.
- **Support:** genetic counseling, family screening, exercise counseling, pregnancy planning, and management of obesity/sleep apnea and other AF-promoting conditions.

The authoritative current frameworks are the **2023 ESC cardiomyopathy guideline** and **2024 AHA/ACC/AMSSM/HRS/PACES/SCMR HCM guideline** (published June 2024; DOI [10.1161/CIR.0000000000001250](https://doi.org/10.1161/CIR.0000000000001250)). A systematic comparison found broad agreement on echocardiography, genetic testing/family screening, medical and invasive management, exercise, and reproductive counseling, with differences in diagnostic definitions, MRI use, and sudden-death risk assessment.

Recombinant soluble corin is an experimental concept only. In pressure-overloaded knockout mice it increased cGMP and reduced RAAS activation, hypertrophy, fibrosis, and edema; no human efficacy, dose, safety, immunogenicity, or delivery data support clinical use. (niu2023corindeficiencyimpairs pages 12-13, niu2023corindeficiencyimpairs pages 1-2)

Suggested NCIT intervention labels: genetic counseling; electrocardiography; ambulatory ECG monitoring; echocardiography; cardiac MRI; antihypertensive therapy; anticoagulation therapy; antiarrhythmic therapy; catheter ablation; implantable cardioverter-defibrillator; septal myectomy. Validate exact NCIT codes during ingestion.

## 13. Prevention

- **Primary prevention:** the inherited variant cannot currently be prevented. Reproductive options after molecular confirmation include prenatal diagnosis and preimplantation genetic testing with nondirective counseling.
- **Secondary prevention:** cascade genetic testing, ECG/rhythm surveillance, echocardiography, MRI when indicated, and early detection/control of hypertension and atrial arrhythmia.
- **Tertiary prevention:** blood-pressure control, stroke prevention in AF, heart-failure therapy, and individualized arrhythmic-risk management.
- **Behavioral measures:** avoid smoking and stimulant misuse; maintain healthy weight; diagnose sleep apnea; use individualized exercise advice; avoid excessive sodium and alcohol where hypertension/AF is present.
- **Vaccination/public-health control:** no disease-specific vaccine or infectious prophylaxis applies.

No intervention has been shown to prevent phenoconversion in genotype-positive CORIN carriers.

## 14. Other species and natural disease

No verified naturally occurring CORIN-associated counterpart in companion animals, livestock, or wildlife was identified. There is no zoonotic transmission. CORIN is evolutionarily conserved, and experimental mouse phenotypes demonstrate conservation of natriuretic-peptide activation and blood-pressure regulation, but engineered knockout disease should not be entered as naturally occurring veterinary HCM30.

Suggested taxonomy for the principal experimental species: *Mus musculus* (NCBI Taxon **10090**). Exact mouse Corin and ortholog gene identifiers should be imported from NCBI Gene/Alliance rather than inferred here.

## 15. Model organisms and experimental systems

### Mouse models

- **Constitutive Corin knockout:** salt-sensitive hypertension, progressive cardiac hypertrophy and fibrosis after nine months, and later dysfunction. Strength: models systemic loss of corin. Limitation: the human variant may be hypomorphic or domain-specific, and the mouse phenotype is not selectively atrial. (niu2023corindeficiencyimpairs pages 12-13, niu2023corindeficiencyimpairs pages 1-2)
- **Corin knockout plus transverse aortic constriction:** at 10–12 weeks, knockout mice deteriorate faster than similarly stressed wild types, modeling gene–pressure-load interaction. Recombinant soluble corin partially rescues function, morphology, cGMP signaling, RAAS activation, and pulmonary edema. Strength: causal perturbation and rescue. Limitation: surgically imposed ventricular afterload differs from spontaneous human atrial disease. (niu2023corindeficiencyimpairs pages 12-13, niu2023corindeficiencyimpairs pages 1-2)
- **Conditional cardiac/renal Corin models:** useful for separating endocrine cardiac CORIN from renal or intestinal sodium-handling effects; these are mechanistic models rather than faithful replicas of HCM30.

### Cellular and computational systems

Neonatal-rat cardiac fibroblasts exposed to TGF-β1 show reduced COL1A1 and α-SMA activation after CORIN overexpression. Human HCM/DCM bulk and single-nucleus transcriptomic analyses identify low-CORIN, fibroblast-rich disease clusters. These systems support anti-fibrotic activity but cannot establish variant-specific atrial causality. (kan2024progressionfromcardiomyopathy pages 1-2)

High-priority future models are patient-derived iPSC atrial cardiomyocytes and fibroblasts, isogenic CRISPR correction/knock-in lines, atrial engineered tissues, and variant-specific knock-in mice. Required readouts include pro-ANP cleavage, cell-surface CORIN abundance, cGMP/PKG activity, electrophysiology, conduction, extracellular-matrix production, and response to pressure/sodium stress.

## Key evidence gaps and curation priorities

1. Retrieve PMID **37913506** and ClinVar RCV003882741/RCV005234881 to capture exact HGVS variant, transcript, zygosity, ACMG class, family size, segregation, and functional assays.
2. Determine whether inheritance is definitively autosomal dominant and quantify age-dependent penetrance.
3. Separate atrial hypertrophy/remodeling from ventricular HCM in the formal disease definition.
4. Obtain individual-level phenotype frequencies, onset, rhythm burden, fibrosis measurements, blood-pressure data, treatment responses, and outcomes.
5. Establish whether soluble corin, pro-ANP:mature-ANP ratio, or cGMP is diagnostically or prognostically useful.
6. Develop variant-specific human atrial models and a prospective international registry.

Overall, the association of **CORIN with MONDO:0958241 is supported**, and the CORIN–ANP–cGMP/RAAS axis provides a coherent causal mechanism. Nevertheless, most clinical implementation currently rests on phenotype-directed cardiomyopathy and atrial-arrhythmia practice, while exact molecular and natural-history annotations remain dependent on direct curation of the foundational 2023 family report. (OpenTargets Search: Hypertrophic cardiomyopathy 30, atrial, niu2023corindeficiencyimpairs pages 12-13, kan2024progressionfromcardiomyopathy pages 1-2, niu2023corindeficiencyimpairs pages 1-2)

References

1. (OpenTargets Search: Hypertrophic cardiomyopathy 30, atrial): Open Targets Query (Hypertrophic cardiomyopathy 30, atrial, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (niu2023corindeficiencyimpairs pages 12-13): Yayan Niu, Tiantian Zhou, Shengnan Zhang, Wenguo Li, Kun Wang, Ningzheng Dong, and Qingyu Wu. Corin deficiency impairs cardiac function in mouse models of heart failure. Frontiers in Cardiovascular Medicine, Aug 2023. URL: https://doi.org/10.3389/fcvm.2023.1164524, doi:10.3389/fcvm.2023.1164524. This article has 11 citations and is from a peer-reviewed journal.

3. (kan2024progressionfromcardiomyopathy pages 1-2): Jun-yan Kan, Dong-chen Wang, Zi-hao Jiang, Li-da Wu, Ke Xu, and Yue Gu. Progression from cardiomyopathy to heart failure with reduced ejection fraction: a corin deficient course. Heliyon, 10:e37838, Sep 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e37838, doi:10.1016/j.heliyon.2024.e37838. This article has 2 citations.

4. (niu2023corindeficiencyimpairs pages 1-2): Yayan Niu, Tiantian Zhou, Shengnan Zhang, Wenguo Li, Kun Wang, Ningzheng Dong, and Qingyu Wu. Corin deficiency impairs cardiac function in mouse models of heart failure. Frontiers in Cardiovascular Medicine, Aug 2023. URL: https://doi.org/10.3389/fcvm.2023.1164524, doi:10.3389/fcvm.2023.1164524. This article has 11 citations and is from a peer-reviewed journal.

5. (kan2024progressionfromcardiomyopathy pages 17-17): Jun-yan Kan, Dong-chen Wang, Zi-hao Jiang, Li-da Wu, Ke Xu, and Yue Gu. Progression from cardiomyopathy to heart failure with reduced ejection fraction: a corin deficient course. Heliyon, 10:e37838, Sep 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e37838, doi:10.1016/j.heliyon.2024.e37838. This article has 2 citations.

6. (niu2023corindeficiencyimpairs pages 13-13): Yayan Niu, Tiantian Zhou, Shengnan Zhang, Wenguo Li, Kun Wang, Ningzheng Dong, and Qingyu Wu. Corin deficiency impairs cardiac function in mouse models of heart failure. Frontiers in Cardiovascular Medicine, Aug 2023. URL: https://doi.org/10.3389/fcvm.2023.1164524, doi:10.3389/fcvm.2023.1164524. This article has 11 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Hypertrophic_Cardiomyopathy_30_Atrial-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 4 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.3390/biomedicines12030682](https://doi.org/10.3390/biomedicines12030682` (1 mention) - Identifier did not resolve to a record