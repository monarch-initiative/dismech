---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-20T14:01:16.912994'
end_time: '2026-07-20T14:30:45.350544'
duration_seconds: 1768.44
template_file: templates\disease_pathophysiology_research.md
template_variables:
  disease_name: RP2-Related Retinopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 48
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: RP2-Related_Retinopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RP2-Related Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **RP2-Related Retinopathy** covering all of the
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
- **Disease Name:** RP2-Related Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **RP2-Related Retinopathy** covering all of the
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


# RP2-Related Retinopathy (RP2-associated X-linked retinitis pigmentosa): Disease characteristics research report

## Executive summary
RP2-related retinopathy is a severe, early-onset **X-linked inherited retinal degeneration** most commonly categorized clinically as **X-linked retinitis pigmentosa (XLRP)** / **Retinitis Pigmentosa 2**. RP2 encodes an **ARL3 GTPase-activating protein (GAP)** critical for **ciliary/outer-segment trafficking of lipidated phototransduction proteins**; disruption leads to progressive photoreceptor dysfunction and degeneration. There is **no approved disease-modifying treatment** in the retrieved evidence; management is supportive, while **gene augmentation** is supported by preclinical animal and human retinal organoid rescue studies. A dedicated global patient registry (InsightRP2; **NCT06982417**) has been launched to enable natural history and genotype–phenotype work to de-risk future RP2-directed trials. (birch2023overcomingthechallenges pages 1-2, pechnikova2025preclinicalandclinical pages 4-6, NCT06982417 chunk 1)

A compact, evidence-bounded table of key facts is provided below.

