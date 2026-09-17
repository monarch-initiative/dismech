---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-26T16:28:21.671634'
end_time: '2026-08-26T16:40:51.536904'
duration_seconds: 749.87
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: RYR1-Related Myopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 2
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: RYR1-Related_Myopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RYR1-Related Myopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **RYR1-Related Myopathy** covering all of the
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
- **Disease Name:** RYR1-Related Myopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **RYR1-Related Myopathy** covering all of the
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


# RYR1-Related Myopathy: Comprehensive Disease-Characteristics Report

## Executive summary

RYR1-related myopathy (RYR1-RM) is an umbrella term for inherited skeletal-muscle disorders caused by pathogenic germline variants in **RYR1**, which encodes the principal sarcoplasmic-reticulum Ca²⁺-release channel of skeletal muscle. The spectrum includes central core disease (CCD), multiminicore disease (MmD), core–rod myopathy, RYR1-related centronuclear myopathy, congenital fiber-type disproportion, congenital neuromuscular disease with uniform type-1 fibers, King–Denborough syndrome, exertional myalgia/rhabdomyolysis, atypical periodic paralysis, and late-onset axial myopathy. Dominant and recessive inheritance occur; recessive disease is generally earlier and more severe. No approved disease-modifying treatment exists, but genotype-aware supportive care, malignant-hyperthermia precautions, and early clinical development of the RyR1-stabilizing agent ARM210/S48168 are current real-world implementations. The best-supported causal chain is **RYR1 variant → abnormal channel opening, impaired opening, or reduced protein abundance → defective excitation–contraction coupling and Ca²⁺ homeostasis → weakness/fatigue, with secondary mitochondrial and oxidative/nitrosative injury**. (lawal2018ryanodinereceptor1related pages 1-2, beaufils2022therapiesforryr1related pages 1-2, beaufils2022therapiesforryr1related pages 7-8)

