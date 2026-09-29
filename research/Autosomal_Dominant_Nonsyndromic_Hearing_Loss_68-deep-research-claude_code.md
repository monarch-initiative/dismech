---
provider: claude_code
model: claude-fable-5, claude-haiku-4-5-20251001
cached: false
start_time: '2026-09-19T02:11:15.995392'
end_time: '2026-09-19T02:14:57.619106'
duration_seconds: 221.62
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: DFNA68 HOMER2-related autosomal dominant nonsyndromic hearing loss
  mondo_id: MONDO:0014740
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
  - claude-fable-5
  - claude-haiku-4-5-20251001
  web_search_requests: 3
  num_turns: 8
  total_cost_usd: 4.644776
  session_id: 388812e5-0caf-48e6-a4af-a4443026502d
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 17
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 13
  validator_version: 0.2.1
term_validation:
  total_terms: 28
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 4
  labels_variant: 4
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** DFNA68 HOMER2-related autosomal dominant nonsyndromic hearing loss
- **MONDO ID:** MONDO:0014740 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **DFNA68 HOMER2-related autosomal dominant nonsyndromic hearing loss** covering all of the
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

I'll research DFNA68/HOMER2 hearing loss. I have a strong local resource — the curated dismech entry on this branch — plus web search for recent literature. Let me gather both.

# DFNA68: HOMER2-Related Autosomal Dominant Nonsyndromic Hearing Loss — Comprehensive Research Report

**Prepared:** 2026-09-19. Evidence base: the six primary DFNA68 family reports (2015–2026) plus the supporting mechanistic literature; all quoted snippets below are verified exact quotes from the cited abstracts/records.

---

## 1. Disease Information

**Overview.** DFNA68 is a bilateral, postlingual, progressive, nonsyndromic sensorineural hearing loss (SNHL) caused by heterozygous variants in *HOMER2*, which encodes a scaffolding protein of the Homer family enriched at the tips of cochlear hair cell stereocilia. Hearing is normal at birth and through early childhood; loss typically begins in the first or second decade at the high frequencies, producing a down-sloping audiogram that flattens as lower frequencies are drawn in, and deteriorates at a measured 1.2–1.6 dB/year until severe or profound. Fewer than ten unrelated families have been reported worldwide since the gene was identified in 2015 (PMID:25816005), making this one of the rarest characterized DFNA loci.

