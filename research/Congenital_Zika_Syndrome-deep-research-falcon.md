---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-11T18:14:15.919523'
end_time: '2026-06-11T18:33:05.839962'
duration_seconds: 1129.92
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Congenital Zika Syndrome
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_tokens: 12000
    max_embedded_images: 8
citation_count: 53
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Congenital_Zika_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Zika Syndrome
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Congenital Zika Syndrome** covering all of the
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
- **Disease Name:** Congenital Zika Syndrome
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Congenital Zika Syndrome** covering all of the
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


# Congenital Zika Syndrome (CZS): Comprehensive Disease Characteristics Report (2023–2025 evidence prioritized)

## 1. Disease Information

### 1.1 Concise overview
Congenital Zika syndrome (CZS) is a specific pattern of congenital anomalies and long-term neurodevelopmental disabilities caused by vertical (mother-to-child) transmission of Zika virus (ZIKV) during pregnancy, with the central nervous system (CNS) as the primary target and frequent multisystem involvement (ocular, musculoskeletal, feeding/swallowing, and other neurologic comorbidities). (martelli2024clinicalspectrumof pages 1-2, crisantolopez2023congenitalzikasyndrome pages 1-2)

### 1.2 Key identifiers (ontology/classification)
- **ICD-11:** *Congenital Zika virus infection* **KA62.0** (explicitly stated as the ICD-11 classification in a 2024 Brazil-focused clinical spectrum update). Publication date: **2024-07**; URL: https://doi.org/10.1590/0037-8682-0153-2024 (martelli2024clinicalspectrumof pages 2-3)
- **MeSH (related concept):** *Zika Virus Infection* (MeSH concept id **D000071243**) appears in ClinicalTrials.gov structured metadata (not specific to congenital infection, but relevant controlled vocabulary). (NCT03110770 chunk 4)
- **MONDO ID / ICD-10 / Orphanet / OMIM / MeSH for “Congenital Zika Syndrome”:** Not available from the retrieved full-text evidence in this run; only ICD-11 KA62.0 was explicitly reported. (martelli2024clinicalspectrumof pages 2-3, crisantolopez2023congenitalzikasyndrome pages 8-10)

### 1.3 Common synonyms / alternative names
- “Congenital Zika syndrome (CZS)” (martelli2024clinicalspectrumof pages 1-2, crisantolopez2023congenitalzikasyndrome pages 1-2)
- “Congenital Zika virus infection” (ICD-11 KA62.0 term; also used as a primary label in the 2024 Brazil review) (martelli2024clinicalspectrumof pages 2-3)
- “Zika-related microcephaly” is frequently used to refer to severe CZS presentations in cohort literature. (mirandafilho2025characterizationof843 pages 2-3)

### 1.4 Evidence provenance (individual patients vs aggregated)
Evidence in this report is derived from both (i) **aggregated resources** (systematic reviews, meta-analyses, surveillance reviews) and (ii) **primary cohorts** (prospective cohorts, pooled individual-participant data analyses, caregiver studies using validated scales). (mirandafilho2025characterizationof843 pages 2-3, rabe2025areviewof pages 4-5, melo2023congenitalzikasyndrome pages 11-12)

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** In utero ZIKV infection (vertical transmission), which can occur even when maternal infection is asymptomatic; congenital manifestations arise from placental infection and fetal neurotropism with injury to neural progenitors and neurodevelopmental disruption. (crisantolopez2023congenitalzikasyndrome pages 4-5, wong2025zikavirusand pages 3-5)

### 2.2 Risk factors
- **Gestational timing:** Earlier maternal infection increases risk of adverse outcomes. A matched cohort study reported that **44%** of pregnancies with **first-trimester** maternal infection had at least one adverse child event, and first-trimester infection had **OR 11.2** (95% CI 3.6–35.0) for adverse outcomes vs third trimester. Publication date: **2025-01**; URL: https://doi.org/10.1542/peds.2024-067552 (venancio2025earlyandlongterm pages 1-3)
- **Population-level risk of congenital outcomes among infected pregnancies:** A large systematic review/meta-analysis estimated **CZS proportion 4.65%** (95% CI 3.38–6.67%) among ZIKV-infected pregnancies. Publication date: **2026-02**; URL: https://doi.org/10.1038/s44360-025-00051-4 (mccain2026asystematicreview pages 1-2)

### 2.3 Protective factors
Evidence for protective factors is limited and heterogeneous. In one longitudinal cohort of normocephalic preschool children in Colombia (not restricted to CZS cases), **daycare/school attendance** was associated with a lower risk of neurodevelopmental delay, while prenatal ZIKV exposure was not significantly associated with delay in that cohort; this represents a social/environmental protective association rather than biological protection. (shah2024analysisofcongenital pages 13-15)

### 2.4 Gene–environment interactions (GxE)
A key hypothesized interaction is **prior flavivirus immunity** and **antibody-dependent enhancement (ADE)** mechanisms at the maternal–fetal interface, which may facilitate placental infection/transfer via Fcγ receptor pathways (conceptualized in placental-interface reviews). (wong2025zikavirusand pages 2-3)

## 3. Phenotypes (clinical spectrum)

### 3.1 Core phenotype summary (current understanding)
CZS is defined by a recognizable phenotype including severe/disproportionate microcephaly, characteristic neuroimaging abnormalities (calcifications, ventriculomegaly, cortical atrophy/malformations), ocular lesions (retinal/optic nerve), congenital contractures (arthrogryposis/clubfoot), and frequent neurologic comorbidities such as epilepsy and dysphagia. (martelli2024clinicalspectrumof pages 1-2, martelli2024clinicalspectrumof pages 2-3)

### 3.2 Quantitative phenotype frequencies and statistics (selected recent syntheses)
A consolidated phenotype-frequency table with suggested **HPO terms** and quantitative ranges is provided below.

