---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-17T21:38:38.620543'
end_time: '2026-09-17T21:54:36.376061'
duration_seconds: 957.76
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Quebec Platelet Disorder
  mondo_id: MONDO:0011136
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 45
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 17
  verified: 13
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0011136
    reported_labels:
    - if available
    ontology_label: Quebec platelet disorder
  labels_variant: 1
  unresolvable_prefixes:
  - OMIM
  - Gene
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Quebec_Platelet_Disorder-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Quebec Platelet Disorder
- **MONDO ID:** MONDO:0011136 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Quebec Platelet Disorder** covering all of the
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
- **Disease Name:** Quebec Platelet Disorder
- **MONDO ID:** MONDO:0011136 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Quebec Platelet Disorder** covering all of the
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


# Quebec Platelet Disorder: Disease-Characteristics Research Report

## Executive summary

Quebec platelet disorder (QPD) is a very rare, nonsyndromic, autosomal-dominant platelet disorder in which a germline tandem duplication encompassing **PLAU** rewires local chromatin architecture. During megakaryopoiesis, the duplicated PLAU copy adopts a neighboring hematopoietic enhancer, causing more than 100-fold excess expression of otherwise normal urokinase-type plasminogen activator (uPA). Platelet-localized uPA generates plasmin, degrades α-granule proteins, and accelerates fibrinolysis at sites of platelet activation without generalized systemic hyperfibrinolysis. The clinical signature is variably severe, often delayed bleeding after dental work, surgery, trauma, or deep cuts; hemarthrosis and spontaneous hematuria are unusually common for a platelet disorder. Tranexamic acid is the principal treatment, although evidence is observational rather than trial-based. (hayward2017theduplicationmutation pages 1-2, hayward2017theduplicationmutation pages 2-3, mckay2004bleedingrisksassociated pages 1-2, liang2020enhancergenerewiringin pages 15-16)

The following table provides the central knowledge-base facts.

