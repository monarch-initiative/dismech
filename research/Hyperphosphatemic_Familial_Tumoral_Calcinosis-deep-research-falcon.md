---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-04T23:23:55.580645'
end_time: '2026-09-04T23:32:45.733669'
duration_seconds: 530.15
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hyperphosphatemic Familial Tumoral Calcinosis
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 13
  verified: 8
  not_found: 0
  obsolete: 0
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0002905
    reported_labels:
    - Universal biochemical hallmark in characterized cohorts; persistent, age-adjusted
      elevation
    ontology_label: Hyperphosphatemia
  unresolvable_prefixes:
  - Orphanet
  - OMIM
  - Taxonomy
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hyperphosphatemic_Familial_Tumoral_Calcinosis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hyperphosphatemic Familial Tumoral Calcinosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hyperphosphatemic Familial Tumoral Calcinosis** covering all of the
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
- **Disease Name:** Hyperphosphatemic Familial Tumoral Calcinosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hyperphosphatemic Familial Tumoral Calcinosis** covering all of the
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


# Hyperphosphatemic Familial Tumoral Calcinosis: Disease-Characteristics Report

## Executive summary

Hyperphosphatemic familial tumoral calcinosis (HFTC) is an ultra-rare Mendelian disorder caused by deficient fibroblast growth factor-23 (FGF23) activity. Biallelic pathogenic variants in **GALNT3**, **FGF23**, or **KL** cause renal phosphate retention, hyperphosphatemia, inadequately suppressed calcitriol, and deposition of calcium-phosphate material in periarticular and other soft tissues. Hyperostosis-hyperphosphatemia syndrome (HHS) is now considered part of the same phenotypic spectrum. Clinical expression ranges from biochemical-only disease to recurrent inflammatory hyperostosis, massive disabling calcific tumors, dental abnormalities, and vascular or visceral calcification. Evidence remains limited principally to case reports, small cohorts, and animal models; no disease-specific randomized treatment trial or validated management guideline was identified. (ramnitz2016phenotypicandgenotypic pages 1-6, ito2021congenitalhyperphosphatemicconditions pages 1-2)

