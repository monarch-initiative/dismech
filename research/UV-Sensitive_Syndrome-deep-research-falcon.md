---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-09T17:08:26.327127'
end_time: '2026-09-09T17:17:34.432954'
duration_seconds: 548.11
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: UV-Sensitive Syndrome
  mondo_id: MONDO:0015797
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 44
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 16
  verified: 16
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0015797
    reported_labels:
    - if available
    ontology_label: UV-sensitive syndrome
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: UV-Sensitive_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** UV-Sensitive Syndrome
- **MONDO ID:** MONDO:0015797 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **UV-Sensitive Syndrome** covering all of the
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
- **Disease Name:** UV-Sensitive Syndrome
- **MONDO ID:** MONDO:0015797 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **UV-Sensitive Syndrome** covering all of the
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


# UV-Sensitive Syndrome: Disease-Characteristics Research Report

**Target disease:** UV-sensitive syndrome (UVSS)  
**Category:** rare Mendelian DNA-repair disorder  
**MONDO:** **MONDO:0015797**

## Executive summary

UVSS is an exceptionally rare, usually childhood-recognized, autosomal-recessive photodermatosis caused by biallelic defects in **UVSSA, ERCC8/CSA, or ERCC6/CSB**. Its defining phenotype is disproportionate sunburn and pigmentary change—especially freckling, xerosis, and sometimes telangiectasia—on sun-exposed skin, without the progressive neurologic, growth, developmental, or progeroid manifestations characteristic of Cockayne syndrome (CS). Patient cells are UV hypersensitive and fail to restore RNA synthesis after UV exposure, while global-genome nucleotide-excision repair remains comparatively intact. This identifies the central lesion as defective **transcription-coupled nucleotide-excision repair (TC-NER)** rather than generalized NER failure. No convincing UVSS-specific predisposition to skin or internal cancer has been established, but the number and follow-up of reported patients are too small to declare the risk zero. (spivak2015photosensitivehumansyndromes. pages 4-6, muzammal2021themoleculargenetics pages 1-2, li2019twonovelmutations pages 2-2, muzammal2021themoleculargenetics pages 3-5)

A 2021 review counted only **18 patients from nine families** and listed Japanese, French, Israeli, Iranian, and Pakistani kindreds. Its quoted prevalence estimate of 1:100,000 is not supported by registry or population-surveillance data and should not be entered as a validated prevalence; incidence, sex ratio, carrier frequency, penetrance, and survival statistics remain unknown. (muzammal2021themoleculargenetics pages 1-2)

The following table summarizes the strongest evidence and its limitations.

