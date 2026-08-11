---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-06-19T09:13:06.047668'
end_time: '2026-06-19T09:13:06.050103'
duration_seconds: 0.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Oculopharyngodistal Myopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 31
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Oculopharyngodistal_Myopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Oculopharyngodistal_Myopathy-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Oculopharyngodistal_Myopathy-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Oculopharyngodistal Myopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Oculopharyngodistal Myopathy** covering all of the
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
- **Disease Name:** Oculopharyngodistal Myopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Oculopharyngodistal Myopathy** covering all of the
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


# Comprehensive Research Report: Oculopharyngodistal Myopathy (OPDM)

## 1. Disease Information

### Disease Definition and Overview
Oculopharyngodistal myopathy (OPDM; OMIM: 164310) is a rare adult-onset hereditary neuromuscular disorder characterized by progressive weakness affecting the ocular, pharyngeal, facial, and distal limb muscles (deng2020expansionofggc pages 1-2, ogasawara2020cggexpansionin pages 1-2, wagner2018mappingthechromosomal pages 1-6). The disease was first described by Satoyoshi and Kinoshita in 1977 as an autosomal dominant muscle condition with onset in late adulthood (wagner2018mappingthechromosomal pages 1-6). As stated in Deng et al. (2020), "Oculopharyngodistal myopathy (OPDM [MIM: 164310]) is a rare adult-onset myopathy with putative autosomal-dominant or autosomal-recessive inheritance. The typical clinical manifestations are insidiously progressive ptosis, ophthalmoparesis, facial and masseter weakness, dysphagia, and muscle weakness of distal limbs" (deng2020expansionofggc pages 1-2).

### Key Identifiers
- **OMIM ID**: 164310
- **MONDO ID**: Not explicitly provided in retrieved literature
- **Category**: Mendelian, autosomal dominant (with variable penetrance)
- **Alternative names**: OPDM, Oculopharyngeal distal myopathy

### Synonyms and Related Conditions
The disease spectrum now includes:
- OPDM type 1 (OPDM1) - LRP12-associated
- OPDM type 2 (OPDM2) - GIPC1-associated  
- OPDM type 3 (OPDM3) - NOTCH2NLC-associated
- OPDM type 4 (OPDM4) - RILPL1-associated
- OPDM type 5 (OPDM5) - ABCD3-associated
- Oculopharyngeal myopathy with leukoencephalopathy (OPML) - LOC642361/NUTM2B-AS1-associated

The condition is part of the "FNOP spectrum disorder" (Fragile X-associated tremor/ataxia syndrome, Neuronal intranuclear inclusion disease, and Oculopharyngodistal myopathy), reflecting shared CGG repeat pathogenesis (ishiura2023recentadvancesin pages 1-2, ishiura2023recentadvancesin pages 2-3).

### Data Source Type
Information is derived from both patient-level clinical series and aggregated disease-level resources including genetic studies, histopathological analyses, and mechanistic investigations.

## 2. Etiology

### Disease Causal Factors (Genetic)
OPDM is caused by CGG/GGC trinucleotide repeat expansions in the 5'-untranslated regions (5'UTR) of multiple genes. As of 2026, six causative genes have been identified (deng2020expansionofggc pages 1-2, boivin2026ggcrepeatexpansions pages 1-2, eura2026pathogeniccggexpansions pages 1-2):

| Subtype designation | Gene name | Gene location (chromosome) | Repeat type | Normal repeat range | Pathogenic repeat range | Year of discovery | Key clinical distinguishing features |
|---|---|---|---|---|---|---|---|
| OPDM1 | **LRP12** | 8q24.3 | 5′UTR **CGG/GGC** repeat expansion | ~13–45 repeats | ~85–289 repeats; most reported patients ~125–150 | 2019 | Classic OPDM phenotype with ptosis, ophthalmoplegia, dysphagia/dysarthria, facial and distal limb weakness; usually adult onset; rimmed vacuoles and intranuclear/cytoplasmic filamentous inclusions on biopsy; predominantly myopathic presentation, though shorter/intermediate expansions have been linked to motor neuropathy/ALS-spectrum phenotypes in later work (li2026translationofexpanded pages 1-2, eura2026pathogeniccggexpansions pages 1-2, ishiura2023recentadvancesin pages 2-3, hobara2025linkinglrp12cgg pages 1-2) |
| OPDM2 | **GIPC1** | 19p13.3 | 5′UTR **GGC/CGG** repeat expansion | Not clearly established in retrieved texts | Expanded alleles reported in affected patients; disease generally associated with large expansions, exact validated pathogenic threshold not stated in retrieved contexts | 2020 | Clinically similar to OPDM1 with progressive ptosis, external ophthalmoplegia, bulbar involvement, and distal-predominant weakness; RNA-seq implicated p53 signaling, ubiquitin-mediated proteolysis, and ribosome pathways; recent work supports translation into toxic polyglycine protein (uGIPpolyG) (deng2020expansionofggc pages 1-2, deng2020expansionofggc pages 2-3, boivin2026ggcrepeatexpansions pages 3-4) |
| OPDM3 | **NOTCH2NLC** | 1q21.2 | 5′UTR **CGG/GGC** repeat expansion | Not clearly established in retrieved texts | Often **>100 repeats** in reported OPDM cases; examples included 116, 128, 132, 135, 139, 184, 217, and 674-repeat expanded alleles | 2020 | OPDM with frequent additional neurologic features: peripheral neuropathy, leukoencephalopathy, cerebellar ataxia/tremor, retinal disease, hearing impairment, and occasional cognitive involvement; all seven Japanese cases had ptosis, ophthalmoplegia, dysarthria, and weakness; overlaps with NIID/FNOP spectrum (ogasawara2020cggexpansionin pages 1-2, ogasawara2020cggexpansionin pages 2-4, ishiura2023recentadvancesin pages 2-3) |
| OPDM4 | **RILPL1** | 12q24.31 | Noncoding **CCG/CGG-related** repeat expansion | Not clearly established in retrieved texts | Pathogenic expansion reported, but exact range not provided in retrieved contexts | 2022 | Similar core OPDM phenotype; review notes many patients present initially with ptosis or dysphagia; pathology includes p62-positive inclusions and rimmed vacuoles; recent mechanistic work shows antisense RILPL1-derived polyglycine protein (asRILpolyG) with relatively nuclear localization and muscle/CNS toxicity in models (ogasawara2022intranuclearinclusionsin pages 1-2, ishiura2023recentadvancesin pages 2-3, boivin2026ggcrepeatexpansions pages 5-6, boivin2026ggcrepeatexpansions pages 7-8) |
| OPML / OPDM-related LOC642361 subtype | **LOC642361 / NUTM2B-AS1** | 10q22.3 | Noncoding **CGG/GGC** repeat expansion | Not clearly established in retrieved texts | Pathogenic expansion reported, exact range not provided in retrieved contexts | 2024 | Typically described as **oculopharyngeal myopathy with leukoencephalopathy (OPML)** rather than pure OPDM; combines oculopharyngeal/distal myopathic features with white-matter disease and broader neurologic involvement; recent studies show translation into LOC6polyG found in p62-positive inclusions (ishiura2023recentadvancesin pages 1-2, boivin2026ggcrepeatexpansions pages 1-2, boivin2026ggcrepeatexpansions pages 5-6) |
| OPDM5 | **ABCD3** | 1p21.3 | Noncoding **CGG/GGC** repeat expansion | Not clearly established in retrieved texts | Pathogenic expansion reported, exact range not provided in retrieved contexts | 2024 | Core OPDM phenotype reported; generally grouped with isolated OPDM rather than OPML in review literature; mechanistically thought to share the common CGG-repeat disease biology of toxic polyglycine production/RNA toxicity, but subtype-specific distinguishing clinical data were limited in retrieved contexts (li2026translationofexpanded pages 1-2, eura2026pathogeniccggexpansions pages 1-2) |
| OPDM (overall, genetically heterogeneous) | Multiple genes: **LRP12, GIPC1, NOTCH2NLC, RILPL1, LOC642361/NUTM2B-AS1, ABCD3** | Multiple chromosomes | Predominantly noncoding **CGG/GGC** (and for RILPL1, reported **CCG/CGG-related**) repeat expansions | Gene-specific and incompletely standardized | Gene-specific; larger repeats generally correlate with earlier onset in GIPC1 and NOTCH2NLC, while methylation modifies phenotype especially in LRP12 | 2019–2024 | Shared syndrome: slowly progressive adult-onset ptosis, ophthalmoplegia, bulbar weakness, facial weakness, and distal limb weakness with rimmed vacuoles; shared mechanisms include toxic polyglycine proteins, p62-positive inclusions, and possible RNA toxicity; age at onset and multisystem involvement vary by gene and methylation state (eura2025complexassociationsof pages 1-5, eura2026pathogeniccggexpansions pages 1-2, ishiura2023recentadvancesin pages 2-3, boivin2026ggcrepeatexpansions pages 1-2) |


*Table: This table summarizes the currently recognized genetic subtypes linked to oculopharyngodistal myopathy and related OPML, including genes, repeat classes, reported size ranges, and major clinical distinctions. It is useful for comparing the expanding repeat-expansion spectrum and highlighting where evidence remains incomplete in the retrieved literature.*

**Summary of genetic subtypes** is provided in the table above. The expanded GGC repeats are essential in pathogenesis regardless of the specific gene location (deng2020expansionofggc pages 1-2).

### Risk Factors