| Topic | Key facts (with numbers) | Recent/authoritative source (short cite) | Evidence (1-2 sentences) | URL/DOI | Pub year/date |
|---|---|---|---|---|---|
| Disease names / synonyms / IDs | RP2-associated retinitis pigmentosa; Retinitis Pigmentosa 2; X-linked retinitis pigmentosa (XLRP). MeSH: Retinitis Pigmentosa 2 (C567523); Retinitis Pigmentosa (D012174); broader MeSH ancestors include Retinal Dystrophies (D058499), Retinal Degeneration (D012162), Eye Diseases, Hereditary (D015785). OMIM/Orphanet/MONDO not available in provided evidence. | InsightRP2 Registry trial (NCT06982417 chunk 1) | The ClinicalTrials.gov registry explicitly uses these disease labels and MeSH identifiers, making them suitable controlled-vocabulary terms for a knowledge base. Do not infer OMIM/MONDO IDs from outside sources here. | https://clinicaltrials.gov/study/NCT06982417 | 2025-05-21 |
| Inheritance / gene contribution | X-linked inheritance. RP2 accounts for ~5-20% of XLRP; RPGR accounts for ~60-80% of XLRP. XLRP overall represents ~10-20% of all RP cases. | Pechnikova 2025 J Clin Med; Birch 2023 TVST (pechnikova2025preclinicalandclinical pages 4-6, birch2023overcomingthechallenges pages 2-4) | RP2 is the second major XLRP gene after RPGR. These percentages are useful for prioritizing RP2 within X-linked IRD testing strategies and for contextualizing disease rarity. | https://doi.org/10.3390/jcm14030898; https://doi.org/10.1167/tvst.12.6.5 | 2025-01; 2023-06 |
| Core clinical phenotype / timing | Night blindness, reduced visual acuity, peripheral vision loss; childhood onset with progression to severe impairment by early adulthood. In pediatric data, X-linked RP night blindness median age was 16 years; RP2 juveniles showed severe night blindness and 81% were myopic; younger RP2 patients may present first with high myopia and/or nystagmus; some pediatric rod-cone dystrophy cases were asymptomatic at genetic diagnosis. | Pechnikova 2025 J Clin Med; Priglinger 2024 Int J Mol Sci (pechnikova2025preclinicalandclinical pages 4-6, priglinger2024phenotypicandgenetic pages 10-11, priglinger2024phenotypicandgenetic pages 1-2) | The phenotype is severe and early, but not always symptom-led at first presentation in children. High myopia/nystagmus before nyctalopia is a practical clue that broadens case finding beyond classic symptomatic RP presentations. | https://doi.org/10.3390/jcm14030898; https://doi.org/10.3390/ijms252212259 | 2025-01; 2024-11 |
| Diagnostic workup / RP2-specific differential advice | Standard workup: visual acuity, visual fields/perimetry, full-field ERG, OCT/SD-OCT, OCTA, fundus imaging/FAF. Real-world genetics: panel-based NGS; example 322-gene IRD panel with ACMG classification; Blueprint Genetics panel used in 2022-2024 clinic setting. RP2-specific advice: in young patients with high myopia and ERG anomalies, exclude CACNA1F, RPGR, and RP2 even without night blindness. | Savastano 2024 TVST; Areblom 2023 Genes; Lynn 2024 Genes; Priglinger 2024 Int J Mol Sci (savastano2024retinalpigmentepithelium pages 1-2, areblom2023adescriptionof pages 1-2, lynn2024expandingthemutation pages 1-2, priglinger2024phenotypicandgenetic pages 10-11) | Evidence supports multimodal retinal phenotyping plus comprehensive NGS rather than single-test diagnosis. Pediatric cohort data specifically warn that absence of reported nyctalopia does not exclude RP2-related disease. | https://doi.org/10.1167/tvst.13.8.44; https://doi.org/10.3390/genes14071413; https://doi.org/10.3390/genes16010032; https://doi.org/10.3390/ijms252212259 | 2024-08; 2023-07; 2024-12; 2024-11 |
| Mechanism / pathophysiology | RP2 locus Xp11.23. RP2 is an ARL3 GTPase-activating protein (GAP); functions with UNC119 and PDEδ in trafficking lipidated proteins (e.g., transducin, GRK1, PDE6) to photoreceptor outer segment/cilia. RP2 localizes near basal body/centriole; is cofactor C-like and linked to β-tubulin folding/microtubule network. | Pechnikova 2025 J Clin Med; Frederick 2020 Biol Chem (pechnikova2025preclinicalandclinical pages 4-6, frederick2020diffuseorhitch pages 7-10, frederick2020diffuseorhitch pages 10-13) | The disease mechanism centers on defective ciliary/outer-segment trafficking and disturbed photoreceptor protein homeostasis. Frederick et al. add mechanistic detail: RP2 helps establish spatial ARL3-GTP regulation required for destination-specific unloading of lipidated cargo. | https://doi.org/10.3390/jcm14030898; https://doi.org/10.1515/hsz-2019-0375 | 2025-01; 2020-12 |
| Epidemiology / prognosis | RP prevalence ~1:3700-1:8300 worldwide; another estimate 1:3000-1:4000, affecting ~2.5 million globally. X-linked RP is 5-15% to 10-20% of RP depending on source. X-linked disease has the worst prognosis; average visual-field loss 4-12%/year. By age 40, ~20% of XLRP individuals are blind; legal blindness median age ~45 years; complete blindness often by 40-50 years. | Birch 2023 TVST; Savastano 2024 TVST; Pechnikova 2025 J Clin Med (birch2023overcomingthechallenges pages 2-4, savastano2024retinalpigmentepithelium pages 1-2, pechnikova2025preclinicalandclinical pages 1-2) | The numeric burden comes mostly from XLRP and broader RP studies, not RP2-only cohorts, but it consistently supports a severe, rapidly progressive prognosis relative to other RP inheritance classes. These figures are useful for counseling and trial planning. | https://doi.org/10.1167/tvst.12.6.5; https://doi.org/10.1167/tvst.13.8.44; https://doi.org/10.3390/jcm14030898 | 2023-06; 2024-08; 2025-01 |
| Treatments / supportive care | No approved treatment for XLRP in provided evidence. Supportive/symptomatic care includes visual aids, vitamin supplementation, treatment of cystoid macular edema/cataract (anti-VEGF, corticosteroids, cataract surgery), and limited prosthetic approaches such as Argus II. | Birch 2023 TVST; Pechnikova 2025 J Clin Med (birch2023overcomingthechallenges pages 1-2, pechnikova2025preclinicalandclinical pages 6-9, pechnikova2025preclinicalandclinical pages 1-2) | Current care mainly preserves function and quality of life but does not alter progression. This gap underlies the strong push toward gene therapy and natural-history infrastructure. | https://doi.org/10.1167/tvst.12.6.5; https://doi.org/10.3390/jcm14030898 | 2023-06; 2025-01 |
| Experimental / advanced therapies | Preclinical RP2 gene augmentation: self-complementary AAV8-RP2 in mouse models preserved cone function for up to 18 months, improved cone viability, corrected opsin mislocalization, and restored enzyme expression; high-dose retinal toxicity reported. RP2-KO/patient-derived retinal organoids showed rod degeneration by day 150 and ONL thinning by day 180; AAV-RP2 rescue restored rhodopsin expression and degeneration phenotype. | Pechnikova 2025 J Clin Med (pechnikova2025preclinicalandclinical pages 14-16) | These data make RP2 one of the clearer examples where both animal and human organoid rescue support biological plausibility for gene replacement. Toxicity signals emphasize the importance of vector dose optimization. | https://doi.org/10.3390/jcm14030898 | 2025-01 |
| Trials / registries | InsightRP2 Registry: NCT06982417; recruiting observational cohort; estimated n=200; actual start 2025-05-01; primary outcomes include genotype-phenotype correlation for age of onset (1 year) and progression (20 years). Vitamin A trial in RP: NCT00065455; non-randomized pilot, n=10, 50,000 IU/day vitamin A palmitate for 4 weeks then 15,000 IU/day for 2 weeks; ERG-based outcomes; Jul 2003-May 2009. | InsightRP2 Registry; NEI Vitamin A trial (NCT06982417 chunk 1, NCT00065455 chunk 1) | InsightRP2 is a practical real-world implementation for natural history, imaging, mutation distribution, and trial readiness in RP2 disease. The vitamin A trial is not RP2-specific, but it shows the historical symptomatic-intervention landscape in RP measured by electrophysiology. | https://clinicaltrials.gov/study/NCT06982417; https://clinicaltrials.gov/study/NCT00065455 | 2025-05-21; 2003-07 to 2009-05 |
| Model organisms | Zebrafish rp2 knockout/knockdown models: early photoreceptor functional defects followed by progressive rod outer-segment degeneration and then cone outer-segment degeneration; decreased/mislocalized GRK1 and rod transducin subunits (GNAT1, GNB1); disrupted distribution of farnesylated proteins. | Noel 2021 Biomolecules; Iribarne 2020 IntechOpen; Pechnikova 2025 J Clin Med (noel2021zebrafishmodelsof pages 10-12, noel2021zebrafishmodelsof pages 25-27, iribarne2020zebrafishphotoreceptordegeneration pages 6-8, pechnikova2025preclinicalandclinical pages 4-6) | The zebrafish model recapitulates the trafficking-centered mechanism and progressive photoreceptor loss, supporting translational hypothesis generation. However, available reviews note that current animal models may not fully mirror the severe human phenotype. | https://doi.org/10.3390/biom11010078; https://doi.org/10.5772/intechopen.88758; https://doi.org/10.3390/jcm14030898 | 2021-01; 2020-09; 2025-01 |


