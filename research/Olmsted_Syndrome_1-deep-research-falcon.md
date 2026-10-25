---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-10-13T08:43:04.150096'
end_time: '2026-10-13T09:09:01.627649'
duration_seconds: 1557.48
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Olmsted Syndrome 1
  mondo_id: MONDO:0100296
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 44
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 5
  validator_version: 0.3.0
term_validation:
  total_terms: 4
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0100296
    reported_labels:
    - if available
    ontology_label: Olmsted syndrome 1
  unresolvable_prefixes:
  - ORPHA
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Olmsted_Syndrome_1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Olmsted Syndrome 1
- **MONDO ID:** MONDO:0100296 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Olmsted Syndrome 1** covering all of the
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
- **Disease Name:** Olmsted Syndrome 1
- **MONDO ID:** MONDO:0100296 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Olmsted Syndrome 1** covering all of the
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


# Olmsted syndrome 1: disease-characteristics research report

**Scope and evidence standard.** Olmsted syndrome 1 (OS1) here means **TRPV3-associated Olmsted syndrome**, not every condition described clinically as “Olmsted syndrome.” The literature often pools TRPV3 disease with genetically distinct *MBTPS2*- and *PERP*-associated disease; pooled frequencies must not be assigned to OS1. Evidence below distinguishes human observations, cell experiments, animal models, and registered trials. DOI links are provided when available; **PMIDs were not consistently present in the retrieved records and are not guessed**. Suggested ontology labels are candidates for knowledge-base curation, not assertions that an unverified accession has been confirmed. (duchatelet2015olmstedsyndromeclinical pages 2-4, kalinovskii2023trpv3ionchannel pages 13-14, duchatelet2015olmstedsyndromeclinical pages 5-7)

## 1. Disease information and identifiers

OS1 is an exceptionally rare Mendelian disorder of epidermal keratinization, classically involving **bilateral, progressively thickening, sometimes mutilating palmoplantar keratoderma (PPK)** and **keratotic plaques around body openings**. Hair loss, nail changes, painful fissures, and itch may accompany it; a genetically established TRPV3 case need not have every classical feature. The 2012 gene-discovery abstract describes OS as “a rare congenital disorder characterized by palmoplantar and periorificial keratoderma, alopecia in most cases, and severe itching.” (lin2012exomesequencingreveals pages 1-2, guo2023novelinsightsinto pages 6-8)

* **Disease:** OMIM **#614594**, cited for TRPV3-associated OS; causal gene **TRPV3**, OMIM **607066**. The supplied MONDO identifier is **MONDO:0100296**; its exact cross-reference to the OS1 subtype was not independently established in the retrieved literature and should be checked before database import. **ORPHA:659** labels the broader Olmsted syndrome phenotype, rather than an independently verified TRPV3-only subtype. An older review also lists OMIM **#300918** for a separate X-linked form. The review’s alternative labels include “mutilating palmoplantar keratoderma with periorificial keratotic plaques” and “palmoplantar and periorificial keratoderma.” (duchatelet2015olmstedsyndromeclinical pages 2-4, hao2024casereportnovel pages 1-2, lin2012exomesequencingreveals pages 1-2)
* **ICD-10/ICD-11 and MeSH:** an OS1-specific code or descriptor was **not verified**; do not substitute a generic keratoderma code as though subtype-specific. The cited information is **aggregated publications, experimental studies, and trial registries**, not an individual electronic-health-record extract. (duchatelet2015olmstedsyndromeclinical pages 2-4, lin2012exomesequencingreveals pages 1-2)

**Core sources:** Lin *et al.*, *American Journal of Human Genetics*, **9 March 2012**, https://doi.org/10.1016/j.ajhg.2012.02.006; Duchatelet and Hovnanian, *Orphanet Journal of Rare Diseases*, **2015**, https://doi.org/10.1186/s13023-015-0246-5. (lin2012exomesequencingreveals pages 1-2, duchatelet2015olmstedsyndromeclinical pages 1-2)

## 2. Etiology, susceptibility, protection, and gene–environment interaction

**Primary cause:** germline pathogenic variants affecting the Ca²⁺-permeable, warm-responsive **TRPV3 cation channel**. Well-characterized dominant missense substitutions increase basal channel activity; pathogenic disease can also result from **biallelic TRPV3 variants**. Some apparently sporadic cases are de novo; multigenerational pedigrees establish dominant transmission. The initial six-person study found p.Gly573Ser in four patients, p.Gly573Cys in one, and p.Trp692Gly in one; tested variants were absent from **216 ancestry-matched controls**. This small control set does **not** establish a current gnomAD allele frequency. (lin2012exomesequencingreveals pages 2-4, lin2012exomesequencingreveals pages 1-2, duchatelet2015olmstedsyndromeclinical pages 5-7)

**Environmental causal risk:** no toxin, diet, infection, occupation, smoking behavior, or lifestyle exposure is established as an **initiating cause** of OS1. Pressure and friction localize or worsen thickened plantar skin, and warmth can provoke burning pain in some cases; these are manifestations or modifiers, not demonstrated primary causes. The relevant gene–environment result is **experimental, not human epidemiology**: mutant DS-Nh mice develop spontaneous dermatitis under certain *Staphylococcus aureus* and genetic-background conditions but not reliably under pathogen-free conditions. Skin infection in a person with OS1 can consequently be a *complication* without being the genetic disease’s cause. (duchatelet2015olmstedsyndromeclinical pages 4-5, fatima2022abnormalsomatosensorybehaviors pages 1-2, dansoabeam2013olmstedsyndromeexploration pages 1-3)

**Protection and modification:** no replicated protective allele, protective lifestyle exposure, or named modifier gene has been validated for OS1. Variable manifestations among relatives carrying the same variant make genetic background and environmental modification plausible, but neither a human modifying locus nor quantitative gene–environment interaction has been demonstrated. Avoid interpreting an unaffected relative or unconfirmed variant as proof of incomplete penetrance. (duchatelet2015olmstedsyndromeclinical pages 5-7, ni2016anovelmutation pages 3-4, zhang2025erlotinibtherapyfor pages 2-4)

## 3. Phenotypes and quality-of-life consequences

The following are **suggested HPO concept labels**; accession numbers and OS1-wide frequencies should be verified against HPO before import. The only directly countable genotype-specific series below comprised **six selected TRPV3-positive patients**, not a representative cohort. (lin2012exomesequencingreveals pages 1-2)

