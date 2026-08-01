---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T17:39:28.503036'
end_time: '2026-07-31T17:50:37.866504'
duration_seconds: 669.36
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CAPOS Syndrome
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
  path: CAPOS_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CAPOS Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CAPOS Syndrome** covering all of the
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
- **Disease Name:** CAPOS Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CAPOS Syndrome** covering all of the
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


# CAPOS syndrome: comprehensive disease-characteristics report

## Executive summary

CAPOS syndrome is an ultra-rare, autosomal-dominant ATP1A3-related neurologic disorder. Its name denotes **cerebellar ataxia, areflexia, pes cavus, optic atrophy, and sensorineural hearing loss**. The classic course begins with fever-associated episodes of acute encephalopathy/ataxia in childhood, followed by incomplete recovery and variably progressive auditory, visual, cerebellar, and peripheral-neurologic impairment. The overwhelmingly characteristic molecular lesion is heterozygous **ATP1A3 c.2452G>A, p.(Glu818Lys), abbreviated E818K**. Presentations may be incomplete: progressive auditory neuropathy can precede or dominate the neurologic syndrome. Fewer than 100 affected people had been reported worldwide by 2021, so phenotype frequencies, prevalence, survival, penetrance, and treatment-effect estimates remain imprecise. (wang2021auditoryneuropathyas pages 5-6, han2017atp1a3mutationscan pages 1-2, wang2021auditoryneuropathyas pages 1-2)

