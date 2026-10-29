---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-10-28T18:35:49.769702'
end_time: '2026-10-28T18:55:04.417470'
duration_seconds: 1154.65
template_file: templates/disease_pathophysiology_research.md
template_sha: f452f0a9c7e3536175154b9683c45663f686f283
template_variables:
  disease_name: Melanotic Neuroectodermal Tumor of Infancy
  mondo_id: MONDO:0002072
  category: ''
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: MNTI; infantile melanotic neuroectodermal neoplasm; melanotic Progonoma;
    melanotic neuroectodermal tumor (morphologic abnormality); melanotic neuroectodermal
    tumor of infancy (morphologic abnormality); melanotic neuroectodermal tumour (morphologic
    abnormality); melanotic neuroectodermal tumour of infancy (morphologic abnormality);
    pigmented neuroectodermal tumor
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
  web_search_requests: 26
  num_turns: 105
  total_cost_usd: 12.465065249999991
  session_id: 160d7d60-5df1-4414-823d-8d39af7f02ca
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 27
reference_validation:
  total_references: 40
  verified: 40
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 38
  quotes_valid: 9
  quotes_unsupported: 29
  unsupported_quote_references:
  - PMID:41522382
  - PMID:34359769
  - PMID:41445906
  - PMID:38681460
  - PMID:40278957
  - PMID:29768520
  - PMID:35400932
  - PMID:42527893
  - PMID:26122804
  - PMID:34094962
  - PMID:20080455
  - PMID:25936939
  relevance_assessed: 40
  on_topic: 30
  off_topic: 1
  off_topic_references:
  - GEO:GSE28875
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 68
  verified: 68
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 15
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0002072
    reported_labels:
    - MONDO
    ontology_label: melanotic neuroectodermal tumor
  - term_id: DOID:166
    reported_labels:
    - DOID
    ontology_label: melanotic neuroectodermal tumor
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Melanotic Neuroectodermal Tumor of Infancy
- **MONDO ID:** MONDO:0002072 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** MNTI; infantile melanotic neuroectodermal neoplasm; melanotic Progonoma; melanotic neuroectodermal tumor (morphologic abnormality); melanotic neuroectodermal tumor of infancy (morphologic abnormality); melanotic neuroectodermal tumour (morphologic abnormality); melanotic neuroectodermal tumour of infancy (morphologic abnormality); pigmented neuroectodermal tumor
- **Category:** 

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Melanotic Neuroectodermal Tumor of Infancy** covering all of the
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

# Melanotic Neuroectodermal Tumor of Infancy (MNTI) — Comprehensive Research Report

**Target concept:** MONDO:0002072 · ICD-O 9363/0 · NCIT:C3717 · MeSH D017600 · UMLS C0206094
**Report date:** 28 October 2026
**Evidence posture:** ~500 published cases worldwide; literature is dominated by single case reports and three systematic reviews. There are **no randomized trials, no registries with published incidence, no animal model, and no GeneReviews chapter.** Numbers below are series-dependent and are reported with their denominators.

---

## 0. Causal-gene statement (required orientation)

**MNTI has no recorded causal gene.** It is a **sporadic somatic neoplasm of cranial neural-crest derivation**, not a Mendelian disorder: there is no OMIM morbid entry, no inheritance pattern, and no gene with recurrent, validated disease-causing status. The template header's "Causal gene(s): not recorded" is correct and should be preserved.

Three molecular lesions have been reported, each in one or very few cases, and none is recurrent across series:

| Gene / lesion | HGNC | Evidence | Status |
|---|---|---|---|
| **BRAF** p.V600E | `hgnc:1097` | 1 of 3 cases (PMID:26122804); **0 of 11** cases by ARMS-qPCR + Sanger (PMID:34094962) | Rare / unconfirmed |
| **CDKN2A** p.Asp74Ala, heterozygous **germline** | `hgnc:1787` | single case, fibular MNTI (PMID:27519597) | Single observation |
| **RPLP1::C19MC** fusion (+ reciprocal) | `hgnc:10372` | same single case (PMID:27519597) | Single observation |

Supporting molecular biology implicates **TYR** (`hgnc:12442`, markedly overexpressed), **MYC** (`hgnc:7553`, amplified in 2 of 7 methylation-profiled cases), and notably **not** **MITF** (`hgnc:7105`, not elevated). HGNC identifiers above were resolved against the HGNC REST API in the same step they were written.

Beware the name: "melanotic neuroectodermal tumor of infancy" shares vocabulary with *malignant melanotic nerve sheath tumour* (PRKAR1A/Carney complex), *melanocytoma / melanocytic tumours of the CNS*, and *embryonal tumour with multilayered rosettes* (ETMR, which is the other C19MC-driven entity). These are different diseases. The MONDO ID above is the authority.

---

## 1. Disease Information

### Overview

MNTI is a rare, rapidly growing, pigmented, **biphasic** neoplasm of probable cranial neural-crest origin that presents almost exclusively in the first year of life, with a strong predilection for the **anterior maxilla**. Its defining histology is a dual population of small neuroblast-like cells and larger melanin-containing epithelioid cells, usually in alveolar/tubular nests within a dense fibrous stroma.

> "Melanotic neuroectodermal tumour of infancy (MNTI) is a locally aggressive neoplasm of neural crest origin. It is primarily a paediatric tumour, and 95% of the cases occur in children below 1 year. The tumour mainly affects the head and neck region." — Janardhanan et al., *Head Neck Pathol* 2023;17(2):509–514 (PMID:36853558)

> "Melanotic neuroectodermal tumor of infancy (MNTI) is a rare tumor, usually diagnosed within the first year of age, with a predilection for the maxilla. Although the tumor is usually benign, its rapidly growing nature and ability to cause major deformities in surrounding structures necessitate early diagnosis and intervention." — Rachidi et al., *J Oral Maxillofac Surg* 2015;73(10):1946–56 (PMID:25936939)

**MONDO's own definition (verbatim, OLS4):**
> "A rare neoplasm usually occurring in infants. It is characterized by the presence of a mixture of melanin-containing epithelial cells and smaller neuroblast-like cells. It may involve the skull and facial bones, or the epididymis. It usually has a benign clinical course."

### Nomenclature history

- **1918** — first described by Krompecher (as "congenital melanocarcinoma").
- **1966** — Borello & Gorlin coined the present name after finding high urinary vanillylmandelic acid (VMA) excretion, which argued for a neural-crest rather than a retinal or odontogenic origin. *Borello ED, Gorlin RJ. Melanotic neuroectodermal tumor of infancy — a neoplasm of neural crest origin. Report of a case associated with high urinary excretion of vanilmandelic acid. Cancer. 1966;19:196–206.*
- Historic synonyms in use before 1966 (all deprecated): retinal anlage tumour, melanotic progonoma, pigmented congenital epulis, melanotic ameloblastoma / melanotic epithelial odontoma, pigmented adamantinoma, congenital melanocarcinoma, atypical melanoblastoma, pigmented teratoma, melanocytoma.

### Key identifiers

| Resource | Identifier | Label (verbatim from source) |
|---|---|---|
| **MONDO** | `MONDO:0002072` | Melanotic neuroectodermal tumor |
| **NCIT** | `NCIT:C3717` | Melanotic Neuroectodermal Tumor |
| **MeSH** | `D017600` | Neuroectodermal Tumor, Melanotic (trees C04.557.465.625.630; C04.557.580.625.630; introduced 1994) |
| **ICD-O-3** | `9363/0` | behaviour code `/0` = benign (see §1 caveat below) |
| **UMLS** | `C0206094` | — |
| **SNOMED CT** | `404042005` | — |
| **DOID** | `DOID:166` | — |
| **MedGen** | `60073` | — |
| **OMIM** | **none** | not a Mendelian entity |
| **Orphanet** | **not identified** in this search | flag as unresolved |
| **ICD-10 / ICD-11** | **not resolved** in this search | ICD-O morphology is the usable code; do not invent an ICD-11 stem |

### ⚠️ Classification caveat — benign vs malignant is currently inconsistent across authorities

ICD-O codes MNTI `9363/0` (**benign**), and most clinical literature calls it "benign but locally aggressive". The **5th edition WHO Classification of Tumours, Volume 7: Paediatric Tumours** (IARC, 2023; MNTI chapter by Prasad & Alaggio) takes the opposite position:

> "the recent 5th edition of the WHO classification of pediatric tumors considers MNTI of the head and neck as a malignant entity" — Head Neck Pathol 2025;19(1) (PMID:40278957)

The same paper, two sentences apart, also states:

> "MNTI is characterized as a rare benign tumor with primitive morphology that behaves in an indolent yet locally aggressive manner"

**Curation implication:** this is a live disagreement, not an error to resolve silently. Record the ICD-O `/0` behaviour code *and* the WHO 5th-edition malignant designation, and put the discrepancy in `notes:`. Do not pick a side.

### Data provenance

All information here is from **aggregated disease-level resources and published case literature** (PubMed, MONDO, NCIT, MeSH, WHO classification, StatPearls). **No EHR-derived or patient-level data** were used, and none are publicly available for this disease — the case counts are literature counts, not registry counts.

---

## 2. Etiology

### Disease causal factors

MNTI is a **neoplasm**, so "etiology" means the transforming lesion, not an exposure or a pathogen.

- **Cell of origin:** cranial neural crest. The original argument was functional (VMA production) and morphologic (multiphenotypic epithelial / neural / melanocytic expression):
  > "The tumor is proposed to be of neural crest origin because the tumor produces VMA and has heterogeneous cellular phenotype microscopically." — Front Oncol 2021;11:668505 (PMID:34094962)
  > "Distinctive morphology and multiphenotypic (epithelial, neural, melanocytic) expression distinguish MNTI from melanoma and metastatic neuroblastoma." — Kapadia et al., *Am J Surg Pathol* 1993;17(6):566–73 (PMID:8392815)
- **Epigenetic class:** the strongest modern evidence for histogenesis is DNA-methylation profiling, which places MNTI inside the **group 3 medulloblastoma** methylation class:
  > "MNTI is a rare tumor of indeterminate histogenesis and molecular signature. We performed methylation and copy number variation (CNV) profiles in patients with MNTI (n = 7) and PAT (n = 1) compared to the methylation brain tumor classifier v11b4 (BT-C) and the medulloblastoma (MB) classifier group 3/4 v1.0 (MB3/4-C)." — Lopez-Nunez et al., *Cancers (Basel)* 2021;13(4):706 (PMID:33572349)

  All 7 MNTIs were classified as **high-risk MB-G3, Subtype II** by the medulloblastoma classifier. The authors propose that MNTI, pineal anlage tumour (PAT), and MB-G3 represent "a spectrum of neoplasms primarily determined by the influence of neural crest-derived stem cells."
- **Genetic lesions:** see §4. No lesion is present in a majority of cases. MNTI is, on current evidence, a tumour with a **strong epigenetic identity and a weak/absent recurrent driver mutation**.
- **Explicit negatives (useful, cite them):** Khoddami et al. tested three typical MNTIs for the signature lesions of the small-round-blue-cell differential and found none:
  > "There is no genetic basis at present to link melanotic neuroectodermal tumor of infancy to neuroblastoma, Ewing sarcoma/peripheral primitive neuroectodermal tumor, or desmoplastic small round cell tumor." — *Pediatr Dev Pathol* 1998;1(4):295–9 (PMID:10463291)
  Specifically: no *MYCN* amplification and no 1p deletion (3/3 cases); no t(11;22)(q24;q12) and no t(11;22)(p13;q12) (2/3 cases).

### Risk factors

- **Genetic risk factors:** none established. **No susceptibility locus, no GWAS, no ClinGen gene–disease validity assertion, no ClinVar variant set for MNTI.** The single germline **CDKN2A** p.Asp74Ala observation (PMID:27519597) raises the possibility that a *CDKN2A*-predisposition background can permit MNTI, but it is **n = 1** and must not be curated as a susceptibility claim.
- **Environmental / lifestyle risk factors:** **none reported.** No toxin, radiation, occupational, dietary, or maternal exposure has been associated with MNTI in any series. Given a median age at diagnosis of ~4.5 months and at least one case detectable on retrospective prenatal ultrasound from the 12th week of gestation, the transforming event is almost certainly **prenatal**, which leaves essentially no window for post-natal environmental contribution.
- **Demographic risk factors:** age (first year of life) and male sex (~1.3:1) are the only reproducible associations — and both are descriptive, not mechanistic.
- **Family history:** no familial clustering reported.

