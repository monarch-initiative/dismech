---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-18T12:07:01.206068'
end_time: '2026-05-18T12:20:44.830499'
duration_seconds: 823.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dental Fluorosis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 39
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Dental_Fluorosis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dental Fluorosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Dental Fluorosis** covering all of the
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
- **Disease Name:** Dental Fluorosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Dental Fluorosis** covering all of the
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


# Dental Fluorosis — Comprehensive Disease Characteristics Report

## Target disease
- **Disease name:** Dental fluorosis
- **Category:** Complex, multifactorial developmental defect of enamel
- **Key note on evidence sources:** This report primarily synthesizes peer‑reviewed human epidemiology (NHANES), regional systematic review/meta-analysis, genetic association study, mechanistic review, and an animal multi-omics study, plus ClinicalTrials.gov records. The retrieved corpus did **not** contain ICD-10/ICD-11, MONDO, Orphanet, or SNOMED CT identifiers; where identifiers are missing, this is stated explicitly.

## 1. Disease information

### 1.1 Concise overview (current understanding)
Dental fluorosis is a developmental enamel defect arising from **excess fluoride exposure during tooth development (odontogenesis)**, producing a spectrum of enamel changes (from mild white opacities/striations to more extensive hypomineralization and, at higher severity, post‑eruptive breakdown). (gamarra2024associationbetweenfluoride pages 1-2, hung2023anationalstudy pages 1-2, fejerskov1990thenatureand pages 1-2)

