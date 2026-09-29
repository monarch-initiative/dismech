---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-05T19:49:56.126704'
end_time: '2026-09-05T19:58:38.098076'
duration_seconds: 521.97
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Persistent Mullerian Duct Syndrome
  mondo_id: MONDO:0009857
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 13
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 22
  verified: 20
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0009857
    reported_labels:
    - if available
    ontology_label: persistent Mullerian duct syndrome
  unresolvable_prefixes:
  - Orphanet
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Persistent_Mullerian_Duct_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Persistent Mullerian Duct Syndrome
- **MONDO ID:** MONDO:0009857 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Persistent Mullerian Duct Syndrome** covering all of the
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
- **Disease Name:** Persistent Mullerian Duct Syndrome
- **MONDO ID:** MONDO:0009857 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Persistent Mullerian Duct Syndrome** covering all of the
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


# Persistent Müllerian Duct Syndrome (PMDS): Disease-Characteristics Research Report

**Scope and evidence date.** This report synthesizes literature retrieved through December 2024. PMDS is exceptionally rare; consequently, most evidence consists of referral cohorts, retrospective surgical series, case reports, and animal models rather than population studies or controlled trials. Percentages from the 157-case expert series are particularly vulnerable to referral and survivorship bias and should not be interpreted as population risks.

## Executive summary

Persistent Müllerian duct syndrome is a congenital, usually autosomal-recessive 46,XY difference/disorder of sex development in which Müllerian derivatives—uterus, fallopian tubes, and upper vagina—persist despite otherwise normal male virilization. Biallelic loss-of-function variants in **AMH** or **AMHR2** explain approximately 86–88% of molecularly investigated cases. Testosterone-dependent differentiation remains intact, explaining the normal male external genitalia and Wolffian derivatives. Clinical recognition usually follows surgery or imaging for cryptorchidism, inguinal hernia, transverse testicular ectopia, or infertility. Management centers on early localization and preservation of viable testes, protection of the vasa deferentia and testicular vessels, selective removal or surveillance of Müllerian remnants, fertility counseling, and tumor surveillance. There is no pharmacological or prenatal treatment capable of reversing an established embryonic developmental anomaly. (liu2022identificationofamh pages 5-6, cima2024persistentmüllerianduct pages 12-13, mullen2019amhandamhr2 pages 1-2)

The following matrix summarizes the most actionable evidence.

