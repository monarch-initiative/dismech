---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-09T00:42:51.804136'
end_time: '2026-11-09T00:48:59.508054'
duration_seconds: 367.7
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Hypomyelinating Leukodystrophy 18
  mondo_id: MONDO:0032730
  category: Mendelian
  causal_genes: DEGS1
  omim_id: OMIM:618404
  synonyms: DEGS1-HLD; DEGS1-related hypomyelinating leukodystrophy; HLD18
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
  web_search_requests: 4
  num_turns: 39
  total_cost_usd: 3.0026355999999987
  session_id: b2cb0ac4-13d2-45b9-9368-a37671d4f330
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 4
citation_count: 10
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 3
  relevance_assessed: 21
  on_topic: 10
  validator_version: 0.5.1
term_validation:
  total_terms: 62
  verified: 60
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 8
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: DOID:0070399
    reported_labels:
    - DOID
    ontology_label: hypomyelinating leukodystrophy 18
  - term_id: HP:0001332
    reported_labels:
    - Common in the severe form
    ontology_label: Dystonia
  - term_id: HP:0001508
    reported_labels:
    - A major problem after age 2, even with gastrostomy
    ontology_label: Failure to thrive
  - term_id: HP:0001249
    reported_labels:
    - Dolgin family (4/4)
    ontology_label: Intellectual disability
  - term_id: HP:0002650
    reported_labels:
    - Dolgin, Karsai
    ontology_label: Scoliosis
  - term_id: HP:0007108
    reported_labels:
    - 5/14 tested (nerve conduction velocity <35 m/s); sural biopsy shows thin myelin
      (Karsai)
    ontology_label: Demyelinating peripheral neuropathy
  - term_id: HP:0008936
    reported_labels:
    - Vaia 2026
    ontology_label: Axial hypotonia
  - term_id: NCIT:C15747
    reported_labels:
    - verify a gastrostomy procedure term
    ontology_label: Supportive Care
  labels_variant: 6
  obsolete_terms:
  - term_id: GO:0034435
    ontology_label: obsolete cholesterol esterification
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypomyelinating Leukodystrophy 18
- **MONDO ID:** MONDO:0032730 (if available)
- **Causal gene(s):** DEGS1
- **OMIM:** OMIM:618404
- **Synonyms:** DEGS1-HLD; DEGS1-related hypomyelinating leukodystrophy; HLD18
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Hypomyelinating Leukodystrophy 18** covering all of the
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

Fetching PubMed summaries for the 23 DEGS1 papers I found.

Getting verbatim abstract sentences from the NCBI efetch API, since the PubMed web pages are blocked behind a cookie wall.

Pulling clinical details and the variant list from the Pant 2019 full text before I write the report.

# Hypomyelinating Leukodystrophy 18 (HLD18, DEGS1-related): research report

## How this report was made

The literature was gathered from PubMed (esearch, esummary and efetch), the Europe PMC and PMC full texts of the two founding papers (Pant 2019, Karsai 2019), the MONDO record in OLS, and the ClinGen gene-validity row already committed in this repository (`cache/clingen/gene_validity.csv`).

Quoted snippets are the abstract wording as the NCBI efetch tool returned it. Run them through `just fetch-reference` and `just count-verified-snippets` before using them as evidence.

The OMIM page (omim.org) returned HTTP 403 and was not read. The OMIM gene number for DEGS1 below comes from secondary sources.

I did not look up the ontology CURIEs marked †. They are leads only. Each must be resolved with `runoak` or the `cache/` files before it is bound (CLAUDE.md: *Every CURIE is read from a source in the same step it is written*).

---

## 1. Disease information

**Overview.** HLD18 is an autosomal recessive, early-onset hypomyelinating leukodystrophy. It is caused by biallelic loss-of-function variants in **DEGS1** (delta 4-desaturase, sphingolipid 1; hgnc:13709). DEGS1 is a lipid desaturase that sits in the endoplasmic reticulum (ER) and at mitochondria-associated ER membranes (MAMs). It performs the last step of de novo ceramide synthesis. In Pant et al. 2019: "This enzyme converts dihydroceramide (DhCer) into ceramide (Cer) in the final step of the de novo biosynthesis pathway." Losing it causes dihydrosphingolipid species to build up, and that build-up causes hypomyelination of the central nervous system (CNS) and, in some patients, demyelination of the peripheral nervous system (PNS).