| Phenotype type and suggested HPO concept | Onset, severity, course and available frequency | Functional impact / evidence |
|---|---|---|
| **Sign:** palmoplantar keratoderma; hyperkeratosis; painful skin fissures | Usually infancy; may progress from focal pressure-site plaques to diffuse, thick, transgredient lesions. **6/6** in Lin’s selected series. Severe or mutilating disease is possible. | Walking, hand use, and footwear can become difficult. (lin2012exomesequencingreveals pages 1-2, duchatelet2015olmstedsyndromeclinical pages 4-5) |
| **Sign:** periorificial hyperkeratosis/keratotic plaques | Often early childhood; **6/6** in the original classical series, but **absent in documented atypical genetically investigated cases**. Sites include mouth, nostrils, ears, eyes, umbilicus, genital and anal regions. | Pain, inflammation, appearance, and secondary infection; absence does not exclude OS1. (lin2012exomesequencingreveals pages 1-2, duchatelet2015olmstedsyndromeclinical pages 4-5, hao2024casereportnovel pages 2-5) |
| **Sign:** pseudoainhum, digit constriction, flexion contracture, spontaneous digit amputation | Later consequence of progressive keratoderma; **variable**, not obligatory. | Loss of grasp, mobility and, exceptionally, digits; radiographic osteolysis and deformity can coexist. (duchatelet2015olmstedsyndromeclinical pages 4-5, hao2024casereportnovel pages 1-2) |
| **Sign:** alopecia/hypotrichosis; nail dystrophy | Variable childhood manifestations; **some hair abnormality in 6/6** in the original series, ranging from alopecia universalis to sparse curly hair; normal hair occurs in other reports. | Appearance and psychosocial effects; nail damage and periungual infection may impair dexterity. (lin2012exomesequencingreveals pages 1-2, duchatelet2015olmstedsyndromeclinical pages 4-5) |
| **Symptoms:** pruritus; palmoplantar pain; burning pain/erythromelalgia | Episodic or persistent, severity variable. **6/6 reported severe lesional itch** in Lin’s selected series. In a **mixed-genotype, historical OS review**, approximately **50%** had painful PPK and **16%** had reported itch; these are **not OS1 frequencies** and inconsistent reporting limits interpretation. Heat-associated flares are uncommon. | Sleep disruption, inability to walk or grasp, reduced participation in sport and daily activity. (lin2012exomesequencingreveals pages 1-2, duchatelet2015olmstedsyndromeclinical pages 4-5, zhang2025erlotinibtherapyfor pages 2-4) |
| **Other signs:** leukokeratosis, corneal disease, sweating abnormalities, recurrent skin infections, growth delay | Inconsistently reported; individual onset and OS1-specific percentages unavailable. | Corneal disease can threaten vision; recurrent infection increases treatment burden. (duchatelet2015olmstedsyndromeclinical pages 4-5, duchatelet2015olmstedsyndromeclinical pages 5-7, dansoabeam2013olmstedsyndromeexploration pages 1-3) |
| **Laboratory finding:** high IgE and eosinophilia | Demonstrated in **one** TRPV3 p.Gly573Ala patient; **not an established diagnostic biomarker**. | Suggests clinically relevant inflammatory assessment where indicated, not routine expectation of immunodeficiency. (dansoabeam2013olmstedsyndromeexploration pages 1-3) |

No validated OS1-specific **EQ-5D, SF-36, PROMIS, or per-phenotype quality-of-life distribution** was identified. Reported pain, itch, insomnia, walking limitation and digit loss provide qualitative evidence of potentially severe disability; avoid manufacturing numerical scores. (duchatelet2015olmstedsyndromeclinical pages 4-5, duchatelet2015olmstedsyndromeclinical pages 7-8)

## 4. Genetics and molecular annotation

**TRPV3** is the defining gene for this entry; a human study locates it at **17p13** and gives OMIM **607066**. Its product is a tetramer-forming, six-transmembrane nonselective cation channel. Altered gating near the S4–S5 linker or post-S6 TRP region is established for some substitutions, but **do not assume that every reported variant has experimentally proven gain of function**. Confirm the current HGNC identifier, reference transcript, and residue numbering before importing genomic HGVS strings. (lin2012exomesequencingreveals pages 1-2, duchatelet2015olmstedsyndromeclinical pages 5-7, lin2012exomesequencingreveals pages 4-6)

* **Strong functional examples:** heterozygous **c.1717G>A, p.Gly573Ser; c.1717G>T, p.Gly573Cys; c.2074T>G, p.Trp692Gly**. All three had constitutive currents in transfected-cell experiments. Human lesional skin and cultured mutant-expressing cells additionally exhibited increased apoptosis/cell death. (lin2012exomesequencingreveals pages 2-4, lin2012exomesequencingreveals pages 1-2, lin2012exomesequencingreveals pages 4-6)
* **Other reported genotypes:** p.Gly573Ala; familial p.Met672Ile; milder familial p.Gln580Pro; **homozygous p.Trp521Ser**; and two affected brothers with compound-heterozygous **p.Gly568Cys** and splice-associated **p.Gln216_Gly262del**. This illustrates recessive as well as dominant TRPV3 disease; molecular functionality and penetrance vary by allele. (dansoabeam2013olmstedsyndromeexploration pages 1-3, duchatelet2015olmstedsyndromeclinical pages 5-7, ni2016anovelmutation pages 3-4)
* **Important 2024–2025 qualification:** a 2024 single-patient report describes **c.916G>A, p.Val306Met** and plantar squamous-cell carcinoma; pathogenicity predictions conflict and the authors specifically request electrophysiological confirmation. A January 2025 familial report describes **c.1964T>C, p.Leu655Pro (p.L655P)**. Because this substitution changes one amino acid rather than the reading frame, it is a **missense variant**, despite contradictory “frameshift” wording in that article. Neither case report by itself supplies a verified ACMG/AMP classification or population-database allele frequency. (hao2024casereportnovel pages 2-5, zhang2025erlotinibtherapyfor pages 2-4, zhang2025erlotinibtherapyfor pages 1-2)
* **Separate disease genes:** X-linked **MBTPS2** and autosomal **PERP** can cause Olmsted-like/Olmsted syndrome but should **not be annotated as causal genes for molecularly defined TRPV3-OS1**. *KRT1, GJB2, LOR, SLURP1,* and *CTSC* chiefly inform overlapping disorders and differential testing. No OS1-specific causal aneuploidy or recurrent translocation, established modifier gene, reproducible methylation signature, founder allele, or protective variant was identified. (kalinovskii2023trpv3ionchannel pages 13-14, duchatelet2015olmstedsyndromeclinical pages 7-8, hao2024casereportnovel pages 2-5)

**Variant-origin guidance:** inherited or de novo **germline** TRPV3 variants underlie this Mendelian entry; no evidence retrieved establishes a recurrent causative **somatic** OS1 mutation. Assign pathogenic/likely pathogenic/VUS status only after **variant-specific ClinVar/ClinGen and ACMG assessment**, including segregation and functional data; do not convert a case-report author’s conjecture or an in-silico score into a database classification. (lin2012exomesequencingreveals pages 2-4, hao2024casereportnovel pages 2-5)

## 5. Environmental information

There is no established initiating infectious agent, occupational toxin, radiation exposure, or dietary/lifestyle cause of OS1. **Secondary bacterial or candidal infection** occurs in abnormal keratotic skin; in the DS-Nh mouse, *S. aureus* exposure changes the expression of dermatitis and itch. Pressure-bearing skin is prominently affected, and some patients report heat-provoked erythromelalgia; neither observation demonstrates preventability of a germline TRPV3 mutation by exposure avoidance. No zoonotic transmission is relevant. (duchatelet2015olmstedsyndromeclinical pages 5-7, fatima2022abnormalsomatosensorybehaviors pages 1-2, duchatelet2015olmstedsyndromeclinical pages 4-5)

## 6. Mechanism and pathophysiology

**Ordered causal chain; evidence levels indicated.**

