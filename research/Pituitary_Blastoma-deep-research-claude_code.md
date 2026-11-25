---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-11-20T20:06:52.541013'
end_time: '2026-11-20T20:21:31.579585'
duration_seconds: 879.04
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Pituitary Blastoma
  mondo_id: MONDO:0858916
  category: ''
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: not recorded
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
  web_search_requests: 52
  num_turns: 53
  total_cost_usd: 4.9430080000000025
  session_id: 29865d6e-998c-4bd2-8505-81d92a9c904c
  stop_reason: end_turn
  tool_calls: 52
  retrieval_calls: 52
  assistant_text_blocks: 2
citation_count: 103
reference_validation:
  total_references: 49
  verified: 47
  not_found: 2
  unverifiable: 0
  confabulation_rate: 0.041
  quotes_checked: 20
  quotes_valid: 5
  quotes_unsupported: 15
  unsupported_quote_references:
  - PMID:33644822
  - DOI:10.3389/fonc.2020.614541
  - PMC:PMC4712775
  - PMC:PMC7823240
  - PMC:PMC8568902
  - PMID:29343557
  - PMID:39400264
  - PMC:PMC11649450
  - PMC:PMC9587932
  - PMC:PMC11140907
  quotes_not_checkable: 13
  relevance_assessed: 47
  on_topic: 31
  unresolved_references:
  - PMID:41912509
  - PMC:PMC11475256
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 18
  verified: 13
  not_found: 0
  obsolete: 0
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0858916
    reported_labels:
    - Mondo
    ontology_label: pituitary blastoma
  - term_id: DOID:0081244
    reported_labels:
    - Disease Ontology
    ontology_label: pituitary blastoma
  unresolvable_prefixes:
  - ORPHA
  - MGI
  - RGD
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pituitary Blastoma
- **MONDO ID:** MONDO:0858916 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** 

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Pituitary Blastoma** covering all of the
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

I'll research this now, starting with the core identifiers and primary literature.

# Comprehensive Research Report: Pituitary Blastoma (MONDO:0858916)

## Interpretation note and scope

**The disease researched here is pituitary blastoma (PitB), MONDO:0858916, whose causal gene is *DICER1* (HGNC:17098; OMIM \*606241; 14q32.13; NCBI Gene 23405; Ensembl ENSG00000100697; UniProt Q9UPY3).** The template listed the causal gene as "not recorded"; the retrieved literature establishes *DICER1* as the single causal gene, and MedGen's definition for this exact concept states that pituitary blastoma is "a pituitary cancer characterized by features of Cushing disease, with elevated blood ACTH levels and hypercortisolism arising within the fetal anterior pituitary and associated with DICER1 mutations" ([MedGen C4743978 / UID 1656462](https://www.ncbi.nlm.nih.gov/medgen/1656462)). No competing gene or similarly named entity was identified.

**Two methodological caveats the reader should weigh.** (1) In this session I had web search available but **no full-text fetch tool**. All claims below are therefore grounded in material surfaced by retrieval, but the "direct quotes" are sentences as they appeared in retrieved search-result renderings of abstracts/pages rather than verified character-by-character against publisher full text. I flag quotations as such. (2) Where I could not retrieve a value (several PMIDs, Orphanet/OMIM-specific PitB entries, CL and NCIT identifiers, NCBI Taxon IDs, incidence rates), I say so explicitly rather than supplying it from memory.

---

## 1. Disease Information

### Overview

