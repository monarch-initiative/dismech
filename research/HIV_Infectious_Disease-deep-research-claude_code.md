---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-10-30T19:17:15.145424'
end_time: '2026-10-30T19:21:26.082696'
duration_seconds: 250.94
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: HIV Infectious Disease
  mondo_id: MONDO:0005109
  category: Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Human immunodeficiency virus disease or disorder; HIV infection; Human
    immunodeficiency virus caused disease or disorder; Human immunodeficiency virus
    infectious disease
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
  - claude-opus-4-8
  - claude-opus-5-5
  web_search_requests: 2
  num_turns: 7
  total_cost_usd: 1.9312257000000004
  session_id: 07f4758f-171b-5128-8762-a80fdddaf3a5
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 2
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 10
  validator_version: 0.4.0
term_validation:
  total_terms: 59
  verified: 54
  not_found: 0
  obsolete: 2
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 5
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: GO:0075713
    reported_labels:
    - establishment of integrated proviral latency
    - Integrase inserts the provirus into host chromatin
    ontology_label: establishment of integrated proviral latency
  - term_id: UBERON:0002048
    reported_labels:
    - opportunistic pneumonia
    ontology_label: lung
  - term_id: UBERON:0002113
    reported_labels:
    - HIV-associated nephropathy
    ontology_label: kidney
  - term_id: UBERON:0002097
    reported_labels:
    - Kaposi sarcoma, seborrheic dermatitis
    ontology_label: skin of body
  - term_id: UBERON:0004535
    reported_labels:
    - accelerated atherosclerosis
    ontology_label: cardiovascular system
  - term_id: CHEBI:75985
    reported_labels:
    - dolutegravir
    ontology_label: CHEBI_75985
  - term_id: CHEBI:176859
    reported_labels:
    - lenacapavir
    ontology_label: PA(P-20:0/22:4(7Z,10Z,13Z,16Z))
  labels_variant: 6
  obsolete_terms:
  - term_id: HP:0005407
    ontology_label: obsolete Decreased proportion of CD4-positive helper T cells
    replaced_by: HP:0032218
  - term_id: CHEBI:75985
    ontology_label: CHEBI_75985
    replaced_by: CHEBI:5516
  unresolvable_prefixes:
  - LOINC
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** HIV Infectious Disease
- **MONDO ID:** MONDO:0005109 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Human immunodeficiency virus disease or disorder; HIV infection; Human immunodeficiency virus caused disease or disorder; Human immunodeficiency virus infectious disease
- **Category:** Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **HIV Infectious Disease** covering all of the
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

I have what I need. The existing `kb/disorders/HIV_Infectious_Disease.yaml` is already a substantial entry; the report below is written as a standalone research document to populate/augment it. The causal agent is the **human immunodeficiency virus (HIV-1/HIV-2, genus *Lentivirus*)** — this is an infectious disease, not a host-gene Mendelian disorder, so "causal gene" is not applicable; host genetics act only as modifiers (notably *CCR5*).

---

# HIV Infectious Disease — Comprehensive Research Report

**MONDO:0005109 · ICD-11 1C62 · ICD-10 B20–B24 · MeSH D015658 (HIV Infections) · NCBITaxon:11676 (HIV-1), NCBITaxon:11709 (HIV-2)**

---

## 1. Disease Information

HIV infectious disease is a chronic, progressive infection caused by the human immunodeficiency virus, a single-stranded positive-sense RNA retrovirus of the genus *Lentivirus* (family *Retroviridae*). HIV-1 (NCBITaxon:11676) is responsible for the global pandemic; HIV-2 (NCBITaxon:11709), largely confined to West Africa, is less transmissible and progresses more slowly. The virus establishes lifelong infection by integrating a DNA provirus into the host genome, with preferential depletion of CD4+ T lymphocytes. Untreated, progressive CD4+ depletion produces acquired immunodeficiency syndrome (AIDS), the advanced clinical stage defined by opportunistic infections, specific malignancies, or a CD4 count <200 cells/µL.

