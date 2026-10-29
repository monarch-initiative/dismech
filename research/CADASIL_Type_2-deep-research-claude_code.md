---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-28T01:27:29.334977'
end_time: '2026-10-28T01:32:54.037516'
duration_seconds: 324.7
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: CADASIL Type 2
  mondo_id: MONDO:0014768
  category: Mendelian
  causal_genes: HTRA1
  omim_id: OMIM:616779
  synonyms: CADASIL caused by mutation in HTRA1; CADASIL2; HTRA1 CADASIL
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
  web_search_requests: 6
  num_turns: 34
  total_cost_usd: 2.8285830000000005
  session_id: 0bfb328d-96db-5dca-803a-342a247b0264
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 5
citation_count: 13
reference_validation:
  total_references: 49
  verified: 49
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:27164673
  relevance_assessed: 49
  on_topic: 39
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 41
  verified: 35
  not_found: 0
  obsolete: 1
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 2
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: GO:0004252
    reported_labels:
    - molecular function; decreased
    ontology_label: serine-type endopeptidase activity
  - term_id: GO:0007179
    reported_labels:
    - direction contested
    ontology_label: transforming growth factor beta receptor signaling pathway
  - term_id: GO:0072593
    reported_labels:
    - emerging
    ontology_label: reactive oxygen species metabolic process
  - term_id: CL:0000128
    reported_labels:
    - downstream white-matter injury
    ontology_label: oligodendrocyte
  labels_variant: 2
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  - Orphanet
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CADASIL Type 2
- **MONDO ID:** MONDO:0014768 (if available)
- **Causal gene(s):** HTRA1
- **OMIM:** OMIM:616779
- **Synonyms:** CADASIL caused by mutation in HTRA1; CADASIL2; HTRA1 CADASIL
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **CADASIL Type 2** covering all of the
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

The local GeneReviews cache gives me the clinical baseline. Next I'm searching the primary literature on heterozygous HTRA1 disease for PMIDs and abstract quotes.

I have the main primary papers identified. Now I'm pulling exact PMIDs and abstract text from PubMed so the citations can be checked.

Shell network calls need approval, so I'm switching to fetching PubMed pages directly.

PubMed pages hit a captcha, so I'm using the NCBI E-utilities endpoint for abstracts instead.

# CADASIL Type 2 (HTRA1-related autosomal dominant cerebral small vessel disease): research report

**Target:** MONDO:0014768 · OMIM:616779 · causal gene **HTRA1** (HGNC:9476, written `hgnc:9476` in this repo), chromosome 10q26.13 · Mendelian, autosomal dominant

**Provenance:** prepared 2026-10-28.
- The clinical baseline comes from the GeneReviews *HTRA1 Disorder* chapter (PMID:20437615), which is already in `references_cache/`.
- Primary-paper quotes were taken from PubMed abstracts through NCBI E-utilities, using a fetch tool that summarises pages. Treat every quoted string as a lead. Run `just fetch-reference PMID:<id>` and check the snippet against the cached abstract before it goes into YAML.
- Every ontology CURIE suggested below is unverified and must be looked up before binding. CLAUDE.md requires this.

---

## 0. Note on the existing KB stub (`kb/disorders/CADASIL_Type_2.yaml`)

- **Synonyms that belong to a different disease.** The current entry lists `CARASIL` and `Maeda syndrome` as synonyms. Those names refer to the **recessive, biallelic** HTRA1 disease (CARASIL, OMIM:600142), which has its own MONDO term. MONDO:0014768 / OMIM:616779 is the **heterozygous, autosomal dominant** disease.
- **Recommendation:** keep CARASIL out of `synonyms`. Mention it only in `description`/`notes`, or as a related entity, as one end of the "HTRA1 disorder" spectrum.
- **Description:** the current text covers both conditions. It should be rewritten to describe the dominant disease.

---

## 1. Disease information

**Overview.** CADASIL2 is an adult-onset hereditary cerebral small vessel disease (CSVD) caused by **heterozygous pathogenic variants in HTRA1**. HTRA1 encodes high-temperature requirement A serine peptidase 1, a secreted, trimeric PDZ-domain serine protease.

