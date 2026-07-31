---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T00:07:33.034851'
end_time: '2026-07-31T00:17:31.399131'
duration_seconds: 598.36
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hereditary Spastic Paraplegia 11
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hereditary_Spastic_Paraplegia_11-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Spastic Paraplegia 11
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Spastic Paraplegia 11** covering all of the
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
- **Disease Name:** Hereditary Spastic Paraplegia 11
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Spastic Paraplegia 11** covering all of the
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


# Hereditary Spastic Paraplegia 11 (SPG11): Disease Characteristics Report

**Scope and evidence date.** This report emphasizes evidence available through 2024, especially a December 2023 disease review, a 2024 human neuroinflammation study, a 2024 human genetics study, primary mechanistic papers, and ClinicalTrials.gov records. Frequencies are estimates from heterogeneous cohorts rather than population-wide prospective studies.

| domain | key knowledge-base fact | quantitative detail | evidence type/source/date |
|---|---|---|---|
| Identifiers | Hereditary spastic paraplegia 11 is the SPG11-related, autosomal-recessive complicated HSP entity; MONDO identifier available. | MONDO:0011445; MeSH browse term in trial record: Spastic paraplegia 11, autosomal recessive | Disease ontology/association context and ClinicalTrials.gov browse terms (OpenTargets Search: hereditary spastic paraplegia 11-SPG11, NCT04912609 chunk 1) |
| Epidemiology | SPG11 is a rare HSP subtype and the most common autosomal-recessive complicated HSP in many series. | Global prevalence estimate for HSP11: 0.34 per 100,000; review states up to 8% of all HSP cases | 2023 review, Int J Mol Sci, Dec 2023, doi:10.3390/ijms242417530 (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4) |
| Inheritance | Disease is caused by biallelic loss of SPG11 function with autosomal recessive inheritance. | AR inheritance; Pakistani family study found variants segregating as AR in 5 of 8 families, including recurrent SPG11 p.Gln716* | 2024 human genetic study, BMC Neurol, Sep 2024, doi:10.1186/s12883-024-03855-1; 2024 neuropathology paper states biallelic loss (azeem2024investigatingthegenetic pages 1-2, krumm2024neuroinflammatorydiseasesignatures pages 1-2) |
| Onset and progression | Typical onset is childhood to young adulthood, with slow progression. | Reported onset 4 to 36 years, mean 14.3 years; rare onset 50 to 60 years; Pakistani cohort onset 1 to 14 years, mean 6.23, SD 3.96 | 2023 review; 2024 Pakistani family study (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4, azeem2024investigatingthegenetic pages 1-2) |
| Core phenotypes and HPO | Core syndrome is progressive spastic paraparesis with cognitive and multisystem involvement; suggested HPO includes spastic paraplegia, lower-limb weakness, cognitive impairment, peripheral neuropathy, dysarthria, dysphagia, cerebellar ataxia, parkinsonism, bladder dysfunction, thin corpus callosum. | Cognitive dysfunction reported in 80 to 100 percent of patients; common additional features include peripheral neuropathy, cerebellar signs, pseudobulbar features | 2023 review synthesis and case details (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4) |
| Genetics and causal gene | SPG11 KIAA1840 encodes spatacsin, a large 2443-aa protein; most pathogenic alleles truncate protein and imply loss of function. | More than 180 pathogenic variants reported; gene has 40 exons; protein length 2443 aa | 2023 review and original gene-discovery paper, Nature Genet, Mar 2007, doi:10.1038/ng1980 (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4, stevanin2007mutationsinspg11 pages 1-2) |
| Variant spectrum | Frameshift variants predominate, followed by nonsense and splice-site changes; CNV deletion-duplication events also occur. | Frameshift 54 percent; nonsense 23.20 percent; splice-site 19.33 percent; large deletions or duplications about 10 percent | 2023 review summarizing variant spectrum (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4) |
| MRI | Hallmark MRI findings are thin corpus callosum and frontal periventricular T2 FLAIR hyperintensities called ears of the lynx. | Corpus callosum thinning especially rostrum, genu, and trunk in case example; spinal cord atrophy reported in review literature | 2023 review and case neuroimaging details, Dec 2023, doi:10.3390/ijms242417530 (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 4-6, chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4) |
| Electrophysiology | Peripheral nerve involvement is common and may show demyelinating or mixed sensorimotor polyneuropathy. | Case-based review example reported sensorimotor polyneuropathy with predominantly demyelinating features | 2023 review and case (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4) |
| Lysosomal mechanism | SPG11 loss disrupts autophagic lysosome reformation, depletes lysosomes, impairs autolysosomal clearance, and causes buildup of undegraded material. | Knockout mice showed reduced lysosome numbers and increased lipidated LC3; mechanism linked to cortical motoneuron and Purkinje-cell vulnerability | Primary mouse mechanistic study, PLoS Genet, Aug 18 2015, doi:10.1371/journal.pgen.1005454 (varga2015invivoevidence pages 1-2) |
| AP-5 trafficking complex | Spatacsin functions with SPG15 and AP-5 in a coat-like trafficking complex on late endosomal and lysosomal membranes. | Co-immunoprecipitation stoichiometry about 1 to 1 to 1 to 1 to 1 to 1 for AP-5 subunits with SPG11 and SPG15 | Primary cell biology study, Mol Biol Cell, Aug 2013, doi:10.1091/mbc.e13-03-0170 (hirst2013interactionbetweenap5 pages 1-2) |
| Lipid and ganglioside storage | Loss of spatacsin alters lysosomal lipid clearance and contributes to ganglioside accumulation, supporting substrate-reduction strategies. | Trial background cites glycosphingolipid or ganglioside accumulation and biomarker monitoring of GM2, GM3, or plasma glycosphingolipids | Mechanistic background cited in trials and review synthesis (NCT04912609 chunk 1, NCT04768166 chunk 1, chojdakłukasiewicz2023hereditaryspasticparaplegia pages 4-6) |
| 2024 neuroinflammation | Human postmortem tissue, blood, iPSC microglia, and mouse data support innate immune activation as a disease mechanism; IFN-gamma STAT1 is a candidate pathway. | 3 human postmortem donations studied; increased IL-6 correlated with severity; STAT1 inhibitor reduced CXCL10 production and rescued microglia-mediated neuronal toxicity in vitro | Primary human iPSC translational study, Acta Neuropathol, Feb 2024, doi:10.1007/s00401-023-02675-w (krumm2024neuroinflammatorydiseasesignatures pages 1-2) |
| Diagnostics | Diagnosis relies on clinical recognition plus genomic testing; whole-gene analysis is needed because there is no mutational hotspot. | NGS, exome, or genome sequencing recommended when phenotype overlaps other HSPs; review notes many suspected HSP cases remain genetically unresolved | 2023 review and registry rationale (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 4-6, NCT05354622 chunk 1, NCT04712812 chunk 1) |
| Differential overlap | SPG11 can overlap clinically with AR juvenile ALS and AR Charcot-Marie-Tooth disease, broadening motor-neuron-spectrum differential diagnosis. | SPATACSIN variants found in 10 unrelated pedigrees with AR juvenile ALS in one primary report | Primary human genetics paper, Brain, 2010, doi:10.1093/brain/awp325; review summary (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4) |
| Symptomatic treatment | No approved disease-modifying therapy; treatment is supportive and multidisciplinary; suggested MAXO concepts include antispastic drug therapy, physical therapy, botulinum toxin injection, intrathecal baclofen. | Review lists baclofen, tizanidine, dalfampridine, botulinum toxin, and baclofen pump implantation; rehabilitation commonly used | 2023 review, Dec 2023, doi:10.3390/ijms242417530 (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 4-6) |
| Trial: miglustat | Phase 2 single-group trial evaluated miglustat safety and biomarker effects in SPG11. | NCT04768166; completed; enrolled 10; dose 100 mg TID for 4 weeks then 200 mg TID for 8 weeks; outcomes included blood tests, neurophysiology, adverse events, GM2 GM3, and SPRS | ClinicalTrials.gov, first posted 2021-02-24, last update 2022-04-11 (NCT04768166 chunk 1) |
| Trial: trehalose | Prospective case-only study tracked SPG11 patients taking trehalose, targeting lysosomal dysfunction and glycosphingolipid accumulation. | NCT04912609; completed; enrolled 13; 12-month follow-up; primary outcome SPRS change at 6 and 12 months; secondary plasma glycosphingolipids and gangliosides | ClinicalTrials.gov, first posted 2021-06-03, last update 2022-08-03 (NCT04912609 chunk 1) |
| Registries and natural history | Active registries are building genotype-phenotype and longitudinal outcome infrastructure, including SPG11-specific enrollment. | HSPseq NCT05354622 recruiting, estimated n equals 200; Early-Onset HSP Natural History Registry NCT04712812 recruiting, estimated n equals 700 | ClinicalTrials.gov registry studies (NCT05354622 chunk 1, NCT04712812 chunk 1, NCT04712812 chunk 2) |
| Cellular models | Patient-derived iPSC cortical neurons model neurite pathology, cell death, transport defects, and membranous inclusions; iPSC-derived microglia model inflammatory toxicity. | Tideglusib rescued shorter and less complex neurites and reduced cell death or inclusions in SPG11 neurons; microglia studies identified hyperphagocytosis and cytokine release | Primary iPSC neuron study, Front Neurosci, Dec 6 2018, doi:10.3389/fnins.2018.00914; Acta Neuropathol 2024 (pozner2018tideglusibrescuesneurite pages 1-2, krumm2024neuroinflammatorydiseasesignatures pages 1-2) |
| Animal models | Knockout mouse and zebrafish models recapitulate core neurodegenerative features and support lysosomal and lipid mechanisms; no established natural veterinary disease model identified here. | Mouse model showed loss of cortical neurons and Purkinje cells with lysosomal autophagic pathology; zebrafish morphants reported similar motor-neuron developmental phenotypes in review background | Primary mouse study and model review (varga2015invivoevidence pages 1-2, hirst2013interactionbetweenap5 pages 1-2, damiani2024pluripotentstemcells pages 5-6) |


