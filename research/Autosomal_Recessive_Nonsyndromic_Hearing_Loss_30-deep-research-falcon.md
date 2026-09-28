---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-04T13:26:56.163204'
end_time: '2026-09-04T13:36:35.744714'
duration_seconds: 579.58
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Autosomal Recessive Nonsyndromic Hearing Loss 30
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 1
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0011774
    reported_labels:
    - MONDO
    ontology_label: autosomal recessive nonsyndromic hearing loss 30
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Recessive_Nonsyndromic_Hearing_Loss_30-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Nonsyndromic Hearing Loss 30
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Nonsyndromic Hearing Loss 30** covering all of the
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
- **Disease Name:** Autosomal Recessive Nonsyndromic Hearing Loss 30
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Nonsyndromic Hearing Loss 30** covering all of the
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


# Autosomal Recessive Nonsyndromic Hearing Loss 30 (DFNB30)

## Executive summary

Autosomal recessive nonsyndromic hearing loss 30 (DFNB30) is a very rare Mendelian sensorineural hearing-loss disorder caused by biallelic pathogenic variants in **MYO3A**, encoding the actin-based motor myosin IIIA. Its defining phenotype is bilateral, progressive hearing loss without a consistent extra-auditory syndrome. Onset is variable—from congenital hearing loss to the second decade—and progression can culminate in severe-to-profound loss. MYO3A dysfunction compromises the dimensions and maintenance of cochlear hair-cell stereocilia, probably through impaired motor activity, kinase regulation, actin interaction, and transport/regulation of stereociliary cargoes such as espin-1 and espin-like. The phenotype is distinct from autosomal-dominant MYO3A-associated hearing loss produced by particular heterozygous dominant-negative alleles. (OpenTargets Search: autosomal recessive nonsyndromic hearing loss 30-MYO3A, doll2020anovelmissense pages 1-2, dantas2018characterizationofa pages 1-2, maekawa2025theprevalenceand pages 1-2)

| Domain | Established finding | Evidence type | Ontology/identifier suggestions |
|---|---|---|---|
| Disease identity | Autosomal recessive nonsyndromic hearing loss 30 (DFNB30), a Mendelian nonsyndromic sensorineural hearing-loss disorder | Aggregated disease-resource association plus human molecular genetics (OpenTargets Search: autosomal recessive nonsyndromic hearing loss 30-MYO3A) | MONDO:0011774; synonym: DFNB30 |
| Causal gene | Biallelic loss-of-function or damaging variants in **MYO3A** (myosin IIIA) cause DFNB30; heterozygous dominant MYO3A disease is a distinct allelic disorder (OpenTargets Search: autosomal recessive nonsyndromic hearing loss 30-MYO3A, doll2020anovelmissense pages 1-2, dantas2018characterizationofa pages 1-2) | Human pedigrees, sequencing, segregation, functional studies | MYO3A; OMIM gene 606808; Ensembl ENSG00000095777 |
| Inheritance | Autosomal recessive; affected individuals are homozygous or compound heterozygous, whereas heterozygous relatives are generally carriers unless they harbor a distinct dominant-acting allele | Human family segregation (doll2020anovelmissense pages 1-2, dantas2018characterizationofa pages 1-2) | Autosomal recessive inheritance; germline variant |
| Core phenotype | Bilateral, nonsyndromic, progressive sensorineural hearing loss, often initially affecting high frequencies; reported onset ranges from congenital to the second decade and may ultimately reach severe-to-profound levels (maekawa2025theprevalenceand pages 6-8, doll2020anovelmissense pages 1-2, maekawa2025theprevalenceand pages 1-2) | Human clinical audiology and cohorts | Sensorineural hearing impairment; bilateral hearing impairment; progressive hearing impairment; high-frequency hearing impairment; profound hearing impairment |
| Anatomy and mechanism | MYO3A localizes near the tips of cochlear and vestibular hair-cell stereocilia. Impaired actin-based motor/cargo regulation disrupts stereocilia length, spacing, staircase organization, and consequently mechanotransduction (dantas2018characterizationofa pages 1-2, maekawa2025theprevalenceand pages 2-4, maekawa2025theprevalenceand pages 1-2) | Hair-cell studies, biochemical/cellular assays, mouse models; final mechanotransduction link partly inferred | Cochlea; organ of Corti; inner and outer hair cell; stereocilium; actin cytoskeleton; sensory perception of sound |
| Epidemiology | Nine candidate individuals were found among 15,684 Japanese hearing-loss referrals—**0.06% of that referral cohort**, not population prevalence (maekawa2025theprevalenceand pages 1-2, maekawa2025theprevalenceand pages 6-8) | 2025 multicenter referral-cohort sequencing study | Rare disease; prevalence among hearing-loss referrals |
| Diagnosis | Confirm sensorineural loss and progression with age-appropriate audiometry, otoacoustic emissions and/or auditory brainstem response, then identify pathogenic/likely pathogenic variants on both MYO3A alleles using a comprehensive hearing-loss panel, exome, or genome sequencing with segregation and copy-number analysis as appropriate (maekawa2025theprevalenceand pages 2-4, maekawa2025theprevalenceand pages 12-13) | Clinical audiology plus molecular diagnosis; general hereditary-hearing-loss practice | Pure-tone audiometry; auditory brainstem response; otoacoustic emission; molecular genetic testing; biallelic genotype |
| Current management | No disease-modifying MYO3A-specific treatment is established. Management follows hearing-loss severity and communication needs: serial audiology, hearing aids, cochlear implantation when indicated, and speech/language, auditory, educational, or sign-language support | Standard-of-care extrapolation from nonsyndromic sensorineural hearing loss; not tested specifically in DFNB30 | Hearing aid; cochlear implantation; audiologic rehabilitation; speech-language therapy |
| Experimental therapy | No MYO3A-targeted gene, RNA, cell, or pharmacologic therapy trial was identified; current hereditary-hearing-loss gene-therapy trials target other genes and should not be represented as DFNB30 trials | Clinical-trial search and literature review | Gene therapy—investigational; no DFNB30-specific intervention |
| Model organisms | MYO3A loss-of-function mouse models develop progressive hearing loss beginning at high frequencies and later involving broader frequencies, with abnormal stereocilia; combined Myo3a/Myo3b loss produces a stronger phenotype, indicating partial redundancy (doll2020anovelmissense pages 1-2, dantas2018characterizationofa pages 1-2, maekawa2025theprevalenceand pages 2-4) | Knock-in/knockout mouse models | Mus musculus; Myo3a knock-in/knockout; auditory hair cell; abnormal stereocilium morphology |