### Protective factors

**None identified** — genetic or environmental. No protective allele, no dietary or lifestyle factor. This is expected for a congenital/early-infantile embryonal neoplasm and should be recorded as "not applicable / no evidence" rather than left blank.

### Gene–environment interactions

**No data.** Nothing in CTD, PheGenI, or the primary literature. Do not infer any.

---

## 3. Phenotypes

### Core clinical presentation

The near-invariant presentation is a **rapidly enlarging, firm, non-tender, bluish-black or reddish-blue mass of the anterior maxillary alveolus or gingiva in an infant under 6 months**, with expansion of overlying bone, displacement of the developing dentition, and secondary feeding difficulty.

> "Patient: 6-month-old female. Presentation: Maxillary anterior swelling for 4 weeks, causing feeding difficulties. Intraoral findings: Firm, reddish-bluish mass approximately 4 cm, extending from right alveolar ridge to hard palate with intact mucosa" — Santos et al., *Einstein (São Paulo)* 2018;16(2):eRC4025 (PMID:29768520)

Growth can be alarming: one mandibular case "had increased double in size in a week" at 2 months of age (PMID:35400932).

### Phenotype table with HPO suggestions

All HP identifiers below were resolved against the HPO API (ontology.jax.org) in the same step they were written; labels are the HPO canonical labels, not paraphrases.

| Phenotype | Type | HPO suggestion | Onset | Severity / course | Frequency (denominator) |
|---|---|---|---|---|---|
| Oral-cavity / alveolar mass | clinical sign | `HP:0100649` Neoplasm of the oral cavity | 0–12 mo | rapidly progressive | ~70% of all MNTI (maxilla+mandible); 93.2% maxilla of 250 jaw cases (PMID:38681460) |
| Head-and-neck neoplasm (generic) | clinical sign | `HP:0012288` Neoplasm of head and neck | 0–12 mo | rapidly progressive | **92.8%** of cases (PMID:27519597, verbatim) |
| Neoplasm (hub term) | clinical sign | `HP:0002664` Neoplasm | congenital–infantile | — | 100% by definition |
| Abnormal maxilla morphology (expansion/deformity) | physical manifestation | `HP:0000326` Abnormal maxilla morphology | 0–12 mo | progressive until excision | 62.2% of 472 (PMID:25936939) |
| Abnormal mandible morphology | physical manifestation | `HP:0000277` Abnormal mandible morphology | 0–12 mo | progressive | 7.8% of 472 |
| Abnormal skull morphology / scalp swelling | physical manifestation | `HP:0000929` Abnormal skull morphology | 0–12 mo | progressive | 15.6% of 472; **88.7%** of skull MNTI present as "rapidly growing, painless scalp swelling without neurological deficit" (PMID:41522382) |
| Facial swelling | clinical sign | `HP:0000282` Facial edema *(imperfect — HPO has no "facial swelling due to mass"; see note)* | 0–12 mo | progressive | very frequent |
| Feeding difficulties | symptom | `HP:0011968` Feeding difficulties (or `HP:0008872` Feeding difficulties in infancy) | 0–12 mo | resolves after excision | common, size-dependent (PMID:38681460) |
| Epistaxis | clinical sign | `HP:0000421` Epistaxis | 0–12 mo | episodic | occasional, size-dependent |
| Nasal obstruction | symptom | `HP:0001742` Nasal congestion | 0–12 mo | progressive | occasional, size-dependent |
| Proptosis / orbital invasion | clinical sign | `HP:0000520` Proptosis | prenatal–12 mo | progressive | rare; documented prenatally (orbital MNTI, *Ultrasound Obstet Gynecol* 2015) |
| Displaced / ectopic unerupted teeth | physical manifestation | `HP:4000093` Ectopic tooth eruption; `HP:0011079` Impacted tooth; `HP:0000164` Abnormality of the dentition | 0–12 mo | permanent sequela | frequent in jaw lesions |
| Osteolysis / bone destruction | laboratory–imaging | `HP:0002797` Osteolysis | 0–12 mo | progressive | characteristic radiologic finding |
| **Elevated urinary VMA** | laboratory abnormality | `HP:0011978` Elevated urinary vanillylmandelic acid | at diagnosis | **normalizes after resection** | ~10–15% (review-level); **2 of 18** preoperatively tested in one skull series (PMID:41522382) |
| Regional lymphadenopathy (nodal metastasis) | clinical sign | `HP:0002716` Lymphadenopathy | 0–24 mo | — | **1.35%** of cases (PMID:40278957) |
| CNS / intracranial mass | clinical sign | `HP:0100006` Neoplasm of the central nervous system | 0–12 mo | — | ~4% of 472 |
| Paratesticular / epididymal mass | clinical sign | `HP:0010788` Testicular neoplasm *(closest; epididymis-specific term absent)* | 0–12 mo | — | ~5% of 472 (male reproductive system, n = 23) |
| Failure to thrive (secondary to feeding obstruction) | symptom | `HP:0001508` Failure to thrive | 0–12 mo | reversible | reported, not quantified |

**Notes on HPO coverage gaps (verified, not assumed):**
- HPO has **no term for "metastasis"** — a search returned zero results. A metastatic MNTI must be encoded through site-specific neoplasm terms plus `HP:0002716` for nodal spread.
- HPO has **no "facial swelling"** term; `HP:0000282` *Facial edema* is a semantic mismatch (oedema vs mass effect). This is a genuine ontology gap. Under the dismech `dismech-terms` rule ("no term beats a bad one") the honest options are to bind the bone-morphology term instead (`HP:0000326`) and carry "facial swelling" in `preferred_term`, or leave the phenotype unbound with a `notes:` line recording the searches run (`facial swelling`, `facial edema`, `maxilla`).
- HPO has **no epididymis neoplasm term**; `HP:0010788` *Testicular neoplasm* is broader than the lesion. `HP:0002664` *Neoplasm* and `HP:0100649`/`HP:0012288` are **coarse** bindings and would need a `coarse_binding_basis` under the dismech coarse-phenotype gate — most plausibly `NO_HPO_TERM` for the pigmented alveolar mass and `PATHOGRAPH_HUB` for `HP:0002664` if it becomes a convergence node.

### Phenotype characteristics

- **Age of onset:** congenital to early infantile. >95% of cases present under 1 year (PMID:36853558). Median age at diagnosis **4.5 months** (Krawczyk, *EJC Paediatr Oncol* 2024;3:100141); **5 months** (median, PMID:40278957); **5 months** (mean, PMID:8392815); **3.2 months** at first symptom (mean, range 1–6, PMID:34094962); **6.5 months** (mean, StatPearls NBK560596). Sowmya's 250-case review: **40.4%** presented at 0–2 months and **53.6%** at 3–6 months (PMID:38681460).
- **Severity:** locally severe (bone destruction, facial deformity, airway/feeding compromise) but systemically mild; most children are otherwise well.
- **Progression:** **rapid and relentless until excised** — the single most clinically distinctive feature, and the reason the tumour is repeatedly mistaken for a sarcoma.
- **Post-treatment course:** typically stable/cured. Recurrence, when it happens, is early (see §8, §11).

### Quality-of-life impact

**No EQ-5D, SF-36, PROMIS, or PedsQL data exist for MNTI** — the population is pre-verbal infants and the cohorts are too small. The documented QoL burden is **surgical sequela, not disease activity**, and it is lifelong:

> "The patient began prosthodontic and orthodontic management at age 7, requiring four successive temporary removable partial dentures through age 15 to accommodate growth and maintain function/esthetics." ... block bone graft at 17, four implants, definitive implant-supported restoration at ~19 years. — *J Maxillofac Oral Surg* 2021 (PMID:35400932)

This is the best-documented long-term functional outcome in the literature and is worth curating as a complication chain: resection → alveolar bone loss and tooth loss → impaired mastication and facial growth → multi-decade prosthodontic rehabilitation.

---

## 4. Genetic / Molecular Information

### Causal genes

**None.** No gene meets any gene–disease validity tier for MNTI. There is no ClinGen GCEP assertion, no ClinVar submission set, and no HGMD entry for MNTI as a phenotype. Record `gene_disease_validity` as **absent** — not as `NO_KNOWN_DISEASE_RELATIONSHIP`, which would be a different (and unsupported) claim.

### Reported variants and rearrangements

**(a) BRAF p.V600E — `hgnc:1097`, somatic, gain-of-function, MAPK pathway**

> "Gomes et al. suggested that MNTI might also harbor *BRAF* V600E mutation and they found 1 case with *BRAF* V600E mutation." — Front Oncol 2021;11:668505 (PMID:34094962)

Primary report: Gomes CC, Diniz MG, de Menezes GHF, Castro WH, Gomez RS. **BRAFV600E Mutation in Melanotic Neuroectodermal Tumor of Infancy: Toward Personalized Medicine?** *Pediatrics.* 2015;136(1):e267–9. doi:10.1542/peds.2014-3331. **PMID:26122804.** The hypothesis was explicitly analogical to melanoma — shared "derivation from the neural crest cells and presence of large melanin-containing cells."

Refutation in a larger series: Xia et al. tested 11 MNTIs by ARMS-qPCR **and** Sanger sequencing (assay sensitivity 97.89%, positive controls valid):
> "None of the MNTI cases showed BRAF V600E mutation." ... "*BRAF* V600E mutation in MNTI is very rare and needs further investigations." (PMID:34094962)

**Curation guidance:** present this as a contested finding with both items cited. Do **not** curate BRAF V600E as a characteristic lesion. Note also that StatPearls renders the Gomes result as "reported in 3 cases of femur MNTI lesions" — that is a **misstatement** of the primary source (3 maxillary cases tested, 1 mutated); use the primary paper and the Frontiers reference list, not the StatPearls summary.

**(b) CDKN2A p.Asp74Ala — `hgnc:1787`, heterozygous GERMLINE, loss of function**

Barnes DJ, Hookway E, Athanasou N, Kashima T, Oppermann U, Hughes S, et al. *BMC Cancer* 2016;16:629. doi:10.1186/s12885-016-2669-3. **PMID:27519597.**

> "Melanotic neuroectodermal tumor of infancy (MNTI) is exceptionally rare and occurs predominantly in the head and neck (92.8 % cases). The patient reported here is only the eighth case of MNTI presenting in an extremity, and the first reported in the fibula."

Variant detail as reported:
- Genomic: chromosome 9:21971137, **T>G**, exon 2
- Protein: **p16INK4A Asp74Ala (D74A)**; synonymous **R88R** in the alternate p14ARF reading frame
- Zygosity/origin: **heterozygous, germline**, predicted deleterious
- COSMIC: **COSM4163712** — previously reported only as *somatic*; this is the first germline observation
- Population allele frequency: **not reported**; no gnomAD frequency retrieved for this report. Flag as unknown rather than asserting "absent".

**(c) RPLP1::C19MC fusion — `hgnc:10372` (RPLP1) × C19MC miRNA cluster (chr19q13.41)**

Same case. RNA-seq identified **50 fusion transcripts**, including **RPLP1-C19MC** with its reciprocal **C19MC-RPLP1** (a balanced translocation), plus balanced **H2AFV-RP11-386M24.4** and **RBBP4-TRA@** translocations and multiple collagen-gene fusions (*COL1A1, COL1A2, COL3A1, COL18A1*).

Mechanistic reading, as the authors frame it: the fusion "may deregulate microRNAs similarly to TTHY1-C19MC fusions in other embryonal tumors" — i.e. the same imprinted 19q13.41 miRNA cluster whose *TTYH1*-driven derepression defines **embryonal tumour with multilayered rosettes (ETMR)**. This is the single most interesting mechanistic lead in MNTI biology and it rests on one case.

**(d) Copy number**

