---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-15T16:10:20.561963'
end_time: '2026-09-15T16:21:28.772880'
duration_seconds: 668.21
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Placenta Previa
  mondo_id: MONDO:0005918
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 51
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 31
  verified: 29
  not_found: 1
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.033
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0005918
    reported_labels:
    - if available
    ontology_label: placenta praevia
  unresolved_terms:
  - HP:0030916
  unresolvable_prefixes:
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Placenta_Previa-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Placenta Previa
- **MONDO ID:** MONDO:0005918 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Placenta Previa** covering all of the
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
- **Disease Name:** Placenta Previa
- **MONDO ID:** MONDO:0005918 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Placenta Previa** covering all of the
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


# Placenta Previa (MONDO:0005918): Disease-Characteristics Research Report

## Executive summary

Placenta previa is a **pregnancy-specific anatomical disorder** in which placental tissue overlies the internal cervical os. Contemporary nomenclature reserves *placenta previa* for tissue covering the os and uses *low-lying placenta* when the placental edge is near, but does not cover, the os. It is not the same disease as placenta accreta spectrum (PAS), although previa—especially over a previous cesarean scar—is a major PAS risk context. The best-supported pathophysiology is abnormal low implantation followed by mechanical separation and bleeding as the lower uterine segment develops and the cervix changes. It is a complex, multifactorial condition, not a validated monogenic disorder. (fan2017theincidenceof pages 1-2, jenabi2023theassociationbetween pages 1-2)

The overall prevalence is approximately **5.2 per 1,000 pregnancies**. Among affected pregnancies, meta-analytic estimates are **51.6% for antepartum hemorrhage**, **22.3% for postpartum hemorrhage**, and **11.1% for concomitant PAS**, although definitions and populations are heterogeneous. Prior cesarean delivery, other endometrial–myometrial injury, advanced maternal age, multiparity, smoking, assisted reproductive technology (ART), and previous previa are the principal epidemiologic risk factors. (jauniaux2019epidemiologyofplacenta pages 3-4, fan2017theincidenceof pages 1-2, jenabi2023theassociationbetween pages 1-2, fan2017prevalenceofantepartum pages 1-2, gurolurganci2011riskofplacenta pages 1-2)

