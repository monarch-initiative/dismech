---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T17:22:09.512261'
end_time: '2026-07-31T17:29:47.692541'
duration_seconds: 458.18
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: MICPCH Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 24
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: MICPCH_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MICPCH Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MICPCH Syndrome** covering all of the
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
- **Disease Name:** MICPCH Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MICPCH Syndrome** covering all of the
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


# MICPCH syndrome: disease-characteristics research report

## Executive summary

Microcephaly with pontine and cerebellar hypoplasia (MICPCH) is a rare, usually de novo X-linked neurodevelopmental disorder caused principally by loss-of-function variants or deletions involving **CASK** at Xp11.4. The characteristic course in females is normal or near-normal head size at birth, developmental delay emerging during infancy, progressive postnatal microcephaly, severe intellectual and motor disability, and disproportionate pontine/cerebellar hypoplasia. Hemizygous males generally have a much more severe epileptic encephalopathy; surviving less-severely affected males often have hypomorphic or mosaic variants. No disease-modifying therapy or registered interventional trial was identified; present implementation is molecular diagnosis, genetic counseling, and multidisciplinary supportive care. Recent 2023–2024 work emphasizes that CASK disease is mechanistically heterogeneous, involving splice-dependent protein functions, selective cerebellar granule-cell degeneration, and altered synaptic excitation/inhibition rather than one simple developmental pathway. (mukherjee2022thenonlinearpath pages 2-3, mori2023diverseclinicalphenotypes pages 2-5, patel2024geneticevidencefor pages 1-3)

