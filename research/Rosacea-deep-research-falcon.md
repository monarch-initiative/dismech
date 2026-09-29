---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-06T16:28:41.924781'
end_time: '2026-09-06T16:43:26.728544'
duration_seconds: 884.8
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Rosacea
  mondo_id: MONDO:0006604
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 30
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 27
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0006604
    reported_labels:
    - if available
    ontology_label: rosacea
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Rosacea-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Rosacea
- **MONDO ID:** MONDO:0006604 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Rosacea** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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
- **Disease Name:** Rosacea
- **MONDO ID:** MONDO:0006604 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Rosacea** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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


# Rosacea (MONDO:0006604): comprehensive disease-characteristics report

## Executive summary

Rosacea is a common, chronic, relapsing inflammatory disorder centered on the face and sometimes the eyes. Current expert practice treats it as a **phenotype spectrum**, not four mutually exclusive subtypes. The best-supported biological model is multifactorial: polygenic susceptibility and barrier vulnerability interact with ultraviolet radiation, heat, stress, dietary vasodilators, and cutaneous microbes; these inputs amplify innate immunity, neurovascular signaling, and tissue remodeling. No single causal gene, pathogenic Mendelian variant, validated molecular diagnostic test, or cure is established. A 2024 review estimates global prevalence at **5.46%**; onset is usually in middle-to-late adulthood, although any adult age and occasionally childhood can be affected. (nguyen2024rosaceapracticalguidance pages 1-3)

The most important recent advance is a 2024 single-cell atlas of 131,243 facial-skin cells from nine women with rosacea and three controls. It implicated inflammatory fibroblasts, IFNγ-associated keratinocytes, endothelial and mural cells, Schwann cells, macrophage/dendritic cells, and type 1/17 and tissue-resident-memory T cells; fibroblast depletion or **PTGDS** knockdown and IFNγ blockade improved disease-like changes in mice. These findings expand the older keratinocyte–TLR2–KLK5–LL-37 model into a multicellular neuroimmune–vascular circuit. (chen2024singlecelltranscriptomicsreveals pages 1-2)

| Domain | Knowledge-Base Assertion | Suggested Ontology Terms/IDs | Evidence Type | Principal Source/Date/DOI | Limitations |
|---|---|---|---|---|---|
| **Definition & Epidemiology** | Chronic inflammatory skin disorder primarily of the centrofacial/periocular regions. Estimated global prevalence ~5.46%, with slight female predominance. | MONDO:0006604 (rosacea); UBERON:0001456 (skin of face); HP:0002716 (Erythema) | Clinical Review | Nguyen et al., Jan 2024, 10.2147/CCID.S391705 (nguyen2024rosaceapracticalguidance pages 1-3); Galluccio et al., Jan 2024, 10.3390/cosmetics11010011 (galluccio2024advancesinthe pages 1-2) | Global prevalence estimates vary highly by population and diagnostic criteria. |
| **Phenotypes & Diagnosis** | Diagnosis requires fixed centrofacial erythema or phymatous changes OR 2+ major features (papules, pustules, flushing, telangiectasia, ocular signs). Transitions away from historic subtypes. | HP:0010783 (Erythema); HP:0200034 (Papule); HP:0200039 (Pustule); HP:0001009 (Telangiectasia); HP:0012737 (Blepharoconjunctivitis) | Consensus Guidelines; Systematic Review | Tan et al., Feb 2017, 10.1111/bjd.15122 (tan2017updatingthediagnosis pages 9-11); van Zuuren et al., Mar 2019, 10.1111/bjd.17590 (zuuren2019interventionsforrosacea pages 1-2) | Ocular diagnostic combinations rely on limited ophthalmologist consensus. |
| **Genetics (Susceptibility)** | Polygenic trait lacking monogenic causation. Genome-wide significant loci linked to immune/inflammatory and pigmentation pathways (HLA, IL13, IRF4, HERC2-OCA2, SLC45A2). | GO:0006955 (immune response); GO:0043473 (pigmentation) | Human GWAS (73,265 European ancestry subjects) | Aponte et al., May 2018, 10.1093/hmg/ddy184 (aponte2018assessmentofrosacea pages 7-8) | Primarily European ancestry cohorts; phenotype based on self-reported symptom questionnaires. |
| **Etiology (Triggers)** | Amplified innate immune and neurovascular responses triggered by UV, heat, stress, diet, and microbiota (Demodex folliculorum density is 5-7x higher in lesions). | NCIT:C16259 (Demodex); GO:0045087 (innate immune response); GO:0050954 (sensory perception of mechanical stimulus) | Narrative Review | Galluccio et al., Jan 2024, 10.3390/cosmetics11010011 (galluccio2024advancesinthe pages 2-4) | Difficult to distinguish primary triggers from opportunistic overgrowth (e.g., Demodex). |
| **Pathophysiology (Cellular)** | ScRNA-seq reveals expansion of pro-inflammatory fibroblasts (primary source of inflammatory/vasodilatory signals), Schwann cells, endothelial cells, and macrophages. Mast cells also increased. | CL:0000057 (fibroblast); CL:0000097 (mast cell); CL:0000235 (macrophage); CL:0002573 (Schwann cell) | scRNA-seq (9 cases, 3 controls); Mouse validation | Chen et al., Oct 2024, 10.1038/s41467-024-52946-7 (chen2024singlecelltranscriptomicsreveals pages 1-2) | Small human sample size, all female, inherent compositional biases in skin digestion. |
| **Pathophysiology (Molecular)** | Primary causal chain: TLR2 activation -> KLK5 induction -> cleavage of cathelicidin to LL-37 -> activation of PAR2, NF-kB, NLRP3 inflammasome, and angiogenesis. | GO:0002224 (toll-like receptor signaling); GO:0001525 (angiogenesis); GO:0032640 (tumor necrosis factor production) | Clinical Reviews | Nguyen et al., Jan 2024, 10.2147/CCID.S391705 (nguyen2024rosaceapracticalguidance pages 1-3); Shi et al., Jun 2026, 10.2147/dddt.s608151 (shi2026neurohormonalimmunedysregulationin pages 2-4) | Highly complex feedback loops blur upstream vs. downstream ordering. |
| **Treatments** | Phenotype-targeted approaches: Brimonidine (erythema); ivermectin, azelaic acid (papules/pustules); doxycycline 40mg MR, isotretinoin (systemic); laser/IPL (telangiectasia). | NCIT:C61702 (Brimonidine); NCIT:C616 (Azelaic Acid); NCIT:C61868 (Ivermectin); NCIT:C480 (Doxycycline) | Systematic Review (152 RCTs, 20,944 subjects) | van Zuuren et al., Mar 2019, 10.1111/bjd.17590 (zuuren2019interventionsforrosacea pages 1-2) | Few long-term or head-to-head active comparator trials available. |
| **Experimental Models** | Subcutaneous LL-37 injection in mice induces rosacea-like lesions (erythema, inflammation, collagen hyperplasia). Demodex-induced rabbit models also utilized. | NCIT:C14251 (Mouse); NCIT:C14264 (Rabbit); HP:0000974 (Hyperextensible skin - surrogate for collagen abnormalities) | Animal experimental models | Zhang et al., Mar 2023, 10.3390/cimb45040177 (zhang2023longtermadministrationof pages 13-14) | Induced models mimic late-stage effector pathways, not spontaneous natural disease initiation. |


