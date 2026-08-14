---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-24T08:17:11.625571'
end_time: '2026-07-24T08:27:23.134439'
duration_seconds: 611.51
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Spinocerebellar Ataxia Type 15/16
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Spinocerebellar_Ataxia_Type_15_16-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spinocerebellar Ataxia Type 15/16
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar Ataxia Type 15/16** covering all of the
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
- **Disease Name:** Spinocerebellar Ataxia Type 15/16
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar Ataxia Type 15/16** covering all of the
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


# Spinocerebellar Ataxia Type 15/16: Disease-Characteristics Report

## Executive summary

Spinocerebellar ataxia type 15/16 (SCA15/16) is a rare, autosomal-dominant, predominantly adult-onset cerebellar disorder caused by heterozygous pathogenic variants in **ITPR1**, most characteristically multi-exon or whole-gene deletions producing IP3R1 haploinsufficiency. Its classic phenotype is a relatively “pure” cerebellar syndrome—gait and limb ataxia, dysarthria, nystagmus, and action/head tremor—with cerebellar vermis-predominant atrophy and unusually slow progression. Typical onset is 30–50 years, although the reported range is 7–66 years; many affected people remain independently ambulant or use only a cane 10–40 years after onset. SCA16 was shown to share the same ITPR1 loss-of-function basis as SCA15 and is now generally treated as the same entity, SCA15/16. (tada2014ip3receptorsin pages 5-8, prestori2019disruptedcalciumsignaling pages 8-10)

The core disease mechanism is impaired IP3-triggered calcium release from the endoplasmic reticulum in cerebellar Purkinje cells. Abnormal calcium homeostasis disrupts dendritic integration and firing, eventually producing Purkinje-cell dysfunction or loss and impaired cerebellar output. There is no approved disease-modifying therapy or SCA15/16-specific interventional trial; current care is genetic counseling, rehabilitation, assistive care, and symptom management. (ghorbani2023copynumbervariant pages 4-6, hisatsune2013ip3r1deficiencyin pages 1-2, shimobayashi2018calciumsignalingpkc pages 1-2, brown2012computationalanalysisof pages 1-3, matsugi2025effectsofphysiotherapy pages 1-2)

The following table provides a compact knowledge-base representation; the narrative below expands and qualifies it.

