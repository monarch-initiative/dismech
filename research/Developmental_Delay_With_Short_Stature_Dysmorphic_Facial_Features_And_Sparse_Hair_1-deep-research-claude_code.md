---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5
cached: false
start_time: '2026-10-27T18:33:36.768658'
end_time: '2026-10-27T18:55:03.078638'
duration_seconds: 1286.31
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Developmental Delay With Short Stature, Dysmorphic Facial Features,
    And Sparse Hair 1
  mondo_id: MONDO:0800438
  category: Mendelian
  causal_genes: DPH1
  omim_id: not recorded
  synonyms: DEDSSH1; diphthamide deficiency syndrome 1; diphtamide deficiency syndrome;
    developmental delay-short stature-dysmorphic features-sparse hair syndrome
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
  - claude-opus-5
  web_search_requests: 6
  num_turns: 82
  total_cost_usd: 9.4196358
  session_id: 57da5f5d-0435-504f-8aaa-d5950c1ad10f
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 17
reference_validation:
  total_references: 34
  verified: 34
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 34
  on_topic: 20
  validator_version: 0.4.0
term_validation:
  total_terms: 74
  verified: 64
  not_found: 0
  obsolete: 0
  unverifiable: 10
  confabulation_rate: 0.0
  labels_checked: 37
  labels_matching: 28
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0800438
    reported_labels:
    - gard_rare`, `ordo_disorder`, `ordo_malformation_syndrome`, `orphanet_rare`,
      `rare
    ontology_label: developmental delay with short stature, dysmorphic facial features,
      and sparse hair 1
  - term_id: CHEBI:15414
    reported_labels:
    - Cofactor
    ontology_label: S-adenosyl-L-methionine
  - term_id: GO:0008285
    reported_labels:
    - p21 effect
    ontology_label: negative regulation of cell population proliferation
  - term_id: GO:0061308
    reported_labels:
    - Cardiac NC limb (inferred)
    ontology_label: cardiac neural crest cell development involved in heart development
  - term_id: GO:0047286
    reported_labels:
    - Diphtheria-toxin reaction (assay basis)
    ontology_label: NAD+-diphthamide ADP-ribosyltransferase activity
  - term_id: GO:0051539
    reported_labels:
    - Fe-S cofactor
    ontology_label: 4 iron, 4 sulfur cluster binding
  - term_id: GO:0072331
    reported_labels:
    - p53 limb
    ontology_label: signal transduction by p53 class mediator
  labels_variant: 2
  unresolvable_prefixes:
  - OMIMPS
  - OMIM
  - ORPHA
  - NCBIGene
  - MGI
  - EXT_ID
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Developmental Delay With Short Stature, Dysmorphic Facial Features, And Sparse Hair 1
- **MONDO ID:** MONDO:0800438 (if available)
- **Causal gene(s):** DPH1
- **OMIM:** not recorded
- **Synonyms:** DEDSSH1; diphthamide deficiency syndrome 1; diphtamide deficiency syndrome; developmental delay-short stature-dysmorphic features-sparse hair syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Developmental Delay With Short Stature, Dysmorphic Facial Features, And Sparse Hair 1** covering all of the
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

# Developmental Delay With Short Stature, Dysmorphic Facial Features, And Sparse Hair 1 (DEDSSH1 / DPH1 syndrome / Loucks–Innes syndrome)

**Causal gene: *DPH1*** (diphthamide biosynthesis 1; HGNC:3003; 17p13.3; NCBI Gene 1801; Ensembl ENSG00000108963; UniProt Q9BZG8; previous symbols *DPH2L*, *DPH2L1*; alias *OVCA1*). Verified from the HGNC REST record for *DPH1* (rest.genenames.org, retrieved 2026-10-27).

