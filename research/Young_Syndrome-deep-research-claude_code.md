---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-14T12:52:45.650304'
end_time: '2026-10-14T12:55:44.083569'
duration_seconds: 178.43
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Young Syndrome
  mondo_id: MONDO:0010220
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
  - claude-haiku-5-5
  - claude-opus-5-5
  web_search_requests: 4
  num_turns: 17
  total_cost_usd: 2.1513418
  session_id: f8ae34a4-fb4f-4d97-bc50-47238c206451
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 18
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 10
  quotes_valid: 10
  relevance_assessed: 24
  on_topic: 15
  off_topic: 3
  off_topic_references:
  - PMID:30659149
  - PMC:PMC8269963
  - PMC:PMC6397547
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 32
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0010220
    reported_labels:
    - MONDO
    ontology_label: Young syndrome
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Young Syndrome
- **MONDO ID:** MONDO:0010220 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Young Syndrome** covering all of the
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

I've read the 19 cached abstracts and am now checking the outside identifiers (OMIM, Orphanet, MONDO) and the mercury and CFTR literature.

I've collected the sources. Next I'm checking the suggested ontology IDs against the repository's term caches, so none of them come from memory.

# Young Syndrome: Research Report

**Target:** Young syndrome (MONDO:0010220) · **Category:** Complex · **Report date:** 2026-10-14

**How the citations were checked.** 19 PMIDs already have a `references_cache/` file on this branch. Quotes from those PMIDs were copied from the cached abstract or full text. Sources that are not cached are marked **[not cached]**, so fetch them with `just fetch-reference` before quoting them in the KB. Ontology CURIEs marked ✓ were read from the repository's `cache/<prefix>/terms.csv` during this session. Unmarked CURIEs are leads, and each one needs a lookup before it is used.

---

## Summary of the evidence (read this first)

Whether Young syndrome is a distinct disease is itself disputed. The literature supports three positions:

1. **A real clinical entity of unknown cause.** Obstructive azoospermia comes from the epididymis being blocked by thick secretions, and occurs alongside chronic sinopulmonary infection. Handelsman 1984 (PMID:6689737) is the main source.
2. **A mostly historical condition caused by childhood mercury exposure.** Incidence dropped sharply in men born after mercury (calomel) was removed from UK teething powders in 1955 (Hendry 1993, PMID:8292944 **[not cached]**; Arya 2009, PMID:19128521; Brown 2025, PMID:40287162).
3. **A misdiagnosed form of primary ciliary dyskinesia (PCD).** In particular, PCD caused by defects in the C1d projection of the ciliary central apparatus (for example CFAP221) gives normal electron microscopy (EM), normal nasal NO and normal situs. It is therefore missed by the classical tests that were used to "exclude" PCD when Young syndrome was defined (Ito 2025, PMID:38960684; Wohlgemuth 2024, PMID:39362668).

Two lines of evidence count against Young syndrome being a mild form of cystic fibrosis (CF): normal sweat chloride, and a CFTR mutation rate no higher than the background carrier rate (PMID:7551394).

**What this means for curation:** the stub's `entry_type` decision is not obvious, and the `notes` should record the reasoning. A defensible choice is a `DISEASE` entry with low-confidence, hypothesis-grouped mechanisms, namely mercury toxicity versus an undiagnosed motile ciliopathy. Each grouping should be marked `EMERGING` or `HYPOTHETICAL` rather than `ESTABLISHED`.

---

## 1. Disease Information

**Overview.** Young syndrome is a triad found mainly in middle-aged men:
- obstructive azoospermia, with normal spermatogenesis and an enlarged, sperm-filled caput epididymis;
- chronic or recurrent rhinosinusitis;
- recurrent bronchitis or bronchiectasis.

It is diagnosed by exclusion, after CF and PCD have been ruled out.

> "We studied 29 men with Young's syndrome, a combination of obstructive azoospermia and chronic sinopulmonary infections. Men with this syndrome have only mildly impaired respiratory function and normal spermatogenesis; the azoospermia is due to obstruction of the epididymis by inspissated secretions." — PMID:6689737 (Handelsman et al., *NEJM* 1984)