| Domain | Specific phenotype (suggested HPO term) | Quantitative estimate(s) | Population / study type | Notes | Supporting citation IDs |
|---|---|---:|---|---|---|
| CNS | Microcephaly (HP:0000252) | ~4% absolute risk of microcephaly after confirmed maternal ZIKV infection; baseline pre-epidemic microcephaly ~2.0/10,000 newborns | Brazil meta-analysis/review summarized in 2024 update | Signature phenotype; risk estimate refers to infected pregnancies/offspring follow-up | (martelli2024clinicalspectrumof pages 1-2) |
| CNS | Severe microcephaly (HP:0011451) | 384/601 (63.9%) among children with microcephaly at birth; moderate 217/601 (36.1%) | IPD meta-analysis of 12 Brazilian cohorts, n=843 children with Zika-related microcephaly | Captures severity distribution among those already affected | (mirandafilho2025characterizationof843 pages 2-3) |
| CNS | Postnatal microcephaly (HP:0000252) | 172/843 (20.4%) | IPD meta-analysis of 12 Brazilian cohorts | Highlights progression after birth in some exposed infants | (mirandafilho2025characterizationof843 pages 2-3) |
| Neuroimaging | Intracranial calcifications (HP:0002514) | ~80% across pooled Brazilian cohorts; 94% in systematic clinicopathologic review | IPD meta-analysis; systematic review of Brazilian outbreak cohorts | One of the most consistent structural markers of severe CZS | (mirandafilho2025characterizationof843 pages 2-3, shah2024analysisofcongenital pages 13-15) |
| Neuroimaging | Ventriculomegaly (HP:0002119) | ~80% across pooled cohorts; 89% in systematic clinicopathologic review | IPD meta-analysis; systematic review | Often co-occurs with calcifications and cortical atrophy | (mirandafilho2025characterizationof843 pages 2-3, shah2024analysisofcongenital pages 13-15) |
| Neuroimaging | Cortical atrophy / reduced cerebral parenchyma (HP:0007373, HP:0002059) | ~50% cortical atrophy/developmental disorders across pooled cohorts; reduced cerebral parenchyma 86%; malformation of cortical development/lack of gyri 78% | IPD meta-analysis; systematic review | Marks severe prenatal brain disruption | (mirandafilho2025characterizationof843 pages 2-3, shah2024analysisofcongenital pages 13-15) |
| CNS | Neurological alteration of any type | 18.7% | Zika Brazilian Cohorts pooled pregnancy/child follow-up | Broader than microcephaly alone | (martelli2024clinicalspectrumof pages 3-4) |
| CNS | Any abnormality after antenatal exposure | 24.7% had ≥1 alteration | Zika Brazilian Cohorts pooled pregnancy/child follow-up | Includes isolated abnormalities; not restricted to classic CZS | (martelli2024clinicalspectrumof pages 3-4) |
| CNS | Epilepsy / seizures (HP:0001250) | 37.7%–71.4% in reviewed cohorts; 71.4% cumulative incidence within 2 years in one microcephaly cohort; 30%–80% across 12-cohort IPD; 91% in clinicopathologic review | Brazil cohorts, systematic reviews, IPD meta-analysis | Often early-onset; epileptic spasms may begin after 3 months | (martelli2024clinicalspectrumof pages 2-3, mirandafilho2025characterizationof843 pages 2-3, shah2024analysisofcongenital pages 13-15) |
| Ocular | Ocular abnormalities overall (HP:0000478) | 21.4%–70%; about one-third in one multisite Brazilian study | Brazil cohorts/review | Some affected infants had ocular findings without microcephaly | (martelli2024clinicalspectrumof pages 2-3) |
| Ocular | Fundus abnormalities (HP:0000580) | 0%–67.1% | IPD meta-analysis of 12 Brazilian cohorts | Wide heterogeneity across sites | (mirandafilho2025characterizationof843 pages 2-3) |
| Ocular | Optic nerve abnormalities (HP:0001138) | 0%–36.5% across cohorts; 67% in systematic clinicopathologic review | IPD meta-analysis; systematic review | Includes optic nerve pallor/atrophy | (mirandafilho2025characterizationof843 pages 2-3, shah2024analysisofcongenital pages 13-15) |
| Ocular | Retinal lesions / chorioretinal atrophy/scarring (HP:0000556, HP:0007703) | 79% retinal lesions in systematic review; examples: chorioretinal atrophy 11/17 eyes (64.7%), macular chorioretinal atrophy/scarring 45.8% | Systematic review; outbreak case series summarized in review | Major cause of visual impairment | (shah2024analysisofcongenital pages 13-15, shah2024analysisofcongenital pages 10-12) |
| Auditory | Hearing abnormality (HP:0000365) | 0%–50% across cohorts; ~20% in systematic clinicopathologic review | IPD meta-analysis; systematic review | Conductive or sensorineural deficits reported | (mirandafilho2025characterizationof843 pages 2-3, shah2024analysisofcongenital pages 1-3, shah2024analysisofcongenital pages 13-15) |
| Musculoskeletal | Arthrogryposis / congenital contractures (HP:0002804, HP:0001371) | ~15% in systematic review; 19.0% (n=4) in one summarized series | Systematic review; case series summarized in review | Commonly associated with severe CNS disease and hypertonia | (shah2024analysisofcongenital pages 13-15, shah2024analysisofcongenital pages 10-12) |
| Musculoskeletal | Hypertonia / spasticity (HP:0001276, HP:0001257) | Hypertonia up to 92%; spasms/spasticity 97%; appendicular hypertonia 94.8% in one series | Systematic review; summarized cohorts | Major contributor to cerebral palsy phenotype | (shah2024analysisofcongenital pages 13-15, shah2024analysisofcongenital pages 10-12) |
| Musculoskeletal | Quadriparesis / severe motor impairment (HP:0002510, HP:0001270) | Quadriparesis 92%; one cohort reported 81% severe motor function impairment | Systematic review; Brazil cohort review | Usually evident in infancy/early childhood | (shah2024analysisofcongenital pages 13-15, martelli2024clinicalspectrumof pages 3-4) |
| Feeding-Growth | Dysphagia / swallowing dysfunction (HP:0002015) | 17.9%–70% across reviews; 22.2%–67.7% across 12-cohort IPD; oropharyngeal dysphagia 79.3% in microcephaly vs 8.5% in normocephalic peers | Brazil cohorts, review, IPD meta-analysis | Major driver of malnutrition and aspiration risk; ~20% required alternative feeding by age 2 | (martelli2024clinicalspectrumof pages 3-4, martelli2024clinicalspectrumof pages 2-3, mirandafilho2025characterizationof843 pages 2-3) |
| Feeding-Growth | Low birth weight (HP:0001518) | 10%–43.8% across cohorts; 23.9% in one infant cohort up to 12 months | IPD meta-analysis; observational cohort | Reflects prenatal growth effects and heterogeneity | (mirandafilho2025characterizationof843 pages 2-3) |
| Feeding-Growth | Linear growth deficit / short stature (HP:0004322) | 39.1% of length-for-age measurements below deficit threshold in one cohort; stunting in literature 14.3%–57.1% | Infant cohort; systematic review of malnutrition studies | Often linked to dysphagia and feeding difficulty | (mirandafilho2025characterizationof843 pages 2-3) |
| Feeding-Growth | Underweight / wasting (HP:0004325) | Underweight 14.3%–54.4%; wasting 4.3%–48.0% | Systematic review of observational studies in children with CZS | Reflects chronic nutritional vulnerability | (mirandafilho2025characterizationof843 pages 2-3) |
| Other | Urological impairment | Frequency not pooled; repeatedly reported as common comorbidity | Brazil cohort review | Included as part of broader multisystem CZS spectrum | (martelli2024clinicalspectrumof pages 1-2) |
| Other | Hospitalization burden | 41.4% in children with microcephaly vs 16.2% in normocephalic peers | Brazil cohorts summarized in review | Likely reflects feeding, neurologic, and respiratory complications | (martelli2024clinicalspectrumof pages 3-4) |
| Other | Mortality | 11.3-fold higher mortality up to 36 months in children with CZS / Zika-related microcephaly vs unexposed peers | Systematic review summary | Severe disease substantially increases early-childhood mortality | (shah2024analysisofcongenital pages 13-15) |

