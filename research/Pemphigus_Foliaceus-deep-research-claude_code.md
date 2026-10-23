---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5-5
cached: false
start_time: '2026-09-29T02:56:07.148292'
end_time: '2026-09-29T02:58:29.930288'
duration_seconds: 142.78
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Pemphigus Foliaceus
  mondo_id: MONDO:0019324
  category: Autoimmune
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
  - claude-sonnet-5-5
  num_turns: 6
  total_cost_usd: 0.7803802
  session_id: 81562984-f39d-5787-be67-7015e0b1b678
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 2
reference_validation:
  total_references: 0
  verified: 0
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 12
  verified: 12
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0019324
    reported_labels:
    - given in the template; confirm the label
    ontology_label: pemphigus foliaceus
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pemphigus Foliaceus
- **MONDO ID:** MONDO:0019324 (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Pemphigus Foliaceus** covering all of the
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

I'll check the key citations against PubMed before writing the report.

# Pemphigus Foliaceus (MONDO:0019324): Disease Characteristics Research Report

**Evidence and citation status**
- I could not run live PubMed, OMIM or ClinicalTrials.gov queries in this session. The PubMed lookup was blocked, so nothing below was verified against a live source.
- The content comes from my knowledge of the literature. Citations are given as author, journal and year, and **I have deliberately given no PMIDs**. A PMID recalled from memory can be wrong, and the KB treats a fabricated identifier as worse than a missing one.
- Before curation, resolve each citation with `just fetch-reference PMID:…` and copy snippets from the cache. Do not use snippets from this report.
- Every ontology CURIE below is a lead only. Look each one up with `runoak` or the term caches before binding it. CURIEs I'm less sure of are written as a label with "(look up)".
- Trial and approval statements from 2023 onward are the least certain. They are marked "verify".

---

## 1. Disease Information

**Overview.** Pemphigus foliaceus (PF) is an organ-specific autoimmune blistering disease. Pathogenic IgG, mainly of the IgG4 subclass, targets desmoglein 1 (Dsg1), the desmosomal cadherin of the upper epidermis.
- The antibodies cause loss of keratinocyte–keratinocyte adhesion (acantholysis) in the superficial epidermis, at the granular or subcorneal layer.
- Lesions are fragile superficial blisters that break easily. They leave scaly, crusted, erythematous erosions on the seborrheic areas (scalp, face, upper trunk), usually **without mucosal involvement**.

**Identifiers**
- MONDO: MONDO:0019324 (given in the template; confirm the label).
- Other codes: ICD-10 L10.2, ICD-11 EB40.1 (look up), MeSH "Pemphigus" (PF is a MeSH descriptor or supplementary concept; look up), Orphanet (check whether PF has its own entry; look up), OMIM (none; PF is not a Mendelian disease).

**Synonyms and variants**
- Superficial pemphigus.
- **Endemic PF**: *fogo selvagem* ("wild fire") in Brazil, and the El Bagre (Colombia) and Tunisian foci.
- **Pemphigus erythematosus** (Senear–Usher syndrome): PF with lupus-like features.
- **Pemphigus herpetiformis**: an eosinophilic or neutrophilic variant.
- **Drug-induced PF**.
- **Paraneoplastic PF**: rare and debated.
- **Neonatal pemphigus**: transplacental IgG transfer.

**Data provenance.** This is aggregated disease-level knowledge from cohort studies, registries, reviews and consensus guidelines. It is not EHR-derived.

---

## 2. Etiology

**Causal factors.** PF is multifactorial: HLA-linked genetic susceptibility plus a loss of B-cell tolerance to Dsg1, usually after an environmental trigger.
- In endemic FS the leading hypothesis is an arthropod-borne exposure. Hematophagous black flies (*Simulium nigrimanum*) were epidemiologically implicated (Eaton et al., Brazil field studies, 1998; Diaz et al.). Causation is not proven.
- The hypothesis is that insect salivary antigens, or a virus or parasite, break tolerance through molecular mimicry or epitope spreading.

**Genetic risk factors**
- **HLA-DRB1 class II alleles.** FS is associated with DRB1*0102, *0404, *1402 and *1406, with a shared epitope in the peptide-binding groove (Petzl-Erler and Diaz groups, Brazil, 1990s–2000s). PV alleles overlap only partly.
- Non-HLA loci in pemphigus generally include ST18 (Sarig et al., PV in Jewish and Egyptian cohorts). Whether this applies to PF is unclear.
- Familial clustering exists in endemic areas.
- No single causal gene or Mendelian variant is known. There is no OMIM gene entry.

**Environmental and other risk factors**
- Rural residence near rivers in endemic areas, and young age at exposure.
- Drug triggers, mostly thiol drugs (penicillamine, captopril) and some non-thiol drugs.
- UV light and possibly other triggers exacerbate the disease.
- A large fraction of healthy people in endemic foci carry anti-Dsg1 IgG, mostly IgG1 (Warren et al., Lancet 2003). This supports an environmental exposure that most people tolerate.

**Protective factors.** None is well established.
- Non-permissive HLA-DRB1 alleles are relatively protective by inference.
- The IgG4-to-IgG1 pattern seems to distinguish exposed-but-healthy people from those who develop disease.

**Gene–environment interaction.** The HLA-DRB1 risk genotype plus the endemic exposure yields anti-Dsg1 IgG1, which class-switches to IgG4 as disease appears. Only a subset of exposed carriers develop clinical disease.

---

## 3. Phenotypes

| Feature | Approximate frequency | HPO suggestion (look up) |
|---|---|---|
| Superficial flaccid blisters that rupture, leaving erosions | Very frequent | Abnormal blistering of the skin (I believe HP:0008066) |
| Scaly, crusted, erythematous plaques in seborrheic distribution | Very frequent | Erythema; Skin erosion; Scaling skin |
| Positive Nikolsky sign | Frequent | Nikolsky sign (look up) |
| Pruritus | Frequent | Pruritus (I believe HP:0000989) |
| Burning or pain | Common | Skin pain (look up) |
| Mucosal sparing | Typical (mucosal involvement is rare) | Not an HPO term; record as a negative feature |
| Exfoliative erythroderma | Uncommon, severe | Exfoliative erythroderma (look up) |
| Secondary bacterial infection | Occasional | Recurrent cutaneous infections (look up) |
| Fever and malaise | Rare, in severe flares | Fever |

**Onset and course**
- Onset is usually in adults. Sporadic PF is typically diagnosed between age 40 and 60.
- Endemic FS often begins in children and young adults.
- The course is chronic and relapsing, occasionally with spontaneous remission (better documented in FS).
- PF is generally less severe than PV, and some patients remain localized for years.
- Sporadic PF and PV can evolve into each other. This is thought to reflect epitope spreading, and mucosal disease appears with anti-Dsg3.

**Quality of life.** Disease-specific instruments include ABQOL and TABQOL, DLQI and Skindex. QoL is impaired by pruritus, pain, disfigurement, crusting and odor, and by corticosteroid side effects. QoL tends to track disease activity (PDAI and ABSIS). I'm not aware of validated per-phenotype QoL data.

---

## 4. Genetic and Molecular Information

- **Autoantigen gene**: *DSG1* (desmoglein 1). HGNC ID probably hgnc:3048 (the KB uses lowercase `hgnc:`; verify by lookup). The protein is a ~160 kDa calcium-dependent desmosomal cadherin with five extracellular cadherin domains (EC1–EC5), highest in the upper epidermis.
- **Not a Mendelian disease.** There are no pathogenic variants in the ACMG/AMP sense.
- **Allele frequency and founder data.** No variant-level data. The HLA-DRB1 associations vary by population.
- **Related germline *DSG1* disease.** Loss-of-function *DSG1* variants cause striate palmoplantar keratoderma and SAM syndrome. This is a distinct mechanism (loss of Dsg1 expression, not antibody blockade), but it confirms Dsg1's role in epidermal integrity.
- **Modifier genes**: unknown.
- **Epigenetic, chromosomal and structural data**: not established for PF.

---

## 5. Environmental Information

- **Exposures.** Endemic vectors (black flies), rural and riverine living, and possibly viral or parasitic infections. Drug exposure is the best-established trigger: penicillamine, captopril and other thiol drugs, plus non-thiol drugs such as rifampin and some NSAIDs (Brenner et al. reviews).
- **Physical triggers.** UV light exacerbates pemphigus, and radiation therapy has been reported as a trigger.
- **Lifestyle.** Smoking appears associated with a lower risk of PV in some studies. This is not established for PF, and it is not a recommendation.
- **Infectious agents.** No pathogen has been proven to be causal. *Staphylococcus aureus* exfoliative toxin A cleaves Dsg1 and causes staphylococcal scalded skin syndrome and bullous impetigo (Amagai et al., Nat Med 2000). This is a phenocopy, not the cause of PF, and it is a key mechanistic proof that Dsg1 loss alone yields superficial blistering.

---

## 6. Mechanism / Pathophysiology

### Causal chain
1. **Genetic susceptibility.** A permissive HLA-DRB1 class II allele presents Dsg1 peptides to CD4+ T cells. *(Association is demonstrated; the mechanism is inferred.)*
2. **Environmental trigger.** Insect-borne, drug or other exposure precedes disease. *(Exposure is epidemiologic; the antigenic link is not demonstrated.)*
3. **Breakdown of tolerance.** Dsg1-reactive T cells and B cells escape tolerance and produce anti-Dsg1 IgG, often IgG1 or IgM at first. The preclinical phase appears in serum before disease. *(Demonstrated in FS.)*
4. **Epitope spreading and class switch.** The response moves from non-pathogenic epitopes in the C-terminal extracellular domains (EC3–EC5) to pathogenic epitopes in the N-terminal EC1–EC2 domains, and to IgG4. *(Demonstrated by Li et al. and Warren et al.; Sekiguchi et al., Immunity 2001, mapped the pathogenic epitopes.)*
5. **Pathogenic IgG4 binds Dsg1 on keratinocytes** in the upper epidermis. This leads to Dsg1 disruption by two routes: steric interference with trans-adhesion, and signalling and endocytic depletion of Dsg1 (the relative weight of the two is debated).
6. **Loss of desmosomal adhesion.** The signalling includes p38 MAPK, Src/EGFR, ERK and calcium, and Dsg1 internalization (Berkowitz et al.; Getsios and Green; Waschke).
7. **Acantholysis in the granular or subcorneal layer** produces superficial blisters that rupture into erosions and crusts.
8. **Desmoglein compensation explains the topography.** In the mucosa and deep epidermis, Dsg3 is abundant and compensates for Dsg1 loss. So in PF, with only anti-Dsg1, the mucosa and lower epidermis are spared. In PV with anti-Dsg3, mucosal and deep lesions occur (Mahoney et al., J Clin Invest 1999).
9. **Chronic inflammation** with neutrophils and eosinophils, pruritus and secondary infection follow. *(Inferred and observational.)*

### Details by category
- **Molecular pathways**: p38 MAPK, Src, EGFR, ERK, calcium and PKC signalling downstream of antibody binding. Apoptosis is a secondary event, not the primary lesion (a debated point).
- **Cellular processes**: acantholysis, keratinocyte detachment, desmosome disassembly.
- **Protein dysfunction**: Dsg1 loses its adhesive function. Pathogenic antibodies map to EC1–EC2 (adhesive interface); non-pathogenic ones bind elsewhere.
- **Immune system**: T-cell-dependent B-cell autoimmunity (Th2 and Tfh bias), and IgG4 that is non-complement-fixing. Blistering does not need complement or inflammation, as shown by Fab-fragment passive transfer (Rock, Labib and Diaz, J Clin Invest 1990). Rituximab response argues for a central role of B cells.
- **Metabolic and biochemical**: no specific abnormalities beyond steroid effects.
- **Omics and advanced technologies**: I know of no robust PF-specific single-cell, spatial or CRISPR dataset. Bulk transcriptomic work exists mainly for PV, and FS serology is well studied. Treat this section as a gap in the report and search GEO before assuming none exists.

### Suggested ontology terms (look up)
- GO: cell–cell adhesion via plasma-membrane adhesion molecules (I believe GO:0098609); homophilic cell adhesion via plasma membrane adhesion molecules (I believe GO:0007156); adaptive immune response (I believe GO:0002250); desmosome organization (look up).
- CL: keratinocyte (I believe CL:0000312), B cell (I believe CL:0000236), plasma cell, CD4+ alpha-beta T cell, T follicular helper cell (look up).
- GO CC: desmosome (look up).

---

## 7. Anatomical Structures Affected

- **Primary**: skin epidermis, upper layers (granular layer and stratum corneum junction). UBERON epidermis (I believe UBERON:0001003) and the more specific layers (look up).
- **Distribution**: seborrheic areas (scalp, face, presternal and interscapular trunk), often bilateral and symmetric. It can generalize to erythroderma.
- **Secondary**: mucous membranes are typically spared. Secondary involvement is the skin surface and barrier (infection, fluid loss), and drug toxicity in other organs.
- **Cells and subcellular**: keratinocytes; the desmosome (Dsg1, plus desmocollin 1 in the same complex); plasma-membrane cadherin domains.

---

## 8. Temporal Development

- **Onset**: adult in sporadic PF, childhood to young adult in endemic FS. Pemphigus onset in childhood is uncommon. Presentation is insidious to subacute.
- **Progression**: chronic and relapsing–remitting, with flares. Patients may stay localized.
- **Duration**: usually chronic. Remission off therapy is possible: treatment-induced (especially after rituximab) or, in some FS patients, spontaneous.
- **Critical windows**: the preclinical period with anti-Dsg1 seropositivity precedes disease in FS. Early treatment reduces cumulative steroid exposure. Pregnancy carries neonatal transfer risk.

---

## 9. Inheritance and Population

- **Inheritance**: not Mendelian. It is a complex autoimmune trait with HLA association. Do not record it as monogenic.
- **Prevalence and incidence**
  - Sporadic pemphigus overall: about 0.1–1 per 100,000 per year, with wide geographic variation. PF is usually much rarer than PV in Europe and North America, and more common in parts of Tunisia, Brazil and Colombia.
  - Endemic FS has historically been reported in up to a few percent of residents in some isolated Brazilian foci, such as Amerindian settlements. Verify the exact figures.
  - Use `measure_type` and `rate_denominator` per the KB conventions, and treat the numbers as leads until sourced.
- **Sex ratio**: about equal in FS. Sporadic PF may show a modest female predominance, and Tunisian PF is female-predominant.
- **Geography**: Brazil (Central-West and Southeast, Goiás, Mato Grosso do Sul, Paraná), El Bagre in Colombia, Tunisia and parts of North Africa, and sporadic worldwide.

---

## 10. Diagnostics

- **Clinical exam**: superficial erosions and crusts in a seborrheic pattern, Nikolsky sign, and absence of mucosal disease.
- **Histopathology**: lesional biopsy from an intact fresh blister or edge shows subcorneal or granular-layer acantholysis. Inflammation is neutrophilic or eosinophilic. A Tzanck smear shows acantholytic cells.
- **Direct immunofluorescence (DIF)**: perilesional skin shows intercellular IgG, with or without C3, in a chicken-wire pattern. In PF it may be strongest in the upper epidermis. DIF is the gold standard for confirmation.
- **Indirect immunofluorescence (IIF)**: serum on monkey or guinea pig esophagus or on salt-split skin. Guinea pig esophagus is often more sensitive for anti-Dsg1.
- **ELISA or BIOCHIP**: anti-Dsg1 IgG is positive and anti-Dsg3 negative in pure PF (commercial assays such as MBL and Euroimmun). Titers correlate with disease activity.
- **Differential diagnosis**: PV, pemphigus erythematosus, IgA pemphigus, subcorneal pustular dermatosis, staphylococcal scalded skin syndrome, bullous impetigo, seborrheic dermatitis, discoid or subacute cutaneous lupus, bullous pemphigoid, Hailey–Hailey and Darier disease, and drug eruptions.
- **Genetic testing**: not indicated.
- **Severity scoring**: PDAI (Rosenbach et al. 2009), ABSIS, and the international consensus definitions of disease activity (Murrell et al., J Am Acad Dermatol 2008).
- **Guidelines**: Murrell et al. (J Am Acad Dermatol 2020, international panel); Joly et al. (EADV, J Eur Acad Dermatol Venereol 2020); Hertl et al. (EDF/EADV, 2015); Venning et al. (BAD, Br J Dermatol 2012).
- **Screening**: none. Anti-Dsg1 surveillance in endemic areas is a research tool.

---

## 11. Outcome / Prognosis

- **Mortality**: untreated pemphigus (mostly PV) was often fatal before corticosteroids. PF is milder overall. Current mortality is modest and largely from treatment complications (infection, cardiovascular disease, steroid toxicity). I did not verify specific survival percentages, so pull them from cohort studies (French, Brazilian, Israeli and Tunisian) before citing.
- **Complications**: secondary infection, dehydration and heat loss in erythroderma, steroid adverse effects (osteoporosis, diabetes, infection), and neonatal pemphigus in offspring of affected mothers.
- **Prognostic factors**: extent of disease at onset, response to first-line treatment, persistence of anti-Dsg1 titers, and age and comorbidity.
- **Recovery**: many patients reach remission on minimal or no therapy, especially with rituximab. Relapse is common when titers rise.
- **Comorbidities**: other autoimmune disease (thyroid, RA, lupus, myasthenia gravis with thymoma), and diabetes and osteoporosis from steroids.

---

## 12. Treatment

**Pharmacotherapy (NCIT:C15986 for the generic action; agents via `therapeutic_agent`)**
- **Localized or mild PF**: high-potency topical corticosteroids, sometimes with dapsone.
- **Systemic corticosteroids**: prednisone or prednisolone, about 0.5–1 mg/kg/day, then tapered. CHEBI class: corticosteroid (CHEBI:50858, per the KB notes).
- **Steroid-sparing immunosuppressants**: azathioprine, mycophenolate mofetil, methotrexate, cyclophosphamide, and dapsone (useful in milder PF).
- **Rituximab** (anti-CD20 monoclonal antibody; `therapeutic_modality: MONOCLONAL_ANTIBODY`). The Ritux 3 randomized trial (Joly et al., Lancet 2017) enrolled newly diagnosed PV and PF. Rituximab plus short-term prednisone produced complete remission off therapy in far more patients at 24 months than prednisone alone (I recall about 89% vs 34%; verify). Rituximab is now first-line in international guidelines. The US FDA approval (2018) is for moderate to severe **PV**, not PF, and PF use is off-label there. Verify.
- **Adjuncts**: IVIG, plasmapheresis or immunoadsorption for refractory disease.
- **Supportive care**: wound care, antiseptics, antibacterial treatment for secondary infection, and patient education.
- **Prophylaxis during immunosuppression**: PJP prophylaxis, calcium and vitamin D with bone protection, gastric protection, and hepatitis B screening before rituximab.

**Experimental and emerging (verify all status before curation)**
- **Anti-FcRn (efgartigimod)**: a phase 3 trial (ADDRESS) in PV and PF was reported as missing its primary endpoint, as I recall. Check the status and publication.
- **BTK inhibitor (rilzabrutinib)**: the phase 3 PEGASUS trial in pemphigus did not meet its primary endpoint, as I recall (verify).
- **DSG3 CAAR-T cells**: preclinical work is from Ellebrecht et al. (Science 2016), and early clinical work is in PV. There are no PF-specific data.
- For NCT identifiers, search ClinicalTrials.gov directly with `just fetch-reference NCT…`. I am not providing NCT numbers from memory.
- The PEMPHIX trial (rituximab vs mycophenolate, Werth et al., N Engl J Med 2021) was PV-only. Do not cite it for PF.

**Pharmacogenomics.** None established.

**Treatment strategy.** Mild localized: topical steroid ± dapsone. Moderate to severe: rituximab plus a short prednisone taper. Relapse: repeat rituximab or add an immunosuppressant.

Suggested NCIT terms (look up): Pharmacotherapy (NCIT:C15986); Corticosteroid Therapy and Immunosuppressive Therapy (look up); Rituximab (drug term, look up); Plasmapheresis and Intravenous Immunoglobulin (look up).

---

## 13. Prevention

- **Primary**: no established prevention. In endemic areas, vector control and reducing insect exposure are proposed. Avoid known trigger drugs where alternatives exist.
- **Secondary**: early recognition and early treatment of localized disease.
- **Tertiary**: prevent relapse with the lowest effective steroid dose and rituximab maintenance. Manage the steroid complications listed above.
- **Immunization**: inactivated vaccines are advised. Live vaccines are contraindicated during high-dose immunosuppression or rituximab. Ideally vaccinate before rituximab, since B-cell depletion blunts responses. Verify against current guidelines.
- **Counseling**: pregnancy counseling for the risk of neonatal pemphigus, which is usually transient. Sun protection.

---

## 14. Other Species / Natural Disease

- **Dogs**: PF is the most common autoimmune skin disease in dogs (NCBITaxon:9615 for *Canis lupus familiaris*, verify). Predisposed breeds include Akita, Chow Chow, Dachshund, Bearded Collie, Doberman Pinscher, Newfoundland and Finnish Spitz.
  - The major autoantigen is **desmocollin-1** (Bizikova et al. and Olivry's group, Vet Dermatol, 2010s), not DSG1. Other targets have been proposed.
  - Lesions are pustules, crusts and footpad hyperkeratosis on the nose, ears and face.
- **Cats and horses**: PF is also seen in cats (the most common feline autoimmune skin disease) and horses. Check OMIA for confirmation.
- **Cross-species comparison.** Superficial acantholysis is conserved, but the antigen differs in dogs (desmocollin-1 vs human DSG1). Treatment is similar: glucocorticoids ± azathioprine or chlorambucil.
- **Zoonosis**: none. Breed ontology (VBO) terms: look up.

---

## 15. Model Organisms

- **Passive-transfer mouse models (main model).** Injecting IgG or Fab from FS or PF patients into neonatal BALB/c mice reproduces superficial blistering (Roscoe et al., 1985; Rock et al., J Clin Invest 1990). It shows that the antibody alone is sufficient, and that Fab fragments are enough, so complement is not required. Limits: the disease is transient and needs no adaptive immune response of the host.
- **Recombinant human monoclonals.** Antibodies from PF patients, or mAbs against Dsg1 EC1/EC2, are pathogenic in neonatal mice and skin explants (Ishii and Amagai group; Sekiguchi et al. 2001).
- **Toxin model.** Exfoliative toxin A injection in neonatal mice cleaves Dsg1 and gives PF-like superficial blistering (Amagai et al., Nat Med 2000).
- **Genetic models.** Loss of Dsg1 in mouse (Dsg1 cluster deletion, from work around Green, Koch and colleagues) gives a barrier defect and blistering phenotype. These do not model the autoimmune phase. I would check the exact model citation before recording it.
- **Active-disease and immunization models.** Adoptive transfer of splenocytes into Rag2-null mice works well in PV (Dsg3 model). A comparable robust chronic model for PF is not established. This is the main limitation.
- **In vitro and ex vivo.** Human keratinocytes (HaCaT, primary NHEK) with dispase-based dissociation assays, human skin explants, and organotypic cultures. Signalling (p38, Src, EGFR) is studied in these systems.
- **Cellosaurus and MGI** identifiers were not pulled. Search them before recording.

---

## Curation Cautions

- **PF vs PV.** Do not merge them. They are separate entries by antigen (Dsg1 vs Dsg3) and by topography. The desmoglein compensation theory is the reason.
- **Endemic FS vs sporadic PF.** Curate FS as a subtype of PF, since it shares the antigen but differs in trigger and epidemiology.
- **Evidence sources.** Rituximab and consensus statements are `HUMAN_CLINICAL`. Passive transfer in neonatal mice is `MODEL_ORGANISM`, and keratinocyte assays are `IN_VITRO`. Do not let the mouse work carry the human phenotypes alone.
- **Mechanism nodes.** Pathogenic vs non-pathogenic anti-Dsg1 epitope shifts should be separate nodes. The exact split between steric and signalling mechanisms is unresolved and belongs in a knowledge-gap discussion. The Dsg1 depletion role of p38 was contested in some models.
- **Genes.** Confirm `hgnc:3048` for DSG1 and check it against the entry text before binding.
- **Gaps.** Omics profiling, per-phenotype QoL, PF-specific survival numbers, and PF-specific trial results were not established here.

## Reference Validation

No PMID or DOI references were found in this report.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0019324` (2 mentions) - the report calls it "given in the template; confirm the label"; MONDO calls it **pemphigus foliaceus**