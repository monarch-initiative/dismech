---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-22T12:23:09.613032'
end_time: '2026-06-22T12:44:21.552216'
duration_seconds: 1271.94
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chromosome 18p Deletion Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 7
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: Chromosome_18p_Deletion_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Chromosome_18p_Deletion_Syndrome-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chromosome 18p Deletion Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Chromosome 18p Deletion Syndrome** covering all of the
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
- **Disease Name:** Chromosome 18p Deletion Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Chromosome 18p Deletion Syndrome** covering all of the
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


# Comprehensive Research Report: Chromosome 18p Deletion Syndrome

## 1. Disease Information

### Overview
Chromosome 18p deletion syndrome (also known as monosomy 18p, 18p- syndrome, or 18p deletion syndrome) is a rare chromosomal disorder characterized by partial or complete loss of the short arm of chromosome 18 (papamichail2024prenataldiagnosisof pages 1-3, papamichail2023prenataldiagnosisof pages 1-3, hasi‐zogaj2015areviewof pages 1-2). First described by de Grouchy and colleagues in 1963, it is one of the most frequent autosomal terminal deletion syndromes and was the first reported partial monosomy compatible with life (papamichail2023prenataldiagnosisof pages 1-3, hasi‐zogaj2015areviewof pages 1-2). The syndrome presents with highly variable clinical features including cognitive impairment, minor facial dysmorphism, strabismus, ptosis, short stature, and systemic involvement affecting multiple organ systems (hasi‐zogaj2015areviewof pages 1-2, hasi‐zogaj2015areviewof pages 7-8).

### Key Identifiers
- **OMIM**: #146390 (papamichail2024prenataldiagnosisof pages 1-3, papamichail2023prenataldiagnosisof pages 1-3)
- **Orphanet**: Not explicitly stated in retrieved literature, but the condition is recognized as a rare disease
- **ICD Codes**: Not explicitly provided in retrieved sources
- **MeSH**: Not explicitly provided in retrieved sources
- **MONDO ID**: Not explicitly provided in retrieved sources

### Synonyms and Alternative Names
- Monosomy 18p (papamichail2024prenataldiagnosisof pages 1-3, oktay202518pdeletionsyndrome pages 1-2)
- 18p- syndrome (hasi‐zogaj2015areviewof pages 1-2, hasi‐zogaj2015areviewof pages 2-4)
- 18p deletion syndrome (papamichail2024prenataldiagnosisof pages 1-3, papamichail2023prenataldiagnosisof pages 1-3)
- Chromosome 18p deletion syndrome (papamichail2024prenataldiagnosisof pages 1-3)

### Data Source Type
The information is derived from both individual patient case reports and aggregated disease-level resources, including a comprehensive cohort study of 106 individuals (hasi‐zogaj2015areviewof pages 1-2, hasi‐zogaj2015areviewof pages 2-4).

---

## 2. Etiology

### Disease Causal Factors
Chromosome 18p deletion syndrome is caused by a chromosomal deletion affecting the short arm (p arm) of chromosome 18 (hasi‐zogaj2015areviewof pages 1-2, hasi‐zogaj2015areviewof pages 2-4). The deletion size and breakpoint location vary significantly between individuals, contributing to phenotypic heterogeneity (hasi‐zogaj2015areviewof pages 1-2, hasi‐zogaj2015areviewof pages 2-4). Approximately 42% of cases have breakpoints within the centromeric region, while the remaining breakpoints are scattered along the entirety of the short arm (hasi‐zogaj2015areviewof pages 2-4, hasi‐zogaj2015areviewof pages 4-7). Interestingly, no large interstitial deletions of 18p have been reported, though microdeletions have been documented (hasi‐zogaj2015areviewof pages 2-4).

### Risk Factors

**Genetic Risk Factors:**
The primary genetic risk factor is the presence of a balanced chromosomal translocation in a parent, particularly involving chromosome 18p and an acrocentric chromosome (papamichail2024prenataldiagnosisof pages 1-3, papamichail2023prenataldiagnosisof pages 1-3, hasi‐zogaj2015areviewof pages 11-12). Approximately 89% of cases arise de novo, while ~11% are inherited or result from unbalanced translocations (hasi‐zogaj2015areviewof pages 2-4). Of de novo cases where parental origin can be determined, approximately 50% arise from the maternal chromosome and 50% from the paternal chromosome (hasi‐zogaj2015areviewof pages 2-4). 

**Specific Causal/Modifier Genes (Haploinsufficiency):**
- **TGIF1** (3,451,591-3,458,406 on 18p): Haploinsufficiency causes holoprosencephaly (HPE) and HPE microforms with ~11% penetrance in deletion carriers (hasi‐zogaj2015areviewof pages 4-7, hasi‐zogaj2015areviewof pages 7-8)
- **SMCHD1** (2,655,886-2,805,015): Conditional haploinsufficiency; individuals with 18p deletion plus a permissive D4Z4 allele on chromosome 4q are at risk for facioscapulohumeral muscular dystrophy type 2 (FSHD2) (hasi‐zogaj2015areviewof pages 8-9, balog2018monosomy18pis pages 1-3)
- **GNAL** (11,689,014-11,885,683): Linked to dystonia with low penetrance (~3% in deletion carriers) (hasi‐zogaj2015areviewof pages 7-8)
- **PTPN2** (12,792,301-12,884,334): Associated with autoimmune disease risk including rheumatoid arthritis, thyroiditis, and other autoimmune conditions (hasi‐zogaj2015areviewof pages 8-9, oktay202518pdeletionsyndrome pages 1-2)
- **AFG3L2** (12,328,943-12,377,275): Potential risk for spinocerebellar ataxia type 28 (SCA28), though not yet manifested in young cohorts (hasi‐zogaj2015areviewof pages 8-9, hasi‐zogaj2015areviewof pages 10-11)
- **LAMA1** (6,941,743-7,117,813): Associated with retinal vascular anomalies and possible skin findings (keratosis pilaris/ulerythema ophryogenes) (hasi‐zogaj2015areviewof pages 7-8)

**Environmental/Other Risk Factors:**
No specific environmental risk factors for developing the deletion have been identified. However, TGIF1 heterozygous knockout mice exposed prenatally to retinoic acid show significantly increased risk for facial deformities, holoprosencephaly, and neural tube defects, suggesting potential gene-environment interactions (hasi‐zogaj2015areviewof pages 9-10).

### Protective Factors
No genetic or environmental protective factors have been identified in the literature.

### Gene-Environment Interactions
The TGIF1/TWSG1 genes, when hemizygous, may interact with retinoic acid or other environmental factors during embryonic development to modulate HPE risk, as demonstrated in mouse models (hasi‐zogaj2015areviewof pages 9-10, hasi‐zogaj2015areviewof pages 11-12).

---

## 3. Phenotypes

The clinical phenotype of chromosome 18p deletion syndrome is highly variable, with significant differences even among individuals with identical breakpoints, indicating incomplete penetrance and expressivity for most features (papamichail2023prenataldiagnosisof pages 1-3, hasi‐zogaj2015areviewof pages 1-2). A comprehensive phenotype table is provided below.