Clinical picture:
- Typical features are progressive gait disturbance, lacunar strokes, cognitive decline and mood change, on a background of confluent white-matter hyperintensities, lacunes and microbleeds.
- Compared with CARASIL, onset is later and extraneurological features (alopecia, spondylosis) are milder and less frequent.

Supporting sources:
- GeneReviews (PMID:20437615): *"'HTRA1 cerebral small vessel disease' (HTRA1-CSVD) refers to the milder phenotype associated with a heterozygous HTRA1 pathogenic variant."*
- Verdura et al., *Brain* 2015 (PMID:26063658), the defining paper: onset is later than in CARASIL or CADASIL, CARASIL's typical extraneurological features are absent, and the disease otherwise resembles sporadic SVD.

**Identifiers**

| System | ID | Status |
|---|---|---|
| MONDO | MONDO:0014768 (*cerebral arteriopathy, autosomal dominant, with subcortical infarcts and leukoencephalopathy, type 2*) | Given in the brief; matches the KB stub |
| OMIM | 616779 | Given |
| Orphanet | **ORPHA:482077** (*HTRA1-related autosomal dominant cerebral small vessel disease*) | Taken from OMIM/GenCC cross-references; confirm in ORPHA cache (`just fetch-reference ORPHA:482077`) |
| MedGen | C4225242 / 895965 | From a MedGen page found in search; verify |
| ICD-10 | I67.8 (other specified cerebrovascular disease) applies generically; there is no specific code | — |
| GeneReviews | *HTRA1 Disorder*, PMID:20437615 (NBK32533) | Cached |

**Synonyms:** CADASIL2; CADASIL type 2; HTRA1-CSVD; HTRA1-related autosomal dominant CSVD (HTRA1-AD-cSVD); "symptomatic/manifesting heterozygotes of CARASIL" (older usage, e.g. PMID:27164673).

**Data basis:** aggregated disease-level resources (OMIM, GeneReviews, Orphanet) plus case series, systematic reviews and population biobank studies (UK Biobank, BioBank Japan). No EHR-derived phenotype profile exists.

---

## 2. Etiology

**Causal factor.** Heterozygous germline HTRA1 variants: missense variants clustered in the protease domain, and also nonsense and frameshift variants. Variant classes and mechanism are covered in §4.

**Genetic risk and modifiers**
- **Variant position and pathogenicity score affect severity.** Systematic review (PMID:33963955): *"clinical phenotype severity was independently related to the pathogenicity score (CADD score; p < 0.05)"*. Also: *"patients with mutations in exon 4 (p = 0.0001) presented with more severe clinical symptoms"*.
- **Common HTRA1 variation (polygenic arm, separate from the Mendelian disease):**
  - rs2293871 is associated with extreme CSVD MRI burden and with small-vessel ischaemic stroke (PMID:30859180).
  - A common variant that raises circulating HTRA1 increases ischaemic stroke risk (PMID:39196222).
- **Semidominance.** Within one consanguineous family, the same allele (p.Pro275Leu) produced CARASIL when homozygous and CADASIL2 when heterozygous (PMID:34303089): *"CARASIL and CADASIL type 2 are two clinical consequences of the same disorder with different severities"*.

**Environmental and lifestyle risk factors**
- **Vascular risk burden increases penetrance.** UK Biobank (PMID:36300346): *"Cardiovascular risk burden is associated with the penetrance of such variants."*
- **Smoking and high-salt diet.** GeneReviews advises avoiding both because they *"may hasten the progression of arteriosclerosis"*.
- **Smoking in common-variant stroke susceptibility.** An HTRA1 × smoking interaction has been reported for stroke susceptibility in Chinese Han cohorts (PMID:33746601). This concerns common variants, not the Mendelian disease.
- **Hypertension** is a frequent comorbidity in case series. Strict risk-factor control is proposed as protective (PMID:36530220): *"strict control of vascular risk factors can prevent vascular events in uniallelic HTRA1 carriers."*

**Protective factors:** none established. Control of vascular risk factors is the only plausible modifiable protection.

**Gene–environment interaction:** the vascular-risk-burden × carrier-status effect on stroke (PMID:36300346) is the best-supported interaction.

