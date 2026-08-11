---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-05T14:50:29.051500'
end_time: '2026-06-05T14:59:02.223744'
duration_seconds: 513.17
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Primary Pigmented Nodular Adrenocortical Disease
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 53
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Primary_Pigmented_Nodular_Adrenocortical_Disease-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Primary Pigmented Nodular Adrenocortical Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Primary Pigmented Nodular Adrenocortical Disease** covering all of the
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
- **Disease Name:** Primary Pigmented Nodular Adrenocortical Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Primary Pigmented Nodular Adrenocortical Disease** covering all of the
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


# Primary Pigmented Nodular Adrenocortical Disease (PPNAD): Disease Characteristics Research Report

**Target disease:** Primary Pigmented Nodular Adrenocortical Disease (PPNAD)  
**Category:** Mendelian adrenal hyperfunction disorder causing ACTH-independent Cushing syndrome  
**MONDO ID / OMIM / Orphanet / MeSH / ICD-10/11:** *Not retrieved with the available tools in this run; requires direct lookup in OMIM/Orphanet/MONDO/MeSH/ICD resources.* (sun2024theclinicalcharacteristics pages 1-2)

## Executive summary (current understanding)
PPNAD is a rare, typically bilateral **micronodular** adrenocortical disease that produces cortisol autonomously (ACTH-independent / pituitary-independent hypercortisolism) and often presents in childhood or young adulthood. It can occur as an isolated condition or as the most common endocrine manifestation of **Carney complex (CNC)**. The dominant mechanistic paradigm is **dysregulated cAMP–PKA signaling** (most often due to **loss-of-function PRKAR1A**), driving autonomous steroidogenesis, abnormal adrenal differentiation, increased proliferation, and resistance to apoptosis; downstream pathway involvement includes **mTORC1** and **Wnt signaling**, with translational hypotheses for targeted therapy (e.g., mTORC1 inhibition; KIT inhibition) supported by experimental models. (sun2024theclinicalcharacteristics pages 1-2, sahutbarnola2010cushingssyndromeand pages 1-2, joussineau2014mtorpathwayis pages 1-2, almeida2012activationofcyclic pages 6-6, nadella2020ckitoncogeneexpression pages 1-3)

---

## 1. Disease information
### 1.1 Definition and overview
*Human clinical / aggregated evidence.*  
PPNAD is a rare cause of endogenous Cushing syndrome (CS) due to **primary adrenal**, **ACTH-independent** cortisol excess. In a 2024 systematic review, PPNAD is described as a rare cause of endogenous CS affecting children and young adults and characterized histologically by multiple pigmented micronodules. (sun2024theclinicalcharacteristics pages 1-2)

