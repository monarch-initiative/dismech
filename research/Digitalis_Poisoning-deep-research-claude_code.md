---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-19T21:58:55.371806'
end_time: '2026-09-19T22:04:51.213671'
duration_seconds: 355.84
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Digitalis Poisoning
  mondo_id: MONDO:0017863
  category: Complex
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
  web_search_requests: 26
  num_turns: 27
  total_cost_usd: 1.755113
  session_id: dc83c613-1fba-53b8-9741-f63fb2448a6e
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 70
reference_validation:
  total_references: 35
  verified: 34
  not_found: 0
  unverifiable: 1
  confabulation_rate: 0.0
  relevance_assessed: 34
  on_topic: 11
  off_topic: 1
  off_topic_references:
  - PMID:40660117
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 41
  verified: 40
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 32
  labels_matching: 17
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0017863
    reported_labels:
    - digitalis poisoning
    - acquired/toxicologic disease entry
    ontology_label: digitalis poisoning
  - term_id: HP:0000496
    reported_labels:
    - Halo vision
    ontology_label: Abnormality of eye movement
  - term_id: HP:0011703
    reported_labels:
    - Atrioventricular block
    ontology_label: Sinus tachycardia
  - term_id: HP:0001700
    reported_labels:
    - 'parent: Cardiac arrhythmia'
    ontology_label: Myocardial necrosis
  - term_id: UBERON:0002205
    reported_labels:
    - AV node
    ontology_label: manubrium of sternum
  - term_id: UBERON:0002136
    reported_labels:
    - Purkinje fiber cell tissue
    ontology_label: hilus of dentate gyrus
  labels_variant: 9
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Digitalis Poisoning
- **MONDO ID:** MONDO:0017863 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Digitalis Poisoning** covering all of the
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

# Digitalis (Digoxin/Cardiac Glycoside) Poisoning — Comprehensive Research Report

## 1. Disease Information

