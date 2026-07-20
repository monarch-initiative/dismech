---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T18:50:46.412848'
end_time: '2026-07-05T19:23:47.735617'
duration_seconds: 1981.32
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Postural Orthostatic Tachycardia Syndrome
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 52
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Postural_Orthostatic_Tachycardia_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Postural_Orthostatic_Tachycardia_Syndrome-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Postural_Orthostatic_Tachycardia_Syndrome-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Postural Orthostatic Tachycardia Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Postural Orthostatic Tachycardia Syndrome** covering all of the
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
- **Disease Name:** Postural Orthostatic Tachycardia Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Postural Orthostatic Tachycardia Syndrome** covering all of the
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


# Comprehensive Research Report: Postural Orthostatic Tachycardia Syndrome (POTS)

## 1. Disease Information

### Overview
Postural Orthostatic Tachycardia Syndrome (POTS) is a chronic, debilitating autonomic nervous system disorder characterized by an excessive increase in heart rate of ≥30 beats per minute (bpm) within 10 minutes of assuming an upright posture (or ≥40 bpm in children and adolescents under 19 years), without accompanying orthostatic hypotension (defined as a sustained decrease in systolic blood pressure of ≥20 mmHg or diastolic blood pressure of ≥10 mmHg within 3 minutes of standing) (schiweck2026systematicliteraturereview pages 1-2, roy2025autonomicdysfunctionin pages 1-4, blitshteyn2026posturalorthostatictachycardia pages 2-4). Symptoms of orthostatic intolerance must be present for at least 3 months for formal diagnosis (schiweck2026systematicliteraturereview pages 1-2, blitshteyn2026posturalorthostatictachycardia pages 2-4). POTS affects an estimated 1–3 million people in the United States (0.2–1.0% of the population), predominantly young women aged 15–50, with a female-to-male ratio of approximately 6:1 (roy2025autonomicdysfunctionin pages 1-4, johansson2022plasmaproteomicprofiling pages 1-2, mallick2023covid19inducedpostural pages 2-4).

### Key Identifiers
The following table summarizes the core identifiers and characteristics:

| Field | Value | Notes / Evidence |
|---|---|---|
| Disease name | Postural Orthostatic Tachycardia Syndrome | Dysautonomia characterized by excessive orthostatic tachycardia without orthostatic hypotension (roy2025autonomicdysfunctionin pages 1-4, schiweck2026systematicliteraturereview pages 1-2, mallick2023covid19inducedpostural pages 1-2) |
| MONDO ID | MONDO:0011479 | Disease-target association retrieved from Open Targets for postural orthostatic tachycardia syndrome (OpenTargets Search: postural orthostatic tachycardia syndrome) |
| OMIM | 604715 | Commonly used disease identifier for POTS in genetic/disease databases |
| ICD-10 | I49.8 | Often mapped clinically under “Other specified cardiac arrhythmias”; coding practice may vary by institution |
| MeSH | Postural Orthostatic Tachycardia Syndrome | Standard biomedical subject heading used in literature indexing |
| Common synonyms | POTS; Postural Tachycardia Syndrome; Orthostatic tachycardia syndrome | Abbreviation and alternate naming used across reviews and clinical literature (schiweck2026systematicliteraturereview pages 1-2, mallick2023covid19inducedpostural pages 1-2) |
| Prevalence | ~0.2% of the general population; up to 1% of the U.S. population; ~1–3 million people in the U.S. | Recent reviews report 0.2% prevalence, while broader U.S. estimates range to 1% and 1–3 million affected individuals (schiweck2026systematicliteraturereview pages 1-2, roy2025autonomicdysfunctionin pages 1-4, johansson2022plasmaproteomicprofiling pages 1-2) |
| Sex ratio | Predominantly female; ~6:1 female:male; ~70–80% women | Strong female predominance is consistently reported, especially in adolescents and adults of reproductive age (mallick2023covid19inducedpostural pages 2-4, johansson2022plasmaproteomicprofiling pages 1-2) |
| Typical age of onset | Usually 15–50 years; often adolescents and young adults | Reviews describe onset most commonly in youth to mid-adulthood, often affecting women of reproductive age (wu2024anoverviewof pages 2-3, roy2025autonomicdysfunctionin pages 1-4, johansson2022plasmaproteomicprofiling pages 1-2) |
| Primary subtypes | Neuropathic; Hyperadrenergic; Hypovolemic | These phenotypes are widely described, though overlap between categories is common (blitshteyn2026posturalorthostatictachycardia pages 2-4, steinberg2023narrativereviewof pages 2-3) |


*Table: This table summarizes the core disease identifiers and high-yield epidemiologic and clinical characteristics for Postural Orthostatic Tachycardia Syndrome. It is useful as a quick-reference scaffold for a disease knowledge base entry.*

**Common Synonyms:** POTS, Postural Tachycardia Syndrome, Orthostatic Tachycardia Syndrome, Orthostatic Intolerance with Tachycardia.

**MONDO ID:** MONDO:0011479 (OpenTargets Search: postural orthostatic tachycardia syndrome)

**OMIM:** 604715

**ICD-10:** I49.8 (Other specified cardiac arrhythmias)

---

## 2. Etiology

### Disease Causal Factors
POTS is a heterogeneous, multifactorial disorder with no single identified cause. The etiology involves a complex interplay of autonomic dysfunction, autoimmune processes, cardiovascular deconditioning, and neuroendocrine dysregulation (blitshteyn2026posturalorthostatictachycardia pages 2-4, qu2024navigatingcomplexityin pages 5-7, qu2024navigatingcomplexityin pages 3-5).

**Common Triggers Include:**
- **Viral infections** (most common trigger), including SARS-CoV-2, Epstein-Barr virus, and other pathogens (roy2025autonomicdysfunctionin pages 1-4, mallick2023covid19inducedpostural pages 1-2)
- **Surgical procedures** (roy2025autonomicdysfunctionin pages 1-4)
- **Pregnancy** (blitshteyn2026posturalorthostatictachycardia pages 2-4)
- **Autoimmune diseases** (roy2025autonomicdysfunctionin pages 1-4)
- **Physical trauma or prolonged deconditioning** (steinberg2023narrativereviewof pages 1-2)

### Risk Factors

**Genetic Risk Factors:**
- Mutations in *SLC6A2* (solute carrier family 6 member 2), encoding the norepinephrine transporter (NET), cause NET deficiency leading to impaired norepinephrine reuptake and elevated circulating norepinephrine levels (steinberg2023narrativereviewof pages 2-3, qu2024navigatingcomplexityin pages 5-7, OpenTargets Search: postural orthostatic tachycardia syndrome)
- GWAS studies have identified gene sets associated with substance-related disorders, cell-cell junctions, synaptic membranes, transporter complexes, and estrogen responses (qu2024navigatingcomplexityin pages 9-10)
- Whole exome sequencing highlighted genes related to muscular and myocardial dysfunction and mitochondrial activity (qu2024navigatingcomplexityin pages 9-10)
- Certain genetic variants influencing autonomic nervous system function, blood volume regulation, or cardiovascular response may predispose to POTS (qu2024navigatingcomplexityin pages 2-3)

**Environmental Risk Factors:**
- Female sex (70–80% of patients are women) (johansson2022plasmaproteomicprofiling pages 1-2, mallick2023covid19inducedpostural pages 2-4)
- Age 15–50 years, particularly adolescents and young adults (roy2025autonomicdysfunctionin pages 1-4)
- Post-infectious states, particularly post-COVID-19 (mallick2023covid19inducedpostural pages 1-2, pena2024autoimmunityinsyndromes pages 6-8)
- Deconditioning and prolonged bed rest (steinberg2023narrativereviewof pages 1-2)
- Hormonal influences: onset commonly around menarche, symptom exacerbation with menstruation (blitshteyn2026posturalorthostatictachycardia pages 2-4)
- The condition is more commonly reported in Caucasian populations, though other populations may be underrepresented due to healthcare access disparities (qu2024navigatingcomplexityin pages 2-3)

