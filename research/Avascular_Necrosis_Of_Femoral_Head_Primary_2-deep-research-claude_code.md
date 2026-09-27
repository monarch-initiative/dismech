---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-04T03:42:55.906200'
end_time: '2026-09-04T03:48:52.501530'
duration_seconds: 356.6
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Avascular Necrosis of Femoral Head, Primary, 2
  mondo_id: MONDO:0054551
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
  web_search_requests: 15
  num_turns: 21
  total_cost_usd: 1.3379371999999998
  session_id: 0ef66ed1-dec7-5650-90c2-e2d1e83a9eb8
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 29
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 0
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMC:PMC5035228
  - PMID:27330106
  relevance_assessed: 19
  on_topic: 3
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 38
  verified: 36
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 0
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0010734
    reported_labels:
    - Avascular necrosis of the capital femoral epiphysis
    - 'Phenotype: avascular necrosis of femoral head'
    ontology_label: Fibrous dysplasia of the bones
  - term_id: HP:0100787
    reported_labels:
    - Gait disturbance
    - 'Phenotype: gait disturbance'
    ontology_label: Prostate neoplasm
  - term_id: HP:0002826
    reported_labels:
    - Limited joint mobility
    - 'Phenotype: limited joint mobility'
    ontology_label: Halberd-shaped pelvis
  - term_id: UBERON:0001417
    reported_labels:
    - 'Anatomy: femur'
    ontology_label: skin of neck
  - term_id: UBERON:0001360
    reported_labels:
    - 'Anatomy: hip joint'
    ontology_label: deep circumflex iliac vein
  labels_variant: 11
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Avascular Necrosis of Femoral Head, Primary, 2
- **MONDO ID:** MONDO:0054551 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Avascular Necrosis of Femoral Head, Primary, 2** covering all of the
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

I have enough primary-source material now. Let me compile the comprehensive research report.

# Avascular Necrosis of Femoral Head, Primary, 2 (ANFH2) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Avascular Necrosis of Femoral Head, Primary, 2 (ANFH2) is a rare, monogenic, autosomal dominant form of osteonecrosis of the femoral head (ONFH) caused by a gain-of-function mutation in **TRPV4** (transient receptor potential vanilloid 4), a calcium-permeable cation channel gene on chromosome 12q24.11. It was first delineated in 2016 by Mah et al., who identified the causal mutation in a Canadian family of Irish/Scottish descent in which four of six siblings developed severe, early-onset, bilateral osteonecrosis of the femoral head with no identifiable acquired risk factor (no corticosteroid use, alcohol abuse, trauma, or thrombophilia) (PMID:27330106). ANFH2 is genetically distinct from, but clinically overlapping with, **ANFH1** (OMIM 608805), the COL2A1-associated form of familial ANFH first mapped and characterized by Liu et al. (2005).

More broadly, "avascular necrosis of the femoral head" (osteonecrosis of the femoral head, ONFH) refers to death of osteocytes and bone marrow elements in the femoral head secondary to interruption of its (already tenuous) blood supply, leading to subchondral collapse and secondary osteoarthritis. The great majority of ONFH cases are **non-genetic/acquired** ("secondary" — corticosteroid-, alcohol-, or trauma-associated) or idiopathic; ANFH1 and ANFH2 represent the rare **familial/primary (Mendelian)** subset in which a single-gene mutation is sufficient to cause the phenotype, typically with earlier onset, higher bilaterality, and a positive family history.

**Key identifiers:**
- **MONDO:** MONDO:0054551 (Avascular Necrosis of Femoral Head, Primary, 2)
- **OMIM:** #617383 (ANFH2, phenotype); *605427 (TRPV4, gene/locus)
- **Related/allelic locus (ANFH1):** OMIM #608805 (phenotype); *120140 (COL2A1, gene)
- **Orphanet:** the broader "familial avascular necrosis of femoral head" concept is cataloged by Orphanet/rarediseases.org under the TRPV4 and COL2A1 gene pages (Orphanet gene pages for TRPV4 and COL2A1)
- **Gene (ANFH2):** TRPV4; HGNC:12716; NCBI Gene ID 59341; UniProt Q9HBA0
- **Broader disease codes** (osteonecrosis of femoral head, general): ICD-10 M87.0 (idiopathic aseptic necrosis of bone)/M87.8x; ICD-11 FA80.0/FA80.Z; MeSH D010020 ("Femur Head Necrosis")
- **Inheritance:** Autosomal dominant

**Synonyms/alternative names:** ANFH2; Osteonecrosis of the femoral head, primary, 2; Familial avascular necrosis of the femoral head (TRPV4-related); Familial osteonecrosis of the femoral head, TRPV4-related. (Not to be confused with "avascular necrosis of the femoral head, primary 1," which is COL2A1-related, or with Legg-Calvé-Perthes disease, the pediatric form of ANFH which has also been linked to some COL2A1 variants.)