*Table: Concise evidence-based summary of DFNB30 identity, phenotype, mechanism, frequency, diagnosis, management, and models. It separates established disease-specific findings from standard-care extrapolation and investigational gaps.*

## 1. Disease information

### Definition and identifiers

DFNB30 is an inherited, usually bilateral, progressive **nonsyndromic sensorineural hearing loss** caused by pathogenic variants affecting both MYO3A alleles. “Nonsyndromic” means that hearing impairment is the primary consistent clinical manifestation; it does not imply that every reported patient is free of coincidental symptoms such as vertigo. Open Targets identifies one associated target, MYO3A, for this disease. (OpenTargets Search: autosomal recessive nonsyndromic hearing loss 30-MYO3A)

| Field | Entry |
|---|---|
| Preferred name | Autosomal recessive nonsyndromic hearing loss 30 |
| Common synonyms | DFNB30; deafness, autosomal recessive 30; MYO3A-related autosomal recessive hearing loss; MYO3A-related DFNB30 |
| MONDO | **MONDO:0011774** |
| Causal gene | **MYO3A**, myosin IIIA; Ensembl **ENSG00000095777** |
| Gene OMIM | **606808** |
| Disease OMIM | Commonly represented as **607101**; users should verify against the current OMIM release before database ingestion |
| Orphanet | No confidently disease-specific ORPHA identifier was recovered; it may be nested under genetic nonsyndromic deafness classifications |
| ICD-10-CM | No DFNB30-specific code; use phenotype codes such as H90.3 for bilateral sensorineural hearing loss as clinically appropriate |
| ICD-11 | No known gene-specific DFNB30 code; classify under sensorineural hearing loss |
| MeSH | No DFNB30-specific descriptor; relevant headings include *Hearing Loss, Sensorineural* and *Hearing Loss, Genetic* |

The original disease evidence was patient-level pedigree and molecular-genetic evidence. Modern MONDO/Open Targets entries and review resources are aggregated disease-level representations of those cases—not individual EHR records. Open Targets cites literature including PMIDs **12032315**, **21165622**, **26841241**, **29880844**, and **33078831** in support of the MYO3A association. (OpenTargets Search: autosomal recessive nonsyndromic hearing loss 30-MYO3A)