| Domain | Evidence-backed finding | Quantitative data | Ontology/identifier suggestions |
|---|---|---|---|
| Disease definition | Ultra-rare Mendelian disorder of deficient FGF23 activity or signaling, characterized by renal phosphate retention, hyperphosphatemia, inappropriately normal/high calcitriol, and ectopic calcium-phosphate deposition; hyperostosis-hyperphosphatemia syndrome represents an overlapping phenotypic spectrum. (ramnitz2016phenotypicandgenotypic pages 1-6, ito2021congenitalhyperphosphatemicconditions pages 1-2) | Reported manifestations range from biochemical-only disease to massive disabling calcinosis. | Orphanet:306661; OMIM:211900; suggested synonym: hyperphosphatemic familial tumoral calcinosis/hyperostosis-hyperphosphatemia syndrome (HFTC/HHS). |
| Molecular subtypes | HFTC1 results from biallelic **GALNT3** variants; HFTC2 from biallelic **FGF23** variants; HFTC3 from biallelic **KL** variants. (OpenTargets Search: Hyperphosphatemic familial tumoral calcinosis-FGF23,GALNT3,KL, ito2021congenitalhyperphosphatemicconditions pages 2-3) | Literature through 2017 identified 44 GALNT3, 19 FGF23, and 1 KL cases among 64 reported cases. | HFTC1—OMIM:211900; HFTC2—OMIM:617993, MONDO:0060714; HFTC3—OMIM:617994, MONDO:0060715. |
| Causal genes and inheritance | **GALNT3** loss impairs protective O-glycosylation of FGF23; **FGF23** loss-of-function impairs hormone secretion/stability; **KL** loss causes resistance to FGF23 signaling. Inheritance is autosomal recessive, usually through germline homozygous or compound-heterozygous variants. (farrow2011miscellaneousnoninflammatorymusculoskeletal pages 3-4, ito2021congenitalhyperphosphatemicconditions pages 1-2) | GALNT3 is the most frequently reported cause; heterozygous carriers are generally unaffected. | HGNC gene symbols: GALNT3, FGF23, KL; Open Targets disease associations support all three genes. (OpenTargets Search: Hyperphosphatemic familial tumoral calcinosis-FGF23,GALNT3,KL) |
| Hallmark biochemistry | Deficient FGF23 action causes excessive proximal-tubular phosphate reabsorption and failure to suppress calcitriol. GALNT3/FGF23 disease generally shows low or inappropriately normal intact FGF23 with markedly elevated C-terminal FGF23 fragments; KL disease shows high intact FGF23 because of hormone resistance. (ito2021congenitalhyperphosphatemicconditions pages 3-4, farrow2011miscellaneousnoninflammatorymusculoskeletal pages 3-4) | NIH cohort: TRP 96.5%, median TmP/GFR 6.5 mg/dL, median 1,25(OH)₂D 62 pg/mL, and median calcium-phosphate product 63.5 mg²/dL². (ramnitz2016phenotypicandgenotypic pages 6-10) | HPO suggestion: Hyperphosphatemia—HP:0002905; laboratory concepts: serum phosphate, TmP/GFR, TRP, intact FGF23, C-terminal FGF23, 1,25-dihydroxyvitamin D. |
| Tumoral calcinosis | Lobular calcium-phosphate masses arise chiefly in periarticular skin, subcutaneous tissue, and connective tissue, especially near the hips, elbows, and shoulders; lesions may be painful, inflamed, ulcerating, infected, and functionally disabling. (ito2021congenitalhyperphosphatemicconditions pages 3-4, cherian2024clinicalcharacteristicstherapeutic pages 2-3) | Six of eight NIH-cohort participants had clinically evident tumoral calcinosis; one initially asymptomatic participant subsequently developed elbow calcinosis. (ramnitz2016phenotypicandgenotypic pages 6-10) | HPO suggestions: Calcinosis; Subcutaneous calcification; Joint limitation; Pain. UBERON suggestions: skin, subcutaneous tissue, hip joint, elbow joint, shoulder joint; exact term identifiers should be ontology-verified. |
| Skeletal and inflammatory disease | Diaphyseal cortical hyperostosis causes episodic painful swelling, warmth, and erythema and may mimic bacterial osteomyelitis or chronic recurrent multifocal osteomyelitis. Calcific lesions can provoke macrophage-rich chronic inflammation and heterotopic ossification. (ramnitz2016phenotypicandgenotypic pages 13-17, ramnitz2016phenotypicandgenotypic pages 1-6) | Three of eight NIH subjects had severe systemic inflammation; biopsies from four showed ectopic calcification with chronic inflammation. (ramnitz2016phenotypicandgenotypic pages 13-17, ramnitz2016phenotypicandgenotypic pages 1-6) | HPO suggestions: Hyperostosis; Limb pain; Elevated C-reactive protein; Fever; Soft-tissue swelling. GO suggestions: inflammatory response—GO:0006954; biomineral tissue development—GO:0031214. |
| Dental phenotype | Characteristic findings include shortened or thistle-shaped roots, midroot bulges with apical thinning, pulp calcification or obliteration, and pulp stones; premolars are usually most severely affected. (lee2021across‐sectionalcohort pages 4-5) | Pulp obliteration occurred in 13/14 evaluable patients (93%); all 10 comprehensively examined patients with GALNT3 variants had shortened thistle-shaped roots and pulp obliteration. (lee2021across‐sectionalcohort pages 4-5) | HPO suggestions: Abnormality of dental root; Pulp calcification; Short tooth roots. Exact identifiers require ontology verification. |
| Other anatomy and complications | Reported involvement includes vascular and coronary calcification, colonic submucosal deposits, ocular and testicular calcification, joint or growth-plate destruction, and reduced range of motion. (ramnitz2016phenotypicandgenotypic pages 13-17, ito2021congenitalhyperphosphatemicconditions pages 1-2) | Coronary calcification above the 95th percentile occurred in 2/5 evaluated NIH subjects, although confounding cardiovascular risks prevent attribution solely to HFTC. (ramnitz2016phenotypicandgenotypic pages 13-17) | UBERON suggestions: coronary artery, colon, eye, testis, growth plate, articular joint; HPO suggestions: Vascular calcification, Joint destruction, Abnormality of the intestine. Exact identifiers should be verified. |
| Diagnostic pattern | Diagnosis rests on persistent age-adjusted hyperphosphatemia, inappropriately high TRP/TmP-GFR, normal renal function, normal serum calcium, and nonsuppressed calcitriol, followed by sequencing and deletion/duplication analysis of GALNT3, FGF23, and KL. Intact-versus-C-terminal FGF23 assays help distinguish hormone deficiency/cleavage from KL-mediated resistance. (farrow2011miscellaneousnoninflammatorymusculoskeletal pages 3-4, ramnitz2016phenotypicandgenotypic pages 6-10) | Normal calcium, creatinine, and alkaline phosphatase accompanied hyperphosphatemia in the NIH cohort. (ramnitz2016phenotypicandgenotypic pages 6-10) | Suggested genetic-test targets: GALNT3, FGF23, KL. Differential concepts: renal-failure-associated tumoral calcinosis, hyperparathyroidism, calcinosis universalis, dystrophic calcification, chronic osteomyelitis, and autoimmune anti-FGF23 tumoral calcinosis. |
| Medical treatment | Current off-label management combines dietary phosphate restriction, non-calcium phosphate binders such as sevelamer, and phosphaturic agents such as acetazolamide or probenecid. Evidence is limited to case reports and small uncontrolled cohorts, with inconsistent biochemical and lesion responses. (ramnitz2016phenotypicandgenotypic pages 1-6, ramnitz2016phenotypicandgenotypic pages 6-10, cherian2024clinicalcharacteristicstherapeutic pages 2-3) | Suggested dietary phosphate intake in the NIH cohort was 400–900 mg/day; one mass resolved after 13 months of combined treatment. (ramnitz2016phenotypicandgenotypic pages 6-10, ramnitz2016phenotypicandgenotypic pages 1-6) | CHEBI suggestions: phosphate—CHEBI:26020; acetazolamide, sevelamer, probenecid, and aluminum hydroxide require identifier verification. NCIT suggestions: Dietary Therapy, Pharmacotherapy, Surgical Excision; exact codes not asserted. |
| Anti-inflammatory and surgical treatment | Anakinra or canakinumab may suppress severe IL-1-mediated inflammation but does not directly correct FGF23 deficiency. Surgery is reserved for painful, infected, ulcerating, or disabling masses because incomplete excision and persistent hyperphosphatemia favor recurrence and wound morbidity. (ramnitz2016phenotypicandgenotypic pages 13-17, ramnitz2016phenotypicandgenotypic pages 1-6) | IL-1 blockade reduced CRP in two severely inflamed NIH patients; one had resolution of calcinosis cutis and surrounding inflammation, and both reported improved well-being. (ramnitz2016phenotypicandgenotypic pages 1-6) | NCIT term suggestions: Anakinra; Canakinumab; Interleukin-1 Inhibition; Surgical Excision—exact codes should be verified. |
| Epidemiology and course | Population prevalence and incidence have not been reliably estimated. Reports suggest enrichment in African and Middle Eastern families, often in association with consanguinity. Onset and expressivity vary markedly, including within families. (chakhtoura2018hyperphosphatemicfamilialtumoral pages 1-2, ito2021congenitalhyperphosphatemicconditions pages 1-2) | Onset ranges from infancy or the first decade through late adulthood; a 2023 genetically diagnosed patient developed calcinosis in her seventies. (chakhtoura2018hyperphosphatemicfamilialtumoral pages 1-2, iwasaki2023elderlyonsetcalcinosisof pages 6-6) | Orphan-disease designation appropriate; no validated sex ratio, carrier frequency, penetrance percentage, survival statistic, or population-screening program is available. |
| Animal models | **Galnt3**-null mice reproduce low circulating intact Fgf23 and hyperphosphatemia despite increased bone Fgf23 expression, but do not consistently develop overt calcific masses. **Fgf23**-null mice reproduce hyperphosphatemia, elevated calcitriol, and ectopic/vascular calcification. (farrow2011miscellaneousnoninflammatorymusculoskeletal pages 3-4) | Galnt3-null mice had approximately one-half the circulating intact Fgf23 concentration of controls; the phenotype included sex-specific growth, fertility, and bone-density effects. | Species: *Mus musculus*, NCBI Taxonomy:10090. Model types: Galnt3 knockout and Fgf23 knockout. GO suggestions: phosphate-ion homeostasis—GO:0055062; renal phosphate excretion; hormone-mediated signaling—exact additional identifiers require verification. |


