---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T00:04:22.713674'
end_time: '2026-07-31T00:16:10.247344'
duration_seconds: 707.53
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Immunoskeletal Dysplasia with Neurodevelopmental Abnormalities
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 20
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Immunoskeletal_Dysplasia_with_Neurodevelopmental_Abnormalities-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunoskeletal Dysplasia with Neurodevelopmental Abnormalities
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunoskeletal Dysplasia with Neurodevelopmental Abnormalities** covering all of the
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
- **Disease Name:** Immunoskeletal Dysplasia with Neurodevelopmental Abnormalities
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunoskeletal Dysplasia with Neurodevelopmental Abnormalities** covering all of the
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


# Immunoskeletal Dysplasia with Neurodevelopmental Abnormalities

## Executive summary

Immunoskeletal dysplasia with neurodevelopmental abnormalities (ISDNA) is an ultra-rare, congenital, autosomal-recessive disorder caused by biallelic **EXTL3** variants. It is best understood as a heparan-sulfate biosynthesis disorder combining spondyloepimetaphyseal dysplasia, neurodevelopmental impairment, and variably severe—sometimes fatal—T-cell immunodeficiency. Published manifestations range from relatively mild T-cell lymphopenia and developmental delay to Omenn-like severe combined immunodeficiency (SCID), profound skeletal disease, cervical cord compression, and death during infancy. The 2023 skeletal-disorder nosology favors gene-linked terminology such as **EXTL3-related/EXTL3-deficient spondyloepimetaphyseal dysplasia**. As of the searched literature through 2024, there is no disease-modifying therapy or disease-specific clinical trial; care is individualized and multidisciplinary. (bajaj2022anultrararecase pages 2-4, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6, unger2023nosologyofgenetic pages 29-30)

The following table provides an ontology-oriented synopsis; mappings marked “suggested” require validation against the current ontology release.

