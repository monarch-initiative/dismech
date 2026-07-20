---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T08:02:59.846440'
end_time: '2026-07-05T08:30:23.369532'
duration_seconds: 1643.52
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Alpha-gal Syndrome
  mondo_id: ''
  category: Complex
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
  path: Alpha-gal_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Alpha-gal_Syndrome-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Alpha-gal_Syndrome-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Alpha-gal Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Alpha-gal Syndrome** covering all of the
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
- **Disease Name:** Alpha-gal Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Alpha-gal Syndrome** covering all of the
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


# Comprehensive Research Report: Alpha-gal Syndrome (AGS)

---

## 1. Disease Information

### Overview

Alpha-gal syndrome (AGS) is an IgE-mediated allergic disorder characterized by delayed hypersensitivity reactions to the oligosaccharide galactose-alpha-1,3-galactose (alpha-gal), a carbohydrate found in non-primate mammalian tissues, meat products, dairy, gelatin, and mammalian-derived medications (wilson2024tickbitesige pages 1-3, macdougall2022themeatof pages 1-2). Unlike conventional food allergies targeting proteins, AGS is uniquely directed against a carbohydrate epitope and features a characteristic delay of 2–6 hours between allergen ingestion and symptom onset (wilson2024tickbitesige pages 1-3, vazrodrigues2022currentandfuture pages 1-2). The syndrome was first recognized when patients experienced severe anaphylaxis upon infusion of cetuximab, a monoclonal antibody produced in mouse-derived cell lines, and subsequent investigation linked the sensitization to tick bites (propst2025alphagalsyndromeand pages 1-2). AGS is now recognized as the tenth most common food allergy in the United States, with an estimated 450,000 cases nationally (choudhary2025singlecellmrnaanalysis pages 1-2).

### Key Identifiers

- **ICD-10:** The MeSH term "red meat allergy" (C000655084) is associated with AGS in clinical trial registrations (NCT06268717 chunk 2). A dedicated ICD-10 code was not widely available until recently; AGS lacked a dedicated diagnostic billing code, contributing to underdiagnosis (wilson2024tickbitesige pages 3-4).
- **OMIM:** No dedicated OMIM entry (AGS is an acquired, not a Mendelian, condition).
- **MONDO:** Not indexed.
- **Synonyms:** Red meat allergy, mammalian meat allergy, alpha-gal allergy, tick-induced meat allergy, galactose-alpha-1,3-galactose allergy.

### Data Source

Information is derived primarily from aggregated disease-level resources (clinical reviews, cohort studies, case series) and clinical trial registrations, with single-cell profiling data from individual patient samples.

---

## 2. Etiology

### Disease Causal Factors

AGS is an acquired immunological disorder. The primary causal factor is sensitization to alpha-gal through bites of hard-bodied (ixodid) ticks, particularly *Amblyomma americanum* (lone star tick) in the southeastern United States (wilson2024tickbitesige pages 1-3, macdougall2022themeatof pages 2-4). Tick saliva contains alpha-gal residues on glycoproteins and glycolipids and other biomolecules such as prostaglandin E2, which, upon injection into the host during blood feeding, initiate an IgE-mediated immune response to alpha-gal (vazrodrigues2022currentandfuture pages 1-2). Tick saliva interferes with dendritic cell maturation, suppressing pro-inflammatory Th1/Th17 responses while promoting Th2 pro-allergic responses, which drives the production of alpha-gal-specific IgE by B cells (macdougall2022themeatof pages 2-4).

The alpha-gal carbohydrate is synthesized by the enzyme alpha-1,3-galactosyltransferase (encoded by the *GGTA1* gene), which is functional in non-primate mammals but is a non-functional pseudogene in humans due to mutations accumulated over approximately 28 million years of evolution (cabezascruz2019environmentalandmolecular pages 1-2, wilson2024tickbitesige pages 3-4). This makes alpha-gal a foreign antigen highly immunogenic in humans (kepley2025tickedoffallergic pages 1-2).

### Risk Factors

**Genetic/Intrinsic Risk Factors:**
- **ABO blood type:** Persons with blood type B are approximately one-fourth as likely to have AGS compared to blood type O, as the B-antigen is structurally similar to alpha-gal (sharing terminal galactoses connected by alpha-1,3 bonds) and may confer cross-protective immune tolerance (taylor2024intrinsicriskfactors pages 6-8, wilson2024tickbitesige pages 3-4). Individuals with A and O blood types have higher AGS risk (macdougall2022themeatof pages 4-5).
- **Race/ethnicity:** White individuals showed higher seroconversion rates (6.6%) compared to Black (1.0%) and Hispanic (1.5%) populations in a military cohort, which may be partly attributable to differential distribution of protective B blood type alleles (taylor2024intrinsicriskfactors pages 6-8).
- **Atopy and childhood allergies:** AGS case patients were significantly more likely to report childhood allergies that resolved in adulthood, family history of AGS (OR 8.33), family history of food allergies (OR 2.70), and vitamin D deficiency (taylor2024intrinsicriskfactors pages 1-3, taylor2024intrinsicriskfactors pages 5-6).
- **Heightened insect bite reactivity:** Longer healing times for insect bites or stings (taylor2024intrinsicriskfactors pages 1-3).
- **Sex:** Male sex has been identified as a risk factor for both sensitization and clinical AGS, though in case-control analyses, sex did not always reach significance when accounting for occupational exposure (macdougall2022themeatof pages 4-5).

**Environmental Risk Factors:**
- **Tick exposure:** The predominant risk factor. 86% of diagnosed AGS patients report tick bite history (binder2023clinicalandlaboratory pages 1-1). Frequent tick exposure confers greater sensitization risk than single prolonged exposure (propst2025alphagalsyndromeand pages 1-2).
- **Outdoor occupation/activities:** Forestry workers, rural workers, military personnel in outdoor occupations, hunters, and gardeners have elevated sensitization rates (nalcacı2024mysteriousallergycaused pages 6-7). Infantry/law enforcement personnel showed 12.7% seroconversion vs. 1.2% for administrative personnel (Ching et al. 2024).
- **Rural residence:** Higher sensitization rates in rural versus urban areas (macdougall2022themeatof pages 4-5).
- **Cofactors:** Alcohol consumption and exercise can potentiate allergic responses and lower the threshold for reactions (binder2023clinicalandlaboratory pages 2-2, propst2025alphagalsyndromeand pages 2-3).

### Protective Factors

- **Blood type B:** Expression of the B-antigen is the best-studied non-tick protective factor. Structural similarity between alpha-gal and B-blood group antigen may provide cross-reactive immune tolerance (wilson2024tickbitesige pages 3-4).
- **IgG4 antibodies:** Higher levels of alpha-gal-specific IgG4 are associated with tolerance; AGS patients show reduced IgG4 compared to non-allergic alpha-gal-sensitized individuals (macdougall2022themeatof pages 2-4, carson2022where’sthebeef? pages 3-4).
- **Tick avoidance:** Long-term tick bite avoidance (1–2 years) may allow tolerance recovery and permit meat reintroduction (vazrodrigues2022currentandfuture pages 6-7).

### Gene–Environment Interactions

The interplay between the non-functional human *GGTA1* pseudogene (making alpha-gal foreign) and environmental tick bite exposure is the fundamental gene–environment interaction underlying AGS. Furthermore, intrinsic genetic factors influencing immune polarization (Th2 tendency, atopic constitution) interact with tick salivary components to determine whether an individual develops clinical AGS or remains asymptomatically sensitized (taylor2024intrinsicriskfactors pages 1-3, taylor2024intrinsicriskfactors pages 5-6).

---

## 3. Phenotypes

The clinical presentation of AGS is diverse and often delayed, making diagnosis challenging. The following table summarizes major phenotypic features:

| Phenotype/Symptom | HPO Term | Frequency | Onset Timing | Severity | Notes |
|---|---|---|---|---|---|
| Urticaria / hives | HP:0001025 | Very common (about 60–80%) | Typically 2–6 hours after ingestion of mammalian meat/products | Mild to severe | Most common cutaneous manifestation; often part of delayed multisystem reactions in AGS (binder2023clinicalandlaboratory pages 2-2, vazrodrigues2022currentandfuture pages 1-2, binder2023clinicalandlaboratory pages 1-1) |
| Anaphylaxis | HP:0011844 | Common (up to about 60%) | Usually delayed 2–6 hours after exposure | Severe / life-threatening | Can involve ≥2 organ systems; 75% of patients in one US cohort met anaphylaxis criteria (vazrodrigues2022currentandfuture pages 1-2, binder2023clinicalandlaboratory pages 2-2, binder2023clinicalandlaboratory pages 1-1) |
| Angioedema | HP:0100665 | Common | Typically 2–6 hours after ingestion | Moderate to severe | Frequently accompanies urticaria and may occur with broader systemic reactions (binder2023clinicalandlaboratory pages 2-2, vazrodrigues2022currentandfuture pages 1-2) |
| Gastrointestinal symptoms (abdominal pain, nausea, vomiting, diarrhea) | HP:0002027, HP:0002018, HP:0002013, HP:0002014 | Common (about 59–79%) | Typically 2–6 hours after ingestion | Mild to severe | Can present in isolation without skin findings; often overlaps with IBS-like symptoms and may be under-recognized (binder2023clinicalandlaboratory pages 2-2, propst2025alphagalsyndromeand pages 1-2, macdougall2022themeatof pages 10-11) |
| Pruritus | HP:0000989 | Very common | Typically 2–6 hours after ingestion | Mild to moderate | Common early allergic manifestation; often accompanies hives or angioedema (vazrodrigues2022currentandfuture pages 1-2, nalcacı2024mysteriousallergycaused pages 1-2) |
| Cardiovascular symptoms | HP:0001626 | Uncommon | Variable; may occur during systemic reactions or in association studies | Potentially severe | Reported associations include noncalcified plaque, obstructive coronary artery disease, and STEMI; evidence includes sensitization/cardiovascular links beyond classic food reactions (wilson2024tickbitesige pages 1-3, propst2025alphagalsyndromeand pages 7-8) |
| Hypotension / shock | HP:0002615 | Uncommon | During anaphylaxis | Severe | Represents severe systemic involvement and requires prompt epinephrine-based management (vazrodrigues2022currentandfuture pages 6-7, leder2024perioperativeconsiderationsin pages 3-5) |
| Respiratory distress | HP:0002098 | Less common | During anaphylaxis | Severe | Part of the anaphylactic cascade; more concerning in severe systemic AGS reactions (vazrodrigues2022currentandfuture pages 6-7, NCT06268717 chunk 2, NCT07611435 chunk 1) |


*Table: This table summarizes the major clinical phenotypes of Alpha-gal Syndrome, including suggested HPO terms, approximate frequencies, timing, severity, and clinically useful notes. It is useful for structuring phenotype annotations in a disease knowledge base.*

### Key Phenotypic Features

- **Delayed onset:** The hallmark of AGS is symptom onset 2–6 hours (sometimes up to 8 hours) after ingestion of mammalian meat, unlike conventional IgE-mediated food allergies that present within minutes (wilson2024tickbitesige pages 1-3, nalcacı2024mysteriousallergycaused pages 1-2).
- **Urticaria and anaphylaxis:** In a large US cohort, 75% of patients met anaphylaxis criteria involving ≥2 organ systems (binder2023clinicalandlaboratory pages 2-2, binder2023clinicalandlaboratory pages 1-1). Anaphylaxis occurs in up to 60% of AGS cases (vazrodrigues2022currentandfuture pages 1-2).
- **Gastrointestinal symptoms:** GI manifestations (abdominal pain, nausea, vomiting, diarrhea) are often predominant or isolated and can mimic irritable bowel syndrome, causing significant diagnostic delay (propst2025alphagalsyndromeand pages 1-2, macdougall2022themeatof pages 10-11). Dairy-reactive patients show higher GI symptom rates (79%) compared to dairy-tolerant patients (59%) (binder2023clinicalandlaboratory pages 2-2).
- **Quality of life:** A study of 28 patients found a mean diagnosis delay of 7.1 years, with over half experiencing anaphylaxis requiring emergency treatment and some requiring multiple hospitalizations. Food avoidance affects social eating and family interactions, and anxiety about potential anaphylaxis is common (macdougall2022themeatof pages 11-13).

### Suggested HPO Terms

- HP:0001025 (Urticaria), HP:0011844 (Anaphylaxis), HP:0100665 (Angioedema), HP:0000989 (Pruritus), HP:0002027 (Abdominal pain), HP:0002018 (Nausea), HP:0002013 (Vomiting), HP:0002014 (Diarrhea), HP:0002615 (Hypotension), HP:0002098 (Respiratory distress)

---

## 4. Genetic/Molecular Information

### Causal Gene: *GGTA1*

AGS is not a Mendelian genetic disease but rather an acquired immunological condition. However, the evolutionary loss of *GGTA1* function in humans is the molecular prerequisite. The *GGTA1* gene encodes alpha-1,3-galactosyltransferase (HGNC:4319), the enzyme responsible for synthesizing the alpha-gal epitope on glycoproteins and glycolipids. In humans and Old World primates, *GGTA1* is a pseudogene that produces only truncated transcripts lacking the two catalytic exons needed for enzyme activity (cabezascruz2019environmentalandmolecular pages 1-2). At least two separate mutations account for this loss of function, accumulated over ~28 million years (wilson2024tickbitesige pages 3-4). Non-primate mammals, New World monkeys, and platyrrhine primates retain a functional *GGTA1* gene (carson2022where’sthebeef? pages 1-3).

### Immunoglobulin Gene Rearrangements

Single-cell analysis has revealed that alpha-gal-specific IgE is secreted by a heterogeneous population of B cells, including CCR6-proficient memory B cells and CCR6-deficient plasmablasts/plasma cells. Individual B cells were found to express IgE-secreting transcripts alongside other immunoglobulin classes (IgA, IgG, IgM), suggesting a unique pattern of Ig gene arrangements and class switching (choudhary2025singlecellmrnaanalysis pages 1-2, choudhary2025singlecellmrnaanalysis pages 14-17).

### No Pathogenic Variants or Chromosomal Abnormalities

AGS does not involve pathogenic variants in the traditional clinical genetics sense. The disease is acquired through environmental exposure (tick bites), and susceptibility is modulated by ABO blood group genotype and atopic predisposition rather than by mutations in a single causative gene.

---

## 5. Environmental Information

### Environmental Factors

- **Tick bites** are the primary environmental trigger, with multiple tick species implicated globally (see Tick Species table below).
- **Medications and medical products** containing alpha-gal represent significant iatrogenic exposure risks, including heparin, gelatin-containing vaccines, cetuximab, surgifoam, lidocaine patches, and bioprosthetic heart valves (macdougall2022themeatof pages 10-11, leder2024perioperativeconsiderationsin pages 3-5, commins2020diagnosis&amp;management pages 16-18).

### Lifestyle Factors

- Alcohol consumption and exercise are known cofactors that potentiate allergic reactions (binder2023clinicalandlaboratory pages 2-2, propst2025alphagalsyndromeand pages 2-3).
- Outdoor recreation, hunting, fishing, and gardening increase tick exposure risk (taylor2024intrinsicriskfactors pages 6-8, taylor2024intrinsicriskfactors pages 5-6).

### Infectious Agents

Tick bites are the sensitizing event. The following table summarizes tick species associated with AGS worldwide:

| Tick Species | Geographic Region/Country | Reference |
|---|---|---|
| *Amblyomma americanum* | Southeastern United States; Coastal Atlantic states, USA | (wilson2024tickbitesige pages 3-4, sharma2024tickbiteinducedalphagal pages 1-2, platts‐mills2025theimmunologyof pages 6-8) |
| *Ixodes holocyclus* | Australia; especially eastern coastal Australia | (wilson2024tickbitesige pages 3-4, sharma2024tickbiteinducedalphagal pages 1-2, platts‐mills2025theimmunologyof pages 6-8) |
| *Ixodes ricinus* | Europe (including Sweden, Germany, broader established range) | (vazrodrigues2022currentandfuture pages 1-2, wilson2024tickbitesige pages 3-4, sharma2024tickbiteinducedalphagal pages 1-2, choudhary2025singlecellmrnaanalysis pages 1-2) |
| *Haemaphysalis longicornis* | Japan/Asia | (vazrodrigues2022currentandfuture pages 1-2, sharma2024tickbiteinducedalphagal pages 1-2, choudhary2025singlecellmrnaanalysis pages 1-2, platts‐mills2025theimmunologyof pages 6-8) |
| *Amblyomma sculptum* | Brazil | (sharma2024tickbiteinducedalphagal pages 1-2, choudhary2025singlecellmrnaanalysis pages 1-2) |
| *Rhipicephalus bursa* | Europe | (sharma2024tickbiteinducedalphagal pages 1-2) |
| *Hyalomma marginatum* | Europe | (sharma2024tickbiteinducedalphagal pages 1-2) |
| *Ixodes scapularis* | Eastern United States | (sharma2024tickbiteinducedalphagal pages 1-2, platts‐mills2025theimmunologyof pages 6-8) |
| *Amblyomma testudinarium* | Asia | (platts‐mills2025theimmunologyof pages 6-8) |
| *Ixodes pacificus* | Western United States | (platts‐mills2025theimmunologyof pages 6-8) |