*Table: Concise evidence table covering HFTC classification, genetics, biochemical and clinical phenotypes, diagnosis, management, epidemiology, and experimental models. Quantitative findings are separated from suggested ontology mappings, with uncertain mappings explicitly flagged for verification.*

## 1. Disease information

### Definition and classification

HFTC is a rare disorder of FGF23 deficiency or resistance characterized by persistent hyperphosphatemia, excessive renal tubular phosphate reabsorption, elevated or inappropriately normal 1,25-dihydroxyvitamin D [1,25(OH)₂D], and ectopic calcification. “Tumoral” describes the mass-like appearance; the deposits are not neoplastic. HFTC and HHS overlap genetically and clinically: calcific masses predominate in HFTC, whereas recurrent painful diaphyseal hyperostosis may dominate in HHS. (ramnitz2016phenotypicandgenotypic pages 1-6, ito2021congenitalhyperphosphatemicconditions pages 3-4)

**Identifiers and synonyms**

- Familial hyperphosphatemic tumoral calcinosis/hyperphosphatemic hyperostosis syndrome: **Orphanet 306661**.
- HFTC1, usually **GALNT3** related: **OMIM 211900**.
- HFTC2, **FGF23** related: **OMIM 617993; MONDO:0060714**.
- HFTC3, **KL** related: **OMIM 617994; MONDO:0060715**. (OpenTargets Search: Hyperphosphatemic familial tumoral calcinosis-FGF23,GALNT3,KL, ito2021congenitalhyperphosphatemicconditions pages 2-3)
- Common names: hyperphosphatemic familial tumoral calcinosis, familial tumoral calcinosis, hyperphosphatemic tumoral calcinosis, FTC/HHS, HFTC/HHS, and hyperostosis-hyperphosphatemia syndrome.
- A single umbrella MONDO identifier was not established in the retrieved evidence; subtype MONDO identifiers above are directly supported. A dedicated ICD-10/ICD-11 or MeSH code specific to inherited HFTC was likewise not verified; broader calcinosis or mineral-metabolism codes may be used clinically but are not disease-equivalent.

This report synthesizes **aggregated disease-level literature**, not individual EHR data. Patient-level observations are drawn from published consented cohorts and case reports.

## 2. Etiology, risk, and protective factors

### Causal factors

HFTC is primarily genetic and autosomal recessive:

1. **GALNT3 loss of function** impairs O-glycosylation and stabilization of FGF23.
2. **FGF23 loss of function** impairs synthesis, secretion, stability, or bioactivity of the phosphaturic hormone.
3. **KL loss of function** impairs Klotho-dependent FGF23 receptor signaling, producing hormone resistance. (farrow2011miscellaneousnoninflammatorymusculoskeletal pages 3-4, ito2021congenitalhyperphosphatemicconditions pages 1-2)

A rare acquired phenocopy caused by **anti-FGF23 autoantibodies** has been reported and should be considered when biochemical HFTC is present without biallelic variants in the three established genes. (ito2021congenitalhyperphosphatemicconditions pages 3-4)

### Risk and modifying factors

- **Genetic risk:** two pathogenic alleles in one causal gene; consanguinity and an affected sibling substantially increase prior probability. In a literature review covering 64 cases through 2017, 44 involved GALNT3, 19 FGF23, and one KL, making GALNT3 the most frequently reported cause. (ito2021congenitalhyperphosphatemicconditions pages 2-3)
- **Family history:** may be absent because recessive carriers are usually asymptomatic and de novo presentations can occur through unrecognized carrier mating or unusual mechanisms.
- **Environmental/lifestyle risk:** no toxin, infection, smoking, alcohol, or occupational exposure causes inherited HFTC. High dietary phosphate plausibly aggravates hyperphosphatemia, but a quantified gene–diet effect has not been established.
- **Tissue injury and comorbidity:** local pressure or trauma may influence where masses become clinically apparent. A 2023 case proposed that limited scleroderma contributed to very late calcinosis, but this is a single-patient hypothesis rather than demonstrated causation. (iwasaki2023elderlyonsetcalcinosisof pages 6-6)
- **Protective factors:** no validated protective allele is known. Dietary phosphate restriction and early biochemical control are therapeutic or tertiary-preventive measures, not proven protection against inheriting or developing the molecular disorder.
- **Modifier genes/epigenetics:** no replicated HFTC-specific modifier locus, methylation signature, or chromatin mechanism was identified. General epigenetic regulation of mineral metabolism should not be entered as HFTC-specific evidence.

## 3. Phenotypes

### Core phenotype and suggested HPO annotations

| Phenotype | Characteristics and frequency | Suggested HPO annotation |
|---|---|---|
| Hyperphosphatemia | Universal biochemical hallmark in characterized cohorts; persistent, age-adjusted elevation | **HP:0002905** |
| Increased renal phosphate reabsorption | High TRP/TmP-GFR despite hyperphosphatemia; NIH cohort TRP 96.5%, median TmP/GFR 6.5 mg/dL | Abnormal renal phosphate handling; verify exact HPO term |
| Tumoral calcinosis | Lobular periarticular masses, especially hips, elbows, and shoulders; 6/8 in one NIH cohort; severity ranges from absent to massive | Calcinosis/subcutaneous calcification; verify exact term |
| Diaphyseal hyperostosis | Episodic painful long-bone swelling, erythema, and warmth, often tibial; can resemble osteomyelitis | Hyperostosis; limb pain; bone pain |
| Restricted joint movement | Secondary to periarticular mass, pain, or joint destruction; potentially severe and progressive | Joint contracture or limitation of joint mobility |
| Systemic inflammation | Fever, elevated CRP/ESR, fatigue, anorexia; severe in 3/8 NIH subjects | **HP:0011227** elevated CRP, fever, constitutional symptoms; identifiers should be verified |
| Dental-root/pulp disease | Short thistle-shaped roots, midroot bulges, apical thinning, pulp stones or obliteration; pulp obliteration in 13/14 (93%) | Abnormal dental root; pulp calcification; short tooth roots |
| Vascular/visceral calcification | Coronary, intestinal, ocular, and testicular deposits reported; clinical frequency uncertain | Vascular calcification and organ-specific calcification terms |

