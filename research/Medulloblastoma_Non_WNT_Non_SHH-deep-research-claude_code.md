---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-11-11T15:13:38.310241'
end_time: '2026-11-11T15:32:18.022664'
duration_seconds: 1119.71
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Medulloblastoma, Non-WNT/Non-SHH
  mondo_id: MONDO:0850198
  category: ''
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: not recorded
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
  - claude-opus-5
  web_search_requests: 66
  num_turns: 85
  total_cost_usd: 14.129241000000007
  session_id: 5d3313d7-8fb8-4eda-8de4-fa9bdf75a7a4
  stop_reason: end_turn
  permission_denials: 7
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 56
reference_validation:
  total_references: 59
  verified: 59
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 59
  on_topic: 26
  validator_version: 0.5.1
term_validation:
  total_terms: 112
  verified: 110
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 0
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0850198
    reported_labels:
    - MONDO
    ontology_label: medulloblastoma non-WNT/non-SHH
  - term_id: MONDO:0007959
    reported_labels:
    - MONDO (parent)
    ontology_label: medulloblastoma
  - term_id: NCIT:C3222
    reported_labels:
    - NCIT (parent)
    ontology_label: Medulloblastoma
  - term_id: DOID:0080706
    reported_labels:
    - DOID
    ontology_label: medulloblastoma non-WNT/non-SHH
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Medulloblastoma, Non-WNT/Non-SHH
- **MONDO ID:** MONDO:0850198 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** 

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Medulloblastoma, Non-WNT/Non-SHH** covering all of the
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

I'll research this now. Let me load the search tool and start gathering sources.

I've completed the research. Here is the full report.

---

# Research Report: Medulloblastoma, Non-WNT/Non-SHH (MONDO:0850198)

**Prepared:** 11 November 2026 · **Target entry:** `kb/disorders/Medulloblastoma_Non_WNT_Non_SHH.yaml` · **Sibling entries already in KB:** `Medulloblastoma.yaml`, `Medulloblastoma_WNT_Activated.yaml`, `Medulloblastoma_SHH_Activated.yaml`, `GPR161-related_Medulloblastoma_Predisposition.yaml`

---

## 0. Three things to read before using this report

**0.1 — There is no causal gene, and that is the defining fact about this entry.** The template field "Causal gene(s): not recorded" is correct and is not a gap to be filled. MONDO:0850198 is a **somatically defined, negatively defined tumour type**: it is medulloblastoma in which neither WNT-pathway activation nor SHH-pathway activation is demonstrable, and it subsumes the transcriptional/methylation entities historically called **Group 3** and **Group 4**. It has no germline causal gene, no OMIM Mendelian entry, and no inheritance pattern. The genes that matter — **MYC** (hgnc:7553), **MYCN** (hgnc:7559), **OTX2** (hgnc:8522), **PRDM6** (hgnc:9350), **GFI1** (hgnc:4237), **GFI1B** (hgnc:4238), **KDM6A** (hgnc:12637), KBTBD4, SNCAIP, **ZMYM3** (hgnc:13054), **KMT2C** (hgnc:13726), **SMARCA4** (hgnc:11100), **CDK6** (hgnc:1777), CTDNEP1 — are **somatic drivers of a tumour**, not disease-causing germline alleles, and every `genetic:` record in the entry should carry `variant_origin: SOMATIC`. Writing this entry as if a gene "causes" it would be the single most likely curation error. (HGNC CURIEs above were read from `cache/hgnc/terms.csv` in this checkout; KBTBD4, SNCAIP, CTDNEP1, NRL, CD276, GPC2, EOMES, ATOH1, NPR3 are **not** in that cache and their CURIEs must be looked up before binding — see §16.)

**0.2 — Content-fence omissions.** Under this project's standing content fence (b), **no evidence on 1p36, 11q or 17q chromosomal changes, and none on chromothripsis, is included in this report.** For non-WNT/non-SHH medulloblastoma this is a material omission, because arm-level lesions on those chromosomes are among the most frequently reported cytogenetic features of Group 3/4 tumours and appear inside two of the risk-stratification schemes summarised in §11. Where a cited scheme depends on them I say so and give the scheme's structure without the arm identities. **The PR body for this entry must state this omission explicitly.** ALK-inhibitor evidence (fence a) is not relevant to this disease and none is included. Nothing here is drawn from PMID:26687816 (fence d).

**0.3 — No snippet below is a certified exact quote.** Everything in this report was gathered through web search in a sandbox with no direct PubMed/PMC fetch available, so abstract text reached me as search-engine summary, not as source bytes. Phrases I mark `CANDIDATE QUOTE` look verbatim but **have not been checked against a cached source and must not be pasted into a `snippet:` field**. Before any of this becomes YAML: `just fetch-reference PMID:NNNNNNNN`, then re-derive every snippet from the cached file, then `just count-verified-snippets`. PMID verification status is tabulated in §16.

---

## 1. Disease Information

### 1.1 Overview

Medulloblastoma is the most common malignant embryonal tumour of the central nervous system in children, arising in the cerebellum/fourth-ventricular region of the posterior fossa. Since the 4th-edition WHO update and definitively in **WHO CNS5 (2021)**, medulloblastoma is classified both histologically and **molecularly**, and the molecular classification is the one that drives management.

The 2021 WHO classification recognises four molecularly defined medulloblastoma types: **WNT-activated**, **SHH-activated and TP53-wildtype**, **SHH-activated and TP53-mutant**, and **non-WNT/non-SHH** (Louis et al., *Neuro Oncol* 2021;23(8):1231–1251, **PMID:34185076**, DOI 10.1093/neuonc/noab106 — this reference is already cached in this checkout as `references_cache/PMID_34185076.md`, `content_type: abstract_only`). The non-WNT/non-SHH type **comprises what the research literature calls Group 3 and Group 4**, and WHO CNS5 characterises it by alterations in **MYC, MYCN, PRDM6 and KDM6A** together with its methylome.

The critical conceptual point for curation is that **Group 3 and Group 4 are not cleanly separable entities**. WHO CNS5 deliberately keeps them under one named type because (i) a substantial fraction of tumours sit between the two archetypes, and (ii) second-generation profiling resolves the combined set into **eight subtypes (I–VIII)** that cut across the Group 3/Group 4 line rather than respecting it (Sharma et al., *Acta Neuropathol* 2019;138:309–326, **PMID:31076851**). Williamson et al. went further and showed the two groups form a **bipolar transcriptional continuum**, with continuum position itself prognostic (*Cell Reports* 2022;40:111162, **PMID:35926460**).

**Recommended entry shape:** one `Disease` entry bound to MONDO:0850198, with Group 3 and Group 4 (and, optionally, subtypes I–VIII) as `has_subtypes` rows rather than as separate entries — consistent with the cancer granularity ladder (design decisions §3a), since the WHO/ICC-defined molecular entity is *non-WNT/non-SHH*, and Group 3 / Group 4 are strata within it that share a first-line therapy pathway.

### 1.2 Identifiers

| Vocabulary | Identifier | Label | Verification |
|---|---|---|---|
| MONDO | **MONDO:0850198** | `medulloblastoma non-WNT/non-SHH` | ✅ read from `cache/mondo/terms.csv` |
| MONDO (parent) | MONDO:0007959 | `medulloblastoma` | ✅ same cache |
| MONDO (siblings) | MONDO:0850196 / MONDO:0850197 | WNT-activated / SHH-activated | ✅ same cache |
| ICD-O-3 | 9477/3 | Medulloblastoma, non-WNT/non-SHH | ⚠️ search-sourced; verify against WHO CNS5 blue book |
| ICD-11 | XH87Q5 | Medulloblastoma, non-WNT/non-SHH | ⚠️ search-sourced (ICD-11 MMS morphology code); **not** in `cache/icd11f/terms.csv` |
| NCIT | C129444 | Medulloblastoma, Non-WNT/Non-SHH | ⚠️ search-sourced; **not** in `cache/ncit/terms.csv` — must resolve before binding |
| NCIT (parent) | NCIT:C3222 | `Medulloblastoma` | ✅ read from `cache/ncit/terms.csv` |
| MedGen / UMLS | C4330667 | Medulloblastoma non-WNT/non-SHH | ⚠️ search-sourced |
| MedGen (Group 3) | C4330665 | Medulloblastoma non-WNT/non-SHH group 3 | ⚠️ search-sourced |
| MedGen (Group 4) | C4330666 | Medulloblastoma non-WNT/non-SHH group 4 | ⚠️ search-sourced |
| DOID | DOID:0080706 | medulloblastoma non-WNT/non-SHH | ⚠️ search-sourced (via ZFIN human-disease page) |
| Orphanet | ORPHA:616 | Medulloblastoma (parent concept only) | ⚠️ Orphanet has **no** non-WNT/non-SHH-specific code |
| MeSH | — | **No subtype-specific MeSH heading exists**; only the parent *Medulloblastoma* heading | reported absent |
| OMIM | — | **Not applicable** — no Mendelian entry; this is a somatic tumour type | n/a |

### 1.3 Synonyms and alternative names

- Medulloblastoma, non-WNT/non-SHH (WHO CNS5 preferred)
- Non-WNT/non-SHH medulloblastoma
- Medulloblastoma, Group 3 *(stratum)*; Medulloblastoma, Group 4 *(stratum)*
- MB_Group3 / MB_Grp3 and MB_Group4 / MB_Grp4 *(methylation-class notation used in HIT/I-HIT-MED and UK-CCLG literature)*
- MB, non-WNT/non-SHH; Group 3/4 medulloblastoma; "Grp3/4 MB"
- Historical/superseded: "classic medulloblastoma" is a **histological** term and is *not* a synonym — it occurs across molecular groups.

### 1.4 Information provenance

Essentially all of the knowledge base for this entry is **aggregated disease-level**: international methylation/transcriptome meta-analyses (n = 1,256–1,600+ tumours), cooperative-group clinical trials (SJMB03, ACNS0331, ACNS0332, HIT2000/I-HIT-MED, HIT-SIOP PNET4, SIOP PNET5), and large retrospective molecular cohorts. **EHR-derived, patient-level data are not a meaningful source for this entity**, because molecular subgrouping requires a methylation array or transcriptome and is not represented in coded clinical records. There is no OMOP/COHD-style phenotype profile available, and none should be invented (see the `kb/phenotype_distributions/` policy).

---

## 2. Etiology

### 2.1 Disease causal factors

**Primary cause: somatic, largely in-utero, oncogenic transformation of a human cerebellar rhombic lip progenitor.** There is no infectious, environmental or Mendelian cause for the overwhelming majority of cases.

The most important recent shift in understanding is about **event order**. Okonechnikov and colleagues, using single-cell RNA/ATAC/DNA, spatial transcriptomics and whole-genome sequencing on primary and relapsed Group 3/4 tumours with mutational-clock modelling, reported that **large-scale copy-number change is the likely tumour-initiating event, while focal oncogene amplifications (including MYC/MYCN) are later, subclonal events acquired during tumour evolution** (*Nature* 2025;642:1062–1072, DOI 10.1038/s41586-025-08973-5; **PMID not verified — see §16**). `CANDIDATE QUOTE`: *"Large-scale copy number variations are nominated as likely tumor-initiating events in group 3/4 medulloblastoma, with focal oncogene aberrations occurring only during tumor evolution."* They also concluded initiation is probably a **multi-step** process.

This is directly relevant to how the pathograph is wired: **MYC amplification should not be drawn as the root/initiating node of the Group 3 arm**. It is better modelled as a progression node downstream of an initiating chromosomal-instability node. (The arm-level identities of the initiating copy-number changes are omitted here under content fence (b).)

### 2.2 Genetic risk factors

**Germline predisposition is uncommon and is not subgroup-defining.** Waszak et al. screened 1,022 medulloblastoma patients and found a significant excess of damaging germline variants in six genes — **APC, BRCA2, PALB2, PTCH1, SUFU, TP53** (*Lancet Oncol* 2018;19:785–798; PMID not verified). Of these, only **BRCA2** (hgnc:1101; 7/1,022, ~1%) and **PALB2** (hgnc:26144; 5/1,022, <1%) distribute into the non-WNT/non-SHH groups; germline PALB2 carriers included one MB_Group3 and one MB_Group4 patient. Germline PALB2/BRCA2 cases were associated with **mutational signatures of homologous-recombination repair deficiency**. APC → WNT; PTCH1/SUFU → SHH; TP53 → SHH (and WNT), so **none of the four high-yield predisposition genes points at this entry**.

Overall, **<5% of Group 3/Group 4 cases are attributable to a recognised cancer-predisposition gene**. This has a practical consequence worth capturing in the entry's `notes:`: a non-WNT/non-SHH molecular assignment **does not remove** the indication for germline assessment, but the prior probability of a syndromic cause is low relative to SHH or WNT medulloblastoma.

**No common susceptibility locus has been established by GWAS at genome-wide significance that is specific to the non-WNT/non-SHH groups.** Treat any claim to the contrary as requiring a primary source.

**Somatic genetic drivers** are covered in §4 — these are the operative "genetic risk factors" for this entity in the mechanistic sense.

### 2.3 Environmental risk factors

- **Ionising radiation** is the only reasonably supported exogenous risk factor for paediatric embryonal CNS tumours generally, chiefly from therapeutic/high-dose exposure. The evidence specific to *diagnostic* radiation is weak: a Children's Oncology Group case-control study found **no association** between head injury or diagnostic head X-rays and medulloblastoma/PNET and **no dose–response** (*Cancer Causes Control* 2010;21:1039–1048; PMID not verified).
- **Parental/preconception exposure**: experimental mouse work shows paternal germ-cell irradiation (1 Gy X-rays) raised offspring susceptibility to neonatally induced medulloblastoma ~1.4-fold (**PMID:26452034**, *Oncotarget* 2015 — note this is in a *Ptch1⁺/⁻* SHH-model background and **does not transfer to non-WNT/non-SHH**). Human epidemiology on paternal occupational/diagnostic exposure is **inconclusive**.
- **Proposed but unestablished**: N-nitroso compounds, pesticides, tobacco smoke, electromagnetic fields, infectious agents, parental occupational exposures, medications. The literature consistently describes the aetiological evidence as scarce.
- **Age and sex** are the only robust demographic risk markers (§9).