| Knowledge-base field | Curated finding | Ontology / identifier suggestions | Key evidence |
|---|---|---|---|
| Identity and inheritance | Quebec platelet disorder (QPD) is a rare, nonsyndromic, autosomal-dominant inherited platelet-function disorder characterized by a platelet-dependent gain of fibrinolytic function without systemic hyperfibrinolysis. Historical names include **factor V Quebec**, **Quebec platelet syndrome**, and **platelet disorder, Quebec type**. | MONDO:0011136; OMIM:601709; disease class: inherited platelet function disorder | QPD is described as autosomal dominant and associated with excess platelet urokinase and α-granule proteolysis (DOI: 10.1182/blood-2003-11-4077). (mckay2004bleedingrisksassociated pages 1-2, blavignac12011quebecplateletdisorder pages 1-2) |
| Causal gene and variant | The established causal lesion is a **germline direct tandem duplication of approximately 78 kb at chromosome 10q22**, encompassing **PLAU** and C10orf55. Reported GRCh37/hg19 coordinates are **chr10:75,659,017–75,736,956**. All 38 tested affected subjects carried the duplication; it was absent from 114 unaffected relatives and 311 unrelated controls. | PLAU; HGNC:9052; NCBI Gene:5328; Ensembl:ENSG00000122861; structural variant/copy-number gain; germline; autosomal dominant | Paterson et al., *Blood*, online 9 Dec 2009/print Feb 2010, PMID:20007542, DOI:10.1182/blood-2009-07-233965; Open Targets recognizes PLAU–QPD association. (OpenTargets Search: Quebec platelet disorder-PLAU, blavignac12011quebecplateletdisorder pages 2-3, paterson2010personswithquebec pages 3-4, liang2020enhancergenerewiringin pages 10-12) |
| Variant interpretation | The duplication is disease-causing by **regulatory gain of function**, not by changing the uPA protein sequence. It produces excessive normal PLAU transcripts from the duplicated disease chromosome. Because it is a recurrent founder structural variant, breakpoint-specific testing is more informative than routine coding-region sequencing. | ACMG/AMP concept: pathogenic copy-number gain; molecular consequence: ectopic enhancer adoption / increased gene expression | Human megakaryocyte evidence: Hayward et al., 16 Mar 2017, PMID:28301587, DOI:10.1371/journal.pone.0173991. (hayward2017theduplicationmutation pages 1-2, hayward2017theduplicationmutation pages 2-3, hayward2017theduplicationmutation pages 16-17) |
| Upstream molecular effect | The duplication crosses the normal boundary between **subTADPLAU** and **subTADVCL**, repositioning one PLAU copy near the hematopoietic enhancer **ENHQPD**. Disease-chromosome PLAU contacts ENHQPD preferentially; allele-specific 4C reads were approximately 88–92% disease allele versus 66.6% expected from copy number alone. PLAU also gains H3K36me3 and loses promoter H3K27me3. | GO suggestions: regulation of transcription by RNA polymerase II; chromatin organization; enhancer–promoter interaction. Cell: megakaryocyte (CL:0000556). | Liang et al., *Blood*, Jul 2020, DOI:10.1182/blood.2020005394. (liang2020enhancergenerewiringin pages 10-12, liang2020enhancergenerewiringin pages 6-7, liang2020enhancergenerewiringin pages 13-14, liang2020enhancergenerewiringin pages 15-16) |
| Enhancer evidence | ENHQPD is a 5.7-kb megakaryocyte-enriched H3K27ac element about 50 kb from both PLAU and VCL; its approximately 375-bp conserved module binds/associates with FLI1, GATA1, RUNX1, and TAL1. It enhanced PLAU-promoter reporter activity 2.4-fold in K562 cells and was active in cultured human megakaryocytes and thrombocyte-forming zebrafish tissues. | GO suggestions: hematopoietic transcriptional regulation; megakaryocyte differentiation. Model taxon: *Danio rerio* (NCBI Taxon:7955). | DOI:10.1182/blood.2020005394. (liang2020enhancergenerewiringin pages 12-13, liang2020enhancergenerewiringin pages 13-14) |
| Downstream molecular effect | Megakaryocyte PLAU expression and platelet urokinase-type plasminogen activator (uPA) stores increase by **more than 100-fold**. Excess uPA is stored in platelet α-granules, released upon activation, and converts plasminogen to plasmin locally. Plasma and urine uPA and systemic fibrinolysis are generally not increased. | Protein: urokinase plasminogen activator; GO:0042730 fibrinolysis; platelet α-granule (GO:0031091); platelet (CL:0000233); plasminogen activation | Human and patient-derived-cell evidence, DOI:10.1371/journal.pone.0173991. (diamandis2009biochemicalandgenetic pages 129-133, hayward2017theduplicationmutation pages 1-2, hayward2017theduplicationmutation pages 2-3, hayward2017theduplicationmutation pages 6-9) |
| Platelet pathology | Intraplatelet plasmin causes proteolysis or loss of α-granule proteins including fibrinogen, factor V, von Willebrand factor, thrombospondin-1, multimerin-1, osteonectin, and P-selectin. Released uPA accelerates platelet-dependent clot lysis, explaining delayed rebleeding after an initially formed hemostatic plug. | HPO suggestion: Abnormality of platelet function; GO suggestions: platelet degranulation, proteolysis, fibrinolysis; platelet α-granule (GO:0031091) | Protein degradation and diagnostic patterns are summarized in disease-focused laboratory evidence. (hayward2017theduplicationmutation pages 2-3, hayward2017theduplicationmutation pages 16-17, diamandis2009biochemicalandgenetica pages 80-83) |
| Hallmark bleeding phenotype | Bleeding is lifelong but variably expressed and commonly appears **12 hours to 4 days after trauma, surgery, dental extraction, or deep cuts**. Episodes can persist for days or weeks without antifibrinolytic therapy. | HPO suggestions: Abnormal bleeding; Prolonged bleeding following procedure; Delayed wound healing | Disease-focused review and family cohort. (diamandis2009biochemicalandgenetica pages 66-69, diamandis2009biochemicalandgenetic pages 66-69, blavignac12011quebecplateletdisorder pages 1-2) |
| Quantified phenotypes | In 23 affected relatives: post-dental-extraction bleeding longer than 24 h occurred in **94% (16/17; OR 176)**; epistaxis in **57% (13/23; OR 4.0)**; prolonged deep-cut bleeding in **56% (9/16; OR 37)**; hematuria in **50% (11/22; OR 7.7)**; joint bleeding in **43% (10/23)**; impaired healing in **26% (6/23; OR 4.9)**; and prior transfusion in **52% (12/23; OR 9.8)**. | HPO: Epistaxis (HP:0000421); Hematuria (HP:0000790); Bruising susceptibility (HP:0000978); Menorrhagia (HP:0000132); Hemarthrosis; Delayed wound healing | McKay et al., *Blood*, 1 Jul 2004, DOI:10.1182/blood-2003-11-4077. (mckay2004bleedingrisksassociated pages 3-4, mckay2004bleedingrisksassociated pages 4-5, diamandis2009biochemicalandgenetica pages 69-72) |
| Hematologic laboratory phenotype | Platelet counts are typically low-normal or mildly reduced—about 50% lower than in unaffected relatives. In one cohort, counts were **120–245 ×10⁹/L** (mean 167), while platelet uPA was **142–575 ng/10⁹ platelets** (mean 275; unaffected reference below 1.3). Bleeding score did not correlate strongly with platelet count or uPA level. | HPO: Thrombocytopenia (HP:0001873); laboratory abnormality: increased platelet uPA | Human family study. (blavignac12011quebecplateletdisorder pages 2-3, mckay2004bleedingrisksassociated pages 4-5, blavignac12011quebecplateletdisorder pages 1-2) |
| Diagnostic hallmarks | PT/INR, aPTT, systemic-fibrinolysis assays, and thromboelastography are usually normal. Aggregometry often shows reduced primary and absent secondary aggregation with epinephrine, but responses can vary and are not specific. Specialized findings are markedly increased platelet uPA and characteristic α-granule-protein degradation. **Definitive testing** is breakpoint PCR or another validated assay that detects the PLAU tandem duplication. | Diagnostic terms: CBC/platelet count; light-transmission aggregometry; platelet uPA immunoassay; immunoblot; copy-number/structural-variant testing | QPD review and modern platelet-diagnostic review, DOI:10.1055/s-0031-1291382 and DOI:10.1080/10408363.2022.2049199. (blavignac12011quebecplateletdisorder pages 4-6, wilson2023preoperativediagnosisand pages 6-7) |
| Genetic-testing implications | Targeted breakpoint PCR is preferred for known-family testing and can be applied to cord blood. WES may miss the duplication because it is noncoding/structural; WGS or CNV-aware panels may detect it if the pipeline is validated. Routine karyotyping is too low-resolution; CMA could detect a 78-kb gain only if probe coverage is adequate, while FISH is generally unnecessary. Cascade testing is appropriate for at-risk relatives, including minimally symptomatic children. | NCIT suggestions: Genetic Testing; Polymerase Chain Reaction; Whole Genome Sequencing; Copy Number Variation Analysis; Genetic Counseling | Breakpoint-testing and family-screening recommendations derive from disease-focused reviews; sequencing-platform limitations are technical inferences and require laboratory validation. (diamandis2009biochemicalandgenetica pages 80-83, blavignac12011quebecplateletdisorder pages 4-6) |
| Treatment | **Tranexamic acid** is first-line for treatment and peri-procedural prevention; ε-aminocaproic acid is a less-potent alternative. Reported durations are approximately 3–4 days for minor bleeding/surgery, 4–5 days after dental extraction, 5–7 days after major trauma/surgery or joint bleeding, and 10–14 days for intracranial bleeding. | CHEBI:48669 tranexamic acid; NCIT suggestions: Tranexamic Acid; Aminocaproic Acid; Antifibrinolytic Therapy | Observational human evidence: all 19 affected individuals challenged without an antifibrinolytic reported excessive bleeding, whereas all 12 treated during some/all challenges reported no serious bleeding. DOI:10.1182/blood-2003-11-4077. (blavignac12011quebecplateletdisorder pages 6-6, mckay2004bleedingrisksassociated pages 4-5, diamandis2009biochemicalandgenetica pages 69-72) |
| Treatments generally ineffective / cautions | Platelet or plasma transfusion and desmopressin do not correct the underlying platelet-localized fibrinolysis and are reported as ineffective for typical QPD bleeding. Spontaneous hematuria usually resolves without antifibrinolytics. Antifibrinolytics require individualized thrombosis-risk assessment; QPD does not eliminate venous-thromboembolism risk. | NCIT suggestions: Platelet Transfusion; Plasma Transfusion; Desmopressin; Thrombosis Prophylaxis | Disease-focused clinical experience and family cohort. (mckay2004bleedingrisksassociated pages 5-6, diamandis2009biochemicalandgenetica pages 80-83, diamandis2009biochemicalandgenetic pages 80-83) |
| Epidemiology and founder effect | Most documented cases descend from a founder family from the Sorel/Yamaska/St-François-du-Lac region of Quebec. Historical estimates are approximately **1:220,000 in Quebec** and **1:655,000 in Canada**, probably underestimates; no robust incidence, sex-ratio, global prevalence, or carrier-frequency estimate exists. | Population descriptor: French Canadian founder population | QPD review. (blavignac12011quebecplateletdisorder pages 2-3) |
| Penetrance and expressivity | Molecular penetrance appears high, but clinical expressivity is strongly variable and exposure-dependent. Young carriers may have low bleeding scores before surgery, trauma, dental extraction, menstruation, or childbirth. No genetic anticipation or established modifier gene is known. | HPO suggestion: Variable expressivity | The cohort included ages 1–89 years; two affected children aged 3 and 6 had bleeding scores below 2. (mckay2004bleedingrisksassociated pages 1-2, mckay2004bleedingrisksassociated pages 4-5) |
| Prognosis and morbidity | QPD is chronic and lifelong; quantitative survival or life-expectancy data are unavailable. With recognition and antifibrinolytic prophylaxis, major challenge-related bleeding is often preventable. Morbidity includes transfusions, lifestyle restriction, delayed healing, destructive arthropathy from recurrent hemarthroses, anemia, compartment bleeding, and rare intracranial hemorrhage. | HPO suggestions: Anemia; Hemarthrosis; Intracranial hemorrhage; Arthropathy | Human cohort and expert review. (mckay2004bleedingrisksassociated pages 2-3, mckay2004bleedingrisksassociated pages 5-6, blavignac12011quebecplateletdisorder pages 1-2) |
| Evidence gaps / current status | Searches identified no QPD-specific interventional clinical trial and no approved disease-modifying, gene, RNA, or cell therapy. No established environmental cause, protective allele, modifier gene, pharmacogenomic rule, single-cell/spatial-omics study, validated prognostic biomarker, or naturally occurring nonhuman QPD is reported. The principal advanced datasets remain patient-derived RNA-seq, ChIP-seq and 4C-seq; 2023–2024 publications mainly review inherited platelet-disorder diagnosis/management rather than report new QPD-specific cohorts or therapies. | Research-gap annotations: natural history study; clinical trial; single-cell transcriptomics; gene therapy | Recent expert literature continues to classify QPD as an inherited platelet disorder and emphasizes comprehensive platelet-function plus genetic testing; disease-specific evidence remains dominated by small founder-family studies. (wilson2023preoperativediagnosisand pages 6-7, liang2020enhancergenerewiringin pages 23-24, hayward2017theduplicationmutation pages 16-17, liang2020enhancergenerewiringin pages 12-13) |


