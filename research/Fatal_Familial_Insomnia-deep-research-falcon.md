---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-29T15:02:05.541098'
end_time: '2026-07-29T15:09:03.793327'
duration_seconds: 418.25
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Fatal Familial Insomnia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 12
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Fatal_Familial_Insomnia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Fatal Familial Insomnia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Fatal Familial Insomnia** covering all of the
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
- **Disease Name:** Fatal Familial Insomnia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Fatal Familial Insomnia** covering all of the
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


# Fatal Familial Insomnia: Disease Characteristics Research Report

## Executive summary

Fatal familial insomnia (FFI) is an ultra-rare, autosomal-dominant genetic prion disease caused classically by **PRNP c.532G>A, p.Asp178Asn (D178N), with methionine at polymorphic codon 129 on the mutant allele**. It is characterized by progressive loss of physiologic sleep, dysautonomia, motor dysfunction, cognitive decline, and selective thalamic degeneration. Reported onset spans approximately 19–76 years, averaging about 51 years, and death usually occurs 6–36 months after clinical onset. No therapy has proven disease-modifying efficacy; management remains supportive, although PrP-lowering oligonucleotide programs now provide a plausible mechanism-directed strategy. (forloni2022preventivepharmacologicaltreatment pages 2-3, thune2023geneticvariantsassociated pages 1-2, thune2023geneticvariantsassociated pages 2-4)

The strongest recent FFI-specific evidence retrieved was a 2023 whole-exome study of onset modifiers and a 2022 report of the decade-long preventive doxycycline study. Because FFI is exceptionally rare, many phenotype frequencies, diagnostic-accuracy estimates, and treatment conclusions remain based on small cohorts, families, or extrapolation from other prion diseases rather than large prospective FFI studies. (forloni2022preventivepharmacologicaltreatment pages 3-5, thune2023geneticvariantsassociated pages 2-4, thune2023geneticvariantsassociated pages 8-9)

## 1. Disease information

**Definition.** FFI is an inherited transmissible spongiform encephalopathy in which pathogenic prion-protein conformers produce a rapidly progressive and fatal neurodegenerative syndrome dominated by sleep–wake disintegration, autonomic overactivity, and thalamic dysfunction. It is a disease-level entity assembled from aggregated family, cohort, neuropathology, and molecular resources—not an EHR-derived individual-patient phenotype. Individual case reports and clinical records constitute part of the underlying evidence.

**Identifiers and synonyms.** Commonly used identifiers are **OMIM #600072** and **Orphanet ORPHA:466**; common names include *fatal familial insomnia*, *familial fatal insomnia*, *FFI*, and *genetic fatal insomnia*. The broader ICD-10-CM placement is generally **A81.8, other atypical virus infections of the central nervous system**, under which prion diseases are grouped. Exact current MONDO, MeSH, SNOMED CT, and ICD-11 leaf identifiers should be checked against the release used by the target knowledge base rather than inferred from literature text; the retrieved primary papers did not supply them.

A concise recent description states that FFI is a “rare autosomal-dominant inherited neurodegenerative prion disease” caused by D178N coupled to methionine at codon 129. (thune2023geneticvariantsassociated pages 1-2)

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal and genetic factors

The primary cause is a **heterozygous germline PRNP p.Asp178Asn allele in cis with 129Met**. The same D178N coding change associated with a different codon-129 haplotypic context can produce a genetic Creutzfeldt–Jakob disease phenotype, illustrating that the codon-129 background helps specify prion strain, molecular pathology, and phenotype. FFI is therefore not simply “D178N disease”; haplotype phasing matters. (thune2023geneticvariantsassociated pages 1-2, forloni2022preventivepharmacologicaltreatment pages 1-2)

The polymorphism on the non-mutant allele—129Met or 129Val—modifies onset, duration, and clinical expression, but does not reliably predict an individual’s onset. A 2023 WES study examined 25 D178N/129M patients: 12 women and 13 men, onset 19–68 years. Five had onset at 19–40 years and 20 at 42–68 years. Candidate later-onset modifiers included **EXOC1L, SRSF11, MSANTD3, NR1H5P, and GNA13P1**; the relevant variants were absent from the early-onset group. These remain exploratory associations requiring replication, not clinically validated protective alleles. (thune2023geneticvariantsassociated pages 2-4, thune2023geneticvariantsassociated pages 6-8, thune2023geneticvariantsassociated pages 8-9)

### Penetrance and conventional risk factors

Penetrance is high and age-dependent. In one large Italian kindred, the summarized estimate was about **95%**, based on 46 affected individuals and two apparent elderly nonpenetrant carriers. Family history and inheriting the pathogenic haplotype are the major established risks. There is no convincing evidence that sex, diet, smoking, alcohol, occupation, toxins, or routine lifestyle exposures materially determine disease occurrence. (forloni2022preventivepharmacologicaltreatment pages 2-3)

### Protective and environmental factors

No validated genetic or environmental protective factor prevents FFI. The candidate later-onset variants above are hypotheses rather than actionable protection. No reproducible gene–environment interaction has been established. Ordinary insomnia or sleep deprivation does **not** cause FFI. FFI is genetic, not naturally acquired through infection or routine contact; standard prion precautions nevertheless apply to high-infectivity tissues and certain neurosurgical or laboratory procedures.

