---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-04T16:11:03.978315'
end_time: '2026-11-04T16:13:23.260787'
duration_seconds: 139.28
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Striate Palmoplantar Keratoderma Type 1
  mondo_id: MONDO:0007859
  category: Mendelian
  causal_genes: DSG1
  omim_id: OMIM:148700
  synonyms: keratosis palmoplantaris striata i, AD
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
  - claude-opus-5-5
  web_search_requests: 3
  num_turns: 12
  total_cost_usd: 1.8152164000000002
  session_id: 5d05f971-a8fc-41a8-956b-fe8be81fd5ee
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 12
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 21
  on_topic: 18
  validator_version: 0.5.1
term_validation:
  total_terms: 22
  verified: 22
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: UBERON:0013776
    reported_labels:
    - 'Primary: skin of the palms and soles'
    ontology_label: skin of palmar/plantar part of autopod
  - term_id: NCIT:C15747
    reported_labels:
    - Mechanical paring / debridement
    - Footwear and custom insoles to offload pressure
    ontology_label: Supportive Care
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Striate Palmoplantar Keratoderma Type 1
- **MONDO ID:** MONDO:0007859 (if available)
- **Causal gene(s):** DSG1
- **OMIM:** OMIM:148700
- **Synonyms:** keratosis palmoplantaris striata i, AD
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Striate Palmoplantar Keratoderma Type 1** covering all of the
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

I'm checking a few more sources on the web (the mouse knockout, SAM syndrome, and recent DSG1 papers) to add to the 16 references already cached in the repo. After that I'll write the report.

# Striate Palmoplantar Keratoderma Type 1 (SPPK1; DSG1): Research Report

**Scope and identifiers.** This report covers MONDO:0007859 / OMIM 148700. It is caused by heterozygous variants in **DSG1** (desmoglein 1; HGNC `hgnc:3048`) on chromosome 18q12.1. Biallelic DSG1 loss of function causes a different disease, SAM syndrome (MONDO:0014218), which this report treats only as a differential diagnosis. Striate PPK caused by DSP (type 2, MONDO:0013034) and by KRT1 (type 3) are separate diseases.

**How this was assembled.** The knowledge base already has an entry, `kb/disorders/Striate_Palmoplantar_Keratoderma_Type_1.yaml`, which cites 16 PubMed papers. All 16 are cached in `references_cache/`. Quotes below marked **[cached]** come from those files and match exactly. Sources found by web search in this session are marked **[web, not cached]**: I checked their PMIDs or bibliographic details, but I did not check their abstract text against a cache file. Each ontology label below was copied from the repository's own term-cache files (`cache/*/terms.csv`), not written from memory.

---

## 1. Disease information

SPPK1 is an autosomal dominant, non-syndromic thickening of the skin of the palms and soles (keratoderma). Typical features:
- **Palms:** linear hyperkeratotic bands running along the volar (palm-side) fingers onto the palm.
- **Soles:** focal hyperkeratosis at pressure points, often appearing before the palmar changes.
- **No other organs involved:** no hair, heart or systemic disease.

The pattern varies. The same gene, and sometimes the same allele, gives focal or diffuse keratoderma in some families. That is why OMIM and MONDO name the disease "striate, focal, or diffuse".