- **This is a disease-level, aggregated-resource concept**, not an EHR/individual-patient entity. Note dismech separately carries `Acquired_Immunodeficiency_Syndrome.yaml`; HIV infectious disease (MONDO:0005109) is the broader infection, of which AIDS is the advanced stage/sequela.
- **Identifiers:** MONDO:0005109; ICD-11 1C62 (human immunodeficiency virus disease); ICD-10 B20–B24; MeSH D015658; DO DOID:526; SNOMED CT 86406008.
- **Synonyms:** HIV infection; human immunodeficiency virus disease; HIV disease.
- **Key reviews (PMID):** 30030793 (Deeks et al., "HIV infection," *Nat Rev Dis Primers* 2015 — the canonical mechanistic review); 29884404 (latent reservoir); 39608393 (GBD 2021 HIV/AIDS burden).

---

## 2. Etiology

**Causal factor — infectious.** HIV is acquired through exposure to infected body fluids (blood, semen, vaginal/rectal secretions, breast milk). Transmission routes: condomless sexual contact (the dominant global route), parenteral exposure (shared injection equipment, contaminated blood products), and vertical/perinatal transmission (in utero, intrapartum, breastfeeding). Environmental exposure terms: `ECTO` exposure-to-virus concepts; transmission is modeled with `TransmissionRoute` = SEXUAL, PARENTERAL (bloodborne), VERTICAL.

**Risk factors (environmental/behavioral):** condomless anal or vaginal intercourse, multiple partners, concurrent STIs (especially genital ulcer disease — HSV-2, syphilis — which increase per-act transmission several-fold), injection drug use, receptive anal intercourse (highest per-act risk ~1.4%), untreated high-viral-load partner, lack of male circumcision (heterosexual men), and commercial sex work. Socioeconomic determinants (poverty, gender inequality, criminalization) are strong structural risk factors.

**Host genetic risk/protective modifiers (host genes are modifiers only, never causal):**
- ***CCR5*-Δ32 (hgnc:1606)** — a 32-bp deletion producing a truncated, non-surface-expressed CCR5 co-receptor. **Homozygotes are highly resistant to R5-tropic HIV-1 acquisition**; heterozygotes show slower progression. Allele frequency ~10% in Northern Europeans, near-absent in African/East Asian populations. This is the basis of the Berlin and London patient cures via CCR5-Δ32/Δ32 stem-cell transplants. (PMID:8898191 — Samson et al.; PMID:30855743 — London patient.)
- ***HLA* class I alleles**: HLA-B*57:01 and B*27:05 are associated with elite control/slow progression; HLA-B*35 with rapid progression.
- **CCL3L1 copy number, KIR/HLA combinations, APOBEC3** variants modulate susceptibility and progression.

**Protective factors (environmental/intervention):** correct/consistent condom use, voluntary medical male circumcision (~60% reduction in female-to-male transmission; PMID:17321311 — Auvert/Orange Farm trial), pre-exposure prophylaxis (PrEP), treatment-as-prevention (U=U, undetectable = untransmittable; PMID:31056293 — PARTNER2), and harm-reduction/needle-exchange programs.

**Gene–environment interaction:** CCR5 genotype modifies per-exposure acquisition risk; HLA background interacts with viral escape mutation to set the viral setpoint.

**GO/CHEBI/CL anchors:** GO:0046718 (viral entry into host cell), GO:0075713 (establishment of integrated proviral latency), CL:0000624 (CD4+ αβ T cell), CHEBI entries for the antiretroviral drug classes (see §12).

---

## 3. Phenotypes

HIV disease is staged clinically (CDC stages / WHO clinical stages 1–4). Phenotypes map to HPO:

