---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-23T03:39:21.885515'
end_time: '2026-09-23T03:44:06.190406'
duration_seconds: 284.3
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Garg-Mishra Progeroid Syndrome
  mondo_id: MONDO:0957953
  category: Mendelian
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
  web_search_requests: 16
  num_turns: 32
  total_cost_usd: 1.605405
  session_id: 45ce5f1a-6721-5dd9-af0a-cb3620796386
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 17
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 7
  validator_version: 0.2.1
term_validation:
  total_terms: 48
  verified: 44
  not_found: 1
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.022
  labels_checked: 31
  labels_matching: 19
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: HP:0000238
    reported_labels:
    - Wide fontanel
    ontology_label: Hydrocephalus
  - term_id: GO:0008637
    reported_labels:
    - "apoptotic mitochondrial changes \u2014 if relevant to downstream cell stress,\
      \ not directly demonstrated"
    ontology_label: apoptotic mitochondrial changes
  - term_id: CL:0000138
    reported_labels:
    - chondrocyte, growth-plate relevance
    ontology_label: chondrocyte
  - term_id: CL:0000057
    reported_labels:
    - fibroblast, the primary cell type studied
    ontology_label: fibroblast
  - term_id: UBERON:0002544
    reported_labels:
    - growth plate cartilage
    ontology_label: digit
  - term_id: UBERON:0001676
    reported_labels:
    - mandible
    ontology_label: occipital bone
  - term_id: GO:0001401
    reported_labels:
    - "SAM complex \u2014 related import machinery"
    ontology_label: SAM complex
  - term_id: NCIT:C1502
    reported_labels:
    - Somatropin
    ontology_label: Fiber
  labels_variant: 4
  unresolved_terms:
  - HP:0005440
  obsolete_terms:
  - term_id: GO:0006626
    ontology_label: obsolete protein targeting to mitochondrion
    replaced_by: GO:0070585
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Garg-Mishra Progeroid Syndrome
- **MONDO ID:** MONDO:0957953 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Garg-Mishra Progeroid Syndrome** covering all of the
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

This is excellent, substantially more severe than the first case — important for the phenotypic spectrum. I now have enough for a comprehensive report. Let me do a couple more targeted checks: current OMIM inheritance/phenotype MIM number format, and confirm there's no treatment/prevention literature beyond what's found, and check Orphanet/GeneReviews coverage status.

# Garg-Mishra Progeroid Syndrome (GMPGS): A Comprehensive Research Report

## Executive Summary