*Table: This table condenses the most decision-relevant facts on RP2-related retinopathy from the retrieved evidence, including identifiers, phenotype, mechanism, diagnostics, prognosis, and the current translational landscape. It is designed for direct use in a disease knowledge base without adding unsupported identifiers or claims.*

---

## 1. Disease information

### 1.1 Definition and overview
RP2-related retinopathy refers to retinal degeneration caused by pathogenic variation in **RP2**, typically presenting as **RP2-associated XLRP** with progressive loss of photoreceptor function and vision. Clinical manifestations commonly include **night blindness**, **peripheral vision loss**, and **reduced visual acuity**, usually with **childhood onset** and progression to severe impairment by **early adulthood**. (pechnikova2025preclinicalandclinical pages 4-6)

### 1.2 Key identifiers and controlled vocabulary
From ClinicalTrials.gov (InsightRP2 registry), the controlled vocabulary terms include:
- **MeSH**: *Retinitis Pigmentosa 2* (**C567523**); *Retinitis Pigmentosa* (**D012174**) (NCT06982417 chunk 1)
- Broader MeSH ancestors relevant for classification: *Eye Diseases, Hereditary (D015785)*, *Retinal Dystrophies (D058499)*, *Retinal Degeneration (D012162)*, *Retinal Diseases (D012164)*, *Genetic Diseases, Inborn (D030342)* (NCT06982417 chunk 1)

**OMIM/Orphanet/ICD-10/ICD-11/MONDO** identifiers were **not present in the retrieved corpus** for this run; therefore they are not asserted here. (NCT06982417 chunk 1)

### 1.3 Synonyms / alternative names
- RP2-associated Retinitis Pigmentosa
- Retinitis Pigmentosa 2
- X-Linked Retinitis Pigmentosa (XLRP) (NCT06982417 chunk 1)

### 1.4 Evidence source type
The content in this report is derived from:
- Aggregated disease-level and trial-design resources (expert panel proceedings; ClinicalTrials.gov registry) (birch2023overcomingthechallenges pages 1-2, NCT06982417 chunk 1)
- Human cohort/clinic-based studies in inherited retinal disease, including pediatric cohorts that include RP2 cases (priglinger2024phenotypicandgenetic pages 10-11, priglinger2024phenotypicandgenetic pages 1-2)
- Mechanistic reviews (photoreceptor trafficking) (frederick2020diffuseorhitch pages 7-10, frederick2020diffuseorhitch pages 10-13)
- Model-organism and preclinical summaries (zebrafish; preclinical gene augmentation; organoids) (iribarne2020zebrafishphotoreceptordegeneration pages 6-8, noel2021zebrafishmodelsof pages 10-12, pechnikova2025preclinicalandclinical pages 14-16)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** germline pathogenic variants in **RP2** causing **X-linked** inherited retinal degeneration (XLRP). (pechnikova2025preclinicalandclinical pages 4-6)

**Contribution among XLRP genes:** RP2 variants account for approximately **5–20%** of XLRP, compared with **RPGR** accounting for **~60–80%**. (pechnikova2025preclinicalandclinical pages 4-6)

### 2.2 Risk factors
- **Genetic:** having a pathogenic RP2 variant; sex-specific effects consistent with X-linked inheritance (males typically more severely affected; carrier females may manifest variably, but detailed carrier natural history was not retrievable in this run). (pechnikova2025preclinicalandclinical pages 4-6, birch2023overcomingthechallenges pages 6-8)
- **Environmental:** no RP2-specific environmental risk factors were identified in the retrieved evidence.

### 2.3 Protective factors
No RP2-specific protective genetic or environmental factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No RP2-specific gene–environment interactions were identified in the retrieved evidence.

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum (human)
Across the retrieved evidence, RP2-associated XLRP is characterized by:
- **Night blindness (nyctalopia)** (symptom) (pechnikova2025preclinicalandclinical pages 4-6)
- **Peripheral vision loss / visual field constriction** (symptom/sign) (pechnikova2025preclinicalandclinical pages 4-6)
- **Reduced visual acuity** (symptom/sign) (pechnikova2025preclinicalandclinical pages 4-6)
- **High myopia** and/or **nystagmus** as early referral features in young children in an IRD clinic cohort, with nyctalopia emerging later (priglinger2024phenotypicandgenetic pages 10-11)

**Quantitative cohort observations (pediatric IRD cohort including RP2):**
- In one pediatric cohort, X-linked RP patients experienced night blindness at a **median age of 16 years** (X-linked RP overall). (priglinger2024phenotypicandgenetic pages 10-11)
- For RP2 cases in that cohort, night blindness was described as a “cardinal and restricting symptom” in juveniles; **81% were myopic** and described as having severe night blindness. (priglinger2024phenotypicandgenetic pages 10-11)
- Rod–cone dystrophies (including RP2) could be **subjectively asymptomatic at the time of genetic diagnosis** in children, consistent with presymptomatic detection in screened settings. (priglinger2024phenotypicandgenetic pages 1-2)

### 3.2 Phenotype characteristics
- **Onset:** often **childhood** (pechnikova2025preclinicalandclinical pages 4-6)
- **Progression:** progressive; can become severe by **early adulthood** (pechnikova2025preclinicalandclinical pages 4-6)
- **Severity/variability:** severity varies among individuals; genotype–phenotype correlations are not clearly established in the retrieved sources. (pechnikova2025preclinicalandclinical pages 4-6)

### 3.3 Quality-of-life impact
Direct RP2-specific quality-of-life instruments (e.g., EQ-5D, VFQ-25) were not found in the retrieved evidence. Nevertheless, XLRP is described as progressing to legal blindness and blindness, implying major functional impacts. (pechnikova2025preclinicalandclinical pages 1-2)