**Identifiers**

| Resource | ID | Source |
|---|---|---|
| MONDO | MONDO:0032730, "leukodystrophy, hypomyelinating, 18" | OLS |
| OMIM (disease) | 618404 | MONDO xref |
| OMIM (gene) | 615843 | PanelApp / FlyBase, secondary |
| DOID | DOID:0070399 | MONDO xref |
| GARD | 0025731 | MONDO xref |
| MedGen | 1680067 | MONDO xref |
| UMLS | C5193078 | MONDO xref |
| Orphanet, MeSH, ICD-10/11 | No disease-specific xref on the MONDO record; none found | — |

Under ICD it would fall within the general leukodystrophy codes; that is an inference, not a mapping.

- **ClinGen:** DEGS1 for MONDO:0032730 is rated **Strong**, mode of inheritance AR. It was assigned by the Leukodystrophy and Leukoencephalopathy Gene Curation Expert Panel (SOP11) on 2026-01-14, as `CGGV:assertion_8a3090a0-8f88-4114-9438-87f8645ea133-2026-01-14T170000.000Z`.
- **Synonyms:** DEGS1-HLD; DEGS1-related hypomyelinating leukodystrophy; HLD18; hypomyelinating leukodystrophy 18; DEGS1-related leukodystrophy.
- **Source type:** The evidence is aggregated case series and case reports, plus experimental models. There is no EHR data. Grinberg 2025 counts the published patients: "DEGS1-related leukodystrophy has been described in 33 individuals to date" (PMID:41404352).

## 2. Etiology

- **Cause.** The cause is purely genetic: biallelic germline DEGS1 variants, homozygous or compound heterozygous, of the following kinds:
  - **Missense.** These lose function or lower protein levels.
  - **Nonsense and frameshift.**
  - **Splice-site.**
  - **Microdeletions.** A whole-gene or exon 2–3 deletion has been found in trans with a missense allele.
- **Risk factors.** Parental consanguinity is the main risk factor. Most reported families are consanguinious (Dolgin, Karsai, many Pant families). The recurrent p.(Asn255Ser) allele was seen in 3 of Pant's 13 families and again in Zanobio 2025 and Dolgin 2019 (as p.N255S). It may be a recurrent or founder allele, but no haplotype study exists.
- **Environmental risk, protective factors, gene–environment interactions.** None are documented. Karsai tried a sphingolipid-rich diet in their patient. It "had only a minor effect" on the plasma profile and did not change the dihydro/total ratio. No modifier genes are known.

## 3. Phenotypes

Frequencies below are from the Pant 2019 cohort of 19 patients (PMC6391109) unless another source is named.

| Phenotype | Frequency, onset and course | Suggested HPO† |
|---|---|---|
| Onset in infancy | Mean 5.6 ± 7.2 months, range 0.5–24 months | HP:0003593 Infantile onset |
| Nystagmus / abnormal eye movements | All but 1 of 19; appears at 1–6 months | HP:0000639 Nystagmus |
| Severe motor arrest / global developmental delay | Severe form in 15/19 (79%) | HP:0001263; HP:0001270 Motor delay |
| Dystonia | Common in the severe form | HP:0001332 |
| Spasticity / spastic tetraplegia | Common and progressive (Karsai, Dolgin) | HP:0001257; HP:0002510 |
| Seizures (often drug-resistant) | About 80%, typically around age 2; ketogenic diet helped in 3 | HP:0001250; HP:0032794? (verify the drug-resistant term) |
| Profound failure to thrive | A major problem after age 2, even with gastrostomy | HP:0001508 |
| Feeding difficulties | Frequent; Vaia 2026 reports "severe feeding difficulties" | HP:0011968 |
| Acquired microcephaly | 3/19 (Pant); also Karsai and Grinberg | HP:0005484 Secondary microcephaly |
| Intellectual disability, mild to severe | Dolgin family (4/4) | HP:0001249 |
| Scoliosis | Dolgin, Karsai | HP:0002650 |
| Demyelinating peripheral neuropathy | 5/14 tested (nerve conduction velocity <35 m/s); sural biopsy shows thin myelin (Karsai) | HP:0007108 |
| Axial hypotonia | Vaia 2026 | HP:0008936 |
| Developmental regression | Dolgin ("severe regressive"), Zanobio | HP:0002376 |
| Neurogenic bladder, GERD | Karsai (single patient) | HP:0000011; HP:0002020 |
| **Imaging: cerebral hypomyelination** | 18/18 on MRI | HP:0006808 Cerebral hypomyelination |
| Thin corpus callosum | 76% | HP:0033725 (verify; older term HP:0002079) |
| Thalamic abnormality / atrophy | 11/15 (73%) | verify HP term |
| Progressive cerebellar (vermian) atrophy | 41% | HP:0001272 |
| Pallidal T2 hypointensity | 2 severe patients | — |
| Cerebellar white-matter calcifications | Vaia 2026 (single case), confirmed on CT | HP:0002514 Cerebral calcification (verify a cerebellar-specific term) |
| Prolonged central conduction on evoked potentials | 7/7 tested | verify |
| **Lab: raised DhCer and DhCer/Cer ratio** | Fibroblasts and muscle (Pant); blood (Karsai, Dolgin) | lab abnormality; no settled HPO term |

