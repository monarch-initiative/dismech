---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5-5
cached: false
start_time: '2026-10-14T15:49:16.494858'
end_time: '2026-10-14T15:51:52.751948'
duration_seconds: 156.26
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Gaze Palsy Familial Horizontal With Progressive Scoliosis 2
  mondo_id: MONDO:0054602
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
  - claude-opus-5-5
  web_search_requests: 2
  num_turns: 19
  total_cost_usd: 2.031674400000001
  session_id: 949daad5-cacb-4729-a76d-d9debb4467d2
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 8
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 6
  validator_version: 0.3.0
term_validation:
  total_terms: 17
  verified: 17
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 1
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0054602
    reported_labels:
    - MONDO
    ontology_label: gaze palsy, familial horizontal, with progressive scoliosis, 2
  - term_id: HP:0001263
    reported_labels:
    - most
    ontology_label: Global developmental delay
  - term_id: HP:0001249
    reported_labels:
    - most (one patient described as "modest")
    ontology_label: Intellectual disability
  - term_id: GO:0005042
    reported_labels:
    - already in the entry
    ontology_label: netrin receptor activity
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Gaze Palsy Familial Horizontal With Progressive Scoliosis 2
- **MONDO ID:** MONDO:0054602 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Gaze Palsy Familial Horizontal With Progressive Scoliosis 2** covering all of the
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

Reviewing the cached abstracts; next I'll pull the key quotes, then do a short web check for any newer reports.

Checking the web for reports newer than 2024 and for the mouse model citations.

# Gaze Palsy, Familial Horizontal, With Progressive Scoliosis 2 (HGPPS2 / Developmental Split-Brain Syndrome): Research Report

**Scope and sourcing.** This report is built mainly from six references already cached in this repository: PMID:28250456, 38585553, 33141514, 29068161, 38516134 and 15105459. Quotes from them were read from the cached abstract or full text. Two web searches were also run: one for newer case reports and one for the mouse knockout paper. Anything not checked against a source is marked **[unverified]** and should be treated as a lead.

Several resources could not be used because they need authorization: the claude.ai PubMed, OLS, bgpt and Noctua connectors. As a result, no ontology CURIE below was looked up in this session. Every term ID is a **suggested lead** and must be checked with `runoak`, the term caches or `just validate-terms` before it goes into an entry.

---

## 1. Disease Information

**Overview.** HGPPS2 is an ultra-rare autosomal recessive disorder of axon guidance caused by biallelic loss-of-function variants in **DCC**, the gene for the netrin-1 receptor "deleted in colorectal carcinoma". In ROBO3-related HGPPS1, the midline-crossing failure is limited to the hindbrain and spinal cord. In HGPPS2 it affects commissures along the whole neuraxis.

- Rahikkala et al. 2024 (PMID:38585553, Mol Syndromol; abstract): *"Horizontal gaze palsy with progressive scoliosis-2 (HGPPS2, MIM 617542) with impaired intellectual development aka developmental split-brain syndrome is an ultra-rare congenital disorder caused by pathogenic biallelic variants in the deleted in colorectal cancer (DCC) gene."*
- Jamuar et al. 2017 (PMID:28250456, Nat Genet), the defining paper: *"Here we report a new human syndrome in which these commissures are widely disrupted, thus causing clinical manifestations of horizontal gaze palsy, scoliosis, and intellectual disability."*

**Identifiers**

| Resource | ID | Status |
|---|---|---|
| MONDO | MONDO:0054602 | already the entry's `disease_term` |
| OMIM | 617542 | quoted in PMID:38585553 and PMID:29068161 |
| Gene (OMIM) | DCC 120470 | quoted in PMID:28250456 |
| HGNC | hgnc:2701 (DCC) | already used in the KB entry |
| Orphanet / ICD-10 / ICD-11 / MeSH | not checked | **[unverified]** ICD-10 probably falls under Q04.x/H51.0 only by analogy; do not assert it |