1. **Germline activating TRPV3 variants lead to** abnormally active channel gating; for p.Gly573Ser, p.Gly573Cys and p.Trp692Gly, increased basal currents were **demonstrated in vitro**. (lin2012exomesequencingreveals pages 2-4)
2. **Excess channel activity leads to** abnormal keratinocyte cation/Ca²⁺ signaling; enhanced conductance is demonstrated, while its precise magnitude and spatiotemporal distribution in each patient’s living epidermis are **inferred**. (lin2012exomesequencingreveals pages 2-4, duchatelet2015olmstedsyndromeclinical pages 7-8)
3. **Altered channel signaling leads to** a disturbed balance of epidermal proliferation, terminal differentiation and cell survival. Increased apoptosis is demonstrated in mutant-expressing cells and selected human lesions; exactly how apoptosis produces chronic hyperkeratosis remains **inferred**. (lin2012exomesequencingreveals pages 2-4, lin2012exomesequencingreveals pages 4-6, duchatelet2015olmstedsyndromeclinical pages 7-8)
4. **Branch A—experimental cell trafficking:** some mutant TRPV3 proteins **lead to** reduced surface localization, altered ER/Golgi distribution, poorer cell adhesion and defective lysosomal labeling/movement in engineered HaCaT keratinocytes. A contribution of these abnormalities to **human OS1 lesion formation is inferred**, not established for every allele. (yadav2017trpv3mutantscausing pages 1-4, yadav2017trpv3mutantscausing pages 4-6)
5. **Branch B—skin signaling and inflammation:** TRPV3 activity **can lead to** TGF-α/EGFR-linked epidermal signaling and inflammatory mediator release in non-OS1 experimental systems. Its precise position upstream of human OS1 keratoderma, any MAPK/mTOR involvement, and the fraction of patients with intrinsic immune dysregulation remain **inferred**; a single human patient had IgE/eosinophil abnormalities. (duchatelet2015olmstedsyndromeclinical pages 7-8, dansoabeam2013olmstedsyndromeexploration pages 1-3, zhang2025erlotinibtherapyfor pages 4-6)
6. **Branch C—hair and sensation:** abnormal follicular TRPV3 activity **leads to** impaired hair growth in experimental systems and is **consistent with** human hypotrichosis/alopecia. Abnormal epidermal innervation and inflammatory signaling **may lead to** itch, burning or pain; the precise human neural mechanism is **not demonstrated**, and one mutant-mouse strain instead showed reduced responses to several pruritogens. (guo2023novelinsightsinto pages 6-8, fatima2022abnormalsomatosensorybehaviors pages 1-2, lin2012exomesequencingreveals pages 1-2)
7. **Downstream barrier damage and prolonged hyperkeratosis lead to** fissures, infection susceptibility and constriction bands; progressive constriction **can result in** contractures and auto-amputation. A carcinoma association is reported, but a direct mutation-to-cancer causal sequence or risk magnitude is **unproven**. (duchatelet2015olmstedsyndromeclinical pages 4-5, hao2024casereportnovel pages 1-2)

**Cell types and suggested ontology concepts:** epidermal **keratinocyte** and hair-follicle keratinocyte are the primary cellular candidates (**CL: keratinocyte**, verify precise IDs); **sensory neuron**, **mast cell**, **eosinophil**, **T lymphocyte**, and **Langerhans cell** are implicated variably, often by inference rather than demonstrated primary injury. Candidate **GO biological processes** are calcium-ion transmembrane transport, regulation of epidermal-cell differentiation, keratinocyte proliferation, apoptotic process, epidermis development, cell adhesion, inflammatory response, and sensory perception of itch/pain. Candidate **GO cellular components** include plasma membrane/ion-channel complex, endoplasmic reticulum, Golgi apparatus, lysosome, and nucleus-associated ER membrane. The lysosomal result is an **engineered-cell observation**, not proof that OS1 is clinically a generalized lysosomal storage disorder. (yadav2017trpv3mutantscausing pages 1-4, yadav2017trpv3mutantscausing pages 4-6, dansoabeam2013olmstedsyndromeexploration pages 1-3, guo2023novelinsightsinto pages 3-4)

**Molecular profiling and technology:** a small p.Gln580Pro-associated investigation reported reduced differentiation, gap-junction, tight-junction and desmosome-associated expression, with increased proliferation/cell-death-associated proteins; it is not a validated diagnostic multi-omic signature. No OS1-specific reproducible metabolomic, lipidomic, epigenomic, single-cell or spatial-transcriptomic signature or therapeutic CRISPR screen was established by the retrieved evidence. EGFR-directed treatment offers clinical pathway support but **does not alone prove** the full proposed pathway. (duchatelet2015olmstedsyndromeclinical pages 7-8, zhang2025erlotinibtherapyfor pages 4-6)

## 7. Anatomical structures affected

**Primary:** palmar and plantar **epidermis**, often bilaterally; periorificial facial and anogenital epidermis; hair follicles and nails. **Secondary/variable:** hand and foot digits, underlying phalanges and joints, oral mucosa, corneal surface, cutaneous sensory nerve endings, and infected keratotic skin. Candidate **UBERON labels** for mapping include skin of palm, skin of sole, epidermis, hair follicle, nail, digit, cornea, and oral mucosa; exact accession IDs should be checked. Hands and feet are classically **bilateral**, whereas degree of severity and complications, including a reported right-sole carcinoma, can be asymmetric. **CL labels:** keratinocyte and sensory neuron; infiltrating mast cell and leukocyte where biopsy demonstrates them. **GO cellular components:** plasma membrane, ER, Golgi and lysosome as above. (lin2012exomesequencingreveals pages 1-2, duchatelet2015olmstedsyndromeclinical pages 4-5, hao2024casereportnovel pages 1-2, yadav2017trpv3mutantscausing pages 4-6)

## 8. Temporal development

Classical disease begins **at birth, during infancy, or in early childhood**, sometimes becoming especially evident when walking or grasping begins. In Lin’s six-person TRPV3 series, **all six developed symptoms in the first year**. The usual untreated course is **chronic, slowly progressive**, with focal lesions potentially extending and thickening; the tempo and eventual severity vary considerably. An atypical familial patient described in 2025 reported approximately eight years of symptoms at age 31, so childhood onset is not an absolute diagnostic requirement. Pain or erythromelalgia can flare with warmth; sustained spontaneous remission rates have not been measured. No formal validated staging system, progression-rate estimate, or defined molecular critical window exists. Early control of keratoderma, fissures and contracture risk is clinically rational, but disease-modifying prevention of future digit loss has not been proven. (duchatelet2015olmstedsyndromeclinical pages 2-4, lin2012exomesequencingreveals pages 1-2, duchatelet2015olmstedsyndromeclinical pages 4-5, zhang2025erlotinibtherapyfor pages 2-4)

## 9. Inheritance and population