| Domain | Key findings | Ontology / identifier suggestions | Key statistics / notes | Evidence |
|---|---|---|---|---|
| Definition / identifiers | MICPCH = microcephaly with pontine and cerebellar hypoplasia; rare X-linked neurodevelopmental disorder within the CASK-related disorder spectrum, usually defined at disease level from aggregated resources plus patient-level case/cohort reports. OMIM explicitly cited as **300749** in recent literature. | OMIM: 300749; Gene: **CASK**; disease label: microcephaly with pontine and cerebellar hypoplasia syndrome | 2023 review summarized 49 reports and 197 patients across CASK-related disorders. | (zhang2022adenovo pages 7-10, mori2023diverseclinicalphenotypes pages 2-5) |
| Cause / inheritance | Primary cause is **loss-of-function or hypomorphic pathogenic variants in CASK** on Xp11.4; includes nonsense, frameshift/indel, splice, missense, and copy-number loss. Inheritance is usually **de novo X-linked dominant** in females; hemizygous males are often much more severely affected, and **somatic mosaicism** can permit survival with milder disease in males. | HGNC gene suggestion: CASK; inheritance: X-linked dominant / X-linked semidominant; variant consequence: loss of function | In 41-patient MICPCH cohort, causative/candidate aberrations in **37/41 (90.2%)**; **32/41** involved CASK, including **23 point mutations** and **9 CNVs**. | (hayashi2017comprehensiveinvestigationof pages 2-3, hayashi2017comprehensiveinvestigationof pages 1-2, hayashi2017comprehensiveinvestigationof pages 4-6) |
| Hallmark phenotypes and frequencies | Core phenotype: severe developmental delay/intellectual disability, postnatal progressive microcephaly, hypotonia or motor disorder, and pontocerebellar hypoplasia. Additional features can include dystonia, scoliosis, epilepsy, ophthalmologic abnormalities, hearing loss, growth retardation, and feeding difficulties. Suggested HPO terms: Microcephaly (HP:0000252), Progressive microcephaly (HP:0000253), Cerebellar hypoplasia (HP:0001321), Pontine hypoplasia (HP:0007366), Global developmental delay (HP:0001263), Severe intellectual disability (HP:0010864), Seizure (HP:0001250), Hypotonia (HP:0001252), Dystonia (HP:0001332), Sensorineural hearing impairment (HP:0000407), Optic atrophy/hypoplasia (HP:0000648/HP:0008058), Feeding difficulties (HP:0011968), Scoliosis (HP:0002650). | HPO terms as listed | Burglen 2012: **13/14** screened PCH patients had CASK abnormalities; in those 13, epilepsy in **4/13**, hearing loss in **2/13**; severe microcephaly **< -6 SD in 7**, **-3 to -4 SD in 4**. Hayashi 2017: only **6/41** could walk and **3/41** could speak. Review-level estimate: seizures occur in about **40%** of cases. | (mukherjee2022thenonlinearpath pages 2-3, burglen2012spectrumofpontocerebellar pages 7-9, hayashi2017comprehensiveinvestigationof pages 2-3) |
| MRI / neuroradiology | Typical MRI shows **pontine and cerebellar hypoplasia**, often with variable vermian and hemispheric involvement and relative preservation of supratentorial structures compared with classic neurodegenerative PCH. Corpus callosum is often normal or relatively spared; a low brain-to-corpus-callosum ratio has been suggested as a clue to CASK-related disease. | UBERON suggestions: cerebellum (UBERON:0002037), pons (UBERON:0000988), corpus callosum (UBERON:0000955), brainstem (UBERON:0002298) | van Dijk 2021 included **6 MICPCH** patients and found severe cerebellar hypoplasia at birth with nearly absent postnatal growth, but without the caudate/ventricular changes seen in PCH1B/PCH2A. Burglen 2012 found universal brainstem/cerebellar hypoplasia in affected individuals. | (burglen2012spectrumofpontocerebellar pages 7-9, zhang2022adenovo pages 7-10) |
| Diagnosis | Diagnosis is clinical-radiologic plus molecular: suspect in infants/children, especially females, with postnatal progressive microcephaly, severe developmental delay, and PCH-like MRI. Recommended testing emphasizes **broad genomic testing** (WES/WGS or neurodevelopmental/PCH panels) plus CNV analysis because both sequence variants and deletions occur. Differential diagnosis includes other genetic causes of radiologic PCH and non-CASK monogenic/chromosomal etiologies. | Diagnostic concepts: WES, WGS, CNV analysis, multigene panel; HPO-driven genomic analysis | Hayashi 2017 showed high yield with combined genomic investigation: **37/41 (90.2%)** solved/candidate; Zakaria 2024 emphasized broad testing because classic OMIM-listed PCH genes explain only a minority of radiologic PCH cases. | (hayashi2017comprehensiveinvestigationof pages 2-3, hayashi2017comprehensiveinvestigationof pages 1-2) |
| Mechanism / pathophysiology | CASK is a **MAGUK scaffold protein** with CaMK, L27, PDZ, SH3, and GuK domains and roles in synaptic organization, protein interactions, and nuclear transcriptional regulation (including TBR1/CINAP-related pathways affecting **GRIN2B/GluN2B** and **RELN**). Human and mouse evidence supports a mixed mechanism: developmental hindbrain malformation plus **post-developmental cerebellar granule-cell vulnerability/degeneration**; neuronal CASK deficiency can also disrupt **excitatory/inhibitory synaptic balance** via GluN2B downregulation, and metabolic stress/oxidative metabolism defects may contribute. Suggested GO terms: synapse organization, regulation of excitatory postsynaptic potential, cerebellar granule cell development/survival, regulation of gene expression, cellular respiration. Suggested CL terms: cerebellar granule cell, Purkinje cell, cortical pyramidal neuron, astrocyte. | GO / CL suggestions as listed; cellular compartments: synapse, nucleus, cytoplasm | Mori 2019 showed GluN2B rescue corrected E/I imbalance in CASK-deficient neurons. Srivastava 2016 suggested non-cell-autonomous postnatal brain growth effects and metabolic abnormalities. Patel 2024 supports splice-dependent forebrain vs hindbrain functional differences. | (patel2024geneticevidencefor pages 1-3, patel2024geneticevidencefor pages 9-11, mori2019deficiencyofcalciumcalmodulindependent pages 1-2, patel2024geneticevidencefor pages 3-4, patel2024geneticevidencefor pages 14-16, patel2024geneticevidencefor pages 11-12) |
| Management / real-world care | No disease-modifying therapy is established. Current care is **supportive and multidisciplinary**: developmental therapies, nutritional/feeding support, seizure management, audiology/hearing support, ophthalmology, orthopedic monitoring for scoliosis, and genetic counseling. | NCIT suggestions: Supportive Care, Physical Therapy, Occupational Therapy, Speech Therapy, Anticonvulsant Therapy, Gastrostomy, Hearing Aid Device, Genetic Counseling | Clinical-trial search identified **no relevant interventional MICPCH/CASK trials** in available tool output. Preclinical concepts (e.g., targeting GluN2B pathways or metabolic dysfunction) remain experimental, not standard care. | (mukherjee2022thenonlinearpath pages 2-3, mori2019deficiencyofcalciumcalmodulindependent pages 1-2, patel2024geneticevidencefor pages 3-4) |
| Prognosis / outcomes | Prognosis is dominated by lifelong severe neurodevelopmental impairment. Females often have a non-progressive or slowly evolving developmental encephalopathy after early postnatal decline in head growth, whereas hemizygous males may have profound encephalopathy, refractory epilepsy, and respiratory/swallowing complications. Functional outcomes are commonly poor, with major limitations in ambulation and speech. | Outcome concepts: severe developmental disability, epilepsy, feeding impairment | Hayashi 2017: **6/41** walked and **3/41** spoke. Burglen 2012 described a severely affected hemizygous boy with refractory epilepsy and a milder mosaic male. Robust disease-specific life expectancy statistics are not available from the retrieved evidence. | (mukherjee2022thenonlinearpath pages 2-3, burglen2012spectrumofpontocerebellar pages 7-9, hayashi2017comprehensiveinvestigationof pages 2-3) |
| Evidence gaps | Major gaps remain in prevalence/incidence, penetrance estimates, genotype-specific prognosis, quality-of-life metrics, validated biomarkers, standardized treatment algorithms, and controlled therapeutic studies. Recent mechanistic work is largely preclinical, and direct human multi-omics or longitudinal natural-history datasets are limited. | Data gap annotation; future ontology mapping could add MONDO/Orphanet when confirmed from source databases | No reliable population prevalence, carrier frequency, or survival curves were found in the retrieved evidence; no established preventive medical intervention beyond reproductive genetic counseling/testing. | (hayashi2017comprehensiveinvestigationof pages 2-3, mori2023diverseclinicalphenotypes pages 2-5, patel2024geneticevidencefor pages 1-3) |


*Table: This compact table summarizes the core knowledge-base elements for MICPCH syndrome, including definition, genetics, phenotype, imaging, diagnosis, mechanism, management, prognosis, and current evidence gaps. It highlights study-level statistics and ontology suggestions while staying within the available evidence.*

## 1. Disease information

**Definition.** MICPCH is the severe structural-neurodevelopmental end of the CASK-related disorder spectrum. “Pontocerebellar hypoplasia” describes reduced pons and cerebellar volume on imaging; unlike several classic PCH syndromes, CASK-associated disease is not adequately characterized as a uniformly progressive prenatal neurodegeneration. Relative supratentorial preservation and lack of the caudate/ventricular evolution seen in PCH1B/PCH2A support a distinct pathogenesis. (burglen2012spectrumofpontocerebellar pages 7-9, zhang2022adenovo pages 7-10)