| Domain | Summary | Suggested ontologies / terms | Key evidence / citations |
|---|---|---|---|
| Definition / identifiers | Spinocerebellar ataxia type 15/16 (SCA15/16) is an autosomal-dominant, usually adult-onset, very slowly progressive **pure cerebellar ataxia** linked to **ITPR1**. MONDO: **MONDO:0011694**. Disease knowledge is derived from **aggregated disease-level resources and published family/case series**, not EHR-derived evidence alone. | MONDO:0011694; MeSH/ICD/Orphanet/OMIM should be verified in source databases before KB entry if exact IDs are required. | OpenTargets links **ITPR1** to “spinocerebellar ataxia type 15/16” with evidence support; reviews describe SCA15/16 as a distinct ITPR1-associated ataxia (OpenTargets Search: spinocerebellar ataxia type 15-ITPR1, tada2014ip3receptorsin pages 5-8) |
| Gene / variant classes | **Causal gene:** **ITPR1** (inositol 1,4,5-trisphosphate receptor type 1). Reported pathogenic classes include **heterozygous multi-exon/whole-gene deletions** and **heterozygous missense variants** (e.g., **p.Pro1059Leu**, **p.Val494Ile** in reviews). 2023 Dutch cohort found a pathogenic familial deletion involving **ITPR1 exons 1–41** plus part of **SUMF1**. Germline origin is typical. | HGNC: ITPR1; variant classes: CNV deletion, missense; molecular consequence often consistent with loss of function / haploinsufficiency. | Deletions involving exons 1–10, 1–40, 1–44, 1–48 and complete gene are summarized in reviews; 2023 cohort identified a 260.8 kb deletion including **ITPR1 exons 1–41** in two related patients (hisatsune2017ip3receptormutations pages 10-13, hisatsune2017ip3receptormutations pages 7-10, ghorbani2023copynumbervariant pages 2-4, ghorbani2023copynumbervariant pages 1-2, ghorbani2023copynumbervariant pages 4-6) |
| Inheritance | **Autosomal dominant**. Penetrance appears **age-dependent** and expressivity **variable**, but precise penetrance estimates are not well established in retrieved evidence. Germline mosaicism is reported for other **ITPR1-associated** phenotypes (especially SCA29-like presentations), but this is not established as a common mechanism for classic SCA15/16. | HPO inheritance term: Autosomal dominant inheritance. | SCA15 is repeatedly described as autosomal dominant; mosaicism evidence in 2023 paper pertains to broader ITPR1-associated ataxia, not classic adult-onset SCA15/16 (tada2014ip3receptorsin pages 5-8, kleyner2023itpr1associatedspinocerebellarataxia pages 18-21) |
| Onset / course | Typical onset is **adult**, often **30–50 years**, with reported range **7–66 years**. Course is **chronic**, **insidious**, and **very slowly progressive**; many patients remain ambulatory independently or with a cane **10–40 years after onset**. | HPO: Adult onset; Progressive ataxia; Chronic course. | Reviews summarizing family series report onset range 7–66 years, usual onset 30–50 years, and long-preserved ambulation (tada2014ip3receptorsin pages 5-8) |
| Core phenotypes | Predominant phenotype is a **pure cerebellar syndrome**: gait/limb ataxia, tremor, dysarthria, gaze-evoked nystagmus or other oculomotor abnormalities, and sometimes hyperreflexia without clear pyramidal syndrome. Suggested HPO terms: **Ataxia**, **Gait ataxia**, **Limb ataxia**, **Dysarthria**, **Nystagmus**, **Intention tremor / Action tremor**, **Head tremor**, **Hyperreflexia**. Cognitive function is often reported as preserved in classic SCA15/16; epilepsy is generally not a feature of classic disease. | HPO terms should be mapped during curation; avoid adding exact IDs here unless verified. | Clinical spectrum summarized in reviews; 2023 Dutch familial cases had limb ataxia, vermian atrophy, father with dysarthria, nystagmus, polyneuropathy (tada2014ip3receptorsin pages 5-8, ghorbani2023copynumbervariant pages 4-6) |
| Anatomy / cell types | Primary anatomy: **cerebellum**, especially **cerebellar vermis** with milder hemispheric involvement; secondarily cerebellar output pathways may be affected functionally. Primary vulnerable cell type: **Purkinje cell**. Other involved structures in mechanistic models include **inferior olive** and **brainstem/cerebellar circuits**. | UBERON: cerebellum, cerebellar vermis (exact IDs not inserted if uncertain); CL: Purkinje cell, cerebellar neuron (exact IDs should be verified). | MRI commonly shows vermian-predominant cerebellar atrophy; mechanistic mouse work localizes causal dysfunction to cerebellum/brainstem Purkinje-cell circuits (tada2014ip3receptorsin pages 5-8, ghorbani2023copynumbervariant pages 4-6, prestori2019disruptedcalciumsignaling pages 8-10, hisatsune2013ip3r1deficiencyin pages 1-2) |
| Mechanism / pathophysiology | Upstream lesion: reduced or altered **IP3R1** function. Core mechanism: **ITPR1 haploinsufficiency** impairs **IP3-mediated Ca2+ release from the endoplasmic reticulum** in Purkinje cells, disrupting intracellular calcium homeostasis, dendritic integration/development, firing patterns, and cerebellar output; downstream consequences include Purkinje-cell dysfunction and cerebellar ataxia, with degeneration over time. Relevant GO processes: **inositol trisphosphate-mediated signaling**, **calcium ion release from endoplasmic reticulum**, **regulation of cytosolic calcium ion concentration**, **Purkinje cell development**, **synaptic signaling**. | GO terms should be finalized by ontology lookup before production use. | Reviews and models converge on abnormal IP3/Ca2+ signaling in Purkinje cells; 2023 CNV paper explicitly supports haploinsufficiency from reduced ITPR1 dosage; conditional cerebellum/brainstem knockout mice show dystonia/ataxia via abnormal Purkinje-cell firing (hisatsune2017ip3receptormutations pages 10-13, ghorbani2023copynumbervariant pages 4-6, prestori2019disruptedcalciumsignaling pages 8-10, hisatsune2013ip3r1deficiencyin pages 1-2, shimobayashi2018calciumsignalingpkc pages 1-2, brown2012computationalanalysisof pages 1-3) |
| Diagnostics | Diagnosis relies on **molecular confirmation of ITPR1 pathogenic variant** in a patient with compatible slowly progressive cerebellar ataxia. Testing approaches include **sequence analysis** plus **CNV analysis** because deletions may be missed by SNV-only workflows. Useful methods: **targeted ataxia panel**, **WES/WGS with CNV calling**, **SNP array**, **MLPA/gene dosage analysis** where available. MRI supports diagnosis by showing cerebellar, often vermian-predominant, atrophy. Differential diagnosis includes other dominant ataxias and **ITPR1-related SCA29/Gillespie syndrome**. | MAXO not applicable; HPO/UBERON can annotate MRI and phenotype findings. | 2023 Dutch study recommends adding CNV analysis for at least **ITPR1** in SCA diagnostics; inherited ataxia review emphasizes NGS-based workup after exclusion of acquired causes (ghorbani2023copynumbervariant pages 1-2, coarelli2023theinheritedcerebellar pages 1-2) |
| Treatment / management | **No disease-modifying therapy specific to SCA15/16** was identified. Current management is **supportive and rehabilitative**: physical therapy, balance/gait/coordination training, occupational therapy, speech therapy, mobility aids, and standard symptomatic management of tremor or other complications as clinically indicated. General degenerative cerebellar ataxia evidence suggests physiotherapy can modestly improve ataxia severity. | MAXO suggestions: physical therapy, gait training, balance training, occupational therapy, speech therapy, assistive device use. Exact MAXO IDs should be verified before insertion. | No relevant SCA15/16-specific interventional trial surfaced. Meta-analysis in degenerative cerebellar ataxia found physiotherapy reduced SARA by **−1.41** overall, though evidence certainty was low (matsugi2025effectsofphysiotherapy pages 1-2, coarelli2023theinheritedcerebellar pages 1-2) |
| Prognosis | Prognosis is generally one of **slow functional decline** rather than shortened survival in classic cases. Ambulation is often preserved for decades, and severe bulbar/fatal complications are not emphasized in classic SCA15/16 reports. Quality-of-life burden is expected from chronic imbalance, tremor, speech impairment, and activity limitation, but disease-specific QoL datasets were not retrieved. | HPO/ICF mapping may be useful for disability annotations. | Long-preserved ambulation and slow progression are consistently reported in reviews; quantitative survival data were not found in retrieved sources (tada2014ip3receptorsin pages 5-8) |
| Epidemiology | Absolute population prevalence/incidence of **SCA15/16** is not well established in retrieved evidence. Reported frequency among dominant ataxia families varies by cohort: about **2.7%** in Australian families, **1.8%** in a cohort of **333 White/Caucasian dominant ataxia families**, and **8.9%** in Central European families; disease appears **rare in Japanese cohorts**. In a 2023 Dutch unsolved ataxia cohort, clinically relevant SCA-gene CNV deletions were found in **3/292 (1%)** high-quality samples, with pathogenic **ITPR1** deletion in **2 related patients**. | Epidemiology fields should note “rare” and “family-series based estimates.” | Frequencies are from review summaries of family cohorts, not population screening; Dutch 2023 CNV study provides recent diagnostic-yield data (tada2014ip3receptorsin pages 5-8, ghorbani2023copynumbervariant pages 1-2, ghorbani2023copynumbervariant pages 4-6) |
| Models | Relevant models include **Itpr1 heterozygous/null mice**, **Itpr1 Δ18/Δ18** and **Δ18/wt** mice with reduced IP3R1 levels, and **conditional Wnt1-Cre;Itpr1 flox/flox** cerebellum/brainstem knockout mice. These models recapitulate impaired coordination/ataxia and abnormal Purkinje-cell physiology; conditional knockout also shows dystonia linked to Purkinje-cell firing abnormalities. Computational Purkinje-cell calcium models predict that altered IP3R1 abundance/sensitivity can normalize or disrupt calcium responses. | Model organism: mouse; cell type: Purkinje cell. | Mouse and computational studies support causal links between ITPR1 dosage, Ca2+ signaling, Purkinje firing, and motor phenotype (hisatsune2013ip3r1deficiencyin pages 1-2, brown2012computationalanalysisof pages 1-3) |
| Evidence limitations | Evidence base is dominated by **small family series, case reports, and reviews**. Precise **phenotype frequencies, penetrance, survival, carrier frequency, sex ratio, and population prevalence** are poorly quantified. Some recent ITPR1 papers describe **SCA29 or broader ITPR1 syndromes**, which should not be conflated with classic adult-onset SCA15/16. Several exact ontology IDs beyond MONDO were not verified in the retrieved context and should be checked before KB ingestion. | Curation note: separate **SCA15/16** from **SCA29**, **Gillespie syndrome**, and other ITPR1-associated disorders. | Recent evidence improves diagnostic and mechanistic clarity but remains sparse for natural history and treatment-specific outcomes (kleyner2023itpr1associatedspinocerebellarataxia pages 18-21, ghorbani2023copynumbervariant pages 1-2, coarelli2023theinheritedcerebellar pages 1-2) |