| Phenotype | Frequency in centromeric 18p- cohort | Suggested HPO term(s) | Typical onset | Usual severity / course | Notes / evidence |
|---|---:|---|---|---|---|
| Hypotonia / mixed tone abnormalities | 84% | HP:0001252 Hypotonia; HP:0003808 Abnormality of muscle tone | Neonatal–infancy | Mild to moderate; often persistent developmental impact | Common early neurologic feature in centromeric 18p- (hasi‐zogaj2015areviewof pages 7-8) |
| Neonatal complications (jaundice, respiratory distress, feeding difficulties) | 71% | HP:0001945 Respiratory distress; HP:0011968 Feeding difficulties; HP:0002904 Neonatal hypoglycemia/jaundice not specifically resolved | Neonatal | Variable; may require supportive care | Composite category reported in review table (hasi‐zogaj2015areviewof pages 7-8) |
| MRI anomalies (excluding holoprosencephaly spectrum) | 66% | HP:0410263 Abnormal brain MRI; HP:0002538 Abnormal cerebral white matter morphology | Congenital / childhood recognition | Variable; often nonprogressive structural findings | White matter abnormalities and other MRI findings frequently observed (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 9-10) |
| Recurrent otitis media | 61% | HP:0000389 Recurrent otitis media | Infancy–childhood | Recurrent; may contribute to conductive hearing loss | Often associated with chronic middle-ear disease (hasi‐zogaj2015areviewof pages 7-8) |
| Heart defects | 56% | HP:0001627 Abnormality of the cardiovascular system; HP:0001629 Ventricular septal defect; HP:0001636 Tetralogy of Fallot | Congenital | Variable from mild to surgically significant | Structural cardiac defects are common; prenatal VSD also reported (hasi‐zogaj2015areviewof pages 7-8, papamichail2023prenataldiagnosisof pages 1-3) |
| Ptosis | 55% | HP:0000508 Ptosis | Congenital / infancy | Mild to moderate; often persistent | Characteristic craniofacial/ophthalmic feature (hasi‐zogaj2015areviewof pages 7-8) |
| Refractive errors | 52% | HP:0000545 Myopia; HP:0000539 Refractive error | Childhood | Mild to moderate; usually manageable with correction | Broad ophthalmic involvement is frequent (hasi‐zogaj2015areviewof pages 7-8) |
| Strabismus | 42% | HP:0000486 Strabismus | Infancy–childhood | Mild to moderate; may need ophthalmologic management | Common visual alignment abnormality (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 10-11) |
| Pectus excavatum | 29% | HP:0000767 Pectus excavatum | Childhood | Usually mild to moderate; generally stable | Skeletal/chest wall manifestation (hasi‐zogaj2015areviewof pages 7-8) |
| Hearing loss (overall) | 23% | HP:0000365 Hearing impairment; HP:0000405 Conductive hearing impairment; HP:0000407 Sensorineural hearing impairment | Childhood | Usually mild to moderate; conductive more common than sensorineural | Review table reports hearing loss overall 23%; critical-region analysis separated conductive 22% and sensorineural 8% penetrance (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 10-11) |
| Isolated growth hormone deficiency | 23% | HP:0000824 Growth hormone deficiency; HP:0001510 Growth delay | Childhood | Variable; treatable when recognized | Endocrine surveillance recommended in review (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 10-11) |
| Scoliosis / kyphosis | 19% | HP:0002650 Scoliosis; HP:0002808 Kyphosis | Childhood–adolescence | Mild to moderate; occasionally requires bracing/surgery | Combined axial skeletal phenotype (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 10-11) |
| Pes planus | 19% | HP:0001763 Pes planus | Childhood | Usually mild; may affect gait/endurance | Common orthopedic feature (hasi‐zogaj2015areviewof pages 7-8) |
| Cryptorchidism | 14% | HP:0000028 Cryptorchidism | Congenital | Variable; may require orchiopexy | Male genital anomaly; micropenis also described in prenatal case literature (hasi‐zogaj2015areviewof pages 7-8, papamichail2023prenataldiagnosisof pages 1-3) |
| Panhypopituitarism / hypopituitarism | 13% | HP:0000826 Hypopituitarism; HP:0000873 Panhypopituitarism | Congenital / childhood | Potentially severe; chronic hormone replacement often required | Includes structural pituitary anomalies in some patients (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 9-10) |
| Seizures | 13% | HP:0001250 Seizure | Childhood | Variable; often intermittent/managed medically | Included grand mal, absence, and partial complex seizures in review cohort (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 10-11) |
| Immunoglobulin deficiency (IgA, IgG, or IgM deficiency) | 13% | HP:0002721 Immunodeficiency; HP:0002205 Recurrent infections; HP:0011347 Decreased circulating IgA level | Childhood | Variable; may predispose to infections/autoimmunity | IgA deficiency specifically reported in review and later case reports (hasi‐zogaj2015areviewof pages 7-8, oktay202518pdeletionsyndrome pages 1-2) |
| Holoprosencephaly or HPE microform | 13% | HP:0001360 Holoprosencephaly; HP:0000668 Single central incisor | Prenatal / congenital | Severe in classic HPE, milder in microforms | TGIF1 hemizygosity is a major mechanistic candidate; penetrance incomplete (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 4-7) |
| Autoimmune disorder | 10% | HP:0002960 Autoimmunity; HP:0000821 Hypothyroidism; HP:0002725 Systemic lupus erythematosus; HP:0012205 Alopecia | Childhood–adult | Variable; chronic, organ-specific or systemic | Review lists rheumatoid arthritis, celiac disease, alopecia, vitiligo, lupus, Sjögren syndrome, autoimmune thyroid disease (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 9-10, oktay202518pdeletionsyndrome pages 1-2) |
| Sacral agenesis | 6% | HP:0003310 Sacral agenesis | Congenital | Moderate to severe; structural | Rare but recurrent caudal malformation (hasi‐zogaj2015areviewof pages 7-8) |
| Optic nerve hypoplasia | 6% | HP:0008058 Optic nerve hypoplasia | Congenital / infancy | Variable visual impairment | Part of ophthalmologic/neurodevelopmental spectrum (hasi‐zogaj2015areviewof pages 7-8) |
| Congenital cataracts | 6% | HP:0000519 Congenital cataract | Congenital | Variable; may need surgery | Rare but documented ocular feature (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 10-11) |
| Myelomeningocele | 3% | HP:0002414 Myelomeningocele | Congenital | Severe structural defect | Uncommon neural tube defect in reported cohort (hasi‐zogaj2015areviewof pages 7-8) |


*Table: This table summarizes the principal phenotypes reported in the comprehensive Hasi-Zogaj 2015 review of chromosome 18p deletion syndrome, including frequencies, suggested HPO mappings, onset, and usual severity/course. It is useful for knowledge-base phenotype annotation and anticipatory clinical assessment.*

### Quality of Life Impact
Individuals with chromosome 18p deletion syndrome experience significant impacts on quality of life related to:
- **Cognitive Function**: Average full-scale IQ of 69 (range 51-99), typically in the mild to borderline intellectual disability range (hasi‐zogaj2015areviewof pages 2-4)
- **Adaptive Functioning**: The majority of participants have problems with activities of everyday life, including difficulties with communication, home living, self-care, and management of social and leisure activities (hasi‐zogaj2015areviewof pages 2-4)
- **Autism Spectrum Features**: Based on parental report using the Gilliam Autism Rating Scale (GARS), between 19% and 38% of individuals score in the range suggesting autism spectrum disorder (hasi‐zogaj2015areviewof pages 9-10, hasi‐zogaj2015areviewof pages 8-9)
- **Medical Complications**: Chronic medical issues including recurrent otitis media (61%), cardiac anomalies requiring management (56%), endocrine dysfunction (23-13%), and sensory impairments significantly impact daily functioning (hasi‐zogaj2015areviewof pages 7-8)

---

## 4. Genetic/Molecular Information

### Chromosomal Abnormalities
Chromosome 18p deletion syndrome is characterized by partial or complete monosomy of the short arm of chromosome 18 (hasi‐zogaj2015areviewof pages 1-2, hasi‐zogaj2015areviewof pages 2-4). The deletions are predominantly terminal, with breakpoints ranging from the centromere to various positions along the p arm (hasi‐zogaj2015areviewof pages 1-2, hasi‐zogaj2015areviewof pages 2-4, hasi‐zogaj2015areviewof pages 4-7). 

**Deletion Characteristics:**
- Size: Variable, ranging from small microdeletions (<1 Mb) to complete p-arm deletions (~15-17 Mb) (papamichail2024prenataldiagnosisof pages 1-3, oktay202518pdeletionsyndrome pages 1-2)
- Breakpoint distribution: ~42% centromeric, ~58% scattered along 18p (hasi‐zogaj2015areviewof pages 2-4)
- Type: Predominantly terminal deletions; no large interstitial deletions reported (hasi‐zogaj2015areviewof pages 2-4)
- Origin: ~89% de novo, ~11% familial (inherited or translocation-derived) (hasi‐zogaj2015areviewof pages 2-4)
- Parental origin of de novo cases: ~50% maternal, ~50% paternal (hasi‐zogaj2015areviewof pages 2-4)