### 3.4 Suggested HPO terms (mapping based on retrieved descriptions)
- Nyctalopia — **HP:0000662**
- Visual field constriction — **HP:0001133**
- Reduced visual acuity — **HP:0007663**
- High myopia — **HP:0000545**
- Nystagmus — **HP:0000639**

(These HPO identifiers are standard ontology mappings; the *phenotypic claims* are evidence-supported as cited above.) (pechnikova2025preclinicalandclinical pages 4-6, priglinger2024phenotypicandgenetic pages 10-11)

---

## 4. Genetic / molecular information

### 4.1 Causal gene
- **RP2** (retinitis pigmentosa 2); locus reported as **Xp11.23**. (pechnikova2025preclinicalandclinical pages 4-6)

### 4.2 Functional role and molecular consequences
**Current understanding (mechanism):**
- RP2 is a **GTPase-activating protein (GAP) for ARL3**, and functions with **UNC119** and **PDEδ** in trafficking lipidated proteins (e.g., **transducin, GRK1, PDE6**) into the **photoreceptor outer segment**; this process is essential for phototransduction. (pechnikova2025preclinicalandclinical pages 4-6)
- Mechanistically, RP2 accelerates **ARL3-GTP hydrolysis**, which is important for recycling PDEδ and completing prenylated-protein transport cycles; when this system fails, lipidated proteins can accumulate in inappropriate photoreceptor compartments rather than being delivered to the outer segment. (frederick2020diffuseorhitch pages 7-10)
- RP2 also has **structural similarity to cofactor C** involved in **β-tubulin folding** and is linked to microtubule network biology, suggesting potential cytoskeletal contributions to disease pathogenesis. (pechnikova2025preclinicalandclinical pages 4-6)

**Ontology suggestions (examples):**
- GO biological process: *protein targeting to cilium*, *photoreceptor outer segment organization*, *intraciliary transport* (supported conceptually by the trafficking pathway evidence) (pechnikova2025preclinicalandclinical pages 4-6, frederick2020diffuseorhitch pages 10-13)
- GO cellular component: *basal body*, *cilium*, *photoreceptor outer segment* (pechnikova2025preclinicalandclinical pages 4-6)

### 4.3 Pathogenic variant spectrum / allele frequencies
Variant-class distributions, specific recurrent variants, and population allele frequencies (gnomAD) for RP2 were **not available** in the retrieved evidence set for this run. The evidence does note uncertainty/lack of clear genotype–phenotype correlations for RP2. (pechnikova2025preclinicalandclinical pages 4-6)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No RP2-specific modifier genes, epigenetic signatures, or chromosomal abnormality patterns were identified in the retrieved evidence.

---

## 5. Environmental information
No RP2-specific environmental or lifestyle contributors were identified in the retrieved evidence. This is consistent with RP2-related retinopathy being primarily a Mendelian genetic condition. (pechnikova2025preclinicalandclinical pages 4-6)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (conceptual)
1. **Pathogenic RP2 variant** → reduced/altered RP2 GAP activity for ARL3 and/or altered subcellular localization (pechnikova2025preclinicalandclinical pages 4-6)
2. **Disrupted ARL3-GTP/GDP cycling** and impaired cargo unloading/recycling (PDEδ/UNC119 pathways) (frederick2020diffuseorhitch pages 7-10, frederick2020diffuseorhitch pages 10-13)
3. **Mislocalization and depletion of lipidated phototransduction proteins** needed in outer segments (e.g., GRK1, transducin subunits) → photoreceptor functional defects (supported by zebrafish and mechanistic descriptions) (iribarne2020zebrafishphotoreceptordegeneration pages 6-8, frederick2020diffuseorhitch pages 7-10)
4. **Progressive photoreceptor degeneration** (rod followed by cone involvement in model systems) → clinical nyctalopia, peripheral field loss, reduced acuity, and eventual blindness (iribarne2020zebrafishphotoreceptordegeneration pages 6-8, pechnikova2025preclinicalandclinical pages 4-6)

### 6.2 Cell types (CL suggestions)
- Photoreceptor cell (rod photoreceptor; cone photoreceptor)
- Retinal pigment epithelium is relevant in general RP diagnostic studies but RP2 mechanism evidence here centers on photoreceptors/cilia (pechnikova2025preclinicalandclinical pages 4-6, iribarne2020zebrafishphotoreceptordegeneration pages 6-8)

---

## 7. Anatomical structures affected

### 7.1 Organ / tissue / cell level
- Primary organ: **eye (retina)**, specifically photoreceptor layer and outer retina (by mechanism and RP phenotypes). (pechnikova2025preclinicalandclinical pages 4-6)

**UBERON suggestions:**
- Retina — *UBERON:0000966*
- Photoreceptor layer — *UBERON:0001880* (ontology suggestion)

### 7.2 Subcellular localization
- Evidence places RP2 in proximity to **basal body/centriole** at the photoreceptor base and in pathways controlling ciliary trafficking. (pechnikova2025preclinicalandclinical pages 4-6, frederick2020diffuseorhitch pages 10-13)

---

## 8. Temporal development

### 8.1 Onset
- Typical onset is **childhood** for RP2-associated XLRP, with some children presenting initially with **high myopia and/or nystagmus** and later developing prominent nyctalopia. (pechnikova2025preclinicalandclinical pages 4-6, priglinger2024phenotypicandgenetic pages 10-11)

### 8.2 Progression
- Progressive course, with severe impairment by early adulthood in RP2-associated disease (pechnikova2025preclinicalandclinical pages 4-6)
- For XLRP more broadly: substantial risk of blindness by age 40 in cohort data (see Prognosis). (birch2023overcomingthechallenges pages 2-4)