**Synonyms:** HGPPS2; Horizontal gaze palsy with progressive scoliosis 2 with impaired intellectual development; Developmental split-brain syndrome (DSBS). PMID:29068161 uses "developmental split brain syndrome (DSBS, MIM# 617542)".

**Data basis:** aggregated case reports, about 8 published patients from 5 families. There are no registry or EHR data.

## 2. Etiology

- **Cause:** biallelic germline loss-of-function variants in DCC on 18q21.2. Marsh et al. 2018 (PMID:29068161): *"Biallelic, predicted loss-of-function DCC mutations cause developmental split brain syndrome (DSBS)."*
- **Consanguinity** is a recurrent risk context: a Saudi family with first-cousin parents (PMID:28250456) and a consanguineous Pakistani family (PMID:33141514).
- **Environmental, protective and gene–environment factors:** none reported. This is a monogenic developmental disorder.
- **Possible modifiers:** Jamuar et al. attribute the variable mirror movements to *"additional, as yet uncharacterized, background genetic modifier effects"*. This is speculation and is not established.

## 3. Phenotypes

The phenotypes below come from about 8 patients, so frequencies are qualitative. Rahikkala 2024 (PMID:38585553) summarizes them: *"HGPPS2 phenotype caused by biallelic DCC variants appears to be fully penetrant and shows a similar clinical presentation including developmental delay, intellectual disability, neuromuscular scoliosis, horizontal gaze palsy, agenesis of corpus callosum, and the absence of cerebral commissures."*

| Phenotype | Onset / course | Frequency | Suggested HPO **[verify]** | Key source |
|---|---|---|---|---|
| Horizontal gaze palsy (no conjugate horizontal eye movements) | congenital, stable | essentially all | Horizontal gaze palsy (HP:0000641?) / Ophthalmoplegia | 33141514, 28250456 |
| Progressive scoliosis | childhood to adolescence, progressive | essentially all | Progressive scoliosis / Scoliosis HP:0002650 | 33141514 |
| Global developmental delay | infancy | most | HP:0001263 | 28250456, 33141514 |
| Intellectual disability | childhood, static | most (one patient described as "modest") | HP:0001249 | 28250456 |
| Agenesis of the corpus callosum | congenital | all imaged | HP:0001274 | 28250456 |
| Absent anterior and hippocampal commissures | congenital | Family 1 and Pakistani family | Absent anterior commissure **[lookup]** | 28250456, 33141514 |
| Midline brainstem cleft, "butterfly" medulla, hypoplastic pons and midbrain | congenital | Families 1 and 2 | Pontine hypoplasia HP:0012110?; Brainstem dysplasia | 28250456 |
| Failed decussation of the superior cerebellar peduncles (no "red dot" sign); absent transverse pontine fibers | congenital | Family 2 (DTI) | **[no specific HPO; search]** | 28250456 |
| Probst bundles; widespread white-matter disorganization with low FA | congenital | Family 2 (DTI) | Abnormal cerebral white matter morphology | 28250456 |
| Mirror movements | — | **variable**: Family 1 proband only | Mirror movements HP:0001335? | 28250456 |
| Interhemispheric cyst | — | 1 patient (missense Family 3) | Interhemispheric cyst | 28250456 |

Supporting quotes:

- **Imaging, Family 1** (PMID:28250456): *"Pons and midbrain structures were hypoplastic, and there was a large midline cleft throughout the extent of the brainstem contributing to a butterfly shaped medulla."*
- **Tractography** (PMID:28250456): *"In place of the normal pattern of interdigitating callosal fibers, no commissural tracts were evident, either on tractography or FA maps."* The same paper adds that the disorganization *"was not limited to commissural fibers, but was strongly evident in associational and subcortical fibers as well."*
- **Mirror movements** (PMID:28250456): *"while the proband in Family 1 exhibited mirror movements, the affected individuals in Family 2 and 3 did not."*