---

## 3. Phenotypes

Main sources:
- GeneReviews (PMID:20437615)
- Uemura et al. 2020 review of 46 symptomatic carriers vs 28 CARASIL patients (PMID:32719647)
- Chinese series of 21 HTRA1-AD-cSVD patients compared with CADASIL (PMID:40607620)
- Comparison of Chinese HTRA1-CSVD with CADASIL (PMID:36047879)

HPO IDs are suggestions and must be checked against the cache or OAK before binding.

| Phenotype | Suggested HPO | Onset / course | Frequency and evidence |
|---|---|---|---|
| Leukoencephalopathy / confluent WMH | HP:0002352 Leukoencephalopathy | Adult; progressive | Near-universal on MRI. One study found a lower WMH proportion than in CADASIL (PMID:36047879) |
| Gait disturbance (often the first symptom) | HP:0001288 Gait disturbance | After age 40; slowly progressive | GeneReviews: *"The most frequent initial symptom in individuals with HTRA1-CSVD is slowly progressive gait disturbance after age 40 years"* |
| Spasticity / pyramidal signs | HP:0001257 Spasticity | Adult; progressive | Common; treated with baclofen or tizanidine per GeneReviews |
| Stroke (lacunar ischaemic) / stroke-like episodes | HP:0001297 Stroke (narrower lacunar term to be checked) | After 40 | GeneReviews: *"A majority of affected individuals have a stroke-like episode after age 40 years."* PMID:40607620: *"Stroke occurred in 81.0% of HTRA1-AD-cSVD patients"* |
| Lacunes on MRI | (radiological; consider an HP lacunar-infarct term) | — | *"lacunes in 90.5%"* (PMID:40607620) |
| Cerebral microbleeds, including brainstem-surface "chocolate chip sign" | HP:0002170? (verify the microbleed term) | — | *"⩾10 cerebral microbleeds (CMBs) in 66.7%"* (PMID:40607620). The SWI chocolate chip sign around the midbrain reached AUC 0.817 (PMID:40017561; also PMID:39270409, PMID:40866829) |
| Cognitive impairment / vascular dementia | HP:0100543 Cognitive impairment; HP:0000726 Dementia | Later course | *"47.6% exhibited cognitive dysfunction"* (PMID:40607620) |
| Mood change: apathy, irritability, depression | HP:0000741 Apathy; HP:0000737 Irritability; HP:0000716 Depression | Follows gait onset | GeneReviews (*"may be followed by the development of mood changes and cognitive dysfunction"*) |
| Pseudobulbar palsy / dysarthria | HP:0007024 Pseudobulbar paralysis; HP:0001260 Dysarthria | Advanced | Mainly CARASIL; seen in some heterozygotes |
| Spondylosis / lumbar disc disease, low back pain | HP:0003419 Low back pain; spondylosis term to verify | Variable | GeneReviews: *"Spondylosis and alopecia are seen in a minority of individuals with HTRA1-CSVD."* PMID:36047879: more spine disorders than in CADASIL |
| Alopecia | HP:0001596 Alopecia | Can be early (PMID:40499346) | Minority |
| Urinary incontinence / urgency | HP:0000020 | Advanced | Reported in case series |
| Small-fibre neuropathy (rare) | HP:0003487? (verify) | — | Single report (PMID:33313782) |

**Quality of life.** Gait failure, cognitive decline and apathy drive disability. No EQ-5D or SF-36 data specific to HTRA1 were found.

**Age at onset.** Symptomatic carriers start significantly later than CARASIL patients (PMID:32719647): *"The ages at onset of neurological symptoms/signs were significantly higher in symptomatic carriers than in CARASIL"*. Onset is usually in the 5th–6th decade. Young-onset severe disease is reported with p.A252T (PMID:36530220).

---

## 4. Genetic and molecular information

**Gene.** HTRA1 (HGNC:9476; OMIM *602194). It has an N-terminal IGFBP/Kazal module, a trypsin-like serine protease domain (catalytic triad H220/D250/S328) and a C-terminal PDZ domain. Activity depends on homotrimer formation and an inter-subunit activation cascade involving loops L3, LD and L1.