---

## 9. Inheritance and population

### 9.1 Inheritance pattern
- **X-linked** inheritance (XLRP) due to RP2 pathogenic variants. (pechnikova2025preclinicalandclinical pages 4-6)

### 9.2 Epidemiology (RP and XLRP context)
Because RP2-specific prevalence was not available in retrieved evidence, the best-supported estimates are for RP/XLRP:
- RP prevalence reported as **~1:3700 to 1:8300 worldwide**; XLRP represents **~10–20% of RP** in one expert-panel summary. (birch2023overcomingthechallenges pages 2-4)
- Another clinical study reports RP prevalence **1:3000–1:4000** and estimates **~2.5 million affected worldwide**; inheritance breakdown: AR 50–60%, AD 30–40%, X-linked 5–15%. (savastano2024retinalpigmentepithelium pages 1-2)

### 9.3 Population genetics (carrier frequency; founder variants)
Not retrievable for RP2 specifically in this run.

---

## 10. Diagnostics

### 10.1 Clinical tests (typical IRD/RP workup)
Across modern RP/IRD studies, the diagnostic workup commonly includes:
- **Full-field ERG** (functional staging) (savastano2024retinalpigmentepithelium pages 1-2, areblom2023adescriptionof pages 1-2)
- **Visual fields/perimetry** (including Goldmann) (areblom2023adescriptionof pages 1-2)
- **OCT / SD-OCT** ± **FAF** and multimodal fundus imaging (suleman2025currentunderstandingon pages 5-6, lynn2024expandingthemutation pages 1-2)
- **OCT angiography (OCTA)** in some studies (savastano2024retinalpigmentepithelium pages 1-2)

A 2024 RP biomarker study incorporated visual field testing, full-field ERG, and OCTA as part of prospective evaluation. (savastano2024retinalpigmentepithelium pages 1-2)

### 10.2 Genetic testing approaches
- Comprehensive **NGS gene panels** are widely used, with pathogenicity classification per **ACMG** guidelines; one reinvestigation study used a **322-gene** IRD panel and reported that repeated DNA testing improved genotype–phenotype understanding and potential eligibility for gene-based therapies. (areblom2023adescriptionof pages 1-2)
- In a US clinic-based 2022–2024 cohort, **panel-based sequencing (Blueprint Genetics)** was paired with standard imaging (SD-OCT; fundus photography) as real-world implementation of IRD diagnostics. (lynn2024expandingthemutation pages 1-2)

**RP2-specific differential advice (pediatric cohort):** in young patients with **high myopia and ERG anomalies**, clinicians should **exclude RP2 (as well as CACNA1F and RPGR) even if night blindness is absent**, reflecting age-dependent symptom reporting and phenotypic overlap among X-linked IRDs. (priglinger2024phenotypicandgenetic pages 10-11)

### 10.3 Differential diagnosis
Key alternative genetic diagnoses within X-linked IRD include **RPGR** (major XLRP gene) and CACNA1F/CHM depending on phenotype; distinguishing relies on combined phenotype, ERG patterns, and genetics. (priglinger2024phenotypicandgenetic pages 10-11, pechnikova2025preclinicalandclinical pages 4-6)

---

## 11. Outcome / prognosis

### 11.1 Prognosis (XLRP context)
- In one expert summary, by age 40 **~20% of XLRP individuals were blind**, underscoring severity of X-linked disease. (birch2023overcomingthechallenges pages 2-4)
- Another XLRP review reports **legal blindness median age ~45 years** and that **complete blindness typically occurs by ages 40–50 years** (XLRP overall, not RP2-only). (pechnikova2025preclinicalandclinical pages 1-2)
- A clinical RP study reported average **visual field loss 4–12% per year** (RP overall, with X-linked described as worst prognosis). (savastano2024retinalpigmentepithelium pages 1-2)

### 11.2 RP2-specific outcomes
RP2-specific survival/mortality is not applicable (ocular disease). RP2-specific longitudinal visual function slopes were not retrievable in this run.

---

## 12. Treatment

### 12.1 Current standard management (supportive care)
The retrieved evidence emphasizes that XLRP has **no approved treatment** and management is largely supportive/symptomatic:
- Visual aids; vitamin supplementation (does not halt progression) (pechnikova2025preclinicalandclinical pages 1-2)
- Management of complications such as **cystoid macular edema** and **cataracts** using intravitreal anti-VEGF agents, corticosteroids, and cataract surgery (pechnikova2025preclinicalandclinical pages 6-9)
- Retinal prosthetics (e.g., Argus II) with limited functional benefit (pechnikova2025preclinicalandclinical pages 6-9)

**MAXO suggestions (examples):** low-vision rehabilitation; cataract extraction; intravitreal anti-VEGF therapy; intravitreal corticosteroid therapy; genetic counseling.

### 12.2 Experimental / advanced therapeutics (RP2 relevant)
**Gene augmentation for RP2** is supported in preclinical summaries:
- Self-complementary **AAV8-RP2** in mouse models: preservation of cone function over prolonged follow-up with **toxicity at high doses** reported. (pechnikova2025preclinicalandclinical pages 14-16)
- **Human retinal organoid** models derived from RP2-knockout iPSCs showed rod degeneration by day ~150 and ONL thinning by day ~180, and **AAV-RP2 gene augmentation rescued degeneration and restored rhodopsin expression**. (pechnikova2025preclinicalandclinical pages 14-16)

