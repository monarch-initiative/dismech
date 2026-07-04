---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-30T10:32:28.196710'
end_time: '2026-06-30T10:48:17.075250'
duration_seconds: 948.88
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Viral Encephalitis
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 57
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Viral_Encephalitis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Viral_Encephalitis-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Viral_Encephalitis-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Viral Encephalitis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Viral Encephalitis** covering all of the
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
- **Disease Name:** Viral Encephalitis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Viral Encephalitis** covering all of the
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


# Comprehensive Research Report: Viral Encephalitis (MONDO_0006009)

## Target Disease
- **Disease Name:** Viral Encephalitis
- **MONDO ID:** MONDO_0006009
- **Category:** Infectious Disease

---
## 1. Disease Information

Viral encephalitis is inflammation of the brain parenchyma due to viral infection, presenting as a neurologic emergency with high morbidity and mortality. Key identifiers: 
- **MONDO:** MONDO_0006009 ("viral encephalitis")
- **ICD-10:** A85-A89 (various viral encephalitides), A86 for "unspecified viral encephalitis"
- **MeSH:** D004677 ("Encephalitis, Viral")
- **OMIM:** Not a single entry; virus-specific (e.g., OMIM:603705 for HSV-1)
- **Orphanet:** ORPHA:230475 ("viral encephalitis")

Common synonyms: "viral meningoencephalitis", "acute viral encephalitis", "primary viral encephalitis". Information here is derived from aggregated disease-level resources and primary literature.

---
## 2. Etiology

Viral encephalitis is caused by neurotropic viruses. Principal viral agents include:
| Virus family | Virus | Typical transmission route | Geographic distribution / epidemiology | Case fatality rate / severity notes |
|---|---|---|---|---|
| **Herpesviridae** | **HSV-1** | Reactivation or primary infection with neural spread to CNS; trans-synaptic spread from trigeminal/olfactory pathways | Worldwide; leading cause of sporadic, non-epidemic encephalitis in developed settings; HSV accounts for >90% of encephalitis cases among immunocompetent adults in HSV encephalitis series (cleaver2024theimmunobiologyof pages 2-2, yang2023advancesinviral pages 2-3, cleaver2024theimmunobiologyof pages 3-4) | Untreated HSE mortality historically ~70%; with aciclovir, mortality falls to ~10–25%; long-term neurologic disability remains common (cleaver2024theimmunobiologyof pages 2-2) |
| **Herpesviridae** | **HSV-2** | Perinatal/neonatal transmission most important for encephalitic disease; less commonly adult CNS infection | Worldwide; causes ~80% of neonatal HSV CNS cases in cited review (yang2023advancesinviral pages 2-3) | Specific CFR not consistently separated from HSV-1 in retrieved evidence; neonatal disease can be severe and life-threatening (yang2023advancesinviral pages 2-3) |
| **Flaviviridae** | **Japanese encephalitis virus (JEV)** | Mosquito-borne | Endemic in Southeast Asia and the Western Pacific; most common epidemic viral encephalitis globally; ~68,000 cases annually, with ~1.15 billion people at risk (cleaver2024theimmunobiologyof pages 2-2, yang2023advancesinviral pages 1-2) | Review evidence notes 10,000–15,000 deaths annually; severe neurologic sequelae common among survivors (yang2023advancesinviral pages 1-2) |
| **Flaviviridae** | **West Nile virus (WNV)** | Mosquito-borne | Africa, Europe, Middle East, North America, West Asia; important cause of arboviral neuroinvasive disease, including in Europe (yang2023advancesinviral pages 1-2, yang2023advancesinviral pages 2-3) | In retrieved evidence, exact CFR for encephalitis not consistently quantified; recognized cause of severe neuroinvasive disease with substantial morbidity (yang2023advancesinviral pages 1-2, yang2023advancesinviral pages 2-3) |
| **Flaviviridae** | **Tick-borne encephalitis virus (TBEV)** | Ixodes tick bite; less often alimentary transmission via unpasteurized dairy | Focally endemic in Europe and Asia; ~5,000–10,000 human cases annually in endemic areas; highest incidence in older adults, male predominance (hills2023tickborneencephalitisvaccine pages 5-6) | Mortality varies by subtype; severe disease risk higher in age ≥60, immunocompromise, and Far Eastern subtype infection; often causes permanent neurologic/cognitive sequelae (hills2023tickborneencephalitisvaccine pages 5-6) |
| **Flaviviridae** | **Zika virus (ZIKV)** | Primarily mosquito-borne; also sexual, vertical, and transfusion routes recognized broadly | Tropics/subtropics with outbreaks in the Americas, Pacific, Asia, and Africa; included among major neurotropic RNA viruses causing VE (yang2023advancesinviral pages 1-2, yang2023advancesinviral pages 2-3) | Exact encephalitis CFR not established in retrieved evidence; neurologic disease recognized but encephalitis less common than congenital/CNS developmental complications (yang2023advancesinviral pages 1-2) |
| **Flaviviridae** | **Dengue virus (DENV)** | Mosquito-borne | Global tropical/subtropical distribution; increasing autochthonous transmission in Europe noted in recent review (yang2023advancesinviral pages 1-2) | Exact encephalitis CFR not given in retrieved evidence; dengue can be neuropathogenic and contribute to VE burden (yang2023advancesinviral pages 1-2) |
| **Togaviridae / Alphavirus** | **Eastern equine encephalitis virus (EEEV)** | Mosquito-borne; laboratory aerosol exposure also documented | Primarily eastern North America; average ~11 annual human cases, but outbreaks occur (woodson2025neuropathogenesisofencephalitic pages 6-8) | High CFR ~30–75%; among survivors, 50–90% experience neurologic sequelae (woodson2025neuropathogenesisofencephalitic pages 6-8, woodson2025neuropathogenesisofencephalitic pages 3-4) |
| **Togaviridae / Alphavirus** | **Venezuelan equine encephalitis virus (VEEV)** | Mosquito-borne; aerosol exposure possible in laboratory/biothreat settings | Americas; causes epizootic and enzootic disease in humans and equids (woodson2025neuropathogenesisofencephalitic pages 3-4, woodson2025neuropathogenesisofencephalitic pages 1-3) | Overall mortality usually <1%, but can reach ~10% in adults with neurologic disease and ~35% in children in cited review (woodson2025neuropathogenesisofencephalitic pages 3-4) |
| **Togaviridae / Alphavirus** | **Western equine encephalitis virus (WEEV)** | Mosquito-borne | Historically Americas, especially western North America (woodson2025neuropathogenesisofencephalitic pages 3-4, woodson2025neuropathogenesisofencephalitic pages 1-3) | CFR ~3–15%; neurologic sequelae common in survivors (woodson2025neuropathogenesisofencephalitic pages 3-4) |
| **Rhabdoviridae** | **Rabies virus** | Animal bite with saliva inoculation; neuronal spread to CNS | Worldwide, especially Asia and Africa; classic neurotropic encephalitic virus included among major VE causes (yang2023advancesinviral pages 1-2, yang2023advancesinviral pages 2-3) | Once clinical encephalitis develops, rabies is typically nearly uniformly fatal; exact figure not quantified in retrieved evidence (yang2023advancesinviral pages 1-2, yang2023advancesinviral pages 2-3) |
| **Picornaviridae** | **Enteroviruses (e.g., EV71)** | Fecal-oral, respiratory, close contact | Worldwide, especially pediatric populations in Asia-Pacific outbreaks; important cause of viral CNS infection (yang2023advancesinviral pages 1-2, yang2023advancesinviral pages 2-3) | Exact CFR for encephalitis not consistently reported in retrieved evidence; can cause severe pediatric brainstem encephalitis and neurologic complications (yang2023advancesinviral pages 2-3) |
| **Coronaviridae** | **SARS-CoV-2** | Respiratory transmission | Worldwide pandemic distribution; included among major RNA viruses associated with VE and post-infectious CNS syndromes (yang2023advancesinviral pages 1-2, loscher2022molecularmechanismsin pages 1-2) | Exact CFR for encephalitis not established in retrieved evidence; neurologic involvement recognized but heterogeneous (yang2023advancesinviral pages 1-2, loscher2022molecularmechanismsin pages 1-2) |
| **Paramyxoviridae** | **Measles virus** | Respiratory droplets / airborne | Worldwide where vaccination gaps persist; included among viral encephalitis pathogens and also relevant to post-vaccine susceptibility syndromes in interferon-pathway deficiencies (yang2023advancesinviral pages 1-2, OpenTargets Search: viral encephalitis,encephalitis) | Exact encephalitis CFR not quantified in retrieved evidence; measles encephalitis can be severe/fatal (yang2023advancesinviral pages 1-2) |
| **Orthomyxoviridae / Pneumoviridae and others** | **Respiratory viruses with encephalitic complications (e.g., RSV, influenza)** | Respiratory transmission | Worldwide; RSV meta-analysis found encephalitis/encephalopathy is uncommon but notable across adults and children (yang2023advancesinviral pages 1-2) | RSV-associated encephalitis/encephalopathy pooled prevalence ~2.20 per 100 RSV cases; case fatality 0.43% in observational studies and 10.71% in case reports, reflecting publication bias (yang2023advancesinviral pages 1-2) |