## 3. Phenotypes

The core syndrome is progressive and heterogeneous. Exact percentages should not be assigned unless tied to a defined cohort; the available recent evidence supports qualitative frequencies rather than population-wide rates.

- **Progressive insomnia and sleep–wake disintegration:** hallmark, usually severe and progressive. Polysomnography may show loss of normal sleep architecture, poorly formed or absent spindles/K-complexes, reduced slow-wave and REM sleep, and intrusion of motor or dream-like behavior into wakefulness. Suggested HPO: *Insomnia*, *Abnormal sleep pattern*, *Sleep-wake cycle disturbance*.
- **Dysautonomia:** common and often prominent—tachycardia, hypertension, hyperhidrosis, hyperthermia, altered respiratory rhythm, constipation, and endocrine/circadian disturbance. Suggested HPO: *Autonomic nervous system dysfunction*, *Tachycardia*, *Hypertension*, *Hyperhidrosis*, *Abnormal body temperature*.
- **Motor manifestations:** ataxia, dysarthria, gait impairment, tremor, myoclonus, pyramidal signs, parkinsonism, and late akinetic-mutism-like states may occur. Suggested HPO: *Cerebellar ataxia*, *Gait disturbance*, *Dysarthria*, *Myoclonus*, *Parkinsonism*, *Pyramidal sign*.
- **Cognitive/behavioral manifestations:** attentional and executive impairment, memory dysfunction, confusion, hallucinations, behavioral change, and progressive dementia. Suggested HPO: *Cognitive impairment*, *Executive dysfunction*, *Hallucinations*, *Behavioral abnormality*, *Dementia*.
- **Systemic/end-stage manifestations:** weight loss, dysphagia, immobility, aspiration risk, infection, and complete dependence.

Recent literature summarizes the hallmarks as “progressive sleep loss, dementia, and autonomic nervous system failure.” The associated loss of independence, continuous autonomic symptoms, inability to obtain restorative sleep, progressive cognitive/motor disability, and terminal dependence imply profound quality-of-life effects, although validated FFI-specific EQ-5D, SF-36, or PROMIS datasets were not identified. (thune2023geneticvariantsassociated pages 1-2, forloni2022preventivepharmacologicaltreatment pages 1-2)

## 4. Genetic and molecular information

**Gene:** **PRNP**, encoding cellular prion protein, PrPᶜ. **Canonical variant:** NM_000311.5:c.532G>A; NP_000302.1:p.Asp178Asn, traditionally D178N. Laboratories must phase codon 129 because the disease-associated allele is D178N-129M. The variant is a germline missense allele with autosomal-dominant inheritance. It is expected to be absent or extraordinarily rare in population databases; current gnomAD release-specific counts should be queried directly before loading an allele-frequency field.

The pathogenic effect is best described as **toxic conformational gain of function** rather than simple PRNP haploinsufficiency. Mutant PrP favors conversion into misfolded, aggregation-prone, partially protease-resistant disease conformers that template additional PrP conversion. No recurrent causal chromosomal deletion, duplication, translocation, aneuploidy, somatic driver, or mitochondrial variant defines FFI.

Candidate modifier genes from the 2023 WES pilot are provisional. No clinically validated epigenetic modifier or disease-specific methylation signature is established. The authors identified 19 possible onset-associated variants and linked candidate genes to programmed cell death, caspase-mediated cytoskeletal cleavage, and apoptotic protein cleavage. (thune2023geneticvariantsassociated pages 6-8, thune2023geneticvariantsassociated pages 8-9)

## 5. Environmental and infectious information

No toxin, radiation, pollutant, occupation, diet, exercise pattern, tobacco exposure, alcohol use, bacterium, virus, fungus, or parasite is known to cause inherited FFI. The word *prion* denotes a protein-based transmissible agent, but familial disease arises endogenously from mutant PRNP. FFI is not considered contagious through social contact, caregiving, air, food, or body fluids. There is no vaccine indication.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream trigger:** germline D178N-129M changes PrP conformational stability.
2. **Prion conversion:** mutant PrP forms or facilitates a disease-associated conformer capable of templated conversion and aggregation.
3. **Proteostasis and cellular stress:** impaired protein handling, mitochondrial/ribosomal dysfunction, cytoskeletal stress, and apoptotic pathways emerge.
4. **Selective network injury:** severe neuronal loss and astrogliosis preferentially affect anterior and mediodorsal thalamic nuclei, with inferior olivary and entorhinal involvement.
5. **Systems failure:** thalamocortical sleep oscillations collapse; hypothalamic/autonomic and limbic-cognitive networks become dysregulated.
6. **Clinical syndrome:** progressive agrypnia/insomnia, sympathetic overactivity, endocrine/circadian disturbance, ataxia and cognitive decline culminate in immobility and death. (forloni2022preventivepharmacologicaltreatment pages 2-3, thune2023geneticvariantsassociated pages 1-2)

Suggested GO terms include *protein misfolding*, *protein aggregation*, *amyloid fibril formation*, *response to endoplasmic-reticulum stress*, *mitochondrial organization*, *oxidative phosphorylation*, *ribosome biogenesis*, *regulation of circadian rhythm*, *apoptotic process*, *caspase-mediated cleavage*, *neuron death*, and *astrocyte activation*. Relevant cellular components are the neuronal plasma membrane, secretory pathway/ER, endolysosomal system, mitochondrion, ribosome, cytoskeleton, and extracellular protein aggregates.