The NIH cohort’s median 1,25(OH)₂D was 62 pg/mL and median calcium-phosphate product was 63.5 mg²/dL². Calcium, creatinine, and alkaline phosphatase were generally normal. (ramnitz2016phenotypicandgenotypic pages 6-10)

A dedicated dental cohort found pulp obliteration in **13/14 evaluable patients (93%)**; all ten comprehensively examined participants with GALNT3 variants had shortened thistle-shaped roots and pulp obliteration. Premolars were more severely affected than canines, molars, or incisors, and mean phosphate was 6.4 ± 1.0 mg/dL. (lee2021across‐sectionalcohort pages 4-5)

### Onset, severity, progression, and quality of life

Onset ranges from infancy to late adulthood and severity varies even among relatives with the same genotype. Calcific masses are not generally present neonatally and tend to accrue with age; reported individual onset ages include 4 and 23 years. A 2023 genetically confirmed case did not manifest clinically important calcinosis until the patient’s seventies. (chakhtoura2018hyperphosphatemicfamilialtumoral pages 1-2, ito2021congenitalhyperphosphatemicconditions pages 3-4, iwasaki2023elderlyonsetcalcinosisof pages 6-6)

Periarticular masses cause pain, reduced range of motion, impaired walking and self-care, ulceration, infection risk, and repeated surgery. Inflammatory attacks cause severe limb pain and constitutional illness. No validated HFTC-specific EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life dataset was identified.

## 4. Genetic and molecular information

### Causal genes

- **GALNT3** encodes polypeptide N-acetylgalactosaminyltransferase-3, a trans-Golgi glycosyltransferase. It O-glycosylates FGF23 near Thr178 and protects the Arg179–Ser180 cleavage region.
- **FGF23** encodes the 251-amino-acid precursor of a bone-derived phosphaturic hormone; after signal-peptide removal, the secreted product contains 227 amino acids.
- **KL** encodes α-Klotho, the obligate coreceptor that permits high-affinity FGF23 signaling through principally FGFR1c in kidney. (farrow2011miscellaneousnoninflammatorymusculoskeletal pages 3-4, ito2021congenitalhyperphosphatemicconditions pages 1-2)

Open Targets independently supports disease associations for GALNT3, FGF23, and KL, linked to primary literature including **PMID 15133511** for GALNT3, **PMIDs 15590700 and 16151858** for FGF23, and **PMID 17710231** for KL. (OpenTargets Search: Hyperphosphatemic familial tumoral calcinosis-FGF23,GALNT3,KL)

### Pathogenic variants

Reported germline variants include missense, nonsense, frameshift, splice-site, and small insertion/deletion alleles. FGF23 examples include p.His41Gln, p.Gln54Lys, p.Ser71Gly, p.Met96Thr, p.Gly123Trp, p.Ser129Pro, and p.Ser129Phe; the established KL example is p.His193Arg. The FGF23 p.Ser71Gly mutant can be retained in the Golgi, with preferential secretion of C-terminal fragments. (ito2021congenitalhyperphosphatemicconditions pages 3-4, farrow2011miscellaneousnoninflammatorymusculoskeletal pages 3-4)

Recent examples include homozygous **GALNT3 c.1524+1G>A** in three siblings reported in 2024 and a novel late frameshift in the lectin domain reported in an elderly patient in 2023. These examples broaden variant and age-of-presentation spectra but do not establish new genes or treatment standards. (iwasaki2023elderlyonsetcalcinosisof pages 6-6, alghubishi2024type1hyperphosphatemic pages 5-5)

Variants are constitutional/germline, not somatic drivers. Most disease alleles are functionally loss-of-function. Population allele frequencies must be retrieved variant-by-variant from a current gnomAD release; the evidence set does not support assigning a universal frequency. Likewise, each variant requires contemporary ACMG/AMP classification using ClinVar, segregation, population, and functional data rather than assuming pathogenicity from gene membership.

No recurrent chromosomal abnormality is established. Uniparental disomy can theoretically unmask a recessive GALNT3 allele, but CMA, karyotyping, and FISH are not routine first-line tests. No HFTC-specific epigenetic biomarker is validated.

## 5. Environmental information

There is no evidence that pollution, radiation, occupational toxins, smoking, alcohol, or an infectious organism initiates familial HFTC. Dietary phosphate influences the biochemical substrate burden and is therefore clinically actionable. Local mechanical stress may help explain periarticular localization, while tissue injury, ulceration, and secondary infection can worsen established lesions. Rheumatologic comorbidity as a modifier is currently supported only by isolated observation. (cherian2024clinicalcharacteristicstherapeutic pages 2-3, iwasaki2023elderlyonsetcalcinosisof pages 6-6)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic GALNT3 or FGF23 loss-of-function variants lead to** deficient secretion or excessive proteolytic cleavage of intact bioactive FGF23; alternatively, **biallelic KL variants lead to** resistance to intact FGF23. (farrow2011miscellaneousnoninflammatorymusculoskeletal pages 3-4, ito2021congenitalhyperphosphatemicconditions pages 1-2)
2. **Deficient FGF23–Klotho–FGFR1c signaling leads to** inadequate downregulation of renal proximal-tubular sodium-phosphate cotransporters NaPi-IIa/NaPi-IIc.
3. **Persistent transporter activity leads to** excessive tubular phosphate reabsorption and hyperphosphatemia.
4. **Loss of FGF23 action also leads to** failure to suppress renal calcitriol production, resulting in elevated or inappropriately normal 1,25(OH)₂D.
5. **Calcitriol activity leads to** increased intestinal calcium and phosphate absorption, further increasing the calcium-phosphate product.
6. **High extracellular phosphate and calcium-phosphate product lead to** precipitation of calcium-phosphate material in periarticular soft tissue, vessels, dental pulp, and viscera; the exact site-selection mechanism remains partly inferred. (ito2021congenitalhyperphosphatemicconditions pages 3-4, farrow2011miscellaneousnoninflammatorymusculoskeletal pages 3-4)
7. **Crystal deposition and tissue injury lead to** macrophage-rich foreign-body inflammation, chronic inflammation, and sometimes heterotopic ossification.
8. **Mass effect and inflammation lead to** pain, ulceration, reduced joint movement, infection risk, and tissue or joint destruction. Independently, abnormal skeletal phosphate/FGF23 biology **leads to** episodic diaphyseal cortical hyperostosis and pain. (ramnitz2016phenotypicandgenotypic pages 13-17, ramnitz2016phenotypicandgenotypic pages 1-6)