**Unbalanced Translocations:**
Unbalanced translocations, particularly between 18p and acrocentric chromosomes (13, 15, 21, 22), account for a subset of cases (papamichail2024prenataldiagnosisof pages 1-3, papamichail2023prenataldiagnosisof pages 1-3, hasi‐zogaj2015areviewof pages 11-12). These often arise from parental balanced translocations or pericentric inversions (hasi‐zogaj2015areviewof pages 1-2).

### Pathogenic Variants and Causal Genes
The syndrome results from structural chromosomal abnormalities (deletions, unbalanced translocations) rather than point mutations (hasi‐zogaj2015areviewof pages 1-2). A comprehensive gene dosage map has been established, identifying 12 genes as likely or possibly dosage-sensitive out of 67 total genes on 18p (hasi‐zogaj2015areviewof pages 2-4, hasi‐zogaj2015areviewof pages 10-11). A detailed gene table is provided below.

| Gene | 18p location (hg19, as reported) | Core function | Haploinsufficiency / dosage status in review | Phenotypes linked to hemizygosity or conditional hemizygosity | Inheritance / mechanistic model | Key evidence from Hasi-Zogaj 2015 review |
|---|---|---|---|---|---|---|
| CETN1 | 580,369-581,524 | Centrin family protein involved in centrosome position/segregation and microtubule functions | Not established as pathogenic for a human 18p- phenotype; discussed as a candidate dosage-sensitive gene | No specific confirmed human phenotype from 18p hemizygosity; possible relevance to male fertility considered but unproven | Unclear; no direct phenotype established in 18p-; maternal transmissions including this region argue against female infertility | Review notes mouse heterozygous mutations cause infertility, but human 18p deletions including CETN1 have been maternally transmitted; no firm human dosage phenotype assigned (hasi‐zogaj2015areviewof pages 4-7) |
| TGIF1 | 3,451,591-3,458,406 | Homeodomain transcriptional regulator in TGF-beta/NODAL-related developmental signaling | Likely dosage-sensitive / haploinsufficient | Holoprosencephaly (HPE), HPE microforms, single central incisor, midline/pituitary anomalies | Classic haploinsufficiency with incomplete penetrance; phenotype modified by additional factors | In the review cohort, 11% (6/65) of individuals hemizygous for TGIF1 had HPE-spectrum malformations; TGIF1 point mutations are established in HPE and 18p hemizygosity is a recognized risk factor (hasi‐zogaj2015areviewof pages 4-7, hasi‐zogaj2015areviewof pages 7-8) |
| DLGAP1 | 3,499,183-3,880,068 | Postsynaptic density scaffold protein | Candidate dosage-sensitive / possible risk gene | Autism spectrum disorder / autistic features | Risk-factor model rather than fully penetrant haploinsufficiency | Seven of eight individuals with clinically significant autism scores had deletions including DLGAP1; proposed because of postsynaptic density enrichment (hasi‐zogaj2015areviewof pages 9-10, hasi‐zogaj2015areviewof pages 8-9) |
| TWSG1 | 9,334,765-9,402,418 | BMP-binding extracellular developmental regulator involved in dorsal-ventral patterning and craniofacial development | Conditional / uncertain dosage sensitivity | Possible modifier for HPE; possible contribution to dental/caries phenotype; direct role in 18p HPE not proven | Likely modifier-gene model, potentially interacting with TGIF1 or environmental exposures | Review states evidence for direct involvement in HPE is conflicting; no study participant with isolated TWSG1 hemizygosity had HPE, though prior literature suggested combined deletion with TGIF1 may increase HPE penetrance (hasi‐zogaj2015areviewof pages 9-10, hasi‐zogaj2015areviewof pages 11-12) |
| ANKRD12 | 9,136,751-9,285,983 | Ankyrin repeat domain-containing protein; exact dosage mechanism uncertain | Candidate conditional dosage-sensitive / risk gene | Autism spectrum disorder risk | Risk-factor model | Listed among 18p genes implicated by overlap in individuals with clinically significant autism scores (hasi‐zogaj2015areviewof pages 8-9) |
| LAMA1 | 6,941,743-7,117,813 | Laminin alpha-1, basement membrane component | Likely dosage-sensitive / conditional | Retinal vascular anomalies, keratosis pilaris / ulerythema ophryogenes candidate, possible ocular/cerebellar features | Incomplete penetrance; possible revealed recessive-allele model for severe manifestations | In the cohort, 1/32 with LAMA1 hemizygosity had tortuous anomalous retinal vessels; skin findings were common but nonspecific; review discusses relevance based on known recessive LAMA1 disease and mouse retinal vasculopathy (hasi‐zogaj2015areviewof pages 7-8) |
| LRRC30 | 7,231,137-7,232,042 | Leucine-rich repeat-containing protein; function poorly defined | Candidate conditional dosage-sensitive / risk gene | Autism spectrum disorder risk | Risk-factor model | Included among genes recurrently deleted in individuals with autism-range GARS/GARS-2 scores (hasi‐zogaj2015areviewof pages 8-9) |
| GNAL | 11,689,014-11,885,683 | G-protein alpha-olf subunit involved in receptor signaling | Likely dosage-sensitive / conditional | Dystonia, torsion dystonia, movement disorders | Conditional / incompletely penetrant haploinsufficiency | GNAL is a major adult-onset dystonia gene in the literature; in the 18p- cohort, 2/58 individuals with deletions encompassing GNAL had dystonia, supporting low-penetrance risk from hemizygosity (hasi‐zogaj2015areviewof pages 7-8) |
| IMPA2 | 11,981,427-12,030,885 | Inositol monophosphatase-related function | Candidate conditional dosage-sensitive / risk gene | Autism spectrum disorder risk | Risk-factor model | Seven of eight autism-range cases had deletions including DLGAP1/LRRC30/ANKRD12/IMPA2; one additional case lacked IMPA2, suggesting it may contribute but is not solely causal (hasi‐zogaj2015areviewof pages 9-10, hasi‐zogaj2015areviewof pages 8-9) |
| AFG3L2 | 12,328,943-12,377,275 | Mitochondrial protease subunit involved in protein quality control and ribosome assembly | Conditional dosage-sensitive | Spinocerebellar ataxia type 28 (SCA28)-like risk; possible later-onset ataxia | Conditional haploinsufficiency / age-dependent penetrance | None of 15 examined individuals met diagnostic criteria for SCA28, but point mutations in AFG3L2 cause dominant ataxia and the review highlights possible future age-related manifestation in 18p- adults (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 10-11) |
| PTPN2 | 12,792,301-12,884,334 | Protein tyrosine phosphatase involved in immune regulation | Conditional dosage-sensitive / susceptibility gene | Autoimmune disease risk (juvenile rheumatoid arthritis, thyroid autoimmunity, celiac disease, vitiligo, psoriasis, alopecia, Sjogren syndrome) | Susceptibility / second-hit model | No inflammatory bowel disease was seen in 67 hemizygous individuals, but 11 had autoimmune conditions; the review considers PTPN2 a plausible contributor with incomplete penetrance and likely additional modifiers (hasi‐zogaj2015areviewof pages 8-9) |
| SMCHD1 | 2,655,886-2,805,015 | Structural maintenance of chromosomes hinge domain protein; chromatin repression and methylation including D4Z4 | Conditional dosage-sensitive | Risk for facioscapulohumeral muscular dystrophy type 2 (FSHD2), retinal vasculopathy in susceptible background | Digenic / permissive-background model requiring hemizygosity plus permissive D4Z4 allele and repeat context | Review states SMCHD1 hemizygosity alone is insufficient, but individuals with 18p deletion may be at risk for FSHD when a permissive 4q D4Z4 background is present; this was later directly supported by Balog et al. 2018 (hasi‐zogaj2015areviewof pages 8-9, balog2018monosomy18pis pages 1-3) |
| PTPRM | Not specified in the review pages provided | Receptor-type protein tyrosine phosphatase | Not classified in Hasi-Zogaj 2015 as a key dosage-sensitive gene | No specific phenotype assigned in the review | Unclear | Mentioned in later case literature on 18p autoimmunity, but not among the key mapped dosage-sensitive genes in the Hasi-Zogaj review sections provided (oktay202518pdeletionsyndrome pages 1-2) |
| ADCYAP1 | Not specified in the review pages provided | Pituitary adenylate cyclase-activating polypeptide signaling | Not classified in Hasi-Zogaj 2015 as a key dosage-sensitive gene | No specific phenotype assigned in the review | Unclear | Reported in later case literature as a potentially relevant deleted gene in autoimmune endocrinopathy, but not a mapped key dosage-sensitive gene in the review (oktay202518pdeletionsyndrome pages 1-2) |
| LPIN2 | Not specified in the review pages provided | Lipin-2, lipid metabolism/inflammation-related protein | Not classified in Hasi-Zogaj 2015 as a key dosage-sensitive gene | No specific phenotype assigned in the review | Unclear | Highlighted in a later autoimmune case report, not as a core dosage-sensitive 18p review gene (oktay202518pdeletionsyndrome pages 1-2) |
| USP14 | Not specified in the review pages provided | Deubiquitinating enzyme involved in proteostasis | Not classified in Hasi-Zogaj 2015 as a key dosage-sensitive gene | No specific phenotype assigned in the review | Unclear | Cited in later case literature as a potentially relevant deleted immune-modifying gene, but not part of the core 2015 dosage map summarized here (oktay202518pdeletionsyndrome pages 1-2) |