| Domain | Key facts | Identifiers / ontology suggestions | Quantitative / implementation notes | Evidence / caveats |
|---|---|---|---|---|
| Disease definition / spectrum | RYR1-related myopathy (RYR1-RM) is a genetically heterogeneous group of skeletal muscle disorders caused by pathogenic **RYR1** variants; it is described as the most common class of congenital myopathies. Reported histopathologic/clinical subtypes include **central core disease**, **multiminicore disease**, **core-rod myopathy**, **centronuclear myopathy**, **congenital fiber-type disproportion**, **King-Denborough syndrome**, **rhabdomyolysis-myalgia syndrome**, **atypical periodic paralysis**, **late-onset axial myopathy**, and malignant-hyperthermia-associated myopathic presentations. | **MONDO:** requires database verification. **OMIM / Orphanet / MeSH / ICD-10/11:** disease-group mapping requires database verification because “RYR1-related myopathy” spans multiple named entities. Suggested disease ontology links: congenital myopathy group, central core disease, malignant hyperthermia susceptibility. | Disease concept is **aggregated disease-level knowledge**, not EHR-derived. NGS expanded recognized spectrum beyond biopsy-led classification. | Spectrum and nomenclature are well supported in reviews, but exact identifier mapping should be verified in OMIM/Orphanet/MONDO because the umbrella term spans several entities (lawal2018ryanodinereceptor1related pages 1-2). |
| Gene / protein | **RYR1** encodes **ryanodine receptor 1 (RyR1)**, the principal skeletal-muscle sarcoplasmic-reticulum Ca²⁺ release channel in excitation-contraction coupling; protein is a large homotetramer. Gene localizes to **19q13.2** and contains **106 exons**; protein length **5038 aa**, about **565 kDa**. | **Gene:** RYR1. **HGNC / NCBI Gene / UniProt IDs:** require database verification. Suggested GO terms: **calcium ion transmembrane transport**, **excitation-contraction coupling**, **sarcoplasmic reticulum calcium ion release channel activity**. Suggested GO cellular component: **sarcoplasmic reticulum membrane**, **terminal cisterna**, **calcium release unit**. | Functionally central to skeletal-muscle calcium release; associated proteins include FKBP12, calmodulin, DHPR/CACNA1S complex, triadin. | Core molecular facts are supported by review evidence; exact ontology IDs should be confirmed in HGNC/UniProt/GO databases (beaufils2022therapiesforryr1related pages 1-2). |
| Inheritance / genetics | Both **autosomal dominant** and **autosomal recessive** inheritance occur. Dominant disease is commonly linked to central core disease and malignant hyperthermia susceptibility; recessive disease is often associated with more severe congenital phenotypes such as multiminicore disease, centronuclear myopathy, and congenital fiber-type disproportion. | Suggested HPO / inheritance terms: **Autosomal dominant inheritance**, **Autosomal recessive inheritance**. Variant classes reported across the spectrum include missense and other pathogenic alleles; many cases are **germline**. | Reviews note approximately **400 RYR1 variants** identified by 2022. | Variant counts are review-level and likely underestimated relative to current ClinVar/literature; penetrance/expressivity are variable and should be verified per subtype/variant (beaufils2022therapiesforryr1related pages 7-8, lawal2018ryanodinereceptor1related pages 1-2). |
| Hallmark phenotypes | Core manifestations: **muscle weakness**, **fatigue/fatigability**, exercise intolerance; additional features reported across the spectrum include hypotonia, facial weakness, ophthalmoparesis/ophthalmoplegia, contractures, scoliosis, respiratory involvement, myalgia, muscle cramps, rhabdomyolysis, and malignant hyperthermia susceptibility. | Suggested HPO terms: **Muscular hypotonia**, **Proximal muscle weakness**, **Exercise intolerance**, **Easy fatigability**, **Myalgia**, **Rhabdomyolysis**, **Scoliosis**, **Joint contracture**, **Respiratory insufficiency**, **Ophthalmoplegia**. | In a 6MWT cohort, disease was stable over **6 months** but fatigability was measurable during testing; speed declined between the first and last minute at 6 months (**p ≤ 0.0005**). In one adult MHS/RYR1 review, **48%** had elevated CK and **81%** showed muscle abnormalities. | Frequencies vary widely by subtype and cohort. Some statistics come from mixed RYR1/MHS populations rather than strictly biopsy/genotype-defined congenital myopathy cohorts (moreno2024myopathicmanifestationsacross pages 4-5, lawal2018ryanodinereceptor1related pages 1-2). |
| Mechanism / pathophysiology | Three broad mechanisms are described: **(1) RyR1 hyperactivity with Ca²⁺ leak**, **(2) reduced channel activity / excitation-contraction uncoupling**, and **(3) reduced RyR1 protein abundance**. Downstream consequences include altered cytosolic Ca²⁺ homeostasis, sarcoplasmic-reticulum store abnormalities, mitochondrial dysfunction, and oxidative/nitrosative stress that can further damage RyR1 and muscle fibers. | Suggested GO terms: **regulation of release of sequestered calcium ion into cytosol**, **skeletal muscle contraction**, **response to oxidative stress**, **mitochondrial ATP synthesis coupled electron transport**. Suggested CL term: **skeletal muscle fiber cell**. Suggested UBERON: **skeletal muscle tissue**. | Patient/model data showed increased mitochondrial ROS: **26% ± 6.7%** increase in patient myotubes under basal conditions; zebrafish mutant myofibers **1369.0 ± 73.1 AU vs 920.6 ± 114.4 AU** in controls (**P = 0.001**). | Mechanistic evidence is strong but heterogeneous across human cells, zebrafish, mouse, and review synthesis; different variants can produce opposite primary channel effects (hyperactive vs hypomorphic) (beaufils2022therapiesforryr1related pages 1-2, dowling2012oxidativestressand pages 11-12, dowling2012oxidativestressand pages 8-9, dowling2012oxidativestressand pages 12-12). |
| Diagnosis | Diagnostic workup typically integrates **clinical phenotype**, **family history**, **anesthesia/rhabdomyolysis history**, **serum CK**, **electromyography when indicated**, **muscle biopsy/histopathology**, **muscle imaging (MRI)**, and **genetic testing**. NGS has improved diagnosis because earlier approaches focused on hotspot regions and biopsy patterns. | Suggested diagnostic ontology links: congenital myopathy panel, **RYR1 single-gene testing**, **WES/WGS**, malignant hyperthermia evaluation. Suggested HPO/LOINC concepts: **Elevated serum creatine kinase**, muscle MRI abnormalities. | Muscle MRI may show selective patterns; review literature notes **relative rectus femoris sparing** among useful imaging clues. | No single universal diagnostic criterion for the umbrella term; biopsy findings and MRI patterns overlap with other congenital myopathies, so molecular confirmation is increasingly central (lawal2018ryanodinereceptor1related pages 1-2). |
| Epidemiology / population | Pediatric point prevalence in the United States has been estimated at **~1:90,000** for RYR1-RM. Dominant **RYR1** variants also contribute to malignant hyperthermia susceptibility, broadening the clinically relevant population. | Disease-level prevalence identifier resources require verification in Orphanet/OMIM. Suggested population descriptors: pediatric congenital myopathy cohorts; anesthesia-triggered MHS cohorts. | Ongoing observational prevalence work: **NCT06791369** plans **~2000** participants using retrospective data from UK and Netherlands specialist centers. | The 1:90,000 estimate is frequently cited but comes from pediatric point-prevalence review synthesis; true prevalence is uncertain and likely underestimated due to underdiagnosis and expanded genotypic spectrum (lawal2018ryanodinereceptor1related pages 1-2, NCT06791369 chunk 3, beaufils2022therapiesforryr1related pages 1-2). |
| Management / current care | No FDA-approved disease-modifying therapy exists. Current care is mainly **supportive and rehabilitative** plus **risk avoidance**: physical therapy, respiratory monitoring, orthopedic management, management of fatigue, and avoidance of malignant-hyperthermia-triggering anesthetics where relevant. Off-label/experimental pharmacologic approaches discussed include **dantrolene**, **N-acetylcysteine (NAC)**, **salbutamol/albuterol**, **pyridostigmine**, and preclinical agents such as **AICAR** or rycals. | Suggested NCIT intervention terms: **Physical Therapy**, **Respiratory Support**, **Dantrolene**, **N-Acetylcysteine**, **Albuterol**, **Pyridostigmine**. Suggested CHEBI terms: calcium, reactive oxygen species, N-acetylcysteine. | NAC reduced oxidative stress in models; no approved standard pharmacotherapy yet. Personalized, genotype-aware strategies are emphasized because “one treatment fits all” is unlikely. | Evidence quality varies from case reports and small open-label studies to preclinical models; supportive care remains the clinical standard (lawal2018ryanodinereceptor1related pages 11-12, beaufils2022therapiesforryr1related pages 7-8, dowling2012oxidativestressand pages 11-12). |
| Trials / recent developments | Clinical development is active. **NCT04141670** evaluated **S 48168 / ARM210** (rycal) in adults with RYR1-RM; ClinicalTrials.gov notes a completed phase 1 study and links to a **2024** publication by Todd et al. (**PMID: 38318125**). **NCT07560020** is a recruiting **phase 2** placebo-controlled adult trial of **Surlorian (ARM210, S48168)** with planned enrollment **28**. Natural-history work includes **NCT06157268** (recruiting observational study, target **100**) and longstanding congenital-myopathy genetics studies such as **NCT00272883**. | Suggested NCIT terms: **Clinical Trial**, **Phase 1 Trial**, **Phase 2 Trial**, **Observational Study**, **Placebo**. | NCT04141670 enrolled **7** participants; NCT07560020 target **28**; NCT06157268 target **100**; NCT06791369 target **2000**. | Phase 1/2 studies are small and early; efficacy conclusions remain preliminary. Trial names and statuses should be rechecked at ClinicalTrials.gov at use time (NCT04141670 chunk 2, NCT06791369 chunk 3). |
| Models / comparative biology | Disease mechanisms and therapy testing use **zebrafish**, **mouse**, **patient-derived myotubes**, and emerging **iPSC / engineered skeletal muscle** systems. Natural disease relevance also extends to **pig** literature mainly through malignant hyperthermia/RYR1 biology rather than a full human-like congenital-myopathy spectrum. | Suggested model resources: zebrafish RYR1 mutants, knock-in mouse models, patient myotubes, iPSC-derived skeletal muscle. Suggested CL terms: **myoblast**, **myotube**, **skeletal muscle fiber cell**. | In zebrafish and patient myotubes, NAC improved oxidative-stress phenotypes; mouse models have been used for calcium-leak, heat sensitivity, and rycal/AICAR studies. | Model evidence is highly informative mechanistically but does not fully recapitulate human phenotypic heterogeneity. The iPSC evidence cited in current context is preprint/future-dated and should not be treated as established clinical evidence (dowling2012oxidativestressand pages 11-12, dowling2012oxidativestressand pages 8-9, rossi2026advancedmodellingof pages 1-5). |