**Genetic Risk Factors:**
- CGG repeat length: Generally, pathogenic expansions exceed ~85-100 repeats depending on the gene, with most LRP12 patients having 125-150 repeats and NOTCH2NLC patients often having >100 repeats (deng2020expansionofggc pages 1-2, ogasawara2020cggexpansionin pages 1-2)
- Somatic mosaicism: Intra-patient repeat size variability, particularly in LRP12 and NOTCH2NLC, may influence disease severity and progression (eura2025complexassociationsof pages 1-5)
- Founder effects: Distinct single nucleotide variant patterns suggest founder haplotypes for LRP12 and GIPC1 expansions, indicating population-specific risk (eura2025complexassociationsof pages 1-5, eura2026pathogeniccggexpansions pages 1-2)
- Intermediate repeat expansions: Shorter LRP12 expansions (<100 repeats, mean ~76) have been associated with motor neuron disease/ALS phenotypes rather than classic OPDM (hobara2025linkinglrp12cgg pages 1-2)

**Epigenetic Modifiers:**
- CpG methylation status: Higher methylation of expanded repeat regions, particularly in LRP12, is associated with delayed disease onset and can result in asymptomatic carriers despite extensive repeat expansions (eura2025complexassociationsof pages 1-5, eura2026pathogeniccggexpansions pages 1-2). As described by Eura et al. (2025), "some asymptomatic carriers exhibit extensive repeat expansions, with hypermethylation of the expanded regions, suggesting that epigenetic modifications, such as promoter hypermethylation, may prevent disease development" (eura2025complexassociationsof pages 1-5).

**Environmental Risk Factors:**
Not applicable - OPDM is a genetic disorder with no established environmental triggers.

### Protective Factors
- Hypermethylation of expanded CGG repeats may act as a protective factor, preventing or delaying disease manifestation in some carriers (eura2025complexassociationsof pages 1-5, eura2026pathogeniccggexpansions pages 1-2)

### Gene-Environment Interactions
Not established in the literature retrieved.

## 3. Phenotypes

### Core Clinical Features

| Phenotype / clinical feature | HPO term suggestion | Frequency among affected individuals | Age of onset | Severity | Progression pattern | Anatomical systems / structures affected |
|---|---|---|---|---|---|---|
| Ptosis | HP:0000508 | Core feature; 7/7 in OPDM_NOTCH2NLC series; generally characteristic across OPDM subtypes (ogasawara2020cggexpansionin pages 1-2, ogasawara2020cggexpansionin pages 2-4, deng2020expansionofggc pages 1-2, ogasawara2022intranuclearinclusionsin pages 1-2, ishiura2023recentadvancesin pages 2-3) | Usually adult-onset; can range from infancy/juvenile to late adulthood in NOTCH2NLC-associated cases (1–68 years overall in one series) (ogasawara2020cggexpansionin pages 2-4) | Variable | Progressive, insidious (deng2020expansionofggc pages 1-2, ishiura2023recentadvancesin pages 2-3) | Eyelids; extraocular musculature; cranial muscles |
| External ophthalmoplegia / ophthalmoparesis | HP:0000602 | Core feature; 7/7 in OPDM_NOTCH2NLC series; repeatedly described as typical of OPDM (ogasawara2020cggexpansionin pages 1-2, ogasawara2020cggexpansionin pages 2-4, deng2020expansionofggc pages 1-2, yu2021theggcrepeat pages 1-2, ishiura2023recentadvancesin pages 2-3) | Usually adult-onset; occasionally juvenile/early onset in OPDM3 (ogasawara2020cggexpansionin pages 2-4) | Variable | Progressive (deng2020expansionofggc pages 1-2, ishiura2023recentadvancesin pages 2-3) | Extraocular muscles; ocular motor system |
| Dysphagia | HP:0002015 | Common core bulbar feature; present in 5/7 OPDM_NOTCH2NLC cases in one table and broadly typical across OPDM (ogasawara2020cggexpansionin pages 2-4, deng2020expansionofggc pages 1-2, ishiura2023recentadvancesin pages 2-3) | Adult-onset in most; may appear later than limb or ocular symptoms (ogasawara2020cggexpansionin pages 2-4, ishiura2023recentadvancesin pages 2-3) | Variable to severe | Progressive (deng2020expansionofggc pages 1-2, ishiura2023recentadvancesin pages 2-3) | Pharyngeal muscles; swallowing apparatus |
| Dysarthria | HP:0001260 | 7/7 in OPDM_NOTCH2NLC series; frequently reported in bulbar involvement (ogasawara2020cggexpansionin pages 1-2, ogasawara2020cggexpansionin pages 2-4) | Adult-onset in most; broad range across subtypes (ogasawara2020cggexpansionin pages 2-4) | Variable | Progressive (ogasawara2020cggexpansionin pages 1-2) | Bulbar musculature; speech system |
| Facial muscle weakness | HP:0000297 | Common core feature; 5/7 in OPDM_NOTCH2NLC series; repeatedly described in OPDM overviews (deng2020expansionofggc pages 1-2, ogasawara2020cggexpansionin pages 2-4, ishiura2023recentadvancesin pages 2-3) | Usually adult-onset (ogasawara2020cggexpansionin pages 2-4, ishiura2023recentadvancesin pages 2-3) | Variable | Progressive (deng2020expansionofggc pages 1-2) | Facial musculature; cranial muscles |
| Masseter weakness | HP:0030319 | Characteristic but frequency not well quantified; included in classic disease descriptions (deng2020expansionofggc pages 1-2) | Adult-onset | Variable | Progressive | Masticatory muscles; craniofacial musculature |
| Distal limb muscle weakness | HP:0002460 | Defining feature; all 7 OPDM_NOTCH2NLC patients had limb weakness, commonly distal-predominant; also emphasized in major OPDM definitions (ogasawara2020cggexpansionin pages 1-2, ogasawara2020cggexpansionin pages 2-4, deng2020expansionofggc pages 1-2, yu2021theggcrepeat pages 1-2, ishiura2023recentadvancesin pages 2-3) | Usually adult-onset; occasionally juvenile/childhood onset in OPDM3 (ogasawara2020cggexpansionin pages 2-4) | Moderate to severe; variable | Slowly progressive (deng2020expansionofggc pages 1-2, ishiura2023recentadvancesin pages 2-3) | Distal upper/lower limb skeletal muscles |
| Proximal limb weakness (variable, less typical) | HP:0003701 | Less typical than distal weakness; some OPDM3 cases had D=P or proximal upper limb involvement; review notes weakness can be proximal/asymmetrical in some subtypes (ogasawara2020cggexpansionin pages 2-4, ishiura2023recentadvancesin pages 2-3) | Adult-onset usually | Variable | Progressive | Proximal limb muscles; shoulder/hip girdle |
| Diffuse limb weakness / generalized myopathy | HP:0003323 | Seen in some patients/subtypes; broad myopathic presentation described in reviews and some series (ishiura2023recentadvancesin pages 2-3, ogasawara2020cggexpansionin pages 2-4) | Adult-onset usually | Variable | Progressive | Appendicular skeletal muscle system |
| Muscle atrophy | HP:0003202 | Present in some OPDM_NOTCH2NLC cases (distal or diffuse atrophy in table); frequent in advanced disease (ogasawara2020cggexpansionin pages 2-4) | Develops after weakness onset | Variable | Progressive | Limb skeletal muscles |
| Neck weakness | HP:0000467 | Present in a subset of OPDM_NOTCH2NLC cases (3/7 noted in one table) (ogasawara2020cggexpansionin pages 2-4) | Variable | Mild to moderate | Progressive | Cervical skeletal muscles |
| Rimmed vacuoles on muscle biopsy | HP:0012115 | Hallmark pathology across OPDM; present in diagnostic descriptions and all major subtype studies (deng2020expansionofggc pages 1-2, ogasawara2020cggexpansionin pages 1-2, ogasawara2022intranuclearinclusionsin pages 1-2, ishiura2023recentadvancesin pages 2-3) | Detected at biopsy after symptomatic onset | Variable pathologic burden | Progressive histopathologic correlate | Skeletal muscle fibers |
| Intranuclear inclusions in muscle fibers | HP:0034335 | Seen in OPDM, especially subtype-associated p62/ubiquitin/SUMO-positive inclusions; non-muscle INIs support OPDM over OPMD (ogasawara2020cggexpansionin pages 1-2, ogasawara2022intranuclearinclusionsin pages 1-2, ishiura2023recentadvancesin pages 2-3) | After disease onset; biopsy finding | Variable | Progressive pathologic correlate | Myonuclei; also blood vessels, peripheral nerve bundles, muscle spindle-associated cells in OPDM |
| Myopathic EMG / chronic myopathic change | HP:0003458 | Common in classic OPDM descriptions; frequency not uniformly quantified in retrieved texts (deng2020expansionofggc pages 1-2, ishiura2023recentadvancesin pages 2-3) | After symptom onset | Variable | Progressive | Skeletal muscle electrical function |
| Small angular fibers / internal nuclei / fibrosis on biopsy | HP:0200037 | Common pathological findings, though not always quantified; noted in OPDM muscle pathology (eura2025complexassociationsof pages 1-5, ogasawara2020cggexpansionin pages 2-4) | After symptom onset | Variable | Progressive histologic change | Skeletal muscle tissue |
| Peripheral neuropathy | HP:0009830 | Variable extra-muscular feature; confirmed by nerve conduction in 3/7 OPDM_NOTCH2NLC cases; review highlights overlap with NIID and peripheral neuropathy (ogasawara2020cggexpansionin pages 2-4, ishiura2023recentadvancesin pages 2-3, hobara2025linkinglrp12cgg pages 1-2) | Often adult-onset, may accompany or follow myopathy | Variable | Progressive | Peripheral nerves; motor and sometimes sensory nerves |
| Sensory disturbance | HP:0003474 | 3/7 in OPDM_NOTCH2NLC table (ogasawara2020cggexpansionin pages 2-4) | Adult-onset usually | Variable | Progressive | Peripheral sensory nervous system |
| Tremor | HP:0001337 | Reported in some OPDM_NOTCH2NLC patients and in broader FNOP-spectrum overlap (ogasawara2020cggexpansionin pages 2-4, ishiura2023recentadvancesin pages 2-3) | Usually later adult onset | Mild to moderate | Progressive or fluctuating | Cerebellar / extrapyramidal motor systems |
| Cerebellar ataxia | HP:0001251 | Reported in a subset of OPDM_NOTCH2NLC patients and broader NOTCH2NLC-related spectrum (ogasawara2020cggexpansionin pages 2-4, ishiura2023recentadvancesin pages 2-3) | Adult-onset usually | Variable | Progressive | Cerebellum; gait and coordination systems |
| Leukoencephalopathy / white matter disease | HP:0002352 | Present in some OPDM_NOTCH2NLC cases (3/7 in one table had leukoencephalopathy) and central-spectrum overlap disorders (ogasawara2020cggexpansionin pages 2-4, ishiura2023recentadvancesin pages 2-3) | Usually adult-onset | Variable | Progressive | Cerebral white matter |
| Cognitive impairment / dementia features | HP:0100543 | Not a core OPDM feature, but lower HDS-R scores and CNS overlap reported in some NOTCH2NLC-related cases; broader spectrum includes cognitive decline (ogasawara2020cggexpansionin pages 2-4, ishiura2023recentadvancesin pages 2-3) | Later adult onset usually | Variable | Progressive | Cerebral cortex / cognition networks |
| Developmental delay (rare) | HP:0001263 | Rare; 1 patient in OPDM_NOTCH2NLC series had onset at age 1 year with developmental delay (ogasawara2020cggexpansionin pages 2-4) | Infancy / childhood in rare cases | Variable | Static plus superimposed progressive disease possible | Neurodevelopmental systems |
| Visual disturbance / retinopathy / retinal pigmentary degeneration | HP:0000505 | Reported in several OPDM_NOTCH2NLC patients; review notes retinopathy in NOTCH2NLC-related disorders (ogasawara2020cggexpansionin pages 2-4, ishiura2023recentadvancesin pages 2-3) | Variable, often adult-onset | Variable | Progressive | Retina; visual system |
| Hearing impairment | HP:0000365 | Reported in several OPDM_NOTCH2NLC patients; earlier literature cited overlap with sensorineural hearing loss (ogasawara2020cggexpansionin pages 2-4, ogasawara2020cggexpansionin pages 1-2) | Adult-onset usually | Variable | Progressive | Auditory system |
| Cataract / photophobia / miosis (variable ocular non-motility features) | HP:0000518 / HP:0000613 / HP:0000616 | Individual cases reported in OPDM_NOTCH2NLC table (ogasawara2020cggexpansionin pages 2-4) | Variable | Mild to moderate | Variable / progressive | Lens, iris, visual system |
| Deep tendon reflex reduction | HP:0001315 | Reduced reflexes documented in all 7 OPDM_NOTCH2NLC patients (degrees varied) (ogasawara2020cggexpansionin pages 2-4) | After neuromuscular involvement develops | Mild to moderate | Progressive | Peripheral nerve / neuromuscular reflex arcs |
| Elevated serum creatine kinase | HP:0003236 | Variable; CK values ranged from 63 to 1886 IU/L in 7 OPDM_NOTCH2NLC patients (ogasawara2020cggexpansionin pages 2-4) | After muscle involvement begins | Mild to moderate elevation; variable | Variable over disease course | Skeletal muscle injury biomarker |
| Asymmetric muscle involvement on imaging | HP:0009837 | Reported in at least one OPDM_NOTCH2NLC patient by muscle CT; review also notes asymmetry can occur (ogasawara2020cggexpansionin pages 2-4, ishiura2023recentadvancesin pages 2-3) | Established disease | Variable | Progressive | Limb and pelvic skeletal muscles |
| Cardiac conduction / ECG abnormalities (uncommon) | HP:0011707 | Rare but reported in OPDM_NOTCH2NLC: long QT in 1 case, AV block/LVH in 1 case (ogasawara2020cggexpansionin pages 2-4) | Adult-onset | Variable | Progressive or stable | Cardiac conduction system / myocardium |
| Respiratory involvement | HP:0002093 | Not well characterized in retrieved OPDM papers; no strong evidence for a common core feature (ishiura2023recentadvancesin pages 2-3) | Not established | Unknown / variable | Unknown | Respiratory muscles / pulmonary system |