**Variant classes and mechanism**

1. **Missense variants in the protease domain**, enriched in exon 4. Two dominant-negative routes have been described: inability to form stable trimers, or trimers that cannot pass on activation.
   - PMID:27164673 (Nozaki 2016): *"These mutant HTRA1s showed markedly decreased protease activities and inhibited wild-type HTRA1 activity"*. Also: *"G283E and T319I HTRA1, observed in manifesting heterozygotes, did not form trimers."*
   - PMID:31316458 (Uemura 2019): *"10 of 11 hetero-HTRA1s and two of six CARASIL-HTRA1s were either defective in trimerization"*. Also: *"eight of 11 hetero-HTRA1s … inhibited WT protease activity"*.
   - Examples: p.R166L (the Verdura founder family), p.G283E, p.P285L, **p.R302Q** (recurrent in Japan), p.T319I, p.A252T (also reported biallelic in CARASIL; severe when uniallelic, PMID:36530220), p.R274Q (knock-in mouse).
2. **Nonsense and frameshift variants:** haploinsufficiency through nonsense-mediated decay. PMID:34270682 (*Brain* 2021): *"Twenty unrelated patients carrying a heterozygous HTRA1 variant leading to a premature stop codon were identified"*. mRNA showed *"a degradation of the mutated allele"*. The authors conclude *"heterozygous HTRA1 stop codons are pathogenic through a haploinsufficiency mechanism"*.
   - Supporting data: carriers' cells show about 50% HTRA1 expression (PMID:32017060): *"CSVD phenotype may also result from 50% of HTRA1 expression."*

**Functional consequence.** Loss of function in every case: haploinsufficiency for null alleles, dominant-negative for many missense alleles. In repo terms this is `LOSS_OF_FUNCTION` or `DOMINANT_NEGATIVE` in `functional_impact_category`, depending on the variant.

**Classification.** ClinVar holds many P/LP heterozygous HTRA1 variants. A curated P/LP review is PMID:37016629.

**ClinGen / GenCC.** GenCC lists HTRA1 for Orphanet:482077. The ClinGen gene–disease validity tier for the AD disease was not retrieved. Check `just list-gene-validity` and the CGGV cache before recording any tier, and never assign one yourself.

**Allele frequency and germline status.** All variants are germline. Rare damaging HTRA1 variants occur in roughly 1 in 450 UK Biobank participants (medRxiv 2021 preprint), so carrier frequency in the population is far higher than clinical disease prevalence.

**Modifier genes:** none established. A patient with coexisting NOTCH3 and HTRA1 variants has been reported (PMID:40634305).

**Epigenetics:** HTRA1 methylation in blood has been studied as a marker of preclinical stroke risk in the general population (PMID:36581876). It is not specific to CADASIL2.

**Chromosomal abnormalities:** not a recognised mechanism.

---

## 5. Environmental information

- **Exposures:** no causal environmental agent or infection.
- **Lifestyle:** smoking, high salt intake and the general vascular risk burden (hypertension, diabetes, dyslipidaemia) modify penetrance and progression (PMID:36300346; PMID:20437615).

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Heterozygous HTRA1 variant.** A null allele leads to NMD and roughly 50% HTRA1 protein (PMID:34270682, PMID:32017060). A missense allele leads to a defective trimer or a trimer that blocks the activation cascade, reducing activity of the wild-type subunits (dominant-negative; PMID:27164673, PMID:31316458).
2. **Reduced extracellular HTRA1 protease activity in the cerebral small-vessel wall** results in failure to cleave matrisome substrates.
   - Demonstrated in Htra1-/- mice (PMID:34779414).
   - Shown by proteomics in human CADASIL vessels (PMID:29725820), where HTRA1 is sequestered by NOTCH3 aggregates. This is the convergent "HTRA1 loss" mechanism.
3. **Matrisome accumulation in the vessel wall** (fibronectin, LTBP-4, EDA-fibronectin, versican and others) leads to intimal thickening and abnormal elastic lamina.
   - Shown in knockout and R274Q knock-in mice (PMID:34779414; LMU dissertation 2022).
   - Inferred for human heterozygotes from CARASIL autopsy and mouse data.