*Table: This compact table summarizes the core knowledge-base elements for RYR1-related myopathy, including spectrum, mechanisms, diagnosis, epidemiology, management, trials, and models. It also flags where identifier mappings or quantitative estimates require external database verification.*

## 1. Disease information

### Definition and scope

RYR1-RM is best treated as a **molecularly defined disease family**, rather than one uniform clinicopathologic entity. Historically, classification depended on muscle-biopsy patterns; sequencing of the entire large RYR1 coding region has shown extensive overlap among biopsy patterns and clinical presentations. As Lawal and colleagues state in the abstract, “**RYR1-RM are the most common class of congenital myopathies**,” and the expanded spectrum is partly attributable to next-generation sequencing beyond historical hotspot testing. Published October 2018; DOI: https://doi.org/10.1007/s13311-018-00677-1. (lawal2018ryanodinereceptor1related pages 1-2)

### Identifiers and synonyms

* **Gene:** RYR1; chromosome **19q13.2**; 106 exons; protein 5,038 amino acids and approximately 565 kDa. (beaufils2022therapiesforryr1related pages 1-2)
* **Common names:** RYR1-related myopathy, ryanodine receptor 1-related myopathy, RYR1-related congenital myopathy, RYR1-RM.
* **Relevant OMIM phenotypic entries:** central core disease (**OMIM 117000**), malignant hyperthermia susceptibility 1 (**OMIM 145600**), and multiminicore disease with external ophthalmoplegia (**OMIM 255320**). These are subtype entries, not exact synonyms for the entire umbrella.
* **MONDO:** a single stable umbrella mapping could not be verified from the retrieved sources. A production knowledge base should map the umbrella to its constituent MONDO subtype records rather than assign an unverified ID.
* **ICD:** ICD-10/ICD-11 generally classify these under congenital myopathy/other specified myopathy and, separately, malignant hyperthermia; no retrieved source established one specific code encompassing the full RYR1-RM spectrum.
* **MeSH:** “Central Core Disease” and “Malignant Hyperthermia” are relevant subtype concepts; “RYR1-related myopathy” is not reliably represented as one umbrella descriptor in the evidence reviewed.

The information in this report is **aggregated disease-level evidence** from publications, registries, and ClinicalTrials.gov—not individual-patient EHR data.

## 2. Etiology, risk, protection, and gene–environment interaction

### Primary cause

The cause is pathogenic **germline RYR1 variation**. Mechanistic classes include: (1) channel hyperactivity and resting SR Ca²⁺ leak; (2) reduced stimulus-coupled Ca²⁺ release or excitation–contraction uncoupling; and (3) reduced RyR1 abundance, particularly in some recessive genotypes. Approximately 400 variants had been reported by the 2022 therapeutic review, but this is not a current ClinVar count. (beaufils2022therapiesforryr1related pages 1-2, beaufils2022therapiesforryr1related pages 7-8)

Variants are predominantly missense, although nonsense, frameshift, splice-altering, in-frame indel, and structural/deep-intronic alleles occur. Clinical classification must be variant-specific under ACMG/AMP criteria; many rare RYR1 missense variants remain VUS because RYR1 is large and missense variation exists in reference populations. Pathogenic causal alleles are expected to be rare or absent in population databases, but no universal allele-frequency threshold is valid across dominant, recessive, and reduced-penetrance malignant-hyperthermia phenotypes.

### Risk factors

* **Genetic:** one pathogenic dominant allele or biallelic pathogenic/hypomorphic alleles; family history of congenital myopathy, unexplained anesthesia reaction, heat illness, exertional rhabdomyolysis, or persistently raised CK.
* **Environmental triggers:** volatile anesthetics and succinylcholine can precipitate malignant hyperthermia in susceptible people. Heat, fever/pyrexia, and intense or prolonged exercise can precipitate myalgia, hyperCKemia, rhabdomyolysis, or heat illness. A 2024 review described 41 contracture- or genetically confirmed malignant-hyperthermia-susceptible individuals in whom intense exercise or pyrexia preceded reactions, supporting a continuum between anesthesia-triggered and non-anesthetic RYR1 disease. (moreno2024myopathicmanifestationsacross pages 4-5)
* **Age and sex:** both sexes and all ages are affected. No robust sex-specific causal risk was established in the retrieved evidence.
* **Noncausal exposures:** smoking, alcohol, diet, infection, pollution, and occupation are not established primary causes.