Dominant OS1 often reflects a **de novo heterozygous activating variant**, although affected parents and children establish familial **autosomal-dominant** disease. Rare homozygous and compound-heterozygous **autosomal-recessive** TRPV3 genotypes are reported. The dominant transmission risk for a heterozygous affected parent is **50% per pregnancy**, conditional on that allele being pathogenic; for two carriers of a confirmed recessive genotype, conventional Mendelian recurrence risk is **25%**. These are genetic-counseling calculations, **not observed OS1 penetrance estimates**. Penetrance, germline-mosaicism frequency, carrier frequency, founder effects, anticipation, and reliable genotype-stratified sex ratio remain unknown. Consanguinity may matter in a particular recessive pedigree but is not a prerequisite. (duchatelet2015olmstedsyndromeclinical pages 5-7, lin2012exomesequencingreveals pages 2-4, ni2016anovelmutation pages 3-4)

The 2015 review found **73 reported patients in 59 publications through 1 December 2014**, including molecularly different and untyped forms; it conjectured overall prevalence **below one per million** and described approximately **63% male** among published cases. Neither figure is a measured OS1-specific prevalence or sex ratio. **Incidence per 100,000 person-years, population age distribution, and ethnic/geographic enrichment cannot be reliably quantified**. Case reports encompass several backgrounds and imply worldwide occurrence, not a proven regional prevalence difference. (duchatelet2015olmstedsyndromeclinical pages 2-4, duchatelet2015olmstedsyndromeclinical pages 1-2, duchatelet2015olmstedsyndromeclinical pages 5-7)

## 10. Diagnostics

**Clinical assessment:** inspect both palms and soles for progressive thick plaques and fissures, assess periorificial sites, hair and nails, painful or constricted digits, gait, infection and vision. Because genetically established OS1 can be atypical, the classical skin combination is suggestive rather than a rigid requirement. Skin biopsy may show **psoriasiform epidermal hyperplasia, acanthosis, ortho-/parakeratosis, and inflammatory infiltrates**; these changes are **nonspecific**. Radiographs are useful for contractures, osteolysis or suspected bony involvement, not for identifying the causal allele. Suspicious enlarging, bleeding or ulcerated lesions require **biopsy to exclude cancer**. (duchatelet2015olmstedsyndromeclinical pages 7-8, lin2012exomesequencingreveals pages 2-4, hao2024casereportnovel pages 1-2, zhang2025erlotinibtherapyfor pages 2-4)

**Molecular confirmation:** sequence **TRPV3** using a suitable keratoderma/genodermatosis panel or single-gene assay when the phenotype is characteristic; family segregation and variant interpretation are essential. **Trio whole-exome sequencing** established the original de novo variant and is useful when phenotype or inheritance is unclear; exome or genome analysis may help if panel testing is unrevealing, including evaluation of other Olmsted-like genes. Seek orthogonal confirmation as appropriate and consider biallelic/splice variants. Routine **karyotyping, CMA, FISH, mitochondrial DNA and repeat-expansion assays** are not primary tests for molecularly typical OS1. No validated disease-specific serum enzyme, circulating protein, imaging biomarker, RNA-seq, proteomic, metabolomic, methylation or liquid-biopsy diagnostic assay was found. Measure **serum zinc** when acrodermatitis enteropathica is plausible rather than treating zinc as an OS1 biomarker. (lin2012exomesequencingreveals pages 1-2, lin2012exomesequencingreveals pages 2-4, duchatelet2015olmstedsyndromeclinical pages 5-7, duchatelet2015olmstedsyndromeclinical pages 7-8)