*Table: This table summarizes tick species reported in the literature as implicated in alpha-gal sensitization or alpha-gal syndrome across major world regions. It is useful for mapping geographic risk and understanding regional differences in AGS epidemiology.*

---

## 6. Mechanism / Pathophysiology

### Sensitization Phase (Tick Bite → IgE Production)

The causal chain begins with tick attachment and blood feeding. Tick saliva contains alpha-gal on glycoproteins and glycolipids, along with immunomodulatory molecules including prostaglandin E2 (vazrodrigues2022currentandfuture pages 1-2). Tick saliva interferes with dendritic cell maturation, suppressing Th1/Th17 responses while favoring Th2 pro-allergic polarization (macdougall2022themeatof pages 2-4). Antigen-presenting cells (dendritic cells, macrophages, B cells) present alpha-gal to Th2 cells, which produce IL-4 and IL-13, driving B cell class switching to IgE (vazrodrigues2022currentandfuture pages 1-2). Repeated tick bites strengthen the Th2 signal (platts‐mills2025theimmunologyof pages 11-13). Notably, all humans produce natural IgG, IgM, and IgA antibodies to alpha-gal from gastrointestinal bacterial exposure, but IgE production is the pathological consequence of tick-mediated sensitization (wilson2024tickbitesige pages 1-3, carson2022where’sthebeef? pages 3-4).

### Effector Phase (Meat Ingestion → Delayed Allergic Reaction)

Upon consumption of mammalian meat, alpha-gal glycolipids cross the intestinal epithelial barrier and are incorporated into chylomicrons in lacteals, entering systemic circulation approximately one hour post-ingestion (platts‐mills2025theimmunologyof pages 11-13). Over 2–6 hours, chylomicrons (300–1000 nm) are progressively metabolized to VLDL and LDL particles (12–25 nm), which carry alpha-gal on their surface glycosylation (platts‐mills2025theimmunologyof pages 11-13). These smaller LDL particles can extravasate through endothelial walls into tissue compartments where they encounter mast cells bearing alpha-gal-specific IgE on FcεRI receptors. Alpha-gal on LDL cross-links surface-bound IgE, triggering mast cell and basophil degranulation and release of histamine, leukotrienes, and tryptase (platts‐mills2025theimmunologyof pages 11-13, branicka2025alphagalsyndrome—aseries pages 4-6). Basophil activation peaks approximately 4 hours after meat consumption, correlating with clinical symptom appearance (macdougall2022themeatof pages 2-4, carson2022where’sthebeef? pages 9-11). AGS patients also show significant differences in lipid metabolism, with delayed lipid processing contributing to the prolonged interval between ingestion and reaction (carson2022where’sthebeef? pages 8-9, kepley2025tickedoffallergic pages 7-8).

### Molecular Pathways

- **Th2 immune signaling:** IL-4, IL-13 → IgE class switching (GO:0045191)
- **FcεRI signaling:** IgE cross-linking → mast cell/basophil degranulation (GO:0038095)
- **Lipid metabolism and chylomicron processing:** GO:0034370 (triglyceride-rich lipoprotein particle remodeling)
- **Antigen presentation:** Enhanced MHC-II expression (GO:0019882)

### Cell Types Involved

- Mast cells (CL:0000097) — primary effector cells in tissue
- Basophils (CL:0000767) — primary effector cells in circulation
- Th2 CD4+ T cells (CL:0000546) — orchestrate IgE class switching
- iNKT cells (CL:0000911) — elevated in AGS; 2.5-fold higher activated CD69+ iNKT frequency (carson2022where’sthebeef? pages 6-8)
- NKB cells — hybrid phenotype expressing NK cytolytic molecules and B cell markers (choudhary2025singlecellmrnaanalysis pages 17-18)
- Mast cell progenitors — circulating population unique to AGS patients (choudhary2025singlecellmrnaanalysis pages 1-2, choudhary2025singlecellmrnaanalysis pages 17-18)
- B cells/plasmablasts — heterogeneous IgE-producing population including CCR6+ memory B cells (choudhary2025singlecellmrnaanalysis pages 1-2)
- Dendritic cells (CL:0000451) — antigen presentation, modulated by tick saliva

### Cardiovascular Associations

Alpha-gal sensitization has been associated with noncalcified plaque, obstructive coronary artery disease, and ST-segment-elevated myocardial infarction (propst2025alphagalsyndromeand pages 7-8). Chronic IgE-mediated inflammation from bioprosthetic valve implantation (containing alpha-gal) may contribute to early valve degradation and accelerated coronary artery disease (kuravi2022allergicresponseto pages 1-2, kuravi2022allergicresponseto pages 6-9).

### Molecular Profiling

**Single-cell analysis (Choudhary & Commins, 2025):** Multimodal single-cell RNA transcriptome and surface protein analysis of PBMCs from 18 AGS and 10 control subjects captured 437,770 total cells and identified 43 distinct immune cell clusters (choudhary2025singlecellmrnaanalysis pages 4-5). Key findings include:
- Circulating mast cell progenitors (cluster C43) with 53-fold elevated TPSAB1/tryptase and 8-fold elevated KIT expression (choudhary2025singlecellmrnaanalysis pages 8-11)
- CD4+-NKT cells predominantly from AGS subjects (96% in cluster C32) linked to Th2 responses (choudhary2025singlecellmrnaanalysis pages 17-18)
- 1,141 IgE-secreting cells containing 11,017 IgE transcripts identified (choudhary2025singlecellmrnaanalysis pages 14-17)
- Elevated S100A9, IFITM3, and THBS1 across multiple cell types in AGS subjects (choudhary2025singlecellmrnaanalysis pages 17-18)
- Enhanced antigen presentation genes: CD52, CXCL16, HLA-DPA1, HLA-DRA, ICAM1, IFITM3, LAP3, THBS1 (choudhary2025singlecellmrnaanalysis pages 8-11)

---

## 7. Anatomical Structures Affected

### Organ Level

- **Primary:** Skin (urticaria, angioedema), gastrointestinal tract (abdominal pain, nausea, vomiting, diarrhea), cardiovascular system (anaphylaxis-associated hypotension)
- **Secondary:** Cardiovascular system (noncalcified plaque, coronary artery disease), respiratory system (during anaphylaxis)
- **Body systems:** Immune system, integumentary system, digestive system, cardiovascular system, respiratory system

### Tissue and Cell Level

- Skin — dermal mast cells (CL:0000097)
- Gastrointestinal mucosa — mucosal mast cells, eosinophils (CL:0000771)
- Vascular endothelium — sites of LDL extravasation and mast cell activation
- Bone marrow — mast cell progenitors

### Subcellular Level

- Endosomes/lysosomes (GO:0005764) — alpha-gal glycoprotein processing
- Cell surface (GO:0009986) — FcεRI receptor complexes
- Secretory granules (GO:0030141) — mast cell/basophil degranulation

### UBERON Terms

- UBERON:0002097 (skin of body), UBERON:0001555 (digestive tract), UBERON:0000948 (heart), UBERON:0002107 (liver)

---

## 8. Temporal Development

### Onset

- **Age of onset:** Typically adult-onset; median age at onset is 53 years in a US cohort (binder2023clinicalandlaboratory pages 1-1). The condition can develop at any age following tick sensitization (propst2025alphagalsyndromeand pages 1-2).
- **Onset pattern:** Subacute to chronic; sensitization develops following repeated tick bites, often over months to years. Mean diagnostic delay is 7.1 years from symptom onset (macdougall2022themeatof pages 11-13).

### Progression

- **Disease course:** Episodic, with reactions triggered by exposure to alpha-gal-containing foods or products.
- **Duration:** Chronic but potentially reversible. Alpha-gal sIgE generally decreases over time with tick avoidance, though complete resolution was observed in only 1 of 13 patients in longitudinal follow-up (binder2023clinicalandlaboratory pages 8-8). Long-term tick avoidance (1–2 years) may allow tolerance recovery (vazrodrigues2022currentandfuture pages 6-7).
- **Severity modulation:** Fattier meals lead to more consistent reactions; exercise, alcohol, and repeated tick bites can increase severity (propst2025alphagalsyndromeand pages 2-3).

---

## 9. Inheritance and Population

### Epidemiology