The principal cell types are thalamic projection neurons, other glutamatergic neurons, inhibitory/GABAergic neurons, and reactive astrocytes; CL labels should include *neuron*, *glutamatergic neuron*, *GABAergic neuron*, and *astrocyte*. The 2023 modifier analysis implicated apoptosis-related biology, but causal roles for the candidate loci have not been experimentally established. (thune2023geneticvariantsassociated pages 6-8, thune2023geneticvariantsassociated pages 8-9)

Human terminal-brain proteomics and experimental cell-type translatomics suggest changes in oxidative phosphorylation, lysosomal/protein-export pathways, mitochondrial and translation machinery, circadian programs, and cytoskeletal responses. These data are mechanistically informative but do not yet constitute a validated diagnostic multi-omics signature. Single-cell and spatial-transcriptomic evidence specific to human FFI remains sparse.

## 7. Anatomical structures affected

The **central nervous system** is the primary organ system. The most characteristic lesions occur bilaterally in the **anterior and mediodorsal/dorsomedial thalamic nuclei**; the inferior olivary nuclei and entorhinal cortex may also be affected. The thalamic pattern is generally bilateral rather than lateralized. Suggested UBERON labels are *brain*, *thalamus*, *mediodorsal nucleus of thalamus*, *anterior thalamic nuclear group*, *inferior olivary complex*, *entorhinal cortex*, *cerebral cortex*, and *hypothalamus*. (forloni2022preventivepharmacologicaltreatment pages 2-3, thune2023geneticvariantsassociated pages 1-2)

Histologically, the dominant lesions are neuronal depletion and astrocytic gliosis. Secondary systemic involvement—cardiovascular, endocrine, thermoregulatory, respiratory, gastrointestinal, and nutritional—is primarily a consequence of autonomic-network failure and terminal neurologic disability rather than primary multiorgan proteinopathy.

## 8. Temporal development

FFI is usually **adult-onset and insidious/subacute**, although onset can occur in young adulthood or late life. Published ranges include **23–76 years**, with an average near **51 years** and a typical range of 36–62 years; the 2023 cohort included onset as early as 19. (thune2023geneticvariantsassociated pages 1-2, thune2023geneticvariantsassociated pages 2-4)

A useful clinical staging model is:

1. **Prodromal/early:** worsening insomnia, altered sleep architecture, anxiety or autonomic activation.
2. **Intermediate:** profound sleep–wake disorganization, dysautonomia, gait/motor impairment, cognitive and behavioral change.
3. **Advanced:** severe dementia/confusion, dysphagia, ataxia or akinetic state, loss of ambulation and self-care.
4. **Terminal:** near-continuous agrypnia, severe autonomic/metabolic instability, mutism/coma-like state, aspiration or infection, and death.

The course is continuously progressive, not relapsing-remitting; durable spontaneous or treatment-induced remission is not documented. Death generally follows within **6–36 months**. Presymptomatic mutation carriers are the most rational intervention population because irreversible neuronal loss probably precedes overt disability. (thune2023geneticvariantsassociated pages 1-2)

## 9. Inheritance and population

Inheritance is **autosomal dominant**: each child of a heterozygous carrier has a 50% chance of inheriting the variant. Penetrance is high but age-dependent and not necessarily absolute; expressivity and age at onset are variable. Anticipation, consanguinity, and germline mosaicism are not established defining features. Founder kindreds exist, including the extensively studied Veneto/Treviso family; FFI has nevertheless been reported across multiple ancestries and geographic regions. (forloni2022preventivepharmacologicaltreatment pages 2-3, forloni2022preventivepharmacologicaltreatment pages 3-5)

The 2023 WES cohort’s near-equal sex distribution—12 women and 13 men—provides no evidence of strong sex bias. Reliable FFI-specific global incidence, point prevalence, and carrier frequency are unavailable. All human prion diseases together occur at roughly 1–2 cases per million person-years, but applying that figure to FFI would grossly overestimate FFI incidence. FFI represents only a very small familial subset.

## 10. Diagnostics

### Recommended approach

1. Recognize progressive insomnia/agrypnia plus dysautonomia, motor/cognitive decline, or a compatible pedigree.
2. Obtain **PRNP sequencing**, explicitly testing D178N and determining/phasing codon 129.
3. Use polysomnography, EEG, MRI, FDG-PET, autonomic testing, neuropsychology, and CSF studies to characterize disease and exclude mimics.
4. Offer postmortem neuropathology where appropriate and consented.

Targeted single-gene sequencing is sufficient when the familial allele is known. A prion/rapid-dementia panel, WES, or WGS is useful for atypical or genetically unresolved cases, but WES/WGS must provide reliable PRNP coverage and codon-129 phasing. CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion testing are not first-line tests for classic FFI.