### Cellular and ontology annotations

Upstream cell types include osteocytes/osteoblast-lineage cells producing FGF23 (**CL: osteocyte and osteoblast terms should be ontology-verified**) and renal proximal-tubule epithelial cells responding through Klotho–FGFR signaling. Downstream lesions contain connective-tissue cells, macrophages, foreign-body giant cells, and in some cases osteoblast-like cells forming heterotopic bone.

Suggested GO concepts include **phosphate-ion homeostasis (GO:0055062)**, **inflammatory response (GO:0006954)**, hormone-mediated signaling, renal phosphate excretion, O-linked glycosylation, and biomineral tissue development (**GO:0031214**). Relevant compartments include the trans-Golgi network for GalNAc-T3 and the plasma membrane receptor complex for Klotho/FGFR1c; exact GO cellular-component identifiers should be verified before production use.

Histology in four NIH subjects showed ectopic calcification with chronic inflammation, and one showed mature lamellar heterotopic bone. Foamy macrophages and chronic inflammatory cells support a downstream innate immune response rather than primary autoimmunity in genetic HFTC. (ramnitz2016phenotypicandgenotypic pages 13-17, ramnitz2016phenotypicandgenotypic pages 1-6)

No reproducible HFTC-specific single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, or integrated multi-omics signature was identified. This is a major research gap.

## 7. Anatomical structures affected

Primary sites are periarticular skin, subcutaneous tissue, fascia, tendons, and connective tissue near the **hip, elbow, and shoulder**; knees, hands, and feet also occur. Hyperostosis principally involves cortical diaphyses of long bones, especially tibiae. Dental disease involves root cementum, pulp, pulp cavity, and odontoblast architecture. (ito2021congenitalhyperphosphatemicconditions pages 3-4, lee2021across‐sectionalcohort pages 4-5)

Secondary or less frequent sites include coronary and other vessels, colonic submucosa, eye, and testis. One NIH subject had complete shoulder-joint destruction and another had ulnar growth-plate destruction. Two of five evaluated subjects had coronary Agatston scores above the 95th percentile, although age and conventional cardiovascular risks confounded attribution. Lesions may be unilateral, bilateral, multifocal, and asymmetric; no fixed lateralization exists. (ramnitz2016phenotypicandgenotypic pages 13-17)

Suggested UBERON mappings include skin, subcutaneous tissue, hip joint, elbow joint, shoulder joint, tibia, coronary artery, colon, eye, testis, tooth pulp, and growth plate. Exact UBERON accession numbers require terminology-service validation.

## 8. Temporal development

HFTC is genetically present from conception but often clinically silent in infancy. The course is chronic and lifelong, with variable, episodic inflammatory attacks and progressive or recurrent calcific masses. Patients may have biochemical disease before palpable lesions; in the NIH cohort, two siblings initially lacked physical calcinosis and one later developed an elbow lesion. (ramnitz2016phenotypicandgenotypic pages 6-10)

No formal stages exist. A practical course model is: (1) biochemical hyperphosphatemia; (2) early dental or episodic hyperostotic disease; (3) localized tumoral calcinosis; and (4) multifocal disabling, ulcerating, vascular, or visceral disease. This is a clinical framework, not a validated staging system.

Spontaneous regression is reported but unpredictable. Treatment-associated complete resolution of one mass occurred after 13 months in the NIH cohort. The ideal preventive window is probably before large deposits form, but prospective evidence proving that early phosphate control prevents lesions is absent. (ramnitz2016phenotypicandgenotypic pages 1-6)

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two heterozygous parents, each pregnancy conventionally has a 25% probability of an affected child, 50% of an unaffected carrier, and 25% of a noncarrier. Expressivity is markedly variable; penetrance of biochemical hyperphosphatemia appears high in biallelic disease, whereas penetrance and timing of tumoral calcinosis are incomplete and age dependent. Anticipation is not known. Germline mosaicism has not emerged as a characteristic mechanism.

No reliable prevalence, incidence, carrier frequency, sex ratio, or survival estimate exists. Sixty-four genetically characterized cases were summarized through 2017, underscoring extreme rarity rather than defining population prevalence. Reports are enriched in African and Middle Eastern families and consanguineous pedigrees, but HFTC occurs worldwide. (ito2021congenitalhyperphosphatemicconditions pages 1-2, ito2021congenitalhyperphosphatemicconditions pages 2-3)

## 10. Diagnostics

### Recommended diagnostic workflow

1. Confirm persistent, age-adjusted fasting **serum phosphate elevation**.
2. Measure calcium, creatinine/eGFR, alkaline phosphatase, PTH, 25-hydroxyvitamin D, and 1,25(OH)₂D.
3. Calculate TRP and **TmP/GFR** from paired serum/urine phosphate and creatinine. HFTC shows inappropriate phosphate conservation despite normal kidney function.
4. Measure both **intact FGF23** and **C-terminal FGF23** where available. GALNT3/FGF23 disease generally produces low or inappropriately normal intact hormone with high C-terminal fragments; KL disease produces high intact FGF23 because of resistance. (farrow2011miscellaneousnoninflammatorymusculoskeletal pages 3-4, ramnitz2016phenotypicandgenotypic pages 6-10)
5. Image symptomatic sites using plain radiography; CT best defines calcific burden and surgical anatomy, while MRI can characterize inflammation but may misleadingly resemble osteomyelitis.
6. Sequence **GALNT3, FGF23, and KL**, preferably using a mineral-metabolism/calcification panel with deletion–duplication analysis. WES or WGS is appropriate if panel testing is negative or phenotype is atypical.
7. If no causal genotype is found, consider anti-FGF23 autoantibodies and reassess acquired causes.

Biopsy is unnecessary for classic biochemistry and imaging but may be required if malignancy, infection, or another calcifying disorder cannot be excluded. Expected pathology is amorphous calcium-phosphate material with macrophages/giant cells, chronic inflammation, fibrosis, and sometimes heterotopic bone. (ramnitz2016phenotypicandgenotypic pages 13-17)

CMA, karyotyping, FISH, mitochondrial sequencing, repeat-expansion testing, liquid biopsy, and routine diagnostic omics have no established role. Cascade biochemical and targeted genetic testing is appropriate for relatives; population or newborn screening is not established.