*Table: Compact disease knowledge-base table integrating the causal PLAU duplication, enhancer-rewiring mechanism, quantified clinical manifestations, diagnostic approach, treatment, epidemiology, ontology suggestions, and major evidence gaps.*

## 1. Disease information

**Definition.** QPD is an inherited qualitative platelet disorder and platelet-dependent gain-of-function fibrinolytic disease. It is not a systemic plasminogen-activation disorder: plasma/urinary uPA and systemic fibrinolysis are generally normal. Historical terminology includes **factor V Quebec**, reflecting its initial attribution to deficient platelet factor V; other names include **Quebec platelet syndrome**, **platelet disorder, Quebec type**, and **autosomal dominant platelet disorder with urokinase overexpression**. (diamandis2009biochemicalandgenetic pages 129-133, mckay2004bleedingrisksassociated pages 1-2)

**Identifiers.** The supplied and Open Targets disease identifier is **MONDO:0011136**; Open Targets links it exclusively to **PLAU** (Ensembl ENSG00000122861), supported by five evidence records including PMID 20007542 and PMID 28301587. Commonly cited database identifiers are **OMIM 601709** and Orphanet’s Quebec platelet disorder entry. There is no disease-specific ICD-10/ICD-11 or MeSH code evident in the retrieved literature; coding ordinarily falls under inherited platelet-function/hemorrhagic disorders. (OpenTargets Search: Quebec platelet disorder-PLAU)

The evidence base is predominantly **aggregated disease-level literature derived from one large French-Canadian founder pedigree**, supplemented by individual case reports and experiments on participant-derived cells. It is not an EHR-derived population dataset. The pivotal clinical study included 127 relatives—23 affected and 104 unaffected—and therefore provides family-level rather than population-representative estimates. (mckay2004bleedingrisksassociated pages 1-2, mckay2004bleedingrisksassociated pages 3-4)

## 2. Etiology, risk, protective factors, and gene–environment interaction

The primary cause is genetic: a heterozygous, germline, direct tandem duplication of approximately 78 kb on chromosome 10q that encompasses **PLAU** and C10orf55. All 38 tested affected subjects carried the duplication; it was absent from 114 unaffected relatives and 311 unrelated controls. The disease effect is regulatory gain of function rather than alteration of uPA amino-acid sequence. (blavignac12011quebecplateletdisorder pages 2-3, paterson2010personswithquebec pages 3-4)

Inheritance of the duplication is the principal risk factor. Family history and French-Canadian ancestry from the Sorel/Yamaska/St-François-du-Lac region increase prior probability. No validated susceptibility locus, modifier gene, protective allele, environmental cause, toxin, diet, infection, or lifestyle cause has been demonstrated. The suggestion that other hemorrhagic or prothrombotic traits may modify expression is plausible but unproven. (blavignac12011quebecplateletdisorder pages 2-3, mckay2004bleedingrisksassociated pages 5-6)

The clinically important gene–environment interaction is exposure to a **hemostatic challenge**: surgery, dental extraction, trauma, deep cuts, menstruation, or childbirth can uncover a previously mild phenotype. Avoidance of high-trauma activity reduces exposure but is not biological protection and may impair quality of life. Antifibrinolytic therapy is an effective pharmacologic protective factor during challenges. (mckay2004bleedingrisksassociated pages 2-3, mckay2004bleedingrisksassociated pages 4-5)

## 3. Phenotypes

QPD is congenital and lifelong, but manifestations are episodic and exposure-dependent. In the controlled family study, the mean age was 34 years and range 1–89 years; two affected children aged three and six had bleeding scores below two, illustrating that absence of early bleeding does not imply nonpenetrance. Mean bleeding scores were 8.0±3.9 in affected versus 1.6±1.9 in unaffected relatives (P<0.0001). (mckay2004bleedingrisksassociated pages 1-2, mckay2004bleedingrisksassociated pages 4-5)

* **Delayed/prolonged procedural bleeding:** 94% (16/17) bled for more than 24 hours after dental extraction, OR 176 (95% CI 18–4250). Untreated bleeding typically emerges 12–24 hours—and sometimes 3–4 days—after a challenge and can persist for days or weeks. Suggested HPO: abnormal bleeding; prolonged bleeding following procedure. (mckay2004bleedingrisksassociated pages 3-4, diamandis2009biochemicalandgenetica pages 66-69)
* **Deep-cut bleeding:** 56% (9/16) reported bleeding continuing for days, OR 37 (5.6–320). Suggested HPO: prolonged bleeding. (mckay2004bleedingrisksassociated pages 3-4)
* **Hemarthrosis:** 43% (10/23), exclusive to affected relatives; recurrent episodes can cause destructive arthropathy. Suggested HPO: hemarthrosis. (mckay2004bleedingrisksassociated pages 3-4, blavignac12011quebecplateletdisorder pages 1-2)
* **Hematuria:** 50% (11/22), OR 7.7 (2.4–25), often spontaneous and episodic. Suggested HPO: **HP:0000790 Hematuria**. (mckay2004bleedingrisksassociated pages 3-4)
* **Epistaxis:** 57% (13/23), OR 4.0 (1.4–12); severe nosebleeds were uncommon. Suggested HPO: **HP:0000421 Epistaxis**. (mckay2004bleedingrisksassociated pages 3-4, mckay2004bleedingrisksassociated pages 2-3)
* **Bruising/hematoma:** abundant bruising or bleeding occurred in 57%; large downward-tracking or orange-sized bruises occurred in 32% and were exclusive to affected participants. Suggested HPO: **HP:0000978 Bruising susceptibility**. (mckay2004bleedingrisksassociated pages 3-4)
* **Menstrual bleeding:** 50% (3/6) reported menses lasting over seven days, OR 14 (1.6–147), although “abundant” menstruation itself was equally frequent in the small affected and control samples. Suggested HPO: **HP:0000132 Menorrhagia**. (mckay2004bleedingrisksassociated pages 3-4, mckay2004bleedingrisksassociated pages 4-5)
* **Delayed wound healing:** 26% (6/23), OR 4.9 (1.3–19). Suggested HPO: delayed wound healing. (mckay2004bleedingrisksassociated pages 3-4)
* **Mild thrombocytopenia:** platelet counts are about 50% lower than in unaffected relatives, but may remain normal. In one cohort the range was 120–245×10⁹/L, mean 167×10⁹/L. Suggested HPO: **HP:0001873 Thrombocytopenia**. (blavignac12011quebecplateletdisorder pages 2-3, mckay2004bleedingrisksassociated pages 4-5)

Morbidity is substantial despite variable expressivity: 60% reported lifestyle changes, commonly reduced participation in sports; 52% had received transfusions; and rare cerebral/intracranial hemorrhage, compartment bleeding, anemia, wound infection, and arthropathy have occurred. Formal EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life data are unavailable. (mckay2004bleedingrisksassociated pages 2-3, mckay2004bleedingrisksassociated pages 3-4, mckay2004bleedingrisksassociated pages 6-8)

## 4. Genetic and molecular information