**Identifiers and names.** Confirmed in the retrieved literature: **OMIM 300749**. Common names include *microcephaly with pontine and cerebellar hypoplasia*, *MICPCH syndrome*, *CASK-related MICPCH*, and historically *mental retardation and microcephaly with pontine and cerebellar hypoplasia*. The broader category is *CASK-related disorder*. A MONDO identifier, Orphanet number, dedicated MeSH heading, and disease-specific ICD-10/ICD-11 code were not verified in the retrieved primary texts and should be validated directly against current ontology releases rather than inferred. Clinically, cases are usually coded under manifestations such as congenital brain malformation, microcephaly, developmental disorder, or epilepsy.

**Evidence provenance.** This entry combines aggregated disease-level interpretation with individual case reports and referral cohorts. The strongest patient-level datasets retrieved were Burglen et al. (13 molecularly affected patients) and Hayashi et al. (41 patients ascertained by microcephaly plus PCH on MRI). These are not population registries and therefore cannot provide unbiased prevalence or penetrance estimates. (burglen2012spectrumofpontocerebellar pages 7-9, hayashi2017comprehensiveinvestigationof pages 2-3)

## 2. Etiology, risk, protection, and gene–environment interaction

The primary causal factor is a germline or postzygotic pathogenic **CASK** variant causing complete or partial loss of function. Established classes include nonsense, frameshift/indel, splice-altering, deleterious missense and in-frame variants, intragenic copy-number changes, and larger Xp11.4 deletions. In the 41-patient cohort, 32 had CASK abnormalities—23 point variants and nine CNVs—while five had candidate abnormalities involving other genes, demonstrating that the *radioclinical MICPCH phenotype* is genetically heterogeneous even though CASK is its dominant cause. (hayashi2017comprehensiveinvestigationof pages 2-3, hayashi2017comprehensiveinvestigationof pages 1-2, hayashi2017comprehensiveinvestigationof pages 4-6)

Risk is principally genetic: female heterozygosity, male hemizygosity, postzygotic mosaicism, or rarely inheritance from a carrier/mosaic parent. Most confirmed cases are de novo. Male hemizygous complete loss is associated with profound disease or early lethality; mosaicism preserves a population of CASK-expressing cells and can produce a female-like or milder phenotype. Random X-chromosome inactivation creates cellular mosaicism in females and is a plausible contributor to variability, although routine blood X-inactivation measurements do not reliably predict neurological severity. (mukherjee2022thenonlinearpath pages 2-3, burglen2012spectrumofpontocerebellar pages 7-9, hayashi2017comprehensiveinvestigationof pages 1-2)

No reproducible environmental, lifestyle, infectious, occupational, or toxic risk factors are established. Likewise, no validated protective genetic alleles, diets, exposures, or gene–environment interactions are known. Metabolic state may modulate cellular vulnerability in experimental systems, but this is not evidence for a modifiable human environmental risk. Consanguinity and anticipation are not expected drivers of this predominantly de novo X-linked disorder. (patel2024geneticevidencefor pages 3-4)

## 3. Phenotypes

The hallmark phenotype is severe, early-onset neurodevelopmental disability. In Hayashi’s 41-patient imaging-defined cohort, only **6/41 walked** and **3/41 spoke**, indicating profound effects on mobility, communication, self-care, education, and caregiver burden. No MICPCH-specific EQ-5D, SF-36, PROMIS, or validated quality-of-life series was found. (hayashi2017comprehensiveinvestigationof pages 2-3)

* **Progressive postnatal microcephaly:** often normal head circumference at birth, followed by deceleration during infancy; severe and usually persistent. Burglen reported head circumference below −6 SD in seven patients and −3 to −4 SD in four. Suggested HPO: **Microcephaly HP:0000252**, **Progressive microcephaly HP:0000253**. (mukherjee2022thenonlinearpath pages 2-3, burglen2012spectrumofpontocerebellar pages 7-9)
* **Global developmental delay/severe intellectual disability:** generally apparent by 3–6 months and lifelong; expressive language and independent ambulation are especially limited. HPO: **Global developmental delay HP:0001263**, **Severe intellectual disability HP:0010864**, **Delayed speech and language development HP:0000750**, **Motor delay HP:0001270**. (mukherjee2022thenonlinearpath pages 2-3, hayashi2017comprehensiveinvestigationof pages 2-3)
* **Pontine and cerebellar hypoplasia:** congenital/infantile imaging sign with variable vermian and hemispheric severity; postnatal cerebellar growth may be nearly absent. HPO: **Pontine hypoplasia HP:0007366**, **Cerebellar hypoplasia HP:0001321**, **Vermis hypoplasia HP:0001320**. (burglen2012spectrumofpontocerebellar pages 7-9)
* **Tone and movement abnormalities:** axial hypotonia is common early; dystonia, spasticity or mixed motor impairment may develop. Severity is variable but often function-limiting. HPO: **Hypotonia HP:0001252**, **Dystonia HP:0001332**, **Spasticity HP:0001257**, **Ataxia HP:0001251**. (burglen2012spectrumofpontocerebellar pages 7-9, zhang2022adenovo pages 7-10)
* **Epilepsy:** variable in females but more frequent and severe in males; approximately 40% is cited in a recent disease review. Phenotypes include infantile spasms/West syndrome, Ohtahara syndrome and refractory developmental epileptic encephalopathy. Burglen observed epilepsy in **4/13**, one refractory. HPO: **Seizure HP:0001250**, **Infantile spasms HP:0012469**. (mukherjee2022thenonlinearpath pages 2-3, burglen2012spectrumofpontocerebellar pages 7-9)
* **Feeding and respiratory dysfunction:** neonatal feeding difficulty occurred throughout the Burglen cohort; severe males may have dysphagia and central neurogenic respiratory failure associated with brainstem thinning. HPO: **Feeding difficulties HP:0011968**, **Dysphagia HP:0002015**, **Central hypoventilation HP:0007110**. (mukherjee2022thenonlinearpath pages 2-3, burglen2012spectrumofpontocerebellar pages 7-9)
* **Ophthalmologic disease:** optic-nerve hypoplasia/atrophy, nystagmus, strabismus, megalocornea or glaucoma are reported. HPO: **Optic nerve hypoplasia HP:0000609**, **Optic atrophy HP:0000648**, **Nystagmus HP:0000639**, **Glaucoma HP:0000501**. At least six of Burglen’s 13 had ophthalmologic abnormalities. (burglen2012spectrumofpontocerebellar pages 7-9)
* **Hearing impairment:** sensorineural loss is recognized but not universal; Burglen reported **2/13**. HPO: **Sensorineural hearing impairment HP:0000407**. (burglen2012spectrumofpontocerebellar pages 7-9)
* **Growth, skeletal and craniofacial findings:** postnatal growth retardation, scoliosis, micrognathia, prominent ears, long philtrum and characteristic but nonspecific facial appearance. HPO: **Growth delay HP:0001510**, **Scoliosis HP:0002650**, **Micrognathia HP:0000347**. (burglen2012spectrumofpontocerebellar pages 7-9, zhang2022adenovo pages 7-10)

