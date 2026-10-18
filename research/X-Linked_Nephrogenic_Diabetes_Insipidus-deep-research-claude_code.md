---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-10T17:42:29.069704'
end_time: '2026-09-10T17:49:38.838828'
duration_seconds: 429.77
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: X-Linked Nephrogenic Diabetes Insipidus
  mondo_id: MONDO:0010581
  category: ''
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 27
  num_turns: 35
  total_cost_usd: 2.0998776
  session_id: 0ecd1216-33cc-58da-968d-9ba73b5b4eb1
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 1
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 7
  off_topic: 1
  off_topic_references:
  - PMC:PMC11095762
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 18
  verified: 17
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 5
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** X-Linked Nephrogenic Diabetes Insipidus
- **MONDO ID:** MONDO:0010581 (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **X-Linked Nephrogenic Diabetes Insipidus** covering all of the
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

# X-Linked Nephrogenic Diabetes Insipidus (NDI1, AVPR2-Related): Comprehensive Research Report

**Target disease:** X-Linked Nephrogenic Diabetes Insipidus
**Key identifiers:** OMIM #304800 (NDI1); Gene OMIM *300538 (AVPR2); MONDO:0010581; Orphanet ORPHA222; HGNC:897 (AVPR2); Gene location Xq28
**Note on ontology terms:** HPO/GO/CL/UBERON/CHEBI/NCIT CURIEs suggested below are research leads compiled from general nomenclature and search-engine synthesis, **not independently verified against OLS/OAK in this session**. Per this repository's ontology-term discipline, treat every ID below as unconfirmed until checked against a live adapter before any KB binding.

---

## 1. Disease Information

X-linked nephrogenic diabetes insipidus (X-NDI, NDI1) is a hereditary disorder of water homeostasis caused by hemizygous loss-of-function variants in **AVPR2**, the gene encoding the renal vasopressin V2 receptor (Xq28). Affected kidneys are structurally normal but insensitive to circulating arginine vasopressin (AVP), so the collecting duct cannot insert aquaporin-2 (AQP2) water channels into the apical membrane. The result is massive, dilute polyuria, compensatory polydipsia, and risk of life-threatening hypernatremic dehydration, typically from birth.

About 90% of hereditary congenital NDI cases are X-linked (AVPR2); the remaining ~10% are autosomal (AQP2-related, OMIM #125800, both dominant ~9% and recessive ~1% of the inherited total) (search synthesis of PMC articles, this session). NDI must be distinguished from far more common **acquired** NDI (lithium, hypercalcemia, hypokalemia, obstructive uropathy) and from central diabetes insipidus and primary polydipsia, which share the polyuria-polydipsia phenotype but have different mechanisms and treatments.

**Key identifiers:**
- OMIM #304800 — DIABETES INSIPIDUS, NEPHROGENIC, 1, X-LINKED; NDI1 ([omim.org/entry/304800](https://omim.org/entry/304800))
- OMIM *300538 — ARGININE VASOPRESSIN RECEPTOR 2; AVPR2
- MONDO:0010581 (per search synthesis; verify before KB use)
- Related: OMIM #125800 (NDI2, autosomal, AQP2) and OMIM *107777 (AQP2 gene) — the genocopy to distinguish from NDI1
- Orphanet: "Nephrogenic diabetes insipidus" (X-linked form as a subtype)
- ICD-10: N25.1 (Nephrogenic diabetes insipidus)

**Synonyms:** Vasopressin-resistant diabetes insipidus; X-linked recessive nephrogenic diabetes insipidus; congenital NDI (X-linked form); AVPR2-related NDI; DI, nephrogenic, X-linked.

**Evidence basis:** This report draws on aggregated disease-level resources (OMIM, GeneReviews, Orphanet-type structured sources) and primary literature — case series, pediatric cohort studies, and functional/mechanistic studies — rather than individual unpublished EHR data.

---

## 2. Etiology

### Disease causal factor
The sole cause of X-NDI (NDI1) is a **hemizygous loss-of-function pathogenic variant in AVPR2** (Xq28), encoding the V2 vasopressin receptor expressed on the basolateral membrane of renal collecting-duct principal cells. Over 200 distinct disease-causing AVPR2 variants have been published — missense, nonsense, small insertions/deletions, large deletions, and complex rearrangements (search synthesis, this session, corroborating GeneReviews NBK1177/PMID:20301356).

### Genetic risk factors
- **Causal variant class:** hemizygous AVPR2 variant in a male, or — less commonly — a heterozygous variant in a manifesting female carrier.
- **Partial-NDI variants:** at least 18 AVPR2 variants (e.g., p.Asp85Asn, p.Val88Met, p.Asn317Lys) produce a **partial** phenotype with later onset and residual DDAVP responsiveness, via mechanisms such as reduced (but not absent) surface expression or impaired G-protein coupling rather than complete intracellular retention (GeneReviews NBK1177/PMID:20301356).
- **Modifier:** degree of X-inactivation skewing in heterozygous females is the principal modifier of female phenotype severity (see below).
- **Founder variants:** regional founder effects elevate local incidence — see Epidemiology (§9).

### Environmental risk factors
There are no known environmental causal or risk factors for the X-linked *hereditary* form — it is a fully penetrant monogenic disorder in hemizygous males. (Environmental/acquired causes of NDI — lithium, hypercalcemia, hypokalemia, obstructive uropathy — are a mechanistically related but etiologically distinct secondary phenomenon; see §5 and §6.) Sex is itself the principal "risk factor": because AVPR2 is X-linked, males are at far higher risk of a full, early-onset phenotype than females.

### Protective factors
No genetic or environmental protective factor against the X-linked inherited form is described in the literature surveyed. The nearest analogue is **favorable X-inactivation skewing** in a female carrier, which can render her phenotypically normal rather than a "protective" factor in the population-genetics sense.

### Gene-environment interaction
The clearest gene-environment interaction is with **water access**: the AVPR2 defect is unmasked and made dangerous specifically when free water intake is restricted (illness, vomiting, reduced access in infancy, anesthesia/surgery, hot weather) — each of these is a described precipitant of acute hypernatremic crisis in case reports reviewed this session (e.g., Capasso et al., natural-history case report, PMID:39644399). There is no described interaction with diet, toxins, or infection altering the AVPR2 genotype-phenotype relationship beyond the acquired-NDI mechanisms listed in §5, which can compound the inherited defect (e.g., superimposed lithium exposure in an AVPR2 hemizygote, not directly documented but mechanistically plausible from the independent acquired-NDI literature).

---

## 3. Phenotypes

### Phenotype type and characteristics
The cardinal phenotype triad is **polyuria, polydipsia, and failure to thrive**, present from birth but typically recognized once nonspecific infant symptoms prompt laboratory evaluation.

| Phenotype | Type | Onset | Frequency / notes | Suggested HPO term (unverified) |
|---|---|---|---|---|
| Polyuria (often >10–20 L/day in adults; median 10.0 mL/kg/h in one pediatric cohort) | Clinical sign / lab | Birth–infancy | Universal | HP:0000103 Polyuria |
| Polydipsia (compensatory) | Symptom | Infancy onward | Universal (in verbal children/adults) | HP:0001959 (per search synthesis; verify — commonly cited for Polydipsia) |
| Hypernatremia (median 160.5 mmol/L in one cohort at presentation) | Lab abnormality | Neonatal/infancy crisis | Common at diagnosis | HP:0003228 Hypernatremia (verify) |
| Hyposthenuria / low urine osmolality, failure to concentrate urine after DDAVP | Lab abnormality | From birth | Universal, diagnostic | — |
| Poor feeding, irritability, vomiting | Symptom | First days–weeks of life | Common presenting complaint | HP:0011968 Feeding difficulties (verify) |
| Failure to thrive / growth retardation | Physical sign | Infancy–childhood | 70–71% below −2 SD for weight/height at initial treatment in a 66-subject cohort (PMID:32039113) | HP:0001508 Failure to thrive |
| Fever (unexplained) | Symptom | Infancy | Recurrent, noted in multiple case series | HP:0001945 Fever (verify) |
| Hydronephrosis / hydroureter / megacystis (secondary urinary tract dilatation from chronic high urine flow and bladder overdistension) | Structural/radiologic | Childhood–adulthood, progressive if untreated | 37% urologic complications in pediatric cohort (PMID:32039113); severe in untreated adults (PMID:39644399) | HP:0000126 Hydronephrosis |
| Nocturia / nocturnal enuresis | Symptom | Childhood | 44% at final follow-up in pediatric cohort | HP:0000017 Nocturia |
| Chronic kidney disease (secondary, from chronic obstructive uropathy) | Lab/clinical | Later childhood–adulthood | 23–30% CKD stage ≥2 in pediatric cohort (PMID:32039113); eGFR 25 mL/min/1.73m² in an untreated 58-year-old (PMID:39644399) | HP:0012622 Chronic kidney disease |
| Neurodevelopmental disorder (intellectual disability, ASD, language delay) | Behavioral/cognitive | Variable | 75% (6/8) in one long-term pediatric follow-up cohort (PMID:40922895) — notably higher than the oft-quoted "normal intelligence with early treatment" figure, reflecting either ascertainment in a severe-case series, subclinical dehydration episodes, or both | HP:0001249 Intellectual disability |
| Secondary hyperparathyroidism | Lab | Adulthood (untreated/CKD) | Described in a severe untreated case (PMID:39644399) | — |
| Hypertension | Clinical sign | Adulthood (CKD-associated) | Described in untreated case | HP:0000822 Hypertension |

**Heterozygous (carrier) females:** clinical expression ranges from asymptomatic to a full NDI phenotype indistinguishable from affected males. This variability is attributed to **skewed X-chromosome inactivation**; one AVPR2-mutation-positive female in a recent cohort had overt NDI despite the "typically asymptomatic carrier" expectation (PMID:40922895).

### Quality-of-life impact
Chronic polyuria/polydipsia in school-age children and adults causes significant social and functional burden: need for constant water access, disrupted sleep from nocturia, school/work disruption, and psychological burden of a rare chronic disease. The pediatric cohort above documented high health-system burden directly attributable to the phenotype: 61% required inpatient hospitalization and 36% required gastrostomy tube placement for fluid/caloric management (PMID:32039113). No disease-specific quality-of-life instrument validation was identified in this search; QoL is inferred from these morbidity proxies rather than from EQ-5D/SF-36/PROMIS studies specific to NDI.

---

## 4. Genetic/Molecular Information

### Causal gene
- **AVPR2** (HGNC:897; OMIM *300538), Xq28, 2.2 kb, 3 exons, encoding a 371-amino-acid, ~40.3 kDa class-A (rhodopsin-like) G protein-coupled receptor with 7 transmembrane domains (search synthesis, this session, consistent with OMIM *300538).

### Pathogenic variants
- **Variant spectrum:** >200 published disease-causing AVPR2 variants — missense (the largest class), nonsense, small insertions/deletions, large deletions, and complex rearrangements.
- **ACMG/AMP classification:** individual variants are classified via ClinVar/ClinGen on a case-by-case basis; e.g., ClinVar RCV000011591 classifies AVPR2 c.1009C>T (p.Arg337Ter) as pathogenic for X-linked NDI, and RCV000011599 classifies c.137T>A (p.Ile46Lys) likewise (search synthesis, this session — verify exact ClinVar classification labels before citing in a KB entry).
- **Allele frequency:** AVPR2 pathogenic variants are individually rare/private (frequent de novo occurrence and many unique familial variants); no single recurrent common allele dominates globally, though regional founder variants exist (§9). No gnomAD constraint metric (LOEUF/pLI) for AVPR2 was retrieved with confidence in this session — recommend a direct gnomAD query before citing a specific constraint value.
- **Origin:** germline (inherited X-linked or de novo); no somatic AVPR2 NDI mechanism is described.
- **Functional consequence — three recognized mechanistic classes** of mutant V2 receptor (search synthesis, consistent with the functional-rescue literature reviewed, e.g., PMID:35153784, and Sci Rep 2020, doi:10.1038/s41598-020-73089-x):
  1. **Type I (protein-expression disorder):** decreased, truncated, or null protein expression from transcription/mRNA-processing/translation defects.
  2. **Type II (localization/trafficking disorder) — the most common class, ~70% of NDI-causing AVPR2 variants:** the receptor misfolds, is retained in the endoplasmic reticulum by ER quality control, and never reaches the plasma membrane (e.g., variants at W164S, A165D, A165P, S167T, Q174R fail to exit the ER). One Danish case documents ER retention with subsequent **lysosomal degradation** of the mutant receptor (academic.oup.com/ckj, this session).
  3. **Type III (functional disorder):** the receptor reaches the cell surface normally but has defective ligand binding, defective Gs-coupling, or constitutive endocytosis, so it cannot generate a normal cAMP response despite correct trafficking.
- **Partial-NDI variants** (§2) typically behave as attenuated Type II/III defects retaining residual function.

### Modifier genes
No AVPR2-independent modifier gene for X-NDI severity is established in the literature surveyed; the principal "modifier" of phenotype in heterozygotes is X-inactivation skewing (an epigenetic, not genic, modifier — see below) rather than a second locus.

### Epigenetic information
The dominant epigenetic determinant of **disease expression in heterozygous females** is the pattern of **X-chromosome inactivation (XCI)**: skewing toward preferential inactivation of the wild-type allele yields a manifesting carrier with an overt (sometimes full) phenotype, while skewing toward the mutant allele yields an asymptomatic carrier. No disease-specific DNA methylation or histone-modification signature of the AVPR2 locus itself (beyond XCI) was identified in this search.

### Chromosomal abnormalities
Some AVPR2-causing lesions are **large deletions** spanning the gene (e.g., a novel large AVPR2 deletion reported in an infant, PMC article reviewed this session) rather than point mutations; complex rearrangements are also reported. No recurrent translocation or aneuploidy mechanism is described for NDI1.

---

## 5. Environmental Information

### Environmental factors
For the **inherited X-linked form**, there is no environmental causal factor — the lesion is a germline AVPR2 variant. However, environmental exposures precipitate the clinical emergencies of the disease (dehydration, hypernatremic crisis) and can be superimposed to worsen the renal concentrating defect:

- **Water restriction / reduced access** — the single most important modifiable precipitant of crisis in an AVPR2 hemizygote (documented repeatedly in case series, this session).
- **Illness with vomiting/reduced intake** — a recurring precipitant of acute decompensation in infants (GeneReviews NBK1177/PMID:20301356).
- **Heat/high ambient temperature and exercise** — increase insensible losses on top of an already maximal obligate renal water loss (general clinical inference; not independently verified by a specific citation in this session).

### Environmental factors relevant to the *acquired/secondary* NDI phenocopy (important differential, and mechanistically informative even though genetically distinct from X-NDI):
- **Lithium therapy** — downregulates renal AQP2 via chronic collecting-duct toxicity (search synthesis, this session).
- **Hypercalcemia** — induces targeted autophagic degradation of AQP2 (ScienceDirect article reviewed, this session).
- **Hypokalemia** — likewise triggers autophagic AQP2 degradation.
- **Increased renal prostaglandin E2 (PGE2) production**, seen in both human and animal acquired-NDI, antagonizes AVP-stimulated water permeability by promoting AQP2 internalization from the apical membrane — this is the documented mechanistic basis for indomethacin's (a PGE2-synthesis inhibitor) therapeutic benefit even in the genetic, receptor-null form of NDI.

### Lifestyle factors
No specific lifestyle (smoking, alcohol, exercise pattern) risk-modifying factor for X-NDI onset or severity was identified; lifestyle management (ensured free water access, avoidance of salt/protein-overload diet) is a **treatment**, not a primary risk factor (§12).

### Infectious agents
X-NDI itself has no infectious etiology. Note for differential diagnosis: **acquired** NDI has been documented secondary to leptospirosis in a dog (PMC4005616, this session) and can occur secondary to pyelonephritis/obstructive uropathy in humans — mechanistically informative as a phenocopy, not a cause of the inherited disorder.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical phenotype)

1. **A hemizygous loss-of-function AVPR2 variant** (Xq28) is inherited or arises de novo, producing a mutant V2 vasopressin receptor — demonstrated, not inferred, by the >200 characterized pathogenic variants and associated functional studies reviewed above.
2. This **leads to** one of three receptor defects (demonstrated by functional/trafficking studies): (a) deficient/absent receptor protein synthesis (Type I), (b) ER misfolding with failure to traffic to the basolateral plasma membrane of the collecting-duct principal cell, followed by ER-associated degradation/lysosomal degradation (Type II, ~70% of cases — the dominant branch), or (c) normal surface expression but defective ligand binding or Gs-coupling (Type III).
3. Each defect **results in** failure of arginine vasopressin (AVP), released from the posterior pituitary in response to rising plasma osmolality, to productively engage a functional V2 receptor on the principal cell's basolateral membrane — demonstrated by radioligand-binding and signaling assays in the mutant-receptor literature.
4. This **leads to** failure to activate the **Gs–adenylyl cyclase–cAMP–protein kinase A (PKA)** cascade inside the principal cell — the canonical V2R signal-transduction pathway, now resolved at near-atomic resolution by cryo-EM structures of the AVP–V2R–Gs ternary complex (PMID:33664408, Cell Research 2021; companion structures in Science Advances, PMID:34020960, 2021, and a 2022 V2R–β-arrestin1 ternary-complex structure).
5. Without PKA activation, **AQP2 is not phosphorylated** at its regulatory serine residues (notably Ser256) — demonstrated biochemically — so **AQP2-containing subapical vesicles fail to fuse with the apical plasma membrane** of the principal cell.
6. This **results in** a structurally intact but functionally "closed" collecting duct: the apical membrane lacks water channels despite an intact basolateral-to-lumen osmotic gradient, so **free water cannot be reabsorbed** regardless of how high circulating AVP rises (demonstrated — NDI patients have elevated, not deficient, plasma AVP, which is the defining diagnostic distinction from central DI).
7. Impaired water reabsorption **leads to** the inability to concentrate urine above ~200 mOsm/kg despite maximal physiologic AVP stimulation (demonstrated diagnostically by the water-deprivation/DDAVP test) and produces **massive hyposthenuric polyuria**.
8. Polyuria **triggers** a compensatory increase in thirst drive and **polydipsia**; when water intake cannot keep pace with obligate renal free-water loss (illness, restricted access, infancy when thirst cannot be behaviorally expressed), this **leads to hypernatremic dehydration**, which in turn can cause CNS injury (inferred from clinical outcome literature — seizures, brain injury, and neurodevelopmental impairment are reported sequelae of *recurrent* hypernatremic episodes, PMID:40922895, rather than of the AVPR2 defect directly).
9. Chronic high urine flow **leads to**, over years, progressive **dilatation of the collecting system** — hydronephrosis, hydroureter, and megacystis with bladder-wall trabeculation and voiding dysfunction — demonstrated longitudinally in both pediatric cohorts (PMID:32039113) and an extreme untreated adult case (post-void residual 3.1 L; PMID:39644399).
10. Chronic obstructive uropathy from branch 9 **results in** slowly progressive **chronic kidney disease**, which can in turn cause secondary hyperparathyroidism and hypertension, as documented in the untreated 58-year-old case above — this is a downstream, largely preventable consequence of delayed diagnosis/treatment rather than a direct effect of the AVPR2 defect on nephron mass.
11. Separately and in parallel, chronic caloric expenditure on excessive urine production plus reduced oral intake during feeding-limited infancy **contributes to** failure to thrive and growth impairment (documented: 70–71% of a pediatric cohort below −2 SD for weight/height at presentation, PMID:32039113) — partially reversible with treatment (29–38% still below −2 SD at follow-up).

### Molecular pathway
Gs–adenylyl cyclase–cAMP–PKA signaling downstream of the V2 receptor is the central, and in the inherited disease the **exclusively disrupted**, pathway (KEGG/Reactome-type annotation: "vasopressin-regulated water reabsorption" pathway). A cAMP-**independent** rescue pathway has been identified pharmacologically: **AMPK activation** (e.g., by metformin) can phosphorylate AQP2 (and UT-A1) and increase apical AQP2 trafficking even in V2R-null cells/mice, providing an alternate kinase route to the same vesicle-trafficking endpoint (search synthesis, this session; mechanistic basis for the NDI-5001 candidate drug, §12).

### Cellular processes
The principal cellular lesion is a **protein-trafficking/quality-control defect** (ER retention, ERAD, lysosomal degradation of misfolded V2R) rather than apoptosis, classical inflammation, or cell-cycle dysregulation. Secondary cellular consequences of chronic obstruction (tubular atrophy, interstitial fibrosis) presumably occur in long-standing untreated disease but were not separately characterized in the sources reviewed.

### Protein dysfunction
Loss-of-function via **misfolding** dominates (Type II, ~70%); a minority of variants alter catalytic/signaling function without misfolding (Type III); a further subset abolish expression outright (Type I). This is a receptor-level loss-of-function disorder, not a gain-of-function or dominant-negative mechanism in the X-linked hemizygous male (dominant-negative mechanisms are instead characteristic of some *autosomal dominant* AQP2 NDI variants, a genocopy — see §4/§9 comparison).

### Metabolic changes
No primary metabolic pathway defect is described; secondary electrolyte derangement (hypernatremia) and, in chronic disease, CKD-associated metabolic bone disease (secondary hyperparathyroidism, documented in the untreated adult case above) are downstream consequences rather than primary mechanisms.

### Immune system involvement
Not implicated; X-NDI is not an immune-mediated or inflammatory disorder.

### Tissue damage mechanisms
The principal tissue-damage mechanism is **mechanical/obstructive** — chronic high urine flow leading to collecting-system dilatation, bladder-wall trabeculation, and secondary CKD — rather than oxidative, ischemic, or fibrotic injury at the cellular level (though fibrosis likely supervenes in long-standing obstructive nephropathy by general nephrology principles, not separately documented here for X-NDI specifically).

### Biochemical abnormalities
Defective **GPCR function** (V2 receptor) is the core biochemical lesion; AQP2 itself is structurally normal in X-NDI (distinguishing it from the AQP2-mutant autosomal form, where AQP2 itself is the defective protein/channel).

### Molecular profiling
No disease-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, or spatial-transcriptomic dataset for human X-NDI kidney tissue was identified in this search (unsurprising given inaccessibility of human collecting-duct tissue and the kidney's structural normalcy). The closest analogues are the **Avpr2-deficient rat model** generated by the rGONAD gene-editing method (PMID:40102322, Clin Exp Nephrol 2025) and **inducible Avpr2-knockout mice** (Avpr2^fl/y^;Esr1-Cre, tamoxifen-inducible, used because constitutive Avpr2-null male pups die within the first week of life), which support molecular/histological characterization (§15).

---

## 7. Anatomical Structures Affected

### Organ level
- **Primary organ:** kidney — specifically the **renal collecting duct** (cortical and medullary segments) and, to a lesser extent, the distal convoluted tubule, where V2 receptor expression is concentrated.
- **Secondary organ involvement:** urinary bladder (chronic overdistension, trabeculation, diverticulum formation in severe/untreated disease) and ureters (hydroureter from chronically high urine flow and, later, outflow dysfunction); CNS (secondary injury from hypernatremic episodes, not primary involvement).
- **Body systems involved:** renal/urinary (primary), endocrine (vasopressin axis — pituitary AVP secretion is normal/elevated, not primarily affected), and secondarily cardiovascular (hypertension in CKD) and skeletal/parathyroid (secondary hyperparathyroidism in CKD).

### Tissue and cell level
- **Cell population targeted:** renal collecting-duct **principal cells** (the AQP2- and V2R-expressing epithelial cell type); suggested Cell Ontology term: CL:1001431 (kidney collecting duct principal cell) — unverified, confirm via OAK/CL before KB use.
- **Tissue type:** simple cuboidal epithelium of the collecting duct.

### Subcellular level
- **Endoplasmic reticulum** — site of V2 receptor misfolding and retention for Type II variants; candidate GO Cellular Component term GO:0005783 (endoplasmic reticulum) — unverified.
- **Apical plasma membrane** of the principal cell — the destination AQP2 fails to reach; candidate GO:0016324 (apical plasma membrane) — unverified.
- **Subapical storage vesicles** — site of AQP2 sequestration absent PKA-mediated trafficking signal.
- **Lysosome** — site of degradation of ER-retained misfolded V2 receptor in at least one documented case (academic.oup.com/ckj, this session).

### Localization
Bilateral, symmetric — there is no described lateralization, consistent with a systemic/genetic (not focal/structural) renal defect. Suggested UBERON term: UBERON:0001232 (collecting duct) — unverified.

---

## 8. Temporal Development

### Onset
The renal concentrating defect is present **from birth** (congenital). Clinical recognition, however, is typically delayed to early infancy: median age at diagnosis was **4.2 months** (IQR 1.1–9.8) in a 66-subject multicenter pediatric cohort (PMID:32039113), and **7.5 months** in a smaller long-term single-center cohort (PMID:40922895). Onset pattern is **insidious/subacute** in presentation (nonspecific feeding/irritability symptoms) punctuated by **acute** hypernatremic crises.

### Progression
- Disease **course pattern** is best described as **chronic and stable at the renal-tubular level** (the receptor defect itself does not worsen over time) but **progressive at the level of secondary complications** when inadequately treated — hydronephrosis, bladder dysfunction, and CKD accumulate over years to decades (documented trajectory from infancy to a severely affected 58-year-old in PMID:39644399).
- **Rate:** slow/progressive for secondary urologic and renal complications; rapid/acute for hypernatremic decompensation episodes.
- **Duration:** lifelong (no spontaneous remission described; this is a structural receptor null state, not a transient or reversible lesion as in some acquired NDI).

### Patterns
- **Remission:** none spontaneous; substantial symptomatic improvement (but not cure) with treatment — thiazide/amiloride/NSAID combination therapy reduces polyuria by up to ~50% (GeneReviews NBK1177/PMID:20301356) and normalized serum sodium in all treated patients in one cohort (PMID:40922895), though the underlying receptor defect persists lifelong.
- **Critical period:** **infancy** is the period of highest vulnerability — thirst cannot be behaviorally satisfied by a pre-verbal infant, so undiagnosed infants are at greatest risk of recurrent hypernatremic injury and of the failure-to-thrive/developmental sequelae documented above. Early diagnosis and treatment within this window is repeatedly identified in the literature as the single most important determinant of long-term neurodevelopmental and renal outcome.

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence (Quebec, Canada):** 8.8 per 1,000,000 males — the most frequently cited population estimate, assumed to be broadly representative worldwide (GeneReviews NBK1177/PMID:20301356; corroborated independently by search synthesis).
- **Regional founder-effect elevation:** incidence is **six times higher** in Nova Scotia/New Brunswick than the Quebec baseline, and is also elevated in Utah, due to population-specific founder AVPR2 variants.
- **Rarity context:** one long-term single-center cohort identified only **8 pediatric patients over a 34-year period** (1991–2024) (PMID:40922895), illustrating the disease's rarity even at a referral center.

### Inheritance pattern
**X-linked recessive** (note: one automated extraction in this session's research mislabeled this "X-linked dominant" — that is incorrect terminology for this disorder and is **not** adopted here). The canonical pattern is: hemizygous males are affected; heterozygous female carriers are classically described as asymptomatic but can manifest a partial-to-full phenotype through **skewed X-inactivation** (a manifesting-carrier phenomenon, not X-linked dominance in the Mendelian sense). At least one AVPR2-positive female in the literature reviewed had an overt, non-partial NDI phenotype (PMID:40922895).

- **Penetrance:** complete in hemizygous males; variable/incomplete in heterozygous females depending on XCI skewing.
- **Expressivity:** variable, most clearly illustrated by the **partial-NDI** variant class (§2, §4), which produces a milder, later-onset phenotype than the typical full loss-of-function variant.
- **Genetic anticipation:** not described (not a repeat-expansion disorder).
- **Germline mosaicism:** GeneReviews notes that for apparent de novo cases, recurrence risk in future offspring of the mother is low (<1%) but not zero, because of the possibility of maternal germline mosaicism (GeneReviews NBK1177/PMID:20301356).
- **Founder effects:** documented in Quebec/Nova Scotia/New Brunswick (Canada) and Utah (USA) populations (see Epidemiology above).
- **Consanguinity:** more relevant to the **autosomal recessive** AQP2 form (NDI2) than to X-linked NDI1, which does not require biallelic inheritance in males.
- **Carrier frequency:** not separately quantified in the sources reviewed beyond the prevalence figures above; would require a dedicated population-genetics study (e.g., gnomAD hemizygote counts), not retrieved with confidence in this session.

### Population demographics
- **Sex ratio:** strongly male-predominant by mechanism; one pediatric cohort was 89% male (PMID:32039113), and 7 of 8 patients in another long-term cohort were male (PMID:40922895) — the residual female cases are manifesting heterozygous carriers, not a second inheritance mechanism.
- **Ethnic/geographic distribution:** documented cases worldwide (Chinese, Turkish, Danish, Asian, and North American pedigrees all cited in this session's sources), with founder-variant clustering in parts of Canada and Utah as above; one cohort was 67% white (PMID:32039113), though this likely reflects referral-center ascertainment rather than a biological ethnic predisposition.
- **Age distribution:** overwhelmingly diagnosed in infancy; adult presentations in the literature largely represent either undiagnosed/untreated childhood-onset disease recognized late (e.g., the 58-year-old case, PMID:39644399) or partial-NDI variants with delayed clinical recognition.

---

## 10. Diagnostics

### Clinical tests
- **Water-deprivation test with DDAVP (desmopressin) challenge:** the classic confirmatory test — affected individuals fail to concentrate urine above ~200 mOsm/kg H2O despite desmopressin administration, distinguishing NDI from central DI (which responds to DDAVP) (GeneReviews NBK1177/PMID:20301356). **Important safety caveat** documented in a recent case series: water-deprivation testing is **contraindicated once serum sodium exceeds 145 mmol/L**; in that setting, a **desmopressin challenge alone** (without prior deprivation) should be used, and "all desmopressin tests were negative" across all NDI1 cases in one cohort (PMID:40922895).
- **Copeptin-based diagnosis** (a major recent diagnostic advance, supplanting/complementing the water-deprivation test): copeptin is the stable C-terminal fragment of the AVP prohormone and is a reliable surrogate for plasma AVP. **Unstimulated basal copeptin reliably diagnoses nephrogenic DI** (high basal copeptin unequivocally indicates NDI, since the defect is downstream of normal/elevated AVP secretion), whereas a **stimulation test** (hypertonic saline or arginine infusion) is needed to separate central DI from primary polydipsia. A stimulated copeptin level of **4.9 pmol/L** after hypertonic saline infusion differentiates central DI from primary polydipsia with high accuracy, superior to the classical water-deprivation test (search synthesis referencing the landmark NEJM copeptin studies, e.g., Fenske et al., N Engl J Med 2018 — PMID not independently verified in this session). The 2024 international consensus statement additionally reports a baseline plasma copeptin cutoff **>21.4 pmol/L** as diagnostic for NDI in adults (Levtchenko et al., Nat Rev Nephrol 2024, DOI:10.1038/s41581-024-00897-z — PMID not captured; cite by DOI).
- **Laboratory findings:** hypernatremia (serum Na+ often >145–160 mmol/L at presentation), low urine specific gravity/osmolality, normal-to-elevated plasma AVP.
- **Imaging:** renal/bladder ultrasound to detect and monitor secondary hydronephrosis, hydroureter, and megacystis (recommended periodic surveillance per GeneReviews — annual in adults).

### Genetic testing
- **First-tier:** AVPR2 single-gene sequence analysis, detecting ~90% of pathogenic variants.
- **Second-tier (if sequencing negative):** gene-targeted deletion/duplication analysis (MLPA or equivalent) for the remaining large-rearrangement cases.
- **Alternative:** multigene renal-tubulopathy or polyuria/DI panel including AVPR2, AQP2, and AVP.
- In the Pediatric Nephrology Research Consortium cohort, genetic testing or family history was obtained in 70% of subjects; among those tested, **89% had AVPR2 variants and 11% had AQP2** (PMID:32039113) — a useful real-world confirmation of the textbook 90:10 split.
- **Whole-exome/genome sequencing** is appropriate when single-gene/panel testing is negative or the phenotype is atypical, per general rare-disease diagnostic practice (not separately validated for NDI specifically in the sources reviewed).

### Differential diagnosis
The core differential is the **polyuria-polydipsia syndrome** triad:
1. **Central (neurogenic) diabetes insipidus** — deficient AVP secretion; responds to desmopressin (the key distinguishing response).
2. **Primary (dipsogenic) polydipsia** — excessive water intake from a primary thirst-drive abnormality, with intact AVP axis.
3. **Nephrogenic diabetes insipidus** — AVP resistance at the kidney (this disease).
Additional mimics/secondary causes to exclude: **acquired NDI** (lithium, hypercalcemia, hypokalemia, obstructive uropathy); **Bartter syndrome** (can present with hypernatremia-hyperchloremia mimicking NDI, and refractory hypokalemia should prompt evaluation for Bartter syndrome rather than primary NDI); sickle cell disease/trait-associated renal medullary injury; other inherited tubulopathies.

### Screening
No population-based newborn screening program for X-NDI exists (it is not detected by standard metabolic newborn screening panels). Cascade/carrier testing in at-risk female relatives and prenatal/preimplantation genetic testing become available once the family's causal AVPR2 variant is identified (GeneReviews NBK1177/PMID:20301356).

---

## 11. Outcome/Prognosis

### Survival and mortality
No disease-specific mortality or survival-rate statistic (5-year/10-year) was identified in the literature surveyed; NDI1 is not generally described as a life-shortening condition **when diagnosed and treated**, though recurrent severe hypernatremic crises in undiagnosed infants carry acute mortality/morbidity risk (general clinical inference, consistent with but not separately quantified by the sources reviewed).

### Morbidity and function
- With **early diagnosis and appropriate management**, intelligence and lifespan are "usually normal" per GeneReviews (NBK1177/PMID:20301356) — but a more recent long-term single-center cohort (median follow-up 16.9 years) found **75% (6 of 8) patients developed a neurodevelopmental disorder** (intellectual disability, ASD, or language delay) despite treatment (PMID:40922895), a substantially more concerning figure that should be weighed against the classic "normal outcome with early treatment" teaching — the discrepancy may reflect residual subclinical dehydration episodes, cohort/ascertainment differences, or genuine evolving understanding of long-term neurodevelopmental risk; this is flagged as an open tension in the literature rather than resolved here.
- **Growth:** severe growth impairment is common at diagnosis (70–71% below −2 SD weight/height) and improves but often does not normalize with treatment (29–38% still below −2 SD at follow-up) (PMID:32039113).
- **Renal function:** 23–30% of a pediatric cohort had CKD stage ≥2 at follow-up (PMID:32039113); an untreated adult case showed eGFR 25 mL/min/1.73m² after decades of disease (PMID:39644399) — illustrating a clear treatment-dependent divergence in renal prognosis.
- **Urologic morbidity:** 37% urologic complications (hydronephrosis, bladder dysfunction) in the pediatric cohort; severe bladder decompensation (3.1 L post-void residual, trabeculation, diverticulum) in the untreated adult case.

### Disease course / complications
Complications cluster into: (1) acute hypernatremic dehydration/CNS injury episodes, (2) chronic urologic tract dilatation and bladder dysfunction, (3) secondary CKD and its sequelae (hypertension, secondary hyperparathyroidism), and (4) growth impairment. Recovery potential for the renal-tubular defect itself is nil (it is a fixed genetic lesion), but recovery/stabilization of the secondary complications is substantial with early, sustained treatment.

### Prognostic factors
**Age at diagnosis/treatment initiation** is the dominant prognostic factor identified across every source reviewed — earlier diagnosis and treatment correlates with better growth, renal, and (per the classic teaching, though contested by the more recent cohort above) neurodevelopmental outcomes. Variant class (full vs. partial loss-of-function) is a secondary prognostic determinant, with partial-NDI variants generally producing a milder course.

---

## 12. Treatment

There is **no curative therapy** for X-NDI; management is lifelong and directed at minimizing polyuria, preventing dehydration, and averting secondary complications (GeneReviews NBK1177/PMID:20301356; search synthesis this session).

### Pharmacotherapy
- **Thiazide diuretics** (hydrochlorothiazide, chlorothiazide) — first-line; paradoxically reduce urine output in NDI by inducing mild volume contraction that increases proximal tubular sodium/water reabsorption, thereby reducing delivery of filtrate to the unresponsive collecting duct. Used in 74% of one pediatric cohort (PMID:32039113) and in **all** patients of another cohort, combined with amiloride (PMID:40922895). Suggested NCIT clinical-action term: NCIT:C15986 (Pharmacotherapy) for the generic action, with the specific agent as `therapeutic_agent` — e.g., CHEBI (hydrochlorothiazide) — unverified CURIEs, confirm before KB use.
- **Potassium-sparing diuretics (amiloride)** — frequently combined with thiazide (33% of one cohort used this combination specifically; PMID:32039113) both for additive antidiuretic effect and to offset thiazide-induced hypokalemia.
- **NSAIDs (indomethacin)** — added in 42% of one cohort (PMID:32039113) and 62.5% of another (PMID:40922895); mechanistically reduces renal PGE2 synthesis, and PGE2 independently promotes AQP2 internalization (§6), so indomethacin provides an AQP2-membrane-stabilizing effect independent of the V2R defect. Use requires monitoring for renal/GI NSAID toxicity with prolonged use.
- **Pharmacogenomics:** no AVPR2-genotype-specific drug-dosing guidance (e.g., PharmGKB/CPIC guideline) was identified; dosing is empiric/weight-based per general pediatric nephrology practice.

### Emergency/acute management
Critical point emphasized in GeneReviews: **IV normal saline is contraindicated** in acute hypernatremic crisis in NDI, as it can **worsen** hypernatremia; free-water-deficit replacement with **5% dextrose in water** is the correct emergency fluid strategy (NBK1177/PMID:20301356).

### Supportive care
Unrestricted free access to water is mandatory and is itself the most important "treatment" — water restriction is explicitly contraindicated. Dietary measures: exclusive breastfeeding in infancy where feasible, and a **high-calorie, low-sodium, low-protein diet** to reduce the obligate solute load the nephron must excrete (search synthesis, this session).

### Experimental / emerging therapeutics (recent developments, 2024–2026)
- **Pharmacological chaperones targeting the mutant V2 receptor directly:** tolvaptan (a clinically approved V2R inverse agonist/antagonist used for other indications) can, counter-intuitively, act as a **pharmacochaperone** for certain misfolded (Type II) AVPR2 variants — aiding correct folding in the ER and escape from ER quality control so the mutant receptor reaches the membrane, where endogenous AVP can then activate it. The **M272R** V2R mutant specifically responded to tolvaptan with improved maturation, membrane trafficking, and DDAVP responsiveness (Sci Rep 2020, doi:10.1038/s41598-020-73089-x). A related study using both the antagonist tolvaptan and a novel high-affinity agonist pharmacochaperone (**MCF14**) showed partial functional rescue of a different NDI-causing V2R mutant (PMID:35153784, Frontiers in Pharmacology 2022). This is inherently a **mutation-specific / personalized-medicine** approach — not all variant classes are rescuable (Type II ER-retained variants are the best candidates; Type I null-expression variants are not).
- **Nonpeptide V2R agonists** (e.g., SR121463) have similarly been shown to act as chaperones, partially rescuing trafficking-defective mutants such as L57R in experimental systems, particularly relevant for **partial** cNDI-causing variants (PMC11095762, this session).
- **β3-adrenergic receptor (β3-AR) agonism — a V2R-independent rescue strategy, 2024:** in the mouse model of X-NDI, the β3-AR agonist **BRL37344** produced a sustained antidiuretic effect (24-h urine output reduced 27%, urine osmolality increased 25%, water intake reduced 20%) by increasing phosphorylation of NKCC2, NCC, and AQP2 (notably AQP2 Ser256) and increasing AQP2 apical membrane expression — entirely bypassing the defective V2 receptor (Milano et al., J Cell Mol Med 2024, PMID:38652212). This is proposed as a candidate strategy applicable regardless of AVPR2 variant class, since it does not require receptor rescue at all.
- **AMPK activation — the basis of an active clinical-stage candidate:** AMPK provides a cAMP/PKA-**independent** route to AQP2 (and UT-A1) phosphorylation and apical trafficking; metformin-mediated AMPK activation improved urine osmolality in **V2R-knockout mice** (search synthesis, this session). This mechanism underlies **NDI-5001**, a proprietary small-molecule AMPK activator in active clinical development by **NephroDI Therapeutics** (partnered with Otsuka's McQuade Center for Strategic Research and Development) as a potential first-in-class therapy. A Phase 1 trial — **NCT07525960**, "A Study in Adult Males With X-linked Congenital Nephrogenic Diabetes Insipidus to Test the Effects of NDI-5001 Given for Multiple Days and to Test How NDI-5001 is Tolerated and Taken up in the Body" — is registered on ClinicalTrials.gov (sponsor: Otsuka Pharmaceutical Development & Commercialization, Inc.), representing the most advanced V2R-bypass therapeutic approach currently in human testing for this disease.
- **Gene therapy:** no AVPR2 gene-replacement or gene-editing clinical program was identified in this search; this remains a theoretical future direction rather than a current pipeline asset.

### Surgical/interventional and rehabilitative
Surgical intervention is reserved for managing severe secondary urologic complications (e.g., bladder decompression/augmentation in cases of severe chronic overdistension) rather than as a primary disease treatment; no NDI-specific surgical protocol was identified. No physical/occupational/speech therapy protocol specific to NDI beyond standard management of any associated neurodevelopmental comorbidity.

### Treatment strategy / algorithm
The de facto algorithm from the sources reviewed is: (1) ensure unrestricted water access and correct any acute hypernatremia with D5W (never isotonic/hypertonic saline); (2) initiate thiazide + amiloride combination as first-line chronic therapy; (3) add indomethacin/NSAID if polyuria remains inadequately controlled, with renal-function monitoring; (4) for select, genotyped Type II "rescuable" variants, pharmacochaperone approaches (tolvaptan, investigational agonist chaperones) are an emerging personalized option rather than standard of care; (5) structured surveillance (growth, serum sodium, renal ultrasound) per the schedule in §10/GeneReviews.

### Treatment outcomes
In the most detailed long-term cohort reviewed, combination hydrochlorothiazide + amiloride (± indomethacin in 62.5%) **normalized serum sodium in all patients** and preserved renal function throughout follow-up (PMID:40922895) — even though neurodevelopmental outcomes in that same cohort were less favorable than classically taught (§11), underscoring that biochemical/renal control does not guarantee freedom from neurodevelopmental sequelae, possibly reflecting the cumulative impact of pre-treatment and breakthrough dehydration episodes.

---

## 13. Prevention

### Primary prevention
There is no way to prevent the underlying genetic lesion; "primary prevention" in this disease is effectively **genetic counseling and reproductive options** (below) rather than risk-factor modification, since there is no modifiable environmental cause of the inherited disorder itself.

### Secondary prevention (early detection)
- **High index of suspicion in male infants** with unexplained fever, poor feeding, irritability, or failure to thrive — the literature consistently identifies delayed recognition (median diagnosis age 4.2–7.5 months, well after birth) as a remediable gap, since the renal defect is congenital.
- **Family-history-triggered testing**: once an index case's AVPR2 variant is known, at-risk male relatives can be tested in the neonatal period, pre-empting the diagnostic delay seen in sporadic/index presentations.

### Tertiary prevention (preventing complications in those already affected)
- Consistent thiazide/amiloride (±NSAID) therapy and unrestricted water access to prevent recurrent hypernatremic crises (which drive neurodevelopmental risk) and to blunt the progression to hydronephrosis/CKD (§6, §11).
- Scheduled surveillance: growth every 3 months (infants) to every 6–12 months (older children/adults); serum sodium on the same cadence; annual renal/bladder ultrasound to catch early structural complications (GeneReviews NBK1177/PMID:20301356).
- Emergency-preparedness education for families (recognizing early dehydration signs, avoiding inappropriate isotonic IV fluids) given the specific and counter-intuitive emergency-management pitfall noted in §12.

### Genetic counseling / family planning
Once the family's causal AVPR2 variant is identified, **carrier testing** in at-risk female relatives, **prenatal diagnosis**, and **preimplantation genetic testing** are all available (GeneReviews NBK1177/PMID:20301356). The 2024 international consensus statement explicitly includes "genetic counselling and family planning" as one of its 36 formal recommendation domains (Levtchenko et al., Nat Rev Nephrol 2024, DOI:10.1038/s41581-024-00897-z), reflecting current expert consensus that this is now a standard, guideline-level component of care — not an ad hoc addition.

### Immunization / public health / prophylaxis
Not applicable — this is a non-infectious, non-communicable monogenic disorder.

---

## 14. Other Species / Natural Disease

### Taxonomy and naturally occurring disease
- **Dogs and cats:** primary (familial) congenital NDI is recognized in veterinary medicine as a rare disorder involving impaired AQP2 membrane insertion, mechanistically analogous to the human disease, though the search did not return a confirmed naturally-occurring **AVPR2**-mutant canine/feline pedigree specifically (as opposed to the human-orthologous mechanism generally) — this should be treated as a mechanistic analogy pending a specific OMIA entry, not a confirmed AVPR2 ortholog defect in a companion-animal breed.
- **Secondary/acquired NDI in companion animals** is well documented and far more common than primary/congenital veterinary NDI — e.g., a case of acquired NDI secondary to **leptospirosis** in a dog (PMC4005616, this session), and secondary NDI as "the most common cause of polyuria/polydipsia in small animals," usually from bacterial infection or hypercalcemia rather than an inherited AVPR2 defect.
- No specific OMIA (Online Mendelian Inheritance in Animals) entry for a naturally occurring AVPR2-mutant breed-specific disease was retrieved with confidence in this session; this gap should be treated as "not found," not as evidence of absence, and would merit a direct OMIA database query before a definitive claim in a KB entry.

### Comparative biology / orthologous gene
AVPR2 and its downstream AQP2/cAMP/PKA pathway are highly conserved across mammals — this conservation is precisely what makes rodent models (mouse, rat) informative surrogates for human mechanism and drug testing (§15). No NCBI Gene ortholog ID or cross-species evolutionary-conservation statistic specific to AVPR2 was independently verified in this session.

### Transmission
Not applicable — this is a non-transmissible monogenic disorder with no zoonotic potential.

---

## 15. Model Organisms

### Mouse models
- **Constitutive Avpr2-null mice are embryonic/perinatally compromised:** male pups lacking Avpr2 die within the **first week after birth**, precluding study of the adult phenotype with a simple knockout — a significant modeling limitation directly analogous to, but more severe than, the human disease (search synthesis, this session).
- **Inducible conditional knockout (Avpr2^fl/y^; Esr1-Cre, tamoxifen-inducible):** developed specifically to circumvent the neonatal-lethality problem, allowing Avpr2 ablation after survival to adulthood, and used as the platform for the 2024 β3-AR agonist rescue study (PMID:38652212) — this is the current standard mouse model for adult-phenotype X-NDI pharmacology.
- **Floxed Aqp2 inducible deletion mouse** (PMID:16434568) — models the downstream/genocopy AQP2 lesion rather than AVPR2 itself, but recapitulates the shared distal phenotype (inability to concentrate urine) and is useful for dissecting AQP2-specific versus receptor-specific contributions.
- **Aqp2 point-mutation mouse** (PLOS Genetics; URL retrieved, PMID not independently confirmed this session) — a genocopy model of the autosomal AQP2 form, useful comparator.
- **Limitations common to all current mouse models:** the neonatal lethality of the true null genotype means available models either require an inducible/conditional strategy (introducing a "when was the gene lost" confound relative to the congenital human disease) or model the AQP2 genocopy rather than the AVPR2 lesion itself — a translational caveat to flag explicitly if these models are cited as supporting evidence for an X-NDI (AVPR2) pathophysiology node in a KB entry, since strict fidelity to the *congenital* AVPR2-null phenotype is not fully captured by the inducible-adult model.

### Rat models
- **Avpr2-deficient rat, generated by the rGONAD (rat Genome-editing via Oviductal Nucleic Acid Delivery) method** (PMID:40102322, Clin Exp Nephrol 2025) — a novel, recently published (2025) gene-edited rat model explicitly developed as "a reliable model of congenital NDI for elucidating the underlying mechanisms and identifying therapeutic targets," with phenotyping by biological, molecular, and histological examination, and pharmacologic testing of hydrochlorothiazide (40 mg/kg/d) effects on water intake, urine volume, and urine osmolality in metabolic cages. This is the most recent (2025) and most directly AVPR2-relevant whole-animal model identified in this research.

### Applications and research use
These rodent models support: (1) mechanistic dissection of receptor-trafficking defects and downstream AQP2 regulation, (2) preclinical testing of V2R-bypass pharmacology (β3-AR agonism, AMPK activators such as the NDI-5001 candidate, metformin) — directly informing the current human Phase 1 program (NCT07525960), and (3) testing of pharmacochaperone rescue strategies for specific trafficking-defective receptor variants, though pharmacochaperone rescue studies to date have relied predominantly on heterologous cell-expression systems (e.g., HEK293, COS-7 — standard in the functional-characterization literature cited throughout §4/§6/§12) rather than whole-animal models, since chaperone rescue is inherently variant-specific and not easily modeled in a single knockout/knock-in animal.

### Resources
No dedicated NDI-specific model registry was identified; relevant models would be catalogued through standard resources — MGI (mouse), RGD (rat) — though specific strain/allele designations for the Avpr2 conditional-knockout and rGONAD rat lines were not independently cross-referenced against MGI/RGD accession numbers in this session.

---

## Summary of Key Sources Cited

| Source | PMID/DOI | Use in report |
|---|---|---|
| Bichet/Knoers, Hereditary Nephrogenic Diabetes Insipidus, GeneReviews | PMID:20301356 (NBK1177) | Clinical description, genetics, management, surveillance |
| Levtchenko E, et al. International expert consensus statement on cNDI. Nat Rev Nephrol. 2024 | DOI:10.1038/s41581-024-00897-z | Classification, copeptin diagnostic threshold, 36-recommendation framework, genetic counseling |
| Pediatric Nephrology Research Consortium cohort study | PMID:32039113 | Genetic-testing yield, treatment patterns, growth/urologic/CKD outcomes (n=66) |
| "Nephrogenic Diabetes Insipidus: Three Decades of Clinical Reality" | PMID:40922895 | Long-term cohort (n=8, 34 years), neurodevelopmental outcome, diagnostic/treatment detail |
| Capasso et al., natural history of untreated X-NDI | PMID:39644399 | Severe untreated-adult complication profile (hydronephrosis, CKD, bladder failure) |
| rGONAD Avpr2-deficient rat model | PMID:40102322 | 2025 whole-animal model |
| Milano et al., β3-AR agonist BRL37344 mouse study | PMID:38652212 | 2024 V2R-independent rescue mechanism/therapeutic lead |
| Cryo-EM AVP–V2R–Gs structure | PMID:33664408; companion PMID:34020960 | Structural basis of signal transduction |
| Pharmacochaperone rescue (tolvaptan/MCF14) | PMID:35153784 | Mutation-specific rescue strategy |
| ClinicalTrials.gov NCT07525960 (NDI-5001) | NCT07525960 | Active 2025–2027 Phase 1 AMPK-activator trial |

**Verification note:** several identifiers in this report (specific HPO/GO/CL/UBERON/CHEBI term IDs, the exact ClinVar classification labels, the MONDO ID, and a small number of PMIDs recalled from general domain knowledge rather than directly confirmed by a fetched source this session — notably the copeptin NEJM paper) are flagged inline as unverified leads. Per this repository's term- and reference-validation discipline, each should be confirmed against its authoritative source (OLS/OAK lookup, ClinVar record, or PubMed) before being written into a KB YAML entry.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 7 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC11095762` (1 mention) - Therapeutic potentials of nonpeptidic V2R agonists for partial cNDI-causing V2R mutants.
  - shared terms: receptor, genetic

Weighed against this report's own most characteristic terms: `avpr2`, `disease`, `session`, `variant`, `renal`, `ndi`, `secondary`, `aqp2`, `cohort`, `water`, `defect`, `synthesis`, `identified`, `mechanism`, `documented`, `x-ndi`, `treatment`, `receptor`, `nbk1177`, `genetic`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 18 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 5 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 0 |

17 of 18 terms resolved to a current term; the rest could not be looked up either way.