*Table: This compact table summarizes the main disease knowledge-base facts for hereditary spastic paraplegia 11, including identifiers, clinical features, genetics, mechanisms, diagnostics, treatments, trials, and models. It emphasizes quantitative details and cites only supported context IDs, DOI-backed sources, or NCT records.*

## 1. Disease information

Hereditary spastic paraplegia type 11 (HSP11/SPG11) is a rare, usually childhood- or juvenile-onset, autosomal-recessive neurodevelopmental and neurodegenerative disorder caused by biallelic loss-of-function variants in **SPG11**. It is generally a **complicated HSP**: progressive bilateral lower-limb spasticity and weakness occur with cognitive decline, thin corpus callosum, peripheral neuropathy, amyotrophy, and variably cerebellar, extrapyramidal, retinal, bulbar, and sphincter manifestations. The pathological core is length-dependent degeneration of corticospinal and other long axons, with broader cortical, cerebellar, peripheral-nerve, and immune-cell involvement. A primary discovery paper described onset “during infancy or puberty,” learning difficulties preceding motor disease, and cognitive decline progressing over 10–20 years. (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4, krumm2024neuroinflammatorydiseasesignatures pages 1-2, stevanin2007mutationsinspg11 pages 1-2)

**Identifiers and synonyms**

- **MONDO:** MONDO:0011445.
- **OMIM phenotype:** *Spastic paraplegia 11, autosomal recessive* (SPG11), commonly indexed as **OMIM 604360**; the gene has a separate OMIM gene entry. This OMIM number should be programmatically verified before production ingestion because OMIM itself was not directly retrieved here.
- **MeSH:** D015419, *Spastic Paraplegia, Hereditary*; ClinicalTrials.gov also maps the specific concept “Spastic paraplegia 11, autosomal recessive” to supplementary concept C537483. (NCT04912609 chunk 1)
- **ICD:** ICD-10-CM generally uses **G11.4, hereditary spastic paraplegia**; there is no widely implemented SPG11-specific ICD-10 code. ICD-11 similarly classifies it under hereditary spastic paraplegia rather than a consistently used subtype-specific billing code.
- **Orphanet:** commonly represented as *Autosomal recessive spastic paraplegia type 11*; the numeric ORPHA identifier should be checked directly against the current Orphanet release before database loading.
- **Synonyms:** SPG11; HSP11; autosomal recessive spastic paraplegia type 11; hereditary spastic paraplegia with thin corpus callosum; ARHSP-TCC; spatacsin-associated HSP; SPG11-related disorder. “Kjellin syndrome” denotes the HSP-with-thin-corpus-callosum/retinal-degeneration phenotype but is not uniquely specific to SPG11.

