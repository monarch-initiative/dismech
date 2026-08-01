---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-08-01T17:19:26.451043'
end_time: '2026-08-01T17:19:26.454843'
duration_seconds: 0.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Choroideremia-Deafness-Obesity Syndrome
  mondo_id: ''
  category: Genetic
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
  path: Choroideremia-Deafness-Obesity_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Choroideremia-Deafness-Obesity Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Choroideremia-Deafness-Obesity Syndrome** covering all of the
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
- **Disease Name:** Choroideremia-Deafness-Obesity Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Choroideremia-Deafness-Obesity Syndrome** covering all of the
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


# Choroideremia–Deafness–Obesity Syndrome (Ayazi Syndrome)

## Executive summary

Choroideremia–deafness–obesity syndrome is an exceptionally rare **X-linked contiguous-gene deletion disorder of Xq21**, historically called **Ayazi syndrome**. Its defining features are choroideremia, congenital deafness, and obesity. The original evidence came from affected males in a three-generation family; subsequent molecular work attributed the phenotype to submicroscopic Xq21 deletions. Modern series show that deletion content—and therefore phenotype—varies substantially. **CHM** loss explains choroideremia, while deletion of **POU3F4** is the best-established explanation for hearing loss. The gene or combination of genes responsible for obesity remains unresolved. Larger deletions may add intellectual disability or other neurodevelopmental abnormalities. Reported Xq21 deletions have generally been approximately 5.2–16 Mb, although a 2024 report described a 3.7-Mb deletion affecting CHM exons 4–15 and completely deleting several neighboring genes. (bonati2024contiguousgenesyndromes pages 13-14, bonati2024contiguousgenesyndromes pages 19-21)

The evidence base is composed almost entirely of pedigrees and isolated deletion cases; syndrome-specific prevalence, natural-history, treatment-response, survival, and quality-of-life statistics do not exist. Information below therefore distinguishes **direct syndrome evidence** from evidence extrapolated from nonsyndromic CHM-related choroideremia or POU3F4-related deafness.

| domain | direct syndrome evidence | implicated locus/gene | confidence/limitations |
|---|---|---|---|
| Xq21 contiguous deletion architecture | Ayazi syndrome is best understood as a rare X-linked contiguous-gene deletion phenotype in Xq21. A 2024 review states the original report was a three-generation family with males showing choroideremia, obesity, and congenital deafness; reported Xq21 deletions in the literature ranged about 5.2–16 Mb, and the 2024 case had a 3.7 Mb deletion including part of **CHM** plus multiple neighboring genes (bonati2024contiguousgenesyndromes pages 13-14) | Xq21; **CHM, POU3F4, CYLC1, RPS6KA6, HDX, APOOL, SATL1, ZNF711, POF1B** | Moderate confidence for syndrome architecture; evidence is from very few families/cases and mostly review-level synthesis of rare reports. No supported standalone MONDO/ICD identifier should be asserted from current evidence. |
| Retinal phenotype (direct + component extrapolation) | Direct syndrome evidence includes choroideremia as a cardinal feature in the original Ayazi family and later Xq21 deletion cases (bonati2024contiguousgenesyndromes pages 13-14, bonati2024contiguousgenesyndromes pages 19-21). Component-disease evidence shows **CHM** loss causes REP1 deficiency with defective Rab prenylation, impaired intracellular trafficking, and progressive degeneration of retinal pigment epithelium, photoreceptors, and choriocapillaris (cehajickapetanovic2024genetherapyfor pages 23-25, ashok2024updatesonproteinprenylation pages 9-11) | **CHM / REP1** | High confidence that CHM deletion explains the retinal disease component; mechanistic detail is extrapolated from nonsyndromic choroideremia rather than syndrome-specific experiments. |
| Hearing phenotype (direct + component extrapolation) | Direct syndrome evidence includes congenital deafness as a cardinal Ayazi feature and hearing loss in Xq21 deletion syndrome (bonati2024contiguousgenesyndromes pages 13-14). Component-disease evidence supports **POU3F4** haploinsufficiency as the likely major driver of DFNX2/DFN3-like hearing loss, often sensorineural or mixed, with inner-ear malformation/stapes fixation and prelingual progression in affected males (bonati2024contiguousgenesyndromes pages 13-14) | **POU3F4** | High confidence for POU3F4 as the major hearing-loss gene in deletions spanning this region; exact syndrome-level audiologic spectrum remains sparsely documented. |
| Obesity | Obesity is part of the defining triad in the original family and is cited in later summaries of the syndrome (bonati2024contiguousgenesyndromes pages 13-14, bonati2024contiguousgenesyndromes pages 19-21). However, currently retrieved evidence does not validate a single obesity gene within the Xq21 deleted segment as causative. | Unresolved within Xq21 deletion interval | Low-to-moderate confidence for obesity as a phenotype; low confidence for gene attribution. Obesity likely reflects contiguous-gene effects or unclarified modifier biology. |
| Neurodevelopmental/cognitive findings in larger deletions | Some Xq21 deletion reports include mental retardation/intellectual disability or broader neurodevelopmental involvement in addition to choroideremia and deafness, particularly in larger deletions (bonati2024contiguousgenesyndromes pages 19-21, bonati2024contiguousgenesyndromes pages 13-14) | Possible contributors include **RPS6KA6, ZNF711** and/or larger deletion burden | Moderate confidence that neurodevelopmental findings can occur in expanded Xq21 deletions; low confidence for assigning causality to any single gene from the present evidence. |
| Inheritance | The syndrome was proposed as a novel **X-linked** disorder based on the original pedigree and is consistently reviewed as X-linked contiguous-gene deletion disease affecting males (bonati2024contiguousgenesyndromes pages 13-14) | X chromosome, Xq21 | High confidence for X-linked inheritance; penetrance/expressivity estimates are unavailable because case numbers are extremely small. |
| Diagnostic approach | Best-supported modern approach is genomic copy-number detection for unexplained congenital hearing loss with syndromic features, especially chromosomal microarray or CNV-sensitive NGS/WES/WGS; the 2024 case was identified after neonatal hearing loss work-up using a multigene NGS panel, and the review emphasizes cytogenomic microarray for unexplained hearing loss (bonati2024contiguousgenesyndromes pages 13-14) | CNV analysis across **Xq21**, with attention to **CHM** and **POU3F4** | Moderate-to-high confidence. Functional ophthalmic/audiologic phenotyping is still required, but no syndrome-specific biomarker was found. |
| Treatment status | No syndrome-specific disease-modifying therapy was identified. Current care is component-based: retinal surveillance/low-vision support for choroideremia, hearing rehabilitation, and standard obesity management. CHM-only gene therapy is active translationally, but 2024 REGENERATE showed no statistically significant BCVA benefit at 24 months and reported six serious adverse events in treated eyes (cehajickapetanovic2024genetherapyfor pages 21-23, cehajickapetanovic2024genetherapyfor pages 27-29) | Supportive multidisciplinary care; experimental **AAV2-REP1/CHM** therapy applies to retinal component only | High confidence that there is no established syndrome-specific therapy. Important limitation: CHM gene therapy trials target nonsyndromic/CHM-confirmed retinal disease, not the full Ayazi contiguous-deletion syndrome. |