*Table: This table summarizes the principal chromosome 18p genes discussed as dosage-sensitive, conditionally dosage-sensitive, or candidate risk genes in the Hasi-Zogaj 2015 review, with later context for several immune-related genes. It is useful for linking deletion breakpoints to expected phenotypes and for distinguishing established haploinsufficiency from low-penetrance or modifier effects.*

### Allele Frequency
As a predominantly de novo chromosomal abnormality, there is no meaningful population allele frequency for specific deletion variants.

### Somatic vs. Germline
The deletions are germline events, present in all cells of affected individuals (hasi‐zogaj2015areviewof pages 1-2, hasi‐zogaj2015areviewof pages 2-4).

### Epigenetic Information
**SMCHD1** hemizygosity specifically impacts DNA methylation and chromatin structure. SMCHD1 is responsible for maintaining methylation of the D4Z4 chromatin domain on chromosome 4q; its loss results in hypomethylation similar to FSHD2, potentially leading to inappropriate DUX4 expression when combined with a permissive genetic background (hasi‐zogaj2015areviewof pages 8-9, balog2018monosomy18pis pages 1-3).

---

## 5. Environmental Information

No specific environmental factors (toxins, radiation, pollution, occupational exposures) have been identified as causative or modifying factors for chromosome 18p deletion syndrome. The deletions arise predominantly as sporadic chromosomal rearrangement events during gametogenesis or early embryonic development (hasi‐zogaj2015areviewof pages 1-2, hasi‐zogaj2015areviewof pages 2-4).

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

**TGF-beta/NODAL Signaling (TGIF1):**
TGIF1 encodes a homeodomain protein that functions as a transcriptional regulator in the TGF-beta and NODAL signaling pathways, critical for dorsal-ventral patterning and midline development during embryogenesis (hasi‐zogaj2015areviewof pages 4-7, hasi‐zogaj2015areviewof pages 11-12). Haploinsufficiency leads to holoprosencephaly spectrum disorders with incomplete penetrance (~11%) (hasi‐zogaj2015areviewof pages 4-7). Point mutations in TGIF1 are established causes of HPE, and 18p hemizygosity represents a genomic mechanism for the same phenotype (hasi‐zogaj2015areviewof pages 4-7).
- **Suggested GO terms**: GO:0007389 (pattern specification process), GO:0001942 (hair follicle development), GO:0030509 (BMP signaling pathway)

**Postsynaptic Density Function (DLGAP1, ANKRD12, IMPA2, LRRC30):**
These genes encode proteins enriched in or associated with the postsynaptic density, a specialized structure at excitatory synapses (hasi‐zogaj2015areviewof pages 9-10, hasi‐zogaj2015areviewof pages 8-9). Hemizygosity of these genes, particularly DLGAP1, is associated with increased risk of autism spectrum features, likely through disruption of synaptic signaling and plasticity (hasi‐zogaj2015areviewof pages 9-10, hasi‐zogaj2015areviewof pages 8-9).
- **Suggested GO terms**: GO:0014069 (postsynaptic density), GO:0099151 (regulation of postsynaptic density organization), GO:0099560 (synaptic membrane adhesion)

**G-protein Signaling (GNAL):**
GNAL encodes the α-subunit of the G-protein olfactory receptor (Golf) involved in neuronal signaling (hasi‐zogaj2015areviewof pages 7-8). Point mutations in GNAL are a major cause of adult-onset dystonia, and hemizygosity in 18p deletion carries a low-penetrance risk (~3%) for dystonia (hasi‐zogaj2015areviewof pages 7-8).
- **Suggested GO terms**: GO:0007186 (G-protein coupled receptor signaling pathway), GO:0007268 (chemical synaptic transmission)

**Mitochondrial Protein Quality Control (AFG3L2):**
AFG3L2 encodes a subunit of a mitochondrial protease critical for degrading misfolded proteins and ribosome assembly (hasi‐zogaj2015areviewof pages 8-9, hasi‐zogaj2015areviewof pages 10-11). Point mutations cause spinocerebellar ataxia type 28 (SCA28) with dominant inheritance. Hemizygosity may confer age-dependent risk for ataxia, though this has not yet manifested in relatively young cohorts (hasi‐zogaj2015areviewof pages 8-9, hasi‐zogaj2015areviewof pages 10-11).
- **Suggested GO terms**: GO:0006515 (protein quality control for misfolded or incompletely synthesized proteins), GO:0034983 (peptidyl-lysine deacetylation)

**Immune Regulation (PTPN2):**
PTPN2 encodes a protein tyrosine phosphatase involved in immune regulation. GWAS studies and mouse models link PTPN2 to inflammatory bowel disease, rheumatoid arthritis, and type 1 diabetes (hasi‐zogaj2015areviewof pages 8-9, oktay202518pdeletionsyndrome pages 1-2). In 18p deletion, hemizygosity is associated with autoimmune conditions (~11% penetrance) including thyroid autoimmunity, rheumatoid arthritis, celiac disease, and others, suggesting a susceptibility/second-hit model (hasi‐zogaj2015areviewof pages 8-9, oktay202518pdeletionsyndrome pages 1-2).
- **Suggested GO terms**: GO:0002376 (immune system process), GO:0050776 (regulation of immune response), GO:0002250 (adaptive immune response)

**Chromatin Methylation and FSHD2 (SMCHD1):**
SMCHD1 is a chromatin modifier responsible for maintaining heavy methylation of the D4Z4 macrosatellite repeat on chromosome 4q35, thereby repressing the DUX4 retrogene (hasi‐zogaj2015areviewof pages 8-9, balog2018monosomy18pis pages 1-3). In FSHD2, digenic inheritance of SMCHD1 haploinsufficiency (from 18p deletion or point mutation) plus a moderately sized, permissive D4Z4 allele leads to chromatin relaxation, DUX4 derepression, and muscle degeneration (hasi‐zogaj2015areviewof pages 8-9, balog2018monosomy18pis pages 1-3). Approximately 12% of Caucasians harbor a permissive genetic background, placing individuals with 18p deletion at conditional risk (balog2018monosomy18pis pages 1-3).
- **Suggested GO terms**: GO:0006325 (chromatin organization), GO:0006346 (DNA methylation-dependent heterochromatin formation)

**Basement Membrane Integrity (LAMA1):**
LAMA1 encodes laminin alpha-1, a basement membrane protein expressed in renal cortex, testis, and retina (hasi‐zogaj2015areviewof pages 7-8). In mice, LAMA1 mutations cause retinal vasculopathy with vessel tortuosity. Recessive LAMA1 mutations in humans cause Poretti-Bolshauser syndrome (cerebellar anomalies, retinal dystrophy). Hemizygosity in 18p deletion may contribute to retinal vascular anomalies (~3% documented) and potentially skin findings (keratosis pilaris) (hasi‐zogaj2015areviewof pages 7-8).
- **Suggested GO terms**: GO:0005604 (basement membrane), GO:0001570 (vasculogenesis)