### Protective factors

No reproducible human **genetic protective allele** is established. Practical environmental protection consists of avoiding trigger anesthetics, preventing dehydration/overheating, pacing exercise, promptly treating fever, and using individualized emergency plans. These reduce episodes but do not prevent inheritance or constitutive myopathy. Antioxidants are mechanistically plausible but are not proven preventive therapy.

## 3. Phenotypes

Clinical expression ranges from fetal hypokinesia and severe neonatal hypotonia to childhood weakness, apparently static congenital myopathy, episodic adult rhabdomyolysis, or late-onset axial weakness. Dominant CCD is often mild or slowly progressive; recessive disease more often includes generalized weakness, ophthalmoparesis, bulbar/respiratory involvement, scoliosis, and contractures. (lawal2018ryanodinereceptor1related pages 1-2)

| Phenotype | Type, onset, course and impact | Suggested HPO term |
|---|---|---|
| Hypotonia | Sign; congenital/neonatal; variable severity; delays motor milestones | Muscular hypotonia, **HP:0001252** |
| Proximal/generalized weakness | Sign; congenital through adult; often stable or slowly progressive; impairs stairs, rising, lifting and ambulation | Proximal muscle weakness, **HP:0003701**; generalized muscle weakness, **HP:0001324** |
| Fatigue/fatigability | Symptom; common and activity-limiting; may occur despite stable strength | Easy fatigability, **HP:0003388**; exercise intolerance, **HP:0003546** |
| Delayed motor development | Developmental manifestation, principally congenital forms | Motor delay, **HP:0001270** |
| Myalgia/cramps | Episodic or increasingly persistent in adult MHS-associated disease | Myalgia, **HP:0003326**; muscle cramp, **HP:0003394** |
| Rhabdomyolysis/hyperCKemia | Episodic laboratory/clinical phenotype, frequently exercise-, heat-, illness-, or anesthesia-associated | Rhabdomyolysis, **HP:0003201**; elevated CK, **HP:0003236** |
| Scoliosis/contractures | Musculoskeletal signs, more consequential in severe recessive disease; can worsen ventilation and mobility | Scoliosis, **HP:0002650**; joint contracture, **HP:0034392** |
| Facial/bulbar weakness | Signs; feeding, speech, airway-clearance and aspiration impact | Facial muscle weakness, **HP:0002058**; dysphagia, **HP:0002015** |
| External ophthalmoparesis | Sign, especially recessive MmD-spectrum disease | External ophthalmoplegia, **HP:0000544** |
| Respiratory insufficiency | Sign/functional abnormality; may be disproportionate to limb weakness | Respiratory insufficiency, **HP:0002093** |
| Malignant-hyperthermia susceptibility | Latent/episodic pharmacogenetic phenotype | Malignant hyperthermia, **HP:0002047** |

In a mixed RYR1-rhabdomyolysis/MHS-myopathy population summarized in 2024, **48% had elevated CK and 81% had muscle abnormalities**; these figures should not be generalized to every congenital subtype. (moreno2024myopathicmanifestationsacross pages 4-5)

Quality-of-life impact is dominated by fatigue, weakness, limited walking/endurance, pain/cramps, recurrent acute-care episodes, respiratory/orthopedic complications, and anxiety surrounding anesthesia and exertion. A longitudinal 6-minute-walk study found no significant change in total distance over six months but detected within-test fatigability, consistent with a stable/slowly progressive baseline plus activity-related performance decline. Robust EQ-5D, SF-36, survival, and subtype-specific frequency estimates remain limited.

## 4. Genetic and molecular information

**RYR1** is the sole defining causal gene for this disease umbrella. RyR1 forms a homotetrameric channel in the terminal sarcoplasmic-reticulum membrane and interacts functionally with the voltage sensor CaV1.1/DHPR, FKBP12, calmodulin, triadin, calsequestrin, and related triadic proteins. (beaufils2022therapiesforryr1related pages 1-2)

Dominant alleles frequently produce channel gain of function/Ca²⁺ leak or altered gating and are associated with CCD, malignant-hyperthermia susceptibility, and exertional rhabdomyolysis. Recessive combinations can cause reduced protein expression, impaired channel activation, or mixed functional effects and generally produce more severe congenital disease. Both penetrance and expressivity are variable; malignant-hyperthermia penetrance is incomplete and exposure-dependent. No repeat-expansion mechanism, aneuploidy, recurrent translocation, or disease-defining somatic mutation is established.

Potential modifiers include other excitation–contraction-coupling and redox genes, but no modifier is sufficiently validated for routine prognostication. A 2024 candidate-locus study supports a threshold/polygenic model for malignant hyperthermia, but this remains supplementary rather than diagnostic. Disease-specific DNA-methylation, histone, or chromatin signatures are not validated clinically.

## 5. Environmental and lifestyle information