*Table: This table summarizes the strongest currently retrieved evidence for choroideremia-deafness-obesity (Ayazi) syndrome and separates direct syndrome evidence from extrapolation based on CHM and POU3F4 component disorders. It is useful for quickly auditing what is established, what is inferred, and where evidence gaps remain.*

## 1. Disease information

### Definition and classification

This is a **genetic, syndromic copy-number disorder**, not a single-nucleotide monogenic syndrome. Hemizygous males carrying an Xq21 deletion that includes relevant dosage-sensitive genes develop a combination of retinal degeneration, hearing loss, obesity, and—depending on deletion extent—additional manifestations. The original Ayazi pedigree established the choroideremia–obesity–congenital-deafness triad and X-linked segregation. Later deletion mapping placed the critical region between markers **DXYS1 and DXS72**. (bonati2024contiguousgenesyndromes pages 13-14)

**Synonyms:**

- Choroideremia–deafness–obesity syndrome
- Choroideremia, congenital deafness, and obesity
- Ayazi syndrome
- Xq21 deletion syndrome, when used more broadly
- Syndromic choroideremia due to an Xq21 contiguous-gene deletion

### Identifiers

No standalone **MONDO, MeSH, ICD-10, or ICD-11 identifier** for the complete triad could be verified from the retrieved literature. It should not be assigned the identifier for isolated choroideremia or isolated POU3F4 deafness. A knowledge base should represent it provisionally as an **Xq21 contiguous-gene deletion syndrome** and cross-reference its components—CHM-related choroideremia and POU3F4-related X-linked deafness. The retrieved evidence likewise did not establish a unique OMIM or Orphanet disease number for the exact triad.

### Evidence provenance

The record is derived from **aggregated disease-level literature based on individual pedigrees and case reports**, not from electronic-health-record cohorts or population registries. The most current syndrome-focused synthesis is Bonati et al., *Genes*, published May 2024, DOI: https://doi.org/10.3390/genes15060677. (bonati2024contiguousgenesyndromes pages 13-14)

## 2. Etiology, risk, and protective factors