> "The diagnosis is based on the occurrence of chronic sinopulmonary infections, persistent azoospermia, normal spermatogenesis, and characteristic epididymal findings, as well as exclusion of cystic fibrosis and the immotile-cilia syndrome." — PMID:6689737

**Identifiers.**

| System | ID | Note |
|---|---|---|
| MONDO | MONDO:0010220 | Not in `cache/mondo/terms.csv`, so confirm the label via OLS |
| OMIM | 279000 | Per [MedGen](https://https.ncbi.nlm.nih.gov/medgen/137934). omim.org returned 403 to a fetch |
| Orphanet | ORPHA:3471 | Per MedGen. Run `just fetch-reference ORPHA:3471` to get a quotable record |
| MedGen | C0221040 / 137934 | |
| ICD-10 | No specific code | Usually coded through its components (N46 male infertility, J47 bronchiectasis) |

**Synonyms:** Young's syndrome; sinusitis–infertility syndrome; Barry–Perkins–Young syndrome; azoospermia–sinusitis–bronchiectasis.

> "Young´s syndrome also known as Barry-Perkins-Young syndrome or sinusitis-infertility syndrome is a rare, inherited syndrome commonly seen in middle-aged men with chronic rhinosinusitis, nasal polyps, infertility and bronchiectasis." — PMID:39119117

**Name collision (a Named Entity Confusion risk).** "Young syndrome" also names an unrelated condition:

> "As an incidental finding, we found that the term Young's syndrome refers to two different medical conditions." — PMID:19128521

When searching, filter out the Young–Simpson / Say–Barber–Biesecker–Young–Simpson (KAT6B) syndrome, which is a different disease.

**Source of the information:** case series and aggregated reviews. There are no registries or EHR cohorts.

---

## 2. Etiology

### Causal factors (unresolved)

**(a) Childhood mercury exposure (environmental hypothesis).** This is the only cause any source documents. Hendry et al. 1993 (*BMJ* 307:1579; PMID:8292944 **[not cached]**) followed 274 men who had epididymovasostomy for obstructive azoospermia. Young syndrome was diagnosed in 114 of 227 men (50%) born up to 1955, against 8 of 47 men (17%) born afterwards. 1955 is the year calomel (mercurous chloride) was withdrawn from UK teething powders and worm treatments, and the drop parallels the disappearance of pink disease (acrodynia). See also Hendry et al. 1996, *BMJ*, "Declining sperm count. Increasing evidence that Young's syndrome is associated with mercury" (PMID:8664779). That PMID is cached, but its content is unavailable, so it cannot be quoted.

> "The only documented aetiological factor is mercury exposure in childhood, an event that is seldom currently encountered; this would support our theory of the extinction of the condition." — PMID:19128521

> "This report details a case of a man who suffered from pink disease as a child following his mother applying teething powder containing inorganic mercury to his gums for 12 weeks, from the age of 6 months. … Throughout his lifetime, however, the man (in his 70s) has been diagnosed as infertile, and with bronchiectasis…" — PMID:40287162

The Ito 2025 full text summarises a second Hendry series: "In a prospective study conducted between 1975 and 1993 on 146 subfertile men with epididymal obstruction, 82% were diagnosed with Young's syndrome and mercury exposure was identified in 11 cases" (PMID:38960684, discussion). This sentence is a `BACKGROUND` quote: Ito restates another group's result.

**(b) Undiagnosed motile ciliopathy, i.e. PCD with normal EM (genetic hypothesis).**

> "He had normal electron microscopy findings, normal nasal nitric oxide levels (116 nL/min), and no situs inversus. However, we found compound heterozygous variants considered pathogenic in CFAP221. This led to a diagnosis of primary ciliary dyskinesia (PCD). … Young's syndrome may be a phenotype of PCD." — PMID:38960684

> "C1d-defective primary ciliary dyskinesia is associated with normal situs composition, normal nasal nitric oxide production rates, normal ciliary ultrastructure by transmission electron microscopy and normal ciliary beating by high-speed videomicroscopy analysis." — PMID:39362668

This matters because the original definition excluded PCD by EM, which every C1d-defective form passes. Some historical Young syndrome cases may therefore have been C1d-defective PCD. That conclusion is inferred: no study has re-genotyped a historical Young syndrome cohort.

**(c) CFTR: not supported as a cause.**

> "Of 26 Young syndrome chromosomes, we identified one with the recognized CF mutation delta F508. The incidence of CFTR mutations (1 in 26) did not differ significantly from the expected carrier frequency in this population. In summary, it is unlikely that the typical Young syndrome patient has a clinical disease associated with CFTR mutation on both alleles." — PMID:7551394 (Friedman et al., *AJRCCM* 1995)

Related cached letters that cannot be quoted (content unavailable): PMID:8100886 (*Lancet* 1993, ΔF508) and PMID:9800754 (*Lancet* 1998, "Cystic fibrosis, Young's syndrome, and normal sweat chloride"). Ito 2025 notes that isolated cases of Young syndrome with CFTR mutations have been reported, so CF should still be excluded.

### Risk factors
- **Environmental:** mercurous chloride in teething powder or vermifuges during infancy; exposure to mercury, ECTO:0001571 ✓.
- **Sex:** the defining feature, obstructive azoospermia, applies only to men. StatPearls says women may have mildly reduced fertility (PMID:30969689). That claim is weakly sourced.
- **Age and birth cohort:** men born before 1955 in the UK and northern Europe.
- **Genetic:** no confirmed locus. Orphanet and MedGen list autosomal recessive inheritance (HP:0000007 ✓). That listing reflects the older "inherited" framing and has no supporting linkage data.

### Protective factors and gene–environment interaction
There are no data. The mercury hypothesis implies that withdrawing calomel was a primary-prevention event at population level.

---

## 3. Phenotypes

| Phenotype | Suggested HPO | Frequency / notes | Source |
|---|---|---|---|
| Obstructive azoospermia | HP:0000027 Azoospermia ✓ (no "obstructive azoospermia" row in the cache, so search HPO for a narrower term) | Defining, about 100% | PMID:6689737 |
| Enlarged caput epididymis with inspissated material | HP:0009714 Abnormal epididymis morphology ✓ | Characteristic | PMID:6689737; PMID:38960684 discussion |
| Normal spermatogenesis | Not a phenotype; diagnostic qualifier | — | PMID:6689737 |
| Male infertility | HP:0003251 ✓ | Defining | PMID:19128521 |
| Chronic rhinosinusitis | HP:0011109 Chronic sinusitis ✓ / HP:0011108 Recurrent sinusitis ✓ | Common but poorly defined | PMID:19128521 |
| Nasal polyps | HP:0100582 Nasal polyposis ✓ | Reported, frequency unknown | PMID:36196705; PMID:8922141 |
| Bronchiectasis | HP:0002110 ✓ | Variable, often mild | PMID:39119117; PMID:38960684 |
| Recurrent bronchitis / lower respiratory infection | HP:0004469 ✓ / HP:0002783 ✓ | Most patients | PMID:7551394 |
| Productive cough | HP:0031245 ✓ | Common | PMID:36196705 |
| Impaired lung mucociliary clearance (lab/physiologic) | No HP row cached; bind GO:0120197 mucociliary clearance ✓ with `DECREASED` on a pathophysiology node | n=14, significantly reduced | PMID:7307631 |
| Mildly reduced FEV1 | Look up an HP term | Mean 74% predicted (range 48–100%) | PMID:7551394 |

On the sinus component, Arya 2009 (PMID:19128521) found that "the diagnosis of sinusitis in Young's syndrome was crude and poorly defined." Frequencies for the sinus features should be treated as unreliable.

**Onset and course:** onset is adult, usually first recognised during an infertility work-up in the 30s or 40s. In the Friedman cohort the mean age was 43 (range 32–50) (PMID:7551394). Respiratory disease is chronic, mild and slowly progressive. There was no chronic *S. aureus* or *P. aeruginosa* colonisation, which distinguishes it from CF.

**Quality of life:** no instrument-based data exist. One case report states: "An accurate diagnosis of YS is usually made late, which reduces patients' quality of life and leads to chronic respiratory problems" (PMID:36196705).

---

## 4. Genetic / Molecular Information

- **No causal gene has been established.** Do not add a `CAUSATIVE` gene row.
- **CFAP221** (hgnc:33720 ✓): one compound-heterozygous case with a Young phenotype that was reclassified as PCD (PMID:38960684). Should a CFAP221 row be included, the defensible framing is a phenocopy or differential diagnosis, or a `SUSCEPTIBILITY`-style lead in `notes`. It should not be causal. On the MalaCards claim that OMIM's CILD55 (CFAP221) entry mentions a Young syndrome presentation ([MalaCards](https://malacards.org/card/ciliary_dyskinesia_primary_55)): verify it against OMIM before citing.
  - Supporting evidence for CFAP221 in mild PCD: "Subtle abnormalities in the protein composition of the ciliary central apparatus were consistent with the asynchronous, circular motion of cilia and reduced ciliary beat frequency in the proband; importantly, the motility of proband's sperm cells was within the normal range." (PMID:40250778). Normal sperm motility fits the Young pattern, because the obstruction lies outside the sperm and the sperm themselves are normal.
- **Other C1d genes** (CFAP46, CFAP54, CFAP74; PMID:39362668) are plausible candidates by the same logic. None has been reported in Young syndrome.
- **DNAH5** (hgnc:2950 ✓): PCD caused by DNAH5 gives epididymal-head dilation and oligozoospermia with motile sperm, "similar to Young's syndrome" (Ito 2025 discussion; this is background).
- **CFTR** (hgnc:1884 ✓): tested and not enriched (PMID:7551394). This is a negative finding and suits a `REFUTE` evidence item on any CF-mechanism claim.
- No ClinGen classification, no ClinVar disease assertion, no epigenetic data and no chromosomal abnormality has been reported.

---

## 5. Environmental Information

- **Exposure:** inorganic mercury, as mercurous chloride (calomel), in teething powders and anthelmintics. Exposure to mercury is ECTO:0001571 ✓. Search ECTO further for an ingestion-route or calomel-specific term and record the queries. The CHEBI CURIEs for mercury and calomel are not cached and need a lookup.
- **Linked childhood disease:** pink disease (acrodynia). PMID:40287162 links the two.
- **Infectious agents:** none causal. Secondary infections are intermittent and non-specific. In the Friedman cohort "none was chronically colonized with Staphylococcus aureus or Pseudomonas aeruginosa" (PMID:7551394).
- **Lifestyle:** tobacco was matched in the clearance study (PMID:7307631). No independent role has been shown.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

**Branch A: mercury hypothesis** (epidemiological; mechanism inferred)
1. Infant exposure to inorganic mercury (calomel teething powder) → *(inferred)* lasting injury to secretory or ciliated epithelium in the airway and the excurrent ducts of the male reproductive tract. No histological study shows this.
2. → Abnormal, thickened (inspissated) mucus in the airways and in the epididymal lumen. Handelsman reports the epididymal secretions directly. For the airway mucus, the evidence is indirect: tip disorientation is "more likely to be a consequence of abnormal mucus", PMID:1387740.
3. → Impaired mucociliary clearance, even though cilia are structurally and kinetically normal (shown, PMID:7307631, PMID:1387740).
4a. → Mucus stasis → recurrent sinobronchial infection → chronic rhinosinusitis and bronchiectasis.
4b. → Obstruction at the caput epididymis → sperm cannot reach the ejaculate → obstructive azoospermia, with spermatogenesis intact (shown, PMID:6689737).

**Branch B: occult motile-ciliopathy hypothesis** (genetic; one case plus model data)
1. Biallelic loss-of-function variants in a central-apparatus C1d gene (e.g. CFAP221) → subtle C1d defect (shown in PCD, PMID:39362668, PMID:40250778).
2. → Abnormal (circular, asynchronous) ciliary waveform. Beat frequency and EM are normal or near normal, so classical PCD tests are negative.
3a. → Reduced airway ciliary transport → chronic airway infection and mild bronchiectasis (shown in PCD; inferred for Young syndrome).
3b. → *(inferred from mouse models)* Defective motile cilia in the efferent ducts → sperm are not kept in suspension → sperm agglutinate and obstruct the efferent ducts or caput epididymis → obstructive azoospermia with normal sperm motility.
   - Mouse support: Yuan et al. 2019 *PNAS* (PMID:30659149 **[not cached]**, [PMC6397526](https://pmc.ncbi.nlm.nih.gov/articles/PMC6397526)). In miR-34b/c / miR-449 knockout mice, loss of efferent-duct motile cilia causes sperm agglutination, luminal obstruction and sperm granulomas. The efferent-duct cilia beat in changing directions to keep sperm suspended.
   - Further support: Terré et al. 2019 *Development* (GEMC1/MCIDAS/CCNO; dev162628; PMID to be resolved) and DNAH5-deficient mice with immotile efferent-duct cilia ([PMC8269963](https://pmc.ncbi.nlm.nih.gov/articles/PMC8269963); PMID to be resolved).
   - Ito 2025 summarises: "Impaired ciliary motility of the efferent duct may explain the obstructive azoospermia observed in patients with Young's syndrome."

**Branch C: CF-spectrum (refuted for the typical patient).** Sweat chloride is normal, pancreatic function and nasal potential difference are normal, and CFTR mutations are no more frequent than background (PMID:7551394). Model this as a `REFUTE` item or a `discussions` entry, not as a node.

### Ciliary and mucus findings in detail
> "Ciliary beat frequency and the incidence of microtubular defects and numbers of dynein arms did not differ between patients with Young's syndrome and control subjects. … at the ciliary tip ciliary deviation (21.9 degrees) was greater than in healthy subjects (14.5 degrees)." — PMID:1387740

> "Lung mucociliary transport was significantly reduced in patients with Young's syndrome compared to 14 control subjects…" — PMID:7307631

> "Patients with YS did not have pathognomonic ultrastructural changes, whereas patients with PCD had a large number of ciliary abnormalities…" — PMID:9213847

### Suggested bindings

| Kind | Term |
|---|---|
| GO | GO:0120197 mucociliary clearance ✓ (DECREASED) |
| GO | GO:0003351 epithelial cilium movement involved in extracellular fluid movement ✓ (Branch B) |
| GO | GO:0003341 cilium movement ✓ |
| GO | GO:0070254 mucus secretion ✓ (ALTERED or INCREASED viscosity; the qualitative claim is about secretion character, so justify the modifier) |
| CL | CL:0000019 sperm ✓ |
| CL | CL:0000160 goblet cell ✓ |
| CL | CL:0002480 nasal mucosa goblet cell ✓ |
| CL | Multiciliated epithelial cell / efferent-duct ciliated cell: **look up** (not cached) |

**Biological scale tags:** the exposure and variant nodes are MOLECULAR; ciliary waveform and mucus are CELLULAR; epididymal obstruction and bronchiectasis are TISSUE.

**Omics:** none. There are no GEO, proteomic or single-cell datasets specific to Young syndrome; the `datasets:` section should stay empty.

---

## 7. Anatomical Structures Affected

| Level | Structures |
|---|---|
| Primary sites | Epididymis UBERON:0001301 ✓ (caput; look up "head of epididymis" and "efferent duct"); bronchus UBERON:0002185 ✓; respiratory airway UBERON:0001005 ✓; paranasal sinus UBERON:0001825 ✓; nasal cavity epithelium UBERON:0005384 ✓ |
| Spared | Testis (spermatogenesis normal), vas deferens (patent, unlike CBAVD in CF), pancreas, sweat gland |
| Subcellular | Motile cilium axoneme and central apparatus (Branch B); extracellular mucus |
| Laterality | Bilateral epididymal involvement; bronchiectasis often bilateral and lower-lobe (PMID:39119117 CT description) |

---

## 8. Temporal Development

- **Onset:** adult, presenting at roughly 30–50 years. Respiratory symptoms often date from childhood: in one case report, "cough, sputum, recurrent nasal congestion, and shortness of breath lasting for more than ten years" (PMID:36196705).
- **Course:** chronic, mild and slowly progressive on the airway side, with stable azoospermia.
- **Remission:** none spontaneous. Fertility can be restored with surgery or ART.
- **Critical period (mercury hypothesis):** infancy, during teething, around 6 months of age (PMID:40287162).
- **Suggested `progression:` phases:** childhood sinopulmonary symptoms → adult infertility presentation → established bronchiectasis.

---

## 9. Inheritance and Population

- **Prevalence:** the only estimate is Handelsman's 1984 claim of a "prevalence comparable to that of Klinefelter's syndrome" (PMID:6689737), roughly 1 in 500–1,000 men. That claim is speculative and predates the post-1955 decline. Model it as `measure_type: UNKNOWN` with a qualitative class, or `CASES_IN_LITERATURE`, and record the original phrasing in `notes`. A more defensible statement is that the condition is now rare or possibly extinct (PMID:19128521).
- **Share of obstructive azoospermia:** 50% in men born up to 1955 versus 17% in men born after (Hendry 1993 **[not cached]**).
- **Inheritance:** stated as autosomal recessive by Orphanet and MedGen, but unproven. Familial case reports are lacking.
- **Population:** northern European men: "all were of northern European extraction" (PMID:7551394). A UK-centred literature, with case reports from Turkey, Japan and India.
- **Sex ratio:** defined in men.

---

## 10. Diagnostics

**Clinical criteria (Handelsman 1984):**
- chronic sinopulmonary infection;
- persistent azoospermia;
- normal spermatogenesis on testicular biopsy;
- characteristic epididymal findings (distended caput, inspissated material);
- exclusion of CF and of PCD.

**Tests:**

| Test | Finding in Young syndrome |
|---|---|
| Semen analysis | Azoospermia, normal volume and pH (distinguishes it from CBAVD) |
| Hormones | FSH, LH and testosterone normal (PMID:38960684) |
| Testicular biopsy / TESE | Normal spermatogenesis |
| Scrotal or transrectal ultrasound | Obstructive pattern (PMID:39119117) |
| Sweat chloride | Normal; mean 29 mEq/L (PMID:7551394). Use a LOINC code here, via `just loinc-seed-cache`; never type the label |
| Nasal potential difference | Normal |
| Chest HRCT | Bronchiectasis |
| Nasal brushing: TEM / CBF | Normal (PMID:1387740, PMID:9213847) |
| Radioaerosol mucociliary clearance | Reduced (PMID:7307631) |

**Genetic testing (the change since 2024):** run a PCD gene panel or exome that includes the C1d genes CFAP221, CFAP46, CFAP54 and CFAP74, plus CFTR. Normal nNO, TEM and HSVM no longer exclude PCD:

> "Despite chronic respiratory disease, PICADAR does not reliably detect this primary ciliary dyskinesia type. … To enable diagnosis, genetic testing should be prioritised in future diagnostic guidelines." — PMID:39362668

**Differential diagnosis:**
- CF / CFTR-related disorder (CBAVD, abnormal sweat test);
- PCD (situs inversus, low nNO, sperm immotility in most genotypes);
- immunodeficiency (CVID);
- ADGRG2-related CBAVD;
- post-infectious epididymal obstruction.

**Screening:** none applicable.

---

## 11. Outcome / Prognosis

- **Life expectancy:** no data. Respiratory function is "only mildly impaired" (PMID:6689737), and the prognosis is considered benign compared with CF.
- **Morbidity:** infertility, plus chronic sinopulmonary infection with hospitalisations if the diagnosis is delayed (PMID:36196705).
- **Fertility:** "Pregnancies had occurred in five couples; in three paternity was documented by genotyping. Thus, improved microsurgical and medical therapy might restore fertility." (PMID:6689737). Surgical results are generally worse than for other causes of obstruction. Hendry's series could support that claim but is not cached.

---

## 12. Treatment

| Treatment | NCIT ✓ | Modality | Evidence |
|---|---|---|---|
| Antibiotics for exacerbations | NCIT:C15620 Antibiotic Therapy ✓ | SMALL_MOLECULE | PMID:39119117 ("treated with intravenous antibiotics") |
| Airway clearance / chest physiotherapy | Look up (no cached row) | BEHAVIORAL | Extrapolated from bronchiectasis care |
| Endoscopic sinus surgery | NCIT:C157836 ✓ | SURGERY | Case-level only |
| Vasoepididymostomy (epididymovasostomy) | Look up; fallback NCIT:C15329 Surgical Procedure | SURGERY | PMID:39119117 ("advised vasoepididymostomy"); Hendry series |
| Sperm retrieval (TESE / MESA) | NCIT:C94427 Sperm Retrieval ✓ | SURGERY | PMID:38960684 |
| ICSI | NCIT:C185482 Intracytoplasmic Sperm Injection ✓ (or NCIT:C93282 ART ✓) | OTHER | PMID:38960684 ("successfully fathered a baby through intracytoplasmic sperm injection") |

There are no disease-specific trials and no pharmacogenomic or advanced therapies. NCT05631509 (genetic study of obstructive azoospermia, CFTR/ADGRG2/WES) is observational. It is not specific to Young syndrome, so it should not be added under `clinical_trials:`.

---

## 13. Prevention

- **Primary prevention (historical):** removing mercury from infant teething powders (UK, 1955). This is the best example of public-health prevention, if the mercury hypothesis holds.
- **Secondary prevention:** early recognition in men with bronchiectasis and infertility, and genetic testing for PCD and CF.
- **Tertiary prevention:** airway clearance, treating exacerbations, vaccination as for bronchiectasis (extrapolated).
- **Counselling:** offer genetic counselling once a PCD or CFTR genotype has been found. Otherwise the recurrence risk is unknown.

---

## 14. Other Species

There is no naturally occurring Young syndrome in animals (no OMIA entry found). Mercury reproductive toxicity in animals is a separate literature and should not be used as disease evidence.

## 15. Model Organisms

There are no Young syndrome-specific models. The relevant mechanistic models for Branch B are below.

| Model | Relationship | Fidelity | Caveat |
|---|---|---|---|
| miR-34b/c;miR-449 double-KO mouse (Yuan 2019, PMID:30659149 **[not cached]**) | PARTIALLY_RECAPITULATES the efferent-duct obstruction node | LOW–MODERATE | Global ciliogenesis loss, unlike the subtle C1d defect; also causes airway disease |
| GEMC1 / MCIDAS / CCNO mutant mice (Terré 2019, *Development*) | PARTIALLY_RECAPITULATES | LOW | Multiciliogenesis failure rather than a waveform defect |
| DNAH5-deficient mice ([PMC8269963](https://pmc.ncbi.nlm.nih.gov/articles/PMC8269963)) | PARTIALLY_RECAPITULATES | MODERATE | ODA loss; human DNAH5-PCD gives oligozoospermia, not strict azoospermia |
| *Schmidtea mediterranea* Smed-cfap221 RNAi (PMID:40250778) | PERTURBS ciliary motility | LOW | Locomotory cilia; no reproductive-tract readout |

These links would be `animal_models:` entries with `SPECIES_MISMATCH` / `BOUNDARY_OMISSION` divergences. A `HUMAN_MODEL_MISMATCH` discussion is also appropriate, because the efferent-duct cilia hypothesis has not been tested in human Young syndrome epididymal tissue.

---

## Gaps to record as `KNOWLEDGE_GAP` discussions

1. **Re-genotyping:** no historical or new Young syndrome cohort has been tested with a PCD panel that includes the C1d genes.
2. **Mercury mechanism:** there is no histology or toxicology linking calomel exposure to epididymal or airway secretion changes. The evidence is birth-cohort epidemiology and case reports only.
3. **Prevalence:** the "Klinefelter-comparable" estimate (1984) has never been revisited.
4. **Sinus phenotype:** poorly defined (PMID:19128521).
5. **Female phenotype:** unsupported beyond StatPearls.

---

## Sources

**Cached and quotable (in `references_cache/` on this branch):** PMID:6689737, 7307631, 1387740, 7551394, 9213847, 8922141, 19128521, 30969689 (StatPearls), 36196705, 38960684 (full text), 39362668 (full text), 39119117, 40250778, 40287162.

**Cached but with no content (cite the PMID only; no snippet possible):** PMID:8100886, 82711, 8664779, 9800754, 16817397.

**Not cached; fetch before use:**
- PMID:8292944 Hendry 1993
- PMID:30659149 Yuan 2019
- Terré 2019 (Development, dev162628)
- DNAH5 efferent-duct mouse study (PMC8269963)

**Web sources:**
- [MedGen 137934](https://https.ncbi.nlm.nih.gov/medgen/137934)
- [PubMed 8292944](https://pubmed.ncbi.nlm.nih.gov/8292944/)
- [PMC1697782 (Hendry 1993)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1697782/?page=3)
- [Wikipedia: Young's syndrome](https://en.wikipedia.org/wiki/Young%27s_syndrome)
- [PMC11308939](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11308939/)
- [PhenoDis](https://iegext02.helmholtz-munich.de/phenodis/disease/show/5207)
- [MalaCards CILD55](https://malacards.org/card/ciliary_dyskinesia_primary_55)
- [NORD](https://rarediseases.org/?p=262742)
- [SAIL concept library MONDO:0010220](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0010220/)
- [StatPearls](https://www.statpearls.com/articlelibrary/viewarticle/31456/)
- [Mayo Clinic: Friedman 1995](https://mayoclinic.elsevierpure.com/en/publications/screening-young-syndrome-patients-for-cftr-mutations)
- [NCT05631509](https://clinicaltrials.gov/study/NCT05631509)
- [AIIMS Rishikesh pulmogenetics, Feb 2025](https://aiimsrishikesh.edu.in/images/upload_documents/Rishi%20Vansh%20Volume%206%20Issue%202%20Feb%202025.pdf)
- [PMC6397526 (Yuan 2019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6397526)
- [PMC6397547](https://pmc.ncbi.nlm.nih.gov/articles/PMC6397547)
- [PMC8269963](https://pmc.ncbi.nlm.nih.gov/articles/PMC8269963)
- [Development dev162628](https://cob.silverchair.com/dev/article-pdf/146/8/dev162628/1859213/dev162628.pdf)
- [SATH library note on Brown 2025](https://www.library.sath.nhs.uk/research/2025/06/03/mercury-exposure-pink-disease-and-youngs-syndrome-a-forgotten-public-health-disaster-2025/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 10 |
| Quoted claims found in source | 10 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 24 |
| On topic | 15 |
| Off topic | 3 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:30659149` (3 mentions) - Motile cilia of the male reproductive system require miR-34/miR-449 for development and function to generate luminal turbulence.
  - shared terms: obstruction, genetic
- `PMC:PMC8269963` (8 mentions) - CEP164 is essential for efferent duct multiciliogenesis and male fertility.
  - shared terms: obstruction
- `PMC:PMC6397547` (3 mentions) - Motile cilia of the male reproductive system require miR-34/miR-449 for development and function to generate luminal turbulence.
  - shared terms: obstruction, genetic

Weighed against this report's own most characteristic terms: `syndrome`, `young`, `cached`, `mercury`, `azoospermia`, `bronchiectasis`, `pcd`, `normal`, `disease`, `obstructive`, `nasal`, `ciliary`, `cftr`, `epididymal`, `obstruction`, `chronic`, `airway`, `exposure`, `genetic`, `infection`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0010220` (5 mentions) - the report calls it "MONDO"; MONDO calls it **Young syndrome**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.