RYR1-RM is not infectious, toxic, or autoimmune in origin. The clinically important environment is **trigger exposure**: anesthetic agents, heat, fever, and intense exercise interact with abnormal channel gating. Sustained Ca²⁺ release increases ATP demand, heat production, contracture, acidosis, membrane injury, CK release, and—at extremes—rhabdomyolysis or malignant hyperthermia. Exercise is not categorically contraindicated; individualized moderate activity, cooling, hydration, and avoidance of exhaustive exertion are preferable to deconditioning.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream lesion:** pathogenic RYR1 allele changes channel gating, stimulus coupling, folding/assembly, or abundance.
2. **Primary cellular defect:** excessive resting Ca²⁺ leak, insufficient depolarization-evoked Ca²⁺ release, or depleted functional channel at the triad.
3. **Functional consequence:** reduced myoplasmic Ca²⁺ transient and force generation causes weakness and fatigability; hyperactive channels confer heat, exercise, and anesthetic-triggered crises.
4. **Downstream amplification:** chronic Ca²⁺ disturbance increases mitochondrial workload and ROS/RNS; oxidative/nitrosative RyR1 modifications can further destabilize the channel.
5. **Tissue pathology:** focal sarcomeric/mitochondrial disorganization produces cores or minicores, fiber-type disproportion, central nuclei, muscle injury, atrophy, and secondary fibrosis.

Human myotubes showed a **26% ± 6.7%** basal increase in mitochondrial ROS. Mutant zebrafish myofibers showed ROS fluorescence of **1,369.0 ± 73.1 versus 920.6 ± 114.4 AU** in controls (**P=0.001**). NAC normalized oxidant measures and protected patient myotubes from oxidant-induced death, although preclinical improvement does not establish clinical efficacy. Dowling et al., April 2012; DOI: https://doi.org/10.1093/brain/aws036. (dowling2012oxidativestressand pages 11-12, dowling2012oxidativestressand pages 8-9, dowling2012oxidativestressand pages 12-12)

**Suggested annotations:** GO biological processes—skeletal-muscle contraction, excitation–contraction coupling, calcium-ion transmembrane transport, release of sequestered Ca²⁺ into cytosol, response to oxidative stress, mitochondrial ATP synthesis; GO cellular components—sarcoplasmic-reticulum membrane, terminal cisterna, T-tubule, calcium-release unit, mitochondrion; GO molecular function—ryanodine-sensitive calcium-release-channel activity. Cell Ontology: skeletal muscle fiber (**CL:0000188**), myoblast (**CL:0000056**), and skeletal-muscle satellite cell. Multi-omics evidence remains exploratory; no validated transcriptomic, proteomic, metabolomic, lipidomic, single-cell, or spatial diagnostic signature exists.

## 7. Anatomical structures affected

The primary organ is **skeletal muscle** (UBERON:0001134), particularly limb-girdle/proximal, axial, paraspinal, respiratory, facial, bulbar, and extraocular muscles depending on genotype. Relative rectus-femoris sparing has been reported as part of a recognizable MRI pattern, but imaging is not independently diagnostic. (lawal2018ryanodinereceptor1related pages 1-2)

At tissue/cell level, multinucleated skeletal myofibers and their triads are affected. Subcellular sites include the sarcoplasmic reticulum, terminal cisternae, T-tubules, RyR1–CaV1.1 calcium-release units, mitochondria, and downstream myofibrils. Weakness is usually bilateral and relatively symmetric; focal/asymmetric disease is atypical and should broaden the differential. The heart is generally spared because cardiac excitation–contraction coupling principally uses RYR2, although cardiac surveillance is appropriate when symptoms or alternative diagnoses warrant it. (beaufils2022therapiesforryr1related pages 1-2)

## 8. Temporal development

Onset may be prenatal, neonatal, childhood, or adult. Congenital disease is chronic and lifelong, commonly static or slowly progressive; severe recessive disease may progress through respiratory and orthopedic complications. Adult MHS-associated disease may begin with cramps/myalgia and evolve toward persistent symptoms and proximal lower-limb weakness. Rhabdomyolysis and malignant-hyperthermia episodes are acute superimposed events rather than conventional relapses. (moreno2024myopathicmanifestationsacross pages 4-5)

There is no formal staging system. Critical intervention windows are before anesthesia, during fever/heat exposure, after the first rhabdomyolysis episode, and early in respiratory or scoliosis progression. True remission is not expected because the genotype persists, although episodic symptoms can resolve and complications can be prevented.

## 9. Inheritance and population

Inheritance is **autosomal dominant or autosomal recessive**. Variable expressivity is pronounced, and penetrance—especially for malignant hyperthermia—is incomplete and exposure-dependent. Genetic anticipation is not established. Parental/germline mosaicism is possible in principle and should be considered when an apparently de novo variant recurs, but its population frequency is unknown. Consanguinity increases the probability of recessive disease. Founder variants exist in some populations, but no single ancestry defines RYR1-RM.

The frequently cited US pediatric point prevalence is approximately **1:90,000**. This is probably an underestimate because mildly affected adults, MHS-only carriers, and previously biopsy-negative individuals may escape diagnosis. (lawal2018ryanodinereceptor1related pages 1-2, beaufils2022therapiesforryr1related pages 1-2)

The ongoing prevalence project **NCT06791369** plans approximately 2,000 records from UK and Dutch specialist centers and includes congenital myopathy and malignant-hyperthermia subgroups; it uses retrospective 2011–2020 data and therefore is not yet a definitive population incidence study. https://clinicaltrials.gov/study/NCT06791369. (NCT06791369 chunk 3)

No reliable annual incidence, carrier frequency, sex ratio, or ethnicity-specific prevalence was established by the retrieved literature.

## 10. Diagnostics

### Recommended pathway