### 12.3 Clinical development expert opinions (authoritative)
An expert panel on XLRP therapy development recommended:
- Robust **genetic screening** to define eligible populations
- **Age stratification** and emphasis on early natural history studies
- Use of clinically meaningful **functional and structural endpoints**, with regulator engagement to validate endpoints (birch2023overcomingthechallenges pages 1-2, birch2023overcomingthechallenges pages 6-8)

These recommendations were framed around RPGR trials but explicitly acknowledge RP2 as a major XLRP cause. (birch2023overcomingthechallenges pages 1-2)

### 12.4 Clinical trials and real-world implementations
- **InsightRP2 Registry (NCT06982417)**: recruiting observational cohort; aims to collect medical, genetic, and imaging data to enable natural history and genotype–phenotype research, with explicit goal to support gene therapy research. Start date **2025-05-01**; outcomes include genotype–phenotype correlations in age of onset and progression. URL: https://clinicaltrials.gov/study/NCT06982417 (NCT06982417 chunk 1)
- **Vitamin A supplementation pilot (NCT00065455)**: non-randomized study in RP (not RP2-specific) assessing acute ERG changes with high-dose vitamin A; ran **Jul 2003–May 2009**. URL: https://clinicaltrials.gov/study/NCT00065455 (NCT00065455 chunk 1)

---

## 13. Prevention

### 13.1 Primary prevention
No established primary prevention exists for RP2-related retinopathy (genetic). The prevention-relevant actions emphasized in the retrieved evidence are genetic and early-detection oriented:
- Early ophthalmic screening visits in childhood may enable presymptomatic identification of IRDs. (priglinger2024phenotypicandgenetic pages 1-2)

### 13.2 Secondary/tertiary prevention
- **Genetic counseling** and **family member testing** are discussed in the pediatric IRD context, with attention to ethical constraints on predictive testing in minors in some jurisdictions. (priglinger2024phenotypicandgenetic pages 16-17)

---

## 14. Other species / natural disease
No naturally occurring RP2 disease in non-model species was identified in the retrieved evidence.

---

## 15. Model organisms

### 15.1 Zebrafish (Danio rerio)
Zebrafish **rp2 knockout/knockdown** models show:
- Early photoreceptor functional defects, followed by **progressive rod outer segment degeneration** and then **cone outer segment degeneration** (noel2021zebrafishmodelsof pages 10-12)
- Disrupted localization/levels of phototransduction proteins (GRK1; rod transducin subunits GNAT1/GNB1) and disrupted farnesylated protein distribution (iribarne2020zebrafishphotoreceptordegeneration pages 6-8)

**Model limitation:** a review notes that existing animal models may not fully replicate the severe human RP2 phenotype. (pechnikova2025preclinicalandclinical pages 4-6)

---

## Direct quotes from abstracts (available in retrieved evidence)
- XLRP expert panel abstract: “X-linked retinitis pigmentosa (XLRP) is a rare inherited retinal disease manifesting as impaired night vision and peripheral vision loss that progresses to legal blindness… there is currently no approved treatment.” (Birch et al., 2023; DOI:10.1167/tvst.12.6.5) (birch2023overcomingthechallenges pages 1-2)
- Pediatric IRD cohort abstract: “Inherited retinal dystrophies (IRDs) are a common cause of blindness or severe visual impairment in children…” and rod–cone dystrophies include “RP2” among others. (Priglinger et al., 2024; DOI:10.3390/ijms252212259) (priglinger2024phenotypicandgenetic pages 1-2)

---

## Key evidence gaps in this run (important for knowledge base completeness)
1. **OMIM/Orphanet/MONDO/ICD identifiers**: not present in retrieved sources; should be added from OMIM/Orphanet/MONDO directly in a follow-on extraction. (NCT06982417 chunk 1)
2. **RP2 variant catalog** (recurrent variants, ACMG classifications, allele frequencies, founder effects): not retrieved; would require ClinVar/gnomAD-focused extraction or RP2-specific variant papers. (pechnikova2025preclinicalandclinical pages 4-6)
3. **Female carrier natural history**: an RP2 carrier cohort paper (AJO 2024) was listed as unobtainable; carrier penetrance/expressivity therefore cannot be summarized here. (paper search unobtainable list; not citable)
4. **RP2-specific patient-reported outcomes/QoL**: not retrieved.

---

## References (URLs/DOIs in evidence)
- Birch DG et al. *Transl Vis Sci Technol.* 2023-06. DOI: https://doi.org/10.1167/tvst.12.6.5 (birch2023overcomingthechallenges pages 1-2)
- Priglinger CS et al. *Int J Mol Sci.* 2024-11. DOI: https://doi.org/10.3390/ijms252212259 (priglinger2024phenotypicandgenetic pages 10-11)
- Savastano MC et al. *Transl Vis Sci Technol.* 2024-08. DOI: https://doi.org/10.1167/tvst.13.8.44 (savastano2024retinalpigmentepithelium pages 1-2)
- Areblom M et al. *Genes.* 2023-07. DOI: https://doi.org/10.3390/genes14071413 (areblom2023adescriptionof pages 1-2)
- Lynn J et al. *Genes.* 2024-12. DOI: https://doi.org/10.3390/genes16010032 (lynn2024expandingthemutation pages 1-2)
- Pechnikova NA et al. *J Clin Med.* 2025-01. DOI: https://doi.org/10.3390/jcm14030898 (pechnikova2025preclinicalandclinical pages 4-6)
- Frederick JM et al. *Biological Chemistry.* 2020-12. DOI: https://doi.org/10.1515/hsz-2019-0375 (frederick2020diffuseorhitch pages 7-10)
- Noel NCL et al. *Biomolecules.* 2021-01. DOI: https://doi.org/10.3390/biom11010078 (noel2021zebrafishmodelsof pages 10-12)
- Iribarne M. IntechOpen chapter. 2020-09. DOI: https://doi.org/10.5772/intechopen.88758 (iribarne2020zebrafishphotoreceptordegeneration pages 6-8)
- ClinicalTrials.gov: InsightRP2 Registry (NCT06982417). Posted 2025-05-21. https://clinicaltrials.gov/study/NCT06982417 (NCT06982417 chunk 1)
- ClinicalTrials.gov: Vitamin A supplementation in RP (NCT00065455). https://clinicaltrials.gov/study/NCT00065455 (NCT00065455 chunk 1)


