---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-19T15:26:58.920196'
end_time: '2026-06-19T15:44:40.456845'
duration_seconds: 1061.54
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: MED13 Syndrome
  mondo_id: MONDO:0032485
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 30
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: MED13_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: MED13_Syndrome-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MED13 Syndrome
- **MONDO ID:** MONDO:0032485 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MED13 Syndrome** covering all of the
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
- **Disease Name:** MED13 Syndrome
- **MONDO ID:** MONDO:0032485 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MED13 Syndrome** covering all of the
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


# Comprehensive Research Report: MED13 Syndrome (MONDO:0032485)

## Executive Summary

MED13 Syndrome, also termed intellectual developmental disorder-61 (MRD61) or MED13-associated neurodevelopmental disorder, is an extremely rare autosomal dominant condition caused by heterozygous pathogenic variants in the MED13 gene (OMIM #618009) (blok2018denovomutations pages 1-2, yang2025anovelframeshift pages 1-2, yang2025anovelframeshift pages 2-3). First comprehensively described by Blok and colleagues in 2018, this syndrome is characterized by universal developmental delay/intellectual disability, severe speech and language disorders, and variable features including autism spectrum disorder, attention deficit hyperactivity disorder, dysmorphic facial features, ophthalmologic abnormalities, and mild cardiac anomalies (blok2018denovomutations pages 1-2, blok2018denovomutations pages 4-5). As of 2025, approximately 26-30 cases have been documented worldwide (yang2025anovelframeshift pages 1-2, yang2025anovelframeshift pages 2-3). The disorder results from disrupted function of MED13, a critical subunit of the CDK8-kinase module within the Mediator complex, which regulates RNA polymerase II-mediated transcription (blok2018denovomutations pages 1-2, harper2018thecomplexstructure pages 1-2).

---

## 1. Disease Information

### Disease Definition and Overview

MED13 Syndrome is a novel neurodevelopmental disorder first systematically characterized in a 2018 GeneMatcher collaboration by Blok et al., who identified 13 affected individuals with protein-altering variants in the MED13 gene (blok2018denovomutations pages 1-2). The syndrome presents as "a neurodevelopmental disorder characterized by developmental delay and/or intellectual disability, including speech delays or disorders" along with a spectrum of additional features (blok2018denovomutations pages 1-2). As stated in the foundational publication, "All patients had intellectual disability and/or developmental delays, including speech delays or disorders" (blok2018denovomutations pages 1-2).

### Key Identifiers

- **OMIM ID**: #618009 (Intellectual Developmental Disorder-61, MRD61)
- **MONDO ID**: MONDO:0032485 (as specified by user)
- **MED13 Gene**: OMIM #603808; located at chromosome 17q23.2 (yang2025anovelframeshift pages 1-2, yang2025anovelframeshift pages 2-3)
- **ICD-11**: Not yet specifically coded; would fall under neurodevelopmental disorders
- **Category**: Mendelian disorder, autosomal dominant

### Alternative Names and Synonyms

- Intellectual Developmental Disorder-61 (MRD61)
- MED13-associated syndrome
- MED13-related neurodevelopmental disorder
- MED13-associated intellectual disability

### Data Source

Information is derived from aggregated disease-level resources including peer-reviewed case series, systematic genetic studies, and functional characterizations, not from individual patient electronic health records. Primary sources include the foundational 2018 Blok et al. cohort study (blok2018denovomutations pages 1-2), subsequent case reports from 2021-2025 (tolmacheva2024expandingphenotypeof pages 1-2, rivera2024med13genemutation pages 1-2, yang2025anovelframeshift pages 1-2, nardi2021couldthemed13 pages 1-2, yang2025anovelframeshift pages 2-3), and comprehensive reviews of Mediator complex disorders (fazio2025geneticclinicaland pages 1-2, fazio2025geneticclinicaland pages 2-4).

---

## 2. Etiology

### Disease Causal Factors

**Genetic Etiology (Primary Cause):**  
MED13 Syndrome is caused by heterozygous pathogenic variants in the MED13 gene (NM_005121.3), which encodes the Mediator complex subunit 13 (blok2018denovomutations pages 1-2, yang2025anovelframeshift pages 2-3). The MED13 gene consists of 30 exons and encodes a 2,174 amino acid protein (239.3 kDa) that serves as a component of the CDK8-kinase module of the Mediator complex (blok2018denovomutations pages 1-2, poss2013themediatorcomplex pages 2-3).

The disorder follows an autosomal dominant inheritance pattern with the vast majority of cases arising from de novo variants. In the original cohort of 13 patients, 11 variants were confirmed de novo, and only one was inherited from an affected mother to an affected child, demonstrating vertical transmission with variable expressivity (blok2018denovomutations pages 1-2, blok2018denovomutations pages 4-5).

**Mechanistic Basis:**  
MED13 is an essential component of the Mediator complex, a large multiprotein assembly (approximately 1.4 MDa in humans) that serves as a critical interface between gene-specific transcription factors and RNA polymerase II (harper2018thecomplexstructure pages 1-2, poss2013themediatorcomplex pages 2-3). As described by Harper and Taatjes (2018), "the Mediator complex is required for expression of most, if not all, pol II transcripts" (harper2018thecomplexstructure pages 1-2). MED13 specifically resides within the CDK8-kinase module, which consists of four proteins: MED13, MED12, CDK8, and cyclin C (blok2018denovomutations pages 1-2, poss2013themediatorcomplex pages 2-3).

### Risk Factors

**Genetic Risk Factors:**

*Causal Variants:* The disease is caused by heterozygous loss-of-function or specific gain-of-dysfunction variants in MED13. Variant types include:
- Nonsense mutations leading to premature termination (e.g., p.Leu131*, p.Arg1400*) (blok2018denovomutations pages 1-2, blok2018denovomutations pages 4-5)
- Frameshift variants causing truncation (e.g., p.Pro42Leufs*6, p.Arg1882Serfs*9) (blok2018denovomutations pages 1-2, yang2025anovelframeshift pages 2-3)
- Missense variants clustering in specific functional domains (blok2018denovomutations pages 1-2, blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11)
- In-frame deletions affecting critical residues (e.g., p.Thr326del) (blok2018denovomutations pages 1-2, blok2018denovomutations pages 6-7)

*Variant Classification:* All pathogenic MED13 variants identified in affected individuals are absent from population databases (gnomAD, TOPMED) and are predicted to be highly deleterious by multiple in silico tools, with CADD scores ranging from 20.5 to 41.0 (blok2018denovomutations pages 1-2, blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11).

*Modifier Genes:* The paralog MED13L may provide partial functional compensation. Studies in knockout mouse embryos demonstrated that "MED13L partially compensates for loss of MED13 function in preimplantation knockout embryos" (miao2018mediatorcomplexcomponent pages 1-2), suggesting genetic background effects involving MED13L expression levels could modify disease severity.

**Environmental Risk Factors:**  
No specific environmental risk factors have been identified for MED13 Syndrome, consistent with its genetic etiology as a de novo dominant Mendelian disorder.

### Protective Factors

No genetic or environmental protective factors have been specifically identified for MED13 Syndrome.

### Gene-Environment Interactions

Given the Mendelian nature of the disorder with predominantly de novo occurrence, traditional gene-environment interactions have not been characterized. However, epigenetic regulation of MED13 expression during development may influence phenotypic severity.

---

## 3. Phenotypes

MED13 Syndrome presents with a consistent core phenotype of neurodevelopmental impairment combined with variable additional features. Below is a comprehensive description of reported phenotypes.

| Phenotype / feature | Frequency among reported patients | Severity / variability | Typical age of onset | Suggested HPO term(s) | Key citations |
|---|---:|---|---|---|---|
| Developmental delay / global developmental delay | 13/13 (100%) in initial cohort; also core feature in later reports | Mild to severe; variable course | Infancy / early childhood | HP:0001263 Global developmental delay; HP:0011344 Severe global developmental delay | (blok2018denovomutations pages 1-2, blok2018denovomutations pages 7-11, tolmacheva2024expandingphenotypeof pages 1-2, yang2025anovelframeshift pages 1-2) |
| Intellectual disability | Present in essentially all reported individuals, though severity ranges from borderline to moderate/severe; some described as DD/ID rather than formal ID | Borderline/mild to moderate; severe developmental impairment in rare neonatal cases | Usually recognized in childhood | HP:0001249 Intellectual disability; HP:0001256 Mild intellectual disability; HP:0002342 Moderate intellectual disability | (blok2018denovomutations pages 1-2, blok2018denovomutations pages 4-5, blok2018denovomutations pages 7-11, nardi2021couldthemed13 pages 1-2) |
| Speech delay / language disorder | 13/13 (100%) in initial cohort | Often severe; expressive language commonly more impaired than receptive language | Infancy / toddler years | HP:0000750 Delayed speech and language development; HP:0002463 Language impairment | (blok2018denovomutations pages 1-2, blok2018denovomutations pages 4-5, blok2018denovomutations pages 7-11, nardi2021couldthemed13 pages 1-2) |
| Childhood apraxia of speech / severe speech production disorder | 3/13 (~23%) in initial cohort explicitly described with speech apraxia | Can be profound, including nonverbal status or limited verbal output | Early childhood | HP:0012469 Childhood apraxia of speech; HP:0001344 Expressive language delay | (blok2018denovomutations pages 2-4, blok2018denovomutations pages 4-5) |
| Motor developmental delay | 7/13 (~54%) in initial cohort; recurrent in later case reports | Mostly gross motor delay; variable | Infancy | HP:0001270 Motor delay; HP:0002194 Delayed gross motor development; HP:0010862 Delayed fine motor development | (blok2018denovomutations pages 2-4, blok2018denovomutations pages 6-7, nardi2021couldthemed13 pages 1-2, yang2025anovelframeshift pages 2-3) |
| Hypotonia | 3/13 (~23%) in initial cohort; described as common infantile feature in later summaries | Usually mild to moderate; often infantile | Infancy | HP:0001252 Muscular hypotonia | (blok2018denovomutations pages 6-7, nardi2021couldthemed13 pages 1-2, yang2025anovelframeshift pages 1-2) |
| Autism spectrum disorder | 5/13 (~38%) in initial cohort; recurrent across later reports and reviews | Variable behavioral severity | Childhood | HP:0000729 Autism | (blok2018denovomutations pages 2-4, blok2018denovomutations pages 1-2, nardi2021couldthemed13 pages 1-2, fazio2025geneticclinicaland pages 1-2) |
| Attention-deficit / hyperactivity disorder | 3/13 (~23%) in initial cohort | Variable | Childhood / school age | HP:0007018 Attention deficit hyperactivity disorder | (blok2018denovomutations pages 2-4, blok2018denovomutations pages 1-2, nardi2021couldthemed13 pages 1-2) |
| Dysmorphic facial features | Common; described as overlapping facial gestalt in multiple patients | Usually mild to moderate; variable expressivity | Congenital / infancy | HP:0001999 Facial dysmorphism; HP:0000316 Hypertelorism; HP:0000450 Broad nasal bridge; HP:0010800 Long philtrum / HP:0000343 Long philtrum as applicable | (blok2018denovomutations pages 5-6, nardi2021couldthemed13 pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5, yang2025anovelframeshift pages 2-3) |
| Eye / vision abnormalities (overall) | 8/13 (~62%) in initial cohort | Mild to severe; includes structural and functional abnormalities | Congenital or childhood | HP:0000505 Visual impairment; HP:0000618 Blindness / low vision umbrella if severe; HP:0000529 Progressive visual loss where relevant | (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11, tolmacheva2024expandingphenotypeof pages 1-2) |
| Optic nerve abnormalities | 3/13 in initial cohort; severe optic nerve/chiasm atrophy in neonatal case | Variable, can be severe | Congenital / childhood | HP:0001138 Optic atrophy; HP:0001098 Abnormality of the optic nerve | (blok2018denovomutations pages 6-7, tolmacheva2024expandingphenotypeof pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5) |
| Duane anomaly / strabismus spectrum | Duane anomaly 2/13 (~15%); strabismus also reported | Variable | Congenital / early childhood | HP:0009928 Duane anomaly; HP:0000486 Strabismus | (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11) |
| Astigmatism / nystagmus / retinal findings | Each uncommon but recurrent across cases | Variable | Childhood / congenital | HP:0000483 Astigmatism; HP:0000639 Nystagmus; HP:0000556 Retinal dystrophy | (blok2018denovomutations pages 6-7, tolmacheva2024expandingphenotypeof pages 2-5) |
| Congenital heart defects / mild cardiac anomalies | 2/13 (~15%) in initial cohort; more severe congenital heart disease in 2024 neonatal case | Usually mild in early cohort; rare severe neonatal presentation | Congenital | HP:0001627 Abnormality of the cardiovascular system; HP:0001631 Aortic root dilatation; HP:0001671 Atrial septal defect; HP:0001629 Ventricular septal defect; HP:0001680 Coarctation of aorta / isthmus hypoplasia as applicable | (blok2018denovomutations pages 6-7, tolmacheva2024expandingphenotypeof pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5) |
| Epilepsy / seizures | Rare in initial cohort (1/13, ~8%); later reports expanded spectrum to epileptic encephalopathy | Can be severe and drug-resistant when present | Childhood or infancy depending on case | HP:0001250 Seizure; HP:0002123 Generalized myoclonic seizure; HP:0012468 Epileptic encephalopathy | (blok2018denovomutations pages 6-7, rivera2024med13genemutation pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5) |
| Brain MRI abnormalities | Uncommon in original cohort but increasingly recognized in later reports | Variable; from mild frontal atrophy to severe callosal/brainstem/chiasmal abnormalities | Infant / childhood | HP:0001273 Abnormality of the corpus callosum; HP:0002060 Abnormality of the cerebral white matter; HP:0002283 Ventriculomegaly; HP:0007364 Hydrocephalus | (blok2018denovomutations pages 6-7, tolmacheva2024expandingphenotypeof pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5, fazio2025geneticclinicaland pages 1-2) |
| Corpus callosum abnormalities | Reported in severe recent cases/reviews | Moderate to severe | Congenital / infancy | HP:0001273 Abnormality of the corpus callosum; HP:0002079 Hypoplasia of the corpus callosum | (tolmacheva2024expandingphenotypeof pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5, fazio2025geneticclinicaland pages 1-2) |
| Microcephaly / growth restriction / short stature | Reported in subset; severe neonatal case had growth restriction; later family report notes restricted growth | Variable | Prenatal or postnatal | HP:0000252 Microcephaly; HP:0001511 Intrauterine growth restriction; HP:0004322 Short stature | (tolmacheva2024expandingphenotypeof pages 1-2, yang2025anovelframeshift pages 1-2, yang2025anovelframeshift pages 2-3) |
| Chronic constipation / obstipation / megacolon | Obstipation in 4/13 (~31%) in initial cohort; congenital megacolon reported as novel complication in family report | Usually chronic; occasionally severe | Infancy / childhood | HP:0002019 Constipation; HP:0002240 Chronic constipation; HP:0012707 Megacolon | (blok2018denovomutations pages 6-7, yang2025anovelframeshift pages 1-2, yang2025anovelframeshift pages 2-3) |
| Hearing loss | 2/13 (~15%) conductive hearing loss in initial cohort; hearing/vision problems noted in later reports | Mild to moderate | Childhood | HP:0000405 Conductive hearing impairment; HP:0000365 Hearing impairment | (blok2018denovomutations pages 5-6, tolmacheva2024expandingphenotypeof pages 1-2) |
| Orthopedic / skeletal anomalies | Recurrent but variable; scoliosis, pes cavus, brachydactyly, hip dysplasia, valgus-pronated feet reported | Mild to moderate | Childhood / congenital | HP:0002650 Scoliosis; HP:0001761 Pes cavus; HP:0001156 Brachydactyly; HP:0001385 Hip dysplasia | (blok2018denovomutations pages 5-6, nardi2021couldthemed13 pages 1-2) |
| Severe multisystem neonatal presentation | Very rare; single recent neonate with hydrocephalic changes, optic/chiasm atrophy, bowel atresia, cardiac disease, multiple organ failure, neonatal death | Severe / potentially lethal | Prenatal to neonatal | HP:0001627 Abnormality of the cardiovascular system; HP:0001138 Optic atrophy; HP:0002079 Hypoplasia of the corpus callosum; HP:0002586 Ileal atresia; HP:0003819 Neonatal death | (tolmacheva2024expandingphenotypeof pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5) |


*Table: This table summarizes the core and variable clinical features reported for MED13 syndrome, including approximate frequencies, severity patterns, onset, suggested HPO mappings, and supporting citations. It is useful for disease knowledge base curation and phenotype annotation.*

### Core Phenotypes

**Developmental Delay and Intellectual Disability (100% penetrance)**

*Phenotype Type:* Neurodevelopmental impairment; clinical sign and behavioral manifestation

*Characteristics:*
- **Severity:** Ranges from borderline/mild to moderate intellectual disability (ID); some patients assessed by formal testing showed IQ scores from 35-50 (moderate ID) to 85 (lower range of normal), though most fall in the mild ID range (blok2018denovomutations pages 1-2, blok2018denovomutations pages 4-5)
- **Age of Onset:** Apparent in infancy; global developmental delay typically recognized within the first year of life
- **Progression:** Generally stable once developmental trajectory is established, though speech may show some improvement with intensive therapy
- **Frequency:** Universal (100%) among all reported cases (blok2018denovomutations pages 1-2, blok2018denovomutations pages 7-11)

*Quality of Life Impact:* Significant impact on educational attainment, independence, and adaptive functioning. Most individuals require ongoing educational support and may need assistance with activities of daily living in adulthood.

*HPO Terms:* HP:0001263 (Global developmental delay); HP:0001249 (Intellectual disability); HP:0001256 (Mild intellectual disability); HP:0002342 (Moderate intellectual disability)

**Speech and Language Disorders (100% penetrance)**

*Phenotype Type:* Neurodevelopmental symptom affecting communication

*Characteristics:*
- **Severity:** Variable from delayed language development to severe speech/language disorder; notably, "speech production was significantly more impaired than language comprehension" in the majority of patients (blok2018denovomutations pages 1-2, blok2018denovomutations pages 4-5)
- **Age of Onset:** Delays apparent from toddler years onward
- **Specific Subtypes:** Three patients (approximately 23%) presented with childhood apraxia of speech, characterized by "difficulties accurately programming the motor sequences required to produce fluent speech" (blok2018denovomutations pages 1-2, blok2018denovomutations pages 4-5). Patient M had "severe speech/language disorder" with "expressive speech severely affected, with signs of speech apraxia. At the age of 8 years she only used single words and very short sentences" (blok2018denovomutations pages 4-5). Patient K showed "regression at the age of 13 months and has since remained non-verbal" (blok2018denovomutations pages 4-5).
- **Progression:** Speech delays persist, though some improvement with therapy
- **Frequency:** Universal (100%) (blok2018denovomutations pages 1-2, blok2018denovomutations pages 4-5)

*Quality of Life Impact:* Severe speech impairments profoundly affect social interaction, educational achievement, and frustration levels in affected children.

*HPO Terms:* HP:0000750 (Delayed speech and language development); HP:0002463 (Language impairment); HP:0012469 (Childhood apraxia of speech); HP:0001344 (Abnormal expressive language)

### Common Variable Phenotypes

**Autism Spectrum Disorder (38-55%)**

*Phenotype Type:* Behavioral/neurodevelopmental disorder

*Characteristics:*
- **Severity:** Variable from mild autistic features to formal ASD diagnosis
- **Age of Onset:** Typically recognized in early childhood
- **Frequency:** Five of 13 patients (38%) in the initial cohort; later reviews suggest up to 55% (blok2018denovomutations pages 1-2, rivera2024med13genemutation pages 1-2, nardi2021couldthemed13 pages 1-2)

*HPO Terms:* HP:0000729 (Autism)

**Attention Deficit Hyperactivity Disorder (23%)**

*Phenotype Type:* Behavioral disorder

*Frequency:* Three of 13 patients (23%) in initial cohort (blok2018denovomutations pages 1-2, nardi2021couldthemed13 pages 1-2)

*HPO Terms:* HP:0007018 (Attention deficit hyperactivity disorder)

**Eye and Vision Abnormalities (62%)**

*Phenotype Type:* Structural and functional ophthalmic abnormalities

*Characteristics:*
- **Specific Features:** Optic nerve abnormalities (pale optic nerves, optic atrophy), Duane anomaly (congenital strabismus with horizontal ophthalmoplegia), astigmatism, nystagmus, retinal abnormalities (blok2018denovomutations pages 1-2, blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11)
- **Severity:** Variable from mild refractive errors to severe optic atrophy with visual impairment
- **Notable Pattern:** Two patients with missense mutations clustering in the C-terminal domain (p.Gln2060Lys and p.Ala2064Val) both presented with Duane anomaly, suggesting potential genotype-phenotype correlation (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11)
- **Age of Onset:** Typically congenital or recognized in early childhood
- **Frequency:** Eight of 13 patients (62%) had eye or vision abnormalities (blok2018denovomutations pages 6-7)

*HPO Terms:* HP:0001098 (Abnormality of the optic nerve); HP:0001138 (Optic atrophy); HP:0009928 (Duane anomaly); HP:0000486 (Strabismus); HP:0000483 (Astigmatism); HP:0000639 (Nystagmus)

**Dysmorphic Facial Features**

*Phenotype Type:* Physical manifestation; craniofacial anomaly

*Characteristics:*
- **Specific Features:** As described by Blok et al., "Overlapping facial characteristics were reported, including widely spaced eyes with narrow palpebral fissures and peri-orbital fullness, a broad and high nasal bridge, full nasal tip, synophrys, a flat philtrum and a wide mouth with thin upper lip" (blok2018denovomutations pages 1-2, blok2018denovomutations pages 6-7)
- **Severity:** Generally mild; may contribute to clinical suspicion but not pathognomonic
- **Age of Onset:** Congenital
- **Frequency:** Common but variable; noted across multiple independent reports (blok2018denovomutations pages 1-2, nardi2021couldthemed13 pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5, yang2025anovelframeshift pages 2-3)

*Note:* One patient initially received a clinical diagnosis of Kabuki syndrome based on facial features before MED13 variant was identified, highlighting phenotypic overlap with other syndromes (nardi2021couldthemed13 pages 1-2).

*HPO Terms:* HP:0001999 (Abnormality of the face); HP:0000316 (Hypertelorism); HP:0000450 (Broad nasal bridge); HP:0000343 (Long philtrum); HP:0000154 (Wide mouth)

**Congenital Heart Defects (15-30%)**

*Phenotype Type:* Structural cardiac anomaly

*Characteristics:*
- **Specific Features:** Mild defects include dilated aortic root and pulmonary artery, subaortic stenosis (blok2018denovomutations pages 6-7). Severe neonatal case presented with "isthmus hypoplasia, ventricular septal defect, small atrial septal defect, right heart hypertrophy, tricuspid insufficiency, and pulmonary hypertension" (tolmacheva2024expandingphenotypeof pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5)
- **Severity:** Usually mild in typical cases; severe in rare neonatal presentations
- **Age of Onset:** Congenital
- **Frequency:** Two of 13 patients (15%) in initial cohort; higher in expanded case series including severe presentations (tolmacheva2024expandingphenotypeof pages 1-2, blok2018denovomutations pages 6-7)

*HPO Terms:* HP:0001627 (Abnormal heart morphology); HP:0001680 (Coarctation of the aorta); HP:0001629 (Ventricular septal defect); HP:0001631 (Atrial septal defect)

**Hypotonia and Motor Delays (23-54%)**

*Phenotype Type:* Neuromuscular symptom; motor developmental delay

*Characteristics:*
- **Hypotonia:** Reported in three of 13 patients (23%), typically as infantile hypotonia (blok2018denovomutations pages 6-7)
- **Motor Delays:** Seven of 13 patients (54%) showed motor developmental delays, mostly affecting gross motor skills (blok2018denovomutations pages 2-4, blok2018denovomutations pages 6-7)
- **Age of Onset:** Hypotonia apparent in infancy; motor delays recognized in first years
- **Progression:** Hypotonia may improve with age; motor delays persist but some improvement with therapy

*HPO Terms:* HP:0001252 (Muscular hypotonia); HP:0001270 (Motor delay); HP:0002194 (Delayed gross motor development)

### Less Common Phenotypes

**Epilepsy and Seizures (8-15%)**

*Phenotype Type:* Neurological disorder; laboratory/clinical abnormality (abnormal EEG)

*Characteristics:*
- **Specific Presentations:** One patient in original cohort developed "severe drug-resistant myoclonic-atonic epilepsy at 4 years of age with generalized clonic, myoclonic, atonic, tonic and atypical absence seizures" (blok2018denovomutations pages 6-7). More recent reports include epileptic encephalopathy with infantile spasms (rivera2024med13genemutation pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5)
- **Severity:** Can be severe and treatment-resistant when present
- **Age of Onset:** Variable, from infancy to childhood
- **Frequency:** Rare; one of 13 in original cohort; several additional cases in later reports

*HPO Terms:* HP:0001250 (Seizure); HP:0012469 (Epileptic encephalopathy); HP:0002123 (Generalized myoclonic seizures)

**Brain MRI Abnormalities**

*Phenotype Type:* Structural brain abnormality; imaging finding

*Characteristics:*
- **Specific Features:** Mild frontal atrophy, corpus callosum abnormalities (hypoplasia, agenesis), ventriculomegaly, hydrocephalic changes, optic chiasm atrophy, brainstem atrophy (tolmacheva2024expandingphenotypeof pages 1-2, blok2018denovomutations pages 6-7, fazio2025geneticclinicaland pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5)
- **Severity:** Variable from mild to severe
- **Age of Onset:** Congenital/developmental
- **Frequency:** Not systematically reported in early cohort; increasingly recognized in recent case reports

*HPO Terms:* HP:0001273 (Abnormality of the corpus callosum); HP:0002079 (Hypoplasia of the corpus callosum); HP:0002119 (Ventriculomegaly); HP:0007364 (Lissencephaly)

**Chronic Constipation and GI Manifestations (31%)**

*Phenotype Type:* Gastrointestinal symptom

*Characteristics:*
- **Specific Features:** Chronic obstipation reported in four of 13 patients (31%) in original cohort (blok2018denovomutations pages 6-7). Novel complication of congenital megacolon described in Chinese family case (yang2025anovelframeshift pages 1-2, yang2025anovelframeshift pages 2-3)
- **Severity:** Variable; can be severe requiring surgical intervention (megacolon case)

*HPO Terms:* HP:0002019 (Constipation); HP:0012707 (Megacolon)

**Severe Neonatal/Multisystem Presentation (Very Rare)**

*Phenotype Type:* Severe multi-organ involvement

One infant with a de novo p.Pro835Ser variant "presented with congenital heart anomalies, dysmorphic features, hydrocephalic changes, hypoplastic corpus callosum, bilateral optic nerve atrophy, optic chiasm atrophy, brain stem atrophy, and overall a more severe condition compared to previously described patients" and "deceased at 76 days of age due to multiple organ failure" (tolmacheva2024expandingphenotypeof pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5). This case highlights the potential for severe presentations.

---

## 4. Genetic/Molecular Information

| Variant / protein change | cDNA change | Variant type | Source / case context | Protein region / domain affected | Clustering pattern | Reported / inferred functional consequence | Pathogenicity classification / evidence level | CADD / in silico data | Conservation / population data | Key notes / citations |
|---|---|---|---|---|---|---|---|---|---|---|
| p.Pro42Leufs*6 | c.125del | Frameshift | Blok 2018 patient A | N-terminus, upstream of annotated Med13_N domain | Non-clustered truncating variant | Predicted premature termination; likely loss of normal function | Likely pathogenic / pathogenic by case-series evidence | CADD 31.0 | Absent from gnomAD/TOPMed in cohort analysis | Associated with mild ID and speech apraxia in original cohort (blok2018denovomutations pages 1-2, blok2018denovomutations pages 4-5, blok2018denovomutations pages 7-11) |
| p.Leu131* | c.392T>G | Nonsense | Blok 2018 patients B/C | N-terminal region, upstream of Med13_N domain | Recurrent truncating variant | Predicted truncation; transcript detected on cDNA, but no truncated protein detected in analogous nonsense case, supporting abnormal protein consequence rather than simple transcript loss | Pathogenic by segregation/case evidence | CADD 37.0 | Absent from gnomAD/TOPMed in cohort analysis | One inherited instance from affected mother to affected child shows AD transmission with variable expressivity (blok2018denovomutations pages 1-2, blok2018denovomutations pages 4-5, blok2018denovomutations pages 7-11) |
| p.Thr326Ile | c.977C>T | Missense | Blok 2018 patient D | Conserved N-terminal phosphodegron within/near Med13_N domain | N-terminal hotspot | Predicted to impair FBW7 phosphodegron recognition and alter MED13 ubiquitination/degradation, potentially increasing abnormal MED13 stability | Likely pathogenic by clustering/mechanistic evidence | CADD 25.0 | Site highly conserved; codon under strong selection; absent from gnomAD/TOPMed | One of four variants affecting Thr326/Pro327 hotspot (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11) |
| p.Thr326del | c.975_977delTAC | In-frame deletion | Blok 2018 patient E | Conserved N-terminal phosphodegron within/near Med13_N domain | N-terminal hotspot | Predicted disruption of phosphodegron and impaired SCF-FBW7-mediated degradation | Likely pathogenic by hotspot/mechanistic evidence | CADD 20.5 | Highly conserved motif; absent from gnomAD/TOPMed | Only in-frame deletion in original cohort; still localized to same hotspot as missense variants (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11) |
| p.Pro327Ser | c.979C>T | Missense | Blok 2018 patient F; Nardi 2021; recurrent in later reports | Conserved N-terminal phosphodegron within/near Med13_N domain | N-terminal hotspot, recurrent | Predicted to reduce phosphodegron-dependent FBW7 binding and MED13 turnover | Likely pathogenic; recurrent across unrelated patients | CADD 23.4 | Highly conserved residue; absent from gnomAD/TOPMed | Recurrent variant with variable expressivity, from neurodevelopmental phenotype to Kabuki-like presentation (nardi2021couldthemed13 pages 1-2, blok2018denovomutations pages 4-5, blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11) |
| p.Pro327Gln | c.980C>A | Missense | Blok 2018 patient G | Conserved N-terminal phosphodegron within/near Med13_N domain | N-terminal hotspot | Same predicted mechanism as other phosphodegron variants: altered phosphorylation/FBW7 interaction and defective degradation | Likely pathogenic by hotspot/mechanistic evidence | CADD 25.2 | Highly conserved; absent from gnomAD/TOPMed | Supports hotspot-specific mechanism at adjacent residues Thr326/Pro327 (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11) |
| p.Pro540Thr | c.1618C>A | Missense | Blok 2018 patient H | Internal conserved linear motif outside named Pfam domains | Non-hotspot missense | Predicted formation of novel Casein Kinase 1 phosphorylation motif and altered protein interactions | VUS-to-likely pathogenic range by case/mechanistic evidence | CADD 26.3 | Highly conserved motif; codon under strong selection; absent from gnomAD/TOPMed | Distinct mechanism proposed versus phosphodegron variants (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11) |
| p.Leu582* | c.1745T>A | Nonsense | Blok 2018 patient I | Internal region between N- and C-terminal domains | Non-clustered truncating variant | Predicted loss of downstream functional regions and loss of normal function | Pathogenic by case evidence | CADD 40.0 | Absent from gnomAD/TOPMed | Truncating variants distributed outside missense hotspots (blok2018denovomutations pages 4-5, blok2018denovomutations pages 6-7) |
| p.Arg1400* | c.4198C>T | Nonsense | Blok 2018 patient J | Mid-protein region, upstream of Med13_C domain | Non-clustered truncating variant | cDNA present, but no truncated protein detected on western blot; supports abnormal protein consequence / defective stable product | Pathogenic by functional follow-up | CADD 41.0 | Absent from gnomAD/TOPMed | Functional transcript/protein analyses were performed for this allele (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11) |
| p.Thr1496Metfs*11 | c.4487delC | Frameshift | Blok 2018 patient K | Mid/C-terminal transition, upstream of Med13_C domain | Non-clustered truncating variant | Predicted premature truncation with loss of C-terminal region | Pathogenic by case evidence | CADD 35.0 | Absent from gnomAD/TOPMed | Associated with severe speech disorder/regression in cohort (blok2018denovomutations pages 4-5, blok2018denovomutations pages 6-7) |
| p.Gln2060Lys | c.6178C>A | Missense | Blok 2018 patient L | C-terminal Med13_C domain | C-terminal hotspot | Predicted disturbance of conserved surface-exposed motif / interaction interface | Likely pathogenic by clustering and conservation | CADD 24.1 | Highly conserved; absent from gnomAD/TOPMed | One of two adjacent C-terminal hotspot variants in patients with eye findings including Duane anomaly (blok2018denovomutations pages 4-5, blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11) |
| p.Ala2064Val | c.6191C>T | Missense | Blok 2018 patient M | C-terminal Med13_C domain | C-terminal hotspot | Predicted structural alteration with increased hydrophobic collapse and reduced linear interaction potential on conserved surface motif | Likely pathogenic by structural modeling | CADD 25.7 | Highly conserved; absent from gnomAD/TOPMed | Supports second missense hotspot in C-terminal region (blok2018denovomutations pages 4-5, blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11) |
| p.Pro835Ser | reported as de novo missense variant in 2024 case report | Missense | Tolmacheva 2024 severe neonatal case | Mid-protein region, outside named hotspot in available summary | Non-hotspot missense | Not mapped to a known functional center in UniProt summary, but predicted damaging; may underlie severe multisystem/neonatal phenotype | Likely pathogenic per ACMG in report | CADD 26.1; PolyPhen-2 0.996; SIFT 0.0 | Position conserved across vertebrates per UCSC alignment; de novo; absent/rare in population databases implied by diagnostic filtering | Expanded phenotype to severe neonatal presentation and death (tolmacheva2024expandingphenotypeof pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5) |
| p.Arg1882Serfs*9 | c.5641delinsTC | Frameshift | Yang 2025 Chinese family | Distal C-terminal half, upstream of Med13_C tail end | Non-clustered truncating variant | Predicted truncation with autosomal dominant disease mechanism | Pathogenic/likely pathogenic by familial segregation and ACMG-based interpretation | Not numerically reported in excerpt | Rare after filtering at MAF ≤0.001; segregated with affected mother and proband | First reported Chinese family; supports inherited AD disease and expands variant spectrum (yang2025anovelframeshift pages 1-2, yang2025anovelframeshift pages 2-3) |
| Overall MED13 variant spectrum | Multiple | Missense, nonsense, frameshift, in-frame deletion | Blok 2018 + recent reports | Two annotated Pfam domains: Med13_N (aa 11-383) and Med13_C (aa 1640-2163), plus conserved internal motifs | Strong clustering of non-truncating variants in two regions: N-terminal phosphodegron hotspot (Thr326/Pro327) and C-terminal hotspot around Gln2060/Ala2064 | Truncating variants support loss-of-function/haploinsufficiency-like mechanism; hotspot missense variants suggest altered degradation or altered protein interaction surfaces | Disease-gene relationship supported by significant enrichment of de novo variants in DD/ID cohorts (p=0.00371) | CADD range for reported 2018 variants: 20.5-41.0 | All 12 unique Blok 2018 variants absent from gnomAD and TOPMed; missense hotspot residues highly conserved and under codon selection | Best current model is mixed mechanism: truncating alleles causing loss of normal function and clustered missense alleles perturbing regulated MED13 turnover or conserved interaction motifs (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11, yang2025anovelframeshift pages 2-3) |


*Table: This table summarizes the reported genetic and molecular features of MED13 syndrome, including representative variants, domains, clustering, functional interpretations, and available in silico evidence. It is useful for disease knowledge base curation and for distinguishing truncating versus hotspot missense mechanisms.*

### Causal Gene

**MED13 (Mediator Complex Subunit 13)**

- **Gene Symbol:** MED13
- **OMIM Gene ID:** #603808
- **Chromosomal Location:** 17q23.2 (yang2025anovelframeshift pages 1-2, yang2025anovelframeshift pages 2-3)
- **Transcript:** NM_005121.3 (reference transcript used in clinical reporting)
- **Protein:** NP_005112.2; 2,174 amino acids; predicted molecular weight 239.3 kDa (blok2018denovomutations pages 1-2, poss2013themediatorcomplex pages 2-3)
- **HGNC ID:** HGNC:2372

### Pathogenic Variants

**Variant Types and Classification:**

The MED13 gene harbors multiple types of pathogenic variants. As summarized by Blok et al. (2018), the cohort included "six affected individuals had mutations that are predicted to truncate the MED13 protein, six had missense mutations, and one had an in-frame-deletion of one amino acid" (blok2018denovomutations pages 1-2).

**Truncating Variants (Loss-of-Function):**
- **Nonsense mutations:** p.Leu131*, p.Leu582*, p.Arg1400* (blok2018denovomutations pages 1-2, blok2018denovomutations pages 4-5)
- **Frameshift variants:** p.Pro42Leufs*6, p.Thr1496Metfs*11, p.Arg1882Serfs*9 (blok2018denovomutations pages 1-2, yang2025anovelframeshift pages 2-3)
- **Mechanism:** Truncating variants likely lead to haploinsufficiency. Functional studies on the p.Arg1400* variant demonstrated that "while full-length MED13 protein was present in the patient (and in the controls), no truncated MED13 protein product could be detected" (blok2018denovomutations pages 1-2, blok2018denovomutations pages 7-11), supporting nonsense-mediated decay or rapid degradation of truncated protein. However, "no differences in MED13 transcript levels were detectable between the affected patient and the unaffected parents or controls" (blok2018denovomutations pages 1-2, blok2018denovomutations pages 7-11), suggesting the remaining transcript from the normal allele may partially compensate at the mRNA level, but haploinsufficiency exists at the protein level.

**Missense Variants with Clustering:**

A striking feature is the clustering of non-truncating variants in two specific protein regions (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11):

1. **N-terminal Phosphodegron Hotspot (Thr326/Pro327):**
   - Variants: p.Thr326Ile, p.Thr326del, p.Pro327Ser, p.Pro327Gln (blok2018denovomutations pages 1-2, nardi2021couldthemed13 pages 1-2, blok2018denovomutations pages 6-7)
   - **Functional Consequence:** These residues are part of a conserved phosphodegron recognized by the SCF-Fbw7 ubiquitin ligase for MED13 degradation. As Blok et al. explain, "it has already been shown that a specific amino acid substitution at position 326 in MED13 (p.Thr326Ala) leads to impaired binding of Fbw7 to the phosphodegron of MED13/MED13L, thus preventing MED13/MED13L ubiquitination and degradation" (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11). Molecular modeling showed that "all four variants (p.Thr326Ile, p.Thr326del, p.Pro327Ser, p.Pro327Gln) are predicted to alter the phosphorylation and Fbw7 interaction with drastic decreases in binding energy to Fbw7" (blok2018denovomutations pages 7-11). This suggests a **dominant-negative or gain-of-dysfunction mechanism** wherein the variant protein is stabilized and accumulates, potentially disrupting normal Mediator complex dynamics.

2. **C-terminal Hotspot (Gln2060/Ala2064):**
   - Variants: p.Gln2060Lys, p.Ala2064Val (blok2018denovomutations pages 1-2, blok2018denovomutations pages 6-7)
   - **Functional Consequence:** These C-terminal variants affect conserved surface-exposed motifs. The p.Ala2064Val change is "predicted to be structure-altering through increasing hydrophobic collapse, secondary structure formation, and increasing aliphatic index of a surface exposed linear motif. This results in a decrease of the regions linear interacting peptide potential" (blok2018denovomutations pages 7-11), suggesting altered protein-protein interactions within the Mediator complex or with transcription factors.

**Variant Classification (ACMG/AMP):**
All reported pathogenic variants are classified as pathogenic or likely pathogenic based on:
- Absence from population databases (gnomAD, TOPMED)
- High conservation of affected residues
- High CADD scores (20.5-41.0) (blok2018denovomutations pages 1-2, blok2018denovomutations pages 6-7)
- Segregation with disease phenotype
- Functional data (for select variants)
- Significant enrichment of de novo MED13 variants in DD/ID cohorts (p=0.00371) (blok2018denovomutations pages 7-11)

**Allele Frequency:**
All pathogenic variants identified to date are absent or extremely rare in population databases (gnomAD allele frequency effectively 0 for disease-causing variants) (blok2018denovomutations pages 1-2, blok2018denovomutations pages 7-11), consistent with the severe reproductive fitness impact and predominantly de novo occurrence.

**Somatic vs. Germline:**
All reported variants are germline. One case of suspected paternal germline mosaicism has been reported for a MED13L variant, and a similar mechanism could theoretically occur for MED13, though not yet documented (fazio2025geneticclinicaland pages 1-2).

**Functional Consequences:**
- **Loss-of-function variants:** Haploinsufficiency mechanism, reducing functional MED13 protein levels
- **Phosphodegron missense variants:** Impaired protein degradation leading to accumulation of dysfunctional MED13, potentially causing dominant-negative effects on Mediator complex function
- **Other missense variants:** Altered protein interactions or structural changes affecting MED13 function within the Mediator complex

### Modifier Genes

**MED13L:**  
The paralog MED13L (chromosome 12q24.21) can partially compensate for MED13 loss. Studies show MED13 and MED13L are mutually exclusive within the CDK8-kinase module (miao2018mediatorcomplexcomponent pages 1-2, fazio2025geneticclinicaland pages 2-4). Mouse studies demonstrated that "MED13L partially compensates for loss of MED13 function in preimplantation knockout embryos, but postimplantation development is not rescued by MED13L" (miao2018mediatorcomplexcomponent pages 1-2), suggesting tissue- and stage-specific compensation.

### Epigenetic Information

While specific epigenetic changes in MED13 Syndrome patients have not been extensively characterized, the Mediator complex itself regulates epigenetic modifications. The MED13-containing kinase module can phosphorylate chromatin regulators and is involved in coordinating transcriptional responses to epigenetic signals (poss2013themediatorcomplex pages 2-3).

### Chromosomal Abnormalities

No large-scale chromosomal abnormalities (aneuploidy, translocations, inversions) involving MED13 have been reported as causes of the syndrome. The disorder results from intragenic sequence variants.

---

## 5. Environmental Information

### Environmental Factors

No specific environmental factors (toxins, radiation, pollution, occupational exposures) have been identified as contributing to MED13 Syndrome, consistent with its genetic etiology as a predominantly de novo Mendelian disorder.

### Lifestyle Factors

Not applicable to disease causation.

### Infectious Agents

Not applicable.

---

## 6. Mechanism / Pathophysiology

### Overview of Molecular Mechanisms

MED13 Syndrome pathophysiology centers on disrupted transcriptional regulation during neurodevelopment due to impaired Mediator complex function.

### Molecular Pathways

**Mediator Complex and RNA Polymerase II Transcription:**

The Mediator complex is "a multi-protein complex that is required for Polymerase II transcription initiation" and "required for expression of most, if not all, pol II transcripts" (blok2018denovomutations pages 1-2, harper2018thecomplexstructure pages 1-2). The human Mediator contains 26 subunits organized into head, middle, and tail modules, with the reversibly associating CDK8-kinase module (consisting of MED13, MED12, CDK8, and cyclin C) (harper2018thecomplexstructure pages 1-2, poss2013themediatorcomplex pages 2-3).

As described by Poss et al. (2013), "the CDK8-module can reversibly bind Mediator...Binding of the CDK8-module to the Mediator core complex has been reported to prevent the association of the Mediator with the Pol II preinitiation complex, thus preventing transcription initiation and/or re-initiation" (poss2013themediatorcomplex pages 2-3). MED13 specifically "serves as the molecular bridge between the core Mediator complex and the kinase submodule" (blok2018denovomutations pages 7-11).

**MED13-Dependent Transcriptional Regulation:**

MED13 regulates transcription through multiple mechanisms:
1. **Kinase Module Association:** MED13 facilitates reversible binding of the CDK8-module to core Mediator, modulating transcriptional activation versus repression (blok2018denovomutations pages 1-2, poss2013themediatorcomplex pages 2-3)
2. **Protein Turnover Regulation:** The N-terminal phosphodegron of MED13 regulates its degradation via SCF-Fbw7, controlling CDK8-module availability. "Protein turnover of MED13 (or MED13L) may be critical in modulating the pools of Mediator-CDK8 kinase complex in cells" (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11)
3. **Transcription Factor Phosphorylation:** The CDK8 kinase can phosphorylate transcription factors and chromatin regulators, with MED13 helping to coordinate these activities (poss2013themediatorcomplex pages 2-3)

### Cellular Processes

**Neuronal Development and Migration:**

Mouse studies using in utero electroporation demonstrate that "silencing Med13 in cortical neurons impaired its radial migration and contralateral projection as well as dendritic complexity" (li2026med13isinvolved pages 1-2). The authors found that "Med13 regulates cortical neuronal radial migration and callosal projection at least in part through PlxnA4," a downstream target involved in axon guidance (li2026med13isinvolved pages 1-2).

**Zygotic Genome Activation:**

MED13 plays a critical role in early embryonic transcriptional activation. Miao et al. (2018) demonstrated that "MED13 is essential for ZGA [zygotic genome activation] in the mouse, in part by regulating expression of the embryo-specific chromatin remodeling complex, esBAF" (miao2018mediatorcomplexcomponent pages 1-2). Knockout of Med13 in mouse embryos resulted in embryonic lethality as early as E8.5 (li2026med13isinvolved pages 1-2, miao2018mediatorcomplexcomponent pages 1-2).

**Cortical Neurogenesis:**

Recent work by Li et al. (2025) on MED13L (the paralog) provides insights relevant to MED13 function. They found that MED13L "orchestrates cortical neurogenesis by priming the transcriptional activation of key developmental genes, including Neurod2, Sox5, Auts2, and Nfib" through binding to the core mediator complex and facilitating "the complex's association with RNA Pol II" (blok2018denovomutations pages 1-2). Given the structural and functional similarities between MED13 and MED13L, analogous mechanisms likely apply to MED13 in neuronal differentiation.

### Protein Dysfunction

**Haploinsufficiency (Truncating Variants):**

Truncating MED13 variants result in reduced functional protein. Western blot analysis of a nonsense variant showed that while transcript was present, "no truncated MED13 protein product could be detected" (blok2018denovomutations pages 7-11), indicating protein instability or degradation.

**Altered Protein Stability and Turnover (Phosphodegron Variants):**

Missense variants affecting Thr326/Pro327 prevent normal SCF-Fbw7-mediated ubiquitination and degradation, potentially leading to abnormal accumulation of MED13 protein. This could disrupt the normal dynamic regulation of Mediator-CDK8 module association (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11).

**Altered Protein-Protein Interactions (C-terminal Variants):**

C-terminal missense variants are predicted to alter surface-exposed interaction motifs, potentially disrupting MED13's interactions with other Mediator subunits or transcription factors (blok2018denovomutations pages 7-11).

### Metabolic Changes

While not a primary metabolic disorder, MED13 does regulate metabolic gene expression. Studies in cardiac-specific MED13 overexpressing mice showed that "cardiac expression of MED13 decreases metabolic gene expression in the heart but enhances them in WAT [white adipose tissue]" and affects systemic energy homeostasis (baskin2014med13‐dependentsignalingfrom pages 1-2). Whether metabolic dysregulation contributes to MED13 Syndrome phenotypes remains unclear.

### Immune System Involvement

No primary immune dysfunction has been reported. One patient had isolated IgA deficiency (nardi2021couldthemed13 pages 1-2), but this is not a consistent feature.

### Tissue Damage Mechanisms

**Neurodevelopmental Disruption:**

The primary tissue damage mechanism is impaired neurodevelopment rather than progressive neurodegeneration. Brain MRI findings in severe cases show structural malformations (corpus callosum hypoplasia, optic nerve/chiasm atrophy, ventriculomegaly) (tolmacheva2024expandingphenotypeof pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5), indicating developmental abnormalities rather than acquired injury.

### Biochemical Abnormalities

**Transcriptional Dysregulation:**

The core biochemical abnormality is widespread transcriptional dysregulation due to impaired Mediator function. Differential protein analysis of MED13-deficient human neuroblastoma cells "revealed a large number of dysregulated proteins" involved in neurodevelopmental pathways (li2026med13isinvolved pages 1-2).

### Molecular Profiling (Where Available)

**Transcriptomics:**  
Single-cell transcriptomics and immunofluorescence of Med13l knockout mouse embryos "reveal severe cortical neurogenesis deficits...driven by impaired neural progenitor differentiation" (blok2018denovomutations pages 1-2). Integrative multi-omics analyses revealed dysregulation of developmental genes including Neurod2, Sox5, Auts2, and Nfib (blok2018denovomutations pages 1-2).

**Proteomics:**  
Differential protein analysis of MED13-deleted SH-SY5Y cells identified dysregulated proteins including PLXNA4, convergent towards neurodevelopmental pathways (li2026med13isinvolved pages 1-2).

### Advanced Technologies

**Single-Cell Analysis:**  
Med13l studies used single-cell RNA-seq to identify cell-type-specific deficits in cortical neurogenesis (blok2018denovomutations pages 1-2).

**Functional Genomics:**  
CRISPR-based knockdown and overexpression studies in mouse cortical neurons demonstrated Med13's roles in migration, dendritic development, and callosal projections (li2026med13isinvolved pages 1-2).

### Suggested Ontology Terms

- **GO Biological Process:**  
  - GO:0006357 (regulation of transcription by RNA polymerase II)
  - GO:0045944 (positive regulation of transcription by RNA polymerase II)
  - GO:0021987 (cerebral cortex development)
  - GO:0021772 (olfactory bulb development)
  - GO:0022008 (neurogenesis)
  - GO:0051301 (cell division)

- **GO Cellular Component:**  
  - GO:0016592 (mediator complex)
  - GO:0005634 (nucleus)

- **Cell Types (Cell Ontology):**  
  - CL:0000540 (neuron)
  - CL:0000598 (pyramidal neuron)
  - CL:0000127 (astrocyte)
  - CL:0011005 (GABAergic neuron)
  - CL:0000125 (glial cell)

---

## 7. Anatomical Structures Affected

### Organ Level

**Primary Organs:**
- **Central Nervous System (Brain):** The brain is the primary organ affected, with widespread impact on cortical development, corpus callosum formation, and optic nerve structures (tolmacheva2024expandingphenotypeof pages 1-2, blok2018denovomutations pages 6-7, fazio2025geneticclinicaland pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5)

**Secondary Organs:**
- **Heart:** Mild to moderate congenital heart defects in 15-30% of cases (tolmacheva2024expandingphenotypeof pages 1-2, blok2018denovomutations pages 6-7)
- **Eyes:** Optic nerves, retina affected in majority of patients (62%) (blok2018denovomutations pages 6-7)
- **Gastrointestinal system:** Chronic constipation, rare megacolon (blok2018denovomutations pages 6-7, yang2025anovelframeshift pages 2-3)

**Body Systems:**
- Nervous system (primary)
- Cardiovascular system (secondary)
- Visual system (secondary)
- Musculoskeletal system (hypotonia, minor skeletal anomalies)

### Tissue and Cell Level

**Specific Tissue Types:**
- Nervous tissue (cerebral cortex, corpus callosum, optic nerves, brainstem)
- Cardiac muscle and connective tissue (in congenital heart defects)
- Neural epithelium (retina, optic nerve)

**Specific Cell Populations:**
- Cortical excitatory neurons (pyramidal neurons of layers II/III and V/VI) (blok2018denovomutations pages 1-2, li2026med13isinvolved pages 1-2)
- Neural progenitor cells during neurogenesis (blok2018denovomutations pages 1-2, li2026med13isinvolved pages 1-2)
- Retinal ganglion cells and optic nerve fibers

### Subcellular Level

MED13 localizes to the nucleus as part of the Mediator complex (harper2018thecomplexstructure pages 1-2, poss2013themediatorcomplex pages 2-3).

**GO Cellular Component Terms:**
- GO:0016592 (mediator complex)
- GO:0005634 (nucleus)
- GO:0000790 (nuclear chromatin)

### Localization

**Specific Anatomical Sites (UBERON Terms):**
- UBERON:0000955 (brain)
- UBERON:0001869 (cerebral cortex)
- UBERON:0002335 (corpus callosum)
- UBERON:0000941 (cranial nerve II)
- UBERON:0001873 (caudate nucleus)
- UBERON:0002298 (brainstem)
- UBERON:0002543 (retina)
- UBERON:0000948 (heart)

**Lateralization:**
Generally bilateral for brain and eye findings; heart defects are typically midline structures.

---

## 8. Temporal Development

### Onset

**Typical Age of Onset:**  
Congenital/prenatal for structural malformations (heart defects, dysmorphic features, brain malformations). Developmental delays apparent in infancy (first 6-12 months), with global developmental delay and motor delays recognized early. Speech delays become evident in toddler years (blok2018denovomutations pages 1-2, blok2018denovomutations pages 4-5).

**Onset Pattern:**  
- **Acute:** Not applicable
- **Chronic/Insidious:** The neurodevelopmental delays emerge insidiously as milestones are missed
- **Congenital:** Structural anomalies present from birth

### Progression

**Disease Stages:**  
No formal staging system exists. The disorder does not progress through distinct stages but rather represents a static or slowly improving developmental trajectory once established.

**Progression Rate:**
- **Developmental Trajectory:** After initial recognition of delays, the developmental trajectory tends to be stable with slow progress. Speech and motor skills may improve somewhat with intensive therapy, but intellectual disability persists.
- **Non-Progressive:** Unlike neurodegenerative disorders, MED13 Syndrome does not typically show progressive worsening. However, one patient showed "regression at the age of 13 months" in speech development (blok2018denovomutations pages 4-5), which is atypical.

**Disease Course Pattern:**
- **Stable:** Generally stable neurodevelopmental disability once established
- **Chronic Lifelong:** Lifelong condition requiring ongoing support

**Disease Duration:**  
Lifelong condition.

### Patterns

**Remission:**  
Not applicable; this is not a relapsing-remitting condition.

**Critical Periods:**  
Prenatal and early postnatal brain development represent critical vulnerable periods when MED13 function is essential for proper cortical neurogenesis, neuronal migration, and connectivity establishment (li2026med13isinvolved pages 1-2, miao2018mediatorcomplexcomponent pages 1-2).

---

## 9. Inheritance and Population

### Epidemiology

**Prevalence:**  
Extremely rare. As of 2025, only approximately 26-30 cases have been reported worldwide (yang2025anovelframeshift pages 1-2, yang2025anovelframeshift pages 2-3). True population prevalence unknown but estimated to be less than 1 per million.

**Incidence:**  
Unknown; extremely rare. The rate of approximately 1 de novo MED13 variant per 2,200 DD/ID-affected individuals suggests it accounts for a very small fraction of neurodevelopmental disorders (blok2018denovomutations pages 7-11).

### For Genetic Etiology

**Inheritance Pattern:**  
Autosomal dominant. As Blok et al. state, "Eleven variants were confirmed to be de novo, and one patient (patient B) inherited the variant from her mother who is also affected" (blok2018denovomutations pages 1-2, blok2018denovomutations pages 4-5). More recent reports include additional familial cases with mother-to-child transmission (yang2025anovelframeshift pages 2-3).

**Penetrance:**  
Appears to be complete for core neurodevelopmental features (DD/ID, speech delay) based on all reported cases showing these features. However, variable expressivity is evident, with the same variant (p.Pro327Ser) causing different phenotypic severity in unrelated individuals (nardi2021couldthemed13 pages 1-2, blok2018denovomutations pages 4-5).

**Expressivity:**  
Highly variable. Even individuals with the same variant show phenotypic variability. For example, the recurrent p.Pro327Ser variant was associated with both a Kabuki-like presentation and a less dysmorphic presentation with cardiac features in different patients (nardi2021couldthemed13 pages 1-2, blok2018denovomutations pages 4-5).

**Genetic Anticipation:**  
Not reported or applicable.

**Germline Mosaicism:**  
While not specifically documented for MED13, germline mosaicism is theoretically possible and has been reported for the related MED13L gene (fazio2025geneticclinicaland pages 1-2). Recurrence risk counseling should consider this possibility.

**Founder Effects:**  
No founder effects or population-specific mutations have been identified. The disorder appears to arise from independent de novo mutational events across diverse populations.

**Consanguinity:**  
Not relevant; autosomal dominant disorder arising de novo.

**Carrier Frequency:**  
Not applicable in traditional sense; nearly all cases are de novo. However, affected individuals are heterozygous carriers who can transmit the variant to offspring with 50% probability.

### Population Demographics

**Affected Populations:**  
No specific ethnic or demographic groups show higher prevalence. Cases have been reported from diverse populations including European, North American, Asian (Chinese family), and others (blok2018denovomutations pages 1-2, yang2025anovelframeshift pages 1-2, yang2025anovelframeshift pages 2-3).

**Geographic Distribution:**  
Worldwide distribution with no geographic clustering. Cases reported from United States, Europe (Netherlands, Germany, France, Italy, UK), China, and other regions (blok2018denovomutations pages 1-2, yang2025anovelframeshift pages 2-3).

**Sex Ratio:**  
No strong sex bias. The original cohort included both males and females; approximately balanced sex distribution across reported cases (blok2018denovomutations pages 1-2).

**Age Distribution:**  
Given recent disease description (2018), most reported individuals are children and young adults. One neonatal death demonstrates the potential for severe early presentations (tolmacheva2024expandingphenotypeof pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5).

---

## 10. Diagnostics

### Clinical Tests

**Laboratory Tests:**
- Standard metabolic panels: Generally normal; not diagnostically informative
- Chromosomal microarray: Typically normal unless large deletion encompassing MED13
- Specific biochemical markers: None identified

**Biomarkers:**
No specific circulating biomarkers have been identified for MED13 Syndrome.

**Imaging Studies:**
- **Brain MRI:** May show corpus callosum abnormalities (hypoplasia, agenesis), ventriculomegaly, cerebral/cerebellar atrophy, optic nerve/chiasm abnormalities, brainstem changes in severe cases (tolmacheva2024expandingphenotypeof pages 1-2, blok2018denovomutations pages 6-7, fazio2025geneticclinicaland pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5). However, many patients have normal or only mildly abnormal MRI findings.
- **Echocardiography:** To assess for congenital heart defects
- **Ophthalmologic Examination:** Fundoscopy, optical coherence tomography (OCT) for optic nerve assessment

**Functional Tests:**
- Developmental assessments (Gesell Developmental Diagnostic Scale, Bayley Scales)
- IQ testing (WISC, Stanford-Binet)
- Speech/language evaluations
- Vision and hearing assessments
- Electroencephalography (EEG) if seizures suspected

### Genetic Testing

**Overview:**  
Whole exome sequencing (WES) or comprehensive neurodevelopmental gene panels are the primary diagnostic approaches. As Yang et al. (2025) describe, "Whole-exome sequencing of the proband revealed a novel heterozygous frameshift variant in the MED13 gene" (yang2025anovelframeshift pages 2-3).

**Recommended Approach:**
- **First-line:** WES trio sequencing (proband + both parents) to identify de novo variants and confirm inheritance pattern
- **Alternative:** Targeted gene panels for neurodevelopmental disorders that include MED13

**Whole Exome Sequencing (WES):**  
WES is the most effective approach, allowing identification of rare variants across all coding regions. Trio sequencing (proband + parents) is strongly recommended to confirm de novo status, which provides strong evidence for pathogenicity (blok2018denovomutations pages 1-2, yang2025anovelframeshift pages 2-3).

**Gene Panels:**  
Neurodevelopmental disorder panels typically include MED13 among hundreds of other genes associated with DD/ID, autism, and epilepsy (blok2018denovomutations pages 1-2).

**Single Gene Testing:**  
Sanger sequencing of MED13 can be used for targeted confirmation of suspected variants or for family segregation studies (blok2018denovomutations pages 1-2, yang2025anovelframeshift pages 2-3).

**Variant Interpretation:**  
Variants are classified using ACMG/AMP guidelines. Key criteria include:
- Absence from population databases (gnomAD, TOPMED)
- De novo occurrence in affected individual
- High conservation of affected residues
- In silico prediction scores (CADD, PolyPhen-2, SIFT, MutationTaster)
- Functional data when available
- Clustering of variants in functional domains (blok2018denovomutations pages 1-2, tolmacheva2024expandingphenotypeof pages 1-2, blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11, yang2025anovelframeshift pages 2-3)

**Functional Validation (Research Setting):**
- qPCR to assess MED13 transcript levels (blok2018denovomutations pages 7-11)
- Western blot to assess protein levels and detect truncated products (blok2018denovomutations pages 7-11)
- Modeling of variant effects on protein structure and interactions (blok2018denovomutations pages 7-11)

### Clinical Criteria

**Standardized Diagnostic Criteria:**  
No formal consensus diagnostic criteria yet established. Clinical diagnosis based on constellation of features:
- **Major criteria:** Developmental delay/intellectual disability AND speech/language disorder
- **Supportive criteria:** Autism, ADHD, dysmorphic facial features, eye abnormalities, heart defects, hypotonia, motor delays
- **Molecular confirmation:** Pathogenic or likely pathogenic variant in MED13

**Differential Diagnosis:**
MED13 Syndrome should be distinguished from:
- **Kabuki syndrome:** Phenotypic overlap noted; MED13 variant was identified in a patient initially suspected to have Kabuki syndrome (nardi2021couldthemed13 pages 1-2)
- **Other Mediator complex disorders:** MED13L syndrome (more severe ID, higher seizure frequency); MED12-related X-linked ID; CDK8-related syndrome (nardi2021couldthemed13 pages 1-2, fazio2025geneticclinicaland pages 1-2, poot2019mutationsinmediator pages 1-1, fazio2025geneticclinicaland pages 2-4)
- **22q11.2 deletion syndrome:** Similar developmental and cardiac features
- **Other syndromic ID conditions:** Numerous syndromes present with DD/ID, speech delays, and dysmorphic features

### Screening

**Newborn Screening:**  
Not included in standard newborn screening panels.

**Carrier Screening:**  
Not applicable; disorder arises predominantly de novo.

**Prenatal Testing:**  
Available for families with known pathogenic variant. Includes:
- Chorionic villus sampling (CVS)
- Amniocentesis
- Cell-free fetal DNA testing (research/specialty labs)

**Cascade Screening:**  
Not routinely performed; family members of affected individuals with inherited variants should receive genetic counseling and may opt for testing.

---

## 11. Outcome/Prognosis

### Survival and Mortality

**Survival Rate:**  
Generally good for typical presentations. Most individuals survive to adulthood with appropriate supportive care.

**Life Expectancy:**  
Near-normal life expectancy expected for most patients. However, one severe neonatal case resulted in death at 76 days due to multiple organ failure (tolmacheva2024expandingphenotypeof pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5), indicating that rare severe presentations can be life-threatening.

**Mortality Rate:**  
Very low in typical cases. The neonatal death case represents the severe end of the phenotypic spectrum.

**Disease-Specific Mortality:**  
Rare; complications from severe heart defects or epilepsy could theoretically contribute to mortality in severe cases.

### Morbidity and Function

**Morbidity:**  
Significant lifelong morbidity related to intellectual disability, speech impairment, and associated features. Quality of life can be substantially impacted by:
- Educational challenges and need for special education
- Social interaction difficulties, especially with comorbid autism
- Communication barriers due to severe speech disorders
- Visual impairment in those with optic nerve abnormalities
- Chronic constipation/GI issues

**Disability Outcomes:**  
Most individuals require ongoing support and accommodations throughout life. Degree of independence varies with severity of ID; those with mild ID may achieve semi-independent living with support, while those with moderate ID typically require more substantial lifelong assistance.

**Quality of Life Measures:**  
Not systematically reported in published case series. Expected to be reduced compared to general population, but can be improved with appropriate therapies, educational support, and behavioral interventions.

### Disease Course

**Complications:**
- Chronic constipation (31% in original cohort) (blok2018denovomutations pages 6-7)
- Feeding difficulties in infancy
- Behavioral problems associated with autism/ADHD
- Visual impairment from optic nerve abnormalities or uncorrected refractive errors
- Seizures (rare but can be severe and drug-resistant when present) (blok2018denovomutations pages 6-7)
- Orthopedic complications (scoliosis, joint issues)
- Cardiac complications from congenital heart defects

**Recovery Potential:**  
No cure or full recovery possible. However, developmental trajectory can improve with:
- Intensive speech and language therapy
- Physical and occupational therapy for motor skills
- Educational interventions tailored to cognitive level
- Behavioral therapies for autism/ADHD
Some patients show meaningful gains in communication and adaptive skills with comprehensive intervention, though intellectual disability persists.

### Prediction

**Prognostic Factors:**
- **Severity of ID:** Mild ID associated with better functional outcomes than moderate/severe ID
- **Presence of seizures:** Drug-resistant epilepsy associated with poorer developmental outcomes
- **Severity of speech impairment:** Those with childhood apraxia of speech have more profound communication challenges
- **Cardiac defects:** Severe congenital heart disease can impact overall health and development
- **Early intervention:** Access to early intensive therapies may improve developmental trajectory

**Prognostic Biomarkers:**  
None identified. Genotype-phenotype correlations are emerging (e.g., C-terminal variants associated with Duane anomaly), but do not yet reliably predict overall severity (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11).

---

## 12. Treatment

### Pharmacotherapy

**No Disease-Specific Pharmacological Treatments:**  
There are currently no medications that target the underlying genetic or molecular cause of MED13 Syndrome.

**Symptomatic Pharmacotherapy:**
- **Anti-epileptic drugs (AEDs):** For patients with seizures; choice of AED depends on seizure type (e.g., valproic acid, levetiracetam for generalized seizures)
- **ADHD medications:** Stimulants (methylphenidate, amphetamines) or non-stimulants (atomoxetine, guanfacine) for attention and behavioral management in those with ADHD
- **Antipsychotics/mood stabilizers:** May be used for severe behavioral problems, though with caution given side effect profiles
- **Gastrointestinal medications:** Laxatives, stool softeners, or motility agents for chronic constipation

**Pharmacogenomics:**  
Not specifically studied for MED13 Syndrome. Standard pharmacogenomic considerations for AED metabolism and ADHD medication response may apply.

### Advanced Therapeutics

**Gene Therapy:**  
Not currently available. Given the autosomal dominant inheritance with likely gain-of-dysfunction mechanisms for some variants (phosphodegron mutations), gene therapy would be complex, potentially requiring allele-specific silencing or gene editing rather than simple gene addition.

**Cell Therapy:**  
Not applicable.

**RNA-Based Therapies:**  
Not currently available. Antisense oligonucleotides (ASOs) targeting mutant MED13 transcripts could theoretically be developed for specific variants.

**Targeted Therapies:**  
None currently available.

### Surgical and Interventional

**Cardiac Surgery:**  
Surgical correction or intervention for congenital heart defects as indicated (e.g., repair of ventricular septal defects, coarctation repair) (tolmacheva2024expandingphenotypeof pages 1-2).

**Gastrointestinal Surgery:**  
Surgical management for severe constipation or megacolon if conservative management fails (yang2025anovelframeshift pages 2-3).

**Orthopedic Interventions:**  
Management of scoliosis, hip dysplasia, or other skeletal abnormalities as needed.

### Supportive and Rehabilitative

**Speech and Language Therapy:**  
Essential intervention for all patients given universal speech/language impairment. Focus on:
- Augmentative and alternative communication (AAC) for those with severe apraxia
- Oral motor therapy
- Language comprehension and expression training

**Physical Therapy:**  
For motor delays and hypotonia; aims to improve gross motor skills, strength, coordination.

**Occupational Therapy:**  
To develop fine motor skills, adaptive behaviors, and activities of daily living.

**Educational Interventions:**  
Individualized Education Programs (IEPs) tailored to cognitive abilities; may include special education services, classroom accommodations, one-on-one aides.

**Behavioral Therapies:**  
- Applied Behavior Analysis (ABA) for autism-related behaviors
- Cognitive-behavioral therapy (CBT) for older children/adults with ADHD or anxiety
- Social skills training

**Ophthalmologic Care:**  
Regular eye exams; correction of refractive errors; low vision services if visual impairment present; monitoring for progressive optic atrophy.

**Cardiac Monitoring:**  
Regular cardiology follow-up for those with congenital heart defects.

**Nutritional Support:**  
Management of feeding difficulties in infancy; dietary modifications for constipation.

### Experimental

**Clinical Trials:**  
No specific clinical trials for MED13 Syndrome are currently registered. Patients may be eligible for trials targeting broader categories (neurodevelopmental disorders, intellectual disability).

### Treatment Outcomes

**Treatment Response:**  
Supportive therapies can improve functional outcomes and quality of life, but do not reverse the underlying disorder. Speech therapy can lead to meaningful communication gains in some patients. Behavioral therapies can reduce problematic behaviors and improve social functioning.

**Side Effects:**  
Depend on specific medications used. AEDs may cause sedation, cognitive effects. ADHD medications may cause appetite suppression, sleep disturbances. Surgical interventions carry standard operative risks.

### Treatment Strategy

**Multidisciplinary Approach:**  
Optimal management involves coordinated care from:
- Medical geneticist
- Developmental pediatrician or neurologist
- Speech-language pathologist
- Physical and occupational therapists
- Educational specialists
- Behavioral therapist/psychologist
- Ophthalmologist
- Cardiologist (if heart defects present)
- Gastroenterologist (if GI issues present)

**Treatment Algorithms:**  
No formal published algorithms. General approach:
1. Confirm genetic diagnosis via WES
2. Comprehensive baseline assessments (developmental, speech/language, cardiac, ophthalmologic)
3. Initiate early intervention therapies (speech, PT, OT)
4. Enroll in appropriate educational programs with IEP
5. Manage comorbidities (seizures, ADHD, GI issues) as they arise
6. Provide genetic counseling to family
7. Ongoing monitoring and adjustment of therapies

**Suggested MAXO Terms:**
- MAXO:0000011 (speech therapy)
- MAXO:0000127 (physical therapy)
- MAXO:0000128 (occupational therapy)
- MAXO:0000218 (special education)
- MAXO:0000058 (pharmaceutical therapy) - for symptomatic medications
- MAXO:0001298 (genetic counseling)

---

## 13. Prevention

### Prevention Levels

**Primary Prevention:**  
Not applicable for de novo genetic disorder. However, preconception genetic counseling for rare families with inherited variants can inform reproductive decisions.

**Secondary Prevention:**  
Early diagnosis through comprehensive developmental screening and genetic testing allows for:
- Early intervention therapies to optimize developmental outcomes
- Appropriate medical surveillance (cardiac, ophthalmologic)
- Family planning and genetic counseling for future pregnancies

**Tertiary Prevention:**  
Ongoing management to prevent complications:
- Regular ophthalmology to detect and treat progressive vision problems
- Cardiac monitoring to prevent decompensation of heart defects
- Aggressive management of constipation to prevent bowel obstruction
- Seizure management to prevent status epilepticus

### Screening and Early Detection

**Newborn Screening:**  
Not currently included.

**Genetic Screening:**
- **Prenatal Testing:** Available for families with known MED13 variant; chorionic villus sampling or amniocentesis
- **Preimplantation Genetic Diagnosis (PGD):** Theoretically available for families with known variant who undergo IVF
- **Carrier Screening:** Not applicable; disorder arises de novo in vast majority of cases

**Risk Stratification:**  
Families with one affected child have recurrence risk primarily dependent on possibility of parental germline mosaicism (estimated 1-2% based on other dominant disorders), unless a parent is confirmed to carry the variant (50% recurrence risk per pregnancy).

### Counseling

**Genetic Counseling:**  
Essential component of care. Should cover:
- Explanation of autosomal dominant inheritance
- De novo occurrence in vast majority of cases
- Low recurrence risk for parents of affected child (unless parent is carrier)
- 50% transmission risk for affected individuals if they reproduce
- Availability of prenatal testing/PGD for future pregnancies
- Natural history and expected outcomes
- Support resources and family organizations

As stated by Yang et al. (2025), "This study also highlights the importance of preconception genetic counseling for couples with suspected genetic disease" (yang2025anovelframeshift pages 2-3).

---

## 14. Other Species / Natural Disease

### Taxonomy

MED13 orthologs exist across eukaryotes, reflecting its ancient and essential role in transcriptional regulation (poss2013themediatorcomplex pages 2-3).

- Humans (Homo sapiens): NCBI Taxon 9606
- Mouse (Mus musculus): NCBI Taxon 10090
- Zebrafish (Danio rerio): NCBI Taxon 7955
- Fruit fly (Drosophila melanogaster): NCBI Taxon 7227
- Nematode (Caenorhabditis elegans): NCBI Taxon 6239
- Yeast (Saccharomyces cerevisiae): NCBI Taxon 4932

### Gene Orthologs

Human MED13 has orthologs across species with varying degrees of sequence conservation. According to Poss et al. (2013), MED13 shows 13% identity to yeast Saccharomyces cerevisiae, 27% to Drosophila, and 94% to mouse (poss2013themediatorcomplex pages 2-3).

### Natural Disease

No naturally occurring MED13-related neurodevelopmental disorders have been documented in veterinary medicine or wildlife populations. This is likely due to:
1. Embryonic lethality of complete loss-of-function
2. Reduced reproductive fitness of affected individuals
3. Limited veterinary genetic diagnostics for rare neurodevelopmental conditions

### Comparative Biology

**Evolutionary Conservation:**  
MED13 function is highly conserved. As noted by Poss et al., "MED13, as well as the other subunits of the CDK8-module, are known to be critical regulators of developmental gene expression programs in Drosophila, zebrafish and C. elegans" (blok2018denovomutations pages 7-11).

---

## 15. Model Organisms

### Model Types and Systems

**Mammalian Models:**

**Mouse (Mus musculus):**

*Complete Knockout:*  
Complete Med13 knockout in mice results in embryonic lethality. As reported by Miao et al. (2018), "genetic inactivation of Med13 caused embryonic lethality as early as embryonic day (E) 8.5 in mouse" (miao2018mediatorcomplexcomponent pages 1-2), indicating absolute requirement for early development.

*Conditional Knockout Models:*  
Conditional Med13 knockout models have been generated to study tissue-specific functions:
- **Cardiac-specific knockout:** Med13 floxed allele with cardiac-specific Cre demonstrated roles in cardiac metabolism and systemic energy homeostasis (baskin2014med13‐dependentsignalingfrom pages 1-2)
- **Skeletal muscle-specific knockout:** Demonstrated Med13 roles in glucose homeostasis (baskin2014med13‐dependentsignalingfrom pages 1-2)
- **Oocyte-specific knockout:** Showed Med13 is essential for zygotic genome activation (miao2018mediatorcomplexcomponent pages 1-2)

*In Utero Electroporation Models:*  
Li et al. (2026) used in utero electroporation to knock down Med13 in developing cortical neurons, demonstrating that "silencing Med13 in cortical neurons impaired its radial migration and contralateral projection as well as dendritic complexity in mice" (li2026med13isinvolved pages 1-2). This model recapitulates neurodevelopmental aspects of the human syndrome.

*Heterozygous Models:*  
While full characterization of heterozygous Med13 mice phenotype is not extensively published, such models would be most relevant to human haploinsufficiency. Studies suggest heterozygous mice may display some neurodevelopmental phenotypes (li2026med13isinvolved pages 1-2).

**Invertebrate Models:**

**Drosophila melanogaster:**  
Studies in Drosophila have shown that Med12 and Med13 subunits are "essential for the transcription of Wingless target genes" and play critical developmental roles (poss2013themediatorcomplex pages 2-3). Drosophila models provide insights into conserved Mediator functions in development.

**Caenorhabditis elegans:**  
C. elegans has been used to study Mediator complex functions in development, though specific Med13 models for neurodevelopmental phenotypes are not extensively characterized in the context of human disease modeling.

### Cellular Models

**Human Neuroblastoma Cells (SH-SY5Y):**  
Li et al. (2026) generated MED13-deficient SH-SY5Y cells using CRISPR-Cas9. "Differential protein analysis of human MED13-deficient SH-SY5Y cells revealed a large number of dysregulated proteins, including PLXNA4" (li2026med13isinvolved pages 1-2), providing insights into downstream pathways affected by MED13 loss.

**Induced Pluripotent Stem Cells (iPSCs):**  
While not yet reported for MED13 patients specifically, iPSC-derived neurons from patients would be valuable for studying disease mechanisms and testing therapeutics.

**Primary Fibroblasts:**  
Western blot studies on patient blood mononuclear cells have been used to assess MED13 protein levels (blok2018denovomutations pages 7-11). Patient fibroblasts could similarly be used for biochemical studies.

### Model Characteristics

**Phenotype Recapitulation:**

*Mouse Models:*
- **Embryonic lethality** in complete knockouts recapitulates the essential developmental role
- **Neuronal migration and dendritic defects** in conditional/knockdown models parallel human neurodevelopmental abnormalities
- **Metabolic phenotypes** in tissue-specific models may relate to systemic features in some patients

*Limitations:*  
- Complete knockout mice die early in embryogenesis, precluding study of postnatal neurodevelopmental trajectory
- Heterozygous mice have not been fully characterized for all features of human syndrome
- Mouse models cannot fully recapitulate human-specific higher cognitive functions and speech

**Applications:**

*Research Applications:*
- Understanding transcriptional mechanisms during neurogenesis and neuronal migration
- Identifying downstream targets and pathways (e.g., PlxnA4 in migration) (li2026med13isinvolved pages 1-2)
- Testing potential therapeutic interventions in preclinical setting
- Studying genotype-phenotype correlations by introducing specific patient variants

### Resources

**Model Organism Databases:**
- MGI (Mouse Genome Informatics): Med13 gene ID MGI:1916232
- RGD (Rat Genome Database): Med13 ortholog information
- FlyBase: Drosophila Med13 ortholog
- WormBase: C. elegans Med13 ortholog
- IMSR (International Mouse Strain Resource): For locating specific Med13 mouse models
- KOMP (Knockout Mouse Project): Resources for generating knockout models

---

## Summary Tables

For ease of reference, two comprehensive tables summarizing clinical phenotypes and genetic/molecular features are provided below.

| Phenotype / feature | Frequency among reported patients | Severity / variability | Typical age of onset | Suggested HPO term(s) | Key citations |
|---|---:|---|---|---|---|
| Developmental delay / global developmental delay | 13/13 (100%) in initial cohort; also core feature in later reports | Mild to severe; variable course | Infancy / early childhood | HP:0001263 Global developmental delay; HP:0011344 Severe global developmental delay | (blok2018denovomutations pages 1-2, blok2018denovomutations pages 7-11, tolmacheva2024expandingphenotypeof pages 1-2, yang2025anovelframeshift pages 1-2) |
| Intellectual disability | Present in essentially all reported individuals, though severity ranges from borderline to moderate/severe; some described as DD/ID rather than formal ID | Borderline/mild to moderate; severe developmental impairment in rare neonatal cases | Usually recognized in childhood | HP:0001249 Intellectual disability; HP:0001256 Mild intellectual disability; HP:0002342 Moderate intellectual disability | (blok2018denovomutations pages 1-2, blok2018denovomutations pages 4-5, blok2018denovomutations pages 7-11, nardi2021couldthemed13 pages 1-2) |
| Speech delay / language disorder | 13/13 (100%) in initial cohort | Often severe; expressive language commonly more impaired than receptive language | Infancy / toddler years | HP:0000750 Delayed speech and language development; HP:0002463 Language impairment | (blok2018denovomutations pages 1-2, blok2018denovomutations pages 4-5, blok2018denovomutations pages 7-11, nardi2021couldthemed13 pages 1-2) |
| Childhood apraxia of speech / severe speech production disorder | 3/13 (~23%) in initial cohort explicitly described with speech apraxia | Can be profound, including nonverbal status or limited verbal output | Early childhood | HP:0012469 Childhood apraxia of speech; HP:0001344 Expressive language delay | (blok2018denovomutations pages 2-4, blok2018denovomutations pages 4-5) |
| Motor developmental delay | 7/13 (~54%) in initial cohort; recurrent in later case reports | Mostly gross motor delay; variable | Infancy | HP:0001270 Motor delay; HP:0002194 Delayed gross motor development; HP:0010862 Delayed fine motor development | (blok2018denovomutations pages 2-4, blok2018denovomutations pages 6-7, nardi2021couldthemed13 pages 1-2, yang2025anovelframeshift pages 2-3) |
| Hypotonia | 3/13 (~23%) in initial cohort; described as common infantile feature in later summaries | Usually mild to moderate; often infantile | Infancy | HP:0001252 Muscular hypotonia | (blok2018denovomutations pages 6-7, nardi2021couldthemed13 pages 1-2, yang2025anovelframeshift pages 1-2) |
| Autism spectrum disorder | 5/13 (~38%) in initial cohort; recurrent across later reports and reviews | Variable behavioral severity | Childhood | HP:0000729 Autism | (blok2018denovomutations pages 2-4, blok2018denovomutations pages 1-2, nardi2021couldthemed13 pages 1-2, fazio2025geneticclinicaland pages 1-2) |
| Attention-deficit / hyperactivity disorder | 3/13 (~23%) in initial cohort | Variable | Childhood / school age | HP:0007018 Attention deficit hyperactivity disorder | (blok2018denovomutations pages 2-4, blok2018denovomutations pages 1-2, nardi2021couldthemed13 pages 1-2) |
| Dysmorphic facial features | Common; described as overlapping facial gestalt in multiple patients | Usually mild to moderate; variable expressivity | Congenital / infancy | HP:0001999 Facial dysmorphism; HP:0000316 Hypertelorism; HP:0000450 Broad nasal bridge; HP:0010800 Long philtrum / HP:0000343 Long philtrum as applicable | (blok2018denovomutations pages 5-6, nardi2021couldthemed13 pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5, yang2025anovelframeshift pages 2-3) |
| Eye / vision abnormalities (overall) | 8/13 (~62%) in initial cohort | Mild to severe; includes structural and functional abnormalities | Congenital or childhood | HP:0000505 Visual impairment; HP:0000618 Blindness / low vision umbrella if severe; HP:0000529 Progressive visual loss where relevant | (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11, tolmacheva2024expandingphenotypeof pages 1-2) |
| Optic nerve abnormalities | 3/13 in initial cohort; severe optic nerve/chiasm atrophy in neonatal case | Variable, can be severe | Congenital / childhood | HP:0001138 Optic atrophy; HP:0001098 Abnormality of the optic nerve | (blok2018denovomutations pages 6-7, tolmacheva2024expandingphenotypeof pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5) |
| Duane anomaly / strabismus spectrum | Duane anomaly 2/13 (~15%); strabismus also reported | Variable | Congenital / early childhood | HP:0009928 Duane anomaly; HP:0000486 Strabismus | (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11) |
| Astigmatism / nystagmus / retinal findings | Each uncommon but recurrent across cases | Variable | Childhood / congenital | HP:0000483 Astigmatism; HP:0000639 Nystagmus; HP:0000556 Retinal dystrophy | (blok2018denovomutations pages 6-7, tolmacheva2024expandingphenotypeof pages 2-5) |
| Congenital heart defects / mild cardiac anomalies | 2/13 (~15%) in initial cohort; more severe congenital heart disease in 2024 neonatal case | Usually mild in early cohort; rare severe neonatal presentation | Congenital | HP:0001627 Abnormality of the cardiovascular system; HP:0001631 Aortic root dilatation; HP:0001671 Atrial septal defect; HP:0001629 Ventricular septal defect; HP:0001680 Coarctation of aorta / isthmus hypoplasia as applicable | (blok2018denovomutations pages 6-7, tolmacheva2024expandingphenotypeof pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5) |
| Epilepsy / seizures | Rare in initial cohort (1/13, ~8%); later reports expanded spectrum to epileptic encephalopathy | Can be severe and drug-resistant when present | Childhood or infancy depending on case | HP:0001250 Seizure; HP:0002123 Generalized myoclonic seizure; HP:0012468 Epileptic encephalopathy | (blok2018denovomutations pages 6-7, rivera2024med13genemutation pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5) |
| Brain MRI abnormalities | Uncommon in original cohort but increasingly recognized in later reports | Variable; from mild frontal atrophy to severe callosal/brainstem/chiasmal abnormalities | Infant / childhood | HP:0001273 Abnormality of the corpus callosum; HP:0002060 Abnormality of the cerebral white matter; HP:0002283 Ventriculomegaly; HP:0007364 Hydrocephalus | (blok2018denovomutations pages 6-7, tolmacheva2024expandingphenotypeof pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5, fazio2025geneticclinicaland pages 1-2) |
| Corpus callosum abnormalities | Reported in severe recent cases/reviews | Moderate to severe | Congenital / infancy | HP:0001273 Abnormality of the corpus callosum; HP:0002079 Hypoplasia of the corpus callosum | (tolmacheva2024expandingphenotypeof pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5, fazio2025geneticclinicaland pages 1-2) |
| Microcephaly / growth restriction / short stature | Reported in subset; severe neonatal case had growth restriction; later family report notes restricted growth | Variable | Prenatal or postnatal | HP:0000252 Microcephaly; HP:0001511 Intrauterine growth restriction; HP:0004322 Short stature | (tolmacheva2024expandingphenotypeof pages 1-2, yang2025anovelframeshift pages 1-2, yang2025anovelframeshift pages 2-3) |
| Chronic constipation / obstipation / megacolon | Obstipation in 4/13 (~31%) in initial cohort; congenital megacolon reported as novel complication in family report | Usually chronic; occasionally severe | Infancy / childhood | HP:0002019 Constipation; HP:0002240 Chronic constipation; HP:0012707 Megacolon | (blok2018denovomutations pages 6-7, yang2025anovelframeshift pages 1-2, yang2025anovelframeshift pages 2-3) |
| Hearing loss | 2/13 (~15%) conductive hearing loss in initial cohort; hearing/vision problems noted in later reports | Mild to moderate | Childhood | HP:0000405 Conductive hearing impairment; HP:0000365 Hearing impairment | (blok2018denovomutations pages 5-6, tolmacheva2024expandingphenotypeof pages 1-2) |
| Orthopedic / skeletal anomalies | Recurrent but variable; scoliosis, pes cavus, brachydactyly, hip dysplasia, valgus-pronated feet reported | Mild to moderate | Childhood / congenital | HP:0002650 Scoliosis; HP:0001761 Pes cavus; HP:0001156 Brachydactyly; HP:0001385 Hip dysplasia | (blok2018denovomutations pages 5-6, nardi2021couldthemed13 pages 1-2) |
| Severe multisystem neonatal presentation | Very rare; single recent neonate with hydrocephalic changes, optic/chiasm atrophy, bowel atresia, cardiac disease, multiple organ failure, neonatal death | Severe / potentially lethal | Prenatal to neonatal | HP:0001627 Abnormality of the cardiovascular system; HP:0001138 Optic atrophy; HP:0002079 Hypoplasia of the corpus callosum; HP:0002586 Ileal atresia; HP:0003819 Neonatal death | (tolmacheva2024expandingphenotypeof pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5) |


*Table: This table summarizes the core and variable clinical features reported for MED13 syndrome, including approximate frequencies, severity patterns, onset, suggested HPO mappings, and supporting citations. It is useful for disease knowledge base curation and phenotype annotation.*

| Variant / protein change | cDNA change | Variant type | Source / case context | Protein region / domain affected | Clustering pattern | Reported / inferred functional consequence | Pathogenicity classification / evidence level | CADD / in silico data | Conservation / population data | Key notes / citations |
|---|---|---|---|---|---|---|---|---|---|---|
| p.Pro42Leufs*6 | c.125del | Frameshift | Blok 2018 patient A | N-terminus, upstream of annotated Med13_N domain | Non-clustered truncating variant | Predicted premature termination; likely loss of normal function | Likely pathogenic / pathogenic by case-series evidence | CADD 31.0 | Absent from gnomAD/TOPMed in cohort analysis | Associated with mild ID and speech apraxia in original cohort (blok2018denovomutations pages 1-2, blok2018denovomutations pages 4-5, blok2018denovomutations pages 7-11) |
| p.Leu131* | c.392T>G | Nonsense | Blok 2018 patients B/C | N-terminal region, upstream of Med13_N domain | Recurrent truncating variant | Predicted truncation; transcript detected on cDNA, but no truncated protein detected in analogous nonsense case, supporting abnormal protein consequence rather than simple transcript loss | Pathogenic by segregation/case evidence | CADD 37.0 | Absent from gnomAD/TOPMed in cohort analysis | One inherited instance from affected mother to affected child shows AD transmission with variable expressivity (blok2018denovomutations pages 1-2, blok2018denovomutations pages 4-5, blok2018denovomutations pages 7-11) |
| p.Thr326Ile | c.977C>T | Missense | Blok 2018 patient D | Conserved N-terminal phosphodegron within/near Med13_N domain | N-terminal hotspot | Predicted to impair FBW7 phosphodegron recognition and alter MED13 ubiquitination/degradation, potentially increasing abnormal MED13 stability | Likely pathogenic by clustering/mechanistic evidence | CADD 25.0 | Site highly conserved; codon under strong selection; absent from gnomAD/TOPMed | One of four variants affecting Thr326/Pro327 hotspot (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11) |
| p.Thr326del | c.975_977delTAC | In-frame deletion | Blok 2018 patient E | Conserved N-terminal phosphodegron within/near Med13_N domain | N-terminal hotspot | Predicted disruption of phosphodegron and impaired SCF-FBW7-mediated degradation | Likely pathogenic by hotspot/mechanistic evidence | CADD 20.5 | Highly conserved motif; absent from gnomAD/TOPMed | Only in-frame deletion in original cohort; still localized to same hotspot as missense variants (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11) |
| p.Pro327Ser | c.979C>T | Missense | Blok 2018 patient F; Nardi 2021; recurrent in later reports | Conserved N-terminal phosphodegron within/near Med13_N domain | N-terminal hotspot, recurrent | Predicted to reduce phosphodegron-dependent FBW7 binding and MED13 turnover | Likely pathogenic; recurrent across unrelated patients | CADD 23.4 | Highly conserved residue; absent from gnomAD/TOPMed | Recurrent variant with variable expressivity, from neurodevelopmental phenotype to Kabuki-like presentation (nardi2021couldthemed13 pages 1-2, blok2018denovomutations pages 4-5, blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11) |
| p.Pro327Gln | c.980C>A | Missense | Blok 2018 patient G | Conserved N-terminal phosphodegron within/near Med13_N domain | N-terminal hotspot | Same predicted mechanism as other phosphodegron variants: altered phosphorylation/FBW7 interaction and defective degradation | Likely pathogenic by hotspot/mechanistic evidence | CADD 25.2 | Highly conserved; absent from gnomAD/TOPMed | Supports hotspot-specific mechanism at adjacent residues Thr326/Pro327 (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11) |
| p.Pro540Thr | c.1618C>A | Missense | Blok 2018 patient H | Internal conserved linear motif outside named Pfam domains | Non-hotspot missense | Predicted formation of novel Casein Kinase 1 phosphorylation motif and altered protein interactions | VUS-to-likely pathogenic range by case/mechanistic evidence | CADD 26.3 | Highly conserved motif; codon under strong selection; absent from gnomAD/TOPMed | Distinct mechanism proposed versus phosphodegron variants (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11) |
| p.Leu582* | c.1745T>A | Nonsense | Blok 2018 patient I | Internal region between N- and C-terminal domains | Non-clustered truncating variant | Predicted loss of downstream functional regions and loss of normal function | Pathogenic by case evidence | CADD 40.0 | Absent from gnomAD/TOPMed | Truncating variants distributed outside missense hotspots (blok2018denovomutations pages 4-5, blok2018denovomutations pages 6-7) |
| p.Arg1400* | c.4198C>T | Nonsense | Blok 2018 patient J | Mid-protein region, upstream of Med13_C domain | Non-clustered truncating variant | cDNA present, but no truncated protein detected on western blot; supports abnormal protein consequence / defective stable product | Pathogenic by functional follow-up | CADD 41.0 | Absent from gnomAD/TOPMed | Functional transcript/protein analyses were performed for this allele (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11) |
| p.Thr1496Metfs*11 | c.4487delC | Frameshift | Blok 2018 patient K | Mid/C-terminal transition, upstream of Med13_C domain | Non-clustered truncating variant | Predicted premature truncation with loss of C-terminal region | Pathogenic by case evidence | CADD 35.0 | Absent from gnomAD/TOPMed | Associated with severe speech disorder/regression in cohort (blok2018denovomutations pages 4-5, blok2018denovomutations pages 6-7) |
| p.Gln2060Lys | c.6178C>A | Missense | Blok 2018 patient L | C-terminal Med13_C domain | C-terminal hotspot | Predicted disturbance of conserved surface-exposed motif / interaction interface | Likely pathogenic by clustering and conservation | CADD 24.1 | Highly conserved; absent from gnomAD/TOPMed | One of two adjacent C-terminal hotspot variants in patients with eye findings including Duane anomaly (blok2018denovomutations pages 4-5, blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11) |
| p.Ala2064Val | c.6191C>T | Missense | Blok 2018 patient M | C-terminal Med13_C domain | C-terminal hotspot | Predicted structural alteration with increased hydrophobic collapse and reduced linear interaction potential on conserved surface motif | Likely pathogenic by structural modeling | CADD 25.7 | Highly conserved; absent from gnomAD/TOPMed | Supports second missense hotspot in C-terminal region (blok2018denovomutations pages 4-5, blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11) |
| p.Pro835Ser | reported as de novo missense variant in 2024 case report | Missense | Tolmacheva 2024 severe neonatal case | Mid-protein region, outside named hotspot in available summary | Non-hotspot missense | Not mapped to a known functional center in UniProt summary, but predicted damaging; may underlie severe multisystem/neonatal phenotype | Likely pathogenic per ACMG in report | CADD 26.1; PolyPhen-2 0.996; SIFT 0.0 | Position conserved across vertebrates per UCSC alignment; de novo; absent/rare in population databases implied by diagnostic filtering | Expanded phenotype to severe neonatal presentation and death (tolmacheva2024expandingphenotypeof pages 1-2, tolmacheva2024expandingphenotypeof pages 2-5) |
| p.Arg1882Serfs*9 | c.5641delinsTC | Frameshift | Yang 2025 Chinese family | Distal C-terminal half, upstream of Med13_C tail end | Non-clustered truncating variant | Predicted truncation with autosomal dominant disease mechanism | Pathogenic/likely pathogenic by familial segregation and ACMG-based interpretation | Not numerically reported in excerpt | Rare after filtering at MAF ≤0.001; segregated with affected mother and proband | First reported Chinese family; supports inherited AD disease and expands variant spectrum (yang2025anovelframeshift pages 1-2, yang2025anovelframeshift pages 2-3) |
| Overall MED13 variant spectrum | Multiple | Missense, nonsense, frameshift, in-frame deletion | Blok 2018 + recent reports | Two annotated Pfam domains: Med13_N (aa 11-383) and Med13_C (aa 1640-2163), plus conserved internal motifs | Strong clustering of non-truncating variants in two regions: N-terminal phosphodegron hotspot (Thr326/Pro327) and C-terminal hotspot around Gln2060/Ala2064 | Truncating variants support loss-of-function/haploinsufficiency-like mechanism; hotspot missense variants suggest altered degradation or altered protein interaction surfaces | Disease-gene relationship supported by significant enrichment of de novo variants in DD/ID cohorts (p=0.00371) | CADD range for reported 2018 variants: 20.5-41.0 | All 12 unique Blok 2018 variants absent from gnomAD and TOPMed; missense hotspot residues highly conserved and under codon selection | Best current model is mixed mechanism: truncating alleles causing loss of normal function and clustered missense alleles perturbing regulated MED13 turnover or conserved interaction motifs (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11, yang2025anovelframeshift pages 2-3) |


*Table: This table summarizes the reported genetic and molecular features of MED13 syndrome, including representative variants, domains, clustering, functional interpretations, and available in silico evidence. It is useful for disease knowledge base curation and for distinguishing truncating versus hotspot missense mechanisms.*

---

## Conclusions

MED13 Syndrome represents a recently recognized autosomal dominant neurodevelopmental disorder characterized by universal developmental delay/intellectual disability and speech/language disorders, along with variable additional features including autism, ADHD, dysmorphic facial features, ophthalmologic abnormalities, and mild cardiac defects (blok2018denovomutations pages 1-2, blok2018denovomutations pages 4-5, fazio2025geneticclinicaland pages 1-2). The disorder results from heterozygous pathogenic variants in the MED13 gene, which encodes a critical subunit of the CDK8-kinase module of the Mediator complex essential for RNA polymerase II transcription (blok2018denovomutations pages 1-2, harper2018thecomplexstructure pages 1-2).

With only 26-30 cases reported worldwide as of 2025, MED13 Syndrome is extremely rare (yang2025anovelframeshift pages 1-2, yang2025anovelframeshift pages 2-3). The vast majority of cases arise from de novo variants, though rare familial transmission with variable expressivity has been documented (blok2018denovomutations pages 1-2, yang2025anovelframeshift pages 2-3). The pathogenic mechanism likely involves both haploinsufficiency (for truncating variants) and gain-of-dysfunction (for specific missense variants affecting protein stability and interactions) (blok2018denovomutations pages 6-7, blok2018denovomutations pages 7-11).

Currently, no disease-modifying treatments exist, and management is entirely supportive, focusing on intensive speech/language therapy, educational interventions, behavioral therapies, and management of associated medical issues (blok2018denovomutations pages 1-2). Prognosis is generally favorable for survival, though lifelong disability and need for support are expected. Further research using animal models and patient-derived cells is elucidating the molecular mechanisms and may inform future therapeutic development (li2026med13isinvolved pages 1-2, miao2018mediatorcomplexcomponent pages 1-2).

Early genetic diagnosis through whole exome sequencing is crucial for enabling early intervention, appropriate medical surveillance, accurate prognostic counseling, and informed family planning (blok2018denovomutations pages 1-2, yang2025anovelframeshift pages 2-3). As additional cases are identified and reported, genotype-phenotype correlations will be refined, and the full clinical spectrum will be better delineated.

---

## References

All citations refer to context IDs from the gathered evidence:
- pqac-00000001: Blok et al. 2018 - Foundational cohort study
- pqac-00000002, pqac-00000016: Tolmacheva et al. 2024 - Severe neonatal case
- pqac-00000003: Rivera et al. 2024 - ASD case report
- pqac-00000004, pqac-00000017: Yang et al. 2025 - Chinese family
- pqac-00000005: Nardi et al. 2021 - Kabuki-like case
- pqac-00000006, pqac-00000007, pqac-00000008, pqac-00000015: Blok et al. 2018 detailed phenotype/variant data
- pqac-00000009, pqac-00000019: Fazio et al. 2025 - MEDopathies review
- pqac-00000010: Li et al. 2026 - Mouse neurodevelopmental studies
- pqac-00000011: Baskin et al. 2014 - Med13 metabolic functions
- pqac-00000012: Harper & Taatjes 2018 - Mediator structure
- pqac-00000013: Poss et al. 2013 - Mediator complex review
- pqac-00000014: Miao et al. 2018 - Med13 in ZGA
- pqac-00000018: Poot 2019 - Mediator complex disorders

Publication dates range from 2013-2026, with emphasis on recent 2023-2025 sources as requested.

References

1. (blok2018denovomutations pages 1-2): Lot Snijders Blok, Susan M. Hiatt, Kevin M. Bowling, Jeremy W. Prokop, Krysta L. Engel, J. Nicholas Cochran, E. Martina Bebin, Emilia K. Bijlsma, Claudia A. L. Ruivenkamp, Paulien Terhal, Marleen E. H. Simon, Rosemarie Smith, Jane A. Hurst, Heather McLaughlin, Richard Person, Amy Crunk, Michael F. Wangler, Haley Streff, Joseph D. Symonds, Sameer M. Zuberi, Katherine S. Elliott, Victoria R. Sanders, Abigail Masunga, Robert J. Hopkin, Holly A. Dubbs, Xilma R. Ortiz-Gonzalez, Rolph Pfundt, Han G. Brunner, Simon E. Fisher, Tjitske Kleefstra, and Gregory M. Cooper. De novo mutations in med13, a component of the mediator complex, are associated with a novel neurodevelopmental disorder. Human Genetics, 137:375-388, May 2018. URL: https://doi.org/10.1007/s00439-018-1887-y, doi:10.1007/s00439-018-1887-y. This article has 95 citations and is from a peer-reviewed journal.

2. (yang2025anovelframeshift pages 1-2): Qi Yang, Qiang Zhang, Sheng Yi, Gaojie Huang, Xunzhao Zhou, Shang Yi, and Jingsi Luo. A novel frameshift variant in the med13 gene causing intellectual developmental disorder-61 in a chinese family. Frontiers in Pediatrics, Oct 2025. URL: https://doi.org/10.3389/fped.2025.1699544, doi:10.3389/fped.2025.1699544. This article has 1 citations.

3. (yang2025anovelframeshift pages 2-3): Qi Yang, Qiang Zhang, Sheng Yi, Gaojie Huang, Xunzhao Zhou, Shang Yi, and Jingsi Luo. A novel frameshift variant in the med13 gene causing intellectual developmental disorder-61 in a chinese family. Frontiers in Pediatrics, Oct 2025. URL: https://doi.org/10.3389/fped.2025.1699544, doi:10.3389/fped.2025.1699544. This article has 1 citations.

4. (blok2018denovomutations pages 4-5): Lot Snijders Blok, Susan M. Hiatt, Kevin M. Bowling, Jeremy W. Prokop, Krysta L. Engel, J. Nicholas Cochran, E. Martina Bebin, Emilia K. Bijlsma, Claudia A. L. Ruivenkamp, Paulien Terhal, Marleen E. H. Simon, Rosemarie Smith, Jane A. Hurst, Heather McLaughlin, Richard Person, Amy Crunk, Michael F. Wangler, Haley Streff, Joseph D. Symonds, Sameer M. Zuberi, Katherine S. Elliott, Victoria R. Sanders, Abigail Masunga, Robert J. Hopkin, Holly A. Dubbs, Xilma R. Ortiz-Gonzalez, Rolph Pfundt, Han G. Brunner, Simon E. Fisher, Tjitske Kleefstra, and Gregory M. Cooper. De novo mutations in med13, a component of the mediator complex, are associated with a novel neurodevelopmental disorder. Human Genetics, 137:375-388, May 2018. URL: https://doi.org/10.1007/s00439-018-1887-y, doi:10.1007/s00439-018-1887-y. This article has 95 citations and is from a peer-reviewed journal.

5. (harper2018thecomplexstructure pages 1-2): Thomas M. Harper and Dylan J. Taatjes. The complex structure and function of mediator. Journal of Biological Chemistry, 293:13778-13785, Sep 2018. URL: https://doi.org/10.1074/jbc.r117.794438, doi:10.1074/jbc.r117.794438. This article has 120 citations and is from a domain leading peer-reviewed journal.

6. (tolmacheva2024expandingphenotypeof pages 1-2): Ekaterina Tolmacheva, Anna S. Bolshakova, Jekaterina Shubina, Margarita S. Rogacheva, Alexey N. Ekimov, Julia L. Podurovskaya, Artem A. Burov, Denis V. Rebrikov, Vladimir G. Bychenko, Dmitry Yu. Trofimov, and Gennady T. Sukhikh. Expanding phenotype of med13-associated syndrome presenting novel de novo missense variant in a patient with multiple congenital anomalies. BMC Medical Genomics, May 2024. URL: https://doi.org/10.1186/s12920-024-01857-z, doi:10.1186/s12920-024-01857-z. This article has 8 citations and is from a peer-reviewed journal.

7. (rivera2024med13genemutation pages 1-2): Marlene D Rivera, Stephanie N Aponte, Felix Rivera, Norma J Arciniegas, and Simón Carlo. Med13 gene mutation related to autism spectrum disorder: a case report. Cureus, May 2024. URL: https://doi.org/10.7759/cureus.59904, doi:10.7759/cureus.59904. This article has 5 citations.

8. (nardi2021couldthemed13 pages 1-2): Laura De Nardi, Flavio Faletra, Adamo Pio D'Adamo, Anna Monica Rosaria Bianco, Emmanouil Athanasakis, Irene Bruno, and Egidio Barbi. Could the med13 mutations manifest as a kabuki‐like syndrome? American Journal of Medical Genetics Part A, 185:584-590, Nov 2021. URL: https://doi.org/10.1002/ajmg.a.61994, doi:10.1002/ajmg.a.61994. This article has 11 citations.

9. (fazio2025geneticclinicaland pages 1-2): Alessandro Fazio, Roberta Leonardi, Lorenzo Aliotta, Manuela Lo Bianco, Gennaro Anastasio, Giuseppe Messina, Corrado Spatola, Pietro Valerio Foti, Stefano Palmucci, Antonio Basile, Martino Ruggieri, and Emanuele David. Genetic, clinical and neuroradiological spectrum of med-related disorders: an updated review. Genes, 16:1444, Dec 2025. URL: https://doi.org/10.3390/genes16121444, doi:10.3390/genes16121444. This article has 1 citations.

10. (fazio2025geneticclinicaland pages 2-4): Alessandro Fazio, Roberta Leonardi, Lorenzo Aliotta, Manuela Lo Bianco, Gennaro Anastasio, Giuseppe Messina, Corrado Spatola, Pietro Valerio Foti, Stefano Palmucci, Antonio Basile, Martino Ruggieri, and Emanuele David. Genetic, clinical and neuroradiological spectrum of med-related disorders: an updated review. Genes, 16:1444, Dec 2025. URL: https://doi.org/10.3390/genes16121444, doi:10.3390/genes16121444. This article has 1 citations.

11. (poss2013themediatorcomplex pages 2-3): Zachary C. Poss, Christopher C. Ebmeier, and Dylan J. Taatjes. The mediator complex and transcription regulation. Critical Reviews in Biochemistry and Molecular Biology, 48:575-608, Oct 2013. URL: https://doi.org/10.3109/10409238.2013.840259, doi:10.3109/10409238.2013.840259. This article has 481 citations and is from a peer-reviewed journal.

12. (blok2018denovomutations pages 6-7): Lot Snijders Blok, Susan M. Hiatt, Kevin M. Bowling, Jeremy W. Prokop, Krysta L. Engel, J. Nicholas Cochran, E. Martina Bebin, Emilia K. Bijlsma, Claudia A. L. Ruivenkamp, Paulien Terhal, Marleen E. H. Simon, Rosemarie Smith, Jane A. Hurst, Heather McLaughlin, Richard Person, Amy Crunk, Michael F. Wangler, Haley Streff, Joseph D. Symonds, Sameer M. Zuberi, Katherine S. Elliott, Victoria R. Sanders, Abigail Masunga, Robert J. Hopkin, Holly A. Dubbs, Xilma R. Ortiz-Gonzalez, Rolph Pfundt, Han G. Brunner, Simon E. Fisher, Tjitske Kleefstra, and Gregory M. Cooper. De novo mutations in med13, a component of the mediator complex, are associated with a novel neurodevelopmental disorder. Human Genetics, 137:375-388, May 2018. URL: https://doi.org/10.1007/s00439-018-1887-y, doi:10.1007/s00439-018-1887-y. This article has 95 citations and is from a peer-reviewed journal.

13. (blok2018denovomutations pages 7-11): Lot Snijders Blok, Susan M. Hiatt, Kevin M. Bowling, Jeremy W. Prokop, Krysta L. Engel, J. Nicholas Cochran, E. Martina Bebin, Emilia K. Bijlsma, Claudia A. L. Ruivenkamp, Paulien Terhal, Marleen E. H. Simon, Rosemarie Smith, Jane A. Hurst, Heather McLaughlin, Richard Person, Amy Crunk, Michael F. Wangler, Haley Streff, Joseph D. Symonds, Sameer M. Zuberi, Katherine S. Elliott, Victoria R. Sanders, Abigail Masunga, Robert J. Hopkin, Holly A. Dubbs, Xilma R. Ortiz-Gonzalez, Rolph Pfundt, Han G. Brunner, Simon E. Fisher, Tjitske Kleefstra, and Gregory M. Cooper. De novo mutations in med13, a component of the mediator complex, are associated with a novel neurodevelopmental disorder. Human Genetics, 137:375-388, May 2018. URL: https://doi.org/10.1007/s00439-018-1887-y, doi:10.1007/s00439-018-1887-y. This article has 95 citations and is from a peer-reviewed journal.

14. (miao2018mediatorcomplexcomponent pages 1-2): Yi-Liang Miao, Andrés Gambini, Yingpei Zhang, Elizabeth Padilla-Banks, Wendy N Jefferson, Miranda L Bernhardt, Weichun Huang, Leping Li, and Carmen J Williams. Mediator complex component med13 regulates zygotic genome activation and is required for postimplantation development in the mouse†, ‡. Biology of Reproduction, 98:449-464, Apr 2018. URL: https://doi.org/10.1093/biolre/ioy004, doi:10.1093/biolre/ioy004. This article has 51 citations and is from a peer-reviewed journal.

15. (blok2018denovomutations pages 2-4): Lot Snijders Blok, Susan M. Hiatt, Kevin M. Bowling, Jeremy W. Prokop, Krysta L. Engel, J. Nicholas Cochran, E. Martina Bebin, Emilia K. Bijlsma, Claudia A. L. Ruivenkamp, Paulien Terhal, Marleen E. H. Simon, Rosemarie Smith, Jane A. Hurst, Heather McLaughlin, Richard Person, Amy Crunk, Michael F. Wangler, Haley Streff, Joseph D. Symonds, Sameer M. Zuberi, Katherine S. Elliott, Victoria R. Sanders, Abigail Masunga, Robert J. Hopkin, Holly A. Dubbs, Xilma R. Ortiz-Gonzalez, Rolph Pfundt, Han G. Brunner, Simon E. Fisher, Tjitske Kleefstra, and Gregory M. Cooper. De novo mutations in med13, a component of the mediator complex, are associated with a novel neurodevelopmental disorder. Human Genetics, 137:375-388, May 2018. URL: https://doi.org/10.1007/s00439-018-1887-y, doi:10.1007/s00439-018-1887-y. This article has 95 citations and is from a peer-reviewed journal.

16. (blok2018denovomutations pages 5-6): Lot Snijders Blok, Susan M. Hiatt, Kevin M. Bowling, Jeremy W. Prokop, Krysta L. Engel, J. Nicholas Cochran, E. Martina Bebin, Emilia K. Bijlsma, Claudia A. L. Ruivenkamp, Paulien Terhal, Marleen E. H. Simon, Rosemarie Smith, Jane A. Hurst, Heather McLaughlin, Richard Person, Amy Crunk, Michael F. Wangler, Haley Streff, Joseph D. Symonds, Sameer M. Zuberi, Katherine S. Elliott, Victoria R. Sanders, Abigail Masunga, Robert J. Hopkin, Holly A. Dubbs, Xilma R. Ortiz-Gonzalez, Rolph Pfundt, Han G. Brunner, Simon E. Fisher, Tjitske Kleefstra, and Gregory M. Cooper. De novo mutations in med13, a component of the mediator complex, are associated with a novel neurodevelopmental disorder. Human Genetics, 137:375-388, May 2018. URL: https://doi.org/10.1007/s00439-018-1887-y, doi:10.1007/s00439-018-1887-y. This article has 95 citations and is from a peer-reviewed journal.

17. (tolmacheva2024expandingphenotypeof pages 2-5): Ekaterina Tolmacheva, Anna S. Bolshakova, Jekaterina Shubina, Margarita S. Rogacheva, Alexey N. Ekimov, Julia L. Podurovskaya, Artem A. Burov, Denis V. Rebrikov, Vladimir G. Bychenko, Dmitry Yu. Trofimov, and Gennady T. Sukhikh. Expanding phenotype of med13-associated syndrome presenting novel de novo missense variant in a patient with multiple congenital anomalies. BMC Medical Genomics, May 2024. URL: https://doi.org/10.1186/s12920-024-01857-z, doi:10.1186/s12920-024-01857-z. This article has 8 citations and is from a peer-reviewed journal.

18. (li2026med13isinvolved pages 1-2): Ze-Xuan Li, Si-Xin Tu, Yi-Wei Li, Zhi-Bin Hu, Wei-Tang Liu, Yun-Chao Tao, Li Zhao, Ning-Ning Song, Jia-Yin Chen, Qiong Zhang, Cong-Cong Qi, Hong-Wen Zhu, Yu-Qiang Ding, and Ling Hu. Med13 is involved in the radial migration and contralateral projection of cortical neurons via plxna4. Communications Biology, Feb 2026. URL: https://doi.org/10.1038/s42003-026-09704-w, doi:10.1038/s42003-026-09704-w. This article has 0 citations and is from a peer-reviewed journal.

19. (baskin2014med13‐dependentsignalingfrom pages 1-2): Kedryn K Baskin, Chad E Grueter, Christine M Kusminski, William L Holland, Angie L Bookout, Santosh Satapati, Y Megan Kong, Shawn C Burgess, Craig R Malloy, Philipp E Scherer, Christopher B Newgard, Rhonda Bassel‐Duby, and Eric N Olson. <scp>med</scp>13‐dependent signaling from the heart confers leanness by enhancing metabolism in adipose tissue and liver. EMBO Molecular Medicine, 6:1610-1621, Nov 2014. URL: https://doi.org/10.15252/emmm.201404218, doi:10.15252/emmm.201404218. This article has 108 citations and is from a highest quality peer-reviewed journal.

20. (poot2019mutationsinmediator pages 1-1): Martin Poot. Mutations in mediator complex genes cdk8, med12, med13, and medl13 mediate overlapping developmental syndromes. Molecular Syndromology, 10:239-242, Aug 2019. URL: https://doi.org/10.1159/000502346, doi:10.1159/000502346. This article has 23 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](MED13_Syndrome-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](MED13_Syndrome-deep-research-falcon_artifacts/artifact-01.md)