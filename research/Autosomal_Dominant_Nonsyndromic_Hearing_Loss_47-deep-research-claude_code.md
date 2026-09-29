---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-24T19:50:15.694708'
end_time: '2026-09-24T19:53:44.278850'
duration_seconds: 208.58
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Autosomal Dominant Nonsyndromic Hearing Loss 47
  mondo_id: MONDO:0012090
  category: Mendelian
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
  web_search_requests: 9
  num_turns: 18
  total_cost_usd: 1.2292201999999999
  session_id: c3b3f1c9-a24d-5e2f-85c1-b82995c77b75
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 9
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 7
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 17
  verified: 15
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 0
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0012090
    reported_labels:
    - MONDO
    ontology_label: autosomal dominant nonsyndromic hearing loss 47
  - term_id: UBERON:0001846
    reported_labels:
    - cochlea
    ontology_label: internal ear
  - term_id: CL:0000201
    reported_labels:
    - auditory hair cell
    ontology_label: CL_0000201
  obsolete_terms:
  - term_id: CL:0000201
    ontology_label: CL_0000201
    replaced_by: CL:0000202
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Nonsyndromic Hearing Loss 47
- **MONDO ID:** MONDO:0012090 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Nonsyndromic Hearing Loss 47** covering all of the
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

# Autosomal Dominant Nonsyndromic Hearing Loss 47 (DFNA47) — Comprehensive Research Report

## Executive Summary

DFNA47 (OMIM `608652`; MONDO:0012090; ORPHA:90635) is a **genetic locus, not yet a gene**, for autosomal dominant nonsyndromic (isolated) sensorineural hearing loss. It was mapped by linkage analysis to chromosome **9p21–p22** in a single large multigenerational Italian family by D'Adamo et al. (2003), and **the causative gene has never been identified** in the more than two decades since — the most recent comprehensive DFNA review (2023) still lists DFNA47 as "unknown gene."[¹](#ref1) This fundamentally shapes what can be reported: sections on genetics, molecular mechanism, biomarkers, targeted treatment, and animal models are necessarily sparse or absent, and that absence is itself the key finding to document faithfully rather than to paper over with inference. Where the source template's search prompts point toward genes such as *MYO1A*, that gene is in fact linked to a **different** locus (DFNA48, 15q22-q25), and this report flags that distinction explicitly to avoid the exact kind of cross-locus confusion the dismech ontology-term contract warns against.

---

## 1. Disease Information