| Domain | Best-supported finding | Quantitative detail | Evidence type/source/date | Ontology-ready annotation |
|---|---|---|---|---|
| Definition / identifiers | PMDS is a congenital disorder of sex development in otherwise normally virilized 46,XY males, characterized by persistence of Müllerian derivatives such as the uterus, fallopian tubes, and upper vagina. | MONDO:0009857; Orphanet:2856 | Aggregated disease-target resource and 2024 human review/case report (OpenTargets Search: Persistent Mullerian duct syndrome-AMH,AMHR2, cima2024persistentmüllerianduct pages 12-13) | MONDO:0009857; 46,XY DSD; persistent Müllerian derivatives |
| Causal genes | Biallelic loss-of-function variants in **AMH** cause deficient hormone activity (type 1); biallelic **AMHR2** variants cause receptor resistance (type 2). | Approximately 88% of cases have homozygous or compound-heterozygous variants in these genes; one 157-case review found AMH variants in 40.4%, AMHR2 variants in 45.7%, and neither in 13.9%. | Human cohort/reviews, 2017–2024 (OpenTargets Search: Persistent Mullerian duct syndrome-AMH,AMHR2, liu2022identificationofamh pages 5-6, cima2024persistentmüllerianduct pages 12-13) | Genes: AMH, AMHR2; mechanism: germline loss of function; inheritance: autosomal recessive |
| Pathogenic variants | Variant classes include missense, nonsense, frameshift, splice, insertion/deletion, and AMHR2 microdeletions. A recurrent 27-bp AMHR2 kinase-domain deletion is enriched in patients of Northern European origin. | Recurrent deletion reported in 30 patients; 2024 AMHR2 c.1046T>C (p.Ile349Thr) had gnomAD frequency 0.00001591 and no homozygotes. | Human molecular cohorts/reviews and 2024 case report (cima2024persistentmüllerianduct pages 17-19, cima2024persistentmüllerianduct pages 7-10) | Sequence variants in AMH/AMHR2; germline; pathogenic/likely pathogenic/VUS classification per ACMG/AMP |
| Core phenotypes | Principal presentations are bilateral cryptorchidism, unilateral cryptorchidism with contralateral hernia containing Müllerian structures, and transverse testicular ectopia; external virilization is usually normal. | Bilateral intra-abdominal testes approximately 60–70%; hernia uteri inguinalis approximately 20–30%; transverse testicular ectopia approximately 10% in one review. A 2024 review grouped approximately 80% as the bilateral intra-abdominal “female form” and 20% as male forms. | Human case-series/reviews, 2017–2024 (liu2022identificationofamh pages 5-6, cima2024persistentmüllerianduct pages 12-13) | Cryptorchidism; inguinal hernia; transverse testicular ectopia; uterus/fallopian-tube/upper-vaginal remnants; normal male external genitalia |
| Diagnosis | Suspect PMDS in bilateral cryptorchidism, transverse testicular ectopia, or an inguinal hernia containing uterus-like tissue. Evaluation combines examination, ultrasonography/MRI, 46,XY karyotype, serum AMH, laparoscopy/pathology, and AMH/AMHR2 sequencing with copy-number analysis when needed. | In a 2022 study, 3 of 11 unrelated cryptorchidism patients had biallelic AMH/AMHR2 variants. MRI demonstrated Müllerian remnants in all three. | Human molecular case series, January 2022 (liu2022identificationofamh pages 6-8, liu2022identificationofamh pages 2-5) | Diagnostic procedures: pelvic ultrasound, pelvic MRI, laparoscopy, karyotype, serum AMH, germline sequencing, CNV analysis, histopathology |
| Biomarkers | Very low or undetectable AMH supports AMH deficiency; normal or elevated AMH supports AMHR2 resistance, but age- and assay-specific interpretation is essential. Testosterone is generally preserved because Leydig-cell androgen production is not the primary defect. | Example AMH values in a 2022 series: 0.06, 3.21, and 7.72 ng/mL; the 2024 AMHR2 p.Ile349Thr case had age-appropriate AMH. | Human case series/case report, 2022 and 2024 (liu2022identificationofamh pages 2-5, cima2024persistentmüllerianduct pages 7-10) | Biomarkers: anti-Müllerian hormone, testosterone, inhibin B, LH, FSH; genotype–biomarker correlation |
| Malignancy / fertility | Cancer risk is driven mainly by undescended testes; malignant transformation of Müllerian remnants is reported but less frequent. Fertility is uncommon but possible if at least one testis is scrotal and its excretory ducts remain intact. | Testicular malignant degeneration was reported in 33% of adults in a selected 157-case experience; other literature estimates range from 3.1–8.4% to 5–18%. Approximately 19% reportedly fathered a child naturally. | Human referral cohort and literature reviews, 2017–2022 (cima2024persistentmüllerianduct pages 17-19, liu2022identificationofamh pages 6-8, krzeminska2024persistentmullerianduct pages 1-3, mullen2019amhandamhr2 pages 1-2) | Complications: testicular neoplasm, Müllerian-remnant neoplasm, azoospermia, oligospermia, male infertility |
| Management | Management is individualized: early orchiopexy when feasible, careful laparoscopic assessment, and selective subtotal/complete resection or retention of Müllerian remnants. Preservation of the vas deferens and testicular blood supply takes priority; retained remnants require surveillance. | In a 12-patient Chinese series, 8 underwent orchiopexy with uterine preservation; 3 later developed remnant cysts. Three underwent subtotal hysterectomy; one sustained vas deferens injury and one postoperative hemorrhage. | Human surgical cohort, 2022 (cima2024persistentmüllerianduct pages 16-17) | Interventions: orchiopexy, laparoscopy, hysterectomy/remnant excision, orchidectomy when indicated, fertility preservation, imaging surveillance |
| 2024 advances | A previously unreported homozygous AMHR2 kinase-domain variant was associated with PMDS and supernumerary testes. Biochemical research also mapped AMH residues involved in type-I and type-II receptor interactions and improved precursor processing, refining understanding of receptor-complex assembly. | AMHR2 NM_020547.3:c.1046T>C (p.Ile349Thr), classified likely pathogenic; engineered AMH variants increased potency approximately 5- to 10-fold in vitro. | Human case report/review and experimental protein study, November–December 2024 (cima2024persistentmüllerianduct pages 7-10) | AMHR2 protein-kinase domain; AMH processing; ligand–receptor binding; TGF-β/BMP-family signaling |
| Mouse model | Homozygous Amh- or Amhr2-null male mice retain uterus, oviducts, and partial vagina despite normal testes and Wolffian derivatives, recapitulating the core human developmental lesion. Progressive seminiferous epithelial atrophy models downstream subfertility. | Amhr2-null males sired offspring at less than a 50% rate; focal tubular atrophy appeared by 2 months and markedly impaired spermatogenesis by 9 months. | Targeted knockout model/review, 2019 (mullen2019amhandamhr2 pages 4-5) | Model: Amh knockout, Amhr2 knockout; phenotypes: persistent Müllerian structures, testicular atrophy, reduced male fertility |
| Canine natural disease | Miniature Schnauzers have sex-limited autosomal-recessive PMDS caused by AMHR2 c.241C>T (p.Arg81*); affected XY dogs retain oviducts, uterus, cervix, and cranial vagina and may have cryptorchidism. | Among 216 North American Miniature Schnauzers, mutant-allele frequency was 0.16 and carrier frequency 0.27; approximately 50% of affected dogs had unilateral or bilateral cryptorchidism. | Natural veterinary cohort and comparative review, 2018–2019 (mullen2019amhandamhr2 pages 4-5, smit2018prevalenceofthe pages 1-2) | Species: dog; breed: Miniature Schnauzer; gene: AMHR2; variant: c.241C>T (p.Arg81*); autosomal recessive, sex limited |
| Canine 2024 genomics | Recent comparative analysis identified technical blind spots in canine PMDS sequencing: GC-rich repetitive AMH exon 5 has poor coverage, and AMHR2 annotation differs among canine genome assemblies. Targeted resequencing may resolve genetically unexplained cases in other breeds. | CanFam3.1 represented 11 AMHR2 coding exons with complete deep coverage; ROS_Cfam_1.0 represented only 8. | Computational genomics preprint, posted December 4, 2024 (krzeminska2024persistentmullerianduct pages 3-7, krzeminska2024persistentmullerianduct pages 7-9, krzeminska2024persistentmullerianduct pages 12-17) | Comparative genomics; AMH exon 5; AMHR2 structural annotation; targeted resequencing |


*Table: Concise evidence matrix covering PMDS definition, genetics, clinical features, diagnosis, outcomes, management, recent advances, and comparative models. Quantitative estimates are tied to their underlying evidence type and should be interpreted cautiously because most human data derive from rare-disease referral cohorts and case series.*