**Severity and variability.** Expressivity varies within and between families. Grinberg 2025 reports "notable variability in severity between them". Pant patient 3, a compound heterozygote for p.(Arg133Trp) and p.(Leu251Phefs*10), was the mildest case. Karsai's p.Ala280Val patient was alive at 22.

**Quality of life.** The disease causes profound dependency: most patients do not walk, need gastrostomy, and have refractory epilepsy. No formal QoL instrument (EQ-5D, SF-36) has been used in any published study.

Key quotes:
- Pant (PMID:30620337): "severe motor arrest, early nystagmus, dystonia, spasticity, and profound failure to thrive." and "MRI showed hypomyelination, thinning of the corpus callosum, and progressive thalamic and cerebellar atrophy".
- Dolgin (PMID:31186544): "had mild to severe intellectual disability, spastic quadriplegia, scoliosis and epilepsy in most".
- Karsai (PMID:30620338): "a patient with a multisystem neurological disorder of both the central and peripheral nervous systems".

## 4. Genetic and molecular information

- **Gene.** DEGS1, hgnc:13709, at chromosome 1q42.11. Reference transcript NM_003676. The protein is sphingolipid delta(4)-desaturase DES1, which carries an N-terminal myristoylation site and a fatty-acid-desaturase domain.
- **Inheritance.** Autosomal recessive (ClinGen AR, Strong).
- **Variant origin.** All reported variants are germline. No somatic disease is described.

**Reported variants** (not exhaustive):

| Variant | Type | Source |
|---|---|---|
| c.604delT p.(Tyr202Thrfs*8), homozygous | frameshift | Pant (index patient 6) |
| p.(Asn255Ser), = c.764A>G; also written p.(N219S) on another isoform, c.656A>G | missense, recurrent | Pant (3 families); Dolgin; Zanobio. Dei Cas: residual activity kept |
| p.(Trp107*) | nonsense | Pant (2 families) |
| p.(Arg133Trp) / p.(Leu251Phefs*10) | compound heterozygous | Pant (mild case) |
| c.110T>C p.(Met37Thr) | missense | Pant; Grinberg 2025 (homozygous, 4 relatives) |
| c.839C>T p.(Ala280Val) | missense; about 20% residual activity, about 80% less protein | Karsai. The paper also writes c.893C>T; check against NM_003676.3 |
| p.His132Arg | missense | Used as the disease variant in SH-SY5Y cells (Tzou 2021) |
| p.Leu175Gln | missense; partial activity | Dei Cas 2024 |
| c.565A>G p.(Asn189Asp) | missense; ClinVar conflicting, raised dhCer/Cer | Wong 2023 |
| c.337A>C p.(Asn113His) | missense | Vaia 2026 |
| p.Asp16His | missense, in trans with a 63-kb whole-gene deletion | Zanobio 2025 |
| p.Asn255Ser | in trans with a 7-kb exon 2–3 deletion | Zanobio 2025 |
| c.825+4_825+5delAGinsTT | 5′ splice variant → exon 2 skipping | Beale 2025/2026 (VUS resolved to pathogenic) |
| p.R331K (also printed R311K) | likely pathogenic, by biomarker | Hülsmeier 2023 |
| p.G270E | probably benign | Hülsmeier 2023 |