Garg-Mishra Progeroid Syndrome (GMPGS; OMIM #620601) is an ultra-rare autosomal recessive mitochondrial disorder first described in 2022 and formally named by the McKusick-Nathans Institute of Genetic Medicine (Johns Hopkins/OMIM) in January 2025 in honor of its discoverers, Abhimanyu Garg, M.D. (UT Southwestern Medical Center) and Prashant Mishra, M.D., Ph.D. (UT Southwestern / Children's Medical Center Research Institute). The syndrome is caused by biallelic hypomorphic (partial loss-of-function) variants in **TOMM7** (*translocase of outer mitochondrial membrane 7*; OMIM *607980), the first human disease ever attributed to a subunit of the mitochondrial outer-membrane protein-import (TOM) complex. Only a handful of patients have been reported worldwide (as of this writing: three independently ascertained probands plus two deceased affected siblings), making this among the rarest described Mendelian disorders. No MONDO, Orphanet, or GeneReviews entry could be confirmed to exist yet for this newly named condition (see Section 1 caveats below).

---

## 1. Disease Information

**Overview.** GMPGS is a syndromic form of severe postnatal growth failure/proportionate dwarfism with progeroid (prematurely-aged) facial appearance, craniofacial dysmorphism (mandibular hypoplasia), severe ophthalmologic abnormalities (high hyperopia, microphthalmia/nystagmus), partial lipodystrophy, developmental delay, and in the most severe reported case, early death. It results from biallelic partial loss-of-function variants in *TOMM7*, which disrupt assembly/stability of the TOM (translocase of the outer mitochondrial membrane) protein-import complex and cause a distinctive mitochondrial bioenergetic uncoupling phenotype rather than classical oxidative-phosphorylation failure.

**Key identifiers:**
| Resource | Identifier | Notes |
|---|---|---|
| OMIM (phenotype) | **#620601** | "Garg-Mishra progeroid syndrome (GMPGS)" |
| OMIM (gene) | ***607980** | TOMM7 |
| HGNC | **21648** (TOMM7) | Locus 7p15.3 |
| Chromosome location | 7p15.3 (GRCh38: chr7:22,812,628–22,822,849, minus strand) | |
| MONDO | Not confirmed available — searches for a dedicated GMPGS MONDO term did not resolve a live record as of Sept 2026; the user-supplied MONDO:0957953 could not be independently verified against Monarch Initiative and should be confirmed before use in curation | flag for verification |
| KEGG DISEASE | **H02768** (Japanese: Garg-Mishra 早老症候群) | Classified under 先天奇形 (congenital malformation); cross-referenced to ICD-11 LD2B "syndrome with premature aging appearance as a major feature" |
| GeneReviews / Orphanet | No dedicated chapter identified | Condition is too newly named/characterized (named Jan 2025) to have an established chapter |
| ICD-11 | LD2B (via KEGG mapping) — "Syndrome with premature aging appearance as a major feature" | not independently confirmed on WHO ICD-11 browser |

**Synonyms / alternative names:** Garg-Mishra progeroid syndrome; GMPGS; TOMM7-associated autosomal recessive progeroid syndrome; TOMM7-related progeroid syndrome / short stature syndrome.

**Data provenance.** All currently available clinical information derives from a small number of **individual patient case reports** (n=3 published probands, plus 2 deceased affected siblings referenced within those reports) — there is no aggregated disease-level registry, cohort study, or epidemiological database entry for this condition given its very recent description.

*Sources:* [OMIM #620601](https://omim.org/entry/620601); [OMIM *607980](https://omim.org/entry/607980); [KEGG DISEASE H02768](https://www.kegg.jp/entry/ds_ja:H02768); [MalaCards: Garg-Mishra Progeroid Syndrome](https://www.malacards.org/card/garg_mishra_progeroid_syndrome); [UT Southwestern CT Plus](https://www.utsouthwestern.edu/ctplus/honors-awards/gene-variant-garg.html)

---

## 2. Etiology

**Disease causal factor:** GMPGS is a monogenic, autosomal recessive mitochondrial disorder. There is no reported environmental, infectious, or multifactorial contribution — all reported cases are attributable to biallelic (homozygous, in all reported cases so far) hypomorphic missense (or, for the allelic-but-distinct Leigh syndrome phenotype, a splice-site null) variant in *TOMM7*.

**Genetic risk factors (causal variants):**
1. **c.86C>T (p.Pro29Leu / P29L)** — the index (founder-region) variant reported by Garg et al. (2022, *J Clin Invest*, PMID 36282599) in a 21-year-old male of Chinese ancestry, and independently confirmed in a second, unrelated 2-year-old Han Chinese boy (American Journal of Case Reports, PMID 41460760). Minor allele frequency in population databases: **0.000048**, observed only in East Asian subpopulations (Korean, Japanese) in gnomAD-type reference panels — consistent with a rare, possibly regional founder allele. GERP++ = 6.07; CADD = 34 (highly deleterious in silico prediction).
2. **c.73T>C (p.Trp25Arg / W25R)** — reported by Young, Batkovskyte, Kitamura et al. (2023, *HGG Advances*, PMID 36299998) in a Japanese boy with non-consanguineous parents; homozygous in the proband, heterozygous (carrier, unaffected) in both parents.
3. A distinct, more severe **biallelic canonical splice-site variant, c.153-2A>C** (intron 2), reported by Yeole et al. (2025, *AJMG Part A*, PMID 39333057) in a consanguineous Indian family, causes aberrant splicing/frameshift and a **lethal Leigh-syndrome phenotype** rather than GMPGS — see the Genotype–Phenotype note below.

**Population/founder considerations:** All GMPGS-causing missense alleles reported to date arise in East Asian probands (Chinese, Han Chinese, Japanese); P29L is essentially private to East Asian gnomAD subpopulations. No consanguinity was reported in the JCI index family or the HGG Advances family (W25R), but both are homozygous — suggesting either founder-allele co-inheritance or a mutational hotspot. The AJCR second case (Han Chinese boy, P29L) is explicitly noted to have **consanguineous parents**.

**Protective factors:** None reported; no data available on modifier alleles or protective variants for this ultra-rare condition.

**Gene-environment interactions:** None reported in the literature to date; the phenotype in every case is explained by the genotype alone, with no environmental co-factor implicated.

**Genotype–phenotype correlation (critical mechanistic point):** *TOMM7* displays striking **allelic heterogeneity with a severity gradient tied to variant type**:
- Hypomorphic missense variants disrupting the TOMM7–TOMM40/TOMM22 transmembrane interaction (P29L, W25R) → **partial loss of TOM-complex assembly**, producing the comparatively milder, chronic GMPGS phenotype (survivable into adulthood in the mildest case).
- A canonical splice/null variant (c.153-2A>C) causing frameshift/loss of functional protein → **near-complete loss of function**, producing a severe, early-lethal **Leigh syndrome** phenotype (mitochondrial encephalopathy, lactic acidosis, death in infancy) rather than the progeroid GMPGS presentation.

This is analogous to other TOM/TIM-complex and mitochondrial-import disorders where allele "dosage" of residual function determines whether the phenotype is a chronic growth/metabolic syndrome versus an acute, fatal encephalopathy.

*Sources:* [JCI 156864](https://www.jci.org/articles/view/156864); [HGG Advances PMC9589026](https://pmc.ncbi.nlm.nih.gov/articles/PMC9589026/); [AJMG Part A / Yeole et al. PMC7617585 summary](https://pmc.ncbi.nlm.nih.gov/articles/PMC7617585/); [AJCR abstract #950967](https://amjcaserep.com/abstract/full/idArt/950967)

---

## 3. Phenotypes

Phenotype data are pooled across the three reported GMPGS probands (JCI index case, HGG Advances case, AJCR case); frequencies below are qualitative given the extremely small n.

| Phenotype category | Feature | Reported in | Suggested HPO term |
|---|---|---|---|
| Growth (postnatal) | Severe postnatal growth retardation / proportionate short stature (height/weight <3rd percentile; Z-scores as low as −5.4 for height, −3.6 for weight at 15 months in the severe case) | 3/3 | HP:0008897 (Postnatal growth retardation); HP:0004322 (Short stature) |
| Growth | Relative macrocephaly | JCI case | HP:0004482 (Relative macrocephaly) |
| Craniofacial | Triangular facies, broad forehead | JCI case | HP:0000322 / HP:0000341 |
| Craniofacial | Severe **mandibular hypoplasia** (micrognathia), dental crowding | JCI, AJCR cases | HP:0000347 (Micrognathia) |
| Craniofacial | Prominent nasal bridge, bulbous nose | JCI case | HP:0000426 / HP:0000414 |
| Craniofacial | Underdeveloped facial bones, large neurocranium, open anterior fontanel (severe case) | HGG Advances case | HP:0000238 (Wide fontanel) |
| Ophthalmologic | **High hyperopia** (up to +10.75 D) | JCI case | HP:0000540 (Hyperopia) |
| Ophthalmologic | **Microphthalmia** (bilateral, axial length 16.8 mm) | JCI case (& news coverage) | HP:0000568 (Microphthalmia) |
| Ophthalmologic | Pendular **nystagmus**; poor visual acuity (3/60) | JCI, HGG Advances cases | HP:0012043 (Pendular nystagmus) |
| Ophthalmologic | Macular scarring | AJCR case | HP:0007754-like (macular scar; exact HPO TBD) |
| Body composition | **Partial lipodystrophy** / loss of subcutaneous fat, "marked muscularity" | 3/3 | HP:0009125 (Lipodystrophy); HP:0009381 (Partial lipodystrophy — verify exact term) |
| Body composition | Café-au-lait spots, coarse eyebrows, sparse hair/frontal hair recession | JCI case | HP:0000957 (Cafe-au-lait spot) |
| Neurodevelopmental | **Developmental delay** / learning disability | 2–3/3 | HP:0001263 (Global developmental delay) |
| Neurologic | Muscular hypotonia, "frog-leg posture," poor head control | HGG Advances (severe case) | HP:0001252 (Hypotonia) |
| Skeletal | Narrow thorax, broad hands, small nails; flattened vertebrae, gracile long bones (severe case) | HGG Advances case | HP:0005440 / HP:0001156 / HP:0004325 |
| Skeletal | No significant bone-age delay (mild case) | JCI case | — |
| Hepatic | Microvesicular hepatic steatosis (at autopsy) | HGG Advances (severe, fatal case) | HP:0001397 (Hepatic steatosis) |
| Laboratory | Elevated serum LDH; mildly elevated alkaline phosphatase; mildly increased WBC | HGG Advances, JCI cases | — |
| Cardiac | Mild mitral regurgitation; mild LV dilation (no structural defect) | JCI case | HP:0031653 / HP:0001635 |
| Lifespan | Shortened lifespan — one affected sibling of the index case died at age 10 during a febrile illness with respiratory symptoms; the HGG Advances proband died at 2.7 years of pneumonia/respiratory failure | 2/3 cases (severe end of spectrum) | HP:0001522 (Death in childhood) |

**Onset/progression:** Growth failure is evident from early childhood (postnatal, not congenital — normal birth weight/length reported in both detailed cases), becoming apparent by approximately age 6 in the mildest reported case and much earlier (by 15 months) in the severe HGG Advances case. Severity appears variant/allele-dependent rather than strictly progressive in the surviving index patient, who at age 21 was described as "doing well" with no Parkinsonism or neurological decline.

**Quality of life:** Not formally assessed with standardized instruments (no EQ-5D/SF-36 data reported); qualitatively, the index patient (age 21) retained verbal communication ability despite significant learning disability, while the more severely affected infant/toddler cases had substantial early mortality.

*Sources:* [JCI 156864](https://www.jci.org/articles/view/156864); [HGG Advances PMC9589026](https://pmc.ncbi.nlm.nih.gov/articles/PMC9589026/); [AJCR abstract](https://amjcaserep.com/abstract/full/idArt/950967); [UT Southwestern CT Plus](https://www.utsouthwestern.edu/ctplus/honors-awards/gene-variant-garg.html)

---

## 4. Genetic/Molecular Information

**Causal gene:** *TOMM7* (HGNC:21648; OMIM *607980), 7p15.3, encoding a 55-amino-acid, ~6.2 kDa outer-mitochondrial-membrane protein.

**Reported pathogenic variants (all recessive, biallelic):**

| Variant (cDNA) | Protein | Zygosity | Classification | Case | PMID |
|---|---|---|---|---|---|
| c.86C>T | p.Pro29Leu (P29L) | Homozygous | Pathogenic (hypomorphic) | JCI index case (21yo, Chinese ancestry); AJCR case (2yo, Han Chinese, consanguineous) | 36282599; 41460760 |
| c.73T>C | p.Trp25Arg (W25R) | Homozygous | Pathogenic (hypomorphic) | HGG Advances case (Japanese boy) | 36299998 |
| c.153-2A>C | splice site, intron 2 → frameshift | Homozygous | Pathogenic (near-null/loss-of-function) | Yeole et al. Leigh syndrome siblings (consanguineous Indian family) — **distinct phenotype, not GMPGS** | 39333057 |

**Allele frequency:** P29L MAF ≈ 0.000048, restricted to East Asian gnomAD subpopulations (no homozygotes reported in population databases, consistent with disease causation). No population-frequency data reported for W25R.

**Variant type/class:** All GMPGS-causing alleles reported to date are **missense** variants situated in/near the transmembrane α-helical domain of TOMM7, at residues (P29, W25/adjacent R24) predicted to mediate physical interaction with the core TOM-complex proteins **TOMM40** and **TOMM22**. Both P29 and the region around W25 are highly evolutionarily conserved across mammals.

**Functional consequence:** **Partial loss of function (hypomorphic)** — mutant TOMM7 protein still localizes normally to the mitochondrial outer membrane (not a trafficking defect) but shows **decreased physical interaction with TOMM40/TOMM22**, reducing TOM core-complex assembly/stability. This is explicitly distinguished from the complete loss-of-function/null allele (c.153-2A>C), which instead produces a severe Leigh-syndrome phenotype — establishing a dose-dependent genotype–phenotype relationship (see Section 2).

**Somatic vs. germline:** All variants are germline (inherited, biallelic, present in unaffected heterozygous carrier parents).

**Modifier genes:** None identified/reported.

**Epigenetic information:** None reported for this condition.

**Chromosomal abnormalities:** None — this is a single-gene point-variant disorder; a ~1 Mb region of homozygosity on chromosome 7 encompassing *TOMM7* was noted in the index proband, consistent with identity-by-descent inheritance rather than a distinct structural chromosomal lesion.

**Suggested ontology terms:** HGNC:21648 (TOMM7); GO:0006626 (protein targeting to mitochondrion); GO:0045040 (protein insertion into mitochondrial outer membrane) — as background gene-function terms for pathograph molecular-function/process nodes.

*Sources:* [JCI 156864](https://www.jci.org/articles/view/156864); [OMIM *607980](https://omim.org/entry/607980); [HGG Advances PMC9589026](https://pmc.ncbi.nlm.nih.gov/articles/PMC9589026/); [GeneCards TOMM7 (via search)](https://www.genecards.org/cgi-bin/carddisp.pl?gene=TOMM7)

---

## 5. Environmental Information

No environmental, lifestyle, or infectious contributing factors are reported for GMPGS — it is a purely monogenic disorder. The HGG Advances proband's terminal event (pneumonia/respiratory failure) and the JCI index case's sibling's terminal febrile illness appear to be **complications of underlying disease vulnerability** (possibly reduced physiologic reserve from the mitochondrial/metabolic defect) rather than independent causal environmental/infectious agents — no specific pathogen was identified as causal to the syndrome itself.

---

## 6. Mechanism / Pathophysiology

### Ordered Causal Chain (index/mild phenotype — P29L/W25R hypomorphic alleles)

1. Biallelic hypomorphic missense variant in *TOMM7* (P29L or W25R, in the transmembrane helix) **leads to** reduced physical/structural interaction between mutant TOMM7 and the TOM core-channel proteins TOMM40 and TOMM22.
2. Reduced TOMM7–TOMM40/TOMM22 interaction **results in** decreased assembly/stability of the TOM (translocase of outer mitochondrial membrane) preprotein-import complex, while overall mitochondrial protein *localization* of TOMM7 itself remains normal (i.e., this is an assembly/stability defect, not a mislocalization defect) — *inferred from proteomic and cell-biology data in the JCI report*.
3. Altered TOM-complex composition **leads to** a shift in the mitochondrial proteome: of 587 mitochondrial proteins assayed, 91 were differentially expressed — with **upregulation** of electron-transport-chain/ATP-production proteins (ATP5A, UQCRC2, SDHB, NDUFB8, TFAM) and **downregulation** of phospholipid-metabolism pathway proteins.
4. This proteomic shift **results in** a bioenergetic phenotype of **elevated basal and maximal mitochondrial oxygen consumption** in patient fibroblasts and in knock-in mouse models — but, critically, **without impairment of electron-transport-chain function** (normal responses to ETC inhibitors) — indicating a **dissociation ("uncoupling") between mitochondrial oxidation and ATP synthesis** rather than classical OXPHOS chain failure (demonstrated mechanistically in the HGG Advances mouse studies).
5. This uncoupling/hypermetabolic state **is proposed to lead to** (a) downregulated phospholipid metabolism contributing to **lipodystrophy** (reduced adipocyte size, hepatic lipid accumulation), and (b) a chronic energy-demand mismatch in high-growth tissues, manifesting as **growth-plate chondrocyte proliferation defects** → **short stature/dwarfism**, and secondarily contributing to the craniofacial (mandibular hypoplasia) and ophthalmologic phenotypes, although the precise tissue-selective mechanisms linking the bioenergetic defect to eye/facial dysmorphology remain **inferred rather than directly demonstrated**.
6. Systemic markers of mitochondrial stress (elevated **Gdf15**, **Fgf21**, phospho-AMPK) are seen in mouse models, consistent with a chronic mitochondrial-integrated-stress-response state driving the growth-failure phenotype.
7. **Branch point — allele severity determines outcome:** where the residual TOM-complex function is more severely disrupted (near-null splice variant, c.153-2A>C) rather than merely reduced (hypomorphic missense), the pathway instead **leads to** severe, early oxidative-phosphorylation failure with lactic acidosis and CNS injury (**Leigh syndrome**), rather than the chronic growth/lipodystrophy phenotype of GMPGS — i.e., the same initiating lesion class (TOM-complex dysfunction) bifurcates into two clinically distinct downstream outcomes depending on the magnitude of residual TOMM7 function.

### Detail by category

- **Molecular pathways:** Mitochondrial protein import (TOM/TIM machinery); downstream effects on oxidative phosphorylation (ETC complexes I–V) and ATP-synthase coupling; phospholipid metabolism pathway (downregulated).
- **Cellular processes:** Protein translocation across the mitochondrial outer membrane (GO:0006626 protein targeting to mitochondrion); mitochondrial respiration/oxidative phosphorylation; Parkin-dependent mitophagy — notably shown to remain **intact** despite TOMM7 P29L, indicating TOMM7's role in mitophagy (via PINK1 stabilization/VDAC2 interaction, per broader TOM-complex literature) is at least partially separable from its role in core TOM-channel assembly.
- **Protein dysfunction:** Not misfolding/aggregation — rather, a **structural interaction defect** (reduced binding to TOMM40/TOMM22) that impairs complex assembly while preserving normal subcellular localization of the mutant protein.
- **Metabolic changes:** Increased basal/maximal cellular oxygen consumption (hypermetabolic mitochondrial phenotype); dissociation of oxygen consumption from ATP synthesis (proposed complex-V/F0-F1 coupling defect, mechanism not fully resolved); reduced adipocyte size; hepatic microvesicular steatosis in the severe case.
- **Tissue damage mechanisms:** Chronic bioenergetic/hypermetabolic stress in energy-demanding tissues (growth plate cartilage, adipose tissue, liver) rather than acute oxidative/ischemic injury.
- **Molecular profiling:** Proteomics performed on patient fibroblasts (mitochondrial proteome, 587 proteins assayed, 91 differentially expressed, P<0.05) — the only "omics" dataset reported for this condition to date; no transcriptomic, metabolomic, or single-cell datasets identified.

**Suggested GO terms:** GO:0006626 (protein targeting to mitochondrion), GO:0045040 (protein insertion into mitochondrial outer membrane), GO:0008637 (apoptotic mitochondrial changes — if relevant to downstream cell stress, not directly demonstrated), GO:0006119 (oxidative phosphorylation).
**Suggested CL terms:** CL:0000138 (chondrocyte, growth-plate relevance), CL:0000136 (adipocyte), CL:0000182 (hepatocyte), CL:0000057 (fibroblast, the primary cell type studied).

*Sources:* [JCI 156864](https://www.jci.org/articles/view/156864); [HGG Advances PMC9589026](https://pmc.ncbi.nlm.nih.gov/articles/PMC9589026/)

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary: skeletal system (growth plates → short stature), craniofacial skeleton (mandible), eyes (globe size, refraction, retina/macula), adipose tissue (lipodystrophy)
- Secondary: liver (steatosis in severe case), cardiovascular system (mild valvular/chamber changes), central nervous system (developmental delay; note the *distinct*, more severe TOM-complex-null allele causes primary CNS/basal-ganglia injury in Leigh syndrome)
- Body systems: musculoskeletal, ophthalmologic, endocrine/metabolic, hepatic, mild cardiovascular

**Tissue/cell level:**
- Growth-plate chondrocytes (reduced proliferation/density — shown in mouse models)
- Adipocytes (reduced size, lipoatrophy)
- Hepatocytes (microvesicular steatosis)
- Dermal fibroblasts (primary cell type used for functional/bioenergetic studies)

**Subcellular level:**
- Mitochondrial outer membrane (site of the primary molecular lesion — TOM complex)
- Mitochondrial matrix/inner membrane secondarily affected via proteome shift (ETC/ATP-synthase proteins)

**Suggested UBERON terms:** UBERON:0002544 (growth plate cartilage), UBERON:0001013 (adipose tissue), UBERON:0002107 (liver), UBERON:0001676 (mandible), UBERON:0000970 (eye).
**Suggested GO Cellular Component terms:** GO:0005741 (mitochondrial outer membrane), GO:0001401 (SAM complex — related import machinery), GO:0005743 (mitochondrial inner membrane, secondary).

**Lateralization:** Bilateral in all reported ophthalmologic and skeletal findings (no asymmetric/unilateral findings reported).

---

## 8. Temporal Development

- **Onset:** Not congenital in the classic sense — both detailed cases report **normal birth weight/length**, with growth failure emerging **postnatally**: by ~15 months in the severe case, by ~age 6 in the mildest (index) case. Onset pattern is insidious/progressive rather than acute.
- **Progression:** Variable and allele-dependent. In the mildest reported allele (P29L, index case), the patient survived to at least age 21 with a relatively stable, non-progressive course (no Parkinsonism, no neurological decline noted). In the W25R case, progression was more rapid, with death at 2.7 years from respiratory failure. Corresponding mouse models show an analogous severity gradient: knock-in (missense) mice show delayed-onset emaciation/death at 9–10 weeks, while null mice die earlier (3–4 weeks), and compound heterozygotes show intermediate severity (6–7 weeks) — directly demonstrating an allele-dose-dependent progression rate.
- **Disease course pattern:** Chronic, non-relapsing in survivors; for the most severely affected patients, disease is ultimately fatal in early childhood (respiratory failure/pneumonia as terminal events).
- **Critical periods:** Growth-plate/skeletal growth period (infancy through adolescence) appears to be a particular window of vulnerability given the mouse growth-plate findings and the human growth-failure timing.
- **Remission:** None reported; no spontaneous or treatment-induced remission described (see growth hormone treatment response in Section 12, which produced partial, not curative, benefit).

---

## 9. Inheritance and Population

**Epidemiology:** No formal prevalence or incidence figures exist. Given only 3 published probands (plus 2 deceased affected siblings referenced within reports) as of this report, GMPGS is among the rarest characterized Mendelian disorders — likely prevalence far below 1/1,000,000 (ultra-rare/"cases in literature" tier).

**Inheritance pattern:** Autosomal recessive (AR), confirmed in all reported families by parental heterozygosity and proband homozygosity.

**Penetrance:** Appears complete for the homozygous genotype (all homozygotes reported to date are affected), though sample size is far too small for a robust penetrance estimate.

**Expressivity:** **Markedly variable** — ranging from a relatively mild, survivable-to-adulthood phenotype (P29L index case) to a severe, early-fatal phenotype (W25R case) — driven at least partly by allelic effect (see Section 2/6), though environmental/genetic-background modifiers cannot be excluded given the small sample.

**Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).

**Germline mosaicism:** Not reported.

**Founder effects:** The P29L allele's restriction to East Asian gnomAD subpopulations (Korean, Japanese) at MAF 0.000048, and its independent identification in two unrelated Chinese-ancestry probands, suggests a possible regional founder or recurrent mutational hotspot, though formal haplotype analysis was not described in available abstracts.

**Consanguinity:** Explicitly reported in the AJCR (P29L, Han Chinese) proband's family; not reported as present in the JCI index family or the Japanese (W25R) family, both of which nonetheless carry homozygous variants (compatible with founder-allele inheritance rather than recent consanguinity).

**Carrier frequency:** Not directly reported; inferable as very low given the rarity of the homozygous MAF (0.000048) reported for P29L.

**Population demographics:** All reported probands are of **East Asian ancestry** (Chinese [including one described as "Malaysian" in a news account, likely of Chinese ethnicity], Han Chinese, Japanese). No cases reported in other ancestries for the GMPGS phenotype specifically (the Indian-family Leigh-syndrome allele is a distinct, non-GMPGS phenotype).

**Sex ratio:** All reported affected probands described in detail are **male** (JCI index case, HGG Advances case, AJCR case); the one detailed affected female relative (the JCI index patient's deceased sister) suggests the disorder is not X-linked and both sexes can be affected, consistent with autosomal recessive inheritance, though the currently published detailed cases happen to be predominantly male probands — likely a small-sample artifact rather than a true sex bias.

**Age distribution:** Reported ages at diagnosis/description range from infancy (severe case, died 2.7 yrs) to early adulthood (21 years, index case) to early childhood (2-year-old, AJCR case).

*Sources:* [JCI 156864](https://www.jci.org/articles/view/156864); [HGG Advances PMC9589026](https://pmc.ncbi.nlm.nih.gov/articles/PMC9589026/); [AJCR abstract](https://amjcaserep.com/abstract/full/idArt/950967)

---

## 10. Diagnostics

**Clinical tests reported/used across cases:**
- **Laboratory:** Largely non-diagnostic/normal routine chemistries; mild alkaline phosphatase elevation; elevated LDH and mild leukocytosis in the severe case; normal IGF-1, growth hormone axis, lipids, and glucose in the index case (i.e., **not** a classical GH-deficiency or lipid/metabolic-panel-diagnosable disorder by standard endocrine labs).
- **Imaging:** Brain MRI — normal structurally in the index case; skeletal survey — no significant bone-age delay in the index case but flattened vertebrae/gracile long bones in the severe case. Ophthalmologic exam — critical for diagnosis given the characteristic hyperopia/microphthalmia/nystagmus triad.
- **Cardiac evaluation:** Echocardiography identified mild valvular/chamber findings (not primary diagnostic criteria but part of the phenotypic workup).
- **Autopsy/histopathology:** In the fatal HGG Advances case, autopsy demonstrated microvesicular hepatic steatosis and reduced adipocyte size — a key pathological correlate of the lipodystrophy phenotype.

**Genetic testing:**
- **Diagnosis is by molecular genetic testing (exome sequencing)** in all reported cases — GMPGS was discovered via **exome sequencing** revealing the homozygous *TOMM7* variant, with **Sanger confirmation and parental carrier testing**.
- No gene panel specific to GMPGS/TOMM7 could be identified (condition too newly described); it would currently be identified incidentally on WES/WGS or via mitochondrial-disease gene panels that happen to include *TOMM7* (note: the UK Genomics England PanelApp does list TOMM7 under "Mitochondrial disorders" and "Likely inborn error of metabolism" panels, per search results).
- Homozygosity mapping was used in the index case (identifying the ~1 Mb region of homozygosity spanning *TOMM7* on chromosome 7) supporting causality.

**Differential diagnosis:** Given the phenotypic overlap, the differential includes other progeroid syndromes (Hutchinson-Gilford Progeria Syndrome/LMNA; mandibuloacral dysplasia; Wiedemann-Rautenstrauch syndrome; atypical progeroid syndrome due to LMNA), other primordial dwarfism syndromes, and other partial lipodystrophy syndromes (e.g., due to LMNA, PPARG, or other genes within Dr. Garg's broader lipodystrophy research portfolio). Distinguishing features favoring GMPGS: the combination of severe mandibular hypoplasia + high hyperopia/microphthalmia + partial lipodystrophy + biallelic (not dominant) inheritance pattern, and normal LMNA/known progeria-gene sequencing.

**Screening:** No population or newborn screening program exists for this ultra-rare condition.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** Highly variable by allele. The mildest reported allele (P29L) is compatible with survival into early adulthood (index proband alive and "doing well" at age 21); however, even within P29L-carrying families, one affected sibling died at age 10 during a febrile illness. The W25R allele proband died at 2.7 years (respiratory failure/pneumonia). No formal survival curves or life-expectancy statistics exist given the tiny cohort size.
- **Morbidity:** Growth failure, ophthalmologic impairment (poor visual acuity, 3/60 in the index case), developmental delay/learning disability, and (in the fatal case) progressive multi-organ involvement (skeletal, hepatic, respiratory) constitute the principal morbidity burden.
- **Complications:** Respiratory infection/failure appears to be a recurring terminal complication in the more severely affected patients, possibly reflecting reduced physiological/metabolic reserve.
- **Quality-of-life measures:** No standardized QoL instrument data reported.
- **Prognostic factors:** The specific causal variant (degree of residual TOM-complex function) appears to be the dominant prognostic factor identified to date, corroborated by parallel severity gradients in corresponding mouse models (knock-in vs. null vs. compound-heterozygous alleles).

---

## 12. Treatment

**Pharmacotherapy:**
- **Recombinant human growth hormone (rhGH)** — the only specific therapeutic intervention reported to date. A 2-year-old Han Chinese boy (P29L, homozygous) with growth stagnation was started on **long-acting recombinant human growth hormone at 31 months of age**; after **10 months of treatment**, length increased by **3.8 cm**, corresponding to a change in height SDS of **−0.34** (i.e., a partial, modest positive response, not normalization of growth). This is reported as a "novel therapeutic insight," suggesting rhGH may have some utility despite the patient's growth-hormone axis being biochemically normal (i.e., this is not classical GH-deficiency treatment, but an empirical trial given growth failure).
  - Suggested NCIT term: NCIT:C1502 (Somatropin) or a generic pharmacotherapy term with therapeutic_agent bound to the specific rhGH product if disclosed.

**Surgical/interventional:** None reported.

**Supportive/rehabilitative care:**
- Ophthalmologic correction (refractive correction for high hyperopia) — implied standard-of-care management, not explicitly detailed as a trial outcome.
- Developmental/educational support implied for learning disability, not detailed.

**Experimental treatments:** No registered clinical trials (ClinicalTrials.gov) were identified specific to GMPGS or TOMM7-related disease — consistent with the extreme rarity and recency of characterization. No targeted/precision mitochondrial therapeutics (e.g., mitochondrial-targeted antioxidants, uncoupling-agent-modulating drugs) have been reported/trialed.

**Treatment strategy notes:** Because the underlying mechanism (bioenergetic uncoupling with preserved ETC function) differs from classical OXPHOS-deficiency mitochondrial diseases, standard mitochondrial-disease supplement "cocktails" (CoQ10, riboflavin, etc., typically aimed at ETC support) have **no reported evidence base** for this specific uncoupling mechanism — this is a notable gap and area for future therapeutic research explicitly framed as such by Garg and Mishra in institutional coverage of the discovery.

**Suggested NCIT treatment terms for KB curation:** NCIT:C15986 (Pharmacotherapy) as `treatment_term`, with `therapeutic_agent` bound to somatropin/rhGH (verify exact CHEBI/NCIT code before binding); NCIT:C15302 (Physical Therapy)/NCIT:C15747 (Supportive Care) as general supportive-care placeholders pending more specific sourced treatments.

*Sources:* [AJCR abstract #950967](https://amjcaserep.com/abstract/full/idArt/950967)

---

## 13. Prevention

No primary, secondary, or tertiary prevention strategies are reported or applicable beyond **genetic counseling** for at-risk (carrier) families, given the autosomal recessive inheritance pattern and the demonstrated East Asian founder-allele association for P29L. No newborn screening, carrier screening program, immunization strategy, or public-health intervention exists for this condition given its extreme rarity and recent characterization. Prenatal diagnosis/preimplantation genetic testing would in principle be technically feasible for known familial variants (as for any characterized AR single-gene disorder) but no reports of this being performed for GMPGS were identified.

---

## 14. Other Species / Natural Disease

No naturally occurring GMPGS-like disease has been reported in non-human species (no OMIA entries or veterinary case reports identified). All animal data derive from **engineered (not naturally occurring) mouse models** — see Section 15. TOMM7 orthologs are highly conserved across mammals (the causal human residues, P29 and the W25/R24 region, are "completely conserved among mammals and other species" per the JCI report), consistent with the gene's fundamental, evolutionarily constrained role in mitochondrial biogenesis. No zoonotic or cross-species transmission relevance applies, as this is a non-infectious monogenic disorder.

---

## 15. Model Organisms

**Genetically engineered mouse models** (both reported in the HGG Advances study, Young et al. 2023) constitute the only model-organism data available:

1. **Knock-in (R/R) mouse** — carries the identical **W25R** missense variant found in the human proband.
   - Phenotype: relatively normal growth until 7–8 weeks of age, then rapidly progressive emaciation and sudden death around 9–10 weeks.
   - Growth-plate shortening with reduced chondrocyte proliferation (recapitulates human growth-plate/short-stature phenotype).
   - Hepatic lipid accumulation and reduced adipocyte size (recapitulates human lipodystrophy/hepatic steatosis).
   - Elevated OCR (oxygen consumption rate) and ECAR (extracellular acidification rate), upregulated phospho-AMPK, elevated Gdf15/Fgf21 — recapitulating the human bioenergetic-uncoupling signature.

2. **Null (deletion, D/D) mouse** — a 184 bp genomic deletion spanning the first exon–intron boundary of *Tomm7*, expected to be a functional null.
   - More severe phenotype: early postnatal growth failure and death at 3–4 weeks (i.e., **more severe than the missense knock-in**, directly modeling the allelic-severity gradient seen in humans, where the near-null splice variant causes lethal Leigh syndrome rather than GMPGS).
   - Similar but more pronounced skeletal/metabolic changes versus the knock-in model.
   - "Most prominent gross phenotype in these mouse models is lipoatrophy."

3. **Compound heterozygous (R/D) mice** — intermediate phenotype severity, death at 6–7 weeks — providing an allelic-series dose-response model directly relevant to understanding human genotype–phenotype correlations.

**Phenotype recapitulation assessment:** The mouse models recapitulate the core human triad of growth failure, lipodystrophy/lipoatrophy, and the bioenergetic-uncoupling mitochondrial signature (elevated respiration without ETC-inhibitor-response abnormality) with good fidelity. They do **not** directly model the human craniofacial dysmorphism (mandibular hypoplasia) or the specific ophthalmologic phenotype (hyperopia/microphthalmia/nystagmus) in the reporting available — these organ-specific human features have not been explicitly assessed/reported in the mouse studies, representing a translational gap between model and human phenotype (relevant to a `HUMAN_MODEL_MISMATCH`-style annotation if curated in dismech).

**Model limitations:** Complete lethality in the null model by 3–4 weeks limits long-term phenotypic characterization; the models have not yet been used to test therapeutic interventions (e.g., rhGH, metabolic modulators) as far as current literature indicates.

**Research applications:** These models are well suited to further mechanistic dissection of the TOM-complex assembly defect, the proton-gradient/ATP-synthase coupling abnormality, and potential pharmacologic correction of the mitochondrial uncoupling phenotype — an active area flagged for future research by the discovering investigators.

**Resources:** MGI:1913419 (*Tomm7* mouse gene entry, Mouse Genome Informatics).

*Sources:* [HGG Advances PMC9589026](https://pmc.ncbi.nlm.nih.gov/articles/PMC9589026/); [MGI:1913419](https://www.informatics.jax.org/marker/MGI:1913419)

---

## Curation Notes / Caveats for dismech KB Population

1. **MONDO ID unverified.** The user-supplied `MONDO:0957953` could not be confirmed against a live Monarch Initiative record during this research session; before creating a `kb/disorders/` entry, run the standard dismech term-lookup workflow to confirm or correct this identifier (or record it as `NOT_YET_DOCUMENTED`/absent per the ontology-term-contract rule against writing unverified CURIEs from memory).
2. **Very small evidence base.** With only 3 detailed published probands (Garg et al. 2022 JCI PMID 36282599; Young et al. 2023 HGG Advances PMID 36299998; and the 2025 AJCR case PMID 41460760) plus 2 deceased affected relatives referenced within those reports, essentially every phenotype/prevalence/prognosis claim in this report should be treated as `CASES_IN_LITERATURE`-tier (Orphanet prevalence-class convention) rather than a population-level statistic.
3. **Allelic heterogeneity is the single most important mechanistic fact** — do not conflate the GMPGS-causing hypomorphic missense alleles (P29L, W25R) with the distinct, non-GMPGS, lethal Leigh-syndrome-causing null/splice allele (c.153-2A>C, Yeole et al. 2025) when building the pathograph; they represent different downstream disease entities from the same gene and should likely be modeled as separate causal branches or even separate KB considerations (GMPGS vs. TOMM7-Leigh syndrome) per the dismech lump/split conventions.
4. **All PMIDs above should be independently re-verified and exact-quote-snippeted** against `references_cache/` per the `dismech-references` skill before use in an actual KB entry — this report's quotes were extracted via web-fetch/summarization tools rather than direct PMID abstract fetches for several sources (PubMed itself returned cookie-wall/403 errors during this session), so a `just fetch-reference PMID:<id>` pass is required before any snippet from this report is used as curated evidence.

---

### Sources
- [OMIM #620601 — Garg-Mishra Progeroid Syndrome](https://omim.org/entry/620601)
- [OMIM *607980 — TOMM7](https://omim.org/entry/607980)
- [JCI 156864 — Autosomal recessive progeroid syndrome due to homozygosity for a TOMM7 variant](https://www.jci.org/articles/view/156864)
- [PMC9711873 — Autosomal recessive progeroid syndrome due to homozygosity for a TOMM7 variant](https://pmc.ncbi.nlm.nih.gov/articles/PMC9711873/)
- [HGG Advances (PMC9589026) — A hypomorphic variant in TOMM7 causes short stature and developmental delay](https://pmc.ncbi.nlm.nih.gov/articles/PMC9589026/)
- [American Journal of Case Reports #950967 — Growth Hormone Response in a Child With a Homozygous TOMM7 Mutation](https://amjcaserep.com/abstract/full/idArt/950967)
- [PubMed 41460760](https://pubmed.ncbi.nlm.nih.gov/41460760/)
- [AJMG Part A — Bi-Allelic Splicing Variant, c.153-2A>C in TOMM7 Is Associated With Leigh Syndrome](https://onlinelibrary.wiley.com/doi/10.1002/ajmg.a.63892) / [PMC7617585 summary](https://pmc.ncbi.nlm.nih.gov/articles/PMC7617585/)
- [KEGG DISEASE H02768](https://www.kegg.jp/entry/ds_ja:H02768)
- [MalaCards: Garg-Mishra Progeroid Syndrome](https://www.malacards.org/card/garg_mishra_progeroid_syndrome)
- [UT Southwestern CT Plus — Premature-aging syndrome named after Garg, Mishra](https://www.utsouthwestern.edu/ctplus/honors-awards/gene-variant-garg.html)
- [IndiaWest News — Garg-Mishra: New Genetic Disorder Named After Indian American Scientists](https://indiawest.com/garg-mishra-new-genetic-disorder-named-after-indian-american-scientists/)
- [American Bazaar — Rapid aging genetic disorder named after two Indian American doctors](https://americanbazaaronline.com/2025/01/16/rapid-aging-genetic-disorder-named-after-two-indian-american-doctors-458398/)
- [GeneCards: TOMM7](https://www.genecards.org/cgi-bin/carddisp.pl?gene=TOMM7)
- [MGI:1913419 — Tomm7 Mouse Gene Detail](https://www.informatics.jax.org/marker/MGI:1913419)
- [PanelApp Genomics England — TOMM7 (Mitochondrial disorders)](https://panelapp.genomicsengland.co.uk/panels/112/gene/TOMM7/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 31 |
| Terms named correctly | 19 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000238` (1 mention) - the report calls it "Wide fontanel"; HP calls it **Hydrocephalus**
- `GO:0008637` (1 mention) - the report calls it "apoptotic mitochondrial changes — if relevant to downstream cell stress, not directly demonstrated"; GO calls it **apoptotic mitochondrial changes**
- `CL:0000138` (1 mention) - the report calls it "chondrocyte, growth-plate relevance"; CL calls it **chondrocyte**
- `CL:0000057` (1 mention) - the report calls it "fibroblast, the primary cell type studied"; CL calls it **fibroblast**
- `UBERON:0002544` (1 mention) - the report calls it "growth plate cartilage"; UBERON calls it **digit**
- `UBERON:0001676` (1 mention) - the report calls it "mandible"; UBERON calls it **occipital bone**
- `GO:0001401` (1 mention) - the report calls it "SAM complex — related import machinery"; GO calls it **SAM complex**
- `NCIT:C1502` (1 mention) - the report calls it "Somatropin"; NCIT calls it **Fiber**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0005440` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006626` (obsolete protein targeting to mitochondrion) (3 mentions) - replaced by `GO:0070585`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000540` (1 mention) - the report calls it "Hyperopia"; HP calls it **Hypermetropia**, and lists "Hyperopia" among its other names
- `HP:0001522` (1 mention) - the report calls it "Death in childhood"; HP calls it **Death in infancy**, and lists "Death in early childhood" among its other names
- `GO:0006626` (3 mentions) - the report calls it "protein targeting to mitochondrion"; GO calls it **obsolete protein targeting to mitochondrion**, and lists "protein targeting to mitochondria" among its other names
- `GO:0005743` (1 mention) - the report calls it "mitochondrial inner membrane, secondary"; GO calls it **mitochondrial inner membrane**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MGI:1913419` - called "Tomm7* mouse gene entry, Mouse Genome Informatics", "Tomm7 Mouse Gene Detail"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.