**Quality of life:** no formal QoL instruments (EQ-5D, SF-36) have been reported. The functional burden comes from intellectual disability, the need for scoliosis care, and compensatory head movements for horizontal gaze. That last point is extrapolated from HGPPS1 **[unverified for HGPPS2]**.

## 4. Genetic / Molecular Information

**Causal gene:** DCC (hgnc:2701; OMIM 120470; 18q21.2). The gene has 29 exons and encodes a 1447-amino-acid, 159 kDa single-pass transmembrane protein of the immunoglobulin superfamily, with 4 Ig and 6 fibronectin type III repeats (PMID:29068161, PMID:28250456).

**Reported HGPPS2 alleles** (all homozygous):

| Family / origin | Variant | Class | Ref |
|---|---|---|---|
| 1, Mexico (2 boys) | 7,682 bp deletion removing the 3′ end of exon 1 (61 bp of coding sequence); RT-PCR shows exon 1 skipping | intragenic deletion; functional null | 28250456 |
| 2, Saudi Arabia | c.788_794delTTTCTGG, p.Val263Alafs*36 (exon 4, Ig3) | frameshift | 28250456 |
| 3 (ACC plus interhemispheric cyst cohort) | c.2071C>A, p.Gln691Lys (FN3 domain 3) | missense; possibly hypomorphic | 28250456 |
| Pakistan (3 sibs) | c.2399dupA, p.(Asn800Lysfs*11) (exon 16) | frameshift | 33141514 |
| Syria | c.(?_1912)_(2359_?)dup, p.(Ser788Tyrfs*4) | intragenic duplication | 38585553 |

- Count: *"three different homozygous pathogenic frameshift variants, one homozygous missense variant, and an intragenic duplication in the DCC gene have been reported in 8 patients"* (PMID:38585553).
- Family 1 deletion: *"Disruption of these features strongly predicts that this mutation represents a functional null."* (PMID:28250456)
- Possible genotype–phenotype gradient for Family 3: *"This finding suggests that weaker biallelic mutations in DCC may cause milder phenotypes, although additional cases will be required to confirm this."* (PMID:28250456)
- **Functional consequence:** loss of function. All variants are germline. ClinVar classifications and gnomAD frequencies were **not checked** in this session. The papers state the variants are absent from ExAC, EVS, dbSNP and 1000 Genomes.
- **Allelic disorders of the same gene** (relevant to counselling and differential diagnosis): monoallelic DCC variants cause congenital mirror movements (MRMV1, MIM 157600) and/or isolated ACC (MIM 217990), with incomplete penetrance (PMID:29068161). The LOVD locus database is https://databases.lovd.nl/shared/genes/DCC.
- **Copy-number testing:** two of the five alleles are CNVs. Rahikkala concludes: *"The analysis of duplications and deletions in the DCC should be included in the routine genetic diagnostic evaluation of patients with suspected HGPPS2."*
- **Epigenetic or chromosomal abnormalities:** none reported beyond the intragenic CNVs.

## 5. Environmental Information

None. There are no known environmental, lifestyle or infectious contributors. This section is not applicable.

## 6. Mechanism / Pathophysiology

**Causal chain**