### Differential diagnosis

Important alternatives are chronic kidney disease with secondary tumoral calcinosis, hyperparathyroidism, excess phosphate administration, vitamin-D intoxication, pseudohypoparathyroidism, dystrophic calcification from connective-tissue disease, calcinosis universalis, calcific tendinopathy, synovial osteochondromatosis, gout, malignancy, bacterial osteomyelitis, and chronic recurrent multifocal osteomyelitis. Normal renal function, high TmP/GFR, nonsuppressed calcitriol, and the characteristic FGF23 assay/genetic pattern distinguish HFTC. HFTC-associated hyperostosis can closely mimic osteomyelitis clinically and on MRI. (ito2021congenitalhyperphosphatemicconditions pages 3-4, alghubishi2024type1hyperphosphatemic pages 5-5)

## 11. Outcome and prognosis

Life expectancy, disease-specific mortality, and five- or ten-year survival have not been quantified. Many patients survive into adulthood, but morbidity can be profound. Major outcomes include chronic pain, impaired mobility, joint destruction, ulceration, secondary infection, disfiguring masses, repeated operations, dental complications, and possible vascular or visceral injury. (ramnitz2016phenotypicandgenotypic pages 13-17)

Prognostic factors are incompletely established. Persistent phosphate elevation, high calcium-phosphate product, extensive baseline lesion burden, poor adherence, and systemic inflammation are clinically concerning, but no validated prognostic model exists. Genotype does not reliably predict severity, and substantial intrafamilial variability argues for other modifiers. Long-term multidisciplinary surveillance should include function, skin integrity, inflammation, dental health, renal function, and individualized cardiovascular assessment.

## 12. Treatment

No FDA/EMA-approved disease-specific therapy or consensus algorithm exists. Expert management seeks to lower phosphate/calcium-phosphate product, suppress inflammatory complications, preserve function, and avoid surgical morbidity. The 2020 authoritative review concluded that efficacy evidence was limited to case reports and small cohorts and that no clearly effective therapy had been identified; this remains broadly consistent with the 2024 systematic-review evidence base. (ramnitz2016phenotypicandgenotypic pages 1-6, cherian2024clinicalcharacteristicstherapeutic pages 2-3)

### Phosphate-directed treatment

- **Low-phosphate diet:** often 400–900 mg/day in the NIH cohort, ideally planned by a metabolic dietitian to avoid malnutrition.
- **Sevelamer:** non-calcium intestinal phosphate binder; avoid calcium-containing binders when possible because they may increase calcium-phosphate substrate.
- **Aluminum hydroxide:** effective binder but unsuitable for prolonged indiscriminate use because of aluminum toxicity; used in two NIH subjects.
- **Acetazolamide:** carbonic-anhydrase inhibitor inducing bicarbonaturia and phosphaturia. Monitor bicarbonate, potassium, renal function, and nephrolithiasis risk; metabolic acidosis is a recognized concern.
- **Probenecid:** promotes phosphaturia but has important drug interactions, including increased exposure to penicillins, cephalosporins, and trimethoprim-sulfamethoxazole.
- **Nicotinamide:** did not add clear benefit in the NIH cohort. (ramnitz2016phenotypicandgenotypic pages 13-17, ramnitz2016phenotypicandgenotypic pages 6-10)

Responses are inconsistent. In the NIH cohort, one mass completely resolved after 13 months of combined medical treatment, but individualized regimens, adherence differences, referral bias, and short follow-up preclude response-rate estimates. (ramnitz2016phenotypicandgenotypic pages 1-6)

### Anti-inflammatory therapy

NSAIDs may treat mild attacks. For severe systemic inflammation, **anakinra** or **canakinumab** has reduced CRP and improved constitutional symptoms in isolated patients. In two NIH subjects, IL-1 blockade lowered inflammatory markers; one had resolution of calcinosis cutis and surrounding inflammation, and both reported improved energy, appetite, and well-being. These agents treat downstream inflammation and do not restore FGF23 activity. (ramnitz2016phenotypicandgenotypic pages 13-17, ramnitz2016phenotypicandgenotypic pages 1-6)

### Surgery and supportive care

Complete excision may be considered for severe pain, ulceration, recurrent infection, neurovascular compromise, or major functional restriction. Surgery is a last resort because persistent hyperphosphatemia, incomplete excision, wound complications, and recurrence are common concerns. Physical/occupational therapy, wound care, analgesia, dental surveillance, and psychosocial support are appropriate.

Suggested NCIt intervention concepts are dietary therapy, phosphate-binding agent therapy, carbonic-anhydrase inhibition, anakinra, canakinumab, IL-1 inhibition, analgesic therapy, physical therapy, wound care, and surgical excision; exact NCIt codes should be validated before database loading.

### Advanced and experimental therapy

Recombinant or long-acting FGF23 replacement is mechanistically attractive for GALNT3/FGF23 deficiency but remains experimental. Gene replacement, CRISPR editing, RNA therapy, and cell therapy have no established human implementation. **Burosumab is an anti-FGF23 antibody and is mechanistically inappropriate—and potentially hazardous—in an FGF23-deficient/resistant hyperphosphatemic disorder.** No disease-specific interventional ClinicalTrials.gov study was identified. The broad NIH observational natural-history protocol **NCT00024804** includes bone/mineral disorders but is not an HFTC treatment trial.

## 13. Prevention

Primary prevention of a recessive genotype is limited to informed reproductive choice. Genetic counseling should address parental carrier testing, cascade testing, prenatal diagnosis, and preimplantation genetic testing when familial pathogenic variants are known. There is no vaccine, infectious prophylaxis, or population-screening program.

Secondary prevention consists of early recognition in siblings and relatives using serum phosphate, renal phosphate handling, and targeted genetic testing. Dental-root changes may appear early and have high penetrance, making dental radiographs a useful diagnostic clue. (lee2021across‐sectionalcohort pages 4-5)

Tertiary prevention includes dietary/pharmacological phosphate control, monitoring calcium-phosphate product and bicarbonate, avoiding unnecessary calcium/phosphate supplements, prompt treatment of inflammation or ulcer infection, dental care, skin protection, and minimizing repetitive pressure over lesions. Evidence that these measures prevent all calcification remains observational.

## 14. Other species and natural disease