4. **Branch: dysregulated TGF-β family signalling.** The direction is disputed.
   - Original CARASIL work found mutant HTRA1 *"failed to repress"* TGF-β family signalling, implying increased signalling (Hara 2009, PMID:19387015).
   - Beaufort 2014 (PMID:25369932) found HTRA1 processes LTBP-1 and that its loss *attenuates* TGF-β signalling.
   - No change in pSMAD2/3 in carrier cells (PMID:32017060).
   - Increased TGF-β/SMAD in a lentiviral mutant endothelial model (PMID:39613464).
   - Treat this step as **contested**.
5. **Vascular smooth muscle cell (VSMC) dysfunction.** Loss of HTRA1 leads to impaired contractile maturation and a shift to the synthetic phenotype, with MMP9 induction, VSMC death and medial degeneration.
   - PMID:31796853: *"HTRA1 is essential for VSMC differentiation into the contractile phenotype."* JAG1/NOTCH3 signalling also increases.
   - PMID:29768431: *"Loss of HtrA1 therefore skews VSMCs toward the synthetic phenotype, induces MMP9 expression, and expedites cell death."*
   - Evidence: in vitro and mouse.
6. **Branch: endothelial oxidative stress.** HTRA1 deficiency leads to NOX4-driven ROS, blood–brain barrier disruption and cognitive impairment.
   - Mouse and in vitro work, 2026 (PMID:42169653). This is an emerging hypothesis.
7. **Arteriopathy of the small penetrating arteries** (wall thickening, loss of VSMCs, vasodilation/ectasia, reduced distensibility) results in impaired autoregulation and reduced cerebral blood flow.
   - Shown in mice: candesartan *"normalized the vascular distensibility and cerebral blood flow"* (PMID:34779414).
   - Human autopsy of a heterozygote: PMID:29797751.
8. **Chronic hypoperfusion of the deep white matter and focal occlusion** lead to leukoencephalopathy and lacunar infarcts. Fragile walls lead to microbleeds, preferentially on the brainstem surface (PMID:39270409).
9. **Disruption of white-matter tracts and lacunes** produces gait disturbance and spasticity, then cognitive and mood dysfunction, pseudobulbar signs and dementia.
10. **Extraneurological branch (inferred):** HTRA1 roles in bone and cartilage, and possibly in hair follicles, may explain spondylosis, disc disease and alopecia. The mechanism is not established.

**Ontology suggestions (verify each)**

- **GO terms:**
  - serine-type endopeptidase activity GO:0004252 (molecular function; decreased)
  - proteolysis GO:0006508
  - extracellular matrix organization GO:0030198
  - transforming growth factor beta receptor signaling pathway GO:0007179 (direction contested)
  - smooth muscle cell differentiation GO:0051145
  - reactive oxygen species metabolic process GO:0072593 (emerging)
- **CL terms:**
  - vascular associated smooth muscle cell CL:0000359
  - brain endothelial cell (verify the specific CL ID; generic endothelial cell CL:0000115)
  - brain pericyte CL:2000043
  - oligodendrocyte CL:0000128 (downstream white-matter injury)
- **Molecular profiling:**
  - vessel proteomics (PMID:29725820)
  - patient iPSC line carrying p.R302Q, with differential HTRA1 and NOG expression (PMID:37009886)
  - no single-cell or spatial data specific to CADASIL2 were found

---

## 7. Anatomical structures affected

- **Organ level:**
  - Brain. Primary sites are the cerebral white matter, basal ganglia, thalamus and pons/brainstem.
  - Spine: vertebrae and intervertebral discs.
  - Scalp hair, in a minority of patients.
  - Retinal involvement is reported mainly in CARASIL (e.g. macular oedema, PMID:38879362).
- **Tissue and cell level:** the walls of small penetrating arteries and arterioles, specifically the tunica media (VSMCs), the intima and the internal elastic lamina.
- **Subcellular level:** extracellular matrix (GO:0031012) and extracellular space (GO:0005615), where HTRA1 is secreted.
- **UBERON suggestions (verify):** cerebral white matter, basal ganglion, pons, arteriole (UBERON:0001980), vertebral column.
- **Lateralization:** bilateral and symmetric white-matter disease; lacunes are multifocal.