| domain | high-confidence finding/statistic | suggested ontology terms/IDs | evidence type |
|---|---|---|---|
| Disease identity | EXTL3-related immunoskeletal dysplasia with neurodevelopmental abnormalities; ultra-rare Mendelian disorder; preferred disease entity linked to EXTL3 | MONDO:0044312; OMIM:617425; suggested synonym mappings: “ISDNA”, “SEMD with immune deficiency, EXTL3 type”, “EXTL3 deficiency” (suggested) | Aggregated disease resource + expert nosology + primary human (OpenTargets Search: Immunoskeletal dysplasia with neurodevelopmental abnormalities, bajaj2022anultrararecase pages 2-4, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6, unger2023nosologyofgenetic pages 29-30) |
| Causal gene | Biallelic pathogenic variants in EXTL3 (exostosin like glycosyltransferase 3) cause disease | EXTL3; suggested HGNC mapping: EXTL3 / exostosin-like glycosyltransferase 3 | Human genetics + disease-target evidence (OpenTargets Search: Immunoskeletal dysplasia with neurodevelopmental abnormalities, bajaj2022anultrararecase pages 2-4, stefano2017extl3mutationscause pages 3-5) |
| Inheritance | Autosomal recessive; several families reported with consanguinity; parents heterozygous in informative families | HP:0000007 Autosomal recessive inheritance | Primary human (bajaj2022anultrararecase pages 2-4, stefano2017extl3mutationscause pages 1-3, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 3-4) |
| Reported pathogenic variant set | Six missense alleles summarized in the literature through 2021-2022: c.953C>T p.Pro318Leu; c.1015C>T p.Arg339Trp; c.1382C>T p.Pro461Leu; c.1537C>T; c.1970A>G; c.2008T>G; all reported variants in early cohorts were missense and concentrated in exon 3 in several reports | Suggested Sequence Ontology class: missense_variant; ACMG classes reported as pathogenic/likely pathogenic in case literature (suggested) | Primary human + review synthesis (bajaj2022anultrararecase pages 2-4, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 3-4) |
| Epidemiology | Extremely rare; 14 patients from 9 unrelated families summarized in 2021, and the 2022 Indian report described the 15th published patient | ORPHA/ICD not confirmed from retrieved sources; frequency not established | Review of published cases + case report (bajaj2022anultrararecase pages 2-4, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3) |
| Skeletal phenotype | Core skeletal pattern: disproportionate short stature/short-limb dwarfism, platyspondyly, brachydactyly, epiphyseal/metaphyseal abnormalities; platyspondyly is the most consistently emphasized feature | HP:0001511 Short stature; HP:0001156 Brachydactyly; HP:0000926 Platyspondyly; suggested HPO: short limbs, epiphyseal dysplasia, metaphyseal dysplasia, kyphoscoliosis | Primary human + review (bajaj2022anultrararecase pages 2-4, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6, bajaj2022anultrararecase pages 1-2, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3) |
| Craniovertebral/cervical phenotype | Odontoid hypoplasia, cervical instability/canal stenosis, craniovertebral junction compression are recurrent and clinically actionable; cervical complications required neurosurgical intervention in multiple patients | Suggested HPO: odontoid hypoplasia, cervical vertebral instability, spinal canal stenosis, spinal cord compression; UBERON suggested: cervical vertebral column, spinal cord | Primary human + long-term follow-up (bajaj2022anultrararecase pages 2-4, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 6-7, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3) |
| Pelvic/hip radiology | Trident-shaped acetabula, coxa valga, acetabular dysplasia, hip subluxation/dislocation, open iliac wings/narrow sacro-ischiatic notches reported | Suggested HPO: coxa valga, acetabular dysplasia, hip dislocation; UBERON suggested: pelvis, acetabulum, femur | Primary human radiology (stefano2017extl3mutationscause pages 3-5, stefano2017extl3mutationscause pages 1-3, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3) |
| Craniofacial phenotype | Coarse facial features/facial dysmorphism common: full cheeks/lips, broad or bulbous nasal tip, depressed/prominent nasal bridge, frontal bossing, micrognathia, dysmorphic facies | HP:0001999 Facial asymmetry not established; suggested HPO: Coarse facial features, Full cheeks, Bulbous nose, Depressed nasal bridge, Frontal bossing, Micrognathia | Primary human + review (bajaj2022anultrararecase pages 2-4, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3) |
| Neurologic/neurodevelopmental phenotype | Global developmental delay, motor delay, hypotonia/truncal hypotonia, intellectual disability or borderline cognition; seizures in severe cases; corpus callosum thinning reported in one long-term follow-up case | HP:0001263 Global developmental delay; HP:0001252 Hypotonia; HP:0001249 Intellectual disability; HP:0001250 Seizure; suggested HPO: thinning of corpus callosum | Primary human (bajaj2022anultrararecase pages 2-4, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6, bajaj2022anultrararecase pages 1-2, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3) |
| Immune phenotype | Variable but often T-cell predominant immune deficiency; among published cases summarized in 2021-2022, 9/14 had T-cell lymphopenia/immunodeficiency; Omenn-like SCID reported in 4/14; one oral candidiasis case; recurrent severe infections contributed to early deaths | Suggested HPO: T-cell lymphopenia, Severe combined immunodeficiency, Omenn syndrome, Recurrent infections, Oral candidiasis, Hypogammaglobulinemia, Elevated IgE, Eosinophilia | Primary human + review (bajaj2022anultrararecase pages 2-4, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6, stefano2017extl3mutationscause pages 1-3, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 6-7, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 3-4) |
| Immune laboratory findings | T−NK+B+ or T−B+NK+ profiles reported; reduced T-cell subsets, low/absent TRECs, impaired mitogen responses, reduced IL-2/IL-7-induced STAT5 phosphorylation; hypogammaglobulinemia and hyper-IgE present in subsets | Suggested terms: SCID immunophenotype; GO: STAT5 phosphorylation; CL suggested: T cell, NK cell, B cell, thymic epithelial cell, hematopoietic progenitor cell | Primary human + functional assays (stefano2017extl3mutationscause pages 3-5, stefano2017extl3mutationscause pages 1-3, stefano2017extl3mutationscause pages 7-9, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 3-4) |
| Respiratory/airway phenotype | Laryngotracheal narrowing reported; progressive kyphoscoliosis caused restrictive lung disease; severe obstructive sleep apnea documented; BiPAP recommended in long-term follow-up | Suggested HPO: laryngotracheal stenosis/narrowing, restrictive lung disease, obstructive sleep apnea, snoring; UBERON suggested: larynx, trachea, lung | Primary human (stefano2017extl3mutationscause pages 1-3, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 6-7, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3) |
| Visceral phenotype | Liver cysts and kidney cysts recur in a subset; hepatic cysts may be prenatal and persistent/stable over time; small ventricular septal defect reported in one case | Suggested HPO: Hepatic cysts, Renal cysts, Ventricular septal defect; UBERON suggested: liver, kidney, heart | Primary human (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6, bajaj2022anultrararecase pages 1-2, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3) |
| Mortality/prognosis | Severe infantile presentations can be lethal; review of 14 cases noted 5 deaths before age 1 year, mainly from recurrent infections; survivors can show long-term disability, wheelchair dependence, and progressive orthopedic/respiratory burden | Suggested HPO: recurrent severe infections, failure to thrive, motor disability; prognosis terms not standardized here | Published case aggregation + longitudinal case (bajaj2022anultrararecase pages 2-4, stefano2017extl3mutationscause pages 7-9, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3) |
| Disease course | Usually congenital/infantile onset; chronic lifelong course with variable severity; some skeletal findings become less conspicuous with age while kyphoscoliosis and cervical complications may progress | Suggested onset term: congenital/infantile onset; suggested HPO: progressive kyphoscoliosis | Primary human longitudinal evidence (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6, bajaj2022anultrararecase pages 1-2, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3) |
| Molecular mechanism | EXTL3 is a Golgi glycosyltransferase required for initiation/extension of heparan sulfate (HS) biosynthesis; disease-causing variants alter HS amount/composition/chain properties, disrupting growth-factor and cytokine signaling important for skeletal, thymic, and neurodevelopment | GO suggested: heparan sulfate proteoglycan biosynthetic process; glycosyltransferase activity; fibroblast growth factor receptor signaling pathway; cytokine-mediated signaling pathway; UBERON suggested: Golgi apparatus is GO-CC rather than UBERON | Primary human functional + structural biochemistry (stefano2017extl3mutationscause pages 3-5, stefano2017extl3mutationscause pages 1-1, wilson2022thestructureof pages 1-2, bourgeais2024chemoenzymaticsynthesisof pages 11-12) |
| Upstream biochemical defect | Patient fibroblasts showed abnormal HS composition and altered FGF2 signaling; wild-type EXTL3 cDNA rescued the signaling defect | GO suggested: fibroblast growth factor receptor signaling pathway; glycosaminoglycan biosynthetic process; CL suggested: fibroblast | Primary human in vitro rescue (stefano2017extl3mutationscause pages 3-5, stefano2017extl3mutationscause pages 1-1) |
| Immune pathophysiology | Reduced IL-2-mediated STAT5 phosphorylation in patient lymphocytes and defects in lymphohematopoietic progenitor expansion plus thymic epithelial progenitor differentiation support combined hematopoietic and thymic-stromal disease mechanisms | GO suggested: interleukin-2-mediated signaling pathway, STAT5 phosphorylation, thymus development, T cell differentiation; CL suggested: lymphocyte, hematopoietic progenitor cell, thymic epithelial cell | Primary human + iPSC (stefano2017extl3mutationscause pages 3-5, stefano2017extl3mutationscause pages 7-9, stefano2017extl3mutationscause pages 1-1) |
| Affected tissues/cells | Strong evidence implicates cartilage/bone, thymus/thymic epithelium, lymphohematopoietic progenitors, and brain/CNS development | UBERON suggested: vertebral column, pelvis, thymus, brain, spinal cord; CL suggested: chondrocyte, thymic epithelial cell, hematopoietic progenitor cell, T cell | Primary human + model organism + expert review (stefano2017extl3mutationscause pages 3-5, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6, stefano2017extl3mutationscause pages 7-9) |
| Structural biology | 2022 cryo-EM/structural work showed EXTL3 is a homodimeric bi-domain exostosin with GT47 and GT64 domains; GT47 is ineffective for GlcA transfer, supporting a non-processive/dissociative HS polymerization model | GO suggested: transferase activity, transferring glycosyl groups; protein domain labels GT47 and GT64 (suggested structural annotations) | Structural biochemistry (wilson2022thestructureof pages 1-2) |
| Biosynthetic specificity | 2023-2024 work supports EXTL3 as a selective HS-initiating “decision” enzyme favoring HS-proteoglycan-like substrates over CS-proteoglycan-like substrates | GO suggested: heparan sulfate proteoglycan biosynthetic process; chondroitin sulfate biosynthetic process | Structural/biochemical in vitro (bourgeais2024chemoenzymaticsynthesisof pages 11-12) |
| Diagnostics | Diagnosis in practice relies on exome/genome sequencing or targeted molecular testing, combined with clinicoradiologic recognition of spondyloepimetaphyseal dysplasia plus neurodevelopmental and immune findings | Suggested methods/MAXO not needed; HPO pattern terms above; molecular testing approach: WES/WGS/EXTL3 single-gene or skeletal dysplasia/immunodeficiency panels (suggested) | Primary human case diagnosis + expert review (bajaj2022anultrararecase pages 2-4, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3) |
| Diagnostic workup adjuncts | Radiographs/spine imaging, brain MRI, immunophenotyping, immunoglobulins, lymphocyte subsets, TREC newborn screening where available, sleep study/airway evaluation, and renal/hepatic imaging are useful adjuncts | Suggested HPO/LOINC-equivalent concepts: lymphocyte subset assay, immunoglobulin quantification, spinal MRI, polysomnography, abdominal imaging | Primary human + expert review (stefano2017extl3mutationscause pages 1-3, stefano2017extl3mutationscause pages 7-9, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3) |
| Differential diagnosis frame | Differential diagnosis includes other immuno-osseous dysplasias and syndromic skeletal dysplasias with immune disease, such as Schimke immuno-osseous dysplasia, cartilage-hair hypoplasia, and SPENCDI | Suggested disease mappings only if separately curated; not specific IDs here | Expert clinical review (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 3-4) |
| Current management | No disease-specific approved therapy identified; management is multidisciplinary supportive care and surveillance | MAXO suggested: multidisciplinary care, surveillance, supportive care (suggested mappings) | Clinical practice extrapolation from case literature (bajaj2022anultrararecase pages 2-4, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3) |
| Immune management | Immune monitoring, infection prevention/treatment, and immunoglobulin replacement/SCID-directed care may be needed in severe immune phenotypes; caution that stromal thymic defects may limit hematopoietic-only correction | MAXO suggested: immunologic monitoring, antimicrobial therapy/prophylaxis, immunoglobulin replacement therapy, hematopoietic stem cell transplantation evaluation (suggested) | Primary human + expert thymus review (stefano2017extl3mutationscause pages 1-3, stefano2017extl3mutationscause pages 7-9, dinges2024primaryandsecondary pages 35-37) |
| Neurosurgical/orthopedic management | Early cervical surveillance and decompression for cord compression/instability, kyphoscoliosis surgery when indicated, orthopedic follow-up, mobility aids, and rehabilitation are real-world implementations documented in cases | MAXO suggested: spinal decompression surgery, scoliosis corrective surgery, orthopedic management, physical therapy, mobility support | Primary human longitudinal care (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 6-7, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3) |
| Respiratory/supportive management | Sleep-study-guided airway support including BiPAP in obstructive sleep apnea, monitoring for restrictive lung disease, and airway assessment in laryngotracheal narrowing | MAXO suggested: noninvasive ventilation, polysomnography-guided management, respiratory monitoring | Primary human (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3, stefano2017extl3mutationscause pages 1-3) |
| Prevention/genetic counseling | Because inheritance is AR, recurrence-risk counseling, carrier testing in relatives, prenatal diagnosis, and preimplantation genetic testing are appropriate preventive strategies when familial variants are known | MAXO suggested: genetic counseling; suggested prevention concepts: carrier screening, prenatal molecular diagnosis, PGT-M | Human genetics practice based on AR disease (bajaj2022anultrararecase pages 2-4, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 3-4) |
| Environmental factors | No specific environmental, lifestyle, infectious, or toxin exposures were identified as causal in retrieved disease-specific literature; immune complications are secondary rather than causal | Not applicable / no validated ontology mapping from retrieved evidence | Evidence gap from retrieved literature (bajaj2022anultrararecase pages 2-4, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6) |
| Natural disease in other species | No naturally occurring veterinary counterpart was identified in retrieved sources | NCBI Taxon not applicable from retrieved evidence | Evidence gap |
| Zebrafish model | extl3-mutant zebrafish show defective thymopoiesis, reduced thymus volume, pectoral fin/cartilage defects, and shortened body axis; wild-type human EXTL3 RNA rescues thymic and fin phenotypes | Suggested Taxon: Danio rerio; CL suggested: thymocyte/T-cell progenitor; UBERON suggested: thymus, pectoral fin cartilage | Primary model-organism rescue evidence (stefano2017extl3mutationscause pages 3-5, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6, stefano2017extl3mutationscause pages 1-1) |
| Mouse model | Extl3-null mice are embryonic lethal around E9.5, limiting full postnatal disease modeling; HS-deficient thymus models support a role for HS in thymus growth | Suggested Taxon: Mus musculus; GO suggested: embryonic development, thymus development | Mouse genetics + mechanistic support (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6, dinges2024primaryandsecondary pages 35-37) |
| Human cellular models | Patient fibroblasts and patient-derived iPSCs recapitulate signaling and developmental defects, including abnormal HS composition, altered FGF2 signaling, reduced lymphohematopoietic progenitor expansion, and impaired thymic epithelial progenitor differentiation | CL suggested: fibroblast, induced pluripotent stem cell, hematopoietic progenitor cell, thymic epithelial progenitor cell | Primary in vitro/iPSC (stefano2017extl3mutationscause pages 3-5, stefano2017extl3mutationscause pages 7-9, stefano2017extl3mutationscause pages 1-1) |


