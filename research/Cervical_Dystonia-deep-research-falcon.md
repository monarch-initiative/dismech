---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-16T20:07:06.263064'
end_time: '2026-08-16T20:15:59.849147'
duration_seconds: 533.59
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cervical Dystonia
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 29
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Cervical_Dystonia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cervical Dystonia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cervical Dystonia** covering all of the
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
- **Disease Name:** Cervical Dystonia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cervical Dystonia** covering all of the
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


# Cervical Dystonia: Disease-Characteristics Research Report

## Scope and evidence note

This report prioritizes 2023–2024 literature retrieved for this review. Cervical-dystonia (CD)-specific human evidence is distinguished from evidence about dystonia generally. Some requested database fields—particularly exact MONDO/Orphanet/HPO accessions, population allele frequencies, and active ClinicalTrials.gov records—could not be independently queried in the available retrieval environment; such fields are marked for ontology-database verification rather than inferred.

| Domain | Key finding/statistic | Evidence type | Ontology suggestions | Source / date / DOI |
|---|---|---|---|---|
| Definition / disease scope | **Cervical dystonia (CD)** is an adult-onset focal dystonia affecting the neck, characterized by sustained or intermittent muscle contractions causing abnormal head/neck postures and movements; sensory trick (geste antagoniste) is a supportive sign. **General dystonia finding:** dystonia is defined as abnormal repetitive movements/postures caused by sustained or intermittent muscle contractions; touching the chin can reduce symptoms in CD (thomsen2024geneticsandpathogenesis pages 1-2). | Expert review; clinical classification | MONDO: cervical dystonia if available; MeSH: Dystonic Disorders; HPO: HP:0001332 Dystonia, HP:0031987 Abnormal head posture, HP:0000496 Abnormality of movement; UBERON: neck region | Thomsen et al., *Annu Rev Pathol* 2024;19:99-131. Published online 2023-09-22. DOI: 10.1146/annurev-pathmechdis-051122-110756 (thomsen2024geneticsandpathogenesis pages 1-2) |
| Key identifiers / classification | **General dystonia finding:** consensus classification uses axis I (age at onset, body distribution, temporal pattern, associated features) and axis II (etiology). Focal dystonia = one body region affected; late adulthood onset >40 years (thomsen2024geneticsandpathogenesis pages 2-4). | Expert consensus review | HPO: HP:0003577 Adult onset, HP:0001332 Dystonia; NCIT: focal dystonia | Thomsen et al., *Annu Rev Pathol* 2024. DOI: 10.1146/annurev-pathmechdis-051122-110756 (thomsen2024geneticsandpathogenesis pages 2-4) |
| Epidemiology | **General isolated dystonia finding:** prevalence estimated at **52.7/100,000** or **30.9/100,000**; true prevalence may be higher because many cases remain un-/misdiagnosed; higher prevalence in females for most subforms (thomsen2024geneticsandpathogenesis pages 2-4, thomsen2024geneticsandpathogenesis pages 1-2). | Epidemiology summarized in review | NCIT: Prevalence; HPO: not applicable | Thomsen et al., *Annu Rev Pathol* 2024. DOI: 10.1146/annurev-pathmechdis-051122-110756 (thomsen2024geneticsandpathogenesis pages 2-4, thomsen2024geneticsandpathogenesis pages 1-2) |
| Epidemiology / sex distribution | In a **1,701-patient** Italian idiopathic adult-onset dystonia registry, **cervical dystonia was present in 848/1701** at last exam; female:male ratio for CD **1.9 (95% CI 1.8-2.1)**. At onset, CD accounted for **681/1574 focal onsets**, female:male ratio **1.9 (1.7-2.0)** (velucci2024doessexinfluence pages 1-2, velucci2024doessexinfluence pages 2-3). | Large human registry | HPO: HP:0001332 Dystonia; NCIT: Female, Male | Velucci et al., *J Neurol Neurosurg Psychiatry* 2024;95:784-790. March 2024. DOI: 10.1136/jnnp-2023-332927 (velucci2024doessexinfluence pages 1-2, velucci2024doessexinfluence pages 2-3) |
| Phenotype / onset | CD usually begins between **45-50 years**; symptoms include dystonic neck posture plus, in some patients, dystonic tremor and pain; risk of spread to other body parts is described as **very low** in one focal-dystonia review/cohort summary (salamon2023geneticscreeningof pages 1-2). | Review with focal-dystonia cohort context | HPO: HP:0002418 Torticollis, HP:0001336 Tremor, HP:0012531 Neck pain, HP:0002829 Arthralgia/pain if needed | Salamon et al., *Int J Mol Sci* 2023;24:10745. 2023-06-28. DOI: 10.3390/ijms241310745 (salamon2023geneticscreeningof pages 1-2) |
| Phenotype / associated features | In the 1,701-patient registry, **sensory trick** occurred in **483/1701 (28.4%)**, tremor in **516/1701 (30.3%)**; among CD cases, **neck pain** occurred in **488/848 (57.5%)** with similar frequency by sex (58.1% women vs 56.6% men) (velucci2024doessexinfluence pages 2-3). | Large human registry | HPO: HP:0003394 Sensory trick (suggested), HP:0001336 Tremor, HP:0012531 Neck pain | Velucci et al., *J Neurol Neurosurg Psychiatry* 2024. DOI: 10.1136/jnnp-2023-332927 (velucci2024doessexinfluence pages 2-3) |
| Non-motor / quality of life | **General dystonia with CD-relevant data:** pain prevalence in CD ranges **67%-75%** in older systematic review data; a study of **116** patients with spasmodic torticollis found **71% lifetime social phobia**, correlated with body image/maladaptive attitude rather than objective severity (kuyper2011nonmotormanifestationsof pages 4-5). | Systematic review of non-motor manifestations | HPO: HP:0012531 Neck pain, HP:0000739 Anxiety, HP:0000729 Depression, HP:0000705 Social phobia (suggested) | Kuyper et al., *Movement Disorders* 2011;26:1206-1217. June 2011. DOI: 10.1002/mds.23709 (kuyper2011nonmotormanifestationsof pages 4-5) |
| Etiology | Most adult-onset isolated/CD cases are **idiopathic/sporadic and likely multifactorial**; monogenic causes are uncommon in isolated focal dystonia, and gene-environment interaction is suspected in sporadic cases (bruggemann2021contemporaryfunctionalneuroanatomy pages 1-2, salamon2023geneticscreeningof pages 5-6). | Review; focal-dystonia sequencing study | MONDO: idiopathic isolated dystonia; HPO: HP:0001332 Dystonia | Brüggemann, *J Neural Transm* 2021;128:499-508. DOI: 10.1007/s00702-021-02299-y; Salamon et al., *Int J Mol Sci* 2023. DOI: 10.3390/ijms241310745 (bruggemann2021contemporaryfunctionalneuroanatomy pages 1-2, salamon2023geneticscreeningof pages 5-6) |
| Genetic factors | In focal dystonia, genes most often implicated in CD screening studies include **THAP1, CIZ1, GNAL, ANO3**; in a Hungarian cohort of **121** focal dystonia patients (**74 CD**), 30-gene NGS found **209 heterozygous variants in 24 genes**, with **9 clinically/genetically relevant variants** total and overall diagnostic yield **7.4%** (salamon2023geneticscreeningof pages 1-2, salamon2023geneticscreeningof pages 5-6). | Human sequencing cohort | HGNC genes: THAP1, CIZ1, GNAL, ANO3, KMT2B, VPS16, KCNN2; NCIT: Next-Generation Sequencing | Salamon et al., *Int J Mol Sci* 2023;24:10745. 2023-06-28. DOI: 10.3390/ijms241310745 (salamon2023geneticscreeningof pages 1-2, salamon2023geneticscreeningof pages 5-6) |
| Pathogenic / candidate variants | CD-relevant variants in the Hungarian cohort included **ANO3 c.2276-6T>C** (splice region), **CIZ1 c.1820A>G p.Glu607Gly**, **KCNN2 c.1625G>A p.Arg542Gln**, **KMT2B c.3136C>T p.Arg1046Cys**, and **VPS16 c.1370T>C p.Leu457Pro**; most relevant variants occurred in earlier-onset cases (mean onset **31.6 years**) (salamon2023geneticscreeningof pages 5-6). | Human sequencing cohort | HGVS variant notation; HPO: HP:0003577 Adult onset, HP:0003621 Juvenile onset if early; NCIT: Variant of Uncertain Significance, Likely Pathogenic Variant | Salamon et al., *Int J Mol Sci* 2023. DOI: 10.3390/ijms241310745 (salamon2023geneticscreeningof pages 5-6) |
| Diagnostic genetics strategy | For focal dystonia/CD, detailed genetic work-up is most justified when there is **early onset, family history, or additional neurological/non-neurological features**; the 2023 cohort recommended targeted gene panels when budget is limited, with WES not clearly superior for yield in their sample (salamon2023geneticscreeningof pages 5-6). | Human cohort interpretation / expert recommendation | NCIT: Gene Panel Testing, Whole Exome Sequencing | Salamon et al., *Int J Mol Sci* 2023. DOI: 10.3390/ijms241310745 (salamon2023geneticscreeningof pages 5-6) |
| Mechanisms / systems neuroscience | **General dystonia finding with relevance to CD:** dystonia is a **network disorder** involving **basal ganglia, cerebellum, thalamus, and cortex** rather than only basal ganglia; impaired sensorimotor integration, reduced inhibition, and maladaptive plasticity are core mechanisms (thomsen2024geneticsandpathogenesis pages 1-2, bruggemann2021contemporaryfunctionalneuroanatomy pages 1-2, rauschenberger2024unravelingdystoniacircuitry pages 1-2). | Expert review; mechanistic review | GO: synaptic signaling, regulation of neurotransmitter levels, motor control; UBERON: basal ganglion, cerebellum, thalamus, cerebral cortex; CL: Purkinje cell, striatal medium spiny neuron, cholinergic interneuron | Thomsen et al., *Annu Rev Pathol* 2024. DOI: 10.1146/annurev-pathmechdis-051122-110756; Brüggemann, *J Neural Transm* 2021. DOI: 10.1007/s00702-021-02299-y; Rauschenberger & Ip, *Dystonia* 2024. DOI: 10.3389/dyst.2024.11793 (thomsen2024geneticsandpathogenesis pages 1-2, bruggemann2021contemporaryfunctionalneuroanatomy pages 1-2, rauschenberger2024unravelingdystoniacircuitry pages 1-2) |
| Mechanisms / molecular pathways | **General dystonia finding:** implicated pathways include **gene transcription during neurodevelopment** (e.g., **KMT2B, THAP1**), **calcium homeostasis** (**ANO3, HPCA**), **striatal dopamine signaling** (**GNAL**), **ER stress response** (**EIF2AK2, PRKRA, TOR1A**), and **autophagy/lysosomal trafficking** (**VPS16**) (thomsen2024geneticsandpathogenesis pages 1-2). | Expert molecular review | GO: regulation of transcription, calcium ion homeostasis, dopamine receptor signaling pathway, response to endoplasmic reticulum stress, autophagy; CL: striatal neuron | Thomsen et al., *Annu Rev Pathol* 2024. DOI: 10.1146/annurev-pathmechdis-051122-110756 (thomsen2024geneticsandpathogenesis pages 1-2) |
| Mechanisms / synaptic physiology | **General dystonia finding:** rodent models support abnormal neurotransmitter signaling, receptor trafficking, and synaptic plasticity in basal ganglia and cerebellum as common hallmarks. In DYT-TOR1A models, altered dopamine-acetylcholine balance disrupts corticostriatal LTD/depotentiation; D2 receptor activation paradoxically excites cholinergic interneurons (atiallah2023synapticdysfunctionin pages 1-2, atiallah2023synapticdysfunctionin pages 4-5). | Rodent/mechanistic review | GO: synaptic plasticity, long-term synaptic depression, dopaminergic signaling, cholinergic signaling; CL: cholinergic interneuron, Purkinje cell, deep cerebellar nucleus neuron | El Atiallah et al., *Curr Neuropharmacol* 2023;21:2310-2322. DOI: 10.2174/1570159X21666230718100156 (atiallah2023synapticdysfunctionin pages 1-2, atiallah2023synapticdysfunctionin pages 4-5) |
| Anatomy affected | Primary clinically affected structure is the **cervical musculature/neck region**; biologically implicated CNS nodes include **cortex, basal ganglia, thalamus, cerebellum**, and brainstem. CD may occur at rest, unlike some task-specific dystonias (bruggemann2021contemporaryfunctionalneuroanatomy pages 1-2). | Review | UBERON: neck, skeletal muscle of neck, cerebellum, thalamus, basal ganglion, cerebral cortex; CL: Purkinje cell, medium spiny neuron | Brüggemann, *J Neural Transm* 2021. DOI: 10.1007/s00702-021-02299-y (bruggemann2021contemporaryfunctionalneuroanatomy pages 1-2) |
| Diagnosis / clinical work-up | CD is primarily a **clinical diagnosis** by expert examination; work-up for idiopathic adult-onset dystonia in the Italian registry included **brain MRI or CT** to exclude structural causes and testing for **Wilson disease** and common monogenic dystonia variants (**TOR1A, THAP1, ANO3, GNAL**) as appropriate (velucci2024doessexinfluence pages 1-2). | Large registry / clinical practice description | NCIT: Magnetic Resonance Imaging, Computed Tomography, Genetic Testing; HPO: HP:0001332 Dystonia | Velucci et al., *J Neurol Neurosurg Psychiatry* 2024. DOI: 10.1136/jnnp-2023-332927 (velucci2024doessexinfluence pages 1-2) |
| Differential diagnosis | Important exclusions include **structural/acquired dystonia**, **Wilson disease**, and **monogenic non-degenerative dystonias**; expert reviews also note combined and complex dystonias, and autoimmune causes should be considered in subacute focal/segmental craniocervical presentations. | Registry protocol; expert review | MONDO: Wilson disease; NCIT: Differential Diagnosis | Velucci et al., *J Neurol Neurosurg Psychiatry* 2024. DOI: 10.1136/jnnp-2023-332927; Thomsen et al., *Annu Rev Pathol* 2024. DOI: 10.1146/annurev-pathmechdis-051122-110756 (velucci2024doessexinfluence pages 1-2, thomsen2024geneticsandpathogenesis pages 1-2) |
| Treatment / first-line | **Botulinum neurotoxin (BoNT) is standard symptomatic treatment** for CD; in the focal-dystonia cohort summary, BoNT therapy (types A and B) was described as essential for proper treatment, with muscle selection aided by **ultrasound and/or EMG** and the collum-caput concept (salamon2023geneticscreeningof pages 1-2). | Clinical review / implementation description | NCIT: Botulinum Toxin Type A, Botulinum Toxin Type B, Electromyography, Ultrasonography | Salamon et al., *Int J Mol Sci* 2023. DOI: 10.3390/ijms241310745 (salamon2023geneticscreeningof pages 1-2) |
| Treatment / BoNT landscape | **General therapeutic context with CD-specific pipeline data:** BoNTs are routinely used for CD. A 2024 toxin review lists formulations/trials including **PrabotulinumtoxinA (ABP-450, phase 2, migraine/cervical dystonia)**, **NeubotulinumtoxinA (phase 3, cervical dystonia)**, and **A2NTX (phase 1, cervical dystonia)** (rasettiescargueil2024embracingtheversatility pages 9-10). | Therapeutics review / clinical pipeline summary | NCIT: Botulinum Toxin, Clinical Trial | Rasetti-Escargueil & Palea, *Toxins* 2024;16:261. June 2024. DOI: 10.3390/toxins16060261 (rasettiescargueil2024embracingtheversatility pages 9-10) |
| Treatment / surgery | For refractory craniocervical dystonia including CD, **GPi deep brain stimulation** shows sustained benefit but variable durability. In a 2024 retrospective series of **24** patients, mean BFMDRS motor improved **55.3% at 6 months** and **56.6% at last follow-up**; **25%** had poor results (<30% improvement) (zhao2024longtermfollowupof pages 1-2, zhao2024longtermfollowupof pages 5-6). | Human surgical cohort | NCIT: Deep Brain Stimulation, Globus Pallidus Internus | Zhao et al., *Neurosurg Focus* 2024;56(6):E16. June 2024. DOI: 10.3171/2024.3.FOCUS23890 (zhao2024longtermfollowupof pages 1-2, zhao2024longtermfollowupof pages 5-6) |
| Prognosis / natural history | CD is usually **chronic**. In idiopathic adult-onset forms, spread and phenotype vary by body region; in craniocervical dystonia, symptoms often begin with blepharospasm or CD and may spread over time. Long-term DBS benefit can fluctuate, with nonresponse or secondary worsening in a subset (zhao2024longtermfollowupof pages 1-2, zhao2024longtermfollowupof pages 5-6, salamon2023geneticscreeningof pages 1-2). | Human cohort; review | HPO: HP:0003676 Progressive course; NCIT: Disease Progression | Zhao et al., *Neurosurg Focus* 2024. DOI: 10.3171/2024.3.FOCUS23890; Salamon et al., *Int J Mol Sci* 2023. DOI: 10.3390/ijms241310745 (zhao2024longtermfollowupof pages 1-2, zhao2024longtermfollowupof pages 5-6, salamon2023geneticscreeningof pages 1-2) |
| Prevention | No established **primary prevention** exists for idiopathic CD. Practical prevention is mainly **tertiary**: early recognition, optimized BoNT injection strategy, rehabilitation, and consideration of DBS in refractory disease to reduce disability and pain. | Inference from current care evidence | NCIT: Rehabilitation, Supportive Care, Deep Brain Stimulation | Supported by treatment reviews/cohorts (salamon2023geneticscreeningof pages 1-2, zhao2024longtermfollowupof pages 1-2, rasettiescargueil2024embracingtheversatility pages 9-10) |
| Models / animal and cellular | **General dystonia model evidence:** rodent and primate models implicate both basal ganglia and cerebellum. Lesion, pharmacologic, optogenetic, chemogenetic, and genetic models show that cerebellar stimulation/inactivation can induce or suppress dystonia-like movements; abnormal Purkinje-cell and deep cerebellar nucleus firing are recurrent findings (rauschenberger2024unravelingdystoniacircuitry pages 1-2, wilson2013animalmodelsfor pages 4-5, atiallah2023synapticdysfunctionin pages 4-5). | Rodent/primate experimental evidence | CL: Purkinje cell, deep cerebellar nucleus neuron, striatal projection neuron; GO: action potential, synaptic signaling | Rauschenberger & Ip, *Dystonia* 2024. DOI: 10.3389/dyst.2024.11793; Wilson & Hess, *Mov Disord* 2013. DOI: 10.1002/mds.25526; El Atiallah et al., *Curr Neuropharmacol* 2023. DOI: 10.2174/1570159X21666230718100156 (rauschenberger2024unravelingdystoniacircuitry pages 1-2, wilson2013animalmodelsfor pages 4-5, atiallah2023synapticdysfunctionin pages 4-5) |


