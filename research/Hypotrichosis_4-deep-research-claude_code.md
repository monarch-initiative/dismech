---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-07T22:07:27.267545'
end_time: '2026-09-07T22:12:40.955537'
duration_seconds: 313.69
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Hypotrichosis 4
  mondo_id: MONDO:0100522
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
  num_turns: 19
  total_cost_usd: 1.2963763999999998
  session_id: 8e6a3453-99e0-563b-8e2c-3bcb30d1c949
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 26
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 10
  validator_version: 0.2.1
term_validation:
  total_terms: 16
  verified: 9
  not_found: 0
  obsolete: 2
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 5
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0002293
    reported_labels:
    - Hypotrichosis
    ontology_label: Alopecia of scalp
  obsolete_terms:
  - term_id: MONDO:0007806
    ontology_label: obsolete hypotrichosis 4
    replaced_by: MONDO:0100522
  - term_id: GO:0070577
    ontology_label: obsolete lysine-acetylated histone binding
    replaced_by: GO:0140566
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
- **Disease Name:** Hypotrichosis 4
- **MONDO ID:** MONDO:0100522 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypotrichosis 4** covering all of the
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

I'll research Hypotrichosis 4 using web search to verify identifiers, gene associations, and clinical details before writing the report.

# Hypotrichosis 4 (HYPT4 / Marie Unna Hereditary Hypotrichosis 1) — Research Report

## 0. Identity and Naming Disambiguation (read first)

