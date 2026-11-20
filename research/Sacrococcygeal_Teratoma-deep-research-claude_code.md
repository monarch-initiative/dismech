---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-11-11T22:37:38.379922'
end_time: '2026-11-11T22:57:09.494050'
duration_seconds: 1171.11
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Sacrococcygeal Teratoma
  mondo_id: MONDO:0042727
  category: Cancer
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: pre-sacral teratoma; presacral teratoma
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
  - claude-opus-5[1m]
  web_search_requests: 27
  num_turns: 83
  total_cost_usd: 9.629179
  session_id: 5128ccf9-3cf7-49c0-b550-7f3537f6bdf6
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 59
reference_validation:
  total_references: 53
  verified: 52
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.019
  relevance_assessed: 52
  on_topic: 30
  off_topic: 1
  off_topic_references:
  - PMID:9592840
  unresolved_references:
  - PMID:38337762
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 95
  verified: 92
  not_found: 0
  obsolete: 2
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 8
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0042727
    reported_labels:
    - MONDO
    ontology_label: sacrococcygeal teratoma
  - term_id: HP:0030736
    reported_labels:
    - HPO
    ontology_label: Sacrococcygeal teratoma
  - term_id: NCIT:C99055
    reported_labels:
    - NCIT
    ontology_label: Sacrococcygeal Teratoma
  obsolete_terms:
  - term_id: GO:0080111
    ontology_label: obsolete DNA demethylation
  - term_id: GO:0006306
    ontology_label: obsolete DNA methylation
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sacrococcygeal Teratoma
- **MONDO ID:** MONDO:0042727 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** pre-sacral teratoma; presacral teratoma
- **Category:** Cancer

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Sacrococcygeal Teratoma** covering all of the
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

I'll research this now. Loading the web tools first.

# Research Report: Sacrococcygeal Teratoma (MONDO:0042727)

**Prepared:** 11 November 2026 · **Target:** `MONDO:0042727` sacrococcygeal teratoma · **Category:** Cancer (congenital neoplasm)

---

## 0. How to read this report