| Phenotype | HPO term | Stage / frequency |
|---|---|---|
| Acute retroviral syndrome (fever, pharyngitis, rash, lymphadenopathy) | HP:0001945 Fever; HP:0002017 Nausea; HP:0000989 Pruritus/rash | ~50–90% of acute infections, 2–4 wk post-exposure |
| Generalized lymphadenopathy | HP:0002716 Lymphadenopathy | Common, all stages |
| Chronic diarrhea / wasting | HP:0002014 Diarrhea; HP:0004325 Decreased body weight | Advanced |
| Oral candidiasis (thrush) | HP:0009098 Oral candidiasis | CD4 <200–400 |
| Opportunistic pneumonia (*Pneumocystis jirovecii*) | HP:0006532 Recurrent pneumonia / HP:0002090 Pneumonia | AIDS-defining, CD4 <200 |
| CNS involvement — HIV-associated neurocognitive disorder | HP:0100543 Cognitive impairment | Chronic |
| Peripheral neuropathy | HP:0009830 Peripheral neuropathy | Chronic / drug-related |
| Immunodeficiency / recurrent infections | HP:0002721 Immunodeficiency | Progressive |
| Decreased CD4 count (lab) | HP:0005407 Decreased proportion of CD4 T cells | Hallmark laboratory abnormality |
| Thrombocytopenia / anemia | HP:0001873 Thrombocytopenia; HP:0001903 Anemia | Common |
| Kaposi sarcoma | HP:0200041 Kaposi sarcoma | AIDS-defining (HHV-8 co-infection) |

- **Onset:** acute syndrome days–weeks after acquisition; immunodeficiency is chronic and progressive over years (median ~8–10 yr untreated to AIDS).
- **Severity/progression:** variable; "rapid progressors," "typical progressors," and "elite controllers/long-term non-progressors" (<1%) who maintain undetectable viremia without therapy.
- **QoL:** on effective ART, near-normal life expectancy and QoL; stigma, polypharmacy, and accelerated comorbidity (cardiovascular, renal, neurocognitive, bone) remain burdens.

---

## 4. Genetic / Molecular Information

**No host causal gene.** The disease is driven by the viral genome; host genes are modifiers (§2).

**Viral genome (≈9.7 kb):** structural genes *gag* (matrix p17, capsid p24, nucleocapsid p7), *pol* (protease, reverse transcriptase/RNase H, integrase), *env* (gp120/gp41); regulatory *tat*, *rev*; accessory *nef*, *vif*, *vpr*, *vpu* (HIV-1) / *vpx* (HIV-2). Flanked by LTRs driving transcription.

**Host modifier genes (HGNC):** *CCR5* (hgnc:1606), *CCR2*, *CXCR4* (hgnc:2561, the X4-tropism co-receptor), *CCL3L1*, *HLA-B* (hgnc:4932), *APOBEC3G* (hgnc:17357, a restriction factor antagonized by viral Vif), *TRIM5* (hgnc:16277), *SAMHD1* (hgnc:25504, antagonized by Vpx), *BST2*/tetherin (antagonized by Vpu).

**"Variant" framework** here is viral, not germline: drug-resistance mutations (RT M184V, K65R; integrase strand-transfer inhibitor resistance G140S/Q148H, R263K — PMID:36560595, PMID:31280314) and tropism switch (R5→X4) are the clinically relevant "variants." `variant_origin: SOMATIC`/`functional_impact_category` do not apply — this is a viral-driven mechanism with no host lesion (per the CLAUDE.md cancer-origin rule for virally driven mechanisms).

**Epigenetic:** proviral latency is maintained by host epigenetic silencing of the integrated LTR — repressive histone marks (HDAC-mediated), DNA methylation, and transcriptional interference — the target of "shock-and-kill" latency-reversing strategies. GO:0075713 (establishment of integrated proviral latency).

---

## 5. Environmental Information

- **Infectious agent:** HIV-1 (NCBITaxon:11676; groups M [pandemic], N, O, P) and HIV-2 (NCBITaxon:11709). Zoonotic origin: cross-species transmission from SIVcpz (chimpanzee) → HIV-1 and SIVsmm (sooty mangabey) → HIV-2.
- **Co-infections that accelerate disease / are AIDS-defining:** *Mycobacterium tuberculosis* (leading cause of HIV death globally), *Pneumocystis jirovecii*, *Cryptococcus neoformans*, CMV, HHV-8 (Kaposi sarcoma), HPV, HBV/HCV.
- **Behavioral/lifestyle:** injection drug use, condomless sex; smoking and alcohol compound comorbidity on ART.
- **No toxin/radiation etiology.**

