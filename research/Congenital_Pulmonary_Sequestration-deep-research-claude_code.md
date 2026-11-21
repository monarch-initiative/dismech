---
provider: claude_code
model: claude-fable-5, claude-haiku-4-5-20251001
cached: false
start_time: '2026-11-11T19:22:20.546698'
end_time: '2026-11-11T19:30:41.381493'
duration_seconds: 500.83
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Congenital Pulmonary Sequestration
  mondo_id: MONDO:0017843
  category: ''
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: bronchopulmonary sequestration; congenital bronchopulmonary sequestration;
    congenital sequestration of lung; pulmonary sequestration; sequestered lobe (pulmonary
    sequestration)
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
  - claude-fable-5
  - claude-haiku-4-5-20251001
  web_search_requests: 33
  num_turns: 34
  total_cost_usd: 12.639677000000004
  session_id: 594f7fb3-13cc-47d2-b062-2b52497ad791
  stop_reason: end_turn
  assistant_text_blocks: 5
citation_count: 58
reference_validation:
  total_references: 47
  verified: 47
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 4
  quotes_valid: 3
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:14632303
  relevance_assessed: 47
  on_topic: 30
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 35
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: UBERON:0002048
    reported_labels:
    - Primary organ:** lung
    ontology_label: lung
  - term_id: NCBITaxon:10090
    reported_labels:
    - Mouse developmental biology
    ontology_label: Mus musculus
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Pulmonary Sequestration
- **MONDO ID:** MONDO:0017843 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** bronchopulmonary sequestration; congenital bronchopulmonary sequestration; congenital sequestration of lung; pulmonary sequestration; sequestered lobe (pulmonary sequestration)
- **Category:** 

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Congenital Pulmonary Sequestration** covering all of the
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

I'll research Congenital Pulmonary Sequestration (MONDO:0017843) and produce the full report inline. First, let me load the web search tool and gather sources.

Now I'll run a batch of searches covering the main axes of the report.

Good grounding so far. Continuing with epidemiology, mechanism, complications, treatment, and comparative sections.

Nearly complete. One final batch to pin down PMIDs for the load-bearing citations.

All research is done — I have the identifiers, epidemiology, mechanism, clinical, treatment, and comparative data with PMIDs. Here is the complete report.

---

# Comprehensive Research Report: Congenital Pulmonary Sequestration

**Target:** Congenital Pulmonary Sequestration — **MONDO:0017843**
**Report date:** 2026-11-11

**Causal gene statement (per template instruction):** Congenital pulmonary sequestration has **no established causal gene**. It is a sporadic structural birth defect of lung development, not a Mendelian disorder: no OMIM phenotype entry, no ClinGen gene–disease validity assertion, and no recurrent pathogenic variant has been attributed to it. The strongest molecular lead is dysregulated persistence of the developmental transcription factor **HOXB5** (with downstream cell-adhesion molecules α2/α3/β1-integrin and E-cadherin) in resected sequestration tissue — an observational tissue-level finding, not a demonstrated germline cause (PMID:14632303; PMID:19411307). A single report of recurrence in two male siblings (PMID:8677110) is the only evidence suggesting any genetic predisposition.

> **Term-validation caveat:** every ontology CURIE suggested below (HP/GO/CL/UBERON/NCIT/CHEBI) is a *lead written from the author's knowledge, not from a same-step ontology lookup*, and must be validated against the ontology (OAK/OLS) before being bound in any KB entry. Quoted sentences were taken from search-result renderings of abstracts/articles and must be re-verified verbatim against the cached reference before use as evidence snippets.

---

## 1. Disease Information

**Overview.** Congenital pulmonary sequestration (synonyms: bronchopulmonary sequestration, BPS; pulmonary sequestration; sequestered lobe) is a rare congenital lung malformation consisting of a mass of non-functioning lung tissue that (a) lacks normal communication with the tracheobronchial tree and (b) receives its arterial blood supply from the systemic circulation rather than the pulmonary artery. Orphanet defines it as "a cystic or solid mass of nonfunctioning primitive segmental lung tissue that does not communicate with the tracheobronchial tree and has anomalous systemic blood supply" ([Orphanet ORPHA:3161](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=3161)). The term "sequestration" was coined by Pryce in 1946.

Two principal anatomic types:

| Feature | Intralobar sequestration (ILS) | Extralobar sequestration (ELS) |
|---|---|---|
| Share of cases | ~75–84% (83.95% in the 2,625-case Chinese series, PMID:21459605) | ~16–25% |
| Pleura | Within the visceral pleura of a normal lobe | Own separate pleural investment |
| Typical site | Posterobasal segment of a lower lobe (left > right) | Between lower lobe and diaphragm; ~10% infradiaphragmatic/intra-abdominal, intradiaphragmatic, or (rarely) intrapericardial |
| Venous drainage | Pulmonary veins (~95% of cases, usually the inferior pulmonary vein) | Systemic veins (azygos/hemiazygos; rarely portal) |
| Associated anomalies | Uncommon | ~40–60% of symptomatic historical cases (CDH, congenital heart disease, CPAM type 2 hybrid lesions, foregut duplications, vertebral anomalies) |
| Typical presentation | Recurrent lower-lobe pneumonia, hemoptysis in older children/adults | Prenatal detection, or neonatal/infant respiratory distress, feeding difficulty, incidental mass |