- Barnes case: **euploid**, "no apparent copy number variations", a "featureless" CNV profile — genomic stability despite multiple balanced rearrangements. (SNP array 4×180k.)
- Lopez-Nunez methylation cohort (PMID:33572349): **5 of 7 MNTIs had nearly flat CNV profiles**; 2 MNTIs plus the PAT showed multiple whole-chromosome gains/losses **including *MYC* amplification**; 1 MNTI had a highly variable profile.
- Kapadia 1993 flow cytometry (PMID:8392815): of 8 interpretable tumours, "four DNA diploid, three DNA aneuploid, and one DNA diploid with a prominent shoulder"; FCM ploidy **did not predict recurrence** in that series.
- Khoddami 1998 (PMID:10463291): no *MYCN* amplification, no 1p deletion.

**Synthesis:** MNTI is usually a **copy-number-quiet** tumour. CNV burden and *MYC* amplification appear in a minority and are the candidate correlates of aggressive behaviour — the authors of the methylation study propose exactly this, that "the indolent behavior of most MNTIs versus aggressive PAT/MB-G3 outcomes may relate to absence of copy number variations, anatomical location, and microenvironmental factors rather than fundamentally distinct molecular origins."

### Modifier genes

**None identified.**

### Epigenetic information — the strongest molecular signal in this disease

| Finding | Detail | Source |
|---|---|---|
| Methylation class | All 7 MNTIs classified as **medulloblastoma group 3** by MB3/4 classifier v1.0; **Subtype II**; brain-tumour classifier v11b4 called 5 as MB-G3 and 2 as PLEX PED B | PMID:33572349 |
| Calibrated scores | >0.9 or >0.45 (BT-C); >0.45 (MB3/4-C) — i.e. several calls are at the **lower confidence band**, which matters | PMID:33572349 |
| Shared class with PAT | PAT primary classified PLEX PED B (score >0.45); **PAT relapse reclassified as MB-G3 (score 0.98)** | PMID:33572349 |
| Imprinted-locus derepression | RPLP1-C19MC fusion at the imprinted chr19q13.41 miRNA cluster | PMID:27519597 |
| Functional epigenetic dependency | MNTI primary cells: "cell viability was reduced" by **bromodomain inhibitors** and "particularly" by **lysine demethylase (KDM) inhibitors** | PMID:27519597 |

The Barnes case's proposed mechanism, verbatim: *"the fully transformed phenotype…may have arisen…because of the combined effects of a germline CDKN2A mutation, tumor promoting somatic fusion genes and epigenetic deregulation."*

### Chromosomal abnormalities

Multiple **balanced** translocations in the one deeply characterized case (above); whole-chromosome gains/losses in a CNV-high minority. No recurrent karyotypic abnormality. Nothing in DECIPHER or ECARUCA for MNTI.

### Transcriptomic / melanogenesis findings

- **TYR (tyrosinase):** "Highly expressed in the MNTI" — FPKM **144.2** vs **0.0** in in-vitro-differentiated human neural crest cells. This is the direct molecular correlate of the tumour's pigment.
- **MITF:** "No significantly elevated expression detected" — notable, because MITF is the master melanocytic transcription factor. MNTI makes melanin **without** the canonical MITF-driven melanocytic program, which is a real mechanistic puzzle worth flagging as a knowledge gap.
- **MFI2 (melanotransferrin):** strong expression not detected.
- Datasets: **GEO GSE84431** (RNA-seq + genomic, this study), **GEO GSE84428** (aCGH sub-series), compared against **GSE28875** (in-vitro-differentiated human neural crest cells).

---

## 5. Environmental Information

- **Environmental factors:** **none reported.** No toxin, heavy metal, radiation, pollutant, or occupational exposure has been linked to MNTI in any case report or review. Nothing in CTD.
- **Lifestyle factors:** **not applicable** — the patients are infants; no maternal smoking, diet, or alcohol association has been reported.
- **Infectious agents:** **none.** No viral, bacterial, fungal, or parasitic association. MNTI is not an infection-attributed neoplasm, so the dismech infectious-disease ladder and `infectious_agent` slot do not apply.

**Curation note:** under the dismech `check-environmental-evidence` gate, if an `environmental[]` block is created at all it will have no citable evidence. The correct handling is to **omit the block** and record in `notes:` that the literature was searched for exposures and none is reported — or, if a block is needed, use the `Left deliberately uncited.` `review_notes:` waiver with the searches named. Do not manufacture an exposure.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

**Where it is inferred vs demonstrated is marked on each step.** Steps 1–3 are inferred from epigenetic class and a single genomic case; steps 4–9 are demonstrated by histology, biochemistry, imaging, and outcome data.

1. **A cranial neural-crest-derived progenitor cell** (shared, on methylation evidence, with the progenitor of group 3 medulloblastoma and pineal anlage tumour) persists in the developing maxillofacial skeleton. *[Inferred — from methylation class, PMID:33572349; not demonstrated by lineage tracing, which has never been done in MNTI.]*
   → **leads to** a pool of cells competent for both neuroblastic and melanocytic differentiation.
2. **A transforming lesion occurs prenatally.** Three non-exclusive routes are documented, each in ≤1–3 cases:
   - **2a.** Loss of **p16INK4A** function (germline *CDKN2A* D74A) → **loss of cyclin-dependent kinase inhibitor activity** (`GO:0004861`) → **failure to restrain the G1/S transition** (`GO:0000082`; loss of `GO:2000134` negative regulation) → **results in** unchecked proliferative entry. *[Demonstrated in one case, PMID:27519597; inferred as a general mechanism.]*
   - **2b.** **RPLP1::C19MC** balanced translocation → derepression of the imprinted chr19q13.41 **miRNA cluster** → aberrant **miRNA-mediated post-transcriptional gene silencing** (`GO:0035195`) of differentiation programs, as in ETMR. *[Demonstrated in one case; mechanism inferred by analogy to ETMR.]*
   - **2c.** **BRAF p.V600E** → constitutive **MAPK cascade** activation → **results in** proliferative signalling. *[Observed 1/3 in one report, 0/11 in another — rare at best.]*
   → All three **converge on** step 3.
3. **A group-3-medulloblastoma-like epigenetic state is established and maintained**, including dependence on histone lysine demethylase and bromodomain-reader activity (demonstrated functionally: KDM and BET inhibitors reduce MNTI cell viability, PMID:27519597).
   → **leads to** a stable, self-perpetuating transcriptional program with **two** differentiation outputs — the branch point of the whole disease.
4. **Branch A — melanocytic/epithelial output.** The program drives **tyrosinase** (TYR FPKM 144.2 vs 0.0) → **melanin biosynthetic process from tyrosine** (`GO:0006583`, parent `GO:0042438`) → melanin deposition in **melanosomes** (`GO:0042470`) of large epithelioid cells → **results in** the HMB-45⁺ / cytokeratin⁺ pigmented cell population and the tumour's gross blue-black colour. Notably this occurs **without MITF elevation**, which is unexplained. *[Demonstrated: RNA-seq + IHC + gross pathology.]*
5. **Branch B — neuroblastic output.** The same program yields small primitive cells expressing **synaptophysin** and **NSE**, **consistently negative for Phox2b** (PMID:33572349) — i.e. neuroblastic by marker but **not** of sympathoadrenal/neuroblastoma lineage, which is the decisive distinction from metastatic neuroblastoma.
   → **leads to** the biphasic histology that defines the entity. Branch B also carries the aggressive potential: in the chemotherapy cohort, "presence of neuroblast-like cells correlated with aggressiveness; neoadjuvant CHT preferentially reduced small round blue cell components" (PMID:34359769).
6. **Residual catecholamine biosynthetic capacity** (`GO:0042423`) in a subset of tumours → norepinephrine turnover → **urinary excretion of vanillylmandelic acid** (`CHEBI:20106`), the degradation product of norepinephrine → **results in** elevated urinary VMA in a minority (~10–15%; only 2/18 in one skull series), which **normalizes within ~1 week to 1 month of resection**, proving the tumour is the source. *[Demonstrated — this is the 1966 observation that named the disease, and it has been reproduced: "One week later the levels of the VMA in urine returned to normal limits." PMID:35400932.]*
7. **Rapid expansile intraosseous growth** within the maxilla/mandible/skull → cortical expansion with a thin lobulated continuous shell, plus **osteolysis** of trabecular bone, occasionally with a sunburst periosteal reaction → **results in** the radiolucent expansile lesion with displaced unerupted teeth seen on CT.
8. **Mass effect on adjacent structures** → **leads to** the clinical phenotype: alveolar/gingival mass, facial deformity, feeding difficulty, nasal obstruction, epistaxis, and (with orbital extension) proptosis.
9. **Branches at outcome:**
   - **9a (common).** Complete excision → removal of the entire clone → cure in 80–90%.
   - **9b (10–27%).** Incomplete excision leaves clonal cells → early local regrowth, overwhelmingly **within 4 months**, and preferentially in the youngest patients. *[Demonstrated epidemiologically; the age effect is unexplained — the leading, untested hypothesis is a larger residual permissive neural-crest progenitor pool in the youngest infants.]*
   - **9c (1.4–3%).** Acquisition of a CNV-high / *MYC*-amplified genotype and/or neuroblast-dominant histology → regional nodal, then hepatic, bone-marrow, or CNS **metastasis** → high mortality. *[The genotype–behaviour link is explicitly proposed but not established — PMID:33572349 calls for "larger cohorts to better determine their impact in prognosis and biologic behavior."]*
   - **9d (universal after resection of a jaw lesion).** Loss of alveolar bone and deciduous/permanent tooth germs → impaired maxillofacial growth → decades of orthodontic and prosthodontic rehabilitation.

### Checklist coverage

- **Molecular pathways:** cell-cycle G1/S control (p16INK4A–CDK4/6–RB); MAPK (BRAF, rare); miRNA-mediated silencing (C19MC); melanogenesis (tyrosinase); catecholamine biosynthesis/degradation. KEGG/Reactome have no MNTI-specific pathway.
- **Cellular processes:** unrestrained cell-cycle entry; bidirectional lineage differentiation from a single progenitor; melanosome biogenesis; proliferation is often **low by Ki-67** — <1–5% in 9 of 11 cases, but **40% and 50%** in two (PMID:34094962), so a low index does not exclude aggressive behaviour and a high one has not been shown to predict it.
- **Protein dysfunction:** p16INK4A D74A — predicted loss of CDK-inhibitory function (computational prediction, not assayed); BRAF V600E — constitutive kinase activation (well characterized in other tumours, not functionally assayed in MNTI); tyrosinase — overexpression, not dysfunction.
- **Metabolic changes:** tyrosine routed into melanin synthesis; catecholamine turnover yielding VMA. No lipidomic, broader metabolomic, or energy-metabolism data exist.
- **Immune system involvement:** **no data.** No immune infiltrate characterization, no checkpoint expression, no autoimmunity. A genuine gap.
- **Tissue damage mechanisms:** direct mechanical expansion and osteolysis. **Not** ischaemia, fibrosis, oxidative stress, or inflammation — do not import a generic tumour-microenvironment mechanism the literature does not support here.
- **Biochemical abnormalities:** elevated urinary VMA (minority). No enzyme deficiency, receptor, or channel defect.
- **Molecular profiling:** transcriptomics — one RNA-seq case (GSE84431); epigenomics — 7 methylation arrays (PMID:33572349); CNV — SNP array and 450k-derived profiles; flow-cytometric ploidy — 8 cases (PMID:8392815). **Proteomics: none. Metabolomics: none. Lipidomics: none. Single-cell: none. Spatial transcriptomics: none. CRISPR/RNAi screens: none.** MNTI is absent from TCGA, ICGC, cBioPortal, and DepMap.

### GO / CL term suggestions (all resolved against OLS4 at time of writing)

**Biological processes / components / functions**

| Term | ID | Role in the chain |
|---|---|---|
| melanin biosynthetic process | `GO:0042438` | step 4 |
| melanin biosynthetic process from tyrosine | `GO:0006583` | step 4 (more specific; preferred) |
| melanosome | `GO:0042470` | step 4 (cellular component) |
| catecholamine biosynthetic process | `GO:0042423` | step 6 |
| neural crest cell migration | `GO:0001755` | step 1 (developmental context) |
| G1/S transition of mitotic cell cycle | `GO:0000082` | step 2a |
| negative regulation of G1/S transition of mitotic cell cycle | `GO:2000134` | step 2a (the function lost) |
| cyclin-dependent protein serine/threonine kinase inhibitor activity | `GO:0004861` | step 2a (p16INK4A molecular function) |
| miRNA-mediated post-transcriptional gene silencing | `GO:0035195` | step 2b |