## 4. Genetic and molecular information

**Causal gene.** **CASK** encodes an X-linked membrane-associated guanylate kinase scaffold expressed strongly in the nervous system. The protein contains CaMK-like, L27, PDZ, SH3 and guanylate-kinase-like domains. Its PDZ domain binds neurexins/syndecans, SH3-related interactions include N-type calcium-channel machinery, and the GuK domain interacts with TBR1 and CINAP in nuclear transcriptional complexes regulating genes such as **GRIN2B** and **RELN**. (mori2023diverseclinicalphenotypes pages 2-5)

**Variants.** The 2023 review surveyed 49 reports/197 patients and noted 306 ClinVar variants: 37 frameshift, 227 missense and 43 nonsense records; truncating variants were much more often pathogenic/likely pathogenic and associated with more severe phenotypes than missense variants (**p<0.0001**). These database counts are not disease prevalence or carrier-frequency estimates. Representative pathogenic variants in Hayashi included c.79C>T (p.Arg27Ter), c.316C>T (p.Arg106Ter), c.868G>T (p.Glu290Ter), c.2632C>T (p.Gln878Ter), and frameshift/stop variants such as c.1006_1012del (p.Thr336GlnfsTer23). (mori2023diverseclinicalphenotypes pages 2-5, hayashi2017comprehensiveinvestigationof pages 4-6)

Most severe MICPCH variants act through loss of function—nonsense-mediated decay, absent/truncated protein, destabilization, or gene dosage loss. A reported c.638T>G missense variant reduced protein but not mRNA, consistent with protein destabilization. No recurrent hotspot explains most cases, and variant size alone does not reliably predict phenotype. (zhang2022adenovo pages 7-10)

Variants are normally germline; mosaic variants are postzygotic, not neoplastic “somatic mutations.” Population allele frequencies are expected to be absent or extremely low for pathogenic alleles, but variant-specific gnomAD/TOPMed values must be retrieved by genomic coordinate and transcript and were not available in the gathered texts. No validated modifier gene or protective allele is established. Larger Xp11.4 deletions may introduce contiguous-gene effects. No disease-specific DNA-methylation episignature or causal epigenetic lesion is established.

A major 2024 development is splice-dependent functional plasticity. Vertebrate-specific exons 19–20 encode a flexible loop between PDZ and SH3 regions; isoforms that include or exclude these exons differ structurally. Damaging variants confined to these exons can preserve older CASK isoforms and produce microcephaly/forebrain dysfunction without classic PCH, helping explain non-linear genotype–phenotype relationships. (patel2024geneticevidencefor pages 1-3, patel2024geneticevidencefor pages 9-11)

## 5. Environmental information

There is no evidence that toxins, radiation, pollution, smoking, alcohol, diet, exercise, occupation, or infection causes MICPCH. Pregnancy is often reportedly uncomplicated. These exposures can independently affect fetal development and should be evaluated in the differential diagnosis, but they are not established components of CASK-MICPCH etiology. No pathogen or zoonotic transmission is applicable.

## 6. Mechanism and pathophysiology

A defensible causal chain is:

**pathogenic CASK variant/CASK haploinsufficiency → altered scaffold, transcriptional and metabolic functions → selective neuronal and circuit vulnerability → impaired hindbrain growth plus cerebellar granule-cell loss and synaptic E/I imbalance → pontocerebellar hypoplasia, progressive microcephaly, epilepsy and severe developmental disability.**

Upstream events are reduced CASK dosage, destabilized protein, or splice-isoform disruption. Intermediate mechanisms include impaired protein interactions at synapses, altered TBR1/CINAP-linked transcription, reduced GluN2B, mitochondrial/oxidative-metabolic disturbance, and non-cell-autonomous growth effects. Downstream consequences are granule-cell degeneration, circuit imbalance, seizures, poor motor learning and reduced brain growth. These mechanisms are complementary hypotheses rather than one fully validated human pathway. (patel2024geneticevidencefor pages 1-3, mori2019deficiencyofcalciumcalmodulindependent pages 1-2, patel2024geneticevidencefor pages 3-4)

In mouse brain slices, CASK-deficient pyramidal neurons showed increased miniature excitatory and decreased inhibitory postsynaptic currents. **GluN2B overexpression rescued the E/I imbalance**, making GRIN2B downregulation a mechanistically strong preclinical finding, although not yet a proven therapeutic target in patients. Suggested GO terms: synapse organization, chemical synaptic transmission, regulation of excitatory postsynaptic potential, regulation of inhibitory postsynaptic potential, and NMDA-receptor signaling. Suggested cell type: cortical pyramidal neuron. (mori2019deficiencyofcalciumcalmodulindependent pages 1-2)