- **Variant class mix.** Pant's 13 variants were 7 truncating (4 stop-gain, 3 frameshift) and 6 missense. The single p.(Met37Thr) change was described as the only variant in the Δ4-desaturase domain.
- **Population frequency.** Dolgin's variant was "not found in a homozygous state in ExAC and gnomAD databases." There is no gnomAD carrier-frequency estimate.
- **Functional consequence: loss of function.** Dei Cas 2024 (PMID:38342436) reports: "In vitro desaturase activity was lost by many variants except L175Q and N255S", "the levels of cognate protein were 40%-80% lower", and "We conclude that loss of function and reduced protein levels are both relevant in disease pathogenesis." For the KB, use `functional_impact_category: LOSS_OF_FUNCTION`, and `PARTIAL_LOSS_OF_FUNCTION` for N255S and L175Q.
- **Copy-number variants.** Zanobio 2025 (PMID:40371095) recommends deletion testing, "underscoring the importance of considering whole or partial gene deletions in the diagnostic pipeline".
- **Modifier genes, epigenetics, chromosomal abnormalities.** None reported.

## 5. Environmental information

There are no environmental, lifestyle or infectious contributors. Not applicable.

## 6. Mechanism and pathophysiology

**Causal chain**

1. Biallelic DEGS1 loss-of-function variants **lead to** loss or reduction of sphingolipid Δ4-desaturase activity. This is shown directly: fibroblast activity was about 20% of normal (Karsai), and most variants lost activity in vitro (Dei Cas).
2. Loss of Δ4-desaturation **results in** accumulation of the substrate dihydroceramide (DhCer) and other dihydrosphingolipids, with a raised DhCer/Cer ratio. Cer, sphingosine, S1P and hexosylceramides fall. This is shown in patient fibroblasts, muscle and blood. Dolgin: "reduced levels of ceramide, sphingosine, sphingosine-1-phosphate and monohexosylceramides". Karsai: dihydro species were about 40% of plasma sphingolipids, against about 10% in controls.
   - **Branch 2a.** An atypical sphingoid base forms, SPB 18:1(14Z);O2, with the double bond at Δ14 instead of Δ4. Karsai calls it "potentially neurotoxic", but whether it is toxic in vivo has not been shown. Hülsmeier 2023 established it as a specific biomarker.
3. The changed sphingolipid pool **disrupts** mitochondria-associated membrane (MAM) integrity. DEGS1 "is a mitochondria-associated endoplasmic reticulum membrane-resident (MAM-resident) enzyme" (Planas-Serra 2023, PMID:36951944). Deficiency **leads to**:
   - a hyperfused mitochondrial network;
   - impaired sterol O-acyltransferase activity, with fewer cholesteryl esters;
   - abnormal lipid-droplet biogenesis;
   - more mitochondrial superoxide;
   - impaired respiration in muscle.

   These are shown in fibroblasts and muscle. Linking them to myelin failure is an inference.
4. In glia, DhCer accumulation **results in**:
   - ER expansion;
   - lipid-droplet depletion;
   - failure of neuronal ensheathment.

   This is shown in Drosophila (*ifc*), where the gene "is expressed primarily in glial cells" (Zhu 2025, PMID:40864161). Knocking down the upstream ceramide synthase (*schlank*) rescues it.
5. In neurons, DhCer accumulation **leads to** Rac1 mislocalisation and Rac1–NADPH oxidase (NOX)-dependent ROS, causing neurodegeneration. This is shown in Drosophila photoreceptors and in SH-SY5Y cells carrying H132R (Tzou 2021, PMID:33852856). Suppressing Rac1–NOX rescues it.
6. Glial and oligodendrocyte dysfunction **results in** fewer myelinating oligodendrocytes and CNS hypomyelination. In zebrafish *degs1* morphants, MBP+ oligodendrocytes fell by about 30% and the DhCer/Cer ratio rose about 10-fold (Pant). In patients, MRI shows hypomyelination. Schwann-cell involvement **leads to** a demyelinating peripheral neuropathy: thin myelin and widened Schwann-cell ER on sural biopsy (Karsai).
7. Hypomyelination together with neurodegeneration **results in** progressive thalamic and cerebellar atrophy, a thin corpus callosum, and the clinical picture:
   - motor arrest, spasticity and dystonia;
   - nystagmus;
   - epilepsy;
   - failure to thrive.

   Glial-primary disease drives neuronal death: knockdown "in glia but not neurons drives neuronal cell death" (Zhu 2025, fly). In humans this step is inferred.

