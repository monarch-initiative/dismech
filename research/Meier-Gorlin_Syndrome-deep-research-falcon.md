---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T22:55:57.254067'
end_time: '2026-07-31T23:06:34.982736'
duration_seconds: 637.73
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Meier-Gorlin syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 29
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Meier-Gorlin_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Meier-Gorlin syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Meier-Gorlin syndrome** covering all of the
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
- **Disease Name:** Meier-Gorlin syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Meier-Gorlin syndrome** covering all of the
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


# Meier–Gorlin syndrome: comprehensive disease-characteristics report

## Executive summary

Meier–Gorlin syndrome (MGORS) is an extremely rare, predominantly autosomal-recessive microcephalic primordial-dwarfism disorder caused by hypomorphic defects in DNA-replication licensing or replicative-helicase assembly. Its classic triad is prenatal/postnatal growth restriction, microtia, and absent or hypoplastic patellae; genital anomalies and post-pubertal mammary hypoplasia are also characteristic. At least two elements of the classic triad occur in approximately 97% of reported patients, but molecularly confirmed cases increasingly demonstrate a broader phenotype. Fewer than 100 affected individuals had been reported by the 2023 review, so frequencies and treatment estimates remain vulnerable to ascertainment and publication bias. (nielsendandoroff2023theexpandinggenetic pages 1-2, mcquaid2022hypomorphicgins3variants pages 1-2)

The current genetic spectrum comprises 13 replication-associated genes: **ORC1, ORC4, ORC6, CDT1, CDC6, GMNN, MCM3, MCM5, MCM7, CDC45, GINS2, GINS3,** and **DONSON**. Most disease is caused by biallelic hypomorphic alleles; heterozygous/de-novo **GMNN** disease is the important inheritance exception. The upstream defect is insufficient origin licensing or CMG-helicase assembly, followed by impaired S-phase progression, reduced proliferation and sometimes senescence/apoptosis in rapidly growing embryonic tissues. (nielsendandoroff2023theexpandinggenetic pages 1-2, mcquaid2022hypomorphicgins3variants pages 19-20, nielsendandoroff2023theexpandinggenetic pages 2-2)

The following structured summary highlights the most reusable evidence.