Cerebellar granule cells appear particularly CASK-dependent. Conditional deletion after adulthood caused progressive cerebellar degeneration and ataxia without reducing survival, arguing that apparent “hypoplasia” can include post-migratory degeneration. Conversely, selective loss of exon 19–20-containing isoforms can spare cerebellum while affecting forebrain function. Suggested GO terms: cerebellar granule-cell differentiation/survival, neuron death, cerebellar development; CL suggestions: cerebellar granule cell, Purkinje cell, astrocyte. (patel2024geneticevidencefor pages 1-3, patel2024geneticevidencefor pages 9-11, patel2024geneticevidencefor pages 14-16)

Human-cell knockdown and heterozygous mouse work implicated reduced cellular respiration and abnormal brain/muscle oxidative metabolism. This supports metabolic stress as a possible contributor, but no validated patient metabolomic biomarker or metabolic treatment exists. Immune activation is not a primary mechanism; astrogliosis in severe cerebellar pathology is better interpreted as a downstream response to neuronal injury. (patel2024geneticevidencefor pages 3-4)

No disease-specific single-cell atlas, spatial-transcriptomic dataset, clinical proteomic/metabolomic signature, or integrated patient multi-omics classifier was identified. Current advanced work is mainly conditional genome editing in mice, RT-PCR of isoforms, electrophysiology and in-silico/structural modeling. (patel2024geneticevidencefor pages 1-3, patel2024geneticevidencefor pages 9-11)

## 7. Anatomical structures affected

The **central nervous system** is primary. Core structures are the cerebellar hemispheres and vermis (**UBERON:0002037**, cerebellum), pons (**UBERON:0000988**) and brainstem (**UBERON:0002298**). The superior pons may be relatively spared, and the corpus callosum is often preserved or proportionate, although variable cerebral and callosal abnormalities occur. Findings are generally bilateral, but cerebellar hemispheric asymmetry has been described. (burglen2012spectrumofpontocerebellar pages 7-9, hayashi2017comprehensiveinvestigationof pages 4-6)

At tissue/cell level, nervous tissue and especially cerebellar granule neurons are implicated; cortical pyramidal neurons show circuit dysfunction in models, and astrocytes participate in reactive gliosis. Secondary systems include optic nerve/retina, auditory pathways, axial musculature, skeleton and oropharyngeal/respiratory motor systems. Subcellular localization spans synaptic membranes and protein complexes, cytoplasm, nucleus/transcriptional complexes, and potentially mitochondria/metabolic machinery. Relevant GO cellular-component suggestions include synapse, postsynaptic density, presynaptic active zone, cytoplasm and nucleus. (mori2023diverseclinicalphenotypes pages 2-5, mori2019deficiencyofcalciumcalmodulindependent pages 1-2, patel2024geneticevidencefor pages 3-4)

## 8. Temporal development

Onset is congenital-to-infantile but often insidious. Many girls have normal head size at birth; motor delay becomes evident at approximately 3–6 months, followed by progressive postnatal microcephaly and recognition of PCH on infant MRI. Cerebellum can already be severely small at birth and show little subsequent growth. (mukherjee2022thenonlinearpath pages 2-3)

The course is chronic and lifelong. In heterozygous females, early structural/growth pathology is often described as self-limiting or relatively non-progressive rather than continuously degenerative, although developmental gains remain markedly impaired and late regression/ataxia has occasionally been reported. Complete male loss permits more severe ongoing degeneration, early epileptic encephalopathy, swallowing/respiratory failure and early death. Adult conditional mouse deletion demonstrates that CASK remains necessary for cerebellar maintenance, but the extent of analogous late human progression is uncertain. (mukherjee2022thenonlinearpath pages 2-3, patel2024geneticevidencefor pages 1-3)

There are no validated clinical stages, remission pattern, or therapeutic critical window. Infancy is biologically and clinically important because head-growth deceleration, seizures, feeding difficulty and developmental delay emerge then, and early supportive intervention is most feasible.

## 9. Inheritance and population

Inheritance is best described as **X-linked dominant/semidominant with sex-dependent severity**. Most typical affected females have a de novo heterozygous variant. Hemizygous male loss-of-function variants cause severe encephalopathy or lethality; hypomorphic or postzygotic mosaic variants can be survivable. In Burglen, all molecular findings were de novo, including the first described mildly affected mosaic male. (burglen2012spectrumofpontocerebellar pages 7-9)

Penetrance for unequivocal loss-of-function variants appears high, but formal age- and sex-stratified estimates are unavailable. Expressivity is variable and influenced by residual function, mosaicism, variant domain/splicing, and probably X-inactivation. Germline mosaicism remains a counseling consideration even when parental blood testing is negative; recurrence risk is therefore low but not zero. Anticipation, founder effects and population-specific high-frequency alleles are not established.

No reliable incidence, prevalence per 100,000, carrier frequency, geographic concentration, or ethnic enrichment was found. Referral cohorts are female-skewed: Hayashi included **35 females and six males**. This reflects biological ascertainment—typical MICPCH is predominantly female and complete male loss is much more severe—not evidence of geographic restriction. (hayashi2017comprehensiveinvestigationof pages 2-3, hayashi2017comprehensiveinvestigationof pages 1-2)

## 10. Diagnostics

Diagnosis requires a compatible phenotype plus molecular confirmation. Clinical evaluation includes serial head circumference and growth, developmental/neurologic examination, feeding and respiratory assessment, ophthalmology, audiology, and musculoskeletal evaluation. Brain MRI is preferred over CT and should evaluate pons, vermis, cerebellar hemispheres, supratentorial structures, corpus callosum and optic pathways. EEG is indicated for seizures, spasms, regression or suspicious events; hearing testing and visual evoked/ophthalmic studies are individualized. There is no diagnostic blood enzyme, metabolite, protein biomarker, biopsy or histopathology requirement.