**Identifiers:**
- MONDO: **MONDO:0017843** (pulmonary sequestration)
- Orphanet: **ORPHA:3161** (Congenital pulmonary sequestration); subtype entry **ORPHA:280811** (Extralobar congenital pulmonary sequestration)
- ICD-10: **Q33.2** (Sequestration of lung); ICD-11: **LA75.6**
- MeSH: **D001998** (Bronchopulmonary Sequestration); UMLS: C0006288
- OMIM: **none** — no OMIM phenotype entry exists for this malformation
- GARD: entry 4593 ([rarediseases.info.nih.gov](https://rarediseases.info.nih.gov/diseases/4593/congenital-pulmonary-sequestration))

**Data provenance.** All information below derives from aggregated disease-level resources (Orphanet, registry/surveillance studies, surgical and fetal-medicine case series, radiology–pathology reviews) and published patient case series — not from individual-patient EHR data.

## 2. Etiology

**Primary cause — developmental, not genetic or infectious (for the congenital lesion).** The dominant embryologic model is the **accessory lung bud theory**: a supernumerary lung bud arises from the ventral primitive foregut caudal to the normal lung bud and migrates caudally with the developing esophagus; splanchnic vessels supplying the aberrant bud persist as the systemic feeding artery. Budding **before** pleural formation produces a sequestration invested within normal lung (ILS); budding **after** pleural formation produces a separately encased ELS ([ILS review, PMC2876708](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2876708/); [Annals of Thoracic Surgery collective review](https://www.annalsthoracicsurgery.org/article/S0003-4975(10)64417-7/pdf)). A complementary and increasingly favored model is the **bronchial atresia/obstruction sequence**: Riedlinger and colleagues found an atretic bronchus in 100% of extralobar and 82% of intralobar sequestrations examined ("Bronchial atresia is common to extralobar sequestration, intralobar sequestration, congenital cystic adenomatoid malformation, and lobar emphysema," Pediatr Dev Pathol 2006;9:361–373 — PMID to be confirmed on fetch), placing BPS on a shared developmental spectrum with CPAM and congenital lobar emphysema in which the level, degree, and timing of fetal airway obstruction determine the resulting malformation ([Bronchial atresia: the hidden pathology, J Pediatr Surg 2006](https://www.sciencedirect.com/science/article/abs/pii/S0022346805007359)).

For **adult-diagnosed ILS specifically**, an **acquired hypothesis** persists: recurrent necrotizing pneumonia with lower-lobe bronchial obstruction and hypertrophy of pre-existing systemic collateral arteries could produce an ILS-like lesion postnatally. Prenatal ultrasound detection of ILS demonstrates that at least a subset is unambiguously congenital; the field treats ILS origin as mixed/contested ([Intralobar sequestration review, PMC2876708](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2876708/); [AFIP radiologic–pathologic correlation](https://www.researchgate.net/publication/14064271_From_the_Archives_of_the_AFIP_Intralobar_Sequestration_Radiologic-Pathologic_Correlation)). This congenital-vs-acquired fork should be recorded as a mechanistic hypothesis grouping, not resolved silently.

**Risk factors.**
- *Genetic:* none established. No susceptibility loci, no GWAS signal, no modifier genes. A single familial recurrence (two male infants of the same parents, both with left lower-lobe echogenic masses with systemic arterial supply on prenatal US) "raises the possibility of a genetic predisposition" (PMID:8677110).
- *Demographic:* male sex is modestly over-represented — male:female 1.58:1 in 2,625 Chinese cases (PMID:21459605); birth-prevalence 0.45 vs 0.38 per 10,000 by infant sex in the Chinese Birth Defects Monitoring Network ([BMC Pulm Med 2023, DOI:10.1186/s12890-023-02308-8](https://bmcpulmmed.biomedcentral.com/articles/10.1186/s12890-023-02308-8)). ELS shows the stronger male predominance (classically ~3–4:1). The Changsha 11-year surveillance analysis found prevalence significantly correlated with **maternal age and education level** (PMID:39837960) — associations, not demonstrated causes.
- *Environmental:* no toxin, infection, or exposure has been causally linked to BPS.

**Protective factors:** none known, genetic or environmental.

**Gene–environment interactions:** none documented.

## 3. Phenotypes

Phenotype expression is strongly stratified by lesion type and age at presentation. Candidate HPO terms are flagged ⚠ = verify before binding.

| Phenotype | Type | Onset / context | Frequency & notes | Candidate HPO ⚠ |
|---|---|---|---|---|
| Echogenic fetal thoracic mass ± mediastinal shift | Imaging sign | Prenatal (2nd trimester) | Majority of modern diagnoses are prenatal | HP:0002088 Abnormal lung morphology |
| Nonimmune hydrops fetalis | Sign | Fetal | ~7% of ELS; driven by tension hydrothorax; 100% fetal demise if untreated hydrops ([UCSF Fetal Center](https://fetus.ucsf.edu/pulmonary-sequestration/); [Management Options, PMC8954010](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8954010/)) | HP:0001790 Nonimmune hydrops fetalis |
| Pleural effusion / fetal hydrothorax | Sign | Fetal–neonatal; also universal in ELS torsion | Present in all torsion cases in series (PMC9241176) | HP:0002202 Pleural effusion |
| Polyhydramnios | Sign | Fetal | With large lesions/esophageal compression | HP:0001561 Polyhydramnios |
| Neonatal respiratory distress, cyanosis | Sign | Neonatal (mostly ELS, large lesions) | Variable | HP:0002098 Respiratory distress; HP:0000961 Cyanosis |
| Feeding difficulty | Symptom | Infant (ELS, esp. infradiaphragmatic) | Occasional | HP:0011968 Feeding difficulties |
| Recurrent/refractory pneumonia in a fixed (usually left lower-lobe) location | Symptom/sign | Childhood–adult (ILS) | ~50% of adult cases: 13/25 recurrent infection incl. lung abscess and empyema ([25 adult cases, PMC5393996](https://pmc.ncbi.nlm.nih.gov/articles/PMC5393996/)) | HP:0006532 Recurrent pneumonia ⚠ |
| Cough, fever, chest pain | Symptoms | Childhood–adult | Most common symptoms in the 2,625-case series (PMID:21459605) | HP:0012735 Cough; HP:0100749 Chest pain ⚠ |
| Hemoptysis (occasionally massive) | Symptom | Adolescent–adult (ILS) | 16% (4/25) of adult cases (PMC5393996); massive hemoptysis case reports (PMID:31886079) | HP:0002105 Hemoptysis |
| High-output congestive heart failure ± pulmonary hypertension | Sign | Neonatal/infant | Rare; large systemic-to-pulmonary-vein shunt through the lesion ([preterm case](https://www.sciencedirect.com/science/article/pii/S2213576615001062); embolization cohort neonate, [Children 2026](https://doi.org/10.3390/children13060842)) | HP:0001635 Congestive heart failure ⚠; HP:0002092 ⚠ |
| Acute chest/abdominal pain from torsion and infarction of ELS | Sign | Child > adult | Rare; hemorrhagic effusion + necrotic mass (PMC9241176; PMID:40674965) | — |
| Asymptomatic incidental mass | — | Any age | 28% (7/25) of adult series asymptomatic (PMC5393996); >50% of Wei & Li cases diagnosed after age 20 (PMID:21459605) | — |

**Progression/severity:** ILS infections are typically chronic, recurrent, and antibiotic-refractory; hemoptysis can escalate to life-threatening. Fetal lesions frequently *regress*: ~80% show partial regression from ~26 weeks and up to ~18.5–50%+ substantial or complete prenatal regression (series-dependent) ([Prenatal growth characteristics, PMC5828905](https://pmc.ncbi.nlm.nih.gov/articles/PMC5828905/)). **Quality-of-life** data specific to BPS are limited to surgical-recovery series; no EQ-5D/SF-36 disease-specific literature was identified — a genuine knowledge gap.

## 4. Genetic / Molecular Information

- **Causal genes:** none. No OMIM entry, no ClinVar/ClinGen assertions, no recurrent pathogenic variants in the malformation itself.
- **Pathogenic variants / allele frequencies / zygosity:** not applicable — the lesion is almost always sporadic and no causal variant class is defined. Nothing is known about somatic (post-zygotic, lesion-confined) variants in BPS; unlike CPAM (where mosaic KRAS variants have been reported), no analogous somatic-driver study of sequestration tissue was identified. This is a flaggable knowledge gap, not evidence of absence.
- **Molecular findings in lesion tissue (IN_VITRO/human tissue evidence):**
  - **HOXB5:** in normal human lung, Hoxb-5 protein is high in the pseudoglandular period, decreased in the canalicular period, negligible at the alveolar stage; "In BPS and CCAM tissue, Hoxb-5 is maintained in a manner typical of an earlier developmental stage and is associated with development of abnormal lung tissue" (Volpe et al., Birth Defects Res A 2003;67:550–556, PMID:14632303).
  - **Cell-adhesion molecules:** α2-, α3-, β1-integrin and E-cadherin expression are aberrant in BPS and CCAM tissue previously showing abnormal HoxB5; the authors conclude "aberrant cell adhesion molecule and Hox protein regulation are likely part of the mechanism involved in the development of BPS and CCAM" (Volpe et al., Am J Physiol Lung Cell Mol Physiol 2009;297:L143–L152, PMID:19411307).
- **Modifier genes, epigenetics, chromosomal abnormalities:** none specifically associated. BPS is usually an isolated anomaly; karyotype is typically normal, and routine microarray is not indicated for isolated lesions (associated-anomaly cases, e.g. with CDH, follow the work-up of the associated anomaly). HGNC binding lead for the one named gene: HOXB5 = hgnc:5115 ⚠ (verify).

## 5. Environmental Information

No environmental factor, lifestyle exposure, or infectious agent is known to cause congenital pulmonary sequestration. CTD lists no curated chemical–disease association specific to BPS. Infection is a *downstream complication* (bacterial pneumonia, lung abscess, empyema within the sequestered tissue; case reports of aspergilloma and mycobacterial colonization), never the documented initiating cause of the congenital lesion. The acquired-ILS hypothesis (necrotizing pneumonia as initiating event for some adult ILS) is the one place infection is proposed as etiologic, and it remains contested (see §2).

## 6. Mechanism / Pathophysiology

### Ordered causal chain

**Developmental trunk (congenital origin — demonstrated at tissue level, inferred at molecular level):**
1. An unknown initiating event during weeks 4–8 of gestation — modeled either as a **supernumerary ventral foregut lung bud** or as **segmental bronchial atresia/obstruction** of a developing airway — *leads to* a focus of lung parenchyma disconnected from the tracheobronchial tree. (The two models branch here and may both be true in different patients; the atresia model is supported by atretic bronchi in 82–100% of resected lesions — Riedlinger et al. 2006.)
2. Persistent/aberrant expression of early-developmental patterning factors (HOXB5 retained "in a manner typical of an earlier developmental stage", PMID:14632303) with dysregulated integrin/E-cadherin adhesion signaling (PMID:19411307) *is associated with* disorganized branching of the sequestered tissue — **inferred** as mechanism, demonstrated only as correlation.
3. Failure of the aberrant tissue's primitive splanchnic vascular connections to regress *results in* a persistent systemic feeding artery — thoracic aorta in ~76.6%, abdominal aorta/celiac axis in ~18.5% (PMID:21459605; PMID:442005), with >1 feeder in ~15% (PMID:442005).
4. Timing relative to pleural formation *determines* the branch: early bud → **ILS** (within the lobe, draining to pulmonary veins in ~95%); late bud → **ELS** (own pleura, draining to systemic veins) ([Predictive role of venous drainage, PMC12072680](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12072680/)).
5. The sequestered tissue is ventilated only by collateral channels (pores of Kohn, incomplete) or not at all, *resulting in* a non-functioning, fluid/mucus-filled, often microcystic mass; ~40–50% of ELS carry coexisting CPAM type 2 histology ("hybrid lesions") ([Pathology Outlines](https://www.pathologyoutlines.com/topic/lungnontumorsequestrations.html)).

**Branch A — fetal mass effect (ELS, large lesions):**
6. A large fetal mass *causes* mediastinal shift, lung compression, and (via lymphatic/venous obstruction or torsion) tension hydrothorax; 7. tension hydrothorax *leads to* impaired venous return and nonimmune hydrops fetalis (~7% of ELS), which untreated *leads to* fetal demise ([UCSF](https://fetus.ucsf.edu/pulmonary-sequestration/); [PMC8954010](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8954010/)); 8. sustained compression *can result in* pulmonary hypoplasia and neonatal respiratory distress. Conversely, involution of the lesion's blood supply *explains* the frequent spontaneous prenatal regression (~80% partial) (PMC5828905).

**Branch B — recurrent infection (mainly ILS, postnatal):**
9. Absent bronchial clearance and poor drainage *lead to* mucus stasis within the sequestration; 10. stasis plus collateral aeration *leads to* recurrent, localized, antibiotic-refractory bacterial pneumonia, abscess, and empyema (13/25 adult cases, PMC5393996); 11. chronic inflammation *results in* fibrosis, bronchiectatic cystic change, and bronchiolization of alveoli seen histologically ([AFIP](https://www.researchgate.net/publication/14064271_From_the_Archives_of_the_AFIP_Intralobar_Sequestration_Radiologic-Pathologic_Correlation)).
12. Chronic inflammation with hypervascular systemic supply *predisposes to* erosion into airways/vessels, *resulting in* hemoptysis — occasionally massive (PMID:31886079).

**Branch C — hemodynamic shunt:**
13. Systemic artery → sequestration → pulmonary/systemic vein flow constitutes a left-to-right shunt; a large shunt *results in* volume overload, high-output congestive heart failure, and pulmonary hypertension in neonates (preterm ELS with celiac-trunk supply and double shunt — [S2213576615001062](https://www.sciencedirect.com/science/article/pii/S2213576615001062); sPAP fall from 35–40 to 17 mmHg after neonatal embolization — [Children 2026](https://doi.org/10.3390/children13060842)).

**Branch D — torsion (ELS):**
14. The ELS pedicle *can* twist, *causing* hemorrhagic infarction of the mass and pleural effusion, presenting as acute chest/abdominal pain (PMC9241176; PMID:40674965).

**Branch E — neoplasia (rare, contested):**
15. The chronically inflamed, aberrantly perfused microenvironment *may rarely* harbor or support malignancy (isolated reports: squamous/adenocarcinoma, carcinoid tumorlet, even melanoma within sequestrations; only ~8 lung-cancer-in-sequestration cases reported since 1963), but "there is no strong evidence supporting the argument that pulmonary sequestration by itself carries a substantial risk of malignant transformation" ([Ann Thorac Surg comment](https://www.annalsthoracicsurgery.org/article/S0003-4975(04)01399-2/pdf); PMID:36617929).

**Candidate ontology leads (⚠ verify all):** GO:0030324 lung development; GO:0060441 epithelial tube branching involved in lung morphogenesis ⚠; GO:0009952 anterior/posterior pattern specification; GO:0007155 cell adhesion; GO:0006954 inflammatory response; GO:0001525 angiogenesis. CL:0000082 epithelial cell of lung ⚠; CL:0000057 fibroblast; CL:0002368 respiratory epithelial cell ⚠. The mechanism nodes map naturally onto a trigger (developmental misbudding/atresia) → structural lesion (systemically perfused nonfunctional lung) → consequence branches (infection, hemorrhage, shunt, mass effect) chain.

## 7. Anatomical Structures Affected

- **Primary organ:** lung (UBERON:0002048), overwhelmingly the **lower lobes** — ILS in the posterobasal segment, left > right (~60% left); ELS between left lower lobe and diaphragm in ~80%, with <10% intradiaphragmatic, infradiaphragmatic/intra-abdominal (classically left suprarenal), or intrapericardial (PMID:442005; [intrapericardial systematic review, PMC12898276](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12898276/)).
- **Vascular structures:** descending thoracic aorta (≈76%) and abdominal aorta/celiac/splenic arteries (≈19%) as feeders (PMID:21459605); inferior pulmonary vein (ILS drainage); azygos/hemiazygos/portal veins (ELS drainage). Candidate UBERON ⚠: thoracic aorta UBERON:0001515 ⚠, abdominal aorta UBERON:0001516 ⚠, pulmonary vein UBERON:0002016, azygos vein UBERON:0006615 ⚠.
- **Secondary involvement:** heart (volume overload), pleura (effusion, empyema), diaphragm (associated CDH; intradiaphragmatic lesions), mediastinum (shift from mass effect), esophagus/foregut (rare patent communications — "total visceral inflow and outflow" variants, PMID:26969317).
- **Body systems:** respiratory (primary), cardiovascular (shunt physiology), rarely gastrointestinal (foregut communication, feeding difficulty).
- **Tissue/cell level:** sequestered tissue contains disorganized airway-like structures lined by ciliated (bronchiolar-type) epithelium, dilated bronchioles/alveolar ducts, mucus-filled cysts, chronic inflammatory infiltrate and fibrosis (ILS), thick-walled muscularized systemic-type arteries; ELS may show lymphangiectasia and frequently CPAM-2-like microcystic areas ([Pathology Outlines](https://www.pathologyoutlines.com/topic/lungnontumorsequestrations.html)).
- **Subcellular:** no specific organelle pathology is described; GO cellular-component annotation is not applicable.
- **Lateralization:** unilateral in nearly all cases; left-sided predominance for both types; bilateral sequestration is reported but rare (PMID:37448606).

## 8. Temporal Development

- **Onset:** congenital by definition; the lesion forms in the first trimester (weeks 4–8). *Clinical* onset is bimodal: prenatal/neonatal (most ELS, large lesions, hydrops) versus childhood–adulthood (most ILS; >50% of the Wei & Li cases diagnosed after age 20, PMID:21459605; case reports extend to the eighth decade, PMC13251046).
- **Progression:** fetal lesions commonly plateau around 26 weeks and partially regress (~80%), with complete prenatal regression in ~18.5% of one cohort (PMC5828905; PMC10726340). Postnatally, untreated ILS tends toward recurrent infection with cumulative fibrotic/bronchiectatic damage; asymptomatic lesions can remain stable for decades.
- **Course pattern:** episodic (recurrent pneumonia, intermittent hemoptysis) on a stable structural base; not relapsing–remitting in the immunologic sense; chronic lifelong if unresected.
- **Remission:** spontaneous prenatal involution is well documented; treatment-induced "remission" is definitive after complete resection, and embolization alone achieves complete regression in a minority (7%) with partial regression in most (83%) ([pediatric embolization vs surgery review](https://www.researchgate.net/publication/24191774_Early_and_Late_Outcomes_of_Coil_Embolization_of_Pulmonary_Sequestration_in_Children)).
- **Critical periods:** mid-gestation surveillance window (hydrops can evolve rapidly; CVR monitoring); the first months of life for elective resection planning (commonly 3 months–2 years, institution-dependent — [Surgical management of CLM, PMC13542683](https://pmc.ncbi.nlm.nih.gov/articles/PMC13542683/)).

## 9. Inheritance and Population

- **Inheritance:** none — sporadic. Not AD/AR/X-linked/mitochondrial; no penetrance, expressivity, anticipation, germline mosaicism, founder effect, consanguinity signal, or carrier frequency applies. The single sibling-recurrence report (PMID:8677110) is the entire familial literature.
- **Prevalence/incidence:**
  - Birth prevalence (China, national surveillance 2010–2019): rose from 0.10 to 0.75 per 10,000 births, average **0.42/10,000** (≈1 in 24,000 births); isolated PS 0.31/10,000, non-isolated 0.11/10,000 ([BMC Pulm Med 2023, DOI:10.1186/s12890-023-02308-8](https://bmcpulmmed.biomedcentral.com/articles/10.1186/s12890-023-02308-8)). The rise is attributed to improved prenatal ultrasound detection.
  - Commonly cited Western figures: ~1 in 20,000–60,000 births; BPS comprises **0.15–6.4% of congenital pulmonary malformations** and is the second most common congenital lung lesion after CPAM ([ESR poster](https://epos.myesr.org/poster/esr/ecr2018/C-0544/background); [Lung Sequestration overview](https://www.sciencedirect.com/topics/pharmacology-toxicology-and-pharmaceutical-science/lung-sequestration)).
  - All congenital lung malformations together: ~1 in 2,500–8,000 live births (rising with prenatal detection; EUROCAT ~4/10,000).
- **Demographics:** male excess overall (1.58:1, PMID:21459605; 0.45 vs 0.38 per 10,000, BMC 2023), strongest in ELS (~3–4:1). Chinese national data show higher detected prevalence in urban than rural areas (0.51 vs 0.30/10,000) and regional variation — detection artifacts are likely. No ethnicity-specific variant geography exists (no causal variant exists).
- **Orphanet prevalence class:** ORPHA:3161 is listed among rare respiratory malformations; copy the exact epidemiology row from the ORPHA:3161 cache when curating rather than from this report.

## 10. Diagnostics

- **Prenatal:** second-trimester ultrasound shows a well-defined, homogeneously **echogenic** thoracic (or suprarenal) mass; **color Doppler demonstration of a systemic feeding artery from the aorta is the pathognomonic finding**. Fetal MRI (high, uniform T2 signal; feeder delineation) refines diagnosis and distinguishes subdiaphragmatic ELS from neuroblastoma and adrenal hemorrhage ([AJR prenatal imaging](https://ajronline.org/doi/10.2214/ajr.180.2.1800433)). For the suprarenal mass: sequestration "usually is echogenic, is left-sided, and can be identified in the second trimester," whereas neuroblastoma is "most often cystic, right-sided, and identified in the third trimester" (PMID:9166798). CVR (lesion volume ÷ head circumference) <1.6 predicts low hydrops risk (PMC10726340).
- **Postnatal imaging:** **contrast CT angiography is the current diagnostic standard** — >95% accuracy/sensitivity, replacing digital subtraction angiography; it defines the feeding artery, venous drainage, and lesion anatomy for operative planning ([clinical value of CTA, PMC3619944](https://pmc.ncbi.nlm.nih.gov/articles/PMC3619944/); [3D MDCT angiography in children](https://ajronline.org/doi/10.2214/ajr.183.1.1830183)). Chest radiograph typically shows a persistent basal opacity or recurrent same-site consolidation. MRA is an alternative without radiation. Doppler US is useful in neonates and for intra-abdominal ELS (PMC3671666).
- **Laboratory:** no specific blood test or biomarker. **Normal urinary catecholamines** (VMA/HVA) help exclude neuroblastoma for neonatal suprarenal masses ([PMC9125789](https://pmc.ncbi.nlm.nih.gov/articles/PMC9125789/)). Infection work-up (cultures, inflammatory markers) during complications.
- **Histopathology (definitive, on resection):** nonfunctional lung with dilated bronchioles/cysts, mucus stasis, chronic inflammation and fibrosis (ILS), elastic-walled systemic arteries; ELS resembles immature/normal lung with dilated airspaces ± lymphangiectasia; hybrid CPAM-2 areas in up to ~50% of ELS.
- **Genetic testing:** not indicated for isolated BPS (no gene to test). Associated-anomaly presentations (e.g., with CDH or multiple malformations) warrant standard genetics work-up (CMA ± exome) directed at the associated condition, not at the sequestration.
- **Differential diagnosis:** CPAM (no systemic feeder), congenital lobar emphysema, bronchogenic cyst, bronchial atresia with mucocele, CDH, teratoma/mediastinal mass, neuroblastoma and adrenal hemorrhage (for suprarenal ELS), necrotizing pneumonia/abscess and malignancy in adults (PMID:36741081; PMC6196208).
- **Screening:** detected through routine obstetric anomaly ultrasound; no population newborn/carrier screening applies.
- **Candidate NCIT leads ⚠:** CT Angiography NCIT:C20081 ⚠; Doppler Ultrasound ⚠; Fetal MRI ⚠ — verify every code before binding.

## 11. Outcome / Prognosis

- **Fetal:** excellent in the absence of hydrops — in the UCSF series of fetal BPS the non-hydropic fetuses did well ("Fetal pulmonary sequestration: a favorable congenital lung lesion," PMID:10511360); hydrops untreated → ~100% demise; with fetal therapy (shunt or laser), hydrops resolves in essentially all treated series and survival is high (PMID:29207383; [PMC8954010](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8954010/)).
- **Postnatal/surgical:** resection is curative with very low mortality in modern series; thoracoscopic resection carries low morbidity and short stay ([Monocentric case series, PMC11476800](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11476800/); [surgical management review, PMC13542683](https://pmc.ncbi.nlm.nih.gov/articles/PMC13542683/)). Symptomatic patients have a >2-fold higher post-operative complication risk than asymptomatic ones — an argument used for elective resection before infection ([timing database study, PMC12417296](https://pmc.ncbi.nlm.nih.gov/articles/PMC12417296/)).
- **Complications defining morbidity:** recurrent pneumonia, lung abscess, empyema, massive hemoptysis, hemothorax, high-output cardiac failure (neonates), ELS torsion/infarction, and rare malignancy-in-lesion (see §6, Branch E).
- **Prognostic factors:** fetal — hydrops, CVR ≥1.6, lesion growth trajectory, tension hydrothorax; postnatal — symptomatic status at surgery, extent of chronic suppurative damage, cardiac shunt burden. No molecular prognostic biomarker exists.
- **Life expectancy:** normal after uncomplicated resection; asymptomatic unresected adults commonly live decades undiagnosed (diagnoses into the 70s reported, PMC13251046).

## 12. Treatment

- **Surgical resection — definitive standard.** ILS: lobectomy or segmentectomy (lung-sparing segmentectomy increasingly used); ELS: sequestrectomy. **Video-assisted thoracoscopic surgery (VATS)** is now the preferred approach, with better musculoskeletal/pulmonary outcomes than thoracotomy; elective resection of asymptomatic lesions is commonly performed between ~3 months and 2 years, though observation is a defensible alternative and the asymptomatic-management question remains genuinely controversial ([PMC13542683](https://pmc.ncbi.nlm.nih.gov/articles/PMC13542683/); [can we postpone resection?](https://www.sciencedirect.com/science/article/abs/pii/S0022346811008979)). **The feeding artery must be identified and controlled first** — intraoperative hemorrhage from an unrecognized (especially infradiaphragmatic) feeder is the classic operative hazard. All symptomatic lesions warrant resection. Candidate NCIT ⚠: Surgical Procedure NCIT:C15329; Lobectomy ⚠; Thoracoscopy ⚠.
- **Endovascular embolization** (coils/vascular plugs of the feeding artery): used as (a) definitive minimally invasive therapy in selected patients — 7% complete and 83% partial regression in a pediatric comparative review, with no significant outcome difference vs surgery and fewer complications ([coil embolization outcomes](https://www.researchgate.net/publication/24191774_Early_and_Late_Outcomes_of_Coil_Embolization_of_Pulmonary_Sequestration_in_Children); [transcatheter series, PMC10378210](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10378210/)); (b) rescue therapy for neonatal high-output heart failure (sPAP 35–40→17 mmHg, [Children 2026](https://doi.org/10.3390/children13060842)); (c) preoperative adjunct to reduce bleeding (PMC12835465). Residual/recollateralized tissue and incomplete involution are its limitations.
- **Fetal therapy** (hydropic lesions): **thoracoamniotic shunting** of tension hydrothorax resolves hydrops within ~1 week in treated series; **ultrasound-guided interstitial laser ablation of the feeding artery** (median 26.9 weeks; hydrops resolution at median 7.5 days; hydrothorax at 21 days, PMID:29207383) appears to be the most effective definitive fetal option; sclerosant injection is reported. A French national cohort covers fetal therapy for congenital pulmonary malformations broadly (PMID:39138024).
- **Supportive care:** antibiotics for infective episodes (bridge to resection, never curative); bronchial-artery/feeder embolization for acute hemoptysis; drainage of empyema; cardiac failure management in neonates.
- **Pharmacotherapy/advanced therapeutics:** no disease-specific drug, gene, cell, RNA, targeted, or immunotherapy exists or is in development — the condition is structural.
- **Experimental/registries:** NCT06302985 (nebulized indocyanine green fluorescence guidance for thoracoscopic sequestration surgery, multicenter, China); NCT03044769 (Swiss congenital lung anomaly registry); NCT03913416 (3D-printed models for thoracoscopic planning); NCT04449614 (surgical management review cohort).
- **Treatment algorithm (synthesis):** prenatal diagnosis → serial US/CVR; hydrops → fetal intervention (shunt/laser); neonatal symptoms → early resection (± embolization bridge); asymptomatic → postnatal CTA, then elective VATS resection in infancy *or* structured observation (institutional equipoise); adult symptomatic → resection (± preoperative embolization); adult asymptomatic/elderly → individualized, with no strong malignancy rationale for prophylactic resection ([Ann Thorac Surg comment](https://www.annalsthoracicsurgery.org/article/S0003-4975(04)01399-2/pdf)).

## 13. Prevention

- **Primary prevention:** none possible — no modifiable cause is known. No vaccine relevance.
- **Secondary prevention:** routine second-trimester anomaly ultrasound *is* the de facto screening program; early detection enables hydrops surveillance, delivery planning at a fetal-surgery-capable center, and elective resection before infective complications.
- **Tertiary prevention:** elective resection of known lesions prevents recurrent pneumonia, hemoptysis, and (in ELS) torsion; prompt treatment of infections pending surgery; feeder embolization to pre-empt hemorrhage in high-risk anatomy.
- **Genetic counseling:** recurrence risk is essentially population-level; the single sibling-recurrence report (PMID:8677110) justifies mentioning anecdotal recurrence without quantifiable risk. No carrier testing or PGD applies.
- **Public health/environmental interventions, prophylactic medication:** not applicable.

## 14. Other Species / Natural Disease

Naturally occurring extralobar pulmonary sequestration is described in **dogs** (first canine report: a 6-month-old male mixed-breed dog with gross and histopathologic characterization, J Vet Med Sci, PMID:23569925; NCBITaxon:9615) and in **cattle** as "pulmonary choristoma/extralobar sequestration" in newborn calves, with systemic intra-mass arterial supply as a shared macroscopic hallmark (NCBITaxon:9913; [Frontiers Vet Sci case](https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2023.1257329/full)). These are sporadic case reports: **no OMIA entry** exists for pulmonary sequestration, no breed predisposition (hence no VBO term) is established, and no inherited animal form is known. Comparative pathology is concordant with the human disease — nonfunctional pulmonary tissue with its own pleura and systemic arterial supply — supporting a conserved developmental accident of foregut/lung budding rather than a species-specific process. The disease is non-transmissible; zoonotic potential is not applicable.

## 15. Model Organisms

**There is no genetic animal model of pulmonary sequestration**, consistent with the absence of a causal gene. Relevant adjacent systems:

- **Mouse developmental biology** (NCBITaxon:10090): mouse Hoxb5 expression during lung branching morphogenesis parallels the human pattern that is pathologically prolonged in BPS tissue (PMID:14632303 draws the human–mouse comparison explicitly). Hoxb5-perturbation mice model branching regulation, not sequestration itself — any KB link should be graded as mechanistic-context only, with explicit fidelity limitations.
- **Human lesion tissue (ex vivo)** is the de facto "model": Western blot/immunohistochemistry of resected BPS vs normal developing lung underpins the entire molecular literature (PMID:14632303; PMID:19411307) — evidence_source IN_VITRO on human surgical tissue.
- **Spontaneous veterinary cases** (dog, calf; §14) recapitulate the anatomy (systemic feeder, separate pleura) with high fidelity but are too rare for systematic study.
- No zebrafish, Drosophila, C. elegans, organoid, or iPSC model of sequestration exists; no IMPC/MGI phenotype line is annotated to this malformation. This is an honest model-organism gap worth recording as such (KNOWLEDGE_GAP), and lung-bud organoid systems are the plausible future platform for testing the HOXB5/adhesion hypothesis.

---

## Key citation list (for reference fetching)

| Claim area | Citation |
|---|---|
| 2,625-case Chinese series; type split; feeder origins; M:F 1.58:1 | **PMID:21459605** (Wei & Li, Eur J Cardiothorac Surg 2011;40:e39–42) |
| 540-case classic review; feeder/drainage anatomy; ELS locations | **PMID:442005** (Savic et al., Thorax 1979) |
| HOXB5 persistence in BPS/CCAM tissue | **PMID:14632303** (Volpe et al., 2003) |
| Integrin/E-cadherin dysregulation downstream of HoxB5 | **PMID:19411307** (Volpe et al., Am J Physiol Lung Cell Mol Physiol 2009;297:L143–52) |
| Familial recurrence (two siblings) | **PMID:8677110** |
| Suprarenal mass: ELS vs neuroblastoma prenatal US criteria | **PMID:9166798** |
| Fetal BPS favorable natural history | **PMID:10511360** (Lopoo et al., Obstet Gynecol 1999) |
| Laser ablation of feeding artery for hydropic BPS | **PMID:29207383** |
| Fetal therapy national cohort | **PMID:39138024** |
| Chinese national birth prevalence 0.42/10,000 | DOI:10.1186/s12890-023-02308-8 (BMC Pulm Med 2023; PMC9830928 — PMID to confirm on fetch) |
| Changsha surveillance; maternal age/education association | **PMID:39837960** |
| Adult presentation frequencies (25 cases) | PMC5393996 (J Thorac Dis 2017 — PMID to confirm on fetch) |
| Adult single-center retrospective | **PMID:36635696** |
| Bronchial atresia in 82–100% of sequestrations | Riedlinger et al., Pediatr Dev Pathol 2006;9:361–373 — **PMID to confirm on fetch** |
| Massive hemoptysis in adult | **PMID:31886079** |
| ELS torsion series/cases | PMC9241176; **PMID:40674965**; **PMID:42500556** |
| Malignancy-in-sequestration skepticism | Ann Thorac Surg 2004 comment (S0003-4975(04)01399-2); **PMID:36617929** |
| Canine ELS | **PMID:23569925** |
| CDH + ELS + CPAM co-occurrence | **PMID:35983859** |
| Esophageal communication variant | **PMID:26969317** |
| Pediatric 25-year surgical experience | **PMID:847649** |
| Imaging review | **PMID:19453525** |

**Flagged uncertainties for the curating session:** (1) Riedlinger 2006 and the BMC Pulm Med 2023 paper lack confirmed PMIDs here — fetch by title/DOI; (2) all ontology CURIEs in this report are unvalidated leads; (3) the ILS congenital-vs-acquired fork and the asymptomatic-lesion management controversy should be modeled as explicit hypothesis groups/knowledge gaps rather than settled claims; (4) quoted sentences must be re-verified verbatim against cached abstracts before use as evidence snippets.

Sources:
- [Orphanet ORPHA:3161 — Congenital pulmonary sequestration](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=3161) · [ORPHA:280811 — Extralobar](https://www.orpha.net/en/disease/detail/280811) · [GARD 4593](https://rarediseases.info.nih.gov/diseases/4593/congenital-pulmonary-sequestration) · [MeSH D001998](https://meshb.nlm.nih.gov/record/ui?ui=D001998) · [Wikidata Q688890](https://www.wikidata.org/wiki/Q688890)
- [Wei & Li 2011, 2625 cases (EJCTS)](https://academic.oup.com/ejcts/article/40/1/e39/602393) · [Savic 1979, 540 cases (PubMed)](https://pubmed.ncbi.nlm.nih.gov/442005/) · [BMC Pulm Med 2023 Chinese prevalence](https://bmcpulmmed.biomedcentral.com/articles/10.1186/s12890-023-02308-8) · [Changsha surveillance (PubMed)](https://pubmed.ncbi.nlm.nih.gov/39837960/)
- [Volpe 2003 Hoxb-5 (PubMed)](https://pubmed.ncbi.nlm.nih.gov/14632303/) · [Volpe 2009 adhesion molecules (PubMed)](https://pubmed.ncbi.nlm.nih.gov/19411307/?dopt=Abstract) · [Familial recurrence (PubMed)](https://pubmed.ncbi.nlm.nih.gov/8677110/)
- [Intralobar sequestration review (PMC2876708)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2876708/) · [Ann Thorac Surg collective review](https://www.annalsthoracicsurgery.org/article/S0003-4975(10)64417-7/pdf) · [Bronchial atresia hidden pathology](https://www.sciencedirect.com/science/article/abs/pii/S0022346805007359) · [Pathology Outlines — Sequestrations](https://www.pathologyoutlines.com/topic/lungnontumorsequestrations.html) · [AFIP radiologic–pathologic correlation](https://www.researchgate.net/publication/14064271_From_the_Archives_of_the_AFIP_Intralobar_Sequestration_Radiologic-Pathologic_Correlation)
- [Prenatal growth characteristics (PMC5828905)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5828905/) · [Antenatal diagnosis review (PMC10726340)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10726340/) · [Fetal BPS favorable lesion (PubMed)](https://pubmed.ncbi.nlm.nih.gov/10511360/) · [UCSF Fetal Treatment Center](https://fetus.ucsf.edu/pulmonary-sequestration/) · [Management options for fetal BPS (PMC8954010)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8954010/) · [FLAFA (PubMed)](https://pubmed.ncbi.nlm.nih.gov/29207383/) · [Fetal therapy national cohort (PubMed)](https://pubmed.ncbi.nlm.nih.gov/39138024/)
- [Suprarenal mass US distinction (PubMed)](https://pubmed.ncbi.nlm.nih.gov/9166798/) · [Prenatal US/MRI of sequestration (AJR)](https://ajronline.org/doi/10.2214/ajr.180.2.1800433) · [Suprarenal masses review (PMC9125789)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9125789/) · [ELS mimicking neuroblastoma (PubMed)](https://pubmed.ncbi.nlm.nih.gov/35796300/)
- [25 adult cases (PMC5393996)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5393996/) · [Adult single-center study (PubMed)](https://pubmed.ncbi.nlm.nih.gov/36635696/) · [Massive hemoptysis (PubMed)](https://pubmed.ncbi.nlm.nih.gov/31886079/) · [Monocentric case series (PMC11476800)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11476800/)
- [CTA clinical value (PMC3619944)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3619944/) · [3D MDCT angiography (AJR)](https://ajronline.org/doi/10.2214/ajr.183.1.1830183) · [Imaging in BPS (PubMed)](https://pubmed.ncbi.nlm.nih.gov/19453525/?dopt=Abstract)
- [Surgical management of CLM (PMC13542683)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13542683/) · [Can we postpone resection?](https://www.sciencedirect.com/science/article/abs/pii/S0022346811008979) · [Timing and outcomes database study (PMC12417296)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12417296/) · [Coil embolization outcomes](https://www.researchgate.net/publication/24191774_Early_and_Late_Outcomes_of_Coil_Embolization_of_Pulmonary_Sequestration_in_Children) · [Embolization with surgical contraindications (Children 2026)](https://doi.org/10.3390/children13060842) · [Transcatheter management (PMC10378210)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10378210/) · [Preoperative embolization (PMC12835465)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12835465/)
- [Preterm high-output failure case](https://www.sciencedirect.com/science/article/pii/S2213576615001062) · [Torsion series in children (PMC9241176)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9241176/) · [Elderly torsion case (PubMed)](https://pubmed.ncbi.nlm.nih.gov/40674965/) · [Malignancy comment (Ann Thorac Surg)](https://www.annalsthoracicsurgery.org/article/S0003-4975(04)01399-2/pdf) · [Scimitar + carcinoma (PubMed)](https://pubmed.ncbi.nlm.nih.gov/36617929/) · [Esophageal communication (PubMed)](https://pubmed.ncbi.nlm.nih.gov/26969317/)
- [Canine ELS (PubMed)](https://pubmed.ncbi.nlm.nih.gov/23569925/) · [Bovine case (Frontiers Vet Sci)](https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2023.1257329/full)
- [NCT06302985](https://clinicaltrials.gov/study/NCT06302985) · [NCT03044769](https://clinicaltrials.gov/study/NCT03044769) · [NCT03913416](https://clinicaltrials.gov/study/NCT03913416) · [NCT04449614](https://clinicaltrials.gov/study/NCT04449614)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 47 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 4 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 47 |
| On topic | 30 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:14632303` *(abstract only)*: "In BPS and CCAM tissue, Hoxb-5 is maintained in a manner typical of an earlier developmental stage and is associated with development of abnormal lung tissue"
  - closest text in source: "This notion is supported by results from BPS and CCAM tissue, in which Hoxb-5 is maintained in a manner typical of an earlier developmental stage and is associated with development of abnormal lung tissue."

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0002048` (1 mention) - the report calls it "Primary organ:** lung"; UBERON calls it **lung**
- `NCBITaxon:10090` (1 mention) - the report calls it "Mouse developmental biology"; NCBITaxon calls it **Mus musculus**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.