---

## 8. Temporal development

- **Onset:** adult, usually after age 40. Onset is insidious: gait first, then mood and cognition. Occasional early onset with p.A252T or early alopecia (PMID:36530220, PMID:40499346).
- **Progression:** slow and progressive. No formal staging exists. GeneReviews describes CARASIL as progressing slowly after symptom onset.
- **Remission:** none.
- **Critical window for intervention:** the presymptomatic carrier period, when vascular risk factors can still be controlled.

---

## 9. Inheritance and population

- **Inheritance:** autosomal dominant (HP:0000006). Penetrance is **incomplete and age-dependent**, and is modified by vascular risk. Expressivity is variable, from MRI-only findings to severe disease.
  - UK Biobank: HTRA1 carriers were *"at least 66% more likely to have had stroke"* (PMID:36300346, pooled monogenic-SVD genes). In a separate 200,000-participant study, rare variants in five CSVD genes occurred in 0.5% of participants, with weak phenotype associations for HTRA1 (PMID:36035235).
- **Frequency among patients with familial or adult CSVD:**
  - 4.97% of NOTCH3-negative familial SVD probands; association statistics *"P = 4.2 × 10(-6); odds ratio = 15.4"* (PMID:26063658)
  - 2.08% (7/337) in Taiwan (PMID:29895533)
  - 11 HTRA1 cases in a Japanese monogenic-CSVD series in which NOTCH3, HTRA1 and ABCC6 together explained 94% (PMID:36261288)
  - 0.8–6.5% of NOTCH3-negative CSVD worldwide (secondary review)
- **Prevalence:** no population prevalence has been measured. Orphanet likely lists it as unknown (<1/1,000,000 class); check ORPHA:482077. Variant carrier frequency is about 1/450, but clinical disease is much rarer, so use `measure_type: UNKNOWN` or `CASES_IN_LITERATURE` until a source says otherwise.
- **Anticipation:** none. **Mosaicism:** not described. **Consanguinity:** relevant to the biallelic form only.
- **Founder effects and geography:** reported in Europe, Japan (R302Q recurrent), China (largest case series), Taiwan, India and Africa (PMID:32042911).
- **Sex ratio:** no consistent sex bias reported.

---

## 10. Diagnostics

- **Genetic testing:** diagnosis rests on finding a heterozygous P/LP HTRA1 variant (GeneReviews). Recommended routes are a CSVD gene panel (NOTCH3, HTRA1, COL4A1/2, ABCC6, TREX1, GLA, CTSA) or exome sequencing. Verdura: *"screening of HTRA1 should be considered in all patients with a hereditary small vessel disease of unknown aetiology."* mRNA analysis can confirm NMD for stop variants (PMID:34270682).
- **Imaging (MRI):**
  - confluent WMH, lacunes, microbleeds, dilated perivascular spaces
  - brainstem/pontine "chocolate chip sign" on SWI as a candidate biomarker (PMID:40017561, PMID:40866829, PMID:40632435)
  - anterior temporal pole WMH is less common than in CADASIL1 (PMID:40607620)
  - 7T caveat: sulcal vessels can mimic microbleeds (PMID:39569513)
- **Biopsy and pathology:** no skin-biopsy marker equivalent to GOM. Autopsy shows arteriosclerosis of small arteries with loss of medial smooth muscle and intimal thickening (PMID:29797751, PMID:36524103).
- **Laboratory:** no specific biomarker. Routine vascular risk work-up applies.
- **Differential diagnosis:** CADASIL1 (NOTCH3; GOM on skin biopsy, temporal pole and external capsule WMH), CARASIL (biallelic, earlier onset), COL4A1/2 disease, Fabry disease, CARASAL (CTSA), RVCL-S (TREX1), sporadic hypertensive arteriolosclerosis, multiple sclerosis and CNS vasculitis (misdiagnoses reported, PMID:36334553, PMID:40997360), and adult-onset leukodystrophies.
- **Screening:** cascade testing of relatives after genetic counselling. No newborn or population screening.

---

## 11. Outcome and prognosis