**Direct abstract quotes supporting definition**:
- “Dental fluorosis (DF) is caused by excessive exposure to fluoride during odontogenesis and leads to various changes in the development of tooth enamel.” (Gamarra et al., 2024, BMC Oral Health; published 2024-06; https://doi.org/10.1186/s12903-024-04472-7) (gamarra2024associationbetweenfluoride pages 1-2)
- “Fluoride is commonly consider as a ‘double-edged sword’ because low consumption of fluoride can effectively prevent dental caries, but excessive consumption of fluoride can cause fluorosis.” (Zhang et al., 2023, Frontiers in Cell and Developmental Biology; published 2023-05; https://doi.org/10.3389/fcell.2023.1168215) (zhang2023advancesinepidemiological pages 1-2)

### 1.2 Key identifiers and controlled vocabulary
**MeSH (explicitly present in retrieved ClinicalTrials.gov records):**
- **Fluorosis, Dental (MeSH ID: D009050)** (NCT05204277 chunk 2, NCT05339503 chunk 2)
- **Fluoride Poisoning (MeSH ID: D005458)** appears in some fluorosis-related trial browse modules (NCT01733888 chunk 2, NCT03746990 chunk 1)

**ICD-10 / ICD-11 / MONDO / Orphanet / SNOMED CT:** Not found in the retrieved evidence corpus; therefore not asserted here.

### 1.3 Synonyms and alternative names
- **“Mottled enamel” / “mottling of enamel”** is discussed as a broader descriptor in classic fluorosis literature and appears in at least one fluorosis record excerpt (“mottling of enamel is the most frequently seen and most reliable sign of excessive quantities of fluoride…”). (NCT03746990 chunk 1, fejerskov1990thenatureand pages 1-2)

### 1.4 Evidence provenance (individual vs aggregated)
- Aggregated disease-level resources: systematic review/meta-analysis (Mexico) and narrative/overview reviews (mechanisms and epidemiology). (gamarra2024associationbetweenfluoride pages 1-2, zhang2023advancesinepidemiological pages 1-2)
- Individual-level observational human data: NHANES cross-sectional analysis. (hung2023anationalstudy pages 1-2)
- Individual-level genetics: case-control genotyping study (Tunisia). (kallala2024theassociationbetween pages 2-4)
- Experimental model systems: rat transcriptome/epigenetics. (hu2024effectoflong pages 5-7)

## 2. Etiology

### 2.1 Primary causal factors
**Excess fluoride exposure during enamel formation** is the central environmental cause, with susceptibility confined to the tooth-development window. (gamarra2024associationbetweenfluoride pages 1-2, hung2023anationalstudy pages 1-2)

The Mexico systematic review emphasizes a high-risk developmental period: “the period from six months to four years” as highest risk (as reported in the review text). (gamarra2024associationbetweenfluoride pages 1-2)

### 2.2 Risk factors (recent and quantitative)

#### 2.2.1 Drinking water fluoride concentration (systemic exposure)
In NHANES 2013–2016 (US children/adolescents 6–15 years), higher fluoride in **water** and **plasma** was associated with higher odds of fluorosis graded by Dean’s Index. (hung2023anationalstudy pages 1-2, hung2023anationalstudy pages 4-5)
- **Water fluoride >0.70 mg/L**: adjusted OR **2.790** (95% CI **1.582–5.249**) for fluorosis (combined cycles). (hung2023anationalstudy pages 7-8)
- **Plasma fluoride >0.50 μmol/L**: adjusted OR **1.659** (95% CI **1.154–2.430**) (combined cycles). (hung2023anationalstudy pages 7-8)

**Direct abstract quote**:
- “This cross-sectional study of 2995 children and adolescents found that higher fluoride levels in water and plasma were associated with dental fluorosis.” (Hung et al., 2023, JAMA Network Open; published 2023-06; https://doi.org/10.1001/jamanetworkopen.2023.18406) (hung2023anationalstudy pages 7-8)

#### 2.2.2 Endemic regions and severity gradients (Mexico example, 2024)
In a 2024 systematic review/meta-analysis focused on Northern vs Western Mexico, higher water fluoride in the North was associated with greater fluorosis severity using the TF index. (gamarra2024associationbetweenfluoride pages 1-2)
- North region: higher prevalence of severe cases **≥ TF 5**, pooled estimate **4.78** [3.55, 6.42]. (gamarra2024associationbetweenfluoride pages 1-2)

#### 2.2.3 Other environmental sources (review-level)
Recent review synthesis lists multiple fluoride sources associated with DF risk, including high-fluoride drinking water and other exposure routes (e.g., toothpaste and region-specific dietary/environmental sources), with children being particularly susceptible. (zhang2023advancesinepidemiological pages 1-2)

### 2.3 Protective factors
The retrieved NHANES analysis did not show an increased fluorosis risk signal for reported supplement use (interpretable as reflecting targeted use patterns); however, this should not be interpreted as a general “protective” effect.
- Self-reported fluoride supplements: adjusted OR **0.727** (95% CI 0.459–1.041) in combined-cycle analysis. (hung2023anationalstudy pages 7-8)

### 2.4 Gene–environment interactions
A recent mechanistic/epidemiology review indicates that genetic factors may modify susceptibility under similar fluoride exposure environments and cites gene–environment interaction work (e.g., antioxidant genes with fluoride exposure), but effect sizes were not available in the retrieved excerpts. (zhang2023advancesinepidemiological pages 4-5)

## 3. Phenotypes

### 3.1 Core clinical phenotypes
- **Enamel opacity/white striations** (often mild)
- **Diffuse opacities and discoloration** (yellow/brown staining can occur post-eruption)
- **Hypomineralized, porous enamel**; in more severe cases, **post-eruptive enamel breakdown** (fejerskov1990thenatureand pages 1-2)

**Age of onset / temporal relation:** arises during **childhood odontogenesis**, becomes clinically apparent upon eruption of affected teeth; risk is constrained to the developmental window (NHANES paper notes risk limited to children whose permanent teeth are still developing). (hung2023anationalstudy pages 1-2)

### 3.2 Severity indices and standardized assessment
- **Dean’s Fluorosis Index**: widely used in population studies and clinical trials; NHANES analysis used Dean’s index for grading. (hung2023anationalstudy pages 1-2)
- **Thylstrup–Fejerskov (TF) index**: emphasized as more biologically valid in classic and methodological literature and used in multiple epidemiologic contexts and the Mexico systematic review/meta-analysis. (gamarra2024associationbetweenfluoride pages 1-2, fejerskov1990thenatureand pages 1-2, rozier1994epidemiologicindicesfor pages 1-2)

A simplified TF method (six upper anterior teeth) showed high diagnostic accuracy in endemic areas: sensitivity **90.6%**, specificity **100%**, ROC **0.953**. (Adelário et al., 2010; https://doi.org/10.3390/ijerph7030927) (from retrieved paper list; quantitative values summarized in artifact; not separately evidenced by a pqac excerpt beyond tool retrieval)

### 3.3 Suggested HPO phenotype terms (proposed mappings)
Because the retrieved sources did not provide explicit HPO mappings, the following are **reasonable candidate mappings** based on described clinical manifestations:
- **Enamel hypomineralization** (candidate; aligns with MeSH ancestor “Dental Enamel Hypomineralization”). (NCT05204277 chunk 2)
- **Abnormal tooth enamel coloration / enamel opacity** (candidate)
- **Enamel hypoplasia** may be relevant particularly in severe/endemic fluorosis contexts described as structural defects. (fejerskov1990thenatureand pages 1-2)

### 3.4 Quality of life impact
No 2023–2024 QoL primary studies were retrieved in the tool outputs. The available corpus includes older pediatric QoL evidence indicating fluorosis may impact specific domains (functional domain) rather than overall QoL scores in that sample. (rozier1994epidemiologicindicesfor pages 1-2)

## 4. Genetic / molecular information

### 4.1 Causal vs susceptibility genes
Dental fluorosis is not represented in the retrieved corpus as a single-gene (Mendelian) disorder; evidence supports **susceptibility/modifier genetics**.

### 4.2 Pathogenic/susceptibility variants (human)
**COL1A2 rs412777 (2024, Tunisia; case-control):**
- Study: 95 participants (51 DF cases, 44 controls) collected 2022-07 to 2022-11; DF phenotyped with Dean index; genotyped by PCR-RFLP. (kallala2024theassociationbetween pages 2-4, kallala2024theassociationbetween pages 1-2)
- A allele protective (C vs A): **OR 0.375** (95% CI **0.207–0.672**; **p=0.001**). (kallala2024theassociationbetween pages 2-4)
- AA genotype protective: codominant **OR 0.18** (95% CI **0.06–0.55**; **p=0.002**) and dominant **OR 0.19** (95% CI **0.07–0.52**; **p<0.001**). (kallala2024theassociationbetween pages 2-4)

**Direct abstract quote**:
- “A allele carriers were significantly protected against (DF) when compared to those with the C allele (C vs. A, p = 0.001; OR = 0.375 (0.207–0.672)).” (Kallala et al., 2024; published 2024-03; https://doi.org/10.1186/s12903-024-04086-z) (kallala2024theassociationbetween pages 2-4)

### 4.3 Additional candidate genes (review synthesis)
A 2023 review summarizes candidate gene associations including **TIMP1, DLX1, DLX2, AMBN, COL14A1, MMP20, AMELX, ESR1, SOD2, COL1A2, TFIP11, TUFT1**, among others. (zhang2023advancesinepidemiological pages 2-3)

### 4.4 Epigenetic information (2024 animal multi-omics)
In a rat DF model (NaF exposure), transcriptomics and targeted DNA methylation implicated **Atp2c1** and **Nr1d1** (calcium transport, ER stress, immunity) and broad immune and ion-transport pathways. (hu2024effectoflong pages 5-7, hu2024effectoflong pages 10-13)

**Direct abstract quotes**:
- “The results demonstrated that a total of 1723 differentially expressed genes (DEGs) and 2511 differential expression lncRNAs (DE-lncRNAs) were mainly involved in the ion channels, calcium ion transport, and immunomodulatory signaling pathways.” (Hu et al., 2024; published 2024-04; https://doi.org/10.1007/s12011-023-03660-w) (hu2024effectoflong pages 5-7)
- “ATP2C1 and Nr1d1… may be the key genes in the formation of dental fluorosis.” (Hu et al., 2024; https://doi.org/10.1007/s12011-023-03660-w) (hu2024effectoflong pages 5-7)

## 5. Environmental information

### 5.1 Environmental contributors (non-genetic)
- **Fluoride in drinking water** (high natural groundwater fluoride in endemic areas; systemic exposure reflected by plasma fluoride). (gamarra2024associationbetweenfluoride pages 1-2, hung2023anationalstudy pages 7-8)
- In endemic Mexico regions, groundwater is a major supply and concentrations can exceed regulatory values; the review cites Mexico’s maximum fluoride concentration for natural water as **1.5 ppm** and for bottled water **0.7 ppm** (as stated in the review text). (gamarra2024associationbetweenfluoride pages 1-2)

### 5.2 Lifestyle-related contributors
- Use of fluoride-containing dental products is discussed as potentially contributing to higher prevalence in certain periods/contexts (NHANES discussion). (hung2023anationalstudy pages 7-8)

### 5.3 Infectious agents
Not applicable based on current understanding and the retrieved evidence.

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (integrated model)
1. **Trigger:** Excess fluoride exposure during enamel maturation and/or secretory/maturation stages of amelogenesis (systemic sources such as water; possibly additional sources depending on context). (gamarra2024associationbetweenfluoride pages 1-2, zhang2023advancesinepidemiological pages 1-2)
2. **Cellular stress responses in ameloblasts:** Review synthesis emphasizes fluoride-induced **oxidative stress (ROS)**, **endoplasmic reticulum stress**, **intracellular Ca2+ dysregulation**, and **autophagy perturbation**, which can progress to **ameloblast apoptosis**. (zhang2023advancesinepidemiological pages 1-2)
3. **Matrix processing/mineralization disruption:** Mechanistic literature summarized in reviews points to impacts on enamel matrix protein processing (e.g., effects on **KLK4** activity/expression) and downstream hypomineralization/porosity. (zhang2023advancesinepidemiological pages 5-5)
4. **Tissue outcome:** enamel porosity/hypomineralization → clinical appearance ranging from faint opacities to chalky enamel and structural breakdown at higher severity. (fejerskov1990thenatureand pages 1-2)

### 6.2 Suggested GO biological process terms (proposed)
Based on mechanisms summarized in 2023–2024 sources (primarily review + animal multi-omics):
- **response to endoplasmic reticulum stress / unfolded protein response** (zhang2023advancesinepidemiological pages 5-5, hu2024effectoflong pages 10-13)
- **response to oxidative stress** (zhang2023advancesinepidemiological pages 1-2)
- **autophagy** (zhang2023advancesinepidemiological pages 5-5)
- **apoptotic process** (zhang2023advancesinepidemiological pages 1-2)
- **calcium ion transport / cellular calcium ion homeostasis** (hu2024effectoflong pages 5-7)
- **immune system process / NF-κB signaling** (hu2024effectoflong pages 5-7)

### 6.3 Suggested CL cell types (proposed)
- **ameloblast** (primary target cell type in enamel development, repeatedly referenced in mechanistic frameworks). (fejerskov1990thenatureand pages 1-2, zhang2023advancesinepidemiological pages 1-2)

## 7. Anatomical structures affected

### 7.1 Organ/tissue level
- Primary: **tooth enamel** (developmental defect; permanent teeth prominently relevant to childhood exposure). (hung2023anationalstudy pages 1-2, fejerskov1990thenatureand pages 1-2)

**Suggested UBERON terms (proposed):**
- tooth enamel (UBERON candidate)
- tooth (UBERON candidate)

## 8. Temporal development

### 8.1 Onset and critical window
- Risk is limited to the period of enamel development (odontogenesis), with the Mexico systematic review reporting peak vulnerability “from six months to four years.” (gamarra2024associationbetweenfluoride pages 1-2)

### 8.2 Course
- Once formed, enamel defects are permanent; staining and breakdown may develop after eruption in more severe cases. (fejerskov1990thenatureand pages 1-2)

## 9. Inheritance and population

### 9.1 Epidemiology statistics (recent)
**US (NHANES 2013–2016; JAMA Network Open 2023):**
- Weighted prevalence of any fluorosis: **87.3% (2013–2014)** and **68.2% (2015–2016)** in ages 6–15. (hung2023anationalstudy pages 7-8)

**Regional endemic burden (Mexico; BMC Oral Health 2024):**
- Northern Mexico shows more severe fluorosis distribution (TF ≥5 pooled estimate 4.78 [3.55–6.42]). (gamarra2024associationbetweenfluoride pages 1-2)

### 9.2 Inheritance pattern
- Not Mendelian in retrieved evidence; described as **susceptibility modified by genetics plus environment**. (zhang2023advancesinepidemiological pages 1-2, kallala2024theassociationbetween pages 2-4)

## 10. Diagnostics

### 10.1 Clinical criteria and indices
- **Dean’s Fluorosis Index** (used in NHANES and in genetic association study phenotyping; also referenced in clinical trials). (hung2023anationalstudy pages 1-2, kallala2024theassociationbetween pages 1-2)
- **Thylstrup–Fejerskov (TF) Index** (used in Mexico review inclusion criteria; emphasized for biological validity). (gamarra2024associationbetweenfluoride pages 1-2, fejerskov1990thenatureand pages 1-2)

### 10.2 Differential diagnosis
Formal differential diagnosis was not detailed in retrieved excerpts; however, methodological reviews emphasize the importance of distinguishing fluoride-related enamel changes from other developmental defects of enamel. (rozier1994epidemiologicindicesfor pages 1-2)

### 10.3 Biomarkers
- Plasma fluoride used as systemic exposure biomarker in NHANES analysis and associated with fluorosis odds. (hung2023anationalstudy pages 7-8)

## 11. Outcome / prognosis

- Dental fluorosis is generally not life-threatening; outcomes are predominantly **esthetic** and (in more severe cases) **structural**. Severity correlates with fluoride exposure level. (fejerskov1990thenatureand pages 1-2, gamarra2024associationbetweenfluoride pages 1-2)

## 12. Treatment

### 12.1 Minimally invasive and esthetic management (real-world implementations)
ClinicalTrials.gov records in the retrieved corpus indicate common clinical approaches focused on esthetics for mild–moderate fluorosis:

- **Microabrasion** (e.g., 6.6% HCl + silicon carbide microparticles; Opalustre). (NCT05204277 chunk 2, NCT05051748 chunk 1)
- **In‑office bleaching** (e.g., Opalescence Boost PF 40% hydrogen peroxide). (NCT05051748 chunk 1)
- **Remineralization creams** (e.g., MI‑Paste Plus; CPP‑ACFP). (NCT05204277 chunk 2)
- **Resin infiltration** (ICON) ± bleaching. (NCT01733888 chunk 2)

### 12.2 Experimental/clinical trials (with NCT identifiers)
- **NCT01733888** (Completed; sponsor DMG): resin infiltration vs resin infiltration + bleaching in children 6–12 for fluorosis stains; references published outcomes (PMID 28654721) in the record. (NCT01733888 chunk 2)
- **NCT05204277** (Completed; Suez Canal University): microabrasion vs in-office bleaching vs remineralization (MI‑Paste Plus), TF score 1–4; primary outcome ∆E color change. (NCT05204277 chunk 2)
- **NCT05051748** (Completed; randomized, double-masked): multiple minimal invasive protocols (bleaching, microabrasion, remineralization and combinations) with VAS/photo ratings and patient satisfaction/sensitivity. (NCT05051748 chunk 1, NCT05051748 chunk 2)
- **NCT05339503** (Completed): comparison of microabrasion compounds with tooth shade change outcome. (NCT05339503 chunk 2)

### 12.3 Suggested MAXO terms (proposed)
- enamel microabrasion (maps to MeSH “Enamel Microabrasion”; procedure present in trial record) (NCT05339503 chunk 2)
- tooth bleaching procedure (candidate)
- resin infiltration of enamel lesions (candidate)
- topical remineralization therapy (candidate)

## 13. Prevention

### 13.1 Primary prevention
- **Optimize fluoride exposure during early childhood** by balancing caries prevention benefits with fluorosis risk; the NHANES analysis explicitly frames policy as a balancing act and references the 2015 DHHS optimal fluoridation recommendation (0.7 mg/L) as a potential contributor to changes over time. (hung2023anationalstudy pages 7-8)

**Direct abstract quote**:
- “These findings suggest that public health policy related to water fluoride levels and fluoridation should consider balancing caries prevention with dental fluorosis risk.” (Hung et al., 2023; https://doi.org/10.1001/jamanetworkopen.2023.18406) (hung2023anationalstudy pages 7-8)

### 13.2 Secondary prevention (screening)
- Population surveillance using Dean or TF indices is a standard approach; simplified TF may support feasible screening in endemic areas (accuracy metrics reported in endemic community validation study). (rozier1994epidemiologicindicesfor pages 1-2)

### 13.3 Tertiary prevention
- Esthetic minimally invasive management to address staining/opacities and potential structural susceptibility is supported by multiple clinical trial protocols. (NCT05051748 chunk 1)

## 14. Other species / natural disease
Not evaluated in the retrieved evidence set for this report.

## 15. Model organisms
A rat model with NaF exposure and mandibular molar sampling was used for transcriptomic/epigenetic profiling, providing mechanistic hypotheses linking fluoride exposure to ER stress, calcium homeostasis, and immune signaling during tooth development. (hu2024effectoflong pages 5-7)

---

## Knowledge-base summary table

| Domain | Key points | Quantitative data | Evidence type | Key sources (with DOI/URL if available) |
|---|---|---|---|---|
| Identifiers | Explicit MeSH disease heading available: **Fluorosis, Dental**; related MeSH ancestors include **Dental Enamel Hypomineralization** and **Developmental Defects of Enamel**. Some trial records also map fluorosis-related concepts to **Fluoride Poisoning**. Synonym/descriptor noted in classic literature: **mottled enamel** / mottling of enamel. No explicit ICD-10/ICD-11, MONDO, or SNOMED CT identifiers were retrieved in the available evidence. | MeSH: **D009050** (Fluorosis, Dental); related MeSH: **D005458** (Fluoride Poisoning) | Registry metadata; review/classification literature | ClinicalTrials.gov-derived records (NCT05204277, NCT03746990, NCT05339503, NCT01589991) (NCT05204277 chunk 2, NCT03746990 chunk 1, NCT05339503 chunk 2, NCT01589991 chunk 2); Fejerskov et al. 1990, J Dent Res, DOI: https://doi.org/10.1177/00220345900690s135 (fejerskov1990thenatureand pages 1-2) |
| Definition / overview | Dental fluorosis is a **developmental enamel defect** caused by **excess fluoride exposure during tooth development/odontogenesis**. It manifests as visible enamel changes ranging from faint white lines/opacities to chalky hypomineralized enamel and post-eruptive breakdown in severe cases. Most contemporary sources emphasize that fluorosis is usually mild/cosmetic, but severity rises with higher fluoride exposure. | Vulnerable developmental window reported as **~6 months to 4 years** in the Mexico systematic review; risk generally limited to children whose permanent teeth are still developing (often stated as up to about **8 years**). | Systematic review/meta-analysis; cross-sectional NHANES; classic mechanistic review | Gamarra et al. 2024, BMC Oral Health, DOI: https://doi.org/10.1186/s12903-024-04472-7 (gamarra2024associationbetweenfluoride pages 1-2); Hung et al. 2023, JAMA Netw Open, DOI: https://doi.org/10.1001/jamanetworkopen.2023.18406 (hung2023anationalstudy pages 1-2); Fejerskov et al. 1990, DOI: https://doi.org/10.1177/00220345900690s135 (fejerskov1990thenatureand pages 1-2) |
| Main risk factors | Primary risk factor is **high fluoride intake during odontogenesis**, especially from **drinking water** in endemic areas. Other exposure sources summarized in recent review include **brick tea, coal-burning exposure, fluoridated foods/beverages, and toothpaste**. Severity is dose-related, and Northern Mexico shows higher severity where water fluoride is higher. | NHANES adjusted OR for fluorosis with water fluoride: **AOR 2.378** (95% CI 1.218–5.345) in one model; combined-cycle water fluoride **>0.70 mg/L AOR 2.790** (95% CI 1.582–5.249). Plasma fluoride **AOR 1.568** (95% CI 1.038–2.499); combined **AOR 1.659** (95% CI 1.154–2.430). Mexico meta-analysis: North region severe **TF ≥5 pooled estimate 4.78 [3.55, 6.42]**; West region **≤TF4 pooled estimate 0.01 [0.00, 0.52]**. | Cross-sectional nationally representative study; systematic review/meta-analysis; review | Hung et al. 2023, DOI: https://doi.org/10.1001/jamanetworkopen.2023.18406 (hung2023anationalstudy pages 7-8, hung2023anationalstudy pages 1-2, hung2023anationalstudy pages 4-5); Gamarra et al. 2024, DOI: https://doi.org/10.1186/s12903-024-04472-7 (gamarra2024associationbetweenfluoride pages 1-2); Zhang et al. 2023, DOI: https://doi.org/10.3389/fcell.2023.1168215 (zhang2023advancesinepidemiological pages 1-2) |
| Epidemiology | Recent high-profile US data suggest fluorosis prevalence remains common among children/adolescents, though lower in 2015–2016 than 2013–2014. Regional endemic burdens remain substantial in high-fluoride water areas such as parts of Mexico. | NHANES weighted prevalence of any fluorosis: **87.3% (2013–2014)** and **68.2% (2015–2016)** among ages 6–15. Water fluoride means: **0.56 mg/L** (2013–2014) and **0.46 mg/L** (2015–2016). | Cross-sectional nationally representative survey; regional systematic review/meta-analysis | Hung et al. 2023, DOI: https://doi.org/10.1001/jamanetworkopen.2023.18406 (hung2023anationalstudy pages 7-8, hung2023anationalstudy pages 4-5); Gamarra et al. 2024, DOI: https://doi.org/10.1186/s12903-024-04472-7 (gamarra2024associationbetweenfluoride pages 1-2) |
| Genetic susceptibility | Available human evidence supports **modifier/susceptibility genetics**, not a simple Mendelian cause. Recent Tunisian case-control data implicate **COL1A2 rs412777**. A recent review summarizes additional candidate loci/genes associated with susceptibility: **DLX1, DLX2, MMP13, TIMP1, TIMP2, AMBN, COL14A1, MMP20, AMELX, ESR1, SOD2, TFIP11, TUFT1**. | COL1A2 rs412777: A allele protective **OR 0.375** (95% CI 0.207–0.672; p=0.001). **AA genotype** protective in codominant model **OR 0.18** (95% CI 0.06–0.55; p=0.002) and dominant model **OR 0.19** (95% CI 0.07–0.52; p<0.001). Study size **95** (51 cases, 44 controls). | Human case-control genetics; narrative review of candidate-gene studies | Kallala et al. 2024, BMC Oral Health, DOI: https://doi.org/10.1186/s12903-024-04086-z (kallala2024theassociationbetween pages 2-4, kallala2024theassociationbetween pages 1-2); Zhang et al. 2023, DOI: https://doi.org/10.3389/fcell.2023.1168215 (zhang2023advancesinepidemiological pages 1-2, zhang2023advancesinepidemiological pages 2-3, zhang2023advancesinepidemiological pages 4-5, zhang2023advancesinepidemiological pages 5-5) |
| Gene–environment interaction | Genetics appears to modify susceptibility under shared fluoride exposure environments. The review literature cites interaction studies involving antioxidant genes and fluoride exposure, and Kallala notes prior literature supporting synergistic gene–environment effects. Formal GxE effect estimates were not available in the retrieved excerpts. | Qualitative only in retrieved excerpts; one review cites **SOD2/SOD3 × fluoride exposure** interaction studies without numerical estimates in the available text. | Review of genetic epidemiology; discussion in case-control study | Zhang et al. 2023, DOI: https://doi.org/10.3389/fcell.2023.1168215 (zhang2023advancesinepidemiological pages 4-5, zhang2023advancesinepidemiological pages 5-5); Kallala et al. 2024, DOI: https://doi.org/10.1186/s12903-024-04086-z (kallala2024theassociationbetween pages 4-5) |
| Epigenetic / transcriptomic findings | Experimental evidence indicates dental fluorosis involves broad transcriptomic and epigenetic dysregulation. Rat molar profiling identified **Atp2c1** and **Nr1d1** as key genes linked to **Ca2+ transport, ER stress, and immune regulation**; pathways included ion transport, cytokine signaling, NOD-like receptor signaling, and NF-κB-related immune signaling. Specific DNA methylation changes were reported in multiple genes. | **1,723 DEGs** (1,050 up, 673 down); **2,511 DE-lncRNAs** (1,507 up, 1,004 down); **67 significant KEGG pathways**; targeted methylation across **409 CpGs/17 genes**, with **13 CpG sites** significantly changed. | Animal model multi-omics (RNA-seq + targeted methylation) | Hu et al. 2024, Biol Trace Elem Res, DOI: https://doi.org/10.1007/s12011-023-03660-w (hu2024effectoflong pages 5-7, hu2024effectoflong pages 10-13) |
| Mechanism / pathophysiology | Current mechanistic understanding centers on **ameloblast stress biology**: excessive fluoride can induce **ER stress**, disturb **Ca2+ homeostasis**, increase **oxidative stress/ROS**, alter **autophagy**, reduce **KLK4/MMP20** synthesis or secretion, and promote **ameloblast apoptosis**, impairing enamel matrix removal and maturation and leading to porous hypomineralized enamel. | Retrieved mechanistic papers provide mainly qualitative mechanistic evidence; no single unifying human effect estimate available. | Review; in vitro ameloblast studies; animal multi-omics | Zhang et al. 2023, DOI: https://doi.org/10.3389/fcell.2023.1168215 (zhang2023advancesinepidemiological pages 5-5, zhang2023advancesinepidemiological pages 1-2); Wei et al. 2013, DOI: https://doi.org/10.1002/tox.20724; Zhang et al. 2016, DOI: https://doi.org/10.1016/j.archoralbio.2016.05.015; Suzuki et al. 2015, DOI: https://doi.org/10.1016/j.freeradbiomed.2015.08.015 (mechanistic papers listed in conversation) |
| Diagnostic indices | The main clinical indices identified were **Dean’s Index** and the **Thylstrup–Fejerskov (TF) index**. Dean’s index remains historically dominant and simple; TF is considered more biologically valid and correlates better with histopathology/enamel fluoride. A simplified TF using six upper anterior teeth performed well in endemic settings. | Simplified TF performance: **Sensitivity 90.6%** (95% CI 86.6–93.6), **Specificity 100%** (95% CI 95.3–100), **PPV 100%**, **NPV 77.5%** (95% CI 69.8–83.5), **ROC 0.953** (95% CI 0.933–0.973). | Methods/validation studies; classic review; current systematic review | Adelario et al. 2010, Int J Environ Res Public Health, DOI: https://doi.org/10.3390/ijerph7030927; Rozier 1994, DOI: https://doi.org/10.1177/08959374940080010901 (rozier1994epidemiologicindicesfor pages 1-2); Fejerskov et al. 1990, DOI: https://doi.org/10.1177/00220345900690s135 (fejerskov1990thenatureand pages 1-2); Gamarra et al. 2024, DOI: https://doi.org/10.1186/s12903-024-04472-7 (gamarra2024associationbetweenfluoride pages 1-2) |
| Clinical / public-health implications | Public-health decisions must balance **caries prevention benefits** of fluoride against **fluorosis risk**. Recent US and English data reinforce that fluoride remains protective for caries while higher systemic exposure raises fluorosis odds. Reviews and position statements argue for **optimized**, not indiscriminate, fluoride use. | England ecological study: compared with <0.2 mg/L, CWF prevented **17%–28%** of caries across SES groups and **56%** of dental extractions. NHANES fluorosis odds increased with higher water/plasma fluoride; supplement use was not significantly associated in the retrieved NHANES analysis. | Ecological study; national cross-sectional study; policy statement | Roberts et al. 2023, J Public Health, DOI: https://doi.org/10.1093/pubmed/fdac066; Hung et al. 2023, DOI: https://doi.org/10.1001/jamanetworkopen.2023.18406 (hung2023anationalstudy pages 7-8, hung2023anationalstudy pages 1-2); Lee et al. 2025, DOI: https://doi.org/10.18332/popmed/200818 |
| Treatment trials / implementations | Evidence in the conversation identifies minimally invasive esthetic management strategies: **microabrasion**, **in-office bleaching**, **remineralization/CPP-ACFP (MI-Paste Plus)**, **resin infiltration**, and combinations of these. These are used mainly for **mild–moderate** fluorosis. | **NCT01733888**: resin infiltration ± bleaching for fluorosis stains, pediatric population, enrollment **80**. **NCT05204277**: microabrasion (6.6% HCl + silicon carbide), in-office bleaching, MI-Paste Plus; enrollment **16**. **NCT05051748**: 8 minimally invasive protocols including Opalescence Boost 40%, Opalustre microabrasion, MI-Paste Plus; **160 fluorosed teeth**, follow-up to **6 months**. **NCT05339503**: microabrasion compounds comparison; enrollment **60**. | Interventional clinical trials / registry records | ClinicalTrials.gov NCT01733888 (NCT01733888 chunk 2); NCT05204277 (NCT05204277 chunk 2); NCT05051748 (NCT05051748 chunk 1, NCT05051748 chunk 2); NCT05339503 (NCT05339503 chunk 2) |
| Evidence gaps | No explicit MONDO/ICD/SNOMED identifiers were found in the retrieved evidence. Genetic findings remain heterogeneous and mostly from candidate-gene studies; strong replication and robust formal GxE analyses are limited in the available excerpts. Mechanistic evidence is richer in cell/animal models than in human tissue studies. | Not applicable | Synthesis across retrieved evidence | Based on retrieved sources only (zhang2023advancesinepidemiological pages 1-2, zhang2023advancesinepidemiological pages 2-3, zhang2023advancesinepidemiological pages 4-5, zhang2023advancesinepidemiological pages 5-5, NCT01733888 chunk 2, NCT05204277 chunk 2, fejerskov1990thenatureand pages 1-2) |


*Table: This table summarizes the key knowledge-base fields for dental fluorosis using only evidence retrieved in the conversation. It highlights identifiers, epidemiology, mechanisms, genetics, diagnostic indices, and current treatment/public-health evidence with traceable source citations.*

---

## Limitations of this report (based on retrieved tool evidence)
1. **Ontology/coding coverage:** ICD-10/ICD-11, MONDO, Orphanet, and SNOMED CT identifiers were not present in the retrieved documents and are therefore not asserted here. (NCT05204277 chunk 2, fejerskov1990thenatureand pages 1-2)
2. **QoL evidence (2023–2024):** recent QoL systematic review(s) were listed as unobtainable in tool output; consequently QoL is summarized from older retrieved evidence only. (rozier1994epidemiologicindicesfor pages 1-2)
3. **GxE effect sizes:** while review text indicates gene–environment interaction studies exist, numeric interaction estimates were not available in the retrieved excerpts; therefore GxE is described qualitatively. (zhang2023advancesinepidemiological pages 4-5)


References

1. (gamarra2024associationbetweenfluoride pages 1-2): José Gamarra, David Álvarez-Ordaz, Nelly Molina-Frechero, Leonor Sánchez-Pérez, Alberto Pierdant-Rodriguez, Mario Alberto Isiordia-Espinoza, León Francisco Espinosa-Cristóbal, Marcelo Gómez Palacio-Gastelum, Rogelio González-González, José Salas-Pacheco, and Ronell Bologna-Molina. Association between fluoride intake from drinking water and severity of dental fluorosis in northern and western mexico: systematic review and meta-analysis. BMC Oral Health, Jun 2024. URL: https://doi.org/10.1186/s12903-024-04472-7, doi:10.1186/s12903-024-04472-7. This article has 15 citations and is from a peer-reviewed journal.

2. (hung2023anationalstudy pages 1-2): Man Hung, Eric S. Hon, Amir Mohajeri, Hyma Moparthi, Teresa Vu, Jason Jeon, and Martin S. Lipsky. A national study exploring the association between fluoride levels and dental fluorosis. JAMA Network Open, 6:e2318406, Jun 2023. URL: https://doi.org/10.1001/jamanetworkopen.2023.18406, doi:10.1001/jamanetworkopen.2023.18406. This article has 64 citations and is from a peer-reviewed journal.

3. (fejerskov1990thenatureand pages 1-2): O. Fejerskov, F. Manji, and V. Baelum. The nature and mechanisms of dental fluorosis in man. Journal of Dental Research, 69:692-700, Feb 1990. URL: https://doi.org/10.1177/00220345900690s135, doi:10.1177/00220345900690s135. This article has 467 citations and is from a highest quality peer-reviewed journal.

4. (zhang2023advancesinepidemiological pages 1-2): Kaiqiang Zhang, Zhenfu Lu, and Xiaoying Guo. Advances in epidemiological status and pathogenesis of dental fluorosis. Frontiers in Cell and Developmental Biology, May 2023. URL: https://doi.org/10.3389/fcell.2023.1168215, doi:10.3389/fcell.2023.1168215. This article has 31 citations.

5. (NCT05204277 chunk 2): Mostafa Nasser Abdelmoniem Youssef. Clinical Evaluation of Dental Fluororsis Treatment Modalities. Suez Canal University. 2019. ClinicalTrials.gov Identifier: NCT05204277

6. (NCT05339503 chunk 2): HAREEM ABDUL SATTAR. This is the Comparison of Clinical Effectiveness of Hydrochloric Acid-pumice Compound and Sodium Hypochlorite-pumice Compound Used in Microabrasion Technique for the Treatment of Dental Fluorosis. Change in Tooth Shade Was Checked Before and After the Procedure.. Fatima Jinnah Dental College. 2019. ClinicalTrials.gov Identifier: NCT05339503

7. (NCT01733888 chunk 2):  Resin Infiltration and Resin Infiltration With Bleaching in Improving the Esthetics for Fluorosis Stains. DMG Dental Material Gesellschaft mbH. 2013. ClinicalTrials.gov Identifier: NCT01733888

8. (NCT03746990 chunk 1): sudhir rama varma. Presence of Enamel Fluorosis in Libyan Children. Ajman University. 2017. ClinicalTrials.gov Identifier: NCT03746990

9. (kallala2024theassociationbetween pages 2-4): Rim Kallala, Afef Slimani, Yosra Gassara, Behaeddin Garrach, Sawssen Chouchen, Hajer Foddha, Asma Rouis, and Aberraouf kenani. The association between dental fluorosis and col1a2 gene polymorphism among a tunisian population. BMC Oral Health, Mar 2024. URL: https://doi.org/10.1186/s12903-024-04086-z, doi:10.1186/s12903-024-04086-z. This article has 6 citations and is from a peer-reviewed journal.

10. (hu2024effectoflong pages 5-7): Xiaoyan Hu, Huiru Li, Minzhi Yang, Yujiong Chen, Ailin Zeng, Jiayuan Wu, Jian Zhang, Yuan Tian, Jing Tang, Shengyan Qian, and Mingsong Wu. Effect of long non-coding rna and dna methylation on gene expression in dental fluorosis. Biological Trace Element Research, 202:221-232, Apr 2024. URL: https://doi.org/10.1007/s12011-023-03660-w, doi:10.1007/s12011-023-03660-w. This article has 1 citations and is from a peer-reviewed journal.

11. (hung2023anationalstudy pages 4-5): Man Hung, Eric S. Hon, Amir Mohajeri, Hyma Moparthi, Teresa Vu, Jason Jeon, and Martin S. Lipsky. A national study exploring the association between fluoride levels and dental fluorosis. JAMA Network Open, 6:e2318406, Jun 2023. URL: https://doi.org/10.1001/jamanetworkopen.2023.18406, doi:10.1001/jamanetworkopen.2023.18406. This article has 64 citations and is from a peer-reviewed journal.

12. (hung2023anationalstudy pages 7-8): Man Hung, Eric S. Hon, Amir Mohajeri, Hyma Moparthi, Teresa Vu, Jason Jeon, and Martin S. Lipsky. A national study exploring the association between fluoride levels and dental fluorosis. JAMA Network Open, 6:e2318406, Jun 2023. URL: https://doi.org/10.1001/jamanetworkopen.2023.18406, doi:10.1001/jamanetworkopen.2023.18406. This article has 64 citations and is from a peer-reviewed journal.

13. (zhang2023advancesinepidemiological pages 4-5): Kaiqiang Zhang, Zhenfu Lu, and Xiaoying Guo. Advances in epidemiological status and pathogenesis of dental fluorosis. Frontiers in Cell and Developmental Biology, May 2023. URL: https://doi.org/10.3389/fcell.2023.1168215, doi:10.3389/fcell.2023.1168215. This article has 31 citations.

14. (rozier1994epidemiologicindicesfor pages 1-2): R.G. Rozier. Epidemiologic indices for measuring the clinical manifestations of dental fluorosis: overview and critique. Advances in Dental Research, 8:39-55, Jun 1994. URL: https://doi.org/10.1177/08959374940080010901, doi:10.1177/08959374940080010901. This article has 272 citations and is from a peer-reviewed journal.

15. (kallala2024theassociationbetween pages 1-2): Rim Kallala, Afef Slimani, Yosra Gassara, Behaeddin Garrach, Sawssen Chouchen, Hajer Foddha, Asma Rouis, and Aberraouf kenani. The association between dental fluorosis and col1a2 gene polymorphism among a tunisian population. BMC Oral Health, Mar 2024. URL: https://doi.org/10.1186/s12903-024-04086-z, doi:10.1186/s12903-024-04086-z. This article has 6 citations and is from a peer-reviewed journal.

16. (zhang2023advancesinepidemiological pages 2-3): Kaiqiang Zhang, Zhenfu Lu, and Xiaoying Guo. Advances in epidemiological status and pathogenesis of dental fluorosis. Frontiers in Cell and Developmental Biology, May 2023. URL: https://doi.org/10.3389/fcell.2023.1168215, doi:10.3389/fcell.2023.1168215. This article has 31 citations.

17. (hu2024effectoflong pages 10-13): Xiaoyan Hu, Huiru Li, Minzhi Yang, Yujiong Chen, Ailin Zeng, Jiayuan Wu, Jian Zhang, Yuan Tian, Jing Tang, Shengyan Qian, and Mingsong Wu. Effect of long non-coding rna and dna methylation on gene expression in dental fluorosis. Biological Trace Element Research, 202:221-232, Apr 2024. URL: https://doi.org/10.1007/s12011-023-03660-w, doi:10.1007/s12011-023-03660-w. This article has 1 citations and is from a peer-reviewed journal.

18. (zhang2023advancesinepidemiological pages 5-5): Kaiqiang Zhang, Zhenfu Lu, and Xiaoying Guo. Advances in epidemiological status and pathogenesis of dental fluorosis. Frontiers in Cell and Developmental Biology, May 2023. URL: https://doi.org/10.3389/fcell.2023.1168215, doi:10.3389/fcell.2023.1168215. This article has 31 citations.

19. (NCT05051748 chunk 1): Mostafa Nasser Abdelmoniem Youssef. Clinical Evaluation of Different Minimal Invasive Treatment Modalities of Mild to Moderate Dental Fluorosis Using A Visual Analog Scale. Suez Canal University. 2019. ClinicalTrials.gov Identifier: NCT05051748

20. (NCT05051748 chunk 2): Mostafa Nasser Abdelmoniem Youssef. Clinical Evaluation of Different Minimal Invasive Treatment Modalities of Mild to Moderate Dental Fluorosis Using A Visual Analog Scale. Suez Canal University. 2019. ClinicalTrials.gov Identifier: NCT05051748

21. (NCT01589991 chunk 2): Livia Maria Andaló Tenuta. Anticaries Potential and Fluorosis Risk From Different Fluoride Toothpastes. University of Campinas, Brazil. 2011. ClinicalTrials.gov Identifier: NCT01589991

22. (kallala2024theassociationbetween pages 4-5): Rim Kallala, Afef Slimani, Yosra Gassara, Behaeddin Garrach, Sawssen Chouchen, Hajer Foddha, Asma Rouis, and Aberraouf kenani. The association between dental fluorosis and col1a2 gene polymorphism among a tunisian population. BMC Oral Health, Mar 2024. URL: https://doi.org/10.1186/s12903-024-04086-z, doi:10.1186/s12903-024-04086-z. This article has 6 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Dental_Fluorosis-deep-research-falcon_artifacts/artifact-00.md)