**Differential:** *GJB2/LOR*-associated Vohwinkel syndrome; *SLURP1*-associated mal de Meleda; *GJB6*-associated Clouston syndrome; *CTSC*-associated Papillon–Lefèvre/Haim–Munk syndromes; keratin-associated pachyonychia congenita; *TAT*-related tyrosinemia II; zinc-transport-related acrodermatitis enteropathica; Huriez-like disease; and *MBTPS2*/*PERP* Olmsted-like conditions. Periorificial plaques, family segregation, associated findings, and targeted molecular testing help discriminate them. No evidence supports a **universal population or newborn OS1 screening program**; offer targeted family testing when an informative familial allele is established. (duchatelet2015olmstedsyndromeclinical pages 7-8, kalinovskii2023trpv3ionchannel pages 13-14, hao2024casereportnovel pages 2-5)

## 11. Outcomes and prognosis

Severe PPK can impair walking and grasping, lead to flexion contractures and, in advanced cases, spontaneous digit loss; itch and pain may cause insomnia. Corneal disease can impair sight. Secondary infection is a recognized complication. Published cases associate longstanding keratotic skin with **squamous-cell carcinoma and, occasionally, melanoma**, but there is **no robust OS1-specific absolute cancer risk or screening interval**. A 2024 patient with a novel, not functionally confirmed TRPV3 p.Val306Met variant developed **biopsy-confirmed plantar squamous-cell carcinoma requiring foot amputation**; this is a serious observed event, not proof of a variant-specific oncogenic mechanism. Historical authors reported **no established reduction in life expectancy**, which should not be construed as a measured normal survival curve. OS1-specific mortality, five-/ten-year survival, validated prognosis models, biomarker-based risk stratification and long-term treatment durability are unavailable. (duchatelet2015olmstedsyndromeclinical pages 7-8, duchatelet2015olmstedsyndromeclinical pages 4-5, hao2024casereportnovel pages 1-2, hao2024casereportnovel pages 2-5)

## 12. Treatment and real-world implementation

**Evidence-graded care sequence:** confirm genotype and assess pain, mobility, fissures, infection, eye disease and suspicious skin lesions; begin individualized barrier and symptomatic treatment; consider specialist-supervised systemic treatment for disabling disease; record pain, mobility, lesion area/thickness and adverse effects over time. There is **no large OS1 randomized efficacy trial** in the retrieved material. **NCIT suggestions below are intervention-class labels, not verified NCIT accessions**. (duchatelet2015olmstedsyndromeclinical pages 8-9, duchatelet2015olmstedsyndromeclinical pages 7-8, NCT07090889 chunk 1)

1. **Supportive dermatologic care — NCIT concepts: emollient therapy, keratolytic therapy, wound care, physical/occupational therapy.** Moisturizers and protective skin care, carefully selected **urea or salicylic-acid keratolytics**, fissure care, footwear adaptation, and indicated management of documented bacterial/fungal infection may relieve symptoms. Historical outcomes range from poor to moderate; none reliably corrects the mutation. Candidate **ChEBI labels**: urea and salicylic acid; verify accession IDs before annotation. (duchatelet2015olmstedsyndromeclinical pages 8-9, lin2012exomesequencingreveals pages 1-2)
2. **Systemic retinoids — NCIT concept: retinoid therapy.** Acitretin or historical etretinate may reduce thickness and itch, but recurrence or incomplete relief is common and safety monitoring is necessary. In the 2012 original series, **three treated patients improved in skin lesions and itching after four weeks**, while hair improvement remained limited after one year. In a 2024 case, **acitretin 10 mg three times daily**, topical tretinoin and moisturizers produced moderate improvement after six months; later carcinoma arose despite intermittent management. These uncontrolled observations are not a validated response rate. Candidate ChEBI labels: acitretin, tretinoin. (lin2012exomesequencingreveals pages 1-2, hao2024casereportnovel pages 1-2, duchatelet2015olmstedsyndromeclinical pages 8-9)
3. **EGFR inhibition — NCIT concept: EGFR inhibitor therapy; agent erlotinib.** A published **2020 three-patient report** describes erlotinib for TRPV3-associated OS (Greco *et al.*, *JAMA Dermatology*, https://doi.org/10.1001/jamadermatol.2019.4126); a separate 2020 publication examines EGFR and mTOR pathway targeting (https://doi.org/10.1001/jamadermatol.2019.4141). A **2023 twin case report** describes combined erlotinib and acitretin (https://doi.org/10.1111/pde.15264). These publications were identified bibliographically or through subsequent papers; their full primary outcome and safety data were **not retrieved here**, so no pooled effect is calculated. (zhang2025erlotinibtherapyfor pages 6-7, zhang2025erlotinibtherapyfor pages 6-6)
4. **Detailed 2025 real-world example:** a patient and his father carried heterozygous **TRPV3 p.Leu655Pro**; the symptomatic patient received **erlotinib 75 mg/day *together with oral acitretin***. Plantar lesions improved by **three months** and only mild residual change was described at **five months**; mild gastric discomfort and transient forearm burning were recorded. **Combination treatment and lack of a control prevent attribution of benefit or toxicity solely to erlotinib.** For a separate 2024 patient, painful disabling PPK improved only moderately under retinoid-based care and subsequent SCC required surgery. (zhang2025erlotinibtherapyfor pages 2-4, hao2024casereportnovel pages 1-2)
5. **Investigational direct TRPV3 blockade — NCIT concept: investigational TRPV3 inhibitor.** **NCT07090889**, first posted **29 July 2025**, started **8 July 2025**, registers oral **KM-023** phase 1 testing in healthy volunteers followed by an approximately **12-week open-label cohort of up to eight Olmsted patients**, measuring safety, pharmacokinetics, plantar-callus dimensions and lesion scores. Its eligibility accepts **TRPV3 *or PERP***, so even a future combined result would require genotype separation for OS1. The estimated **64 total participants** are mainly healthy volunteers, **not 64 OS1 cases**; no efficacy or adverse-event outcome was available in the retrieved registry. Registry: https://clinicaltrials.gov/study/NCT07090889. Separate topical **KM-001** studies **NCT05435638** and **NCT05956314** enrolled punctate PPK or pachyonychia congenita, **not OS1**; their results cannot be relabeled as OS1 treatment success. (NCT07090889 chunk 1, NCT07090889 chunk 2, NCT05435638 chunk 1, NCT05956314 chunk 1)
6. **Other measures:** analgesia, topical lidocaine, selected neuropathic-pain agents and itch management may be needed; surgical debulking or grafting has often been followed by recurrent keratosis. Biopsy and oncologic excision are indicated for suspected cancer. No disease-correcting gene therapy, RNA therapy, cell therapy, immunotherapy, established pharmacogenomic dosing rule or approved OS1-specific precision intervention was verified. A trial registry discussing erlotinib for **other keratinopathies**, **NCT06545695**, excludes TRPV3-OS1 under its listed entry criteria and must not be presented as an OS1 trial. (duchatelet2015olmstedsyndromeclinical pages 8-9, hao2024casereportnovel pages 1-2, NCT06545695 chunk 1)

**Recent evidence at a glance:** the table juxtaposes primary observations and trial design while flagging where molecular attribution or therapeutic efficacy remains uncertain. (lin2012exomesequencingreveals pages 1-2, hao2024casereportnovel pages 1-2, NCT07090889 chunk 1)

| Evidence/source date | Key observation | Inference/limitation |
|---|---|---|
| **Human genetics and functional study — Lin et al., 9 Mar 2012; n=6** | All six patients had first-year onset. Heterozygous TRPV3 missense variants were p.Gly573Ser in 4/6, p.Gly573Cys in 1/6, and p.Trp692Gly in 1/6; variants were de novo where parental samples permitted assessment and were absent from 216 ancestry-matched controls. Mutant-transfected HEK293 cells showed constitutive currents; mutant cells and lesional keratinocytes showed increased death or apoptosis. (lin2012exomesequencingreveals pages 2-4, lin2012exomesequencingreveals pages 1-2, lin2012exomesequencingreveals pages 4-6) | **Strong OS1 gene–disease and gain-of-function evidence**, but based on a small, selected series. HEK293 cells are not native epidermis, and the proposed progression from apoptosis to hyperkeratosis was not fully demonstrated. No population penetrance estimate follows from n=6. |
| **Human immune case — Danso-Abeam et al., 2013; n=1** | A patient carrying TRPV3 c.1718G>C (p.Gly573Ala) had recurrent skin infections, inflammatory lesional infiltrates, hyper-IgE, persistent eosinophilia, and increased circulating follicular T cells. (dansoabeam2013olmstedsyndromeexploration pages 1-3) | **Suggestive immune involvement only.** A single uncontrolled case cannot determine whether the abnormalities were primary effects of TRPV3 dysfunction, secondary to barrier failure or infection, or individual-specific. |
| **Genetic mouse study — Fatima et al., 4 Jan 2022** | Trpv3 p.Gly573Ser mice showed no spontaneous itch or dermatitis under *Staphylococcus aureus*-free conditions. Earlier DS-Nh phenotypes depended on *S. aureus* and genetic background; the tested 129S1/SvlmJ mutants instead had reduced pruritogen-evoked scratching, epidermal sensory hypoinnervation, and reduced cold and mechanical-pain responses. (fatima2022abnormalsomatosensorybehaviors pages 1-2, fatima2022abnormalsomatosensorybehaviors pages 2-3) | **Strong evidence for a model-specific gene–microbiome and genetic-background interaction**, but not proof of an equivalent interaction in human OS1. The model incompletely reproduces human mutilating palmoplantar keratoderma and cannot independently predict treatment efficacy. |
| **Human case — Hao et al., 14 Oct 2024; n=1** | Severe bilateral mutilating keratoderma preceded well-differentiated squamous-cell carcinoma of the sole requiring foot amputation. A heterozygous TRPV3 c.916G>A (p.Val306Met) missense variant was reported; computational predictions conflicted, and electrophysiologic validation was not performed. (hao2024casereportnovel pages 1-2, hao2024casereportnovel pages 2-5) | **Compelling malignancy event but uncertain molecular attribution.** The case supports surveillance of chronic ulcerated or changing lesions, but it neither establishes p.Val306Met as pathogenic nor quantifies OS1-associated cancer risk. |
| **Human treatment case — Zhang et al., 24 Jan 2025; n=1 treated** | Familial heterozygous TRPV3 c.1964T>C (p.Leu655Pro; p.L655P) was associated with focal keratoderma. The patient received **erlotinib plus oral acitretin**; plantar lesions and pain improved over 3–5 months, with mild stomach discomfort and transient forearm burning reported. (zhang2025erlotinibtherapyfor pages 1-2, zhang2025erlotinibtherapyfor pages 2-4, zhang2025erlotinibtherapyfor pages 4-6) | **Very-low-certainty therapeutic evidence:** an uncontrolled single case, combination therapy, no standardized endpoint, and short follow-up prevent attribution to erlotinib or calculation of a response rate. Because c.1964T>C produces an amino-acid substitution, p.L655P is a **missense**, not frameshift, variant despite contradictory wording in the report. |
| **Registered Phase 1 trial — NCT07090889; started 8 Jul 2025, completion estimated 21 Nov 2026** | Oral KM-023 is being evaluated in healthy volunteers and an open-label 12-week disease cohort of up to eight patients. Efficacy endpoints include plantar-callus thickness and size and Investigator Global Assessment. Eligibility accepts confirmed **TRPV3 or PERP** variants. No efficacy outcomes are available. (NCT07090889 chunk 1, NCT07090889 chunk 2) | **Prospective but not OS1-specific:** PERP-associated disease is molecularly distinct from TRPV3-associated OS1. Estimated enrollment is not an outcome, and the small open-label cohort will provide only preliminary safety, pharmacokinetic, and efficacy evidence rather than a validated response rate. |


*Table: Evidence-graded comparison of pivotal human, experimental, and trial records relevant to TRPV3-associated Olmsted syndrome 1. It distinguishes established findings from single-case inference, model limitations, variant uncertainty, and a trial that also enrolls non-OS1 disease.*

## 13. Prevention

**Primary:** no vaccine, diet, environmental intervention, or prophylactic medication prevents a confirmed germline OS1 variant. **Genetic counseling** permits family-specific assessment of dominant versus recessive recurrence risk and, where appropriate and desired, discussion of cascade testing, prenatal testing and preimplantation testing after a familial pathogenic allele is validated. These are reproductive options, not treatment or prevention of disease in someone carrying the variant. (duchatelet2015olmstedsyndromeclinical pages 7-8, duchatelet2015olmstedsyndromeclinical pages 5-7)

**Secondary/tertiary:** recognize childhood lesions promptly, address fissures and pain, protect function, manage infections, monitor progressive digit constriction, and assess visual complaints. Persistently **bleeding, ulcerated, enlarging or morphologically changing keratotic lesions warrant prompt dermatologic evaluation and biopsy**, given reported cancers, although no evidence-based OS1 surveillance interval is known. Population-wide newborn screening, prophylactic antibiotics, or preventive EGFR inhibition is not established. (duchatelet2015olmstedsyndromeclinical pages 4-5, hao2024casereportnovel pages 1-2, duchatelet2015olmstedsyndromeclinical pages 7-8)

## 14. Other species and naturally occurring disease

Orthologous **Trpv3** mutations occur in **mouse (*Mus musculus*, NCBI Taxon:10090)** and **rat (*Rattus norvegicus*, NCBI Taxon:10116)**. Naturally occurring **DS-Nh mice** carry p.Gly573Ser and **WBN/Kob-Ht rats** p.Gly573Cys at the homologous residue. Both can exhibit hairlessness and dermatitis, providing comparative evidence of conserved channel biology. They are **not evidence that the complete human OS1 disorder naturally occurs in those species**: the original human report notes rodent facial dermatitis and whole-body hairlessness **without paw keratosis**. Species-specific ortholog **NCBI Gene IDs** and breed **VBO identifiers** were not verified; DS-Nh and WBN/Kob-Ht are laboratory strains, not demonstrated companion-animal disease breeds. OS1 is inherited, not zoonotic or cross-species transmissible. (lin2012exomesequencingreveals pages 4-6, guo2023novelinsightsinto pages 3-4, fatima2022abnormalsomatosensorybehaviors pages 1-2)

## 15. Model organisms and research uses

* **Spontaneous genetic models:** DS-Nh **Trpv3^G573S** mice and WBN/Kob-Ht **Trpv3^G573C** rats model channel hyperactivity, hair abnormalities, itch and inflammation. A separately constructed G573S transgenic mouse has also been reported. Their major limitation is incomplete recreation of **mutilating human palmoplantar disease**. (lin2012exomesequencingreveals pages 4-6, guo2023novelinsightsinto pages 3-4)
* **Background/microbiome experiment:** a backcrossed **129S1/SvlmJ Trpv3^G573S** mouse under *S. aureus*-free housing **did not show spontaneous dermatitis or itch**; it exhibited epidermal sensory hypoinnervation and diminished responses to cold, mechanical pain and several pruritogens. Thus a model’s apparent antipruritic or pro-pruritic phenotype cannot be generalized without specifying genetic background, microbiological conditions and assay. Fatima *et al.*, **4 January 2022**, https://doi.org/10.3389/fnmol.2021.790435. (fatima2022abnormalsomatosensorybehaviors pages 1-2, fatima2022abnormalsomatosensorybehaviors pages 2-3)
* **Human cell models:** mutant-expressing **HEK293** cells establish channel-gating differences; **HaCaT keratinocytes** transfected with selected alleles show variant-dependent viability/apoptosis, ER-associated trafficking, adhesion and lysosomal phenotypes. These are mechanistic tests and compound-screening platforms, **not fully differentiated human soles or clinical efficacy models**. Original reports: Lin *et al.*, **2012**, https://doi.org/10.1016/j.ajhg.2012.02.006; Ni *et al.*, **2016**, https://doi.org/10.1038/srep21815; Yadav and Goswami, **2017**, https://doi.org/10.1080/19336950.2016.1249076. No validated OS1 patient-derived organoid, iPSC system, or verified MGI model accession was established here. (lin2012exomesequencingreveals pages 2-4, ni2016anovelmutation pages 3-4, yadav2017trpv3mutantscausing pages 1-4)

### Verbatim, traceable abstract excerpts

* **Human genetics / functional expression, 2012:** “In transfected HEK293 cells expressing TRPV3 mutants, much larger inward currents were recorded, probably because of the constitutive opening of the mutants.” The same abstract calls the apoptosis-to-hyperkeratosis connection something that the mutations **“might”** cause, distinguishing measurement from inference. https://doi.org/10.1016/j.ajhg.2012.02.006. (lin2012exomesequencingreveals pages 1-2)
* **Human immune case, 2013:** “The systemic phenotype of hyper IgE and persistent eosinophilia suggest a primary or secondary role of immunological processes in the pathogenesis of Olmsted syndrome.” **One patient**, not an established universal OS1 biomarker. https://doi.org/10.1186/1750-1172-8-79. (dansoabeam2013olmstedsyndromeexploration pages 1-3)
* **Recent clinical surveillance, 2024:** “The patient presented with disabling, bilateral palmoplantar keratoderma, and subsequently developed squamous cell carcinoma on the right sole.” This describes an event; the authors explicitly state additional experiments are needed to establish how **p.Val306Met** affects the channel. https://doi.org/10.3389/fonc.2024.1420555. (hao2024casereportnovel pages 1-2, hao2024casereportnovel pages 2-5)

**Knowledge-base import cautions:** Preserve **OS1 versus broad-OS denominators**, label hypothesized edges in the causal chain, capture variant-specific evidence instead of assigning gain of function to every case allele, record the 2025 **p.Leu655Pro missense/“frameshift” reporting inconsistency**, and keep trial enrollment separate from treatment response. Ontology accession numbers, HGNC accession, gnomAD frequencies, ClinVar classifications and PMIDs should be independently verified before structured import where not explicitly supported above. (duchatelet2015olmstedsyndromeclinical pages 1-2, hao2024casereportnovel pages 2-5, zhang2025erlotinibtherapyfor pages 2-4, NCT07090889 chunk 1)

References

1. (duchatelet2015olmstedsyndromeclinical pages 2-4): Sabine Duchatelet and Alain Hovnanian. Olmsted syndrome: clinical, molecular and therapeutic aspects. Orphanet Journal of Rare Diseases, Mar 2015. URL: https://doi.org/10.1186/s13023-015-0246-5, doi:10.1186/s13023-015-0246-5. This article has 130 citations and is from a peer-reviewed journal.

2. (kalinovskii2023trpv3ionchannel pages 13-14): Aleksandr P. Kalinovskii, Lyubov L. Utkina, Yuliya V. Korolkova, and Yaroslav A. Andreev. Trpv3 ion channel: from gene to pharmacology. International Journal of Molecular Sciences, 24:8601, May 2023. URL: https://doi.org/10.3390/ijms24108601, doi:10.3390/ijms24108601. This article has 30 citations.

3. (duchatelet2015olmstedsyndromeclinical pages 5-7): Sabine Duchatelet and Alain Hovnanian. Olmsted syndrome: clinical, molecular and therapeutic aspects. Orphanet Journal of Rare Diseases, Mar 2015. URL: https://doi.org/10.1186/s13023-015-0246-5, doi:10.1186/s13023-015-0246-5. This article has 130 citations and is from a peer-reviewed journal.

4. (lin2012exomesequencingreveals pages 1-2): Zhimiao Lin, Quan Chen, Mingyang Lee, Xu Cao, Jie Zhang, Donglai Ma, Long Chen, Xiaoping Hu, Huijun Wang, Xiaowen Wang, Peng Zhang, Xuanzhu Liu, Liping Guan, Yiquan Tang, Haizhen Yang, Ping Tu, Dingfang Bu, Xuejun Zhu, KeWei Wang, Ruoyu Li, and Yong Yang. Exome sequencing reveals mutations in trpv3 as a cause of olmsted syndrome. American journal of human genetics, 90 3:558-64, Mar 2012. URL: https://doi.org/10.1016/j.ajhg.2012.02.006, doi:10.1016/j.ajhg.2012.02.006. This article has 270 citations and is from a highest quality peer-reviewed journal.

5. (guo2023novelinsightsinto pages 6-8): Yaotao Guo, Yajuan Song, Wei Liu, Tong Wang, Xianjie I. Ma, and Zhou Yu. Novel insights into the role of keratinocytes-expressed trpv3 in the skin. Biomolecules, 13:513, Mar 2023. URL: https://doi.org/10.3390/biom13030513, doi:10.3390/biom13030513. This article has 37 citations.

6. (hao2024casereportnovel pages 1-2): Yangyang Hao, Rong Wu, Xi Chen, Yunjia Shen, Mengwei Chou, and Jianqiang Yang. Case report: novel p.val306met missense mutation in trpv3 in a case of olmsted syndrome accompanied by squamous cell carcinoma. Frontiers in Oncology, Oct 2024. URL: https://doi.org/10.3389/fonc.2024.1420555, doi:10.3389/fonc.2024.1420555. This article has 0 citations.

7. (duchatelet2015olmstedsyndromeclinical pages 1-2): Sabine Duchatelet and Alain Hovnanian. Olmsted syndrome: clinical, molecular and therapeutic aspects. Orphanet Journal of Rare Diseases, Mar 2015. URL: https://doi.org/10.1186/s13023-015-0246-5, doi:10.1186/s13023-015-0246-5. This article has 130 citations and is from a peer-reviewed journal.

8. (lin2012exomesequencingreveals pages 2-4): Zhimiao Lin, Quan Chen, Mingyang Lee, Xu Cao, Jie Zhang, Donglai Ma, Long Chen, Xiaoping Hu, Huijun Wang, Xiaowen Wang, Peng Zhang, Xuanzhu Liu, Liping Guan, Yiquan Tang, Haizhen Yang, Ping Tu, Dingfang Bu, Xuejun Zhu, KeWei Wang, Ruoyu Li, and Yong Yang. Exome sequencing reveals mutations in trpv3 as a cause of olmsted syndrome. American journal of human genetics, 90 3:558-64, Mar 2012. URL: https://doi.org/10.1016/j.ajhg.2012.02.006, doi:10.1016/j.ajhg.2012.02.006. This article has 270 citations and is from a highest quality peer-reviewed journal.

9. (duchatelet2015olmstedsyndromeclinical pages 4-5): Sabine Duchatelet and Alain Hovnanian. Olmsted syndrome: clinical, molecular and therapeutic aspects. Orphanet Journal of Rare Diseases, Mar 2015. URL: https://doi.org/10.1186/s13023-015-0246-5, doi:10.1186/s13023-015-0246-5. This article has 130 citations and is from a peer-reviewed journal.

10. (fatima2022abnormalsomatosensorybehaviors pages 1-2): Mahar Fatima, Hannah Slade, Lorraine R Horwitz, Angela Shi, Jingyi Liu, Delaney McKinstry, Troy Villani, Haoxing Xu, and Bo Duan. Abnormal somatosensory behaviors associated with a gain-of-function mutation in trpv3 channels. Frontiers in Molecular Neuroscience, Jan 2022. URL: https://doi.org/10.3389/fnmol.2021.790435, doi:10.3389/fnmol.2021.790435. This article has 11 citations.

11. (dansoabeam2013olmstedsyndromeexploration pages 1-3): Dina Danso-Abeam, Jianguo Zhang, James Dooley, Kim A Staats, Lien Van Eyck, Thomas Van Brussel, Shari Zaman, Esther Hauben, Marc Van de Velde, Marie-Anne Morren, Marleen Renard, Christel Van Geet, Heidi Schaballie, Diether Lambrechts, Jinsheng Tao, Dean Franckaert, Stephanie Humblet-Baron, Isabelle Meyts, and Adrian Liston. Olmsted syndrome: exploration of the immunological phenotype. Orphanet Journal of Rare Diseases, 8:79-79, May 2013. URL: https://doi.org/10.1186/1750-1172-8-79, doi:10.1186/1750-1172-8-79. This article has 69 citations and is from a peer-reviewed journal.

12. (ni2016anovelmutation pages 3-4): Cheng Ni, Ming Yan, Jia Zhang, Ruhong Cheng, Jianying Liang, Dan Deng, Zhen Wang, Ming Li, and Zhirong Yao. A novel mutation in trpv3 gene causes atypical familial olmsted syndrome. Scientific Reports, Feb 2016. URL: https://doi.org/10.1038/srep21815, doi:10.1038/srep21815. This article has 54 citations and is from a peer-reviewed journal.

13. (zhang2025erlotinibtherapyfor pages 2-4): Jia Zhang, MengYue Guo, DongYang Yuan, JinYang Wei, and Hongzhou Cui. Erlotinib therapy for olmsted syndrome with p.l655p missense mutation in the trpv3 gene: a case report. Frontiers in Medicine, Jan 2025. URL: https://doi.org/10.3389/fmed.2025.1512673, doi:10.3389/fmed.2025.1512673. This article has 3 citations.

14. (hao2024casereportnovel pages 2-5): Yangyang Hao, Rong Wu, Xi Chen, Yunjia Shen, Mengwei Chou, and Jianqiang Yang. Case report: novel p.val306met missense mutation in trpv3 in a case of olmsted syndrome accompanied by squamous cell carcinoma. Frontiers in Oncology, Oct 2024. URL: https://doi.org/10.3389/fonc.2024.1420555, doi:10.3389/fonc.2024.1420555. This article has 0 citations.

15. (duchatelet2015olmstedsyndromeclinical pages 7-8): Sabine Duchatelet and Alain Hovnanian. Olmsted syndrome: clinical, molecular and therapeutic aspects. Orphanet Journal of Rare Diseases, Mar 2015. URL: https://doi.org/10.1186/s13023-015-0246-5, doi:10.1186/s13023-015-0246-5. This article has 130 citations and is from a peer-reviewed journal.

16. (lin2012exomesequencingreveals pages 4-6): Zhimiao Lin, Quan Chen, Mingyang Lee, Xu Cao, Jie Zhang, Donglai Ma, Long Chen, Xiaoping Hu, Huijun Wang, Xiaowen Wang, Peng Zhang, Xuanzhu Liu, Liping Guan, Yiquan Tang, Haizhen Yang, Ping Tu, Dingfang Bu, Xuejun Zhu, KeWei Wang, Ruoyu Li, and Yong Yang. Exome sequencing reveals mutations in trpv3 as a cause of olmsted syndrome. American journal of human genetics, 90 3:558-64, Mar 2012. URL: https://doi.org/10.1016/j.ajhg.2012.02.006, doi:10.1016/j.ajhg.2012.02.006. This article has 270 citations and is from a highest quality peer-reviewed journal.

17. (zhang2025erlotinibtherapyfor pages 1-2): Jia Zhang, MengYue Guo, DongYang Yuan, JinYang Wei, and Hongzhou Cui. Erlotinib therapy for olmsted syndrome with p.l655p missense mutation in the trpv3 gene: a case report. Frontiers in Medicine, Jan 2025. URL: https://doi.org/10.3389/fmed.2025.1512673, doi:10.3389/fmed.2025.1512673. This article has 3 citations.

18. (yadav2017trpv3mutantscausing pages 1-4): Manoj Yadav and Chandan Goswami. Trpv3 mutants causing olmsted syndrome induce impaired cell adhesion and nonfunctional lysosomes. Channels, 11:196-208, Feb 2017. URL: https://doi.org/10.1080/19336950.2016.1249076, doi:10.1080/19336950.2016.1249076. This article has 37 citations and is from a peer-reviewed journal.

19. (yadav2017trpv3mutantscausing pages 4-6): Manoj Yadav and Chandan Goswami. Trpv3 mutants causing olmsted syndrome induce impaired cell adhesion and nonfunctional lysosomes. Channels, 11:196-208, Feb 2017. URL: https://doi.org/10.1080/19336950.2016.1249076, doi:10.1080/19336950.2016.1249076. This article has 37 citations and is from a peer-reviewed journal.

20. (zhang2025erlotinibtherapyfor pages 4-6): Jia Zhang, MengYue Guo, DongYang Yuan, JinYang Wei, and Hongzhou Cui. Erlotinib therapy for olmsted syndrome with p.l655p missense mutation in the trpv3 gene: a case report. Frontiers in Medicine, Jan 2025. URL: https://doi.org/10.3389/fmed.2025.1512673, doi:10.3389/fmed.2025.1512673. This article has 3 citations.

21. (guo2023novelinsightsinto pages 3-4): Yaotao Guo, Yajuan Song, Wei Liu, Tong Wang, Xianjie I. Ma, and Zhou Yu. Novel insights into the role of keratinocytes-expressed trpv3 in the skin. Biomolecules, 13:513, Mar 2023. URL: https://doi.org/10.3390/biom13030513, doi:10.3390/biom13030513. This article has 37 citations.

22. (duchatelet2015olmstedsyndromeclinical pages 8-9): Sabine Duchatelet and Alain Hovnanian. Olmsted syndrome: clinical, molecular and therapeutic aspects. Orphanet Journal of Rare Diseases, Mar 2015. URL: https://doi.org/10.1186/s13023-015-0246-5, doi:10.1186/s13023-015-0246-5. This article has 130 citations and is from a peer-reviewed journal.

23. (NCT07090889 chunk 1):  Study of KM-023 in Healthy Volunteers and Patients With Olmsted Syndrome.. Orvida Pharma (formerly Kamari Pharma). 2025. ClinicalTrials.gov Identifier: NCT07090889

24. (zhang2025erlotinibtherapyfor pages 6-7): Jia Zhang, MengYue Guo, DongYang Yuan, JinYang Wei, and Hongzhou Cui. Erlotinib therapy for olmsted syndrome with p.l655p missense mutation in the trpv3 gene: a case report. Frontiers in Medicine, Jan 2025. URL: https://doi.org/10.3389/fmed.2025.1512673, doi:10.3389/fmed.2025.1512673. This article has 3 citations.

25. (zhang2025erlotinibtherapyfor pages 6-6): Jia Zhang, MengYue Guo, DongYang Yuan, JinYang Wei, and Hongzhou Cui. Erlotinib therapy for olmsted syndrome with p.l655p missense mutation in the trpv3 gene: a case report. Frontiers in Medicine, Jan 2025. URL: https://doi.org/10.3389/fmed.2025.1512673, doi:10.3389/fmed.2025.1512673. This article has 3 citations.

26. (NCT07090889 chunk 2):  Study of KM-023 in Healthy Volunteers and Patients With Olmsted Syndrome.. Orvida Pharma (formerly Kamari Pharma). 2025. ClinicalTrials.gov Identifier: NCT07090889

27. (NCT05435638 chunk 1):  Study Designed to Evaluate Safety and Efficacy of 1% Topical Formulation of KM-001 on Type 1 Punctate Palmoplantar Keratoderma or Pachyonychia Congenita Diseases. Orvida Pharma (formerly Kamari Pharma). 2022. ClinicalTrials.gov Identifier: NCT05435638

28. (NCT05956314 chunk 1):  Assessment of KM-001 - Safety, Tolerability, and Efficacy in Patients With PPPK1 or PC. Orvida Pharma (formerly Kamari Pharma). 2023. ClinicalTrials.gov Identifier: NCT05956314

29. (NCT06545695 chunk 1): Amy Paller. Epidermal Growth Factor Receptor Inhibition for Keratinopathies. Northwestern University. 2027. ClinicalTrials.gov Identifier: NCT06545695

30. (fatima2022abnormalsomatosensorybehaviors pages 2-3): Mahar Fatima, Hannah Slade, Lorraine R Horwitz, Angela Shi, Jingyi Liu, Delaney McKinstry, Troy Villani, Haoxing Xu, and Bo Duan. Abnormal somatosensory behaviors associated with a gain-of-function mutation in trpv3 channels. Frontiers in Molecular Neuroscience, Jan 2022. URL: https://doi.org/10.3389/fnmol.2021.790435, doi:10.3389/fnmol.2021.790435. This article has 11 citations.

## Artifacts

- [Edison artifact artifact-00](Olmsted_Syndrome_1-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 4 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0100296` (2 mentions) - the report calls it "if available"; MONDO calls it **Olmsted syndrome 1**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `Taxon`.