---

## 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating exposure → clinical manifestation):**

1. **Mucosal/parenteral exposure** delivers HIV virions, which **bind CD4 (via gp120) on CD4+ T cells, macrophages and dendritic cells**, *leading to* co-receptor engagement.
2. **gp120 binds the chemokine co-receptor CCR5 (R5-tropic, early) or CXCR4 (X4-tropic, late)**, *resulting in* gp41-mediated fusion of viral and cell membranes (GO:0046718 viral entry into host cell).
3. **Fusion delivers the capsid into the cytoplasm**; reverse transcriptase copies viral RNA into dsDNA (GO:0001171 reverse transcription), *leading to* nuclear import of the pre-integration complex.
4. **Integrase inserts the provirus into host chromatin** (GO:0075713), *establishing* a permanent, heritable infection of the cell and — in resting memory CD4+ T cells — a **latent reservoir** that is the principal barrier to cure (PMID:29884404; PMID:27382129).
5. **Productive infection drives viral transcription (Tat-dependent), assembly and budding**, *causing* direct cytopathic death of productively infected activated CD4+ T cells.
6. **Bystander CD4+ depletion** occurs by abortive infection of resting cells triggering **CARD8/caspase-1 inflammasome-mediated pyroptosis** (GO:0070269 pyroptosis), releasing inflammatory cytokines that recruit more susceptible cells — a self-amplifying loop, *leading to* progressive CD4+ T-cell loss (inferred-to-demonstrated; pyroptosis mechanism from Doitsh/Greene, PMID:24356306).
7. **Early, massive depletion of gut-associated lymphoid tissue (GALT) CD4+ Th17 cells** damages the mucosal barrier, *resulting in* **microbial translocation** and systemic LPS-driven **chronic immune activation** — the engine of both progression and non-AIDS comorbidity (PMID:30030793).
8. **Chronic immune activation + progressive CD4+ decline** *lead to* collapse of adaptive immunity, *resulting in* **opportunistic infections and malignancies (AIDS)** once CD4 <200/µL.
9. In parallel, **persistent inflammation on ART** (residual reservoir, co-infections) *drives* accelerated cardiovascular, renal, bone and neurocognitive disease.

- **Upstream:** entry, reverse transcription, integration. **Downstream:** immune activation, CD4 depletion, immunodeficiency.
- **Cell types (CL):** CL:0000624 CD4+ αβ T cell (primary target); CL:0000235 macrophage and CL:0000451 dendritic cell (reservoirs/trans-infection); CL:0000899 Th17 cell (GALT depletion); CL:0000084 T cell generally.
- **Biological processes (GO):** GO:0046718 viral entry; GO:0019068 virion assembly/budding; GO:0075713 proviral latency; GO:0070269 pyroptosis; GO:0002534 cytokine production in inflammatory response; GO:0006955 immune response.
- **Protein dysfunction:** viral accessory proteins disable host restriction — Vif degrades APOBEC3G, Vpu degrades CD4 and antagonizes tetherin/BST2, Nef downregulates CD4 and MHC-I, Vpx (HIV-2) degrades SAMHD1.

---

## 7. Anatomical Structures Affected

- **Primary:** immune system (UBERON:0002405), lymph nodes (UBERON:0000029), gut-associated lymphoid tissue / intestinal mucosa (UBERON:0004185), spleen (UBERON:0002106), thymus (UBERON:0002370), bone marrow (UBERON:0002371).
- **Secondary/complication organs:** central nervous system/brain (UBERON:0000955 — HIV encephalitis, HAND), lung (UBERON:0002048 — opportunistic pneumonia), kidney (UBERON:0002113 — HIV-associated nephropathy), skin (UBERON:0002097 — Kaposi sarcoma, seborrheic dermatitis), cardiovascular system (UBERON:0004535 — accelerated atherosclerosis).
- **Cell level:** CD4+ T lymphocytes, tissue macrophages, follicular dendritic cells, microglia (CNS reservoir).
- **Subcellular (GO CC):** host nucleus (GO:0005634, integration site), plasma membrane (GO:0005886, entry/budding).
- **Lateralization:** systemic, not lateralized.

