---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T19:25:47.140219'
end_time: '2026-07-31T19:36:35.282103'
duration_seconds: 648.14
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Microcephaly, Short Stature, and Impaired Glucose Metabolism 2
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Microcephaly_Short_Stature_and_Impaired_Glucose_Metabolism_2-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Microcephaly, Short Stature, and Impaired Glucose Metabolism 2
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Microcephaly, Short Stature, and Impaired Glucose Metabolism 2** covering all of the
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
- **Disease Name:** Microcephaly, Short Stature, and Impaired Glucose Metabolism 2
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Microcephaly, Short Stature, and Impaired Glucose Metabolism 2** covering all of the
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


# Microcephaly, Short Stature, and Impaired Glucose Metabolism 2 (MSSGM2)

## Executive summary

MSSGM2 is an ultra-rare autosomal-recessive neurodevelopmental–endocrine disorder caused by biallelic pathogenic variants in **PPP1R15B**, encoding the constitutive repressor of eIF2α phosphorylation (**CReP**). The best-established phenotype combines congenital or early growth failure and microcephaly, intellectual disability, and later autoimmune-negative diabetes. The foundational evidence is a 2015 report of two affected siblings homozygous for **p.Arg658Cys**; a 2024 structural study described a homozygous **p.Asn423Asp** variant with an overlapping growth and neurodevelopmental phenotype but without established diabetes in the available report. The evidence base remains too small for reliable prevalence, penetrance, survival, or phenotype-frequency estimates. (abdulkarim2015amissensemutation pages 1-2, fatalska2024recruitmentoftrimeric pages 10-12, fatalska2024recruitmentoftrimeric pages 8-10)

