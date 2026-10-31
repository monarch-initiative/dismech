---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-15T20:02:11.178692'
end_time: '2026-10-15T20:03:26.087661'
duration_seconds: 74.91
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Lethal Congenital Glycogen Storage Disease of Heart
  mondo_id: MONDO:0009867
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
  web_search_requests: 4
  num_turns: 6
  total_cost_usd: 0.8293428999999999
  session_id: 1411d6e0-a3a9-57ef-a642-a756ff0785bd
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 10
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
  total_terms: 21
  verified: 18
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 5
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: DOID:0090101
    reported_labels:
    - Disease Ontology
    ontology_label: lethal congenital glycogen storage disease of heart
  labels_variant: 1
  unresolvable_prefixes:
  - MIM
  - ICD10CM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lethal Congenital Glycogen Storage Disease of Heart
- **MONDO ID:** MONDO:0009867 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Lethal Congenital Glycogen Storage Disease of Heart** covering all of the
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

# Lethal Congenital Glycogen Storage Disease of Heart (MONDO:0009867): Research Report

**Verification status.** I ran four web searches, which returned database entries and citation snippets. I did not read any full text. PMIDs and DOIs below are marked *verified* only where a search result showed them. Everything else is background knowledge, flagged "unverified, check before citing". No snippets were checked against `references_cache/`. Run `just fetch-reference` and `just validate-disorders` before any of this goes into a KB entry.

Two source caveats:
- A Monarch/dismech page for `PRKAG2_Cardiac_Syndrome` surfaced in the results. It looks like an AI-generated draft whose ORPHA and MONDO codes are unverified, so I did not use it as evidence.
- One search summary said Torok 2017 describes eight infants. A second search said three. The Duke and Springer abstracts point to **three**, so I use three. Confirm against the abstract.

## 1. Disease Information

**Overview.** This is a rare, usually fatal, fetal- or neonatal-onset cardiac glycogenosis. It presents as severe biventricular hypertrophic cardiomyopathy with vacuolated, glycogen-filled cardiomyocytes and pre-excitation (Wolff-Parkinson-White-like) conduction anomalies. It was originally attributed to "heart-specific phosphorylase kinase deficiency". The recurrent activating **PRKAG2 p.Arg531Gln (R531Q)** variant explains a subset of cases. This is the severe, early-onset end of the PRKAG2 cardiac syndrome spectrum.