**Curation guidance:** the `environmental:` block for this entry will be thin, and that is the correct answer. Use the `review_notes:` waiver pattern (`Left deliberately uncited.` + ≥20 words recording what was searched) rather than citing weak associations, per the `check-environmental-evidence` rule.

### 2.4 Protective factors

**None established.** No protective genetic variant, dietary factor, or exposure has been shown to reduce risk of non-WNT/non-SHH medulloblastoma. Do not populate a `PROTECTS_AGAINST` environmental link.

### 2.5 Gene–environment interactions

**No validated GxE interaction** is reported for this entity in humans. The *Ptch1⁺/⁻* transgenerational radiation work above is the closest analogue and belongs to SHH biology, not here.

---

## 3. Phenotypes

### 3.1 How the phenotype arises

Non-WNT/non-SHH medulloblastoma is clinically a **posterior-fossa mass + obstructive hydrocephalus + leptomeningeal dissemination** syndrome. Almost every presenting feature is explained by one of three things: raised intracranial pressure from fourth-ventricular obstruction, direct cerebellar/brainstem involvement, or CSF dissemination. **Hydrocephalus is present in >80% of medulloblastoma at diagnosis**, and Group 3/Group 4 tumours specifically present with moderate-to-severe hydrocephalus.

### 3.2 Presenting phenotypes (with suggested HPO bindings)

All HP CURIEs below were **read from `cache/hp/terms.csv` in this checkout** and are therefore cache-verified for existence and label; enum membership and clinical appropriateness still need the curator's judgement.

| Phenotype | HPO term | Mechanism | Frequency / character |
|---|---|---|---|
| Obstructive hydrocephalus | **HP:0000238** `Hydrocephalus` | fourth-ventricle outflow obstruction | >80% of MB at diagnosis; moderate–severe in Grp3/Grp4 |
| Raised intracranial pressure | **HP:0002516** `Increased intracranial pressure` | hydrocephalus + mass effect | very frequent; the proximate cause of the classic triad |
| Headache (classically morning, worsening) | **HP:0002315** `Headache` | raised ICP | very frequent; cardinal presenting symptom |
| Vomiting (classically morning, projectile) | **HP:0002013** `Vomiting` | raised ICP ± area postrema involvement | very frequent; cardinal |
| Nausea | **HP:0002018** `Nausea` | as above | frequent |
| Ataxia (general) | **HP:0001251** `Ataxia` | cerebellar parenchymal involvement | very frequent; **early** |
| Truncal ataxia | **HP:0002078** `Truncal ataxia` | vermian/nodular involvement | early, often first sign (midline tumour) |
| Gait ataxia | **HP:0002066** `Gait ataxia` | vermian involvement | very frequent |
| Dysmetria | **HP:0001310** `Dysmetria` | cerebellar hemispheric spread | appendicular signs appear **after** truncal signs |
| Papilledema | **HP:0001085** `Papilledema` | raised ICP | frequent in older children |
| Nystagmus | **HP:0000639** `Nystagmus` | cerebellar/brainstem | frequent |
| Diplopia | **HP:0000651** `Diplopia` | VI nerve palsy from raised ICP | frequent |
| Abducens palsy (false localising) | **HP:0006897** `Abducens palsy` | raised ICP stretching CN VI | characteristic |
| Cranial nerve palsy (other) | **HP:0006824** `Cranial nerve paralysis` | brainstem/floor-of-IV-ventricle invasion | less frequent |
| Head tilt / torticollis | **HP:0000473** `Torticollis` | tonsillar herniation, posterior-fossa irritation | characteristic red flag in children |
| Lethargy | **HP:0001254** `Lethargy` | raised ICP | frequent |
| Irritability | **HP:0000737** `Irritability` | raised ICP (infants) | frequent in infants |
| Macrocephaly | **HP:0000256** `Macrocephaly` | hydrocephalus pre-fusion of sutures | **infants only** |
| Developmental regression / loss of milestones | **HP:0002376** `Developmental regression` | raised ICP, tumour burden | characteristic infant presentation |
| Failure to thrive | **HP:0001508** `Failure to thrive` | vomiting, raised ICP | infants |
| Back pain | **HP:0003418** `Back pain` | spinal leptomeningeal drop metastases | in M3 disease |
| Seizure | **HP:0001250** `Seizure` | uncommon; supratentorial dissemination | uncommon |
| Medulloblastoma (the lesion itself) | **HP:0002885** `Medulloblastoma` | — | definitional |
| CNS neoplasm (coarse) | **HP:0100006** `Neoplasm of the central nervous system` | — | use only with `coarse_binding_basis` |

**Coarse-binding warning:** `HP:0002664` *Neoplasm* and `HP:0100006` *Neoplasm of the central nervous system* are in the coarse set gated by `just check-coarse-phenotypes`. If either is bound, it needs a `coarse_binding_basis` — most plausibly `NO_HPO_TERM` (HPO has no non-WNT/non-SHH-specific term) with a note; `HP:0002885 Medulloblastoma` is the specific term and should be preferred.

### 3.3 Phenotype characteristics

- **Age of onset.** Group 3 is weighted to **infants and young children**; Group 4 spans the whole paediatric age range. Overall MB peaks at **3–7 years**; one source gives a **median age of 8 years at diagnosis for non-WNT/non-SHH**. In adults, Group 3 is **rare** and Group 4 is uncommon (§9.3).
- **Severity.** Severe. This is a malignant, rapidly progressive tumour; untreated it is uniformly fatal.
- **Progression.** **Subacute to rapidly progressive** — typical symptom duration before diagnosis is weeks to a few months, shorter in Group 3. Not episodic, not relapsing–remitting in the natural history (relapse after therapy is a different matter, §8.4).
- **Frequency among affected individuals.** Headache/vomiting/ataxia are the near-universal triad; hydrocephalus >80%; metastatic disease at diagnosis **~40–45% in Group 3** and **~35–40% in Group 4** (both substantially higher than WNT or SHH).

### 3.4 Quality-of-life impact

Acutely, QoL is dominated by raised ICP and the perioperative course (including posterior fossa syndrome / cerebellar mutism, which occurs in a significant minority after midline resection). **Long-term QoL is dominated by treatment, not by the tumour** (§11.3, §12.9): craniospinal irradiation in a developing brain produces lifelong neurocognitive, endocrine and auditory morbidity. One survivor series reported deficits in attention/processing speed in **79%**, learning and memory in **88%**, language in **56%**, visual perception in **50%**, executive function in **64%**. Survivors are described as at risk of social isolation with substantially reduced self-rated QoL. No disease-specific PRO instrument is standard; EQ-5D/PedsQL and the COG neurocognitive battery (used in ACNS0331) are what appear in trials.

---

## 4. Genetic / Molecular Information

### 4.1 There is no causal germline gene — these are somatic drivers

Repeating §0.1 because it governs every record in this section: all genes below are **somatic** in this entity. Every `genetic:` record should carry `genetic_context.variant_origin: SOMATIC`, and `relationship_type` should reflect a somatic-driver claim rather than `CAUSATIVE` germline causation. `gene_disease_validity` should generally be **left absent** — ClinGen does not classify *MYC → non-WNT/non-SHH medulloblastoma* as a gene–disease validity pair, and per the repo rule a tier is copied from a source, never assigned.

### 4.2 Driver landscape

Northcott et al. sequenced 491 untreated medulloblastomas with methylation profiling of 1,256 (*Nature* 2017;547:311–317, DOI 10.1038/nature22973). Driver events were confidently assigned to **76% of Group 3** and **82% of Group 4** tumours. `CANDIDATE QUOTE`: *"New molecular subtypes were differentially enriched for specific driver events, including hotspot in-frame insertions that target KBTBD4 and 'enhancer hijacking' events that activate PRDM6."*

**Group 3 recurrent somatic alterations** (percentages are of Group 3 unless stated):

| Gene / event | Frequency | Type | Consequence |
|---|---|---|---|
| **MYC** amplification (hgnc:7553) | ~10–20% (one source ~17%) | focal high-level amplification, 8q | GAIN_OF_FUNCTION; global transcriptional amplification; **strong adverse prognostic marker** |
| **OTX2** amplification/overexpression (hgnc:8522) | ~6–8% amplified, overexpression broader | amplification / overexpression | GAIN_OF_FUNCTION; lineage transcription factor; blocks differentiation, activates cell-cycle genes |
| **GFI1 / GFI1B** activation (hgnc:4237 / hgnc:4238) | reports range 11–30%; ~15–20% overexpression; GFI1 mutation/rearrangement ~4% | **enhancer hijacking** via somatic structural variant | GAIN_OF_FUNCTION; transcriptional repressors placed under super-enhancer control |
| **SMARCA4** (hgnc:11100) | ~9% | mutation | SWI/SNF chromatin remodeller, LOF |
| **CTDNEP1** | ~5% | mutation | LOF; CURIE **not cached**, look up |
| **KMT2D** (hgnc:7133) | ~5% | mutation | H3K4 methyltransferase, LOF |

**Group 4 recurrent somatic alterations:**

| Gene / event | Frequency | Type | Consequence |
|---|---|---|---|
| **PRDM6** activation via **SNCAIP** tandem duplication | **17% of Group 4** | **enhancer hijacking**; SNCAIP lies ~600 kb upstream of PRDM6 | GAIN_OF_FUNCTION of a putative transcriptional repressor / histone methyltransferase |
| **KDM6A** (hgnc:12637) | ~7% | mutation | LOF; H3K27 demethylase — differentiation block |
| **KBTBD4** hotspot in-frame indels | ~6% | **neomorphic** in-frame insertions/delins in the Kelch 2b–2c loop (P311delinsPP, R313delinsPRR most common) | **NEOMORPHIC** — see §6.5 |
| **OTX2** (hgnc:8522) | ~6% | amplification | GOF |
| **ZMYM3** (hgnc:13054) | ~6% | mutation | chromatin regulator, LOF |
| **KMT2C** (hgnc:13726) | ~6% | mutation | H3K4 methyltransferase, LOF |
| **MYCN** amplification (hgnc:7559) | ~6% (up to ~10% with CDK6) | focal amplification | GOF; enriched in Group 4α |
| **CDK6** amplification (hgnc:1777) | ~4% | focal amplification | GOF; cell-cycle; enriched in Group 4γ |
| **ZIC1** (hgnc:12872) | ~4% | mutation | cerebellar lineage TF |
| **CHD7** (hgnc:20626) | reported | mutation | chromatin remodeller |

**The headline biological statement to curate** is that Group 3/Group 4 medulloblastoma has a **low point-mutation burden and is instead driven by copy-number change, structural-variant-mediated enhancer hijacking, and mutation of chromatin regulators.** Enhancer hijacking was first defined in this disease: Northcott et al. 2014 (**PMID:25043047**, *Nature* 511:428–434) showed that `CANDIDATE QUOTE` *"somatic structural variants juxtapose GFI1 or GFI1B coding sequences proximal to active enhancer elements, including super-enhancers, instigating oncogenic activity"* and *"identify GFI1 and GFI1B as prominent medulloblastoma oncogenes and implicate 'enhancer hijacking' as an efficient mechanism driving oncogene activation in a childhood cancer."*

### 4.3 Variant classification, population frequency, origin

- **ACMG/AMP classification does not apply** to these as somatic events; they are graded by somatic-oncology frameworks (AMP/ASCO/CAP tiers, OncoKB, CIViC), not by ClinVar germline criteria.
- **Allele frequency in gnomAD/1000G is not applicable** — these are somatic amplifications, structural variants and tumour-restricted indels. Do not populate population allele frequencies.
- **Somatic vs germline:** essentially all somatic. The small germline component is BRCA2/PALB2 (§2.2).
- **Functional consequences:** mixed by design — `GAIN_OF_FUNCTION` (MYC, MYCN, OTX2, CDK6, PRDM6, GFI1/GFI1B), `LOSS_OF_FUNCTION` (KDM6A, KMT2C, KMT2D, SMARCA4, ZMYM3, CTDNEP1), and **`NEOMORPHIC`** (KBTBD4). KBTBD4 is the one that most often gets mis-typed: it is **not** a loss-of-function allele, and `FunctionalImpactEnum` has `NEOMORPHIC` precisely for this shape.

### 4.4 Modifier genes

No validated germline modifier. The functional modifiers of outcome are **somatic co-occurrence patterns** — e.g. MYC amplification on a Group 3 background versus on a Group 4 background behaves differently (§11.4) — and these are better modelled as subtype strata than as `MODIFIER` gene records.

### 4.5 Epigenetic information

This is the mechanistic core of the entity and is dealt with in §6.5–6.7. Summary:

- **DNA methylation** is the *diagnostic* substrate: the Heidelberg/DKFZ classifier assigns molecular group and subtype from an array (Capper et al., *Nature* 2018;555:469–474, **PMID:29539639**).
- **Chromatin-modifier mutation** (KDM6A, KMT2C/D, ZMYM3, SMARCA4, CHD7) is the dominant somatic mutational theme in Group 4.
- **Enhancer hijacking** (GFI1/GFI1B, PRDM6) is a structural-variant-driven epigenetic mechanism.
- **Bivalent/poised chromatin and PRC1/PRC2** maintain the differentiation block: Chen et al./St Jude + KiTZ identified an EnhBiv chromatin signature enriched for **KDM2B** binding in Group 3/4 tumours, with KDM2B required for growth and acting by promoting H3K27me3 and bivalency at neuronal differentiation genes (*Nat Genet* 2026;58:2590–2604, **PMID:42786297**).
- **Super-enhancers** at *CRX* and *NRL* drive the Group 3 photoreceptor program (§6.4).