"Hypotrichosis 4" (**HYPT4**, OMIM **#146550**) is the numbered-series name for **Marie Unna Hereditary Hypotrichosis 1 (MUHH1)**, first clinically described by Marie and Unna in a German family in 1925 [Nature Genetics 41:228–233, PMID:19122663]. It is **not** the same disease as the LIPH-related or LPAR6-related autosomal-recessive woolly-hair/hypotrichosis entries that also carry "Hypotrichosis N" numbers in OMIM's series (those are clinically and genetically distinct recessive disorders with kinky/woolly rather than wiry hair). Within the same clinical entity, there is **locus heterogeneity**: MUHH1 (HYPT4, chromosome 8p21.3, gene *HRURF*/historically "*U2HR*") is the classic and most common form; a second, minor form, **MUHH2 (HYPT5, OMIM #612841)**, is caused by heterozygous missense mutation in **EPS8L3** (chromosome 1p13.3) in a single reported Chinese family [escholarship.org/uc/item/6pf0m22z; PMID:24236410]. This report focuses on HYPT4/MUHH1 as specified by MONDO:0100522, and flags MUHH2 only as a lump/split-relevant sibling locus — subsequent sequencing studies in other MUHH families found no EPS8L3 mutations, indicating it is a minor/rare cause [PMID:24236410].

**Key identifiers:**
- OMIM: **#146550** (HYPOTRICHOSIS 4; HYPT4) — [omim.org/entry/146550](https://omim.org/entry/146550)
- Gene/locus: **HRURF** (HR Upstream Reading Frame; formerly designated *U2HR*), OMIM gene entry **\*619257**, HGNC:55085, chromosome 8p21.3, embedded in the 5′-untranslated region of the *HR* gene (HR Lysine Demethylase and Nuclear Receptor Corepressor, OMIM \*602302, HGNC:5172)
- Orphanet: **ORPHA444** — [orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=444](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=444)
- MONDO: MONDO:0100522 (as specified in the target; note MONDO:0007806 appeared adjacent in search results and should be checked for obsolescence/merge status against the current MONDO release before binding)
- Synonyms: Marie Unna Hereditary Hypotrichosis 1 (MUHH1); Marie Unna Congenital Hypotrichosis; Hypotrichosis Congenita
- Inheritance: Autosomal dominant, full penetrance with variable expressivity (see §9)

---

## 1. Disease Information

MUHH1/HYPT4 is a rare autosomal dominant hair disorder with a distinctive triphasic natural history: **absent or sparse hair at birth**, replaced in infancy/childhood by **coarse, wiry, unruly scalp hair**, followed by **progressive patterned hair loss beginning around puberty** that can proceed to near-total alopecia in adulthood [Orphanet ORPHA444; PMID:19122663]. Eyebrows, eyelashes, and body/pubic/axillary/beard hair are sparse to absent from early life onward, distinguishing it from isolated androgenetic alopecia [Orphanet ORPHA444].

Approximately 30 families and sporadic cases with a molecular diagnosis have been reported in the literature to date [Orphanet ORPHA444], spanning German (the original 1925 kindred, molecularly resolved by PMID:20659777), Chinese [PMID:26269244], Turkish, and other ethnic backgrounds — indicating the disorder is panethnic rather than population-restricted.

All information below is derived from **aggregated disease-level resources** (OMIM, Orphanet, GeneReviews-style literature reviews) and **case series/family reports** in the primary literature — there is no large EHR/registry cohort for this rare Mendelian disorder.

---

## 2. Etiology

### Disease Causal Factors
HYPT4 is a purely **genetic** (monogenic, Mendelian) disorder. There is no established environmental, infectious, or acquired contributing mechanism — the phenotype is present from birth and driven entirely by a *cis*-regulatory germline mutation (see §4, §6).

### Genetic Risk Factors
- **Causal**: Heterozygous loss-of-function mutations in *HRURF*/*U2HR*, a small inhibitory upstream open reading frame (uORF) located in the 5′-UTR of the *HR* transcript [PMID:19122663]. Every reported mutation is a **gain-of-function at the level of HR protein output** achieved through **loss of function of the inhibitory uORF peptide** — see §4/§6 for the precise mechanism.
- No susceptibility loci, polygenic risk, or modifier-gene data are available for HYPT4; the disorder behaves as a fully penetrant single-gene trait.
- **Locus heterogeneity**: a minority of MUHH families instead carry EPS8L3 mutations (MUHH2/HYPT5, OMIM #612841) [PMID:24236410] — genetically distinct but phenotypically overlapping.

### Environmental Risk Factors
None established. Age and sex are not risk-modifying (both sexes affected equally per Orphanet); disease onset (birth/infancy) precedes any plausible environmental exposure window.

### Protective Factors
None reported in the genetic or environmental literature. No protective variant or exposure has been described for this gene.

### Gene-Environment Interactions
None reported. The disorder's fully penetrant, congenital-onset Mendelian pattern leaves little described room for environmental modulation of penetrance, though the well-documented **variable expressivity between and within families** (see §9) suggests unidentified modifiers (genetic or environmental) affect severity — this is an open question, not something directly evidenced.

---

## 3. Phenotypes

| Phenotype | Type | Onset | Frequency | Suggested HPO term |
|---|---|---|---|---|
| Sparse/absent scalp hair at birth | Physical sign | Congenital | Nearly universal | HP:0008070 (Sparse hair) — verify against HPO browser before binding |
| Coarse, wiry, unruly scalp hair in childhood | Physical sign/hair-shaft abnormality | Infancy–childhood | Nearly universal (defining feature) | Candidate: "Coarse hair" (HP term exists in the Abnormality of hair texture branch — verify exact CURIE via OAK before curation) |
| Progressive patterned scalp hair loss | Physical sign, progressive | Onset at/after puberty | Nearly universal, progresses with age | HP:0002293 (Hypotrichosis) or a more specific "progressive alopecia" descriptor — verify |
| Sparse/absent eyebrows | Physical sign | Congenital/infancy | All affected individuals per Orphanet | Candidate "Sparse eyebrow" term — verify CURIE |
| Sparse/absent eyelashes | Physical sign | Congenital/infancy | All affected individuals per Orphanet | Candidate "Sparse eyelashes" term — verify CURIE |
| Sparse/absent body, axillary, pubic, beard hair | Physical sign | Peripubertal | All affected individuals per Orphanet | Related to HP:0002215 (Sparse axillary hair) family of terms — verify per-site CURIEs |
| Follicular hyperkeratosis with milia-like facial papules | Physical sign/histopathologic finding | Variable, often childhood–adulthood | Reported in a substantial minority; not universal | Candidate keratosis-pilaris-adjacent HP term — verify; this is a distinguishing feature from simple androgenetic alopecia |
| Hair shaft abnormalities: increased/variable diameter (up to 0.12 mm), twisting, bending at odd angles, longitudinal grooving, cuticle peeling (on SEM) | Laboratory/microscopic finding | Present once hair grows in (childhood onward) | Consistently described across case series | Relates to "Pili torti"/hair-shaft-abnormality branch of HPO — a specific match should be confirmed rather than assumed |

**Characteristics:**
- **Age of onset**: Congenital (present from birth) — the sparse-hair phase is neonatal; the wiry-hair phase is early childhood; progressive loss begins peripubertally.
- **Severity**: Variable — ranges from a fringe of tonsorial-pattern hair remaining in adulthood to near-total scalp alopecia; eyebrow/eyelash/body-hair sparseness is comparatively more uniform in severity across patients.
- **Progression**: Progressive after puberty; scalp involvement typically worsens with age, described as advancing "until only a sparse fringe in the tonsorial distribution remains" [Orphanet ORPHA444].
- **Frequency**: Core triad (sparse birth hair → wiry childhood hair → progressive scalp loss with sparse eyebrows/eyelashes/body hair) is present in essentially all molecularly confirmed cases; follicular hyperkeratosis/milia-like papules are a variable, not universal, accessory feature [PMC4212298].

**Quality of life impact**: No disease-specific EQ-5D/SF-36 data were found in the literature searched. The condition is not associated with reduced survival, systemic organ involvement, or intellectual disability — QoL impact is inferred to be primarily psychosocial/cosmetic (a lifelong, progressive, visible hair disorder from birth), consistent with general literature on congenital hypotrichoses, but this inference is not directly sourced to a validated QoL instrument study in HYPT4 specifically.

---

## 4. Genetic/Molecular Information

### Causal Gene
- ***HRURF*** (previously annotated as *U2HR*, "upstream open reading frame 2 of *HR*"), OMIM gene **\*619257**, HGNC:55085, chromosome 8p21.3. Located within the 5′-UTR of the *HR* gene transcript.
- The disease-causing gene was mapped to 8p21 by linkage in 2000 [Lefèvre et al., Eur J Hum Genet, PMID:10854110, LOD 8.26 at D8S1786], refined to a 1.1-cM interval in 2004 [PMID:15149494], and the causal gene was identified in 2009 when Wen et al. showed that the pathogenic mutations lay not in the *HR* coding sequence itself (previously excluded) but in a small **inhibitory upstream ORF (uORF)** overlapping the *HR* 5′-UTR [Nat Genet, PMID:19122663].

### Pathogenic Variants
- **Affected gene/product**: *U2HR*/*HRURF* is predicted to encode a highly conserved **34–amino acid peptide** (not the HR protein itself) [PMID:19122663].
- **Variant classes reported**: loss-of-initiation-codon mutations, delayed/read-through termination-codon mutations, nonsense mutations, and missense mutations within the small uORF — all of which converge functionally on **loss of the uORF's translational-repressor activity** [PMID:19122663; search summary of subsequent Chinese/Turkish family reports].
- **Functional consequence**: These are **gain-of-function mutations at the level of downstream HR protein expression** — loss of the inhibitory uORF removes translational repression of the main *HR* open reading frame, resulting in **increased HR protein levels**, i.e., a dose-sensitivity ("just right" amount of HR corepressor) mechanism rather than classic HR loss-of-function (contrast with atrichia with papular lesions/alopecia universalis congenita, caused by biallelic *HR* coding loss-of-function — see §6, §14).
- **Origin**: Germline, autosomal dominant; recurrent/founder-like variants have been reported across multiple ethnically distinct families (German original-1925 kindred [PMID:20659777], Chinese families [PMID:26269244], and others), consistent with mutational hotspots within this small uORF rather than a single global founder haplotype.
- **Allele frequency**: No population allele-frequency data (gnomAD, etc.) were retrieved for specific *HRURF* pathogenic alleles in this search; given the rarity of the disease (~30 molecularly confirmed families worldwide) and dominant fully penetrant inheritance, pathogenic alleles would be expected to be absent or vanishingly rare in population reference databases — this should be confirmed per-variant in gnomAD before curation rather than assumed.

### Modifier Genes
None established. The variable expressivity of scalp-loss severity between affected relatives carrying the same mutation (see §9) implies unidentified modifiers, but no specific modifier gene has been reported.

### Epigenetic Information
No disease-specific DNA methylation, histone modification, or chromatin studies in HYPT4 patient tissue were identified in this search. Mechanistically, the *downstream* consequence of the mutation (increased HR corepressor levels) itself alters chromatin state at nuclear-receptor target genes via HR's histone-deacetylase-recruiting corepressor activity (see §6) — this is a molecular mechanism, not a patient-epigenome finding.

### Chromosomal Abnormalities
None reported; HYPT4 is caused by point/small-indel mutations, not by large structural chromosomal rearrangements.

---

## 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents have been implicated as causal or modifying for HYPT4 in the literature searched. This is consistent with its status as a fully penetrant monogenic disorder with congenital onset.

---

## 6. Mechanism / Pathophysiology

### Causal chain (ordered)

1. A heterozygous germline mutation disrupts the small inhibitory upstream open reading frame (**U2HR/*HRURF***) in the 5′-UTR of the ***HR*** transcript — loss of the initiation codon, a delayed/read-through termination codon, or a nonsense/missense change within the 34-aa uORF peptide [PMID:19122663]. *(Molecular lesion.)*
2. This **leads to** loss of the uORF peptide's normal translational-repressor function on the downstream, in-frame main *HR* ORF — ribosomes that would normally stall/re-initiate poorly after translating the short uORF instead proceed efficiently to translate full-length HR protein [PMID:19122663]. *(Directly demonstrated — the founding paper shows increased HR expression from mutant uORF constructs.)*
3. This **results in** increased steady-state levels of the HR protein — HR Lysine Demethylase and Nuclear Receptor Corepressor — in hair-follicle keratinocytes and other HR-expressing tissue [PMID:19122663; genesdev.cshlp.org/content/15/20/2687].
4. Excess HR protein **leads to** exaggerated corepressor activity at nuclear-receptor target genes. HR is a nuclear-localized transcriptional corepressor that binds directly to the **vitamin D receptor (VDR)**, and also represses **thyroid hormone receptor (TR)** and **retinoic-acid-receptor-related orphan receptor-α (RORα)**, by recruiting histone deacetylases (HDACs) and by intrinsic histone-demethylase activity, driving chromatin remodeling that silences VDR/TR/RORα target genes [PMID:12847098 (Physical and functional interaction between VDR and hairless corepressor); Endocrinology 150:4950 (isoform-specific VDR modulation); genesdev.cshlp.org/content/15/20/2687]. *(Demonstrated in cell/biochemical and mouse systems — an inference step when extrapolated to the specific human HYPT4 hair follicle, i.e., indirect evidence for the human disease mechanism.)*
5. Excessive/dysregulated repression of VDR/TR/RORα target-gene transcription **disrupts** the normal transcriptional program that HR and VDR jointly execute during the **catagen-to-telogen and telogen-to-anagen transitions of the postnatal hair cycle** — both HR loss-of-function and VDR loss-of-function independently cause total alopecia in mice and humans, establishing that *correctly dosed* HR/VDR corepressor activity, not simply "more or less," is required for normal cycling [PMID:12847098; Sci Rep, "Molecular evolution of HR", PMC3216519]. *(This step is inferred from parallel HR/VDR loss-of-function biology; direct demonstration that HR gain-of-function specifically disrupts this transition in human MUHH1 follicles has not been shown at the molecular level — flagged as inferred rather than demonstrated in patients.)*
6. Failure of the hair follicle to complete normal cycling **manifests clinically** as an unstable, progressively degenerating follicular program: normal follicles at birth transiently produce structurally abnormal (coarse, twisted, variable-diameter) hair shafts in childhood, and then, beginning at puberty (a period of major systemic hormonal/nuclear-receptor signaling change), follicles progressively fail to re-enter productive anagen, causing patterned, progressive alopecia together with sparse eyebrows/eyelashes/body hair [Orphanet ORPHA444; PMID:19122663]. *(Clinical manifestation — directly observed; the precise cellular step at which follicles fail, e.g., stem-cell-niche exhaustion vs. premature catagen entry, has not been isolated in human tissue in the sources reviewed.)*
7. Branch — accessory/variable feature: in a subset of patients, disordered follicular keratinization also produces **follicular hyperkeratosis with milia-like facial papules**, histologically distinct from classic keratosis pilaris (which shows epidermal hyperkeratosis/hypergranulosis/follicular plugging from a different, non-HR-driven process) [PMC4212298; comparison search]. The mechanistic link from HR dosage to this keratinization phenotype specifically is not detailed in the sources reviewed and should be treated as an open question rather than an established step in the chain.

### Molecular pathways
The operative pathway is **nuclear-receptor corepressor signaling**: HR–VDR, HR–TR (thyroid hormone receptor), and HR–RORα axes, converging on HDAC recruitment and chromatin remodeling at target promoters controlling the hair cycle [PMID:12847098; genesdev.cshlp.org/content/15/20/2687]. Suggested GO terms: **GO:0003714** (transcription corepressor activity); **GO:0070577** (lysine-histone demethylase activity, if using HR's demethylase function); **GO:0042633** (hair cycle) — verify exact CURIEs before binding.

### Cellular processes
Disrupted terminal differentiation/keratinization program of the hair follicle outer root sheath and matrix keratinocytes; disrupted hair-cycle-phase transitioning (anagen–catagen–telogen). No apoptosis, autophagy, or classic inflammatory-cascade mechanism is centrally implicated by the sources reviewed, though mild inflammatory infiltrate around reduced follicle numbers has been noted histologically [search: histopathology summary].

### Protein dysfunction
This is fundamentally a **dosage/gain-of-expression** disorder rather than a structural protein-misfolding disorder: the mutant uORF peptide loses its own inhibitory function, and the downstream consequence is **excess of an otherwise wild-type HR protein**, not a structurally altered HR protein. This is mechanistically distinct from *HR*-coding-region loss-of-function mutations that cause atrichia with papular lesions/alopecia universalis congenita (§14).

### Metabolic changes
None specifically reported for HYPT4.

### Immune system involvement
Not centrally implicated; mild perifollicular inflammatory infiltrate has been described histologically but is not characterized as a primary immune-mediated mechanism [search: histopathology summary; PMC4212298 for full histopathology detail — should be read directly before asserting further specifics].

### Tissue damage mechanisms
Progressive follicular miniaturization/loss with reduced follicle density; no fibrosis or scarring is described, consistent with a **non-scarring alopecia** [search: histopathology summary].

### Biochemical abnormalities
Increased HR corepressor protein dosage (see causal chain step 3) is the core molecular lesion; no enzyme-deficiency or ion-channel-defect mechanism applies here.

### Molecular profiling / advanced technologies
No transcriptomic, proteomic, metabolomic, lipidomic, single-cell, or spatial-transcriptomic datasets specific to HYPT4 patient hair follicles were identified in this search (GEO/ArrayExpress/Human Cell Atlas were not directly queried with disease-specific hits returned). This is a gap — human hair-follicle multi-omic characterization of HYPT4 has apparently not been published, or was not surfaced by this search; this should be explicitly stated as **absent evidence**, not silently omitted, in any downstream curation.

**Suggested cell types (CL) and anatomical terms (UBERON)**: hair follicle outer root sheath cell, hair matrix keratinocyte, hair follicle dermal papilla cell — exact CL CURIEs should be selected and verified via OAK rather than guessed here.

---

## 7. Anatomical Structures Affected

- **Organ level**: Primary — **skin/integumentary system**, specifically the pilosebaceous unit (hair follicles) of the scalp, eyebrows, eyelashes, and body/pubic/axillary/beard sites. No other organ system involvement is reported for HYPT4 (contrast with some *HR*-coding mutations, which have been associated in isolated case reports with additional findings — see §14 caveat).
- **Tissue/cell level**: Hair follicle epithelium (outer root sheath, matrix), hair shaft cuticle/cortex (structurally abnormal — twisted, variable-diameter, grooved shafts visible by SEM) [search: histopathology summary].
- **Subcellular level**: Nuclear — HR protein and its VDR/TR/RORα corepressor complexes act in the nucleus of follicular keratinocytes; relevant GO Cellular Component term candidates include **GO:0005634** (nucleus) and a nuclear-receptor-corepressor-complex term — verify exact CURIE.
- **Localization**: Diffuse across scalp, eyebrows, eyelashes, and body-hair-bearing skin; scalp involvement is patterned (tonsorial-distribution-sparing in advanced disease, similar in distribution to androgenetic alopecia) [Orphanet ORPHA444]. Bilateral/symmetric, not lateralized.

---

## 8. Temporal Development

- **Onset**: Congenital — sparse/absent hair present at birth. Onset of the coarse-wiry-hair phase is early infancy/childhood. Onset of progressive hair *loss* is peripubertal.
- **Onset pattern**: Insidious/progressive rather than acute, across three sequential clinical phases (sparse at birth → coarse in childhood → progressive loss from puberty).
- **Progression**: Continuous, generally worsening with age into adulthood; not staged by a formal clinical staging system in the sources reviewed. Progression rate is described qualitatively as gradual, with severity plateauing to "a sparse fringe in the tonsorial distribution" in the most advanced cases rather than complete universal alopecia [Orphanet ORPHA444].
- **Course pattern**: Progressive, not episodic or relapsing-remitting; no spontaneous remission is described.
- **Duration**: Chronic and lifelong — no reported spontaneous resolution.
- **Critical periods**: Puberty is repeatedly identified across sources as the key inflection point for onset of hair loss, plausibly reflecting interaction with the pubertal hormonal/nuclear-receptor signaling milieu acting on an already HR-dysregulated follicle — this link is suggested by the coincidence of timing across the literature but is not mechanistically proven in the sources reviewed.

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence/incidence**: Unknown/not formally estimated; Orphanet explicitly states prevalence and incidence are unknown, with "approximately 30 families and sporadic cases" molecularly reported worldwide [Orphanet ORPHA444]. This should be curated as `prevalence_class: NOT_YET_DOCUMENTED` with `measure_type: CASES_IN_LITERATURE` per the dismech prevalence-modeling convention, rather than assigning a numeric rate.

### Inheritance
- **Pattern**: Autosomal dominant [OMIM #146550; Orphanet ORPHA444].
- **Penetrance**: Described in the literature as effectively complete (all mutation carriers manifest some degree of the phenotype), though this report did not retrieve a formal penetrance-percentage study; this should be verified against GeneReviews/ClinGen-style sources before asserting "complete" with high confidence.
- **Expressivity**: **Variable** — severity of scalp hair loss (from a mild receding pattern to near-total alopecia) differs between and within affected families carrying comparable mutations [general theme across case reports, e.g., PMC12646977, PMC4212298].
- **Genetic anticipation**: Not reported.
- **Germline mosaicism**: Not specifically reported for this gene, though the diversity of independently arising uORF mutations across families suggests standard germline transmission rather than a single ancestral mutation being propagated by mosaicism.
- **Founder effects**: No single global founder mutation has been established; distinct pathogenic uORF variants have been independently identified in German, Chinese, and Turkish (among other) families, consistent with a hotspot-mutable small regulatory element rather than one founder haplotype [PMID:20659777; PMID:26269244].
- **Consanguinity**: Not a relevant risk factor for this autosomal *dominant* disorder (in contrast to the *recessive* LIPH/LPAR6 hypotrichoses).
- **Carrier frequency**: Not applicable in the classic sense (dominant, not silent-carrier disease); no population carrier-frequency data located.

### Population demographics
- **Affected populations**: Reported across multiple ethnic backgrounds (German, Chinese, Turkish, and others per Orphanet's "various ethnic backgrounds" note) — no population enrichment identified.
- **Geographic distribution**: No endemic or regionally clustered distribution reported; cases are globally sporadic/familial.
- **Sex ratio**: Reported as affecting both sexes, without a stated skew (autosomal, non-sex-linked inheritance is consistent with this).
- **Age distribution**: All affected individuals are, by definition, affected from birth; clinical presentation/severity distribution shifts with age due to the three-phase natural history (see §8).

---

## 10. Diagnostics

### Clinical tests
- **Laboratory tests**: No disease-specific biochemical or enzymatic assay exists; routine labs are not diagnostic.
- **Biomarkers**: None established.
- **Imaging**: Not routinely used; not a structural/organ-imaging diagnosis.
- **Biopsy/histopathology**: Scalp biopsy can show reduced follicle numbers with mild-to-moderate inflammatory infiltrate, **without fibrosis or scarring**, sometimes with diffuse follicular hyperkeratosis and milia-like facial lesions [PMC4212298; search summary]. **Hair shaft microscopy/SEM** is diagnostically supportive: shafts of increased and variable diameter (up to 0.12 mm), deeply pigmented, twisted, bent at odd angles, with longitudinal grooving and cuticle peeling [search: clinical-features summary; PMC4212298 for the full large-pedigree description].

### Genetic testing
- **Recommended approach**: Molecular confirmation via sequencing of the small *HRURF*/*U2HR* uORF region in the *HR* 5′-UTR — a single-gene/targeted-region test given the small size of the causal element, though it may be captured incidentally on hair-loss/ectodermal-dysplasia gene panels or WES/WGS depending on annotation of this UTR-embedded ORF (note: because *HRURF* is a small uORF and only relatively recently (2009) recognized as a distinct causal element, older *HR*-only coding-sequence panels/tests would miss these mutations — a clinically important pitfall) [PMID:19122663].
- **WES/WGS utility**: Useful if the *HRURF* uORF region is specifically annotated/captured; historically several "novel loci"/negative-sequencing reports in MUHH families reflect exactly this annotation gap (e.g., a WES study reporting "a novel loci of the HR gene," IJDVL) — should be read directly for detail before citing further.
- **Single-gene testing**: *HRURF* uORF sequencing is the direct confirmatory test once MUHH1 is clinically suspected.
- **CMA/karyotype/FISH/mitochondrial/repeat-expansion testing**: Not applicable — this is a small point-mutation/indel disorder in a discrete non-coding regulatory element, not a structural, mitochondrial, or repeat-expansion disease.

### Omics-based diagnostics
Not part of routine or reported diagnostic practice for this disorder based on the sources reviewed.

### Clinical criteria
No formal DSM/ICD/society-published diagnostic-criteria checklist was identified; diagnosis rests on the characteristic triphasic clinical history (sparse birth hair → coarse childhood hair → progressive peripubertal loss) plus family history consistent with autosomal dominant inheritance, supported by hair-shaft microscopy and confirmed by *HRURF* sequencing.

**Differential diagnosis** (distinguishing features):
- **Atrichia with papular lesions / Alopecia universalis congenita** (biallelic *HR* coding loss-of-function; autosomal recessive; complete, permanent, non-regrowing alopecia from infancy without the intervening coarse-hair phase) [genesdev.cshlp.org/content/15/20/2687].
- **Autosomal recessive woolly hair/hypotrichosis** (LIPH, LPAR6/P2RY5, KRT25, C3ORF52 — recessive, kinky/woolly rather than wiry hair) [search: LIPH summary].
- **Keratosis pilaris / keratosis pilaris atrophicans faciei** (distinct histology: epidermal hyperkeratosis/hypergranulosis/follicular plugging without the hair-density/hair-shaft phenotype of HYPT4) [search: KP comparison].
- **MUHH2/HYPT5** (EPS8L3-related; phenotypically similar but genetically distinct — OMIM #612841) [PMID:24236410].
- **Androgenetic alopecia** (much later onset, no congenital sparse-hair or coarse-wiry-hair phase, no eyebrow/eyelash involvement).

### Screening
No population or newborn screening program exists for this ultra-rare dominant disorder; case-finding is via clinical recognition and, once a family mutation is known, cascade testing of at-risk relatives is appropriate (standard practice for a dominant Mendelian trait, though not explicitly documented in the sources reviewed as a formal cascade-screening protocol for this specific gene).

---

## 11. Outcome/Prognosis

- **Survival/mortality**: Not a life-limiting condition; no mortality or reduced-life-expectancy data are relevant, as HYPT4 has no reported systemic/visceral organ involvement.
- **Morbidity/function**: Purely a hair/integumentary phenotype; no functional organ impairment reported. Presumed psychosocial/cosmetic morbidity given the visible, progressive, lifelong nature of the condition, though no disease-specific QoL instrument study was located in this search (flagged as absent evidence, not asserted).
- **Complications**: Follicular hyperkeratosis/milia-like facial papules in a subset of patients (§3) is the main reported "complication"-adjacent finding beyond the core hair phenotype; no infections, organ failure, or other systemic complications reported.
- **Recovery potential**: The natural course is progressive rather than self-limited; treatment (§12) can partially restore hair density/regrowth in some patients but does not reverse the underlying follicular dysregulation, and effects are reported to be treatment-dependent (regrowth plateaus/reverses on discontinuation of topical minoxidil in the one reported pediatric case) [PMC12340736].
- **Prognostic factors**: No formal prognostic-biomarker or severity-predictor study was identified; clinical severity appears to vary by family/individual (variable expressivity, §9) without an established predictor.

---

## 12. Treatment

**Current status: no disease-modifying or targeted (mutation-correcting) therapy exists; management is symptomatic** [search: treatment summary].

### Pharmacotherapy
- **Topical minoxidil 5%**: The best-documented intervention. A 2025 case report describes a 4-year-old girl with a recurrent *HRURF* variant treated with once-daily 5% topical minoxidil, achieving significant scalp hair density/regrowth improvement by 12 weeks, further improvement at 6 months, with **regression on discontinuation and resumption of growth on restarting** — supporting a maintenance-dependent pharmacologic effect rather than a cure [J Cosmet Dermatol 2025, PMID pending confirmation via PMC12340736 — DOI: 10.1111/jocd.70382]. Proposed mechanism: minoxidil promotes anagen entry and prolongs follicular activity, plausibly counteracting the disrupted hair-cycle transition described in §6, though this is inferred general minoxidil pharmacology rather than a mechanism proven specific to HR-corepressor dysregulation. NCIT candidate term: **NCIT:C15986** (Pharmacotherapy) as `treatment_term`, with `therapeutic_agent` bound to minoxidil (CHEBI term — verify exact CURIE).
- No other pharmacologic agent has published efficacy data for HYPT4 specifically in the sources reviewed.
- **Pharmacogenomics**: Not applicable/not studied for this disorder.

### Advanced therapeutics
Gene therapy, cell therapy, RNA-based therapy, targeted molecular therapy, and immunotherapy have **not** been reported or trialed for HYPT4 in the literature searched — the small-uORF, gain-of-repressor-dosage mechanism is in principle an attractive target for future antisense/uORF-modulating approaches, but no such published work was found; this should be stated as an evidence gap rather than a therapeutic option.

### Surgical/interventional
- **Hair transplantation**: Discussed in general hypotrichosis-management literature as showing "the most promise for localized forms" but success is described as variable and dependent on remaining donor-follicle density, without HYPT4-specific outcome data located in this search [search: treatment summary].

### Supportive/rehabilitative
No disease-specific supportive-care, physical therapy, or rehabilitation literature applies (non-functional, cosmetic/dermatologic condition). Psychosocial/cosmetic counseling is a reasonable inferred supportive measure but is not specifically documented in a HYPT4 source.

### Experimental
No registered clinical trials (ClinicalTrials.gov / WHO ICTRP) specific to HYPT4/MUHH1 were identified in this search.

### Treatment outcomes
- **Response rates**: Limited to the single detailed pediatric minoxidil case report cited above; no larger case series with quantified response rates was found.
- **Adverse events**: The minoxidil case reported **no irritation or hypertrichosis** at 5% topical dosing in that patient [PMC12340736]; general minoxidil adverse-event profile (irritant contact dermatitis, unwanted facial hypertrichosis) applies generically but was not specifically documented as occurring in HYPT4 patients in the sources reviewed.

### Treatment strategy
No published treatment algorithm/guideline specific to HYPT4 exists; management is empiric and individualized, with topical minoxidil as the most evidence-supported current first-line symptomatic option and lifelong dermatologic follow-up recommended given the progressive natural history [search: treatment summary].

---

## 13. Prevention

- **Primary prevention**: Not applicable in the population-health sense (monogenic dominant disorder; no modifiable risk-factor-based primary prevention exists). The only "primary prevention" concept applicable is **reproductive/genetic counseling** for known mutation carriers regarding the 50% transmission risk to offspring given autosomal dominant inheritance.
- **Secondary prevention**: No early-detection screening program exists; early clinical recognition (sparse birth hair progressing to coarse childhood hair) allows earlier initiation of symptomatic management (e.g., minoxidil) before extensive hair loss, which is a plausible but not formally studied secondary-prevention rationale.
- **Tertiary prevention**: Ongoing dermatologic monitoring and symptomatic treatment (§12) to limit progression-related cosmetic morbidity.
- **Immunization**: Not applicable.
- **Genetic screening**: Prenatal diagnosis or preimplantation genetic diagnosis has not been specifically reported for this condition in the sources reviewed, though it would be technically feasible once a family's causal *HRURF* variant is known (standard for any characterized autosomal dominant Mendelian disorder) — this is an inference, not a documented practice.
- **Genetic counseling**: Appropriate and presumably standard of care given full penetrance and 50% transmission risk, though no HYPT4-specific counseling-outcomes literature was located.
- **Public health/environmental/prophylaxis**: Not applicable — no environmental or infectious contributor exists to intervene upon (§5).

---

## 14. Other Species / Natural Disease

- **Taxonomy**: The principal comparative/model system is **mouse** (*Mus musculus*, NCBITaxon:10090).
- **Orthologous gene**: Mouse *Hr* (hairless) — the murine ortholog of human *HR*; the *Hr* mutation was first recognized in mice ~75 years before the human gene was cloned, originally arising from an **endogenous retroviral insertion** [RIKEN BRC mouse-of-the-month summary]. Note: the specific *HRURF*/*U2HR* uORF-level gain-of-repressor-dosage mechanism causing human MUHH1 is a **distinctly human** (or at least separately characterized) regulatory mechanism — the classic mouse *hr*/*hr^rh* (rhino) models are **coding-region loss-of-function** models, mechanistically analogous to human recessive *HR*-null disease (atrichia with papular lesions / alopecia universalis congenita, see below), **not** to the dominant uORF gain-of-function mechanism of HYPT4 itself. This distinction is important and should not be blurred in curation.
- **Natural/veterinary disease**: The classic hairless (*hr*) and rhino (*hr^rh*) mouse strains are naturally arising/ENU-induced coding mutants, not spontaneous companion-animal disease reports; homozygous mutant mice are born with normal skin/follicles but become completely naked within four weeks and develop skin and nail anomalies, and are widely used as a dermatology research tool strain precisely because of this phenotype [RIKEN BRC; ScienceDirect Hairless Mouse overview]. No OMIA (naturally occurring companion-animal) entry specific to a *HRURF*-uORF-analogous dominant disorder was identified in this search.
- **Comparative biology**: HR functions as a nuclear receptor corepressor (of TR, RORα, VDR) in both mouse and human, and *Hr*/*HR* is evolutionarily conserved in its role regulating the postnatal hair cycle [Sci Rep, "Molecular evolution of HR", PMC3216519]. The progression of the human congenital *HR*-coding disorders (atrichia with papular lesions, alopecia universalis congenita) closely parallels the hairless-mouse phenotype, establishing strong cross-species conservation of HR's hair-cycle role at the loss-of-function end of the allelic spectrum — the human MUHH1/HYPT4 gain-of-repressor-dosage phenotype is the human-specific, milder, dominant end of that same gene's allelic spectrum.
- **Transmission**: Not applicable — non-infectious, non-zoonotic monogenic disorder.

---

## 15. Model Organisms

- **Model type**: Genetic (naturally arising and induced) mouse models exist for the ***HR* gene** broadly, but **no mouse model specifically recapitulating the *HRURF*/*U2HR* uORF dominant gain-of-function mechanism of HYPT4/MUHH1** was identified in this search — this is a notable gap given how mechanistically specific (uORF-level dosage control) the human disease mutation class is.
- **Specific model systems available (for the broader *HR* locus)**:
  - **Hairless (*hr*) mouse**: classic naturally arising coding-loss-of-function mutant (originally a retroviral insertion) [RIKEN BRC].
  - **Rhino (*hr^rh*) mouse**: allelic *Hr* coding mutant with a related but distinct phenotype [ScienceDirect Hairless Mouse overview].
  - ***Hr^m1Enu*** mouse: an ENU-induced novel missense *Hr* mutant causing irreversible hair loss, characterized genetically and molecularly [ScienceDirect, PMID search: "A novel missense mutation in the mouse hairless gene causes irreversible hair loss"].
- **Induced models**: The ENU mutagenesis-derived *Hr^m1Enu* allele is the clearest "induced" (as opposed to spontaneous) *Hr* model identified.
- **Genetic model types available**: Naturally arising and ENU-induced point/insertional coding mutants exist; no conditional, humanized, or uORF-specific knock-in model for the *HRURF* dominant mechanism was located.
- **Phenotype recapitulation**: The existing *Hr*-coding mouse models recapitulate the **recessive, complete-alopecia end** of the human *HR*-related disease spectrum (analogous to atrichia with papular lesions/alopecia universalis congenita) well — "the progression of the human disorders atrichia with papular lesions and alopecia universalis congenita is very similar to that of the hairless mouse" [search: mouse-model summary]. They do **not** model the dominant, dosage-sensitive, triphasic (sparse→coarse→progressive-loss) HYPT4/MUHH1 phenotype, which is mechanistically a *gain* of HR corepressor dosage rather than its loss.
- **Model limitations**: The absence of a uORF-specific dosage model for HYPT4 is itself the principal limitation — inference about the human dominant disease mechanism currently rests on (a) *in vitro* translation/reporter assays of the mutant uORF [PMID:19122663] and (b) parallel HR/VDR biochemical corepressor studies performed in cell lines and in the (loss-of-function) mouse models, not on a disease-matched *in vivo* gain-of-function model.
- **Research applications**: The existing *Hr* mouse models are broadly used for skin/dermatology research generally (their naked phenotype is convenient for topical/dermatologic testing without shaving), but their specific research applicability to HYPT4/MUHH1 mechanism is indirect (informs HR/VDR/TR corepressor biology generally, not the dominant uORF-dosage mechanism specifically).
- **Resources**: MGI (Mouse Genome Informatics) is the relevant repository for *Hr* allele records; specific accession numbers for *hr*, *hr^rh*, and *Hr^m1Enu* were not individually retrieved in this search and should be looked up directly in MGI before citing as dismech `animal_models` entries.

---

## Summary of Key Ontology Term Candidates (verify all before binding)

| Concept | Suggested term | Note |
|---|---|---|
| Disease | MONDO:0100522 (as given); cross-check MONDO:0007806 for merge/obsolescence | OMIM:146550, ORPHA:444 |
| Causal gene | hgnc:55085 (HRURF) | chr8p21.3 |
| Related HR gene | hgnc:5172 (HR) | chr8p21.3 |
| MUHH2 sibling locus gene | EPS8L3 (HGNC:21297), OMIM #612841 | For lump/split note only |
| Core phenotype | HP:0008070 (Sparse hair) | Reasonably confident |
| Hypotrichosis general | HP:0002293 (Hypotrichosis) | Reasonably confident |
| Sparse eyebrow/eyelash/body hair | Not confidently resolved in this search | **Must verify exact CURIEs via OAK before curation** |
| Coarse/wiry hair shaft abnormality | Not confidently resolved | **Must verify** |
| Corepressor mechanism | GO:0003714 (transcription corepressor activity) | Verify |
| Hair cycle | GO:0042633 (hair cycle) | Verify |
| Cell types | Hair follicle outer root sheath cell, hair matrix keratinocyte (CL) | Verify exact CURIEs |
| Anatomy | Hair follicle, eyebrow, eyelash (UBERON) | Verify exact CURIEs |
| Treatment | NCIT:C15986 (Pharmacotherapy) + therapeutic_agent minoxidil (CHEBI, verify) | |

---

## Sources

- [Entry - #146550 - HYPOTRICHOSIS 4; HYPT4 - OMIM](https://omim.org/entry/146550)
- [Loss-of-function mutations of an inhibitory upstream ORF in the human hairless transcript cause Marie Unna hereditary hypotrichosis — Nature Genetics (PMID:19122663)](https://www.nature.com/articles/ng.276)
- [Marie Unna hereditary hypotrichosis: Identification of a U2HR mutation in the family from the original 1925 report (PMID:20659777)](https://pubmed.ncbi.nlm.nih.gov/20659777/)
- [Identification of mutations in U2HR in two Chinese families with Marie Unna hereditary hypotrichosis (PMID:26269244)](https://pubmed.ncbi.nlm.nih.gov/26269244/)
- [Two cases of Marie Unna hereditary hypotrichosis: clinical features and mutation analysis of the U2HR and EPS8L3 genes (PMID:24236410)](https://pubmed.ncbi.nlm.nih.gov/24236410/)
- [Exome sequencing identified a missense mutation of EPS8L3 in Marie Unna hereditary hypotrichosis](https://escholarship.org/uc/item/6pf0m22z)
- [Entry - #612841 - HYPOTRICHOSIS 5; HYPT5 - OMIM](https://omim.org/entry/612841)
- [Linkage of Marie-Unna hypotrichosis locus to chromosome 8p21 and exclusion of 10 genes including the hairless gene by mutation analysis (PMID:10854110)](https://pubmed.ncbi.nlm.nih.gov/10854110/)
- [Refinement of a locus for Marie Unna hereditary hypotrichosis to a 1.1-cM interval at 8p21.3 (PMID:15149494)](https://pubmed.ncbi.nlm.nih.gov/15149494/)
- [Orphanet: Marie Unna hereditary hypotrichosis (ORPHA444)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=444)
- [Marie-Unna Hereditary Hypotrichosis - PMC (PMC4212298)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4212298/)
- [Clinical Presentation of a Family Diagnosed With Marie Unna Hereditary Hypotrichosis 1 Caused by a Novel Variant in HRURF - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12646977/)
- [Significant Hair Regrowth With 5% Topical Minoxidil in a Child With Marie Unna Hereditary Hypotrichosis Caused by a Recurrent HRURF Variant - PMC (PMC12340736)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12340736/)
- [Modulation of Vitamin D Receptor Activity by the Corepressor Hairless: Differential Effects of Hairless Isoforms - Endocrinology](https://academic.oup.com/endo/article/150/11/4950/2455445)
- [Physical and functional interaction between the vitamin D receptor and hairless corepressor, two proteins required for hair cycling (PMID:12847098)](https://pubmed.ncbi.nlm.nih.gov/12847098/)
- [The hairless gene mutated in congenital hair loss disorders encodes a novel nuclear receptor corepressor - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC312820/)
- [Molecular evolution of HR, a gene that regulates the postnatal cycle of the hair follicle - PMC (PMC3216519)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3216519/)
- [HR Gene - GeneCards](https://www.genecards.org/card/HR)
- [Entry #604379 / #278150 / #607903 (HYPT7/HYPT8/HYPT6) LIPH/LPAR6-related hypotrichoses - OMIM](https://omim.org/entry/604379)
- [Founder mutations in the lipase H (LIPH) gene in families with autosomal recessive woolly hair/hypotrichosis - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2859194/)
- [Nov 2011 Hairless Congenics for Dermatology Studies - RIKEN BRC](https://mus.brc.riken.jp/en/mouse_of_month/nov_2011_mm)
- [Entry - #203655 - ALOPECIA UNIVERSALIS CONGENITA; ALUNC - OMIM](https://omim.org/entry/203655)
- [A novel missense mutation in the mouse hairless gene causes irreversible hair loss: Genetic and molecular analyses of Hr^m1Enu - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S088875430500368X)
- [Hypotrichosis 4 - NIH Genetic Testing Registry (GTR)](https://www.ncbi.nlm.nih.gov/gtr/conditions/C2750815/)
- [HRURF gene with submissions organized by classifications - GenCC](https://thegencc.org/genes/HGNC:55085)
- [HR gene with submissions organized by classifications - GenCC](https://search.thegencc.org/genes/HGNC:5172)

**Evidence gaps to flag explicitly in curation** (per this session's evidence-attribution standard — an acknowledged gap, not a smoothed-over one): (1) no molecular/omics dataset specific to HYPT4 patient hair-follicle tissue was located; (2) no disease-specific quantitative penetrance or QoL-instrument study was located; (3) no HYPT4-matched (uORF-level dominant gain-of-function) animal model exists — all current mouse models represent the mechanistically distinct recessive *HR*-coding-loss end of the allelic spectrum; (4) several HPO term matches above are stated as *candidates only* and were not resolved to verified CURIEs in this search — resolve via OAK/HPO browser before any KB curation.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 16 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 5 |
| Terms whose name was checked | 6 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002293` (2 mentions) - the report calls it "Hypotrichosis"; HP calls it **Alopecia of scalp**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `MONDO:0007806` (obsolete hypotrichosis 4) (2 mentions) - replaced by `MONDO:0100522`
- `GO:0070577` (obsolete lysine-acetylated histone binding) (1 mention) - replaced by `GO:0140566`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`.
