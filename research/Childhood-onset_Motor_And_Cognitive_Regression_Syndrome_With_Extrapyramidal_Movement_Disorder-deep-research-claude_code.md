---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-12T15:57:40.252304'
end_time: '2026-10-12T15:59:31.893786'
duration_seconds: 111.64
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: childhood-onset motor and cognitive regression syndrome with extrapyramidal
    movement disorder
  mondo_id: ''
  category: ''
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
  - claude-sonnet-5-5
  web_search_requests: 6
  num_turns: 12
  total_cost_usd: 0.8631021
  session_id: c5bca049-79dd-565a-9d58-3e2354d3de80
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 15
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 3
  validator_version: 0.3.0
term_validation:
  total_terms: 22
  verified: 20
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 5
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0001257
    reported_labels:
    - Later feature
    ontology_label: Spasticity
  - term_id: HP:0000752
    reported_labels:
    - Early
    ontology_label: Hyperactivity
  - term_id: HP:0001250
    reported_labels:
    - Absent in Toro's four; reported in some others
    ontology_label: Seizure
  labels_variant: 1
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** childhood-onset motor and cognitive regression syndrome with extrapyramidal movement disorder
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **childhood-onset motor and cognitive regression syndrome with extrapyramidal movement disorder** covering all of the
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

# Research Report: Childhood-onset motor and cognitive regression syndrome with extrapyramidal movement disorder (UBTF E210K neuroregression syndrome)

**Evidence status.** I did not confirm every detail in this report against the primary text.
- **Fetched or read:** the Toro 2018 abstract page, the 2024 Brain Sciences review's search summary, and the GenCC, ClinGen, NORD, GARD, GTR and Genomics England pages.
- **Blocked:** PMC full texts returned a CAPTCHA, so I could not read them. This includes the Tinker 2022 case report and the full review.
- **PMIDs:** only PMID:28777933 (Edvardson 2017) and PMID:38391753 (Overview review, 2024) were seen in results. For other papers I give journal, year and DOI where seen. A curator should run `just fetch-reference` on them before quoting anything.
- **Snippets:** the quotes below are search-result paraphrases, not verified exact abstract text. Do not paste them as evidence snippets without checking them against the cached reference.
- **Items marked [unverified]:** these are not backed by anything I retrieved. Treat them as leads.

---

## 1. Disease information

**Overview.** This is a rare, autosomal dominant neurodegenerative disorder of childhood. It is caused almost always by a recurrent de novo missense variant in *UBTF*, c.628G>A (p.Glu210Lys, "E210K").
- Development is normal or mildly delayed at first.
- Between about 2.5 and 7 years, children regress in motor, speech, cognitive and behavioural skills.
- A movement disorder (dystonia, parkinsonism, chorea or rigidity) develops, along with ataxia and spasticity.
- MRI shows progressive cerebral and cerebellar atrophy.
- By the early teens many have lost speech and walking.

**Identifiers**

| Resource | ID |
|---|---|
| MONDO | MONDO:0044701 |
| OMIM | 617672 (gene: *600673, UBTF) |
| Orphanet | 500180 |
| UMLS | C4540086 |
| HGNC | HGNC:12511 (`hgnc:12511` in dismech), 17q21.31 |
| ClinVar condition | "UBTF E210K Neuroregression Syndrome" |