| Domain | Curated finding | Suggested ontology/identifier | Evidence strength |
|---|---|---|---|
| Identity / IDs | CAPOS syndrome = cerebellar ataxia, areflexia, pes cavus, optic atrophy, sensorineural hearing loss; disease-level knowledge here is derived from aggregated literature and registry-style resources plus individual case series/case reports (OpenTargets Search: CAPOS syndrome, han2017atp1a3mutationscan pages 1-2) | MONDO:0011038; Orphanet:1171; OMIM:601338/601388 as reported in literature nomenclature; synonym: cerebellar ataxia-areflexia-pes cavus-optic atrophy-sensorineural hearing loss syndrome | Moderate |
| Causal gene / variant | CAPOS is strongly linked to heterozygous ATP1A3 variants, with canonical recurrent c.2452G>A, p.Glu818Lys (p.E818K); Open Targets lists ATP1A3 as the associated target for MONDO:0011038/Orphanet:1171 (OpenTargets Search: CAPOS syndrome, wang2021auditoryneuropathyas pages 5-6, han2017atp1a3mutationscan pages 1-2) | ATP1A3; ENSG00000105409; HGNC:806; variant: NM_152296.5:c.2452G>A; p.Glu818Lys | Strong |
| Inheritance | Usually autosomal dominant with many de novo cases; familial recurrence also reported in CAPOS families; de novo status was confirmed in Chinese auditory-neuropathy/CAPOS cases by trio confirmation methods (wang2021auditoryneuropathyas pages 5-6, wang2021auditoryneuropathyas pages 1-2, han2017atp1a3mutationscan pages 3-5) | Autosomal dominant inheritance; germline heterozygous | Strong |
| Core phenotype | Core acronym features are cerebellar ataxia, areflexia, pes cavus, optic atrophy, and sensorineural hearing loss/auditory neuropathy; neurologic findings can include dysarthria, nystagmus/abnormal eye movements, visual disturbance, and variable weakness (wang2021auditoryneuropathyas pages 5-6, han2017atp1a3mutationscan pages 1-2, han2017atp1a3mutationscan pages 3-5, han2017atp1a3mutationscan pages 2-3) | HPO: Ataxia HP:0001251; Areflexia HP:0001284; Pes cavus HP:0001761; Optic atrophy HP:0000648; Sensorineural hearing impairment HP:0000407; Dysarthria HP:0001260; Nystagmus HP:0000639 | Strong |
| Temporal course / triggers | Typical onset is childhood with acute neurologic deterioration during or after febrile illness; residual deficits may persist and hearing/optic findings may progress over years; one reported patient had 15-year follow-up with delayed neurologic progression and progressive bilateral SNHL (wang2021auditoryneuropathyas pages 5-6, wang2021auditoryneuropathyas pages 1-2, han2017atp1a3mutationscan pages 2-3) | HPO: Episodic ataxia HP:0001250; Fever-triggered/precipitated episodes (free-text trigger annotation); Childhood onset HP:0011463 | Moderate-strong |
| Auditory phenotype and tests | Auditory neuropathy spectrum disorder can be an initial or dominant phenotype; characteristic testing includes preserved otoacoustic emissions with absent/delayed ABR, plus PTA/SDS/ECochG; some carriers have mild neurologic signs so ATP1A3 testing is useful in progressive post-lingual ANSD (han2017atp1a3mutationscan pages 1-2, wang2021auditoryneuropathyas pages 1-2, han2017atp1a3mutationscan pages 2-3) | HPO: Auditory neuropathy HP:0031869; ABR; OAE; pure-tone audiometry; electrocochleography | Strong |
| Cochlear implantation | CI outcomes are variable: one study reported remarkable or favorable short-term benefit in auditory synaptopathy cases, while another CAPOS/ATP1A3 p.E818K patient had poor CI outcome; benefit may depend on lesion site and phenotype severity (han2017atp1a3mutationscan pages 1-2, han2017atp1a3mutationscan pages 5-6, wang2021auditoryneuropathyas pages 1-2, han2017atp1a3mutationscan pages 3-5) | NCIT: Cochlear Implantation; Hearing aid device/supportive intervention | Moderate |
| Mechanism / pathophysiology | ATP1A3 encodes neuron-enriched Na+/K+-ATPase alpha-3 (NKAα3), required for rapid restoration of intracellular Na+ and membrane potential after neuronal firing; ATP1A3 dysfunction is inferred to impair excitability recovery and synaptic transmission, contributing to paroxysmal episodes and chronic neurologic dysfunction (han2017atp1a3mutationscan pages 5-6) | GO: sodium ion transmembrane transport; GO: membrane potential maintenance; protein: Na+/K+-transporting ATPase subunit alpha-3 | Moderate |
| Anatomy / cell types | Evidence particularly supports auditory system involvement: NKAα3 is abundant in type I afferent terminals contacting inner hair cells, spiral ganglion somata, and medial efferent terminals at outer hair cells; broader CAPOS manifestations implicate cerebellum, optic nerve, and peripheral reflex pathways (han2017atp1a3mutationscan pages 5-6) | UBERON: inner ear/cochlea, cerebellum, optic nerve; CL: spiral ganglion neuron, auditory afferent neuron; HPO mappings above | Moderate |
| Epidemiology / demographics | CAPOS is ultra-rare; a 2021 report stated fewer than 100 patients worldwide, and a 2017 paper referred to the 10th CAPOS family and 27th patient in the literature; reported across multiple ancestries including Korean and Chinese cases (wang2021auditoryneuropathyas pages 5-6, han2017atp1a3mutationscan pages 5-6, wang2021auditoryneuropathyas pages 1-2) | Orphan disease / rare disease designation | Moderate |
| Diagnostics | Recommended confirmation is molecular testing for ATP1A3, often by NGS/WES followed by Sanger confirmation; in auditory presentations, add neurologic exam, ABR/OAE/audiometry, and consider MRI/temporal bone imaging to exclude structural causes; imaging may be anatomically normal (wang2021auditoryneuropathyas pages 1-2, han2017atp1a3mutationscan pages 3-5, han2017atp1a3mutationscan pages 2-3) | ATP1A3 single-gene testing; multigene neurologic/hearing-loss panel; WES/WGS; ABR; OAE; MRI | Strong |
| Differential diagnosis | Differential includes other ATP1A3-related disorders such as alternating hemiplegia of childhood and rapid-onset dystonia-parkinsonism, as well as inherited/idiopathic ataxia plus auditory neuropathy disorders; CAPOS is distinguished by the p.Glu818Lys hotspot and characteristic hearing/visual syndrome (han2017atp1a3mutationscan pages 1-2, han2017atp1a3mutationscan pages 3-5) | ATP1A3-related disorders umbrella; AHC; RDP | Moderate |
| Treatment / management | No CAPOS-specific disease-modifying therapy was identified in gathered evidence; current care is supportive and rehabilitative, including hearing aids/CI when appropriate, neurologic follow-up, and management around febrile-triggered episodes by trigger avoidance/rapid fever treatment is biologically plausible but not directly protocolized in the retrieved CAPOS studies (wang2021auditoryneuropathyas pages 1-2, han2017atp1a3mutationscan pages 3-5) | NCIT: Supportive Care; Rehabilitation; Cochlear Implantation | Limited-moderate |
| Trial / research status | No interventional CAPOS-specific therapeutic trial was identified; one ATP1A3 natural-history observational study includes CAPOS phenotypes: NCT03857607, prospective cohort, planned enrollment 100, focused on disease progression and benchmarking for future therapies (NCT03857607 chunk 1) | ClinicalTrials.gov: NCT03857607 | Moderate |
| Model organisms | A 2021 ATP1A3 model review noted that available animal models mainly cover other ATP1A3 disorders; no published CAPOS-specific animal model was identified in gathered evidence (ng2021geneticallyalteredanimal pages 12-12) | Disease Models & Mechanisms review; ATP1A3 model-organism resources | Limited |
| Major evidence gaps | No robust CAPOS-specific prevalence/incidence, penetrance, sex ratio, survival/life-expectancy, validated QoL measures, standardized treatment algorithm, biomarker panel, or CAPOS-specific omics/epigenetic dataset was found in gathered evidence; CI evidence remains case-based and heterogeneous (han2017atp1a3mutationscan pages 3-5, NCT03857607 chunk 1) | Evidence gap annotation | Strong for absence in retrieved evidence |