**Testing algorithm:**

1. Trio exome or genome sequencing with CNV calling, or a comprehensive neurodevelopmental/PCH panel including **CASK**.
2. Ensure deletion/duplication analysis—sequence-only testing can miss intragenic or Xp11.4 CNVs.
3. Confirm by orthogonal sequencing/CNV method and test parents.
4. In an affected male with negative blood testing or discordant severity, use high-depth testing for mosaicism and consider a second tissue.
5. If negative, reassess the radiologic label and investigate other PCH/cerebellar-development genes and chromosomal causes.

Combined genomic investigation identified causative/candidate abnormalities in **37/41 (90.2%)** in a selected MRI-defined cohort; this is not a general-population diagnostic yield. WES is particularly useful, but WGS may better detect noncoding, structural and mosaic variants. CMA is useful for deletions; karyotyping and FISH are not first-line unless a larger rearrangement is suspected. Mitochondrial DNA and repeat-expansion testing are not routine unless additional features suggest another disorder. (hayashi2017comprehensiveinvestigationof pages 2-3, zhang2022adenovo pages 7-10)

Differential diagnoses include TSEN54/PCH2 and other classic PCH disorders; ITPR1- or RELN-related cerebellar disease; DDX3X-, PNKP- and other microcephaly-developmental disorders; chromosomal CNVs; congenital infection; and acquired prenatal/perinatal injury. Preserved supratentorial structures/corpus callosum, postnatal microcephaly, female sex and a CASK variant favor MICPCH. Broad testing is important because radiologic PCH is an imaging descriptor rather than a single etiologic class. (hayashi2017comprehensiveinvestigationof pages 1-2, hayashi2017comprehensiveinvestigationof pages 4-6)

There is no population newborn screen. Cascade testing is appropriate after a familial variant is found; prenatal and preimplantation testing are technically feasible for a known pathogenic variant.

## 11. Outcome and prognosis

No robust 5- or 10-year survival rates, life-expectancy curves, disease-specific mortality rates or validated prognostic biomarkers are available. Female survival into adulthood occurs, but severe lifelong disability is common. Functional prognosis is poor: in the 41-patient cohort, only 14.6% walked and 7.3% spoke. Male prognosis depends strongly on residual CASK function/mosaicism; complete loss is associated with refractory epilepsy, profound developmental impairment, respiratory/swallowing complications and possible early death. (mukherjee2022thenonlinearpath pages 2-3, hayashi2017comprehensiveinvestigationof pages 2-3)

Morbidity includes nonverbal or minimally verbal communication, non-ambulation, feeding dependence, epilepsy, visual/hearing impairment, scoliosis and extensive caregiver needs. Recovery to normal development is not expected, although therapies may improve comfort, communication, mobility and participation. Likely prognostic features include sex, mosaic allele fraction, residual protein function, seizure burden, respiratory/feeding involvement and severity of cerebellar/brainstem disease; none forms a validated prediction model.

## 12. Treatment and implementation

There is **no established disease-modifying pharmacotherapy, gene therapy, RNA therapy or cell therapy**. A ClinicalTrials.gov search for MICPCH/CASK-related disease identified no relevant interventional trial. Present management is individualized and multidisciplinary:

* antiseizure medication selected by seizure type and EEG syndrome; rescue plans for prolonged seizures;
* physical and occupational therapy, seating/orthotics and contracture/scoliosis surveillance;
* speech-language therapy and augmentative/alternative communication;
* feeding/swallow evaluation, nutrition support and gastrostomy when aspiration or inadequate growth warrants it;
* respiratory monitoring in severely affected males;
* hearing aids/cochlear evaluation and ophthalmologic treatment;
* sleep, tone, dystonia, constipation and pain management;
* special education, social services, palliative-care involvement when appropriate, and genetic counseling.

Suggested NCIT concepts include **Supportive Care**, **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, **Anticonvulsant Therapy**, **Gastrostomy**, **Hearing Aid**, and **Genetic Counseling**. Exact NCIT codes should be resolved against the current NCIT release.

GluN2B restoration rescued synaptic imbalance experimentally, while metabolic work suggests potentially modifiable stress pathways. Neither constitutes evidence for NMDA-targeted medication, supplements or metabolic therapy in patients. Gene replacement is theoretically complicated by developmental timing, cell-type requirements, X-linked mosaicism and CASK’s multiple isoforms/domains. (mori2019deficiencyofcalciumcalmodulindependent pages 1-2, patel2024geneticevidencefor pages 3-4)

## 13. Prevention

There is no vaccine, lifestyle modification, environmental intervention or prophylactic medication that prevents a de novo CASK variant. Primary reproductive prevention consists of preconception genetic counseling and, when a familial pathogenic variant is known, carrier testing, preimplantation genetic testing, chorionic-villus sampling or amniocentesis. Negative parental blood testing substantially lowers but does not eliminate recurrence risk because gonadal mosaicism is possible.

Secondary prevention means early recognition and intervention: serial infant head measurements, prompt MRI/genomic testing, early EEG for spasms, and early feeding, vision, hearing and developmental services. Tertiary prevention addresses aspiration, malnutrition, uncontrolled seizures, contractures, scoliosis, pressure injury and respiratory complications. Population screening is unsupported because the disorder is ultra-rare, usually de novo, and lacks a validated newborn biomarker.

## 14. Other species and natural disease

No well-established naturally occurring veterinary MICPCH syndrome, breed predisposition, zoonotic potential or cross-species transmission was identified. CASK orthologs are evolutionarily conserved in vertebrates and invertebrates, supporting conservation of synaptic and hindbrain-related functions. Exact NCBI Taxon and orthologous Gene IDs should be obtained directly from NCBI/Alliance records before database loading. MICPCH is genetic and noninfectious, so transmission is Mendelian/cellular rather than zoonotic.