---

## 8. Temporal Development

- **Onset:** acute phase 1–4 weeks post-exposure (acute retroviral syndrome); "eclipse" and ramp-up viremia peak ~3–4 weeks.
- **Stages:** (1) acute/primary infection with high viremia and transient CD4 drop; (2) clinical latency / chronic infection (viral setpoint, gradual CD4 decline over years); (3) symptomatic HIV; (4) AIDS (CD4 <200 or AIDS-defining illness).
- **Progression rate:** variable — median ~8–10 years untreated to AIDS; rapid progressors (<3 yr); elite controllers/long-term non-progressors (stable for decades).
- **Course:** chronic, lifelong; **not** self-limited; **not** curable with current therapy (latent reservoir persists). ART converts it to a managed chronic condition.
- **Critical window for intervention:** PEP within 72 h of exposure; early ART (acute infection) limits reservoir seeding.

---

## 9. Inheritance and Population

- **Not heritable** — infectious; "inheritance pattern" is not applicable. Vertical transmission ≠ genetic inheritance.
- **Epidemiology (UNAIDS, figures for 2024/2025):**
  - **~41.0 million people living with HIV globally in 2025** (40.8 million in 2024).
  - **~1.2–1.3 million new infections/year** (1.3 M in 2024; 1.2 M in 2025).
  - **~570,000–630,000 AIDS-related deaths/year** (630,000 in 2024; 570,000 in 2025).
  - GBD 2021 provides modeled burden to 2050 (PMID:39608393).
- **Geographic distribution:** sub-Saharan Africa bears ~two-thirds of the global burden (eastern/southern Africa hardest hit); key populations (men who have sex with men, sex workers, people who inject drugs, transgender people, and their partners) account for a large and rising share of new infections elsewhere.
- **Sex ratio:** roughly balanced globally, but adolescent girls and young women in sub-Saharan Africa are disproportionately affected; MSM dominate in many high-income settings.
- **Host-modifier population genetics:** CCR5-Δ32 ~10% carrier frequency in Northern Europeans (founder-like distribution), near-absent in Africa/East Asia.

---

## 10. Diagnostics

- **Laboratory / serology (LOINC):** 4th/5th-generation **HIV Ag/Ab combination immunoassay** (p24 antigen + anti-HIV; LOINC panels, e.g. LOINC:56888-1) → confirmatory **HIV-1/HIV-2 antibody differentiation immunoassay** (CDC algorithm). Window period ~2–4 weeks (shorter with antigen/NAT).
- **Nucleic acid / viral load:** HIV-1 RNA quantitative PCR (LOINC:20447-9 HIV 1 RNA [copies/mL]) — diagnosis in the window period, acute infection, infant diagnosis, and treatment monitoring.
- **Immune monitoring:** CD4+ T-cell count and CD4% (LOINC:24467-3) — staging and opportunistic-infection risk.
- **Resistance testing:** genotypic resistance assay before/at ART initiation and on virologic failure (protease/RT; integrase genotyping).
- **Tropism assay** (before CCR5-antagonist use).
- **Point-of-care / self-testing:** rapid antibody tests and oral-fluid self-tests expand access.
- **Clinical criteria:** CDC surveillance case definition and WHO clinical staging.
- **Differential diagnosis** of acute syndrome: EBV/CMV mononucleosis, acute hepatitis, secondary syphilis, influenza.
- **Screening:** CDC/USPSTF recommend one-time routine screening (ages 13–64) and risk-based repeat testing; universal antenatal screening; infant NAT testing (serology confounded by maternal antibody).

---

## 11. Outcome / Prognosis