*Table: This compact table summarizes high-confidence, ontology-ready facts for EXTL3-related immunoskeletal dysplasia with neurodevelopmental abnormalities, including identifiers, phenotypes, mechanisms, diagnostics, management, and models. It is designed to support structured disease knowledge-base curation while clearly marking suggested mappings and evidence types.*

## 1. Disease information

### Definition and classification

ISDNA is a Mendelian glycosaminoglycan-biosynthesis disorder in the spondyloepimetaphyseal dysplasia group. The characteristic combination is disproportionate short stature and vertebral/epiphyseal/metaphyseal abnormalities, developmental delay or intellectual disability, and variable cellular immunodeficiency. Liver or renal cysts, airway disease, and cervical instability may broaden the phenotype. (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3)

**Identifiers and nomenclature**

- **MONDO:** MONDO:0044312.
- **OMIM phenotype:** MIM 617425.
- **Causal target:** EXTL3, Ensembl ENSG00000012232. Open Targets associates this disease uniquely with EXTL3 and cites the two foundational 2017 reports, PMID **28132690** and **28148688**. (OpenTargets Search: Immunoskeletal dysplasia with neurodevelopmental abnormalities)
- **Common names:** immunoskeletal dysplasia with neurodevelopmental abnormalities; ISDNA; EXTL3 deficiency; EXTL3-related immunoskeletal dysplasia; spondyloepimetaphyseal dysplasia with immune deficiency, EXTL3 type; SEMD, EXTL3-deficient type. (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3)
- **Orphanet, ICD-10/ICD-11, and MeSH:** no disease-specific identifier was verified in the retrieved evidence. In practice, nonspecific skeletal-dysplasia, immunodeficiency, and developmental-disorder codes may be used, but they should not be represented as exact equivalents.

The evidence is principally **aggregated disease-level literature built from very small case series and individual patients**, not population-scale EHR data. The 2021 review counted 14 affected people from nine unrelated families; the 2022 Indian report described its patient as the 15th published case. Later 2023–2024 case reports indicate that this historical count is no longer exhaustive, but no comprehensive contemporary registry was found. (bajaj2022anultrararecase pages 2-4, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3)

## 2. Etiology, risk, and protective factors

The necessary causal factor is a **germline biallelic pathogenic or likely pathogenic EXTL3 genotype**. The inheritance pattern is autosomal recessive; affected children have been born to heterozygous parents, and consanguinity was present in several families. (bajaj2022anultrararecase pages 2-4, stefano2017extl3mutationscause pages 1-3, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 3-4)