| Identifier | Value |
|---|---|
| MONDO | MONDO:0007859 *palmoplantar keratoderma i, striate, focal, or diffuse* |
| OMIM | 148700 (gene: DSG1, *125670) |
| HGNC | `hgnc:3048` DSG1 |
| ICD-10 | Q82.8 (other specified congenital malformations of skin), the code used for hereditary PPK in the German reference Altmeyers ([altmeyers.org](https://www.altmeyers.org/de/dermatologie/keratosis-palmoplantaris-striata-mit-mutationen-in-desmoglein-1-2104)) |
| Synonyms | SPPK1; PPKS1; keratosis palmoplantaris striata I; Brunauer-Fuhs-Siemens type PPK (historical); DSG1-related striate PPK |

**Where the information comes from:** aggregated disease-level resources (OMIM, MONDO, Orphanet) plus family reports and small case series. There are no EHR cohorts or registries.

---

## 2. Etiology

**Primary cause.** Heterozygous germline loss-of-function variants in DSG1 reduce the amount of desmoglein 1 by half (haploinsufficiency).
- "Recently we have identified a mutation in the DSG1 gene coding for desmoglein 1 as the cause of the autosomal dominant skin disease striate palmoplantar keratoderma (SPPK) in which affected individuals have marked hyperkeratotic bands on the palms and soles." **PMID:11313759 [cached]** (Hunt et al. 2001, *Eur J Hum Genet*)
- "This latter mutation thus results in the mutant allele synthesising only 25 amino acid residues of the prosequence of the protein so that this is effectively a null mutation implying that dominance in the case of this mutation was caused by haploinsufficiency." **PMID:11313759 [cached]**

**Environmental modifier: mechanical stress.** This is a modifier of how severe the lesions are, not a cause.
- "The most severe consequences of SPPK mutations are in regions of the body where pressure and abrasion are greatest and where desmosome function is most necessary." **PMID:11313759 [cached]**
- Desmoglein 1 loss "has a critical impact on the integrity of tissues experiencing strong mechanical stress." **PMID:16484817 [cached]**

**Other factors:**
- No GWAS or susceptibility loci have been reported.
- No protective genetic or environmental factors have been reported.
- One 2024 case had a co-occurring LDLR splice variant. The authors only speculated about a role and did not show one: He & Zhu 2024, *Genes & Genomics*, doi 10.1007/s13258-024-01587-7 **[web, not cached]**.

**Gene-environment interaction.** The only one documented is genotype × friction/pressure: lesions concentrate at sites of mechanical load. This comes from clinical observation, not from formal study.

---

## 3. Phenotypes

| Phenotype | HPO (label from cache) | Onset / course | Frequency | Evidence |
|---|---|---|---|---|
| Linear palmar/digital hyperkeratosis | HP:0007501 *Streaks of hyperkeratosis along each finger onto the palm* | Childhood; lifelong, stable | Defining (most families) | "Clinically, these patients presented with hyperkeratotic palms and with linear hyperkeratosis on the fingers." PMID:17194569 [cached] |
| Focal plantar hyperkeratosis at pressure points | HP:0007497 *Focal friction-related palmoplantar hyperkeratosis* | Often the first sign | Very frequent | "Additionally, focal hyperkeratosis was seen on the sole of the toes as well as the ball and heel of the foot." PMID:17194569 [cached]; "striate palmar involvement and varying focal or diffuse plantar disease" PMID:27534273 [cached] |
| Diffuse PPK (in some families) | HP:0007447 *Diffuse palmoplantar hyperkeratosis* | Variable | Occasional | "Mutations in the desmoglein 1 gene (DSG1)… have been reported primarily in striate, but also in focal and diffuse PPKs." PMID:27534273 [cached] |
| Plantar pain on walking | HP:6001399 *Plantar pain* | From early childhood | Common; the main effect on quality of life | "She reported thickening of the skin of palms and soles since 1 year of age, resulting in pain while walking." PMID:29315490 [cached] |
| Keratotic lesions at knees, ankles, knuckles | HP:0000962 *Hyperkeratosis* | Variable | Occasional | PMID:16484817 [cached] |
| Mild nail dystrophy | HP:0008404 *Nail dystrophy* | — | Rare | "…with mild nail dystrophy." PMID:16484817 [cached] |
| Acantholysis / widened intercellular spaces (histology) | HP:0100792 *Acantholysis* | — | Characteristic finding | "Widening of the intercellular spaces and disadhesion of epidermal keratinocytes may serve as a histologic clue to PPKs caused by DSG1 mutations." PMID:20082890 [cached] |

**Typical course across these features:**
- **Onset:** infancy or childhood. The soles often precede the palms (PMID:32147745 [cached]).
- **Severity:** mild to moderate. It varies between and within families.
- **Course:** stable throughout life and worsened by manual or pedal work.
- **Quality of life:** no EQ-5D or SF-36 data specific to SPPK1 were found. The burden described is pain on walking and functional limits on manual work.

---

## 4. Genetic and molecular information

**Gene and protein.**
- **Gene:** DSG1 (`hgnc:3048`, OMIM *125670). It encodes a desmosomal cadherin of the stratified epidermis that is expressed most strongly in the suprabasal and granular layers.
- **Protein structure:** the extracellular domains are EC1–EC4 plus an extracellular anchor. The intracellular part binds plakoglobin.

**Variant spectrum.** More than 25 alleles have been reported. Almost all introduce a premature termination codon (PTC).
- "To date, more than 25 mutations in DSG1 have been identified in patients with SPPK1. These mutations were uniformly found to result in a premature termination codon (PTC)." **PMID:29315490 [cached]**
- **First allele described (Rickman et al. 1999):** a splice-site variant causing in-frame skipping of exon 3. "This causes aberrant splicing of exon 2 to exon 4, which are in-frame, with the consequent removal of exon 3 encoding part of the prosequence, the mature protein cleavage site and part of the first extracellular domain." **PMID:10332028 [cached]**
- **Nonsense:**
  - c.395C>A: "Direct DNA sequencing analysis revealed a heterozygous C-to-A transversion at nt 395 of the DSG1 gene." **PMID:12930313 [cached]**
  - Recurrent p.R26X, Pakistani families: "Mutation analysis resulted in the identification of one recurrent mutation (p.R26X) and four novel mutations (c.Ivs4-2A>G, c.515C>T, c.Ivs9-3C>G, and c.1399delA) in the DSG1 gene. Each mutation is predicted to cause haploinsufficiency of DSG1 protein." **PMID:19157795 [cached]**
  - p.(Arg117*), reported 2024 (Koschitzki et al., *Clin Case Rep*, [DOAJ](https://doaj.org/article/6d956dc05ec54493957bc3cb2395a270)) **[web, not cached]**
- **Frameshift / NMD:**
  - Exon-12 skipping allele: "We predict that this mutation will lead to the skipping of exon 12 which is out of frame (134nt), subsequent degradation of the mutant mRNA by non-sense mediated RNA decay, and haploinsufficiency for DSG1." **PMID:17194569 [cached]**
  - UK series: p.Tyr126Hisfs*2, p.Ser521Tyrfs*2, p.Trp3*, p.Asp591Phefs*9, p.Met249Ilefs*6 **PMID:27534273 [cached]**
  - Syrian family: "This frameshift mutation was heterozygous in all affected family members and absent in all normal individuals." **PMID:31192455 [cached]**
- **Missense (exceptional):** "…the first case of SPPK caused by a missense (rather than PTC-causing) mutation affecting a residue predicted to be of critical importance for DSG1-mediated adhesion." **PMID:29315490 [cached]**
- **Somatic vs germline:** germline. No somatic or mosaic cases were found.

**Functional consequence.** Loss of function through haploinsufficiency, mostly via nonsense-mediated decay (GO:0000184 *nuclear-transcribed mRNA catabolic process, nonsense-mediated decay*). There is no dominant-negative effect. In one patient, sequencing of cDNA from affected skin found no transcript from the mutant allele: "Direct sequencing of cDNA derived from affected skin in one patient failed to reveal a pathogenic mutation, suggesting that SPPK results from haploinsufficiency for DSG1." **PMID:19018793 [cached]**

**Allelic series by dose:**
- Heterozygous → SPPK1.
- Biallelic → SAM syndrome: "Monoallelic desmoglein 1 mutations have been known for many years to cause striate palmoplantar keratoderma, but only recently, biallelic loss-of-function mutations were associated with a new disorder, designated as SAM syndrome…" **PMID:25041099 [cached]**; original description Samuelov et al. 2013, *Nat Genet* **PMID:23974871 [web; PMID confirmed on PubMed]**.
- **Exception:** a 2025 *J Dermatol* report describes a homozygous splice variant, c.685-3T>A, that gave only *mild striate PPK* without SAM ([PMC12592573](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12592573/)) **[web, not cached]**. A hypomorphic (partially functional) allele would explain this, but that explanation is an inference.

**Other genetic data:**
- **Allele frequency:** PTC alleles are absent or ultra-rare in gnomAD. DSG1 tolerates loss of function less than most genes, but some heterozygous LoF carriers exist, so penetrance or ascertainment caveats apply. gnomAD was not queried for this report.
- **ClinVar / ClinGen:** neither was queried in this session, so no curated tier is reported here.
- **Modifier genes, epigenetics, chromosomal abnormalities:** none reported. Large 18q deletions spanning the desmosomal cadherin cluster would be expected to cause haploinsufficiency, but no such case was found.

---

## 5. Environmental information

- **Main modifier:** mechanical friction and pressure (manual labour, walking, footwear), as described in section 2. There is no chemical, toxic, infectious or lifestyle cause.
- **Infection:** not applicable as a cause. Secondary fungal or bacterial infection of fissures is a general PPK complication; no SPPK1-specific data were found.

---

## 6. Mechanism and pathophysiology

### Causal chain
1. **A heterozygous DSG1 PTC variant (nonsense, frameshift or splice) leads to** the mutant mRNA being degraded by nonsense-mediated decay (GO:0000184), and therefore **to** about 50% of normal desmoglein 1 protein. *Demonstrated:* PMID:17194569, 19018793, 11313759.
   - *Branch:* the rare missense allele (PMID:29315490) instead impairs adhesion through the EC interface, so the protein is present but less functional. *Inferred* from structural prediction.
2. **Reduced Dsg1 in suprabasal keratinocytes (CL:4033013 *suprabasal keratinocyte*) leads to** fewer and smaller suprabasal desmosomes, i.e. disturbed GO:0002934 *desmosome organization*. *Demonstrated in patient skin:* "Both Dp and Dsg1 mutations were accompanied by significantly reduced numbers of desmosomes in the suprabasal layers, while decreased desmosome size was evident only in Dsg1-associated SPPK." **PMID:15149499 [cached]**
3. **Weaker desmosomes lead to** reduced keratinocyte cell-cell adhesion (GO:0098609 *cell-cell adhesion*), which appears as widened intercellular spaces and partial acantholysis in the spinous and granular layers. "varying degrees of widening of the intercellular spaces and partial disadhesion of keratinocytes in the mid and upper epidermal spinous cell layers, often extending to the granular cell layer." **PMID:20082890 [cached]**
4. **Parallel branch: loss of Dsg1 signalling.** Normally Dsg1 binds Erbin, which disrupts SHOC2–Ras–Raf scaffolds and so suppresses EGFR → ERK1/2 signalling (GO:0007173 *epidermal growth factor receptor signaling pathway*; GO:0070371 *ERK1 and ERK2 cascade*).
   - "Instead, Dsg1 was required for suppression of epidermal growth factor receptor-Erk1/2 (extracellular signal-regulated kinase 1/2) signaling, thereby facilitating keratinocyte progression through a terminal differentiation program." **PMID:19546243 [cached; in vitro]**
   - In patient epidermis: "analysis of epidermis from DSG1-deficient patients with SPPK demonstrated increased Ras-SHOC2 colocalization and decreased Erbin-SHOC2 colocalization…" **PMID:23524970 [cached]**
   - **Result:** the brake on ERK signalling is weaker.
5. **Higher ERK activity and weakened scaffolding lead to** abnormal terminal differentiation (GO:0030216 *keratinocyte differentiation*): K16 goes up, the keratin filament network is disturbed, and involucrin is abnormal.
   - "In both types of SPPK upregulation of K16 was pronounced and involucrin labelling was abnormal." **PMID:15149499 [cached]**
   - "The expression of keratins K5, K14 and K10 was reduced in Dsg1-associated SPPK skin…" **PMID:15149499 [cached]**
6. **Steps 3 and 5 combined with mechanical load (friction and pressure on volar skin) lead to** compensatory hyperproliferation and hyperkeratosis, which is localised to stressed areas (UBERON:0013776 *skin of palmar/plantar part of autopod*). The result is linear bands along flexural lines of the fingers and focal plantar plaques. *How load is turned into hyperkeratosis is inferred* from where lesions occur (PMID:11313759, 16484817).
7. **Thick hyperkeratotic plaques lead to** fissuring and pain on walking (HP:6001399), the main clinical burden.

### Upstream vs downstream
- **Upstream:** NMD → haploinsufficiency.
- **Middle:** desmosome loss and EGFR-ERK de-repression, which are parallel and interacting branches.
- **Downstream:** differentiation defect → hyperkeratosis → pain.

### Other mechanism categories
- **Immune involvement:** not part of SPPK1. Allergic/Th2 inflammation emerges only with complete DSG1 loss (SAM: PMID:23974871, PMID:25041099).
- **Metabolic, epigenetic, omics:** no metabolic, epigenetic, single-cell, spatial or proteomic studies specific to SPPK1 were found. Dsg1-related transcriptomic studies come from keratinocyte knockdown and SAM work, not from SPPK1 tissue.

### Suggested terms

| Kind | Terms |
|---|---|
| CL | CL:0000312 *keratinocyte*; CL:4033013 *suprabasal keratinocyte* |
| GO | GO:0000184; GO:0002934; GO:0098609; GO:0007173; GO:0070371; GO:0030216 |
| GO cellular component | Desmosome is suggested, but the CURIE was not looked up in this session, so verify it before binding |

---

## 7. Anatomical structures affected

- **Organ:**
  - Primary: skin of the palms and soles (UBERON:0013776).
  - Occasional: knees, ankles, knuckles, nails.
  - No internal organs are affected. Hair and heart are normal, unlike DSP-related syndromes.
- **Tissue and cell:** stratified squamous epidermis; suprabasal (spinous and granular) keratinocytes.
- **Subcellular:** the desmosome (the adhesive junction plaque) and the keratin intermediate-filament network.
- **Laterality:** bilateral, but often asymmetric, following individual pressure patterns.

---

## 8. Temporal development

- **Onset:** infancy or childhood, often in the first years once the child walks. The soles are frequently affected before the palms. Example: "since 1 year of age" (PMID:29315490).
- **Course:** chronic, lifelong and stable. There are no stages and it does not progress systemically.
- **Fluctuation:** severity changes with mechanical load and occupation. There is no spontaneous remission.
- **Possible intervention window:** early protective footwear may reduce painful plantar plaques. This is expert opinion only.

---

## 9. Inheritance and population

| Feature | Data |
|---|---|
| Mode | Autosomal dominant (HP:0000006 *Autosomal dominant inheritance*) |
| Penetrance | High within reported families, with variable expressivity (striate vs focal vs diffuse in the same family; PMID:27534273) |
| Anticipation | None |
| Germline mosaicism | Not reported |
| Founder / recurrent alleles | p.R26X recurs in Pakistani families (PMID:19157795) |
| Consanguinity | Not relevant to the dominant form; it matters for biallelic forms (SAM; the mild homozygous splice family) |
| Prevalence / incidence | No population-based estimate exists. Literature is limited to family reports. Treat as rare / unknown. |
| Geography | Families reported from the UK, Europe, Pakistan, Syria, China, Japan, the Middle East and elsewhere; worldwide |
| Sex ratio | About 1:1, as expected for autosomal dominant inheritance |

---

## 10. Diagnostics

**Clinical diagnosis.** Striate or focal PPK with a dominant family history, without hair, cardiac or other organ involvement.

**Histology.** Hyperkeratosis and acanthosis with widened intercellular spaces and suprabasal disadhesion. "These findings, which are associated with haploinsufficiency of desmoglein 1, were not observed in any of the other 6 PPK cases." **PMID:20082890 [cached]**
- **Electron microscopy:** fewer and smaller suprabasal desmosomes (PMID:15149499).
- **Immunostaining:** reduced Dsg1 staining.

**Genetic testing:**
- **Recommended first test:** a multigene PPK panel (DSG1, DSP, KRT1, KRT9, KRT16, AAGAB, SERPINB7, TRPV3, AQP5, GJB2 and others), or exome sequencing.
- **Single-gene DSG1 testing:** reasonable when the striate pattern and histology fit.
- **Copy number:** deletion/duplication analysis is worth considering, although no SPPK1 CNV has been reported.
- **Not useful:** chromosomal microarray, karyotype, FISH, mtDNA and repeat-expansion testing.
- **Why a broad panel matters:** "Mutations in desmoglein 1 cause diverse inherited palmoplantar keratoderma phenotypes: implications for genetic screening" (PMID:27534273). Because the gene also produces focal and diffuse forms, DSG1 should be on panels for non-striate PPK as well.

**Differential diagnosis:**
- **SPPK2 (DSP):** may come with woolly hair or cardiomyopathy in recessive and syndromic forms (Carvajal syndrome).
- **SPPK3 (KRT1)**.
- **Focal non-epidermolytic PPK:** KRT6C/KRT16.
- **Punctate PPK:** AAGAB.
- **Other hereditary PPK (e.g. epidermolytic PPK, KRT9):** shows epidermolysis on histology.
- **SAM syndrome (biallelic DSG1):** severe dermatitis, allergies, metabolic wasting.
- **Acquired keratoderma:** friction callosities, keratoderma climactericum.

**Screening.** No newborn or population screening. Cascade testing of relatives is possible once the familial variant is known.

---

## 11. Outcome and prognosis

- **Survival:** normal life expectancy. There is no disease-specific mortality.
- **Morbidity:** pain, fissures, limits on walking and manual work, and cosmetic and psychosocial burden. There are no validated QoL instrument data.
- **Complications:** painful fissures and possible secondary infection (general PPK knowledge). No increased cancer risk has been reported.
- **Recovery:** none expected. Symptoms can be controlled.
- **Prognostic factors:** occupational and mechanical load. No biomarkers exist.

---

## 12. Treatment

Treatment is entirely supportive. There are no disease-modifying or approved targeted therapies. Koschitzki 2024 notes that effective treatment options remain limited **[web, not cached]**.

| Intervention | NCIT term | Evidence |
|---|---|---|
| Topical keratolytics (urea, salicylic acid), emollients | NCIT:C15747 *Supportive Care* (agents via CHEBI as `therapeutic_agent`) | "…Keratolytics" (management table) PMID:32147745 [cached] |
| Mechanical paring / debridement | NCIT:C15747 | Expert practice |
| Footwear and custom insoles to offload pressure | NCIT:C15747 | "As with most PPKs, comfortable foot wear and customised insoles are helpful." PMID:32147745 [cached] |
| Systemic retinoids (acitretin) | Pharmacotherapy (`NCIT:C15986`, listed in the repo's guidance) with an acitretin CHEBI agent, to be looked up | Used generally in severe PPK. No SPPK1-specific trial found; in desmosomal PPK they can increase fragility. Expert opinion only. |

- **Pharmacogenomics:** none.
- **Gene, RNA or cell therapy:** none.
- **Clinical trials:** none found for SPPK1.
- **Rationale only:** EGFR-pathway modulation follows from the mechanism. EGFR/MEK inhibition can cause PPK-like eruptions, which argues against a simple inhibitor approach. No trial exists.

---

## 13. Prevention

- **Primary prevention:** not applicable beyond genetic counselling. Each child of an affected parent has a 50% risk. Prenatal or preimplantation testing is technically possible but rarely sought for a mild condition.
- **Secondary prevention:** early diagnosis to start footwear and skin-care habits.
- **Tertiary prevention:** reduce friction (occupational adjustments, padded gloves and footwear) and treat fissures to prevent infection.
- **Immunization, prophylaxis, public health measures:** none applicable.

---

## 14. Other species and natural disease

- **Naturally occurring disease:** no DSG1-associated PPK in animals was found. OMIA was not queried in this session.
- **Dsg1 orthologs:** conserved in mammals. Mice have three Dsg1 paralogs (Dsg1a/b/c), which makes modelling harder.
- **Related animal disease:** canine pemphigus foliaceus involves autoantibodies to Dsc1 and Dsg1. This is acquired autoimmune disease, not a genetic model.
- **Zoonotic or transmission questions:** not applicable.

---

## 15. Model organisms and systems

| Model | Type | Recapitulation | Source |
|---|---|---|---|
| Human keratinocyte Dsg1 knockdown / 3D organotypic culture | In vitro | Shows EGFR-ERK de-repression and impaired differentiation. Does not reproduce striate palmar lesions. | PMID:19546243; PMID:23524970 [cached] |
| Dsg1-deficient mouse | Knockout | Full loss is lethal from skin blistering, so it models SAM-type complete loss rather than heterozygous SPPK1. Murine Dsg1 paralog redundancy limits fidelity. | Kugelmann et al. 2019, *J Invest Dermatol* 139:1596, **PMID:30660666 [web; title and citation confirmed; phenotype from title only]** |
| CRISPR Dsg1-null mouse (Green/Fitz-related work) | Knockout | Delayed adhesion and keratinization gene expression in embryonic skin | Reported in search results; citation not confirmed |

**Limitations of current models:**
- Mice lack the thick, friction-adapted palmoplantar epidermis in its human form.
- Murine footpads differ from human soles.
- There is no heterozygous model with a striate phenotype. This is a `HUMAN_MODEL_MISMATCH`-type gap.

---

## Key gaps
1. No prevalence data.
2. No quality-of-life measurement.
3. No treatment trials.
4. No haploinsufficient animal model.
5. No omics data from patient palmoplantar skin.
6. No clear explanation for why the same allele gives striate, focal or diffuse disease (candidate explanations: modifier genes, mechanical load).
7. The mild homozygous splice family (2025) conflicts with the simple "biallelic = SAM" rule and needs functional study.

---

## Sources

**Cached in `references_cache/` (snippets match exactly):** PMID:10332028, 11313759, 12930313, 15149499, 16484817, 17194569, 19018793, 19157795, 19546243, 20082890, 23524970, 25041099, 27534273, 29315490, 31192455, 32147745.

**Web (not cached; fetch with `just fetch-reference` before citing as KB evidence):**
- [Samuelov et al. 2013, Nat Genet, PMID:23974871](https://pubmed.ncbi.nlm.nih.gov/23974871/) ([PMC3791825](https://pmc.ncbi.nlm.nih.gov/articles/3791825))
- [Kugelmann et al. 2019, J Invest Dermatol, PMID:30660666](https://searchworks.jioinstitute.edu.in/articles/cmedm__30660666) ([sonar.ch record](https://sonar.ch/global/documents/102166))
- [Koschitzki et al. 2024, Clin Case Rep (DOAJ)](https://doaj.org/article/6d956dc05ec54493957bc3cb2395a270) ([alternate record](https://searchworks.jioinstitute.edu.in/articles/cmedm__38721567))
- [He & Zhu 2024, Genes & Genomics: novel DSG1 mutation with LDLR mutation](https://ouci.dntb.gov.ua/works/40NOAv59) ([bohrium](https://bohrium.dp.tech/paper/arxiv/b00e2e16cc79817131f452cda21ed352617d009decaacb57b18ad2edf69fff6d))
- [Bi-allelic DSG1 splice-site variant in non-syndromic SPPK, 2025 (PMC12592573)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12592573/) ([immunosensation.de](https://www.immunosensation.de/publications/bi-allelic-dsg1-splice-site-variant-identified-in-a-family-with-non-syndromic-striate-palmoplantar-keratoderma))
- [Altmeyers Enzyklopädie: Keratosis palmoplantaris striata (DSG1)](https://www.altmeyers.org/de/dermatologie/keratosis-palmoplantaris-striata-mit-mutationen-in-desmoglein-1-2104)
- [Wikipedia: Desmoglein-1](https://en.wikipedia.org/wiki/Desmoglein-1) (its SAM PMID link is wrong; use 23974871)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 21 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0013776` (2 mentions) - the report calls it "Primary: skin of the palms and soles"; UBERON calls it **skin of palmar/plantar part of autopod**
- `NCIT:C15747` (3 mentions) - the report calls it "Mechanical paring / debridement", "Footwear and custom insoles to offload pressure"; NCIT calls it **Supportive Care**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCIT:C15747` - called "Mechanical paring / debridement", "Footwear and custom insoles to offload pressure"