*Table: This table condenses key cervical dystonia knowledge-base facts across clinical, genetic, mechanistic, diagnostic, therapeutic, prognostic, and model domains. It distinguishes cervical-dystonia-specific evidence from broader dystonia findings and attaches ontology suggestions plus source metadata for downstream curation.*

## 1. Disease information

**Definition.** Cervical dystonia is a focal dystonia in which sustained or intermittent involuntary contractions of cervical muscles produce patterned, often twisting or repetitive head/neck movements and abnormal postures. It was historically called **spasmodic torticollis**. Presentations include torticollis, laterocollis/laterocaput, antecollis/antecaput, retrocollis/retrocaput, sagittal or lateral shift, and combinations thereof. Dystonic head tremor, muscle hypertrophy, pain, overflow activation, and a relieving maneuver (“geste antagoniste” or sensory trick, such as touching the chin) support the diagnosis. The current expert framework classifies dystonia on two axes: clinical characteristics—age at onset, distribution, temporal pattern, and associated features—and etiology. “Focal” means one body region; isolated dystonia permits tremor but no other movement disorder. (thomsen2024geneticsandpathogenesis pages 2-4, thomsen2024geneticsandpathogenesis pages 1-2)

**Suggested identifiers.** ICD-10-CM **G24.3** (“spasmodic torticollis”); ICD-11 is within the dystonia/movement-disorder hierarchy; MeSH concepts include *Dystonic Disorders* and *Torticollis*. Common synonyms are cervical dystonia, spasmodic torticollis, adult-onset idiopathic cervical dystonia, idiopathic rotational torticollis, and focal neck dystonia. The exact current MONDO and Orphanet accessions should be resolved against the live ontology release before database ingestion; cervical dystonia should not be conflated with generalized “isolated dystonia” or congenital muscular torticollis.

