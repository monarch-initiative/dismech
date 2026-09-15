---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-01T20:12:42.585046'
end_time: '2026-09-01T20:20:31.017754'
duration_seconds: 468.43
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Autosomal Dominant Nonsyndromic Hearing Loss 25
  mondo_id: MONDO:0011568
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 35
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 5
  off_topic: 1
  off_topic_references:
  - PMID:22794260
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 8
  verified: 8
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0011568
    reported_labels:
    - if available
    ontology_label: autosomal dominant nonsyndromic hearing loss 25
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Dominant_Nonsyndromic_Hearing_Loss_25-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Nonsyndromic Hearing Loss 25
- **MONDO ID:** MONDO:0011568 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Nonsyndromic Hearing Loss 25** covering all of the
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
- **Disease Name:** Autosomal Dominant Nonsyndromic Hearing Loss 25
- **MONDO ID:** MONDO:0011568 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Nonsyndromic Hearing Loss 25** covering all of the
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


# Autosomal Dominant Nonsyndromic Hearing Loss 25 (DFNA25)

## Executive summary

Autosomal dominant nonsyndromic hearing loss 25 (DFNA25) is a very rare, progressive, predominantly high-frequency sensorineural hearing loss caused by heterozygous pathogenic variants in **SLC17A8**, which encodes vesicular glutamate transporter 3 (**VGLUT3/VGluT3**). VGLUT3 loads glutamate into synaptic vesicles of cochlear inner hair cells (IHCs), enabling transmission from IHC ribbon synapses to type I spiral-ganglion neurons. Human evidence remains limited to a small number of families, so disease-specific prevalence, quantitative penetrance, progression rates, and quality-of-life statistics are not established. The strongest therapeutic evidence is preclinical: AAV-mediated VGLUT3 replacement has restored hearing in neonatal and adult *Slc17a8*-null mice, but no DFNA25-specific human gene-therapy trial or approved disease-modifying drug was identified.

The following table provides an ontology-ready synopsis.