**Report date:** 2026-10-27
**Scope:** autosomal recessive, ultra-rare Mendelian multisystem neurodevelopmental disorder caused by biallelic loss of DPH1 function; the first step of diphthamide biosynthesis on eukaryotic elongation factor 2 (eEF2). This is a **germline** developmental disorder and is kept strictly separate below from the **somatic** tumour-suppressor literature on *OVCA1*/*DPH1*.

---

## 0. Two things to read before anything else

### 0a. There are two co-circulating *DPH1* numbering systems, differing by 5 residues / 15 nucleotides

Every published patient variant is reported in the literature with a numbering **5 residues higher** than the one ClinVar now uses on `NM_001383.6`. This is a live curation hazard: the same allele appears in the literature and in ClinVar under two different names, and neither is "wrong".

| Literature name (NM_001383.3/.4) | Current ClinVar name (NM_001383.6) | ClinVar VCV | ClinVar germline classification |
|---|---|---|---|
| c.17T>A, p.Met6Lys | c.2T>A, p.Met1Lys | VCV000218949 | Likely pathogenic (1 submitter) |
| c.335A>G, p.Tyr112Cys | c.320A>G, p.Tyr107Cys | VCV000997988 | Pathogenic (1 submitter) |
| c.374T>C, p.Leu125Pro | c.359T>C, p.Leu120Pro | VCV000521028 | Conflicting classifications |
| c.701T>C, p.Leu234Pro | c.686T>C, p.Leu229Pro | VCV000183359 | Pathogenic/Likely pathogenic (6 SCVs, no conflicts) |

*Source: NCBI E-utilities `esummary` against ClinVar for VCV 218949, 997988, 521028, 183359, retrieved 2026-10-27. ClinVar's `protein_change` field carries both spellings (e.g. "M6K, M1K"; "L234P, L223P, L94P, L229P").*

The underlying biology of the discrepancy is stated by Urreizti et al.: human Met6 is the initiation codon in most other mammals, and **it is genuinely uncertain whether Met1 or Met6 is the initiator**. From the paper (read directly from the manuscript PDF): *"as stated in Uniprot (Q9BZG8; accessed June 2018) it is uncertain whether Met1 or Met6 is the initiator"*, and *"A variety of bioinformatic tools predict both Met1 and Met6 as putative initiation codons, with Met1 having the highest scores."* **Recommendation for a knowledge-base entry: record both spellings, and always carry the transcript version with the cDNA coordinate.**

### 0b. Germline syndrome vs. somatic tumour suppressor — do not merge these

*DPH1* was first characterised as *OVCA1*, an ovarian/breast cancer candidate tumour suppressor, and `Ovca1^+/−` mice **spontaneously develop cancer** (Chen & Behringer, Genes Dev 2004; PMID:14744934 — verbatim per automated extraction: *"Ovca1 heterozygotes spontaneously develop cancer."*). **No cancer predisposition has been reported in DEDSSH1 patients or in their obligate heterozygous parents**, and no study has looked. This is a genuine, unresolved gap rather than a negative finding, and it should be recorded as such (see §11 and §16). The somatic/oncology literature on DPH1 (hepatocellular carcinogenesis, immunotoxin resistance, CD123-targeted therapy resistance) belongs to a different entry.

---

## 1. Disease Information

### 1.1 Overview

DEDSSH1 is an autosomal recessive, congenital-onset multisystem disorder caused by biallelic variants in *DPH1*. Its cardinal tetrad — present in essentially every reported patient — is **(i) developmental delay / intellectual disability, (ii) an unusual skull shape (most often a broad or prominent forehead, scaphocephaly or trigonocephaly, with or without craniosynostosis), (iii) sparse scalp hair, eyebrows and eyelashes, and (iv) dysmorphic facial features**, with **short stature** in the large majority. Central nervous system malformations (cerebellar vermis hypoplasia / Dandy–Walker spectrum, agenesis of the corpus callosum, ventriculomegaly), congenital heart defects, abnormal toenails, dental anomalies, renal anomalies and genital anomalies occur in substantial minorities.

The disorder's history is a history of misdiagnosis: the index Saudi family was published as **Ritscher–Schinzel (3C) syndrome** (Seidahmed et al., Am J Med Genet A 2011;155A:1393–1397); the North American cohort was thought to have **Sensenbrenner syndrome / cranioectodermal dysplasia** (Loucks et al. 2015 — verbatim per automated extraction: *"The phenotype was considered most consistent with Sensenbrenner syndrome (cranioectodermal dysplasia; MIM# 218330)"*); Urreizti's Patient 1 was *"initially clinically diagnosed with Opitz C syndrome"* (read directly from the manuscript PDF); and a sibling pair carried a clinical diagnosis of **Fine–Lubinsky syndrome** for years (Waskow et al. 2025, PMID:39166428). A 2026 series re-examining patients clinically diagnosed with **Noonan syndrome** also surfaced non-RASopathy diphthamide-pathway diagnoses in the broader literature.

Urreizti et al. proposed renaming the condition **DPH1 syndrome**; Hawer et al. proposed **diphthamide-deficiency syndrome** as the umbrella for the *DPH1*/*DPH2*/*DPH5* group; the eponym **Loucks–Innes syndrome** is in current use in case reports.

### 1.2 Identifiers (all verified 2026-10-27)

| Resource | Identifier | Source of verification |
|---|---|---|
| MONDO (this entry) | **MONDO:0800438** — *developmental delay with short stature, dysmorphic facial features, and sparse hair 1* | EBI OLS4 MONDO term record |
| MONDO (grouping / phenotypic series) | **MONDO:0031632** — *developmental delay with short stature, dysmorphic facial features, and sparse hair* (xref OMIMPS:616901, `has_children: true`) | EBI OLS4 |
| OMIM (phenotype) | **#616901** | MONDO xref; HPO annotation API (`OMIM:616901`) |
| OMIM (gene) | ***603527*** (DPH1) | HGNC record; Urreizti et al. |
| Orphanet | **ORPHA:459061** | MONDO xref (exact match) |
| Disease Ontology | **DOID:0070477** (*diphthamide deficiency syndrome 1*) | MONDO xref; MGI disease page |
| GARD | 0017814 | MONDO xref |
| MedGen / UMLS | MedGen 934768 / UMLS C4310801 are attached to the **grouping** term MONDO:0031632, not to the DPH1-specific entry | EBI OLS4 |
| Gene | HGNC:3003; NCBIGene:1801; Ensembl ENSG00000108963; UniProt Q9BZG8; RefSeq NM_001383 | genenames.org REST |
| ICD-10 / ICD-11 / MeSH | **No specific code identified.** No dedicated ICD-10-CM, ICD-11 or MeSH term was found for this entity; it would be coded to a generic congenital-malformation-syndrome rubric. Recorded as a gap, not as an absence proven by exhaustive search. | — |

**MONDO subsets** on MONDO:0800438: `gard_rare`, `ordo_disorder`, `ordo_malformation_syndrome`, `orphanet_rare`, `rare`.

### 1.3 Synonyms

DEDSSH1 · DPH1 syndrome · Loucks–Innes syndrome · diphthamide deficiency syndrome 1 · diphtamide deficiency syndrome (the misspelling is carried as a MONDO synonym) · developmental delay–short stature–dysmorphic features–sparse hair syndrome.

### 1.4 Nature of the evidence base

**Entirely case reports and small family series — there is no registry, no natural-history study, no EHR cohort, and no clinical-trial data.** Approximately 17–20 patients have been published. Two independent 2021 and 2025 reports state the count explicitly (verbatim per automated extraction): Cheng et al. — *"Less than 20 patients were reported from different ethnicities."*; Al-Ajlouni et al. — *"fewer than 20 reported cases of Loucks-Innes syndrome in the literature."* All disease-level aggregation (OMIM, Orphanet, HPO) is derived from those same primary reports; HPO's frequency annotations for OMIM:616901 derive from **a single publication**, PMID:26220823 (see §3.1).

---

## 2. Etiology

### 2.1 Primary cause

**Biallelic (homozygous or compound heterozygous) loss-of-function or hypomorphic variants in *DPH1***, which encodes the catalytic subunit of the 2-(3-amino-3-carboxypropyl)histidine synthase that performs step 1 of diphthamide biosynthesis on eEF2 (EC 2.5.1.108). From Urreizti et al., read directly from the manuscript PDF:

> *"DPH1 (diphtamide biosynthesis 1, OMIM \*603527) encodes the enzyme [2-(3-amino-3-carboxypropyl) histidine synthase subunit 1; EC 2.5.1.108], which is required for the first step in the synthesis of diphthamide and, therefore, essential for generating the diphthamide modification of eukaryotic EF2 (eEF2)."*

There is **no environmental, infectious or toxic contribution** to disease causation. The disorder is fully genetically determined.

### 2.2 Genetic risk factors

- **Consanguinity is the dominant risk factor.** Reported families are consanguineous or from genetic isolates: a consanguineous Saudi family (Alazami et al.), a North American genetic isolate with second-cousin parents (Loucks et al.), a Pakistani consanguineous family (Riazuddin et al., Mol Psychiatry 2017;22:1604–1614), a consanguineous Iranian family (Sekiguchi et al.), first-cousin Yemeni Bedouin parents (Urreizti et al.; Al-Ajlouni et al.), and second-cousin Yemeni parents (Al-Ajlouni et al.). Urreizti's Patient 3 had *"223 Mb of absence of heterozygosity (AOH) (~7.8% of autosomal genome), consistent with the history of consanguinity"* (read directly from the PDF).
- **A founder allele exists in one North American isolate.** Loucks et al. found c.17T>A in 5 of 1,098 control chromosomes from that population and never homozygous (verbatim per automated extraction: *"it was seen in 5 of 1098 chromosomes"*, *"giving a minor allele frequency of 0.46% in the population"*, *"This is consistent with the c.17T>A variant being a founder mutation within this population."*). **The isolate is not named in the paper.**
- **Heterozygous carriers are unaffected.** Ütkür et al. 2023 (PMID:37675463, verbatim per automated extraction): *"with their heterozygous (DPH+/−) parents showing no phenotype"* and *"Because one functional allele for each enzyme is sufficient for activity"*.
- **Population constraint is consistent with a recessive gene.** gnomAD constraint for *DPH1* (ENSG00000108963), retrieved from the gnomAD API 2026-10-27: **pLI = 8.84 × 10⁻²²**, **o/e LoF = 1.067 (90% CI 0.866–1.325)**, **LOEUF = 1.325**, LoF z = −0.42, missense z = −0.76. Heterozygous LoF is fully tolerated in the population — exactly what is expected, and an argument against any strong dominant effect.

### 2.3 Protective factors

**None known.** No protective allele, modifier, dietary or lifestyle factor has been identified. One mechanistic observation is adjacent but is *not* a protective factor in patients: an eEF2 Gly717Arg knock-in in mouse **partially compensates** for diphthamide loss (Liu et al., PNAS 2012, PMID:22869748 — verbatim per automated extraction: *"the Gly(717)-to-Arg mutation partially compensates the eEF2 functional loss"*), by adding a +1 charge that offsets the charge lost with diphthamide. No human eEF2 modifier has been described.

### 2.4 Gene–environment interactions

**None described for the human disease.** The one biologically real G×E axis is pharmacological and inverse: cells lacking diphthamide are **resistant** to diphtheria toxin and *Pseudomonas* exotoxin A, and therefore to ADP-ribosylating immunotoxins (Stahl et al., PNAS 2015, PMID:26261303 — verbatim per automated extraction: *"Loss of diphthamide prevented ADP ribosylation of eEF2, rendered cells resistant to PE and DT"*). Whether DEDSSH1 patients are clinically diphtheria-toxin resistant has never been tested and should **not** be asserted. In plants, diphthamide synthesis is stress-sensitive (Zhang et al., Nat Commun 2022, PMID:35817801) — no human counterpart is established.

---

## 3. Phenotypes

### 3.1 HPO annotations currently attached to OMIM:616901

Retrieved from the HPO annotation API (`ontology.jax.org/api/network/annotation/OMIM:616901`) on 2026-10-27. **Every annotation cites PMID:26220823 (Loucks et al. 2015) and the denominators are that paper's 8 patients.** Onset data: none recorded except `HP:0003577 Congenital onset 8/8`. Inheritance: `HP:0000007 Autosomal recessive inheritance`.

| HPO ID | Label | Frequency (n/8) | System |
|---|---|---|---|
| HP:0001263 | Global developmental delay | 8/8 | Nervous system |
| HP:0001249 | Intellectual disability | 8/8 | Nervous system |
| HP:0003577 | Congenital onset | 8/8 | Clinical course |
| HP:0002209 | Sparse scalp hair | 8/8 | Hair |
| HP:0045075 | Sparse eyebrow | 8/8 | Hair |
| HP:0000653 | Sparse eyelashes | 8/8 | Hair |
| HP:0030799 | Scaphocephaly | 8/8 | Head |
| HP:0011220 | Prominent forehead | 8/8 | Head |
| HP:0000316 | Hypertelorism | 8/8 | Eye |
| HP:0000286 | Epicanthus | 8/8 | Head/neck |
| HP:0000494 | Downslanted palpebral fissures | 8/8 | Head/neck |
| HP:0005280 | Depressed nasal bridge | 8/8 | Head/neck |
| HP:0000347 | Micrognathia | 8/8 | Head/neck |
| HP:0000369 | Low-set ears | 8/8 | Ear |
| HP:0004322 | Short stature | frequency not given | Growth |
| HP:0000243 | Trigonocephaly | frequency not given | Head |
| HP:0001320 | Cerebellar vermis hypoplasia | 4/6 | Nervous system |
| HP:0001305 | Dandy-Walker malformation | 4/6 | Head/neck |
| HP:0001629 | Ventricular septal defect | 3/8 | Cardiovascular |
| HP:0001800 | Hypoplastic toenails | 3/8 | Nails |
| HP:0003819 | Death in childhood | 2/8 | Clinical course |
| HP:0001522 | Death in infancy | 1/8 | Clinical course |
| HP:0004442 | Sagittal craniosynostosis | 1/8 | Head |
| HP:0000695 | Natal tooth | 1/8 | Teeth |
| HP:0001763 | Pes planus | 1/8 | Limbs |
| HP:0000093 | Proteinuria | 1/8 | Laboratory |
| HP:0000790 | Hematuria | 1/8 | Laboratory |
| HP:0001970 | Tubulointerstitial nephritis | 1/8 | Genitourinary |

**Curation note:** this annotation set is *stale relative to the literature*. It predates Sekiguchi 2018 (agenesis of the corpus callosum, cleft palate), Nakajima 2018 (airway obstruction, external genital anomalies), Urreizti 2020 (tetralogy of Fallot, dilated cardiomyopathy, keratoconus, hypothyroidism, microcephaly, seizures), Cheng 2021 (growth hormone deficiency), and Waskow 2025 (sensorineural hearing loss with remission; cardiomyopathy). A dismech entry should not be limited to the HPO-annotated set.

### 3.2 Aggregate frequencies across the published cohort (n ≈ 17)

Reproduced from **Table 1 of Hawer et al. 2020 (PMID:32576952)**, whose *DPH1* column tabulates the Urreizti et al. cohort. Denominators vary because not every patient was assessed for every feature — carry the denominator, not a percentage alone.

| Feature | DPH1 patients |
|---|---|
| Developmental delay / intellectual disability | **17/17** |
| Dysmorphic features | **17/17** |
| Sparse scalp hair | **15/15** |
| Unusual skull shape | **15/15** |
| Short stature | **14/15** |
| Hand/foot anomalies | **12/12** |
| CNS malformations | **9/11** |
| Dental abnormalities | **7/10** |
| Heart malformation | **7/15** |
| Abnormal toenails | **6/8** |
| Abnormal head circumference | **6/9** |
| Epilepsy | **5/7** |
| Genitalia anomalies | **5/9** |

Urreizti's own Discussion (read directly from the PDF) is consistent and adds severity context:

> *"To date, a total of 16 patients have been published with homozygous or compound heterozygous variants in DPH1 ... characterized mainly by variable developmental delay or intellectual disability, unusual skull shape with or without craniosynostosis (most often with a broad forehead), sparse hair, and a variety of dysmorphic features (Table 1). Most patients also have short stature. Central nervous system malformations are present in nearly all the assessed patients with the exception of two cases."*

(The 16-vs-17 discrepancy between Urreizti's text and Hawer's table is in the sources; do not silently reconcile it.)

### 3.3 Phenotype detail by domain, with ontology suggestions

Ontology CURIEs below were **looked up at the time of writing** (HPO annotation API; EBI OLS4 for GO/CL/UBERON/CHEBI/NCIT). Terms marked ⚠ were not individually resolved and are **leads requiring lookup before binding**.

**Neurodevelopmental (near-100%; congenital onset; static with superimposed complications)**
- Global developmental delay `HP:0001263`; intellectual disability `HP:0001249`, severity **variable by genotype** — "mild or moderate" in the p.Met6Lys/p.Met1Lys founder cohort (Urreizti, direct read: *"In the four cases bearing the p.(Met6Lys) variant, the intellectual disability was often referred to as mild or moderate ... with no mention to heart or CNS malformations"*), through to *"profound intellectual disability"* with non-ambulatory, non-verbal, no sphincter control in the p.Leu125Pro siblings (direct read).
- Hypotonia (congenital, central) — Urreizti Family 1 both sibs, Family 2 both sibs ("significant hypotonia and gross motor delay"); later cortical spasticity with brisk reflexes and clonus in Patient 1 (direct read). ⚠ HP terms for hypotonia/spasticity not individually resolved here.
- Seizures: neonatal seizures (Urreizti P1; Al-Ajlouni case, seizures to age 1), febrile seizure (Urreizti P3), multiple seizures with abnormal EEG (Urreizti P4), generalised/absence seizures (Loucks P1); epilepsy 5/7 in the aggregate table.
- Brain malformations: cerebellar vermis hypoplasia `HP:0001320` / Dandy–Walker malformation `HP:0001305` (4/6, Loucks); **agenesis of the corpus callosum** (Sekiguchi siblings; Urreizti P2); ventricular dilatation, cavum septi pellucidi, leukomalacia, leukodystrophy (Urreizti P1/P2, direct read); congenital hydrocephalus requiring VP shunt (Al-Ajlouni).

**Growth (short stature 14/15)**
- Short stature `HP:0004322`; severity spans −2.4 SD (Urreizti P3 at 20 months) to **−8.4 SD height with −13.6 SD weight** (Urreizti P1 at 21 years, direct read). Failure to thrive from early childhood; tube feeding in the most severe.
- **Growth hormone deficiency** is documented and treatable — Cheng et al. 2021 (verbatim per automated extraction): *"Our patient was the first reported patient with documented growth hormone deficiency."* Shi et al. 2024 report a DEDSSH1 proband with GHD in whom GH replacement restored growth. **This is the single most actionable phenotype in the disorder.**

**Craniofacial / skull**
- Scaphocephaly `HP:0030799`, trigonocephaly `HP:0000243`, dolichocephaly, brachycephaly (Sekiguchi), prominent/broad forehead `HP:0011220`, metopic and sagittal suture prominence, **craniosynostosis in a minority** (sagittal `HP:0004442`, 1/8 Loucks; metopic synostosis in Urreizti P2).
- Hypertelorism `HP:0000316` / telecanthus, epicanthus `HP:0000286`, downslanted palpebral fissures `HP:0000494`, depressed nasal bridge `HP:0005280`, short nose, micrognathia `HP:0000347`, low-set/protruding/overfolded ears `HP:0000369`, small mouth, high-arched palate, **cleft palate** (Sekiguchi siblings).
- Head size is **bidirectional** — Urreizti (direct read): *"Surprisingly, both micro- and macrocephaly have been observed previously"*. Severe microcephaly (OFC −6.1 SD, −6.2 SD) in Family 1; macrocephaly/frontal bossing in the Yemeni family and the Al-Ajlouni case. Hawer 2020 (verbatim per automated extraction): *"Both macrocephaly and microcephaly have been described in individuals with variants in DPH1"*.

**Ectodermal (the discriminating feature)**
- Sparse, thin, coarse scalp hair `HP:0002209`; sparse eyebrows `HP:0045075`; sparse or **absent** eyelashes `HP:0000653`; high anterior hairline; absent axillary and pubic hair in the adult male (Urreizti P1, direct read).
- Hypoplastic/dysplastic toenails `HP:0001800` (6/8).
- Dental: small peg-shaped teeth, multiple missing teeth, natal teeth `HP:0000695`, notched incisor (in the *DPH2* sib).
- **Age-dependence is explicit** — Cheng et al. (verbatim per automated extraction): *"Dysplastic toenails and dental abnormalities are age-dependent characteristics of DPH1 syndrome."* A young infant lacking these does not exclude the diagnosis.

**Cardiac (7/15) — the main late-morbidity axis**
- Ventricular septal defect `HP:0001629` (3/8 Loucks); **tetralogy of Fallot** diagnosed on fetal echo at 20 weeks, repaired at 4 months (Urreizti P3, direct read); PDA.
- **Acquired cardiomyopathy**: Urreizti P1 had *"an episode of congestive heart failure and his echocardiogram showed dilated cardiomyopathy"* at 18 years (direct read); Urreizti P4 at 5 years had *"a moderately dilated left ventricle with eccentric left ventricular hypertrophy"* (direct read). Waskow et al. 2025 (verbatim per automated extraction): *"individuals with DEDSSH1 should be monitored for the development of cardiomyopathy."*
- Aortic root and ascending aorta dilatation with mild aortic insufficiency, on losartan and atenolol (Al-Ajlouni case).

**Renal / genitourinary (≈4/8 in Loucks; 5/9 genital anomalies)**
- Renal anomalies in the Saudi cohort; horseshoe kidney (Urreizti P1); focal interstitial nephritis with recurrent haematuria/proteinuria (Loucks P1); normal renal imaging in the Yemeni sibs. **Absent renal findings** in the Iranian siblings (Sekiguchi).
- Micropenis, hypoplastic scrotum, undescended testes, hypospadias, hydrocele; *"the external genital anomaly was newly recognized in our case"* (Nakajima, verbatim per automated extraction).

**Hearing and vision**
- Mild hearing loss (Loucks P2); **severe mixed conductive and sensorineural hearing loss** interfering with schooling (Al-Ajlouni). Waskow et al. (verbatim per automated extraction): *"hearing loss associated with DEDSSH1 may remit over time"* — a clinically important and counter-intuitive claim from a single sibling pair; treat as provisional.
- Keratoconus and ocular proptosis (Urreizti P1); high myopia without retinal degeneration (Loucks P3); **no retinal or hepatic disease**, which is what separates this from Sensenbrenner syndrome (Loucks, verbatim per automated extraction: *"Our study patients also did not have significant retinal or hepatic disease"*).

**Airway / respiratory**
- Obstructive sleep apnoea (Urreizti P3 and P4, both; Loucks P4), neonatal respiratory support, airway obstruction as a presenting feature (Nakajima), recurrent respiratory infections — one patient died after *"a severe respiratory tract infection"* at 20 years (Urreizti P2, direct read).

**Skeletal / limb**
- Brachydactyly, short tapered digits, clinodactyly, single transverse palmar crease, cutaneous syndactyly, pes planus `HP:0001763`, hallux valgus with overriding toes, pectus excavatum, congenital vertical talus, bowed legs, fused vertebrae, low bone mineral density (−5 SD), advanced bone age (Urreizti P2, bone age 9 years at chronological 7 years — direct read). Hand/foot anomalies 12/12.

**Endocrine / other**
- Hypothyroidism requiring treatment (Urreizti P1, direct read); growth hormone deficiency (Cheng; Shi).

### 3.4 Quality-of-life impact

**No disease-specific or generic QoL instrument (EQ-5D, SF-36, PROMIS, PedsQL) has ever been applied to this disorder.** The functional burden is inferable from case descriptions only: non-ambulatory wheelchair dependence with no speech and no sphincter control at the severe end; lifelong tube feeding; special schooling with twice-weekly PT/OT/speech; at the mild end, independent walking with grade-2 academic attainment at age 12 and partial independence in adulthood. Any QoL statement beyond this would be fabrication.

---

## 4. Genetic / Molecular Information

### 4.1 Published patient variant roster

Variants are given in the **literature numbering** used by each paper, with the current ClinVar/NM_001383.6 spelling where verified (see §0a).

| Variant (literature) | Zygosity | Origin / family | Patients | First report | Functional result (ADPR assay) |
|---|---|---|---|---|---|
| c.701T>C, p.Leu234Pro (= c.686T>C p.Leu229Pro) | hom | Saudi, consanguineous (previously published as 3C syndrome) | 4 | Alazami et al., Cell Rep 2015;10:148–161 (PMID:25558065) | **Strongly reduced** |
| c.17T>A, p.Met6Lys (= c.2T>A p.Met1Lys) | hom | North American genetic isolate (founder), second-cousin parents | 4 | Loucks et al., Hum Mutat 2015;36:1015–1019 (PMID:26220823) | **Wild-type-like in vitro** (see note) |
| p.Pro382Ser | hom | Pakistani consanguineous | 2 | Riazuddin et al., Mol Psychiatry 2017;22:1604–1614 | **Wild-type-like in vitro** |
| c.289delG p.Glu97Lysfs\*8 + c.491T>C p.Leu164Pro | compound het | Japanese, non-consanguineous | 1 | Nakajima et al., J Hum Genet 2018;63:529–532 (PMID:29362492) | Leu164Pro **reduced**; frameshift predicted NMD |
| c.1227delG, p.Ala411Argfs\*91 | hom | Iranian consanguineous | 2 | Sekiguchi et al., J Hum Genet 2018;63:487–491 (PMID:29410513) | **Reduced** (escapes NMD — last exon) |
| c.374T>C, p.Leu125Pro (= c.359T>C p.Leu120Pro) | hom | Maltese | 2 | Urreizti et al., Eur J Hum Genet 2020;28:64–75 (PMID:30877278) | **Reduced** |
| c.335A>G, p.Tyr112Cys (= c.320A>G p.Tyr107Cys) | hom | Yemeni Bedouin, first-cousin parents | 2 | Urreizti et al. 2020 | **Reduced** |
| c.335A>G | hom | Yemeni, second-cousin parents | 1 | Al-Ajlouni et al., J Med Case Rep 2025 (PMID:41444928) | not tested |
| **c.749+39G>A (intronic)**, NM_001383.6 | hom | sibling pair, prior clinical dx Fine–Lubinsky | 2 | Waskow et al., Am J Med Genet A 2025;197:e63845 (PMID:39166428) | RNA-seq: markedly reduced transcript |
| p.Ala114Thr (one of two alleles) | compound het (second allele not stated in the source I read) | the only reported **adult** patient | 1 | assigned by Ütkür et al. 2023 (PMID:37675463) | **Reduced** |
| p.Glu242Gln + p.Gln46\* (human) | compound het, inferred | proband with GH deficiency | 1 | Shi et al., Nat Commun 2024 (PMID:38671004) | modelled in knock-in mice |

**The p.Met6Lys exception matters and is the clearest genotype–phenotype lesson in the disorder.** It behaves like wild type in the heterologous ADPR assay yet segregates with a real (milder) phenotype. Urreizti's explanation (read directly from the PDF): *"In humans, Met6 could be acting as an alternative initiation codon and its loss could reduce overall DPH1 protein levels in vivo, which may not be reflected in our functional assay that uses an exogenous expression construct."* A negative in vitro assay therefore does **not** exclude pathogenicity for a start-codon-region allele.

### 4.2 Variant classes and functional consequence

- **Class:** missense (majority), frameshift (2), and one deep-intronic splice-affecting variant. **No whole-gene deletions, no structural variants, and no reported de novo dominant cases.**
- **Mechanism: loss of function / hypomorph.** Complete human DPH1 null has not been proven in a liveborn; mouse `Ovca1^−/−` is 100% embryonic/perinatal lethal (Chen & Behringer 2004; Liu et al. 2012, verbatim per automated extraction: *"eEF2(G717R/G717R) mice showed milder phenotypes than OVCA1(−/−) mice (which are 100% embryonic lethal)"*). **Inference, not demonstration:** surviving human patients plausibly all retain residual DPH1 activity. State this as an inference.
- **No gain-of-function and no dominant-negative mechanism** has been proposed.
- **Somatic origin:** not applicable — all reported disease alleles are germline. (`p.Ser221Pro` entered the literature from COSMIC as a somatic cancer catalogue entry and was used by Urreizti only as an assay control.)

### 4.3 Population frequency and classification

- ClinVar, queried 2026-10-27: **323 records** for `DPH1[gene]`; **84** carry a pathogenic or likely-pathogenic property. Review status is weak — the three best-known disease alleles are single-submitter except p.Leu234Pro/p.Leu229Pro (6 SCVs, no conflicts), and p.Leu125Pro/p.Leu120Pro currently has **conflicting classifications**.
- Patient alleles are absent or vanishingly rare in population databases: c.17T>A was *"absent from ExAC"* (Loucks); Ütkür et al. report the *DPH1* variants they screened occur in *"between one and five of 125,748 exomes and 15,708 genomes"*.
- **Carrier frequency is unknown** for every population except the one North American isolate (0.46%, 5/1,098 chromosomes).

### 4.4 Variants of uncertain significance: a dedicated functional resource exists

Ütkür et al. 2023 (PMID:37675463) screened gnomAD *DPH1*/*DPH2* missense variants near the active site and functionally classified them as **"deficiency-susceptibility alleles"** (their term, verbatim per automated extraction). Reduced function: **DPH1 G113R, A114T, H132P, H132R, S136R, C137F, L138P, Y152C, S221P, H240R**; **DPH2 H105P, C341Y**. Tolerated: **R223P, P249R, L297S, R299C**, plus **P348S and L350H** (tolerated in MCF7 but reduced in the more sensitive yeast assay). Their framing is careful and should be preserved: *"variants with reduced functionality are likely to be disease relevant in homozygous or compound heterozygous combinations"* and *"This underlines the importance of experimental assessment to differentiate deleterious from tolerated variants."* These residue numbers follow the literature (Met6) convention.

