---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-24T04:43:50.322429'
end_time: '2026-11-24T04:50:23.553279'
duration_seconds: 393.23
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Intellectual Developmental Disorder, Autosomal Dominant 65
  mondo_id: MONDO:0023657
  category: Mendelian
  causal_genes: KDM4B
  omim_id: OMIM:619320
  synonyms: MRD65; mental retardation, autosomal dominant 65
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
  num_turns: 15
  total_cost_usd: 0.9346227400000001
  session_id: 5f98bd7a-5b67-4013-b060-002214b195bb
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 31
  retrieval_calls: 29
  assistant_text_blocks: 2
citation_count: 10
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 6
  quotes_valid: 6
  relevance_assessed: 9
  on_topic: 4
  off_topic: 1
  off_topic_references:
  - PMID:42985254
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 77
  verified: 74
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 41
  labels_matching: 26
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0023657
    reported_labels:
    - MONDO
    ontology_label: intellectual developmental disorder, autosomal dominant 65
  - term_id: HP:0025100
    reported_labels:
    - Hippocampal dysgenesis
    ontology_label: Abnormal hippocampus morphology
  - term_id: HP:0000582
    reported_labels:
    - 'Eyes and eyebrows: upslanted'
    ontology_label: Upslanted palpebral fissure
  - term_id: HP:0000322
    reported_labels:
    - 'Philtrum, lips and mouth: short'
    ontology_label: Short philtrum
  - term_id: NCBITaxon:10090
    reported_labels:
    - Kdm4b
    - 'Orthologs: mouse *Kdm4b'
    ontology_label: Mus musculus
  labels_variant: 10
  unresolvable_prefixes:
  - OMIM
  - EXT_ID
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Developmental Disorder, Autosomal Dominant 65
- **MONDO ID:** MONDO:0023657 (if available)
- **Causal gene(s):** KDM4B
- **OMIM:** OMIM:619320
- **Synonyms:** MRD65; mental retardation, autosomal dominant 65
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Intellectual Developmental Disorder, Autosomal Dominant 65** covering all of the
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

Both direct fetches were blocked, so I'm trying Europe PMC and the open-access copies of the papers.

**Intellectual Developmental Disorder, Autosomal Dominant 65 (MRD65; OMIM:619320; MONDO:0023657): research report**

**Scope and limitations.** This report covers the disorder caused by heterozygous variants in **KDM4B** (lysine demethylase 4B, also called JMJD2B; HGNC:29136; gene OMIM 609765; NCBI Gene 23030; chromosome 19p13.3). MedGen confirmed that MONDO:0023657 is linked to OMIM:619320 and KDM4B.

The full texts of the key papers were blocked: PMC, Wiley and Europe PMC full text returned bot checks or 403/500 errors. So the clinical and molecular detail below comes from abstracts (via the Europe PMC API), MedGen/OMIM-derived records and UniProt.

- **Not retrieved:** per-patient variant tables, HGVS for most variants, and per-feature frequencies. These are marked "not retrieved" rather than filled from memory.
- **Paraphrased quotes:** the retrieval tools limited verbatim quoting. Quotes marked "(abstract)" are exact short fragments; longer passages are paraphrased.

---

## 1. Disease information