No well-established naturally occurring veterinary counterpart was identified in the retrieved literature. The pathway is evolutionarily conserved across mammals, but veterinary “tumoral calcinosis” can have different etiologies and should not automatically be annotated as orthologous HFTC. The disorder is not infectious, transmissible, or zoonotic.

Relevant orthologs are **Galnt3, Fgf23, and Kl** in *Mus musculus* (**NCBI Taxonomy 10090**). Exact NCBI Gene IDs and any OMIA/VBO entries should be verified directly before knowledge-base ingestion.

## 15. Model organisms

### Mouse models

- **Galnt3-knockout mouse:** reproduces low circulating intact Fgf23 and hyperphosphatemia despite increased bone Fgf23 expression. Circulating intact Fgf23 was approximately half that of controls, with increased C-terminal fragments. Mice did not consistently develop overt calcific masses, limiting fidelity to severe human HFTC; sex-specific growth retardation, infertility, and increased bone density were also reported.
- **Fgf23-null mouse:** reproduces hyperphosphatemia, elevated calcitriol, and ectopic/vascular calcification and strongly supports the causal endocrine pathway.
- **Klotho-deficient models:** reproduce deficient FGF23 signaling and mineral abnormalities and have been used to evaluate calcification-modifying strategies, although their broader premature-aging phenotype limits direct clinical translation. (ramnitz2016phenotypicandgenotypic pages 13-17, farrow2011miscellaneousnoninflammatorymusculoskeletal pages 3-4)

These are genetic mammalian knockout models useful for studying phosphate sensing, FGF23 processing, renal transport, calcification, and candidate therapies. No validated HFTC organoid, patient-iPSC platform, zebrafish model, or humanized model was identified.

## Recent developments, 2023–2024