- **Survival:** no survival or life-expectancy data exist. Progressive disability and dementia accumulate over years to decades.
- **Complications:** recurrent stroke, vascular dementia, gait failure leading to falls and dependence, depression.
- **Prognostic factors:** variant domain (exon 4) and CADD score (PMID:33963955), plus vascular risk burden (PMID:36300346).
- **Recovery:** none. Management is supportive.

---

## 12. Treatment

**No disease-modifying therapy exists.** GeneReviews management (PMID:20437615) with suggested NCIT bindings (verify each):

| Intervention | Suggested NCIT term | Notes |
|---|---|---|
| Antiplatelet therapy, used cautiously when microbleeds are present | Pharmacotherapy NCIT:C15986, plus `therapeutic_agent` (e.g. aspirin, CHEBI) | GeneReviews: *"Consideration of anti-platelet therapy and anti-hypertensive therapy"* |
| Antihypertensive therapy and vascular risk control | NCIT:C15986, plus an agent class | Supported by penetrance data (PMID:36300346, PMID:36530220) |
| Spasticity drugs (baclofen, tizanidine) | NCIT:C15986, plus CHEBI baclofen / tizanidine | GeneReviews |
| Physical therapy, walking aids, home adaptation | Physical Therapy NCIT:C15302; Rehabilitation NCIT:C15315 | `therapeutic_modality: BEHAVIORAL` |
| Wig for alopecia; standard care for spondylosis and mood disorder | Supportive Care NCIT:C15747 | — |
| Genetic counselling | Genetic Counseling NCIT:C15240 | — |

**Experimental and preclinical:**
- Candesartan (AT1 receptor blocker) prevented arteriopathy progression in Htra1-/- mice (PMID:34779414). This is preclinical only, in a CARASIL model.
- The NOX4 inhibitor GLX351322 rescued BBB and cognitive deficits in mice (PMID:42169653).
- No registered ClinicalTrials.gov trial specific to HTRA1-CSVD was found in this search.

**Pharmacogenomics:** none.

---

## 13. Prevention

- **Primary:** no primary prevention for the variant itself. Preimplantation and prenatal testing are possible once the familial variant is known (GeneReviews).
- **Secondary and tertiary:** strict control of vascular risk factors, smoking cessation, and limiting salt intake (GeneReviews; PMID:36530220).
- **Counselling:** each offspring has a 50% risk. For the semidominant spectrum, offer counselling to all family members (PMID:34303089).

---

## 14. Other species and natural disease

- **Naturally occurring disease:** none found in OMIA for HTRA1-related cerebral arteriopathy.
- **Orthologs:** mouse *Htra1* (MGI). The protease is highly conserved; bacterial DegP/HtrA is the ancestral family.

---

## 15. Model organisms

| Model | Recapitulation | Key reference |
|---|---|---|
| **Htra1-/- mouse** | CARASIL-like arteriopathy: intimal thickening, abnormal elastic lamina, vasodilation, matrisome (FN, LTBP-4) accumulation, reduced distensibility and CBF. Used to test candesartan. Models the **biallelic** state, so it shows only partial fidelity for heterozygous disease | PMID:34779414 |
| Htra1-/- mouse, aortic VSMCs | Synthetic VSMC switch, MMP9, cell death | PMID:29768431 |
| Htra1-/- mouse, placenta | Intrauterine growth restriction and placental defects (off-target phenotype) | PMID:25446274 |
| **Htra1 R274Q knock-in mouse** | Vessel accumulation of FN, LTBP4, FBLN5 and EGFL8. Closer to a missense allele | LMU dissertation 2022 (not peer-reviewed) |
| Htra1 L364P mouse | Reported CARASIL-like features; VSMC apoptosis | PMID:31601092 |
| HTRA1-deficient VSMCs | Impaired contractile maturation; increased JAG1/NOTCH3 | PMID:31796853 |
| Patient iPSC line (heterozygous p.R302Q) | Cell resource; HTRA1 and NOG dysregulation | PMID:37009886 |
| Lentiviral missense HtrA1 in mouse brain endothelial cells | TGF-β/SMAD activation, ROS, apoptosis | PMID:39613464 |