The evidence summarized here is primarily **aggregated disease-level evidence** from registries, cohorts, reviews, and experimental models—not individual EHR-derived patient data. One important recent source analyzed 1,701 patients from 42 Italian movement-disorder centers using a common specialist protocol. (velucci2024doessexinfluence pages 1-2)

> Exact abstract wording from a 2024 authoritative review: “Dystonia is a clinically and genetically highly heterogeneous neurological disorder characterized by abnormal movements and postures caused by involuntary sustained or intermittent muscle contractions.” DOI: https://doi.org/10.1146/annurev-pathmechdis-051122-110756; first online September 22, 2023; issue date January 2024. (thomsen2024geneticsandpathogenesis pages 1-2)

## 2. Etiology, risk, protective factors, and gene–environment interaction

Most typical adult-onset isolated CD is **idiopathic and multifactorial**, not a single-gene disorder. Current models invoke a susceptible motor network in which polygenic/developmental factors interact with age-, sex-, and possibly exposure-dependent triggers. Acquired cervical dystonia can follow structural brain injury, neuroleptic or dopamine-blocking drugs, neurodegenerative disease, infection/autoimmunity, or peripheral trauma, but causality for many reported environmental associations remains uncertain. A subacute, rapidly progressive, relapsing, or neurologically complex presentation should prompt investigation for acquired/autoimmune disease rather than classification as idiopathic CD. (bruggemann2021contemporaryfunctionalneuroanatomy pages 1-2, thomsen2024geneticsandpathogenesis pages 2-4)