**Ancillary findings.** PSG is particularly informative because it directly measures the defining physiological disturbance. FDG-PET may reveal thalamic and cingulate/cortical hypometabolism before major structural atrophy. Routine MRI can be normal or nonspecific and often lacks the classic cortical-ribbon/basal-ganglia diffusion pattern of sporadic CJD. EEG may show diffuse slowing but usually not the characteristic periodic sharp-wave complexes of typical sCJD. CSF 14-3-3, total tau, and RT-QuIC may be negative or less sensitive in FFI because neurodegeneration and seeding characteristics differ from sCJD; a negative result cannot exclude genetically confirmed FFI. The retrieved evidence did not support defensible FFI-specific sensitivity or specificity values.

Plasma neurofilament light chain has been reported as increased and is a candidate progression biomarker, but it is a nonspecific axonal-injury marker and not a replacement for PRNP testing. (thune2023geneticvariantsassociated pages 9-10)

**Differential diagnosis:** sporadic fatal insomnia; MM2-thalamic sCJD; other genetic prion diseases; autoimmune/paraneoplastic encephalitis; Lewy-body disease; frontotemporal dementia; multiple-system atrophy; spinocerebellar ataxia; primary psychiatric disease; severe primary insomnia; and toxic-metabolic encephalopathy. Sporadic fatal insomnia lacks the causal familial PRNP haplotype.

Predictive testing in asymptomatic adults requires formal genetic counseling, informed consent, psychological support, and a protocol respecting the right not to know. Testing minors is generally inappropriate for an adult-onset condition without proven childhood intervention.

## 11. Outcome and prognosis

FFI is currently uniformly or nearly uniformly fatal after symptomatic onset; conventional 5- or 10-year survival statistics are not meaningful because most patients die within three years. Historical data from one large family showed mortality peaking near age 53 and only two carriers surviving beyond 60. (forloni2022preventivepharmacologicaltreatment pages 3-5)

Morbidity includes complete sleep disruption, autonomic instability, falls, loss of ambulation, dementia, dysphagia, malnutrition, aspiration, infection, and total dependence. Recovery after established disease is not documented. Codon-129 genotype, age at onset, and candidate modifier loci may influence duration, but no biomarker is validated for precise individual prognostication.

## 12. Treatment and current applications

There is **no approved curative or proven disease-modifying treatment**. Supportive practice includes sleep-symptom management, autonomic and cardiac monitoring, hydration and nutrition, swallowing/aspiration assessment, fall prevention, physical/occupational/speech therapy where feasible, psychiatric support, advance-care planning, and palliative/hospice care. Sedatives may transiently reduce distress but generally do not restore normal sleep architecture; polypharmacy can worsen confusion, falls, or respiratory risk. (forloni2022preventivepharmacologicaltreatment pages 1-2)

**Doxycycline.** The DOXIFF preventive study used doxycycline because preclinical studies suggested interference with β-sheet/aggregate formation plus antioxidant and anti-inflammatory effects. Ten D178N carriers aged 44–53 received **100 mg/day doxycycline hyclate**, while 15 noncarriers received placebo under a genotype-concealing design. Follow-up was planned for ten years; success required fewer than four incident cases. Assessments included biennial neurologic/instrumental visits, annual neuropsychology, six-monthly laboratory sampling, and PSG. The absence of a surrogate endpoint forced comparison with historical incidence. Earlier randomized doxycycline treatment in symptomatic CJD was negative, reinforcing the view that intervention after extensive neurodegeneration may be too late. Published material retrieved here establishes feasibility and design, not proven prevention. (forloni2022preventivepharmacologicaltreatment pages 2-3, forloni2022preventivepharmacologicaltreatment pages 3-5)

**Current translational direction.** PrP lowering is attractive because reducing substrate PrP should act upstream of conformational propagation. Relevant registered programs include **ION717, NCT06153966** (phase 1/2 PrP-lowering antisense program), **NCT07444580** (phase 1 PrP-targeting siRNA safety/mechanism study), **NCT05124392** (at-risk biomarker profiling), and genetic-prion natural-history studies. Eligibility and status must be confirmed directly at ClinicalTrials.gov. These studies are relevant to FFI but do not yet demonstrate clinical benefit.

Suggested MAXO labels: *genetic counseling*, *molecular genetic testing*, *polysomnography*, *neurological examination*, *neuropsychological assessment*, *autonomic monitoring*, *nutritional support*, *physical therapy*, *speech therapy*, *palliative care*, *clinical trial participation*, and *preventive pharmacotherapy*. Suggested CHEBI entity: *doxycycline*.

## 13. Prevention

There is no lifestyle, vaccine, or environmental primary prevention for a person who already carries the pathogenic allele. Mendelian transmission can be prevented or reduced through nondirective reproductive counseling, preimplantation genetic testing for monogenic disease, prenatal diagnosis, donor gametes, or choosing not to have genetically related children. Predictive testing and cascade testing are secondary-prevention/risk-identification measures, not treatment.

Tertiary prevention consists of early recognition of dysphagia, aspiration, falls, malnutrition, autonomic instability, pressure injury, and caregiver distress. At-risk adults may consider longitudinal natural-history or prevention studies. The unusual DOXIFF design preserved participants’ desire not to learn their genotype while allowing preventive research, illustrating the central ethical importance of autonomy in FFI families. (forloni2022preventivepharmacologicaltreatment pages 3-5, forloni2022preventivepharmacologicaltreatment pages 1-2)

## 14. Other species and natural disease

