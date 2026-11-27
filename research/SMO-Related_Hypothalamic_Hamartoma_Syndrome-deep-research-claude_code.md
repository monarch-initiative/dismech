---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-25T15:24:49.753835'
end_time: '2026-11-25T15:28:11.405444'
duration_seconds: 201.65
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: SMO-Related Hypothalamic Hamartoma Syndrome
  mondo_id: MONDO:0009436
  category: Mendelian
  causal_genes: SMO
  omim_id: OMIM:241800
  synonyms: hypothalamic hamartomas; Pallister-Hall-like syndrome; hamartoma of hypothalamus;
    hypothalamic hamartoma
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
  web_search_requests: 14
  num_turns: 19
  total_cost_usd: 0.8377065899999999
  session_id: 4c8a5d8d-3ea5-4360-9f77-bd58acaa8d1d
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  tool_calls: 25
  retrieval_calls: 22
  assistant_text_blocks: 3
citation_count: 11
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 9
  validator_version: 0.8.0
term_validation:
  total_terms: 56
  verified: 43
  not_found: 0
  obsolete: 1
  unverifiable: 12
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 7
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0025258
    reported_labels:
    - Dacrystic seizure; ID to verify
    ontology_label: Stiff neck
  - term_id: UBERON:0001898
    reported_labels:
    - hypothalamus, especially the tuber cinereum and mammillary region
    ontology_label: hypothalamus
  - term_id: UBERON:0004148
    reported_labels:
    - atrioventricular septum
    ontology_label: cardiac vein
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0097711
    ontology_label: obsolete ciliary basal body-plasma membrane docking
    replaced_by: GO:1905349
  service_unreachable: 11
  obsolescence_unchecked: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SMO-Related Hypothalamic Hamartoma Syndrome
- **MONDO ID:** MONDO:0009436 (if available)
- **Causal gene(s):** SMO
- **OMIM:** OMIM:241800
- **Synonyms:** hypothalamic hamartomas; Pallister-Hall-like syndrome; hamartoma of hypothalamus; hypothalamic hamartoma
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **SMO-Related Hypothalamic Hamartoma Syndrome** covering all of the
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

Let me try a single simple command.

I'm collecting the last sources (PMIDs, mouse models, treatment) and will then write the report.