| Epidemiology statistic | Estimate | Population / timeframe | Notes | Supporting citation IDs |
|---|---:|---|---|---|
| CZS proportion among ZIKV-infected pregnancies | 4.65% (95% CI 3.38–6.67%) | Systematic review/meta-analysis of ZIKV epidemiology | Pooled estimate for CZS among infected pregnancies | (mccain2026asystematicreview pages 1-2, mccain2026asystematicreview pages 7-7) |
| Countries/territories with documented autochthonous mosquito-borne ZIKV transmission | 92 | Global status as of Dec 2023 | Transmission likely underrecognized because many infections are asymptomatic/mild | (rabe2025areviewof pages 1-2, rabe2025areviewof pages 3-4) |
| Brazil confirmed CZS cases | 1,858 confirmed; 2,960 suspected under investigation | 2015 to epidemiological week 31 of 2023 | National surveillance; cases fell sharply after 2017 | (martelli2024clinicalspectrumof pages 1-2) |
| Brazil 2023 reported Zika cases | 54,116 cases; incidence 25/100,000; 6,201 laboratory confirmed | Brazil, 2023 | Brazil accounted for 97% of reported Americas cases in preliminary 2023 surveillance | (rabe2025areviewof pages 4-5) |
| Preliminary Americas Zika cases in 2023 | 55,813 cases from 14 countries; 4 deaths | Americas, 2023 preliminary surveillance | 11% laboratory confirmed | (rabe2025areviewof pages 4-5) |


*Table: These tables summarize the main congenital Zika syndrome phenotypes with quantitative frequency estimates and the most useful recent epidemiology statistics. They are designed for rapid knowledge-base extraction and link each major claim to supporting context IDs.*

Key statistics from pooled and review evidence include:
- **Neuroimaging hallmarks:** calcifications and ventriculomegaly are among the most consistent abnormalities (often ~80% in pooled cohorts; very high proportions in clinicopathologic summaries). (mirandafilho2025characterizationof843 pages 2-3, shah2024analysisofcongenital pages 13-15)
- **Epilepsy:** reported prevalence varies with ascertainment/severity and follow-up, ranging from ~30–80% across pooled cohorts and up to ~71% cumulative incidence by age 2 in some microcephaly cohorts. (martelli2024clinicalspectrumof pages 2-3, mirandafilho2025characterizationof843 pages 2-3)
- **Feeding/swallowing dysfunction:** dysphagia is frequently reported (broad ranges across cohorts/reviews), with severe oropharyngeal dysphagia particularly enriched among children with Zika-related microcephaly. (martelli2024clinicalspectrumof pages 3-4)

### 3.3 Age of onset, progression, severity
- **Onset:** Congenital, with abnormalities present at birth or emerging postnatally (e.g., postnatal microcephaly can occur). (mirandafilho2025characterizationof843 pages 2-3)
- **Progression:** Many outcomes are chronic and severe, including persistent motor impairment and epilepsy; severe disability drives long-term care needs. (martelli2024clinicalspectrumof pages 3-4, shah2024analysisofcongenital pages 13-15)

### 3.4 Quality of life and family impact
A 2023 integrative review (31 studies) described caregiver burdens spanning social, psychological, economic/material, and health domains, with quantified mental-health burdens in some studies (e.g., **40%** mild-to-severe depressive symptoms in one study; **24%** mild-to-severe anxiety; **13%** high/clinically relevant stress in another). Publication date: **2023-05**; URL: https://doi.org/10.1590/1413-81232023285.14852022en (melo2023congenitalzikasyndrome pages 11-12)

## 4. Genetic / Molecular Information

### 4.1 Causal genes
CZS is not classically a monogenic disease; the causal factor is infectious (ZIKV). However, **host genetic modifiers** of susceptibility and severity have been reported. (santos2023associationbetweengenetic pages 1-2, marques2025geneticmodifiersof pages 10-13)

### 4.2 Pathogenic variants / modifier loci (host genetics)
A 2023 case–control candidate-gene study (Brazil; 245 individuals including mother–infant pairs) reported associations between:
- **TREM1 rs2234246** with CZS occurrence (e.g., CC genotype OR reported ~4.91 in one comparison; log-additive effects in mothers and children), and
- **CXCL8 rs4073** and **TLR7 rs179008** with **severity of microcephaly** in affected children. Publication date: **2023-03**; URL: https://doi.org/10.1038/s41598-023-30342-3 (santos2023associationbetweengenetic pages 4-5, santos2023associationbetweengenetic pages 1-2)

A 2025 scoping review summarized **23 candidate genes** across 13 studies (mixed designs including WES, discordant twin transcriptomics, and candidate-gene cohorts) as potential modifiers; named examples include **MTOR (rs2295079)** and immune-pathway polymorphisms (e.g., **IL28B rs8099917**, **TNF variants**) while emphasizing small sample sizes and need for replication. Publication date: **2025-01**; URL: https://doi.org/10.1101/2025.01.02.25319896 (marques2025geneticmodifiersof pages 10-13)

### 4.3 Epigenetics and chromosomal abnormalities
No specific epigenetic signatures or recurrent chromosomal abnormalities were identified in the retrieved evidence for this run.

## 5. Environmental Information

### 5.1 Infectious agent
- **Pathogen:** Zika virus (ZIKV), primarily mosquito-borne (Aedes spp.) with additional sexual and vertical transmission routes. (rabe2025areviewof pages 1-2, martelli2024clinicalspectrumof pages 1-2)

### 5.2 Environmental/lifestyle contributors
Environmental conditions that facilitate **Aedes** proliferation (standing water, household exposure, and broader ecological suitability) indirectly increase risk of maternal infection; prevention focuses on vector control and personal protective measures. (crisantolopez2023congenitalzikasyndrome pages 8-10)

## 6. Mechanism / Pathophysiology (current model)

### 6.1 Causal chain from trigger to clinical manifestations
**Trigger:** Maternal ZIKV infection during pregnancy → **placental infection and vertical transmission** → fetal CNS infection and/or placental insufficiency/inflammatory injury → neurodevelopmental disruption → congenital malformations and long-term neurologic disability. (wong2025zikavirusand pages 3-5, wong2025zikavirusand pages 1-2)

Key mechanistic steps supported by recent reviews:
1. **Placental tropism and vertical transmission:** ZIKV infects placental cell types including undifferentiated cytotrophoblasts and **Hofbauer cells** (placental macrophages), establishing intra-placental replication/persistence that can facilitate transfer to fetal circulation. (wong2025zikavirusand pages 3-5)
2. **Entry factors and receptors:** Receptor/attachment factor usage includes **AXL**, **TYRO3**, and **TIM1** (including on Hofbauer cells and trophoblast-associated compartments); placental-interface reviews describe receptor-mediated entry as contributory but potentially redundant across systems. (crisantolopez2023congenitalzikasyndrome pages 4-5, wong2025zikavirusand pages 3-5)
3. **Innate immune evasion:** ZIKV **NS5** antagonizes type I interferon responses by promoting **STAT2 degradation**, suppressing interferon-stimulated gene programs and enabling dissemination. (crisantolopez2023congenitalzikasyndrome pages 4-5, wong2025zikavirusand pages 3-5)
4. **Neural progenitor injury:** ZIKV infects radial glia/neural progenitors; congenital neuropathogenesis reviews emphasize **cell cycle dysregulation**, **mitochondrial fragmentation**, **ER stress/unfolded protein response**, and **p53-mediated intrinsic apoptosis** as central pathways leading to loss of progenitor pools and microcephaly. (metzler2024zikavirusneuropathogenesis—research pages 1-2)
5. **Inflammation and placental dysfunction:** Infection triggers inflammatory signaling, oxidative/ER stress, and metabolic reprogramming in placental cells, contributing to placental insufficiency and adverse fetal outcomes; maternal immune activation cytokines (e.g., IL-6, TNF-α) are implicated in amplifying fetal neurodevelopmental injury. (wong2025zikavirusand pages 1-2, wong2025zikavirusand pages 3-5)