- **With effective ART:** near-normal life expectancy; **U=U** — a durably suppressed person does not sexually transmit HIV (PMID:31056293 PARTNER2; PMID:27404185 PARTNER1).
- **Without treatment:** progressive immunodeficiency, AIDS, and death from opportunistic infection/malignancy within ~10 years median.
- **Mortality:** declining globally with ART scale-up; TB remains the leading cause of HIV-related death.
- **Residual morbidity on ART:** accelerated cardiovascular disease, chronic kidney disease, neurocognitive disorder (HAND), non-AIDS malignancies, frailty/bone disease — driven by residual inflammation.
- **Prognostic factors:** baseline and nadir CD4, viral setpoint, time to ART initiation, adherence, HLA background, co-infections (TB, HCV), age.

---

## 12. Treatment

**Combination antiretroviral therapy (ART)** — lifelong suppression; **NCIT:C15986 Pharmacotherapy / NCIT:C15632-adjacent antiretroviral concepts**. Drug classes (with CHEBI/NCIT agent anchors):

| Class | Mechanism | Examples (CHEBI/NCIT) |
|---|---|---|
| **INSTI** (integrase strand-transfer inhibitors) — **first-line backbone** | block integration | dolutegravir (CHEBI:75985), bictegravir, cabotegravir |
| **NRTI** | chain-terminate reverse transcription | tenofovir (TDF/TAF), emtricitabine (CHEBI:63090), lamivudine (CHEBI:63577), abacavir |
| **NNRTI** | allosteric RT inhibition | efavirenz, rilpivirine, doravirine |
| **PI** (protease inhibitors) | block Gag-Pol maturation | darunavir (CHEBI:367163)/ritonavir-boosted |
| **Entry/attachment** | block gp120/CD4/co-receptor/fusion | maraviroc (CCR5 antagonist), enfuvirtide (fusion), fostemsavir (attachment), ibalizumab (CD4 mAb) |
| **Capsid inhibitor** | block capsid function/assembly | **lenacapavir (CHEBI:176859)** — long-acting |

- **First-line (WHO/DHHS):** a dolutegravir (INSTI)–based regimen, typically TDF/3TC/DTG or BIC/FTC/TAF (PMID:30030793; dolutegravir in LMICs PMID:36560595).
- **Long-acting injectables:** cabotegravir + rilpivirine (every 1–2 months) for treatment; **cabotegravir** and **lenacapavir** for prevention.
- **PrEP (pre-exposure prophylaxis):** daily oral TDF/FTC or TAF/FTC; long-acting injectable cabotegravir (every 2 months); **twice-yearly subcutaneous lenacapavir** — the PURPOSE-1 trial in cisgender women reported **zero incident infections** in the lenacapavir arm (Bekker et al., *NEJM* 2024; **PMID:39046157**; NCT04994509), and PURPOSE-2 confirmed high efficacy in a broader population.
- **PEP (post-exposure prophylaxis):** 28-day 3-drug regimen within 72 h.
- **Pharmacogenomics:** **HLA-B*57:01 screening before abacavir** (hypersensitivity; CPIC/FDA PGx); UGT1A1/CYP interactions affect several agents.
- **Curative / advanced (investigational):** CCR5-Δ32/Δ32 allogeneic HSCT has produced documented cures (Berlin, London patients — PMID:30855743); "shock-and-kill" latency reversal, "block-and-lock," broadly neutralizing antibodies (bnAbs), and CCR5 gene editing (CRISPR/zinc-finger) remain experimental (NCT identifiers vary).
- **Supportive:** opportunistic-infection prophylaxis (co-trimoxazole for *Pneumocystis*/CD4<200; TB preventive therapy), vaccination, management of comorbidity.
- **Treatment strategy:** treat-all at diagnosis regardless of CD4; U=U as both clinical goal and prevention.

NCIT anchors: NCIT:C15986 (Pharmacotherapy) as the `treatment_term`, with `therapeutic_agent` CHEBI/NCIT drug terms; NCIT:C15431 (hematopoietic cell transplantation) → `CELL_THERAPY` for the HSCT-cure cases.

---

## 13. Prevention