| domain | established finding | evidence type | suggested ontology terms/IDs | key evidence |
|---|---|---|---|---|
| disease identifier | Autosomal Dominant Nonsyndromic Hearing Loss 25 (DFNA25) is a Mendelian deafness entity linked to SLC17A8 | Human pedigree/genetic discovery | MONDO:0011568; OMIM 605583 | DFNA25 described as an "autosomal-dominant form of progressive, high-frequency nonsyndromic deafness" caused by SLC17A8 mutation (ruel2008impairmentofslc17a8 pages 1-2) |
| causal gene/protein | SLC17A8 encodes vesicular glutamate transporter 3 (VGLUT3) | Human, mouse, review | SLC17A8; VGLUT3; OMIM 607557 | VGLUT3 loads glutamate into inner hair cell synaptic vesicles before release to auditory nerve terminals (ruel2008impairmentofslc17a8 pages 1-2, ryu2016screeningofthe pages 1-2) |
| synonyms | DFNA25; deafness, autosomal dominant 25; SLC17A8-related autosomal dominant nonsyndromic hearing loss | Aggregated disease/gene nomenclature with primary literature support | OMIM 605583; SLC17A8-related hearing loss | Primary papers and reviews use DFNA25 / deafness, autosomal dominant 25 terminology (ruel2008impairmentofslc17a8 pages 1-2, ryu2016screeningofthe pages 1-2) |
| pathogenic variants | Reported disease-associated variants include c.632C>T (p.A211V), p.M206Nfs*4, and c.763+1G>T | Human genetic studies | HGVS nomenclature where known; ACMG classification not uniformly published | p.A211V segregated in two unrelated families and was absent in 267 controls; p.M206Nfs*4 absent in 100 controls; c.763+1G>T co-segregated in a 3-generation Korean family (ruel2008impairmentofslc17a8 pages 1-2, ryu2016screeningofthe pages 1-2, ryu2017identificationofa pages 1-6) |
| inheritance | Inheritance is autosomal dominant | Human pedigree | HP:0000006 Autosomal dominant inheritance | Multiple families showed autosomal-dominant segregation (ruel2008impairmentofslc17a8 pages 1-2, ryu2017identificationofa pages 1-6) |
| core phenotype | Progressive high-frequency sensorineural hearing loss, nonsyndromic | Human clinical | HP:0000407 Sensorineural hearing impairment; HP:0002066 Hearing impairment; high-frequency qualifier if used in HPO mapping | Human families had delayed/progressive high-frequency SNHL without syndromic features (ruel2008impairmentofslc17a8 pages 1-2, ryu2016screeningofthe pages 1-2) |
| onset/natural history | Typically delayed/late onset with age-related penetrance increase and progression over time | Human pedigree/clinical | HPO terms for progressive hearing impairment; adult/late onset descriptors as appropriate | DFNA phenotypes are described as delayed-onset and progressive; DFNA25 specifically showed age-related penetrance increase (ruel2008impairmentofslc17a8 pages 1-2, ruel2008impairmentofslc17a8 pages 13-14, ryu2016screeningofthe pages 1-2) |
| syndromic status | No consistent extra-auditory syndromic findings established | Human clinical | HP:0000007 Autosomal dominant inheritance; nonsyndromic descriptor | Korean family report noted hearing loss was non-syndromic with no accompanying symptoms (ryu2017identificationofa pages 1-6) |
| primary anatomy | Primary site is the cochlea, especially the organ of Corti inner hair cell synapse | Human-mechanistic inference supported by mouse and expression data | UBERON: cochlea; organ of Corti; inner hair cell | VGLUT3 is selectively expressed in cochlear inner hair cells and mediates afferent transmission (ryu2016screeningofthe pages 1-2, ruel2008impairmentofslc17a8 pages 1-2) |
| affected cells | Inner hair cells are primary; type I spiral ganglion neuron afferents are secondarily affected | Mouse physiology/morphology with human disease relevance | CL: inner hair cell; spiral ganglion neuron | Slc17a8-null mice lacked acoustic auditory-nerve responses and later showed decline in afferent synapses and spiral ganglion neurons (ruel2008impairmentofslc17a8 pages 1-2, ruel2008impairmentofslc17a8 pages 13-14) |
| subcellular localization | VGLUT3 localizes to synaptic vesicle-like glutamatergic organelles/ribbon-synapse trafficking compartments in IHCs | Proteomics, prior functional work | GO cellular component: synaptic vesicle; presynaptic active zone; synaptic ribbon | 2024 proteomics isolated "VGluT3-containing membrane vesicles" from IHCs and profiled ribbon-synapse trafficking machinery (cepeda2024proteomicanalysisreveals pages 1-3) |
| mechanism | Impaired vesicular glutamate loading/release at the IHC ribbon synapse leads to failure of auditory nerve activation; downstream synapse and neuron loss can follow | Human genetic inference plus mouse functional demonstration | GO: glutamate transport; chemical synaptic transmission; synaptic vesicle cycle | Null mice had absent acoustically evoked ABRs but preserved electrically evoked ABRs and otoacoustic emissions, supporting a synaptic glutamate-release defect rather than OHC failure (ruel2008impairmentofslc17a8 pages 1-2, ruel2008impairmentofslc17a8 pages 13-14) |
| variant-specific mechanism | The human p.A211V allele is modeled by mouse p.A224V and is associated with IHC stereocilia collapse, reduced summating potential, and oversized synaptic ribbons | Mouse knock-in model of human allele | GO: mechanotransduction; synaptic transmission; hair bundle organization | Knock-in mice showed progressive hearing loss with intact cochlear amplification, IHC bundle collapse, and altered ribbon exocytosis, suggesting mechanotransduction failure followed by altered synaptic transfer (joshi2021vglut3‐p.a211vvariantfuses pages 1-2) |
| diagnostic testing | Diagnosis relies on audiologic evaluation plus molecular testing (single gene, deafness panel, WES/WGS depending context) | Clinical genetics practice supported by gene-specific reports | SLC17A8 sequencing; hereditary hearing loss panel | SLC17A8 mutations were identified by candidate-gene sequencing and by whole-exome sequencing in affected families (ryu2016screeningofthe pages 1-2, ryu2017identificationofa pages 1-6) |
| electrophysiology | ABR is abnormal from failed acoustic neural transmission; OAE/DPOAE may remain preserved when OHC function is intact | Mouse functional evidence; clinically relevant inference | ABR; otoacoustic emissions | Slc17a8-null mice lacked auditory-nerve responses to sound yet retained robust otoacoustic emissions; p.A224V model had progressive ABR loss with intact DPOAEs (ruel2008impairmentofslc17a8 pages 1-2, joshi2021vglut3‐p.a211vvariantfuses pages 1-2) |
| treatment status | No DFNA25-specific approved molecular therapy identified; current real-world care is supportive/rehabilitative (hearing aids, cochlear implantation as indicated) | Review plus mechanistic/animal evidence | NCIT: Hearing Aid; Cochlear Implantation | Reviews note hearing aids and cochlear implants remain standard care for hereditary deafness; SLC17A8-specific therapy remains preclinical (duhon2024genetherapyadvancements pages 4-5, zhang2024aav‐mediatedgenetherapy pages 3-4) |
| cochlear implant implication | Because neural responses to electrical stimulation are preserved in Slc17a8-null mice, cochlear implantation is considered biologically plausible | Mouse translational inference | NCIT: Cochlear Implantation | Electrically evoked ABRs were preserved in null mice, suggesting bypass of the defective IHC synapse may help (ruel2008impairmentofslc17a8 pages 13-14) |
| gene therapy/preclinical | AAV1-VGLUT3 cochlear delivery rescued hearing in Vglut3 knockout mice; early postnatal RWM delivery achieved 100% normal ABR threshold recovery in one series | Mouse preclinical interventional | AAV gene replacement; VGLUT3 gene augmentation | Akil 2012 reported normalized ABR thresholds within 2 weeks; P1-P3 RWM delivery rescued 19/19 mice and some maintained hearing long term (akil2012restorationofhearing pages 1-2, akil2012restorationofhearing pages 6-8) |
| mature-cochlea translational development | 2023 mature-mouse CSF/cisterna magna delivery of AAV-PHP.B-CBA-VGLUT3-WPRE reportedly restored hearing in SLC17A8-/- mice except at 40 kHz | Review summarizing preclinical primary study | AAV-PHP.B; cisterna magna delivery | 2024 review summarizes mature-mouse rescue at dose 2.27 × 10^11 vg with limited off-target expression reported (duhon2024genetherapyadvancements pages 11-12) |
| human trials status | No human interventional trial specific to SLC17A8/DFNA25 was identified in the tool-based search | Trial search / evidence gap | ClinicalTrials.gov status: none identified for this gene-disease pair | Recent reviews discuss human OTOF trials, not SLC17A8-specific trials; trial search returned no relevant SLC17A8 intervention (zhang2024aav‐mediatedgenetherapy pages 3-4, duhon2024genetherapyadvancements pages 4-5) |
| model organisms | Key models are Slc17a8 knockout mice and VGLUT3A224V/A224V knock-in mice modeling human p.A211V | Mouse in vivo models | MGI/IMSR resources if needed; Slc17a8 mouse models | Knockout demonstrates synaptic glutamate-release failure; knock-in models progressive/mechanosensory and synaptic pathology (ruel2008impairmentofslc17a8 pages 1-2, joshi2021vglut3‐p.a211vvariantfuses pages 1-2) |
| comparative conservation | The affected alanine residue is conserved across species and among human VGLUT paralogs | Human/mouse comparative sequence evidence | conserved residue annotation | Conservation of A211 supported pathogenic relevance of p.A211V (ruel2008impairmentofslc17a8 pages 1-2) |
| epidemiology | Disease-specific prevalence, incidence, sex ratio, and carrier frequency are not established in the retrieved DFNA25-specific literature | Explicit data gap | not available | Available papers are family-based discovery/screening studies rather than population epidemiology (ruel2008impairmentofslc17a8 pages 1-2, ryu2016screeningofthe pages 1-2) |
| penetrance/expressivity | Penetrance appears age-dependent and expressivity likely variable, but robust quantitative estimates are lacking | Human pedigree with data gap | age-dependent penetrance descriptor | Human paper notes age-related penetrance increase; no precise percent penetrance estimate retrieved (ruel2008impairmentofslc17a8 pages 13-14) |
| environmental modifiers | No DFNA25-specific environmental risk or protective modifiers were established in retrieved primary disease papers | Explicit data gap | not available | Reviews discuss generic contributors to hearing loss (noise, aging), but not validated DFNA25-specific gene-environment interactions (ruel2008impairmentofslc17a8 pages 1-2, bottom2024defectsinhair pages 1-2) |
| QoL/prognosis gap | No DFNA25-specific quality-of-life or life-expectancy studies were identified; morbidity is expected to derive mainly from chronic progressive hearing impairment | Explicit data gap with general clinical inference | hearing-disability QoL instruments if studied in future | Family reports focus on hearing phenotype/genetics, not QoL or survival outcomes (ruel2008impairmentofslc17a8 pages 1-2, ryu2016screeningofthe pages 1-2) |