| Domain | Summary | Key details / ontology hints | Evidence |
|---|---|---|---|
| Disease definition | Microcephaly, short stature, and impaired glucose metabolism 2 (MSSGM2) is an ultra-rare Mendelian multisystem disorder linked to biallelic PPP1R15B dysfunction, with neurodevelopmental abnormalities and diabetes or impaired glucose metabolism as major manifestations. | Mendelian disorder; syndrome-level, disease-aggregated knowledge derived from published case reports and reviews. | (abdulkarim2015amissensemutation pages 1-2, stone2021monogenicandsyndromic pages 6-8, gobble2025neonatalandsyndromic pages 7-8) |
| Causal gene / protein | Causal gene: **PPP1R15B**; protein: **protein phosphatase 1 regulatory subunit 15B** / **CReP**, a regulatory subunit of an eIF2α phosphatase complex. | Pathway anchor: eIF2α dephosphorylation / integrated stress response (ISR). | (abdulkarim2015amissensemutation pages 1-2, fatalska2024recruitmentoftrimeric pages 10-12, hicks2023theppp1r15family pages 7-9, gobble2025neonatalandsyndromic pages 7-8) |
| Inheritance | Autosomal recessive. | Reported affected individuals carried homozygous missense variants; one index family was consanguineous. | (abdulkarim2015amissensemutation pages 4-7, abdulkarim2015amissensemutation pages 3-4, gobble2025neonatalandsyndromic pages 7-8) |
| Established variants | Best-established disease variant: **p.Arg658Cys (R658C)** in PPP1R15B. A later **p.Asn423Asp (N423D)** homozygous variant was reported with overlapping neurodevelopmental/growth features and impaired substrate recruitment; diabetes status was not established in the extracted evidence. | R658C impairs PP1 binding; N423D impairs eIF2 recruitment while preserving PP1 binding. Variant-class evidence is strongest for homozygous missense change(s); avoid overcalling broader allelic series from current sparse literature. | (abdulkarim2015amissensemutation pages 1-2, fatalska2024recruitmentoftrimeric pages 10-12, fatalska2024recruitmentoftrimeric pages 8-10, fatalska2024recruitmentoftrimeric pages 3-5) |
| Core phenotype | Core syndrome comprises **microcephaly**, **short stature/growth retardation**, **intellectual disability/developmental delay**, and **impaired glucose metabolism/diabetes**. Additional reported findings include sensorineural deafness, delayed puberty, kyphoscoliosis, pectus excavatum, dental anomalies/oligodontia, sparse hair, hepatic fibrosis/cirrhosis, and hypothyroidism. | HPO suggestions: Microcephaly HP:0000252; Short stature HP:0004322; Intellectual disability HP:0001249; Diabetes mellitus HP:0000819; Sensorineural hearing impairment HP:0000407; Kyphoscoliosis HP:0002751; Pectus excavatum HP:0000767; Oligodontia HP:0000677. | (abdulkarim2015amissensemutation pages 4-7, abdulkarim2015amissensemutation pages 3-4, stone2021monogenicandsyndromic pages 6-8, gobble2025neonatalandsyndromic pages 7-8) |
| Diabetes course | Diabetes has been reported from adolescence to adulthood in the primary family, with insulin dependence, negative type 1 diabetes autoantibodies, residual C-peptide, moderate insulin requirements, and ketosis in at least one patient. Reviews describe the glucose phenotype as late-onset relative to the congenital growth/neurodevelopmental features. | Reported ages at onset in extracted evidence: 15 years and 28 years. Insulin requirement examples: ~0.5 and ~0.7 U/kg/day. | (abdulkarim2015amissensemutation pages 4-7, abdulkarim2015amissensemutation pages 3-4, abdulkarim2015amissensemutation pages 9-11, stone2021monogenicandsyndromic pages 6-8) |
| Key mechanism | PPP1R15B/CReP normally helps PP1 dephosphorylate **eIF2α-Ser51**. Disease variants impair PP1 binding and/or eIF2 substrate recruitment, causing persistently increased eIF2α phosphorylation, dysregulated ISR/ER-stress signaling, impaired translation/secretory homeostasis, β-cell dysfunction, and apoptosis. | Cell/process hints: pancreatic beta cell (CL:0000169); endoplasmic reticulum stress GO:0034976; response to unfolded protein GO:0006986; regulation of translation GO:0006417; apoptotic process GO:0006915. | (abdulkarim2015amissensemutation pages 1-2, abdulkarim2015amissensemutation pages 9-11, abdulkarim2015amissensemutation pages 7-9, fatalska2024recruitmentoftrimeric pages 10-12, hicks2023theppp1r15family pages 7-9, fatalska2024recruitmentoftrimeric pages 3-5) |
| Diagnosis | Diagnosis is based on syndromic clinical recognition plus molecular confirmation of biallelic PPP1R15B variants, typically by exome sequencing with segregation confirmation. Supportive evaluations include diabetes phenotyping, neurodevelopmental assessment, hearing testing, and imaging/skeletal/endocrine workup as clinically indicated. | In the index report, exome sequencing, segregation filtering, and confirmatory Sanger/PCR-RFLP genotyping were used. Differential considerations include other ER-stress/monogenic diabetes syndromes such as Wolcott-Rallison syndrome. | (abdulkarim2015amissensemutation pages 4-7, abdulkarim2015amissensemutation pages 1-2, hicks2023theppp1r15family pages 7-9) |
| Treatment | No disease-specific approved therapy or disease-targeted clinical trial was identified in the available evidence. Current care is supportive and phenotype-directed: insulin for diabetes, endocrine management, developmental/educational support, audiology, orthopedic care, dental care, and surveillance for liver/thyroid/puberty complications. | NCIT-style intervention hints: Insulin Therapy; Genetic Counseling; Physical Therapy; Occupational Therapy; Hearing Aid. These are management extrapolations, not validated disease-specific protocols. | (abdulkarim2015amissensemutation pages 9-11, gobble2025neonatalandsyndromic pages 7-8) |
| Epidemiology | Extremely rare; available evidence supports only a very small number of reported individuals worldwide. No robust prevalence, incidence, carrier-frequency, or sex-ratio estimates were identified in the extracted sources. | Human evidence base includes the original two siblings plus later review-level mention of additional patients/affected siblings and one N423D patient with overlapping phenotype. | (stone2021monogenicandsyndromic pages 6-8, fatalska2024recruitmentoftrimeric pages 8-10, vaneynde2022theroleof pages 6-7, abdulkarim2015amissensemutation pages 4-7) |
| Evidence limitations | Knowledge remains constrained by very small sample size, incomplete longitudinal follow-up, review-level aggregation of some later cases, uncertain phenotype frequencies, and lack of disease-specific natural-history studies, treatment trials, or omics datasets. Some later features (e.g., hepatic fibrosis, hypothyroidism) are review-reported and not fully resolvable to individual primary cases from the extracted evidence. | Use cautious wording for penetrance, prognosis, and variant spectrum; avoid unsupported identifiers or precise epidemiologic estimates. | (stone2021monogenicandsyndromic pages 6-8, gobble2025neonatalandsyndromic pages 7-8, vaneynde2022theroleof pages 6-7, abdulkarim2015amissensemutation pages 4-7) |


*Table: This table condenses the most reliable current knowledge on PPP1R15B-related MSSGM2 for disease knowledge-base use. It highlights established facts, likely clinical annotations, and major evidence gaps from the small published case literature.*

## 1. Disease information

### Definition and identifiers

- **Preferred name:** Microcephaly, short stature, and impaired glucose metabolism 2.
- **Abbreviation:** MSSGM2.
- **OMIM:** **#616817**.
- **Causal gene:** **PPP1R15B**; OMIM gene entry **613257**.
- **Common alternatives:** PPP1R15B-related disorder; PPP1R15B-related syndromic diabetes; CReP deficiency; diabetes–short stature–microcephaly syndrome.
- **MONDO:** A dedicated MONDO identifier could not be verified from the retrieved evidence; it should be resolved directly against the current MONDO release before database ingestion rather than inferred.
- **Orphanet, MeSH, ICD-10/ICD-11:** No disease-specific entries or codes were verified. Coding generally must use component findings—congenital microcephaly, short stature, intellectual disability, and diabetes—plus a rare-genetic-disease code where locally supported.