## 1. Disease information

### Definition and classification

PMDS is a **Mendelian congenital 46,XY DSD** characterized by persistent Müllerian structures in an otherwise normally virilized male. It is not synonymous with ambiguous genitalia: Leydig-cell testosterone production and androgen response are ordinarily intact. One recent abstract defines it as “a rare autosomal recessive disorder of sexual development in males, defined by the presence of Müllerian remnants with otherwise normal sexual differentiation.” (liu2022identificationofamh pages 5-6, cima2024persistentmüllerianduct pages 12-13)

**Identifiers and synonyms**

- **MONDO:** MONDO:0009857.
- **Orphanet:** ORPHA:2856.
- **OMIM:** commonly represented as PMDS type 1/AMH-related disease (**OMIM 261550**) and PMDS type 2/AMHR2-related disease (**OMIM 600956**); these identifiers should be checked against the current OMIM release before automated ingestion.
- **MeSH:** no uniquely granular PMDS descriptor was established in the retrieved evidence; indexing commonly falls under disorders of sex development, cryptorchidism, and Müllerian ducts.
- **ICD-10/ICD-11:** no PMDS-specific billable code was verified. Coding generally uses congenital malformations/differences of genital development plus cryptorchidism or hernia codes; local coding rules should be applied.
- **Synonyms:** persistent Müllerian duct syndrome; Müllerian duct persistence syndrome; PMDS; persistent Müllerian derivatives; AMH deficiency/PMDS type 1; AMH-receptor resistance or AMHR2 deficiency/PMDS type 2; historically, *hernia uteri inguinalis* for one presentation.

OpenTargets independently links MONDO:0009857 and ORPHA:2856 to **AMH** and **AMHR2**, with supporting literature including PMIDs **28528332, 8872466, 8162013, and 23295284**. (OpenTargets Search: Persistent Mullerian duct syndrome-AMH,AMHR2)

**Data provenance:** these are aggregated disease-level findings derived from curated resources and published cases/cohorts, not individual EHR data. The 2022 and 2024 clinical publications contain patient-level observations, but this report does not reproduce identifiable patient records.

## 2. Etiology, risk, protective, and environmental factors

### Primary cause

The initiating cause is defective fetal AMH signaling:

1. **Type 1 PMDS:** biallelic pathogenic **AMH** variants cause absent, reduced, improperly processed, or biologically inactive ligand.
2. **Type 2 PMDS:** biallelic pathogenic **AMHR2** variants cause receptor deficiency or resistance despite normal or elevated circulating AMH.
3. **Genetically unresolved PMDS:** approximately 12–14% of historical cases lacked detectable AMH/AMHR2 variants. Rare truncating **PPP1R12A** variants have subsequently implicated myosin-phosphatase/cytoskeletal regulation in Müllerian regression, but this is not yet as firmly established as AMH/AMHR2 disease. (liu2022identificationofamh pages 5-6, cima2024persistentmüllerianduct pages 12-13, cima2024persistentmüllerianduct pages 17-19)

### Risk factors

- **Genetic:** two pathogenic alleles in AMH or AMHR2; parental consanguinity increases the probability of homozygosity. A recurrent 27-bp AMHR2 kinase-domain deletion was reported in 30 patients, mainly of Northern European ancestry, consistent with a founder-enriched allele. (cima2024persistentmüllerianduct pages 17-19)
- **Family history:** affected brothers and carrier parents are expected under autosomal-recessive inheritance. Females carrying biallelic defects do not develop the male PMDS anatomy because Müllerian structures are normally retained in females.
- **Sex/chromosomal context:** the defining phenotype occurs in individuals with testes, usually 46,XY, because failure is specifically failure of male fetal Müllerian regression.

No reproducible **environmental, infectious, occupational, dietary, smoking, alcohol, age-related, or lifestyle cause** has been demonstrated. No protective genetic allele, diet, medication, or exposure is known. PMDS is established during a critical fetal developmental window; postnatal lifestyle cannot prevent it. Gene–environment interactions, GWAS susceptibility loci, and polygenic risk scores have not been established.

## 3. Phenotypes