**Risk factors supported most consistently:** middle or later adult age, female sex, and family history of dystonia or tremor. In the Italian registry, CD had a female:male ratio of **1.9 (95% CI 1.8–2.1)** at last examination and **1.9 (1.7–2.0)** at onset. Family history of dystonia or tremor occurred in 11.1% across idiopathic adult-onset dystonia, although this was not CD-specific. The authors proposed that age-related sexual dimorphism could reflect interactions between environmental exposures and hormonal/biological factors; this is a hypothesis rather than a proven causal mechanism. (velucci2024doessexinfluence pages 1-2, velucci2024doessexinfluence pages 2-3)

No replicated **protective genetic variant**, diet, exercise pattern, medication, or exposure has been shown to prevent idiopathic CD. Alcohol may transiently reduce some dystonic symptoms but is not protective and carries dependence risk. Smoking, diet, exercise, and occupational exposures do not currently support actionable prevention recommendations. No infectious agent is established as the cause of ordinary idiopathic CD.

## 3. Phenotypes and quality-of-life effects

The principal phenotype is persistent or action-aggravated abnormal head posture with patterned cervical muscle activation. Severity ranges from mild intermittent pulling to fixed, painful postures causing substantial disability. CD usually begins at **45–50 years** and generally remains focal, although craniocervical or other segmental spread can occur. (salamon2023geneticscreeningof pages 1-2)

Suggested phenotype annotations include:

- Torticollis/abnormal head posture—clinical sign; **HPO HP:0002418 (Torticollis)** and abnormal head-posture terms.
- Dystonia—motor sign; **HP:0001332**.
- Dystonic head tremor—sign; **HP:0001336 (Tremor)**, with a dystonic-tremor qualifier.
- Neck pain—symptom; **HP:0012531 (Pain)** plus neck localization. In the 2024 registry, neck pain affected **488/848 CD cases (57.5%)**; older systematic-review estimates were 67–75%, illustrating cohort and ascertainment differences. (velucci2024doessexinfluence pages 2-3, kuyper2011nonmotormanifestationsof pages 4-5)
- Sensory trick/geste antagoniste—supportive sign; 28.4% across the complete adult-onset dystonia registry, not solely CD. (velucci2024doessexinfluence pages 2-3)
- Restricted cervical range of motion, muscle spasm/hypertrophy, dysphagia or dysphonia where relevant—use the corresponding HPO terms after phenotype-level confirmation.
- Anxiety, depression, embarrassment, social avoidance, sleep disturbance, and fatigue—nonmotor manifestations requiring separate assessment. An older study summarized in a systematic review found **71% lifetime social phobia among 116 people with spasmodic torticollis**, associated more with body image and maladaptive illness attitudes than objective motor severity. (kuyper2011nonmotormanifestationsof pages 4-5)

Pain, visible postural abnormality, tremor, and unpredictable symptom fluctuation interfere with driving, reading, work, sleep, social interaction, and activities of daily living. Motor severity alone therefore incompletely represents quality of life; CD-specific instruments such as the Cervical Dystonia Impact Profile and Toronto Western Spasmodic Torticollis Rating Scale should be complemented by pain, mood, sleep, and participation measures.

## 4. Genetic and molecular information

CD is genetically heterogeneous. Confirmed monogenic dystonias that can include prominent cervical or craniocervical involvement include **THAP1, GNAL, ANO3, TOR1A**, and in selected complex or early-onset cases **KMT2B, VPS16, SGCE, ADCY5, ATP1A3, GCH1, EIF2AK2, PRKRA**, among others. The 2024 review listed 52 well-supported monogenic dystonia genes in the 2022 MDS nomenclature update, while more than 400 genes had been associated with dystonia or dystonic symptoms at varying evidence levels. This broader number must not be interpreted as 400 established CD genes. (thomsen2024geneticsandpathogenesis pages 2-4, thomsen2024geneticsandpathogenesis pages 1-2)