**Cell types — read the labels carefully, two common assumptions are wrong**

| Term | ID | Note |
|---|---|---|
| neural crest cell | `CL:0011012` | **this** is the generic term |
| migratory neural crest cell | `CL:0000333` | **not** "neural crest cell" — `CL:0000333` is the *migratory* subtype; binding it asserts migration |
| migratory cranial neural crest cell | `CL:0000008` | closest to the proposed MNTI progenitor |
| melanocyte | `CL:0000148` | the differentiated analogue of the pigmented component |
| neural crest derived neuroblast | `CL:0002676` | best fit for the small-cell component |
| neuroblast (sensu Vertebrata) | `CL:0000031` | canonical label **includes** "(sensu Vertebrata)" |

**Important caveat on cell-type binding:** MNTI's two populations are *melanocyte-like* and *neuroblast-like*, not proven melanocytes or neuroblasts — the Phox2b-negative result argues specifically against sympathoadrenal neuroblast identity. Bind `CL:0011012` / `CL:0000008` for the progenitor with confidence; bind `CL:0000148` and `CL:0002676` only with `preferred_term` carrying the "-like" hedge and a `notes:` line, or leave the differentiated components unbound.

---

## 7. Anatomical Structures Affected

### Organ level — site distribution

The authoritative distribution is Rachidi's 472-case systematic review (PMID:25936939), restated verbatim in the Frontiers series:

> "The largest systematic review of 472 cases showed that 62.2% cases involved maxilla, followed by the skull (15.6%), and mandible (7.8%)." (PMID:34094962)

| Site | n / 472 | % | UBERON suggestion |
|---|---|---|---|
| Maxilla (predominantly **anterior**) | 279 | 62.2% | `UBERON:0002397` maxilla; `UBERON:0004527` alveolar process of maxilla |
| Skull | ~70 | 15.6% | `UBERON:0003129` skull |
| Mandible | ~35 | 7.8% | `UBERON:0001684` mandible; `UBERON:0004528` alveolar ridge of mandible |
| Male reproductive system (epididymis > testis) | 23 | ~5% | `UBERON:0001301` epididymis; `UBERON:0000473` testis |
| Central nervous system | 20 | ~4% | `UBERON:0000955` brain *(label not re-verified in this session — look it up before binding)* |
| Soft tissue | 7 | ~1% | site-specific |
| Female reproductive tract (ovary, uterus) | rare | <1% | site-specific |

Additional site data worth recording:
- **Head and neck overall: 92.8%** (PMID:27519597, verbatim).
- Other series skew differently: 70% maxilla (PMID:41522382); 93.2% maxilla vs 6.8% mandible among 250 **jaw** cases (PMID:38681460 — denominator is jaws only, so this is **not** comparable to the 62.2% figure); HNP 2025's 11 cases were maxilla 8, mandible 1, **sphenoid bone** 1, **temporal bone** 1 (PMID:40278957); Kapadia's 20 cases were maxilla 13, mandible 3, **dura** 2, brain 1, skull/orbit 1 (PMID:8392815).
- Documented rare sites: **fibula** (first reported case, PMID:27519597 — "only the eighth case of MNTI presenting in an extremity"), forearm soft tissue (PMID:26722579), ovary (PMID:31804335), postauricular region, femur, frontal midline of the skull (extra-axial, 2025).
- Involved contiguous structures in jaw lesions: **hard palate** (`UBERON:0003216`), **gingiva** (`UBERON:0001828`), nasal cavity, maxillary sinus, and **orbit** (`UBERON:0001697` orbit of skull).
- **Pineal body** (`UBERON:0001905`) is the site of the related pineal anlage tumour — relevant to MNTI's methylation class, not a site of MNTI itself.

**Body systems involved:** skeletal (craniofacial), digestive (oral cavity, feeding), respiratory (nasal airway), nervous (CNS minority; cranial nerves spared in most skull cases — 88.7% present "without neurological deficit"), reproductive (male, minority), lymphatic (nodal metastasis, 1.35%).

**Secondary organ involvement (metastatic MNTI only):** regional lymph nodes, liver, bone marrow, CNS.

### Tissue and cell level

- **Tissue types:** intraosseous — tumour arises within and expands bone, with a **dense fibroblastic / fibrocollagenous stroma** forming the alveolar and trabecular compartments. Overlying mucosa is typically **intact** (an important clinical sign).
- **Entrapped normal elements:** odontogenic epithelial rests and developing tooth germs are frequently entrapped — a recognized diagnostic pitfall that invites a mistaken diagnosis of ameloblastoma.
- **Cell populations:** see §6. Large pigmented epithelioid (melanocyte-like) cells lining alveolar/tubular structures; small primitive neuroblast-like cells in the nest centres.

### Subcellular level

- **Melanosome** (`GO:0042470`) — the pigment compartment; melanin granules are the diagnostic ultrastructural feature. Ultrastructural studies date to the 1980s (e.g. PMID:6263455).
- Nucleus (p16INK4A cell-cycle control; chromatin-modifier dependency).
- No mitochondrial, ER, lysosomal, or peroxisomal involvement reported.

### Localization and lateralization

**Unilateral** in essentially all reported cases, centred on the **anterior maxillary alveolus** when in the jaw (midline-adjacent but lateralized). Skull lesions may be midline (e.g. the 2025 frontal-midline extra-axial case). No series reports bilateral or symmetric disease. Suggested HPO/qualifier handling: record laterality in `description` rather than inventing a term.

---

## 8. Temporal Development

### Onset

- **Pattern:** congenital in origin, clinically **acute-to-subacute** in presentation — the mass is usually noticed days to a few weeks before diagnosis and grows visibly week to week.
- **Age:** see §3. Median 4.5–5 months at diagnosis; >95% under 1 year; present at or near birth in a substantial minority.
- **Prenatal detectability is established.** One orbital MNTI was detected at **34 weeks** by ultrasound, and "retrospective examination showing the tumor had been present since the 12th week of pregnancy" — which dates the transforming event to the first trimester. Prenatal sonographic appearance: "a homogeneous isoechoic soft-tissue mass in the periorbital region, encasing the ocular globe"; on later ultrasound "heterogeneous, well-demarcated, with decreased vascularization." (*Ultrasound Obstet Gynecol* 2015, Koob et al.; see also *J Pediatr Hematol Oncol* prenatal case report.)
- Neonates may present with "substantial infraorbital and jaw swelling with occlusion of the eyelid as well as blackish freckles in overlying skin."

### Progression

- **No stage system exists.** AJCC/UICC do not stage MNTI; WHO Paediatric Tumours does not define grades. Practical stratification in the literature is: **resectable localized** / **locally unresectable** / **metastatic**.
- **Progression rate:** rapid pre-treatment ("increased double in size in a week"); tumours commonly reach 2–6.3 cm by presentation (HNP 2025 range 3.2–6.3 cm, median 4.5 cm; Kapadia mean 3.5 cm, range 1.0–10.0 cm; Frontiers series 2.0–6.0 cm).
- **Course:** monophasic — grow until excised, then usually stable. **Not** relapsing-remitting, not episodic, not chronic-progressive.
- **Duration:** effectively self-limited by treatment. There is no chronic active phase.

### Patterns