### Gene-Environment Interactions
Genetic variants affecting autonomic function can be modulated by environmental conditions such as diet, stress, and physical activity levels, which vary across populations and impact genetic trait expression (qu2024navigatingcomplexityin pages 2-3). Post-infectious autoimmunity, where viral infection triggers autoantibody production in genetically susceptible individuals, represents a key gene-environment interaction in POTS pathogenesis (qu2024navigatingcomplexityin pages 5-7, elrhermoul2023autoimmunityinlong pages 2-3).

---

## 3. Phenotypes

### Clinical Subtypes
POTS is classified into three primary phenotypes, though significant clinical overlap is common (blitshteyn2026posturalorthostatictachycardia pages 2-4, steinberg2023narrativereviewof pages 2-3):

1. **Neuropathic POTS:** Involves autonomic denervation, particularly sympathetic denervation of lower extremities, leading to impaired vasoconstriction and blood pooling. Associated with small fiber neuropathy affecting postganglionic sympathetic innervation (steinberg2023narrativereviewof pages 2-3, qu2024navigatingcomplexityin pages 3-5). *HPO: HP:0012332 (Abnormal autonomic nervous system physiology)*

2. **Hyperadrenergic POTS:** Characterized by elevated standing plasma norepinephrine (>600 pg/mL), with symptoms including palpitations, tremulousness, and excessive sympathetic activation. Associated with SLC6A2/NET mutations (steinberg2023narrativereviewof pages 2-3). *HPO: HP:0012670 (Orthostatic tachycardia)*

3. **Hypovolemic POTS:** Features persistently low plasma volumes related to renin-angiotensin-aldosterone system (RAAS) dysregulation, with reduced venous return and compensatory tachycardia (steinberg2023narrativereviewof pages 2-3, qu2024navigatingcomplexityin pages 3-5).

### Symptoms and Clinical Signs

**Orthostatic Symptoms** (worsen with standing):
- Tachycardia/palpitations (*HP:0001962*, *HP:0001649*)
- Dizziness/lightheadedness (*HP:0002321*)
- Presyncope and syncope (*HP:0001279*)
- Visual disturbances/blurred vision (*HP:0000572*)
- Dyspnea (*HP:0002094*)
- Chest pain (*HP:0100749*)
- Sweating changes (*HP:0000975*)

**Non-Orthostatic Symptoms:**
- Fatigue (often cyclic, lasting days to weeks) (*HP:0012378*) (mallick2023covid19inducedpostural pages 2-4, mallick2023covid19inducedpostural pages 4-5)
- Cognitive dysfunction/"brain fog" (memory problems, attention difficulties) (*HP:0100543*) (roy2025autonomicdysfunctionin pages 10-12, mallick2023covid19inducedpostural pages 4-5)
- Gastrointestinal dysfunction (nausea, constipation, diarrhea, abdominal pain, gastroparesis) (*HP:0002027*) (mallick2023covid19inducedpostural pages 4-5)
- Sleep disturbance (*HP:0002360*) (wu2024anoverviewof pages 2-3)
- Headache/migraine (*HP:0002076*) (wu2024anoverviewof pages 2-3)
- Anxiety and depression (*HP:0000739*) (mallick2023covid19inducedpostural pages 2-4)
- Bladder dysfunction with nocturia (*HP:0000017*) (mallick2023covid19inducedpostural pages 4-5)
- Dermatologic manifestations including livedo reticularis and Raynaud's phenomenon (mallick2023covid19inducedpostural pages 4-5)

**Onset and Progression:**
- Typical onset age: 15–50 years, often adolescence or young adulthood (roy2025autonomicdysfunctionin pages 1-4, wu2024anoverviewof pages 2-3)
- Onset pattern: Often subacute following a triggering event (viral infection, surgery, pregnancy)
- Course: Chronic, fluctuating; symptom severity influenced by hydration, temperature, humidity, and menstrual cycle (wu2024anoverviewof pages 2-3)

### Quality of Life Impact
POTS profoundly impairs quality of life, causing limitations in daily activities and severely affecting patients' ability to work and socialize (wei2025pathophysiologicalmechanismsof pages 1-2). Patients report significant decreases in quality of life due to the combination of autonomic, cognitive, and gastrointestinal symptoms (roy2025autonomicdysfunctionin pages 10-12). Approximately one-third of patients remain symptomatic despite escalation of medical therapy (pena2024autoimmunityinsyndromes pages 8-9).

---

## 4. Genetic/Molecular Information

### Causal Gene
- **SLC6A2** (Solute Carrier Family 6 Member 2; ENSG00000103546): Encodes the norepinephrine transporter (NET). Loss-of-function mutations impair norepinephrine reuptake, resulting in elevated circulating norepinephrine and hyperadrenergic POTS symptoms (OpenTargets Search: postural orthostatic tachycardia syndrome, steinberg2023narrativereviewof pages 2-3, qu2024navigatingcomplexityin pages 5-7). This is the sole disease-target association identified in OpenTargets (score: 0.509; PMID: 10684912) (OpenTargets Search: postural orthostatic tachycardia syndrome).

### GWAS and Proteomic Findings
Genomic and proteomic studies have identified additional molecular contributors:
- **GWAS:** Gene sets associated with synaptic membranes, transporter complexes, estrogen responses, and cell-cell junctions (qu2024navigatingcomplexityin pages 9-10)
- **WES:** Genes related to myocardial dysfunction and mitochondrial activity (qu2024navigatingcomplexityin pages 9-10)
- **Differentially expressed proteins:** 30 differentially expressed plasma proteins identified by label-free mass spectrometry, including six upregulated actin cytoskeleton proteins: *MYL1* (fast-twitch muscle contraction), *MYL12B* (vascular smooth muscle function), *ILK* (cardiac and vascular responses), *PARVB* (vascular integrity), *CAVIN2* (endothelial signaling), and *WDR1* (actin dynamics) (qu2024navigatingcomplexityin pages 9-10, johansson2022plasmaproteomicprofiling pages 1-2)
- **Biomarkers:** Growth hormone (GH) elevated (especially in women) and myoglobin (MB) reduced (especially in men) suggest sex-specific immune-neuroendocrine dysregulation (qu2024navigatingcomplexityin pages 9-10)

### Autoantibodies
Autoimmunity is increasingly recognized as a central pathophysiological mechanism. The following table summarizes the key autoantibodies identified in POTS:

| Autoantibody Target | Abbreviation | Receptor Type | Functional Effect | Prevalence/Clinical Significance |
|---|---|---|---|---|
| Alpha-1 adrenergic receptor | α1-AR | GPCR | Impairs peripheral vasoconstriction; may contribute to venous pooling and orthostatic intolerance | ~89% of POTS patients in one cited study; widely implicated in autoimmune/hyperadrenergic POTS (chakraborty2023noninvasivevagusnerve pages 2-3, elrhermoul2023autoimmunityinlong pages 2-3, johansson2022plasmaproteomicprofiling pages 6-7) |
| Beta-1 adrenergic receptor | β1-AR | GPCR | Enhances adrenergic cardiac responses; may promote tachycardia | Frequently elevated/reported in POTS autoantibody panels (blitshteyn2026posturalorthostatictachycardia pages 2-4, chakraborty2023noninvasivevagusnerve pages 2-3, blitshteyn2026posturalorthostatictachycardiaa pages 2-4) |
| Beta-2 adrenergic receptor | β2-AR | GPCR | Enhances sympathetic outflow and abnormal adrenergic signaling | Frequently elevated; among the most common antibodies in post-COVID POTS series (chakraborty2023noninvasivevagusnerve pages 2-3, pena2024autoimmunityinsyndromes pages 6-8) |
| Muscarinic M2 acetylcholine receptor | M2AChR | GPCR | Impairs parasympathetic/cholinergic regulation of heart rate | Commonly found in autoimmune POTS literature and GPCR autoantibody profiles (chakraborty2023noninvasivevagusnerve pages 2-3, blitshteyn2026posturalorthostatictachycardiaa pages 2-4, pena2024autoimmunityinsyndromes pages 6-8) |
| Muscarinic M3 acetylcholine receptor | M3AChR | GPCR | May affect smooth muscle and autonomic effector function | Reported in autonomic autoimmunity literature overlapping with POTS (chakraborty2023noninvasivevagusnerve pages 2-3, blitshteyn2026posturalorthostatictachycardiaa pages 2-4) |
| Angiotensin II type 1 receptor | AT1-R | GPCR | Alters vascular tone and RAAS signaling | Common in post-COVID POTS reports; often co-detected with β2-AR and M2R antibodies (chakraborty2023noninvasivevagusnerve pages 2-3, pena2024autoimmunityinsyndromes pages 6-8) |
| Ganglionic acetylcholine receptor | gAChR | Ligand-gated ion channel | Impairs autonomic ganglionic transmission | Recognized marker of autoimmune autonomic ganglionopathy; also reported in subsets of POTS patients (qu2024navigatingcomplexityin pages 5-7, qu2024navigatingcomplexityin pages 3-5, blitshteyn2026posturalorthostatictachycardiaa pages 2-4) |
| Opioid-like 1 receptor | OLR1 / opioid-like 1 receptor | GPCR | May modulate autonomic signaling | Reported in expanded autoimmune POTS autoantibody profiles; clinical significance remains uncertain (blitshteyn2026posturalorthostatictachycardiaa pages 2-4) |