**Gene.** **PLAU**, HGNC:9052, encodes urokinase plasminogen activator. Open Targets records PLAU as the sole associated target. **C10orf55** lies in the duplicated interval but is not comparably dysregulated and is not considered the causal effector. (OpenTargets Search: Quebec platelet disorder-PLAU, hayward2017theduplicationmutation pages 1-2, hayward2017theduplicationmutation pages 16-17)

**Variant.** The structural variant is a germline tandem copy-number gain, reported on GRCh37/hg19 as **chr10:75,659,017–75,736,956**, approximately 77.9 kb. A standardized HGVS genomic expression depends on reference assembly and breakpoint representation and should be generated by the testing laboratory. It is appropriately considered pathogenic based on complete segregation in the founder families, absence in controls, strong functional evidence, and phenotype recapitulation. Population allele frequency in gnomAD, TOPMed, or 1000 Genomes was not established in the retrieved evidence; it is expected to be extremely rare and founder-enriched. (blavignac12011quebecplateletdisorder pages 2-3, liang2020enhancergenerewiringin pages 10-12)

The duplication produces normal PLAU transcript/protein sequence but extreme lineage-specific expression. QPD megakaryocytes and platelets show over 100-fold elevation; granulocytes and monocytes show only approximately twofold and fivefold increases, respectively, consistent largely with copy number rather than pathologic enhancer adoption. (hayward2017theduplicationmutation pages 2-3, hayward2017theduplicationmutation pages 6-9)

No validated modifier gene, somatic form, germline mosaicism, anticipation, pathogenic SNV allelic series, or protective allele has been reported. Disease-relevant epigenetic changes include disease-chromosome-selective loss of promoter H3K27me3 and increased H3K36me3 across PLAU; these are downstream consequences of the inherited rearrangement, not independently inherited epimutations. (liang2020enhancergenerewiringin pages 12-13, liang2020enhancergenerewiringin pages 10-12)

## 5. Environmental information

No toxin, radiation, pollution, occupational exposure, pathogen, smoking pattern, alcohol use, diet, or exercise pattern causes QPD. Trauma and invasive procedures are **phenotype triggers**, not etiologic factors. High-impact activity increases bleeding opportunity, while activity restriction may reduce trauma at the cost of quality of life. There is no infectious component or vaccine relevance. (mckay2004bleedingrisksassociated pages 2-3, mckay2004bleedingrisksassociated pages 5-6)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A germline 78-kb tandem duplication encompassing **PLAU** **leads to** disruption of the normal boundary between subTADPLAU and subTADVCL. (liang2020enhancergenerewiringin pages 10-12, liang2020enhancergenerewiringin pages 24-25)
2. The altered 3D architecture **results in** relocation of one PLAU copy into the ENHQPD-containing regulatory neighborhood and preferential enhancer–PLAU contact on the disease chromosome. (liang2020enhancergenerewiringin pages 13-14, liang2020enhancergenerewiringin pages 15-16)
3. ENHQPD enhancer adoption during megakaryopoiesis **leads to** disease-allele loss of repressive H3K27me3, increased transcription-associated H3K36me3, and more than 100-fold production of normal PLAU transcripts. (liang2020enhancergenerewiringin pages 12-13, liang2020enhancergenerewiringin pages 10-12)
4. Megakaryocyte overexpression **results in** more than 100-fold excess uPA stored in platelet α-granules; this cell specificity explains the absence of generalized hyperfibrinolysis. (hayward2017theduplicationmutation pages 1-2, hayward2017theduplicationmutation pages 2-3)
5. Intraplatelet uPA **leads to** plasminogen conversion to plasmin, which **results in** proteolysis/loss of fibrinogen, factor V, von Willebrand factor, thrombospondin-1, multimerin-1, osteonectin, and P-selectin. (hayward2017theduplicationmutation pages 2-3, diamandis2009biochemicalandgenetica pages 80-83)
6. Platelet activation at an injury **releases** active uPA and **results in** accelerated, platelet-localized clot lysis. (hayward2017theduplicationmutation pages 2-3)
7. Premature dissolution of the initially formed plug **leads to** delayed rebleeding, prolonged post-procedural bleeding, hemarthrosis, hematuria, bruising, and impaired wound healing. The exact contribution of individual degraded α-granule proteins to each manifestation remains inferred rather than separately demonstrated. (mckay2004bleedingrisksassociated pages 1-2, blavignac12011quebecplateletdisorder pages 1-2)
8. **Branch:** intraplatelet proteolysis and/or shortened platelet survival probably **contributes to** mild thrombocytopenia; the causal detail is less directly established than the fibrinolysis mechanism. (blavignac12011quebecplateletdisorder pages 2-3, mckay2004bleedingrisksassociated pages 4-5)

ENHQPD is a 5.7-kb H3K27ac-enriched element about 50 kb from PLAU and VCL. Its 375-bp conserved module is associated with FLI1, GATA1, RUNX1, and TAL1; it increased PLAU-promoter reporter activity 2.4-fold and VCL-promoter activity 3.7-fold in K562 cells. Disease-allele PLAU contacts represented medians of 88.0% and 92.3% of informative 4C reads, above the 66.6% expected solely from the extra copy. (liang2020enhancergenerewiringin pages 12-13, liang2020enhancergenerewiringin pages 13-14, liang2020enhancergenerewiringin pages 15-16)

Suggested annotations include **GO:0042730 fibrinolysis**, platelet degranulation, plasminogen activation, proteolysis, chromatin organization, enhancer–promoter interaction, and megakaryocyte differentiation; **CL:0000556 megakaryocyte**, **CL:0000233 platelet**; and **GO:0031091 platelet α-granule**. The primary affected process is hemostasis/fibrinolysis, not MAPK, mTOR, PI3K–AKT, metabolism, immunity, apoptosis, or inflammation. Proposed uPA/uPAR–STAT/EGR1 and interferon-pathway effects remain speculative. (hayward2017theduplicationmutation pages 16-17)

**Molecular profiling.** RNA-seq found few transcriptome-wide differences beyond PLAU and down-regulated type-I-interferon gene sets; α-granule-protein transcripts were not reduced, supporting post-translational proteolysis. ChIP-seq profiled H3K27ac, H3K4me2, H3K36me3, H3K27me3, and CTCF; 4C-seq demonstrated altered contacts. Controlled-access raw data were deposited under **EGA EGAS00001004315**. No QPD-specific single-cell, spatial-transcriptomic, metabolomic, lipidomic, or integrated multi-omic study was identified. (liang2020enhancergenerewiringin pages 9-10, liang2020enhancergenerewiringin pages 10-12, hayward2017theduplicationmutation pages 16-17)

## 7. Anatomical structures affected

The primary system is hematologic/cardiovascular hemostasis. The directly affected lineage is bone-marrow megakaryocytes and their circulating platelets; the critical subcellular compartment is the platelet α-granule. Suggested anatomy/cell terms are bone marrow (**UBERON:0002371**), blood (**UBERON:0000178**), megakaryocyte (**CL:0000556**), platelet (**CL:0000233**), and platelet α-granule (**GO:0031091**). (hayward2017theduplicationmutation pages 2-3, liang2020enhancergenerewiringin pages 6-7)

Secondary injury can occur wherever bleeding develops: synovial joints, urinary tract, skin/subcutaneous tissue, muscle compartments, operative wounds, uterus, and intracranial tissues. These are complication sites rather than sites of PLAU dysregulation. There is no lateralization pattern. (mckay2004bleedingrisksassociated pages 2-3, mckay2004bleedingrisksassociated pages 5-6, mckay2004bleedingrisksassociated pages 3-4)

## 8. Temporal development