### Causal factor

The primary cause is a **constitutional germline deletion of Xq21**. It is a loss-of-function/copy-number mechanism involving multiple adjacent genes rather than an infectious, toxic, dietary, or autoimmune cause. Relevant deleted genes reported in a 2024 3.7-Mb case included part of **CHM** (exons 4–15) and complete loss of **POU3F4, CYLC1, RPS6KA6, HDX, APOOL, SATL1, ZNF711,** and **POF1B**. Historical deletions vary from about 5.2 to 16 Mb. (bonati2024contiguousgenesyndromes pages 13-14)

### Genetic risk

- **Male hemizygosity** for the deletion is the principal risk factor.
- A carrier mother gives each son a 50% probability of inheriting the deleted X chromosome and each daughter a 50% probability of being a carrier.
- Female carriers may exhibit variable retinal manifestations because of X-chromosome inactivation, as is known for CHM deficiency, but syndrome-specific penetrance in women is not quantified. (cehajickapetanovic2024genetherapyfor pages 23-25)
- Larger deletions plausibly increase the probability of neurodevelopmental manifestations; this is a deletion-content correlation, not a validated prognostic rule. (bonati2024contiguousgenesyndromes pages 19-21, bonati2024contiguousgenesyndromes pages 13-14)

No susceptibility loci, modifier genes, protective alleles, founder variants, anticipation, or confirmed germline mosaicism have been demonstrated for the complete syndrome.

### Environmental and protective factors

No environmental exposure causes or prevents the constitutional deletion. Diet, physical activity, and weight-management services may modify **downstream obesity and cardiometabolic risk**, but they do not alter disease occurrence. Avoidance of excessive noise and ototoxic medication is prudent for residual hearing, but syndrome-specific protective effects have not been measured. No disease-specific gene–environment interaction has been established.

## 3. Phenotypes

### Core phenotype inventory

| Phenotype | Type and course | Evidence/frequency | Suggested HPO annotation |
|---|---|---|---|
| Choroideremia/retinal degeneration | Clinical sign; childhood-onset nyctalopia and peripheral-field loss in CHM disease, followed by progressive centripetal degeneration and possible adult blindness | Defining feature in the original family; no syndrome-specific percentage | Choroideremia; retinal dystrophy; nyctalopia; constricted visual fields; progressive visual loss |
| Congenital or prelingual deafness | Clinical sign; commonly severe sensorineural or mixed loss; inner-ear malformation or stapes fixation may occur when POU3F4 is deleted | Defining feature; no reliable percentage | Congenital hearing impairment; sensorineural hearing impairment; mixed hearing loss; cochlear malformation |
| Obesity | Physical/metabolic manifestation; onset and trajectory are insufficiently documented | Defining original feature, but penetrance and gene attribution are unknown | Obesity (**HP:0001513**); increased body weight |
| Intellectual disability/developmental delay | Neurodevelopmental manifestation in some larger Xq21 deletions, not obligatory in the Ayazi triad | Case-level evidence only | Global developmental delay; intellectual disability; speech delay |
| Stapes fixation/perilymphatic-gusher risk | Structural/operative feature associated with POU3F4 deletion | Component-gene inference; not quantified in Ayazi cases | Stapes ankylosis; inner-ear malformation; abnormal cochlear morphology |

The retinal component is a diffuse, progressive degeneration of **retinal pigment epithelium (RPE), photoreceptors, and choriocapillaris**, producing rod–cone dysfunction and progressive peripheral-field loss. (cehajickapetanovic2024genetherapyfor pages 23-25, ashok2024updatesonproteinprenylation pages 9-11)

The hearing phenotype is mechanistically consistent with **POU3F4 haploinsufficiency**: sensorineural or mixed hearing loss, cochlear hypoplasia/incomplete-partition-type morphology, and/or stapes fixation, usually congenital or prelingual in males. (bonati2024contiguousgenesyndromes pages 13-14)

### Severity, frequency, and quality of life

Severity is expected to be high because dual sensory impairment compromises communication, education, mobility, independence, and employment; obesity adds cardiometabolic and psychosocial burden. However, no EQ-5D, SF-36, PROMIS, or syndrome-specific patient-reported-outcome study was found. Percent frequencies cannot be inferred from a defining triad observed in one pedigree. For knowledge-base purposes, core findings should be marked **“characteristic, frequency unknown,”** not “100%.”

## 4. Genetic and molecular information

### Principal genes