*Table: This table summarizes the principal autoantibodies reported in POTS, the receptor classes they target, and their proposed physiologic effects. It is useful for understanding the autoimmune hypothesis of POTS and for distinguishing well-reported versus still-emerging antibody associations.*

Functional autoantibodies against G-protein coupled receptors (GPCRs) act as partial agonists or allosteric activators, enhancing adrenergic responses and sympathetic outflow while impairing vasoconstriction (chakraborty2023noninvasivevagusnerve pages 2-3). In one study, approximately 89% of POTS patients exhibited elevated autoantibodies against the α1 adrenergic receptor (johansson2022plasmaproteomicprofiling pages 6-7). A study of 31 post-COVID POTS patients found all had positive autoantibodies, most frequently β2-AR, M2R, and AT1-R (pena2024autoimmunityinsyndromes pages 6-8).

### Proteomic Profiling
Plasma proteomic profiling revealed a distinctive proteomic footprint in POTS characterized by a hypercoagulable state (upregulated platelet proteins GP1BA, GP1BB, TUBB1), proinflammatory state (elevated beta-2-microglobulin/B2M), enhanced cardiac contractility and hypertrophy, and increased adrenergic activity. STRING pathway analysis showed strong enrichment in platelet aggregation (FDR 6.88×10⁻⁶) and activation (FDR 1.39×10⁻⁵) pathways (johansson2022plasmaproteomicprofiling pages 1-2, johansson2022plasmaproteomicprofiling pages 3-5, johansson2022plasmaproteomicprofiling pages 5-6). These findings support the hypothesis that "POTS may be an autoimmune, inflammatory and hyperadrenergic disorder" (johansson2022plasmaproteomicprofiling pages 1-2). Proteomic data are deposited in the ProteomeXchange Consortium (dataset PXD031458) (johansson2022plasmaproteomicprofiling pages 7-8).

CSF proteomic analysis in ME/CFS patients with POTS showed enrichment of neutrophil degranulation and platelet activation pathways (bragee2026proteomicsignaturesin pages 1-7).

---

## 5. Environmental Information

### Infectious Agents
**SARS-CoV-2** has emerged as a major trigger for POTS development. COVID-19 survivors develop POTS within 6–8 months of infection, with autonomic dysfunction noted in more than half of COVID-19 patients as post-acute sequelae in some studies (mallick2023covid19inducedpostural pages 1-2). Proposed mechanisms include: autoantibody production against autonomic nerve fibers, direct viral neurotoxicity via ACE2 receptor binding, sympathetic nervous system stimulation, cytokine-mediated immune activation, RAAS dysregulation, and brainstem invasion disrupting cardiovascular regulation (mallick2023covid19inducedpostural pages 2-4). Distinctive SARS-CoV-2-specific IgA responses may contribute to vascular and autonomic dysfunction through IgA-mediated inflammation (qu2024navigatingcomplexityin pages 5-7).

Other viral triggers historically associated with POTS include Epstein-Barr virus, influenza, and various other infections (roy2025autonomicdysfunctionin pages 1-4).

### Lifestyle Factors
Deconditioning from prolonged inactivity or bed rest can precipitate or worsen POTS. Hydration status, temperature exposure, humidity, and menstrual cycle stage all modulate symptom severity (wu2024anoverviewof pages 2-3).

---

## 6. Mechanism / Pathophysiology

### Core Pathophysiological Mechanisms

**Autonomic Dysfunction (Dysautonomia):**
Disruption of the sympathetic-parasympathetic balance is fundamental to POTS. Exaggerated parasympathetic withdrawal and sympathetic overdrive during postural stress are principal mechanisms of postural tachycardia (chakraborty2023noninvasivevagusnerve pages 2-3, qu2024navigatingcomplexityin pages 3-5). Heart rate variability analysis demonstrates consistently attenuated parasympathetic tone (chakraborty2023noninvasivevagusnerve pages 2-3).

**Hypovolemia and Hemodynamic Dysfunction:**
Hemodynamic modeling demonstrates that hypovolemia reduces cerebral blood flow by approximately 100 mL/min through a 30% decrease in blood volume, while vascular dysfunction marked by 50–100% increase in arterial stiffness further diminishes cardiac output and cerebral perfusion, triggering compensatory tachycardia (wei2025pathophysiologicalmechanismsof pages 1-2). Thoracic hypovolemia results from blood pooling, dehydration, inadequate fluid intake, and RAAS abnormalities (qu2024navigatingcomplexityin pages 3-5).

**Autoimmune Mechanisms:**
POTS shows elevated autoimmune markers and autoantibodies targeting autonomic nervous system components. Autoantibodies against GPCRs (α1-AR, β1-AR, β2-AR, M2AChR, AT1-R) and ganglionic acetylcholine receptors (gAChR) impair normal vasoconstriction, enhance sympathetic activation, and disrupt autonomic balance (chakraborty2023noninvasivevagusnerve pages 2-3, blitshteyn2026posturalorthostatictachycardiaa pages 2-4). Elevated pro-inflammatory markers including IL-1β, IL-6, and TNF-α have been documented (blitshteyn2026posturalorthostatictachycardiaa pages 2-4).

**Neuropathic Mechanisms:**
Small fiber neuropathy (SFN) affects up to half of POTS cases, causing dysautonomia through impaired adrenergic nervous function and reduced sympathetic innervation of lower extremities (mallick2023covid19inducedpostural pages 2-4, qu2024navigatingcomplexityin pages 3-5).

**Mast Cell Activation:**
Mast cell dysregulation leads to release of vasoactive substances causing vasodilation, flushing, and orthostatic intolerance. Elevated baseline tryptase levels and *TPSAB1* gene variations are associated with multisystem symptoms (qu2024navigatingcomplexityin pages 5-7, steinberg2023narrativereviewof pages 3-4).

**Neuroendocrine Dysfunction:**
POTS patients exhibit elevated catecholamine and angiotensin II levels with decreased plasma renin and aldosterone, indicating RAAS dysregulation (mallick2023covid19inducedpostural pages 2-4).

### Causal Chain
Initial trigger (viral infection, surgery, etc.) → autoimmune activation and/or direct autonomic damage → impaired peripheral vasoconstriction and venous pooling → reduced venous return and thoracic hypovolemia → decreased cardiac preload → compensatory sympathetic activation and tachycardia → cerebral hypoperfusion → orthostatic intolerance symptoms (wei2025pathophysiologicalmechanismsof pages 1-2, qu2024navigatingcomplexityin pages 3-5, chakraborty2023noninvasivevagusnerve pages 2-3).