### 4.6 Chromosomal abnormalities

Non-WNT/non-SHH medulloblastomas are characterised by **extensive aneuploidy and whole-chromosome/arm-level copy-number change**, and a **whole-chromosomal-aberration (WCA) signature** is prognostic within standard-risk disease (Goschzik et al., *Lancet Oncol* 2018, retrospective molecular analysis of HIT-SIOP PNET 4; PMID not verified) and is incorporated into the Group 4 risk scheme of Williamson/Goddard et al. (*Acta Neuropathol* 2023, **PMID:37014508**). **The identities of the specific chromosome arms in those signatures are omitted from this report under content fence (b).** A curator writing this section should either (a) keep the WCA concept at the level of "≥N whole-chromosome aberrations defines a favourable-risk group" without naming arms, or (b) get the fence lifted by the user for this entry.

Focal amplifications (MYC, MYCN, OTX2, CDK6) and the SNCAIP tandem duplication are covered in §4.2 and are not fenced.

---

## 5. Environmental Information

- **Environmental factors:** none established as causal (§2.3). Therapeutic ionising radiation is a risk factor for paediatric CNS tumours in general; no exposure is specific to non-WNT/non-SHH.
- **Lifestyle factors:** **not applicable.** This is an embryonal tumour that initiates in utero or in early postnatal life; adult lifestyle factors have no plausible role, and paediatric lifestyle factors have no evidence.
- **Infectious agents:** **none.** No pathogen is implicated in medulloblastoma aetiology. (A 2026 paper reports an HCMV-associated late-gene expression signature correlating with poor survival in paediatric Group 3 medulloblastoma — PMID:42351756 — but this is an **association in tumour transcriptomes**, not an aetiological claim, and should be curated as an association signal with explicit caveats if used at all.)
- **Notable absence of a transmission/agent block:** do not create `infectious_agent:` or `transmission:` records.

**ECTO binding:** the only plausibly bindable exposure is ionising radiation. `cache/ecto/terms.csv` exists in this checkout and should be searched (`l~radiation`, `l~ionizing`, **and** the British spelling `l~ionising` — per the CLAUDE.md worked example of `l~anaesthetic` vs `l~anesthetic`) before asserting that no ECTO term exists.

---

## 6. Mechanism / Pathophysiology

### 6.1 The causal chain, as an ordered sequence

Each step names what it causes next. `[DEMONSTRATED]` = directly shown in human tissue or a faithful model; `[INFERRED]` = reconstructed or extrapolated.

1. **In the first trimester of human cerebellar development, a human-specific rhombic lip (RL) progenitor compartment is established** — comprising an RL ventricular zone (RLVZ) and a protracted RL subventricular zone (RLSVZ) — which **provides the pool of cells from which both Group 3 and Group 4 tumours arise.** `[DEMONSTRATED]` — Smith et al., *Nature* 2022;609:1012–1020, **PMID:36131015**; Hendrikse et al., *Nature* 2022, **PMID:36131014** (see §16). `CANDIDATE QUOTE` (Smith): *"molecular signatures encoded within a human rhombic-lip-derived lineage trajectory aligned with photoreceptor and unipolar brush cell expression profiles that are maintained in group 3 and group 4 medulloblastoma."*

2. **A large-scale chromosomal copy-number change arises in one such progenitor, in utero, and this — not oncogene amplification — initiates the tumour.** `[DEMONSTRATED by mutational-clock/subclonal reconstruction; the identity of the initiating lesion in any individual tumour is INFERRED]` — Okonechnikov et al., *Nature* 2025;642:1062–1072. *(Arm identities omitted under fence (b).)*

3. **The affected progenitor fails to execute the normal RL differentiation trajectory**, so a proliferative, undifferentiated RL-like progenitor population persists beyond the developmental window in which it should have been consumed. `[DEMONSTRATED]` — Hendrikse et al. (PMID:36131014) describe EOMES⁺ KI67⁺ RL-SVZ progenitors failing to differentiate in the presence of chromosomal instability and/or driver alterations.

4. **The anatomical consequence of (3) is that the persisting progenitor mass sits in the region of the nodulus / inferior vermis**, which is where systematic diagnostic-imaging review localises the putative anatomical origin of Group 3 and Group 4 tumours. `[DEMONSTRATED]` — Smith et al. 2022.

   *The chain now branches.*

5. **Branch A — Group 3 lineage.** The retained progenitor corresponds to the **earliest** RLVZ apex: a **PRTG⁺ MYC-high NESTIN-low stem-like cell**, present in the four-week human embryonic hindbrain, which grows adjacent to a **human-specific interposed vascular plexus** in the RLVZ. `[DEMONSTRATED]` — Visvanathan et al., *Cell* 2024, **PMID:38971152**. This niche is recapitulated in Group 3 medulloblastoma and not in other medulloblastoma types; co-culture with endothelial cells promotes tumour stem-cell growth. **→ the niche sustains a self-renewing stem compartment.**

6. **Branch A, continued — focal oncogene events are acquired on top of the initiating lesion:** MYC amplification, OTX2 amplification, and GFI1/GFI1B activation by enhancer hijacking. `[DEMONSTRATED]` — Northcott 2014 (PMID:25043047), Northcott 2017. Per step 2 these are **progression**, not initiation.

7. **Branch A — MYC amplification causes global transcriptional amplification, proliferative drive, a differentiation block, and metabolic rewiring** toward glycolysis, glutamine dependence, and **de novo serine/glycine synthesis through PHGDH** (hgnc:8923). `[DEMONSTRATED in vitro and in two independent MYC-amplified Group 3 mouse models]` — PHGDH inhibition (genetic or with NCT-503) induced greater cell death in MYC-expressing cells and extended survival (*Neuro Oncol* 2025;27:237–; PMID not verified).

8. **Branch A — OTX2 transactivates the photoreceptor master regulators CRX and NRL**, whose elevated expression is additionally driven by **super-enhancers** at both loci; the resulting **photoreceptor transcriptional program becomes a Group 3-specific lineage dependency** required for growth in vitro and in orthotopic grafts. `[DEMONSTRATED]` — Garancher et al., *Cancer Cell* 2018 (PMID not verified). OTX2 also acts non-canonically through **alternative splicing** to maintain a Group 3 stem-cell program (2024; PMC11321995).

9. **Branch B — Group 4 lineage.** The retained progenitor sits **further along** the RL trajectory, toward **unipolar brush cell (UBC)** and glutamatergic cerebellar-nuclei identity. `[DEMONSTRATED]` — Hovestadt et al., *Nature* 2019;572:74–79, **PMID:31341285**: `CANDIDATE QUOTE` *"Group 4 tumours consisted exclusively of differentiated neuronal-like neoplastic cells"*; glutamatergic cerebellar nuclei and unipolar brush cells matched Group 4 developmental programmes most closely. Also Vladoiu et al., *Nature* 2019 (PMID not verified).

10. **Branch B — chromatin-regulator lesions arrest that differentiation trajectory:**
    - **KDM6A** LOF → failure to remove H3K27me3 → neuronal differentiation genes stay repressed;
    - **KMT2C/KMT2D** LOF → defective enhancer H3K4 monomethylation;
    - **PRDM6** activation (via SNCAIP tandem duplication) → **represses chromatin accessibility and alters gene expression** (PMC11239875; bioRxiv 2023);
    - **KBTBD4** neomorphic indels → see 11;
    - **SMARCA4 / ZMYM3 / CHD7** LOF → SWI/SNF and co-repressor dysfunction.
    `[DEMONSTRATED for the individual lesions; the integration into one differentiation-arrest model is partly INFERRED]`

11. **Branch B — KBTBD4 hotspot mutants acquire neomorphic ubiquitin-ligase substrate specificity.** The mutant KELCH β-propeller directly engages **HDAC1/2**, which brings the **LSD1–HDAC1/2–CoREST (LHC) complex** into a CRL3^KBTBD4 complex, causing **ubiquitylation and degradation of CoREST and LSD1**. Cryo-EM shows a KBTBD4 homodimer asymmetrically engaging HDAC1 with two β-propellers, buttressed by the endogenous cofactor **inositol hexakisphosphate acting as a second molecular glue**; the same interface is the one the stem-cell agonist **UM171** glues pharmacologically. `[DEMONSTRATED — structural + cellular]` — *Cell Death Differ* 2022 (PMC9525703); *Nature* 2025, "Converging mechanism of UM171 and KBTBD4 neomorphic cancer mutations" (PMC11882451). **Therapeutic corollary:** HDAC1/2 inhibitors block the mutant KBTBD4–HDAC1 interface and the proliferation of KBTBD4-mutant medulloblastoma cells.

12. **Both branches converge on a shared epigenetic differentiation block.** **KDM2B**, highly expressed in Group 3 and Group 4, promotes sequential **PRC1/PRC2** recruitment and a **bivalent/poised enhancer (EnhBiv)** state at neuronal differentiation genes, raising H3K27me3 and repressing those programs; KDM2B is required for tumour growth in both groups. `[DEMONSTRATED — 52 primary samples + functional dependency]` — *Nat Genet* 2026;58:2590–2604, **PMID:42786297**.

13. **The expanding differentiation-arrested mass fills the fourth ventricle → obstructs CSF outflow → obstructive hydrocephalus → raised intracranial pressure.** `[DEMONSTRATED — clinical]` → produces morning headache (HP:0002315), vomiting (HP:0002013), papilledema (HP:0001085), lethargy (HP:0001254), false-localising abducens palsy (HP:0006897), and, in infants, macrocephaly (HP:0000256).

14. **Direct cerebellar invasion, vermian first → truncal and gait ataxia (HP:0002078, HP:0002066), later appendicular dysmetria (HP:0001310) and nystagmus (HP:0000639).** `[DEMONSTRATED — clinical]`

15. **Tumour cells shed into the CSF → leptomeningeal dissemination along the craniospinal axis** (Chang M1–M3), present **at diagnosis** in ~40–45% of Group 3 and ~35–40% of Group 4. `[DEMONSTRATED]` This is the step that makes craniospinal irradiation mandatory and is the dominant determinant of outcome.

16. **Therapy (resection + CSI + platinum/alkylator chemotherapy) eradicates the bulk clone but a subclone persists — frequently in the disseminated compartment — and re-expands.** `[DEMONSTRATED — molecular studies of matched primary/relapse pairs]` Relapse in Group 3/Group 4 is **predominantly metastatic rather than local** (17/20 metastatic recurrences in one series were Group 3 or Group 4), with median time to relapse ~**0.9 y in Group 3** and ~**2.7 y in Group 4**. Subgroup identity is **preserved** at relapse.

17. **In parallel, craniospinal irradiation of a developing nervous system, cochlea, hypothalamic–pituitary axis and spine → the late-effect burden** (§11.3): neurocognitive decline, sensorineural hearing loss (compounded by cisplatin), growth-hormone deficiency and other endocrinopathy, growth failure, and second malignancy.

### 6.2 Molecular pathways

- **MYC/MYCN transcriptional network** — the dominant Group 3 (MYC) and a Group 4α (MYCN) axis. Global transcriptional amplification; downstream EIF4EBP1/4EBP1 upregulation linked to shorter survival (PMC12267489).
- **Cell-cycle / CDK–RB axis** — CDK6 amplification (Group 4γ); CDK4/6 inhibition is an active therapeutic hypothesis, synergistic with BET inhibition.
- **Polycomb (PRC1/PRC2) and H3K27me3** — KDM2B-dependent bivalency; KDM6A LOF removes the opposing demethylase.
- **COMPASS/MLL H3K4 methylation** — KMT2C/KMT2D LOF.
- **LSD1–HDAC1/2–CoREST co-repressor complex** — degraded by neomorphic KBTBD4.
- **SWI/SNF chromatin remodelling** — SMARCA4.
- **Photoreceptor differentiation program (OTX2 → CRX/NRL)** — Group 3 lineage dependency.
- **TGF-β signalling** — components frequently amplified in Group 3; robust pathway activation with elevated pSMAD3 relative to other groups, and a mediator of immunosuppression (relevant to CAR-T resistance).
- **Metabolic**: glycolysis, glutaminolysis, altered TCA flux, de novo serine/glycine synthesis (PHGDH), MPC–SOD2 axis.
- **Notably absent**: canonical WNT and SHH signalling — their absence is definitional.

**Suggested GO bindings** (all **read from `cache/go/terms.csv`** in this checkout):

| Concept | GO term |
|---|---|
| cerebellar development context | **GO:0021549** `cerebellum development` |
| differentiation block | **GO:0030182** `neuron differentiation` (with `modifier: DECREASED`) and **GO:0045665** `negative regulation of neuron differentiation` (`modifier: INCREASED`) |
| proliferative drive | **GO:0008284** `positive regulation of cell population proliferation`; **GO:0008283** `cell population proliferation` |
| transcriptional dysregulation | **GO:0006357** `regulation of transcription by RNA polymerase II`; **GO:0003700** `DNA-binding transcription factor activity` |
| chromatin mechanisms | **GO:0006325** `chromatin organization`; **GO:0006338** `chromatin remodeling` |
| KBTBD4 neomorphic degradation | **GO:0016567** `protein ubiquitination`; **GO:0000209** `protein polyubiquitination` |
| CoREST/HDAC axis | **GO:0004407** `histone deacetylase activity` |
| stemness | **GO:0019827** `stem cell population maintenance` |
| apoptosis evasion | **GO:0006915** `apoptotic process` (`modifier: DECREASED`) |
| nervous-system development frame | **GO:0007399** `nervous system development` |

**Not in cache — must be looked up before binding:** *histone H3-K27 demethylation* (for KDM6A), *histone H3-K4 methylation* (KMT2C/D), *photoreceptor cell differentiation* (CRX/NRL), *canonical Wnt signaling pathway* and *smoothened signaling pathway* (if the entry asserts their absence). **Do not write these CURIEs from memory** — this is exactly the failure mode CLAUDE.md documents.

### 6.3 Cellular processes