1. **CHM**, encoding Rab escort protein-1 (**REP1**), is the established causal gene for the retinal phenotype. Deletion produces gene-dosage loss and functional REP1 deficiency. (cehajickapetanovic2024genetherapyfor pages 23-25, ashok2024updatesonproteinprenylation pages 9-11)
2. **POU3F4**, encoding a POU-domain transcription factor important in middle- and inner-ear development, is the established major gene for the deafness phenotype. (bonati2024contiguousgenesyndromes pages 13-14)
3. **RPS6KA6, ZNF711**, and other genes may contribute to cognitive or broader developmental findings when included, but syndrome-specific causal partitioning is incomplete. (bonati2024contiguousgenesyndromes pages 19-21, bonati2024contiguousgenesyndromes pages 13-14)
4. No individual deleted gene has been validated as the cause of obesity in this syndrome.

### Variant class and interpretation

The canonical pathogenic lesion is a **germline hemizygous structural deletion/CNV**. A deletion removing coding exons or an entire dosage-sensitive gene is expected to cause loss of function. Classification should follow ACMG/ClinGen CNV standards using deletion size, gene content, inheritance, phenotype match, and segregation. Exact breakpoints must be recorded in HGVS/ISCN on the reference assembly used by the laboratory.

Population allele frequency is expected to be extremely low, but no syndrome-specific gnomAD-SV/TOPMed frequency was recovered. These are not somatic variants. Missense, isolated splice, or nonsense variants in CHM or POU3F4 can cause their respective component diseases but do **not** by themselves establish the full Ayazi syndrome.

### Epigenetics and modifiers

Female expression may be modified by X-inactivation, but no syndrome-specific methylation signature, histone abnormality, modifier locus, or validated epigenetic biomarker is known. No molecular evidence supports anticipation.

## 5. Environmental, lifestyle, and infectious information

No toxin, radiation, pollutant, occupation, infection, or lifestyle behavior is known to initiate the syndrome. Environmental influences operate only on downstream morbidity:

- Caloric intake and activity affect obesity severity.
- Noise and ototoxic exposure may further reduce residual hearing.
- Accessibility, early language exposure, low-vision adaptation, and educational support strongly influence functional outcome, although no Ayazi-specific intervention study exists.
- Infectious agents and zoonotic transmission are not applicable.

## 6. Mechanism and pathophysiology

### Retinal causal chain

**Xq21 deletion → CHM loss → REP1 deficiency → reduced chaperoning of unprenylated Rab GTPases to Rab geranylgeranyl transferase/GGTase-II → defective Rab geranylgeranylation and membrane anchoring → impaired vesicular trafficking and cellular homeostasis → RPE deposit accumulation/dysfunction → secondary photoreceptor and choriocapillaris degeneration → nyctalopia, peripheral-field constriction, and progressive blindness.** (cehajickapetanovic2024genetherapyfor pages 23-25, ashok2024updatesonproteinprenylation pages 9-11)

A useful direct summary from the 2024 prenylation review is: **“REP-1 functions to chaperone unprenylated Rab proteins and present them to GGTase-II for geranylgeranylation.”** The affected subcellular system is therefore the cytosol-to-organelle membrane trafficking apparatus. (ashok2024updatesonproteinprenylation pages 9-11)

**Suggested GO terms:** Rab protein geranylgeranylation; protein lipidation; intracellular vesicle-mediated transport; endosomal transport; phagosome maturation; photoreceptor maintenance; retinal homeostasis. **Suggested cellular components:** cytosol, endosome, lysosome, transport vesicle, plasma/organelle membrane.

**Suggested cell types:** retinal pigment epithelial cell; rod photoreceptor; cone photoreceptor; choroidal endothelial cell. The best-supported upstream lesion is in Rab prenylation/trafficking; cell loss is downstream.

### Auditory causal chain

**Xq21 deletion → POU3F4 haploinsufficiency → abnormal transcriptional control in otic mesenchyme and inner-ear neurodevelopment → deficient cochlear/modiolar architecture and abnormal separation from the internal auditory canal, sometimes with stapes fixation → congenital/prelingual mixed or sensorineural hearing loss and operative perilymphatic-gusher risk.** POU3F4 also participates in neural stem-cell proliferation, inner-ear neurogenesis, and inner radial-bundle formation. (bonati2024contiguousgenesyndromes pages 13-14)

**Suggested GO terms:** inner-ear morphogenesis; cochlea development; auditory receptor-cell development; neuron differentiation; transcription regulation. **Suggested cell types:** otic mesenchyme cell, spiral-ganglion neuron, cochlear supporting cell, auditory hair cell. The deletion primarily disrupts developmental patterning; sensory dysfunction is downstream.

### Obesity and neurodevelopment

