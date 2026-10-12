---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-12T14:10:22.879271'
end_time: '2026-10-12T14:12:12.499577'
duration_seconds: 109.62
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Guttmacher syndrome
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
  web_search_requests: 3
  num_turns: 13
  total_cost_usd: 0.8178919000000001
  session_id: c5bca049-79dd-565a-9d58-3e2354d3de80
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 4
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 4
  validator_version: 0.3.0
term_validation:
  total_terms: 11
  verified: 9
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 2
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: DOID:0111544
    reported_labels:
    - Disease Ontology
    ontology_label: Guttmacher syndrome
  labels_variant: 3
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Guttmacher syndrome
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Guttmacher syndrome** covering all of the
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

Try the Europe PMC API and the mirror.

# Research Report: Guttmacher Syndrome

**Evidence base.** The OMIM entry was read in full, apart from the last ~8 kB of that page. The PubMed pages would not load because of a cookie wall. For two papers I got only paraphrased abstracts from the Europe PMC API, so I have no verbatim abstract quotes. Every snippet destined for the KB must be fetched with `just fetch-reference PMID:…` and quoted from the cache. Items marked "not retrieved" below were not found.

## 1. Disease Information

**Overview.** Guttmacher syndrome is an extremely rare, dominantly inherited malformation syndrome of the distal limbs and the distal genitourinary tract. Orphanet's definition, reproduced by NORD, lists these features:
- hypoplastic thumbs and halluces
- 5th-finger clinobrachydactyly
- postaxial polydactyly of the hands
- short or uniphalangeal 2nd toes with absent nails
- hypospadias