| domain | key finding | ontology-ready terms/IDs where confidently known | evidence type | key source/date/DOI |
|---|---|---|---|---|
| Disease definition / core triad | Meier-Gorlin syndrome (MGORS), previously called ear-patella-short stature syndrome, is a rare microcephalic primordial dwarfism classically defined by short stature, microtia, and patella hypo/aplasia; many patients also have genital anomalies and post-pubertal female mammary hypoplasia | Candidate disease ontology term: MONDO not confirmed here; phenotype terms confidently usable: short stature HP:0004322; microtia HP:0008551; patellar aplasia/hypoplasia candidate HPO term(s), exact ID not confirmed here; primordial dwarfism candidate term not confirmed here | Human disease review / cohort synthesis | Nielsen-Dandoroff et al., 2023, Eur J Hum Genet, published Apr 2023, https://doi.org/10.1038/s41431-023-01359-z (nielsendandoroff2023theexpandinggenetic pages 1-2) |
| Inheritance | Usually autosomal recessive; most disease genes act through biallelic hypomorphic variants; GMNN is an exception reported with autosomal dominant inheritance in the literature summarized by the review evidence | Autosomal recessive; autosomal dominant (GMNN exception) | Human genetics review | Nielsen-Dandoroff et al., 2023, https://doi.org/10.1038/s41431-023-01359-z; McQuaid et al., 2022, https://doi.org/10.1172/jci.insight.155648 (nielsendandoroff2023theexpandinggenetic pages 1-2, mcquaid2022hypomorphicgins3variants pages 19-20) |
| Causal gene set | 13 genes associated with MGORS/relevant MGORS spectrum: ORC1, ORC4, ORC6, CDT1, CDC6, GMNN, CDC45, DONSON, MCM3, MCM5, MCM7, GINS2, GINS3 | HGNC gene symbols listed; pre-RC / CMG-associated genes | Human review integrating primary studies | Nielsen-Dandoroff et al., 2023, https://doi.org/10.1038/s41431-023-01359-z (nielsendandoroff2023theexpandinggenetic pages 1-2, nielsendandoroff2023theexpandinggenetic pages 2-2) |
| Molecular mechanism | Core mechanism is defective DNA replication initiation/licensing and/or CMG helicase assembly, reducing loading of early replication machinery onto replication origins and impairing cellular proliferation during development | GO candidate terms: DNA replication initiation; DNA replication; replication origin licensing; CMG helicase complex assembly (exact GO IDs not confirmed here) | Human review + functional studies | Nielsen-Dandoroff et al., 2023, https://doi.org/10.1038/s41431-023-01359-z; Kingsley et al., 2023, https://doi.org/10.1093/nar/gkad694; Evrin et al., 2023, https://doi.org/10.15252/embr.202357677 (nielsendandoroff2023theexpandinggenetic pages 1-2, kingsley2023donsonfacilitatescdc45 pages 1-1) |
| Representative variant: GINS2 | Homozygous GINS2 NM_016095.2:c.341G>T, p.(Arg114Leu) causes MGORS with craniosynostosis; missense change affects a conserved residue at the CDC45/MCM5 docking site, likely disrupting CMG function | GINS2; missense variant; craniosynostosis phenotype term candidate, exact HPO ID not confirmed here | Human case + yeast functional modeling | Sá et al., 2022, J Med Genet, published Aug 2022, https://doi.org/10.1136/jmedgenet-2020-107572 (sa2022biallelicgins2variant pages 1-1, sa2022biallelicgins2variant pages 1-2) |
| Representative variant: GINS3 | Hypomorphic GINS3 variants affecting Asp24 cause an MGORS-like phenotype in 7 individuals from 5 families; effects include impaired proliferation, S-phase accumulation, reduced protein half-life, altered replisome interactions, and slower fork progression | GINS3; hypomorphic missense spectrum affecting Asp24 | Human genetics + in vitro + yeast + mouse | McQuaid et al., 2022, JCI Insight, published May 2022, https://doi.org/10.1172/jci.insight.155648 (mcquaid2022hypomorphicgins3variants pages 1-2) |
| Representative variant: CDT1 | Novel homozygous intronic CDT1 variant c.352-30A>C disrupts a branch point, causes exon 3 skipping on minigene assay, and expands the mutational spectrum to noncanonical splice/branch-point defects | CDT1; intronic/splicing variant; likely pathogenic by ACMG in study | Human case + minigene functional assay | Li et al., 2024, Orphanet J Rare Dis, published Dec 2024, https://doi.org/10.1186/s13023-024-03430-4 (li2024anovelhomozygous pages 9-10) |
| DONSON | DONSON is now established within the MGORS spectrum; 2023 studies show it is required for Cdc45 and GINS chromatin association and for CMG helicase assembly during S phase, explaining how DONSON variants cause disease | DONSON; CMG helicase assembly; replication initiation | Human review + Xenopus extract + mammalian cell studies | Kingsley et al., 2023, https://doi.org/10.1093/nar/gkad694; Evrin et al., 2023, https://doi.org/10.15252/embr.202357677; Nielsen-Dandoroff et al., 2023, https://doi.org/10.1038/s41431-023-01359-z (kingsley2023donsonfacilitatescdc45 pages 12-13, kingsley2023donsonfacilitatescdc45 pages 1-1, nielsendandoroff2023theexpandinggenetic pages 5-6) |
| Growth / phenotype statistics | Fewer than 100 cases were noted in the 2023 review; severe prenatal/postnatal growth failure is typical. In the 2024 review of molecularly defined cases, mean birth length was -3.9 SDS, birth weight -3.4 SDS, and adult height averaged -4.5 SDS; reported mean adult heights were 137.7 cm in females and 147.0 cm in males | short stature HP:0004322; intrauterine growth restriction candidate term not confirmed here; microcephaly candidate term not confirmed here | Human review / literature summary | Nielsen-Dandoroff et al., 2023, https://doi.org/10.1038/s41431-023-01359-z; Li et al., 2024, https://doi.org/10.1186/s13023-024-03430-4 (nielsendandoroff2023theexpandinggenetic pages 1-2, li2024anovelhomozygous pages 10-12) |
| Diagnostic phenotype threshold | At least two of the three core features are present in 97% of patients summarized in the GINS3 paper’s background review, supporting phenotype-driven suspicion even when the full triad is incomplete | short stature HP:0004322; microtia HP:0008551; patella aplasia/hypoplasia candidate HPO term(s) | Human literature synthesis | McQuaid et al., 2022, https://doi.org/10.1172/jci.insight.155648 (mcquaid2022hypomorphicgins3variants pages 1-2) |
| Growth hormone response | Evidence remains limited and off-label, but GH may benefit a subset: literature review of 12 treated patients found 58% (7/12) positive response; response was 100% in those with low IGF-1 and 50% in those with normal IGF-1 in the 2024 review dataset; no adverse reactions were reported in that review | Growth hormone treatment candidate NCIT term not confirmed here; IGF-1 biomarker candidate not mapped here | Human case + literature review | Li et al., 2024, https://doi.org/10.1186/s13023-024-03430-4 (li2024anovelhomozygous pages 10-12, li2024anovelhomozygous pages 9-10) |
| Model systems | Disease mechanism has been studied in zebrafish (ORC1 depletion causing MGS-like growth phenotype; H4K20me2 depletion reducing body size), mouse embryos/fibroblasts (GINS3 Asp24 models with growth retardation, lethality, senescence), budding yeast (GINS2/GINS3 ortholog assays), Xenopus egg extracts (DONSON-dependent CMG assembly), and Drosophila/other systems summarized in reviews | Cell/tissue candidates not fully resolved here; zebrafish NCBI Taxon candidate 7955; mouse 10090; Xenopus laevis 8355; budding yeast Saccharomyces cerevisiae 4932 | Model organism + in vitro + cell-free functional evidence | Kuo et al., 2012, https://doi.org/10.1038/nature10956; McQuaid et al., 2022, https://doi.org/10.1172/jci.insight.155648; Kingsley et al., 2023, https://doi.org/10.1093/nar/gkad694; Nielsen-Dandoroff et al., 2023, https://doi.org/10.1038/s41431-023-01359-z (mcquaid2022hypomorphicgins3variants pages 1-2, kingsley2023donsonfacilitatescdc45 pages 1-1, nielsendandoroff2023theexpandinggenetic pages 8-9) |
| Epigenetic link | ORC1 BAH domain recognizes H4K20me2, linking histone methylation to replication licensing; loss of this interaction impairs origin occupancy/chromatin loading and can produce an MGS-like growth phenotype in zebrafish | H4K20me2 as histone mark; ORC1 BAH domain | Structural biology + cell biology + zebrafish | Kuo et al., 2012, Nature, published Mar 2012, https://doi.org/10.1038/nature10956 (nielsendandoroff2023theexpandinggenetic pages 1-2) |
| Clinical-trial status | No disease-specific interventional MGORS trial was identified in the retrieved evidence; one broader observational registry is recruiting: Primordial Dwarfism Registry (NCT04569149), observational, target enrollment 200 | ClinicalTrials.gov: NCT04569149 | Registry / observational study | ClinicalTrials.gov entry NCT04569149, recruiting at retrieval time (trial search evidence) |


*Table: This table summarizes high-yield knowledge-base facts for Meier-Gorlin syndrome, including core definition, gene set, mechanism, representative variants, growth data, treatment signals, models, and trial status. It is designed for rapid curation and ontology-aware annotation while avoiding uncertain IDs.*