No validated molecular chain connects a specific deleted gene to obesity. It should be represented as **“contiguous-deletion-associated obesity; mechanism unknown.”** Intellectual disability in some larger deletions likely reflects loss of additional dosage-sensitive genes, but assigning it specifically to RPS6KA6 or ZNF711 from the current syndrome evidence would be premature. (bonati2024contiguousgenesyndromes pages 19-21, bonati2024contiguousgenesyndromes pages 13-14)

### Omics and advanced technologies

No syndrome-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omic profile was identified. Available mechanistic work concerns CHM-deficient retinal models or POU3F4 auditory models rather than the complete deletion syndrome. There is likewise no syndrome-wide CRISPR screen.

## 7. Anatomical structures affected

- **Eye:** retina, RPE, photoreceptor layer, choroid, and choriocapillaris; typically bilateral and progressive. Suggested UBERON labels: retina, retinal pigment epithelium, choroid, photoreceptor layer. (cehajickapetanovic2024genetherapyfor pages 23-25, ashok2024updatesonproteinprenylation pages 9-11)
- **Ear:** bilateral middle/inner-ear structures, particularly cochlea, modiolus, internal auditory canal interface, and stapes; involvement can produce mixed conductive–sensorineural loss. Suggested UBERON labels: cochlea, modiolus, stapes, inner ear, spiral ganglion. (bonati2024contiguousgenesyndromes pages 13-14)
- **Metabolic/body-composition system:** adipose mass is increased, but a specific depot or cellular lesion has not been established.
- **Central nervous system:** variably involved in larger deletions associated with developmental delay or intellectual disability. (bonati2024contiguousgenesyndromes pages 19-21)
- **Subcellular retinal sites:** cytosolic REP1–Rab complex, GGTase-II machinery, transport-vesicle and organelle membranes.

## 8. Temporal development

Hearing loss is generally **congenital or prelingual**, making neonatal and early-childhood diagnosis critical. The retinal disease is chronic and progressive: nonsyndromic CHM evidence indicates childhood nyctalopia and peripheral-field loss, followed by gradual centripetal degeneration and potential blindness in adulthood. The REGENERATE report states that choroideremia **“begins in childhood with nyctalopia and loss of peripheral vision, and gradually progresses to blindness in adulthood.”** (cehajickapetanovic2024genetherapyfor pages 23-25)

Obesity onset was not sufficiently reported to define a neonatal, childhood, or adolescent pattern. The condition is lifelong; spontaneous remission is not expected. Critical intervention windows are early hearing/language rehabilitation and retinal surveillance while viable central retina remains, although no Ayazi-specific window has been validated.

## 9. Inheritance and population

### Inheritance

The pattern is **X-linked**, usually described as X-linked recessive in affected pedigrees. Hemizygous males are most severely affected; heterozygous women may be asymptomatic or variably manifesting because of X-inactivation. (bonati2024contiguousgenesyndromes pages 13-14, cehajickapetanovic2024genetherapyfor pages 23-25)

Penetrance and expressivity cannot be numerically estimated. Expressivity is demonstrably variable across Xq21 deletions because deletion size and gene content vary. No anticipation or confirmed founder effect is known.

### Epidemiology

The complete syndrome is likely **ultra-rare**, with only a very small number of pedigrees/cases described; no incidence, sex ratio, ethnic enrichment, geographic distribution, or carrier-frequency estimate exists. General CHM disease—not the full syndrome—has been estimated at about **1 in 50,000**, and this number must not be used as the prevalence of Ayazi syndrome. (cehajickapetanovic2024genetherapyfor pages 23-25)

## 10. Diagnostics

### Clinical assessment

A diagnosis should be considered in a male with congenital/prelingual hearing loss plus retinal dystrophy, obesity, developmental abnormalities, or an X-linked family history.

**Ophthalmic tests:** dilated examination, color fundus photography, fundus autofluorescence, optical coherence tomography, visual fields, microperimetry, dark adaptation, and full-field electroretinography. The expected pattern is bilateral chorioretinal atrophy with progressive loss of viable autofluorescent RPE.

**Audiologic/otologic tests:** newborn hearing screen, age-appropriate pure-tone or behavioral audiometry, tympanometry, otoacoustic emissions, auditory-brainstem responses, and temporal-bone CT/MRI. Imaging should specifically assess POU3F4-associated inner-ear malformation and stapes anatomy before surgery. POU3F4 deletion can create a perilymphatic-gusher hazard during stapes or cochlear-implant surgery. (bonati2024contiguousgenesyndromes pages 13-14)

**Metabolic assessment:** serial BMI/BMI-for-age, waist measurement, blood pressure, fasting lipid profile, glucose/HbA1c, liver enzymes, sleep-apnea assessment, and nutrition/activity review. These assess consequences rather than diagnose the syndrome.

### Genetic-testing strategy

