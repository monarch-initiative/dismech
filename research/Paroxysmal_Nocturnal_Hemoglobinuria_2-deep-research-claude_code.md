---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-20T13:56:02.348007'
end_time: '2026-11-20T14:03:01.454323'
duration_seconds: 419.11
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Paroxysmal Nocturnal Hemoglobinuria 2
  mondo_id: MONDO:0014166
  category: Hematologic
  causal_genes: not recorded
  omim_id: OMIM:615399
  synonyms: PIGT paroxysmal nocturnal hemoglobinuria; paroxysmal nocturnal hemoglobinuria
    2, autosomal dominant, somatic mutation; paroxysmal nocturnal hemoglobinuria caused
    by mutation in PIGT; paroxysmal nocturnal hemoglobinuria type 2
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
  - claude-haiku-5-5
  - claude-opus-5-5
  web_search_requests: 13
  num_turns: 25
  total_cost_usd: 1.3637384
  session_id: 8bfdcc78-2fdc-4928-9a09-65f702209965
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  - Read
  tool_calls: 46
  retrieval_calls: 42
  assistant_text_blocks: 3
citation_count: 12
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 7
  validator_version: 0.8.0
term_validation:
  total_terms: 2
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0014166
    reported_labels:
    - MONDO
    ontology_label: paroxysmal nocturnal hemoglobinuria 2
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Paroxysmal Nocturnal Hemoglobinuria 2
- **MONDO ID:** MONDO:0014166 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** OMIM:615399
- **Synonyms:** PIGT paroxysmal nocturnal hemoglobinuria; paroxysmal nocturnal hemoglobinuria 2, autosomal dominant, somatic mutation; paroxysmal nocturnal hemoglobinuria caused by mutation in PIGT; paroxysmal nocturnal hemoglobinuria type 2
- **Category:** Hematologic

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Paroxysmal Nocturnal Hemoglobinuria 2** covering all of the
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

Still researching: I've confirmed the two key papers (Krawitz 2013 and Höchsmann 2019) and am now pulling abstracts, the related commentary and the database records.

I've collected the primary case series and two case reports. Now checking for model organisms, the PIGT gene identifiers, and later mechanistic work.

# Paroxysmal Nocturnal Hemoglobinuria 2 (PIGT‑PNH; MONDO:0014166; OMIM:615399): research report

**Scope.** This report covers the disease defined by MONDO:0014166 / OMIM:615399. The causal gene is **PIGT** (phosphatidylinositol glycan anchor biosynthesis class T, on chromosome 20; NCBI Gene 51604). The task form listed the gene as "not recorded". The MONDO definition settles it: *"Any paroxysmal nocturnal hemoglobinuria in which the cause of the disease is a mutation in the PIGT gene"* ([OLS4 MONDO record](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0014166)). Classic PNH, caused by somatic PIGA mutation, is a different disease and is mentioned here only for contrast.

**Limits of what I could retrieve.** OMIM and the Orphanet pages returned 403 errors or browser-check pages. PubMed and PMC returned cookie or CAPTCHA pages. I could not read the full text of Höchsmann et al. 2019, so its per-patient details below come from a tool-generated summary and are labelled **[unverified]**. Quotes marked "verbatim" were retrieved word for word in this session. I did not retrieve ontology identifiers (HPO, GO, CL, UBERON, NCIT, CHEBI), so I give term **labels only**; their IDs still need looking up, because the OLS and PubMed connectors need authorisation in claude.ai connector settings. Evidence is human clinical unless marked otherwise.

---

## 1. Disease information

**Overview.** PIGT‑PNH is a very rare acquired clonal blood-stem-cell disorder. A patient carries an inherited (germline) loss-of-function variant in one PIGT copy, and later in life a blood-forming stem cell loses the other copy through a somatic 20q deletion. Daughter cells cannot attach GPI anchors to proteins. They therefore lack the complement regulators CD55 and CD59, which causes complement-driven intravascular hemolysis as in classic PNH. Unlike PIGA‑PNH, the cells also display **free (unattached) GPI** on their surface, and patients have prominent **autoinflammation**: recurrent aseptic meningitis, urticaria, arthralgia and fever.