**Overview.** Digitalis poisoning (digoxin toxicity, cardiac glycoside toxicity) is a potentially life-threatening intoxication produced by excessive exposure to digoxin or related cardiac glycosides (digitoxin, oleandrin, bufalin/bufadienolides, ouabain). It results from Na⁺/K⁺-ATPase pump inhibition and manifests as a triad of gastrointestinal, neurologic/visual, and cardiac-conduction disturbances, the last being the dominant cause of morbidity and mortality ([StatPearls NBK459165](https://www.ncbi.nlm.nih.gov/books/NBK459165/); [Medscape](https://emedicine.medscape.com/article/154336-overview)). Toxicity is classically divided into **acute** (single large ingestion, often suicidal or accidental, in a previously non-exposed person), **acute-on-chronic** (an extra dose/overdose superimposed on chronic therapy), and **chronic** (gradual accumulation from impaired clearance, drug interactions, or dose creep in a patient already on maintenance therapy) — these three patterns differ substantially in electrolyte pattern (hyperkalemia is typically an **acute**-poisoning finding; chronic toxicity does not usually cause hyperkalemia) and prognosis ([LITFL Digoxin Toxicity](https://litfl.com/digoxin-toxicity-ccc/); [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK459165/)).

**Key identifiers**
| System | ID |
|---|---|
| MONDO | MONDO:0017863 ("digitalis poisoning") ([Wikidata Q151350](https://www.wikidata.org/wiki/Q151350); [NORD/Mondo mirror](https://rarediseases.org/mondo-disease/digitalis-poisoning/)) |
| MeSH | "Digoxin" (D004077); toxicity subheading; related "Cardiac Glycosides/poisoning" |
| ATC | C01AA05 (digoxin, cardiac glycoside class C01A); V03AB24 (digoxin immune Fab antidote) |
| ChEBI | CHEBI:4551 (digoxin) — cardenolide glycoside from *Digitalis lanata*, a steroid nucleus + unsaturated lactone ring + trisaccharide ([ChEBI](https://www.ebi.ac.uk/chebi/CHEBI:4551)) |
| PubChem CID | 2724385 (digoxin, C₄₁H₆₄O₁₄) ([PubChem](https://pubchem.ncbi.nlm.nih.gov/compound/2724385)) |
| ICD-10-CM | T46.0X1– (poisoning by cardiac-stimulant glycosides, accidental), with intent-based 5th/6th character extensions |

**Synonyms/alternative names:** digoxin toxicity, digitalis intoxication, cardiac glycoside toxicity/poisoning, digitalis glycoside overdose; plant-source variants are named for the source (oleander/yellow oleander poisoning, foxglove poisoning, toad-venom/bufadienolide poisoning).

**Nature of source data.** Because this is a toxidrome rather than a Mendelian or classically epidemiologic disease, most of the evidence base is: (a) aggregated case series and poison-control/registry data (individual case reports contribute mechanistic and phenotype detail but are not population-representative); (b) the large RCT evidence base for therapeutic digoxin use in heart failure/atrial fibrillation (the DIG trial and its post-hoc analyses), which is the source of dose–toxicity relationship data; and (c) basic-science/model-organism electrophysiology studies establishing mechanism. There is essentially no disease-specific EHR-derived cohort literature distinct from these three streams.

---

## 2. Etiology

### Disease causal factor
Digitalis poisoning is fundamentally a **pharmacologic/toxicologic** disease, not a genetic one: it is caused by supratherapeutic tissue concentrations of a cardiac glycoside, reaching a level at which Na⁺/K⁺-ATPase inhibition exceeds the myocardium's compensatory capacity ("mechanistic" causal factor). There is no single-gene or chromosomal cause of the disease itself; genetic contributions are limited to **pharmacokinetic/pharmacogenomic modifiers** of individual susceptibility (below).

### Risk factors

**Environmental / iatrogenic / mechanistic:**
- **Narrow therapeutic index.** Therapeutic total digoxin is 0.8–2.0 ng/mL (older target) or, per contemporary heart-failure guidance, 0.5–1.0 ng/mL (lower is now preferred because higher levels raise morbidity/mortality without added benefit); toxicity is generally associated with levels >2.4 ng/mL, but **~10% of toxic patients have levels below 2 ng/mL**, especially with hypokalemia, hypomagnesemia, hypoxia, or hypercalcemia ([PMC10350506](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10350506/); [StatPearls NBK459165](https://www.ncbi.nlm.nih.gov/books/NBK459165/)).
- **Renal impairment** — the leading cause of *chronic* toxicity; ~50–70% of a digoxin dose is excreted unchanged by the kidney, closely tracking GFR, so renal decline (common with age) markedly prolongs half-life (1.5–2.0 days with normal renal function → 3.5–5 days in anuric patients) ([Clinical Pharmacokinetics of Digoxin, PMID:322907](https://pubmed.ncbi.nlm.nih.gov/322907/); [StatPearls NBK556025](https://www.ncbi.nlm.nih.gov/books/NBK556025/)).
- **Electrolyte disturbance**: hypokalemia and hypomagnesemia (digoxin competes with K⁺ at the ATPase binding site, so low K⁺ increases glycoside binding/effect), hypercalcemia (potentiates the arrhythmogenic Ca²⁺-overload mechanism), hypoxemia, acid–base disturbance.
- **Drug–drug interactions**: >100–400 reported interacting drugs; the clinically dominant mechanism is inhibition of P-glycoprotein (ABCB1)-mediated renal/biliary clearance and reduced volume of distribution — amiodarone, verapamil, quinidine, macrolides (clarithromycin, erythromycin), itraconazole, cyclosporine — each of which can roughly double serum digoxin concentration ([StatPearls NBK459165](https://www.ncbi.nlm.nih.gov/books/NBK459165/); [uspharmacist.com](https://www.uspharmacist.com/article/digoxin-toxicity-a-review)).
- **Age and sex**: advanced age (renal decline, lower muscle mass → smaller volume of distribution, polypharmacy) and female sex are independently associated with higher toxicity risk and, in post-mortem genotyping series, greater lethality for a given exposure ([PMID:21311904](https://pubmed.ncbi.nlm.nih.gov/21311904/)).
- **Plant/zootoxin exposure** (non-iatrogenic route): ingestion of foxglove (*Digitalis purpurea*/*lanata*), oleander (*Nerium oleander*), yellow oleander (*Thevetia peruviana*), lily-of-the-valley (*Convallaria majalis*), or toad-derived bufadienolide preparations produces an identical clinical/ECG toxidrome via the same Na⁺/K⁺-ATPase mechanism ([PMC3721620](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3721620/); [PMC7472096](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7472096/)).
- **Intentional self-poisoning** is a major global route, dominated in South/Southeast Asia by yellow oleander seed ingestion (see §9 Epidemiology).

**Genetic risk/modifier factors (pharmacogenomic, not causal):**
- **ABCB1 (MDR1, P-glycoprotein, HGNC gene ABCB1)** polymorphisms (notably 2677G>T/A and 3435C>T) modestly alter digoxin serum concentration via effects on P-gp–mediated intestinal absorption and renal/biliary excretion; results across studies are mixed — several show no clinically meaningful pharmacokinetic effect ([PMID:12492608](https://pubmed.ncbi.nlm.nih.gov/12492608/)), while others link variant ABCB1 alleles to increased sudden-cardiac-death risk in digoxin users and to sex-differential post-mortem toxicity ([PMID:26531821](https://pubmed.ncbi.nlm.nih.gov/26531821/); [PMID:21311904 "Post-mortem ABCB1 genotyping reveals an elevated toxicity for female digoxin users"](https://pubmed.ncbi.nlm.nih.gov/21311904/); [PMID:28208135](https://pubmed.ncbi.nlm.nih.gov/28208135/); review [PMID: Clin Pharmacokinet 2016](https://link.springer.com/article/10.1007/s40262-015-0267-1)).
- **SLCO1B3** (organic anion transporter) variants have also been examined as modifiers of digoxin disposition alongside ABCB1 in the Tunisian AF cohort study above.
- There is **no known primary Mendelian causal gene** for digitalis poisoning; it is not a heritable disease.

**Protective factors:**
- No genetic protective variant is described specifically against digitalis poisoning (unlike, e.g., predator/herbivore cardiac-glycoside-resistance alleles in other species — see §14).
- **Environmental/clinical protective factors**: routine therapeutic drug monitoring, dose reduction with declining renal function, avoidance of known P-gp inhibitors, potassium/magnesium repletion, and (in the modern heart-failure era) preference for lower target concentrations (0.5–0.8 ng/mL) have reduced population-level toxicity incidence ([StatPearls NBK459165](https://www.ncbi.nlm.nih.gov/books/NBK459165/)).

**Gene–environment interaction:** The clearest G×E pattern is genotype (ABCB1)–drug interaction: a P-gp inhibitor (environmental exposure) produces a larger rise in serum digoxin in a patient whose ABCB1 genotype already confers reduced transporter efficiency, and this combination is proposed to explain some of the sex-based differences in fatal toxicity reported in post-mortem series ([PMID:21311904](https://pubmed.ncbi.nlm.nih.gov/21311904/)).

---

## 3. Phenotypes

Digitalis poisoning presents with a fairly stereotyped triad. Frequencies below are drawn from case-series/registry literature; most are qualitative ("common," "most common") rather than precisely quantified in a single denominator study.

| Phenotype | Type | HPO suggestion | Onset/course | Notes |
|---|---|---|---|---|
| Nausea and vomiting | Symptom (GI) | HP:0002018 (Nausea and vomiting); HP:0002017 (Nausea) | Earliest sign in both acute and chronic toxicity | Often the presenting complaint; anorexia frequently precedes it |
| Anorexia | Symptom | HP:0002039 (Anorexia) | Early | — |
| Abdominal pain | Symptom | HP:0002027 (Abdominal pain) | Variable | — |
| Diarrhea | Symptom | HP:0002014 (Diarrhea) | Variable | Less prominent than nausea/vomiting |
| Xanthopsia / chromatopsia (yellow-tinged vision) | Symptom (visual) | HP:0025590 or closest available "abnormality of color vision" term; no exact HPO term for xanthopsia exists — consider free text with SNOMED CT grounding | Chronic toxicity predominant | Classically described as "Van Gogh's yellow" vision; near-pathognomonic |
| Halo vision / photopsia / scotoma | Symptom (visual) | HP:0000496 (Halo vision) | Chronic toxicity | — |
| Diminished visual acuity | Sign | HP:0000505 (Visual impairment) | Chronic | — |
| Headache | Symptom | HP:0002315 (Headache) | Variable | — |
| Confusion / altered mental status | Symptom | HP:0001289 (Confusion) | More prominent in elderly/chronic toxicity | — |
| Malaise / weakness | Symptom | HP:0033834 (Fatigue) / HP:0001324 (weakness) | Variable | — |
| Insomnia | Symptom | HP:0100785 (Insomnia) | Variable | — |
| Premature ventricular complexes | Lab/ECG sign | Not HPO-mapped directly; consider EKG-specific ontologies (LOINC/SNOMED) | Cardiac | Most common dysrhythmia in digoxin toxicity |
| AV nodal (junctional) block, varying degree | ECG/clinical sign | HP:0011703 (Atrioventricular block) | Cardiac; 30–40% of toxic cases | "AV junctional blocks... are the most common manifestations of digoxin toxicity, occurring in 30-40% of cases" ([Medscape/StatPearls synthesis](https://emedicine.medscape.com/article/154336-overview)) |
| Bidirectional ventricular tachycardia | ECG sign | HP:0004756 (Ventricular tachycardia) as parent term | Cardiac | Near pathognomonic for digoxin toxicity — alternating QRS axis beat-to-beat ([LITFL](https://litfl.com/digoxin-effect-ecg-library/)) |
| Atrial tachycardia with block (esp. 2:1 AV block) | ECG sign | HP:0001700 (parent: Cardiac arrhythmia) | Cardiac | Classic pattern |
| Sinus bradycardia | Sign | HP:0001662 (Sinus bradycardia) | Cardiac | Vagotonic effect |
| Hyperkalemia | Lab abnormality | HP:0002153 (Hyperkalemia) | **Acute** poisoning predominant; usually absent in chronic toxicity | Strong severity/mortality marker (see §11) |
| "Scooped"/sagging ST depression, T-wave flattening/inversion, short QT, prominent U wave, PR prolongation | ECG (lab) finding | — (ECG morphology, not an HPO phenotype per se) | Chronic "digitalis effect," not toxicity per se | Reflects therapeutic exposure, distinct from toxic arrhythmia |

**Severity/progression:** Acute poisoning tends to be more abrupt and life-threatening (vomiting, hyperkalemia, brady-/tachyarrhythmias progressing rapidly to hemodynamic collapse), whereas chronic toxicity is insidious, dominated by GI/CNS/visual symptoms with bradyarrhythmia and increased automaticity evolving over days ([LITFL](https://litfl.com/digoxin-poisoning/)). Nearly any arrhythmia can occur — "almost any type of arrhythmia has been reported," making digoxin toxicity a classic diagnostic mimicker ([Healio](https://www.healio.com/cardiology/learn-the-heart/cardiology-review/topic-reviews/digoxin-toxicity)).

**Quality-of-life impact:** Not separately studied with EQ-5D/SF-36 instruments for the acute poisoning entity (as opposed to chronic digoxin-treated heart failure, where instrument data exist but reflect the underlying heart failure rather than glycoside toxicity itself). This is a data gap.

---

## 4. Genetic/Molecular Information

Digitalis poisoning is **not a monogenic disease** — there is no OMIM causal-gene entry, no ClinVar pathogenic-variant catalog, and no chromosomal-abnormality association analogous to a Mendelian disorder. The molecular information relevant to this entry is instead:

1. **The molecular target**: Na⁺/K⁺-ATPase (sodium pump), specifically the α-subunit's extracellular cardiac-glycoside binding pocket. In humans this is encoded chiefly by **ATP1A1** (HGNC:799, the ubiquitously expressed catalytic α1 isoform, the principal cardiac isoform relevant to glycoside binding) and **ATP1A2/ATP1A3** in other tissues. Digoxin binds a highly conserved extracellular pocket involving residues homologous to Q111, N122, F786, and T797 across species ([eLife 48224](https://elifesciences.org/articles/48224.pdf); [PMID:8385116](https://pubmed.ncbi.nlm.nih.gov/8385116/)).
2. **Pharmacogenomic modifier genes** — ABCB1 (P-glycoprotein) and SLCO1B3 (organic-anion transporter), discussed in §2, which alter systemic exposure but do not cause the disease.
3. **Endogenous digoxin-like immunoreactive substances (DLIS/"endobain"/"endoxin")** — an important *molecular confounder* rather than a causal factor: uncharacterized endogenous Na⁺/K⁺-ATPase-inhibiting factors cross-react with anti-digoxin immunoassays and are elevated in renal failure, liver failure, pregnancy, and especially **neonates** (with an inverse relationship to gestational/postnatal age and possibly linked to bilirubin level), producing falsely elevated "digoxin" levels in patients who have never taken the drug ([Ann Intern Med, DOI:10.7326/0003-4819-99-5-604](https://doi.org/10.7326/0003-4819-99-5-604); [Acta Paediatrica DLIS neonates](https://onlinelibrary.wiley.com/doi/10.1111/j.1651-2227.1989.tb11093.x); [Eur J Pediatr](https://link.springer.com/article/10.1007/BF02343220)). "As long as the chemical structure, origin and physiological properties of DLIS remain unknown, clinicians must be cautious in interpreting the serum levels of digoxin."
4. **Somatic/epigenetic/chromosomal information**: not applicable — no evidence of epigenetic dysregulation or chromosomal abnormality contributing to susceptibility beyond the pharmacogenomic SNP-level effects above.

Ontology note for a KB entry: since there is no causal Mendelian gene, `genetic:` entries (if used at all) should be scoped as **modifier/susceptibility** relationships (ABCB1, SLCO1B3) rather than causal, and the molecular target (ATP1A1, GO:0005391 sodium:potassium-exchanging ATPase activity) belongs in `pathophysiology` as the affected molecular function, not in a causal `genetic:` block.

---

## 5. Environmental Information

- **Iatrogenic/pharmaceutical exposure**: digoxin prescribed for heart failure or atrial fibrillation rate control is the dominant real-world exposure route in high-income settings.
- **Toxins/plants** (the classic "digitalis" exposure route and origin of the disease name): *Digitalis purpurea* and *D. lanata* (foxglove — original glycoside source), *Nerium oleander* (oleander) and *Thevetia peruviana* (yellow oleander), *Convallaria majalis* (lily of the valley), *Kalanchoe* spp., and toad venom (bufadienolides, e.g., from *Bufo* species used in some traditional Chinese medicines) — all inhibit the same Na⁺/K⁺-ATPase target and produce a clinically indistinguishable toxidrome ([PMC3721620 Cardiotoxicity of plants in South Africa](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3721620/); [VETgirl](https://vetgirlontherun.com/cardiac-glycoside-plants-poisonous-to-dogs-and-cats/); StatPearls, bufalin/toad section).
- **Occupational/accidental exposure**: pediatric accidental ingestion of ornamental plants or grandparents' medications; livestock grazing on oleander (documented outbreak in dairy cattle with food-safety implications for milk/meat, [PMC7472096](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7472096/); [PMC6723884 fatal cattle case](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6723884/)).
- **Lifestyle factors**: none specific to the causal mechanism; comorbid heart failure/AF (which drive prescription) are lifestyle-modifiable but the toxicity itself is dose/clearance-driven, not lifestyle-driven, apart from alcohol/renal-toxin exposures that worsen renal clearance.
- **Infectious agents**: not applicable — this is not an infectious disease.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Excess systemic exposure** to a cardiac glycoside (supratherapeutic dose, impaired renal clearance, P-gp–inhibiting drug interaction, or ingestion of a glycoside-containing plant/toad product) **leads to** cardiac-glycoside tissue concentrations that exceed the therapeutic window.
2. Digoxin **binds** the extracellular K⁺-binding site of the **Na⁺/K⁺-ATPase (Na,K-ATPase; sodium pump)** α-subunit on the cardiomyocyte sarcolemma, **which inhibits** the enzyme's Na⁺-extrusion/K⁺-uptake activity in a manner that is competitively worsened by hypokalemia (digoxin and K⁺ compete for the same site) ([StatPearls; PMID:322907; Deranged Physiology](https://derangedphysiology.com/main/cicm-primary-exam/cardiovascular-system/Chapter-968/digoxin)).
3. Na,K-ATPase inhibition **causes** a rise in intracellular Na⁺ concentration, **which** collapses the transmembrane Na⁺ gradient that the Na⁺/Ca²⁺ exchanger (NCX1) normally uses to extrude Ca²⁺.
4. Reduced Ca²⁺ extrusion via NCX1 **leads to** intracellular (and, specifically, sarcoplasmic-reticulum) Ca²⁺ accumulation — "**calcium overload**." (At therapeutic concentrations this same step, more modestly engaged, is the basis of digoxin's positive inotropic effect; recent work shows the mechanism critically depends on a specific allosteric state of NCX1 called Na⁺-dependent inactivation — [Science Advances, sciadv.ady9596](https://www.science.org/doi/10.1126/sciadv.ady9596).)
5. At toxic (but not therapeutic) degrees of Na,K-ATPase inhibition, SR Ca²⁺ overload **exceeds** the SR's sequestering capacity, **causing** spontaneous, oscillatory Ca²⁺ release from the SR after normal repolarization.
6. Spontaneous Ca²⁺ release **activates** the electrogenic 3Na⁺/1Ca²⁺ exchanger in the Ca²⁺-extrusion direction, **generating** a net inward (depolarizing) current during phase 4 — a **delayed afterdepolarization (DAD)** ([PMC5446409](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5446409/); [PMC5597635 erratum](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5597635/)).
7. If the DAD reaches threshold, it **triggers** spontaneous, non-driven action potentials (**triggered automaticity/aftercontractions**), which **manifest as** ectopic beats and, when they arise from independent foci with alternating exit pathways through the ventricular conduction system, produce the near-pathognomonic **bidirectional ventricular tachycardia**, as well as PVCs, accelerated junctional rhythms, and atrial tachycardia with block.
8. In parallel, digoxin **increases vagal (parasympathetic) tone** and **enhances central sympathetic outflow / inhibits norepinephrine reuptake at adrenergic terminals**, which **branches to** two further effects: (a) increased vagal tone **slows** SA-node discharge and **prolongs** AV-nodal conduction/refractoriness, **producing** sinus bradycardia and AV block (the basis of the classic "increased automaticity + decreased conduction" toxidrome description); (b) enhanced sympathetic tone **contributes to** the ectopic/triggered-automaticity burden above.
9. Independently, Na,K-ATPase inhibition **causes** a shift of intracellular K⁺ into the extracellular space, **producing hyperkalemia** — this branch is most evident in **acute** massive ingestion (where the sudden, large-magnitude pump inhibition rapidly redistributes total-body K⁺) and is typically **absent** in slowly accumulating chronic toxicity ([StatPearls; LITFL](https://litfl.com/digoxin-poisoning/)). Serum K⁺ is therefore both a **downstream biomarker** of pump-inhibition severity and, empirically, the single best **prognostic marker** in acute poisoning (§11).
10. The combined arrhythmia burden (bradyarrhythmia, AV block, and/or ventricular tachyarrhythmia) **culminates in** hemodynamic instability, and, when untreated or severe, **cardiac arrest/death** — the proximate cause of most digitalis-poisoning mortality.
11. A separate, less-defined branch: digoxin's Na,K-ATPase inhibition in the **area postrema/CNS** and GI tract **contributes to** the nausea/vomiting and the visual-pathway effects (color-vision disturbance, xanthopsia), inferred rather than fully mechanistically demonstrated at the retinal/cortical level in humans; retinal Na,K-ATPase inhibition affecting photoreceptor signal processing is the leading hypothesis but retinal-level human mechanistic data are limited (inferred step).

### Category detail

- **Molecular pathway/function**: GO:0005391 (P-type Na⁺/K⁺-exchanging ATPase activity, sodium/potassium-transporting ATPase complex) inhibition is the initiating molecular lesion; downstream engagement of the Na⁺/Ca²⁺ exchanger (NCX1, gene *SLC8A1*) and SR Ca²⁺-handling machinery (SERCA2a/*ATP2A2*, ryanodine receptor RyR2) is the amplifying pathway.
- **Cellular process**: GO:0086036 (regulation of cardiac muscle cell membrane potential), GO:0086013 (membrane repolarization in ventricular cardiac muscle cell), and triggered-automaticity/afterdepolarization processes; increased cardiomyocyte contractility (positive inotropy at sub-toxic levels) versus disordered automaticity at toxic levels.
- **Protein dysfunction**: not a structural protein-misfolding disease — the "dysfunction" is pharmacologic inhibition of a normally functioning enzyme (Na,K-ATPase), not a mutant/misfolded protein.
- **Metabolic/biochemical**: net cellular ion-homeostasis derangement (↑ intracellular Na⁺, ↑ intracellular Ca²⁺, ↑ extracellular K⁺); no primary energy-metabolism or lipid-metabolism lesion.
- **Immune involvement**: none intrinsic to the toxicity; immune mechanisms are only relevant to the **antidote** (ovine anti-digoxin Fab fragments) and to rare Fab-associated serum-sickness/anaphylaxis reactions.
- **Tissue damage mechanisms**: primarily electrophysiologic/functional (arrhythmia) rather than structural cell death; myocardial injury markers are not classically part of the toxidrome (unlike ischemic injury).
- **Cell types involved**: cardiomyocyte (CL:0000746, cardiac muscle myoblast/cardiac muscle cell), cardiac Purkinje fiber cell/cardiac conduction system cells, SA-node and AV-node pacemaker cells, and (for the extracardiac symptoms) enteric/vagal afferent neurons and retinal photoreceptor/bipolar cells (visual symptoms).
- **Molecular profiling / advanced technologies**: no transcriptomic, proteomic, single-cell, or spatial-omics signature is established for this toxidrome in humans — mechanistic knowledge derives almost entirely from classical electrophysiology (voltage-clamp, sharp-electrode recording in isolated Purkinje fibers and whole-heart preparations), not omics.

**Suggested GO terms**: GO:0005391 (Na⁺/K⁺-ATPase activity), GO:0086036 (cardiac membrane potential regulation), GO:0060402 (calcium ion transport into cytosol via sarcoplasmic reticulum), GO:0086016 (AV node cell action potential).
**Suggested CL terms**: CL:0000746 (cardiac muscle cell), CL:1000497 (Purkinje myocyte), CL:0002129 (cardiac pacemaker cell).

---

## 7. Anatomical Structures Affected

- **Organ level**: heart (primary organ); secondary/systemic effects on GI tract (nausea/vomiting), CNS (confusion, headache), and visual system (retina/optic pathway — xanthopsia, halos).
- **Body systems**: cardiovascular system (primary), digestive system, nervous system (CNS and autonomic/vagal), visual system.
- **Tissue/cell level**: the cardiac **conduction system** specifically — SA node, AV node, His-Purkinje fibers — plus ventricular and atrial myocardium generally. UBERON suggestions: UBERON:0002018 (SA node), UBERON:0002205 (AV node), UBERON:0002136 (Purkinje fiber cell tissue), UBERON:0000948 (heart).
- **Subcellular level**: sarcolemma (site of Na,K-ATPase inhibition; GO cellular component GO:0005890 Na⁺/K⁺-ATPase complex), sarcoplasmic reticulum (Ca²⁺ overload site, GO:0033017 sarcoplasmic reticulum membrane), mitochondria (secondary Ca²⁺ handling, not primary).
- **Localization**: diffuse/systemic rather than focal; no lateralization applicable (bilateral/systemic toxicity).

---

## 8. Temporal Development

- **Onset**: any age; timing depends on exposure route. Acute ingestion → symptom onset typically within hours (GI symptoms first, cardiac effects following the ~6–8-hour distribution phase). Chronic toxicity develops insidiously over days to weeks as clearance declines or dose/interacting drugs accumulate.
- **Progression/stages**: pre-symptomatic supratherapeutic level → GI prodrome → neurologic/visual symptoms (chronic pattern) → cardiac conduction/arrhythmia phase → (if untreated) hemodynamic collapse/cardiac arrest.
- **Course pattern**: acute poisoning is typically a self-limited event (resolves with elimination/antidote) unless fatal; chronic toxicity may recur if the precipitating renal/drug-interaction/dosing problem is not corrected.
- **Critical period for intervention**: the first ~1 hour post-acute-ingestion is the window for GI decontamination (activated charcoal); the diagnostic/therapeutic window for digoxin-specific antibody (Fab) therapy is essentially the entire symptomatic period, since Fab does not depend on the same narrow timing constraint as charcoal ([StatPearls NBK459165](https://www.ncbi.nlm.nih.gov/books/NBK459165/); [RebelEM](https://rebelem.com/management-of-digoxin-toxicity/)).
- **Remission**: recovery typically follows drug clearance/discontinuation and, when indicated, Fab administration; recurrence is possible if the underlying cause (renal failure, ongoing interacting drug) persists.

---

## 9. Inheritance and Population

**Inheritance**: not applicable — digitalis poisoning is an acquired toxicologic disease, not a Mendelian condition. No inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder-effect, or carrier-frequency concept applies to the disease itself (only to the minor ABCB1/SLCO1B3 pharmacogenomic modifiers described in §4).

**Epidemiology**:
- **United States**: an estimated **~8,000 hospital visits annually** for digitalis toxicity; in 2011 the US Poison Control system recorded **2,513 cases**, of which **27 resulted in death** ([Medscape/StatPearls synthesis](https://emedicine.medscape.com/article/154336-overview)).
- **Age-stratified ED burden**: digoxin toxicity accounted for **~1% of adverse-drug-event ED visits** in patients ≥40 years, rising to **3.3%** in patients ≥85 years, and **5.9% of adverse-drug-event hospitalizations** in patients ≥85 years; ED admissions for digoxin toxicity were **3.5-fold greater** in patients >85 years than in a younger comparison cohort ([CDC report](https://stacks.cdc.gov/view/cdc/37152/cdc_37152_DS1.pdf)).
- **Historical elderly-specific series**: up to **a quarter of all drug poisonings** in elderly cohorts have historically been attributed to digitalis toxicity in some series ([ScienceDirect PMID:073567579190161C](https://www.sciencedirect.com/science/article/abs/pii/073567579190161C)).
- **Prescribing trend**: digoxin use in heart failure has declined substantially (to roughly ~8% of HF patients started on it at discharge in recent practice), which has correspondingly reduced toxicity incidence over the past decade ([StatPearls NBK459165](https://www.ncbi.nlm.nih.gov/books/NBK459165/)).
- **Global/plant-poisoning burden**: Yellow oleander (*Thevetia peruviana*) seed self-poisoning is a major cause of digitalis-like toxicity in South Asia, with **"thousands of cases each year"** in northern Sri Lanka alone, and an estimated **tens of thousands of cases and probably thousands of deaths per year across South Asia**; in some Sri Lankan regions up to **40% of self-poisoning cases** are oleander-related, with annual incidence >150/100,000 in affected districts, disproportionately affecting adolescents/young adults; overall **mortality ~10%** in Sri Lankan series, and oleander plus paraquat together caused 74% of poisoning deaths in patients <25 years old ([Trop Med Int Health 1999](https://onlinelibrary.wiley.com/doi/abs/10.1046/j.1365-3156.1999.00397.x); [PMID:16319413](https://pubmed.ncbi.nlm.nih.gov/16319413/); [Sci Total Environ review, ScienceDirect 0379073888901508](https://www.sciencedirect.com/science/article/abs/pii/0379073888901508)).
- **Sex distribution**: females are disproportionately represented in ED visits for digoxin toxicity relative to outpatient prescription frequency ([CDC report](https://stacks.cdc.gov/view/cdc/37152/cdc_37152_DS1.pdf)); in the Sri Lankan oleander series, **61% of admitted cases were women**, and **46% were <21 years old** ([oleander case series](https://www.sciencedirect.com/science/article/abs/pii/0379073888901508)).
- **Geographic distribution**: iatrogenic digoxin toxicity is globally distributed wherever digoxin is prescribed (highest absolute case counts in older, higher-income populations with heart failure/AF); plant-glycoside poisoning is concentrated in regions where the causative plants grow and are used for self-harm (South Asia for yellow oleander; parts of Africa for other cardiotoxic plants — [PMC3721620](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3721620/)).

---

## 10. Diagnostics

**Laboratory tests**
- **Serum digoxin concentration**: therapeutic 0.8–2.0 ng/mL (older range) / 0.5–1.0 ng/mL (contemporary HF target); toxic threshold >2.4 ng/mL, but diagnosis is **clinical**, since levels do not reliably correlate with toxicity — deaths have occurred within the "therapeutic" range, and atrial-fibrillation patients show increased mortality risk even at >1.2 ng/mL ([StatPearls NBK459165](https://www.ncbi.nlm.nih.gov/books/NBK459165/); [PMC10350506](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10350506/)). **Timing matters**: levels must be drawn ≥6 hours post-dose/ingestion (after the distribution phase) to avoid falsely elevated readings.
- **Free (unbound) digoxin**: therapeutic 0.4–0.9 ng/mL; toxicity associated with ≥3.0 ng/mL free digoxin ([droracle summary](https://www.droracle.ai/articles/643703/what-are-the-target-serum-levels-for-digoxin-digitalis)).
- **Serum potassium** — the single best-validated **severity/prognostic** biomarker in acute poisoning (see §11); also magnesium, calcium, and renal function (creatinine/GFR) — essential because renal impairment is the dominant chronic-toxicity risk factor.
- **Assay caveats**: endogenous digoxin-like immunoreactive substances (DLIS) cause false-positive "digoxin" levels in renal failure, hepatic failure, pregnancy, and neonates (§4); Fab therapy itself invalidates standard immunoassay readings post-treatment because bound digoxin-Fab complex cross-reacts, giving falsely high apparent levels ([StatPearls NBK459165](https://www.ncbi.nlm.nih.gov/books/NBK459165/)).

**Electrophysiology / imaging**
- **12-lead ECG and continuous cardiac monitoring** are the primary and most time-sensitive diagnostic tools: look for PVCs (most common), AV block of any degree, sinus bradycardia, atrial tachycardia with block, and — near-pathognomonic — **bidirectional ventricular tachycardia** ([LITFL](https://litfl.com/digoxin-effect-ecg-library/); [PMC8212916 case report](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8212916/)).
- "**Digitalis effect**" (as opposed to toxicity) — scooped/sagging ST depression, T-wave flattening/inversion, short QT, prominent U-wave, PR prolongation — reflects therapeutic exposure and is distinct from a toxic arrhythmia and must not itself be mistaken for toxicity.
- No specific imaging modality is diagnostic; echocardiography may be used to assess the underlying cardiac disease (not the toxicity per se).

**Clinical criteria / differential diagnosis**
- Diagnosis is clinical, integrating exposure history, ECG pattern, and (supportively) serum level; differential includes other causes of AV block/bradyarrhythmia (beta-blocker or calcium-channel-blocker toxicity, hyperkalemia from other causes, sick sinus syndrome), other toxidromes causing GI+neuro symptoms, and — importantly — other cardiac glycoside exposures (oleander, foxglove, toad venom) which may or may not cross-react on a digoxin immunoassay depending on the specific assay ([StatPearls NBK459165](https://www.ncbi.nlm.nih.gov/books/NBK459165/)).

**Screening**: no population screening program exists; this is an acute/subacute event rather than a screenable condition. The nearest analog is *therapeutic drug monitoring* protocol in patients on chronic digoxin (checking level after dose change, with new renal impairment, or with initiation of an interacting drug).

**Genetic testing**: not indicated for the disease itself. ABCB1 genotyping remains a research tool rather than a validated clinical decision aid for digoxin dosing at this time.

---

## 11. Outcome/Prognosis

- **Mortality**: severe digoxin toxicity carries an estimated **~20% mortality** in historical series predating widespread Fab availability ([StatPearls NBK459165](https://www.ncbi.nlm.nih.gov/books/NBK459165/)); more recent in-hospital mortality estimates range **3–20%** depending on population and era ([search synthesis, various](https://www.ajkd.org/article/S0272-6386(21)00999-9/fulltext)). US Poison Control 2011 data show a case-fatality of ~1.1% (27/2,513) across the broad (including less-severe) reported case population ([Medscape overview](https://emedicine.medscape.com/article/154336-overview)).
- **Best-validated prognostic marker — serum potassium in acute ingestion**: a classic series of 91 patients (pre-Fab era) found **serum K⁺ >5.5 mEq/L associated with 100% mortality**, **5.0–5.5 mEq/L with ~50% mortality**, and **<5.0 mEq/L with 0% mortality**, and potassium outperformed both initial ECG changes and serum digoxin level as a predictor of death ([synthesis of the classic Bismuth series, cited via StatPearls/PMC3372009](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3372009/)). Expert consensus treats serum K⁺ ≥6 mEq/L (with other causes of hyperkalemia excluded) as an indication for Fab therapy.
- **Complications**: refractory bradyarrhythmia/heart block, ventricular arrhythmia and cardiac arrest (leading direct cause of death), hyperkalemia-related complications, and — as a treatment complication — anaphylaxis or serum sickness from ovine Fab fragments.
- **Recovery potential**: generally good with prompt recognition and Fab therapy where indicated; digoxin's positive inotropic/toxic effects are reversible once free drug is neutralized or eliminated, and no long-term structural cardiac sequelae are described from the toxicity itself (as opposed to the underlying heart disease that led to digoxin prescription).
- **Prognostic factors** overall: age, degree/type of arrhythmia (heart block or new arrhythmia worsens prognosis), renal function, timing of presentation, and (per the above) serum potassium at presentation.

---

## 12. Treatment

**Decontamination**
- **Activated charcoal** (single or multi-dose) is first-line for **recent (~within 1 hour) acute ingestion**; multi-dose charcoal can interrupt enterohepatic recirculation. By the time cardiac symptoms manifest, most patients are outside this window ([RebelEM](https://rebelem.com/management-of-digoxin-toxicity/); [StatPearls NBK459165](https://www.ncbi.nlm.nih.gov/books/NBK459165/)).
- **Gastric lavage is avoided** — vagal stimulation from the procedure risks worsening bradyarrhythmia.

**Definitive antidote — Digoxin Immune Fab (ovine)**
- **Digoxin Immune Fab** (brand names Digibind, DigiFab) — ovine polyclonal Fab fragments raised against a digoxin derivative (digoxindicarboxymethoxylamine, DDMA) that rapidly bind and neutralize free digoxin ([DigiFab prescribing info, FDA](https://www.fda.gov/media/74693/download); [Wikipedia](https://en.wikipedia.org/wiki/Digoxin_immune_fab)).
- **Indications**: life-threatening arrhythmia (especially AV block or ventricular tachyarrhythmia), acute ingestion ≥10 mg in a previously healthy adult (≥4 mg or >0.1 mg/kg in a child), serum digoxin >10 ng/mL, or serum K⁺ ≥5 mEq/L in the setting of digoxin toxicity ([mdcalc](https://www.mdcalc.com/calc/4036/digifab-dosing-digoxin-poisoning); [StatPearls NBK459165](https://www.ncbi.nlm.nih.gov/books/NBK459165/)).
- **Dosing**: one 40 mg vial neutralizes ~0.5 mg digoxin; empiric dosing of 10 vials (adult)/5 vials (pediatric) is used when the ingested dose/level is unknown; a weight-and-level-based formula (vials = [serum level (ng/mL) × weight (kg)] / 100) is used when data are available.
- **Practical consequences**: after Fab administration, standard digoxin immunoassays become clinically uninterpretable (falsely high, reflecting bound complex) until Fab is cleared; hypokalemia commonly follows successful Fab therapy as the pump is "released," requiring close K⁺ monitoring ([StatPearls NBK459165](https://www.ncbi.nlm.nih.gov/books/NBK459165/)).
- **Adverse effects**: hypersensitivity/anaphylaxis (screen for known sheep-protein, papain/papaya allergy) and serum sickness.

**Supportive/electrolyte management**
- **Hyperkalemia**: standard measures (insulin/glucose, sodium bicarbonate, binding resins); **IV calcium is classically considered relatively contraindicated** in digoxin toxicity because it can precipitate ventricular arrhythmia by further raising already-elevated intracellular Ca²⁺ ("stone heart" concern) — though this theoretical concern lacks strong clinical-outcome data supporting an absolute contraindication, per recent reviews ([StatPearls NBK459165](https://www.ncbi.nlm.nih.gov/books/NBK459165/)); Fab is preferred over calcium when K⁺ ≥5 mEq/L is due to digoxin.
- **Bradyarrhythmia/AV block**: **atropine** as a temporizing measure (excess vagal tone); temporary transvenous pacing may be considered but pacing/beta-agonists risk provoking ventricular tachyarrhythmia and are used cautiously.
- **Ventricular arrhythmia**: lidocaine or phenytoin have been used for digoxin-induced ventricular ectopy/tachyarrhythmia; **magnesium is generally avoided** if it will worsen bradycardia/AV block; **cardioversion is avoided** where possible (risk of precipitating refractory ventricular fibrillation) — defibrillation per ACLS protocol is reserved for pulseless arrest.
- **Hemodialysis/hemofiltration**: **not effective** for digoxin removal because of its very large volume of distribution (~6 L/kg) and extensive tissue binding (only ~0.5% of total-body digoxin is in the blood at steady state); the digoxin-Fab complex is likewise not cleared by conventional hemodialysis. Continuous venovenous hemodialysis/plasma exchange have been reported in refractory renal-failure cases as salvage options ([Pharmacy Times summary](https://www.pharmacytimes.com/view/digoxin-overdose-still-no-role-for-dialysis); [PMC12702486 plasma exchange after Fab failure](https://pmc.ncbi.nlm.nih.gov/articles/PMC12702486/)).

**Yellow-oleander-specific note**: fructose-1,6-diphosphate has been trialed as a low-cost antidote for yellow-oleander cardiotoxicity in resource-limited settings where Fab is unaffordable, given cost barriers to Fab access in South Asia ([PMC2912827 FDP RCT](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2912827/)).

**Suggested NCIT terms**: NCIT:C15747 (Supportive Care) for general management; NCIT:C15986 (Pharmacotherapy) with `therapeutic_agent` bound to the Fab product (no confirmed NCIT code identified in this search — verify via OAK/NCIT lookup before curation); a device/procedure term (e.g., transvenous pacing) would use the standard NCIT clinical-intervention/device pattern already established elsewhere in this KB.

---

## 13. Prevention

- **Primary prevention (iatrogenic)**: careful patient selection, renal-function-adjusted dosing, preference for lower target serum concentrations (0.5–0.8/1.0 ng/mL) in heart failure, avoidance/careful monitoring when co-prescribing known P-gp inhibitors (amiodarone, verapamil, macrolides, azole antifungals), and electrolyte optimization (avoid/correct hypokalemia, hypomagnesemia).
- **Secondary prevention**: routine therapeutic drug monitoring in at-risk patients (elderly, renal impairment, new interacting drug, dose change), with digoxin levels drawn correctly (≥6 h post-dose).
- **Primary prevention (plant/environmental)**: public-health messaging around the toxicity of foxglove, oleander, lily-of-the-valley, and related ornamental plants for households with children/pets; means-restriction approaches (reducing accessibility of yellow oleander seeds) have been proposed as a suicide-prevention strategy in South Asia, analogous to pesticide means-restriction, though this is less developed in the literature than pesticide restriction programs.
- **Public health/behavioral**: recognition that self-poisoning with a lethal, locally accessible plant agent (yellow oleander) is closely tied to impulsive self-harm in young people in endemic regions, making rapid access to antidote (Fab) and emergency care — rather than exposure elimination alone — a key tertiary-prevention lever given the plant's ubiquity.
- **Veterinary/agricultural prevention**: removing oleander and other cardiotoxic ornamentals from livestock-accessible pasture/hedgerows to prevent grazing-animal poisoning outbreaks and downstream food-safety concerns (contaminated milk/meat) ([PMC7472096](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7472096/)).
- **Prophylaxis**: no chemoprophylactic agent exists; prevention is entirely a matter of dosing/monitoring practice and exposure avoidance.
- **Genetic counseling**: not applicable (no heritable component to counsel about).

---

## 14. Other Species / Natural Disease

- **Companion animals**: dogs and cats are frequently poisoned by ingestion of foxglove, oleander, lily-of-the-valley, or *Kalanchoe* houseplants; clinical signs mirror the human toxidrome — drooling, vomiting/diarrhea, bradyarrhythmia, "nearly any type of dysrhythmia," tremors, and sudden death with few premonitory signs ([Pet Poison Helpline](https://www.petpoisonhelpline.com/poison/foxglove/); [VETgirl](https://vetgirlontherun.com/cardiac-glycoside-plants-poisonous-to-dogs-and-cats/)). Dog-toad (bufadienolide) poisoning from *Bufo* species interaction is a recognized veterinary presentation, especially where toads/frogs and dogs cohabit outdoor spaces.
- **Livestock**: cattle are poisoned by grazing on oleander, with documented outbreak-level mortality in dairy herds and secondary food-safety concerns about oleandrin residues in milk/meat ([PMC7472096](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7472096/); [PMC6723884](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6723884/)).
- **NCBI Taxon references**: *Canis lupus familiaris* (NCBITaxon:9615), *Felis catus* (NCBITaxon:9685), *Bos taurus* (NCBITaxon:9913), *Equus caballus* (NCBITaxon:9796) are all reported natural hosts of cardiac-glycoside plant poisoning.
- **Comparative/evolutionary biology — a genuinely distinctive feature of this "disease"**: several vertebrate and invertebrate lineages that specialize on cardiac-glycoside-containing diets or prey have **independently evolved target-site resistance** in the Na,K-ATPase α-subunit. Rodents (Cricetidae and Muridae) have convergently evolved substitutions **Q111L + A119S in ATP1A2** and **Q111R in ATP1A1**, reducing cardiac-glycoside binding affinity at the same pocket digoxin exploits in humans ([eLife 48224](https://elifesciences.org/articles/48224.pdf)); the crested serpent-eagle preying on invasive toxic cane toads in Okinawa shows analogous Na,K-ATPase-mediated resistance ([PMID:40660117](https://pubmed.ncbi.nlm.nih.gov/40660117/)); milkweed-specialist insect predators/parasites show the same convergent pattern ([ScienceDirect S0960982221014147](https://www.sciencedirect.com/science/article/pii/S0960982221014147)). This is directly relevant to why **rodents used as toxicology/pest-control models are relatively insensitive to cardiac glycosides**, a key consideration in interpreting rodent-model data for this entry.
- **Zoonotic potential**: none — this is a toxicologic, not infectious, process, so it is not "transmissible," though secondary human poisoning via contaminated animal products (milk/meat from oleander-grazing livestock) is a real, documented food-safety pathway.

---

## 15. Model Organisms

Digitalis poisoning is modeled almost entirely through **acute pharmacologic/electrophysiologic challenge**, not through genetic (knockout/transgenic) disease models, because the "disease" is drug/toxin exposure rather than a genetic lesion.

- **Guinea pig (whole-animal, in vivo)**: slow IV digoxin infusion in the anesthetized guinea pig reliably provokes extrasystoles, ventricular tachyarrhythmia, and cardiac arrest, and has been used classically to test antidote efficacy — e.g., a loading dose of 500 µg/kg digoxin was used to establish otherwise-lethal toxicity before testing monoclonal anti-digoxin antibody/Fab reversal ([PMID:6707937 "Reversal of lethal digoxin toxicity in guinea pigs using monoclonal antibodies and Fab fragments"](https://pubmed.ncbi.nlm.nih.gov/6707937/)). Standardized "Electrocardiographic Toxicity in the Guinea Pig" protocols exist for this purpose ([Curr Protoc Pharmacol](https://currentprotocols.onlinelibrary.wiley.com/doi/10.1002/0471141755.ph0529s18)).
- **Dog (whole-animal and isolated Purkinje fiber)**: canine Purkinje fiber preparations, using the cardiac glycoside **strophanthidin** as a pharmacologic proxy, are the classical system for demonstrating glycoside-induced enhancement of diastolic depolarization slope and spontaneous automaticity, and abnormal Ca²⁺ cycling as the source of non-driven depolarizations in conduction tissue ([PMID:1257581 "On the mechanisms underlying digitalis toxicity in cardiac Purkinje fibers"](https://pubmed.ncbi.nlm.nih.gov/1257581/); [JACC 1985, S0735-1097(85)80460-5](https://www.jacc.org/doi/10.1016/S0735-1097(85)80460-5)). Selective AV-block induction with physostigmine has been used in dogs to terminate digoxin-induced ventricular arrhythmia experimentally ([PMID:512919](https://pubmed.ncbi.nlm.nih.gov/512919/)).
- **Rodent limitation** (mouse/rat): as noted in §14, rodents have evolved reduced-affinity Na,K-ATPase isoforms (ATP1A1 Q111R; ATP1A2 Q111L/A119S), making them comparatively **insensitive** to cardiac glycosides relative to humans/dogs/guinea pigs — an important translational caveat for any rodent-based mechanistic or antidote study, and part of why guinea pig and dog (not mouse/rat) are the historical gold-standard toxicity models.
- **Cell-based/isolated-tissue systems**: isolated cardiac Purkinje fiber and ventricular myocyte preparations (sharp-electrode/voltage-clamp) remain the primary reductionist system for dissecting the DAD/triggered-automaticity mechanism; no major organoid, iPSC-cardiomyocyte, or CRISPR-screen literature specific to digoxin toxicity was identified in this search (a plausible gap/opportunity area rather than an established resource).
- **Model translational fidelity**: guinea pig and dog models recapitulate the core arrhythmia phenotype (ectopy, tachyarrhythmia, AV block) and were historically used to validate Fab-fragment antidote efficacy prior to human licensure, giving them **high fidelity** for the cardiac-electrophysiology endpoint; they do not model the human GI/visual symptom complex, which remains characterized almost exclusively from human case reports and case series.

---

## Summary for Knowledge-Base Curation

Digitalis poisoning is best curated as an **acquired/toxicologic disease entry** (MONDO:0017863) with:
- **Pathophysiology nodes**: Na⁺/K⁺-ATPase inhibition (molecular) → intracellular Na⁺/Ca²⁺ overload (molecular) → NCX1-mediated delayed afterdepolarization (cellular) → triggered automaticity/AV block (cellular→tissue) → arrhythmia/hemodynamic collapse (systemic), plus a parallel autonomic (vagal/sympathetic) branch and a hyperkalemia branch specific to acute massive exposure.
- **No causal `genetic:` entries** in the Mendelian sense; ABCB1/SLCO1B3 belong, if included at all, as **modifier/susceptibility** relationships, and ATP1A1 as the pathophysiology-node molecular target.
- **Environmental entries** for iatrogenic overdose, drug–drug interaction (P-gp inhibitors), and plant/zootoxin exposure (foxglove, oleander, yellow oleander, lily of the valley, toad bufadienolides), each with `influences_mechanisms` linking to the Na⁺/K⁺-ATPase inhibition node.
- **Treatments**: Digoxin Immune Fab as the flagship targeted antidote (with `therapeutic_agent`/NCIT binding to be resolved via OAK lookup), activated charcoal, atropine/pacing, and explicit `notes` on the calcium-contraindication controversy and hemodialysis ineffectiveness.
- **Animal models**: guinea pig and dog (RECAPITULATES, high fidelity for the cardiac phenotype), with an explicit divergence note for rodent Na,K-ATPase target-site insensitivity if a mouse/rat model is ever added.

---

## Sources

- [Digitalis Toxicity: Background, Etiology, Pathophysiology (Medscape)](https://emedicine.medscape.com/article/154336-overview)
- [Digitalis Toxicity Clinical Presentation (Medscape)](https://emedicine.medscape.com/article/154336-clinical)
- [Digitalis Toxicity Treatment & Management (Medscape)](https://emedicine.medscape.com/article/154336-treatment)
- [Digoxin toxicity (Wikipedia)](https://en.wikipedia.org/wiki/Digoxin_toxicity)
- [Cardiac Glycoside and Digoxin Toxicity — StatPearls (NBK459165)](https://www.ncbi.nlm.nih.gov/books/NBK459165/)
- [Digoxin Toxicity — StatPearls (NBK470568)](https://www.ncbi.nlm.nih.gov/books/NBK470568/)
- [Digoxin — StatPearls (NBK556025)](https://www.ncbi.nlm.nih.gov/books/NBK556025/)
- [Digoxin Immune Fab — StatPearls (NBK556101)](https://www.ncbi.nlm.nih.gov/books/NBK556101/)
- [Digoxin Toxicity • LITFL • CCC Toxicology](https://litfl.com/digoxin-toxicity-ccc/)
- [Digoxin poisoning • LITFL Toxicology Library](https://litfl.com/digoxin-poisoning/)
- [Digoxin Effect • LITFL ECG Library](https://litfl.com/digoxin-effect-ecg-library/)
- [Digoxin & cardiac glycosides: toxicity & therapeutic use — EMCrit IBCC](https://emcrit.org/ibcc/dig/)
- [Management of Digoxin Toxicity — REBEL EM](https://rebelem.com/management-of-digoxin-toxicity/)
- [Digoxin Toxicity Topic Review — Learn the Heart](https://www.healio.com/cardiology/learn-the-heart/cardiology-review/topic-reviews/digoxin-toxicity)
- [Identification of Na+/K+-ATPase inhibition-independent proarrhythmic ionic mechanisms of cardiac glycosides — PMC5446409](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5446409/)
- [Erratum — PMC5597635](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5597635/)
- [The mechanism of action of digoxin requires the sodium-dependent inactivation of the sodium-calcium exchanger — Science Advances](https://www.science.org/doi/10.1126/sciadv.ady9596)
- [Digoxin and Symptomatic Bradyarrhythmia — PMC10937055](https://pmc.ncbi.nlm.nih.gov/articles/PMC10937055/)
- [Clinical pharmacokinetics of digoxin — PMID:322907](https://pubmed.ncbi.nlm.nih.gov/322907/)
- [Impact of ABCB1 (MDR1) gene polymorphism and P-gp inhibitors on digoxin serum concentration — PMID:17377214](https://pubmed.ncbi.nlm.nih.gov/17377214/)
- [Post-mortem ABCB1 genotyping reveals elevated toxicity for female digoxin users — PMID:21311904](https://pubmed.ncbi.nlm.nih.gov/21311904/)
- [ABCB1 and SLCO1B3 gene polymorphisms and digoxin pharmacokinetics in AF — PMID:28208135](https://pubmed.ncbi.nlm.nih.gov/28208135/)
- [ABCB1 gene variants, digoxin and risk of sudden cardiac death — PMID:26531821](https://pubmed.ncbi.nlm.nih.gov/26531821/)
- [MDR1 genotypes and digoxin absorption — PMID:12492608](https://pubmed.ncbi.nlm.nih.gov/12492608/)
- [Impact of genetic polymorphisms of ABCB1 on drug disposition — Clin Pharmacokinet review](https://link.springer.com/article/10.1007/s40262-015-0267-1)
- [Cardiotoxicity of plants in South Africa — PMC3721620](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3721620/)
- [Outbreak of Oleander Poisoning in Dairy Cattle — PMC7472096](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7472096/)
- [A Probable Fatal Case of Oleander Poisoning on a Cattle Farm — PMC6723884](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6723884/)
- [Cardiac Glycoside Plants Poisonous to Dogs and Cats — VETgirl](https://vetgirlontherun.com/cardiac-glycoside-plants-poisonous-to-dogs-and-cats/)
- [Foxglove Is Toxic To Dogs — Pet Poison Helpline](https://www.petpoisonhelpline.com/poison/foxglove/)
- [MONDO:0017863 digitalis poisoning — Wikidata Q151350](https://www.wikidata.org/wiki/Q151350)
- [digitalis poisoning — NORD/Mondo mirror](https://rarediseases.org/mondo-disease/digitalis-poisoning/)
- [digoxin (CHEBI:4551)](https://www.ebi.ac.uk/chebi/CHEBI:4551)
- [Digoxin — PubChem CID 2724385](https://pubchem.ncbi.nlm.nih.gov/compound/2724385)
- [DigiFab dosing calculator — MDCalc](https://www.mdcalc.com/calc/4036/digifab-dosing-digoxin-poisoning)
- [DIGIFAB prescribing information — FDA](https://www.fda.gov/media/74693/download)
- [Digoxin immune fab — Wikipedia](https://en.wikipedia.org/wiki/Digoxin_immune_fab)
- [Digoxin Toxicity in Renal Failure: Resolution With Plasma Exchange After Fab Therapy Failure — PMC12702486](https://pmc.ncbi.nlm.nih.gov/articles/PMC12702486/)
- [Digoxin Overdose: Still No Role for Dialysis — Pharmacy Times](https://www.pharmacytimes.com/view/digoxin-overdose-still-no-role-for-dialysis)
- [An Endogenous Digoxin-Like Substance in Patients with Renal Impairment — Ann Intern Med](https://doi.org/10.7326/0003-4819-99-5-604)
- [Endogenous Digoxin-Like Factor in Neonates — Acta Paediatrica](https://onlinelibrary.wiley.com/doi/10.1111/j.1651-2227.1989.tb11093.x)
- [Digoxin-like immunoreactive substance in serum of preterm and full-term neonates — Eur J Pediatr](https://link.springer.com/article/10.1007/BF02343220)
- [Epidemic of self-poisoning with seeds of the yellow oleander tree in northern Sri Lanka — Trop Med Int Health 1999](https://onlinelibrary.wiley.com/doi/abs/10.1046/j.1365-3156.1999.00397.x)
- [Epidemiology of intentional self-poisoning in rural Sri Lanka — PMID:16319413](https://pubmed.ncbi.nlm.nih.gov/16319413/)
- [Yellow oleander poisoning — a study of 170 cases](https://www.sciencedirect.com/science/article/abs/pii/0379073888901508)
- [Fructose-1,6-diphosphate as a novel antidote for yellow oleander cardiotoxicity — PMC2912827](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2912827/)
- [Human Deaths Related to Oleander Poisoning: A Review of the Literature — MDPI Toxins](https://www.mdpi.com/2072-6651/17/3/115)
- [Good Outcome after Digoxin Toxicity Despite Very High Serum Potassium Level — PMC3372009](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3372009/)
- [Expert Consensus on the Diagnosis and Management of Digoxin Toxicity — Am J Med](https://www.amjmed.com/article/S0002-9343(24)00543-6/fulltext)
- [Review: Failure of current digoxin monitoring for toxicity — PMC10350506 / PMID:37465455](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10350506/)
- [The Effect of Digoxin on Mortality and Morbidity in Patients with Heart Failure — NEJM (DIG trial)](https://www.nejm.org/doi/full/10.1056/NEJM199702203360801)
- [Digoxin and reduction in mortality and hospitalization in heart failure: post hoc analysis of the DIG trial — Eur Heart J](https://academic.oup.com/eurheartj/article/27/2/178/553763)
- [Association of Serum Digoxin Concentration and Outcomes in Patients With Heart Failure — JAMA](https://jamanetwork.com/journals/jama/fullarticle/195990)
- [Effects of Digoxin in high-risk chronic heart failure patients in the DIG trial: subgroup analysis — PMC3860905](https://pmc.ncbi.nlm.nih.gov/articles/PMC3860905/)
- [Adaptive substitutions underlying cardiac glycoside insensitivity in rodents — eLife 48224](https://elifesciences.org/articles/48224.pdf)
- [Amino acid residues of Na,K-ATPase involved in ouabain sensitivity — PMID:8385116](https://pubmed.ncbi.nlm.nih.gov/8385116/)
- [Convergent evolution of cardiac-glycoside resistance in predators and parasites of milkweed herbivores — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0960982221014147)
- [Evolutionary insights into Na+/K+-ATPase-mediated toxin resistance in the Crested Serpent-eagle — PMID:40660117](https://pubmed.ncbi.nlm.nih.gov/40660117/)
- [Reversal of lethal digoxin toxicity in guinea pigs using monoclonal antibodies and Fab fragments — PMID:6707937](https://pubmed.ncbi.nlm.nih.gov/6707937/)
- [Electrocardiographic Toxicity in the Guinea Pig — Curr Protoc Pharmacol](https://currentprotocols.onlinelibrary.wiley.com/doi/10.1002/0471141755.ph0529s18)
- [On the mechanisms underlying digitalis toxicity in cardiac Purkinje fibers — PMID:1257581](https://pubmed.ncbi.nlm.nih.gov/1257581/)
- [Cellular electrophysiology of digitalis toxicity — JACC 1985](https://www.jacc.org/doi/10.1016/S0735-1097(85)80460-5)
- [Termination of ventricular arrhythmias from digoxin by physostigmine in the dog — PMID:512919](https://pubmed.ncbi.nlm.nih.gov/512919/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 35 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 1 |
| References weighed for topical relevance | 34 |
| On topic | 11 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:40660117` (5 mentions) - Evolutionary insights into Na(+)/K(+)-ATPase-mediated toxin resistance in the Crested Serpent-eagle preying on introduced cane toads in Okinawa, Japan.
  - shared terms: atpase

Weighed against this report's own most characteristic terms: `digoxin`, `toxicity`, `cardiac`, `poisoning`, `digitalis`, `glycoside`, `disease`, `drug`, `exposure`, `fab`, `failure`, `effect`, `oleander`, `atpase`, `patient`, `heart`, `renal`, `ventricular`, `acute`, `arrhythmia`.

34 of 35 references resolved; the rest could not be looked up either way.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 32 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0017863` (3 mentions) - the report calls it "digitalis poisoning", "acquired/toxicologic disease entry"; MONDO calls it **digitalis poisoning**
- `HP:0000496` (1 mention) - the report calls it "Halo vision"; HP calls it **Abnormality of eye movement**
- `HP:0011703` (1 mention) - the report calls it "Atrioventricular block"; HP calls it **Sinus tachycardia**
- `HP:0001700` (1 mention) - the report calls it "parent: Cardiac arrhythmia"; HP calls it **Myocardial necrosis**
- `UBERON:0002205` (1 mention) - the report calls it "AV node"; UBERON calls it **manubrium of sternum**
- `UBERON:0002136` (1 mention) - the report calls it "Purkinje fiber cell tissue"; UBERON calls it **hilus of dentate gyrus**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001662` (1 mention) - the report calls it "Sinus bradycardia"; HP calls it **Bradycardia**
- `GO:0005391` (3 mentions) - the report calls it "P-type Na⁺/K⁺-exchanging ATPase activity, sodium/potassium-transporting ATPase complex", "Na⁺/K⁺-ATPase activity"; GO calls it **P-type sodium:potassium-exchanging transporter activity**, and lists "P-type sodium:potassium-exchanging ATPase activity" among its other names
- `GO:0086036` (2 mentions) - the report calls it "regulation of cardiac muscle cell membrane potential", "cardiac membrane potential regulation"; GO calls it **regulation of cardiac muscle cell membrane potential**
- `GO:0086013` (1 mention) - the report calls it "membrane repolarization in ventricular cardiac muscle cell"; GO calls it **membrane repolarization during cardiac muscle cell action potential**
- `GO:0060402` (1 mention) - the report calls it "calcium ion transport into cytosol via sarcoplasmic reticulum"; GO calls it **calcium ion transport into cytosol**
- `CL:1000497` (1 mention) - the report calls it "Purkinje myocyte"; CL calls it **kidney cell**
- `CL:0002129` (1 mention) - the report calls it "cardiac pacemaker cell"; CL calls it **regular atrial cardiac myocyte**, and lists "atrial cardiac muscle cell" among its other names
- `UBERON:0002018` (1 mention) - the report calls it "SA node"; UBERON calls it **synovial membrane of synovial joint**, and lists "stratum synoviale" among its other names
- `NCBITaxon:9615` (1 mention) - the report calls it "Canis lupus familiaris", "NCBI Taxon references**: *Canis lupus familiaris"; NCBITaxon calls it **Canis lupus familiaris**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0017863` - called "digitalis poisoning", "acquired/toxicologic disease entry"
- `GO:0005391` - called "P-type Na⁺/K⁺-exchanging ATPase activity, sodium/potassium-transporting ATPase complex", "Na⁺/K⁺-ATPase activity"
- `GO:0086036` - called "regulation of cardiac muscle cell membrane potential", "cardiac membrane potential regulation"
- `NCBITaxon:9615` - called "Canis lupus familiaris", "NCBI Taxon references**: *Canis lupus familiaris"