**There is no causal gene for sacrococcygeal teratoma (SCT), and the research below confirms that the "Causal gene(s): not recorded" line in the brief is correct rather than a gap in the record.** SCT is a sporadic congenital germ cell tumour of the caudal midline, not a Mendelian disorder: the global 3,407-patient cohort treats it as a sporadic surgical disease, and the one gene with a reproducible causal relationship to a *presacral* mass is **MNX1** (`hgnc:4979`, formerly *HLXB9*, OMIM \*142994) — the Currarino syndrome gene (OMIM #176450, `MONDO:0008305`), which causes a **different** lesion that happens to sit in the same anatomical space and which the literature now explicitly separates from SCT on malignant potential (§2, §9, §10). Everything else gene-level in SCT is germ-cell-tumour susceptibility (*KITLG*, *SPRY4*, *BAK1*) or somatic change in the malignant yolk-sac component (*KIT*, *KRAS*, *NRAS*), never germline causation.

Two verification notes, both load-bearing for the curation step that follows:

- **Quotations.** Abstract text below was retrieved through NCBI E-utilities and publisher pages and is reproduced as the retrieval returned it. It has **not** been checked against a committed `references_cache/` file, because **no `references_cache/` file exists in this checkout for any PMID cited here** (checked: all of 33142194, 32376010, 33906346, 17560233, 39248311, 37964422, 21683219 are absent). Every snippet must be re-derived with `just fetch-reference PMID:<id>` and re-verified before it enters a `snippet:` field. Treat each quote here as a *lead on where the sentence is*, not as a verified snippet.
- **CURIEs.** Every CURIE given below was read from a source in this session: either the EBI OLS4 API (MONDO, HP:0030736, NCIT:C99055, UBERON:0001350, UBERON:0004341, UBERON:0003062) or this repository's own authority-backed term caches (`cache/hp/`, `cache/go/`, `cache/cl/`, `cache/uberon/`, `cache/chebi/`, `cache/ncit/`, `cache/hgnc/`, `cache/ncbitaxon/`). Terms I could **not** verify are named in prose and explicitly flagged `[CURIE NOT VERIFIED]`. None were written from memory.

**Content-fence disclosure.** This report deliberately omits chromosome-arm loss detail reported alongside the copy-number gains in §4, because that material falls next to this project's content fence (b) on chromosomal lesions. The gains (1q, 12p, 20q) and the losses at 4q, 6q and 16 are carried; one further arm-level loss reported in the same analysis is not. No ALK-inhibitor content appears anywhere in this report (fence a), and `PMID:26687816` was neither fetched nor cited (fence d).

---

## 1. Disease Information

### 1.1 Overview

Sacrococcygeal teratoma is a **germ cell tumour arising at the base of the coccyx**, containing tissues derived from all three embryonic germ layers. It is the commonest tumour of the newborn and the commonest fetal neoplasm identified on antenatal ultrasound. MONDO's own definition is short and is the one to curate against: *"A teratoma that is found at the base of the coccyx. It is the most commonly seen tumor in newborns."* NCI Thesaurus gives the near-identical *"A teratoma that arises from the base of the coccyx. It is the most commonly seen tumor in newborns."*

Three facts set the clinical shape of the disease and recur through every section below:

1. **Most SCTs are histologically benign but mechanically and haemodynamically dangerous in utero.** The threat before birth is not malignancy but high-output cardiac failure driven by arteriovenous shunting through the tumour (§6).
2. **Malignant potential is a function of age at resection, not of the tumour's intrinsic nature at birth.** Malignancy at resection rises from 3.3% at three months to a plateau of 64.2% beyond six years (§11), which is why "resect in the neonatal period" is the single most consequential clinical statement about this disease.
3. **The disease does not end with the operation.** Roughly 10% recur, a third of recurrences are malignant, and long-term urinary and anorectal dysfunction affects a large minority of survivors (§11).

### 1.2 Identifiers

| Resource | Identifier | Notes |
|---|---|---|
| MONDO | **`MONDO:0042727`** | label "sacrococcygeal teratoma"; subsets `gard_rare`, `nord_rare`, `ordo_subtype_of_a_disorder`, `rare` — note MONDO itself classes this as a *subtype of a disorder* |
| HPO | **`HP:0030736`** | "Sacrococcygeal teratoma" — *"A teratoma arising in the sacro-coccygeal region."* Carried as an `xref` by the MONDO term, i.e. the same concept exists as a phenotype term |
| NCIT | **`NCIT:C99055`** | "Sacrococcygeal Teratoma" |
| Orphanet | ORPHA:494421 | listed as MONDO xref; the Orphanet page itself was behind a bot check this session, so its prevalence class and ICD codes were **not** read — fetch `ORPHA:494421` into the cache and read them there |
| UMLS | C0559459 | |
| MedGen | 107852 | |
| SNOMED CT | 281561000 | from MONDO's `SCTID` xref |
| GARD | 0000319 | |
| NORD | 1685 | |
| NANDO | 2100216, 2200816, 2201287 | three Japanese Nanbyo records map here |
| OMIM | **none for SCT** | OMIM #176450 is *Currarino syndrome*, a different entity (§2.1) |
| ICD-10 / ICD-11 | **not verified in this run** | MONDO carries no ICD xref for this term; read them from the ORPHA:494421 record rather than composing them |
| ICD-O-3 morphology | 9080/x family (teratoma), 9071/3 (yolk sac tumour) | **flagged for verification** against ICD-O-3 before use in a `classifications` block |

### 1.3 Synonyms

MONDO and NCIT both carry exactly two alternatives: **pre-sacral teratoma** and **presacral teratoma**. These are worth treating with care, because *presacral teratoma* is also the term used for the Currarino lesion, which the 2015 and 2026 comparative studies show behaves differently (§11.3). Other names in clinical use, not in the ontologies: *congenital sacrococcygeal teratoma*, *coccygeal teratoma*, *SCT*. Note the HPO sibling term **`HP:0009793` "Presacral teratoma"** exists separately from `HP:0030736` and is the term the Currarino literature maps to.

### 1.4 Information provenance

The content below is **disease-level aggregated**, not patient-level. The strongest sources are:

- two **national/registry population-based** series (Finland, Hawaii) for incidence;
- one **global retrospective cohort** of 3,407 patients across 145 institutes in 62 countries for malignancy and recurrence (PMID:39248311);
- **systematic reviews and meta-analyses** for prenatal prognostic factors (PMID:37964422), AFP diagnostic accuracy (PMID:32376010), malignant recurrence after mature SCT (PMID:33142194) and fetal intervention outcomes (PMID:38731178);
- **NCI PDQ** (updated 5 November 2024) and the **COG 2023 Blueprint** (PMID:37449938) for staging, chemotherapy and risk stratification.

No EHR-derived phenotype profile, no OMOP cohort definition and no dataset-level omics resource specific to SCT was identified. There is **no GeneReviews chapter** for sacrococcygeal teratoma — as expected for a non-Mendelian condition — so the mandatory Mendelian phenotype baseline does not apply here; run `just check-genereviews` and record the result rather than asserting absence from this report.

---

## 2. Etiology

### 2.1 Causal factors

**The initiating lesion is developmental and epigenetic, not mutational.** SCT is a **type I germ cell tumour** in the Oosterhuis–Looijenga developmental classification: a tumour of early, still-migrating primordial germ cells (PGCs) or of residual totipotent primitive-streak cells, arising in the one body region where pluripotency persists latest in gastrulation.

Two non-exclusive origin hypotheses, both still current:

1. **Residual totipotent primitive-streak / Hensen's-node cells.** The classic account, stated in the 2013 review as: *"the source of totipotential cells is a residual cell from the primitive streak and Hansen node of very early embryonic development"* (Szyllo & Lesnik, PMID:23569550). This explains the anatomy directly: the caudal cell mass is the last remnant of the primitive streak, and it sits exactly where SCTs grow.
2. **Mismigrated primordial germ cells with aberrant reprogramming.** Phi's 2021 synthesis (PMID:33906346) states that early PGCs *undergo abnormal reprogramming to attain pluripotency, becoming embryonic stem-like cells that survive without KIT signalling and form teratomas* — and critically that *"Type I GCTs demonstrate partially erased genomic imprinting patterns characteristic of early migrating PGCs,"* contrasting with type II tumours whose imprints are fully erased. The imprinting signature is therefore evidence *for* a germ-cell origin and *for* a specific, early developmental window.

The two hypotheses converge on the same mechanistic requirement — a cell that retains or re-acquires pluripotency in the caudal midline — and the imprinting data arbitrate the timing rather than the cell. This is the single most important mechanistic claim to curate, and §6 gives the ordered chain.

**Currarino syndrome is the one genuinely causal genetic etiology in this anatomical region, and it is a different disease.** Heterozygous loss of **MNX1** (`hgnc:4979`) causes the autosomal dominant triad of sacral bone defect, anorectal malformation and presacral mass. Roughly half of Currarino cases carry an *MNX1* variant; detection is far higher in familial than in sporadic cases (reported as ~57% overall, with no variant in ~8% of familial but ~68% of sporadic patients). The presacral mass in Currarino may be a teratoma, an anterior meningocele (`HP:0007293`) or an enteric cyst. **The malignant behaviour differs and this is now established on two independent cohorts (§11.3), so lumping the two would be a curation error.** A `Currarino_Triad.yaml` entry already exists in this repository bound to `MONDO:0008305`; the SCT entry should relate to it rather than absorb it.

### 2.2 Risk factors

**Genetic.**

- **No germline causal variant.** Phi (PMID:33906346) states most cases are sporadic, with *no consistent familial tendency* unlike testicular GCTs.
- **Susceptibility loci (germ cell tumour, not SCT-specific).** The adult testicular GCT GWAS loci partly transfer to paediatric disease. Poynter et al. 2012 (PMID:22072546) tested *KITLG*, *SPRY4*, *BAK1* and *DMRT1*; Marcotte et al. 2017 (`10.1002/gcc.22457`) reported *BAK1* rs210138 positively associated with GCT with a strong effect for testicular tumours, *SPRY4* rs4624820 associated with reduced risk, and a *GAB2* association. The retrieved summary records that *KITLG* and *SPRY4* were significant **only in the adolescent** age group and *BAK1* in the paediatric group. These are susceptibility signals in mixed GCT cohorts — **do not curate any of them as an SCT risk factor without checking the site stratification in the source**, which is the Named Entity Confusion risk here.
- **Family history of twinning** is reported in 10–15% of cases (Phi, PMID:33906346), and the fetus-in-fetu literature notes both entities are *"more prevalent in families with a history of twinning."* This is an association in case series, not a measured relative risk.
- **No chromosomal syndrome** is established as predisposing. Major birth defects co-occurred in 31.8% of infant teratoma cases in the Hawaii registry (PMID:16420341), but co-occurring malformation is not the same as a syndromic cause.

**Environmental / demographic.**

- **Female sex is the only robust risk factor.** Female-to-male ratio 3:1 to 4.6:1 across series; the Hawaii registry put females at 58.3% of sacrococcygeal cases (PMID:16420341) — a notably weaker skew than the 4:1 of referral series, which is what a population denominator usually does to a referral statistic.
- Beyond sex, risk factors are **not defined**. No toxin, drug, radiation, occupational or dietary exposure has been established. Maternal age has not been shown to be a risk factor in any case-control study located in this run.
- Twin gestation is over-represented in case series (3 twin sets among 30 cases, 10%, in one series) but the denominator problem is unresolved.

### 2.3 Protective factors

**None identified, genetic or environmental.** There is no reported protective allele, no dietary or lifestyle factor, and no plausible primary-prevention target — which follows from the etiology being a stochastic event in week-3 gastrulation. For a `protective` or `environmental` block, the honest curation is absence with the search recorded, using the `Left deliberately uncited.` waiver convention if an `environmental[]` entry is created at all. **Recommendation: do not create an `environmental[]` block for this entry.** There is nothing to put in it, and an empty or speculative one would be worse than none.

### 2.4 Gene–environment interactions

**No gene–environment interaction has been reported for SCT.** CTD, PheGenI and the GxE literature return nothing specific. This is the expected state for a tumour whose initiating event precedes most postnatal exposure.

---

## 3. Phenotypes

### 3.1 Presentation by Altman type and timing

The **Altman classification** (Altman RP, Randolph JG, Lilly JR. *Sacrococcygeal teratoma: American Academy of Pediatrics Surgical Section Survey-1973.* J Pediatr Surg. 1974;9(3):389–98. PMID:4843993; DOI 10.1016/s0022-3468(74)80297-6) is derived from 405 patients and remains the reference description. It classifies by the balance of external and presacral components, and the type predicts both the operation and the malignancy risk.

| Altman type | Anatomy | Frequency (neonatal series) | Metastasis / malignancy |
|---|---|---|---|
| **I** | Predominantly external, attached to coccyx, minimal presacral component | 45–46% | lowest; no metastases in the original survey |
| **II** | External mass with significant intrapelvic extension | 34–35% | ~6% metastasis rate in the original survey |
| **III** | Visible externally but predominantly pelvic/intra-abdominal | 8.6–10% | higher |
| **IV** | **Presacral only, no external component** | ~10% | **highest**; presents late, so highest malignant potential |

Two consequences worth curating explicitly: **type IV is the dangerous one precisely because it is invisible**, presenting in older infants or adults with pelvic symptoms rather than at birth; and in **adults**, type III is the commonest presentation, inverting the neonatal distribution.

Timing: *"50–70% are found during first few days of life, less than 10% are diagnosed beyond the age of two years"* (PMID:23569550). Prenatal detection accounts for roughly 25–50% of cases (Phi, PMID:33906346).

### 3.2 Phenotype table with HPO suggestions

All CURIEs below were read from `cache/hp/terms.csv` in this session except `HP:0030736` (OLS). Frequencies are from the sources named; where a frequency is a referral-series figure rather than a population one, that is stated.

| Phenotype | HPO term | Onset | Frequency | Severity / course | Source |
|---|---|---|---|---|---|
| Sacrococcygeal teratoma (the lesion) | **`HP:0030736`** Sacrococcygeal teratoma | congenital | 100% (definitional) | — | MONDO/HPO |
| Presacral teratoma (type IV / Currarino overlap) | **`HP:0009793`** Presacral teratoma | congenital, often late-presenting | ~10% of SCT | — | PMID:4843993 |
| Germ cell neoplasia (parent concept) | **`HP:0100728`** Germ cell neoplasia | congenital | 100% | — | HPO |
| **Non-immune hydrops fetalis** | **`HP:0001790`** Nonimmune hydrops fetalis (parent `HP:0001789` Hydrops fetalis) | fetal, usually 2nd–3rd trimester | the dominant lethal complication; OR **21.0** (CI 2.6–275.1) for poor outcome | severe, progressive, usually irreversible once advanced | PMID:34327722 |
| **High-output congestive heart failure** | **`HP:0001722`** High-output congestive heart failure | fetal | present in a substantial minority of large solid tumours | severe, progressive | PMID:24488859 |
| Cardiomegaly | **`HP:0001640`** Cardiomegaly | fetal | one of five meta-analysis-confirmed predictors | progressive | PMID:37964422 |
| Polyhydramnios | **`HP:0001561`** Polyhydramnios | fetal | significantly commoner in non-survivors (p<0.001) | drives preterm labour | PMID:38731178 |
| Large placenta (placentomegaly) | **`HP:0006267`** Large placenta | fetal | meta-analysis-confirmed predictor | marker of irreversibility | PMID:37964422 |
| Premature birth | **`HP:0001622`** Premature birth | fetal/neonatal | very common in intervention cohorts (mean GA 29.7 ± 4.0 wk after minimally invasive therapy) | — | PMID:24488859 |
| Stillbirth | **`HP:0003826`** Stillbirth | fetal | **10%** of a national cohort of 124 | lethal | PMID:23432104 |
| Elevated circulating AFP | **`HP:0006254`** Elevated circulating alpha-fetoprotein concentration | neonatal onwards | 75% of recurrences; **must be interpreted against age-specific norms** (§10.2) | marker, not symptom | PMID:32376010 |
| Elevated amniotic fluid AFP | **`HP:0004639`** Elevated amniotic fluid alpha-fetoprotein concentration | fetal | not quantified | — | flagged, frequency unsourced |
| Hydronephrosis | **`HP:0000126`** Hydronephrosis | fetal/neonatal | commonest urogenital association | obstructive; may resolve after resection | Phi, PMID:33906346 |
| **Neurogenic bladder** | **`HP:0000011`** Neurogenic bladder | postoperative, childhood | part of the 13–33% urological sequelae band | chronic, often lifelong | PMID:17560233; PMID:33906346 |
| **Urinary incontinence** | **`HP:0000020`** Urinary incontinence | childhood onwards | **31%** (national cohort); ~13% in a 353-patient series | chronic | PMID:17560233 |
| **Bowel incontinence** | **`HP:0002607`** Bowel incontinence | childhood onwards | 9% involuntary bowel movements, 13% soiling (national cohort) | chronic | PMID:17560233 |
| Constipation | **`HP:0002019`** Constipation (chronic: `HP:0012450`) | childhood onwards | **17%** | chronic | PMID:17560233 |
| Anal atresia (Currarino context) | **`HP:0002023`** Anal atresia | congenital | definitional in Currarino, not in SCT | — | OMIM 176450 |
| Dysplastic / absent sacrum | **`HP:0008455`** Dysplastic sacrum; **`HP:0008517`** Aplasia/Hypoplasia of the sacrum; **`HP:0009790`** Hemisacrum | congenital | Currarino context | — | OMIM 176450 |
| Absent/hypoplastic coccyx | **`HP:0008436`** Absent/hypoplastic coccyx | postoperative (coccygectomy) or congenital | universal after correct surgery | — | §12 |
| Anterior sacral meningocele | **`HP:0007293`** Anterior sacral meningocele | congenital | Currarino alternative mass | — | OMIM 176450 |
| Spina bifida | **`HP:0002414`** Spina bifida | congenital | part of the 15–30% anomaly burden | — | Phi, PMID:33906346 |
| Hip dysplasia | **`HP:0001385`** Hip dysplasia | congenital | commonest musculoskeletal association | — | UpToDate-class sources |
| Lower-limb motor dysfunction | no verified HP CURIE located this run `[CURIE NOT VERIFIED]` | childhood | **4.2%** (15/353) | chronic | 353-patient series |

**Congenital anomalies overall: 15–30% of infants with SCT** (Phi, PMID:33906346), most commonly musculoskeletal, nervous-system, urogenital and cardiac. The Hawaii population registry's independent figure — *"Major birth defects were identified in 7 (31.8%) of the cases"* (PMID:16420341) — sits at the top of that band and is population-based, so it is the better one to cite.

### 3.3 Quality of life

Derikx et al. 2007 (PMID:17560233) is the key paper and the one that makes the QoL claim quantitatively rather than rhetorically. From the abstract: *"There were 46% who reported impaired bowel function and/or urinary incontinence"*; *"31% urinary incontinence"*; *"In 40%, the scar was cosmetically unacceptable"*; and decisively, *"Long-term sequelae were correlated with diminished QoL."*

Two things follow for curation. First, the **cosmetic** outcome is a first-class QoL finding in this disease, not a footnote — 40% unacceptable scar is a higher figure than most of the functional sequelae. Second, no disease-specific PRO instrument exists for SCT; published work uses generic instruments. A structured `clinical_burden` block should record the functional and cosmetic domains separately.

A systematic review of "real-world" long-term functional outcomes reports impaired bowel function across studies at **19–38%** and urinary incontinence at **approximately 50%** — wider bands than Derikx, reflecting heterogeneous ascertainment. The 353-patient series gives the lowest figures: 83/353 (23.4%) with any functional sequela, 62 (17.5%) anorectal, 56 (13.0%) urinary, 15 (4.2%) lower-limb motor. **The spread between 13% and 50% for urinary dysfunction is the honest state of the evidence and should be curated as a range with its sources, not collapsed to a single number.**

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes

**None for SCT.** This must be stated positively in the entry rather than left as an empty `genetic:` block, because an absent block reads as un-curated. The accurate statement: SCT has no germline causal gene; it is a sporadic developmental germ cell tumour.

**MNX1** (`hgnc:4979`, OMIM \*142994, 7q36.3) is causal for **Currarino syndrome** (`MONDO:0008305`, OMIM #176450), autosomal dominant, with variable penetrance and expressivity even within one family, and detected in roughly half of cases. Curate it on the Currarino entry, and relate the two entries rather than putting *MNX1* in the SCT `genetic:` section.

### 4.2 Somatic molecular profile

The primary source is **Kubota Y, Seki M, Kawai T, et al. Comprehensive genetic analysis of pediatric germ cell tumors identifies potential drug targets. Commun Biol. 2020;3(1):544. PMID:32999426; DOI 10.1038/s42003-020-01267-8** — 51 paediatric GCT samples (25 female, 26 male): 6 germinomas, 2 embryonal carcinomas, 4 immature teratomas, 3 mature teratomas, 30 yolk sac tumours, 6 mixed. **Six sacrococcygeal samples** were included (~12% of the cohort).

Findings relevant to SCT:

- **Copy number.** In yolk sac tumours: *"gains of chromosome 1q (14 samples), 12p (nine samples), and 20q (23 samples)"*, with losses at 4q (13), 6q (13) and 16 (13). (One further arm-level loss reported in the same sentence is omitted here under content fence (b).) The COG Blueprint states the type-level pattern as: *"Type I tumors show recurrent gains in 12p, 20q and 21 … while type II have gains in 12p (commonly isochromosome i12p)"* (PMID:37449938).
- **Isochromosome 12p is an age marker, not an SCT marker.** *"Isochromosome 12p in YST samples was detected only in older children"*, and the broader literature records that *all samples with isochromosome 12p belonged to children aged >10 years*. Sacrococcygeal samples showed the **infant-type** pattern. **This is the single most important molecular distinction for this entry: i(12p), the canonical GCT lesion, is a feature of post-pubertal type II tumours and must not be attributed to neonatal SCT.**
- **Methylation.** Consensus clustering split GCTs into two clusters matching histology (teratoma vs yolk sac tumour); sacrococcygeal samples clustered with the infant-type group and showed a *"partially common methylation pattern with ES cells"*.
- **Point mutations are rare.** *"KIT, KRAS, and NRAS mutations were detected in one, three, and one YST sample, respectively"* — in older children only. The COG Blueprint reports TCGA frequencies of *KIT, KRAS* and *NRAS* at *"18%, 14% and 4% of tumors respectively"* in malignant GCT generally, which is adult/adolescent data. Phi's review notes testicular GCTs carry a minimal mutational burden of **0.3–0.5 mutations/Mb**. **Mature neonatal SCT is, to a first approximation, a genomically quiet tumour.**
- **Proposed targets:** *KIT, TNFRSF8* and *ERBB4*; for yolk sac tumours specifically *ERBB4*. KIT signalling is relevant because it *"is essential for migration and proliferation of primordial germ cells"*.

Verified gene CURIEs for any of this that is curated: `hgnc:6342` KIT, `hgnc:6343` KITLG, `hgnc:6407` KRAS, `hgnc:7989` NRAS, `hgnc:15924` SALL4, `hgnc:9221` POU5F1, `hgnc:20857` NANOG, `hgnc:11195` SOX2, `hgnc:4451` GPC3, `hgnc:11998` TP53, `hgnc:4979` MNX1. **`BAK1`, `SPRY4`, `GAB2`, `DMRT1`, `DND1` and `AFP` are not in `cache/hgnc/terms.csv`** — look them up at HGNC before binding `[CURIE NOT VERIFIED]`.

### 4.3 Variant classification, allele frequency, origin

- **Germline pathogenic variants: none for SCT.** ClinVar/ClinGen carry no gene–disease validity assertion for sacrococcygeal teratoma; do not populate `gene_disease_validity`.
- **Somatic:** the *KIT*/*KRAS*/*NRAS* changes above are somatic activating mutations, present in a minority of malignant (yolk sac) components, essentially confined to older children. `variant_origin: SOMATIC`, `functional_impact_category: GAIN_OF_FUNCTION`.
- **Susceptibility SNPs** (*BAK1* rs210138, *SPRY4* rs4624820, plus *KITLG* and *GAB2* variants) are common polymorphisms; their population frequencies are in gnomAD but were not read this session. If curated, they belong as `relationship_type: SUSCEPTIBILITY` with the age-group stratification preserved.

### 4.4 Modifier genes

**None established.** Mouse genetics gives the only modifier evidence of any kind, and it is strain background rather than a named modifier: the *Dnd1^Ter* teratoma phenotype *"occurs only on the 129 strain background"* (§15), and *Dnd1* acts with *Nanos2* and *Nanos3*. There is no human modifier data.

### 4.5 Epigenetics — the mechanistically central layer

This is where the molecular biology of SCT actually lives, and it should be curated as mechanism (§6) rather than as an afterthought in a genetics block.

- **Imprinting is partially erased, matching early PGCs.** The retrieved synthesis: *"Sacrococcygeal teratomas showed a bimodal global methylation and somatic imprinting status, a profile comparable with that of early PGCs, which are on the global demethylation and prior to imprinting erasure."* Phi (PMID:33906346) states type I GCTs have *partially* erased imprinting, type II *completely* erased.
- **SCT is biparental, not parthenogenetic.** This distinguishes it sharply from mature ovarian teratoma: *"sacrococcygeal teratomas differ from parthenogenetic ovarian teratomas in their imprinting patterns due to their biparental origin."* A comparative study of imprinted-gene methylation across mature ovarian teratoma, complete hydatidiform mole and extragonadal mature teratoma (Mod Pathol / Nature, `10.1038/s41379-020-00668-8`) is the source to fetch for this. **Curating SCT as parthenogenetic would be a substantive error.**
- **Methylation and chemosensitivity.** The COG Blueprint: *"When comparing GCT cell lines that become cisplatin-resistant, there is an increase in global DNA methylation,"* with DNA methyltransferase inhibitors (guadecitabine) restoring sensitivity preclinically. This is a therapeutic hypothesis, not established practice.

**GO term caution:** `GO:0080111` *DNA demethylation* and `GO:0006306` *DNA methylation* are both recorded as **obsolete** in `cache/go/terms.csv`. Do not bind either. Usable verified alternatives: `GO:0071514` genomic imprinting, `GO:0141068` autosome genomic imprinting, `GO:0141166` chromosomal 5-methylcytosine DNA demethylation pathway, `GO:0070988` demethylation.

### 4.6 Chromosomal abnormalities

No recurrent germline karyotypic abnormality. Somatic arm-level changes as in §4.2. Chromosomal microarray and karyotype have no established diagnostic role in SCT.

---

## 5. Environmental Information

- **Environmental factors:** none established. No toxin, radiation, pollutant or occupational exposure is linked to SCT in CTD, EPA resources or the clinical literature.
- **Lifestyle factors:** none established.
- **Infectious agents:** not applicable. SCT is a neoplasm of embryonic origin with no infectious etiology.

**Curation recommendation:** leave `environmental:` absent. If it is created for completeness, every row needs the `Left deliberately uncited.` waiver in `review_notes` with the searches recorded — and a block of waivers is a worse entry than no block.

---

## 6. Mechanism / Pathophysiology

### 6.1 The ordered causal chain

**Trunk — tumour genesis (steps 1–5):**

1. During gastrulation (≈week 3), primordial germ cells are specified in the posterior epiblast and transit the **primitive streak** (`UBERON:0004341`) and **primitive knot / Hensen's node** (`UBERON:0003062`); the caudal cell mass is the last region in which pluripotent cells persist. → **leads to** a transient population of pluripotent cells in the caudal midline. *(Demonstrated developmental biology; the inference to SCT is step 2.)*
2. A subset of these cells — either mismigrating early PGCs or residual totipotent primitive-streak cells — **fails to complete migration** to the gonadal ridge and is **retained in the presacral/coccygeal mesenchyme**. → **results in** an ectopic pluripotent clone at the base of the coccyx. *(Inferred from tumour site and imprinting signature; not directly observed in human embryos.)*
3. The retained cells undergo **aberrant epigenetic reprogramming**, arresting with globally demethylated DNA and **only partially erased somatic imprints**, i.e. an early-PGC/ES-cell-like state. → **results in** acquisition of embryonic-stem-cell-like pluripotency. *(Supported by direct imprinting and methylation measurement in SCT tissue — this is the best-evidenced molecular step.)*
4. The reprogrammed cells **survive independently of KITLG–KIT signalling**, which normally restricts PGC survival to the migratory niche. → **leads to** escape from the niche dependency that would otherwise eliminate an ectopic germ cell. *(Mechanism stated in review synthesis; the KIT-independence claim rests on mouse and cell-line work, so grade as `INDIRECT`.)*
5. The surviving pluripotent clone **proliferates and differentiates along all three germ layers**. → **results in** a teratoma containing ectodermal, mesodermal and endodermal derivatives — a type I GCT, mature or immature by the proportion of neuroepithelial immaturity.

**Branch A — mass effect (mechanical):**

6. Tumour expansion in the pelvis and presacral space → **compresses** the ureters, bladder outlet and rectum → **hydronephrosis** (`HP:0000126`), bladder dysfunction, constipation; and at delivery, **obstructed labour / dystocia**.

**Branch B — haemodynamic, the lethal fetal pathway:**

7. The growing tumour undergoes **neovascularisation with low-resistance arteriovenous shunts**: *"As the SCT grows it develops increasing vascularity with arteriovenous shunting within the SCT"* and *"The teratoma acts as a large arteriovenous shunt."* → **results in** a large, low-resistance parallel circuit.
8. The shunt **increases venous return and combined ventricular output** → **leads to** tachycardia, ventricular dilatation and **cardiomegaly** (`HP:0001640`), with tricuspid and mitral regurgitation and extreme IVC enlargement on Doppler.
9. Sustained volume overload → **results in** **high-output cardiac failure** (`HP:0001722`).
10. Cardiac failure → **results in** **non-immune hydrops fetalis** (`HP:0001790`): ascites, pleural and pericardial effusions, skin oedema — with **placentomegaly** (`HP:0006267`) from the same mechanism ("placental steal").
11. The oedematous placenta releases vasoactive factors/endothelial toxins → **leads to** **maternal mirror syndrome**: a preeclampsia-like maternal illness with hypertension, peripheral oedema, proteinuria, vomiting and pulmonary oedema. *(Mechanistic attribution to placental factors is inferred, not demonstrated.)*
12. Parallel sub-branch: **polyhydramnios** (`HP:0001561`) → **leads to** preterm labour and **premature birth** (`HP:0001622`).
13. Parallel sub-branch: **intratumoral haemorrhage or tumour rupture** → **results in** fetal/neonatal anaemia and consumptive coagulopathy, which further **aggravates** step 9.
14. Endpoint: intrauterine fetal demise, **stillbirth** (`HP:0003826`), or neonatal death from prematurity plus failure.

**Branch C — malignant transformation:**

15. Persistence of undifferentiated, yolk-sac-committed cells within the teratoma — as **microscopic yolk sac tumour deposits**, found in 16% of nominally mature SCTs — → **leads to** AFP-secreting **yolk sac tumour** (`MONDO:0005744`, already curated here as `Yolk_Sac_Tumor.yaml`), either at presentation or at recurrence.
16. Time from birth without resection → **increases** the probability that malignant histology is present at operation, from 3.3% at 3 months to a 64.2% plateau beyond 6 years. *(This is the strongest quantitative causal claim in the whole disease, from 3,407 patients.)*

**Branch D — iatrogenic / postoperative:**

17. Resection through the presacral space → **injures** pelvic splanchnic nerves and sacral roots and disrupts the pelvic floor → **results in** neurogenic bladder (`HP:0000011`), urinary and bowel incontinence, constipation, and lower-limb motor dysfunction. The adult presacral series quantifies this directly: *"postoperative complications (31%) that may be expected are bladder dysfunction (15%), incontinence for faeces (7%) and dysesthesia (7%), especially in the case of damage to pelvic splanchnic nerves."*

**Separate chain — the Currarino lesion (do not merge):** heterozygous *MNX1* loss → caudal developmental field defect → sacral bone defect + anorectal malformation + presacral mass (teratoma, anterior meningocele or enteric cyst) → low malignant potential (§11.3).

### 6.2 Coverage of the requested mechanism categories

| Category | Content | Suggested terms (verified unless flagged) |
|---|---|---|
| **Molecular pathways** | KITLG–KIT receptor tyrosine kinase signalling governs PGC migration and survival; *SPRY4* is an RTK inhibitor shown to abrogate KIT signalling; downstream RAS/MAPK (*KRAS*, *NRAS* mutations in malignant components). **WNT/β-catenin** is the newest signal: *"Patients whose tumors had ≥5 changes in the WNT pathway had higher beta-catenin expression and lower EFS and OS"* (PMID:37449938) — and it is druggable (tegavivint, NCT04851119). | `hgnc:6342` KIT, `hgnc:6343` KITLG; GO terms for KIT and WNT signalling `[CURIE NOT VERIFIED]` |
| **Cellular processes** | Germ cell migration; germ cell development; maintenance of a pluripotent state; multilineage differentiation; apoptosis evasion (*BAK1* susceptibility is an anti-apoptotic signal — Phi notes *BAK1* variants associated with type I GCTs); tumour angiogenesis | `GO:0008354` germ cell migration, `GO:0007281` germ cell development, `GO:0019827` stem cell population maintenance, `GO:0006915` apoptotic process, `GO:0001525` angiogenesis, `GO:0001944` vasculature development, `GO:0071514` genomic imprinting, `GO:0008015` blood circulation |
| **Protein dysfunction** | No misfolding/aggregation mechanism. The relevant protein biology is **transcription-factor-driven pluripotency** (POU5F1/OCT4, NANOG, SOX2, SALL4) and receptor signalling, not protein damage. | `hgnc:9221`, `hgnc:20857`, `hgnc:11195`, `hgnc:15924` |
| **Metabolic changes** | None specific. AFP secretion by yolk-sac elements is a **differentiation marker**, not a metabolic defect — a distinction worth preserving in the entry. | — |
| **Immune involvement** | No autoimmune, immunodeficiency or chronic-inflammatory mechanism. Immunotherapeutic *targets* exist (GPC3 via codrituzumab, CLDN6 CAR-T) but these are therapeutic, not pathogenic. | `hgnc:4451` GPC3 |
| **Tissue damage** | Fetal: congestive organ injury from high-output failure (hepatomegaly, serous effusions); haemorrhage/necrosis within the tumour. Postnatal: surgical nerve injury. No oxidative-stress or fibrosis mechanism is established. | `UBERON:0001987` placenta |
| **Biochemical abnormalities** | No enzyme deficiency, receptor loss or channelopathy. | — |
| **Epigenetic changes** | §4.5 — the central mechanism. Partial imprint erasure; biparental origin; global demethylation; methylation increase with cisplatin resistance. | `GO:0071514`, `GO:0141068`, `GO:0141166` — **not** the obsolete `GO:0080111` |
| **Transcriptomics** | Kubota 2020 expression clustering by histology; no SCT-specific GEO series identified. `just discover-datasets Sacrococcygeal_Teratoma` is the next step. | — |
| **Proteomics / metabolomics / lipidomics** | **No SCT-specific studies identified.** State as a knowledge gap. | — |
| **Single-cell / spatial** | **None identified for SCT.** A genuine `KNOWLEDGE_GAP` candidate: single-cell profiling of a human SCT against a fetal PGC reference would directly test the origin hypothesis of steps 2–3. | — |
| **Functional genomic screens** | None SCT-specific. GCT cell lines in DepMap are adult testicular. | — |
| **Circulating biomarkers (emerging)** | *"The identification of circulating miR-371a-3p is one of the biggest recent biological breakthroughs for patients with testicular tumors"* — sensitivity 90.1%, specificity 94% (PMID:37449938). **Note: miR-371a-3p is not expressed by teratoma**, so its utility in a predominantly teratomatous SCT is limited; verify this before carrying it over. | — |

### 6.3 Cell types and anatomy involved in the mechanism

Verified CL terms: **`CL:0000670`** primordial germ cell (the proposed cell of origin), `CL:0000586` germ cell, `CL:0002248` pluripotent stem cell, `CL:0002322` embryonic stem cell, `CL:0000115` endothelial cell and `CL:0000071` blood vessel endothelial cell (the AV-shunt vasculature of Branch B).

**Cell of origin (derived, per this repository's convention):** SCT has **no recorded host somatic lesion** — there is no mutation for `variant_origin: SOMATIC` to describe in a mature neonatal SCT, and no initiating environmental exposure either. This entry therefore falls into the class `just check-cancer-origin` reports as *not saying where it starts*, and that is the correct answer rather than a defect to paper over. Do **not** mark a node `SOMATIC` to make the derivation fire: the origin claim here is a developmental/epigenetic one that the existing derivation rules cannot express. Record the proposed origin cell (`CL:0000670`) on the genesis node and state the limitation in `notes:`.

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

**Primary site:** the sacrococcygeal region — **coccyx `UBERON:0001350`** (verified via OLS this session), adjacent **sacral vertebra `UBERON:0001094`**, and the presacral/retrorectal space. *No UBERON term for "presacral space" or "retrorectal space" was located this run* `[CURIE NOT VERIFIED]`; search UBERON before binding, and if none exists, carry the specificity in `preferred_term` over a broader anchor rather than manufacturing a match.

**Secondary / compressed or congested:**

| Structure | UBERON | Involvement |
|---|---|---|
| rectum | `UBERON:0001052` | anterior displacement, compression, postoperative dysfunction |
| urinary bladder | `UBERON:0001255` | outlet obstruction; postoperative neurogenic bladder |
| bony pelvis | `UBERON:0001270` | intrapelvic extension (Altman II–IV) |
| perineum | `UBERON:0002356` | external component, surgical approach |
| abdominal cavity | `UBERON:0003684` | Altman III extension |
| spinal cord | `UBERON:0002240` | **rare** intradural/intraspinal extension — *"extremely rare and only reported in a few cases"*; a literature review yielded 6 cases. Must be excluded by MRI before resection |
| placenta | `UBERON:0001987` | placentomegaly from high-output failure |
| gonad | `UBERON:0000991` | the destination the cell of origin failed to reach — developmental, not involved |

**Body systems:** musculoskeletal (sacrococcygeal skeleton), nervous (sacral roots, pelvic autonomics, rare cord involvement), genitourinary, gastrointestinal/anorectal, cardiovascular (fetal high-output failure — the system that kills), reproductive (germ cell lineage).

**Developmental structures:** **primitive streak `UBERON:0004341`**, **primitive knot (Hensen's node) `UBERON:0003062`** — both verified via OLS. These belong on the genesis node, and `UBERON:0003062` is the precise anchor for the "Hensen's node" claim that the classic literature makes loosely.

### 7.2 Tissue and cell level

The tumour contains derivatives of **all three germ layers** by definition: neuroectoderm (the tissue whose immaturity defines the grade), skin and adnexa, respiratory and gastrointestinal epithelium, cartilage, bone, smooth and skeletal muscle, adipose. Immature elements are predominantly **neuroepithelial**, which is why grading is anchored on neuroepithelium. Malignant elements are almost always **yolk sac tumour**.

### 7.3 Subcellular level

**No subcellular compartment is specifically implicated.** The mechanism is nuclear/epigenomic in the loose sense of chromatin state, but no GO Cellular Component binding is justified by the evidence. Leave absent rather than binding `GO:0005634` nucleus to look complete.

### 7.4 Localization and lateralization

**Midline, caudal, exophytic from the coccyx.** The lesion is a midline structure and is not meaningfully lateralized, though large tumours are frequently asymmetric in their external projection. Oosterhuis et al. 2007 (*Int J Androl*, `10.1111/j.1365-2605.2007.00793.x`) is the conceptual source for why extragonadal GCTs are midline at all: *"Human germ cell tumours occur in the gonads … and also in extragonadal sites, where migrating primordial germ cells are located during embryogenesis,"* with the cranium and sacrococcygeal region the common paediatric sites. **The midline distribution is itself evidence for the migration hypothesis**, and is worth curating as such.

---

## 8. Temporal Development

### 8.1 Onset

- **Congenital.** The initiating event is in week 3 of gestation; the tumour is present at birth in essentially all true SCTs.
- **Detection:** prenatally in ~25–50% of cases, typically at the second-trimester anomaly scan. Median gestational age at diagnosis **22 weeks** (IQR 18–23) in a 55-fetus multicentre series (PMID:39482803); median 23 weeks in a smaller series.
- **Postnatal presentation:** 50–70% in the first few days of life; <10% beyond age 2 years. Altman type IV, having no external component, is the type that presents late — in older children or adults with pelvic pain, constipation, incomplete evacuation, narrowed stools, urinary frequency, or lower-limb paraesthesia.
- **Onset pattern:** congenital and, in utero, often **rapidly progressive**. Growth velocity is now a validated prognostic axis: *"Tumor growth velocity ≥ 7 mm/week appears to be an appropriate discriminative cut-off for poor perinatal outcome"* (PMID:39482803).

### 8.2 Progression and staging

SCT uses **COG staging for extragonadal germ cell tumours** (NCI PDQ, updated 5 November 2024), not a TNM system:

- **Stage I** — complete resection with negative margins, intact capsule, negative peritoneal cytology, lymph nodes ≤1 cm. For the sacrococcygeal site, **coccygectomy is written into the stage definition**. *"Tumor capsule cannot have been violated by needle biopsy, incisional biopsy, or tumor rupture."*
- **Stage II** — microscopic residual disease, or gross resection with preoperative biopsy/capsular disruption; nodes negative.
- **Stage III** — gross residual disease or lymph nodes ≥2 cm (or 1–2 cm unresolved on re-imaging).
- **Stage IV** — distant metastases (liver, lung, bone, brain).

**Progression rate** is bimodal. In utero: hours-to-days for hydrops once high-output failure begins, which is why fetal intervention has such a narrow window. Postnatally after complete resection: the disease is usually over, with a tail of recurrence at a median of **11.4 months** and documented as late as **22.1 years** (PMID:39248311).

**Course pattern:** for mature completely resected SCT, **self-limited after surgery**. For immature or malignant disease, **relapsing** with a defined surveillance window. 96% of recurrences occur before age 6 years, which is what sets the follow-up duration.

### 8.3 Patterns

- **Remission:** treatment-induced only. There is **no spontaneous regression** of SCT — a contrast with neonatal neuroblastoma worth keeping in mind, since both are congenital tumours of the same age group with opposite natural histories.
- **Critical periods — three distinct ones, and conflating them is a clinical error:**
  1. **18–28 weeks' gestation:** the window in which TFR and growth velocity predict outcome and in which fetal intervention can still reverse failure. Beyond advanced hydrops with placentomegaly or maternal preeclampsia, intervention is futile — *"Women who have fetuses with advanced hydrops, placentomegaly or maternal preeclampsia are not candidates for fetal intervention as these symptoms indicate an irreversible situation."*
  2. **Delivery planning, ≥32 weeks:** *"An attempt should be made to continue pregnancy until 32 weeks' gestation and that after this age infants should be delivered by elective cesarean section as soon as possible."*
  3. **First month of life:** the window for resection that minimises malignancy. The global cohort's recommendation is *"complete resection of SCT before 1 month of age"* when safe and feasible.
- **Growing teratoma syndrome** is a distinct temporal pattern after chemotherapy for malignant disease: an enlarging mass of purely mature teratoma despite normalised markers. A coccygeal case is reported (*"the first case of growing teratoma syndrome in the coccygeal region"*), with 20% MRI growth during chemotherapy and mature teratoma plus immature coccygeal cells on histology. Treatment is surgical, since teratoma is chemo- and radio-resistant.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

| Measure | Value | Population / source |
|---|---|---|
| **Total prevalence** | **1 : 10,700 pregnancies** | **Finland, nationwide, 1993–2010-ish: 124 SCT among 1,331,699 pregnancies.** Pauniaho SL et al. *High prevalence of sacrococcygeal teratoma in Finland — a nationwide population-based study.* Acta Paediatr. 2013;102(6):e251-6. **PMID:23432104** |
| Birth prevalence, live births | **0.43 per 10,000 live births** (≈1 : 23,000) | Hawaii birth-defects registry 1986–2001; 13 sacrococcygeal among 22 infant teratomas; all-teratoma rate 0.74/10,000. Forrester MB, Merz RD. Paediatr Perinat Epidemiol. 2006;20(1):54-8. **PMID:16420341** |
| Commonly quoted range | 1 : 20,000 – 1 : 40,000 live births | Phi JH, **PMID:33906346**; 1:35,000–40,000 in **PMID:23569550** |
| Adult incidence | 1 : 40,000 – 1 : 63,000 | **PMID:23569550** |
| Pregnancy outcome distribution | **72% live births, 10% stillbirths, 18% terminations** | Finland, **PMID:23432104** |
| Perinatal mortality | **28% of all SCT births** | Finland, **PMID:23432104** |

**The Finnish 1:10,700 and the Hawaiian 1:23,000 are not in conflict — they measure different things**, and the gap between them is itself informative. The Finnish denominator is *pregnancies* and the numerator includes stillbirths and terminations; the Hawaiian denominator is *live births*. Roughly 28% of Finnish SCT pregnancies did not produce a surviving infant, which accounts for most of the difference. **Curate both, with `measure_type` and `rate_denominator` set explicitly** — this is exactly the case the `PrevalenceMeasureEnum` / `RateDenominatorEnum` distinction exists for, and collapsing them into one "incidence" figure would destroy the information.

For a `prevalence_class` band: 1:10,700 pregnancies ≈ 9.3 per 100,000, placing it in the 1–9 per 100,000 band; 0.43/10,000 live births = 4.3 per 100,000, same band. **Note that `rate_denominator: LIVE_BIRTHS` applies to the Hawaii figure and `POPULATION` is wrong for both.**

### 9.2 Inheritance

**SCT itself: sporadic, non-Mendelian.** No inheritance pattern; `inheritance:` should either be absent or record sporadic occurrence explicitly. Not polygenic in any demonstrated sense — the GWAS loci of §2.2 are GCT-wide susceptibility signals, not an SCT polygenic architecture.

**Currarino syndrome: autosomal dominant**, *MNX1*, with **variable penetrance and expressivity even within one family**. Curate on `Currarino_Triad.yaml`. Penetrance is not quantified; expressivity is explicitly variable; no anticipation; germline mosaicism not reported; no founder effect or carrier-frequency data located. *MNX1* variant detection in Currarino: ~57% overall, ~92% of familial, ~32% of sporadic cases (i.e. no variant in 7.7% of familial and 68% of sporadic) — **re-read these percentages from the source before curating; the retrieved phrasing is ambiguous between "no mutation detected in 7.7% of familial" and the complement.**

### 9.3 Population demographics

- **Sex ratio: female predominance, 3:1 to 4.6:1.** Referral series cluster at 4:1; the population registry gives 58.3% female for sacrococcygeal cases (≈1.4:1), and **the population figure should be preferred for any prevalence-linked statement**. Adult series: 3:1. No mechanism for the sex skew is established — a legitimate knowledge gap, and an interesting one given that the cell of origin is a germ cell.
- **Geographic distribution:** no established variation beyond the Finnish "high prevalence" finding, which the authors themselves frame as a *high prevalence* observation rather than a confirmed geographic difference, and which may reflect completeness of a nationwide register (including TOPs and stillbirths) rather than true excess risk. **Do not curate a Finnish geographic risk claim.**
- **Ancestry:** no HANCESTRO-bindable ancestry association identified. Do not populate `population_effects`.
- **Age distribution:** heavily neonatal (50–70% in the first days); a small childhood tail; rare adult presentations, almost all Altman III/IV.

---

## 10. Diagnostics

### 10.1 Imaging

- **Prenatal ultrasound** is the primary modality and the source of every prognostic metric in §11.1: tumour volume, solid-versus-cystic morphology, vascularity, growth velocity, cardiomegaly, hydrops, placentomegaly, polyhydramnios. Fetal echocardiography (`NCIT:C114079` Fetal Echocardiography Test) demonstrates *dilated ventricles and pericardial effusion … increased velocities and volume flows, along with tricuspid and mitral regurgitation* and *extreme enlargement of the inferior vena cava*.
- **Fetal MRI** (`NCIT:C16809` Magnetic Resonance Imaging) adds anatomical definition and is specifically better at two things: excluding **myelomeningocele** from the differential, and detecting intraspinal extension — *"in two fetuses, extension into the spinal canal was visible only on MRI."*
- **Postnatal MRI** is the standard for defining pelvic extent and spinal anatomy before resection, and is the surveillance modality that detects mature (AFP-negative) recurrence. In one series, *"two patients demonstrated recurrence of mature teratoma and were detected on surveillance magnetic resonance imaging."*
- CT (`NCIT:C17204`) and transvaginal/transrectal ultrasound are used in adult presacral presentations.

### 10.2 Laboratory and biomarkers

**Serum AFP is the single biomarker of the disease, and interpreting it requires the neonatal reference curve.** This is the most error-prone number in SCT care and should be curated as a `reference_ranges` block with `interpretation_bands`, not as prose.

From **Blohm ME, Vesterling-Hörner D, Calaminus G, Göbel U. *Alpha 1-fetoprotein (AFP) reference values in infants up to 2 years of age.* Pediatr Hematol Oncol. 1998;15(2):135-42. PMID:9592840:**

- *"At birth mean serum AFP levels were 41,687 ng/ml in 256 term babies and 158,125 ng/ml in 90 premature babies"*
- *"In the first 4 weeks of life, AFP levels decreased by 50% in 5.1 days in term babies."*
- *"Between day 180 and 720 of life, AFP levels up to 87 ng/ml were within the 95.5% interval … with a mean of 8 ng/ml"*

NCI PDQ states the clinical corollary plainly: *"The fetal liver produces AFP, and during the first year of life, infants have elevated serum AFP levels, which are not associated with the presence of a GCT,"* and *"The serum half-life of AFP is 5 to 7 days."* **A single raised neonatal AFP therefore says nothing; the trajectory against the age curve is the test.** Note the premature-infant value is nearly four times the term value — a trap in exactly the population (preterm delivery is common in SCT) where it matters most.

**Diagnostic accuracy for recurrence** — van Heurn LJ, Knipscheer MM, Derikx JPM, van Heurn LWE. J Pediatr Surg. 2020;55(9):1732-1739. **PMID:32376010**:

- *"The incidence of children developing recurrent sacrococcygeal teratoma (SCT) is 2-35%."*
- *"83 (75%) patients with recurrent SCT had elevated serum AFP levels."*
- *"The sensitivity and specificity of 79% and 95%, respectively."*
- *"The sensitivity of AFP levels to detect malignant recurrence was 96%."*

**The 79% overall versus 96% for malignant recurrence is the key asymmetry: AFP is near-perfect for the recurrence that matters and mediocre for mature recurrence, which is why MRI surveillance runs alongside it rather than instead of it.**

β-hCG is monitored alongside AFP per PDQ. For LOINC binding of AFP and the derived reference intervals, **look the codes up and seed `cache/loinc/terms.csv` with `just loinc-seed-cache` — do not type a LOINC label** (see the repository's LOINC rules).

### 10.3 Histopathology and immunohistochemistry

**Resection, never drainage or biopsy.** *"The definitive diagnosis is possible only after histopathological examination … Therefore the lesion should always be surgically removed. Drainage or biopsy is not recommended."* This is not merely a diagnostic-yield argument: capsular violation by needle or incisional biopsy **upstages** the tumour under COG criteria.

- **Grading (Gonzalez-Crussi)** for immature teratoma: Grade I <10% immature tissue, Grade II 10–50%, Grade III >50% — with grade 0 for fully mature. The frequency of additional **microscopic foci of malignant yolk sac tumour correlates with the grade of immaturity**, which is the mechanistic justification for grading at all.
- **IHC panel** (CAP protocol for extragonadal GCT): a general germ cell marker (**SALL4**), **OCT4**, **AFP** and **CD30**.
  - **SALL4** is *"a sensitive (100% sensitivity) marker for the diagnosis of extragonadal yolk sac tumor, more sensitive than PLAP, AFP, or glypican-3"* — from a study of 59 extragonadal yolk sac tumours **including 27 primary sacrococcygeal cases**, which makes it directly applicable here.
  - **OCT4** (`hgnc:9221` POU5F1): *"All 59 yolk sac tumors were negative for OCT4"* — OCT4 negativity excludes seminoma/germinoma and embryonal carcinoma.
  - **Glypican-3** (`hgnc:4451` GPC3): cytoplasmic and membranous reactivity in yolk sac tumour and choriocarcinoma, absent in embryonal carcinoma and germinoma.

### 10.4 Genetic testing

**Genetic testing has no role in diagnosing SCT.** No gene panel, WES, WGS, single-gene test, chromosomal microarray, karyotype, FISH, mtDNA or repeat-expansion test is indicated. This is a positive finding to curate, not an omission.

The exceptions, both narrow:
- ***MNX1* sequencing when the Currarino triad is suspected** — i.e. a presacral mass *with* a sacral bone defect and/or anorectal malformation, or a positive family history. ~50% detection rate, so a negative result does not exclude the syndrome.
- Somatic tumour profiling in relapsed/refractory malignant GCT, to identify *KIT* or RAS-pathway targets or WNT alterations for trial eligibility — research/trial context, not standard care.

### 10.5 Clinical criteria and differential diagnosis

Diagnosis is **imaging plus histology**; there are no society diagnostic criteria, no DSM/ICD operational definition, and no computable phenotype algorithm in the OHDSI/PheKB sense.

**Differential diagnosis** — this is where real diagnostic error happens, and each entry has a specific discriminator:

| Alternative | Discriminating feature |
|---|---|
| **Lumbosacral myelomeningocele** | *"invariably demonstrates a spinal defect"*; cystic or semicystic rather than solid; **no calcification**; associated intracranial findings in most cases. Fetal MRI is the resolver |
| Myelocystocele | spinal dysraphism plus continuity of the sac with the central canal on MRI |
| **Presacral neuroblastoma** | arises from paraspinal sympathetic chain; congenital sacrococcygeal neuroblastoma is reported and *"must be differentiated from an immature or malignant neural lesion arising from a teratoma"* — a genuinely hard distinction, and note this repository already holds `Neuroblastoma.yaml` and `Ganglioneuroblastoma.yaml` |
| **Fetus in fetu** | vertebral axis present; both entities are commoner in families with a twinning history, and coexistence is documented |
| Anterior sacral meningocele (`HP:0007293`) | CSF-filled, continuous with thecal sac; the Currarino alternative mass |
| Chordoma | midline, destructive bone involvement, older patients |
| Hemangioma / lymphangioma / lipoma | vascular or fatty signal characteristics |
| Rhabdomyosarcoma, glioma, neurofibroma, leiomyoma, melanoma | reported in adult presacral series |
| Abscess, duplication/enteric cyst | infective or enteric features |

### 10.6 Screening

- **Population screening for SCT exists de facto**: the routine second-trimester anomaly ultrasound is what detects 25–50% of cases, and the Finnish and Hawaiian registry data depend on it.
- **No newborn screening, no carrier screening, no cascade screening** for SCT.
- **Cascade testing applies to Currarino families** — *MNX1* testing of relatives, with the caveat of ~50% detection and highly variable expressivity. This is the one place genetic counselling (`NCIT:C15240`) is genuinely indicated.

---

## 11. Outcome / Prognosis

### 11.1 Prenatal prognosis — the quantitative core

**The meta-analysis.** van Heurn LJ, Coumans A, Haak MC, et al. *Prognostic accuracy of factors associated with poor outcome in prenatally diagnosed sacrococcygeal teratoma: A systematic review and meta-analysis.* Prenat Diagn. 2023;43(12):1495-1505. **PMID:37964422**; DOI 10.1002/pd.6457. Eleven studies, **447 patients**, **overall mortality including termination 34.9%**. Factors predictive of poor outcome: *"cardiomegaly, hypervascular tumor, solid tumor morphology, fetal hydrops, and placentomegaly"*, and *"a tumor volume to fetal weight ratio (TFR) of >0.12 before a gestational age of 24 weeks is predictive of poor outcome."* The authors' own verdict is appropriately hedged: *"the prognostic accuracy of factors associated with poor outcome in fetuses prenatally diagnosed with SCT seems promising."*

**TFR, the index that organises fetal counselling.** Rodriguez MA, Cass DL, Lazar DA, et al. *Tumor volume to fetal weight ratio as an early prognostic classification for fetal sacrococcygeal teratoma.* J Pediatr Surg. 2011;46(6):1182-5. **PMID:21683219** — *"a TFR greater than 0.12 predicted poor outcome with 100% sensitivity and 83% specificity."* Validated multi-institutionally in 79 cases by Akinkuotu AC, Coleman A, Shue E, et al. J Pediatr Surg. 2015;50(5):771-4. **PMID:25783370**. Independently: *"All 4 patients who developed hydrops had a TFR greater than 0.12"*; and in one series *"5/10 [with TFR>0.12] had poor prognosis, while the fetuses with TFR≤0.12 all had good prognosis (100%, 31/31)."* Reported risk multipliers: hydrops/intervention/perinatal death **4.7× higher** with TFR >0.12, and **6.2× higher before 32 weeks** at TFR ≥0.11.

**Single-cohort anchors.**
- van Heurn LJ, Coumans ABC, Derikx JPM, et al. Prenat Diagn. 2021;41(11):1430-1438. **PMID:34327722** — 84 fetuses; *"Sixteen (19.0%) TOPs"*; *"Overall mortality was 32.1%, with a mortality excluding TOPs of 13.1%"*; *"Thirteen fetal interventions were performed in 11 (13.1%) fetuses"*; **hydrops OR 21.0 (CI 2.6–275.1, p=0.012)**. The very wide confidence interval is honest and should be carried.
- Vinit N, Benachi A, Rosenblatt J, et al. *Growth velocity of fetal sacrococcygeal teratoma as predictor of perinatal morbidity and mortality: multicenter study.* Ultrasound Obstet Gynecol. 2024;64(5):651-660. **PMID:39482803** — 55 fetuses, median GA at diagnosis 22 weeks; *"There was a poor perinatal outcome in 31% (n = 17)"*, including IUFD 4% and TOP 13%; *"The overall survival rate after prenatal diagnosis of isolated SCT was 75% (n = 41 of 55)"*; growth velocity ≥7 mm/week as the cut-off. **This adds a dynamic index to the static TFR and is the most recent prognostic advance.**
- Related indices: Gebb JS et al. Fetal Diagn Ther 2019 (**PMID:29495013**) on high TFR and maternal risk; Shue E et al. J Pediatr Surg 2013 (**PMID:23845611**); Coleman A et al. J Surg Res 2013 (**PMID:23773720**) prenatal solid tumour volume index; Llancarí P et al. J Perinat Med 2025 (**PMID:39753205**) a further proposed index.

### 11.2 Postnatal survival

From the global cohort (PMID:39248311): **5-year survival 95.4%, 10-year survival 94.8%.** The 2026 SCT-study reports survival **94.9%** in SCT versus 96.9% in Currarino presacral teratoma (p=0.343) — statistically indistinguishable.

**Read these next to the prenatal figures rather than instead of them.** A liveborn infant who reaches resection has a ~95% ten-year survival; a fetus diagnosed at 22 weeks has ~75% overall survival and ~35% mortality including terminations. **The prognosis of "sacrococcygeal teratoma" depends entirely on which cohort the denominator is, and an entry that quotes only 95% survival would be misleading.**

Histology-stratified mortality: *"the mortality rate among newborns with immature teratomas was 25.8%, significantly higher than that of mature teratomas, which was 4.16%"* (Varlas et al. Diagnostics 2024;14(3):246. **PMID:38337762**).

Malignant disease survival: COG low-risk 4-year EFS ~89–92%; children 90% versus adolescents 72%; MaGIC poor-risk long-term disease-free survival **<70%**, and extragonadal stage IV as low as **40%** (NCI PDQ; PMID:37449938).

### 11.3 Malignant transformation and recurrence — the age-dependence result

**van Heurn LJ, Derikx JPM, et al. *Malignant transformation and tumour recurrence in sacrococcygeal teratoma: a global, retrospective cohort study.* Int J Surg. 2024;110(11):7177-7186. PMID:39248311; DOI 10.1097/JS9.0000000000002045.** 145 institutes, 62 countries, 1982–2020; 3,612 patients identified, **205 with Currarino syndrome excluded**, 3,407 analysed. This is the definitive dataset for the disease.

**Malignancy at resection, by age:**

| Age at resection | Malignant histology |
|---|---|
| 3 months | 3.3% |
| 6 months | 5.1% |
| **1 year** | **10.3%** |
| **2 years** | **32.9%** |
| ≥6 years | 64.2% (plateau) |

Malignancy-free survival: 94.7% at 1 year, 88.2% at 2 years, 80.2% after 6 years.

**Recurrence:** 349/3,407 (**10.2%**), median **11.4 months** after surgery, malignant in **126/349 (36.1%)**, latest recorded at **22.1 years**. Multivariable odds ratios: **Altman II 1.62** (1.18–2.23), **Altman III 1.63** (1.23–2.35), **immature histology 1.91** (1.43–2.56), **malignant histology 4.00** (2.91–5.41). *(Re-read the Altman III CI from the paper; the retrieved bounds are not symmetric with the point estimate in the usual way and may have been transcribed imprecisely.)*

Recommendations as stated: *"complete resection of SCT before 1 month of age"* when safe and feasible, with *"follow-up to 6 years of age"* since **96% of recurrences occurred within that period**.

**Recurrence after apparently mature SCT.** Kops AL, Hulsker CC, Fiocco M, Zsiros J, Mavinkurve-Groothuis AMC, Looijenga LH, van der Steeg AF, Wijnen MH. *Malignant recurrence after mature Sacrococcygeal teratoma: A meta-analysis and review of the literature.* Crit Rev Oncol Hematol. 2020;156:103140. **PMID:33142194**:
- *"The pooled proportions of mature and malignant recurrences after mature SCT were 3 % (95 % CI 1-4 %) and 5% (95 % CI 3-6 %), respectively."*
- *"Fifty-seven (56 %) of a total of 102 recurrences after resection of an initially mature SCT were malignant, mostly yolk sac tumour (YST)."*
- *"Treatment of mature SCTs with resection alone requires thorough follow-up of at least 6 years."*

**Why a mature tumour recurs malignant — the mechanism.** Johnston WR, Hwang R, Mattei P. *Impact of microscopic deposits of yolk sac tumor on recurrence of mature sacrococcygeal teratoma.* J Surg Oncol. 2024;130(3):569-573. **PMID:39016163**:
- *"We identified 56 patients with mature SCT, of which 9 (16%) demonstrated microscopic YST."*
- *"Following surgery, 7/56 (13%) patients developed local recurrence at a mean of 1.2 ± 0.7 years"*
- *"Recurrence was more likely in patients with microscopic YST [5/9 (56%) vs. 2/47 (4%), p = 0.021]"*
- *"Five patients demonstrated malignant recurrence and were all detected by a rising alpha-fetoprotein (AFP)"*

**This closes the loop: "mature" SCT is a sampling statement about the sections examined, and a sixth of them harbour microscopic yolk sac tumour that predicts a 56% recurrence rate.** It is the best mechanistic explanation available for the malignant-recurrence-after-mature-histology paradox and belongs in the pathograph, not just in the prognosis section.

**SCT versus Currarino presacral teratoma — two independent cohorts agree.**
- Dirix M, van Becelaere T, Berkenbosch L, et al. J Pediatr Surg. 2015;50(3):462-4. **PMID:25746708** — *"The malignancy free survival of patients with SCT was lower than for patients with a presacral teratoma associated with CS (80% and 58% after one and two years in SCT versus 100% after two years in CS, p=0.017)"*; *"In SCT, malignancy and recurrence risk are high"*; *"Our data show that the risk of malignant transformation of a presacral teratoma in CS is small."*
- van Heurn LJ, Derikx JPM, Hall NJ, AbouZeid AA, de Campos Vieira Abib S, et al. *Malignant transformation of sacrococcygeal teratoma versus presacral teratoma in Currarino syndrome: Results of 'The SCT-study'.* J Pediatr Surg. 2026;61(6):162848. **PMID:42250912** — *"10·3 % and 31·9 % after one and two years, versus 4·2 % in CS patients after two years, respectively (p < 0.001)"*; *"Histology in recurrent teratoma was malignant in 35·4 % (n = 114) of SCT patients and 5·9 % (n = 1) of CS patients (p = 0.005)"*; *"Survival in both groups was equivalent at 94·9 % in SCT patients versus 96·9 % in CS patients (p = 0·343)"*. **Read the exact outcome definition behind the 10.3%/31.9% figures from the paper before curating — they are numerically close to the global cohort's malignancy-at-resection figures, and I could not confirm from the abstract excerpt whether they are cumulative malignant transformation or recurrence.**

**This is the strongest argument for keeping the two entries separate**: identical survival, radically different malignant behaviour. An entry that lumped them would assert a malignancy risk for Currarino patients that two cohorts refute.

### 11.4 Complications, morbidity and disability

See §3.2–3.3. In addition: tumour rupture and haemorrhage at delivery; neonatal anaemia and coagulopathy requiring transfusion; prematurity-related morbidity (the dominant cause of neonatal death after successful fetal intervention); wound complications; and the 40% cosmetically unacceptable scar rate.

### 11.5 Prognostic factors — summary

| Prenatal | Postnatal |
|---|---|
| TFR >0.12 before 24 weeks | **Age at resection** (strongest) |
| Growth velocity ≥7 mm/week | Histology: malignant (OR 4.00) > immature (OR 1.91) > mature |
| Solid (vs cystic) morphology | Altman type II/III (OR ~1.6) |
| Hypervascularity | Completeness of resection; coccygectomy performed |
| Cardiomegaly, hydrops, placentomegaly | Microscopic YST deposits (OR not reported; 56% vs 4% recurrence) |
| Polyhydramnios | COG stage; MaGIC risk group |
| Gestational age at delivery | AFP decline after chemotherapy |

**Prognostic biomarker:** AFP, both at diagnosis and as a decline trajectory — PDQ notes a satisfactory response when *"AFP normalized after two cycles of chemotherapy."* miR-371a-3p is promising in testicular GCT but is **not expressed by teratoma**, limiting its SCT application.

---

## 12. Treatment

### 12.1 Fetal therapy

Offered **only** for documented fetal cardiac failure, and futile once hydrops is advanced with placentomegaly or maternal mirror syndrome. The principle, from Paek BW, Jennings RW, Harrison MR, Filly RA, Tacy TA, Farmer DL, Albanese CT. *Radiofrequency ablation of human fetal sacrococcygeal teratoma.* Am J Obstet Gynecol. 2001;184(3):503-507. **PMID:11228510**: *"Targeted ablation of the feeding tumor vessels diminishes blood flow sufficiently to reverse high-output fetal heart failure."* The corollary matters as much: *"ablation of a majority of the tumor tissue in sacrococcygeal teratoma is not necessary and proved fatal in two instances."* **The target is the feeding vessels, not the tumour.**

| Technique | Cases | Survival | NCIT term |
|---|---|---|---|
| Open fetal surgery (debulking) | 16 | **56.2%** | `NCIT:C15329` Surgical Procedure |
| Radiofrequency ablation | 18 | **67%** | **`NCIT:C15666`** Radiofrequency Ablation |
| Laser ablation / coagulation | 23 | **39%** | **`NCIT:C15466`** Laser Therapy (or `NCIT:C111241` Laser Ablation) |
| Alcohol sclerosis | 5 | 20% | `[CURIE NOT VERIFIED]` |
| Coiling | 1 | 0% | — |
| Thermocoagulation | 1 | 0% | — |
| **No intervention** | 93 | **71.0%** | — |

Source: Konno H, Okpaise OO, Sbragia L, Tonni G, Ruano R. *Perinatal Outcomes of Intrauterine Interventions for Fetal Sacrococcygeal Teratoma Based on Different Surgical Techniques — A Systematic Review.* J Clin Med. 2024;13(9):2649. **PMID:38731178**; DOI 10.3390/jcm13092649. Verbatim: *"The survival rate was 56.2% in OS, 45.8% in PI (p = 0.568), and 71.0% in NI patients."*

**The no-intervention arm has the highest survival, and this is selection, not efficacy** — intervention cohorts are the hydropic, high-TFR, large-tumour fetuses. The review's own conclusion is that there was *"no significant difference in perinatal outcomes"* between surgical approaches. Van Mieghem T, Al-Ibrahim A, Deprest J, et al. Ultrasound Obstet Gynecol. 2014;43(6):611-619. **PMID:24488859** gives the cleaner within-stratum figure: *"Six of 20 hydropic fetuses survived after minimally invasive therapy (30%)"*, with *"Mean gestational age at delivery after minimally invasive therapy was 29.7 ± 4.0 weeks."* **Any benefit from intervention is bought at the price of extreme prematurity, which is the dominant cause of death in the intervened group.** See also Hirose S, Farmer DL. *Fetal surgery for sacrococcygeal teratoma.* 2003. **PMID:14533891**; and the CHOP open-fetal-surgery experience (**PMID:19540178**) reporting 6/11 (55%) survival in hydropic fetuses with mean GA at delivery 29.8 ± 2.9 weeks.

### 12.2 Delivery planning

- **Caesarean section** (`[CURIE NOT VERIFIED]` — look up an NCIT caesarean term) for tumours **>5 cm diameter or >750 cm³**, to avoid dystocia, tumour rupture and haemorrhage; some guidance uses a 10 cm threshold. Vaginal delivery is acceptable for small (<5 cm), non-vascular tumours.
- **Classical (vertical) hysterotomy** for very large tumours.
- Target **≥32 weeks**, then elective delivery as soon as feasible.
- EXIT-type and delivery-room-ready arrangements with immediate neonatal stabilisation, vascular access and transfusion capability (`NCIT:C15192` Blood Transfusion; `NCIT:C15409` Packed Red Blood Cell Transfusion; `NCIT:C15366` Platelet Transfusion; `NCIT:C116475` Fresh Frozen Plasma Transfusion).

### 12.3 Definitive surgery — the core treatment

- **Complete resection with coccygectomy**, in the neonatal period, ideally before 1 month of age. `NCIT:C154430` Definitive Surgical Resection; `NCIT:C15329` Surgical Procedure; `NCIT:C164212` Tumor Resection; `NCIT:C175027` Complete Resection.
- **Coccygectomy is non-negotiable**: *"Failure to remove the coccyx results in a high recurrence rate, and one study reported a recurrence rate as high as 37% when the coccyx was not removed."* **This is the highest-leverage single technical statement in SCT surgery.** No NCIT coccygectomy term was located this run `[CURIE NOT VERIFIED]`; bind `NCIT:C15329` with `preferred_term: coccygectomy` if none exists, per the repository's device/action convention.
- **No biopsy, no drainage** (capsular violation upstages; §10.3).
- Laparoscopic or laparoscopically assisted approaches are described for adult type III/IV lesions and for median sacral artery control in neonates.
- Laminectomy where intraspinal extension is present — *"Intraspinal extension in SCT is rare but should be excluded at birth before attempting any resection."*

### 12.4 Chemotherapy for malignant disease

From NCI PDQ (updated 5 November 2024). `NCIT:C15632` Chemotherapy; `NCIT:C15986` Pharmacotherapy; `NCIT:C15681` Cytotoxic Chemotherapy.

**PEb (21-day cycles):** bleomycin 15 units/m² day 1 (max 30 units); etoposide 100 mg/m² days 1–5; cisplatin 20 mg/m² days 1–5.
**JEb (21–28-day cycles):** bleomycin 15 units/m² day 3 (max 30 units); etoposide 120 mg/m² days 1–3; carboplatin 600 mg/m² or GFR-based dosing day 2.

PDQ: *"The use of JEb appears to be associated with fewer otologic toxic effects and renal toxic effects than does the use of PEb."* The UKCCSG comparison behind this: 5-year EFS 57% with BEP in GC I versus 87% with JEB in GC II (`[PMID NEEDED]` — the "'JEB' — a carboplatin based regimen for malignant germ cell tumours in children" paper, PMC1971831; fetch it before citing). Historical regimens (VAC, Adriamycin) were replaced from 1985.

Verified CHEBI agents: **`CHEBI:27899` cisplatin, `CHEBI:31355` carboplatin, `CHEBI:4911` etoposide, `CHEBI:22907` bleomycin.** For a `treatments` block, use `treatment_term: NCIT:C15632` Chemotherapy with these as `therapeutic_agent`, and a `regimen_term` only if an NCIT PEb/JEb regimen term exists — look it up rather than reusing a FOLFIRINOX-style approximation.

**Chemotherapy does not prevent recurrence of resected mature/immature SCT.** Phi (PMID:33906346) states postoperative chemotherapy is ineffective for preventing recurrence. Adjuvant chemotherapy for immature teratoma is reserved for cases meeting INTERIM-guideline criteria including AFP above a stated threshold (the retrieved phrasing mentions *"above 1000 ng/mL"* — **verify this threshold directly in the INTERIM guideline before curating it**; an AFP threshold in the neonatal period is meaningless without the age curve of §10.2).

### 12.5 Experimental and targeted therapy

| Agent | Target | Trial |
|---|---|---|
| Tegavivint | WNT pathway | **NCT04851119** |
| Cabozantinib | c-MET / VEGFR / KIT | **NCT04876456** |
| Codrituzumab | GPC3 antibody | **NCT04928677** |
| CLDN6 CAR-T | claudin-6 | **NCT04503278** |
| Guadecitabine (preclinical/early) | DNMT inhibitor, restoring cisplatin sensitivity | — |

Active COG trials: **AGCT1531** (randomises standard-risk to cisplatin vs carboplatin; *"assesses observation in all stage I extragonadal tumors and reserves chemotherapy for patients with residual or relapsed disease"* — directly relevant to SCT); **AGCT1532** (*"4-cycles of standard BEP (3-week cycles) vs. accelerated BEP (2-week cycles)"* for poor-risk, ages 11–45). **No trial is SCT-specific**; all are extracranial-GCT trials in which SCT is an extragonadal stratum. Fetch these NCT records with `just fetch-reference` and set `phase`/`status` as enum values, then re-check status with `just clinicaltrials-status-audit` — these will go stale.

### 12.6 Supportive care, rehabilitation and surveillance

- `NCIT:C15747` Supportive Care: neonatal stabilisation, transfusion, pain control, nutrition.
- Rehabilitation and continence management for the Branch-D sequelae: `NCIT:C15302` Physical Therapy, `NCIT:C15315` Rehabilitation `[verify]`, bladder management, bowel programmes. Derikx's conclusion is the one to carry: *"Follow-up after surgery for SCT should not only search for tumor recurrence but include the diagnosis and treatment of possible secondary urinary and/or fecal incontinence."*
- **Surveillance (PDQ):** *"Monitor AFP and beta-hCG levels monthly for 6 months (period of highest risk) and then every 3 months, for a total of 2 years (3 years for sacrococcygeal teratoma)."* Imaging at completion of therapy, then every 3–6 months in years 1–2. **Note the conflict to resolve in curation: PDQ says 3 years for SCT; the global cohort and the Kops meta-analysis both say at least 6 years, because 96% of recurrences fall inside 6 years and recurrences are documented to 22 years. Curate both with their sources rather than picking one.**
- **Late effects** (PMID:37449938): ototoxicity, peripheral neuropathy, nephrotoxicity, cardiovascular disease, second malignancies, infertility — extrapolated from adult testicular GCT survivors since *"children and adolescents are treated with the same chemotherapy agents."* The **GOLD study (APEI17N3)** is the COG cohort established to measure them. Sodium thiosulfate for cisplatin ototoxicity is under consideration for randomised study.

### 12.7 Pharmacogenomics

No SCT-specific pharmacogenomic guidance. The relevant general signal is **cisplatin ototoxicity** pharmacogenetics (*TPMT*, *COMT*, *ACYP2* in CPIC/PharmGKB-adjacent literature), **not verified in this run** and not SCT-specific. Do not curate without reading PharmGKB/CPIC directly.

---

## 13. Prevention

**Primary prevention: none possible.** The initiating event is a stochastic developmental/epigenetic accident in week 3 of gestation, with no identified modifiable exposure. There is no vaccine, no risk-factor modification, no behavioural intervention, no prophylactic medication and no public-health or environmental intervention. **This should be stated positively in the entry.**

**Secondary prevention is where everything happens, and it is the strongest prevention story in the disease:**

1. **Prenatal ultrasound detection** at the routine anomaly scan → risk stratification by TFR, morphology, vascularity and growth velocity → planned delivery at a centre with fetal and neonatal surgical capability → prevention of dystocia, tumour rupture and unanticipated haemorrhage.
2. **Resection before one month of age** → prevention of malignant transformation. The numbers in §11.3 make this the single most effective preventive act available: 3.3% malignancy at three months against 32.9% at two years.
3. **Coccygectomy at the index operation** → prevention of recurrence (37% without it).
4. **AFP plus MRI surveillance for at least 6 years** → early detection of the 10% who recur and the third of those whose recurrence is malignant, at a stage where salvage chemotherapy works.

**Tertiary prevention:** structured continence and functional follow-up (§12.6), and surveillance for chemotherapy late effects.

**Genetic counselling (`NCIT:C15240`):** **not indicated for isolated sporadic SCT** — recurrence risk in siblings is not elevated by any established mechanism, and offering counselling would misrepresent the disease. It **is** indicated when the Currarino triad is present or suspected: autosomal dominant transmission, ~50% *MNX1* detection rate, and markedly variable expressivity within families, so a mildly affected parent may be identified only on imaging. Prenatal and preimplantation testing are theoretically available for a known familial *MNX1* variant.

**Risk stratification for prevention** is prenatal (TFR, growth velocity) and postnatal (age, Altman type, histology, microscopic YST) — see §11.5.

---

## 14. Other Species / Natural Disease

### 14.1 Natural disease in animals

**Extragonadal teratomas occur across many species but sacrococcygeal/coccygeal cases are genuinely rare.** The reference review is **Lee S-J, Triana Garcia PA, Choi EA. *Congenital oropharyngeal teratoma in a neonatal goat and brief review of extragonadal teratomas in animals.* J Vet Diagn Invest. 2026 Jan 29:10406387251410495. PMID:41612690; DOI 10.1177/10406387251410495.** Its verdict is unambiguous: *"Extragonadal teratomas are rare in veterinary medicine."*

Species with reported extragonadal teratomas, per that review's Table 1: cats, cattle, sheep, horses, dogs, ducks, ferrets, rabbits, bears, monkeys, skunks, deer, alpacas, birds (herons, kestrels, turkeys, pigeons, parrots) and fish. Common sites are oropharyngeal, head/orbital, intracranial, adrenal, retroperitoneal, mediastinal and umbilical cord.

**Coccygeal cases:** **two coccygeal teratomas in cats** (`NCBITaxon:9685` *Felis catus*), at 6 and 8 months of age. A separate report describes a **feline coccygeal teratoma in a male Burmese cat**, immunohistochemically characterised, composed of derivatives of all three germ layers with **neuroectodermal predominance** — the same histological bias as human immature SCT. The earlier literature stated that congenital teratomas of the coccygeal region *had not been previously reported in domestic animals* before that case, which places the species overlap with human SCT at roughly two documented cats.

**Pathogenesis in animals is described in the same terms as in humans:** *"Teratomas are congenital tumors that arise from pluripotent germ cells. At least 2 embryonic germ layers (ectoderm, mesoderm, endoderm) are present; teratomas therefore arise most often in the gonads."* For oropharyngeal teratomas the cell of origin is unknown, with *"pluripotent cells in the notochord during early embryogenesis"* hypothesised — the animal analogue of the primitive-streak hypothesis of §2.1.

### 14.2 Comparative and evolutionary biology

- **Comparative pathology:** the histology is conserved (tri-germ-layer, neuroectoderm-predominant immaturity); the **site distribution is not**. Humans have a strong sacrococcygeal predilection that domestic species do not share, where oropharyngeal and head sites dominate. **That asymmetry is a real comparative finding and plausibly reflects the human caudal cell mass and the extent of the human primitive streak — but it is a hypothesis, not a demonstrated species difference, and should be curated as such if at all.**
- **Evolutionary conservation of mechanism:** the PGC specification/migration programme and the KITLG–KIT axis are deeply conserved across vertebrates, as is the imprinting-erasure programme, which supports the mechanistic model being transferable in principle. The *Dnd1* mouse data (§15) demonstrate that the same pathway produces teratoma in mouse, at a different site.
- **OMIA:** no OMIA entry for sacrococcygeal teratoma was located. The cases above are sporadic case reports, not inherited traits, so absence from OMIA is expected rather than a gap.

### 14.3 Transmission

**Not applicable.** No zoonotic potential, no cross-species susceptibility, no transmissible component. SCT is a congenital neoplasm.

### 14.4 Orthologues

Human genes relevant here and their rodent orthologues: *KIT*, *KITLG*, *MNX1*, *DND1*, *NANOS2*, *NANOS3*, *POU5F1*. Per this repository's rule, a mouse model's `genes` must be bound to **MGI**, not HGNC — e.g. mouse *Dnd1* and *Mnx1* take `MGI:` identifiers. **No MGI identifiers were looked up in this session; read them from the Alliance gene page and run `just check-gene-namespaces-online` before committing** `[CURIE NOT VERIFIED]`.

---

## 15. Model Organisms

### 15.1 The honest summary first

**There is no animal model of sacrococcygeal teratoma.** No mouse, rat, zebrafish or other system develops a sacrococcygeal germ cell tumour. The two genetic systems closest to the biology — *Dnd1^Ter* and *Mnx1* — each fail in an instructive and different way, and both failures are worth curating as `FAILS_TO_RECAPITULATE` links or `HUMAN_MODEL_MISMATCH` discussions rather than being quietly omitted.

### 15.2 The *Dnd1^Ter* mouse — right tumour, wrong site

The *Ter* mutation is *"a single nucleotide polymorphism that generates a premature stop codon of Dead end1 (Dnd1)"* and increases spontaneous testicular teratoma incidence on the 129 background: **17% in heterozygotes, 94% in homozygotes**, with *"no ovarian teratomas in the 129/Sv genetic background."* The mechanism connects directly to §6: *ter/ter* embryos show **primordial germ cell deficiency at E9.5–E12.5**, and *"loss of Dnd1 increases testicular germ cell tumor incidence in parallel to PGC depletion."* *DND1* acts with **NANOS2 and NANOS3** to regulate teratoma development from PGCs (PMID:32339196, PLoS One 2020; and *Dnd1*-mediated epigenetic control of teratoma formation, PMC5829515).

| Aspect | Assessment |
|---|---|
| Relationship to SCT | `PARTIALLY_RECAPITULATES` at best — models **teratoma formation from PGCs**, which is the trunk of §6, steps 1–5 |
| Fidelity | `LOW` for SCT specifically |
| `model_scale` | `CELLULAR` / `MOLECULAR` — the model observes PGC survival and tumour incidence |
| **Divergences** | **Site:** testicular, never sacrococcygeal — the defining anatomy of SCT is absent (`BOUNDARY_OMISSION`, likely `INVALIDATING` for any site-specific claim). **Strain dependence:** *"Tumor development due to Ter is a strain-specific phenomenon … only on the 129 strain background"* (`POPULATION_MISMATCH`). **Sex:** only male *Dnd1^Ter* mice develop the tumour, inverting the human female predominance (`SPECIES_MISMATCH` / phenotype divergence). **Gene:** *DND1* has no established role in human SCT |

**The strain dependence and the sex inversion are the two divergences a reader most needs, and neither is captured by `fidelity: LOW` alone.** A model whose tumour requires one inbred background and occurs only in males is not a model of a disease with a 4:1 female excess.

### 15.3 The *Mnx1*/*Hlxb9* knockout — right gene, no phenotype

For the Currarino arm: **no *Mnx1* mouse, heterozygous or null, has a sacral or hindgut defect.** The retrieved statement is explicit: *"Neither of the mouse mutants had any detectable disruption of sacral or hindgut development,"* and the proposed reason is a species difference in expression — **MNX1 is not detected in the human tail-bud notochord**, so the human and mouse caudal expression domains differ. This is a textbook `HUMAN_MODEL_MISMATCH`: evidence exists in the model and shows *nothing*, and the translational validity is the open question.

**This repository already records it.** The `Currarino_Triad.yaml` entry (bound to `MONDO:0008305`, from PR #15902) carries the *Hlxb9* knockout as failing to reproduce the disease with a matching human-model-mismatch discussion. **Do not re-derive it in the SCT entry** — relate to the existing entry.

### 15.4 Other systems

- **MC4R mutant mice develop ovarian teratomas** (PMC7876032) — ovarian, so a further wrong-site model; of interest only as evidence that multiple genetic routes to murine teratoma exist.
- **The ESC/iPSC teratoma assay** forms teratomas *by design*, as the standard functional test of pluripotency. It is a model **of teratoma formation from pluripotent cells** — relevant to §6 steps 3–5 and to the claim that an ES-like state suffices — but it is not a model of a disease, and should not be curated as one. Relevant CL terms: `CL:0002322` embryonic stem cell, `CL:0002248` pluripotent stem cell.
- **GCT cell lines** (NTERA-2, NCCIT, TCam-2 and the cisplatin-resistant derivatives behind the methylation findings of §4.5) are adult/adolescent-type lines. Useful for the cisplatin-resistance mechanism, not for SCT biology. Look up Cellosaurus identifiers before curating.
- **No organoid, organ-chip or NAM system for SCT** was identified. Given that the disease is a pluripotent-cell phenomenon, an iPSC-derived PGC-like-cell system would be the obvious NAM to test the reprogramming step — a concrete `KNOWLEDGE_GAP` with a proposed experiment.

### 15.5 Research applications and resources

What the existing models *can* study: PGC specification, migration and survival; the KITLG–KIT dependency; the imprinting-erasure programme; teratoma formation from pluripotent cells; cisplatin resistance and its methylation basis.

What **nothing** currently models: the caudal-midline site specificity, the female predominance, the arteriovenous-shunt/high-output-failure pathway (Branch B, which is what actually kills fetuses), and malignant transformation to yolk sac tumour with age.

**Branch B is the striking gap.** The lethal mechanism of fetal SCT is haemodynamic and in principle highly tractable — a fetal lamb or computational circulation model of a low-resistance AV shunt would address it directly, and the TFR literature is effectively a crude clinical surrogate for exactly that calculation. No such model was identified.

Databases: MGI (for *Dnd1*, *Mnx1*, *Nanos2*, *Nanos3*), IMPC, IMSR, Alliance of Genome Resources, Cellosaurus, DepMap.

Verified taxon CURIEs: `NCBITaxon:9606` *Homo sapiens*, `NCBITaxon:10090` *Mus musculus*, `NCBITaxon:9685` *Felis catus*, `NCBITaxon:7955` *Danio rerio*, `NCBITaxon:10116` *Rattus norvegicus*.

---

## 16. Curation notes for this repository

Practical findings from this run, offered so the curation step does not have to rediscover them:

1. **Granularity.** SCT is a histologic/site-defined congenital neoplasm, correctly a `Disease` entry at the default rung of design decisions §3a. MONDO classes `MONDO:0042727` in the `ordo_subtype_of_a_disorder` subset, so check whether a broader germ-cell-tumour grouping should hold it. Related entries already present: `Yolk_Sac_Tumor.yaml` (`MONDO:0005744`), `Mixed_Germ_Cell_Tumor.yaml` (`MONDO:0015864`), `Testicular_Germ_Cell_Tumor.yaml`, `Central_Nervous_System_Germ_Cell_Tumor.yaml`, `Central_Nervous_System_Teratoma.yaml`, `Malignant_Germ_Cell_Tumor_of_Ovary.yaml`, and **`Currarino_Triad.yaml`** (`MONDO:0008305`). **A `Grouping` over the type-I/extragonadal paediatric GCTs may be the right structural move; check `kb/groupings/` before creating one.**
2. **Do not merge SCT and the Currarino presacral teratoma.** Two independent cohorts (PMID:25746708, PMID:42250912) show equivalent survival but radically different malignant transformation. Relate the entries.
3. **No `references_cache/` file exists for any PMID in this report.** Every citation needs `just fetch-reference PMID:<id>` and every snippet needs re-verification; `just count-verified-snippets` is the fast loop and `just validate-disorders` is the gate.
4. **`HP:0030736` is not yet in `cache/hp/terms.csv`** (verified via OLS this session); `just validate-terms` will resolve and cache it. `HP:0009793` Presacral teratoma **is** cached.
5. **Obsolete GO terms to avoid:** `GO:0080111` DNA demethylation and `GO:0006306` DNA methylation are both marked obsolete in the local cache. Use `GO:0071514` genomic imprinting / `GO:0141166` / `GO:0070988`.
6. **Cell of origin will report as unmarked** under `just check-cancer-origin`, and that is correct — there is no host somatic lesion and no initiating exposure to mark. Record the reason in `notes:` instead of forcing the derivation.
7. **Phenotype wiring.** This entry has a genuinely rich causal chain (§6) reaching phenotypes through four branches, so most phenotypes can be connected rather than left stranded. Run `just list-disconnected-phenotypes kb/disorders/Sacrococcygeal_Teratoma.yaml` after drafting.
8. **Candidate `conforms_to` targets:** `tumor_angiogenesis` (Branch B step 7) and possibly `invasion_and_metastasis` for the malignant arm. `germline_two_hit_tumor_predisposition` does **not** apply. Read each module's own `description` before conforming, and run `just list-modules` for the current set.
9. **Three evidence-grading traps in this material:** (a) isochromosome 12p is adolescent/adult GCT, not neonatal SCT — grading an i(12p) quote as `DIRECT` support for SCT biology would be wrong; (b) the GCT susceptibility SNPs come from mixed-site cohorts with age stratification that must be preserved; (c) several numbers quoted in reviews (the 37% no-coccygectomy recurrence, the 5-year JEB/BEP EFS figures, the INTERIM AFP threshold) are secondary citations — trace them to the primary paper before grading as `PRIMARY_RESULT`.
10. **Content fence disclosure for the PR body:** arm-level chromosomal loss detail adjacent to content fence (b) has been left out of §4.2 and should remain out of the entry.

---

## Sources

**Primary literature (PubMed)**

- Altman RP, Randolph JG, Lilly JR. Sacrococcygeal teratoma: American Academy of Pediatrics Surgical Section Survey-1973. J Pediatr Surg. 1974;9(3):389-98. [PMID:4843993](https://pubmed.ncbi.nlm.nih.gov/4843993/)
- Blohm ME et al. Alpha 1-fetoprotein (AFP) reference values in infants up to 2 years of age. Pediatr Hematol Oncol. 1998;15(2):135-42. [PMID:9592840](https://pubmed.ncbi.nlm.nih.gov/9592840/)
- Paek BW et al. Radiofrequency ablation of human fetal sacrococcygeal teratoma. Am J Obstet Gynecol. 2001;184(3):503-7. [PMID:11228510](https://pubmed.ncbi.nlm.nih.gov/11228510/)
- Hirose S, Farmer DL. Fetal surgery for sacrococcygeal teratoma. 2003. [PMID:14533891](https://pubmed.ncbi.nlm.nih.gov/14533891/)
- Neubert S et al. Sonographic prognostic factors in prenatal diagnosis of SCT. Fetal Diagn Ther. 2004;19(4):319-26. [PMID:15192290](https://pubmed.ncbi.nlm.nih.gov/15192290/)
- Forrester MB, Merz RD. Descriptive epidemiology of teratoma in infants, Hawaii, 1986-2001. Paediatr Perinat Epidemiol. 2006;20(1):54-8. [PMID:16420341](https://pubmed.ncbi.nlm.nih.gov/16420341/)
- Derikx JP et al. Long-term functional sequelae of sacrococcygeal teratoma: a national study in The Netherlands. J Pediatr Surg. 2007;42(6):1122-6. [PMID:17560233](https://pubmed.ncbi.nlm.nih.gov/17560233/)
- Oosterhuis JW, Stoop H, Honecker F, Looijenga LHJ. Why human extragonadal germ cell tumours occur in the midline of the body. Int J Androl. 2007. [doi:10.1111/j.1365-2605.2007.00793.x](https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2605.2007.00793.x)
- Open fetal surgery for life-threatening fetal anomalies. 2009. [PMID:19540178](https://pubmed.ncbi.nlm.nih.gov/19540178/)
- Rodriguez MA et al. Tumor volume to fetal weight ratio as an early prognostic classification for fetal sacrococcygeal teratoma. J Pediatr Surg. 2011;46(6):1182-5. [PMID:21683219](https://pubmed.ncbi.nlm.nih.gov/21683219/)
- Poynter JN et al. Associations between variants in KITLG, SPRY4, BAK1, and DMRT1 and pediatric germ cell tumors. Genes Chromosomes Cancer. 2012;51:266-71. [PMID:22072546](https://pubmed.ncbi.nlm.nih.gov/22072546/)
- Pauniaho SL et al. High prevalence of sacrococcygeal teratoma in Finland — a nationwide population-based study. Acta Paediatr. 2013;102(6):e251-6. [PMID:23432104](https://pubmed.ncbi.nlm.nih.gov/23432104/)
- Szyllo K, Lesnik N. Sacrococcygeal teratoma — case report and review of the literature. Am J Case Rep. 2013;14:1-5. [PMC3614378](https://pmc.ncbi.nlm.nih.gov/articles/PMC3614378/)
- Shue E et al. Tumor metrics and morphology predict poor prognosis in prenatally diagnosed sacrococcygeal teratoma. J Pediatr Surg. 2013. [PMID:23845611](https://pubmed.ncbi.nlm.nih.gov/23845611/)
- Coleman A et al. Prenatal solid tumor volume index. J Surg Res. 2013. [PMID:23773720](https://pubmed.ncbi.nlm.nih.gov/23773720/)
- Van Mieghem T et al. Minimally invasive therapy for fetal sacrococcygeal teratoma. Ultrasound Obstet Gynecol. 2014;43(6):611-9. [PMID:24488859](https://pubmed.ncbi.nlm.nih.gov/24488859/)
- Dirix M et al. Malignant transformation in sacrococcygeal teratoma and in presacral teratoma associated with Currarino syndrome: a comparative study. J Pediatr Surg. 2015;50(3):462-4. [PMID:25746708](https://pubmed.ncbi.nlm.nih.gov/25746708/)
- Akinkuotu AC et al. Predictors of poor prognosis in prenatally diagnosed sacrococcygeal teratoma. J Pediatr Surg. 2015;50(5):771-4. [PMID:25783370](https://pubmed.ncbi.nlm.nih.gov/25783370/)
- Marcotte EL et al. Variants in BAK1, SPRY4, and GAB2 are associated with pediatric germ cell tumors. Genes Chromosomes Cancer. 2017. [PMC5612339](https://pmc.ncbi.nlm.nih.gov/articles/PMC5612339/)
- Gebb JS et al. High tumor volume to fetal weight ratio is associated with worse fetal outcomes. Fetal Diagn Ther. 2019. [PMID:29495013](https://pubmed.ncbi.nlm.nih.gov/29495013/)
- Kops AL et al. Malignant recurrence after mature sacrococcygeal teratoma: a meta-analysis. Crit Rev Oncol Hematol. 2020;156:103140. [PMID:33142194](https://pubmed.ncbi.nlm.nih.gov/33142194/)
- van Heurn LJ et al. Diagnostic accuracy of serum alpha-fetoprotein levels in diagnosing recurrent sacrococcygeal teratoma. J Pediatr Surg. 2020;55(9):1732-9. [PMID:32376010](https://pubmed.ncbi.nlm.nih.gov/32376010/)
- Kubota Y et al. Comprehensive genetic analysis of pediatric germ cell tumors identifies potential drug targets. Commun Biol. 2020;3(1):544. [PMID:32999426](https://pubmed.ncbi.nlm.nih.gov/32999426/) · [PMC7528104](https://pmc.ncbi.nlm.nih.gov/articles/PMC7528104/)
- Mouse dead end1 acts with Nanos2 and Nanos3 to regulate testicular teratoma incidence. PLoS One. 2020. [PMID:32339196](https://pubmed.ncbi.nlm.nih.gov/32339196/) · Dnd1-mediated epigenetic control of teratoma formation [PMC5829515](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5829515/)
- Phi JH. Sacrococcygeal teratoma: a tumor at the center of embryogenesis. J Korean Neurosurg Soc. 2021;64(3):406-13. [PMID:33906346](https://pubmed.ncbi.nlm.nih.gov/33906346/) · [full text](https://www.jkns.or.kr/journal/view.php?doi=10.3340%2Fjkns.2021.0015)
- van Heurn LJ et al. Factors associated with poor outcome in fetuses prenatally diagnosed with sacrococcygeal teratoma. Prenat Diagn. 2021;41(11):1430-8. [PMID:34327722](https://pubmed.ncbi.nlm.nih.gov/34327722/)
- Bhuta R et al. Children's Oncology Group's 2023 Blueprint for Research: Germ Cell Tumors. Pediatr Blood Cancer. 2023. [PMID:37449938](https://pubmed.ncbi.nlm.nih.gov/37449938/) · [PMC10529374](https://pmc.ncbi.nlm.nih.gov/articles/PMC10529374/)
- van Heurn LJ et al. Prognostic accuracy of factors associated with poor outcome in prenatally diagnosed sacrococcygeal teratoma. Prenat Diagn. 2023;43(12):1495-505. [PMID:37964422](https://pubmed.ncbi.nlm.nih.gov/37964422/)
- Varlas VN et al. Immature sacrococcygeal teratoma: a case report and extensive review of the literature. Diagnostics. 2024;14(3):246. [PMID:38337762](https://pubmed.ncbi.nlm.nih.gov/38337762/) · [PMC10854813](https://pmc.ncbi.nlm.nih.gov/articles/PMC10854813/)
- Konno H et al. Perinatal outcomes of intrauterine interventions for fetal sacrococcygeal teratoma based on different surgical techniques. J Clin Med. 2024;13(9):2649. [PMID:38731178](https://pubmed.ncbi.nlm.nih.gov/38731178/) · [PMC11084939](https://pmc.ncbi.nlm.nih.gov/articles/PMC11084939/)
- Johnston WR, Hwang R, Mattei P. Impact of microscopic deposits of yolk sac tumor on recurrence of mature sacrococcygeal teratoma. J Surg Oncol. 2024;130(3):569-73. [PMID:39016163](https://pubmed.ncbi.nlm.nih.gov/39016163/)
- van Heurn LJ et al. Malignant transformation and tumour recurrence in sacrococcygeal teratoma: a global, retrospective cohort study. Int J Surg. 2024;110(11):7177-86. [PMID:39248311](https://pubmed.ncbi.nlm.nih.gov/39248311/) · [PMC11573091](https://pmc.ncbi.nlm.nih.gov/articles/PMC11573091/)
- Vinit N et al. Growth velocity of fetal sacrococcygeal teratoma as predictor of perinatal morbidity and mortality. Ultrasound Obstet Gynecol. 2024;64(5):651-60. [PMID:39482803](https://pubmed.ncbi.nlm.nih.gov/39482803/)
- Llancarí P et al. Proposal of a novel index in assessing perinatal mortality in prenatal diagnosis of sacrococcygeal teratoma. J Perinat Med. 2025. [PMID:39753205](https://pubmed.ncbi.nlm.nih.gov/39753205/)
- van Heurn LJ et al. Malignant transformation of sacrococcygeal teratoma versus presacral teratoma in Currarino syndrome: results of 'The SCT-study'. J Pediatr Surg. 2026;61(6):162848. [PMID:42250912](https://pubmed.ncbi.nlm.nih.gov/42250912/)
- Lee S-J, Triana Garcia PA, Choi EA. Congenital oropharyngeal teratoma in a neonatal goat and brief review of extragonadal teratomas in animals. J Vet Diagn Invest. 2026. [PMID:41612690](https://pmc.ncbi.nlm.nih.gov/articles/PMC12858381/)

**Guidelines, databases and other resources**

- [NCI PDQ — Childhood Extracranial Germ Cell Tumors Treatment (updated 5 Nov 2024)](https://www.cancer.gov/types/extracranial-germ-cell/hp/germ-cell-treatment-pdq)
- [OMIM #176450 — Currarino syndrome](https://omim.org/entry/176450) · [OMIM \*142994 — MNX1](https://omim.org/entry/142994)
- [EBI OLS4 — MONDO:0042727](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0042727) · [HP:0030736](https://www.ebi.ac.uk/ols4/api/ontologies/hp/terms?obo_id=HP:0030736) · [NCIT:C99055](https://www.ebi.ac.uk/ols4/api/ontologies/ncit/terms?obo_id=NCIT:C99055)
- [Orphanet — sacrococcygeal teratoma (ORPHA:494421)](https://www.orpha.net/en/disease/detail/494421) *(behind bot check; fetch into the reference cache)*
- [CAP protocol — extragonadal germ cell tumour biopsy specimens](https://documents.cap.org/protocols/ExGonad.GCT.Bx_5.0.0.0.REL_CAPCP_R.pdf)
- [Methylation profiles of imprinted genes in mature ovarian teratoma, complete hydatidiform mole and extragonadal mature teratoma](https://www.nature.com/articles/s41379-020-00668-8)
- [Genome-wide DNA methylation profiles provide clues to the origin and pathogenesis of germ cell tumors (PLoS One)](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0122146)
- ['JEB' — a carboplatin-based regimen for malignant germ cell tumours in children](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1971831/)
- [Feline coccygeal teratoma: immunohistochemical characterization](https://www.sciencedirect.com/science/article/abs/pii/S0021997514000863)
- [UCSF Fetal Treatment Center — sacrococcygeal teratoma](https://fetus.ucsf.edu/sct/) · [Johns Hopkins — sacrococcygeal teratoma](https://www.hopkinsmedicine.org/health/conditions-and-diseases/sacrococcygeal-teratoma) · [NORD — sacrococcygeal teratoma](https://rarediseases.org/rare-diseases/sacrococcygeal-teratoma/)
- [dismech PR #15902 — Curate Currarino triad (MNX1, MONDO:0008305)](https://github.com/monarch-initiative/dismech/pull/15902)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 53 |
| Resolved | 52 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 52 |
| On topic | 30 |
| Off topic | 1 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:38337762` (4 mentions) - Identifier did not resolve to a record

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:9592840` (4 mentions) - Alpha 1-fetoprotein (AFP) reference values in infants up to 2 years of age.
  - shared terms: age, year

Weighed against this report's own most characteristic terms: `sct`, `teratoma`, `sacrococcygeal`, `tumour`, `cell`, `malignant`, `germ`, `disease`, `age`, `fetal`, `neonatal`, `currarino`, `recurrence`, `tumor`, `mature`, `patient`, `year`, `presacral`, `mnx1`, `resection`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 95 |
| Resolved | 92 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 1 |
| Terms whose name was checked | 11 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0042727` (7 mentions) - the report calls it "MONDO"; MONDO calls it **sacrococcygeal teratoma**
- `HP:0030736` (9 mentions) - the report calls it "HPO"; HP calls it **Sacrococcygeal teratoma**
- `NCIT:C99055` (5 mentions) - the report calls it "NCIT"; NCIT calls it **Sacrococcygeal Teratoma**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0080111` (obsolete DNA demethylation) (3 mentions)
- `GO:0006306` (obsolete DNA methylation) (2 mentions)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.