*Table: This table summarizes the principal viral causes of viral encephalitis by virus family, with transmission route, geographic distribution, and severity or case-fatality information based on the gathered evidence. It is useful for comparing the epidemiologic patterns and relative clinical severity of major encephalitic viruses.*

### Key Points:
- **Herpes simplex virus type 1 (HSV-1)** is the leading cause of sporadic fatal encephalitis in developed settings (incidence ~1/250,000-500,000/yr for HSV encephalitis in Western populations). HSV-2 causes most neonatal cases.
- **Flaviviruses** (e.g., JEV, WNV, TBEV) cause epidemic encephalitides, often mosquito- or tick-borne, with dramatic geographic and seasonal patterns (yang2023advancesinviral pages 1-2, hills2023tickborneencephalitisvaccine pages 5-6).
- **Alphaviruses** (EEEV, VEEV, WEEV) cause severe, often fatal, encephalitis in the Americas with high case fatality rates in several settings (woodson2025neuropathogenesisofencephalitic pages 6-8, woodson2025neuropathogenesisofencephalitic pages 3-4).
- **Rabies virus** causes nearly universally fatal encephalitis after clinical onset, especially in Asia and Africa (yang2023advancesinviral pages 2-3).
- **Incubation periods** vary: 6 days for most neurotropic RNA viruses, 7–14 days for tick-borne encephalitis (hills2023tickborneencephalitisvaccine pages 5-6).
- **Major risk factors:** older age (>60), immunocompromise, Far Eastern TBEV, genetic defects (see section 5), exposure to vector-borne pathogens.

---
## 3. Phenotypes

### Symptoms and Clinical Presentation
- **Fever, headache, altered mental status, behavioral changes, seizures** are cardinal symptoms (cleaver2024theimmunobiologyof pages 2-2, yang2023advancesinviral pages 2-3).
- **Focal neurologic signs** may occur, especially with HSV affecting the temporal lobe (cleaver2024theimmunobiologyof pages 2-2).
- **Neonatal disease** (HSV-2, enteroviruses, CMV) presents with more diffuse CNS involvement.
- **Prodromal symptoms:** mild fever, sore throat, cough, nausea, vomiting, myalgia, fatigue (yang2023advancesinviral pages 1-2).

### Laboratory Findings
- **CSF:** mild pleocytosis, elevated protein, and viral PCR or immunoglobulin M for diagnostic confirmation (cleaver2024theimmunobiologyof pages 2-2, hills2023tickborneencephalitisvaccine pages 5-6).
- **Imaging:** MRI showing temporally lobe hyperintensity (HSV), edema, demyelination (arboviruses).

### Disease Spectrum
- **Severity:** Ranges from asymptomatic or mild to severe coma, seizures, and death.
- **Long-term sequelae:** Intellectual disability, motor dysfunction, paralysis, speech and memory deficits, particularly in survivors of HSV, JEV, EEEV encephalitides (woodson2025neuropathogenesisofencephalitic pages 3-4, abbuehl2023canweforecast pages 12-13, abbuehl2023canweforecast pages 3-4).

### HPO Terms
- HP:0002353 (encephalitis), HP:0001250 (seizures), HP:0001288 (encephalopathy), HP:0002352 (meningoencephalitis), HP:0001289 (behavioral abnormality), HP:0002378 (memory impairment)

---
## 4. Genetic/Molecular Information