The molecular defect is congenital, but clinical onset ranges from childhood to adulthood depending on exposure. The course is chronic lifelong, nonprogressive at the molecular level, and episodic clinically. Bleeding commonly begins after an apparently successful initial hemostatic response, usually 12 hours to four days after a challenge. Repeated hemarthrosis can produce cumulative progressive arthropathy; otherwise no formal disease stages exist. (diamandis2009biochemicalandgenetica pages 66-69, blavignac12011quebecplateletdisorder pages 1-2)

There is no spontaneous remission. Antifibrinolytics suppress episodes but do not correct the genotype. Critical intervention windows are before and for several days after surgery, dental extraction, or major trauma. Asymptomatic children remain at risk because they may not yet have encountered a sufficient challenge. (diamandis2009biochemicalandgenetica pages 80-83, blavignac12011quebecplateletdisorder pages 4-6)

## 9. Inheritance and population

Inheritance is autosomal dominant. In the pedigree, the affected:unaffected offspring ratio was 1:1.5, not significantly different from the Mendelian 1:1 expectation (P=0.13). Molecular penetrance appears high, but bleeding expressivity is variable and age/exposure dependent. No anticipation or established role for consanguinity exists. (mckay2004bleedingrisksassociated pages 4-5)

Most documented cases trace to a founder family from the Sorel/Yamaska/St-François-du-Lac region. Historical prevalence estimates are approximately **1:220,000 in Quebec** and **1:655,000 in Canada**, likely underestimates; another older estimate was 1:300,000 in Quebec. Incidence, global prevalence, carrier frequency, age distribution, and sex ratio are unknown. Both sexes are affected, with sex-specific uterine/obstetric manifestations in females. (diamandis2009biochemicalandgenetic pages 129-133, blavignac12011quebecplateletdisorder pages 2-3)

## 10. Diagnostics

QPD should be suspected with autosomal-dominant delayed bleeding, large tracking bruises, hemarthrosis, unexplained hematuria, or bleeding responsive to antifibrinolytics. CBC may show mild thrombocytopenia. PT/INR and aPTT are usually normal; samples require appropriate handling because ex-vivo platelet factor-V proteolysis can confound results. Systemic-fibrinolysis tests and thromboelastography are generally normal. (blavignac12011quebecplateletdisorder pages 4-6)

Light-transmission aggregometry may show reduced primary and absent secondary aggregation with epinephrine; ADP/collagen responses can also be reduced. This is neither fully sensitive nor specific. Specialized biochemical confirmation demonstrates markedly increased platelet uPA and characteristic α-granule-protein degradation by ELISA/Western blot. (mckay2004bleedingrisksassociated pages 1-2, diamandis2009biochemicalandgenetica pages 80-83, blavignac12011quebecplateletdisorder pages 4-6)

**Definitive testing** is breakpoint-specific PCR or another validated copy-number/structural-variant assay for the PLAU duplication; cord-blood PCR can support newborn testing in an affected family. WES can miss this noncoding structural variant. CNV-aware WGS or a validated bleeding-disorder panel may detect it, but breakpoint PCR remains preferable for a known familial lesion. CMA detection depends on probe coverage; karyotyping is too low-resolution, and FISH is generally unnecessary. The platform comments beyond breakpoint PCR are technical inferences and should be validated by the diagnostic laboratory. (diamandis2009biochemicalandgenetica pages 80-83, blavignac12011quebecplateletdisorder pages 4-6)

Differential diagnosis includes von Willebrand disease, hemophilia/other coagulation deficiencies, immune thrombocytopenia, other inherited platelet secretion/storage-pool disorders, Gray platelet syndrome, and hyperfibrinolytic disorders. Delayed bleeding plus hemarthrosis resembles a coagulation defect, whereas bruising and aggregation abnormalities resemble a platelet disorder; platelet uPA/PLAU-duplication testing resolves the distinction. Cascade testing is appropriate for first-degree and other at-risk relatives, including minimally symptomatic children. (mckay2004bleedingrisksassociated pages 5-6, diamandis2009biochemicalandgenetica pages 80-83)

## 11. Outcome and prognosis

No 5- or 10-year survival rate, mortality rate, or life-expectancy estimate exists. QPD does not appear intrinsically degenerative, and major challenge-related bleeding is often preventable once recognized. Nonetheless, untreated morbidity includes transfusion, anemia, lifestyle restriction, delayed wound healing, hemarthrosis/arthropathy, severe muscle bleeding, and rare intracranial hemorrhage. One affected study participant and three deceased affected relatives were known to have had hemorrhagic strokes, but the cohort was insufficient to estimate risk. (mckay2004bleedingrisksassociated pages 5-6, mckay2004bleedingrisksassociated pages 6-8)

Neither platelet count nor platelet uPA concentration predicted overall bleeding score (adjusted R²≈0.05 for each). Hematuria correlated with higher platelet uPA (355±141 versus 207±51 ng/10⁹ platelets; P=0.005), and wound-healing problems with lower platelet counts (144±27 versus 174±31×10⁹/L; P=0.02), but these are exploratory, not validated prognostic biomarkers. (mckay2004bleedingrisksassociated pages 4-5)

## 12. Treatment

**Tranexamic acid** is first-line for acute bleeding and peri-procedural prevention; ε-aminocaproic acid is a less-potent alternative requiring higher doses. Suggested annotations are CHEBI:48669 and NCIT concepts *Tranexamic Acid*, *Aminocaproic Acid*, and *Antifibrinolytic Therapy*. Observationally, all 19 affected individuals challenged without an antifibrinolytic reported excessive bleeding, whereas all 12 treated during some or all challenges reported no serious bleeding while treated. This striking result is not from a randomized trial. (mckay2004bleedingrisksassociated pages 4-5, diamandis2009biochemicalandgenetica pages 69-72)

Expert schedules are event-dependent: approximately 3–4 days for minor bleeding/minor surgery, 4–5 days after dental extraction, 5–7 days after major surgery, trauma, or joint bleeding, and 10–14 days for intracranial bleeding. Major surgery may include a preoperative intravenous dose. Recurrent hemarthrosis may justify reduced-frequency prophylaxis. For procedures with high thrombosis risk, antifibrinolytic coverage should be coordinated with standard thromboprophylaxis rather than assuming QPD prevents thrombosis. (diamandis2009biochemicalandgenetica pages 80-83, blavignac12011quebecplateletdisorder pages 4-6, blavignac12011quebecplateletdisorder pages 6-6)

Platelet transfusion, plasma, and desmopressin have been reported ineffective for typical QPD bleeding because they do not suppress localized uPA/plasmin activity. Spontaneous hematuria generally resolves without treatment. Routine prophylaxis during uncomplicated pregnancy or childbirth is not supported, although individualized delivery planning is appropriate. Five affected women had nine successful pregnancies; two of five had received transfusions during childbirth. (mckay2004bleedingrisksassociated pages 5-6, mckay2004bleedingrisksassociated pages 4-5, diamandis2009biochemicalandgenetica pages 80-83)

No QPD-specific gene therapy, gene editing, ASO/siRNA, cell therapy, or targeted biologic is approved or in clinical trials. A ClinicalTrials.gov search retrieved no relevant interventional QPD study. Pharmacogenomic response predictors are unknown.

## 13. Prevention

Primary prevention of a germline founder disorder is not possible through lifestyle or immunization. Genetic counseling should explain a 50% transmission risk for a heterozygous affected parent, variable expressivity, and reproductive options such as targeted prenatal or preimplantation testing where locally available.