1. Biallelic DCC loss-of-function variants (deletion, frameshift, duplication, or possibly hypomorphic missense) **lead to** absent or nonfunctional DCC receptor on growth cones of developing commissural axons. This is demonstrated at the RNA level for the exon-1 deletion and inferred for the other variants.
2. Loss of DCC **results in** failure to transduce netrin-1 midline attraction and long-range signalling (PMID:29068161). In the hindbrain and spinal cord, the DCC–ROBO3 complex that silences Slit repulsion is also lost (PMID:28250456: *"Robo3 forms a direct molecular complex with DCC that silences repulsion from Slits … and enhances attraction to Netrins"*). The human DCC–ROBO3 link is **inferred** from the overlap with HGPPS1 and from mouse work.
3. Commissural axons fail to cross the midline at every level of the neuraxis. This **leads to** branching consequences:
   - **3a. Forebrain:** agenesis of the corpus callosum and the anterior and hippocampal commissures. Probst bundles form instead.
   - **3b. Brainstem:** absent pontine crossing fibers and failed decussation of the superior cerebellar peduncles, producing the midline cleft or split pons and the butterfly medulla. The failure of crossing gaze pathways **results in** horizontal gaze palsy. The exact crossing tract has not been shown in humans; the authors write of *"shared brainstem crossing defects disrupting pathways controlling conjugate gaze"*.
   - **3c. Spinal cord:** defective left–right interneuron circuits are thought to **lead to** unbalanced paraspinal muscle activity and progressive scoliosis. The authors call this **speculative**: *"We speculate that scoliosis may pertain to unbalanced paraspinal muscle activity due to defective spinal interneuron circuits."* It is supported only by Netrin-1/Dcc-deficient mice.
   - **3d. Non-commissural white matter:** broad disorganization of associational and subcortical tracts with reduced FA. A possible additional role of DCC/netrin in oligodendrocyte myelin regulation is a hypothesis only. Together these probably **contribute to** intellectual disability and developmental delay (inferred: *"cognitive deficits may at least partially be attributable to non-commissural forebrain white matter abnormalities"*).
4. Corticospinal-tract laterality is variable. This **may result in** mirror movements in some patients. The mechanism is unclear; partial and complete loss of DCC may differ.

**Checklist detail (term IDs to verify)**

| Category | Detail | Suggested terms |
|---|---|---|
| Pathways | Netrin-1/DCC signalling; Slit/ROBO crosstalk | GO "netrin-activated signaling pathway"; "axon midline choice point recognition"; "axon guidance" GO:0007411 |
| Molecular function | Netrin receptor activity | GO:0005042 (already in the entry) |
| Cellular processes | Growth-cone guidance, commissural axon crossing, possibly myelination | GO "corpus callosum development"; "commissural neuron axon guidance" |
| Cell types | Commissural neurons; cortical (callosal) projection neurons; spinal commissural interneurons; possibly oligodendrocytes | CL search needed (e.g. CL:0000540 neuron is too broad; look for "commissural neuron") |
| Subcellular | Growth cone; plasma membrane | GO:0030426 growth cone |
| Metabolic, immune, omics | None reported; no transcriptomic, proteomic or single-cell data specific to the disease | — |

## 7. Anatomical Structures Affected

- **Primary:** CNS commissures, namely the corpus callosum, anterior commissure, hippocampal commissure, superior cerebellar peduncle decussation and transverse pontine fibers. Also the pons, midbrain and medulla oblongata.
- **Secondary:** the vertebral column (scoliosis) and extraocular motor control.
- **UBERON leads [verify]:** corpus callosum, anterior commissure, hippocampal commissure, pons, medulla oblongata, midbrain, superior cerebellar peduncle, cerebral white matter, vertebral column.
- **Laterality:** midline and bilateral by nature. Scoliosis direction is not described.

## 8. Temporal Development

- **Onset:** congenital. The malformation forms prenatally, and the gaze palsy is present from birth.
- **Progression:** scoliosis appears and worsens through childhood and adolescence (PMID:33141514). Cognitive and brain-structure features are static.
- **Duration:** lifelong. Remission is not applicable.
- **Critical periods:** scoliosis surveillance during the growth years. The window for commissure formation is embryonic, which is the axon-guidance window, inferred from mouse data.

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive (HP:0000007). The Pakistani family shows co-segregation: *"the parents were heterozygous carriers of the mutation, in accordance with an autosomal recessive inheritance pattern"* (PMID:33141514).
- **Penetrance:** described as full penetrance for biallelic loss of function (PMID:38585553). Heterozygous carriers are usually unaffected but are at risk of the allelic dominant conditions (mirror movements or isolated ACC) with incomplete penetrance.
- **Expressivity:** variable for mirror movements, and possibly milder with missense alleles.
- **Anticipation and germline mosaicism:** none reported.
- **Epidemiology:** about 8 patients and 5 families worldwide (Mexico, Saudi Arabia, Pakistan, Syria, and Family 3 of unstated origin). There is no prevalence or incidence figure. Use `CASES_IN_LITERATURE` with `ULTRA_RARE`.
- **Founder effects and carrier frequency:** unknown.
- **Sex ratio:** too few cases to estimate.