### Cellular Processes
- **Neurodevelopmental patterning defects**: TGIF1 and TWSG1 haploinsufficiency during embryogenesis (hasi‐zogaj2015areviewof pages 4-7, hasi‐zogaj2015areviewof pages 9-10)
- **Synaptic dysfunction**: Postsynaptic density protein deficiency (hasi‐zogaj2015areviewof pages 9-10, hasi‐zogaj2015areviewof pages 8-9)
- **Mitochondrial stress and proteostasis**: AFG3L2 haploinsufficiency (hasi‐zogaj2015areviewof pages 8-9, hasi‐zogaj2015areviewof pages 10-11)
- **Immune dysregulation**: PTPN2 haploinsufficiency (hasi‐zogaj2015areviewof pages 8-9, oktay202518pdeletionsyndrome pages 1-2)

### Tissue Damage Mechanisms
Chronic otitis media leading to conductive hearing loss involves middle ear mucosal dysfunction, possibly related to TGIF1 or other gene hemizygosity affecting epithelial integrity (hasi‐zogaj2015areviewof pages 7-8).

---

## 7. Anatomical Structures Affected

### Organ Level

**Primary Organs Directly Affected:**
- **Brain**: 66% of individuals have MRI anomalies including white matter abnormalities, holoprosencephaly spectrum (13%), pituitary anomalies (13%), and structural changes (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 9-10)
  - **UBERON terms**: UBERON:0000955 (brain), UBERON:0002037 (cerebellum), UBERON:0000007 (pituitary gland)
- **Heart**: 56% have cardiac defects including ventricular septal defects, tetralogy of Fallot, and other structural anomalies (hasi‐zogaj2015areviewof pages 7-8)
  - **UBERON term**: UBERON:0000948 (heart)
- **Eyes**: 52-55% have ophthalmologic findings including ptosis, strabismus, refractive errors, and rare retinal vascular anomalies (hasi‐zogaj2015areviewof pages 7-8)
  - **UBERON term**: UBERON:0000970 (eye)
- **Endocrine System**: 23% isolated growth hormone deficiency, 13% panhypopituitarism/hypopituitarism (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 9-10)
  - **UBERON term**: UBERON:0000949 (endocrine system)
- **Immune System**: 13% immunoglobulin deficiency, 10% autoimmune disorders (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 9-10, oktay202518pdeletionsyndrome pages 1-2)
  - **UBERON term**: UBERON:0002405 (immune system)
- **Ears**: 61% recurrent otitis media, 23% hearing loss (hasi‐zogaj2015areviewof pages 7-8)
  - **UBERON term**: UBERON:0001690 (ear)

**Secondary Organ Involvement:**
- **Musculoskeletal**: Hypotonia (84%), scoliosis/kyphosis (19%), pectus excavatum (29%), pes planus (19%) (hasi‐zogaj2015areviewof pages 7-8)
  - **UBERON term**: UBERON:0002204 (musculoskeletal system)

### Tissue and Cell Level
Specific cell populations targeted include:
- **Neurons and postsynaptic structures** (autism risk associated with synaptic gene haploinsufficiency) (hasi‐zogaj2015areviewof pages 9-10, hasi‐zogaj2015areviewof pages 8-9)
  - **Cell Ontology term**: CL:0000540 (neuron)
- **Pituitary somatotrophs and other endocrine cells** (growth hormone deficiency) (hasi‐zogaj2015areviewof pages 7-8)
  - **Cell Ontology term**: CL:0000441 (somatotroph)
- **Immune cells (B-cells and T-cells)** (immunoglobulin deficiency, autoimmunity) (hasi‐zogaj2015areviewof pages 7-8, oktay202518pdeletionsyndrome pages 1-2)
  - **Cell Ontology terms**: CL:0000236 (B cell), CL:0000084 (T cell)

### Subcellular Level
- **Postsynaptic density** (DLGAP1 function) (hasi‐zogaj2015areviewof pages 9-10)
  - **GO Cellular Component term**: GO:0014069 (postsynaptic density)
- **Mitochondria** (AFG3L2 protease function) (hasi‐zogaj2015areviewof pages 8-9, hasi‐zogaj2015areviewof pages 10-11)
  - **GO Cellular Component term**: GO:0005739 (mitochondrion)
- **Chromatin/nucleus** (SMCHD1 methylation function) (hasi‐zogaj2015areviewof pages 8-9)
  - **GO Cellular Component term**: GO:0000785 (chromatin)

---

## 8. Temporal Development

### Onset
- **Typical Age of Onset**: Congenital for structural anomalies (holoprosencephaly, cardiac defects, dysmorphic features); neonatal for hypotonia and feeding difficulties; childhood for developmental delay recognition and medical complications; potentially adult-onset for dystonia, FSHD2, and some autoimmune features (hasi‐zogaj2015areviewof pages 1-2, hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 2-4)
- **Onset Pattern**: Predominantly congenital with chronic/progressive manifestations through childhood and adulthood (hasi‐zogaj2015areviewof pages 1-2, hasi‐zogaj2015areviewof pages 2-4)

### Progression
- **Disease Stages**: No formal staging system; clinical presentation evolves from congenital structural defects through developmental delays in childhood to potential adult complications (hasi‐zogaj2015areviewof pages 1-2, hasi‐zogaj2015areviewof pages 2-4)
- **Progression Rate**: Variable; cognitive impairment is relatively stable (average IQ 69), while medical complications can accumulate over time (hasi‐zogaj2015areviewof pages 2-4)
- **Disease Course Pattern**: Chronic, lifelong condition with stable cognitive baseline and variable medical complications (hasi‐zogaj2015areviewof pages 1-2, hasi‐zogaj2015areviewof pages 2-4)
- **Disease Duration**: Lifelong (hasi‐zogaj2015areviewof pages 1-2, hasi‐zogaj2015areviewof pages 2-4)

### Patterns
- **Remission Patterns**: Not applicable; this is a chromosomal condition without remission (hasi‐zogaj2015areviewof pages 1-2)
- **Critical Periods**: Embryonic development (for structural malformations related to TGIF1/TWSG1), early childhood (for developmental intervention), adolescence/adulthood (for monitoring dystonia, FSHD2, autoimmune disease risk) (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 4-7, hasi‐zogaj2015areviewof pages 8-9)

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence**: Approximately 1 in 50,000 live births (papamichail2024prenataldiagnosisof pages 1-3, papamichail2023prenataldiagnosisof pages 1-3)
- **Incidence**: Not separately reported; presumed similar to prevalence given lifelong nature
- **Sex Ratio**: Female to male ratio of 3:2 (papamichail2024prenataldiagnosisof pages 1-3, papamichail2023prenataldiagnosisof pages 1-3)

### Genetic Etiology and Inheritance
- **Inheritance Pattern**: Predominantly de novo (~89% of cases); ~11% familial, arising from unbalanced segregation of parental balanced translocations or direct parent-to-child transmission (hasi‐zogaj2015areviewof pages 2-4, hasi‐zogaj2015areviewof pages 11-12)
- **Penetrance**: 
  - Complete penetrance for the chromosomal abnormality itself
  - Incomplete penetrance for specific phenotypes: TGIF1 → HPE (11%), GNAL → dystonia (3%), SMCHD1 → FSHD2 (conditional on 4q background), PTPN2 → autoimmunity (~11-17%) (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 4-7, hasi‐zogaj2015areviewof pages 9-10, hasi‐zogaj2015areviewof pages 8-9)
- **Expressivity**: Highly variable even with identical breakpoints, indicating modifier genes and environmental factors influence phenotype (papamichail2023prenataldiagnosisof pages 1-3, hasi‐zogaj2015areviewof pages 1-2)
- **Genetic Anticipation**: Not documented (no trinucleotide repeat mechanism)
- **Germline Mosaicism**: Not specifically reported in retrieved literature
- **Founder Effects**: Not reported; no population-specific variants identified
- **Consanguinity Role**: Not relevant for de novo deletions; may unmask recessive alleles in deleted regions (theoretical)
- **Carrier Frequency**: Not applicable for de novo events; parental balanced translocation carriers exist but specific frequency not documented

### Population Demographics
- **Affected Populations**: No specific ethnic or demographic groups with higher prevalence reported; cases described across multiple populations (papamichail2024prenataldiagnosisof pages 1-3, papamichail2023prenataldiagnosisof pages 1-3, hasi‐zogaj2015areviewof pages 1-2)
- **Geographic Distribution**: Worldwide distribution; no endemic areas identified (hasi‐zogaj2015areviewof pages 1-2)
- **Age Distribution**: Congenital condition with lifelong manifestations; cohorts studied range from neonates to adults (hasi‐zogaj2015areviewof pages 1-2, hasi‐zogaj2015areviewof pages 2-4)

