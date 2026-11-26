---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-26T03:55:05.445389'
end_time: '2026-11-26T03:57:54.725583'
duration_seconds: 169.28
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Tuberculous Empyema
  mondo_id: MONDO:0005999
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: tuberculous empyema (& pleural)
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
  web_search_requests: 19
  num_turns: 24
  total_cost_usd: 0.9177402000000001
  session_id: 8654f53f-e924-4f35-a78c-d226160a2832
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  tool_calls: 23
  retrieval_calls: 20
  assistant_text_blocks: 2
citation_count: 32
reference_validation:
  total_references: 27
  verified: 26
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.037
  quotes_checked: 0
  quotes_valid: 0
  quotes_not_checkable: 2
  relevance_assessed: 26
  on_topic: 10
  unresolved_references:
  - DOI:10.1055/s-2001-18800
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 29
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 0
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0005999
    reported_labels:
    - MONDO
    ontology_label: tuberculous empyema
  - term_id: HP:0045050
    reported_labels:
    - to be checked
    ontology_label: Increased DLCO
  - term_id: GO:0001774
    reported_labels:
    - activation of microglia; not applicable
    ontology_label: microglial cell activation
  - term_id: UBERON:0002048
    reported_labels:
    - Secondary sites:** lung
    ontology_label: lung
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Tuberculous Empyema
- **MONDO ID:** MONDO:0005999 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** tuberculous empyema (& pleural)
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Tuberculous Empyema** covering all of the
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

Bash network is unavailable; switching to web search.

I've finished the literature searches and am now writing the report.

# Tuberculous Empyema: Disease Characteristics Report

**Scope and limits.** This report is about tuberculous empyema, using the identifier given (MONDO:0005999). It is an infectious disease caused by *Mycobacterium tuberculosis*. **It has no causal human gene**, which matches "Causal gene(s): not recorded" in the template. Shell access to PubMed's E-utilities was blocked in this session, so all sources came from web search. PMIDs are given only where a retrieved source showed them. Where a source was found without a PMID, I give its PMC ID or DOI instead. I could not open the MONDO record to check that the ID matches this label.

---

## 1. Disease Information