**Therapeutic hinge (upstream of step 2).** Blocking ceramide synthase, one step before DEGS1, lowers DhCer accumulation. In zebrafish, fingolimod (FTY720) at 1.0 ng/µl was best: it reduced the DhCer/Cer ratio, improved locomotion and increased myelinating oligodendrocytes (Pant). Knocking down *schlank* rescues the fly phenotype (Zhu).

**Suggested terms†**

- **GO:**
  - sphingolipid delta-4 desaturase activity (GO:0042284)
  - ceramide biosynthetic process (GO:0046513)
  - sphingolipid metabolic process (GO:0006665)
  - myelination (GO:0042552)
  - oligodendrocyte differentiation (GO:0048709)
  - lipid droplet formation (GO:0140042)
  - mitochondrial fusion (GO:0008053)
  - response to oxidative stress (GO:0006979)
  - cholesterol esterification (GO:0034435)
  - Cellular component: mitochondria-associated ER membrane (GO:0044233); endoplasmic reticulum membrane (GO:0005789)
- **CL:** oligodendrocyte (CL:0000128), myelinating Schwann cell (CL:0002376), glial cell (CL:0000125), neuron (CL:0000540), fibroblast (CL:0000057; patient-cell readout).
- **CHEBI:** ceramide (CHEBI:17761), N-acylsphinganine/dihydroceramide (CHEBI:31488), sphingosine (CHEBI:16393), sphingosine 1-phosphate (CHEBI:37550), fingolimod (CHEBI:63115).
- **Biological scale tags:** step 1 MOLECULAR; steps 2–5 CELLULAR; step 6 TISSUE; step 7 ORGANISM.

**Omics.** Targeted lipidomics is the main omics readout.
- Byeon 2024 (PMID:39206579) built a multiplexed LC-MS/MS panel of 47 sphingolipids that detects DEGS1-HLD.
- Beale 2026 (PMID:42090037) added RNA-seq and splicing assays.
- I found no single-cell, spatial or CRISPR-screen studies of this disease.

## 7. Anatomical structures affected†

- **CNS.** Cerebral white matter (UBERON:0002316), corpus callosum (UBERON:0002336), thalamus (UBERON:0001897), cerebellum and vermis (UBERON:0002037), brainstem (UBERON:0002298), globus pallidus (UBERON:0001875).
- **PNS.** Peripheral nerve (UBERON:0001021), including the sural nerve.
- **Skeletal muscle.** Mitochondrial respiration defect and DhCer accumulation (Pant; Planas-Serra).
- **Subcellular.** ER, MAMs, mitochondria and lipid droplets (GO:0005811).
- **Laterality.** Bilateral and symmetric.

## 8. Temporal development

- **Onset.** Infantile, at 0.5–24 months, mean 5.6 months. Nystagmus and motor arrest are usually the first signs.
- **Course.** In the severe form (79%), motor development halts or regresses, seizures begin around age 2, and failure to thrive worsens over time. Cerebellar and thalamic atrophy can progress. Pant reports partial improvement of myelination on serial MRI in 6 patients, which suggests the white-matter disease is hypomyelinating rather than strictly demyelinating.
- **Milder or slower forms** exist: the Karsai patient was alive at 22, and the Dolgin family ranged from mild to severe.
- **Duration and remission.** The disease is lifelong. There is no remission.
- **Critical period.** Infancy is the critical window for myelination. Any substrate-reduction therapy would most plausibly help if started early; this is inferred.

## 9. Inheritance and population

- **Inheritance.** Autosomal recessive (HP:0000007). There is no evidence of reduced penetrance in biallelic carriers. Expressivity varies.
- **Anticipation and mosaicism.** Neither has been reported.
- **Epidemiology.** Fewer than 40 reported individuals (33 by late 2025, plus Vaia's and Beale's patients). No prevalence or incidence data exist. Use `CASES_IN_LITERATURE` with an `ULTRA_RARE`/`RARE` band.
- **Populations and geography.** Families come from many backgrounds: Pant's cohort was European/French/Spanish-led with international families; Karsai's family was Turkish and consanguineous; Dolgin's kindred was a consanguineous Israeli Bedouin/Arab family (check the ethnicity in the full text); Grinberg; Iranian (Fathi 2025, PMID:40594583); Chinese (Yan 2021, PMID:33597727); Italian (Zanobio, Vaia). Consanguinity is common.
- **Sex ratio.** No sex bias is expected or reported.
- **Carrier frequency.** Not established.