No validated environmental, infectious, occupational, lifestyle, age-related, or sex-specific cause exists. Infection is a consequence of immune dysfunction, not the initiating etiology. Family history and parental consanguinity increase prior genetic risk but are not required. No protective allele, modifier gene, diet, exposure, or lifestyle intervention has been established. Marked immune variability among individuals carrying the same p.Pro318Leu allele suggests unidentified genetic modifiers and possibly environmental effects on infectious outcomes, but no specific gene–environment interaction has been demonstrated. (bajaj2022anultrararecase pages 1-2, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 3-4)

## 3. Phenotypic spectrum

### Skeletal and craniofacial disease

Core, early-onset physical and radiographic findings include disproportionate short stature or short-limb dwarfism, severe platyspondyly with widened intervertebral spaces, brachydactyly, epiphyseal and metaphyseal dysplasia, coxa valga, acetabular dysplasia, delayed femoral-head ossification, hip subluxation/dislocation, and progressive kyphoscoliosis. Pelvic radiographs may show squared or open iliac wings, trident-shaped acetabula, and narrow sacro-ischiatic notches. (bajaj2022anultrararecase pages 2-4, stefano2017extl3mutationscause pages 3-5, bajaj2022anultrararecase pages 1-2, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3)

Craniovertebral disease is particularly consequential: odontoid hypoplasia, atlas non-ossification, cervical stenosis or instability, and cord compression have required early neurosurgical intervention. Craniosynostosis, including cloverleaf skull deformity, occurs in severe cases but is not universal. Suggested HPO concepts include **Short stature (HP:0001511), Platyspondyly (HP:0000926), Brachydactyly (HP:0001156), Kyphoscoliosis, Odontoid hypoplasia, Cervical vertebral instability, Spinal-cord compression, Coxa valga,** and **Acetabular dysplasia**. (bajaj2022anultrararecase pages 2-4, stefano2017extl3mutationscause pages 1-3, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 6-7)

Facial findings are variable but often recognizable: coarse facies, frontal bossing, full cheeks and lips, broad/bulbous nasal tip, abnormal nasal bridge, long eyelashes or synophrys, and micrognathia. Dysmorphism may become more apparent with age. (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3)

### Neurologic and behavioral phenotype

Global and especially gross-motor delay, axial or central hypotonia, delayed language, and mild-to-severe intellectual disability are common. Severe presentations may include seizures, opisthotonus, hyperreflexia, nystagmus, developmental arrest, or hyporeflexia. Diffuse corpus-callosum thinning was documented in one longitudinally observed patient. Suggested terms include **Global developmental delay (HP:0001263), Hypotonia (HP:0001252), Intellectual disability (HP:0001249), Seizure (HP:0001250), Motor delay,** and **Thin corpus callosum**. (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6, stefano2017extl3mutationscause pages 1-3, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3)

### Immune and laboratory phenotype

The immune phenotype is highly variable and predominantly T-cell related. In the historical 14-patient synthesis, nine had T-cell lymphopenia; four were described with Omenn-like SCID, while one had oral candidiasis without the full severe phenotype. Another tabulation reported T-cell SCID in 5/9 evaluable patients, hypogammaglobulinemia in 5/9, Omenn-like disease in 3/9, and hyper-IgE in 1/9, illustrating both small denominators and differences in case classification. (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 6-7, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 3-4)

Reported abnormalities include T−B+NK+ or T−NK+B+ profiles, low/absent TRECs, impaired mitogen proliferation, predominantly activated/memory residual T cells, eosinophilia, hypogammaglobulinemia, elevated IgE, and reduced IL-2/IL-7-induced STAT5 phosphorylation. Some individuals have little infection susceptibility, and T-cell numbers improved spontaneously in one survivor. Normal routine CBC or biochemistry therefore does not exclude the disease. (stefano2017extl3mutationscause pages 3-5, stefano2017extl3mutationscause pages 1-3, stefano2017extl3mutationscause pages 7-9, bajaj2022anultrararecase pages 1-2)

### Other manifestations and quality of life

Additional findings include hepatic cysts—occasionally detected prenatally—renal cysts, laryngotracheal narrowing, restrictive lung disease secondary to kyphoscoliosis, obstructive sleep apnea, neurogenic bladder, and occasional congenital heart disease such as ventricular septal defect. One 15-year-old survivor was unable to walk independently and became wheelchair-dependent; progressive spinal disease, respiratory impairment, developmental disability, recurrent infections, surgery, and mobility loss therefore impose substantial functional burden. No validated disease-specific EQ-5D, SF-36, PROMIS, or other quality-of-life dataset was found. (bajaj2022anultrararecase pages 1-2, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 6-7, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3)

## 4. Genetic and molecular information

**EXTL3** encodes exostosin-like glycosyltransferase 3, an enzyme that initiates heparan-sulfate chains by transferring N-acetylglucosamine and also has GlcNAc transferase activity during chain synthesis. The early literature summarized six disease alleles: **c.953C>T (p.Pro318Leu), c.1015C>T (p.Arg339Trp), c.1382C>T (p.Pro461Leu), c.1537C>T, c.1970A>G, and c.2008T>G**. All were germline missense alleles; p.Arg339Trp was experimentally characterized as hypomorphic. Exact protein consequences of the latter three should be rechecked against the current reference transcript before database ingestion. (stefano2017extl3mutationscause pages 3-5, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 3-4)

The recurrent p.Pro318Leu variant was reported at very low ExAC frequency and was classified as likely pathogenic under 2015 ACMG criteria in the 2021 case, with a CADD score of 22.2 and appropriate parental segregation. Current ClinVar classifications and gnomAD frequencies should be queried directly at ingestion because database assertions can change. No established pathogenic structural variant, repeat expansion, mitochondrial variant, somatic mechanism, chromosomal abnormality, or disease-specific epigenetic signature was identified. (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 3-4)

There is no robust variant-position/severity correlation. Individuals homozygous for the same p.Pro318Leu allele have ranged from severe immunodeficiency to subtle immune findings, supporting variable expressivity and unknown modifiers. Penetrance among confirmed biallelic pathogenic genotypes appears high for a syndromic phenotype, but the sample is too small to calculate penetrance formally. (bajaj2022anultrararecase pages 1-2, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 3-4)

## 5. Environmental and infectious information