**Overview.** DFNA47 is an autosomal dominant, postlingual, progressive, nonsyndromic (isolated) sensorineural hearing loss (SNHL). It was described in a single large Italian kindred; affected individuals have no other associated abnormalities — hearing loss is the sole phenotype, with no vestibular, ophthalmologic, renal, or other systemic involvement reported.[¹](#ref1)[²](#ref2)

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | `608652` — DEAFNESS, AUTOSOMAL DOMINANT 47; DFNA47 (a locus-designation "number sign"-less entry, denoting a mapped-but-gene-unknown phenotype)[²](#ref2) |
| MONDO | MONDO:0012090 |
| Orphanet | ORPHA:90635 |
| Gene Symbol | **Not established** — no causal gene has been cloned |
| Cytogenetic locus | 9p21–p22 (also cited as 9p22-p21) |
| Physical interval (GRCh37/hg19, per Shahin et al. 2010) | approximately chr9:13,046,167–21,980,675 |
| ICD-10 | H90.5 (Unspecified sensorineural hearing loss) or H90.3 (Bilateral sensorineural hearing loss) — no DFNA47-specific code exists |
| MeSH | D003638 (Deafness) / D006319 (Hearing Loss, Sensorineural) — no locus-specific term |

**Synonyms/alternative names:** DEAFNESS, AUTOSOMAL DOMINANT 47; DFNA47 locus; progressive postlingual autosomal dominant nonsyndromic hearing loss (9p21-p22-linked).

**Source of information:** All disease-level knowledge derives from **aggregated, published pedigree/linkage data**, not individual-patient EHR data — specifically one extended Italian family reported in a single primary linkage paper (D'Adamo et al., 2003), subsequently catalogued in locus databases (OMIM, Hereditary Hearing Loss Homepage, Orphanet) and cited in review literature. No subsequent independent family or cohort has been reported as linked to this locus, so the evidentiary base is unusually narrow — essentially n = 1 family.

---

## 2. Etiology

**Disease causal factor:** Purely genetic — an autosomal dominant mendelian trait mapped to 9p21–p22 with complete penetrance in the reported family. The causal gene/variant is unknown.

**Genetic risk factors:**
- Inheriting the disease haplotype at the 9p21-p22 DFNA47 interval from an affected parent (autosomal dominant, one copy sufficient).
- No specific pathogenic variant, susceptibility allele, or modifier locus has been published, because the gene itself has not been cloned.
- **Possible allelism with DFNB83** (a recessive nonsyndromic hearing-loss locus): Shahin et al. (2010) mapped DFNB83 to a 16.5-Mb interval on 9p23–p21.2 in a consanguineous Palestinian family and noted this interval **encompasses** the DFNA47 region, raising the hypothesis that different mutation types (loss-of-function vs. dominant-negative/gain-of-function) in the same still-unidentified gene could underlie both the recessive (DFNB83) and dominant (DFNA47) phenotypes.[³](#ref3) This is a genotype-driven allelic-series hypothesis, not a confirmed finding — the gene for DFNB83 has also not been definitively cloned in the public literature reviewed here.

**Environmental risk factors:** None reported or plausible as a primary cause — this is described as a fully penetrant monogenic trait. No published data associate noise exposure, ototoxic drugs, or other environmental modifiers with age of onset or severity in this specific family.

**Protective factors:** None reported (genetic or environmental) — not applicable given the small literature.

**Gene-environment interactions:** Not studied for DFNA47 specifically; no data available.

---

## 3. Phenotypes

The **sole phenotype domain affected is hearing** — DFNA47 is explicitly nonsyndromic. The original description (D'Adamo et al., 2003) and subsequent OMIM/review synopses converge on:

| Phenotype | Type | HPO term (suggested) | Onset | Severity/progression | Frequency in family |
|---|---|---|---|---|---|
| Progressive sensorineural hearing loss | Clinical sign/symptom | **HP:0000407** Sensorineural hearing impairment | Audiometric abnormality detectable age 20–25 yr; subjectively noticed age 30–35 yr | Progressive: initially high-frequency, later spreading to mid/low frequencies; moderate-to-severe by ~age 50 | Fully penetrant in affected branches of the pedigree |
| High-frequency-predominant hearing loss (early stage) | Audiometric configuration | **HP:0000407** (general) / audiometric "sloping/downsloping" configuration is a clinical descriptor, not a distinct HPO term | 2nd–3rd decade | Mild-to-moderate initially | — |
| Postlingual onset (language already acquired before hearing loss) | Temporal qualifier | **HP:0000403**-adjacent concept (postlingual onset is typically captured via onset-age slots rather than a dedicated HPO term) | By definition, after speech acquisition | — | — |
| Absence of vestibular dysfunction | Negative finding | (Absence of **HP:0000737** Vestibular dysfunction) | N/A | Not present | Explicitly noted as absent in the reported family |

**Characteristics:**
- **Age of onset:** Adult-onset (2nd–3rd decade for audiometric detection; symptomatic recognition somewhat later, 3rd–4th decade).
- **Severity:** Variable but consistently progressive — mild/high-frequency-only in young adulthood, evolving to moderate-to-severe pantonal loss by the 5th decade.
- **Progression:** Progressive (not stable, not episodic) — a classic "sloping-worsening-to-flat" audiometric trajectory over decades.
- **Frequency among affected individuals:** Fully penetrant — every gene-carrier in the reported pedigree was reported as eventually affected (penetrance described as complete, distinguishing it from many other DFNA loci with age-dependent incomplete penetrance).

**Quality-of-life impact:** Not formally measured in the primary literature (no EQ-5D, SF-36, or hearing-specific QoL instrument data published for this specific cohort). By inference from the general adult-onset progressive SNHL literature, such presentations are associated with progressive communication difficulty, and — because onset is postlingual and gradual — patients typically retain spoken language but experience increasing functional impairment (speech-in-noise difficulty, social withdrawal risk) as the loss becomes moderate-to-severe in the 5th decade. No disease-specific QoL study exists.

**No other organ systems, syndromic features, developmental abnormalities, or laboratory abnormalities have been reported.**

---

## 4. Genetic/Molecular Information

This section is the most constrained by the state of the science.

- **Causal gene:** **Unidentified.** No gene has been cloned, validated, or widely accepted as the DFNA47 gene despite the locus having been mapped in 2003. The 2023 comprehensive DFNA review (PMC10296186) explicitly lists the gene status for DFNA47 as "Unknown gene."[¹](#ref1)
- **Locus/candidate interval:** 9p21–p22; narrowed by recombinant analysis in the original family to an approximately 9-cM interval between microsatellite markers **D9S268** and **D9S942**, with peak linkage (LOD = 3.67 at θ = 0.0) at marker **D9S162**.[⁴](#ref4)
- **Overlapping recessive locus:** DFNB83 (OMIM `613685`), mapped by Shahin et al. (2010) to a 16.5-Mb region on 9p23–p21.2 (LOD = 3.07, markers rs4742645–rs1471364) in a consanguineous Palestinian family, is reported to physically encompass the DFNA47 interval (~chr9:13,046,167–21,980,675), suggesting the two loci may represent **allelic disorders** of one still-uncloned gene.[³](#ref3) This remains a hypothesis, not a demonstrated fact — no shared causal variant has been published.
- **Pathogenic variants:** None reported — there is no ClinVar, HGMD, or gnomAD entry attributable to "the DFNA47 gene" because no such gene designation exists in variant databases.
- **A note on MYO1A** (flagged specifically because the research-template's search prompts for this section would otherwise lead a curator toward it): *MYO1A*, a cochlear-expressed unconventional myosin gene, **was** reported by Donaudy et al. (2003, PMID:12736868) to carry multiple mutations (one nonsense, one in-frame trinucleotide insertion, six missense) in Italian patients with moderate-to-severe (never profound) bilateral SNHL.[⁵](#ref5) However, *MYO1A* maps to chromosome **15q22-q25** and is associated with locus **DFNA48**, not DFNA47 — the two loci are numerically adjacent but genetically and cytogenetically distinct. Furthermore, the *MYO1A*-deafness association itself has since been substantially **refuted**: a 2016 genotypic-ascertainment study (Eisenberger et al./Lee et al., PMID:27759032, *Eur J Hum Genet*) found the originally reported *MYO1A* variants also present in unaffected controls and in individuals whose hearing loss was better explained by pathogenic variants in other, well-established deafness genes, concluding *MYO1A* variants are not a convincing cause of nonsyndromic deafness.[⁶](#ref6) **DFNA47 curators should not bind this entry's causal gene to MYO1A** — that would conflate two different OMIM loci and cite evidence for a claim now considered unsupported in the literature.
- **Modifier genes, epigenetics, chromosomal abnormalities:** No data published for DFNA47.
- **Functional consequences:** Cannot be characterized (variant type, LOF vs. GOF, dominant-negative mechanism) because no variant has been identified.

**Suggested ontology bindings for the locus/phenotype layer (not gene layer, since none exists):**
- Phenotype: **HP:0000407** (Sensorineural hearing impairment)
- Mode of inheritance: **HP:0000006** (Autosomal dominant inheritance)
- Onset: **HP:0011462** (Young adult onset) or **HP:0003621** (Juvenile onset) depending on how audiometric-vs-symptomatic onset ages are modeled

---

## 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents have been reported as contributing to or modifying DFNA47. As a fully penetrant monogenic trait in the single reported family, environmental influence on penetrance/expressivity was not a subject of the original study and has not been investigated since. Not applicable / no data.

---

## 6. Mechanism / Pathophysiology

**Causal chain (as currently understood — heavily inferred, since the gene is unknown):**

1. An as-yet-unidentified dominant pathogenic variant at the 9p21–p22 locus is inherited (autosomal dominant, fully penetrant) → **[inferred, not demonstrated]**
2. The variant is presumed to disrupt a gene product expressed in, or required for maintenance of, cochlear sensory or supporting cells (by analogy to essentially all other cloned DFNA genes, which encode structural, motor, ion-channel, or transcriptional proteins active in the organ of Corti, stria vascularis, or spiral ganglion) → **[inferred by analogy; no direct evidence for DFNA47 specifically]**
3. Progressive cochlear dysfunction develops with age, beginning in the basal (high-frequency-encoding) turn of the cochlea — consistent with the clinical audioprofile of initial high-frequency loss — and spreading apically over decades to involve mid- and low-frequency hearing → **[clinically observed, mechanistically unexplained]**
4. This manifests as postlingual, progressive sensorineural hearing loss reaching moderate-to-severe severity by the 5th decade, with the vestibular end-organ spared (no reported vestibular dysfunction), implying any underlying cellular process is either cochlea-restricted or has a threshold effect not reached in the vestibular system → **[clinical observation]**

Because no gene, transcript, or protein has been identified, **none** of the following can be populated with disease-specific data:
- Molecular pathways (no KEGG/Reactome pathway can be assigned to an unknown gene)
- Cellular processes / GO biological process terms
- Protein structure/dysfunction (misfolding, LOF, GOF, dominant-negative)
- Metabolic changes
- Immune involvement (none expected/reported for a nonsyndromic SNHL locus)
- Tissue damage mechanisms at the molecular level
- Biochemical abnormalities
- Epigenetic changes
- Any -omics profiling (transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial) — no such studies exist for this locus, since there is no gene or model system to study
- Functional genomic screens

The only mechanistic inference that can be responsibly drawn from the clinical phenotype alone is the **general pattern typical of progressive DFNA loci**: a high-frequency-first, base-to-apex progression consistent with basal cochlear outer/inner hair cell vulnerability, by analogy with better-characterized dominant progressive SNHL genes (e.g., *TECTA*, *COCH*, *WFS1*), but this is **pattern-matching, not evidence specific to DFNA47**, and should not be curated as a mechanistic claim without an explicit caveat.

**Suggested ontology terms** for a maximally conservative (phenotype-level only) pathophysiology annotation:
- **UBERON:0001846** (cochlea) as the presumed affected structure
- **GO:0007605** (sensory perception of sound) as the disrupted process at the organismal level
- **CL:0000201** (auditory hair cell) — candidate cell type by analogy to other DFNA loci, but unconfirmed for this specific locus

---

## 7. Anatomical Structures Affected

- **Organ level:** Primary organ affected — the inner ear (cochlea); specifically the auditory portion (organ of Corti). Secondary organ involvement: none reported. Body system: auditory/special sensory system only (nonsyndromic).
- **Tissue/cell level:** Presumed cochlear sensory epithelium (hair cells) and/or supporting structures (stria vascularis, spiral ligament, spiral ganglion), by analogy with other progressive DFNA phenotypes — **not directly demonstrated** for DFNA47, since no histopathology, temporal bone study, or animal model exists for this locus.
  - Suggested CL term (candidate, unconfirmed): CL:0000201 (auditory hair cell)
- **Subcellular level:** Cannot be specified — no molecular target known.
- **Localization:** Bilateral (both cochleae affected symmetrically, consistent with a germline dominant trait); UBERON:0001846 (cochlea). No lateralization/asymmetry reported.

---

## 8. Temporal Development

- **Onset:** Adult-onset — audiometric threshold changes first detectable around age 20–25 years; subjective symptom awareness around age 30–35 years. Onset pattern is insidious/gradual, not acute.
- **Progression:** Slowly progressive over decades. Disease "stages" are not formally defined (no published staging system specific to DFNA47), but the natural history can be summarized as three informal phases:
  1. Subclinical/early audiometric — high-frequency threshold elevation, 2nd–3rd decade, often asymptomatic
  2. Symptomatic progressive — 4th decade, expanding to mid frequencies, noticeable functional impact
  3. Established moderate-to-severe pantonal loss — by the 5th decade (~age 50)
- **Disease course pattern:** Progressive, not relapsing-remitting or episodic. Lifelong/chronic — no spontaneous remission reported.
- **Critical periods:** None identified; because onset is postlingual, spoken language acquisition is not at risk, distinguishing DFNA47 clinically from prelingual/congenital deafness loci where early intervention windows are critical.

---

## 9. Inheritance and Population

- **Epidemiology:** No population-level prevalence or incidence estimate exists. DFNA47 has been reported in essentially one large Italian family; it has not been shown to be a recurrent or population-relevant cause of hearing loss elsewhere, and no locus-specific frequency data appear in Orphanet, GBD, or national registries. Reasonable to classify as **ultra-rare** (single-family report), but this is a qualitative judgment rather than a sourced numeric estimate.
- **Inheritance pattern:** Autosomal dominant (**HP:0000006**).
- **Penetrance:** Reported as **complete/fully penetrant** in the index family — an unusual and notable feature relative to many other adult-onset DFNA loci, which more commonly show age-dependent, incomplete penetrance.
- **Expressivity:** Variable age of onset within the fully penetrant pedigree (audiometric onset 20–25 yr vs. subjective onset 30–35 yr) suggests some variable expressivity in timing, though ultimate severity (moderate-to-severe by age 50) appears consistent across affected members.
- **Genetic anticipation:** Not reported/assessed.
- **Germline mosaicism:** Not reported.
- **Founder effect:** Plausibly relevant, given the single-family, geographically restricted (central/southern Italy region, per the original cohort's ascertainment) origin, but no explicit founder-haplotype study has been published for DFNA47 specifically.
- **Consanguinity:** Not a factor — dominant trait, and the original family was ascertained through multigenerational dominant transmission, not consanguinity (contrast with the recessive DFNB83 family, which was consanguineous).
- **Carrier frequency:** Not applicable in the classic sense for a dominant, fully penetrant trait with unknown gene (no population carrier-frequency data exist).
- **Population demographics:** Only known affected population is the original Italian kindred; no data on other ethnic groups, geographic distribution of the (unknown) variant, sex ratio, or age distribution beyond what is captured in the onset/progression data above.

---

## 10. Diagnostics

- **Clinical tests:**
  - Pure-tone audiometry is the primary diagnostic tool, demonstrating the characteristic high-frequency-initial, progressively pantonal, sloping-to-flat sensorineural configuration.
  - No disease-specific biomarker, imaging finding, or histopathological signature has been published.
  - Vestibular testing has been reported as normal in affected individuals (used to support the "nonsyndromic, cochlea-restricted" classification).
- **Genetic testing:** Because no causal gene is known, there is **no commercially or clinically available single-gene or targeted test for "DFNA47."** Diagnosis in a new family suspected of DFNA47-type presentation would in practice proceed via:
  - Comprehensive hearing-loss gene panel or clinical exome/genome sequencing (to identify pathogenic variants in the ~150+ known nonsyndromic deafness genes) — used to **exclude** known genes;
  - Linkage/segregation analysis to the 9p21-p22 interval **only** if a large, informative, multigenerational pedigree is available — impractical for isolated cases or small families;
  - A diagnosis of "DFNA47" today would essentially be a diagnosis of exclusion plus locus-consistent linkage evidence, not a positive molecular diagnostic result.
  - GTR (Genetic Testing Registry) does not list a validated single-gene assay for this locus, consistent with the absence of a cloned gene.
- **Omics-based diagnostics:** Not applicable — no validated RNA-seq, proteomic, or liquid-biopsy diagnostic exists or would be expected for a nonsyndromic nuclear nervous-system-sparing trait.
- **Clinical criteria:** No formal consensus diagnostic criteria specific to DFNA47 exist; diagnosis rests on (a) clinical pattern (autosomal dominant, postlingual, progressive, high-frequency-first bilateral SNHL, no syndromic features), (b) exclusion of known deafness genes, and, ideally, (c) demonstration of linkage to 9p21-p22 in a sufficiently large pedigree.
- **Differential diagnosis:** Broad — essentially all other progressive autosomal dominant nonsyndromic hearing-loss loci with adult onset and high-frequency-first audioprofiles (e.g., DFNA2/*KCNQ4*, DFNA8/12/*TECTA*, DFNA9/*COCH*, DFNA10/*EYA4*, DFNA20/26/*ACTG1*, DFNA48/*MYO1A*-associated phenotype) must be excluded by molecular testing, since audioprofile alone cannot distinguish DFNA47 from these better-characterized entities.
- **Screening:** No newborn or population screening applicable — this is adult-onset, and there is no test to screen for it specifically. Standard newborn hearing screening protocols (which target congenital/early-onset hearing loss) would not detect DFNA47, consistent with its postlingual onset.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** Not a life-limiting condition; no mortality data relevant (isolated SNHL does not affect survival).
- **Morbidity/function:** Progressive functional hearing impairment; by the 5th decade, moderate-to-severe bilateral SNHL is expected in all penetrant carriers, with attendant communication difficulty. No formalized disability outcome or QoL instrument data published for this specific locus.
- **Disease course:** No complications beyond the hearing impairment itself have been reported (nonsyndromic — no cardiac, renal, ophthalmologic, or neurologic sequelae). No spontaneous recovery is described or expected, consistent with a progressive sensorineural (rather than conductive/reversible) process.
- **Prognostic factors:** The main "prognostic" information available is the pedigree-derived natural history itself (age-linked severity milestones, above) rather than any biomarker-based prognostic model.
- **Prognostic biomarkers:** None identified.

---

## 12. Treatment

There is **no disease-specific (mechanism-targeted) treatment** for DFNA47, because there is no known molecular target. Management is the standard supportive/rehabilitative approach used for any progressive sensorineural hearing loss:

- **Pharmacotherapy:** None specific; no drug is indicated for the underlying cause. (NCIT: not applicable for a causal pharmacotherapy; general audiologic pharmacotherapy is not disease-modifying here.)
- **Advanced therapeutics:**
  - Gene therapy: none developed or in trials for DFNA47 specifically (impossible without a known target gene). General inner-ear gene-therapy platforms under investigation for other, gene-defined SNHL forms (e.g., *OTOF*-related deafness) are not applicable here.
  - Cell therapy, RNA-based therapy, targeted/immunotherapy: not applicable — no molecular target exists.
- **Surgical/interventional:** **Cochlear implantation** (NCIT:C15329, Surgical Procedure, as the general clinical-action binding; the device itself, NCIT:C157820 Cochlear Implant, would be recorded as a `qualifiers` device annotation per this repository's convention) would be the expected intervention once hearing loss becomes severe-to-profound and hearing aids are no longer sufficient — this is a standard-of-care inference for progressive SNHL generally, not a DFNA47-specific outcome study.
- **Supportive/rehabilitative:**
  - Hearing aid amplification (NCIT:C — no precise device-class NCIT term for "hearing aid" is available in this repository's ontology per the MAXO-removal note; would require a `qualifiers` device pattern analogous to cochlear implants) is the standard first-line intervention as the high-frequency loss becomes functionally significant.
  - Audiologic rehabilitation / speech-in-noise strategies, aural rehabilitation (NCIT:C15302 Physical Therapy is not a precise fit; NCIT:C159273 Speech-Language Therapy or general "Rehabilitation," NCIT:C15315, would be the closer generic binding for auditory rehabilitation counseling).
- **Experimental:** No DFNA47-specific clinical trials identified on ClinicalTrials.gov or WHO ICTRP.
- **Treatment outcomes:** No disease-specific data on hearing-aid or cochlear-implant outcomes in DFNA47 carriers (as distinct from general adult-onset progressive SNHL populations) have been published.
- **Treatment strategy / personalized medicine:** Not applicable — genotype-guided treatment is impossible without a known gene.

---

## 13. Prevention

- **Primary prevention:** Not possible for a fully penetrant monogenic trait once inherited; no risk-factor modification applies (no environmental cause identified).
- **Secondary prevention (early detection):** Periodic audiometric monitoring of at-risk relatives (known carriers or first-degree relatives of affected individuals in the index pedigree) beginning in the 2nd decade would be a reasonable clinical recommendation by analogy with other adult-onset progressive DFNA loci, allowing earlier initiation of amplification — but this is inferred general practice, not a published DFNA47-specific screening protocol.
- **Tertiary prevention:** Early hearing-aid fitting once threshold changes are detected, to minimize functional/communicative impact and reduce risk of auditory deprivation effects.
- **Immunization:** Not applicable (not an infectious or immune-mediated condition).
- **Genetic screening:** Because no gene is cloned, no targeted prenatal, carrier, or preimplantation genetic test exists for DFNA47. In a family with established linkage, haplotype-based predictive testing (linked-marker segregation analysis) is theoretically possible but has not been reported as clinically implemented, and would require careful genetic counseling given its indirect (linkage-based, not variant-based) nature.
- **Genetic counseling:** Standard autosomal dominant counseling principles apply — 50% transmission risk to offspring of an affected individual, complete penetrance implying essentially all gene-carriers will eventually be affected (unlike many incompletely penetrant DFNA loci).
- **Public health / environmental interventions:** Not applicable — no environmental contributor identified.
- **Prophylaxis:** None available.

---

## 14. Other Species / Natural Disease

No orthologous gene can be discussed because the human gene itself is unknown. Consequently:

- **Taxonomy:** Not applicable (no gene to compare across species; NCBITaxon:9606 Homo sapiens is the only relevant taxon for this entry).
- **Breed:** No naturally occurring veterinary correlate has been linked to this human locus.
- **Orthologous gene:** Cannot be identified.
- **Natural disease in other species:** No OMIA (Online Mendelian Inheritance in Animals) entry corresponds to DFNA47, since OMIA cross-references are built from known human genes.
- **Comparative biology / evolutionary conservation:** Not assessable.
- **Zoonotic potential / cross-species susceptibility:** Not applicable (non-infectious, monogenic human trait).

---

## 15. Model Organisms

**No model organism (mouse, rat, zebrafish, Drosophila, C. elegans, yeast, cell line, organoid, or iPSC-derived system) has been developed or reported for DFNA47,** and none can be rationally engineered until the causal gene is identified — knockout, knock-in, transgenic, or humanized models all require a known target locus/gene. This is a direct and important consequence of the "gene unknown" status and should not be filled in by extrapolating from the retracted *MYO1A* literature or from other, unrelated DFNA loci's mouse models, since doing so would misattribute model evidence to this specific locus.

---

## Summary: What Can and Cannot Be Curated

| Category | Status |
|---|---|
| Locus, mapping, LOD score, markers | **Well-documented** (single primary source) |
| Clinical/audiometric phenotype, natural history | **Well-documented** (single primary source) |
| Causal gene | **Unknown** — do not bind to *MYO1A* (that is DFNA48) |
| Molecular mechanism, pathway, cell biology | **Not available** — any pathophysiology entry must be built at the phenotype/anatomical level only, explicitly flagged as inferred-by-analogy where used |
| Genetic testing / variant classification | **Not available** as a positive test; diagnosis is exclusion-based |
| Treatment | **Generic SNHL management only** (hearing aids, cochlear implantation) — no disease-modifying or targeted therapy |
| Model organisms | **None exist** |
| Epidemiology | **Single-family report only**; no population prevalence/incidence figure is sourced |

---

## References (with PMIDs where available)

1. <a id="ref1"></a>Comprehensive narrative review of autosomal dominant nonsyndromic hearing loss (DFNA), including summary table listing DFNA47 as 9p21–p22, gene unknown, adulthood (2nd–3rd decade) onset, sloping/progressive audioprofile reaching moderate-to-severe by the 5th decade. PMC10296186. https://pmc.ncbi.nlm.nih.gov/articles/PMC10296186/
2. <a id="ref2"></a>OMIM Entry `608652` — DEAFNESS, AUTOSOMAL DOMINANT 47; DFNA47. https://omim.org/entry/608652
3. <a id="ref3"></a>Shahin H, et al. (2010). Five novel loci for inherited hearing loss mapped by SNP-based homozygosity profiles in Palestinian families. *Eur J Hum Genet.* — reports DFNB83 (9p23-p21.2) overlapping the DFNA47 interval and proposes possible allelism. PMC2987250. https://pmc.ncbi.nlm.nih.gov/articles/PMC2987250/ ; OMIM DFNB83 entry `613685`. https://omim.org/entry/613685
4. <a id="ref4"></a>D'Adamo P, et al. (2003). A new locus (DFNA47) for autosomal dominant non-syndromic inherited hearing loss maps to 9p21-22 in a large Italian family. *Eur J Hum Genet.* PMID:12634859. https://pubmed.ncbi.nlm.nih.gov/12634859/ ; https://www.nature.com/articles/5200929
5. <a id="ref5"></a>Donaudy F, et al. (2003). Multiple mutations of MYO1A, a cochlear-expressed gene, in sensorineural hearing loss. *Am J Hum Genet.* PMID:12736868 — describes the **DFNA48**-associated gene *MYO1A* (15q22-q25); distinct from DFNA47. PMC1180318. https://pmc.ncbi.nlm.nih.gov/articles/PMC1180318/
6. <a id="ref6"></a>Genotypic ascertainment study refuting the association of *MYO1A* variants with nonsyndromic deafness. PMID:27759032. *Eur J Hum Genet.* https://www.nature.com/articles/ejhg2016140 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC5159773/

---

### Note on evidentiary limits

This report is transparent that DFNA47 is among the sparsest entries in the nonsyndromic hearing-loss nosology: essentially one primary linkage paper (2003), one secondary paper noting a possible overlapping recessive locus (2010), and citation in periodic review articles — with **no gene-level, mechanistic, diagnostic-test, treatment-specific, or model-organism literature existing at all**. Any dismech curation of this entry should reflect that honestly (an entry that is mostly locus/phenotype metadata with `notes:` explaining the absent gene, rather than an entry padded with inferred or cross-locus content) rather than manufacturing specificity — consistent with this repository's Ontology Term Contract's instruction to omit a field and record why, rather than fabricate a binding, when a claim cannot be sourced.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 17 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 3 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012090` (2 mentions) - the report calls it "MONDO"; MONDO calls it **autosomal dominant nonsyndromic hearing loss 47**
- `UBERON:0001846` (2 mentions) - the report calls it "cochlea"; UBERON calls it **internal ear**
- `CL:0000201` (2 mentions) - the report calls it "auditory hair cell"; CL calls it **CL_0000201**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `CL:0000201` (CL_0000201) (2 mentions) - replaced by `CL:0000202`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.