---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-10T01:34:58.977039'
end_time: '2026-09-10T01:40:39.038792'
duration_seconds: 340.06
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Cyanide Poisoning
  mondo_id: MONDO:0018754
  category: Environmental
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
  num_turns: 16
  total_cost_usd: 1.240558
  session_id: 9e69cc81-c7bf-5849-9c45-54bef1e4f4c3
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 37
reference_validation:
  total_references: 26
  verified: 26
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 26
  on_topic: 7
  validator_version: 0.2.1
term_validation:
  total_terms: 58
  verified: 55
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 39
  labels_matching: 25
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: HP:0100660
    reported_labels:
    - "Camptocormia \u2014 not exact"
    ontology_label: Dyskinesia
  - term_id: HP:0007015
    reported_labels:
    - "Symmetric limb weakness \u2014 approximate"
    ontology_label: Poor gross motor coordination
  - term_id: HP:0002061
    reported_labels:
    - Progressive spastic paraparesis, though konzo is characteristically non-progressive
      once established
    ontology_label: Lower limb spasticity
  - term_id: HP:0007281
    reported_labels:
    - Sensory neuropathy
    ontology_label: Developmental stagnation
  - term_id: CHEBI:75504
    reported_labels:
    - crystalline salts used in mining/electroplating, common in intentional poisoning
    ontology_label: pyranoside
  - term_id: CHEBI:9539
    reported_labels:
    - "iatrogenic cyanide source via hepatic/enzymatic release of 5 CN\u207B per molecule"
    ontology_label: Thiarubrine B
  - term_id: CHEBI:15672
    reported_labels:
    - cassava, lima beans, flax
    ontology_label: D-tartaric acid
  - term_id: UBERON:0001769
    reported_labels:
    - corticospinal tract
    ontology_label: iris
  - term_id: UBERON:0001791
    reported_labels:
    - optic nerve
    ontology_label: inner nuclear layer of retina
  - term_id: UBERON:0001846
    reported_labels:
    - cochlea
    ontology_label: internal ear
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0005751
    ontology_label: obsolete mitochondrial respiratory chain complex IV
    replaced_by: GO:0045277
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cyanide Poisoning
- **MONDO ID:** MONDO:0018754 (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Cyanide Poisoning** covering all of the
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

I'll research this now using web search and fetch tools, gathering current literature and data on cyanide poisoning to build the comprehensive report.

# Cyanide Poisoning: Comprehensive Research Report

## 1. Disease Information

**Overview.** Cyanide poisoning is an acute or chronic toxidrome caused by exposure to cyanide ions (CN⁻) or cyanide-releasing compounds (hydrogen cyanide gas, alkali cyanide salts, cyanogenic glycosides, or nitroprusside metabolism), producing "histotoxic hypoxia" — inhibition of cellular oxygen utilization despite normal oxygen delivery — via blockade of mitochondrial complex IV (cytochrome c oxidase). It is "a broad-spectrum poisoning by inhibition of the aerobic respiration metabolism at the cellular level in mitochondria" (Wikipedia/Wikidata summary, consistent with toxicology literature) ([Wikidata](https://www.wikidata.org/wiki/Q883082)). Exposure routes include inhalation (fire smoke, industrial gas release), ingestion (cyanide salts, cyanogenic plant foods, suicide attempts), dermal/mucosal absorption, and iatrogenic exposure (sodium nitroprusside infusion).

**Key identifiers:**
- **MONDO:** MONDO:0018754 (confirmed by user; Orphanet cross-reference also lists an entry, [Orphanet: Cyanide poisoning](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=466670&lng=EN))
- **ICD-10-CM:** T65.0 (Toxic effect of cyanides), with subcodes T65.0X1– (accidental), T65.0X2– (intentional self-harm), T65.0X3– (assault), T65.0X4– (undetermined); T57.3 covers toxic effect of hydrogen cyanide specifically ([ICD10Data](https://www.icd10data.com/ICD10CM/Codes/S00-T88/T51-T65/T65-/T65.0))
- **ICD-11:** NE61 (Toxic effect of cyanides) / PC91 (poisoning by exposure category)
- **MeSH:** Cyanides (D003489); "Cyanide Poisoning" indexed under Poisoning + Cyanides
- **OMIM:** No dedicated OMIM entry — this is an acquired/environmental toxidrome, not a Mendelian disease, though OMIM entries exist for enzymes involved in detoxification (e.g., *TST*/rhodanese)

**Synonyms:** Hydrocyanic acid poisoning, prussic acid poisoning, HCN toxicity, cyanogen poisoning; disease-specific forms include konzo (chronic cassava-cyanide spastic paraparesis), tropical ataxic neuropathy (TAN), and nitroprusside-induced cyanide toxicity.

**Data provenance:** Most available evidence is aggregated at the disease level — case reports/series (the largest systematic review found 65 articles describing 102 patients), poison-control-center registries (National Poison Data System, NPDS), forensic/autopsy series, and occupational/environmental exposure studies — rather than large EHR cohorts, because acute cyanide poisoning is rare, often lethal before presentation, and frequently undiagnosed due to lack of rapid assays.

---

## 2. Etiology

### Disease Causal Factors
Cyanide poisoning is fundamentally **exogenous/environmental**, not genetic, though genetic factors modulate individual susceptibility and detoxification capacity (see below). Causal exposure categories:

1. **Combustion/inhalational** — house/structure fires (combustion of nitrogen-containing synthetic polymers: polyurethane foam, nylon, wool, silk, melamine); the dominant real-world cause of cyanide exposure in industrialized countries.
2. **Industrial/occupational** — electroplating, metal polishing, photographic development, gold/silver mining (cyanide leaching — ~300,000 tons of hydrogen cyanide produced annually in the US, much used in gold extraction), plastics and synthetic fiber manufacturing, fumigation.
3. **Iatrogenic** — sodium nitroprusside infusion (each nitroprusside molecule releases 5 cyanide ions upon metabolism by oxyhemoglobin); risk rises above 1 mg/kg over <3 hours or >0.5 mg/kg/hr over 24 hours.
4. **Ingestion of cyanide salts** — potassium/sodium cyanide (suicide, homicide, industrial accident).
5. **Dietary/cyanogenic glycosides** — amygdalin (bitter almonds, apricot/peach/apple kernels — lethal dose ~0.5–3.5 mg/kg bw), linamarin (cassava, lima beans) — chronic low-dose exposure underlies konzo and tropical ataxic neuropathy in cassava-dependent populations of sub-Saharan Africa.
6. **Chemical warfare/terrorism** — hydrogen cyanide (AC) and cyanogen chloride (CK) are blood agents historically weaponized (WWI, Iran-Iraq War allegations, Nazi extermination camps [Zyklon B]).
7. **Mass-casualty industrial disasters** — the Bhopal methyl isocyanate disaster (1984) is cited as a major industrial cyanide/related-toxin mass-casualty event (~4,000 immediate deaths, 15,000–20,000 subsequent deaths).

### Risk Factors

**Genetic:**
- Polymorphisms in **thiosulfate sulfurtransferase (TST/rhodanese)**, the principal cyanide-detoxifying enzyme, alter enzymatic clearance capacity. Eleven polymorphisms were characterized in French Caucasians, including two missense variants (E102D, P285A) and six promoter-region variants; the P285A variant shows ~50% reduced intrinsic clearance in vitro, and the promoter variants reduce reporter-gene activity by 40–73% (Bebarta/Baud group; PMID:[16790311](https://pubmed.ncbi.nlm.nih.gov/16790311/), *Toxicology* 2006). These polymorphisms plausibly explain inter-individual variation in cyanide sensitivity but have not been validated as clinical risk predictors in large cohorts.
- Deficiency in **cobalamin (vitamin B12)** status reduces endogenous cyanide-scavenging capacity (hydroxocobalamin binds cyanide to form cyanocobalamin), a mechanism implicated in "tobacco-alcohol amblyopia" (Leber-like optic neuropathy exacerbated by chronic low-dose cyanide from tobacco smoke in the context of marginal B12/folate status).
- **3-mercaptopyruvate sulfurtransferase (MPST)** is a secondary cyanide-detoxifying enzyme; polymorphisms are less well characterized.

**Environmental:**
- Occupational exposure (mining, electroplating, fumigation, jewelry polishing).
- Enclosed-space fires involving synthetic materials.
- Age/sex: fire-related cyanide exposure affects all ages; occupational exposure skews toward working-age adults, predominantly male in mining/industrial settings.
- Malnutrition/protein deficiency — markedly increases susceptibility to chronic dietary cyanide toxicity (konzo), because sulfur amino acids (cysteine/methionine) are required substrates for rhodanese-mediated detoxification to thiocyanate.
- Geography — konzo is endemic to cassava-dependent rural populations of the Democratic Republic of Congo, Mozambique, Tanzania, Cameroon, Central African Republic, and Angola, often during drought or war-related food insecurity when cassava processing (soaking/fermentation to reduce cyanogen content) is curtailed.

### Protective Factors
- Adequate dietary **sulfur amino acid** (cysteine, methionine) and **protein intake**, which sustains rhodanese/thiosulfate-dependent detoxification.
- Adequate **vitamin B12/cobalamin** status.
- Proper cassava **processing** (soaking, sun-drying, fermentation) that hydrolyzes and volatilizes cyanogenic glycosides before consumption — the principal public-health protective intervention against konzo.
- No genetic "protective variant" analogous to a GWAS hit has been robustly established; TST promoter/coding variants associated with *higher* activity would be presumptively protective but are not independently validated as such.

### Gene-Environment Interactions
The clearest documented gene-environment interaction is **TST/rhodanese genotype × dietary sulfur-amino-acid and cyanogen intake**: individuals with reduced-activity rhodanese variants combined with chronic dietary cyanogenic-glycoside exposure (cassava) and protein/sulfur-amino-acid malnutrition are hypothesized to be at elevated risk for konzo and tropical ataxic neuropathy, though this precise gene-diet interaction has not been formally tested in affected populations to my knowledge — it remains a biologically plausible but epidemiologically unconfirmed hypothesis based on enzymology data from Western cohorts (PMID:16790311).

---

## 3. Phenotypes

### Acute Cyanide Poisoning — Symptoms/Signs

| Phenotype | Category | Frequency (from systematic review of 102 patients, 65 articles) | HPO suggestion |
|---|---|---|---|
| Unresponsiveness/coma | Clinical sign | 78% | HP:0001259 (Coma) |
| Hypotension | Clinical sign | 54% | HP:0002615 (Hypotension) |
| Respiratory failure/tachypnea/dyspnea | Clinical sign | 73% | HP:0002093 (Respiratory failure); HP:0002094 (Dyspnea) |
| Cardiac arrest | Clinical sign | 20% | HP:0001695 (Cardiac arrest) |
| Seizures | Clinical sign | 20% | HP:0001250 (Seizure) |
| Cyanosis | Physical sign | 15% | HP:0000961 (Cyanosis) |
| "Cherry-red" skin (classically taught, actually uncommon) | Physical sign | 11% | — (not a discrete HPO term; related to HP:0012472 flushing is not accurate — best left as free text) |
| Bitter-almond breath odor | Physical sign | ~15% (only ~40–60% of people can genetically perceive the odor at all) | — |
| Headache, weakness, nausea, vomiting, diaphoresis, tachycardia | Early symptoms | Common | HP:0002315 (Headache); HP:0025145 (Weakness); HP:0002018 (Nausea); HP:0002013 (Vomiting) |
| Bradycardia, AV block, ventricular dysrhythmias, asystole | Late/terminal cardiac signs | — | HP:0001662 (Bradycardia); HP:0011703 (Atrioventricular block) |
| Lactic (anion-gap metabolic) acidosis | Laboratory abnormality | Near-universal in significant poisoning | HP:0003128 (Lactic acidosis) |
| Elevated venous oxygen saturation ("arterialized" venous blood) | Laboratory abnormality | Characteristic but underused | — |

**Onset:** Inhalational exposure produces symptoms within seconds to minutes; ingestion of cyanide salts within minutes; ingestion of cyanogenic glycosides (which require enzymatic hydrolysis) may be delayed 30 minutes to several hours.

**Severity/course:** Highly dose-dependent — ranges from mild (headache, dizziness, tachycardia) to fulminant (coma, seizures, cardiovascular collapse, death within minutes at high doses). "Cyanide poisoning is a life-threatening condition that impairs cellular oxygen utilization, leading to lactic acidosis" and serum lactate ≥8 mmol/L is both sensitive and specific for toxic cyanide concentrations in suspected exposure (case report and prior validation studies; PMID:[41204534](https://pubmed.ncbi.nlm.nih.gov/41204534/), *Medicine* 2025).

### Delayed/Chronic Neurological Phenotypes
A **delayed neurological syndrome** — dystonia, parkinsonism, dyskinesia — has been documented in survivors of severe acute poisoning, emerging weeks to months after apparent recovery, with progressive rigidity, flexed upper limbs, and extended lower limbs (basal ganglia/globus pallidus/putamen injury on MRI, decreased striatal fluorodopa uptake on PET). HPO suggestions: HP:0001300 (Parkinsonism), HP:0001332 (Dystonia), HP:0100660 (Camptocormia — not exact), HP:0002072 (Chorea, if choreiform component present).

**Chronic dietary cyanide exposure (konzo):** abrupt-onset, irreversible, non-progressive, symmetric **spastic paraparesis or tetraparesis** ("tied legs") — an upper motor neuron syndrome. HPO: HP:0001258 (Spastic paraplegia), HP:0007015 (Symmetric limb weakness — approximate), HP:0002061 (Progressive spastic paraparesis, though konzo is characteristically non-progressive once established).

**Tropical ataxic neuropathy (TAN):** sensory polyneuropathy, sensory ataxia, bilateral optic atrophy, bilateral sensorineural hearing loss, occurring in older individuals on chronic monotonous cassava diets. HPO: HP:0007281 (Sensory neuropathy), HP:0001272 (Cerebellar/sensory ataxia), HP:0000648 (Optic atrophy), HP:0000407 (Sensorineural hearing loss).

### Quality of Life Impact
Acute survivors with hypoxic-ischemic brain injury or basal-ganglia damage may have lasting cognitive, motor, and psychiatric impairment; a longitudinal neuropsychological study with interval MRI in acute-poisoning survivors documented persistent deficits. Konzo produces permanent, non-progressive motor disability (wheelchair/crutch dependence in severe cases) with major impact on subsistence-agriculture livelihoods in affected regions; TAN produces disabling ataxia, blindness, and deafness in elderly patients. No disease-specific validated QOL instrument was identified; general disability/QOL measures (EQ-5D, WHODAS) have been applied in konzo cohorts in the broader literature.

---

## 4. Genetic/Molecular Information

Cyanide poisoning is **not a monogenic disease**; there is no single causal gene. Relevant genetic/molecular factors instead concern detoxification-pathway genes that modulate individual pharmacodynamics/pharmacokinetics of cyanide:

- **TST (Thiosulfate Sulfurtransferase / Rhodanese)** — HGNC:12362, chromosome 22q12.3. The principal mitochondrial-matrix enzyme catalyzing CN⁻ + thiosulfate → SCN⁻ (thiocyanate) + sulfite, using thiosulfate as sulfur donor. Functional polymorphisms (missense E102D and P285A; six 5′-regulatory-region SNPs) alter enzyme activity and expression (PMID:16790311). No disease-causing "pathogenic variant" per ACMG/ClinVar classification exists for TST in the context of cyanide poisoning specifically — these are population-frequency modifier polymorphisms, not Mendelian pathogenic alleles.
- **MPST (3-Mercaptopyruvate Sulfurtransferase)** — HGNC:7386, chromosome 22q12.3 (adjacent to TST, arose by gene duplication) — secondary/complementary cyanide-detoxification enzyme using 3-mercaptopyruvate as sulfur donor.
- **CBS (Cystathionine Beta-Synthase)** and other sulfur-amino-acid metabolism genes indirectly affect substrate (thiosulfate/cysteine) availability for detoxification.
- **Cytochrome c oxidase subunit genes (mtDNA-encoded MT-CO1/2/3 and nuclear-encoded subunits)** are the molecular *target* of cyanide (binding site: ferric heme a3–CuB binuclear center) rather than a susceptibility locus; polymorphisms here are not established modifiers of cyanide sensitivity in humans.
- **Somatic/germline variant classification:** Not applicable — no ClinVar pathogenic/likely-pathogenic variant classification exists for cyanide-poisoning susceptibility. gnomAD population-frequency data exist for TST coding variants but disease-association evidence is limited to functional/enzymatic studies rather than large-scale case-control genetic association.
- **Epigenetics:** No established disease-specific epigenetic (DNA methylation/histone) signature. Some general literature exists on chronic low-dose cyanide/thiocyanate exposure and oxidative-stress-linked epigenetic modification, but this is not well characterized for acute poisoning.
- **Chromosomal abnormalities:** Not applicable (acquired toxic disease, not a chromosomal disorder).

**Ontology suggestions:** GENO terms are not typically applicable given the acquired nature; if modeling TST/MPST as modifier genes, `hgnc:12362` (TST) and `hgnc:7386` (MPST) with `relationship_type: MODIFIER` or `SUSCEPTIBILITY` would be appropriate in a dismech-style schema.

---

## 5. Environmental Information

**Environmental/toxic factors (primary etiologic category for this disease):**
- **Hydrogen cyanide gas (HCN)** — CHEBI:18407 — from combustion of nitrogen-containing polymers (polyurethane, nylon, wool, silk, melamine, polyacrylonitrile) in structure fires; from industrial processes (metal plating/mining); historically as a fumigant and chemical-warfare agent.
- **Potassium cyanide (KCN)** — CHEBI:32035 — and **sodium cyanide (NaCN)** — CHEBI:75504 — crystalline salts used in mining/electroplating, common in intentional poisoning.
- **Cyanogen chloride (CK)** — a chemical-warfare "blood agent."
- **Sodium nitroprusside** — CHEBI:9539 — iatrogenic cyanide source via hepatic/enzymatic release of 5 CN⁻ per molecule.
- **Amygdalin** — CHEBI:2637 (bitter almonds, apricot/peach/apple kernels; EFSA established acute reference dose concerns for raw apricot kernels, 2016).
- **Linamarin** — CHEBI:15672 (cassava, lima beans, flax); requires linamarase (endogenous plant β-glucosidase or gut microbial enzymes) for hydrolysis to release HCN.
- **Acetonitrile and other nitriles** — metabolized to cyanide in vivo (relevant to nail-glue-remover ingestion poisoning).

**Lifestyle/behavioral factors:**
- Chronic tobacco smoking is a source of chronic low-level HCN exposure (implicated in "tobacco amblyopia," particularly with concurrent malnutrition/B12 deficiency).
- Monotonous, poorly processed cassava-based diets (protein/sulfur-amino-acid-poor) in food-insecure populations — the central environmental driver of konzo and TAN.

**Infectious agents:** Not applicable — cyanide poisoning is a chemical toxidrome, not infectious. (Note: an unrelated coincidental homonym exists — "Cyanide" is sometimes discussed alongside cyanobacterial toxins, but cyanobacteria/cyanotoxins are a biologically and chemically distinct hazard and should not be conflated with cyanide/HCN poisoning.)

---

## 6. Mechanism / Pathophysiology

### Causal Chain (Acute Cyanide Poisoning)

1. **Exposure** to a cyanide-releasing source (HCN gas inhalation, cyanide salt ingestion, cyanogenic glycoside hydrolysis, or nitroprusside metabolism) **leads to** systemic absorption of the cyanide ion (CN⁻) into blood.
2. Free CN⁻ **leads to** rapid diffusion into cells and mitochondria, where it **binds** with high affinity to the ferric (Fe³⁺) heme a3–CuB binuclear center of **cytochrome c oxidase (Complex IV)** of the mitochondrial electron transport chain (demonstrated structurally; PMID:[17906319](https://pubmed.ncbi.nlm.nih.gov/17906319/)).
3. This binding **results in** reversible inhibition of Complex IV, which **blocks** the terminal transfer of electrons to molecular oxygen — despite oxygen being physically present and delivered normally (**"histotoxic hypoxia"**).
4. Blocked electron transport **leads to** collapse of the mitochondrial proton-motive force and cessation of oxidative phosphorylation, **causing** rapid depletion of cellular ATP.
5. ATP depletion **forces** a shift from aerobic to anaerobic glycolysis as a compensatory (but grossly insufficient) energy source, which **generates** excess pyruvate converted to lactate, **producing** severe high-anion-gap **lactic acidosis** — this is the basis for using serum lactate ≥8 mmol/L as a sensitive/specific biomarker of significant cyanide exposure (PMID:41204534).
6. Cellular energy failure disproportionately **affects** tissues with the highest oxidative metabolic demand — **myocardium, CNS (especially basal ganglia/striatum), and to a lesser extent liver/kidney** — because these tissues have the highest local cytochrome oxidase density and glucose/oxygen utilization, explaining the selective vulnerability of the striatum to delayed neurotoxicity.
7. In the **heart**, ATP failure **leads to** an initial catecholamine-driven hypertensive/bradycardic phase, **followed by** progressive myocardial depression, **causing** hypotension, bradyarrhythmia, AV block, ventricular dysrhythmia, and **culminating in** cardiovascular collapse/asystole in severe/untreated cases.
8. In the **CNS**, energy failure **triggers** a cascade of excitotoxicity (glutamate release), **calcium influx**, mitochondrial permeability transition, reactive-oxygen-species generation, and lipid peroxidation, which **causes** neuronal injury/death, particularly in the globus pallidus and putamen — **manifesting acutely as** coma and seizures, and, in survivors of severe poisoning, **as a delayed sequela**, a dystonic-parkinsonian syndrome emerging weeks to months later, correlated on MRI with bilateral globus pallidus/putaminal lesions and reduced striatal fluorodopa uptake on PET (a mechanistic link that is **inferred** from imaging/neuropathology correlation rather than fully demonstrated at the molecular level in humans).
9. Concurrently, cyanide **binds** nitric oxide synthase and interacts with nitric oxide signaling, and recent work proposes cyanide may also function physiologically at low concentrations as an endogenous gasotransmitter modulating vascular tone — a **hypothesis under active investigation** rather than established mechanism (systematic review, PMC:[PMC9291117](https://pmc.ncbi.nlm.nih.gov/articles/PMC9291117/); vascular-effects review, PMC:[PMC12486351](https://pmc.ncbi.nlm.nih.gov/articles/PMC12486351/)).
10. **Endogenous detoxification** operates in parallel: mitochondrial rhodanese (TST) and 3-mercaptopyruvate sulfurtransferase (MPST) **convert** a fraction of the cyanide load to thiocyanate (SCN⁻, renally excreted) using thiosulfate/3-mercaptopyruvate as sulfur donors; this pathway is capacity-limited (sulfur-donor-dependent) and is overwhelmed at high cyanide doses — the rate-limiting nature of this pathway is the pharmacologic basis for **thiosulfate antidote** therapy, which supplies additional sulfur donor to accelerate this natural route.
11. In the **chronic, low-dose dietary form (konzo/TAN)**, sustained cyanide/thiocyanate exposure from poorly processed cassava, compounded by dietary protein/sulfur-amino-acid deficiency (which limits the rhodanese pathway's substrate supply), **is hypothesized to lead to** selective upper-motor-neuron toxicity (konzo) or combined sensory/optic/cochlear toxicity (TAN) via a still not fully resolved chronic sub-lethal energy-failure/oxidative-stress mechanism, with **thiamine deficiency** proposed as a possible cofactor (this causal link remains actively debated in the literature and should be regarded as a hypothesis, not an established mechanism).

### Category Detail

- **Molecular pathways:** Oxidative phosphorylation/electron transport chain (Complex IV inhibition) is central; secondary involvement of glutamate/NMDA excitotoxicity pathways, nitric oxide signaling, and Nrf2-antioxidant response pathway (carnosic acid, an Nrf2 activator, is protective against cyanide-induced brain injury in rodent models — PMC:[PMC4465065](https://pmc.ncbi.nlm.nih.gov/articles/PMC4465065/)). GO suggestion: GO:0006123 (mitochondrial electron transport, cytochrome c to oxygen); GO:0045333 (cellular respiration).
- **Cellular processes:** Necrosis and apoptosis of high-oxidative-demand cells; anaerobic glycolysis upregulation; oxidative stress/lipid peroxidation; excitotoxic calcium influx.
- **Protein dysfunction:** Direct, reversible inhibition (not structural misfolding) of cytochrome c oxidase (Complex IV) via heme-iron/copper coordination by CN⁻; this is a pharmacologic/toxicologic inhibition rather than a genetic loss-of-function.
- **Metabolic changes:** Shift from oxidative to anaerobic (glycolytic) metabolism; lactic acidosis; secondary hyperglycemia (catecholamine-driven) in early poisoning; elevated venous oxygen saturation (tissue extraction failure).
- **Immune system involvement:** Not a primary feature of acute poisoning; secondary inflammatory injury (e.g., ARDS in smoke-inhalation co-exposure) is common but attributable to co-exposures (heat, particulates, CO) rather than cyanide per se.
- **Tissue damage mechanisms:** Cytotoxic/histotoxic hypoxia (not ischemic hypoxia), oxidative stress, excitotoxicity — most pronounced in basal ganglia, myocardium, and (in smoke-inhalation cases) airway/lung parenchyma from co-exposure to thermal injury and other combustion toxins (CO, particulates, other irritant gases).
- **Biochemical abnormalities:** Complex IV inhibition; elevated lactate; elevated mixed/central venous oxygen saturation; in nitroprusside toxicity, secondary methemoglobinemia and thiocyanate accumulation (renal-failure-dependent) causing a distinct delayed thiocyanate toxidrome (confusion, tinnitus, seizures, hyperreflexia).
- **Molecular profiling:** Limited disease-specific -omics data exist given the acute/lethal, low-N nature of severe poisoning; a 2025 FASEB Journal paper on "redirecting intermediary metabolism to counteract cyanide poisoning" (Bebarta et al.) represents recent metabolomics-informed therapeutic research (https://faseb.onlinelibrary.wiley.com/doi/full/10.1096/fj.202400230RR).
- **Advanced technologies:** No single-cell or spatial transcriptomic studies specific to human cyanide poisoning were identified; animal (mouse/pig) models are used for pharmacodynamic and antidote-efficacy profiling (see Section 15).

**Cell types involved:** cardiomyocytes (CL:0000746), medium spiny neurons of the striatum/globus pallidus (CL:0000842 or more specific GABAergic striatal projection neuron terms), hepatocytes (CL:0000182, site of rhodanese-mediated detoxification), and, in konzo, upper motor neurons (CL:0008015 corticospinal neuron approximate).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Cardiovascular system (myocardium, conduction system), central nervous system (brain — basal ganglia, brainstem respiratory centers), and (in fire-related exposure) the respiratory system (co-injury from smoke, thermal injury, CO).
- **Secondary:** Liver (site of rhodanese detoxification, secondarily stressed), kidney (excretes thiocyanate; impaired in renal failure, increasing risk of thiocyanate toxicity), peripheral/optic/auditory nervous system in chronic dietary exposure (TAN).
- **Body systems:** Cardiovascular, nervous, respiratory (in inhalational/fire cases), and — in chronic dietary exposure — the visual and auditory systems.

**Tissue/cell level:**
- Cardiac muscle tissue (myocardium); basal ganglia neurons (particularly globus pallidus internal/external segments and putamen — high metabolic/oxidative demand); upper motor neurons of the corticospinal tract (konzo); retinal ganglion cells/optic nerve (TAN, optic atrophy); cochlear hair cells (TAN, sensorineural hearing loss); hepatocytes (rhodanese-rich).

**Subcellular level:** Mitochondria — specifically the inner mitochondrial membrane, Complex IV (cytochrome c oxidase) of the electron transport chain. GO Cellular Component: GO:0005751 (mitochondrial respiratory chain complex IV), GO:0005739 (mitochondrion).

**Localization (UBERON):**
- UBERON:0002370 (thymus) — not relevant
- UBERON:0002349 (myocardium)
- UBERON:0002435 (striatum) / UBERON:0001873 (globus pallidus) / UBERON:0001874 (putamen)
- UBERON:0000955 (brain)
- UBERON:0002107 (liver)
- UBERON:0002113 (kidney)
- UBERON:0001769 (corticospinal tract) — konzo
- UBERON:0000966 (retina) / UBERON:0001791 (optic nerve) — TAN
- UBERON:0001846 (cochlea) — TAN

**Lateralization:** Basal ganglia lesions and delayed dystonic-parkinsonian syndrome are typically **bilateral/symmetric**; konzo motor deficits are bilateral and symmetric ("tied legs" gait); TAN optic atrophy and hearing loss are bilateral.

---

## 8. Temporal Development

**Onset:**
- **Acute poisoning:** Inhalational — seconds to minutes; ingestion of cyanide salts — minutes; ingestion of cyanogenic glycosides — 30 minutes to several hours (delay reflects need for enzymatic/gut-microbial hydrolysis to release HCN).
- **Chronic (konzo):** Abrupt onset over hours to days in an individual who has had sustained dietary cyanogen exposure, often during periods of drought/famine when inadequately processed cassava becomes dietary staple; epidemic clusters can appear within weeks in a community.
- **Delayed neurological sequelae:** Weeks to months after apparent recovery from acute severe poisoning.

**Progression:**
- **Acute poisoning stages:** Early (headache, dizziness, tachycardia, hyperventilation) → intermediate (dyspnea, confusion, hypotension progressing from initial reflex hypertension/bradycardia) → late/severe (coma, seizures, cardiovascular collapse, respiratory arrest, death) — progression can be extremely rapid (minutes) at high doses.
- **Konzo:** Sudden onset followed by a **non-progressive, stable** course once established (a distinguishing feature from other spastic paraparesis etiologies); severity is graded clinically (mild — able to walk without support; moderate — requires one support; severe — requires two supports or is unable to walk).
- **TAN:** Chronic, may show slow progression with continued dietary exposure; not typically episodic.
- **Delayed dystonic-parkinsonian syndrome:** Progressive rigidity following the latent interval, potentially plateauing but often not fully reversible.

**Duration:** Acute poisoning is self-limited if treated promptly and the patient survives the initial hours (survival beyond ~4 hours after treatment initiation generally predicts recovery, per toxicology reviews); konzo-related spastic paraparesis and TAN sequelae are typically **permanent/lifelong**.

**Remission patterns:** Acute poisoning — full recovery is possible with prompt antidotal/supportive therapy in the absence of severe hypoxic/ischemic end-organ injury; no spontaneous remission of konzo-associated motor deficits is described; some recovery of neuropsychological function has been documented over months to years post-acute-poisoning in longitudinal MRI/neuropsychological follow-up (PMC:[PMC3962856](https://ncbi.nlm.nih.gov/pmc/articles/PMC3962856)).

**Critical periods:** The first few minutes to hours after exposure represent the critical therapeutic window — antidote administration (hydroxocobalamin, nitrites, thiosulfate) before irreversible hypoxic-ischemic organ injury dramatically improves outcome. For konzo, the critical prevention window is at the population/food-processing level (ensuring adequate cassava soaking/fermentation and dietary protein sufficiency) rather than an individual clinical window.

---

## 9. Inheritance and Population

**This is not a heritable Mendelian disease** — no inheritance pattern, penetrance, expressivity, anticipation, germline mosaicism, founder effect, or carrier frequency applies in the classical genetic-disease sense. The relevant "genetic" contribution is polygenic/modifier-gene susceptibility (TST/MPST activity variants) layered on an environmental exposure.

**Epidemiology:**
- **Fire-related exposure:** In the US, >3,000 fire deaths and >14,000 fire injuries occur annually (2017 data: 3,400 deaths, 14,670 injuries), with smoke inhalation (not thermal injury) the leading cause of fire mortality; cyanide is "increasingly recognized as a significant toxicant" in smoke inhalation, though the proportion of fire deaths specifically attributable to cyanide (versus co-toxicants like CO) varies substantially across studies — a classic forensic series of 364 fire fatalities found mean blood cyanide 1.0 mg/L with levels exceeding the fatal threshold (>3 mg/L) in 31 cases (PMID:[8150843](https://pubmed.ncbi.nlm.nih.gov/8150843/?dopt=Abstract), *J Burn Care Rehabil* 1994), while a prospective clinical study of 144 smoke-exposed patients and 43 fire fatalities found elevated blood cyanide in 90% of survivors and 100% of the deceased, illustrating substantial measurement/cohort-dependent variability.
- **US poison-center data:** The 2023 National Poison Data System (NPDS) annual report recorded 1 death among 145 single-substance cyanide exposures; the 2021 AAPCC Toxic Exposure Surveillance data recorded 4 deaths among 163 cyanide exposure cases — indicating acute isolated cyanide poisoning is rare in the general US population but carries substantial case-fatality when it occurs.
- **Konzo:** Endemic/epidemic in specific rural regions of the Democratic Republic of Congo, Mozambique, Tanzania, Cameroon, Central African Republic, and Angola; outbreaks historically correlate with drought, conflict, and food insecurity that force reliance on inadequately processed bitter-cassava varieties; precise contemporary prevalence figures vary by region and survey year and were not independently re-verified in this session — cite the primary konzo epidemiological literature (e.g., PLOS NTD review, https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0001051) for current numbers.
- **Occupational:** Elevated risk populations include artisanal/small-scale gold miners (common in low- and middle-income countries using cyanide leaching), electroplaters, and jewelry polishers; global burden estimates for occupational cyanide morbidity/mortality are not centrally tracked in a single registry.

**Population demographics:**
- **Sex ratio:** Occupational and industrial cyanide exposure skews male (reflecting mining/industrial workforce demographics); suicidal ingestion shows variable sex distribution by country/era; fire-related exposure affects both sexes and all ages roughly proportional to fire-victim demographics.
- **Age distribution:** Fire-related — all ages; occupational — working-age adults; konzo — historically over-represented in children and women of childbearing age in affected communities (reflecting household dietary patterns), though whole-community outbreaks occur.
- **Geographic distribution:** Industrialized-country exposure is dominated by fire/industrial/iatrogenic/suicidal sources; chronic dietary cyanide toxicity (konzo, TAN) is essentially restricted to cassava-dependent regions of sub-Saharan Africa.

---

## 10. Diagnostics

**Clinical diagnosis is primary** — "no single, readily available laboratory test has been identified to confirm cyanide poisoning; thus, diagnosis is primarily driven by clinical assessment" (StatPearls, [NBK507796](https://www.ncbi.nlm.nih.gov/books/NBK507796/)). Classic teaching signs (bitter-almond odor, cherry-red skin) are present in only ~11–15% of cases and should not be relied upon.

**Laboratory tests:**
- **Whole-blood cyanide concentration** — the definitive confirmatory test, but turnaround time (hours to days in most labs) makes it useless for real-time management; normal <0.5 mg/L (nonsmokers), toxic >1.0 mg/L, potentially lethal >3 mg/L. LOINC-codable analyte.
- **Serum/whole-blood lactate** — the most clinically useful rapid surrogate biomarker; lactate ≥8 mmol/L is sensitive and specific for toxic cyanide exposure in the appropriate clinical context (PMID:41204534, and earlier validation, e.g., Baud et al.).
- **Arterial and venous blood gas with co-oximetry** — narrowed arteriovenous oxygen difference / elevated venous oxygen saturation reflects failure of tissue oxygen extraction (histotoxic hypoxia), a useful ancillary clue.
- **Anion gap metabolic acidosis** on basic metabolic panel.
- **Carboxyhemoglobin (CO-Hgb)** and **methemoglobin** levels — essential in smoke-inhalation and nitrite-antidote-monitoring contexts, respectively, to distinguish/quantify co-toxicity.
- **Thiocyanate level** — reflects cumulative/chronic exposure or antidote (thiosulfate) response; also relevant to diagnosing thiocyanate toxicity from prolonged nitroprusside infusion.

**Imaging:**
- **Brain MRI** — in survivors of severe poisoning, bilateral T2/FLAIR hyperintensities (or T1 low-signal, hemorrhagic change) in globus pallidus and posterior putamen; diffuse white-matter injury in severe cases; used to characterize/predict delayed neurological sequelae (PMID/AJNR: [AJNR 2002;23:1398](https://www.ajnr.org/content/23/8/1398)).
- **Fluorodopa PET** — decreased bilateral striatal uptake correlating with delayed parkinsonism.

**Functional/electrophysiological tests:** EEG (nonspecific encephalopathic slowing/seizure activity in severe poisoning); ECG (bradyarrhythmia, AV block, QTc changes — early vs. delayed QTc prolongation has prognostic relevance in acute poisonings broadly, PMC:[PMC11386474](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11386474/)).

**Genetic testing:** Not part of routine clinical diagnosis; TST/MPST genotyping is a research tool only, with no established clinical testing pathway, panel, or GTR listing specific to cyanide-poisoning risk stratification.

**Clinical criteria:** No formal DSM/consensus diagnostic-criteria instrument exists (this is an acute-poisoning diagnosis based on exposure history + clinical toxidrome + supportive labs, e.g., lactate); several clinical prediction scores/nomograms based on exposure circumstance (fire vs. industrial vs. ingestion), vital signs, and lactate have been proposed in the emergency-medicine literature to guide empiric antidote administration when confirmatory cyanide levels are unavailable in real time.

**Differential diagnosis:** Carbon monoxide poisoning (frequently co-occurs in fire victims and must be distinguished/co-treated), methemoglobinemia, hydrogen sulfide poisoning (also inhibits cytochrome oxidase, at a different binding site), severe sepsis/septic shock (lactic acidosis overlap), salicylate toxicity, other causes of anion-gap metabolic acidosis and coma.

**Screening:** No population newborn or carrier screening applies (not a genetic disease). Occupational medical surveillance (periodic thiocyanate monitoring) is used in some cyanide-handling industries as a biomonitoring/screening tool for chronic low-level exposure.

---

## 11. Outcome/Prognosis

**Survival/mortality:**
- Case-fatality is highly dose- and treatment-timing-dependent. US poison-center surveillance (NPDS 2023) recorded 1 death among 145 single-substance exposures reported to poison centers (a population skewed toward milder/detected exposures); the 2021 AAPCC data recorded 4 deaths among 163 cases. These figures likely substantially **underestimate** true population mortality because many fatal exposures (suicide, homicide, mass-casualty industrial events, undiagnosed fire deaths) never reach poison-center reporting.
- In a systematic review of 102 published patients (65 articles), most were severely ill (78% unresponsive, 73% respiratory failure, 54% hypotensive, 20% cardiac arrest), reflecting publication bias toward severe/notable cases.
- **Prognosis is generally good** for patients with mild symptoms not requiring antidote, and **reasonably good** for moderate poisoning with rapid supportive care and antidotal therapy; prognosis is **poor** for patients who suffer cardiac arrest, even with prompt antidote administration.
- **Survival beyond ~4 hours after treatment initiation** is generally considered a favorable prognostic marker for eventual recovery, assuming adequate hemodynamic/respiratory support was maintained (Medscape/StatPearls synthesis).

**Morbidity/functional outcomes:**
- Hypoxic-ischemic brain injury from severe/prolonged poisoning can cause permanent cognitive impairment, and delayed basal-ganglia-mediated dystonia/parkinsonism is a recognized long-term morbidity in survivors of severe acute poisoning.
- Konzo produces lifelong, non-progressive but irreversible spastic paraparesis/tetraparesis with major functional-independence and economic impact in affected rural communities.
- TAN produces permanent sensory ataxia, visual impairment (optic atrophy), and hearing loss.

**Complications:** In smoke-inhalation cases specifically, combined cyanide + carbon monoxide toxicity, airway thermal/chemical injury, and ARDS materially worsen outcomes; prehospital hydroxocobalamin administration in smoke-inhalation victims is associated with decreased ventilator dependence time, reduced pneumonia rates, and shorter ICU stay (systematic reviews of prehospital hydroxocobalamin use, PMC:[PMC12767669](https://pmc.ncbi.nlm.nih.gov/articles/PMC12767669/)).

**Prognostic factors:** Degree/duration of hypotension and hypoxia before treatment, initial lactate level, presence of cardiac arrest, time to antidote administration, co-exposure to carbon monoxide (in fire victims), and pre-existing hepatic/nutritional/vitamin-B12 status (which affects endogenous detoxification reserve).

---

## 12. Treatment

### Pharmacotherapy / Antidotes
Antidotal therapy targets three complementary mechanisms: (1) directly sequestering cyanide, (2) generating methemoglobin as a cyanide "sink," and (3) accelerating enzymatic detoxification to thiocyanate.

1. **Hydroxocobalamin (Cyanokit®)** — first-line/gold-standard antidote (2023 American Heart Association guidance recommends hydroxocobalamin for cyanide poisoning-associated cardiac arrest or life-threatening toxicity). Mechanism: the cobalt(III) center of hydroxocobalamin directly binds CN⁻ to form cyanocobalamin (vitamin B12), which is renally excreted — non-toxic and safe for prehospital/field administration, including in smoke-inhalation victims with unknown CO co-exposure (does not impair oxygen-carrying capacity the way nitrites do). NCIT suggestion: closest available NCIT clinical-action term would be Pharmacotherapy (NCIT:C15986) with `therapeutic_agent` bound to the specific compound; note that NCIT has a code for hydroxocobalamin as an agent (search via OAK). **Supply note:** as of November 2024, hydroxocobalamin (Cyanokit) was placed on the ASHP drug-shortage list with no anticipated resolution date at that time — a clinically important recent development affecting antidote availability.
2. **Sodium nitrite** — recommended when hydroxocobalamin is unavailable (2023 AHA guidance); oxidizes hemoglobin iron (Fe²⁺→Fe³⁺) to form methemoglobin, which competitively binds cyanide (higher affinity than cytochrome oxidase) to form cyanomethemoglobin, sparing cytochrome oxidase. Risk: induces methemoglobinemia, which itself impairs oxygen-carrying capacity — relatively contraindicated as first-line in smoke-inhalation victims with concurrent carboxyhemoglobinemia (compounds hypoxia).
3. **Sodium thiosulfate** — reasonable adjunct to either hydroxocobalamin or nitrite (2023 AHA); serves as sulfur donor accelerating the endogenous rhodanese-mediated conversion of cyanide to renally excreted thiocyanate; slower onset than hydroxocobalamin but synergistic in combination, and safe to combine with hydroxocobalamin.
4. **Amyl nitrite** — inhalational bridge therapy (pending IV access) with the same methemoglobin-forming mechanism as sodium nitrite; part of older-generation "Cyanide Antidote Kits."
5. **Dicobalt edetate** — used in some countries (particularly UK, historically); direct cyanide chelator; narrower therapeutic index/higher toxicity than hydroxocobalamin, so used less in North America.

### Supportive Care
100% supplemental oxygen (even though the core lesion is utilization-, not delivery-limited, hyperoxia may partially overcome the reversible cytochrome oxidase inhibition by mass action); aggressive correction of hemodynamic instability (vasopressors, fluids); mechanical ventilation for respiratory failure; sodium bicarbonate for severe acidosis (adjunctive, not primary therapy); seizure management (benzodiazepines); extracorporeal support (ECMO) has been used in refractory cardiogenic shock in case reports; a recent case report highlighted early **blood purification (hemoperfusion/hemodialysis)** as an adjunct in a lethal cyanide poisoning with multimodal management (PMC:[PMC13311073](https://pmc.ncbi.nlm.nih.gov/articles/PMC13311073/), *Frontiers in Pharmacology* 2026).

### Experimental/Emerging Therapeutics (active research, 2024–2026)
- **Cobinamide** — a vitamin B12 precursor/analog lacking the "tail" of cobalamin, giving it higher water solubility and cyanide-binding capacity; found more effective than hydroxocobalamin, thiosulfate, nitrite, or thiosulfate-nitrite combination in mouse models (PMID:[20704457](https://pubmed.ncbi.nlm.nih.gov/20704457/)); under continued development as a next-generation antidote, notably attractive for mass-casualty/military stockpiling due to smaller required dose volumes than hydroxocobalamin.
- **Platinum-based complexes** (hexachloroplatinate, platinum-methionine [Met2Pt]) — investigational metal-based cyanide scavengers showing efficacy in mouse and swine lethal-inhalation models, with intramuscular route feasibility of interest for battlefield/mass-casualty use (2024–2025 preclinical publications, PMC:[PMC6660183](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6660183/); PMC:[PMC13458706](https://pmc.ncbi.nlm.nih.gov/articles/PMC13458706/)).
- **Molybdenum-based [Mo₂O₂(µ-S)₂]²⁺ metallodrug** — a novel cyanide-neutralizing compound evaluated pharmacokinetically in mice (2025), rapidly absorbed with elimination within 8 hours.
- **Dimethyl trisulfide** — a sulfur-donor small molecule investigated as a faster-acting alternative/adjunct to sodium thiosulfate (patented formulations).
- **Metabolic-redirection strategies** — the 2025 FASEB Journal paper by Bebarta and colleagues explores "redirecting intermediary metabolism" (e.g., providing alternative metabolic substrates/cofactors) as a countermeasure strategy distinct from direct cyanide chelation.

### Surgical/Interventional, Rehabilitative, and Chronic-Disease Treatment
Not applicable for acute poisoning beyond supportive/ICU-level intervention. For **delayed dystonic-parkinsonian syndrome**, symptomatic management follows standard movement-disorder approaches (levodopa — often with limited efficacy, since the lesion is post-synaptic striatal rather than nigral dopaminergic — anticholinergics, botulinum toxin for focal dystonia, physical/occupational therapy). For **konzo**, management is rehabilitative/supportive: physical therapy, orthotics/mobility aids, and — critically — public-health-level **prevention** (see Section 13) rather than a curative individual treatment, since the upper-motor-neuron injury is established and largely irreversible.

### Clinical Trials
Given the acute, rare, and often lethal nature of cyanide poisoning, prospective randomized controlled trials in human poisoning are essentially infeasible; the evidence base is built on animal efficacy studies, observational/registry data (e.g., prehospital hydroxocobalamin cohorts), and case series. No disease-specific ClinicalTrials.gov interventional RCTs for acute cyanide poisoning antidotes were identified in this session; most relevant "trials" are preclinical animal pharmacology studies. NCIT suggestion for pharmacotherapy generally: NCIT:C15986 (Pharmacotherapy); for the antidote class specifically, consider a `therapeutic_agent` binding via CHEBI for hydroxocobalamin/thiosulfate/nitrite.

### Pharmacogenomics
No established CPIC/PharmGKB guideline exists for cyanide-antidote dosing based on genotype; TST/MPST genotype-guided dosing remains theoretical/research-stage rather than clinically implemented.

---

## 13. Prevention

**Primary prevention:**
- Engineering/occupational controls in cyanide-handling industries (mining, electroplating): closed-system processing, ventilation, personal protective equipment, biological monitoring (urinary/blood thiocyanate).
- Fire-safety measures reducing combustion of cyanide-releasing synthetic materials, and building-material regulation limiting nitrogen-containing polymer combustion products, are indirect but relevant primary-prevention levers for smoke-inhalation cyanide exposure.
- **Cassava-processing interventions** (soaking, sun-drying, fermentation, "wetting method") to reduce cyanogenic glycoside content before consumption — the central, evidence-based primary-prevention strategy against konzo/TAN in affected sub-Saharan African communities, promoted through community health education programs.
- Restriction/regulation of cyanide salt sales and access reduces suicidal/homicidal ingestion opportunity in some jurisdictions.

**Secondary prevention:**
- Prompt recognition and empiric antidotal treatment protocols for suspected cyanide exposure in fire victims (many EMS systems and burn centers now have standing protocols for empiric prehospital hydroxocobalamin administration in smoke-inhalation patients meeting clinical criteria — altered mental status, soot in airway, hypotension — rather than waiting for confirmatory testing).
- Community-based clinical surveillance for early konzo case detection in cassava-dependent regions during drought/food-insecurity periods, enabling rapid public-health cassava-processing intervention.

**Tertiary prevention:** Rehabilitative care (physical therapy, mobility aids) to minimize secondary complications (contractures, pressure injuries) in established konzo/TAN cases; movement-disorder management to reduce morbidity from delayed dystonic-parkinsonian syndrome.

**Immunization:** Not applicable (non-infectious).

**Screening/early detection:** No individual genetic or newborn screening applies. Population/community-level cassava-processing-adequacy surveillance and biomonitoring (urinary thiocyanate) in at-risk communities functions as an early-warning/risk-stratification tool.

**Behavioral interventions:** Dietary diversification programs to reduce dependence on cassava monoculture and improve sulfur-amino-acid/protein intake in food-insecure regions.

**Counseling:** Not classically "genetic counseling" (non-Mendelian disease), but occupational-health counseling for at-risk workers and public-health education for cassava-dependent communities serve an analogous risk-communication role.

**Public health/environmental interventions:** WHO/FAO guidance on maximum permissible cyanogenic-glycoside content in cassava-derived food products; occupational exposure limits (OSHA/NIOSH permissible exposure limits for hydrogen cyanide and cyanide salts); mining-sector cyanide-management protocols (e.g., the International Cyanide Management Code for the gold-mining industry).

**Prophylaxis:** No standing pre-exposure chemoprophylactic agent is in routine clinical/public-health use; military/first-responder research continues to explore pre-treatment countermeasures (e.g., pre-exposure hydroxocobalamin or dicobalt edetate has shown only "modest and variable efficacy" in porcine models — PMC:[PMC7034532](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7034532/) — underscoring that prophylactic pretreatment is not currently a robust strategy compared to rapid post-exposure antidote administration).

---

## 14. Other Species / Natural Disease

**Taxonomy/species affected:** Cyanide toxicity is essentially universal across aerobic organisms possessing cytochrome c oxidase, given the conserved nature of the mitochondrial electron transport chain. Documented natural/veterinary cyanide poisoning occurs in:
- **Cattle, sheep, goats (NCBITaxon:9913, 9940, 9925)** — most frequently reported livestock cyanide poisoning, typically from grazing on cyanogenic forage plants (sorghum/Sudan grass, Johnson grass, white clover, wild cherry leaves) under stress conditions (drought, frost, wilting) that increase cyanogenic glycoside concentration and hydrolysis (Merck Veterinary Manual).
- **Dogs (NCBITaxon:9615)** — reported cases from cyanide-containing pesticide or rodenticide exposure, or ingestion of cyanogenic plant material; rhodanese distribution across canine respiratory-tract tissue has been specifically studied.
- **Horses, pigs** — less common but documented cyanogenic-plant poisoning.
- **Wildlife** — documented mortality from illegal cyanide use in poaching (e.g., elephant/wildlife poisoning at waterholes in parts of Africa) and from cyanide-based fishing practices in some regions (though the latter is more an ecological/conservation concern than a formally studied "natural disease" model).

**Breed:** No specific Vertebrate Breed Ontology (VBO) susceptibility differences were identified as well-characterized in the literature reviewed; susceptibility in livestock relates more to forage/pasture management than breed genetics.

**Orthologous genes:** TST/rhodanese orthologs are highly conserved across mammals (bovine and canine rhodanese have been extensively studied biochemically, in some cases predating and informing human enzymology); NCBI Gene entries exist for Tst orthologs in mouse (Mus musculus, NCBI Gene ID for Tst) and other model species.

**Comparative pathology:** The core molecular mechanism (Complex IV inhibition, histotoxic hypoxia, lactic acidosis) is conserved across mammalian species, supporting direct translational relevance of animal antidote-efficacy studies to human treatment. Species differences chiefly involve dose sensitivity, respiratory rate/uptake kinetics, and possibly rhodanese tissue distribution/activity levels (e.g., sheep and dog respiratory-tract rhodanese distribution has been specifically mapped).

**Evolutionary conservation:** Cytochrome c oxidase and the rhodanese/TST detoxification system are ancient, highly conserved across eukaryotes (and rhodanese homologs exist even in some bacteria/archaea, reflecting an ancient sulfur-metabolism origin), consistent with cyanide sensitivity being a near-universal aerobic-life vulnerability rather than a human-specific trait.

**Zoonotic potential/transmission:** Not applicable — cyanide poisoning is a direct chemical toxicity, not a transmissible infectious disease; there is no cross-species "transmission," only shared environmental/dietary exposure risk (e.g., livestock and humans sharing exposure to the same cyanogenic forage/food sources in a given region).

---

## 15. Model Organisms

**Model types and their applications** (nearly all model-organism work in this space is **acute pharmacology/antidote-efficacy testing**, not a chronic-disease or genetic model, since cyanide poisoning is an induced toxic exposure rather than a heritable phenotype):

1. **Mouse (Mus musculus)** — the dominant small-animal model for antidote screening, typically via intraperitoneal, subcutaneous, or inhalational KCN/NaCN or HCN-gas challenge with survival/time-to-death as the primary endpoint. Example: cobinamide efficacy studies used mouse lethal-challenge models to demonstrate superiority over hydroxocobalamin, thiosulfate, and nitrite (PMID:20704457). C57BL/6 mice (commonly 8–10 weeks old) are frequently used given established physiological/toxicological reference ranges. **Limitations:** small blood volume limits serial biomarker sampling; interspecies differences in cyanide metabolism kinetics and respiratory physiology limit direct dose-extrapolation to humans; mouse models generally test bolus/rapid lethal challenge rather than the sustained lower-dose inhalational exposure typical of structure fires.
2. **Rat (Rattus norvegicus)** — used in some cyanide/thiocyanate pharmacokinetic and chronic-dietary (cassava-simulating) toxicity studies, including studies of cross-species cyanide detoxification-rate variation under protein-restricted diet conditions — directly relevant to modeling the konzo/malnutrition interaction (ScienceDirect reference on cross-species/tissue detoxification rate variation in rodents and non-human primates on protein-restricted diet).
3. **Swine/porcine models** — considered the most clinically translatable large-animal model given closer cardiovascular and pulmonary physiological similarity to humans; used for lethal cyanide-salt-poisoning and inhalational (fire-simulating smoke) antidote studies, including recent (2025) pilot studies of platinum-methionine complex countermeasures (PMC:[PMC13458706](https://pmc.ncbi.nlm.nih.gov/articles/PMC13458706/)) and earlier studies of pre-exposure hydroxocobalamin/dicobalt edetate efficacy (PMC:[PMC7034532](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7034532/)). **Limitations:** cost and ethical/regulatory burden limit sample sizes; still imperfect recapitulation of human basal-ganglia vulnerability patterns for delayed neurotoxicity endpoints.
4. **Non-human primates (cynomolgus macaque)** — used in some smoke-inhalation/HCN-gas exposure models, particularly for U.S. military/countermeasure development programs (referenced in the 2025 bioRxiv preprint on fire-related toxic gas detection and antidote efficacy in controlled smoke-inhalation models), given closer physiological homology though with substantial ethical/cost constraints limiting widespread use.
5. **Cell-based/in vitro models** — isolated mitochondria and cultured cells (e.g., neuronal or cardiomyocyte cell lines) are used to study cytochrome c oxidase inhibition kinetics, oxidative stress, and candidate-antidote binding chemistry directly, without whole-organism confounds; not a disease "model" per se but mechanistic tool.
6. **Genetic models:** No knockout/knock-in mouse model of TST or MPST deficiency was identified as a well-established, widely used model for studying cyanide-poisoning susceptibility in this search; this represents a potential research gap, since a *Tst*-knockout mouse would directly test the hypothesis that reduced rhodanese activity increases cyanide lethality/sensitivity.

**Resources:** MGI (Mouse Genome Informatics) for Tst/Mpst mouse gene and allele records; IMPC/KOMP for any existing or planned Tst knockout lines; standard toxicology-testing facility protocols (OECD acute-toxicity guidelines) rather than a disease-specific model registry, since this is a chemical-toxicant model rather than a genetic-disease model organism community.

---

## Summary of Key Ontology Term Suggestions

| Category | Suggested terms |
|---|---|
| Disease/condition | MONDO:0018754 (cyanide poisoning); ICD-10-CM T65.0; T57.3 (hydrogen cyanide specifically) |
| Chemical entities (CHEBI) | CHEBI:18407 (hydrogen cyanide); CHEBI:32035 (potassium cyanide); CHEBI:75504 (sodium cyanide); CHEBI:9539 (sodium nitroprusside); CHEBI:2637 (amygdalin); CHEBI:15672 (linamarin) |
| Genes (HGNC) | hgnc:12362 (TST); hgnc:7386 (MPST) |
| GO Biological Process | GO:0006123 (mitochondrial electron transport, cytochrome c to oxygen); GO:0045333 (cellular respiration) |
| GO Cellular Component | GO:0005751 (mitochondrial respiratory chain complex IV); GO:0005739 (mitochondrion) |
| Cell types (CL) | CL:0000746 (cardiac muscle myoblast/cardiomyocyte); CL:0000182 (hepatocyte); relevant striatal/upper-motor-neuron CL terms |
| Anatomy (UBERON) | UBERON:0002349 (myocardium); UBERON:0001873 (globus pallidus); UBERON:0001874 (putamen); UBERON:0002107 (liver); UBERON:0000966 (retina); UBERON:0001846 (cochlea) |
| Phenotypes (HP) | HP:0001259 (Coma); HP:0002615 (Hypotension); HP:0002093 (Respiratory failure); HP:0001695 (Cardiac arrest); HP:0001250 (Seizure); HP:0003128 (Lactic acidosis); HP:0001300 (Parkinsonism); HP:0001332 (Dystonia); HP:0001258 (Spastic paraplegia); HP:0000648 (Optic atrophy); HP:0000407 (Sensorineural hearing loss) |
| Treatment (NCIT) | NCIT:C15986 (Pharmacotherapy) with `therapeutic_agent` for hydroxocobalamin, sodium thiosulfate, sodium/amyl nitrite |

---

## Notes on Evidence Gaps and Caveats

- **No dedicated OMIM entry** exists because this is not a Mendelian disease; genetic-susceptibility data (TST/MPST polymorphisms) come from a single well-cited functional-genetics study (PMID:16790311) and have **not** been validated in large clinical outcome cohorts.
- **Precise contemporary global incidence/prevalence figures** for cyanide poisoning (overall, or split by fire/occupational/suicidal/dietary etiology) are fragmented across poison-control registries, forensic series, and regional epidemiological studies; no single authoritative global-burden-of-disease figure specific to cyanide poisoning was located in this session, and this should be flagged as a gap rather than filled with an unsupported number.
- **Konzo/TAN current prevalence** was not independently re-verified with current-year survey data in this session; cite the primary konzo epidemiological literature directly (PLOS Neglected Tropical Diseases review; Lancet Global Health commentary) for up-to-date figures before curating specific rate values.
- Some PMIDs above were located directly via search and are provided with confidence; where a specific PMID could not be independently confirmed in this session (e.g., some classic Baud et al. NEJM/Hall & Rumack reviews cited by convention in the toxicology literature), the claim is attributed by author/journal/year rather than by an unverified PMID, consistent with anti-fabrication practice.

**Sources:**
- [Interaction of cyanide and nitric oxide with cytochrome c oxidase (PMID:17906319)](https://pubmed.ncbi.nlm.nih.gov/17906319/)
- [Cyanide Toxicity - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK507796/)
- [The two faces of cyanide: environmental toxin and potential gasotransmitter (PMC9291117)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9291117/)
- [Cyanide Beyond Toxicity: vascular function systematic review (PMC12486351)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12486351/)
- [Redirecting Intermediary Metabolism to Counteract Cyanide Poisoning, FASEB J 2025](https://faseb.onlinelibrary.wiley.com/doi/full/10.1096/fj.202400230RR)
- [So Long, Cyanide, Utah Poison Control 2025](https://poisoncontrol.utah.edu/news/2025/02/so-long-cyanide)
- [Acute Cyanide Poisoning: Hydroxocobalamin and Sodium Thiosulfate (PMID:26543483)](https://pubmed.ncbi.nlm.nih.gov/26543483/)
- [Cyanide poisoning in victims of fire: 364 cases (PMID:8150843)](https://pubmed.ncbi.nlm.nih.gov/8150843/?dopt=Abstract)
- [Elevated Blood Cyanide Concentrations in Victims of Smoke Inhalation, NEJM 1991](https://www.nejm.org/doi/full/10.1056/NEJM199112193252502)
- [Evidence for a functional genetic polymorphism of human TST/rhodanese (PMID:16790311)](https://pubmed.ncbi.nlm.nih.gov/16790311/)
- [Orphanet: Cyanide poisoning](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=466670&lng=EN)
- [ICD-10-CM T65.0](https://www.icd10data.com/ICD10CM/Codes/S00-T88/T51-T65/T65-/T65.0)
- [Cyanide poisoning - Wikidata](https://www.wikidata.org/wiki/Q883082)
- [Konzo: From Poverty, Cassava, and Cyanogen Intake to Toxico-Nutritional Neurological Disease, PLOS NTD](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0001051)
- [Cassava food toxins, konzo disease, and neurodegeneration (PMC3653209)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3653209/)
- [Lathyrism, konzo, and tropical ataxic neuropathy - MedLink Neurology](https://www.medlink.com/articles/lathyrism-konzo-and-tropical-ataxic-neuropathy)
- [A case report of acute cyanide poisoning treated with lactate as an indicator (PMID:41204534)](https://pubmed.ncbi.nlm.nih.gov/41204534/)
- [Delayed cyanide induced dystonia (PMC1014725)](https://ncbi.nlm.nih.gov/pmc/articles/PMC1014725)
- [Dystonic-Parkinsonian syndrome after cyanide poisoning: clinical and MRI findings (PMC1032927)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1032927/)
- [Surviving acute cyanide poisoning: longitudinal neuropsychological investigation (PMC3962856)](https://ncbi.nlm.nih.gov/pmc/articles/PMC3962856)
- [MR Changes after Acute Cyanide Intoxication, AJNR 2002](https://www.ajnr.org/content/23/8/1398)
- [Protection from cyanide-induced brain injury by carnosic acid (PMC4465065)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4465065/)
- [Cobinamide superior in mouse model of cyanide poisoning (PMID:20704457)](https://pubmed.ncbi.nlm.nih.gov/20704457/)
- [Pilot study in swine model of lethal cyanide intoxication: platinum-methionine complex (PMC13458706)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13458706/)
- [Intramuscular hexachloroplatinate reverses cyanide-induced metabolic derangements (PMC6660183)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6660183/)
- [Pharmacokinetics/efficacy of molybdenum-based metallodrug in NMRI mice](https://pubmed.ncbi.nlm.nih.gov/42183871/)
- [Modest and variable efficacy of pre-exposure hydroxocobalamin/dicobalt edetate in porcine model (PMC7034532)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7034532/)
- [Forensic toxicology perspective on cyanide poisoning from natural seeds](https://link.springer.com/article/10.1007/s44339-025-00041-x)
- [EFSA: Acute health risks of cyanogenic glycosides in raw apricot kernels, 2016](https://efsa.onlinelibrary.wiley.com/doi/10.2903/j.efsa.2016.4424)
- [Case Report: multimodal management of lethal cyanide poisoning with blood purification (PMC13311073)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13311073/)
- [Sodium Nitroprusside - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK557487/)
- [Evidence for Hydroxocobalamin in Cyanide Toxicity from Smoke Inhalation: Updated Systematic Review (PMC12767669)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12767669/)
- [Prehospital hydroxocobalamin for inhalation injury and cyanide toxicity in the US (PMC5627550)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5627550/)
- [Cyanide Toxicity - Medscape](https://emedicine.medscape.com/article/814287-overview)
- [Cyanide Poisoning in Animals - Merck Veterinary Manual](https://www.merckvetmanual.com/toxicology/cyanide-poisoning/cyanide-poisoning-in-animals)
- [Health risk management framework for heavy metals and cyanide in Kwekwe, Zimbabwe (PMC10069024)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10069024/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 26 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 58 |
| Resolved | 55 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 39 |
| Terms named correctly | 25 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0100660` (1 mention) - the report calls it "Camptocormia — not exact"; HP calls it **Dyskinesia**
- `HP:0007015` (1 mention) - the report calls it "Symmetric limb weakness — approximate"; HP calls it **Poor gross motor coordination**
- `HP:0002061` (1 mention) - the report calls it "Progressive spastic paraparesis, though konzo is characteristically non-progressive once established"; HP calls it **Lower limb spasticity**
- `HP:0007281` (1 mention) - the report calls it "Sensory neuropathy"; HP calls it **Developmental stagnation**
- `CHEBI:75504` (2 mentions) - the report calls it "crystalline salts used in mining/electroplating, common in intentional poisoning"; CHEBI calls it **pyranoside**
- `CHEBI:9539` (2 mentions) - the report calls it "iatrogenic cyanide source via hepatic/enzymatic release of 5 CN⁻ per molecule"; CHEBI calls it **Thiarubrine B**
- `CHEBI:15672` (2 mentions) - the report calls it "cassava, lima beans, flax"; CHEBI calls it **D-tartaric acid**
- `UBERON:0001769` (1 mention) - the report calls it "corticospinal tract"; UBERON calls it **iris**
- `UBERON:0001791` (1 mention) - the report calls it "optic nerve"; UBERON calls it **inner nuclear layer of retina**
- `UBERON:0001846` (2 mentions) - the report calls it "cochlea"; UBERON calls it **internal ear**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005751` (obsolete mitochondrial respiratory chain complex IV) (2 mentions) - replaced by `GO:0045277`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002072` (1 mention) - the report calls it "Chorea, if choreiform component present"; HP calls it **Chorea**, and lists "Choreiform movements" among its other names
- `HP:0001272` (1 mention) - the report calls it "Cerebellar/sensory ataxia"; HP calls it **Cerebellar atrophy**
- `GO:0005751` (2 mentions) - the report calls it "mitochondrial respiratory chain complex IV"; GO calls it **obsolete mitochondrial respiratory chain complex IV**
- `UBERON:0001873` (2 mentions) - the report calls it "globus pallidus"; UBERON calls it **caudate nucleus**, and lists "nucleus caudatus" among its other names