Secondary prevention consists of cascade testing, early molecular confirmation, medical-alert documentation, and pre-procedure hematology planning. Population or newborn screening is not justified by present prevalence evidence, but targeted newborn/cord-blood breakpoint PCR is feasible in known families. Tertiary prevention consists of timely antifibrinolytic prophylaxis, avoidance of unnecessary platelet-inhibiting drugs and high-trauma exposure, prompt evaluation of head injury, and prevention of recurrent joint damage. (diamandis2009biochemicalandgenetica pages 80-83, blavignac12011quebecplateletdisorder pages 4-6)

## 14. Other species and natural disease

No naturally occurring homologous QPD has been established in companion animals, livestock, or wildlife; therefore there is no veterinary breed, VBO term, zoonotic potential, or cross-species transmission. PLAU and its fibrinolytic function are evolutionarily conserved, but natural animal disease should not be inferred from experimental models.

The human ENHQPD_CONS sequence is 91% identical to mouse, with conserved H3K27ac and FLI1/GATA1/RUNX1/TAL1 occupancy. Although zebrafish lack a direct sequence orthologue, the human element drove reporter activity in thrombocyte-forming tissue, showing conserved regulatory logic rather than natural QPD. (liang2020enhancergenerewiringin pages 12-13)

## 15. Model organisms

A platelet/megakaryocyte-targeted uPA transgenic mouse reproduces important downstream features: platelet uPA expression, QPD-like bleeding, reduced thrombosis, fetal loss, and fatal postpartum hemorrhage. It validates the sufficiency of ectopic platelet uPA but does **not** model the human tandem duplication or enhancer rewiring. Its reproductive phenotype is more severe than human QPD: all nine pregnancies among five affected women in the family study were successful, illustrating a major species/model limitation. (hayward2017theduplicationmutation pages 2-3, mckay2004bleedingrisksassociated pages 5-6)

The **Tg(ENHQPD_CONS:GFP)hsc96 zebrafish** is a regulatory reporter, not a disease model. At 24 hours post-fertilization it showed activity in gata1-positive hematopoietic/thrombocyte-forming tissues, validating enhancer function in vivo. K562 reporter assays and CD34-derived human megakaryocytes are complementary in-vitro models. No knock-in mouse carrying the human duplication, patient iPSC model, organoid, or CRISPR screen was identified. (liang2020enhancergenerewiringin pages 8-9, liang2020enhancergenerewiringin pages 12-13, liang2020enhancergenerewiringin pages 13-14)

## Recent developments and expert assessment, 2023–2024

Recent literature has mainly consolidated diagnosis and management rather than changed the QPD model. A May 2023 review of inherited bleeding disorders emphasized CBC/smear followed by specialized aggregometry, secretion assays, flow cytometry, Western blotting, and genetic testing, while noting the expense and interpretive difficulty of platelet-function testing. A 2024 ClinGen-framework study evaluated the validity of hemostasis genes, and the 2024 ISTH state-of-the-art material continued to identify abnormal platelet PLAU expression as QPD’s defining mechanism. No new 2023–2024 QPD-specific natural-history cohort, pathogenic variant, randomized treatment study, or disease-modifying therapy was identified. (wilson2023preoperativediagnosisand pages 6-7)

The authoritative interpretation is therefore that QPD is one of the clearest examples of a pathogenic structural variant acting through **cell-type-specific enhancer adoption**. Mechanistic confidence is high, but clinical evidence remains constrained by founder-family cohorts, retrospective histories, and expert experience. Contemporary priorities are CNV-aware diagnosis, prospective natural-history data, standardized bleeding outcomes, and development of models that reproduce the actual human duplication rather than merely platelet uPA overexpression.

## Key primary references and URLs