Viral encephalitis is rarely associated with chromosomal or Mendelian disease, except in the context of monogenic inborn errors of immunity—especially in herpes simplex encephalitis (HSE). See key susceptibility genes and their clinical implications here:
| Gene symbol | Gene name | Pathway involved | Inheritance pattern* | Clinical significance |
|---|---|---|---|---|
| UNC93B1 | unc-93 homolog B1, TLR signaling regulator | Endosomal TLR trafficking; upstream of TLR3/7/8/9-mediated type I IFN responses | AR; AD not established for HSE | First human gene clearly linked to isolated HSE susceptibility; impaired trafficking of TLR3 and related receptors reduces neuron-intrinsic antiviral defense against HSV-1 (zhang2024geneticdefectsof pages 3-4, zhang2024geneticdefectsof pages 13-15, skouboe2023inbornerrorsof pages 6-8) |
| TLR3 | toll-like receptor 3 | TLR3–TRIF–TBK1–IRF3 interferon pathway | AR and AD | Deficiency predisposes to childhood HSE with incomplete penetrance; TLR3 defects are reported in ~5% of HSE patients and impair CNS-intrinsic IFN-mediated control of HSV-1 (zhang2024geneticdefectsof pages 4-6, zhang2024geneticdefectsof pages 3-4, skouboe2023inbornerrorsof pages 6-8) |
| TICAM1 (TRIF) | TIR domain-containing adaptor molecule 1 | TLR3 adaptor signaling to TBK1/IRF3 | AR/AD reported in pathway defects; exact pattern varies by family | Loss impairs downstream TLR3 signaling and type I IFN induction, increasing risk of HSV CNS infection/HSE (skouboe2023inbornerrorsof pages 4-6, skouboe2023inbornerrorsof pages 6-8) |
| TRAF3 | TNF receptor-associated factor 3 | TLR3/RIG-I signaling to TBK1/IRF3 | AD reported for HSE-associated defects | Defects compromise antiviral interferon induction and are established monogenic causes of HSE susceptibility (skouboe2023inbornerrorsof pages 4-6, zhang2024geneticdefectsof pages 4-6, skouboe2023inbornerrorsof pages 6-8) |
| TBK1 | TANK-binding kinase 1 | TLR3/RIG-I signaling; IRF3 activation | AD reported for HSE-associated defects | Deficiency reduces interferon induction downstream of TLR3, predisposing to HSE and severe HSV CNS infection (skouboe2023inbornerrorsof pages 4-6, zhang2024geneticdefectsof pages 4-6, skouboe2023inbornerrorsof pages 6-8) |
| IRF3 | interferon regulatory factor 3 | Terminal transcription factor in TLR3/RIG-I/STING interferon signaling | AD reported; family-specific | HSE-associated variants impair IFN-α/β and IFN-λ responses in CNS-resident cells, enabling HSV-1 replication in brain tissue (zhang2024geneticdefectsof pages 4-6, skouboe2023inbornerrorsof pages 6-8) |
| IKBKG (NEMO) | inhibitor of nuclear factor kappa B kinase regulatory subunit gamma | NF-κB and IRF3-linked antiviral signaling; TLR3/RIG-I/STING related | XL | Mutations impair IFN-α/β and IFN-λ production and can cause selective susceptibility to HSE despite relative systemic immune competence (skouboe2023inbornerrorsof pages 4-6, zhang2024geneticdefectsof pages 3-4, zhang2024geneticdefectsof pages 13-15, skouboe2023inbornerrorsof pages 6-8) |
| IFNAR1 | interferon alpha and beta receptor subunit 1 | Type I IFN receptor signaling | AR | Deficiency disrupts IFN-α/β immunity crucial for CNS defense against HSV-1 and is a significant cause of HSE susceptibility (skouboe2023inbornerrorsof pages 4-6, zhang2024geneticdefectsof pages 4-6, skouboe2023inbornerrorsof pages 6-8) |
| STAT1 | signal transducer and activator of transcription 1 | Type I/III (and also IFN-γ) interferon receptor signaling | AR complete deficiency; other forms vary | Deficiency impairs cellular responses to interferons and is linked to severe HSV CNS infection/HSE (skouboe2023inbornerrorsof pages 4-6, zhang2024geneticdefectsof pages 3-4, zhang2024geneticdefectsof pages 13-15, skouboe2023inbornerrorsof pages 6-8) |
| TYK2 | tyrosine kinase 2 | IFNAR downstream signaling | AR | Defects impair type I IFN signaling and are associated with susceptibility to HSE/severe HSV infection in some patients (zhang2024geneticdefectsof pages 4-6, skouboe2023inbornerrorsof pages 6-8) |
| IRF9 | interferon regulatory factor 9 | ISGF3 complex; downstream IFNAR signaling | AR | Deficiency compromises ISG induction after IFNAR activation, predisposing to HSV CNS infection/HSE (skouboe2023inbornerrorsof pages 4-6, skouboe2023inbornerrorsof pages 6-8) |
| SNORA31 | small nucleolar RNA, H/ACA box 31 | IFN-independent, neuron-intrinsic antiviral defense | Presumed AR from reported deficiency cases | Identified as a noncanonical cause of HSE susceptibility; loss impairs cortical neuron intrinsic immunity to HSV-1 (skouboe2023inbornerrorsof pages 4-6, skouboe2023inbornerrorsof pages 1-2, zhang2024geneticdefectsof pages 13-15) |
| DBR1 | debranching RNA lariats 1 | RNA lariat metabolism; IFN-independent antiviral defense | AR | Variants impair RNA lariat metabolism and predispose to brainstem viral encephalitis/HSE-spectrum disease by weakening intrinsic antiviral restriction (skouboe2023inbornerrorsof pages 1-2, zhang2024geneticdefectsof pages 13-15, skouboe2023inbornerrorsof pages 10-11) |
| GTF3A | general transcription factor IIIA | 5S rRNA/RNA5SP141–RIG-I antiviral pathway | Not clearly established; likely AR in reported rare IEI | Newly identified mechanism of susceptibility in which disrupted RNA-mediated antiviral sensing compromises protection from HSV CNS infection (skouboe2023inbornerrorsof pages 4-6, skouboe2023inbornerrorsof pages 6-8) |
| RIPK3 | receptor interacting serine/threonine kinase 3 | Cell-death-dependent intrinsic antiviral defense; necroptosis/apoptosis control | AR | Inherited RIPK3 deficiency causes HSE by impairing neuronal death-mediated control of HSV-1 despite preserved IFN induction; highlights IFN-independent protection (zhang2024geneticdefectsof pages 1-3) |
| STAT2 | signal transducer and activator of transcription 2 | Type I IFN receptor signaling / ISGF3 | AR | Deficiency disrupts antiviral interferon signaling and is implicated in severe viral susceptibility; relevant to post-vaccine viral encephalitic vulnerability and broader HSV/CNS antiviral defense framework (zhang2024geneticdefectsof pages 4-6, OpenTargets Search: viral encephalitis,encephalitis) |
| IFNAR2 | interferon alpha and beta receptor subunit 2 | Type I IFN receptor signaling | AR | Deficiency impairs IFN-α/β signaling and is relevant to severe viral CNS susceptibility within the IFNAR pathway, though stronger evidence exists for vaccine-strain viral disease than classic HSE (OpenTargets Search: viral encephalitis,encephalitis) |
| TMEFF1 | tomoregulin-1 | Neuron-intrinsic restriction factor pathway | Not yet clearly defined | Emerging candidate restriction factor in brain immunity; proposed by Zhang & Casanova as part of newer antiviral pathways involved in HSE susceptibility (zhang2024geneticdefectsof pages 1-3) |