- **Primary:** condoms; **PrEP** (oral TDF/FTC/TAF, injectable cabotegravir, twice-yearly lenacapavir — PMID:39046157); **voluntary medical male circumcision** (~60% reduction, PMID:17321311); **treatment-as-prevention / U=U** (PMID:31056293); **prevention of mother-to-child transmission (PMTCT)** — maternal ART + infant prophylaxis reduces vertical transmission to <1%; harm reduction (needle/syringe programs, opioid substitution); blood-supply screening.
- **Secondary:** routine HIV testing, early diagnosis and immediate ART; partner notification and index testing.
- **Tertiary:** opportunistic-infection prophylaxis, comorbidity screening, adherence support.
- **Immunization:** **no licensed HIV vaccine** despite major efforts (RV144 showed modest ~31% efficacy, PMID:19843557; subsequent mosaic and mRNA candidates in trials). bnAb passive immunization (AMP trials) showed proof-of-concept but partial coverage.
- **Public health:** 95-95-95 targets (95% diagnosed, 95% on ART, 95% virally suppressed); health education; criminalization/stigma reduction.
- **Counseling:** risk-reduction and adherence counseling; partner testing.

---

## 14. Other Species / Natural Disease

- **Taxonomy / origin:** HIV-1 arose from **SIVcpz** of *Pan troglodytes* (NCBITaxon:9598) and gorillas; HIV-2 from **SIVsmm** of sooty mangabey *Cercocebus atys* (NCBITaxon:9531) — repeated zoonotic cross-species transmissions.
- **Natural SIV infection:** >40 African primate species carry species-specific SIVs; **natural hosts (sooty mangabey, African green monkey) typically do not progress to AIDS** despite high viremia — a key comparative-immunology clue (attenuated immune activation).
- **Animal analogues:** **FIV** (feline immunodeficiency virus) in domestic cats and **BIV/SIV** in other species are comparative lentiviral models of veterinary relevance.
- **Zoonotic potential:** the pandemic itself is the product of primate-to-human spillover; no ongoing animal reservoir sustains human transmission.

---

## 15. Model Organisms

- **Non-human primate (SIV/SHIV):** rhesus macaque (*Macaca mulatta*, NCBITaxon:9544) infected with SIVmac or chimeric SHIV — the **gold-standard model** for pathogenesis, vaccines, PrEP, and cure/reservoir studies. Recapitulates CD4 depletion, GALT damage, immune activation, and AIDS; limitation: SIV ≠ HIV-1, and natural-host species do not model disease.
- **Humanized mice:** BLT (bone-marrow/liver/thymus) and hu-CD34 NSG mice support HIV-1 infection, mucosal transmission, latency, and PrEP/cure testing; limitation: incomplete human immune reconstitution, weak adaptive responses.
- **In vitro / cellular:** primary CD4+ T cells and monocyte-derived macrophages; cell lines (Jurkat, MT-4, TZM-bl reporter line for neutralization/entry); **latency models** (J-Lat, primary-cell latency models) for reservoir and shock-and-kill work.
- **Organoids / iPSC:** gut and lymphoid organoids for mucosal transmission and reservoir studies (emerging).
- **Resources:** NIH HIV Reagent Program; Cellosaurus (TZM-bl, J-Lat); Los Alamos HIV Sequence Database (viral variation, resistance).
- **Model→mechanism linking (dismech `AnimalModel.modeled_mechanisms`):** SIV/macaque → `RECAPITULATES` CD4+ depletion and GALT immune activation nodes, `fidelity: HIGH`; humanized mouse → `PARTIALLY_RECAPITULATES` latent reservoir, `fidelity: MODERATE`, with species/immune-reconstitution `limitations`.

---

## Key Citations (PMID)

- **30030793** — Deeks SG et al. *HIV infection.* Nat Rev Dis Primers 2015 (master mechanistic review).
- **29884404** — Siliciano RF. The latent reservoir for HIV-1.
- **27382129** — HIV persistence on ART and barriers to a cure.
- **24356306** — Doitsh/Greene. CD4 T-cell death by pyroptosis in lymphoid tissue.
- **39608393** — GBD 2021 HIV/AIDS burden and forecasts to 2050.
- **8898191** — Samson et al. CCR5-Δ32 and resistance to HIV infection.
- **30855743** — Gupta et al. London patient (CCR5-Δ32/Δ32 HSCT remission).
- **17321311** — Auvert et al. Male circumcision randomized trial.
- **31056293** — Rodger et al. PARTNER2 (U=U).
- **39046157** — Bekker et al. Twice-yearly lenacapavir for PrEP (PURPOSE-1), NEJM 2024.
- **36560595 / 31280314 / 27188527** — dolutegravir use and INSTI resistance.
- **19843557** — Rerks-Ngarm et al. RV144 vaccine trial.