No toxin, radiation, pollution, diet, exercise pattern, smoking, alcohol exposure, or infectious agent is known to cause ISDNA. Pathogens influence morbidity because affected patients may have SCID or T-cell lymphopenia. Accordingly, infectious exposure can modify clinical outcome without being etiologic. No zoonotic or transmissible mechanism applies.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic defect:** biallelic hypomorphic EXTL3 variants alter glycosyltransferase function.
2. **Biochemical defect:** initiation and structural composition of heparan sulfate (HS) on proteoglycans become abnormal; patient fibroblasts produced aberrant HS chains and sulfation patterns.
3. **Signal-distribution defect:** HS normally binds and spatially regulates morphogens, growth factors, and cytokines. Abnormal HS changed FGF2–ERK signaling and impaired IL-2/IL-7–STAT5 responses.
4. **Developmental consequences:** altered extracellular signaling disrupts chondrocyte/cartilage development, thymic epithelial differentiation, lymphohematopoietic progenitor expansion, and brain development.
5. **Clinical consequences:** spondyloepimetaphyseal dysplasia and spinal instability, T-cell immunodeficiency, and neurodevelopmental disability result. (stefano2017extl3mutationscause pages 3-5, stefano2017extl3mutationscause pages 7-9, stefano2017extl3mutationscause pages 1-1)

In primary fibroblasts, wild-type EXTL3 cDNA rescued altered FGF2 signaling, strengthening causality. Patient-derived iPSCs showed reduced lymphohematopoietic progenitor expansion and deficient thymic epithelial progenitor differentiation, with reduced TBX1, EYA1, and CK5 and persistent SOX17 expression. Thus, the immune phenotype likely combines hematopoietic-intrinsic and thymic-stromal defects. (stefano2017extl3mutationscause pages 7-9, stefano2017extl3mutationscause pages 1-1)

### Recent mechanistic developments

A 2022 cryo-EM study showed that human EXTL3 is a roughly 170-kDa homodimer with GT47 and GT64 glycosyltransferase domains. Its GT47 domain is ineffective at glucuronic-acid transfer, whereas the enzyme retains GlcNAc-transferase activity; the domain arrangement supports a dissociative rather than processive HS-extension mechanism. Published June 2022, DOI/URL: https://doi.org/10.1038/s41467-022-31048-2. (wilson2022thestructureof pages 1-2)

A 2024 biochemical study found that EXTL3 preferentially modifies peptides resembling HS-proteoglycan core proteins, including syndecan-3 and TGFBR3, supporting a “decision-making” role at the HS-versus-chondroitin-sulfate branch. Published February 2024, DOI/URL: https://doi.org/10.1093/glycob/cwae016. (bourgeais2024chemoenzymaticsynthesisof pages 11-12)

Suggested annotations include **GO: heparan-sulfate proteoglycan biosynthetic process, glycosyltransferase activity, FGF-receptor signaling, cytokine-mediated signaling, STAT5 phosphorylation, thymus development, T-cell differentiation**; **CL: chondrocyte, fibroblast, hematopoietic progenitor cell, thymic epithelial cell, thymocyte, T lymphocyte**; and **GO cellular component: Golgi apparatus, cell surface, extracellular matrix**. No disease-specific single-cell atlas, spatial transcriptomic dataset, clinical proteome, metabolome, lipidome, or epigenomic signature was identified.

## 7. Anatomical structures affected

Primary systems are the axial and appendicular skeleton, growth plate/cartilage, thymus and lymphoid system, and CNS. Particularly important sites are the vertebral bodies, craniovertebral junction, cervical spinal canal and cord, pelvis/acetabulum, proximal femora, and long-bone epiphyses/metaphyses. Secondary involvement includes liver, kidneys, larynx/trachea, lungs, bladder, and occasionally heart. (stefano2017extl3mutationscause pages 1-3, bajaj2022anultrararecase pages 1-2, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3)

Suggested UBERON concepts are **vertebral column, cervical vertebral column, spinal cord, cartilage, femur, pelvis, acetabulum, thymus, brain, corpus callosum, liver, kidney, larynx, trachea,** and **lung**. Skeletal disease is generally bilateral/systemic rather than consistently lateralized.

## 8. Temporal development and natural history

Onset is prenatal, congenital, or early infantile. Severe cases manifest at birth with short limbs, craniosynostosis, seizures, and infections. Hepatic cysts can be detected prenatally. The condition is chronic and lifelong rather than episodic or remitting. (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 3-4, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3)

The course is variable. Some radiographic skeletal features become less conspicuous with age, but kyphoscoliosis, hip disease, cervical compression, restrictive lung disease, sleep apnea, and mobility impairment may progress. Immune dysfunction can remain severe, fluctuate, or partially improve. Developmental intervention and cervical surveillance represent critical early opportunities; cord compression can lead to neurogenic bladder and irreversible disability. (stefano2017extl3mutationscause pages 7-9, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3)

## 9. Inheritance, epidemiology, and population

Inheritance is autosomal recessive. For two carrier parents, standard Mendelian counseling gives a 25% affected, 50% carrier, and 25% unaffected/non-carrier probability in each pregnancy, assuming both variants are fully disease-causing. Genetic anticipation is not expected. Germline mosaicism has not been specifically demonstrated, and no founder allele or reliable carrier frequency is established. (bajaj2022anultrararecase pages 2-4, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 3-4)

Prevalence and incidence per 100,000 are unknown. The published cohort includes Turkish, North African, Portuguese, Colombian/South American, Indian, and other ancestries, indicating worldwide occurrence rather than a proven geographic concentration. Both sexes are affected; no reliable sex ratio can be calculated. Consanguinity contributed to ascertainment in several families but is not obligatory. (bajaj2022anultrararecase pages 4-5, bajaj2022anultrararecase pages 5-6)

## 10. Diagnosis

There are no formal society diagnostic criteria. Suspicion should arise from the combination of SEMD/platyspondyly, disproportionate short stature, developmental delay or hypotonia, and T-cell lymphopenia or recurrent infections. Absence of clinically obvious immunodeficiency does not exclude EXTL3 disease. (bajaj2022anultrararecase pages 2-4, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 3-4)

**Recommended evaluation:**

- Trio WES or WGS, or an inclusive skeletal-dysplasia/inborn-error-of-immunity panel containing EXTL3; confirm candidate variants and familial segregation by Sanger sequencing where appropriate.
- Skeletal survey plus dynamic or specialist-directed cervical radiography/MRI; avoid unsafe neck manipulation until instability has been assessed.
- Brain MRI and developmental, neurologic, audiologic, and ophthalmologic assessment as indicated.
- CBC with differential, lymphocyte subsets, naïve/memory T-cell phenotype, immunoglobulins, vaccine responses, mitogen proliferation, and TREC assessment. Newborn TREC screening may detect severe cases.
- Liver/renal ultrasonography, echocardiography, airway evaluation, pulmonary function testing when feasible, and polysomnography for snoring or suspected apnea. (stefano2017extl3mutationscause pages 1-3, stefano2017extl3mutationscause pages 7-9, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3)

Routine metabolic screening and urinary glycosaminoglycans may be normal; a normal result does not exclude EXTL3 deficiency. CMA, karyotype, FISH, mitochondrial sequencing, and repeat-expansion assays are not first-line tests unless the phenotype or initial sequencing indicates another diagnosis. (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3)