1. Document congenital weakness/hypotonia, fatigability, axial or ocular involvement, rhabdomyolysis, anesthesia reactions, exercise/heat intolerance, and a three-generation pedigree.
2. Measure CK, renal function and urine myoglobin during episodes; baseline CK may be normal or mildly elevated. Obtain pulmonary function—sitting and supine FVC, maximal pressures, sleep assessment when indicated—and orthopedic evaluation.
3. Muscle MRI can identify selective involvement and guide biopsy but is supportive.
4. Perform a congenital-myopathy/rhabdomyolysis panel including full **RYR1** coding and splice regions with deletion/duplication analysis. Single-gene RYR1 testing is suitable when phenotype/family variant is specific. WES or preferably WGS is useful after negative panel testing, particularly for structural, deep-intronic, or blended diagnoses.
5. Confirm segregation, phase recessive variants, review gnomAD/ClinVar, and apply ACMG/AMP criteria with phenotype and functional evidence.
6. Muscle biopsy is now adjunctive: central cores, multiple minicores, core–rod change, central nuclei, type-1 predominance/uniformity, or fiber-type disproportion are suggestive but neither necessary nor specific.

NGS is favored because hotspot-only analysis misses pathogenic variation and histology overlaps among RYR1-RM subtypes. (lawal2018ryanodinereceptor1related pages 1-2)

For malignant-hyperthermia risk, a pathogenic RYR1 variant may establish susceptibility; where genetics is negative or uncertain but clinical risk remains high, specialist in-vitro contracture testing may be considered. CMA, karyotype, FISH, mitochondrial-DNA analysis, and repeat-expansion testing are not first-line unless another diagnosis is suspected. RNA sequencing from muscle can resolve selected splice variants but is not routine screening.

**Differential diagnosis:** SELENON-related myopathy, ACTA1/NEB-related nemaline myopathy, MTM1/DNM2/BIN1/SPEG-associated centronuclear myopathy, CACNA1S-related channelopathy/MHS, STAC3-related Native American myopathy, TTN congenital myopathy, congenital muscular dystrophies, metabolic rhabdomyolysis disorders, mitochondrial myopathy, periodic paralysis, inflammatory myopathy, motor-neuron disease, and neuromuscular-junction disorders.

## 11. Outcomes and prognosis

Most mildly affected dominant patients retain ambulation and have near-normal life expectancy, but robust survival curves are unavailable. Morbidity is driven by fatigue, reduced endurance, pain, scoliosis/contractures, respiratory weakness, episodic rhabdomyolysis, and preventable malignant-hyperthermia crises. Severe neonatal recessive disease can be life-threatening through respiratory insufficiency and feeding/bulbar complications.

Prognostic factors include recessive inheritance, prenatal/neonatal onset, respiratory or bulbar involvement, severe scoliosis, recurrent rhabdomyolysis, and low functional baseline. Genotype alone has limited precision because allelic and intrafamilial expressivity is variable. No validated circulating prognostic biomarker exists; CK is an injury marker, not a reliable measure of chronic severity.

## 12. Treatment and current applications

### Standard management

There is **no FDA-approved disease-modifying treatment**. Current care is multidisciplinary: individualized physiotherapy and moderate aerobic/strength activity, energy conservation, mobility/orthotic support, contracture prevention, scoliosis surveillance, respiratory monitoring and noninvasive ventilation/cough support where needed, swallowing/nutritional support, pain management, and renal monitoring during rhabdomyolysis. (lawal2018ryanodinereceptor1related pages 1-2, beaufils2022therapiesforryr1related pages 7-8)

All affected or potentially susceptible patients should carry an anesthesia alert. Trigger-free anesthesia, machine preparation, monitoring, and immediate dantrolene availability are practical standard implementations. **Dantrolene** is established for acute malignant hyperthermia; chronic oral use for myalgia/cramps remains off-label and limited by weakness, fatigue, and hepatotoxicity risk. Suggested NCIT concepts include Physical Therapy, Respiratory Support, Noninvasive Ventilation, Dantrolene, N-Acetylcysteine, Albuterol, Pyridostigmine, and Clinical Trial.

### Investigational pharmacotherapy

* **N-acetylcysteine (NAC):** reduced oxidative stress and improved selected histological/motor measures in zebrafish and patient myotubes, but the subsequent randomized clinical program did not establish an approved therapy. Preclinical evidence must not be equated with clinical benefit. (dowling2012oxidativestressand pages 11-12, dowling2012oxidativestressand pages 8-9)
* **Salbutamol/albuterol and pyridostigmine:** small uncontrolled reports suggested symptomatic improvement in selected patients; evidence is insufficient for routine disease-modifying use. Pyridostigmine benefit in RYR1-centronuclear cases was reportedly nonsustained. (lawal2018ryanodinereceptor1related pages 11-12)
* **AICAR:** reduced Ca²⁺ leak/ROS-RNS and prevented heat-induced death in an RYR1 mouse model; preclinical only. (lawal2018ryanodinereceptor1related pages 11-12)
* **ARM210/S48168 (surlorian):** a Rycal designed to stabilize the RyR1 complex. Phase 1 **NCT04141670** enrolled seven adults; the linked 2024 open-label dose-escalation publication is PMID **38318125**. The study excluded FVC below 50% predicted and included pharmacokinetic and muscle-biopsy assessments. Small size and open-label design preclude definitive efficacy conclusions. https://clinicaltrials.gov/study/NCT04141670. (NCT04141670 chunk 2)
* **Phase 2:** **NCT07560020**, recruiting, placebo-controlled, planned n=28 adults with autosomal-dominant RYR1-RM. Its identifier indicates a post-2024 development and should not be presented as a 2024 result. https://clinicaltrials.gov/study/NCT07560020.
* **Natural history:** **NCT06157268**, recruiting observational study, planned n=100, studies congenital-myopathy fatigability. https://clinicaltrials.gov/study/NCT06157268.