## 1. Disease information

### Definition and identifiers

MGORS was historically called **ear–patella–short stature syndrome**, **microtia–absent patellae–micrognathia syndrome**, and **Meier–Gorlin primordial dwarfism**. It is a congenital, lifelong Mendelian developmental disorder rather than an acquired endocrine growth disorder. (nielsendandoroff2023theexpandinggenetic pages 1-2, mcquaid2022hypomorphicgins3variants pages 1-2)

Recommended identifiers for curation are:

- **OMIM phenotype:** **224690**, Meier-Gorlin syndrome 1; OMIM also assigns gene-specific MGORS subtypes.
- **Orphanet:** **ORPHA:2554**.
- **MONDO:** commonly mapped to **MONDO:0012826**; this identifier should be checked against the release used by the target knowledge base.
- **ICD-10/ICD-11:** no uniquely specific MGORS code was identified; coding generally falls under congenital malformation or short-stature categories.
- **MeSH:** no dedicated disease descriptor was identified in the retrieved evidence; “Dwarfism” and “Microcephaly” are broader indexing concepts.

The evidence summarized here is **aggregated disease-level evidence** from published cohorts, case reports, reviews, and functional studies—not individual EHR data. The 2023 review is the most current broad synthesis; the December 2024 report adds a functionally validated CDT1 splice variant and treatment review. (nielsendandoroff2023theexpandinggenetic pages 1-2, li2024anovelhomozygous pages 9-10)

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factors

MGORS is genetic. Pathogenic variants impair proteins that license replication origins or assemble/activate the **CDC45–MCM2-7–GINS (CMG) helicase**. The disorder is therefore best understood as a developmental “replication-initiation disorder.” (nielsendandoroff2023theexpandinggenetic pages 2-2, nielsendandoroff2023theexpandinggenetic pages 1-2)

Most alleles are missense, splice-altering, or otherwise hypomorphic. Complete loss of an essential replication factor is frequently presumed incompatible with embryonic survival; accordingly, disease severity often reflects residual activity. A hypomorphic/hypomorphic combination tends to be less severe than a hypomorphic/null combination, although gene-specific exceptions and small sample sizes limit prediction. Approximately 20% of clinically diagnosed cases remained molecularly unresolved in one recent analysis. (sa2022biallelicgins2variant pages 1-1)

### Risk factors

- **Genetic:** biallelic pathogenic or likely pathogenic variants in the listed genes; parental consanguinity increases the probability of homozygosity but is not required.
- **Family history:** affected siblings and carrier parents are expected under recessive inheritance; recurrence risk is ordinarily 25% for each pregnancy when both parents carry the same autosomal-recessive condition.
- **Environmental, lifestyle, infectious, occupational, age, and sex-dependent acquisition risks:** none established. Sex changes the visibility of genital and mammary phenotypes, not the underlying genetic risk.

### Protective factors and gene–environment interactions

No validated protective variant, diet, lifestyle measure, toxin avoidance strategy, or infectious prophylaxis prevents MGORS after conception. No reproducible human gene–environment interaction has been demonstrated. Nicotinamide sensitivity in a **GINS2** yeast assay is a functional replication-stress readout, not evidence that dietary nicotinamide causes or modifies human MGORS. (sa2022biallelicgins2variant pages 1-1)

## 3. Phenotypes

### Core and associated phenotype set

| Phenotype | Type, onset, course | Frequency/severity evidence | Suggested HPO annotation |
|---|---|---|---|
| Prenatal growth restriction | Fetal sign; congenital; persistent into postnatal life | Mean birth length −3.9 SDS and weight −3.4 SDS in the 2024 synthesis | Intrauterine growth retardation; low birth weight |
| Short stature/primordial dwarfism | Physical sign; congenital/childhood; chronic, generally proportionate | Mean adult height approximately −4.5 SDS; reported means 137.7 cm in females and 147.0 cm in males | **HP:0004322 Short stature**, proportionate short stature |
| Microtia, often bilateral | Congenital structural sign; stable | One of the classic triad; severity variable | **HP:0008551 Microtia** |
| Patellar aplasia/hypoplasia | Congenital skeletal sign, sometimes recognized only when ossification permits imaging | Classic triad; can be incomplete or delayed diagnostically | Absent patella; patellar hypoplasia |
| Microcephaly | Congenital/developmental sign; generally proportionate to body size but can be marked | Variable by gene; MGORS is classified among microcephalic primordial dwarfisms | **HP:0000252 Microcephaly** |
| Mammary hypoplasia/agenesis | Pubertal physical manifestation | Reported as completely penetrant among evaluated post-pubertal females in the 2023 synthesis | Breast hypoplasia/aplasia |
| Genital anomalies | Congenital physical sign | Variable; may include cryptorchidism or hypoplastic external genitalia | Abnormality of genital system; cryptorchidism where applicable |
| Characteristic face | Congenital/evolving physical signs | Downslanting palpebral fissures, full lower lip, micrognathia; nasal prominence may increase with age | Downslanting palpebral fissures; full lower lip; micrognathia |
| Feeding/GI or respiratory difficulty | Symptom/complication, usually infancy | Variable; may materially affect early morbidity | Feeding difficulties; gastroesophageal reflux; respiratory distress as applicable |
| Developmental delay/intellectual disability | Neurodevelopmental phenotype | Variable and not obligatory; severe neurological involvement should prompt gene-specific interpretation or differential diagnosis | Global developmental delay; intellectual disability |
| Craniosynostosis | Congenital cranial sign | Enriched particularly in **CDC45**- and **GINS2**-related disease | Craniosynostosis; coronal craniosynostosis |
| Cardiac malformation | Congenital structural sign | Uncommon/variable; atrial septal defect documented in a GINS2 case | Congenital heart defect; atrial septal defect |