1. McKay H, et al. “Bleeding risks associated with inheritance of the Quebec platelet disorder.” *Blood*. Published online 16 March 2004; print 1 July 2004. DOI: [10.1182/blood-2003-11-4077](https://doi.org/10.1182/blood-2003-11-4077). Abstract: “These data illustrate that QPD is associated with increased risks of bleeding that can be modified by fibrinolytic inhibitors.” (mckay2004bleedingrisksassociated pages 1-2)
2. Paterson AD, et al. “Persons with Quebec platelet disorder have a tandem duplication of PLAU.” *Blood*. Published online 9 December 2009; print February 2010. PMID: **20007542**. DOI: [10.1182/blood-2009-07-233965](https://doi.org/10.1182/blood-2009-07-233965). (paterson2010personswithquebec pages 3-4)
3. Hayward CPM, et al. “The duplication mutation of Quebec platelet disorder dysregulates PLAU, but not C10orf55…” *PLOS ONE*. 16 March 2017. PMID: **28301587**; PMCID: **PMC5354430**. DOI: [10.1371/journal.pone.0173991](https://doi.org/10.1371/journal.pone.0173991). (OpenTargets Search: Quebec platelet disorder-PLAU, hayward2017theduplicationmutation pages 1-2)
4. Liang M, et al. “Enhancer-gene rewiring in the pathogenesis of Quebec Platelet Disorder.” *Blood*. July 2020. DOI: [10.1182/blood.2020005394](https://doi.org/10.1182/blood.2020005394). Abstract: “the reorganization of subTAD genome architecture results in a dramatic, cell-type specific blood disorder phenotype.” (liang2020enhancergenerewiringin pages 6-7, liang2020enhancergenerewiringin pages 15-16)
5. Blavignac J, et al. “Quebec Platelet Disorder: Update on Pathogenesis, Diagnosis, and Treatment.” *Seminars in Thrombosis and Hemostasis*. September 2011. DOI: [10.1055/s-0031-1291382](https://doi.org/10.1055/s-0031-1291382). (blavignac12011quebecplateletdisorder pages 2-3, blavignac12011quebecplateletdisorder pages 4-6)
6. Bourguignon A, et al. “Screening and diagnosis of inherited platelet disorders.” *Critical Reviews in Clinical Laboratory Sciences*. 2022. DOI: [10.1080/10408363.2022.2049199](https://doi.org/10.1080/10408363.2022.2049199). (wilson2023preoperativediagnosisand pages 6-7)

**Evidence qualification:** Clinical estimates come chiefly from one founder pedigree and should not be interpreted as unbiased global frequencies. Treatment evidence is observational. Molecular causality is substantially stronger, supported by segregation, patient-derived megakaryocytes, allele-specific expression, chromatin profiling, chromosome-conformation capture, reporter experiments, and downstream animal phenocopy.

References

1. (hayward2017theduplicationmutation pages 1-2): Catherine P. M. Hayward, Minggao Liang, Subia Tasneem, Asim Soomro, John S. Waye, Andrew D. Paterson, Georges E. Rivard, and Michael D. Wilson. The duplication mutation of quebec platelet disorder dysregulates plau, but not c10orf55, selectively increasing production of normal plau transcripts by megakaryocytes but not granulocytes. PLOS ONE, 12(3):e0173991, Mar 2017. URL: https://doi.org/10.1371/journal.pone.0173991, doi:10.1371/journal.pone.0173991. This article has 27 citations and is from a peer-reviewed journal.

2. (hayward2017theduplicationmutation pages 2-3): Catherine P. M. Hayward, Minggao Liang, Subia Tasneem, Asim Soomro, John S. Waye, Andrew D. Paterson, Georges E. Rivard, and Michael D. Wilson. The duplication mutation of quebec platelet disorder dysregulates plau, but not c10orf55, selectively increasing production of normal plau transcripts by megakaryocytes but not granulocytes. PLOS ONE, 12(3):e0173991, Mar 2017. URL: https://doi.org/10.1371/journal.pone.0173991, doi:10.1371/journal.pone.0173991. This article has 27 citations and is from a peer-reviewed journal.

3. (mckay2004bleedingrisksassociated pages 1-2): Heather McKay, Francine Derome, M. Anwar Haq, Susan Whittaker, Emmy Arnold, Frédéric Adam, Nancy M. Heddle, Georges E. Rivard, and Catherine P. M. Hayward. Bleeding risks associated with inheritance of the quebec platelet disorder. Blood, 104 1:159-65, Jul 2004. URL: https://doi.org/10.1182/blood-2003-11-4077, doi:10.1182/blood-2003-11-4077. This article has 133 citations and is from a highest quality peer-reviewed journal.

4. (liang2020enhancergenerewiringin pages 15-16): Minggao Liang, Asim Usman Soomro, Subia Tasneem, Luis E Abatti, Azad Alizada, Xuefei Yuan, Liis Uusküla-Reimand, Lina Antounians, Sana Akhtar Alvi, Andrew David Paterson, Georges E Rivard, Ian C Scott, Jennifer A Mitchell, Catherine P M Hayward, and Michael Davies Wilson. Enhancer-gene rewiring in the pathogenesis of quebec platelet disorder. Blood, Jul 2020. URL: https://doi.org/10.1182/blood.2020005394, doi:10.1182/blood.2020005394. This article has 41 citations and is from a highest quality peer-reviewed journal.

5. (blavignac12011quebecplateletdisorder pages 1-2): Jessica Blavignac1, Natalia Bunimov1, Georges Rivard2, and Catherine P.M. Hayward1. Quebec platelet disorder: update on pathogenesis, diagnosis, and treatment. Semin Thromb Hemost, 37:713-720, Sep 2011. URL: https://doi.org/10.1055/s-0031-1291382, doi:10.1055/s-0031-1291382. This article has 79 citations.

6. (OpenTargets Search: Quebec platelet disorder-PLAU): Open Targets Query (Quebec platelet disorder-PLAU, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (blavignac12011quebecplateletdisorder pages 2-3): Jessica Blavignac1, Natalia Bunimov1, Georges Rivard2, and Catherine P.M. Hayward1. Quebec platelet disorder: update on pathogenesis, diagnosis, and treatment. Semin Thromb Hemost, 37:713-720, Sep 2011. URL: https://doi.org/10.1055/s-0031-1291382, doi:10.1055/s-0031-1291382. This article has 79 citations.

8. (paterson2010personswithquebec pages 3-4): Andrew D. Paterson, Johanna M. Rommens, Bhupinder Bharaj, Jessica Blavignac, Isidro Wong, Maria Diamandis, John S. Waye, Georges E. Rivard, and Catherine P. M. Hayward. Persons with quebec platelet disorder have a tandem duplication of plau, the urokinase plasminogen activator gene. Blood, 115 6:1264-6, Feb 2010. URL: https://doi.org/10.1182/blood-2009-07-233965, doi:10.1182/blood-2009-07-233965. This article has 116 citations and is from a highest quality peer-reviewed journal.

9. (liang2020enhancergenerewiringin pages 10-12): Minggao Liang, Asim Usman Soomro, Subia Tasneem, Luis E Abatti, Azad Alizada, Xuefei Yuan, Liis Uusküla-Reimand, Lina Antounians, Sana Akhtar Alvi, Andrew David Paterson, Georges E Rivard, Ian C Scott, Jennifer A Mitchell, Catherine P M Hayward, and Michael Davies Wilson. Enhancer-gene rewiring in the pathogenesis of quebec platelet disorder. Blood, Jul 2020. URL: https://doi.org/10.1182/blood.2020005394, doi:10.1182/blood.2020005394. This article has 41 citations and is from a highest quality peer-reviewed journal.

10. (hayward2017theduplicationmutation pages 16-17): Catherine P. M. Hayward, Minggao Liang, Subia Tasneem, Asim Soomro, John S. Waye, Andrew D. Paterson, Georges E. Rivard, and Michael D. Wilson. The duplication mutation of quebec platelet disorder dysregulates plau, but not c10orf55, selectively increasing production of normal plau transcripts by megakaryocytes but not granulocytes. PLOS ONE, 12(3):e0173991, Mar 2017. URL: https://doi.org/10.1371/journal.pone.0173991, doi:10.1371/journal.pone.0173991. This article has 27 citations and is from a peer-reviewed journal.

11. (liang2020enhancergenerewiringin pages 6-7): Minggao Liang, Asim Usman Soomro, Subia Tasneem, Luis E Abatti, Azad Alizada, Xuefei Yuan, Liis Uusküla-Reimand, Lina Antounians, Sana Akhtar Alvi, Andrew David Paterson, Georges E Rivard, Ian C Scott, Jennifer A Mitchell, Catherine P M Hayward, and Michael Davies Wilson. Enhancer-gene rewiring in the pathogenesis of quebec platelet disorder. Blood, Jul 2020. URL: https://doi.org/10.1182/blood.2020005394, doi:10.1182/blood.2020005394. This article has 41 citations and is from a highest quality peer-reviewed journal.

12. (liang2020enhancergenerewiringin pages 13-14): Minggao Liang, Asim Usman Soomro, Subia Tasneem, Luis E Abatti, Azad Alizada, Xuefei Yuan, Liis Uusküla-Reimand, Lina Antounians, Sana Akhtar Alvi, Andrew David Paterson, Georges E Rivard, Ian C Scott, Jennifer A Mitchell, Catherine P M Hayward, and Michael Davies Wilson. Enhancer-gene rewiring in the pathogenesis of quebec platelet disorder. Blood, Jul 2020. URL: https://doi.org/10.1182/blood.2020005394, doi:10.1182/blood.2020005394. This article has 41 citations and is from a highest quality peer-reviewed journal.

13. (liang2020enhancergenerewiringin pages 12-13): Minggao Liang, Asim Usman Soomro, Subia Tasneem, Luis E Abatti, Azad Alizada, Xuefei Yuan, Liis Uusküla-Reimand, Lina Antounians, Sana Akhtar Alvi, Andrew David Paterson, Georges E Rivard, Ian C Scott, Jennifer A Mitchell, Catherine P M Hayward, and Michael Davies Wilson. Enhancer-gene rewiring in the pathogenesis of quebec platelet disorder. Blood, Jul 2020. URL: https://doi.org/10.1182/blood.2020005394, doi:10.1182/blood.2020005394. This article has 41 citations and is from a highest quality peer-reviewed journal.

14. (diamandis2009biochemicalandgenetic pages 129-133): M Diamandis. Biochemical and genetic studies. Unknown journal, 2009.

15. (hayward2017theduplicationmutation pages 6-9): Catherine P. M. Hayward, Minggao Liang, Subia Tasneem, Asim Soomro, John S. Waye, Andrew D. Paterson, Georges E. Rivard, and Michael D. Wilson. The duplication mutation of quebec platelet disorder dysregulates plau, but not c10orf55, selectively increasing production of normal plau transcripts by megakaryocytes but not granulocytes. PLOS ONE, 12(3):e0173991, Mar 2017. URL: https://doi.org/10.1371/journal.pone.0173991, doi:10.1371/journal.pone.0173991. This article has 27 citations and is from a peer-reviewed journal.

16. (diamandis2009biochemicalandgenetica pages 80-83): M Diamandis. Biochemical and genetic studies. Unknown journal, 2009.

17. (diamandis2009biochemicalandgenetica pages 66-69): M Diamandis. Biochemical and genetic studies. Unknown journal, 2009.

18. (diamandis2009biochemicalandgenetic pages 66-69): M Diamandis. Biochemical and genetic studies. Unknown journal, 2009.

19. (mckay2004bleedingrisksassociated pages 3-4): Heather McKay, Francine Derome, M. Anwar Haq, Susan Whittaker, Emmy Arnold, Frédéric Adam, Nancy M. Heddle, Georges E. Rivard, and Catherine P. M. Hayward. Bleeding risks associated with inheritance of the quebec platelet disorder. Blood, 104 1:159-65, Jul 2004. URL: https://doi.org/10.1182/blood-2003-11-4077, doi:10.1182/blood-2003-11-4077. This article has 133 citations and is from a highest quality peer-reviewed journal.

20. (mckay2004bleedingrisksassociated pages 4-5): Heather McKay, Francine Derome, M. Anwar Haq, Susan Whittaker, Emmy Arnold, Frédéric Adam, Nancy M. Heddle, Georges E. Rivard, and Catherine P. M. Hayward. Bleeding risks associated with inheritance of the quebec platelet disorder. Blood, 104 1:159-65, Jul 2004. URL: https://doi.org/10.1182/blood-2003-11-4077, doi:10.1182/blood-2003-11-4077. This article has 133 citations and is from a highest quality peer-reviewed journal.

21. (diamandis2009biochemicalandgenetica pages 69-72): M Diamandis. Biochemical and genetic studies. Unknown journal, 2009.

22. (blavignac12011quebecplateletdisorder pages 4-6): Jessica Blavignac1, Natalia Bunimov1, Georges Rivard2, and Catherine P.M. Hayward1. Quebec platelet disorder: update on pathogenesis, diagnosis, and treatment. Semin Thromb Hemost, 37:713-720, Sep 2011. URL: https://doi.org/10.1055/s-0031-1291382, doi:10.1055/s-0031-1291382. This article has 79 citations.

23. (wilson2023preoperativediagnosisand pages 6-7): MD MSc R. Douglas Wilson. Preoperative diagnosis and management of inherited bleeding disorders in female adolescents and adults. Canadian Journal of Surgery, 66:E246-E263, May 2023. URL: https://doi.org/10.1503/cjs.005922, doi:10.1503/cjs.005922. This article has 7 citations and is from a peer-reviewed journal.

24. (blavignac12011quebecplateletdisorder pages 6-6): Jessica Blavignac1, Natalia Bunimov1, Georges Rivard2, and Catherine P.M. Hayward1. Quebec platelet disorder: update on pathogenesis, diagnosis, and treatment. Semin Thromb Hemost, 37:713-720, Sep 2011. URL: https://doi.org/10.1055/s-0031-1291382, doi:10.1055/s-0031-1291382. This article has 79 citations.

25. (mckay2004bleedingrisksassociated pages 5-6): Heather McKay, Francine Derome, M. Anwar Haq, Susan Whittaker, Emmy Arnold, Frédéric Adam, Nancy M. Heddle, Georges E. Rivard, and Catherine P. M. Hayward. Bleeding risks associated with inheritance of the quebec platelet disorder. Blood, 104 1:159-65, Jul 2004. URL: https://doi.org/10.1182/blood-2003-11-4077, doi:10.1182/blood-2003-11-4077. This article has 133 citations and is from a highest quality peer-reviewed journal.

26. (diamandis2009biochemicalandgenetic pages 80-83): M Diamandis. Biochemical and genetic studies. Unknown journal, 2009.

27. (mckay2004bleedingrisksassociated pages 2-3): Heather McKay, Francine Derome, M. Anwar Haq, Susan Whittaker, Emmy Arnold, Frédéric Adam, Nancy M. Heddle, Georges E. Rivard, and Catherine P. M. Hayward. Bleeding risks associated with inheritance of the quebec platelet disorder. Blood, 104 1:159-65, Jul 2004. URL: https://doi.org/10.1182/blood-2003-11-4077, doi:10.1182/blood-2003-11-4077. This article has 133 citations and is from a highest quality peer-reviewed journal.

28. (liang2020enhancergenerewiringin pages 23-24): Minggao Liang, Asim Usman Soomro, Subia Tasneem, Luis E Abatti, Azad Alizada, Xuefei Yuan, Liis Uusküla-Reimand, Lina Antounians, Sana Akhtar Alvi, Andrew David Paterson, Georges E Rivard, Ian C Scott, Jennifer A Mitchell, Catherine P M Hayward, and Michael Davies Wilson. Enhancer-gene rewiring in the pathogenesis of quebec platelet disorder. Blood, Jul 2020. URL: https://doi.org/10.1182/blood.2020005394, doi:10.1182/blood.2020005394. This article has 41 citations and is from a highest quality peer-reviewed journal.

29. (mckay2004bleedingrisksassociated pages 6-8): Heather McKay, Francine Derome, M. Anwar Haq, Susan Whittaker, Emmy Arnold, Frédéric Adam, Nancy M. Heddle, Georges E. Rivard, and Catherine P. M. Hayward. Bleeding risks associated with inheritance of the quebec platelet disorder. Blood, 104 1:159-65, Jul 2004. URL: https://doi.org/10.1182/blood-2003-11-4077, doi:10.1182/blood-2003-11-4077. This article has 133 citations and is from a highest quality peer-reviewed journal.

30. (liang2020enhancergenerewiringin pages 24-25): Minggao Liang, Asim Usman Soomro, Subia Tasneem, Luis E Abatti, Azad Alizada, Xuefei Yuan, Liis Uusküla-Reimand, Lina Antounians, Sana Akhtar Alvi, Andrew David Paterson, Georges E Rivard, Ian C Scott, Jennifer A Mitchell, Catherine P M Hayward, and Michael Davies Wilson. Enhancer-gene rewiring in the pathogenesis of quebec platelet disorder. Blood, Jul 2020. URL: https://doi.org/10.1182/blood.2020005394, doi:10.1182/blood.2020005394. This article has 41 citations and is from a highest quality peer-reviewed journal.

31. (liang2020enhancergenerewiringin pages 9-10): Minggao Liang, Asim Usman Soomro, Subia Tasneem, Luis E Abatti, Azad Alizada, Xuefei Yuan, Liis Uusküla-Reimand, Lina Antounians, Sana Akhtar Alvi, Andrew David Paterson, Georges E Rivard, Ian C Scott, Jennifer A Mitchell, Catherine P M Hayward, and Michael Davies Wilson. Enhancer-gene rewiring in the pathogenesis of quebec platelet disorder. Blood, Jul 2020. URL: https://doi.org/10.1182/blood.2020005394, doi:10.1182/blood.2020005394. This article has 41 citations and is from a highest quality peer-reviewed journal.

32. (liang2020enhancergenerewiringin pages 8-9): Minggao Liang, Asim Usman Soomro, Subia Tasneem, Luis E Abatti, Azad Alizada, Xuefei Yuan, Liis Uusküla-Reimand, Lina Antounians, Sana Akhtar Alvi, Andrew David Paterson, Georges E Rivard, Ian C Scott, Jennifer A Mitchell, Catherine P M Hayward, and Michael Davies Wilson. Enhancer-gene rewiring in the pathogenesis of quebec platelet disorder. Blood, Jul 2020. URL: https://doi.org/10.1182/blood.2020005394, doi:10.1182/blood.2020005394. This article has 41 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Quebec_Platelet_Disorder-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 17 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011136` (3 mentions) - the report calls it "if available"; MONDO calls it **Quebec platelet disorder**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001873` (2 mentions) - the report calls it "HPO: Thrombocytopenia"; HP calls it **Thrombocytopenia**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `Gene`, `Taxon`.