| *Inheritance abbreviations | Meaning |
|---|---|
| AR | autosomal recessive |
| AD | autosomal dominant |
| XL | X-linked |


*Table: This table summarizes key host genes implicated in susceptibility to viral encephalitis, especially childhood herpes simplex encephalitis, emphasizing the TLR3–interferon axis and newer neuron-intrinsic antiviral pathways. It is useful for linking monogenic immune defects to mechanism-based diagnosis and interpretation of severe HSV CNS infection.*

- Inborn errors in the **TLR3-interferon pathway** (UNC93B1, TLR3, TRIF, TRAF3, TBK1, IRF3, NEMO, IFNAR1, STAT1, TYK2, IRF9) account for up to 20% of childhood HSE cases. Some (e.g., STAT2, IFNAR2) are relevant for vaccine-strain viral infection post-MMR, while GTF3A, SNORA31, DBR1, TMEFF1, and RIPK3 point to newly-discovered intrinsic neuronal immune mechanisms (zhang2024geneticdefectsof pages 4-6, zhang2024geneticdefectsof pages 1-3, skouboe2023inbornerrorsof pages 6-8).
- All described pathogenic variants are rare, often segregate recessively, and primarily affect CNS-intrinsic, neuron-specific antiviral pathways, not systemic immune competence (zhang2024geneticdefectsof pages 1-3).

---
## 5. Environmental and Infectious Factors

- **Primary non-genetic factors:** Exposure to vector-borne viruses, seasonality (e.g., tick/mosquito activity), travel to endemic areas, consumption of unpasteurized dairy (TBE), lack of vaccination.
- **Infectious agent:** Virus is required; most cases involve no other predisposing exposures beyond infection (cleaver2024theimmunobiologyof pages 2-2, yang2023advancesinviral pages 1-2).

---
## 6. Mechanism / Pathophysiology

- **Causal chain:** Virus reaches CNS (via neural or hematogenous route) → neuroinvasion, often via blood-brain barrier (BBB) disruption or retrograde axonal transport (liu2023tcellsin pages 7-8, woodson2025neuropathogenesisofencephalitic pages 4-6, cleaver2024theimmunobiologyof pages 3-4, yang2023advancesinviral pages 3-4).
- **Molecular immune response:**
  - **Primary:** CNS-resident cell-intrinsic interferon (type I and III) production and downstream ISG induction. TLR3/UNC93B1 defects impair this defense.
  - **Secondary:** Cytokine responses (IL-6, IL-8, IL-1α, TNF-α, CXCL1, CCL2) cause neuroinflammation and BBB breakdown.
  - **Pathology:** Perivascular cuffing, gliosis, demyelination, neuronal loss, edema, inflammatory infiltrate (cleaver2024theimmunobiologyof pages 3-4, woodson2025neuropathogenesisofencephalitic pages 4-6, woodson2025neuropathogenesisofencephalitic pages 28-29).
- **Neuronal damage:** Direct viral cytotoxicity, excessive cytokine release, excitotoxicity, and immune-mediated injury.
- **Chronic consequences:** Persistent viral RNA, chronic inflammation, and metabolic/tryptophan pathway disruption may contribute to long-term cognitive deficits (woodson2025neuropathogenesisofencephalitic pages 28-29).

**GO terms:** GO:0006955 (immune response), GO:0030431 (sleep-wake cycle), GO:0005622 (intracellular), etc.
**CL terms:** CL:0000127 (neuron), CL:0000129 (astrocyte), CL:0000128 (microglia)

---
## 7. Anatomical Structures Affected

- **Organ:** Brain (temporal lobes—especially for HSV), spinal cord (meningoencephalomyelitis in some forms), occasionally brainstem and cerebellum (woodson2025neuropathogenesisofencephalitic pages 3-4, woodson2025neuropathogenesisofencephalitic pages 4-6).
- **System:** Central nervous system (primary), sometimes meninges.
- **Cell/Tissue:** Neurons, astrocytes, microglia, oligodendrocytes, especially CNS-resident populations (woodson2025neuropathogenesisofencephalitic pages 4-6, cleaver2024theimmunobiologyof pages 3-4).
- **Localization:** Lesions may be asymmetric (temporal lobe for HSV), bilateral, or brainstem-predominant (flaviviruses).

---
## 8. Temporal Development

- **Onset:** Acute (hours to days); occasionally subacute for post-infectious (e.g., autoimmune) forms.
- **Progression:** Rapid; prodrome advances to encephalopathy, seizures, focal deficits, coma if untreated.
- **Critical windows:** Delay in acyclovir initiation (>2 days) worsens outcomes in HSV cases (cleaver2024theimmunobiologyof pages 2-2, abbuehl2023canweforecast pages 5-5).

---
## 9. Inheritance and Population

- **Epidemiology:**
  - **Incidence:** Global: ~1.4/100,000/year; HSV encephalitis in Western nations: 1 in 250,000–500,000/year (cleaver2024theimmunobiologyof pages 2-2, yang2023advancesinviral pages 1-2)
  - **Prevalence (HSV):** 8% of patients with viral CNS infection (adult); higher rates in some pediatric outbreaks (yang2023advancesinviral pages 1-2, hills2023tickborneencephalitisvaccine pages 5-6).
  - **Geography:** Arboviral cases are endemic in Asia, Americas, Europe, depending on virus type (see artifact-01).
  - **Sex/Age:** Male predominance, bimodal age peaks (children, older adults in arboviruses), higher severity in older adults/immunocompromised.
- **Genetic epidemiology:** ~10-20% of childhood HSE due to true monogenic inborn errors (zhang2024geneticdefectsof pages 4-6, zhang2024geneticdefectsof pages 1-3).

---
## 10. Diagnostics

- **Mainstays:**
  - **Clinical:** Presentation and course (fever, encephalopathy, seizures)
  - **CSF analysis:** Pleocytosis, elevated protein, viral PCR/IgM (cleaver2024theimmunobiologyof pages 2-2, hills2023tickborneencephalitisvaccine pages 5-6)
  - **Imaging:** MRI (frontotemporal hyperintensity—HSV; multifocal lesions—arboviruses)
  - **Biomarkers:** Not yet universally validated for differentiation, though neurofilament light and cytokine patterns are under study (abbuehl2023canweforecast pages 5-6).
  - **Genetic testing:** Indicated in severe pediatric HSV cases, especially with family history or recurrence; panels should target TLR3-IFN pathway genes (skouboe2023inbornerrorsof pages 6-8).
- **Differential:** Other causes of encephalitis (bacterial, autoimmune, toxic, metabolic).

---
## 11. Outcome/Prognosis