Important differentials include Schimke immuno-osseous dysplasia (**SMARCAL1**), cartilage-hair hypoplasia (**RMRP**), spondyloenchondrodysplasia with immune dysregulation (**ACP5**), other SEMDs, mucopolysaccharidoses, achondroplasia-like skeletal disorders, and syndromic craniosynostosis. (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 3-4)

## 11. Outcome and prognosis

No actuarial survival curve, five- or ten-year survival rate, or validated prognostic model exists. In the 14-case literature review, **5/14 patients died before one year**, mainly from recurrent infection. Two siblings in the foundational series died at seven and 11 months. Conversely, survival into adolescence is documented, although with progressive kyphoscoliosis, cervical surgery, respiratory disease, intellectual disability, and wheelchair dependence. (bajaj2022anultrararecase pages 2-4, stefano2017extl3mutationscause pages 7-9, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3)

Likely adverse prognostic features are profound neonatal T-cell deficiency/Omenn-like SCID, recurrent severe infection, airway narrowing, early seizures or developmental arrest, and cervical cord compression. These are clinically plausible markers derived from a very small series, not validated predictors. Recovery from the genetic skeletal/neurodevelopmental disorder is not expected, but infection risk, respiratory function, spinal compression, communication, and mobility may improve with timely intervention.

## 12. Treatment and real-world implementation

No approved pharmacologic, gene, RNA, cell, or targeted therapy corrects EXTL3 deficiency, and the ClinicalTrials.gov search identified no disease-specific interventional study or NCT identifier.

Current care is phenotype directed:

- **Immune care:** pediatric immunology follow-up; prompt antimicrobial treatment; individualized antibacterial/antiviral/antifungal prophylaxis; immunoglobulin replacement when antibody deficiency is clinically significant; avoidance of live vaccines in severe cellular immunodeficiency. Suggested MAXO concepts: immunologic monitoring, antimicrobial prophylaxis, immunoglobulin replacement.
- **SCID-directed therapy:** hematopoietic stem-cell transplantation may be considered for life-threatening hematopoietic immune deficiency, but EXTL3 disease also affects thymic stroma and nonhematopoietic tissues, so transplantation should not be assumed to correct the complete syndrome. Published disease-specific response rates are unavailable. (stefano2017extl3mutationscause pages 7-9, stefano2017extl3mutationscause pages 1-1)
- **Spine/orthopedics:** serial cervical and scoliosis assessment; urgent decompression/stabilization for cord compression or instability; hip and contracture management; mobility aids. A longitudinal patient underwent C1-arch excision/decompression and kyphoscoliosis correction. Suggested MAXO: spinal decompression surgery, spinal stabilization, scoliosis surgery. (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 6-7, akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3)
- **Respiratory:** airway assessment, pulmonary monitoring, sleep study, and noninvasive ventilation. Severe obstructive sleep apnea with apnea–hypopnea index 29.7 led to BiPAP recommendation in one patient. (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 3-4)
- **Development and function:** early physical, occupational, speech/language, feeding, and educational therapies; seizure treatment according to standard neurology practice.
- **Visceral disease:** monitor liver and kidney cysts; intervene for mass effect, infection, impaired function, or other standard indications.

There are no EXTL3-specific pharmacogenomic recommendations, response statistics, or systematic adverse-event data.

## 13. Prevention

There is no lifestyle or vaccine-based primary prevention of the genotype. Primary genetic prevention consists of carrier testing, genetic counseling, preimplantation genetic testing for monogenic disease, prenatal diagnosis by chorionic-villus sampling or amniocentesis, and cascade testing after familial variants are established.

Secondary prevention comprises early genomic diagnosis, SCID newborn screening where available, immune evaluation before serious infection, and early cervical imaging before neurologic injury. Tertiary prevention includes infection prophylaxis, immunoglobulin replacement when indicated, spinal surveillance, respiratory care, vaccination planning under immunology supervision, rehabilitation, and avoidance of hazardous cervical manipulation. Population-wide EXTL3 carrier or newborn genomic screening is not currently established.

## 14. Other species and natural disease

No naturally occurring homologous veterinary disorder, affected breed, wildlife reservoir, zoonotic transmission, or cross-species infectious susceptibility was identified. Relevant orthologs include **Extl3** in mouse (*Mus musculus*, NCBI Taxon 10090) and **extl3** in zebrafish (*Danio rerio*, NCBI Taxon 7955). Ortholog-specific NCBI Gene identifiers should be verified directly before database loading.

## 15. Model organisms and experimental systems

**Zebrafish:** extl3-mutant zebrafish have reduced/abnormal HS, defective cartilage and chondrocyte organization, shortened body axis and pectoral fins, and approximately 50% reduced thymic GFP-positive volume in a rag2 reporter background. Injection of wild-type human EXTL3 RNA rescued thymic and fin phenotypes, providing strong functional-complementation evidence. The model is useful for HS-dependent cartilage development and thymopoiesis but does not reproduce the full human spinal, cognitive, or longitudinal phenotype. (stefano2017extl3mutationscause pages 3-5, stefano2017extl3mutationscause pages 1-1)

**Mouse:** complete Extl3 deficiency is embryonically lethal at approximately embryonic day 9.5, demonstrating developmental essentiality but limiting postnatal modeling. Conditional HS-deficient thymic models support an essential role for HS in thymus growth. (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6)

**Human cellular models:** patient fibroblasts reproduce HS and FGF2-signaling abnormalities, while patient iPSCs model impaired lymphohematopoietic expansion and thymic epithelial differentiation. These systems are valuable for variant validation and therapeutic screening but cannot model whole-organ biomechanics or infection outcomes. (stefano2017extl3mutationscause pages 3-5, stefano2017extl3mutationscause pages 7-9, stefano2017extl3mutationscause pages 1-1)

## Key evidence quotations and sources

- Volpi et al., *Journal of Experimental Medicine*, published February 2017, DOI/URL: https://doi.org/10.1084/jem.20161525. Abstract: **“These data identify EXTL3 mutations as a novel cause of severe immune deficiency with skeletal dysplasia and developmental delay and underline a crucial role of HS in thymopoiesis and skeletal and brain development.”** (stefano2017extl3mutationscause pages 1-1)
- Bajaj et al., *BMC Pediatrics*, published February 2022, DOI/URL: https://doi.org/10.1186/s12887-022-03143-2. Abstract: **“ISDNA is an ultra-rare genetic condition… caused due to presence of biallelic variants in the EXTL3 gene.”** The report described the 15th published patient and emphasized phenotypic variability despite an identical allele. (bajaj2022anultrararecase pages 2-4, bajaj2022anultrararecase pages 1-2)
- Akalın et al., *American Journal of Medical Genetics Part A*, accepted May 18, 2021, DOI/URL: https://doi.org/10.1002/ajmg.a.62378. Abstract: **“Affected individuals display variable skeletal abnormalities and neurodevelopmental findings… Patients may exhibit varying degrees of immune deficiency as well.”** (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3)
- Wilson et al., *Nature Communications*, June 2022, DOI/URL: https://doi.org/10.1038/s41467-022-31048-2. The study reported human EXTL3 structures and proposed dissociative HS polymerization. (wilson2022thestructureof pages 1-2)
- Bourgeais et al., *Glycobiology*, February 2024, DOI/URL: https://doi.org/10.1093/glycob/cwae016. The study found substrate preferences consistent with EXTL3 helping determine whether a proteoglycan receives HS. (bourgeais2024chemoenzymaticsynthesisof pages 11-12)