---

## 10. Diagnostics

### Genetic Testing

**Recommended Genetic Testing Approach:**
Chromosomal microarray analysis (CMA) / array-based comparative genomic hybridization (array-CGH) is the primary diagnostic method, providing sensitive detection of deletions and precise breakpoint mapping (papamichail2024prenataldiagnosisof pages 1-3, papamichail2023prenataldiagnosisof pages 1-3, hasi‐zogaj2015areviewof pages 2-4). CMA can detect submicroscopic deletions missed by conventional karyotyping and is considered first-tier testing for developmental delay/intellectual disability (papamichail2024prenataldiagnosisof pages 1-3, hasi‐zogaj2015areviewof pages 2-4).

**Specific Methods:**
- **Chromosomal Microarray (CMA)**: Detects deletions, defines breakpoints, and identifies size of deleted region; current technology uses 400K-750K oligonucleotide platforms (papamichail2024prenataldiagnosisof pages 1-3, hasi‐zogaj2015areviewof pages 2-4)
- **Karyotyping**: Useful for identifying gross deletions and, critically, for detecting balanced translocations in parents (papamichail2024prenataldiagnosisof pages 1-3, hasi‐zogaj2015areviewof pages 11-12). Parental testing is recommended, especially if there is a family history of cognitive impairment, congenital anomalies, or recurrent pregnancy loss (hasi‐zogaj2015areviewof pages 11-12)
- **FISH (Fluorescence In Situ Hybridization)**: Can confirm specific deletions but is targeted rather than genome-wide (papamichail2024prenataldiagnosisof pages 1-3)
- **Prenatal Testing**: CMA can be performed on chorionic villus sampling (CVS) or amniocentesis samples; however, prenatal phenotype prediction is challenging due to variable expressivity (papamichail2024prenataldiagnosisof pages 1-3, papamichail2023prenataldiagnosisof pages 1-3)

### Clinical Tests

**Laboratory Tests:**
- **Immunoglobulin levels** (IgA, IgG, IgM): To detect immunodeficiency (13% affected) (hasi‐zogaj2015areviewof pages 7-8)
- **Endocrine evaluation**: Growth hormone stimulation testing, thyroid function tests, complete pituitary hormone panel for individuals with growth failure or pituitary structural anomalies (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 9-10)
- **Autoimmune markers**: Anti-thyroid antibodies, rheumatoid factor, celiac antibodies as clinically indicated (oktay202518pdeletionsyndrome pages 1-2)

**Imaging Studies:**
- **Brain MRI**: Recommended to evaluate for white matter anomalies, holoprosencephaly, pituitary abnormalities (66% have abnormal findings) (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 9-10)
- **Echocardiography**: To screen for cardiac defects (56% affected) (hasi‐zogaj2015areviewof pages 7-8)
- **Ophthalmologic examination**: For ptosis, strabismus, refractive errors, and rare retinal anomalies (hasi‐zogaj2015areviewof pages 7-8)

**Functional Tests:**
- **Audiology**: Audiometry to assess for hearing loss (23% overall; conductive more common than sensorineural) (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 10-11)
- **Developmental/Neuropsychological Assessment**: Cognitive testing (average IQ 69, range 51-99), adaptive behavior assessment (hasi‐zogaj2015areviewof pages 2-4)

### Clinical Criteria and Differential Diagnosis
There are no standardized clinical diagnostic criteria; diagnosis is confirmed by genetic testing. Differential diagnosis includes other microdeletion syndromes and isolated features such as holoprosencephaly from other causes, isolated growth hormone deficiency, and syndromic intellectual disability (hasi‐zogaj2015areviewof pages 1-2, hasi‐zogaj2015areviewof pages 11-12).

### Screening
- **Newborn Screening**: Not part of routine newborn screening panels
- **Prenatal Screening**: May be detected incidentally on prenatal CMA performed for other indications; non-invasive prenatal testing (NIPT) may detect large deletions but is not a primary screening tool for 18p deletion (papamichail2024prenataldiagnosisof pages 1-3, papamichail2023prenataldiagnosisof pages 1-3)
- **Carrier Screening**: Relevant for families with balanced translocations; preimplantation genetic diagnosis theoretically possible (hasi‐zogaj2015areviewof pages 11-12)

---

## 11. Outcome/Prognosis

### Survival and Mortality
- **Life Expectancy**: Compatible with survival into adulthood; the condition was historically described as the "first reported partial monosomy compatible with life" (papamichail2023prenataldiagnosisof pages 1-3, hasi‐zogaj2015areviewof pages 1-2). Specific mortality data not provided in retrieved literature, but the syndrome is not considered lethal.
- **Mortality Rate**: Not specifically documented; chronic condition with lifelong management needs

### Morbidity and Function
- **Cognitive Function**: Average full-scale IQ of 69 (range 51-99), typically falling in the mild to borderline intellectual disability range (hasi‐zogaj2015areviewof pages 2-4)
- **Adaptive Functioning**: Majority have problems with activities of daily living including communication, home living, self-care, and social/leisure activities (hasi‐zogaj2015areviewof pages 2-4)
- **Autism Risk**: 19-38% score in the clinically significant range on autism rating scales (hasi‐zogaj2015areviewof pages 9-10, hasi‐zogaj2015areviewof pages 8-9)
- **Medical Morbidity**: Chronic medical complications including recurrent infections (otitis media 61%), cardiac disease (56%), endocrine dysfunction (23-13%), sensory impairments, and potential adult-onset conditions (FSHD2, autoimmunity, dystonia) (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 8-9, balog2018monosomy18pis pages 1-3)

### Quality of Life
Problems with communication, self-care, home living, and social functioning significantly impact quality of life (hasi‐zogaj2015areviewof pages 2-4). Educational and vocational support needs are substantial for most individuals.

### Disease Course and Complications
**Common Complications:**
- Recurrent infections due to immunodeficiency (hasi‐zogaj2015areviewof pages 7-8)
- Cardiac complications requiring surgical intervention (hasi‐zogaj2015areviewof pages 7-8)
- Chronic otitis media leading to conductive hearing loss (hasi‐zogaj2015areviewof pages 7-8)
- Endocrine deficiencies requiring hormone replacement (hasi‐zogaj2015areviewof pages 7-8)
- Scoliosis/kyphosis potentially requiring bracing or surgery (hasi‐zogaj2015areviewof pages 10-11)
- Adult-onset: dystonia, FSHD2 (if permissive background), autoimmune disease (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 8-9, balog2018monosomy18pis pages 1-3)

**Recovery Potential:**
The chromosomal abnormality is permanent; symptomatic treatments can improve function (e.g., growth hormone therapy for GH deficiency, cardiac surgery, hearing aids), but the underlying genetic condition persists (hasi‐zogaj2015areviewof pages 7-8).

### Prognostic Factors
- Deletion size and specific genes involved (genotype-phenotype correlations) (hasi‐zogaj2015areviewof pages 2-4, hasi‐zogaj2015areviewof pages 11-12)
- Early intervention and multidisciplinary management (hasi‐zogaj2015areviewof pages 11-12)
- Presence of SMCHD1 deletion plus permissive 4q background (FSHD2 risk) (balog2018monosomy18pis pages 1-3)

---

## 12. Treatment

### Pharmacotherapy
**Supportive Medications:**
- **Growth hormone therapy**: For isolated growth hormone deficiency; individuals respond to treatment (hasi‐zogaj2015areviewof pages 7-8)
- **Thyroid hormone replacement**: For hypothyroidism/hypopituitarism (hasi‐zogaj2015areviewof pages 7-8, oktay202518pdeletionsyndrome pages 1-2)
- **Immunoglobulin replacement**: For significant immunoglobulin deficiency (hasi‐zogaj2015areviewof pages 7-8)
- **Antiepileptic drugs**: For seizure management (13% affected) (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 10-11)
- **Immunosuppressive/disease-modifying agents**: For autoimmune diseases as clinically indicated (oktay202518pdeletionsyndrome pages 1-2)