| Domain | Best quantitative finding | Evidence type/year | Source DOI or NCT |
|---|---|---|---|
| Prevalence | 5.2 cases per 1,000 pregnancies (0.52%) (jenabi2023theassociationbetween pages 1-2) | Systematic-review estimate cited in 2023 | [10.1186/s12887-023-04433-z](https://doi.org/10.1186/s12887-023-04433-z) |
| Antepartum hemorrhage (APH) | 51.6% (2,347/4,687; 95% CI 42.7–60.6%; 29 studies; I²=97.9%) (fan2017prevalenceofantepartum pages 1-2) | Systematic review/meta-analysis, 2017 | [10.1038/srep40320](https://doi.org/10.1038/srep40320) |
| Postpartum hemorrhage (PPH) | 22.3% (95% CI 15.8–28.7%; 11 studies; 5,146 pregnancies); 27.4% for previa versus 14.5% for low-lying placenta (fan2017theincidenceof pages 1-2) | Systematic review/meta-analysis, 2017 | [10.1371/journal.pone.0170194](https://doi.org/10.1371/journal.pone.0170194) |
| Placenta accreta spectrum (PAS) | Median PAS incidence among pregnancies with placenta previa: 11.10% (IQR 7.65–17.35%) (jauniaux2019epidemiologyofplacenta pages 3-4) | Systematic review/meta-analysis, 2019 | [10.1136/bmjopen-2019-031193](https://doi.org/10.1136/bmjopen-2019-031193) |
| Prior cesarean delivery | Second-birth previa: 8.7/1,000 after prior cesarean versus 4.4/1,000 after vaginal birth; adjusted OR 1.60 (95% CI 1.44–1.76; n=399,674) (gurolurganci2011riskofplacenta pages 1-2) | Population cohort plus meta-analysis, 2011 | [10.1186/1471-2393-11-95](https://doi.org/10.1186/1471-2393-11-95) |
| Fetal growth | IUGR/SGA: 8.7% with previa versus 5.8% in controls; pooled OR 1.19 (95% CI 1.10–1.27; 13 studies; 1,593,226 singleton pregnancies) (balayla2019placentapreviaand pages 1-2) | Systematic review/meta-analysis, 2019 | [10.1515/jpm-2019-0116](https://doi.org/10.1515/jpm-2019-0116) |
| Congenital abnormalities | Crude OR 1.81 (95% CI 1.34–2.28); adjusted OR 6.38 (95% CI 1.47–11.30); substantial heterogeneity (eight studies) (jenabi2023theassociationbetween pages 1-2) | Systematic review/meta-analysis, 2023 | [10.1186/s12887-023-04433-z](https://doi.org/10.1186/s12887-023-04433-z) |
| First-trimester miRNA signature | Seven-miRNA panel: AUC 0.937, sensitivity 100.0%, specificity 83.75%; 24 future-previa and 80 control pregnancies (hromadnikova2024abnormalmicrornaexpression pages 1-2) | Retrospective original study, 2024 | [10.3389/fmed.2024.1469855](https://doi.org/10.3389/fmed.2024.1469855) |
| Pharmacologic PPH prevention trial | Completed phase 4 randomized trial; n=81; IV tranexamic acid versus intrauterine misoprostol versus oxytocin-only control (NCT05340205 chunk 1) | Clinical trial, completed 2023 | [NCT05340205](https://clinicaltrials.gov/study/NCT05340205) |
| Surgical PPH prevention trial | Completed randomized trial; n=60; balloon tamponade versus B-Lynch compression suture (NCT05133167 chunk 1) | Clinical trial, completed 2021 | [NCT05133167](https://clinicaltrials.gov/study/NCT05133167) |


*Table: Compact quantitative evidence covering prevalence, hemorrhage, PAS, major risk and outcome associations, a preliminary molecular biomarker, and completed interventional trials. Estimates should be interpreted in light of observational designs and substantial heterogeneity in several meta-analyses.*

## 1. Disease information

### Definition and classification

Placenta previa is complete or partial placental coverage of the internal cervical os. A 2023 systematic review states directly: **“Placenta previa is the complete or partial coverage of the internal cervical os with the placenta.”** Low-lying placenta is distinct: placental tissue is close to, but does not overlie, the os. Older terminology divided previa into marginal, partial, and complete forms; contemporary practice generally classifies cases by whether the placenta covers the os and by the measured placental-edge–os distance. (fan2017theincidenceof pages 1-2, jenabi2023theassociationbetween pages 1-2, hromadnikova2024abnormalmicrornaexpression pages 1-2)

This distinction matters clinically. In a 4,490-pregnancy cohort, complete previa had stronger associations with PAS, severe postpartum hemorrhage, hemorrhagic shock, and hysterectomy than low-lying placenta; marginal and partial categories were less reproducible by ultrasound and had broadly similar outcomes. (bi2021effectoftypes pages 4-5)

### Identifiers and synonyms

- **MONDO:** MONDO:0005918, placenta previa.
- **ICD-10-CM:** O44.-, placenta previa; subcodes distinguish hemorrhage, trimester, and unspecified forms. The English population cohort identified cases with ICD-10 O44. (gurolurganci2011riskofplacenta pages 1-2)
- **MeSH:** D010923, *Placenta Previa*. (NCT05133167 chunk 1)
- **Common synonyms:** placenta praevia, placental previa, low implantation of placenta; historical terms include marginal, partial/incomplete, total/complete, minor, and major placenta previa.
- **ICD-11:** categorized within maternal disorders predominantly related to pregnancy/placental location; implementation-specific code verification is recommended before database loading.
- **OMIM/Orphanet:** no dedicated Mendelian-disease entry is expected because this is an acquired, multifactorial obstetric condition rather than a monogenic syndrome.

The evidence summarized here is **aggregated disease-level evidence** from systematic reviews, registries, cohorts, and trials. It is not an individual EHR record, although one major study used de-identified English Hospital Episode Statistics. (gurolurganci2011riskofplacenta pages 1-2)

## 2. Etiology, risk, and protective factors

### Causal framework

The exact initiating cause is unknown. The dominant model is that implantation occurs abnormally low because the upper uterine endometrium is relatively unfavorable or because scarred lower-segment tissue alters implantation and decidualization. This model is biologically plausible and consistent with epidemiology, but low implantation is not reducible to one molecular lesion.

### Established or strongly supported risk factors

- **Prior cesarean delivery:** in 399,674 English second births, previa occurred in 8.7/1,000 after a first cesarean versus 4.4/1,000 after vaginal birth; adjusted OR 1.60 (95% CI 1.44–1.76). A 37-study meta-analysis gave pooled OR 2.20 (1.96–2.46). The authors concluded: **“There is an increased risk of placenta previa in the subsequent pregnancy after CS delivery at first birth.”** (gurolurganci2011riskofplacenta pages 1-2)
- **Other uterine/endometrial injury:** curettage, induced or spontaneous abortion, myomectomy, manual placental removal, and other intrauterine operations are repeatedly associated. These associations support, but do not prove, the scar/decidualization mechanism. (sahu2024maternalandperinatal pages 2-3, jenabi2023theassociationbetween pages 1-2)
- **Previous placenta previa:** recurrence has been reported at approximately 4–8%. (balayla2019placentapreviaand pages 1-2)
- **Advanced maternal age and multiparity:** consistent epidemiologic associations; interaction between age, parity, cumulative uterine procedures, and conception method likely contributes.
- **ART and infertility:** a 2021 Chinese IVF cohort found that, relative to spontaneous conception, adjusted odds of previa varied by infertility subgroup: tubal disease 2.70 (95% CI 1.59–4.59), endometriosis 9.33 (4.22–20.62), male-factor infertility 4.14 (2.23–7.68), and mixed infertility 4.73 (1.83–12.21). This suggests contributions from both treatment and underlying reproductive pathology. (wang2021pregnancyoutcomesof pages 1-2)
- **Smoking:** consistently identified by reviews as a modifiable association, plausibly through placental hypoxia or compensatory enlargement, but direct mechanistic proof is limited. (sahu2024maternalandperinatal pages 1-2, jenabi2023theassociationbetween pages 1-2)
- **Multiple gestation and male fetus:** reported associations, but less actionable and less consistently quantified. (sahu2024maternalandperinatal pages 2-3, hromadnikova2024abnormalmicrornaexpression pages 1-2)

### Genetic, infectious, and environmental factors

No causal gene, susceptibility locus with accepted clinical validity, chromosomal abnormality, founder mutation, or Mendelian inheritance pattern has been established. Therefore, penetrance, carrier frequency, anticipation, germline mosaicism, and consanguinity are **not applicable**. Routine ClinVar/ClinGen-style variant annotation is inappropriate.

No bacterium, virus, fungus, or parasite is established as a cause. No specific occupational toxicant, radiation exposure, pollutant, diet, alcohol pattern, or medication has a validated causal relationship. Smoking is the main reproducible lifestyle association.

### Protective factors and gene–environment interaction

No validated protective allele, diet, supplement, or prophylactic drug prevents previa. Avoiding medically unnecessary primary cesarean delivery and smoking cessation may reduce population risk, but neither guarantees prevention. No replicated gene–environment interaction has been demonstrated. The clinically relevant interaction is instead **uterine scar × subsequent implantation** and possibly **infertility biology × ART procedure**. (wang2021pregnancyoutcomesof pages 1-2, gurolurganci2011riskofplacenta pages 1-2)

## 3. Phenotypes

Placenta previa is often asymptomatic when first found sonographically. Its classic symptomatic phenotype is sudden, painless, bright-red vaginal bleeding in the second half of pregnancy, usually episodic or recurrent and ranging from spotting to life-threatening hemorrhage.

- **Antepartum vaginal hemorrhage:** symptom/sign; adult pregnancy onset, episodic and severity-variable. Meta-analysis of 29 studies and 4,687 affected women estimated 51.6% (95% CI 42.7–60.6%; I² 97.9%). Suggested HPO: **HP:0001892 Abnormal bleeding** and **HP:0030972 Vaginal hemorrhage**; an obstetric-specific ontology term should be preferred where available. (fan2017prevalenceofantepartum pages 1-2)
- **Postpartum hemorrhage:** clinical sign, acute peripartum onset, potentially severe. Eleven studies involving 5,146 women gave pooled incidence 22.3% (15.8–28.7%); the estimate was 27.4% for previa versus 14.5% for low-lying placenta. Suggested HPO: **HP:0011891 Postpartum hemorrhage**. (fan2017theincidenceof pages 1-2)
- **Maternal anemia/hypovolemia/hemorrhagic shock:** laboratory and clinical consequences of blood loss; severity depends on bleeding. Suggested HPO: **HP:0001903 Anemia**, **HP:0033392 Hypovolemia**, and **HP:0031273 Hemorrhagic shock** where validated locally. (sahu2024maternalandperinatal pages 1-2, jenabi2023theassociationbetween pages 1-2)
- **Preterm labor/delivery:** downstream obstetric manifestation from bleeding or indicated delivery. Approximately 5% of all preterm deliveries have been attributed to previa in the reviewed evidence. Suggested HPO: **HP:0001622 Premature birth**. (sahu2024maternalandperinatal pages 3-5)
- **Fetal growth restriction/SGA:** generally mild association. Across 1,593,226 singleton pregnancies, growth abnormality occurred in 8.7% with previa versus 5.8% in controls; pooled OR 1.19 (1.10–1.27; I² 94%). The authors’ conclusion was: **“Neonates from pregnancies with placenta previa have a mild increase in the risk of IUGR/SGA.”** Suggested HPO: **HP:0001511 Intrauterine growth retardation**, **HP:0001518 Small for gestational age**. (balayla2019placentapreviaand pages 1-2)
- **Low birth weight, low Apgar score, respiratory distress, NICU admission, stillbirth/neonatal death:** mainly mediated by prematurity and hemorrhage rather than a fetal-intrinsic disorder. Suggested HPO: **HP:0001518**, **HP:0030916 Neonatal respiratory distress**, **HP:0003811 Neonatal death**, and **HP:0003826 Stillbirth**, subject to terminology validation. (sahu2024maternalandperinatal pages 3-5, jenabi2023theassociationbetween pages 1-2)
- **Congenital abnormalities:** a 2023 eight-study meta-analysis reported crude OR 1.81 (1.34–2.28) and adjusted OR 6.38 (1.47–11.30), but heterogeneity was extreme (I² 80.6–97.9%), so causality and the adjusted magnitude are uncertain. (jenabi2023theassociationbetween pages 1-2)

Quality-of-life studies using EQ-5D, SF-36, or PROMIS are sparse. Practical burden includes emergency admission, activity disruption, anxiety about recurrent hemorrhage, prolonged inpatient observation, transfusion, operative morbidity, preterm neonatal hospitalization, and possible fertility loss after hysterectomy.

## 4. Genetic and molecular information

### Clinical genetics

There are **no validated causal genes, pathogenic variants, modifier genes, chromosomal abnormalities, or clinically actionable pharmacogenomic markers** for isolated placenta previa. WES, WGS, gene panels, single-gene testing, CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion testing are not indicated for diagnosing maternal previa. Fetal genetic testing follows ordinary prenatal indications—for example, fetal anomaly or abnormal aneuploidy screening—not the placental location alone.

### Emerging molecular profiling

A 2024 retrospective study compared first-trimester whole-blood microRNAs in 24 singleton pregnancies later developing isolated previa and 80 controls. Fifteen miRNAs were downregulated, including miR-20b-5p, miR-24-3p, miR-26a-5p, miR-92a-3p, miR-103a-3p, miR-130b-3p, miR-133a-3p, miR-145-5p, miR-146a-5p, miR-155-5p, miR-181a-5p, miR-195-5p, miR-210-3p, miR-342-3p, and miR-574-3p. A seven-miRNA model achieved AUC 0.937, 100% sensitivity, and 83.75% specificity; 75% of future cases were detected at a 10% false-positive rate. The authors appropriately cautioned: **“Consecutive large-scale analyses must be performed to verify the reliability”** of the model. This is preliminary association/prediction evidence, not a diagnostic assay or proof of causal gene regulation. Published 3 December 2024; DOI: [10.3389/fmed.2024.1469855](https://doi.org/10.3389/fmed.2024.1469855). (hromadnikova2024abnormalmicrornaexpression pages 1-2)

No reproducible placenta-previa-specific proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, CRISPR-screen, or epigenome signature is clinically validated.

## 5. Environmental and lifestyle information

Smoking is the principal modifiable exposure associated with previa. Prior uterine instrumentation and cesarean delivery are iatrogenic/anatomical exposures rather than environmental toxins. ART is a reproductive-technology exposure whose association varies by infertility diagnosis. Evidence is insufficient for a previa-specific role of air pollution, endocrine disruptors, occupational agents, radiation, exercise, diet, alcohol, or infection. (wang2021pregnancyoutcomesof pages 1-2, jenabi2023theassociationbetween pages 1-2, gurolurganci2011riskofplacenta pages 1-2)

Suggested chemical ontology terms for treatment—not etiology—include **CHEBI:30623 oxytocin**, **CHEBI:48669 tranexamic acid**, and **CHEBI:7023 misoprostol**, with identifier verification before ingestion.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Prior uterine scarring/endometrial injury, altered implantation biology, ART-related factors, or an unknown initiating determinant leads to implantation of the blastocyst in the lower uterine segment**; this first mechanistic link is strongly supported epidemiologically but incompletely demonstrated molecularly. (wang2021pregnancyoutcomesof pages 1-2, gurolurganci2011riskofplacenta pages 1-2)
2. **Low implantation leads to placental tissue reaching or covering the internal cervical os**, producing the defining anatomical lesion. (fan2017theincidenceof pages 1-2, jenabi2023theassociationbetween pages 1-2)
3. **Growth of the uterus and formation of the lower uterine segment lead to apparent placental “migration” or resolution in many early cases** through differential uterine growth/trophotropism rather than physical movement of the placenta. Persistent complete/major previa is more likely after prior cesarean and with greater initial overlap. (sahu2024maternalandperinatal pages 6-7, wei2022dynamicchangeof pages 6-9)
4. **If previa persists, lower-segment stretching, cervical effacement/dilatation, or uterine contractions leads to shear at the relatively inelastic placental attachment**, resulting in partial placental separation and maternal-vessel disruption; this mechanical explanation is biologically plausible and widely accepted, though direct experimental demonstration is limited. (balayla2019placentapreviaand pages 1-2)
5. **Vessel disruption leads to painless antepartum bleeding**, which may recur and branch:
   1. **Maternal branch:** ongoing blood loss leads to anemia, hypovolemia, shock, transfusion, emergency cesarean delivery, intensive care, and occasionally hysterectomy or death. (sahu2024maternalandperinatal pages 1-2, jenabi2023theassociationbetween pages 1-2, fan2017prevalenceofantepartum pages 1-2)
   2. **Fetal branch:** hemorrhage and urgent delivery lead to fetal hypoxia and prematurity, which result in low birth weight, respiratory morbidity, NICU admission, and increased perinatal mortality. (sahu2024maternalandperinatal pages 3-5)
6. **Implantation over a scar with defective decidualization may branch into PAS**, in which villi abnormally adhere to or invade myometrium; PAS then markedly amplifies surgical hemorrhage and adjacent-organ injury. Previa itself and PAS must not be conflated. (sahu2024maternalandperinatal pages 5-6, jauniaux2019epidemiologyofplacenta pages 3-4)
7. **Placental separation after delivery plus poor contractility of the lower uterine segment leads to postpartum hemorrhage**, potentially requiring uterotonics, antifibrinolytic therapy, tamponade, compression sutures, arterial control, or hysterectomy. (NCT05340205 chunk 1, NCT05133167 chunk 1, fan2017theincidenceof pages 1-2)

### Cellular, molecular, and tissue detail

The dominant cells are decidual stromal cells, extravillous trophoblasts, syncytiotrophoblasts, uterine smooth-muscle cells, and maternal endothelial cells. Unlike PAS, uncomplicated previa is principally a localization disorder; excessive trophoblast invasion is not required.

A small 2023 histopathology study compared 20 previa, 20 accreta, and 20 control placentas. Previa sections showed pyknotic nuclei in muscle cells, vascular dilatation and fibrinoid structures, and dense intervillous erythrocyte accumulation. These findings are hypothesis-generating because the sample was small and the journal/reporting quality limits generalizability. Published 15 October 2023; DOI: [10.22270/jddt.v13i10.6235](https://doi.org/10.22270/jddt.v13i10.6235). (erdogan2023histopatologicalchangesin pages 1-2)

Suggested GO biological-process terms include **GO:0007566 embryo implantation**, **GO:0001892 embryonic placenta development**, **GO:0042060 wound healing**, **GO:0001525 angiogenesis**, **GO:0007599 hemostasis**, **GO:0007596 blood coagulation**, **GO:0008285 negative regulation of cell proliferation** only where experimentally supported, and terms for smooth-muscle contraction and extracellular-matrix organization. Suggested Cell Ontology terms include **CL:0000351 trophoblast**, **CL:0000525 syncytiotrophoblast cell**, decidual stromal cell, vascular endothelial cell (**CL:0000115**), and smooth muscle cell (**CL:0000192**); exact releases should be verified.

Subcellular protein misfolding, aggregation, channelopathy, enzyme deficiency, autophagy failure, or a specific metabolic block has not been demonstrated. Similarly, Wnt, MAPK, PI3K–AKT, mTOR, or immune pathways should not be asserted as causal for isolated previa based only on general placental biology.

## 7. Anatomical structures affected

- **Primary organ:** placenta and gravid uterus.
- **Primary site:** lower uterine segment and internal cervical os; suggested terms: **UBERON:0001987 placenta**, **UBERON:0000995 uterus**, **UBERON:0000002 uterine cervix**, subject to release verification.
- **Tissue interface:** decidua basalis/endometrium, chorionic villi, intervillous maternal blood space, myometrium, and lower-segment vasculature.
- **Secondary involvement:** maternal cardiovascular/hematologic systems during hemorrhage; fetal/neonatal respiratory and neurologic risk through hypoxia and prematurity. Bladder, ureters, and pelvic structures are generally threatened only when PAS/percreta coexists.
- **Lateralization:** not applicable. Clinically relevant location descriptors are anterior versus posterior, complete versus incomplete coverage, and relation to a cesarean scar.
- **Subcellular localization:** no disease-defining organelle lesion is known.

## 8. Temporal development

The lesion originates during implantation and placentation but is usually detected during routine mid-trimester ultrasound. Screening at approximately 18–22 weeks is followed by repeat localization later in pregnancy when the placenta is low. (hromadnikova2024abnormalmicrornaexpression pages 1-2)

Many second-trimester low placentas resolve as the lower segment develops. One review reports apparent migration around 5.4 mm/week and resolution of more than 98% of suspected second-trimester low-lying/previa findings, but estimates depend heavily on initial overlap and case definition. By contrast, a selected cohort of **major** second-trimester previa found 71.2% persistent previa at delivery, illustrating why low-lying and major/complete disease cannot be pooled. (sahu2024maternalandperinatal pages 6-7, wei2022dynamicchangeof pages 6-9)

Clinical bleeding is acute and episodic, usually in the late second or third trimester; recurrence and severity are unpredictable. The critical windows are mid-trimester detection, third-trimester reassessment, onset of any bleeding, and planned delivery before labor. The condition ends with delivery and placental removal; it is not lifelong, although recurrence risk affects subsequent pregnancies.

## 9. Inheritance and population epidemiology

Overall prevalence is approximately **5.2/1,000 pregnancies (0.52%)**. A PAS-focused meta-analysis found median previa prevalence 0.56% (IQR 0.39–1.24), with marked heterogeneity. Regional and institutional estimates vary because of maternal age, parity, cesarean and ART rates, ultrasound practice, referral concentration, and diagnostic thresholds. (jauniaux2019epidemiologyofplacenta pages 3-4, jenabi2023theassociationbetween pages 1-2, hromadnikova2024abnormalmicrornaexpression pages 1-2)

This disease affects pregnant individuals with a placenta; fetal sex is not the defining sex distribution. The typical affected population is reproductive-age adults, with risk increasing at advanced maternal age. Some studies report higher rates among Asian and Black populations, but ethnicity may proxy differences in obstetric history, access, ascertainment, and social determinants; it should not be treated as a deterministic biological category. (sahu2024maternalandperinatal pages 2-3)

Inheritance is **multifactorial/non-Mendelian**. Penetrance, expressivity, anticipation, founder effects, carrier frequency, mosaicism, and variant geography are not applicable.

## 10. Diagnostics

### Standard diagnostic pathway

1. **Routine obstetric ultrasound** identifies placental location.
2. If low placement is suspected, **transvaginal ultrasound (TVUS)** is the reference imaging method for accurately measuring the placental edge relative to the internal os; it is more accurate than transabdominal assessment and is considered safe when performed appropriately. (sahu2024maternalandperinatal pages 5-6)
3. Repeat TVUS in the third trimester determines persistence and informs delivery mode. After approximately 35 weeks, an edge–os distance under 2 cm is associated with a higher cesarean rate; complete coverage is a contraindication to vaginal delivery. (sahu2024maternalandperinatal pages 6-7)
4. In previa with prior cesarean or suspicious ultrasound, evaluate specifically for **PAS**. Findings include placental lacunae, loss of the retroplacental hypoechoic zone, myometrial thinning/interruption, and abnormal uterovesical or placental–myometrial vascularity. MRI is adjunctive for inconclusive ultrasound, posterior placenta, invasion mapping, or surgical planning—not routine previa diagnosis. (sahu2024maternalandperinatal pages 5-6)

### Acute bleeding evaluation

Assess hemodynamic status, fetal heart rate, bleeding quantity, CBC/hemoglobin, blood type and antibody screen/crossmatch, coagulation studies when bleeding is substantial, and ultrasound. A sterile speculum examination may identify another source. **Digital cervical examination should be avoided until previa has been excluded**, because contact can precipitate severe hemorrhage. New bleeding generally warrants hospital assessment. (sahu2024maternalandperinatal pages 7-8)

### Differential diagnosis

Placental abruption usually causes painful bleeding, uterine tenderness/hypertonus, or fetal compromise; vasa previa causes fetal bleeding after membrane rupture; other alternatives include labor-related bloody show, cervical ectropion/polyp, cervicitis, trauma, and genital-tract malignancy. PAS is a comorbidity/differential placental invasion disorder, not a synonym.

### Biomarkers and screening

No blood, urine, tissue, or genetic biomarker is approved for diagnosis. The 2024 seven-miRNA model is exploratory and needs prospective external validation. Routine population ultrasound is effectively anatomical screening; there is no newborn, carrier, or cascade screening. (hromadnikova2024abnormalmicrornaexpression pages 1-2)

## 11. Outcome and prognosis

With prenatal recognition, blood availability, planned cesarean delivery, and multidisciplinary care, most patients survive and recover fully after delivery. Conventional five- or ten-year survival measures are not meaningful for this time-limited pregnancy complication.

Major maternal outcomes are recurrent antepartum hemorrhage, emergency delivery, postpartum hemorrhage, transfusion, anemia, shock, ICU admission, surgical injury, hysterectomy, and PAS. Median PAS incidence in a previa cohort was 11.10% (IQR 7.65–17.35). In a heterogeneous PAS-with-previa review, five maternal deaths occurred among 387 cases (1.3%); this figure pertains to the high-risk PAS subset, not uncomplicated previa. (jauniaux2019epidemiologyofplacenta pages 3-4, jauniaux2019epidemiologyofplacenta pages 4-5)

Perinatal prognosis is driven primarily by gestational age at delivery and hemorrhage. One reviewed estimate reported neonatal mortality of 10.7/1,000 in previa pregnancies versus 2.5/1,000 in other pregnancies (RR 4.3, 95% CI 4.0–4.8). Prematurity, low birth weight, fetal hypoxia, respiratory distress, and sepsis mediate much of this risk. (sahu2024maternalandperinatal pages 3-5)

Poor prognostic indicators include complete/major previa, anterior placenta over a cesarean scar, increasing numbers of prior cesareans, suspected PAS, recurrent or early bleeding, short cervix, emergency rather than planned delivery, anemia, and limited access to blood products or specialist surgery. Complete previa was the subtype most clearly associated with severe hemorrhage, shock, and hysterectomy in a large cohort. (bi2021effectoftypes pages 4-5)

## 12. Treatment and current implementation

There is no drug that relocates the placenta or cures previa. Management prevents and treats hemorrhage while optimizing fetal maturity.

### Clinical algorithm

- **Asymptomatic, stable, preterm:** expectant outpatient or inpatient management according to bleeding history, distance from hospital, support, laboratory status, and local guidance. Counsel about urgent presentation for bleeding, contractions, pain, or reduced fetal movement.
- **Bleeding:** hospitalize or assess urgently; establish IV access, quantify blood loss, obtain CBC and type/crossmatch, monitor maternal hemodynamics and fetus, administer anti-D immunoglobulin to eligible RhD-negative patients, and resuscitate with balanced blood-component therapy when needed. (sahu2024maternalandperinatal pages 7-8)
- **Risk of preterm delivery:** antenatal corticosteroids are used according to gestational-age guidance; magnesium sulfate is used for fetal neuroprotection when very preterm delivery is imminent, not to treat previa itself. Tocolysis may occasionally permit steroid completion in a stable patient but is inappropriate with major ongoing hemorrhage or maternal/fetal instability.
- **Planned delivery:** uncomplicated persistent complete previa is generally delivered by cesarean at **36–37 weeks**; earlier delivery is indicated for uncontrolled or recurrent major bleeding, labor, rupture of membranes, or maternal/fetal compromise. Suspected PAS follows an earlier specialist pathway, often 34–35+6 weeks, and should not be managed as simple previa. (sahu2024maternalandperinatal pages 2-3, sahu2024maternalandperinatal pages 6-7)
- **Operative preparation:** senior obstetric and anesthesia teams, neonatal support, large-bore access, crossmatched blood, hemorrhage protocol, uterotonics, cell salvage where available, and PAS/urology/interventional-radiology expertise when indicated.

### Hemorrhage interventions

Oxytocin and other uterotonics treat uterine atony; tranexamic acid inhibits fibrinolysis and is established for treatment of postpartum hemorrhage. Mechanical and surgical options include intrauterine balloon tamponade, uterine compression sutures, uterine or internal iliac artery ligation/embolization, stepwise devascularization, and hysterectomy. These interventions treat bleeding, not placental location. (NCT05340205 chunk 1, NCT05133167 chunk 1, fan2017theincidenceof pages 1-2)

Suggested NCIT mappings include **Cesarean Section**, **Blood Transfusion**, **Tranexamic Acid**, **Oxytocin**, **Misoprostol**, **Balloon Tamponade**, **Uterine Artery Embolization**, **Compression Suture**, and **Hysterectomy**; exact NCIT codes should be checked against the target release.

### Recent/experimental trials

- **NCT05340205**, completed phase 4 randomized open-label trial, Cairo University, actual n=81: IV tranexamic acid 1 g before incision versus intrauterine misoprostol 400 µg versus oxytocin-only control, all with postpartum oxytocin; primary endpoint was cesarean blood loss. The registry had no result values in the retrieved record, so efficacy cannot be inferred. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT05340205). (NCT05340205 chunk 1)
- **NCT05133167**, completed randomized open-label trial, Pakistan, n=60: Foley-balloon tamponade versus B-Lynch suture for prevention of hemorrhage; primary endpoint was 24-hour blood loss. No numerical results were available in the retrieved record. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT05133167). (NCT05133167 chunk 1)

Gene therapy, cell therapy, RNA therapy, immunotherapy, genotype-guided therapy, and precision oncology-style targeted treatment are not applicable. Pharmacogenomic testing is not standard.

## 13. Prevention

### Primary prevention

No intervention reliably prevents low implantation. Population-level strategies include avoiding medically unnecessary cesarean delivery and uterine instrumentation, smoking cessation, and evidence-based ART practice. The cesarean cohort estimated that 359 first-birth cesareans would produce one additional previa in the next pregnancy, illustrating a modest individual but meaningful population effect. (gurolurganci2011riskofplacenta pages 1-2)

### Secondary prevention

Routine mid-trimester placental localization, repeat TVUS for low placement, and targeted PAS assessment in patients with previa plus prior cesarean are the main early-detection strategies. Optimize maternal hemoglobin and arrange delivery at an appropriately resourced center.

### Tertiary prevention

Prevent death and organ injury through planned delivery before labor, readily available blood products, standardized hemorrhage protocols, experienced multidisciplinary teams, antenatal corticosteroids when preterm birth is expected, and timely escalation from uterotonics to tamponade, embolization/surgery, or hysterectomy. (sahu2024maternalandperinatal pages 5-6, sahu2024maternalandperinatal pages 7-8)

Vaccination, antimicrobial prophylaxis directed at disease causation, genetic counseling, preimplantation genetic testing, carrier screening, and prophylactic gene-based interventions are not applicable. Counseling should instead address recurrence, cesarean-associated future risk, PAS risk, and reproductive planning.

## 14. Other species and natural disease

No well-characterized, naturally occurring veterinary disorder directly homologous to human placenta previa was identified in the retrieved literature. Placental anatomy and implantation differ markedly across species; the human discoid, hemochorial placenta and uniquely remodeled lower uterine segment/internal os make direct extrapolation difficult. Sporadic low placentation may occur in nonhuman primates or domestic animals, but there is no established breed predisposition, orthologous causal gene, OMIA syndrome, or zoonotic/transmissible process. Consequently, NCBI Taxon and VBO annotations should not be asserted beyond **Homo sapiens (NCBI Taxon:9606)** without case-specific veterinary evidence.

## 15. Model organisms and experimental systems

There is no validated mouse, rat, sheep, zebrafish, invertebrate, knockout, or transgenic model that faithfully reproduces human placenta covering the internal cervical os and its late-pregnancy mechanical hemorrhage. Rodent uterine and placental geometry limits face validity. Models of cesarean scarring, decidualization failure, ART, trophoblast invasion, PAS, placental hypoxia, or hemorrhage can illuminate component processes but are not placenta-previa models.

The most relevant systems are therefore:

- human longitudinal ultrasound cohorts;
- registry/EHR studies of cesarean, ART, and obstetric outcomes;
- delivered human placenta and lower-segment histopathology;
- primary trophoblast/decidual cultures and organoids for implantation biology;
- maternal blood liquid-biopsy studies, including the preliminary first-trimester miRNA work. (hromadnikova2024abnormalmicrornaexpression pages 1-2, erdogan2023histopatologicalchangesin pages 1-2, gurolurganci2011riskofplacenta pages 1-2)

Their principal limitation is that tissues obtained at delivery reflect downstream consequences and cannot directly reconstruct implantation-site selection months earlier.

## Evidence appraisal and knowledge gaps

The strongest evidence concerns anatomy, ultrasound diagnosis, prior cesarean risk, hemorrhage burden, and clinical management. Most etiologic evidence is observational and susceptible to confounding by age, parity, infertility, uterine surgery, and referral patterns. Meta-analytic heterogeneity is substantial for hemorrhage, growth, and congenital-anomaly estimates. Molecular studies remain small and largely unvalidated; there are no clinically established causal genes or omics tests. Priority research areas are prospective first-trimester prediction, standardized definitions separating previa from low-lying placenta and PAS, external validation of molecular biomarkers, optimal hemorrhage-prevention strategies, patient-reported outcomes, and long-term infant outcomes.

References

1. (fan2017theincidenceof pages 1-2): Dazhi Fan, Qing Xia, Li Liu, Shuzhen Wu, Guo Tian, Wen Wang, Song Wu, Xiaoling Guo, and Zhengping Liu. The incidence of postpartum hemorrhage in pregnant women with placenta previa: a systematic review and meta-analysis. PLoS ONE, 12:e0170194, Jan 2017. URL: https://doi.org/10.1371/journal.pone.0170194, doi:10.1371/journal.pone.0170194. This article has 174 citations and is from a peer-reviewed journal.

2. (jenabi2023theassociationbetween pages 1-2): Ensiyeh Jenabi, Saeid Bashirian, and Sahar Khoshravesh. The association between of placenta previa and congenital abnormalities: a systematic review and network meta-analysis. BMC Pediatrics, Nov 2023. URL: https://doi.org/10.1186/s12887-023-04433-z, doi:10.1186/s12887-023-04433-z. This article has 5 citations and is from a peer-reviewed journal.

3. (jauniaux2019epidemiologyofplacenta pages 3-4): Eric Jauniaux, Lene Grønbeck, Catey Bunce, Jens Langhoff-Roos, and Sally L Collins. Epidemiology of placenta previa accreta: a systematic review and meta-analysis. BMJ Open, 9:e031193, Nov 2019. URL: https://doi.org/10.1136/bmjopen-2019-031193, doi:10.1136/bmjopen-2019-031193. This article has 252 citations and is from a peer-reviewed journal.

4. (fan2017prevalenceofantepartum pages 1-2): Dazhi Fan, Song Wu, Li Liu, Qing Xia, Wen Wang, Xiaoling Guo, and Zhengping Liu. Prevalence of antepartum hemorrhage in women with placenta previa: a systematic review and meta-analysis. Scientific Reports, Jan 2017. URL: https://doi.org/10.1038/srep40320, doi:10.1038/srep40320. This article has 143 citations and is from a peer-reviewed journal.

5. (gurolurganci2011riskofplacenta pages 1-2): Ipek Gurol-Urganci, David A Cromwell, Leroy C Edozien, Gordon CS Smith, Chidimma Onwere, Tahir A Mahmood, Allan Templeton, and Jan H van der Meulen. Risk of placenta previa in second birth after first birth cesarean section: a population-based study and meta-analysis. BMC Pregnancy and Childbirth, 11:95-95, Nov 2011. URL: https://doi.org/10.1186/1471-2393-11-95, doi:10.1186/1471-2393-11-95. This article has 247 citations and is from a peer-reviewed journal.

6. (balayla2019placentapreviaand pages 1-2): Jacques Balayla, Jade Desilets, and Guy Shrem. Placenta previa and the risk of intrauterine growth restriction (iugr): a systematic review and meta-analysis. Journal of Perinatal Medicine, 47:577-584, Aug 2019. URL: https://doi.org/10.1515/jpm-2019-0116, doi:10.1515/jpm-2019-0116. This article has 65 citations and is from a peer-reviewed journal.

7. (hromadnikova2024abnormalmicrornaexpression pages 1-2): Ilona Hromadnikova, Katerina Kotlabova, and Ladislav Krofta. Abnormal microrna expression profile at early stages of gestation in pregnancies destined to develop placenta previa. Frontiers in Medicine, Dec 2024. URL: https://doi.org/10.3389/fmed.2024.1469855, doi:10.3389/fmed.2024.1469855. This article has 3 citations.

8. (NCT05340205 chunk 1): Noran Amin. Blood Loss During Cesarean Delivery in Placenta Previa Patients. Cairo University. 2022. ClinicalTrials.gov Identifier: NCT05340205

9. (NCT05133167 chunk 1): M. Awais Qarni. Balloon Tamponade Vs B-Lynch In Placenta Previa. CMH Jhelum. 2021. ClinicalTrials.gov Identifier: NCT05133167

10. (bi2021effectoftypes pages 4-5): Shilei Bi, Lizi Zhang, Zhijian Wang, Jingsi Chen, Jingman Tang, Jingjin Gong, Sushan Xie, Lin Lin, Luwen Ren, Shanshan Zeng, Lijun Huang, Shaoshuai Wang, Lili Du, and Dunjin Chen. Effect of types of placenta previa on maternal and neonatal outcomes: a 10-year retrospective cohort study. Archives of Gynecology and Obstetrics, pages 1-8, Jan 2021. URL: https://doi.org/10.1007/s00404-020-05912-9, doi:10.1007/s00404-020-05912-9. This article has 49 citations and is from a peer-reviewed journal.

11. (sahu2024maternalandperinatal pages 2-3): Shreya A Sahu and Deepti Shrivastava. Maternal and perinatal outcomes in placenta previa: a comprehensive review of evidence. May 2024. URL: https://doi.org/10.7759/cureus.59737, doi:10.7759/cureus.59737. This article has 31 citations.

12. (wang2021pregnancyoutcomesof pages 1-2): Jingxue Wang, Qiwei Liu, Boer Deng, Fang Chen, Xiaowei Liu, and Jiumei Cheng. Pregnancy outcomes of chinese women undergoing ivf with embryonic cryopreservation as compared to natural conception. Jan 2021. URL: https://doi.org/10.1186/s12884-020-03486-7, doi:10.1186/s12884-020-03486-7. This article has 40 citations and is from a peer-reviewed journal.

13. (sahu2024maternalandperinatal pages 1-2): Shreya A Sahu and Deepti Shrivastava. Maternal and perinatal outcomes in placenta previa: a comprehensive review of evidence. May 2024. URL: https://doi.org/10.7759/cureus.59737, doi:10.7759/cureus.59737. This article has 31 citations.

14. (sahu2024maternalandperinatal pages 3-5): Shreya A Sahu and Deepti Shrivastava. Maternal and perinatal outcomes in placenta previa: a comprehensive review of evidence. May 2024. URL: https://doi.org/10.7759/cureus.59737, doi:10.7759/cureus.59737. This article has 31 citations.

15. (sahu2024maternalandperinatal pages 6-7): Shreya A Sahu and Deepti Shrivastava. Maternal and perinatal outcomes in placenta previa: a comprehensive review of evidence. May 2024. URL: https://doi.org/10.7759/cureus.59737, doi:10.7759/cureus.59737. This article has 31 citations.

16. (wei2022dynamicchangeof pages 6-9): Sumei Wei, Xin Li, Tianjiao Liu, Rui Ding, Lu Wei, Conghong Fan, Dongmei Tang, Wen Xiong, Yalan Li, and Xiao Yang. Dynamic change of placenta previa from second trimester to delivery: a retrospective longitudinal study cohort. ArXiv, Jan 2022. URL: https://doi.org/10.21203/rs.3.rs-1188255/v1, doi:10.21203/rs.3.rs-1188255/v1. This article has 0 citations.

17. (sahu2024maternalandperinatal pages 5-6): Shreya A Sahu and Deepti Shrivastava. Maternal and perinatal outcomes in placenta previa: a comprehensive review of evidence. May 2024. URL: https://doi.org/10.7759/cureus.59737, doi:10.7759/cureus.59737. This article has 31 citations.

18. (erdogan2023histopatologicalchangesin pages 1-2): Gamze ERDOĞAN, Engin DEVECİ, Nurullah PEKER, İbrahim İBİLOĞLU, Yavuz TEKELİOĞLU, Dilek YAVUZ, Gül Ebru AKDENİZ, and Hasan ERDOĞAN. Histopatological changes in plasenta previa, plasenta acreata and normotensive plasentas in the 3rd trimestry of pregnancy. Journal of Drug Delivery and Therapeutics, 13(10):28-32, Oct 2023. URL: https://doi.org/10.22270/jddt.v13i10.6235, doi:10.22270/jddt.v13i10.6235. This article has 0 citations.

19. (sahu2024maternalandperinatal pages 7-8): Shreya A Sahu and Deepti Shrivastava. Maternal and perinatal outcomes in placenta previa: a comprehensive review of evidence. May 2024. URL: https://doi.org/10.7759/cureus.59737, doi:10.7759/cureus.59737. This article has 31 citations.

20. (jauniaux2019epidemiologyofplacenta pages 4-5): Eric Jauniaux, Lene Grønbeck, Catey Bunce, Jens Langhoff-Roos, and Sally L Collins. Epidemiology of placenta previa accreta: a systematic review and meta-analysis. BMJ Open, 9:e031193, Nov 2019. URL: https://doi.org/10.1136/bmjopen-2019-031193, doi:10.1136/bmjopen-2019-031193. This article has 252 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Placenta_Previa-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005918` (3 mentions) - the report calls it "if available"; MONDO calls it **placenta praevia**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0030916` (1 mention) - HP does not contain this term

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.