## 15. Model organisms

**Mouse models** include constitutive heterozygous females, neuron-specific conditional knockouts, cerebellum-specific deletions, adult inducible deletions, and knockdown/knockout neurons studied in acute slices. Heterozygous females recapitulate postnatal microcephaly and aspects of systemic growth/metabolic abnormality. Neuron-specific deletion causes seizures and growth retardation, while cerebellar or adult deletion reveals selective granule-cell degeneration and progressive ataxia. (patel2024geneticevidencefor pages 1-3, patel2024geneticevidencefor pages 3-4)

**Cellular and slice models** show reduced respiration and altered E/I balance, with GluN2B rescue providing a functional intervention experiment. **Computational/structural models** in 2024 showed that inclusion of vertebrate-specific exons 19–20 changes flexibility of the PDZ–SH3–GuK supradomain and helps explain cerebellar-sparing genotypes. (patel2024geneticevidencefor pages 9-11, mori2019deficiencyofcalciumcalmodulindependent pages 1-2)

Important limitations are perinatal lethality of complete mouse knockout, species differences in brain development, non-equivalence of engineered deletion to human cellular mosaicism, and inability of a single model to reproduce the full visual, auditory, language and cognitive phenotype. Patient-derived iPSC neurons, cerebellar organoids, single-cell profiling and isogenic variant correction would be high-value future systems, but validated MICPCH datasets using these approaches were not identified.

## Key recent developments and expert interpretation

The most important recent synthesis is Mori et al., **August 2023**, which frames CASK disease as domain- and variant-dependent rather than a single uniform syndrome: truncating variants favor MICPCH, whereas hypomorphic missense variants more often cause X-linked intellectual disability with or without nystagmus. DOI/URL: https://doi.org/10.3390/genes14081656. (mori2023diverseclinicalphenotypes pages 2-5)

Patel et al., **April 2024**, adds genetic and structural evidence that alternative splicing creates distinct CASK functions. Its central conclusion is that loss of CASK disproportionately affects cerebellum, while vertebrate-specific splice isoforms contribute additional forebrain functions. DOI/URL: https://doi.org/10.1136/jmg-2023-109747. (patel2024geneticevidencefor pages 1-3, patel2024geneticevidencefor pages 9-11)

Representative exact abstract statements from retrieved sources are:

> “CASK-related disorders are a form of rare X-linked neurological diseases and most of the patients are females.” — Mori et al., 2023. (mori2023diverseclinicalphenotypes pages 2-5)

> “Loss of CASK function disproportionately affects the cerebellum.” — Patel et al., 2024. (patel2024geneticevidencefor pages 1-3)

> “Both CASK-KO and CASK-KD neurons showed a disruption of the excitatory and inhibitory (E/I) balance.” — Mori et al., 2019. DOI/URL: https://doi.org/10.1038/s41380-018-0338-4. (mori2019deficiencyofcalciumcalmodulindependent pages 1-2)

> “We observed a high frequency of patients with a CASK mutation (13/14).” — Burglen et al., March 2012. DOI/URL: https://doi.org/10.1186/1750-1172-7-18. (burglen2012spectrumofpontocerebellar pages 7-9)

PMIDs were not exposed in the retrieved source metadata and therefore are not invented here; DOI URLs provide persistent primary-source links. The most consequential knowledge gaps are unbiased epidemiology, longitudinal adult natural history, variant-level penetrance, patient-reported outcomes, validated biomarkers and controlled therapeutic studies.

References

1. (mukherjee2022thenonlinearpath pages 2-3): Konark Mukherjee, Leslie E. W. LaConte, and Sarika Srivastava. The non-linear path from gene dysfunction to genetic disease: lessons from the micpch mouse model. Cells, 11:1131, Mar 2022. URL: https://doi.org/10.3390/cells11071131, doi:10.3390/cells11071131. This article has 7 citations.

2. (mori2023diverseclinicalphenotypes pages 2-5): Takuma Mori, Mengyun Zhou, and Katsuhiko Tabuchi. Diverse clinical phenotypes of cask-related disorders and multiple functional domains of cask protein. Genes, 14:1656, Aug 2023. URL: https://doi.org/10.3390/genes14081656, doi:10.3390/genes14081656. This article has 17 citations.

3. (patel2024geneticevidencefor pages 1-3): Paras A Patel, Leslie E W LaConte, Chen Liang, Thomas Cecere, Deepa Rajan, Sarika Srivastava, and Konark Mukherjee. Genetic evidence for splicing-dependent structural and functional plasticity in cask protein. Journal of Medical Genetics, 61:759-768, Apr 2024. URL: https://doi.org/10.1136/jmg-2023-109747, doi:10.1136/jmg-2023-109747. This article has 4 citations and is from a domain leading peer-reviewed journal.

4. (zhang2022adenovo pages 7-10): Ying Zhang, Ya-ling Nie, Y. Mu, Jie Zheng, Xiaowei Xu, Fang Zhang, Jianbo Shu, and Yang Liu. A de novo variant in cask gene causing intellectual disability and brain hypoplasia: a case report and literature review. Italian Journal of Pediatrics, May 2022. URL: https://doi.org/10.1186/s13052-022-01248-z, doi:10.1186/s13052-022-01248-z. This article has 4 citations and is from a peer-reviewed journal.