*Table: A structured overview of rosacea phenotypes, genetics, mechanisms, treatments, and models mapped to ontology concepts, designed for knowledge base integration.*

**Ontology caution:** mappings below are suggestions for curation. Exact HPO/GO/CL/UBERON/NCIT identifiers should be checked against the current ontology release; rosacea-specific concepts are not always represented by exact HPO terms.

---

## 1. Disease information

### Definition and names

Rosacea is a chronic inflammatory dermatosis primarily affecting the **centrofacial and periocular regions**, characterized in varying combinations by transient flushing, persistent erythema, telangiectasia, inflammatory papules/pustules, phymatous tissue overgrowth, and ocular inflammation. Signs fluctuate and may coexist; therefore, the current ROSCO/National Rosacea Society framework documents individual phenotypes rather than forcing each patient into one subtype. (tan2017updatingthediagnosis pages 9-11, galluccio2024advancesinthe pages 1-2, tan2018applyingthephenotype pages 5-10)

Common names include **rosacea**, **acne rosacea** (older and potentially misleading because comedones are absent), **couperose**, and phenotype labels such as erythematotelangiectatic, papulopustular, phymatous rosacea/rhinophyma, and ocular rosacea.

### Identifiers

- **MONDO:** MONDO:0006604.
- **ICD-10-CM:** L71 (rosacea); L71.0 perioral dermatitis, L71.1 rhinophyma, L71.8 other rosacea, L71.9 unspecified rosacea. Perioral dermatitis is coded in the same family but is clinically distinct.
- **ICD-11:** ED90.0, rosacea.
- **MeSH:** Rosacea, commonly indexed as D012393.
- **OMIM/Orphanet:** no dedicated Mendelian-disease entry is expected because ordinary rosacea is neither a monogenic nor rare disorder.

This report synthesizes **aggregated disease-level resources and published cohorts**, not identifiable patient-level EHR data. Individual studies include questionnaires, clinician-diagnosed cohorts, biopsies, and clinical trials.

---

## 2. Etiology

### Causal and susceptibility factors

Rosacea has no singular proven cause. Current understanding invokes interacting genetic, immune, neurovascular, barrier, microbial, and environmental factors. Human genetic evidence establishes susceptibility rather than deterministic causation. A GWAS of **73,265** predominantly European-ancestry participants found genome-wide signals near **IRF4, PSMB9–HLA-DMB, HERC2–OCA2, SLC45A2, IL13, NRXN3–DIO2, and OVOL1–SNX32**; a clinician-diagnosis analysis included 2,618 cases and 20,334 controls. The pigmentation and immune loci plausibly help explain the association with lighter phototypes, but ancestry and self-reported symptoms limit generalizability. (aponte2018assessmentofrosacea pages 7-8)

Other reported candidates—HLA class II alleles and rare familial variants in **LRRC4, SH3PXD2A**, and **SLC26A8**—remain susceptibility observations, not ACMG-classified causal variants. No recognized pathogenic/likely pathogenic germline variant, somatic driver, chromosomal abnormality, or Mendelian inheritance pattern defines common rosacea. (galluccio2024advancesinthe pages 2-4)

### Environmental and lifestyle risk or flare factors

Frequently reported aggravators are ultraviolet exposure, hot or cold weather, abrupt temperature change, hot drinks, spicy/capsaicin-containing food, cinnamaldehyde- or histamine-containing food, alcohol, exercise, emotional stress, and irritating cosmetics. They are better established as **flare triggers** than as causes of incident disease. Heat, capsaicin, alcohol, and stress can activate TRP/neuropeptide and vasodilatory pathways. (galluccio2024advancesinthe pages 2-4, nguyen2024rosaceapracticalguidance pages 1-3)

**Demodex folliculorum** density has been reported as approximately **five- to sevenfold higher** in rosacea biopsies, especially papulopustular and phymatous disease. Associated *Bacillus oleronius* and *Staphylococcus epidermidis* may stimulate neutrophilic inflammation. Demodex is therefore a plausible amplifier/trigger and therapeutic target, not a sufficient infectious cause: mites also inhabit normal skin, and rosacea is not classified as contagious. (galluccio2024advancesinthe pages 2-4)