No naturally occurring veterinary disease is recognized as an exact ortholog of human D178N-129M FFI. Other mammals develop natural prion diseases—scrapie in sheep/goats, bovine spongiform encephalopathy, chronic wasting disease in cervids, and feline transmissible spongiform encephalopathy—but these are not FFI and usually arise from different strains, exposure routes, and host PRNP genotypes. Prion mechanisms and PRNP orthologs are evolutionarily conserved, enabling comparative research, but there is no evidence that human FFI is zoonotic or naturally transmitted from FFI families to animals.

Relevant taxa for comparative annotation include *Homo sapiens* (NCBI Taxon 9606) and *Mus musculus* (10090). Breed ontology is not applicable to the human disorder.

## 15. Model organisms

Models include transgenic or knock-in mice expressing FFI-associated mutant PrP, prion-inoculated mice, cultured cells expressing mutant PRNP, protein-conversion assays, and patient-derived cellular systems. D178N/129M mouse models can reproduce mutant-PrP accumulation, selective neurologic injury, sleep/circadian abnormalities, and molecular changes involving mitochondrial/ribosomal programs. Cell-type-specific translatome studies implicate astrocytes, glutamatergic neurons, and GABAergic neurons and suggest that molecular responses can precede EEG or overt histopathology.

Their limitations are important: mouse sleep architecture, lifespan, PRNP expression, strain background, and prion conformers differ from humans; some models require overexpression or inoculation and do not fully reproduce the human thalamic-autonomic syndrome. Consequently, therapeutic success in mice is hypothesis-generating rather than predictive of human efficacy. Candidate-model resources include MGI, IMSR, EMMA, and MMRRC.

## Knowledge-base annotation summary

The following compact mapping separates robust evidence from suggested ontology labels requiring release-specific curator verification.