5. (hayashi2017comprehensiveinvestigationof pages 2-3): Shin Hayashi, Daniela Tiaki Uehara, Kousuke Tanimoto, Seiji Mizuno, Yasutsugu Chinen, Shinobu Fukumura, Jun-ichi Takanashi, Hitoshi Osaka, Nobuhiko Okamoto, and Johji Inazawa. Comprehensive investigation of cask mutations and other genetic etiologies in 41 patients with intellectual disability and microcephaly with pontine and cerebellar hypoplasia (micpch). PLOS ONE, 12:e0181791, Aug 2017. URL: https://doi.org/10.1371/journal.pone.0181791, doi:10.1371/journal.pone.0181791. This article has 81 citations and is from a peer-reviewed journal.

6. (hayashi2017comprehensiveinvestigationof pages 1-2): Shin Hayashi, Daniela Tiaki Uehara, Kousuke Tanimoto, Seiji Mizuno, Yasutsugu Chinen, Shinobu Fukumura, Jun-ichi Takanashi, Hitoshi Osaka, Nobuhiko Okamoto, and Johji Inazawa. Comprehensive investigation of cask mutations and other genetic etiologies in 41 patients with intellectual disability and microcephaly with pontine and cerebellar hypoplasia (micpch). PLOS ONE, 12:e0181791, Aug 2017. URL: https://doi.org/10.1371/journal.pone.0181791, doi:10.1371/journal.pone.0181791. This article has 81 citations and is from a peer-reviewed journal.

7. (hayashi2017comprehensiveinvestigationof pages 4-6): Shin Hayashi, Daniela Tiaki Uehara, Kousuke Tanimoto, Seiji Mizuno, Yasutsugu Chinen, Shinobu Fukumura, Jun-ichi Takanashi, Hitoshi Osaka, Nobuhiko Okamoto, and Johji Inazawa. Comprehensive investigation of cask mutations and other genetic etiologies in 41 patients with intellectual disability and microcephaly with pontine and cerebellar hypoplasia (micpch). PLOS ONE, 12:e0181791, Aug 2017. URL: https://doi.org/10.1371/journal.pone.0181791, doi:10.1371/journal.pone.0181791. This article has 81 citations and is from a peer-reviewed journal.

8. (burglen2012spectrumofpontocerebellar pages 7-9): Lydie Burglen, Sandra Chantot-Bastaraud, Catherine Garel, Mathieu Milh, Renaud Touraine, Ginevra Zanni, Florence Petit, Alexandra Afenjar, Cyril Goizet, Sabina Barresi, Aurélie Coussement, Christine Ioos, Leila Lazaro, Sylvie Joriot, Isabelle Desguerre, Didier Lacombe, Vincent des Portes, Enrico Bertini, Jean-Pierre Siffroi, Thierry Billette de Villemeur, and Diana Rodriguez. Spectrum of pontocerebellar hypoplasia in 13 girls and boys with cask mutations: confirmation of a recognizable phenotype and first description of a male mosaic patient. Orphanet Journal of Rare Diseases, 7:18-18, Mar 2012. URL: https://doi.org/10.1186/1750-1172-7-18, doi:10.1186/1750-1172-7-18. This article has 126 citations and is from a peer-reviewed journal.

9. (patel2024geneticevidencefor pages 9-11): Paras A Patel, Leslie E W LaConte, Chen Liang, Thomas Cecere, Deepa Rajan, Sarika Srivastava, and Konark Mukherjee. Genetic evidence for splicing-dependent structural and functional plasticity in cask protein. Journal of Medical Genetics, 61:759-768, Apr 2024. URL: https://doi.org/10.1136/jmg-2023-109747, doi:10.1136/jmg-2023-109747. This article has 4 citations and is from a domain leading peer-reviewed journal.

10. (mori2019deficiencyofcalciumcalmodulindependent pages 1-2): Takuma Mori, Enas A. Kasem, Emi Suzuki-Kouyama, Xueshan Cao, Xue Li, Taiga Kurihara, Takeshi Uemura, Toru Yanagawa, and Katsuhiko Tabuchi. Deficiency of calcium/calmodulin-dependent serine protein kinase disrupts the excitatory-inhibitory balance of synapses by down-regulating glun2b. Molecular Psychiatry, 24:1079-1092, Jan 2019. URL: https://doi.org/10.1038/s41380-018-0338-4, doi:10.1038/s41380-018-0338-4. This article has 44 citations and is from a highest quality peer-reviewed journal.

11. (patel2024geneticevidencefor pages 3-4): Paras A Patel, Leslie E W LaConte, Chen Liang, Thomas Cecere, Deepa Rajan, Sarika Srivastava, and Konark Mukherjee. Genetic evidence for splicing-dependent structural and functional plasticity in cask protein. Journal of Medical Genetics, 61:759-768, Apr 2024. URL: https://doi.org/10.1136/jmg-2023-109747, doi:10.1136/jmg-2023-109747. This article has 4 citations and is from a domain leading peer-reviewed journal.

12. (patel2024geneticevidencefor pages 14-16): Paras A Patel, Leslie E W LaConte, Chen Liang, Thomas Cecere, Deepa Rajan, Sarika Srivastava, and Konark Mukherjee. Genetic evidence for splicing-dependent structural and functional plasticity in cask protein. Journal of Medical Genetics, 61:759-768, Apr 2024. URL: https://doi.org/10.1136/jmg-2023-109747, doi:10.1136/jmg-2023-109747. This article has 4 citations and is from a domain leading peer-reviewed journal.

13. (patel2024geneticevidencefor pages 11-12): Paras A Patel, Leslie E W LaConte, Chen Liang, Thomas Cecere, Deepa Rajan, Sarika Srivastava, and Konark Mukherjee. Genetic evidence for splicing-dependent structural and functional plasticity in cask protein. Journal of Medical Genetics, 61:759-768, Apr 2024. URL: https://doi.org/10.1136/jmg-2023-109747, doi:10.1136/jmg-2023-109747. This article has 4 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](MICPCH_Syndrome-deep-research-falcon_artifacts/artifact-00.md)