Sources: [GenCC](https://thegencc.org/genes/HGNC:12511), [PomBase MONDO page](https://www.pombase.org/term/MONDO:0044701), [NCBI GTR](https://ncbi.nlm.nih.gov/gtr/conditions/C4540086), [GARD](https://rarediseases.info.nih.gov/diseases/13658/childhood-onset-motor-and-cognitive-regression-syndrome-with-extrapyramidal-movement-disorder).

**Synonyms**
- CONDBA
- Neurodegeneration, childhood-onset, with brain atrophy (the OMIM title)
- UBTF neuroregression syndrome
- UBTF E210K neuroregression syndrome
- UBTF-related disorder
- Developmental neuroregression due to UBTF E210K

**Data provenance.** The data are aggregated from published case reports and series, plus curated resources (OMIM, ClinGen, GenCC). They are not EHR-derived.

**Scope note for curators.** The MONDO name describes the syndrome, and OMIM names it by the gene. The entry should be a single `DISEASE`-level record anchored on the E210K variant. Other *UBTF* variants cause different, non-regressive neurodevelopmental phenotypes (see section 4). They belong in `notes` or `has_subtypes` only if curated separately. I did not apply the lump/split ladder here, because it governs cancer and infection entries.

---

## 2. Etiology

- **Cause.** The cause is genetic: a heterozygous, de novo, recurrent *UBTF* c.628G>A (p.E210K). ClinGen rates the gene–disease relationship **Definitive** (evaluated 16 August 2023; [GenCC](https://thegencc.org/genes/HGNC:12511)).
- **Discovery.** Edvardson et al., *Am J Hum Genet* 2017, PMID:28777933 (DOI 10.1016/j.ajhg.2017.07.002). They reported 7 unrelated patients with the same de novo variant, found by exome sequencing and confirmed by Sanger. Fibroblast studies suggested gain of function.
- **Replication.** Toro et al., *Hum Mol Genet* 2018;27(4):691–705, DOI 10.1093/hmg/ddx435. They found the same variant in 4 more probands.
- **Genetic risk factors.** I found no modifier genes or susceptibility loci.
- **Environmental and protective factors.** No environmental risk factors, protective factors or gene–environment interactions are documented. The variant is de novo and recurrent, so it probably reflects a mutation hotspot. I did not retrieve the source for the hotspot reasoning, so it is [unverified].

---

## 3. Phenotypes

Frequencies are approximate and come from the Toro cohort (n=4) and summaries of the 2024 review. They are not per-feature counts from a verified source. Candidate HPO terms need a lookup (`runoak` or the cache) before binding.

| Phenotype | Notes | Candidate HPO (verify) |
|---|---|---|
| Developmental regression | Core feature; onset ~2.5–7 y, median ~3 y | HP:0002376 Developmental regression |
| Motor regression / loss of ambulation | Lost by early teens | HP:0002505-type terms, e.g. loss of ability to walk [lookup] |
| Cognitive decline, profound intellectual disability | Progressive | HP:0001256 / HP:0002342 [lookup] |
| Speech loss, aphasia, dysarthria | Dysarthria early; speech lost by early teens | HP:0001344 Absent speech; HP:0001260 Dysarthria |
| Hypotonia, gait ataxia | Early features | HP:0001252; HP:0002066 |
| Dystonia | Reported in 7 of 11 unrelated cases per a Genomics England panel note | HP:0001332 |
| Parkinsonism, rigidity, chorea | Variable. A juvenile dystonia-parkinsonism report exists (Ikeda et al., *Neurol Sci* 2020/2021, no PMID found) | HP:0001300; HP:0002072 |
| Spasticity | Later feature | HP:0001257 |
| Hyperactivity / behavioural change | Early | HP:0000752 |
| Seizures | Absent in Toro's four; reported in some others | HP:0001250 |

**Imaging.** Progressive generalised atrophy, supratentorial more than infratentorial, involving grey and white matter. The corpus callosum is thin and the cerebellar vermis is atrophic. Some reports describe diffuse white-matter T2 change.

**Quality of life.** There are no formal QoL instruments. Function is lost progressively, and many patients are wheelchair-dependent and non-verbal by the teen years.

---

## 4. Genetic and molecular information

- **Gene.** *UBTF* (`hgnc:12511`), upstream binding transcription factor, which encodes UBF (UBTF1 and UBTF2 isoforms). The inheritance is autosomal dominant.
- **Variant.** NM_014233.4:c.628G>A, p.Glu210Lys, in HMG-box 2. It creates a positively charged stretch of three lysines. It is absent from gnomAD. ClinVar lists it as pathogenic.
- **Origin.** It is germline and de novo. Germline mosaicism in a parent has not been described in what I saw, so I make no claim either way.
- **Functional consequence.** Most evidence points to gain of function.
  - The variant binds negatively charged DNA more strongly.
  - It leads to unstable preinitiation complexes at rDNA.
  - Patient fibroblasts show elevated pre-rRNA (>3×) and 18S rRNA (>2×), nucleolar abnormalities, DNA double-strand breaks, defective G2 progression and increased apoptosis (Toro 2018).
- **Unsettled mechanism.** ClinGen notes that a mouse study (including knock-in work) suggested loss of function, so the mechanism needs more experiments. I could not read that knock-in study, so details are [unverified]. The *Ubtf* knockout/knockdown paper (*Brain Research*) is a different paper.
- **Other UBTF variants.** A novel likely-pathogenic variant with a severe, divergent neurodevelopmental phenotype is reported (Tinker et al., *Mol Genet Genomic Med* 2022, DOI 10.1002/mgg3.2054). Truncating variants and microdeletions involving *UBTF* are linked to developmental delay and intellectual disability without regression. These should not be pooled with E210K.
- **Epigenetics and chromosomal abnormalities.** I found nothing disease-specific beyond altered rDNA chromatin state (OMIM summary of Edvardson). The 17q21.31 microdeletions above overlap *UBTF* but are a different condition.

---

## 5. Environmental information

None documented. There are no toxin, lifestyle or infectious-agent associations. Under the dismech environmental-evidence rules, this is a case for leaving the section empty, not for a "Left deliberately uncited" waiver.

---

## 6. Mechanism and pathophysiology

**Causal chain** (steps marked *inferred* are not demonstrated in patients):

1. De novo UBTF c.628G>A (p.E210K) in HMG-box 2 puts a lysine run in the DNA-binding domain *(demonstrated)*.
2. This increases UBF's affinity for negatively charged DNA, which leads to unstable preinitiation complex formation at rDNA promoters *(proposed, from cell studies)*.
3. That results in altered rDNA chromatin structure and rRNA dysregulation, with elevated pre-rRNA and 18S rRNA and nucleolar abnormalities *(demonstrated in patient fibroblasts)*.
4. Nucleolar and transcriptional stress then leads to DNA double-strand breaks, defective G2 progression and apoptosis *(demonstrated in fibroblasts)*.
5. Neurons are vulnerable, since rDNA heterochromatin is tightly regulated in differentiation, so progressive neuronal loss follows *(inferred; no patient neuropathology retrieved)*.
6. The result is cerebral and cerebellar atrophy, with regression of motor, speech and cognitive function *(clinical and MRI observation)*.
7. The extrapyramidal movement disorder (dystonia, parkinsonism, chorea) is attributed to basal ganglia involvement *(inferred; not demonstrated)*.

**Branch.** A loss-of-function or haploinsufficiency contribution is possible. Heterozygous *Ubtf*+/− mice have only mild motor and behavioural phenotypes, which argues against pure haploinsufficiency as the main cause.

**Candidate ontology terms** (look up before binding):
- GO: rRNA transcription, RNA polymerase I preinitiation complex assembly, nucleolus (cellular component), DNA damage response, apoptotic process.
- Cell types: neuron, fibroblast (the cell type studied). Specific CL terms for cortical and cerebellar neuron populations are [unverified], since no neuropathology was retrieved.
- Omics, immune and metabolic changes: none documented.

---

## 7. Anatomical structures affected

- **Primary:** brain, including cerebral cortex, cerebral white matter, corpus callosum, cerebellum (vermis) and basal ganglia (inferred from the movement disorder).
- **Body system:** nervous system.
- **Subcellular:** nucleolus and rDNA chromatin.
- **Lateralisation:** bilateral and symmetric atrophy, as far as reported.

---

## 8. Temporal development

- **Onset:** early childhood after normal or mildly delayed development; regression starts at about 2.5–7 years. The pattern is insidious and progressive.
- **Progression:** slowly progressive. Speech and ambulation are typically lost by the early teens.
- **Remission:** none described.
- **Critical windows:** no treatment window is defined.

---

## 9. Inheritance and population

- **Prevalence/incidence:** not established. The 2024 Brain Sciences review counted about 17 reported cases worldwide; ClinGen counts 16 E210K probands.
- **Inheritance:** autosomal dominant, with the variant arising de novo. Recurrence risk is low unless parental germline mosaicism is present, which is not documented.
- **Penetrance:** apparently complete in reported cases.
- **Expressivity:** variable. Seizures, the type of movement disorder and the age of onset differ between patients.
- **Anticipation, founder effects, consanguinity, carrier frequency, sex ratio:** no evidence found.
- **Geography and ancestry:** cases come from several countries; I found no enrichment.

---

## 10. Diagnostics

- **Genetic testing:** exome or genome sequencing, or a neurodegeneration/neuroregression panel including *UBTF* (it appears on the Genomics England "Childhood onset dystonia, chorea or related movement disorder" panel). Confirm by Sanger sequencing. Targeted testing for c.628G>A is justified in a child with regression plus dystonia or parkinsonism. Whether CMA, mtDNA or repeat-expansion tests are useful is not documented, beyond ruling out other causes.
- **Imaging:** serial MRI shows progressive atrophy, a thin corpus callosum and vermis atrophy.
- **Biomarkers:** none validated. Fibroblast pre-rRNA and 18S rRNA are research-only.
- **Differential diagnosis:** other causes of childhood neuroregression, including NCL, leukodystrophies, mitochondrial disease, Rett and other neurodevelopmental regression disorders, and other genetic dystonia-parkinsonism syndromes. Distinguishing features are not systematically documented.
- **Screening:** none.

---

## 11. Outcome and prognosis

- **Survival:** not well characterised. I found no life-expectancy data.
- **Function:** profound disability. Speech and walking are usually lost by the early teens.
- **Complications:** spasticity and dystonia. Others such as dysphagia and aspiration are plausible but [unverified].
- **Prognostic factors:** none established.

---

## 12. Treatment

- **No disease-modifying therapy is known.** I found no gene therapy, antisense, cell-based or targeted treatment. I found no clinical trials. Searching ClinicalTrials.gov for NCT numbers is a recommended next step.
- **Symptomatic care:** supportive care, physical, occupational and speech therapy, and standard management of dystonia, spasticity and seizures. Specific drug responses are not documented in what I retrieved.
- **Pharmacogenomics:** none.
- **Candidate NCIT treatment terms:** NCIT:C15747 (Supportive Care), NCIT:C15302 (Physical Therapy), NCIT:C15315 (Rehabilitation), NCIT:C159273 (Speech Language Therapy), and NCIT:C121351 (Occupational Therapy). Each was taken from the CLAUDE.md term list, so look them up again before binding.

---

## 13. Prevention

- No primary or secondary prevention exists.
- **Genetic counselling:** the variant is de novo, so recurrence risk is low. Parental germline mosaicism cannot be excluded, and prenatal testing is possible for families who want it.
- No vaccine, behavioural or environmental measure applies.

---

## 14. Other species and natural disease

- No naturally occurring disease in non-human species was found.
- Orthologues exist in mouse (*Ubtf*) and *Drosophila*. UBF is highly conserved, and the conserved HMG-box is relevant to the variant.

---

## 15. Model organisms

- ***Drosophila*.** Pan-neuronal expression of human mutant UBTF1 (E210K) is lethal before adulthood, while wild-type expression is not (Toro 2018; also listed on FlyBase as a human disease model, [FBhh0000958](https://flybase.org/reports/FBhh0000958.html)). This is in vivo model-organism evidence and partly recapitulates toxicity, but it does not recapitulate regression.
- **Mouse.**
  - *Ubtf*−/− is embryonic lethal.
  - *Ubtf*+/− shows mild motor and behavioural changes, and a later study reported age-progressive worsening with haploinsufficiency. It did not show clear neurodegeneration at 18 months in the tissue examined.
  - A knock-in mouse was reported that points toward loss of function (per ClinGen); I could not retrieve it, so treat the details as [unverified].
- **Cell models:** patient fibroblasts (in vitro) show the rRNA, nucleolar and DNA-damage phenotypes.
- **Limitations:** no model reproduces the human progressive regression and movement disorder. The mouse haploinsufficiency data and the human gain-of-function data conflict. This fits a `HUMAN_MODEL_MISMATCH` discussion in the entry.

---

## Suggested next steps for curation

1. Run `just fetch-reference PMID:28777933` and `PMID:38391753`. Find the PMIDs for Toro 2018 (DOI 10.1093/hmg/ddx435) and Tinker 2022 (DOI 10.1002/mgg3.2054) from the DOIs.
2. Pull the ClinGen CGGV assertion for UBTF, which supports a `gene_disease_validity` record. The GenCC search result lists it as Definitive.
3. Check the stub and claim issue for MONDO:0044701 before starting the entry.
4. Look up every HPO, GO, NCIT and CL term above. Several are placeholders.

## Sources
- [GenCC: UBTF (HGNC:12511)](https://thegencc.org/genes/HGNC:12511)
- [MGI/OMIM:617672 disease page](https://informatics.jax.org/disease/OMIM:617672)
- [NORD (MONDO)](https://rarediseases.org/mondo-disease/childhood-onset-motor-and-cognitive-regression-syndrome-with-extrapyramidal-movement-disorder/)
- [GARD](https://rarediseases.info.nih.gov/diseases/13658/childhood-onset-motor-and-cognitive-regression-syndrome-with-extrapyramidal-movement-disorder)
- [Global Genes](https://globalgenes.org/disorder/childhood-onset-motor-and-cognitive-regression-syndrome-with-extrapyramidal-movement-disorder/)
- [NCBI GTR C4540086](https://ncbi.nlm.nih.gov/gtr/conditions/C4540086)
- [OMIM *600673 UBTF](https://omim.org/entry/600673)
- [Toro et al. 2018, Hum Mol Genet](https://academic.oup.com/hmg/article/27/4/691/4782494)
- [An Overview of UBTF Neuroregression Syndrome, Brain Sci 2024 (PMID 38391753)](https://pubmed.ncbi.nlm.nih.gov/38391753/)
- [Tinker et al. 2022](https://onlinelibrary.wiley.com/doi/full/10.1002/mgg3.2054)
- [ClinVar RCV000504592](https://www.ncbi.nlm.nih.gov/clinvar/RCV000504592/)
- [Genomics England PanelApp, UBTF](https://panelapp.genomicsengland.co.uk/panels/847/gene/UBTF/)
- [FlyBase disease model report](https://flybase.org/reports/FBhh0000958.html)
- [Ubtf knockout/knockdown mice, Brain Research](https://www.sciencedirect.com/science/article/am/pii/S0006899322002773)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 22 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 9 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001257` (1 mention) - the report calls it "Later feature"; HP calls it **Spasticity**
- `HP:0000752` (1 mention) - the report calls it "Early"; HP calls it **Hyperactivity**
- `HP:0001250` (1 mention) - the report calls it "Absent in Toro's four; reported in some others"; HP calls it **Seizure**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0044701` (4 mentions) - the report calls it "MONDO"; MONDO calls it **childhood-onset motor and cognitive regression syndrome with extrapyramidal movement disorder**, and lists "CONDBA" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.