**Identifiers:**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | [#616707 — DEAFNESS, AUTOSOMAL DOMINANT 68; DFNA68](https://omim.org/entry/616707) |
| OMIM (gene) | [*604799 — HOMER SCAFFOLD PROTEIN 2; HOMER2](https://omim.org/entry/604799) |
| MONDO | MONDO:0014740 (autosomal dominant nonsyndromic hearing loss 68) |
| HGNC | hgnc:17513 (HOMER2) |
| Orphanet | No dedicated ORPHA code for DFNA68; it falls under the group concept [ORPHA:90635, autosomal dominant non-syndromic sensorineural deafness type DFNA](https://www.orpha.net/consor4.01/www/cgi-bin/OC_Exp.php?Expert=90635&lng=EN) |
| ICD-10 / ICD-11 | H90.3 / AB50 (at the DFNA group level, per Orphanet) |
| LOVD | [Disease #06261](https://databases.lovd.nl/shared/diseases/06261) |

**Synonyms:** DFNA68; deafness, autosomal dominant 68; autosomal dominant nonsyndromic deafness 68; HOMER2-related hearing loss.

**Data provenance:** All clinical information is aggregated from published family reports (pedigree/case-series literature), not EHR-derived. The entire clinical description rests on approximately six pedigrees plus one isolated patient.

Key primary literature (PMIDs): 25816005 (founding study, 2015); 30047143 (second family, Chinese, 2018); 33809266 (Spanish family, 2021); 37173411 (nonstop variant, 2023); 40515814 (frameshift extension + cochlear implant outcome, 2025); 41351289 (Chinese four-generation family, 2026).

## 2. Etiology

**Causal factor:** Purely genetic — heterozygous germline variants in *HOMER2* (15q24.3; OMIM places it at 15q25). No environmental, infectious, or lifestyle cause or modifier has been reported in any DFNA68 family.

**Critically, this is not a haploinsufficiency disease.** Three independent lines of evidence converge:
- Mice heterozygous for a *Homer2* null hear normally; only the homozygous null is deaf (PMID:25816005; restated in PMID:33809266: *"mice heterozygous for the targeted deletion of exon 3 in Homer2 (Homer−/+) displayed normal hearing levels"*).
- *HOMER2* is tolerant of loss-of-function variation in population data: *"Low pLI score (0.01) of HOMER2 suggests that alteration of HOMER2 exerts a pathogenic effect via a mechanism other than loss-of-function"* (PMID:40515814).
- The founding allele was shown experimentally to act as a dominant negative: zebrafish mutant-mRNA injection produced an ear phenotype while knockdown of the endogenous gene did not (PMID:25816005).

**Risk factors:** Being an obligate carrier in an affected family (50% transmission risk). No susceptibility loci, modifier genes, protective variants, or gene–environment interactions have been reported. No known environmental risk or protective factors specific to this disorder (standard noise/ototoxin avoidance advice for any progressive SNHL applies on general principles only — not disease-specific evidence).

## 3. Phenotypes

The phenotype is essentially monosymptomatic. Suggested HPO annotations with frequencies (frequencies reflect the small reported family set, not measured cohort proportions):

| Phenotype | HPO term | Frequency | Characteristics |
|---|---|---|---|
| Progressive sensorineural hearing impairment | HP:0000408 | Obligate | Defining feature; bone conduction excluded conductive loss; reaches severe/profound |
| Postlingual onset | HP:0008596 | Obligate | Normal speech acquisition; onset 1st–2nd decade typically, 17–24 years in one family, 50s in one patient |
| Bilateral involvement | HP:0008619 | Obligate | Binaural symmetry verified in the founding family |
| High-frequency-onset, down-sloping loss | HP:0001757 | Very frequent | Characteristic audiogram; flattens with progression |
| Low-frequency (ascending) loss at presentation | HP:0008573 | Very rare | One proband (18 y); authors read it as a stage effect: *"the different forms of auditory configuration may present different stages of the disease"* (PMID:41351289) |
| Tinnitus | HP:0000360 | Occasional | Present in some members of two families, explicitly absent in two others (PMID:33809266, PMID:41351289) |

Key supporting quotes: *"Hearing impairment had a typical onset in the first decade of life in the high frequencies, with significant subsequent progression of hearing loss over all frequencies"* and *"The resulting annual threshold deterioration (ATD) was 1.2 to 1.6 dB per year"* (PMID:25816005).

**Substantive negatives (actively tested, not just unreported):**
- **No vestibular dysfunction:** *"Tandem gait and Romberg tests did not reveal any symptoms of vestibular dysfunction in all family members"* (PMID:41351289).
- **No syndromic features:** *"Clinical examination was negative for any findings consistent with syndromic hearing loss and also ruled out autoimmune phenotypes"* (PMID:25816005). Intelligence and speech normal (PMID:41351289).

**Quality of life:** Documented at the severe end: one patient reached 8% bilateral speech discrimination ten years after significant progression began, requiring cochlear implantation (PMID:40515814). No formal QoL instrument (EQ-5D/SF-36) data exist for this disorder.

## 4. Genetic/Molecular Information

**Gene:** *HOMER2* (hgnc:17513; OMIM *604799), chromosome 15q24.3, nine exons, two transcripts encoding 343-residue (NM_004839) and 354-residue (NM_199330) isoforms. **Nomenclature trap:** both numbering systems appear in the literature for the same variants — the founding missense is p.Arg185Pro (isoform 1) and p.Arg196Pro (isoform 2); these are one allele, not two.

**Protein architecture:** N-terminal EVH1 domain (binds proline-rich motifs) + C-terminal coiled-coil (CC) domain that (a) drives tetramerization and (b) carries the CDC42-binding domain (CBD, ~residues 191–283; mapped in neurons, PMID:19309525).

**Reported pathogenic variants — three mechanistic classes** (all germline, heterozygous; ~6–7 variants in fewer than ten families; the two published tallies — "five variants" in PMID:41351289 vs "seventh variant" in PMID:40515814 — disagree by one and were never reconciled):

1. **Coiled-coil missense (dominant negative):** c.554G>C, p.Arg185Pro/p.Arg196Pro (European kindred, PMID:25816005). *"These results show that HOMER2 plays an essential role in the normal development and/or maintenance of hair cells in the zebrafish inner ear and that the p.Arg185Pro mutation has a dominant-negative effect on this process."*
2. **Frameshift truncations within the CDC42-binding domain (dominant negative / possible GoF):** c.840_841insC (Chinese, PMID:30047143) and a five-base deletion producing p.Pro278Alafs\*10 (Spanish, PMID:33809266). The truncated product shows *"decreased protein stability, reduced ability to multimerize, and altered distribution pattern in transfected cells."* The Spanish authors explicitly leave open whether the mechanism is *"a gain-of-function of the Ct aberrant tail or ... a dominant-negative mechanism."*
3. **C-terminal extension variants (argued gain-of-function):** nonstop c.1064A>G converting the stop codon to tryptophan (+10 residues; transcripts escape nonstop decay, PMID:37173411); c.1033delC p.Arg345Glufs\*64 (+~64 residues; PMID:40515814 — *"Our findings reveal a solid pathogenic gain-of-function effect related to the long extension to the C-terminal of HOMER2"*); c.1023_1029del p.Asp342ArgfsTer54 (PMID:41351289). AlphaFold2 predicts the longest extension disrupts the distant EVH1 domain and its Cdc42 interface while preserving multimerization (computational, not measured).

**Population frequency:** Disease alleles are absent/ultra-rare in population databases; the gene itself tolerates LoF (pLI 0.01), which is the population-genetic argument against haploinsufficiency.

**Modifiers, epigenetics, chromosomal abnormalities:** None reported. No recessive *HOMER2* patient has been reported, despite the founding authors' prediction: *"The recessive phenotype exhibited by null alleles of Homer2 makes it a strong candidate for autosomal recessive hearing loss due to loss of function in humans as well"* (PMID:25816005) — still open a decade later.

## 5. Environmental Information

Not applicable. No environmental, lifestyle, or infectious contributor has been reported in any DFNA68 family. This is a fully penetrant-appearing Mendelian mechanosensory disorder as described (though formal penetrance quantification is lacking — see §9).

## 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinic):**

1. A heterozygous *HOMER2* variant (missense in the coiled coil, frameshift truncation in the CDC42-binding domain, or C-terminal extension) **produces** a mutant scaffold protein that is expressed, not eliminated (NMD escape shown/inferred for the extension and truncation classes).
2. The mutant protein **interferes with** wild-type HOMER2 — impairing tetramer assembly for the missense/truncation classes (demonstrated in vitro for the truncation: reduced multimerization, instability, mislocalization), or **adding** an aberrant C-terminal tail (extension class; gain-of-function argued from a designed zebrafish truncation-vs-extension comparison). *This step is why the disease is dominant despite a phenotype-free null heterozygote.*
3. Defective scaffold hubs **lead to** disrupted HOMER2–CDC42 coupling at the stereocilia (the CBD sits inside the coiled coil; for the extension class, the route is a *predicted* EVH1 conformational change) — **inferred, not demonstrated**: no binding assay exists for any disease allele, and no HOMER2–CDC42 complex has been shown in a cochlear hair cell.
   - **Branch (alternative/parallel hypothesis):** impaired scaffolding **leads to** dysregulated hair-cell calcium handling via Homer's regulation of PMCA pumps and TRPC channels — **hypothetical**: the one real measurement is in mouse parotid gland (PMID:25049230), PMCA2 being *"the only system for clearance of Ca2+ from hair cell stereocilia"* is what makes it attractive (PMID:25816005), and the established Homer2 TRPC partner (TRPC1) is not the TRPC3/TRPC6 hair cells use. The founding paper named both hypotheses and *"further functional studies are needed"* — nothing since has closed them.
4. Loss of CDC42-tuned actin turnover **results in** failure of stereocilia maintenance — bundles form normally, then deteriorate. **Inferred by analogy:** hair-cell-specific *Cdc42* knockout mice show exactly this: *"Hair cells of Atoh1-Cre;Cdc42(flox/flox) mice developed normally but progressively degenerated after maturation, resulting in progressive hearing loss particularly at high frequencies"*, beginning as *"stereocilia fusion and depletion"* (PMID:24610943). No stereocilia morphology has been reported for any HOMER2 patient or model.
5. Bundle failure **results in** hair-cell functional failure *without hair-cell death* — the mechanistically distinctive claim, and the step the models actually establish: the homozygous null mouse is profoundly deaf with a full complement of inner and outer hair cells at 8 weeks (*"No differences in IHCs and OHCs were observed in any animals regardless of genotype"*, PMID:25816005), and zebrafish injected with disease alleles show *"severely impaired ... capacity of neuromast hair cells to uptake FM1-43"* with *"no significant differences in hair cell numbers"* (PMID:40515814).
6. Failed mechanotransduction **leads to** progressive bilateral sensorineural hearing loss, postlingual, high-frequency-first, at 1.2–1.6 dB/year — the clinical endpoint.

**Ontology suggestions:** GO:0097110 scaffold protein binding; GO:0051289 protein homotetramerization; GO:0031267 small GTPase binding; GO:0030036 actin cytoskeleton organization; GO:0060088 auditory receptor cell stereocilium organization; GO:0051480 regulation of cytosolic calcium ion concentration; GO:0050910 detection of mechanical stimulus involved in sensory perception of sound; GO:0007605 sensory perception of sound; cellular components GO:0032420 stereocilium, GO:0032426 stereocilium tip; cell types CL:0000589 cochlear inner hair cell, CL:0000601 cochlear outer hair cell.

**No molecular profiling** (transcriptomics, proteomics, metabolomics, single-cell) has been published for this disorder specifically.

## 7. Anatomical Structures Affected

- **Organ:** inner ear / cochlea only (UBERON:0001846 internal ear; UBERON:0001844 cochlea; UBERON:0002227 organ of Corti). No secondary organ involvement in any patient (a zebrafish cardiac signal for the longest extension allele is an open question — the patient carrying it had no cardiac abnormality; see §11/§15).
- **Cells:** cochlear inner and outer hair cells (CL:0000589, CL:0000601). Mouse Homer2 expression is *"particularly enriched in the tips of stereocilia of both IHCs and OHCs"* (PMID:25816005).
- **Subcellular:** stereocilium and stereocilium tip (GO:0032420, GO:0032426); the actin core and apical junctional actin belt (by CDC42-model analogy).
- **Lateralization:** bilateral, symmetric.

## 8. Temporal Development

- **Presymptomatic phase:** normal hearing through infancy; passes newborn hearing screening; carriers identified genetically before audiometrically.
- **Onset:** postlingual, typically first–second decade; 17–24 years in the most recent Chinese family; one patient's significant progression began in her 50s. Insidious.
- **Progression:** relentlessly progressive, non-episodic, lifelong; 1.2–1.6 dB/year across frequencies (founding family, threshold-on-age regression). Audiometric configuration is stage-dependent: high-frequency down-sloping early (or, rarely, low-frequency ascending), flattening to all-frequency involvement, ending severe-to-profound.
- **No remission** is described; no critical intervention window beyond ordinary timing of amplification/implantation.

## 9. Inheritance and Population

- **Inheritance:** autosomal dominant (HP:0000006), segregating across up to five generations. Every reported allele is heterozygous; no homozygote or compound heterozygote described.
- **Penetrance/expressivity:** appears complete in reported pedigrees but is formally unquantified (age-dependent onset means young carriers look unaffected). Expressivity is variable mainly in onset age and audiogram configuration. No anticipation, germline mosaicism, founder effect, or consanguinity role reported.
- **Epidemiology:** no prevalence or incidence estimate exists; *"Hearing loss caused by HOMER2 mutations is an extremely rare disorder"* (PMID:33809266). Ultra-rare; countable in families: European, Chinese (×2), Spanish, Sicilian, Italian origins plus one isolated patient. No sex bias apparent in the pedigrees. For context, dominant nonsyndromic hearing loss overall involves ~50 genes at ~67 loci (PMID:33809266, citing the field count).

## 10. Diagnostics

- **Route to diagnosis is molecular, not clinical.** There is no biomarker, no biochemical test, and no audiometric pattern specific enough to distinguish DFNA68 from the ~50 other DFNA genes. Every family was diagnosed by comprehensive hearing-loss gene panel or whole-exome sequencing followed by Sanger co-segregation. *"Our study also highlights the importance of using NGS-based diagnostic methods to identify mutations in low-prevalence deafness genes like HOMER2"* (PMID:33809266). The practical issue is panel content: HOMER2 must be on the ordered panel to be found.
- **Audiology:** pure-tone audiometry with bone conduction (excludes conductive loss) and **serial follow-up** — a single audiogram describes a stage, not the disorder; the deterioration rate requires threshold-on-age regression. ABR and speech discrimination scoring at the severe end.
- **Imaging:** the one temporal-bone CT reported was normal — *"CT scans of the proband ruled out middle- and inner-ear malformations"* (PMID:41351289). Imaging excludes alternatives rather than making the diagnosis.
- **Differential:** other DFNA loci (notably other progressive high-frequency forms such as DFNA2/KCNQ4), excluded syndromic mimics (vestibular testing and syndromic examination were normal — see §3).
- **Screening:** newborn hearing screening does **not** detect DFNA68 (postlingual onset). Cascade genetic testing of at-risk relatives is the applicable screening mode.
- No GeneReviews chapter exists for DFNA68 or HOMER2 (verified against the full GeneReviews index, snapshot 2026-09-10).

## 11. Outcome/Prognosis

- **Survival:** normal; no mortality or systemic morbidity attributable to the disorder.
- **Functional trajectory:** progressive to severe/profound deafness in an adult who acquired speech normally. Best-documented endpoint: *"Ten years after the onset of significant SNHL, SB1190-1923 had developed profound deafness with a speech discrimination score of only 8%"* (PMID:40515814).
- **Prognostic factors:** allele class may modulate onset/severity (the longest extension allele was argued to be more severe than a matched artificial truncation in zebrafish), but human genotype–phenotype correlation is not established across so few families. The measured 1.2–1.6 dB/year rate is the single quantitative prognostic anchor.
- **Recovery potential:** hearing does not recover; cochlear implantation restores speech recognition (below).
- **Open cardiac question:** zebrafish overexpressing the longest extension allele showed increased cardiac anomalies (*"a possible link to cardiac anomalies"*, PMID:40515814); no cardiac feature has been described in any DFNA68 patient, so this remains an unconfirmed model-system signal, not a prognosis item.

## 12. Treatment

No disease-modifying, gene-directed, or pharmacological therapy exists or is in trials; no HOMER2-directed agent and no NCT identifier appears in any primary report. Management is device-based and supportive:

1. **Hearing aids** (first line while thresholds permit; NCIT note: hearing-aid *fitting* has no NCIT clinical-action term; NCIT:C183182 is the device concept). The disorder-specific point is commitment to **repeated audiological review** given measurable annual progression: *"A long audiological follow-up is of paramount importance to identify hearing threshold deteriorations early and ensure prompt treatment with hearing aids or cochlear implants"* (DFNA class-level review, PMID:37371710).
2. **Cochlear implantation** (NCIT:C15329 Surgical Procedure + device NCIT:C157820 Cochlear Implant) once amplification fails. DFNA68 has one published genotype-confirmed outcome: a patient in her 60s with 8% speech discrimination implanted, with *"speech recognition improves significantly at 3- and 6-months post-implantation across various syllable and sentence conditions"* (PMID:40515814). Mechanistically favorable: the lesion is hair-cell-level and non-degenerative (hair cells and, presumably, spiral ganglion neurons preserved), upstream of what the implant stimulates.
3. **Genetic counselling and cascade testing** (NCIT:C15240 Genetic Counseling): 50% transmission risk; a normal audiogram in a young relative is uninformative (onset can be delayed to the late teens/twenties or beyond); the molecular diagnosis mainly buys a predicted trajectory, since it selects no therapy.

**Pharmacogenomics, gene therapy, ASO/RNA therapy:** none exists for DFNA68. (The dominant-negative/gain-of-function allele biology would make allele-selective knockdown a rational future strategy — as pursued in other DFNA genes — but no such program has been reported for HOMER2; this is an inference, not a published claim.)

## 13. Prevention

- **Primary prevention:** none possible (germline genetic).
- **Secondary:** cascade genetic testing in known families; serial audiometry in carriers to time amplification. Newborn hearing screening does not capture it.
- **Tertiary:** timely re-fitting of amplification and timely implant referral to limit auditory deprivation.
- **Reproductive options:** standard for an AD condition (prenatal/preimplantation testing where a familial variant is known) — general genetic-counselling practice; no DFNA68-specific guideline exists.

## 14. Other Species / Natural Disease

No naturally occurring HOMER2-associated deafness has been reported in companion animals or wildlife (no OMIA phenotype record identified). Orthologs are conserved across vertebrates — mouse *Homer2* (MGI) and zebrafish *homer2* (~67% identity to human protein) are the studied orthologs. Not zoonotic; not applicable.

## 15. Model Organisms

| Model | System | Key result | Limitation |
|---|---|---|---|
| *Homer2* constitutive knockout mouse (PMID:25816005) | Homozygous and heterozygous null | Homozygotes: *"early-onset rapidly progressive hearing loss"* from ~2 weeks, profound by 8 weeks, high-frequency-first — with a **normal complement of hair cells**. Heterozygotes hear normally. | Models **absence** of the protein; every human allele is something other than absence. Hair-cell count made at 8 weeks cannot exclude late loss. |
| Zebrafish mutant-mRNA overexpression (PMIDs 25816005, 37173411, 40515814) | Human mutant HOMER2 mRNA injected into wild-type embryos | Founding allele: smaller otic vesicles, fewer kinocilia vs wild-type mRNA — while endogenous knockdown changed nothing → dominant-negative assay. Extension alleles: reduced FM1-43 uptake with unchanged hair-cell numbers; startle-reflex deficits (*"both variants reduced distance and increased latency"*). | Supraphysiological, transient expression; lateral-line neuromasts, no cochlea, no endocochlear potential. |
| *Cdc42* conditional knockout mouse (PMID:24610943) | Atoh1-Cre hair-cell deletion | Stereocilia fusion/depletion after normal development; progressive high-frequency loss resembling the human course. | Removes CDC42, not HOMER2 — tests only the downstream half of the proposed chain. |

**The central model gap:** no system carries a single copy of a human DFNA68 allele expressed at its own level in a mammalian cochlea. A heterozygous knock-in allelic series (missense, CBD-frameshift, extension) with ABR/DPOAE follow-up, SEM bundle morphology, and late hair-cell counts is the experiment that would convert the dominant-negative and gain-of-function classifications from inference to measurement — and settle whether hair cells truly survive decades of the lesion.

---

## Key open questions (for knowledge-base gap tracking)

1. **Actin vs. calcium:** does HOMER2 act in hair cells through CDC42/actin, through PMCA2/TRPC calcium handling, or both? Proposed in 2015, still untested; no binding assay for any disease allele, no HOMER2 partner mapping in cochlear tissue.
2. **No model of the human genotype** (above).
3. **Cardiac signal of the extension allele:** zebrafish-only; echocardiography of existing carrier cohorts would resolve it.
4. **Recessive HOMER2 hearing loss:** predicted from the mouse null in 2015, never observed.

## Sources

- [OMIM #616707 — Deafness, autosomal dominant 68](https://omim.org/entry/616707) · [OMIM *604799 — HOMER2](https://omim.org/entry/604799)
- [Azaiez et al. 2015 — HOMER2, a stereociliary scaffolding protein, is essential for normal hearing in humans and mice (PMID:25816005)](https://pubmed.ncbi.nlm.nih.gov/25816005/)
- [Lu et al. 2018 — WES identified a second pathogenic variant in HOMER2 (PMID:30047143)](https://pubmed.ncbi.nlm.nih.gov/30047143/)
- [2021 — Novel truncating mutation in HOMER2, Spanish family (PMID:33809266)](https://pubmed.ncbi.nlm.nih.gov/33809266/) ([PMC8001007](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8001007/), [DOI:10.3390/genes12030411](https://doi.org/10.3390/genes12030411))
- [2023 — HOMER2 nonstop variant, EJHG (PMID:37173411)](https://pubmed.ncbi.nlm.nih.gov/37173411/) ([Nature/EJHG](https://www.nature.com/articles/s41431-023-01374-0))
- [2025 — Impact of HOMER2 frameshift extension variant on auditory function and development (PMID:40515814)](https://pubmed.ncbi.nlm.nih.gov/40515814/) ([PMC12343744](https://pmc.ncbi.nlm.nih.gov/articles/PMC12343744/))
- [2026 — Novel frameshift c.1023_1029del in HOMER2, J Clin Lab Anal (PMID:41351289)](https://onlinelibrary.wiley.com/doi/10.1002/jcla.70137)
- [Ueyama et al. 2014 — Maintenance of stereocilia by Cdc42 in cochlear hair cells (PMID:24610943)](https://pubmed.ncbi.nlm.nih.gov/24610943/)
- [DFNA narrative review 2023 (PMID:37371710)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10296186/)
- [Orphanet ORPHA:90635 — AD non-syndromic sensorineural deafness type DFNA](https://www.orpha.net/consor4.01/www/cgi-bin/OC_Exp.php?Expert=90635&lng=EN)
- [LOVD Disease #06261 (DFNA68)](https://databases.lovd.nl/shared/diseases/06261) · [GeneCards HOMER2](https://www.genecards.org/cgi-bin/carddisp.pl?gene=HOMER2)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 8 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 4 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0008596` (1 mention) - the report calls it "Postlingual onset"; HP calls it **Postlingual sensorineural hearing impairment**
- `HP:0008619` (1 mention) - the report calls it "Bilateral involvement"; HP calls it **Bilateral sensorineural hearing impairment**, and lists "Bilateral nerve deafness" among its other names
- `HP:0001757` (1 mention) - the report calls it "High-frequency-onset, down-sloping loss"; HP calls it **High-frequency sensorineural hearing impairment**
- `HP:0008573` (1 mention) - the report calls it "Low-frequency (ascending) loss at presentation"; HP calls it **Low-frequency sensorineural hearing impairment**, and lists "Low-frequency sensorineural hearing loss" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

27 of 28 terms resolved to a current term; the rest could not be looked up either way.