## 10. Diagnostics

- **Genetic testing.** Exome or genome sequencing is first-line in hypomyelinating leukodystrophy. DEGS1 is on leukodystrophy panels, for example Genomics England PanelApp panel 476. Add CNV analysis, either array CGH or CNV calling from exome/genome data, when only one variant is found or the variants do not segregate as expected (Zanobio). Use RNA-seq to resolve splice-region variants of uncertain significance (Beale).
- **Biochemical tests.**
  - **Plasma or fibroblast sphingolipidomics** showing raised DhCer and a raised DhCer/Cer ratio, measured by LC-MS/MS (Byeon 2024).
  - **SPB 18:1(14Z);O2** is a more specific biomarker for classifying variants. Hülsmeier 2023 (PMID:37890668): "the SPB 18:1(14Z);O2 seems to be a more specific biomarker to discriminate between pathogenic and benign DEGS1 variants."
  - **In vitro desaturase assay** (Dei Cas 2024).
- **Imaging.** MRI shows a diffuse hypomyelination pattern (T2/FLAIR hyperintensity), a thin corpus callosum, thalamic signal change or atrophy, and progressive cerebellar atrophy. SWI or CT may show cerebellar calcification.
- **Electrophysiology.** Nerve conduction studies (demyelinating neuropathy, NCV below 35 m/s in about one-third of those tested), evoked potentials (prolonged central conduction) and EEG.
- **Pathology.** Sural nerve biopsy shows thin myelin, myelin folding and widened Schwann-cell ER.
- **Differential diagnosis.**
  - Pelizaeus–Merzbacher disease (PLP1, X-linked) and PMLD (GJC2)
  - POLR3-related HLD (which has hypodontia and hypogonadotropism)
  - TUBB4A H-ABC (basal-ganglia atrophy)
  - SOX10 PCWH (with Waardenburg/Hirschsprung features)
  - Other sphingolipid disorders (FA2H/SPG35, CERS, SPTLC)
  - Mitochondrial leukoencephalopathies

  Nystagmus with infantile motor arrest, peripheral demyelination and a raised DhCer/Cer ratio together point to DEGS1.
- **Screening.** There is no newborn screening. Cascade carrier testing and prenatal or preimplantation testing are possible once the familial variants are known.

## 11. Outcome and prognosis

- **Mortality.** In Pant, 4 of 19 patients (about 26%) died in childhood, between 1.5 and 7 years. The paper's summary says mean 4.6 years, range 2.5–7, but its individual ages do not match those figures. Early death came from severe neurological disease and failure to thrive.
- **Survival into adulthood** is possible in milder genotypes; the Karsai patient was alive at 22.
- **Morbidity.**
  - Non-ambulatory, with spastic or dystonic tetraparesis
  - Refractory epilepsy
  - Gastrostomy dependence
  - Scoliosis and contractures
  - Neurogenic bladder
- **Prognostic factors.** Genotype appears to matter: truncating or null alleles go with the severe form, and residual-activity missense alleles (N255S, R133W/fs) with milder disease. This correlation is suggested, not formally established. No prognostic biomarkers are validated.

## 12. Treatment

There is no disease-modifying therapy. All care is supportive.

| Intervention | Notes | NCIT† |
|---|---|---|
| Antiseizure drugs (valproate, carbamazepine and others) | Often pharmacoresistant | Pharmacotherapy NCIT:C15986, with `therapeutic_agent` (CHEBI) |
| Ketogenic diet | Helped seizures in 3 of Pant's patients | Dietary Intervention NCIT:C15447; modality BEHAVIORAL |
| Gastrostomy / nutritional support | For failure to thrive | Supportive Care NCIT:C15747 (verify a gastrostomy procedure term) |
| Intrathecal baclofen, antispasticity drugs | Karsai patient, from age 19 | Pharmacotherapy + baclofen (CHEBI) |
| Physical, occupational and speech therapy | Rehabilitation | NCIT:C15302 / C15315 |
| Genetic counseling | — | NCIT:C15240 |
| **Experimental: fingolimod (FTY720)** | Preclinical only. In zebrafish, ceramide synthase inhibition "reduced the critical DhCer/Cer imbalance". There is no human trial. | Pharmacotherapy + fingolimod |
| Sphingolipid-rich diet | Tried in 1 patient; minimal biochemical effect (Karsai) | — |