A classic transcriptomic study defines PPNAD as: **“another form of bilateral adrenocortical hyperplasia that is often associated with ACTH-independent Cushing’s syndrome and is characterized by small to normal-sized adrenal glands containing multiple small cortical pigmented nodules.”** (PMID not available in tool output; J Clin Endocrinol Metab, Feb 2006; URL: https://doi.org/10.1210/jc.2005-1301) (horvath2006serialanalysisof pages 1-1)

The NIH observational protocol similarly characterizes PPNAD as a **pituitary-independent** primary adrenal hypercortisolism with dexamethasone resistance, loss of diurnal rhythm, and distinctive bilateral histopathology including pigmented nodules and extranodular cortical atrophy. (ClinicalTrials.gov NCT00001452; first posted 1995-12-14; URL: https://clinicaltrials.gov/study/NCT00001452) (NCT00001452 chunk 1)

### 1.2 Synonyms / alternative names
From the 2024 systematic review: **“PPNAD … also termed i-PPNAD, familial isolated PPNAD, isolated PPNAD or micronodular adrenal disease.”** (sun2024theclinicalcharacteristics pages 1-2)

### 1.3 Data provenance
Evidence in this report is derived from:
- **Aggregated disease-level sources:** systematic review of 210 published cases (Sun et al., 2024). (sun2024theclinicalcharacteristics pages 1-2, sun2024theclinicalcharacteristics pages 4-5)
- **Individual patient reports/series:** e.g., PRKACA amplification case report (2024) and a 5-patient case series (2006). (yang2024germlineprkacaamplificationassociated pages 2-4, zhu2006primarypigmentednodular pages 1-2)
- **Experimental models:** adrenal cortex–specific Prkar1a knockout mouse, cell lines, xenografts. (sahutbarnola2010cushingssyndromeand pages 1-2, nadella2020ckitoncogeneexpression pages 1-3, joussineau2014mtorpathwayis pages 1-2)

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause:** Mendelian or mosaic genetic dysregulation of cAMP/PKA signaling leading to autonomous cortisol production via bilateral micronodular adrenal disease (PPNAD). (chevalier2021bilateraladrenalhyperplasia pages 1-3, robinsonwhite2006prkar1amutationsandprotein pages 1-2)

**Major causal/associated genes in recent aggregated evidence (2024):** PRKAR1A, PDE11A, PRKACA, CTNNB1, PDE8B, ARMC5 were reported among genetically tested PPNAD cases, with PRKAR1A predominant. (sun2024theclinicalcharacteristics pages 1-2, sun2024theclinicalcharacteristics pages 4-5)

### 2.2 Risk factors
**Genetic risk factors (causal genes / susceptibility):**
- **PRKAR1A** pathogenic variants (most common in tested PPNAD cases; see Section 4). (sun2024theclinicalcharacteristics pages 1-2, sun2024theclinicalcharacteristics pages 4-5)
- **PDE11A** variants (often co-occurring with PRKAR1A in the 2024 review). (sun2024theclinicalcharacteristics pages 4-5)
- **PRKACA copy-number gain/amplification** reported as a causal event in at least one pediatric case report. (yang2024germlineprkacaamplificationassociated pages 2-4)

**Non-genetic risk factors:** No robust environmental/lifestyle risk factors were identified in the evidence retrieved for this run; PPNAD is primarily genetic. (chevalier2021bilateraladrenalhyperplasia pages 1-3)

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved evidence. (sun2024theclinicalcharacteristics pages 1-2)

### 2.4 Gene–environment interactions
Not established in the retrieved evidence; currently appears primarily genotype-driven. (sun2024theclinicalcharacteristics pages 1-2)

---

## 3. Phenotypes (clinical spectrum)
### 3.1 Core phenotype: ACTH-independent Cushing syndrome / hypercortisolism
**Key features** (HPO suggestions in parentheses):
- Hypercortisolism with loss of circadian rhythm (**Abnormal circulating cortisol concentration** [HP:0008207]; **Abnormality of circadian rhythm** [HP:0001270 as proxy]; **Cushing syndrome** [HP:0000863]). Loss of cortisol rhythm was reported in **98.59% (70/71)** of cases with data in the 2024 systematic review. (sun2024theclinicalcharacteristics pages 4-5)
- Low/undetectable ACTH (**Decreased circulating ACTH level** [no exact HPO term; use **Abnormality of pituitary hormone level** HP:0000851 + ACTH annotation]) reported in **78.57% (77/98)**. (sun2024theclinicalcharacteristics pages 4-5)
- Classical Cushingoid appearance: moon facies, buffalo hump, plethora, violaceous striae (e.g., **Moon facies** [HP:0000270], **Dorsocervical fat pad** [HP:0002775], **Facial plethora** [HP:0031307], **Purple striae** [HP:0001055]). (zhu2006primarypigmentednodular pages 1-2)

**Course:** PPNAD may be mild, subclinical, or cyclic in some cases (not consistently quantified in the retrieved evidence). (NCT00001452 chunk 1)

### 3.2 Skeletal phenotype
- Osteoporosis/osteopenia (**Osteoporosis** [HP:0000939], **Osteopenia** [HP:0012055]) in **94.29% (33/35)** in the 2024 systematic review. (sun2024theclinicalcharacteristics pages 1-2, sun2024theclinicalcharacteristics pages 4-5)

### 3.3 Cardiometabolic phenotype
- Hypertension (**Hypertension** [HP:0000822]) in **67.50% (81/120)**. (sun2024theclinicalcharacteristics pages 4-5)
- Weight gain/obesity (**Weight gain** [HP:0004324], **Obesity** [HP:0001513]) in **59.17% (71/120)**. (sun2024theclinicalcharacteristics pages 4-5)
- Diabetes/impaired glucose tolerance reported in case series and case report (HPO: **Diabetes mellitus** [HP:0000819], **Impaired glucose tolerance** [HP:0001959]). (zhu2006primarypigmentednodular pages 1-2, yang2024germlineprkacaamplificationassociated pages 2-4)

### 3.4 Pigmentary / syndromic features (Carney complex association)
Among PPNAD patients in the 2024 review, **31.43% (66/210)** had concurrent CNC; among these, **71.21% (47/66)** had spotty skin pigmentation (HPO: **Lentigines** [HP:0001003], **Hyperpigmentation** [HP:0000953]). (sun2024theclinicalcharacteristics pages 4-5)

### 3.5 Quality-of-life impact
Direct QoL instrument data (SF-36/EQ-5D/PROMIS) were not identified in the retrieved sources. Clinically, the high frequency of osteoporosis, hypertension, and metabolic disease implies substantial morbidity in untreated hypercortisolism. (sun2024theclinicalcharacteristics pages 4-5)

---

## 4. Genetic / molecular information
### 4.1 Causal genes and inheritance
**Inheritance:** Often autosomal dominant in the context of PRKAR1A-related CNC/PPNAD (tumor-suppressor model with haploinsufficiency/second hit described in reviews). (chevalier2021bilateraladrenalhyperplasia pages 6-7, chevalier2021bilateraladrenalhyperplasia pages 1-3)

**Genes implicated in the 2024 systematic review (151 tested; 132 with pathogenic variants):** PRKAR1A, PDE11A, PRKACA, CTNNB1, PDE8B, ARMC5; **PRKAR1A** was most frequent (79.47%). (sun2024theclinicalcharacteristics pages 1-2, sun2024theclinicalcharacteristics pages 4-5)

**High-yield statistic:** In the 2024 review, genetic testing had **87.42% (132/151)** yield for a pathogenic variant in reported cases. (sun2024theclinicalcharacteristics pages 1-2)

### 4.2 Pathogenic variants and functional classes
- **PRKAR1A loss-of-function:** Reviews describe many PRKAR1A mutations as premature stop codons leading to nonsense-mediated decay and haploinsufficiency; other mutations may generate altered proteins (some degraded; some potentially dominant-negative). (chevalier2021bilateraladrenalhyperplasia pages 6-7)
- **PRKACA amplification (copy-number gain):** A 2024 case report describes germline PRKACA copy-number gain on chr19p13.13p13.12 associated with pediatric-onset PPNAD and CNC features. (yang2024germlineprkacaamplificationassociated pages 1-2, yang2024germlineprkacaamplificationassociated pages 2-4)

**Population allele frequency / gnomAD / ClinVar classifications:** Not retrievable in this run because ClinVar/gnomAD tools were not available.

### 4.3 Genotype–phenotype association
Sun et al. (2024) reports a significant association between **PRKAR1A** pathogenic variants and **spotty skin pigmentation** in CNC with concurrent PPNAD. (sun2024theclinicalcharacteristics pages 1-2, sun2024theclinicalcharacteristics pages 4-5)

---

## 5. Environmental information
No specific environmental toxins, lifestyle exposures, or infectious triggers were identified in the retrieved evidence. Current literature captured here supports PPNAD as primarily a genetic disease driven by cAMP/PKA pathway dysregulation. (chevalier2021bilateraladrenalhyperplasia pages 1-3)

---

## 6. Mechanism / pathophysiology
### 6.1 Core pathway: cAMP–PKA dysregulation (upstream → downstream causal chain)
**Upstream trigger:** Germline inactivating PRKAR1A (PKA regulatory subunit RIα) or other cAMP/PKA pathway alterations. (chevalier2021bilateraladrenalhyperplasia pages 6-7, chevalier2021bilateraladrenalhyperplasia pages 1-3)

**Cellular consequence:** Increased PKA catalytic activity and altered signaling, leading to autonomous cortisol production and adrenal hyperplasia.

**In vivo mechanistic evidence (mouse model):** In adrenal cortex–specific Prkar1a knockout (AdKO) mice, PRKAR1A loss caused increased PKA activity and **pituitary-independent Cushing syndrome**, with autonomous steroidogenic gene expression, deregulated differentiation, increased proliferation, and resistance to apoptosis. The abstract explicitly states: **“AdKO mice develop pituitary-independent Cushing's syndrome with increased PKA activity.”** (PLoS Genet, Jun 2010; URL: https://doi.org/10.1371/journal.pgen.1000980) (sahutbarnola2010cushingssyndromeand pages 1-2)

**Ontology suggestions:**
- GO Biological Process: **cAMP-mediated signaling** (GO:0019933), **protein kinase A signaling** (GO:?), **steroid biosynthetic process** (GO:0006694), **regulation of apoptotic process** (GO:0042981), **cell proliferation** (GO:0008283).
- Cell types (CL): **adrenocortical cell** (use CL term for adrenal cortical cell), **steroidogenic cell**.

### 6.2 mTORC1 activation and apoptosis resistance
A mechanistic study reports that **mTOR pathway is activated by PKA** in adrenocortical cells and contributes to **apoptosis resistance** in PPNAD; BAD phosphorylation is highlighted as a downstream effector, and **rapamycin (mTORC1 inhibitor)** restored apoptosis sensitivity in vivo in the mouse model. (Hum Mol Genet, Oct 2014; URL: https://doi.org/10.1093/hmg/ddu265) (joussineau2014mtorpathwayis pages 1-2)

**Translational implication:** mTORC1 is a candidate therapeutic target for PPNAD when surgery is not optimal (hypothesis supported by mechanistic in vivo work). (joussineau2014mtorpathwayis pages 1-2)

### 6.3 KIT/SCF as a potential therapeutic axis
In PRKAR1A-mutant PPNAD tissue, **c-KIT** and **SCF** are upregulated in certain nodular areas; in vitro, PRKAR1A deficiency and forskolin-induced cAMP signaling increased c-KIT expression, and PRKACA knockdown reduced it. KIT inhibition with **imatinib** reduced growth and induced apoptosis in a PRKAR1A-deficient adrenocortical cell line and inhibited growth in xenografts. (Endocr Relat Cancer, Oct 2020; URL: https://doi.org/10.1530/erc-20-0270) (nadella2020ckitoncogeneexpression pages 1-3)

### 6.4 Wnt/cell-cycle programs downstream of PRKAR1A defects
Transcriptomic/pathway analyses in PRKAR1A-mutant adrenal lesions show overexpression of Wnt pathway genes (e.g., CCND1, CTNNB1, LEF1, LRP5) and cell-cycle regulators, supporting Wnt-linked proliferative programs downstream of cAMP/PKA activation in PPNAD. (J Clin Endocrinol Metab, Apr 2012; URL: https://doi.org/10.1210/jc.2011-3000) (almeida2012activationofcyclic pages 6-6)

**Omics datapoint (SAGE):** The 2006 SAGE study reported increased expression in PPNAD of steroidogenesis-related genes including **steroidogenic acute regulator** and steroidogenic enzymes **CYP17A1** and **CYP21A2**. (URL: https://doi.org/10.1210/jc.2005-1301) (horvath2006serialanalysisof pages 1-1)

---

## 7. Anatomical structures affected
### 7.1 Primary organ
- **Adrenal cortex (bilateral)** (UBERON suggestion: adrenal gland UBERON:0002369; adrenal cortex subregion). PPNAD is characterized by multiple small pigmented nodules with extranodular cortical atrophy. (sun2024theclinicalcharacteristics pages 1-2, NCT00001452 chunk 1)

### 7.2 Secondary system involvement (complications of hypercortisolism)
- Skeletal system: osteoporosis/osteopenia. (sun2024theclinicalcharacteristics pages 4-5)
- Cardiovascular/metabolic systems: hypertension, diabetes/metabolic syndrome features. (sun2024theclinicalcharacteristics pages 4-5, zhu2006primarypigmentednodular pages 1-2)

### 7.3 Subcellular/cellular compartments
Not specifically described in retrieved evidence; however, pathway data imply cytosolic/nuclear PKA signaling and mTORC1 signaling complexes (GO Cellular Component suggestions: **cytosol**, **nucleus**, **mTOR complex 1**).

---

## 8. Temporal development
- Typical onset: childhood to young adulthood; in Sun et al. 2024, **71.88%** were 10–30 years. (sun2024theclinicalcharacteristics pages 4-5)
- Course: can be prolonged and misdiagnosed; diagnostic difficulty emphasized in systematic review and NIH protocol. (sun2024theclinicalcharacteristics pages 1-2, NCT00001452 chunk 1)

---

## 9. Inheritance and population
### 9.1 Epidemiology
Precise prevalence/incidence estimates were not identified in the retrieved sources.

A 2006 clinical review/case series stated PPNAD accounts for **~0.6%–1.9% of all Cushing syndrome** (statement within that article’s text; not independently validated here). (Chinese Medical Journal, May 2006; URL: https://doi.org/10.1097/00029330-200605010-00015) (zhu2006primarypigmentednodular pages 2-4)

### 9.2 Demographics (from 2024 systematic review)
Median age 22; female:male 2:1. (sun2024theclinicalcharacteristics pages 1-2)

---

## 10. Diagnostics
### 10.1 Clinical and laboratory tests
Key biochemical findings:
- Elevated cortisol with **loss of circadian rhythm** (98.59% where reported). (sun2024theclinicalcharacteristics pages 4-5)
- Low/undetectable ACTH (78.57% where reported). (sun2024theclinicalcharacteristics pages 4-5)

**Paradoxical / absent dexamethasone suppression:** In the 2024 systematic review, **31/31 (100%)** with reported testing had no suppression or paradoxical increase on high-dose dexamethasone/Liddle-type testing. (sun2024theclinicalcharacteristics pages 4-5)

Example case report wording: **“LDDST and HDDST revealed that the patient’s UFC level was not inhibited… indicating a paradoxical increase.”** (Archives Endocrinol Metab, Jan 2024; URL: https://doi.org/10.20945/2359-4292-2022-0491) (yang2024germlineprkacaamplificationassociated pages 2-4)

### 10.2 Imaging
Imaging may be subtle; small bilateral nodules may be seen on MRI/CT in some cases (e.g., “multiple small adrenal nodules” in a CNC case report; bilateral thickening/nodular change ~10 mm in PRKACA amplification case). (yang2024germlineprkacaamplificationassociated pages 2-4)

### 10.3 Pathology
2024 systematic review/WHO 2022-oriented description: multiple beaded pigmented micronodules (<10 mm, often 2–5 mm), CYP11B1 positivity confirming cortisol production, and inter-nodular cortical atrophy. (sun2024theclinicalcharacteristics pages 1-2)

NIH protocol: pigmented nodular adenomas with loss of normal zonation and extranodular cortical atrophy. (NCT00001452 chunk 1)

### 10.4 Genetic testing strategy
Given high yield in the systematic review (87.42% of tested patients), Sun et al. recommend considering **genetic testing prior to surgery** due to diagnostic difficulty and syndromic implications (CNC surveillance). (sun2024theclinicalcharacteristics pages 1-2)

### 10.5 Differential diagnosis
Not comprehensively extracted in this run; key differentiations include other causes of ACTH-independent Cushing syndrome (e.g., cortisol-producing adenoma; PBMAH) and ACTH-dependent Cushing disease. (NCT00001452 chunk 1)

---

## 11. Outcome / prognosis
- Long-term outcome statistics (survival, mortality, QoL scores) were not identified in the retrieved evidence.
- The NIH protocol emphasizes the need to “establish prognosis for carriers/affected individuals,” highlighting that natural history is an ongoing research aim. (NCT00001452 chunk 1)

Complications expected from chronic hypercortisolism include osteoporosis, hypertension, diabetes, and thromboembolic risk in CNC due to myxomas; embolism rates are discussed in the 2024 review in the context of recurrent myxomas (not PPNAD-specific mortality). (sun2024theclinicalcharacteristics pages 11-12)

---

## 12. Treatment
### 12.1 Surgical (real-world implementation)
Surgery is the dominant real-world definitive therapy for cortisol excess.

In Sun et al. 2024 (patients with reported surgery data, n=122):
- Bilateral adrenalectomy: **50.82% (62/122)**
- Unilateral adrenalectomy: **33.61% (41/122)**
- Two-stage bilateral adrenalectomy: **12.30% (15/122)**

Unilateral adrenalectomy was discussed as an option in selected patients (including fertility considerations), but some unilateral cases required completion because hypercortisolism persisted/returned. (sun2024theclinicalcharacteristics pages 4-5, sun2024theclinicalcharacteristics pages 12-14)

**MAXO suggestions:** adrenalectomy (MAXO term for adrenalectomy), unilateral adrenalectomy, bilateral adrenalectomy.

### 12.2 Pharmacotherapy for hypercortisolism (bridging or recurrence)
Sun et al. list steroidogenesis inhibitors used in persistent/recurrent hypercortisolism: **ketoconazole, metyrapone, mitotane, trilostane**, and note **fluconazole** proposed as a safer alternative to ketoconazole in some contexts. (sun2024theclinicalcharacteristics pages 11-12)

**MAXO suggestions:** pharmacological inhibition of steroid biosynthesis; glucocorticoid replacement therapy (post-bilateral adrenalectomy).

### 12.3 Targeted/experimental therapeutics (mechanism-informed)
- **mTORC1 inhibition (rapamycin):** restored apoptosis sensitivity in vivo in a mouse model, supporting mTORC1 as a candidate target. (joussineau2014mtorpathwayis pages 1-2)
- **KIT inhibition (imatinib):** reduced growth and induced apoptosis in PRKAR1A-deficient adrenocortical cells and inhibited xenograft growth. (nadella2020ckitoncogeneexpression pages 1-3)

These are not established standard-of-care treatments for PPNAD but represent translational directions grounded in mechanistic evidence.

### 12.4 Clinical trials
No interventional trials specific to PPNAD were identified in the retrieved clinical trial set; however, an NIH cohort study focused on PPNAD/CNC genetics and natural history enrolled **1,387** participants (NCT00001452; initiated 1995-12-14). (NCT00001452 chunk 1)

---

## 13. Prevention
Primary prevention is not currently established because PPNAD is primarily genetic.

**Secondary prevention / early detection:** Genetic counseling and cascade testing in families with PRKAR1A-related disease and surveillance for CNC manifestations are supported conceptually; the NIH protocol notes that “there are no standardized screening tests” for family members at present (historical context, 1995 protocol). (NCT00001452 chunk 1)

---

## 14. Other species / natural disease
No naturally occurring veterinary/other-species PPNAD analogs were identified in the retrieved evidence.

---

## 15. Model organisms
**Adrenal cortex–specific Prkar1a knockout mouse (AdKO):** recapitulates key human features (ACTH-independent Cushing syndrome, bilateral adrenal hyperplasia) and provides in vivo evidence that PRKAR1A loss is sufficient for PPNAD-like disease. (PLoS Genet, Jun 2010; https://doi.org/10.1371/journal.pgen.1000980) (sahutbarnola2010cushingssyndromeand pages 1-2)

**Mechanism-focused mouse work:** AdKO model used to show PKA→mTORC1 activation contributing to apoptosis resistance; rapamycin reversed apoptosis resistance in vivo. (joussineau2014mtorpathwayis pages 1-2)

**Cellular/xenograft systems:** PRKAR1A-deficient adrenocortical cell lines (e.g., CAR47) and H295 xenografts used to test KIT inhibition (imatinib). (nadella2020ckitoncogeneexpression pages 1-3)

---

## Recent developments (prioritizing 2023–2024)
1) **Largest recent synthesis of clinical/genetic data:** Systematic review of **210** PPNAD patients (Jun 2024) quantifying phenotype frequencies, gene frequencies, and surgical patterns; highlights diagnostic yield of genetic testing and pregnancy/fertility considerations for unilateral adrenalectomy. (https://doi.org/10.3389/fendo.2024.1356870; Jun 2024) (sun2024theclinicalcharacteristics pages 1-2, sun2024theclinicalcharacteristics pages 4-5)

2) **PRKACA copy-number gain as a causal mechanism:** 2024 case report describing germline PRKACA amplification-associated PPNAD with paradoxical dexamethasone response and micronodular pathology; reinforces expansion of genetic causes beyond PRKAR1A. (https://doi.org/10.20945/2359-4292-2022-0491; Jan 2024) (yang2024germlineprkacaamplificationassociated pages 2-4)

---

## Key quantitative evidence table (Sun et al., 2024)
| Domain | Variable | Numerator/Denominator | Frequency / Value | Notes |
|---|---|---:|---:|---|
| Cohort | Total patients included | 210/210 | 210 patients | Systematic review cohort size; median age 22 years (Sun et al., *Frontiers in Endocrinology*, Jun 2024, https://doi.org/10.3389/fendo.2024.1356870) (sun2024theclinicalcharacteristics pages 1-2) |
| Demographics | Female:male ratio | — | 2:1 | Female predominance in pooled cohort; most patients were 10–30 years old (71.88%) (Sun et al., Jun 2024, DOI above) (sun2024theclinicalcharacteristics pages 1-2, sun2024theclinicalcharacteristics pages 4-5) |
| Demographics | Age distribution 10–30 years | — | 71.88% | Majority presented in adolescence/young adulthood (Sun et al., Jun 2024, https://doi.org/10.3389/fendo.2024.1356870) (sun2024theclinicalcharacteristics pages 4-5) |
| Carney complex association | Concurrent Carney complex (CNC) | 66/210 | 31.43% | cPPNAD/CNC subset in pooled review (Sun et al., Jun 2024, DOI above) (sun2024theclinicalcharacteristics pages 1-2, sun2024theclinicalcharacteristics pages 4-5) |
| CNC phenotype | Spotty skin pigmentation among cPPNAD/CNC | 47/66 | 71.21% | Pigmentary findings common in CNC-associated cases; supports PRKAR1A testing consideration (Sun et al., Jun 2024, DOI above) (sun2024theclinicalcharacteristics pages 4-5, sun2024theclinicalcharacteristics pages 12-14) |
| CNC phenotype | Cardiac or cutaneous myxoma among cPPNAD/CNC | 19/66 | 28.79% | Relevant for surveillance due to embolic risk in CNC (Sun et al., Jun 2024, DOI above) (sun2024theclinicalcharacteristics pages 11-12) |
| Major phenotype | Osteoporosis / osteopenia | 33/35 | 94.29% | One of the most frequent reported morbidity features (Sun et al., Jun 2024, https://doi.org/10.3389/fendo.2024.1356870) (sun2024theclinicalcharacteristics pages 1-2, sun2024theclinicalcharacteristics pages 4-5) |
| Major phenotype | Hypertension | 81/120 | 67.50% | Common hypercortisolism-related comorbidity (Sun et al., Jun 2024, DOI above) (sun2024theclinicalcharacteristics pages 4-5) |
| Major phenotype | Weight gain | 71/120 | 59.17% | Typical Cushing syndrome manifestation in pooled cases (Sun et al., Jun 2024, DOI above) (sun2024theclinicalcharacteristics pages 4-5) |
| Diagnostic laboratory | Loss of cortisol circadian rhythm | 70/71 | 98.59% | Strong biochemical hallmark of hypercortisolism (Sun et al., Jun 2024, https://doi.org/10.3389/fendo.2024.1356870) (sun2024theclinicalcharacteristics pages 4-5) |
| Diagnostic laboratory | Low/undetectable ACTH | 77/98 | 78.57% | Consistent with ACTH-independent Cushing syndrome (Sun et al., Jun 2024, DOI above) (sun2024theclinicalcharacteristics pages 4-5) |
| Diagnostic laboratory | Plasma cortisol not suppressed on dexamethasone testing | 31/31 | 100% | Included paradoxical or absent suppression on low-/high-dose dexamethasone/Liddle-type testing (Sun et al., Jun 2024, DOI above) (sun2024theclinicalcharacteristics pages 4-5) |
| Genetics | Patients undergoing genetic testing | 151/210 | 71.90% | Not all published cases had molecular testing (Sun et al., Jun 2024, https://doi.org/10.3389/fendo.2024.1356870) (sun2024theclinicalcharacteristics pages 1-2, sun2024theclinicalcharacteristics pages 12-14) |
| Genetics | Any pathogenic variant detected | 132/151 | 87.42% | High diagnostic yield in tested cases (Sun et al., Jun 2024, DOI above) (sun2024theclinicalcharacteristics pages 1-2, sun2024theclinicalcharacteristics pages 4-5) |
| Genetics | Genes reported in cohort | — | 6 genes | PRKAR1A, PDE11A, PRKACA, CTNNB1, PDE8B, ARMC5 (Sun et al., Jun 2024, DOI above) (sun2024theclinicalcharacteristics pages 1-2, sun2024theclinicalcharacteristics pages 4-5) |
| Genetics | PRKAR1A pathogenic variants | 120/151 | 79.47% | Most common implicated gene in tested patients (Sun et al., Jun 2024, https://doi.org/10.3389/fendo.2024.1356870) (sun2024theclinicalcharacteristics pages 1-2, sun2024theclinicalcharacteristics pages 4-5) |
| Genetics | PDE11A variants | 40/151 | 26.49% | Some patients carried PDE11A along with PRKAR1A (Sun et al., Jun 2024, DOI above) (sun2024theclinicalcharacteristics pages 4-5) |
| Genetics | PRKAR1A + PDE11A co-occurrence | 33/151 | 21.85% | Reported overlap among genetically tested cases (Sun et al., Jun 2024, DOI above) (sun2024theclinicalcharacteristics pages 4-5) |
| Genotype-phenotype | Spotty pigmentation with PRKAR1A variant among evaluable CNC cases | 33/45 | 73.33% | Significant association reported between PRKAR1A and spotty skin pigmentation in CNC with PPNAD (Sun et al., Jun 2024, DOI above) (sun2024theclinicalcharacteristics pages 1-2, sun2024theclinicalcharacteristics pages 4-5) |
| Surgery | Any surgery data available | 122/210 | 58.10% | Surgical approach reported for subset of pooled cases (Sun et al., Jun 2024, https://doi.org/10.3389/fendo.2024.1356870) (sun2024theclinicalcharacteristics pages 4-5) |
| Surgery | Bilateral adrenalectomy | 62/122 | 50.82% | Most common surgical treatment in reported cases (Sun et al., Jun 2024, DOI above) (sun2024theclinicalcharacteristics pages 4-5) |
| Surgery | Unilateral adrenalectomy | 41/122 | 33.61% | Considered in selected patients; review discusses fertility/pregnancy considerations (Sun et al., Jun 2024, DOI above) (sun2024theclinicalcharacteristics pages 4-5, sun2024theclinicalcharacteristics pages 12-14) |
| Surgery | Two-stage bilateral adrenalectomy | 15/122 | 12.30% | Often reflects completion adrenalectomy after initial unilateral approach (Sun et al., Jun 2024, DOI above) (sun2024theclinicalcharacteristics pages 4-5) |


*Table: This table compiles the main quantitative findings from Sun et al. 2024’s systematic review of 210 PPNAD patients, including demographics, phenotype frequencies, diagnostic findings, genetic results, and surgery patterns. It is useful as a concise evidence summary for knowledge-base curation and clinical overview.*

References

1. (sun2024theclinicalcharacteristics pages 1-2): Julian Sun, Lin Ding, Liping He, Hang Fu, Rui Li, Jing Feng, Jianjun Dong, and Lin Liao. The clinical characteristics and pathogenic variants of primary pigmented nodular adrenocortical disease in 210 patients: a systematic review. Frontiers in Endocrinology, Jun 2024. URL: https://doi.org/10.3389/fendo.2024.1356870, doi:10.3389/fendo.2024.1356870. This article has 12 citations.

2. (sahutbarnola2010cushingssyndromeand pages 1-2): Isabelle Sahut-Barnola, Cyrille de Joussineau, Pierre Val, Sarah Lambert-Langlais, Christelle Damon, Anne-Marie Lefrançois-Martinez, Jean-Christophe Pointud, Geoffroy Marceau, Vincent Sapin, Frédérique Tissier, Bruno Ragazzon, Jérôme Bertherat, Lawrence S. Kirschner, Constantine A. Stratakis, and Antoine Martinez. Cushing's syndrome and fetal features resurgence in adrenal cortex–specific prkar1a knockout mice. PLoS Genetics, 6:e1000980, Jun 2010. URL: https://doi.org/10.1371/journal.pgen.1000980, doi:10.1371/journal.pgen.1000980. This article has 128 citations and is from a domain leading peer-reviewed journal.

3. (joussineau2014mtorpathwayis pages 1-2): Cyrille de Joussineau, Isabelle Sahut-Barnola, Frédérique Tissier, Typhanie Dumontet, Coralie Drelon, Marie Batisse-Lignier, Igor Tauveron, Jean-Christophe Pointud, Anne-Marie Lefrançois-Martinez, Constantine A. Stratakis, Jérôme Bertherat, Pierre Val, and Antoine Martinez. Mtor pathway is activated by pka in adrenocortical cells and participates in vivo to apoptosis resistance in primary pigmented nodular adrenocortical disease (ppnad). Human molecular genetics, 23 20:5418-28, Oct 2014. URL: https://doi.org/10.1093/hmg/ddu265, doi:10.1093/hmg/ddu265. This article has 48 citations and is from a domain leading peer-reviewed journal.

4. (almeida2012activationofcyclic pages 6-6): Madson Q. Almeida, Monalisa F. Azevedo, Paraskevi Xekouki, Eirini I. Bimpaki, Anelia Horvath, Michael T. Collins, Lefkothea P. Karaviti, George S. Jeha, Nisan Bhattacharyya, Chris Cheadle, Tonya Watkins, Isabelle Bourdeau, Maria Nesterova, and Constantine A. Stratakis. Activation of cyclic amp signaling leads to different pathway alterations in lesions of the adrenal cortex caused by germline prkar1a defects versus those due to somatic gnas mutations. The Journal of Clinical Endocrinology &amp; Metabolism, 97:E687-E693, Apr 2012. URL: https://doi.org/10.1210/jc.2011-3000, doi:10.1210/jc.2011-3000. This article has 71 citations.

5. (nadella2020ckitoncogeneexpression pages 1-3): Kiran Nadella, Fabio R Faucz, and Constantine A Stratakis. C-kit oncogene expression in prkar1a-mutant adrenal cortex. Oct 2020. URL: https://doi.org/10.1530/erc-20-0270, doi:10.1530/erc-20-0270. This article has 1 citations and is from a domain leading peer-reviewed journal.

6. (horvath2006serialanalysisof pages 1-1): Anelia Horvath, Ludmila Mathyakina, Queenie Vong, Vanessa Baxendale, Alan L. Y. Pang, Wai-Yee Chan, and Constantine A. Stratakis. Serial analysis of gene expression in adrenocortical hyperplasia caused by a germline prkar1a mutation. The Journal of clinical endocrinology and metabolism, 91 2:584-96, Feb 2006. URL: https://doi.org/10.1210/jc.2005-1301, doi:10.1210/jc.2005-1301. This article has 71 citations.

7. (NCT00001452 chunk 1):  Defining the Genetic Basis for the Development of Primary Pigmented Nodular Adrenocortical Disease (PPNAD) and the Carney Complex. Eunice Kennedy Shriver National Institute of Child Health and Human Development (NICHD). 1995. ClinicalTrials.gov Identifier: NCT00001452

8. (sun2024theclinicalcharacteristics pages 4-5): Julian Sun, Lin Ding, Liping He, Hang Fu, Rui Li, Jing Feng, Jianjun Dong, and Lin Liao. The clinical characteristics and pathogenic variants of primary pigmented nodular adrenocortical disease in 210 patients: a systematic review. Frontiers in Endocrinology, Jun 2024. URL: https://doi.org/10.3389/fendo.2024.1356870, doi:10.3389/fendo.2024.1356870. This article has 12 citations.

9. (yang2024germlineprkacaamplificationassociated pages 2-4): Wang-Rong Yang, Xing-Huan Liang, Ying-Fen Qin, Hai-Yan Yang, Shu-Zhan He, Zhen-Xing Huang, Yu-Ping Liu, and Zuo-Jie Luo. Germline prkaca amplification-associated primary pigmented nodular adrenocortical disease: a case report and literature review. Archives of Endocrinology and Metabolism, Jan 2024. URL: https://doi.org/10.20945/2359-4292-2022-0491, doi:10.20945/2359-4292-2022-0491. This article has 8 citations.

10. (zhu2006primarypigmentednodular pages 1-2): Yu ZHU, Yu-xuan WU, Wen-bin RUI, Ding-yi LIU, Wen-long ZHOU, Rong-ming ZHANG, Fu-kang SUN, Chong-yu ZHANG, and Zhou-jun SHEN. Primary pigmented nodular adrenocortical disease. Chinese Medical Journal, 119(9):782-785, May 2006. URL: https://doi.org/10.1097/00029330-200605010-00015, doi:10.1097/00029330-200605010-00015. This article has 2 citations and is from a peer-reviewed journal.

11. (chevalier2021bilateraladrenalhyperplasia pages 1-3): Benjamin Chevalier, Marie-Christine Vantyghem, and Stéphanie Espiard. Bilateral adrenal hyperplasia: pathogenesis and treatment. Biomedicines, 9:1397, Oct 2021. URL: https://doi.org/10.3390/biomedicines9101397, doi:10.3390/biomedicines9101397. This article has 35 citations.

12. (robinsonwhite2006prkar1amutationsandprotein pages 1-2): Audrey Robinson-White, Elise Meoli, Sotirios Stergiopoulos, Anelia Horvath, Sosipatros Boikos, Ioannis Bossis, and Constantine A. Stratakis. <i>prkar1a</i>mutations and protein kinase a interactions with other signaling pathways in the adrenal cortex. The Journal of Clinical Endocrinology &amp; Metabolism, 91:2380-2388, Jun 2006. URL: https://doi.org/10.1210/jc.2006-0188, doi:10.1210/jc.2006-0188. This article has 83 citations.

13. (chevalier2021bilateraladrenalhyperplasia pages 6-7): Benjamin Chevalier, Marie-Christine Vantyghem, and Stéphanie Espiard. Bilateral adrenal hyperplasia: pathogenesis and treatment. Biomedicines, 9:1397, Oct 2021. URL: https://doi.org/10.3390/biomedicines9101397, doi:10.3390/biomedicines9101397. This article has 35 citations.

14. (yang2024germlineprkacaamplificationassociated pages 1-2): Wang-Rong Yang, Xing-Huan Liang, Ying-Fen Qin, Hai-Yan Yang, Shu-Zhan He, Zhen-Xing Huang, Yu-Ping Liu, and Zuo-Jie Luo. Germline prkaca amplification-associated primary pigmented nodular adrenocortical disease: a case report and literature review. Archives of Endocrinology and Metabolism, Jan 2024. URL: https://doi.org/10.20945/2359-4292-2022-0491, doi:10.20945/2359-4292-2022-0491. This article has 8 citations.

15. (zhu2006primarypigmentednodular pages 2-4): Yu ZHU, Yu-xuan WU, Wen-bin RUI, Ding-yi LIU, Wen-long ZHOU, Rong-ming ZHANG, Fu-kang SUN, Chong-yu ZHANG, and Zhou-jun SHEN. Primary pigmented nodular adrenocortical disease. Chinese Medical Journal, 119(9):782-785, May 2006. URL: https://doi.org/10.1097/00029330-200605010-00015, doi:10.1097/00029330-200605010-00015. This article has 2 citations and is from a peer-reviewed journal.

16. (sun2024theclinicalcharacteristics pages 11-12): Julian Sun, Lin Ding, Liping He, Hang Fu, Rui Li, Jing Feng, Jianjun Dong, and Lin Liao. The clinical characteristics and pathogenic variants of primary pigmented nodular adrenocortical disease in 210 patients: a systematic review. Frontiers in Endocrinology, Jun 2024. URL: https://doi.org/10.3389/fendo.2024.1356870, doi:10.3389/fendo.2024.1356870. This article has 12 citations.

17. (sun2024theclinicalcharacteristics pages 12-14): Julian Sun, Lin Ding, Liping He, Hang Fu, Rui Li, Jing Feng, Jianjun Dong, and Lin Liao. The clinical characteristics and pathogenic variants of primary pigmented nodular adrenocortical disease in 210 patients: a systematic review. Frontiers in Endocrinology, Jun 2024. URL: https://doi.org/10.3389/fendo.2024.1356870, doi:10.3389/fendo.2024.1356870. This article has 12 citations.

## Artifacts

- [Edison artifact artifact-00](Primary_Pigmented_Nodular_Adrenocortical_Disease-deep-research-falcon_artifacts/artifact-00.md)