The landmark report was Walsh et al., *PNAS*, published 28 May 2002, DOI [10.1073/pnas.102091699](https://doi.org/10.1073/pnas.102091699), PMID **12032315**. Its abstract states: **“In an extended Israeli family, nonsyndromic progressive hearing loss is caused by three different recessive, loss-of-function mutations in myosin IIIA.”** It further reports that, among 18 affected relatives, seven were homozygous and 11 compound heterozygous. (souissi2022molecularinsightsinto pages 12-13)

## 2. Etiology

### Causal and genetic factors

The primary cause is **germline biallelic MYO3A dysfunction**. Established disease alleles include nonsense, frameshift, splice-disrupting, and damaging missense variants in the kinase, motor, and tail regions. The 2002 Family N carried three recessive loss-of-function alleles; later families expanded the spectrum and demonstrated congenital as well as delayed-onset disease. (doll2020anovelmissense pages 1-2, maekawa2025theprevalenceand pages 2-4)

Representative reported variants include:

- **p.Ser614Phe**, a recessive motor-domain variant reported in a consanguineous Kazakh family with congenital hearing loss. (dantas2018characterizationofa pages 1-2)
- **p.Lys50Arg**, a kinase-domain variant segregating with congenital profound nonsyndromic hearing loss; computational and previous in-vitro evidence supported a “kinase-dead” effect. DOI [10.1080/07391102.2021.1953600](https://doi.org/10.1080/07391102.2021.1953600), published in final form in 2022. (souissi2022molecularinsightsinto pages 12-13)
- Recent Japanese candidates included **c.893dupA (p.Gln300Thrfs*21)**, **c.991C>T (p.Arg331Ter)**, **c.1450T>C (p.Ser484Pro)**, **c.1464del (p.Lys489Asnfs*3)**, and **c.4164dup (p.Asn1389Lysfs*4)**. Two reported missense candidates, p.Ala238Thr and p.Glu770Lys, remained VUS in that study and should not independently establish diagnosis. (maekawa2025theprevalenceand pages 4-6)

Allele frequencies in the recent Japanese series were below 0.0007. Exact gnomAD frequencies must be retrieved by transcript/build and variant; rarity alone is not evidence of pathogenicity. Variants are germline, not somatic. (maekawa2025theprevalenceand pages 6-8)

### Risk, protective factors, and gene–environment interaction

- **Risk:** two pathogenic alleles in trans; parental consanguinity increases the probability that a rare allele is inherited homozygously. Family history may be absent because carriers are generally unaffected and onset can be delayed.
- **Modifiers:** no replicated DFNB30 modifier gene has been established. Partial functional redundancy with **MYO3B** is biologically important, but a clinically validated human MYO3B modifier effect has not been demonstrated. (maekawa2025theprevalenceand pages 2-4)
- **Protective alleles:** none established.
- **Environmental causes:** noise, aminoglycosides, cisplatin, and other ototoxic exposures can independently worsen hearing, but no DFNB30-specific gene–environment interaction has been demonstrated.
- **Lifestyle, infection, sex, diet:** no evidence that these initiate the Mendelian disorder. Avoiding excessive noise and unnecessary ototoxins protects residual hearing generally but does not prevent inheritance or molecular onset.

## 3. Phenotypes

| Phenotype | Characterization | Suggested HPO annotation |
|---|---|---|
| Sensorineural hearing impairment | Defining manifestation; usually bilateral and nonsyndromic | Sensorineural hearing impairment; Bilateral sensorineural hearing impairment |
| Progressive hearing impairment | Common defining course; all eight clinically characterized individuals in the 2025 Japanese series recognized progression | Progressive hearing impairment |
| High-frequency-predominant loss | Characteristic in original Family N and mouse model; six of eight recent audiograms were down-sloping | High-frequency hearing impairment |
| Severe/profound hearing loss | May be congenital for severe alleles or arise after progression | Severe hearing impairment; Profound hearing impairment |
| Postlingual hearing impairment | Common in later-onset disease; recent cohort onset usually 10–30 years | Postlingual hearing impairment |
| Congenital hearing impairment | Documented with some kinase/motor-domain alleles | Congenital sensorineural hearing impairment |
| Vertigo/vestibular symptom | Reported in two recent subjects, but not sufficiently consistent to redefine DFNB30 as syndromic | Vertigo, if clinically documented |

In the 2025 Japanese referral cohort, clinical data from eight patients showed onset at 10–30 years (mean **19.6 years**), mild-to-profound severity, six down-sloping and two flat audiograms, and recognized progression in all eight. Two reported vertigo. The broader literature supports onset from birth through the second decade and eventual severe-to-profound loss. (maekawa2025theprevalenceand pages 6-8, maekawa2025theprevalenceand pages 1-2)

Phenotype frequencies cannot be generalized reliably because published cases are few and ascertainment is biased. The strongest qualitative conclusions are bilateral sensorineural loss, progression, and frequent early high-frequency involvement. There is no validated DFNB30-specific EQ-5D, SF-36, PROMIS, behavioral, or laboratory phenotype. Expected consequences of inadequately treated hearing loss include impaired speech perception, communication, education, employment, and social participation, especially when onset occurs before or during language acquisition; these are general hearing-loss consequences rather than quantified DFNB30-specific outcomes.

## 4. Genetic and molecular information

**MYO3A** lies at chromosome **10p12.1**, has 33 exons, and encodes myosin IIIA. Its architecture comprises an N-terminal serine/threonine kinase region, an actin-activated ATPase motor/head, a neck containing three IQ/calmodulin-binding motifs, and a specialized C-terminal tail with actin- and cargo-interaction functions. (doll2020anovelmissense pages 1-2)

Pathogenic mechanisms are principally **loss of function or severe functional impairment**. Truncating and canonical splice variants may cause absent/truncated protein or nonsense-mediated decay. Missense variants can disrupt ATP binding, kinase autophosphorylation, actin binding, ATPase cycling, motility, or tip localization. Both intact motor and tail domains are needed for normal tip localization and actin-protrusion regulation. (maekawa2025theprevalenceand pages 2-4)

Variant interpretation should use ACMG/AMP criteria with hearing-loss specifications, population frequency, phase, segregation, phenotype consistency, and functional evidence. A VUS must not be used alone for predictive testing or reproductive decision-making. No recurrent large chromosomal abnormality, repeat expansion, mitochondrial lesion, or somatic event defines DFNB30. No clinically established DNA-methylation, histone, or other epigenetic signature is known.

Particular heterozygous MYO3A motor/kinase variants cause a **distinct autosomal-dominant allelic disorder**. For example, p.Leu697Trp reduces ATPase activity and motility, increases actin affinity, displaces wild-type MYO3A at stereocilia tips, and acts dominantly negatively. It must not be conflated with recessive DFNB30. (dantas2018characterizationofa pages 1-2, dantas2018characterizationofa pages 10-11, dantas2018characterizationofa pages 2-3)

## 5. Environmental information

DFNB30 is not an infectious, toxic, nutritional, occupational, or lifestyle-induced disease. No pathogen, immune trigger, smoking effect, dietary factor, radiation exposure, or pollution exposure has been shown to cause it. General cochlear hazards—intense noise, aminoglycosides, platinum chemotherapy, and other ototoxic agents—may add acquired injury to genetically vulnerable hearing but have not been shown to interact specifically with MYO3A. Such exposures should be documented as comorbidity or possible aggravators, not disease causes.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic pathogenic MYO3A variants lead to** absent, unstable, truncated, kinase-impaired, or motor-impaired myosin IIIA.
2. **MYO3A dysfunction leads to** reduced actin-plus-end motility and/or abnormal kinase autophosphorylation, actin binding, and stereociliary tip localization.
3. **Impaired tip-directed function leads to** abnormal delivery or regulation of actin-associated cargoes, especially espin-1 and espin-like; a role in PCDH15-CD2 trafficking is supported experimentally but its contribution to human DFNB30 remains partly inferred. (dantas2018characterizationofa pages 1-2, dantas2018characterizationofa pages 10-11)
4. **Abnormal motor/cargo regulation results in** disturbed actin-protrusion growth, stereocilia length, width, spacing, and staircase organization; MYO3B partially compensates, producing variable onset and progression. (maekawa2025theprevalenceand pages 2-4, maekawa2025theprevalenceand pages 1-2)
5. **Disordered stereociliary architecture leads to** inefficient hair-bundle deflection and impaired mechanoelectrical transduction; this final connection is strongly biologically supported but not directly measured in living DFNB30 patients.
6. **Chronic hair-cell dysfunction and probable degeneration result in** high-frequency sensorineural hearing loss that progressively spreads to additional frequencies and may become severe-to-profound. (doll2020anovelmissense pages 1-2, dantas2018characterizationofa pages 1-2)

This is primarily a **cytoskeletal mechanotransduction disorder**, not a canonical Wnt, MAPK, PI3K–AKT, immune, inflammatory, or metabolic disease. Relevant processes include actin-filament organization, actin-dependent motor activity, protein transport along actin, stereocilium organization, sensory perception of sound, and auditory receptor-cell development/maintenance. Suggested GO concepts are *actin filament organization*, *actin-dependent ATPase activity*, *microfilament motor activity*, *stereocilium organization*, *protein localization to stereocilium*, and *sensory perception of sound*.

The principal cells are cochlear inner and outer hair cells—suggested CL concepts: *auditory hair cell*, *inner hair cell*, and *outer hair cell*. Vestibular hair-cell expression is documented, although clinically important vestibular disease is inconsistent. MYO3A localizes at the stereociliary tip and associates with the F-actin cytoskeleton and plasma-membrane-adjacent tip complex. (maekawa2025theprevalenceand pages 1-2, doll2020anovelmissense pages 1-2)

No validated DFNB30 patient transcriptomic, proteomic, metabolomic, lipidomic, spatial-transcriptomic, or single-cell disease signature was found. Available molecular profiling is principally expression/localization, biochemical motor assays, structural modeling, cultured-cell protrusion assays, and animal hair-bundle morphology.

## 7. Anatomical structures affected

- **Organ/system:** inner ear; auditory system.
- **Primary site:** cochlea and organ of Corti.
- **Tissue:** sensory neuroepithelium.
- **Cells:** inner and outer cochlear hair cells; vestibular hair cells express MYO3A but are not consistently clinically impaired.
- **Subcellular site:** actin-rich stereocilia, especially distal tips; F-actin core and associated cargo complex.
- **Laterality:** usually bilateral.
- **Suggested UBERON terms:** inner ear, cochlea, organ of Corti, cochlear hair cell, hair-cell stereocilium; vestibular sensory epithelium may be recorded as an expression site rather than a universally diseased structure.
- **Suggested GO cellular components:** stereocilium, stereocilium tip, actin cytoskeleton, actin filament bundle.

No consistent secondary-organ disease is established despite MYO3A expression in retina; the human DFNB30 phenotype remains nonsyndromic. (doll2020anovelmissense pages 1-2)

## 8. Temporal development

Onset varies from congenital to the second decade. Classic Family N developed bilateral high-frequency loss beginning in the second decade, whereas some later kinase- or motor-domain genotypes caused congenital profound loss. The condition is chronic and lifelong. Progression is generally insidious rather than episodic, initially affecting higher frequencies and later broader frequencies. (doll2020anovelmissense pages 1-2, maekawa2025theprevalenceand pages 1-2)

No formal staging system or genotype-specific annual dB progression rate exists. Practical stages are: detectable high-frequency loss; broader speech-frequency involvement; severe-to-profound hearing loss requiring increasingly intensive rehabilitation. Spontaneous remission is not expected. Critical intervention periods include infancy and early childhood for congenital cases and the interval before speech-frequency deterioration in later-onset cases.

## 9. Inheritance and population

Inheritance is autosomal recessive. When both parents are heterozygous carriers, each pregnancy has a 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of inheriting neither familial allele. Both sexes should be affected equally. Penetrance appears high for clearly pathogenic biallelic genotypes but may be age-dependent; exact penetrance estimates are unavailable. Expressivity is variable in onset and severity. Anticipation has not been reported. Germline mosaicism is theoretically possible but not established as a recurrent feature.

The original extended Israeli Jewish family and subsequent Kazakh, Chinese, Tunisian/North African, Cameroonian, and Japanese cases demonstrate broad geographic distribution. Consanguinity has facilitated discovery, but DFNB30 is not limited to consanguineous families. No universally important founder allele or reliable global carrier frequency has been established. (doll2020anovelmissense pages 1-2, dantas2018characterizationofa pages 1-2, maekawa2025theprevalenceand pages 12-13)

In the largest recent study, nine candidates were detected among **15,684 Japanese hearing-loss referrals**, or **0.06%**. This is a clinic-based proportion—not population prevalence or annual incidence. Before that study, only 13 cases had reportedly been published. Disease-specific prevalence per 100,000 and incidence are unknown. (maekawa2025theprevalenceand pages 1-2, maekawa2025theprevalenceand pages 6-8, maekawa2025theprevalenceand pages 2-4)

## 10. Diagnostics

### Clinical evaluation

Diagnosis starts with otoscopy and age-appropriate audiology: pure-tone and speech audiometry, tympanometry, otoacoustic emissions, and auditory brainstem response when behavioral testing is unreliable. Serial audiograms are important because progression is central to DFNB30. Vestibular testing is appropriate when vertigo or imbalance is present. CT/MRI is not diagnostic of DFNB30 and should be reserved for cochlear-implant planning, asymmetric findings, or suspected structural disease.

There is no characteristic blood, urine, enzyme, metabolite, biopsy, or circulating biomarker. The molecular biomarker is a pathogenic/likely pathogenic **biallelic MYO3A genotype in trans** consistent with phenotype and inheritance.

### Genetic-testing strategy

1. Use a comprehensive hereditary-hearing-loss panel that includes **MYO3A**, with deletion/duplication analysis.
2. If nondiagnostic, use exome or genome sequencing, ideally trio/family based; genome sequencing can better detect noncoding and structural variants.
3. Confirm candidate variants and phase by parental/relative testing.
4. Apply hearing-loss-specific ACMG/AMP interpretation and periodically reanalyze negative or VUS results.
5. Single-gene testing is efficient only when familial MYO3A variants are already known.

The 2025 multicenter study used massively parallel sequencing of 158 hearing-loss genes, illustrating current real-world implementation and why a panel is preferable to sequential single-gene testing in this genetically heterogeneous phenotype. (maekawa2025theprevalenceand pages 2-4)

CMA, karyotyping, FISH, mitochondrial DNA testing, and repeat-expansion testing are not first-line DFNB30 tests unless other clinical findings suggest an alternative diagnosis. Differential diagnoses include other progressive nonsyndromic hearing-loss genes—such as TMC1, TMPRSS3, MYO15A, POU4F3, ACTG1, and dominant MYO3A alleles—plus congenital CMV, noise/ototoxic injury, auditory neuropathy, and syndromic hearing loss.

Newborn physiologic hearing screening remains essential but may miss delayed-onset DFNB30. Once a familial genotype is known, cascade testing can identify siblings or relatives requiring prospective audiologic surveillance.

## 11. Outcome and prognosis

DFNB30 does not appear to shorten life expectancy or directly increase mortality. Its burden is auditory disability rather than systemic organ failure. Untreated progression can substantially impair speech understanding, communication, education, employment, safety, and social participation. Congenital profound loss poses the greatest risk to spoken-language development if access to communication and rehabilitation is delayed.

Hearing recovery is not expected spontaneously. Functional prognosis depends on age at onset, rate and severity of progression, timing and consistency of amplification, communication access, and candidacy for cochlear implantation. No validated molecular prognostic biomarker exists, although genotype/domain and residual MYO3A function may partly explain congenital-profound versus later-progressive phenotypes. The 2025 study concluded that genetic identification can help anticipate progression and enable timely intervention. (maekawa2025theprevalenceand pages 1-2)

## 12. Treatment

There is no approved MYO3A-restoring drug, RNA therapy, cell therapy, or gene therapy. Pharmacogenomic guidance specific to DFNB30 is unavailable.

Current management is individualized:

- **Hearing aids** for aidable mild-to-severe loss; suggested NCIt concept: *Hearing Aid*.
- **Cochlear implantation** for severe-to-profound loss with insufficient aided speech recognition; suggested NCIt concept: *Cochlear Implantation*.
- **Audiologic rehabilitation**, auditory-verbal or speech-language therapy, educational accommodations, assistive listening technology, captioning, and/or sign-language access according to patient goals.
- **Serial audiometry**, because thresholds may deteriorate after a normal newborn screen or initial mild high-frequency loss.
- **Vestibular rehabilitation** only for documented vestibular dysfunction.

A ClinicalTrials.gov search found gene-therapy studies for other genetic hearing losses—including OTOF and GJB2—and general human auditory-cell transduction research, but no MYO3A/DFNB30-specific interventional trial. Those studies should not be entered as DFNB30 treatments.

Gene replacement is conceptually attractive because recessive disease is usually loss-of-function, but challenges include MYO3A coding size, delivery to the correct mature hair cells, dosage, developmental timing, and whether abnormal/degenerating stereocilia remain rescuable. Thus, gene therapy is preclinical speculation, not present clinical care.

## 13. Prevention

The inherited genotype cannot be prevented by lifestyle modification.

- **Primary prevention/reproductive options:** genetic counseling, partner testing when appropriate, prenatal diagnosis, and preimplantation genetic testing for monogenic disease after familial variants are established. These are optional, values-sensitive choices—not requirements.
- **Secondary prevention:** newborn hearing screening, cascade genetic testing, and periodic audiology for genetically at-risk relatives, including those who initially pass newborn screening.
- **Tertiary prevention:** early amplification or implantation, communication access, education support, and avoidance of unnecessary cochlear hazards to preserve residual hearing.
- **Vaccination:** no DFNB30-specific vaccine; routine immunization can prevent some acquired infectious causes of hearing loss but not MYO3A disease.
- **Counseling:** clearly distinguish recessive carrier status from dominant MYO3A alleles and explain age-dependent manifestation.

## 14. Other species and natural disease

No well-established naturally occurring companion-animal or livestock disorder directly equivalent to human MYO3A-DFNB30 was identified. There is no zoonotic potential or cross-species transmission because this is a germline genetic disease.

The human MYO3A protein is evolutionarily related to Drosophila **NINAC**, a class III myosin required in photoreceptors. The original paper described this as an evolutionary connection between visual and auditory sensory systems, but NINAC retinal degeneration is not a literal fly model of human cochlear disease. (souissi2022molecularinsightsinto pages 12-13)

Suggested taxonomy annotations include *Homo sapiens* (NCBI Taxon 9606), *Mus musculus* (10090), and *Drosophila melanogaster* (7227). Ortholog identifiers should be taken from the current NCBI Gene/Alliance release at ingestion.

## 15. Model organisms

The most disease-relevant model is the mouse carrying a human DFNB30-associated MYO3A loss-of-function allele. These mice developed significant hearing loss by approximately **2.5 months**, first at high frequencies and subsequently across all tested frequencies, recapitulating the progressive human course. DOI [10.1007/s00335-010-9310-6](https://doi.org/10.1007/s00335-010-9310-6), PMID **21165622**. (doll2020anovelmissense pages 1-2, dantas2018characterizationofa pages 1-2)

Myo3a-deficient mice show abnormal stereocilia dimensions and spacing. Combined Myo3a/Myo3b deficiency produces a more severe or profound phenotype than MYO3A loss alone, demonstrating partial redundancy between class III myosins. These models are useful for longitudinal auditory brainstem response testing, otoacoustic emissions, ultrastructural analysis, actin/cargo trafficking, and preclinical rescue studies. (maekawa2025theprevalenceand pages 1-2, maekawa2025theprevalenceand pages 2-4)

Limitations include interspecies differences in cochlear maturation and frequency range, redundancy between Myo3a and Myo3b, and the inability of a single engineered allele to represent the full human genotype–phenotype spectrum. COS-7 filopodia and epithelial microvilli are useful reductionist systems for motor and actin-protrusion assays but are not auditory hair cells. Patient-derived iPSC hair-cell or organoid models would be valuable, but no validated DFNB30 clinical platform was identified.

## Recent developments and evidence appraisal

A 2024 authoritative review of hearing-loss-associated myosins emphasized that MYO3A, MYO6, MYO7A, and MYO15A are essential to developing and maintaining functional hair-cell stereocilia, while also noting that variant-level clinical correlations and in-stereocilium trafficking remain incompletely understood. Miyoshi et al., *Frontiers in Physiology*, published March 2024, DOI [10.3389/fphys.2024.1374901](https://doi.org/10.3389/fphys.2024.1374901). This is expert synthesis rather than new DFNB30 patient evidence. (elbagoury2025wholeexomesequencing pages 10-11)

The strongest new disease-specific clinical evidence is the study published **16 January 2025**, just outside the requested 2023–2024 priority window. It supplied the largest unrelated MYO3A series, eight candidate causal variants—six novel—and the 0.06% estimate among Japanese hearing-loss referrals. Its abstract states: **“Our findings confirmed that MYO3A variants cause progressive hearing loss, with its onset varying from birth to the second decade, eventually leading to severe-to-profound hearing loss.”** Maekawa et al., *Genes* 2025;16:92, DOI [10.3390/genes16010092](https://doi.org/10.3390/genes16010092). (maekawa2025theprevalenceand pages 1-2)

Overall certainty is **high** for MYO3A causality, autosomal-recessive inheritance, sensorineural pathology, and progression; **moderate** for domain-specific genotype–phenotype correlations and individual cargo contributions; and **low or absent** for population prevalence, penetrance estimates, modifiers, environmental interaction, epigenetics, patient omics, disease-specific quality-of-life statistics, and MYO3A-targeted treatment outcomes.

References

1. (OpenTargets Search: autosomal recessive nonsyndromic hearing loss 30-MYO3A): Open Targets Query (autosomal recessive nonsyndromic hearing loss 30-MYO3A, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (doll2020anovelmissense pages 1-2): Julia Doll, Michaela A. H. Hofrichter, Paulina Bahena, Alfred Heihoff, Dennis Segebarth, Tobias Müller, Marcus Dittrich, Thomas Haaf, and Barbara Vona. A novel missense variant in myo3a is associated with autosomal dominant high‐frequency hearing loss in a german family. Molecular Genetics & Genomic Medicine, Jun 2020. URL: https://doi.org/10.1002/mgg3.1343, doi:10.1002/mgg3.1343. This article has 17 citations and is from a peer-reviewed journal.

3. (dantas2018characterizationofa pages 1-2): Vitor G. L. Dantas, Manmeet H. Raval, Angela Ballesteros, Runjia Cui, Laura K. Gunther, Guilherme L. Yamamoto, Leandro Ucela Alves, André Silva Bueno, Karina Lezirovitz, Sulene Pirana, Beatriz C. A. Mendes, Christopher M. Yengo, Bechara Kachar, and Regina C. Mingroni-Netto. Characterization of a novel myo3a missense mutation associated with a dominant form of late onset hearing loss. Scientific Reports, Jun 2018. URL: https://doi.org/10.1038/s41598-018-26818-2, doi:10.1038/s41598-018-26818-2. This article has 32 citations and is from a peer-reviewed journal.

4. (maekawa2025theprevalenceand pages 1-2): Karuna Maekawa, Shin-ya Nishio, Hiromitsu Miyazaki, Yoko Ohta, Naoki Oishi, Misato Kasai, Ai Yamamoto, Mayuri Okami, Koichiro Wasano, Akihiro Sakai, and Shin-ichi Usami. The prevalence and clinical characteristics of myo3a-associated hearing loss in 15,684 hearing loss patients. Jan 2025. URL: https://doi.org/10.3390/genes16010092, doi:10.3390/genes16010092. This article has 1 citations.

5. (maekawa2025theprevalenceand pages 6-8): Karuna Maekawa, Shin-ya Nishio, Hiromitsu Miyazaki, Yoko Ohta, Naoki Oishi, Misato Kasai, Ai Yamamoto, Mayuri Okami, Koichiro Wasano, Akihiro Sakai, and Shin-ichi Usami. The prevalence and clinical characteristics of myo3a-associated hearing loss in 15,684 hearing loss patients. Jan 2025. URL: https://doi.org/10.3390/genes16010092, doi:10.3390/genes16010092. This article has 1 citations.

6. (maekawa2025theprevalenceand pages 2-4): Karuna Maekawa, Shin-ya Nishio, Hiromitsu Miyazaki, Yoko Ohta, Naoki Oishi, Misato Kasai, Ai Yamamoto, Mayuri Okami, Koichiro Wasano, Akihiro Sakai, and Shin-ichi Usami. The prevalence and clinical characteristics of myo3a-associated hearing loss in 15,684 hearing loss patients. Jan 2025. URL: https://doi.org/10.3390/genes16010092, doi:10.3390/genes16010092. This article has 1 citations.

7. (maekawa2025theprevalenceand pages 12-13): Karuna Maekawa, Shin-ya Nishio, Hiromitsu Miyazaki, Yoko Ohta, Naoki Oishi, Misato Kasai, Ai Yamamoto, Mayuri Okami, Koichiro Wasano, Akihiro Sakai, and Shin-ichi Usami. The prevalence and clinical characteristics of myo3a-associated hearing loss in 15,684 hearing loss patients. Jan 2025. URL: https://doi.org/10.3390/genes16010092, doi:10.3390/genes16010092. This article has 1 citations.

8. (souissi2022molecularinsightsinto pages 12-13): Amal Souissi, Dorra Abdelmalek Driss, Imen Chakchouk, Mariem Ben Said, Ikhlas Ben Ayed, Mohamed Ali Mosrati, Ines Elloumi, Abdelaziz Tlili, Sami Aifa, and Saber Masmoudi. Molecular insights into myo3a kinase domain variants explain variability in both severity and progression of dfnb30 hearing impairment. Journal of Biomolecular Structure and Dynamics, 40:10940-10951, Aug 2022. URL: https://doi.org/10.1080/07391102.2021.1953600, doi:10.1080/07391102.2021.1953600. This article has 4 citations and is from a peer-reviewed journal.

9. (maekawa2025theprevalenceand pages 4-6): Karuna Maekawa, Shin-ya Nishio, Hiromitsu Miyazaki, Yoko Ohta, Naoki Oishi, Misato Kasai, Ai Yamamoto, Mayuri Okami, Koichiro Wasano, Akihiro Sakai, and Shin-ichi Usami. The prevalence and clinical characteristics of myo3a-associated hearing loss in 15,684 hearing loss patients. Jan 2025. URL: https://doi.org/10.3390/genes16010092, doi:10.3390/genes16010092. This article has 1 citations.

10. (dantas2018characterizationofa pages 10-11): Vitor G. L. Dantas, Manmeet H. Raval, Angela Ballesteros, Runjia Cui, Laura K. Gunther, Guilherme L. Yamamoto, Leandro Ucela Alves, André Silva Bueno, Karina Lezirovitz, Sulene Pirana, Beatriz C. A. Mendes, Christopher M. Yengo, Bechara Kachar, and Regina C. Mingroni-Netto. Characterization of a novel myo3a missense mutation associated with a dominant form of late onset hearing loss. Scientific Reports, Jun 2018. URL: https://doi.org/10.1038/s41598-018-26818-2, doi:10.1038/s41598-018-26818-2. This article has 32 citations and is from a peer-reviewed journal.

11. (dantas2018characterizationofa pages 2-3): Vitor G. L. Dantas, Manmeet H. Raval, Angela Ballesteros, Runjia Cui, Laura K. Gunther, Guilherme L. Yamamoto, Leandro Ucela Alves, André Silva Bueno, Karina Lezirovitz, Sulene Pirana, Beatriz C. A. Mendes, Christopher M. Yengo, Bechara Kachar, and Regina C. Mingroni-Netto. Characterization of a novel myo3a missense mutation associated with a dominant form of late onset hearing loss. Scientific Reports, Jun 2018. URL: https://doi.org/10.1038/s41598-018-26818-2, doi:10.1038/s41598-018-26818-2. This article has 32 citations and is from a peer-reviewed journal.

12. (elbagoury2025wholeexomesequencing pages 10-11): Nagham M. Elbagoury, Engy A. Ashaat, Mona K. Mekkawy, Ragaey Y. Mohamed, Anas M. Askoura, Peter M. Milad, and Mona L. Essawi. Whole exome sequencing diagnosing syndromic and non-syndromic hearing loss with expansion of the phenotypic spectrum related to tmc1 variants. European Journal of Pediatrics, Mar 2025. URL: https://doi.org/10.1007/s00431-025-06052-5, doi:10.1007/s00431-025-06052-5. This article has 2 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Recessive_Nonsyndromic_Hearing_Loss_30-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011774` (2 mentions) - the report calls it "MONDO"; MONDO calls it **autosomal recessive nonsyndromic hearing loss 30**