| Domain | Evidence-backed finding | Suggested ontology terms/identifiers | Evidence type/strength |
|---|---|---|---|
| Disease entity | Fatal familial insomnia (FFI) is an ultra-rare inherited human prion disease with insomnia, dysautonomia, progressive neurologic decline, and death typically within months after onset (forloni2022preventivepharmacologicaltreatment pages 2-3, thune2023geneticvariantsassociated pages 1-2, forloni2022preventivepharmacologicaltreatment pages 1-2) | Disease label: Fatal familial insomnia; MONDO: curator verification needed; OMIM: curator verification needed; Orphanet: curator verification needed; MeSH/ICD: curator verification needed | Human clinical/review; moderate-strong |
| Causal gene/variant | Core causal genotype is germline PRNP p.Asp178Asn (D178N) in cis with methionine at codon 129 on the mutant allele; autosomal dominant inheritance (thune2023geneticvariantsassociated pages 1-2, thune2023geneticvariantsassociated pages 2-4, forloni2022preventivepharmacologicaltreatment pages 1-2) | PRNP (HGNC: curator verification needed); sequence variant: p.Asp178Asn / D178N; codon 129 Met on mutant allele; inheritance: autosomal dominant | Human genetic; strong |
| Penetrance/risk | Penetrance is described as very high; one large Italian kindred report summarized ~95% penetrance with 46 cases and 2 apparent non-penetrant individuals (forloni2022preventivepharmacologicaltreatment pages 2-3) | Inheritance annotation: age-dependent/high penetrance; family history present in many kindreds | Human family data; moderate |
| Onset/natural history | Age at onset is highly variable, reported from 19-76 years; average around 51 years; typical disease duration ~6-36 months after symptom onset (thune2023geneticvariantsassociated pages 1-2, thune2023geneticvariantsassociated pages 2-4) | HPO: Adult onset; Progressive neurologic deterioration; Reduced lifespan; Fatal outcome | Human cohort/review; strong |
| Genetic modifiers | Codon 129 on the non-mutated allele modifies phenotype but does not fully predict onset; WES study identified candidate modifier loci NR1H5P, GNA13P1, EXOC1L, SRSF11, MSANTD3 associated with later onset (thune2023geneticvariantsassociated pages 1-2, thune2023geneticvariantsassociated pages 6-8, thune2023geneticvariantsassociated pages 8-9) | Modifier genes: NR1H5P, GNA13P1, EXOC1L, SRSF11, MSANTD3; note: provisional disease modifiers | Human exploratory genomics; preliminary-moderate |
| Core phenotypes | Hallmark manifestations include progressive insomnia/sleep loss, altered sleep-wake rhythm, autonomic dysfunction, dementia/cognitive decline, and motor signs (forloni2022preventivepharmacologicaltreatment pages 2-3, thune2023geneticvariantsassociated pages 1-2, forloni2022preventivepharmacologicaltreatment pages 1-2) | HPO labels: Insomnia; Sleep disturbance; Abnormality of circadian rhythm; Autonomic nervous system dysfunction; Dementia; Cognitive impairment; Gait disturbance; Ataxia/parkinsonism/motor signs (IDs for curator verification) | Human clinical/review; strong |
| Phenotype severity/course | Disease course is progressive, severe, and usually fatal without remission; symptom heterogeneity is substantial even among patients sharing the same PRNP core genotype (thune2023geneticvariantsassociated pages 1-2, thune2023geneticvariantsassociated pages 8-9) | HPO labels: Progressive neurologic deterioration; Variable expressivity; Lethal phenotype | Human cohort/review; strong |
| Primary anatomy | Selective vulnerability centers on thalamus, especially anterior and dorsomedial/mediodorsal thalamic nuclei; additional involvement includes inferior olive and entorhinal cortex (forloni2022preventivepharmacologicaltreatment pages 2-3, thune2023geneticvariantsassociated pages 1-2) | UBERON labels: thalamus; mediodorsal thalamic nucleus; anterior thalamic nuclei; inferior olivary nucleus; entorhinal cortex (IDs for curator verification) | Human neuropathology; strong |
| Tissue pathology | Neuropathology features severe neuronal loss/depletion, astrocytic gliosis/astrogliosis, and pathologic prion protein deposition in vulnerable regions (forloni2022preventivepharmacologicaltreatment pages 2-3, thune2023geneticvariantsassociated pages 1-2) | GO/pathology labels: neuron death; astrocyte activation; protein aggregation; prion protein amyloid formation; CL: neuron, astrocyte | Human neuropathology; strong |
| Cell types implicated | Disease mechanisms and omics literature implicate neurons and astrocytes; experimental translatome work also highlights GABAergic and glutamatergic neuronal populations (thune2023geneticvariantsassociated pages 6-8, thune2023geneticvariantsassociated pages 8-9) | CL labels: neuron; astrocyte; GABAergic neuron; glutamatergic neuron (IDs for curator verification) | Human omics + animal model/review; moderate |
| Molecular mechanism | Pathogenesis is consistent with prion protein misfolding/conformational conversion leading to selective neurodegeneration, sleep/autonomic network failure, and downstream apoptotic/cellular stress pathways (forloni2022preventivepharmacologicaltreatment pages 2-3, thune2023geneticvariantsassociated pages 1-2, thune2023geneticvariantsassociated pages 6-8) | GO labels: protein misfolding; amyloid fibril formation; programmed cell death; caspase-mediated cleavage; regulation of circadian rhythm | Human genetics/neuropathology + experimental support; moderate-strong |
| Cellular processes | Candidate pathways include programmed cell death, apoptotic cleavage/caspase-mediated processes, proteostasis disruption, cytoskeletal injury, circadian dysregulation, and mitochondrial/ribosomal decline (thune2023geneticvariantsassociated pages 6-8, thune2023geneticvariantsassociated pages 8-9) | GO labels: apoptotic process; caspase-mediated cleavage; cytoskeleton organization; circadian rhythm; mitochondrial organization; ribosome biogenesis/translation | Human WES pathway analysis + animal translatome; moderate |
| Subcellular compartments | Omics/translatome evidence points to mitochondrial and ribosomal/translation machinery abnormalities early in disease-related responses (thune2023geneticvariantsassociated pages 6-8, thune2023geneticvariantsassociated pages 8-9) | GO cellular component labels: mitochondrion; ribosome; cytoskeleton (IDs for curator verification) | Human pathway inference + animal translatome; moderate |
| Proteomics/omics | Human prion-disease brain proteomics found broad terminal-stage protein changes with shared pathways across FFI and other prion diseases, including oxidative phosphorylation, lysosome, protein export, and drug metabolism pathways (context from retrieved literature summarized alongside FFI-specific evidence) (thune2023geneticvariantsassociated pages 1-2) | GO/Pathway labels: oxidative phosphorylation; lysosome; protein export | Human tissue proteomics; limited-direct FFI specificity |
| Diagnostic approach | Diagnosis is centered on clinical syndrome plus confirmatory PRNP testing; in at-risk or symptomatic subjects, longitudinal neurologic exam, neuropsychology, laboratory studies, and polysomnography are used in research/monitoring settings (forloni2022preventivepharmacologicaltreatment pages 3-5, forloni2022preventivepharmacologicaltreatment pages 1-2) | MAXO labels: genetic testing; neurologic examination; neuropsychological assessment; polysomnography; laboratory monitoring | Human clinical trial protocol/review; moderate |
| Biomarkers | Plasma neurofilament light chain is cited as a biomarker in FFI-related literature, but quantitative performance was not available in the retrieved evidence here (thune2023geneticvariantsassociated pages 9-10) | Biomarker label: neurofilament light chain; specimen: plasma | Human biomarker citation in recent literature; limited in current evidence set |
| Imaging/electrophysiology | Sleep studies/polysomnography are important in FFI evaluation; thalamic functional abnormalities are central, but specific sensitivity/specificity values for PSG, EEG, MRI, or FDG-PET were not available in the retrieved evidence here (forloni2022preventivepharmacologicaltreatment pages 3-5) | MAXO labels: polysomnography; electroencephalography; brain MRI; FDG-PET (IDs for curator verification) | Human clinical context; limited-direct quantitative evidence |
| Supportive treatment | No curative therapy is established; care is mainly palliative/supportive, targeting neurologic, sleep, and autonomic complications (forloni2022preventivepharmacologicaltreatment pages 1-2) | MAXO labels: palliative care; supportive care; symptom management; autonomic monitoring | Human clinical/review; strong for absence of cure |
| Investigational drug therapy | Doxycycline has been tested as preventive/repurposed therapy in at-risk carriers due to anti-prion and neuroprotective rationale; 10 D178N carriers received 100 mg/day in the DOXIFF protocol (forloni2022preventivepharmacologicaltreatment pages 2-3, forloni2022preventivepharmacologicaltreatment pages 3-5) | CHEBI/drug label: doxycycline; MAXO labels: preventive pharmacotherapy; oral antibiotic repurposing; clinical trial participation | Human trial protocol + preclinical rationale; moderate |
| Doxycycline trial design | DOXIFF enrolled 10 carriers (ages 44-53) on doxycycline and 15 non-carriers on placebo, with 10-year follow-up and blinded assessments; trial lacked validated surrogate biomarkers and relied on historical comparison (forloni2022preventivepharmacologicaltreatment pages 3-5) | Trial ID: EudraCT 2010-022233-28; MAXO labels: longitudinal surveillance; preventive treatment trial | Human interventional protocol; moderate |
| Current clinical trials | Broader genetic-prion/PRNP-lowering trials now recruiting may be relevant to FFI families, including ION717 (NCT06153966, phase 1/2), PrP-targeting siRNA safety/mechanism study (NCT07444580, phase 1), and observational biomarker/natural-history studies (NCT05124392, NCT05746715, NCT07732608) | ClinicalTrials.gov IDs: NCT06153966; NCT07444580; NCT05124392; NCT05746715; NCT07732608 | Trial registry evidence; strong for existence/status, limited for efficacy |
| Prevention/genetic counseling | For this Mendelian disease, prevention is mainly family-based risk assessment, predictive PRNP testing in appropriate counseling settings, and potential enrollment in surveillance/prevention studies (forloni2022preventivepharmacologicaltreatment pages 3-5, forloni2022preventivepharmacologicaltreatment pages 1-2) | MAXO labels: genetic counseling; predictive genetic testing; cascade testing; clinical surveillance | Human clinical/research practice; moderate |
| Model organisms | Mouse models carrying FFI-associated PRNP mutations and prion-disease translatome systems are used to study selective vulnerability, early cell-type responses, and therapeutic hypotheses, but they may incompletely capture the full human sleep/autonomic syndrome (thune2023geneticvariantsassociated pages 8-9) | Model labels: PRNP D178N/129M knock-in mouse (curator verification needed); CL labels: astrocyte, GABAergic neuron, glutamatergic neuron | Animal model; moderate with translational limitations |
| Evidence gaps | Important gaps in the currently retrieved evidence set: verified ontology numeric IDs; robust prevalence/incidence estimates specific to FFI; test sensitivity/specificity for PSG/EEG/MRI/PET/RT-QuIC in FFI; validated prognostic biomarkers; controlled efficacy data for any disease-modifying therapy; nonhuman natural disease analogs (forloni2022preventivepharmacologicaltreatment pages 1-2, thune2023geneticvariantsassociated pages 8-9, forloni2022preventivepharmacologicaltreatment pages 3-5) | Curator action items: verify MONDO/OMIM/Orphanet/MeSH/ICD IDs; add PMID-linked diagnostic accuracy and epidemiology sources | Evidence synthesis; strong for gap identification |