### Protective factors and gene–environment interaction

No reproducible protective allele is clinically actionable. Environmental “protection” consists mainly of reducing individual triggers, daily broad-spectrum photoprotection, barrier-supportive moisturization, and gentle skin care. These reduce flares; evidence that they prevent first onset is lacking. A reasonable gene–environment model is that pigmentation/immune susceptibility loci alter UV response and inflammatory threshold, while UV, heat, microbes, and irritants push a predisposed neuroimmune–vascular system beyond that threshold. This integrated model is biologically plausible but has not been established by large prospective G×E studies. (galluccio2024advancesinthe pages 2-4, aponte2018assessmentofrosacea pages 7-8)

---

## 3. Phenotypes

| Phenotype | Type, course, frequency/severity | Suggested ontology terms |
|---|---|---|
| Persistent centrofacial erythema | Diagnostic sign; fixed but can intensify episodically; severity variable | facial erythema; HPO “Erythema”; UBERON facial skin |
| Flushing/transient erythema | Symptom/sign; episodic, trigger-associated | HPO “Flushing”/episodic erythema |
| Telangiectasia | Physical sign; often persistent and slowly progressive | HPO “Telangiectasia” |
| Papules and pustules | Inflammatory signs; episodic/relapsing; typically without comedones | HPO “Papule,” “Pustule” |
| Burning, stinging, pruritus, dryness | Subjective symptoms; fluctuating; may indicate barrier/neurosensory dysfunction | HPO “Pruritus,” “Dry skin,” pain/burning-sensation terms |
| Edema | Secondary sign; intermittent or persistent in severe disease | HPO “Facial edema” |
| Phyma, especially rhinophyma | Tissue hypertrophy/fibrosis and sebaceous enlargement; slowly progressive; more common in men | HPO “Rhinophyma” if available; tissue hypertrophy/fibrosis |
| Ocular rosacea | Dryness, foreign-body sensation, lid-margin telangiectasia, blepharitis, meibomian dysfunction, conjunctival injection; keratitis/scleritis are less common but sight-threatening | HPO “Blepharitis,” “Conjunctival injection,” “Keratitis,” “Dry eye,” “Meibomian gland dysfunction” |

Persistent erythema is the central diagnostic phenotype. Papules, pustules, flushing, telangiectasia, and ocular involvement are major features; burning, stinging, edema, and dryness are secondary features. Historic erythematotelangiectatic and papulopustular patterns are the most frequent, while phyma is less common. (nguyen2024rosaceapracticalguidance pages 1-3, galluccio2024advancesinthe pages 1-2)

Onset is usually adult, often middle-to-late adulthood. Severity ranges from mild intermittent flushing to persistent inflammation, ocular injury, or disfiguring phyma. Reliable universal percentages for each phenotype are unavailable because older studies used mutually exclusive subtypes and heterogeneous definitions; this is precisely why consensus groups recommend feature-level registries. (tan2018applyingthephenotype pages 5-10)

### Quality of life

Because manifestations are visible and often uncomfortable, rosacea can impair self-esteem, social and occupational interaction, and well-being. Consensus experts recommend routinely assessing poor self-esteem, social isolation, anxiety, depression, treatment burden, cost, and lifestyle restriction. RosaQoL is disease-specific, but it omits some features and lacks a firmly established minimal clinically important difference. (tan2017updatingthediagnosis pages 9-11, tan2018applyingthephenotype pages 5-10)

---

## 4. Genetic and molecular information

Rosacea is **complex, multifactorial, and polygenic**. There are no established causal genes with OMIM disease-gene assignments, no routine ClinVar pathogenic-variant interpretation, and no meaningful carrier frequency, penetrance, anticipation, consanguinity, founder-mutation, germline-mosaicism, or chromosomal-abnormality framework.

The principal replicated biological categories from GWAS are:

- **Immune regulation:** HLA region, **IRF4, IL13, PSMB9/HLA-DMA/B**.
- **Pigmentation/photobiology:** **HERC2/OCA2, SLC45A2, MC1R, IRF4**.
- **Less-resolved regulatory loci:** **NRXN3/DIO2** and **OVOL1/SNX32** regions. (aponte2018assessmentofrosacea pages 7-8)

Open Targets associates rosacea with MMP-family and adrenergic-receptor targets, and lists TLR1, IRF4, MC1R, ELOVL4, and SLC45A2 among disease-associated targets. These are mixed genetic, expression, and drug-mechanism associations and must not be interpreted as causal genes. (OpenTargets Search: rosacea)

No validated rosacea-specific DNA methylation, histone, chromatin, or structural-variant signature is ready for clinical curation. Epigenetic and noncoding-RNA studies remain exploratory.

---

## 5. Environmental information

- **Physical exposures:** UV radiation, heat, cold, wind, and temperature transitions can provoke vasodilation, oxidative stress, barrier injury, and inflammatory signaling.
- **Lifestyle:** alcohol, spicy or hot foods/drinks, vigorous exercise, stress, and irritating skin products are common patient-specific triggers. Smoking associations are inconsistent and should not be treated as protective.
- **Microorganisms:** increased Demodex density and associated bacterial antigens can amplify inflammation; altered cutaneous microbiota is implicated, while gut dysbiosis, small-intestinal bacterial overgrowth, and *Helicobacter pylori* remain less certain and are not accepted routine diagnostic explanations.
- **Pollution/occupation:** plausible irritant or oxidative contributors, but robust rosacea-specific causal estimates are lacking.