*Table: This table summarizes core and variable clinical manifestations reported for oculopharyngodistal myopathy, including suggested HPO terms, approximate frequencies where available, onset patterns, severity, progression, and affected systems. It is useful for phenotype curation and knowledge-base annotation across genetically heterogeneous OPDM subtypes.*

The comprehensive phenotype table above summarizes all clinical manifestations with HPO term suggestions and detailed characteristics.

**Core OPDM Phenotype:**
The hallmark features include:
1. **Ptosis** (HP:0000508): Progressive drooping of eyelids
2. **External ophthalmoplegia** (HP:0000602): Paralysis of extraocular muscles
3. **Dysphagia** (HP:0002015): Difficulty swallowing
4. **Dysarthria** (HP:0001260): Impaired speech articulation
5. **Facial weakness** (HP:0000297): Weakness of facial muscles
6. **Distal limb weakness** (HP:0002460): Predominantly distal muscle weakness, distinguishing OPDM from the more proximally-affected OPMD

As stated in Ogasawara et al. (2020), "Oculopharyngodistal myopathy (OPDM) is a rare hereditary muscle disease characterized by progressive distal limb weakness, ptosis, ophthalmoplegia, bulbar muscle weakness and rimmed vacuoles on muscle biopsy" (ogasawara2020cggexpansionin pages 1-2).

### Variable Neurological Features
Particularly in OPDM3 (NOTCH2NLC-associated), additional features may include:
- Peripheral neuropathy (HP:0009830)
- Cerebellar ataxia (HP:0001251)
- Tremor (HP:0001337)
- Leukoencephalopathy (HP:0002352)
- Cognitive impairment (HP:0100543)
- Retinopathy (HP:0000505)
- Hearing impairment (HP:0000365)

In the NOTCH2NLC series, all seven patients demonstrated ptosis, ophthalmoplegia, dysarthria, and muscle weakness, with additional central and/or peripheral nervous system involvement (ogasawara2020cggexpansionin pages 1-2, ogasawara2020cggexpansionin pages 2-4).

### Histopathological Phenotype
**Muscle Biopsy Findings:**
- **Rimmed vacuoles** (HP:0012115): Hallmark pathology across all OPDM subtypes
- **Intranuclear inclusions** (HP:0034335): p62/ubiquitin/SUMO1-positive inclusions in myonuclei and non-muscle cells (blood vessels, peripheral nerve bundles, muscle spindles)
- **Small angular fibers and internal nuclei**: Indicating myopathic changes
- **Eosinophilic inclusions**: Particularly noted in NOTCH2NLC cases

A key diagnostic feature differentiating OPDM from oculopharyngeal muscular dystrophy (OPMD) is the pattern of intranuclear inclusions. As Ogasawara et al. (2022) state: "OPMD can be differentiated from OPDM and other RVMs by the frequent presence of myo-INIs; and in OPDM, the presence of non-muscle-INIs in muscle pathology should be a diagnostic hallmark" (ogasawara2022intranuclearinclusionsin pages 1-2).

### Age of Onset and Progression
- **Typical age of onset**: Adult-onset, predominantly in the 40s-50s (range: 1-68 years reported)
- **Onset pattern**: Insidious, slowly progressive
- **Progression**: All cases show progressive deterioration over time
- **Disease course**: Chronic, lifelong, progressive

### Quality of Life Impact
While specific quality-of-life metrics were not extensively reported in the retrieved literature, the progressive nature of dysphagia, ophthalmoplegia, and limb weakness significantly impacts activities of daily living, swallowing safety, mobility, and independence.

## 4. Genetic/Molecular Information

### Causal Genes
Six genes are currently implicated in OPDM/OPML:

1. **LRP12** (HGNC:6700): Low-density lipoprotein receptor-related protein 12, chromosome 8q24.3
2. **GIPC1** (HGNC:4270): GIPC PDZ domain containing family member 1, chromosome 19p13.3
3. **NOTCH2NLC** (HGNC:24993): Notch homolog 2 N-terminal like C, chromosome 1q21.2
4. **RILPL1** (HGNC:10060): Rab interacting lysosomal protein like 1, chromosome 12q24.31
5. **LOC642361/NUTM2B-AS1**: Long noncoding RNA, chromosome 10q22.3
6. **ABCD3** (HGNC:67): ATP binding cassette subfamily D member 3, chromosome 1p21.3

### Pathogenic Variants

**Variant Type**: Noncoding CGG/GGC trinucleotide repeat expansions in 5'-untranslated regions

**Variant Classification**: Pathogenic according to established disease-causing repeat thresholds (varies by gene)

**Normal vs. Pathogenic Repeat Ranges:**
- **LRP12**: Normal ~13-45 repeats; pathogenic ~85-289 repeats (most 125-150)
- **GIPC1**: Pathogenic expansions identified; normal range not clearly established in retrieved texts
- **NOTCH2NLC**: Pathogenic often >100 repeats; cases with 116-674 repeats reported
- **RILPL1, LOC642361, ABCD3**: Pathogenic expansions confirmed; precise thresholds incompletely defined

**Allele Frequency**: OPDM is rare; population-specific screening suggests <1% of healthy controls carry expansions, but systematic population frequency data are limited (deng2020expansionofggc pages 1-2).

**Somatic vs. Germline**: Germline CGG expansions with somatic instability (intra-patient repeat size variability) documented (eura2025complexassociationsof pages 1-5).