**Overview.** Tuberculous empyema is "a rare form of tuberculous pleuritis. It consists of a purulent infection of the pleural cavity with detectable bacilli in pleural fluid" (Semin Respir Crit Care Med 2001, DOI 10.1055/s-2001-18800, https://www.thieme-connect.de/products/ejournals/abstract/10.1055/s-2001-18800).

Sahn & Iseman (Semin Respir Infect 1999, **PMID 10197400**) separate it from the much more common tuberculous pleural effusion. The effusion results from "an exaggerated inflammatory response to a localized paucibacillary pleural infection". Empyema, by contrast, is a chronic, active pleural infection that "can persist for years with few symptoms". Their summary of treatment: "treatment consists of pleural space drainage and antituberculous chemotherapy".

**Identifiers**

| Resource | Identifier | Status |
|---|---|---|
| MONDO | MONDO:0005999 | As provided; not checked this session |
| MeSH | **D004654** "Empyema, Tuberculous", defined as empyema due to *M. tuberculosis*; tree numbers C01.748…, C08.528.928.405 | Retrieved (https://meshb.nlm.nih.gov/record/ui?ui=D004654) |
| ICD-10 | Tuberculous pleurisy codes A15.6 (confirmed) / A16.5 (not confirmed) | From general knowledge, not retrieved; check before use |
| ICD-11, Orphanet, OMIM | Not retrieved | OMIM is not applicable (not a Mendelian disease) |

**Synonyms:** tuberculous pleural empyema; TB empyema; tuberculous pyothorax; chronic tuberculous empyema (CTE). *Empyema necessitatis / necessitans* is the variant in which pus breaks out through the chest wall.

**Source of information:** aggregated disease-level resources and case series. There is no EHR or registry resource specific to this disease.

## 2. Etiology

- **Cause:** infection of the pleural space by *M. tuberculosis* complex. A large bacillary load and pus formation separate empyema from the paucibacillary, hypersensitivity-driven effusion (PMID 10197400; McNally, Ross & Gleeson, *Breathe* 2023;19:230143, PMC10729826).
- **Routes of entry:**
  - Rupture of a subpleural caseous focus or cavity into the pleura (Vorster et al., J Thorac Dis 2015, PMC4466424).
  - Bronchopleural fistula (BPF). In a surgical series of chronic TB empyema, BPF was present in 46 patients (65.7%) (PMC7870130).
  - Historically, artificial pneumothorax or collapse therapy used to treat TB (see the lymphoma discussion in §11).
- **Risk factors (human clinical data):**
  - Advanced pulmonary TB. In a Korean series, "tuberculous empyema is frequently accompanied by advanced pulmonary lesions" (Tuberc Respir Dis, https://synapse.koreamed.org/articles/1000947).
  - Younger age in endemic settings. In an Indian cohort of 75 empyema patients, the mean age was 32.7 years for TB empyema versus 46.5 years for other causes (Kundu et al., Lung India 2010;27:196–201, PMC2988167).
  - HIV and low CD4 counts are linked to higher bacillary yield in the pleura (PMC4466424).
  - Drug-resistant TB. Multidrug-resistant strains were found in 7 of 18 cultures (Bai et al., Respirology 1998;3:261–6, **PMID 10201053**).
- **Genetic risk and protective factors:** none specific to TB empyema were found. Host-genetic TB susceptibility (for example Mendelian susceptibility to mycobacterial disease, MSMD) is a general TB topic and was not retrieved for this entry. Mouse strain-dependent differences in BCG pleurisy suggest a role for host genetics (Inflamm Res 2000, https://link.springer.com/doi/10.1007/s000110050581).
- **Protective factors:** prompt diagnosis and full treatment of pulmonary and pleural TB, and TB control programs (see §13). No genetic protective variants were found.
- **Gene–environment interactions:** no data found.

## 3. Phenotypes

Per-symptom frequencies specific to TB empyema were not available. The figures below come from the cited series.

| Phenotype | Suggested HPO term | Notes |
|---|---|---|
| Pleural effusion / empyema (pus) | HP:0002202 Pleural effusion; empyema (term to be checked) | Defining feature. Typically unilateral and loculated. |
| Pleural thickening / fibrous rind | HP:0045050 (to be checked) | "Chronic fibrous pleural rind… is a unique feature of stage III tuberculous empyema" (PMC5946583) |
| Pleural calcification | Pleural calcification (HPO term to be checked) | Present in chronic disease (radiology case reports; Radiopaedia) |
| Fever, weight loss, cough, chest pain, dyspnea | HP:0001945, HP:0001824, HP:0012735, HP:0100749, HP:0002094 | Course is chronic and can be nearly symptomless for years (PMID 10197400) |
| Bronchopleural fistula | Bronchopleural fistula (term to be checked) | 65.7% in a surgical series (PMC7870130). More common in TB empyema than in other empyema (PMC2988167) |
| Chest-wall abscess / empyema necessitatis | — | Case series in immunocompetent and immunocompromised patients (https://doaj.org/article/8b808110bab84b8785905ba5685e3d6b; PMID 38601432) |
| Restrictive ventilatory defect / trapped lung | HP:0002091 | A main indication for decortication (PMC7870130) |
| Neutrophil-predominant exudate | Laboratory finding | "Polymorphonuclear leukocytes are predominant in the pleural fluid" in TB empyema (synapse.koreamed.org/articles/1000947) |

- **Onset:** adult, with a younger peak in endemic regions.
- **Course:** chronic and progressive.
- **Severity:** moderate to severe.
- **Quality of life:** no EQ-5D or SF-36 data were found.

## 4. Genetic / Molecular Information

- **Causal genes, pathogenic variants, ClinVar entries, chromosomal abnormalities:** not applicable to the human host.
- **Pathogen genetics that matter clinically:** drug-resistance mutations, shown by rifampicin resistance on Xpert MTB/RIF and by MDR strains (PMID 10201053). The specific genes involved were not retrieved this session.
- **Resistance acquired inside the empyema cavity:** low drug levels in the pleural fluid can select for resistance (Elliott et al., Tuber Lung Dis 1995;76:463–7; PMID not retrieved).
- **Epigenetics and modifier genes:** no data found.

## 5. Environmental Information

- **Infectious agent:** *Mycobacterium tuberculosis* complex, NCBI Taxon 1773. The taxon ID is from general knowledge and was not retrieved this session.
- **Environmental and lifestyle factors:** the general TB determinants (crowding, HIV, poor access to care) apply. No exposures specific to TB empyema were retrieved.
- **Iatrogenic factors (historical):** artificial pneumothorax therapy led to chronic pyothorax and, later, pyothorax-associated lymphoma (PMID 16330929).

## 6. Mechanism / Pathophysiology

**Causal chain**

1. *M. tuberculosis* infects the lung, then a subpleural caseous focus or cavity ruptures into the pleural space (PMC4466424). In other cases, a bronchopleural fistula or past collapse therapy introduces bacilli **→ leads to** heavy bacillary seeding of the pleura.
2. **Branch A (common, paucibacillary):** Th1 delayed-type hypersensitivity **→ results in** a lymphocytic exudative effusion (tuberculous pleurisy). The response is driven by IFN-γ and IL-12, which are higher in pleural fluid than in blood, with Th17 and regulatory T cells also present in the pleural space (PMC6935897, PMC4466424, PMC10331301). This is demonstrated in human samples and in animal models.
   **Branch B (empyema):** a high bacillary load with caseous necrosis **→ leads to** a purulent, neutrophil-rich collection with visible bacilli (DOI 10.1055/s-2001-18800; synapse 1000947). The step from pleurisy to empyema is inferred from clinical series; its mechanism has not been shown experimentally.
3. Chronic inflammation and fibrin deposition **→ result in** loculations and a thick fibrous visceral and parietal rind, which later calcifies (PMC5946583).
4. The rind **→ leads to** a trapped lung, failure to re-expand, and a restrictive defect. It also **→ leads to** poor drug penetration: pleural-fluid Cmax as a fraction of serum Cmax was 4% for rifampicin, 34% for streptomycin and 48% for ofloxacin (Elliott 1995; cited in PMID 26265445).
5. Low drug concentrations in the cavity **→ lead to** persistent infection and **acquired drug resistance**. This is shown in case reports with pharmacokinetic data (Elliott 1995; PMID 26265445).
6. Erosion into the bronchus or chest wall **→ results in** a bronchopleural fistula or empyema necessitatis. Decades of chronic inflammation, together with EBV, **→ can result in** pyothorax-associated B-cell lymphoma (PMID 16330929; PMID 33564306).

**Suggested ontology terms**

- **GO:** GO:0006954 inflammatory response; GO:0001774 (activation of microglia; not applicable); GO:0002456 T cell mediated immunity; GO:0032609 type II interferon production; GO:0042110 T cell activation; GO:0070266 necroptotic process (to be checked); GO:0061448 connective tissue development / fibrosis (to be checked).
- **CL:** CL:0000775 neutrophil; CL:0000235 macrophage; CL:0000624 CD4-positive αβ T cell; CL:0000899 T-helper 17 cell; CL:0000815 regulatory T cell; CL:0000077 mesothelial cell; CL:0000057 fibroblast.
- **Molecular profiling:** single-cell profiling of tuberculous pleural effusion shows CD4 T cells biased toward Th1 and Th17 (PMC10331301). No omics data specific to empyema were found.

## 7. Anatomical Structures Affected

- **Primary site:** the pleural cavity and pleura (UBERON:0002402 pleural cavity, UBERON:0000977 pleura), both visceral (UBERON:0002401) and parietal (UBERON:0002400) layers.
- **Secondary sites:** lung (UBERON:0002048), bronchi (bronchopleural fistula), and chest wall (UBERON:0016435) in empyema necessitatis.
- **Body system:** respiratory.
- **Lateralization:** typically unilateral.
- **Tissue and cells:** mesothelium and fibrous connective tissue; neutrophils, macrophages and T cells (CL terms in §6).
- **Subcellular level:** bacilli survive within macrophage phagosomes (general TB biology; not retrieved for this entry).

## 8. Temporal Development

- **Onset:** subacute to chronic.
- **Duration:** illness and drainage last longer than in other empyema. Mean chest-tube drainage was 48.7 days versus 23.2 days (PMC2988167).
- **Stages:** the stage III (chronic, fibrous-rind) category comes from surgical literature (PMC5946583). The disease can be silent for years (PMID 10197400).
- **Critical window:** early antituberculous treatment and drainage, before the rind becomes fibrotic and calcified. Late referral causes pleural thickening and lung injury (PAFMJ, DOI 10.51253/PAFMJ.V70I6.3724). The duration of symptoms and of preoperative chemotherapy were associated with the CT low-density line (PMC5946583).

## 9. Inheritance and Population

- **Inheritance:** not applicable (an acquired infection).
- **Burden of TB overall:** the WHO Global TB Report 2025 estimates that about 10.7 million people fell ill with TB in 2024, with more than 1.2 million deaths (https://www.who.int/news/item/12-11-2025-global-gains-in-tuberculosis-response-endangered-by-funding-challenges).
- **Frequency of TB empyema:**
  - It is rare compared with TB effusion (PMID 10197400).
  - In endemic India it is a major cause of empyema: 29 of 75 adult empyemas (38.7%) were tuberculous (PMC2988167).
  - No population-based incidence of TB empyema was found.
- **Geography:** high-burden countries in Asia and Africa. Pyothorax-associated lymphoma is reported mainly from Japan (PMID 16330929).

## 10. Diagnostics

- **Pleural fluid analysis:**
  - Purulent exudate, often neutrophil-predominant (synapse 1000947).
  - AFB smear is positive in fewer than 10% of cases of TB pleurisy, "except for HIV-infected patients and tuberculous empyema" (koreascience JAKO201421762413590).
  - In TB pleurisy, neutrophil-predominant fluid gave a higher culture yield (50% vs 10%) (same source).
- **Microbiology:**
  - Culture remains the reference standard. Yield in TB pleurisy is about 30–44% (PMC8278995).
  - Pleural fluid Xpert MTB/RIF has a pooled sensitivity of 51.4% and specificity of 98.6% against culture (meta-analysis cited in PMC8278995).
  - Yields in empyema are likely higher, but no retrieved study quantifies this.
- **Biomarkers:** adenosine deaminase (ADA) is widely used, with reported sensitivity of 47–100% (PMC8278995). Pleural fluid IFN-γ is another option.
- **Imaging:**
  - CT shows the split-pleura sign (Radiopaedia), a thick and often calcified rind, and loculation.
  - A low-density line between the parietal rind and the chest wall was seen in 44 of 80 stage III patients (PMC5946583).
- **Biopsy:** pleural biopsy with histology (caseating granulomas) and culture is more sensitive than fluid testing (PMC8203050).
- **Genetic testing:** not applicable for the host. Testing of the pathogen for resistance (Xpert rifampicin resistance, phenotypic drug-susceptibility testing) is essential.
- **Differential diagnosis:**
  - Bacterial parapneumonic empyema, which is often *S. aureus* or Gram-negative (PMC2988167).
  - Malignant effusion (nodular pleural thickening).
  - Hemothorax / fibrothorax.
  - Pyothorax-associated lymphoma.
  - Nontuberculous mycobacterial or fungal empyema.

## 11. Outcome / Prognosis

- **Compared with other empyema:**
  - TB empyema has "a significantly poorer outcome" than nontuberculous empyema (PMC2988167).
  - It has worse lung expansion, more need for decortication, and longer hospital stays (Nigerian series; scielo jbpneu).
  - Outcomes are worse than for pulmonary TB, though "modern multidrug chemotherapy with repeated drainage and opportune surgical interventions" can succeed (PMID 10201053).
- **Surgical outcomes:**
  - VATS decortication (n=274): 9.9% complications, 44.1% in chronic versus 4.8% in acute cases, and 2.3% late recurrence (Ann Thorac Cardiovasc Surg 2015, DOI 10.5761/atcs.oa.14-00185).
  - Open decortication (n=128): 1.56% mortality and 7% morbidity (DOI 10.51253/PAFMJ.V70I6.3724).
- **Complications:**
  - Bronchopleural fistula, empyema necessitatis, trapped lung and fibrothorax.
  - Acquired drug resistance.
  - Pyothorax-associated lymphoma, a B-cell non-Hodgkin lymphoma that arises after more than 20 years of pyothorax and is strongly associated with EBV (PMID 16330929; PMID 33564306; PMID 25705606).
- **Prognostic factors:** chronicity, bronchopleural fistula, drug resistance, and late referral.
- **Quality-of-life data:** none found.

## 12. Treatment

- **Drugs:**
  - Standard antituberculous therapy: isoniazid, rifampicin, pyrazinamide and ethambutol. NCIT intervention terms were not retrieved and should be looked up for each drug.
  - Isoniazid, pyrazinamide and ethambutol reach better pleural-fluid levels relative to serum than rifampicin does (PMID 26265445).
  - Therapeutic drug monitoring (TDM) with high-end dosing achieved "sustained closure of the BPF and mycobacteriologic cure" without surgery in an 84-year-old patient (PMID 26265445).
  - Drug-resistant TB needs regimens guided by susceptibility testing (PMID 10201053).
  - Intrapleural drug administration has been reported in case reports (British Library record 100179095466).
- **Drainage and surgery:**
  - Tube thoracostomy, often repeated.
  - VATS or open decortication.
  - Open-window thoracostomy with muscle flap and negative-pressure wound therapy for fistulas (PMC12306518).
  - Thoracoplasty for the most difficult cases (historical).
- **Timing of surgery:**
  - More than 6 weeks of antituberculous treatment before decortication was linked to better outcomes (Cureus, PMC7870130).
  - Reported pre-operative treatment ranges from 2 weeks to 12 months (same source).
  - Surgery should be done by experienced thoracic surgeons (PMID 10197400).
- **Pharmacogenomics:** NAT2 acetylator status affects isoniazid exposure. This is general TB knowledge, not retrieved for this entry.
- **Advanced or experimental therapies:** none. No NCT trials specific to TB empyema were found.
- **Rehabilitation:** chest physiotherapy after decortication. No specific data were found.

## 13. Prevention

- **Primary:** TB control, including case finding, treatment of latent TB infection, BCG vaccination in endemic countries, and HIV control (WHO, general).
- **Secondary:** early diagnosis and full treatment of pulmonary TB and tuberculous pleurisy, with early drainage of complicated collections.
- **Tertiary:**
  - Adequate drug levels (TDM) to prevent acquired resistance (PMID 26265445).
  - Timely decortication.
  - Long-term surveillance of chronic pyothorax for lymphoma (PMID 16330929).
- **Genetic counseling:** not applicable.

## 14. Other Species

- No naturally occurring "tuberculous empyema" entry was found in animals, and OMIA is not applicable.
- *M. tuberculosis* complex organisms such as *M. bovis* cause tuberculous pleuritis and serositis in cattle and other species, and *M. bovis* is zoonotic. These points were not retrieved this session.

## 15. Model Organisms

- **Guinea pig (*Cavia porcellus*):**
  - BCG-vaccinated animals given intrapleural heat-killed *M. tuberculosis* developed 5–10 mL effusions by days 6–7, with granulomatous pleuritis and antigen-driven lymphocyte proliferation (Infect Immun 1993, PMC302698).
  - The model has been used to study TGF-β and TNF-α (PMC356004, PMC2744482, PMC166002).
  - **What it reproduces:** the hypersensitivity effusion (Branch A), not purulent empyema.
- **Mouse:**
  - Intrapleural live *M. bovis* BCG produces a biphasic pleurisy: neutrophils peak at about 24 hours and a second wave of cells arrives around day 15.
  - Eosinophil responses differ between susceptible and resistant strains (Inflamm Res 2000; SciELO Mem Inst Oswaldo Cruz review).
- **Rabbit:** older studies of intrapleural BCG (JCI, https://www.jci.org/articles/view/112131).
- **Limitations:** no model was found that reproduces chronic, bacillus-rich empyema with rind formation, poor drug penetration or bronchopleural fistula.

---

### Main gaps

- PMIDs could not be retrieved for Elliott 1995, Kundu 2010 and the Thieme 2001 review. PMC IDs or DOIs are given instead.
- There is no population-based incidence of TB empyema.
- Symptom frequencies and quality-of-life data specific to TB empyema are missing.
- ICD-10/11 and Orphanet codes were not checked.
- There is no host-genetic data.
- HPO, GO, CL and UBERON IDs should be checked against the ontologies before they go into the knowledge base.

### Sources

- [Sahn & Iseman 1999, PMID 10197400 (via AuntMinnie)](https://www.auntminnie.com/15561137)
- [Bai 1998, PMID 10201053](https://www.curehunter.com/public/pubmed10201053.do)
- [Thieme 2001 review](https://www.thieme-connect.de/products/ejournals/abstract/10.1055/s-2001-18800?lang=en)
- [McNally et al., Breathe 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10729826)
- [Vorster et al., J Thorac Dis 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4466424)
- [Kundu et al., Lung India 2010](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2988167/)
- [Long et al., BMC Infect Dis 2015, PMID 26265445](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4542105/)
- [Elliott et al. 1995 record](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_77714595)
- [Cureus, ATT before decortication](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7870130/)
- [VATS decortication series, ATCS 2015](https://www.jstage.jst.go.jp/article/atcs/21/3/21_oa.14-00185/_article)
- [Open decortication series, PAFMJ](https://doi.org/10.51253/PAFMJ.V70I6.3724)
- [Nigerian comparison, J Bras Pneumol](https://scielo.br/j/jbpneu/a/L4sFFyKCskcPp57xjvp6HDr/?lang=en)
- [Stage III CT study](https://pmc.ncbi.nlm.nih.gov/articles/PMC5946583/)
- [Split pleura sign, Radiopaedia](https://radiopaedia.org/articles/split-pleura-sign-empyema)
- [Korean TB empyema series](https://synapse.koreamed.org/articles/1000947)
- [Korean TB pleurisy study](https://koreascience.kr/article/JAKO201421762413590.pdf)
- [The perplexing pleura (diagnostics review)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8278995/)
- [Xpert on pleural biopsy](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8203050/)
- [MeSH D004654](https://meshb.nlm.nih.gov/record/ui?ui=D004654)
- [WHO Global TB Report 2025](https://www.who.int/news/item/12-11-2025-global-gains-in-tuberculosis-response-endangered-by-funding-challenges)
- [Pyothorax-associated lymphoma, PMID 16330929](https://pubmed.ncbi.nlm.nih.gov/16330929/)
- [Pyothorax-associated lymphoma without artificial pneumothorax, Chen 2021](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7850845/)
- [Pleural Th1/Th17 immunology](https://pmc.ncbi.nlm.nih.gov/articles/PMC6935897)
- [Single-cell profiling of TB pleural effusion](https://pmc.ncbi.nlm.nih.gov/articles/PMC10331301)
- [Guinea pig pleuritis model](https://pmc.ncbi.nlm.nih.gov/articles/PMC302698)
- [Mouse BCG pleurisy, Inflamm Res 2000](https://link.springer.com/doi/10.1007/s000110050581)
- [Mycobacterial pleurisy models review, SciELO](https://www.scielo.br/j/mioc/a/Jq3HZ8cpf5gDJq968PK3qGG/?lang=en)
- [Empyema necessitans case series](https://doaj.org/article/8b808110bab84b8785905ba5685e3d6b)
- [Empyema necessitans case report, PMID 38601432](https://pubmed.ncbi.nlm.nih.gov/38601432/)
- [Open-window thoracostomy with NPWT for BPF](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12306518/)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 0 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 0 |
| Quoted claims with nothing to check against | 2 |
| References weighed for topical relevance | 26 |
| On topic | 10 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1055/s-2001-18800` (2 mentions) - Identifier did not resolve to a record

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1055/s-2001-18800`: "a rare form of tuberculous pleuritis. It consists of a purulent infection of the pleural cavity with detectable bacilli in pleural fluid"
  - Reference did not resolve, so the quote could not be checked
- `PMC:PMC5946583`: "Chronic fibrous pleural rind… is a unique feature of stage III tuberculous empyema"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 5 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005999` (2 mentions) - the report calls it "MONDO"; MONDO calls it **tuberculous empyema**
- `HP:0045050` (1 mention) - the report calls it "to be checked"; HP calls it **Increased DLCO**
- `GO:0001774` (1 mention) - the report calls it "activation of microglia; not applicable"; GO calls it **microglial cell activation**
- `UBERON:0002048` (1 mention) - the report calls it "Secondary sites:** lung"; UBERON calls it **lung**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002091` (1 mention) - the report calls it "Restrictive ventilatory defect / trapped lung"; HP calls it **Restrictive ventilatory defect**