Differentiation arrest of a committed neuronal progenitor; sustained self-renewal in a vascular niche; cell-cycle dysregulation; evasion of apoptosis; migration/invasion into leptomeninges; and — distinctively — **persistence of a normal fetal developmental program past its window**, rather than de-differentiation of a mature cell.

### 6.4 Protein dysfunction

- **MYC/MYCN** — overexpressed wild-type protein; dosage, not structure. Classically "undruggable" directly; targeted indirectly through BET bromodomain inhibition (JQ1 and successors), CDK inhibition, and metabolic dependencies.
- **OTX2 / CRX / NRL** — homeodomain and leucine-zipper lineage transcription factors acting as master regulators; dependency is expression-level, not structural.
- **GFI1/GFI1B** — zinc-finger transcriptional repressors, structurally normal, mislocalised in regulatory space by enhancer hijacking.
- **KBTBD4** — a **structurally altered substrate receptor**; the 2b–2c loop indel reshapes the KELCH β-propeller surface to create a new protein–protein interface for HDAC1/2. This is a *gain of a new interaction surface*, and cryo-EM has resolved it.
- **KDM6A / KMT2C / KMT2D / SMARCA4 / ZMYM3** — truncating/damaging LOF alleles.
- **PRDM6** — PR/SET-domain protein acting as a transcriptional repressor; overexpressed, not mutated.

### 6.5–6.7 Epigenetic changes, metabolic changes, immune involvement

Epigenetics is covered in §4.5 and steps 10–12. Metabolism in step 7. **Immune system:** non-WNT/non-SHH medulloblastoma is **immunologically "cold"** — low mutational burden, low neoantigen load, sparse T-cell infiltrate, and an immunosuppressive microenvironment in which **TGF-β signalling is prominently activated in Group 3**. Group 4 shows a distinctive enrichment of tumour-infiltrating **B cells** and mast cells (PMC9101625), reported as favourable for the anti-tumour response. **B7-H3 (CD276) is overexpressed in >80% of medulloblastoma, particularly Group 3 and Group 4**, making it the leading CAR-T target (§12.4). There is **no autoimmune or immunodeficiency component** — do not model one.

### 6.8 Tissue damage mechanisms

Direct mass effect and parenchymal invasion; obstructive hydrocephalus with transependymal oedema; leptomeningeal infiltration. **Therapy-mediated** damage (radiation and platinum) is responsible for the great majority of permanent tissue injury in survivors and should be modelled as a treatment-toxicity chain, not as disease pathophysiology.

### 6.9 Molecular profiling resources

- **Transcriptomics**: bulk RNA-seq meta-cohorts (Sharma 2019 n=1,501 methylation with 852 matched transcriptomes; Williamson 2022 continuum cohorts); single-cell RNA-seq (Hovestadt 2019 n=25 tumours; Vladoiu 2019; Riemondy 2022); spatial transcriptomics (Okonechnikov 2025).
- **Epigenomics**: Illumina 450k/EPIC methylation arrays underpin the whole classification; ChIP-seq/ATAC-seq enhancer maps (Lin et al., active medulloblastoma enhancers, **PMID:26814967**); EnhBiv/KDM2B chromatin maps (PMID:42786297).
- **Proteomics**: a 2026 proteogenomic characterisation of medulloblastoma reporting clinically relevant molecular subtypes associated with progression (PMID:42249086) — recent, worth reading before curating; and Forget et al.'s integrative phosphoproteomics identifying **ERBB4–SRC** signalling as a Group 4 hallmark (*Cancer Cell* 2018; PMID not verified).
- **Functional genomics**: DepMap and targeted CRISPR screens; KDM2B emerged as a selective dependency this way (PMID:42786297).
- **Datasets**: **I could not verify any GEO/EGA accession offline in this session.** GSE207266 surfaced in a search result in connection with the rhombic-lip work but is **unverified**. Per the repo's dataset rule, run `just discover-datasets` / `just verify-datasets` and commit the resulting `references_cache/GEO_*.md`; do **not** transcribe an accession from this report.

### 6.10 Cell types and anatomy for the pathograph

**Suggested CL bindings** (read from `cache/cl/terms.csv`):

| Role | CL term |
|---|---|
| cell of origin pool (generic) | **CL:0011020** `neural progenitor cell` |
| stem-like apex (Group 3) | **CL:0000047** `neural stem cell` or **CL:0000034** `stem cell` |
| lineage identity of the tumour | **CL:0000679** `glutamatergic neuron` |
| differentiated neuronal-like tumour cells | **CL:0000540** `neuron` |
| the photoreceptor program referent | **CL:0000210** `photoreceptor cell` *(use with care — the tumour expresses a photoreceptor program, it is not a photoreceptor; `preferred_term` should say so)* |
| microenvironment | **CL:0000129** `microglial cell`, **CL:0000235** `macrophage`, **CL:0000236** `B cell`, **CL:0000084** `T cell` |
| comparison/control lineage | **CL:0001031** `cerebellar granule cell`, **CL:0000120** `granule cell` |

**Not in cache — must be looked up:** **unipolar brush cell** (the single most important cell type for Group 4 and a likely CL gap), *endothelial cell* (for the Group 3 vascular niche). If CL has no unipolar brush cell term, that is a legitimate `preferred_term`-without-`term:` case **with the search recorded in `notes:`** — and re-run the search before writing that note.

---

## 7. Anatomical Structures Affected

**UBERON bindings below were read from `cache/uberon/terms.csv` in this checkout.**

### 7.1 Organ level
- **Primary site:** cerebellum — **UBERON:0002037** `cerebellum`; specifically the midline/vermian region — **UBERON:0004720** `cerebellar vermis`; filling/abutting the **UBERON:0002422** `fourth ventricle`; within **UBERON:0008788** `posterior cranial fossa`.
- **Developmental origin:** **UBERON:0006215** `rhombic lip` (and **UBERON:0002028** `hindbrain`). The **nodulus** specifically is where imaging localises the putative origin of Group 3/4 tumours — **"nodulus" is not in the local UBERON cache and must be looked up** (it is a vermian lobule; if no suitable term resolves, bind `cerebellar vermis` and carry "nodulus" in `preferred_term`).
- **Secondary involvement:** leptomeninges / **UBERON:0002360** `meninx` and **UBERON:0000315** `subarachnoid space`; **UBERON:0001359** `cerebrospinal fluid` as the dissemination route; **UBERON:0002240** `spinal cord` (drop metastases); **UBERON:0000955** `brain` (supratentorial dissemination). Extraneural metastasis (bone, bone marrow, lymph node) is rare but recognised, mostly at relapse.
- **Body systems:** nervous system primarily. Secondarily (treatment-mediated): endocrine (hypothalamic–pituitary, thyroid, gonadal), auditory, musculoskeletal (spinal growth), haematopoietic (myelosuppression, secondary leukaemia).

### 7.2 Tissue and cell level
Nervous tissue; a small-round-blue-cell embryonal tumour of **densely packed, poorly differentiated neuroepithelial cells** with high nuclear:cytoplasmic ratio and brisk mitotic/apoptotic activity. Cell populations as in §6.10. Histologically, **classic** morphology predominates across non-WNT/non-SHH; **large cell / anaplastic (LC/A)** morphology is enriched in Group 3, particularly MYC-amplified Group 3, and is itself a high-risk feature. Desmoplastic/nodular and MBEN morphologies are SHH-associated and **argue against** this entry.

### 7.3 Subcellular level
Nucleus and chromatin are where the mechanism lives — GO cellular-component terms for *nucleus*, *chromatin*, *transcription repressor complex* and *Cul3-RING ubiquitin ligase complex* would be apt, but **none of these CURIEs is verified in this checkout** and all must be looked up.

### 7.4 Localization and laterality
**Midline**, filling the fourth ventricle, arising from the vermis/nodulus — this midline position distinguishes the typical Group 3/4 tumour from the frequently **lateral/hemispheric** SHH tumour, and is a usable imaging surrogate (§10.3). Lesions are **not lateralised**; dissemination is **bilateral/diffuse** through the subarachnoid space. Reported vermian localisation: ~73% of Group 3 and ~70% of Group 4.

---

## 8. Temporal Development

### 8.1 Onset
- **Biological onset: in utero.** Steps 1–3 of §6.1 place initiation in first-trimester rhombic lip, with failed differentiation and persistence of progenitors; Okonechnikov's mutational-clock analysis supports a prolonged, multi-step pre-clinical phase.
- **Clinical onset:** Group 3 — infants and young children; Group 4 — across the paediatric age range; **median 8 years at diagnosis for non-WNT/non-SHH** (one CBTRUS-derived source). Overall MB peaks at 3–7 years. Adult presentation is uncommon (§9.3).
- **Onset pattern:** **subacute**, usually weeks to a few months of symptoms. Can be acute if the tumour decompensates hydrocephalus.

### 8.2 Staging

**Chang M-stage** (still the operative staging system, alongside residual-disease R-stage):

| Stage | Definition |
|---|---|
| M0 | no evidence of metastasis |
| M1 | tumour cells in CSF on cytology only (microscopic) |
| M2 | gross nodular seeding intracranially beyond the primary site |
| M3 | gross nodular seeding in the spinal subarachnoid space |
| M4 | metastasis outside the craniospinal axis |

**Conventional clinical risk** (pre-molecular, still used as a layer): *average/standard risk* = age >3 y, M0, residual tumour <1.5 cm²; *high risk* = age <3 y, or residual ≥1.5 cm², or M1–M3.

**Molecular risk** (Ramaswamy et al. consensus, *Acta Neuropathol* 2016;131:821–831, **PMID:27040285**, DOI 10.1007/s00401-016-1569-6) defines bands by observed survival: **low risk >90%**, **standard/average risk 75–90%**, **high risk 50–75%**, **very high risk <50%**. Within that scheme, **Group 3 with metastases is very-high-risk**; Group 4 non-metastatic is standard-risk; Group 4 metastatic is high-risk. Current schemes refine this considerably (§11.4).

### 8.3 Progression rate and course
Rapidly progressive if untreated. With therapy the course is **"treat once, then watch for metastatic relapse"** rather than chronic or relapsing–remitting. Disease duration is defined by the relapse hazard, which is concentrated in the first 2–3 years for Group 3 and extends later for Group 4.

### 8.4 Remission and relapse
Remission is **treatment-induced**; spontaneous regression does not occur. Relapse patterns (§6.1 step 16): predominantly **metastatic/leptomeningeal**, median ~0.9 y (Group 3) vs ~2.7 y (Group 4); Group 4 metastatic relapses tend to be **isolated deposits**, Group 3 relapses **multifocal or laminar**. Molecular subgroup is preserved at relapse. **Relapsed non-WNT/non-SHH medulloblastoma is, with few exceptions, incurable.**

### 8.5 Critical periods
- **Developmental:** the first-trimester rhombic lip window — the period of vulnerability, and not clinically actionable.
- **Therapeutic:** the interval from surgery to completion of craniospinal irradiation. Delay or dose reduction in this window costs survival (§12.2). For infants, the critical decision window is whether and when to give CSI (§12.3).
- **Toxicity:** the younger the child at irradiation, the more severe the neurocognitive consequence — the entire infant-therapy literature exists to manage this trade-off.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

| Metric | Value | Source quality |
|---|---|---|
| Medulloblastoma incidence, ages 0–19 | **0.41 / 100,000 person-years** | CBTRUS-derived, search-sourced |
| Medulloblastoma incidence, US children 0–14 | **0.47 / 100,000 / year** | Orphanet-derived |
| adolescents/young adults | 0.11 / 100,000 / year | Orphanet-derived |
| adults >40 | 0.02 / 100,000 / year | Orphanet-derived |
| Developed-country age-adjusted range, children | 0.39–0.7 / 100,000 | review-sourced |
| Orphanet prevalence class (medulloblastoma, all) | **1–9 / 100,000** | ORPHA:616 |
| **non-WNT/non-SHH incidence** | **~0.03 / 100,000 population** (CBTRUS-style, all ages) | search-sourced, **verify** |
| Group 3 share of medulloblastoma | **~25%** | multiple reviews |
| Group 4 share of medulloblastoma | **~35–40%** (most common single group) | multiple reviews |
| Combined non-WNT/non-SHH share | **~60–70%** of all medulloblastoma | multiple reviews |

**For the `prevalence:` block:** use `measure_type: ANNUAL_INCIDENCE` with an **explicit `rate_denominator`** (the repo requires it for incidence, with no fallback — `POPULATION_PER_YEAR` or `PERSON_YEARS` as the source states), `rate_per_100000`, and the verbatim source phrasing in `notes`. Do **not** pair a qualitative tier (`RARE`, `ULTRA_RARE`) with an incidence measure.

In SJMB03, a prospectively enrolled international phase III cohort of 330 eligible medulloblastoma patients, methylome profiling gave **65 Group 3 (21.3%)** and **139 Group 4 (45.6%)** — i.e. **~67% non-WNT/non-SHH** — against 53 WNT (17.4%) and 48 SHH (15.7%). This is the cleanest trial-based denominator available.

### 9.2 Inheritance
**Not heritable.** No inheritance pattern, no penetrance, no expressivity, no anticipation, no germline mosaicism, no founder effect, no consanguinity role, no carrier frequency. Do **not** create an `inheritance:` block with a mode-of-inheritance term. If anything is recorded, it should be the rare germline BRCA2/PALB2 association from §2.2, modelled as a `relationship_type: SUSCEPTIBILITY` genetic record with explicit framing — and even that is a weak, subgroup-non-specific association.

### 9.3 Population demographics