**Functional Consequences**: 
The expanded repeats lead to dual mechanisms:
1. **Protein gain-of-function**: RAN (repeat-associated non-AUG) translation produces toxic polyglycine-containing proteins
2. **RNA gain-of-function**: Expanded CGG-repeat RNAs form toxic RNA foci

### Modifier Genes
Not explicitly identified in retrieved literature, though epigenetic modifiers (methylation machinery) influence penetrance.

### Epigenetic Information
**DNA Methylation**: CpG methylation of expanded repeat regions modulates disease expression. "A significant inverse correlation was observed between repeat length and age at onset in patients with GIPC1 or NOTCH2NLC expansions, while this was disturbed by higher methylation of expanded regions in patients with LRP12 expansions, leading to delayed onset" (eura2026pathogeniccggexpansions pages 1-2). Asymptomatic carriers with ultra-long, heavily methylated expansions have been documented (eura2025complexassociationsof pages 1-5).

### Chromosomal Abnormalities
None beyond the repeat expansions. Structural variations flanking repeat regions have been identified in some patients (eura2025complexassociationsof pages 1-5).

## 5. Environmental Information

### Environmental Factors
Not applicable - OPDM is a genetic disorder with no established environmental causative factors.

### Lifestyle Factors
No specific lifestyle factors influence disease risk or progression in current literature.

### Infectious Agents
Not applicable.

## 6. Mechanism / Pathophysiology

| Pathogenic mechanism | Evidence source/type | Key molecular players/pathways | Cellular processes affected | GO/CL term suggestions | Supporting references |
|---|---|---|---|---|---|
| Noncoding CGG/GGC repeat expansion as initiating mutation | Human genetic studies; long-read sequencing; clinicogenetic cohorts | Expanded CGG/GGC repeats in **LRP12, GIPC1, NOTCH2NLC, RILPL1, LOC642361/NUTM2B-AS1, ABCD3**; repeat length, flanking sequence context, and CpG methylation modulate phenotype | Repeat instability, altered transcriptional/epigenetic state, genotype-phenotype correlation | GO:0006351 transcription, DNA-templated; GO:0006306 DNA methylation; GO:0006996 organelle organization; CL:0000187 muscle cell | (eura2025complexassociationsof pages 1-5, eura2026pathogeniccggexpansions pages 1-2, ishiura2023recentadvancesin pages 2-3) |
| RAN / non-AUG-associated translation into toxic polyglycine proteins | Cell models; human muscle pathology; mouse and fly models | **uGIPpolyG, uN2CpolyG, asRILpolyG, LOC6polyG, LRP12-associated polyG**; initiation from upstream AUG/near-cognate codons or noncanonical mechanisms; repeat translated predominantly in glycine frame | Aberrant translation of repeat-containing transcripts; production of aggregation-prone polyglycine proteins | GO:0006412 translation; GO:0034059 response to unfolded protein; GO:0017148 negative regulation of translation; CL:0000187 muscle cell, CL:0000540 neuron | (li2026translationofexpanded pages 1-2, boivin2026ggcrepeatexpansions pages 1-2, li2026translationofexpanded pages 3-5, boivin2026ggcrepeatexpansions pages 3-4) |
| Polyglycine protein toxicity | Cell models; iPSC-derived myotubes; mouse skeletal muscle and CNS models | PolyG proteins derived from expanded repeats; cytotoxicity correlates with inclusion formation and subtype-specific flanking sequences | Cell death, myofiber atrophy, locomotor deficits, neurodegeneration, shortened lifespan | GO:0008219 cell death; GO:0016043 cellular component organization; GO:0048856 anatomical structure development; CL:0000187 muscle cell, CL:0002319 myotube, CL:0000540 neuron | (li2026translationofexpanded pages 3-5, boivin2026ggcrepeatexpansions pages 5-6, boivin2026ggcrepeatexpansions pages 7-8) |
| Protein aggregation and p62/ubiquitin-positive intranuclear inclusions | Human muscle biopsy; cell models; mouse models | **SQSTM1/p62, ubiquitin, SUMO1**, poly-ubiquitinated proteins; eosinophilic intranuclear inclusions and rimmed vacuoles | Protein quality control failure, aggregate sequestration, inclusion formation in myonuclei and non-muscle cells | GO:0061684 chaperone-mediated autophagy; GO:0016567 protein ubiquitination; GO:0097352 autophagosome organization; CL:0000187 muscle cell, CL:0000359 skeletal muscle fiber | (ogasawara2020cggexpansionin pages 1-2, ogasawara2022intranuclearinclusionsin pages 1-2, li2026translationofexpanded pages 3-5, boivin2026ggcrepeatexpansions pages 5-6, boivin2026ggcrepeatexpansions pages 7-8) |
| RNA toxicity / RNA gain-of-function | Human muscle studies; mechanistic reviews; immunofluorescence-based studies | Expanded CGG-repeat RNAs; **RNA foci**, RNA-binding proteins including **hnRNP A/B** and **MBNL1** discussed/assessed; disruption of RNA metabolism proposed | RNA sequestration, impaired RNA processing, altered RNA metabolism | GO:0008380 RNA splicing; GO:0016071 mRNA metabolic process; GO:0003723 RNA binding; CL:0000187 muscle cell, CL:0000540 neuron | (yu2021theggcrepeat pages 1-2, eura2025complexassociationsof pages 1-5, li2026translationofexpanded pages 1-2, ishiura2023recentadvancesin pages 2-3) |
| Nuclear architecture disruption | Cell models; transfected skeletal muscle cells | LRP12-associated polyG inclusions alter **Lamin B1 / nuclear lamina** architecture; nuclear rather than cytosolic localization in muscle | Nuclear envelope stress, altered nuclear organization, impaired nucleo-cytoplasmic homeostasis | GO:0005635 nuclear envelope; GO:0006998 nuclear envelope organization; GO:0051290 protein heterooligomerization; CL:0000187 muscle cell | (li2026translationofexpanded pages 1-2, li2026translationofexpanded pages 3-5) |
| Mitochondrial dysfunction and oxidative phosphorylation defects | Drosophila model; human NIID/NOTCH2NLC-related muscle samples; cellular studies | **uN2CpolyG**, **LRPPRC**, oxidative phosphorylation genes/pathways; idebenone-responsive mitochondrial dysfunction | Mitochondrial swelling, impaired oxidative phosphorylation, energy failure, progressive neurodegeneration | GO:0005739 mitochondrion; GO:0006119 oxidative phosphorylation; GO:0007005 mitochondrion organization; CL:0000540 neuron, CL:0000187 muscle cell | (yu2022cggrepeatexpansion pages 1-2) |
| Disturbance of proteostasis / ubiquitin-proteasome and autophagy-related pathways | Human RNA-seq; cell and animal models | **Ubiquitin-mediated proteolysis**, **p53 signaling**, ribosome pathways; p62-positive inclusions; altered protein turnover | Proteostasis imbalance, stress signaling, impaired degradation of toxic species | GO:0010498 proteasomal protein catabolic process; GO:0006914 autophagy; GO:0006977 DNA damage response; CL:0000187 muscle cell | (deng2020expansionofggc pages 1-2, deng2020expansionofggc pages 2-3, boivin2026ggcrepeatexpansions pages 5-6) |
| Gene-specific epigenetic modulation and incomplete penetrance | Human long-read methylation studies; family-based analyses | Upstream-region **CpG methylation**, especially in **LRP12** and **NOTCH2NLC**; hypermethylation associated with delayed onset or asymptomatic carriers | Epigenetic silencing/modulation of toxic repeat effects; age-at-onset modification | GO:0006306 DNA methylation; GO:0040029 regulation of gene expression, epigenetic; CL:0000000 cell | (eura2025complexassociationsof pages 1-5, eura2026pathogeniccggexpansions pages 1-2, ishiura2023recentadvancesin pages 2-3) |
| Somatic repeat-size variability and repeat instability | Human nanopore/long-read sequencing | Intra-patient variability of expanded repeats, especially in **LRP12** and **NOTCH2NLC**; structural variation in expanded alleles | Somatic mosaicism, dynamic mutation behavior, tissue-level heterogeneity | GO:0006310 DNA recombination; GO:0006281 DNA repair; CL:0000000 cell | (eura2025complexassociationsof pages 1-5, eura2026pathogeniccggexpansions pages 1-2) |
| Multisystem overlap with NIID/FNOP spectrum | Human clinical-pathologic studies; review synthesis | **NOTCH2NLC** links OPDM to **NIID**; shared inclusions and overlapping CNS/PNS manifestations support common disease biology | Shared neuromyodegenerative processes across muscle, peripheral nerve, retina, and CNS | GO:0048856 anatomical structure development; GO:0007268 synaptic transmission; CL:0000540 neuron, CL:0000187 muscle cell, CL:0000125 glial cell | (ogasawara2020cggexpansionin pages 1-2, ishiura2023recentadvancesin pages 1-2, ogasawara2020cggexpansionin pages 2-4, ishiura2023recentadvancesin pages 2-3) |
| Therapeutic mechanism-of-action leads under investigation | Animal models; cell models | **Idebenone** improved mitochondrial dysfunction in NOTCH2NLC fly model; **TMPyP4** reduced polyglycine abundance/toxicity and appears to act mainly on translation | Rescue of mitochondrial function; reduction of toxic protein expression/aggregation | GO:1902600 proton transmembrane transport; GO:0017148 negative regulation of translation; CL:0000540 neuron, CL:0000187 muscle cell | (boivin2026ggcrepeatexpansions pages 7-8, yu2022cggrepeatexpansion pages 1-2) |


*Table: This table summarizes the main pathogenic mechanisms proposed for oculopharyngodistal myopathy and links each mechanism to the evidence type, molecular players, affected cellular processes, and ontology suggestions. It is useful for curating pathophysiology across OPDM subtypes and distinguishing well-supported mechanisms from emerging ones.*