Growth figures are from aggregated molecularly characterized cases and must not be treated as population norms. (li2024anovelhomozygous pages 10-12, nielsendandoroff2023theexpandinggenetic pages 1-2, sa2022biallelicgins2variant pages 1-2)

### Functional and quality-of-life effects

Likely burdens include reduced mobility or knee instability from patellar defects, repeated orthopedic assessment, feeding support during infancy, surgeries for craniosynostosis or congenital anomalies, psychosocial effects of extreme short stature, and reproductive/body-image effects of genital or mammary hypoplasia. No validated MGORS-specific EQ-5D, SF-36, PROMIS, or quality-of-life cohort was found; quantitative claims would therefore be inappropriate.

## 4. Genetic and molecular information

### Causal genes and pathway position

- **Origin recognition/licensing:** **ORC1, ORC4, ORC6, CDC6, CDT1, GMNN**.
- **MCM helicase core:** **MCM3, MCM5, MCM7**.
- **CMG activation/assembly:** **CDC45, GINS2, GINS3, DONSON**.

The 2023 review counted 13 causal genes and emphasized that all converge on early DNA replication, although DONSON’s initiation role was only clarified in 2023. (nielsendandoroff2023theexpandinggenetic pages 1-2, kingsley2023donsonfacilitatescdc45 pages 1-1)

### Representative pathogenic variants

- **GINS2 NM_016095.2:c.341G>T, p.(Arg114Leu):** homozygous missense allele affecting a conserved CDC45/MCM5 docking interface. Yeast modeling showed increased sensitivity to replication interference; the human phenotype included coronal craniosynostosis, mild short stature, and patellar hypoplasia. (sa2022biallelicgins2variant pages 1-1, sa2022biallelicgins2variant pages 1-2)
- **GINS3 Asp24 variants:** hypomorphic variants were found in seven individuals from five families. They shorten protein half-life, alter replisome interactions, slow fork progression, reduce proliferation, and produce S-phase accumulation. (mcquaid2022hypomorphicgins3variants pages 1-2)
- **CDT1 NM_030928.4:c.352-30A>C:** homozygous deep-intronic/branch-point variant classified likely pathogenic by the authors (PS3, PM2, PP4); a minigene assay confirmed exon 3 skipping. (li2024anovelhomozygous pages 9-10)
- **ORC1:** pathogenic substitutions often affect the N-terminal BAH chromatin-binding domain; splice, frameshift, and deletion alleles can lower protein abundance. (nielsendandoroff2023theexpandinggenetic pages 2-2)
- **CDC45:** missense, splice, and an unusually prominent group of synonymous splice-altering variants occur; reduced protein abundance and craniosynostosis are recurrent observations. (nielsendandoroff2023theexpandinggenetic pages 5-6, nielsendandoroff2023theexpandinggenetic pages 1-2)
- **DONSON:** biallelic hypomorphic missense, splice, and deep-intronic variants can reduce nuclear localization or protein function. More severe biallelic DONSON disease overlaps microcephaly–micromelia syndrome/MISSLA, illustrating an allelic continuum. (nielsendandoroff2023theexpandinggenetic pages 5-6)

Variants are **constitutional germline** changes, not somatic drivers. Pathogenic alleles should generally be absent or extremely rare in population databases, but variant-specific gnomAD frequencies must be obtained from the relevant genome build and transcript rather than inferred from syndrome frequency.

### Modifiers, epigenetics, and chromosome abnormalities

No validated human modifier gene or MGORS-specific DNA-methylation episignature is established. The strongest epigenetic mechanistic link is that the ORC1 BAH domain recognizes **H4K20me2**; disruption decreases ORC1 origin occupancy, ORC chromatin loading, and cell-cycle progression. This is chromatin-mediated replication regulation, not evidence of an acquired epigenetic cause. No recurrent aneuploidy, translocation, inversion, or pathogenic copy-number syndrome defines MGORS, although deletions involving a causal gene can act as one allele.

## 5. Environmental information

No toxin, radiation exposure, pollutant, occupation, diet, smoking, alcohol use, exercise pattern, or infectious agent is known to cause or trigger MGORS. Environmental and infectious-agent sections are therefore **not applicable as primary etiology**. Standard nutrition, vaccination, and avoidance of tobacco/alcohol remain general health measures but are not disease prevention.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream germline defect:** a hypomorphic replication-factor allele reduces protein level, stability, localization, chromatin interaction, or complex binding.
2. **Origin licensing/activation defect:** ORC–CDC6–CDT1 loading of MCM2-7, or subsequent CDC45/GINS recruitment, becomes inefficient.
3. **CMG and S-phase dysfunction:** fewer origins fire, replication forks progress abnormally, and cells accumulate in S phase or experience replication stress.
4. **Cellular outcome:** reduced proliferation, prolonged cell cycle, senescence and, in severe contexts, apoptosis or embryonic lethality.
5. **Developmental outcome:** rapidly expanding embryonic progenitor populations generate fewer cells, producing global growth restriction and tissue-selective malformations of ear, patella, skull, genitalia, and mammary tissue. (mcquaid2022hypomorphicgins3variants pages 1-2, nielsendandoroff2023theexpandinggenetic pages 1-2)

The 2023 DONSON work filled an important mechanistic gap: DONSON is dispensable for MCM loading in G1 but required in S phase for CDC45/GINS association and active CMG assembly. Xenopus egg extracts and mammalian-cell experiments independently support this conclusion. (kingsley2023donsonfacilitatescdc45 pages 12-13, kingsley2023donsonfacilitatescdc45 pages 1-1)

### Suggested ontology annotations

