---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-11-01T05:19:10.221691'
end_time: '2026-11-01T05:24:01.630690'
duration_seconds: 291.41
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: TLR7-Related Systemic Lupus Erythematosus
  mondo_id: ''
  category: Mendelian
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: systemic lupus erythematosus 17; SLE17; TLR7 gain-of-function disease;
    TLR7 gain-of-function lupus
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
  web_search_requests: 4
  num_turns: 22
  total_cost_usd: 2.5833580000000005
  session_id: 2ccff955-20d8-5bb4-8e86-b52d55e2a947
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 7
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 14
  validator_version: 0.4.0
term_validation:
  total_terms: 48
  verified: 46
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 2
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0003493
    reported_labels:
    - Immunology/serology:** ANA
    ontology_label: Antinuclear antibody positivity
  - term_id: HP:0003765
    reported_labels:
    - no exact term
    ontology_label: Psoriasiform dermatitis
  - term_id: NCIT:C127799
    reported_labels:
    - anifrolumab
    ontology_label: Requires Secure Email Delivery of XML Indicator
  obsolete_terms:
  - term_id: NCIT:C15282
    ontology_label: Oriental Medicine
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TLR7-Related Systemic Lupus Erythematosus
- **MONDO ID:**  (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** systemic lupus erythematosus 17; SLE17; TLR7 gain-of-function disease; TLR7 gain-of-function lupus
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **TLR7-Related Systemic Lupus Erythematosus** covering all of the
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

Reading the cached TLR7 papers; now running a few searches to fill in the remaining primary papers and identifiers.

Collecting verbatim abstracts for the key PMIDs so the report can quote them exactly.

I have enough to produce the report. I'll write it now from the three full-text papers I read in full (PMID:35477763, PMID:42170322, PMID:42321474) plus the verified titles/findings of the surrounding literature. Quotes marked as direct are copied verbatim from the cached full texts; for papers where I only retrieved metadata and summaries, I describe findings without fabricating quotes.

---

# Comprehensive Research Report: TLR7-Related Systemic Lupus Erythematosus

**Causal gene: `TLR7`** (toll-like receptor 7, HGNC:15631, Xp22.2). This report concerns the Mendelian, **TLR7 gain-of-function (GOF)** monogenic form of systemic lupus erythematosus — OMIM **301080** (systemic lupus erythematosus 17, SLEB17), **MONDO:0859083** — and should not be conflated with polygenic SLE (MONDO:0005002) or with the complement-deficiency monogenic lupus forms (C1Q, C4A) that share the "SLE-N" naming series. The disease was first established as a human monogenic entity in 2022 by Brown, Vinuesa and colleagues (PMID:35477763).

---

## 1. Disease Information

TLR7-related SLE is a **monogenic, X-linked dominant form of systemic lupus erythematosus** caused by gain-of-function missense variants in *TLR7*, which encodes an endosomal single-stranded-RNA sensor. Enhanced receptor signalling lowers the threshold for activation by guanosine-containing self-ligands, breaking B-cell tolerance and driving type I interferon production and autoantibody formation. It belongs to the family of **type I interferonopathies / monogenic lupus** and is one of the clearest demonstrations that a single gene can cause SLE.

Key identifiers:
- **OMIM:** 301080 (Systemic lupus erythematosus 17; SLEB17)
- **MONDO:** MONDO:0859083
- **Gene:** *TLR7*, HGNC:15631, OMIM gene 300365, Xp22.2
- **ICD-11:** 4A40.0Z (Systemic lupus erythematosus) — no monogenic-specific code
- **ICD-10-CM:** M32.9
- **MeSH:** "Lupus Erythematosus, Systemic" (D008180); "Toll-Like Receptor 7" (D051196)

Synonyms: systemic lupus erythematosus 17; SLE17; SLEB17; TLR7 gain-of-function disease; TLR7 GOF lupus/interferonopathy.

**Source of information:** derived from aggregated, disease-level resources — individual case reports and functional genetic/immunological studies of a small set of probands (≈11–13 patients from ≈8–10 families worldwide as of 2026), not EHR cohorts. This is a very rare Mendelian condition and all knowledge is literature-based.

Landmark reference (direct quote, PMID:35477763, *Nature* 2022): *"Here we describe human systemic lupus erythematosus caused by a TLR7 gain-of-function variant."*

---

## 2. Etiology

**Primary cause — genetic, monogenic.** De novo or inherited **gain-of-function missense variants in *TLR7***. The founding paper identified a de novo p.Tyr264His (Y264H) in a Spanish girl with severe childhood SLE, plus p.Phe507Leu (F507L) and p.Arg28Gly (R28G) in additional families (PMID:35477763).

Direct quote (PMID:35477763): *"We identified a de novo, previously undescribed missense TLR7Y264H variant in a child with severe lupus and additional variants in other patients with lupus. The TLR7Y264H variant selectively increased sensing of guanosine and 2',3'-cGMP … and was sufficient to cause lupus when introduced into mice."*

**Genetic risk/modifier factors.**
- *TLR7* sits on **Xp22.2**; it escapes X-inactivation, contributing to female preponderance in both polygenic and monogenic lupus (Miquel et al., *J Autoimmun* 2023, PMID:36641351; reviewed PMID:42321474).
- Potential **digenic/epistatic modifiers**: the index proband also carried a heterozygous *RNASEH2B* p.Ala177Thr (Aicardi–Goutières-associated); mouse modelling found *Rnaseh2b* hemizygosity did **not** materially exacerbate the TLR7 phenotype beyond a mild interferon-signature increase (PMID:35477763). Villalvazo et al. described GOF *TLR7* together with loss-of-function *TNFAIP3/A20* as a Mendelian lupus pathway (*Clin Kidney J* 2022, PMID:36324999).
- Mechanistically adjacent monogenic causes converge on the same pathway: **UNC93B1** GOF variants (the TLR7 chaperone) cause SLE and chilblain lupus (David et al., *J Exp Med* 2024, PMID:38869500; Mishra et al., *Sci Immunol* 2024, PMID:38207015, showing disrupted degradative sorting of TLR7).

**Environmental contribution.** ssRNA viruses that engage TLR7 (e.g. SARS-CoV-2) are hypothesized disease triggers/exacerbators. Direct quote (PMID:35477763): *"an exacerbating role of this variant in humans may occur in the presence of environmental stimuli, including ssRNA viruses such as SARS-CoV-2 that are dependent on TLR7 immunity."* This is a mechanistic hypothesis, not a demonstrated clinical trigger.

**Protective factors.** None established genetically. By mechanistic inference, loss/reduction of TLR7 or MyD88 is protective: in mice, *Myd88* deficiency completely rescued the phenotype (PMID:35477763). No human protective allele is documented.

---

## 3. Phenotypes

The phenotype is **childhood-onset SLE** (often severe/early), with a type I interferonopathy flavour and, in a subset, Aicardi–Goutières-like neuro-inflammation. Frequencies below are from a small case series (≈11 patients; PMID:42170322 review) and should be read as qualitative.

| Phenotype | Type | HPO suggestion | Notes / frequency |
|---|---|---|---|
| Systemic lupus erythematosus | clinical diagnosis | HP:0002725 Systemic lupus erythematosus | Defining feature |
| Autoimmune thrombocytopenia | laboratory/clinical | HP:0001973 Autoimmune thrombocytopenia | Common presenting sign; often refractory (index patient and F507S cases) |
| Antinuclear antibody positivity | laboratory | HP:0003493 Antinuclear antibody positivity | Characteristic; anti-dsDNA, anti-Sm/RNP, anti-ssRNA |
| Hypocomplementemia | laboratory | HP:0005339 Abnormality of complement system / HP:0500167 low complement | Reported in index and F507S cases |
| Glomerulonephritis / lupus nephritis | clinical | HP:0000099 Glomerulonephritis; HP:0000093 Proteinuria | Renal involvement (proliferative GN in mouse and patients) |
| Arthralgia / inflammatory arthritis | symptom | HP:0002829 Arthralgia | Index patient |
| Cutaneous lupus / livedo reticularis / rash | clinical sign | HP:0000988 Abnormal skin morphology; HP:0100550 Livedo reticularis | F507S case livedo reticularis; chilblain lupus in UNC93B1 arm |
| Neurological involvement (AGS-like white-matter disease, intracranial calcification, hemichorea, developmental delay) | clinical | HP:0002352 Leukoencephalopathy; HP:0002514 Cerebral calcification; HP:0002072 Chorea; HP:0001263 Global developmental delay | Prominent in F507 and somatic F506S cases |
| Autoimmune hemolytic anemia | laboratory/clinical | HP:0001890 Autoimmune hemolytic anemia | Reported in acquired-mutation case (PMID:42067661) |
| Elevated type I interferon signature | laboratory | HP:0003765 (no exact term) | Hallmark biomarker |
| Hypertriglyceridemia | laboratory | HP:0002155 Hypertriglyceridemia | First metabolic manifestation, F507S (PMID:42170322) |
| Autoimmune retinopathy | clinical | HP:0000479 Abnormal retinal morphology | L528I case (PMID:42159815) |

**Onset:** predominantly neonatal–early-childhood. Direct quote (PMID:42170322): *"The median age at disease onset was 8 mo (range: second day of life to mid-20s), with marked female predominance (10/11 patients, 91%)."*

**Severity/progression:** variable; ranges from devastating AGS-like neurodegeneration to modest developmental delay with white-matter lesions. Direct quote (PMID:42170322): *"she avoided severe neurological sequelae, exhibiting only modest developmental delay and white matter lesions, in contrast to three previously reported F507S individuals who experienced devastating AGS-like neurological consequences and cerebral vasculitis."*

**Quality-of-life impact:** not formally measured with instruments (EQ-5D/SF-36) in this rare population; burden is driven by refractory cytopenias, nephritis, and neurodevelopmental impairment.

---

## 4. Genetic / Molecular Information

**Causal gene:** *TLR7* (HGNC:15631; OMIM 300365; Xp22.2; UniProt Q9NYK1). Suggested GO: receptor function GO:0035197 (siRNA binding) is not apt — use **GO:0002224 toll-like receptor signaling pathway**, **GO:0034154 toll-like receptor 7 signaling pathway**, and ligand sensing GO:0032727 (positive regulation of interferon-alpha production).

**Reported pathogenic variants** (all missense, GOF):
- **p.Tyr264His (Y264H)** — de novo; eighth leucine-rich repeat, ligand-binding site 1; increases affinity for guanosine/2′,3′-cGMP (PMID:35477763).
- **p.Phe507Leu (F507L)** — familial (mother+daughter) (PMID:35477763).
- **p.Arg28Gly (R28G)** — enhanced NF-κB after guanosine+ssRNA (PMID:35477763).
- **p.Phe507Ser (F507S)** — dimerization-interface; de novo and maternally transmitted multiplex family; severe neuro-inflammation; one case with hypertriglyceridemia (PMID:38324161; PMID:42170322).
- **p.Leu528Ile (L528I)** — de novo, interface; neuro-inflammatory, later autoimmune retinopathy (PMID:38324161; PMID:42159815).
- **p.Phe506Ser (F506S)** — **somatic/post-zygotic mosaic**, first somatic case, male infant (Zeng et al., *Ann Rheum Dis* 2025, PMID:39919974).
- **p.Pro435Ser (P435S)** — novel GOF, female, early-onset SLE + neuroinflammation (Tusseau et al., 2026, PMID:41846847).
- **p.Leu840Arg (L840R)** — male proband + asymptomatic carrier mother; alters TLR7–UNC93B1 interaction (Sethumadhavan et al., 2026, PMID:41743833).
- De novo infant case, *J Clin Invest* 2024 (Stremenova Spegarova et al., PMID:38753439).

**Variant classification:** pathogenic/likely pathogenic by ACMG, supported by functional GOF assays; absent from gnomAD/ExAC/dbSNP. Direct quote (PMID:35477763): *"This variant was not present in the databases of normal human genome variation (gnomAD, ExAC, dbSNP)."* ClinGen/GenCC curation rates the TLR7–SLE relationship as **moderate**.

**Functional consequence:** **gain of function** — increased affinity of ligand-binding site 1 for guanosine and 2′,3′-cGMP, enhanced NF-κB activation, spontaneous TLR7 cleavage to the active form, and increased MyD88. Direct quote (PMID:35477763): *"TLR7 GOF can cause B-cell-driven autoimmunity including SLE due to increased affinity to guanosine, leading to a lowered threshold for TLR7 activation."* Interface variants (F506S/F507S/L528I) appear to act by altering homodimerization rather than direct ligand affinity (PMID:38324161).

**Inheritance mechanism:** X-linked dominant; the Y264H mouse behaved as *"an X chromosome-linked dominant GOF allele"* (direct quote, PMID:35477763). Female preponderance is attributed partly to severity/lethality in hemizygous males. Somatic mosaicism now also recognized (PMID:39919974).

**Modifier genes:** *RNASEH2B* (A177T), *TNFAIP3/A20* (LOF), and chaperone *UNC93B1* GOF all modulate or phenocopy the TLR7 pathway (PMID:36324999; PMID:38869500; PMID:38207015).

**Epigenetics / chromosomal abnormalities:** none specifically described beyond X-chromosome dosage/escape from X-inactivation.

---

## 5. Environmental Information

- **Infectious triggers:** ssRNA viruses (SARS-CoV-2, other) that are TLR7 ligands are hypothesized exacerbators (PMID:35477763). NCBI Taxonomy: *Severe acute respiratory syndrome coronavirus 2* NCBITaxon:2697049.
- **Self-ligand "exposure":** endogenous guanosine, 2′,3′-cGMP, and RNA–protein complexes act as the operative ligands; this is an internal molecular "environment" rather than an external exposure.
- **Lifestyle/occupational/toxic exposures:** none established as disease-specific. General SLE environmental factors (UV light, smoking) are not characterized in this monogenic form.

---

## 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A germline (or post-zygotic somatic) **GOF missense variant in *TLR7*** (e.g. Y264H in LRR8/binding-site-1, or interface variants F506S/F507S/L528I) **results in** a structurally altered endosomal receptor.
2. The altered receptor **leads to** increased affinity for guanosine / 2′,3′-cGMP (site-1 variants) *or* altered homodimerization/UNC93B1 interaction (interface variants) — i.e. a **lowered activation threshold**.
3. Lowered threshold **results in** sensing of otherwise non-stimulatory self-RNA/guanosine and **spontaneous TLR7 cleavage to its active form** (≈75-kDa C-terminal / 65-kDa N-terminal fragments) even without exogenous stimulus.
4. Active TLR7 **leads to** increased **MyD88** recruitment and **NF-κB activation** (and type I/III interferon induction). [Demonstrated biochemically; direct quote PMID:35477763: *"MyD88 was also increased in kika splenocytes … consistent with enhanced TLR signalling."*]
5. Constitutive TLR7 signalling **provides an aberrant "signal 2"** to BCR-engaged self-reactive (immature) B cells that would normally die, **resulting in** their aberrant survival (upregulated anti-apoptotic *Mxd3*, *Serpina3g*). 
6. Aberrant survival **leads to** cell-intrinsic **accumulation of CD11c⁺ age-associated B cells (ABCs/DN2) and germinal-centre B cells**, and expansion of plasma cells.
7. **Branch (cell-extrinsic):** signalling also **drives** expansion of **follicular and extrafollicular helper T cells** and activation of plasmacytoid dendritic cells with a type I **interferon signature**.
8. Extrafollicular ABCs (the likely pathogenic source) **produce** anti-nuclear/anti-RNA/anti-Sm-RNP **autoantibodies**. [GC-independent; direct quote PMID:35477763: *"these results support the idea that TLR7-driven autoimmunity is GC independent."*]
9. Autoantibodies + immune complexes + sustained interferon **result in** end-organ injury: **proliferative glomerulonephritis** (mesangial immune deposits), thrombocytopenia, cytokine elevation (IFNγ, IL-6, IL-10, TNF), and, in a subset, **neuro-inflammation / AGS-like white-matter disease and intracranial calcification**.
10. Clinical manifestation: **childhood-onset SLE** with cytopenias, nephritis, and variable neurological disease.

The entire cascade is **MyD88-dependent** — a key therapeutic inference. Direct quote (PMID:35477763): *"Deficiency of MyD88 (an adaptor protein downstream of TLR7) rescued autoimmunity, aberrant B cell survival, and all cellular and serological phenotypes."* Direct quote: *"Therapies blocking TLR7 itself or MyD88 may be more effective than therapies blocking GCs in patients with SLE due to increased TLR7 signalling."*

**Molecular pathways:** TLR7→MyD88→IRAK→NF-κB (Reactome R-HSA-168181 Toll-like receptor 7/8 cascade; KEGG hsa04620); type I IFN induction. **Cellular processes:** breakdown of B-cell tolerance, aberrant anti-apoptotic B-cell survival (GO:0001783 B cell apoptotic process, decreased), germinal-centre and extrafollicular responses, chronic inflammation. **Protein dysfunction:** gain-of-function endosomal receptor (ligand affinity ↑ or dimerization interface altered). **Immune involvement:** autoimmunity with type I interferonopathy. **Subcellular localization:** endosome (GO:0005768); disrupted degradative sorting via UNC93B1/BORC implicated in related cases (PMID:38207015).

**Cell types (CL):** B cell CL:0000236; age-associated/double-negative B cell (no exact CL; use CL:0000236 with qualifier); germinal center B cell CL:0000844; plasma cell CL:0000786; plasmacytoid dendritic cell CL:0000784; follicular helper T cell CL:0002038; CD4-positive helper T cell CL:0000492; macrophage CL:0000235.

**Anatomy (UBERON):** spleen UBERON:0002106; kidney/glomerulus UBERON:0000074; bone marrow UBERON:0002371; brain white matter UBERON:0003544; lymph node UBERON:0000029.

**Molecular profiling:** RNA-seq of mutant mouse B cells showed upregulation of anti-apoptotic *Mxd3*, *Serpina3g*, *Ifnlr1/IL28ra*, *Cxcr3*; patient single-cell RNA-seq showed an elevated type I IFN signature (PMID:35477763). **Computational:** thermodynamic-integration molecular-dynamics simulations predicted increased guanosine binding free energy for the Y264H variant (PMID:35477763) — a COMPUTATIONAL evidence source.

---

## 7. Anatomical Structures Affected

- **Organ level:** kidney (lupus nephritis/glomerulonephritis — primary), hematologic system (platelets, red cells), skin (cutaneous lupus/livedo/chilblain), central nervous system (white matter, basal ganglia calcification), spleen/lymphoid organs (splenomegaly in mouse), and in case reports liver/pancreas/salivary gland/lung lymphoid infiltrates and heart (mouse). Body systems: immune, renal, hematologic, nervous, integumentary.
- **Tissue/cell level:** lymphoid tissue; B-lymphocyte lineage (ABC/DN2, GC B cells, plasma cells), pDCs, helper T cells, macrophages; renal mesangium (immune-complex deposits).
- **Subcellular (GO CC):** endosome (GO:0005768), endolysosome; receptor normally trafficked by UNC93B1.
- **Localization/lateralization:** neurological lesions typically **bilateral** (bilateral periventricular/temporal white-matter changes; bilateral intracranial calcification).

---

## 8. Temporal Development

- **Onset:** congenital to early childhood predominantly (median ~8 months; range second day of life to mid-20s; PMID:42170322). Pattern: often insidious then evolving — e.g. refractory thrombocytopenia preceding overt SLE.
- **Progression:** chronic, lifelong; neurological disease may be progressive/AGS-like in severe cases or stable/mild in others. Hematologic disease frequently relapsing and refractory to conventional therapy.
- **Remission:** treatment-induced partial remissions reported with JAK inhibition; no spontaneous remission documented.
- **Critical windows:** early targeted therapy may prevent severe neurological sequelae (hypothesis from F507S phenotypic heterogeneity, PMID:42170322).

---

## 9. Inheritance and Population

- **Inheritance:** **X-linked dominant** (Xp22.2). Monoallelic variants in females and hemizygous variants in males can cause disease. **De novo** in roughly half of probands; also maternally inherited (multiplex families); **somatic mosaicism** recognized (F506S, PMID:39919974). Asymptomatic/mildly affected carrier mothers occur (PMID:41743833).
- **Penetrance/expressivity:** incomplete penetrance and **highly variable expressivity** (asymptomatic carriers to lethal early disease), even within the same variant (F507S).
- **Sex ratio:** marked female predominance — *"10/11 patients, 91%"* female (direct quote PMID:42170322); males who survive tend to have severe early disease.
- **Epidemiology:** ultra-rare — only ~11–13 patients from ~8–10 families reported worldwide as of 2026; no prevalence/incidence estimate exists. It represents a small fraction of the broader "monogenic lupus" group.
- **Founder effects / consanguinity / anticipation:** none described; one de novo somatic case and several de novo germline cases argue against founder effects.

---

## 10. Diagnostics

- **Immunology/serology:** ANA (HP:0003493), anti-dsDNA, anti-Sm/RNP, anti-ssRNA; hypocomplementemia (low C3/C4). LOINC: ANA panels; complement C3 LOINC 4485-2, C4 LOINC 4498-5; anti-dsDNA LOINC 5131-1 (verify exact codes before binding).
- **Hematology:** thrombocytopenia, anemia, leukopenia.
- **Type I interferon signature** (ISG expression / blood transcriptomics) — a key supportive biomarker distinguishing interferonopathy-type monogenic lupus.
- **Imaging:** brain MRI (bilateral periventricular/temporal subcortical white-matter hyperintensities), CT for intracranial calcification (AGS-like).
- **Histopathology:** renal biopsy showing proliferative glomerulonephritis with mesangial immune-complex deposits.
- **Genetic testing (definitive):** **whole-exome or whole-genome sequencing** (how all cases were found; PMID:35477763 WGS/WES), confirmed by **Sanger sequencing**; targeted *TLR7* single-gene/next-gen panels for early-onset SLE or autoimmune cytopenia. Direct quote (PMID:42170322): *"next-generation gene panel or whole-exome sequencing offer significant benefit for the diagnosis of autoimmune cytopenia or in patients with early-onset SLE."* Deep/somatic-variant sequencing needed to detect mosaicism.
- **Functional confirmation:** NF-κB luciferase reporter GOF assays, cytokine responses to guanosine/R848 — research-grade.
- **Differential diagnosis:** polygenic SLE; Aicardi–Goutières syndrome and other type I interferonopathies; complement-deficiency monogenic lupus (C1q, C4); UNC93B1-related SLE/chilblain lupus; DNASE1L3/DNASE2 deficiency; immune thrombocytopenia of other cause.
- **Screening:** cascade genetic testing of relatives once a variant is identified; consider in any early-onset/refractory SLE or unexplained refractory autoimmune cytopenia.

---

## 11. Outcome / Prognosis

- **Mortality/survival:** no cohort survival data (ultra-rare). Severe early-onset and hemizygous-male cases can be life-threatening; mouse models showed decreased survival (direct quote PMID:35477763: Y264H mice had *"decreased survival"*).
- **Morbidity:** driven by lupus nephritis, refractory cytopenias, and neurodevelopmental/neuro-inflammatory disease (white-matter injury, calcification, developmental delay).
- **Disease course:** chronic, relapsing; conventional immunosuppression often insufficient.
- **Prognostic factors:** variant/codon (F507 codon linked to severe neuro disease), age of onset, degree of neurological involvement, and treatment timing. Direct quote (PMID:42170322): *"F507 codon variants were linked to severe disease."* Earlier targeted therapy is hypothesized to improve neurological outcome.
- **Prognostic biomarker:** sustained type I interferon signature; persistent hypocomplementemia tracks incomplete response.

---

## 12. Treatment

**Mechanism-directed options (the core therapeutic insight):**

- **JAK inhibition (ruxolitinib, baricitinib)** — targets downstream type I interferon/JAK-STAT signalling; the most consistently effective reported therapy. Direct quote (PMID:42170322): *"While four out of five patients treated with Janus kinase (JAK) inhibitors showed improved responses, conventional immunosuppressives showed limited sustained efficacy among the patients."* In the F507S case ruxolitinib normalized triglycerides and improved cytopenia, developmental, neurological measures. NCIT: NCIT:C15986 Pharmacotherapy + therapeutic_agent ruxolitinib (CHEBI:103180 / NCIT:C82725); baricitinib NCIT:C116724.
- **TLR7/8 antagonists (enpatoran; afimetoran)** — the rational upstream target. Direct quote (PMID:42170322): *"Enpatoran, a dual TLR7/8 inhibitor, has demonstrated encouraging preliminary results in clinical trials for SLE."* Direct quote (PMID:42321474): *"Phase II trials of an oral dual TLR7-TLR8 antagonist show durable suppression of the interferon signature in all patients … This treatment has shown clinical benefit for SLE and cutaneous lupus erythematosus."*
- **MyD88 inhibition** — mechanistically rescues the full phenotype in mice (PMID:35477763); no approved human agent yet.
- **Anifrolumab (anti-type I interferon receptor, anti-IFNAR1)** — benefits interferon-driven SLE generally (reviewed PMID:42321474). NCIT: NCIT:C127799 (anifrolumab).
- **B-cell–directed therapy / CAR-T** — B-cell-depleting CAR-T offers benefit in SLE but is costly (PMID:42321474). Rituximab was attempted in one case but discontinued for allergy (PMID:42170322).

**Conventional (incompletely effective):** corticosteroids (dexamethasone/prednisolone), IVIG, mycophenolate mofetil, hydroxychloroquine, romiplostim/platelet support for thrombocytopenia (PMID:42170322). NCIT: pharmacotherapy NCIT:C15986; corticosteroid therapy; immunosuppressive therapy NCIT:C15282.

**Supportive:** management of cytopenias, lipid control (fenofibrate, MCT formula in the hypertriglyceridemia case), renal and neurodevelopmental support/rehabilitation.

**Treatment strategy / personalized medicine:** genotype-guided — identification of a TLR7 GOF variant provides *"a convincing scientific rationale for direct TLR7 inhibition as a targeted therapy"* (direct quote, PMID:42170322). Recommendation emerging from the case literature: **JAK inhibitors as first-line**, moving toward TLR7/8 antagonists as they become available.

---

## 13. Prevention

- **Primary prevention:** not applicable (genetic). **Genetic counseling** for X-linked dominant inheritance, de novo recurrence (germline mosaicism) and somatic-mosaicism considerations. NCIT:C15240 Genetic Counseling.
- **Secondary prevention:** early genetic diagnosis in refractory early-onset SLE / autoimmune cytopenia enables earlier targeted therapy, hypothesized to prevent severe neurological sequelae.
- **Prenatal/reproductive:** carrier testing of at-risk mothers; prenatal or preimplantation genetic testing possible once a familial variant is known. 
- **Tertiary prevention:** interferon-pathway suppression (JAK/TLR7-8 inhibitors) to prevent organ damage; infection prophylaxis given immunosuppression; avoidance/awareness of TLR7-engaging viral triggers (hypothetical).
- **Immunization:** no disease-specific vaccine; standard SLE/immunosuppression vaccination precautions apply.

---

## 14. Other Species / Natural Disease

- **Model-organism orthologue:** mouse *Tlr7* (NCBI Gene 170743); human *TLR7* (NCBI Gene 51284). The human Y264H allele was knocked into the orthologous mouse residue ("kika" allele), reproducing disease — direct quote (PMID:35477763): *"was sufficient to cause lupus when introduced into mice."*
- **Spontaneous mouse lupus models:** the **Yaa** locus (Y-linked autoimmune accelerator = *Tlr7* duplication) and *Tlr7*-transgenic mice are long-standing spontaneous/engineered lupus models; TLR7 deletion ameliorates disease in other lupus-prone strains (reviewed in PMID:35477763).
- **Natural disease in companion animals/wildlife:** no naturally occurring *TLR7*-GOF lupus is documented (not in OMIA); canine SLE exists but is not attributed to this mechanism.
- **Conservation:** the Y264 residue is *"highly conserved across species, including zebrafish"* (direct quote, PMID:35477763), supporting evolutionary conservation of the ligand-sensing mechanism.
- **Zoonosis / cross-species transmission:** not applicable (non-infectious genetic disease).

---

## 15. Model Organisms

- **Primary model — mouse:**
  - **"kika" knock-in** (*Tlr7^Y264H*) on C57BL/6, CRISPR-Cas9 generated; recapitulates human disease: splenomegaly, ANAs, anti-ssRNA/Sm/RNP autoantibodies, thrombocytopenia, proliferative glomerulonephritis with mesangial deposits, spontaneous GCs, expanded ABCs/plasma cells/Tfh/extrafollicular Th, elevated IFNγ/IL-6/IL-10/TNF, and decreased survival (PMID:35477763). **Resource:** MGI.
  - **TLR7-deficient** control line (1-bp deletion).
  - **Compound crosses:** *Myd88*-knockout (complete rescue — establishes MyD88-dependence); *Bcl6^fl/fl;Cd23^cre* GC-deficient (autoimmunity persists → GC-independence); *Rag1⁻/⁻* mixed bone-marrow chimeras (dissected cell-intrinsic B vs cell-extrinsic T phenotypes); *Rnaseh2b* 1-bp deletion line (epistasis test — no major exacerbation).
  - Yaa / *Tlr7*-transgenic spontaneous models for comparison.
- **In vitro / cellular models:** RAW264.7 macrophage NF-κB luciferase reporter assays with TLR7 variant plasmids; patient PBMCs and bone-marrow-derived macrophages tested for guanosine/R848/ssRNA responsiveness; patient 10x single-cell RNA-seq for interferon signature (PMID:35477763).
- **Computational model:** thermodynamic-integration molecular-dynamics simulation of guanosine/R848 binding to dimeric TLR7 (PMID:35477763) — a validated in-silico mechanism for the affinity increase.
- **Phenotype recapitulation:** high for serological and B-cell-intrinsic phenotypes; the kika mouse is the exemplar "model recapitulates human mechanism" system. **Limitations:** mouse neuro-inflammation less emphasized; X-inactivation/sex-bias and human-specific immune compartments differ; single-residue models may not capture interface-variant biology.

---

## Key References (PMIDs)

- **PMID:35477763** — Brown GJ, …, Vinuesa CG. *TLR7 gain-of-function genetic variation causes human lupus.* Nature 2022. (Foundational; full text, mechanism, mouse models.)
- **PMID:42321474** — Vinuesa CG, Shrotri M, Rahman A. *TLR7 in systemic lupus erythematosus: genetics and emerging therapies.* Nat Rev Rheumatol 2026. (Current review; TLR7/8 antagonist trials.)
- **PMID:42170322** — Parvaneh N, et al. *TLR7 F507S gain-of-function mutation presenting with early-onset SLE and hypertriglyceridemia: Response to JAK inhibition.* J Hum Immun 2026. (Case + 11-patient review; onset, sex ratio, therapy.)
- **PMID:38324161** — David C, et al. *Interface Gain-of-Function Mutations in TLR7 Cause Systemic and Neuro-inflammatory Disease.* J Clin Immunol 2024. (F507S, L528I interface variants.)
- **PMID:38753439** — Stremenova Spegarova J, et al. *A de novo TLR7 gain-of-function mutation causing severe monogenic lupus in an infant.* J Clin Invest 2024.
- **PMID:39919974** — Zeng Y, et al. *Somatic gain-of-function mutation in TLR7 causes early-onset systemic lupus erythematosus.* Ann Rheum Dis 2025. (First somatic F506S case.)
- **PMID:41846847** — Tusseau M, et al. *Novel TLR7 gain-of-function variant and review of the associated disease spectrum.* J Hum Immun 2026. (P435S.)
- **PMID:41743833** — Sethumadhavan A, et al. *Identification of a novel TLR7 gain-of-function variant that underlies SLE.* J Hum Immun 2026. (L840R, UNC93B1 interaction.)
- **PMID:42159815** — Antropoli A, et al. *Autoimmune Retinopathy Complicating TLR7-related Monogenic Interferonopathy.* J Clin Immunol 2026. (L528I.)
- **PMID:38869500** — David C, et al. *Gain-of-function human UNC93B1 variants cause SLE and chilblain lupus.* J Exp Med 2024.
- **PMID:38207015** — Mishra H, et al. *Disrupted degradative sorting of TLR7 is associated with human lupus.* Sci Immunol 2024.
- **PMID:36324999** — Villalvazo P, et al. *Gain-of-function TLR7 and loss-of-function A20 … Mendelian lupus.* Clin Kidney J 2022.
- **PMID:36641351** — Miquel CH, et al. *Influence of X chromosome in sex-biased autoimmune diseases.* J Autoimmun 2023.
- **PMID:42067661** — Han Y, et al. *Autoimmune hemolytic anemia with acquired functional mutation of TLR7.* Immunol Res 2026.

---

### Notes on evidence provenance and curation caveats

- **Verbatim quotes** above are copied from the cached full texts of PMID:35477763, PMID:42170322 and PMID:42321474, which I read in full. For the remaining PMIDs I verified title/author/year/journal via PubMed but worked from abstract-level summaries, so I did **not** present invented verbatim quotes for them — before using any of those as KB evidence, fetch each with `just fetch-reference PMID:…` and confirm an exact-quote snippet.
- The **somatic F506S** case (PMID:39919974) means this entry should carry a somatic-mosaicism arm (`inheritance` bound to HP:0001442, `variant_origin: SOMATIC`) in addition to the X-linked dominant germline inheritance — consistent with the `somatic-mosaicism` skill.
- `MONDO:0859083` was **not** found in the local cache (`cache/mondo/terms.csv`) during my check; verify the binding with `just validate-terms` before committing, since the ID was sourced from mirrored MedGen/aggregator pages rather than the primary MONDO file.

Sources (web): [Interface GOF TLR7 (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10850255/), [GenCC submission SGC-107007.2](https://thegencc.org/submissions/SGC-107007.2), [PUMCH somatic TLR7 report](https://www.pumch.cn/en/detail/40153.html), [JHI TLR7 review](https://rupress.org/jhi/article-split/2/3/e20250266/281522/TLR7-mutations-leading-to-enhanced-TLR7-signaling), [MalaCards SLE17](https://www.malacards.org/card/systemic_lupus_erythematosus_17), [LOVD SLEB17](https://databases.lovd.nl/shared/diseases/07172), [JCI de novo infant TLR7 (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11213501/).

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 46 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 5 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0003493` (2 mentions) - the report calls it "Immunology/serology:** ANA"; HP calls it **Antinuclear antibody positivity**
- `HP:0003765` (1 mention) - the report calls it "no exact term"; HP calls it **Psoriasiform dermatitis**
- `NCIT:C127799` (1 mention) - the report calls it "anifrolumab"; NCIT calls it **Requires Secure Email Delivery of XML Indicator**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `NCIT:C15282` (Oriental Medicine) (1 mention)