## 10. Diagnostics

**Brain MRI and DTI.** Look for the combination of agenesis of the corpus callosum, absent anterior and hippocampal commissures, a split pons, a butterfly medulla, and an absent midbrain "red dot". That combination with horizontal gaze palsy and intellectual disability points to DCC rather than ROBO3.

**Genetic testing.**
- Exome or genome sequencing plus **CNV analysis of DCC**, which is mandatory because 2 of 5 alleles are CNVs.
- Targeted DCC sequencing with ddPCR/qPCR for deletions or duplications.
- Homozygosity mapping helps in consanguineous families. For example, the Pakistani family had loss of heterozygosity at 18q21.1–21.3 (PMID:33141514).

**Other tests.** Orthoptic and ocular-motility examination; spine radiographs; developmental assessment.

**Differential diagnosis**

| Condition | Distinguishing features |
|---|---|
| HGPPS1 (ROBO3, MIM 607313) | Normal intellect, no ACC. PMID:38516134: *"HGPPS2 … distinguished from HGPPS1 by impaired intellectual development, global developmental delay, agenesis of the corpus callosum, and absence of the anterior and hippocampal commissures."* |
| Joubert syndrome | Molar-tooth sign, oculomotor apraxia **[clinical knowledge]** |
| Möbius and Duane syndromes (other congenital cranial dysinnervation disorders) | — |
| Isolated ACC | — |
| Pontine tegmental cap dysplasia | — |

**Screening:** no newborn or population screening. Cascade carrier testing and prenatal or preimplantation testing are possible once the familial variants are known.

## 11. Outcome / Prognosis

- No survival or mortality data. The affected patients reported were alive in childhood to young adulthood; the Pakistani family included adolescents and adults, per MeSH age tags.
- Morbidity comes from intellectual disability, progressive scoliosis (which may need surgery), and the gaze limitation.
- No prognostic biomarkers. The only proposed modifier of severity is allele type (null versus missense), and that is unproven.

## 12. Treatment

There is no disease-modifying therapy, no trial, and no pharmacogenomics. Management is supportive and draws on HGPPS1 and scoliosis practice **[no HGPPS2-specific outcome data]**.

| Intervention | Suggested NCIT term (verify) |
|---|---|
| Scoliosis bracing and spinal fusion (orthopedic surgery) | Orthopedic Surgical Procedure NCIT:C16186; therapeutic modality SURGERY |
| Physical, occupational and speech therapy; special education for developmental delay | Physical Therapy NCIT:C15302; Rehabilitation NCIT:C15315 |
| Strabismus or ophthalmologic management | — |
| Genetic counselling | NCIT:C15240 |

No gene therapy, ASO or cell therapy has been developed.

## 13. Prevention

- **Primary:** none.
- **Secondary and tertiary:** spine surveillance through growth to allow early scoliosis intervention; developmental surveillance.
- **Counselling:** 25% recurrence risk for carrier couples. Discuss carrier testing in consanguineous families and prenatal or preimplantation testing. Note the separate dominant risk to heterozygous relatives (mirror movements or isolated ACC).

## 14. Other Species / Natural Disease

- No naturally occurring animal disease is known. OMIA was not searched **[unverified]**.
- DCC and netrin signalling is conserved from *C. elegans* (*unc-40*) and *Drosophila* (*frazzled*) to vertebrates. PMID:28250456 calls the pathway *"evolutionarily conserved from C. elegans through vertebrates"*.

## 15. Model Organisms