The evidence summarized here is **aggregated disease-level literature and registry information**, supplemented by individual case reports, family studies, three human postmortem donations, and patient-derived cells. It is not an EHR-derived patient-level dataset. (azeem2024investigatingthegenetic pages 1-2, krumm2024neuroinflammatorydiseasesignatures pages 1-2)

## 2. Etiology, risk, protection, and environment

### Causal factor

The necessary cause is generally **biallelic pathogenic or likely pathogenic germline variation in SPG11**, encoding spatacsin. Most alleles introduce premature termination and loss of function. The original 12-family mapping study identified ten nonsense or frameshifting mutations and explicitly concluded that they suggested a loss-of-function mechanism. (stevanin2007mutationsinspg11 pages 1-2)

### Risk factors

- **Genetic:** two pathogenic SPG11 alleles in trans; parental carrier status; an affected sibling; and consanguinity. The 2023 review estimated higher prevalence in Mediterranean and Middle Eastern populations where consanguinity is more frequent. (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4)
- **Founder/recurrent alleles:** a 2024 Pakistani family study found recurrent **SPG11 c.2146C>T, p.(Gln716*)**, suggesting a possible local founder effect. Across eight HSP/ataxia families, pathogenic variants were found in five (62.5%), all segregating recessively; this statistic is for the mixed study cohort, not SPG11 alone. (azeem2024investigatingthegenetic pages 1-2)
- **Family history may be absent:** recessive inheritance, small sibships, and de novo diagnostic ascertainment can produce apparently sporadic cases.
- **Age and sex:** age affects manifestation because penetrance is clinically age-dependent, but neither sex is an established etiologic risk factor. Males and females are affected.

### Protective factors and gene–environment interaction

No validated human protective SPG11 allele, diet, lifestyle, toxin avoidance strategy, or pharmacologic prophylaxis is known. No infectious cause exists. Environmental exposures are not established causes or modifiers. Variable intrafamilial expression suggests unidentified genetic, epigenetic, stochastic, or environmental modifiers, but no reproducible SPG11-specific gene–environment interaction has been demonstrated. Claims that exercise, diet, smoking, alcohol, toxins, pollution, radiation, or infection alter onset should therefore be recorded as **unknown**, not negative evidence. (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4)

## 3. Phenotypes

The usual onset is insidious and chronic. Published estimates place onset at **4–36 years (mean 14.3)**, with rare onset at 50–60 years. The 2024 Pakistani mixed HSP/ataxia cohort had onset at 1–14 years (mean 6.23, SD 3.96), illustrating population and ascertainment variability. (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4, azeem2024investigatingthegenetic pages 1-2)

| Phenotype and type | Characteristics and frequency | Suggested HPO term |
|---|---|---|
| Progressive spastic paraparesis—sign/signature symptom | Usually childhood/juvenile onset; bilateral, slowly progressive; eventually impairs walking and transfers | HP:0001258 Spasticity; HP:0001264 Spastic diplegia; HP:000腿-related lower-limb weakness should be mapped to the current HPO release |
| Hyperreflexia/Babinski signs—sign | Pyramidal pattern; upper-limb hyperreflexia may emerge later | HP:0001347 Hyperreflexia; HP:0003487 Babinski sign |
| Cognitive impairment/learning difficulty—behavioral/neuropsychological | **80–100%** in reviewed cohorts; executive function, attention, memory, and visual perception are prominent; may progress to frontal dementia | HP:0100543 Cognitive impairment; HP:0001328 Specific learning disability; HP:0000726 Dementia |
| Thin corpus callosum—imaging manifestation | Hallmark, especially rostrum/genu/trunk; not fully specific to SPG11 | HP:0002079 Thin corpus callosum |
| “Ears of the lynx”—imaging sign | Frontal periventricular forceps-minor T2/FLAIR hyperintensity; supports SPG11/SPG15 differential but is not independently diagnostic | HP:0002500 Abnormal cerebral white matter morphology |
| Peripheral neuropathy/amyotrophy—sign | Axonal motor or sensorimotor neuropathy is typical; occasional predominantly demyelinating studies; distal wasting develops with progression | HP:0009830 Peripheral neuropathy; HP:0003202 Skeletal muscle atrophy |
| Dysarthria/dysphagia/pseudobulbar involvement—symptom/sign | Usually later; creates aspiration and communication risk | HP:0001260 Dysarthria; HP:0002015 Dysphagia; HP:0002200 Pseudobulbar signs |
| Bladder/sphincter dysfunction—symptom | Common accompaniment of progressive spastic paraparesis | HP:0000016 Urinary incontinence or more specific current HPO term |
| Cerebellar ataxia—sign | Variable and less frequent than corticospinal disease | HP:0001251 Ataxia; HP:0002072 Cerebellar atrophy when imaged |
| Parkinsonism/dystonia—sign | Less frequent extrapyramidal phenotype | HP:0001300 Parkinsonism; HP:0001332 Dystonia |
| Retinal degeneration/Kjellin phenotype—sign | Uncommon; may impair central vision | HP:0000546 Retinal degeneration |
| Pes cavus/scoliosis—physical manifestation | Secondary or associated musculoskeletal features | HP:0001761 Pes cavus; HP:0002650 Scoliosis |

The review’s case had concentration and short-term-memory deficits, thin corpus callosum, “ears of the lynx,” and sensorimotor polyneuropathy, while EEG, visual evoked potentials, ophthalmic examination, spinal MRI, and routine laboratory studies were unrevealing. These are case observations, not universal negatives. (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4)

