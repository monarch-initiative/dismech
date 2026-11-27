---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-26T03:48:46.463651'
end_time: '2026-11-26T03:51:31.411310'
duration_seconds: 164.95
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Fournier Gangrene
  mondo_id: MONDO:0043352
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: fournier's gangrene
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
  web_search_requests: 16
  num_turns: 20
  total_cost_usd: 0.9310122999999999
  session_id: b737b236-0c42-4c47-89ff-5dc8d65e5261
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 19
  retrieval_calls: 17
  assistant_text_blocks: 1
citation_count: 51
reference_validation:
  total_references: 31
  verified: 31
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 2
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC7368210
  relevance_assessed: 31
  on_topic: 8
  off_topic: 1
  off_topic_references:
  - PMC:PMC8024095
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 36
  verified: 29
  not_found: 0
  obsolete: 1
  unverifiable: 6
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 3
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0043352
    reported_labels:
    - MONDO
    ontology_label: fournier gangrene
  - term_id: GO:0030574
    reported_labels:
    - bacterial
    ontology_label: collagen catabolic process
  labels_variant: 2
  obsolete_terms:
  - term_id: GO:0070265
    ontology_label: obsolete necrotic cell death
  service_unreachable: 6
  obsolescence_unchecked: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Fournier Gangrene
- **MONDO ID:** MONDO:0043352 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** fournier's gangrene
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Fournier Gangrene** covering all of the
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

# Fournier Gangrene (MONDO:0043352): Disease Characteristics Report

**How this report was scoped:** Fournier gangrene (FG) is an acquired infection. It has no causal gene and no OMIM entry, so the gene and inheritance sections say "not applicable" and do not name a gene. PubMed's API could not be queried directly in this session, so all evidence comes from web searches of PubMed, PMC, MeSH, FDA and journal pages. Some PMIDs were confirmed only through search snippets and are flagged where that is the case. Quotes are taken from the abstract or snippet text the searches returned.

---

## 1. Disease Information

