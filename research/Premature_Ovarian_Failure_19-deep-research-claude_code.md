---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-21T00:06:28.246151'
end_time: '2026-10-21T00:07:49.811545'
duration_seconds: 81.57
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Premature Ovarian Failure 19
  mondo_id: MONDO:0030985
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
  - claude-haiku-5-5
  - claude-sonnet-5-5
  web_search_requests: 5
  num_turns: 12
  total_cost_usd: 0.8130699
  session_id: 72755858-3307-5af9-bc7e-eb9acc2062f1
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 10
reference_validation:
  total_references: 5
  verified: 4
  not_found: 0
  unverifiable: 1
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 1
  validator_version: 0.3.0
term_validation:
  total_terms: 16
  verified: 16
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 4
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0030985
    reported_labels:
    - MONDO
    ontology_label: premature ovarian failure 19
  - term_id: DOID:0112278
    reported_labels:
    - synonyms POF19, POI19
    ontology_label: primary ovarian insufficiency 19
  labels_variant: 6
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Premature Ovarian Failure 19
- **MONDO ID:** MONDO:0030985 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Premature Ovarian Failure 19** covering all of the
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

I'll start by loading the search tools.

I'm gathering primary-source details on the HSF2BP paper. The direct fetches of the eLife and PMC pages were refused by the proxy, so I'm checking the proxy status and trying other routes.

# Premature Ovarian Failure 19 (POF19): research report

**Verification status.** Sources I could read were search-result summaries only. The proxy refused direct fetches of the eLife and PMC full text, and PubMed needed cookies. Anything not seen in a result is marked **[unverified]**. Quotes are not exact abstract text and must be re-checked with `just fetch-reference` before use as snippets. I give no PMID for the founding paper because none appeared in my results.

## 1. Disease information

POF19 is a rare autosomal recessive form of primary ovarian insufficiency (POI), meaning loss of ovarian function before age 40. Its gene is **HSF2BP** (21q22). Only one family is reported in the sources I saw (see section 3).