| Domain | Established finding | Evidence/model | Key quantitative or variant detail | Caveat |
|---|---|---|---|---|
| Phenotype and epidemiology | UV-sensitive syndrome (UVSS) is a mild, usually isolated cutaneous photosensitivity disorder characterized by exaggerated sunburn, freckling or pigmentary change, telangiectasia, and xerosis on sun-exposed skin; classic Cockayne neurologic, developmental, and systemic abnormalities are absent. | Aggregated case literature and reviews; DOI: [10.1016/j.mrfmmm.2014.11.003](https://doi.org/10.1016/j.mrfmmm.2014.11.003) and [10.47391/JPMA.03-476](https://doi.org/10.47391/JPMA.03-476) (spivak2015photosensitivehumansyndromes. pages 4-6, muzammal2021themoleculargenetics pages 1-2, muzammal2021themoleculargenetics pages 3-5) | A 2021 review counted 18 patients from nine families of Japanese, French, Israeli, Iranian, and Pakistani ancestry. | Extreme rarity and likely underdiagnosis preclude reliable incidence, prevalence, penetrance, sex-ratio, or phenotype-frequency estimates. The reported 1:100,000 prevalence lacks population surveillance support. No tumor predisposition is established, but limited cohorts cannot prove zero risk. |
| ERCC6/CSB | Biallelic **ERCC6** loss can cause UVSS1 rather than Cockayne syndrome, showing that genotype alone does not fully explain the clinical difference between these TC-NER disorders. | Human patients, fibroblast complementation, and molecular studies; DOI: [10.1073/pnas.0404587101](https://doi.org/10.1073/pnas.0404587101) and [10.1038/ng.2229](https://doi.org/10.1038/ng.2229) (nakazawa2012mutationsinuvssa pages 19-22, nakazawa2012mutationsinuvssa pages 22-24) | Two reported patients were homozygous for **ERCC6 c.229C>T (p.Arg77Ter)**, producing severe N-terminal truncation or absence of CSB. | Some secondary sources give inconsistent cDNA numbering for p.Arg77Ter; HGVS should be validated against the specified transcript. ERCC6 variants more commonly cause Cockayne syndrome. |
| ERCC8/CSA | Biallelic **ERCC8** variants cause UVSS2; CSA is a substrate-receptor component of the CRL4CSA ubiquitin-ligase complex involved in TC-NER assembly. | Human cases, segregation, and patient-cell studies; DOI: [10.1038/ng.2229](https://doi.org/10.1038/ng.2229) and [10.2340/00015555-3032](https://doi.org/10.2340/00015555-3032) (nakazawa2012mutationsinuvssa pages 22-24, li2019twonovelmutations pages 2-2) | Reported alleles include homozygous **c.1083G>T (p.Trp361Cys)** and **c.582G>T** plus **c.769G>A (p.Gly257Arg)** in a Chinese case; c.769G>A was reported below 0.01% in a Chinese dataset. | ERCC8 also causes Cockayne syndrome type A, so variant-specific functional and clinical context is essential. Current ClinVar classifications and gnomAD frequencies require independent verification. |
| UVSSA | Biallelic loss-of-function variants in **UVSSA** cause UVSS3 or UVSS-A and impair recovery of transcription after UV by disrupting TC-NER recruitment or stabilization. | Whole-exome sequencing, patient fibroblasts, complementation, and functional assays; DOI: [10.1038/ng.2229](https://doi.org/10.1038/ng.2229) (muzammal2021themoleculargenetics pages 2-3, nakazawa2012mutationsinuvssa pages 19-22) | Reported variants include **c.367A>T (p.Lys123Ter)**, **c.94T>C (p.Cys32Arg)**, **c.87delG (p.Ile31PhefsTer9)**, and **c.1040G>A**, reported as a codon-347 truncating allele. | Secondary sources inconsistently label c.1040G>A as p.Trp347Ter or p.Tyr347Ter; transcript and reference-sequence validation is mandatory. Population frequencies and ACMG classifications were not uniformly reported. |
| Cellular diagnostics | UVSS cells show increased UV cytotoxicity and defective recovery of RNA synthesis after UV, while global-genome photoproduct repair or unscheduled DNA synthesis is relatively preserved, indicating selective TC-NER deficiency. | Cultured patient fibroblasts assessed by post-UV survival, recovery of RNA synthesis, unscheduled DNA synthesis, and complementation (spivak2015photosensitivehumansyndromes. pages 4-6, nakazawa2012mutationsinuvssa pages 19-22, li2019twonovelmutations pages 2-2) | Characteristic qualitative pattern: low UV survival plus abnormal recovery of RNA synthesis with near-normal global repair. | These are specialized assays without universal clinical cutoffs. Molecular confirmation of biallelic pathogenic variants is preferred. |
| Canonical TC-NER | A transcription-blocking UV photoproduct stalls RNA polymerase II; CSB binds first, recruits CRL4CSA or CSA, and facilitates ELOF1-dependent UVSSA positioning. UVSSA helps inactivate stalled polymerase and recruit TFIIH; XPA, RPA, XPG, and XPF-ERCC1 then support verification, dual incision, repair synthesis, and ligation. | Patient cells, isogenic knockout cells, biochemistry, and structural biology; DOI: [10.1038/ng.2229](https://doi.org/10.1038/ng.2229) and [10.1101/707216](https://doi.org/10.1101/707216) (nakazawa2012mutationsinuvssa pages 19-22, muzammal2021themoleculargenetics pages 3-5, weegen2019thesequentialand pages 11-13) | UVSSA contains an N-terminal CSA-interacting region and a C-terminal TFIIH-interacting region around amino acids 400–500. | The pathway integrates multiple experimental systems. Some early models of RNAPII backtracking and degradation have been refined by later structural work. |
| 2024 structural advance | Cryo-EM and functional work showed that ELOF1 positions UVSSA and CRL4CSA on arrested Pol II, activating Pol II ubiquitylation. A TFIIS-like UVSSA element enters the Pol II pore and prevents TFIIS-mediated transcription reactivation, while other UVSSA regions promote TFIIH recruitment. | Structural, biochemical, immunoprecipitation, complementation, and nascent-RNA assays; February 2024; DOI: [10.1038/s41594-023-01207-0](https://doi.org/10.1038/s41594-023-01207-0) (kokic2024structuralbasisfor pages 11-11, kokic2024structuralbasisfor pages 9-11) | UVSSA zinc-finger and K414-site mutants could preserve Pol II ubiquitylation while reducing TFIIH interaction, separating polymerase inactivation from repair recruitment. | Primarily mechanistic work in reconstituted complexes and cultured cells, not a clinical or natural-history study; direct genotype-phenotype prediction remains uncertain. |
| 2024 interstrand-crosslink finding | UVSSA also facilitates transcription-coupled repair of DNA interstrand crosslinks: loss sensitized human cells to crosslinking agents, delayed repair, and impaired a single-ICL reporter; rescue required intact UVSSA-TFIIH interaction. | Human HAP1 and MCF10A cells, clonogenic assays, reporter repair, chromatin fractionation, co-immunoprecipitation, and proteomics; DOI: [10.1101/2023.05.10.538304](https://doi.org/10.1101/2023.05.10.538304) (liebau2024transcriptioncoupledrepairof pages 7-8, liebau2024transcriptioncoupledrepairof pages 5-7, liebau2024transcriptioncoupledrepairof pages 1-3) | UVSSA loss reduced reporter ICL-repair efficiency by approximately 50%; **F408A/V411A**, defective in TFIIH binding, failed to rescue. | Initially reported as a preprint; relevance to untreated UVSS patients and clinical crosslinker toxicity is unproven. |
| Management and trials | Care is preventive and supportive: rigorous UV avoidance, broad-spectrum sunscreen, UV-protective clothing and gloves, sunglasses, environmental UV controls, dermatologic surveillance, emollients, genetic counseling, and cascade testing. | Expert-review recommendations and photoprotection practice; DOI: [10.47391/JPMA.03-476](https://doi.org/10.47391/JPMA.03-476) (muzammal2021themoleculargenetics pages 1-2, muzammal2021themoleculargenetics pages 5-6) | No disease-modifying drug, gene therapy, validated pharmacogenomic strategy, response rate, or UVSS-specific interventional trial was identified. | Recommendations are extrapolated from pathophysiology and related photodermatoses rather than controlled UVSS trials. Topical corticosteroids should be used only for clinically indicated inflammation. |


*Table: Compact evidence table summarizing the phenotype, causal genes and variants, diagnostic cellular signature, TC-NER mechanism, 2024 mechanistic advances, and present management of UV-sensitive syndrome. Major evidence limitations and nomenclature issues are identified explicitly.*

## 1. Disease information

### Definition and nomenclature

UVSS is a hereditary photosensitivity syndrome in which defective repair of transcription-blocking DNA lesions produces an isolated or predominantly cutaneous phenotype. Common names include **UV-sensitive syndrome**, **ultraviolet-sensitive syndrome**, **UVSS**, and **UV-sensitive syndrome A/UVSS-A** for UVSSA-associated disease. Historical molecular subclasses are **UVSS1** (ERCC6), **UVSS2** (ERCC8), and **UVSS3/UVSS-A** (UVSSA). It is distinct from xeroderma pigmentosum (XP), CS, and photosensitive trichothiodystrophy (TTD). (spivak2015photosensitivehumansyndromes. pages 4-6, muzammal2021themoleculargenetics pages 1-2, nakazawa2012mutationsinuvssa pages 22-24)

### Identifiers

* **MONDO:** MONDO:0015797.
* **OMIM:** the retrieved literature uses **MIM 600630** for the UVSS phenotype. Gene-specific OMIM entries and current phenotype mappings should be verified directly in OMIM before ingestion.
* **Orphanet, MeSH, ICD-10/ICD-11:** no disease-specific identifiers were verified in the retrieved evidence. UVSS may be indexed under broader hereditary photosensitivity or DNA-repair-disorder categories; absence of a dedicated billing code should not be interpreted as absence of disease recognition.
* **Disease-target resources:** Open Targets associates MONDO:0015797 with **ERCC6, ERCC8, and UVSSA**, each supported by genetic and literature evidence. (OpenTargets Search: UV-sensitive syndrome)

This report is based on aggregated disease resources, published kindreds, individual case reports, patient-derived fibroblasts, and engineered cell systems—not longitudinal electronic-health-record data.

## 2. Etiology

### Causal factors and genetic risk

UVSS is caused by **germline biallelic pathogenic variants** affecting TC-NER:

* **UVSSA**—the most frequently reported UVSS gene; encodes ultraviolet-stimulated scaffold protein A.
* **ERCC8**—encodes CSA, a WD-repeat substrate receptor in the CRL4–DDB1 ubiquitin-ligase complex.
* **ERCC6**—encodes CSB, an ATP-dependent chromatin-remodeling/translocase factor recruited to lesion-stalled RNA polymerase II. (OpenTargets Search: UV-sensitive syndrome, muzammal2021themoleculargenetics pages 2-3, nakazawa2012mutationsinuvssa pages 22-24, li2019twonovelmutations pages 2-2)

Family history, parental consanguinity, and ancestry from a kindred carrying a pathogenic allele increase genetic risk, but UVSS is not restricted to one population. There is no evidence for polygenic susceptibility loci, modifier genes, anticipation, or a reproducible founder effect. Phenotypic divergence between UVSS and CS despite involvement of ERCC6 or ERCC8 indicates that allelic context and presently unresolved modifiers or repair-independent functions influence expressivity. This is a mechanistic inference, not an established modifier-gene model. (nakazawa2012mutationsinuvssa pages 22-24)

### Environmental and gene–environment interaction

Solar or artificial **ultraviolet radiation**, especially wavelengths that generate cyclobutane pyrimidine dimers and 6-4 photoproducts, is the essential environmental trigger. Genotype creates deficient TC-NER; UV exposure creates transcription-blocking lesions; together they produce acute sunburn and chronic pigmentary change. UV exposure does not cause the inherited disorder, but strongly controls manifestation and severity. There is no established contribution from smoking, diet, alcohol, exercise, occupational chemicals, or infection. (spivak2015photosensitivehumansyndromes. pages 4-6, muzammal2021themoleculargenetics pages 3-5)

### Protective factors

No protective allele has been established. Environmental protection consists of reducing UV dose through avoidance, clothing, sunscreens, UV-filtering eyewear, window films, and control of indoor UV sources. These measures reduce lesion formation rather than correcting the repair defect. (muzammal2021themoleculargenetics pages 1-2, muzammal2021themoleculargenetics pages 5-6)

**Suggested ontology/chemical annotations:** ultraviolet radiation; **CHEBI:17627** for nitrate or unrelated entities is not appropriate—UV is a physical exposure, not a chemical. Specific UV-photoproduct CHEBI identifiers should be ontology-validated before ingestion.

## 3. Phenotypes

| Phenotype | Type and course | Frequency/evidence | Suggested HPO term |
|---|---|---|---|
| Photosensitivity/exaggerated sunburn | Symptom/sign; usually recognized in childhood after sun exposure; recurrent and exposure-dependent | Core feature, but no defensible percentage | Photosensitivity (**HP:0000992**); exaggerated sunburn, ontology validation advised |
| Freckling or hyperpigmentation on exposed skin | Physical manifestation; chronic after repeated exposure | Common/core qualitative feature | Freckling (**HP:0001480**); abnormal skin pigmentation (**HP:0001000**) |
| Telangiectasia | Cutaneous sign; variable | Reported across cases | Telangiectasia (**HP:0001009**) |
| Xerosis/dry skin | Cutaneous sign; variable, generally mild | Repeatedly reported | Dry skin (**HP:0000958**) |
| Cellular UV hypersensitivity | Laboratory/cellular abnormality | Characteristic in tested patient fibroblasts | Cellular sensitivity to UV; exact HPO term should be validated |
| Defective recovery of RNA synthesis after UV | Functional laboratory abnormality | Characteristic TC-NER signature | No routinely used clinical HPO term; encode as assay result/GO annotation |
| Normal or near-normal global-genome repair | Negative laboratory discriminator | Characteristic relative to XP | Encode as diagnostic evidence, not a patient phenotype |
| Absence of progressive neurologic/developmental disease | Important negative finding | Distinguishes UVSS from CS | Do not encode absent phenotypes as positive associations |

The disease is generally mild and non-progressive systemically, while cutaneous injury is recurrent and cumulative with exposure. Available reports do not support intellectual disability, microcephaly, growth failure, sexual immaturity, premature aging, or internal-organ disease as typical UVSS manifestations. (spivak2015photosensitivehumansyndromes. pages 4-6, muzammal2021themoleculargenetics pages 2-3, muzammal2021themoleculargenetics pages 3-5)

No UVSS-specific EQ-5D, SF-36, PROMIS, disability, or work/school-participation study was identified. Likely burdens include activity restriction, heat and discomfort from protective clothing, anxiety about sunlight, cosmetic effects of pigmentary change, and recurrent painful burns; these are clinically plausible but have not been quantified in UVSS cohorts.

## 4. Genetic and molecular information

### Genes and selected published variants

* **ERCC6/CSB:** homozygous **c.229C>T (p.Arg77Ter)** was reported in two UVSS patients and produces severe N-terminal truncation or absence of CSB. Some secondary literature gives inconsistent cDNA numbering; annotation must be normalized to the selected MANE transcript. (nakazawa2012mutationsinuvssa pages 19-22, nakazawa2012mutationsinuvssa pages 22-24)
* **ERCC8/CSA:** reported UVSS alleles include homozygous **c.1083G>T (p.Trp361Cys)** and two variants reported in a Chinese patient, **c.582G>T** and **c.769G>A (p.Gly257Arg)**. The latter was reported below 0.01% in a Chinese population dataset. (nakazawa2012mutationsinuvssa pages 22-24, li2019twonovelmutations pages 2-2)
* **UVSSA:** published variants include **c.367A>T (p.Lys123Ter)**, **c.94T>C (p.Cys32Arg)**, **c.87delG (p.Ile31PhefsTer9)**, and **c.1040G>A**, reported as a codon-347 stop allele. Secondary sources disagree between p.Trp347Ter and p.Tyr347Ter, so the protein consequence must be re-derived from the transcript before database loading. (muzammal2021themoleculargenetics pages 1-2, muzammal2021themoleculargenetics pages 2-3)

These are germline variants. The prevailing consequence is loss of function, destabilization, defective partner binding, or failure to recruit the repair machinery. A uniform ACMG/AMP reassessment and current ClinVar/gnomAD query were not available from the retrieved evidence; therefore, historical disease attribution should not automatically be converted into a present-day “pathogenic” ClinVar assertion. No somatic cause, recurrent chromosomal abnormality, repeat expansion, mitochondrial variant, or disease-specific epigenetic signature is established.

### Modifier and epigenetic information

No validated modifier gene, protective allele, methylation signature, histone mark, or chromatin-level diagnostic biomarker has been demonstrated for UVSS. Ubiquitin and SUMO regulation are central post-translational mechanisms in TC-NER, but they are not inherited epigenetic causes. UVSSA interacts functionally with **USP7**, while CSA is part of **CRL4CSA**; these are pathway partners rather than established UVSS modifier genes. (kokic2024structuralbasisfor pages 11-11, weegen2019thesequentialand pages 11-13)

## 5. Environmental information

The major non-genetic determinant is cumulative UV exposure from sunlight, tanning devices, germicidal lamps, welding arcs, and other artificial sources. UV dose, wavelength, exposed surface area, and effectiveness of protection are expected to shape severity. No infectious agent or zoonotic process is involved. Evidence does not support diet, tobacco, alcohol, pollutants, or exercise as causal factors. Crosslinking chemicals and aldehydes are mechanistically relevant to the broader transcription-coupled-repair pathway, but their clinical importance in UVSS remains unproven. (liebau2024transcriptioncoupledrepairof pages 7-8, liebau2024transcriptioncoupledrepairof pages 1-3, liebau2024transcriptioncoupledrepairof pages 8-11)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic loss or dysfunction of UVSSA, CSA/ERCC8, or CSB/ERCC6 leads to defective assembly or function of the TC-NER complex.**
2. **UV exposure leads to bulky transcription-blocking DNA photoproducts in epidermal-cell nuclei.**
3. **A photoproduct on the transcribed strand leads to stalling of elongating RNA polymerase II (Pol II).**
4. **Stalled Pol II leads to CSB binding and displacement/reorganization of elongation factors.**
5. **CSB binding leads to recruitment of CRL4CSA; ELOF1 helps position CSA, UVSSA, and the ubiquitin ligase on arrested Pol II.**
6. **Correct complex positioning leads to Pol II ubiquitylation/inactivation; a TFIIS-like element of UVSSA enters the Pol II pore and prevents inappropriate TFIIS-mediated transcriptional restart.**
7. **UVSSA docking leads to recruitment and positioning of TFIIH; UVSSA-associated USP7 contributes to complex stability and deubiquitylation control.**
8. **TFIIH recruitment leads to local DNA opening, damage verification with XPA/RPA, and assembly of XPG and XPF–ERCC1.**
9. **Dual incision leads to removal of the lesion-containing oligonucleotide, followed by DNA synthesis and ligation, which leads to recovery of transcription.**
10. **In UVSS, failure at steps 4–7 leads to persistent transcription arrest, abnormal Pol II processing/degradation, stress signaling, and increased apoptosis after UV.**
11. **Loss of UV-exposed epidermal cells and repeated injury leads to acute sunburn; repeated exposure leads to freckling, pigmentary change, xerosis, and telangiectasia.** The final tissue-level link is biologically well supported but inferred from repair and clinical data rather than directly traced in patients. (spivak2015photosensitivehumansyndromes. pages 4-6, nakazawa2012mutationsinuvssa pages 19-22, muzammal2021themoleculargenetics pages 3-5, kokic2024structuralbasisfor pages 11-11, kokic2024structuralbasisfor pages 9-11, weegen2019thesequentialand pages 11-13)

### Upstream and downstream processes

Upstream events are lesion formation, Pol II arrest, CSB/CSA/ELOF1/UVSSA assembly, and ubiquitin regulation. Downstream events are TFIIH recruitment, helix opening, dual incision, repair synthesis, transcription recovery, and cell survival. Global-genome NER is comparatively preserved, explaining why UVSS is milder and apparently less cancer-prone than XP. Why UVSS lacks the neurodegeneration and progeria of CS remains incompletely resolved; authoritative interpretation favors additional transcriptional, mitochondrial, or repair-independent functions of CSA/CSB in CS rather than TC-NER deficiency alone. (spivak2015photosensitivehumansyndromes. pages 4-6, nakazawa2012mutationsinuvssa pages 22-24, li2019twonovelmutations pages 2-2)

### 2023–2024 advances

Kokic and colleagues used cryo-EM, biochemical assays, immunoprecipitation, mutant complementation, and nascent-RNA measurements to show that **ELOF1 acts as an adaptor positioning UVSSA and CRL4CSA**, and that the UVSSA TFIIS-like element blocks reactivation of arrested Pol II. Their abstract states: “**ELOF1 serves as an adaptor to stably position UVSSA and CRL4CSA on arrested Pol II**” and that a UVSSA element “**extends through the Pol II pore, thus preventing reactivation of Pol II by TFIIS**.” Published February 2024, DOI: https://doi.org/10.1038/s41594-023-01207-0. (kokic2024structuralbasisfor pages 11-11, kokic2024structuralbasisfor pages 9-11)

A 2024 human-cell study extended UVSSA function beyond canonical UV-photoproduct repair to transcription-coupled interstrand-crosslink repair. UVSSA loss reduced single-ICL reporter repair by approximately **50%**, and a TFIIH-binding-defective F408A/V411A UVSSA mutant failed to rescue. The preprint abstract states: “**Inactivation of UVSSA sensitizes human cells to ICL-inducing drugs, and delays ICL repair**.” Preprint posted in 2024, DOI: https://doi.org/10.1101/2023.05.10.538304. This finding is mechanistically important, but its relevance to untreated patients or drug toxicity is not established. (liebau2024transcriptioncoupledrepairof pages 7-8, liebau2024transcriptioncoupledrepairof pages 5-7, liebau2024transcriptioncoupledrepairof pages 1-3)

Recent work also distinguishes lesion-specific branches: CSA and CSB are required for transcription-coupled DNA–protein-crosslink repair, whereas downstream UVSSA and XPA are dispensable in at least one 2024 experimental system. Therefore, not every transcription-blocking lesion uses canonical UVSSA-dependent TC-NER.

### Suggested ontology terms

* **GO biological process:** transcription-coupled nucleotide-excision repair (**GO:0006283**); nucleotide-excision repair (**GO:0006289**); cellular response to UV; DNA repair; regulation of transcription by RNA polymerase II; protein ubiquitination; apoptotic process.
* **GO cellular component:** nucleus (**GO:0005634**); chromatin; RNA polymerase II elongation complex; nucleotide-excision-repair complex.
* **Cell Ontology:** keratinocyte (**CL:0000312**), epidermal cell, dermal fibroblast (**CL:0000057**, ontology context should be checked), melanocyte (**CL:0000148**).

No UVSS-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or clinical multi-omics signature has been validated. Proteomics and structural methods have mapped repair-complex interactions, but not a patient diagnostic signature.

## 7. Anatomical structures affected

The primary organ is the **skin**, especially chronically sun-exposed face, neck, hands, and forearms. The relevant tissues are epidermis and superficial dermis; likely target populations include keratinocytes, melanocytes, and dermal fibroblasts. Ocular surfaces may receive UV exposure, but a consistent UVSS-specific ocular phenotype was not established. No characteristic nervous-system, endocrine, cardiovascular, respiratory, renal, gastrointestinal, musculoskeletal, or immune involvement is supported. Lesions are exposure-distributed rather than inherently unilateral; exposed sites are generally bilateral but may be asymmetric according to behavior and shielding. (spivak2015photosensitivehumansyndromes. pages 4-6, muzammal2021themoleculargenetics pages 3-5)

**Suggested anatomy:** skin of body (**UBERON:0002097**), epidermis (**UBERON:0001003**), dermis (**UBERON:0002067**); nucleus (**GO:0005634**) and chromatin are the principal subcellular compartments. Exact regional UBERON identifiers should be validated before ingestion.

## 8. Temporal development

UVSS is congenital at the molecular level but generally becomes clinically evident in infancy or childhood after meaningful UV exposure. Onset is exposure-provoked rather than spontaneous. Acute episodes consist of exaggerated sunburn; freckling, dryness, and telangiectasia accumulate chronically. There are no validated disease stages. The underlying repair defect is lifelong, while manifestations can be markedly reduced by photoprotection. Spontaneous molecular remission does not occur; apparent clinical remission reflects reduced exposure. Childhood is a critical prevention period because early cumulative UV injury can be avoided. Quantitative progression rates and longitudinal natural-history cohorts are unavailable. (spivak2015photosensitivehumansyndromes. pages 4-6, muzammal2021themoleculargenetics pages 1-2)

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two carrier parents, the conventional per-pregnancy risks are 25% affected, 50% carrier, and 25% unaffected/non-carrier. Penetrance appears high for cellular UV sensitivity and photosensitivity among biallelic cases, but formal age-dependent penetrance has not been measured. Cutaneous expressivity is variable and strongly exposure-dependent. There is no evidence of anticipation. Germline mosaicism has not been documented but cannot be excluded in a family with an apparently de novo allele. (muzammal2021themoleculargenetics pages 1-2, muzammal2021themoleculargenetics pages 3-5)

The 2021 literature synthesis reported 18 patients from nine families across Japan, France, Israel, Iran, and Pakistan. Consanguinity contributed to ascertainment in some families, but no reliable ethnicity-specific prevalence, geographic incidence, carrier frequency, sex ratio, or age distribution exists. The published 1:100,000 estimate should be treated as conjectural; a case count this small is incompatible with precise worldwide prevalence estimation. (muzammal2021themoleculargenetics pages 1-2)

## 10. Diagnostics

### Recommended clinical workflow

1. Suspect UVSS in a child or adult with recurrent disproportionate sunburn, freckling or pigmentary change on exposed skin, but normal growth, cognition, neurologic examination, and development.
2. Document exposure timing, medications and porphyrin symptoms; perform complete skin and eye examinations and assess for CS, XP, and TTD features.
3. Order a hereditary photosensitivity/DNA-repair panel containing at minimum **UVSSA, ERCC8, and ERCC6**, preferably alongside XP/CS/TTD genes because of phenotypic overlap.
4. Confirm candidate variants by orthogonal sequencing and parental segregation; assess phase for compound heterozygosity.
5. If sequencing is negative but suspicion remains high, add deletion/duplication analysis, WES/WGS, transcript analysis, and—where available—functional testing in fibroblasts.

### Functional tests

Patient fibroblasts characteristically show reduced survival after 254-nm UV and deficient **recovery of RNA synthesis (RRS)**, with relatively preserved **unscheduled DNA synthesis (UDS)** or global photoproduct repair. Complementation can assign a repair group. These assays are highly informative but specialized, non-standardized across routine laboratories, and lack universal clinical cutoffs. (spivak2015photosensitivehumansyndromes. pages 4-6, nakazawa2012mutationsinuvssa pages 19-22, li2019twonovelmutations pages 2-2)

### Genetic technologies

A multigene panel is the efficient first test. Single-gene testing is appropriate only when a familial variant is known. WES identified UVSSA in the landmark study and is useful for panel-negative cases; WGS may detect deep-intronic, regulatory, or structural alleles but has no UVSS-specific validated yield. RNA sequencing can establish aberrant splicing in selected cases. CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion testing are not first-line unless independent clinical findings indicate them. Prenatal and preimplantation testing become technically feasible once familial pathogenic variants are established. (nakazawa2012mutationsinuvssa pages 19-22, nakazawa2012mutationsinuvssa pages 22-24)

### Differential diagnosis

* **Xeroderma pigmentosum:** defective global-genome NER, marked freckling, very high UV-induced skin-cancer risk, and sometimes neurologic disease; UDS is typically abnormal.
* **Cockayne syndrome:** photosensitivity plus growth failure, microcephaly, neurodevelopmental regression, cachectic/progeroid appearance, hearing/vision involvement, and other systemic disease; ERCC6/ERCC8 overlap requires clinical and functional correlation.
* **Photosensitive TTD:** brittle sulfur-deficient hair, ichthyosis, developmental abnormalities, and TFIIH-related disease.
* **Erythropoietic protoporphyria/other porphyrias:** painful photosensitivity, characteristic porphyrin abnormalities, and no TC-NER cellular signature.
* **Drug-induced phototoxicity, lupus, and polymorphous light eruption:** acquired or immune-mediated features and negative Mendelian/TC-NER work-up.

There are no universally accepted UVSS clinical criteria and no population or newborn screening program. Cascade testing of relatives is appropriate after molecular confirmation.

## 11. Outcome and prognosis

Published patients generally have mild, skin-limited disease without the shortened survival, neurodegeneration, or multisystem morbidity typical of CS. No 5-year or 10-year survival, mortality rate, or life-expectancy estimate exists. No tumor had been reported in the 2015 synthesis, and subsequent reviews continue to describe absent cancer predisposition; nevertheless, sparse case numbers and follow-up mean that routine dermatologic surveillance remains prudent. (spivak2015photosensitivehumansyndromes. pages 4-6, muzammal2021themoleculargenetics pages 1-2, muzammal2021themoleculargenetics pages 3-5)

Morbidity is dominated by painful burns, cumulative pigmentary change, strict lifestyle constraints, and potential psychosocial burden. Prognosis should improve with early, sustained photoprotection. No validated prognostic biomarker exists; likely determinants are cumulative UV dose, adherence to protection, and residual TC-NER function, but these have not been modeled quantitatively.

## 12. Treatment

There is no approved disease-modifying pharmacotherapy, gene therapy, RNA therapy, cell therapy, or surgical correction. Management is preventive and supportive:

* rigorous sunlight and artificial-UV avoidance;
* broad-spectrum, high-SPF sunscreen applied adequately and repeatedly;
* tightly woven/UV-rated clothing, hat, gloves, and UV-filtering glasses;
* UV-protective films and environmental UV measurement where feasible;
* emollients for xerosis;
* short courses of topical anti-inflammatory therapy only for clinically indicated dermatitis or burns;
* regular dermatologic examination and prompt biopsy of suspicious lesions;
* ophthalmologic review when ocular symptoms or substantial exposure occur;
* genetic counseling and family testing. (muzammal2021themoleculargenetics pages 1-2, muzammal2021themoleculargenetics pages 5-6)

No UVSS-specific treatment-response rates, adverse-event datasets, pharmacogenomic guidance, combination-treatment algorithm, or interventional ClinicalTrials.gov study was identified. Experimental UVSSA targeting in MYC-driven cancer and the association between UVSSA expression and crosslinker resistance are oncology applications, not treatments for UVSS. (liebau2024transcriptioncoupledrepairof pages 7-8, liebau2024transcriptioncoupledrepairof pages 8-11)

**Suggested NCIT concepts:** Sun Avoidance; Sunscreen; Protective Clothing; Genetic Counseling; Genetic Testing; Dermatologic Examination; Skin Biopsy. Exact NCIT codes should be validated against the current thesaurus.

## 13. Prevention

**Primary prevention of genotype** is not possible after conception. Reproductive options include carrier testing, partner testing, prenatal diagnosis, and preimplantation genetic testing for a known familial genotype. **Primary prevention of manifestations** is immediate lifelong UV minimization. **Secondary prevention** consists of early diagnosis, cascade testing, surveillance of exposed skin, and prompt evaluation of new lesions. **Tertiary prevention** consists of preventing recurrent burns, treating xerosis/inflammation, and mitigating psychosocial and educational restrictions. Vaccination and antimicrobial prophylaxis have no disease-specific role. Public-health measures include accurate UV-risk education and accommodation at school or work. (muzammal2021themoleculargenetics pages 1-2, muzammal2021themoleculargenetics pages 5-6)

## 14. Other species and natural disease

No naturally occurring veterinary disorder confidently equivalent to human UVSS was identified in the retrieved evidence. Orthologues of **UVSSA, ERCC8, and ERCC6** are evolutionarily conserved across mammals and many eukaryotes, supporting comparative study of transcription-coupled repair. UVSS is noninfectious and has no transmission or zoonotic potential. NCBI Taxonomy identifiers relevant to laboratory work include **Homo sapiens 9606** and **Mus musculus 10090**. Species-specific NCBI Gene and VBO breed identifiers require direct database verification.

## 15. Model organisms and experimental models

The strongest disease-relevant systems are:

* **Primary patient dermal fibroblasts:** reproduce UV hypersensitivity, abnormal RRS, preserved relative UDS, defective Pol II processing, and genetic complementation. They offer the closest ex-vivo model but do not reproduce whole-skin architecture or lifetime exposure. (spivak2015photosensitivehumansyndromes. pages 4-6, nakazawa2012mutationsinuvssa pages 19-22)
* **Isogenic UVSSA-, ERCC8-, or ERCC6-knockout human cells:** define assembly order and permit rescue by wild-type or mutant proteins. Limitations include transformed-cell context and acute experimental UV doses. (kokic2024structuralbasisfor pages 11-11, kokic2024structuralbasisfor pages 9-11, weegen2019thesequentialand pages 11-13)
* **Reconstituted biochemical and cryo-EM complexes:** resolve ELOF1, CRL4CSA, UVSSA, Pol II, and TFIIH interfaces at high resolution but cannot model tissue inflammation, pigmentation, or clinical severity. (kokic2024structuralbasisfor pages 11-11, kokic2024structuralbasisfor pages 9-11)
* **HAP1 and MCF10A UVSSA-knockout cells with single-ICL reporters:** showed approximately 50% loss of ICL-repair efficiency and established dependence on UVSSA–TFIIH binding. These model an expanded repair function, not the natural cutaneous syndrome. (liebau2024transcriptioncoupledrepairof pages 7-8, liebau2024transcriptioncoupledrepairof pages 5-7)

Mouse models of broader TCR and aldehyde-clearance defects demonstrate transcription-associated endogenous damage, but a validated mouse model reproducing the isolated mild human UVSS phenotype was not established by the retrieved evidence. No natural canine, livestock, zebrafish, Drosophila, or C. elegans UVSS counterpart was confirmed.

## Evidence-quality assessment and knowledge-base cautions

The causal-gene and cellular-repair assignments are strong because they combine human segregation, patient fibroblasts, complementation, and mechanistic experiments. Clinical frequency and prognosis evidence are weak because the literature contains very few patients, heterogeneous follow-up, and no registry. The frequently repeated “no cancer” statement means **no established excess has been observed**, not that excess risk has been statistically excluded. Likewise, the quoted prevalence of 1:100,000 is not a defensible epidemiologic statistic. Variant HGVS, current ClinVar classification, gnomAD frequency, HGNC IDs, and some ontology codes should be validated directly against current reference databases before production ingestion.

### Key source URLs and dates

* Nakazawa et al., *Nature Genetics*, April 2012: https://doi.org/10.1038/ng.2229. Landmark human-genetic identification of UVSSA and patient-cell mechanism. (nakazawa2012mutationsinuvssa pages 19-22, nakazawa2012mutationsinuvssa pages 22-24)
* Horibata et al., *PNAS*, October 2004: https://doi.org/10.1073/pnas.0404587101. ERCC6/CSB absence associated with UVSS rather than classic CS.
* Spivak and Hanawalt, *Mutation Research*, June 2015: https://doi.org/10.1016/j.mrfmmm.2014.11.003. Authoritative clinical/mechanistic review. (spivak2015photosensitivehumansyndromes. pages 4-6)
* Li et al., *Acta Dermato-Venereologica*, January 2019: https://doi.org/10.2340/00015555-3032. ERCC8-associated UVSS case and variants. (li2019twonovelmutations pages 2-2)
* Muzammal et al., *Journal of the Pakistan Medical Association*, July 2021: https://doi.org/10.47391/JPMA.03-476. Case-count, phenotype, variant, and management synthesis. (muzammal2021themoleculargenetics pages 1-2, muzammal2021themoleculargenetics pages 2-3, muzammal2021themoleculargenetics pages 3-5, muzammal2021themoleculargenetics pages 5-6)
* Kokic et al., *Nature Structural & Molecular Biology*, February 2024: https://doi.org/10.1038/s41594-023-01207-0. Structural basis of ELOF1/UVSSA/CRL4CSA-mediated Pol II inactivation. (kokic2024structuralbasisfor pages 11-11, kokic2024structuralbasisfor pages 9-11)
* Liebau et al., 2024 preprint: https://doi.org/10.1101/2023.05.10.538304. UVSSA in transcription-coupled interstrand-crosslink repair. (liebau2024transcriptioncoupledrepairof pages 7-8, liebau2024transcriptioncoupledrepairof pages 5-7, liebau2024transcriptioncoupledrepairof pages 1-3)

PMIDs explicitly recoverable from the disease-target evidence include **22466610, 22466611, and 22466612** for the 2012 UVSSA discovery series; **15486090** for the ERCC6/UVSS report; **19329487** and **25655951** for ERCC8/TC-NER-related evidence. These identifiers should be reconciled to titles in PubMed before automated import. (OpenTargets Search: UV-sensitive syndrome)

References

1. (spivak2015photosensitivehumansyndromes. pages 4-6): Graciela Spivak and Philip C. Hanawalt. Photosensitive human syndromes. Mutation research, 776:24-30, Jun 2015. URL: https://doi.org/10.1016/j.mrfmmm.2014.11.003, doi:10.1016/j.mrfmmm.2014.11.003. This article has 34 citations and is from a peer-reviewed journal.

2. (muzammal2021themoleculargenetics pages 1-2): Muhammad Muzammal, Muhammad Zeeshan Ali, Safeer Ahmad, Shawana Huma, Rizwan, Sohail Ahmad, Ansar Ahmad Abbasi, Saadullah Khan, and Muzammil Ahmad Khan. The molecular genetics of uv-sensitive syndrome; a rare dermal anomaly. Jul 2021. URL: https://doi.org/10.47391/jpma.03-476, doi:10.47391/jpma.03-476. This article has 14 citations.

3. (li2019twonovelmutations pages 2-2): Yue Li, Luyao Zheng, Fuying Chen, Z. Yao, and Ming Li. Two novel mutations in the ercc8 gene in a patient with ultraviolet-sensitive syndrome. Acta dermato-venereologica, 99 1:117-118, Jan 2019. URL: https://doi.org/10.2340/00015555-3032, doi:10.2340/00015555-3032. This article has 3 citations and is from a domain leading peer-reviewed journal.

4. (muzammal2021themoleculargenetics pages 3-5): Muhammad Muzammal, Muhammad Zeeshan Ali, Safeer Ahmad, Shawana Huma, Rizwan, Sohail Ahmad, Ansar Ahmad Abbasi, Saadullah Khan, and Muzammil Ahmad Khan. The molecular genetics of uv-sensitive syndrome; a rare dermal anomaly. Jul 2021. URL: https://doi.org/10.47391/jpma.03-476, doi:10.47391/jpma.03-476. This article has 14 citations.

5. (nakazawa2012mutationsinuvssa pages 19-22): Yuka Nakazawa, Kensaku Sasaki, Norisato Mitsutake, Michiko Matsuse, Mayuko Shimada, Tiziana Nardo, Yoshito Takahashi, Kaname Ohyama, Kosei Ito, Hiroyuki Mishima, Masayo Nomura, Akira Kinoshita, Shinji Ono, Katsuya Takenaka, Ritsuko Masuyama, Takashi Kudo, Hanoch Slor, Atsushi Utani, Satoshi Tateishi, Shunichi Yamashita, Miria Stefanini, Alan R Lehmann, Koh-ichiro Yoshiura, and Tomoo Ogi. Mutations in uvssa cause uv-sensitive syndrome and impair rna polymerase iio processing in transcription-coupled nucleotide-excision repair. Nature Genetics, 44:586-592, Apr 2012. URL: https://doi.org/10.1038/ng.2229, doi:10.1038/ng.2229. This article has 246 citations and is from a highest quality peer-reviewed journal.

6. (nakazawa2012mutationsinuvssa pages 22-24): Yuka Nakazawa, Kensaku Sasaki, Norisato Mitsutake, Michiko Matsuse, Mayuko Shimada, Tiziana Nardo, Yoshito Takahashi, Kaname Ohyama, Kosei Ito, Hiroyuki Mishima, Masayo Nomura, Akira Kinoshita, Shinji Ono, Katsuya Takenaka, Ritsuko Masuyama, Takashi Kudo, Hanoch Slor, Atsushi Utani, Satoshi Tateishi, Shunichi Yamashita, Miria Stefanini, Alan R Lehmann, Koh-ichiro Yoshiura, and Tomoo Ogi. Mutations in uvssa cause uv-sensitive syndrome and impair rna polymerase iio processing in transcription-coupled nucleotide-excision repair. Nature Genetics, 44:586-592, Apr 2012. URL: https://doi.org/10.1038/ng.2229, doi:10.1038/ng.2229. This article has 246 citations and is from a highest quality peer-reviewed journal.

7. (muzammal2021themoleculargenetics pages 2-3): Muhammad Muzammal, Muhammad Zeeshan Ali, Safeer Ahmad, Shawana Huma, Rizwan, Sohail Ahmad, Ansar Ahmad Abbasi, Saadullah Khan, and Muzammil Ahmad Khan. The molecular genetics of uv-sensitive syndrome; a rare dermal anomaly. Jul 2021. URL: https://doi.org/10.47391/jpma.03-476, doi:10.47391/jpma.03-476. This article has 14 citations.

8. (weegen2019thesequentialand pages 11-13): Yana van der Weegen, Hadar Golan Berman, Tycho E.T. Mevissen, Katja Apelt, Román González-Prieto, Elisheva Heilbrun, Alfred C.O. Vertegaal, Diana van den Heuvel, Johannes C. Walter, Sheera Adar, and Martijn S. Luijsterburg. The sequential and cooperative action of csb, csa and uvssa targets the tfiih complex to dna damage-stalled rna polymerase ii. bioRxiv, Jul 2019. URL: https://doi.org/10.1101/707216, doi:10.1101/707216. This article has 5 citations.

9. (kokic2024structuralbasisfor pages 11-11): Goran Kokic, George Yakoub, Diana van den Heuvel, Annelotte P. Wondergem, Paula J. van der Meer, Yana van der Weegen, Aleksandar Chernev, Isaac Fianu, Thornton J. Fokkens, Sonja Lorenz, Henning Urlaub, Patrick Cramer, and Martijn S. Luijsterburg. Structural basis for rna polymerase ii ubiquitylation and inactivation in transcription-coupled repair. Nature Structural & Molecular Biology, 31:536-547, Feb 2024. URL: https://doi.org/10.1038/s41594-023-01207-0, doi:10.1038/s41594-023-01207-0. This article has 64 citations and is from a highest quality peer-reviewed journal.

10. (kokic2024structuralbasisfor pages 9-11): Goran Kokic, George Yakoub, Diana van den Heuvel, Annelotte P. Wondergem, Paula J. van der Meer, Yana van der Weegen, Aleksandar Chernev, Isaac Fianu, Thornton J. Fokkens, Sonja Lorenz, Henning Urlaub, Patrick Cramer, and Martijn S. Luijsterburg. Structural basis for rna polymerase ii ubiquitylation and inactivation in transcription-coupled repair. Nature Structural & Molecular Biology, 31:536-547, Feb 2024. URL: https://doi.org/10.1038/s41594-023-01207-0, doi:10.1038/s41594-023-01207-0. This article has 64 citations and is from a highest quality peer-reviewed journal.

11. (liebau2024transcriptioncoupledrepairof pages 7-8): Rowyn C Liebau, Crystal Waters, Arooba Ahmed, Rajesh K Soni, and Jean Gautier. Transcription-coupled repair of dna interstrand crosslinks by uvssa. bioRxiv, May 2024. URL: https://doi.org/10.1101/2023.05.10.538304, doi:10.1101/2023.05.10.538304. This article has 4 citations.

12. (liebau2024transcriptioncoupledrepairof pages 5-7): Rowyn C Liebau, Crystal Waters, Arooba Ahmed, Rajesh K Soni, and Jean Gautier. Transcription-coupled repair of dna interstrand crosslinks by uvssa. bioRxiv, May 2024. URL: https://doi.org/10.1101/2023.05.10.538304, doi:10.1101/2023.05.10.538304. This article has 4 citations.

13. (liebau2024transcriptioncoupledrepairof pages 1-3): Rowyn C Liebau, Crystal Waters, Arooba Ahmed, Rajesh K Soni, and Jean Gautier. Transcription-coupled repair of dna interstrand crosslinks by uvssa. bioRxiv, May 2024. URL: https://doi.org/10.1101/2023.05.10.538304, doi:10.1101/2023.05.10.538304. This article has 4 citations.

14. (muzammal2021themoleculargenetics pages 5-6): Muhammad Muzammal, Muhammad Zeeshan Ali, Safeer Ahmad, Shawana Huma, Rizwan, Sohail Ahmad, Ansar Ahmad Abbasi, Saadullah Khan, and Muzammil Ahmad Khan. The molecular genetics of uv-sensitive syndrome; a rare dermal anomaly. Jul 2021. URL: https://doi.org/10.47391/jpma.03-476, doi:10.47391/jpma.03-476. This article has 14 citations.

15. (OpenTargets Search: UV-sensitive syndrome): Open Targets Query (UV-sensitive syndrome, 3 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

16. (liebau2024transcriptioncoupledrepairof pages 8-11): Rowyn C Liebau, Crystal Waters, Arooba Ahmed, Rajesh K Soni, and Jean Gautier. Transcription-coupled repair of dna interstrand crosslinks by uvssa. bioRxiv, May 2024. URL: https://doi.org/10.1101/2023.05.10.538304, doi:10.1101/2023.05.10.538304. This article has 4 citations.

## Artifacts

- [Edison artifact artifact-00](UV-Sensitive_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0015797` (4 mentions) - the report calls it "if available"; MONDO calls it **UV-sensitive syndrome**