1. **First line:** chromosomal microarray or another validated genome-wide CNV assay.
2. **If a hearing-loss/retinal panel is used:** ensure exon-level deletion/duplication calling across CHM, POU3F4, and Xq21. A 2024 patient was discovered through a multigene NGS work-up after neonatal hearing loss. (bonati2024contiguousgenesyndromes pages 13-14)
3. **Breakpoint resolution:** CNV-sensitive WGS is preferred when array/panel boundaries are unclear or a complex rearrangement is suspected.
4. **Confirmation and family studies:** qPCR, MLPA, ddPCR, or targeted array/FISH, followed by maternal testing and cascade testing.
5. Conventional karyotyping may miss a submicroscopic deletion; mitochondrial testing and repeat-expansion analysis are not routine unless another differential is suspected.

### Differential diagnosis

Important alternatives include isolated CHM-related choroideremia; isolated POU3F4-related DFNX2/DFN3; Usher syndrome; Alström syndrome; Bardet–Biedl syndrome; CHARGE syndrome; mitochondrial diabetes/deafness disorders; and larger Xq21 deletion phenotypes with intellectual disability. The distinguishing feature is demonstration of an Xq21 deletion spanning the relevant genes.

No universally accepted syndrome-specific clinical diagnostic criteria exist. Molecular confirmation is therefore central.

## 11. Outcome and prognosis

There are no syndrome-specific survival curves, mortality estimates, five- or ten-year outcomes, or validated prognostic biomarkers. Life expectancy has not been shown to be intrinsically shortened, but obesity-related cardiometabolic disease could affect long-term health.

The major expected morbidity is cumulative dual-sensory disability: congenital hearing impairment affects language and education, while progressive retinal degeneration subsequently restricts mobility and independence. Visual prognosis depends on age and residual retinal area; auditory function depends on malformation severity and rehabilitation. Deletion size/content may predict additional developmental disability, but no formal model exists. Spontaneous recovery of the genetic deficits is not expected.

## 12. Treatment and current applications

### Current real-world management

No approved therapy treats the entire contiguous-gene syndrome. Management should be multidisciplinary:

- **Hearing:** early amplification, speech/language therapy, educational accommodations, sign-language access, and consideration of cochlear implantation. Temporal-bone imaging and an experienced implant team are essential because POU3F4-related anatomy can complicate surgery.
- **Vision:** regular inherited-retinal-disease review, refractive correction, low-vision services, orientation/mobility training, assistive technology, school/work accommodations, and management of treatable ocular complications.
- **Obesity:** individualized nutrition, physical activity adapted for dual sensory impairment, behavioral therapy, sleep and cardiometabolic screening, and standard evidence-based anti-obesity pharmacotherapy or bariatric evaluation when otherwise indicated. No genotype-specific pharmacotherapy is established.
- **Development:** neuropsychological assessment, early intervention, occupational/physical therapy, and individualized educational planning.
- **Genetics:** counseling and cascade testing.

Suggested NCIt intervention labels include **Genetic Counseling, Hearing Aid, Cochlear Implantation, Low Vision Rehabilitation, Nutrition Therapy, Behavioral Therapy, Physical Activity Intervention,** and **Gene Transfer Therapy**.

### Experimental retinal gene therapy

AAV-mediated REP1 replacement addresses only the **CHM retinal component**, not deafness, obesity, or effects of other deleted genes. In the 2024 phase-II REGENERATE study (NCT02407678; ISRCTN15602229), 30 adult males received up to **1 × 10¹¹ vector particles** by subretinal injection. At 24 months, comparative BCVA change was not significantly different: treated eyes lost 2.63 letters versus a 2.67-letter gain in control eyes in the full cohort; the reported *p* value was 0.08. Treated eyes had greater visual-field loss, possibly surgery-related. Six serious adverse events occurred in four participants—one surgery-related, two inflammation-related with clinically significant BCVA reduction, and three central-retinal-sensitivity events in one participant. The investigators concluded that no discernible efficacy signal was demonstrated over 24 months. (cehajickapetanovic2024genetherapyfor pages 21-23, cehajickapetanovic2024genetherapyfor pages 27-29)

A particularly important abstract statement is: **“No evidence of possible efficacy of the intervention was observed.”** The slow natural decline of control-eye acuity limited endpoint sensitivity. (cehajickapetanovic2024genetherapyfor pages 21-23)