*Table: This compact table summarizes evidence-backed findings for fatal familial insomnia in a knowledge-base-ready format, including genetics, phenotypes, anatomy, mechanisms, diagnostics, treatment, and evidence gaps. It also flags ontology identifiers that should be curator-verified rather than inferred.*

## Evidence assessment and research gaps

The most robust claims are the D178N-129M causal haplotype, autosomal-dominant inheritance, progressive sleep/autonomic syndrome, selective thalamic degeneration, and rapidly fatal course. Major unresolved areas are FFI-specific incidence and prevalence; validated prodromal biomarkers; quantitative diagnostic performance of PSG, PET, RT-QuIC, and NfL; replication of onset-modifier loci; human single-cell/spatial datasets; and controlled evidence for any disease-modifying treatment. The 2023 WES investigators explicitly characterized their modifier work as a small pilot constrained by rarity, so its candidate genes should not yet influence counseling or clinical decisions. (thune2023geneticvariantsassociated pages 2-4, thune2023geneticvariantsassociated pages 8-9)

### Key recent sources

- Thüne K, et al. **Genetic Variants Associated with the Age of Onset Identified by Whole-Exome Sequencing in Fatal Familial Insomnia.** *Cells*. Published August 2023;12:2053. DOI/URL: https://doi.org/10.3390/cells12162053. Abstract: “We identified nineteen potential gene variants with a potential effect on the age of onset.” PMID was not supplied in the retrieved record. (thune2023geneticvariantsassociated pages 1-2, thune2023geneticvariantsassociated pages 2-4)
- Forloni G, et al. **Preventive pharmacological treatment in subjects at risk for fatal familial insomnia: science and public engagement.** *Prion*. Published June 2022;16:66–77. DOI/URL: https://doi.org/10.1080/19336896.2022.2083435. Abstract: the study “led to a clinical trial based on the repurposing of doxycycline” and included ten mutation carriers and 15 noncarriers. PMID was not supplied in the retrieved record. (forloni2022preventivepharmacologicaltreatment pages 3-5, forloni2022preventivepharmacologicaltreatment pages 1-2)

**Curation caution:** ontology and coding systems change independently of primary literature. OMIM/Orphanet identifiers above should be confirmed at ingestion, and current MONDO, ICD-11, MeSH, HPO, GO, CL, UBERON, CHEBI, and MAXO numeric IDs should be resolved against the knowledge base’s pinned ontology releases.