**GO Biological Process terms:** GO:0001659 (temperature homeostasis), GO:0008217 (regulation of blood pressure), GO:0042756 (drinking behavior), GO:0003013 (circulatory system process), GO:0001974 (blood vessel remodeling)

**Cell types involved (CL terms):** CL:0002150 (postganglionic sympathetic neuron), CL:0000746 (cardiac muscle cell), CL:0000235 (macrophage), CL:0000097 (mast cell), CL:0000540 (neuron), CL:0002139 (endothelial cell of vein)

---

## 7. Anatomical Structures Affected

### Primary Organs and Systems
- **Cardiovascular system** (heart, blood vessels): Primary site of tachycardia and hemodynamic dysfunction; *UBERON:0000948* (heart), *UBERON:0001981* (blood vessel)
- **Autonomic nervous system:** Central pathology; *UBERON:0002410* (autonomic nervous system)
- **Central nervous system** (brain): Cerebral hypoperfusion causing cognitive dysfunction; SPECT scans reveal abnormal blood flow in lateral prefrontal and sensorimotor cortices (roy2025autonomicdysfunctionin pages 10-12); *UBERON:0000955* (brain)
- **Gastrointestinal tract:** Gastroparesis, motility disorders; *UBERON:0001555* (digestive tract)

### Secondary Involvement
- **Endocrine system:** RAAS dysregulation, catecholamine excess
- **Immune system:** Autoantibody production, chronic inflammation
- **Peripheral nervous system:** Small fiber neuropathy
- **Urinary system:** Bladder dysfunction

---

## 8. Temporal Development

### Onset
- Typical age of onset: 15–50 years, most commonly in adolescence or early adulthood (roy2025autonomicdysfunctionin pages 1-4, johansson2022plasmaproteomicprofiling pages 1-2)
- Onset pattern: Usually subacute, developing over weeks to months following a trigger event

### Progression
- Disease course: Chronic, fluctuating, with episodic exacerbations
- Duration: Often years to decades; some patients experience spontaneous improvement
- Prognosis: Remains unclear in the long term, particularly for the increasing population acquiring POTS following COVID-19 (roy2025autonomicdysfunctionin pages 10-12)
- Exercise programs have shown that 53–71% of patients no longer meet POTS diagnostic criteria after three months of structured training (roy2025autonomicdysfunctionin pages 7-10)

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence:** 0.2% of the general population; up to 1% of the US population (approximately 1–3 million people in the US) (schiweck2026systematicliteraturereview pages 1-2, roy2025autonomicdysfunctionin pages 1-4, johansson2022plasmaproteomicprofiling pages 1-2)
- **In ME/CFS population:** 11–25% prevalence (schiweck2026systematicliteraturereview pages 1-2)
- **Sex ratio:** Approximately 6:1 female:male; 70–80% of patients are women (johansson2022plasmaproteomicprofiling pages 1-2, mallick2023covid19inducedpostural pages 2-4)
- **Age distribution:** Predominantly affects individuals aged 12–50 years (roy2025autonomicdysfunctionin pages 1-4)
- **Racial distribution:** More commonly reported in Caucasian populations, though other groups may be underrepresented (qu2024navigatingcomplexityin pages 2-3)

### Inheritance Pattern
POTS is generally considered multifactorial/polygenic rather than following a simple Mendelian inheritance pattern. Familial clustering has been reported, and *SLC6A2* mutations represent a rare monogenic cause (autosomal dominant with variable penetrance). The condition demonstrates variable expressivity and incomplete penetrance.

### Post-COVID Impact
The COVID-19 pandemic has substantially increased POTS prevalence. A study found that all 31 post-COVID POTS patients had positive autoantibodies (ranging from 2 to 7 types), and 17 of 20 patients in a case series had residual autonomic effects 6 months post-infection, with 12 unable to return to work (pena2024autoimmunityinsyndromes pages 6-8).

---

## 10. Diagnostics

### Clinical Diagnostic Criteria
Diagnosis requires (schiweck2026systematicliteraturereview pages 1-2, roy2025autonomicdysfunctionin pages 1-4, mallick2023covid19inducedpostural pages 4-5):
1. Sustained heart rate increase ≥30 bpm (≥40 bpm in children/adolescents) within 10 minutes of standing or head-up tilt
2. Absence of orthostatic hypotension
3. Symptoms of orthostatic intolerance lasting ≥3 months
4. Exclusion of other causes of tachycardia

### Clinical Tests
- **Tilt table testing:** Gold standard; measures heart rate, blood pressure, oxygen, and CO₂ during postural transition (mallick2023covid19inducedpostural pages 4-5)
- **Active standing test:** Alternative bedside assessment
- **Heart rate variability analysis** (roy2025autonomicdysfunctionin pages 1-4)
- **Autonomic reflex testing** including sudomotor testing (mallick2023covid19inducedpostural pages 4-5)
- **Skin biopsy:** For small fiber neuropathy assessment (intraepidermal nerve fiber density)
- **Plasma norepinephrine levels:** Standing levels >600 pg/mL suggest hyperadrenergic subtype (steinberg2023narrativereviewof pages 2-3)
- **Autoantibody panels:** GPCR autoantibodies (adrenergic, muscarinic, angiotensin receptors), gAChR antibodies (chakraborty2023noninvasivevagusnerve pages 2-3, blitshteyn2026posturalorthostatictachycardiaa pages 2-4)

### Differential Diagnosis
Conditions to rule out include: orthostatic hypotension, inappropriate sinus tachycardia, anxiety disorders, cardiac arrhythmias, thyroid disorders, pheochromocytoma, dehydration, and medication side effects (steinberg2023narrativereviewof pages 1-2).

### Biomarkers
Elevated B2M (beta-2-microglobulin) was identified as the most upregulated proinflammatory protein in POTS (johansson2022plasmaproteomicprofiling pages 5-6). Platelet activation and thrombogenicity markers are consistently elevated (johansson2022plasmaproteomicprofiling pages 3-5).

---

## 11. Outcome/Prognosis

### Disease Course
Long-term prognosis remains incompletely characterized. Some patients experience gradual improvement, while others have chronic, fluctuating courses (roy2025autonomicdysfunctionin pages 10-12). Exercise training programs show significant benefit, with 53–71% of patients no longer meeting POTS diagnostic criteria after three months (roy2025autonomicdysfunctionin pages 7-10). However, approximately one-third of patients remain symptomatic despite treatment escalation (pena2024autoimmunityinsyndromes pages 8-9). Post-COVID POTS prognosis is particularly uncertain and requires further longitudinal study (roy2025autonomicdysfunctionin pages 10-12).

### Quality of Life
POTS causes significant functional impairment comparable to that of congestive heart failure and COPD. Patients face physical, psychological, and social challenges including inability to work, decreased social participation, and mental health impacts (wei2025pathophysiologicalmechanismsof pages 1-2, mouslmani2025characterizationofpostural pages 9-10).

---

## 12. Treatment

### Treatment Overview
The following table provides a comprehensive summary of POTS treatment modalities:

| Treatment Category | Treatment Name | Mechanism of Action | Evidence Level | Key Notes |
|---|---|---|---|---|
| Non-pharmacological | Exercise training (Levine Protocol) | Improves cardiac output, reverses deconditioning, increases orthostatic tolerance | Moderate | Reported benefit with structured recumbent-to-upright training; 53–71% of patients no longer met POTS criteria after 3 months in cited summaries (steinberg2023narrativereviewof pages 6-7, roy2025autonomicdysfunctionin pages 7-10) |
| Non-pharmacological | Salt supplementation (8–12 g/day) | Expands plasma volume | Expert consensus | First-line measure; commonly recommended with fluids for most patients (steinberg2023narrativereviewof pages 6-7, mallick2023covid19inducedpostural pages 5-6) |
| Non-pharmacological | Fluid intake (2–3 L/day) | Expands intravascular volume | Expert consensus | First-line measure; often paired with sodium loading (steinberg2023narrativereviewof pages 6-7, steinberg2023narrativereviewof pages 5-6, mallick2023covid19inducedpostural pages 5-6) |
| Non-pharmacological | Compression garments (20–30 mmHg) | Reduces venous pooling in lower extremities and abdomen | Moderate | Waist-high or thigh-high garments/abdominal binders preferred in reviews and management algorithms (steinberg2023narrativereviewof pages 7-8, steinberg2023narrativereviewof pages 5-6, schiweck2026systematicliteraturereview pages 1-2) |
| Non-pharmacological | Vagus nerve stimulation (tVNS) | Restores sympathovagal balance; may reduce inflammation | Emerging | Non-invasive option under study; highlighted as a possible first-line adjunct in recent reviews (chakraborty2023noninvasivevagusnerve pages 2-3, schiweck2026systematicliteraturereview pages 1-2) |
| Pharmacological | Ivabradine | If-channel blocker in sinoatrial node; lowers heart rate without reducing blood pressure | RCT evidence | Frequently highlighted as one of the stronger pharmacologic options; Phase 3 trial completed: NCT03182725 (schiweck2026systematicliteraturereview pages 1-2, qu2024navigatingcomplexityin pages 10-12, mallick2023covid19inducedpostural pages 5-6, OpenTargets Search: postural orthostatic tachycardia syndrome) |
| Pharmacological | Beta-blockers (e.g., propranolol, bisoprolol) | Heart-rate reduction and sympatholytic effect | RCT evidence | Multiple options used clinically; improve tachycardia and symptoms in many patients (steinberg2023narrativereviewof pages 6-7, steinberg2023narrativereviewof pages 5-6, schiweck2026systematicliteraturereview pages 1-2, mallick2023covid19inducedpostural pages 5-6) |
| Pharmacological | Midodrine | Alpha-1 adrenergic agonist causing peripheral vasoconstriction | Limited RCT | Often used for venous pooling/hypotension phenotype; hemodynamic benefit suggested in single studies (steinberg2023narrativereviewof pages 7-8, steinberg2023narrativereviewof pages 5-6, schiweck2026systematicliteraturereview pages 1-2) |
| Pharmacological | Fludrocortisone | Mineralocorticoid promoting sodium/water retention and volume expansion | Expert consensus | Commonly used in hypovolemic presentations; evidence base remains limited (steinberg2023narrativereviewof pages 6-7, qu2024navigatingcomplexityin pages 10-12) |
| Pharmacological | Pyridostigmine | Acetylcholinesterase inhibitor; enhances parasympathetic/cholinergic tone | Limited RCT | Can improve fatigue/hemodynamics in selected patients; evidence from limited studies (steinberg2023narrativereviewof pages 7-8, steinberg2023narrativereviewof pages 6-7, schiweck2026systematicliteraturereview pages 1-2) |
| Immunotherapy | IVIG | Immunomodulation; may reduce pathogenic autoantibody effects | Case series/RCT | Considered for autoimmune-mediated refractory POTS; case series positive, but small RCT showed no clear advantage over albumin in one study (pena2024autoimmunityinsyndromes pages 8-9, blitshteyn2025immunotherapiesforpostural pages 5-7) |
| Immunotherapy | Plasmapheresis | Removes circulating autoantibodies and immune mediators | Case series | Used in severe refractory cases; reported functional improvement in small series (blitshteyn2025immunotherapiesforpostural pages 5-7, pena2024autoimmunityinsyndromes pages 8-9, blitshteyn2025immunotherapiesforpostural pages 16-17) |
| Immunotherapy | Rituximab | Anti-CD20 B-cell depletion | Case reports | Very limited evidence; reported in isolated autoimmune autonomic cases including POTS-related presentations (blitshteyn2025immunotherapiesforpostural pages 5-7, blitshteyn2025immunotherapiesforpostural pages 1-2, blitshteyn2025immunotherapiesforpostural pages 17-18) |
| Immunotherapy | Corticosteroids | Anti-inflammatory and immunosuppressive effects | Case reports | Considered when autoimmune contribution is suspected; evidence remains sparse and indirect (blitshteyn2025immunotherapiesforpostural pages 1-2, blitshteyn2025immunotherapiesforpostural pages 18-19, blitshteyn2025immunotherapiesforpostural pages 15-16) |


*Table: This table summarizes current POTS management strategies across non-pharmacological, pharmacological, and immunotherapy categories. It is useful for comparing mechanisms, strength of evidence, and key clinical notes from recent literature and trial context.*

### Non-Pharmacological Approaches (First-Line)
- **Graded exercise training:** The Levine Protocol is a 3-month program starting with recumbent exercises (rowing, swimming, recumbent cycling) before progressing to upright activities. Combined endurance and resistance training has shown 53–71% of patients no longer meeting diagnostic criteria (roy2025autonomicdysfunctionin pages 7-10, steinberg2023narrativereviewof pages 6-7). *MAXO:0001001 (exercise therapy)*
- **Salt and fluid intake:** 8–12 g sodium/day and 2–3 L fluid daily recommended for all patients (steinberg2023narrativereviewof pages 6-7, mallick2023covid19inducedpostural pages 5-6). *MAXO:0000127 (dietary modification)*
- **Compression garments:** 20–30 mmHg thigh-high stockings or abdominal binders to reduce venous pooling (steinberg2023narrativereviewof pages 7-8, steinberg2023narrativereviewof pages 5-6). *MAXO:0000588 (compression therapy)*
- **Transcutaneous vagus nerve stimulation (tVNS):** Emerging therapy that restores sympathovagal balance and exerts immunomodulatory effects (chakraborty2023noninvasivevagusnerve pages 2-3, schiweck2026systematicliteraturereview pages 1-2)

### Pharmacological Treatments
- **Ivabradine:** Selective If-channel blocker in sinoatrial node pacemaker cells; reduces heart rate without affecting blood pressure or myocardial contractivity. Phase 3 trial completed (NCT03182725, 37 participants). Effectively reduces HR and alleviates symptoms (qu2024navigatingcomplexityin pages 10-12, schiweck2026systematicliteraturereview pages 1-2). *MAXO:0000058 (pharmacotherapy)*
- **Beta-blockers** (propranolol, bisoprolol, metoprolol): Heart rate reduction and sympatholytic effects (steinberg2023narrativereviewof pages 5-6, schiweck2026systematicliteraturereview pages 1-2)
- **Midodrine:** α1-adrenergic agonist for peripheral vasoconstriction (steinberg2023narrativereviewof pages 7-8, schiweck2026systematicliteraturereview pages 1-2)
- **Fludrocortisone:** Mineralocorticoid for blood volume expansion in hypovolemic subtype (steinberg2023narrativereviewof pages 6-7, qu2024navigatingcomplexityin pages 10-12)
- **Pyridostigmine:** Acetylcholinesterase inhibitor enhancing parasympathetic tone (steinberg2023narrativereviewof pages 7-8, schiweck2026systematicliteraturereview pages 1-2)

### Immunotherapy (Emerging)
For severe, refractory POTS with autoimmune features:
- **IVIG/SCIG:** Case series show improvement in orthostatic symptoms, fatigue, and autoantibody titers (blitshteyn2025immunotherapiesforpostural pages 5-7, pena2024autoimmunityinsyndromes pages 8-9). However, one small RCT showed no significant advantage over albumin, though study limitations may have affected results (blitshteyn2025immunotherapiesforpostural pages 5-7). Phase 3 trial of IgPro20 (NCT06524739) was terminated (blitshteyn2025immunotherapiesforpostural pages 17-18). *MAXO:0000780 (immunotherapy)*
- **Plasmapheresis:** Reported to improve function in severe cases, allowing return to daily activities (blitshteyn2025immunotherapiesforpostural pages 5-7, pena2024autoimmunityinsyndromes pages 8-9)
- **Rituximab:** Case reports of autonomic symptomatic resolution with decreased autoantibodies (blitshteyn2025immunotherapiesforpostural pages 5-7)
- At least 3–6 months of treatment may be needed for full effects (blitshteyn2025immunotherapiesforpostural pages 16-17)