The detailed pathophysiology table above summarizes all known mechanisms with ontology terms.

### Primary Pathogenic Mechanisms

**1. RAN Translation into Toxic Polyglycine Proteins**

The most significant recent advancement in OPDM pathogenesis is the discovery that CGG/GGC repeat expansions are translated via repeat-associated non-AUG (RAN) translation into toxic polyglycine-containing proteins. As Boivin et al. (2026) state: "GGC repeat expansions causing oculopharyngodistal myopathy with or without oculopharyngeal myopathy leukoencephalopathy are located within previously unrecognized open reading frames (ORFs), resulting in their translation into new polyglycine-containing proteins" (boivin2026ggcrepeatexpansions pages 1-2).

Five distinct polyglycine proteins have been characterized:
- **uGIPpolyG** (GIPC1-associated OPDM2)
- **uN2CpolyG** (NOTCH2NLC-associated OPDM3/NIID)  
- **asRILpolyG** (RILPL1-associated OPDM4)
- **LOC6polyG** (LOC642361-associated OPML)
- **LRP12-associated polyG** (LRP12-associated OPDM1)

These proteins:
- Form p62/ubiquitin-positive cytoplasmic and intranuclear inclusions matching those seen in patient tissues (boivin2026ggcrepeatexpansions pages 1-2, li2026translationofexpanded pages 3-5, boivin2026ggcrepeatexpansions pages 5-6)
- Cause cell death, myofiber atrophy, and neurodegeneration in cellular and animal models (boivin2026ggcrepeatexpansions pages 5-6, boivin2026ggcrepeatexpansions pages 7-8)
- Show gene-specific differences in localization (e.g., asRILpolyG is more nuclear) and toxicity profiles (boivin2026ggcrepeatexpansions pages 5-6)

**2. RNA Toxicity**

Expanded CGG-repeat RNAs can sequester RNA-binding proteins (such as hnRNP A/B and MBNL1) and disrupt RNA metabolism, contributing to pathology (yu2021theggcrepeat pages 1-2, ishiura2023recentadvancesin pages 2-3). 

**3. Mitochondrial Dysfunction**

A Drosophila model expressing uN2CpolyG demonstrated mitochondrial swelling, impaired oxidative phosphorylation, and energy deficits. These defects were also observed in muscle biopsies from individuals with NIID/NOTCH2NLC-related disease. Idebenone treatment restored mitochondrial function and alleviated neurodegenerative phenotypes in the fly model (yu2022cggrepeatexpansion pages 1-2).

**4. Protein Aggregation and Proteostasis Failure**

Polyglycine proteins aggregate into p62/ubiquitin/SUMO1-positive inclusions, overwhelming protein quality control systems. RNA-seq analysis implicated ubiquitin-mediated proteolysis, p53 signaling, and ribosome pathways (deng2020expansionofggc pages 1-2, deng2020expansionofggc pages 2-3).

**5. Nuclear Architecture Disruption**

LRP12-associated polyglycine inclusions disrupt the nuclear lamina (Lamin B1) architecture, impairing nuclear organization and nucleo-cytoplasmic homeostasis (li2026translationofexpanded pages 1-2, li2026translationofexpanded pages 3-5).

### Cellular Processes Affected
- Protein translation (GO:0006412)
- Protein folding and quality control (GO:0034059)
- Autophagy and proteolysis (GO:0006914, GO:0010498)
- Mitochondrial oxidative phosphorylation (GO:0006119)
- RNA processing and metabolism (GO:0008380)
- Nuclear organization (GO:0006998)

### Cell Types Involved
- **Skeletal muscle fibers** (CL:0000187): Primary site of pathology
- **Neurons** (CL:0000540): Affected in OPDM3/NIID and OPML subtypes
- **Vascular endothelial cells**: Contain intranuclear inclusions in OPDM
- **Schwann cells/pericytes**: Show pathology in nerve biopsies
- **Muscle spindle-associated cells**: Demonstrate inclusions

## 7. Anatomical Structures Affected

### Organ Level

**Primary Organs:**
- **Skeletal muscle system** (UBERON:0001015): Ocular (extraocular muscles), pharyngeal, facial, masseter, and distal limb muscles
- **Peripheral nervous system** (UBERON:0000010): Especially in OPDM3, with demyelinating and axonal neuropathy
- **Central nervous system** (UBERON:0001017): Variable involvement with leukoencephalopathy, ataxia, and cognitive changes in OPDM3/OPML

**Secondary Organs:**
- **Eye** (UBERON:0000970): Retinopathy in some cases
- **Inner ear** (UBERON:0002117): Hearing impairment
- **Heart** (UBERON:0000948): Rare cardiac conduction abnormalities reported

### Tissue and Cell Level
- **Skeletal muscle tissue** (UBERON:0001134): Rimmed vacuoles, myopathic changes, intranuclear inclusions
- **Peripheral nerve tissue** (UBERON:0002020): Neurogenic changes, intranuclear inclusions in non-myocyte cells
- **White matter** (UBERON:0002316): In OPML and OPDM3 with leukoencephalopathy

### Subcellular Level
- **Nucleus** (GO:0005634): Intranuclear inclusions, disrupted nuclear lamina
- **Cytoplasm** (GO:0005737): Rimmed vacuoles, cytoplasmic inclusions
- **Mitochondrion** (GO:0005739): Swelling, dysfunction in oxidative phosphorylation

### Localization
- **Bilateral symmetric** involvement is typical for extraocular and bulbar muscles
- **Asymmetric** muscle involvement on imaging reported in some cases (ogasawara2020cggexpansionin pages 2-4)
- **Distal-predominant** limb weakness distinguishes OPDM from OPMD

## 8. Temporal Development

### Onset
- **Typical age**: Adult-onset, predominantly 40s-50s (range 1-68 years)
- **Onset pattern**: Insidious, slowly progressive over years to decades
- **Mode of presentation**: Variable - may begin with ptosis, dysphagia, or limb weakness depending on subtype

### Progression
- **Disease stages**: Not formally staged, but progressive worsening of weakness
- **Progression rate**: Slow, over decades
- **Disease course pattern**: Progressive, chronic
- **Disease duration**: Lifelong, chronic condition

### Patterns
- **Remission**: No spontaneous remissions documented
- **Critical periods**: Age-dependent onset influenced by repeat methylation status; earlier onset correlates with longer repeat lengths in GIPC1 and NOTCH2NLC (eura2025complexassociationsof pages 1-5, eura2026pathogeniccggexpansions pages 1-2)

## 9. Inheritance and Population

### Epidemiology
- **Prevalence**: Rare disease; approximately 300 individuals reported worldwide as of recent reviews (deng2020expansionofggc pages 1-2, ishiura2023recentadvancesin pages 2-3)
- **Incidence**: Not established due to rarity
- **Geographic distribution**: Predominantly East Asian populations (Japan, China), with cases also reported from Thailand, Netherlands, Turkey, England, Italy, and other regions (deng2020expansionofggc pages 1-2, ishiura2023recentadvancesin pages 2-3)

### For Genetic Etiology

**Inheritance Pattern**: Autosomal dominant with variable penetrance and incomplete penetrance noted (deng2020expansionofggc pages 1-2, eura2025complexassociationsof pages 1-5, ishiura2023recentadvancesin pages 2-3)

**Penetrance**: Incomplete; age-dependent with influence from repeat methylation status. Asymptomatic carriers with heavily methylated long repeats have been documented (eura2025complexassociationsof pages 1-5).

**Expressivity**: Variable; phenotypic spectrum ranges from isolated myopathy to multisystem neurodegeneration depending on affected gene

**Genetic Anticipation**: Not formally established, though somatic instability and intergenerational transmission warrant further study

**Germline Mosaicism**: Not explicitly documented in retrieved texts

**Founder Effects**: Distinct SNP haplotypes flanking LRP12 and GIPC1 expansions suggest founder effects in affected populations (eura2025complexassociationsof pages 1-5, eura2026pathogeniccggexpansions pages 1-2)

**Consanguinity Role**: Not a prominent feature given autosomal dominant inheritance

**Carrier Frequency**: Not systematically established; OPDM is rare

### Population Demographics

**Affected Populations**: Predominantly Japanese and Chinese populations. "Most cases of OPDM were reported from Japan and China, whereas only 13 families were reported from other regions such as Thai, Netherlands, Turkey, England, and Italy until 2019" (ishiura2023recentadvancesin pages 2-3).

**Sex Ratio**: Both males and females affected; no clear sex predilection evident in case series (ogasawara2020cggexpansionin pages 2-4)

**Age Distribution**: Adult-onset disease; most patients symptomatic by 40s-60s

## 10. Diagnostics

### Clinical Tests

**Laboratory Tests:**
- **Serum creatine kinase (CK)**: Elevated in most cases (range 63-1886 IU/L in one series), indicating muscle damage (ogasawara2020cggexpansionin pages 2-4)
- **CSF analysis**: Generally normal or mildly elevated protein (60-157 mg/dL reported); cell count typically <10/µL (ogasawara2020cggexpansionin pages 2-4)
- **Lactate**: Mildly elevated in some cases (9.7-21.6 mg/dL), potentially reflecting mitochondrial involvement (ogasawara2020cggexpansionin pages 2-4)

**Biomarkers:**
- **p62/SQSTM1-positive inclusions**: Hallmark in muscle and other tissues
- **Polyglycine proteins**: Recently developed antibodies can detect subtype-specific polyglycine proteins (uGIPpolyG, uN2CpolyG, asRILpolyG, LOC6polyG) in tissue inclusions (boivin2026ggcrepeatexpansions pages 1-2)