**Identifiers**
- OMIM **#261740**, "Glycogen storage disease of heart, lethal congenital". Phenotype-gene entry: 7q36.1, AD, PRKAG2 (602743) ([OMIM mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/261740); [LOVD](https://databases.lovd.nl/shared/diseases/02013)).
- Disease Ontology [DOID:0090101](https://disease-ontology.org/term/DOID:0090101) cross-references MIM:261740, ORDO:439854, ICD10CM:E74.0 and ICD10CM:G73.6.
- MONDO:0009867 comes from the template. I did not independently resolve it.
- Orphanet, MeSH and ICD-11 codes: not verified.
- KEGG disease entry: [H01956](https://www.kegg.jp/entry/H01956).

**Synonyms.** Glycogen storage disease of heart, lethal congenital; phosphorylase kinase deficiency of heart (or "in heart muscle only"); fatal congenital hypertrophic cardiomyopathy due to glycogen storage disease; fatal congenital nonlysosomal cardiac glycogenosis ([PhenoDis](https://iegext02.helmholtz-munich.de/phenodis/disease/show/12762)).

**Data provenance.** The case series are individual-patient reports, mostly post-mortem or infant clinical data. OMIM and Disease Ontology are aggregated disease-level resources.

## 2. Etiology

- **Causal factor.** It is genetic. Burwinkel et al. found identical heterozygous R531Q PRKAG2 missense mutations in 3 of 5 patients, and no mutations in the phosphorylase kinase or glycogen phosphorylase genes in the four patients examined for them. They concluded that the fatal congenital nonlysosomal cardiac glycogenosis phenotype is genetically heterogeneous (Am J Hum Genet 2005; [PMID:15877279](https://pubmed.ncbi.nlm.nih.gov/15877279/), [PMC1196441](https://pmc.ncbi.nlm.nih.gov/articles/PMC1196441), *verified*).
- **Other de novo variants.** Akman et al. (Pediatr Res 2007, [PMID:17667862](https://pubmed.ncbi.nlm.nih.gov/17667862), *verified*) report a girl with severe septal hypertrophy who died at 5 months, with glycogen accumulation at autopsy. She carried a novel heterozygous R384T variant absent from the father's DNA (likely de novo).
- **Risk, protective and environmental factors.** None known. I found no modifier genes, protective variants or gene-environment interactions in the sources reviewed.

## 3. Phenotypes (suggested HPO terms are unverified)

Look up each HPO term with `runoak` before binding it.

| Phenotype | Suggested HPO | Notes |
|---|---|---|
| Hypertrophic cardiomyopathy, biventricular | HP:0001639 | Nonobstructive; fetal or neonatal onset |
| Cardiomyocyte vacuolization / glycogen storage | HP:0011675 and storage-related terms | Check term applicability |
| Short PR interval / pre-excitation (WPW-like) | HP:0005165, HP:0001716 | |
| Congestive heart failure | HP:0001635 | |
| Pulmonary edema | HP:0100598 | |
| Neonatal hypoglycemia | HP:0001998 | Listed in OMIM clinical synopsis |
| Neonatal death | HP:0003811 | |

The clinical picture comes from OMIM and Burwinkel et al.: patients died of hemodynamic and respiratory failure secondary to hypertrophic nonobstructive cardiomyopathy, with WPW-like conduction anomalies and prenatal onset. Frequencies per phenotype are not available from the sources I read. Quality-of-life data are not applicable given early lethality.

## 4. Genetic and Molecular Information

- **Gene.** PRKAG2, 7q36.1. It encodes the γ2 regulatory subunit of AMP-activated protein kinase (AMPK). The HGNC ID should be looked up (the repo uses lowercase `hgnc:`).
- **Variants.**
  - R531Q is recurrent and activating.
  - R384T (Akman 2007) was likely de novo.
  - A K475E de novo variant with prenatal onset was surfaced by search, not confirmed.
  - PRKAG2 variants have also been reported in infants who mimic Pompe disease (Torok et al., J Inherit Metab Dis 2017;40:823–830, [DOI:10.1007/s10545-017-0072-0](https://doi.org/10.1007/s10545-017-0072-0), *verified*; PMID not retrieved).
  - A prenatally diagnosed neonate with a PRKAG2 missense variant and poor prognosis is reported by Gorla et al., J Pediatr Genet 2018 ([DOI:10.1055/s-0038-1657763](https://www.thieme-connect.de/products/ejournals/html/10.1055/s-0038-1657763), *verified*; PMID not retrieved).
- **Functional consequence.** R531Q protein showed >100-fold reduced binding affinity for the regulatory nucleotides AMP and ATP, with enhanced basal activity and increased phosphorylation of the α-subunit (Burwinkel 2005). Treat this as an altered-nucleotide-sensing gain of function.
- **ClinVar/ClinGen classification and gnomAD frequency.** Not retrieved. Do not fill `gene_disease_validity` without a ClinGen CGGV record.
- **Germline or somatic.** Germline, often de novo.
- **Genetic heterogeneity.** Some patients carry no PRKAG2 mutation (Burwinkel 2005), so the causal gene for those cases is unresolved.
- **Epigenetic, modifier and chromosomal data.** None found.

## 5. Environmental Information

No environmental, lifestyle or infectious contributors are known. The exception is the diagnostic lookalike below: infantile Pompe disease must be excluded.

## 6. Mechanism / Pathophysiology

**Causal chain.** Steps 4 to 6 are stated by the sources only at the level of "enhanced AMPK activity". The glycogen mechanism is inferred from the general PRKAG2 literature (not verified here).
1. A heterozygous activating PRKAG2 missense variant (recurrently R531Q, often de novo) alters the AMPK γ2 nucleotide-binding region. *Demonstrated.*
2. The mutant γ2 subunit shows >100-fold reduced AMP and ATP binding, with enhanced basal activity and increased α-subunit phosphorylation. *Demonstrated in vitro by Burwinkel 2005.*
3. This leads to constitutive, energy-state-uncoupled AMPK activity in cardiomyocytes. *Inferred.*
4. This is expected to promote excess glucose uptake and glycogen synthesis (unverified; check the PRKAG2 mechanism literature) and so produces nonlysosomal glycogen accumulation and vacuolated cardiomyocytes. *Inferred.*
5. Glycogen-laden myocytes lead to massive biventricular hypertrophy from the fetal period. *Inferred.*
6. Accessory-pathway and conduction abnormalities (WPW-like, short PR) arise alongside. Mechanism is *not resolved here*.
7. Hypertrophy leads to heart failure, respiratory failure and neonatal death.

**Suggested ontology terms (unverified):** GO glycogen biosynthetic process (GO:0005978) and AMPK-related terms (look up in OLS); CL cardiac muscle cell (CL:0000746); UBERON heart (UBERON:0000948).

**Old model.** Early cases were labelled "heart-specific phosphorylase kinase deficiency". Burwinkel 2005 found no mutations in the phosphorylase kinase or glycogen phosphorylase genes in the four patients examined for them, which argues against that explanation.

**Omics, single-cell and functional screens.** None identified.

## 7. Anatomical Structures Affected

- **Primary organ:** heart, biventricular myocardium (UBERON:0000948; ventricle terms to be looked up).
- **Cells:** cardiac muscle cells (CL:0000746).
- **Subcellular:** cytoplasm. The glycogen is nonlysosomal, which separates it from Pompe disease.
- **Secondary involvement:** lungs (edema).
- **Lateralization:** bilateral/biventricular.

## 8. Temporal Development

Onset is prenatal or neonatal (congenital). The course is rapid and progressive, with death in the neonatal period or early infancy. Akman's patient died at 5 months, so survival can extend into infancy in at least some cases. No remission or critical-period data were found.

## 9. Inheritance and Population

- **Inheritance:** autosomal dominant per OMIM. The reported cases are mostly de novo or isolated, so the practical picture is sporadic de novo heterozygous variants. Germline mosaicism and recurrence risk were not addressed in the sources I read. A founder effect for R531Q is not documented in the retrieved material.
- **Prevalence and incidence, sex ratio, geography:** not available from the sources reviewed. The MONDO/Orphanet prevalence class is not verified. Use the `NOT_YET_DOCUMENTED` band only after checking Orphanet.

## 10. Diagnostics

- **Clinical and imaging:** a prenatal or neonatal echocardiogram showing biventricular hypertrophy, and an ECG showing a short PR interval or pre-excitation.
- **Pathology:** vacuolated cardiomyocytes with excess nonlysosomal glycogen at biopsy or autopsy.
- **Biochemistry:** phosphorylase kinase activity can look deficient in cardiac tissue, which is why the old label arose (Akman 2007).
- **Genetic testing:** PRKAG2 sequencing is the key test. Gene panels for cardiomyopathy or glycogen storage should include it. The Duke group (Torok 2017) recommends PRKAG2 sequencing before a Pompe diagnosis is accepted.
- **Differential diagnosis:** Pompe disease (GAA deficiency, lysosomal glycogen), Danon disease (LAMP2), other infantile hypertrophic cardiomyopathies and other glycogenoses. An Austin et al. 2017 case report (Mol Genet Metab) describes a patient given enzyme replacement therapy for presumed Pompe disease before a PRKAG2 mutation was found, as reported by the search summary; PMID not retrieved.
- **Screening:** no established newborn screening. Cascade testing is not documented here.

## 11. Outcome / Prognosis

The condition is generally fatal in the neonatal period or early infancy, with death from hemodynamic and respiratory failure (Burwinkel 2005). Gorla 2018 links a prenatally diagnosed case to poor prognosis. Registry survival figures and quality-of-life measures were not found.

## 12. Treatment

No disease-specific therapy is documented in the retrieved sources. Treatment is supportive (heart failure management, arrhythmia management). Cardiac transplantation is possible in principle for infants but is not documented in the sources I read, so I make no claim about outcomes. Enzyme replacement therapy is **inappropriate** unless Pompe disease is truly present, as the Austin case illustrates. No gene therapy or RNA therapy trials were identified. ClinicalTrials.gov was not searched, so no NCT identifiers are given. Suggested NCIT terms (look up before binding): Supportive Care (NCIT:C15747, listed in the repo's CLAUDE.md), Pharmacotherapy (NCIT:C15986), Organ Transplantation (NCIT:C15289).

## 13. Prevention

Primary prevention is not possible. Genetic counseling is appropriate (NCIT:C15240). Prenatal diagnosis is feasible once a family variant is known. Because most reported variants are de novo, recurrence risk is low but germline mosaicism is not excluded. This is unverified.

## 14. Other Species

Not verified. OMIA lists no confirmed natural disease for this phenotype as far as I know. Not searched.

## 15. Model Organisms

My search for Prkag2 transgenic mouse models returned nothing. From background knowledge (unverified, find PMIDs before citing), transgenic mouse models of PRKAG2 variants (such as N488I) show cardiac glycogen storage, hypertrophy and pre-excitation. These models are generally the adult-onset, milder PRKAG2 syndrome, so they probably capture the severe lethal neonatal form poorly. Treat the fidelity as an open question.

## Gaps Before Curation

1. Fetch and read the abstracts of PMID:15877279 and PMID:17667862 and take snippets only from the cache.
2. Resolve the Torok and Gorla PMIDs. Check the case counts (three vs. eight for Torok).
3. Verify MONDO:0009867, HGNC and all HPO/GO/CL/UBERON/NCIT IDs.
4. Search ClinGen, ClinVar, Orphanet, GeneReviews and ClinicalTrials.gov, none of which I reached.
5. Decide the lump/split question against the existing `PRKAG2_Cardiac_Syndrome` entry. This disease may be better treated as a subtype or severe arm of that entry than as a separate one.

**Sources**
- [Burwinkel et al. 2005, PMID 15877279](https://pubmed.ncbi.nlm.nih.gov/15877279/) / [PMC1196441](https://pmc.ncbi.nlm.nih.gov/articles/PMC1196441)
- [Akman et al. 2007, PMID 17667862](https://pubmed.ncbi.nlm.nih.gov/17667862)
- [Torok et al. 2017](https://doi.org/10.1007/s10545-017-0072-0)
- [Gorla et al. 2018](https://www.thieme-connect.de/products/ejournals/html/10.1055/s-0038-1657763)
- [OMIM 261740 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/261740)
- [LOVD disease 02013](https://databases.lovd.nl/shared/diseases/02013)
- [Disease Ontology DOID:0090101](https://disease-ontology.org/term/DOID:0090101)
- [KEGG H01956](https://www.kegg.jp/entry/H01956)
- [PhenoDis](https://iegext02.helmholtz-munich.de/phenodis/disease/show/12762)

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
| Terms checked | 21 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 7 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0090101` (5 mentions) - the report calls it "Disease Ontology"; DOID calls it **lethal congenital glycogen storage disease of heart**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001639` (1 mention) - the report calls it "Hypertrophic cardiomyopathy, biventricular"; HP calls it **Hypertrophic cardiomyopathy**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MIM`, `ICD10CM`.