- **Estimated prevalence (USA):** Approximately 450,000 cases nationally; approximately 2–5 cases per 100,000 persons reported, though county-level estimates suggest much higher prevalence (wilson2024tickbitesige pages 3-4, choudhary2025singlecellmrnaanalysis pages 1-2).
- **Sensitization rates:** 22% of North Carolina endoscopy patients; 20.8% of a Tennessee asymptomatic cohort; 35% among German forest workers/hunters (though only 8.6% of the German cohort reported clinical symptoms) (binder2023clinicalandlaboratory pages 2-2, binder2023clinicalandlaboratory pages 2-3).
- **Seroconversion incidence (military):** 4.9% seroconversion rate over a mean 3.4-year interval among 2,821 initially seronegative military personnel (Ching et al. 2024).
- **Global distribution:** Cases documented on every continent except Antarctica, with highest prevalence in the southeastern United States, Sweden, Australia, South Africa, and Germany (macdougall2022themeatof pages 4-5, wilson2024tickbitesige pages 3-4).
- **Search volume trends:** Google search volume for alpha-gal increased by an estimated 627% from 2015 to 2022, with an average annual percent change of 33.78% (Romeiser et al. 2024).

### Inheritance Pattern

AGS is not inherited in a Mendelian fashion. It is an acquired immunological condition. However, familial clustering has been observed—AGS patients are 8.33 times more likely to report relatives with AGS (taylor2024intrinsicriskfactors pages 5-6)—which may reflect shared genetic predisposition (atopy, blood type), shared environmental exposures (tick habitat), and increased diagnostic awareness within families.

### Population Demographics

- **Sex ratio:** 56% female in one cohort (binder2023clinicalandlaboratory pages 1-1); higher seroconversion in males (5.5% vs 1.9%) likely due to occupational exposure differences (Ching et al. 2024).
- **Race:** 95% White in a US cohort (binder2023clinicalandlaboratory pages 1-1). White individuals showed significantly higher seroconversion (6.6%) than Black (1.0%) or Hispanic (1.5%) individuals, partly attributable to differential B blood type frequency (taylor2024intrinsicriskfactors pages 6-8).
- **Geographic:** Southeastern and Coastal Atlantic US states are the epicenter in the USA, corresponding to *A. americanum* distribution (wilson2024tickbitesige pages 3-4).

---

## 10. Diagnostics

### Clinical Tests

- **Alpha-gal-specific IgE (sIgE):** The primary diagnostic biomarker. Titers ≥0.1 IU/mL (or kU/L) are considered positive, though elevated sIgE alone does not confirm clinical AGS—clinical history is essential (binder2023clinicalandlaboratory pages 2-3, macdougall2022themeatof pages 1-2).
- **Skin prick test (SPT):** Wheal and flare responses to alpha-gal-containing extracts (macdougall2022themeatof pages 4-5).
- **Basophil activation test (BAT):** Measures CD63 activation on peripheral blood basophils stimulated with mammalian-based extracts; peak activation at ~4 hours post-meat ingestion (vazrodrigues2022currentandfuture pages 1-2, macdougall2022themeatof pages 2-4).
- **Oral food challenge (OFC):** The gold standard but carries anaphylaxis risk; double-blind, placebo-controlled food challenges are used in research settings, including novel challenges using alpha-gal knockout pork (NCT06268717 chunk 1, NCT07611435 chunk 1).
- **Serum tryptase:** Marker for mast cell degranulation, elevated in only 30% of AGS patients (macdougall2022themeatof pages 4-5).
- **Total IgE:** Often elevated in AGS patients.

### Emerging Diagnostic Tools

- Mast cell activation test (MAT), histamine-release (HR) assay, omics technologies, and model-based reasoning (MBR) are under investigation (vazrodrigues2022currentandfuture pages 1-2).

### Clinical Criteria

Diagnosis is based on: (1) compatible clinical history of delayed allergic reactions to mammalian meat/products, (2) elevated alpha-gal-specific IgE, and (3) exclusion of alternative diagnoses. No universally standardized diagnostic criteria exist (binder2023clinicalandlaboratory pages 2-3).

### Differential Diagnosis

- Irritable bowel syndrome (for GI-predominant AGS)
- Chronic spontaneous urticaria
- Idiopathic anaphylaxis
- Systemic mastocytosis
- Non-celiac gluten sensitivity
- Lactose intolerance
- Other food allergies

---

## 11. Outcome / Prognosis

### Mortality and Morbidity

AGS can be life-threatening when anaphylaxis occurs, but mortality data are limited. The primary morbidity includes recurrent allergic reactions, dietary restriction, quality of life impairment, and diagnostic delay (macdougall2022themeatof pages 11-13). AGS is a leading cause of anaphylaxis in southeastern US adults and adolescents (macdougall2022themeatof pages 4-5).

### Disease Course

- **Natural history:** With strict tick avoidance, alpha-gal sIgE generally decreases over time, though complete resolution occurs infrequently (binder2023clinicalandlaboratory pages 8-8). Long-term avoidance of tick bites (1–2 years) may allow tolerance recovery and gradual meat reintroduction (vazrodrigues2022currentandfuture pages 6-7).
- **Dietary response:** Approximately 80% of patients achieve symptom resolution with mammalian meat elimination alone, and an additional 15% require dairy removal (macdougall2022themeatof pages 7-8).
- **Prognostic factors:** Higher alpha-gal sIgE titers correlate with greater severity; patients who tolerate dairy generally have better prognosis for remission (macdougall2022themeatof pages 8-10).

---

## 12. Treatment

### Pharmacotherapy

- **Avoidance diet** (MAXO:0000004 — dietary modification): The cornerstone of treatment. Patients must avoid mammalian meat (beef, pork, lamb), dairy products (for some), gelatin, and other alpha-gal-containing products. Safe alternatives include poultry, fish, and plant-based proteins (propst2025alphagalsyndromeand pages 4-5, macdougall2022themeatof pages 7-8).
- **Epinephrine** (MAXO:0000587): Intramuscular epinephrine auto-injectors for emergency anaphylaxis management. Intravenous epinephrine with fluid resuscitation for shock patients (vazrodrigues2022currentandfuture pages 6-7).
- **Antihistamines:** Oral antihistamines (hydroxyzine, cetirizine, desloratadine, diphenhydramine, fexofenadine) for urticaria and angioedema (vazrodrigues2022currentandfuture pages 7-8, propst2025alphagalsyndromeand pages 4-5).
- **Corticosteroids:** Prednisone, methylprednisolone for more severe allergic reactions (vazrodrigues2022currentandfuture pages 7-8).
- **Cromolyn sodium:** Oral mast cell stabilizer for gastrointestinal symptoms (macdougall2022themeatof pages 7-8, vazrodrigues2022currentandfuture pages 7-8).
- **Omalizumab** (anti-IgE monoclonal antibody): Binds free serum IgE, reduces availability to mast cells/basophils, increases reaction threshold; some patients on omalizumab were able to reintroduce restricted foods (macdougall2022themeatof pages 7-8, vazrodrigues2022currentandfuture pages 7-8). Notably, omalizumab is produced in CHO cell lines and contains no detectable alpha-gal (macdougall2022themeatof pages 10-11).
- **Metformin:** Some patients on metformin were able to reintroduce restricted foods, though the mechanism is unclear (macdougall2022themeatof pages 7-8).

### Advanced/Experimental Therapeutics

- **Oral immunotherapy (OIT):** Case reports show successful beef desensitization in adults (27-day protocol) and children (24-day protocol), achieving tolerance of 100–120 g beef daily. Sustained daily consumption is required to maintain desensitization. A pilot study demonstrated cow's milk containing 6 mg alpha-gal daily was safely tolerated over 3 years (macdougall2022themeatof pages 8-10). No FDA-approved OIT exists for AGS.
- **Nanoparticle immunotherapy:** Nanoparticles encapsulating alpha-gal glycoprotein reduced Th2 cytokine production and IgE formation in prophylactic mouse models, though therapeutic administration showed only partial efficacy (propst2025alphagalsyndromeand pages 4-5).
- **Mast cell-directed therapy:** A Phase 2 trial (NCT07526558) is testing ketotifen + cromolyn + fexofenadine vs. fexofenadine alone for post-tick bite illness including AGS (NCT07526558 chunk 1).
- **Alpha-gal knockout pork:** Clinical trials are evaluating pork from GGTA1-knockout pigs as a safe food alternative and diagnostic control (NCT06268717, NCT07611435) (NCT06268717 chunk 1, NCT07611435 chunk 1).

### Perioperative Management