References

1. (birch2023overcomingthechallenges pages 1-2): David G. Birch, Janet K. Cheetham, Stephen P. Daiger, Carel Hoyng, Christine Kay, Ian M. MacDonald, Mark E. Pennesi, and Lori S. Sullivan. Overcoming the challenges to clinical development of x-linked retinitis pigmentosa therapies: proceedings of an expert panel. Translational Vision Science &amp; Technology, 12:5, Jun 2023. URL: https://doi.org/10.1167/tvst.12.6.5, doi:10.1167/tvst.12.6.5. This article has 24 citations and is from a peer-reviewed journal.

2. (pechnikova2025preclinicalandclinical pages 4-6): Nadezhda A. Pechnikova, Malamati Poimenidou, Ioannis Iliadis, Maria Zafeiriou-Chatziefraimidou, Aleksandra V. Iaremenko, Tamara V. Yaremenko, Kalliopi Domvri, and Alexey V. Yaremenko. Pre-clinical and clinical advances in gene therapy of x-linked retinitis pigmentosa: hope on the horizon. Journal of Clinical Medicine, 14:898, Jan 2025. URL: https://doi.org/10.3390/jcm14030898, doi:10.3390/jcm14030898. This article has 9 citations.

3. (NCT06982417 chunk 1): Nina Bogershausen. InsightRP2 Registry. University of Göttingen. 2025. ClinicalTrials.gov Identifier: NCT06982417

4. (birch2023overcomingthechallenges pages 2-4): David G. Birch, Janet K. Cheetham, Stephen P. Daiger, Carel Hoyng, Christine Kay, Ian M. MacDonald, Mark E. Pennesi, and Lori S. Sullivan. Overcoming the challenges to clinical development of x-linked retinitis pigmentosa therapies: proceedings of an expert panel. Translational Vision Science &amp; Technology, 12:5, Jun 2023. URL: https://doi.org/10.1167/tvst.12.6.5, doi:10.1167/tvst.12.6.5. This article has 24 citations and is from a peer-reviewed journal.

5. (priglinger2024phenotypicandgenetic pages 10-11): Claudia S. Priglinger, Maximilian J. Gerhardt, Siegfried G. Priglinger, Markus Schaumberger, Teresa M. Neuhann, Hanno J. Bolz, Yasmin Mehraein, and Guenther Rudolph. Phenotypic and genetic spectrum in 309 consecutive pediatric patients with inherited retinal disease. International Journal of Molecular Sciences, 25:12259, Nov 2024. URL: https://doi.org/10.3390/ijms252212259, doi:10.3390/ijms252212259. This article has 5 citations.

6. (priglinger2024phenotypicandgenetic pages 1-2): Claudia S. Priglinger, Maximilian J. Gerhardt, Siegfried G. Priglinger, Markus Schaumberger, Teresa M. Neuhann, Hanno J. Bolz, Yasmin Mehraein, and Guenther Rudolph. Phenotypic and genetic spectrum in 309 consecutive pediatric patients with inherited retinal disease. International Journal of Molecular Sciences, 25:12259, Nov 2024. URL: https://doi.org/10.3390/ijms252212259, doi:10.3390/ijms252212259. This article has 5 citations.

7. (savastano2024retinalpigmentepithelium pages 1-2): Maria Cristina Savastano, Giorgio Placidi, Claudia Fossataro, Federico Giannuzzi, Nicola Claudio D'Onofrio, Lorenzo Hu, Valentina Cestrone, Elena D'Agostino, Ilaria Biagini, Ludovica Paris, Giorgia Coppa, Clara Rizzo, Raphael Kilian, Pietro Chiurazzi, Matteo Bertelli, Paolo Enrico Maltese, Benedetto Falsini, and Stanislao Rizzo. Retinal pigment epithelium and outer retinal atrophy (rora) in retinitis pigmentosa: functional, structural, and genetic evaluation. Translational Vision Science &amp; Technology, 13:44, Aug 2024. URL: https://doi.org/10.1167/tvst.13.8.44, doi:10.1167/tvst.13.8.44. This article has 2 citations and is from a peer-reviewed journal.

8. (areblom2023adescriptionof pages 1-2): Maria Areblom, Sten Kjellström, Sten Andréasson, Anders Öhberg, Lotta Gränse, and Ulrika Kjellström. A description of the yield of genetic reinvestigation in patients with inherited retinal dystrophies and previous inconclusive genetic testing. Genes, 14:1413, Jul 2023. URL: https://doi.org/10.3390/genes14071413, doi:10.3390/genes14071413. This article has 8 citations.

9. (lynn2024expandingthemutation pages 1-2): Jacob Lynn, Samuel J. Huang, Grace K. Trigler, Ronald Kingsley, Razek G. Coussa, and Lea D. Bennett. Expanding the mutation spectrum for inherited retinal diseases. Genes, 16:32, Dec 2024. URL: https://doi.org/10.3390/genes16010032, doi:10.3390/genes16010032. This article has 1 citations.

