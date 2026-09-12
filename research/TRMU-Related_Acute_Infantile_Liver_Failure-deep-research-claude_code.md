---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-29T19:36:56.183600'
end_time: '2026-08-29T19:41:21.056582'
duration_seconds: 264.87
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: TRMU-Related Acute Infantile Liver Failure
  mondo_id: ''
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
  web_search_requests: 14
  num_turns: 27
  total_cost_usd: 1.3190936
  session_id: 947d87eb-a7bc-50ae-bd2b-57097ad6c44a
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 12
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 8
  validator_version: 0.2.1
term_validation:
  total_terms: 45
  verified: 42
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 33
  labels_matching: 25
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0009723
    reported_labels:
    - MONDO
    ontology_label: Leigh syndrome
  - term_id: CL:0000187
    reported_labels:
    - "muscle cell \u2014 for the myopathic phenotype"
    ontology_label: muscle cell
  - term_id: UBERON:0002107
    reported_labels:
    - Liver
    - 'Primary organ**: **Liver'
    ontology_label: liver
  labels_variant: 5
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TRMU-Related Acute Infantile Liver Failure
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **TRMU-Related Acute Infantile Liver Failure** covering all of the
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

I have gathered sufficient comprehensive, well-sourced material. Here is the complete research report.

I now have sufficient primary-source material to compile the comprehensive report.

---

# TRMU-Related Acute Infantile Liver Failure (TRMU Deficiency): Comprehensive Research Report

## 1. Disease Information