**Overview.**
- FG is a necrotizing fasciitis of the perineum, the external genitalia and the area around the anus.
- MeSH defines it as "an acute necrotic infection of the scrotum, penis, or perineum… characterized by scrotum pain and redness with rapid progression to gangrene and sloughing of tissue" ([MeSH D018934](https://meshb.nlm.nih.gov/record/ui?ui=D018934)).
- A 2015 review describes it as "an obliterative endarteritis of the subcutaneous arteries resulting in gangrene of the overlying skin" ([PMC4580094](https://pmc.ncbi.nlm.nih.gov/articles/4580094)).
- Jean-Alfred Fournier first described it in 1883 as a sudden, fulminant scrotal gangrene in previously healthy young men, with no identifiable cause ([PMC4359426](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4359426/)).
- Today a source of infection is found in most cases (colorectal, urogenital or skin).

**Causal gene:** none. This is an infectious, acquired disease.

**Identifiers**

| System | ID | Source |
|---|---|---|
| MONDO | MONDO:0043352 | [Pharos](https://pharos.nih.gov/diseases/fournier%20gangrene) |
| MeSH | D018934 (tree numbers C01.150.252.377; C12.100.500.229; C12.200.294.229) | [MeSH](https://meshb.nlm.nih.gov/record/ui?ui=D018934) |
| ICD-10-CM | N49.3 | [AAPC](https://www.aapc.com/codes/icd-10-codes/N49.3) |
| ICD-10-GM (German modification) | N49.80 | [gesund.bund.de](https://gesund.bund.de/en/icd-code-search/n49-80) |
| GARD | 0010912 | [Pharos](https://pharos.nih.gov/diseases/fournier%20gangrene) |
| MedGen | 65967 | [MedGen](https://https.ncbi.nlm.nih.gov/medgen/65967) |
| OMIM | not applicable | — |
| Orphanet | not found in searches | — |
| ICD-11 | not retrieved | — |

**Synonyms:** Fournier's gangrene; necrotizing fasciitis of the perineum/genitalia; synergistic gangrene of the scrotum. Only the first was confirmed in retrieved sources.

**Evidence base:** The disease-level data are aggregated mainly from:
- single-centre retrospective case series;
- administrative and claims databases, such as the US Nationwide Inpatient Sample ([PMID 19286224](https://pubmed.ncbi.nlm.nih.gov/19286224/)) and Medicare-based NIDDK claims analyses ([NIDDK UDA 2025](https://www.niddk.nih.gov/-/media/Files/Strategic-Plans/urologic/2025/UDA-ADR-FG-2025_508.pdf));
- pharmacovigilance (FAERS) reports.

---

## 2. Etiology

**Causal factors (infectious).**
- FG is a synergistic infection by aerobic and anaerobic bacteria. It is polymicrobial in more than 80% of cases, with *E. coli*, *Klebsiella pneumoniae*, *Bacteroides fragilis* and *Staphylococcus aureus* as common pathogens ([PMC9355918](https://pmc.ncbi.nlm.nih.gov/articles/PMC9355918); [PMC5798415](https://pmc.ncbi.nlm.nih.gov/articles/PMC5798415)).
- Typical portals of entry:
  - lower urinary tract, about 40% (urethral stricture, indwelling catheters);
  - colorectal or anorectal, about 30% (fistulas, perirectal abscess, hemorrhoids);
  - skin of the penis or scrotum, about 30% ([5-Minute Emergency Consult](https://emergency.unboundmedicine.com/view/5-Minute_Emergency_Consult/307215/all/Fournier_Gangrene)).
- In infants, reported triggers include omphalitis, strangulated hernia, prematurity, diaper rash, varicella, circumcision and perineal abscess ([tp.amegroups](https://tp.amegroups.org/article/view/141046/html)).

**Risk factors (environmental and clinical).**
- **Diabetes mellitus:** present in 20–70% of cases, and the most common comorbidity ([PMC10184784](https://pmc.ncbi.nlm.nih.gov/articles/PMC10184784)).
- **Other conditions:** alcohol use disorder, obesity, immunosuppression, HIV, renal failure and heart disease ([PMID 16927060](https://pubmed.ncbi.nlm.nih.gov/16927060/); [PMID 38625013](https://www.pubmed.gov/38625013/)).
- **Age and sex:**
  - Incidence peaks in men aged 50–79, at 3.3/100,000 ([PMID 19286224](https://pubmed.ncbi.nlm.nih.gov/19286224/)).
  - Men are affected far more often (1,641 men versus 39 women in the same cohort).
- **SGLT2 inhibitors (drug exposure):**
  - In August 2018 the FDA required a class-wide warning, after 12 cases that all needed hospitalization and surgery ([FDA](https://www.fda.gov/Drugs/DrugSafety/ucm617360.htm)).
  - Bersoff-Matcha et al. (*Ann Intern Med* 2019; PMID 31060053, PMID not directly verified) reported 55 cases up to January 2019, with onset 5 days to 49 months after starting the drug ([PubMed 31060053](https://pubmed.ncbi.nlm.nih.gov/31060053/)).
  - A FAERS analysis concluded that FG "may be a class effect of SGLT2 inhibitors" ([PMC7368210](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7368210/)).

**Genetic risk factors:** none identified. No GWAS, ClinVar or ClinGen associations were found.

**Protective factors:** No genetic protective factors are known. Plausible environmental protective measures were not supported by direct primary data in the retrieved literature:
- good glycemic control;
- perineal hygiene;
- prompt treatment of perianal and urethral disease.

**Gene–environment interactions:** none described.

---

## 3. Phenotypes

Frequencies are qualitative unless a source gives a number. HPO IDs are suggestions and should be checked against the HPO release.

| Phenotype | Type | HPO (suggested) | Notes |
|---|---|---|---|
| Scrotal or perineal pain, often out of proportion to visible findings | Symptom | Pelvic pain HP:0034267; scrotal pain (term to be confirmed) | Characteristic early sign (MeSH definition) |
| Erythema, edema, induration of scrotum or perineum | Sign | Erythema HP:0010783; Edema HP:0000969 | Nearly universal |
| Crepitus or subcutaneous gas | Sign / imaging | Subcutaneous emphysema HP:0100756 | "Hallmark" but not always present ([PMID 18349455](https://pubmed.ncbi.nlm.nih.gov/18349455/)) |
| Necrosis or gangrene of skin, foul discharge | Sign | Skin ulcer HP:0200042; Gangrene HP:0100758 | Late feature |
| Fever, tachycardia, sepsis or septic shock | Sign | Fever HP:0001945; Sepsis HP:0100806 | Sepsis predicts mortality ([PMID 38625013](https://www.pubmed.gov/38625013/)) |
| Leukocytosis, high CRP, hyponatremia, hyperglycemia, raised creatinine, low bicarbonate, anemia | Laboratory | Leukocytosis HP:0001974; Hyponatremia HP:0002902; Elevated CRP HP:0011227; Hyperglycemia HP:0003074; Elevated serum creatinine HP:0003259 | Components of the LRINEC and FGSI scores |
| Spread to the anterior abdominal wall | Sign | — | Spreads through Scarpa fascia ([PMC4580094](https://pmc.ncbi.nlm.nih.gov/articles/4580094)) |

**Onset and course:** onset is usually in adulthood (most often 50–79 years), with rare cases in neonates and infants. Disease is acute and progresses rapidly, over hours to days.

**Quality-of-life impact** (after the acute illness):
- 65% of survivors in a German cohort reported worse sexual function ([PMID 24034257](https://www.ncbi.nlm.nih.gov/pubmed/24034257), attribution inferred).
- A multi-institutional study (Langston 2023) found significant drops in general and sexual functional domains ([Can J Urol PDF](https://www.canjurol.com/html/subscriber/Spdf/V30I02/CJU_V30_I2_11_DrLangston.pdf)).
- A 2026 systematic review reported fecal incontinence, sexual dysfunction, urinary symptoms and psychosocial impairment ([search result](https://boris-portal.unibe.ch/entities/publication/344e455b-a5ea-43a4-b4fa-3bd08579d60c)).

---

## 4. Genetic / Molecular Information

These items are **not applicable**:
- causal genes;
- pathogenic variants (ACMG classification, allele frequencies, somatic versus germline origin);
- modifier genes;
- epigenetic changes;
- chromosomal abnormalities.

No human genetic association was found. Bacterial virulence factors (collagenase, heparinase) are covered in Section 6.

---

## 5. Environmental Information

- **Infectious agents** (NCBI Taxonomy IDs are given from standard taxonomy and should be verified):
  - *Escherichia coli* (562): 46.6% ([PMID 25635243](https://pubmed.ncbi.nlm.nih.gov/25635243/)) and 72% ([PMID 28257985](https://pubmed.ncbi.nlm.nih.gov/28257985/)) in two single-centre series.
  - *Bacteroides* spp. (*B. fragilis* 817): 24–43.9%.
  - *Streptococcus* spp.: 36.8%.
  - Also reported: *Klebsiella pneumoniae* (573), *Staphylococcus aureus* (1280), *Prevotella*, *Enterococcus*, *Clostridium* and *Candida* ([Unbound Medicine](https://www.unboundmedicine.com/5minute/view/5-Minute-Clinical-Consult/1688603/2.5/Fournier_Gangrene)).
  - In the 2024 systematic review, fungal infection raised the risk of death ([PMID 38625013](https://www.pubmed.gov/38625013/)).
- **Drugs:** SGLT2 inhibitors, e.g. canagliflozin, dapagliflozin and empagliflozin (FDA class labeling).
- **Lifestyle:** alcohol use disorder and obesity ([PMID 16927060](https://pubmed.ncbi.nlm.nih.gov/16927060/)).
- **Iatrogenic or traumatic:** urethral instrumentation, catheters, perianal surgery, circumcision.

---

## 6. Mechanism / Pathophysiology

**Causal chain**
1. A breach of the perineal or genital skin, the anorectal mucosa or the urethral mucosa lets mixed aerobic and anaerobic flora into the superficial fascial planes.
   - Typical breaches are fistula, abscess, stricture, catheter or minor trauma.
2. Host factors (hyperglycemia, immunosuppression, alcohol use) impair neutrophil defense. This allows bacteria to multiply.
   - The step is inferred from risk-factor associations. It was not shown mechanistically in the retrieved sources.
3. Aerobes and anaerobes act in synergy:
   - Anaerobes produce collagenase and heparinase, which promote clotting and break down fascia.
   - *Bacteroides* inhibits phagocytosis of the aerobes ([PMC4580094](https://pmc.ncbi.nlm.nih.gov/articles/4580094)).
4. Inflammation and edema lead to **obliterative endarteritis** and thrombosis of the subcutaneous arteries.
5. Ischemia and hypoxia of tissue result in necrosis of fascia and skin.
   - Hypoxia favors anaerobic growth and gas production. This feedback loop is inferred.
6. Infection spreads along the fascial planes:
   - Colles fascia → Buck and Dartos fascia (penis and scrotum);
   - Colles fascia → Scarpa fascia (anterior abdominal wall).
   - Spread toward the posterior and lateral sides is limited by attachments to the pubic rami, fascia lata and urogenital diaphragm ([PMC4580094](https://pmc.ncbi.nlm.nih.gov/articles/4580094)).
   - The testes, corpora and urethra are usually spared because they have a separate blood supply.
7. The process branches into two outcomes:
   - **Local:** gangrene and sloughing, which leaves large soft-tissue defects.
   - **Systemic:** toxins and bacteremia cause sepsis, septic shock and multi-organ failure, and this leads to death.
8. In SGLT2-inhibitor users, glycosuria may encourage genital colonization and infection.
   - This is a hypothesis; the retrieved sources did not show it directly.

**Ontology suggestions**
- **GO terms:**
  - inflammatory response GO:0006954;
  - neutrophil chemotaxis GO:0030593;
  - phagocytosis GO:0006909;
  - blood coagulation GO:0007596;
  - necrotic cell death GO:0070265;
  - response to hypoxia GO:0001666;
  - collagen catabolic process GO:0030574 (bacterial).
- **CL terms:**
  - neutrophil CL:0000775;
  - macrophage CL:0000235;
  - fibroblast CL:0000057;
  - endothelial cell CL:0000115;
  - keratinocyte CL:0000312.
- **No data found:** molecular profiling of FG tissue (transcriptomic, proteomic, metabolomic, single-cell, spatial) or functional screens.

---

## 7. Anatomical Structures Affected

UBERON IDs are suggestions and should be verified.

- **Primary sites:**
  - perineum (UBERON:0002356);
  - scrotum (UBERON:0001300);
  - penis (UBERON:0000989);
  - vulva in women (UBERON:0000997);
  - perianal region;
  - superficial fascia, including Colles, Dartos, Buck and Scarpa fascia.
- **Secondary spread:** anterior abdominal wall and thighs.
- **Systemic involvement:** cardiovascular and renal systems, through sepsis.
- **Tissues:** subcutaneous connective tissue (UBERON:0002384), fascia (UBERON:0008982) and skin (UBERON:0002097).
- **Usually spared:** testes, corpora cavernosa and urethra ([PMC4580094](https://pmc.ncbi.nlm.nih.gov/articles/4580094)).
- **Subcellular level:** not applicable. Extracellular matrix (GO:0031012) is the main compartment degraded.
- **Laterality:** the disease is often asymmetric. CT typically shows "asymmetric fascial thickening" ([PMID 18349455](https://pubmed.ncbi.nlm.nih.gov/18349455/)).

---

## 8. Temporal Development

- **Onset:** acute, in adults (peak age 50–79).
  - In children, about 66% of pediatric cases occur in infants under 3 months ([tp.amegroups](https://tp.amegroups.org/article/view/141046/html)).
- **Progression:**
  - The disease progresses rapidly, over hours.
  - Its usual course runs from cellulitis to fascial necrosis to gangrene and sepsis.
  - No formal staging system exists. Severity is graded with scores (FGSI, Section 10).
- **Remission:** happens only with treatment (debridement plus antibiotics). Spontaneous resolution is not described.
- **Critical window:** debridement is recommended within 24 hours ([PMC9388173](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9388173/)). A delay in treatment was linked to higher mortality ([PMC9018989](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9018989/)).

---

## 9. Inheritance and Population

**Epidemiology**
- US Nationwide Inpatient Sample:
  - Incidence was 1.6/100,000 males.
  - It peaked at 3.3/100,000 in men aged 50–79.
  - The highest regional rate was in the South (1.9/100,000).
  - Cases made up less than 0.02% of hospital admissions ([PMID 19286224](https://pubmed.ncbi.nlm.nih.gov/19286224/)).
- Medicare claims for people aged 65 and over showed 3–4/100,000 per year from 2016 to 2023 ([NIDDK 2025](https://www.niddk.nih.gov/-/media/Files/Strategic-Plans/urologic/2025/UDA-ADR-FG-2025_508.pdf)).
- Pediatric incidence is about 0.8 per 1 million ([tp.amegroups](https://tp.amegroups.org/article/view/141046/html)).
- **Sex ratio:** about 42:1 male to female (1,641 men vs 39 women) ([PMID 19286224](https://pubmed.ncbi.nlm.nih.gov/19286224/)).
- **Genetic inheritance:** not applicable. There is no inheritance pattern, penetrance, anticipation, founder effect or carrier frequency.

---

## 10. Diagnostics

- **Clinical diagnosis:** FG is a clinical diagnosis, confirmed during surgery by necrotic fascia.
- **Imaging:**
  - CT shows "asymmetric fascial thickening, subcutaneous emphysema, fluid collections, and abscesses."
  - CT offers "higher specificity… and superior evaluation of disease extent" than plain radiography or ultrasound ([PMID 18349455](https://pubmed.ncbi.nlm.nih.gov/18349455/)).
  - Gas is not always present.
  - Mimics include necrotic tumors, gas from trauma or iatrogenic causes, and vaginitis emphysematosa ([PMC7047600](https://pmc.ncbi.nlm.nih.gov/articles/PMC7047600)).
  - Ultrasound can show gas in the scrotal wall. No sensitivity data were retrieved.
- **Laboratory tests and scores:**
  - **LRINEC score** (Wong 2004, *Crit Care Med* 32:1535):
    - built from CRP, white cell count, hemoglobin, sodium, creatinine and glucose;
    - a score of 6 or more suggests necrotizing fasciitis;
    - a score above 8 had a positive predictive value of 93.4% in the derivation cohort.
    - Later validation was weaker: an AUROC of 0.696 in one prospective study, and false negatives with a score of 0 ([PMC12925613](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12925613/)).
    - No FG-specific validation was retrieved.
  - **FGSI** (Laor 1995):
    - nine physiologic and laboratory parameters;
    - in the original series, mortality was about 75% above a score of 9 versus about 22% below ([PMC6732100](https://pmc.ncbi.nlm.nih.gov/articles/PMC6732100)).
    - Corcoran 2008 (68 patients): a cutoff of 9 gave sensitivity 71.4% and specificity 90%, with mortality 46% versus 4% ([LVHN](https://scholarlyworks.lvhn.org/surgery/5851)).
  - **Simplified and Uludag scores:** the 2023 meta-analysis found higher admission scores in non-survivors. Mean differences were 5.53 for FGSI, 2.41 for the simplified FGSI and 5.47 for the Uludag FGSI ([J Pers Med 2023](https://doaj.org/article/06a09b62d21f43d886fba069c19c2efd); [PMC10532663](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10532663/)).
  - **Cultures:** wound and blood cultures guide de-escalation of antibiotics ([PMID 24973422](https://pubmed.ncbi.nlm.nih.gov/24973422/)).
- **Histopathology:** fascial necrosis with thrombosis of the subcutaneous vessels (endarteritis obliterans).
- **Genetic, omics-based and screening tests:** not applicable.
- **Differential diagnosis:**
  - cellulitis or erysipelas;
  - scrotal abscess;
  - epididymo-orchitis;
  - testicular torsion;
  - strangulated hernia;
  - necrotic tumors;
  - pyoderma gangrenosum;
  - non-infectious gas in tissue (trauma or iatrogenic).

---

## 11. Outcome / Prognosis

**Mortality**
- **US population data:**
  - In-hospital case fatality was 7.5% in the NIS cohort.
  - Referral-centre series report 20–40% ([PMID 19286224](https://pubmed.ncbi.nlm.nih.gov/19286224/)).
- **2024 systematic review** (57 studies, 3,646 patients):
  - Pooled mortality was 20.41%.
  - Mortality was highest in HIV-positive patients (54.17%).
  - The authors concluded that female sex, comorbidities, anatomic extent, sepsis and fungal infection increase mortality ([PMID 38625013](https://www.pubmed.gov/38625013/)).
- **2020 meta-analysis** (38 studies): diabetes, heart disease and renal failure were linked to death ([PMID 31962181](https://www.pubmed.gov/31962181/)).
  - Its abstract gives a risk ratio for diabetes of 0.72, which contradicts the text. Check the full text before using it.
- **Women:** their mortality is reported to be higher, possibly because of atypical signs and delayed presentation ([PMC10184784](https://pmc.ncbi.nlm.nih.gov/articles/PMC10184784)).
- **Children:** one series of 12 neonates and infants had no deaths ([PMC4359426](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4359426/)).
- **Long-term:** mortality ranged from 5% to 21% over follow-up of 60 days to 11 years (2026 systematic review).

**Morbidity and complications**
- multiple debridements;
- large tissue defects needing skin grafts or flaps;
- fecal diversion;
- sexual and urinary dysfunction, incontinence and psychological effects.

**Prognostic factors**
- FGSI or Uludag score above threshold;
- sepsis;
- greater extent of disease;
- delay to surgery;
- older age;
- comorbidity.

---

## 12. Treatment

| Intervention | NCIT (suggested) | Evidence |
|---|---|---|
| Emergency surgical debridement, repeated as needed | Debridement (NCIT C51698, to be verified) | Cornerstone; within 24 h ([PMC9388173](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9388173/)) |
| Broad-spectrum IV antibiotics (empiric) | Antibiotic therapy | IDSA 2014: vancomycin plus piperacillin-tazobactam or a carbapenem (strong recommendation, moderate evidence) ([PMID 24973422](https://pubmed.ncbi.nlm.nih.gov/24973422/)) |
| Clindamycin (toxin suppression) | Clindamycin C376 (to be verified) | Commonly added; dosing found only in a secondary source ([NDSU](https://ndsu.edu/fileadmin/centers/cap/documents/Skin_and_Soft_tissue_infection.pdf)) |
| Resuscitation and sepsis care | Supportive care | Standard practice |
| Negative-pressure wound therapy | Negative pressure wound therapy | See notes below |
| Hyperbaric oxygen (adjunct) | Hyperbaric oxygenation | See notes below |
| Fecal diversion (colostomy), urinary diversion (suprapubic catheter) | Colostomy | Used for anorectal or urethral involvement |
| Reconstruction (skin graft, flaps) | Skin graft | QoL scores above 70/100 in 4 of 5 domains in a small series ([Frontiers 2022](https://www.frontiersin.org/journals/surgery/articles/10.3389/fsurg.2022.994936/pdf)) |
| Stopping the SGLT2 inhibitor | — | FDA advice |

**Negative-pressure wound therapy (NPWT)**
- It is recommended after full necrosectomy by the WSES and SIS-E guidelines ([PMC9604683](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9604683/)).
- In a 36-patient study it meant fewer operations and faster healing ([PMID 36684293](https://pubmed.ncbi.nlm.nih.gov/36684293/)).
- In a 2025 cohort it shortened hospital stay but did not change mortality ([PMC12771018](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12771018/)).

**Hyperbaric oxygen (HBOT)**
- A 2022 meta-analysis of observational studies linked it to lower mortality but did not confirm shorter stays or fewer debridements ([PMC9388173](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9388173/); [PMC9388185](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9388185/)).
- A 23-patient series found no survival benefit ([PMC9018989](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9018989/)).
- Its benefit remains debated.

**Not applicable:** pharmacogenomics, gene therapy, cell therapy, RNA-based therapy, targeted therapy and immunotherapy.

**Clinical trials:** no FG-specific NCT trials were retrieved.

**Treatment algorithm:**
1. Recognize the condition and resuscitate.
2. Start empiric broad-spectrum antibiotics.
3. Debride urgently, and re-look every 24–48 hours.
4. Divert stool or urine as needed.
5. Manage the wound with NPWT, with HBOT as an optional adjunct.
6. Reconstruct.

---

## 13. Prevention

- **Primary:**
  - control diabetes;
  - limit alcohol;
  - treat perianal and urethral disease early;
  - care for catheters properly;
  - use SGLT2 inhibitors cautiously and counsel patients on genital symptoms (FDA).
  - The effect of these measures on FG rates has not been quantified.
- **Secondary:** early recognition (pain out of proportion to findings) and early CT. LRINEC, FGSI and Uludag scores help with triage.
- **Tertiary:** prevent recurrence and complications through wound care, rehabilitation and psychosocial support ([Urol Int 2025 / bvsalud](https://pesquisa.bvsalud.org/portal/resource/en/mdl-37074748), attribution uncertain).
- **Not applicable:** vaccines, genetic screening and genetic counseling.

---

## 14. Other Species / Natural Disease

- **Cattle:** necrotizing fasciitis of the scrotum and perineum was reported in a Hereford bull (*Bos taurus*, NCBITaxon:9913). It was caused by *Arcanobacterium haemolyticum*, and the bull was euthanized (*NZ Vet J* 2010; [bvsalud mdl-20927177](https://pesquisa.bvsalud.org/portal/resource/en/mdl-20927177)).
- **Dogs** (*Canis familiaris*, NCBITaxon:9615): necrotizing fasciitis occurs, including polymicrobial cases ([PMC8024095](https://pmc.ncbi.nlm.nih.gov/articles/PMC8024095)). Mortality is reported as 100% without timely debridement ([Today's Vet Practice](https://todaysveterinarypractice.com/emergency-medicine-critical-care/necrotizing-fasciitis-in-dogs/)). No scrotal-specific canine cases were retrieved.
- **Not applicable:** OMIA entry, orthologous genes and breed predisposition.
- **Zoonotic potential:** none (the disease arises from the patient's own flora).

---

## 15. Model Organisms

- **No FG-specific model:** no polymicrobial perineal FG model was found.
- **Related necrotizing soft-tissue infection models:**
  - Mouse subcutaneous *Streptococcus pyogenes* necrotizing skin and fascial infection ([JoVE](https://www.jove.com/t/70159/a-mouse-model-of-streptococcus-pyogenes-necrotizing-skin-infection)). It shows necrosis along the fascial planes at 24–48 hours.
  - A mouse study found ibuprofen worsens *S. pyogenes* soft-tissue infection ([PMID 21697021](https://pubmed.ncbi.nlm.nih.gov/21697021/)).
  - A fecal-slurry wound model in immunosuppressed mice is the closest polymicrobial analogue. It is a chronic wound model rather than necrotizing fasciitis ([PMC7359036](https://pmc.ncbi.nlm.nih.gov/articles/PMC7359036)).
  - A 2025 review covers inoculation, trauma, immunosuppression, genetically engineered and imaging-based models ([Dovepress JIR](https://www.dovepress.com/advances-in-necrotizing-fasciitis-animal-models-current-trends-and-fut-peer-reviewed-fulltext-article-JIR)).
- **Limitations of these models:**
  - single-organism inoculum;
  - sites other than the perineum;
  - no diabetic or SGLT2-inhibitor background;
  - differences between rodent and human fascial anatomy.
- **Not found:** genetic models (MGI, IMPC).

---

## Key Evidence Items

| PMID / ID | Claim |
|---|---|
| [19286224](https://pubmed.ncbi.nlm.nih.gov/19286224/) | Incidence 1.6/100,000 males; case fatality 7.5% |
| [38625013](https://www.pubmed.gov/38625013/) | Pooled mortality 20.41% (n=3,646) |
| [31962181](https://www.pubmed.gov/31962181/) | Comorbidities raise mortality (17-year meta-analysis) |
| [18349455](https://pubmed.ncbi.nlm.nih.gov/18349455/) | "Subcutaneous emphysema is the hallmark… but is not seen in all cases" |
| [24973422](https://pubmed.ncbi.nlm.nih.gov/24973422/) | IDSA empiric regimen for necrotizing infections |
| [25635243](https://pubmed.ncbi.nlm.nih.gov/25635243/), [28257985](https://pubmed.ncbi.nlm.nih.gov/28257985/) | Microbiology: polymicrobial, *E. coli* dominant |
| [31060053](https://pubmed.ncbi.nlm.nih.gov/31060053/) | SGLT2 inhibitor–associated FG (PMID to be verified) |
| [36684293](https://pubmed.ncbi.nlm.nih.gov/36684293/) | NPWT: fewer operations, faster healing |
| [16927060](https://pubmed.ncbi.nlm.nih.gov/16927060/) | Risk factors and management |
| [19040919](https://pubmed.ncbi.nlm.nih.gov/19040919/) | FG in infants |

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 31 |
| On topic | 8 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC7368210` *(abstract only)*: "may be a class effect of SGLT2 inhibitors"
  - closest text in source: "Multiple statistical analysis methods were applied to evaluate the potential association between SGLT2 inhibitors and FG, thus providing reliable and professionalized medication usage recommendations for SGLT2 inhibitors in clinical practice"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC8024095` (3 mentions) - Polymicrobial Necrotizing Fasciitis in a Dog: The Involvement of Macrococcus caseolyticus, Proteus mirabilis, and Escherichia coli.
  - shared terms: necrotizing

Weighed against this report's own most characteristic terms: `disease`, `found`, `infection`, `skin`, `mortality`, `subcutaneous`, `score`, `gene`, `genetic`, `sepsis`, `scrotum`, `gangrene`, `fascial`, `necrotizing`, `fgsi`, `patient`, `perineum`, `serie`, `tissue`, `fda`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 6 |
| Terms whose name was checked | 7 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0043352` (2 mentions) - the report calls it "MONDO"; MONDO calls it **fournier gangrene**
- `GO:0030574` (1 mention) - the report calls it "bacterial"; GO calls it **collagen catabolic process**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0070265` (obsolete necrotic cell death) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000997` (1 mention) - the report calls it "vulva in women"; UBERON calls it **mammalian vulva**, and lists "vulva" among its other names
- `UBERON:0002384` (1 mention) - the report calls it "Tissues:** subcutaneous connective tissue"; UBERON calls it **connective tissue**

### Terms the ontology service could not be reached for

6 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `HP:0034267` (1 mention)
- `HP:0010783` (1 mention)
- `HP:0000969` (1 mention)
- `HP:0100756` (1 mention)
- `HP:0100758` (1 mention)
- `HP:0001974` (1 mention)

### Terms whose obsolescence could not be checked

1 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `HP:0100806` (1 mention)