*Table: This table condenses the most actionable, ontology-ready facts for DFNA25/SLC17A8-related hearing loss, including core identifiers, phenotype, mechanism, models, and treatment status. It also flags major evidence gaps where disease-specific epidemiology, modifiers, and outcomes are not yet established.*

## 1. Disease information

### Definition and identifiers

DFNA25 is an inherited, nonsyndromic cochlear disorder characterized by progressive high-frequency sensorineural hearing impairment. The landmark report described it as an “autosomal-dominant form of progressive, high-frequency nonsyndromic deafness.” (ruel2008impairmentofslc17a8 pages 1-2)

* **Preferred name:** Autosomal dominant nonsyndromic hearing loss 25
* **Synonyms:** DFNA25; deafness, autosomal dominant 25; SLC17A8-related autosomal dominant nonsyndromic hearing loss
* **MONDO:** **MONDO:0011568**
* **OMIM phenotype:** **605583**, DFNA25
* **Causal gene/protein:** **SLC17A8**, VGLUT3; OMIM **607557**
* **Locus:** chromosome **12q21–q24.5** in the original linkage interval
* **ICD-10-CM:** no DFNA25-specific code; generally coded under **H90.3** (bilateral sensorineural hearing loss) or another audiometrically appropriate H90 category
* **ICD-11/MeSH:** no uniquely specific DFNA25 entry was established in the retrieved literature; broader hereditary/sensorineural hearing-loss concepts apply.

The foundational human evidence came from pedigrees, clinical audiometry, linkage analysis, and germline DNA sequencing—not individual EHR-derived records. The broader identifiers and nomenclature are aggregated disease-level annotations.