- **GO biological process:** DNA replication initiation; DNA replication origin licensing; DNA unwinding involved in DNA replication; cell-cycle S phase; regulation of mitotic cell cycle; cellular response to DNA replication stress; cellular senescence.
- **GO cellular component:** nucleus; chromatin; replication fork; origin recognition complex; MCM complex; CMG complex/replisome.
- **Candidate cell types (CL):** embryonic fibroblast; chondrocyte and chondrocyte progenitor; osteoblast; cranial neural-crest-derived mesenchymal cell; mammary epithelial progenitor; neural progenitor. These are biologically plausible developmental targets, but direct cell-type-resolved human evidence is limited.

### Omics and advanced technologies

Patient-cell protein abundance, interaction, cell-cycle, and replication-fork assays provide the strongest molecular profiles. No validated diagnostic metabolomic, lipidomic, bulk-transcriptomic, single-cell, spatial-transcriptomic, or integrated multi-omic signature was identified. A 2024 computational “progeria phenome” study clustered MGORS with progeroid disorders, but this is hypothesis-generating rather than proof that MGORS is clinically a premature-aging syndrome. (worm2024definingtheprogeria pages 10-11)

## 7. Anatomical structures affected

Primary structures include the whole-body skeleton/growth plate, external ear, patella/knee, skull sutures, brain/head, external genitalia, testes, and mammary gland. Secondary or variably involved systems include gastrointestinal, respiratory, cardiac, and neurodevelopmental systems. Most structural abnormalities are bilateral or generalized; microtia and patellar changes may nevertheless be asymmetric.

Suggested mappings include **UBERON:0001690 ear**, patella, knee, skull suture, mammary gland, external genitalia, testis, brain, and growth plate. At the subcellular level, the principal sites are **nucleus, chromatin, replication origin, replication fork, and replisome**, not mitochondria, lysosomes, or extracellular matrix.

## 8. Temporal development and natural history

Onset is prenatal and insidious, with fetal growth restriction often detectable by ultrasound. Microtia and genital anomalies are apparent at birth; patellar hypoplasia may not be radiographically obvious until later childhood because of normal ossification timing. Growth failure persists throughout childhood, while mammary hypoplasia becomes assessable only at puberty. Facial nasal prominence may become more evident with age. (nielsendandoroff2023theexpandinggenetic pages 1-2)

MGORS is chronic and lifelong, not episodic or relapsing-remitting. There are no standardized stages or spontaneous remission. Critical windows include prenatal development, infancy for feeding/respiratory support, childhood for growth and orthopedic surveillance, and puberty for sexual development and mammary assessment. Severe combinations can cause prenatal or neonatal lethality, but lethality is unusual in classic surviving MGORS. (nielsendandoroff2023theexpandinggenetic pages 2-2)

## 9. Inheritance and population characteristics

The usual inheritance pattern is **autosomal recessive** with variable expressivity. Penetrance for a molecularly severe biallelic genotype appears high, but gene- and feature-specific penetrance cannot be estimated reliably from fewer than 100 published cases. Mammary hypoplasia was completely penetrant among evaluated post-pubertal females in the available synthesis. (nielsendandoroff2023theexpandinggenetic pages 1-2)

No anticipation is known. Parental germline mosaicism is theoretically relevant to apparently de-novo cases but is not a defining feature. Founder variants may occur in individual consanguineous or geographically restricted families, but no universal founder population was identified. Carrier frequency, incidence, sex ratio, and prevalence per 100,000 are unknown; the published-case count must not be converted into population prevalence. Both sexes and multiple ancestries are affected. Consanguinity increases case ascertainment for recessive forms but non-consanguineous families are well documented, including the GINS2 family. (sa2022biallelicgins2variant pages 1-1)

## 10. Diagnostics

### Clinical evaluation

Diagnostic suspicion should arise with severe prenatal/postnatal proportionate short stature plus microtia and/or absent/hypoplastic patellae. Recommended evaluation includes serial length/height, weight and head circumference; detailed dysmorphology; knee examination and age-appropriate radiographs; hearing assessment; feeding/respiratory review; genital examination; pubertal and endocrine assessment; and targeted cardiac, renal, gastrointestinal, or cranial imaging when indicated.

No enzyme assay, circulating protein, metabolite, liquid biopsy, EEG, EMG, or biopsy is diagnostic. IGF-1 and growth-hormone-axis testing can evaluate coincident endocrine abnormalities and treatment candidacy but do not establish MGORS.

### Molecular testing algorithm

1. Use a **primordial dwarfism/short-stature panel** containing all 13 genes, or exome/genome sequencing with copy-number analysis.
2. Confirm likely causal variants and phase them in parents.
3. Analyze splice effects, including synonymous and noncanonical intronic variants; RNA studies or minigene assays may be necessary.
4. If exome/panel testing is negative, prefer genome sequencing or targeted deep-intronic/CNV analysis. The CDT1 branch-point case demonstrates why exome-centered pipelines may miss causal intronic variants. (li2024anovelhomozygous pages 9-10)

CMA can detect a deletion involving a causal gene but is not a first-line standalone diagnostic test. Karyotyping, FISH, mitochondrial-DNA testing, and repeat-expansion testing have no routine role unless another diagnosis is suspected.

### Differential diagnosis

Important alternatives include Seckel syndrome, microcephalic osteodysplastic primordial dwarfism types I/III and II, Silver–Russell syndrome, 3-M syndrome, SHORT syndrome, mandibulofacial dysostosis with microcephaly, and other replication disorders. Microtia plus absent/hypoplastic patellae strongly favors MGORS; cerebrovascular disease is more characteristic of PCNT-related MOPD II, and Silver–Russell syndrome more often shows relative macrocephaly and body asymmetry.

### Screening

MGORS is not included in population newborn screening. Cascade carrier testing, prenatal diagnosis by chorionic-villus sampling/amniocentesis, and preimplantation genetic testing are possible after familial variants are identified.

## 11. Outcome and prognosis