### 6.2 Suggested ontology terms (examples)
- **GO biological process (suggested):** type I interferon signaling pathway; response to virus; apoptotic process; ER stress response / unfolded protein response; regulation of cell cycle; neurogenesis. (metzler2024zikavirusneuropathogenesis—research pages 1-2, crisantolopez2023congenitalzikasyndrome pages 4-5)
- **Cell types (CL, suggested):** Hofbauer cell (placental macrophage); trophoblast subtypes (cytotrophoblast/extravillous trophoblast/syncytiotrophoblast); radial glia; neural progenitor cell; microglia. (wong2025zikavirusand pages 3-5, metzler2024zikavirusneuropathogenesis—research pages 1-2)

## 7. Anatomical Structures Affected

### 7.1 Primary organs and systems
- **CNS/brain:** primary target; includes cortical development abnormalities, ventriculomegaly, calcifications, and brain parenchymal loss. (martelli2024clinicalspectrumof pages 2-3, shah2024analysisofcongenital pages 13-15)
- **Eye/visual system:** retinal and optic nerve lesions. (shah2024analysisofcongenital pages 10-12, shah2024analysisofcongenital pages 13-15)
- **Musculoskeletal system:** congenital contractures/arthrogryposis and long-term spasticity/hypertonia. (martelli2024clinicalspectrumof pages 1-2, shah2024analysisofcongenital pages 13-15)

### 7.2 Tissue/cell level localization
Placenta (trophoblast lineages and fetal macrophages) is a key site of replication/persistence relevant to transmission; fetal neurogenic zones (ventricular/subventricular regions) are implicated in neural progenitor injury. (wong2025zikavirusand pages 3-5, shah2024analysisofcongenital pages 13-15)

## 8. Temporal Development (onset and progression)

- **Onset:** congenital; may present at birth or evolve (e.g., postnatal microcephaly). (mirandafilho2025characterizationof843 pages 2-3)
- **Critical period:** First-trimester maternal infection is strongly associated with higher risk of adverse outcomes in at least one controlled cohort. (venancio2025earlyandlongterm pages 1-3)

## 9. Inheritance and Population

### 9.1 Epidemiology and geographic distribution
- As of **December 2023**, autochthonous mosquito-borne ZIKV transmission had been documented in **92 countries/territories**. Publication date: **2025-02**; URL: https://doi.org/10.4269/ajtmh.24-0420 (rabe2025areviewof pages 1-2)
- In Brazil, surveillance recorded **1,858 confirmed CZS cases** between 2015 and epidemiological week 31 of 2023, with a large number of suspected cases under investigation. (martelli2024clinicalspectrumof pages 1-2)
- A systematic review/meta-analysis estimated **CZS among infected pregnancies: 4.65%** (95% CI 3.38–6.67%). (mccain2026asystematicreview pages 1-2)

### 9.2 Sex ratio / demographic patterns
The retrieved evidence did not provide a consistent, pooled sex ratio for CZS; cohort-level details exist but were not systematically extractable from the provided snippets.

## 10. Diagnostics

### 10.1 Laboratory testing and key constraints
Recent diagnostic synthesis emphasizes two major limitations:
- **Short NAT window in blood** due to transient viremia (often within ~≤7 days of symptom onset), and
- **Serologic cross-reactivity** among flaviviruses (especially dengue vs Zika), complicating IgG/IgM interpretation and requiring confirmatory neutralization testing (PRNT). Publication date: **2025-04**; URL: https://doi.org/10.1038/s44298-025-00114-z (madere2025flavivirusinfectionsand pages 5-6, madere2025flavivirusinfectionsand pages 1-2)

### 10.2 Imaging
Brain CT/MRI abnormalities (cortical atrophy, ventriculomegaly, calcifications) are used as structural markers of severity and part of clinical evaluation of suspected CZS. (martelli2024clinicalspectrumof pages 1-2)

### 10.3 Differential diagnosis
When congenital infection is suspected, evaluation should exclude other teratogenic infections (e.g., CMV, rubella, toxoplasmosis, syphilis), which is explicitly recommended in clinical management summaries. (crisantolopez2023congenitalzikasyndrome pages 8-10)

## 11. Outcome / Prognosis

### 11.1 Neurodevelopmental outcomes after exposure (with and without CZS)
Outcomes vary markedly by whether an infant has classic CZS/microcephaly versus antenatal exposure without congenital findings.
- In a matched cohort (Brazil), in utero exposure was associated with **IRR 2.7** (95% CI 1.4–5.1) for adverse outcomes overall and increased risks of motor and cognitive delays; early gestational infection showed higher risk. (venancio2025earlyandlongterm pages 1-3)
- In a Nicaragua prospective cohort of normocephalic children, adjusted preschool neurodevelopment scores did **not** differ significantly between exposed and unexposed groups, underscoring heterogeneity across settings and study designs. Publication date: **2024-07**; URL: https://doi.org/10.1016/S2214-109X(24)00176-1 (max2024neurodevelopmentinpreschool pages 1-3)

### 11.2 Mortality
A 2024 systematic clinicopathologic review summarized markedly increased early-childhood mortality in severe CZS presentations (reported as ~11.3-fold higher risk up to 36 months in one cited estimate). (shah2024analysisofcongenital pages 13-15)

## 12. Treatment

### 12.1 Current standard of care (real-world implementation)
There is **no specific curative treatment** for CZS; management is **supportive and multidisciplinary**, requiring constant monitoring, early intervention/rehabilitation, feeding/nutrition management, and management of epilepsy and motor impairment. (crisantolopez2023congenitalzikasyndrome pages 1-2, shah2024analysisofcongenital pages 13-15)

Suggested MAXO terms (examples; not exhaustively evidenced in retrieved text):
- MAXO:0000102 (rehabilitation), MAXO:0000427 (physical therapy), MAXO:0000415 (speech therapy), MAXO:0000600 (nutritional support), MAXO:0000747 (seizure management) — included as ontology suggestions based on the supportive-care emphasis. (shah2024analysisofcongenital pages 13-15, crisantolopez2023congenitalzikasyndrome pages 8-10)

### 12.2 Experimental / investigational countermeasures
Preclinical evidence summarized in an animal-model review notes repurposed antivirals (e.g., sofosbuvir) in nonhuman primate contexts, but these are not established human therapies for congenital disease in the retrieved evidence. (gardinali2025congenitalzikavirus pages 3-4)

## 13. Prevention

### 13.1 Primary prevention
Prevention focuses on reducing maternal infection risk:
- **Vector control and personal protection:** reduction of breeding sites, window/door screens, bed nets, covering clothing, and repellents (e.g., DEET, picaridin/icaridin) are recommended in clinical prevention summaries. (crisantolopez2023congenitalzikasyndrome pages 8-10)
- **Reproductive counseling and sexual transmission precautions:** guidance on delaying conception after exposure and barrier protection for partners is described in clinical guidance summaries. (crisantolopez2023congenitalzikasyndrome pages 8-10)