- **Mortality:**
  - HSV-1: 70% if untreated, reduced to 10–25% with acyclovir (cleaver2024theimmunobiologyof pages 2-2, abbuehl2023canweforecast pages 12-13).
  - VZV: Mortality 0–15% (up to 33–36% in severe ICU cohorts) (abbuehl2023canweforecast pages 12-12).
  - EEEV: 30–75% mortality (woodson2025neuropathogenesisofencephalitic pages 6-8).
- **Morbidity:** 50–90% of survivors experience neurologic sequelae in EEEV, 50% in pediatric HSV, with motor, cognitive, or speech deficits (abbuehl2023canweforecast pages 12-13, woodson2025neuropathogenesisofencephalitic pages 3-4).
- **Prognostic factors:** Older age, immunocompromise, delay in antiviral treatment, need for mechanical ventilation, and severe imaging abnormalities at presentation (abbuehl2023canweforecast pages 5-5, abbuehl2023canweforecast pages 7-7).

---
## 12. Treatment

- **HSV Encephalitis:** Intravenous acyclovir is the standard of care; mortality falls substantially with prompt treatment (cleaver2024theimmunobiologyof pages 2-2).
   - Adjunctive steroids: Recent systematic review/meta-analysis found no conclusive benefit in viral encephalitis overall (abbuehl2023canweforecast pages 5-5).
- **Arbovirus/Alphavirus Encephalitis:** No specific antiviral therapies; management is supportive (woodson2025neuropathogenesisofencephalitic pages 6-8).
- **Tick-borne/Japanese Encephalitis:** No antivirals; some evidence for immunoglobulin support in severe Japanese encephalitis (clinical trials identified).
- **Immunotherapy:** In post-infectious autoimmune encephalitis, immunomodulation with IVIg, steroids, rituximab, or plasma exchange is used; for classic viral encephalitis, only tested in trials (abbuehl2023canweforecast pages 5-5).
- **Vaccines:** Available for TBEV, JEV (see section 13).
- **MAXO terms:** MAXO:0000625 (antiviral therapy), MAXO:0000796 (supportive care), MAXO:0000208 (immunomodulatory therapy)

---
## 13. Prevention

- **Primary:**
  - **Vaccines:** Highly effective for JEV, TBEV, yellow fever; not for WNV, rabies (except pre-exposure prophylaxis in specific settings) (hills2023tickborneencephalitisvaccine pages 5-6).
  - **Vector control, tick avoidance, pasteurized dairy,"Safe sex," and travel vaccination guidelines; see ACIP/CDC 2023 recommendations for TBE vaccine (hills2023tickborneencephalitisvaccine pages 5-6).
- **Secondary:**
  - Early diagnosis/treatment for higher-risk groups, genetic counseling in recurrent severe HSV cases;
- **Tertiary:**
  - Rehabilitation and long-term care for neurologic sequelae.

---
## 14. Other Species/Natural Disease

Major flaviviruses, alphaviruses, and rabies affect a wide range of domestic and wild animals, with encephalitic syndromes recapitulating elements of human disease (cleaver2024theimmunobiologyof pages 2-2, yang2023advancesinviral pages 1-2).

---
## 15. Model Organisms