**Quality of life.** No robust SPG11-specific EQ-5D or SF-36 dataset was identified through 2024. Nonetheless, progressive loss of ambulation, cognition, hand function, speech, swallowing, continence, and independence imposes major educational, occupational, caregiver, and psychosocial burdens. In one postmortem case, onset was at 31, ambulation was lost by 46, and death occurred at 51 after dysphagia and aspiration; this illustrates severe disease but must not be generalized as median survival. (krumm2024neuroinflammatorydiseasesignatures pages 1-2)

## 4. Genetic and molecular information

- **Gene:** **SPG11** (formerly **KIAA1840**), approved name *SPG11 vesicle trafficking associated, spatacsin*; Ensembl **ENSG00000104133**. It maps to chromosome **15q21**, not 15p; some secondary text contains a 15p typographical error. Spatacsin is a 2,443-amino-acid, approximately 280-kDa protein. (OpenTargets Search: hereditary spastic paraplegia 11-SPG11, pozner2018tideglusibrescuesneurite pages 1-2, stevanin2007mutationsinspg11 pages 1-2)
- **Origin/inheritance:** constitutional germline, autosomal recessive. Somatic mutation is not the disease mechanism.
- **Variant spectrum:** more than 180 pathogenic variants were summarized by 2023. Approximate classes were frameshift **54%**, nonsense **23.20%**, splice-site **19.33%**, and large deletions/duplications about **10%**; categories may overlap across source compilations. Variants are distributed across approximately 40 exons without a hotspot, so full-gene and copy-number analysis are necessary. (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4)
- **Functional consequence:** nonsense-mediated decay, truncated protein, and spatacsin loss of function predominate. Missense variants require careful ACMG/AMP assessment because pathogenic missense variation is less common and functional interpretation is difficult.
- **Population frequency:** disease-causing alleles are individually rare. A universal carrier frequency cannot be responsibly inferred from the available evidence; variant-specific gnomAD frequencies and ancestry-matched quality metrics should be imported directly during variant curation.
- **Genotype–phenotype relation:** no robust deterministic correlation. Some reports associate missense/splice variants with later or milder disease, but marked intrafamilial variability limits prediction. (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4)
- **Modifier genes:** no clinically validated modifier. **ZFYVE26/SPG15** and **AP5Z1/SPG48** are pathway partners and phenocopies, not established modifiers. CAPN1 and EIF3J appear in broad disease-association outputs but should not be annotated as causal SPG11 genes. (OpenTargets Search: hereditary spastic paraplegia 11-SPG11, hirst2013interactionbetweenap5 pages 1-2)
- **Epigenetics/chromosomal abnormalities:** no reproducible disease-specific methylation signature or recurrent cytogenetic abnormality is established. Intragenic exon-level CNVs are relevant; routine karyotyping will generally miss them.

## 5. Environmental information

SPG11 is Mendelian, not infectious, toxic, nutritional, occupational, or lifestyle-induced. No vaccine, antimicrobial, toxin removal, smoking cessation, special diet, or supplement prevents the genotype from causing disease. Physical activity and nutrition remain important for secondary health, contracture prevention, bone health, and weight control, but are supportive measures rather than etiologic modifiers.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream trigger:** biallelic SPG11 loss of function eliminates or markedly reduces spatacsin.
2. **Endolysosomal trafficking defect:** spatacsin normally associates with SPG15 and the AP-5 adaptor complex. Biochemical work found an approximately **1:1:1:1:1:1** AP-5/SPG11/SPG15 complex and proposed a coat-like scaffold on late endosomal/lysosomal membranes. Knockdown trapped the cation-independent mannose-6-phosphate receptor in early-endosomal clusters. (hirst2013interactionbetweenap5 pages 1-2)
3. **Autophagic lysosome reformation failure:** after autophagosome–lysosome fusion, lysosomes are inadequately regenerated. Spg11-null cells and mice show fewer lysosomes, impaired recovery during starvation, increased lipidated LC3, LAMP1/p62-positive autofluorescent material, and defective clearance despite relatively preserved lysosomal pH and cathepsin-D processing. (varga2015invivoevidence pages 1-2)
4. **Lipid storage/metabolic stress:** defective membrane recycling and cholesterol/lipid clearance cause lysosomal glycosphingolipid and ganglioside accumulation. This provides the rationale for miglustat substrate reduction. Primary cited studies include PMID **28237315** and PMID **29949766**. (NCT04912609 chunk 1, NCT04768166 chunk 1)
5. **Neurodevelopmental and axonal dysfunction:** patient-derived neural progenitors and cortical neurons exhibit impaired proliferation, reduced neurite length/complexity, disturbed organelle/vesicle transport, inclusions, and increased death. Tideglusib rescue implicates dysregulated **GSK3β/β-catenin** signaling, although this is preclinical rather than an established human therapeutic mechanism. (pozner2018tideglusibrescuesneurite pages 1-2)
6. **Selective degeneration:** extremely long corticospinal axons, cortical motor neurons, dorsal-column pathways, peripheral motor axons, and Purkinje cells are particularly vulnerable. The result is progressive upper- and lower-motor-neuron dysfunction, spasticity, weakness, neuropathy, ataxia, and cognitive decline. (varga2015invivoevidence pages 1-2)
7. **Downstream neuroinflammation:** the major 2024 development was evidence of profound microgliosis, loss of homeostatic microglial markers, and lipid/lipofuscin accumulation in IBA1-positive human cells. Patients had altered monocyte ratios and increased serum IL-6 correlated with severity. IFNγ provoked exaggerated phagocytosis and CXCL10/cytokine release in patient iPSC-derived microglia through increased STAT1 phosphorylation; STAT1 inhibition reduced CXCL10 and rescued microglia-mediated neuronal toxicity in vitro. This establishes inflammation as a plausible amplifying—and potentially druggable—mechanism, not yet a validated clinical target. (krumm2024neuroinflammatorydiseasesignatures pages 1-2)