- **Clinical trials.** I found no NCT or ICTRP trials for HLD18.
- **Gene, cell and RNA therapies.** None reported.

## 13. Prevention

- **Primary.** Carrier testing in at-risk relatives and in consanguineous couples; prenatal diagnosis or PGT-M for known familial variants.
- **Secondary.** Early sphingolipidomic or genetic diagnosis allows proactive management of seizures and nutrition.
- **Tertiary.** Prevent aspiration, contractures, scoliosis and malnutrition.
- **Not applicable.** Vaccination, lifestyle or public-health measures.

## 14. Other species and natural disease

- No naturally occurring animal disease was found; I did not search OMIA.
- **Orthologs:**
  - mouse *Degs1* (MGI:1097711)
  - zebrafish *degs1* (74% protein identity)
  - Drosophila *infertile crescent* (*ifc*), FlyBase homology group FBhh0001141
- DEGS1 function is conserved from flies to humans.
- Zoonotic and transmission questions are not applicable.

## 15. Model organisms

| Model | Recapitulation | Limitations | Ref. |
|---|---|---|---|
| Zebrafish *degs1* splice morpholino; *Tg(mbp:egfp)* | DhCer/Cer up about 10-fold; locomotion severely reduced (about 1,147 → 28 mm); about 30% fewer MBP+ oligodendrocytes; fingolimod rescue | Transient knockdown; larval stage only | PMID:30620337 |
| Drosophila *ifc* mutant / glial RNAi | DhCer accumulation, glial ER expansion, lipid-droplet loss, failed ensheathment, neuronal death; *schlank* knockdown rescues | No vertebrate myelin; uses ensheathment as a proxy | PMID:40864161 |
| Drosophila *ifc*-KO photoreceptors; SH-SY5Y DEGS1-H132R | DhCer → Rac1–NOX ROS → degeneration; rescued by Rac1–NOX suppression | Retina rather than white matter; neuronal-cell-line model | PMID:33852856 |
| Patient fibroblasts; HAP1 DEGS1-KO and HEK-293T DEGS1-KO cells | Dihydro species up (about 90% in KO); MAM defect, mitochondrial superoxide; variant activity assays | Non-neural cells | PMID:30620338, 36951944, 38342436 |
| Mouse *Degs1*⁻/⁻ | Premature death (about 8 weeks), tremors, growth failure, scaly skin, low ceramide (MGI summary). Heterozygotes are more insulin-sensitive. | CNS myelin not characterised in the source found; the work focused on metabolism | Holland et al. 2007, Cell Metab, PMID:17339025 (check the full text for the knockout phenotype) |

**Suggested KB links.** The zebrafish model would be PARTIALLY_RECAPITULATES the hypomyelination node, at MODERATE fidelity, with `model_scale` TISSUE. The fly model would also be PARTIALLY_RECAPITULATES, with a `PROXY_QUANTITY` divergence: glial ensheathment stands in for myelination.

---

## Notes for curation

- **An entry already exists.** `kb/disorders/Hypomyelinating_Leukodystrophy_18.yaml` is a skeletal entry created 2026-11-09. A stub, `stubs/Leukodystrophy_Hypomyelinating_18.yaml` (priority HIGH), is also still in the queue; the curating PR should delete it.
- **References to fetch before use** (`just fetch-reference PMID:…`): 30620337, 30620338, 31186544, 36951944, 37890668, 38342436, 40864161, 33852856, 41404352, 40371095, 42090037, 42260209, 37195341, 39206579. The ClinGen citation is `CGGV:assertion_8a3090a0-…`.
- **Unconfirmed points:**
  - Karsai's c.839C>T vs c.893C>T discrepancy.
  - The Pant age-at-death inconsistency.
  - Which variant reference sequence to use for the isoform-specific p.N219S / p.N255S naming.
- **No GeneReviews chapter was found** in this search. Confirm with `just check-genereviews`.

## Sources