- **Sex ratio.** Strong, consistent **male predominance**: Group 3 ~**2:1**, Group 4 reported **2:1 to 3:1**. Medulloblastoma overall ~1.7:1. This is one of the more reliable epidemiological facts about the entity and is worth an evidence item.
- **Age distribution.** Group 3 skewed young (infants/young children); Group 4 across the paediatric range. **In adults, SHH predominates (~60%), Group 4 is less common, and Group 3 is rare** — one adult tertiary cohort reported 30 WNT, 112 SHH, **6 Group 3**, 41 Group 4. Adult Group 4 has notably **worse** outcome than paediatric Group 4 (5-y PFS 44.9% in one adult series), a genuinely counterintuitive finding worth capturing.
- **Ancestry / geography.** No established ancestry-specific risk and no endemic distribution. Incidence differences between registries (e.g. US 0.39 vs Finland 0.45 per 100,000) are small and plausibly ascertainment-driven. **Do not bind HANCESTRO terms** without a source that actually stratifies by ancestry.
- **Variant geography:** not applicable (somatic).

---

## 10. Diagnostics

### 10.1 The diagnostic pathway, in order

1. **MRI brain and whole spine with contrast, before surgery** — characterises the posterior-fossa mass and stages the neuraxis.
2. **Maximal safe resection** → tissue.
3. **Histopathology** — confirms medulloblastoma; assigns morphology (classic / LC-A / desmoplastic-nodular / MBEN).
4. **Molecular group assignment — mandatory under WHO CNS5.** This is what makes the diagnosis *non-WNT/non-SHH*.
5. **Lumbar CSF cytology**, usually ~14 days post-operatively, for M1 staging.
6. **Risk assignment** combining age, M-stage, residual disease, histology and molecular group/subtype.

### 10.2 Molecular classification — the defining test

- **DNA-methylation array classification is the reference standard.** Capper et al. (*Nature* 2018;555:469–474, **PMID:29539639**) established a machine-learning classifier across CNS entities that resolves WNT, SHH (two subclasses), Group 3 and Group 4; in that study methylation profiling **changed the diagnosis in ~12% of CNS tumour cases**. Practical implementation is documented in the Heidelberg experience (*Acta Neuropathol* 2018;136:181–210; PMID not verified).
- **Subtype assignment (I–VIII)** within non-WNT/non-SHH also runs off the methylome (Sharma 2019, **PMID:31076851**), and cross-platform classifiers for the eight subtypes continue to be developed.
- **Important negative:** *non-WNT/non-SHH* is defined by **absence** of WNT and SHH activation. A tumour is assigned here when the classifier calls Group 3 or Group 4 — not by a positive marker. This matters for how the entry's `definitions:` block is written.
- **NanoString-based 22-gene subgrouping assays** are a validated, cheaper alternative used in several centres and in resource-limited settings.
- **Nanopore sequencing** is emerging as a rapid classification route (PMID:39731757).

### 10.3 Immunohistochemistry — useful but insufficient

The routine panel **YAP1, GAB1, OTX2, β-catenin** shows high concordance with methylation profiling for *group* assignment: nuclear β-catenin → WNT; YAP1/GAB1 positivity → SHH; **YAP1-negative, GAB1-negative, OTX2-positive → non-WNT/non-SHH**. 

**Group 3 vs Group 4 cannot be reliably separated by IHC.** The proposed markers perform badly: **NPR3** lacks sensitivity and **KCNA1** lacks specificity (KCNA1 expression was found in all subgroups). Any claim that IHC alone assigns Group 3 vs Group 4 should be curated as refuted or heavily caveated.

### 10.4 Imaging

- **Typical appearance:** midline, fourth-ventricular, restricted diffusion (low ADC — reflecting dense small-cell packing), variable enhancement, hydrocephalus.
- **Subgroup surrogates:** ~73% of Group 3 and ~70% of Group 4 are vermian. Group 3 shows **"fluffy"** enhancement; Group 4 **"patchy"** enhancement with intervening non-enhancing areas. Group 4 is often strikingly **minimally or non-enhancing**, which can mislead.
- **Radiomics/radiogenomics:** multiparametric-MRI models predict subgroup with ~74% overall accuracy — good for Group 4 (78%), **modest for Group 3 (56%)**; a dedicated Group 3-vs-Group 4 classifier reached AUC 98% in one multicentre study (*Radiology* 2022, PMID not verified). **Imaging is a research adjunct, not a substitute for methylation.**

### 10.5 Liquid biopsy / CSF ctDNA

This is the most clinically actionable newer diagnostic.

- **Characterisation:** low-coverage whole-genome sequencing of CSF-derived cfDNA recapitulates the tumour's copy-number landscape and supports subgrouping and risk stratification (Escudero et al., *Nat Commun* 2020;11:5376; PMID not verified).
- **Measurable residual disease (MRD):** Liu et al. analysed **476 serial CSF samples from 123 children** on a prospective trial. Baseline MRD detection was **lowest in SHH (32%)** and **highest in non-WNT/non-SHH — Group 3 77%, Group 4 75%** (WNT 63%). **MRD detectability at end of therapy was significantly associated with progression-free survival: HR 4.07 in Group 3 and HR 8.58 in Group 4** (*Cancer Cell* 2021; PMID not verified, PMC9620970).
- Genome-wide **cfDNA fragmentation patterns** in CSF also reflect medulloblastoma group (*npj Precis Oncol* 2025).

**This is a strong candidate for a `BiomarkerReadout` with `endpoint_context: CANDIDATE_SURROGATE`** (not `REGULATORY_SURROGATE` — no regulator has accepted it).

### 10.6 Other tests
- **Laboratory tests:** no diagnostic blood or urine biomarker exists. Routine bloods, audiometry and renal function are baseline **toxicity** assessments, not diagnostics.
- **Electrophysiology:** no role diagnostically; audiometry/ABR for ototoxicity monitoring.
- **Genetic testing (germline):** targeted or panel testing for the six Waszak genes is reasonable in selected cases, but **the yield in non-WNT/non-SHH is low** (<5%). WGS/WES on tumour is research/precision-oncology, not routine diagnostics. CMA, karyotyping, FISH, mtDNA and repeat-expansion testing have **no role** for this entity (FISH for MYC/MYCN amplification is the one exception and is being displaced by array-based copy number from the same methylation run).
- **Differential diagnosis:** atypical teratoid/rhabdoid tumour (**loss of INI1/SMARCB1** — note the KB already has `Atypical_Teratoid_Rhabdoid_Tumor.yaml`), ependymoma (`Ependymoma.yaml` in KB), embryonal tumour with multilayered rosettes, CNS neuroblastoma/other CNS embryonal tumours, pilocytic astrocytoma, choroid plexus tumours, and — most importantly — **the other three medulloblastoma types**, since the distinction is molecular, not morphological.

### 10.7 Screening
**There is no screening programme and none is feasible.** No newborn screening, no carrier screening, no population screening. Cascade screening applies only to the rare germline BRCA2/PALB2 families, and then as a general cancer-predisposition matter rather than a medulloblastoma-specific one. Surveillance MRI post-treatment is **follow-up**, not screening.

---

## 11. Outcome / Prognosis

### 11.1 Survival by group

| Group | 5-year overall survival | Note |
|---|---|---|
| **Group 3** | **~50%**, cited ranges **20–50%** | worst of the four medulloblastoma groups; worse still with MYC amplification and/or M+ |
| **Group 4** | **~75–90%** | intermediate; but heterogeneous — see §11.4 |
| Medulloblastoma overall | ~66% | all groups, all ages |

### 11.2 Survival by trial

- **SJMB03** (international phase III, risk-adapted, n=330): **5-year PFS 83.2% average-risk** (n=227) vs **58.7% high-risk** (n=103). Molecular group was a main determinant of outcome.
- **ACNS0331** (COG, average-risk): in children 3–7 y randomised to 18 Gy vs 23.4 Gy CSI, **5-year EFS 71.4% (low-dose) vs 82.9% (standard-dose)** — **low-dose CSI was inferior**, and `CANDIDATE QUOTE`: *"group 4 was the primary subgroup that drove these inferior outcomes"* (Group 4: **77.2% vs 97.1%, p=.047**). Reduced **boost volume** was non-inferior. The neurocognitive cost of the standard dose was a **7.34-point greater IQ decline**.
- **ACNS0332** (COG, high-risk): adding **carboplatin during craniospinal radiotherapy improved 5-year EFS by 19% in Group 3** and not in other subgroups (Leary et al., *JAMA Oncol* 2021). Isotretinoin arms closed for futility; a secondary analysis confirmed no EFS benefit from isotretinoin in any molecular group (**PMID:40276374**).

### 11.3 Morbidity, disability and late effects

Late effects are driven by craniospinal irradiation plus platinum, and are the principal long-term burden:

- **Neurocognitive:** progressive IQ decline; deficits reported in attention/processing speed **79%**, learning/memory **88%**, language **56%**, visual perception **50%**, executive function **64%**. Severity scales inversely with age at irradiation. Suggested bindings: **HP:0100543** `Cognitive impairment`, **HP:0001249** `Intellectual disability`.
- **Endocrine:** growth hormone deficiency in **nearly all** patients after 36 Gy CSI and **~50%** after 23.4 Gy; hypothyroidism in up to **75%**. Bindings: **HP:0040075** `Hypopituitarism`, **HP:0000821** `Hypothyroidism`, **HP:0011787** `Central hypothyroidism`, **HP:0004322** `Short stature`, **HP:0000826** `Precocious puberty`, **HP:0000044** `Hypogonadotropic hypogonadism`.
- **Auditory:** grade 3 hearing loss requiring intervention in **~20.5%** of long-term survivors in one series; **60%** with some hearing loss. Bindings: **HP:0000365** `Hearing impairment`, **HP:0000407** `Sensorineural hearing impairment`.
- **Second malignancy:** 10-year cumulative incidence **~5–7%**, CNS most common (high-grade glioma, meningioma), then thyroid carcinoma and bone/soft-tissue tumours.
- **Musculoskeletal/other:** spinal growth impairment and scoliosis (**HP:0002650** `Scoliosis`), cardiac and pulmonary effects from spinal-field exit dose, early-ageing phenotypes in adult survivors.
- **Posterior fossa syndrome / cerebellar mutism** after midline resection — a major acute-subacute morbidity in exactly the midline tumours this entry covers.

### 11.4 Prognostic factors and biomarkers — the current state of the art

This is where the field has moved furthest since 2019 and is the most valuable content for the entry.

**(a) Classical factors:** metastatic stage (M+), extent of resection, age <3 years, LC/A histology, MYC amplification.

**(b) Subtype (I–VIII) is prognostic within non-WNT/non-SHH** (Sharma 2019, **PMID:31076851**; n=1,501 with methylation, 852 with matched transcriptome). `CANDIDATE QUOTE`: *"enrichment of specific driver gene alterations and cytogenetic events amongst subtypes, and identified highly disparate survival outcomes."* Reported figures (**all require primary-source verification — the two sets below disagree and are probably from different cohorts/analyses**): MYC amplification enriched in **subtypes II and III**, with 5-year survival ~50% (II) and ~43% (III); **subtype VII favourable at ~85%**; subtypes II, III and V clinically worse than the rest; highest metastatic rate in subtypes II and IV (~50%), lowest in subtype VIII (~20%). *Treat these numbers as leads, not facts, until read from the paper.*

**(c) Improved clinico-molecular stratification across all of non-WNT/non-SHH** — Mynarek et al., *Acta Neuropathol* 2023;145:829–842 (**PMID:36459208**), analysing HIT2000 and I-HIT-MED with independent validation: defines a **low-risk stratum (6% of patients)** and a **very-high-risk stratum (21%)** that existing schemes miss. `CANDIDATE QUOTE`: *"These newly identified clinico-molecular low-risk and very high-risk strata, accounting for 6%, and 21% of non-WNT/non-SHH MB patients, respectively, may improve future treatment stratification."*

**(d) Group 4-specific stratification** — Williamson/Goddard et al., *Acta Neuropathol* 2023 (**PMID:37014508**), discovery cohort n=362 from UK-CCLG and international trials. Three strata:

| Stratum | Definition (abridged) | Share | 5-year PFS |
|---|---|---|---|
| Favourable risk | non-metastatic **and** (subtype VII **or** a favourable whole-chromosomal-aberration signature) | 21% | **97%** |
| High risk | remainder | 43% | 67% |
| Very high risk | metastatic **and** high-risk WCA signature | 36% | **49%** |

*The arm identities constituting the WCA signature are omitted under content fence (b).* Note the headline: **a fifth of Group 4 patients have a 97% 5-year PFS** — a de-escalation population hiding inside an "intermediate-risk" group.

**(e) MYC-family amplification is itself heterogeneous** — *Neuro Oncol* 2025;27(1):222–236, DOI 10.1093/neuonc/noae178 (MYC-amp n=64, MYCN-amp n=95, drawn from >1,600 diagnostic cases): a **very-high-risk MYC-amplified group with 10% 5-year PFS**, while **the majority of remaining MYC-amplified tumours reached 61% 5-year PFS**; **MYCN_Grp3 / MYCN_Grp4 tumours with no other clinicopathological risk factor were intermediate-risk at 70% 5-year PFS.** This directly contradicts the common shorthand "MYC amplification = uniformly fatal" and is worth an explicit evidence item.

**(f) Infant non-WNT/non-SHH** — the newest and most clinically consequential dataset (*Lancet Child Adolesc Health* 2026, **PMID:42150584**; international cohort, nine countries, ages 0–5, methylation-classified with confidence >0.8). Two findings:
  - A **favourable-risk group (MB_Group3 subtype 4)** and a **very-high-risk group (MB_Group3 subtype 2 or 3 with MYC amplification)** — i.e. infant non-WNT/non-SHH is **not** uniformly high-risk, which is how it has been treated.
  - **Upfront craniospinal irradiation was associated with better 5-year PFS (62%, 95% CI 55–70) than non-CSI approaches (focal RT or chemotherapy-only; 33%, 23–44; p<0.0001).**
  A linked comment, *"From favourable to fatal: survival outcomes among young children with non-WNT/non-SHH medulloblastoma"*, accompanies it.

**(g) MRD by CSF ctDNA at end of therapy** — HR 4.07 (Group 3), HR 8.58 (Group 4) for PFS (§10.5).