No robust 5-year survival, mortality rate, or life-expectancy estimate exists. Many classically affected individuals survive into adulthood; lethality is rare in typical MGORS but can occur with severe allelic combinations. Major morbidity arises from extreme short stature, feeding or respiratory problems, orthopedic dysfunction, craniosynostosis, genital anomalies, and variable developmental involvement. (nielsendandoroff2023theexpandinggenetic pages 2-2)

Potential prognostic factors include causal gene, residual protein function, null-versus-hypomorphic allele combination, severity of prenatal growth restriction, microcephaly, respiratory compromise, and major congenital anomalies. **CDC45/GINS2** variants raise concern for craniosynostosis; broader GINS/MCM disorders can overlap immunodeficiency, although this is not universal MGORS. No validated molecular prognostic biomarker or risk calculator exists. (sa2022biallelicgins2variant pages 4-5, sa2022biallelicgins2variant pages 1-1)

## 12. Treatment and current applications

There is no approved disease-modifying drug, gene therapy, RNA therapy, cell therapy, or replication-targeted therapy. Management is individualized and multidisciplinary:

- nutritional and feeding support, including reflux management;
- respiratory care when required;
- audiology and hearing intervention;
- physical/occupational therapy and orthopedic management of patellar/knee dysfunction;
- craniofacial/neurosurgical treatment of clinically significant craniosynostosis;
- endocrine monitoring, pubertal support, and management of genital anomalies;
- developmental assessment and educational intervention;
- cardiac or other organ-specific treatment.

Suggested NCIT intervention concepts include **Genetic Counseling**, **Physical Therapy**, **Occupational Therapy**, **Nutritional Support**, **Hearing Aid**, **Surgical Procedure**, and **Growth Hormone Therapy**; exact NCIT codes should be resolved against the implementation release.

### Growth hormone

GH is off-label and evidence is limited to case reports/series. In a 2024 review of 12 treated children, mean treatment-start age was 3.7±1.2 years, baseline height −5.9±1.2 SDS, and treatment duration 4.8±2.9 years. Seven of 12 (58%) were considered responders; five gained a mean 2.2±0.9 height SDS and two had accelerated growth velocity. The index CDT1 patient’s velocity increased from 4.0 to an average 6.2 cm/year over five years. No adverse reactions were reported in that small literature set, but long-term safety and final-height efficacy remain uncertain. (li2024anovelhomozygous pages 10-12, li2024anovelhomozygous pages 9-10)

No MGORS-specific interventional trial was identified. **NCT04569149**, the recruiting Primordial Dwarfism Registry, is observational with planned enrollment of 200 and may improve natural-history knowledge.

## 13. Prevention

Primary prevention by lifestyle modification or vaccination is impossible because MGORS is inherited. Meaningful prevention consists of reproductive genetics: carrier/cascade testing, counseling about recurrence, prenatal molecular diagnosis, donor gametes, or preimplantation genetic testing.

Secondary prevention means early recognition of fetal growth restriction and the microtia–patella phenotype, followed by molecular diagnosis and surveillance. Tertiary prevention includes early nutrition and respiratory support, monitoring cranial sutures and hearing, orthopedic therapy, developmental services, and endocrine/puberty follow-up. Routine immunization remains appropriate but is not MGORS-specific prophylaxis.

## 14. Other species and natural disease

No well-established naturally occurring veterinary counterpart, breed predisposition, zoonotic transmission, or cross-species infectious susceptibility was found. MGORS is noncommunicable and has no zoonotic potential. Orthologs of the causal replication genes are deeply conserved across eukaryotes, enabling comparative functional modeling rather than veterinary case surveillance.

Relevant taxa include **Homo sapiens** (NCBI Taxon 9606), **Mus musculus** (10090), **Danio rerio** (7955), **Drosophila melanogaster** (7227), **Xenopus laevis** (8355), and **Saccharomyces cerevisiae** (4932).

## 15. Model organisms and experimental systems

- **Zebrafish:** ORC1 depletion causes an MGORS-like small-body phenotype; wild-type human ORC1, but not H4K20me2-binding-defective ORC1, rescues growth. H4K20me2 depletion also reduces body size, connecting chromatin recognition to organismal growth.
- **Mouse:** embryos homozygous for GINS3 Asp24-associated alleles show intrauterine growth retardation and fail to survive to birth; embryonic fibroblasts undergo accelerated senescence. This recapitulates growth failure but is more severe than many surviving humans. (mcquaid2022hypomorphicgins3variants pages 1-2, nielsendandoroff2023theexpandinggenetic pages 6-7)
- **Budding yeast:** engineered PSF3/GINS3 variants impair growth, S-phase progression, and protein stability; GINS2 p.Arg114Leu sensitizes cells to replication interference. Yeast provides strong conserved-function evidence but cannot model mammalian ears, patellae, or mammary development. (mcquaid2022hypomorphicgins3variants pages 1-2, sa2022biallelicgins2variant pages 1-1)
- **Xenopus egg extracts:** DONSON depletion prevents Cdc45/GINS recruitment and active CMG assembly; add-back experiments permit functional testing of patient substitutions. This is a powerful biochemical system but not a whole-organism phenotype model. (kingsley2023donsonfacilitatescdc45 pages 12-13, kingsley2023donsonfacilitatescdc45 pages 1-1)
- **Drosophila and patient-derived cells:** replication-factor variants and depletion models support conserved cell-cycle dysfunction; fibroblasts, HEK-293T minigene assays, and mammalian stem cells are used for protein-level, splicing, localization, and replication phenotyping. (nielsendandoroff2023theexpandinggenetic pages 8-9, li2024anovelhomozygous pages 9-10)

## Recent developments and evidence appraisal

The most consequential 2023 advance was the demonstration that DONSON is a missing mammalian CMG-assembly factor rather than merely a downstream fork-stability protein. The 2024 CDT1 report broadened the diagnostic variant spectrum to branch-point defects and provided the most quantitative—but still low-certainty—GH synthesis. Recent interactome work also showed that a disease-associated CDC45 mutation can disrupt a nuclear-localization signal, supporting protein-localization defects as an additional pathogenic route. (li2024anovelhomozygous pages 9-10, kingsley2023donsonfacilitatescdc45 pages 12-13, kingsley2023donsonfacilitatescdc45 pages 1-1)