Patients with AGS require careful perioperative medication review. Many common anesthetic and surgical products contain mammalian-derived alpha-gal, including heparin, gelatin-based hemostatic agents (surgifoam), gelatin capsules, propofol (glycerol content), and bioprosthetic heart valves (leder2024perioperativeconsiderationsin pages 3-5, leder2024perioperativeconsiderationsin pages 2-3, leder2024perioperativeconsiderationsin pages 1-2). Preoperative steroids and antihistamines are recommended before high-dose heparin exposure, and alternative anticoagulants (sodium citrate) should be considered (commins2020diagnosis&amp;management pages 16-18, leder2024perioperativeconsiderationsin pages 2-3). 24–50% of AGS patients undergoing cardiac surgery with cardiopulmonary bypass experienced severe allergic reactions (leder2024perioperativeconsiderationsin pages 2-3). Intravenous formulations are generally safer than oral formulations due to fewer mammalian-derived fillers (leder2024perioperativeconsiderationsin pages 7-9).

### Clinical Trials

The following table summarizes active and completed clinical trials for AGS:

| NCT ID | Title | Phase | Status | Sponsor | Enrollment | Key Design Features |
|---|---|---|---|---|---:|---|
| NCT06268717 | GI Alpha-Gal Study | NA | Completed | University of North Carolina, Chapel Hill | 30 | Double-blind randomized crossover food challenge comparing pork with alpha-gal vs pork without alpha-gal; includes lactulose/C13 mannitol testing, transnasal upper endoscopy with GI biopsies, basophil activation, tryptase, and mRNA/pathology studies (NCT06268717 chunk 1, NCT06268717 chunk 2) |
| NCT04828317 | Alpha-gal Pork Challenge | NA | Unknown | University of Virginia | 54 | Pork challenge study in alpha-gal syndrome; interventional design evaluating clinical responses to pork exposure (clinical trial search result in prior tool output) |
| NCT07611435 | Beginning to Assess an Appropriate CONtrol for Oral Food Challenges in Alpha-Gal Syndrome (CoFAR-13) - BeACON4AG | Phase 2 | Not yet recruiting | National Institute of Allergy and Infectious Diseases (NIAID) | 160 | Multisite randomized double-blind crossover diagnostic trial; participants receive alpha-gal knockout pork and wild-type pork on separate visits to compare odds of positive double-blind food challenges and define AGS sub-phenotypes (NCT07611435 chunk 1, NCT07611435 chunk 2) |
| NCT07177729 | The α-gal Syndrome - Investigating Immune Reactions to Tick Bites (ImmunoGal) | Observational | Recruiting | Luxembourg Institute of Health | 100 | Prospective cohort enrolling participants within 48 hours of tick removal; longitudinal blood sampling, tick collection/PCR, serology, and multi-omics immune profiling to identify signatures associated with alpha-gal sensitization after tick bites (NCT07177729 chunk 1) |
| NCT07526558 | Mast Cell Treatment in Post-tick Bite Illness (PTBI) | Phase 2 | Not yet recruiting | University of North Carolina, Chapel Hill | 50 | Randomized double-blind parallel pilot trial testing ketotifen + cromolyn + fexofenadine versus fexofenadine alone for persistent mast cell activation symptoms after post-tick bite illness, including AGS (NCT07526558 chunk 1) |


*Table: This table summarizes the main clinical trials identified for alpha-gal syndrome and related post-tick bite illness. It is useful for quickly comparing study design, status, enrollment, and the main research focus of each trial.*

---

## 13. Prevention

### Primary Prevention

- **Tick bite avoidance:** The most critical prevention strategy. Recommended measures include protective clothing treated with permethrin, prompt tick removal with specialized forceps, and use of tick repellents (vazrodrigues2022currentandfuture pages 6-7).
- **Public awareness:** Provider knowledge of AGS remains limited; inclusion of AGS content in medical school curricula is recommended (Thompson et al. 2025).

### Secondary Prevention

- **Early diagnosis:** Clinicians should suspect AGS in patients with adult-onset atopy, idiopathic anaphylaxis, insect bite hypersensitivity, or delayed reactions to red meat (taylor2024intrinsicriskfactors pages 1-3).
- **Alpha-gal sIgE testing:** Should be performed in at-risk individuals with compatible symptoms.
- **Dietary counseling:** Dietician consultation recommended for identifying hidden alpha-gal ingredients in processed foods, supplements, and medications (propst2025alphagalsyndromeand pages 4-5).

### Tertiary Prevention

- **Continued tick avoidance:** Essential to prevent disease severity escalation and allow potential IgE decline (propst2025alphagalsyndromeand pages 4-5, binder2023clinicalandlaboratory pages 8-8).
- **Medication review:** Comprehensive review of all medications for mammalian-derived ingredients (leder2024perioperativeconsiderationsin pages 1-2).
- **Emergency preparedness:** Epinephrine auto-injector prescription and patient education on anaphylaxis management.

---

## 14. Other Species / Natural Disease

### Tick Species and Cross-Species Biology

Alpha-gal is widely expressed in non-primate mammals (including cows, pigs, sheep, deer), bacteria, and parasites including ticks (wilson2024tickbitesige pages 1-3). The alpha-gal epitope is synthesized by functional alpha-1,3-galactosyltransferase in these organisms. Tick galactosyltransferases are involved in synthesizing alpha-gal in tick tissues and saliva (cabezascruz2019environmentalandmolecular pages 1-2). N-glycome profiling and proteome analysis have demonstrated alpha-gal antigens in salivary gland extracts and saliva of *A. americanum* and *Ixodes scapularis*, but not in *Amblyomma maculatum* (sharma2024tickbiteinducedalphagal pages 1-2).

### Zoonotic/Vector-Borne Considerations

AGS is fundamentally a vector-borne allergic disease. The sensitization pathway is unique in that it involves an arthropod vector (tick) but is not an infectious disease. The clinical syndrome is dependent on subsequent exposure to mammalian-derived products, making it a complex interface of ectoparasite biology and human immunology.

---

## 15. Model Organisms

### AGKO Mouse Model

The primary animal model is the alpha-gal knockout (AGKO) mouse, which has a targeted disruption of alpha-1,3-galactosyltransferase and therefore cannot produce alpha-gal, mimicking the human condition (sharma2024tickbiteinducedalphagal pages 1-2). In this model:
- *A. americanum* nymph infestation induced significant increases in total IgE, IgG1, and alpha-gal IgG1 antibody titers compared to *A. maculatum*-sensitized mice (sharma2024tickbiteinducedalphagal pages 1-2).
- Pork challenge in *A. americanum*-sensitized AGKO mice led to body temperature decline (anaphylaxis-like response) (sharma2024tickbiteinducedalphagal pages 1-2).
- Gene expression analysis revealed *A. americanum* bites direct mouse immunity toward Th2 polarization (sharma2024tickbiteinducedalphagal pages 1-2).

### In Vitro Models

- Humanized cell lines and primary cultures using human sera and novel human alpha-gal-specific IgE monoclonal antibodies are used to study allergic effector cell activation (kepley2025tickedoffallergic pages 1-2).
- Nanoparticle immunotherapy has been tested in mouse models showing reduction in Th2 cytokines and alpha-gal-specific IgE with prophylactic treatment (choudhary2025singlecellmrnaanalysis pages 1-2).

### Model Limitations

- AGKO mice do not fully recapitulate all features of human AGS, particularly the delayed reaction kinetics and the complexity of human lipid metabolism.
- Species-specific differences in tick-host interactions may limit translational applicability.

---

## Summary of Key Ontology Terms

- **MONDO:** Not indexed for AGS
- **HPO:** HP:0001025 (Urticaria), HP:0011844 (Anaphylaxis), HP:0100665 (Angioedema), HP:0000989 (Pruritus), HP:0002027 (Abdominal pain), HP:0002018 (Nausea/vomiting), HP:0002014 (Diarrhea)
- **GO Biological Process:** GO:0045191 (regulation of isotype switching to IgE), GO:0038095 (Fc-epsilon receptor signaling), GO:0034370 (triglyceride-rich lipoprotein particle remodeling), GO:0019882 (antigen processing and presentation)
- **CL (Cell Ontology):** CL:0000097 (mast cell), CL:0000767 (basophil), CL:0000546 (T-helper 2 cell), CL:0000911 (iNKT cell), CL:0000451 (dendritic cell)
- **UBERON:** UBERON:0002097 (skin), UBERON:0001555 (digestive tract), UBERON:0000948 (heart)
- **CHEBI:** CHEBI:59517 (galactose-alpha-1,3-galactose), CHEBI:16042 (histamine), CHEBI:17855 (tryptase)
- **MAXO:** MAXO:0000004 (dietary modification), MAXO:0000587 (epinephrine administration), MAXO:0001001 (allergen avoidance)
- **Gene:** GGTA1 (HGNC:4319) — pseudogene in humans; functional in non-primate mammals