### Overview
TRMU-related acute infantile liver failure — clinically termed **TRMU deficiency** — is an autosomal recessive mitochondrial disorder caused by biallelic pathogenic variants in *TRMU* (tRNA 5-methylaminomethyl-2-thiouridylate methyltransferase, also called *MTU1*). It is characterized by **transient, life-threatening acute liver failure** presenting in infancy (classically ages 2–4 months), accompanied by severe lactic acidosis, hypoglycemia, hyperammonemia, and poor weight gain. A defining and clinically critical feature is that, unlike most mitochondrial hepatopathies, **survivors of the acute episode typically show full clinical and biochemical resolution of liver disease with no recurrence** — hence "transient" ([GeneReviews, NBK591557](https://www.ncbi.nlm.nih.gov/books/NBK591557/), updated May 2023; [OMIM #613070](https://omim.org/entry/613070)).

### Key Identifiers
| Resource | ID | Notes |
|---|---|---|
| OMIM (phenotype) | **#613070** — LIVER FAILURE, INFANTILE, TRANSIENT (LFIT) | [omim.org/entry/613070](https://www.omim.org/entry/613070) |
| OMIM (gene) | **\*610230** — TRMU | Chromosome 22q13.31 ([omim.org/entry/610230](https://www.omim.org/entry/610230)) |
| MONDO | **MONDO:0009723** | TRMU deficiency (autosomal recessive, Leigh-syndrome-spectrum related disorder) |
| Orphanet | **ORPHA:217371** — Acute infantile liver failure due to synthesis defect of mtDNA-encoded proteins; also cross-referenced under ORPHA:254864 (Mitochondrial myopathy with reversible cytochrome c oxidase deficiency) | [orpha.net/en/disease/detail/217371](https://www.orpha.net/en/disease/detail/217371) |
| HGNC | HGNC:25481 (TRMU) | |
| Gene symbol/aliases | *TRMU*; formerly *MTU1*, *SDO1*, *KIAA0812* | |
| GeneReviews | NBK591557 | Vogel et al, updated 2023 |

### Synonyms
Reversible infantile liver failure (RILF); transient infantile liver failure due to TRMU mutations; mitochondrial DNA depletion-like syndrome due to TRMU deficiency; MTU1 deficiency.

### Evidence base
Information is derived from **aggregated disease-level resources** (OMIM, Orphanet, GeneReviews, MalaCards) built from pooled case series and cohort studies (not raw EHR data) — most authoritatively the GeneReviews chapter (Vogel et al., 2023) and the largest published cohort to date, Murali et al. and colleagues' *Genetics in Medicine* study of 62 individuals from 56 families (Vogel CH et al., "Genotypic and phenotypic spectrum of infantile liver failure due to pathogenic TRMU variants," *Genet Med* 2022 Dec, PMID: [36305855](https://pubmed.ncbi.nlm.nih.gov/36305855/)).

---

## 2. Etiology

### Disease Causal Factors
The sole known cause is **biallelic (homozygous or compound heterozygous) pathogenic loss-of-function variants in *TRMU*** (22q13.31), which abolish or reduce the enzyme's 2-thiolation activity on mitochondrial tRNAs. This is a purely genetic/mitochondrial-translation disease; there is no known infectious or purely environmental primary cause, though physiologic/metabolic **stress is a key disease-triggering cofactor** (see below).

### Genetic Risk Factors
- **Causal variants**: missense, nonsense, frameshift, splice-site, and small indel variants throughout *TRMU*; sequence analysis detects ~93% (26/28) of pathogenic alleles, with gene-targeted deletion/duplication analysis detecting the remainder (~7%, 2/28) (GeneReviews).
- **Founder variant**: **c.229T>C (p.Tyr77His)** is a well-documented founder mutation in the **Yemenite Jewish population**, first described by Zeharia et al. (2009, *Am J Hum Genet*, PMID: [19732863](https://pubmed.ncbi.nlm.nih.gov/19732863/)), the paper that originally established TRMU as the causal gene for this syndrome.
- **Loss-of-function (nonsense/frameshift/splice) variants** are significantly associated with **worse survival** than missense/in-frame indel variants (10/20 deaths in LOF carriers vs. 10/42 in missense/in-frame carriers; p=0.022; GeneReviews, citing Vogel et al. 2023).
- **c.2T>A (p.Met1?)** (loss of the start codon) is specifically associated with **early mortality despite aggressive management** (observed in 5 deceased individuals).

### Environmental / Physiologic Risk Factors
- **Age window of vulnerability**: acute liver failure occurs almost exclusively within the first year of life (43/62 individuals in the largest cohort), with a specific window of increased risk around 1–4 months of age.
- **Intercurrent illness/physiologic stress**: episodes are typically precipitated by febrile illness or other metabolic stress; patients are often well between episodes.
- **Low endogenous cysteine**: infants have a **physiologic nadir in cystathionase (cystathionine γ-lyase) activity**, making cysteine a *conditionally essential* amino acid in the neonatal/infantile period — this is the key gene-environment (developmental) interaction underlying disease timing (Murali et al., *Mol Genet Metab* 2021, PMID: [33485800](https://pubmed.ncbi.nlm.nih.gov/33485800/)).
- A case report documents **cytomegalovirus infection aggravating/precipitating fatal hepatic dysfunction** in a TRMU-mutation carrier (Cureus case report), illustrating infection as a secondary stressor rather than a primary cause.

### Protective Factors
- **Presymptomatic/prenatal cysteine + N-acetylcysteine (NAC) supplementation** in at-risk siblings (identified via prior affected sibling) is associated with a **milder clinical course**, less severe acidosis/liver dysfunction, and fewer hospitalizations (GeneReviews).
- The **p.Tyr77His founder allele** itself appears relatively protective/lower-mortality compared with other genotypes (0/8 deaths in homozygotes; 1/9 in compound heterozygotes in the Vogel et al. cohort).

### Gene-Environment Interaction
The central gene-environment interaction in this disease is the intersection of (1) genetically reduced TRMU thiolation capacity with (2) the developmentally programmed, transient physiologic deficiency of endogenous cysteine synthesis in infancy. This is why the disease is age-restricted and why exogenous cysteine/NAC supplementation is disease-modifying rather than merely supportive.

---

## 3. Phenotypes

Frequencies below are from the largest published cohort of **60 untreated symptomatic children** (GeneReviews/Vogel et al. 2023):

| Phenotype | Frequency | Onset | Suggested HPO term |
|---|---|---|---|
| Liver disease (elevated transaminases/liver dysfunction) | 58/60 (97%) | 2–4 months typical | HP:0001392 (Abnormality of the liver) |
| Lactic acidosis | 44/60 (73%) | Acute episodes | HP:0003128 (Lactic acidosis) |
| Jaundice | 34/60 (57%) | With acute episodes | HP:0000952 (Jaundice) |
| Failure to thrive | 33/60 (55%) | Progressive | HP:0001508 (Failure to thrive) |
| Emesis/diarrhea | 28/60 (47%) | Acute episodes | HP:0002013 (Vomiting) / HP:0002014 (Diarrhea) |
| Neurodevelopmental delay | 24/60 (40%) | Often resolves with liver recovery | HP:0012758 (Neurodevelopmental delay) |
| Hypotonia | 20/60 (33%) | Acute/subacute | HP:0001252 (Hypotonia) |
| Hypoglycemia | 11/28 assessed (39%) | Acute episodes | HP:0001943 (Hypoglycemia) |
| Hepatomegaly | 13/60 (22%) | Acute episodes | HP:0002240 (Hepatomegaly) |
| Cardiomyopathy | 5/60 (8%) | Variable | HP:0001638 (Cardiomyopathy) |
| Seizures | 4/60 (7%) | Acute/severe cases | HP:0001250 (Seizures) |
| Coagulopathy | Common in acute episodes (specific % not separately tabulated) | Acute | HP:0001928 (Abnormal coagulation) |
| Hyperammonemia | Reported as metabolic derangement | Acute | HP:0001987 (Hyperammonemia) |
| Sensorineural hearing loss | Reported in a subset (broader clinical spectrum) | Variable, can be later-onset | HP:0000407 (Sensorineural hearing loss) |
| Ragged red fibers on muscle biopsy | Subset (histologic finding) | — | HP:0003200 (Ragged-red muscle fibers) |

### Phenotype Characteristics
- **Onset**: classically 2–4 months of age; presymptomatic/prenatally treated at-risk siblings can be identified and managed before symptom onset.
- **Course**: **episodic/acute and — in survivors — self-limited and reversible**, distinguishing this from most other mitochondrial hepatopathies (e.g., DGUOK, MPV17, POLG-related disease), which are progressive. Genetics in Medicine cohort work also documents a broader phenotypic spectrum, including patients **without overt liver failure**, some presenting instead with **Leigh-syndrome-like neuroimaging** (symmetric restricted diffusion in thalami/putamen), chronic respiratory failure, or isolated myopathy (Murali et al. 2021, PMID: 33485800).
- **Severity/variability**: highly variable — from fatal neonatal multiorgan failure to mild, self-resolving transaminitis; genotype (LOF vs. missense) and treatment timing are major severity modifiers.
- **Hepatic copper accumulation** has been reported as a possible secondary, cholestasis-associated feature in at least one case (Grover et al., *JIMD Reports*, PMID: [25665837](https://pubmed.ncbi.nlm.nih.gov/25665837/)), postulated to be secondary to cholangiopathy rather than a primary TRMU effect.
- **Quality of life**: for survivors, long-term outcomes are generally favorable; among 25 followed individuals in the GeneReviews cohort, 9 had full resolution of developmental delay following liver recovery, while 5 had persistent developmental delays — indicating QOL impact is concentrated in the acute period and in the minority with residual neurodevelopmental sequelae.

---

## 4. Genetic/Molecular Information

### Causal Gene
- **TRMU** (HGNC:25481; OMIM \*610230), chromosome **22q13.31**. Encodes **tRNA 5-methylaminomethyl-2-thiouridylate methyltransferase** (also known as mitochondrial tRNA-specific 2-thiouridylase 1, MTU1).

### Gene Function
TRMU is a nuclear-encoded, mitochondrially targeted enzyme that catalyzes **2-thiolation of uridine at the wobble (position 34) anticodon position** of three mitochondrial tRNAs — **mt-tRNA^Lys, mt-tRNA^Glu, and mt-tRNA^Gln** — generating the modified nucleoside **5-taurinomethyl-2-thiouridine (τm5s2U)**. This modification is essential for accurate codon-anticodon pairing, translational fidelity, and structural stability of these tRNAs (PubMed 16513084; Suzuki lab reviews, WIREs RNA 2011).

### Pathogenic Variants
- **Variant types**: missense (most common), nonsense, frameshift, splice-site, small indels, and gene-level deletion/duplication (rare).
- **ACMG classification**: cataloged in ClinVar (e.g., RCV001277295, RCV000351468) predominantly as Pathogenic/Likely Pathogenic when biallelic and segregating with disease.
- **Allele frequency**: specific gnomAD population allele-frequency figures were not identified in available secondary sources beyond the qualitative statement that overall disease prevalence is **<1 per 1,000,000** (OMIM) with **founder-elevated frequency of c.229T>C (p.Tyr77His) in the Yemenite Jewish population**.
- **Somatic vs. germline**: exclusively germline (biallelic recessive); no somatic TRMU disease association reported.
- **Functional consequence**: **loss of function** — reduced or absent thiolation activity leads to loss of τm5s2U modification, reduced steady-state levels of the three target mt-tRNAs, impaired mitochondrial translation of OXPHOS subunits, and downstream **respiratory chain complex I, III, and IV deficiency** (GeneReviews; muscle biopsy shows decreased complex I/III/IV activity and ragged red fibers).
- A 2024 mechanistic paper (*Nucleic Acids Research*, doi:10.1093/nar/gkad1197) shows that **pathological MTU1 mutations promote proteolysis of the MTU1 protein via mitochondrial caseinolytic peptidase (CLPP)**, providing a protein-stability mechanism for how missense variants cause loss of function.

### Modifier Genes
- **TRMU acts as a nuclear modifier gene** for the phenotypic expression of the deafness-associated **mitochondrial 12S rRNA m.1555A>G mutation** — i.e., TRMU variants can modulate penetrance/severity of aminoglycoside-induced and non-syndromic hearing loss in carriers of 12S rRNA mutations (Guan et al., PMID: 16513084). This is a related but mechanistically and clinically distinct TRMU-associated phenotype (maternally inherited deafness) from the infantile liver failure syndrome, and should not be conflated with it.
- Related paralogous tRNA-thiolation pathway genes **GTPBP3** and **MTO1** cause overlapping/similar τm5s2U-modification-deficiency phenotypes (deafness, reversible liver failure, hypertrophic cardiomyopathy, lactic acidosis) and are relevant differential-diagnosis/pathway partners.

### Epigenetic Information
A study describes **microRNA-mediated differential expression of TRMU, GTPBP3, and MTO1** in cell models of mitochondrial-DNA disease (PMC5524753), suggesting post-transcriptional/epigenetic-adjacent regulation of this pathway, though this is not established as a primary disease mechanism in TRMU deficiency itself.

### Chromosomal Abnormalities
No large-scale chromosomal rearrangements (aneuploidy, translocation) are reported as a cause; disease is driven by intragenic sequence-level variants.

---

## 5. Environmental Information

- **No toxic/occupational/pollutant etiology** is established; this is a monogenic mitochondrial disease.
- **Nutritional/metabolic environment**: the infant's transient physiologic cysteine deficiency (low cystathionase activity) functions as the key "environmental" (developmental-metabolic) permissive factor.
- **Infectious triggers**: intercurrent viral illness (e.g., CMV, reported in one fatal case) can precipitate or worsen acute decompensation, acting as a physiologic stressor rather than a primary cause.
- **Drugs to avoid** (iatrogenic environmental risk factors that worsen mitochondrial function or increase metabolic demand): corticosteroids, valproic acid, prolonged propofol infusion, fasting, and acetaminophen during liver dysfunction — all flagged in GeneReviews management guidance as agents that can exacerbate hepatic/mitochondrial decompensation.

---

## 6. Mechanism / Pathophysiology

### Causal Chain
1. **Molecular trigger**: Biallelic *TRMU* loss-of-function variants → loss of 2-thiouridylase activity on mt-tRNA^Lys, mt-tRNA^Glu, mt-tRNA^Gln (loss of τm5s2U wobble modification).
2. **RNA-level consequence**: Reduced steady-state levels/stability of thio-modified mitochondrial tRNAs; impaired aminoacylation and codon-anticodon decoding fidelity.
3. **Translational consequence**: Impaired mitochondrial protein synthesis — specifically of the 13 mtDNA-encoded OXPHOS subunits — causing **combined respiratory chain deficiency** (complexes I, III, IV, all of which contain mtDNA-encoded subunits reliant on these tRNAs).
4. **Cellular consequence — proteostress/UPR activation**: A key mechanistic paper (Cell Reports, PMID: 29320742) shows that defective mt-tRNA taurine modification (via Mto1/Trmu loss) causes **mistrafficking and cytoplasmic aggregation/misfolding of nuclear-DNA-encoded mitochondrial proteins** (e.g., OPA1), which **activates a cytotoxic unfolded protein response (UPR)** and global proteostasis stress — a mechanism distinct from, and additive to, simple OXPHOS insufficiency.
5. **Tissue/organ consequence**: Hepatocyte energy failure, cell death (apoptosis/necrosis), and macrophage infiltration. A liver-specific conditional *Mtu1* knockout mouse model shows **hepatocellular injury with karyomegaly/multinucleation, macrophage infiltration, and spotty necrosis, without fibrosis** — closely recapitulating human RILF histology (PLOS Genetics, PMID: 27689697; follow-up NAR work).
6. **Clinical manifestation**: Acute hepatic decompensation (jaundice, coagulopathy, transaminitis), systemic lactic acidosis (impaired oxidative phosphorylation → compensatory anaerobic glycolysis), hypoglycemia, and (in a subset) CNS involvement resembling Leigh syndrome (thalamic/putaminal restricted diffusion) and cardiomyopathy.
7. **Reversibility mechanism**: Because the defect is a modifiable post-transcriptional RNA modification rather than a structural/genomic lesion, and because the developmental cysteine deficiency is time-limited, **hepatocyte and mitochondrial function can recover once the infant ages past the vulnerable cysteine-deficient window and/or receives exogenous sulfur-donor supplementation** — explaining the "transient" clinical hallmark unique among mitochondrial hepatopathies.

### Molecular Pathways
- Mitochondrial tRNA wobble-position modification pathway (τm5s2U biosynthesis: TRMU, GTPBP3, MTO1 cooperate).
- Mitochondrial translation machinery (mitoribosome-dependent synthesis of OXPHOS subunits).
- Oxidative phosphorylation / electron transport chain (Complexes I, III, IV).
- Unfolded protein response (mitochondrial and cytosolic UPR) triggered by protein mistargeting.

### Cellular Processes
Apoptosis/necrosis of hepatocytes; mitochondrial biogenesis impairment; proteostasis/UPR activation; inflammatory macrophage recruitment; (in bone-related studies) impaired osteogenic differentiation has also been linked to Mtu1 defects (Cell Death & Disease, PMC on osteogenic differentiation), suggesting a broader cell-differentiation impact of τm5s2U loss beyond hepatocytes.

### Protein Dysfunction
Loss-of-function/reduced enzymatic activity of TRMU protein; some pathogenic missense variants additionally **destabilize the protein and target it for proteolysis via mitochondrial CLPP protease**, compounding the enzymatic defect with reduced protein abundance (NAR 2024, doi:10.1093/nar/gkad1197).

### Metabolic Changes
Lactic acidosis (impaired pyruvate oxidation via ETC dysfunction); hypoglycemia (impaired hepatic gluconeogenesis/energy failure); hyperammonemia (impaired urea cycle function secondary to hepatocellular failure); disrupted sulfur amino acid (cysteine/taurine) metabolism as the central biochemical lever of both pathogenesis and treatment.

### Immune System Involvement
Secondary innate immune activation — **macrophage infiltration** into injured liver tissue is a consistent histologic finding in both human liver biopsies and the mouse model, reflecting a response to hepatocyte injury rather than primary autoimmune/immunodeficiency pathology.

### Tissue Damage Mechanisms
Hepatocellular necrosis/apoptosis, oxidative-phosphorylation failure-driven energy crisis, and proteostress-induced cytotoxicity converge on hepatocyte death; histologically the human liver shows bridging fibrosis, cirrhosis (in some cases), steatosis, and mitochondrial proliferation on biopsy (GeneReviews).

### Biochemical Abnormalities
Specific enzymatic defect: loss of mitochondrial tRNA 2-thiouridylase activity (EC 2.8.1.-); combined respiratory chain complex I, III, IV deficiency on muscle biopsy enzymology.

### Suggested Ontology Terms
- **GO (Biological Process)**: GO:0002143 (tRNA wobble position uridine thiolation), GO:0032543 (mitochondrial translation), GO:0006120 (mitochondrial electron transport, NADH to ubiquinone), GO:0034341 (response to type II interferon — not core), GO:0006986 (response to unfolded protein / UPR-related terms), GO:0006915 (apoptotic process).
- **GO (Cellular Component)**: GO:0005739 (mitochondrion), GO:0005759 (mitochondrial matrix), GO:0005743 (mitochondrial inner membrane).
- **CL (Cell Type)**: CL:0000182 (hepatocyte), CL:0000235 (macrophage), CL:0000187 (muscle cell — for the myopathic phenotype).

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary organ**: **Liver** (UBERON:0002107) — the dominant and most consistent manifestation.
- **Secondary/associated organ involvement**: brain (Leigh-syndrome-like lesions in thalami, putamen, basal nuclei, pontine tracts — UBERON:0001897 thalamus, UBERON:0001874 putamen), heart (cardiomyopathy — UBERON:0000948), skeletal muscle (myopathy, ragged red fibers — UBERON:0001134), inner ear (sensorineural hearing loss, in the broader spectrum/related deafness phenotype — UBERON:0001846 cochlea).
- **Body systems**: hepatic, metabolic/endocrine (hypoglycemia, lactic acidosis), hematologic (coagulopathy), neurologic, cardiovascular, and (in related phenotypes) audiologic.

### Tissue and Cell Level
- Hepatocytes (CL:0000182) — primary target of injury.
- Kupffer cells/macrophages (CL:0000235) — secondary inflammatory infiltration.
- Skeletal muscle fibers with ragged red fiber morphology (mitochondrial proliferation).
- Cochlear hair cells (in zebrafish model and in human deafness-associated phenotype).

### Subcellular Level
- **Mitochondrial matrix** (GO:0005759) — site of tRNA modification defect and impaired translation.
- **Mitochondrial inner membrane** (GO:0005743) — site of the respiratory chain complexes affected.
- Cytoplasm — secondary site of misfolded/mistargeted protein aggregation (proteostress mechanism).

### Localization
Diffuse/bilateral, symmetric involvement is typical for the brain lesions (symmetric thalamic/putaminal restricted diffusion) — not lateralized. Liver involvement is diffuse (whole-organ hepatocellular dysfunction), not focal.

---

## 8. Temporal Development

- **Onset**: typically **2–4 months of age** (infantile), occasionally as early as neonatal or as late as ~1 year; presymptomatic identification possible in at-risk siblings via prenatal/newborn testing.
- **Onset pattern**: **acute** — episodes of decompensation are abrupt, often precipitated by intercurrent illness.
- **Disease course pattern**: **episodic and, in survivors, self-limited/monophasic** — this is the disease's defining feature. Acute liver failure occurs only in the first year of life (43/62 in the largest cohort); survivors of the initial episode show clinical/biochemical resolution and **no further episodes** (OMIM #613070).
- **Progression rate**: rapid during the acute episode (can progress to multiorgan failure and death within weeks); but the overall disease is **not chronically progressive** in survivors, unlike most mitochondrial hepatopathies.
- **Critical period**: the first ~4–6 months of life, corresponding to the developmental nadir of endogenous cystathionase activity — the key window for both risk and for the protective effect of early cysteine/NAC supplementation.
- **Remission**: spontaneous biochemical/clinical resolution occurs in survivors after the acute window passes, and is further improved by treatment (cysteine supplementation); this is not "treatment-induced remission" in the oncologic sense but genuine reversal of the acute hepatopathy.

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence**: <1 per 1,000,000 (OMIM), consistent with an ultra-rare disease.
- **Cohort size reported to date**: 62 individuals from 56 families in the largest combined cohort (GeneReviews/Vogel et al. 2023, *Genet Med*, PMID: 36305855).

### Inheritance Pattern
- **Autosomal recessive.** For carrier parents: 25% risk of an affected child, 50% risk of a carrier child, 25% risk of an unaffected/non-carrier child per pregnancy (GeneReviews).

### Penetrance / Expressivity
- Penetrance and expressivity are **variable** — presentation ranges from asymptomatic/mild transaminitis to fatal multiorgan failure, with genotype (LOF vs. missense) as a major modifier of severity.

### Founder Effects
- **c.229T>C (p.Tyr77His)** is a well-established founder variant in the **Yemenite Jewish population**, first reported by Zeharia et al. (2009, PMID: 19732863).

### Consanguinity
- As an autosomal recessive disease, consanguineous unions increase risk in affected families/populations, consistent with the founder-population pattern described.

### Population Demographics
- Highest documented ancestry association: **Yemenite Jewish** founder population; cases are otherwise reported across diverse ethnicities/geographies (cohorts include patients from the US, China, and elsewhere), indicating global but very low-frequency distribution with no single dominant geographic endemic focus outside the noted founder population.
- **Sex ratio**: no sex predilection reported (autosomal recessive; no data suggesting skew).
- **Age distribution of affected individuals**: concentrated in the first year of life at symptom onset; median age at death (in fatal cases) reported as ~3 months.

---

## 10. Diagnostics

### Clinical/Laboratory Tests
- **Liver function panel**: elevated transaminases (AST/ALT), elevated bilirubin, coagulopathy (elevated INR/PT).
- **Metabolic panel**: elevated serum/plasma lactate (HP:0002151), hypoglycemia, hyperammonemia.
- **Muscle biopsy**: ragged red fibers; decreased respiratory chain complex I, III, IV enzyme activities.
- **Liver biopsy histology**: bridging fibrosis, cirrhosis, steatosis, mitochondrial proliferation.
- **Brain MRI**: variable lesions in thalami, putamen, basal ganglia, and pontine tracts (Leigh-syndrome-like), which may normalize after clinical recovery.

### Genetic Testing
- **Diagnosis is established by molecular genetic testing** identifying biallelic pathogenic *TRMU* variants.
- **Approach**: mitochondrial disease, cholestasis, or acute infantile liver failure multigene panels; or comprehensive genomic testing (exome/genome sequencing) when the phenotype is broad/atypical.
- **Yield**: sequence analysis detects ~93% of pathogenic alleles (26/28); deletion/duplication analysis detects the remainder (~7%, 2/28) (GeneReviews Table 2).
- **Prenatal/presymptomatic testing**: feasible and clinically used in at-risk families with a known familial variant, enabling presymptomatic/prenatal cysteine supplementation (as documented in multiple case reports).

### Differential Diagnosis (from GeneReviews)
Deoxyguanosine kinase (DGUOK) deficiency; Leigh syndrome (>90 causal genes); POLG-related Alpers-Huttenlocher syndrome; SERAC1 deficiency; other mtDNA maintenance disorders (MPV17, DGUOK); organic acidemias (propionic acidemia, methylmalonic acidemia); fatty acid oxidation disorders (MCAD, VLCAD, SCAD deficiency); glycogen storage disease type Ia. Related genes in the same τm5s2U-modification pathway — **GTPBP3** and **MTO1** — cause phenotypically overlapping disease (deafness, reversible liver failure, hypertrophic cardiomyopathy, lactic acidosis) and should specifically be considered/excluded.

### Screening
No population-based newborn screening currently exists for TRMU deficiency specifically (it is not part of standard NBS panels); the recommended approach in suspected/at-risk cases is **targeted familial variant testing and prenatal diagnosis** once a proband is identified, combined with a low-risk empiric-treatment strategy (starting cysteine/NAC supplementation) in symptomatic infants with compatible biochemistry (persistent lactic acidosis + hypoglycemia) even before molecular confirmation, given its safety and time-critical benefit (Murali et al. 2021, PMID: 33485800).

---

## 11. Outcome/Prognosis

### Survival and Mortality
- **Mortality among symptomatic children**: 20/60 (33%) died in the largest reported cohort.
  - Causes: 8 from liver failure complications, 8 from multiorgan failure, 3 from cardiorespiratory failure, 1 from sepsis.
  - **Median age at death: 3 months.**
- **Overall cohort survival** (all 62 individuals, symptomatic and presymptomatic combined): **42/62 alive at a median age of 6.8 years**, median follow-up 3.6 years (Vogel et al. 2023 per WebSearch synthesis of GeneReviews/GIM data).
- **Impact of cysteine/NAC supplementation on survival**: survival beyond acute decompensation was **84% in supplemented children vs. 61% in unsupplemented children** (GeneReviews, citing Vogel et al. 2023) — a substantial, clinically actionable treatment effect.
- **Genotype effect on survival**: LOF variants → 10/20 deaths; missense/in-frame indel variants → 10/42 deaths (p=0.022). The Yemenite founder variant p.Tyr77His is associated with the lowest mortality (0/8 homozygotes, 1/9 compound heterozygotes died).
- **Follow-up duration by variant class**: nonsense/frameshift/splice variant carriers had shorter average follow-up (38 months) than missense/in-frame indel carriers (78 months), consistent with earlier mortality in the LOF group.

### Morbidity / Functional Outcomes
- Among 25 long-term followed individuals: **9 had full resolution** of neurodevelopmental delay after liver recovery; **5 had persistent developmental delays.**
- **Liver transplantation does not appear to improve overall survival**: 11 children underwent orthotopic liver transplantation at a median age of 4 months, but two post-transplant deaths were reported, and GeneReviews states transplantation "did not influence overall survival" — an important finding given that this is otherwise a self-limited disease, meaning transplant may treat a transient problem with a permanent, high-risk intervention.

### Prognostic Factors
- Genotype (LOF vs. missense), timing of cysteine/NAC initiation (pre-symptomatic/early vs. late), and severity of the initial acute episode are the principal prognostic determinants identified to date.

---

## 12. Treatment

### Targeted (Disease-Modifying) Therapy: Sulfur-Donor Supplementation
This is the **only disease-specific/targeted therapy** currently established, and represents a genuine precision-metabolic intervention aimed directly at the enzymatic substrate deficiency.

- **Regimen**: combined **L-cysteine** (85–300 mg/kg/day, goal 300 mg/kg/day) **and N-acetylcysteine (NAC)** (70–150 mg/kg/day; proposed total combined goal 300 mg/kg/day with 150 mg/kg/day as NAC) (GeneReviews; Murali et al. 2021, PMID: 33485800).
- **Duration**: minimum through the first year of life (the vulnerable cysteine-deficient developmental window).
- **Mechanism**: provides exogenous sulfur donor to compensate for reduced TRMU enzymatic capacity and for the physiologic infantile cystathionase nadir, increasing thiouridylation of residual/partially functional mitochondrial tRNAs.
- **Evidence**: multiple case reports (e.g., Sasarman et al., ScienceDirect S2214426918301332 — "L-Cysteine supplementation prevents liver transplantation in a patient with TRMU deficiency") and cohort data (84% vs. 61% survival, above) support benefit; presymptomatic/prenatal initiation produces the mildest courses.
- **NCIT term suggestion**: NCIT:C15986 (Pharmacotherapy) as the treatment action, with `therapeutic_agent` bound to CHEBI for L-cysteine (CHEBI:17561) and N-acetylcysteine (CHEBI:47704).

### Supportive Care
- Management of hypoglycemia, lactic acidosis, coagulopathy, and hyperammonemia during acute episodes.
- Feeding support (may require gastrostomy tube) for failure to thrive.
- Seizure management as needed.
- Cardiac monitoring (given cardiomyopathy risk).
- Developmental/early intervention services (ages 0–3) and special education as needed for children with persistent neurodevelopmental delay.
- NCIT terms: NCIT:C15747 (Supportive Care), NCIT:C15302 (Physical Therapy)/rehabilitation as applicable.

### Surgical/Interventional
- **Orthotopic liver transplantation**: has been performed (11 children at median age 4 months in the largest cohort) for hepatopathy unresponsive to medical management, but **does not appear to improve overall survival** compared with medical management given the disease's transient/reversible natural history — a critical nuance for clinical decision-making (avoid unless truly refractory, given the risk of transplanting a self-limited disease). NCIT:C15289 (Organ Transplantation).

### Agents to Avoid (iatrogenic risk)
- **Corticosteroids** (increase metabolic demand).
- **Valproic acid** and **prolonged propofol infusion** (mitochondrial toxicity/inhibition).
- **Fasting** (worsens hypoglycemia and metabolic demand).
- **Acetaminophen** during active liver dysfunction.

### Experimental/Research Directions
No gene therapy, RNA-based therapy, or targeted molecular therapy beyond sulfur-donor supplementation is currently in clinical trials specifically for TRMU deficiency, per available search results; mechanistic work on CLPP-mediated proteolysis of mutant MTU1 protein (NAR 2024) suggests a potential future therapeutic angle (e.g., CLPP inhibition to stabilize residual mutant protein), but this remains preclinical.

### Treatment Strategy / Algorithm
Given the low risk and potential high benefit, GeneReviews and Murali et al. recommend **empiric initiation of combined L-cysteine + NAC supplementation in any infant with persistent lactic acidosis and hypoglycemia suggestive of TRMU deficiency, even prior to molecular confirmation**, alongside standard supportive metabolic/hepatic care, while genetic testing is pending.

---

## 13. Prevention

### Primary Prevention
No population-level primary prevention (e.g., vaccination) applies to this genetic disease. The principal actionable "prevention" is **presymptomatic identification and early/prenatal cysteine-NAC supplementation** in at-risk siblings once a family's causal variant is known — documented to blunt disease severity substantially.

### Screening and Early Detection
- **Genetic carrier screening / cascade testing**: recommended in families with a known affected child, especially relevant in populations with elevated carrier frequency (e.g., Yemenite Jewish ancestry) — following the standard ACMG/genetic-counseling framework for autosomal recessive disease.
- **Prenatal diagnosis**: has been used clinically (e.g., a documented case of prenatal L-cysteine initiation in the third trimester based on prenatal molecular diagnosis).
- Not currently part of routine population newborn screening panels.

### Genetic Counseling
Standard autosomal recessive counseling: 25%/50%/25% recurrence risk pattern per pregnancy for carrier couples; particular relevance for genetic counseling in Yemenite Jewish families given the founder variant.

### Prophylaxis
Early/prophylactic cysteine + NAC supplementation in genetically identified at-risk (presymptomatic) infants functions as a form of secondary/tertiary prevention, reducing severity of the first (and typically only) disease episode.

---

## 14. Other Species / Natural Disease

- No naturally occurring TRMU-deficiency disease has been reported in companion animals or wildlife in the literature surveyed; this appears to be a laboratory-model-only cross-species picture (see Model Organisms, below) rather than a naturally occurring veterinary disease.
- **Orthologous gene**: *Trmu*/*Mtu1* is conserved across vertebrates (mouse *Trmu*, NCBI Gene; zebrafish *trmu*/*mtu1*, ZFIN ZDB-GENE-050522-540), reflecting deep evolutionary conservation of the mitochondrial tRNA thiolation pathway.

---

## 15. Model Organisms

### Zebrafish (*Danio rerio*)
- **mtu1 (trmu) knockout zebrafish** (Zhou et al., *Nucleic Acids Research* 2018, PMID: [30137487](https://pubmed.ncbi.nlm.nih.gov/30137487/); [full text](https://academic.oup.com/nar/article/46/20/10930/5077603)) show:
  - Abolished 2-thiouridine modification of mt-tRNA^Lys, mt-tRNA^Glu, mt-tRNA^Gln.
  - Impaired mitochondrial translation, respiratory complex activity reduced to **38–83% of wild-type**, mitochondrial ATP production reduced to **~51%** in homozygous mutants.
  - **Auditory/vestibular phenotype**: abnormal startle response and swimming behavior (~42% of larvae abnormal swimming, ~23% weak/absent startle), reduced saccular otolith size, reduced hair cell numbers and hair bundle density in inner ear structures — modeling the **deafness** component of the human TRMU-associated phenotypic spectrum, though this particular model did not recapitulate liver pathology at the stages examined.
- A related zebrafish model of **Mto1** ablation (pathway partner gene) shows **hypertrophic cardiomyopathy** via mitochondrial RNA maturation deficiency (PMC8096277), relevant as a comparative model for the cardiomyopathy phenotype seen in a subset of human TRMU-deficiency patients.

### Mouse (*Mus musculus*)
- **Global *Mtu1* (Trmu) knockout is embryonic lethal** at a very early developmental stage, precluding study of postnatal disease in constitutive knockouts.
- **Liver-specific conditional knockout mice (Mtu1-LKO)** show:
  - Severe liver injury with hepatocyte cell death, **macrophage infiltration**, and **spotty necrosis**.
  - **Enlarged hepatocytes with karyomegaly and multinucleation.**
  - Notably, **no significant fibrosis**, distinguishing the acute-injury mouse model from some human biopsy findings of fibrosis/cirrhosis in severe cases.
  - This model is described as closely resembling the histologic features of human RILF (PLOS Genetics, PMID: [27689697](https://pubmed.ncbi.nlm.nih.gov/27689697/), "Mtu1-Mediated Thiouridine Formation of Mitochondrial tRNAs Is Required for Mitochondrial Translation and Is Involved in Reversible Infantile Liver Injury").
- Additional mouse/cell-based work links Mtu1 defects to **impaired osteogenic differentiation** (*Cell Death & Disease*, doi:10.1038/s41419-020-03345-5), suggesting a broader tissue impact of the pathway beyond liver, ear, and heart that may be under-recognized clinically.

### Model Recapitulation Assessment
- **Zebrafish model**: high fidelity for the auditory/hair-cell and mitochondrial bioenergetic phenotype; **does not recapitulate the hepatic phenotype** at examined stages — a translational gap (candidate for a `HUMAN_MODEL_MISMATCH`-type annotation if curated into a knowledge base).
- **Liver-conditional mouse model**: high fidelity for acute hepatocellular injury/macrophage infiltration; **partially recapitulates** human histology (misses fibrosis seen in some human cases) and, being an induced conditional knockout, does not model the transient/reversible natural history directly (the mouse model is not reported to spontaneously resolve).
- **Global mouse knockout**: fails to recapitulate any postnatal phenotype due to embryonic lethality, underscoring that a full-body, physiological TRMU-null state is likely incompatible with life in mammals — a key mechanistic insight, since human patients rarely if ever carry complete null/null genotypes (most surviving patients carry at least one hypomorphic/missense allele).

---

## Summary of Key Evidence-Grade Citations

| Claim | Source | PMID/DOI |
|---|---|---|
| Original gene discovery, Yemenite founder mutation | Zeharia et al. 2009, *Am J Hum Genet* | PMID: 19732863 |
| Largest cohort (62 individuals/56 families), genotype-phenotype, survival stats | Vogel et al. 2023 (cited in GeneReviews); Genotypic/phenotypic spectrum paper | PMID: 36305855; GeneReviews NBK591557 |
| Cysteine/NAC treatment protocol and case outcomes | Murali et al. 2021, *Mol Genet Metab* | PMID: 33485800 |
| Mechanism: proteostress/UPR activation | Cell Reports 2017 | PMID: 29320742 |
| Zebrafish model (hearing, mito biogenesis) | Zhou et al. 2018, *NAR* | PMID: 30137487 |
| Mouse liver-conditional knockout model | PLOS Genetics 2016 | PMID: 27689697 |
| CLPP-mediated proteolysis mechanism | *NAR* 2024 | doi:10.1093/nar/gkad1197 |
| Hepatic copper accumulation case | Grover et al., *JIMD Reports* | PMID: 25665837 |
| TRMU as modifier of 12S rRNA deafness | Guan et al. | PMID: 16513084 |
| OMIM phenotype/gene entries | OMIM | #613070; \*610230 |

---

## Notes on Information Gaps
- Specific gnomAD population allele-frequency and carrier-frequency figures for individual TRMU pathogenic variants were **not retrievable** from the sources searched (beyond the qualitative OMIM prevalence estimate of <1/1,000,000 and the known Yemenite Jewish founder-variant enrichment); direct gnomAD/ClinVar query would be needed to populate this precisely.
- Detailed transcriptomic/proteomic/metabolomic dataset accessions (GEO, MetaboLights, etc.) specific to TRMU-deficiency patient or model-organism samples were not identified in this search and may require a dedicated dataset-repository search (e.g., GEO query for "TRMU" or "Mtu1").
- Full OMIM Clinical Synopsis (categorized organ-system checklist) and the complete Genetics in Medicine full-text (both paywalled/403 in this session) could supplement further granular phenotype-frequency and variant-table detail if full-text access is available in a curation environment (e.g., via institutional subscription or PubMed Central when eligible).

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 45 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 33 |
| Terms named correctly | 25 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009723` (1 mention) - the report calls it "MONDO"; MONDO calls it **Leigh syndrome**
- `CL:0000187` (1 mention) - the report calls it "muscle cell — for the myopathic phenotype"; CL calls it **muscle cell**
- `UBERON:0002107` (1 mention) - the report calls it "Liver", "Primary organ**: **Liver"; UBERON calls it **liver**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001928` (1 mention) - the report calls it "Abnormal coagulation"; HP calls it **Abnormality of coagulation**
- `GO:0034341` (1 mention) - the report calls it "response to type II interferon — not core"; GO calls it **response to type II interferon**
- `GO:0006986` (1 mention) - the report calls it "response to unfolded protein / UPR-related terms"; GO calls it **response to unfolded protein**
- `CL:0000235` (2 mentions) - the report calls it "macrophage", "Kupffer cells/macrophages"; CL calls it **macrophage**
- `HP:0002151` (1 mention) - the report calls it "Metabolic panel**: elevated serum/plasma lactate"; HP calls it **Increased circulating lactate concentration**, and lists "Increased serum lactate" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005759` - called "mitochondrial matrix", "Mitochondrial matrix"
- `GO:0005743` - called "mitochondrial inner membrane", "Mitochondrial inner membrane"
- `CL:0000182` - called "hepatocyte", "Hepatocytes"
- `CL:0000235` - called "macrophage", "Kupffer cells/macrophages"
- `UBERON:0002107` - called "Liver", "Primary organ**: **Liver"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
