---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-02T16:08:06.821487'
end_time: '2026-09-02T16:14:11.764495'
duration_seconds: 364.94
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Cardiac Facial and Digital Anomalies with Developmental Delay
  mondo_id: MONDO:0032572
  category: Genetic
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
  - claude-sonnet-5
  web_search_requests: 13
  num_turns: 37
  total_cost_usd: 1.7514165999999995
  session_id: b3630604-0814-5496-a401-d7ca13ab983f
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 29
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 6
  quotes_valid: 4
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:37043537
  - PMC:PMC10120005
  relevance_assessed: 16
  on_topic: 13
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 53
  verified: 49
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 27
  labels_matching: 18
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0032572
    reported_labels:
    - MONDO
    - CAFDADD
    ontology_label: cardiac, facial, and digital anomalies with developmental delay
  - term_id: HP:0031650
    reported_labels:
    - bicuspid aortic valve
    ontology_label: Abnormal atrioventricular valve physiology
  - term_id: HP:0004385
    reported_labels:
    - double outlet right ventricle
    ontology_label: Protracted diarrhea
  - term_id: CL:0002518
    reported_labels:
    - "cardiac endothelial cell \u2014 outflow tract context"
    ontology_label: kidney epithelial cell
  - term_id: UBERON:0004134
    reported_labels:
    - cardiac outflow tract
    ontology_label: proximal tubule
  - term_id: UBERON:0004674
    reported_labels:
    - upper eyelid
    ontology_label: facial nerve root
  labels_variant: 3
  obsolete_terms:
  - term_id: HP:0001180
    ontology_label: obsolete Hand oligodactyly
    replaced_by: HP:0009380
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cardiac Facial and Digital Anomalies with Developmental Delay
- **MONDO ID:** MONDO:0032572 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Cardiac Facial and Digital Anomalies with Developmental Delay** covering all of the
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

Found a very recent (2025) mechanistic review — "TRAF7 in signaling and disease: emerging mechanisms and clinical implications." Let me pull that plus a couple final confirmatory details (GARD ID for the correct disease, and gnomAD/OMIM gene entry basics).

I have enough material now to compile a thorough, well-cited report.

# Cardiac, Facial, and Digital Anomalies with Developmental Delay (CAFDADD) — Comprehensive Research Report

## Important Nomenclature Note (Named-Entity Disambiguation)

Two rare disorders carry nearly identical plain-language names and must not be conflated:

| | **CAFDADD (this report's target)** | **MED13L syndrome (different disease)** |
|---|---|---|
| MONDO | MONDO:0032572 | different MONDO ID |
| OMIM | #618164 | #616789 (Asadollahi-Rauch syndrome) |
| Orphanet | ORPHA:592570 | ORPHA:471810 |
| GARD | disease 22370 ("TRAF7-associated heart defect–digital anomalies–facial dysmorphism–motor and speech delay syndrome") | disease 17588 ("Cardiac anomalies–developmental delay–facial dysmorphism syndrome") |
| Gene | **TRAF7** (16p13) | **MED13L** (12q24) |

An early web search surfaced the GARD page for the MED13L-caused disorder ("Cardiac anomalies-developmental delay-facial dysmorphism syndrome") as a top hit; that record was verified and excluded from this report — it is a distinct MED13L-mediator-complex disorder, not the TRAF7 entity requested. All content below pertains specifically to the TRAF7-caused, OMIM #618164 / MONDO:0032572 entity, commonly abbreviated **CAFDADD** or "TRAF7 syndrome."

---

## 1. Disease Information

**Overview.** CAFDADD is a rare, autosomal dominant, multisystem neurodevelopmental malformation syndrome caused by heterozygous (typically de novo) germline missense variants in **TRAF7** (TNF Receptor-Associated Factor 7, chromosome 16p13.3). It was first delineated in 2018 and is characterized by a recognizable facial gestalt (blepharophimosis being a hallmark), variable congenital heart defects, digital/limb anomalies, and global developmental delay/intellectual disability ([Tokita et al. 2018, AJHG, PMID:29961569](https://pubmed.ncbi.nlm.nih.gov/29961569/); [Castilla-Vallmanya et al. 2020, Genet Med, PMID:32376980](https://www.nature.com/articles/s41436-020-0792-7)).

**Key identifiers:**
- **OMIM:** #618164 (phenotype, CAFDADD) / *606692 (gene, TRAF7) ([omim.org/entry/618164](https://omim.org/entry/618164), [omim.org/entry/606692](https://omim.org/entry/606692))
- **Orphanet:** ORPHA:592570, "TRAF7-associated heart defect-digital anomalies-facial dysmorphism-motor and speech delay syndrome" ([orpha.net/en/disease/detail/592570](https://www.orpha.net/en/disease/detail/592570))
- **MONDO:** MONDO:0032572
- **GARD:** disease ID 22370 ([rarediseases.info.nih.gov/diseases/22370](https://rarediseases.info.nih.gov/diseases/22370/traf7-associated-heart-defect-digital-anomalies-facial-dysmorphism-motor-and-speech-delay-syndrome))
- **Gene:** HGNC:20456 (TRAF7); ClinGen HGNC:20456
- **ClinGen validity:** the Intellectual Disability and Autism GCEP issued a **Definitive** gene-disease validity classification for TRAF7 / "autosomal dominant syndromic complex neurodevelopmental disorder" (09/06/2023) ([search.clinicalgenome.org/kb/genes/HGNC:20456](https://search.clinicalgenome.org/kb/genes/HGNC:20456))

**Synonyms:** CAFDADD; TRAF7 syndrome; TRAF7-related multiple congenital anomalies–intellectual disability syndrome (MCA-IDS); TRAF7-related developmental delay–malformation syndrome.

**Source of information:** knowledge derives almost entirely from **aggregated case-series/cohort literature** (case reports pooled through systematic literature review) rather than large EHR-based epidemiology — appropriate given the disorder's rarity (fewer than 70 published cases as of 2024).

---

## 2. Etiology

**Primary cause — genetic, monogenic.** CAFDADD is caused by heterozygous, usually **de novo**, germline missense variants clustering in the **WD40 repeat domain** of TRAF7. Tokita et al. identified variants in 7 unrelated individuals (4 unique variants, with p.Arg655Gln recurrent in 4 patients) ([PMID:29961569](https://pubmed.ncbi.nlm.nih.gov/29961569/)). Castilla-Vallmanya et al. (2020) expanded this to 45 patients, finding that "almost all variants occur in the WD40 repeats and most are recurrent" ([nature.com/articles/s41436-020-0792-7](https://www.nature.com/articles/s41436-020-0792-7)). By 2023–2024, literature review tallies reached **58–69 published individuals with 8–26 distinct variants** ([medRxiv 10.1101/2023.12.13.23299272](https://www.medrxiv.org/content/10.1101/2023.12.13.23299272v1.full); Korean case report, [PMC11011995](https://pmc.ncbi.nlm.nih.gov/articles/PMC11011995/)).

**Genetic risk factors:**
- Virtually all reported variants are **missense**; "no other types of variants or variations have been identified" — i.e., truncating/loss-of-function alleles are not established causes, consistent with TRAF7 tolerating LoF at the population level (gnomAD v4.0 **pLI ≈ 0**), while missense variants act through a distinct dominant-negative/hypomorphic mechanism.
- **Recurrent hotspot residues** (e.g., p.Arg655Gln) are seen across unrelated probands, and pathogenic variants are found at highly conserved WD40 amino acids.
- **Somatic mosaicism** has been documented: multiple mosaic probands and at least one asymptomatic mosaic parent transmitting the variant to an affected child have been reported (ClinGen curation notes; [PMID:37067385](https://pubmed.ncbi.nlm.nih.gov/37067385/), "Novel mosaic TRAF7 likely pathogenic variant in an African American family").
- Inherited (non-de-novo) TRAF7 variants have also been reported in isolated **congenital heart disease** cohorts with **incomplete penetrance** — three unrelated CHD probands (p.Val142Met, p.Val442Met, splice variant c.1998+2T>G) had unaffected carrier parents ([PNAS 2023, PMID:37043537](https://www.pnas.org/doi/10.1073/pnas.2214997120)).

**Environmental risk factors:** none established; this is a purely monogenic disorder with no known toxin, infectious, or lifestyle contributor. Advanced paternal age is a plausible but unquantified de novo-variant risk factor common to this class of disorder (not specifically studied for TRAF7).

**Protective factors:** none reported.

**Gene-environment interactions:** none described in the literature; not applicable to this monogenic, fully genetically determined disorder.

---

## 3. Phenotypes

Phenotype frequencies below are drawn primarily from the pooled literature-review cohorts (Castilla-Vallmanya et al. 2020, n=45; the 2023/2024 update, n=69 total) and individual case reports.

### Craniofacial (near-universal; present from birth)
- **Blepharophimosis** — the single most characteristic and recurrent feature, present in the great majority of patients; sometimes accompanied by **ptosis** and **epicanthal folds** (suggested HP terms: HP:0000581 Blepharophimosis, HP:0000508 Ptosis, HP:0000286 Epicanthus)
- Dysmorphic, low-set, or dysplastic ears (HP:0000369 Low-set ears; HP:0008551 Microtia or HP:0000377 Abnormal helix morphology depending on case)
- Short neck with excess nuchal skin (HP:0000470 Short neck)

### Cardiac (present in ~6/7 to most patients across cohorts; onset prenatal/congenital)
- Wide phenotypic spectrum from mild to complex: bicuspid aortic valve, patent ductus arteriosus (a recurrent "core" feature), atrial/ventricular septal defects, double outlet right ventricle, pulmonary atresia, tricuspid atresia, truncus arteriosus, aortic root dilation/aneurysm, hypoplastic left heart syndrome ([Tokita 2018](https://pubmed.ncbi.nlm.nih.gov/29961569/); [PNAS 2024 "spectrum of heart defects" paper, PMID:38466853](https://pubmed.ncbi.nlm.nih.gov/38466853/)). Suggested HP terms: HP:0001631 (ASD), HP:0001629 (VSD), HP:0001643 (PDA), HP:0031650 (bicuspid aortic valve), HP:0004385 (double outlet right ventricle)
- Adult-onset progressive aortic root aneurysm has been reported requiring surgical repair (Bentall procedure) in the first documented adult (Korean) case, mimicking connective-tissue-disorder presentations ([PMC11011995](https://pmc.ncbi.nlm.nih.gov/articles/PMC11011995/))

### Digital/skeletal (near-universal)
- Overlapping toes, finger/toe deviations, joint contractures, arachnodactyly, pectus carinatum, vertebral anomalies, scoliosis; one adult case developed degenerative joint disease and bilateral avascular necrosis (HP:0001180 Toe joint contracture; HP:0009484 Camptodactyly; HP:0000768 Pectus carinatum)

### Neurodevelopmental
- **Global developmental delay / intellectual disability** — a defining feature across nearly all patients, with variable severity (HP:0001263 Global developmental delay; HP:0001249 Intellectual disability)
- Speech/language delay, often disproportionately severe, sometimes requiring augmentative/alternative communication
- **Seizures** in a subset (HP:0001250 Seizure)
- Autism spectrum features and sleep disturbance/OSA reported as recurrent, less-universal manifestations
- Brain imaging abnormalities: diffuse cerebral atrophy, cerebellar atrophy, enlarged ventricles/hydrocephalus, tethered cord in some patients

### Sensory
- **Hearing loss** (sensorineural) — reported as present in **all patients** in the 2024 pooled cohort along with short stature ("Hearing loss and short stature, present in all patients," per the 11-new-case/58-case literature review, [medicalxpress summary](https://medicalxpress.com/news/2024-04-elucidate-traf7-syndrome-neurological-developmental.html))
- Ocular anomalies including optic atrophy and cortical blindness in severe cases; one report of **primary congenital glaucoma** co-occurring with a rare TRAF7 variant (ScienceDirect, 2026 case report)

### Endocrine/growth
- **Growth deficiency/short stature** is a recurrent, near-universal feature
- Endocrine anomalies described generally in the pooled cohort, though the literature does not detail specific hormone axes (e.g., no confirmed reports isolating growth hormone deficiency vs. constitutional short stature)

### Other/postnatal
- Prenatal ultrasound abnormalities in a subset: cystic hygroma, 2-vessel umbilical cord, cardiac defects visible antenatally
- Neonatal respiratory distress, poor feeding, hypotonia, jaundice

**Progression/severity:** Highly variable expressivity even among unrelated patients with the same recurrent variant (e.g., p.Arg655Gln); no strict genotype–severity correlation has been established. Developmental delay/regression can be progressive in a subset.

**Quality of life impact:** Communication impairment (expressive language) is prominent and functionally limiting; cardiac defects — when severe — drive early-life morbidity/mortality risk; sleep-disordered breathing (OSA, exacerbated by craniofacial/skeletal features) contributes materially to adult morbidity (documented AHI of 88/hour in the Korean adult case, managed with CPAP).

---

## 4. Genetic/Molecular Information

**Causal gene:** TRAF7 (HGNC:20456; OMIM *606692; 16p13.3).

**Variant classification/type:** Exclusively germline **heterozygous missense** variants for CAFDADD; classified pathogenic/likely pathogenic per ACMG/AMP criteria (commonly invoking PS2 [de novo], PM1/PM2 [mutational hotspot/absence from population databases], PP1/PP2/PP3 in case reports — see the Korean p.Arg655Gln case, [PMC11011995](https://pmc.ncbi.nlm.nih.gov/articles/PMC11011995/)).

**Mutational hotspot:** the great majority of pathogenic variants localize to the **WD40 β-propeller repeat domain** (C-terminal), which mediates TRAF7's protein-protein interactions; these residues are highly conserved across vertebrates.

**Allele frequency:** pathogenic CAFDADD variants are essentially absent from population databases (gnomAD), consistent with de novo occurrence; ~50 total TRAF7 variants are catalogued in ClinVar with several classified pathogenic/likely pathogenic.

**Somatic vs. germline — a critical dual biology:**
- **Germline** missense TRAF7 variants (WD40 domain) → CAFDADD (developmental syndrome)
- **Somatic** TRAF7 variants (also predominantly WD40 domain, but often at overlapping/distinct residues, e.g., C388Y, G536S, K615E, R653Q) → found in **~25% of meningiomas**, where they very frequently co-occur with a recurrent **KLF4 p.Lys409Gln (K409Q)** mutation (secretory meningioma subtype) or with PI3K-pathway activating mutations, indicating TRAF7 loss is "necessary but not sufficient" and requires a cooperating second hit ([Cancer Research, AACR](https://aacrjournals.org/cancerres/article/81/16/4218/670292/Loss-of-Function-Mutations-in-TRAF7-and-KLF4); [PMC9468091](https://pmc.ncbi.nlm.nih.gov/articles/PMC9468091/)). TRAF7 somatic mutations are also implicated in mesotheliomas and perineuriomas, and altered TRAF7 expression correlates with poorer prognosis in hepatocellular carcinoma, breast cancer, and prostate cancer ([Orock et al. 2025 review, Mol Med, PMID:41372821 / PMC12801879](https://pmc.ncbi.nlm.nih.gov/articles/PMC12801879)).
- A case of **TRAF7 somatic mosaicism causing bilateral optic nerve sheath meningiomas** has also been reported, bridging the germline-syndromic and somatic-oncogenic biology ([PMID:35733823](https://pubmed.ncbi.nlm.nih.gov/35733823/)).
- **Long-term meningioma/tumor risk in CAFDADD patients is not yet established** — one of the original 7 Tokita patients (Subject 3) developed a meningioma, raising an open question about tumor surveillance for germline carriers, but most reported patients are pediatric and follow-up is limited.

**Functional consequence — dominant-negative / loss-of-function-like:** Multiple independent lines of evidence converge on a **dominant-negative** mechanism rather than classic gain-of-function:
- Tokita et al. showed mutant TRAF7 causes **decreased ERK1/2 phosphorylation** relative to wild-type, implicating impaired **MAPK (MAP3K3/MEKK3–MEK–ERK)** signaling; TRAF7 normally interacts via its WD40 domain with **MAP3K3**, contributing to JNK/p38/AP-1 activation as well ([PMC6035372](https://pmc.ncbi.nlm.nih.gov/articles/PMC6035372/); [Orock 2025 review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12801879)). This phenotypic direction parallels ERK2-knockout mouse cardiovascular/craniofacial phenotypes.
- The 2023 PNAS mechanistic study (Mishra-Gorur et al.) showed WT and mutant TRAF7 **heterodimerize**, and that mutant protein has a **dominant effect**, disrupting WT TRAF7's interaction with **MEKK3** — "low concentrations of mutant TRAF7...sufficient to disrupt the interaction of WT TRAF7 with MEKK3" ([PMC10120005](https://pmc.ncbi.nlm.nih.gov/articles/PMC10120005); PMID:37043537).
- The same study identified a previously unrecognized TRAF7 function in **ciliogenesis / intraflagellar transport**, via interaction with **IFT57**: both somatic (meningioma) and germline (CHD/CAFDADD) mutants show "substantially diminished interactions of IFT57 with...TRAF7 mutants," and TRAF7 knockdown in zebrafish/*Xenopus* impairs both anterograde and retrograde ciliary transport.

**Modifier genes:** none formally established; variable expressivity and incomplete penetrance (in familial/inherited CHD-only presentations) suggest modifiers or mosaicism-related dosage effects exist but are uncharacterized.

**Epigenetic information:** Castilla-Vallmanya et al. (2020) performed **transcriptomic profiling of patient fibroblasts**, identifying differentially expressed genes associated with TRAF7 variant status — supporting a measurable downstream transcriptional signature, though specific pathway enrichment beyond MAPK/NF-κB was not detailed in the available abstracts. No DNA methylation "episignature" for CAFDADD has been reported to date (in contrast to some other chromatinopathies).

**Chromosomal abnormalities:** not a feature of this disorder — CAFDADD is caused by sequence-level missense variants, not copy-number or structural chromosomal changes.

**Protein structure:** TRAF7 comprises an **N-terminal RING finger domain**, an adjacent **zinc-finger domain**, a central **coiled-coil (TRAF-N-like) motif**, and **seven WD40 repeats** forming a C-terminal β-propeller. Homology modeling shows meningioma- and CHD-associated missense variants disrupt either the WD40 ligand-binding surface (via hydrophobic-residue substitutions, e.g., W400, Y563, Y603, Y621, P398, I441, V661) or destabilize protein-protein interaction interfaces ([PMC10120005](https://pmc.ncbi.nlm.nih.gov/articles/PMC10120005)).

---

## 5. Environmental Information

No environmental, lifestyle, or infectious contributors have been identified or studied for CAFDADD; it is a fully penetrant (in de novo cases) monogenic disorder. This section is not applicable beyond the genetic mechanism described above.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (as currently supported by the literature; branch points and inference levels noted)

1. A **de novo (or rarely inherited/mosaic) heterozygous missense variant** arises in the WD40 repeat domain (or occasionally RING/zinc-finger region) of **TRAF7** — *demonstrated directly by exome sequencing in >90% of published cases*.
2. The variant **destabilizes the WD40 β-propeller's protein-interaction surface**, altering TRAF7's binding to its partners — *inferred from homology modeling and co-immunoprecipitation studies of specific recurrent residues* ([PMC10120005](https://pmc.ncbi.nlm.nih.gov/articles/PMC10120005)).
3. Mutant TRAF7 **heterodimerizes with wild-type TRAF7** and exerts a **dominant-negative effect**, disrupting the wild-type protein's interaction with its downstream partner **MEKK3/MAP3K3** even at substoichiometric mutant:WT ratios — *demonstrated experimentally in vitro*.
4. This leads to **two parallel, partially independent downstream consequences** (branch point):
   - **4a. Impaired MAPK signaling:** reduced activation of the **MAP3K3(MEKK3)–MEK1/2–ERK1/2** axis (and downstream JNK/p38/AP-1 branch) — *demonstrated by reduced ERK1/2 phosphorylation in patient-variant expression assays* ([Tokita 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6035372/)). This phenocopies ERK2-conditional-knockout mice, which show cardiovascular and craniofacial malformations closely resembling CAFDADD — *supporting inference by cross-species phenotype comparison, not direct demonstration in human tissue*.
   - **4b. Impaired ciliogenesis/intraflagellar transport:** disrupted TRAF7–**IFT57** interaction degrades primary cilia and both anterograde and retrograde ciliary transport — *demonstrated directly in zebrafish/*Xenopus* morphant models* ([PMC10120005](https://pmc.ncbi.nlm.nih.gov/articles/PMC10120005)).
5. Because the cardiac outflow tract, craniofacial skeleton, and anterior skull-base meninges **all derive embryologically from neural crest**, and TRAF7 mRNA is enriched in neural tube tissue overlapping the neural crest marker **Sox10**, disruption of TRAF7 signaling in this lineage produces the syndrome's convergent, multi-organ phenotype — *inferred from expression data and morphant phenotypes (disorganized pharyngeal arches, reduced sox10 expression, disrupted Sox10/Twist neural-crest marker expression) rather than directly demonstrated in human embryonic tissue*.
6. **Ciliary dysfunction** (from step 4b) independently produces **left-right patterning defects** (via disrupted **pitx2c** laterality signaling at the ciliated left-right organizer) → contributes to complex/laterality-associated heart defects, and separately causes **hydrocephalus and renal cystic pathology** seen in some patients — *demonstrated in Xenopus/zebrafish, extrapolated to explain overlapping human phenotypes (ventricular enlargement, complex CHD)*.
7. Combined MAPK hypofunction (4a) and neural-crest/ciliary disruption (4b→5→6) manifest clinically as the CAFDADD triad: **congenital heart defects, craniofacial dysmorphism (notably blepharophimosis), and digital/skeletal anomalies**, layered with **global developmental delay** from presumed CNS neural-crest/ciliary contributions (cerebral/cerebellar atrophy, hydrocephalus on imaging) — *this final integrative step is a clinical-pathological correlation, not a directly traced single mechanism*.
8. Separately, in **somatic tissue** (meninges), an analogous but tissue-restricted TRAF7 loss-of-function mutation, cooperating with a **second hit** (commonly KLF4 K409Q or a PI3K-pathway activator), drives **meningioma** formation via the same dominant-negative MEKK3-disruption and cilia-loss mechanism, now acting oncogenically — explaining why the germline (CAFDADD) and somatic (meningioma) mutation spectra overlap in the same WD40 hotspots despite radically different clinical consequences (developmental syndrome vs. tumor) ([PNAS 2023, PMID:37043537](https://www.pnas.org/doi/10.1073/pnas.2214997120); [Cancer Research 2021](https://aacrjournals.org/cancerres/article/81/16/4218/670292/)).

### Category detail

- **Molecular pathways:** MAPK cascade (MAP3K3/MEKK3 → MEK1/2 → ERK1/2; also JNK/p38 → AP-1); NF-κB modulation (TRAF7 also inhibits c-Myb and stabilizes VE-cadherin at cell junctions per the 2025 review); Wnt pathway de-repression secondary to cilia loss ("loss of cilia...relieves Wnt pathway regulation," implicated specifically in the tumor context) ([Orock et al. 2025, PMC12801879](https://pmc.ncbi.nlm.nih.gov/articles/PMC12801879); [PMC10120005](https://pmc.ncbi.nlm.nih.gov/articles/PMC10120005)).
- **Cellular processes:** primary ciliogenesis, intraflagellar transport (anterograde/retrograde), neural crest cell specification/migration, E3-ubiquitin-ligase–mediated protein turnover (TRAF7 itself is an E3 ubiquitin ligase).
- **Protein dysfunction:** dominant-negative heterodimerization disrupting a normally functioning WT protein pool — distinct from simple haploinsufficiency (consistent with gnomAD pLI≈0, i.e., LoF alleles alone are tolerated, but missense dominant-negative alleles are pathogenic).
- **Tissue damage/laterality mechanisms:** ciliary dysfunction at the embryonic left-right organizer → laterality defects contributing to complex CHD; no primary oxidative-stress, fibrotic, or ischemic mechanism described.
- **Molecular profiling:** patient-fibroblast transcriptomics (Castilla-Vallmanya 2020) show differential gene expression associated with variant status, supporting a measurable transcriptional signature downstream of TRAF7 dysfunction.

### Suggested ontology terms
- **GO (biological process):** GO:0000165 (MAPK cascade), GO:0007266 (Rho protein signal transduction — via MEKK3 axis), GO:0035556 (intracellular signal transduction), GO:0060271 (cilium assembly), GO:0003351 (epithelial cilium movement involved in extracellular fluid movement), GO:0007368 (determination of left/right symmetry), GO:0014032 (neural crest cell development)
- **GO (molecular function):** GO:0061630 (ubiquitin protein ligase activity)
- **GO (cellular component):** GO:0005929 (cilium), GO:0005814 (centriole)
- **CL:** CL:0011012 (neural crest cell), CL:0000057 (fibroblast), CL:0002518 (cardiac endothelial cell — outflow tract context)

---

## 7. Anatomical Structures Affected

**Organ level (primary):**
- **Heart** — outflow tract, septa, valves (bicuspid aortic valve, PDA, ASD/VSD, DORV, pulmonary/tricuspid atresia, truncus arteriosus, aortic root)
- **Craniofacial skeleton and periocular structures** — eyelids (blepharophimosis, ptosis), ears
- **Skeletal system** — digits, spine, chest wall
- **CNS** — cerebrum, cerebellum, ventricular system (atrophy, hydrocephalus), spinal cord (tethered cord)

**Secondary/complication-level organ involvement:**
- Ear/auditory system (sensorineural hearing loss)
- Eye (optic atrophy, cortical blindness, congenital glaucoma in at least one case)
- Kidney (cystic changes reported in animal models; not well-documented in human patients)
- Respiratory system (obstructive sleep apnea secondary to craniofacial/skeletal anatomy)
- Meninges (tumor risk via analogous somatic mechanism, not yet confirmed as a CAFDADD-specific complication)

**Body systems involved:** cardiovascular, craniofacial/musculoskeletal, nervous, sensory (auditory, visual), endocrine/growth, respiratory (secondary).

**Tissue/cell level:** neural-crest-derived mesenchyme (cardiac outflow tract, craniofacial cartilage/bone, meninges anterior to the foramen magnum) is the convergent cell lineage implicated across the syndrome's major organ systems.

**Subcellular level:** primary cilium / basal body and intraflagellar transport machinery (IFT57-dependent anterograde/retrograde transport); cell-cell junctions (VE-cadherin stabilization, per the 2025 review).

**Localization/laterality:** cardiac laterality defects (via ciliary left-right organizer dysfunction) can produce complex, sometimes asymmetric heart malformations; craniofacial and digital anomalies are typically bilateral/symmetric.

**Suggested UBERON terms:** UBERON:0000948 (heart), UBERON:0004134 (cardiac outflow tract), UBERON:0001690 (ear), UBERON:0004674 (upper eyelid), UBERON:0002102 (forelimb digit), UBERON:0001851 (cortex), UBERON:0002037 (cerebellum), UBERON:0002037 (meninges — UBERON:0002360).

---

## 8. Temporal Development

- **Onset:** congenital/antenatal to neonatal in most cases; Orphanet lists onset as "antenatal or neonatal period." Prenatal ultrasound abnormalities (cystic hygroma, 2-vessel cord, cardiac defects) are detectable in a subset of pregnancies.
- **Onset pattern:** for the structural anomalies, essentially present at birth (congenital); developmental delay becomes apparent through infancy/early childhood; some patients show developmental **regression** rather than purely static delay.
- **Progression:** variable — most features are static congenital malformations, but neurodevelopmental and orthopedic/joint manifestations (e.g., degenerative joint disease, avascular necrosis reported in an adult) can be progressive over decades. Growth deficiency and short stature persist through childhood.
- **Disease course pattern:** predominantly a static malformation syndrome with an added chronic, non-progressive-to-mildly-progressive neurodevelopmental course; seizures, when present, may be episodic.
- **Critical periods:** the antenatal/neonatal period is the critical window for detecting and managing life-threatening cardiac defects; early childhood is critical for developmental/rehabilitative intervention.
- **Adult natural history:** essentially undescribed until the first Korean adult case (36-year-old, first reported adult with long-term follow-up), which revealed previously unrecognized adult complications — progressive aortic root aneurysm requiring surgical repair, and severe undiagnosed OSA — underscoring that "long-term clinical findings for patients with CAFDADD syndrome remain unknown" for the largely pediatric literature to date ([PMC11011995](https://pmc.ncbi.nlm.nih.gov/articles/PMC11011995/)).

---

## 9. Inheritance and Population

- **Epidemiology:** Orphanet lists prevalence as **<1/1,000,000** — an ultra-rare disorder. As of the most recent literature review (2024), **58–69 patients** have been published worldwide since the first description in 2018.
- **Inheritance pattern:** **Autosomal dominant.** The overwhelming majority of cases are **de novo**; rare inherited transmission has been documented, notably in isolated CHD-only presentations with unaffected carrier parents.
- **Penetrance:** appears high/complete for de novo classic CAFDADD presentations, but **incomplete penetrance** is documented for some inherited variants (asymptomatic parents transmitting pathogenic alleles), and ClinGen notes overall penetrance status as formally "unknown."
- **Expressivity:** markedly **variable** — even the recurrent p.Arg655Gln variant produces a range of severity across unrelated patients; a 2025 case report specifically describes "A Patient With TRAF7-Related Neurodevelopmental Disorder Without Developmental Delay or Intellectual Disability" (Fukuda et al., *Congenital Anomalies* 2025), further extending the phenotypic floor of the spectrum.
- **Genetic anticipation:** not reported/applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** documented — multiple mosaic probands reported, plus at least one mosaic parent (unaffected or subtly affected) transmitting to an affected child, which is clinically important for recurrence-risk counseling in "de novo" families.
- **Founder effects / consanguinity:** none reported; autosomal dominant de novo disorders are not typically associated with consanguinity.
- **Carrier frequency:** not applicable (dominant, not a carrier-screened recessive condition); population allele frequency of pathogenic variants is essentially zero in gnomAD.
- **Affected populations / geography:** cases reported across diverse populations and geographies (North America, Europe, Korea [first Korean case, 2024], reported African American family — [PMID:37067385](https://pubmed.ncbi.nlm.nih.gov/37067385/)); no evidence of founder or ethnically restricted variants — the disorder appears to be pan-ethnic, ascertainment-limited by access to exome/genome sequencing.
- **Sex ratio:** not clearly skewed in reported cohorts; no formal sex-ratio statistic has been published (autosomal, so no inherent sex bias expected).
- **Age distribution:** literature is heavily skewed toward pediatric ascertainment, since patients typically present in infancy/childhood for developmental and cardiac evaluation; the adult literature is essentially limited to isolated case reports.

---

## 10. Diagnostics

**Clinical recognition:** suspected based on the combination of blepharophimosis/ptosis, congenital heart defect, digital anomalies, and developmental delay — overlapping differentials must be excluded (see below).

**Genetic testing (primary diagnostic modality):**
- **Exome sequencing (WES)** or **genome sequencing (WGS)**, typically as a **trio** (proband + parents) to establish de novo status, is the standard approach used in essentially all published cases (Tokita 2018, Castilla-Vallmanya 2020, subsequent case series).
- **Targeted gene panels** for multiple-congenital-anomaly/intellectual-disability syndromes, or for CHD-specific panels (TRAF7 is listed as a CHD gene by CHDgene — [chdgene.victorchang.edu.au/gene/84231](https://chdgene.victorchang.edu.au/gene/84231)), can capture TRAF7.
- **Single-gene TRAF7 sequencing** is reasonable when the clinical gestalt (especially blepharophimosis + CHD + digital anomaly) is highly suggestive.
- **Chromosomal microarray (CMA)/karyotype:** not causally informative (CAFDADD is not a CNV/chromosomal disorder) but often performed first-line to exclude other etiologies in the diagnostic workup of multiple congenital anomalies.
- **Mosaicism detection:** given documented mosaic cases, deep/high-coverage sequencing or targeted re-analysis of parental samples may be warranted when a "de novo" variant is found, to refine recurrence-risk counseling.

**Clinical/imaging tests:**
- Echocardiography for cardiac defect characterization (essential at diagnosis and for long-term surveillance, given the adult case's late aortic root aneurysm)
- Brain MRI (cerebral/cerebellar atrophy, ventriculomegaly/hydrocephalus, tethered cord evaluation with spinal MRI)
- Audiology (sensorineural hearing loss is near-universal)
- Ophthalmologic exam (optic atrophy, glaucoma, blepharophimosis/ptosis assessment)
- Sleep study (given the high burden of OSA reported, especially in adults)
- Skeletal survey/orthopedic evaluation for digital, spinal, and joint anomalies

**Differential diagnosis** (per the Korean case report and general phenotype overlap):
- **Loeys-Dietz syndrome** (TGFBR1/TGFBR2) — most phenotypically similar for aortic root involvement
- **Marfan syndrome** (FBN1) — aortic root dilation overlap
- **Ehlers-Danlos syndrome** (COL3A1/COL5A1/COL5A2)
- **Blepharophimosis-ptosis-epicanthus inversus syndrome (BPES)**, given the prominence of blepharophimosis
- **Ohdo syndrome** spectrum (per the case-report title referencing this differential, [PMC8428514](https://pmc.ncbi.nlm.nih.gov/articles/PMC8428514/))
- RASopathies (Noonan spectrum) given craniofacial/cardiac overlap, given TRAF7's convergence on MAPK/ERK signaling

**Screening:** no population-based newborn or carrier screening exists or is warranted given the ultra-rare, predominantly de novo nature of the disorder.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** no formal survival statistics (e.g., 5-/10-year survival rates) have been published; mortality risk is presumed to correlate with **severity of the congenital heart defect** (complex lesions such as HLHS, truncus arteriosus, and pulmonary/tricuspid atresia carry the highest early-life risk), consistent with general CHD outcome literature, though CAFDADD-specific mortality figures are not reported in the literature reviewed.
- **Morbidity:** driven primarily by (1) cardiac defect severity, (2) global developmental delay/intellectual disability (functional/communicative impact), (3) sensorineural hearing loss, and (4) orthopedic complications (contractures, scoliosis, and in the one documented adult, degenerative joint disease with avascular necrosis).
- **Adult natural history:** essentially a data gap — "most investigated patients...have been pediatric, and long-term clinical findings...remain unknown," per the first adult (Korean) case report. That case revealed a previously unrecognized progressive complication (aortic root aneurysm) and severe untreated OSA, suggesting under-recognized adult morbidity.
- **Recovery/functional potential:** with early developmental support, motor rehabilitation, and multidisciplinary management, functional outcomes can be optimized, though intellectual disability is generally persistent.
- **Prognostic factors:** severity/type of cardiac lesion at diagnosis is the most clinically actionable prognostic variable; no molecular/genotype-based prognostic biomarker has been validated (no clear genotype-phenotype severity correlation established, even for the recurrent p.Arg655Gln hotspot).
- **Tumor-risk prognosis:** whether germline CAFDADD carriers face an elevated lifetime meningioma (or other TRAF7-associated tumor) risk analogous to the somatic-mutation tumor spectrum is an **open, unresolved question** flagged explicitly in the primary literature (one of the original 7 patients developed a meningioma).

---

## 12. Treatment

There are **no disease-specific or targeted pharmacotherapies** for CAFDADD; management is supportive, multidisciplinary, and organ-system-directed.

- **Cardiac management:** standard congenital cardiology/cardiac surgery per defect type — e.g., surgical repair of septal defects, valve repair/replacement, and in the documented adult case, **Bentall procedure** (aortic root/valve replacement) for aneurysmal aortic root disease. (NCIT: C15329 Surgical Procedure; more specifically, congenital heart surgery falls under NCIT:C15329 with cardiovascular specificity as available.)
- **Respiratory/sleep management:** **CPAP** for obstructive sleep apnea, which provided "significant symptom relief" in the adult case; ENT evaluation for airway anatomy contributing to OSA.
- **Neurodevelopmental/rehabilitative care:** early intervention, physical therapy, occupational therapy, speech-language therapy (with alternative/augmentative communication strategies given prominent expressive-language impairment) (NCIT:C15302 Physical Therapy; NCIT:C159273 Speech Therapy; NCIT:C121351 Occupational Therapy).
- **Audiology:** hearing aids/cochlear implantation evaluation for sensorineural hearing loss as indicated.
- **Ophthalmology:** management of ptosis/blepharophimosis (surgical correction as needed), monitoring for glaucoma and optic atrophy.
- **Orthopedics:** management of contractures, scoliosis, and joint disease (e.g., avascular necrosis) as they arise.
- **Psychology/mental health follow-up:** recommended given autism-spectrum features and the psychosocial burden of a multisystem rare disease, per the 2024 literature review's care recommendations.
- **Genetic counseling** (NCIT:C15240 Genetic Counseling): essential given documented mosaicism and rare inherited transmission with incomplete penetrance — recurrence risk counseling should account for possible parental mosaicism even after a "de novo" finding.
- **Experimental/targeted therapy:** none in clinical trials specific to CAFDADD; the elucidation of the **MAPK/ERK hypofunction** and **ciliary dysfunction** mechanisms is mechanistically informative but has not yet translated into a targeted therapeutic strategy (e.g., no MEK-pathway modulator trials reported for CAFDADD, in contrast to some RASopathies).
- **Surveillance considerations:** given the somatic TRAF7-meningioma link, some authors raise (without yet establishing formal guidelines) whether germline carriers warrant longer-term oncologic surveillance — this remains an open clinical question rather than an established recommendation.

**Overarching management recommendation** (per the 2024 pooled literature review): "comprehensive, multidisciplinary clinical assessment for each patient," with regular medical evaluations, targeted therapeutic interventions per organ system, and long-term monitoring for disease progression and complications.

---

## 13. Prevention

As a predominantly de novo monogenic disorder, there is **no primary prevention** strategy analogous to vaccination or risk-factor modification.

- **Secondary prevention (early detection):** prenatal ultrasound can flag suggestive findings (cystic hygroma, structural cardiac anomalies, 2-vessel cord) prompting diagnostic genetic testing (prenatal exome sequencing or postnatal confirmatory testing).
- **Genetic counseling:** for families with a previously affected child, counseling should address the **empiric recurrence risk**, factoring in the possibility of **parental germline mosaicism** even when the proband's variant initially appears de novo — informing decisions about prenatal diagnosis or preimplantation genetic testing (PGT-M) in a subsequent pregnancy.
- **Tertiary prevention:** the multidisciplinary surveillance/management program described in Section 12 functions as tertiary prevention — averting or minimizing complications (aortic aneurysm rupture, severe OSA sequelae, orthopedic deterioration) in individuals already diagnosed.
- **Screening:** no population-level newborn or carrier screening program exists or is indicated for this ultra-rare, predominantly de novo disorder.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Homo sapiens (NCBITaxon:9606) is the only species in which the CAFDADD *clinical syndrome* has been described. No naturally occurring veterinary/companion-animal disease attributable to TRAF7 variants has been reported in OMIA or the veterinary literature surveyed.
- **Orthologous gene:** Traf7 orthologs exist in mouse, zebrafish, and *Xenopus* (used experimentally — see Section 15) and are highly conserved, particularly at the WD40 repeat residues mutated in human disease.
- **Comparative biology:** the developmental-biology literature (zebrafish, *Xenopus* knockdown) demonstrates strong evolutionary conservation of TRAF7's role in cardiac looping, pharyngeal arch/neural crest development, and ciliary left-right patterning — directly informing the proposed human disease mechanism (Section 6).
- **Transmission:** not applicable — CAFDADD is a non-communicable, purely genetic disorder with no zoonotic or cross-species transmission potential.

---

## 15. Model Organisms

No germline knock-in mouse model faithfully reproducing the CAFDADD phenotype has been reported to date; **CHDgene explicitly notes "No mouse models currently available in MGI"** for TRAF7 ([chdgene.victorchang.edu.au/gene/84231](https://chdgene.victorchang.edu.au/gene/84231)). Instead, the field has relied on knockdown/morphant approaches in lower vertebrates:

- **Zebrafish (*Danio rerio*) morphants** (TRAF7 knockdown): show **significant heart looping defects** at 36 hours post-fertilization, **disorganized pharyngeal arches**, and **reduced *sox10* expression** (indicating impaired neural crest development); ciliary transport (both anterograde and retrograde) is severely impaired in morphant embryos ([PNAS 2023, PMC10120005](https://pmc.ncbi.nlm.nih.gov/articles/PMC10120005)).
- **Xenopus (frog) knockdown models:** recapitulate cardiac dysfunction (abnormal looping, pericardial edema, ventricular pump dysfunction), left-right patterning defects (abnormal/bilateral *pitx2c* expression linked to reduced ciliary number at the left-right organizer), disrupted neural crest marker expression (*Sox10*, *Twist*), and ciliopathy-like features including **severe hydrocephaly** and **renal cystic pathology**.
- **Related mouse model (indirect/analogous):** **ERK2 conditional knockout mice** show a cardiovascular/craniofacial phenotype described as "highly consistent" with human CAFDADD features, supporting the MAPK-hypofunction arm of the proposed mechanism — though this is an ERK2 model, not a direct Traf7 model, and should be interpreted as mechanistic-pathway support rather than a disease-specific model.
- **In vitro models:** patient-derived **dermal fibroblasts** have been used for transcriptomic profiling (Castilla-Vallmanya et al. 2020); HEK293/heterologous overexpression systems have been used to demonstrate the ERK1/2 phosphorylation defect (Tokita et al. 2018) and the TRAF7–MEKK3/IFT57 dominant-negative interaction biochemistry (PNAS 2023).

**Model limitations:** the absence of a genetically faithful mammalian (mouse) knock-in model is a significant gap — current zebrafish/*Xenopus* morphant systems capture cardiac, craniofacial, and ciliary phenotypes but cannot model the neurodevelopmental/intellectual-disability component of CAFDADD, nor long-term postnatal outcomes (e.g., adult aortic aneurysm progression, tumor risk) captured only in human case reports.

**Applications:** these models have been most useful for dissecting the **dominant-negative biochemical mechanism** (heterodimerization, MEKK3 disruption) and the **neural crest/ciliary developmental basis** of the pleiotropic human phenotype, directly bridging the germline-syndromic and somatic-oncogenic faces of TRAF7 biology.

---

## Summary of Key Ontology Term Suggestions

| Category | Suggested terms |
|---|---|
| MONDO | MONDO:0032572 (CAFDADD) |
| OMIM | #618164 (phenotype); *606692 (TRAF7 gene) |
| Orphanet | ORPHA:592570 |
| HGNC | HGNC:20456 (TRAF7) |
| HP (phenotypes) | HP:0000581 Blepharophimosis; HP:0000508 Ptosis; HP:0000286 Epicanthus; HP:0001629 VSD; HP:0001631 ASD; HP:0001643 PDA; HP:0031650 Bicuspid aortic valve; HP:0004385 DORV; HP:0001263 Global developmental delay; HP:0001249 Intellectual disability; HP:0001250 Seizure; HP:0000407 Sensorineural hearing loss; HP:0000648 Optic atrophy; HP:0001824 Weight loss / HP:0004322 Short stature; HP:0001180 Joint contracture; HP:0000470 Short neck; HP:0000768 Pectus carinatum |
| GO (BP) | GO:0000165 MAPK cascade; GO:0060271 Cilium assembly; GO:0007368 Determination of L/R symmetry; GO:0014032 Neural crest cell development |
| GO (MF) | GO:0061630 Ubiquitin protein ligase activity |
| CL | CL:0011012 Neural crest cell; CL:0000057 Fibroblast |
| UBERON | UBERON:0000948 Heart; UBERON:0004134 Cardiac outflow tract; UBERON:0004674 Eyelid; UBERON:0002360 Meninges |
| NCIT (treatment) | NCIT:C15329 Surgical Procedure; NCIT:C15302 Physical Therapy; NCIT:C15240 Genetic Counseling; NCIT:C121351 Occupational Therapy |

---

## Sources

- [Entry - #618164 - CARDIAC, FACIAL, AND DIGITAL ANOMALIES WITH DEVELOPMENTAL DELAY; CAFDADD - OMIM](https://omim.org/entry/618164)
- [Entry - *606692 - TNF RECEPTOR-ASSOCIATED FACTOR 7; TRAF7 - OMIM](https://omim.org/entry/606692)
- [Orphanet: TRAF7-associated heart defect-digital anomalies-facial dysmorphism-motor and speech delay syndrome (ORPHA:592570)](https://www.orpha.net/en/disease/detail/592570)
- [GARD: TRAF7-associated heart defect-digital anomalies-facial dysmorphism-motor and speech delay syndrome](https://rarediseases.info.nih.gov/diseases/22370/traf7-associated-heart-defect-digital-anomalies-facial-dysmorphism-motor-and-speech-delay-syndrome)
- [GARD: Cardiac anomalies-developmental delay-facial dysmorphism syndrome (MED13L — distinct disease, excluded)](https://rarediseases.info.nih.gov/diseases/17588/cardiac-anomalies-developmental-delay-facial-dysmorphism-syndrome)
- Tokita MJ et al. "De Novo Missense Variants in TRAF7 Cause Developmental Delay, Congenital Anomalies, and Dysmorphic Features." Am J Hum Genet. 2018 Jul 5;103(1):154-162. [PMID:29961569](https://pubmed.ncbi.nlm.nih.gov/29961569/) / [PMC6035372](https://pmc.ncbi.nlm.nih.gov/articles/PMC6035372/)
- Castilla-Vallmanya L, Selmer KK, Dimartino C, et al. "Phenotypic spectrum and transcriptomic profile associated with germline variants in TRAF7." Genet Med. 2020. [PMID:32376980](https://pubmed.ncbi.nlm.nih.gov/32376980/) / [nature.com](https://www.nature.com/articles/s41436-020-0792-7)
- "The First Korean Case with Cardiac, Facial, and Digital Anomalies with Developmental Delay Caused by De Novo TRAF7 p.Arg655Gln Variant." [PMC11011995](https://pmc.ncbi.nlm.nih.gov/articles/PMC11011995/)
- "Expanding the phenotypic spectrum of TRAF7 syndrome: report of eleven new cases and literature review." medRxiv 2023.12.13.23299272 / Pediatric Neurology 2024. [medRxiv](https://www.medrxiv.org/content/10.1101/2023.12.13.23299272v1.full) / [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0887899424000833)
- Mishra-Gorur K et al. "Pleiotropic role of TRAF7 in skull-base meningiomas and congenital heart disease." PNAS 2023. [PMID:37043537](https://pubmed.ncbi.nlm.nih.gov/37043537/) / [PMC10120005](https://pmc.ncbi.nlm.nih.gov/articles/PMC10120005)
- "The spectrum of heart defects in the TRAF7-related multiple congenital anomalies-intellectual disability syndrome." PNAS 121(12):e2317601121, 2024. [PMID:38466853 (Reply to Pisan et al.)](https://pubmed.ncbi.nlm.nih.gov/38466853/) / [pnas.org](https://www.pnas.org/doi/10.1073/pnas.2317601121)
- Orock A et al. "TRAF7 in signaling and disease: emerging mechanisms and clinical implications." Mol Med. 2025. [PMID:41372821](https://pubmed.ncbi.nlm.nih.gov/41372821/) / [PMC12801879](https://pmc.ncbi.nlm.nih.gov/articles/PMC12801879)
- "Loss-of-Function Mutations in TRAF7 and KLF4 Cooperatively Activate RAS-Like GTPase Signaling and Promote Meningioma Development." Cancer Res. 2021. [aacrjournals.org](https://aacrjournals.org/cancerres/article/81/16/4218/670292/)
- "Single-cell DNA sequencing reveals order of mutational acquisition in TRAF7/AKT1 and TRAF7/KLF4 mutant meningiomas." [PMC9468091](https://pmc.ncbi.nlm.nih.gov/articles/PMC9468091/)
- "TRAF7 somatic mosaicism in a patient with bilateral optic nerve sheath meningiomas." [PMID:35733823](https://pubmed.ncbi.nlm.nih.gov/35733823/)
- "Novel mosaic TRAF7 likely pathogenic variant in an African American family." [PMID:37067385](https://pubmed.ncbi.nlm.nih.gov/37067385/)
- CHDgene: TRAF7 gene page. [chdgene.victorchang.edu.au/gene/84231](https://chdgene.victorchang.edu.au/gene/84231)
- ClinGen TRAF7 curation results (gene-disease validity and dosage sensitivity). [search.clinicalgenome.org/kb/genes/HGNC:20456](https://search.clinicalgenome.org/kb/genes/HGNC:20456)
- "New findings better elucidate TRAF7 syndrome, a neurological and developmental disease" (Univ. Barcelona / medicalxpress summary of 2024 literature review). [medicalxpress.com](https://medicalxpress.com/news/2024-04-elucidate-traf7-syndrome-neurological-developmental.html)
- Fukuda et al. "A Patient With TRAF7-Related Neurodevelopmental Disorder Without Developmental Delay or Intellectual Disability." Congenital Anomalies 2025. [onlinelibrary.wiley.com](https://onlinelibrary.wiley.com/doi/abs/10.1111/cga.70030)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 6 |
| Quoted claims found in source | 4 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 16 |
| On topic | 13 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:37043537` *(abstract only)*: "low concentrations of mutant TRAF7...sufficient to disrupt the interaction of WT TRAF7 with MEKK3"
  - closest text in source: "Somatic and inherited mutations disrupt TRAF7-IFT57 interactions leading to cilia degradation"
- `PMC:PMC10120005` *(abstract only)*: "low concentrations of mutant TRAF7...sufficient to disrupt the interaction of WT TRAF7 with MEKK3"
  - closest text in source: "Somatic and inherited mutations disrupt TRAF7-IFT57 interactions leading to cilia degradation"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 53 |
| Resolved | 49 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 27 |
| Terms named correctly | 18 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032572` (4 mentions) - the report calls it "MONDO", "CAFDADD"; MONDO calls it **cardiac, facial, and digital anomalies with developmental delay**
- `HP:0031650` (2 mentions) - the report calls it "bicuspid aortic valve"; HP calls it **Abnormal atrioventricular valve physiology**
- `HP:0004385` (2 mentions) - the report calls it "double outlet right ventricle"; HP calls it **Protracted diarrhea**
- `CL:0002518` (1 mention) - the report calls it "cardiac endothelial cell — outflow tract context"; CL calls it **kidney epithelial cell**
- `UBERON:0004134` (2 mentions) - the report calls it "cardiac outflow tract"; UBERON calls it **proximal tubule**
- `UBERON:0004674` (2 mentions) - the report calls it "upper eyelid"; UBERON calls it **facial nerve root**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0001180` (obsolete Hand oligodactyly) (2 mentions) - replaced by `HP:0009380`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0007266` (1 mention) - the report calls it "Rho protein signal transduction — via MEKK3 axis"; GO calls it **Rho protein signal transduction**
- `UBERON:0002102` (1 mention) - the report calls it "forelimb digit"; UBERON calls it **forelimb**
- `NCBITaxon:9606` (1 mention) - the report calls it "Taxonomy:** Homo sapiens"; NCBITaxon calls it **Homo sapiens**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0032572` - called "MONDO", "CAFDADD"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.