**(h) Continuum position** between the Group 3 and Group 4 archetypes is itself prognostic (Williamson 2022, **PMID:35926460**).

### 11.5 Recovery and cure
Cure is achievable at first presentation for a substantial fraction — but is **essentially never achieved after relapse** in non-WNT/non-SHH disease. "Recovery" should be understood as cure-with-sequelae: the great majority of long-term survivors carry permanent neurocognitive, endocrine and auditory deficits.

---

## 12. Treatment

**NCIT bindings below were read from `cache/ncit/terms.csv`; CHEBI from `cache/chebi/terms.csv`.**

### 12.1 Surgery
Maximal safe resection, aiming for ≤1.5 cm² residual, usually via suboccipital midline approach; CSF diversion (EVD, shunt or endoscopic third ventriculostomy) as needed. Extent of resection is a weaker independent prognostic factor once molecular subgroup is accounted for (Thompson et al., *Lancet Oncol* 2016; PMID not verified) — **gross total resection should not be pursued at the cost of brainstem injury.** Posterior fossa syndrome is a major risk of aggressive midline resection.

**NCIT:** `NCIT:C15329` **Surgical Procedure**. `therapeutic_modality: SURGERY`.

### 12.2 Radiotherapy
The backbone of cure, and the source of most long-term harm.

- **Average/standard risk:** **23.4 Gy craniospinal irradiation** + tumour-bed/posterior-fossa boost to ~54 Gy. ACNS0331 established that **18 Gy is inferior** and that the failure was driven by Group 4 — so 23.4 Gy is the floor for non-WNT/non-SHH average-risk disease. Reduced **boost volume** (tumour bed rather than whole posterior fossa) is acceptable.
- **High risk:** **36 Gy CSI** + boost, with boosts to metastatic deposits.
- **Proton therapy** is increasingly used to spare exit dose to cochlea, thyroid, heart, lungs and vertebral bodies.
- **Infants/<3–5 years:** historically CSI-avoiding; the 2026 infant cohort (§11.4f) **challenges that directly** for non-WNT/non-SHH.

**NCIT:** `NCIT:C116437` **Craniospinal Irradiation**; `NCIT:C15313` **Radiation Therapy**; `NCIT:C66897` **Proton Beam Radiation Therapy**. `therapeutic_modality: RADIOTHERAPY`.

### 12.3 Chemotherapy

| Setting | Regimen |
|---|---|
| Average-risk maintenance (COG-style) | **cisplatin + cyclophosphamide + vincristine**, or **lomustine (CCNU) + cisplatin + vincristine**; weekly vincristine during RT |
| High-risk (ACNS0332) | 36 Gy CSI + weekly vincristine **± daily carboplatin**, then 6 cycles cisplatin/cyclophosphamide/vincristine |
| Infant/young child, CSI-sparing | intensive systemic chemotherapy **± intraventricular methotrexate** (HIT-SKK), ± high-dose chemotherapy with autologous stem-cell rescue (carboplatin/thiotepa/etoposide) |
| SIOP PNET5 standard-risk | post-RT maintenance, with randomised **carboplatin concomitant with RT** in the phase III stratum |

**CHEBI bindings (cache-verified):** `CHEBI:27899` cisplatin · `CHEBI:31355` carboplatin · `CHEBI:28445` vincristine · `CHEBI:4027` cyclophosphamide · `CHEBI:6520` lomustine · `CHEBI:4911` etoposide · `CHEBI:44185` methotrexate · `CHEBI:9570` Thiotepa (note the cache label is capitalised — copy it exactly) · `CHEBI:72564` temozolomide · `CHEBI:80630` irinotecan · `CHEBI:63632` topotecan · `CHEBI:749495` bevacizumab.

**NCIT (cache-verified):** `NCIT:C15632` Chemotherapy · `NCIT:C15986` Pharmacotherapy · `NCIT:C376` Cisplatin · `NCIT:C1282` Carboplatin · `NCIT:C933` Vincristine · `NCIT:C405` Cyclophosphamide · `NCIT:C491` Etoposide · `NCIT:C642` Methotrexate · `NCIT:C16039` Autologous Hematopoietic Stem Cell Transplantation · `NCIT:C15431` Hematopoietic Cell Transplantation.

**The one treatment with a subgroup-specific, randomised-trial-grade indication is carboplatin concurrent with CSI in high-risk Group 3** (ACNS0332): +19% 5-year EFS, and **no benefit in other subgroups**. This is the single best candidate for a `treatments[].effect_modifiers` record with `effect_modifier_type: BIOMARKER`, `modification_analysis: PRESPECIFIED_SUBGROUP` or `POST_HOC_SUBGROUP` (check the paper), and `effect_in_stratum: LARGER_EFFECT`.

### 12.4 Targeted, immuno- and advanced therapies — **all investigational; none is standard of care**

- **CAR-T.** **B7-H3 (CD276)** is overexpressed in >80% of medulloblastoma, especially Group 3/4 — the leading target (e.g. NCT05835687, a basket trial). **GPC2**-directed CAR-T has a dedicated medulloblastoma trial (**NCT07087002**) and potent preclinical activity in orthotopic xenografts. HER2 CAR-T basket: NCT03500991. Head-to-head preclinical work shows GPC2-CAR acts faster but B7-H3-CAR achieves deeper responses. **TGF-β-mediated immunosuppression is a documented resistance mechanism in Group 3.** *(All NCT identifiers here are search-sourced and must be confirmed with `just fetch-reference NCT…` before curation.)*
- **CDK4/6 inhibitors** (palbociclib, ribociclib) — rationale from CDK6 amplification in Group 4γ and from MYC-driven cell-cycle dependency; synergy with BET inhibition is preclinically established (JQ1 + ribociclib potently repressed MYC in MYC-amplified Group 3 cells).
- **BET bromodomain inhibitors** — the principal indirect route to MYC; preclinically active, with documented metabolic rewiring of MYC-driven MB.
- **PHGDH / serine-glycine synthesis inhibition** (NCT-503) — preclinical survival benefit in two independent MYC-amplified Group 3 mouse models.
- **HDAC1/2 inhibitors** — a **mechanistically specific** hypothesis for **KBTBD4-mutant** tumours: HDAC1/2 inhibitors block the mutant KBTBD4–HDAC1 interface and the proliferation of KBTBD4-mutant cells. This is one of the few genotype-matched hypotheses in the entity.
- **KDM2B** — newly nominated selective dependency in Group 3/4 (PMID:42786297); no clinical agent yet.
- **PRTG-high stem compartment** — targetable in vivo in Group 3 models by diphtheria-toxin ablation or CAR-T (PMID:38971152).
- **Epigenetic agents more broadly** (LSD1, EZH2, HDAC) and kinase inhibitors are in basket trials for which non-WNT/non-SHH patients are eligible (reviewed in *Cancers* 2022;14:679, PMC8833659).
- **Relapse regimens:** MEMMAT-style metronomic antiangiogenic therapy; re-irradiation in selected cases; ¹⁷⁷Lu-DTPA-omburtamab radioimmunotherapy (NCT04167618).
- **Gene therapy, RNA therapeutics (ASO/siRNA), protein replacement:** **no role** — leave `oligonucleotide_details` and `delivery_system` absent.

### 12.5 Supportive care and rehabilitation
Perioperative corticosteroids and CSF diversion; antiemetics; audiological surveillance and hearing aids/cochlear implantation for cisplatin ototoxicity; growth-hormone and thyroid-hormone replacement; neuropsychological assessment and educational support; physiotherapy, occupational therapy and speech/language therapy, particularly for posterior fossa syndrome. **NCIT:** `NCIT:C15747` Supportive Care, `NCIT:C15315` Rehabilitation, `NCIT:C15302` Physical Therapy, `NCIT:C15240` Genetic Counseling.

### 12.6 Pharmacogenomics
No medulloblastoma-specific pharmacogenomics. The relevant PGx is generic to the agents: **TPMT/NUDT15** (not used here), and most importantly **cisplatin ototoxicity**, where CPIC/PharmGKB-level evidence concerns *TPMT* and *COMT* variants — contested — and sodium thiosulfate otoprotection is the established intervention. Any PGx claim should be sourced from CPIC/PharmGKB directly.

### 12.7 Treatment strategy / algorithm
Risk-adapted, and increasingly **molecularly** risk-adapted. The current direction of travel is: (i) **de-escalate** the newly identified favourable strata (Group 4 favourable-risk at 97% 5-y PFS; Mynarek low-risk 6%; infant MB_Group3 subtype 4); (ii) **intensify or redesign** for the very-high-risk strata (MYC-amplified very-high-risk at 10% 5-y PFS; metastatic Group 3); (iii) **do not reduce CSI dose in Group 4** (ACNS0331); (iv) **add carboplatin during CSI in high-risk Group 3** (ACNS0332); (v) **reconsider upfront CSI in infant non-WNT/non-SHH** (2026 cohort).

### 12.8 Active trial programmes
**SIOP PNET5 MB** (standard risk; opened 2014; first European trial stratifying by clinical + histological + molecular parameters; randomised carboplatin concomitant with RT; added WNT-HR and SHH-TP53 exploratory strata) — **NCT02066220**. **SIOP-HR-MB** (first international biomarker-driven randomised trial for high-risk MB; >800 patients, 16 countries; all arms give two cycles of carboplatin/etoposide induction over 6 weeks, then randomise conventional RT vs hyperfractionated accelerated RT). **COG** successors to ACNS0331/0332. *(Verify all NCT identifiers before curating; `clinicaltrials:` references and `ICTRP:` for non-US registries.)*

### 12.9 Treatment outcomes and adverse events
Response rates at first presentation are high; the problem is durability in the high-risk strata and toxicity in the cured. Acute toxicity: myelosuppression, nephrotoxicity and ototoxicity (cisplatin), haemorrhagic cystitis (cyclophosphamide), neuropathy (vincristine), radiation dermatitis and somnolence syndrome. Late toxicity as §11.3. **The side-effect profile here is substantial enough that the entry should carry treatment-toxicity content as mechanism, possibly conforming to an existing toxicity module** — `grep -il` across `kb/modules/` for peripheral axonal degeneration (vincristine neuropathy) and any ototoxicity module before writing new nodes.

---

## 13. Prevention

- **Primary prevention: none exists and none is foreseeable.** The initiating event occurs in a first-trimester fetal progenitor; there is no modifiable exposure, no vaccine, no chemoprevention. The only general principle is avoidance of unnecessary ionising radiation in children.
- **Secondary prevention / screening: none.** No population or newborn screening; no asymptomatic detection strategy. Early diagnosis depends on clinical recognition of the raised-ICP triad plus ataxia in a child — public and primary-care awareness of posterior-fossa red flags (persistent morning headache with vomiting, new ataxia, head tilt, new squint) is the only available "early detection" lever, and is a health-education measure rather than a screening programme.
- **Tertiary prevention** is where the real activity is: (i) surveillance MRI to detect relapse; (ii) **reducing treatment-related late effects** — proton therapy, boost-volume reduction, sodium thiosulfate otoprotection, endocrine surveillance and replacement, neurocognitive rehabilitation; (iii) second-malignancy surveillance in long-term survivors.
- **Genetic counselling:** offered where a germline predisposition gene is identified. Because <5% of non-WNT/non-SHH cases are attributable to one, counselling is driven by family history and tumour findings, not by the subgroup assignment itself. **PGD/prenatal testing is not applicable** to a somatic tumour type.
- **Immunisation, public-health and environmental interventions:** not applicable.
- **Prophylaxis:** none disease-specific; infection prophylaxis during myelosuppressive therapy is standard supportive care.

---

## 14. Other Species / Natural Disease

- **Taxonomy.** Naturally occurring medulloblastoma is reported in **dogs, cattle, pigs, rats, and non-human primates**, with single case reports in a **cat**, a **grizzly bear**, and a **kowari**, plus a documented cerebellar medulloblastoma in a **heifer** (PMC6332746) and a spontaneous cerebellar PNET in a juvenile **cynomolgus monkey** (*Macaca fascicularis*). **NCBITaxon CURIEs are not in this checkout's `cache/ncbitaxon/terms.csv` for these species as far as I checked — look each up before binding.**
- **Breed.** No breed predisposition is established; **no VBO binding is warranted.**
- **Comparative pathology.** Veterinary medulloblastoma shows the same predilection for **young animals** across all species and is described as never diagnosed in an adult animal — a notable comparative-biology point, consistent with an embryonal/developmental origin. The veterinary WHO classification of embryonal CNS tumours of domestic animals still uses the **PNET** framework (medulloblastoma = PNET arising from the cerebellum), so veterinary nomenclature lags human nomenclature by a full classification generation.
- **Crucially: there is no veterinary molecular subgrouping.** No animal species has a documented naturally occurring *non-WNT/non-SHH* medulloblastoma, because nobody has methylation-classified animal tumours into the human groups. **Natural animal disease is therefore relevant to `Medulloblastoma.yaml`, the parent entry, and only weakly to this one.** Do not assert that a dog's medulloblastoma is Group 3 or Group 4.
- **Orthologous genes:** mouse *Myc*, *Mycn*, *Otx2*, *Gfi1*, *Gfi1b*, *Prdm6*, *Kdm6a*, *Trp53*, *Atoh1*, *Prom1* — bind on **`MGI:`**, not `hgnc:`, per the repo's MOD-first rule, and **look every MGI identifier up at the Alliance** (the CLAUDE.md worked example of `MGI:107573` labelled *Blm* that is actually *Ott* is the cautionary case). `cache/mgi/terms.csv` exists in this checkout and should be checked first.
- **Zoonotic potential / cross-species transmission:** **none.** Not transmissible.
- **OMIA:** no OMIA entry was found for medulloblastoma in this search; verify directly before asserting absence.

---

## 15. Model Organisms

### 15.1 Group 3 models — well established

Two independent 2012 papers created the first faithful Group 3 models, both by combining **enforced MYC overexpression with Trp53 loss** in cerebellar progenitors followed by **orthotopic transplantation** into immunocompromised recipients:

- **Pei et al.** (*Cancer Cell* 2012, "An Animal Model of MYC-Driven Medulloblastoma") — sorted **Prom1⁺ (CD133⁺), lineage-negative** postnatal cerebellar stem cells.
- **Kawauchi et al.** (*Cancer Cell* 2012, "A mouse model of the most aggressive subgroup of human medulloblastoma") — introduced **Myc** ex vivo into **Trp53-null, Atoh1-sorted** granule neuron progenitors.

Resulting tumours can be serially passaged as neurospheres expressing *Prom1, Lgr5, Oct4, Nanog, Sox2* and generate secondary medulloblastomas on re-transplantation.

**Fidelity:** good for the **MYC-amplified, TP53-altered, LC/A Group 3** phenotype — aggressive, disseminating, transcriptionally Group 3-like. **Limitations to record as typed `divergences`:** (i) they are **transplant/retroviral** models, not autochthonous, so initiation does not follow the human in-utero sequence — and given Okonechnikov 2025 (§2.1) this is now a **substantive** divergence, not a technicality: the model starts from the event the human tumour acquires *last*; (ii) they use a **murine granule/stem progenitor**, whereas the human cell of origin is a **human-specific rhombic-lip progenitor in a human-specific vascular niche** that has no mouse counterpart — a `SPECIES_MISMATCH` plus `BOUNDARY_OMISSION`; (iii) *Trp53* loss is engineered but is **not** a common feature of human Group 3; (iv) immunocompromised hosts mean **the immune microenvironment is absent**, which matters for any immunotherapy claim.

Also available: **CRISPR-activation of endogenous cellular Myc** produces mouse medulloblastoma (*Sci Rep* 2018;8, DOI 10.1038/s41598-018-24956-1).

### 15.2 Group 4 models — the field's biggest gap

**There is no well-accepted, faithful genetically engineered Group 4 mouse model.** This is worth stating plainly in the entry as a `HUMAN_MODEL_MISMATCH` discussion rather than a generic `KNOWLEDGE_GAP`, because the issue is not absence of evidence but **translational validity**: models exist and do not reproduce Group 4.

The clearest worked example: PRDM6 was tested as a Group 4 driver in **human hindbrain neuroepithelial stem cells**. `CANDIDATE QUOTE`: *"Medulloblastomas derived from PRDM6-expressing neuroepithelial stem cells matched human Group 3, but not Group 4, medulloblastoma"* — the conclusion being that **PRDM6 has oncogenic potential but is insufficient to drive Group 4 from neuroepithelial stem cells, and both PRDM6 and specific cell-of-origin features are required.** That is a textbook `relationship: FAILS_TO_RECAPITULATE` link, which under the repo rules **requires both `limitations` and `evidence`**.

The mechanistic explanation now available is that Group 4 arises from **unipolar brush cells — the last cells to emerge from the RL-SVZ** — a protracted, human-specific developmental compartment that the mouse does not reproduce.

### 15.3 Human-cell and organoid models — where the field has moved

- **Cerebellar organoids (CbOs)** from expanded-potential stem cells, with integrated single-cell transcriptomic and methylation analysis, resolve discrete human RL progenitor populations aligning with Group 3- and Group 4-associated lineages, and have been assembled into a model collection for studying Group 3/4 initiation, growth and microenvironmental dependencies (*Modeling medulloblastoma pathogenesis and treatment in human cerebellar organoids*, PMC13224868 / **PMID:42020313**).
- **Patient-derived organoids (MBOs)** from 10 patients spanning WNT, SHH and Group 4, 100% establishment efficiency, stable passage.
- **PDX and PDX-derived organoid (PDXO)** cultures including multiple Group 3 and Group 4 cases.
- **Human hindbrain neuroepithelial stem cells** — the system used for the PRDM6 experiment above, and for directed differentiation recapitulating cerebellar granule neurogenesis.
- **PRTG⁺ human embryonic hindbrain stem cells** co-cultured with endothelial cells, modelling the Group 3 vascular niche (PMID:38971152).

### 15.4 Applications and resources
Models support: MYC-dependency and metabolic-vulnerability testing (PHGDH/NCT-503, BET, CDK4/6); CAR-T efficacy comparison (B7-H3 vs GPC2 in orthotopic xenografts); cell-of-origin dissection; and dissemination biology. **Resources:** MGI, IMPC/KOMP/IMSR for mouse alleles; Alliance of Genome Resources for orthologs; Cellosaurus/ATCC for lines (D425, D458, HD-MB03, MED8A are the commonly used Group 3 lines — **verify any line identifier in Cellosaurus before recording it**); the Childhood Cancer Model Atlas / PDX consortia for xenografts.

**Section placement reminder:** mouse models go in `animal_models:` (never `experimental_models:`); organoids, iPSC/NES-derived systems and cell lines go in `experimental_models:`; and every one that reaches the pathograph needs a `modeled_mechanisms` link with `relationship`, `fidelity`, `model_scale`, `limitations`/`divergences` and `readouts`.

---

## 16. Citation register — verification status

**Do not transcribe any PMID from this table into YAML without running `just fetch-reference` first.** The two columns differ in how the identifier was obtained.

### ✅ PMID confirmed by a `pubmed.ncbi.nlm.nih.gov/<PMID>` URL in search results, with a matching title

| PMID | Citation |
|---|---|
| **34185076** | Louis DN et al. The 2021 WHO Classification of Tumors of the Central Nervous System: a summary. *Neuro Oncol* 2021;23(8):1231–1251. **Already cached in this checkout.** |
| **36131015** | Smith KS et al. Unified rhombic lip origins of group 3 and group 4 medulloblastoma. *Nature* 2022;609:1012–1020. DOI 10.1038/s41586-022-05208-9 |
| **36131054** | The origins of medulloblastoma tumours in humans. *Nature* 2022 (accompanying News & Views) |
| **31076851** | Sharma T et al. Second-generation molecular subgrouping of medulloblastoma: an international meta-analysis of Group 3 and Group 4 subtypes. *Acta Neuropathol* 2019;138:309–326 |
| **25043047** | Northcott PA et al. Enhancer hijacking activates GFI1 family oncogenes in medulloblastoma. *Nature* 2014;511(7510):428–434 |
| **29539639** | Capper D et al. DNA methylation-based classification of central nervous system tumours. *Nature* 2018;555:469–474 |
| **31341285** | Hovestadt V et al. Resolving medulloblastoma cellular architecture by single-cell genomics. *Nature* 2019;572(7767):74–79 |
| **36459208** | Mynarek M et al. Identification of low and very high-risk patients with non-WNT/non-SHH medulloblastoma by improved clinico-molecular stratification of the HIT2000 and I-HIT-MED cohorts. *Acta Neuropathol* 2023;145:829–842 |
| **37014508** | Williamson D / Goddard J et al. Molecular characterisation defines clinically-actionable heterogeneity within Group 4 medulloblastoma and improves disease risk-stratification. *Acta Neuropathol* 2023 |
| **35926460** | Williamson D et al. Medulloblastoma group 3 and 4 tumors comprise a clinically and biologically significant expression continuum reflecting human cerebellar development. *Cell Rep* 2022;40:111162 |
| **38971152** | Visvanathan A et al. Early rhombic lip Protogenin⁺ᵛᵉ stem cells in a human-specific neurovascular niche initiate and maintain group 3 medulloblastoma. *Cell* 2024 |
| **42786297** | Divergent medulloblastoma chromatin states disclose KDM2B as a selective dependency. *Nat Genet* 2026;58:2590–2604 |
| **42150584** | Integrated biomarker and treatment correlates of prognosis in infant non-WNT/non-SHH medulloblastoma: a multinational retrospective cohort study. *Lancet Child Adolesc Health* 2026 |
| **40276374** | Isotretinoin has no effect on event-free survival across high-risk medulloblastoma molecular groups when added to maintenance: a secondary analysis of COG ACNS0332 |
| **26452034** | Transgenerational inheritance of enhanced susceptibility to radiation-induced medulloblastoma in newborn Ptch1⁺/⁻ mice after paternal irradiation. *Oncotarget* 2015 |
| **26814967** | Active medulloblastoma enhancers reveal subgroup-specific cellular origins. *Nature* 2016 |
| **27040285** | Ramaswamy V et al. Risk stratification of childhood medulloblastoma in the molecular era: the current consensus. *Acta Neuropathol* 2016;131(6):821–831. DOI 10.1007/s00401-016-1569-6 (PMID read from a Google Scholar lookup URL carrying both DOI and PMID) |
| **42020313** | Modeling medulloblastoma pathogenesis and treatment in human cerebellar organoids |
| **42249086** | Comprehensive proteogenomic characterization reveals clinically relevant molecular subtypes associated with medulloblastoma progression |

### ⚠️ Cited by DOI/journal/volume but **PMID NOT verified** — look up before use

| Citation | Known identifier |
|---|---|
| Hendrikse LD et al. Failure of human rhombic lip differentiation underlies medulloblastoma formation. *Nature* 2022 | PMID **36131014** asserted by a search summary only; PMC10026724 |
| Northcott PA et al. The whole-genome landscape of medulloblastoma subtypes. *Nature* 2017;547:311–317 | DOI 10.1038/nature22973 confirmed; PMID unverified |
| Cavalli FMG et al. Intertumoral Heterogeneity within Medulloblastoma Subgroups. *Cancer Cell* 2017;31:737–754 | PMID unverified |
| Okonechnikov K et al. Oncogene aberrations drive medulloblastoma progression, not initiation. *Nature* 2025;642:1062–1072 | DOI 10.1038/s41586-025-08973-5 |
| Gajjar A et al. SJMB03 outcomes. *J Clin Oncol* 2021 | PMID unverified |
| Michalski JM et al. COG ACNS0331. *J Clin Oncol* 2021 | PMID unverified |
| Leary SES, Packer RJ, Li Y et al. Efficacy of Carboplatin and Isotretinoin in Children With High-risk Medulloblastoma (ACNS0332). *JAMA Oncol* 2021 | PMID unverified |
| Waszak SM et al. Spectrum and prevalence of genetic predisposition in medulloblastoma. *Lancet Oncol* 2018;19:785–798 | PMID unverified |
| Ramaswamy V et al. Recurrence patterns across medulloblastoma subgroups. *Lancet Oncol* 2013 | PMID unverified |
| Hill RM et al. Time, pattern and outcome of medulloblastoma relapse. *Lancet Child Adolesc Health* 2020 | PMID unverified |
| Vladoiu MC et al. Childhood cerebellar tumours mirror conserved fetal transcriptional programs. *Nature* 2019 | PMID unverified |
| Garancher A et al. NRL and CRX Define Photoreceptor Identity and Reveal Subgroup-Specific Dependencies in Medulloblastoma. *Cancer Cell* 2018 | PMID unverified |
| Forget A et al. Aberrant ERBB4-SRC Signaling as a Hallmark of Group 4 Medulloblastoma. *Cancer Cell* 2018 | PMID unverified |
| Pei Y et al. An Animal Model of MYC-Driven Medulloblastoma. *Cancer Cell* 2012 | PMID unverified |
| Kawauchi D et al. A mouse model of the most aggressive subgroup of human medulloblastoma. *Cancer Cell* 2012 | PMID unverified |
| Escudero L et al. Circulating tumour DNA from the cerebrospinal fluid allows the characterisation and monitoring of medulloblastoma. *Nat Commun* 2020;11:5376 | PMID unverified |
| Liu APY et al. Serial assessment of measurable residual disease in medulloblastoma liquid biopsies. *Cancer Cell* 2021 | PMC9620970 |
| Thompson EM et al. Prognostic value of medulloblastoma extent of resection after accounting for molecular subgroup. *Lancet Oncol* 2016 | PMID unverified |
| Goschzik T et al. Prognostic effect of whole chromosomal aberration signatures in standard-risk, non-WNT/non-SHH medulloblastoma (HIT-SIOP PNET 4). *Lancet Oncol* 2018 | PMC6262170 |
| Schwalbe EC, Lindsey JC et al. Molecular and clinical heterogeneity within MYC-family amplified medulloblastoma. *Neuro Oncol* 2025;27(1):222–236 | DOI 10.1093/neuonc/noae178 |
| Ghasemi DR et al. The Current Landscape of Targeted Clinical Trials in Non-WNT/Non-SHH Medulloblastoma. *Cancers* 2022;14:679 | DOI 10.3390/cancers14030679; PMC8833659 |
| Mynarek M, Milde T et al. SIOP PNET5 MB Trial: History and Concept. *Cancers* 2021;13:6077 | DOI 10.3390/cancers13236077; PMC8657236 |
| Bailey S et al. Clinical Trials in High-Risk Medulloblastoma: Evolution of the SIOP-Europe HR-MB Trial. *Cancers* 2022;14:374 | PMC8773789 |
| Disease-associated KBTBD4 mutations in medulloblastoma elicit neomorphic ubiquitylation activity to promote CoREST degradation. *Cell Death Differ* 2022 | PMC9525703 |
| Converging mechanism of UM171 and KBTBD4 neomorphic cancer mutations. *Nature* 2025 | PMC11882451; DOI 10.1038/s41586-024-08533-3 |
| PRDM6 promotes medulloblastoma by repressing chromatin accessibility and altering gene expression | PMID **38992221** (seen in a pubmed URL, title matched) — treat as ✅ |
| MYC-dependent upregulation of the de novo serine and glycine synthesis pathway … *Neuro Oncol* 2025;27:237– | PMC11726242 |
| Robinson GW et al. Risk-adapted therapy for young children with medulloblastoma (SJYC07). *Lancet Oncol* 2018 | PMID unverified |
| Mynarek M et al. Nonmetastatic Medulloblastoma of Early Childhood: HIT-2000. *J Clin Oncol* 2020 | PMID unverified |
| MRI Radiogenomics of Pediatric Medulloblastoma: A Multicenter Study. *Radiology* 2022 | PMID unverified |