**Imaging Studies:**
- **Brain MRI**: Diffusion-weighted imaging (DWI) hyperintensities at corticomedullary junctions, leukoencephalopathy, cerebellar/cerebral atrophy in OPDM3/OPML (ogasawara2020cggexpansionin pages 2-4, ishiura2023recentadvancesin pages 2-3)
- **Muscle MRI/CT**: Asymmetric muscle atrophy and fat replacement, distal-predominant changes (ogasawara2020cggexpansionin pages 2-4)

**Electrophysiology:**
- **EMG**: Myopathic changes (short-duration, low-amplitude motor unit potentials)
- **Nerve conduction studies**: Slowed motor/sensory velocities or decreased amplitudes in cases with peripheral neuropathy (ogasawara2020cggexpansionin pages 2-4)

**Muscle Biopsy:**
- **Histochemistry**: Rimmed vacuoles (modified Gomori trichrome), small angular fibers, internal nuclei, chronic myopathic changes
- **Immunohistochemistry**: p62-positive intranuclear inclusions in myonuclei and non-muscle cells (blood vessels, nerve bundles, muscle spindles) - this pattern differentiates OPDM from OPMD (ogasawara2022intranuclearinclusionsin pages 1-2)
- **Electron microscopy**: Intranuclear filamentous inclusions (10-18 nm diameter, distinct from OPMD's 8.5 nm) (ishiura2023recentadvancesin pages 2-3)

**Skin Biopsy:**
- Can demonstrate intranuclear inclusions in NOTCH2NLC-associated cases (ogasawara2020cggexpansionin pages 2-4)

### Genetic Testing

**Recommended Approach**: Targeted genetic testing for CGG/GGC repeat expansions in known OPDM genes

**Methods:**
1. **Repeat-primed PCR (RP-PCR)**: Initial screening method for detecting expanded repeats (deng2020expansionofggc pages 1-2, ogasawara2020cggexpansionin pages 1-2)
2. **Amplicon-length PCR (AL-PCR) / Fluorescence AL-PCR**: Sizing of repeat expansions (deng2020expansionofggc pages 1-2, yu2021theggcrepeat pages 1-2)
3. **Southern blotting**: Confirmation and accurate sizing of large expansions (ogasawara2020cggexpansionin pages 1-2, yu2021theggcrepeat pages 1-2)
4. **Long-read sequencing (Oxford Nanopore)**: Comprehensive repeat characterization, methylation analysis (deng2020expansionofggc pages 1-2, yu2021theggcrepeat pages 1-2)
5. **CRISPR/Cas9-targeted nanopore sequencing (nCATS)**: Advanced method for simultaneous analysis of repeat length, flanking sequences, haplotypes, structural variation, and CpG methylation (eura2025complexassociationsof pages 1-5, eura2026pathogeniccggexpansions pages 1-2)

**Gene Panels**: Should include LRP12, GIPC1, NOTCH2NLC, RILPL1, LOC642361/NUTM2B-AS1, and ABCD3

**Single Gene Testing**: Appropriate when specific subtype suspected based on phenotype

**Whole Exome/Genome Sequencing**: May miss repeat expansions due to technical limitations; dedicated repeat-expansion methods required

### Clinical Criteria

**Diagnostic Criteria**: OPDM is diagnosed based on:
1. Characteristic clinical features (ptosis, ophthalmoplegia, bulbar weakness, distal limb weakness)
2. Myopathological findings (rimmed vacuoles, intranuclear inclusions)
3. Genetic confirmation of CGG/GGC repeat expansion
4. Exclusion of OPMD (PABPN1 GCN expansion) and myotonic dystrophy (DMPK CTG expansion)

**Differential Diagnosis:**
- **Oculopharyngeal muscular dystrophy (OPMD)**: Distinguished by proximal>distal weakness, 8.5 nm intranuclear filaments, frequent myo-INIs (>5.9%), and PABPN1 GCN expansion. OPDM has non-muscle INIs and rare myo-INIs (<2.8%) (ogasawara2022intranuclearinclusionsin pages 1-2)
- **Myotonic dystrophy type 1**: DMPK CTG expansion, myotonia
- **Mitochondrial myopathies**: May have ptosis and ophthalmoplegia but distinct histology
- **Inclusion body myositis**: Inflammatory myopathy with rimmed vacuoles but different clinical pattern

### Screening
- **Newborn screening**: Not applicable
- **Carrier screening**: Not routine given rarity and incomplete penetrance
- **Cascade screening**: May be considered in families with identified pathogenic expansions

## 11. Outcome/Prognosis

### Survival and Mortality
- **Life expectancy**: Not systematically studied; disease is progressive but not typically immediately life-threatening
- **Mortality rate**: No specific mortality data available in retrieved literature
- **Disease-specific mortality**: Complications from dysphagia (aspiration) and respiratory involvement may contribute to mortality

### Morbidity and Function
- **Morbidity**: Progressive disability from muscle weakness, dysphagia, and visual impairment
- **Disability outcomes**: Increasing dependence for activities of daily living, mobility aids, feeding assistance
- **Quality of life**: Significantly impacted by dysphagia, ophthalmoplegia, and limb weakness

### Disease Course
- **Complications**: Aspiration pneumonia from dysphagia, malnutrition, falls from muscle weakness, peripheral neuropathy complications
- **Recovery potential**: No recovery; progressive deterioration is the rule

### Prediction
- **Prognostic factors**: 
  - Longer CGG repeats correlate with earlier onset in GIPC1 and NOTCH2NLC (eura2025complexassociationsof pages 1-5, eura2026pathogeniccggexpansions pages 1-2)
  - Methylation status modifies onset in LRP12 (eura2025complexassociationsof pages 1-5, eura2026pathogeniccggexpansions pages 1-2)
  - NOTCH2NLC-associated cases may have more multisystem involvement (ogasawara2020cggexpansionin pages 2-4)
- **Prognostic biomarkers**: Repeat length and methylation status

## 12. Treatment

### Pharmacotherapy
Currently, no disease-modifying pharmacological treatments are available for OPDM. Management is supportive and symptomatic.

**Experimental Therapeutics:**
- **Idebenone**: Showed promise in a Drosophila model of NOTCH2NLC-related disease. "Idebenone treatment restored mitochondrial function and alleviated neurodegenerative phenotypes in transgenic flies" (yu2022cggrepeatexpansion pages 1-2). Clinical trials have not been reported.
- **TMPyP4 (cationic porphyrin)**: A 2026 study identified TMPyP4 as reducing polyglycine protein abundance and toxicity in cell cultures and animal models by targeting translation (boivin2026ggcrepeatexpansions pages 7-8). This represents a proof-of-concept therapeutic approach but is not yet in clinical use.

### Advanced Therapeutics
- **Gene therapy**: Not developed for OPDM
- **RNA-based therapies**: Antisense oligonucleotides (ASOs) targeting expanded CGG-repeat RNAs are theoretically applicable but not yet developed for OPDM
- **CRISPR-based approaches**: Could theoretically target repeat expansions but not clinically available

### Surgical and Interventional
- **Ptosis surgery**: May improve visual field
- **Gastrostomy tube (PEG)**: For severe dysphagia to maintain nutrition and prevent aspiration
- **Tracheostomy**: May be required if respiratory muscles severely affected

### Supportive and Rehabilitative
- **Supportive care**: 
  - Dysphagia management: Modified diet consistencies, speech-language pathology evaluation
  - Nutritional support: Dietitian consultation
  - Respiratory support: Monitoring of pulmonary function
- **Rehabilitation**:
  - Physical therapy: Maintain mobility and prevent contractures
  - Occupational therapy: Adaptive devices for activities of daily living
  - Speech therapy: Swallowing exercises, communication strategies

### Experimental
- Phase I/II trials: None identified in retrieved literature

### Treatment Outcomes
No systematic treatment outcome data are available given the lack of disease-modifying therapies.

### Treatment Strategy
**Multidisciplinary Approach**:
- Neurology/neuromuscular specialist
- Ophthalmology (for ptosis, ophthalmoplegia)
- Speech-language pathology (dysphagia)
- Physical and occupational therapy
- Nutritional support
- Genetic counseling

## 13. Prevention

### Prevention Levels
- **Primary prevention**: Not applicable for genetic disease
- **Secondary prevention**: Early genetic diagnosis allows anticipatory guidance and symptomatic management
- **Tertiary prevention**: Management of dysphagia, prevention of aspiration pneumonia, fall prevention

### Immunization
Not applicable.

### Screening and Early Detection
- **Genetic screening**: Family members of affected individuals may consider predictive genetic testing
- **Preimplantation genetic diagnosis (PGD)**: Theoretically possible for families with known pathogenic expansions
- **Prenatal testing**: Technically feasible but ethical considerations apply given adult onset and variable penetrance

### Behavioral Interventions
Not applicable.

### Counseling
**Genetic counseling**: Recommended for:
- Affected individuals understanding inheritance and recurrence risk
- At-risk family members considering predictive testing
- Reproductive planning

### Public Health
Not applicable for this rare genetic disorder.

### Prophylaxis
Not applicable.

## 14. Other Species / Natural Disease

### Taxonomy
No naturally occurring OPDM has been documented in other species.

### Natural Disease
No spontaneous animal models identified in retrieved literature.

## 15. Model Organisms

### Model Types

**Drosophila melanogaster (Fruit Fly):**
A transgenic fly model expressing uN2CpolyG (NOTCH2NLC-associated polyglycine) was developed by Yu et al. (2022). The model recapitulates key disease features:
- Progressive neuronal cell loss
- Locomotor deficiency
- Shortened lifespan  
- Mitochondrial swelling and dysfunction
- p62-positive inclusions

The fly model was used to identify idebenone as a therapeutic candidate targeting mitochondrial dysfunction (yu2022cggrepeatexpansion pages 1-2).

**Mus musculus (Mouse):**
Mouse models have been generated using recombinant adeno-associated viral (rAAV) vectors to express polyglycine proteins in skeletal muscle and CNS:
- Muscle-specific expression causes myofiber atrophy, centralized nuclei, p62-positive inclusions, and histological changes resembling human OPDM (boivin2026ggcrepeatexpansions pages 5-6, boivin2026ggcrepeatexpansions pages 7-8)
- CNS expression causes progressive motor deficits, coordination changes, neuroinflammation, Purkinje cell loss, and reduced lifespan (boivin2026ggcrepeatexpansions pages 5-6, boivin2026ggcrepeatexpansions pages 7-8)
- Different polyglycine proteins (uGIPpolyG, uN2CpolyG, LOC6polyG, asRILpolyG) show varying toxicity profiles, with LOC6polyG and uN2CpolyG showing more severe phenotypes than uGIPpolyG (boivin2026ggcrepeatexpansions pages 5-6, boivin2026ggcrepeatexpansions pages 7-8)

### Genetic Models
- **Transgenic**: Fly and mouse models expressing polyglycine proteins under various promoters
- **Viral transduction**: rAAV-mediated delivery in mouse muscle and CNS

### Model Characteristics

**Phenotype Recapitulation:**
- Polyglycine protein aggregation and p62-positive inclusions: Yes
- Muscle pathology (atrophy, centralized nuclei): Yes
- Neurodegeneration: Yes
- Mitochondrial dysfunction: Yes (fly model)
- Progressive locomotor deficits: Yes

**Model Limitations:**
- Do not fully capture the slowly progressive, decades-long human disease course
- Single-gene models may not reflect genetic heterogeneity
- Methylation-mediated modulation of phenotype not extensively modeled

### Applications
- Mechanistic studies of polyglycine toxicity
- Testing of therapeutic candidates (idebenone, TMPyP4)
- Understanding mitochondrial involvement
- Dissecting cell-autonomous vs. non-autonomous pathology

### Resources
- Drosophila models: Available through research groups (Yu, Deng, Wang laboratories)
- Mouse models: rAAV constructs and protocols described in recent publications

---

## Summary and Key Insights

Oculopharyngodistal myopathy represents a genetically heterogeneous group of adult-onset myopathies caused by CGG/GGC trinucleotide repeat expansions in at least six different genes. Recent breakthroughs (2020-2026) have dramatically advanced our understanding:

1. **Unified Molecular Mechanism**: Despite genetic heterogeneity, all OPDM subtypes share a common pathogenic mechanism involving RAN translation of expanded CGG repeats into toxic polyglycine-containing proteins that aggregate and cause cellular dysfunction (boivin2026ggcrepeatexpansions pages 1-2, li2026translationofexpanded pages 3-5, boivin2026ggcrepeatexpansions pages 5-6).

2. **Dual Pathogenesis**: Both protein toxicity (polyglycine aggregates) and RNA toxicity (RNA foci) likely contribute to disease (ishiura2023recentadvancesin pages 2-3).

3. **Epigenetic Modulation**: CpG methylation of expanded repeats modulates penetrance and age of onset, explaining incomplete penetrance and asymptomatic carriers (eura2025complexassociationsof pages 1-5, eura2026pathogeniccggexpansions pages 1-2).

4. **Phenotypic Spectrum**: While core myopathic features are shared, NOTCH2NLC-associated OPDM3 often includes multisystem neurological involvement, overlapping with NIID and forming part of the "FNOP spectrum" (ishiura2023recentadvancesin pages 1-2, ishiura2023recentadvancesin pages 2-3).

5. **Diagnostic Advances**: Long-read sequencing and CRISPR/Cas9-targeted approaches now enable comprehensive repeat characterization including length, methylation, and structural variation (eura2025complexassociationsof pages 1-5, eura2026pathogeniccggexpansions pages 1-2).

6. **Therapeutic Prospects**: Proof-of-concept therapeutics targeting polyglycine expression (TMPyP4) and mitochondrial function (idebenone) offer hope for future disease-modifying treatments (boivin2026ggcrepeatexpansions pages 7-8, yu2022cggrepeatexpansion pages 1-2).

This comprehensive report synthesizes current knowledge (2020-2026) on OPDM, providing a foundation for disease knowledge base curation, diagnostic algorithm development, and therapeutic research directions.

---

**Note**: This report prioritizes recent sources (2023-2026) while incorporating landmark earlier studies. All major claims are cited with PMIDs where available through the pqac citation system. The report is structured for direct use in populating a disease knowledge base with ontology terms, evidence items, and detailed annotations.

References

1. (deng2020expansionofggc pages 1-2): Jianwen Deng, Jiaxi Yu, Pidong Li, Xinghua Luan, Li Cao, Juan Zhao, Meng Yu, Wei Zhang, He Lv, Zhiying Xie, LingChao Meng, Yiming Zheng, Yawen Zhao, Qiang Gang, Qingqing Wang, Jing Liu, Min Zhu, Xueyu Guo, Yanan Su, Yu Liang, Fan Liang, Tomohiro Hayashi, Meiko Hashimoto Maeda, Tatsuro Sato, Shigehisa Ura, Yasushi Oya, Masashi Ogasawara, Aritoshi Iida, Ichizo Nishino, Chang Zhou, Chuanzhu Yan, Yun Yuan, Daojun Hong, and Zhaoxia Wang. Expansion of ggc repeat in gipc1 is associated with oculopharyngodistal myopathy. The American Journal of Human Genetics, 106:793-804, Jun 2020. URL: https://doi.org/10.1016/j.ajhg.2020.04.011, doi:10.1016/j.ajhg.2020.04.011. This article has 162 citations.

2. (ogasawara2020cggexpansionin pages 1-2): Masashi Ogasawara, Aritoshi Iida, Theerawat Kumutpongpanich, Ayami Ozaki, Yasushi Oya, Hirofumi Konishi, Akinori Nakamura, Ryuta Abe, Hiroshi Takai, Ritsuko Hanajima, Hiroshi Doi, Fumiaki Tanaka, Hisayoshi Nakamura, Ikuya Nonaka, Zhaoxia Wang, Shinichiro Hayashi, Satoru Noguchi, and Ichizo Nishino. Cgg expansion in notch2nlc is associated with oculopharyngodistal myopathy with neurological manifestations. Acta Neuropathologica Communications, Nov 2020. URL: https://doi.org/10.1186/s40478-020-01084-4, doi:10.1186/s40478-020-01084-4. This article has 122 citations and is from a peer-reviewed journal.

3. (wagner2018mappingthechromosomal pages 1-6): Matias Wagner. Mapping the chromosomal locus of oculopharyngodistal myopathy with microsatellite markers and next generation sequencing. Dissertation, Jan 2018. URL: https://doi.org/10.5282/edoc.22478, doi:10.5282/edoc.22478. This article has 0 citations.

4. (ishiura2023recentadvancesin pages 1-2): Hiroyuki Ishiura, Shoji Tsuji, and Tatsushi Toda. Recent advances in cgg repeat diseases and a proposal of fragile x-associated tremor/ataxia syndrome, neuronal intranuclear inclusion disease, and oculophryngodistal myopathy (fnop) spectrum disorder. Journal of Human Genetics, 68:169-174, Jan 2023. URL: https://doi.org/10.1038/s10038-022-01116-y, doi:10.1038/s10038-022-01116-y. This article has 26 citations and is from a peer-reviewed journal.

5. (ishiura2023recentadvancesin pages 2-3): Hiroyuki Ishiura, Shoji Tsuji, and Tatsushi Toda. Recent advances in cgg repeat diseases and a proposal of fragile x-associated tremor/ataxia syndrome, neuronal intranuclear inclusion disease, and oculophryngodistal myopathy (fnop) spectrum disorder. Journal of Human Genetics, 68:169-174, Jan 2023. URL: https://doi.org/10.1038/s10038-022-01116-y, doi:10.1038/s10038-022-01116-y. This article has 26 citations and is from a peer-reviewed journal.

6. (boivin2026ggcrepeatexpansions pages 1-2): Manon Boivin, Jiaxi Yu, Nobuyuki Eura, Léa Schmitt, David Pietri, Erwan Grandgirard, Patrice Goetz-Reiner, Damien Plassard, Chadia Nahy, Anne Maglott, Bastien Morlet, Chao Gao, Elise Lefebvre, Muriel Philipps, Pascal Eberling, Angélique Pichot, Paola Rossolillo, Christelle Thibault, Mustapha Oulad-Abdelghani, Ichizo Nishino, Kang Yang, Ning Wang, Zhaoxia Wang, Jianwen Deng, and Nicolas Charlet-Berguerand. Ggc repeat expansions within new open reading frames are translated into toxic polyglycine proteins in oculopharyngodistal myopathy. Nature Genetics, 58:517-529, Feb 2026. URL: https://doi.org/10.1038/s41588-026-02507-z, doi:10.1038/s41588-026-02507-z. This article has 6 citations and is from a highest quality peer-reviewed journal.

7. (eura2026pathogeniccggexpansions pages 1-2): Nobuyuki Eura, Satoru Noguchi, Megumu Ogawa, Kyuto Sonehara, Ai Yamanaka, Takashi Kurashige, Shinichiro Hayashi, Yukinori Okada, Kazuma Sugie, and Ichizo Nishino. Pathogenic cgg expansions in oculopharyngodistal myopathy exhibit distinct characteristics of each causative gene on the flanking sequences as well as methylation status. Genome Medicine, Mar 2026. URL: https://doi.org/10.1186/s13073-026-01617-x, doi:10.1186/s13073-026-01617-x. This article has 0 citations and is from a highest quality peer-reviewed journal.

8. (li2026translationofexpanded pages 1-2): Chengcheng Li, Jil A. Daw, Sara K. Pittman, Connor J. Maltby, Hidetoshi Sakurai, Peter K. Todd, and Conrad C. Weihl. Translation of expanded cgg repeats in lrp12 associated oculopharyngodistal myopathy. Acta Neuropathologica Communications, Mar 2026. URL: https://doi.org/10.1186/s40478-026-02272-4, doi:10.1186/s40478-026-02272-4. This article has 1 citations and is from a peer-reviewed journal.

9. (hobara2025linkinglrp12cgg pages 1-2): Takahiro Hobara, Masahiro Ando, Yujiro Higuchi, Jun-Hui Yuan, Akiko Yoshimura, Fumikazu Kojima, Yutaka Noguchi, Jun Takei, Yu Hiramatsu, Satoshi Nozuma, Tomonori Nakamura, Tadashi Adachi, Keiko Toyooka, Toru Yamashita, Yusuke Sakiyama, Akihiro Hashiguchi, Eiji Matsuura, Yuji Okamoto, and Hiroshi Takashima. Linking lrp12 cgg repeat expansion to inherited peripheral neuropathy. Journal of Neurology, Neurosurgery &amp; Psychiatry, 96:140-149, Jul 2025. URL: https://doi.org/10.1136/jnnp-2024-333403, doi:10.1136/jnnp-2024-333403. This article has 18 citations.

10. (deng2020expansionofggc pages 2-3): Jianwen Deng, Jiaxi Yu, Pidong Li, Xinghua Luan, Li Cao, Juan Zhao, Meng Yu, Wei Zhang, He Lv, Zhiying Xie, LingChao Meng, Yiming Zheng, Yawen Zhao, Qiang Gang, Qingqing Wang, Jing Liu, Min Zhu, Xueyu Guo, Yanan Su, Yu Liang, Fan Liang, Tomohiro Hayashi, Meiko Hashimoto Maeda, Tatsuro Sato, Shigehisa Ura, Yasushi Oya, Masashi Ogasawara, Aritoshi Iida, Ichizo Nishino, Chang Zhou, Chuanzhu Yan, Yun Yuan, Daojun Hong, and Zhaoxia Wang. Expansion of ggc repeat in gipc1 is associated with oculopharyngodistal myopathy. The American Journal of Human Genetics, 106:793-804, Jun 2020. URL: https://doi.org/10.1016/j.ajhg.2020.04.011, doi:10.1016/j.ajhg.2020.04.011. This article has 162 citations.

11. (boivin2026ggcrepeatexpansions pages 3-4): Manon Boivin, Jiaxi Yu, Nobuyuki Eura, Léa Schmitt, David Pietri, Erwan Grandgirard, Patrice Goetz-Reiner, Damien Plassard, Chadia Nahy, Anne Maglott, Bastien Morlet, Chao Gao, Elise Lefebvre, Muriel Philipps, Pascal Eberling, Angélique Pichot, Paola Rossolillo, Christelle Thibault, Mustapha Oulad-Abdelghani, Ichizo Nishino, Kang Yang, Ning Wang, Zhaoxia Wang, Jianwen Deng, and Nicolas Charlet-Berguerand. Ggc repeat expansions within new open reading frames are translated into toxic polyglycine proteins in oculopharyngodistal myopathy. Nature Genetics, 58:517-529, Feb 2026. URL: https://doi.org/10.1038/s41588-026-02507-z, doi:10.1038/s41588-026-02507-z. This article has 6 citations and is from a highest quality peer-reviewed journal.

12. (ogasawara2020cggexpansionin pages 2-4): Masashi Ogasawara, Aritoshi Iida, Theerawat Kumutpongpanich, Ayami Ozaki, Yasushi Oya, Hirofumi Konishi, Akinori Nakamura, Ryuta Abe, Hiroshi Takai, Ritsuko Hanajima, Hiroshi Doi, Fumiaki Tanaka, Hisayoshi Nakamura, Ikuya Nonaka, Zhaoxia Wang, Shinichiro Hayashi, Satoru Noguchi, and Ichizo Nishino. Cgg expansion in notch2nlc is associated with oculopharyngodistal myopathy with neurological manifestations. Acta Neuropathologica Communications, Nov 2020. URL: https://doi.org/10.1186/s40478-020-01084-4, doi:10.1186/s40478-020-01084-4. This article has 122 citations and is from a peer-reviewed journal.

13. (ogasawara2022intranuclearinclusionsin pages 1-2): Masashi Ogasawara, Nobuyuki Eura, Aritoshi Iida, Theerawat Kumutpongpanich, Narihiro Minami, Ikuya Nonaka, Shinichiro Hayashi, Satoru Noguchi, and Ichizo Nishino. Intranuclear inclusions in muscle biopsy can differentiate oculopharyngodistal myopathy and oculopharyngeal muscular dystrophy. Acta Neuropathologica Communications, Dec 2022. URL: https://doi.org/10.1186/s40478-022-01482-w, doi:10.1186/s40478-022-01482-w. This article has 21 citations and is from a peer-reviewed journal.

14. (boivin2026ggcrepeatexpansions pages 5-6): Manon Boivin, Jiaxi Yu, Nobuyuki Eura, Léa Schmitt, David Pietri, Erwan Grandgirard, Patrice Goetz-Reiner, Damien Plassard, Chadia Nahy, Anne Maglott, Bastien Morlet, Chao Gao, Elise Lefebvre, Muriel Philipps, Pascal Eberling, Angélique Pichot, Paola Rossolillo, Christelle Thibault, Mustapha Oulad-Abdelghani, Ichizo Nishino, Kang Yang, Ning Wang, Zhaoxia Wang, Jianwen Deng, and Nicolas Charlet-Berguerand. Ggc repeat expansions within new open reading frames are translated into toxic polyglycine proteins in oculopharyngodistal myopathy. Nature Genetics, 58:517-529, Feb 2026. URL: https://doi.org/10.1038/s41588-026-02507-z, doi:10.1038/s41588-026-02507-z. This article has 6 citations and is from a highest quality peer-reviewed journal.

15. (boivin2026ggcrepeatexpansions pages 7-8): Manon Boivin, Jiaxi Yu, Nobuyuki Eura, Léa Schmitt, David Pietri, Erwan Grandgirard, Patrice Goetz-Reiner, Damien Plassard, Chadia Nahy, Anne Maglott, Bastien Morlet, Chao Gao, Elise Lefebvre, Muriel Philipps, Pascal Eberling, Angélique Pichot, Paola Rossolillo, Christelle Thibault, Mustapha Oulad-Abdelghani, Ichizo Nishino, Kang Yang, Ning Wang, Zhaoxia Wang, Jianwen Deng, and Nicolas Charlet-Berguerand. Ggc repeat expansions within new open reading frames are translated into toxic polyglycine proteins in oculopharyngodistal myopathy. Nature Genetics, 58:517-529, Feb 2026. URL: https://doi.org/10.1038/s41588-026-02507-z, doi:10.1038/s41588-026-02507-z. This article has 6 citations and is from a highest quality peer-reviewed journal.

16. (eura2025complexassociationsof pages 1-5): Nobuyuki Eura, Satoru Noguchi, Megumu Ogawa, Kyuto Sonehara, Ai Yamanaka, Shinichiro Hayashi, Yukinori Okada, Kazuma Sugie, and Ichizo Nishino. Complex associations of genetic/epigenetic variations of cgg repeats with patient phenotypes in oculopharyngodistal myopathy. MedRxiv, May 2025. URL: https://doi.org/10.1101/2025.05.13.25327490, doi:10.1101/2025.05.13.25327490. This article has 1 citations.

17. (yu2021theggcrepeat pages 1-2): Jiaxi Yu, Jianwen Deng, Xueyu Guo, Jingli Shan, Xinghua Luan, Li Cao, Juan Zhao, Meng Yu, Wei Zhang, He Lv, Zhiying Xie, LingChao Meng, Yiming Zheng, Yawen Zhao, Qiang Gang, Qingqing Wang, Jing Liu, Min Zhu, Binbin Zhou, Pidong Li, Yinzhe Liu, Yang Wang, Chuanzhu Yan, Daojun Hong, Yun Yuan, and Zhaoxia Wang. The ggc repeat expansion in notch2nlc is associated with oculopharyngodistal myopathy type 3. Brain, 144:1819-1832, Mar 2021. URL: https://doi.org/10.1093/brain/awab077, doi:10.1093/brain/awab077. This article has 143 citations and is from a highest quality peer-reviewed journal.

18. (li2026translationofexpanded pages 3-5): Chengcheng Li, Jil A. Daw, Sara K. Pittman, Connor J. Maltby, Hidetoshi Sakurai, Peter K. Todd, and Conrad C. Weihl. Translation of expanded cgg repeats in lrp12 associated oculopharyngodistal myopathy. Acta Neuropathologica Communications, Mar 2026. URL: https://doi.org/10.1186/s40478-026-02272-4, doi:10.1186/s40478-026-02272-4. This article has 1 citations and is from a peer-reviewed journal.

19. (yu2022cggrepeatexpansion pages 1-2): Jiaxi Yu, Tongling Liufu, Yilei Zheng, Jin Xu, Lingchao Meng, Wei Zhang, Yun Yuan, Daojun Hong, Nicolas Charlet-Berguerand, Zhaoxia Wang, and Jianwen Deng. Cgg repeat expansion in notch2nlc causes mitochondrial dysfunction and progressive neurodegeneration in drosophila model. Proceedings of the National Academy of Sciences of the United States of America, Oct 2022. URL: https://doi.org/10.1073/pnas.2208649119, doi:10.1073/pnas.2208649119. This article has 57 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Oculopharyngodistal_Myopathy-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Oculopharyngodistal_Myopathy-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Oculopharyngodistal_Myopathy-deep-research-falcon_artifacts/artifact-02.md)