Guttmacher described it in 1993 in one family (a father, a son and a daughter). He judged it distinct from hand-foot-genital syndrome (HFGS). He took postaxial polydactyly as the distinguishing feature (OMIM #176305, which cites Guttmacher 1993, PMID:8484413).

**Identifiers** (from the sources below; confirm each in a lookup step before binding).

| Source | Identifier |
|---|---|
| OMIM phenotype | #176305, "Preaxial deficiency, postaxial polydactyly, and hypospadias" (Guttmacher syndrome is an alternative title) |
| Orphanet | ORPHA:2957 |
| MONDO | MONDO:0008301 (reported by one search summary; verify) |
| Disease Ontology | DOID:0111544 |
| SNOMED CT | 722452004 |
| MedGen | 401304 |
| Gene | HOXA13 (OMIM 142959), 7p15.2; HGNC ID not retrieved. In the KB it is written lowercase as `hgnc:NNNN`, copied from a lookup. |

Do not confuse these with hand-foot-genital syndrome (HFGS, also called hand-foot-uterus syndrome), which is OMIM #140000 and ORPHA:2438. It is a separate entry.

**Synonyms.** Preaxial deficiency–postaxial polydactyly–hypospadias syndrome (GUTTS); Guttmacher syndrome.

**Level of data.** The data are aggregated, disease-level resources and one family-level report. No EHR-derived data were found.

**Curation implication.** Under the lump/split rules this is probably a `DISEASE` entry. It is a distinct OMIM and Orphanet entity with its own MONDO term. Overlap with HFGS must be recorded, and a note should say that HFGS has its own entry. The gene–disease link is provisional (see §4).

## 2. Etiology

- **Causal factor.** Genetic. Heterozygous HOXA13 missense variant, Q50L, found in the original family (Innis et al. 2002, PMID:11968094).
- **Genetic risk factors.** None beyond the HOXA13 variant. The reported allele also carried a 2-bp deletion in the HOXA13 promoter. It caused no detectable abnormality by itself but "may contribute" (OMIM, summarizing Innis 2002). Treat this as a possible cis-modifier, not an established one.
- **Environmental, protective and gene–environment factors.** Nothing found. Not applicable or not documented.

## 3. Phenotypes

All of this comes from one family (OMIM #176305, Guttmacher 1993). Frequencies cannot be given, so use qualitative terms only.

| Phenotype | HPO (OMIM synopsis; others need lookup) | Notes |
|---|---|---|
| Short thumbs (preaxial hypoplasia) | HP:0009778 | Thumb hypoplasia; "preaxial deficiencies" in all 3 affected |
| Postaxial polydactyly of hands | HP:0001162 | Distinguishing feature versus HFGS |
| 5th-finger brachydactyly/clinodactyly | HP:0001156 (mild brachydactyly of the 5th finger) | Orphanet: clinobrachydactyly |
| Glanular hypospadias | HP:0000807 | Father and son |
| Rudimentary or hypoplastic halluces | Lookup needed | |
| Uniphalangeal or short 2nd toes | Lookup needed | |
| Absent nails of halluces and 2nd toes | Lookup needed | |
| Limited interphalangeal joint motion | Lookup needed | |

- **Onset.** Congenital or neonatal (Orphanet).
- **Progression.** Static malformations (inference; not stated).
- **Severity.** Variable in the HOXA13 spectrum. One severe, de novo HOXA13 case with absent nails, absent halluces and genitourinary malformations was placed by the authors at the severe end of the HFGS/Guttmacher spectrum (Imagawa 2014, PMID:24934387).
- **Quality of life.** No data.
- **Uterine anomalies.** These belong to HFGS, not to the Guttmacher family as described. The one female case in that family was a daughter, and a uterine anomaly is not recorded for her. Do not add a uterine phenotype.

## 4. Genetic/Molecular Information

- **Gene.** HOXA13, a homeobox transcription factor. OMIM marks the gene–phenotype link as provisional ("?").
- **Variant.** c.1112A>T, p.Gln50Leu (homeodomain residue 50; OMIM allelic variant 142959.0005). It was found in the original family (Innis et al. 2002).
- **Mechanism.** The missense change alters a key residue in the recognition helix of the homeodomain. Innis et al. suggest this may affect DNA binding, with both loss and gain of function (my summary; verify against the full text).
- **Classification.** The OMIM source is a single family. Under ACMG, only the original report supports it, and ClinVar and ClinGen status was not retrieved. No ClinGen gene–disease validity record was checked. Do not fill `gene_disease_validity` unless a CGGV record turns up for this disease.
- **Origin.** Germline (familial).
- **Allele frequency, epigenetic and chromosomal data.** Not retrieved.
- **Related variants.** Other HOXA13 variants cause HFGS (OMIM #140000). Imagawa 2014 reports a de novo HOXA13 variant in a severe case. One search summary gave p.Ile368Phe for it (also written c.1102A>T), but that comes from a search summary only and must be checked against the paper.

## 5. Environmental Information

No environmental, lifestyle or infectious factors are documented. Not applicable.

## 6. Mechanism / Pathophysiology

**Causal chain** (the HOXA13 steps are inferred from the general HOXA13 literature and the Innis 2002 interpretation. The patient-level steps are observed in the family.)

1. A heterozygous HOXA13 missense variant (Q50L) changes the homeodomain recognition helix. *Demonstrated as a variant; its functional effect is inferred* (PMID:11968094).
2. This is predicted to alter DNA binding by the HOXA13 transcription factor, with possible loss and gain of function. *Inferred.* A promoter 2-bp deletion on the same allele may modulate expression. *Hypothesised.*
3. Abnormal HOXA13-dependent patterning of the distal limb bud (autopod) follows. *Inferred from the HOXA13 literature; not curated from a source in this session.*
4. The patterning defect produces preaxial hypoplasia of thumbs and halluces, 5th-finger shortening, postaxial polydactyly, and hypoplastic nails and phalanges. *Observed in the family; the link from step 3 is inferred.*
5. A parallel defect in genital tubercle development produces hypospadias. *Observed in males; mechanism inferred.*

**Suggested ontology terms.** Verify each by lookup before binding.
- GO: pattern specification process; embryonic limb morphogenesis; DNA-binding transcription factor activity.
- Cell types: limb bud mesenchymal cells and distal limb progenitors (CL term to look up).
- Anatomy: autopod, hand, foot, nail, penis/urethra (UBERON IDs to look up).

Molecular profiling, single-cell and multi-omics data for this disease were not found.

## 7. Anatomical Structures Affected

- Primary: hands (thumb, 5th finger, ulnar side), feet (hallux, 2nd toe), nails, and the distal male urethra (glanular hypospadias).
- Pattern: bilateral involvement is not stated in the sources I read, so lateralization is unknown.
- Subcellular site: nucleus (the HOXA13 transcription factor).

## 8. Temporal Development

- Congenital, with neonatal recognition (Orphanet).
- Static course; there is no source for progression.
- No stages, remission, or critical periods are documented, apart from embryonic limb and genital development (inference).

## 9. Inheritance and Population

- **Inheritance.** Autosomal dominant (HP:0000006). In the family, a father transmitted it to a son and a daughter, consistent with dominant inheritance.
- **Penetrance and expressivity.** Not formally assessed. Only one family has been described.
- **Prevalence.** Orphanet gives no prevalence data. One aggregator mentions an estimate of about 1,000 US cases. I could not verify it and do not recommend using it. The class is probably `NOT_YET_DOCUMENTED`, or `CASES_IN_LITERATURE` with `measure_type` set accordingly.
- **Founder effect, consanguinity, carrier frequency, ancestry, sex ratio.** Not documented.

## 10. Diagnostics

- **Clinical.** Examination of the hands, feet and genitalia, plus limb radiographs. No criteria were retrieved.
- **Differential.** HFGS (OMIM #140000): no postaxial polydactyly, and uterine anomalies in women. Also consider other HOXA13-related phenotypes and other syndromic limb malformations (not reviewed).
- **Genetic testing.** Single-gene HOXA13 sequencing or a limb-malformation gene panel (no panel contents retrieved). HOXA13 contains a polyalanine tract, so check how the laboratory handles repeat-region variants and deletions. This is general knowledge, not from a retrieved source.
- **Biomarkers and screening.** None known.

## 11. Outcome/Prognosis

No survival, life expectancy or quality-of-life data were found. Morbidity is presumably functional (hand and foot use, hypospadias repair), which is an inference. Not documented.

## 12. Treatment

No disease-specific literature was found. Management is supportive and surgical, which is an inference rather than a sourced claim:
- Hypospadias repair: NCIT surgical procedure terms (verify the CURIE by lookup).
- Hand and foot reconstructive or orthopaedic surgery (NCIT:C16186 Orthopedic Surgical Procedure appears in the repository guidance).
- Genetic counseling (NCIT:C15240).

There is no pharmacotherapy, gene therapy or clinical trial. I did not search ClinicalTrials.gov.

## 13. Prevention

- Genetic counseling for autosomal dominant recurrence (50% risk for offspring of an affected parent, from the standard dominant model).
- Prenatal or preimplantation testing is possible in a family with a known variant (general principle).
- No other prevention data.

## 14. Other Species / Natural Disease

No natural disease is documented in the sources read. OMIA was not searched. The OMIM page links to Alliance Genome and MGI resources but gives no animal model description.

## 15. Model Organisms

- I did not retrieve any Guttmacher-specific model.
- General knowledge, unsourced here: mouse *Hoxa13* mutants show distal limb and genital phenotypes, and Mortlock and colleagues linked HOXA13 mutation to the hand-foot-genital phenotype (Mortlock 1996, cited in one search result as the HFGS origin; the PMID was not retrieved). Verify through MGI before adding any `animal_models` entry.
- No Q50L knock-in model was found.

## Key References

1. Guttmacher AE et al. 1993. Am J Med Genet 46:219-222. **PMID:8484413**. Original family description, cited by OMIM.
2. Innis JW, Goodman FR, Bacchelli C, Williams TM, Mortlock DP, Sateesh P, Scambler PJ, McKinnon W, Guttmacher AE. Hum Mutat 2002;19(5):573-574. **PMID:11968094**. Title as returned: a HOXA13 allele with a missense mutation in the homeobox and a dinucleotide deletion in the promoter underlies Guttmacher syndrome. Q50L; re-examination of the original family.
3. Imagawa E, Kayserili H, Nishimura G, Nakashima M, Tsurusaki Y, Saitsu H, Ikegawa S, Matsumoto N, Miyake N. Am J Med Genet A 2014;164A(9):2398-2402. **PMID:24934387**. Severe HFGS manifestations with a novel de novo HOXA13 variant. Its authors mention Guttmacher syndrome as part of the spectrum.
4. OMIM #176305 (the page text was read; its last ~8 kB was not): https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/176305
5. OMIM #140000, hand-foot-genital syndrome: https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/a3492137cada35c1427e5783c176e4344e6cbb56/www.ncbi.nlm.nih.gov/omim/140000
6. Orphanet/NORD summary: https://rarediseases.org/mondo-disease/guttmacher-syndrome/
7. MalaCards, Preaxial deficiency, postaxial polydactyly, and hypospadias: https://www.malacards.org/card/preaxial_deficiency_postaxial_polydactyly_and_hypospadias_2

A search also turned up PMID:36734258, a case with a HOXA9/HOXA13 deletion whose background reviews Guttmacher syndrome. I did not read it, so use it only as a lead.

## Gaps and Cautions for Curation

- **Single family.** The whole phenotype list rests on one family, and the gene–disease link is provisional in OMIM. Say so in `notes`. Do not assign a validity tier that no external body has given.
- **Quotes.** I have no verbatim snippets. Fetch the cache entries and quote from them.
- **IDs.** HGNC, UBERON, CL and GO identifiers and the remaining HPO terms have not been looked up. Do not bind any from this report without a lookup.
- **HFGS overlap.** Orphanet and OMIM keep Guttmacher syndrome and HFGS separate, while the literature treats them as one spectrum (PMID:24934387). Record this overlap in the entry.
- **Possible merge.** If MONDO later merges the two, the entry would be affected. A `mondo_replaced_by` check is cheap.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 11 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 6 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0111544` (1 mention) - the report calls it "Disease Ontology"; DOID calls it **Guttmacher syndrome**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0009778` (1 mention) - the report calls it "Short thumbs (preaxial hypoplasia)"; HP calls it **Short thumb**, and lists "Thumb hypoplasia" among its other names
- `HP:0001162` (1 mention) - the report calls it "Postaxial polydactyly of hands"; HP calls it **Postaxial hand polydactyly**, and lists "Postaxial polydactyly of hand" among its other names
- `HP:0001156` (1 mention) - the report calls it "mild brachydactyly of the 5th finger"; HP calls it **Brachydactyly**, and lists "Brachydactyly syndrome" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.