### Advanced therapy

Gene replacement is difficult because the approximately 15-kb RYR1 coding sequence exceeds conventional single-AAV capacity. Proposed approaches include dual-vector systems, allele-specific silencing, splice correction, CRISPR editing, transcriptional activation for hypomorphic alleles, and RNA delivery. As of the reviewed evidence, these remain preclinical; no RYR1 gene, RNA, or cell therapy is approved. The therapeutic review identifies five target levels: DNA correction, RNA/splicing correction, protein folding/SR stress, triadic Ca²⁺ leak, and ROS/RNS regulation. (beaufils2022therapiesforryr1related pages 7-8)

## 13. Prevention

* **Primary:** inherited disease itself cannot presently be prevented after conception. Genetic counseling, carrier/partner testing in recessive families, prenatal diagnosis, and preimplantation genetic testing are reproductive options after familial variants are established.
* **Secondary:** cascade testing of relatives; early pulmonary, orthopedic, swallowing and functional assessment; specialist evaluation after unexplained heat illness, rhabdomyolysis, or anesthesia reaction. No population newborn screening is available.
* **Tertiary:** trigger-free anesthesia, emergency dantrolene access, heat/exertion plans, hydration, fever management, gradual conditioning, avoidance of prolonged immobilization, and surveillance for respiratory/scoliosis complications.
* **Vaccination:** no disease-specific vaccine; routine vaccination and prompt infection management may indirectly reduce fever- and respiratory-related complications.

## 14. Other species and natural disease

The clearest naturally occurring comparative disease is porcine malignant-hyperthermia/porcine stress syndrome caused by **RYR1** variation in domestic pig (*Sus scrofa*, NCBI Taxon **9823**). It reproduces stress/anesthetic-triggered Ca²⁺ dysregulation, hypermetabolism, rigidity, and meat-quality effects, but porcine inheritance and variant architecture do not reproduce the complete human congenital-myopathy spectrum. There is no zoonotic transmission.

Naturally occurring or breed-associated RYR1 phenotypes have also been reported in other domestic species, but exact OMIA/VBO mappings were not verified here and should be curated directly from those resources. The mechanism is evolutionarily conserved because RyR1-mediated skeletal-muscle Ca²⁺ release is conserved across vertebrates.

## 15. Model organisms and experimental systems

* **Zebrafish:** ryr1 mutant/knockdown models reproduce abnormal swimming, myofibrillar/SR pathology, Ca²⁺ dysfunction, and oxidative stress. They enabled NAC rescue experiments, but teleost paralogy and developmental physiology limit direct genotype–phenotype translation. (dowling2012oxidativestressand pages 11-12, dowling2012oxidativestressand pages 8-9, dowling2012oxidativestressand pages 1-1)
* **Mouse:** knock-in models such as Y522S/Y524S and other humanized alleles reproduce Ca²⁺ leak, heat/anesthetic susceptibility, oxidative/nitrosative stress, core development, and weakness. They are used for dantrolene, AICAR, Rycal, antioxidant, and gene-correction studies; many model one dominant allele and not severe recessive human disease. (lawal2018ryanodinereceptor1related pages 13-13, lawal2018ryanodinereceptor1related pages 11-12)
* **Pig:** a valuable large-animal model of malignant hyperthermia and anesthetic physiology, but less representative of multisystem developmental RYR1-RM.
* **Patient myoblasts/myotubes:** preserve human genotype and revealed increased mitochondrial ROS and oxidant vulnerability, but lack mature innervation, loading, and whole-body pharmacology. (dowling2012oxidativestressand pages 8-9)
* **iPSC-derived and 3-D engineered muscle:** promising for variant-specific Ca²⁺ and contractility assays, genome editing, and personalized drug testing. The retrieved detailed iPSC report was a 2026 preprint and therefore is excluded as established 2023–2024 evidence. (rossi2026advancedmodellingof pages 1-5)

## Evidence appraisal and major gaps