Other CHM-only studies retrieved included completed subretinal gene-therapy trials NCT01461213, NCT02077361, NCT02341807, NCT02553135, NCT02671539, NCT03496012, and NCT03507686; active-not-recruiting intravitreal 4D-110 study NCT04483440; and an optogenetic study including choroideremia, NCT06460844. None was designed specifically for Ayazi syndrome. One earlier NCT02341807 cohort included 15 participants; most returned to within 15 letters of baseline acuity, but this does not establish efficacy for the contiguous-deletion syndrome. (cehajickapetanovic2024genetherapyfor pages 27-29)

## 13. Prevention

The constitutional deletion cannot be prevented through vaccination, lifestyle change, or environmental control.

- **Primary genetic prevention/reproductive options:** carrier testing, reproductive counseling, prenatal diagnosis after an informative familial deletion is identified, and preimplantation genetic testing for a known familial CNV.
- **Secondary prevention:** newborn hearing screening, early etiologic testing for unexplained male congenital hearing loss, cascade testing, and presymptomatic retinal surveillance in at-risk boys.
- **Tertiary prevention:** early hearing rehabilitation, visual rehabilitation, obesity/cardiometabolic risk reduction, avoidance of unnecessary ototoxic exposures, and operative planning to reduce gusher-related complications.

Population-wide newborn genomic screening is not established. Targeted family-based testing is more appropriate given the extreme rarity.

## 14. Other species and natural disease

No naturally occurring veterinary disorder equivalent to the complete CHM–POU3F4–obesity Xq21 deletion syndrome was identified. The condition is not infectious, transmissible, or zoonotic. CHM and POU3F4 orthologs are evolutionarily conserved, supporting comparative mechanistic research, but component-gene phenotypes in animals should not be labeled natural Ayazi syndrome.

## 15. Model organisms and experimental systems

No single model was found that reproduces the complete contiguous deletion and its full retinal–auditory–obesity phenotype.

**Component models include:**

- CHM/REP1-deficient retinal cell models, including RPE and patient-derived or engineered iPSC systems, for Rab under-prenylation, vesicular trafficking, RPE dysfunction, and gene-replacement studies.
- Conditional Chm-deficient mouse models, because complete systemic disruption may not faithfully reproduce viable human disease; these are useful for retinal degeneration and AAV delivery but do not model deafness or obesity.
- Pou3f4-deficient or engineered mice for cochlear/modiolar malformation, auditory dysfunction, otic-mesenchyme biology, and surgical anatomy.
- Human lymphoblastoid/HEK-derived systems for POU3F4 localization and transcriptional assays, although they lack the complete developmental context.

Principal limitations are species differences, incomplete recapitulation of slow human retinal degeneration, and the absence of a model carrying the full patient-specific CNV. A high-value future resource would combine patient-derived iPSCs with isogenic CNV correction and differentiation into RPE/retinal organoids and otic organoids.

## Recent developments and expert interpretation

The key 2024 advance was Bonati et al.’s systematic reappraisal of Xq21 deletion-associated hearing loss and description of a **3.7-Mb deletion**, smaller than the previously summarized 5.2–16-Mb range, with partial CHM deletion and complete loss of POU3F4 and neighboring genes. This strengthens the expert view that unexplained congenital hearing loss with syndromic features warrants **cytogenomic CNV analysis**, not only small-variant sequencing. (bonati2024contiguousgenesyndromes pages 13-14)

A second 2024 advance was the updated mechanistic synthesis of retinal protein prenylation: REP1 is understood as the chaperone that presents unprenylated Rab proteins to GGTase-II, connecting CHM loss directly to membrane-trafficking failure in RPE and photoreceptors. (ashok2024updatesonproteinprenylation pages 9-11)

The 2024 REGENERATE results temper early optimism about subretinal AAV2-REP1: in 30 participants, the treatment did not produce a statistically significant BCVA advantage and carried surgery/inflammation-related risks. Expert interpretation should therefore be conservative—REP1 replacement remains experimental even for ordinary choroideremia and is not a complete treatment for a multigene Xq21 deletion. (cehajickapetanovic2024genetherapyfor pages 21-23, cehajickapetanovic2024genetherapyfor pages 27-29)

## Knowledge-base conclusions and evidence gaps

1. **High-confidence assertions:** X-linked Xq21 contiguous deletion; CHM-mediated retinal degeneration; POU3F4-mediated deafness; congenital/prelingual hearing involvement; progressive choroideremia.
2. **Moderate-confidence assertions:** obesity is part of the historical defining phenotype; larger deletions can add neurodevelopmental abnormalities; phenotype varies with deletion content.
3. **Unknown or unavailable:** standalone MONDO/OMIM/Orphanet identifier for the exact triad, syndrome prevalence/incidence, penetrance percentages, obesity gene, carrier frequency, founder effects, protective variants, biomarkers, survival statistics, quality-of-life scores, syndrome-level omics, natural animal disease, and syndrome-specific therapy.
4. **Curation rule:** record each patient’s exact deletion coordinates and gene content. Do not infer the complete Ayazi phenotype from a CHM sequence variant alone, a POU3F4 variant alone, or a generic Xq21 deletion that does not span the relevant genes.