| Item | Value | Source |
|---|---|---|
| OMIM | 619245 | [DrugMap](https://drugmap.idrblab.net/data/disease/details/DIS60A1W) and [OMIM mirror](https://0-www-ncbi-nlm-nih-gov.brum.beds.ac.uk/omim/619245) (secondary; the OMIM page itself was not read) |
| MONDO | MONDO:0030985 | DrugMap, [NORD](https://rarediseases.org/mondo-disease/premature-ovarian-failure-19/) |
| DOID | DOID:0112278 (synonyms POF19, POI19) | [Disease Ontology](https://disease-ontology.org/term/DOID:0112278/owl) |
| MedGen | C5543229 / 1779702 (the two IDs conflict across sources) | MedGen via search |
| ClinGen-style gene-disease evidence | "Limited" | DrugMap |

Orphanet, ICD-10/11 and MeSH identifiers were not found **[unverified]**. The condition is disease-level and derived from one pedigree plus mouse work, not from EHR data.

## 2. Etiology

- **Cause:** biallelic HSF2BP variants. The reported allele is the missense **p.Ser167Leu (S167L)**, a hypomorph in mouse. The nucleotide change was not confirmed in my sources. c.500C>T is only my inference from the codon change.
- **Risk and protective factors:** none specific to POF19 are documented. Generic POI risks (chemotherapy, radiation, autoimmunity, FMR1 premutation) are not relevant to this entry. No gene-environment interaction data were found.

## 3. Phenotypes

Source: the 2020 eLife paper ([article](https://elifesciences.org/articles/56996), [PMC7498267](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7498267/)). The family is consanguineous: the parents are first cousins of Moslem-Arab origin. Three of five daughters, including a monozygotic twin pair, are affected. They had irregular menses from menarche, then early secondary amenorrhea at ages 24 and 25. One summary mentions elevated gonadotropins and low estradiol **[unverified: figures and the third sister's details not seen]**.

| Phenotype | Suggested HPO | Frequency |
|---|---|---|
| Secondary amenorrhea | HP:0000869 | 3/3 reported |
| Irregular menstruation, oligomenorrhea | HP:0000858 | 3/3 reported |
| Premature ovarian failure | HP:0008209 | 3/3 reported |
| Female infertility | HP:0008222 | Implied |
| Elevated FSH / hypergonadotropism | HP:0000837 | **[unverified]** |

Age at onset is early adulthood (about 24–25 years). Quality-of-life data are not available.

## 4. Genetic and molecular information

- **Gene:** HSF2BP (heat shock transcription factor 2 binding protein). Use lowercase `hgnc:` in the KB, with the CURIE looked up via runoak, not typed from memory.
- **Variant:** S167L, homozygous in affected sisters. The gnomAD frequency is about 0.00018 and the GME frequency about 0.0005, so it is very rare.
- **Functional consequence:** partial loss of function. The eLife abstract summary calls it a hypomorph compared with a new knockout mouse.
- **ACMG classification:** not found in ClinVar or ClinGen **[unverified]**.
- **Modifiers, epigenetics, chromosomal abnormalities:** none reported.

## 5. Environmental information

No environmental, lifestyle or infectious factors are reported.

## 6. Mechanism and pathophysiology

**Causal chain** (steps 1–3 are demonstrated in mouse and biochemically; step 4 is inferred for humans):

1. Homozygous HSF2BP S167L reduces the amount and function of HSF2BP in meiocytes.
2. HSF2BP is a BRCA2 partner and a stabilizing partner of C19ORF57/BRME1. Together they bind BRCA2, RAD51, RPA and PALB2. Reduced HSF2BP lowers HSF2BP and BRME1 signal at recombination nodules.
3. Fewer RAD51/DMC1 foci form, which impairs meiotic double-strand-break repair and lowers crossover frequency. Mutant mouse females have reduced fertility and smaller litters.
4. Oocyte and follicle loss follows, which is **inferred** for women. The result is early depletion of the ovarian reserve, then secondary amenorrhea and infertility.

- **Mouse knockout:** three independent knockouts have nearly identical phenotypes. Published descriptions I saw cover male meiotic failure and spermatogenesis arrest. I found no female knockout detail.
- **Later work:** Sci Adv 2023 describes BRME1 disassembling the BRCA2–HSF2BP ring ([article](https://www.science.org/doi/abs/10.1126/sciadv.adi7352)). A Nat Commun 2021 paper ([article](https://link.springer.com/article/10.1038/s41467-021-24871-6)) shows that deleting BRCA2's HSF2BP-binding region does not reproduce the HSF2BP-null meiotic defect.
- **Suggested terms:**
  - GO: meiotic recombination (GO:0007131), double-strand break repair via homologous recombination (GO:0000724), oogenesis (GO:0048477), oocyte maturation (GO:0001556). All **[unverified]**; look up before binding.
  - CL: oocyte (CL:0000023), primary oocyte.
  - Omics: none available.

## 7. Anatomical structures affected

- **Organ:** ovary (UBERON:0000992), within the female reproductive/endocrine system.
- **Cell and subcellular level:** oocytes and ovarian follicles; the nucleus (meiotic chromosomes, recombination nodules).
- **Lateralization:** bilateral.

## 8. Temporal development

Onset is in early adulthood, after normal menarche. The course is progressive: irregular cycles, then amenorrhea. Remission and critical-period data are not available.

## 9. Inheritance and population

- Autosomal recessive (HP:0000007).
- Consanguinity is present in the one family.
- Penetrance and expressivity are unknown; all homozygous sisters were affected as far as I saw.
- There is no evidence of anticipation or germline mosaicism.
- A founder effect is possible in the Arab family but was not evaluated.
- Prevalence is unknown, and only a single family is reported.
- Sex ratio is not applicable beyond affected females. Whether homozygous males are infertile is not reported in the human data.

## 10. Diagnostics

- **Labs:** FSH, LH and estradiol (high gonadotropins and low estradiol are the standard POI pattern); AMH is not reported.
- **Genetic testing:** whole-exome sequencing found the variant. A POI gene panel including HSF2BP is reasonable. Karyotype and FMR1 testing are standard first-line exclusions for POI.
- **Differential diagnosis:** other recessive meiosis and DNA-repair POI genes (for example HFM1, MCM8, MCM9, STAG3), Turner syndrome, FMR1 premutation, autoimmune oophoritis and iatrogenic POI.

## 11. Prognosis

Ovarian function is lost permanently. Survival data are not available. Expected complications are those of estrogen deficiency (bone loss and cardiovascular risk), which I draw from general POI knowledge, not from POF19 sources.

## 12. Treatment

No POF19-specific therapy exists. Management is as for POI:

- Hormone replacement therapy. NCIT: Pharmacotherapy (NCIT:C15986), with estrogen/progestogen as `therapeutic_agent` bound to CHEBI.
- Bone and cardiovascular monitoring.
- Fertility options: oocyte donation, and early fertility counseling.
- Genetic counseling (NCIT:C15240).

No trials were identified, and I did not search ClinicalTrials.gov. Pharmacogenomics is not applicable.

## 13. Prevention

- Genetic counseling for relatives, with carrier testing of siblings in affected families.
- Prenatal or preimplantation testing is possible in principle once the familial variant is known.
- No primary prevention exists.

## 14. Other species

Orthologs are in mouse and other mammals. OMIA data were not checked. No natural disease is known.

## 15. Model organisms

- **Mouse knockouts (three independent lines):** meiotic failure, described in the sources I saw mainly in males.
- **Hsf2bp S167L knock-in mouse (eLife 2020):** hypomorphic. Females have reduced fertility and smaller litters. Meiocytes show reduced HSF2BP/BRME1 at recombination nodules, fewer RAD51/DMC1 foci and lower crossover frequency.
- **Cell and biochemical systems:** co-immunoprecipitation of the BRME1/HSF2BP complex with BRCA2, RAD51, RPA and PALB2.
- **Fidelity:** the S167L mouse recapitulates reduced female fertility, but the human phenotype is early ovarian failure, so fidelity is partial. A `modeled_mechanisms` link should note this limitation.
- Mouse-resource entries (MGI, IMPC, genOway knockout) were not verified.

## Gaps to close before curating

1. Fetch the eLife paper and its PMID with `just fetch-reference` (DOI 10.7554/eLife.56996, PMC7498267), then copy snippets from the cached text.
2. Confirm the HGVS nucleotide change, the hormone values, the third sister's data and the female knockout phenotype.
3. Read OMIM 619245 and the ClinGen validity record directly. Check ClinVar for HSF2BP variants.
4. Search PubMed for additional HSF2BP POI families published after 2020.
5. Run `just check-genereviews` for a GeneReviews baseline. A POI chapter may exist, though I expect no POF19-specific one.

## Sources

- [NORD: Premature ovarian failure 19](https://rarediseases.org/mondo-disease/premature-ovarian-failure-19/)
- [DrugMap disease DIS60A1W](https://drugmap.idrblab.net/data/disease/details/DIS60A1W)
- [OMIM 619245 mirror](https://0-www-ncbi-nlm-nih-gov.brum.beds.ac.uk/omim/619245)
- [Disease Ontology DOID:0112278](https://disease-ontology.org/term/DOID:0112278/owl)
- [eLife 2020;9:e56996](https://elifesciences.org/articles/56996) and [PMC7498267](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7498267/)
- [bioRxiv preprint](https://www.biorxiv.org/content/10.1101/2020.03.05.978007v1)
- [Nat Commun 2021, BRCA2–HSF2BP](https://link.springer.com/article/10.1038/s41467-021-24871-6)
- [Sci Adv 2023, BRCA2–HSF2BP ring disassembly by BRME1](https://www.science.org/doi/abs/10.1126/sciadv.adi7352)
- [Reprod Biol Endocrinol 2024, POI genetics review](https://link.springer.com/article/10.1186/s12958-024-01254-2)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 1 |
| References weighed for topical relevance | 4 |
| On topic | 1 |
| Off topic | 0 |

4 of 5 references resolved; the rest could not be looked up either way.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 12 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030985` (1 mention) - the report calls it "MONDO"; MONDO calls it **premature ovarian failure 19**
- `DOID:0112278` (5 mentions) - the report calls it "synonyms POF19, POI19"; DOID calls it **primary ovarian insufficiency 19**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000858` (1 mention) - the report calls it "Irregular menstruation, oligomenorrhea"; HP calls it **Irregular menstruation**
- `HP:0000837` (1 mention) - the report calls it "Elevated FSH / hypergonadotropism"; HP calls it **Increased circulating gonadotropin level**, and lists "Elevated serum gonadotropins" among its other names
- `GO:0007131` (1 mention) - the report calls it "GO: meiotic recombination"; GO calls it **reciprocal meiotic recombination**, and lists "female meiotic recombination" among its other names
- `CL:0000023` (1 mention) - the report calls it "CL: oocyte"; CL calls it **oocyte**
- `UBERON:0000992` (1 mention) - the report calls it "Organ:** ovary"; UBERON calls it **ovary**, and lists "animal ovary" among its other names
- `HP:0000007` (1 mention) - the report calls it "Autosomal recessive"; HP calls it **Autosomal recessive inheritance**, and lists "Autosomal recessive" among its other names