### Representative abstract quotations

- Nielsen-Dandoroff et al. (published April 2023): “**Previously known as ear-patella short stature syndrome, MGORS is characterized by growth delay, microtia, and patella hypo/aplasia, as well as genital abnormalities, and breast agenesis in females.**” DOI: https://doi.org/10.1038/s41431-023-01359-z. (nielsendandoroff2023theexpandinggenetic pages 1-2)
- McQuaid et al. (published May 2022): “**Taken together, our findings implicate GINS3 in the pathogenesis of MGS and support the notion that hypomorphic variants identified in this gene impaired cell and organismal growth by compromising DNA replication.**” DOI: https://doi.org/10.1172/jci.insight.155648. (mcquaid2022hypomorphicgins3variants pages 1-2)
- Kingsley et al. (published August 2023): “**DONSON’s presence is essential for replication initiation as it is required for Cdc45 and GINS association with Mcm2–7 complexes and helicase activation.**” DOI: https://doi.org/10.1093/nar/gkad694. (kingsley2023donsonfacilitatescdc45 pages 1-1)
- Li et al. (published December 2024): “**GH therapy may be beneficial for height outcomes in children with MGORS with normal IGF-1 levels.**” This conclusion is based on only 12 literature cases and should be considered preliminary. DOI: https://doi.org/10.1186/s13023-024-03430-4. (li2024anovelhomozygous pages 10-12, li2024anovelhomozygous pages 9-10)

## Principal knowledge gaps

Reliable incidence/prevalence, age- and gene-stratified penetrance, adult survival, fertility, quality of life, cancer risk, standardized treatment outcomes, variant-specific population frequencies, and prospective GH safety are not established. There are also no validated clinical biomarkers, disease-specific omics signature, cell-type-resolved human atlas, natural-animal disease, or disease-modifying trial. The small, genetically heterogeneous literature means that quantitative frequencies should be stored with cohort size, ascertainment method, and publication date rather than as universal disease constants.

References

1. (nielsendandoroff2023theexpandinggenetic pages 1-2): Emily Nielsen-Dandoroff, Mischa S. G. Ruegg, and Louise S. Bicknell. The expanding genetic and clinical landscape associated with meier-gorlin syndrome. European Journal of Human Genetics, 31:859-868, Apr 2023. URL: https://doi.org/10.1038/s41431-023-01359-z, doi:10.1038/s41431-023-01359-z. This article has 45 citations and is from a domain leading peer-reviewed journal.

2. (mcquaid2022hypomorphicgins3variants pages 1-2): Mary E. McQuaid, Kashif Ahmed, Stephanie Tran, Justine Rousseau, Ranad Shaheen, Kristin D. Kernohan, Kyoko E. Yuki, Prerna Grover, Ema S. Dreseris, Sameen Ahmed, Lucie Dupuis, Jennifer Stimec, Mary Shago, Zuhair N. Al-Hassnan, Roch Tremblay, Philipp G. Maass, Michael D. Wilson, Eyal Grunebaum, Kym M. Boycott, François-Michel Boisvert, Sateesh Maddirevula, Eissa A. Faqeih, Fahad Almanjomi, Zaheer Ullah Khan, Fowzan S. Alkuraya, Philippe M. Campeau, Peter Kannu, Eric I. Campos, and Hugo Wurtele. Hypomorphic gins3 variants alter dna replication and cause meier-gorlin syndrome. JCI Insight, May 2022. URL: https://doi.org/10.1172/jci.insight.155648, doi:10.1172/jci.insight.155648. This article has 25 citations and is from a domain leading peer-reviewed journal.

3. (mcquaid2022hypomorphicgins3variants pages 19-20): Mary E. McQuaid, Kashif Ahmed, Stephanie Tran, Justine Rousseau, Ranad Shaheen, Kristin D. Kernohan, Kyoko E. Yuki, Prerna Grover, Ema S. Dreseris, Sameen Ahmed, Lucie Dupuis, Jennifer Stimec, Mary Shago, Zuhair N. Al-Hassnan, Roch Tremblay, Philipp G. Maass, Michael D. Wilson, Eyal Grunebaum, Kym M. Boycott, François-Michel Boisvert, Sateesh Maddirevula, Eissa A. Faqeih, Fahad Almanjomi, Zaheer Ullah Khan, Fowzan S. Alkuraya, Philippe M. Campeau, Peter Kannu, Eric I. Campos, and Hugo Wurtele. Hypomorphic gins3 variants alter dna replication and cause meier-gorlin syndrome. JCI Insight, May 2022. URL: https://doi.org/10.1172/jci.insight.155648, doi:10.1172/jci.insight.155648. This article has 25 citations and is from a domain leading peer-reviewed journal.

4. (nielsendandoroff2023theexpandinggenetic pages 2-2): Emily Nielsen-Dandoroff, Mischa S. G. Ruegg, and Louise S. Bicknell. The expanding genetic and clinical landscape associated with meier-gorlin syndrome. European Journal of Human Genetics, 31:859-868, Apr 2023. URL: https://doi.org/10.1038/s41431-023-01359-z, doi:10.1038/s41431-023-01359-z. This article has 45 citations and is from a domain leading peer-reviewed journal.

5. (kingsley2023donsonfacilitatescdc45 pages 1-1): Georgia Kingsley, Aggeliki Skagia, Paolo Passaretti, Cyntia Fernandez-Cuesta, Alicja Reynolds-Winczura, Kinga Koscielniak, and Agnieszka Gambus. Donson facilitates cdc45 and gins chromatin association and is essential for dna replication initiation. Nucleic Acids Research, 51:9748-9763, Aug 2023. URL: https://doi.org/10.1093/nar/gkad694, doi:10.1093/nar/gkad694. This article has 39 citations and is from a highest quality peer-reviewed journal.