**Evidence basis:** Information for ANFH2 specifically derives from a **single reported pedigree study** (one Canadian family, 4 affected siblings; human clinical + in vitro electrophysiological functional data) (PMID:27330106), supplemented by OMIM curation (#617383) and by the broader TRPV4 channelopathy literature (skeletal dysplasias and peripheral neuropathies caused by other TRPV4 alleles), which is derived from many aggregated case reports/small cohorts rather than large-scale epidemiological data. This is not an EHR-derived or population-registry disease entity — data are case/pedigree-level.

---

## 2. Etiology

### Disease Causal Factors
ANFH2 is caused by a **heterozygous gain-of-function mutation in TRPV4**, a mechanosensitive/osmosensitive Ca²⁺-permeable cation channel. The causal mechanism is genetic (single-gene, monogenic), not environmental/infectious — this distinguishes ANFH2 from the majority of ONFH cases, which are acquired (corticosteroid, alcohol, trauma).

### Genetic Risk Factors
- **Causal variant (ANFH2 family):** heterozygous *TRPV4* c.2480_2483delCCCG frameshift deletion immediately followed by a c.2486T>A substitution (NM_021625.4), predicted to cause p.Val829TrpfsTer3 (V829Wfs*3), a C-terminal frameshift/truncation. Functional testing showed this is a **gain-of-function** allele (see Mechanism, below) (PMID:27330106). "All affected siblings with osteonecrosis of the femoral head harbored a heterozygous frameshift deletion in TRPV4" (per PMC5035228 summary of the paper); unaffected siblings were wild type — full segregation with disease in this family.
- **Allelic gene (ANFH1):** heterozygous *COL2A1* missense variants — e.g., c.2149G>A (p.Gly717Ser) in the original ANFH1 family (Liu et al., 2005) and a second independent family with c.3517G>A (p.Gly1173Ser) in exon 50 (Chinese family, PMID reported in PMC8178877) — establish genetic heterogeneity of primary/familial ANFH.
- **Susceptibility loci for sporadic (non-Mendelian) ONFH:** SREBP-2 gene polymorphisms have been reported associated with AVN risk in a Korean population (PMC2600781); these are population susceptibility signals, distinct from the Mendelian ANFH1/ANFH2 causal alleles, and are not directly relevant to the ANFH2 KB entry's causal claim.

### Environmental Risk Factors (relevant mainly to the broader ONFH phenotype, not specific to the TRPV4-driven form, but relevant for differential/modifier context)
- **Corticosteroid use** — accounts for a large share of acquired (secondary) ONFH; risk estimates for corticosteroid-associated AVN range roughly 3–40% depending on dose/duration.
- **Alcohol use** — dose-dependent risk: <400 mL/week alcohol confers ~3-fold risk; >400 mL/week confers ~11-fold risk versus non-drinkers.
- **Trauma** (femoral neck fracture, hip dislocation).
- **Age/sex** — AVN typically affects physically active adults 20–40 years old; a Japanese survey found idiopathic mechanisms accounted for 37.1% of cases, corticosteroids 34.7%, and alcohol 21.8%.
- In the ANFH2 pedigree specifically, all of these acquired causes were **explicitly excluded** by the investigators ("no identifiable risk factors — alcohol, steroids, trauma, thrombophilia" per PMC5035228), supporting a purely genetic etiology in this family.

### Protective Factors
No specific genetic or environmental protective factors have been established for TRPV4-related ANFH2. In the general ONFH literature, avoidance of high-dose/prolonged corticosteroids and heavy alcohol intake are the principal modifiable protective measures, but these pertain to the acquired form, not the Mendelian TRPV4 form.

### Gene-Environment Interactions
No gene-environment interaction data have been reported specifically for TRPV4/ANFH2. It is biologically plausible (though undemonstrated) that mechanical loading of the femoral head — an already watershed, poorly collateralized vascular bed under constant mechanical stress — could interact with a constitutively gain-of-function TRPV4 channel (itself a mechanosensor) to potentiate localized vasoconstriction, but this remains inferential rather than experimentally established (see Mechanism section).

---

## 3. Phenotypes

| Phenotype | Type | Onset | Frequency in ANFH2 pedigree | Suggested HPO term |
|---|---|---|---|---|
| Hip/groin pain | Symptom | 3rd–4th decade typically (proband diagnosed at age 21) | Present in all 4 affected siblings | HP:0030839 (Groin pain) / HP:0003326 (Myalgia) — best available is generic hip pain; consider HP:0030828 not applicable; use free text if no exact HP term |
| Avascular necrosis of the femoral head | Clinical sign / imaging finding | Onset 2nd–4th decade | 4/4 affected, bilateral in all affected members | HP:0010734 (Avascular necrosis of the capital femoral epiphysis) |
| Bilateral hip involvement | Clinical sign | Concurrent with above | "All affected family members had bilateral hip involvement, whereas only two-thirds of the sporadic patients had bilateral disease" | HP:0410030-type bilaterality qualifier, or a `laterality: BILATERAL` descriptor |
| Limping gait | Sign | Progressive | Typical of advanced-stage disease | HP:0100787 (Gait disturbance) |
| Limitation of hip range of motion | Sign | Progressive, later disease stages | Typical | HP:0002826 (Limited joint mobility) |
| Femoral head collapse / subchondral fracture (Steinberg stage III–V) | Radiographic finding | Progressive | Affected siblings ranged Steinberg Stage III to Stage V | HP:0003043 (relevant femoral abnormality terms are limited; consider HP:0011869 or free text "femoral head collapse") |
| Leg length discrepancy | Sign (secondary to collapse) | Late-stage | Reported as part of the general ONFH clinical picture (per general ONFH literature) | HP:0100559 (Asymmetric growth / limb length discrepancy) |
| Normal stature / no skeletal dysplasia | Negative finding — differential | N/A | Explicitly documented negative (excludes TRPV4 skeletal-dysplasia allelic phenotype) | — |
| Normal neurological exam / normal nerve conduction studies | Negative finding — differential | N/A | Explicitly excludes TRPV4 peripheral-neuropathy allelic phenotype (CMT2C) | — |

**Phenotype characteristics:**
- **Age of onset:** In the index family, the proband was diagnosed at age 21; OMIM notes onset of hip pain in reported ANFH2 families "typically occurs in the third to fourth decade of life." This is notably earlier than the acquired/idiopathic ONFH population (usually 20–40, similar range but with a genetic family showing earlier, more penetrant, and more severe presentation).
- **Severity/progression:** Progressive — untreated disease advances through radiographic stages (Ficat/Arlet, Steinberg, or 2019 ARCO systems) toward subchondral collapse and secondary osteoarthritis. In the ANFH2 family, disease had already reached Steinberg Stage III–V at presentation in affected siblings, i.e., advanced/collapsed disease, consistent with a highly penetrant and aggressive natural history.
- **Bilaterality:** A phenotypic hallmark distinguishing the familial/genetic form: **100% of affected ANFH2 family members had bilateral disease**, versus roughly two-thirds of sporadic (acquired) ONFH patients — an important discriminating feature for entity classification.
- **Quality of life impact:** Not separately quantified for ANFH2, but ONFH generally is "a severely disabling disease" causing progressive pain, gait disturbance, and eventual need for total hip arthroplasty, with substantial impact on mobility and work capacity in an otherwise young, active population.

---

## 4. Genetic/Molecular Information

**Causal gene:** TRPV4 (HGNC:12716; NCBI Gene ID 59341; OMIM *605427; chromosome 12q24.11; UniProt Q9HBA0). Encodes "transient receptor potential cation channel, subfamily V, member 4," a polymodal, calcium-permeable, non-selective cation channel activated by hypotonic cell swelling, moderate heat, mechanical stress/shear stress, low pH, and phorbol esters/endogenous lipid ligands.

**Pathogenic variant (ANFH2 index family):**
- **cDNA change:** c.2480_2483delCCCG followed immediately by c.2486T>A (NM_021625.4/NM_021625.5)
- **Protein change:** p.Val829TrpfsTer3 (V829Wfs*3) — a frameshift causing premature truncation
- **Variant classification:** Not formally reported to ClinVar under a standard ACMG tier in the sources retrieved here, but functionally characterized as pathogenic/gain-of-function by the original authors via electrophysiology.
- **Location/domain effect:** The frameshift "eliminates a highly conserved region including residues within a calmodulin-binding domain" in the cytoplasmic C-terminus of TRPV4 — i.e., it removes part of the channel's autoinhibitory/regulatory machinery rather than ablating channel expression.
- **Origin:** Germline, autosomal dominant, fully segregating with disease in the 4 affected/2 unaffected sibling pedigree.
- **Allele frequency:** Not reported in population databases (gnomAD) for this specific ANFH2 frameshift variant in the sources retrieved; TRPV4 pathogenic missense alleles causing other TRPV4-opathies (e.g., p.Arg315Trp) are found only at extremely low frequency (e.g., 2/1,614,018 in gnomAD) or are entirely absent from population controls, consistent with strong purifying selection against gain-of-function TRPV4 alleles generally.
- **Functional consequence:** **Gain-of-function** — not loss-of-function. Disruption of the C-terminal calmodulin-binding region impairs normal Ca²⁺-calmodulin-dependent negative feedback/channel closure, producing sustained, excessive Ca²⁺ influx (see Mechanism, Section 6).

**Allelic disease (ANFH1) causal gene:** COL2A1 (HGNC:2200; OMIM *120140; chromosome 12q13.11), encoding the alpha-1 chain of type II collagen. Reported ANFH1 variants: c.2149G>A (p.Gly717Ser) in the original 2005 pedigree (Liu et al.), and c.3517G>A (p.Gly1173Ser) in a large Chinese kindred — both classic glycine-substitution collagen triple-helix mutations. COL2A1 variants are also implicated in Legg-Calvé-Perthes disease (LCPD, a pediatric ONFH phenotype), underscoring that COL2A1-collagenopathy mechanisms differ fundamentally (structural/matrix) from the TRPV4 vasoregulatory/ion-channel mechanism.

**Modifier genes:** None specifically established for ANFH2. For the general/sporadic ONFH phenotype, SREBP-2 polymorphisms have been proposed as population-level modifiers of risk (Korean cohort, PMC2600781), but this is not established as a modifier of TRPV4-driven ANFH2 specifically.

**Epigenetic information:** No epigenetic (DNA methylation/histone) data specific to ANFH2 or TRPV4-driven ONFH were identified in this search.

**Chromosomal abnormalities:** None reported; ANFH2 is caused by a small indel, not a chromosomal-scale rearrangement.

**Suggested ontology bindings:**
- Gene: `hgnc:12716` (TRPV4)
- GO Molecular Function: `GO:0005227` (calcium activated cation channel activity) / `GO:0015643` — best available specific term is TRPV4's calcium channel activity, `GO:0005262` (calcium channel activity)
- GO Biological Process: `GO:0070588` (calcium ion transmembrane transport); osmosensory/mechanosensory transduction — `GO:0050982` (detection of mechanical stimulus) is plausible for TRPV4's mechanosensor role

---

## 5. Environmental Information

**Environmental factors:** Not causally implicated in the TRPV4-driven ANFH2 form itself (the index family was specifically screened and found negative for alcohol, steroid, trauma, and thrombophilia exposure). For the broader ONFH disease category (relevant as differential/comorbid triggers, and potentially as modifiers of expressivity in TRPV4 carriers, though this gene-environment interaction is not demonstrated):
- **Corticosteroid exposure** (exogenous glucocorticoid therapy for any indication) — major driver of secondary ONFH.
- **Chronic heavy alcohol consumption** — dose-dependent risk factor for secondary ONFH.
- Case reports also describe ONFH following **COVID-19 infection**, independent of steroid use (PMC12337778), suggesting a possible inflammatory/coagulopathic environmental trigger pathway relevant to the broader disease category, though not tested in ANFH2 carriers specifically.

**Lifestyle factors:** Smoking and heavy alcohol use are generally cited modifiable lifestyle risk factors for ONFH broadly; no ANFH2-specific lifestyle-modifier data exist.

**Infectious agents:** No infectious etiology for ANFH2. (COVID-19 has been reported as an environmental trigger for sporadic ONFH cases generally, as above, but this is not established for the TRPV4-mutant form.)

---

## 6. Mechanism / Pathophysiology

### Causal chain (ANFH2)

1. A heterozygous germline frameshift mutation in *TRPV4* (c.2480_2483delCCCG; c.2486T>A → p.Val829Trpfs*3) **removes/disrupts** a conserved C-terminal calmodulin-binding regulatory domain of the TRPV4 channel protein.
2. This loss of the normal calmodulin-mediated negative feedback **leads to** a gain-of-function biophysical phenotype: patch-clamp/TIRF "sparklet" recordings in cells expressing the mutant channel show **2.5-fold higher baseline TRPV4 sparklet (single-channel Ca²⁺ influx event) activity** and **two-fold longer mean channel burst-open times** at each conductance level compared to wild-type channel — i.e., the mutant channel opens more often and stays open longer (PMID:27330106).
3. Prolonged/excessive channel opening **results in** sustained, pathologically elevated intracellular Ca²⁺ influx in cells expressing mutant TRPV4 (demonstrated experimentally, not merely inferred).
4. Because TRPV4 is expressed in, and regulates, **vascular endothelium/smooth muscle (vasoregulation)** and **osteoclasts (osteoclastic differentiation and bone resorption)**, this excess Ca²⁺ influx is proposed to **cause** two convergent downstream effects: (a) endothelial dysfunction and abnormal vascular tone/vasoconstriction in the vessels supplying the femoral head, and (b) altered osteoclast differentiation/bone-remodeling activity.
5. The femoral head is anatomically a **watershed vascular territory** with minimal collateral circulation and is subject to constant mechanical loading — a physiologic niche in which TRPV4 (itself a mechanosensor) would be expected to be tonically engaged. The authors propose that this anatomic vulnerability **amplifies** the effect of chronic TRPV4 gain-of-function, producing localized "calcium overload, leading to endothelial dysfunction and vasoconstriction, resulting in bone loss at the hip" (quoted mechanistic hypothesis from PMID:27330106) — this step (from cellular Ca²⁺ overload to clinically apparent ischemia at the hip specifically) is the authors' proposed integrative hypothesis rather than a step demonstrated in vivo in the family; it is **inferred**, not directly shown in patient bone/vascular tissue.
6. Chronic interruption of blood supply to the femoral head **leads to** osteocyte death (necrosis) in the trabecular bone and marrow of the femoral head.
7. Cumulative osteocyte death and unrepaired microdamage **result in** subchondral microfractures, which the femoral head — due to its high mechanical load-bearing role — cannot structurally tolerate, and this **leads to** progressive subchondral bone collapse (radiographically staged via Ficat/Steinberg/ARCO systems).
8. Structural collapse of the femoral head **causes** the clinical manifestations: progressive groin/hip pain, limping gait, limitation of hip motion, leg-length discrepancy, and — ultimately — secondary degenerative osteoarthritis of the hip joint requiring total hip arthroplasty in advanced (uncollapsed-refractory) cases.

**Branch — general (acquired) ONFH pathway**, for contrast: in the far more common acquired/idiopathic form, the "final common pathway is interruption of blood flow to the bone," with **intravascular coagulation** (rather than a primary vasoregulatory ion-channel defect) proposed as the central inciting event, triggered by corticosteroid-induced lipid embolization/adipocyte hypertrophy or alcohol-induced fat emboli and hypercoagulability — a mechanistically distinct but convergent route to the same endpoint of osteocyte death, microfracture accumulation, and collapse.

### Category detail

- **Molecular pathways:** TRPV4-mediated Ca²⁺ signaling; downstream Ca²⁺/calmodulin signaling normally provides negative feedback on channel activity (disrupted in ANFH2); in TRPV4 skeletal-dysplasia alleles (a related but phenotypically distinct allelic series), gain-of-function Ca²⁺ signaling reprograms chondrocytes to increase follistatin production, which inhibits BMP signaling and impairs endochondral ossification — illustrating the pleiotropic, tissue-context-dependent downstream consequences of TRPV4 gain-of-function across the allelic series (skeletal dysplasia vs. ANFH vs. peripheral neuropathy).
- **Cellular processes:** Osteocyte/osteoclast biology (TRPV4 regulates steady-state Ca²⁺ influx at the late stage of osteoclast differentiation, required for NFATc1-dependent transcription controlling osteoclast terminal differentiation and resorptive capacity — established in Trpv4-knockout mouse studies, which show the converse phenotype: reduced osteoclast number/activity and increased bone mass); vascular endothelial/smooth muscle tone regulation; mechanotransduction (TRPV4 mediates oscillatory fluid-shear-induced Ca²⁺ signaling in mesenchymal stem cells, partly via the primary cilium).
- **Protein dysfunction:** Gain-of-function (not loss-of-function) via disruption of a C-terminal calmodulin-binding autoregulatory domain — a distinct molecular mechanism from the COL2A1 glycine-substitution mechanism in ANFH1 (structural collagen triple-helix disruption/dominant-negative matrix defect) and from TRPV4 loss-of-function.
- **Metabolic changes:** Not specifically profiled for ANFH2.
- **Immune system involvement:** Not implicated in the TRPV4-driven mechanism; in the general ONFH literature, intravascular coagulation/thromboembolic mechanisms (relevant to secondary ONFH) are more prominent than adaptive/innate immune mechanisms.
- **Tissue damage mechanisms:** Ischemic necrosis (osteocyte death from vascular compromise) → microfracture accumulation → mechanical structural failure (subchondral collapse). This is fundamentally an **ischemia/mechanical-failure** mechanism rather than primary inflammatory or autoimmune tissue damage.
- **Biochemical abnormalities:** Excess, prolonged Ca²⁺ influx through mutant TRPV4 channels (directly measured); downstream biochemical consequences (endothelial NO/vasoactive mediator dysregulation, osteoclast NFATc1 signaling) are inferred from the known biology of TRPV4 in vascular and bone tissue rather than measured directly in the ANFH2 family.
- **Molecular profiling:** No transcriptomic, proteomic, metabolomic, or single-cell/spatial data specific to the ANFH2 family or its causal variant were identified in the literature retrieved.

**Suggested ontology terms:**
- GO Biological Process: `GO:0070588` (calcium ion transmembrane transport); `GO:0030316` (osteoclast differentiation); vasoregulation — `GO:0042311` (vasodilation) / `GO:0042310` (vasoconstriction)
- GO Molecular Function: `GO:0005262` (calcium channel activity); `GO:0005516` (calmodulin binding)
- Cell types (CL): `CL:0000092` (osteoclast); `CL:0000115` (endothelial cell); `CL:0002518` (kidney/vascular smooth muscle) — most relevant here is `CL:0000359` (vascular associated smooth muscle cell) for the vasoregulatory arm, and `CL:0001035` (bone cell) more generally for the osteoclast/osteocyte arm.

---

## 7. Anatomical Structures Affected

- **Organ level:**
  - **Primary:** Femoral head (proximal epiphysis of the femur) — bilateral in ANFH2.
  - **Secondary:** Hip joint (acetabulum secondarily affected as osteoarthritis develops); overall lower-limb biomechanics (leg-length discrepancy, gait).
  - **Body systems:** Musculoskeletal system (primary); cardiovascular system (vascular supply to bone — the proposed mechanistic substrate).
  - UBERON: `UBERON:0002378` (femur head / femoral head epiphysis — precise term is "head of femur," UBERON:0001417 is femur; the specific structure is the femoral head, UBERON:0001417's epiphyseal head — best available specific term: **UBERON:0001417** femur, with the head specifically captured by HPO's HP:0010734 rather than a distinct UBERON term for "femoral head" alone in some ontology builds); Hip joint: `UBERON:0001360`.

- **Tissue and cell level:**
  - Subchondral trabecular bone and bone marrow of the femoral head (site of osteocyte necrosis and microfracture).
  - Articular cartilage of the femoral head (secondarily affected once subchondral collapse occurs).
  - Osteoclasts (`CL:0000092`) — implicated via TRPV4's role in osteoclast differentiation.
  - Vascular endothelial cells (`CL:0000115`) and vascular smooth muscle (`CL:0000359`) of the retinacular/epiphyseal arteries supplying the femoral head — the anatomically limited, largely end-arterial blood supply of the femoral head (chiefly via the medial femoral circumflex artery) is the key anatomic vulnerability exploited by this mechanism.

- **Subcellular level:**
  - Plasma membrane (site of TRPV4 channel activity) — `GO:0005886` (plasma membrane) / `GO:0034704` (calcium channel complex).
  - Primary cilium — implicated in TRPV4 mechanotransduction in mesenchymal/osteogenic cells generally (`GO:0005929`, cilium).

- **Localization:** Bilateral in all reported ANFH2-affected individuals (100% bilaterality), in contrast to ~two-thirds bilaterality in sporadic/acquired ONFH — a notable, ontologically codable laterality distinction.

---

## 8. Temporal Development

- **Onset:** Typically third to fourth decade of life for hip pain onset (per OMIM #617383); the index proband was formally diagnosed at age 21 with bilateral disease already present. Onset pattern is **insidious** (gradual, non-acute), with pain preceding radiographic collapse.
- **Progression:** Progressive and, in the reported family, already advanced at diagnosis — affected siblings ranged from **Steinberg Stage III to Stage V** (i.e., subchondral collapse through end-stage secondary osteoarthritic change) at the time of clinical presentation, indicating a relatively aggressive, highly penetrant natural history in this pedigree. Using the general ONFH staging frameworks (Ficat/Arlet, University of Pennsylvania/Steinberg, 2019-revised ARCO), disease evolves from an asymptomatic pre-radiographic stage (Stage 0/I, MRI-only marrow signal change) through radiographically apparent sclerosis/cystic change (Stage II), subchondral fracture with head depression ≤2 mm (Stage IIIA) or >2 mm (Stage IIIB), to secondary osteoarthritis (Stage IV).
- **Patterns:** No spontaneous remission is described for structurally collapsed disease; earlier-stage (pre-collapse) lesions can regress with intervention (e.g., core decompression halting/reversing Stage I disease in some general-ONFH series), but once subchondral collapse has occurred the process is essentially irreversible and progresses toward joint destruction. The **critical window for joint-preserving intervention is pre-collapse (Ficat/ARCO Stage I–II)**; once Stage III (subchondral fracture/collapse) is reached, joint-preserving procedures are far less effective and total hip arthroplasty becomes the definitive treatment.

---

## 9. Inheritance and Population

- **Epidemiology (general ONFH, for context):** ~10,000–20,000 new ONFH cases/year in the United States; a Japanese national survey estimated ~2,500–3,300 new hip ONFH cases/year, with idiopathic mechanisms accounting for 37.1%, corticosteroids 34.7%, and alcohol 21.8% of cases. ANFH2 (TRPV4-driven, Mendelian) is an **ultra-rare** subset of this broader idiopathic/familial category — only a single multiplex pedigree has been reported to date in the literature identified here, so no independent prevalence/incidence estimate exists for ANFH2 specifically; it should be classed as **prevalence class: NOT_YET_DOCUMENTED / ultra-rare** pending further case ascertainment.
- **Inheritance pattern:** Autosomal dominant, fully penetrant in the reported pedigree (4/4 mutation carriers among tested siblings were affected; unaffected siblings were confirmed wild-type) — i.e., complete segregation, consistent with high penetrance, though formal penetrance/expressivity estimates across a larger population are not available (n=1 family).
- **Expressivity:** Variable in severity/stage at presentation is plausible given the general ONFH literature but not separately quantified across ANFH2 carriers beyond the single reported family; bilaterality appears highly consistent (100% in this family).
- **Genetic anticipation:** Not reported/assessed.
- **Germline mosaicism:** Not reported/assessed; parents were deceased in the index family, so parental mutation status/de novo vs. inherited origin at the founder generation could not be determined from available records ("Parents and grandparents are deceased, but family members recalled paternal joint pain never formally evaluated" — consistent with, but not proof of, the mutation having been inherited from the paternal line).
- **Founder effects / consanguinity:** No founder effect or consanguinity reported; this is a single, non-consanguineous Canadian (Irish/Scottish ancestry) pedigree.
- **Carrier frequency:** Not established in population databases; the specific ANFH2 frameshift variant was not found reported in large population reference databases in the sources retrieved, consistent with its rarity and pathogenicity.
- **Population demographics:** No broader ethnic/geographic prevalence data exist specific to TRPV4-driven ANFH2. General ONFH shows a male predominance in most series and predominantly affects adults 20–40 years old.
- **Sex ratio:** Not separately reported for the ANFH2 pedigree (4 of 6 siblings affected; sex distribution among the 4 affected not specified in retrieved sources).

---

## 10. Diagnostics

- **Clinical tests / imaging:**
  - **Radiography (X-ray)** — used for initial staging; normal in earliest disease (Ficat/ARCO Stage 0–I) and shows sclerosis, cystic change, subchondral lucency ("crescent sign"), and eventually head flattening/collapse in later stages.
  - **MRI** — the gold-standard imaging modality; the pathognomonic **"double-line sign"** (an outer low-signal-intensity rim adjacent to a second inner high-signal-intensity rim on T2/fluid-sensitive sequences, representing a fibrous/sclerotic reactive interface with an inner hyperemic granulation-tissue zone) is seen in ~80–85% of AVN cases and is considered highly specific for the diagnosis; MRI is sensitive to pre-radiographic (Stage I) marrow edema/signal change.
  - **Staging systems**: Ficat and Arlet classification (original, 3–6 stages); University of Pennsylvania (Steinberg) system (mild <15%, moderate 15–30%, severe >30% of articular surface/head involved); 2019-revised Association Research Circulation Osseous (ARCO) system (Stage I: normal X-ray, abnormal MRI; Stage II: abnormal X-ray and MRI, no collapse; Stage IIIA: subchondral fracture/collapse ≤2 mm; Stage IIIB: collapse >2 mm; Stage IV: secondary osteoarthritis).
  - In the ANFH2 family specifically, **Steinberg classification** was used, with affected siblings ranging from Stage III to Stage V.
- **Genetic testing:**
  - Whole-exome sequencing was the discovery method used to identify the causal TRPV4 variant in the index family, followed by Sanger sequencing confirmation and segregation testing across siblings.
  - For clinical diagnostic purposes today, a **targeted single-gene test (TRPV4) or a skeletal-dysplasia/osteonecrosis gene panel including TRPV4 and COL2A1** would be the appropriate approach in a patient with early-onset, bilateral, familial ONFH without acquired risk factors.
  - **Differential genetic workup should also include COL2A1** (ANFH1) given genetic heterogeneity of the familial ONFH phenotype.
- **Exclusionary workup performed in the ANFH2 family** (relevant "rule-out" diagnostics): skeletal survey (negative — excludes TRPV4 skeletal dysplasia allelic phenotype), neurological exam and nerve conduction studies (normal — excludes TRPV4 peripheral neuropathy/CMT2C allelic phenotype), thrombophilia panel (negative), and COL2A1 sequencing (negative, prior to TRPV4 discovery).
- **Clinical criteria / differential diagnosis:** Differential diagnosis for early-onset bilateral hip osteonecrosis includes corticosteroid- or alcohol-associated secondary ONFH, sickle cell disease, Gaucher disease, hemoglobinopathies, thrombophilia/hypercoagulable states, systemic lupus erythematosus, decompression sickness ("caisson disease"), radiation-induced necrosis, and other primary/familial (COL2A1-associated) ANFH.
- **Screening:** No population or newborn screening applicable given extreme rarity; cascade genetic testing/counseling of at-risk relatives in a known TRPV4-ANFH2 family would be the appropriate clinical screening strategy once a proband is identified.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** ANFH2 (and ONFH generally) is not directly life-threatening; it is a joint-destructive, disabling musculoskeletal condition rather than one associated with excess mortality.
- **Morbidity/function:** Progressive pain, gait disturbance, and functional impairment of hip range of motion; untreated or advanced disease leads to secondary osteoarthritis and often requires total hip arthroplasty. In the ANFH2 family, disease had already advanced to Steinberg Stage III–V (subchondral collapse through secondary arthritic change) by the time of diagnosis/intervention, indicating a prognosis dominated by need for surgical joint preservation or replacement rather than medical management alone.
- **Disease course:** Once subchondral collapse occurs, the process is essentially irreversible; pre-collapse (early-stage) disease has a better prognosis with joint-preserving intervention (e.g., core decompression).
- **Complications:** Secondary osteoarthritis of the hip; leg-length discrepancy; long-term consequences of early hip arthroplasty in young patients (implant longevity/revision risk over a young patient's remaining lifespan is a significant prognostic concern given the young age of onset in ANFH2).
- **Recovery potential:** With joint-preserving intervention (core decompression) at early (Ficat/ARCO Stage I) stage, some lesions have been reported to regress; more advanced disease (as seen in the ANFH2 family at presentation) gains little benefit from joint-preserving procedures, and total hip arthroplasty is the eventual outcome.
- **Prognostic factors:** Stage at diagnosis/intervention is the dominant prognostic factor (pre-collapse vs. post-collapse); percentage of femoral head involvement (Steinberg mild/moderate/severe); bilaterality (100% in ANFH2, versus ~two-thirds in sporadic disease) worsens overall disease burden by requiring management of both hips.

---

## 12. Treatment

- **Pharmacotherapy** *(general ONFH management; not specifically trialed in ANFH2 patients in the literature retrieved)*:
  - **Bisphosphonates / alendronate** — reported effective against ischemic bone necrosis in some series, aiming to reduce bone resorption and preserve structural integrity during the reparative phase. NCIT: `NCIT:C15986` (Pharmacotherapy); therapeutic agent class `NCIT:C285` (Bisphosphonate, if available) or specific CHEBI term for alendronate.
  - **Statins** — proposed to reduce adipogenic differentiation of marrow stem cells and lower intraosseous pressure, improving perfusion.
  - **Anticoagulants (e.g., enoxaparin)** — used where hypercoagulability/thromboembolic mechanisms are implicated (more relevant to secondary/acquired ONFH than to the TRPV4 vasoregulatory mechanism, but occasionally used empirically).
  - No TRPV4-channel-targeted pharmacotherapy (e.g., a TRPV4 antagonist) has been reported as clinically trialed in ANFH2 patients, though this is a mechanistically rational future therapeutic direction given the established gain-of-function mechanism.
- **Non-pharmacologic/physical:**
  - **Hyperbaric oxygen therapy (HBOT)** — reported to correct tissue ischemia/hypoxia, improve microcirculation, reduce blood viscosity, and promote angiogenesis; a controlled trial of 20 HBOT sessions reported sustained asymptomatic status at 7-year follow-up in treated patients (general ONFH literature).
- **Surgical/interventional:**
  - **Core decompression** (± bone grafting) — the mainstay joint-preserving procedure for early-stage (pre-collapse) disease; reduces intraosseous pressure, disrupts the sclerotic barrier to healing, and stimulates local angiogenesis and new bone formation. In one series, all ARCO Stage I lesions regressed to Stage 0 at 12-month follow-up post-decompression. **The ANFH2 proband underwent bilateral hip core decompression and bone grafting at age 21.** NCIT: `NCIT:C15329` (Surgical Procedure) or a more specific decompression/bone-grafting procedure term if available.
  - **Free vascularized fibular grafting (FVFG)** — indicated for smaller lesions (<300° of femoral head involvement) without preoperative collapse; provides both structural support and a new vascular supply to promote revascularization.
  - **Total hip arthroplasty (THA)** — definitive treatment for advanced/collapsed disease (Steinberg/ARCO Stage III–IV), as seen in the more severely affected ANFH2 siblings (Stage IV–V). NCIT: `NCIT:C15329` or a specific hip-replacement procedure term (`NCIT:C80355`-type arthroplasty code if available).
- **Supportive/rehabilitative:** Physical therapy, weight-bearing restriction/protected weight-bearing during the reparative phase, and pain management are standard adjuncts.
- **Experimental:** No TRPV4-specific targeted or gene-based experimental therapy for ANFH2 was identified in the literature retrieved (no relevant ClinicalTrials.gov NCT identified for TRPV4-directed osteonecrosis therapy in this search).
- **Treatment strategy:** Staging-driven treatment algorithm — pre-collapse (Ficat/ARCO 0–II): core decompression ± adjuncts (bone marrow aspirate/mesenchymal cell injection, bisphosphonates, HBOT); post-collapse, low-grade (IIIA, smaller lesion): FVFG or other joint-preserving osteotomy/grafting procedures; post-collapse, advanced (IIIB–IV): total hip arthroplasty. Because ANFH2 patients present with bilateral disease and often already at advanced stage, treatment planning must anticipate **staged or combined bilateral intervention**.

---

## 13. Prevention

- **Primary prevention:** No TRPV4-channel-specific primary prevention exists. For carriers of a known familial TRPV4 (or COL2A1) mutation, there is no established pharmacologic prophylaxis to prevent osteonecrosis onset; avoidance of superimposed acquired risk factors (corticosteroids, heavy alcohol use, trauma) in a known mutation carrier would be a reasonable precautionary/behavioral recommendation, though not formally studied.
- **Secondary prevention (early detection):** Given the young age of onset and high penetrance in the reported family, **surveillance MRI of both hips in at-risk relatives of a confirmed ANFH2 proband** would allow detection of pre-radiographic (Stage 0–I) disease, when joint-preserving core decompression is most effective — this is a reasonable extrapolated clinical strategy, not one formally validated in a screening trial.
- **Genetic screening/counseling:** Cascade genetic testing of first-degree relatives of an identified TRPV4-ANFH2 proband is appropriate given autosomal dominant inheritance with apparently high penetrance; genetic counseling should address the ~50% transmission risk to offspring.
- **Behavioral interventions:** Avoidance of corticosteroid overuse and heavy alcohol consumption remains generally advisable, though these were not implicated as contributing/modifying factors in the one reported ANFH2 pedigree.
- **Public health/prophylaxis:** Not applicable at a population level given the extreme rarity of this Mendelian entity.

---

## 14. Other Species / Natural Disease

- No naturally occurring TRPV4-associated osteonecrosis of the femoral head has been reported in non-human species in the literature retrieved by this search. TRPV4 orthologs are broadly conserved (mouse Trpv4, NCBI Gene ID 63873; also present in zebrafish and other vertebrates), and TRPV4 is functionally characterized across multiple species (e.g., zebrafish TRPV4 studies referenced in the ZFIN database), but a natural/spontaneous disease phenotype specifically analogous to ANFH2 has not been documented in veterinary or comparative-pathology literature retrieved here.
- **Comparative biology:** The role of TRPV4 in vascular tone regulation and osteoclast differentiation is functionally conserved across mammals (demonstrated in mouse models — see Section 15), supporting cross-species relevance of the proposed mechanism, but this is inferred from engineered mouse models rather than observed natural disease.
- **Zoonotic potential:** Not applicable (non-infectious, monogenic disorder).

---

## 15. Model Organisms

- **Mouse models (Trpv4 genetically engineered mice):**
  - **Global Trpv4-knockout mice** show a bone phenotype **opposite** to the human gain-of-function ANFH2 phenotype: "male TRPV4 knockout mice have reduced osteoclast activity and numbers, increased bone mass, and increased subchondral bone volume" — consistent with, and supportive of, the proposed gain-of-function mechanism in ANFH2 (i.e., loss of TRPV4 → less osteoclast activity/more bone; gain of TRPV4 function → implied increased osteoclast activity/bone loss, the inferred direction relevant to ANFH2, though a direct knock-in gain-of-function ANFH2 mouse model was not identified in this search).
  - Trpv4-knockout mice also show **reduced bone loss and reduced osteoclast function in an unloading-induced bone-loss model**, and TRPV4 has been shown to regulate steady-state Ca²⁺ influx at the late stage of osteoclast differentiation, essential for NFATc1-controlled transcription governing osteoclast terminal differentiation and resorptive capacity — mechanistic support (in the opposite/loss-of-function direction) for the human gain-of-function disease mechanism.
  - **Combined Trpv1/Trpv4 double-knockout mice** show increased bone mass, further supporting a role for TRPV4 (and possibly TRPV1) in normal bone-resorption homeostasis.
  - **Cartilage-specific Trpv4 knockout mice** and mice bearing other **gain-of-function Trpv4 knock-in alleles** (e.g., models of TRPV4 skeletal dysplasia) have been generated and used to study the mechanoregulatory role of TRPV4 in prenatal skeletal development (Science Advances, referenced in this search) and cartilage-specific TRPV4 effects on cilia/mechanosensation (Scientific Reports, srep29053) — these are the closest existing genetic models to the gain-of-function mechanism relevant to ANFH2, though they model skeletal dysplasia phenotypes rather than the vascular/femoral-head-osteonecrosis phenotype specifically. **No mouse model directly recapitulating femoral head osteonecrosis via the ANFH2 V829Wfs*3 (or an equivalent gain-of-function) TRPV4 allele was identified in this search** — this represents a genuine gap (a candidate `HUMAN_MODEL_MISMATCH`/knowledge-gap item: existing Trpv4 mouse models establish the channel's role in osteoclast and vascular biology generally, but fidelity of any specific model to the human ANFH2 femoral-head phenotype has not been demonstrated).
  - **Cellular models:** In vitro electrophysiological characterization of the mutant channel (heterologous expression system, likely HEK293-type cells based on standard methodology for such TRPV4 functional studies) was the direct functional model used in the discovery paper (PMID:27330106), demonstrating the gain-of-function sparklet/burst-open-time phenotype described above — this is an **IN_VITRO** functional/mechanistic model, not a disease model per se, but it is the key piece of direct causal/functional evidence for pathogenicity.
  - A separate report describes **novel gain-of-function TRPV4 mutations characterized using patient-derived dental pulp stem cells** differentiated along chondrogenic lineage (metatropic dysplasia context, PMC6709385) — an iPSC/patient-cell-derived model approach that could in principle be applied to ANFH2-specific variants (osteoclast or endothelial differentiation from patient-derived iPSCs) but has not yet been reported for the ANFH2 allele specifically.

- **Model limitations:** Existing Trpv4 mouse models (knockout, skeletal-dysplasia knock-in) capture TRPV4's general roles in bone remodeling and skeletal development but have not been shown to reproduce the specific femoral-head-restricted osteonecrosis phenotype of human ANFH2; the field currently relies on human pedigree/clinical data plus in vitro channel electrophysiology for causal evidence, without an established in vivo whole-organism disease model of ANFH2 itself.

---

## Summary of Key Ontology Term Suggestions

| Concept | Suggested term |
|---|---|
| Gene | TRPV4 — `hgnc:12716` |
| Disease (broad) | Osteonecrosis, MONDO general term; MONDO:0054551 (ANFH2 specific) |
| Phenotype: avascular necrosis of femoral head | `HP:0010734` |
| Phenotype: hip/groin pain | best available generic pain term; consider free text if no exact HP match |
| Phenotype: gait disturbance | `HP:0100787` |
| Phenotype: limited joint mobility | `HP:0002826` |
| GO BP: calcium ion transmembrane transport | `GO:0070588` |
| GO BP: osteoclast differentiation | `GO:0030316` |
| GO MF: calcium channel activity | `GO:0005262` |
| GO MF: calmodulin binding | `GO:0005516` |
| Cell type: osteoclast | `CL:0000092` |
| Cell type: vascular endothelial cell | `CL:0000115` |
| Cell type: vascular smooth muscle cell | `CL:0000359` |
| Anatomy: hip joint | `UBERON:0001360` |
| Anatomy: femur | `UBERON:0001417` |
| Treatment: pharmacotherapy | `NCIT:C15986` |
| Treatment: surgical procedure (core decompression / THA) | `NCIT:C15329` |
| Treatment: radiation/hyperbaric oxygen | consider `NCIT:C15313`-adjacent or a specific HBOT term if present in NCIT |

---

## Notable Gaps / Items Needing Further Verification Before Curation

1. **The specific ANFH2 TRPV4 variant's ClinVar accession/classification** was not directly retrieved in this search (ClinVar hits found were for other TRPV4 variants such as p.Arg269His, p.Arg315Trp, associated with related but distinct TRPV4-opathy phenotypes) — this should be directly queried in ClinVar/OAK before curation to confirm formal variant classification and accession ID for c.2480_2483delCCCG;c.2486T>A.
2. **Exact sex distribution and individual ages of the 4 affected ANFH2 siblings** were not fully itemized in the sources retrieved (only proband age 21 was specified) — the full case series table in PMID:27330106 (Table 1 in the original paper) should be consulted directly for per-individual phenotype data before writing an evidence-dense phenotype table.
3. **No second independent TRPV4-ANFH2 family** has been identified in the literature retrieved here — curation should flag that causal evidence rests on a single pedigree (n=1 family, n=4 affected individuals) plus supportive in vitro functional data, an important evidentiary caveat for a Mendelian gene-disease claim of this size.
4. OMIM #617383's full clinical synopsis text could not be directly fetched in this session (proxy connection error to omim.org) — recommend a direct OMIM API/manual lookup during curation to confirm the exact "Clinical Synopsis" field values (e.g., formally coded HPO-style synopsis terms) rather than relying solely on secondary summaries.

---

### Sources

- [Entry - #617383 - AVASCULAR NECROSIS OF FEMORAL HEAD, PRIMARY, 2 - OMIM](https://omim.org/entry/617383)
- [Entry - #608805 - AVASCULAR NECROSIS OF FEMORAL HEAD, PRIMARY, 1 - OMIM](https://www.omim.org/entry/608805)
- [Gain-of-function mutation in TRPV4 identified in patients with osteonecrosis of the femoral head — Mah et al., J Med Genet 2016 (PMID:27330106)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035228/) / [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC5035228/)
- [A novel mutation of COL2A1 in a large Chinese family with avascular necrosis of the femoral head](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8178877/)
- [Entry - *120140 - COLLAGEN, TYPE II, ALPHA-1; COL2A1 - OMIM](https://omim.org/entry/120140)
- [TRPV4‐pathy manifesting both skeletal dysplasia and peripheral neuropathy](https://onlinelibrary.wiley.com/doi/abs/10.1002/ajmg.a.35268)
- [Novel gain-of-function mutation of TRPV4 associated with accelerated chondrogenic differentiation of dental pulp stem cells derived from a patient with metatropic dysplasia](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6709385/)
- [TRPV4 Gene - GeneCards](https://www.genecards.org/card/TRPV4)
- [The Multifaceted Functions of TRPV4 and Calcium Oscillations in Tissue Repair](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10816018/)
- [TRPV4-mediates oscillatory fluid shear mechanotransduction in mesenchymal stem cells in part via the primary cilium](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5830574/)
- [Transient receptor potential vanilloid 1 and 4 double knockout leads to increased bone mass in mice](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7191598/)
- [Mechanoregulatory role of TRPV4 in prenatal skeletal development](https://www.science.org/doi/10.1126/sciadv.ade2155)
- [Cartilage-Specific Knockout of the Mechanosensory Ion Channel TRPV4](https://www.nature.com/articles/srep29053)
- [Femoral Head Avascular Necrosis: Background, Etiology, Epidemiology - Medscape](https://emedicine.medscape.com/article/86568-overview)
- [Femoral Head Avascular Necrosis - StatPearls - NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK546658/)
- [Avascular Necrosis of Femoral Head—Overview and Current State of the Art](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9223442/)
- [Osteonecrosis of the Femoral Head: an Updated Review of ARCO](https://pmc.ncbi.nlm.nih.gov/articles/PMC8216992/)
- [The Double-Line Sign — Radiology](https://pubs.rsna.org/doi/abs/10.1148/radiology.212.2.r99au13541)
- [Osteonecrosis Imaging - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK604199/)
- [Core decompression in early stages of femoral head osteonecrosis](https://link.springer.com/article/10.1007/s00264-001-0311-7)
- [The efficacy and safety of core decompression for the treatment of femoral head necrosis: a systematic review and meta-analysis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6737645/)
- [Indications for free vascularized fibular grafting for the treatment of osteonecrosis of the femoral head](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1988800/)
- [Etiology, pathology, and treatment of osteonecrosis of the femoral head](https://pmc.ncbi.nlm.nih.gov/articles/PMC11272257/)
- [The association of COVID-19 with the development of acute avascular necrosis of the head of the femur, apart from steroid usage](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12337778/)
- [Significant association of SREBP-2 genetic polymorphisms with avascular necrosis in the Korean population](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2600781/)
- [NM_021625.5(TRPV4):c.2471C>T (p.Ser824Leu) AND multiple conditions - ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV002494683/)
- [De novo TRPV4 Leu619Pro variant causes a new channelopathy characterised by giant cell lesions of the jaws and skull, skeletal abnormalities and polyneuropathy](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8867273/)
- [familial avascular necrosis of femoral head - National Organization for Rare Disorders / MONDO](https://rarediseases.org/mondo-disease/familial-avascular-necrosis-of-femoral-head/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 19 |
| On topic | 3 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMC:PMC5035228`: "All affected siblings with osteonecrosis of the femoral head harbored a heterozygous frameshift deletion in TRPV4"
  - closest text in source: "Siblings affected with osteonecrosis of the femoral head (black symbols) all harbour a heterozygous frameshift deletion in transient receptor potential vanilloid 4 (TRPV4) (TRPV4+/−)"
- `PMID:27330106`: "calcium overload, leading to endothelial dysfunction and vasoconstriction, resulting in bone loss at the hip"
  - closest text in source: "Together, this could cause Ca2+ overload, leading to endothelial dysfunction and vasoconstriction, resulting in bone loss at the hip"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 16 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 11 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0010734` (3 mentions) - the report calls it "Avascular necrosis of the capital femoral epiphysis", "Phenotype: avascular necrosis of femoral head"; HP calls it **Fibrous dysplasia of the bones**
- `HP:0100787` (2 mentions) - the report calls it "Gait disturbance", "Phenotype: gait disturbance"; HP calls it **Prostate neoplasm**
- `HP:0002826` (2 mentions) - the report calls it "Limited joint mobility", "Phenotype: limited joint mobility"; HP calls it **Halberd-shaped pelvis**
- `UBERON:0001417` (4 mentions) - the report calls it "Anatomy: femur"; UBERON calls it **skin of neck**
- `UBERON:0001360` (2 mentions) - the report calls it "Anatomy: hip joint"; UBERON calls it **deep circumflex iliac vein**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0054551` (2 mentions) - the report calls it "Avascular Necrosis of Femoral Head, Primary, 2", "ANFH2 specific"; MONDO calls it **avascular necrosis of femoral head, primary, 2**, and lists "ANFH2" among its other names
- `HP:0100559` (1 mention) - the report calls it "Asymmetric growth / limb length discrepancy"; HP calls it **Lower limb asymmetry**, and lists "Leg length discrepancy" among its other names
- `GO:0005262` (3 mentions) - the report calls it "GO MF: calcium channel activity"; GO calls it **calcium channel activity**
- `GO:0070588` (3 mentions) - the report calls it "GO BP: calcium ion transmembrane transport"; GO calls it **calcium ion transmembrane transport**
- `GO:0030316` (2 mentions) - the report calls it "GO BP: osteoclast differentiation"; GO calls it **osteoclast differentiation**
- `GO:0005516` (2 mentions) - the report calls it "GO MF: calmodulin binding"; GO calls it **calmodulin binding**
- `CL:0000092` (3 mentions) - the report calls it "Cell type: osteoclast"; CL calls it **osteoclast**
- `CL:0000115` (3 mentions) - the report calls it "Cell type: vascular endothelial cell"; CL calls it **endothelial cell**
- `CL:0000359` (3 mentions) - the report calls it "Cell type: vascular smooth muscle cell"; CL calls it **vascular associated smooth muscle cell**, and lists "vascular smooth muscle cell" among its other names
- `NCIT:C15986` (2 mentions) - the report calls it "Treatment: pharmacotherapy"; NCIT calls it **Pharmacotherapy**
- `NCIT:C15329` (3 mentions) - the report calls it "Treatment: surgical procedure (core decompression / THA)"; NCIT calls it **Surgical Procedure**, and lists "Surgical Procedures" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0054551` - called "Avascular Necrosis of Femoral Head, Primary, 2", "ANFH2 specific"
- `HP:0010734` - called "Avascular necrosis of the capital femoral epiphysis", "Phenotype: avascular necrosis of femoral head"
- `HP:0100787` - called "Gait disturbance", "Phenotype: gait disturbance"
- `HP:0002826` - called "Limited joint mobility", "Phenotype: limited joint mobility"