| Model organism | Specific strains / types | Virus studied | Route of infection | Key features / phenotype recapitulation | Limitations |
|---|---|---|---|---|---|
| Mouse | C57BL/6 | VEEV, JEV, HSV-1 | Intranasal, subcutaneous, aerosol depending on study | Widely used immunocompetent model; develops encephalitic disease and allows study of host genetics, neuroinvasion, neuroinflammation, and neurological sequelae; useful for attenuated and virulent VEEV comparisons (yang2023advancesinviral pages 9-10, woodson2025neuropathogenesisofencephalitic pages 13-14, woodson2025neuropathogenesisofencephalitic pages 14-15) | Murine immune and neurobiology differ from humans; disease severity can depend strongly on strain and inoculation route (yang2023advancesinviral pages 9-10, woodson2025neuropathogenesisofencephalitic pages 14-15) |
| Mouse | BALB/c | VEEV, WEEV, EEEV | Intranasal, aerosol, subcutaneous | Commonly used for lethal alphavirus encephalitis; recapitulates CNS invasion, brain inflammation, neuronal injury, and survival outcomes; useful for antiviral testing such as brain-penetrant therapeutics (woodson2025neuropathogenesisofencephalitic pages 14-15, woodson2025neuropathogenesisofencephalitic pages 10-11) | Some exposure routes, especially aerosol/intranasal, may model laboratory or biothreat exposure better than natural mosquito transmission (woodson2025neuropathogenesisofencephalitic pages 23-25, woodson2025neuropathogenesisofencephalitic pages 10-11) |
| Mouse | CD-1 / outbred mice | VEEV, EEEV | Intranasal, aerosol, subcutaneous | Outbred background can capture variability in host response; develops fever, encephalitis, neuronal death, gliosis, meningitis, and other neuropathology (woodson2025neuropathogenesisofencephalitic pages 14-15, woodson2025neuropathogenesisofencephalitic pages 10-11) | Greater biological variability may complicate mechanistic interpretation; still limited by species differences from humans (woodson2025neuropathogenesisofencephalitic pages 14-15, yang2023advancesinviral pages 9-10) |
| Mouse | AG129 (type I/II IFN receptor-deficient) | ZIKV and other flavivirus studies | Often peripheral inoculation; route varies by study | Highly permissive model for flavivirus neuroinvasion because of impaired interferon responses; useful for pathogenesis and therapeutic testing when wild-type mice are resistant (yang2023advancesinviral pages 9-10) | Severe interferon deficiency creates nonphysiologic susceptibility and may overestimate neurovirulence relative to immunocompetent humans (yang2023advancesinviral pages 9-10) |
| Mouse | Transgenic hACE2 | SARS-CoV-2 | Typically intranasal | Enables study of coronavirus neuroinvasion and encephalitic/CNS manifestations in a receptor-humanized context (yang2023advancesinviral pages 9-10) | Model is pathogen-specific and receptor-driven; CNS disease may reflect transgene expression pattern rather than typical human biology (yang2023advancesinviral pages 9-10) |
| Mouse | Tg2576 (amyloidosis / Alzheimer-related transgenic line) | VEEV | Noted in infection studies; route varies | Shows more severe neurological deficits after VEEV infection, useful for probing interactions between neurodegenerative vulnerability and viral encephalitis (woodson2025neuropathogenesisofencephalitic pages 13-14, woodson2025neuropathogenesisofencephalitic pages 14-15) | Specialized comorbidity model, not representative of the general population; interpretation is limited to specific host-background questions (woodson2025neuropathogenesisofencephalitic pages 13-14) |
| Mouse | TMEV model (Theiler's murine encephalomyelitis virus) | TMEV | Experimental infection in mice | Best-characterized model for infection-associated seizures and acquired epilepsy after encephalitis; useful for studying ictogenesis, epileptogenesis, hippocampal injury, synaptic reorganization, and inflammatory mechanisms (loscher2022molecularmechanismsin pages 1-2, loscher2022molecularmechanismsin pages 18-19) | TMEV is not a human pathogen, so translational relevance is strongest for mechanisms rather than exact human disease replication (loscher2022molecularmechanismsin pages 1-2, loscher2022molecularmechanismsin pages 18-19) |
| Non-human primate | Cynomolgus macaques | VEEV, EEEV and other encephalitic alphaviruses | Aerosol, intranasal, subcutaneous | Closely resembles human disease; useful for fever, viremia, tremor, ataxia, photophobia, CNS pathology, and evaluation of vaccines/therapeutics under the Animal Rule (woodson2025neuropathogenesisofencephalitic pages 23-25, woodson2025neuropathogenesisofencephalitic pages 8-9, woodson2025neuropathogenesisofencephalitic pages 13-14, woodson2025neuropathogenesisofencephalitic pages 14-15) | Expensive, longer experiments, ethical constraints, and limited throughput; feeding/handling restrictions compared with rodents (yang2023advancesinviral pages 9-10) |
| Non-human primate | Common marmosets | EEEV | Intranasal | Develop lethal encephalitis with pathology comparable to human EEEV, including neuronal loss, neuronophagia, and leptomeningitis; valuable for severe disease modeling (woodson2025neuropathogenesisofencephalitic pages 8-9, woodson2025neuropathogenesisofencephalitic pages 10-11) | Less widely characterized than macaques; cost and ethical considerations remain substantial (woodson2025neuropathogenesisofencephalitic pages 8-9, woodson2025neuropathogenesisofencephalitic pages 10-11) |
| Small mammal | Chinese tree shrew | Viral encephalitis research platform (general) | Varies by virus/model | Proposed as a promising alternative model with favorable safety, efficacy, and predictability for investigating neural mechanisms of brain diseases, including viral encephalitis (yang2023advancesinviral pages 9-10) | Less standardized and less extensively validated than mouse and NHP models for specific encephalitic viruses (yang2023advancesinviral pages 9-10) |


*Table: This table summarizes the principal animal models used to study viral encephalitis, including standard mouse strains, specialized transgenic models, non-human primates, and alternative species. It highlights which viruses and exposure routes are modeled, what human disease features are reproduced, and the main translational limitations.*

Mouse models (including Theiler's virus for post-encephalitic epilepsy), non-human primates, and tree shrew are commonly employed. Each has distinct strengths for mechanism, pathogenesis, and preclinical therapeutic testing (loscher2022molecularmechanismsin pages 18-19, woodson2025neuropathogenesisofencephalitic pages 23-25, yang2023advancesinviral pages 9-10).

---
## Expert Opinion and Current Gaps

- **"Specific therapeutic approaches for effectively treating VE remain limited, highlighting the need for more intensive investigations into viral invasion routes, pathogenesis, and host immunity."** (yang2023advancesinviral pages 1-2)
- Early treatment, supportive care, and long-term rehabilitation remain cornerstones due to lack of broad-spectrum antivirals for most viral encephalitides.
- Precision medicine (genotype-guided testing/treatment) is emerging for HSV-related encephalitis.
- Best available current statistics are referenced in the tables and citations above.

---
## Citations
- Cleaver J et al. "The immunobiology of herpes simplex virus encephalitis..." Brain, 2024. [doi:10.1093/brain/awad419](https://doi.org/10.1093/brain/awad419)
- Yang D et al. "Advances in viral encephalitis..." Zoological Research, 2023. [doi:10.24272/j.issn.2095-8137.2023.025](https://doi.org/10.24272/j.issn.2095-8137.2023.025)
- Hills SL et al. "Tick-Borne Encephalitis Vaccine: Recommendations..." MMWR, 2023. [doi:10.15585/mmwr.rr7205a1](https://doi.org/10.15585/mmwr.rr7205a1)
- Woodson CM et al. "Neuropathogenesis of encephalitic alphaviruses..." Pathogens, 2025. [doi:10.3390/pathogens14020193](https://doi.org/10.3390/pathogens14020193)
- Zhang SY, Casanova JL. "Genetic defects of brain immunity in childhood herpes simplex encephalitis." Nature, 2024. [doi:10.1038/s41586-024-08119-z](https://doi.org/10.1038/s41586-024-08119-z)
- Skouboe MK et al. "Inborn errors of immunity predisposing to herpes simplex virus infections..." Pathogens, 2023. [doi:10.3390/pathogens12020310](https://doi.org/10.3390/pathogens12020310)
- Abbuehl LS et al. "Can we forecast poor outcome in herpes simplex and varicella zoster encephalitis?..." Front Neurol, 2023. [doi:10.3389/fneur.2023.1130090](https://doi.org/10.3389/fneur.2023.1130090)

---

## URLs for Primary Sources
- https://doi.org/10.1093/brain/awad419
- https://doi.org/10.24272/j.issn.2095-8137.2023.025
- https://doi.org/10.15585/mmwr.rr7205a1
- https://doi.org/10.3390/pathogens14020193
- https://doi.org/10.1038/s41586-024-08119-z
- https://doi.org/10.3390/pathogens12020310
- https://doi.org/10.3389/fneur.2023.1130090

All major claims are supported by high-quality reviews and recent primary research (2023-2024).

References

1. (cleaver2024theimmunobiologyof pages 2-2): Jonathan Cleaver, Katie Jeffery, Paul Klenerman, Ming Lim, Lahiru Handunnetthi, Sarosh R Irani, and Adam Handel. The immunobiology of herpes simplex virus encephalitis and post-viral autoimmunity. Brain, 147:1130-1148, Dec 2024. URL: https://doi.org/10.1093/brain/awad419, doi:10.1093/brain/awad419. This article has 57 citations and is from a highest quality peer-reviewed journal.

2. (yang2023advancesinviral pages 2-3): Dan Yang, Xiao-Jing Li, De-Zhen Tu, Xiu-Li Li, and Bin Wei. Advances in viral encephalitis: viral transmission, host immunity, and experimental animal models. Zoological Research, 44:525-542, May 2023. URL: https://doi.org/10.24272/j.issn.2095-8137.2023.025, doi:10.24272/j.issn.2095-8137.2023.025. This article has 28 citations.

3. (cleaver2024theimmunobiologyof pages 3-4): Jonathan Cleaver, Katie Jeffery, Paul Klenerman, Ming Lim, Lahiru Handunnetthi, Sarosh R Irani, and Adam Handel. The immunobiology of herpes simplex virus encephalitis and post-viral autoimmunity. Brain, 147:1130-1148, Dec 2024. URL: https://doi.org/10.1093/brain/awad419, doi:10.1093/brain/awad419. This article has 57 citations and is from a highest quality peer-reviewed journal.

4. (yang2023advancesinviral pages 1-2): Dan Yang, Xiao-Jing Li, De-Zhen Tu, Xiu-Li Li, and Bin Wei. Advances in viral encephalitis: viral transmission, host immunity, and experimental animal models. Zoological Research, 44:525-542, May 2023. URL: https://doi.org/10.24272/j.issn.2095-8137.2023.025, doi:10.24272/j.issn.2095-8137.2023.025. This article has 28 citations.

5. (hills2023tickborneencephalitisvaccine pages 5-6): Susan L. Hills, Katherine A. Poehling, Wilbur H. Chen, and J. Erin Staples. Tick-borne encephalitis vaccine: recommendations of the advisory committee on immunization practices, united states, 2023. MMWR Recommendations and Reports, 72:1-29, Nov 2023. URL: https://doi.org/10.15585/mmwr.rr7205a1, doi:10.15585/mmwr.rr7205a1. This article has 39 citations.

6. (woodson2025neuropathogenesisofencephalitic pages 6-8): Caitlin M. Woodson, Shannon K. Carney, and Kylene Kehn-Hall. Neuropathogenesis of encephalitic alphaviruses in non-human primate and mouse models of infection. Pathogens, 14:193, Feb 2025. URL: https://doi.org/10.3390/pathogens14020193, doi:10.3390/pathogens14020193. This article has 15 citations.

7. (woodson2025neuropathogenesisofencephalitic pages 3-4): Caitlin M. Woodson, Shannon K. Carney, and Kylene Kehn-Hall. Neuropathogenesis of encephalitic alphaviruses in non-human primate and mouse models of infection. Pathogens, 14:193, Feb 2025. URL: https://doi.org/10.3390/pathogens14020193, doi:10.3390/pathogens14020193. This article has 15 citations.

8. (woodson2025neuropathogenesisofencephalitic pages 1-3): Caitlin M. Woodson, Shannon K. Carney, and Kylene Kehn-Hall. Neuropathogenesis of encephalitic alphaviruses in non-human primate and mouse models of infection. Pathogens, 14:193, Feb 2025. URL: https://doi.org/10.3390/pathogens14020193, doi:10.3390/pathogens14020193. This article has 15 citations.

9. (loscher2022molecularmechanismsin pages 1-2): Wolfgang Löscher and Charles L. Howe. Molecular mechanisms in the genesis of seizures and epilepsy associated with viral infection. Frontiers in Molecular Neuroscience, May 2022. URL: https://doi.org/10.3389/fnmol.2022.870868, doi:10.3389/fnmol.2022.870868. This article has 53 citations.

10. (OpenTargets Search: viral encephalitis,encephalitis): Open Targets Query (viral encephalitis,encephalitis, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

11. (abbuehl2023canweforecast pages 12-13): Lena S. Abbuehl, Eveline Hofmann, Arsany Hakim, and Anelia Dietmann. Can we forecast poor outcome in herpes simplex and varicella zoster encephalitis? a narrative review. Frontiers in Neurology, Jun 2023. URL: https://doi.org/10.3389/fneur.2023.1130090, doi:10.3389/fneur.2023.1130090. This article has 29 citations and is from a peer-reviewed journal.

12. (abbuehl2023canweforecast pages 3-4): Lena S. Abbuehl, Eveline Hofmann, Arsany Hakim, and Anelia Dietmann. Can we forecast poor outcome in herpes simplex and varicella zoster encephalitis? a narrative review. Frontiers in Neurology, Jun 2023. URL: https://doi.org/10.3389/fneur.2023.1130090, doi:10.3389/fneur.2023.1130090. This article has 29 citations and is from a peer-reviewed journal.

13. (zhang2024geneticdefectsof pages 3-4): Shen-Ying Zhang and Jean-Laurent Casanova. Genetic defects of brain immunity in childhood herpes simplex encephalitis. Nature, 635:563-573, Nov 2024. URL: https://doi.org/10.1038/s41586-024-08119-z, doi:10.1038/s41586-024-08119-z. This article has 38 citations and is from a highest quality peer-reviewed journal.

14. (zhang2024geneticdefectsof pages 13-15): Shen-Ying Zhang and Jean-Laurent Casanova. Genetic defects of brain immunity in childhood herpes simplex encephalitis. Nature, 635:563-573, Nov 2024. URL: https://doi.org/10.1038/s41586-024-08119-z, doi:10.1038/s41586-024-08119-z. This article has 38 citations and is from a highest quality peer-reviewed journal.

15. (skouboe2023inbornerrorsof pages 6-8): Morten Kelder Skouboe, Marvin Werner, and Trine H. Mogensen. Inborn errors of immunity predisposing to herpes simplex virus infections of the central nervous system. Pathogens, 12:310, Feb 2023. URL: https://doi.org/10.3390/pathogens12020310, doi:10.3390/pathogens12020310. This article has 23 citations.

16. (zhang2024geneticdefectsof pages 4-6): Shen-Ying Zhang and Jean-Laurent Casanova. Genetic defects of brain immunity in childhood herpes simplex encephalitis. Nature, 635:563-573, Nov 2024. URL: https://doi.org/10.1038/s41586-024-08119-z, doi:10.1038/s41586-024-08119-z. This article has 38 citations and is from a highest quality peer-reviewed journal.

17. (skouboe2023inbornerrorsof pages 4-6): Morten Kelder Skouboe, Marvin Werner, and Trine H. Mogensen. Inborn errors of immunity predisposing to herpes simplex virus infections of the central nervous system. Pathogens, 12:310, Feb 2023. URL: https://doi.org/10.3390/pathogens12020310, doi:10.3390/pathogens12020310. This article has 23 citations.

18. (skouboe2023inbornerrorsof pages 1-2): Morten Kelder Skouboe, Marvin Werner, and Trine H. Mogensen. Inborn errors of immunity predisposing to herpes simplex virus infections of the central nervous system. Pathogens, 12:310, Feb 2023. URL: https://doi.org/10.3390/pathogens12020310, doi:10.3390/pathogens12020310. This article has 23 citations.

19. (skouboe2023inbornerrorsof pages 10-11): Morten Kelder Skouboe, Marvin Werner, and Trine H. Mogensen. Inborn errors of immunity predisposing to herpes simplex virus infections of the central nervous system. Pathogens, 12:310, Feb 2023. URL: https://doi.org/10.3390/pathogens12020310, doi:10.3390/pathogens12020310. This article has 23 citations.

20. (zhang2024geneticdefectsof pages 1-3): Shen-Ying Zhang and Jean-Laurent Casanova. Genetic defects of brain immunity in childhood herpes simplex encephalitis. Nature, 635:563-573, Nov 2024. URL: https://doi.org/10.1038/s41586-024-08119-z, doi:10.1038/s41586-024-08119-z. This article has 38 citations and is from a highest quality peer-reviewed journal.

21. (liu2023tcellsin pages 7-8): William J. Liu, Cong Jin, Ashley L. St, John Xi, Wang, E. T. Stone, and Amelia K. Pinto. T cells in tick-borne flavivirus encephalitis: a review of current paradigms in protection and disease pathology. Viruses, 15:958, Apr 2023. URL: https://doi.org/10.3390/v15040958, doi:10.3390/v15040958. This article has 20 citations.

22. (woodson2025neuropathogenesisofencephalitic pages 4-6): Caitlin M. Woodson, Shannon K. Carney, and Kylene Kehn-Hall. Neuropathogenesis of encephalitic alphaviruses in non-human primate and mouse models of infection. Pathogens, 14:193, Feb 2025. URL: https://doi.org/10.3390/pathogens14020193, doi:10.3390/pathogens14020193. This article has 15 citations.

23. (yang2023advancesinviral pages 3-4): Dan Yang, Xiao-Jing Li, De-Zhen Tu, Xiu-Li Li, and Bin Wei. Advances in viral encephalitis: viral transmission, host immunity, and experimental animal models. Zoological Research, 44:525-542, May 2023. URL: https://doi.org/10.24272/j.issn.2095-8137.2023.025, doi:10.24272/j.issn.2095-8137.2023.025. This article has 28 citations.

24. (woodson2025neuropathogenesisofencephalitic pages 28-29): Caitlin M. Woodson, Shannon K. Carney, and Kylene Kehn-Hall. Neuropathogenesis of encephalitic alphaviruses in non-human primate and mouse models of infection. Pathogens, 14:193, Feb 2025. URL: https://doi.org/10.3390/pathogens14020193, doi:10.3390/pathogens14020193. This article has 15 citations.

25. (abbuehl2023canweforecast pages 5-5): Lena S. Abbuehl, Eveline Hofmann, Arsany Hakim, and Anelia Dietmann. Can we forecast poor outcome in herpes simplex and varicella zoster encephalitis? a narrative review. Frontiers in Neurology, Jun 2023. URL: https://doi.org/10.3389/fneur.2023.1130090, doi:10.3389/fneur.2023.1130090. This article has 29 citations and is from a peer-reviewed journal.

26. (abbuehl2023canweforecast pages 5-6): Lena S. Abbuehl, Eveline Hofmann, Arsany Hakim, and Anelia Dietmann. Can we forecast poor outcome in herpes simplex and varicella zoster encephalitis? a narrative review. Frontiers in Neurology, Jun 2023. URL: https://doi.org/10.3389/fneur.2023.1130090, doi:10.3389/fneur.2023.1130090. This article has 29 citations and is from a peer-reviewed journal.

27. (abbuehl2023canweforecast pages 12-12): Lena S. Abbuehl, Eveline Hofmann, Arsany Hakim, and Anelia Dietmann. Can we forecast poor outcome in herpes simplex and varicella zoster encephalitis? a narrative review. Frontiers in Neurology, Jun 2023. URL: https://doi.org/10.3389/fneur.2023.1130090, doi:10.3389/fneur.2023.1130090. This article has 29 citations and is from a peer-reviewed journal.

28. (abbuehl2023canweforecast pages 7-7): Lena S. Abbuehl, Eveline Hofmann, Arsany Hakim, and Anelia Dietmann. Can we forecast poor outcome in herpes simplex and varicella zoster encephalitis? a narrative review. Frontiers in Neurology, Jun 2023. URL: https://doi.org/10.3389/fneur.2023.1130090, doi:10.3389/fneur.2023.1130090. This article has 29 citations and is from a peer-reviewed journal.

29. (yang2023advancesinviral pages 9-10): Dan Yang, Xiao-Jing Li, De-Zhen Tu, Xiu-Li Li, and Bin Wei. Advances in viral encephalitis: viral transmission, host immunity, and experimental animal models. Zoological Research, 44:525-542, May 2023. URL: https://doi.org/10.24272/j.issn.2095-8137.2023.025, doi:10.24272/j.issn.2095-8137.2023.025. This article has 28 citations.

30. (woodson2025neuropathogenesisofencephalitic pages 13-14): Caitlin M. Woodson, Shannon K. Carney, and Kylene Kehn-Hall. Neuropathogenesis of encephalitic alphaviruses in non-human primate and mouse models of infection. Pathogens, 14:193, Feb 2025. URL: https://doi.org/10.3390/pathogens14020193, doi:10.3390/pathogens14020193. This article has 15 citations.

31. (woodson2025neuropathogenesisofencephalitic pages 14-15): Caitlin M. Woodson, Shannon K. Carney, and Kylene Kehn-Hall. Neuropathogenesis of encephalitic alphaviruses in non-human primate and mouse models of infection. Pathogens, 14:193, Feb 2025. URL: https://doi.org/10.3390/pathogens14020193, doi:10.3390/pathogens14020193. This article has 15 citations.

32. (woodson2025neuropathogenesisofencephalitic pages 10-11): Caitlin M. Woodson, Shannon K. Carney, and Kylene Kehn-Hall. Neuropathogenesis of encephalitic alphaviruses in non-human primate and mouse models of infection. Pathogens, 14:193, Feb 2025. URL: https://doi.org/10.3390/pathogens14020193, doi:10.3390/pathogens14020193. This article has 15 citations.

33. (woodson2025neuropathogenesisofencephalitic pages 23-25): Caitlin M. Woodson, Shannon K. Carney, and Kylene Kehn-Hall. Neuropathogenesis of encephalitic alphaviruses in non-human primate and mouse models of infection. Pathogens, 14:193, Feb 2025. URL: https://doi.org/10.3390/pathogens14020193, doi:10.3390/pathogens14020193. This article has 15 citations.

34. (loscher2022molecularmechanismsin pages 18-19): Wolfgang Löscher and Charles L. Howe. Molecular mechanisms in the genesis of seizures and epilepsy associated with viral infection. Frontiers in Molecular Neuroscience, May 2022. URL: https://doi.org/10.3389/fnmol.2022.870868, doi:10.3389/fnmol.2022.870868. This article has 53 citations.

35. (woodson2025neuropathogenesisofencephalitic pages 8-9): Caitlin M. Woodson, Shannon K. Carney, and Kylene Kehn-Hall. Neuropathogenesis of encephalitic alphaviruses in non-human primate and mouse models of infection. Pathogens, 14:193, Feb 2025. URL: https://doi.org/10.3390/pathogens14020193, doi:10.3390/pathogens14020193. This article has 15 citations.

## Artifacts

- [Edison artifact artifact-00](Viral_Encephalitis-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Viral_Encephalitis-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Viral_Encephalitis-deep-research-falcon_artifacts/artifact-02.md)