**Overview.** MRD65 is a neurodevelopmental chromatinopathy. MedGen, citing OMIM, states it "is characterized by delayed motor and speech acquisition" ([MedGen 1787923](https://www.ncbi.nlm.nih.gov/medgen/1787923)). The rest of the OMIM-derived definition, paraphrased:
- intellectual development is variably impaired;
- behavioral abnormalities and dysmorphic facial features are present;
- brain imaging may be normal or may show cerebellar hypoplasia, poor corpus callosum development, a dysmorphic hippocampus or polymicrogyria;
- feeding difficulties, hypotonia and seizures may occur.

UniProt O94953 gives a matching description: "delayed motor and speech acquisition, variably impaired intellectual development, behavioral abnormalities, and dysmorphic facial features" ([UniProt O94953](https://rest.uniprot.org/uniprotkb/O94953.txt)).

**Founding publication.** Duncan AR et al. *Am J Hum Genet* 2020;107(6):1170–1177, PMID **33232677**, DOI 10.1016/j.ajhg.2020.11.001 ([PMC7820620](https://pmc.ncbi.nlm.nih.gov/articles/PMC7820620)). The authors conclude that "variants in KDM4B are associated with GDD/ intellectual disability and neuroanatomical defects" (abstract) and propose that the disorder is a chromatinopathy.

**Identifiers**

| System | ID |
|---|---|
| OMIM (phenotype) | 619320 |
| OMIM (gene) | 609765 |
| MONDO | MONDO:0023657 |
| MedGen | UID 1787923; CUI C5543371 |
| HGNC | HGNC:29136 |
| GenCC | "Strong" classification; submitted as OMIM:619320, evaluated November 2023 ([GenCC](https://search.thegencc.org/genes/HGNC:29136)) |
| PanelApp Australia | Green (high evidence) on the intellectual disability panel; monoallelic ([PanelApp](https://panelapp-aus.org/panels/250/gene/KDM4B)) |
| Orphanet | No disease-specific ORPHA code found. It most likely falls under the generic rare ID groupings; not verified. |
| ICD-10 / ICD-11 | No specific code. The general codes are F7x (ICD-10) and 6A00 (ICD-11) for disorders of intellectual development. |
| MeSH | No specific heading; the umbrella term is "Intellectual Disability" (D008607). |

**Synonyms:** MRD65; mental retardation, autosomal dominant 65; KDM4B-related neurodevelopmental disorder (descriptive name).

**Source type.** All information is aggregated from case series and case reports of individual patients: one multicenter cohort, one biallelic case and one prenatal case. There are no EHR-scale or registry data.

---

## 2. Etiology

**Causal factors.**
- The cause is genetic: heterozygous, mostly de novo but sometimes inherited, variants in KDM4B.
- The original cohort comprised "nine individuals with mono-allelic de novo or inherited variants in KDM4B" (paraphrase of PMID 33232677 abstract). A secondary search summary mentioned eight more individuals with rare missense variants found through MatchMaker Exchange; this could not be confirmed from the full text.
- A 2024 report states that loss-of-function heterozygous KDM4B variants cause MRD65, and that only 23 heterozygous patients had been reported at the time (Takada S et al., *Clin Genet* 2024;105(1):72–76, PMID **37526414**).

**Risk factors.**
- *Genetic:* a pathogenic KDM4B variant, or having an affected or carrier parent. At least one family shows inheritance from a mildly affected parent (PMID 37526414).
- *Environmental:* none are known.

**Protective factors and modifiers:** none are reported.

**Gene–environment interactions:** none are reported. A theoretical point (inference, not a disease study): KDM4B is a 2-oxoglutarate/Fe²⁺-dependent dioxygenase that is inhibited by L-2-hydroxyglutarate (UniProt). Its activity therefore depends on cellular metabolic state, but no disease relevance has been shown. The Comparative Toxicogenomics Database (CTD) was not searched.

---

## 3. Phenotypes

The features below are the HPO annotations listed in MedGen for OMIM:619320 (46 entries) ([MedGen](https://www.ncbi.nlm.nih.gov/medgen/1787923)). Abstract-level frequencies come from Duncan et al. 2020 (n=9). HPO IDs are my suggestions, mapped from the term names; MedGen displayed CUIs, not HP IDs.

**Neurodevelopmental, neurological and behavioral features**

| Phenotype | Suggested HPO | Frequency / notes |
|---|---|---|
| Global developmental delay | HP:0001263 | 9/9; "language and motor skills most affected" (PMID 33232677) |
| Intellectual disability (variable) | HP:0001249 | Common; severity variable |
| Delayed speech and language development | HP:0000750 | Most affected domain |
| Delayed gross motor development | HP:0002194 | Common |
| Delayed fine motor development | HP:0010862 | Reported |
| Hypotonia | HP:0001252 | Variable; hypotonic face (HP:0000297) in the biallelic case |
| Seizure | HP:0001250 | 3/9 (33%) |
| Infantile spasms | HP:0012469 | Reported (MedGen) |
| Ataxia / clumsiness | HP:0001251 / HP:0002312 | Reported |
| Autistic behavior | HP:0000729 | Reported |
| ADHD | HP:0007018 | Reported |
| Aggressive behavior | HP:0000718 | Reported |
| Compulsive behaviors | HP:0000722 | Reported |
| Feeding difficulties | HP:0011968 | Variable (OMIM/UniProt) |

**Brain imaging features.** Brain imaging was abnormal in 4/9 (44%), ranging "from agenesis of the corpus callosum with hydrocephalus to cystic formations, abnormal hippocampi, and polymicrogyria" (PMID 33232677).

| Phenotype | Suggested HPO | Notes |
|---|---|---|
| Agenesis of the corpus callosum | HP:0001274 | Also seen prenatally (PMID 38270710) |
| Noncommunicating hydrocephalus | HP:0010953 | |
| Hippocampal dysgenesis | HP:0025100 | |
| Polymicrogyria | HP:0002126 | |
| Cerebellar hypoplasia | HP:0001321 | OMIM definition |
| Ventriculomegaly | HP:0002119 | Fetal case (PMID 38270710) |

**Craniofacial and limb features.** All 9 individuals in Duncan et al. had dysmorphic features, but no single feature was consistent. Listed features include:
- Head and face: turricephaly (HP:0000262), prominent metopic ridge (HP:0005487), narrow forehead (HP:0000341), round face (HP:0000311), facial asymmetry (HP:0000324).
- Eyes and eyebrows: upslanted (HP:0000582) or narrow (HP:0045025) palpebral fissures, synophrys (HP:0000664), thin eyebrows (HP:0045074).
- Nose: wide nasal bridge (HP:0000431), bulbous nose (HP:0000414), anteverted nares (HP:0000463).
- Philtrum, lips and mouth: short (HP:0000322) or long (HP:0000343) philtrum, tented upper lip (HP:0010804), thick upper lip vermilion (HP:0000215), downturned mouth corners (HP:0002714).
- Jaw and ears: micrognathia (HP:0000347), low-set (HP:0000369), posteriorly rotated (HP:0000358) and large (HP:0000400) ears.
- Hair: low posterior hairline (HP:0002162), sparse hair (HP:0008070).
- Hands and feet: fifth-finger clinodactyly (HP:0004209; highlighted in PMID 37526414), single transverse palmar crease (HP:0000954), short palm (HP:0004279), short foot (HP:0001773).

**Characteristics**
- *Onset:* congenital or infantile; brain malformations can be detected prenatally (PMID 38270710).
- *Severity:* variable, from mild (a heterozygous carrier mother) to more severe. The biallelic case was more severely affected than her mother (PMID 37526414).
- *Progression:* appears static, as expected for a neurodevelopmental disorder; no natural history data exist.
- *Quality of life:* no EQ-5D or SF-36 data. Impact is expected through ID, communication deficits, behavior and epilepsy.

---

## 4. Genetic and molecular information

**Gene:** KDM4B, at 19p13.3. It encodes lysine-specific demethylase 4B (EC 1.14.11.66), 1,096 amino acids, located in the nucleus ([UniProt O94953](https://rest.uniprot.org/uniprotkb/O94953.txt)).

**Domains (UniProt)**

| Domain | Residues |
|---|---|
| JmjN | 15–57 |
| JmjC (catalytic; Fe²⁺ ligands His189, Glu191, His277; 2-oxoglutarate-binding residues 133, 199, 207, 242) | 146–309 |
| PHD-type 1 | 731–789 |
| C2HC pre-PHD | 794–827 |
| PHD-type 2 | 850–907 |
| Tudor 1 | 917–974 |
| Tudor 2 | 975–1031 |

**Variants with retrieved specifics**

| Variant | Type | Domain | Origin / classification | Source |
|---|---|---|---|---|
| p.Leu220Pro | Missense | JmjC | MRD65 (UniProt) | PMID 33232677 |
| p.Arg222Trp | Missense | JmjC | MRD65 | PMID 33232677 |
| p.His768Arg | Missense | PHD1 | MRD65 | PMID 33232677 |
| p.Pro1095Leu | Missense | C-terminus | Uncertain significance | PMID 33232677 |
| NM_015015.3:c.1384_1394delinsGGG, p.(Leu462Glyfs\*43) | Frameshift, exon 12 of 23; predicted NMD | — | Homozygous in proband; heterozygous in the less affected mother | PMID 37526414 |
| NM_015015.3:c.2889_2890ins (exact insertion not retrieved) | Insertion | — | De novo in a fetus with ACC and ventriculomegaly; "significantly reduced expression of the mutant protein" in 293T cells | PMID 38270710 (Zhao X et al., *Mol Biol Rep* 2024;51:188) |

The Duncan cohort also included truncating (LoF) variants, but their HGVS could not be retrieved.

- **ClinVar / ACMG:** classifications were not retrieved; ClinVar should be checked directly.
- **Allele frequency:** gnomAD data were not retrieved. The variants are described as rare. Constraint metrics (pLI/LOEUF) were not retrieved.
- **Origin:** germline (de novo or inherited). Somatic KDM4B changes occur in cancer but are unrelated to MRD65.
- **Functional consequence:**
  - Heterozygous loss of function / haploinsufficiency is supported by truncating variants, NMD prediction, reduced protein from the fetal insertion, and the Kdm4b+/- mouse phenotype.
  - The mechanism of the missense variants in the catalytic JmjC or PHD domains (hypomorphic vs dominant-negative) is not established.
  - The biallelic case suggests a dosage effect: two LoF alleles give a more severe phenotype than one.
- **Modifier genes:** none reported.

**Epigenetic information.**
- KDM4B is a "Histone demethylase that specifically demethylates 'Lys-9' of histone H3" and is "Only able to demethylate trimethylated H3 'Lys-9'" (UniProt). There is also a GO annotation for H3K36 demethylase activity (GO:0051864, IDA), but it conflicts with UniProt's own function text.
- No DNA-methylation episignature specific to MRD65 was found.

**Chromosomal abnormalities.**
- KDM4B lies in 19p13.3. Gains of 19p13.3–p13.2 have been reported (PMID 42985254, 2026; not assessed), but there is no established link to the KDM4B dosage phenotype.
- DECIPHER was not queried.

---

## 5. Environmental information

No environmental, lifestyle or infectious factors are known; this section is not applicable.

---

## 6. Mechanism and pathophysiology

**Causal chain** (steps marked [inferred] have not been directly shown in patients)

1. A germline heterozygous KDM4B variant (truncating, or missense in JmjC/PHD) **leads to** reduced functional KDM4B protein. This is shown for the NMD-predicted frameshift and for the fetal insertion with reduced protein (PMIDs 37526414, 38270710); for missense variants it is [inferred].
2. Reduced KDM4B **results in** less demethylation of H3K9me3, and therefore excess repressive heterochromatin marks at target loci in neural progenitors and neurons. This is [inferred] for patients; the enzymatic function itself is established (UniProt), and the neuronal knockout paper says JMJD2B "regulates gene expression through demethylation of H3K9me3" (PMID 27023172).
3. Altered H3K9me3 **leads to** dysregulated transcription of neurodevelopmental genes [inferred; no transcriptomic data from patient tissue].
4. This then branches:
   - **4a.** During brain development, disturbed progenitor proliferation, migration or axon guidance **results in** reduced brain volume, a smaller dentate gyrus, partial corpus callosum agenesis and ventriculomegaly. This is shown in Kdm4b+/- mice: "the total brain volume was significantly reduced" with "partial agenesis of the corpus callosum, and ventriculomegaly" (PMID 33232677). In patients it corresponds to ACC, hydrocephalus, hippocampal dysgenesis and polymicrogyria.
   - **4b.** In postmitotic neurons, loss of KDM4B **leads to** defective dendritic spine maturation, with "an increase in total spine number, but a decrease in mature spines, in the CA1 region of the hippocampus" (PMID 27023172, neuron-specific knockout mice).
5. Structural and synaptic defects **result in** the clinical features. The mouse findings (hyperactivity, working-memory deficits and "spontaneous epileptic-like seizures"; PMID 27023172) match the human GDD/ID, ADHD, autistic features and seizures. The link between mouse and human is [inferred].

**Checklist of other mechanism categories**
- *Pathways:* chromatin regulation, specifically the Reactome "HDMs demethylate histones" pathway. No signaling cascade has been specifically implicated.
- *Protein dysfunction:* loss of a 2-oxoglutarate/Fe²⁺-dependent dioxygenase activity.
- *Metabolic, immune and tissue-damage mechanisms:* none shown in this disorder. Separately, Kdm4b ablation affects antiviral immunity via demethylation of cGAS (PMID 40595456; summary-level evidence only), with no established relevance to MRD65.
- *Omics, single-cell and CRISPR data:* none specific to MRD65.

**Suggested GO terms**
- histone H3K9 demethylase activity (GO:0032454)
- histone H3K9me3 demethylase activity (GO:0140684)
- chromatin organization (GO:0006325)
- regulation of DNA-templated transcription (GO:0006355)
- forebrain development (GO:0030900)
- hippocampus development (GO:0021766)
- corpus callosum development (GO:0022038)
- dendritic spine maturation (GO:0097062)

**Suggested CL terms:** neuron (CL:0000540), neural progenitor cell (CL:0011020), hippocampal granule cell of the dentate gyrus (CL:0001033), CA1 pyramidal neuron (CL:1001571).

---

## 7. Anatomical structures affected

- **Primary organ:** the brain (UBERON:0000955). Affected structures include:
  - corpus callosum (UBERON:0002336)
  - hippocampus and dentate gyrus (UBERON:0001954, UBERON:0001885)
  - cerebral cortex (UBERON:0000956), with polymicrogyria
  - cerebellum (UBERON:0002037)
  - lateral ventricles (UBERON:0002285)
- **Secondary systems:** craniofacial (head, UBERON:0000033), hands and feet (dysmorphisms), and feeding.
- **Subcellular level:** the nucleus (GO:0005634) and chromatin (GO:0000785).
- **Lateralization:** midline structures such as the corpus callosum; facial asymmetry has been reported. Otherwise bilateral.

---

## 8. Temporal development

- **Onset:** congenital; structural changes are detectable prenatally (fetal ACC and ventriculomegaly, PMID 38270710). Developmental delay becomes evident in infancy.
- **Course:** a chronic, lifelong, static neurodevelopmental disorder. There are no staging or natural history studies and no remission.
- **Critical period:** the prenatal and early postnatal period of brain development [inferred]. Early intervention for speech and motor skills is the window for intervention.

---

## 9. Inheritance and population

- **Inheritance:** autosomal dominant. Most variants are de novo; some are inherited from mildly affected or apparently unaffected parents (PMID 33232677).
- **Biallelic case:** one human biallelic (homozygous) case exists, with a more severe phenotype than the heterozygous mother (PMID 37526414, a Chilean–Japanese collaboration). The authors argue that the "embryonic lethality in male mice" seen in homozygous knockout mice does not necessarily apply to humans.
- **Penetrance and expressivity:** penetrance appears incomplete or mild in some carriers, and expressivity is variable.
- **Not reported:** anticipation, germline mosaicism, founder effects, consanguinity effects (beyond the biallelic case), carrier frequency, sex ratio.
- **Prevalence:** unknown and extremely rare, with about 23–25 published patients by 2023–2024 (PMID 37526414).

---

## 10. Diagnostics

- **Genetic testing:** first-tier exome or genome sequencing, or an ID/NDD gene panel that includes KDM4B (Green in PanelApp Australia).
  - Variants are mostly de novo, so trio analysis helps.
  - Chromosomal microarray detects 19p13.3 copy-number changes.
  - Prenatal exome sequencing can identify cases with ACC or ventriculomegaly (PMID 38270710).
- **Imaging:** brain MRI (abnormal in about 44%) and fetal ultrasound or MRI.
- **Electrophysiology:** EEG for seizures and infantile spasms.
- **Not available:** biochemical biomarkers, a validated episignature and formal clinical criteria.
- **Differential diagnosis:**
  - other chromatinopathies, for example KDM5C, KDM6A/KDM6B, KMT2D and EHMT1 disorders;
  - other causes of syndromic ID with corpus callosum agenesis;
  - 19p13.3 microdeletion syndromes.
  Distinguishing these requires molecular testing.
- **Screening:** no newborn screening. Cascade testing of parents is advised because of inherited, variably expressed alleles.

---

## 11. Outcome and prognosis

- **Mortality and life expectancy:** no data; no early mortality has been reported.
- **Morbidity:** lifelong ID, speech and motor disability, behavioral disorders and epilepsy (about one-third).
- **Complications:** hydrocephalus (which may need shunting), seizures and feeding problems.
- **Prognostic factors:** not established. Biallelic LoF alleles and structural brain anomalies may predict a more severe course [inferred].

---

## 12. Treatment

There is no disease-specific or targeted therapy, and no trials registered on ClinicalTrials.gov for KDM4B or MRD65 were identified. Management is supportive:

| Intervention | Suggested NCIT term |
|---|---|
| Speech/language therapy | C17646 |
| Physical therapy | C15336 |
| Occupational therapy | C15339 |
| Special education and developmental intervention | — |
| Antiseizure medication | C264 (anticonvulsant agent) |
| Behavioral therapy / ADHD management | — |
| Feeding support | — |
| Neurosurgical CSF shunt for hydrocephalus | Ventriculoperitoneal shunt procedure |

- **Pharmacogenomics:** not applicable.
- **Gene, RNA or cell therapy:** none. KDM4 inhibitors exist only as oncology research tools; they would be counterproductive in a loss-of-function disorder.

---

## 13. Prevention

- **Primary prevention:** not applicable.
- **Genetic counseling:**
  - For de novo cases, recurrence risk is low but includes possible germline mosaicism (an empiric risk of about 1%; a general principle, not KDM4B-specific data).
  - For inherited cases, the risk to offspring is 50%, with variable expressivity.
  - Where both parents are carriers, biallelic offspring are possible (PMID 37526414).
- **Prenatal and preimplantation options:** prenatal or preimplantation genetic testing for a known familial variant. Fetal ACC or ventriculomegaly should prompt sequencing that includes KDM4B (PMID 38270710).
- **Tertiary prevention:** seizure surveillance, hydrocephalus monitoring and early developmental intervention.

---

## 14. Other species and natural disease

- No naturally occurring KDM4B disease was found in animals (OMIA was not queried).
- Orthologs: mouse *Kdm4b* (NCBITaxon:10090), zebrafish, and a *Drosophila* Kdm4 family member (Kdm4B). Ortholog IDs were not retrieved.
- Not zoonotic.

---

## 15. Model organisms

| Model | Key findings | Recapitulation | Source |
|---|---|---|---|
| Kdm4b+/- heterozygous mouse (MRI-based neuroanatomy) | Reduced total brain volume, smaller dentate gyrus, partial corpus callosum agenesis, ventriculomegaly | Good for the structural brain features (ACC, hydrocephalus, hippocampal anomalies) | PMID 33232677 |
| Neuron-specific Jmjd2b knockout (floxed exon 5 × Tau-Cre) | Hyperactivity, "sustained hyperactivity in a novel environment", working-memory deficits, spontaneous epileptic-like seizures, immature CA1 spines | Behavioral, cognitive and seizure features (ADHD, ID, epilepsy) | Fujiwara K et al., *Transl Psychiatry* 2016;6:e766, PMID 27023172 |
| Homozygous Kdm4b knockout mouse | Embryonic lethality reported in males | Corresponds to the biallelic state; human biallelic survival differs | Cited in PMID 37526414 |
| 293T cells expressing the fetal insertion variant | Reduced mutant protein | Supports LoF | PMID 38270710 |

- **Limitations:** the mouse models do not capture the facial dysmorphism or the missense-specific mechanisms. The neuronal knockout is complete (homozygous), not heterozygous.
- **Resources:** MGI (OMIM:619320 page at [informatics.jax.org](https://www.informatics.jax.org/disease/OMIM:619320)) and IMPC/KOMP for Kdm4b alleles; not queried in detail.

---

### Key evidence (PMIDs)
- **33232677**: Duncan et al. 2020, *AJHG*. Founding cohort (n=9) and the Kdm4b+/- mouse.
- **37526414**: Takada et al. 2024, *Clin Genet*. Biallelic frameshift p.(Leu462Glyfs\*43); about 23 prior heterozygous patients.
- **38270710**: Zhao et al. 2024, *Mol Biol Rep*. Fetal de novo insertion with ACC and ventriculomegaly; reduced protein.
- **27023172**: Fujiwara et al. 2016, *Transl Psychiatry*. Neuron-specific Jmjd2b knockout: spine maturation defects, hyperactivity, memory deficits, seizures.

### Sources
- [MedGen 1787923](https://www.ncbi.nlm.nih.gov/medgen/1787923)
- [PMC7820620 (Duncan 2020)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7820620)
- [PubMed 37526414](https://www.pubmed.gov/37526414/)
- [PMC4872455 (Fujiwara 2016)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4872455/)
- [UniProt O94953](https://rest.uniprot.org/uniprotkb/O94953.txt)
- [GenCC HGNC:29136](https://search.thegencc.org/genes/HGNC:29136)
- [PanelApp Australia KDM4B](https://panelapp-aus.org/panels/250/gene/KDM4B)
- [MGI OMIM:619320](https://www.informatics.jax.org/disease/OMIM:619320)
- [GeneCards KDM4B](https://www.genecards.org/card/KDM4B)
- [Europe PMC REST API](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:33232677&resultType=core&format=json)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 6 |
| Quoted claims found in source | 6 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 9 |
| On topic | 4 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:42985254` (1 mention) - Partial trisomy 19p13.3-p13.2 from antenatal diagnosis to 7-year follow-up: case report and literature review.
  - shared terms: patient

Weighed against this report's own most characteristic terms: `kdm4b`, `variant`, `brain`, `biallelic`, `heterozygous`, `disorder`, `seizure`, `ventriculomegaly`, `fetal`, `gene`, `acc`, `mrd65`, `callosum`, `corpus`, `novo`, `hydrocephalus`, `affected`, `mouse`, `patient`, `behavioral`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 77 |
| Resolved | 74 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 41 |
| Terms named correctly | 26 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 10 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0023657` (3 mentions) - the report calls it "MONDO"; MONDO calls it **intellectual developmental disorder, autosomal dominant 65**
- `HP:0025100` (1 mention) - the report calls it "Hippocampal dysgenesis"; HP calls it **Abnormal hippocampus morphology**
- `HP:0000582` (1 mention) - the report calls it "Eyes and eyebrows: upslanted"; HP calls it **Upslanted palpebral fissure**
- `HP:0000322` (1 mention) - the report calls it "Philtrum, lips and mouth: short"; HP calls it **Short philtrum**
- `NCBITaxon:10090` (1 mention) - the report calls it "Kdm4b", "Orthologs: mouse *Kdm4b"; NCBITaxon calls it **Mus musculus**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001249` (1 mention) - the report calls it "Intellectual disability (variable)"; HP calls it **Intellectual disability**
- `HP:0001274` (1 mention) - the report calls it "Agenesis of the corpus callosum"; HP calls it **Agenesis of corpus callosum**, and lists "Agenesis of the corpus callosum" among its other names
- `HP:0000262` (1 mention) - the report calls it "Head and face: turricephaly"; HP calls it **Turricephaly**
- `HP:0000431` (1 mention) - the report calls it "Nose: wide nasal bridge"; HP calls it **Wide nasal bridge**
- `HP:0000347` (1 mention) - the report calls it "Jaw and ears: micrognathia"; HP calls it **Micrognathia**, and lists "Mandibular micrognathia" among its other names
- `HP:0002162` (1 mention) - the report calls it "Hair: low posterior hairline"; HP calls it **Low posterior hairline**
- `GO:0140684` (1 mention) - the report calls it "histone H3K9me3 demethylase activity"; GO calls it **histone H3K9me2/H3K9me3 demethylase activity**, and lists "histone H3K9me3 demethylase activity" among its other names
- `GO:0097062` (1 mention) - the report calls it "dendritic spine maturation"; GO calls it **dendritic spine maintenance**
- `UBERON:0000955` (1 mention) - the report calls it "Primary organ:** the brain"; UBERON calls it **brain**, and lists "the brain" among its other names
- `GO:0005634` (1 mention) - the report calls it "Subcellular level:** the nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCBITaxon:10090` - called "Kdm4b", "Orthologs: mouse *Kdm4b"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `EXT_ID`.