- Pant DC et al. *J Clin Invest* 2019;129:1240–1256. PMID:30620337. [jci.org/articles/view/123959](https://www.jci.org/articles/view/123959), [PMC6391109](https://pmc.ncbi.nlm.nih.gov/articles/PMC6391109/)
- Karsai G et al. *J Clin Invest* 2019;129:1229–1239. PMID:30620338. [PMC6391115](https://pmc.ncbi.nlm.nih.gov/articles/PMC6391115/)
- Dolgin V et al. *Eur J Hum Genet* 2019. PMID:31186544
- Planas-Serra L et al. *J Clin Invest* 2023. PMID:36951944
- Hülsmeier AJ et al. *J Lipid Res* 2023. PMID:37890668
- Dei Cas M et al. *J Lipid Res* 2024. PMID:38342436
- Zhu Y et al. *eLife* 2025. PMID:40864161
- Tzou FY et al. *Cell Rep* 2021. PMID:33852856
- Tzou FY et al. *Prog Lipid Res* 2023 (review). PMID:37187315
- Grinberg M et al. *Neurol Genet* 2025. PMID:41404352
- Zanobio M et al. *Hum Mutat* 2025. PMID:40371095. [PMC12077970](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12077970/)
- Beale HC et al. *Hum Genet* 2026. PMID:42090037 ([medRxiv preprint](https://www.medrxiv.org/content/10.1101/2025.04.04.25325118.full.pdf))
- Vaia Y et al. *Neurol Sci* 2026. PMID:42260209
- Wong MST et al. *Clin Dysmorphol* 2023. PMID:37195341
- Byeon SK et al. *Clin Chem* 2024. PMID:39206579
- Yan H et al. *J Hum Genet* 2021. PMID:33597727
- Fathi M et al. *Sci Rep* 2025. PMID:40594583
- Holland WL et al. *Cell Metab* 2007. PMID:17339025
- [MGI Degs1 (MGI:1097711)](https://www.informatics.jax.org/marker/MGI:1097711)
- [Genomics England PanelApp DEGS1](https://panelapp.genomicsengland.co.uk/panels/476/gene/DEGS1/)
- [FlyBase FBhh0001141](https://flybase.org/reports/FBhh0001141.html)
- [GlyCosmos DOID:0070399](https://glycosmos.org/diseases/DOID:0070399)
- [Institut Imagine summary](https://www.institutimagine.org/en/loss-sphingolipid-desaturase-degs1-causes-hypomyelinating-leukodystrophy-600)
- OLS MONDO:0032730

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 21 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 62 |
| Resolved | 60 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 22 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0070399` (4 mentions) - the report calls it "DOID"; DOID calls it **hypomyelinating leukodystrophy 18**
- `HP:0001332` (1 mention) - the report calls it "Common in the severe form"; HP calls it **Dystonia**
- `HP:0001508` (1 mention) - the report calls it "A major problem after age 2, even with gastrostomy"; HP calls it **Failure to thrive**
- `HP:0001249` (1 mention) - the report calls it "Dolgin family (4/4)"; HP calls it **Intellectual disability**
- `HP:0002650` (1 mention) - the report calls it "Dolgin, Karsai"; HP calls it **Scoliosis**
- `HP:0007108` (1 mention) - the report calls it "5/14 tested (nerve conduction velocity <35 m/s); sural biopsy shows thin myelin (Karsai)"; HP calls it **Demyelinating peripheral neuropathy**
- `HP:0008936` (1 mention) - the report calls it "Vaia 2026"; HP calls it **Axial hypotonia**
- `NCIT:C15747` (1 mention) - the report calls it "verify a gastrostomy procedure term"; NCIT calls it **Supportive Care**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0034435` (obsolete cholesterol esterification) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011968` (1 mention) - the report calls it "Frequent; Vaia 2026 reports "severe feeding difficulties"; HP calls it **Feeding difficulties**
- `HP:0002376` (1 mention) - the report calls it "Dolgin ("severe regressive"), Zanobio"; HP calls it **Developmental regression**
- `GO:0034435` (1 mention) - the report calls it "cholesterol esterification"; GO calls it **obsolete cholesterol esterification**
- `GO:0044233` (1 mention) - the report calls it "Cellular component: mitochondria-associated ER membrane"; GO calls it **mitochondria-associated endoplasmic reticulum membrane contact site**, and lists "mitochondria-associated ER membrane" among its other names
- `CL:0000128` (1 mention) - the report calls it "CL:** oligodendrocyte"; CL calls it **oligodendrocyte**
- `CHEBI:17761` (1 mention) - the report calls it "CHEBI:** ceramide"; CHEBI calls it **ceramide**, and lists "a ceramide" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MGI:1097711` - called "Degs1", "mouse *Degs1"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.