This is aggregated disease-level knowledge derived principally from published families, not an EHR-derived cohort. The original article appeared in *Diabetes* 64(11), November 2015, DOI [10.2337/db15-0477](https://doi.org/10.2337/db15-0477), PMID **26310607**. Its abstract states: “Here, we report the first homozygous mutation in the PPP1R15B gene … in two siblings affected by a novel syndrome of diabetes of youth with short stature, intellectual disability, and microcephaly.” (abdulkarim2015amissensemutation pages 1-2)

## 2. Etiology, risk, and protective factors

### Primary cause

The disease is caused by **germline biallelic PPP1R15B dysfunction**. The original family had first-cousin parents and homozygous p.Arg658Cys in both affected siblings, establishing autosomal-recessive transmission. Consanguinity is therefore a reproductive risk factor—not a biological cause beyond increasing the probability that both parents carry the same rare allele. (abdulkarim2015amissensemutation pages 3-4, abdulkarim2015amissensemutation pages 4-7)

### Variants and risk architecture

1. **p.Arg658Cys (R658C), homozygous:** strongest disease association. It affects the conserved C-terminal PP1-binding functional core, weakens PP1 recruitment, and reduces eIF2α dephosphorylation. (abdulkarim2015amissensemutation pages 1-2, abdulkarim2015amissensemutation pages 7-9)
2. **p.Asn423Asp (N423D), homozygous:** reported in 2024 in a child with microcephaly, short stature, intellectual disability, and white-matter abnormalities. It disrupts eIF2-substrate recruitment while preserving PP1 binding. Because diabetes was not established in the extracted evidence, this is best annotated as an overlapping **PPP1R15B-related neurodevelopmental phenotype**, with possible age-dependent evolution toward MSSGM2, rather than automatically assigning the complete MSSGM2 phenotype. (fatalska2024recruitmentoftrimeric pages 10-12, fatalska2024recruitmentoftrimeric pages 8-10)

No validated susceptibility loci, modifier genes, protective alleles, founder effect, germline mosaicism, genetic anticipation, or population carrier frequency have been established. The original study screened 22 additional compatible families without finding further biallelic PPP1R15B variants, illustrating both rarity and genetic heterogeneity among phenocopies. (abdulkarim2015amissensemutation pages 4-7)

### Environment and gene–environment interaction

No toxin, infection, diet, occupation, smoking exposure, or lifestyle factor is known to cause MSSGM2. Cellular experiments show that palmitate and pharmacologic ER stressors induce PPP1R15B in β cells, supporting the general concept that metabolic or proteotoxic stress could worsen a genetically reduced stress-response reserve; this has **not** been demonstrated clinically as a disease-specific gene–environment interaction. (abdulkarim2015amissensemutation pages 7-9)

## 3. Phenotypes

Because the primary cohorts contain only a few patients, observed fractions must not be interpreted as population frequencies.

| Phenotype | Type, onset, and course | Evidence and impact | Suggested HPO |
|---|---|---|---|
| Microcephaly | Clinical sign; congenital/childhood; persistent | Both original siblings; one male had head circumference 46 cm, approximately −4 SD. The N423D child was −2.60 SD. Associated with developmental disability. | HP:0000252 |
| Short stature/growth retardation | Physical sign; prenatal or early childhood; persistent | Original siblings were small for gestational age; reported adult heights included 155 cm and 139 cm. N423D child: −2.16 SD. | HP:0004322; small for gestational age HP:0001518 |
| Intellectual disability/global developmental delay | Neurodevelopmental sign; childhood; lifelong | Severe in the original family—one individual had an estimated mental age of 5–6 years at age 15. N423D patient had IQ 57. | HP:0001249; HP:0001263 |
| Diabetes mellitus/impaired glucose metabolism | Laboratory abnormality and disease; adolescence–adulthood in the best-documented family | Onset at 15 and 28 years; autoimmune-negative in the index case, with residual C-peptide. One patient presented with ketosis. Insulin treatment affects daily self-care and hypoglycemia risk. | HP:0000819; hyperglycemia HP:0003074; ketosis HP:0001946 |
| Sensorineural hearing impairment | Clinical sign; timing incompletely defined | Neurogenic hearing loss, including 39% loss in one patient; affects communication and education. | HP:0000407 |
| Brain MRI abnormalities | Imaging sign | White-matter rarefaction/delayed myelination and periventricular white-matter hyperintensities; hypoplastic brainstem/spinal cord described at review level. | HP:0002500; HP:0012448 where applicable |
| Skeletal/thoracic findings | Physical signs; developmental | Kyphoscoliosis, pectus excavatum, vertebral abnormalities; potential mobility and respiratory impact not quantified. | HP:0002751; HP:0000767 |
| Dental/hair findings | Physical signs | Oligodontia, dental hypoplasia, and sparse hair. | HP:0000677; HP:0000691; HP:0008070 |
| Endocrine/reproductive findings | Clinical/laboratory signs | Delayed puberty and hypothyroidism appear in later aggregate reviews; individual frequencies are unresolved. | HP:0000823; HP:0000878 |
| Liver disease | Clinical/laboratory/pathology finding | Hepatic fibrosis/cirrhosis is review-reported; patient-level frequency and progression are unresolved. | HP:0001395; HP:0002613 |

Clinical measurements and associated findings come from the original family and 2024 case; broader features such as hypothyroidism and hepatic fibrosis are mainly review-level aggregates. (abdulkarim2015amissensemutation pages 4-7, abdulkarim2015amissensemutation pages 3-4, stone2021monogenicandsyndromic pages 6-8, fatalska2024recruitmentoftrimeric pages 8-10, gobble2025neonatalandsyndromic pages 7-8)

No validated MSSGM2-specific quality-of-life instrument or EQ-5D/SF-36 study exists. Likely burdens include dependence arising from intellectual disability, insulin administration and glucose monitoring, hypoglycemia, hearing impairment, and orthopedic/dental morbidity, but these have not been quantified.

## 4. Genetic and molecular information

**PPP1R15B** encodes CReP, a regulatory/targeting subunit that combines with protein phosphatase 1 catalytic subunit to dephosphorylate eIF2α. PPP1R15B is broadly expressed and is prominent in human islets and β cells. (abdulkarim2015amissensemutation pages 4-7)

- **Variant class:** reported disease alleles are germline, homozygous missense variants.
- **Functional consequence:** hypomorphic loss of holophosphatase function rather than proven complete null activity.
- **p.Arg658Cys:** weakens the ionic/structural contact between PPP1R15B Arg658 and PP1 Asp71, destabilizing the complex. Wild-type complexes substantially dephosphorylated eIF2α by 45 minutes; mutant complexes retained substantial phospho-eIF2α at 60 minutes. (abdulkarim2015amissensemutation pages 7-9)
- **p.Asn423Asp:** lies immediately before helix H1 and impairs eIF2 capture and dephosphorylation without materially impairing PP1 binding. (fatalska2024recruitmentoftrimeric pages 10-12, fatalska2024recruitmentoftrimeric pages 8-10)
- **Population frequency:** no reliable frequency was recovered; the alleles are sufficiently rare to be compatible with an ultra-rare recessive disorder. A current gnomAD query should be stored with transcript/version and ancestry-specific counts before assigning an exact frequency.
- **ClinVar/ACMG:** classifications should be imported from the current ClinVar record rather than inferred from this review. p.Arg658Cys has strong case, segregation, conservation, and functional evidence; p.Asn423Asp has functional evidence but a narrower clinical association.

No validated modifier genes, disease-specific methylation signature, chromosomal rearrangement, copy-number syndrome, somatic variant mechanism, or repeat expansion has been reported.

## 5. Environmental information

MSSGM2 is not an infectious, toxic, occupational, radiation-associated, or lifestyle-acquired disease. No causal pathogens or immune triggers are known. Ordinary nutrition, exercise, and avoidance of smoking remain relevant to diabetes care but have not been shown to prevent the underlying syndrome. There are no established environmental protective factors.

## 6. Mechanism and pathophysiology

### Causal chain

**Biallelic PPP1R15B variant → defective PP1 or eIF2 recruitment → reduced dephosphorylation of eIF2α-Ser51 → persistent integrated stress response (ISR) and translation repression → defective secretory-cell homeostasis, altered insulin production/secretion, and stress-induced apoptosis → diabetes; impaired growth and neurodevelopment arise from analogous vulnerability during development.** (abdulkarim2015amissensemutation pages 1-2, fatalska2024recruitmentoftrimeric pages 10-12, hicks2023theppp1r15family pages 7-9)

The 2024 *Molecular Cell* study—published February 1, 2024, DOI [10.1016/j.molcel.2023.12.011](https://doi.org/10.1016/j.molcel.2023.12.011)—is the principal recent advance. It showed that PPP1R15B binds trimeric eIF2 with high affinity independently of PP1 through a substrate-binding region containing helices H1 (residues 424–429) and H2 (472–482). PPP1R15B grasps eIF2 at a site remote from eIF2α-Ser51 and positions that phosphosite for PP1 catalysis. Thus, R658C and N423D converge on the same biochemical endpoint through different upstream defects: deficient enzyme recruitment versus deficient substrate recruitment. (fatalska2024recruitmentoftrimeric pages 10-12, fatalska2024recruitmentoftrimeric pages 3-5)

### β-cell evidence

In INS-1E β cells, approximately 75% PPP1R15B knockdown increased basal phospho-eIF2α and ATF3, lowered insulin content by 20%, and eliminated normal glucose-stimulated insulin secretion. Controls increased secretion 2.8-fold at 16.7 mmol/L glucose, whereas deficient cells showed little response; forskolin-stimulated secretion fell from approximately tenfold to fourfold. Knockdown increased apoptosis by up to 20%, involving intrinsic-pathway BH3-only proteins DP5, PUMA, and BIM. This is cellular perturbation evidence—not direct histology from affected human pancreas. (abdulkarim2015amissensemutation pages 9-11, abdulkarim2015amissensemutation pages 7-9)

### Ontology suggestions

- **GO biological processes:** response to endoplasmic-reticulum stress (GO:0034976); response to unfolded protein (GO:0006986); translational initiation (GO:0006413); regulation of translation (GO:0006417); protein dephosphorylation (GO:0006470); intrinsic apoptotic signaling (GO:0097193); insulin secretion (GO:0030073).
- **GO cellular components:** endoplasmic reticulum (GO:0005783); cytosol (GO:0005829); protein phosphatase complex (GO:0008287).
- **Cell Ontology:** pancreatic β cell (CL:0000169); neuron (CL:0000540); oligodendrocyte (CL:0000128), hepatocyte (CL:0000182), chondrocyte (CL:0000138), and erythroid cells are biologically plausible/animal-supported but not all directly demonstrated as primary human disease targets.

No MSSGM2-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or integrated multi-omics patient dataset was identified. The available molecular profiling consists chiefly of targeted expression, phosphorylation, secretion, apoptosis, interaction, NMR, HDX-MS, and structural-modeling experiments.

## 7. Anatomical structures affected

- **Primary:** brain/central nervous system, pituitary–somatic growth axis or growth tissues, and endocrine pancreas.
- **Additional:** inner ear/auditory system, axial skeleton and thorax, teeth/hair, liver, thyroid, and reproductive endocrine system.
- **Suggested UBERON:** brain UBERON:0000955; cerebral white matter UBERON:0002316; pancreas UBERON:0001264; pancreatic islet UBERON:0000006; liver UBERON:0002107; thyroid gland UBERON:0002046; inner ear UBERON:0001846; vertebral column UBERON:0001130.
- **Subcellular:** cytosolic PPP1R15B–PP1–eIF2 complex and ER-linked ISR machinery.

No consistent lateralization has been reported. CNS and growth abnormalities are generalized rather than unilateral.

## 8. Temporal development

Growth restriction and microcephaly are congenital or evident early; developmental delay emerges in childhood and remains chronic. Diabetes is not necessarily neonatal: the best-documented patients developed it at 15 and 28 years, and younger reported individuals may not yet have developed hyperglycemia. This implies age-dependent expression of the metabolic component and supports lifelong surveillance. (abdulkarim2015amissensemutation pages 9-11, stone2021monogenicandsyndromic pages 6-8)

No formal stages, remission pattern, median progression rate, or natural-history curve exists. Congenital neurodevelopmental and skeletal findings appear persistent; diabetes is chronic once established. A critical biological period likely exists during prenatal brain and skeletal development, while a practical intervention window exists before metabolic decompensation through periodic glucose/HbA1c surveillance.

## 9. Inheritance and population

Inheritance is autosomal recessive. For two heterozygous parents, each pregnancy has the standard Mendelian expectation of **25% affected, 50% carrier, and 25% unaffected/non-carrier**, assuming both variants are fully disease-causing. Both sexes can be affected. (abdulkarim2015amissensemutation pages 4-7, abdulkarim2015amissensemutation pages 3-4)

The literature supports only a handful of affected individuals; no cases-per-100,000 prevalence, annual incidence, sex ratio, geographic distribution, carrier frequency, founder population, or robust penetrance estimate is available. Reviews mention the original affected siblings and four additional patients, while another review describes four patients in two sibling pairs with Arg658Cys; discrepancies and possible overlapping reports make simple summation unsafe. (stone2021monogenicandsyndromic pages 6-8, vaneynde2022theroleof pages 6-7)

Expressivity is variable, especially for age at diabetes onset and multisystem complications. Apparent nonpenetrance of diabetes in children may instead be age dependence. Genetic anticipation is not expected for missense alleles and has not been observed.

## 10. Diagnostics

### Recommended approach

1. Recognize the combination of microcephaly, proportionate short stature or prenatal growth restriction, developmental disability, and autoimmune-negative youth/adult-onset diabetes.
2. Measure fasting glucose, HbA1c, ketones when symptomatic, C-peptide, and diabetes autoantibodies. The original index patient had HbA1c 13.0% and fasting glucose 11.4 mmol/L; residual C-peptide and modest insulin requirements supported nonautoimmune monogenic diabetes. (abdulkarim2015amissensemutation pages 4-7, abdulkarim2015amissensemutation pages 9-11)
3. Perform audiology, dental and orthopedic examination, thyroid function, liver enzymes/synthetic function, pubertal assessment, and brain MRI where neurologically indicated.
4. Confirm with a syndromic-diabetes/neurodevelopmental panel containing **PPP1R15B**, or preferably trio/parent–child **WES/WGS** when the presentation is nonspecific. The original diagnosis used exome sequencing followed by segregation analysis and Sanger/PCR-RFLP confirmation. (abdulkarim2015amissensemutation pages 4-7)
5. Phase variants and test parents. For uncertain splice variants, RNA sequencing may help; no validated MSSGM2 transcriptomic diagnostic signature exists.

CMA is appropriate when a broader developmental phenotype suggests a copy-number disorder but will generally not detect single-nucleotide PPP1R15B variants. Karyotype, FISH, mitochondrial DNA, and repeat-expansion testing are not first-line MSSGM2 tests unless another diagnosis is suspected.

### Differential diagnosis

- **Wolcott–Rallison syndrome (EIF2AK3):** usually earlier/neonatal diabetes, epiphyseal dysplasia, and recurrent acute liver failure; mechanistically involves insufficient rather than excessive eIF2α phosphorylation.
- **MEHMO syndrome (EIF2S3):** X-linked; severe intellectual disability, epilepsy, hypogonadism/hypogenitalism, microcephaly, and obesity, sometimes diabetes.
- **WFS1-related Wolfram syndrome:** juvenile diabetes with optic atrophy, deafness, and diabetes insipidus.
- Other monogenic/syndromic diabetes: **INS, PDX1, PTF1A, IER3IP1, DNAJC3, YIPF5**, mitochondrial diabetes, and chromosomal disorders.

No consensus diagnostic criteria or newborn biochemical screen exists. Cascade testing is indicated after a familial variant is established.

## 11. Outcome and prognosis

No 5- or 10-year survival, life-expectancy, mortality, hospitalization, or standardized disability data exist. The original affected siblings survived into their late twenties/early thirties, showing that p.Arg658Cys is compatible with adulthood despite substantial neurodevelopmental and metabolic morbidity. (abdulkarim2015amissensemutation pages 4-7)

Major long-term burdens likely include lifelong intellectual/developmental disability, insulin-treated diabetes and hypoglycemia, hearing impairment, skeletal deformity, and possible hepatic/endocrine complications. Frequent hypoglycemia was reported in the index patient. Prognostic factors and biomarkers have not been validated; genotype, residual phosphatase activity, developmental severity, and onset of liver disease or diabetes are plausible but unproven predictors. (abdulkarim2015amissensemutation pages 9-11)

## 12. Treatment and applications

There is no approved disease-modifying therapy, gene therapy, RNA therapy, cell therapy, or MSSGM2-specific interventional trial in the retrieved literature or ClinicalTrials.gov search.

Current real-world management is phenotype-directed:

- **Diabetes:** insulin, continuous or capillary glucose monitoring, ketone/sick-day education, individualized nutrition, and hypoglycemia prevention. Reported requirements were approximately 0.5–0.7 U/kg/day. (abdulkarim2015amissensemutation pages 4-7)
- **Development:** early developmental intervention, special education, speech/language, occupational and physical therapy.
- **Hearing:** serial audiology and hearing aids or other assistive technology.
- **Skeletal/dental:** orthopedic monitoring and treatment of kyphoscoliosis/pectus; preventive and restorative dental care.
- **Endocrine/hepatic:** monitor growth, thyroid function, puberty, glucose/HbA1c, and liver function; treat deficiencies or complications according to standard specialty guidelines.

Suggested NCIt concepts include **Insulin Therapy**, **Genetic Counseling**, **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, and **Hearing Aid**, but no MSSGM2-specific NCIt intervention term was verified.

Pharmacologic manipulation of PPP1R15 proteins or the ISR remains experimental and directionally complex. In MSSGM2, phospho-eIF2α is already excessive; PPP1R15B inhibitors such as Raphin1 would therefore be mechanistically concerning rather than rational treatment candidates. Reviews also emphasize controversy over the direct targets of guanabenz/Sephin1-class compounds. No efficacy or safety data exist in affected patients. (hicks2023theppp1r15family pages 7-9)

## 13. Prevention

The molecular disorder cannot presently be prevented by vaccination, diet, or exposure avoidance.

- **Primary/reproductive prevention:** genetic counseling, familial-variant carrier testing, preimplantation genetic testing, chorionic-villus sampling, or amniocentesis where desired.
- **Secondary prevention:** early molecular diagnosis and periodic metabolic surveillance before symptomatic hyperglycemia or ketoacidosis; assess hearing, thyroid, liver, growth, puberty, and skeletal status.
- **Tertiary prevention:** optimize glucose control while minimizing hypoglycemia; developmental and hearing support; orthopedic, dental, hepatic, and endocrine monitoring.

Population newborn screening is not currently justified by available prevalence or treatment evidence. Targeted cascade screening is appropriate in an affected family.

## 14. Other species and natural disease

No naturally occurring veterinary MSSGM2 analogue, breed association, zoonotic transmission, or cross-species infectious susceptibility is known. PPP1R15B orthologues are evolutionarily conserved in vertebrates, consistent with the conservation of eIF2α stress signaling. Relevant taxa include human **NCBI Taxon 9606** and laboratory mouse **NCBI Taxon 10090**. Exact orthologue NCBI Gene identifiers should be imported from the current NCBI/Alliance release.

## 15. Model organisms

### Mouse

Constitutive **Ppp1r15b/CReP knockout mice** are approximately half normal size at birth, pale, fail to nurse, and die neonatally; none in the cited series survived beyond postnatal day 1. Their severe phenotype includes hematopoietic defects and demonstrates that complete loss is more damaging than the surviving human hypomorphic missense alleles. Genetic reduction of phosphorylatable eIF2α through an eIF2α-Ser51 alteration rescued body size and red-cell counts, strongly supporting excessive eIF2α phosphorylation as the causal axis. (hicks2023theppp1r15family pages 7-9)

### Cellular and biochemical models

- HEK293T reconstitution and co-immunoprecipitation defined impaired PP1 binding by R658C.
- INS-1E β-cell knockdown modeled impaired insulin secretion and apoptosis.
- Purified-complex assays, HDX-MS, NMR, mutagenesis, and AlphaFold-based structural modeling defined eIF2 recruitment and the N423D defect. (abdulkarim2015amissensemutation pages 7-9, fatalska2024recruitmentoftrimeric pages 10-12, fatalska2024recruitmentoftrimeric pages 3-5)

These systems are valuable for variant interpretation and ISR-target discovery but do not reproduce human brain development, lifelong metabolic progression, or whole-organism dosage effects. No patient-derived iPSC, cerebral organoid, pancreatic organoid, zebrafish, Drosophila, or CRISPR knock-in MSSGM2 model was identified.

## Evidence assessment and recent developments

The disease evidence is dominated by small human case series plus strong functional validation. The most important recent advance is not a large clinical cohort but the 2024 resolution of how PPP1R15B recruits intact eIF2 and how distinct disease alleles disrupt either enzyme or substrate engagement. This strengthens the causal interpretation of PPP1R15B variants while also showing why variant-specific functional assays are necessary. The 2025 syndromic-diabetes review continues to characterize MSSGM2 as a rare autosomal-recessive disorder with late-onset impaired glucose metabolism and multisystem involvement, but it supplies no new natural-history cohort or treatment trial. (gobble2025neonatalandsyndromic pages 7-8, fatalska2024recruitmentoftrimeric pages 10-12)

### Key evidence limitations

1. Patient numbers are too small for defensible percentages beyond within-family observations.
2. Some later clinical features are reported only in reviews and cannot be assigned confidently to individual patients.
3. Diabetes may be age dependent, complicating classification of young PPP1R15B-positive patients.
4. There are no disease-specific guidelines, registries, prospective natural-history studies, validated biomarkers, patient-reported outcomes, or therapeutic trials.
5. Ontology and database identifiers should be version-checked before production ingestion, particularly MONDO, Orphanet, ClinVar, gnomAD, HGNC, and NCIt mappings.

References

1. (abdulkarim2015amissensemutation pages 1-2): Baroj Abdulkarim, Marc Nicolino, Mariana Igoillo-Esteve, Mathilde Daures, Sophie Romero, Anne Philippi, Valérie Senée, Miguel Lopes, Daniel A Cunha, Heather P Harding, Céline Derbois, Nathalie Bendelac, Andrew T Hattersley, Décio L Eizirik, David Ron, Miriam Cnop, and Cécile Julier. A missense mutation in ppp1r15b causes a syndrome including diabetes, short stature, and microcephaly. JournalArticle, Aug 2015. URL: https://doi.org/10.17863/cam.10390, doi:10.17863/cam.10390. This article has 123 citations.

2. (fatalska2024recruitmentoftrimeric pages 10-12): Agnieszka Fatalska, George Hodgson, Stefan M.V. Freund, Sarah L. Maslen, Tomos Morgan, Sigurdur R. Thorkelsson, Marjon van Slegtenhorst, Sonja Lorenz, Antonina Andreeva, Laura Donker Kaat, and Anne Bertolotti. Recruitment of trimeric eif2 by phosphatase non-catalytic subunit ppp1r15b. Feb 2024. URL: https://doi.org/10.1016/j.molcel.2023.12.011, doi:10.1016/j.molcel.2023.12.011. This article has 8 citations and is from a highest quality peer-reviewed journal.

3. (fatalska2024recruitmentoftrimeric pages 8-10): Agnieszka Fatalska, George Hodgson, Stefan M.V. Freund, Sarah L. Maslen, Tomos Morgan, Sigurdur R. Thorkelsson, Marjon van Slegtenhorst, Sonja Lorenz, Antonina Andreeva, Laura Donker Kaat, and Anne Bertolotti. Recruitment of trimeric eif2 by phosphatase non-catalytic subunit ppp1r15b. Feb 2024. URL: https://doi.org/10.1016/j.molcel.2023.12.011, doi:10.1016/j.molcel.2023.12.011. This article has 8 citations and is from a highest quality peer-reviewed journal.

4. (stone2021monogenicandsyndromic pages 6-8): Stephen I. Stone, Damien Abreu, Janet B. McGill, and Fumihiko Urano. Monogenic and syndromic diabetes due to endoplasmic reticulum stress. Jan 2021. URL: https://doi.org/10.1016/j.jdiacomp.2020.107618, doi:10.1016/j.jdiacomp.2020.107618. This article has 46 citations and is from a peer-reviewed journal.

5. (gobble2025neonatalandsyndromic pages 7-8): McKinlee R. S. Gobble and Stephen I. Stone. Neonatal and syndromic forms of diabetes. Current Diabetes Reports, Mar 2025. URL: https://doi.org/10.1007/s11892-024-01567-x, doi:10.1007/s11892-024-01567-x. This article has 4 citations and is from a peer-reviewed journal.

6. (hicks2023theppp1r15family pages 7-9): Danielle Hicks, Krithika Giresh, Lisa A. Wrischnik, and Douglas C. Weiser. The ppp1r15 family of eif2-alpha phosphatase targeting subunits (gadd34 and crep). International Journal of Molecular Sciences, 24:17321, Dec 2023. URL: https://doi.org/10.3390/ijms242417321, doi:10.3390/ijms242417321. This article has 46 citations.

7. (abdulkarim2015amissensemutation pages 4-7): Baroj Abdulkarim, Marc Nicolino, Mariana Igoillo-Esteve, Mathilde Daures, Sophie Romero, Anne Philippi, Valérie Senée, Miguel Lopes, Daniel A Cunha, Heather P Harding, Céline Derbois, Nathalie Bendelac, Andrew T Hattersley, Décio L Eizirik, David Ron, Miriam Cnop, and Cécile Julier. A missense mutation in ppp1r15b causes a syndrome including diabetes, short stature, and microcephaly. JournalArticle, Aug 2015. URL: https://doi.org/10.17863/cam.10390, doi:10.17863/cam.10390. This article has 123 citations.

8. (abdulkarim2015amissensemutation pages 3-4): Baroj Abdulkarim, Marc Nicolino, Mariana Igoillo-Esteve, Mathilde Daures, Sophie Romero, Anne Philippi, Valérie Senée, Miguel Lopes, Daniel A Cunha, Heather P Harding, Céline Derbois, Nathalie Bendelac, Andrew T Hattersley, Décio L Eizirik, David Ron, Miriam Cnop, and Cécile Julier. A missense mutation in ppp1r15b causes a syndrome including diabetes, short stature, and microcephaly. JournalArticle, Aug 2015. URL: https://doi.org/10.17863/cam.10390, doi:10.17863/cam.10390. This article has 123 citations.

9. (fatalska2024recruitmentoftrimeric pages 3-5): Agnieszka Fatalska, George Hodgson, Stefan M.V. Freund, Sarah L. Maslen, Tomos Morgan, Sigurdur R. Thorkelsson, Marjon van Slegtenhorst, Sonja Lorenz, Antonina Andreeva, Laura Donker Kaat, and Anne Bertolotti. Recruitment of trimeric eif2 by phosphatase non-catalytic subunit ppp1r15b. Feb 2024. URL: https://doi.org/10.1016/j.molcel.2023.12.011, doi:10.1016/j.molcel.2023.12.011. This article has 8 citations and is from a highest quality peer-reviewed journal.

10. (abdulkarim2015amissensemutation pages 9-11): Baroj Abdulkarim, Marc Nicolino, Mariana Igoillo-Esteve, Mathilde Daures, Sophie Romero, Anne Philippi, Valérie Senée, Miguel Lopes, Daniel A Cunha, Heather P Harding, Céline Derbois, Nathalie Bendelac, Andrew T Hattersley, Décio L Eizirik, David Ron, Miriam Cnop, and Cécile Julier. A missense mutation in ppp1r15b causes a syndrome including diabetes, short stature, and microcephaly. JournalArticle, Aug 2015. URL: https://doi.org/10.17863/cam.10390, doi:10.17863/cam.10390. This article has 123 citations.

11. (abdulkarim2015amissensemutation pages 7-9): Baroj Abdulkarim, Marc Nicolino, Mariana Igoillo-Esteve, Mathilde Daures, Sophie Romero, Anne Philippi, Valérie Senée, Miguel Lopes, Daniel A Cunha, Heather P Harding, Céline Derbois, Nathalie Bendelac, Andrew T Hattersley, Décio L Eizirik, David Ron, Miriam Cnop, and Cécile Julier. A missense mutation in ppp1r15b causes a syndrome including diabetes, short stature, and microcephaly. JournalArticle, Aug 2015. URL: https://doi.org/10.17863/cam.10390, doi:10.17863/cam.10390. This article has 123 citations.

12. (vaneynde2022theroleof pages 6-7): Pieter Vaneynde, Iris Verbinnen, and Veerle Janssens. The role of serine/threonine phosphatases in human development: evidence from congenital disorders. Frontiers in Cell and Developmental Biology, Oct 2022. URL: https://doi.org/10.3389/fcell.2022.1030119, doi:10.3389/fcell.2022.1030119. This article has 14 citations.

## Artifacts

- [Edison artifact artifact-00](Microcephaly_Short_Stature_and_Impaired_Glucose_Metabolism_2-deep-research-falcon_artifacts/artifact-00.md)