---

## Key References

This report draws from 17 primary research publications and 4 clinical trial registrations, including comprehensive reviews in *Allergy* (Wilson et al. 2024), *Journal of Immunology* (Carson et al. 2022), *ImmunoTargets and Therapy* (Macdougall et al. 2022), *Immunological Reviews* (Platts-Mills et al. 2025), *Frontiers in Immunology* (Sharma et al. 2024; Choudhary & Commins 2025), and clinical data from the CDC-affiliated cohort study published in *Allergy* (Binder et al. 2023) and the case-control study in *Annals of Allergy, Asthma & Immunology* (Taylor et al. 2024).

References

1. (wilson2024tickbitesige pages 1-3): Jeffrey M. Wilson, Loren Erickson, Michael Levin, Samuel M. Ailsworth, Scott P. Commins, and Thomas A. E. Platts‐Mills. Tick bites, ige to galactose-alpha-1,3-galactose and urticarial or anaphylactic reactions to mammalian meat: the alpha-gal syndrome. Allergy, 79:1440-1454, Jan 2024. URL: https://doi.org/10.1111/all.16003, doi:10.1111/all.16003. This article has 72 citations and is from a highest quality peer-reviewed journal.

2. (macdougall2022themeatof pages 1-2): Jessica D Macdougall, Kevin O Thomas, and Onyinye I Iweala. The meat of the matter: understanding and managing alpha-gal syndrome. ImmunoTargets and Therapy, 11:37-54, Sep 2022. URL: https://doi.org/10.2147/itt.s276872, doi:10.2147/itt.s276872. This article has 71 citations.

3. (vazrodrigues2022currentandfuture pages 1-2): Rita Vaz-Rodrigues, Lorena Mazuecos, and José de la Fuente. Current and future strategies for the diagnosis and treatment of the alpha-gal syndrome (ags). Journal of Asthma and Allergy, 15:957-970, Jul 2022. URL: https://doi.org/10.2147/jaa.s265660, doi:10.2147/jaa.s265660. This article has 70 citations and is from a peer-reviewed journal.

4. (propst2025alphagalsyndromeand pages 1-2): Susan B. H. Propst and Dorothea K. Thompson. Alpha-gal syndrome and the gastrointestinal reaction: a narrative review. Frontiers in Allergy, Jan 2025. URL: https://doi.org/10.3389/falgy.2025.1535103, doi:10.3389/falgy.2025.1535103. This article has 13 citations and is from a peer-reviewed journal.

5. (choudhary2025singlecellmrnaanalysis pages 1-2): Shailesh K. Choudhary and Scott P. Commins. Single-cell mrna analysis and surface marker expression profiling of circulating immune cells in humans with alpha-gal syndrome. Frontiers in Immunology, Sep 2025. URL: https://doi.org/10.3389/fimmu.2025.1629310, doi:10.3389/fimmu.2025.1629310. This article has 2 citations and is from a peer-reviewed journal.

6. (NCT06268717 chunk 2):  GI Alpha-Gal Study. University of North Carolina, Chapel Hill. 2023. ClinicalTrials.gov Identifier: NCT06268717

7. (wilson2024tickbitesige pages 3-4): Jeffrey M. Wilson, Loren Erickson, Michael Levin, Samuel M. Ailsworth, Scott P. Commins, and Thomas A. E. Platts‐Mills. Tick bites, ige to galactose-alpha-1,3-galactose and urticarial or anaphylactic reactions to mammalian meat: the alpha-gal syndrome. Allergy, 79:1440-1454, Jan 2024. URL: https://doi.org/10.1111/all.16003, doi:10.1111/all.16003. This article has 72 citations and is from a highest quality peer-reviewed journal.

8. (macdougall2022themeatof pages 2-4): Jessica D Macdougall, Kevin O Thomas, and Onyinye I Iweala. The meat of the matter: understanding and managing alpha-gal syndrome. ImmunoTargets and Therapy, 11:37-54, Sep 2022. URL: https://doi.org/10.2147/itt.s276872, doi:10.2147/itt.s276872. This article has 71 citations.

9. (cabezascruz2019environmentalandmolecular pages 1-2): Alejandro Cabezas-Cruz, Adnan Hodžić, Patricia Román-Carrasco, Lourdes Mateos-Hernández, Georg Gerhard Duscher, Deepak Kumar Sinha, Wolfgang Hemmer, Ines Swoboda, Agustín Estrada-Peña, and José de la Fuente. Environmental and molecular drivers of the α-gal syndrome. Frontiers in Immunology, May 2019. URL: https://doi.org/10.3389/fimmu.2019.01210, doi:10.3389/fimmu.2019.01210. This article has 84 citations and is from a peer-reviewed journal.

10. (kepley2025tickedoffallergic pages 1-2): Christopher L. Kepley, Yinghui Wang, Amy Yelton, Eva R. Siebert, and Onyinye I. Iweala. Ticked off: allergic effector cells in the pathogenesis of alpha-gal syndrome. Current Allergy and Asthma Reports, Nov 2025. URL: https://doi.org/10.1007/s11882-025-01237-2, doi:10.1007/s11882-025-01237-2. This article has 3 citations and is from a peer-reviewed journal.

11. (taylor2024intrinsicriskfactors pages 6-8): Marissa L. Taylor, Gilbert J. Kersh, Johanna S. Salzer, Emma S. Jones, Alison M. Binder, Paige A. Armstrong, Shailesh K. Choudhary, Grace K. Commins, Claire L. Amelio, Brad J. Biggerstaff, Charles B. Beard, Lyle R. Petersen, and Scott P. Commins. Intrinsic risk factors for alpha-gal syndrome in a case-control study, 2019 to 2020. Annals of Allergy, Asthma &amp; Immunology, 132:759-764.e2, Jun 2024. URL: https://doi.org/10.1016/j.anai.2024.01.029, doi:10.1016/j.anai.2024.01.029. This article has 23 citations.

12. (macdougall2022themeatof pages 4-5): Jessica D Macdougall, Kevin O Thomas, and Onyinye I Iweala. The meat of the matter: understanding and managing alpha-gal syndrome. ImmunoTargets and Therapy, 11:37-54, Sep 2022. URL: https://doi.org/10.2147/itt.s276872, doi:10.2147/itt.s276872. This article has 71 citations.

13. (taylor2024intrinsicriskfactors pages 1-3): Marissa L. Taylor, Gilbert J. Kersh, Johanna S. Salzer, Emma S. Jones, Alison M. Binder, Paige A. Armstrong, Shailesh K. Choudhary, Grace K. Commins, Claire L. Amelio, Brad J. Biggerstaff, Charles B. Beard, Lyle R. Petersen, and Scott P. Commins. Intrinsic risk factors for alpha-gal syndrome in a case-control study, 2019 to 2020. Annals of Allergy, Asthma &amp; Immunology, 132:759-764.e2, Jun 2024. URL: https://doi.org/10.1016/j.anai.2024.01.029, doi:10.1016/j.anai.2024.01.029. This article has 23 citations.

14. (taylor2024intrinsicriskfactors pages 5-6): Marissa L. Taylor, Gilbert J. Kersh, Johanna S. Salzer, Emma S. Jones, Alison M. Binder, Paige A. Armstrong, Shailesh K. Choudhary, Grace K. Commins, Claire L. Amelio, Brad J. Biggerstaff, Charles B. Beard, Lyle R. Petersen, and Scott P. Commins. Intrinsic risk factors for alpha-gal syndrome in a case-control study, 2019 to 2020. Annals of Allergy, Asthma &amp; Immunology, 132:759-764.e2, Jun 2024. URL: https://doi.org/10.1016/j.anai.2024.01.029, doi:10.1016/j.anai.2024.01.029. This article has 23 citations.

15. (binder2023clinicalandlaboratory pages 1-1): Alison M. Binder, Dena Cherry‐Brown, Brad J. Biggerstaff, Emma S. Jones, Claire L. Amelio, Charles B. Beard, Lyle R. Petersen, Gilbert J. Kersh, Scott P. Commins, and Paige A. Armstrong. Clinical and laboratory features of patients diagnosed with alpha‐gal syndrome—2010–2019. Allergy, 78:477-487, Oct 2023. URL: https://doi.org/10.1111/all.15539, doi:10.1111/all.15539. This article has 42 citations and is from a highest quality peer-reviewed journal.