*Table: This table provides a concise knowledge-base style summary of Spinocerebellar Ataxia Type 15/16, covering identifiers, genetics, phenotypes, mechanism, diagnostics, treatment, prognosis, epidemiology, and models. It also flags evidence gaps and separates classic adult-onset SCA15/16 from other ITPR1-associated disorders.*

## 1. Disease information

### Definition and nomenclature

SCA15/16 is a Mendelian neurodegenerative ataxia in the autosomal-dominant spinocerebellar ataxia group. Synonyms include **spinocerebellar ataxia type 15**, **SCA15**, **spinocerebellar ataxia type 16**, **SCA16**, **SCA15/16**, and, less specifically, **ITPR1-associated ataxia**. “SCA16” arose from a Japanese kindred but was subsequently shown to result from an ITPR1 deletion, establishing allelism with SCA15; some experts have therefore called SCA16 a “vacant SCA” designation. (ghorbani2023copynumbervariant pages 7-8, prestori2019disruptedcalciumsignaling pages 8-10)

**Key identifiers**

- **MONDO:** [MONDO:0011694](https://monarchinitiative.org/disease/MONDO:0011694), spinocerebellar ataxia type 15/16. Open Targets associates this disease specifically with ITPR1. (OpenTargets Search: spinocerebellar ataxia type 15-ITPR1)
- **Gene:** **ITPR1**, Ensembl **ENSG00000150995**; approved name *inositol 1,4,5-trisphosphate receptor type 1*. (OpenTargets Search: spinocerebellar ataxia type 15-ITPR1)
- Exact OMIM, Orphanet, MeSH, ICD-10, and ICD-11 identifiers were not verified in the retrieved primary-source corpus and should be checked directly before production ingestion. ICD systems generally classify it under hereditary ataxia rather than assigning a subtype-specific code.

The evidence is primarily **aggregated disease-level evidence** from pedigrees, case series, diagnostic cohorts, reviews, and model systems. It is not principally an individual-EHR-derived phenotype definition.

## 2. Etiology, risk, and protective factors

### Causal factor

The primary cause is a **heterozygous germline pathogenic variant in ITPR1**. Large deletions have involved exons 1–10, 1–40, 1–44, 1–48, most or all of the gene, and sometimes adjacent **SUMF1** or **SETMAR** sequence. The recurring observation that heterozygous SUMF1 deficiency does not cause a movement disorder, together with reduced ITPR1 RNA/protein in deletion carriers, identifies ITPR1 haploinsufficiency—not SUMF1 loss—as the causal mechanism. (hisatsune2017ip3receptormutations pages 10-13, hisatsune2017ip3receptormutations pages 7-10, ghorbani2023copynumbervariant pages 2-4, ghorbani2023copynumbervariant pages 4-6)

Reported SCA15/16 missense substitutions include **p.Pro1059Leu** and **p.Val494Ile**. p.Pro1059Leu lies in a regulatory region and showed approximately twofold greater IP3-binding affinity than wild-type receptor in one experimental context, indicating that not every allele is a simple null and that variant effects may be cell-type dependent. (hisatsune2017ip3receptormutations pages 10-13)

### Risk factors

- **Genetic:** carrying a pathogenic heterozygous ITPR1 allele and having an affected parent are the established risks. Each child of a heterozygous affected individual ordinarily has a 50% transmission probability.
- **Age:** penetrance is plausibly age-dependent because onset can be late, but a reliable age-specific penetrance curve is unavailable.
- **Sex:** no established sex bias.
- **Environmental, infectious, occupational, diet, alcohol, smoking, or toxin risks:** none are established as causes or modifiers of SCA15/16. Such exposures remain important differential causes of acquired ataxia, not demonstrated SCA15/16 risk factors. (coarelli2023theinheritedcerebellar pages 1-2)
- **Protective factors or modifier genes:** no validated genetic or environmental protective factor was identified.
- **Gene–environment interaction:** no disease-specific interaction has been established.

## 3. Phenotypes

The classic phenotype is a slowly progressive, predominantly pure cerebellar syndrome. Available publications are small and do not support robust percentages for most individual findings. Suggested ontology mappings should therefore carry qualitative rather than fabricated frequencies.

- **Gait and balance ataxia:** usually the presenting or dominant sign; chronic and slowly progressive. Suggested HPO: *Ataxia*, *Gait ataxia*, *Unsteady gait*.
- **Limb dysmetria/ataxia and truncal ataxia:** common cerebellar signs. Suggested HPO: *Limb ataxia*, *Truncal ataxia*, *Dysmetria*.
- **Dysarthria/ataxic speech:** common but variably present. Suggested HPO: *Dysarthria*.
- **Oculomotor abnormalities:** gaze-evoked nystagmus and impaired oculocephalic reflex have been described. Suggested HPO: *Nystagmus*, *Abnormality of ocular movements*.
- **Tremor:** postural, action/intention, and head tremor may precede or accompany gait ataxia. Suggested HPO: *Intention tremor*, *Postural tremor*, *Head tremor*.
- **Hyperreflexia:** may occur without spasticity or extensor plantar responses. Suggested HPO: *Hyperreflexia*.
- **Episodic dystonic symptoms:** described in some cases but not a defining or consistently frequent feature. Suggested HPO: *Dystonia*. (prestori2019disruptedcalciumsignaling pages 8-10)
- **Peripheral neuropathy:** atypical but possible. In the 2023 Dutch father–daughter pair, both had limb ataxia and vermian atrophy; only the father had dysarthria and polyneuropathy, illustrating variable expressivity. (ghorbani2023copynumbervariant pages 2-4, ghorbani2023copynumbervariant pages 4-6)
- **Cognition and epilepsy:** cognition is usually preserved, and epilepsy is not characteristic of classic SCA15/16. Developmental delay, intellectual disability, congenital ataxia, craniofacial anomalies, aniridia, or fixed congenital mydriasis should prompt consideration of other ITPR1 phenotypes rather than automatic expansion of the SCA15/16 phenotype. (tada2014ip3receptorsin pages 5-8, kleyner2023itpr1associatedspinocerebellarataxia pages 18-21)

### Quality-of-life impact

Disease-specific EQ-5D, SF-36, or PROMIS datasets were not found. Expected burdens include falls, restricted community mobility, difficulty with fine motor tasks, impaired speech intelligibility, loss of driving or employment capacity, and increasing need for aids. The unusually slow course can preserve independence for decades, but chronic imbalance and tremor still produce meaningful disability.

## 4. Genetic and molecular information

**ITPR1** encodes IP3R1, a tetrameric, IP3-gated calcium-release channel in the endoplasmic-reticulum membrane. The disorder is usually caused by germline heterozygous deletion or other loss of function. Somatic variants are not an established cause. Population frequencies for individual pathogenic alleles were not available in the retrieved evidence; causal large deletions are expected to be absent or exceptionally rare in reference populations.

A 2023 Dutch study identified a **260.8-kb heterozygous deletion at 3p26.1**, GRCh37 coordinates 4,503,353–4,764,171, removing **ITPR1 exons 1–41** and **SUMF1 exons 1–2** in a father and daughter. The deletion was represented by 108 SNP probes and absent from 3,280 internal controls. Both patients developed symptoms at approximately age 40 and had slow progression and vermian atrophy. (ghorbani2023copynumbervariant pages 2-4, ghorbani2023copynumbervariant pages 4-6)

No validated modifier gene or SCA15/16-specific DNA-methylation, histone, or chromatin signature has been established. No recurrent aneuploidy or balanced rearrangement defines the disease; the relevant structural lesions are focal heterozygous CNV deletions at the ITPR1 locus.

## 5. Environmental information

SCA15/16 is not infectious, toxic, nutritional, or occupational in origin. No pathogen, radiation exposure, pollutant, lifestyle behavior, or environmental prophylaxis is known to alter its occurrence. Alcohol and sedating or cerebellotoxic drugs may pragmatically worsen balance in any ataxic patient, but this is symptom aggravation rather than demonstrated disease modification. Acquired toxic, autoimmune, vascular, metabolic, and infectious ataxias must nevertheless be excluded during diagnosis. (coarelli2023theinheritedcerebellar pages 1-2)

## 6. Mechanism and pathophysiology

### Causal chain

1. A heterozygous deletion or functionally disruptive ITPR1 variant reduces or alters IP3R1.
2. IP3R1-mediated release of calcium from the smooth ER is reduced or mistimed.
3. Purkinje cells are disproportionately vulnerable because IP3R1 is highly expressed in their soma and dendrites and supports mGluR1–PLC–IP3 calcium signaling, synaptic plasticity, dendritic integration, and firing precision.
4. Calcium-homeostasis disturbance impairs dendritic development or maintenance, synaptic integration, and Purkinje-cell firing.
5. Purkinje dysfunction and later degeneration disturb inhibitory output from cerebellar cortex to deep cerebellar nuclei, producing gait/limb incoordination, dysarthria, oculomotor signs, and tremor. (ghorbani2023copynumbervariant pages 4-6, prestori2019disruptedcalciumsignaling pages 8-10, hisatsune2013ip3r1deficiencyin pages 1-2, shimobayashi2018calciumsignalingpkc pages 1-2)

**Direct mechanistic quotation:** the 2023 CNV study states that deletion of one ITPR1 copy produces reduced RNA and protein and that “haploinsufficiency of ITPR1 is very likely the underlying disease mechanism”; it further links haploinsufficiency to “aberrant intracellular Ca2+ homeostasis and dysfunction of Purkinje cells that ultimately causes their degeneration.” (ghorbani2023copynumbervariant pages 4-6)

Suggested GO concepts include *inositol trisphosphate-mediated signaling*, *calcium ion release from endoplasmic reticulum*, *regulation of cytosolic calcium ion concentration*, *regulation of synaptic plasticity*, *Purkinje cell development*, and *neuron projection development*. Relevant cellular compartments are the **endoplasmic-reticulum membrane**, Purkinje-cell soma, and dendritic arbor. Suggested cell type: **cerebellar Purkinje cell**.

There is no established SCA15/16-specific inflammatory, immune, metabolomic, lipidomic, single-cell, spatial-transcriptomic, proteomic, or epigenomic signature. Computational modeling predicts that increasing residual IP3R1 sensitivity might normalize calcium responses when receptor abundance is not too low, but this remains a preclinical hypothesis, not a treatment recommendation. (brown2012computationalanalysisof pages 1-3)

## 7. Anatomical structures affected

The primary organ is the **central nervous system**, particularly the **cerebellum**. MRI usually shows marked **cerebellar vermis atrophy** with milder hemispheric atrophy; bilateral, symmetric involvement is expected rather than focal lateralization. The principal tissue is cerebellar cortex and the key cell population is the Purkinje neuron. Functional downstream structures include deep cerebellar nuclei, inferior olive, brainstem, and cerebello-thalamo-cortical motor networks. (tada2014ip3receptorsin pages 5-8, ghorbani2023copynumbervariant pages 4-6, hisatsune2013ip3r1deficiencyin pages 1-2)

Suggested terms: UBERON *cerebellum*, *cerebellar cortex*, *cerebellar vermis*, *cerebellar hemisphere*, *inferior olivary complex*; CL *Purkinje cell*; GO cellular component *endoplasmic reticulum membrane*. Exact IDs should be validated against current ontology releases.

## 8. Temporal development

Onset is insidious and most often adult, usually 30–50 years, with a reported 7–66-year range. The course is chronic, lifelong, and very slowly progressive rather than episodic or relapsing-remitting. A practical staging scheme is: early imbalance/tremor; established gait and limb ataxia with dysarthria/ocular signs; and later mobility-aid dependence. Formal SCA15/16 stages or validated progression coefficients are unavailable. Most reported individuals remain independently ambulant or use a cane 10–40 years after onset. No spontaneous or treatment-induced remission pattern is recognized. (tada2014ip3receptorsin pages 5-8)

## 9. Inheritance and population

Inheritance is **autosomal dominant**, with variable expressivity and likely age-dependent penetrance. Genetic anticipation is not expected because SCA15/16 is not a repeat-expansion disorder. Germline mosaicism has been reported in broader ITPR1-associated developmental ataxia, but is not established as a common mechanism in classic SCA15/16. Founder effects, consanguinity, carrier frequency, and sex ratio are insufficiently characterized. (kleyner2023itpr1associatedspinocerebellarataxia pages 18-21)

Population prevalence and incidence are unknown. Family-cohort estimates cited in reviews include approximately **2.7% of Australian dominant-ataxia families**, **1.8% of 333 White/Caucasian dominant-ataxia families**, and **8.9% in a Central European series**, with rarity in Japanese cohorts. These are diagnostic proportions, not general-population prevalence estimates. (tada2014ip3receptorsin pages 5-8)

In the 2023 Dutch cohort, 338 unsolved ataxia patients were screened; after exclusion of 46 low-quality samples, 3/292 (1%) carried potentially relevant SCA-gene deletions. Two were related individuals with the same pathogenic ITPR1 deletion, so this does not imply a 0.68% population prevalence. (ghorbani2023copynumbervariant pages 2-4, ghorbani2023copynumbervariant pages 1-2)

## 10. Diagnostics

### Clinical and imaging assessment

Evaluate slowly progressive cerebellar gait disorder, limb dysmetria, dysarthria, ocular motor signs, and tremor; obtain a three-generation pedigree and brain MRI. MRI evidence of vermian-predominant cerebellar atrophy supports but does not establish the diagnosis. SARA or ICARS can quantify severity, but neither is a diagnostic biomarker. No validated blood, CSF, urine, electrophysiologic, biopsy, proteomic, or metabolomic biomarker is specific for SCA15/16. (tada2014ip3receptorsin pages 5-8, coarelli2023theinheritedcerebellar pages 1-2)

### Genetic strategy

1. Exclude acquired and treatable ataxias and common repeat expansions appropriate to ancestry and phenotype.
2. Use a hereditary-ataxia panel, WES, or WGS that includes **ITPR1 sequence and CNV calling**.
3. If CNV sensitivity is uncertain, perform MLPA, quantitative dosage analysis, chromosomal microarray/SNP array, or validated read-depth analysis.
4. Confirm the variant and perform segregation/cascade testing when relatives are available.

A major 2023 practical conclusion was: “we suggest adding CNV analysis alongside SNV analysis to SCA gene diagnostics using next-generation sequencing approaches, at least for ITPR1.” (ghorbani2023copynumbervariant pages 1-2)

Conventional karyotyping is usually too insensitive. FISH is not first line but can confirm a known locus deletion. Mitochondrial testing and repeat-expansion assays are useful for differential diagnosis, not for detecting the canonical SCA15/16 lesion. WES can detect coding SNVs but may miss or incompletely resolve CNVs; WGS offers more uniform CNV and breakpoint detection.

### Differential diagnosis

Important alternatives include SCA5, SCA6, SCA11, SCA14, SCA26, FGF14-related ataxia/SCA27B, other dominant SCAs, CANVAS, FXTAS, immune-mediated ataxia, alcohol/drug toxicity, and structural cerebellar disease. ITPR1 allelic disorders require particular care:

- **SCA15/16:** usually adult-onset, slowly progressive, relatively pure cerebellar ataxia, often deletion/haploinsufficiency.
- **SCA29:** congenital or infantile-onset, usually nonprogressive developmental ataxia with motor delay and sometimes cognitive involvement, often missense variants.
- **Gillespie syndrome:** congenital aniridia/iris hypoplasia plus cerebellar ataxia and developmental impairment.

The 2023 p.Thr267Met family—with developmental delay, intellectual disability, craniofacial findings, and presumed germline mosaicism—fits a broader SCA29-like ITPR1 disorder and should not be used to redefine classic SCA15/16. (prestori2019disruptedcalciumsignaling pages 8-10, kleyner2023itpr1associatedspinocerebellarataxia pages 18-21)

## 11. Outcome and prognosis

No 5- or 10-year survival estimates, mortality rate, or disease-specific life-expectancy analysis is available. Classic SCA15/16 is not generally associated with early death; severe bulbar complications and epilepsy are not typical. Morbidity is mainly progressive mobility, coordination, speech, and fall-related disability. Recovery of lost neurologic function is not expected, although compensatory function can improve with rehabilitation and aids. Earlier onset, broader neurologic involvement, and more severe baseline ataxia may plausibly predict greater lifetime disability, but no validated SCA15/16 prognostic model or molecular biomarker exists. (tada2014ip3receptorsin pages 5-8)

## 12. Treatment and current implementation

No approved pharmacologic, gene, cell, RNA, immunologic, or surgical therapy modifies SCA15/16 progression. No SCA15/16-specific interventional NCT study was identified; a broad rare-disease registry, NCT01793168, is observational rather than a treatment trial.

Real-world care is multidisciplinary:

- physical therapy emphasizing balance, coordination, gait, strength, and aerobic conditioning;
- occupational therapy, home-safety modification, and adaptive equipment;
- cane, walker, or wheelchair assessment as required;
- speech-language therapy and swallowing assessment if symptoms arise;
- individualized treatment of tremor, dystonia, sleep, mood, pain, or neuropathy;
- fall prevention and avoidance of unnecessarily sedating/cerebellotoxic medication.

Suggested MAXO concepts include *physical therapy*, *gait training*, *balance training*, *occupational therapy*, *speech therapy*, *assistive-device use*, *brain MRI*, *molecular genetic testing*, and *genetic counseling*.

The latest retrieved rehabilitation synthesis was published **10 January 2025**, based on a search completed in 2024. Across 18 randomized trials and 398 people with degenerative cerebellar ataxia, 315 contributed to SARA meta-analysis; physiotherapy improved SARA by a mean **−1.41 points** (95% CI −2.16 to −0.66). Multi-aspect training, balance training, and aerobic training had respective mean differences of −1.59, −1.58, and −1.65 points, but certainty was low and risk of bias serious. These data support rehabilitation generally, not a proven SCA15/16-specific effect. DOI: [10.3389/fneur.2024.1491142](https://doi.org/10.3389/fneur.2024.1491142). (matsugi2025effectsofphysiotherapy pages 1-2)

## 13. Prevention

There is no vaccine, lifestyle prophylaxis, or population/newborn screening program. Primary prevention is reproductive: genetic counseling, cascade testing, and—where desired and legally available—prenatal diagnosis or preimplantation genetic testing after identification of a familial pathogenic variant. Secondary prevention consists of presymptomatic testing in competent at-risk adults after counseling and early surveillance for balance impairment. Tertiary prevention includes rehabilitation, fall prevention, assistive devices, and management of secondary deconditioning. Predictive testing in minors is generally deferred for an adult-onset disorder unless a clear childhood medical benefit exists.

## 14. Other species and natural disease

**Mus musculus** (NCBI Taxonomy **10090**) has an orthologous *Itpr1* gene and several spontaneous or engineered movement-disorder alleles. These are experimental or laboratory-observed models; a naturally occurring veterinary homolog in a defined companion-animal breed was not established in the retrieved evidence. SCA15/16 is not transmissible and has no zoonotic potential.

## 15. Model organisms

Mouse models include heterozygous and null *Itpr1* mice, *Itpr1* Δ18/wild-type and Δ18/Δ18 alleles, and conditional **Wnt1-Cre;Itpr1 flox/flox** deletion in cerebellum/brainstem. Heterozygous mice show motor discoordination; homozygous or tissue-specific severe depletion produces marked ataxia/dystonia, abnormal Purkinje-cell complex-spike patterns, feeding difficulty, and shortened survival. Inactivation of the cerebellum or inferior olive—and experimental removal of Purkinje cells—ameliorated dystonic output in the conditional model, demonstrating an olivocerebellar circuit origin independent of basal ganglia. (hisatsune2013ip3r1deficiencyin pages 1-2, brown2012computationalanalysisof pages 1-3)

These models strongly support dosage-sensitive IP3R1/Purkinje-cell physiology but can be more severe than heterozygous human SCA15/16 and therefore incompletely model its late onset and very slow progression. Computational Purkinje-cell models provide a complementary platform for testing how receptor abundance and sensitivity shape calcium release and membrane electrophysiology. (brown2012computationalanalysisof pages 1-3)

## Recent developments and evidence gaps

The most directly relevant recent advance is the **February 2023** Dutch CNV study, DOI [10.1212/NXG.0000000000200050](https://doi.org/10.1212/NXG.0000000000200050). It showed that large SCA-gene CNVs were rare but clinically decisive and argued that ITPR1 CNV analysis should be integrated with SNV analysis in modern NGS workflows. Its abstract reports: “Of the 338 patients with cerebellar ataxia, we identified putative clinically relevant CNV deletions in 3 patients,” including the pathogenic ITPR1 deletion in two related patients. (ghorbani2023copynumbervariant pages 1-2)

The **October 2023** p.Thr267Met report, DOI [10.1101/mcs.a006303](https://doi.org/10.1101/mcs.a006303), added evidence for parental germline mosaicism and craniofacial involvement across the wider ITPR1 disease spectrum, but its developmental SCA29-like phenotype is not classic SCA15/16. (kleyner2023itpr1associatedspinocerebellarataxia pages 18-21)

No disease-specific 2024 natural-history cohort, biomarker validation, omics atlas, or therapeutic trial was identified. Major knowledge gaps remain population prevalence, age-specific penetrance, longitudinal SARA progression, patient-reported quality of life, genotype–phenotype prediction for missense alleles, and disease-specific treatment response. Therefore, exact phenotype percentages, survival estimates, environmental modifiers, protective alleles, and treatment response rates should be recorded as **unknown**, rather than inferred from other SCA subtypes.

References

1. (tada2014ip3receptorsin pages 5-8): Masayoshi Tada, Masatoyo Nishizawa, and Osamu Onodera. Ip3 receptors in neurodegenerative disorders: spinocerebellar ataxias and huntington’s and alzheimer’s diseases. ArXiv, pages 579-600, Nov 2014. URL: https://doi.org/10.1007/978-3-642-40282-1\_28, doi:10.1007/978-3-642-40282-1\_28. This article has 2 citations.

2. (prestori2019disruptedcalciumsignaling pages 8-10): Francesca Prestori, Francesco Moccia, and Egidio D’Angelo. Disrupted calcium signaling in animal models of human spinocerebellar ataxia (sca). International Journal of Molecular Sciences, 21:216, Dec 2019. URL: https://doi.org/10.3390/ijms21010216, doi:10.3390/ijms21010216. This article has 42 citations.

3. (ghorbani2023copynumbervariant pages 4-6): Fatemeh Ghorbani, Eddy N. de Boer, Marloes Benjamins-Stok, Corien C. Verschuuren-Bemelmans, Jurjen Knapper, Jelkje de Boer-Bergsma, Jeroen J. de Vries, Birgit Sikkema-Raddatz, Dineke S. Verbeek, Helga Westers, and Cleo C. van Diemen. Copy number variant analysis of spinocerebellar ataxia genes in a cohort of dutch patients with cerebellar ataxia. Neurology: Genetics, Feb 2023. URL: https://doi.org/10.1212/nxg.0000000000200050, doi:10.1212/nxg.0000000000200050. This article has 10 citations.

4. (hisatsune2013ip3r1deficiencyin pages 1-2): Chihiro Hisatsune, Hiroyuki Miyamoto, Moritoshi Hirono, Naohide Yamaguchi, Takeyuki Sugawara, Naoko Ogawa, Etsuko Ebisui, Toshio Ohshima, Masahisa Yamada, Takao K. Hensch, Mitsuharu Hattori, and Katsuhiko Mikoshiba. Ip3r1 deficiency in the cerebellum/brainstem causes basal ganglia-independent dystonia by triggering tonic purkinje cell firings in mice. Frontiers in Neural Circuits, Oct 2013. URL: https://doi.org/10.3389/fncir.2013.00156, doi:10.3389/fncir.2013.00156. This article has 68 citations.

5. (shimobayashi2018calciumsignalingpkc pages 1-2): Etsuko Shimobayashi and Josef P. Kapfhammer. Calcium signaling, pkc gamma, ip3r1 and car8 link spinocerebellar ataxias and purkinje cell dendritic development. Jan 2018. URL: https://doi.org/10.2174/1570159x15666170529104000, doi:10.2174/1570159x15666170529104000. This article has 58 citations and is from a peer-reviewed journal.

6. (brown2012computationalanalysisof pages 1-3): Sherry-Ann Brown and Leslie M Loew. Computational analysis of calcium signaling and membrane electrophysiology in cerebellar purkinje neurons associated with ataxia. BMC Systems Biology, 6:70-70, Jun 2012. URL: https://doi.org/10.1186/1752-0509-6-70, doi:10.1186/1752-0509-6-70. This article has 32 citations and is from a peer-reviewed journal.

7. (matsugi2025effectsofphysiotherapy pages 1-2): Akiyoshi Matsugi, Kyota Bando, Yuki Kondo, Yutaka Kikuchi, Kazuhiro Miyata, Yuichi Hiramatsu, Yuya Yamanaka, Hiroaki Tanaka, Yuta Okuda, Koshiro Haruyama, and Yuichiro Yamasaki. Effects of physiotherapy on degenerative cerebellar ataxia: a systematic review and meta-analysis. Frontiers in Neurology, Jan 2025. URL: https://doi.org/10.3389/fneur.2024.1491142, doi:10.3389/fneur.2024.1491142. This article has 25 citations and is from a peer-reviewed journal.

8. (OpenTargets Search: spinocerebellar ataxia type 15-ITPR1): Open Targets Query (spinocerebellar ataxia type 15-ITPR1, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

9. (hisatsune2017ip3receptormutations pages 10-13): Chihiro Hisatsune and Katsuhiko Mikoshiba. Ip3 receptor mutations and brain diseases in human and rodents. Journal of Neurochemistry, 141:790-807, Jun 2017. URL: https://doi.org/10.1111/jnc.13991, doi:10.1111/jnc.13991. This article has 86 citations and is from a domain leading peer-reviewed journal.

10. (hisatsune2017ip3receptormutations pages 7-10): Chihiro Hisatsune and Katsuhiko Mikoshiba. Ip3 receptor mutations and brain diseases in human and rodents. Journal of Neurochemistry, 141:790-807, Jun 2017. URL: https://doi.org/10.1111/jnc.13991, doi:10.1111/jnc.13991. This article has 86 citations and is from a domain leading peer-reviewed journal.

11. (ghorbani2023copynumbervariant pages 2-4): Fatemeh Ghorbani, Eddy N. de Boer, Marloes Benjamins-Stok, Corien C. Verschuuren-Bemelmans, Jurjen Knapper, Jelkje de Boer-Bergsma, Jeroen J. de Vries, Birgit Sikkema-Raddatz, Dineke S. Verbeek, Helga Westers, and Cleo C. van Diemen. Copy number variant analysis of spinocerebellar ataxia genes in a cohort of dutch patients with cerebellar ataxia. Neurology: Genetics, Feb 2023. URL: https://doi.org/10.1212/nxg.0000000000200050, doi:10.1212/nxg.0000000000200050. This article has 10 citations.

12. (ghorbani2023copynumbervariant pages 1-2): Fatemeh Ghorbani, Eddy N. de Boer, Marloes Benjamins-Stok, Corien C. Verschuuren-Bemelmans, Jurjen Knapper, Jelkje de Boer-Bergsma, Jeroen J. de Vries, Birgit Sikkema-Raddatz, Dineke S. Verbeek, Helga Westers, and Cleo C. van Diemen. Copy number variant analysis of spinocerebellar ataxia genes in a cohort of dutch patients with cerebellar ataxia. Neurology: Genetics, Feb 2023. URL: https://doi.org/10.1212/nxg.0000000000200050, doi:10.1212/nxg.0000000000200050. This article has 10 citations.

13. (kleyner2023itpr1associatedspinocerebellarataxia pages 18-21): Robert Kleyner, Nathaniel Ung, Mohammad Arif, Elaine Marchi, Karen Amble, Maureen Gavin, Ricardo Madrid, and Gholson Lyon. Itpr1-associated spinocerebellar ataxia with craniofacial features—additional evidence for germline mosaicism. Cold Spring Harbor Molecular Case Studies, 9:a006303, Oct 2023. URL: https://doi.org/10.1101/mcs.a006303, doi:10.1101/mcs.a006303. This article has 3 citations and is from a peer-reviewed journal.

14. (coarelli2023theinheritedcerebellar pages 1-2): Giulia Coarelli, Thomas Wirth, Christine Tranchant, Michel Koenig, Alexandra Durr, and Mathieu Anheim. The inherited cerebellar ataxias: an update. Journal of Neurology, 270:208-222, Sep 2023. URL: https://doi.org/10.1007/s00415-022-11383-6, doi:10.1007/s00415-022-11383-6. This article has 91 citations and is from a domain leading peer-reviewed journal.

15. (ghorbani2023copynumbervariant pages 7-8): Fatemeh Ghorbani, Eddy N. de Boer, Marloes Benjamins-Stok, Corien C. Verschuuren-Bemelmans, Jurjen Knapper, Jelkje de Boer-Bergsma, Jeroen J. de Vries, Birgit Sikkema-Raddatz, Dineke S. Verbeek, Helga Westers, and Cleo C. van Diemen. Copy number variant analysis of spinocerebellar ataxia genes in a cohort of dutch patients with cerebellar ataxia. Neurology: Genetics, Feb 2023. URL: https://doi.org/10.1212/nxg.0000000000200050, doi:10.1212/nxg.0000000000200050. This article has 10 citations.

## Artifacts

- [Edison artifact artifact-00](Spinocerebellar_Ataxia_Type_15_16-deep-research-falcon_artifacts/artifact-00.md)