**Sources (web):** [UNAIDS Global HIV Fact Sheet](https://www.unaids.org/en/resources/fact-sheet); [PURPOSE-1, PMID:39046157 (PubMed)](https://pubmed.ncbi.nlm.nih.gov/39046157/).

---

### Note for KB curation
The existing `kb/disorders/HIV_Infectious_Disease.yaml` (681 lines) already cites PMIDs 27188527, 27382129, 29884404, 30030793, 31280314, 36560595, 39608393. The highest-value *additions* this report supports are: the pyroptosis/GALT immune-activation causal nodes (PMID:24356306), CCR5-Δ32 host modifier and HSCT-cure cases (PMID:8898191, 30855743), prevention evidence (PMID:17321311, 31056293, 39046157), and the vaccine gap (PMID:19843557). Per the infectious-disease granularity ladder (design decisions §3e), HIV infectious disease is correctly the named clinical entity with NCBITaxon-bound `infectious_agent` (11676/11709) and SEXUAL/PARENTERAL/VERTICAL `transmission` routes; AIDS remains a separate advanced-stage entry. All PMIDs above should be fetched via `just fetch-reference PMID:…` and each claim backed by an exact-quote snippet before curation.

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 59 |
| Resolved | 54 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 3 |
| Terms whose name was checked | 18 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0075713` (4 mentions) - the report calls it "establishment of integrated proviral latency", "Integrase inserts the provirus into host chromatin"; GO calls it **establishment of integrated proviral latency**
- `UBERON:0002048` (1 mention) - the report calls it "opportunistic pneumonia"; UBERON calls it **lung**
- `UBERON:0002113` (1 mention) - the report calls it "HIV-associated nephropathy"; UBERON calls it **kidney**
- `UBERON:0002097` (1 mention) - the report calls it "Kaposi sarcoma, seborrheic dermatitis"; UBERON calls it **skin of body**
- `UBERON:0004535` (1 mention) - the report calls it "accelerated atherosclerosis"; UBERON calls it **cardiovascular system**
- `CHEBI:75985` (1 mention) - the report calls it "dolutegravir"; CHEBI calls it **CHEBI_75985**
- `CHEBI:176859` (1 mention) - the report calls it "lenacapavir"; CHEBI calls it **PA(P-20:0/22:4(7Z,10Z,13Z,16Z))**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0005407` (obsolete Decreased proportion of CD4-positive helper T cells) (1 mention) - replaced by `HP:0032218`
- `CHEBI:75985` (CHEBI_75985) (1 mention) - replaced by `CHEBI:5516`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCBITaxon:11676` (3 mentions) - the report calls it "HIV-1"; NCBITaxon calls it **Human immunodeficiency virus 1**, and lists "HIV-1" among its other names
- `NCBITaxon:11709` (3 mentions) - the report calls it "HIV-2"; NCBITaxon calls it **Human immunodeficiency virus 2**, and lists "HIV-2" among its other names
- `GO:0046718` (3 mentions) - the report calls it "viral entry into host cell"; GO calls it **symbiont entry into host cell**, and lists "viral entry into host cell" among its other names
- `CL:0000624` (2 mentions) - the report calls it "CD4+ αβ T cell"; CL calls it **CD4-positive, alpha-beta T cell**
- `UBERON:0002405` (1 mention) - the report calls it "Primary:** immune system"; UBERON calls it **immune system**
- `UBERON:0000955` (1 mention) - the report calls it "HIV encephalitis, HAND"; UBERON calls it **brain**, and lists "encephalon" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0075713` - called "establishment of integrated proviral latency", "Integrase inserts the provirus into host chromatin"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `LOINC`.