- **Spontaneous remission: not reported.** Remission is always treatment-induced.
- **Recurrence timing is the key temporal fact and it is tight:**
  - "Most of the recurrences occur within the first 6 months of therapy" (PMID:41445906)
  - "Mean recurrence time: 3.26 months (range: 15 days–20 months); **92% of recurrences occurred within four months**" (250 cases, PMID:38681460)
  - "More than 80% of recurrences occur in the first four months" (StatPearls NBK560596)
  - "Five tumors (45%) recurred within 4 months of diagnosis, but none metastasized." (PMID:8392815 — note this series reports follow-up on 12 cases and recurrence "in two of five cases with follow-up" elsewhere in the same abstract; the 45% figure's denominator is ambiguous and should be quoted with that caveat)
  - Median time from initial surgery to first relapse in the chemotherapy cohort: **1.5 months** (range 2 weeks–18 months) (PMID:34359769)
  - One outlier recurrence at **77 months** (PMID:34094962) — so late relapse is possible and a 2-year "all clear" is not absolute.
- **Critical period for intervention:** the first weeks after presentation. Early complete excision is the single determinant of outcome, and delay costs both local control and the extent of reconstruction needed.
- **Critical period for surveillance:** the **first four months post-operatively**, which is why the recommended follow-up is front-loaded (weekly for the first month — §12).

---

## 9. Inheritance and Population

### Epidemiology

- **Total reported cases:** "In the last 100 years since the first description of MNTI only around 500 cases have been described from 32 countries." (PMID:41445906); "accounting for approximately 500 cases globally" (PMID:41522382); 472 cases 1918–2013 in the largest systematic review (PMID:25936939).
- **Prevalence / incidence:** **no published rate.** There is no incidence per 100,000, no birth prevalence, and no Orphanet prevalence class. On the dismech `PrevalenceClassEnum`, the defensible encoding is `measure_type: CASES_IN_LITERATURE` with the 472 or ~500 figure and `prevalence_class: ULTRA_RARE` — **not** a numeric band, since no denominator exists. Do not derive a rate.
- ⚠️ One review states MNTI "constitutes 2 to 5% of all pediatric neoplasms" in the head/neck region (PMID:41445906). **Treat this with scepticism**: it is arithmetically hard to reconcile with ~500 lifetime reported cases worldwide and is not corroborated by other sources. If curated at all, attribute it explicitly and flag the inconsistency in `notes:`.

### Inheritance

- **Not heritable.** MNTI is a sporadic somatic neoplasm. **No inheritance pattern, no penetrance, no expressivity, no anticipation, no germline mosaicism, no founder effect, no consanguinity role, and no carrier frequency** — all of these fields are **not applicable**, which is a different and more informative answer than "unknown". Do not create an `inheritance:` block.
- The single germline *CDKN2A* D74A case (PMID:27519597) is the only germline observation in the literature. The infant was disease-free 3 years after wide excision; no family history is reported. This does **not** establish a predisposition syndrome.

### Population demographics

- **Sex ratio:** male predominance in most series, but not uniformly:

| Series | M:F | n | Source |
|---|---|---|---|
| 250-case review | 61.2% M : 36.8% F (~1.7:1) | 250 | PMID:38681460 |
| Chemotherapy cohort | 69.2% M (27:12) | 39–42 | PMID:34359769 |
| Chinese BRAF series | 8 M : 3 F | 11 | PMID:34094962 |
| Indian 10-year series | 1.75:1 (7 M : 4 F) | 11 | PMID:40278957 |
| General literature estimate | 1.3:1 | — | StatPearls NBK560596 |
| **Kapadia 1993** | **7 M : 13 F** (female predominant) | 20 | PMID:8392815 |

  Record this as a **modest male predominance with series-level heterogeneity**, and cite Kapadia as the counter-example rather than averaging it away.
- **Geographic distribution:** "MNTI shows a wide geographic variation, however, the highest prevalence of MNTI has been reported from the **United States** followed by **India**" (PMID:41445906); also Germany and Brazil among high-reporting countries. This almost certainly reflects **reporting and publication intensity, not true incidence** — say so.
- **Ethnic predisposition:** none established. No HANCESTRO-codeable population effect has been reported. Do not bind an ancestry term.
- **Variant geography:** not applicable (no recurrent variant).
- **Age distribution:** see §3 and §8.

---

## 10. Diagnostics

### Clinical tests

**Histopathology is the diagnostic gold standard.** Everything else is supportive.

> "Histopathology is the gold standard for diagnosis wherein a biphasic tumor is seen. It comprises larger polygonal cells with melanin pigment and smaller round blue cells." — StatPearls NBK560596

**Microscopic description:** alveolar, tubular, cord-and-trabecular or nested architecture; large cuboidal/polygonal epithelioid cells with pale abundant cytoplasm, vesicular nuclei and coarse brown melanin granules lining the alveoli; small round cells with hyperchromatic nuclei and scant or fibrillar cytoplasm in the nest centres; dense fibrocollagenous stroma; entrapped odontogenic epithelium and bony trabeculae; mitoses and necrosis usually absent.

> "All cases demonstrated classic biphasic morphology with smaller neuroblast-like cells and larger melanin-containing epithelioid cells." (9/9 and 6/6 by IHC, PMID:40278957)

**Immunohistochemistry — the discriminating test.** Pooled across series:

| Marker | Large epithelioid cells | Small neuroblast-like cells | Reported rate | Source |
|---|---|---|---|---|
| **Cytokeratin / AE1-AE3 / pan-CK** | **positive** | negative | 12/12; 9/9; 11/11 | PMID:8392815; PMID:40278957; PMID:34094962 |
| **HMB-45** | **positive** | negative | 12/12; 9/9; 11/11 | same |
| **Synaptophysin** | variable | **strongly positive** | 6/6; 11/11; 4/12 (older series) | PMID:40278957; PMID:34094962; PMID:8392815 |
| **NSE** | positive | **positive** | 7/12; 11/11 | PMID:8392815; PMID:34094962 |
| Vimentin | positive | scattered positive | 7/8 | PMID:8392815 |
| Leu-7 (CD57) | positive | positive | 9/12 | PMID:8392815 |
| EMA | positive | — | 4/9 | PMID:8392815 |
| **S-100** | usually **negative** or focal/weak | negative | 2/12 positive; 0/11 | PMID:8392815; PMID:34094962 |
| **Melan-A** | **conflicting** | negative | 0/11 negative (PMID:34094962) vs "strongly and diffusely positive in epithelioid cells" (PMID:29768520) | — |
| **SOX10** | **negative** | negative | "uniformly negative" | PMID:41445906 |
| **Phox2b** | **negative** | **negative** | "consistently negative (all components)" | PMID:33572349 |
| Desmin, myogenin | negative | negative | no staining | PMID:8392815; PMID:27519597 |
| Chromogranin | negative | negative | no staining | PMID:8392815 |
| CD99 | **conflicting** | negative in one series, positive in the Barnes case | — | PMID:27519597 vs PMID:34094962 |
| GFAP | — | — | 3/12 positive | PMID:8392815 |
| CEA, LCA/CD45, CD20, CD31, CD68 | negative | negative | — | PMID:8392815; PMID:27519597 |
| **Ki-67** | — | — | <1–5% in 9/11; **40%** and **50%** in 2/11 | PMID:34094962 |

**The high-yield diagnostic triad:** HMB-45⁺/cytokeratin⁺ large cells + synaptophysin⁺/NSE⁺ small cells + **S-100 negative**. Two negatives do the heaviest lifting against the differential: **SOX10-negative** excludes ameloblastoma and most melanocytic lesions, and **Phox2b-negative** excludes metastatic neuroblastoma.

> "MNTI commonly does not express diffuse reactivity with S-100, which helps distinguish it from similar lesions." (PMID:29768520 context)

**Laboratory tests / biomarkers**

- **Urinary VMA** (`CHEBI:20106`; HPO `HP:0011978`) — the historical biomarker, and a **poor screening test**:
  - "About 10% to 15% of MNTIs will elaborate vanillylmandelic acid (VMA…)"
  - "Some employ the measurement of urinary vanillylmandelic acid (VMA) levels; however, **it can be negative even in recurrent cases**." (PMID:41445906)
  - "positive results in only **two of 18** preoperatively tested patients" (PMID:41522382)
  - When elevated it is informative post-operatively: 10 mg/24 h pre-op (normal 2.0–7.0); "One week later the levels of the VMA in urine returned to normal limits." (PMID:35400932). Another report: elevated immediately after surgery, normal one month later.
  - **Use:** a positive pre-operative VMA supports the diagnosis and gives a cheap post-operative marker of completeness; a negative one excludes nothing.
  - **LOINC:** a VMA-in-urine measurement code exists in LOINC but was **not resolved in this session** — look it up and seed `cache/loinc/terms.csv` via `just loinc-seed-cache` before binding. Do not type a LOINC label from memory.
- **No circulating protein, metabolite, or genetic biomarker** for MNTI. No liquid biopsy. Catecholamines other than VMA are not systematically reported.

**Imaging**

Recommended by the 2026 expert consensus: "local imaging through MRI and CT with histopathological confirmation" (PMID:42527893).

| Modality | Findings | Source |
|---|---|---|
| **Plain radiograph** | "A well-circumscribed, radiolucent, expansile lesion involving the anterior maxilla" with displaced developing dentition; "sunburst pattern" in aggressive cases | PMID:20080455 |
| **CT** | "Bilobular, expansile bone lesion with homogenous soft-tissue density content" with "thin, lobulated and continuous" margins and hyperostosis; "Moderate homogenous enhancement"; calcification uncommon; bone erosion/destruction; unerupted teeth visible within the lesion | PMID:20080455; PMID:41445906 |
| **MRI (series 1)** | T1 **hyperintense**; T2 mildly hyperintense; moderate contrast enhancement. The authors note: "the MR signals are unlike a melanin signal, because of the variable proportion of melanin in the predominantly non-melanin content." | PMID:20080455 |
| **MRI (series 2)** | "T1/T2 isointense" or hypointense; "Well-defined lobulated expansile lesion"; "Patchy diffusion restriction on diffusion-weighted imaging"; minimal to no post-contrast enhancement | PMID:41445906 |
| **Prenatal ultrasound** | "homogeneous isoechoic soft-tissue mass in the periorbital region, encasing the ocular globe"; later "heterogeneous, well-demarcated, with decreased vascularization" | Koob et al. 2015 |

⚠️ **The two MRI descriptions above genuinely conflict** (T1 hyperintense + moderate enhancement vs iso/hypointense + minimal enhancement). This is real heterogeneity driven by variable melanin content, and both should be recorded rather than one picked. MRI signal is **not** a reliable discriminator for MNTI.

**Functional tests / electrophysiology:** no role.

### Genetic testing

- **No diagnostic genetic test exists**, and none is recommended. WGS, WES, gene panels, single-gene testing, CMA, karyotype, FISH, mtDNA testing and repeat-expansion testing all have **no established diagnostic role** in MNTI. Nothing in GTR; no GeneReviews chapter.
- **Targeted/predictive testing:** **BRAF V600E** testing has been proposed "as a potential predictive biomarker for vemurafenib therapy" (PMID:26122804, and discussion in PMID:34094962). Given 0/11 in the larger series, its yield is low; reserve it for unresectable or metastatic disease where a targeted option would change management.
- **DNA methylation profiling** (EPIC/450k array + brain-tumour and medulloblastoma classifiers) is currently a **research / reference-centre** tool. It is the most informative molecular assay available, it reliably places MNTI in a defined methylation class, and it may become diagnostically useful — but note the calibrated scores in the published series included values at the low-confidence band (>0.45).
- **FISH/karyotype negatives worth knowing when excluding mimics:** no *MYCN* amplification, no 1p deletion, no *EWSR1* t(11;22) (PMID:10463291).

### Omics-based diagnostics

RNA-seq: one case (GSE84431). Proteomics, metabolomics, liquid biopsy: **none**. Epigenomics: see above.

### Clinical criteria and differential diagnosis

**No consensus diagnostic criteria exist** beyond "characteristic biphasic histology with the characteristic immunophenotype, in an infant". The 2026 EXPeRT/ERN PaedCan consensus (PMID:42527893) is the first formal management guidance and recommends MRI + CT with histopathological confirmation.

**Differential diagnosis — the small-round-blue-cell and pigmented-jaw-lesion lists:**

| Entity | Distinguishing features |
|---|---|
| **Metastatic neuroblastoma** | **Phox2b positive**; MYCN amplification and/or 1p deletion; raised catecholamines more consistently; MIBG avid; no HMB-45⁺/CK⁺ pigmented population |
| **Rhabdomyosarcoma** (incl. paratesticular — a documented misdiagnosis of epididymal MNTI) | desmin⁺, myogenin⁺, MyoD1⁺; MNTI is desmin-negative |
| **Ewing sarcoma / pPNET** | CD99 diffuse membranous, NKX2-2⁺, *EWSR1* fusion — absent in MNTI (0/2 tested) |
| **Desmoplastic small round cell tumour** | *EWSR1-WT1* t(11;22)(p13;q12) — absent in MNTI |
| **Ameloblastoma / melanotic ameloblastoma** | **SOX10 positive**; MNTI uniformly SOX10-negative; entrapped odontogenic rests in MNTI are a trap |
| **Congenital epulis (gingival granular cell tumour)** | granular eosinophilic cytoplasm, S-100-negative but HMB-45-negative; non-pigmented; does not destroy bone |
| **Melanoma** | adult; S-100 and SOX10 positive; no neuroblastic component; "multiphenotypic (epithelial, neural, melanocytic) expression distinguish[es] MNTI from melanoma" (PMID:8392815) |
| **Lymphoma / leukaemic infiltrate** | LCA/CD45⁺, CD20⁺; MNTI negative |
| **Langerhans cell histiocytosis** | CD1a⁺, langerin⁺ |
| **Central giant cell granuloma, fibrous dysplasia, osteoma** | radiologic/histologic; no biphasic pigmented population |
| **Dentigerous / odontogenic keratocyst, unicystic ameloblastoma** | the usual *pre-biopsy* provisional diagnoses in jaw cases (PMID:41445906) |
| **Meningioma** (skull lesions) | EMA/SSTR2A⁺, whorls/psammoma bodies |
| **Pineal anlage tumour** | midline pineal; shares the MNTI/MB-G3 methylation class and may be biologically continuous with MNTI (PMID:33572349) |

### Screening

**No screening exists and none is justified** — no newborn screening, no carrier screening, no cascade screening, no population screening. The disease is sporadic, has no heritable basis, and is ~500 cases in a century. Prenatal detection occurs incidentally on routine obstetric ultrasound, not by design.

---

## 11. Outcome / Prognosis

### Survival and mortality

- **Cure rate:** "surgery is the mainstay of treatment, achieving **80%-90% cure rates**" — EXPeRT/ERN PaedCan consensus, *Pediatr Blood Cancer* 2026;70:e70458 (PMID:42527893).
- **Mortality:** **2.4%** across 250 reviewed cases (PMID:38681460). Deaths are concentrated in disseminated/inoperable disease: "Disseminated inoperable MNTI was almost universally associated with poor response to CHT and unfavorable outcome" (PMID:34359769). In that chemotherapy cohort, 2 of 24 first-line patients and 2 of 18 recurrence-treated patients died of disease.
- **Series outcomes:** HNP 2025 — all 8 patients with follow-up alive with no evidence of disease (1–93 months, median 16) (PMID:40278957). Lopez-Nunez — 4 MNTI cases in clinical remission at median 54 months; the one PAT died at 16 months (PMID:33572349). Kapadia — "One surgical death occurred" among 20 (PMID:8392815).
- **No 5-year or 10-year survival rate has been formally published.** Do not construct one. SEER does not report MNTI separately.
- **Life expectancy:** normal after complete excision, on current evidence.

### Morbidity and function

- Disability is **surgical and developmental**, not oncologic: alveolar bone loss, loss of deciduous and permanent tooth germs, maxillofacial growth disturbance, malocclusion, and the need for staged orthodontic/prosthodontic/implant rehabilitation into adulthood (PMID:35400932). This burden is **greater the more extensive the resection**, which is the whole argument for neoadjuvant chemotherapy enabling "complete, non-mutilating delayed surgery" (PMID:34359769).
- Orbital and ocular morbidity in orbit-invading lesions; airway and feeding morbidity pre-operatively.
- **No GBD estimate, no ICF-coded disability data, no validated QoL instrument data.**

### Disease course and complications

- **Recurrence** — the dominant complication. Rates by source:

| Rate | Denominator / context | Source |
|---|---|---|
| **15.2%** (38/250) | pooled review of jaw-predominant cases | PMID:38681460 |
| "less than 20%" | review-level | PMID:41445906 |
| "about 20%" | review-level | PMID:20080455 |
| **15–27%** | review-level | StatPearls NBK560596 |
| "up to 27%" / "up to 30%" | skull-focused review | PMID:41522382 |
| **10–60%** | review-level, widest published range | PMID:26122804 |
| 2/11 | single institutional series | PMID:34094962 |

  **By site** (chemotherapy-cohort analysis, PMID:34359769): **mandible 33.3% > skull 31.8% > maxilla 19.3%**.
  **By margin:** "Without free margins, recurrence increases **five-fold**" (PMID:20080455); "incomplete resection has been purported to be one of the main reasons for frequent recurrences" (PMID:40278957).
  **By age — the best-replicated prognostic finding:** 0–2 months **24.8%** vs 3–6 months **9.7%** (p significant, PMID:38681460); "the recurrence rate for tumours seen in patients younger than two months of age is **quadruple** that of tumours seen in patients 4.5 months of age and older" (Rachidi, PMID:25936939); "Recurrence highest in children diagnosed within first 2 months; minimal risk beyond 4-5 months" (PMID:34359769).
- **Malignant transformation / metastasis:**

| Rate | Context | Source |
|---|---|---|
| **2%** (5/250) | pooled review | PMID:38681460 |
| **3%** | review-level, "regional lymph nodes and central nervous system" | StatPearls NBK560596 |
| 3.2% (5/158) | older review | 1982 review (PMID:6286519 era) |
| **3–7%** | review-level | PMID:20080455 |
| **1.35%** lymph-node metastasis; **1.4–2.1%** malignant+metastatic | institutional series | PMID:40278957 |
| 6.5% malignant transformation overall / 2% of maxillary tumours | review-level | institutional review |

  **Metastatic sites:** regional lymph nodes, liver, bone marrow, CNS. "Distant metastasis at presentation is associated with higher recurrence rates and **14-fold higher mortality**."
  Malignancy and recurrence are tightly coupled: "**80% of malignant cases showed recurrence**" (χ², p<0.001; PMID:38681460).
- **Recovery potential:** excellent with complete excision; recurrent disease is usually salvageable by re-excision ("in recurrent cases, surgery is the preferred therapeutic modality", PMID:41445906); disseminated disease is usually not.

### Prognostic factors

Ranked by strength of evidence:

1. **Completeness of resection** (margins) — strongest modifiable factor.
2. **Age at diagnosis** — younger = worse; the inverse of the usual paediatric-oncology intuition, and mechanistically unexplained.
3. **Disseminated / inoperable disease at presentation** — the dominant determinant of mortality.
4. **Anatomic site** — mandible and skull recur more than maxilla.
5. **Histologic features** — "Aneuploidy, necrosis, and high mitotic figures suggested as potential negative factors, **though not definitively established**" (PMID:34359769). Neuroblast-cell predominance correlates with aggressiveness.
6. **Flow-cytometric ploidy** — tested and **not** predictive: "we were unable to demonstrate the usefulness of FCM in predicting recurrences" (PMID:8392815).
7. **Candidate, unvalidated:** CNV burden and *MYC* amplification by methylation-array profiling (PMID:33572349); Ki-67 index (two of eleven cases had 40–50% with no reported outcome difference).

**No validated prognostic biomarker and no prognostic model/calculator exists for MNTI.**

---

## 12. Treatment

### Surgery — the standard of care

Complete surgical excision with clear margins. NCIT suggestions: `NCIT:C15329` **Surgical Procedure** (generic action); consider `NCIT:C154430` for resection specifically (**verify before binding** — not re-resolved in this session).

- "The treatment of choice for MNTI is excision, and it is usually curative." (PMID:36853558)
- "Wide surgical excision with at least **5 mm** of healthy margins." (PMID:20080455)
- **Extent is contested, and the evidence favours conservatism:** Rachidi's review "found no difference in recurrence rates in patients treated by curettage only and patients who underwent resection" (PMID:25936939); "There is no difference in recurrence rates between both the modality of treatment" (PMID:41445906). Options used in practice: simple enucleation; enucleation with curettage ± peripheral ostectomy; marginal resection; segmental resection. Surgery was the primary modality in **90.4%** of 250 cases (PMID:38681460).
- **The conservative-surgery argument is a growth argument, not an oncologic one:** "Extensive surgery in a child may interfere with the normal growth and development of the facial structures and reconstruction can be very challenging in infants. Hence, early diagnosis is critical for the effective management." (PMID:36853558)
- **Endoscopic-assisted** excision is recommended for complete removal of maxillary lesions (PMID:41445906).
- One documented operative death (PMID:8392815) — the procedure is not risk-free in a 2-month-old.

### Chemotherapy — for inoperable, metastatic, or recurrent disease

NCIT: `NCIT:C15632` **Chemotherapy**. The definitive source is Styczewska M, Krawczyk MA, Brecht IB, et al. *Cancers (Basel)* 2021;13(15):3872 (PMID:34359769) — 4 institutional cases plus a systematic review of 38 literature cases over 42 years.

> "Neoadjuvant CHT, based mainly on the protocols for neuroblastoma, was often effective, allowing for complete delayed surgery in most cases."

**Regimens reported** (all borrowed from other paediatric tumours — there is no MNTI-specific protocol):

| Family | Regimens | Agents (CHEBI, verified) |
|---|---|---|
| Neuroblastoma-based | **CADO**, VP-16 + Carbo, **NB2004**, **OPEC/OJEC** | cyclophosphamide `CHEBI:4027`; vincristine `CHEBI:28445`; doxorubicin `CHEBI:28748`; etoposide `CHEBI:4911`; carboplatin `CHEBI:31355`; cisplatin |
| Ewing sarcoma-based | **VIDE**, **VAC** | vincristine, ifosfamide `CHEBI:5864`, doxorubicin, etoposide; dactinomycin / actinomycin D `CHEBI:27666` |
| Soft-tissue sarcoma | I2VAdr, I2VE, **CWS-2006**, **RMS 2005** | ifosfamide, vincristine, doxorubicin, etoposide |
| Intracranial | **8-in-1** | multi-agent |
| Recurrent benign disease | cyclophosphamide + vincristine | — |

**Response rates** (PMID:34359769):

| Setting | n | Outcomes |
|---|---|---|
| Neoadjuvant, first-line | 12 | PR 7 (58%), SD 3 (25%), CR 1 (8%), PD 1 (8%) |
| Adjuvant, first-line | 10 | CR 2, PR 2, SD 2, not assessable 4; **7 of 10 had no recurrence/progression** (follow-up 10 months–4.5 years) |
| Neoadjuvant for recurrence | 8 | CR 1, PR 4, SD 1, PD 1 |
| Adjuvant for recurrence | 12 | **6 of 6 R1-resected patients had no recurrence**; long-term CR 1, PR 2, SD 1 |

**Recommendations from that review, verbatim in substance:** neoadjuvant chemotherapy for initially inoperable tumours, permitting delayed non-mutilating surgery; adjuvant chemotherapy considered for incomplete (R1) resection, particularly in infants under 2 months, though "risk-to-benefit ratio should always be carefully evaluated".

### Radiotherapy — generally avoided

NCIT: `NCIT:C15313` **Radiation Therapy**.

- "Radiotherapy is typically avoided in young children." (consensus, PMID:42527893)
- Used in only ~6 reported cases historically (StatPearls NBK560596); one HNP 2025 patient with incomplete resection received **41.4 Gy** adjuvant RT (PMID:40278957).
- Note the perverse-looking statistic from the 250-case review: recurrence was **66.7%** with combined chemo/radiotherapy vs **12.4%** with surgery alone (PMID:38681460). This is **selection bias**, not a treatment effect — multimodal therapy was reserved for the worst tumours. Do not curate it as evidence against chemo/RT.

### Targeted therapy — proposed, never reported in use

- **Vemurafenib** (BRAF inhibitor) was proposed on the strength of the single BRAF V600E case: "offering potential pathways toward targeted therapeutic approaches for aggressive cases where conventional surgery may be insufficient" (PMID:26122804). **No clinical administration of a BRAF inhibitor to an MNTI patient has been reported.** Curate this as a hypothesis, not a treatment.
- **Epigenetic therapy** — the only *in vitro* pharmacologic signal in MNTI: primary MNTI cell viability "was reduced" by **bromodomain (BET) inhibitors** and "particularly" by **lysine demethylase (KDM) inhibitors** (PMID:27519597). Entirely pre-clinical; `evidence_source: IN_VITRO`.
- **MB-G3-directed therapy** is the forward-looking idea implied by the methylation class but has not been tested in MNTI.
- No immunotherapy, gene therapy, cell therapy, or RNA-based therapy has been applied or proposed.

### Supportive and rehabilitative care

NCIT: `NCIT:C15747` **Supportive Care**; `NCIT:C15302` **Physical Therapy** (not typically relevant).

- Peri-operative feeding support (including nasogastric feeding — `HP:0040288` as a phenotype if curated), airway management, analgesia.
- **Long-term dental/craniofacial rehabilitation** is the main rehabilitative need: staged removable partial dentures through childhood, autologous block bone grafting, and implant-supported definitive restoration in late adolescence (PMID:35400932).

### Experimental treatments

**No clinical trial is recruiting for MNTI.** ClinicalTrials.gov has no MNTI-specific interventional study. The nearest relevant observational study is **NCT05984108** — "Clinical, Radiological, Histologic and Molecular Features of a Cohort of Melanocytic Tumors of the Central Nervous System" — which is **adjacent, not MNTI-specific**; verify its eligibility criteria before citing it as an MNTI trial. Do not curate a `clinical_trials:` block on the basis of a keyword match.

### Side effects and adverse events

No MNTI-specific toxicity data. Toxicities are those of the borrowed regimens (anthracycline cardiotoxicity, alkylator gonadotoxicity and secondary malignancy, platinum ototoxicity and nephrotoxicity, vincristine neuropathy) and are a serious consideration in a 2-month-old. Radiotherapy in an infant carries growth-arrest and second-malignancy risk — the stated reason it is avoided.

### Treatment algorithm and follow-up

1. Infant with a rapidly enlarging craniofacial mass → MRI **and** CT → **biopsy with full IHC panel** (CK, HMB-45, synaptophysin, NSE, S-100, SOX10, Phox2b, desmin/myogenin).
2. Pre-operative urinary VMA (cheap; informative if positive, uninformative if negative).
3. **Resectable** → complete excision with clear margins, as conservative as margins allow; endoscopic assistance for maxillary lesions.
4. **Unresectable or metastatic** → neoadjuvant neuroblastoma-type chemotherapy → delayed complete non-mutilating resection.
5. **R1 margin**, especially under 2 months of age → consider adjuvant chemotherapy.
6. **Recurrence** → re-excision is first choice; chemotherapy for unresectable recurrence.
7. **Surveillance** (from PMID:34359769): weekly clinical examination for the first month; biweekly for 3 months; monthly for 6–12 months post-surgery for maxillary/mandibular tumours. **CNS/skull tumours require MR surveillance for a minimum of 5 years.** Sowmya adds: "A minimum follow-up of four months to two years" with weekly visits in the first month, monthly for four months, then regular surveillance for two years (PMID:38681460).
8. **Long-term:** dental/orthodontic/prosthodontic follow-up to skeletal maturity and beyond.

**Personalized medicine:** essentially none in practice. BRAF genotyping in refractory disease is the only genotype-guided option proposed, and the consensus guidance is for "multidisciplinary, risk-adapted management with structured follow-up protocols" (PMID:42527893) — risk-adapted by resectability and age, not by genotype.

---

## 13. Prevention

**There is no prevention for MNTI, at any level.** This is an honest and complete answer, not a gap.

- **Primary prevention:** not possible. The transforming event is prenatal (detectable from ~12 weeks in one case), sporadic, and has no known modifiable antecedent. No vaccination, no risk-factor modification.
- **Secondary prevention (early detection):** no screening programme exists or is justifiable at ~500 cases per century. The practical equivalent is **clinical vigilance**, which the literature repeatedly emphasizes: "A high index of suspicion is needed to diagnose such a rare tumor, to avoid morbidity and to plan effective management when an infant presents with facial swelling." (PMID:41445906). Prenatal detection on routine obstetric ultrasound is incidental.
- **Tertiary prevention (preventing complications in affected children):** this is where the actionable prevention lies —
  - complete first excision with clear margins **prevents recurrence** (five-fold margin effect);
  - **neoadjuvant chemotherapy prevents mutilating surgery** in initially unresectable tumours;
  - front-loaded post-operative surveillance (weekly in month 1) catches the 80–92% of recurrences that occur within four months while they are still small and re-resectable;
  - early orthodontic/prosthodontic planning prevents fixed malocclusion and growth asymmetry.
- **Immunization:** not applicable.
- **Genetic screening / PGD / prenatal testing:** not applicable — no heritable basis.
- **Behavioural interventions:** not applicable.
- **Genetic counselling:** `NCIT:C15240` **Genetic Counseling** is **not** indicated for MNTI as such. The one scenario in which it arises is the single germline *CDKN2A* case, where counselling would be about *CDKN2A* predisposition (melanoma, pancreatic cancer) in the family rather than about MNTI recurrence risk — and that rests on **n = 1**. Do not generalize it.
- **Public health / environmental interventions:** not applicable.
- **Prophylaxis:** none.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** **`NCBITaxon:9606` (Homo sapiens) only.** A targeted search for veterinary or animal cases of melanotic neuroectodermal tumour returned **no reports in dogs or any other species**; all retrieved literature is human paediatric.
- **Breed (VBO):** not applicable.
- **Orthologous genes:** *CDKN2A*, *BRAF*, *TYR*, *MITF*, *MYC* all have well-characterized orthologs in mouse, rat and zebrafish (Alliance of Genome Resources), but **no ortholog has been linked to an MNTI-like tumour in any species.**
- **Natural disease in other species:** **none reported.** Nothing in OMIA. Pigmented neuroectodermal neoplasms of young animals exist in the veterinary literature (e.g. canine melanocytic and neuroectodermal tumours) but none has been characterized as the MNTI counterpart, and none should be curated as one.
- **Comparative pathology:** the only cross-species comparison in the MNTI literature is *conceptual* — the Barnes transcriptomic comparison against **in-vitro-differentiated human neural crest cells** (GSE28875), which is human-to-human, not cross-species.
- **Evolutionary conservation of mechanism:** the C19MC miRNA cluster at 19q13.41 is **primate-specific**, which is directly relevant: the one deeply characterized MNTI driver lesion cannot be modelled in mouse, because the locus does not exist there. This is a hard constraint on model development and is worth recording as a `HUMAN_MODEL_MISMATCH`-flavoured knowledge gap.
- **Transmission / zoonotic potential / cross-species susceptibility:** not applicable (neoplasm, not transmissible).

---

## 15. Model Organisms

**There is no animal model of MNTI** — no knockout, knock-in, transgenic, conditional, or humanized mouse; no rat, zebrafish, *Drosophila*, or *C. elegans* model; no PDX reported. Nothing in MGI, IMPC, KOMP, IMSR, RGD, ZFIN, FlyBase, or WormBase. Nothing in the Alliance of Genome Resources.

### What does exist

| Model | Type | What it supports | Limitations | Source |
|---|---|---|---|---|
| **Primary MNTI cell culture (fibular case)** | in vitro, patient-derived primary cells | the only pharmacologic data in MNTI: reduced viability with **bromodomain inhibitors** and "particularly" **lysine demethylase inhibitors**; plus RNA-seq and SNP-array characterization | a single patient's tumour; no reported immortalization, passaging characterization, karyotype stability, or independent replication; drug effects on viability only — no in-vivo or orthotopic confirmation; no report that the line is distributed | PMID:27519597 |
| **Historical tissue culture of malignant MNTI** | in vitro | ultrastructural/behavioural description | 1979 methodology; not available; not molecularly characterized | PMID:221089 |
| **Human neural crest cell reference** | in vitro differentiated hNCC | the *comparator* that established TYR overexpression (FPKM 144.2 vs 0.0) | a normal-tissue reference, **not** a disease model — do not curate it as one | GSE28875 |

### Why no model exists, and what it would take

1. **No recurrent driver to engineer.** With BRAF V600E at ~1/14 across both series and *CDKN2A*/*RPLP1::C19MC* at n = 1, there is no consensus lesion to knock in.
2. **The best-characterized lesion is unmodellable in mouse** — C19MC is primate-specific (see §14).
3. **The disease identity is epigenetic, not mutational.** A faithful model would have to reproduce a group-3-medulloblastoma-like methylation state in a cranial neural-crest progenitor at a specific developmental window — which is a developmental-timing problem, not a genotype problem.
4. **The plausible route forward** is an iPSC-derived cranial neural crest model (the lineage the methylation data implicate) carrying *CDKN2A* loss ± C19MC derepression, rather than a mouse. No such model has been reported.

### Research applications currently possible

- Methylation-array classification of new cases against the MB-G3 class (reference centres).
- BRAF V600E genotyping for a targeted option in refractory disease.
- Retrospective clinicopathologic and outcome studies via international collaboration — which is what the field itself asks for: "International collaborative studies with unified standards of management…are mandatory if we are to improve the knowledge and the prognosis" (PMID:34359769); "further collaborative studies to establish standards of management in patients with MNTI are necessary to improve outcomes and diminish sequelae of surgery" (Krawczyk, *EJC Paediatr Oncol* 2024).

### Datasets available for curation

| Accession | Content | Source |
|---|---|---|
| **GEO GSE84431** | RNA-seq + genomic data, the fibular MNTI case | PMID:27519597 |
| **GEO GSE84428** | aCGH sub-series for the same case | PMID:27519597 / OmicsDI |
| **GEO GSE28875** | in-vitro-differentiated human neural crest cells (comparator, **not MNTI**) | PMID:27519597 |

⚠️ **Verify both MNTI accessions with `just verify-datasets` before committing** — the article text names GSE84431 while the dataset indexes surface GSE84428, which suggests a GEO SuperSeries/SubSeries relationship. Fetch each record (`just fetch-reference`) and copy GEO's **own title verbatim** into `datasets[].title`. GSE28875 must not be curated as an MNTI dataset.

---

## Appendix A — Knowledge gaps worth encoding as `discussions`

| Gap | Kind | Why it matters |
|---|---|---|
| Why does **younger age at diagnosis** predict higher recurrence, inverting the usual paediatric pattern? | `KNOWLEDGE_GAP` | The best-replicated prognostic factor in the disease has no proposed mechanism. |
| How does MNTI make melanin with **no MITF elevation**? | `KNOWLEDGE_GAP` | TYR is 144 FPKM vs 0 in hNCC, yet the master melanocytic TF is not up. Attaches to the melanogenesis node. |
| Is the **MB-G3 methylation class** a shared progenitor or a convergent state? | `KNOWLEDGE_GAP` | Determines whether MB-G3-directed therapy is rational in MNTI. n = 7, some calibrated scores at the low band. |
| Does **CNV burden / *MYC* amplification** predict aggressive behaviour? | `KNOWLEDGE_GAP` | Explicitly proposed and explicitly unresolved by the authors; would give MNTI its first molecular risk stratifier. |
| Is **BRAF V600E** real in MNTI at all? | `KNOWLEDGE_GAP` | 1/3 vs 0/11; it gates the only targeted-therapy proposal. |
| **No model system can carry the C19MC lesion** | `HUMAN_MODEL_MISMATCH` | C19MC is primate-specific; the only characterized fusion driver is structurally unmodellable in rodents. The in-vitro BET/KDM sensitivity is single-patient primary culture with no in-vivo confirmation. |
| **Benign (ICD-O `/0`) vs malignant (WHO 5th ed.)** | `KNOWLEDGE_GAP` | An unresolved authority conflict that changes how the entity is coded and counselled. |

## Appendix B — dismech curation notes

- **Granularity (design decisions §3a):** MNTI is a **histologic entity** at the WHO blue-book level → default to a single `DISEASE` entry at `kb/disorders/Melanotic_Neuroectodermal_Tumor_of_Infancy.yaml`. Do **not** split by site (maxillary vs skull vs epididymal MNTI); site is `pathophysiology`/`phenotypes` detail, and the extracranial cases are the same entity. Do **not** split "malignant MNTI" into its own entry — it is a behaviour, not a separate disease.
- **Cell of origin (derived, §3d):** the entry will likely report `ORIGIN_UNMARKED` under `just check-cancer-origin`, because **no recurrent somatic lesion is established** and the one germline lesion is not a somatic initiating event. The honest handling is to leave the origin unmarked and record in `notes:` that no transforming lesion is established in the majority of cases, rather than marking a node `variant_origin: SOMATIC` to satisfy the check. Bind `CL:0011012` / `CL:0000008` on the progenitor node; the derivation rule reads `cell_types` from the marked origin node only.
- **Coarse phenotypes:** `HP:0002664` *Neoplasm* and `HP:0012288` *Neoplasm of head and neck* will trip `just check-coarse-phenotypes`. Likely bases: `NO_HPO_TERM` for the pigmented alveolar mass (HPO has no term for it) and `PATHOGRAPH_HUB` for `HP:0002664` if it becomes a convergence node. Use the `coarse-phenotype-bindings` skill.
- **Prevalence:** encode as `measure_type: CASES_IN_LITERATURE` with `prevalence_class: ULTRA_RARE` and the 472/~500 figures in `notes:`. **Do not populate `rate_per_100000`** — no denominator exists.
- **No `inheritance:` block, no `environmental:` block, no `animal_models:` block.** Each absence is a sourced finding, and each should carry a `notes:` line saying what was searched.
- **`experimental_models:`** the Barnes primary culture belongs here (not in `animal_models:`) with `modeled_mechanisms` → the epigenetic-dependency node, `fidelity: LOW`, `model_scale: MOLECULAR`, and `divergences` of type `BOUNDARY_OMISSION` (single patient, no in-vivo compartment) and `POPULATION_MISMATCH` (n = 1 genotype atypical of the disease).
- **Module conformance candidates:** the Hallmarks-of-cancer family — "Sustaining proliferative signalling" (BRAF/MAPK, rare), "Evading growth suppressors" (CDKN2A/p16INK4A, single case), "Unlocking phenotypic plasticity / non-mutational epigenetic reprogramming" (the methylation class and BET/KDM dependency — the best fit), and `invasion_and_metastasis` only for the 1.4–3% metastatic arm. Run `just list-modules` for current members and anchors before writing `conforms_to`.
- **Every CURIE in this report that I resolved is marked as resolved against a named authority in the section where it appears.** Three are explicitly **not** resolved and must be looked up before binding: the LOINC code for urinary VMA, `UBERON:0000955` (brain), and `NCIT:C154430` (surgical resection). Do not copy them from here without a lookup.

---

## Sources

- [Rachidi et al. Melanotic Neuroectodermal Tumor of Infancy: A Systematic Review. J Oral Maxillofac Surg 2015 (PMID:25936939)](https://pubmed.ncbi.nlm.nih.gov/25936939/)
- [Krawczyk et al. Clinical Guidance for the Management of Melanotic Neuroectodermal Tumor of Infancy — A Consensus by the Expert Group. Pediatr Blood Cancer 2026 (PMID:42527893)](https://pubmed.ncbi.nlm.nih.gov/42527893/)
- [Xia et al. MNTI: A Clinicopathological and BRAF V600E Mutation Study of 11 Cases. Front Oncol 2021 (PMID:34094962)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8173088/) · [full text](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2021.668505/full)
- [MNTI: Clinicopathological Evaluation of a 10-Year Consecutive Case Series from a Tertiary Cancer Center. Head Neck Pathol 2025 (PMID:40278957)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12031676/)
- [Lopez-Nunez et al. MNTI and Pineal Anlage Tumor Harbor A Medulloblastoma Signature by DNA Methylation Profiling. Cancers 2021 (PMID:33572349)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7916108/)
- [Barnes et al. A germline mutation of CDKN2A and a novel RPLP1-C19MC fusion detected in a rare MNTI: a case report. BMC Cancer 2016 (PMID:27519597)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4983003/)
- [Gomes et al. BRAFV600E Mutation in MNTI: Toward Personalized Medicine? Pediatrics 2015 (PMID:26122804)](https://pubmed.ncbi.nlm.nih.gov/26122804/)
- [Styczewska et al. The Role of Chemotherapy in Management of Inoperable, Metastatic and/or Recurrent MNTI. Cancers 2021 (PMID:34359769)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8345623/)
- [Kapadia et al. MNTI. Clinicopathological, immunohistochemical, and flow cytometric study. Am J Surg Pathol 1993 (PMID:8392815)](https://pubmed.ncbi.nlm.nih.gov/8392815/)
- [Khoddami et al. MNTI: a molecular genetic study. Pediatr Dev Pathol 1998 (PMID:10463291)](https://pubmed.ncbi.nlm.nih.gov/10463291/)
- [Janardhanan et al. Melanotic Neuroectodermal Tumour of Infancy. Head Neck Pathol 2023 (PMID:36853558)](https://pubmed.ncbi.nlm.nih.gov/36853558/)
- [Sowmya et al. MNTI of Jaws: A Case Report and Review of Literature. Cureus 2024 (PMID:38681460)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11055504/)
- [MNTI: A Case Report and Literature Review. South Asian J Cancer 2023 (PMID:41445906)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12727035/)
- [Khizar et al. MNTI: A report of two cases from Pakistan. Pak J Med Sci 2025 (PMID:41522382)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12790020/)
- [Nazir et al. MNTI: discussion of a case and a review of the imaging findings. Cancer Imaging 2009 (PMID:20080455)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2821590/)
- [Santos et al. Clinical and immunohistochemical study of MNTI in the maxilla. Einstein (São Paulo) 2018 (PMID:29768520)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5998940/)
- [Mandibular MNTI: Interdisciplinary Treatment from 2 Months to 19 Years of Age. J Maxillofac Oral Surg 2021 (PMID:35400932)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8934838/)
- [Melanotic Neuroectodermal Tumor of Infancy — StatPearls, NCBI Bookshelf NBK560596](https://www.ncbi.nlm.nih.gov/books/NBK560596/)
- [Koob et al. Prenatal diagnosis of orbital melanotic neuroectodermal tumor in infancy. Ultrasound Obstet Gynecol 2015](https://obgyn.onlinelibrary.wiley.com/doi/10.1002/uog.14787)
- [Krawczyk et al. Focus on melanotic neuroectodermal tumor of infancy. EJC Paediatr Oncol 2024;3:100141](https://www.researchgate.net/publication/376985239_Focus_on_melanotic_neuroectodermal_tumor_of_infancy)
- [WHO Classification of Tumours, 5th ed., Vol. 7: Paediatric Tumours (IARC, 2023)](https://publications.iarc.who.int/Book-And-Report-Series/Who-Classification-Of-Tumours/Paediatric-Tumours-2023)
- [MONDO:0002072 via EBI OLS4](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMONDO_0002072) · [MeSH D017600](https://id.nlm.nih.gov/mesh/D017600.json) · [HPO API](https://ontology.jax.org/) · [HGNC REST](https://rest.genenames.org/)
- [Pathology Outlines — Melanotic neuroectodermal tumor of infancy](https://www.pathologyoutlines.com/topic/mandiblemaxillaPigNEtumor0.html) (rate-limited during this session; listed for follow-up, not cited above)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 40 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 38 |
| Quoted claims found in source | 9 |
| Quoted claims **not** found in source | 29 |
| References weighed for topical relevance | 40 |
| On topic | 30 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

18 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:41522382` *(abstract only)*: "rapidly growing, painless scalp swelling without neurological deficit"
  - closest text in source: "We are presenting here two rare cases, including a six months old girl with right orbitotemporal swelling and a three months old boy with right temporal swelling"
- `PMID:34359769`: "presence of neuroblast-like cells correlated with aggressiveness; neoadjuvant CHT preferentially reduced small round blue cell components"
  - closest text in source: "In cases evaluated histologically both before and after CHT, the CHT resulted in almost complete reduction of the small round blue cell component of MNTI; however, the reduction of epithelioid cells was poor [4,62]"
- `PMID:41445906` *(abstract only)*: "Most of the recurrences occur within the first 6 months of therapy"
  - closest text in source: "In the last 100 years since the first description of MNTI, only around 500 cases have been described from 32 countries"
- `PMID:38681460`: "Mean recurrence time: 3.26 months (range: 15 days–20 months); **92% of recurrences occurred within four months**"
  - closest text in source: "Regular follow-up is a requisite during the initial months of surgery or other forms of management as MNTI has a high incidence of recurrence during the initial months itself, with a mean recurrence time of 3.26 months and a maximum of 20 months, and 92% of recurrences are within four months"
- `PMID:41522382` *(abstract only)*: "accounting for approximately 500 cases globally"
  - closest text in source: "Despite their very aggressive growth, they are mostly benign in nature, commonly involving the maxilla, but in very rare cases, the skull and brain have also been seen to be affected"
- `PMID:41445906` *(abstract only)*: "MNTI shows a wide geographic variation, however, the highest prevalence of MNTI has been reported from the **United States** followed by **India**"
  - closest text in source: "In the last 100 years since the first description of MNTI, only around 500 cases have been described from 32 countries"
- `PMID:40278957`: "All cases demonstrated classic biphasic morphology with smaller neuroblast-like cells and larger melanin-containing epithelioid cells."
  - closest text in source: "Microscopically, it consists of a biphasic population of small neuroblast-like cells and larger melanin-containing epithelioid cells"
- `PMID:29768520`: "strongly and diffusely positive in epithelioid cells"
  - closest text in source: "Immunohistochemically, the melanocyte-like component was strongly and diffusely positive for HMB-45 and Melan-A, but weakly positive for S100"
- `PMID:29768520`: "MNTI commonly does not express diffuse reactivity with S-100, which helps distinguish it from similar lesions."
  - closest text in source: "Melanotic neuroectodermal tumor of infancy may share a common histological and immunophenotypic expression with other lesions, such as cellular blue nevus, melanoma, neuroblastoma, and rhabdomyosarcoma, but MNTI commonly does not express diffuse reactivity with S-100,( 2 , 3 , 6 , 8 ) as observed in our case"
- `PMID:41445906` *(abstract only)*: "Some employ the measurement of urinary vanillylmandelic acid (VMA) levels; however, **it can be negative even in recurrent cases**."
  - closest text in source: "In the last 100 years since the first description of MNTI, only around 500 cases have been described from 32 countries"
- `PMID:41522382` *(abstract only)*: "positive results in only **two of 18** preoperatively tested patients"
  - closest text in source: "We are presenting here two rare cases, including a six months old girl with right orbitotemporal swelling and a three months old boy with right temporal swelling"
- `PMID:35400932` *(abstract only)*: "One week later the levels of the VMA in urine returned to normal limits."
  - closest text in source: "A well-defined lesion in the left mandible shown on MRI and high urine vanillylmandelic acid (VMA) level determined the diagnosis"
- `PMID:42527893` *(abstract only)*: "local imaging through MRI and CT with histopathological confirmation"
  - closest text in source: "Diagnosis requires local imaging assessment with magnetic resonance imaging (MRI) and computed tomography (CT) and histopathological confirmation"
- `PMID:26122804` *(abstract only)*: "as a potential predictive biomarker for vemurafenib therapy"
  - closest text in source: "However, as there are no conclusive data regarding the molecular profile of this tumor, currently there is no targeted therapy that may be used in the treatment of selected aggressive cases"
- `PMID:34094962`: "as a potential predictive biomarker for vemurafenib therapy"
  - closest text in source: "The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest"
- `PMID:34359769`: "complete, non-mutilating delayed surgery"
  - Text part not found as substring: 'complete, non-mutilating delayed surgery'
- `PMID:20080455` *(abstract only)*: "Without free margins, recurrence increases **five-fold**"
  - Text part not found as substring: 'Without free margins, recurrence increases **five-fold**' (note: only abstract available for PMID:20080455, full text may contain this excerpt)
- `PMID:25936939` *(abstract only)*: "the recurrence rate for tumours seen in patients younger than two months of age is **quadruple** that of tumours seen in patients 4.5 months of age and older"
  - closest text in source: "This investigation uncovered age at diagnosis as an important prognostic indicator, because younger age correlated with a higher recurrence rate"
- `PMID:34359769`: "Recurrence highest in children diagnosed within first 2 months; minimal risk beyond 4-5 months"
  - closest text in source: "In children diagnosed within the first 2 months of life, the recurrence rate is the highest, while in those beyond 4, 5 months of age it is minimal [1]"
- `PMID:38681460`: "**80% of malignant cases showed recurrence**"
  - closest text in source: "The association between the presence of malignancy and the recurrence shows that among cases without malignancy, 211 (86.1%) cases showed no recurrence, while 34 (13.9%) cases experienced a recurrence"
- `PMID:34359769`: "Aneuploidy, necrosis, and high mitotic figures suggested as potential negative factors, **though not definitively established**"
  - closest text in source: "Some authors implied that the presence of necrosis and mitotic figures may be associated with a malignant course of disease [53]"
- `PMID:20080455` *(abstract only)*: "Wide surgical excision with at least **5 mm** of healthy margins."
  - Text part not found as substring: 'Wide surgical excision with at least **5 mm** of healthy margins.' (note: only abstract available for PMID:20080455, full text may contain this excerpt)
- `PMID:25936939` *(abstract only)*: "found no difference in recurrence rates in patients treated by curettage only and patients who underwent resection"
  - closest text in source: "The authors performed a systematic review of the 472 reported cases from 1918 through 2013 and provided a comprehensive update on this rare entity that can have devastating effects on young patients"
- `PMID:41445906` *(abstract only)*: "There is no difference in recurrence rates between both the modality of treatment"
  - closest text in source: "A high index of suspicion, early diagnosis, and timely treatment are needed to diagnose such a rare tumor, to avoid morbidity, and to plan effective management when an infant presents with facial swelling"
- `PMID:42527893` *(abstract only)*: "Radiotherapy is typically avoided in young children."
  - closest text in source: "Chemotherapy may be considered for advanced disease, whereas radiotherapy is generally avoided in young children"
- `PMID:26122804` *(abstract only)*: "offering potential pathways toward targeted therapeutic approaches for aggressive cases where conventional surgery may be insufficient"
  - closest text in source: "However, as there are no conclusive data regarding the molecular profile of this tumor, currently there is no targeted therapy that may be used in the treatment of selected aggressive cases"
- `PMID:42527893` *(abstract only)*: "multidisciplinary, risk-adapted management with structured follow-up protocols"
  - closest text in source: "Multidisciplinary, risk-adapted management, and structured follow-up are essential."
- `PMID:41445906` *(abstract only)*: "A high index of suspicion is needed to diagnose such a rare tumor, to avoid morbidity and to plan effective management when an infant presents with facial swelling."
  - closest text in source: "A high index of suspicion, early diagnosis, and timely treatment are needed to diagnose such a rare tumor, to avoid morbidity, and to plan effective management when an infant presents with facial swelling"
- `PMID:34359769`: "International collaborative studies with unified standards of management…are mandatory if we are to improve the knowledge and the prognosis"
  - closest text in source: "International collaborative studies with unified standards of management of children with inoperable, metastatic or persistently recurring MNTI and prospective enrollment in national or international databases are mandatory if we are to improve the knowledge and the prognosis of children with these rare types of MNTI"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `GEO:GSE28875` (5 mentions) - RNA-seq experiments in human neural crest cells (hNCC)
  - shared terms: cell

Weighed against this report's own most characteristic terms: `mnti`, `tumour`, `disease`, `cell`, `lesion`, `serie`, `tumor`, `patient`, `month`, `clinical`, `braf`, `exist`, `year`, `age`, `methylation`, `bone`, `diagnosis`, `metastatic`, `recurrence`, `neoplasm`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 68 |
| Resolved | 68 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 18 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0002072` (3 mentions) - the report calls it "MONDO"; MONDO calls it **melanotic neuroectodermal tumor**
- `DOID:166` (1 mention) - the report calls it "DOID"; DOID calls it **melanotic neuroectodermal tumor**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCIT:C3717` (2 mentions) - the report calls it "NCIT"; NCIT calls it **Melanotic Neuroectodermal Tumor**, and lists "MNTI" among its other names