### 4.5 Modifier genes, epigenetics, chromosomal context

- **Modifier genes: none identified.** Urreizti raised inter-family severity differences that *"could reflect variant severity or other genetic factors"* (Loucks' wording) — unresolved.
- **Epigenetics: nothing for the germline disorder.** *DPH1* promoter methylation causing immunotoxin resistance is a somatic, cancer-cell-line observation (Hu et al., Leuk Res 2013, PMID:24070652) and must not be imported.
- **Chromosomal: *DPH1* lies in the Miller–Dieker syndrome 17p13.3 critical deletion region.** Yu et al. (Hum Mol Genet 2014, PMID:24895408) showed with conditional mouse genetics that OVCA1/DPH1 loss accounts for part of the **craniofacial** component of MDS (verbatim per automated extraction: *"OVCA1 deficiency in the neural crest contributes to the craniofacial abnormalities in patients with MDS"*). **Clinical consequence:** a 17p13.3 deletion unmasking a *DPH1* variant on the other allele is a plausible but, as far as I found, **unreported** compound mechanism — flag it as a hypothesis, not a finding. CMA in reported patients showed only AOH, no pathogenic CNV.

---

## 5. Environmental Information

**Not applicable.** No environmental factor, lifestyle factor, occupational exposure, infectious agent or teratogen contributes to DEDSSH1. Recurrent respiratory infections and aspiration-related illness are **consequences** of hypotonia, airway obstruction and feeding difficulty, not causes — and they are the proximate cause of at least one death (Urreizti Patient 2, severe respiratory tract infection at 20 years). Any environmental node in a pathograph for this disease should be modelled downstream, as a complication, not as an initiating exposure.

---

## 6. Mechanism / Pathophysiology

### 6.1 The causal chain

Each step names what it causes next. Evidence class is stated per step: **[H]** human patient data, **[M]** mouse, **[X]** *Xenopus*, **[Y]** yeast, **[V]** human cell line in vitro, **[C]** computational/structural.

1. **A biallelic *DPH1* variant reduces or abolishes the activity of the DPH1–DPH2 heterodimeric radical-SAM enzyme** (2-(3-amino-3-carboxypropyl)histidine synthase, EC 2.5.1.108). **[H, V, Y, C]** The enzyme is a [4Fe-4S]-cluster protein; in human DPH1 the cluster-binding cysteines align to **Cys115, Cys219 and Cys347** (Urreizti, direct read, aligned to *P. horikoshii* DPH2 Cys59/Cys163/Cys287).
2. **→ leads to failure of step 1 of diphthamide biosynthesis: transfer of the 3-amino-3-carboxypropyl (ACP) group from S-adenosyl-L-methionine (`CHEBI:15414`) to histidine 715 of eEF2.** **[V, Y]** Ütkür et al. (verbatim per automated extraction): *"to modify histidine 715 of human eEF2 with ACP, the first intermediate in diphthamide formation."* The downstream pathway (DPH5 methylation → DPH7 demethylation → DPH6 amidation; DPH3/DPH4 supplying electrons to the Fe-S cluster) cannot proceed without this step.
3. **→ results in eEF2 lacking the diphthamide residue (`CHEBI:16692` diphthamide residue).** **[H, V, Y, M]** Demonstrable by the diphtheria-toxin ADP-ribosylation assay: unmodified eEF2 cannot be biotin-ADP-ribosylated.
4. **→ reduces the fidelity of translational elongation**, specifically permitting **−1 ribosomal frameshifting**. **[Y, M]** Liu et al. (verbatim per automated extraction): *"the diphthamide modification is essential for eEF2 to prevent −1 frameshifting during translation"*; Hawer et al. 2018: *"increased ribosomal −1 frame-shift errors in mutants lacking modifiable pools of EF2"*. Hawer et al. 2020 summarise the clinical framing: *"Diphthamide deficiency was shown to reduce the accuracy of ribosomal protein biosynthesis."* **This step is demonstrated in yeast and mouse; it has not been measured in patient cells.**
5. **The chain branches here.** Diphthamide loss does **not** cause a global collapse of protein synthesis; it is selective. Webb et al. (verbatim per automated extraction): *"suggesting that lack of diphthamide on eEF2 could result in translational failure of specific proteins"*.

   **Branch A — eEF2 → p53 → p21 → neural crest proliferation arrest (the best-supported route to the craniofacial and growth phenotype).** **[M, X, V]**
   6A. **→ unmodified eEF2 dissociates from ribosomes and accumulates in the nucleus**, where its N-terminal GTPase domains bind p53. Shi et al. 2024 (verbatim per automated extraction): *"DPH1 depletion facilitates dissociation of eEF2 from ribosomes and association with p53"*.
   7A. **→ eEF2-bound p53 occupies the *CDKN1A* (p21) and *PUMA* promoters**, raising p21 mRNA and protein — *"Consequently, there is more eEF2-bound p53 with enhanced association with the p21 promoter"*. Crucially, **total p53 is unchanged and no apoptosis occurs** — *"Thus, the NC defects caused by loss of DPH1 cannot be attributed to increased p53 levels"*. This distinguishes the mechanism from classical ribosomopathies, where p53 is stabilised.
   8A. **→ elevated p21 inhibits proliferation of the dorsal neuroepithelium and pre-migratory neural crest cells** (`CL:0011012` neural crest cell; `CL:0007004` premigratory neural crest cell; `GO:0008285` negative regulation of cell population proliferation).
   9A. **→ reduced neural crest output produces unfused palatal shelves, a shortened Meckel's cartilage, reduced SOX10 and pH3, and a smaller embryo** — and **knocking out one *p21* allele partially rescues body size and palate fusion** (*"Knockout of one p21 allele rescues the NC phenotypes in the knockin mice"*). Independently, Yu et al. 2014 showed **neural-crest-specific** *Ovca1* ablation reproduces cleft palate and a short mandible while paraxial-mesoderm ablation does not.
   10A. **→ in humans this maps onto the craniofacial dysmorphism, cleft palate and micrognathia**; and, because pituitary hormone-producing cells are neural-crest-associated, Shi et al. propose the route to short stature: *"Growth retardation and short stature are common symptoms of NC defects"*; *"these results provide a connection between NC defects and growth retardation"*. **The pituitary/GH limb is a proposal supported by the clinical observation of GH deficiency in at least two patients, not a demonstrated human mechanism.**

   **Branch B — p53-dependent proliferation arrest in non-neural-crest tissue.** **[M, V]** `Ovca1^−/−` MEFs have proliferation defects that *"p53 deficiency can rescue"*, and p53 loss partially rescues the embryonic phenotypes (Chen & Behringer 2004). This is the older, cell-autonomous version of Branch A and is consistent with it.

   **Branch C — pre-activation of NF-κB and death-receptor signalling.** **[V]** Diphthamide-null MCF7 cells are *"presensitized"* in NF-κB and death-receptor pathways without dying, and are *"hypersensitive toward TNF-mediated apoptosis"* (Stahl et al. 2015). Hawer et al. explicitly float this as a candidate route to the neurodevelopmental phenotype while conceding the gap: *"Why the loss of eEF2-diphthamide modification leads to an intellectual disability syndrome is unclear."* **Unconnected to any patient observation — a hypothesis node, not an established edge.**

   **Branch D — selenoprotein under-production and replication stress.** **[V]** Diphthamide loss reduces selenocysteine incorporation and so selenoprotein expression (Hawer et al. 2020), and modulates translation of RRM1 with consequent DNA replication stress (Zhao et al., ACS Cent Sci 2024, PMID:39463834). **No patient-level selenoprotein or replication-stress data exist.**

11. **→ the clinical phenotype**: static global developmental delay and intellectual disability; craniofacial dysmorphism and abnormal skull shape; cleft palate in a minority; sparse hair and dysplastic nails and teeth (ectodermal derivatives, mechanism **not** worked out — plausibly the same proliferation deficit in ectodermal appendages, but this is an inference with no supporting experiment); short stature (growth-plate and/or GH-axis); cardiac outflow and septal malformations (cardiac neural crest, `GO:0061308` — inference by lineage, not demonstrated for *DPH1*); renal and genital anomalies (mechanism unknown).

### 6.2 Is this a ribosomopathy?

Hawer et al. argue yes, with a qualifier (verbatim per automated extraction): the disorder *"may be considered a special type of ribosomopathy"*, grouped with Diamond–Blackfan anaemia, Shwachman–Diamond and Bowen–Conradi syndromes — *"as a special ribosomopathy due to reduced functionality of components of the cellular machinery"*. The qualification is load-bearing: the lesion is in a **translation factor modification**, not in a ribosomal protein or rRNA, and (per Shi et al.) **p53 is not stabilised**, which is the usual ribosomopathy signature. A dismech entry should record the ribosomopathy classification *and* the two ways it departs from the prototype.

### 6.3 Structural basis of individual variants

From Urreizti et al. (read directly from the manuscript PDF; homology model of human DPH1–DPH2 on the *P. horikoshii* DPH2 homodimer, PDB **3LZD**; GROMACS molecular dynamics ≥12 ns, OPLS-AA):

- **Two "gates" (A and B)** form the only opening through which the ~4 Å cube-shaped [4Fe-4S] cluster can reach the catalytic cavity. **Gate A** is defined by Phe329, Trp354, Glu327, Arg349 and **Tyr112** sitting on top of them; **Gate B** by Tyr112, Arg349, His135, Gln185 and His240.
- **p.Tyr112Cys** sits in the centre of the entry gate: *"variant Tyr112Cys could hinder the insertion of the iron-sulfur cluster to its final destination."*
- **p.Leu234Pro** and p.Ser221Pro **shrink gate A**; **p.Leu125Pro** sits at the DPH1–DPH2 interface, close to DPH2 Thr290/Gln295/Arg297/Ala318, and *"may affect the DPH1-DPH2 interaction"*, also reducing inter-cysteine distances.
- **p.Leu164Pro** and **p.Pro382Ser** act differently — Pro382Ser *"showed the highest reduction in the number of hydrogen bonds between both subunits"*.
- **Overall conclusion:** *"all five missense variants analyzed by molecular dynamics simulations displayed some structural alteration compared to the wild-type or affected a residue located in a critical position for the iron-sulfur cluster insertion."*

### 6.4 Suggested ontology bindings for mechanism nodes

All CURIEs below were resolved via EBI OLS4 on 2026-10-27; labels are exact as returned.

| Concept | CURIE | Exact label |
|---|---|---|
| The modification reaction itself | `GO:0017183` | protein histidyl modification to diphthamide |
| The DPH1–DPH2 enzyme complex | `GO:0120513` | 2-(3-amino-3-carboxypropyl)histidine synthase complex |
| Diphtheria-toxin reaction (assay basis) | `GO:0047286` | NAD+-diphthamide ADP-ribosyltransferase activity |
| Downstream pathway enzymes | `GO:0141133` / `GO:0017178` | diphthine methyl ester synthase activity / diphthine-ammonia ligase activity |
| Fe-S cofactor | `GO:0051539` | 4 iron, 4 sulfur cluster binding |
| Translation step affected | `GO:0006414` | translational elongation |
| p53 limb | `GO:0072331` | signal transduction by p53 class mediator |
| p21 effect | `GO:0008285` | negative regulation of cell population proliferation |
| Neural crest limb | `GO:0014032` | neural crest cell development |
| Cardiac NC limb (inferred) | `GO:0061308` | cardiac neural crest cell development involved in heart development |
| Cell type | `CL:0011012` / `CL:0007004` / `CL:0000008` | neural crest cell / premigratory neural crest cell / migratory cranial neural crest cell |
| Cofactor | `CHEBI:15414` | S-adenosyl-L-methionine |
| Product residue | `CHEBI:16692` (residue) / `CHEBI:15949` (free) | diphthamide residue / diphthamide |

---

## 7. Anatomical Structures Affected

**Primary (directly implicated by the mechanism):**
- **Craniofacial skeleton and sutures** — skull vault shape, metopic and sagittal sutures, mandible (Meckel's cartilage in mouse), maxilla; **secondary palate** `UBERON:0001716`, **secondary palatal shelf** `UBERON:0005619` (unfused shelves at E15.5 in *Dph1* knock-in mice).
- **Central nervous system** — cerebral cortex (ID, seizures), **cerebellar vermis** `UBERON:0004720` (hypoplasia, Dandy–Walker spectrum), corpus callosum (agenesis), ventricular system (dilatation, hydrocephalus), white matter (leukomalacia, leukodystrophy in one patient).
- **Ectodermal appendages** — scalp hair follicles, eyebrow/eyelash follicles, toenails, teeth (number, shape, eruption).
- **Growth plate / growth axis** — short stature, low BMD, advanced bone age in one patient; pituitary somatotroph axis (GH deficiency) ⚠ anatomical binding to adenohypophysis not individually resolved.

**Secondary / complication-level:**
- **Heart** — interventricular septum (VSD), conotruncal outflow (tetralogy of Fallot), myocardium (dilated cardiomyopathy, eccentric LV hypertrophy), aortic root and ascending aorta (dilatation).
- **Kidney** — structural (horseshoe kidney, unspecified anomalies) and interstitial (focal interstitial nephritis).
- **External genitalia** — penis (micropenis, hypospadias), scrotum, testis descent, tunica vaginalis (hydrocele).
- **Upper airway** — obstructive sleep apnoea, congenital airway obstruction.
- **Ear** — external (low-set, protruding, overfolded helices); middle and inner ear implied by mixed conductive/sensorineural hearing loss.
- **Eye** — cornea (keratoconus), orbit (proptosis), refractive (high myopia).

**Cell level:** neural crest cells and their cranial/cardiac derivatives (`CL:0011012`, `CL:0000008`); dorsal neuroepithelium; fibroblasts (the patient-derived cell type used for RNA-seq and functional work); lymphoblastoid cells.

**Subcellular:** cytoplasmic translation machinery (eEF2 on the ribosome); the nucleus (eEF2–p53 complex, the key relocalisation event); the DPH1–DPH2 heterodimer with its [4Fe-4S] cluster.

**Lateralisation:** malformations are midline/bilateral (palate, corpus callosum, vermis, skull sutures). No asymmetric or lateralised pattern is reported.

---

## 8. Temporal Development

**Onset: congenital** (`HP:0003577` annotated 8/8). Prenatal detection is documented — tetralogy of Fallot on fetal echocardiogram at 20 weeks, and polyhydramnios prompting caesarean delivery. (A 2024 ACMG conference abstract, *"P295: Expanding the prenatal phenotype of a rare syndrome due to variants in DPH1"*, Genetics in Medicine Open, appears in search results but **I could not retrieve its text**; treat any prenatal-series claim attributed to it as unverified.)

**Pattern:** non-progressive (static) neurodevelopmental impairment on a background of congenital malformations, with **superimposed acquired complications** that are progressive. Explicitly:
- **Neonatal:** seizures, feeding difficulty, respiratory support, hypotonia, congenital hydrocephalus; multiple congenital anomalies prompting NICU admission (one patient nursed 2 months).
- **Infancy–early childhood:** global developmental delay; failure to thrive; cardiac surgery where indicated (ToF repair at 4 months); G-tube at 5 months in one patient; OSA from 3 months in one.
- **Childhood:** the ectodermal phenotype becomes fully expressed — **dysplastic toenails and dental abnormalities are explicitly age-dependent** (Cheng et al.). Craniosynostosis where present. Epilepsy.
- **Adolescence/adulthood:** **cardiomyopathy is an adult-onset acquired complication** — congestive heart failure with dilated cardiomyopathy at 18 years in one patient; aortic root dilatation on medical therapy in another. Progressive hearing loss is reported in some, while Waskow et al. report hearing loss that **remitted**.
- **Death:** 3 of the 4 Saudi patients died early (8 months, 18 months, 4 years); one Maltese patient died at 20 years after severe respiratory infection. Others survive to 31 years and into adulthood.

**Critical intervention windows (pediatric framing):** (i) the neonatal period for airway, feeding and seizure management; (ii) infancy for cardiac surgical repair; (iii) childhood for GH assessment — this is the one window where a specific therapy changes a measurable outcome; (iv) ongoing childhood/adolescence for audiology and dental surveillance; (v) adolescence onward for cardiomyopathy surveillance.

**Remission:** none for the core disorder. The only reported remission of any feature is hearing loss (single sibling pair).

---

## 9. Inheritance and Population

- **Inheritance: autosomal recessive** (`HP:0000007`), confirmed in every reported family. No X-linked, mitochondrial, digenic, or de novo dominant case.
- **Prevalence/incidence: not documented.** Orphanet (ORPHA:459061) carries no prevalence class that I could retrieve; no incidence figure exists in any source. Both Cheng 2021 and Al-Ajlouni 2025 state fewer than 20 published patients. The honest statement is "ultra-rare; prevalence not estimated", **not** a fabricated band.
- **Penetrance:** appears complete in biallelic individuals; **expressivity is markedly variable and tracks the genotype** (see §4.1 and §11.3). No unaffected homozygote has been reported.
- **Anticipation:** not applicable (no repeat expansion).
- **Germline mosaicism:** not reported.
- **Founder effect:** one, in an unnamed North American genetic isolate (c.17T>A, MAF 0.46%). The recurrence of c.335A>G in **three independent Yemeni families** across two publications is suggestive of a second founder allele but has not been formally established by haplotype analysis — record as a hypothesis.
- **Consanguinity:** central; most families are consanguineous.
- **Carrier frequency:** unknown outside the one isolate.
- **Populations reported:** Saudi (4), North American isolate (4), Pakistani (2), Iranian (2), Maltese (2), Yemeni (3 across two reports), Japanese (1), Chinese (1), plus US-based sibling pair. Al-Ajlouni et al. tabulate 17 cases across these origins.
- **Sex ratio:** no sex bias reported; both sexes affected; the apparent male excess among detailed case reports is an artefact of small numbers (and of genital anomalies being ascertainable only in males).
- **Age distribution:** reported patients span 20 months to 31 years.

---

## 10. Diagnostics

### 10.1 Genetic testing — the diagnostic route

- **Exome or genome sequencing is the diagnostic test.** Every published diagnosis was made by WES/WGS (trio or proband-plus-parent), frequently after years of undiagnosed clinical-syndrome labels. Two patients waited from a non-diagnostic 2013 WES to a 2020 VUS reclassification.
- **The phenotype does not reliably suggest the gene**, so a targeted single-gene test is not a sensible first move. Where a panel is used, it must include *DPH1*, *DPH2* and *DPH5*.
- **Chromosomal microarray** is useful chiefly for documenting absence of heterozygosity (consanguinity) and for excluding 17p13.3 deletion (Miller–Dieker). Reported CMAs showed no pathogenic CNVs.
- **RNA sequencing of patient fibroblasts is a necessary adjunct** when exome is negative. Waskow et al. (verbatim per automated extraction): *"both were homozygous for an intronic c.749+39G>A [NM_001383.6] variant in DPH1"*, and *"RNAseq analysis performed on RNA from fibroblasts revealed significantly reduced expression of DPH1 transcripts"*, demonstrating *"the clinical utility of RNAseq as a means of functionally validating the effects of intronic variants"*. A deep-intronic variant 39 bp into an intron would be filtered out of a standard exome pipeline.
- **Functional confirmation exists and is uniquely clean for this gene.** The **diphtheria-toxin ADP-ribosylation (ADPR) assay** on eEF2 — biotinylated NAD + DT, with the biotin signal read on a Western blot — directly measures whether diphthamide is present. Urreizti et al. (direct read): *"eEF2 without diphthamide does not become ADP-ribosylated, and hence, is not labeled with biotin."* The assay is performed by transfecting DPH1-knockout MCF7 cells with the patient allele. Urreizti et al. conclude the combination of assay plus structural modelling *"may be used for predicting patient outcomes and prognoses"*. **Caveat (Ütkür et al.):** the MCF7 assay relies on over-expression and can miss partial loss of function — and it misses p.Met6Lys entirely (§4.1).
- **Not indicated:** karyotype (normal in reported cases), FISH, mtDNA testing, repeat-expansion testing.

### 10.2 Clinical and laboratory evaluation at diagnosis

No diagnostic biomarker, enzyme assay on blood, metabolite or imaging finding is specific to this disorder. The evaluation is organ-directed:

| Modality | Purpose | Findings reported |
|---|---|---|
| Brain MRI (preferred over CT) | malformation detection | vermis hypoplasia, Dandy–Walker, ACC, ventriculomegaly, cavum septi pellucidi, parenchymal volume loss, leukodystrophy |
| Echocardiography | CHD + baseline for cardiomyopathy | VSD, tetralogy of Fallot, PDA, dilated cardiomyopathy, eccentric LVH, aortic root dilatation |
| Renal ultrasound | structural anomaly | horseshoe kidney; normal in others |
| Urinalysis / renal function | interstitial nephritis | haematuria, proteinuria; one renal biopsy showed mild focal interstitial nephritis |
| Audiology | conductive/SNHL | mixed severe hearing loss; mild hearing loss; possible remission |
| EEG | seizures | generalised slow spike-and-wave; focal spikes; also normal in one |
| Skeletal survey / bone age | skeletal anomalies | fused vertebrae, hand/foot bony defects, advanced bone age, low BMD |
| Ophthalmology | keratoconus, myopia | keratoconus, proptosis, high myopia, esotropia |
| Endocrine (thyroid; **GH stimulation testing**) | treatable deficiency | hypothyroidism; **documented GH deficiency** |
| Dental | age-dependent anomalies | peg-shaped teeth, missing teeth, natal teeth |
| Sleep study | OSA | obstructive sleep apnoea in several |

Cheng et al.'s explicit recommendation (verbatim per automated extraction): *"Dental and endocrine checkup should be considered in the routine follow-up of DPH1 syndrome patients."*

### 10.3 Differential diagnosis

Every one of these has been a **wrong** clinical label on a patient later shown to have biallelic *DPH1* variants — this list is clinical history, not speculation:

| Differential | Distinguishing features |
|---|---|
| **Ritscher–Schinzel (3C) syndrome** | cranio-cerebello-cardiac; the Saudi family was published as 3C in 2011 before *DPH1* was found |
| **Sensenbrenner syndrome / cranioectodermal dysplasia** (MIM 218330) | shares sagittal craniosynostosis + ectodermal features; **DEDSSH1 lacks significant retinal and hepatic disease, and has prominent developmental delay** |
| **Fine–Lubinsky syndrome** (brachycephaly, deafness, cataract, microstomia, ID) | Waskow et al.: *"all individuals with a clinical diagnosis of Fine-Lubinsky syndrome be screened for variants in DPH1"* |
| **Opitz C / trigonocephaly syndromes** | Urreizti Patient 1's original diagnosis |
| **Noonan syndrome and RASopathies** | raised as the differential for DPH5-related disease (Politano et al. 2025); the combination of short stature, relative macrocephaly and CHD overlaps |
| **DEDSSH2 (*DPH2*, OMIM 620062; MONDO term exists)** | clinically near-identical — see §10.4 |
| **DPH5-related diphthamide deficiency** (Shankar et al., Genet Med 2022, PMID:35482014; Politano et al., Genes 2025) | embryonic lethality / profound NDD at the severe end |
| Miller–Dieker syndrome / 17p13.3 deletion | lissencephaly dominates; *DPH1* loss contributes the craniofacial component (Yu et al.) |

### 10.4 DEDSSH2 (*DPH2*) — the closest mimic

HPO annotations for OMIM:620062 (retrieved 2026-10-27; all from PMID:32576952, n=3): global developmental delay 3/3, short stature 3/3, sparse scalp hair 3/3, prominent forehead 3/3, low-set ears 3/3, microcephaly 2/3, macrocephaly 1/3, muscular VSD 1/3, brachydactyly 1/3, single transverse palmar crease 1/3, hydrocele testis 1/3, notched primary central incisor 1/1, high anterior hairline 1/3; infantile onset 3/3; autosomal recessive. **The DEDSSH1 and DEDSSH2 phenotypes are not clinically separable** — they differ by gene, and that is the argument for keeping them as separate entries under the MONDO:0031632 / OMIM PS616901 grouping while sharing a mechanism module.

### 10.5 Screening

No newborn screening, no population carrier screening. **Cascade carrier testing within a family and within a founder population is feasible and appropriate** once the familial variant is known.

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

No survival curve, life-expectancy estimate or mortality rate exists — the denominators are far too small. What is on record:
- **Early death in 3 of 4 Saudi patients** homozygous for p.Leu234Pro: at 8 months, 18 months and 4 years. HPO records `HP:0001522 Death in infancy 1/8` and `HP:0003819 Death in childhood 2/8`.
- **Death at 20 years** after a severe respiratory tract infection (Maltese p.Leu125Pro homozygote).
- **Survival to 31 years** (her brother), to adulthood in the Chinese patient, and to 14 years in the Yemeni patient with ongoing care.

Urreizti et al. (direct read): *"three out of four patients suffered an early death, with heart, renal, and CNS malformations (Table 1) and represent the most severely affected DPH1 syndrome patients."*

### 11.2 Morbidity, disability, complications

Lifelong intellectual disability spanning mild to profound; non-ambulatory status and absent speech at the severe end; tube feeding; recurrent respiratory infection and aspiration risk; epilepsy; hearing impairment; dental loss; hydrocephalus requiring shunt; and **cardiomyopathy as the key acquired adult complication**. No ICF-coded disability data and no QoL instrument data exist.

### 11.3 Prognostic factors — genotype is the strongest available predictor

This is the best-developed prognostic statement in the literature, and it comes from a functional assay. Urreizti et al. (read directly from the manuscript PDF):

> *"Generally, the DPH1 activity measured for each variant by our assay correlated with the severity of the corresponding patients' clinical presentation."*

> *"The remaining five DPH1 variants showed a significantly greater reduction in DPH1 activity, correlating with these patients' more severe clinical presentations."*

Practically:
- **Residual activity preserved in vitro (p.Met6Lys, p.Pro382Ser)** → milder: ID described as mild/moderate, no reported heart or CNS malformation, one patient described as a "good learner". Urreizti nonetheless warn: *"we cannot rule out these variants being non-pathogenic, and further characterization of them would be necessary."*
- **Markedly reduced activity (p.Leu234Pro, p.Leu125Pro, p.Tyr112Cys, p.Leu164Pro, p.Ala411Argfs\*91)** → severe: CNS and cardiac malformations, profound ID, early death in several.
- **Structural correlate:** loss of activity tracked with *"reduced size of the opening to the catalytic site, and changes in the size of the catalytic site with clinical severity"* (abstract, direct read).

**Do not over-apply this.** It is a correlation across ~16 patients in ~7 genotype groups, with no statistical analysis, and the p.Met6Lys assay result is a known false negative.

### 11.4 Prognostic biomarkers

None. The ADPR assay is a **variant**-level, not a patient-level, predictor.

### 11.5 Recovery potential

None for the structural malformations or the intellectual disability. **Two reversible or improvable elements are documented**: growth, through GH replacement in GH-deficient patients; and hearing, in the single report where it remitted.

---

## 12. Treatment

**There is no disease-modifying or targeted therapy, and none is in development.** No clinical trial has ever been registered for this disorder (no NCT or ICTRP identifier was found). Management is entirely supportive, organ-directed, and anticipatory.

### 12.1 Reported interventions

| Intervention | Indication | Evidence | NCIT lead (⚠ verify reachability from `NCIT:C25218` before binding) |
|---|---|---|---|
| **Growth hormone replacement** | documented GH deficiency | Shi et al. 2024: GH replacement restored growth in the DEDSSH1 proband; Cheng et al. 2021 documented GHD | agent: `NCIT:C837` **Somatropin** (OLS4-verified label); action term ⚠ |
| **Losartan + atenolol** | dilated aortic root / ascending aorta | Al-Ajlouni 2025 | agent CHEBI/NCIT ⚠; action `NCIT:C15986` Pharmacotherapy (per repo documentation) |
| **Ventriculoperitoneal shunt** | congenital hydrocephalus (placed at age 8) | Al-Ajlouni 2025 | `NCIT:C168483` **Ventriculoperitoneal Shunt Placement** (OLS4-verified) |
| **Cardiac surgery** | tetralogy of Fallot repair at 4 months | Urreizti 2020 | `NCIT:C15329` Surgical Procedure (per repo documentation) |
| **Antiseizure medication** | neonatal seizures, epilepsy | multiple reports (specific agents rarely named) | ⚠ |
| **Gastrostomy / nutritional support** | poor feeding, failure to thrive (G-tube at 5 months; lifelong tube feeding in one) | Urreizti 2020; Al-Ajlouni 2025 | ⚠ |
| **Supplemental oxygen / OSA management** | obstructive sleep apnoea | Urreizti 2020 (nocturnal O₂ for several years) | ⚠ |
| **Hearing amplification** | mixed hearing loss | Al-Ajlouni 2025 | device `NCIT:C183182` Hearing Aid — **a device term, not a clinical action**; per repo convention bind the action and carry the device as a `qualifiers` predicate–value pair |
| **Physical, occupational and speech therapy** (twice weekly) + special education | global delay | Al-Ajlouni 2025 | `NCIT:C15302` Physical Therapy; `NCIT:C159273` speech language therapy; `NCIT:C121351` occupational therapy (per repo documentation) |
| **Ankle–foot orthosis, gait training** | congenital vertical talus, weakness | Al-Ajlouni 2025 | `NCIT:C15315` Rehabilitation (per repo documentation) |
| **Levothyroxine** | hypothyroidism | Urreizti 2020 (P1 "required treatment for hypothyroidism") | ⚠ |
| **Orchidopexy, inguinal hernia repair** | undescended testes, hernias | Urreizti 2020; Loucks 2015 | `NCIT:C15329` Surgical Procedure |
| **Genetic counselling** | 25% sibling recurrence | universal | `NCIT:C15240` Genetic Counseling (per repo documentation) |

### 12.2 Proposed surveillance protocol (synthesised; no published guideline exists)

No society guideline, GeneReviews chapter or care standard exists for this disorder — **state that explicitly rather than implying a consensus**. Synthesising the published recommendations:

- **Echocardiography** at diagnosis and periodically lifelong — Waskow et al.: *"individuals with DEDSSH1 should be monitored for the development of cardiomyopathy."*
- **Audiology** at diagnosis and serially — Al-Ajlouni et al. note progressive hearing loss supports regular surveillance; Waskow et al. note possible remission (so do not assume a fixed deficit).
- **Endocrine review including growth monitoring and GH assessment**, and **dental review** — Cheng et al.
- Developmental/educational assessment; seizure surveillance; renal function and urinalysis; ophthalmology (keratoconus); sleep study where symptomatic; nutrition/aspiration risk.

### 12.3 Pharmacogenomics, advanced therapeutics

- **Pharmacogenomics:** none established for this disorder. The one mechanistically real, non-clinical interaction is **resistance to diphtheria-toxin- and *Pseudomonas*-exotoxin-based immunotoxins** in diphthamide-deficient cells. Whether this has any bearing on a DEDSSH1 patient's response to such an agent is entirely untested — this is a **hypothesis worth recording, not a recommendation**.
- **Gene therapy, cell therapy, RNA therapy, enzyme replacement:** none exist, none proposed. For the intronic c.749+39G>A allele, splice-modulating antisense oligonucleotide therapy is theoretically conceivable — **this is my inference, with no supporting publication**.

---

## 13. Prevention

- **Primary prevention of the disease itself: not possible.** Genetically determined, congenital onset.
- **Reproductive prevention is the only real lever.** Genetic counselling with a 25% recurrence risk per pregnancy for carrier couples; carrier testing of at-risk relatives; prenatal diagnosis (CVS/amniocentesis) and preimplantation genetic testing once the familial variants are known. In consanguineous communities and in the founder isolate, population-level carrier screening for the known local allele is technically straightforward — **not implemented anywhere, to my knowledge**.
- **Secondary prevention (early detection):** no newborn screening; not a candidate (no treatment that must be started presymptomatically, no biochemical marker). **Prenatal ultrasound/fetal echo can detect the malformation phenotype** (tetralogy of Fallot was detected at 20 weeks in one case), which affects delivery planning rather than prevention.
- **Tertiary prevention (preventing complications) is where the real clinical value lies** — the surveillance protocol in §12.2, particularly cardiomyopathy surveillance, GH assessment, and audiological and dental follow-up.
- **Immunisation, public-health, environmental and behavioural interventions:** not applicable, beyond routine childhood immunisation and respiratory-infection precautions appropriate to a child with hypotonia, aspiration risk and OSA.

---

## 14. Other Species / Natural Disease

- **No naturally occurring animal counterpart of this disease has been identified.** I did not find an OMIA entry; recorded as "not found", not as "does not exist" — I did not query OMIA directly.
- **Taxonomy of experimental species:** *Mus musculus* `NCBITaxon:10090` ⚠ (not individually resolved this session); *Xenopus tropicalis*; *Saccharomyces cerevisiae*; *Arabidopsis thaliana*. ⚠ All NCBITaxon CURIEs require lookup before binding.
- **Breed (VBO):** not applicable.
- **Orthologue:** mouse **Dph1**, MGI:2151233 (verified from the MGI disease page for DOID:0070477). The gene is referred to interchangeably as *Ovca1* and *Dph1* in the mouse literature.
- **Evolutionary conservation:** very high. Urreizti et al. aligned DPH1 across 80–85 eukaryotic species (40 mammals, 9 birds, 4 reptiles, 1 amphibian, 7 fishes, 8 insects, 1 nematode, 1 ascidian, 10 fungi, 4 plants) and found (direct read) *"the central part of the protein (positions 80 to 310 of the human DPH1) was highly conserved"*; **Tyr112 is conserved in all analysed species up to and including fungi**; Leu125, Leu164 and Leu234 in nearly all; Pro382 only in mammals, *Xenopus*, most birds and insects. Diphthamide itself is present in **all eukaryotes and archaea but not eubacteria** (GO:0017183 definition).
- **Comparative pathology:** the mouse reproduces the craniofacial and growth phenotype faithfully (cleft palate, shortened mandible, reduced body size) and the plant/yeast systems reproduce the translational-fidelity phenotype. The human-specific neurodevelopmental phenotype — intellectual disability — is the part no model captures (see §15.3).
- **Zoonotic potential / cross-species transmission:** not applicable.

---

## 15. Model Organisms

### 15.1 Mouse

| Model | Phenotype | Reference |
|---|---|---|
| ***Ovca1*/*Dph1* knockout** | Homozygotes die during embryogenesis or at birth with developmental delay and multi-organ defects; **cleft palate** and craniofacial abnormalities; growth restriction; MEF proliferation defect. Heterozygotes spontaneously develop cancer. **p53 loss rescues the MEF proliferation defect and partially rescues the embryonic phenotype.** | Chen & Behringer, Genes Dev 2004;18:320–332 (PMID:14744934) |
| **Conditional *Ovca1* ablation in neural crest vs. cranial paraxial mesoderm** | NC-specific deletion reproduces cleft palate and shortened mandible; paraxial-mesoderm deletion does not. Transgenic myc-Ovca1 partially rescues. Establishes the lineage. | Yu et al., Hum Mol Genet 2014;23:5579–5596 (PMID:24895408) |
| **eEF2 Gly717Arg knock-in** (blocks step 1 of diphthamide synthesis at the substrate end) | Milder than `Ovca1^−/−`; a small fraction survive to adulthood; MEFs retain full elongation activity and normal growth; **does not rescue the −1 frameshifting defect**. Double mutants show the milder phenotype → the lethality of `Ovca1^−/−` is attributable to diphthamide deficiency. | Liu et al., PNAS 2012;109:13817–13822 (PMID:22869748) |
| ***Dph1* patient-allele knock-in** (mouse E237Q and Q41X = human E242Q and Q46X); MGI alleles **Dph1^em1Swei^ / Dph1^em2Swei^** on C57BL/6J | Reduced body size, reduced pH3 and SOX10, **unfused palatal shelves at E15.5**, shortened Meckel's cartilage. **Heterozygous *p21* knockout partially rescues body size and palate fusion.** p53 levels unchanged, no apoptosis. | Shi et al., Nat Commun 2024 (PMID:38671004); alleles listed on the MGI DOID:0070477 page |
| ***Dph4* mutant mouse** | Lacks the eEF2 modification; DT-resistant cells; growth retardation; usually prenatally lethal; survivors have an extra hind-foot digit — **also seen in *Dph1* mutants**. | Webb et al., J Cell Sci 2008;121:3140–3145 (PMID:18765564) |
| ***Dph5* p.His260Arg knock-in** (comparator gene) | Embryonically lethal with one subviable mouse showing growth impairment, craniofacial dysmorphology and multisystem dysfunction resembling the human phenotype. | Shankar et al., Genet Med 2022 (PMID:35482014) |

### 15.2 Non-mammalian and cellular systems

- ***Xenopus tropicalis*:** CRISPR/Cas9 F0 mosaic knockout and morpholino knockdown of *dph1*, read out in a `snai2:eGFP` transgenic line for live neural-crest imaging (Shi et al. 2024). The best system available for neural-crest dynamics.
- **Yeast (*S. cerevisiae*):** the workhorse for mechanism and for variant interpretation. Readouts: Western blot for residual unmodified eEF2 (**more sensitive than the DT assay**), DT and sordarin resistance, hygromycin B hypersensitivity, and **−1 frameshift reporter assays**. Ütkür et al. 2023 retested the human patient alleles' yeast equivalents (Y112C, L125P, L164P, L234P, P382S) and found all compromised. Hawer et al. 2018 (PMID:30335802) established the growth, stress and fidelity phenotypes.
- **Human cell lines:** **MCF7 DPH1-knockout (DPH1ko) cells** are the reference system for the ADPR assay — *"MCF7 derivatives that have all chromosomal DPH1 gene copies inactivated ... lack DPH1 enzyme activity, are diphthamide-deficient, and are resistant to diphtheria toxin"* (Urreizti, direct read). Also U251 glioblastoma knockout/knockdown and HEK293T rescue assays (Shi et al.).
- **Patient-derived cells:** fibroblasts (used for the diagnostic RNA-seq in Waskow et al.) and lymphoblastoid cell lines (Shi et al.). **Patient iPSCs, organoids and organ-chips: none reported — a clear gap**, particularly for the neurodevelopmental phenotype.
- **Plants:** *Arabidopsis* diphthamide synthesis is stress-sensitive and required for translational fidelity and growth (Zhang et al., Nat Commun 2022, PMID:35817801; Plant Physiol 2025, PMID:40200557) — useful for pathway biology, irrelevant to clinical phenotype.

### 15.3 Model fidelity and limitations

- **Recapitulated well:** craniofacial dysmorphism and cleft palate (mouse, NC-conditional); growth restriction; the biochemical lesion (all systems); translational infidelity (yeast, mouse).
- **Recapitulated poorly or not at all:** **intellectual disability** — no model addresses it, and Hawer et al. say so plainly (verbatim per automated extraction): *"Why the loss of eEF2-diphthamide modification leads to an intellectual disability syndrome is unclear."* Also unmodelled: the ectodermal phenotype (sparse hair, dysplastic nails, dental anomalies), the acquired cardiomyopathy, hearing loss, and the renal and genital anomalies.
- **Severity mismatch:** mouse null is embryonic-lethal while human patients survive, so **the null mouse models a severity that does not exist in patients**. The patient-allele knock-in (Shi et al.) is the right model for the human disorder; the null is the right model for pathway biology.
- **Heterozygote divergence:** `Ovca1^+/−` mice develop spontaneous tumours; human heterozygotes are reportedly unaffected. **This is an unexplained species divergence with direct implications for counselling carrier parents, and nobody has studied it.** In dismech terms this is a `HUMAN_MODEL_MISMATCH`, not a `KNOWLEDGE_GAP`.
- **Assay limitations (stated by the authors):** the MCF7 ADPR assay over-expresses the construct and can miss partial LoF (false-negative for p.Met6Lys); the yeast assay tests yeast counterparts rather than the human proteins.

### 15.4 Resources

MGI (`Dph1`, MGI:2151233; alleles MGI:7645689, MGI:7645690); Alliance of Genome Resources; IMPC/KOMP for additional *Dph1* alleles (not checked this session); the Disease Ontology page DOID:0070477 at informatics.jax.org lists the current mouse model for this disease.

---

## 16. Evidence Quality, Open Questions, and Curation Cautions

### 16.1 Priority knowledge gaps

1. **Why diphthamide loss causes intellectual disability.** Stated as unresolved by the field's own review. The p53–p21–neural-crest axis explains the craniofacial and growth phenotype but not cortical function.
2. **Cancer risk in patients and in heterozygous carriers.** `Ovca1^+/−` mice develop spontaneous tumours; no human data exist in either direction. Given the user's domain, this is the single most consequential unasked question in the disorder.
3. **The mechanism of the ectodermal phenotype** (sparse hair, nail dysplasia, dental anomalies) — the feature that most reliably distinguishes the syndrome clinically, and the one with no mechanistic account at all.
4. **Why cardiomyopathy appears late**, and whether it is a primary myocardial consequence of diphthamide deficiency or secondary to the congenital lesion.
5. **The reported remission of hearing loss** — a single sibling pair; needs replication before it is treated as a natural-history fact.
6. **Human-cell evidence for the translational-fidelity defect.** −1 frameshifting has been measured in yeast and mouse, never in patient cells.
7. **Prevalence** — not estimated anywhere.
8. **Whether c.335A>G in three Yemeni families is a founder allele** — never haplotyped.

### 16.2 Cautions for anyone curating this into a structured knowledge base

- **Carry both variant numbering systems**, always with the transcript version (§0a). A snippet quoting "p.Leu234Pro" and a ClinVar record saying "p.Leu229Pro" are the same allele.
- **HPO's annotation set for OMIM:616901 derives from one 2015 paper** and is ~10 years behind the literature. Do not treat it as the phenotype.
- **Keep the frequency denominators** (17/17, 9/11, 7/15…) rather than converting to percentages; the denominators differ because ascertainment differed.
- **Keep germline DEDSSH1 separate from somatic *OVCA1*/*DPH1* oncology** (§0b), and keep DEDSSH1 (*DPH1*) separate from DEDSSH2 (*DPH2*) and DPH5-related disease, under the MONDO:0031632 / OMIM PS616901 grouping.
- **`evidence_source` grading for this literature:** the ADPR assay papers are `IN_VITRO`; the yeast and mouse work is `MODEL_ORGANISM` (yeast included); the case reports are `HUMAN_CLINICAL`; the homology-model and molecular-dynamics results are `COMPUTATIONAL`. Several papers mix these within one abstract — split the evidence items.
- **Quote provenance in this report.** Quotes attributed to "read directly from the manuscript PDF" are from the Urreizti et al. accepted manuscript (University of Barcelona repository), whose pages I read myself. **All other quotes were extracted by an automated fetch-and-extract step from Europe PMC / PMC full text and are reported as verbatim by that step but have not been re-verified character-for-character by me.** Before any of them is used as a dismech `snippet:`, fetch the reference into `references_cache/` with `just fetch-reference PMID:<n>` and re-verify with `just count-verified-snippets`. The automated extractor also enforced a ~120-character ceiling, so several "quotes" are sentence fragments and may fall below the repo's `MIN_SNIPPET_WORDS` propositional-content bar even when exact.
- **Three items I could not verify and have deliberately left unasserted:** the ACMG 2024 conference abstract on the prenatal phenotype (403 on every route); an Orphanet prevalence class for ORPHA:459061; and an ICD-10/ICD-11/MeSH code for this entity.

---

## Sources

**Primary clinical reports**
- Alazami AM, et al. Accelerating novel candidate gene discovery in neurogenetic disorders via whole-exome sequencing of prescreened multiplex consanguineous families. *Cell Rep.* 2015;10:148–161. PMID:25558065. doi:10.1016/j.celrep.2014.12.015 — [europepmc.org](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:25558065&resultType=core&format=json)
- Loucks CM, et al. Matching two independent cohorts validates DPH1 as a gene responsible for autosomal recessive intellectual disability with short stature, craniofacial, and ectodermal anomalies. *Hum Mutat.* 2015;36:1015–1019. PMID:26220823. PMC4575268 — [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/4575268/)
- Riazuddin S, et al. Exome sequencing of Pakistani consanguineous families identifies 30 novel candidate genes for recessive intellectual disability. *Mol Psychiatry.* 2017;22:1604–1614.
- Nakajima J, et al. Novel compound heterozygous DPH1 mutations in a patient with the unique clinical features of airway obstruction and external genital abnormalities. *J Hum Genet.* 2018;63:529–532. PMID:29362492.
- Sekiguchi F, et al. A novel homozygous DPH1 mutation causes intellectual disability and unique craniofacial features. *J Hum Genet.* 2018;63:487–491. PMID:29410513.
- Urreizti R, et al. DPH1 syndrome: two novel variants and structural and functional analyses of seven missense variants identified in syndromic patients. *Eur J Hum Genet.* 2020;28:64–75. PMID:30877278 (correction PMID:31477843) — [diposit.ub.edu](https://diposit.ub.edu/dspace/handle/2445/195034)
- Cheng SSW, Luk HM, Lo IFM. An adult Chinese patient with developmental delay with short stature, dysmorphic features, and sparse hair (Loucks-Innes syndrome). *Am J Med Genet A.* 2021;185:1925–1931. PMID:33704902 — [onlinelibrary.wiley.com](https://onlinelibrary.wiley.com/doi/10.1002/ajmg.a.62164)
- Waskow ER, et al. Recessive loss-of-function variants in DPH1 identified as the molecular cause in a sibling pair previously diagnosed with Fine-Lubinsky syndrome. *Am J Med Genet A.* 2025;197:e63845. PMID:39166428 — [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC11637968/)
- Al-Ajlouni YA, et al. A pediatric case of diphthamide biosynthesis 1 gene defect... (Loucks-Innes syndrome): a case report. *J Med Case Rep.* 2025. PMID:41444928. PMC12729241 — [pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/41444928/)
- Seidahmed MZ, et al. Ritscher-Schinzel (cranio-cerebello-cardiac, 3C) syndrome: report of four new cases with renal involvement. *Am J Med Genet A.* 2011;155A:1393–1397.

**Mechanism, functional and model-organism work**
- Chen CM, Behringer RR. Ovca1 regulates cell proliferation, embryonic development, and tumorigenesis. *Genes Dev.* 2004;18:320–332. PMID:14744934.
- Webb TR, et al. Diphthamide modification of eEF2 requires a J-domain protein and is essential for normal development. *J Cell Sci.* 2008;121:3140–3145. PMID:18765564.
- Liu S, et al. Diphthamide modification on eEF2 is needed to assure fidelity of mRNA translation and mouse development. *PNAS.* 2012;109:13817–13822. PMID:22869748.
- Yu YR, You LR, Yan YT, Chen CM. Role of OVCA1/DPH1 in craniofacial abnormalities of Miller-Dieker syndrome. *Hum Mol Genet.* 2014;23:5579–5596. PMID:24895408.
- Stahl S, et al. Loss of diphthamide pre-activates NF-κB and death receptor pathways and renders MCF7 cells hypersensitive to TNF. *PNAS.* 2015;112:10732–10737. PMID:26261303.
- Mayer K, et al. Influence of DPH1 and DPH5 protein variants on the synthesis of diphthamide. *Toxins.* 2017;9:78. PMID:28245596.
- Hawer H, et al. Importance of diphthamide modified EF2 for translational accuracy and competitive cell growth in yeast. *PLoS One.* 2018;13:e0205870. PMID:30335802.
- Hawer H, et al. Diphthamide-deficiency syndrome: a novel human developmental disorder and ribosomopathy. *Eur J Hum Genet.* 2020;28:1497–1508. PMID:32576952. PMC7575589 — [europepmc.org](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7575589/fullTextXML)
- Ütkür K, et al. DPH1 and DPH2 variants that confer susceptibility to diphthamide deficiency syndrome in human cells and yeast models. *Dis Model Mech.* 2023;16. PMID:37675463. PMC10538292 — [europepmc.org](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10538292/fullTextXML)
- Schaffrath R, Brinkmann U. Diphthamide — a conserved modification of eEF2 with clinical relevance. *Trends Mol Med.* 2024;30:164–177. PMID:38097404.
- Shi Y, et al. Diphthamide deficiency promotes association of eEF2 with p53 to induce p21 expression and neural crest defects. *Nat Commun.* 2024. PMID:38671004. PMC11053169 — [europepmc.org](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11053169/fullTextXML)
- Zhao J, et al. Loss of diphthamide increases DNA replication stress in mammalian cells by modulating the translation of RRM1. *ACS Cent Sci.* 2024. PMID:39463834.

**Related genes (differential diagnosis)**
- Shankar SP, et al. A novel DPH5-related diphthamide-deficiency syndrome causing embryonic lethality or profound neurodevelopmental disorder. *Genet Med.* 2022;24:1567–1582. PMID:35482014.
- Politano D, et al. Expanding the phenotypic spectrum associated with DPH5-related diphthamide deficiency. *Genes.* 2025;16:799. PMID:40725455.

**Databases queried directly (all 2026-10-27)**
- [HGNC REST — DPH1](https://rest.genenames.org/fetch/symbol/DPH1)
- [HPO annotation API — OMIM:616901](https://ontology.jax.org/api/network/annotation/OMIM%3A616901) and [OMIM:620062](https://ontology.jax.org/api/network/annotation/OMIM%3A620062)
- [EBI OLS4 — MONDO:0800438](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0800438), [MONDO:0031632](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0031632), and GO/CL/UBERON/CHEBI/NCIT term searches
- NCBI E-utilities — ClinVar counts (`DPH1[gene]` = 323; P/LP = 84) and `esummary` for VCV 183359, 218949, 521028, 997988
- [gnomAD API — DPH1 constraint](https://gnomad.broadinstitute.org/) (pLI 8.84e-22; LOEUF 1.325)
- [MGI Disease Ontology page — DOID:0070477](https://www.informatics.jax.org/disease/DOID:0070477)
- [Europe PMC REST](https://www.ebi.ac.uk/europepmc/) for abstracts and open-access full text

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 34 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 34 |
| On topic | 20 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 74 |
| Resolved | 64 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 10 |
| Terms whose name was checked | 37 |
| Terms named correctly | 28 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0800438` (5 mentions) - the report calls it "gard_rare`, `ordo_disorder`, `ordo_malformation_syndrome`, `orphanet_rare`, `rare"; MONDO calls it **developmental delay with short stature, dysmorphic facial features, and sparse hair 1**
- `CHEBI:15414` (2 mentions) - the report calls it "Cofactor"; CHEBI calls it **S-adenosyl-L-methionine**
- `GO:0008285` (2 mentions) - the report calls it "p21 effect"; GO calls it **negative regulation of cell population proliferation**
- `GO:0061308` (2 mentions) - the report calls it "Cardiac NC limb (inferred)"; GO calls it **cardiac neural crest cell development involved in heart development**
- `GO:0047286` (1 mention) - the report calls it "Diphtheria-toxin reaction (assay basis)"; GO calls it **NAD+-diphthamide ADP-ribosyltransferase activity**
- `GO:0051539` (1 mention) - the report calls it "Fe-S cofactor"; GO calls it **4 iron, 4 sulfur cluster binding**
- `GO:0072331` (1 mention) - the report calls it "p53 limb"; GO calls it **signal transduction by p53 class mediator**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006414` (1 mention) - the report calls it "Translation step affected"; GO calls it **translational elongation**, and lists "translation elongation" among its other names
- `GO:0014032` (1 mention) - the report calls it "Neural crest limb"; GO calls it **neural crest cell development**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIMPS`, `OMIM`, `ORPHA`, `NCBIGene`, `MGI`, `EXT_ID`.