**Scope note:** This report covers **Pallister-Hall-like syndrome (PHLS; OMIM #241800)**, the autosomal recessive syndrome caused by bi-allelic germline variants in **SMO** (Smoothened, frizzled class receptor; OMIM *601500; 7q32.1). It is grouped here under "SMO-related hypothalamic hamartoma syndrome". It is a different disorder from GLI3-related Pallister-Hall syndrome (PHS; #146510, autosomal dominant). It is also different from Curry-Jones syndrome (#601707), which is a somatic mosaic SMO disorder. Somatic and two-hit SMO findings in sporadic hypothalamic hamartoma (HH) are included because they share the same mechanism.

**Access limits:** PubMed and PMC pages blocked automated access in this session. Abstract-level text came from web search snippets, institutional repositories, and an OMIM mirror. Quotes come from those retrieved snippets, and some may be paraphrased by the search tool rather than verbatim. Exact quotes should be re-checked against PubMed before curation. Where a PMID could not be retrieved, the report gives the DOI or PMCID instead.

---

## 1. Disease Information

**Overview.** OMIM describes PHLS this way: *"Pallister-Hall-like syndrome (PHLS) is a pleiotropic autosomal recessive disorder characterized by phenotypic variability"*. It *"is caused by homozygous or compound heterozygous mutation in the SMO gene (601500) on chromosome 7q32"* ([OMIM 241800 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/241800)). The core features are:
- hypothalamic hamartoma with gelastic or dacrystic epilepsy;
- postaxial polydactyly and syndactyly;
- microcephaly;
- atrioventricular septal defect;
- Hirschsprung disease;
- craniofacial and skeletal anomalies.

**Identifiers**

| Resource | ID | Status |
|---|---|---|
| OMIM | #241800 (gene *601500) | retrieved |
| MONDO | MONDO:0009436 | as supplied; not independently verified |
| Orphanet | not retrieved | — |
| ICD-10 | Q87.8 or D33.0/Q04.8 for HH | assignment not retrieved; needs checking |
| MeSH | Hamartoma; Hypothalamic Diseases | descriptors only; no disease-specific term found |

**Synonyms.** Pallister-Hall-like syndrome (PHLS); hypothalamic hamartomas (historical OMIM title); hamartoma of hypothalamus.

The historical entry draws on early families: Marcuse 1953, PMID 13085273, and Encha-Razavi 1992, PMID 1308364 (OMIM).

**Data provenance.** All data are aggregated case reports, about 11 molecularly confirmed individuals across about 7 families. There are no EHR or registry cohorts.

## 2. Etiology

**Causal factors**
- **Germline cause:** bi-allelic loss-of-function variants in SMO.
- **Rubino et al. 2018** (J Neurosurg Pediatr 23:98–103; PMID 30497210): two brothers with *"compound heterozygosity for a 2-bp deletion in the SMO gene (601500.0004) and a deletion at chromosome 7q32.1 involving part of the SMO gene"* (OMIM). The authors called it *"the first report… describing a familial syndrome caused by germline mutations in the Smoothened (SMO) gene"* ([curehunter abstract](https://curehunter.com/public/pubmed30497210.do)).
- **Le et al. 2020** (Am J Hum Genet 106:779–792; PMID 32413283): *"bi-allelic loss-of-function SMO variants in seven individuals from five families"* ([PubMed](https://pubmed.ncbi.nlm.nih.gov/32413283/)). OMIM lists these as alleles 601500.0005–.0009.
- **Green et al. 2022** (Eur J Hum Genet 30:384–388; DOI 10.1038/s41431-021-01023-4; PMC8904774): two siblings of non-consanguineous parents, compound heterozygous for:
  - NM_005631.5 c.1199G>A p.(Arg400His), paternal;
  - c.1416C>T p.(Tyr472=), maternal, a synonymous variant that causes partial skipping of exon 8, a frameshift, and predicted nonsense-mediated decay.

  The authors concluded that bi-allelic SMO variants are an uncommon recessive cause of a PHS-like phenotype ([PMC8904774](https://pmc.ncbi.nlm.nih.gov/articles/PMC8904774)).
- **Two-hit (germline plus somatic) cause in sporadic HH:** Green et al. 2022 (Hum Mol Genet 31:2307–2316; PMID 35137044) studied 27 resected HH tissues. In 7 patients they found *"bi-allelic (one germline, one somatic) variants within one of four cilia genes—DYNC2I1, DYNC2H1, IFT140 or SMO"*. Overall, *"a plausible molecular cause was established for 15/27 (56%) patients"* ([PMC9307310](https://pmc.ncbi.nlm.nih.gov/articles/PMC9307310)).
- **Large somatic lesions:** Hildebrand et al. 2016 (Am J Hum Genet 99:423–429; PMID 27453577) found Shh-pathway somatic mutations in *"14/38 individuals (37%)"*. Large somatic copy-number lesions in that study included *"the receptor SMO"* ([PMC4974069](https://pmc.ncbi.nlm.nih.gov/articles/PMC4974069)).

**Risk factors**
- Genetic: parents who are both carriers, giving a 25% recurrence risk. Consanguinity was not documented in the families retrieved; the Green 2022 parents were non-consanguineous.
- Environmental: none known.

**Protective factors and gene-environment interactions:** none reported.

## 3. Phenotypes

Frequencies use the OMIM-aggregated series (Le 2020, n=7, plus Rubino 2018 and Green 2022). Denominators are approximate.

| Phenotype | HPO | Frequency / notes |
|---|---|---|
| Hypothalamic hamartoma | HP:0002444 | ≥3/7 (Le); 2/2 (Rubino); 2/2 (Green). Congenital and non-progressive. |
| Gelastic seizures | HP:0010821 | in HH-bearing patients; childhood onset |
| Dacrystic seizures | HP:0025258 (Dacrystic seizure; ID to verify) | OMIM |
| Postaxial polydactyly (hands and feet) | HP:0100259 / HP:0001830 | most patients |
| Syndactyly | HP:0001159 | some |
| Microcephaly | HP:0000252 | several |
| Atrioventricular septal defect | HP:0006695 | 3/7 (Le); also monoatrium and coarctation of the aorta (HP:0001680) |
| Hirschsprung disease / rectosigmoid aganglionosis | HP:0002251 | 1 (Le) and Rubino family |
| Micropenis, cryptorchidism, hypospadias | HP:0000054, HP:0000028, HP:0000047 | single cases |
| Cleft palate, choanal stenosis, microstomia, microglossia, ankyloglossia, short nose, large fontanel | HP:0000175, HP:0000453, HP:0000160, HP:0000171, HP:0010296, HP:0003196, HP:0000239 | 5/7 had craniofacial dysmorphism |
| Narrow chest, trident acetabulum, short long bones | HP:0000774, HP:0002984 | 2/7 |
| Short stature, oligodontia, nail hypoplasia, epulis, spatulate mandible | HP:0004322, HP:0000677, HP:0001792 | OMIM synopsis (summary-level) |
| Pituitary cyst; Chiari type I malformation | HP:0011755; HP:0007099 | 1 patient |
| Speech delay | HP:0000750 | OMIM synopsis |

All quotes and counts above are from OMIM.

**Endocrine features.** Central precocious puberty (HP:0000826) is typical of HH in general, but it was not documented in the SMO-PHLS text retrieved.

**Severity and progression.** Severity varies; OMIM records variable expressivity between siblings. The malformations are congenital and static. The epilepsy can be progressive and refractory, as is generally true of HH.

**Quality of life.** No PHLS-specific QoL data were found. In HH generally, refractory gelastic epilepsy drives cognitive and behavioural morbidity.

## 4. Genetic / Molecular Information

**Gene.** SMO (HGNC:11119; OMIM *601500; 7q32.1). It encodes a class F 7-transmembrane GPCR-like transducer of Hedgehog signalling.

**Variant types**
- frameshift (2-bp deletion);
- partial-gene deletion;
- missense, e.g. p.Arg400His;
- exon-skipping synonymous variant (c.1416C>T);
- other LoF alleles described by Le 2020 (exact nomenclature not retrieved).

**Classification and frequency.** ClinVar classifications and gnomAD frequencies were not retrieved.

**Mechanism.** Loss of function in a recessive model. Contrast this with:
- activating somatic SMO variants, e.g. p.Leu412Phe in Curry-Jones syndrome and in basal cell carcinoma or medulloblastoma (not retrieved here);
- GLI3 truncation in PHS, which produces a constitutive repressor. Saitsu 2016 reported *"The truncated GLI3 showed stronger repressor activity than the wild-type protein"* ([PMC4863748](https://pmc.ncbi.nlm.nih.gov/articles/PMC4863748)).

**Germline versus somatic**
- Germline bi-allelic: the syndromic form.
- Germline plus somatic second hit: sporadic HH (PMID 35137044).
- Large somatic CNVs in hamartoma tissue: PMID 27453577.

**Modifier genes and epigenetics:** none reported.

**Chromosomal abnormalities.** 7q32.1 deletions that include SMO, in trans with a point variant (Rubino 2018).

## 5. Environmental Information

No environmental, lifestyle, or infectious contributors are known. Not applicable.

## 6. Mechanism / Pathophysiology

**Causal chain**
1. Bi-allelic SMO loss-of-function variants (germline, or germline plus a somatic second hit) **lead to** absent or dysfunctional Smoothened protein (PMID 32413283; PMID 35137044).
2. Loss of SMO **results in** failure to transduce Hedgehog (SHH/IHH) signals at the primary cilium after PTCH1 relief. Patient cells *"showed normal ciliogenesis but severely altered Hh-signal transduction"* (PMID 32413283).
3. Without SMO activity, GLI processing is abnormal. Le 2020 observed *"Hh-independent GLI2 accumulation at the PC tip"*, which suggests that SMO regulates basal ciliary GLI2 trafficking (PMID 32413283). This **leads to** reduced GLI activator output and/or an excess of GLI repressor. The repressor-dominance step is inferred by analogy with GLI3-truncation PHS (PMC4863748).
4. Reduced Hh pathway output during embryogenesis **branches** into:
   - 4a. abnormal patterning and proliferation of the ventral diencephalon and hypothalamic primordium, **resulting in** hypothalamic hamartoma. The exact cellular mechanism is inferred; it is shared with GLI3, OFD1, and cilia-gene HH (PMID 35137044).
   - 4b. altered limb anteroposterior patterning, **resulting in** postaxial polydactyly. This is paradoxical for Hh loss, and the mechanism is unresolved.
   - 4c. defective cardiac morphogenesis and atrioventricular cushion/septation, **resulting in** AVSD. This is supported by Smo-null mice (Zhang et al., Cell 2001;105:781).
   - 4d. impaired enteric neural crest development, **resulting in** aganglionosis (Hirschsprung disease).
   - 4e. skeletal and craniofacial Hh defects (IHH and SHH), **resulting in** short long bones, narrow chest, and cleft palate.
5. Hamartoma neurons (mainly small GABAergic interneuron-like cells, described in the general HH literature but not retrieved here) form an intrinsically epileptogenic network. This **leads to** gelastic and dacrystic seizures, which can then generalise secondarily and contribute to cognitive and behavioural comorbidity.

**Ontology suggestions**
- GO biological process:
  - smoothened signaling pathway, GO:0007224
  - cilium assembly / non-motile cilium-dependent signalling, GO:0097711
  - hypothalamus development, GO:0021854
  - limb development, GO:0060173
  - atrioventricular septum morphogenesis, GO:0003281
  - enteric nervous system development, GO:0048484
- GO cellular component:
  - ciliary membrane, GO:0060170
  - primary cilium / non-motile cilium, GO:0097730
  - ciliary tip, GO:0097542
- CL: neuron, CL:0000540; GABAergic neuron, CL:0011005; enteric neuron, CL:0007011; neural crest cell, CL:0000333; fibroblast, CL:0000057 (patient cells).

**Molecular profiling.** No omics, single-cell, or spatial data specific to SMO-PHLS were found. HH-wide single-cell studies exist, but they were not retrieved here.

## 7. Anatomical Structures

| Level | Structures | UBERON |
|---|---|---|
| Primary | hypothalamus, especially the tuber cinereum and mammillary region | UBERON:0001898 |
| Limbs | hand and foot digits | UBERON:0002389, UBERON:0001466 |
| Heart | atrioventricular septum | UBERON:0004148 |
| Gut | colon/rectum, enteric nervous system | UBERON:0001155, UBERON:0002005 |
| Other | palate | UBERON:0001716 |
| Other | pituitary | UBERON:0000007 |
| Other | long bones | UBERON:0002495 |
| Other | external genitalia | UBERON:0004176 |

The hamartoma is midline. Polydactyly is usually bilateral.

## 8. Temporal Development

The disorder is congenital. Malformations are present at birth, and HH can be seen on prenatal or neonatal imaging. Gelastic seizures typically begin in infancy or early childhood (general HH knowledge; not PHLS-specific data). The hamartoma is non-neoplastic and does not grow. The epilepsy may evolve into refractory epileptic encephalopathy. Early surgical disconnection is a critical window for preventing cognitive decline in HH-associated epilepsy, though this point comes from the general HH literature. No spontaneous remission has been reported.

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive (OMIM). Carriers are unaffected; the Green 2022 parents were unaffected heterozygotes.
- **Penetrance and expressivity:** penetrance appears complete for bi-allelic LoF, with variable expressivity.
- **Anticipation, founder effects, carrier frequency:** none reported or not retrieved.
- **Prevalence:** fewer than about 15 molecularly confirmed cases. Hypothalamic hamartoma overall is estimated at about 1 in 50,000–200,000 children (common estimate; not retrieved this session).
- **Sex:** both sexes are affected. Reported families include affected brothers and siblings of both sexes.

## 10. Diagnostics

- **Imaging:** MRI shows a non-enhancing mass that is iso- or hypointense on T1 and iso- or hyperintense on T2 in the tuber cinereum. Additional work-up includes:
  - echocardiography for AVSD;
  - skeletal survey;
  - rectal biopsy (absent ganglion cells, acetylcholinesterase staining) if Hirschsprung disease is suspected.
- **EEG:** often non-localising. Depth recording from the HH shows seizure onset within the lesion.
- **Genetic testing:**
  - Exome or genome sequencing with CNV analysis is recommended. One allele in the Rubino family was a 7q32.1 partial deletion, and the Green family needed re-analysis to detect a synonymous splice variant. RNA or cDNA studies can confirm splice effects (PMC8904774).
  - Panels for HH, PHS, or ciliopathy should include SMO, GLI3, OFD1, DYNC2H1, DYNC2I1, IFT140, and PRKACA.
  - In sporadic HH, paired testing of resected tissue and blood at high depth detects somatic second hits (PMID 35137044).
- **Differential diagnosis:**
  - GLI3-PHS (AD; mesoaxial/insertional polydactyly, bifid epiglottis, imperforate anus);
  - OFD syndromes (OFD1);
  - Bardet-Biedl syndrome and short-rib thoracic dysplasias (DYNC2H1, IFT140);
  - Curry-Jones syndrome (somatic activating SMO);
  - Smith-Lemli-Opitz syndrome;
  - isolated sporadic HH.
- **Clinical criteria and screening:** no formal criteria exist. Cascade carrier testing is possible once familial variants are known.

## 11. Prognosis

No survival data are available. Morbidity is driven by:
- refractory epilepsy and cognitive or behavioural impairment;
- congenital heart disease, including surgical AVSD repair;
- Hirschsprung disease.

Prognosis depends on the severity of the extra-CNS malformations and on epilepsy control. No biomarkers have been established.

## 12. Treatment

There is no disease-modifying therapy. Hedgehog agonists such as SAG would require a functional SMO, so they are not applicable.

- **Antiseizure medication (NCIT: Anticonvulsant Agent):** gelastic seizures are usually pharmacoresistant.
- **Surgery for the hamartoma:**
  - **MR-guided laser interstitial thermal therapy (MRgLITT; NCIT: Laser Interstitial Thermal Therapy).** In one series of 18 patients, *"12 of 15 (80%) patients with gelastic seizures and 5 (56%) of 9 patients with nongelastic seizures were seizure free"* ([PMC9658093](https://pmc.ncbi.nlm.nih.gov/articles/PMC9658093)). A 2024 meta-analysis concluded that MRgLITT *"might be a feasible and effective technique… leading to seizure freedom in a large proportion of patients"*. Pooled figures were not verified.
  - **Pediatric laser series:** Southwell 2018 (J Neurosurg Pediatr 21), report of 5 cases.
  - **Other options:** stereotactic radiofrequency thermocoagulation, Gamma Knife radiosurgery (NCIT: Radiosurgery), and endoscopic or open disconnection or resection. In one Rubino brother, the abstract describes *"endoscopic endonasal biopsy and subtotal resection"*.
  - **Morbidity:** one review reports permanent morbidity in up to 20% after ablation, mainly hypothalamic or endocrine and memory effects ([Neurosurg Rev](https://link.springer.com/content/pdf/10.1007/s10143-020-01298-z.pdf)).
- **Other surgery:** AVSD repair, pull-through surgery for Hirschsprung disease, polydactyly excision, and cleft palate repair.
- **Supportive care:** endocrine monitoring (GnRH agonist if precocious puberty develops), neuropsychology, speech therapy, and educational support.
- **Gene, cell, or RNA therapy:** none.
- **Clinical trials:** no SMO-PHLS-specific trials were identified.
- **Pharmacogenomics:** not applicable.

## 13. Prevention

There is no primary prevention. Options are:
- genetic counselling (25% recurrence risk);
- carrier testing of relatives;
- prenatal or preimplantation genetic testing once both variants are known;
- prenatal ultrasound or MRI for polydactyly, AVSD, or a hypothalamic mass.

Tertiary prevention means early epilepsy surgery to limit epileptic encephalopathy, and early recognition of Hirschsprung disease to avoid enterocolitis. Vaccines, public-health and environmental measures do not apply.

## 14. Other Species

- **Orthologues:** mouse Smo (MGI:108075), zebrafish smo, and Drosophila smo, the founding gene of the pathway. Hedgehog–Smoothened signalling is highly conserved.
- **Natural disease:** no OMIA entry for naturally occurring hypothalamic hamartoma or SMO-PHLS was found.
- **Zoonotic potential:** none.

## 15. Model Organisms

- **Smo-null mouse** (Zhang et al., Cell 2001;105:781–792, *"Smoothened mutants reveal redundant roles for Shh and Ihh signaling…"*). The mutant *"Smo acts epistatic to Ptc1"*, and the study showed *"a role in cardiac morphogenesis"*. Homozygous nulls die at about E9.5 with cyclopia and holoprosencephaly (JAX/Harvard listing). This makes the model too severe to reproduce HH. The cardiac phenotype supports the AVSD mechanism.
- **Conditional Smo alleles (Smo^flox):** allow tissue-specific deletion in diencephalon, limb, or enteric neural crest. HH-specific recapitulation was not retrieved.
- **Patient fibroblasts** (Le 2020): show Hh transduction and GLI2 ciliary-trafficking defects with normal cilia.
- **cDNA/splicing assays** (Green 2022).
- **Gap:** no model faithfully reproduces hypothalamic hamartoma. Hypomorphic Smo mice and patient iPSC-derived hypothalamic organoids are logical next steps; none were found in the literature.

Resources: MGI, IMPC, ZFIN, FlyBase.

---

### Key sources
- [OMIM #241800 (mirror)](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/241800)
- Rubino et al. 2018, PMID 30497210 — [abstract](https://curehunter.com/public/pubmed30497210.do)
- Le et al. 2020, PMID 32413283 — [PubMed](https://pubmed.ncbi.nlm.nih.gov/32413283/)
- Green et al. 2022 EJHG — [PMC8904774](https://pmc.ncbi.nlm.nih.gov/articles/PMC8904774)
- Green et al. 2022 HMG, PMID 35137044 — [PMC9307310](https://pmc.ncbi.nlm.nih.gov/articles/PMC9307310)
- Hildebrand et al. 2016, PMID 27453577 — [PMC4974069](https://pmc.ncbi.nlm.nih.gov/articles/PMC4974069)
- Saitsu et al. 2016 — [PMC4863748](https://pmc.ncbi.nlm.nih.gov/articles/PMC4863748)
- MRgLITT outcomes — [PMC9658093](https://pmc.ncbi.nlm.nih.gov/articles/PMC9658093); [Neurosurg Rev review](https://link.springer.com/content/pdf/10.1007/s10143-020-01298-z.pdf); [NHS England evidence review](https://www.england.nhs.uk/wp-content/uploads/2022/10/2006-mrg-litt-evidence-review.pdf)
- Smo knockout mouse — [Harvard OTD listing](https://otd.harvard.edu/explore-innovation/research-tools/smo-knock-out-mice/)

**Not retrieved this session:**
- PMIDs for Saitsu 2016, Green 2022 EJHG, and Zhang 2001;
- the exact Le 2020 variant table;
- Orphanet and ICD codes;
- ClinVar and gnomAD data.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 56 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 12 |
| Terms whose name was checked | 13 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0025258` (1 mention) - the report calls it "Dacrystic seizure; ID to verify"; HP calls it **Stiff neck**
- `UBERON:0001898` (1 mention) - the report calls it "hypothalamus, especially the tuber cinereum and mammillary region"; UBERON calls it **hypothalamus**
- `UBERON:0004148` (1 mention) - the report calls it "atrioventricular septum"; UBERON calls it **cardiac vein**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0097711` (obsolete ciliary basal body-plasma membrane docking) (1 mention) - replaced by `GO:1905349`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0006695` (1 mention) - the report calls it "Atrioventricular septal defect"; HP calls it **Atrioventricular canal defect**, and lists "Atrioventricular septal defect" among its other names
- `HP:0002251` (1 mention) - the report calls it "Hirschsprung disease / rectosigmoid aganglionosis"; HP calls it **Aganglionic megacolon**, and lists "Hirschsprung disease" among its other names
- `UBERON:0001716` (1 mention) - the report calls it "palate"; UBERON calls it **secondary palate**, and lists "palate" among its other names

### Terms the ontology service could not be reached for

11 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `HP:0010296` (1 mention)
- `HP:0003196` (1 mention)
- `HP:0000239` (1 mention)
- `HP:0002984` (1 mention)
- `HP:0004322` (1 mention)
- `GO:0097542` (1 mention)
- `CL:0000540` (1 mention)
- `CL:0011005` (1 mention)
- `CL:0000057` (1 mention)
- `UBERON:0002495` (1 mention)
- `MGI:108075` (1 mention)

### Terms whose obsolescence could not be checked

5 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `MONDO:0009436` (1 mention)
- `HP:0000171` (1 mention)
- `UBERON:0002389` (1 mention)
- `UBERON:0002005` (1 mention)
- `UBERON:0004176` (1 mention)