### Principal current sources

- Bonati MT et al. “Contiguous Gene Syndromes and Hearing Loss: A Clinical Report of Xq21 Deletion and Comprehensive Literature Review.” *Genes*. Published May 2024. DOI/URL: https://doi.org/10.3390/genes15060677. (bonati2024contiguousgenesyndromes pages 13-14)
- Ashok S, Rao SR. “Updates on protein-prenylation and associated inherited retinopathies.” *Frontiers in Ophthalmology*. Published July 2024. DOI/URL: https://doi.org/10.3389/fopht.2024.1410874. (ashok2024updatesonproteinprenylation pages 9-11)
- Cehajic-Kapetanovic J et al. “Gene therapy for choroideremia using an adeno-associated viral vector encoding Rab escort protein 1: the REGENERATE open-label trial.” *Efficacy and Mechanism Evaluation*. Published May 2024. DOI/URL: https://doi.org/10.3310/wara5730; trial NCT02407678. (cehajickapetanovic2024genetherapyfor pages 23-25, cehajickapetanovic2024genetherapyfor pages 21-23)

PMIDs were not available in the retrieved full-text metadata and therefore are not supplied rather than risk assigning incorrect identifiers.

References

1. (bonati2024contiguousgenesyndromes pages 13-14): Maria Teresa Bonati, Agnese Feresin, Paolo Prontera, Paola Michieletto, Valeria Gambacorta, Giampietro Ricci, and Eva Orzan. Contiguous gene syndromes and hearing loss: a clinical report of xq21 deletion and comprehensive literature review. Genes, 15:677, May 2024. URL: https://doi.org/10.3390/genes15060677, doi:10.3390/genes15060677. This article has 0 citations.

2. (bonati2024contiguousgenesyndromes pages 19-21): Maria Teresa Bonati, Agnese Feresin, Paolo Prontera, Paola Michieletto, Valeria Gambacorta, Giampietro Ricci, and Eva Orzan. Contiguous gene syndromes and hearing loss: a clinical report of xq21 deletion and comprehensive literature review. Genes, 15:677, May 2024. URL: https://doi.org/10.3390/genes15060677, doi:10.3390/genes15060677. This article has 0 citations.

3. (cehajickapetanovic2024genetherapyfor pages 23-25): Jasmina Cehajic-Kapetanovic, Marco P Bellini, Laura J Taylor, Imran H Yusuf, Taha Soomro, Lyndon da Cruz, and Robert E MacLaren. Gene therapy for choroideremia using an adeno-associated viral vector encoding rab escort protein 1: the regenerate open-label trial. Efficacy and Mechanism Evaluation, pages 1-59, May 2024. URL: https://doi.org/10.3310/wara5730, doi:10.3310/wara5730. This article has 17 citations.

4. (ashok2024updatesonproteinprenylation pages 9-11): Sudhat Ashok and Sriganesh Ramachandra Rao. Updates on protein-prenylation and associated inherited retinopathies. Frontiers in Ophthalmology, Jul 2024. URL: https://doi.org/10.3389/fopht.2024.1410874, doi:10.3389/fopht.2024.1410874. This article has 7 citations.

5. (cehajickapetanovic2024genetherapyfor pages 21-23): Jasmina Cehajic-Kapetanovic, Marco P Bellini, Laura J Taylor, Imran H Yusuf, Taha Soomro, Lyndon da Cruz, and Robert E MacLaren. Gene therapy for choroideremia using an adeno-associated viral vector encoding rab escort protein 1: the regenerate open-label trial. Efficacy and Mechanism Evaluation, pages 1-59, May 2024. URL: https://doi.org/10.3310/wara5730, doi:10.3310/wara5730. This article has 17 citations.

6. (cehajickapetanovic2024genetherapyfor pages 27-29): Jasmina Cehajic-Kapetanovic, Marco P Bellini, Laura J Taylor, Imran H Yusuf, Taha Soomro, Lyndon da Cruz, and Robert E MacLaren. Gene therapy for choroideremia using an adeno-associated viral vector encoding rab escort protein 1: the regenerate open-label trial. Efficacy and Mechanism Evaluation, pages 1-59, May 2024. URL: https://doi.org/10.3310/wara5730, doi:10.3310/wara5730. This article has 17 citations.

## Artifacts

- [Edison artifact artifact-00](Choroideremia-Deafness-Obesity_Syndrome-deep-research-falcon_artifacts/artifact-00.md)