**Limitations and suggested KB encoding**
- No heterozygous mouse model reproduces human CSVD.
- Mice lack the decades of vascular-risk exposure that drive penetrance.
- Candidate `HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` discussions: heterozygous mice, and the direction of TGF-β signalling.

---

## Key references (PMIDs)

**Clinical, genetic and population**
- 20437615: GeneReviews, *HTRA1 Disorder*
- 26063658: Verdura 2015, *Brain*
- 19387015: Hara 2009, *NEJM*
- 27164673: Nozaki 2016, *Neurology*
- 31316458: Uemura 2019, *Front Neurol*
- 34270682: stop-codon haploinsufficiency, *Brain* 2021
- 32719647: review, *Front Neurol* 2020
- 33963955: genotype–phenotype systematic review, 2021
- 40607620: HTRA1 vs NOTCH3 comparison, *Int J Stroke*
- 36047879: Chinese series compared with CADASIL
- 36261288: Japanese monogenic CSVD frequency
- 29895533: Taiwanese series
- 36530220: uniallelic p.A252T
- 34303089: semidominant family
- 36300346: UK Biobank penetrance
- 36035235: UK Biobank five-gene study
- 39196222: genetically proxied HTRA1 activity and stroke
- 30859180: rs2293871 and CSVD MRI extremes

**Imaging and pathology**
- 40017561, 39270409: chocolate chip sign and brainstem microbleeds
- 29797751: autopsy of a heterozygote

**Mechanism and models**
- 29725820: CADASIL vessels show an HTRA1 loss-of-function profile
- 25369932: HTRA1 processes LTBP-1
- 32017060: HTRA1 expression and TGF-β in carriers
- 31796853: HTRA1 and VSMC maturation
- 29768431: synthetic VSMC switch in Htra1-/-
- 34779414: candesartan in Htra1-/- mice
- 42169653: endothelial NOX4
- 37009886: patient iPSC line

**Web sources consulted:** [PMC7284040](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7284040/); [OMIM 616779 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/616779); [Verdura 2015 (HAL)](https://integ04-cnspfv.archimed.fr/doc/OAI_1/oai-HAL-hal-01987719v1); [Frontiers Neurol 2019 (Uemura)](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2019.00693/full); [QxMD 19387015](https://www.qxmd.com/r/19387015); [PMC10659557](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10659557/); [Cambridge UKB penetrance](https://neuroscience.cam.ac.uk/publications/the-prevalence-and-penetrance-of-monogenic-small-vessel-stroke-variants-in-450000-uk-biobank-participants); [medRxiv 2021 WMH preprint](https://www.medrxiv.org/content/10.1101/2021.03.26.21253954v1.full.pdf+html); [JCI 140555](https://jci.org/articles/view/140555/files/pdf); [LMU dissertation](https://edoc.ub.uni-muenchen.de/30627); [MedGen 895965](https://ncbi.nlm.nih.gov/medgen/895965); [GenCC HTRA1](https://thegencc.org/genes/HGNC:9476); [NCBI E-utilities](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/).

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 49 |
| Resolved | 49 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 49 |
| On topic | 39 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:27164673` *(abstract only)*: "symptomatic/manifesting heterozygotes of CARASIL"
  - Text part not found as substring: 'symptomatic/manifesting heterozygotes of CARASIL' (note: only abstract available for PMID:27164673, full text may contain this excerpt)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 5 |
| Terms whose name was checked | 8 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0004252` (1 mention) - the report calls it "molecular function; decreased"; GO calls it **serine-type endopeptidase activity**
- `GO:0007179` (1 mention) - the report calls it "direction contested"; GO calls it **transforming growth factor beta receptor signaling pathway**
- `GO:0072593` (1 mention) - the report calls it "emerging"; GO calls it **reactive oxygen species metabolic process**
- `CL:0000128` (1 mention) - the report calls it "downstream white-matter injury"; CL calls it **oligodendrocyte**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000020` (1 mention) - the report calls it "Urinary incontinence / urgency"; HP calls it **Urinary incontinence**
- `GO:0031012` (1 mention) - the report calls it "Subcellular level:** extracellular matrix"; GO calls it **extracellular matrix**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`, `Orphanet`.