16. (nalcacı2024mysteriousallergycaused pages 6-7): Muhammed Nalçacı. Mysterious allergy caused by tick bite: alpha-gal syndrome. Turkiye parazitolojii dergisi, 48 3:195-207, Oct 2024. URL: https://doi.org/10.4274/tpd.galenos.2024.97720, doi:10.4274/tpd.galenos.2024.97720. This article has 7 citations.

17. (binder2023clinicalandlaboratory pages 2-2): Alison M. Binder, Dena Cherry‐Brown, Brad J. Biggerstaff, Emma S. Jones, Claire L. Amelio, Charles B. Beard, Lyle R. Petersen, Gilbert J. Kersh, Scott P. Commins, and Paige A. Armstrong. Clinical and laboratory features of patients diagnosed with alpha‐gal syndrome—2010–2019. Allergy, 78:477-487, Oct 2023. URL: https://doi.org/10.1111/all.15539, doi:10.1111/all.15539. This article has 42 citations and is from a highest quality peer-reviewed journal.

18. (propst2025alphagalsyndromeand pages 2-3): Susan B. H. Propst and Dorothea K. Thompson. Alpha-gal syndrome and the gastrointestinal reaction: a narrative review. Frontiers in Allergy, Jan 2025. URL: https://doi.org/10.3389/falgy.2025.1535103, doi:10.3389/falgy.2025.1535103. This article has 13 citations and is from a peer-reviewed journal.

19. (carson2022where’sthebeef? pages 3-4): Audrey S. Carson, Aliyah Gardner, and Onyinye I. Iweala. Where’s the beef? : understanding allergic responses to red meat in alpha-gal syndrome. Journal of immunology (Baltimore, Md. : 1950), 208:267-277, Jan 2022. URL: https://doi.org/10.4049/jimmunol.2100712, doi:10.4049/jimmunol.2100712. This article has 47 citations.

20. (vazrodrigues2022currentandfuture pages 6-7): Rita Vaz-Rodrigues, Lorena Mazuecos, and José de la Fuente. Current and future strategies for the diagnosis and treatment of the alpha-gal syndrome (ags). Journal of Asthma and Allergy, 15:957-970, Jul 2022. URL: https://doi.org/10.2147/jaa.s265660, doi:10.2147/jaa.s265660. This article has 70 citations and is from a peer-reviewed journal.

21. (macdougall2022themeatof pages 10-11): Jessica D Macdougall, Kevin O Thomas, and Onyinye I Iweala. The meat of the matter: understanding and managing alpha-gal syndrome. ImmunoTargets and Therapy, 11:37-54, Sep 2022. URL: https://doi.org/10.2147/itt.s276872, doi:10.2147/itt.s276872. This article has 71 citations.

22. (nalcacı2024mysteriousallergycaused pages 1-2): Muhammed Nalçacı. Mysterious allergy caused by tick bite: alpha-gal syndrome. Turkiye parazitolojii dergisi, 48 3:195-207, Oct 2024. URL: https://doi.org/10.4274/tpd.galenos.2024.97720, doi:10.4274/tpd.galenos.2024.97720. This article has 7 citations.

23. (propst2025alphagalsyndromeand pages 7-8): Susan B. H. Propst and Dorothea K. Thompson. Alpha-gal syndrome and the gastrointestinal reaction: a narrative review. Frontiers in Allergy, Jan 2025. URL: https://doi.org/10.3389/falgy.2025.1535103, doi:10.3389/falgy.2025.1535103. This article has 13 citations and is from a peer-reviewed journal.

24. (leder2024perioperativeconsiderationsin pages 3-5): John Leder, Anna Diederich, Bhavik Patel, Mark Bowie, Christian M Renwick, and Venkat Mangunta. Perioperative considerations in alpha-gal syndrome: a review. Cureus, Jan 2024. URL: https://doi.org/10.7759/cureus.53208, doi:10.7759/cureus.53208. This article has 16 citations.

25. (NCT07611435 chunk 1):  Beginning to Assess an Appropriate CONtrol for Oral Food Challenges in Alpha-Gal Syndrome (CoFAR-13) - BeACON4AG. National Institute of Allergy and Infectious Diseases (NIAID). 2026. ClinicalTrials.gov Identifier: NCT07611435

26. (macdougall2022themeatof pages 11-13): Jessica D Macdougall, Kevin O Thomas, and Onyinye I Iweala. The meat of the matter: understanding and managing alpha-gal syndrome. ImmunoTargets and Therapy, 11:37-54, Sep 2022. URL: https://doi.org/10.2147/itt.s276872, doi:10.2147/itt.s276872. This article has 71 citations.

27. (carson2022where’sthebeef? pages 1-3): Audrey S. Carson, Aliyah Gardner, and Onyinye I. Iweala. Where’s the beef? : understanding allergic responses to red meat in alpha-gal syndrome. Journal of immunology (Baltimore, Md. : 1950), 208:267-277, Jan 2022. URL: https://doi.org/10.4049/jimmunol.2100712, doi:10.4049/jimmunol.2100712. This article has 47 citations.

28. (choudhary2025singlecellmrnaanalysis pages 14-17): Shailesh K. Choudhary and Scott P. Commins. Single-cell mrna analysis and surface marker expression profiling of circulating immune cells in humans with alpha-gal syndrome. Frontiers in Immunology, Sep 2025. URL: https://doi.org/10.3389/fimmu.2025.1629310, doi:10.3389/fimmu.2025.1629310. This article has 2 citations and is from a peer-reviewed journal.

29. (commins2020diagnosis&amp;management pages 16-18): Scott P. Commins. Diagnosis &amp; management of alpha-gal syndrome: lessons from 2,500 patients. Jul 2020. URL: https://doi.org/10.1080/1744666x.2020.1782745, doi:10.1080/1744666x.2020.1782745. This article has 114 citations and is from a peer-reviewed journal.

30. (sharma2024tickbiteinducedalphagal pages 1-2): Surendra Raj Sharma, Shailesh K. Choudhary, Julia Vorobiov, Scott P. Commins, and Shahid Karim. Tick bite-induced alpha-gal syndrome and immunologic responses in an alpha-gal deficient murine model. Frontiers in Immunology, Feb 2024. URL: https://doi.org/10.3389/fimmu.2023.1336883, doi:10.3389/fimmu.2023.1336883. This article has 28 citations and is from a peer-reviewed journal.

31. (platts‐mills2025theimmunologyof pages 6-8): Thomas A. E. Platts‐Mills, Roopesh Singh Gangwar, Lisa Workman, and Jeffrey M. Wilson. The immunology of alpha‐gal syndrome: history, tick bites, ige, and delayed anaphylaxis to mammalian meat. Immunological Reviews, Jun 2025. URL: https://doi.org/10.1111/imr.70035, doi:10.1111/imr.70035. This article has 19 citations and is from a domain leading peer-reviewed journal.

32. (platts‐mills2025theimmunologyof pages 11-13): Thomas A. E. Platts‐Mills, Roopesh Singh Gangwar, Lisa Workman, and Jeffrey M. Wilson. The immunology of alpha‐gal syndrome: history, tick bites, ige, and delayed anaphylaxis to mammalian meat. Immunological Reviews, Jun 2025. URL: https://doi.org/10.1111/imr.70035, doi:10.1111/imr.70035. This article has 19 citations and is from a domain leading peer-reviewed journal.

33. (branicka2025alphagalsyndrome—aseries pages 4-6): Olga Branicka, Lesia Rozłucka, Radosław Gawlik, and Joanna Glück. Alpha-gal syndrome—a series of cases with different clinical pictures. International Journal of Molecular Sciences, 26:8601, Sep 2025. URL: https://doi.org/10.3390/ijms26178601, doi:10.3390/ijms26178601. This article has 0 citations.

34. (carson2022where’sthebeef? pages 9-11): Audrey S. Carson, Aliyah Gardner, and Onyinye I. Iweala. Where’s the beef? : understanding allergic responses to red meat in alpha-gal syndrome. Journal of immunology (Baltimore, Md. : 1950), 208:267-277, Jan 2022. URL: https://doi.org/10.4049/jimmunol.2100712, doi:10.4049/jimmunol.2100712. This article has 47 citations.

35. (carson2022where’sthebeef? pages 8-9): Audrey S. Carson, Aliyah Gardner, and Onyinye I. Iweala. Where’s the beef? : understanding allergic responses to red meat in alpha-gal syndrome. Journal of immunology (Baltimore, Md. : 1950), 208:267-277, Jan 2022. URL: https://doi.org/10.4049/jimmunol.2100712, doi:10.4049/jimmunol.2100712. This article has 47 citations.