**Pharmacogenomics:**
No specific pharmacogenomic considerations documented in retrieved literature.

### Advanced Therapeutics
No gene therapy, cell therapy, RNA-based therapies, or targeted molecular therapies are currently available or under investigation for chromosome 18p deletion syndrome.

### Surgical and Interventional
- **Cardiac surgery**: For structural heart defects (e.g., VSD repair, tetralogy of Fallot correction) (hasi‐zogaj2015areviewof pages 7-8)
- **Orthopedic interventions**: Bracing or surgical correction for scoliosis/kyphosis (hasi‐zogaj2015areviewof pages 10-11)
- **Ophthalmologic surgery**: For strabismus, cataracts as needed (hasi‐zogaj2015areviewof pages 7-8)
- **Ear tube placement**: For chronic otitis media (hasi‐zogaj2015areviewof pages 7-8)

### Supportive and Rehabilitative
- **Early intervention services**: Physical therapy, occupational therapy, speech therapy (hasi‐zogaj2015areviewof pages 11-12)
- **Developmental therapies**: To optimize cognitive and adaptive functioning (hasi‐zogaj2015areviewof pages 2-4, hasi‐zogaj2015areviewof pages 11-12)
- **Educational support**: Special education services, individualized education plans (hasi‐zogaj2015areviewof pages 2-4)
- **Audiologic/ophthalmologic management**: Hearing aids, glasses, ongoing monitoring (hasi‐zogaj2015areviewof pages 7-8)
- **Nutritional support**: For feeding difficulties in infancy (hasi‐zogaj2015areviewof pages 7-8)

### Treatment Strategy and Algorithms
**Recommended Anticipatory Guidance (from Hasi-Zogaj 2015):**
- **At diagnosis**:
  - Chromosomal microarray to define deletion breakpoints (hasi‐zogaj2015areviewof pages 11-12)
  - Parental karyotype to rule out balanced translocation (hasi‐zogaj2015areviewof pages 11-12)
  - Echocardiography to rule out cardiac defects (hasi‐zogaj2015areviewof pages 11-12)
  - Brain MRI to evaluate structural anomalies (hasi‐zogaj2015areviewof pages 11-12)
  - Pituitary function monitoring (growth, endocrine axes) (hasi‐zogaj2015areviewof pages 11-12)
  - Ophthalmology and audiology evaluations (hasi‐zogaj2015areviewof pages 11-12)
  - Immunoglobulin levels (hasi‐zogaj2015areviewof pages 11-12)
  - Referral to early intervention services (hasi‐zogaj2015areviewof pages 11-12)
- **Ongoing surveillance**:
  - Endocrine monitoring (especially for growth hormone deficiency and thyroid function)
  - Regular ophthalmology/audiology follow-up
  - Monitoring for autoimmune disease manifestations
  - For individuals with SMCHD1 deletion: genetic testing for 4q D4Z4 permissive background and clinical monitoring for FSHD2 (balog2018monosomy18pis pages 1-3)

**MAXO (Medical Action Ontology) Terms (suggested):**
- MAXO:0000004 (hormone replacement therapy)
- MAXO:0000058 (developmental therapy)
- MAXO:0000011 (surgical procedure)
- MAXO:0001175 (rehabilitation therapy)

---

## 13. Prevention

### Primary Prevention
- **Genetic counseling**: For families with known balanced translocations; recurrence risk depends on the specific translocation (hasi‐zogaj2015areviewof pages 11-12)
- **Preimplantation genetic diagnosis (PGD)**: Theoretically possible for known familial rearrangements, though not specifically documented in retrieved literature

### Secondary Prevention
- **Prenatal diagnosis**: CMA on CVS or amniocentesis can detect 18p deletions, though prenatal phenotype prediction is challenging due to variable expressivity (papamichail2024prenataldiagnosisof pages 1-3, papamichail2023prenataldiagnosisof pages 1-3)
- **Early multisystem screening**: At diagnosis to identify cardiac, endocrine, ophthalmologic, audiologic, and immunologic issues for early intervention (hasi‐zogaj2015areviewof pages 11-12)

### Tertiary Prevention
- **Treatment of complications**: Growth hormone therapy, cardiac surgery, management of infections, seizure control, autoimmune disease treatment (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 11-12)
- **Surveillance for late-onset features**: Monitoring for dystonia, FSHD2, autoimmune disease in at-risk individuals (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 8-9, balog2018monosomy18pis pages 1-3)

### Screening Programs
- **Newborn screening**: Not part of routine newborn screening
- **Cascade screening**: Not applicable (predominantly de novo condition)

---

## 14. Other Species / Natural Disease

### Natural Disease in Other Species
No naturally occurring chromosome 18p deletion syndrome has been described in other species in the retrieved literature.

---

## 15. Model Organisms

### Gene-Specific Mouse Models
While no comprehensive mouse model of chromosome 18p deletion syndrome exists in the retrieved literature, several individual gene knockout/knockdown models have been studied:

**TGIF1 Knockout Mice:**
Heterozygous TGIF1 knockout mice exposed prenatally to retinoic acid show significantly increased risk for facial deformities (30%), holoprosencephaly (23%), and neural tube defects (7%), recapitulating the HPE phenotype seen in human 18p deletion (hasi‐zogaj2015areviewof pages 9-10).

**CETN1 Heterozygous Mice:**
Male mice with heterozygous CETN1 mutations are infertile, though this phenotype has not been confirmed in humans with 18p deletion (maternal transmission documented) (hasi‐zogaj2015areviewof pages 4-7).

**AFG3L2 Models:**
Deletions and duplications of AFG3L2 in mice are associated with ataxia phenotypes, though point mutations are more penetrant than copy number changes (hasi‐zogaj2015areviewof pages 8-9, hasi‐zogaj2015areviewof pages 10-11).

**LAMA1 Mutant Mice:**
Chemically induced mutations in LAMA1 result in retinal vasculopathy characterized by vitreous fibroplasia and vessel tortuosity (hasi‐zogaj2015areviewof pages 7-8).

**TWSG1 Knockout Mice:**
Knockout mice show defects in craniofacial and dorsal-ventral patterning during embryonic development; prenatal retinoic acid exposure increases risk of malformations (hasi‐zogaj2015areviewof pages 9-10).

### Model Applications
These gene-specific models are useful for understanding individual gene functions and testing potential therapeutic interventions, but do not fully recapitulate the complex multi-gene haploinsufficiency of human 18p deletion syndrome.

---

## Summary and Conclusions