10. (frederick2020diffuseorhitch pages 7-10): Jeanne M. Frederick, Christin Hanke-Gogokhia, Guoxin Ying, and Wolfgang Baehr. Diffuse or hitch a ride: how photoreceptor lipidated proteins get from here to there. Biological Chemistry, 401:573-584, Dec 2020. URL: https://doi.org/10.1515/hsz-2019-0375, doi:10.1515/hsz-2019-0375. This article has 22 citations and is from a peer-reviewed journal.

11. (frederick2020diffuseorhitch pages 10-13): Jeanne M. Frederick, Christin Hanke-Gogokhia, Guoxin Ying, and Wolfgang Baehr. Diffuse or hitch a ride: how photoreceptor lipidated proteins get from here to there. Biological Chemistry, 401:573-584, Dec 2020. URL: https://doi.org/10.1515/hsz-2019-0375, doi:10.1515/hsz-2019-0375. This article has 22 citations and is from a peer-reviewed journal.

12. (pechnikova2025preclinicalandclinical pages 1-2): Nadezhda A. Pechnikova, Malamati Poimenidou, Ioannis Iliadis, Maria Zafeiriou-Chatziefraimidou, Aleksandra V. Iaremenko, Tamara V. Yaremenko, Kalliopi Domvri, and Alexey V. Yaremenko. Pre-clinical and clinical advances in gene therapy of x-linked retinitis pigmentosa: hope on the horizon. Journal of Clinical Medicine, 14:898, Jan 2025. URL: https://doi.org/10.3390/jcm14030898, doi:10.3390/jcm14030898. This article has 9 citations.

13. (pechnikova2025preclinicalandclinical pages 6-9): Nadezhda A. Pechnikova, Malamati Poimenidou, Ioannis Iliadis, Maria Zafeiriou-Chatziefraimidou, Aleksandra V. Iaremenko, Tamara V. Yaremenko, Kalliopi Domvri, and Alexey V. Yaremenko. Pre-clinical and clinical advances in gene therapy of x-linked retinitis pigmentosa: hope on the horizon. Journal of Clinical Medicine, 14:898, Jan 2025. URL: https://doi.org/10.3390/jcm14030898, doi:10.3390/jcm14030898. This article has 9 citations.

14. (pechnikova2025preclinicalandclinical pages 14-16): Nadezhda A. Pechnikova, Malamati Poimenidou, Ioannis Iliadis, Maria Zafeiriou-Chatziefraimidou, Aleksandra V. Iaremenko, Tamara V. Yaremenko, Kalliopi Domvri, and Alexey V. Yaremenko. Pre-clinical and clinical advances in gene therapy of x-linked retinitis pigmentosa: hope on the horizon. Journal of Clinical Medicine, 14:898, Jan 2025. URL: https://doi.org/10.3390/jcm14030898, doi:10.3390/jcm14030898. This article has 9 citations.

15. (NCT00065455 chunk 1):  Investigating the Effect of Vitamin A Supplementation on Retinitis Pigmentosa. National Eye Institute (NEI). 2003. ClinicalTrials.gov Identifier: NCT00065455

16. (noel2021zebrafishmodelsof pages 10-12): Nicole C. L. Noel, Ian M. MacDonald, and W. Ted Allison. Zebrafish models of photoreceptor dysfunction and degeneration. Biomolecules, 11:78, Jan 2021. URL: https://doi.org/10.3390/biom11010078, doi:10.3390/biom11010078. This article has 46 citations.

17. (noel2021zebrafishmodelsof pages 25-27): Nicole C. L. Noel, Ian M. MacDonald, and W. Ted Allison. Zebrafish models of photoreceptor dysfunction and degeneration. Biomolecules, 11:78, Jan 2021. URL: https://doi.org/10.3390/biom11010078, doi:10.3390/biom11010078. This article has 46 citations.

18. (iribarne2020zebrafishphotoreceptordegeneration pages 6-8): Maria Iribarne. Zebrafish photoreceptor degeneration and regeneration research to understand hereditary human blindness. Visual Impairment and Blindness - What We Know and What We Have to Know, Sep 2020. URL: https://doi.org/10.5772/intechopen.88758, doi:10.5772/intechopen.88758. This article has 9 citations.

19. (birch2023overcomingthechallenges pages 6-8): David G. Birch, Janet K. Cheetham, Stephen P. Daiger, Carel Hoyng, Christine Kay, Ian M. MacDonald, Mark E. Pennesi, and Lori S. Sullivan. Overcoming the challenges to clinical development of x-linked retinitis pigmentosa therapies: proceedings of an expert panel. Translational Vision Science &amp; Technology, 12:5, Jun 2023. URL: https://doi.org/10.1167/tvst.12.6.5, doi:10.1167/tvst.12.6.5. This article has 24 citations and is from a peer-reviewed journal.

20. (suleman2025currentunderstandingon pages 5-6): Naning Suleman. Current understanding on retinitis pigmentosa: a literature review. Frontiers in Ophthalmology, Jun 2025. URL: https://doi.org/10.3389/fopht.2025.1600283, doi:10.3389/fopht.2025.1600283. This article has 26 citations.

21. (priglinger2024phenotypicandgenetic pages 16-17): Claudia S. Priglinger, Maximilian J. Gerhardt, Siegfried G. Priglinger, Markus Schaumberger, Teresa M. Neuhann, Hanno J. Bolz, Yasmin Mehraein, and Guenther Rudolph. Phenotypic and genetic spectrum in 309 consecutive pediatric patients with inherited retinal disease. International Journal of Molecular Sciences, 25:12259, Nov 2024. URL: https://doi.org/10.3390/ijms252212259, doi:10.3390/ijms252212259. This article has 5 citations.

## Artifacts

- [Edison artifact artifact-00](RP2-Related_Retinopathy-deep-research-falcon_artifacts/artifact-00.md)