36. (kepley2025tickedoffallergic pages 7-8): Christopher L. Kepley, Yinghui Wang, Amy Yelton, Eva R. Siebert, and Onyinye I. Iweala. Ticked off: allergic effector cells in the pathogenesis of alpha-gal syndrome. Current Allergy and Asthma Reports, Nov 2025. URL: https://doi.org/10.1007/s11882-025-01237-2, doi:10.1007/s11882-025-01237-2. This article has 3 citations and is from a peer-reviewed journal.

37. (carson2022where’sthebeef? pages 6-8): Audrey S. Carson, Aliyah Gardner, and Onyinye I. Iweala. Where’s the beef? : understanding allergic responses to red meat in alpha-gal syndrome. Journal of immunology (Baltimore, Md. : 1950), 208:267-277, Jan 2022. URL: https://doi.org/10.4049/jimmunol.2100712, doi:10.4049/jimmunol.2100712. This article has 47 citations.

38. (choudhary2025singlecellmrnaanalysis pages 17-18): Shailesh K. Choudhary and Scott P. Commins. Single-cell mrna analysis and surface marker expression profiling of circulating immune cells in humans with alpha-gal syndrome. Frontiers in Immunology, Sep 2025. URL: https://doi.org/10.3389/fimmu.2025.1629310, doi:10.3389/fimmu.2025.1629310. This article has 2 citations and is from a peer-reviewed journal.

39. (kuravi2022allergicresponseto pages 1-2): Kasinath V. Kuravi, Lori T. Sorrells, Joseph R. Nellis, Farzana Rahman, Anneke H. Walters, Robert G. Matheny, Shailesh K. Choudhary, David L. Ayares, Scott P. Commins, John R. Bianchi, and Joseph W. Turek. Allergic response to medical products in patients with alpha-gal syndrome. The Journal of Thoracic and Cardiovascular Surgery, 164:e411-e424, Dec 2022. URL: https://doi.org/10.1016/j.jtcvs.2021.03.100, doi:10.1016/j.jtcvs.2021.03.100. This article has 72 citations.

40. (kuravi2022allergicresponseto pages 6-9): Kasinath V. Kuravi, Lori T. Sorrells, Joseph R. Nellis, Farzana Rahman, Anneke H. Walters, Robert G. Matheny, Shailesh K. Choudhary, David L. Ayares, Scott P. Commins, John R. Bianchi, and Joseph W. Turek. Allergic response to medical products in patients with alpha-gal syndrome. The Journal of Thoracic and Cardiovascular Surgery, 164:e411-e424, Dec 2022. URL: https://doi.org/10.1016/j.jtcvs.2021.03.100, doi:10.1016/j.jtcvs.2021.03.100. This article has 72 citations.

41. (choudhary2025singlecellmrnaanalysis pages 4-5): Shailesh K. Choudhary and Scott P. Commins. Single-cell mrna analysis and surface marker expression profiling of circulating immune cells in humans with alpha-gal syndrome. Frontiers in Immunology, Sep 2025. URL: https://doi.org/10.3389/fimmu.2025.1629310, doi:10.3389/fimmu.2025.1629310. This article has 2 citations and is from a peer-reviewed journal.

42. (choudhary2025singlecellmrnaanalysis pages 8-11): Shailesh K. Choudhary and Scott P. Commins. Single-cell mrna analysis and surface marker expression profiling of circulating immune cells in humans with alpha-gal syndrome. Frontiers in Immunology, Sep 2025. URL: https://doi.org/10.3389/fimmu.2025.1629310, doi:10.3389/fimmu.2025.1629310. This article has 2 citations and is from a peer-reviewed journal.

43. (binder2023clinicalandlaboratory pages 8-8): Alison M. Binder, Dena Cherry‐Brown, Brad J. Biggerstaff, Emma S. Jones, Claire L. Amelio, Charles B. Beard, Lyle R. Petersen, Gilbert J. Kersh, Scott P. Commins, and Paige A. Armstrong. Clinical and laboratory features of patients diagnosed with alpha‐gal syndrome—2010–2019. Allergy, 78:477-487, Oct 2023. URL: https://doi.org/10.1111/all.15539, doi:10.1111/all.15539. This article has 42 citations and is from a highest quality peer-reviewed journal.

44. (binder2023clinicalandlaboratory pages 2-3): Alison M. Binder, Dena Cherry‐Brown, Brad J. Biggerstaff, Emma S. Jones, Claire L. Amelio, Charles B. Beard, Lyle R. Petersen, Gilbert J. Kersh, Scott P. Commins, and Paige A. Armstrong. Clinical and laboratory features of patients diagnosed with alpha‐gal syndrome—2010–2019. Allergy, 78:477-487, Oct 2023. URL: https://doi.org/10.1111/all.15539, doi:10.1111/all.15539. This article has 42 citations and is from a highest quality peer-reviewed journal.

45. (NCT06268717 chunk 1):  GI Alpha-Gal Study. University of North Carolina, Chapel Hill. 2023. ClinicalTrials.gov Identifier: NCT06268717

46. (macdougall2022themeatof pages 7-8): Jessica D Macdougall, Kevin O Thomas, and Onyinye I Iweala. The meat of the matter: understanding and managing alpha-gal syndrome. ImmunoTargets and Therapy, 11:37-54, Sep 2022. URL: https://doi.org/10.2147/itt.s276872, doi:10.2147/itt.s276872. This article has 71 citations.

47. (macdougall2022themeatof pages 8-10): Jessica D Macdougall, Kevin O Thomas, and Onyinye I Iweala. The meat of the matter: understanding and managing alpha-gal syndrome. ImmunoTargets and Therapy, 11:37-54, Sep 2022. URL: https://doi.org/10.2147/itt.s276872, doi:10.2147/itt.s276872. This article has 71 citations.

48. (propst2025alphagalsyndromeand pages 4-5): Susan B. H. Propst and Dorothea K. Thompson. Alpha-gal syndrome and the gastrointestinal reaction: a narrative review. Frontiers in Allergy, Jan 2025. URL: https://doi.org/10.3389/falgy.2025.1535103, doi:10.3389/falgy.2025.1535103. This article has 13 citations and is from a peer-reviewed journal.

49. (vazrodrigues2022currentandfuture pages 7-8): Rita Vaz-Rodrigues, Lorena Mazuecos, and José de la Fuente. Current and future strategies for the diagnosis and treatment of the alpha-gal syndrome (ags). Journal of Asthma and Allergy, 15:957-970, Jul 2022. URL: https://doi.org/10.2147/jaa.s265660, doi:10.2147/jaa.s265660. This article has 70 citations and is from a peer-reviewed journal.

50. (NCT07526558 chunk 1):  Mast Cell Treatment in Post-tick Bite Illness (PTBI). University of North Carolina, Chapel Hill. 2026. ClinicalTrials.gov Identifier: NCT07526558

51. (leder2024perioperativeconsiderationsin pages 2-3): John Leder, Anna Diederich, Bhavik Patel, Mark Bowie, Christian M Renwick, and Venkat Mangunta. Perioperative considerations in alpha-gal syndrome: a review. Cureus, Jan 2024. URL: https://doi.org/10.7759/cureus.53208, doi:10.7759/cureus.53208. This article has 16 citations.

52. (leder2024perioperativeconsiderationsin pages 1-2): John Leder, Anna Diederich, Bhavik Patel, Mark Bowie, Christian M Renwick, and Venkat Mangunta. Perioperative considerations in alpha-gal syndrome: a review. Cureus, Jan 2024. URL: https://doi.org/10.7759/cureus.53208, doi:10.7759/cureus.53208. This article has 16 citations.

53. (leder2024perioperativeconsiderationsin pages 7-9): John Leder, Anna Diederich, Bhavik Patel, Mark Bowie, Christian M Renwick, and Venkat Mangunta. Perioperative considerations in alpha-gal syndrome: a review. Cureus, Jan 2024. URL: https://doi.org/10.7759/cureus.53208, doi:10.7759/cureus.53208. This article has 16 citations.

54. (NCT07611435 chunk 2):  Beginning to Assess an Appropriate CONtrol for Oral Food Challenges in Alpha-Gal Syndrome (CoFAR-13) - BeACON4AG. National Institute of Allergy and Infectious Diseases (NIAID). 2026. ClinicalTrials.gov Identifier: NCT07611435

55. (NCT07177729 chunk 1):  The α-gal Syndrome - Investigating Immune Reactions to Tick Bites. Luxembourg Institute of Health. 2025. ClinicalTrials.gov Identifier: NCT07177729

## Artifacts

- [Edison artifact artifact-00](Alpha-gal_Syndrome-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Alpha-gal_Syndrome-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Alpha-gal_Syndrome-deep-research-falcon_artifacts/artifact-02.md)