The most authoritative recent source retrieved was the October 2024 *British Journal of Anaesthesia* review of adult myopathic manifestations in malignant-hyperthermia susceptibility (DOI: https://doi.org/10.1016/j.bja.2024.05.046). It strengthens recognition of chronic myalgia, cramps, later weakness, and heat/exercise-triggered rhabdomyolysis as part of an RYR1 continuum. (moreno2024myopathicmanifestationsacross pages 4-5)

Nevertheless, the knowledge base remains limited by heterogeneous subtype definitions, ascertainment through specialist centers, small natural-history cohorts, incomplete penetrance, and scarcity of randomized trials. Reliable annual incidence, carrier frequency, sex/ancestry effects, phenotype percentages by genotype, long-term survival, validated QoL norms, modifier genes, epigenetic signatures, and clinically actionable multi-omics biomarkers are not currently established. Expert interpretation therefore favors a **molecular diagnosis plus individualized functional and trigger-risk assessment**, rather than predicting outcome solely from biopsy label or variant location. (lawal2018ryanodinereceptor1related pages 11-12, beaufils2022therapiesforryr1related pages 7-8)

References

1. (lawal2018ryanodinereceptor1related pages 1-2): Tokunbor A. Lawal, Joshua J. Todd, and Katherine G. Meilleur. Ryanodine receptor 1-related myopathies: diagnostic and therapeutic approaches. Neurotherapeutics, 15:885-899, Oct 2018. URL: https://doi.org/10.1007/s13311-018-00677-1, doi:10.1007/s13311-018-00677-1. This article has 130 citations and is from a peer-reviewed journal.

2. (beaufils2022therapiesforryr1related pages 1-2): Mathilde Beaufils, Lauriane Travard, John Rendu, and Isabelle Marty. Therapies for ryr1-related myopathies: where we stand and the perspectives. Jan 2022. URL: https://doi.org/10.2174/1389201022666210910102516, doi:10.2174/1389201022666210910102516. This article has 15 citations and is from a peer-reviewed journal.

3. (beaufils2022therapiesforryr1related pages 7-8): Mathilde Beaufils, Lauriane Travard, John Rendu, and Isabelle Marty. Therapies for ryr1-related myopathies: where we stand and the perspectives. Jan 2022. URL: https://doi.org/10.2174/1389201022666210910102516, doi:10.2174/1389201022666210910102516. This article has 15 citations and is from a peer-reviewed journal.

4. (moreno2024myopathicmanifestationsacross pages 4-5): Carlos A. Ibarra Moreno, Helga C.A. Silva, Nicol C. Voermans, Heinz Jungbluth, Luuk R. van den Bersselaar, John Rendu, Agnieszka Cieniewicz, Philip M. Hopkins, and Sheila Riazi. Myopathic manifestations across the adult lifespan of patients with malignant hyperthermia susceptibility: a narrative review. British Journal of Anaesthesia, 133(4):759-767, Oct 2024. URL: https://doi.org/10.1016/j.bja.2024.05.046, doi:10.1016/j.bja.2024.05.046. This article has 10 citations and is from a highest quality peer-reviewed journal.

5. (dowling2012oxidativestressand pages 11-12): James J. Dowling, Sandrine Arbogast, Junguk Hur, Darcee D. Nelson, Anna McEvoy, Trent Waugh, Isabelle Marty, Joel Lunardi, Susan V. Brooks, John Y. Kuwada, and Ana Ferreiro. Oxidative stress and successful antioxidant treatment in models of ryr1-related myopathy. Brain : a journal of neurology, 135 Pt 4:1115-27, Apr 2012. URL: https://doi.org/10.1093/brain/aws036, doi:10.1093/brain/aws036. This article has 102 citations.

6. (dowling2012oxidativestressand pages 8-9): James J. Dowling, Sandrine Arbogast, Junguk Hur, Darcee D. Nelson, Anna McEvoy, Trent Waugh, Isabelle Marty, Joel Lunardi, Susan V. Brooks, John Y. Kuwada, and Ana Ferreiro. Oxidative stress and successful antioxidant treatment in models of ryr1-related myopathy. Brain : a journal of neurology, 135 Pt 4:1115-27, Apr 2012. URL: https://doi.org/10.1093/brain/aws036, doi:10.1093/brain/aws036. This article has 102 citations.

7. (dowling2012oxidativestressand pages 12-12): James J. Dowling, Sandrine Arbogast, Junguk Hur, Darcee D. Nelson, Anna McEvoy, Trent Waugh, Isabelle Marty, Joel Lunardi, Susan V. Brooks, John Y. Kuwada, and Ana Ferreiro. Oxidative stress and successful antioxidant treatment in models of ryr1-related myopathy. Brain : a journal of neurology, 135 Pt 4:1115-27, Apr 2012. URL: https://doi.org/10.1093/brain/aws036, doi:10.1093/brain/aws036. This article has 102 citations.

8. (NCT06791369 chunk 3):  The Prevalence of RYR1-related Disease. King's College London. 2025. ClinicalTrials.gov Identifier: NCT06791369

9. (lawal2018ryanodinereceptor1related pages 11-12): Tokunbor A. Lawal, Joshua J. Todd, and Katherine G. Meilleur. Ryanodine receptor 1-related myopathies: diagnostic and therapeutic approaches. Neurotherapeutics, 15:885-899, Oct 2018. URL: https://doi.org/10.1007/s13311-018-00677-1, doi:10.1007/s13311-018-00677-1. This article has 130 citations and is from a peer-reviewed journal.

10. (NCT04141670 chunk 2):  S 48168 (ARM 210) for the Treatment of RYR1-related Myopathies (RYR1-RM). RyCarma Therapeutics, Inc.. 2020. ClinicalTrials.gov Identifier: NCT04141670

11. (rossi2026advancedmodellingof pages 1-5): Lucia Rossi, SungWoo Choi, Isobel Terri Olden, Aude Biehler, Lyn Healy, Francesco Muntoni, Giovanni Baranello, Anna Sarkozy, Valentina Maria Lionello, and Francesco Saverio Tedesco. Advanced modelling of ryr1-related myopathies using human ips cells and 3d engineered skeletal muscles. Unknown journal, Aug 2026. URL: https://doi.org/10.21203/rs.3.rs-10606489/v1, doi:10.21203/rs.3.rs-10606489/v1.

12. (dowling2012oxidativestressand pages 1-1): James J. Dowling, Sandrine Arbogast, Junguk Hur, Darcee D. Nelson, Anna McEvoy, Trent Waugh, Isabelle Marty, Joel Lunardi, Susan V. Brooks, John Y. Kuwada, and Ana Ferreiro. Oxidative stress and successful antioxidant treatment in models of ryr1-related myopathy. Brain : a journal of neurology, 135 Pt 4:1115-27, Apr 2012. URL: https://doi.org/10.1093/brain/aws036, doi:10.1093/brain/aws036. This article has 102 citations.

13. (lawal2018ryanodinereceptor1related pages 13-13): Tokunbor A. Lawal, Joshua J. Todd, and Katherine G. Meilleur. Ryanodine receptor 1-related myopathies: diagnostic and therapeutic approaches. Neurotherapeutics, 15:885-899, Oct 2018. URL: https://doi.org/10.1007/s13311-018-00677-1, doi:10.1007/s13311-018-00677-1. This article has 130 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](RYR1-Related_Myopathy-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.