The appropriate knowledge-base relationship is usually “aggravates/associated with,” not “causes.” (galluccio2024advancesinthe pages 2-4, nguyen2024rosaceapracticalguidance pages 1-3)

---

## 6. Mechanism/pathophysiology

### Ordered causal chain

1. **Polygenic susceptibility plus barrier/neurovascular vulnerability leads to** a lowered threshold for facial responses to UV, thermal, chemical, emotional, and microbial stimuli; this initiating architecture is supported epidemiologically but remains incompletely demonstrated.  
2. **Triggers lead to** keratinocyte and innate-sensor activation, including increased TLR2 signaling and TRP-channel activity.  
3. **TLR2 activation leads to** NF-κB inflammatory transcription and increased kallikrein-5 (**KLK5**) activity.  
4. **KLK5 leads to** abnormal processing of hCAP18/CAMP into bioactive **LL-37** fragments and can activate PAR2.  
5. **LL-37 leads to** chemotaxis, cytokine release, NLRP3/IL-1β activity, mast-cell degranulation, MMP activation, extracellular-matrix remodeling, and angiogenic signaling.  
6. **Microbial branch:** high Demodex/*B. oleronius* burden plus LL-37 leads to bacterial-DNA–peptide complexes, which activate plasmacytoid dendritic-cell type-I interferon; downstream IL-22/endothelial signaling is proposed to cause neovascularization.  
7. **Neural branch:** heat/capsaicin/stress activation of TRPV/TRPA channels leads to substance P and CGRP release, which results in vasodilation, burning/stinging, and neurogenic inflammation.  
8. **Cellular-amplification branch:** inflammatory fibroblasts, macrophage/DCs, mast cells, type 1/17 and resident-memory T cells, IFNγ-responsive keratinocytes, Schwann cells, and activated endothelial/mural cells form reciprocal cytokine and vasodilatory loops.  
9. **These loops lead to** transient flushing and persistent erythema/telangiectasia; neutrophilic inflammation leads to papules/pustules; chronic matrix remodeling and fibrosis can result in phyma; analogous eyelid/ocular-surface inflammation results in ocular rosacea. (galluccio2024advancesinthe pages 2-4, nguyen2024rosaceapracticalguidance pages 1-3, chen2024singlecelltranscriptomicsreveals pages 1-2)

### Pathway, cellular, and profiling detail

The most established molecular axis is **TLR2–KLK5–CAMP/LL-37**, with downstream NF-κB, JAK/STAT, mTORC1, MMP9, PAR2, and NLRP3 signaling. Mast-cell-deficient mice fail to develop the full erythema, telangiectasia, and inflammation induced in conventional models, supporting—but not proving in humans—a necessary amplification role. (galluccio2024advancesinthe pages 2-4)

The 2024 single-cell study sampled **131,243 cells** from lesional and nonlesional facial skin of nine women—three each with erythematotelangiectatic, papulopustular, and phymatous disease—and three healthy women. It found a rosacea-associated CD74-high keratinocyte state, IFNγ-mediated barrier damage, proinflammatory fibroblast expansion, increased endothelial, Schwann, macrophage/DC, type 1/17, and resident-memory T-cell populations, and impaired contraction programs in vascular mural cells. Fibroblasts emerged as a major source of inflammatory and vasodilatory signals; **PTGDS** knockdown or fibroblast depletion blocked disease-like changes in mice. The small, women-only cohort and tissue-dissociation/compositional biases require replication. (chen2024singlecelltranscriptomicsreveals pages 1-2)

Integrated transcriptomic analysis identified 169 genes shared with acne and highlighted **IL1B, PTPRC, CXCL8, MMP9, CCL4, CXCL10, CD163, CCR5, CXCR4**, and **TLR8**, with increased γδ-T-cell signatures. These computational associations do not establish causality. (liang2024exploringtheassociation pages 14-15)

Suggested GO biological processes include innate immune response, TLR signaling, NF-κB signaling, inflammasome activation, cytokine production, leukocyte chemotaxis, angiogenesis, vasodilation, sensory perception of pain, extracellular-matrix organization, collagen deposition, and epidermal-barrier establishment. Suggested CL terms include keratinocyte, fibroblast, vascular endothelial cell, vascular smooth-muscle/mural cell, Schwann cell, mast cell, neutrophil, macrophage, dendritic cell/plasmacytoid DC, γδ T cell, Th1/Th17 cell, and tissue-resident-memory T cell.

---

## 7. Anatomical structures affected

The primary organ is skin, especially the **cheeks, nose, chin, forehead, glabella, and central facial/periocular skin**; distribution is commonly bilateral but not necessarily perfectly symmetric. Ocular involvement affects eyelid margins, meibomian glands, conjunctiva, tear film, and occasionally cornea/sclera. Phyma most often affects the nose (rhinophyma), but chin, forehead, ears, and eyelids may be affected. (galluccio2024advancesinthe pages 1-2, zuuren2019interventionsforrosacea pages 1-2)

Tissue/cell compartments include epidermal keratinocytes and stratum-corneum barrier; pilosebaceous follicles and sebaceous glands; dermal microvessels and perivascular tissue; dermal extracellular matrix; sensory nerves/Schwann cells; and infiltrating innate/adaptive immune cells. Relevant subcellular systems include plasma-membrane TLR/TRP receptors, cytosolic NLRP3 inflammasome, NF-κB/JAK-STAT/mTOR signaling machinery, secretory granules of mast cells, and extracellular protease/LL-37 compartments.

Suggested UBERON concepts: skin of face, cheek, nose, forehead, chin, eyelid, conjunctiva, cornea, meibomian gland, sebaceous gland, hair follicle, epidermis, dermis, and cutaneous microvasculature.

---

## 8. Temporal development

Rosacea generally begins insidiously in adulthood with intermittent flushing/sensitivity, followed variably—not inevitably—by persistent erythema, telangiectasia, inflammatory lesions, ocular disease, or tissue hypertrophy. It is chronic and relapsing, with trigger-associated exacerbations and treatment-induced remissions. The old linear “stage progression” concept is not reliable: patients may present with isolated or mixed phenotypes, and one phenotype does not necessarily evolve into another. (nguyen2024rosaceapracticalguidance pages 1-3, tan2018applyingthephenotype pages 5-10)

Early treatment can suppress symptoms and may limit inflammatory remodeling, but no validated critical period prevents lifelong disease. Long-term maintenance is often required. Ocular warning features—pain, photophobia, visual change, marked redness, or suspected keratitis—constitute a time-sensitive referral window.

---

## 9. Inheritance and population

A 2024 synthesis estimates worldwide prevalence at **5.46%**, while another contemporary review uses approximately 5%; differences reflect sampling, geography, skin phototype, and diagnostic definition. Rosacea is reported more often in Northern European/fair-skinned populations, but it occurs in every skin color and can be underrecognized when erythema is less visually apparent. (nguyen2024rosaceapracticalguidance pages 1-3, galluccio2024advancesinthe pages 1-2)

Overall sex occurrence may be approximately equal or show modest female predominance depending on setting. Women more often seek care for erythema/inflammatory disease; phymatous disease is disproportionately male. Typical onset is middle-to-late adulthood. There is no Mendelian inheritance ratio, penetrance estimate, carrier state, anticipation, or founder variant. Familial aggregation and GWAS support polygenic heritability with variable expressivity strongly modified by exposures. (nguyen2024rosaceapracticalguidance pages 1-3, galluccio2024advancesinthe pages 1-2, aponte2018assessmentofrosacea pages 7-8)

Reported incidence is much less certain than prevalence; a defensible universal cases-per-100,000/year estimate is not available from the retrieved evidence.

---

## 10. Diagnostics

### Clinical criteria

Diagnosis is clinical. Either **persistent centrofacial erythema** that periodically intensifies or **phymatous change** is independently diagnostic. Otherwise, at least two major features—papules/pustules, flushing, telangiectasia, or ocular manifestations—support diagnosis. Each feature should be graded independently and documented with patient-reported burden. (zuuren2019interventionsforrosacea pages 1-2, zuuren2019interventionsforrosacea pages 2-3)

For ocular disease, ROSCO proposed either lid-margin telangiectasia plus interpalpebral conjunctival injection, or corneal abnormality plus scleral inflammation; this recommendation had limited ophthalmologist representation and is not a substitute for eye examination. (tan2017updatingthediagnosis pages 9-11)

### Tests and pathology

There is no diagnostic blood, urine, enzyme, electrophysiologic, imaging, or genetic test. Dermoscopy can document linear vessels, follicular plugs/scales, and background erythema. Standardized skin-surface biopsy, scraping, microscopy, or PCR can quantify Demodex when demodicosis is suspected but is not mandatory for ordinary rosacea. Biopsy is reserved for atypical or treatment-refractory lesions.

Histology is nonspecific and phenotype-dependent: dilated superficial vessels, perifollicular/perivascular lymphohistiocytic infiltrates, neutrophils in papulopustular lesions, solar elastosis, Demodex in follicles, sebaceous hyperplasia, and fibrosis in phyma. Molecular classifiers—such as transcriptomic models for neurogenic rosacea—remain research tools.

### Differential diagnosis and screening

Important alternatives are acne vulgaris (comedones), seborrheic dermatitis (greasy scale), periorificial dermatitis, steroid-induced rosaceiform dermatitis, demodicosis, lupus erythematosus, dermatomyositis, allergic/irritant contact dermatitis, photodermatitis, sarcoidosis, carcinoid/mast-cell flushing disorders, and medication-induced flushing. There is no population, newborn, carrier, prenatal, or cascade-screening program.

WGS, WES, panels, single-gene testing, CMA, karyotype, FISH, mtDNA, and repeat-expansion testing have **no routine utility** for typical rosacea.

---

## 11. Outcome and prognosis

Rosacea is not ordinarily life-shortening, and disease-specific mortality or reduced survival has not been demonstrated. Its burden is morbidity: discomfort, visible disfigurement, recurrent treatment, psychosocial distress, and occasionally ocular injury. Untreated phyma may become permanently deforming; severe keratitis can threaten vision. (tan2017updatingthediagnosis pages 9-11, galluccio2024advancesinthe pages 1-2)

Control is usually achievable, but cure is not. Prognosis depends on dominant phenotype, trigger burden, adherence, barrier care, Demodex burden, ocular involvement, and access to laser/surgical treatment. Persistent erythema and telangiectasia often respond less completely to anti-inflammatory drugs than papules/pustules. No validated molecular prognostic biomarker is available.

---

## 12. Treatment and current implementation

Treatment should target each active phenotype and combine modalities when necessary. The strongest synthesis retrieved included **152 randomized studies and 20,944 participants**. It found high-certainty evidence for brimonidine for temporary persistent erythema and azelaic acid or ivermectin for papules/pustules; moderate-to-high certainty supported doxycycline 40-mg modified release and isotretinoin, while laser/light evidence for erythema/telangiectasia was low-to-moderate and omega-3 evidence for ocular disease moderate. (zuuren2019interventionsforrosacea pages 1-2)

### Phenotype-directed algorithm

- **Universal care:** gentle nonsoap cleanser, fragrance-free moisturizer/barrier repair, broad-spectrum SPF ≥30, individualized trigger diary/avoidance, camouflage cosmetics, and psychosocial assessment.
- **Papules/pustules:** topical ivermectin 1%, azelaic acid 15–20%, metronidazole 0.75–1%, or newer microencapsulated benzoyl peroxide 5%; topical minocycline foam is another option. For moderate/severe disease, use subantimicrobial doxycycline 40 mg modified release; short antimicrobial-dose tetracycline courses or low-dose isotretinoin are selected alternatives.
- **Persistent erythema:** brimonidine gel (α2-adrenergic agonist) or oxymetazoline cream (α1A agonist) provides reversible vasoconstriction. Counsel about irritation and paradoxical/rebound erythema, particularly with brimonidine.
- **Telangiectasia/fixed vascular erythema:** pulsed-dye laser, KTP laser, or intense pulsed light; multiple sessions and maintenance may be required. Risks include pain, edema, purpura, pigment change, and scarring.
- **Phyma:** ablative CO₂/Er:YAG laser, electrosurgery, dermabrasion, radiofrequency, or surgical debulking/contouring; medical therapy does not reverse established hypertrophy.
- **Ocular disease:** lid hygiene, warm compresses, preservative-free lubricants, management of meibomian dysfunction, oral doxycycline where appropriate, and omega-3 in selected patients; ophthalmology referral for corneal disease, pain, photophobia, or visual change.
- **Neurogenic/refractory burning:** evidence for gabapentinoids, antidepressants, β-blockers, botulinum toxin, or hydroxychloroquine is limited and off-label; specialist supervision is required.

Suggested NCIT intervention concepts include azelaic acid, ivermectin, metronidazole, doxycycline, minocycline, isotretinoin, brimonidine, oxymetazoline, benzoyl peroxide, laser therapy, intense-pulsed-light therapy, and surgical debulking. Exact term identifiers should be release-validated.

### Recent developments

Microencapsulated benzoyl peroxide 5% is a notable recent US approval for inflammatory lesions. Microencapsulation prolongs delivery to reduce the irritation historically associated with benzoyl peroxide; efficacy was detectable by week 2 and extension data reached 52 weeks, although comparative placement in guidelines still requires study. (galluccio2024advancesinthe pages 1-2)

Mechanism-targeted research includes IFNγ blockade, PTGDS/fibroblast targeting, mast-cell/MRGPRX2 inhibition, TRP/neuropeptide modulation, JAK/STAT and mTOR approaches, microbiome interventions, and anti-CGRP therapy. These are investigational rather than standard care. The evidence base still lacks enough long-term, head-to-head, cost-effectiveness, skin-of-color, and phyma trials. (tan2018applyingthephenotype pages 5-10, chen2024singlecelltranscriptomicsreveals pages 1-2)

No validated pharmacogenomic test, genotype-guided regimen, gene therapy, cell therapy, RNA therapy, or approved biologic immunotherapy exists.

---

## 13. Prevention

True primary prevention is unknown because etiology is multifactorial and no vaccine or prophylactic drug prevents onset. Practical prevention is predominantly secondary/tertiary:

1. identify personal triggers rather than impose universal dietary restriction;
2. use daily UV protection, shade, hats, and temperature moderation;
3. maintain the epidermal barrier with gentle, nonirritating products;
4. avoid unnecessary topical corticosteroids on the face;
5. treat inflammatory or ocular manifestations early;
6. monitor for Demodex overgrowth when follicular scale or refractory papulopustules are present;
7. maintain effective therapy to reduce relapse; and
8. provide early ophthalmology referral for warning symptoms.

There is no role for genetic counseling for reproductive risk in ordinary rosacea beyond explaining multifactorial familial susceptibility. No public-health screening or immunization program applies.

---

## 14. Other species and natural disease

Naturally occurring **human rosacea has no established exact veterinary counterpart**. Dogs develop demodicosis—often due to species-specific *Demodex canis*—which is clinically and immunologically important but is not canine rosacea. Comparative value lies in host–mite immune tolerance, follicular inflammation, and acaricidal treatment, not in assuming identical disease. Demodex mites are normal residents in many mammals; in humans, higher density is associated with rosacea, whereas generalized canine demodicosis can be severe or fatal if untreated.

A Demodex-induced rosacea-like model has been produced in Japanese rabbits by intradermal mite suspension. It generated erythematous papules, telangiectasia, foreign-body material, and progressively organized granuloma-like histology over four weeks. This is an induced model rather than spontaneous rabbit disease and particularly represents Demodex-positive inflammation. Suggested taxonomy: *Homo sapiens* NCBI Taxon 9606, *Mus musculus* 10090, *Oryctolagus cuniculus* 9986, and *Canis lupus familiaris* 9615.

There is no zoonotic transmission of rosacea. Demodex species are substantially host-adapted; ordinary rosacea is neither communicable nor a veterinary public-health hazard.

---

## 15. Model organisms and experimental systems

### LL-37 mouse model

Repeated intradermal LL-37 in BALB/c mice produces erythema, leukocyte infiltration, epidermal/dermal thickening, and inflammatory mediators. Twenty-day administration caused lesion expansion for approximately 13 days followed by stabilization, with collagen deposition and increased α-SMA, TNF-α, vimentin, and COL1; unlike short exposure, lesions did not completely recover. This model is useful for TLR/LL-37, mast-cell, NLRP3, fibrosis, and candidate-drug studies but bypasses human initiation, facial neurovascular anatomy, chronic spontaneous relapse, and full ocular/phyma biology. (zhang2023longtermadministrationof pages 13-14)

### 2024 single-cell functional validation

The scRNA-seq study used murine interventions to show that IFNγ blockade improved barrier injury and rosacea-like inflammation, while fibroblast depletion or **PTGDS** knockdown inhibited disease development. This provides functional support for human atlas findings, but species differences and the small human discovery cohort prevent direct therapeutic extrapolation. (chen2024singlecelltranscriptomicsreveals pages 1-2)

### Other systems

- **Demodex-injected rabbit:** best for mite-associated papules, telangiectasia, and granulomatous histology; artificial inoculation and species mismatch are major limitations.
- **Keratinocyte/reconstructed epidermis/ex-vivo human skin:** useful for CAMP/LL-37, KLK5, cytokine, barrier, and topical-drug mechanisms; lacks intact vascular, neural, endocrine, and systemic immunity.
- **Human facial biopsies and bulk/single-cell transcriptomics:** highest disease relevance for cell-state discovery but usually cross-sectional, small, and vulnerable to treatment, site, sex, phototype, and tissue-dissociation confounding.
- **Canine demodicosis:** comparative natural host–mite immunology model, not a phenocopy of human rosacea.

No universally satisfactory spontaneous genetic mouse, zebrafish, Drosophila, organoid, iPSC, or humanized model captures the entire disease. Consensus literature explicitly identifies the absence of a comprehensive model, registry, and tissue biobank as a major research barrier. (tan2018applyingthephenotype pages 5-10)

---

## Evidence-strength assessment and abstract quotations

The strongest evidence tiers are: phenotype criteria from international consensus; treatment efficacy from systematic review of RCTs; susceptibility from large human GWAS; and mechanism from convergent human tissue, single-cell, in-vitro/ex-vivo, and induced-animal studies. Causal confidence is lower for individual dietary factors, gut dysbiosis, *H. pylori*, rare familial variants, and computationally inferred biomarkers.

Representative verbatim abstract statements from retrieved 2023–2024 sources are:

> “Rosacea is a complex inflammatory condition characterized by papulopustular lesions and erythema on the central face for which there is no cure.” — Tu et al., 2024, DOI 10.3389/fimmu.2024.1403798.

> “Among keratinocytes, a subpopulation characterized by IFNγ-mediated barrier function damage is found to be unique to rosacea lesions.” — Chen et al., 2024, DOI 10.1038/s41467-024-52946-7. (chen2024singlecelltranscriptomicsreveals pages 1-2)

> “The identified loci provide specificity of inflammatory mechanisms in rosacea, and identify potential pathways for therapeutic intervention.” — Aponte et al., 2018, DOI 10.1093/hmg/ddy184. (aponte2018assessmentofrosacea pages 7-8)

> “A transition from a subtyping to a phenotyping approach in rosacea is underway, allowing individual patient management according to presenting features instead of categorization by predefined subtypes.” — ROSCO update, DOI 10.1111/bjd.18420.

### Key source links and dates

- Nguyen et al., **23 January 2024**, practical clinical review: https://doi.org/10.2147/CCID.S391705. (nguyen2024rosaceapracticalguidance pages 1-3)
- Galluccio et al., **17 January 2024**, pathogenesis/treatment review: https://doi.org/10.3390/cosmetics11010011. (galluccio2024advancesinthe pages 2-4, galluccio2024advancesinthe pages 1-2)
- Chen et al., **October 2024**, primary single-cell study: https://doi.org/10.1038/s41467-024-52946-7. (chen2024singlecelltranscriptomicsreveals pages 1-2)
- Liang et al., **February 2024**, integrated transcriptomics: https://doi.org/10.1038/s41598-024-53453-x. (liang2024exploringtheassociation pages 14-15)
- Tan et al., **February 2017**, ROSCO diagnosis consensus: https://doi.org/10.1111/bjd.15122. (tan2017updatingthediagnosis pages 9-11)
- van Zuuren et al., **2019**, 152-study intervention review: https://doi.org/10.1111/bjd.17590. (zuuren2019interventionsforrosacea pages 1-2, zuuren2019interventionsforrosacea pages 2-3)
- Aponte et al., **May 2018**, GWAS: https://doi.org/10.1093/hmg/ddy184. (aponte2018assessmentofrosacea pages 7-8)
- Zhang et al., **March 2023**, prolonged LL-37 mouse model: https://doi.org/10.3390/cimb45040177. (zhang2023longtermadministrationof pages 13-14)

PMIDs were not printed in the retrieved full-text metadata for most sources; DOI URLs are therefore supplied as the stable primary links rather than risking incorrect PMID assignment.

References

1. (nguyen2024rosaceapracticalguidance pages 1-3): Cassidy Nguyen, Guilherme Kuceki, Michael Birdsall, Dev Ram Sahni, Vikram Sahni, and Christopher M Hull. Rosacea: practical guidance and challenges for clinical management. Clinical, Cosmetic and Investigational Dermatology, 17:175-190, Jan 2024. URL: https://doi.org/10.2147/ccid.s391705, doi:10.2147/ccid.s391705. This article has 44 citations and is from a peer-reviewed journal.

2. (chen2024singlecelltranscriptomicsreveals pages 1-2): Mengting Chen, Li Yang, Peijie Zhou, Suoqin Jin, Zheng Wu, Zixin Tan, Wenqin Xiao, San Xu, Yan Zhu, Mei Wang, Dan Jian, Fangfen Liu, Yan Tang, Zhixiang Zhao, Yingxue Huang, Wei Shi, Hongfu Xie, Qing Nie, Ben Wang, Zhili Deng, and Ji Li. Single-cell transcriptomics reveals aberrant skin-resident cell populations and identifies fibroblasts as a determinant in rosacea. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-52946-7, doi:10.1038/s41467-024-52946-7. This article has 24 citations and is from a highest quality peer-reviewed journal.

3. (galluccio2024advancesinthe pages 1-2): Giulia Galluccio, Martina D’Onghia, Dalma Malvaso, Laura Lazzeri, Elisa Cinotti, Giovanni Rubegni, Pietro Rubegni, and Laura Calabrese. Advances in the pathogenesis and treatment of rosacea: a phenotype-based therapeutic approach. Cosmetics, 11:11, Jan 2024. URL: https://doi.org/10.3390/cosmetics11010011, doi:10.3390/cosmetics11010011. This article has 31 citations.

4. (tan2017updatingthediagnosis pages 9-11): J. Tan, L.M.C. Almeida, A. Bewley, B. Cribier, N.C. Dlova, R. Gallo, G. Kautz, M. Mannis, H.H. Oon, M. Rajagopalan, M. Steinhoff, D. Thiboutot, P. Troielli, G. Webster, Y. Wu, E.J. Zuuren, and M. Schaller. Updating the diagnosis, classification and assessment of rosacea: recommendations from the global rosacea consensus (rosco) panel. British Journal of Dermatology, 176:431-438, Feb 2017. URL: https://doi.org/10.1111/bjd.15122, doi:10.1111/bjd.15122. This article has 423 citations and is from a highest quality peer-reviewed journal.

5. (zuuren2019interventionsforrosacea pages 1-2): E. J. Zuuren, Z. Fedorowicz, Jerry Tan, M. Linden, B. Arents, B. Carter, and L. Charland. Interventions for rosacea based on the phenotype approach: an updated systematic review including grade assessments. The British Journal of Dermatology, 181:65-79, Mar 2019. URL: https://doi.org/10.1111/bjd.17590, doi:10.1111/bjd.17590. This article has 208 citations.

6. (aponte2018assessmentofrosacea pages 7-8): Jennifer L Aponte, Mathias N Chiano, Laura M Yerges-Armstrong, David A Hinds, Chao Tian, Akanksha Gupta, Cong Guo, Dana J Fraser, Johannes M Freudenberg, Deepak K Rajpal, Margaret G Ehm, and Dawn M Waterworth. Assessment of rosacea symptom severity by genome-wide association study and expression analysis highlights immuno-inflammatory and skin pigmentation genes. Human Molecular Genetics, 27:2762-2772, May 2018. URL: https://doi.org/10.1093/hmg/ddy184, doi:10.1093/hmg/ddy184. This article has 60 citations and is from a domain leading peer-reviewed journal.

7. (galluccio2024advancesinthe pages 2-4): Giulia Galluccio, Martina D’Onghia, Dalma Malvaso, Laura Lazzeri, Elisa Cinotti, Giovanni Rubegni, Pietro Rubegni, and Laura Calabrese. Advances in the pathogenesis and treatment of rosacea: a phenotype-based therapeutic approach. Cosmetics, 11:11, Jan 2024. URL: https://doi.org/10.3390/cosmetics11010011, doi:10.3390/cosmetics11010011. This article has 31 citations.

8. (shi2026neurohormonalimmunedysregulationin pages 2-4): Lei Shi, Siying Li, Xiaodong Yao, Zijian Zhang, Qinyi Dong, Han Zhang, Xinman Wang, Jiahao Bai, Huiyan Han, Xiaoyi Fu, Kailin Zheng, and Li-Li Liang. Neurohormonal-immune dysregulation in rosacea: emerging perspectives from the skin-gut-brain axis. Jun 2026. URL: https://doi.org/10.2147/dddt.s608151, doi:10.2147/dddt.s608151. This article has 0 citations.

9. (zhang2023longtermadministrationof pages 13-14): Chuanxi Zhang, Yumeng Kang, Ziyan Zhang, Heliang Liu, Hong Xu, Wenchen Cai, Xuemin Gao, and Jie Yang. Long-term administration of ll-37 can induce irreversible rosacea-like lesion. Current Issues in Molecular Biology, 45:2703-2716, Mar 2023. URL: https://doi.org/10.3390/cimb45040177, doi:10.3390/cimb45040177. This article has 26 citations.

10. (tan2018applyingthephenotype pages 5-10): Jerry Tan, M. Berg, Richard L. Gallo, and J. Q. D. Rosso. Applying the phenotype approach for rosacea to practice and research. British Journal of Dermatology, 179:741-746, Jul 2018. URL: https://doi.org/10.1111/bjd.16815, doi:10.1111/bjd.16815. This article has 52 citations and is from a highest quality peer-reviewed journal.

11. (OpenTargets Search: rosacea): Open Targets Query (rosacea, 12 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

12. (liang2024exploringtheassociation pages 14-15): Jingchen Liang, Ying Chen, Zihao Wang, Yawen Wang, Shengzhi Mu, Dewu Zhang, Weihui Zeng, and Zhao Wang. Exploring the association between rosacea and acne by integrated bioinformatics analysis. Scientific Reports, Feb 2024. URL: https://doi.org/10.1038/s41598-024-53453-x, doi:10.1038/s41598-024-53453-x. This article has 6 citations and is from a peer-reviewed journal.

13. (zuuren2019interventionsforrosacea pages 2-3): E. J. Zuuren, Z. Fedorowicz, Jerry Tan, M. Linden, B. Arents, B. Carter, and L. Charland. Interventions for rosacea based on the phenotype approach: an updated systematic review including grade assessments. The British Journal of Dermatology, 181:65-79, Mar 2019. URL: https://doi.org/10.1111/bjd.17590, doi:10.1111/bjd.17590. This article has 208 citations.

## Artifacts

- [Edison artifact artifact-00](Rosacea-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0006604` (4 mentions) - the report calls it "if available"; MONDO calls it **rosacea**