The discovery article was published **8 August 2008** in the *American Journal of Human Genetics*, DOI [10.1016/j.ajhg.2008.07.008](https://doi.org/10.1016/j.ajhg.2008.07.008), PMID **18674745**. Its abstract states: “We have identified SLC17A8…as the gene responsible for DFNA25.” (ruel2008impairmentofslc17a8 pages 1-2)

## 2. Etiology, risk, and protective factors

### Causal factor

The primary cause is a **heterozygous germline SLC17A8 variant** affecting VGLUT3. The best-established allele, **NM_139319.2:c.632C>T, p.(Ala211Val)**, segregated with hearing loss in two nominally unrelated families and was absent from 267 controls; linkage-disequilibrium analysis suggested distant common ancestry. The alanine is conserved across species and all three human VGLUT paralogs. (ruel2008impairmentofslc17a8 pages 1-2)

Additional reported alleles include:

* **p.(Met206AsnfsTer4)**: heterozygous frameshift predicted to terminate at residue 209 and remove transmembrane domains 5–12. It was found while screening **87 unrelated Korean patients** with ADNSHL and was absent from **100 normal-hearing controls**. The original authors described it as “likely” pathogenic; current ClinVar assertions should be checked at ingestion time rather than inferred from that wording. Publication: January 2016; DOI [10.1186/s12881-016-0269-3](https://doi.org/10.1186/s12881-016-0269-3). (ryu2016screeningofthe pages 1-2)
* **c.763+1G>T**: canonical splice-donor variant identified by WES in a three-generation Korean family. It was present in three affected relatives, absent from the tested unaffected relative and 100 normal-hearing controls, and was reported as probably pathogenic. Publication: September 2017; DOI [10.1016/j.gene.2017.06.040](https://doi.org/10.1016/j.gene.2017.06.040). (ryu2017identificationofa pages 23-25, ryu2017identificationofa pages 1-6)

These are germline, not somatic, variants. Population allele frequencies were not supplied in the retrieved primary evidence; contemporary gnomAD frequencies and transcript-normalized HGVS should be obtained directly before clinical interpretation.

### Genetic mechanism and modifiers

Simple haploinsufficiency is unlikely to explain every DFNA25 allele: heterozygous *Slc17a8* knockout mice have normal hearing and anatomy, whereas humans heterozygous for p.A211V develop age-dependent disease. This supports an allele-specific dominant-negative or toxic gain-of-function mechanism for p.A211V, although the precise molecular interaction remains unresolved. Truncating and splice variants may act differently, and pathogenicity should therefore be evaluated allele by allele. (ruel2008impairmentofslc17a8 pages 13-14)

No replicated modifier gene, protective SLC17A8 allele, epigenetic modifier, founder frequency, or germline-mosaicism estimate has been established. Family history is the major ascertainable risk factor; each child of a heterozygous affected person has a **50% transmission probability**, although age-dependent penetrance complicates phenotype-based testing.

### Environment and gene–environment interaction

Noise, aging, and ototoxic agents are established general causes or accelerants of cochlear synaptopathy, but no study has quantified a DFNA25-specific interaction. Recent work notes that genetic defects, loud noise, ototoxic drugs, and aging can all compromise IHC synaptic sound encoding. Consequently, noise and ototoxin avoidance is biologically reasonable but not proven to alter DFNA25 natural history. (bottom2024defectsinhair pages 1-2, cepeda2024proteomicanalysisreveals pages 1-3)

No specific diet, exercise program, supplement, vaccine, or medication has been demonstrated to prevent genetically initiated DFNA25.

## 3. Phenotypes

### Core phenotype

The principal phenotype is **bilateral, nonsyndromic, sensorineural hearing impairment**, initially most prominent at high frequencies and progressive with age. Onset is generally delayed rather than congenital in the original p.A211V families, and penetrance rises with age. Severity and onset vary among carriers; robust percentages and annual threshold-shift estimates are unavailable. (ruel2008impairmentofslc17a8 pages 1-2, ruel2008impairmentofslc17a8 pages 13-14)

Suggested annotations are:

* **Sensorineural hearing impairment — HP:0000407**
* **High-frequency hearing impairment — use the current HPO high-frequency term at database ingestion**
* **Progressive hearing impairment — HP:0001730**
* **Bilateral hearing impairment — HP:0012715**
* **Autosomal dominant inheritance — HP:0000006**
* **Adult/late onset — apply only when documented for the individual, because onset is variable**

Preserved otoacoustic emissions and synaptic/auditory-neuropathy physiology are strongly demonstrated in mice, but should not automatically be entered as universal human phenotypes. In the null model, robust OAEs coexisted with absent sound-evoked auditory-nerve responses, localizing dysfunction downstream of outer-hair-cell amplification. (ruel2008impairmentofslc17a8 pages 1-2)

No consistent vestibular, visual, neurologic, renal, endocrine, craniofacial, or behavioral abnormality has been reported; a Korean pedigree specifically had no accompanying symptoms. (ryu2017identificationofa pages 1-6)

### Functional and quality-of-life consequences

Disease-specific EQ-5D, SF-36, PROMIS, speech-recognition, educational, or employment data are unavailable. By clinical inference, progressive high-frequency loss can impair speech understanding—particularly consonants and speech in noise—communication, education, work, and social participation. These generic consequences should not be represented as measured DFNA25 outcomes.

## 4. Genetic and molecular information

**SLC17A8** encodes a 589-amino-acid, predicted 12-transmembrane-domain major-facilitator-superfamily transporter. In cochlear IHCs, VGLUT3 packages glutamate into vesicles for release at ribbon synapses. (ryu2016screeningofthe pages 1-2)

Relevant molecular annotations include:

* **GO biological process:** glutamate transmembrane transport; synaptic-vesicle loading; chemical synaptic transmission; synaptic-vesicle cycle; sensory perception of sound.
* **GO molecular function:** vesicular glutamate transmembrane transporter activity.
* **GO cellular component:** synaptic vesicle membrane; glutamatergic synapse; presynaptic active zone; ribbon synapse.
* **CHEBI:** L-glutamate (**CHEBI:29985**).

No large recurrent deletion, inversion, translocation, aneuploidy, DNA-methylation signature, or disease-specific chromatin abnormality is established. Likewise, no validated prognostic transcriptomic, circulating, metabolomic, lipidomic, or epigenomic biomarker exists.

## 5. Environmental information

DFNA25 is not infectious, toxic, occupational, or lifestyle-caused. Environmental exposures may add independent cochlear injury to the inherited defect. Avoidable generic hazards include excessive sound, aminoglycosides when alternatives exist, cisplatin, and other recognized ototoxins. There is no evidence that smoking, alcohol, diet, exercise, radiation, pollution, or a pathogen specifically changes SLC17A8 penetrance.

A rat salicylate model found increased IHC VGLUT3 expression and tinnitus without a significant hearing-threshold difference, but this is acquired-toxicity evidence and does **not** establish salicylate as a DFNA25 modifier.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous pathogenic **SLC17A8** lesion **leads to** altered amount, structure, trafficking, or function of VGLUT3 in cochlear IHCs.
2. Altered VGLUT3 **leads to** defective glutamate accumulation in IHC synaptic vesicles; this is directly demonstrated for complete loss of VGLUT3 and inferred, with allele-specific complexities, for human dominant variants. (ruel2008impairmentofslc17a8 pages 12-13, ruel2008impairmentofslc17a8 pages 1-2)
3. In the **loss-of-function branch**, empty or inadequately loaded vesicles can still undergo Ca²⁺-triggered exocytosis, but insufficient glutamate release **results in** failure to activate type I spiral-ganglion afferents. Vesicle turnover and exocytotic kinetics were initially preserved in null IHCs. (ruel2008impairmentofslc17a8 pages 12-13)
4. In the **p.A211V branch**, the modeled mouse allele p.A224V **leads to** IHC stereociliary-bundle collapse and reduced receptor potential, followed by oversized ribbons and altered sustained exocytosis; these findings suggest primary mechano-transduction failure plus later synaptic dysfunction rather than pure transporter insufficiency. (joshi2021vglut3‐p.a211vvariantfuses pages 1-2)
5. Failed or distorted IHC-to-afferent signaling **results in** reduced auditory-nerve activity and elevated/absent acoustically evoked ABRs, while outer-hair-cell cochlear amplification may remain intact. (ruel2008impairmentofslc17a8 pages 1-2, joshi2021vglut3‐p.a211vvariantfuses pages 1-2)
6. Chronic loss of afferent activity **leads to** secondary decline of IHC afferent synapses, spiral-ganglion neurons, and lateral efferent endings; altered trophic support and activity-dependent circuit maturation are plausible mediators. (ruel2008impairmentofslc17a8 pages 12-13, ruel2008impairmentofslc17a8 pages 13-14)
7. Tonotopically unequal vulnerability, not yet fully explained, **results in** the characteristic progressive high-frequency sensorineural hearing phenotype.

The principal upstream lesion is vesicular transporter dysfunction; mechano-transduction and ribbon abnormalities may be allele-specific parallel or downstream processes. Secondary neural/circuit degeneration is downstream. No primary immune, fibrotic, ischemic, endocrine, or metabolic mechanism has been demonstrated.

Suggested cell terms are **inner hair cell**, **type I spiral-ganglion neuron**, and secondarily lateral olivocochlear efferent neuron. Suggested anatomical terms are cochlea, organ of Corti, spiral ganglion, and IHC ribbon synapse. Exact CL/UBERON identifiers should be ontology-validated during curation.

### Recent molecular profiling

A 2024 study used subcellular fractionation, anti-VGluT3 immunoisolation, label-free LC–MS, and imaging to generate the first broad proteomic inventory of native IHC trafficking organelles. It identified an age-dependent, mixed synaptic-vesicle/endosomal signature and enrichment after hearing onset of VAMP7, syntaxins 7/8/12–13, SCAMP1, V-ATPase, SV2, and PKCα. This profiles normal VGLUT3-positive organelles rather than DFNA25 patient tissue, but supplies an authoritative molecular framework for studying variant effects. Publication: February 2024; DOI [10.1016/j.mcpro.2023.100704](https://doi.org/10.1016/j.mcpro.2023.100704). (cepeda2024proteomicanalysisreveals pages 1-3)

No DFNA25 patient-derived single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, organoid, iPSC, or CRISPR-screen dataset was identified.

## 7. Anatomical structures affected

* **Primary organ/system:** inner ear/cochlea; auditory sensory system.
* **Primary tissue:** sensory epithelium of the organ of Corti.
* **Primary cell:** IHC, especially its apical stereociliary bundle for p.A211V-like disease and basolateral ribbon-synapse vesicular compartment for VGLUT3 function.
* **Secondary cells:** IHC-afferent terminals and type I spiral-ganglion neurons; lateral efferent endings decline in null mice.
* **Relatively preserved structure:** OHCs and cochlear amplification in the principal mouse models, reflected by robust OAE/DPOAE measurements. (ruel2008impairmentofslc17a8 pages 1-2, joshi2021vglut3‐p.a211vvariantfuses pages 1-2)
* **Laterality:** human disease is understood as bilateral; asymmetry is not a defining feature.

VGLUT3 is also expressed in selected central neurons, but DFNA25 is clinically nonsyndromic and no reproducible central-neurologic phenotype is established.

## 8. Temporal development

The human course is chronic and lifelong: high-frequency thresholds typically deteriorate progressively, with age-dependent clinical penetrance. There are no validated early/intermediate/end-stage definitions, median onset age, dB/year trajectory, spontaneous remissions, or episodic pattern. (ruel2008impairmentofslc17a8 pages 13-14)

The mouse evidence suggests two potentially important intervention windows. First, restoring neurotransmission before secondary spiral-ganglion loss should be advantageous. Second, treatment remains possible after auditory maturation: adult-mouse rescue has been reported, although delivery and neural preservation become more difficult. Neonatal mice are unusually permissive to AAV and do not directly model the fully developed human neonatal cochlea. (duhon2024genetherapyadvancements pages 11-12, duhon2024genetherapyadvancements pages 4-5)

## 9. Inheritance and population

Inheritance is **autosomal dominant**. Both sexes are expected to be affected equally and male-to-male transmission is possible. Penetrance appears age-dependent; no defensible percentage is available. Expressivity is variable, while anticipation has not been shown. Consanguinity is not etiologically important for this dominant condition.

A distant founder relationship was suggested for the two p.A211V families of Czech/German ancestry, but there is no population-wide founder-frequency estimate. Korean frameshift and splice variants demonstrate that DFNA25 is not confined to European ancestry. (ruel2008impairmentofslc17a8 pages 1-2, ryu2017identificationofa pages 1-6)

Disease-specific prevalence, incidence, carrier frequency, geographic distribution, sex ratio, and age distribution are unknown. The Korean screening study found one proposed frameshift allele among **87 unrelated ADNSHL probands**, but this selected sample cannot be converted into population prevalence. For context only, the paper reported that roughly 70% of hereditary SNHL is nonsyndromic and that 10–20% of nonsyndromic cases follow dominant inheritance; these are not DFNA25-specific statistics. (ryu2016screeningofthe pages 1-2)

## 10. Diagnostics

### Clinical evaluation

Recommended assessment includes otologic examination, family history over at least three generations, pure-tone air/bone audiometry, speech audiometry including speech-in-noise where available, tympanometry, and serial threshold monitoring. OAEs and ABR can help localize cochlear amplification versus IHC-synaptic/neural transmission, but no DFNA25-specific diagnostic cut-off exists.

Imaging is usually unnecessary in a classic bilateral hereditary presentation but may be appropriate for asymmetry, vestibular symptoms, cochlear-implant planning, or another suspected structural cause. Routine blood chemistry, biopsy, EEG, EMG, or metabolic testing does not diagnose DFNA25.

### Genetic testing strategy

1. Use a comprehensive hereditary-hearing-loss panel containing **SLC17A8**, with copy-number calling where technically validated.
2. Use exome or genome sequencing when a panel is negative, the phenotype is atypical, or broader reanalysis is desirable. WES identified c.763+1G>T in the Korean pedigree. (ryu2017identificationofa pages 1-6)
3. Confirm reportable variants by an orthogonal method as appropriate, evaluate segregation, and apply current ACMG/AMP and hearing-loss specifications.
4. For a splice variant, RNA analysis can provide useful functional confirmation when an informative tissue or minigene assay is feasible.
5. Once a familial pathogenic variant is established, use targeted testing for relatives, prenatal diagnosis, or preimplantation genetic testing.

CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not first-line tests for isolated, sequence-variant-mediated DFNA25 unless another diagnosis is suspected.

### Differential diagnosis

The differential includes other progressive dominant nonsyndromic hearing losses—such as **KCNQ4/DFNA2A, TECTA/DFNA8/12, WFS1/DFNA6/14/38, ACTG1/DFNA20/26, POU4F3/DFNA15, TMC1/DFNA36**, and **COCH/DFNA9**—plus age/noise-related loss, ototoxicity, congenital infection, and structural disease. Vestibular dysfunction strongly suggests alternatives such as COCH-related disease. Molecular diagnosis is essential because audiograms overlap.

Newborn hearing screening can miss delayed-onset DFNA25. Children carrying a familial variant require scheduled audiologic surveillance even after a normal newborn screen.

## 11. Outcome and prognosis

DFNA25 is not known to reduce survival or life expectancy, and no disease-specific mortality is reported. Morbidity is auditory: progressive communication disability may eventually require amplification or implantation. Spontaneous biological recovery is not expected, although functional rehabilitation is often substantial.

Baseline severity, age of onset, serial threshold slope, speech recognition, and preservation of spiral-ganglion function are clinically relevant prognostic features. No molecular biomarker predicts progression beyond the familial variant and family-specific natural history. No five- or ten-year survival statistic is applicable.

## 12. Treatment and current implementation

### Current care

There is no approved DFNA25-specific drug, RNA therapy, gene therapy, or pharmacogenomic guideline. Current management is individualized:

* **Hearing aids** for aidable mild-to-severe loss—suggested NCIT annotation: *Hearing Aid*.
* **Assistive listening/remote-microphone systems**, captioning, communication accommodations, and auditory rehabilitation.
* **Speech-language and educational support**, especially for childhood onset.
* **Cochlear implantation** for severe-to-profound loss or poor aided speech recognition—suggested NCIT annotation: *Cochlear Implantation*.

Cochlear implantation is mechanistically plausible because electrically evoked ABRs remained present in *Slc17a8*-null mice even when acoustic responses were absent, indicating that electrical stimulation can bypass the defective IHC synapse. This is translational inference, not a DFNA25-specific clinical outcome series. (ruel2008impairmentofslc17a8 pages 13-14)

### Experimental gene replacement

In 2012, cochlear **AAV1-VGLUT3** delivery to knockout mice produced IHC-selective protein expression and normalized ABR thresholds within two weeks. At postnatal days 1–3, round-window delivery rescued normal ABR thresholds in **19/19 mice**; five followed for nine months retained normal thresholds. A 1-µL dose at 2.3×10¹³ vg/mL labeled 100% of IHCs, whereas 0.6 µL labeled about 40%; even partial IHC transduction could restore near-normal thresholds. Some rescued animals retained normal thresholds for up to 1.5 years, although neural counts and response amplitudes did not fully normalize. Publication: **26 July 2012**, *Neuron*; DOI [10.1016/j.neuron.2012.05.019](https://doi.org/10.1016/j.neuron.2012.05.019), PMID **22794260**. (akil2012restorationofhearing pages 1-2, akil2012restorationofhearing pages 6-8, akil2012restorationofhearing pages 9-10)

A 2023 study summarized in a 2024 review delivered **AAV-PHP.B-CBA-VGLUT3-WPRE** into the cisterna magna of mice aged P28–P105. A dose of **2.27×10¹¹ vg** reportedly restored hearing across tested frequencies except 40 kHz. Minimal brain expression and no liver expression were reported, but spinal-cord, dorsal-root-ganglion, and liver-vector-genome analyses were incomplete. The review appropriately highlights dorsal-root-ganglion toxicity seen in **83% of 213 nonhuman primates** across other intracisternal AAV studies, making safety and species-specific tropism major translational barriers. (duhon2024genetherapyadvancements pages 11-12)

For dominant p.A211V-like disease, simple addition of wild-type SLC17A8 may not suppress a dominant-negative/toxic mutant allele. Mutation-agnostic silencing plus replacement, allele-specific silencing, or editing may ultimately be required; none has yet been validated clinically for DFNA25.

Recent expert reviews conclude that VGLUT3 replacement is among the most successful preclinical hearing-loss programs, sometimes restoring wild-type ABR thresholds, but emphasize poorer adult transduction and incomplete ABR wave-I/neural rescue. One review contrasts approximately 100% IHC/~75% spiral-ganglion-neuron transduction in neonatal mice with 100% IHC but **<20% SGN** transduction in adults. (duhon2024genetherapyadvancements pages 4-5)

A search of ClinicalTrials.gov found **no SLC17A8/DFNA25-specific human interventional trial**. Human hereditary-deafness gene-therapy trials described in the 2024 literature concern chiefly **OTOF/DFNB9**, not DFNA25. (zhang2024aav‐mediatedgenetherapy pages 3-4)

## 13. Prevention

Primary prevention of a de novo or inherited pathogenic allele is not possible through lifestyle change. Reproductive options after molecular diagnosis include genetic counseling, natural conception with or without prenatal diagnosis, donor gametes, adoption, and IVF with preimplantation genetic testing.

Secondary prevention comprises cascade testing and longitudinal audiology, particularly because phenotype-based screening may miss young, age-dependent carriers. Early amplification and educational intervention can reduce developmental and communication consequences.

Tertiary prevention includes hearing conservation, avoidance of unnecessary ototoxic exposure, optimized amplification, vaccination and infection prevention according to routine standards—especially before cochlear implantation—and maintenance of social/communication access. These measures prevent additive injury or complications; they do not correct SLC17A8.

## 14. Other species and natural disease

Orthologous **Slc17a8** is conserved across vertebrates, and the p.A211 residue is conserved across species. Suggested taxa include *Mus musculus* (NCBI Taxonomy **10090**), *Rattus norvegicus* (**10116**), *Danio rerio* (**7955**), and *Homo sapiens* (**9606**). (ruel2008impairmentofslc17a8 pages 1-2)

No well-validated, naturally occurring companion-animal or livestock counterpart attributable to an orthologous dominant SLC17A8 allele was identified; therefore no defensible VBO breed annotation or veterinary prevalence can be assigned. DFNA25 is noninfectious and has no zoonotic or cross-species transmission potential.

## 15. Model organisms

### *Slc17a8* knockout mouse

Targeted exon-2 deletion produces congenital profound deafness with absent acoustic auditory-nerve responses, preserved electrically evoked ABRs, and robust OAEs. Ca²⁺-triggered vesicle turnover remains intact at approximately two weeks, demonstrating that vesicle fusion can occur without glutamate loading. Afferent synapses, spiral-ganglion neurons, and lateral efferent terminals decline later. This model is excellent for transporter loss and gene-replacement studies but does not reproduce heterozygous, delayed-onset human p.A211V disease. (ruel2008impairmentofslc17a8 pages 12-13, ruel2008impairmentofslc17a8 pages 1-2)

### p.A224V knock-in mouse

Mouse p.A224V models human p.A211V. Homozygous knock-in mice exhibit progressive ABR loss with preserved cochlear amplification, reduced summating potentials, IHC—but not OHC—stereociliary-bundle collapse, oversized ribbons, and increased sustained-pool exocytosis. The authors concluded that DFNA25 “stems from a failure in the mechano-transduction followed by a change in synaptic transfer.” Publication: December 2021; DOI [10.1113/JP282181](https://doi.org/10.1113/JP282181). The homozygous design may exaggerate a heterozygous human phenotype. (joshi2021vglut3‐p.a211vvariantfuses pages 1-2)

### Other model uses and limitations

VGLUT3-positive IHC organelle immunoisolation and cochlear explants support biochemical and cellular studies; zebrafish offer conserved hair-cell biology and regeneration but differ from mammalian cochlear frequency tuning and OHC specialization. No validated DFNA25 patient iPSC-derived IHC or cochlear-organoid model was identified.

## Evidence appraisal and principal knowledge gaps

The causal gene–disease relationship is strong: linkage and segregation in human families align with highly specific knockout and knock-in physiology. Nevertheless, the clinical evidence base is small and family-biased. Major missing items are disease-specific prevalence, quantitative penetrance, variant-level natural history, prospective speech and quality-of-life outcomes, human cochlear-implant outcomes, validated environmental modifiers, patient-derived omics, and clinical therapeutic trials. The most important translational distinction is that successful replacement in a recessive/null mouse does not prove efficacy against a dominant human missense allele.

### Key source list

1. Ruel J, et al. *Am J Hum Genet.* Published 8 August 2008. DOI: [10.1016/j.ajhg.2008.07.008](https://doi.org/10.1016/j.ajhg.2008.07.008); PMID 18674745. (ruel2008impairmentofslc17a8 pages 1-2)
2. Akil O, et al. *Neuron.* Published 26 July 2012. DOI: [10.1016/j.neuron.2012.05.019](https://doi.org/10.1016/j.neuron.2012.05.019); PMID 22794260. (akil2012restorationofhearing pages 1-2)
3. Ryu N, et al. *BMC Medical Genetics.* January 2016. DOI: [10.1186/s12881-016-0269-3](https://doi.org/10.1186/s12881-016-0269-3). (ryu2016screeningofthe pages 1-2)
4. Ryu N, et al. *Gene.* September 2017. DOI: [10.1016/j.gene.2017.06.040](https://doi.org/10.1016/j.gene.2017.06.040). (ryu2017identificationofa pages 1-6)
5. Joshi Y, et al. *Journal of Physiology.* December 2021. DOI: [10.1113/JP282181](https://doi.org/10.1113/JP282181). (joshi2021vglut3‐p.a211vvariantfuses pages 1-2)
6. Cepeda AP, et al. *Molecular & Cellular Proteomics.* February 2024. DOI: [10.1016/j.mcpro.2023.100704](https://doi.org/10.1016/j.mcpro.2023.100704). (cepeda2024proteomicanalysisreveals pages 1-3)
7. Duhon BH, et al. *Frontiers in Audiology and Otology.* July 2024. DOI: [10.3389/fauot.2024.1423853](https://doi.org/10.3389/fauot.2024.1423853). (duhon2024genetherapyadvancements pages 11-12, duhon2024genetherapyadvancements pages 4-5)
8. Zhang L, et al. *Advanced Science.* November 2024. DOI: [10.1002/advs.202402166](https://doi.org/10.1002/advs.202402166). (zhang2024aav‐mediatedgenetherapy pages 3-4)

References

1. (ruel2008impairmentofslc17a8 pages 1-2): Jérôme Ruel, Sarah Emery, Régis Nouvian, Tiphaine Bersot, Bénédicte Amilhon, Jana M. Van Rybroek, Guy Rebillard, Marc Lenoir, Michel Eybalin, Benjamin Delprat, Theru A. Sivakumaran, Bruno Giros, Salah El Mestikawy, Tobias Moser, Richard J.H. Smith, Marci M. Lesperance, and Jean-Luc Puel. Impairment of slc17a8 encoding vesicular glutamate transporter-3, vglut3, underlies nonsyndromic deafness dfna25 and inner hair cell dysfunction in null mice. American journal of human genetics, 83 2:278-92, Aug 2008. URL: https://doi.org/10.1016/j.ajhg.2008.07.008, doi:10.1016/j.ajhg.2008.07.008. This article has 345 citations and is from a highest quality peer-reviewed journal.

2. (ryu2016screeningofthe pages 1-2): Nari Ryu, Borum Sagong, Hong-Joon Park, Min-A Kim, Kyu-Yup Lee, Jae Young Choi, and Un-Kyung Kim. Screening of the slc17a8 gene as a causative factor for autosomal dominant non-syndromic hearing loss in koreans. BMC Medical Genetics, Jan 2016. URL: https://doi.org/10.1186/s12881-016-0269-3, doi:10.1186/s12881-016-0269-3. This article has 26 citations and is from a peer-reviewed journal.

3. (ryu2017identificationofa pages 1-6): Nari Ryu, Seokwon Lee, Hong-Joon Park, Byeonghyeon Lee, Tae-Jun Kwon, Jinwoong Bok, Chan Ik Park, Kyu-Yup Lee, Jeong-In Baek, and Un-Kyung Kim. Identification of a novel splicing mutation within slc17a8 in a korean family with hearing loss by whole-exome sequencing. Gene, 627:233-238, Sep 2017. URL: https://doi.org/10.1016/j.gene.2017.06.040, doi:10.1016/j.gene.2017.06.040. This article has 16 citations and is from a peer-reviewed journal.

4. (ruel2008impairmentofslc17a8 pages 13-14): Jérôme Ruel, Sarah Emery, Régis Nouvian, Tiphaine Bersot, Bénédicte Amilhon, Jana M. Van Rybroek, Guy Rebillard, Marc Lenoir, Michel Eybalin, Benjamin Delprat, Theru A. Sivakumaran, Bruno Giros, Salah El Mestikawy, Tobias Moser, Richard J.H. Smith, Marci M. Lesperance, and Jean-Luc Puel. Impairment of slc17a8 encoding vesicular glutamate transporter-3, vglut3, underlies nonsyndromic deafness dfna25 and inner hair cell dysfunction in null mice. American journal of human genetics, 83 2:278-92, Aug 2008. URL: https://doi.org/10.1016/j.ajhg.2008.07.008, doi:10.1016/j.ajhg.2008.07.008. This article has 345 citations and is from a highest quality peer-reviewed journal.

5. (cepeda2024proteomicanalysisreveals pages 1-3): Andreia P. Cepeda, Momchil Ninov, Jakob Neef, Iwan Parfentev, Kathrin Kusch, Ellen Reisinger, Reinhard Jahn, Tobias Moser, and Henning Urlaub. Proteomic analysis reveals the composition of glutamatergic organelles of auditory inner hair cells. Feb 2024. URL: https://doi.org/10.1016/j.mcpro.2023.100704, doi:10.1016/j.mcpro.2023.100704. This article has 12 citations and is from a domain leading peer-reviewed journal.

6. (joshi2021vglut3‐p.a211vvariantfuses pages 1-2): Yuvraj Joshi, Chloé P. Petit, Stéphanie Miot, Marie Guillet, Gaston Sendin, Jérôme Bourien, Jing Wang, Rémy Pujol, Salah El Mestikawy, Jean‐Luc Puel, and Régis Nouvian. Vglut3‐p.a211v variant fuses stereocilia bundles and elongates synaptic ribbons. Dec 2021. URL: https://doi.org/10.1113/jp282181, doi:10.1113/jp282181. This article has 12 citations.

7. (duhon2024genetherapyadvancements pages 4-5): Bailey H. Duhon, Eric C. Bielefeld, Yin Ren, and Jerusha Naidoo. Gene therapy advancements for the treatment of acquired and hereditary hearing loss. Frontiers in Audiology and Otology, Jul 2024. URL: https://doi.org/10.3389/fauot.2024.1423853, doi:10.3389/fauot.2024.1423853. This article has 9 citations.

8. (zhang2024aav‐mediatedgenetherapy pages 3-4): Liyan Zhang, Fangzhi Tan, Jieyu Qi, Yicheng Lu, Xiaohan Wang, Xuehan Yang, Xiangyan Chen, Xinru Zhang, Jinyi Fan, Yinyi Zhou, Li Peng, Nianci Li, Lei Xu, Shiming Yang, and Renjie Chai. Aav‐mediated gene therapy for hereditary deafness: progress and perspectives. Advanced Science, Nov 2024. URL: https://doi.org/10.1002/advs.202402166, doi:10.1002/advs.202402166. This article has 41 citations and is from a peer-reviewed journal.

9. (akil2012restorationofhearing pages 1-2): Omar Akil, Rebecca P. Seal, Kevin Burke, Chuansong Wang, Aurash Alemi, Matthew During, Robert H. Edwards, and Lawrence R. Lustig. Restoration of hearing in the vglut3 knockout mouse using virally mediated gene therapy. Neuron, 75:283-293, Jul 2012. URL: https://doi.org/10.1016/j.neuron.2012.05.019, doi:10.1016/j.neuron.2012.05.019. This article has 480 citations and is from a highest quality peer-reviewed journal.

10. (akil2012restorationofhearing pages 6-8): Omar Akil, Rebecca P. Seal, Kevin Burke, Chuansong Wang, Aurash Alemi, Matthew During, Robert H. Edwards, and Lawrence R. Lustig. Restoration of hearing in the vglut3 knockout mouse using virally mediated gene therapy. Neuron, 75:283-293, Jul 2012. URL: https://doi.org/10.1016/j.neuron.2012.05.019, doi:10.1016/j.neuron.2012.05.019. This article has 480 citations and is from a highest quality peer-reviewed journal.

11. (duhon2024genetherapyadvancements pages 11-12): Bailey H. Duhon, Eric C. Bielefeld, Yin Ren, and Jerusha Naidoo. Gene therapy advancements for the treatment of acquired and hereditary hearing loss. Frontiers in Audiology and Otology, Jul 2024. URL: https://doi.org/10.3389/fauot.2024.1423853, doi:10.3389/fauot.2024.1423853. This article has 9 citations.

12. (bottom2024defectsinhair pages 1-2): Riley T. Bottom, Yijun Xu, Caroline Siebald, Jinsei Jung, and Ulrich Müller. Defects in hair cells disrupt the development of auditory peripheral circuitry. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-55275-x, doi:10.1038/s41467-024-55275-x. This article has 7 citations and is from a highest quality peer-reviewed journal.

13. (ryu2017identificationofa pages 23-25): Nari Ryu, Seokwon Lee, Hong-Joon Park, Byeonghyeon Lee, Tae-Jun Kwon, Jinwoong Bok, Chan Ik Park, Kyu-Yup Lee, Jeong-In Baek, and Un-Kyung Kim. Identification of a novel splicing mutation within slc17a8 in a korean family with hearing loss by whole-exome sequencing. Gene, 627:233-238, Sep 2017. URL: https://doi.org/10.1016/j.gene.2017.06.040, doi:10.1016/j.gene.2017.06.040. This article has 16 citations and is from a peer-reviewed journal.

14. (ruel2008impairmentofslc17a8 pages 12-13): Jérôme Ruel, Sarah Emery, Régis Nouvian, Tiphaine Bersot, Bénédicte Amilhon, Jana M. Van Rybroek, Guy Rebillard, Marc Lenoir, Michel Eybalin, Benjamin Delprat, Theru A. Sivakumaran, Bruno Giros, Salah El Mestikawy, Tobias Moser, Richard J.H. Smith, Marci M. Lesperance, and Jean-Luc Puel. Impairment of slc17a8 encoding vesicular glutamate transporter-3, vglut3, underlies nonsyndromic deafness dfna25 and inner hair cell dysfunction in null mice. American journal of human genetics, 83 2:278-92, Aug 2008. URL: https://doi.org/10.1016/j.ajhg.2008.07.008, doi:10.1016/j.ajhg.2008.07.008. This article has 345 citations and is from a highest quality peer-reviewed journal.

15. (akil2012restorationofhearing pages 9-10): Omar Akil, Rebecca P. Seal, Kevin Burke, Chuansong Wang, Aurash Alemi, Matthew During, Robert H. Edwards, and Lawrence R. Lustig. Restoration of hearing in the vglut3 knockout mouse using virally mediated gene therapy. Neuron, 75:283-293, Jul 2012. URL: https://doi.org/10.1016/j.neuron.2012.05.019, doi:10.1016/j.neuron.2012.05.019. This article has 480 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Dominant_Nonsyndromic_Hearing_Loss_25-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 5 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:22794260` (1 mention) - Striatal dopamine release is triggered by synchronized activity in cholinergic interneurons.
  - shared terms: none

Weighed against this report's own most characteristic terms: `disease`, `human`, `dfna25`, `clinical`, `gene`, `loss`, `hearing`, `genetic`, `model`, `variant`, `slc17a8`, `dominant`, `cochlear`, `molecular`, `phenotype`, `allele`, `type`, `nonsyndromic`, `progressive`, `ihc`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011568` (3 mentions) - the report calls it "if available"; MONDO calls it **autosomal dominant nonsyndromic hearing loss 25**