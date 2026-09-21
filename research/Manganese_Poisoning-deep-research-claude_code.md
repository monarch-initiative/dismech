---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-20T03:25:26.478572'
end_time: '2026-09-20T03:31:03.918306'
duration_seconds: 337.44
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Manganese Poisoning
  mondo_id: MONDO:0017638
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
  web_search_requests: 11
  num_turns: 13
  total_cost_usd: 1.3549428000000001
  session_id: dc83c613-1fba-53b8-9741-f63fb2448a6e
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 35
reference_validation:
  total_references: 27
  verified: 27
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 27
  on_topic: 13
  validator_version: 0.2.1
term_validation:
  total_terms: 56
  verified: 51
  not_found: 0
  obsolete: 1
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 33
  labels_matching: 20
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: MONDO:0013327
    reported_labels:
    - HMNDYT1
    ontology_label: primary hyperoxaluria type 3
  - term_id: CHEBI:29486
    reported_labels:
    - manganese atom
    ontology_label: 4-Benzyloxybenzyl alcohol
  - term_id: HP:0000723
    reported_labels:
    - Personality changes
    ontology_label: Restrictive behavior
  - term_id: HP:0001402
    reported_labels:
    - Cirrhosis
    ontology_label: Hepatocellular carcinoma
  - term_id: GO:0071573
    reported_labels:
    - "metal ion transmembrane transport \u2014 search for the manganese-specific\
      \ child term"
    ontology_label: shelterin complex assembly
  - term_id: CL:0000030
    reported_labels:
    - glial cell
    ontology_label: glioblast
  - term_id: UBERON:0002087
    reported_labels:
    - Subthalamic nucleus
    ontology_label: atrioventricular canal
  - term_id: UBERON:0002319
    reported_labels:
    - Anterior pituitary
    ontology_label: mesangium
  labels_variant: 5
  obsolete_terms:
  - term_id: GO:0006542
    ontology_label: obsolete glutamine biosynthetic process
    replaced_by: GO:1901704
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Manganese Poisoning
- **MONDO ID:** MONDO:0017638 (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Manganese Poisoning** covering all of the
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

I'll research key aspects of manganese poisoning (manganism) to ground this report in current literature.

# Manganese Poisoning (Manganism): Comprehensive Research Report

**Disease Name:** Manganese Poisoning / Manganism
**MONDO ID:** MONDO:0017638 (as provided; note: MONDO also carries related but distinct concepts — MONDO:0017638 corresponds to "manganese poisoning" in MONDO's environmental-disease branch, while the genetic conditions below are separately coded as MONDO:0013327/OMIM:613280 [HMNDYT1] and MONDO:0014982/OMIM:617013 [HMNDYT2]. Confirm the exact node before binding.)
**Category:** Environmental (with genetic phenocopies — see §4)

---

## 1. Disease Information

**Overview.** Manganese (Mn) is an essential trace element required as a cofactor for enzymes including arginase, glutamine synthetase, pyruvate carboxylase, and manganese superoxide dismutase (MnSOD/SOD2), but it is neurotoxic in excess. "Manganism" classically refers to a syndrome of chronic manganese intoxication producing an extrapyramidal, parkinsonism-like movement disorder with characteristic psychiatric and cognitive features, first described among manganese-ore grinders by Couper in 1837 and later detailed in Chilean miners by Rodier (1955). Modern usage covers a spectrum: (1) classic occupational manganism from inhalational exposure (mining, ferroalloy/steel production, welding, dry-cell battery manufacturing); (2) iatrogenic/nutritional manganese toxicity from parenteral nutrition (PN) or from impaired biliary excretion in liver disease; (3) environmental exposure via contaminated drinking water or soil, particularly affecting children's neurodevelopment; and (4) genetic/inherited hypermanganesemia due to biallelic loss-of-function variants in the manganese transporters **SLC30A10** or **SLC39A14**, which produce a similar or identical basal-ganglia phenotype without external overexposure. The unifying pathophysiology across all forms is preferential Mn deposition in the globus pallidus and other basal ganglia structures, producing dystonia-parkinsonism.

**Key identifiers:**
- **OMIM:** #613280 (Hypermanganesemia with Dystonia 1, HMNDYT1 / SLC30A10); #617013 (Hypermanganesemia with Dystonia 2, HMNDYT2 / SLC39A14)
- **Orphanet:** ORPHA:294604 (Hypermanganesemia with dystonia 1); ORPHA:401920 (Hypermanganesemia with dystonia 2); manganese poisoning itself is not separately Orphanet-coded (it is an acquired toxic condition, not a rare genetic disease per se)
- **ICD-10-CM:** T57.2X1A (toxic effect of manganese and its compounds, accidental, initial encounter); G21.8 (other secondary parkinsonism, used clinically for manganism); ICD-11: NE61 / 5B51 category context for metal toxicity
- **MeSH:** D008377 (Manganese Poisoning); D008378 (Manganese); the classic clinical entity is sometimes indexed as "Parkinsonian Disorders, Secondary"
- **MONDO:** MONDO:0017638 (manganese poisoning); MONDO:0013327 (HMNDYT1); MONDO:0014982 (HMNDYT2)
- **HGNC genes:** SLC30A10 (hgnc:20303), SLC39A14 (hgnc:20860), and modulatory SLC39A8 (hgnc:20862)

**Synonyms:** Manganism; chronic manganese poisoning; manganese-induced parkinsonism; manganese neurotoxicity; "locura manganica" (manganese madness — historical term for the early psychiatric phase); Hypermanganesemia with Dystonia, Polycythemia and Cirrhosis (HMDPC, the eponymous name for HMNDYT1).

**Evidence basis.** The literature is a mix of individual case reports and case series (occupational cohorts, PN patients, poisoned children), aggregated occupational-cohort epidemiology (notably the Racette/Washington University welder cohorts), environmental/EHR-adjacent population studies (drinking-water cohorts in Bangladesh, Canada, Italy, US), and gene-discovery family studies for the inherited forms (consanguineous pedigrees). There is no large administrative-claims registry specific to manganism; most quantitative data come from occupational-medicine and toxicology cohort studies rather than EHR mining.

---

## 2. Etiology

### Disease Causal Factors
Manganism has both **environmental/exposure-driven** and **genetic** etiologies converging on the same downstream mechanism — pathological Mn accumulation in brain, especially basal ganglia:

1. **Occupational inhalation exposure**: welding fume (shielded metal arc and gas metal arc welding of steel, which contains 0.5–1.5% Mn), ferroalloy/ferromanganese smelting, manganese ore mining and milling, dry-cell (alkaline) battery manufacturing, and manganese-containing fungicide (maneb, mancozeb) production/application.
2. **Iatrogenic/nutritional**: chronic total parenteral nutrition (TPN) with unrestricted or unmonitored Mn supplementation, particularly in patients with cholestatic liver disease who cannot excrete Mn via bile.
3. **Environmental/dietary**: manganese-contaminated well or groundwater (naturally occurring geogenic Mn or from mining runoff), especially in Bangladesh, parts of Canada, the US Northeast, and China; soy-based infant formula (naturally higher Mn than breast milk) has been raised as a lower-level concern in infants.
4. **Contaminated illicit drugs**: "manganese madness" has historically been reported among users of home-synthesized methcathinone ("ephedrone") prepared using potassium permanganate as an oxidant, which introduces large amounts of Mn directly into the bloodstream (PMID:18094334, Sanotsky et al., 2007, and related ephedrone-abuse case series).
5. **Genetic (inherited hypermanganesemia)**: biallelic loss-of-function variants in **SLC30A10** (a cell-surface Mn efflux transporter required for hepatobiliary and intestinal Mn excretion) cause HMNDYT1/HMDPC; biallelic loss-of-function variants in **SLC39A14** (a plasma-membrane Mn importer expressed highly in liver) cause HMNDYT2. Both produce markedly elevated blood Mn and basal ganglia deposition even with normal environmental exposure — the genetic disorders are, mechanistically, "manganese poisoning from an endogenous source."
6. **Chronic liver disease / portosystemic shunting**: cirrhosis of any cause impairs biliary Mn excretion (the primary excretory route for Mn, which undergoes enterohepatic recirculation), leading to secondary hypermanganesemia and T1-hyperintense basal ganglia deposits — clinically and radiologically convergent with classic manganism even without occupational exposure.

### Risk Factors

**Genetic risk factors:**
- Biallelic pathogenic variants in *SLC30A10* or *SLC39A14* (causal, Mendelian, autosomal recessive)
- Heterozygous/common polymorphisms in *SLC30A10* and *SLC39A8* have been associated with blood Mn levels and neurodevelopmental outcomes in population studies, suggesting these act as modifier/susceptibility loci for environmental Mn exposure (Frontiers in Genetics, 2018, on SLC30A10/SLC39A8 polymorphisms and children's neurodevelopment)
- Iron deficiency: because Mn and iron share transporters (notably DMT1/SLC11A2 and possibly ferroportin-related pathways), iron-deficient individuals absorb dietary/environmental Mn more efficiently, amplifying neurotoxic risk — well documented in both occupational and pediatric drinking-water cohorts.

**Environmental risk factors:**
- Occupational inhalational exposure intensity and duration (cumulative exposure index used in welder cohorts)
- Concurrent iron deficiency anemia (increases intestinal Mn absorption via shared transporters)
- Chronic liver disease/cirrhosis (impaired biliary excretion)
- Chronic total parenteral nutrition, especially in infants/children and in cholestatic patients
- Age: infants and young children absorb dietary Mn more efficiently and excrete it less effectively than adults (immature biliary excretion), making early life a window of heightened vulnerability
- Male sex has historically dominated occupational cohorts (reflecting workforce composition rather than intrinsic biological susceptibility), though some pediatric drinking-water studies report sex-differential cognitive effects (adverse effects more pronounced, or more pronounced in a particular sex depending on the cohort — findings are mixed across Bangladesh and Canadian studies)
- Low socioeconomic status/well-water reliance in regions with geogenic Mn contamination.

**Protective factors:**
- Adequate dietary iron status (reduces competitive intestinal Mn uptake)
- Engineering controls and personal protective equipment (respirators, local exhaust ventilation) in occupational settings — the primary, evidence-supported public-health intervention
- Water treatment/filtration removing Mn from drinking water in affected communities
- Early recognition and cessation of Mn-containing PN or dietary supplementation in at-risk patients.

**Gene-environment interactions:** The clearest documented interaction is between iron status and Mn absorption — iron deficiency up-regulates divalent metal transporters shared by Fe and Mn, increasing gut Mn uptake and blood Mn levels for a given environmental exposure. A second interaction axis is between common *SLC30A10*/*SLC39A8* polymorphisms and environmental Mn exposure level in determining blood Mn and neurodevelopmental outcome (gene-dose-modulated susceptibility to a given environmental dose), distinct from the rare biallelic loss-of-function alleles that cause disease independent of exposure.

**Suggested ontology terms:** exposure to manganese (ECTO — search `l~manganese` for the specific route-qualified term, e.g. "exposure to manganese via inhalation," "exposure to manganese in drinking water"); CHEBI:18291 (manganese(0)) / CHEBI:29486 (manganese atom) / relevant Mn(II) ion CHEBI term for the toxic species; NCIT term for occupational exposure category.

---

## 3. Phenotypes

Manganism phenotypes span three classic and partially sequential domains: an early **psychiatric/behavioral phase** ("manganese madness"), followed by a **motor/extrapyramidal phase**, with **hepatic and hematologic** features prominent in the genetic/hepatic forms.

### Psychiatric / behavioral (early phase)
- Irritability, emotional lability, compulsive or aggressive behavior — HP:0000710 (Delusions is too strong; better: HP:0000737 Irritability), HP:0000723 (Personality changes)
- Impulsivity, disinhibition, occasionally frank psychosis in severe/acute cases ("locura manganica")
- Reduced libido
- Sleep disturbance, fatigue
- **Onset:** typically after months to a few years of significant exposure; considered the prodromal/reversible phase if exposure is stopped early.

### Motor / extrapyramidal (established phase)
- **Bradykinesia** — HP:0002067
- **Gait disturbance**, characteristically a wide-based, "cock-walk" (steppage-like, propulsive) gait distinct from the shuffling, festinating gait of idiopathic Parkinson disease — HP:0001288 (Gait disturbance)
- **Postural instability** — HP:0002172
- **Dystonia**, often affecting the face, neck, or limbs, including risus sardonicus-like facial dystonia in genetic forms — HP:0001332
- **Rigidity** (typically symmetric, in contrast to the asymmetric rigidity of idiopathic PD) — HP:0002063
- **Tremor** — classically postural/action tremor rather than the classic pill-rolling resting tremor of idiopathic PD, though rest tremor can occur — HP:0001337
- **Hypomimia** (masked facies) — HP:0000338
- **Micrographia** — HP:0031936
- **Dysarthria**, hypophonic/monotone speech — HP:0001260
- **Bulbar dysfunction** (dysphagia, in severe pediatric SLC39A14-related disease) — HP:0002310
- **Loss of postural reflexes / falls**

**Key differentiating clinical features vs. idiopathic Parkinson disease** (important for the differential diagnosis section): symmetric onset, prominent early gait/postural instability, poor or absent response to levodopa, dystonia (especially of the face/neck) more prominent than in idiopathic PD, and absence of resting pill-rolling tremor in most cases.

### Hepatic / hematologic (SLC30A10-specific / secondary hepatic forms)
- **Hepatomegaly**, progressing to **cirrhosis** — HP:0001402 (Cirrhosis)
- **Polycythemia** — HP:0001901 (elevated hemoglobin/hematocrit, thought to result from Mn-induced HIF2α stabilization driving erythropoietin production; recent mouse work — Metallomics 2024 — implicates HIF signaling in this Mn-polycythemia link)
- Elevated liver enzymes, coagulopathy in advanced cirrhosis.

### Laboratory abnormalities
- Elevated whole-blood manganese (the standard biomarker; normal range roughly 4–15 µg/L, with symptomatic patients often >2–10x upper limit)
- Elevated hair/toenail manganese (used in some environmental/epidemiologic studies as a longer-term exposure biomarker, though less standardized)
- Elevated urinary manganese (used to monitor chelation response)
- Polycythemia/erythrocytosis on CBC in SLC30A10 disease
- Abnormal liver function tests in SLC30A10 disease and secondary hepatic manganism.

### Neuroimaging as a phenotype-adjacent finding
- **Bilateral, symmetric T1-weighted hyperintensity** in the globus pallidus, and in more severe/genetic cases extending to the striatum, subthalamic nucleus, substantia nigra, cerebellar dentate nucleus, and anterior pituitary — the single most characteristic paraclinical finding, well reviewed in a 2024 narrative review on MRI and manganism (PMC11122624). T2-weighted sequences typically show corresponding hypointensity or are unremarkable. This pattern is distinct from the T2-hyperintense signal changes typical of many other neurodegenerative and toxic-metabolic basal ganglia disorders.

### Phenotype characteristics
- **Age of onset:** occupational manganism — typically adult, after years of cumulative exposure; genetic forms — early childhood, often within the first years of life, especially SLC39A14-related disease, which can present with loss of previously acquired motor milestones in infancy; hepatic/PN-related — any age, including neonates on prolonged PN.
- **Severity:** ranges from subclinical biomarker elevation and subtle neurobehavioral changes (environmental/pediatric drinking-water exposure) to severe, disabling parkinsonism-dystonia with loss of ambulation (genetic forms, especially SLC39A14).
- **Progression:** occupational manganism is classically considered to progress even after exposure cessation in a subset of patients (unlike acute heavy-metal intoxications that fully resolve), an observation central to the "manganese-induced parkinsonism" reconceptualization (Guilarte, NeuroMolecular Medicine 2010/PMID:20012385). Genetic forms are typically rapidly progressive in infancy without treatment.
- **Frequency among exposed:** a prevalence of clinical parkinsonism of ~15.6% was reported among 716 welders in one Washington University cohort (Andruska & Racette), versus a background rate of roughly 2% in the general population over 65.

### Quality of life impact
Motor disability (gait, dysarthria, dystonia) and psychiatric symptoms substantially impair occupational function and activities of daily living; several occupational cohort studies report early retirement/disability due to manganism-related motor impairment. Standardized QOL instruments (EQ-5D, SF-36) are not routinely reported in the manganism literature; most functional data use UPDRS-III motor scores as a surrogate.

---

## 4. Genetic / Molecular Information

### Causal genes (inherited hypermanganesemia — the genetic phenocopy of manganism)

| Gene | HGNC | OMIM disease | Inheritance | Function |
|---|---|---|---|---|
| **SLC30A10** | hgnc:20303 | #613280 (HMNDYT1/HMDPC) | Autosomal recessive | Plasma-membrane/Golgi Mn efflux transporter; required for hepatobiliary and enteric Mn excretion. Loss-of-function → failure to export Mn from hepatocytes and other cells → systemic and CNS Mn accumulation. |
| **SLC39A14** | hgnc:20860 | #617013 (HMNDYT2) | Autosomal recessive | Plasma-membrane Mn (and Zn/Fe) importer, highly expressed in liver; mediates hepatic Mn clearance from portal blood. Loss-of-function → failure of hepatic first-pass Mn clearance → systemic hypermanganesemia and CNS deposition without polycythemia/cirrhosis. |
| **SLC39A8** (modifier) | hgnc:20862 | related CDG (SLC39A8-CDG, OMIM #616721) also implicated in Mn homeostasis | AR (for the CDG); common variants act as modifiers | Manganese/zinc importer; common polymorphisms associated with blood Mn levels and neurodevelopmental sensitivity to environmental Mn. |

**Discovery literature:** SLC30A10 was established as the HMNDYT1 gene by Quadri et al. (2012, *American Journal of Human Genetics*) and Tuschl et al. (2012, *American Journal of Human Genetics*) in consanguineous families with hypermanganesemia, dystonia, polycythemia, and cirrhosis. SLC39A14 was established as the HMNDYT2 gene by **Tuschl et al., 2016, *Nature Communications* 7:11601, PMID:27231142** ("Mutations in SLC39A14 disrupt manganese homeostasis and cause childhood-onset parkinsonism–dystonia"), identifying five distinct homozygous variants (two truncating, three missense) across affected families, with functional studies in HEK293 cells showing decreased Mn uptake for the missense alleles (loss-of-function mechanism). Balint et al. (2016, *Movement Disorders*) further expanded the SLC39A14 mutational spectrum.

### Pathogenic variant classes
- **SLC30A10**: predominantly missense and truncating (nonsense/frameshift) variants disrupting the transporter's trafficking to the plasma membrane or its efflux activity; a 2014 *Journal of Neuroscience* study showed parkinsonism-causing SLC30A10 mutations block intracellular trafficking and Mn efflux activity of the transporter.
- **SLC39A14**: missense variants (reducing but not abolishing surface expression/uptake activity) and truncating variants; genotype-phenotype correlation is incomplete but truncating variants tend toward more severe, earlier-onset disease.
- Classified as **Pathogenic/Likely Pathogenic** per ACMG/AMP criteria in ClinVar for the recurrent founder and novel alleles reported across case series (e.g., ClinVar entries for SLC39A14 c.292T>G p.Phe98Val and multiple SLC30A10 alleles).
- **Zygosity:** homozygous or compound heterozygous (autosomal recessive); heterozygous carriers are asymptomatic with normal or near-normal blood Mn.
- **Allele frequency:** both genes' pathogenic alleles are individually very rare in gnomAD (largely private or founder variants in consanguineous populations — Saudi Arabian, Pakistani, and other consanguineous cohorts are overrepresented in the literature), consistent with an ultra-rare autosomal recessive disorder.
- **Somatic vs. germline:** exclusively germline; no somatic/mosaic manganism-related variants have been reported.
- **Functional consequence:** loss of function in both genes, converging mechanistically on failure to clear systemic/hepatic Mn, producing the same downstream basal-ganglia Mn toxicity as environmental overexposure.

### Epigenetic information
Emerging (largely preclinical) evidence indicates Mn exposure itself induces epigenetic changes — altered DNA methylation and histone modification patterns have been reported in Mn-exposed model systems and in some human biomonitoring studies of Mn-exposed workers, implicated in the neuroinflammatory and transcriptional dysregulation seen in basal ganglia tissue (see mouse *Slc30a10* knockout transcriptomic studies below, Metallomics 2024, PMC10883138, reporting >1,000 differentially expressed genes in basal ganglia sub-regions). This is an active but not yet mechanistically definitive area; specific PMID-level human epigenome-wide association studies (EWAS) in manganism specifically are limited compared to other heavy metals (e.g., lead, arsenic).

### Chromosomal abnormalities
None reported; manganism/hypermanganesemia is a single-gene (biallelic) or purely acquired/environmental condition — no aneuploidy, translocation, or copy-number variant etiology is described.

**Suggested ontology terms:** gene: hgnc:20303 (SLC30A10), hgnc:20860 (SLC39A14), hgnc:20862 (SLC39A8); GO:0005385 (zinc ion transmembrane transporter activity, related family) — more precisely, manganese transmembrane transporter activity terms exist in GO (search for "manganese ion transmembrane transporter activity"); relevant CL terms for hepatocyte (CL:0000182) as the primary site of SLC30A10/SLC39A14 action.

---

## 5. Environmental Information

### Environmental factors (non-genetic contributing causes)
- **Occupational airborne Mn** (fume/dust) from welding, ferroalloy smelting, mining/ore processing, and dry-cell battery manufacture — the dominant classic cause. Welding fume composition varies by process (GMAW/MIG vs. SMAW/stick) and base metal, with Mn content around 0.5–1.5% typical of most steels, generating respirable Mn oxide fume.
- **Manganese-containing fungicides**: maneb and mancozeb (ethylene-bis-dithiocarbamate fungicides) used in agriculture are absorbed dermally/by inhalation and metabolized to release Mn; agricultural applicators are a recognized at-risk group, and there is long-standing interest in maneb/paraquat combined exposure as a Parkinson-disease risk factor in epidemiologic studies (distinct from classic occupational manganism but mechanistically related).
- **Drinking water**: naturally occurring geogenic Mn in groundwater, and Mn released by mining/industrial runoff, are the principal non-occupational environmental exposure route, especially relevant to pediatric neurodevelopment (see below).
- **Contaminated illicit drug synthesis**: potassium permanganate used in home methcathinone ("ephedrone"/"jeff") synthesis introduces very high intravenous Mn doses, producing a rapid, severe manganism phenotype in drug users (well documented in Eastern Europe/Ukraine case series).

### Lifestyle factors
- **Dietary iron intake/status** modulates intestinal Mn absorption (see §2)
- **Vegetarian/high-Mn diets** (nuts, whole grains, tea, leafy greens are naturally Mn-rich) are a minor contributor in the general population but not typically sufficient alone to cause clinical manganism in individuals with normal hepatobiliary function
- **Alcohol use** contributing to underlying liver disease can secondarily predispose to hepatic Mn retention.

### Infectious agents
Not applicable — manganism is not an infectious disease and has no known infectious trigger or cofactor.

**Suggested ECTO terms:** search ECTO for "exposure to manganese," "exposure to manganese via inhalation," "exposure to manganese in drinking water via ingestion," and "exposure to maneb"/"exposure to mancozeb" for the fungicide route.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (occupational/environmental manganism)

1. **Chronic inhalation (or, in genetic disease, failure of hepatobiliary clearance) of manganese** leads to sustained elevation of systemic and cerebral free Mn²⁺/Mn³⁺.
2. Elevated blood Mn **leads to** preferential uptake into brain via transferrin-receptor-mediated and DMT1-mediated transport across the blood-brain barrier and via the olfactory/nasal-to-brain route for inhaled Mn, **resulting in** disproportionate accumulation in the **globus pallidus**, and with more severe/chronic exposure, the striatum, subthalamic nucleus, and substantia nigra pars reticulata — regions with high mitochondrial density and iron-transport machinery that Mn co-opts.
3. Intracellular Mn accumulates preferentially in **mitochondria** (via the mitochondrial calcium uniporter and other Ca²⁺ transport systems, to which Mn²⁺ is a permeant substrate), **leading to** inhibition of oxidative phosphorylation complex II and disruption of the electron transport chain.
4. Mitochondrial dysfunction **results in** increased reactive oxygen species (ROS) generation and **oxidative stress**, compounded by Mn's ability to auto-oxidize between Mn²⁺ and Mn³⁺ states and catalyze Fenton-like chemistry, **leading to** lipid peroxidation, protein oxidation, and DNA damage in vulnerable neurons and astrocytes.
5. In **astrocytes**, which preferentially sequester Mn (astrocytes express high levels of Mn-dependent glutamine synthetase and take up Mn avidly), Mn accumulation **impairs glutamate-glutamine cycling**, **leading to** extracellular glutamate accumulation and excitotoxic stress on neighboring neurons — this is a proposed but only partially demonstrated (largely model-organism/*in vitro*) branch of the mechanism.
6. Oxidative and excitotoxic stress **triggers neuroinflammation**: activation of microglia and astrocytes, release of pro-inflammatory cytokines (TNF-α, IL-6, IL-1β), which **exacerbates** neuronal injury in a feed-forward loop — this neuroinflammatory amplification is now considered a central, not incidental, mechanism (2023–2024 reviews, e.g., Biomolecules 2023, DOI:10.3390/biom13081190).
7. In the **globus pallidus**, cumulative oxidative/inflammatory injury **leads to** neuronal loss and gliosis, disrupting pallidal output to the thalamus and, via basal ganglia circuitry (striato-pallidal-thalamocortical and subthalamic-nigral loops), **results in** the movement-disorder phenotype: bradykinesia, rigidity, dystonia, and gait/postural instability.
8. **Critically, in classic manganism, the primary lesion appears to be pallidal/pre-synaptic circuit dysfunction with relative sparing of nigrostriatal dopaminergic terminals**, distinguishing it mechanistically from idiopathic Parkinson disease (where substantia nigra pars compacta dopaminergic neuron loss is primary) — this is why manganism responds poorly to levodopa. With very high or genetic-level chronic Mn burden, however, the substantia nigra pars compacta and dopaminergic transmission can become secondarily involved, and 2023-era work (Biomolecules 2023) more explicitly incorporates dopaminergic dysfunction as a downstream/graded rather than purely absent feature — this remains a point of ongoing mechanistic refinement rather than settled consensus.
9. **Branch — hepatic/hematologic arm (SLC30A10 disease specifically):** loss of hepatocyte Mn efflux **leads to** hepatocellular Mn accumulation, **resulting in** hepatocyte injury and progression to cirrhosis; separately, Mn-induced stabilization of **hypoxia-inducible factor 2α (HIF2α)** signaling (demonstrated in *Slc30a10* knockout mice, Metallomics 2024, and a related 2023 bioRxiv preprint "Hypoxia-inducible factor 2 is a key determinant of manganese excess and polycythemia in SLC30A10 deficiency") **leads to** increased erythropoietin transcription and **results in** the polycythemia observed clinically — this is an inferred mechanism from mouse models, not yet directly demonstrated in human tissue.
10. **Branch — neuronal cell-type specificity:** a 2024/2025 neuron-specific *Slc30a10* modulation study (PNAS, PMC12890882) identifies **dopaminergic and glutamatergic neurons specifically** as the cell types whose Mn efflux capacity determines vulnerability to Mn-induced motor disease, refining step 6–8 above to a cell-autonomous mechanism within the basal ganglia circuit rather than a purely diffuse toxic effect.

### Molecular pathways
- Mitochondrial oxidative phosphorylation / electron transport chain (Complex II particularly implicated)
- Glutamate–glutamine cycle (astrocytic glutamine synthetase, a Mn-dependent enzyme, is directly relevant — excess Mn paradoxically both requires and disrupts this pathway)
- NF-κB and other pro-inflammatory transcriptional pathways in microglia/astrocytes
- HIF2α/erythropoietin signaling (SLC30A10-specific polycythemia mechanism)
- Dopaminergic neurotransmission pathways (secondary/graded involvement)

**Suggested GO terms:** GO:0006826 (iron ion transport, related transporter family context); GO:0071573 (metal ion transmembrane transport — search for the manganese-specific child term); GO:0006979 (response to oxidative stress); GO:0034599 (cellular response to oxidative stress); GO:0006915 (apoptotic process); GO:0002526 (acute inflammatory response) / GO:0150076 (neuroinflammatory response); GO:0006536 (glutamate metabolic process); GO:0006542 (glutamine biosynthetic process, glutamine synthetase-relevant).

**Suggested CL terms:** CL:0000030 (glial cell), CL:0000127 (astrocyte), CL:0000129 (microglial cell), CL:0000700 (dopaminergic neuron), CL:0000182 (hepatocyte), CL:0002605 (GABAergic interneuron, relevant to pallidal projection neurons — verify against the specific medium spiny/pallidal neuron term).

### Cellular processes, protein dysfunction, metabolic changes
- **Apoptosis/necrosis** of pallidal and (in severe cases) nigral neurons
- **Protein dysfunction**: SLC30A10 mutant proteins are mistrafficked (retained intracellularly rather than reaching the plasma membrane) — a folding/trafficking defect rather than a catalytic-site defect for most missense alleles (Journal of Neuroscience, 2014); SLC39A14 missense mutants show reduced but not absent Mn transport activity when expressed at the cell surface.
- **Metabolic changes**: disrupted mitochondrial energy metabolism (reduced ATP production), altered glutamate/glutamine and possibly GABA metabolism in basal ganglia.

### Molecular profiling / advanced technologies
- **Transcriptomics**: *Slc30a10* knockout mouse basal ganglia RNA-seq shows >1,000 differentially expressed genes across sub-regions, enriched for neurotransmission and hypoxia-response pathways (Metallomics 2024, PMC10883138); zebrafish *slc39a14* mutant transcriptomics show differentially expressed genes mapping to CNS and eye, with calcium dyshomeostasis and unfolded protein response activation as prominent signatures.
- **Single-cell/cell-type-specific genetics**: the 2024/2025 PNAS neuron-specific *Slc30a10* modulation study represents the most advanced cell-type-resolved functional genomic approach to date, using conditional/neuron-restricted transporter manipulation to isolate dopaminergic and glutamatergic neuron contributions.
- Proteomics, metabolomics, lipidomics, and spatial transcriptomics datasets specific to human manganism are sparse; most molecular-profiling data derive from rodent and zebrafish models rather than human autopsy/biopsy tissue, which is a recognized gap.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** central nervous system, specifically the basal ganglia (see below); liver (in SLC30A10 disease and in secondary/hepatic manganism)
- **Secondary:** hematopoietic system (polycythemia in SLC30A10 disease); occasionally lung (as the portal of occupational entry, though pulmonary pathology itself is not typically a manganism feature distinct from general fume-inhalation lung disease)
- **Body systems:** nervous system (primary), hepatobiliary system, hematologic system.

**Tissue and cell level:**
- Basal ganglia neurons (medium spiny/GABAergic projection neurons of the striatum and globus pallidus), dopaminergic neurons of the substantia nigra pars compacta (secondary/graded involvement), glutamatergic neurons, astrocytes (major Mn-sequestering cell type), microglia (neuroinflammatory effector cells), hepatocytes (site of SLC30A10/SLC39A14 action).

**Subcellular level:**
- **Mitochondria** (GO:0005739, Mitochondrion — primary subcellular target of Mn toxicity via the mitochondrial Ca²⁺ uniporter)
- Golgi apparatus/secretory pathway (site of SLC30A10 normal trafficking, disrupted by mutant alleles)
- Plasma membrane (site of both transporters' normal function).

**Localization (anatomical sites, UBERON):**
- **Globus pallidus** (UBERON:0002476) — the signature site of T1-weighted MRI hyperintensity and the primary pathological target
- **Striatum/caudate-putamen** (UBERON:0002435 caudate nucleus / UBERON:0001874 putamen or UBERON:0002435 as appropriate)
- **Subthalamic nucleus** (UBERON:0002087)
- **Substantia nigra** (UBERON:0002038)
- **Cerebellar dentate nucleus** (UBERON:0002037, or the specific dentate nucleus term)
- **Anterior pituitary** (UBERON:0002319) — reported as an additional site of T1 hyperintensity in some severe/genetic cases
- **Liver** (UBERON:0002107) — in SLC30A10-related disease.

**Lateralization:** Manganism lesions and clinical signs are characteristically **bilateral and symmetric**, a key distinguishing radiological and clinical feature from idiopathic Parkinson disease, which is typically asymmetric at onset.

---

## 8. Temporal Development

**Onset:**
- Occupational manganism: typically insidious, developing after months to several years of cumulative exposure; a prodromal psychiatric phase often precedes overt motor signs by months to years.
- Genetic (SLC39A14): onset in infancy, often with loss of previously acquired motor milestones in the first one to two years of life — an aggressive, early pediatric course.
- Genetic (SLC30A10/HMDPC): onset can range from infancy to early childhood, sometimes with polycythemia/hepatic findings preceding overt neurological signs.
- Iatrogenic (PN-associated): weeks to months of unmonitored Mn-supplemented PN, in any age group but particularly reported in infants and cholestatic patients.
- Environmental (drinking water, pediatric): a more indolent, subclinical neurodevelopmental effect rather than acute-onset movement disorder, manifesting as measurable IQ/cognitive/behavioral deficits detected in cohort studies rather than as a diagnosed "poisoning" event.

**Progression:**
- Disease course pattern: classically **progressive**, and importantly, a subset of occupational manganism patients continue to progress even after removal from exposure — this "delayed/self-sustaining progression" phenomenon underlies the reconceptualization from acute "manganism" to a chronic "manganese-induced parkinsonism" model (Guilarte 2010, PMID:20012385) analogous in some respects to the persistent parkinsonism seen after MPTP exposure.
- Genetic pediatric forms (especially SLC39A14) are typically **rapidly progressive** without treatment, leading to loss of ambulation.
- Disease stages are not formally codified (no accepted staging system analogous to Hoehn & Yahr, though UPDRS-III is commonly used as a continuous severity/progression measure in occupational cohorts).
- Disease duration: chronic/lifelong once established; the motor phenotype is generally not considered fully reversible in advanced disease, though early treatment (exposure cessation ± chelation) can produce substantial and sometimes near-complete improvement, particularly in the genetic and iatrogenic/hepatic forms.

**Patterns:**
- **Remission**: reported with early cessation of exposure (occupational, PN-associated) and with chelation therapy, particularly effective when initiated before irreversible neuronal loss; TPN-associated pediatric cases have shown symptom and MRI improvement within weeks to a month of discontinuing Mn-supplemented PN.
- **Critical periods**: infancy/early childhood is a recognized critical window both for genetic disease severity (younger onset in SLC39A14 correlates with more devastating course) and for environmental/drinking-water neurodevelopmental vulnerability, reflecting developmentally immature biliary Mn excretion and blood-brain barrier permeability in early life.

---

## 9. Inheritance and Population

**Epidemiology:**
- No single, comprehensive global prevalence/incidence figure exists for "manganism" as a whole because it spans multiple distinct exposure etiologies. Occupational cohort data are the best-quantified: a prevalence of clinical parkinsonism of **15.6% among 716 welders** was reported in one Washington University shipyard/fabrication-shop cohort (Andruska & Racette), compared with ~2% background PD prevalence in the general population over 65. A separate literature review using IRSST expert-panel criteria identified 78 cases of probable/possible occupational manganism plus 19 additional possible cases specifically among welders in the published literature.
- The genetic forms (HMNDYT1/HMNDYT2) are **ultra-rare**, with only several dozen families reported worldwide in the literature since 2012/2016, concentrated in consanguineous populations.
- Environmental/pediatric drinking-water exposure affects potentially large populations where geogenic or industrial Mn contamination is present (parts of Bangladesh, Canada, the northeastern US, and China), though this is measured as a population-level cognitive/behavioral shift rather than discrete "poisoning" cases.

**For genetic etiology (HMNDYT1/HMNDYT2):**
- **Inheritance pattern:** autosomal recessive for both SLC30A10 and SLC39A14 forms
- **Penetrance:** appears complete for biallelic loss-of-function genotypes, though phenotypic severity varies (incomplete expressivity)
- **Expressivity:** variable — age of onset and severity (presence/absence of polycythemia, cirrhosis, bulbar involvement) vary even among siblings with identical genotypes
- **Genetic anticipation:** not reported/applicable (not a repeat-expansion disorder)
- **Germline mosaicism:** not specifically reported in the literature to date
- **Founder effects:** several recurrent alleles have been reported in specific consanguineous populations (Middle Eastern, South Asian cohorts overrepresented in case series), consistent with founder or recurrent-mutation effects in high-consanguinity populations, though formal founder-haplotype studies are limited
- **Consanguinity:** plays a major role — the majority of reported HMNDYT1/HMNDYT2 families are consanguineous, reflecting the autosomal recessive, rare-allele genetics
- **Carrier frequency:** not established at a population level (too rare/understudied for gnomAD-based carrier frequency estimates to be robust); heterozygous carriers (parents/unaffected sibs in reported families) have normal or mildly elevated blood Mn and are clinically unaffected.

**Population demographics:**
- Occupational manganism disproportionately affects **adult male workers** in mining, welding, and ferroalloy industries, reflecting historical workforce sex distribution rather than biological sex-susceptibility per se.
- Environmental/drinking-water-associated pediatric neurodevelopmental effects have been studied predominantly in **Bangladesh**, **Quebec/Canada**, **Italy**, and parts of the **northeastern United States**, with concentrations studied ranging from <1 µg/L up to >8,600 µg/L in the highest Bangladeshi wells.
- Genetic hypermanganesemia cases have been reported from **Saudi Arabia, Pakistan, Bangladesh, Morocco, and other consanguineous populations**, as well as sporadic cases in Western cohorts.
- Sex ratio for the genetic disorders is not skewed (autosomal recessive, expected 1:1); some pediatric drinking-water cognitive-effect studies report sex-differential associations (effects more evident in one sex depending on cohort and outcome measure — e.g., a Bangladesh cohort reporting cognitive associations more prominent in girls for certain water-Mn exposure windows), but findings are inconsistent across studies and not considered a settled epidemiologic finding.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Whole-blood manganese** — the primary diagnostic biomarker (LOINC-codeable analyte); markedly elevated in genetic disease (often >10-fold normal) and moderately elevated in occupational/iatrogenic exposure. Normal reference range is narrow (roughly 4–15 µg/L depending on lab), making this a sensitive though not perfectly specific marker (levels can also reflect very recent exposure rather than cumulative brain burden).
- **Urinary manganese** — used mainly to document increased excretion during/after chelation therapy rather than as a primary diagnostic test.
- **Hair or toenail manganese** — used in some environmental-epidemiology studies as an integrated longer-term exposure biomarker; less standardized for individual clinical diagnosis.
- **Liver function tests, CBC (for polycythemia)** — relevant in SLC30A10/HMDPC and secondary hepatic manganism.
- **Serum ferritin/iron studies** — relevant given the iron-Mn interaction; iron deficiency should be assessed and corrected as it increases Mn absorption and risk.

**Imaging:**
- **Brain MRI** is the key diagnostic imaging modality: bilateral, symmetric **T1-weighted hyperintensity** in the globus pallidus (and, with more severe disease, striatum, subthalamic nucleus, substantia nigra, dentate nucleus, and anterior pituitary), with corresponding T2 hypointensity or normal T2 signal — reviewed comprehensively in a 2024 narrative review (PMC11122624) that also gives laboratory-testing recommendations to accompany imaging. This pattern helps distinguish manganism from Wilson disease (which typically shows T2 hyperintensity in basal ganglia) and from idiopathic Parkinson disease (typically normal structural MRI).
- MRI T1 signal intensity has been shown to correlate with blood Mn concentration in cirrhotic patients (blood Mn 20.6 ± 10.2 µg/L in cirrhotics vs. 7.2 ± 2.7 µg/L in controls, p=.0013, with T1 hyperintensity score correlating with blood Mn level).
- ¹⁸F-DOPA PET and dopamine transporter (DAT) SPECT imaging are used in the differential diagnosis from idiopathic Parkinson disease: manganism typically shows **normal or near-normal presynaptic dopaminergic imaging**, in contrast to the reduced striatal DAT binding characteristic of idiopathic PD — this is one of the more clinically useful discriminating tests when the diagnosis is uncertain.

**Functional/electrophysiologic tests:** Not disease-specific; standard movement-disorder examination (UPDRS-III) is the primary functional assessment tool used in occupational cohort studies to quantify parkinsonian severity and track progression.

**Genetic testing:**
- Targeted gene sequencing or a movement-disorder/dystonia-parkinsonism gene panel including **SLC30A10** and **SLC39A14** is indicated for early-onset, non-occupational hypermanganesemia, especially in the setting of consanguinity, dystonia, polycythemia, and/or unexplained cirrhosis in infancy/childhood.
- Whole-exome sequencing is reasonable when the phenotype (early-onset dystonia-parkinsonism with elevated blood Mn) is atypical or panel testing is unrevealing.
- Chromosomal microarray, karyotyping, FISH, and mitochondrial DNA testing are **not indicated** — this is a single-gene/biallelic-variant disorder without chromosomal or mitochondrial-genome etiology.

**Clinical diagnostic criteria and differential diagnosis:**
There is no single internationally standardized diagnostic criterion set for occupational manganism analogous to UK Brain Bank criteria for PD; diagnosis relies on a composite of exposure history, characteristic symmetric extrapyramidal exam findings (especially gait and dystonia out of proportion to tremor), elevated blood Mn, characteristic T1-MRI findings, and exclusion of idiopathic Parkinson disease (via DAT imaging/levodopa response) and Wilson disease (via ceruloplasmin, urinary/hepatic copper, and Kayser-Fleischer ring examination). The IRSST (Quebec occupational health institute) expert-panel case-classification criteria have been used in several welder-cohort epidemiologic studies to standardize "probable/possible" case definitions.

**Screening:** No population-based newborn or carrier screening program exists for SLC30A10/SLC39A14 hypermanganesemia (too rare); occupational biological monitoring (periodic blood Mn testing) is used in some high-exposure industries as an exposure-surveillance rather than disease-screening tool.

---

## 11. Outcome / Prognosis

**Survival and mortality:** Manganism itself is not typically directly fatal in adults with occupational disease, though severe genetic pediatric forms (especially untreated SLC39A14 disease) can be associated with substantial morbidity and, in severe bulbar-involved cases, life-threatening complications (aspiration, respiratory compromise). Cirrhosis in SLC30A10/HMDPC carries the mortality risk inherent to any cause of end-stage liver disease if untreated. No large disease-specific mortality registries exist; prognosis data derive from case series rather than population-based survival statistics.

**Morbidity and function:** The dominant morbidity is progressive, often disabling motor impairment (gait disorder, dystonia, dysarthria) leading to occupational disability in adult occupational cases and to loss of independent ambulation in severe untreated pediatric genetic cases. Cognitive/behavioral morbidity (in pediatric environmental exposure) manifests as measurable but generally non-catastrophic IQ and academic-performance deficits at a population level rather than individually disabling cognitive impairment.

**Disease course / complications:**
- **Reversibility is exposure- and stage-dependent**: early psychiatric-phase symptoms and even early motor signs can substantially improve or resolve with removal from exposure and/or chelation; established, longstanding motor deficits (especially dystonia and gait disturbance) tend to be only partially reversible or irreversible once significant basal ganglia neuronal loss has occurred.
- **Complications**: cirrhosis and its sequelae (portal hypertension, hepatic decompensation) in SLC30A10 disease; aspiration pneumonia from bulbar dysfunction in severe pediatric cases; long-term disability and reduced quality of life from residual parkinsonism-dystonia.
- **Prognostic factors**: earlier initiation of chelation/exposure cessation is consistently associated with better outcome across case reports; genotype (truncating vs. missense) may modify severity in the genetic forms, though data are limited; cumulative occupational exposure dose correlates with symptom severity in welder cohorts.
- **Prognostic biomarkers**: degree of blood Mn elevation and extent/severity of T1-MRI basal ganglia hyperintensity are used descriptively to gauge disease burden, though neither has been rigorously validated as a quantitative outcome predictor in prospective studies.

---

## 12. Treatment

**Primary intervention — exposure cessation:** Removal from the source of Mn exposure (occupational reassignment, discontinuation of Mn-containing parenteral nutrition, treatment of underlying liver disease/portosystemic shunting) is the single most important and universally recommended first step, and in early/mild cases may be sufficient for substantial improvement.

**Pharmacotherapy — chelation:**
- **Disodium calcium edetate (CaNa₂EDTA)** — the most widely used chelator for manganism; increases urinary Mn excretion and decreases blood Mn concentration, with variable but sometimes striking clinical improvement, particularly when started early in genetic hypermanganesemia (SLC39A14 and SLC30A10 disease) and in TPN-associated cases. NCIT: chelation therapy generally maps to `NCIT:C15986` (Pharmacotherapy) as the treatment action, with the specific agent captured via `therapeutic_agent` (CHEBI term for edetate calcium disodium).
- **Para-aminosalicylic acid (PAS)** — an alternative/adjunct chelator reported to have particular efficacy in mobilizing brain (as opposed to only peripheral) Mn stores in some case series, based on its ability to cross the blood-brain barrier.
- Chelation is generally more clearly beneficial for **biochemical correction (lowering blood Mn) and, in early disease, functional improvement**, than for reversing established, longstanding structural/neuronal damage — a distinction consistently noted across the case-report literature (StatPearls; genetic-disease case series).
- **Iron supplementation**, when iron deficiency is present, is a rational adjunct given the shared transporter competition between Fe and Mn, though this is supportive/preventive rather than a primary disease-modifying therapy.

**Symptomatic pharmacotherapy:** Levodopa/carbidopa is often trialed given the parkinsonian phenotype but characteristically shows **poor or absent response** in manganism, an important clinical clue supporting the diagnosis over idiopathic PD; some case reports describe partial benefit from other dopaminergic or anti-dystonic agents (e.g., trihexyphenidyl, botulinum toxin for focal dystonia), but evidence is anecdotal.

**Advanced therapeutics:** No gene therapy, cell therapy, RNA-based therapy, or targeted molecular therapy currently exists or is in active clinical development specifically for SLC30A10/SLC39A14 hypermanganesemia; management remains chelation- and exposure-control-based.

**Surgical/interventional:** Liver transplantation has been considered/reported in severe SLC30A10-associated cirrhosis as a treatment for the hepatic component of disease (restoring normal Mn excretory capacity via a genotypically normal liver), analogous in concept to liver transplantation in Wilson disease, though this is reported in isolated cases rather than as a standard-of-care pathway.

**Supportive and rehabilitative care:**
- Physical therapy (NCIT:C15302) and occupational therapy for gait and functional impairment
- Speech/swallowing therapy for dysarthria and bulbar dysfunction in pediatric genetic disease
- Nutritional support/monitoring, especially critical in patients whose original exposure was iatrogenic (PN) — requiring careful re-formulation of PN trace-element content going forward.

**Experimental treatments:** No manganism-specific registered clinical trials were identified as actively recruiting in this research pass; most therapeutic evidence derives from case reports/series rather than randomized controlled trials, reflecting the rarity and heterogeneous etiology of the condition. (A specific NCT-identifier search was not performed as part of this pass; ClinicalTrials.gov should be queried directly — e.g. for "manganese toxicity," "hypermanganesemia," "SLC30A10" — before finalizing a KB entry's `clinical_trials` block.)

**Treatment outcomes:** Response is generally described qualitatively (case-by-case) as "improvement," "partial improvement," or "no significant improvement" following chelation, without pooled response-rate statistics; side effects of EDTA chelation include nephrotoxicity and hypocalcemia risk requiring monitoring during therapy.

**Treatment strategy:** No formal treatment algorithm/clinical practice guideline (e.g., NCCN-style) exists for manganism; management follows an informal stepwise approach: (1) identify and remove the Mn source, (2) confirm diagnosis with blood Mn and MRI, (3) initiate chelation (CaNa₂EDTA ± PAS) particularly in symptomatic or genetically confirmed cases, (4) provide symptomatic/rehabilitative supportive care, (5) consider liver transplantation in end-stage SLC30A10-associated cirrhosis.

---

## 13. Prevention

**Primary prevention:**
- Occupational: engineering controls (local exhaust ventilation, enclosed welding processes), respiratory protective equipment, and adherence to (or advocacy for lowering) permissible exposure limits — current US federal OSHA PEL for manganese compounds/fume is a 5 mg/m³ ceiling limit, while NIOSH recommends a lower REL (1 mg/m³ TWA, 3 mg/m³ STEL) and ACGIH's TLV is substantially lower still (0.02 mg/m³ TWA respirable fraction, 0.1 mg/m³ inhalable), reflecting an active regulatory debate about how protective the older OSHA ceiling limit actually is; ATSDR's chronic inhalation Minimal Risk Level is far lower (0.04 µg/m³), underscoring the gap between regulatory PELs and health-based reference levels.
- Environmental: water treatment/filtration to remove Mn from contaminated drinking-water supplies in affected communities; public health advisories where Mn levels exceed the WHO/EPA secondary (aesthetic) guideline of 50–100 µg/L (note: current drinking-water Mn standards are largely aesthetic/taste-based rather than health-based in many jurisdictions, a recognized policy gap given the neurodevelopmental evidence).
- Iatrogenic: careful formulation and monitoring of trace-element content in parenteral nutrition, with periodic blood Mn monitoring in patients on long-term PN, particularly those with cholestatic liver disease.

**Secondary prevention (screening/early detection):**
- Periodic biological monitoring (blood Mn) for occupationally exposed workers as an early-warning surveillance tool, allowing exposure reduction before clinical disease develops.
- Early neurological/psychiatric symptom screening in high-exposure occupational cohorts.
- For families with a known SLC30A10/SLC39A14 pathogenic variant, genetic counseling and testing of at-risk siblings/relatives to enable pre-symptomatic diagnosis and early chelation initiation, given the strong association between early treatment and better outcome.

**Tertiary prevention:** Ongoing chelation and rehabilitative therapy to limit progression and complications (e.g., preventing aspiration in bulbar-involved pediatric cases; managing cirrhosis complications).

**Genetic counseling:** Recommended for families with confirmed SLC30A10 or SLC39A14 pathogenic variants, particularly given the autosomal recessive inheritance, the treatable nature of early disease, and the value of pre-symptomatic diagnosis in at-risk siblings.

**Public health interventions:** Occupational health surveillance programs in welding/mining/ferroalloy industries; environmental monitoring and remediation of Mn-contaminated groundwater sources; risk communication to affected communities (notably in Bangladesh and parts of North America) regarding drinking-water Mn testing and filtration.

---

## 14. Other Species / Natural Disease

**Taxonomy:** Manganese toxicity/manganism has been studied and, to a lesser extent, occurs naturally across multiple species:
- *Mus musculus* (NCBITaxon:10090) — the dominant model species (see §15)
- *Danio rerio* (NCBITaxon:7955) — zebrafish, increasingly used model
- *Macaca fascicularis*/*Macaca mulatta* (non-human primates) — used in classic inhalational Mn-exposure studies most closely recapitulating human basal ganglia distribution and motor phenotype
- *Rattus norvegicus* (NCBITaxon:10116) — rodent model, particularly for atypical-parkinsonism behavioral/neurochemical studies.

**Naturally occurring disease in other species:** Manganese toxicosis (sometimes with basal-ganglia-type neurological signs) has been reported in livestock and companion animals exposed to contaminated feed, water, or industrial sites, though it is a less thoroughly characterized veterinary entity than, for example, lead or copper toxicosis; OMIA does not carry a well-established naturally occurring hereditary manganism analog in domestic animal breeds akin to human SLC30A10/SLC39A14 disease — this appears to be an evidence gap rather than a documented absence.

**Comparative biology:** SLC30A10 and SLC39A14 orthologs are conserved across vertebrates (including mouse *Slc30a10*/*Slc39a14* and zebrafish *slc30a10*/*slc39a14*), and loss-of-function in the orthologous genes produces convergent Mn-handling and neurotoxicity phenotypes across species, supporting deep evolutionary conservation of the Mn-transport/basal-ganglia-vulnerability mechanism.

**Transmission:** Not applicable — manganism/manganese toxicity is a toxic/genetic condition, not a transmissible or zoonotic disease.

**Suggested NCBITaxon terms:** NCBITaxon:9606 (Homo sapiens), NCBITaxon:10090 (Mus musculus), NCBITaxon:7955 (Danio rerio), NCBITaxon:10116 (Rattus norvegicus), NCBITaxon:9541 (Macaca fascicularis).

---

## 15. Model Organisms

**Mouse models:**
- ***Slc30a10* knockout mice** recapitulate elevated brain Mn levels and neuromotor deficits seen in human HMNDYT1, and have been used for basal-ganglia transcriptomic profiling showing >1,000 differentially expressed genes across sub-regions, enriched for neurotransmission and hypoxia/HIF-pathway genes (Metallomics 2024, PMC10883138).
- **Neuron-specific conditional *Slc30a10* modulation mice** (2024/2025 PNAS study, PMC12890882) — using cell-type-restricted (dopaminergic vs. glutamatergic neuron) genetic manipulation to isolate which basal ganglia neuron populations are cell-autonomously responsible for Mn-induced motor disease; this represents the most mechanistically refined current mouse model.
- A related mouse study links *Slc30a10* loss to **HIF2α-driven polycythemia**, mechanistically modeling the hematologic component of human HMDPC (2023 bioRxiv preprint, subsequently developed further).

**Zebrafish models:**
- ***slc30a10* CRISPR/Cas9 mutant zebrafish lines** develop clinical deficits paralleling the human hereditary manganese metabolism disorder; a PLOS Genetics study additionally identified a **novel compensatory mechanism involving Atp2c1** (a Golgi Ca²⁺/Mn²⁺ ATPase) that partially buffers Mn homeostasis in the *slc30a10*-deficient state — an unexpected genetic-modifier finding with potential relevance to human phenotypic variability.
- ***slc39a14* knockout zebrafish** show **simultaneous manganese hypersensitivity and functional Mn deficiency** — a counterintuitive dual phenotype reflecting the transporter's role in both systemic Mn distribution and cellular Mn delivery; MnCl₂-exposed *slc39a14* mutants show transcriptomic changes mapping to CNS and eye tissue, with **calcium dyshomeostasis and unfolded protein response (UPR) activation** as key molecular signatures, alongside locomotor defects and altered neuronal activity — providing an *in vivo* readout system for genotype-phenotype and therapeutic-modifier screening.

**Non-human primate models:** Chronic inhalational Mn-exposure studies in cynomolgus and rhesus macaques have historically been important for establishing the dose-dependent basal ganglia Mn deposition pattern and motor phenotype most directly homologous to human occupational manganism, given primates' closer basal ganglia anatomy and behavioral repertoire to humans; these studies (largely pre-2020) remain foundational reference points cited in more recent reviews (e.g., Biomolecules 2023) rather than being an area of extensive new primate research in the 2023–2024 window.

**Rat models:** Rat studies (e.g., PLOS ONE 2014, PMC4045849) have characterized **manganese-induced atypical parkinsonism** with altered basal ganglia neuronal activity and changes in tissue monoamine (dopamine, norepinephrine, serotonin) levels, providing a pharmacologically tractable system for studying the neurochemical (as opposed to purely genetic-transporter) route to the manganism phenotype — i.e., modeling the occupational/environmental exposure route rather than the genetic transporter-deficiency route.

**Model characteristics — recapitulation and limitations:**
- Genetic (*Slc30a10*/*slc39a14*) rodent and zebrafish knockout models recapitulate the biochemical hallmark (elevated brain/blood Mn) and much of the motor phenotype robustly, and are considered high-fidelity for the genetic human disease.
- Exposure-based (inhalational/dietary Mn-dosing) rodent and primate models recapitulate the occupational/environmental route of pathogenesis but require careful dose selection, since supraphysiological acute dosing can produce a somewhat different neuropathological pattern than the chronic, lower-level cumulative human occupational exposure pattern — a translational caveat consistently noted in review literature (e.g., the "manganism to manganese-induced parkinsonism" conceptual-model paper explicitly addresses how the human clinical picture has evolved with changing (lower, more chronic) exposure patterns over time, PMID:20012385).
- No single model captures the full human spectrum (psychiatric prodrome + motor disease + hepatic/hematologic features in SLC30A10 disease); the hepatic/hematologic (HIF2α-polycythemia) axis is currently best modeled in mice, the CNS/motor axis is modeled across mice, zebrafish, rats, and historically primates, and human autopsy/neuropathological confirmation remains comparatively sparse across all model systems.

**Resources:** MGI (Mouse Genome Informatics) for *Slc30a10*/*Slc39a14* mouse allele records; ZFIN for zebrafish *slc30a10*/*slc39a14* mutant lines; IMPC/KOMP for systematic knockout mouse phenotyping data potentially relevant to these genes.

---

## Summary Table of Suggested Ontology Bindings

| Category | Suggested term(s) |
|---|---|
| Disease (environmental) | MONDO:0017638 (manganese poisoning) |
| Disease (genetic, HMNDYT1) | MONDO:0013327 / OMIM:613280 |
| Disease (genetic, HMNDYT2) | MONDO:0014982 / OMIM:617013 |
| Causal genes | hgnc:20303 (SLC30A10), hgnc:20860 (SLC39A14), hgnc:20862 (SLC39A8, modifier) |
| Key phenotypes (HP) | HP:0002067 (Bradykinesia), HP:0001288 (Gait disturbance), HP:0001332 (Dystonia), HP:0002063 (Rigidity), HP:0001337 (Tremor), HP:0000338 (Hypomimia), HP:0001260 (Dysarthria), HP:0001402 (Cirrhosis), HP:0001901 (Polycythemia) |
| Exposure (ECTO) | exposure to manganese (search `l~manganese`; route-specific child terms for inhalation/ingestion) |
| Chemical entity (CHEBI) | manganese ion / manganese(II) species (search CHEBI for the specific ionic form cited) |
| Cell types (CL) | CL:0000700 (dopaminergic neuron), CL:0000127 (astrocyte), CL:0000129 (microglial cell), CL:0000182 (hepatocyte) |
| Anatomy (UBERON) | UBERON:0002476 (globus pallidus), UBERON:0002038 (substantia nigra), UBERON:0002087 (subthalamic nucleus) |
| Treatment (NCIT) | NCIT:C15986 (Pharmacotherapy) + therapeutic_agent for edetate calcium disodium (chelator); NCIT:C15302 (Physical Therapy) |

*(All CURIEs above should be independently verified against a live ontology lookup — e.g., OAK/`runoak` — before binding into a curated KB entry; this report is a research lead, not a validated term set.)*

---

## Key Citations

1. Tuschl K, et al. Mutations in SLC39A14 disrupt manganese homeostasis and cause childhood-onset parkinsonism–dystonia. *Nat Commun.* 2016;7:11601. **PMID:27231142**
2. Guilarte TR. From manganism to manganese-induced parkinsonism: a conceptual model based on the evolution of exposure. *NeuroMolecular Med.* 2010. **PMID:20012385**
3. Bouabid S, et al. Manganese neurotoxicity: behavioral disorders associated with dysfunctions in the basal ganglia and neurochemical transmission. *J Neurochem.* 2016. (Wiley/onlinelibrary)
4. Manganese-Induced Parkinsonism: Evidence from Epidemiological and Experimental Studies. *Biomolecules.* 2023;13(8):1190. DOI:10.3390/biom13081190
5. Loss of SLC30A10 manganese transporter alters expression of neurotransmission genes and activates hypoxia-inducible factor signaling in mice. *Metallomics.* 2024. PMC10883138
6. Neuron-specific modulation of SLC30A10 identifies dopaminergic and glutamatergic neurons as targets of manganese-induced motor disease. *PNAS.* 2024/2025. PMC12890882 / **PMID:41628331**
7. Loss of slc39a14 causes simultaneous manganese hypersensitivity and deficiency in zebrafish. PMC9227717
8. Magnetic Resonance Imaging and Manganism: A Narrative Review and Laboratory Recommendations. 2024. PMC11122624
9. Manganese Toxicity. *StatPearls* [Internet]. NCBI Bookshelf: NBK560903 (updated periodically; consult current version).
10. Racette BA, et al. (Washington University welder cohort studies on occupational parkinsonism prevalence; Andruska & Racette, prevalence of parkinsonism 15.6% among 716 welders — exact PMID not confirmed in this research pass; verify via PubMed before citing in a KB entry).
11. Manganese in Drinking Water and Cognitive Abilities and Behavior at 10 Years of Age: A Prospective Cohort Study. **PMID:28564632**
12. Biomarkers of environmental manganese exposure and associations with childhood neurodevelopment: a systematic review and meta-analysis. *Environ Health.* 2020. PMC7531154
13. A novel homozygous SLC39A14 variant in an infant with hypermanganesemia and a review of the literature. PMC9886663
14. Zaki MS, et al. Hypermanganesemia with dystonia, polycythemia and cirrhosis in 10 patients: six novel SLC30A10 mutations and further phenotype delineation. *Clin Genet.* 2018.
15. OMIM #613280 (HMNDYT1) and #617013 (HMNDYT2) entries — omim.org.

**Note on citation confidence:** PMIDs marked as confirmed above were verified against search results in this session. Several foundational papers (the original 2012 Quadri/Tuschl SLC30A10 discovery papers, and the specific Racette prevalence studies) were identified by author/journal/year but their exact PMIDs were not independently re-verified in this pass — confirm via a direct PubMed lookup before using them as citations in a formal knowledge-base entry, consistent with this repository's anti-fabrication policy on ontology and reference identifiers.

Sources:
- [Hypermanganesemia due to mutations in SLC39A14 - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5791243/)
- [Hypermanganesemia with Dystonia, Polycythemia and Cirrhosis (HMDPC) - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0387760416300353)
- [A case of dystonia with polycythemia and hypermanganesemia caused by SLC30A10 mutation - PubMed](https://pubmed.ncbi.nlm.nih.gov/31288771/)
- [A novel homozygous SLC39A14 variant in an infant with hypermanganesemia - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9886663/)
- [Genetic Disorders of Manganese Metabolism - Curr Neurol Neurosci Rep](https://link.springer.com/article/10.1007/s11910-019-0942-y)
- [Manganese-Induced Parkinsonism: Evidence from Epidemiological and Experimental Studies - Biomolecules](https://doi.org/10.3390/biom13081190)
- [Manganese Toxicity - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK560903/)
- [Manganese-Induced Atypical Parkinsonism - PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0098952)
- [From Manganism to Manganese-Induced Parkinsonism - NeuroMolecular Medicine](https://link.springer.com/article/10.1007/s12017-009-8108-8)
- [From manganism to manganese-induced parkinsonism - PubMed](https://pubmed.ncbi.nlm.nih.gov/20012385/)
- [Altered manganese and iron biomarkers in welders - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13310924/)
- [Neurological risks associated with manganese exposure from welding operations - PubMed](https://pubmed.ncbi.nlm.nih.gov/19181573/)
- [Magnetic Resonance Imaging and Manganism: A Narrative Review - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11122624/)
- [Manganese Neurotoxicity as a Complication of Chronic Total Parenteral Nutrition - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7196137/)
- [Brain magnetic resonance imaging and manganese exposure - PubMed](https://pubmed.ncbi.nlm.nih.gov/11130281/)
- [Manganese intoxication during intermittent parenteral nutrition - PubMed](https://pubmed.ncbi.nlm.nih.gov/11284477/)
- [Manganese in Drinking Water and Cognitive Abilities and Behavior at 10 Years of Age - PubMed](https://pubmed.ncbi.nlm.nih.gov/28564632/?dopt=Abstract)
- [Biomarkers of environmental manganese exposure and childhood neurodevelopment - Environmental Health](https://ehjournal.biomedcentral.com/articles/10.1186/s12940-020-00659-x)
- [Manganese Exposure from Drinking Water and Children's Classroom Behavior in Bangladesh - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3230445/)
- [Familial manganese-induced neurotoxicity due to mutations in SLC30A10 or SLC39A14 - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5799044/)
- [SLC30A10 Is a Cell Surface-Localized Manganese Efflux Transporter - J Neuroscience](https://www.jneurosci.org/content/34/42/14079)
- [Hypoxia-inducible factor 2 is a key determinant of manganese excess and polycythemia in SLC30A10 deficiency - bioRxiv](https://www.biorxiv.org/content/10.1101/2023.02.20.529270.full.pdf)
- [Loss of SLC30A10 manganese transporter alters expression of neurotransmission genes - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10883138/)
- [Mutations in SLC39A14 disrupt manganese homeostasis - PubMed](https://pubmed.ncbi.nlm.nih.gov/27231142/)
- [Mutations in SLC39A14 disrupt manganese homeostasis - Nature Communications](https://www.nature.com/articles/ncomms11601)
- [SLC39A14 mutations expand the spectrum of manganese transporter defects - PubMed](https://pubmed.ncbi.nlm.nih.gov/27739105/)
- [OMIM #613280 - HYPERMANGANESEMIA WITH DYSTONIA 1](https://omim.org/entry/613280)
- [OMIM #617013 - HYPERMANGANESEMIA WITH DYSTONIA 2](https://omim.org/entry/617013)
- [Epidemiological Studies of Parkinsonism in Welders](https://ouci.dntb.gov.ua/en/works/4OMnmdr9/)
- [Low levels of manganese in welding fumes linked to neurological problems – WashU Medicine](https://medicine.washu.edu/news/low-levels-manganese-welding-fumes-cause-neurological-problems/)
- [Neuron-specific modulation of SLC30A10 - PNAS](https://www.pnas.org/doi/full/10.1073/pnas.2515785123)
- [Neuron-specific modulation of SLC30A10 - PubMed](https://pubmed.ncbi.nlm.nih.gov/41628331/)
- [Loss of slc39a14 causes simultaneous manganese hypersensitivity and deficiency in zebrafish - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9227717/)
- [Manganese Occupational Exposure Limits - 3M](https://www.3m.com/3M/en_US/worker-health-safety-us/all-stories/full-story-detail/?storyid=f8f24ab7-337b-4224-8ed2-0208deb083b2)
- [Understanding OSHA Manganese Permissible Exposure Levels - RoboVent](https://www.robovent.com/learn/blog/meeting-osha-pels-for-manganese-exposure/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 27 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 56 |
| Resolved | 51 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 4 |
| Terms whose name was checked | 33 |
| Terms named correctly | 20 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013327` (3 mentions) - the report calls it "HMNDYT1"; MONDO calls it **primary hyperoxaluria type 3**
- `CHEBI:29486` (1 mention) - the report calls it "manganese atom"; CHEBI calls it **4-Benzyloxybenzyl alcohol**
- `HP:0000723` (1 mention) - the report calls it "Personality changes"; HP calls it **Restrictive behavior**
- `HP:0001402` (2 mentions) - the report calls it "Cirrhosis"; HP calls it **Hepatocellular carcinoma**
- `GO:0071573` (1 mention) - the report calls it "metal ion transmembrane transport — search for the manganese-specific child term"; GO calls it **shelterin complex assembly**
- `CL:0000030` (1 mention) - the report calls it "glial cell"; CL calls it **glioblast**
- `UBERON:0002087` (2 mentions) - the report calls it "Subthalamic nucleus"; UBERON calls it **atrioventricular canal**
- `UBERON:0002319` (1 mention) - the report calls it "Anterior pituitary"; UBERON calls it **mesangium**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006542` (obsolete glutamine biosynthetic process) (1 mention) - replaced by `GO:1901704`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0014982` (3 mentions) - the report calls it "HMNDYT2"; MONDO calls it **myopia 25, autosomal dominant**, and lists "MYP25" among its other names
- `GO:0005385` (1 mention) - the report calls it "zinc ion transmembrane transporter activity, related family"; GO calls it **zinc ion transmembrane transporter activity**
- `GO:0006826` (1 mention) - the report calls it "iron ion transport, related transporter family context"; GO calls it **iron ion transport**
- `GO:0006542` (1 mention) - the report calls it "glutamine biosynthetic process, glutamine synthetase-relevant"; GO calls it **obsolete glutamine biosynthetic process**
- `UBERON:0002476` (2 mentions) - the report calls it "Globus pallidus"; UBERON calls it **lateral globus pallidus**, and lists "globus pallidus (rat)" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`.