*Table: This table condenses the highest-confidence CAPOS syndrome findings from the gathered evidence into a knowledge-base friendly format. It highlights what is well-supported, what is only moderately supported, and where major evidence gaps remain.*

## Evidence scope and limitations

This report integrates aggregated disease-level resources with published human cases, small case series, functional studies, and a trial registry. The strongest CAPOS-specific human evidence available here is Han et al., published November 2017, DOI [10.1038/s41598-017-16676-9](https://doi.org/10.1038/s41598-017-16676-9), and Wang et al., published October 2021, DOI [10.3389/fcell.2021.749484](https://doi.org/10.3389/fcell.2021.749484). Recent 2024 publications describe additional cases, fluctuating symptoms, hearing loss, and the broader ATP1A3 spectrum, but retrievable full evidence was sparse; consequently, they do not yet supersede the core genotype–phenotype evidence. Claims about broader ATP1A3 biology are explicitly distinguished from direct E818K/CAPOS findings.

## 1. Disease information

**Definition.** CAPOS is a Mendelian neurogenetic syndrome characterized by childhood, often fever-triggered cerebellar attacks and a chronic combination of ataxia, absent reflexes, cavus feet, optic atrophy, and sensorineural hearing loss—frequently an auditory-neuropathy-spectrum disorder (ANSD). The phenotype belongs to the continuous spectrum of ATP1A3-related neurologic disease. (wang2021auditoryneuropathyas pages 5-6, han2017atp1a3mutationscan pages 1-2)

**Identifiers and synonyms.** Recommended identifiers are **MONDO:0011038** and **Orphanet:1171**. Open Targets associates this disease with ATP1A3 alone. Common names are *CAPOS syndrome*, *cerebellar ataxia–areflexia–pes cavus–optic atrophy–sensorineural hearing loss syndrome*, and, when pes cavus is absent, *CAOS syndrome*. OMIM commonly indexes CAPOS as **601338**; ATP1A3 is OMIM **182350**. No dedicated MeSH term or specific ICD-10/ICD-11 code was established in the retrieved evidence; coding generally requires broader hereditary ataxia, hearing-loss, optic-atrophy, or rare-disease categories. (OpenTargets Search: CAPOS syndrome, han2017atp1a3mutationscan pages 1-2, ng2021geneticallyalteredanimal pages 12-12)

The evidence is primarily **aggregated disease-level literature derived from individual patients and pedigrees**, not population EHR data. The small number of reported families makes publication and ascertainment bias substantial.

## 2. Etiology

### Causal and genetic factors

CAPOS is caused by a heterozygous germline pathogenic missense variant in **ATP1A3**, most consistently **NM_152296:c.2452G>A, p.(Glu818Lys)**. Han et al. reported E818K in all nine unrelated CAPOS families then documented, whereas later studies showed that the same allele can produce incomplete CAPOS or apparently isolated postlingual auditory neuropathy. The variant is often **de novo**, although vertical transmission in autosomal-dominant families occurs. (han2017atp1a3mutationscan pages 5-6, wang2021auditoryneuropathyas pages 1-2, han2017atp1a3mutationscan pages 3-5)

**Risk factors.** Possession of the pathogenic ATP1A3 allele is the necessary major risk factor. Fever/febrile infection is a recurrent **attack trigger**, not an infectious cause of the inherited disease. Family history increases prior probability, but its absence does not exclude CAPOS because recurrent de novo mutation is common. No validated susceptibility loci, modifier genes, sex effect, toxic exposure, diet, smoking, alcohol, or occupational risks have been demonstrated. (wang2021auditoryneuropathyas pages 5-6, han2017atp1a3mutationscan pages 5-6)

**Protective factors.** No genetic protective allele or proven environmental protective factor is known. Prompt antipyresis and avoidance of overheating are rational precautions, but controlled evidence showing prevention of permanent deficits is unavailable.

**Gene–environment interaction.** The clinically important interaction is ATP1A3 dysfunction plus fever/systemic stress. Increased neuronal metabolic and firing demand during febrile illness plausibly exceeds the reduced reserve of Na⁺/K⁺-ATPase α3, precipitating acute dysfunction. This chain is biologically coherent but has not been quantitatively proven for E818K in a temperature-controlled human model.

## 3. Phenotypes

| Phenotype | Pattern and impact | Suggested HPO term |
|---|---|---|
| Episodic cerebellar ataxia | Usually childhood onset; abrupt deterioration during/after fever; episodes may include lethargy, dysarthria and nystagmus; recovery can be incomplete | Ataxia **HP:0001251**; episodic ataxia **HP:0001250** |
| Chronic gait/limb ataxia | Variable residual or progressive impairment; affects walking, balance and independence | Cerebellar ataxia **HP:0001251** |
| Areflexia/hyporeflexia | Common defining sign, sometimes subclinical; may be the only neurologic clue in auditory-predominant disease | Areflexia **HP:0001284**; hyporeflexia **HP:0001265** |
| Sensorineural hearing loss/ANSD | Postlingual or childhood onset, usually bilateral and progressive; impaired speech understanding can be disproportionate to pure-tone threshold | Sensorineural hearing impairment **HP:0000407**; auditory neuropathy **HP:0031869** |
| Optic atrophy/visual dysfunction | Variable onset and progression; visual disturbance and abnormal eye movements may occur | Optic atrophy **HP:0000648**; visual impairment **HP:0000505** |
| Pes cavus | Chronic structural manifestation, not obligatory and potentially late | Pes cavus **HP:0001761** |
| Dysarthria | Episodic or residual cerebellar manifestation; impairs communication | Dysarthria **HP:0001260** |
| Nystagmus/opsoclonus | May accompany attacks or chronic ocular-motor dysfunction | Nystagmus **HP:0000639**; opsoclonus **HP:0010543** |
| Weakness/encephalopathy | Can occur during severe febrile episodes; frequency is unknown | Muscle weakness **HP:0001324**; encephalopathy **HP:0001298** |

In Han et al., three p.E818K subjects had onset ranging from age 3 years to the third decade. One child had fever-triggered attacks; adult auditory-predominant cases demonstrated that onset and expressivity can be much broader. In Wang et al., all four subjects had AN, two had neurologic manifestations sufficient for CAPOS, and two children aged six and eight years had not yet developed neurologic symptoms. A 15-year follow-up documented delayed neurologic events and progressive bilateral hearing loss. These observations support age-dependent and variable expression but do not provide population-level phenotype frequencies. (wang2021auditoryneuropathyas pages 1-2, han2017atp1a3mutationscan pages 3-5)

Quality-of-life burden is likely driven by combined communication, vision, balance, mobility, education, and employment limitations. However, no CAPOS-specific EQ-5D, SF-36, PROMIS, disability-weight, or caregiver-burden study was identified.

## 4. Genetic and molecular information

**Gene.** ATP1A3, encoding Na⁺/K⁺-transporting ATPase α3; Ensembl **ENSG00000105409**. The CAPOS association is strong and disease-specific in Open Targets. (OpenTargets Search: CAPOS syndrome)

**Variant.** c.2452G>A, p.Glu818Lys is a heterozygous germline missense change and is regarded as pathogenic for CAPOS. It is recurrent across ancestries and commonly de novo, consistent with a mutational hotspot rather than a founder allele. The retrieved studies did not provide a numerical gnomAD/TOPMed allele frequency; its repeated de novo occurrence and ultra-rare disease association imply absence or extreme rarity in reference populations. It is not a somatic cancer variant in this context. (han2017atp1a3mutationscan pages 5-6)

**Functional consequence.** ATP1A3 pathogenic variants generally reduce catalytic/pump-current function and alter ion affinity. Direct E818K-specific biophysical data in the retrieved material were limited, so CAPOS should be annotated conservatively as **impaired α3 Na⁺/K⁺ pump function**, not as a proven dominant-negative, gain-of-function leak, or complete loss-of-function state. (han2017atp1a3mutationscan pages 5-6)

No validated CAPOS modifier gene, methylation signature, histone/chromatin abnormality, repeat expansion, mitochondrial-DNA lesion, or structural chromosome abnormality has been established. CMA, karyotyping and FISH therefore have low expected diagnostic yield for classic CAPOS unless a separate genomic disorder is suspected.

## 5. Environmental information

CAPOS is not caused by toxin, radiation, pollution, occupation, diet, smoking, alcohol, or an infectious agent. **Febrile infection acts as a physiologic trigger** for attacks in genetically susceptible individuals. No specific pathogen has been implicated, and CAPOS is neither communicable nor zoonotic. Data are insufficient to define effects of exercise, sleep deprivation, emotional stress, anesthesia, or specific medications, although such stressors may be relevant across ATP1A3 disorders.

## 6. Mechanism and pathophysiology

ATP1A3 encodes the neuron-enriched α3 catalytic subunit of the plasma-membrane Na⁺/K⁺-ATPase. The pump uses ATP to export Na⁺ and import K⁺, restoring ionic gradients and membrane potential after neuronal firing. α3 is particularly important during high-frequency activity and high intracellular Na⁺ load. (han2017atp1a3mutationscan pages 5-6)

**Proposed causal chain:** germline E818K → reduced or dysregulated α3 pump reserve → delayed restoration of neuronal Na⁺/K⁺ gradients after activity → altered membrane excitability and synaptic transmission → acute network failure during fever/metabolic stress → episodic cerebellar/encephalopathic manifestations; repeated or persistent dysfunction may contribute to chronic auditory, optic, cerebellar, and peripheral-neural deficits. The first clinical and final anatomic links are supported in human CAPOS; the intermediate cellular chain partly relies on broader ATP1A3 evidence. (han2017atp1a3mutationscan pages 5-6)

In the auditory system, NKAα3 is abundant in type-I afferent terminals contacting inner hair cells, spiral-ganglion somata, and efferent terminals near outer hair cells. Pharmacologic inhibition abolished cochlear compound action potentials without reducing endocochlear potential, supporting a neural/synaptic rather than hair-cell-mechanical lesion. This explains preserved otoacoustic emissions with abnormal auditory brainstem responses and motivates the term **auditory synaptopathy/neuropathy**. (han2017atp1a3mutationscan pages 5-6)

Suggested annotations include GO *sodium ion transmembrane transport*, *potassium ion transmembrane transport*, *maintenance of membrane potential*, *ATP hydrolysis-coupled ion transport*, and *regulation of neuronal action potential*; cellular component: **plasma membrane** and **Na⁺/K⁺-ATPase complex**. Suggested cells include neuron, cerebellar neuron/Purkinje cell, auditory afferent neuron, spiral-ganglion neuron, retinal ganglion cell/optic-nerve axon, and peripheral sensory or motor neuron. Purkinje-, retinal-, and peripheral-neuron assignments are anatomically plausible but not resolved by CAPOS-specific single-cell data.

No CAPOS-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, CRISPR-screen, or multi-omic signature was identified. Immune activation is not a primary mechanism; fever is a stressor. Oxidative stress, apoptosis, and neurodegeneration remain possible downstream processes but are not established E818K biomarkers.

## 7. Anatomical structures affected

Primary systems are neurologic, auditory and visual. Principal sites are the **cerebellum** (UBERON:0002037), **cochlea/inner ear**, auditory nerve and spiral ganglion, **optic nerve** (UBERON:0000965), and peripheral reflex arcs. Pes cavus reflects secondary chronic neuromuscular imbalance in the foot. Hearing loss and optic atrophy are generally bilateral; no consistent lateralization is known. (han2017atp1a3mutationscan pages 5-6)

At subcellular level, the relevant compartment is the neuronal **plasma membrane**, where α3 participates in the Na⁺/K⁺-ATPase complex. CAPOS is not primarily a mitochondrial, lysosomal, nuclear, or endoplasmic-reticulum disease.

## 8. Temporal development

The classic pattern is pediatric and episodic: acute or subacute neurologic deterioration follows fever, often beginning in infancy or childhood. Attacks may become less prominent with age, while residual ataxia, areflexia, hearing loss, optic atrophy, and foot deformity persist or progress. Auditory neuropathy can instead appear as a postlingual, slowly progressive presentation in adolescence or adulthood. (wang2021auditoryneuropathyas pages 5-6, han2017atp1a3mutationscan pages 3-5)

The disease is lifelong and does not have validated stages. A useful descriptive framework is: (1) presymptomatic genetically affected period; (2) initial febrile attack or auditory presentation; (3) recurrent attacks with incomplete recovery; and (4) chronic multisensory/motor disability. No established spontaneous or treatment-induced remission pattern exists. Childhood febrile episodes may represent a critical period because deficits can accumulate, but prospective evidence is lacking.

## 9. Inheritance and population

Inheritance is **autosomal dominant**, with both de novo and familial heterozygous cases. Expressivity is highly variable and likely age-dependent: the same E818K allele can produce classic CAPOS, incomplete CAPOS, or auditory-predominant disease. Formal penetrance estimates, germline-mosaicism rate, anticipation, carrier frequency, and consanguinity effects are unknown. Anticipation is not expected for a missense disorder. (han2017atp1a3mutationscan pages 5-6, wang2021auditoryneuropathyas pages 1-2)

CAPOS is ultra-rare. A 2017 publication described the tenth family and 27th reported patient; a 2021 report stated that fewer than 100 patients had been reported worldwide. No reliable prevalence per 100,000, annual incidence, sex ratio, or age distribution is available. Cases from European-ancestry, Korean, and Chinese families argue against a geographically restricted founder effect. (wang2021auditoryneuropathyas pages 5-6, han2017atp1a3mutationscan pages 5-6)

## 10. Diagnostics

Diagnosis requires recognition of the phenotype and molecular confirmation of a heterozygous pathogenic ATP1A3 variant. For classic CAPOS, targeted sequencing for c.2452G>A is efficient. An ATP1A3-containing ataxia, movement-disorder, auditory-neuropathy, or hearing-loss panel is appropriate for incomplete presentations. WES or WGS is useful when the phenotype is atypical or initial panel testing is negative; Sanger sequencing should confirm the variant and test parents. (wang2021auditoryneuropathyas pages 1-2, han2017atp1a3mutationscan pages 3-5)

Clinical assessment should include neurologic examination, gait/coordination, deep-tendon reflexes, foot morphology, ophthalmology with optic-disc and visual-function assessment, and serial audiology. ANSD testing includes pure-tone and speech audiometry, otoacoustic emissions, ABR and, where indicated, electrocochleography/EABR. Preserved OAE with absent or delayed ABR supports auditory neuropathy. Temporal-bone CT/MRI may exclude cochlear-nerve or structural abnormalities; reported ATP1A3 auditory-neuropathy cases had intact cochlear nerves and no explanatory anatomic lesion. Routine blood chemistry, CSF, biopsy, EEG, EMG/NCS, or metabolic testing is not diagnostic, although these may exclude alternatives. (wang2021auditoryneuropathyas pages 1-2, han2017atp1a3mutationscan pages 2-3)

Differential diagnosis includes alternating hemiplegia of childhood, rapid-onset dystonia-parkinsonism, relapsing encephalopathy with cerebellar ataxia and other ATP1A3 phenotypes; episodic ataxias; mitochondrial disease; hereditary sensory neuropathies; OPA1-related optic-atrophy-plus disease; Friedreich and other hereditary ataxias; and genetic auditory neuropathies. E818K plus the auditory/optic/areflexic phenotype strongly favors CAPOS, but phenotype overlap means genotype should not be interpreted from the acronym alone. (OpenTargets Search: CAPOS syndrome, han2017atp1a3mutationscan pages 3-5)

Population or newborn screening is not established. Once a pathogenic familial variant is known, cascade testing, prenatal diagnosis, and preimplantation genetic testing are technically feasible. Predictive testing of minors requires counseling because onset and severity are variable.

## 11. Outcome and prognosis

CAPOS generally causes chronic morbidity rather than a documented reduction in survival. No five- or ten-year survival, mortality rate, or life-expectancy estimate is available. Major long-term burdens are progressive hearing impairment, optic dysfunction, gait ataxia, falls, areflexia, cavus-foot complications, dysarthria, and cumulative disability after attacks. The 15-year observation reported by Wang et al. illustrates delayed neurologic manifestations and progressive bilateral hearing loss. (wang2021auditoryneuropathyas pages 1-2)

Recovery from an acute attack can be incomplete. Prognosis is individually unpredictable; earlier onset, repeated severe febrile attacks, progressive hearing loss and optic atrophy plausibly indicate greater disability, but no validated prognostic model or biomarker exists. Normal early neurologic examination does not guarantee that later CAPOS features will not emerge.

## 12. Treatment

There is **no approved disease-modifying, genotype-targeted, gene, cell, RNA, immunologic, or pump-correcting therapy** for CAPOS. Treatment is multidisciplinary and symptom-directed:

* promptly assess and treat fever and dehydration; avoid overheating where practical—reasonable tertiary prevention, although not trial-proven;
* physical and occupational therapy, balance/fall prevention, mobility aids, and orthotic/podiatric management for pes cavus;
* speech-language therapy for dysarthria and communication support;
* serial ophthalmology and low-vision services;
* hearing aids when useful, with formal CI candidacy assessment for severe ANSD;
* educational, psychosocial and genetic-counseling support.

Suggested NCIT intervention concepts are **Supportive Care**, **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, **Hearing Aid**, **Cochlear Implantation**, and **Genetic Counseling**.

CI outcomes are heterogeneous. Han et al. reported two auditory-synaptopathy subjects reaching approximately **90–94% K-CID speech-recognition scores three months after implantation**, with continued improvement in one. Conversely, Wang et al. reported poor outcome in one implanted CAPOS patient. Thus, E818K does not guarantee benefit; lesion localization, cochlear-nerve integrity, duration of auditory deprivation and neurologic severity should inform individualized counseling. (han2017atp1a3mutationscan pages 5-6, wang2021auditoryneuropathyas pages 1-2, han2017atp1a3mutationscan pages 3-5)

No CAPOS-specific pharmacogenomic recommendation or controlled medication response rate was identified. The prospective observational **Natural History Study of ATP1A3-related Disease**, [NCT03857607](https://clinicaltrials.gov/study/NCT03857607), planned 100 participants aged 6 months–60 years, included CAPOS and measured one-year progression. It was designed to establish natural-history benchmarks, not test treatment. (NCT03857607 chunk 1)

## 13. Prevention

The pathogenic allele cannot currently be prevented after conception. Primary prevention consists of informed reproductive counseling: an affected heterozygous parent generally has a 50% transmission risk per pregnancy, while recurrence after an apparently de novo event is low but not zero because parental germline mosaicism cannot be excluded. Prenatal or preimplantation testing can be offered when the familial variant is known.

Secondary prevention includes cascade testing of relatives, prospective neurologic/audiologic/ophthalmologic surveillance, and early rehabilitation. Tertiary prevention includes prompt fever management, hydration, avoidance of excessive heat, hearing and vision support, fall prevention, and treatment of orthopedic complications. No vaccine specifically prevents CAPOS; routine vaccination remains appropriate because preventing febrile infections may reduce trigger exposure, but vaccine-specific CAPOS outcome data are absent.

## 14. Other species and natural disease

No naturally occurring veterinary CAPOS homolog, breed predisposition, cross-species transmission, or zoonotic potential was identified. ATP1A3 orthologs are evolutionarily conserved in vertebrates and invertebrate Na⁺/K⁺-ATPase systems, supporting comparative functional research, but this is not evidence of naturally occurring CAPOS in animals. Relevant taxa for experimental work include *Mus musculus* (NCBI Taxon 10090), *Danio rerio* (7955), *Drosophila melanogaster* (7227), and *Caenorhabditis elegans* (6239).

## 15. Model organisms

ATP1A3-related disorders have been investigated using knock-in/knockout mice, zebrafish, Drosophila, *C. elegans*, and transfected cells. These systems model altered excitability, motor abnormalities, developmental effects and reduced pump function. However, a 2021 review explicitly noted the absence of a published **CAPOS/E818K-specific animal model** at that time; existing models primarily represent alternating hemiplegia, rapid-onset dystonia-parkinsonism, or generic ATP1A3 deficiency. Therefore, their mechanistic relevance to CAPOS is indirect. (ng2021geneticallyalteredanimal pages 12-12)

A 2024 cellular/zebrafish study of ATP1A3 p.Ala275Pro found reduced transcript/protein abundance and Na⁺/K⁺-ATPase activity with movement abnormalities, but that allele causes AHC/RDP rather than CAPOS and must not be treated as direct E818K evidence. CAPOS research priorities include an E818K knock-in model, patient-derived iPSC auditory and cerebellar neurons, temperature-stress experiments, rescue assays, and longitudinal genotype-linked biomarkers.

## Key evidence quotations

* Han et al. reported that two of three sporadic progressive-hearing-loss subjects with ANSD shared a de novo E818K allele and that CI produced “**remarkable benefits**” in one subject; this supports ATP1A3 as a cause of progressive auditory synaptopathy but not uniform CI success. (han2017atp1a3mutationscan pages 1-2)
* Wang et al. stated: “**During the 15 years follow-up of patient 1, we observed delayed neurological events and progressive bilateral sensorineural hearing loss**,” directly supporting delayed and progressive expression. (wang2021auditoryneuropathyas pages 1-2)
* The ATP1A3 model review characterized these conditions as a “**phenotypic continuum of rare neurological disorders**” and emphasized that their molecular mechanisms remain poorly understood, accurately framing both spectrum overlap and current uncertainty. (ng2021geneticallyalteredanimal pages 12-12)

## Knowledge-base conclusions

CAPOS should be represented as **MONDO:0011038**, an autosomal-dominant ATP1A3 α3 Na⁺/K⁺-pump disorder strongly associated with germline c.2452G>A/p.Glu818Lys. Its defining biology is impaired neuronal ionic-gradient recovery, with especially strong human evidence for auditory synaptopathy. Fever-triggered childhood attacks and progressive hearing/optic dysfunction are central, but incomplete and adult auditory-predominant presentations are recognized. Molecular testing is definitive; management remains supportive. Major unmet needs are prospective prevalence and penetrance estimates, standardized outcomes, CAPOS-specific functional models and omics, validated prevention protocols, and interventional trials.

References

1. (wang2021auditoryneuropathyas pages 5-6): Wenjia Wang, Jin Li, Lan Lan, Linyi Xie, Fen Xiong, Jing Guan, Hongyang Wang, and Qiuju Wang. Auditory neuropathy as the initial phenotype for patients with atp1a3 c.2452 g > a: genotype–phenotype study and ci management. Frontiers in Cell and Developmental Biology, Oct 2021. URL: https://doi.org/10.3389/fcell.2021.749484, doi:10.3389/fcell.2021.749484. This article has 14 citations.

2. (han2017atp1a3mutationscan pages 1-2): Kyu-Hee Han, Doo-Yi Oh, Seungmin Lee, Chung Lee, Jin Hee Han, Min Young Kim, Hye-Rim Park, Moo Kyun Park, Nayoung K. D. Kim, Jaekwang Lee, Eunyoung Yi, Jong-Min Kim, Jeong-Whun Kim, Jong-Hee Chae, Seung Ha Oh, Woong-Yang Park, and Byung Yoon Choi. Atp1a3 mutations can cause progressive auditory neuropathy: a new gene of auditory synaptopathy. Scientific Reports, Nov 2017. URL: https://doi.org/10.1038/s41598-017-16676-9, doi:10.1038/s41598-017-16676-9. This article has 69 citations and is from a peer-reviewed journal.

3. (wang2021auditoryneuropathyas pages 1-2): Wenjia Wang, Jin Li, Lan Lan, Linyi Xie, Fen Xiong, Jing Guan, Hongyang Wang, and Qiuju Wang. Auditory neuropathy as the initial phenotype for patients with atp1a3 c.2452 g > a: genotype–phenotype study and ci management. Frontiers in Cell and Developmental Biology, Oct 2021. URL: https://doi.org/10.3389/fcell.2021.749484, doi:10.3389/fcell.2021.749484. This article has 14 citations.

4. (OpenTargets Search: CAPOS syndrome): Open Targets Query (CAPOS syndrome, 14 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (han2017atp1a3mutationscan pages 3-5): Kyu-Hee Han, Doo-Yi Oh, Seungmin Lee, Chung Lee, Jin Hee Han, Min Young Kim, Hye-Rim Park, Moo Kyun Park, Nayoung K. D. Kim, Jaekwang Lee, Eunyoung Yi, Jong-Min Kim, Jeong-Whun Kim, Jong-Hee Chae, Seung Ha Oh, Woong-Yang Park, and Byung Yoon Choi. Atp1a3 mutations can cause progressive auditory neuropathy: a new gene of auditory synaptopathy. Scientific Reports, Nov 2017. URL: https://doi.org/10.1038/s41598-017-16676-9, doi:10.1038/s41598-017-16676-9. This article has 69 citations and is from a peer-reviewed journal.

6. (han2017atp1a3mutationscan pages 2-3): Kyu-Hee Han, Doo-Yi Oh, Seungmin Lee, Chung Lee, Jin Hee Han, Min Young Kim, Hye-Rim Park, Moo Kyun Park, Nayoung K. D. Kim, Jaekwang Lee, Eunyoung Yi, Jong-Min Kim, Jeong-Whun Kim, Jong-Hee Chae, Seung Ha Oh, Woong-Yang Park, and Byung Yoon Choi. Atp1a3 mutations can cause progressive auditory neuropathy: a new gene of auditory synaptopathy. Scientific Reports, Nov 2017. URL: https://doi.org/10.1038/s41598-017-16676-9, doi:10.1038/s41598-017-16676-9. This article has 69 citations and is from a peer-reviewed journal.

7. (han2017atp1a3mutationscan pages 5-6): Kyu-Hee Han, Doo-Yi Oh, Seungmin Lee, Chung Lee, Jin Hee Han, Min Young Kim, Hye-Rim Park, Moo Kyun Park, Nayoung K. D. Kim, Jaekwang Lee, Eunyoung Yi, Jong-Min Kim, Jeong-Whun Kim, Jong-Hee Chae, Seung Ha Oh, Woong-Yang Park, and Byung Yoon Choi. Atp1a3 mutations can cause progressive auditory neuropathy: a new gene of auditory synaptopathy. Scientific Reports, Nov 2017. URL: https://doi.org/10.1038/s41598-017-16676-9, doi:10.1038/s41598-017-16676-9. This article has 69 citations and is from a peer-reviewed journal.

8. (NCT03857607 chunk 1):  Natural History Study of ATP1A3-related Disease. Institute of Child Health. 2018. ClinicalTrials.gov Identifier: NCT03857607

9. (ng2021geneticallyalteredanimal pages 12-12): Hannah W. Y. Ng, Jennifer A. Ogbeta, and Steven J. Clapcote. Genetically altered animal models for atp1a3-related disorders. Disease Models & Mechanisms, Oct 2021. URL: https://doi.org/10.1242/dmm.048938, doi:10.1242/dmm.048938. This article has 15 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](CAPOS_Syndrome-deep-research-falcon_artifacts/artifact-00.md)