Chromosome 18p deletion syndrome (OMIM #146390) is a rare chromosomal disorder with an estimated prevalence of 1 in 50,000 live births, characterized by partial or complete monosomy of the short arm of chromosome 18 (papamichail2024prenataldiagnosisof pages 1-3, papamichail2023prenataldiagnosisof pages 1-3, hasi‐zogaj2015areviewof pages 1-2). The syndrome presents with highly variable clinical features including cognitive impairment (average IQ 69), minor dysmorphic features, hypotonia (84%), cardiac defects (56%), brain MRI anomalies (66%), and multisystem involvement (hasi‐zogaj2015areviewof pages 1-2, hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 2-4).

Approximately 89% of cases arise de novo, while ~11% are familial, often resulting from unbalanced translocations (hasi‐zogaj2015areviewof pages 2-4). Breakpoint location varies, with ~42% occurring in the centromeric region and the remainder scattered along the p arm, contributing to phenotypic heterogeneity (hasi‐zogaj2015areviewof pages 2-4). Current understanding identifies 12 dosage-sensitive genes out of 67 on 18p, with variable penetrance for specific phenotypes: TGIF1 (holoprosencephaly 11%), SMCHD1 (conditional FSHD2 risk), GNAL (dystonia 3%), PTPN2 (autoimmunity ~11%), and others (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 2-4, hasi‐zogaj2015areviewof pages 4-7, hasi‐zogaj2015areviewof pages 8-9).

Diagnosis relies on chromosomal microarray analysis for deletion detection and breakpoint mapping (papamichail2024prenataldiagnosisof pages 1-3, hasi‐zogaj2015areviewof pages 2-4). Parental karyotyping is recommended to identify balanced translocations (hasi‐zogaj2015areviewof pages 11-12). Management is primarily supportive and multidisciplinary, including early intervention, growth hormone therapy for GH deficiency, cardiac surgery for structural defects, and surveillance for late-onset complications (autoimmunity, dystonia, FSHD2) (hasi‐zogaj2015areviewof pages 7-8, hasi‐zogaj2015areviewof pages 11-12). Prognosis is compatible with survival into adulthood, though significant impacts on quality of life stem from cognitive impairment, medical comorbidities, and adaptive functioning challenges (hasi‐zogaj2015areviewof pages 2-4).

This comprehensive report synthesizes current evidence from primary literature to provide a foundation for disease knowledge base entry, clinical management, and future research into genotype-phenotype correlations and potential therapeutic targets.

References

1. (papamichail2024prenataldiagnosisof pages 1-3): Maria Papamichail, Anna Eleftheriades, Emmanouil Manolakos, Adamantia Papamichail, Panagiotis Christopoulos, Gwendolin Manegold-Brauer, and Makarios Eleftheriades. Prenatal diagnosis of 18p deletion and 8p trisomy syndrome: literature review and report of a novel case. BMC Women's Health, Apr 2024. URL: https://doi.org/10.1186/s12905-024-03081-4, doi:10.1186/s12905-024-03081-4. This article has 1 citations.

2. (papamichail2023prenataldiagnosisof pages 1-3): Maria Papamichail, Anna Eleftheriades, Emmanouil Manolakos, Adamantia Papamichail, Panagiotis Christopoulos, Gwendolin Manegold-Brauer, and Makarios Eleftheriades. Prenatal diagnosis of 18p deletion and 8p trisomy syndrome: case report and review of literature. Unknown journal, Nov 2023. URL: https://doi.org/10.21203/rs.3.rs-3405499/v1, doi:10.21203/rs.3.rs-3405499/v1.

3. (hasi‐zogaj2015areviewof pages 1-2): Minire Hasi‐Zogaj, Courtney Sebold, Patricia Heard, Erika Carter, Bridgette Soileau, Annice Hill, David Rupert, Brian Perry, Sidney Atkinson, Louise O'Donnell, Jon Gelfond, Jack Lancaster, Peter T. Fox, Daniel E. Hale, and Jannine D. Cody. A review of 18p deletions. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 169:251-264, Sep 2015. URL: https://doi.org/10.1002/ajmg.c.31445, doi:10.1002/ajmg.c.31445. This article has 93 citations.

4. (hasi‐zogaj2015areviewof pages 7-8): Minire Hasi‐Zogaj, Courtney Sebold, Patricia Heard, Erika Carter, Bridgette Soileau, Annice Hill, David Rupert, Brian Perry, Sidney Atkinson, Louise O'Donnell, Jon Gelfond, Jack Lancaster, Peter T. Fox, Daniel E. Hale, and Jannine D. Cody. A review of 18p deletions. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 169:251-264, Sep 2015. URL: https://doi.org/10.1002/ajmg.c.31445, doi:10.1002/ajmg.c.31445. This article has 93 citations.

5. (oktay202518pdeletionsyndrome pages 1-2): Mehmet Ali Oktay, Elif Tuğçe Tunca Küçükali, Aylin Kılınç Uğurlu, Esra Döğer, Gülsüm Kayhan, Mahmut Orhun Çamurdan, and Aysun Bideci. 18p deletion syndrome associated with type 1 diabetes and hashimoto’s thyroiditis: a case report on autoimmune disorders and genetic factors. Journal of Clinical Research in Pediatric Endocrinology, Nov 2025. URL: https://doi.org/10.4274/jcrpe.galenos.2025.2025-6-5, doi:10.4274/jcrpe.galenos.2025.2025-6-5. This article has 1 citations.

6. (hasi‐zogaj2015areviewof pages 2-4): Minire Hasi‐Zogaj, Courtney Sebold, Patricia Heard, Erika Carter, Bridgette Soileau, Annice Hill, David Rupert, Brian Perry, Sidney Atkinson, Louise O'Donnell, Jon Gelfond, Jack Lancaster, Peter T. Fox, Daniel E. Hale, and Jannine D. Cody. A review of 18p deletions. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 169:251-264, Sep 2015. URL: https://doi.org/10.1002/ajmg.c.31445, doi:10.1002/ajmg.c.31445. This article has 93 citations.

7. (hasi‐zogaj2015areviewof pages 4-7): Minire Hasi‐Zogaj, Courtney Sebold, Patricia Heard, Erika Carter, Bridgette Soileau, Annice Hill, David Rupert, Brian Perry, Sidney Atkinson, Louise O'Donnell, Jon Gelfond, Jack Lancaster, Peter T. Fox, Daniel E. Hale, and Jannine D. Cody. A review of 18p deletions. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 169:251-264, Sep 2015. URL: https://doi.org/10.1002/ajmg.c.31445, doi:10.1002/ajmg.c.31445. This article has 93 citations.

8. (hasi‐zogaj2015areviewof pages 11-12): Minire Hasi‐Zogaj, Courtney Sebold, Patricia Heard, Erika Carter, Bridgette Soileau, Annice Hill, David Rupert, Brian Perry, Sidney Atkinson, Louise O'Donnell, Jon Gelfond, Jack Lancaster, Peter T. Fox, Daniel E. Hale, and Jannine D. Cody. A review of 18p deletions. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 169:251-264, Sep 2015. URL: https://doi.org/10.1002/ajmg.c.31445, doi:10.1002/ajmg.c.31445. This article has 93 citations.

9. (hasi‐zogaj2015areviewof pages 8-9): Minire Hasi‐Zogaj, Courtney Sebold, Patricia Heard, Erika Carter, Bridgette Soileau, Annice Hill, David Rupert, Brian Perry, Sidney Atkinson, Louise O'Donnell, Jon Gelfond, Jack Lancaster, Peter T. Fox, Daniel E. Hale, and Jannine D. Cody. A review of 18p deletions. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 169:251-264, Sep 2015. URL: https://doi.org/10.1002/ajmg.c.31445, doi:10.1002/ajmg.c.31445. This article has 93 citations.

10. (balog2018monosomy18pis pages 1-3): Judit Balog, Remko Goossens, Richard J L F Lemmers, Kirsten R Straasheijm, Patrick J van der Vliet, Anita van den Heuvel, Chiara Cambieri, Nicolas Capet, Léonard Feasson, Veronique Manel, Julian Contet, Marjolein Kriek, Colleen M Donlin-Smith, Claudia A L Ruivenkamp, Patricia Heard, Stephen J Tapscott, Jannine D Cody, Rabi Tawil, Sabrina Sacconi, and Silvère M van der Maarel. Monosomy 18p is a risk factor for facioscapulohumeral dystrophy. Journal of Medical Genetics, 55:469-478, Mar 2018. URL: https://doi.org/10.1136/jmedgenet-2017-105153, doi:10.1136/jmedgenet-2017-105153. This article has 25 citations and is from a domain leading peer-reviewed journal.

11. (hasi‐zogaj2015areviewof pages 10-11): Minire Hasi‐Zogaj, Courtney Sebold, Patricia Heard, Erika Carter, Bridgette Soileau, Annice Hill, David Rupert, Brian Perry, Sidney Atkinson, Louise O'Donnell, Jon Gelfond, Jack Lancaster, Peter T. Fox, Daniel E. Hale, and Jannine D. Cody. A review of 18p deletions. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 169:251-264, Sep 2015. URL: https://doi.org/10.1002/ajmg.c.31445, doi:10.1002/ajmg.c.31445. This article has 93 citations.

12. (hasi‐zogaj2015areviewof pages 9-10): Minire Hasi‐Zogaj, Courtney Sebold, Patricia Heard, Erika Carter, Bridgette Soileau, Annice Hill, David Rupert, Brian Perry, Sidney Atkinson, Louise O'Donnell, Jon Gelfond, Jack Lancaster, Peter T. Fox, Daniel E. Hale, and Jannine D. Cody. A review of 18p deletions. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 169:251-264, Sep 2015. URL: https://doi.org/10.1002/ajmg.c.31445, doi:10.1002/ajmg.c.31445. This article has 93 citations.

## Artifacts

- [Edison artifact artifact-00](Chromosome_18p_Deletion_Syndrome-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Chromosome_18p_Deletion_Syndrome-deep-research-falcon_artifacts/artifact-01.md)