| Phenotype | Characteristics and frequency | Suggested HPO term |
|---|---|---|
| Persistent uterus/tubes/upper vagina | Congenital and lifelong unless resected; often asymptomatic and discovered intraoperatively | **Persistent Müllerian duct structures** (use current HPO label/ID); abnormality of internal genitalia |
| Cryptorchidism | Most common presentation; bilateral intra-abdominal testes reported in approximately 60–70%; 2024 review’s “female form” ≈80% | HP:0000028 Cryptorchidism; bilateral cryptorchidism |
| Inguinal hernia/*hernia uteri inguinalis* | Uterus/tube and sometimes testis in a hernia; approximately 20–30% in one synthesis | HP:0000023 Inguinal hernia |
| Transverse testicular ectopia | Both testes migrate toward one hemiscrotum/inguinal canal; estimates vary around 10%, or higher in selected mutation-positive series | Testicular ectopia; transverse testicular ectopia |
| Male infertility | Usually recognized in adulthood; azoospermia, severe oligospermia, duct injury/obstruction, cryptorchid testicular damage | HP:0003251 Male infertility; HP:0000027 Azoospermia; oligozoospermia |
| Abnormal vas/excretory ducts | Frequent; vas may run tightly along uterus/tubes, creating surgical risk | Abnormal vas deferens morphology; obstructive azoospermia |
| Testicular hypoplasia/atrophy | Variable, worsens with prolonged ectopia; 2024 case had hypoplastic testes and absent spermatogenesis | HP:0008734 Decreased testicular size; testicular atrophy |
| Müllerian-remnant cysts | May arise after preservation; 3/8 patients after uterine preservation in one surgical cohort | Müllerian duct cyst |
| Neoplasia | Predominantly undescended-testis germ-cell tumors; rarer Müllerian-derived carcinomas/sarcomas | Testicular neoplasm; neoplasm of uterus |

The three canonical anatomical presentations are bilateral cryptorchidism, unilateral cryptorchidism with contralateral hernia, and transverse testicular ectopia. Reported proportions differ because categories, referral patterns, and mutation ascertainment differ. (liu2022identificationofamh pages 5-6, cima2024persistentmüllerianduct pages 12-13, mullen2019amhandamhr2 pages 1-2)

**Onset and course:** the lesion is congenital, but clinical detection ranges from infancy during hernia/cryptorchidism surgery to adulthood during infertility or hematospermia evaluation. Müllerian persistence itself is stable; testicular degeneration, infertility, remnant cysts, and cancer risk are progressive secondary consequences. No behavioral or neuropsychiatric phenotype is established as part of classical biallelic PMDS.

**Quality of life:** no PMDS-specific EQ-5D, SF-36, PROMIS, or validated patient-reported outcome study was found. Likely burdens include repeated operations, infertility, cancer anxiety, surveillance, and possible psychosocial effects of a DSD diagnosis. These should not be converted into quantitative QOL estimates without direct data.

## 4. Genetic and molecular information

### Causal genes and proteins

- **AMH** (HGNC symbol AMH; Ensembl **ENSG00000104899**): TGF-β-superfamily ligand produced by fetal Sertoli cells. Pathogenic mechanism is predominantly **germline loss of function**.
- **AMHR2** (Ensembl **ENSG00000135409**): ligand-specific transmembrane serine/threonine kinase receptor. Pathogenic mechanisms include impaired expression, trafficking, ligand binding, kinase signaling, or receptor stability. (OpenTargets Search: Persistent Mullerian duct syndrome-AMH,AMHR2, cima2024persistentmüllerianduct pages 17-19)

A 157-case synthesis found AMH variants in 40.4%, AMHR2 variants in 45.7%, and neither in 13.9%. By 2017, 80 families carrying 64 AMH mutations and 75 families carrying 58 AMHR2 alleles had been reported. Variant classes include missense, nonsense, frameshift, splice-site, insertion/deletion, in-frame deletion, and exon-level microdeletion. (liu2022identificationofamh pages 5-6, cima2024persistentmüllerianduct pages 17-19)

### Illustrative variants

- **AMH NM_000479:c.321_324del, p.Gln109LeufsTer29:** homozygous frameshift, predicted loss of function; reported as likely pathogenic.
- **AMHR2 c.494_502del, p.Ile165_Ala168delinsThr; p.Glu390Lys; p.Met439Val**, and a splice-region variant were found in adult infertility cases; classifications ranged from pathogenic/likely pathogenic to VUS, emphasizing the need for variant-specific ACMG assessment. (liu2022identificationofamh pages 5-6)
- **AMHR2 NM_020547.3:c.1046T>C, p.Ile349Thr:** 2024 homozygous likely-pathogenic kinase-domain variant; gnomAD frequency **0.00001591**, with no homozygotes. The associated phenotype included PMDS and supernumerary testes. (cima2024persistentmüllerianduct pages 7-10)
- **Recurrent AMHR2 27-bp kinase-domain deletion:** reported in 30 patients, mainly Northern European. (cima2024persistentmüllerianduct pages 17-19)

Variants are constitutional/germline, not somatic drivers. Individual allele frequencies must be retrieved from the current gnomAD release and transcript-matched; most pathogenic alleles are absent or extremely rare. No validated modifier gene, protective allele, anticipation, or recurrent germline mosaicism pattern is established. No disease-defining methylation, histone, chromatin, metabolomic, proteomic, lipidomic, or single-cell signature has been validated.

## 5. Environmental information

Environmental toxins, radiation, pollution, medications, maternal infection, diet, exercise, smoking, and alcohol have not been established as causes or modifiers. PMDS is not infectious and has no zoonotic transmission. Environmental and lifestyle fields should therefore be recorded as **not established/not applicable**, rather than “negative exposure.”

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic AMH loss-of-function or AMHR2 loss-of-function/resistance leads to insufficient AMH signaling during the male fetal Müllerian-regression window.**
2. **Insufficient ligand–receptor signaling leads to failure to assemble/activate the AMHR2–type-I BMP receptor complex** in Müllerian-duct mesenchyme; ACVR1 and BMPR1A are implicated type-I receptors. (krzeminska2024persistentmullerianduct pages 1-3, mullen2019amhandamhr2 pages 1-2)
3. **Reduced receptor serine/threonine-kinase activity leads to deficient downstream SMAD-mediated transcription and mesenchymal remodeling**; the exact human cell-death/remodeling sequence is substantially inferred from developmental models rather than directly demonstrated in affected fetuses.
4. **Failure of epithelial–mesenchymal regression leads to persistence of uterus, fallopian tubes, and upper vagina.**
5. **Preserved fetal Leydig-cell testosterone leads to normal Wolffian derivatives, male external genitalia, and usual pubertal virilization**, creating the characteristic discordance between external and internal anatomy. (cima2024persistentmüllerianduct pages 12-13)
6. **Persistent Müllerian structures and abnormal genito-inguinal ligament/gubernacular shortening lead to mechanically restricted testicular descent**, producing bilateral cryptorchidism, hernia uteri inguinalis, or transverse ectopia. (cima2024persistentmüllerianduct pages 12-13)
7. **Chronic testicular malposition plus ductal distortion and surgical vulnerability leads to impaired spermatogenesis, obstruction, azoospermia/oligospermia, and infertility.**
8. **Cryptorchid testicular tissue leads to increased germ-cell tumor risk; retained Müllerian epithelium can independently lead, much less often, to Müllerian-derived malignancy.** (cima2024persistentmüllerianduct pages 17-19, liu2022identificationofamh pages 6-8, mullen2019amhandamhr2 pages 1-2)

**Upstream:** ligand production/processing, AMHR2 binding, receptor trafficking and kinase activity. **Downstream:** SMAD transcription, Müllerian mesenchymal remodeling, gubernacular/testicular positioning, later heat-associated testicular damage and neoplasia.

**Suggested GO annotations:** GO:0001701 in utero embryonic development; GO:0008585 female gonad development is not appropriate for the male lesion; use Müllerian duct development/regression where available; GO:0007179 TGF-β receptor signaling pathway; GO:0060395 SMAD protein signal transduction; GO:0007283 spermatogenesis; GO:0043067 regulation of programmed cell death when supported by model-specific evidence. **Cell types:** Sertoli cell (CL:0000216), Müllerian-duct mesenchymal cell, Müllerian-duct epithelial cell, Leydig cell (CL:0000178), germ cell/spermatogonium. **Subcellular sites:** secretory pathway for AMH; plasma membrane and cytoplasmic kinase domain for AMHR2; cytosol/nucleus for SMAD transduction.

There is no established primary metabolic, immune, inflammatory, oxidative-stress, mitochondrial, lysosomal, or ion-channel mechanism. Advanced single-cell, spatial-transcriptomic, and multi-omics studies directly profiling human PMDS were not found.

## 7. Anatomical structures affected

**Primary:** Müllerian ducts and derivatives—uterus, uterine tubes, cervix/upper vagina—plus testes whose descent is mechanically disturbed. **Secondary:** epididymides, vasa deferentia, seminal outflow tract, gubernacula, inguinal canals, and scrotum. Müllerian remnants may be midline; testes may be bilateral intra-abdominal, unilateral, inguinal, crossed, or both on one side. (cima2024persistentmüllerianduct pages 12-13, liu2022identificationofamh pages 6-8)

**Suggested UBERON mappings:** Müllerian duct; uterus (UBERON:0000995); uterine tube (UBERON:0003889); vagina (UBERON:0000996); testis (UBERON:0000473); vas deferens (UBERON:0001000); epididymis (UBERON:0001301); gubernaculum; inguinal canal; scrotum. IDs should be validated against the current ontology release before ingestion.

## 8. Temporal development

- **Initiation:** congenital, during fetal sex differentiation and Müllerian regression.
- **Early clinical stage:** cryptorchidism, inguinal hernia, or ectopia in infancy/childhood.
- **Intermediate:** repeated orchiopexy, re-ascent, remnant cysts, or progressive testicular atrophy.
- **Adult presentation:** infertility, azoospermia/oligospermia, hematospermia, or tumor.
- **Course:** lifelong unless remnants are removed; complications accumulate variably rather than following a standardized staging system.

The principal intervention window is early childhood, when recognition during cryptorchidism/hernia assessment can prevent repeated surgery and permit timely orchiopexy. A 2024 case underwent multiple operations before molecular recognition, illustrating the real-world cost of low awareness. (cima2024persistentmüllerianduct pages 12-13, cima2024persistentmüllerianduct pages 7-10)

## 9. Inheritance and population

PMDS is usually **autosomal recessive and sex-limited in phenotypic expression**. Penetrance of Müllerian persistence appears high for biallelic severe AMH/AMHR2 defects, whereas the position and viability of testes and fertility show variable expressivity. Anticipation is not expected. De novo variants are reported but uncommon. Consanguinity is relevant; founder enrichment exists for the recurrent AMHR2 deletion. (cima2024persistentmüllerianduct pages 12-13, cima2024persistentmüllerianduct pages 17-19)

No defensible population prevalence or annual incidence per 100,000 was identified. Statements such as “fewer than 300 cases reported” measure publication rarity, not prevalence. PMDS occurs globally; no ethnicity is intrinsically protected. The affected clinical sex ratio is effectively male because the defining internal/external discordance requires testes and male differentiation.

## 10. Diagnostics

### Practical diagnostic pathway

1. **Suspect PMDS** in bilateral/nonpalpable cryptorchidism, both testes on one side, transverse ectopia, recurrent inguinal hernia, or an unexpected uterus/tube at surgery.
2. **Map anatomy:** high-resolution inguinoscrotal and pelvic ultrasound; pelvic MRI when anatomy is uncertain; diagnostic laparoscopy remains highly informative.
3. **Establish sex-development context:** karyotype or chromosome analysis, typically 46,XY; document external virilization and palpable gonads.
4. **Laboratory testing:** AMH, inhibin B, testosterone, LH and FSH; tumor markers AFP, β-hCG and LDH when a mass is present. Very low AMH supports AMH deficiency; normal/high AMH supports AMHR2 resistance, but normal AMH does not exclude PMDS. A 2022 series reported AMH values of 0.06, 3.21 and 7.72 ng/mL across genetically distinct cases. (liu2022identificationofamh pages 2-5)
5. **Genetics:** sequence and deletion/duplication analysis of **AMH and AMHR2**. A DSD/cryptorchidism panel or WES is appropriate when first-line testing is negative; ensure CNV detection because AMHR2 microdeletions can be missed. WGS may resolve regulatory/structural variants, but its incremental PMDS yield is not established.
6. **Pathology:** verify Müllerian epithelium/smooth muscle and assess testicular maturation, atrophy, germ-cell neoplasia, or malignancy.

In a molecular study, 3 of 11 unrelated cryptorchidism patients carried biallelic AMH/AMHR2 variants, and MRI identified Müllerian remnants in all three—supporting genetics and MRI in selected cryptorchidism rather than universal screening. (liu2022identificationofamh pages 6-8, liu2022identificationofamh pages 2-5)

**Not routinely indicated:** mitochondrial sequencing, repeat-expansion testing, FISH, metabolomics, proteomics, liquid biopsy, or epigenomic testing. CMA/karyotype is useful when syndromic features or another DSD is suspected but will not detect most single-gene PMDS.

**Differential diagnosis:** androgen-insensitivity syndrome, 46,XY gonadal dysgenesis, testosterone-biosynthesis defects, mixed gonadal dysgenesis, ovotesticular DSD, congenital bilateral cryptorchidism without Müllerian persistence, and nonsyndromic transverse testicular ectopia. Normal male virilization plus uterus/tubes and AMH/AMHR2 biallelic variants strongly favors PMDS. Müllerian remnants can rarely coexist with another DSD, so anatomy alone is insufficient.

**Screening:** no newborn population screening. Offer cascade testing to siblings and carrier testing to relatives after a molecular diagnosis.

## 11. Outcome and prognosis

Life expectancy is generally expected to be near normal when cryptorchidism and tumors are appropriately managed, but no 5-year, 10-year, mortality, or life-expectancy cohort was found. Morbidity is reproductive and surgical rather than multisystemic.

Fertility is uncommon but possible when at least one testis is scrotal and its ductal drainage remains intact. Approximately **19%** reportedly fathered a child naturally in compiled cases. TESE/micro-TESE with ICSI may enable biological paternity; in one very small series, micro-TESE retrieved sperm in 1/2 azoospermic men. (liu2022identificationofamh pages 6-8, krzeminska2024persistentmullerianduct pages 1-3, mullen2019amhandamhr2 pages 1-2)

A selected expert series reported testicular malignant degeneration in **33% of adults**, whereas other reviews gave approximately **3.1–8.4%** or **5–18%**. The 33% figure should not be used for individual counseling as a population estimate; ascertainment and prolonged untreated cryptorchidism likely inflate it. Müllerian-remnant malignancies—adenocarcinoma, adenosarcoma and others—are documented but rarer. (cima2024persistentmüllerianduct pages 17-19, liu2022identificationofamh pages 6-8, mullen2019amhandamhr2 pages 1-2)

Prognosis is better with early testicular descent, at least one viable scrotal testis, intact vasa, avoidance of repeated operations, and absence of malignancy. No validated prognostic biomarker or calculator exists.

## 12. Treatment and current implementation

There is no drug, hormone, gene therapy, RNA therapy, cell therapy, or immunotherapy that can regress established Müllerian organs postnatally. Treatment is anatomical and preventive.

- **Orchiopexy** for viable testes, preferably early; **NCIT suggestion:** Orchiopexy.
- **Laparoscopic exploration/dissection** to define shared blood supply and vas anatomy; **NCIT:** Laparoscopic Surgical Procedure.
- **Selective subtotal/complete Müllerian-remnant excision or hysterectomy** when safely separable, symptomatic, cystic, or suspicious; **NCIT:** Hysterectomy/Surgical Resection.
- **Preservation with surveillance** when excision threatens the vas deferens or testicular vessels.
- **Orchidectomy** for nonviable/atrophic testis or malignancy concern; **NCIT:** Orchiectomy.
- **Fertility care:** semen analysis, cryopreservation when sperm are present, TESE/micro-TESE and ICSI; **NCIT:** Sperm Cryopreservation, Testicular Sperm Extraction, Intracytoplasmic Sperm Injection.
- **Supportive care:** genetic counseling, endocrine follow-up where gonadal function is compromised, tumor surveillance, and psychosocial DSD-informed care.

There is no consensus guideline on routine uterus removal. In a 12-patient Chinese series, 8 underwent orchiopexy with uterine preservation; 3 developed remnant cysts. Of 3 undergoing subtotal hysterectomy, one sustained vas injury and one postoperative hemorrhage. These observations support individualized, anatomy-preserving surgery rather than mandatory excision. (cima2024persistentmüllerianduct pages 16-17)

No PMDS-specific interventional ClinicalTrials.gov study was identified. Pharmacogenomic guidance is not applicable to the congenital lesion.

## 13. Prevention

- **Primary prevention:** no lifestyle or vaccine prevention. In known families, carrier testing, genetic counseling, prenatal diagnosis, and PGT-M are technically possible after identifying familial variants; use requires nondirective counseling.
- **Secondary prevention:** early recognition in cryptorchidism/hernia, preoperative imaging and AMH/genetic testing, and cascade testing can reduce delayed diagnosis and repeated surgery.
- **Tertiary prevention:** timely orchiopexy, preservation of vas/vessels, fertility preservation, surveillance of testes and retained remnants, and prompt evaluation of masses, pain, bleeding, or hematospermia.

For an autosomal-recessive couple in which both partners carry the same disease-causing gene defect, each pregnancy has a 25% probability of biallelic inheritance; phenotypic consequences depend on fetal sex and gonadal development. No public-health or environmental intervention is indicated.

## 14. Other species and natural disease

Naturally occurring PMDS is best characterized in the domestic dog (**Canis lupus familiaris**, NCBI Taxon 9615), particularly Miniature Schnauzers. A sex-limited recessive **AMHR2 c.241C>T, p.Arg81Ter** nonsense allele prevents signaling. Among 216 North American Miniature Schnauzers, allele frequency was **0.16** and carrier frequency **0.27**; approximately half of affected dogs had unilateral or bilateral cryptorchidism. Retained oviducts, uterus, cervix and cranial vagina, pyometra, infertility, and Sertoli-cell tumors have veterinary relevance. (mullen2019amhandamhr2 pages 4-5, smit2018prevalenceofthe pages 1-2)

A 2024 canine preprint found that GC-rich repetitive **AMH exon 5** is poorly covered by WGS/RNA-seq and that AMHR2 annotation differs markedly among canine assemblies. It recommends targeted resequencing of unresolved cases in Yorkshire Terriers and other breeds. This is a computational/preprint result, not yet definitive evidence of new causal alleles. (krzeminska2024persistentmullerianduct pages 3-7, krzeminska2024persistentmullerianduct pages 7-9, krzeminska2024persistentmullerianduct pages 12-17)

PMDS is not transmissible or zoonotic. Veterinary prevention consists of genotyping and avoiding carrier-to-carrier matings, not infection control.

## 15. Model organisms

### Mouse

Targeted **Amh-null** and **Amhr2-null** male mice retain a uterus, oviducts, and partial vagina despite normal testes and Wolffian structures, closely recapitulating the developmental core of human PMDS. Amhr2-null males can reproduce, but at less than a 50% rate and with smaller litters; focal seminiferous epithelial atrophy appears by 2 months and markedly reduces spermatogenesis by 9 months. These models support studies of ligand/receptor signaling, Müllerian regression, testicular descent, duct anatomy, and fertility. (mullen2019amhandamhr2 pages 4-5)

**Limitations:** mouse fertility is better preserved than in many clinical cases; surgical history and prolonged human cryptorchidism are not reproduced; species-specific reproductive anatomy differs; and constitutive knockouts do not model every human missense allele’s trafficking or residual function.

### Other experimental systems

Cell-based receptor assays can distinguish deficient AMH processing, receptor binding, trafficking, and kinase signaling. A 2024 biochemical study improved AMH precursor cleavage to over 90% and engineered variants with approximately 5- to 10-fold greater in-vitro potency; this clarifies receptor-complex assembly but is not a PMDS therapy. No validated PMDS patient-derived organoid, iPSC, CRISPR-screen, spatial-transcriptomic, or humanized model was identified.

## Recent developments and expert interpretation

1. **Expanded genotype/phenotype spectrum:** the 2024 AMHR2 p.Ile349Thr report links a very rare kinase-domain variant to PMDS with supernumerary testes and demonstrates why normal serum AMH should trigger receptor-focused analysis. Its abstract emphasizes that “a high degree of suspicion and awareness is needed … to avoid iterative surgery.” (cima2024persistentmüllerianduct pages 7-10)
2. **Beyond AMH/AMHR2:** genetically unresolved cases and reported PPP1R12A truncations suggest additional cytoskeletal/remodeling pathways, but evidence remains limited and should not displace AMH/AMHR2 first-line testing. (cima2024persistentmüllerianduct pages 12-13, cima2024persistentmüllerianduct pages 17-19)
3. **Precision surgery rather than uniform hysterectomy:** experts prioritize descended viable testes and intact vasa over complete Müllerian removal because remnants and male excretory ducts may share close attachments and blood supply. The small Chinese cohort quantifies both preservation-related cysts and excision-related injuries. (cima2024persistentmüllerianduct pages 16-17)
4. **Sequencing blind spots matter:** AMHR2 CNVs and GC-rich AMH regions can evade routine analysis; negative panel/WES results do not exclude pathway disease. Canine comparative genomics reinforces this methodological concern. (krzeminska2024persistentmullerianduct pages 3-7, krzeminska2024persistentmullerianduct pages 7-9, krzeminska2024persistentmullerianduct pages 12-17)

## Evidence gaps and knowledge-base cautions

No reliable population incidence, prevalence, carrier frequency, survival curve, standardized QOL result, evidence-based surveillance interval, prospective surgical comparison, or interventional trial exists. Phenotype and malignancy percentages derive from heterogeneous published/referral cases. Ontology IDs—especially granular HPO, UBERON, CL, NCIT and legacy OMIM mappings—should be programmatically validated against current releases before ingestion. Exact abstract quotations are necessarily sparse because several mechanistic sources were reviews or full-text excerpts rather than accessible PubMed abstracts.

References

1. (liu2022identificationofamh pages 5-6): Yang Liu, Sida Wang, Ruzhu Lan, and Jun Yang. Identification of amh and amhr2 variants led to the diagnosis of persistent müllerian duct syndrome in three cases. Jan 2022. URL: https://doi.org/10.3390/genes13010159, doi:10.3390/genes13010159. This article has 9 citations.

2. (cima2024persistentmüllerianduct pages 12-13): Luminita Nicoleta Cima, Iustina Grosu, Isabela Magdalena Draghici, Augustina Cornelia Enculescu, Adela Chirita-Emandi, Nicoleta Andreescu, Maria Puiu, Carmen Gabriela Barbu, and Simona Fica. Persistent müllerian duct syndrome with supernumerary testicles due to a novel homozygous variant in the amhr2 gene and literature review. Diagnostics, 14:2621, Nov 2024. URL: https://doi.org/10.3390/diagnostics14232621, doi:10.3390/diagnostics14232621. This article has 3 citations.

3. (mullen2019amhandamhr2 pages 1-2): Rachel D. Mullen, Alejandra E. Ontiveros, Malcolm M. Moses, and Richard R. Behringer. Amh and amhr2 mutations: a spectrum of reproductive phenotypes across vertebrate species. Developmental biology, 455:1-9, Nov 2019. URL: https://doi.org/10.1016/j.ydbio.2019.07.006, doi:10.1016/j.ydbio.2019.07.006. This article has 66 citations and is from a peer-reviewed journal.

4. (OpenTargets Search: Persistent Mullerian duct syndrome-AMH,AMHR2): Open Targets Query (Persistent Mullerian duct syndrome-AMH,AMHR2, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (cima2024persistentmüllerianduct pages 17-19): Luminita Nicoleta Cima, Iustina Grosu, Isabela Magdalena Draghici, Augustina Cornelia Enculescu, Adela Chirita-Emandi, Nicoleta Andreescu, Maria Puiu, Carmen Gabriela Barbu, and Simona Fica. Persistent müllerian duct syndrome with supernumerary testicles due to a novel homozygous variant in the amhr2 gene and literature review. Diagnostics, 14:2621, Nov 2024. URL: https://doi.org/10.3390/diagnostics14232621, doi:10.3390/diagnostics14232621. This article has 3 citations.

6. (cima2024persistentmüllerianduct pages 7-10): Luminita Nicoleta Cima, Iustina Grosu, Isabela Magdalena Draghici, Augustina Cornelia Enculescu, Adela Chirita-Emandi, Nicoleta Andreescu, Maria Puiu, Carmen Gabriela Barbu, and Simona Fica. Persistent müllerian duct syndrome with supernumerary testicles due to a novel homozygous variant in the amhr2 gene and literature review. Diagnostics, 14:2621, Nov 2024. URL: https://doi.org/10.3390/diagnostics14232621, doi:10.3390/diagnostics14232621. This article has 3 citations.

7. (liu2022identificationofamh pages 6-8): Yang Liu, Sida Wang, Ruzhu Lan, and Jun Yang. Identification of amh and amhr2 variants led to the diagnosis of persistent müllerian duct syndrome in three cases. Jan 2022. URL: https://doi.org/10.3390/genes13010159, doi:10.3390/genes13010159. This article has 9 citations.

8. (liu2022identificationofamh pages 2-5): Yang Liu, Sida Wang, Ruzhu Lan, and Jun Yang. Identification of amh and amhr2 variants led to the diagnosis of persistent müllerian duct syndrome in three cases. Jan 2022. URL: https://doi.org/10.3390/genes13010159, doi:10.3390/genes13010159. This article has 9 citations.

9. (krzeminska2024persistentmullerianduct pages 1-3): Paulina Krzeminska. Persistent mullerian duct syndrome in dogs – a new insight into organization of amh and amhr2 genes. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.11.28.625841, doi:10.1101/2024.11.28.625841. This article has 1 citations.

10. (cima2024persistentmüllerianduct pages 16-17): Luminita Nicoleta Cima, Iustina Grosu, Isabela Magdalena Draghici, Augustina Cornelia Enculescu, Adela Chirita-Emandi, Nicoleta Andreescu, Maria Puiu, Carmen Gabriela Barbu, and Simona Fica. Persistent müllerian duct syndrome with supernumerary testicles due to a novel homozygous variant in the amhr2 gene and literature review. Diagnostics, 14:2621, Nov 2024. URL: https://doi.org/10.3390/diagnostics14232621, doi:10.3390/diagnostics14232621. This article has 3 citations.

11. (mullen2019amhandamhr2 pages 4-5): Rachel D. Mullen, Alejandra E. Ontiveros, Malcolm M. Moses, and Richard R. Behringer. Amh and amhr2 mutations: a spectrum of reproductive phenotypes across vertebrate species. Developmental biology, 455:1-9, Nov 2019. URL: https://doi.org/10.1016/j.ydbio.2019.07.006, doi:10.1016/j.ydbio.2019.07.006. This article has 66 citations and is from a peer-reviewed journal.

12. (smit2018prevalenceofthe pages 1-2): M. M. Smit, K. J. Ekenstedt, K. Minor, C. Lim, P. Leegwater, and E. Furrow. Prevalence of the amhr2 mutation in miniature schnauzers and genetic investigation of a belgian malinois with persistent müllerian duct syndrome. Reproduction in Domestic Animals, 53:371–376, Apr 2018. URL: https://doi.org/10.1111/rda.13116, doi:10.1111/rda.13116. This article has 23 citations and is from a peer-reviewed journal.

13. (krzeminska2024persistentmullerianduct pages 3-7): Paulina Krzeminska. Persistent mullerian duct syndrome in dogs – a new insight into organization of amh and amhr2 genes. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.11.28.625841, doi:10.1101/2024.11.28.625841. This article has 1 citations.

14. (krzeminska2024persistentmullerianduct pages 7-9): Paulina Krzeminska. Persistent mullerian duct syndrome in dogs – a new insight into organization of amh and amhr2 genes. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.11.28.625841, doi:10.1101/2024.11.28.625841. This article has 1 citations.

15. (krzeminska2024persistentmullerianduct pages 12-17): Paulina Krzeminska. Persistent mullerian duct syndrome in dogs – a new insight into organization of amh and amhr2 genes. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.11.28.625841, doi:10.1101/2024.11.28.625841. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](Persistent_Mullerian_Duct_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 22 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009857` (5 mentions) - the report calls it "if available"; MONDO calls it **persistent Mullerian duct syndrome**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Orphanet`, `ORPHA`.