Pituitary blastoma is an ultra-rare malignant embryonal neoplasm of the **anterior pituitary (adenohypophysis)** that occurs almost exclusively in infants under 2 years of age and is **pathognomonic for *DICER1* tumor predisposition syndrome**. It was first defined as an entity in 2008 by Scheithauer and colleagues at the Mayo Clinic, who named it to reflect the ultrastructural resemblance of the tumor to the **10–12 week stage of embryonic pituitary development** ([Scheithauer et al., *Acta Neuropathol* 2008;116:657–666, PMID 18551299](https://link.springer.com/article/10.1007/s00401-008-0388-9); [Scheithauer et al., *Pituitary* 2012;15(3):365–73, PMID 21805093](https://pubmed.ncbi.nlm.nih.gov/21805093/)).

Retrieved descriptions of its defining pathology: the tumor "exhibits differentiation to Rathke epithelium and adenohypophysial cells of folliculostellate and secretory type, **a reflection of arrested pituitary development and unchecked proliferation**" ([*Pituitary* 2012, PMID 21805093](https://pubmed.ncbi.nlm.nih.gov/21805093/)). The 2008 paper's rationale for the name rested on "(a) prominence of primitive Rathke-type epithelium, (b) disposition of secretory cells in lobules rather than acini, (c) the limited range of secretory cells represented, (d) the presence of their corresponding transcription factors, and (e) ultrastructural features indicating orderly development of the 10- to 12-week embryonic stage" ([*Acta Neuropathol* 2008](https://link.springer.com/article/10.1007/s00401-008-0388-9)).

### Key identifiers

| Resource | Identifier | Source |
|---|---|---|
| Mondo | **MONDO:0858916** | [MedGen cross-ref](https://www.ncbi.nlm.nih.gov/medgen/1656462) |
| MedGen | UID **1656462**; CUI **C4743978**; semantic type *Neoplastic Process* | [MedGen](https://www.ncbi.nlm.nih.gov/medgen/1656462) |
| HPO | **HP:0034921** ("Pituitary blastoma"; def. "a distinctive anterior hypophyseal tumor of infants") | [MedGen](https://www.ncbi.nlm.nih.gov/medgen/1656462) |
| Disease Ontology | **DOID:0081244** | [MGI/DO browser](https://www.informatics.jax.org/disease/DOID:0081244) |
| ICD-O-3 | **8273/3** (morphology), topography **C75.1** (pituitary gland) | [ICD-O listing](http://notasalud.com/cie-o/m-8273-3); [ICD-O-3.2 change list, ENCR](https://www.encr.eu/sites/default/files/inline-files/Changes%20ICD-O-3.2.pdf) |
| WHO classification | Recognized anterior-lobe tumour type in the 2017 WHO pituitary classification and retained in the 2021 CNS5 / 2022 ENDO5 5th editions | [Overview of the 2022 WHO Classification of Pituitary Tumors, *Endocr Pathol*](https://link.springer.com/article/10.1007/s12022-022-09703-7) |
| Causal gene (OMIM) | *DICER1* **\*606241** | [OMIM 606241](https://omim.org/entry/606241) |
| Related syndromic OMIM entry | **#601200** PLEUROPULMONARY BLASTOMA; PPB (the *DICER1*-syndrome phenotype entry) | [OMIM 601200](https://omim.org/entry/601200) |
| EFO | EFO_1000478 appeared in retrieval alongside this concept but I could not confirm its label — **unverified** | [EBI OLS4](https://www.ebi.ac.uk/ols4/ontologies/efo/entities?short_form=EFO_1000478) |
| Orphanet | **No dedicated ORPHA entry retrieved** for pituitary blastoma (searches returned pituitary adenoma ORPHA:91349 and pulmonary blastoma ORPHA:64741 instead) | [Orphanet search results](https://www.orpha.net/en/disease/detail/64741) |
| MeSH | **No specific MeSH descriptor retrieved** for pituitary blastoma | — |
| ICD-10/ICD-11 | No PitB-specific code retrieved; coded by morphology (ICD-O 8273/3) with pituitary neoplasm topography | — |

### Synonyms

Per MedGen: **Pituitary blastoma; Pituitary embryoma; Pituitary gland blastoma; Pituitary gland embryoma** ([MedGen](https://www.ncbi.nlm.nih.gov/medgen/1656462)). "PitB" is the standard literature abbreviation.

### Provenance of the information

All disease-level knowledge derives from **aggregated case series, registry data, and pathology reviews**, not from EHR/phenotype-at-scale resources. The principal data source is the **International PPB/DICER1 Registry** (founded 1987; >700 enrolled individuals with PPB/*DICER1* conditions; [NCT03382158](https://clinicaltrials.gov/study/NCT03382158)), supplemented by multi-institutional pathology cohorts ([de Kock et al., *Acta Neuropathol* 2014;128:111–122](https://link.springer.com/article/10.1007/s00401-014-1285-z); [Liu et al., *J Clin Endocrinol Metab* 2021;106(2):351, PMC7823240](https://pmc.ncbi.nlm.nih.gov/articles/PMC7823240/)). Because the total world literature is on the order of **~17–23 cases**, essentially every published statement is derived from small-n human clinical/pathological evidence.

---

## 2. Etiology

### Disease causal factors

Pituitary blastoma is a **monogenic, two-hit germline–somatic tumor** with no established non-genetic contributor.

- **Germline first hit:** heterozygous loss-of-function *DICER1* variant. In the defining cohort, "**nine of ten tested infants with pituitary blastoma harbored a heterozygous germ-line *DICER1* mutation**" ([de Kock et al. 2014](https://link.springer.com/article/10.1007/s00401-014-1285-z), as surfaced in retrieval).
- **Somatic second hit:** "**Nine of ten tested PitB tumor samples harbored additional *DICER1* mutations, eight of which were confirmed to be somatic in origin**" ([de Kock et al. 2014](https://link.springer.com/article/10.1007/s00401-014-1285-z)). The index case report had already shown both hits in one patient: *Germline and somatic DICER1 mutations in a pituitary blastoma causing infantile-onset Cushing's disease* ([*JCEM* 2014;99(8):E1487, PMID 24823459](https://pubmed.ncbi.nlm.nih.gov/24823459/)).
- **The second hit is a hotspot missense in the RNase IIIb domain.** "Most of the tumors in this syndrome occur in affected individuals with one inherited *DICER1* mutation, mainly a loss-of-function mutation, and an acquired somatic missense *DICER1* mutation within five hotspot codons in the RNase IIIb domain (**E1705, D1709, G1809, D1810 and E1813**)" (retrieved synthesis; see [*Cancers* 2025 review of DICER1 pathogenetic mechanisms](https://www.mdpi.com/2072-6694/17/17/2885) and [Foulkes et al., *Nat Rev Cancer* 2014](https://www.nature.com/articles/nrc3802)).
- **Germline mutation alone is insufficient:** "Germline mutation in one *DICER1* allele is insufficient for oncogenesis, and a second hit on the other allele is required, as a result of postnatal somatic mutation" (retrieved).
- **Near-complete attribution to *DICER1*:** the largest clinical cohort states "**Molecular and/or clinical evidence implicates *DICER1* in 16 of the 17 pituitary blastoma cases**" ([Liu et al., *JCEM* 2021](https://academic.oup.com/jcem/article/106/2/351/6000434)); the parallel molecular study reports "**Sixteen of seventeen pituitary blastoma cases were attributed to *DICER1* abnormalities**" ([Nadaf/de Kock et al., *Acta Neuropathol* 2021;141:929–944, PMID 33644822](https://pubmed.ncbi.nlm.nih.gov/33644822/)). On this basis PitB "may be considered **pathognomonic** for DICER1 syndrome" ([*Cancers*/review retrieval](https://www.mdpi.com/2673-5261/5/3/19)).

### Risk factors

**Genetic**
- **Causal:** germline heterozygous *DICER1* pathogenic/likely pathogenic (P/LP) variant — the dominant and essentially only known risk determinant.
- **Carrier background rate:** population prevalence of *DICER1* P/LP variation was estimated at **1:870–1:2,529** in ExAC-nonTCGA (53,105 exomes) by in-silico classifiers, and at a stringent **1:10,600** when restricted to loss-of-function plus previously published pathogenic variants ([Kim J et al., *Int J Cancer* 2017](https://onlinelibrary.wiley.com/doi/abs/10.1002/ijc.30907); see also [Kim J et al., *Mol Genet Genomic Med* 2019, PMC6418698](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6418698/)).
- **Mosaicism as a severity modifier:** mosaic RNase IIIb hotspot variants produce a "highly penetrant and severe phenotype … compared with patients with classic DICER1 syndrome caused by germline loss-of-function pathogenic variants," and patients with mosaic hotspot mutations "are more prone to manifestations in multiple sites" ([retrieved review](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2020.614541/full); [GLOW syndrome description](https://www.researchgate.net/publication/261187740_Expanding_the_phenotype_of_mutations_in_DICER1_mosaic_missense_mutations_in_the_RNase_IIIb_domain_of_DICER1_cause_GLOW_syndrome)).
- **Modifier genes:** **none identified** for PitB in retrieved literature.

**Demographic / environmental**
- **Age** is the dominant non-genetic risk descriptor: PitB occurs "exclusively in children under 2 years of age" in classical series ([Liu et al., *Acta Neuropathol* 2022;143:415–417, PMID 35129635](https://pubmed.ncbi.nlm.nih.gov/35129635/)), with median age at diagnosis **11 months** ([Liu et al., *JCEM* 2021](https://academic.oup.com/jcem/article/106/2/351/6000434)).
- **Sex:** 10 girls vs 7 boys in the 17-case cohort ([Liu et al., *JCEM* 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC7823240/)) — no established sex predilection at this sample size.
- **Family history** of DICER1-spectrum tumors (PPB, cystic nephroma, multinodular goiter, SLCT) is a risk indicator for carrier status.
- **No toxin, radiation, occupational, dietary, or infectious risk factor** for PitB was identified in any retrieved source. Searches of toxicogenomic/environmental framings returned nothing PitB-specific.

### Protective factors

- **Genetic protective factors:** none reported. *DICER1* is strongly loss-of-function–constrained (pLI 1.0; LOEUF 0.28; LoF observed/expected 0.09 — retrieved from gnomAD-derived constraint summaries and [ClinGen dosage curation, HGNC:17098](https://search.clinicalgenome.org/kb/gene-dosage/HGNC:17098)), which argues against common protective LoF alleles.
- **Environmental/lifestyle protective factors:** none identified. Given a congenital-onset, two-hit somatic mechanism in the first two years of life, there is no plausible retrieved lifestyle target.
- The only *actionable* "protection" is **secondary**: early detection through *DICER1* surveillance (Section 13).

### Gene–environment interactions

**No gene–environment interaction has been described for pituitary blastoma.** The closest retrieved concept is a *gene–developmental timing* interaction rather than a GxE one: the **temporal order** of the RNase IIIb and loss-of-function hits during development determines phenotype in DICER1 syndrome, described as "a unique variant of the two-hit tumor suppression model" ([Brenneman et al., *F1000Research* 2015;4:214, PMC4712775](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4712775/)). One clinically relevant iatrogenic interaction is flagged in the literature: "**Radiation therapy for pituitary blastoma must be considered with special caution**" in a radiation-sensitive, tumor-predisposed infant ([Liu et al., *JCEM* 2021](https://academic.oup.com/jcem/article/106/2/351/6000434)).

---

## 3. Phenotypes

The best frequency data come from the 17-patient multi-institutional cohort. Direct quote as retrieved: "**The median age at diagnosis was 11 months, and the most frequent presentations were Cushing syndrome (n=10), cranial nerve palsies including ophthalmoplegia (n=7), reduced visual acuity (n=4), developmental delay (n=4), and symptoms of increased intracranial pressure (n=3)**" ([Liu et al., *JCEM* 2021;106(2):351](https://academic.oup.com/jcem/article/106/2/351/6000434)).

| Phenotype | Type | Frequency | Onset | Severity / course | Suggested HPO |
|---|---|---|---|---|---|
| **Cushing syndrome / ACTH-dependent hypercortisolism** | Clinical sign + lab abnormality | **10/17 (~59%)** | Infancy (median 11 mo) | Severe, progressive; life-threatening in infancy | *Cushingoid* phenotype term — **HPO ID not verified in this session**; pair with "Increased circulating ACTH level" (ID unverified) and *Hypercortisolism* |
| **Cranial nerve palsy / ophthalmoplegia** | Clinical sign | **7/17 (~41%)** | Infancy | Moderate–severe, progressive with mass growth | **HP:0000602** Ophthalmoplegia ([HPO def. "Paralysis of one or more extraocular muscles…"](https://monarchinitiative.org/HP:0000873)) |
| **Reduced visual acuity** | Clinical sign | **4/17 (~24%)** | Infancy | Often permanent; 4 survivors had chronic visual deficits | **HP:0000505** Visual impairment |
| **Developmental delay** | Behavioral / neurodevelopmental | **4/17 (~24%)** | Infancy | Variable; 3 survivors had chronic neurodevelopmental deficit | *Global developmental delay* (ID unverified) |
| **Raised intracranial pressure** (headache, emesis) | Clinical sign | **3/17 (~18%)** | Infancy | Acute/subacute, progressive | *Increased intracranial pressure* (ID unverified) |
| **Diabetes insipidus** | Clinical sign + lab | Reported in individual cases (e.g. 13-month-old with Cushing disease *and* DI; a 10-month-old presenting with DI) | Infancy | Chronic, requires replacement | **HP:0000873** Diabetes insipidus |
| **Hyperprolactinemia** | Lab abnormality | Single case (young adult) — "Unlike most reported cases, which present with Cushing's syndrome or ophthalmoplegia, this patient had an **elevated prolactin level, a feature not previously described in pituitary blastoma**" ([Das et al., *Neuropathology* 2025;45(4), PMID 40451220](https://pubmed.ncbi.nlm.nih.gov/40451220/)) | Young adult | — | *Hyperprolactinemia* (ID unverified) |
| **GH immunoexpression / GH-related features** | Lab / pathology | Minority ("ACTH or, **less often**, growth hormone immunoexpression") | Infancy | — | *Growth hormone excess* (ID unverified) |
| **Panhypopituitarism (post-treatment sequela)** | Lab + clinical | Up to panhypopituitarism in survivors; neuroendocrine deficits in **8** of the cohort | Post-treatment, lifelong | Chronic, treatment-induced/destructive | **HP:0000871** Panhypopituitarism |
| **Precocious puberty** | Clinical sign | Listed as a feature to assess for in *DICER1* carriers with pituitary pathology | Childhood | — | *Precocious puberty* (ID unverified) |

**Laboratory abnormality profile (biochemistry).** In infantile ACTH-dependent Cushing syndrome of pituitary origin, "aside from blood adrenocorticotropin (ACTH) and cortisol elevation, other pituitary hormone blood levels were normal or markedly reduced," with elevated 17-OHP and testosterone and raised urinary 17-ketosteroids/17-hydroxycorticoids reported ([retrieved from *Endotext*, Cushing Syndrome/Disease in Children and Adolescents, NBK602210](https://www.ncbi.nlm.nih.gov/sites/books/NBK602210/)). *Endotext* also states directly: "**Infantile onset of ACTH-dependent Cushing syndrome with a pituitary lesion is often due to a pituitary blastoma**" and that "*DICER1* gene defects in these patients suggest that pituitary blastoma is a rare but almost pathognomonic presentation of DICER1 syndrome."

**Quality-of-life impact.** No EQ-5D/SF-36/PROMIS data exist for PitB (retrieval found HRQoL instruments applied to **PPB**, not PitB: [HRQoL in children with PPB, PMC9974753](https://pmc.ncbi.nlm.nih.gov/articles/PMC9974753/)). The nearest PitB-specific statement is from the outcomes cohort: survivors "experienced hormonal sequelae ranging from **none to panhypopituitarism** and neurocognitive function ranging from **fully functional to impaired**, with some survivors being visually impaired" ([Liu et al., *JCEM* 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC7823240/)). Per-phenotype QoL weights are **not available**.

---

## 4. Genetic / Molecular Information

### Causal gene

**\*DICER1* (dicer 1, ribonuclease III)** — HGNC:17098; OMIM \*606241; NCBI Gene 23405; Ensembl ENSG00000100697 (GRCh38 chr14:95,086,228–95,158,010); UniProt Q9UPY3; cytoband **14q32.13** ([NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/23405); [Ensembl](https://www.ensembl.org/Homo_sapiens/Gene/Summary?db=core&g=ENSG00000100697&r=14:95086228-95158010); [OMIM 606241](https://omim.org/entry/606241); [Monarch HGNC:17098](https://monarchinitiative.org/HGNC:17098)).

Function: "DICER1 encodes a ribonuclease III enzyme that processes long double-stranded RNA and precursor microRNAs into mature siRNAs and miRNAs, enabling sequence-specific gene silencing through the RNA-induced silencing complex"; it "cleaves the pre-miRNA hairpin to its mature double-stranded length of around 22 nucleotides" in complex with TARBP2 or PRKRA/PACT ([NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/23405); [Human Protein Atlas DICER1](https://www.proteinatlas.org/ENSG00000100697-DICER1/summary/gene)).

### Pathogenic variants

**Germline (first hit) — loss of function.** "One allele exhibits a pathogenic loss-of-function variant, such as a nonsense, frameshift, or splice-site variant, which can be inherited in an autosomal dominant fashion or can arise de novo" ([GeneReviews, *DICER1*-Related Tumor Predisposition, NBK196157](https://www.ncbi.nlm.nih.gov/sites/books/NBK196157/)). In one retrieved series of 43 germline *DICER1* P variants the distribution was **frameshift 39.5% (17/43), nonsense 30.2% (13/43), splicing 18.6% (8/43), missense 4.6% (2/43), large intragenic deletion 2.3% (1/43)**. Intronic/deep-splice and platform-domain missense variants are now also recognized ([Intronic germline *DICER1* variants in SLCT, *JCO PO* 2023](https://ascopubs.org/doi/10.1200/PO.23.00189); [*DICER1* platform domain missense variants inhibit miRNA biogenesis, PMC10273190](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10273190/)). A gene-specific ACMG/AMP specification exists: [ClinGen *DICER1* ACMG/AMP specifications v1](https://clinicalgenome.org/site/assets/files/8147/clingen_dicer1_acmg_specifications_dicer1_v1.pdf).

**Somatic (second hit) — RNase IIIb hotspot missense.** Codons **E1705, D1709, G1809, D1810, E1813** encode "key amino acids in the metal-binding catalytic cleft" (retrieved). c.5113G>A p.(E1705K) is the single most frequently reported hotspot allele across DICER1 tumors (reported as 16/20, 80%, of analyzed ovarian Sertoli–Leydig cell tumors in [*Mod Pathol* 2015](https://www.nature.com/articles/modpathol2015115); PitB-specific hotspot frequencies were not retrieved at codon resolution).

**Classification and allele frequency.** Pathogenic *DICER1* LoF variants "were absent or sufficiently rare in gnomAD as of February 2022" (retrieved from GeneReviews-derived material); *DICER1* shows **pLI 1.0, LOEUF 0.28, LoF o/e 0.09**, and ClinGen assigns a **haploinsufficiency score of 3** ("sufficient evidence for haploinsufficiency") ([ClinGen dosage](https://search.clinicalgenome.org/kb/gene-dosage/HGNC:17098)). ClinVar carries a dedicated condition label "*DICER1*-related pleuropulmonary blastoma cancer predisposition syndrome" (e.g. [RCV000226155 for c.2026C>T p.Arg676Ter](https://www.ncbi.nlm.nih.gov/clinvar/RCV000226155.7/)). **I did not retrieve a current total count of ClinVar *DICER1* P/LP submissions and therefore do not state one.**

**Germline vs somatic, and functional consequence.** The architecture is **germline LoF (haploinsufficiency) + somatic hypomorphic/neomorphic missense**. Mechanistically this is *not* simple biallelic loss: the hotspot allele retains RNase IIIa activity while abolishing RNase IIIb-mediated 5p cleavage, so the net effect is **selective loss of function for 5p miRNAs with gain of function for 3p passenger miRNAs** — "the Dicer hotspot mutation is not merely a loss-of-function mutation for 5p-miRNAs but also a **gain-of-function mutation for passenger 3p-miRNAs**" ([*Nat Struct Mol Biol* 2025, "DICER1 hotspot mutation induces 3p microRNA gain of function via Argonaute strand switch"](https://www.nature.com/articles/s41594-025-01671-w)).

### Modifier genes

None established. In PitB specifically, whole-genome sequencing "demonstrated a **quiet genome with very few somatic alterations**," arguing against cooperating somatic drivers ([Nadaf/de Kock et al., *Acta Neuropathol* 2021;141:929–944](https://link.springer.com/article/10.1007/s00401-021-02283-6)).

### Epigenetic information

PitB has a **distinct DNA methylation class**: "The comparison of methylation profiles to publicly available data from approximately 3000 other central nervous system tumors revealed that pituitary blastomas have a **distinct methylation profile compared to all other tumors, including pituitary adenomas**," and "methylation profiling confirms clustering among pituitary blastoma samples and references" ([*Acta Neuropathol* 2021;141:929–944, PMID 33644822](https://pubmed.ncbi.nlm.nih.gov/33644822/)). No PitB-specific histone-modification or chromatin-accessibility data were retrieved; ENCODE/Roadmap/DiseaseMeth searches returned no PitB entries.

### Chromosomal abnormalities

None characteristic. WGS shows a quiet genome (above). No aneuploidy, translocation, or recurrent CNV has been reported for PitB; DECIPHER/dbVar searches returned nothing PitB-specific. (By contrast, the *DICER1*-mutant **primary intracranial sarcoma** that can arise in the sella carries additional TP53 mutation and ATRX inactivation — see Section 10 differential.)

---

## 5. Environmental Information

- **Environmental factors:** **None identified.** No toxin, pollutant, radiation, or occupational exposure has been associated with pituitary blastoma in any retrieved source. The one environmental agent discussed in the literature is **therapeutic ionizing radiation as an iatrogenic hazard**, not a cause: "Radiation therapy for pituitary blastoma must be considered with special caution" ([Liu et al., *JCEM* 2021](https://academic.oup.com/jcem/article/106/2/351/6000434)). A second brain tumor (suspected pineoblastoma) was among the causes of death in the cohort (Section 11).
- **Lifestyle factors:** **Not applicable.** The disease presents at a median of 11 months; no diet, smoking, alcohol, or activity exposure is biologically plausible or reported.
- **Infectious agents:** **None.** No bacterial, viral, fungal, or parasitic trigger is described; searches of infectious-disease resources returned nothing relevant.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **A heterozygous germline loss-of-function *DICER1* variant** (nonsense, frameshift, splice-site, or large deletion), inherited in an autosomal dominant manner or arising de novo/mosaic, **leads to** constitutional DICER1 haploinsufficiency in every cell of the embryo ([GeneReviews NBK196157](https://www.ncbi.nlm.nih.gov/sites/books/NBK196157/); [*Int J Cancer* 2017](https://onlinelibrary.wiley.com/doi/abs/10.1002/ijc.30907)).
2. **A somatic missense mutation in one of five RNase IIIb hotspot codons (E1705, D1709, G1809, D1810, E1813) in the remaining allele**, acquired in a Rathke-pouch–derived adenohypophyseal progenitor in fetal/early postnatal life, **results in** a catalytically crippled metal-binding cleft in RNase IIIb while RNase IIIa remains active. *Demonstrated* in PitB tumors: 8 of 10 tested tumors carried confirmed somatic second-hit *DICER1* mutations ([de Kock et al. 2014](https://link.springer.com/article/10.1007/s00401-014-1285-z)). *Inferred*: the precise progenitor cell of origin and the timing of the second hit.
3. **Loss of RNase IIIb cleavage leads to failure of 5p-arm miRNA maturation**, while 3p-arm processing is preserved — "RNase IIIb hotspot mutations specifically block the maturation of 5p miRNAs, while the processing of 3p miRNAs remains unaffected" (retrieved). In PitB this was shown directly: "*DICER1* RNase IIIb hotspot mutations in pituitary blastomas induced **improper processing of miRNA precursors, resulting in aberrant 5p-derived miRNA products and a skewed distribution of miRNAs favoring mature 3p over 5p miRNAs**" ([*Acta Neuropathol* 2021;141:929–944](https://link.springer.com/article/10.1007/s00401-021-02283-6)). Independently corroborated in PitB tissue by microRNA array: "**decreased mature microRNA expression and preferential down-regulation of 5p/3p species in tumor compared to control pituitary tissue**" ([Liu et al., *Acta Neuropathol* 2022, PMID 35129635](https://pubmed.ncbi.nlm.nih.gov/35129635/)).
4. **Branch 4a — loss of tumor-suppressor 5p miRNAs.** Depletion of 5p species "including tumor suppressors such as the **let-7 family**" (all 5′-derived) **leads to** derepression of let-7 target oncogenes and increased proliferation: "Cells expressing DICER1 hotspot mutation grew faster than those with wildtype DICER1, which was **at least partially due to loss of let-7 expression**" (retrieved; [*Nat Rev Cancer* 2014](https://www.nature.com/articles/nrc3802); [bioRxiv 2025 Dicer1 hotspot loss+gain](https://www.biorxiv.org/content/10.1101/2025.10.15.682667.full.pdf)).
   **Branch 4b — gain of 3p passenger miRNA function.** An **Argonaute strand-switch** converts retained 3p species into dominant guide strands, imposing a novel repressive program — a true gain of function ([*Nat Struct Mol Biol* 2025](https://www.nature.com/articles/s41594-025-01671-w)). This branch is demonstrated in cell systems; its specific contribution *within PitB* is **inferred**.
5. **The resulting miRNA imbalance leads to dysregulation of developmental signaling programs.** In PitB specifically: "**PRAME** [was] the most significantly upregulated gene (**500-fold increase**)," a member of the retinoic-acid-receptor signaling pathway, "and in pituitary blastomas, the **RAR, WNT and NOTCH pathways are dysregulated**"; Cancer Hallmarks analysis showed "the **PI3K pathway is activated** in the tumors" ([*Acta Neuropathol* 2021;141:929–944](https://link.springer.com/article/10.1007/s00401-021-02283-6)). The *DICER1*-hotspot→**MAPK activation** axis is established in another DICER1 tumor type (pediatric thyroid cancer: [*PMC9990750*, PMID 36896180](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9990750/)) and is **inferred, not demonstrated,** for PitB.
6. **Dysregulated RAR/WNT/NOTCH plus PI3K activation in a Rathke-pouch progenitor results in arrested adenohypophyseal differentiation coupled to unchecked proliferation** — the "arrested pituitary development and unchecked proliferation" formulation of the entity ([*Pituitary* 2012, PMID 21805093](https://pubmed.ncbi.nlm.nih.gov/21805093/)). Ultrastructurally the tumor is frozen at the **10–12 week embryonic pituitary stage** ([*Acta Neuropathol* 2008](https://link.springer.com/article/10.1007/s00401-008-0388-9)). Mechanistic plausibility is supported by mouse loss of Dicer in pituitary progenitors producing developmental failure (Section 15).
7. **The arrested tumor retains three coexisting lineages — primitive blastemal cells, Rathke-type epithelium in rosettes/glands, and large secretory cells (plus folliculostellate cells)** ([*Pituitary* 2012](https://pubmed.ncbi.nlm.nih.gov/21805093/)).
8. **The secretory component, of corticotroph lineage, leads to ACTH hypersecretion.** IHC "confirms ACTH expression and nuclear expression of **TBX19 (TPIT)**, supporting a corticotroph lineage" (retrieved from [*J Neuropathol Exp Neurol* 2025;84(5):436](https://academic.oup.com/jnen/article/84/5/436/7917506)). ACTH excess **results in** adrenal cortisol overproduction → **infantile Cushing syndrome** (10/17 cases). A minority express GH instead; one case expressed prolactin excess.
9. **In parallel, local tumor growth results in mass-effect manifestations:** cavernous sinus and parasellar invasion → cranial nerve III/IV/VI palsies and ophthalmoplegia (7/17); compression of the optic apparatus → reduced visual acuity (4/17); obstructive/mass effect → raised intracranial pressure (3/17); hypothalamic–stalk–posterior-pituitary involvement → **central diabetes insipidus**. *Inference*: the DI is attributed to stalk/neurohypophyseal involvement; the retrieved case reports document the association but not the lesion-level mechanism.
10. **Downstream, both the hypercortisolism and the surgical/radiotherapeutic destruction of the gland lead to chronic hypopituitarism** (neuroendocrine deficits in 8 of the cohort, up to panhypopituitarism), neurodevelopmental impairment, and visual loss ([Liu et al., *JCEM* 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC7823240/)).

### Checklist coverage within the chain

- **Molecular pathways:** miRNA biogenesis (the primary lesion); **RAR**, **WNT**, **NOTCH** dysregulation; **PI3K** activation; MAPK (inferred by analogy to DICER1 thyroid tumors). Suggested GO/pathway anchors: **GO:0031054** pre-miRNA processing; **GO:0035195** miRNA-mediated post-transcriptional gene silencing; GO:0035196 miRNA processing; GO:0030422 siRNA processing; GO:0031047 gene silencing by RNA ([AmiGO GO:0031054](https://amigo.geneontology.org/amigo/term/GO:0031054); [AmiGO GO:0035195](https://amigo.geneontology.org/amigo/term/GO:0035195)).
- **Cellular processes:** cell-cycle/proliferative dysregulation (faster growth with hotspot DICER1, let-7-dependent); arrested lineage differentiation of pituitary progenitors; retained multilineage differentiation (rosette formation). Apoptosis/autophagy/inflammation contributions: **not characterized in PitB**.
- **Protein dysfunction:** the hotspot residues sit in the **RNase IIIb metal-binding catalytic cleft**; the defect is domain-selective catalytic loss plus altered guide-strand selection by Argonaute, not misfolding or aggregation ([*Nat Struct Mol Biol* 2025](https://www.nature.com/articles/s41594-025-01671-w)).
- **Metabolic changes:** no PitB metabolomic/lipidomic data retrieved. The clinically dominant metabolic derangement is **secondary** — glucocorticoid excess (central obesity, hypertension, hyperglycemia; and in infants raised 17-OHP/testosterone, 17-KS/17-OHCS).
- **Immune involvement:** no autoimmune/immunodeficiency/inflammatory mechanism retrieved. **PRAME**, the top-upregulated gene, is a cancer-testis antigen of potential immunotherapeutic interest, but no immunologic work in PitB was retrieved.
- **Tissue damage mechanisms:** direct **local invasion and destruction** ("a locally destructive tumor"), not oxidative stress/ischemia/fibrosis.
- **Biochemical abnormalities:** endocrine — ACTH/cortisol excess, variable AVP deficiency, post-treatment multi-axis deficiency. Enzymopathy/channelopathy: **none**.
- **Molecular profiling available for PitB:** small-RNA-seq, RNA-seq, methylation array, WGS, NanoString miRNA on 3 fresh-frozen PitB vs 3 fetal and 3 postnatal normal pituitaries, with a 21-sample validation series ([*Acta Neuropathol* 2021;141:929–944](https://link.springer.com/article/10.1007/s00401-021-02283-6)). **Proteomics, metabolomics, and lipidomics for PitB: none retrieved** (PRIDE/MetaboLights/LIPID MAPS searches surfaced nothing PitB-specific).
- **Advanced technologies:** **no single-cell or spatial transcriptomic study of PitB was retrieved.** The nearest is single-cell/spatial work on a different DICER1 tumor: "Spatial single cell transcriptomic analysis informs tumor developmental hierarchy of DICER1 syndrome related sarcoma" ([PMID 41912509](https://pubmed.ncbi.nlm.nih.gov/41912509/)). No CRISPR/RNAi functional screen specific to PitB; DepMap contains no PitB model to my retrieval.
- **Cell types involved (Cell Ontology):** corticotroph (ACTH-secreting adenohypophyseal cell), folliculostellate cell, Rathke-pouch epithelial cell, and primitive blastemal progenitor. **I was unable to verify CL identifiers in this session and therefore give labels only.** Supporting biology: corticotrophs "secrete proopiomelanocortin (POMC)-derived hormones such as adrenocorticotrophic hormone (ACTH)"; folliculostellate cells are "non-endocrine… agranular chromophobic cells" that "express vimentin and the nervous tissue-specific S-100 protein… but no secretory pituitary cell markers" ([Folliculostellate cell review, PMC11475256](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11475256/); [Wikipedia/Claudin-9 FS-cell study, PMC8568902](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8568902/)).

---

## 7. Anatomical Structures Affected

### Organ level

- **Primary organ: the anterior pituitary / adenohypophysis**, within the sella turcica. UBERON anchor verified in this session: **UBERON:0006964** *pars distalis of adenohypophysis* — "the distal part of adenohypophysis: the part that makes up the main body of the gland… the region of the adenohypophysis which produces the follicle-stimulating hormone, luteinizing hormone, prolactin, thyrotropin, and adrenocorticotropin" ([EBI OLS, UBERON_0006964](https://www.ebi.ac.uk/ols/ontologies/uberon/terms?iri=http://purl.obolibrary.org/obo/UBERON_0006964); [BioPortal](https://bioportal.bioontology.org/ontologies/UBERON?p=classes&conceptid=UBERON:0006964)). Note: the pars distalis constitutes ~80% of the anterior lobe.
- **Local/contiguous extension:** suprasellar cistern, cavernous sinus, optic apparatus. "Pituitary blastoma presents as an **intra- and suprasellar mass with inhomogeneous enhancement, potentially invading the cavernous sinus and adjacent structures**" (retrieved imaging synthesis; [Primary tumors of the pituitary gland: radiologic-pathologic correlation, *RadioGraphics* 2021](https://pubs.rsna.org/doi/10.1148/rg.2021200203)).
- **Secondary organ involvement:** **adrenal cortex** (ACTH-driven hypercortisolism and its systemic sequelae), **optic nerves/chiasm**, **cranial nerves III/IV/VI**, **hypothalamus/neurohypophysis** (diabetes insipidus), and the whole-body consequences of glucocorticoid excess (metabolic, skeletal, immune).
- **Body systems:** **endocrine** (primary), **nervous/CNS**, **visual**, with secondary cardiovascular/metabolic effects of hypercortisolism.

### Tissue and cell level

- **Epithelial:** primitive **Rathke-type epithelium** forming rosettes, glands, and primitive multilayered rosette-like structures; CAM 5.2 positivity in tubule-forming cells "suggests an immature epithelial origin, likely from Rathke's pouch" (retrieved).
- **Neuroendocrine/secretory:** large secretory cells of **corticotroph** (ACTH⁺, TPIT/TBX19⁺) and, less often, **somatotroph** (GH⁺) type.
- **Sustentacular:** **folliculostellate cells**.
- **Primitive/blastemal:** "small, polyhedral, primitive-appearing cells (blastema) with scant cytoplasm, abundant glycogen and few organelles" ([*Pituitary* 2012](https://pubmed.ncbi.nlm.nih.gov/21805093/)).
- Proliferative index: "diffuse strong staining for **synaptophysin** with a very high **MIB-1 index**" ([retrieved case description, *Indian J Pathol Microbiol* 2022, PMID 35435381](https://pubmed.ncbi.nlm.nih.gov/35435381/)).
- An unusual immunophenotype documented recently: "Within the primitive multilayered rosette-like structures, there is clustered positive staining for both **Pit-1 and SALL4**, and these primitive areas… are negative for prolactin, growth hormone, and TSH" ([*J Neuropathol Exp Neurol* 2025;84(5):436](https://academic.oup.com/jnen/article/84/5/436/7917506)).

### Subcellular level

The molecular lesion acts in the **cytoplasmic miRNA-processing machinery** (Dicer–TARBP2/PRKRA complex and the RNA-induced silencing complex), with downstream effects on nuclear transcriptional programs (RAR/WNT/NOTCH) — per DICER1 functional annotation ([Human Protein Atlas](https://www.proteinatlas.org/ENSG00000100697-DICER1/summary/gene)). **I did not retrieve PitB-specific GO Cellular Component annotations** and therefore do not assert specific GO CC identifiers beyond DICER1's own process annotations listed in Section 6.

### Localization and lateralization

**Midline, central, non-lateralized** — a sellar/suprasellar mass. Parasellar invasion may be asymmetric (unilateral cavernous sinus invasion with unilateral cranial nerve palsy), but the tumor itself is not a lateralized entity. No HPO/imaging-database laterality annotation for PitB was retrieved.

---

## 8. Temporal Development

### Onset

- **Age:** median **11 months**, range **2–24 months** in the 17-patient cohort ([Liu et al., *JCEM* 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC7823240/)); classically described as occurring "exclusively in children under 2 years of age" ([PMID 35129635](https://pubmed.ncbi.nlm.nih.gov/35129635/)). Infants presenting as early as 7 months and a 13-month-old Korean female with Cushing disease plus diabetes insipidus are documented individual cases.
- **Exceptions now recognized:** a **young adult** case with prior Wilms tumor and multinodular goiter — "the first case of a pituitary blastoma occurring in a young adult" ([Chong, Han, Albrecht, *Acta Neuropathol* 2021, doi 10.1007/s00401-021-02378-0](https://link.springer.com/article/10.1007/s00401-021-02378-0)); a **19-year-old woman** ([*World Neurosurg* case report](https://www.sciencedirect.com/science/article/abs/pii/S1878875020308032)); and a 2025 young-adult case with hyperprolactinemia ([PMID 40451220](https://pubmed.ncbi.nlm.nih.gov/40451220/)).
- **Onset pattern:** **subacute to acute and rapidly progressive** — infants present with evolving hypercortisolism, new cranial neuropathy, or raised ICP over weeks to months. Because the germline hit is constitutional and the tumor arises from fetal/early-postnatal pituitary, the biology is **developmental/congenital in origin with postnatal clinical onset**.

### Progression

- **Staging:** **no stage or grade system exists for PitB.** Unlike pleuropulmonary blastoma (types Ir/I/II/III), PitB has no accepted morphologic progression scheme; it is coded as malignant by behavior (ICD-O /3). AJCC does not stage it.
- **Progression rate:** rapid, with local destruction. The summary judgment of the only outcomes cohort: "**Pituitary blastoma is a locally destructive tumor associated with high mortality**" ([Liu et al., *JCEM* 2021](https://academic.oup.com/jcem/article/106/2/351/6000434)).
- **Course pattern:** **progressive** with treatment-dependent plateau; recurrence/persistence after subtotal resection is documented (one patient received gamma-knife radiotherapy at 17 months for persistent residual disease; another received conformal radiation at 24 months for progression).
- **Duration:** the tumor phase is months-to-years; **survivorship is lifelong and chronic**, dominated by endocrine, visual, and neurocognitive sequelae plus lifelong *DICER1*-syndrome cancer risk.

### Patterns

- **Remission:** **treatment-induced only**; no spontaneous regression reported. Documented responses include "no evidence of residual disease or recurrence by imaging at 1.2 years after surgery" following induction chemotherapy and focal radiation, and "significant therapeutic response to chemoradiation" in the 2025 JNEN case.
- **Critical periods:** (i) **birth to ~24 months** — the window of tumor emergence and the only window in which PitB is expected; (ii) **the moment a *DICER1* carrier develops signs of cortisol excess or intracranial pathology** — the guideline-defined intervention window: "**Urgent brain MRI is recommended for persons with a *DICER1* pathogenic variant with signs of intracranial pathology or cortisol excess** for the detection of pineoblastoma or pituitary blastoma" (retrieved from the *DICER1* surveillance guidance; [Schultz et al. 2018, PMID 29343557](https://www.researchgate.net/publication/322564582_DICER1_and_Associated_Conditions_Identification_of_At-risk_Individuals_and_Recommended_Surveillance_Strategies); [2024 update, *Clin Cancer Res* 2024;30(24):5681, PMID 39400264](https://aacrjournals.org/clincancerres/article/30/24/5681/750430/DICER1-Related-Tumor-Predisposition-Identification)).

---

## 9. Inheritance and Population

### Epidemiology

- **Case count, not rates.** PitB is among the rarest named human tumors. Retrieved counts: "fewer than 20 published cases" (WHO-classification commentary), "only 21 cases reported" (MalaCards/retrieved review), 17 cases in the pooled clinical cohort, and 17 in the parallel molecular cohort. **No incidence or prevalence per 100,000 has been published**, and none appears in Orphanet, SEER, CBTRUS, or GBD to my retrieval. I therefore decline to state a rate; the honest statement is **<1 case per 10 million children, on the order of a handful of cases worldwide per decade**, derived from total case counts rather than a registry denominator.
- **Sex ratio:** 10 female : 7 boys ≈ **1.4:1 F:M** in the largest cohort — not statistically meaningful at n=17 ([Liu et al., *JCEM* 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC7823240/)).
- **Age distribution:** sharply concentrated in infancy (median 11 months; range 2–24 months), with rare adolescent/young-adult outliers.
- **Geography:** cases reported from multiple continents (the *DICER1* Registry spans **38 countries**); no endemic clustering, founder population, or regional variant distribution has been described for PitB ([NCT03382158](https://clinicaltrials.gov/study/NCT03382158)).

### Genetic etiology parameters

- **Inheritance:** **autosomal dominant with reduced, age-related penetrance** — "DICER1-related tumor predisposition is inherited in an **autosomal dominant manner with reduced, age-related penetrance**" ([GeneReviews NBK196157](https://www.ncbi.nlm.nih.gov/sites/books/NBK196157/)). Variants "are typically inherited in an autosomal dominant pattern but **may arise de novo in the germline or in a somatic mosaic distribution**" ([de Kock, Wu & Foulkes, *Hum Mutat* 2019;40:1939–1953](https://onlinelibrary.wiley.com/doi/10.1002/humu.23877)).
- **Penetrance (any DICER1 neoplasm, not PitB specifically):** "By age 10 years, **5.3% (95% CI, 0.6%–9.7%)** of nonproband *DICER1* carriers had developed a neoplasm (females 4.0%; males 6.6%)"; by 50 years, **19.3%** (females 26.5%, males 10.2%) ([Khan et al., *J Clin Oncol* 2019, PMID 30715996](https://pubmed.ncbi.nlm.nih.gov/30715996/)). **Penetrance of PitB specifically is extremely low** — far under 1% of carriers — because PitB accounts for a tiny fraction of DICER1 tumors; a precise carrier-level PitB penetrance estimate was **not retrieved**.
- **Expressivity:** **highly variable** — the DICER1 phenotype spans >25–30 distinct lesions; a single family can include PPB, cystic nephroma, multinodular goiter, and (rarely) PitB. The young-adult PitB patient also had Wilms tumor and multinodular goiter ([*Acta Neuropathol* 2021](https://link.springer.com/article/10.1007/s00401-021-02378-0)).
- **Genetic anticipation:** **not described**; *DICER1* is not a repeat-expansion locus.
- **Germline/somatic mosaicism:** well documented and clinically important. Mosaic RNase IIIb hotspot variants cause **GLOW syndrome** (**G**lobal developmental delay, **L**ung cysts, **O**vergrowth, **W**ilms tumor); "mosaic *DICER1* mutations are an important cause of DICER1 syndrome in patients with severe phenotypes and often appear to be accompanied by second somatic truncating mutations"; high-sensitivity sequencing has revealed multi-organ somatic mosaicism causing DICER1 syndrome ([retrieved: GLOW description](https://www.researchgate.net/publication/261187740_Expanding_the_phenotype_of_mutations_in_DICER1_mosaic_missense_mutations_in_the_RNase_IIIb_domain_of_DICER1_cause_GLOW_syndrome); [high-sensitivity sequencing study](https://www.semanticscholar.org/paper/High-sensitivity-sequencing-reveals-multi-organ-Kock-Wang/51475c6993ae32172bf6f7d31705cbb04a8f068f)).
- **Founder effects:** none reported for *DICER1*.
- **Consanguinity:** **not relevant** — the mechanism is dominant germline + somatic, not biallelic recessive inheritance.
- **Carrier frequency:** **1:10,600** (stringent LoF-only estimate) to **1:870–1:2,529** (broader in-silico estimate) in ExAC-nonTCGA ([Kim J et al., *Int J Cancer* 2017](https://onlinelibrary.wiley.com/doi/abs/10.1002/ijc.30907)).

---

## 10. Diagnostics

### Clinical tests

**Laboratory**
- **Hypercortisolism workup:** plasma ACTH, serum cortisol, 24-h urinary free cortisol, late-night salivary cortisol, dexamethasone suppression — the pathway for ACTH-dependent Cushing syndrome in children ([*Endotext* NBK602210](https://www.ncbi.nlm.nih.gov/sites/books/NBK602210/)). In infants, concurrent elevations of 17-OHP, testosterone, urinary 17-KS and 17-OHCS have been documented.
- **Anterior pituitary panel:** GH/IGF-1, prolactin (elevated prolactin has now been reported, [PMID 40451220](https://pubmed.ncbi.nlm.nih.gov/40451220/)), TSH/free T4, gonadotropins — typically "normal or markedly reduced" apart from the ACTH axis.
- **Posterior pituitary:** paired serum/urine osmolality and sodium, water-deprivation/desmopressin testing for central diabetes insipidus (**HP:0000873**).
- LOINC codes for these analytes exist but **I did not retrieve specific LOINC identifiers** and do not assert them.

**Biomarkers.** There is **no validated circulating or liquid-biopsy biomarker** for PitB. The disease-defining molecular marker is the *DICER1* genotype itself (germline LoF + somatic RNase IIIb hotspot). **PRAME** is a candidate tissue marker by virtue of its ~500-fold overexpression ([*Acta Neuropathol* 2021](https://link.springer.com/article/10.1007/s00401-021-02283-6)); **PEG10** has been proposed as a biomarker for *malignant* DICER1-related tumors generally ([Wu et al., *J Pathol* 2025](https://pathsocjournals.onlinelibrary.wiley.com/doi/10.1002/path.70141)) — neither is validated for PitB diagnosis. No FDA-qualified biomarker exists.

**Imaging.** Gadolinium-enhanced **MRI of the sella** is the primary modality. Retrieved descriptors: an "intra- and suprasellar mass with inhomogeneous enhancement, potentially invading the cavernous sinus and adjacent structures"; a "focally cystic, contrast-enhancing, sellar and suprasellar mass" in a 13-month-old; and the practical rule that "the presence of a **sellar/suprasellar mass in small children should raise the suspicion of a pituitary blastoma or an AT/RT**." Importantly, "pituitary blastoma is rare and has **no specific imaging finding**," so histopathology is required ([*RadioGraphics* 2021](https://pubs.rsna.org/doi/10.1148/rg.2021200203); [sellar-region imaging review, PMC10033642](https://pmc.ncbi.nlm.nih.gov/articles/PMC10033642/)). RadLex/DICOM-specific descriptors were not retrieved.

**Functional tests / electrophysiology.** Not diagnostic. Relevant ancillary assessments are **formal ophthalmologic examination with visual acuity and fields** (for chiasmal compression) and developmental assessment; no EEG/EMG/ECG role.

**Biopsy / histopathology — the diagnostic gold standard.** Required features: a cellular tumor with **three cell populations** — primitive blastemal cells, Rathke-type epithelium in rosettes/glands, and large secretory cells, plus folliculostellate cells. Retrieved description: "a cellular tumor… with primitive-looking round cells with scanty cytoplasm with few well-defined gland or rosette-like structures, with diffuse strong staining for **synaptophysin** with a very high **MIB-1 index**."
**Immunohistochemistry panel:** synaptophysin (diffuse), **ACTH** (and TPIT/TBX19 nuclear positivity → corticotroph lineage), GH (minority), **CAM 5.2** (tubule-forming epithelium), **PIT-1 + SALL4** co-positivity in primitive rosette areas, S100/vimentin (folliculostellate), Ki-67/MIB-1 (high). The 2022 WHO classification endorses "the routine use of immunohistochemistry for pituitary transcription factors (**PIT1, TPIT, SF1, GATA3, and ERα**)" for pituitary tumors generally ([*Endocr Pathol* 2022](https://link.springer.com/article/10.1007/s12022-022-09703-7); [*JNEN* 2025;84(5):436](https://academic.oup.com/jnen/article/84/5/436/7917506)). **Electron microscopy** was historically contributory (three cell populations; glycogen-rich blastemal cells).

### Genetic testing

- **Recommended approach:** a histologic diagnosis of pituitary blastoma is itself an indication for testing — "**the diagnosis of a pituitary blastoma is an indication for germline *DICER1* testing**" (retrieved), and PitB "is listed among CNS indications for germline *DICER1* testing" in the 2024 guidance ([*Clin Cancer Res* 2024;30(24):5681, PMID 39400264](https://pmc.ncbi.nlm.nih.gov/articles/PMC11649450)). Practically: **paired tumor + germline (blood) *DICER1* sequencing**, since the diagnostic signature is germline LoF *plus* tumor hotspot missense.
- **Single-gene testing / targeted hotspot sequencing:** high yield and the most direct route (tumor RNase IIIb hotspot codons E1705/D1709/G1809/D1810/E1813 plus full germline *DICER1*).
- **Gene panels:** *DICER1* is included in pediatric cancer-predisposition and hereditary-tumor panels; it is a curated gene on the Genomics England PanelApp ([PanelApp DICER1](https://panelapp.genomicsengland.co.uk/panels/entities/DICER1)) and has ClinGen curation ([ClinGen DICER1](https://search.clinicalgenome.org/kb/genes/HGNC:17098)).
- **WES/WGS:** useful when panels are negative, for structural/deep-intronic variants, and to document the quiet tumor genome. Note two retrieval-supported pitfalls: **intronic and synonymous variants** can be pathogenic through splicing effects and may be missed or misclassified ([*JCO PO* 2023](https://ascopubs.org/doi/10.1200/PO.23.00189); [PMC10635218](https://pmc.ncbi.nlm.nih.gov/articles/PMC10635218/); [reclassification of two germline splicing variants, PMID 37248399](https://pubmed.ncbi.nlm.nih.gov/37248399/)); and **mosaicism requires high-sensitivity/deep sequencing**, not standard Sanger.
- **CMA / karyotype / FISH:** low yield — PitB has a quiet genome with no recurrent cytogenetic lesion. CMA retains a role only for detecting large *DICER1* deletions (≈2% of germline variants in one series).
- **mtDNA testing and repeat-expansion testing:** **not applicable.**
- **Methylation classification** is an emerging adjunct: PitB forms a distinct methylation class separable from pituitary adenomas and ~3,000 other CNS tumors ([PMID 33644822](https://pubmed.ncbi.nlm.nih.gov/33644822/)).

### Omics-based diagnostics

- **RNA-seq / small-RNA-seq:** can demonstrate the diagnostic miRNA signature (5p depletion, 3p/5p skew). A microRNA array in an atypical case "revealed decreased mature microRNA expression and preferential down-regulation of 5p/3p species in tumor compared to control pituitary tissue," which supported reclassification of a tumor originally called "pituitary ependymoblastoma" then "pituitary CNS-PNET" ([PMID 35129635](https://pubmed.ncbi.nlm.nih.gov/35129635/)). The authors' conclusion is directly actionable: "it might be prudent to consider **sequencing for *DICER1* alteration in pediatric pituitary tumors** to facilitate diagnosis."
- **Epigenomics:** methylation array classification (above).
- **Proteomics, metabolomics, liquid biopsy:** **no PitB-specific application retrieved.**

### Clinical criteria and differential diagnosis

There are **no formal consensus diagnostic criteria** (no DSM/ICD algorithm); diagnosis rests on WHO-classification histopathology plus *DICER1* genotyping. The differential for a sellar mass in an infant/young child, per retrieved sources:

| Entity | Distinguishing features |
|---|---|
| **Corticotroph PitNET/adenoma** (incl. infantile ACTH-secreting adenoma) | Monomorphic neuroendocrine cells, no Rathke epithelium/blastemal component, no *DICER1* hotspot; note infantile corticotroph adenomas are themselves rare ([PMID 6278457](https://pubmed.ncbi.nlm.nih.gov/6278457/)) |
| **Atypical teratoid/rhabdoid tumor (AT/RT)** | Rhabdoid cells, **biallelic SMARCB1/INI-1 inactivation with loss of nuclear INI-1 by IHC**; the key mimic in this age group ([PMC10938043](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10938043/)) |
| **Craniopharyngioma** | Adamantinomatous epithelium, wet keratin, CTNNB1; or papillary/BRAF V600E |
| **Germ cell tumor**, **Langerhans cell histiocytosis**, **low-grade glioma**, pituitary carcinoma, hypothalamic/pituitary hamartoma | Each explicitly listed in the 2024 *DICER1* guidance as considerations for "a pituitary mass in a young child" ([PMC11649450](https://pmc.ncbi.nlm.nih.gov/articles/PMC11649450)) |
| **Primary intracranial sarcoma, *DICER1*-mutant** (sellar) | Also *DICER1*-driven but a different entity — "DICER1 mutations are definite features, commonly along with **TP53 mutations and ATRX inactivation**"; illustrated by a 16-year-old with a sellar mass finally diagnosed as "corticotroph tumor/adenoma associated with primary intracranial sarcoma, DICER1-mutant," in whom "pituitary blastoma should be included as a differential diagnosis" ([Xiao et al., *Brain Pathol* 2025, PMID 40040389](https://pubmed.ncbi.nlm.nih.gov/40040389/)) |
| **Embryonal tumor with multilayered rosettes (non-C19MC-altered) in DICER1 syndrome** | Reported; morphologic overlap with primitive rosette-forming areas ([PMC11447652](https://pmc.ncbi.nlm.nih.gov/articles/PMC11447652)) |

### Screening of asymptomatic individuals

No newborn or population screening exists or is recommended for PitB. Screening is **carrier-directed**: cascade *DICER1* testing in first-degree relatives, with the symptom-triggered urgent brain MRI rule (Section 13). Routine surveillance brain MRI is explicitly contested: "**The role of surveillance brain MRI is controversial. The authors suggest urgent brain MRI if there are symptoms of concern**" (retrieved from the *DICER1* surveillance guidance).

---

## 11. Outcome / Prognosis

### Survival and mortality

- **The only pooled outcome dataset:** of **17 patients**, "**Nine of 17 patients survived with median survival of 6.7 years and median age at last follow-up of 10.8 years**" — i.e. **8 deaths (~47%)** ([Liu et al., *JCEM* 2021;106(2):351](https://pmc.ncbi.nlm.nih.gov/articles/PMC7823240/); [ESPE Yearbook summary](https://www.espeyearbook.org/ey/0018/ey0018.1-15)). At a median follow-up of 6.7 years, 9 patients were alive.
- **Cause of death is as often treatment/complication-related as tumor-related:** among 17 reported cases with outcomes, "8 patients died, **1 with disease progression, and 7 with early or late complications** (including sepsis, second brain tumor/suspected pineoblastoma, catheter complications, or aneurysm)" (retrieved).
- **Headline prognostic statement:** "**Pituitary blastoma is a locally destructive tumor associated with high mortality.**"
- **5-year and 10-year actuarial survival rates, life expectancy estimates, and population mortality rates are NOT available** for PitB. No SEER/CBTRUS/GBD figures exist for this entity; I decline to compute pseudo-rates from n=17.

### Morbidity and function

Chronic complications in the cohort: "**neuroendocrine (n=8), visual (n=4), and neurodevelopmental (n=3) deficits**" ([Liu et al., *JCEM* 2021](https://academic.oup.com/jcem/article/106/2/351/6000434)). Survivor status spans "hormonal sequelae ranging from none to **panhypopituitarism**" and "neurocognitive function ranging from fully functional to impaired," with some survivors visually impaired. **No ICF-coded disability data, EQ-5D/SF-36/PROMIS scores, or disease-specific QoL instruments exist for PitB** (searches returned PPB-specific HRQoL work only).

### Disease course and recovery potential

- **Complications:** persistent/residual disease after subtotal resection; progression requiring salvage radiation; infectious complications (sepsis); device/catheter complications; vascular complications (aneurysm); **second primary CNS tumor** (suspected pineoblastoma) — the last being especially significant in a radiation-exposed *DICER1* carrier.
- **Recovery potential:** durable local control is achievable — one patient had "no evidence of residual disease or recurrence by imaging at 1.2 years after surgery" after chemotherapy plus proton therapy; another was "good" in overall well-being at 4-year follow-up after chemo-radiotherapy. Endocrine and visual deficits, once established, are generally **not recoverable** and require lifelong replacement/support.

### Prediction

- **Prognostic factors (observational, low-evidence given n):** extent of resection (gross-total vs subtotal), severity and control of perioperative hypercortisolism, tumor invasion of cavernous sinus/parasellar structures, age and radiation tolerance, and the capacity to deliver multimodal therapy safely in an infant. These are inferred from the case-level narratives rather than from a fitted prognostic model — **no validated prognostic model or calculator exists**.
- **Prognostic biomarkers:** **none validated**. PRAME and PEG10 are research-stage candidates (above). Germline *DICER1* status is prognostic for *subsequent* tumor risk (lifelong DICER1-spectrum surveillance) rather than for PitB outcome itself.

---

## 12. Treatment

> There is **no clinical practice guideline, NCCN pathway, or prospective trial specific to pituitary blastoma**. Everything below is case-series/registry-derived or extrapolated from adjacent fields, and I mark the extrapolations. NCIT identifiers: **I could not verify NCIT codes in this session**, so interventions are given as labels for later NCIT mapping.

### Surgical and interventional

- **Surgery is the mainstay.** "**Surgical resection is the mainstay of management for pituitary blastoma**" ([GeneReviews NBK196157](https://www.ncbi.nlm.nih.gov/sites/books/NBK196157/)). In practice resections have often been **subtotal** ("the subtotally resected tumors were subject to histochemical, immunohistochemical and… ultrastructural study," [*Pituitary* 2012](https://pubmed.ncbi.nlm.nih.gov/21805093/)); "surgical decompression was performed" in the 2025 young-adult case. Candidate NCIT concepts: *pituitary tumor resection / transsphenoidal surgery / craniotomy*.
- **Bilateral adrenalectomy** is a salvage option for life-threatening hypercortisolism. From general Cushing literature (**extrapolated, not PitB-specific**): "Bilateral adrenalectomy may be indicated in cases of life-threatening severe hypercortisolism, but UFC should be reduced before surgery to reduce the perioperative morbimortality"; it "has nearly a 100% success rate and results in immediate control of steroid excess" ([*Gland Surgery* review](https://gs.amegroups.org/article/view/34956/html); [*Cushing's disease: adrenal steroidogenesis inhibitors*, PMC9587932](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9587932/)).

### Pharmacotherapy

- **Cytotoxic chemotherapy.** In the pooled cohort, "**Five patients received chemotherapy after surgery**." A documented regimen: "2 cycles of induction chemotherapy (**cyclophosphamide, carboplatin, etoposide**) followed by focal radiation therapy (**54 CGE proton therapy**)," with imaging complete response at 1.2 years ([*JNEN* 2025;84(5):436](https://academic.oup.com/jnen/article/84/5/436/7917506); [Liu et al., *JCEM* 2021](https://academic.oup.com/jcem/article/106/2/351/6000434)). Candidate NCIT/CHEBI anchors: cyclophosphamide, carboplatin, etoposide (CHEBI identifiers not retrieved in this session).
- **Medical control of hypercortisolism (adrenal steroidogenesis inhibitors)** — **extrapolated from Cushing syndrome management, not PitB-specific evidence**: "Adrenal steroidogenesis inhibitors, such as **metyrapone and ketoconazole**, are well tolerated and can be highly effective at reducing cortisol levels, either alone or in combination." Pediatric metyrapone dosing cited as "15 mg/kg every 4 h for 6 doses, alternatively 300 mg/m² every 4 h," with adverse effects "hirsutism, dizziness, arthralgia, fatigue, hypokalaemia and nausea"; rectal metyrapone has been used in an infant (for McCune-Albright-related hypercortisolism) ([PMC9587932](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9587932/); [ESE Clinical Update on Cushing's Syndrome 2021](https://www.ese-hormones.org/media/z1el5vx4/ese-cu-cushings-webinar-report_v13-web.pdf)). Perioperative note: "for metyrapone, 48 h discontinuation should be sufficient" before surgery.
- **Hormone replacement:** glucocorticoid, levothyroxine, GH, and **desmopressin (DDAVP)** for central DI, as dictated by post-treatment deficits — the implied standard of care given that 8/17 had neuroendocrine deficits. (Inferred standard endocrine practice; not separately cited for PitB.)
- **Pharmacogenomics:** **no PitB- or *DICER1*-specific PGx guidance** was retrieved from PharmGKB/CPIC/FDA PGx tables. Not applicable at present.

### Radiotherapy

Used as focal/adjuvant therapy: "two patients received focal radiation: **Gamma-knife radiotherapy 17 months after diagnosis for persistent residual disease, and conformal radiation 24 months after the diagnosis of disease progression**"; proton therapy (54 CGE) in another. The explicit caution: "**Radiation therapy for pituitary blastoma must be considered with special caution**" — reflecting infant neurotoxicity plus second-tumor risk in a *DICER1* carrier (one cohort death involved a second brain tumor/suspected pineoblastoma).

### Advanced therapeutics

- **Gene therapy, gene editing, cell therapy/CAR-T, RNA-based therapies (ASO/siRNA/mRNA):** **none exist or are in trial for PitB.** No ClinicalTrials.gov/FDA entry was retrieved.
- **Targeted therapy:** none approved. Mechanistically motivated but **untested** candidates arising from the PitB molecular profile are **PI3K-pathway inhibition** (PI3K hallmark activation) and **retinoid/RAR-axis or PRAME-directed approaches** (PRAME 500-fold up; RAR/WNT/NOTCH dysregulated) ([*Acta Neuropathol* 2021;141:929–944](https://link.springer.com/article/10.1007/s00401-021-02283-6)). I emphasize these are **hypotheses generated by the profiling paper, not therapies**.
- **Immunotherapy:** none reported. PRAME is a cancer-testis antigen and a theoretical immunotherapy target; **no PitB immunotherapy data retrieved**.

### Supportive, rehabilitative, and strategic

- **Supportive care:** perioperative glucocorticoid/fluid-electrolyte management (DI/SIADH), infection prophylaxis and vigilance (sepsis was a cause of death), nutrition, and ophthalmologic support.
- **Rehabilitation:** developmental/neurocognitive early-intervention, vision rehabilitation, and physical/occupational/speech therapy as dictated by deficits (3 survivors with neurodevelopmental deficits, 4 with visual deficits). Specific rehabilitation protocols for PitB: **none published**.
- **Treatment algorithm (synthesized, low-evidence):** (1) stabilize hypercortisolism and endocrine/metabolic status → (2) maximal safe resection → (3) tumor + germline *DICER1* testing and histologic confirmation → (4) adjuvant chemotherapy for residual/incompletely resected disease → (5) focal radiotherapy reserved for persistent or progressive disease, with explicit caution → (6) lifelong endocrine replacement, neurodevelopmental and visual follow-up → (7) enrollment in the *DICER1* Registry and initiation of syndrome-wide surveillance plus family cascade testing.
- **Combination therapy:** the documented effective combination is **surgery + multi-agent chemotherapy ± focal/proton radiation** ("significant therapeutic response to chemoradiation").
- **Personalized medicine:** at present, "personalization" in PitB means **genotype-driven diagnosis and lifelong syndrome surveillance**, not genotype-driven drug selection.
- **Experimental/registry studies with identifiers:** [**NCT03382158** International PPB/DICER1 Registry](https://clinicaltrials.gov/study/NCT03382158) (PitB is an explicit eligibility condition; target 3,400 participants; estimated completion 6 Dec 2035); [**NCT00565903** Elucidating the Genetic Basis of the PPB Familial Cancer Syndrome](https://clinicaltrials.gov/study/NCT00565903); [**NCT01247597** DICER1-related PPB Cancer Predisposition Syndrome: A Natural History Study](https://clinicaltrials.gov/study/NCT01247597); [**NCT01970696** International Ovarian & Testicular Stromal Tumor Registry](https://clinicaltrials.gov/study/NCT01970696). **No interventional trial enrolling pituitary blastoma was found.**

### Treatment outcomes and adverse events

Response: individual complete radiologic responses documented (above); 9/17 survival overall. Adverse events, from the cohort's own complication list: **sepsis, catheter complications, aneurysm, second brain tumor**, plus chronic neuroendocrine/visual/neurodevelopmental deficits. **No FAERS/MedWatch signal specific to PitB therapy** exists given the case numbers.

---

## 13. Prevention

### Primary prevention

**None possible.** PitB arises from a constitutional germline variant plus a stochastic somatic hotspot mutation in fetal/infant pituitary. No vaccine, chemoprophylaxis, behavioral intervention, or environmental control applies. The only "primary prevention" available operates at the reproductive level (below).

### Secondary prevention — surveillance and early detection

This is where the actionable prevention lies, and it is guideline-backed:

- **Symptom-triggered urgent imaging:** "**Urgent brain MRI is recommended for persons with a *DICER1* pathogenic variant with signs of intracranial pathology or cortisol excess** for the detection of pineoblastoma or pituitary blastoma" ([Schultz et al. 2018, PMID 29343557](https://www.researchgate.net/publication/322564582_DICER1_and_Associated_Conditions_Identification_of_At-risk_Individuals_and_Recommended_Surveillance_Strategies); carried into the [2024 update, *Clin Cancer Res* 2024;30(24):5681, PMID 39400264](https://pmc.ncbi.nlm.nih.gov/articles/PMC11649450)).
- **Routine surveillance brain MRI is NOT recommended as standard:** "The role of surveillance brain MRI is controversial. The authors suggest urgent brain MRI if there are symptoms of concern."
- **Targeted clinical examination for PitB-relevant signs:** *DICER1* carriers "should be assessed for **headache, emesis, diplopia, decreased upward gaze, altered gait, precocious puberty, and Cushing syndrome**" ([GeneReviews NBK196157](https://www.ncbi.nlm.nih.gov/sites/books/NBK196157/)).
- **The broader DICER1 surveillance program** (which detects the far commoner syndrome tumors): the SIOPE HGWG/CanGene-CanVar harmonized minimum program is "**annual clinical examination from birth to age 20 years, six-monthly chest X-ray and renal ultrasound from birth to age 6 years, and thyroid ultrasound every 3 years from age 8 to age 40 years**" ([Bakhuizen et al., *Fam Cancer* 2021, PMC8484187](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8484187/)). The 2024 Registry update adds low-dose chest CT for occult type I PPB, annual dilated ophthalmologic exam with visual acuity screening from age 3 to at least 10 (for ciliary body medulloepithelioma), and earlier pelvic ultrasound from the time a germline P/LP variant is identified ([PMC11649450](https://pmc.ncbi.nlm.nih.gov/articles/PMC11649450)). Note: an adult risk-management summary is also maintained at [eviQ 3569 DICER1](https://www.eviq.org.au/cancer-genetics/adult/risk-management/3569-dicer1-risk-management-adult).
- **Clinical actionability** of *DICER1* has been formally curated by ClinGen ([Actionability summary AC002](https://actionability.clinicalgenome.org/ac/ui/Adult/ui/stg2SummaryRpt/AC002)).
- **Provider/family education is the stated cornerstone:** "**Provider and individual/family education is the cornerstone of surveillance**" ([PMC11649450](https://pmc.ncbi.nlm.nih.gov/articles/PMC11649450)) — appropriate because PitB is too rare and too fast for scheduled imaging to catch, so the practical lever is a caregiver/clinician who recognizes infantile Cushing features and orders urgent MRI.

### Tertiary prevention

Prevention of complications in affected children: meticulous endocrine replacement and sick-day/stress-dosing education, DI management, infection prevention (sepsis caused deaths), judicious use of radiation to limit second-malignancy and neurocognitive harm, developmental surveillance and early intervention, and lifelong DICER1-spectrum tumor surveillance in survivors.

### Genetic screening and counseling

- **Counseling model:** autosomal dominant with reduced age-related penetrance; "It is appropriate to offer genetic counseling (including discussion of potential risks to offspring and reproductive options) to young adults who are affected or at risk," and parental testing is recommended even for an apparently isolated proband "to evaluate their genetic status, determine their need for surveillance, and inform reproductive counseling" ([GeneReviews NBK196157](https://www.ncbi.nlm.nih.gov/sites/books/NBK196157/)).
- **Cascade testing:** "For individuals identified with a germline *DICER1* P/LP variant, genetic education, counseling, and testing in **first-degree relatives (parents and siblings)** are recommended," with further cascade testing after determining parental vs de novo origin ([PMC11649450](https://pmc.ncbi.nlm.nih.gov/articles/PMC11649450)).
- **Prenatal testing / PGT:** reproductive options are explicitly within the counseling discussion per GeneReviews. **I did not retrieve a DICER1-specific PGT-M guideline or case series** and do not assert one.
- **Risk stratification:** carrier status is the stratifier; mosaic/germline RNase IIIb hotspot genotypes mark a more severe, multi-site phenotype and warrant heightened vigilance.

### Immunization, public health, environmental interventions, prophylaxis

**Not applicable** — no infectious or environmental etiology; no prophylactic medication or procedure exists for PitB.

---

## 14. Other Species / Natural Disease

### Taxonomy and natural disease

- **Dog (*Canis lupus familiaris*)** — **the first and only non-human natural case of pituitary blastoma**, reported in 2025/2026: *Pituitary blastoma in a dog: comparative clinical, imaging, and pathologic features of a newly recognized and rare human entity* ([PMID 42177605; PMC13383401](https://pmc.ncbi.nlm.nih.gov/articles/PMC13383401/)). Retrieved findings: "This is the **first detailed description of pituitary blastoma in dogs**. The canine patient exhibited clinical signs consistent with **ACTH-hypersecretion** related to a pituitary mass." Histopathology mirrored the human entity: "proliferating **Rathke's epithelium with rosette formations, adenohypophyseal neuroendocrine cells expressing ACTH and occasionally GH, and primitive small blastemal cells**." Imaging: "a solid and well-defined mass, **isointense at T1-weighted sequence and weakly hyperintense at T2-weighted sequence**" — notable because "in humans… no detailed description[s] are available for the MRI appearance of the human PitB at different weighted sequences." Genotype: "**DICER1 mutation analysis was not performed due to technical limitations with FFPE tissue**," so canine *DICER1* causation remains **unproven but hypothesized** ("this case raises the possibility of a similar pathogenetic mechanism in dogs").
- **NCBI Taxonomy identifiers were not retrieved in this session** and I do not state them.
- **Breed:** no breed predisposition can be inferred from n=1. **No VBO identifier retrieved.** Of adjacent interest, PPB-like canine lung tumors have been characterized in two young **Labrador Retrievers** ([*Vet Sci* 2025;13(10):1111](https://www.mdpi.com/2306-7381/13/10/1111)), suggesting the broader DICER1-spectrum phenotype may exist in dogs.
- **OMIA:** **no OMIA entry for pituitary blastoma was retrieved.** Given the 2025 publication date, an OMIA record may not yet exist.

### Orthologous genes

- Mouse **Dicer1** — MGI:2177178 ([MGI](https://www.informatics.jax.org/marker/MGI:2177178))
- Rat **Dicer1** — RGD:1319699 ([RGD](https://rgd.mcw.edu/rgdweb/report/gene/main.html?id=1319699))
- Human **DICER1** — NCBI Gene 23405
- Canine ortholog exists but **I did not retrieve its NCBI Gene ID**.

### Comparative biology

- **Comparative pathology:** the canine case "expands the known species range of PitB and highlights important **clinical, morphological and immunohistochemical parallels with the human counterpart**, providing new insights into comparative pituitary tumor pathology" — same three-population histology, same ACTH (± GH) immunophenotype, same ACTH-hypersecretion syndrome. Difference: the canine MRI signal characteristics are better documented than the human ones, and *DICER1* status is unconfirmed in the dog.
- **Evolutionary conservation of mechanism:** Dicer-dependent miRNA biogenesis is deeply conserved; Dicer1 is essential for mammalian development (mouse null lethality at E7.5, Section 15), and pituitary-specific Dicer loss in mouse disrupts adenohypophyseal development — consistent with the human arrested-development model.

### Transmission

**Not applicable** — zero zoonotic potential and no cross-species transmissibility; this is a germline/somatic genetic neoplasm.

### Veterinary relevance

Limited by rarity (single case) but clinically meaningful: PitB should enter the differential for a young dog with ACTH-hypersecretion and a sellar mass, and the case establishes a potential spontaneous large-animal comparative model.

---

## 15. Model Organisms

**The central finding to record: no animal or cellular model of pituitary blastoma itself was retrieved. There is no mouse, rat, zebrafish, organoid, or iPSC model that reproduces PitB.** What exists are *Dicer1* models that illuminate individual mechanistic steps.

### Available models and what each contributes

| Model | Type | Finding | Relevance to PitB |
|---|---|---|---|
| ***Dicer1*-null mouse** (Bernstein et al. 2003, *Nat Genet* 35:215) | Mammalian, constitutive KO | "Disruption of the *Dicer1* gene in mice results in **lethality at embryonic day 7.5** due to a loss of pluripotent stem cells"; *Dicer1*-null ES cells cannot be generated ([retrieved](https://www.researchgate.net/publication/9064525_Dicer_is_essential_for_mouse_development)) | Establishes Dicer as essential and explains why complete biallelic loss cannot model a tumor — consistent with the human hypomorphic-hotspot second hit |
| **Pitx2-Cre; *Dicer1*^flox/flox** | Mammalian, conditional/tissue-specific KO | "Loss of *Dicer1* function in Pitx2Cre/Dicer1^flox/flox mice results in **hypoplastic anterior pituitary lobes and growth retardation with decreased levels of prolactin and growth and thyroid stimulating hormones**" ([Genome Med 2024, PMC11140907](https://pmc.ncbi.nlm.nih.gov/articles/PMC11140907/)) | **The closest available model of the developmental arm.** Recapitulates *arrested adenohypophyseal development* but produces hypopituitarism/hypoplasia, **not a blastoma** |
| ***Dicer1*^E1705K mouse cell model** | Cellular/in vitro (murine) | "A mouse cell model of DRTP (*Dicer1*^E1705K…) has been developed"; "Expression of DICER1 hotspot mutants **promoted cell proliferation, whereas wild-type DICER1 inhibited** cell proliferation"; growth advantage "at least partially due to loss of let-7 expression" ([retrieved; bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.10.15.682667.full.pdf)) | Models the **hotspot second hit** and the let-7 loss step of the causal chain |
| **Human/engineered cell systems for strand switch** | In vitro | Hotspot mutation "induces 3p microRNA **gain of function via Argonaute strand switch**" ([*Nat Struct Mol Biol* 2025](https://www.nature.com/articles/s41594-025-01671-w)) | Models the gain-of-function branch |
| **Primary PitB tissue profiling** (3 fresh-frozen tumors vs 3 fetal + 3 postnatal normal pituitaries, plus 21-sample validation series) | Human ex vivo — the de facto "model system" for this disease | Multi-omic characterization: 5p/3p miRNA skew, PRAME 500-fold up, RAR/WNT/NOTCH dysregulation, PI3K activation, quiet genome, distinct methylation class ([PMID 33644822](https://pubmed.ncbi.nlm.nih.gov/33644822/)) | **The primary evidence base substitutes for an animal model** |
| **Dicer1 in gonadal/other tissues** (e.g. folliculogenesis) | Mammalian conditional KO | Dicer regulates folliculogenesis in mice ([PMC2814883](https://pmc.ncbi.nlm.nih.gov/articles/PMC2814883/)) | Background on tissue-specific Dicer requirement; not PitB-relevant |

### Genetic model types available for *Dicer1*

Constitutive knockout, **conditional (floxed) alleles** usable with any pituitary Cre driver (Pitx2-Cre demonstrated; Hesx1-, Prop1-, Pomc-Cre are conceivable but **I retrieved no published pituitary-blastoma attempt**), and **hotspot knock-in** approaches (E1705K at cell-model level). Humanized models: none retrieved. Repositories: [MGI](https://www.informatics.jax.org/marker/MGI:2177178), RGD, IMPC/KOMP, IMSR, EMMA, MMRRC.

### Phenotype recapitulation and limitations

- **What is recapitulated:** the *molecular* lesion (5p miRNA loss, let-7 depletion, 3p gain, proliferative advantage) and, separately, the *developmental* consequence of pituitary Dicer loss (anterior-lobe hypoplasia, multi-hormone deficiency).
- **What is NOT recapitulated:** the tumor. **No model produces a pituitary blastoma, ACTH-driven infantile Cushing syndrome, the three-cell-population histology, Rathke-type rosettes, or the PitB methylation class.** The timing problem is central: human PitB requires a hotspot second hit in a Rathke-pouch progenitor within a narrow developmental window, and conditional complete loss instead yields hypoplasia.
- **Research applications currently feasible:** dissecting miRNA biogenesis and let-7 biology, testing candidate pathway inhibitors (PI3K, RAR) in hotspot-mutant cells, and modeling pituitary developmental arrest. Not feasible: preclinical therapeutic testing against an authentic PitB tumor model.
- **The clear research gap:** a **conditional, pituitary-progenitor-restricted *Dicer1* hotspot knock-in (e.g. Pitx2-Cre or Hesx1-Cre driving E1705K/D1709N on a LoF background)** is the obvious unbuilt model, and none was found in retrieval.

---

## Evidence summary, source types, and explicit gaps

**Evidence-type distribution.** Human clinical/pathological: the entire clinical, phenotypic, prognostic, and treatment base (n≈17–23 total world cases; largest cohorts n=17). Human molecular/ex vivo: the mechanistic core (small-RNA-seq, RNA-seq, methylation, WGS on 3 tumors + 21-sample validation). In vitro/cell models: hotspot functional consequences (let-7 loss, 3p strand switch, proliferation). Model organism: *Dicer1* developmental biology only — **no tumor model**. Computational: gene-constraint metrics (pLI/LOEUF), carrier-prevalence estimates from population exomes.

**What I could not retrieve and therefore did not state:**
- PMIDs for de Kock 2014 (*Acta Neuropathol*), Liu 2021 (*JCEM*), Chong 2021 (*Acta Neuropathol*), Bakhuizen 2021 (*Fam Cancer*) — DOIs/PMC IDs given instead.
- Any dedicated **Orphanet (ORPHA)** entry, **MeSH** descriptor, or **ICD-10/ICD-11** code for pituitary blastoma; any separate **OMIM phenotype MIM** for PitB.
- **CL (Cell Ontology)** identifiers for corticotroph, folliculostellate, and Rathke-epithelial cells; **NCIT** codes for the interventions; **CHEBI** codes for the chemotherapeutics; **LOINC** codes for the endocrine assays; **NCBI Taxon** and **VBO** identifiers for the dog; a general **UBERON** id for "pituitary gland" (only UBERON:0006964, pars distalis of adenohypophysis, was verified).
- HPO identifiers beyond the four verified (**HP:0034921**, **HP:0000602**, **HP:0000873**, **HP:0000505**, **HP:0000871**); Cushingoid-habitus and increased-ACTH HPO ids remain unverified.
- Any **incidence/prevalence rate**, **5-/10-year survival rate**, **life expectancy**, or **DALY/GBD** figure for PitB — none exists in the literature I could reach.
- Any **PitB-specific proteomic, metabolomic, lipidomic, single-cell, spatial, or CRISPR-screen** dataset; any **interventional clinical trial** enrolling PitB; any **PGx** guidance; any **prognostic model**.

**Bottom line for the knowledge base.** Pituitary blastoma is a single-gene disease: a germline loss-of-function *DICER1* variant plus a somatic RNase IIIb hotspot missense in a fetal/infant adenohypophyseal progenitor produces selective 5p-miRNA (let-7) loss with 3p gain, which arrests Rathke-pouch differentiation while driving proliferation, generating an ACTH-secreting embryonal tumor that presents at a median of 11 months with infantile Cushing syndrome, cranial neuropathies, and visual loss, kills roughly half of those affected, and leaves survivors with lifelong endocrine, visual, and neurodevelopmental deficits plus lifelong DICER1-spectrum cancer risk. Its diagnosis is, by itself, an indication for germline *DICER1* testing and for enrolling the family in cascade testing and surveillance.

---

**Sources:**

- [Pituitary blastoma — Scheithauer et al., *Acta Neuropathol* 2008;116:657–666 (PMID 18551299)](https://link.springer.com/article/10.1007/s00401-008-0388-9)
- [Pituitary blastoma: a unique embryonal tumor — *Pituitary* 2012;15(3):365–73 (PMID 21805093)](https://pubmed.ncbi.nlm.nih.gov/21805093/)
- [Pituitary blastoma: a pathognomonic feature of germ-line DICER1 mutations — de Kock et al., *Acta Neuropathol* 2014;128:111–122](https://link.springer.com/article/10.1007/s00401-014-1285-z)
- [Germline and somatic DICER1 mutations in a pituitary blastoma causing infantile-onset Cushing's disease — *JCEM* 2014 (PMID 24823459)](https://pubmed.ncbi.nlm.nih.gov/24823459/)
- [Clinical Outcomes and Complications of Pituitary Blastoma — *JCEM* 2021;106(2):351](https://academic.oup.com/jcem/article/106/2/351/6000434) · [PMC7823240](https://pmc.ncbi.nlm.nih.gov/articles/PMC7823240/) · [ESPE Yearbook summary](https://www.espeyearbook.org/ey/0018/ey0018.1-15)
- [Molecular characterization of DICER1-mutated pituitary blastoma — *Acta Neuropathol* 2021;141:929–944 (PMID 33644822)](https://pubmed.ncbi.nlm.nih.gov/33644822/) · [Springer](https://link.springer.com/article/10.1007/s00401-021-02283-6)
- [Expanding the clinical and molecular spectrum of pituitary blastoma — *Acta Neuropathol* 2022;143:415–417 (PMID 35129635)](https://pubmed.ncbi.nlm.nih.gov/35129635/)
- [DICER1 syndrome in a young adult with pituitary blastoma — *Acta Neuropathol* 2021](https://link.springer.com/article/10.1007/s00401-021-02378-0)
- [Pituitary Blastoma: Expanding the Spectrum of Histopathological Findings in a Young Adult With DICER1 Mutation — *Neuropathology* 2025 (PMID 40451220)](https://pubmed.ncbi.nlm.nih.gov/40451220/)
- [Concurrent Pit-1 and SALL4 staining in primitive component of pituitary blastoma — *J Neuropathol Exp Neurol* 2025;84(5):436](https://academic.oup.com/jnen/article/84/5/436/7917506)
- [Pituitary blastoma, expanding the spectrum of newly recognized entities. A case report (PMID 35435381)](https://pubmed.ncbi.nlm.nih.gov/35435381/)
- [Pituitary Blastoma in a 19-Year-Old Woman — *World Neurosurgery* case report](https://www.sciencedirect.com/science/article/abs/pii/S1878875020308032)
- [A 16-year-old female with an intrasellar mass — *Brain Pathol* 2025 (PMID 40040389)](https://pubmed.ncbi.nlm.nih.gov/40040389/) · [PMC11961203](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11961203/)
- [Pituitary blastoma in a dog — PMID 42177605](https://pubmed.ncbi.nlm.nih.gov/42177605/) · [PMC13383401](https://pmc.ncbi.nlm.nih.gov/articles/PMC13383401/)
- [Pulmonary neoplasms with PPB-like features in two young Labrador Retrievers — *Vet Sci* 2025](https://www.mdpi.com/2306-7381/13/10/1111)
- [MedGen: Pituitary blastoma (C4743978 / UID 1656462)](https://www.ncbi.nlm.nih.gov/medgen/1656462) · [MalaCards: Pituitary Blastoma](https://www.malacards.org/card/pituitary_blastoma) · [DOID:0081244](https://www.informatics.jax.org/disease/DOID:0081244) · [Mondo curation issue #18554](https://github.com/monarch-initiative/dismech/issues/18554)
- [ICD-O M-8273/3 Pituitary blastoma](http://notasalud.com/cie-o/m-8273-3) · [ICD-O-3.2 changes (ENCR)](https://www.encr.eu/sites/default/files/inline-files/Changes%20ICD-O-3.2.pdf)
- [Overview of the 2022 WHO Classification of Pituitary Tumors — *Endocr Pathol*](https://link.springer.com/article/10.1007/s12022-022-09703-7) · [Clinical integration of the 2022 WHO pituitary classification, PMC12288123](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12288123/)
- [OMIM \*606241 DICER1](https://omim.org/entry/606241) · [OMIM #601200 Pleuropulmonary blastoma](https://omim.org/entry/601200)
- [NCBI Gene: DICER1 (23405)](https://www.ncbi.nlm.nih.gov/gene/23405) · [Ensembl ENSG00000100697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?db=core&g=ENSG00000100697&r=14:95086228-95158010) · [Monarch HGNC:17098](https://monarchinitiative.org/HGNC:17098) · [Human Protein Atlas DICER1](https://www.proteinatlas.org/ENSG00000100697-DICER1/summary/gene) · [Atlas of Genetics & Cytogenetics: DICER1](https://atlasgeneticsoncology.org/gene/45773/dicer1-(dicer-1-ribonuclease-iii))
- [ClinGen DICER1 dosage sensitivity (HGNC:17098)](https://search.clinicalgenome.org/kb/gene-dosage/HGNC:17098) · [ClinGen DICER1 ACMG/AMP specifications v1](https://clinicalgenome.org/site/assets/files/8147/clingen_dicer1_acmg_specifications_dicer1_v1.pdf) · [ClinGen actionability AC002](https://actionability.clinicalgenome.org/ac/ui/Adult/ui/stg2SummaryRpt/AC002) · [Genomics England PanelApp DICER1](https://panelapp.genomicsengland.co.uk/panels/entities/DICER1)
- [GeneReviews: DICER1-Related Tumor Predisposition (NBK196157)](https://www.ncbi.nlm.nih.gov/sites/books/NBK196157/)
- [DICER1-Related Tumor Predisposition: Identification of At-risk Individuals and Recommended Surveillance Strategies — *Clin Cancer Res* 2024;30(24):5681 (PMID 39400264)](https://aacrjournals.org/clincancerres/article/30/24/5681/750430/DICER1-Related-Tumor-Predisposition-Identification) · [PMC11649450](https://pmc.ncbi.nlm.nih.gov/articles/PMC11649450)
- [DICER1 and Associated Conditions: surveillance strategies — Schultz et al. 2018 (PMID 29343557)](https://www.researchgate.net/publication/322564582_DICER1_and_Associated_Conditions_Identification_of_At-risk_Individuals_and_Recommended_Surveillance_Strategies)
- [Surveillance recommendations for DICER1 pathogenic variant carriers — SIOPE HGWG / CanGene-CanVar, *Fam Cancer* 2021 (PMC8484187)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8484187/) · [eviQ DICER1 risk management](https://www.eviq.org.au/cancer-genetics/adult/risk-management/3569-dicer1-risk-management-adult)
- [Neoplasm Risk Among Individuals With a Pathogenic Germline Variant in DICER1 — Khan et al., *JCO* 2019 (PMID 30715996)](https://pubmed.ncbi.nlm.nih.gov/30715996/) · [ASCO Post summary](https://ascopost.com/News/59785)
- [The prevalence of DICER1 pathogenic variation in population databases — Kim et al., *Int J Cancer* 2017](https://onlinelibrary.wiley.com/doi/abs/10.1002/ijc.30907) · [Prevalence in cancer populations, *Mol Genet Genomic Med* 2019 (PMC6418698)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6418698/)
- [Ten years of DICER1 mutations: provenance, distribution, associated phenotypes — *Hum Mutat* 2019;40:1939–1953](https://onlinelibrary.wiley.com/doi/10.1002/humu.23877)
- [DICER1 tumor predisposition syndrome: an evolving story initiated with the pleuropulmonary blastoma (PMC8695383)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8695383/) · [DICER1 Tumor Syndrome: retrospective review](https://www.mdpi.com/2673-5261/5/3/19) · [DICER1 Syndrome: pathogenetic mechanisms, *Cancers* 2025](https://www.mdpi.com/2072-6694/17/17/2885) · [DICER1 Syndrome and Cancer Predisposition (PMC7859642)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7859642/)
- [DICER1: mutations, microRNAs and mechanisms — *Nat Rev Cancer* 2014](https://www.nature.com/articles/nrc3802) · [DICER1 hotspot mutation induces 3p microRNA gain of function via Argonaute strand switch — *Nat Struct Mol Biol* 2025](https://www.nature.com/articles/s41594-025-01671-w) · [Human Dicer1 hotspot mutation induces both loss and gain of miRNA function (bioRxiv 2025)](https://www.biorxiv.org/content/10.1101/2025.10.15.682667.full.pdf) · [DICER1 RNase IIIb mutations trigger miRNA dysregulation and MAPK activation in pediatric thyroid cancer (PMID 36896180 / PMC9990750)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9990750/) · [DICER1 platform domain missense variants (PMC10273190)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10273190/)
- [Temporal order of RNase IIIb and LoF mutations determines phenotype — *F1000Research* 2015 (PMC4712775)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4712775/) · [GLOW syndrome: mosaic RNase IIIb missense mutations](https://www.researchgate.net/publication/261187740_Expanding_the_phenotype_of_mutations_in_DICER1_mosaic_missense_mutations_in_the_RNase_IIIb_domain_of_DICER1_cause_GLOW_syndrome) · [High-sensitivity sequencing reveals multi-organ somatic mosaicism](https://www.semanticscholar.org/paper/High-sensitivity-sequencing-reveals-multi-organ-Kock-Wang/51475c6993ae32172bf6f7d31705cbb04a8f068f) · [Intronic germline DICER1 variants in SLCT — *JCO PO* 2023](https://ascopubs.org/doi/10.1200/PO.23.00189) · [Reclassification of two germline DICER1 splicing variants (PMID 37248399)](https://pubmed.ncbi.nlm.nih.gov/37248399/) · [ClinVar RCV000226155 (DICER1 c.2026C>T)](https://www.ncbi.nlm.nih.gov/clinvar/RCV000226155.7/)
- [A survey of DICER1 hotspot mutations in ovarian and testicular sex cord-stromal tumors — *Mod Pathol* 2015](https://www.nature.com/articles/modpathol2015115) · [PEG10 as a candidate biomarker for malignant DICER1 tumors — *J Pathol* 2025](https://pathsocjournals.onlinelibrary.wiley.com/doi/10.1002/path.70141) · [Spatial single-cell analysis of DICER1-related sarcoma (PMID 41912509)](https://pubmed.ncbi.nlm.nih.gov/41912509/) · [Non-C19MC-altered ETMR in DICER1 syndrome (PMC11447652)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11447652) · [Pathology Outlines: Primary intracranial sarcoma, DICER1-mutant](https://www.pathologyoutlines.com/topic/CNSintracranialsarcoma.html)
- [Endotext: Cushing Syndrome/Disease in Children and Adolescents (NBK602210)](https://www.ncbi.nlm.nih.gov/sites/books/NBK602210/) · [ACTH-secreting pituitary adenoma in an 18-month infant (PMID 6278457)](https://pubmed.ncbi.nlm.nih.gov/6278457/) · [Consensus guideline for pituitary adenomas in childhood and adolescence, Part 2 — *Nat Rev Endocrinol* 2023](https://www.nature.com/articles/s41574-023-00949-7)
- [Cushing's disease: adrenal steroidogenesis inhibitors (PMC9587932)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9587932/) · [Surgical approach to patients with hypercortisolism — *Gland Surgery*](https://gs.amegroups.org/article/view/34956/html) · [ESE Clinical Update on Cushing's Syndrome 2021](https://www.ese-hormones.org/media/z1el5vx4/ese-cu-cushings-webinar-report_v13-web.pdf)
- [Primary tumors of the pituitary gland: radiologic-pathologic correlation — *RadioGraphics* 2021](https://pubs.rsna.org/doi/10.1148/rg.2021200203) · [Neoplasms and tumor-like lesions of the sellar region (PMC10033642)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10033642/) · [High-grade AT/RT in the pituitary region (PMC10938043)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10938043/)
- [UBERON:0006964 pars distalis of adenohypophysis (EBI OLS)](https://www.ebi.ac.uk/ols/ontologies/uberon/terms?iri=http://purl.obolibrary.org/obo/UBERON_0006964) · [BioPortal UBERON:0006964](https://bioportal.bioontology.org/ontologies/UBERON?p=classes&conceptid=UBERON:0006964) · [Anatomy, Adenohypophysis (StatPearls, NBK519039)](https://www.ncbi.nlm.nih.gov/books/NBK519039/?report=reader)
- [AmiGO GO:0031054 pre-miRNA processing](https://amigo.geneontology.org/amigo/term/GO:0031054) · [AmiGO GO:0035195 miRNA-mediated post-transcriptional gene silencing](https://amigo.geneontology.org/amigo/term/GO:0035195) · [HPO HP:0000873 Diabetes insipidus (Monarch)](https://monarchinitiative.org/HP:0000873) · [HPO portal](https://hpo.jax.org/)
- [Dicer is essential for mouse development — Bernstein et al. 2003](https://www.researchgate.net/publication/9064525_Dicer_is_essential_for_mouse_development) · [Knockout mice with pituitary malformations help identify human cases of hypopituitarism — *Genome Med* 2024 (PMC11140907)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11140907/) · [MGI Dicer1 MGI:2177178](https://www.informatics.jax.org/marker/MGI:2177178) · [RGD Dicer1](https://rgd.mcw.edu/rgdweb/report/gene/main.html?id=1319699) · [The regulatory role of Dicer in folliculogenesis (PMC2814883)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2814883/)
- [Folliculostellate cells review (PMC11475256)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11475256/) · [Claudin-9 in folliculo-stellate cells (PMC8568902)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8568902/)
- ClinicalTrials.gov: [NCT03382158 International PPB/DICER1 Registry](https://clinicaltrials.gov/study/NCT03382158) · [NCT00565903](https://clinicaltrials.gov/study/NCT00565903) · [NCT01247597](https://clinicaltrials.gov/study/NCT01247597) · [NCT01970696](https://clinicaltrials.gov/study/NCT01970696) · [HRQoL in PPB (PMC9974753)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9974753/)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 49 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 2 |
| Unverifiable | 0 |
| Quoted claims checked | 20 |
| Quoted claims found in source | 5 |
| Quoted claims **not** found in source | 15 |
| Quoted claims with nothing to check against | 13 |
| References weighed for topical relevance | 47 |
| On topic | 31 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:41912509` (5 mentions) - Identifier did not resolve to a record
- `PMC:PMC11475256` (5 mentions) - Identifier did not resolve to a record

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

7 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:33644822` *(abstract only)*: "**Sixteen of seventeen pituitary blastoma cases were attributed to *DICER1* abnormalities**"
  - closest text in source: "Pituitary blastoma (PitB) has recently been identified as a rare and potentially lethal pediatric intracranial tumor"
- `DOI:10.3389/fonc.2020.614541` *(abstract only)*: "are more prone to manifestations in multiple sites"
  - Text part not found as substring: 'are more prone to manifestations in multiple sites' (note: only abstract available for DOI:10.3389/fonc.2020.614541, full text may contain this excerpt)
- `PMC:PMC4712775` *(abstract only)*: "a unique variant of the two-hit tumor suppression model"
  - closest text in source: "Pleuropulmonary blastoma (PPB) is the most frequent pediatric lung tumor and often the first indication of a pleiotropic cancer predisposition, DICER1 syndrome, comprising a range of other individually rare, benign and malignant tumors of childhood and early adulthood"
- `PMC:PMC7823240`: "experienced hormonal sequelae ranging from **none to panhypopituitarism** and neurocognitive function ranging from **fully functional to impaired**, with some survivors being visually impaired"
  - closest text in source: "Nine of 17 patients survived (median survival, 6.7 years; median age at last follow-up, 10.8 years) with hormonal sequalae ranging from none to panhypopituitarism and neurocognitive function ranging from fully functional to impaired, and some survivors were visually impaired"
- `PMID:33644822` *(abstract only)*: "methylation profiling confirms clustering among pituitary blastoma samples and references"
  - closest text in source: "Here, we characterized nine pituitary samples, including three fresh frozen PitBs, three normal fetal pituitary glands and three normal postnatal pituitary glands using small-RNA-Seq, RNA-Seq, methylation profiling, whole genome sequencing and Nanostring® miRNA analyses; an extended series of 21 pituitary samples was used for validation purposes"
- `PMC:PMC8568902` *(abstract only)*: "express vimentin and the nervous tissue-specific S-100 protein… but no secretory pituitary cell markers"
  - closest text in source: "The expression of claudin-9 was gradually increased in the pituitary gland after birth, suggesting that claudin-9 is developmentally regulated and performs some specific functions on the paracellular barrier of follicles in the pituitary gland"
- `PMID:29343557`: "**Urgent brain MRI is recommended for persons with a *DICER1* pathogenic variant with signs of intracranial pathology or cortisol excess** for the detection of pineoblastoma or pituitary blastoma"
  - closest text in source: "Education regarding signs and symptoms of intracranial tumors (including cortisol excess, increased intracranial pressure, neurologic changes, vomiting, lethargy etc.) is encouraged, with urgent brain MRI suggested for any new presenting symptoms"
- `PMID:39400264`: "**Urgent brain MRI is recommended for persons with a *DICER1* pathogenic variant with signs of intracranial pathology or cortisol excess** for the detection of pineoblastoma or pituitary blastoma"
  - closest text in source: "Pineoblastoma is a rare primitive neuroectodermal tumor most frequently diagnosed in the first two decades of life, with primary presenting symptoms of vomiting, headaches, and altered mental status.[31] Pineoblastoma pathogenesis diverges from the typical acquisition of a tumor-specific somatic missense RNase IIIb “hotspot” variant since loss of heterozygosity of the wild-type DICER1 allele is the usual somatic event.[31] Pituitary blastoma is a rare tumor of the anterior pituitary that generally occurs in children aged 2 years and younger and presents with Cushing syndrome, ophthalmoplegia, and/or diabetes insipidus.[32] Nearly all cases of pituitary blastoma with documented germline testing have germline DICER1 P/LP variants.[32] PIS DICER1 has been described in multiple series and is primarily diagnosed in the first two decades of life.[33–35] Although some cases of primary PIS DICER1 have been reported in the context of a germline DICER1 P/LP variant, in many cases, DICER1 alteration is confined to the tumor"
- `PMC:PMC11649450`: "a pituitary mass in a young child"
  - closest text in source: "Data from a separate cohort showed lung cysts in 39% of individuals with a germline DICER1 P/LP variant whose first chest CT was performed at 12 years of age or older.[20] Further studies of the mechanism of non-progression or regression of DICER1-related lung cysts in childhood are needed to guide judicious surgical intervention and inform decision making for cystic lesions in young children"
- `PMC:PMC9587932` *(abstract only)*: "has nearly a 100% success rate and results in immediate control of steroid excess"
  - closest text in source: "The current review focuses on efficacy and safety of steroidogenesis inhibitors, and particularly the historical drugs, ketoconazole and metyrapone, and the novel drugs levoketoconazole and osilodrostat, which seem to offer a rapid, sustained, and effective disease control"
- `PMID:29343557`: "**Urgent brain MRI is recommended for persons with a *DICER1* pathogenic variant with signs of intracranial pathology or cortisol excess** for the detection of pineoblastoma or pituitary blastoma"
  - closest text in source: "Education regarding signs and symptoms of intracranial tumors (including cortisol excess, increased intracranial pressure, neurologic changes, vomiting, lethargy etc.) is encouraged, with urgent brain MRI suggested for any new presenting symptoms"
- `PMID:39400264`: "**Urgent brain MRI is recommended for persons with a *DICER1* pathogenic variant with signs of intracranial pathology or cortisol excess** for the detection of pineoblastoma or pituitary blastoma"
  - closest text in source: "Pineoblastoma is a rare primitive neuroectodermal tumor most frequently diagnosed in the first two decades of life, with primary presenting symptoms of vomiting, headaches, and altered mental status.[31] Pineoblastoma pathogenesis diverges from the typical acquisition of a tumor-specific somatic missense RNase IIIb “hotspot” variant since loss of heterozygosity of the wild-type DICER1 allele is the usual somatic event.[31] Pituitary blastoma is a rare tumor of the anterior pituitary that generally occurs in children aged 2 years and younger and presents with Cushing syndrome, ophthalmoplegia, and/or diabetes insipidus.[32] Nearly all cases of pituitary blastoma with documented germline testing have germline DICER1 P/LP variants.[32] PIS DICER1 has been described in multiple series and is primarily diagnosed in the first two decades of life.[33–35] Although some cases of primary PIS DICER1 have been reported in the context of a germline DICER1 P/LP variant, in many cases, DICER1 alteration is confined to the tumor"
- `PMC:PMC11649450`: "**Urgent brain MRI is recommended for persons with a *DICER1* pathogenic variant with signs of intracranial pathology or cortisol excess** for the detection of pineoblastoma or pituitary blastoma"
  - closest text in source: "Pineoblastoma is a rare primitive neuroectodermal tumor most frequently diagnosed in the first two decades of life, with primary presenting symptoms of vomiting, headaches, and altered mental status.[31] Pineoblastoma pathogenesis diverges from the typical acquisition of a tumor-specific somatic missense RNase IIIb “hotspot” variant since loss of heterozygosity of the wild-type DICER1 allele is the usual somatic event.[31] Pituitary blastoma is a rare tumor of the anterior pituitary that generally occurs in children aged 2 years and younger and presents with Cushing syndrome, ophthalmoplegia, and/or diabetes insipidus.[32] Nearly all cases of pituitary blastoma with documented germline testing have germline DICER1 P/LP variants.[32] PIS DICER1 has been described in multiple series and is primarily diagnosed in the first two decades of life.[33–35] Although some cases of primary PIS DICER1 have been reported in the context of a germline DICER1 P/LP variant, in many cases, DICER1 alteration is confined to the tumor"
- `PMC:PMC11649450`: "**Provider and individual/family education is the cornerstone of surveillance**"
  - closest text in source: "Patient, family, and clinician education remain the cornerstone of surveillance"
- `PMC:PMC11140907` *(abstract only)*: "Loss of *Dicer1* function in Pitx2Cre/Dicer1^flox/flox mice results in **hypoplastic anterior pituitary lobes and growth retardation with decreased levels of prolactin and growth and thyroid stimulating hormones**"
  - closest text in source: "RESULTS: Of the 209 knockout mouse lines, we identified 51 that have embryonic pituitary malformations"

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1007/s00401-008-0388-9`: "(a) prominence of primitive Rathke-type epithelium, (b) disposition of secretory cells in lobules rather than acini, (c) the limited range of secretory cells represented, (d) the presence of their corresponding transcription factors, and (e) ultrastructural features indicating orderly development of the 10- to 12-week embryonic stage"
  - Reference resolved but exposes no abstract or full text to search
- `DOI:10.1007/s00401-014-1285-z`: "**nine of ten tested infants with pituitary blastoma harbored a heterozygous germ-line *DICER1* mutation**"
  - Reference resolved but exposes no abstract or full text to search
- `DOI:10.1007/s00401-014-1285-z`: "**Nine of ten tested PitB tumor samples harbored additional *DICER1* mutations, eight of which were confirmed to be somatic in origin**"
  - Reference resolved but exposes no abstract or full text to search
- `DOI:10.1007/s00401-021-02283-6`: "*DICER1* RNase IIIb hotspot mutations in pituitary blastomas induced **improper processing of miRNA precursors, resulting in aberrant 5p-derived miRNA products and a skewed distribution of miRNAs favoring mature 3p over 5p miRNAs**"
  - Reference resolved but exposes no abstract or full text to search
- `PMID:35129635`: "**decreased mature microRNA expression and preferential down-regulation of 5p/3p species in tumor compared to control pituitary tissue**"
  - Reference resolved but exposes no abstract or full text to search
- `DOI:10.1007/s00401-021-02283-6`: "the **PI3K pathway is activated** in the tumors"
  - Reference resolved but exposes no abstract or full text to search
- `PMID:41912509`: "Spatial single cell transcriptomic analysis informs tumor developmental hierarchy of DICER1 syndrome related sarcoma"
  - Reference did not resolve, so the quote could not be checked
- `PMC:PMC11475256`: "express vimentin and the nervous tissue-specific S-100 protein… but no secretory pituitary cell markers"
  - Reference did not resolve, so the quote could not be checked
- `DOI:10.1148/rg.2021200203`: "Pituitary blastoma presents as an **intra- and suprasellar mass with inhomogeneous enhancement, potentially invading the cavernous sinus and adjacent structures**"
  - Reference resolved but exposes no abstract or full text to search
- `PMID:35129635`: "exclusively in children under 2 years of age"
  - Reference resolved but exposes no abstract or full text to search
- `DOI:10.1007/s00401-021-02378-0`: "the first case of a pituitary blastoma occurring in a young adult"
  - Reference resolved but exposes no abstract or full text to search
- `DOI:10.1002/humu.23877`: "are typically inherited in an autosomal dominant pattern but **may arise de novo in the germline or in a somatic mosaic distribution**"
  - Reference resolved but exposes no abstract or full text to search
- `PMID:40040389`: "pituitary blastoma should be included as a differential diagnosis"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 18 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 5 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0858916` (3 mentions) - the report calls it "Mondo"; MONDO calls it **pituitary blastoma**
- `DOID:0081244` (5 mentions) - the report calls it "Disease Ontology"; DOID calls it **pituitary blastoma**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`, `RGD`.