1. **2024 systematic review:** Cherian et al., *Calcified Tissue International* 115:215–228, published July 2024, DOI [10.1007/s00223-024-01247-8](https://doi.org/10.1007/s00223-024-01247-8), systematically assessed clinical characteristics, therapeutic approaches, and lesion outcomes. Its underlying literature remains dominated by case reports and case series rather than controlled trials. (cherian2024clinicalcharacteristicstherapeutic pages 2-3)
2. **Very-late onset:** Iwasaki, published online October 3, 2023, DOI [10.1530/edm-23-0071](https://doi.org/10.1530/edm-23-0071), described genetically diagnosed elderly-onset disease and argued that HFTC should remain in the differential for unexplained hyperphosphatemia or ectopic calcinosis even in older adults. (iwasaki2023elderlyonsetcalcinosisof pages 6-6)
3. **Phenotypic and allelic expansion:** 2024 reports described recurrent osteomyelitis-like presentations, a three-sibling family with homozygous GALNT3 c.1524+1G>A, and additional novel GALNT3 variants. These reports reinforce use of WES/WGS in atypical cases but do not alter the three-gene causal model. (alghubishi2024type1hyperphosphatemic pages 5-5)
4. **Current expert interpretation:** recent work emphasizes phenotype diversity, dental and vascular surveillance, inflammatory biology, and the inadequacy of current phosphate-lowering therapy. The major unmet needs are prospective natural-history data, standardized lesion imaging and outcomes, and FGF23-replacement therapy.

## Exact supporting abstract quotations

Short quotations retained from accessible abstracts include:

- HFTC is described as a “**rare and disabling disorder of fibroblast growth factor 23 (FGF23) deficiency or resistance**,” and periarticular calcinosis as “**the primary cause of disability**.” (ramnitz2016phenotypicandgenotypic pages 1-6)
- The dental cohort concluded that its study “**defines the spectrum and confirms the high penetrance of dental features in HFTC**.” (lee2021across‐sectionalcohort pages 4-5)
- The Galnt3 model supplied in-vivo evidence that impaired Galnt3 causes “**decreased circulating Fgf23 and hyperphosphatemia, despite increased Fgf23 expression**.” (farrow2011miscellaneousnoninflammatorymusculoskeletal pages 3-4)

## Evidence limitations and knowledge-base cautions

HFTC literature is exceptionally sparse. Percentages from cohorts of 8–17 individuals should not be treated as population frequencies. Prevalence, incidence, sex ratio, penetrance percentages, mortality, life expectancy, carrier frequency, standardized quality-of-life effects, pharmacogenomics, validated biomarkers of progression, and treatment-response rates remain unknown. Most 2023–2024 publications are systematic reviews or single-family reports rather than prospective studies. Ontology terms marked “suggested” should undergo release-specific validation against HPO, GO, CL, UBERON, CHEBI, NCIt, and MONDO before production loading.

References

1. (ramnitz2016phenotypicandgenotypic pages 1-6): Mary Scott Ramnitz, Pravitt Gourh, Raphaela Goldbach-Mansky, Felasfa Wodajo, Shoji Ichikawa, Michael J Econs, Kenneth E White, Alfredo Molinolo, Marcus Y Chen, Theo Heller, Jaydira Del Rivero, Patricia Seo-Mayer, Bita Arabshahi, Malaka B Jackson, Sarah Hatab, Edward McCarthy, Lori C Guthrie, Beth A Brillante, Rachel I Gafni, and Michael T Collins. Phenotypic and genotypic characterization and treatment of a cohort with familial tumoral calcinosis/hyperostosis‐hyperphosphatemia syndrome. Journal of Bone and Mineral Research, 31:1845-1854, Oct 2016. URL: https://doi.org/10.1002/jbmr.2870, doi:10.1002/jbmr.2870. This article has 109 citations and is from a highest quality peer-reviewed journal.

2. (ito2021congenitalhyperphosphatemicconditions pages 1-2): Nobuaki Ito and Seiji Fukumoto. Congenital hyperphosphatemic conditions caused by the deficient activity of fgf23. Calcified Tissue International, 108:104-115, Jan 2021. URL: https://doi.org/10.1007/s00223-020-00659-6, doi:10.1007/s00223-020-00659-6. This article has 29 citations and is from a peer-reviewed journal.

3. (OpenTargets Search: Hyperphosphatemic familial tumoral calcinosis-FGF23,GALNT3,KL): Open Targets Query (Hyperphosphatemic familial tumoral calcinosis-FGF23,GALNT3,KL, 9 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (ito2021congenitalhyperphosphatemicconditions pages 2-3): Nobuaki Ito and Seiji Fukumoto. Congenital hyperphosphatemic conditions caused by the deficient activity of fgf23. Calcified Tissue International, 108:104-115, Jan 2021. URL: https://doi.org/10.1007/s00223-020-00659-6, doi:10.1007/s00223-020-00659-6. This article has 29 citations and is from a peer-reviewed journal.

5. (farrow2011miscellaneousnoninflammatorymusculoskeletal pages 3-4): Emily G. Farrow, Erik A. Imel, and Kenneth E. White. Miscellaneous non-inflammatory musculoskeletal conditions. hyperphosphatemic familial tumoral calcinosis (fgf23, galnt3 and αklotho). Best practice & research. Clinical rheumatology, 25 5:735-47, Oct 2011. URL: https://doi.org/10.1016/j.berh.2011.10.020, doi:10.1016/j.berh.2011.10.020. This article has 78 citations.

6. (ito2021congenitalhyperphosphatemicconditions pages 3-4): Nobuaki Ito and Seiji Fukumoto. Congenital hyperphosphatemic conditions caused by the deficient activity of fgf23. Calcified Tissue International, 108:104-115, Jan 2021. URL: https://doi.org/10.1007/s00223-020-00659-6, doi:10.1007/s00223-020-00659-6. This article has 29 citations and is from a peer-reviewed journal.

7. (ramnitz2016phenotypicandgenotypic pages 6-10): Mary Scott Ramnitz, Pravitt Gourh, Raphaela Goldbach-Mansky, Felasfa Wodajo, Shoji Ichikawa, Michael J Econs, Kenneth E White, Alfredo Molinolo, Marcus Y Chen, Theo Heller, Jaydira Del Rivero, Patricia Seo-Mayer, Bita Arabshahi, Malaka B Jackson, Sarah Hatab, Edward McCarthy, Lori C Guthrie, Beth A Brillante, Rachel I Gafni, and Michael T Collins. Phenotypic and genotypic characterization and treatment of a cohort with familial tumoral calcinosis/hyperostosis‐hyperphosphatemia syndrome. Journal of Bone and Mineral Research, 31:1845-1854, Oct 2016. URL: https://doi.org/10.1002/jbmr.2870, doi:10.1002/jbmr.2870. This article has 109 citations and is from a highest quality peer-reviewed journal.

8. (cherian2024clinicalcharacteristicstherapeutic pages 2-3): Kripa Elizabeth Cherian, Jacob Cherian, Dharmasivam Vinodhini, and Thomas Vizhalil Paul. Clinical characteristics, therapeutic options, and outcomes in hyperphosphatemic tumoral calcinosis: a systematic review. Calcified tissue international, 115:215-228, Jul 2024. URL: https://doi.org/10.1007/s00223-024-01247-8, doi:10.1007/s00223-024-01247-8. This article has 6 citations and is from a peer-reviewed journal.

9. (ramnitz2016phenotypicandgenotypic pages 13-17): Mary Scott Ramnitz, Pravitt Gourh, Raphaela Goldbach-Mansky, Felasfa Wodajo, Shoji Ichikawa, Michael J Econs, Kenneth E White, Alfredo Molinolo, Marcus Y Chen, Theo Heller, Jaydira Del Rivero, Patricia Seo-Mayer, Bita Arabshahi, Malaka B Jackson, Sarah Hatab, Edward McCarthy, Lori C Guthrie, Beth A Brillante, Rachel I Gafni, and Michael T Collins. Phenotypic and genotypic characterization and treatment of a cohort with familial tumoral calcinosis/hyperostosis‐hyperphosphatemia syndrome. Journal of Bone and Mineral Research, 31:1845-1854, Oct 2016. URL: https://doi.org/10.1002/jbmr.2870, doi:10.1002/jbmr.2870. This article has 109 citations and is from a highest quality peer-reviewed journal.

10. (lee2021across‐sectionalcohort pages 4-5): Alisa E Lee, Emily Y Chu, Pamela J Gardner, Olivier Duverger, Amanda Saikali, Sean K Wang, Rachel I Gafni, Iris R Hartley, Kelly G Ten Hagen, Martha J Somerman, and Michael T Collins. A cross‐sectional cohort study of the effects of <scp>fgf23</scp> deficiency and hyperphosphatemia on dental structures in hyperphosphatemic familial tumoral calcinosis. JBMR Plus, Mar 2021. URL: https://doi.org/10.1002/jbm4.10470, doi:10.1002/jbm4.10470. This article has 18 citations and is from a peer-reviewed journal.

11. (chakhtoura2018hyperphosphatemicfamilialtumoral pages 1-2): M. Chakhtoura, M.S. Ramnitz, N. Khoury, G. Nemer, N. Shabb, A. Abchee, A. Berberi, M. Hourani, M. Collins, S. Ichikawa, and G. El Hajj Fuleihan. Hyperphosphatemic familial tumoral calcinosis secondary to fibroblast growth factor 23 (fgf23) mutation: a report of two affected families and review of the literature. Osteoporosis International, 29:1987-2009, Jun 2018. URL: https://doi.org/10.1007/s00198-018-4574-x, doi:10.1007/s00198-018-4574-x. This article has 22 citations and is from a domain leading peer-reviewed journal.

12. (iwasaki2023elderlyonsetcalcinosisof pages 6-6): Hiroaki Iwasaki. Elderly-onset calcinosis of hyperphosphataemic familial tumoural calcinosis/hyperostosis-hyperphosphataemia syndrome: the role of comorbid scleroderma. Endocrinology, Diabetes & Metabolism Case Reports, Oct 2023. URL: https://doi.org/10.1530/edm-23-0071, doi:10.1530/edm-23-0071. This article has 1 citations and is from a peer-reviewed journal.

13. (alghubishi2024type1hyperphosphatemic pages 5-5): Somayah A Alghubishi, Eman J Ghazwani, Sami E Abdelmogeit, and Khalid Alzubair. Type 1 hyperphosphatemic familial tumoral calcinosis associated with a homozygous variant mutation in the galnt3 gene. Oct 2024. URL: https://doi.org/10.7759/cureus.71390, doi:10.7759/cureus.71390. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](Hyperphosphatemic_Familial_Tumoral_Calcinosis-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 13 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 5 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002905` (2 mentions) - the report calls it "Universal biochemical hallmark in characterized cohorts; persistent, age-adjusted elevation"; HP calls it **Hyperphosphatemia**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Orphanet`, `OMIM`, `Taxonomy`.