### Active Clinical Trials
Multiple trials are currently recruiting, including:
- **NCT04186286:** Crossover study of propranolol vs. ivabradine (Phase 2, University of Calgary)
- **NCT05924646:** Calgary Salt for POTS trial
- **NCT04881318:** Compression garments in community POTS
- **NCT05554107:** Physical activity effects (Lund University, n=200)
- **NCT06292104:** Phenotyping study (UT Southwestern, n=350)
- **NCT07197905:** Restoring iron deficiency in POTS (Vanderbilt, Phase 2)
- **NCT02673996:** POTS adrenergic autoantibody study (University of Calgary)

---

## 13. Prevention

### Primary Prevention
No established primary prevention exists for POTS. However, strategies to reduce risk include:
- Maintaining physical fitness and avoiding prolonged deconditioning
- Adequate hydration and salt intake
- COVID-19 vaccination may reduce post-COVID POTS risk, though POTS has also been reported rarely after vaccination (pena2024autoimmunityinsyndromes pages 6-8)

### Secondary Prevention
- Early recognition and diagnosis of autonomic dysfunction symptoms
- Prompt initiation of non-pharmacological interventions
- Screening for POTS in long COVID populations, where autonomic testing should be routinely undertaken (mouslmani2025characterizationofpostural pages 9-10)

### Tertiary Prevention
- Structured exercise programs to prevent deconditioning
- Ongoing compression therapy and lifestyle modifications
- Treatment of comorbid conditions (EDS, MCAS, SFN)

---

## 14. Associated Conditions and Comorbidities

POTS frequently co-occurs with several conditions (blitshteyn2026posturalorthostatictachycardia pages 2-4, steinberg2023narrativereviewof pages 2-3, steinberg2023narrativereviewof pages 3-4):

- **Hypermobile Ehlers-Danlos Syndrome (hEDS):** Prevalence up to 50% in hEDS patients; connective tissue abnormalities may affect vasculature (steinberg2023narrativereviewof pages 3-4)
- **Mast Cell Activation Syndrome (MCAS):** Frequency ranges from 2% to 87% depending on diagnostic criteria used (steinberg2023narrativereviewof pages 2-3, steinberg2023narrativereviewof pages 3-4)
- **Myalgic Encephalomyelitis/Chronic Fatigue Syndrome (ME/CFS):** 11–25% prevalence of POTS in ME/CFS; significant symptom overlap (schiweck2026systematicliteraturereview pages 1-2, steinberg2023narrativereviewof pages 3-4)
- **Small Fiber Neuropathy:** Present in up to 50% of POTS patients (mallick2023covid19inducedpostural pages 2-4)
- **Migraine** (with and without aura) (blitshteyn2026posturalorthostatictachycardia pages 2-4)
- **Autoimmune disorders** including Hashimoto's thyroiditis, rheumatoid arthritis, Sjögren's syndrome (qu2024navigatingcomplexityin pages 3-5, blitshteyn2026posturalorthostatictachycardia pages 2-4)

---

## 15. Model Organisms

Animal models for POTS are limited, reflecting the complex multifactorial nature of the disorder. Experimental approaches include:

- **Passive transfer models:** Serum immunoglobulin from POTS patients is transferred to rodents to assess whether autoantibodies reproduce the POTS phenotype, consistent with the approach used for other symptom-based autoimmune disorders (johansson2022plasmaproteomicprofiling pages 6-7)
- **TSP-4 deficient mice:** Thrombospondin-4 (TSP-4) deficient mouse models have been used to study vascular proteomic changes relevant to POTS (johansson2022plasmaproteomicprofiling pages 6-7)
- Brain biopsy studies in existing animal models for ME/CFS and POTS are needed to determine neuroinflammatory mechanisms (blitshteyn2026posturalorthostatictachycardiaa pages 2-4)

The limited availability of validated animal models represents a significant gap in POTS research, necessitating development of more representative preclinical systems.

---

## Summary

POTS is a complex, heterogeneous autonomic disorder whose understanding has advanced considerably in recent years, driven in part by the COVID-19 pandemic. Key developments include: the recognition of autoimmune mechanisms involving GPCR autoantibodies, plasma proteomic profiling revealing hypercoagulable and proinflammatory states, and the identification of post-COVID-19 as a major trigger. Treatment remains primarily symptomatic, with exercise training, salt/fluid supplementation, and pharmacotherapy (ivabradine, beta-blockers, midodrine) forming the cornerstone, while immunotherapy shows promise for autoimmune-mediated cases. Large randomized controlled trials are urgently needed to establish evidence-based treatment algorithms and to better define the long-term prognosis of this debilitating condition (schiweck2026systematicliteraturereview pages 1-2, blitshteyn2025immunotherapiesforpostural pages 15-16).

References

1. (schiweck2026systematicliteraturereview pages 1-2): Nicole Schiweck, Katharina Langer, Andrea Maier, Daniel Vilser, and Juliane Spiegler. Systematic literature review: treatment of postural orthostatic tachycardia syndrome (pots). Clinical Autonomic Research, 36:3-16, Nov 2026. URL: https://doi.org/10.1007/s10286-025-01172-2, doi:10.1007/s10286-025-01172-2. This article has 6 citations and is from a peer-reviewed journal.

2. (roy2025autonomicdysfunctionin pages 1-4): George P. Roy, Lakshmi Sruthi Chunduri, Janhavi Rajesh Kudale, Mahdi Hassan Bin Mahmud Khan, and Maneesha Manu. Autonomic dysfunction in postural orthostatic tachycardia syndrome (pots): a neurocardiological perspective. JUNIOR RESEARCHERS, Aug 2025. URL: https://doi.org/10.52340/jr.2025.03.03.15, doi:10.52340/jr.2025.03.03.15. This article has 0 citations.

3. (blitshteyn2026posturalorthostatictachycardia pages 2-4): Svetlana Blitshteyn. Postural orthostatic tachycardia syndrome, menopause and hormone replacement therapy: clinical decisions in times of uncertainty. Journal of Clinical Medicine, 15:1477, Feb 2026. URL: https://doi.org/10.3390/jcm15041477, doi:10.3390/jcm15041477. This article has 0 citations.

4. (johansson2022plasmaproteomicprofiling pages 1-2): Madeleine Johansson, Hong Yan, Charlotte Welinder, Ákos Végvári, Viktor Hamrefors, Magnus Bäck, Richard Sutton, and Artur Fedorowski. Plasma proteomic profiling in postural orthostatic tachycardia syndrome (pots) reveals new disease pathways. Scientific Reports, Nov 2022. URL: https://doi.org/10.1038/s41598-022-24729-x, doi:10.1038/s41598-022-24729-x. This article has 26 citations and is from a peer-reviewed journal.

5. (mallick2023covid19inducedpostural pages 2-4): Deobrat Mallick, Lokesh Goyal, Prabal Chourasia, Miana R Zapata, Kanica Yashi, and Salim Surani. Covid-19 induced postural orthostatic tachycardia syndrome (pots): a review. Cureus, Mar 2023. URL: https://doi.org/10.7759/cureus.36955, doi:10.7759/cureus.36955. This article has 89 citations.

6. (mallick2023covid19inducedpostural pages 1-2): Deobrat Mallick, Lokesh Goyal, Prabal Chourasia, Miana R Zapata, Kanica Yashi, and Salim Surani. Covid-19 induced postural orthostatic tachycardia syndrome (pots): a review. Cureus, Mar 2023. URL: https://doi.org/10.7759/cureus.36955, doi:10.7759/cureus.36955. This article has 89 citations.