### 🚫 Excluded by content fence
- PMID:26687816 — fence (d). Not fetched, not cited, not used.
- Evidence concerning 1p36, 11q or 17q chromosomal change, and chromothripsis — fence (b). Omitted throughout; see §0.2 and §4.6.

---

## 17. Curation notes for the DisMech entry

1. **Entry type.** One `Disease` entry on MONDO:0850198. Group 3 / Group 4 as `has_subtypes` rows with short slug-friendly names (`Group 3`, `Group 4`), optionally subtypes I–VIII beneath. Each phenotype/genetic/prevalence row that differs between them should carry the `subtype:` foreign key — the `subtype-usage-audit` exists because declared subtypes usually go unwired.
2. **`disease_term` sharing.** The KB already has `Medulloblastoma.yaml` on MONDO:0007959 and the two sibling type entries on MONDO:0850196/0850197. This entry takes MONDO:0850198 alone, so `check-shared-disease-terms` should pass without a `mappings.mondo_mappings` broadMatch — but check, because `Medulloblastoma.yaml` may already map the subtype terms.
3. **Cancer cell of origin is derived, not a slot.** Mark the initiating node with `genetic_context.variant_origin: SOMATIC` and bind the cell type there. Given §6.1 step 2, the honest origin node is the **chromosomal-instability node in a rhombic lip progenitor**, not the MYC amplification node. Expect `just check-cancer-origin` to report **multiple derived origins** if both the Group 3 and Group 4 arms carry somatic `genetic_context` — that is a true reflection of a two-lineage entity, and the remedy is subtype stratification, not deletion.
4. **Hallmarks-of-cancer conformance.** Likely `conforms_to` targets: sustaining proliferative signalling, evading growth suppressors, and (strongly) `invasion_and_metastasis` for the leptomeningeal dissemination chain. Run `just list-modules` before picking — do not assume the names.
5. **Pathograph targets are bare names.** The causal chain in §6.1 is long and branching; `downstream[].target` takes a bare node name, never `phenotypes#Name`. Run `just check-causal-targets` and `just check-name-collisions` — "Hydrocephalus" as both a pathophysiology node and a phenotype would silently collapse into one node.
6. **Phenotype wiring.** §6.1 steps 13–15 give explicit mechanism→phenotype edges; use them, so this entry does not join the ~985 entries with zero connected phenotypes (`just list-disconnected-phenotypes`).
7. **Terms.** Every CURIE in this report is labelled ✅ cache-read or ⚠️ needs-lookup. **Look up every ⚠️ one in the same step you write it.** The ones I expect to be genuine ontology gaps — *unipolar brush cell* (CL), *nodulus* (UBERON) — need the search recorded in `notes:` **and re-run immediately before the note is committed**, per the `Digitalis_Poisoning` precedent.
8. **The strongest evidence items available**, in rough order of value: ACNS0332 carboplatin-in-Group-3 (randomised, subgroup-specific); ACNS0331 CSI-dose-inferiority-driven-by-Group-4 (randomised); the 2026 infant CSI finding; the Group 4 favourable-risk 97% PFS stratum; MYC-family heterogeneity (10% vs 61% 5-y PFS); the rhombic-lip origin pair; GFI1 enhancer hijacking; KBTBD4 neomorphic degradation with its matched HDAC1/2 therapeutic hypothesis; KDM2B dependency.
9. **What this entry should say it does not have:** no causal germline gene, no inheritance, no environmental cause, no infectious agent, no screening, no prevention, no approved targeted therapy, and no faithful Group 4 animal model. Several of those are substantive, citable negatives and belong in the entry as `NO_EVIDENCE` items, `HUMAN_MODEL_MISMATCH` discussions, or recorded waivers — not as silent omissions.

---

## Sources

- [The 2021 WHO Classification of Tumors of the Central Nervous System: a summary (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8328013/)
- [Unified rhombic lip origins of group 3 and group 4 medulloblastoma — Nature](https://www.nature.com/articles/s41586-022-05208-9)
- [Failure of human rhombic lip differentiation underlies medulloblastoma formation (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10026724/)
- [The origins of medulloblastoma tumours in humans — PubMed](https://pubmed.ncbi.nlm.nih.gov/36131054)
- [The whole-genome landscape of medulloblastoma subtypes — Nature](https://www.nature.com/articles/nature22973)
- [Second-generation molecular subgrouping of medulloblastoma — PubMed](https://pubmed.ncbi.nlm.nih.gov/31076851)
- [Enhancer hijacking activates GFI1 family oncogenes in medulloblastoma — PubMed](https://pubmed.ncbi.nlm.nih.gov/25043047/)
- [DNA methylation-based classification of central nervous system tumours — PubMed](https://pubmed.ncbi.nlm.nih.gov/29539639/)
- [Resolving medulloblastoma cellular architecture by single-cell genomics — PubMed](https://pubmed.ncbi.nlm.nih.gov/31341285/)
- [Identification of low and very high-risk patients with non-WNT/non-SHH medulloblastoma (HIT2000/I-HIT-MED) — PubMed](https://pubmed.ncbi.nlm.nih.gov/36459208)
- [Molecular characterisation defines clinically-actionable heterogeneity within Group 4 medulloblastoma — PubMed](https://pubmed.ncbi.nlm.nih.gov/37014508/)
- [Medulloblastoma group 3 and 4 tumors comprise a clinically and biologically significant expression continuum — PubMed](https://pubmed.ncbi.nlm.nih.gov/35926460/)
- [Early rhombic lip Protogenin+ve stem cells … initiate and maintain group 3 medulloblastoma — Cell](https://www.cell.com/cell/fulltext/S0092-8674(24)00651-2)
- [Oncogene aberrations drive medulloblastoma progression, not initiation — Nature](https://www.nature.com/articles/s41586-025-08973-5)
- [Divergent medulloblastoma chromatin states disclose KDM2B as a selective dependency — PubMed](https://pubmed.ncbi.nlm.nih.gov/42786297)
- [Integrated biomarker and treatment correlates of prognosis in infant non-WNT/non-SHH medulloblastoma — PubMed](https://pubmed.ncbi.nlm.nih.gov/42150584/)
- [From favourable to fatal: survival outcomes among young children with non-WNT/non-SHH medulloblastoma — Lancet Child Adolesc Health](https://www.thelancet.com/journals/lanchi/article/PIIS2352-4642(26)00100-8/abstract)
- [Risk stratification of childhood medulloblastoma in the molecular era: the current consensus — Acta Neuropathologica](https://link.springer.com/article/10.1007/s00401-016-1569-6)
- [Efficacy of Carboplatin and Isotretinoin in Children With High-risk Medulloblastoma (ACNS0332) — JAMA Oncology](https://jamanetwork.com/journals/jamaoncology/fullarticle/2782033)
- [Reduced-Dose and Reduced-Volume Radiotherapy … Average-Risk Medulloblastoma (ACNS0331) — ASCO Post](https://ascopost.com/news/june-2021/reduced-dose-and-reduced-volume-radiotherapy-plus-chemotherapy-in-newly-diagnosed-patients-with-average-risk-medulloblastoma/)
- [Outcomes by Clinical and Molecular Features … Phase III Trial (SJMB03) — Cancer Research UK Cambridge](https://www.cruk.cam.ac.uk/publications/outcomes-by-clinical-and-molecular-features-in-children-with-medulloblastoma-treated-with-riskadapted-therapy-results-of-an-international-phase-iii-trial-sjmb03/)
- [Spectrum and prevalence of genetic predisposition in medulloblastoma — Lancet Oncology](https://www.thelancet.com/journals/lanonc/article/PIIS1470-2045(18)30242-0/fulltext)
- [Serial assessment of measurable residual disease in medulloblastoma liquid biopsies (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9620970/)
- [Circulating tumour DNA from the cerebrospinal fluid allows the characterisation and monitoring of medulloblastoma — Nature Communications](https://www.nature.com/articles/s41467-020-19175-0)
- [Disease-associated KBTBD4 mutations in medulloblastoma elicit neomorphic ubiquitylation activity to promote CoREST degradation — Nature](https://www.nature.com/articles/s41418-022-00983-4)
- [Converging mechanism of UM171 and KBTBD4 neomorphic cancer mutations — Nature](https://www.nature.com/articles/s41586-024-08533-3)
- [PRDM6 promotes medulloblastoma by repressing chromatin accessibility and altering gene expression (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11239875/)
- [NRL and CRX Define Photoreceptor Identity and Reveal Subgroup-Specific Dependencies in Medulloblastoma — Cancer Cell](https://www.cell.com/cancer-cell/fulltext/S1535-6108(18)30059-X)
- [MYC-dependent upregulation of the de novo serine and glycine synthesis pathway … — Neuro-Oncology](https://academic.oup.com/neuro-oncology/article/27/1/237/7815637)
- [Molecular and clinical heterogeneity within MYC-family amplified medulloblastoma — Neuro-Oncology](https://academic.oup.com/neuro-oncology/article/27/1/222/7815636)
- [The Current Landscape of Targeted Clinical Trials in Non-WNT/Non-SHH Medulloblastoma (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8833659/)
- [Molecular markers and potential therapeutic targets in non-WNT/non-SHH (group 3 and group 4) medulloblastomas](https://link.springer.com/article/10.1186/s13045-019-0712-y)
- [SIOP PNET5 MB Trial: History and Concept (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8657236/)
- [Clinical Trials in High-Risk Medulloblastoma: Evolution of the SIOP-Europe HR-MB Trial (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8773789/)
- [Prognostic effect of whole chromosomal aberration signatures … HIT-SIOP PNET 4 (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6262170/)
- [GPC2-CAR T cells have potent preclinical activity against orthotopic medulloblastoma xenografts (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12554907/)
- [Decoding the immune microenvironment: precision immunotherapy for medulloblastoma subtypes (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13111466/)
- [Enrichment of Tumor-Infiltrating B Cells in Group 4 Medulloblastoma in Children (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9101625/)
- [MRI Radiogenomics of Pediatric Medulloblastoma: A Multicenter Study — Radiology](https://pubs.rsna.org/doi/full/10.1148/radiol.212137)
- [MRI features as a helpful tool to predict the molecular subgroups of medulloblastoma (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6024494/)
- [Recurrence patterns across medulloblastoma subgroups — Lancet Oncology](https://www.thelancet.com/journals/lanonc/article/PIIS1470-2045(13)70449-2/abstract)
- [Time, pattern, and outcome of medulloblastoma relapse — Lancet Child & Adolescent Health](https://www.thelancet.com/journals/lanchi/article/PIIS2352-4642(20)30246-7/fulltext)
- [Late effects of medulloblastoma treatment: multidisciplinary approach of survivors — Childs Nerv Syst](https://link.springer.com/article/10.1007/s00381-023-06146-1)
- [Medulloblastoma — StatPearls (NCBI Bookshelf)](https://www.ncbi.nlm.nih.gov/sites/books/NBK431069/)
- [Orphanet: Medulloblastoma (ORPHA:616)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=616)
- [CBTRUS Statistical Report 2018–2022 — Neuro-Oncology](https://academic.oup.com/neuro-oncology/article/27/Supplement_4/iv1/8285946)
- [Childhood Medulloblastoma and Other CNS Embryonal Tumors (PDQ®) — NCI](https://www.cancer.gov/types/brain/hp/child-cns-embryonal-treatment-pdq)
- [Medulloblastoma, Non-WNT/Non-SHH — My Cancer Genome](https://www.mycancergenome.org/content/disease/medulloblastoma-non-wnt-non-shh/)
- [Medulloblastoma non-WNT/non-SHH (Concept Id: C4330667) — MedGen](https://www.ncbi.nlm.nih.gov/medgen/1387799)
- [Modeling medulloblastoma pathogenesis and treatment in human cerebellar organoids (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13224868/)
- [Modeling pediatric medulloblastoma — Roussel, Brain Pathology](https://onlinelibrary.wiley.com/doi/10.1111/bpa.12803)
- [An Animal Model of MYC-Driven Medulloblastoma — Cancer Cell](https://www.cell.com/cancer-cell/fulltext/S1535-6108(11)00483-1)
- [Clinical and MRI findings of a cerebellar medulloblastoma in a heifer (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6332746/)
- [Subgroup and subtype-specific outcomes in adult medulloblastoma (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10723183/)
- [Head injury, diagnostic X-rays, and risk of medulloblastoma and PNET — Cancer Causes Control](https://link.springer.com/article/10.1007/s10552-010-9529-2)
- [Transgenerational inheritance of enhanced susceptibility to radiation-induced medulloblastoma — PubMed](https://pubmed.ncbi.nlm.nih.gov/26452034/)

---

**Three things I could not do in this session, stated plainly:** (1) network access from the shell was blocked, so I could not query PubMed E-utilities directly — PMID verification was done through search-result URLs, which is why §16 separates confirmed from unconfirmed; (2) consequently **no snippet here is a verified exact quote**, and every `CANDIDATE QUOTE` must be re-derived from `references_cache/` before entering YAML; (3) content on 1p36, 11q, 17q and chromothripsis is **deliberately absent** under the project's content fence, which for this particular disease removes a genuinely load-bearing part of the cytogenetic and risk-stratification picture — if the user wants that content, the fence needs lifting for this entry, and either way the PR body must disclose the omission.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 59 |
| Resolved | 59 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 59 |
| On topic | 26 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 112 |
| Resolved | 110 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 4 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0850198` (6 mentions) - the report calls it "MONDO"; MONDO calls it **medulloblastoma non-WNT/non-SHH**
- `MONDO:0007959` (2 mentions) - the report calls it "MONDO (parent)"; MONDO calls it **medulloblastoma**
- `NCIT:C3222` (1 mention) - the report calls it "NCIT (parent)"; NCIT calls it **Medulloblastoma**
- `DOID:0080706` (1 mention) - the report calls it "DOID"; DOID calls it **medulloblastoma non-WNT/non-SHH**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.