### 13.2 Vaccines (status: clinical development, not licensed)
Multiple Zika vaccines have been evaluated in clinical trials; several have completed early-phase studies:
- **mRNA vaccine (mRNA-1893; Moderna):** Phase 2, randomized observer-blind placebo-controlled; **COMPLETED**; enrollment 808; completion date 2024-07-26; results posted Sept 2025. ClinicalTrials.gov: NCT04917861. (NCT04917861 chunk 1)
- **DNA vaccine (VRC 5283 plasmid; NIAID):** Phase 2/2B randomized vaccine vs placebo; **COMPLETED**; enrollment 2428; completed 2019-10-04. ClinicalTrials.gov: NCT03110770. (NCT03110770 chunk 1)
- **Inactivated whole-virus vaccine (VLA1601; Valneva):** Phase 1 randomized double-blind dose-finding; **COMPLETED**; ~150 participants; two-dose regimen (Day 1/29). ClinicalTrials.gov: NCT06334393. (NCT06334393 chunk 1)

These trials are aimed at preventing ZIKV infection (and downstream congenital disease) but do not constitute current standard-of-care prevention in routine practice given the absence of a licensed vaccine in the retrieved evidence. (rabe2025areviewof pages 1-2, NCT04917861 chunk 1)

## 14. Other Species / Natural Disease
ZIKV congenital outcomes are modeled across species; the evidence here primarily supports experimental susceptibility rather than naturally occurring veterinary disease burdens.

## 15. Model Organisms (mechanism and translational research)

### 15.1 Major model systems and what they recapitulate
- **Human brain organoids / iPSC-derived neural progenitors:** reproduce preferential infection of neural progenitors and outcomes such as reduced organoid size, thinner cortical layers, and increased cell death; useful for mechanistic dissection and therapeutic screening but lower throughput and complex. (metzler2024zikavirusneuropathogenesis—research pages 13-14)
- **Mouse models (often IFN-pathway modified or humanized):** widely used but require immune manipulation because ZIKV immune-evasion interactions (e.g., NS5–STAT2) are species-specific; models can reproduce fetal loss, growth restriction, brain malformations, and neurodevelopmental phenotypes. (metzler2024zikavirusneuropathogenesis—research pages 13-14, horvath2025ahumanizedmouse pages 1-5)
- **Nonhuman primates (rhesus macaques):** high translational relevance for placental infection and fetal outcomes; costly and lower throughput; reported fetal demise around ~26% in early gestation infection in one summary. (metzler2024zikavirusneuropathogenesis—research pages 13-14)

### 15.2 Limitations
Key limitations include differences in placentation/anatomy and interferon biology across species, and the need for immune suppression/genetic modification in many rodent studies, which can distort the human-like spectrum. (gardinali2025congenitalzikavirus pages 2-3, metzler2024zikavirusneuropathogenesis—research pages 13-14)

## Expert opinion and synthesis (authoritative analyses)
- Surveillance-focused experts emphasize that ZIKV remains a public-health threat due to re-emergence potential, diagnostic limitations, and ongoing transmission across many regions, recommending targeted surveillance and clear testing algorithms. (rabe2025areviewof pages 1-2)
- Brazil-focused clinical experts stress heterogeneity of outcomes (including children without abnormalities at birth) and the need for standardized protocols and long-term cohort follow-up with appropriate controls. (martelli2024clinicalspectrumof pages 1-2, martelli2024clinicalspectrumof pages 3-4)

## Evidence limitations / gaps for knowledge-base completion
- Formal identifiers beyond **ICD-11 KA62.0** (e.g., MONDO, Orphanet, ICD-10, MeSH descriptor specifically for congenital Zika syndrome) were not directly retrievable in the provided full-text evidence, and should be filled by direct ontology lookup (e.g., ICD-11 MMS browser, MONDO, MeSH). (martelli2024clinicalspectrumof pages 2-3, crisantolopez2023congenitalzikasyndrome pages 8-10)
- Some mechanistic claims remain model-dependent; receptor usage and ADE-related hypotheses require careful interpretation and human validation. (wong2025zikavirusand pages 2-3)



References

1. (martelli2024clinicalspectrumof pages 1-2): Celina Maria Turchi Martelli, Fanny Cortes, Sinval Pinto Brandão-Filho, Marilia Dalva Turchi, Wayner Vieira de Souza, Thalia Velho Barreto de Araújo, Ricardo Arraes de Alencar Ximenes, and Demócrito de Barros Miranda-Filho. Clinical spectrum of congenital zika virus infection in brazil: update and issues for research development. Revista da Sociedade Brasileira de Medicina Tropical, Jul 2024. URL: https://doi.org/10.1590/0037-8682-0153-2024, doi:10.1590/0037-8682-0153-2024. This article has 12 citations.

2. (crisantolopez2023congenitalzikasyndrome pages 1-2): Israel E. Crisanto-López, Pablo López-De Jesús, Jacqueline López-Quecho, and Juan C. Flores-Alonso. Congenital zika syndrome. Boletín Médico del Hospital Infantil de México, Mar 2023. URL: https://doi.org/10.24875/bmhim.22000110, doi:10.24875/bmhim.22000110. This article has 15 citations.

3. (martelli2024clinicalspectrumof pages 2-3): Celina Maria Turchi Martelli, Fanny Cortes, Sinval Pinto Brandão-Filho, Marilia Dalva Turchi, Wayner Vieira de Souza, Thalia Velho Barreto de Araújo, Ricardo Arraes de Alencar Ximenes, and Demócrito de Barros Miranda-Filho. Clinical spectrum of congenital zika virus infection in brazil: update and issues for research development. Revista da Sociedade Brasileira de Medicina Tropical, Jul 2024. URL: https://doi.org/10.1590/0037-8682-0153-2024, doi:10.1590/0037-8682-0153-2024. This article has 12 citations.

4. (NCT03110770 chunk 4):  VRC 705: A Zika Virus DNA Vaccine in Healthy Adults and Adolescents. National Institute of Allergy and Infectious Diseases (NIAID). 2017. ClinicalTrials.gov Identifier: NCT03110770

5. (crisantolopez2023congenitalzikasyndrome pages 8-10): Israel E. Crisanto-López, Pablo López-De Jesús, Jacqueline López-Quecho, and Juan C. Flores-Alonso. Congenital zika syndrome. Boletín Médico del Hospital Infantil de México, Mar 2023. URL: https://doi.org/10.24875/bmhim.22000110, doi:10.24875/bmhim.22000110. This article has 15 citations.

6. (mirandafilho2025characterizationof843 pages 2-3): Demócrito de Barros Miranda-Filho, Ricardo Arraes de Alencar Ximenes, Ulisses Ramos Montarroyos, Marília Rosa Abtibol-Bernardino, Elizabeth B. Brickley, Celina Maria Turchi Martelli, Laura Cunha Rodrigues, Thália Velho Barreto de Araújo, Liana O. Ventura, Mariana Carvalho Leal, Darci Neves Santos, Letícia Marques dos Santos, Lucas Monteiro Santos, Mariana Rabelo Gomes, Isadora Cristina de Siqueira, Letícia Serra, Débora Patrícia Medeiros Santos Rios, Alessandra Carvalho, Antônio Moura Silva, Patrícia Silva Sousa, Marizélia Costa Ribeiro, Marcos Garcia Campos, Saulo Duarte Passos, Ana Paula Paschoalicchio Bertozzi, Rosa Estela Gazeta, Daniel T. Catalan, Ricardo Queiroz Gurgel, Aline de Siqueira Alves Lopes, Andrea Monteiro Correia Medeiros, Patrícia Brasil, Karin Nielsen-Saines, Zilton Vasconcelos, Andrea Araújo Zin, Marisa Márcia Mussi-Pinhata, Silvia Fabiana Biason de Moura Negrini, Bento Vidal de Moura Negrini, Carla Andrea Cardoso Tanuri Caldas, Daniela Vivacqua, Bernadete Perez Coelho, Lucíola de Fátima Albuquerque de Almeida Peixoto, Camila Bôtto-Menezes, Silvana Gomes Benzecry, Consuelo Silva de Oliveira, Joelma Karin Sagica Fernandes Paschoal, Emilene Monteiro Furtado Serra, Luna Thais Sousa Gomes, Maria Elisabeth Moreira, and Cristina Barroso Hofer. Characterization of 843 children with zika-related microcephaly in the first three years of life: an individual participant data meta-analysis of 12 cohorts in the zika brazilian cohorts consortium. PLOS Global Public Health, 5(12):e0005425, Dec 2025. URL: https://doi.org/10.1371/journal.pgph.0005425, doi:10.1371/journal.pgph.0005425. This article has 1 citations and is from a peer-reviewed journal.