In a 2023 Hungarian study of 121 unrelated focal-dystonia patients—74 CD and 47 blepharospasm—a 30-gene panel identified 209 heterozygous variants in 24 genes. Nine variants were judged clinically/genetically relevant, yielding **7.4%**, although six were VUS and no functional testing was performed. Relevant variants occurred almost exclusively in CD and disproportionately in earlier-onset cases (mean onset 31.6 years). (salamon2023geneticscreeningof pages 1-2, salamon2023geneticscreeningof pages 5-6)

Reported CD-associated candidates included **ANO3 c.2276-6T>C**, **CIZ1 c.1820A>G (p.Glu607Gly)**, **KCNN2 c.1625G>A (p.Arg542Gln)**, **KMT2B c.3136C>T (p.Arg1046Cys)**, and **VPS16 c.1370T>C (p.Leu457Pro)**. These were chiefly VUS and should **not** be entered as established pathogenic variants without updated ClinVar/ClinGen review, segregation, population-frequency evaluation, and functional evidence. (salamon2023geneticscreeningof pages 5-6)

The best-characterized inherited forms are generally germline, with autosomal-dominant inheritance and incomplete penetrance common among isolated dystonias. Variable expressivity is substantial. Somatic mosaicism, anticipation, and recurrent chromosomal abnormalities are not recognized defining features of ordinary CD. No robust CD-specific modifier gene or clinically validated epigenetic signature is established. Population allele frequencies must be obtained variant-by-variant from the current gnomAD release; rare-disease pathogenic variants are generally expected to be absent or extremely rare, but no frequency should be assigned from disease reports alone.

## 5. Environmental and lifestyle information

The evidence for environmental causation in idiopathic CD is weaker than the evidence for age, sex, and genetic susceptibility. Clinicians should document dopamine-receptor-blocking drug exposure, neck/peripheral trauma, structural CNS injury, occupational repetitive activity, toxins, and infections, but distinguish temporal association from causality. Acute or subacute focal dystonia is atypical for ordinary idiopathic CD and raises concern for drug-induced, structural, metabolic, or autoimmune disease. There is no validated diet, exercise regimen, smoking pattern, alcohol exposure, pollution exposure, radiation source, or pathogen that specifically causes or prevents typical CD.

## 6. Mechanism and pathophysiology

The prevailing view is a **distributed network disorder**, not a primary cervical-muscle disease and not solely a basal-ganglia disorder. The implicated network comprises cerebral sensorimotor cortex, striatum and pallidum, thalamus, cerebellum, and brainstem. Core physiological abnormalities are impaired sensorimotor integration, deficient inhibition at cortical, basal-ganglia, brainstem, and spinal levels, maladaptive plasticity, and faulty motor “gating.” The causal chain proposed for idiopathic CD is: inherited/developmental susceptibility plus incompletely defined environmental or physiological triggers → altered synaptic signaling and plasticity in basal-ganglia–cerebellar–thalamo–cortical circuits → reduced surround inhibition and poor suppression of competing motor programs → simultaneous agonist/antagonist and overflow muscle activation → patterned head posture, tremor, and pain. (bruggemann2021contemporaryfunctionalneuroanatomy pages 1-2, thomsen2024geneticsandpathogenesis pages 1-2)

Molecular groupings include neurodevelopmental transcription (**KMT2B, THAP1**), calcium homeostasis (**ANO3, HPCA**), striatal dopamine/cAMP signaling (**GNAL**), endoplasmic-reticulum stress (**TOR1A, EIF2AK2, PRKRA**), and autophagy/lysosomal trafficking (**VPS16**). These pathways derive mainly from genetic dystonia rather than common idiopathic CD, but may expose convergent therapeutic mechanisms. (thomsen2024geneticsandpathogenesis pages 1-2)

Rodent work supports abnormal dopamine–acetylcholine balance, glutamatergic transmission, receptor trafficking, and corticostriatal plasticity. In DYT-TOR1A models, D2-receptor activation can paradoxically excite striatal cholinergic interneurons, increasing acetylcholine and impairing corticostriatal long-term depression/depotentiation. Cerebellar Purkinje-cell and deep-nuclear firing abnormalities also correlate with dystonic movements. (wilson2013animalmodelsfor pages 4-5, atiallah2023synapticdysfunctionin pages 4-5, atiallah2023synapticdysfunctionin pages 1-2)

Suggested annotations are **GO: synaptic signaling; regulation of synaptic plasticity; long-term synaptic depression; dopamine-receptor signaling; cholinergic synaptic transmission; calcium-ion homeostasis; response to ER stress; autophagy**. Suggested cell types are striatal medium spiny/projection neuron, striatal cholinergic interneuron, cerebellar Purkinje cell, deep cerebellar nuclear neuron, thalamic neuron, and cortical pyramidal neuron. There is no validated CD-specific immune, metabolomic, lipidomic, methylomic, proteomic, single-cell, spatial-transcriptomic, or multi-omic diagnostic signature. Available advanced-omics evidence is mostly from monogenic models and remains investigational.

## 7. Anatomical structures affected

At the effector level, CD affects skeletal muscles of the neck and upper shoulder girdle, commonly including sternocleidomastoid, splenius capitis/cervicis, semispinalis, levator scapulae, trapezius, scalene, and deep suboccipital muscles. Activation is usually asymmetric but can be bilateral. Secondary effects include cervical pain, restricted mobility, degenerative musculoskeletal strain, and occasionally dysphagia.

At the nervous-system level, implicated sites are motor/premotor and somatosensory cortex, striatum, globus pallidus, thalamus, cerebellar cortex/deep nuclei, and brainstem. Suggested UBERON annotations are **neck region, skeletal muscle of neck, cerebral cortex, basal ganglion, globus pallidus, thalamus, cerebellum, brainstem**. Relevant subcellular compartments in genetic forms include ER/nuclear envelope (torsinA), synapse/presynaptic vesicle machinery, plasma-membrane signaling complexes, and lysosome/autophagosome. (atiallah2023synapticdysfunctionin pages 4-5, bruggemann2021contemporaryfunctionalneuroanatomy pages 1-2)

## 8. Temporal development

Typical onset is insidious in middle adulthood, often initially intermittent and aggravated by action, stress, fatigue, or particular head positions. Symptoms commonly evolve over months to several years before becoming relatively stable, although day-to-day fluctuation persists. CD is generally chronic and lifelong. Spread is less common than in blepharospasm but may produce craniocervical or other segmental dystonia. Spontaneous remissions are reported clinically but are uncommon and may relapse; no evidence supports a predictable critical window for disease prevention. Early specialist diagnosis is nevertheless valuable because prolonged diagnostic delay extends pain, disability, and ineffective care. (salamon2023geneticscreeningof pages 1-2, zhao2024longtermfollowupof pages 1-2)

