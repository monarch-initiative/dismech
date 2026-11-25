---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-24T04:43:50.322477'
end_time: '2026-11-24T04:50:43.107022'
duration_seconds: 412.78
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Neurodevelopmental Disorder With Hypotonia and Variable Intellectual
    and Behavioral Abnormalities
  mondo_id: MONDO:0032829
  category: Mendelian
  causal_genes: POLR2A
  omim_id: OMIM:618603
  synonyms: NEDHIB; POLR2A-Related Disorders; POLR2A-associated neurodevelopmental
    disability; POLR2A-related disorder
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
  num_turns: 18
  total_cost_usd: 1.295184405
  session_id: 4c5c0a0b-a3a2-47f9-8018-7ae308bae22b
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 44
  retrieval_calls: 42
  assistant_text_blocks: 4
citation_count: 13
reference_validation:
  total_references: 19
  verified: 18
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.053
  relevance_assessed: 18
  on_topic: 12
  unresolved_references:
  - PMID:36543156
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 71
  verified: 68
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 40
  labels_matching: 26
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0032829
    reported_labels:
    - MONDO
    ontology_label: neurodevelopmental disorder with hypotonia and variable intellectual
      and behavioral abnormalities
  - term_id: HP:0033409
    reported_labels:
    - verify
    ontology_label: Elevated urinary 2-hydroxybutyric acid
  - term_id: HP:0007663
    reported_labels:
    - verify
    ontology_label: Reduced visual acuity
  - term_id: HP:0033725
    reported_labels:
    - verify
    ontology_label: Thin corpus callosum
  - term_id: HP:0000692
    reported_labels:
    - verify
    ontology_label: Tooth malposition
  labels_variant: 9
  unresolvable_prefixes:
  - EXT_ID
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With Hypotonia and Variable Intellectual and Behavioral Abnormalities
- **MONDO ID:** MONDO:0032829 (if available)
- **Causal gene(s):** POLR2A
- **OMIM:** OMIM:618603
- **Synonyms:** NEDHIB; POLR2A-Related Disorders; POLR2A-associated neurodevelopmental disability; POLR2A-related disorder
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Hypotonia and Variable Intellectual and Behavioral Abnormalities** covering all of the
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

Let me try PubMed E-utilities directly.

Still gathering sources: next I'm checking the 2022–2026 case reports (Giacomini, Paparella, Errichiello) and a possible Drosophila lead, then I'll write the report.

Let me read the saved PDF directly.

# POLR2A-Related Neurodevelopmental Disorder (NEDHIB; OMIM #618603; MONDO:0032829): Research Report

**Scope.** This report covers the autosomal-dominant neurodevelopmental disorder caused by germline heterozygous variants in **POLR2A**. POLR2A encodes RPB1, the largest subunit of RNA polymerase II (gene MIM 180660; NCBI Gene ID 5430). It does not cover somatic POLR2A variants in tumours such as meningioma. The literature is small: two cohort papers and about five case reports.

**What I could and could not retrieve.**
- **Read in full:** the Haijes et al. 2019 author manuscript, from the Oxford ORA PDF.
- **Read through intermediaries:** the Hansen et al. 2021 PMC text, Europe PMC records for the case reports, and the NORD page. The fetching tool could quote at most about 125 characters per passage from these. Quotes from those sources are therefore short, and everything else from them is paraphrased.
- **Blocked:** OMIM, Orphanet, PubMed/PMC HTML, ClinVar and LOVD pages.
- **Not verified, so treat as provisional:** the MONDO ID (taken from the request), the HGNC ID, ICD codes and the ORPHA code.
- **Ontology terms:** the HPO, GO, CL, UBERON and NCIT IDs below are my suggestions. I did not check them against the ontology browsers in this session.

---

## 1. Disease Information

**Overview.** NEDHIB is a rare autosomal-dominant neurodevelopmental syndrome. It is caused mostly by de novo heterozygous POLR2A variants.