7. (rabe2025areviewof pages 4-5): Ingrid B. Rabe, Susan L. Hills, Joana M. Haussig, Allison T. Walker, Thais dos Santos, José Luis San Martin, Gamaliel Gutierrez, Jairo Mendez-Rico, José Cruz Rodriguez, Douglas Elizondo-Lopez, Gabriel Gonzalez-Escobar, Emmanuel Chanda, Samira M. Al Eryani, Chiori Kodama, Aya Yajima, Manish Kakkar, Masaya Kato, Pushpa R. Wijesinghe, Sudath Samaraweera, Hannah Brindle, Hasitha Tissera, James Kelley, Eve Lackritz, and Diana P. Rojas. A review of the recent epidemiology of zika virus infection. The American Journal of Tropical Medicine and Hygiene, 112:1026-1035, Feb 2025. URL: https://doi.org/10.4269/ajtmh.24-0420, doi:10.4269/ajtmh.24-0420. This article has 63 citations.

8. (melo2023congenitalzikasyndrome pages 11-12): Ana Paula Lopes de Melo, Tereza Maciel Lyra, Jessyka Mary Vasconcelos Barbosa, and Thália Velho Barreto de Araújo. Congenital zika syndrome and family impacts: an integrative review. Ciência &amp; Saúde Coletiva, May 2023. URL: https://doi.org/10.1590/1413-81232023285.14852022en, doi:10.1590/1413-81232023285.14852022en. This article has 14 citations.

9. (crisantolopez2023congenitalzikasyndrome pages 4-5): Israel E. Crisanto-López, Pablo López-De Jesús, Jacqueline López-Quecho, and Juan C. Flores-Alonso. Congenital zika syndrome. Boletín Médico del Hospital Infantil de México, Mar 2023. URL: https://doi.org/10.24875/bmhim.22000110, doi:10.24875/bmhim.22000110. This article has 15 citations.

10. (wong2025zikavirusand pages 3-5): Sam Chak Sum Wong, Joshua Fung, Pak-Ting Hau, Yanjie Guo, Philip C. N. Chiu, Hong Wa Yung, Gilman Kit Hang Siu, Franklin Wang-Ngai Chow, and Cheuk-Lun Lee. Zika virus and the fetal-maternal interface: deciphering the mechanisms of placental infection and implications for pregnancy outcomes. Jul 2025. URL: https://doi.org/10.1080/22221751.2025.2532681, doi:10.1080/22221751.2025.2532681. This article has 6 citations and is from a domain leading peer-reviewed journal.

11. (venancio2025earlyandlongterm pages 1-3): Fabio Antonio Venancio, Maria Eulina Quilião, Sanny Cerqueira de Oliveira Gabeira, Amanda Torrentes de Carvalho, Silvia Helena dos Santos Leite, Sheila Maria Barbosa de Lima, Nathalia dos Santos Alves, Luma da Cruz Moura, Waleska Dias Schwarcz, Adriana de Souza Azevedo, Luiz Henrique Ferraz Demarchi, Marina Castilhos Souza Umaki Zardin, Gislene Garcia de Castro Lichs, Deborah Ledesma Taira, Wagner de Souza Fernandes, Natália Oliveira Alves, Aline Etelvina Casaril Arrua, Ana Isabel do Nascimento, Lisany Krug Mareto, Micael Viana de Azevedo, Camila Guadeluppe Maciel, Márcio José de Medeiros, Moreno Magalhães de Souza Rodrigues, Zilton Vasconcelos, Karin Nielsen-Saines, Rivaldo Venâncio da Cunha, Cláudia Du Bocage Santos-Pinto, and Everton Falcão de Oliveira. Early and long-term adverse outcomes of in utero zika exposure. Pediatrics, Jan 2025. URL: https://doi.org/10.1542/peds.2024-067552, doi:10.1542/peds.2024-067552. This article has 11 citations and is from a highest quality peer-reviewed journal.

12. (mccain2026asystematicreview pages 1-2): Kelly McCain, Anna Vicco, Christian Morgenstern, Thomas Rawson, Tristan M. Naidoo, Sangeeta Bhatia, Dominic P. Dee, Patrick Doohan, Keith Fraser, Anna-Maria Hartner, Sequoia I. Leuba, Shazia Ruybal-Pesántez, Richard J. Sheppard, H. Juliette T. Unwin, Kelly Charniga, Zulma M. Cucunubá, Gina Cuomo-Dannenburg, Natsuko Imai-Eaton, Edward S. Knock, Adam Kucharski, Mantra Kusumgar, Paul Liétar, Rebecca K. Nash, Sabine van Elsland, Aaron Morris, Alpha Forna, Amy Dighe, Anna-Maria Hartner, Anne Cori, Arran Hamlet, Ben Lambert, Bethan Cracknell Daniels, Charles Whittaker, Cosmo Santoni, Cyril Geismar, Dariya Nikitin, David Jorgensen, Dominic P. Dee, Edward S. Knock, Hayley Thompson, Isobel Routledge, Jack Wardle, Janetta Skarp, Joseph Hicks, Kanchan Parchani, Kieran Drake, Lily Geidelberg, Lorenzo Cattarino, Mara Kont, Marc Baguelin, Pablo N. Perez-Guzman, Paula Christen, Rebecca Nash, Richard Fitzjohn, Richard Sheppard, Rob Johnson, Sabine van Elsland, Sequoia I. Leuba, Shazia Ruybal-Pesántez, Sreejith Radhakrishnan, Tristan M. Naidoo, Zulma M. Cucunubá, Nuno R. Faria, Anne Cori, Ruth McCabe, and Ilaria Dorigatti. A systematic review and meta-analysis of zika virus epidemiology. Nature Health, 1:355-367, Feb 2026. URL: https://doi.org/10.1038/s44360-025-00051-4, doi:10.1038/s44360-025-00051-4. This article has 1 citations.

13. (shah2024analysisofcongenital pages 13-15): Dhaara Shah, Dhairavi Shah, Olivia Mua, and Rana Zeine. Analysis of congenital zika syndrome clinicopathologic findings reported in the 8 years since the brazilian outbreak. Exploration of Neuroprotective Therapy, pages 82-99, Feb 2024. URL: https://doi.org/10.37349/ent.2024.00072, doi:10.37349/ent.2024.00072. This article has 3 citations.