## 9. Inheritance and population epidemiology

Dystonia was historically classified as rare, but recent estimates cited in the 2024 review placed **isolated dystonia overall** at **30.9–52.7 per 100,000**; true prevalence may be higher because of underdiagnosis and misdiagnosis. These are not CD-specific prevalence estimates. (thomsen2024geneticsandpathogenesis pages 2-4)

In the Italian registry, 848/1,701 patients had cervical involvement at final examination; 558 were women and 290 men. Neck pain prevalence did not differ materially by sex. The study also supports female predominance in craniocervical dystonia, while task-specific upper-limb dystonia showed male predominance. (velucci2024doessexinfluence pages 2-3)

Geographic estimates vary with ascertainment and ancestry. A 2024 craniocervical-dystonia report cited a roughly threefold higher CD incidence among White than Asian populations, but this secondary statement requires confirmation in the original multiethnic epidemiologic study before population-risk annotation. (zhao2024longtermfollowupof pages 1-2)

Most CD is sporadic/multifactorial. Monogenic cases can be autosomal dominant with reduced penetrance and variable expressivity; recessive and other inheritance patterns occur in broader dystonia syndromes. Founder effects, carrier frequency, anticipation, germline mosaicism, and consanguinity are gene- and variant-specific rather than general CD properties.

## 10. Diagnosis

Diagnosis is clinical and should be made by a clinician experienced in movement disorders. Examination establishes the posture/movement pattern, active muscles, tremor, pain, sensory tricks, task dependence, range of motion, and spread. Standardized scales include TWSTRS, Tsui score, Cervical Dystonia Impact Profile, and pain/quality-of-life measures. Surface or needle EMG and ultrasound help identify injection targets but are not standalone diagnostic biomarkers.

MRI or CT is appropriate when onset or examination suggests a structural cause. In the Italian registry, all patients underwent brain MRI or CT, with Wilson-disease testing and testing of **TOR1A, THAP1, ANO3, and GNAL** when appropriate. (velucci2024doessexinfluence pages 1-2)

There is no diagnostic blood, CSF, tissue, electrophysiologic, imaging, proteomic, metabolomic, or liquid-biopsy biomarker for idiopathic CD. Genetic testing is highest yield with onset before approximately 20–30 years, positive family history, generalized/segmental spread, developmental or additional neurologic features, or an atypical course. A dystonia panel is a reasonable first test; WES/WGS is appropriate when panel testing is unrevealing and suspicion remains high. CMA, karyotype, FISH, mitochondrial testing, and repeat-expansion testing are not routine for typical adult-onset isolated CD but may be indicated by syndromic features. The 2023 focal-dystonia cohort found no clear WES-yield advantage over a curated panel in its small WES subset. (salamon2023geneticscreeningof pages 5-6)

Differential diagnoses include essential or dystonic tremor, Parkinsonian anterocollis, tics, functional dystonia, congenital/orthopedic torticollis, cervical radiculopathy, atlantoaxial disease, drug-induced/tardive dystonia, Wilson disease, structural lesions, neurodegenerative or metabolic dystonia, autoimmune encephalitis, and craniocervical dystonia/Meige syndrome. Population or newborn screening is not recommended. Cascade testing is appropriate only after a clearly pathogenic familial variant is established.

## 11. Outcome and prognosis

CD generally does not shorten life expectancy, and disease-specific survival statistics are not clinically applicable. Its burden is morbidity: pain, impaired head control, tremor, sleep disturbance, reduced employment and driving, anxiety/depression, social isolation, and treatment burden. Fixed postures, orthopedic strain, dysphagia, and treatment-related neck weakness are possible complications.

Prognosis is heterogeneous. Many patients obtain meaningful symptomatic control with individualized botulinum-neurotoxin treatment, but treatment must be repeated. Motor response does not guarantee resolution of pain, mood, sleep, or social disability. No validated molecular prognostic biomarker predicts spread, remission, toxin response, or DBS response.

## 12. Treatment and recent developments

### Botulinum neurotoxin

Intramuscular botulinum neurotoxin is the standard first-line treatment. BoNT/A products include onabotulinumtoxinA, abobotulinumtoxinA, incobotulinumtoxinA, and the longer-acting daxibotulinumtoxinA-lanm; rimabotulinumtoxinB is a BoNT/B option. Products are not dose-unit interchangeable. The toxin cleaves SNARE proteins in cholinergic terminals, reducing acetylcholine release and excessive muscle contraction. Muscle selection should follow the observed posture and collum–caput pattern, with ultrasound and/or EMG guidance for deep or difficult targets. (salamon2023geneticscreeningof pages 1-2)

Common adverse effects are dysphagia, neck weakness, local pain, dry mouth, flu-like symptoms, and excessive weakness. Apparent nonresponse should prompt reassessment of diagnosis, muscle selection, dose, guidance, injection interval, fixed contracture, and rarely neutralizing antibodies.

A 2024 review documented continued formulation development, including **prabotulinumtoxinA/ABP-450 (phase 2)**, **neubotulinumtoxinA (phase 3)**, and **A2NTX (phase 1)** for CD at the time reviewed. These pipeline statuses require confirmation against the current trial registry. DOI: https://doi.org/10.3390/toxins16060261; published June 2024. (rasettiescargueil2024embracingtheversatility pages 9-10)

Suggested NCIt concepts: Botulinum Toxin Type A, Botulinum Toxin Type B, intramuscular injection, electromyography-guided injection, ultrasonography-guided injection.

### Oral, supportive, and rehabilitative treatment

Oral drugs are generally adjunctive and have weaker evidence than BoNT: trihexyphenidyl, clonazepam or other benzodiazepines, baclofen, and selected dopamine-modulating agents. Treatment should address pain, depression/anxiety, sleep, and occupational limitations. Physical therapy emphasizing sensorimotor retraining, posture, active exercise, and home programs may complement BoNT; forceful passive manipulation should be avoided. Occupational, psychological, and pain-management support are often appropriate.

### Deep-brain stimulation and surgery

Bilateral globus pallidus internus DBS is an option for severe medically refractory CD/segmental craniocervical dystonia. In a 2024 retrospective series of 24 refractory craniocervical-dystonia patients, mean BFMDRS motor score improved **55.3% at six months** and **56.6% at a mean 37.5-month follow-up**; six patients (25%) had less than 30% improvement, demonstrating important response variability. DOI: https://doi.org/10.3171/2024.3.FOCUS23890; published June 2024. (zhao2024longtermfollowupof pages 5-6, zhao2024longtermfollowupof pages 1-2)