References

1. (forloni2022preventivepharmacologicaltreatment pages 2-3): Gianluigi Forloni, Ignazio Roiter, Vladimiro Artuso, Manuel Marcon, Walter Colesso, Elviana Luban, Ugo Lucca, Mauro Tettamanti, Elisabetta Pupillo, Veronica Redaelli, Francesco Mariuzzo, Giulia Boscolo Buleghin, Alice Mariuzzo, Fabrizio Tagliavini, Roberto Chiesa, and Anna Ambrosini. Preventive pharmacological treatment in subjects at risk for fatal familial insomnia: science and public engagement. Prion, 16:66-77, Jun 2022. URL: https://doi.org/10.1080/19336896.2022.2083435, doi:10.1080/19336896.2022.2083435. This article has 10 citations and is from a peer-reviewed journal.

2. (thune2023geneticvariantsassociated pages 1-2): Katrin Thüne, Matthias Schmitz, John Wiedenhöft, Orr Shomroni, Stefan Göbel, Timothy Bunck, Neelam Younas, Saima Zafar, Peter Hermann, and Inga Zerr. Genetic variants associated with the age of onset identified by whole-exome sequencing in fatal familial insomnia. Cells, 12:2053, Aug 2023. URL: https://doi.org/10.3390/cells12162053, doi:10.3390/cells12162053. This article has 2 citations.

3. (thune2023geneticvariantsassociated pages 2-4): Katrin Thüne, Matthias Schmitz, John Wiedenhöft, Orr Shomroni, Stefan Göbel, Timothy Bunck, Neelam Younas, Saima Zafar, Peter Hermann, and Inga Zerr. Genetic variants associated with the age of onset identified by whole-exome sequencing in fatal familial insomnia. Cells, 12:2053, Aug 2023. URL: https://doi.org/10.3390/cells12162053, doi:10.3390/cells12162053. This article has 2 citations.

4. (forloni2022preventivepharmacologicaltreatment pages 3-5): Gianluigi Forloni, Ignazio Roiter, Vladimiro Artuso, Manuel Marcon, Walter Colesso, Elviana Luban, Ugo Lucca, Mauro Tettamanti, Elisabetta Pupillo, Veronica Redaelli, Francesco Mariuzzo, Giulia Boscolo Buleghin, Alice Mariuzzo, Fabrizio Tagliavini, Roberto Chiesa, and Anna Ambrosini. Preventive pharmacological treatment in subjects at risk for fatal familial insomnia: science and public engagement. Prion, 16:66-77, Jun 2022. URL: https://doi.org/10.1080/19336896.2022.2083435, doi:10.1080/19336896.2022.2083435. This article has 10 citations and is from a peer-reviewed journal.

5. (thune2023geneticvariantsassociated pages 8-9): Katrin Thüne, Matthias Schmitz, John Wiedenhöft, Orr Shomroni, Stefan Göbel, Timothy Bunck, Neelam Younas, Saima Zafar, Peter Hermann, and Inga Zerr. Genetic variants associated with the age of onset identified by whole-exome sequencing in fatal familial insomnia. Cells, 12:2053, Aug 2023. URL: https://doi.org/10.3390/cells12162053, doi:10.3390/cells12162053. This article has 2 citations.

6. (forloni2022preventivepharmacologicaltreatment pages 1-2): Gianluigi Forloni, Ignazio Roiter, Vladimiro Artuso, Manuel Marcon, Walter Colesso, Elviana Luban, Ugo Lucca, Mauro Tettamanti, Elisabetta Pupillo, Veronica Redaelli, Francesco Mariuzzo, Giulia Boscolo Buleghin, Alice Mariuzzo, Fabrizio Tagliavini, Roberto Chiesa, and Anna Ambrosini. Preventive pharmacological treatment in subjects at risk for fatal familial insomnia: science and public engagement. Prion, 16:66-77, Jun 2022. URL: https://doi.org/10.1080/19336896.2022.2083435, doi:10.1080/19336896.2022.2083435. This article has 10 citations and is from a peer-reviewed journal.

7. (thune2023geneticvariantsassociated pages 6-8): Katrin Thüne, Matthias Schmitz, John Wiedenhöft, Orr Shomroni, Stefan Göbel, Timothy Bunck, Neelam Younas, Saima Zafar, Peter Hermann, and Inga Zerr. Genetic variants associated with the age of onset identified by whole-exome sequencing in fatal familial insomnia. Cells, 12:2053, Aug 2023. URL: https://doi.org/10.3390/cells12162053, doi:10.3390/cells12162053. This article has 2 citations.

8. (thune2023geneticvariantsassociated pages 9-10): Katrin Thüne, Matthias Schmitz, John Wiedenhöft, Orr Shomroni, Stefan Göbel, Timothy Bunck, Neelam Younas, Saima Zafar, Peter Hermann, and Inga Zerr. Genetic variants associated with the age of onset identified by whole-exome sequencing in fatal familial insomnia. Cells, 12:2053, Aug 2023. URL: https://doi.org/10.3390/cells12162053, doi:10.3390/cells12162053. This article has 2 citations.

## Artifacts

- [Edison artifact artifact-00](Fatal_Familial_Insomnia-deep-research-falcon_artifacts/artifact-00.md)