- The founding paper described 16 individuals ([Haijes et al., *Am J Hum Genet* 2019;105(2):283–301, PMID 31353023, DOI 10.1016/j.ajhg.2019.06.016](https://www.pubmed.gov/31353023/)). Its abstract concludes: *"subtle variants central in functionally important domains of POLR2A cause a neurodevelopmental syndrome characterized by profound infantile onset hypotonia and developmental delay through a dominant-negative effect on pol II-mediated transcription of DNA."*
- A second cohort of 12 individuals broadened the picture to *"a heterogeneous, multi-systemic developmental disorder characterized by transcriptional dysregulation"* ([Hansen et al., *HGG Adv* 2021;2(1):100014, PMID 33665635, DOI 10.1016/j.xhgg.2020.100014](https://pmc.ncbi.nlm.nih.gov/articles/PMC7928427)).

**Identifiers.**

| Identifier | Value | Status |
|---|---|---|
| OMIM phenotype | #618603 | Confirmed by secondary sources ([Evans et al. 2022, PMC8955435](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8955435/); [NCBI Gene 5430](https://www.ncbi.nlm.nih.gov/gene/5430)) |
| OMIM gene | POLR2A *180660 | Stated in Haijes 2019 |
| MONDO | MONDO:0032829 | From the request; not independently verified |
| NCBI Gene | 5430 | Cited on the NORD page |
| Orphanet / ICD-10 / ICD-11 / MeSH | No disease-specific code retrieved | The Orphanet site returned a bot challenge. Generic codes such as ICD-10 F88/F79 or ICD-11 LD90 may apply, but I did not verify them. |
| NORD | "POLR2A-related disorder" | [rarediseases.org](https://rarediseases.org/rare-diseases/polr2a-related-disorder/), last updated 23 April 2025 |

**Synonyms.** NEDHIB; POLR2A-related disorder; POLR2A-related neurodevelopmental disorder; POLR2A-associated neurodevelopmental disability. Gene aliases include RPB1, RPO2, POLR2, POLRA, hRPB220 and NEDHIB ([NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/5430)).

**Data source type.** All information comes from case series and individual case reports, gathered mainly through GeneMatcher and clinical exome or genome sequencing, plus disease-level summaries (NORD, OMIM). There are no EHR or registry-based data. A natural history study and registry at the University of Pittsburgh is listed by [NORD](https://rarediseases.org/rare-diseases/polr2a-related-disorder/).

---

## 2. Etiology

**Primary cause.** The cause is genetic: heterozygous germline POLR2A variants. Variant types and their likely effects:
- missense variants, thought to act dominant-negatively;
- in-frame deletions;
- truncating variants (nonsense or frameshift), thought to cause haploinsufficiency and a milder phenotype.

In Haijes 2019, all 16 variants were ultra-rare and de novo. The cohort had *"three individuals with truncating variants (two stop codons and one frame-shift), three individuals with in-frame deletions (IF deletion) and ten individuals with missense variants"* (PMID 31353023).

**Genetic risk factors.** The main risk is a de novo mutation. One C-terminal frameshift (p.Gln1814Valfs*99) was inherited from a mother described as "largely asymptomatic", who had mild learning difficulty (Hansen 2021, PMID 33665635). This shows that some C-terminal truncations can be mild and transmissible. No modifier genes, susceptibility loci or GWAS signals are known.

**Environmental risk factors.** None are known. Infection can trigger temporary regression: *"Temporary loss of milestones was reported in four individuals, usually following an infection"* (Haijes 2019). This is a precipitant of decompensation, not a cause of the disease.

**Protective factors and gene–environment interactions.** None are known in humans.

There is one model-level gene–environment observation. In yeast, RPB1 equivalents of the patient variants caused growth defects only under stress. Stresses included loss of the transcription factors Dst1 (yeast TFIIS) or Sub1 (yeast PC4), galactose read-through assays, and mycophenolic acid (Haijes 2019). The authors noted that *"phenotypic consequences of rpb1 variants in yeast may be concealed by transcript buffering and may only become apparent under conditions of environmental or nutrient stress."* This is model-organism evidence and has not been shown in humans.

---

## 3. Phenotypes

**Pooled frequency data.**
- **Haijes 2019:** 16 individuals, one of them a terminated fetus. Counts are out of 16 unless noted.
- **Hansen 2021:** 12 individuals. Its abstract contrasts its own rates with the earlier cohort: epilepsy 8/12 versus 3/15, and hypotonia 8/12 versus 14/15.

| Phenotype | Suggested HPO | Haijes 2019 (N=16) | Hansen 2021 (N=12) | Onset / course |
|---|---|---|---|---|
| Global developmental delay | HP:0001263 | All live-born individuals ("all domains… mild to severe") | 12/12 | Infancy; stable Z-scores, *"without developmental catch-up or decline"* |
| Hypotonia (generalized, infantile-onset) | HP:0001290 / HP:0008947 | 14; profound in 9 | 8/12 | Neonatal or infantile; *"tended to improve over time, albeit slowly"* |
| Frog-leg posture | HP:0033409 (verify) | 8 of 11 "probable" cases | — | Infancy |
| Muscle atrophy | HP:0003202 | 4 | — | — |
| Decreased endurance / exercise intolerance | HP:0003546 | 10 | — | Later childhood |
| Intellectual disability | HP:0001249 | Variable | 8/12 | Childhood |
| Feeding difficulties | HP:0011968 | 10 | 7/12 (with failure to thrive) | Infancy |
| Gastroesophageal reflux | HP:0002020 | 6 | — | Infancy |
| Failure to thrive | HP:0001508 | 3 | (included above) | Infancy |
| Strabismus | HP:0000486 | 11 | — | Infancy |
| Delayed visual maturation | HP:0007663 (verify) | 6; decreased vision in 5 | Visual impairment 5/12 | Infancy |
| Sensorineural hearing loss | HP:0000407 | 2 | — | — |
| Recurrent respiratory infections | HP:0002205 | 8 | — | Childhood |
| Seizures / epilepsy | HP:0001250 | 3 (severe) | 8/12 | Variable; refractory in some cases |
| Abnormal brain MRI | HP:0012443 | 10 of the 11 scanned had white-matter abnormalities | 7/12 | — |
| Delayed myelination | HP:0012448 | 5 | — | — |
| Ventriculomegaly / white-matter loss | HP:0002119 / HP:0002352 | 4 | — | — |
| Thin corpus callosum | HP:0033725 (verify) | 2 | — | — |
| Cerebellar abnormality / atrophy | HP:0001272 | 3 | — | Slowly progressive in Giacomini 2022 |
| Sleep disturbance | HP:0002360 | 8 | — | — |
| Autistic behaviour | HP:0000729 | 4 | 6/12 | Childhood |
| Aggressive behaviour (including pica) | HP:0000718 / HP:0011856 | 4 | — | Childhood |
| Developmental regression | HP:0002376 | 4 (temporary, after infection) | 4/12 | — |
| Ataxia | HP:0001251 | — | 7/12 | — |
| Abnormal movements / dystonia | HP:0100022 / HP:0001332 | — | 7/12 / 3/12 | — |
| Joint hypermobility | HP:0001382 | — | 6/12 | — |
| Short stature | HP:0004322 | — | 5/12 | — |
| Skeletal abnormality (hip dysplasia, short Achilles tendons) | HP:0001385 / HP:0001771 | — | 5/12 | — |
| Cardiac abnormality | HP:0001627 | — | 3/12 | Congenital |
| Immune abnormality | HP:0002715 | — | 3/12 | — |
| Recurrent fever | HP:0001954 | — | 4/12 | — |
| Urogenital findings | HP:0000119 | — | 7/12 | — |
| High forehead | HP:0000348 | 7 | — | Congenital |
| Hypertelorism | HP:0000316 | 6 | — | Congenital |
| Dental misalignment | HP:0000692 (verify) | 5 | — | — |
| High palate | HP:0000218 | 5 | — | — |
| Brachy-/plagiocephaly | HP:0000248 / HP:0001357 | 5 | — | — |
| Pectus excavatum | HP:0000767 | 3 | — | — |
| Inguinal hernia | HP:0000023 | 4 | — | — |
| Decreased fetal movement | HP:0001558 | 3 | — | Prenatal |

**Further detail from Haijes 2019 and later case reports.**
- **Hypotonia examination:** hypotonia was shown by *"decreased muscle tone, a frog-like posture in infancy and reduced spontaneous movements but normal tendon reflexes."* Muscle biopsies were inconclusive.
- **Terminated fetus:** this fetus carried p.Asn531Ser and showed corpus callosum agenesis, frontonasal dysplasia and cleft lip.
- **Metabolic work-up:** *"Additional metabolic investigations ruled out known inborn errors of metabolism."*
- **Ependymoma:** one posterior fossa ependymoma was reported in a 2-year-old boy with a de novo germline variant ([Paparella et al., *Am J Med Genet A* 2022;188(9):2796–2802, PMID 35689525](https://onlinelibrary.wiley.com/doi/full/10.1002/ajmg.a.62869); erratum PMID 36543156). NORD states that there is *"no known connection"* to cancer otherwise.
- **Adult case with autism:** a 31-year-old with autism spectrum disorder, epilepsy, strabismus and self-injurious behaviour ([Evans et al., *Genes* 2022;13(3):470, PMID 35328024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8955435/)).
- **Regression with dystonia:** marked regression at age 3, with loss of sitting and walking and language decline, together with sleep-related dystonic nodding ([Cao et al., *Front Neurosci* 2026, PMID 43047756, DOI 10.3389/fnins.2026.1997676](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2026.1997676/full)). The authors conclude that *"neurodevelopmental regression may occur within the phenotypic spectrum of this disorder."*

**Quality of life.** No EQ-5D, SF-36 or PROMIS data exist. The main functional burdens implied by the case data are:
- motor disability, with delayed sitting and walking and reduced endurance;
- feeding dependence;
- visual impairment;
- refractory epilepsy in a subset;
- behavioural problems, including self-injury and aggression.

---

## 4. Genetic / Molecular Information

**Causal gene.**
- POLR2A, RNA polymerase II subunit A (RPB1), on chromosome 17p13.1.
- Reference transcript: NM_000937.4/.5.
- HGNC:9187: from memory, not verified in this session.

**Constraint.** POLR2A is highly intolerant of variation. Per Haijes 2019 (gnomAD):
- pLI is 1.0 and the loss-of-function observed/expected ratio is 0.08;
- *"the Z-score for missense variants is one of the highest (7.13) of all human protein coding genes."*

The 52-repeat C-terminal domain (CTD) tolerates variation in the population, while patient variants cluster in "desert" regions that lack gnomAD missense variants (desert Z-scores 2.9–11.9).

**Reported variants.** All are heterozygous and, unless stated otherwise, germline de novo.

| Variant (protein) | Type | Domain / predicted effect | Source and classification |
|---|---|---|---|
| p.Pro371Leu | Missense | Funnel | Haijes; possibly disease-causing |
| p.Ile457Thr (c.1370T>C) | Missense | Nucleotide-binding site; dominant-negative | Haijes (probable); recurrent in [Giacomini et al., *Brain Dev* 2022;44(7):480–485, PMID 35461703](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:35461703%20AND%20SRC:MED&format=json&resultType=core) |
| p.Val456Ala (c.1367T>C) | Missense | Adjacent to Ile457 | Evans 2022, PMID 35328024 |
| p.Asn531Ser | Missense | Not catalytic | Haijes; unknown significance (fetus) |
| p.Tyr669del | In-frame deletion | Near the "quay" | Haijes; possibly disease-causing |
| p.Gln700* | Nonsense | Haploinsufficiency | Haijes; probable |
| p.Gln735* | Nonsense | Haploinsufficiency | Haijes; probable |
| p.Thr736Met | Missense | Quay; dominant-negative | Haijes; probable |
| p.Ser755del | In-frame deletion | Near the quay | Haijes; probable |
| p.Met769Thr | Missense | Nucleotide-binding site | Haijes; probable |
| p.Ile848Thr | Missense | Bridge helix | Haijes; probable |
| p.Tyr1109His | Missense | Trigger loop | Haijes; probable |
| p.Leu1124Pro | Missense | Trigger loop | Haijes; probable |
| p.Lys1125del | In-frame deletion | Trigger loop | Haijes; probable |
| p.Leu1127Phe (c.3379C>T) | Missense | Trigger-loop region | Cao 2026; likely pathogenic (PS2, PM2_Supporting, PP3) |
| p.Asn1251Ser | Missense | TFIIS-binding surface | Haijes (probable); recurrent ×2 in Hansen |
| p.Glu1289Lys (c.3865G>A) | Missense | Predicted to impair TFIIS interaction | Paparella 2022 |
| p.Arg1603His | Missense | Core–CTD linker; seen 3× in gnomAD | Haijes; possibly disease-causing |
| p.Pro1767fs | Frameshift | Loses about 50% of CTD repeats | Haijes; possibly disease-causing |
| p.Leu438_His439del; p.Ser1094Phe; p.Thr1136Ile; p.Gly1418Arg | In-frame deletion; missense | Various | Hansen 2021; likely pathogenic, de novo |
| p.Gln1814Valfs*99 | Frameshift (C-terminal) | Inherited from a mildly affected mother | Hansen 2021 |
| p.Pro28Arg; p.Arg108His; p.Arg140Trp; p.Ala1092Val | Missense | Inheritance unknown; yeast assays supportive | Hansen 2021 |

**Classification, population frequency and origin.**
- **ClinVar:** not accessible in this session. Hansen classified its 12 variants as likely pathogenic.
- **Population frequency:** essentially absent from gnomAD, except p.Arg1603His (3 alleles).
- **Origin:** germline. In this disease, somatic POLR2A variants are relevant only as a differential consideration: somatic hotspot variants occur in meningioma (e.g., PMID 38380947), which is unrelated to NEDHIB.

**Functional classes.**
- Dominant-negative: missense variants near the catalytic core.
- Haploinsufficiency: truncating variants, which produce a milder phenotype.
- Uncertain: some in-frame deletions sit between these two classes.

**Modifier genes, epigenetics, chromosomal abnormalities.**
- No modifier genes or epigenetic signatures (e.g., DNA-methylation episignatures) have been reported.
- 17p13.1 deletions that include POLR2A would be expected to cause haploinsufficiency. I did not retrieve DECIPHER data on this.

---

## 5. Environmental Information

- **Environmental and lifestyle factors:** none known, and not applicable to disease causation.
- **Infections:** infection is a reported trigger for temporary loss of milestones (Haijes 2019). Hyperpyrexia triggered focal status epilepticus in one infant ([Errichiello et al., *Pediatr Radiol* 2026;56(7):1592–1596, PMID 42033488](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42033488%20AND%20SRC:MED&format=json&resultType=core)).
- **Infectious agents:** none are causal.

---

## 6. Mechanism / Pathophysiology

**Causal chain.**

1. **A heterozygous germline POLR2A variant arises,** usually de novo (human genetic evidence). This leads to one of two branches.
2. **Branch A: missense or some in-frame variants in catalytic regions** (trigger loop, bridge helix, funnel, nucleotide-binding site, quay, TFIIS interface). These produce full-length RPB1 that still assembles into Pol II. Mass spectrometry showed that *"all tested missense RPB1 variants were found to interact with other pol II subunits, indicating that complex formation is largely unaltered"* (in vitro, HeLa).
   - This leads to **catalytically impaired Pol II**: reduced pausing, elongation and/or backtracking, and lower transcriptional fidelity. The evidence comes from structural modelling and yeast Δdst1/Δsub1 and read-through assays, plus reduced HeLa viability for p.Thr736Met, p.Ser755del and p.Leu1124Pro.
   - This in turn leads to a **dominant-negative effect on transcription.** This step is inferred: the authors *"propose that the aberrant pol II enzymes are capable of proper assembly… but subsequent elongation of the nascent RNA occurs at reduced rates and possibly with an increased error rate, blocking access and progression of wildtype pol II on the same DNA strand."* This defective-elongation hypothesis has not been directly demonstrated.
3. **Branch B: early truncating variants** (p.Gln700*, p.Gln735*). The truncated RPB1 cannot assemble with Pol II; the p.Lys812* mimic bound only RPABC3 (POLR2H). The likely result is reduced RPB1 levels but functional Pol II, i.e. haploinsufficiency.
   - This leads to a **milder phenotype**. Haploinsufficient cases had a mean severity score of 10, versus 17 for dominant-negative cases. Their developmental Z-scores were also lower (1.74 vs 4.23, p<0.0001). This is a human genotype–phenotype correlation from a small sample.
4. **Global, non-specific disturbance of RNA polymerase II–dependent transcription** of mRNAs and some non-coding RNAs. This probably affects tissues with high transcriptional demand during development, especially the brain, skeletal muscle and eye. This step is inferred; no tissue transcriptomic data exist. Hansen 2021 describes the disorder as "characterized by transcriptional dysregulation", based on yeast assays.
5. **Impaired neurodevelopment.** Consequences include delayed or deficient myelination and white-matter loss (MRI), thin corpus callosum, and cerebellar atrophy in some cases. Together these lead to global developmental delay, intellectual disability, epilepsy, autism and behavioural features.
   - This is inferred from imaging. Haijes noted overlap with POLR3-related hypomyelinating leukodystrophy (delayed myelination 5/15, white-matter loss 6/15) and proposed that defects in Pol II and Pol III subunits *"can affect protein synthesis via different mechanisms… [resulting] in similar clinical phenotypes."*
6. **Hypotonia, reduced endurance and muscle atrophy.** Muscle biopsies were inconclusive. Whether the cause is central, peripheral, or a muscle transcriptional deficit is unknown.
7. **Stress-sensitive decompensation.** Infections or fever can unmask the transcriptional deficit and cause temporary regression. This is inferred by analogy to the yeast stress-dependent phenotypes and has not been demonstrated in humans.

**Coverage of the checklist.**
- **Pathways:** RNA polymerase II transcription (Reactome "RNA Polymerase II Transcription"; KEGG hsa03020 "RNA polymerase"); transcription elongation with TFIIS (TCEA1), DSIF and P-TEFb; CTD heptad phosphorylation.
- **Suggested GO biological process terms:**
  - GO:0006366, transcription by RNA polymerase II
  - GO:0006368, transcription elongation by RNA polymerase II
  - GO:0001193, maintenance of transcriptional fidelity during transcription elongation by RNA polymerase II
  - GO:0042552, myelination
  - GO:0007399, nervous system development
- **Suggested GO molecular function term:** GO:0003899, DNA-directed RNA polymerase activity.
- **Protein dysfunction:** the largest catalytic subunit is altered in conserved elements (trigger loop, bridge helix). About 50% of Pol II core residues are identical between human and yeast.
- **Immune involvement:** immune abnormalities (3/12), recurrent fever and recurrent respiratory infections were observed (Hansen 2021; Haijes 2019). The mechanism is uncharacterized.
- **Metabolic and biochemical changes:** inborn errors of metabolism were ruled out. No metabolic signature is known.
- **Epigenetic changes:** none reported.
- **Omics, single-cell and CRISPR data:** I found no disease-specific transcriptomic, proteomic, metabolomic, single-cell or CRISPR-screen data. Note that POLR2A is a common-essential gene in DepMap; this is general knowledge and was not retrieved here.
- **Cell types (suggested CL terms, inferred and not experimentally demonstrated):**
  - CL:0000540, neuron
  - CL:0000128, oligodendrocyte (the myelination defect)
  - CL:0000188, skeletal muscle cell
  - Cerebellar Purkinje or granule cells (CL:0000121 / CL:0001031), in the cerebellar-atrophy cases

---

## 7. Anatomical Structures Affected

**Organ level.**
- **Primary:**
  - brain (UBERON:0000955), including cerebral white matter (UBERON:0002437), corpus callosum (UBERON:0002336), cerebellum (UBERON:0002037) and lateral ventricles (UBERON:0002285);
  - basal ganglia and brainstem, in one MRI report (Errichiello 2026, where the findings were vigabatrin-associated);
  - skeletal muscle (UBERON:0001134).
- **Secondary:**
  - eye (UBERON:0000970) and visual system: strabismus, delayed visual maturation;
  - gastrointestinal tract: feeding difficulty, GERD;
  - respiratory tract: recurrent infections;
  - skeleton: pectus, hip dysplasia, clubfoot, short Achilles tendons;
  - heart: congenital anomalies;
  - urogenital system: hydronephrosis;
  - immune system.
- **Body systems:** nervous, musculoskeletal, visual, digestive, respiratory, cardiovascular (minority), immune (minority).

**Tissue and cell level.** Nervous tissue (white matter) and skeletal muscle. See section 6 for suggested CL terms.

**Subcellular level.**
- Nucleus (GO:0005634) and nucleoplasm (GO:0005654).
- RNA polymerase II core complex (GO:0005665).

**Lateralization.** Findings are bilateral and symmetric (generalized hypotonia, bilateral white-matter loss).

---

## 8. Temporal Development

- **Onset:**
  - congenital or neonatal to infantile, sometimes prenatal (decreased fetal movements in 3/16);
  - NORD: *"Onset is typically during the infant and toddler years."*
- **Progression:**
  - typically a static encephalopathy with gradual development. Haijes found developmental Z-scores *"stable over time… without developmental catch-up or decline."*
  - hypotonia improves slowly, but endurance is reduced later in life.
- **Exceptions:**
  - episodic, infection-related temporary regression in 4 of 16 individuals;
  - developmental regression in 4 of 12 (Hansen);
  - slowly progressive cerebellar atrophy (Giacomini 2022);
  - marked regression at age 3 (Cao 2026).
- **Duration:** lifelong. The oldest reported individual was 31 years old (Evans 2022).
- **Stages and remission:** no formal staging. The only remission reported is partial and treatment-associated (levodopa response in Cao 2026).
- **Critical periods:** infancy, for feeding support, early therapy and seizure control (inferred).

---

## 9. Inheritance and Population

- **Prevalence:** unknown. NORD: *"As of 2025, about 99 people have been diagnosed worldwide"*, and there are *"less than 100 reports in the medical literature."* No incidence data exist.
- **Inheritance:** autosomal dominant. Most cases are de novo. One case was maternally inherited from a mother with mild learning difficulty (Hansen 2021).
- **Penetrance:** apparently high for de novo missense variants. Variants with milder effects, such as the C-terminal frameshift, may show reduced expressivity in carrier parents.
- **Expressivity:** highly variable, from mild delay to profound hypotonia with refractory epilepsy. Severity correlates with mechanism (dominant-negative worse than haploinsufficiency).
- **Not reported:**
  - anticipation (not expected, since this is not a repeat disorder);
  - germline mosaicism, although a theoretical recurrence risk applies to any de novo disorder;
  - founder effects;
  - a role for consanguinity;
  - carrier frequency (not applicable).
- **Demographics:**
  - cohorts are from Europe, North America, Italy and China;
  - NORD: no confirmed diagnoses in Africa, which likely reflects ascertainment, and no population predisposition;
  - both sexes are affected, and no sex bias has been reported.

---

## 10. Diagnostics

- **Diagnostic approach:** clinical suspicion followed by molecular confirmation. NORD: *"The diagnosis may be suspected in an infant or toddler with hypotonia, global developmental delay and abnormal MRI imaging."* There are no published diagnostic criteria.
- **Genetic testing:**
  - trio exome or genome sequencing is the method used in all published cases (GeneMatcher, Haijes 2019; trio WGS, Evans 2022; trio WES, Giacomini 2022);
  - multigene panels for hypotonia, epilepsy or neurodevelopmental disorders that include POLR2A are an alternative;
  - chromosomal microarray, karyotype, FISH, mtDNA and repeat-expansion testing are useful only for excluding differentials;
  - parental testing establishes whether a variant is de novo and supports ACMG PS2 classification.
- **Variant interpretation:**
  - in silico scores such as CADD do not discriminate here: Haijes found pathogenic and gnomAD variants alike scored above 20;
  - regional constraint ("desert" Z-score) and functional assays (yeast spot assays, HeLa α-amanitin-resistant RPB1 rescue) helped classify variants in research settings.
- **Imaging:** brain MRI may show delayed myelination, white-matter loss, ventriculomegaly, thin corpus callosum or cerebellar atrophy. NORD also lists periventricular cysts, brainstem atrophy and polymicrogyria.
- **EEG:** for seizures. Cao 2026 reported background slowing with epileptiform discharges.
- **Biochemical tests and muscle biopsy:** metabolic work-up is used for exclusion and was normal. Muscle biopsy is non-diagnostic.
- **Omics diagnostics:** no RNA-seq, proteomic, metabolomic or episignature tests are established.
- **Differential diagnosis:**
  - congenital myopathies and spinal muscular atrophy (profound hypotonia; tendon reflexes are preserved in NEDHIB);
  - POLR3-related hypomyelinating leukodystrophy and other hypomyelinating disorders;
  - Prader-Willi syndrome (infantile hypotonia with feeding difficulty);
  - Angelman, Rett and Fragile X syndromes, which NORD lists as similar disorders;
  - inborn errors of metabolism and mitochondrial disease.
- **Screening:** no newborn or carrier screening applies.

---

## 11. Outcome / Prognosis

- **Survival:** no survival, mortality or life-expectancy data exist. No deaths attributable to the disease were described in the material I reviewed. Adults up to 31 years have been reported.
- **Morbidity:** lifelong developmental and intellectual disability, motor impairment, reduced endurance, visual impairment, and refractory epilepsy in a subset.
- **Complications:**
  - recurrent respiratory infections;
  - failure to thrive;
  - status epilepticus;
  - possible tumour (one ependymoma);
  - adverse drug reactions, such as vigabatrin-associated MRI changes (Errichiello 2026, where causality is uncertain).
- **Recovery and prognostic factors:**
  - hypotonia improves partially;
  - the main prognostic factor is the variant mechanism: missense variants near the catalytic core predict greater severity than truncating variants (Haijes 2019);
  - severity scores (defined in Haijes 2019) are research tools only;
  - no prognostic biomarkers exist.
- **Quality-of-life studies:** none.

---

## 12. Treatment

**No disease-modifying therapy exists.** NORD: *"There is currently no genetic therapy available for direct treatment."*

**Supportive and symptomatic care** (NORD; suggested NCIT terms not verified):
- physical, occupational and speech therapy (NCIT physical therapy, occupational therapy and speech therapy concepts);
- feeding therapy and nutritional support, including gastrostomy where needed;
- management of gastroesophageal reflux;
- antiseizure medications;
- ophthalmologic care for strabismus;
- durable medical equipment;
- multidisciplinary follow-up: genetics, neurology, cardiology, pulmonology, GI, physiatry and developmental pediatrics.

**Drugs mentioned in the literature.**
- **Levodopa-benserazide, low dose (31.3 mg twice daily).** This produced marked motor and cognitive gains and resolved dystonic nodding in one child (Cao 2026, PMID 43047756). This is single-case evidence.
- **Vigabatrin.** Use was followed by reversible MRI changes during febrile status epilepticus in a 9-month-old (PMID 42033488). Causality is uncertain.

**Other therapies.**
- Gene, cell, RNA-based and targeted therapies: none.
- Allele-specific silencing of dominant-negative alleles is a theoretical approach and has not been reported.
- Pharmacogenomics: none known.

**Clinical trials.** No POLR2A-specific trial is known. The University of Pittsburgh natural history study and registry is per NORD; I did not retrieve its NCT number.

**Treatment response rates and outcomes:** not available.

---

## 13. Prevention

- **Primary prevention:** not applicable to de novo variants.
- **Genetic counselling:**
  - for de novo cases, recurrence risk is low but above population risk because of possible parental germline mosaicism (general principle);
  - for inherited cases, the risk is 50% (autosomal dominant).
- **Reproductive options:** prenatal diagnosis or preimplantation genetic testing are possible once the familial variant is known.
- **Secondary prevention:** early genomic diagnosis in infants with hypotonia, so that early intervention can start.
- **Tertiary prevention:**
  - prompt treatment of infections and fever, given infection-associated regression and status epilepticus;
  - management of aspiration and reflux;
  - routine vision checks.
- **Vaccination:** no disease-specific vaccine. Routine immunization is reasonable given the recurrent respiratory infections (inferred, no evidence).

---

## 14. Other Species / Natural Disease

- **Naturally occurring disease:** I found no POLR2A-associated developmental disease in animals. An OMIA search could not be performed.
- **Orthologues:**
  - mouse *Polr2a*;
  - zebrafish *polr2a*;
  - *Drosophila* RpII215;
  - *S. cerevisiae* RPO21/RPB1.
  - NCBI Gene IDs for these orthologues were not retrieved.
- **Conservation:** RPB1 is extremely conserved. In the Pol II core, about 50% of residues are identical and about 20% are highly similar between human and yeast (Haijes 2019).
- **Livestock GWAS:** a POLR2A association with body size in Dezhou donkeys (PMID 39079013) is a growth-trait GWAS, not a disease model.
- **Zoonotic potential:** not applicable.

---

## 15. Model Organisms

| Model | Type | Findings | Source |
|---|---|---|---|
| *S. cerevisiae* rpo21/rpb1 equivalents of patient variants | Genetic knock-in on plasmid | In wild-type yeast, normal growth for all but p.Leu1124Pro (yeast Leu1101Pro). In Δdst1/Δsub1 backgrounds, 4 of 6 variants showed aberrant growth, plus galactose read-through defects and mycophenolic-acid sensitivity, *"suggestive of reduced transcriptional fidelity"* | Haijes 2019 |
| Yeast spot assays, 15 alleles | Genetic | Classified transcription versus protein defects for individuals in the Hansen cohort | Hansen 2021 |
| HeLa FRT cells with dox-inducible GFP-RPB1 (α-amanitin-resistant); endogenous RPB1 inhibited with α-amanitin | In vitro (human cell line) | Viability *"grossly reduced"* for p.Thr736Met, p.Ser755del, p.Lys812* and p.Leu1124Pro; no effect for p.Ile457Thr, p.Asn531Ser, p.Asn1251Ser or p.Arg1603His; TFIIS binding unchanged | Haijes 2019 |
| Mass spectrometry of RPB1 interactomes | In vitro | Missense variants assemble into Pol II; truncated RPB1 binds only RPABC3 | Haijes 2019 |
| Mouse, zebrafish, *Drosophila*, patient iPSCs or organoids | — | **I found no published disease model** in the literature searches I ran | — |

**Limitations.**
- Yeast and HeLa cells cannot reproduce the neurodevelopmental, myelination or muscle phenotypes. Haijes notes they *"may not fully recapitulate the complex developmental disease."*
- Some pathogenic variants, such as p.Ile457Thr, showed no HeLa phenotype, so these assays have limited sensitivity.

**Research applications.** These models allow variant classification and dissection of elongation and fidelity defects. A gap remains: vertebrate knock-in models are needed to test the dominant-negative elongation hypothesis in neurons and oligodendrocytes.

**Model resources:** MGI, ZFIN, FlyBase and SGD for the orthologues. Specific allele records were not retrieved.

---

## Key References

1. Haijes HA, et al. De Novo Heterozygous POLR2A Variants Cause a Neurodevelopmental Syndrome with Profound Infantile-Onset Hypotonia. *Am J Hum Genet.* 2019;105(2):283–301. PMID 31353023; PMCID PMC6699192; DOI 10.1016/j.ajhg.2019.06.016. [Author manuscript, ORA](https://ora.ox.ac.uk/objects/uuid:a38bf334-3015-4933-8183-455bc0548681)
2. Hansen AW, …, Gibbs RA. Germline mutation in POLR2A: a heterogeneous, multi-systemic developmental disorder characterized by transcriptional dysregulation. *HGG Adv.* 2021;2(1):100014. PMID 33665635; DOI 10.1016/j.xhgg.2020.100014. [PMC7928427](https://pmc.ncbi.nlm.nih.gov/articles/PMC7928427)
3. Evans DR, et al. Complex Autism Spectrum Disorder with Epilepsy, Strabismus and Self-Injurious Behaviors in a Patient with a De Novo Heterozygous POLR2A Variant. *Genes (Basel).* 2022;13(3):470. PMID 35328024. [PMC8955435](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8955435/)
4. Giacomini T, et al. De novo POLR2A p.(Ile457Thr) variant associated with early-onset encephalopathy and cerebellar atrophy. *Brain Dev.* 2022;44(7):480–485. PMID 35461703; DOI 10.1016/j.braindev.2022.04.002.
5. Paparella R, et al. Posterior fossa ependymoma in neurodevelopmental syndrome caused by a de novo germline pathogenic POLR2A variant. *Am J Med Genet A.* 2022;188(9):2796–2802. PMID 35689525 (erratum PMID 36543156). [PMC9543264](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9543264/)
6. Errichiello G, et al. Brain MRI markers of vigabatrin-associated neurotoxicity during hyperpyrexia-triggered focal status epilepticus. *Pediatr Radiol.* 2026;56(7):1592–1596. PMID 42033488.
7. Cao Z, …, Shi X. De novo POLR2A p.(L1127F) variant presenting with neurodevelopmental regression and dystonia, with favorable response to low-dose dopamine therapy. *Front Neurosci.* 2026;20. PMID 43047756; DOI 10.3389/fnins.2026.1997676. [Link](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2026.1997676/full)
8. NORD. POLR2A-Related Disorder (last updated 23 April 2025). https://rarediseases.org/rare-diseases/polr2a-related-disorder/
9. NCBI Gene 5430 (POLR2A). https://www.ncbi.nlm.nih.gov/gene/5430
10. PhenomeGene / Human Disease Genes, POLR2A professionals page. https://humandiseasegenes.nl/polr2a/professionals

**A note on GeneCards.** GeneCards also lists "alacrima, achalasia, and impaired intellectual development syndrome" under POLR2A ([GeneCards](https://www.genecards.org/card/POLR2A)). I could not confirm this association in the primary literature. It is probably a text-mining artefact and should not be entered without checking.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 12 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:36543156` (2 mentions) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 71 |
| Resolved | 68 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 40 |
| Terms named correctly | 26 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032829` (2 mentions) - the report calls it "MONDO"; MONDO calls it **neurodevelopmental disorder with hypotonia and variable intellectual and behavioral abnormalities**
- `HP:0033409` (1 mention) - the report calls it "verify"; HP calls it **Elevated urinary 2-hydroxybutyric acid**
- `HP:0007663` (1 mention) - the report calls it "verify"; HP calls it **Reduced visual acuity**
- `HP:0033725` (1 mention) - the report calls it "verify"; HP calls it **Thin corpus callosum**
- `HP:0000692` (1 mention) - the report calls it "verify"; HP calls it **Tooth malposition**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003202` (1 mention) - the report calls it "Muscle atrophy"; HP calls it **Skeletal muscle atrophy**, and lists "Muscle atrophy" among its other names
- `HP:0003546` (1 mention) - the report calls it "Decreased endurance / exercise intolerance"; HP calls it **Exercise intolerance**
- `HP:0001250` (1 mention) - the report calls it "Seizures / epilepsy"; HP calls it **Seizure**, and lists "Seizures" among its other names
- `HP:0012443` (1 mention) - the report calls it "Abnormal brain MRI"; HP calls it **Abnormal brain morphology**
- `HP:0001272` (1 mention) - the report calls it "Cerebellar abnormality / atrophy"; HP calls it **Cerebellar atrophy**
- `HP:0001627` (1 mention) - the report calls it "Cardiac abnormality"; HP calls it **Abnormal heart morphology**, and lists "Cardiac abnormality" among its other names
- `HP:0002715` (1 mention) - the report calls it "Immune abnormality"; HP calls it **Abnormality of the immune system**, and lists "Immunological abnormality" among its other names
- `HP:0000119` (1 mention) - the report calls it "Urogenital findings"; HP calls it **Abnormality of the genitourinary system**, and lists "Urogenital anomalies" among its other names
- `UBERON:0001134` (1 mention) - the report calls it "skeletal muscle"; UBERON calls it **skeletal muscle tissue**, and lists "skeletal muscle" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `EXT_ID`.