7. (OpenTargets Search: postural orthostatic tachycardia syndrome): Open Targets Query (postural orthostatic tachycardia syndrome, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

8. (wu2024anoverviewof pages 2-3): William Wu and Vincent Ho. An overview of ehlers danlos syndrome and the link between postural orthostatic tachycardia syndrome and gastrointestinal symptoms with a focus on gastroparesis. Frontiers in Neurology, Aug 2024. URL: https://doi.org/10.3389/fneur.2024.1379646, doi:10.3389/fneur.2024.1379646. This article has 17 citations and is from a peer-reviewed journal.

9. (steinberg2023narrativereviewof pages 2-3): Rebecca S. Steinberg, Weston Dicken, and Alexis Cutchins. Narrative review of postural orthostatic tachycardia syndrome: associated conditions and management strategies. US Cardiology Review, Sep 2023. URL: https://doi.org/10.15420/usc.2022.35, doi:10.15420/usc.2022.35. This article has 11 citations.

10. (qu2024navigatingcomplexityin pages 5-7): Hui-Qi Qu and Hakon Hakonarson. Navigating complexity in postural orthostatic tachycardia syndrome. Biomedicines, 12:1911, Aug 2024. URL: https://doi.org/10.3390/biomedicines12081911, doi:10.3390/biomedicines12081911. This article has 7 citations.

11. (qu2024navigatingcomplexityin pages 3-5): Hui-Qi Qu and Hakon Hakonarson. Navigating complexity in postural orthostatic tachycardia syndrome. Biomedicines, 12:1911, Aug 2024. URL: https://doi.org/10.3390/biomedicines12081911, doi:10.3390/biomedicines12081911. This article has 7 citations.

12. (steinberg2023narrativereviewof pages 1-2): Rebecca S. Steinberg, Weston Dicken, and Alexis Cutchins. Narrative review of postural orthostatic tachycardia syndrome: associated conditions and management strategies. US Cardiology Review, Sep 2023. URL: https://doi.org/10.15420/usc.2022.35, doi:10.15420/usc.2022.35. This article has 11 citations.

13. (qu2024navigatingcomplexityin pages 9-10): Hui-Qi Qu and Hakon Hakonarson. Navigating complexity in postural orthostatic tachycardia syndrome. Biomedicines, 12:1911, Aug 2024. URL: https://doi.org/10.3390/biomedicines12081911, doi:10.3390/biomedicines12081911. This article has 7 citations.

14. (qu2024navigatingcomplexityin pages 2-3): Hui-Qi Qu and Hakon Hakonarson. Navigating complexity in postural orthostatic tachycardia syndrome. Biomedicines, 12:1911, Aug 2024. URL: https://doi.org/10.3390/biomedicines12081911, doi:10.3390/biomedicines12081911. This article has 7 citations.

15. (pena2024autoimmunityinsyndromes pages 6-8): Clarissa Pena, Abdelmoniem Moustafa, Abdel-Rhman Mohamed, and Blair Grubb. Autoimmunity in syndromes of orthostatic intolerance: an updated review. Journal of Personalized Medicine, 14:435, Apr 2024. URL: https://doi.org/10.3390/jpm14040435, doi:10.3390/jpm14040435. This article has 13 citations.

16. (elrhermoul2023autoimmunityinlong pages 2-3): Fatema-Zahra El-Rhermoul, Artur Fedorowski, Philip Eardley, Patricia Taraborrelli, Dimitrios Panagopoulos, Richard Sutton, Phang Boon Lim, and Melanie Dani. Autoimmunity in long covid and pots. Oxford Open Immunology, Mar 2023. URL: https://doi.org/10.1093/oxfimm/iqad002, doi:10.1093/oxfimm/iqad002. This article has 64 citations.

17. (mallick2023covid19inducedpostural pages 4-5): Deobrat Mallick, Lokesh Goyal, Prabal Chourasia, Miana R Zapata, Kanica Yashi, and Salim Surani. Covid-19 induced postural orthostatic tachycardia syndrome (pots): a review. Cureus, Mar 2023. URL: https://doi.org/10.7759/cureus.36955, doi:10.7759/cureus.36955. This article has 89 citations.

18. (roy2025autonomicdysfunctionin pages 10-12): George P. Roy, Lakshmi Sruthi Chunduri, Janhavi Rajesh Kudale, Mahdi Hassan Bin Mahmud Khan, and Maneesha Manu. Autonomic dysfunction in postural orthostatic tachycardia syndrome (pots): a neurocardiological perspective. JUNIOR RESEARCHERS, Aug 2025. URL: https://doi.org/10.52340/jr.2025.03.03.15, doi:10.52340/jr.2025.03.03.15. This article has 0 citations.

19. (wei2025pathophysiologicalmechanismsof pages 1-2): Liuchuang Wei, Heming Cheng, Suihai Chen, Jifeng Dai, Gen Li, Dongfang Ding, Xue Zhang, Ke Zhang, Jianyun Li, and Jie Hou. Pathophysiological mechanisms of postural orthostatic tachycardia syndrome analyzed by means of hemodynamics. PLOS One, 20:e0327236, Jul 2025. URL: https://doi.org/10.1371/journal.pone.0327236, doi:10.1371/journal.pone.0327236. This article has 1 citations and is from a peer-reviewed journal.

20. (pena2024autoimmunityinsyndromes pages 8-9): Clarissa Pena, Abdelmoniem Moustafa, Abdel-Rhman Mohamed, and Blair Grubb. Autoimmunity in syndromes of orthostatic intolerance: an updated review. Journal of Personalized Medicine, 14:435, Apr 2024. URL: https://doi.org/10.3390/jpm14040435, doi:10.3390/jpm14040435. This article has 13 citations.

21. (chakraborty2023noninvasivevagusnerve pages 2-3): Praloy Chakraborty, Kassem Farhat, Lynsie Morris, Seabrook Whyte, Xichun Yu, and Stavros Stavrakis. Non-invasive vagus nerve simulation in postural orthostatic tachycardia syndrome. Arrhythmia & Electrophysiology Review, Dec 2023. URL: https://doi.org/10.15420/aer.2023.20, doi:10.15420/aer.2023.20. This article has 18 citations and is from a peer-reviewed journal.

22. (johansson2022plasmaproteomicprofiling pages 6-7): Madeleine Johansson, Hong Yan, Charlotte Welinder, Ákos Végvári, Viktor Hamrefors, Magnus Bäck, Richard Sutton, and Artur Fedorowski. Plasma proteomic profiling in postural orthostatic tachycardia syndrome (pots) reveals new disease pathways. Scientific Reports, Nov 2022. URL: https://doi.org/10.1038/s41598-022-24729-x, doi:10.1038/s41598-022-24729-x. This article has 26 citations and is from a peer-reviewed journal.

23. (blitshteyn2026posturalorthostatictachycardiaa pages 2-4): Svetlana Blitshteyn, Taylor Doherty, and Lawrence Steinman. Postural orthostatic tachycardia syndrome, myalgic encephalomyelitis/chronic fatigue syndrome and long covid as neuroimmune disorders. ImmunoTargets and Therapy, Volume 15:1-10, Feb 2026. URL: https://doi.org/10.2147/itt.s581262, doi:10.2147/itt.s581262. This article has 5 citations.

24. (johansson2022plasmaproteomicprofiling pages 3-5): Madeleine Johansson, Hong Yan, Charlotte Welinder, Ákos Végvári, Viktor Hamrefors, Magnus Bäck, Richard Sutton, and Artur Fedorowski. Plasma proteomic profiling in postural orthostatic tachycardia syndrome (pots) reveals new disease pathways. Scientific Reports, Nov 2022. URL: https://doi.org/10.1038/s41598-022-24729-x, doi:10.1038/s41598-022-24729-x. This article has 26 citations and is from a peer-reviewed journal.

25. (johansson2022plasmaproteomicprofiling pages 5-6): Madeleine Johansson, Hong Yan, Charlotte Welinder, Ákos Végvári, Viktor Hamrefors, Magnus Bäck, Richard Sutton, and Artur Fedorowski. Plasma proteomic profiling in postural orthostatic tachycardia syndrome (pots) reveals new disease pathways. Scientific Reports, Nov 2022. URL: https://doi.org/10.1038/s41598-022-24729-x, doi:10.1038/s41598-022-24729-x. This article has 26 citations and is from a peer-reviewed journal.

26. (johansson2022plasmaproteomicprofiling pages 7-8): Madeleine Johansson, Hong Yan, Charlotte Welinder, Ákos Végvári, Viktor Hamrefors, Magnus Bäck, Richard Sutton, and Artur Fedorowski. Plasma proteomic profiling in postural orthostatic tachycardia syndrome (pots) reveals new disease pathways. Scientific Reports, Nov 2022. URL: https://doi.org/10.1038/s41598-022-24729-x, doi:10.1038/s41598-022-24729-x. This article has 26 citations and is from a peer-reviewed journal.

27. (bragee2026proteomicsignaturesin pages 1-7): Björn Bragée, Peng Li, Danielle Meadows, Anna Widgren, Per Sjögren, Per Hamid Ghatan, Bo C. Bertilson, Wenzhong Xiao, and Jonas Bergquist. Proteomic signatures in cerebrospinal fluid and their clinical associations in patients with me/cfs. Scientific Reports, Apr 2026. URL: https://doi.org/10.1038/s41598-026-46965-1, doi:10.1038/s41598-026-46965-1. This article has 0 citations and is from a peer-reviewed journal.

28. (steinberg2023narrativereviewof pages 3-4): Rebecca S. Steinberg, Weston Dicken, and Alexis Cutchins. Narrative review of postural orthostatic tachycardia syndrome: associated conditions and management strategies. US Cardiology Review, Sep 2023. URL: https://doi.org/10.15420/usc.2022.35, doi:10.15420/usc.2022.35. This article has 11 citations.

29. (roy2025autonomicdysfunctionin pages 7-10): George P. Roy, Lakshmi Sruthi Chunduri, Janhavi Rajesh Kudale, Mahdi Hassan Bin Mahmud Khan, and Maneesha Manu. Autonomic dysfunction in postural orthostatic tachycardia syndrome (pots): a neurocardiological perspective. JUNIOR RESEARCHERS, Aug 2025. URL: https://doi.org/10.52340/jr.2025.03.03.15, doi:10.52340/jr.2025.03.03.15. This article has 0 citations.

30. (mouslmani2025characterizationofpostural pages 9-10): Mohammad AL Mouslmani, Mitsuaki Sawano, Adith S. Arun, Yilun Wu, Rishi M. Shah, Shayaan Kaleem, Tianna Zhou, Karthik Murugiah, Yuan Lu, Jeph Herrin, Pamela Bishop, Pam Taub, Aldo J. Peixoto, Bornali Bhattacharjee, Akiko Iwasaki, and Harlan M. Krumholz. Characterization of postural orthostatic tachycardia syndrome in long covid. JACC: Advances, 4(8):101873, Aug 2025. URL: https://doi.org/10.1016/j.jacadv.2025.101873, doi:10.1016/j.jacadv.2025.101873. This article has 7 citations.

31. (steinberg2023narrativereviewof pages 6-7): Rebecca S. Steinberg, Weston Dicken, and Alexis Cutchins. Narrative review of postural orthostatic tachycardia syndrome: associated conditions and management strategies. US Cardiology Review, Sep 2023. URL: https://doi.org/10.15420/usc.2022.35, doi:10.15420/usc.2022.35. This article has 11 citations.

32. (mallick2023covid19inducedpostural pages 5-6): Deobrat Mallick, Lokesh Goyal, Prabal Chourasia, Miana R Zapata, Kanica Yashi, and Salim Surani. Covid-19 induced postural orthostatic tachycardia syndrome (pots): a review. Cureus, Mar 2023. URL: https://doi.org/10.7759/cureus.36955, doi:10.7759/cureus.36955. This article has 89 citations.

33. (steinberg2023narrativereviewof pages 5-6): Rebecca S. Steinberg, Weston Dicken, and Alexis Cutchins. Narrative review of postural orthostatic tachycardia syndrome: associated conditions and management strategies. US Cardiology Review, Sep 2023. URL: https://doi.org/10.15420/usc.2022.35, doi:10.15420/usc.2022.35. This article has 11 citations.

34. (steinberg2023narrativereviewof pages 7-8): Rebecca S. Steinberg, Weston Dicken, and Alexis Cutchins. Narrative review of postural orthostatic tachycardia syndrome: associated conditions and management strategies. US Cardiology Review, Sep 2023. URL: https://doi.org/10.15420/usc.2022.35, doi:10.15420/usc.2022.35. This article has 11 citations.

35. (qu2024navigatingcomplexityin pages 10-12): Hui-Qi Qu and Hakon Hakonarson. Navigating complexity in postural orthostatic tachycardia syndrome. Biomedicines, 12:1911, Aug 2024. URL: https://doi.org/10.3390/biomedicines12081911, doi:10.3390/biomedicines12081911. This article has 7 citations.

36. (blitshteyn2025immunotherapiesforpostural pages 5-7): Svetlana Blitshteyn, Gabriela Funez-dePagnier, Anna Szombathy, and Meagan Hutchinson. Immunotherapies for postural orthostatic tachycardia syndrome, other common autonomic disorders, and long covid: current state and future direction. Frontiers in Cellular and Infection Microbiology, Sep 2025. URL: https://doi.org/10.3389/fcimb.2025.1647203, doi:10.3389/fcimb.2025.1647203. This article has 11 citations.

37. (blitshteyn2025immunotherapiesforpostural pages 16-17): Svetlana Blitshteyn, Gabriela Funez-dePagnier, Anna Szombathy, and Meagan Hutchinson. Immunotherapies for postural orthostatic tachycardia syndrome, other common autonomic disorders, and long covid: current state and future direction. Frontiers in Cellular and Infection Microbiology, Sep 2025. URL: https://doi.org/10.3389/fcimb.2025.1647203, doi:10.3389/fcimb.2025.1647203. This article has 11 citations.

38. (blitshteyn2025immunotherapiesforpostural pages 1-2): Svetlana Blitshteyn, Gabriela Funez-dePagnier, Anna Szombathy, and Meagan Hutchinson. Immunotherapies for postural orthostatic tachycardia syndrome, other common autonomic disorders, and long covid: current state and future direction. Frontiers in Cellular and Infection Microbiology, Sep 2025. URL: https://doi.org/10.3389/fcimb.2025.1647203, doi:10.3389/fcimb.2025.1647203. This article has 11 citations.

39. (blitshteyn2025immunotherapiesforpostural pages 17-18): Svetlana Blitshteyn, Gabriela Funez-dePagnier, Anna Szombathy, and Meagan Hutchinson. Immunotherapies for postural orthostatic tachycardia syndrome, other common autonomic disorders, and long covid: current state and future direction. Frontiers in Cellular and Infection Microbiology, Sep 2025. URL: https://doi.org/10.3389/fcimb.2025.1647203, doi:10.3389/fcimb.2025.1647203. This article has 11 citations.

40. (blitshteyn2025immunotherapiesforpostural pages 18-19): Svetlana Blitshteyn, Gabriela Funez-dePagnier, Anna Szombathy, and Meagan Hutchinson. Immunotherapies for postural orthostatic tachycardia syndrome, other common autonomic disorders, and long covid: current state and future direction. Frontiers in Cellular and Infection Microbiology, Sep 2025. URL: https://doi.org/10.3389/fcimb.2025.1647203, doi:10.3389/fcimb.2025.1647203. This article has 11 citations.

41. (blitshteyn2025immunotherapiesforpostural pages 15-16): Svetlana Blitshteyn, Gabriela Funez-dePagnier, Anna Szombathy, and Meagan Hutchinson. Immunotherapies for postural orthostatic tachycardia syndrome, other common autonomic disorders, and long covid: current state and future direction. Frontiers in Cellular and Infection Microbiology, Sep 2025. URL: https://doi.org/10.3389/fcimb.2025.1647203, doi:10.3389/fcimb.2025.1647203. This article has 11 citations.

## Artifacts

- [Edison artifact artifact-00](Postural_Orthostatic_Tachycardia_Syndrome-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Postural_Orthostatic_Tachycardia_Syndrome-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Postural_Orthostatic_Tachycardia_Syndrome-deep-research-falcon_artifacts/artifact-02.md)