Selective peripheral denervation is now less common but may be considered at specialized centers. Gene, cell, RNA, and immune therapies are not established for idiopathic CD. Genotype-directed treatment applies mainly to a minority of broader dystonia syndromes—for example levodopa-responsive GCH1 disease—not to routine adult-onset CD.

## 13. Prevention

There is no proven primary prevention, vaccine, prophylactic drug, population screening program, or validated behavioral intervention for idiopathic CD. Avoiding unnecessary dopamine-receptor-blocking drugs may reduce tardive dystonia risk but does not prevent idiopathic CD. Secondary prevention consists of prompt recognition of patterned dystonia and investigation of atypical or treatable acquired causes. Tertiary prevention includes optimized BoNT treatment, rehabilitation, pain and psychiatric care, swallowing monitoring, avoidance of fixed contractures, and DBS evaluation where appropriate. Genetic counseling is indicated for pathogenic variants or strong familial disease; prenatal or preimplantation testing is relevant only after a well-established familial pathogenic variant and individualized counseling.

## 14. Other species and naturally occurring disease

No well-established naturally occurring veterinary disorder is a direct homolog of common adult-onset idiopathic human CD. Animals may display torticollis from vestibular, infectious, toxic, traumatic, or structural disease, but this is not equivalent to human cervical dystonia. There is no zoonotic transmission. Orthologous dystonia genes are highly conserved across mammals, enabling mechanistic models, but veterinary breed-specific and VBO annotations should not be assigned without OMIA/VetCompass confirmation.

## 15. Model organisms

Models include genetic knock-in/knockout/conditional mice for **Tor1a, Thap1, Gnal, Sgce**, pharmacologic and lesion models in mice/rats, and toxin or pallidal-manipulation models in nonhuman primates. Dystonic rats carrying **Caytaxin** defects and *tottering* mice with **Cacna1a/Cav2.1** dysfunction exhibit abnormal Purkinje/deep-cerebellar-nuclear firing correlated with dystonic movements. Cerebellar lesion or inactivation can suppress dystonia in several models, while targeted glutamatergic stimulation can provoke it. (wilson2013animalmodelsfor pages 4-5)

Modern optogenetic and chemogenetic studies permit cell- and circuit-specific perturbation of basal-ganglia and cerebellar pathways. A 2024 review concluded that both systems are pathologically altered but emphasized that exact causal cell populations remain unresolved. DOI: https://doi.org/10.3389/dyst.2024.11793; published February 19, 2024. (rauschenberger2024unravelingdystoniacircuitry pages 1-2)

These models have construct validity for particular monogenic dystonias and are useful for synaptic physiology, developmental timing, circuit mapping, DBS mechanisms, and target discovery. Their principal limitation is that many do not reproduce spontaneous adult-onset focal neck dystonia; some show only subtle physiology or generalized dystonia-like movements. Findings therefore support convergent dystonia mechanisms but cannot automatically be treated as CD-specific human biology.

## Overall expert interpretation

Cervical dystonia is best represented in a knowledge base as a **complex, predominantly sporadic adult-onset focal network disorder** with occasional monogenic causes. Its defining data layer should prioritize clinical phenomenology, neck pain, tremor, sensory tricks, disability, and treatment response. Genetic entries should carry evidence-level qualifiers: **THAP1, GNAL, and ANO3** are credible causes of inherited dystonia with cervical involvement, whereas many recently observed focal-dystonia variants remain VUS. The most mature real-world intervention is individualized, repeatedly administered botulinum neurotoxin; GPi-DBS is effective for selected refractory disease but has meaningful nonresponse and durability uncertainty. The largest gaps are validated biomarkers, CD-specific multi-omics, firmly replicated gene–environment interactions, preventive strategies, and models that faithfully reproduce adult-onset focal cervical disease. (thomsen2024geneticsandpathogenesis pages 1-2, salamon2023geneticscreeningof pages 5-6, zhao2024longtermfollowupof pages 1-2)

References

1. (thomsen2024geneticsandpathogenesis pages 1-2): Mirja Thomsen, Lara M. Lange, Michael Zech, and Katja Lohmann. Genetics and pathogenesis of dystonia. Annual Review of Pathology: Mechanisms of Disease, 19:99-131, Jan 2024. URL: https://doi.org/10.1146/annurev-pathmechdis-051122-110756, doi:10.1146/annurev-pathmechdis-051122-110756. This article has 117 citations and is from a domain leading peer-reviewed journal.

2. (thomsen2024geneticsandpathogenesis pages 2-4): Mirja Thomsen, Lara M. Lange, Michael Zech, and Katja Lohmann. Genetics and pathogenesis of dystonia. Annual Review of Pathology: Mechanisms of Disease, 19:99-131, Jan 2024. URL: https://doi.org/10.1146/annurev-pathmechdis-051122-110756, doi:10.1146/annurev-pathmechdis-051122-110756. This article has 117 citations and is from a domain leading peer-reviewed journal.

3. (velucci2024doessexinfluence pages 1-2): Vittorio Velucci, Sarah Idrissi, R. Pellicciari, Marcello Esposito, Assunta Trinchillo, D. Belvisi, Giovanni Fabbrini, G. Ferrazzano, C. Terranova, P. Girlanda, Giovanni Majorana, V. Rizzo, Francesco Bono, Giovanni Idone, Vincenzo Laterza, L. Avanzino, F. di Biasio, R. Marchese, A. Castagna, M. Ramella, C. Lettieri, S. Rinaldo, M. C. Altavista, Luigi Polidori, L. Bertolasi, M. C. Tozzi, R. Erro, P. Barone, Pierangelo Barbero, R. Ceravolo, M. Mascia, Tommaso Ercoli, A. Muroni, C. Artusi, M. Zibetti, C. Scaglione, A. Bentivoglio, Maria Sofia Cotelli, L. Magistrelli, G. Cossu, A. Albanese, G. Squintani, T. Schirinzi, A. Gigante, L. Maderna, R. Eleopra, Antonio Pisani, D. Cassano, M. Romano, Marina Rizzo, A. Berardelli, and G. Defazio. Does sex influence the natural history of idiopathic adult-onset dystonia? Journal of Neurology, Neurosurgery, and Psychiatry, 95:784-790, Mar 2024. URL: https://doi.org/10.1136/jnnp-2023-332927, doi:10.1136/jnnp-2023-332927. This article has 12 citations.