**Dcc knockout mouse.** Fazeli et al. 1997, *Nature* 386:796–804, **PMID:9126737**. The PMID comes from a web search and is not cached; run `just fetch-reference PMID:9126737` before citing.
- Inactivating Dcc caused axonal-projection defects resembling those in netrin-1-deficient mice and had no intestinal tumour phenotype.
- Jamuar notes that Netrin-1 and DCC knockout mice *"are also acallosal"*.
- **Recapitulates:** forebrain commissure agenesis.
- **Limitations:** perinatal lethality is commonly reported **[unverified]**, which limits study of scoliosis and cognition. Brainstem crossing defects are *"less consistently predicted from animal studies"* (PMID:28250456).
- Fidelity: high for ACC, low or unknown for gaze palsy and scoliosis.

**Netrin-1–deficient mice.** These show disrupted spinal left–right interneuron circuits and are the basis of the scoliosis hypothesis (PMID:28250456, refs 29–30; primary PMIDs **[not retrieved]**).

**Zebrafish *dcc* mutants.** These show hindbrain startle-circuit abnormalities (PMID:28250456; primary PMID **[not retrieved]**).

**Kanga (Dcc^kanga) mouse.** A spontaneous allele that removes the P3 intracellular domain and causes corticospinal and spinal midline defects with a hopping gait. This is a **[lead, unverified]**.

**Other systems:** no iPSC or organoid model of HGPPS2 has been reported.

---

## Gaps and recommendations for curation

1. Fetch and cite PMID:9126737 for the mouse model. Search for primary PMIDs for the Netrin-1 interneuron, zebrafish and kanga papers.
2. Look up every HPO, GO, CL, UBERON and NCIT term listed above. None were checked in this session because the OLS connector needs authorization.
3. No case reports after 2024 were found in a standard web search. The count of about 8 patients is current as of PMID:38585553.
4. The mechanism behind scoliosis and the specific gaze-pathway tract are hypotheses. Model them with `directness: INDIRECT` or as an `EMERGING` mechanistic hypothesis rather than as established edges.
5. The existing KB entry, `kb/disorders/Gaze_Palsy_Familial_Horizontal_With_Progressive_Scoliosis_2.yaml`, already cites five of the six references above.

**Sources**
- Jamuar et al. 2017, PMID:28250456 — https://www.nature.com/articles/ng.3804.pdf
- Rahikkala et al. 2024, PMID:38585553 — https://www.utupub.fi/items/21c918e6-1e57-4076-bbcd-562f429bd836/full ; https://oulurepo.oulu.fi/handle/10024/48657 ; https://research.utu.fi/converis/portal/detail/Publication/380543436
- Zaka et al. 2021, PMID:33141514 (cached abstract)
- Marsh et al. 2018, PMID:29068161 (cached)
- Xie et al. 2024, PMID:38516134 (cached)
- Jen et al. 2004, PMID:15105459 (cached)
- Fazeli et al. 1997, PMID:9126737 — https://www.nature.com/articles/386796a0 ; https://pesquisa.bvsalud.org/ses/resource/es/mdl-9126737 ; https://wi.mit.edu/news/deleted-colorectal-cancer-dcc-gene-plays-role-wiring-mouse-brain-and-spinal-cord

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 7 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0054602` (1 mention) - the report calls it "MONDO"; MONDO calls it **gaze palsy, familial horizontal, with progressive scoliosis, 2**
- `HP:0001263` (1 mention) - the report calls it "most"; HP calls it **Global developmental delay**
- `HP:0001249` (1 mention) - the report calls it "most (one patient described as "modest")"; HP calls it **Intellectual disability**
- `GO:0005042` (1 mention) - the report calls it "already in the entry"; GO calls it **netrin receptor activity**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001274` (1 mention) - the report calls it "all imaged"; HP calls it **Agenesis of corpus callosum**, and lists "Callosal agenesis" among its other names
- `NCIT:C15240` (1 mention) - the report calls it "Genetic counselling"; NCIT calls it **Genetic Counseling**