14. (wong2025zikavirusand pages 2-3): Sam Chak Sum Wong, Joshua Fung, Pak-Ting Hau, Yanjie Guo, Philip C. N. Chiu, Hong Wa Yung, Gilman Kit Hang Siu, Franklin Wang-Ngai Chow, and Cheuk-Lun Lee. Zika virus and the fetal-maternal interface: deciphering the mechanisms of placental infection and implications for pregnancy outcomes. Jul 2025. URL: https://doi.org/10.1080/22221751.2025.2532681, doi:10.1080/22221751.2025.2532681. This article has 6 citations and is from a domain leading peer-reviewed journal.

15. (martelli2024clinicalspectrumof pages 3-4): Celina Maria Turchi Martelli, Fanny Cortes, Sinval Pinto Brandão-Filho, Marilia Dalva Turchi, Wayner Vieira de Souza, Thalia Velho Barreto de Araújo, Ricardo Arraes de Alencar Ximenes, and Demócrito de Barros Miranda-Filho. Clinical spectrum of congenital zika virus infection in brazil: update and issues for research development. Revista da Sociedade Brasileira de Medicina Tropical, Jul 2024. URL: https://doi.org/10.1590/0037-8682-0153-2024, doi:10.1590/0037-8682-0153-2024. This article has 12 citations.

16. (shah2024analysisofcongenital pages 10-12): Dhaara Shah, Dhairavi Shah, Olivia Mua, and Rana Zeine. Analysis of congenital zika syndrome clinicopathologic findings reported in the 8 years since the brazilian outbreak. Exploration of Neuroprotective Therapy, pages 82-99, Feb 2024. URL: https://doi.org/10.37349/ent.2024.00072, doi:10.37349/ent.2024.00072. This article has 3 citations.

17. (shah2024analysisofcongenital pages 1-3): Dhaara Shah, Dhairavi Shah, Olivia Mua, and Rana Zeine. Analysis of congenital zika syndrome clinicopathologic findings reported in the 8 years since the brazilian outbreak. Exploration of Neuroprotective Therapy, pages 82-99, Feb 2024. URL: https://doi.org/10.37349/ent.2024.00072, doi:10.37349/ent.2024.00072. This article has 3 citations.

18. (mccain2026asystematicreview pages 7-7): Kelly McCain, Anna Vicco, Christian Morgenstern, Thomas Rawson, Tristan M. Naidoo, Sangeeta Bhatia, Dominic P. Dee, Patrick Doohan, Keith Fraser, Anna-Maria Hartner, Sequoia I. Leuba, Shazia Ruybal-Pesántez, Richard J. Sheppard, H. Juliette T. Unwin, Kelly Charniga, Zulma M. Cucunubá, Gina Cuomo-Dannenburg, Natsuko Imai-Eaton, Edward S. Knock, Adam Kucharski, Mantra Kusumgar, Paul Liétar, Rebecca K. Nash, Sabine van Elsland, Aaron Morris, Alpha Forna, Amy Dighe, Anna-Maria Hartner, Anne Cori, Arran Hamlet, Ben Lambert, Bethan Cracknell Daniels, Charles Whittaker, Cosmo Santoni, Cyril Geismar, Dariya Nikitin, David Jorgensen, Dominic P. Dee, Edward S. Knock, Hayley Thompson, Isobel Routledge, Jack Wardle, Janetta Skarp, Joseph Hicks, Kanchan Parchani, Kieran Drake, Lily Geidelberg, Lorenzo Cattarino, Mara Kont, Marc Baguelin, Pablo N. Perez-Guzman, Paula Christen, Rebecca Nash, Richard Fitzjohn, Richard Sheppard, Rob Johnson, Sabine van Elsland, Sequoia I. Leuba, Shazia Ruybal-Pesántez, Sreejith Radhakrishnan, Tristan M. Naidoo, Zulma M. Cucunubá, Nuno R. Faria, Anne Cori, Ruth McCabe, and Ilaria Dorigatti. A systematic review and meta-analysis of zika virus epidemiology. Nature Health, 1:355-367, Feb 2026. URL: https://doi.org/10.1038/s44360-025-00051-4, doi:10.1038/s44360-025-00051-4. This article has 1 citations.

19. (rabe2025areviewof pages 1-2): Ingrid B. Rabe, Susan L. Hills, Joana M. Haussig, Allison T. Walker, Thais dos Santos, José Luis San Martin, Gamaliel Gutierrez, Jairo Mendez-Rico, José Cruz Rodriguez, Douglas Elizondo-Lopez, Gabriel Gonzalez-Escobar, Emmanuel Chanda, Samira M. Al Eryani, Chiori Kodama, Aya Yajima, Manish Kakkar, Masaya Kato, Pushpa R. Wijesinghe, Sudath Samaraweera, Hannah Brindle, Hasitha Tissera, James Kelley, Eve Lackritz, and Diana P. Rojas. A review of the recent epidemiology of zika virus infection. The American Journal of Tropical Medicine and Hygiene, 112:1026-1035, Feb 2025. URL: https://doi.org/10.4269/ajtmh.24-0420, doi:10.4269/ajtmh.24-0420. This article has 63 citations.

20. (rabe2025areviewof pages 3-4): Ingrid B. Rabe, Susan L. Hills, Joana M. Haussig, Allison T. Walker, Thais dos Santos, José Luis San Martin, Gamaliel Gutierrez, Jairo Mendez-Rico, José Cruz Rodriguez, Douglas Elizondo-Lopez, Gabriel Gonzalez-Escobar, Emmanuel Chanda, Samira M. Al Eryani, Chiori Kodama, Aya Yajima, Manish Kakkar, Masaya Kato, Pushpa R. Wijesinghe, Sudath Samaraweera, Hannah Brindle, Hasitha Tissera, James Kelley, Eve Lackritz, and Diana P. Rojas. A review of the recent epidemiology of zika virus infection. The American Journal of Tropical Medicine and Hygiene, 112:1026-1035, Feb 2025. URL: https://doi.org/10.4269/ajtmh.24-0420, doi:10.4269/ajtmh.24-0420. This article has 63 citations.

21. (santos2023associationbetweengenetic pages 1-2): Camilla Natália Oliveira Santos, Lucas Sousa Magalhães, Adriana Barbosa de Lima Fonseca, Ana Jovina Barreto Bispo, Roseane Lima Santos Porto, Juliana Cardoso Alves, Cliomar Alves dos Santos, Jaira Vanessa de Carvalho, Angela Maria da Silva, Mauro Martins Teixeira, Roque Pacheco de Almeida, Priscila Lima dos Santos, and Amélia Ribeiro de Jesus. Association between genetic variants in trem1, cxcl10, il4, cxcl8 and tlr7 genes with the occurrence of congenital zika syndrome and severe microcephaly. Scientific Reports, Mar 2023. URL: https://doi.org/10.1038/s41598-023-30342-3, doi:10.1038/s41598-023-30342-3. This article has 22 citations and is from a peer-reviewed journal.

22. (marques2025geneticmodifiersof pages 10-13): Fernanda J P Marques, Janet Ruan, Rozel B. Razal, Marcio Leyser, and Youssef A. Kousa. Genetic modifiers of prenatal brain injury after zika virus infection: a scoping review. medRxiv : the preprint server for health sciences, Jan 2025. URL: https://doi.org/10.1101/2025.01.02.25319896, doi:10.1101/2025.01.02.25319896. This article has 0 citations.