4. (velucci2024doessexinfluence pages 2-3): Vittorio Velucci, Sarah Idrissi, R. Pellicciari, Marcello Esposito, Assunta Trinchillo, D. Belvisi, Giovanni Fabbrini, G. Ferrazzano, C. Terranova, P. Girlanda, Giovanni Majorana, V. Rizzo, Francesco Bono, Giovanni Idone, Vincenzo Laterza, L. Avanzino, F. di Biasio, R. Marchese, A. Castagna, M. Ramella, C. Lettieri, S. Rinaldo, M. C. Altavista, Luigi Polidori, L. Bertolasi, M. C. Tozzi, R. Erro, P. Barone, Pierangelo Barbero, R. Ceravolo, M. Mascia, Tommaso Ercoli, A. Muroni, C. Artusi, M. Zibetti, C. Scaglione, A. Bentivoglio, Maria Sofia Cotelli, L. Magistrelli, G. Cossu, A. Albanese, G. Squintani, T. Schirinzi, A. Gigante, L. Maderna, R. Eleopra, Antonio Pisani, D. Cassano, M. Romano, Marina Rizzo, A. Berardelli, and G. Defazio. Does sex influence the natural history of idiopathic adult-onset dystonia? Journal of Neurology, Neurosurgery, and Psychiatry, 95:784-790, Mar 2024. URL: https://doi.org/10.1136/jnnp-2023-332927, doi:10.1136/jnnp-2023-332927. This article has 12 citations.

5. (salamon2023geneticscreeningof pages 1-2): András Salamon, Zsófia Flóra Nagy, Margit Pál, Máté Szabó, Ádám Csősz, László Szpisjak, Gabriella Gárdián, Dénes Zádori, Márta Széll, and Péter Klivényi. Genetic screening of a hungarian cohort with focal dystonia identified several novel putative pathogenic gene variants. International Journal of Molecular Sciences, 24:10745, Jun 2023. URL: https://doi.org/10.3390/ijms241310745, doi:10.3390/ijms241310745. This article has 8 citations.

6. (kuyper2011nonmotormanifestationsof pages 4-5): Daniel J. Kuyper, Veronica Parra, Shanae Aerts, Michael S. Okun, and Benzi M. Kluger. Nonmotor manifestations of dystonia: a systematic review. Movement Disorders, 26:1206-1217, Jun 2011. URL: https://doi.org/10.1002/mds.23709, doi:10.1002/mds.23709. This article has 264 citations and is from a highest quality peer-reviewed journal.

7. (bruggemann2021contemporaryfunctionalneuroanatomy pages 1-2): Norbert Brüggemann. Contemporary functional neuroanatomy and pathophysiology of dystonia. Journal of Neural Transmission, 128:499-508, Jan 2021. URL: https://doi.org/10.1007/s00702-021-02299-y, doi:10.1007/s00702-021-02299-y. This article has 77 citations and is from a peer-reviewed journal.

8. (salamon2023geneticscreeningof pages 5-6): András Salamon, Zsófia Flóra Nagy, Margit Pál, Máté Szabó, Ádám Csősz, László Szpisjak, Gabriella Gárdián, Dénes Zádori, Márta Széll, and Péter Klivényi. Genetic screening of a hungarian cohort with focal dystonia identified several novel putative pathogenic gene variants. International Journal of Molecular Sciences, 24:10745, Jun 2023. URL: https://doi.org/10.3390/ijms241310745, doi:10.3390/ijms241310745. This article has 8 citations.

9. (rauschenberger2024unravelingdystoniacircuitry pages 1-2): Lisa Rauschenberger and Chi Wang Ip. Unraveling dystonia circuitry in rodent models using novel neuromodulation techniques. Dystonia, Feb 2024. URL: https://doi.org/10.3389/dyst.2024.11793, doi:10.3389/dyst.2024.11793. This article has 2 citations.

10. (atiallah2023synapticdysfunctionin pages 1-2): Ilham El Atiallah, Paola Bonsi, Annalisa Tassone, Giuseppina Martella, Gerardo Biella, Antonio N. Castagno, Antonio Pisani, and Giulia Ponterio. Synaptic dysfunction in dystonia: update from experimental models. Current Neuropharmacology, 21:2310-2322, Nov 2023. URL: https://doi.org/10.2174/1570159x21666230718100156, doi:10.2174/1570159x21666230718100156. This article has 11 citations and is from a peer-reviewed journal.

11. (atiallah2023synapticdysfunctionin pages 4-5): Ilham El Atiallah, Paola Bonsi, Annalisa Tassone, Giuseppina Martella, Gerardo Biella, Antonio N. Castagno, Antonio Pisani, and Giulia Ponterio. Synaptic dysfunction in dystonia: update from experimental models. Current Neuropharmacology, 21:2310-2322, Nov 2023. URL: https://doi.org/10.2174/1570159x21666230718100156, doi:10.2174/1570159x21666230718100156. This article has 11 citations and is from a peer-reviewed journal.

12. (rasettiescargueil2024embracingtheversatility pages 9-10): Christine Rasetti-Escargueil and Stefano Palea. Embracing the versatility of botulinum neurotoxins in conventional and new therapeutic applications. Toxins, 16:261, Jun 2024. URL: https://doi.org/10.3390/toxins16060261, doi:10.3390/toxins16060261. This article has 37 citations.

13. (zhao2024longtermfollowupof pages 1-2): Zhuoling Zhao, Zhiwei Ren, Yongsheng Hu, Kaijia Yu, Fangzhao Yin, Jianyu Li, and Guojun Zhang. Long-term follow-up of pallidal deep brain stimulation for craniocervical dystonia: is the globus pallidus internus the best target? Neurosurgical focus, 56 6:E16, Jun 2024. URL: https://doi.org/10.3171/2024.3.focus23890, doi:10.3171/2024.3.focus23890. This article has 2 citations.

14. (zhao2024longtermfollowupof pages 5-6): Zhuoling Zhao, Zhiwei Ren, Yongsheng Hu, Kaijia Yu, Fangzhao Yin, Jianyu Li, and Guojun Zhang. Long-term follow-up of pallidal deep brain stimulation for craniocervical dystonia: is the globus pallidus internus the best target? Neurosurgical focus, 56 6:E16, Jun 2024. URL: https://doi.org/10.3171/2024.3.focus23890, doi:10.3171/2024.3.focus23890. This article has 2 citations.

15. (wilson2013animalmodelsfor pages 4-5): Bethany K. Wilson and Ellen J. Hess. Animal models for dystonia. Movement Disorders, 28:982-989, Jun 2013. URL: https://doi.org/10.1002/mds.25526, doi:10.1002/mds.25526. This article has 84 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Cervical_Dystonia-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.