## Evidence limitations

The knowledge base rests on a few families, heterogeneous reporting, and partially overlapping case summaries. Frequencies such as 9/14 immune involvement and 5/14 infant deaths describe the early published cohort, not unbiased population estimates. No contemporary natural-history registry, validated quality-of-life instrument, formal treatment guideline, prevalence study, or disease-specific trial was found. Variant nomenclature, ClinVar status, population frequencies, and exact ontology identifiers should therefore be refreshed from live databases during production curation.

References

1. (bajaj2022anultrararecase pages 2-4): Shruti Bajaj, Purnima Satoskar, Aadhira Nair, Frenny Sheth, Jayesh Sheth, and Harsh Sheth. An ultra-rare case of immunoskeletal dysplasia with neurodevelopmental abnormalities in an indian patient with homozygous c.953c > t variant in extl3 gene: a case report. BMC Pediatrics, Feb 2022. URL: https://doi.org/10.1186/s12887-022-03143-2, doi:10.1186/s12887-022-03143-2. This article has 6 citations and is from a peer-reviewed journal.

2. (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 4-6): Akçahan Akalın, Ekim Z. Taskiran, Pelin Özlem Şimşek‐Kiper, Eda Utine, Yasemin Alanay, Uğur Özçelik, and Koray Boduroğlu. Spondyloepimetaphyseal dysplasia extl3‐deficient type: long‐term follow‐up and review of the literature. American Journal of Medical Genetics Part A, 185:3104-3110, Jun 2021. URL: https://doi.org/10.1002/ajmg.a.62378, doi:10.1002/ajmg.a.62378. This article has 12 citations.

3. (unger2023nosologyofgenetic pages 29-30): Sheila Unger, Carlos R. Ferreira, Geert R. Mortier, Houda Ali, Débora R. Bertola, Alistair Calder, Daniel H. Cohn, Valerie Cormier‐Daire, Katta M. Girisha, Christine Hall, Deborah Krakow, Outi Makitie, Stefan Mundlos, Gen Nishimura, Stephen P. Robertson, Ravi Savarirayan, David Sillence, Marleen Simon, V. Reid Sutton, Matthew L. Warman, and Andrea Superti‐Furga. Nosology of genetic skeletal disorders: 2023 revision. American Journal of Medical Genetics Part A, 191:1164-1209, Feb 2023. URL: https://doi.org/10.1002/ajmg.a.63132, doi:10.1002/ajmg.a.63132. This article has 528 citations.