23. (santos2023associationbetweengenetic pages 4-5): Camilla Natália Oliveira Santos, Lucas Sousa Magalhães, Adriana Barbosa de Lima Fonseca, Ana Jovina Barreto Bispo, Roseane Lima Santos Porto, Juliana Cardoso Alves, Cliomar Alves dos Santos, Jaira Vanessa de Carvalho, Angela Maria da Silva, Mauro Martins Teixeira, Roque Pacheco de Almeida, Priscila Lima dos Santos, and Amélia Ribeiro de Jesus. Association between genetic variants in trem1, cxcl10, il4, cxcl8 and tlr7 genes with the occurrence of congenital zika syndrome and severe microcephaly. Scientific Reports, Mar 2023. URL: https://doi.org/10.1038/s41598-023-30342-3, doi:10.1038/s41598-023-30342-3. This article has 22 citations and is from a peer-reviewed journal.

24. (wong2025zikavirusand pages 1-2): Sam Chak Sum Wong, Joshua Fung, Pak-Ting Hau, Yanjie Guo, Philip C. N. Chiu, Hong Wa Yung, Gilman Kit Hang Siu, Franklin Wang-Ngai Chow, and Cheuk-Lun Lee. Zika virus and the fetal-maternal interface: deciphering the mechanisms of placental infection and implications for pregnancy outcomes. Jul 2025. URL: https://doi.org/10.1080/22221751.2025.2532681, doi:10.1080/22221751.2025.2532681. This article has 6 citations and is from a domain leading peer-reviewed journal.

25. (metzler2024zikavirusneuropathogenesis—research pages 1-2): Anna D. Metzler and Hengli Tang. Zika virus neuropathogenesis—research and understanding. Pathogens, 13:555, Jul 2024. URL: https://doi.org/10.3390/pathogens13070555, doi:10.3390/pathogens13070555. This article has 23 citations.

26. (madere2025flavivirusinfectionsand pages 5-6): Ferralita S. Madere, Aurea Virginia Andrade da Silva, Efemena Okeze, Emma Tilley, Andriyan Grinev, Krishnamurthy Konduru, Mayra García, and Maria Rios. Flavivirus infections and diagnostic challenges for dengue, west nile and zika viruses. npj Viruses, Apr 2025. URL: https://doi.org/10.1038/s44298-025-00114-z, doi:10.1038/s44298-025-00114-z. This article has 43 citations.

27. (madere2025flavivirusinfectionsand pages 1-2): Ferralita S. Madere, Aurea Virginia Andrade da Silva, Efemena Okeze, Emma Tilley, Andriyan Grinev, Krishnamurthy Konduru, Mayra García, and Maria Rios. Flavivirus infections and diagnostic challenges for dengue, west nile and zika viruses. npj Viruses, Apr 2025. URL: https://doi.org/10.1038/s44298-025-00114-z, doi:10.1038/s44298-025-00114-z. This article has 43 citations.

28. (max2024neurodevelopmentinpreschool pages 1-3): Ryan Max, Christian Toval-Ruiz, Sylvia Becker-Dreps, Anna M Gajewski, Evelin Martinez, Kaitlyn Cross, Bryan Blette, Oscar Ortega, Damaris Collado, Omar Zepeda, Itziar Familiar, Michael J Boivin, Meylin Chavarria, María José Meléndez, Juan Carlos Mercado, Aravinda de Silva, Matthew H Collins, Daniel Westreich, Sandra Bos, Eva Harris, Angel Balmaseda, Emily W Gower, Natalie M Bowman, Elizabeth Stringer, and Filemón Bucardo. Neurodevelopment in preschool children exposed and unexposed to zika virus in utero in nicaragua: a prospective cohort study. The Lancet. Global health, 12:e1129-e1138, Jul 2024. URL: https://doi.org/10.1016/s2214-109x(24)00176-1, doi:10.1016/s2214-109x(24)00176-1. This article has 7 citations.

29. (gardinali2025congenitalzikavirus pages 3-4): Noemi Rovaris Gardinali, Renato Sergio Marchevsky, Yara Cavalcante Vieira, Marcelo Pelajo-Machado, Tatiana Kugelmeier, Juliana Gil Melgaço, Márcio Pinto Castro, Jaqueline Mendes de Oliveira, and Marcelo Alves Pinto. Congenital zika virus infection in laboratory animals: a comparative review highlights translational studies on the maternal-foetal interface. Memórias do Instituto Oswaldo Cruz, Feb 2025. URL: https://doi.org/10.1590/0074-02760240125, doi:10.1590/0074-02760240125. This article has 1 citations.

30. (NCT04917861 chunk 1):  A Study of Zika Vaccine mRNA-1893 in Adult Participants Living in Endemic and Non-Endemic Flavivirus Areas. ModernaTX, Inc.. 2021. ClinicalTrials.gov Identifier: NCT04917861

31. (NCT03110770 chunk 1):  VRC 705: A Zika Virus DNA Vaccine in Healthy Adults and Adolescents. National Institute of Allergy and Infectious Diseases (NIAID). 2017. ClinicalTrials.gov Identifier: NCT03110770

32. (NCT06334393 chunk 1):  Phase 1 Trial to Assess the Safety and Immunogenicity of an Inactivated, Adjuvanted Whole Zika Virus Vaccine Candidate (VLA1601) in Healthy Adults. Valneva Austria GmbH. 2024. ClinicalTrials.gov Identifier: NCT06334393

33. (metzler2024zikavirusneuropathogenesis—research pages 13-14): Anna D. Metzler and Hengli Tang. Zika virus neuropathogenesis—research and understanding. Pathogens, 13:555, Jul 2024. URL: https://doi.org/10.3390/pathogens13070555, doi:10.3390/pathogens13070555. This article has 23 citations.

34. (horvath2025ahumanizedmouse pages 1-5): Allison R. Horvath, Clara M. Abdelmalek, Eunbin Park, Aubrey P. Alexander, Sadhana A. Maheswaran, Arnav H. Patel, Nandi G. Patel, Janet E. Ruan, Ademide T. Adeyemo, Erin C. Li, Katherine E. Helmicki, Stephen Lin, Paul C. Wang, Zhen Li, Li Wang, Heather A. Gordish-Dressman, Tarik F. Haydar, Tamer A. Mansour, and Youssef A. Kousa. A humanized mouse model system mimics prenatal zika infection and reveals premature differentiation of neural stem cells. bioRxiv, Feb 2025. URL: https://doi.org/10.1101/2025.02.21.639556, doi:10.1101/2025.02.21.639556. This article has 2 citations.

35. (gardinali2025congenitalzikavirus pages 2-3): Noemi Rovaris Gardinali, Renato Sergio Marchevsky, Yara Cavalcante Vieira, Marcelo Pelajo-Machado, Tatiana Kugelmeier, Juliana Gil Melgaço, Márcio Pinto Castro, Jaqueline Mendes de Oliveira, and Marcelo Alves Pinto. Congenital zika virus infection in laboratory animals: a comparative review highlights translational studies on the maternal-foetal interface. Memórias do Instituto Oswaldo Cruz, Feb 2025. URL: https://doi.org/10.1590/0074-02760240125, doi:10.1590/0074-02760240125. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](Congenital_Zika_Syndrome-deep-research-falcon_artifacts/artifact-00.md)