- Krawitz et al. 2013, verbatim: *"PNH can occur even in the presence of fully assembled GPI if its transfer to proteins is defective."* ([PMID 23733340](https://pubmed.ncbi.nlm.nih.gov/23733340/), via Europe PMC)
- Höchsmann et al. 2019, verbatim: *"PIGT-PNH differs from PIGA-PNH both in the mechanism of clonal expansion and in clinical manifestations."* ([PMID 31430258](https://pubmed.ncbi.nlm.nih.gov/31430258/))

**Identifiers** (from [OLS4 MONDO](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0014166)):

| Resource | ID |
|---|---|
| MONDO | MONDO:0014166 |
| OMIM | 615399 |
| GARD | 0015958 |
| MedGen | 815699 |
| UMLS | C3809369 |

- The MONDO record has no Orphanet, MeSH or ICD‑10 cross-references. I could not confirm these from Orphanet. Parent-level PNH codes (for example the PNH Orphanet entry and ICD‑10 D59.5) would apply only at the parent level and were not verified here.
- **Synonyms (MONDO):** paroxysmal nocturnal hemoglobinuria type 2; PIGT paroxysmal nocturnal hemoglobinuria; paroxysmal nocturnal hemoglobinuria caused by mutation in PIGT; paroxysmal nocturnal hemoglobinuria 2, autosomal dominant, somatic mutation; PNH2 (abbreviation).
- **Literature names:** "PIGT‑PNH" ([Höchsmann 2019](https://pubmed.ncbi.nlm.nih.gov/31430258/)); "autoinflammation‑PNH (AIF‑PNH)" (bioRxiv preprint title, [10.1101/635573](https://www.biorxiv.org/content/10.1101/635573.full.pdf)).
- **Source of the information:** All knowledge comes from individual patient case reports and one small series, about 5–6 patients in total. No registry or EHR cohort exists.

## 2. Etiology

**Causal factors (genetic, two-hit).**
- **Hit 1:** a germline heterozygous loss-of-function PIGT variant.
- **Hit 2:** a somatic deletion of about 8–18 Mb on 20q in a blood-forming stem cell, removing the other PIGT allele.
- Krawitz 2013 (verbatim): they *"identified a heterozygous germline splice site mutation in PIGT and a somatic 8-MB deletion in granulocytes affecting the other copy of PIGT"* ([PMID 23733340](https://pubmed.ncbi.nlm.nih.gov/23733340/)).
- Höchsmann 2019 (verbatim): *"In all these patients we find a germ-line point mutation in one PIGT allele, whereas the other PIGT allele is removed by somatic deletion of a 20q region comprising maternally imprinted genes implicated in myeloproliferative syndromes."* ([PMID 31430258](https://pubmed.ncbi.nlm.nih.gov/31430258/))

**Risk factors.**
- The only defined risk factor is being a heterozygous carrier of a PIGT loss-of-function allele.
- Carriers of biallelic germline PIGT variants have a different disease: the recessive developmental disorder multiple congenital anomalies–hypotonia–seizures syndrome 3 (MCAHS3) ([MedlinePlus PIGT](https://medlineplus.gov/genetics/gene/pigt/)).
- No environmental, occupational, age or sex risk factors have been described. Onset in middle to late adulthood (age 47–71 in reported cases) is consistent with age-related somatic 20q deletions. This is an inference, not a demonstrated finding.

**Protective factors.** None identified.

**Gene–environment interactions.** None described. Autoinflammatory flares often follow urticaria and arthralgia prodromes. No external triggers have been defined.

## 3. Phenotypes

| Phenotype | Type | Frequency / characteristics | Source | HPO label (ID to verify) |
|---|---|---|---|---|
| Intravascular hemolysis / hemolytic anemia | lab / sign | All reported patients; adult onset; chronic with flares | PMID 31430258; 35979111 | Hemolytic anemia; Intravascular hemolysis |
| Hemoglobinuria / dark urine | sign | Reported (Schenone: "dark urine") | PMID 35979111 | Hemoglobinuria |
| Recurrent aseptic meningitis | sign | Most cases, possibly 3 of 5. Kawamoto case: 121 episodes over about 16 years before PNH. Schenone: 4 episodes during one hospitalisation | PMID 30262533; 35979111; 31430258 | Aseptic meningitis; Recurrent meningitis |
| Recurrent urticaria | sign | Very frequent; often decades before PNH (Schenone: from age 30) | PMID 30262533; 35979111 | Urticaria |
| Arthralgia | symptom | Very frequent; precedes meningitis episodes | PMID 30262533; 35979111 | Arthralgia |
| Recurrent fever | sign | Frequent | PMID 35979111; [unverified: 31430258] | Recurrent fever |
| Pancytopenia / cytopenias | lab | Schenone case (WBC 2×10⁹/L, platelets 137, Hb 93 g/L) | PMID 35979111 | Pancytopenia |
| Elevated CRP | lab | Schenone (CRP 20 mg/L) | PMID 35979111 | Elevated C-reactive protein level |
| CSF neutrophilic pleocytosis (sterile) | lab | Schenone (307 PMN/mm³, all cultures negative) | PMID 35979111 | CSF pleocytosis |
| Elevated serum IL‑18 / IL‑1β | lab | Reported in patients | PMID 31430258; Brodsky commentary | (no HPO term; LOINC-level) |
| Inflammatory bowel disease / ulcerative colitis | sign | German patient | MedlinePlus; search summary of Höchsmann 2019 | Ulcerative colitis |
| Neutrophil/monocyte infiltrate in urticarial skin | pathology | Schenone | PMID 35979111 | — |
| Myelodysplasia with 20q deletion; rising blasts (8%) | lab / pathology | Schenone | PMID 35979111 | Myelodysplasia |
| Arteriosclerosis | sign | One German patient [unverified] | PMID 31430258 | — |
| Thrombosis | — | Not documented in retrieved sources | — | — |

- **Course:** Autoinflammatory symptoms are episodic and recurrent. Hemolysis is chronic.
- **Quality of life:** Kawamoto's patient had 121 meningitis episodes, and Schenone's patient needed repeated hospitalisations, which suggests a heavy burden. No EQ‑5D or SF‑36 data exist.

## 4. Genetic and molecular information

**Causal gene.** PIGT encodes GPI transamidase component PIG‑T ([MedlinePlus](https://medlineplus.gov/genetics/gene/pigt/)). It is part of the GPI transamidase (GPI‑T), a heteropentamer of PIGK, GPAA1, PIGT, PIGS and PIGU. PIGK is the catalytic subunit (Cys‑His‑Asn triad), and PIGT forms a disulfide link with PIGK and plays a structural role. Cryo-EM structures:
- [Xu et al. 2022, Nat Commun](https://www.nature.com/articles/s41467-022-30250-6.pdf); PDB 7WLD
- [Zhang et al. 2022, Nat Struct Mol Biol](https://www.nature.com/articles/s41594-022-00726-6); PDB [7W72](https://www.rcsb.org/structure/7W72)

The OMIM gene entry for PIGT (610272) and the HGNC ID could not be retrieved.

**Reported germline variants** (all loss of function, heterozygous):

| Patient | Variant | Source / status |
|---|---|---|
| Japanese patient J1 (Kawamoto 2018) | c.250G>T (p.Glu84Ter, nonsense) | Schenone 2022 discussion; JCI summary [unverified] |
| German patient (Krawitz 2013) | Splice-site variant; JCI summary gives c.1401‑2A>G, exon 11 skipping [unverified] | PMID 23733340 |
| German patient G2 | c.761_764delGAAA, frameshift [unverified] | PMID 31430258 |
| German patient G3 | c.197delA, frameshift [unverified] | PMID 31430258 |
| Schenone patient | NM_015937.6:c.766_769del (p.Lys256ThrfsTer38), exon 6; ClinVar RCV000735856.1 | PMID 35979111 |

- The G2 and Schenone deletions may describe the same 4-bp deletion written in different notation. This is unresolved.
- **Function:** In Krawitz 2013, the splice variant restored CD59 expression in Pigt-null CHO cells only minimally (in vitro), consistent with loss of function. This was reported in a secondary summary and should be verified against the paper.
- **ACMG classification:** I did not retrieve ClinVar classifications.
- **Population allele frequency:** gnomAD data not retrieved.

**Somatic second hit.**
- 20q deletions reported as 8 Mb (20q11.23–q13.12; Krawitz), 12 Mb and 18 Mb (20q11.21–q13.13; Schenone).
- They cover the myeloid common deleted region (CDR) and, in some cases, PIGU as well (search summaries of Höchsmann 2019 and the preprint).

**Modifier / co-deleted genes.** The deletion removes the maternally imprinted genes **L3MBTL1** and **SGK2**. The authors propose these as candidate tumour suppressors whose loss gives the clone its growth advantage ([Brodsky 2019 commentary, JCI 131647](https://www.jci.org/articles/view/131647)).

**Epigenetics.**
- Because only the paternal allele of L3MBTL1/SGK2 is expressed, deleting the paternal 20q copy silences them. In J1 granulocytes neither transcript was detectable.
- L3MBTL1 methylation varied between patients [unverified; PMID 31430258].

**Chromosomal abnormality.** del(20q) is seen on marrow karyotype and array CGH ([PMID 35979111](https://doi.org/10.12998/wjcc.v10.i17.5702)).

## 5. Environmental information

No environmental, lifestyle, toxic or infectious causes have been described. In Schenone's patient, bacterial, fungal, viral and mycobacterial studies of the CSF were all negative, so the meningitis was confirmed as sterile ([PMID 35979111](https://doi.org/10.12998/wjcc.v10.i17.5702)).

## 6. Mechanism / pathophysiology

**Ordered causal chain**

1. A germline heterozygous PIGT loss-of-function variant leaves one working allele, so carriers are clinically silent. *(Demonstrated: PMID 23733340, 31430258.)*
2. A somatic del(20q) in a blood-forming stem cell removes the second PIGT allele plus the myeloid CDR genes. *(Demonstrated.)*
3. Branch A, clonal expansion: loss of the paternally expressed imprinted genes L3MBTL1 and SGK2 gives the clone a growth advantage, which leads to clonal dominance. *(Inferred and proposed by the authors; not proven.)* This differs from PIGA‑PNH, where expansion is attributed to immune escape in bone marrow failure. No PIGT‑PNH patient had documented marrow failure [unverified].
4. Branch B, the protein defect: biallelic PIGT loss abolishes GPI transamidase activity. GPI is still made but cannot be attached to proteins, so the cells lack GPI-anchored proteins, including **CD55 and CD59** (FLAER‑negative, CD59‑negative). *(Demonstrated.)*
5. Unattached **free GPI** reaches the cell surface and is detected by the T5 antibody. *(Demonstrated in patient cells and in PIGT‑KO THP‑1 cells: PMID 31430258.)*
6. 5a. Without CD55/CD59, complement attacks the patient's own red cells, which leads to MAC (C5b‑9) formation, **intravascular hemolysis**, hemoglobinuria and anemia. *(Demonstrated; shared with PIGA‑PNH.)*
7. 5b. Free GPI on myeloid cells activates the **lectin complement pathway**, causing more C3b and C5b‑9 deposition than on PIGA‑deficient cells. MAC deposition then drives **inflammasome-dependent IL‑1β** (and IL‑18) secretion. *(Demonstrated in vitro in THP‑1 PIGT‑KO cells and patient leukocytes.)* Verbatim (search snippet of the paper): *"complement activation is enhanced on the surface of PIGT-defective cells, leading to MAC-dependent elevated secretion of IL-1β."* In vitro, blocking C6/C7 reduced IL‑1β, whereas C5aR blockade had little effect [unverified].
8. IL‑1β/IL‑18-driven systemic **autoinflammation** results in recurrent sterile neutrophilic meningitis, urticaria (neutrophil/monocyte skin infiltrate), arthralgia, fever and possibly colitis. *(The link from cytokine to organ is inferred from cytokine levels and response to treatment.)*
9. C5 blockade (eculizumab) stops MAC formation, which ends both hemolysis and autoinflammation. This supports steps 5–7 as causal. Verbatim: *"Eculizumab treatment abrogates not only intravascular hemolysis, but also autoinflammation."* ([PMID 31430258](https://pubmed.ncbi.nlm.nih.gov/31430258/))
10. Long-term, the del(20q) clone can progress to myelodysplasia with rising blasts (8% in Schenone's patient). *(Observed in one case.)*

**Checklist mapping (labels only; IDs to verify)**

| Category | Content |
|---|---|
| Pathways | GPI-anchor biosynthesis / attachment; complement (lectin pathway, terminal pathway); NLRP3-type inflammasome / IL‑1β. The specific inflammasome sensor was not confirmed in what I retrieved |
| GO biological process | attachment of GPI anchor to protein; GPI anchor biosynthetic process; complement activation, lectin pathway; membrane attack complex assembly; interleukin‑1 beta production; inflammasome-mediated signaling; hemolysis |
| GO cellular component | GPI-anchor transamidase complex; endoplasmic reticulum membrane; plasma membrane (site of free GPI) |
| CL cell types | hematopoietic stem cell; erythrocyte; neutrophil; monocyte; granulocyte |
| CHEBI | glycosylphosphatidylinositol; IL‑1β and IL‑18 (proteins, not CHEBI); mannose (used as a lectin-pathway inhibitor in vitro) |
| Omics | No transcriptomic, proteomic or single-cell datasets found. Cryo-EM structures of GPI‑T are available (7WLD, 7W72) |
| Functional genomics | CRISPR PIGT‑KO and PIGA‑KO THP‑1 cell lines (Höchsmann 2019) |

## 7. Anatomical structures affected

- **Primary:** bone marrow / hematopoietic system; blood (erythrocytes, leukocytes).
- **Secondary:**
  - meninges / central nervous system (aseptic meningitis)
  - skin (urticaria)
  - joints (arthralgia)
  - kidney / urinary tract (hemoglobinuria)
  - possibly colon (ulcerative colitis) and arteries [unverified]
- **Subcellular:** endoplasmic reticulum (GPI‑T complex); plasma membrane.
- **UBERON labels (IDs to verify):** bone marrow; blood; meninx; skin of body; synovial joint; urine; colon.
- **Laterality:** not applicable (systemic).

## 8. Temporal development

- **Onset:** adult. Autoinflammatory symptoms start years to decades before overt PNH. In Schenone's patient, urticaria and arthralgia began at age 30 and PNH was diagnosed at 47. In Kawamoto's patient, 16 years of meningitis preceded PNH at about 71 ([PMID 30262533](https://pmc.ncbi.nlm.nih.gov/articles/PMC6169622); [PMID 35979111](https://doi.org/10.12998/wjcc.v10.i17.5702)). Ages at PNH diagnosis in the JCI series are reported as 49–68 [unverified].
- **Pattern:** autoinflammation is episodic and relapsing; hemolysis is chronic; progression to MDS is possible.
- **Remission:** induced by treatment (eculizumab). Allogeneic transplant cured one patient. No spontaneous remission has been reported.
- **Critical period:** the long inflammatory phase before PNH is a diagnostic window. Kawamoto and colleagues propose PIGT mutation as a cause of unexplained recurrent meningitis.

## 9. Inheritance and population

- **Inheritance:** germline heterozygous variant plus a somatic second hit. MONDO's synonym "autosomal dominant, somatic mutation" reflects this. The disease itself is acquired: carriers need a somatic hit, so penetrance is presumably very low. This is inferred; no data exist.
- **Prevalence:** fewer than 1% of PNH patients ([Brodsky 2019](https://www.jci.org/articles/view/131647)). Schenone described their patient as the fifth reported worldwide in 2022 ([PMID 35979111](https://doi.org/10.12998/wjcc.v10.i17.5702)). Population prevalence is unknown.
- **Geography:** Japan (1 case), Germany (3, per the JCI summary [unverified]), France/Europe (Schenone, 1).
- **Sex:** all individually described cases with known sex were male (Kawamoto, Schenone). The numbers are far too small to infer a sex ratio.
- **Not reported:** anticipation, germline mosaicism, founder effects, consanguinity role, carrier frequency.

## 10. Diagnostics

- **Flow cytometry:** loss of CD59 on red cells (type II/III populations) and FLAER‑negative neutrophils and monocytes (CD24/CD14/FLAER) ([PMID 35979111](https://doi.org/10.12998/wjcc.v10.i17.5702)). This is standard PNH testing, so it detects PIGT‑PNH clones.
- **Distinguishing test:** the **T5 monoclonal antibody** detects free GPI. It stains PIGT‑deficient cells but not PIGA‑deficient cells ([PMID 31430258](https://pubmed.ncbi.nlm.nih.gov/31430258/); Brodsky commentary).
- **Hemolysis labs:** LDH, haptoglobin, bilirubin, reticulocytes, urine hemoglobin. These are standard; specific values were not retrieved.
- **Inflammation markers:** CRP; serum IL‑18 and IL‑1β (raised).
- **CSF:** sterile neutrophilic pleocytosis with negative microbiology.
- **Genetic testing:**
  - Sequence PIGA first. If no PIGA mutation is found in a GPI-AP-deficient clone, sequence a GPI-pathway panel (PIGT, PIGB, PIGV and others) on both sorted clone cells and germline (T cells, other non-clonal tissue). Krawitz used deep sequencing of all GPI-pathway genes.
  - Array CGH or SNP array, or karyotype, to detect del(20q).
  - Exome sequencing of germline DNA is useful because the first hit is inherited.
- **Bone marrow:** karyotype del(20q); dysplasia and blast count.
- **Differential diagnosis:**
  - PIGA‑PNH (no free GPI, T5‑negative, usually no autoinflammation)
  - PIGB‑PNH (another rare germline-plus-somatic PNH; familial PIGB with CN‑LOH reported, Langemeijer 2020, Blood Adv)
  - Monogenic autoinflammatory syndromes: cryopyrin-associated periodic syndromes (CAPS), Schnitzler syndrome
  - Mollaret meningitis / recurrent viral meningitis
  - Urticarial vasculitis; aHUS (complement factors were normal in Schenone's patient)
- **Screening:** none established. Cascade testing of relatives for the germline variant is possible, but its clinical value is unknown.

## 11. Outcome / prognosis

- **Survival:** no survival statistics exist. One German patient died; the cause was not stated in the summary I retrieved [unverified].
- **Morbidity:** recurrent hospitalisations for meningitis; hemolysis; cytopenias; MDS/blast progression; catheter sepsis while on treatment (Schenone).
- **Recovery:**
  - On eculizumab, meningitis was absent for 3–5 years in two patients [unverified].
  - The Schenone patient was "now considered cured" 24 months after allo‑SCT, with 99.8% CD59+ red cells and 100% FLAER+ neutrophils and monocytes ([PMID 35979111](https://doi.org/10.12998/wjcc.v10.i17.5702)).
- **Prognostic factors:** proposed, not validated: size of the del(20q) clone, evolution of dysplasia or blasts, persistent IL‑18 elevation.

## 12. Treatment

| Intervention | Mechanism | Evidence / outcome | NCIT label (ID to verify) |
|---|---|---|---|
| **Eculizumab** | Anti-C5 monoclonal antibody; blocks MAC formation | Resolved hemolysis, meningitis, urticaria and arthralgia in Kawamoto's patient, the JCI series and Schenone's patient. Schenone, verbatim: *"We confirm that eculizumab is the best treatment to abrogate intravascular hemolysis and autoinflammation."* | Eculizumab |
| Ravulizumab | Long-acting anti-C5 | Proposed by analogy (Brodsky commentary); no PIGT-specific data found | Ravulizumab |
| Corticosteroids | Anti-inflammatory | Ended one meningitis episode within 3 days (Schenone). Earlier patients were only partly controlled with corticosteroids, colchicine, antihistamines, cromoglycate and azathioprine | Corticosteroid |
| IL‑1 blockade (anakinra, canakinumab) with prednisolone | IL‑1 antagonism | Reduced urticaria but not arthralgia or meningitis in one patient [unverified] | Anakinra; Canakinumab |
| **Allogeneic HSCT** | Replaces the clone | Curative in one patient: HLA-mismatched unrelated PBSC; reduced-intensity thiotepa/fludarabine/busulfan; GVHD prophylaxis PTCy + cyclosporine + MMF; moderate chronic GVHD that resolved. Verbatim: *"allo-SCT should be considered to cure PIGT-PNH patients."* (PMID 35979111) | Allogeneic Hematopoietic Stem Cell Transplantation |

- **Pharmacogenomics, gene therapy, RNA therapy:** none reported. Pharmacogenomic considerations for C5 inhibitors (such as C5 variants causing non-response in PNH) were not retrieved.
- **Experimental:** no PIGT-specific trials found. Proximal complement inhibitors (C3 or factor B/D inhibitors, lectin-pathway/MASP inhibitors) are mechanistically plausible but untested in PIGT‑PNH. This is my inference.
- **Supportive and prophylactic care:** anti-C5 therapy carries a meningococcal infection risk, so meningococcal vaccination is a standard requirement. That is general PNH practice and was not retrieved for this disease.
- **Suggested algorithm (from the case literature):** start anti-C5 therapy for hemolysis and autoinflammation. Consider allo‑SCT if cytopenias, dysplasia or blasts progress, or if a fit donor is available.

## 13. Prevention

- **Primary:** no prevention is possible.
- **Secondary:** consider PNH flow testing and T5 staining in adults with unexplained recurrent aseptic meningitis plus urticaria (Kawamoto 2018).
- **Tertiary:** complement inhibition; monitor for MDS; vaccination with anti-C5 therapy.
- **Genetic counselling:** relatives may carry the germline allele and face a low, unquantified risk of PIGT‑PNH. Two carrier parents risk an affected child with MCAHS3, which is relevant to reproductive counselling.
- **Not applicable:** public health, immunisation (other than with anti-C5 therapy) and environmental measures.

## 14. Other species / natural disease

- No naturally occurring PIGT‑PNH has been reported in animals. OMIA was not searched successfully.
- PIGT and the GPI‑T complex are conserved across eukaryotes; the yeast orthologue is GPI16. This is noted in the cryo-EM literature cited above, but the ortholog IDs were not retrieved.
- Zoonotic potential: not applicable.

## 15. Model organisms

- **Cell models (in vitro):**
  - PIGT‑KO and PIGA‑KO THP‑1 monocytic cell lines (CRISPR), which reproduce free-GPI display, increased lectin-pathway C3b/MAC deposition and IL‑1β secretion ([PMID 31430258](https://pubmed.ncbi.nlm.nih.gov/31430258/)).
  - Pigt-null CHO cells, used to test variant function (Krawitz 2013).
- **Animal models:** I found no mouse or other animal model of PIGT‑PNH. Searches returned only Piga conditional knockouts and Pign/Pgap1/Pgap2 mutants used for inherited GPI deficiency ([e.g., PMC8161520](https://pmc.ncbi.nlm.nih.gov/articles/PMC8161520)).
- **Limitations:** the cell lines do not capture clonal expansion via 20q imprinted genes, or the effects on the meninges and skin.
- **Resources not queried:** MGI and IMPC Pigt alleles.

---

## Key references (retrieved this session)

1. Krawitz PM et al. A case of PNH caused by a germline mutation and a somatic mutation in PIGT. *Blood* 2013;122:1312–5. **PMID 23733340**. doi:10.1182/blood-2013-01-481499
2. Luzzatto L. PNH from mutations of another PIG gene. *Blood* 2013;122:1099–100. **PMID 23950173** (commentary)
3. Kawamoto M, Murakami Y, Kinoshita T, Kohara N. Recurrent aseptic meningitis with PIGT mutations… treated by eculizumab. *BMJ Case Rep* 2018. **PMID 30262533**; PMC6169622; doi:10.1136/bcr-2018-225910
4. Höchsmann B et al. Complement and inflammasome overactivation mediates PNH with autoinflammation. *J Clin Invest* 2019;129:5123–36. **PMID 31430258**; doi:10.1172/JCI123501
5. Brodsky RA. PNH without GPI-anchor deficiency. *J Clin Invest* 2019;129:5074–6. doi:10.1172/JCI131647 (PMID 31638602 per a Europe PMC listing; not independently verified)
6. Schenone L et al. Allogeneic SCT — a curative treatment for PNH with PIGT mutation. *World J Clin Cases* 2022;10:5702. **PMID 35979111**; doi:10.12998/wjcc.v10.i17.5702
7. Xu Y et al. *Nat Commun* 2022 (GPI‑T structure, PDB 7WLD); Zhang H et al. *Nat Struct Mol Biol* 2022 (PDB 7W72)
8. MedlinePlus Genetics, PIGT (updated 24 Feb 2022): https://medlineplus.gov/genetics/gene/pigt/
9. MONDO:0014166 via OLS4.

**Still to verify before loading into the knowledge base:**
- Per-patient variants and clinical details from the Höchsmann 2019 full text, especially G1–G3.
- The PIGT HGNC ID and OMIM gene entry.
- All HPO, GO, CL, UBERON, NCIT and CHEBI identifiers for the term labels suggested above.
- ClinVar classifications.
- Any post-2022 PIGT‑PNH case reports (none found).

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014166` (7 mentions) - the report calls it "MONDO"; MONDO calls it **paroxysmal nocturnal hemoglobinuria 2**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.