4. (OpenTargets Search: Immunoskeletal dysplasia with neurodevelopmental abnormalities): Open Targets Query (Immunoskeletal dysplasia with neurodevelopmental abnormalities, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (stefano2017extl3mutationscause pages 3-5): Stefano Volpi, Yasuhiro Yamazaki, Patrick M. Brauer, Ellen van Rooijen, Atsuko Hayashida, Anne Slavotinek, Hye Sun Kuehn, Maja Di Rocco, Carlo Rivolta, Ileana Bortolomai, Likun Du, Kerstin Felgentreff, Lisa Ott de Bruin, Kazutaka Hayashida, George Freedman, Genni Enza Marcovecchio, Kelly Capuder, Prisni Rath, Nicole Luche, Elliott J. Hagedorn, Antonella Buoncompagni, Beryl Royer-Bertrand, Silvia Giliani, Pietro Luigi Poliani, Luisa Imberti, Kerry Dobbs, Fabienne E. Poulain, Alberto Martini, John Manis, Robert J. Linhardt, Marita Bosticardo, Sergio Damian Rosenzweig, Hane Lee, Jennifer M. Puck, Juan Carlos Zúñiga-Pflücker, Leonard Zon, Pyong Woo Park, Andrea Superti-Furga, and Luigi D. Notarangelo. Extl3 mutations cause skeletal dysplasia, immune deficiency, and developmental delay. The Journal of Experimental Medicine, 214:623-637, Feb 2017. URL: https://doi.org/10.1084/jem.20161525, doi:10.1084/jem.20161525. This article has 103 citations.

6. (stefano2017extl3mutationscause pages 1-3): Stefano Volpi, Yasuhiro Yamazaki, Patrick M. Brauer, Ellen van Rooijen, Atsuko Hayashida, Anne Slavotinek, Hye Sun Kuehn, Maja Di Rocco, Carlo Rivolta, Ileana Bortolomai, Likun Du, Kerstin Felgentreff, Lisa Ott de Bruin, Kazutaka Hayashida, George Freedman, Genni Enza Marcovecchio, Kelly Capuder, Prisni Rath, Nicole Luche, Elliott J. Hagedorn, Antonella Buoncompagni, Beryl Royer-Bertrand, Silvia Giliani, Pietro Luigi Poliani, Luisa Imberti, Kerry Dobbs, Fabienne E. Poulain, Alberto Martini, John Manis, Robert J. Linhardt, Marita Bosticardo, Sergio Damian Rosenzweig, Hane Lee, Jennifer M. Puck, Juan Carlos Zúñiga-Pflücker, Leonard Zon, Pyong Woo Park, Andrea Superti-Furga, and Luigi D. Notarangelo. Extl3 mutations cause skeletal dysplasia, immune deficiency, and developmental delay. The Journal of Experimental Medicine, 214:623-637, Feb 2017. URL: https://doi.org/10.1084/jem.20161525, doi:10.1084/jem.20161525. This article has 103 citations.

7. (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 3-4): Akçahan Akalın, Ekim Z. Taskiran, Pelin Özlem Şimşek‐Kiper, Eda Utine, Yasemin Alanay, Uğur Özçelik, and Koray Boduroğlu. Spondyloepimetaphyseal dysplasia extl3‐deficient type: long‐term follow‐up and review of the literature. American Journal of Medical Genetics Part A, 185:3104-3110, Jun 2021. URL: https://doi.org/10.1002/ajmg.a.62378, doi:10.1002/ajmg.a.62378. This article has 12 citations.

8. (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 1-3): Akçahan Akalın, Ekim Z. Taskiran, Pelin Özlem Şimşek‐Kiper, Eda Utine, Yasemin Alanay, Uğur Özçelik, and Koray Boduroğlu. Spondyloepimetaphyseal dysplasia extl3‐deficient type: long‐term follow‐up and review of the literature. American Journal of Medical Genetics Part A, 185:3104-3110, Jun 2021. URL: https://doi.org/10.1002/ajmg.a.62378, doi:10.1002/ajmg.a.62378. This article has 12 citations.

9. (bajaj2022anultrararecase pages 1-2): Shruti Bajaj, Purnima Satoskar, Aadhira Nair, Frenny Sheth, Jayesh Sheth, and Harsh Sheth. An ultra-rare case of immunoskeletal dysplasia with neurodevelopmental abnormalities in an indian patient with homozygous c.953c > t variant in extl3 gene: a case report. BMC Pediatrics, Feb 2022. URL: https://doi.org/10.1186/s12887-022-03143-2, doi:10.1186/s12887-022-03143-2. This article has 6 citations and is from a peer-reviewed journal.

10. (akalın2021spondyloepimetaphysealdysplasiaextl3‐deficient pages 6-7): Akçahan Akalın, Ekim Z. Taskiran, Pelin Özlem Şimşek‐Kiper, Eda Utine, Yasemin Alanay, Uğur Özçelik, and Koray Boduroğlu. Spondyloepimetaphyseal dysplasia extl3‐deficient type: long‐term follow‐up and review of the literature. American Journal of Medical Genetics Part A, 185:3104-3110, Jun 2021. URL: https://doi.org/10.1002/ajmg.a.62378, doi:10.1002/ajmg.a.62378. This article has 12 citations.

11. (stefano2017extl3mutationscause pages 7-9): Stefano Volpi, Yasuhiro Yamazaki, Patrick M. Brauer, Ellen van Rooijen, Atsuko Hayashida, Anne Slavotinek, Hye Sun Kuehn, Maja Di Rocco, Carlo Rivolta, Ileana Bortolomai, Likun Du, Kerstin Felgentreff, Lisa Ott de Bruin, Kazutaka Hayashida, George Freedman, Genni Enza Marcovecchio, Kelly Capuder, Prisni Rath, Nicole Luche, Elliott J. Hagedorn, Antonella Buoncompagni, Beryl Royer-Bertrand, Silvia Giliani, Pietro Luigi Poliani, Luisa Imberti, Kerry Dobbs, Fabienne E. Poulain, Alberto Martini, John Manis, Robert J. Linhardt, Marita Bosticardo, Sergio Damian Rosenzweig, Hane Lee, Jennifer M. Puck, Juan Carlos Zúñiga-Pflücker, Leonard Zon, Pyong Woo Park, Andrea Superti-Furga, and Luigi D. Notarangelo. Extl3 mutations cause skeletal dysplasia, immune deficiency, and developmental delay. The Journal of Experimental Medicine, 214:623-637, Feb 2017. URL: https://doi.org/10.1084/jem.20161525, doi:10.1084/jem.20161525. This article has 103 citations.

12. (stefano2017extl3mutationscause pages 1-1): Stefano Volpi, Yasuhiro Yamazaki, Patrick M. Brauer, Ellen van Rooijen, Atsuko Hayashida, Anne Slavotinek, Hye Sun Kuehn, Maja Di Rocco, Carlo Rivolta, Ileana Bortolomai, Likun Du, Kerstin Felgentreff, Lisa Ott de Bruin, Kazutaka Hayashida, George Freedman, Genni Enza Marcovecchio, Kelly Capuder, Prisni Rath, Nicole Luche, Elliott J. Hagedorn, Antonella Buoncompagni, Beryl Royer-Bertrand, Silvia Giliani, Pietro Luigi Poliani, Luisa Imberti, Kerry Dobbs, Fabienne E. Poulain, Alberto Martini, John Manis, Robert J. Linhardt, Marita Bosticardo, Sergio Damian Rosenzweig, Hane Lee, Jennifer M. Puck, Juan Carlos Zúñiga-Pflücker, Leonard Zon, Pyong Woo Park, Andrea Superti-Furga, and Luigi D. Notarangelo. Extl3 mutations cause skeletal dysplasia, immune deficiency, and developmental delay. The Journal of Experimental Medicine, 214:623-637, Feb 2017. URL: https://doi.org/10.1084/jem.20161525, doi:10.1084/jem.20161525. This article has 103 citations.

13. (wilson2022thestructureof pages 1-2): L. F. L. Wilson, T. Dendooven, S. W. Hardwick, A. Echevarría-Poza, T. Tryfona, K. B. R. M. Krogh, D. Y. Chirgadze, B. F. Luisi, D. T. Logan, K. Mani, and P. Dupree. The structure of extl3 helps to explain the different roles of bi-domain exostosins in heparan sulfate synthesis. Nature Communications, 13:1-15, Jun 2022. URL: https://doi.org/10.1038/s41467-022-31048-2, doi:10.1038/s41467-022-31048-2. This article has 37 citations and is from a highest quality peer-reviewed journal.

14. (bourgeais2024chemoenzymaticsynthesisof pages 11-12): Marie Bourgeais, Farah Fouladkar, Margot Weber, Elisabetta Boeri-Erba, and Rebekka Wild. Chemo-enzymatic synthesis of tetrasaccharide linker peptides to study the divergent step in glycosaminoglycan biosynthesis. Glycobiology, Feb 2024. URL: https://doi.org/10.1093/glycob/cwae016, doi:10.1093/glycob/cwae016. This article has 15 citations and is from a peer-reviewed journal.

15. (dinges2024primaryandsecondary pages 35-37): Sarah S. Dinges, Kayla Amini, Luigi D. Notarangelo, and Ottavia M. Delmonte. Primary and secondary defects of the thymus. Immunological Reviews, 322:178-211, Jan 2024. URL: https://doi.org/10.1111/imr.13306, doi:10.1111/imr.13306. This article has 29 citations and is from a domain leading peer-reviewed journal.

16. (bajaj2022anultrararecase pages 4-5): Shruti Bajaj, Purnima Satoskar, Aadhira Nair, Frenny Sheth, Jayesh Sheth, and Harsh Sheth. An ultra-rare case of immunoskeletal dysplasia with neurodevelopmental abnormalities in an indian patient with homozygous c.953c > t variant in extl3 gene: a case report. BMC Pediatrics, Feb 2022. URL: https://doi.org/10.1186/s12887-022-03143-2, doi:10.1186/s12887-022-03143-2. This article has 6 citations and is from a peer-reviewed journal.

17. (bajaj2022anultrararecase pages 5-6): Shruti Bajaj, Purnima Satoskar, Aadhira Nair, Frenny Sheth, Jayesh Sheth, and Harsh Sheth. An ultra-rare case of immunoskeletal dysplasia with neurodevelopmental abnormalities in an indian patient with homozygous c.953c > t variant in extl3 gene: a case report. BMC Pediatrics, Feb 2022. URL: https://doi.org/10.1186/s12887-022-03143-2, doi:10.1186/s12887-022-03143-2. This article has 6 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Immunoskeletal_Dysplasia_with_Neurodevelopmental_Abnormalities-deep-research-falcon_artifacts/artifact-00.md)