6. (sa2022biallelicgins2variant pages 1-1): Maria J Nabais Sá, Kerry A Miller, Mary McQuaid, Nils Koelling, Andrew O M Wilkie, Hugo Wurtele, Arjan P M de Brouwer, and Jorge Oliveira. Biallelic gins2 variant p.(arg114leu) causes meier-gorlin syndrome with craniosynostosis. Journal of Medical Genetics, 59:776-780, Aug 2022. URL: https://doi.org/10.1136/jmedgenet-2020-107572, doi:10.1136/jmedgenet-2020-107572. This article has 26 citations and is from a domain leading peer-reviewed journal.

7. (sa2022biallelicgins2variant pages 1-2): Maria J Nabais Sá, Kerry A Miller, Mary McQuaid, Nils Koelling, Andrew O M Wilkie, Hugo Wurtele, Arjan P M de Brouwer, and Jorge Oliveira. Biallelic gins2 variant p.(arg114leu) causes meier-gorlin syndrome with craniosynostosis. Journal of Medical Genetics, 59:776-780, Aug 2022. URL: https://doi.org/10.1136/jmedgenet-2020-107572, doi:10.1136/jmedgenet-2020-107572. This article has 26 citations and is from a domain leading peer-reviewed journal.

8. (li2024anovelhomozygous pages 9-10): Qing Li, Yichi Wu, Fucheng Meng, Zhu-xi Li, Di Zhan, and Xiaoping Luo. A novel homozygous intronic variant in cdt1 that alters splicing causes meier–gorlin syndrome, and a review of published mutations and growth hormone treatments. Orphanet Journal of Rare Diseases, Dec 2024. URL: https://doi.org/10.1186/s13023-024-03430-4, doi:10.1186/s13023-024-03430-4. This article has 1 citations and is from a peer-reviewed journal.

9. (kingsley2023donsonfacilitatescdc45 pages 12-13): Georgia Kingsley, Aggeliki Skagia, Paolo Passaretti, Cyntia Fernandez-Cuesta, Alicja Reynolds-Winczura, Kinga Koscielniak, and Agnieszka Gambus. Donson facilitates cdc45 and gins chromatin association and is essential for dna replication initiation. Nucleic Acids Research, 51:9748-9763, Aug 2023. URL: https://doi.org/10.1093/nar/gkad694, doi:10.1093/nar/gkad694. This article has 39 citations and is from a highest quality peer-reviewed journal.

10. (nielsendandoroff2023theexpandinggenetic pages 5-6): Emily Nielsen-Dandoroff, Mischa S. G. Ruegg, and Louise S. Bicknell. The expanding genetic and clinical landscape associated with meier-gorlin syndrome. European Journal of Human Genetics, 31:859-868, Apr 2023. URL: https://doi.org/10.1038/s41431-023-01359-z, doi:10.1038/s41431-023-01359-z. This article has 45 citations and is from a domain leading peer-reviewed journal.

11. (li2024anovelhomozygous pages 10-12): Qing Li, Yichi Wu, Fucheng Meng, Zhu-xi Li, Di Zhan, and Xiaoping Luo. A novel homozygous intronic variant in cdt1 that alters splicing causes meier–gorlin syndrome, and a review of published mutations and growth hormone treatments. Orphanet Journal of Rare Diseases, Dec 2024. URL: https://doi.org/10.1186/s13023-024-03430-4, doi:10.1186/s13023-024-03430-4. This article has 1 citations and is from a peer-reviewed journal.

12. (nielsendandoroff2023theexpandinggenetic pages 8-9): Emily Nielsen-Dandoroff, Mischa S. G. Ruegg, and Louise S. Bicknell. The expanding genetic and clinical landscape associated with meier-gorlin syndrome. European Journal of Human Genetics, 31:859-868, Apr 2023. URL: https://doi.org/10.1038/s41431-023-01359-z, doi:10.1038/s41431-023-01359-z. This article has 45 citations and is from a domain leading peer-reviewed journal.

13. (worm2024definingtheprogeria pages 10-11): Cecilie Worm, Maya Elena Ramirez Schambye, Garik V. Mkrtchyan, Alexander Veviorskiy, Anastasia Shneyderman, Ivan V. Ozerov, Alex Zhavoronkov, Daniela Bakula, and Morten Scheibye-Knudsen. Defining the progeria phenome. Aging (Albany NY), 16:2026-2046, Feb 2024. URL: https://doi.org/10.18632/aging.205537, doi:10.18632/aging.205537. This article has 11 citations.

14. (sa2022biallelicgins2variant pages 4-5): Maria J Nabais Sá, Kerry A Miller, Mary McQuaid, Nils Koelling, Andrew O M Wilkie, Hugo Wurtele, Arjan P M de Brouwer, and Jorge Oliveira. Biallelic gins2 variant p.(arg114leu) causes meier-gorlin syndrome with craniosynostosis. Journal of Medical Genetics, 59:776-780, Aug 2022. URL: https://doi.org/10.1136/jmedgenet-2020-107572, doi:10.1136/jmedgenet-2020-107572. This article has 26 citations and is from a domain leading peer-reviewed journal.

15. (nielsendandoroff2023theexpandinggenetic pages 6-7): Emily Nielsen-Dandoroff, Mischa S. G. Ruegg, and Louise S. Bicknell. The expanding genetic and clinical landscape associated with meier-gorlin syndrome. European Journal of Human Genetics, 31:859-868, Apr 2023. URL: https://doi.org/10.1038/s41431-023-01359-z, doi:10.1038/s41431-023-01359-z. This article has 45 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Meier-Gorlin_Syndrome-deep-research-falcon_artifacts/artifact-00.md)