A key exact abstract statement is: **“Our data establish neuroinflammation as a novel disease mechanism in SPG11–HSP patients and constitute the first description of myeloid cell/microglia activation in human SPG11–HSP.”** (Krumm et al., accepted December 22, 2023; published 2024; DOI: https://doi.org/10.1007/s00401-023-02675-w). (krumm2024neuroinflammatorydiseasesignatures pages 1-2)

**Suggested ontology annotations:** GO:0006914 autophagy; GO:0007040 lysosome organization; GO:0006629 lipid metabolic process; GO:0006886 intracellular protein transport; GO:0006954 inflammatory response; GO:0061909 autophagosome–lysosome fusion; GO:0032008 positive regulation of TOR signaling where contextually supported. Cell types: CL:0000127 astrocyte, CL:0000129 microglial cell, CL:0000125 glial cell, CL:0000540 neuron, CL:0000117 CNS neuron, and the current CL term for upper motor/corticospinal neuron. These are suggested mappings and should be release-validated.

**Molecular profiling.** Human postmortem immunophenotyping and iPSC studies support inflammatory and lipid-storage signatures. Through 2024, no clinically validated SPG11 transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omic diagnostic signature existed. Serum IL-6, gangliosides, and neurofilament light are research candidates, not approved diagnostic or prognostic biomarkers. (krumm2024neuroinflammatorydiseasesignatures pages 1-2, NCT04912609 chunk 1, NCT04768166 chunk 1)

## 7. Anatomical structures affected

- **Primary system:** central nervous system, especially bilateral corticospinal tracts and long descending axons.
- **Brain:** motor and frontal cortex, corpus callosum, periventricular white matter/forceps minor, thalamus, basal ganglia, cerebellum/Purkinje cells, and variably hippocampus.
- **Spinal cord:** corticospinal and posterior columns; spinal-cord atrophy may correlate with duration.
- **Peripheral nervous system:** motor and sensorimotor peripheral axons, producing neuropathy and distal amyotrophy.
- **Secondary structures:** skeletal muscle, joints, spine, bladder, swallowing and respiratory-protective systems are affected through denervation, spasticity, immobility, or bulbar dysfunction.
- **Subcellular compartments:** late endosome, lysosome, autolysosome, autophagosome, lipid-containing inclusions, and trafficking vesicles; mitochondria have been implicated in some models but are less firmly established than lysosomal dysfunction.

Suggested UBERON mappings include cerebral cortex, corpus callosum, corticospinal tract, spinal cord, cerebellum, basal ganglion, thalamus, peripheral nerve, and skeletal muscle; suggested GO cellular components include lysosome (GO:0005764), autophagosome (GO:0005776), late endosome (GO:0005770), and neuron projection (GO:0043005). Disease is normally **bilateral**, although severity may be asymmetric. (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 4-6, chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4, varga2015invivoevidence pages 1-2)

## 8. Temporal development

SPG11 often has an early neurodevelopmental phase—learning difficulty or subtle gait abnormality—followed by chronic neurodegeneration. Early disease includes school difficulty, clumsiness, and lower-limb stiffness; intermediate disease adds progressive gait impairment, neuropathy, distal wasting, cognitive decline, dysarthria, bladder dysfunction, and upper-limb involvement; advanced disease may include wheelchair dependence, severe dementia, dysphagia, aspiration, contractures, and complete dependence. There is no established remission or relapsing-remitting course. Disease is lifelong and generally slowly progressive, but rate varies markedly. Early diagnosis before irreversible axonal loss is the rational therapeutic window, although no disease-modifying intervention has yet been proven. (krumm2024neuroinflammatorydiseasesignatures pages 1-2, stevanin2007mutationsinspg11 pages 1-2, NCT04712812 chunk 1)

## 9. Inheritance and population

- **Prevalence:** estimated **0.34 per 100,000** for SPG11; HSP collectively is often estimated at 1–10 per 100,000. SPG11 accounts for up to **8% of all HSP**, approximately **20% of autosomal-recessive HSP**, and up to **45% of AR-HSP with thin corpus callosum** in selected series. These figures are referral- and ancestry-sensitive. (damiani2024pluripotentstemcells pages 15-16, chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4)
- **Incidence:** no reliable SPG11-specific annual incidence was identified.
- **Inheritance:** autosomal recessive. For two confirmed heterozygous parents, each pregnancy has 25% affected, 50% carrier, and 25% unaffected/non-carrier probabilities.
- **Penetrance:** likely high for clearly pathogenic biallelic null genotypes but age-dependent; precise penetrance is unknown.
- **Expressivity:** variable, including within families.
- **Anticipation:** not established; this is not a repeat-expansion disorder.
- **Mosaicism:** germline mosaicism is theoretically possible but not a recognized major mechanism.
- **Consanguinity/founder effects:** important in some Mediterranean, Middle Eastern, North African, South Asian, and isolated populations. (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4, azeem2024investigatingthegenetic pages 1-2)
- **Sex ratio:** no consistent sex bias.
- **Carrier frequency:** not established globally; calculate ancestry- and variant-specific estimates directly from gnomAD rather than from disease prevalence alone.

## 10. Diagnostics

### Clinical work-up

Suspect SPG11 in a child, adolescent, or young adult with progressive bilateral spastic paraparesis plus learning/cognitive decline, thin corpus callosum, “ears of the lynx,” neuropathy, distal wasting, or cerebellar/bulbar features. Evaluation should include neurological and cognitive examination, three-generation pedigree, brain MRI, spinal MRI where indicated, nerve-conduction studies/EMG, vision/retinal assessment, swallowing and bladder assessment, and the **Spastic Paraplegia Rating Scale (SPRS)** for longitudinal severity. Routine metabolic, infectious, inflammatory, nutritional, and structural investigations primarily exclude treatable mimics; no blood enzyme assay diagnoses SPG11. (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 4-6, chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4)

### Genetic testing strategy

1. Use a comprehensive HSP/spastic-ataxia panel or exome/genome sequencing because phenotypic overlap is extensive.
2. Ensure **SPG11 exon-level deletion/duplication/CNV calling**; sequencing-only assays may miss approximately 10% represented by large intragenic changes.
3. Confirm candidate variants and parental phase/segregation, applying ACMG/AMP criteria.
4. If negative, reanalyze exome data, consider genome sequencing for noncoding/structural variants, and reconsider acquired mimics. The 2024 Pakistani study demonstrates practical WES plus Sanger segregation analysis. (azeem2024investigatingthegenetic pages 1-2, chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4)

Single-gene sequencing is reasonable when phenotype and MRI are highly characteristic, but a broad panel is often more efficient. CMA may detect a large deletion but is less sensitive than exon-level CNV analysis for small intragenic events. Karyotype, FISH, mitochondrial sequencing, and repeat-expansion testing are not routine SPG11 tests; they are reserved for an alternative differential. RNA sequencing may resolve selected splice variants but is not standard first-line testing.

### Differential diagnosis

Key genetic differentials are **ZFYVE26/SPG15**, **AP5Z1/SPG48**, AP-4-associated HSPs, **KIDINS220/SINO syndrome**, **ALS2**, **KIF1A**, **CAPN1**, **FA2H**, **CYP2U1**, **DDHD2**, **GBA2**, **SACS**, **KIAA0415/SPG48-related pathways**, leukodystrophies, juvenile ALS, and Charcot–Marie–Tooth disease. Acquired mimics include cerebral palsy, structural myelopathy, multiple sclerosis, HTLV-1, HIV, syphilis, vitamin B12/copper deficiency, dopa-responsive dystonia, and toxic/metabolic myelopathy. SPG11 variants can themselves produce juvenile ALS- or CMT-like phenotypes, so upper/lower motor-neuron boundaries are not absolute. (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4, pozner2018tideglusibrescuesneurite pages 1-2)

## 11. Outcome and prognosis

No valid 5- or 10-year survival estimate, disease-specific mortality rate, or median life expectancy is available. The disease causes substantial lifelong morbidity: progressive gait failure, wheelchair use, cognitive disability/dementia, neuropathy, dysarthria, dysphagia, bladder dysfunction, pain/spasticity, deformity, and caregiver dependence. Recovery of lost neurons is not expected with current care, although spasticity, mobility, communication, swallowing safety, and secondary complications may improve. Aspiration, immobility, falls, fractures, urinary complications, and respiratory infection are plausible advanced complications. Prognostic prediction from genotype remains weak; age at onset, baseline SPRS, ambulation, cognition, bulbar involvement, and longitudinal change are more practical clinical variables. (krumm2024neuroinflammatorydiseasesignatures pages 1-2, NCT04712812 chunk 1)

## 12. Treatment and current implementation

There is **no approved disease-modifying, gene, cell, RNA, or immunotherapy** for SPG11. Current real-world care is multidisciplinary and symptomatic.

- **Spasticity:** oral baclofen, tizanidine, or other individualized antispastic medication; focal botulinum toxin; selected intrathecal baclofen. Suggested MAXO: pharmacotherapy, botulinum toxin injection, intrathecal drug administration.
- **Rehabilitation:** regular physiotherapy, stretching, strengthening, gait/balance training, orthoses, mobility aids, wheelchair/seating, occupational therapy, and home/school adaptations. Suggested MAXO: physical therapy, occupational therapy, assistive-device prescription.
- **Bulbar/communication:** speech-language assessment, augmentative communication, swallow study, texture modification, and enteral nutrition if needed. Suggested MAXO: speech therapy, swallowing assessment, gastrostomy.
- **Bladder/bowel, pain, orthopedic, retinal, mood, cognition, and nutrition:** treat according to manifestation; monitor contractures, scoliosis, bone health, pressure injury, and caregiver needs.

The 2023 review lists baclofen, tizanidine, dalfampridine, botulinum toxin, baclofen pumps, physical therapy, and exploratory high-frequency repetitive transcranial magnetic stimulation, but efficacy evidence is limited and not SPG11-definitive. (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 4-6)

### Experimental treatments and trials

- **Miglustat—NCT04768166 (TreatSPG11):** completed, open-label, single-group phase 2 safety study; **10 participants**. Dosing was 100 mg three times daily for four weeks, then 200 mg three times daily for eight weeks. Outcomes included laboratory/neurophysiological safety, serious adverse events, GM2/GM3, and SPRS. The registry does not provide a controlled efficacy result; it should not be interpreted as demonstrating benefit. https://clinicaltrials.gov/study/NCT04768166 (first posted February 24, 2021). (NCT04768166 chunk 1)
- **Trehalose—NCT04912609:** completed prospective observational case-only study; **13 actual participants**, despite an intended 20. It monitored SPRS and plasma glycosphingolipids/gangliosides over 12 months. Because it was observational and lacked a randomized control, causal efficacy cannot be inferred. https://clinicaltrials.gov/study/NCT04912609 (first posted June 3, 2021). (NCT04912609 chunk 1)
- **Tideglusib:** rescued reduced neurite complexity, cell death, and membranous inclusions in patient and CRISPR SPG11 cortical neurons. The authors wrote: **“Our results provide a first evidence for the rescue of neurite pathology in SPG11-HSP by tideglusib.”** This is in-vitro evidence only. DOI: https://doi.org/10.3389/fnins.2018.00914, published December 6, 2018. (pozner2018tideglusibrescuesneurite pages 1-2)
- **Immunomodulation:** STAT1 inhibition rescued microglia-mediated neuronal toxicity in vitro in 2024; no human trial establishes safety or efficacy. (krumm2024neuroinflammatorydiseasesignatures pages 1-2)
- **Research infrastructure:** HSPseq, NCT05354622, is recruiting an estimated 200 participants for genomic/phenotypic analysis; NCT04712812 is recruiting an estimated 700 for early-onset HSP natural history and biobanking. These are observational, not treatment trials. (NCT05354622 chunk 1, NCT04712812 chunk 1)

No SPG11 pharmacogenomic prescribing guideline from CPIC/PharmGKB was identified.

## 13. Prevention

Primary lifestyle prevention is impossible because disease is inherited. Effective prevention is genetic and reproductive:

- genetic counseling and parental segregation testing;
- cascade/carrier testing for adult relatives after the familial variants are known;
- partner testing where relevant;
- prenatal diagnosis through chorionic-villus sampling or amniocentesis;
- preimplantation genetic testing for monogenic disease;
- early testing of symptomatic at-risk siblings to shorten diagnostic delay.

Population newborn screening is not established, and SPG11 is not a routine universal newborn-screening condition. Secondary prevention means early rehabilitation, surveillance for swallowing/aspiration, contractures, scoliosis, falls, bladder dysfunction, malnutrition, and psychosocial needs. Tertiary prevention focuses on maintaining mobility, communication, nutrition, respiratory safety, skin integrity, and participation. Vaccination follows ordinary schedules and may reduce respiratory complications but does not prevent SPG11.

## 14. Other species and natural disease

No well-established naturally occurring veterinary disease caused by biallelic SPG11 ortholog variants was identified. Thus breed-specific VBO terms, veterinary prevalence, zoonotic transmission, and cross-species contagion are **not applicable**. SPG11 is evolutionarily conserved and experimentally modeled in **Mus musculus** (NCBI Taxonomy 10090) and **Danio rerio** (7955). Orthologous gene identifiers should be imported directly from NCBI Gene/Alliance in the production pipeline rather than inferred here.

## 15. Model organisms and experimental systems

- **Spg11-knockout mouse:** develops HSP-like motor abnormalities, progressive loss of cortical motor neurons and Purkinje cells, reduced lysosome numbers, impaired autophagic lysosome reformation, and LAMP1/p62-positive storage material. It supports causality from lysosomal depletion to neuronal death. A limitation is incomplete reproduction of the human thin-corpus-callosum phenotype. The primary abstract states that disruption “causes hereditary spastic paraplegia-like phenotypes with loss of cortical neurons and Purkinje cells.” DOI: https://doi.org/10.1371/journal.pgen.1005454, published August 18, 2015. (varga2015invivoevidence pages 1-2)
- **Zebrafish morphants:** SPG11/SPG15 knockdown produces related motor-neuron developmental and tail/motility phenotypes. Advantages are rapid developmental analysis and screening; limitations include transient knockdown and imperfect human neuroanatomy. (damiani2024pluripotentstemcells pages 5-6, hirst2013interactionbetweenap5 pages 1-2)
- **Patient fibroblasts/primary neurons:** reproduce lysosomal lipid and ganglioside accumulation and support substrate-reduction experiments with miglustat. (NCT04912609 chunk 1, NCT04768166 chunk 1)
- **Patient iPSC-derived cortical neurons and CRISPR knockout neurons:** show shortened, less-complex neurites, transport defects, inclusions, and increased cell death; they support isogenic validation and drug screening, including tideglusib rescue. Limitations are cellular immaturity, culture variability, and absence of full corticospinal circuitry. (pozner2018tideglusibrescuesneurite pages 1-2)
- **Patient iPSC-derived microglia:** reproduce IFNγ/STAT1 hyperactivation, increased phagocytosis, CXCL10 release, and neuronal toxicity, connecting human immune cells to pathology. (krumm2024neuroinflammatorydiseasesignatures pages 1-2)
- **Organoids and advanced omics:** emerging cortical-organoid work is promising for neurodevelopmental and lysosomal-calcium mechanisms, but through 2024 it was not yet a mature, independently replicated basis for clinical annotation. Spatial and single-cell atlases remain important research gaps.

## Overall assessment

SPG11 is best understood as a **biallelic spatacsin-loss disorder spanning neurodevelopment, lysosomal membrane recycling failure, lipid/ganglioside storage, long-axon degeneration, and secondary innate immune activation**. The strongest 2023–2024 advances were improved phenotypic/genomic characterization and direct human evidence that IFNγ/STAT1-driven microglial activation may amplify neurodegeneration. Clinical implementation remains centered on genomic confirmation, MRI and neurophysiological characterization, multidisciplinary rehabilitation, complication prevention, and genetic counseling. Miglustat, trehalose, tideglusib, and immunomodulation remain investigational; no controlled study has yet established disease modification.

References

1. (OpenTargets Search: hereditary spastic paraplegia 11-SPG11): Open Targets Query (hereditary spastic paraplegia 11-SPG11, 11 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (NCT04912609 chunk 1): Filippo Maria Santorelli. Trehalose Administration in Subjects With Spastic Paraplegia 11 (3AL-SPG11). IRCCS Fondazione Stella Maris. 2021. ClinicalTrials.gov Identifier: NCT04912609

3. (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4): Justyna Chojdak-Łukasiewicz, Katarzyna Sulima, Anna Zimny, Marta Waliszewska-Prosół, and Sławomir Budrewicz. Hereditary spastic paraplegia type 11—clinical, genetic and neuroimaging characteristics. International Journal of Molecular Sciences, 24:17530, Dec 2023. URL: https://doi.org/10.3390/ijms242417530, doi:10.3390/ijms242417530. This article has 8 citations.

4. (azeem2024investigatingthegenetic pages 1-2): Arfa Azeem, Asif Naveed Ahmed, Niamat Khan, Nikol Voutsina, Irfan Ullah, Nishanka Ubeyratna, Muhammad Yasin, Emma L. Baple, Andrew H. Crosby, Lettie E. Rawlins, and Shamim Saleha. Investigating the genetic basis of hereditary spastic paraplegia and cerebellar ataxia in pakistani families. BMC Neurology, Sep 2024. URL: https://doi.org/10.1186/s12883-024-03855-1, doi:10.1186/s12883-024-03855-1. This article has 6 citations and is from a peer-reviewed journal.

5. (krumm2024neuroinflammatorydiseasesignatures pages 1-2): Laura Krumm, Tatyana Pozner, Naime Zagha, Roland Coras, Philipp Arnold, Thanos Tsaktanis, Kathryn Scherpelz, Marie Y. Davis, Johanna Kaindl, Iris Stolzer, Patrick Süß, Mukhran Khundadze, Christian A. Hübner, Markus J. Riemenschneider, Jonathan Baets, Claudia Günther, Suman Jayadev, Veit Rothhammer, Florian Krach, Jürgen Winkler, Beate Winner, and Martin Regensburger. Neuroinflammatory disease signatures in spg11-related hereditary spastic paraplegia patients. Acta Neuropathologica, Feb 2024. URL: https://doi.org/10.1007/s00401-023-02675-w, doi:10.1007/s00401-023-02675-w. This article has 17 citations and is from a highest quality peer-reviewed journal.

6. (stevanin2007mutationsinspg11 pages 1-2): Giovanni Stevanin, Filippo M Santorelli, Hamid Azzedine, Paula Coutinho, Jacques Chomilier, Paola S Denora, Elodie Martin, Anne-Marie Ouvrard-Hernandez, Alessandra Tessa, Naïma Bouslam, Alexander Lossos, Perrine Charles, José L Loureiro, Nizar Elleuch, Christian Confavreux, Vítor T Cruz, Merle Ruberg, Eric Leguern, Djamel Grid, Meriem Tazir, Bertrand Fontaine, Alessandro Filla, Enrico Bertini, Alexandra Durr, and Alexis Brice. Mutations in spg11, encoding spatacsin, are a major cause of spastic paraplegia with thin corpus callosum. Nature Genetics, 39:366-372, Mar 2007. URL: https://doi.org/10.1038/ng1980, doi:10.1038/ng1980. This article has 419 citations and is from a highest quality peer-reviewed journal.

7. (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 4-6): Justyna Chojdak-Łukasiewicz, Katarzyna Sulima, Anna Zimny, Marta Waliszewska-Prosół, and Sławomir Budrewicz. Hereditary spastic paraplegia type 11—clinical, genetic and neuroimaging characteristics. International Journal of Molecular Sciences, 24:17530, Dec 2023. URL: https://doi.org/10.3390/ijms242417530, doi:10.3390/ijms242417530. This article has 8 citations.

8. (varga2015invivoevidence pages 1-2): Rita-Eva Varga, Mukhran Khundadze, Markus Damme, Sandor Nietzsche, Birgit Hoffmann, Tobias Stauber, Nicole Koch, J. Christopher Hennings, Patricia Franzka, Antje K. Huebner, Michael M. Kessels, Christoph Biskup, Thomas J. Jentsch, Britta Qualmann, Thomas Braulke, Ingo Kurth, Christian Beetz, and Christian A. Hübner. In vivo evidence for lysosome depletion and impaired autophagic clearance in hereditary spastic paraplegia type spg11. PLOS Genetics, 11:e1005454, Aug 2015. URL: https://doi.org/10.1371/journal.pgen.1005454, doi:10.1371/journal.pgen.1005454. This article has 154 citations and is from a domain leading peer-reviewed journal.

9. (hirst2013interactionbetweenap5 pages 1-2): Jennifer Hirst, Georg H. H. Borner, James Edgar, Marco Y. Hein, Matthias Mann, Frank Buchholz, Robin Antrobus, and Margaret S. Robinson. Interaction between ap-5 and the hereditary spastic paraplegia proteins spg11 and spg15. Molecular Biology of the Cell, 24:2558-2569, Aug 2013. URL: https://doi.org/10.1091/mbc.e13-03-0170, doi:10.1091/mbc.e13-03-0170. This article has 155 citations and is from a domain leading peer-reviewed journal.

10. (NCT04768166 chunk 1): Filippo Maria Santorelli. Testing Miglustat Administration in Subjects With Spastic Paraplegia 11. IRCCS Fondazione Stella Maris. 2021. ClinicalTrials.gov Identifier: NCT04768166

11. (NCT05354622 chunk 1): Darius Ebrahimi-Fakhari. Hereditary Spastic Paraplegia Genomic Sequencing Initiative (HSPseq). Boston Children's Hospital. 2022. ClinicalTrials.gov Identifier: NCT05354622

12. (NCT04712812 chunk 1): Darius Ebrahimi-Fakhari. Registry and Natural History Study for Early Onset Hereditary Spastic Paraplegia. Boston Children's Hospital. 2020. ClinicalTrials.gov Identifier: NCT04712812

13. (NCT04712812 chunk 2): Darius Ebrahimi-Fakhari. Registry and Natural History Study for Early Onset Hereditary Spastic Paraplegia. Boston Children's Hospital. 2020. ClinicalTrials.gov Identifier: NCT04712812

14. (pozner2018tideglusibrescuesneurite pages 1-2): Tatyana Pozner, Annika Schray, Martin Regensburger, Dieter Chichung Lie, Ursula Schlötzer-Schrehardt, Jürgen Winkler, Soeren Turan, and Beate Winner. Tideglusib rescues neurite pathology of spg11 ipsc derived cortical neurons. Frontiers in Neuroscience, Dec 2018. URL: https://doi.org/10.3389/fnins.2018.00914, doi:10.3389/fnins.2018.00914. This article has 37 citations and is from a peer-reviewed journal.

15. (damiani2024pluripotentstemcells pages 5-6): Devid Damiani, Matteo Baggiani, Stefania Della Vecchia, Valentina Naef, and Filippo Maria Santorelli. Pluripotent stem cells as a preclinical cellular model for studying hereditary spastic paraplegias. International Journal of Molecular Sciences, 25:2615, Feb 2024. URL: https://doi.org/10.3390/ijms25052615, doi:10.3390/ijms25052615. This article has 11 citations.

16. (damiani2024pluripotentstemcells pages 15-16): Devid Damiani, Matteo Baggiani, Stefania Della Vecchia, Valentina Naef, and Filippo Maria Santorelli. Pluripotent stem cells as a preclinical cellular model for studying hereditary spastic paraplegias. International Journal of Molecular Sciences, 25:2615, Feb 2024. URL: https://doi.org/10.3390/ijms25052615, doi:10.3390/ijms25052615. This article has 11 citations.

## Artifacts

- [Edison artifact artifact-00](Hereditary_Spastic_Paraplegia_11-deep-research-falcon_artifacts/artifact-00.md)