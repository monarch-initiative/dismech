---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-25T04:34:36.711770'
end_time: '2026-08-25T04:39:05.902985'
duration_seconds: 269.19
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Complex Regional Pain Syndrome Type 1
  mondo_id: ''
  category: Neurologic
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
  web_search_requests: 19
  num_turns: 21
  total_cost_usd: 1.3587861999999997
  session_id: 21924873-a28a-5e64-81d5-a552bf3cfbda
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 42
reference_validation:
  total_references: 31
  verified: 31
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 31
  on_topic: 19
  off_topic: 2
  off_topic_references:
  - PMC:PMC5928634
  - PMC:PMC8750957
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Complex Regional Pain Syndrome Type 1
- **MONDO ID:**  (if available)
- **Category:** Neurologic

## Research Objectives

Please provide a comprehensive research report on **Complex Regional Pain Syndrome Type 1** covering all of the
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

I'll research CRPS-I across the major topic areas using parallel searches, then synthesize into a full report.

# Complex Regional Pain Syndrome Type I (CRPS-I): Comprehensive Research Report

## 1. Disease Information

**Overview.** Complex Regional Pain Syndrome (CRPS) is a chronic neuropathic pain disorder characterized by continuous, disproportionate regional pain (usually affecting a limb) accompanied by sensory, vasomotor, sudomotor/edema, and motor/trophic abnormalities that are not explained by any other diagnosis. CRPS **Type I** (formerly "reflex sympathetic dystrophy," RSD) occurs **without evidence of a definable major nerve lesion**, whereas CRPS **Type II** (formerly "causalgia") follows a confirmed peripheral nerve injury. The pain is classically triggered by a relatively minor inciting event (fracture, sprain, surgery, immobilization) but grows out of proportion to, and outlasts, that event ([PMC12428113](https://pmc.ncbi.nlm.nih.gov/articles/PMC12428113/); [PMC11756781](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11756781/)).

**Key identifiers:**
- **Orphanet:** ORPHA:83452 ([orpha.net](https://www.orpha.net/en/disease/detail/83452))
- **OMIM:** 604335 (susceptibility locus discussion)
- **ICD-11:** MG30.04 ("Complex regional pain syndrome," under chronic secondary musculoskeletal pain)
- **ICD-10-CM:** G90.5x (complex regional pain syndrome I, by limb)
- **MeSH:** Reflex Sympathetic Dystrophy (D012172); "Complex Regional Pain Syndromes" (D020918)
- MONDO's disease page for "complex regional pain syndrome type 1" is indexed via NORD/MONDO ([rarediseases.org/mondo-disease](https://rarediseases.org/mondo-disease/complex-regional-pain-syndrome-type-1/)); exact MONDO CURIE should be confirmed against the local MONDO release rather than assumed from this search.

**Synonyms:** Reflex sympathetic dystrophy (RSD), Sudeck's atrophy, algodystrophy, causalgia (historically CRPS-II), shoulder-hand syndrome, post-traumatic dystrophy, sympathetically maintained pain (an overlapping but distinct mechanistic concept, since not all CRPS pain is sympathetically maintained).

**Evidence base composition:** CRPS knowledge derives from a mix of (a) individual case series/cohorts and single-center registries, (b) population-based epidemiologic studies (Olmsted County, Netherlands, South Korea nationwide claims data), (c) mechanistic human physiology/imaging studies, and (d) rodent model studies (tibia-fracture and chronic post-ischemia pain models) — the pathophysiology narrative is therefore a blend of human clinical/EHR-derived observation and model-organism mechanistic inference, which should be kept distinct in evidence tagging.

---

## 2. Etiology

### Disease Causal Factors
CRPS-I has no single cause; it is a multifactorial syndrome triggered by tissue trauma (most commonly a **distal extremity fracture**, but also sprains, surgery, casting/immobilization, or even trivial injury) in a susceptible individual, followed by an exaggerated and self-sustaining local and systemic inflammatory/neuro-immune response ([PMC10993759](https://pmc.ncbi.nlm.nih.gov/articles/PMC10993759/)). CRPS "stems from a complex interplay of inflammatory, immunologic, neurogenic, genetic, and psychologic factors" (PMID: 38828388).

### Risk Factors — Genetic
- **HLA associations:** HLA-DQ8 has been replicated as conferring genetic risk for CRPS, including CRPS with dystonia; additional MHC associations reported include HLA-DR6, HLA-DR13, HLA-DR2, HLA-DQ1, and HLA-B62 ([jpain.org](https://www.jpain.org/article/S1526-5900(12)00655-4/fulltext)).
- **Candidate gene polymorphisms:** A single-nucleotide polymorphism across four genes — **ANO10, P2RX7, PRKAG1, SLC12A9** — has been associated with CRPS-I development, notably expressed as rare alleles more often in males (PMID: 38828388).
- **Familial CRPS:** Familial clustering exists without a clear Mendelian inheritance pattern; siblings of sporadic CRPS patients do not show a large excess risk, but in families with ≥2 affected members, onset is earlier and multi-limb/dystonic presentations are more common (ResearchGate summary of genetic/epidemiological studies).
- Genome-profiling work has flagged upregulated genes including HLA-A29.1, MMP9, alanyl aminopeptidase, histidine decarboxylase, G-CSF3-R, and STAT-3 in affected tissue (PMID: 38828388).

### Risk Factors — Environmental/Clinical
- **Fracture** is the most common inciting event, accounting for ~42% of CRPS cases; **distal radius fracture** is a classic trigger.
- Documented risk factors after distal radius fracture/surgery include **rheumatoid arthritis, female sex, concomitant ulnar fracture, open reduction, and open fracture** ([Sci Rep 2019](https://www.nature.com/articles/s41598-019-41152-x)).
- **Motor nerve injury** and **female sex** are independent risk factors after traumatic extremity injury (PMID: 20517769).
- Immobilization/casting, surgery, crush injury, and polytrauma are recognized triggers ([Sci Rep](https://www.nature.com/articles/s41598-019-41152-x)).
- Non-genetic host factors: age (peak incidence 50s–70s), postmenopausal status in women, and possibly psychological state at time of injury.

### Protective Factors
- **Vitamin C supplementation** after wrist fracture is the best-studied protective/preventive intervention (see Section 13).
- No specific genetic protective alleles for CRPS have been well characterized in the literature surveyed; gnomAD-level protective-variant data for CRPS specifically is not established.

### Gene-Environment Interactions
The prevailing model is that a genetically/immunologically primed individual (e.g., HLA-DQ8 carriers, certain cytokine gene variants) mounts an exaggerated neuro-immune and inflammatory response to a peripheral tissue injury, with sex (estrogen/postmenopausal status), age, and psychological state modulating the magnitude and chronicity of that response — i.e., trauma is necessary but not sufficient; host susceptibility factors determine who develops chronic CRPS versus normal post-traumatic recovery (PMID: 38828388; PMC10993759).

---

## 3. Phenotypes

CRPS-I phenotypes cluster into four Budapest-criteria domains — **sensory, vasomotor, sudomotor/edema, and motor/trophic** — plus documented CNS/cognitive and psychological phenotypes. Two large data-driven phenotype clusters have been described: a **"central" cluster** (minor inciting injury, motor signs, allodynia, glove/stocking sensory deficit) and a **"peripheral" cluster** (edema, skin-color change, temperature asymmetry, sweating, trophic change) ([Neurology 2020](https://www.neurology.org/doi/10.1212/WNL.0000000000008736)).

| Phenotype | Domain | Suggested HPO term |
|---|---|---|
| Allodynia (pain to normally non-painful stimuli) | Sensory | HP:0034381 Allodynia (or general neuropathic pain term) |
| Hyperalgesia | Sensory | HP:0033391 Hyperalgesia (verify local HPO release) |
| Chronic/persistent regional pain disproportionate to injury | Sensory | HP:0012532 Chronic pain |
| Skin temperature asymmetry (warm or cold phase) | Vasomotor | HP:0025195 Abnormal thermoregulation / HP:0007512 Vasomotor instability (verify) |
| Skin color change (mottled, red, or cyanotic) | Vasomotor | HP:0011820 Abnormal skin color / HP:0100543 Cognitive impairment n/a — use skin discoloration terms |
| Edema of affected limb | Sudomotor/edema | HP:0000969 Edema |
| Sweating abnormality (hyperhidrosis or anhidrosis) | Sudomotor | HP:0000975 Hyperhidrosis / HP:0000970 Anhidrosis |
| Decreased range of motion / weakness | Motor | HP:0001376 Limitation of joint mobility |
| Tremor | Motor | HP:0001337 Tremor |
| Dystonia | Motor | HP:0001332 Dystonia |
| Trophic changes: shiny/atrophic skin, abnormal hair/nail growth | Trophic | HP:0000963 Thin skin; HP:0100836 (nail dystrophy variants) |
| Bone demineralization / patchy osteoporosis | Trophic | HP:0000939 Osteoporosis |
| Impaired tactile acuity / two-point discrimination | Sensory/cortical | HP:0025145 (verify local terms) |

**Onset and course:** Onset typically follows the trigger by days to weeks; historically staged into acute ("warm"), dystrophic, and atrophic ("cold") phases, though the strict three-stage model is increasingly questioned — a 2025 paper explicitly asks whether the "warm phase" concept needs reassessment relative to the Budapest criteria ([PMC12468258](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12468258/)). Course is variable: some patients remit spontaneously or with treatment; others become chronic and treatment-refractory, occasionally spreading to other limbs.

**Frequency/severity:** Budapest clinical criteria require ≥1 symptom in 3/4 categories and ≥1 sign in 2/4 categories on exam, reflecting that no single phenotype is present in 100% of patients; sensory (pain/allodynia) is near-universal, while individual trophic or motor signs vary widely in frequency across cohorts.

**Quality of life impact:** Long-term CRPS is associated with substantial disability, sleep disturbance, and reduced quality of life; a cross-sectional study of long-term CRPS patients documented ongoing physical symptoms, disability, and impaired psychological health years after onset ([PMC11419548](https://pmc.ncbi.nlm.nih.gov/articles/PMC11419548/)).

---

## 4. Genetic/Molecular Information

CRPS-I is **not a monogenic Mendelian disorder**; there is no single causal gene comparable to a classic OMIM disease gene. Instead:

- **Susceptibility loci:** HLA-DQ8 (replicated), plus HLA-DR6, -DR13, -DR2, -DQ1, -B62 (less consistently replicated) ([jpain.org](https://www.jpain.org/article/S1526-5900(12)00655-4/fulltext)).
- **Candidate SNPs:** ANO10 (anoctamin-10, calcium-activated chloride channel), P2RX7 (purinergic receptor, implicated broadly in neuroinflammatory/microglial signaling), PRKAG1 (AMPK gamma subunit, metabolic sensing), SLC12A9 (cation-chloride cotransporter) — associated with CRPS-I, more often in males as rare alleles (PMID: 38828388).
- **Variant classification:** These are *susceptibility/risk* variants under population-genetics frameworks (odds-ratio associations), not ACMG pathogenic/likely-pathogenic single-gene variants; ClinVar does not carry CRPS as a Mendelian indication.
- **Somatic vs. germline:** All reported associations are germline population-genetic associations; no somatic mutation model applies.
- **Functional consequence framing:** Rather than loss/gain-of-function at a single locus, the molecular model is **immune/neuro-inflammatory dysregulation** — e.g., autoantibody production against autonomic receptors, and altered microglial/astrocyte reactivity (see Section 6).
- **Epigenetics:** Not deeply characterized in the retrieved literature for CRPS specifically; broader chronic-pain literature implicates DNA methylation changes at inflammatory and opioid-receptor loci, but CRPS-specific methylome studies were not surfaced in this search and should be treated as a knowledge gap rather than asserted.
- **Chromosomal abnormalities:** None reported; CRPS is not associated with aneuploidy or structural chromosomal rearrangement.

---

## 5. Environmental Information

- **Physical trauma** is the dominant environmental/mechanistic trigger: fractures (especially distal radius), sprains, contusions, surgical procedures (including carpal tunnel release, and other elective hand/foot surgery), and prolonged immobilization/casting.
- **Iatrogenic factors:** Tight casting, prolonged immobilization, and possibly surgical technique (open vs. closed reduction) modulate risk after fracture ([Sci Rep 2019](https://www.nature.com/articles/s41598-019-41152-x)).
- **Lifestyle/host factors:** Smoking and psychological stress at time of injury are frequently cited in the broader clinical literature as modulators of pain chronification, though CRPS-specific quantitative data were not retrieved in this pass.
- **Infectious agents:** No established infectious trigger; CRPS is not classified as an infectious or post-infectious syndrome in the literature surveyed.
- **ECTO-style exposure framing:** the principal "exposure" relevant to dismech-style environmental modeling is mechanical/traumatic tissue injury (fracture, surgery) rather than a chemical/toxin exposure — this differs structurally from toxin-driven disorders and should be modeled as a triggering physical trauma event rather than a chemical ECTO term.

---

## 6. Mechanism / Pathophysiology

CRPS-I pathophysiology is best understood as a **causal chain**: peripheral tissue/nerve injury → exaggerated local neurogenic inflammation and immune activation → peripheral sensitization → central sensitization and glial activation in spinal cord and brain → maladaptive cortical reorganization → sustained pain, autonomic dysregulation, and motor abnormality, with autoimmune antibody production acting as an amplifying/maintaining loop (PMID: 38828388; PMC10993759; PMID: 37701560).

### 6a. Peripheral mechanisms — Neurogenic inflammation
- Nociceptor C-fibers, once activated by mechanical/chemical injury, release **substance P, CGRP (calcitonin gene-related peptide), and bradykinin**, which cause **vasodilation, plasma extravasation, edema, erythema, increased sweating**, and recruit/activate local immune cells — the biological basis for the vasomotor/sudomotor/edema domain of the Budapest criteria (PMID: 38828388; PMID: 37701560).
- CRPS patients show **elevated circulating CGRP and substance P** relative to controls, and elevated pro-inflammatory cytokines (TNF-α, IL-1β, IL-6) locally and systemically, consistent with a neuro-immune amplification loop.
- GO terms: `GO:0002544` chronic inflammatory response; `GO:0007204` positive regulation of cytosolic calcium ion concentration; `GO:0006954` inflammatory response; neuropeptide signaling via CGRP/substance P receptors.

### 6b. Autoimmune component
- **~70% of CRPS patients carry IgG autoantibodies** against surface antigens on autonomic neurons, functionally active against the **β2-adrenergic receptor** and the **muscarinic-2 (M2) acetylcholine receptor**; activating antibodies against the **α1a-adrenoceptor** have also been reported ([PMC4337272](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4337272/); PMID: 38828388).
- **Passive transfer experiments** (mouse model): injecting IgG from severe/persistent human CRPS patients into hind-paw-injured mice reproduces key clinical features and **profound microglial and astrocyte activation** in pain-related brain regions and spinal dorsal horn — direct mechanistic (model-organism) evidence that autoantibodies are pathogenic, not merely epiphenomenal ([PNAS](https://www.pnas.org/doi/10.1073/pnas.1820168116); PMID: 31182576).
- This CRPS-IgG-induced phenotype is **mediated in part by microglia-derived IL-1β**, and **IL-1 blockade both prevents and reverses** the transferred phenotype in mice — flagging IL-1 pathway antagonism as a candidate therapeutic mechanism (PMID: 31182576).
- **B-cell/IgM contribution:** In the tibia-fracture mouse model, mice lacking B cells/IgM show attenuated nociceptive/inflammatory changes at 3 weeks post-fracture, and transfer of IgM from acutely fractured mice induces pronociceptive effects — implicating an early IgM-driven autoimmune contribution distinct from the later IgG-driven phase (PMID: 38828388).

### 6c. Central sensitization and glial activation
- Central sensitization arises via **NMDA receptor** activation, **microglia and astrocyte activation**, **pro-inflammatory cytokine release**, and leukocyte trafficking in the dorsal horn and supraspinal pain-processing regions (PMID: 38828388).
- Sustained glutamate/substance-P release at the spinal level lowers the threshold for response to mechanical stimuli — the proposed mechanistic basis of mechanical allodynia (PMID: 38828388).
- GO terms: `GO:0038096` Fc-receptor signaling pathway (relevant to IgG-mediated microglial activation); `GO:0034976` response to endoplasmic reticulum stress (general neuroinflammation context); `GO:0002526` acute inflammatory response.
- Cell Ontology terms: `CL:0000129` microglial cell, `CL:0000127` astrocyte, `CL:0000540` neuron.

### 6d. Sympathetic nervous system dysregulation
- Early CRPS: **decreased circulating norepinephrine** with **compensatory upregulation of peripheral adrenergic receptors** (explaining early "warm," vasodilated phase).
- Later CRPS: **excessive vasoconstriction**, producing the classic cold, cyanotic, "blue" extremity (PMID: 38828388).
- Elevated sympathetic activity has been estimated to amplify spontaneous pain (cited figure: "by 22%" in one synthesis; treat as an approximate, review-level estimate rather than a precisely reproducible statistic) (PMID: 38828388).
- Not all CRPS pain is "sympathetically maintained" — a subset is sympathetically independent, which is part of why sympathetic blocks show inconsistent efficacy (see Section 12).

### 6e. Cortical/CNS reorganization
- **Somatosensory cortex (S1):** the cortical representation of the affected limb is reduced in size and spatially distorted relative to the unaffected side; this reorganization **reverses with successful treatment**, arguing for a causal (not merely correlative) relationship to symptom severity (PMC11140106 fetch, PMID: 38828388).
- **Motor cortex (M1):** reduced intracortical inhibition contralateral to (or bilateral to) the affected limb, correlating with impaired fine motor control (decreased pinch-grip performance, two-point discrimination) — a maladaptive plasticity signature (doi:10.3233/RNN-180886).
- **Structural imaging:** decreased gray matter volume in dorsal insula, left orbitofrontal cortex, and cingulate cortex; increased gray matter volume in bilateral dorsal putamen and right hypothalamus (PMID: 38828388).
- **Functional connectivity:** somatotopic disruption of primary sensorimotor cortex functional connectivity has been demonstrated with fMRI, plausibly underlying spontaneous pain and motor symptoms ([onlinelibrary.wiley.com/hbm.26513](https://onlinelibrary.wiley.com/doi/full/10.1002/hbm.26513)).
- Motor abnormalities (dystonia, tremor, weakness, reduced range of motion) are attributed to aberrant involvement of primary motor cortex, supplementary motor area, posterior parietal cortex, and basal ganglia circuits (PMID: 38828388).
- Notably, one controlled MR spectroscopy study found **no significant alteration in sensorimotor cortex GABA or glutamate concentrations** in CRPS, indicating that not every proposed cortical mechanism is uniformly supported and that metabolite-level changes are not yet an established biomarker ([PMC7029188](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7029188/)).

### 6f. Bone pathology
- CRPS-associated regional osteoporosis/patchy bone demineralization is mechanistically consistent with the general inflammatory-bone-loss paradigm: **TNF-α, IL-1, and IL-6** cooperate with **RANKL** to enhance **osteoclastogenesis** via **NF-κB** (TNF-α) and **JAK-STAT** (IL-6) signaling, providing a plausible mechanistic bridge between the neuro-inflammatory milieu of CRPS and the periarticular bone loss seen on imaging (general inflammatory bone-loss literature — PMC5928634, PMC8750957 — applied to CRPS by extrapolation, not CRPS-specific primary data in this search pass).
- This periarticular osteopenia is the structural correlate of the characteristic **three-phase bone scintigraphy** pattern (see Section 10).

### 6g. Oxidative stress
- The rodent **chronic post-ischemia pain (CPIP)** model — tourniquet-induced hindlimb ischemia-reperfusion — produces allodynia, edema, hyperemia, and demonstrable **oxidative stress**, supporting a role for reactive oxygen species in early CRPS-like pathology, particularly relevant to warm/vasodilated phase mechanisms (JoVE 60562; ResearchGate CPIP description).

### Causal chain summary (upstream → downstream)
1. Peripheral tissue/nerve trauma (initiating event)
2. Nociceptor activation → neuropeptide release (substance P, CGRP) → neurogenic inflammation, local immune cell recruitment
3. Autoantibody generation (IgM early, IgG later) against β2-AR/M2-receptor/α1a-adrenoceptor on autonomic neurons
4. Autoantibody/cytokine (IL-1β)-driven microglial and astrocyte activation in spinal cord dorsal horn
5. Central sensitization (NMDA-receptor dependent) → mechanical allodynia/hyperalgesia
6. Supraspinal maladaptive plasticity: S1 cortical reorganization, M1 disinhibition, limbic/insular structural change
7. Clinical CRPS phenotype: chronic disproportionate pain, sensory/vasomotor/sudomotor/motor/trophic signs, periarticular bone loss

---

## 7. Anatomical Structures Affected

- **Organ/system level:** Primary — peripheral nervous system (sensory/autonomic nerve fibers) and the affected limb (usually distal extremity: hand/wrist or foot/ankle). Secondary/systemic — central nervous system (spinal dorsal horn, brain), musculoskeletal system (periarticular bone), integumentary system (skin, nails, hair), and vascular system (microvasculature, sympathetic vasomotor control).
- **UBERON candidates:** `UBERON:0002398` manus (hand), `UBERON:0002387` pes (foot), `UBERON:0001466` limb, `UBERON:0002037` cerebellum (n/a — use `UBERON:0002616` gray matter / `UBERON:0006459` primary somatosensory cortex, `UBERON:0001384` motor cortex), `UBERON:0002771` skin of hand.
- **Tissue/cell level:** Cutaneous small-fiber nociceptors (C and Aδ fibers), sympathetic postganglionic autonomic neurons, dermal/epidermal skin cells, osteoclasts/osteoblasts in periarticular bone, microglia and astrocytes in spinal dorsal horn and brain.
- **Cell Ontology terms:** `CL:0000850` C fiber neuron / `CL:0011012` neuron associated with sensory ganglion, `CL:0000636` sympathetic neuron, `CL:0000092` osteoclast, `CL:0000062` osteoblast, `CL:0000129` microglial cell, `CL:0000127` astrocyte.
- **Subcellular:** Cell-surface adrenergic and muscarinic receptors (targets of autoantibodies), NMDA receptor complexes at central synapses (`GO:0043195` terminal bouton; `GO:0045202` synapse).
- **Localization:** Distal extremity, typically unilateral, though multi-limb spread can occur in a subset of (especially familial) cases; no consistent laterality preference documented in the retrieved literature.

---

## 8. Temporal Development

- **Onset:** Days to weeks after inciting trauma; onset pattern is typically subacute, occasionally acute.
- **Historical staging (contested):** Classic three-stage model — acute/"warm"/inflammatory stage, dystrophic stage, atrophic/"cold" stage — is widely taught but increasingly questioned as an oversimplification; a 2025 review explicitly interrogates whether the warm phase concept needs revision relative to Budapest criteria performance ([PMC12468258](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12468258/)).
- **Progression:** Variable — some patients improve/resolve within months (especially with early treatment), others progress to chronic, treatment-resistant disease lasting years; a minority develop multi-limb spread.
- **Course pattern:** Can be self-limited, chronic-stable, chronic-progressive, or relapsing (particularly documented in pediatric cohorts, where relapse is associated with greater baseline mental-health difficulty).
- **Critical window for intervention:** Early diagnosis (ideally <3 months from onset) and early mobilization/functional restoration are repeatedly cited as key modifiers of long-term outcome, especially in pediatric CRPS.

---

## 9. Inheritance and Population

### Epidemiology
- Overall CRPS incidence estimates vary by study; one synthesis cites **26.2 per 100,000 person-years** overall, while the population-based Olmsted County study found **~5.5/100,000 person-years for CRPS-I** and **~0.8/100,000 for CRPS-II**, with point prevalence of **~21/100,000 (Type I)** and **~4/100,000 (Type II)** ([Mayo Clinic/Olmsted study](https://mayoclinic.elsevierpure.com/en/publications/complex-regional-pain-syndrome-type-i-incidence-and-prevalence-in/); PMID: 12749974).
- A South Korea nationwide claims-based study provides more recent (population-scale EHR-derived) epidemiologic characteristics ([Sci Rep](https://www.nature.com/articles/s41598-026-45686-9)).

### Sex ratio
- Consistent **female predominance**, historically cited as ~3:1 to 4:1, more precisely reported at **~1.5:1 for Type I** vs. **~1.1:1 for Type II** in recent data (overall female share ~57.5%).

### Age distribution
- Mean age at diagnosis **40–50 years**; incidence peaks around **61–70 years**; rare in children/adolescents; **postmenopausal women** appear to carry the highest risk.

### Inheritance pattern
- CRPS is **not a classically Mendelian-inherited disorder**. It shows **polygenic/multifactorial susceptibility** (HLA and candidate-gene associations) rather than a single high-penetrance causal gene. Familial clustering exists in a minority of cases without a defined inheritance mode; use `HP:0010982` Polygenic inheritance or `HP:0001426` Multifactorial inheritance framing rather than AD/AR/X-linked, with the caveat that formal segregation/penetrance data are limited.
- **Founder effects / consanguinity:** Not established in the literature surveyed.
- **Carrier frequency:** Not applicable in the traditional Mendelian sense (susceptibility alleles like HLA-DQ8 are common in the general population and are risk-modifying, not disease-defining).

### Geographic/ancestral distribution
- No strong evidence of geographic clustering was retrieved in this search; population-based data exist from the US (Olmsted County, Minnesota), the Netherlands, and South Korea, suggesting broad but not systematically globally mapped epidemiology.

---

## 10. Diagnostics

### Clinical criteria — Budapest Criteria (IASP-adopted)
The dominant, most widely used diagnostic framework requires ([PMC12428113](https://pmc.ncbi.nlm.nih.gov/articles/PMC12428113/); PMID: 20493633):
1. Continuing pain disproportionate to any inciting event.
2. At least **1 reported symptom in 3 of 4 categories** (sensory, vasomotor, sudomotor/edema, motor/trophic) **and** at least **1 observed sign in 2 of 4 categories** on exam.
3. No other diagnosis better explains the presentation.

The **clinical (looser)** Budapest criteria have sensitivity **0.99** and specificity **0.68**; the **research (stricter)** criteria trade some sensitivity for markedly improved specificity relative to the older 1994 IASP criteria (PMC12428113).

### Imaging — Three-phase bone scintigraphy (TPBS)
- Classic finding: **increased blood flow (phase 1), increased blood pool activity (phase 2), and intense periarticular delayed uptake (phase 3)** in small joints of the affected region, with **periarticular accentuation on the delayed/osseous phase** considered characteristic ([tech.snmjournals.org](https://tech.snmjournals.org/content/45/3/243)).
- With optimized/modified image-interpretation criteria, TPBS sensitivity/specificity for CRPS-I have been reported around **80%/72%** (PMID: 24900016).
- Combining TPBS with **QSART (quantitative sudomotor axon reflex test)** and **infrared thermography** improves overall diagnostic confidence, though no single modality is individually definitive ([JPR](https://www.tandfonline.com/doi/full/10.2147/JPR.S474451)).

### Quantitative sensory testing (QST)
- Standardized QST batteries assess vibration and thermal (warm/cold) perception thresholds, mechanical/thermal allodynia, and mechanical hyperalgesia — used to objectively document the sensory domain and to research-stratify "central" vs. "peripheral" phenotype clusters.

### Laboratory
- No specific diagnostic biomarker/lab test exists; routine labs are used mainly to exclude alternative diagnoses (infection, inflammatory arthropathy, DVT). Research-level markers (autoantibodies to β2-AR/M2 receptor, elevated CGRP/substance P, inflammatory cytokines) are **not** yet validated clinical diagnostics.

### Genetic testing
- Not part of routine clinical diagnosis; HLA typing and candidate SNP panels (ANO10, P2RX7, PRKAG1, SLC12A9) remain research tools without established clinical utility or a Genetic Testing Registry (GTR) entry identified in this search.

### Electrophysiology
- Nerve conduction studies/EMG are used primarily to **exclude CRPS-II** (i.e., to confirm the absence of a major identifiable nerve lesion) and to rule out competing peripheral neuropathies.

### Differential diagnosis
Key conditions to exclude: deep vein thrombosis, cellulitis/infection, peripheral neuropathy, vasculitis, unrecognized fracture/nerve injury (which would reclassify as CRPS-II), inflammatory arthritis, and factitious/malingering presentations.

### Screening
No population-level screening program exists; "screening" in practice equates to a **high index of suspicion** after fracture/surgery, particularly in patients with recognized risk factors (female sex, RA, open fracture/reduction), given evidence that early recognition materially improves outcome.

---

## 11. Outcome/Prognosis

- **Mortality:** CRPS-I is not directly life-threatening; no disease-specific mortality data were retrieved, consistent with it being a morbidity- rather than mortality-driving condition.
- **Adult prognosis:** Variable; a substantial fraction of adults develop chronic, disabling disease with persistent pain, functional limitation, and psychological comorbidity documented even in long-term (multi-year) follow-up ([PMC11419548](https://pmc.ncbi.nlm.nih.gov/articles/PMC11419548/)).
- **Pediatric prognosis:** Markedly more favorable — remission in roughly **90%** of children with a multidisciplinary approach; one cohort of 103 children found **92% symptom-free** after aerobic/hydrotherapy/desensitization therapy, with **88% remaining symptom-free at ≥2 years follow-up**; mean time to complete resolution was **15.4 weeks** (range 3 days–64 weeks), though **40%** required inpatient treatment and **20%** relapsed ([JPR](https://www.dovepress.com/recovery-from-acute-pediatric-complex-regional-pain-syndrome-type-i-af-peer-reviewed-fulltext-article-JPR); PMC4850724).
- **Relapse risk (pediatric):** Higher in children with greater baseline mental-health difficulty.
- **Prognostic factors:** Early diagnosis (<3 months), early mobilization, aggressive neuropathic pain control, and concurrent attention to mood/sleep are repeatedly identified as favorable prognostic modifiers across both adult and pediatric literature.
- **Quality-of-life outcome measures:** Disability, pain catastrophizing, kinesiophobia, sense of coherence, anxiety, depression, and sleep quality are all significant independent contributors to long-term disability and life satisfaction, supporting biopsychosocial (not purely biomedical) outcome tracking (PMID: 34870547; PMC11419548).

---

## 12. Treatment

### Pharmacotherapy
- **Bisphosphonates** (IV alendronate, IV neridronate, IV pamidronate, IV clodronate) have **high-quality evidence** (consistent, statistically significant pain relief and functional improvement) and are considered, alongside ketamine, a **first-line evidence-based option**, particularly for upper-extremity CRPS.
- **Ketamine** (NMDA-receptor antagonist), given topically or as subanesthetic IV infusion, **significantly reduces CRPS pain**; multi-day outpatient infusions have produced **long-lasting but not permanent** remission ([Curr Pain Headache Rep 2025](https://link.springer.com/article/10.1007/s11916-025-01360-9); PMID: 19783371). Long-term cognitive safety of repeated ketamine dosing remains incompletely characterized.
- **Low-dose naltrexone (LDN):** An emerging, actively-trialed candidate (e.g., ClinicalTrials NCT06306157, Hospital for Special Surgery), hypothesized to act via microglial/TLR4 modulation; early/other-chronic-pain data suggest pain reduction and functional improvement, but CRPS-specific RCT results were not yet available in this search.
- Standard neuropathic pain agents (gabapentinoids, TCAs, SNRIs) and corticosteroids are used clinically but show **less consistent trial-level efficacy** in systematic reviews than bisphosphonates/ketamine.

### Interventional/procedural
- **Sympathetic (stellate ganglion) block:** Meta-analytic evidence (8 studies, 4 RCTs) shows significant pain reduction up to 2 weeks and 4–28 weeks post-procedure, but with **marked study heterogeneity**; a 2022 RCT comparing ropivacaine+clonidine vs. methylprednisolone found **no significant between-group difference** ([Indian J Anaesth 2023](https://journals.lww.com/ijaweb/fulltext/2023/67080/efficacy_of_stellate_ganglion_interventions_for.2.aspx)). Broader reviews note that "clear benefits have not been reported with stellate/lumbar sympathetic blocks" in several syntheses — i.e., evidence is genuinely mixed, not uniformly positive.
- **Stellate ganglion cryoablation:** A 2023 retrospective study reported mean CRPS symptom scores decreasing from 7.0 to 3.8 at 6 months ([JVIR](https://www.jvir.org/article/S1051-0443(23)00725-X/pdf)).
- **Spinal cord stimulation (SCS):** Among the interventions with the strongest evidence for select, refractory cases; carries procedural risk and should be reserved for treatment-resistant patients.
- **Epidural clonidine, intrathecal baclofen** (particularly for CRPS-associated dystonia): reported improvement in smaller studies; further trials needed.

### Rehabilitative / non-invasive
- **Graded motor imagery (GMI)** and **mirror therapy (MT)**: good evidence base, particularly for **acute** CRPS-I; GMI (sequenced as laterality recognition → motor imagery → mirror therapy) reduced pain by an average of ~20 points on the Neuropathic Pain Scale and improved function and swelling in systematic review data ([PMC11428672](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11428672/); PMID: 27858687).
- **Aerobic exercise** and **CBT-informed neurocognitive interventions** (mirror therapy, graded exposure) show consistent pain reduction and functional improvement.
- **Physical/occupational therapy** more broadly is a cornerstone of pediatric management protocols (aerobic exercise, hydrotherapy, desensitization) driving the high pediatric remission rates cited above.

### Experimental / advanced therapeutics
- No approved gene therapy, cell therapy, or targeted biologic exists for CRPS. The mechanistic case for **IL-1 pathway blockade** (from the CRPS-IgG mouse transfer model) represents a plausible future targeted-therapy direction but remains preclinical (PMID: 31182576).
- Active clinical trials as of 2024–2025 include ketamine/midazolam infusion feasibility studies (NCT05945147), low-dose naltrexone RCTs (NCT06306157), pulsed electromagnetic field therapy (NCT05922618), and mesotherapy-delivered ketamine (NCT04650074).

### Treatment strategy
Contemporary guidance favors a **multidisciplinary, staged algorithm**: early functional rehabilitation + neuropathic pain pharmacotherapy + psychological support, escalating to bisphosphonates/ketamine for moderate-severe disease, and reserving sympathetic blocks/SCS for refractory cases — echoing the pediatric model of rapid diagnosis, mobilization, and multidomain (pain + mood + sleep) management reviewed every 4–6 weeks.

**NCIT terms:** `NCIT:C15986` Pharmacotherapy (ketamine, bisphosphonates, LDN as therapeutic_agent); `NCIT:C15302` Physical Therapy (GMI/mirror therapy/aerobic exercise); `NCIT:C15313` Radiation Therapy (n/a); relevant interventional term for nerve block would need an NCIT clinical-procedure lookup (e.g., a nerve-block/ganglion-block term) and for SCS a device/procedure term — verify exact NCIT IDs via `runoak` rather than assuming from this search.

---

## 13. Prevention

- **Primary prevention — Vitamin C:** The best-evidenced prophylactic intervention. Zollinger et al.'s landmark 1999 RCT found CRPS-I incidence of **7% with vitamin C 500 mg/day × 50 days** vs. **22% with placebo** after distal radius fracture (PMID: 17606778 references the 2007 follow-up multicenter dose-response trial across 200/500/1500 mg doses in 331 patients). A subsequent systematic review/meta-analysis supports efficacy in preventing CRPS after wrist fracture, with **no significant safety signal** at 500 mg/day ([ScienceDirect meta-analysis](https://www.sciencedirect.com/science/article/pii/S1877056817300555); [JFAS meta-analysis](https://www.jfas.org/article/S1067-2516(12)00392-4/fulltext)).
- **Secondary prevention (early detection):** Prompt recognition of disproportionate pain/edema after fracture or surgery, with low threshold for early mobilization and multidisciplinary referral — most robustly evidenced in the pediatric literature, where diagnosis within 3 months predicts markedly better outcomes.
- **Tertiary prevention:** Early graded motor imagery/mirror therapy and aerobic exercise to prevent progression to chronic, treatment-refractory disease and to limit maladaptive cortical reorganization.
- **Surgical/procedural prevention:** Minimizing unnecessary tight casting/immobilization duration and considering surgical technique (open vs. closed reduction) in at-risk fracture patients, per the risk-factor data in Section 2.
- **Genetic counseling:** Not applicable in the traditional Mendelian sense given the polygenic/multifactorial risk architecture; HLA-DQ8 or candidate-SNP status is not currently used for pre-emptive counseling or risk stratification in practice.

---

## 14. Other Species / Natural Disease

- CRPS-I as clinically defined (a human diagnostic construct requiring subjective pain report and the Budapest criteria) has **no established natural/spontaneous veterinary correlate** identified in this search; unlike many Mendelian diseases, there is no OMIA (Online Mendelian Inheritance in Animals) entry surfaced for a naturally occurring CRPS analog in companion animals or livestock.
- Comparative biology is instead represented entirely through **induced models** (Section 15) rather than naturally occurring disease in other species — a distinction worth flagging explicitly in the KB entry (i.e., `animal_models` here are all induced/experimental, not natural-disease `PERTURBS`/`RECAPITULATES` analogs of spontaneous veterinary disease).
- No zoonotic or cross-species transmission relevance applies, as CRPS is not an infectious disease.

---

## 15. Model Organisms

Four principal rodent models of CRPS-I are recognized in the literature ([ScienceDirect scoping review](https://www.sciencedirect.com/science/article/abs/pii/S0149763423002932); [Dove/JPR review](https://www.dovepress.com/animal-models-of-complex-regional-pain-syndrome-type-i-peer-reviewed-fulltext-article-JPR)):

1. **Chronic post-ischemia pain (CPIP) model** — tourniquet-induced hind-paw ischemia-reperfusion (3 h tourniquet + reperfusion) in rats. Produces **mechanical and cold allodynia lasting ≥4 weeks**, edema, hyperemia, and oxidative stress, **without direct nerve injury** — closely modeling early/warm-phase CRPS-I vasomotor and sensory features (JoVE 60562; ResearchGate CPIP original description).
2. **Tibia fracture / cast immobilization model** — closed tibial fracture with hindlimb casting in rodents. Recapitulates **warmth, edema, enhanced neurogenic extravasation, epidermal hypertrophy, bone loss, and nociceptive changes**, with an evolution of signs over time resembling chronic human CRPS; however, most post-fracture changes **resolve within ~5 months**, limiting its fidelity as a model of persistent chronic CRPS (PMID: 29684510). This is the model system underlying the IgM/B-cell mechanistic data in Section 6b.
3. **Passive transfer-trauma model** — injection of patient-derived CRPS IgG (or IgM) into injured mice; used specifically to establish the **autoantibody-pathogenicity** and **IL-1-dependent glial activation** findings described in Section 6b (PMID: 31182576).
4. **Needlestick-nerve-injury (NNI) model** — a minor/partial nerve injury paradigm, used to probe boundary mechanisms between CRPS-I (no major nerve lesion) and CRPS-II (defined nerve injury).

**Model characteristics and limitations:**
- CPIP is considered strong for **early, sympathetically-influenced, vasomotor/inflammatory** phenotype recapitulation but does not involve fracture/bone pathology.
- The tibia-fracture model is strong for **bone/trophic and neurogenic-inflammatory** features but its self-limited (~5-month) time course means it may not capture mechanisms that perpetuate genuinely chronic human CRPS — an explicit **human-model translational-fidelity gap** worth flagging in a `HUMAN_MODEL_MISMATCH` framing for KB curation.
- The passive-transfer model isolates the **autoimmune/glial** axis specifically and is the strongest current causal (not just correlative) evidence for autoantibody pathogenicity, since IL-1 blockade both prevents and reverses the induced phenotype.
- **Applications:** These models are used to dissect neurogenic inflammation, test candidate pharmacotherapies (e.g., IL-1 blockade, ketamine analogs), and probe sex-dependent microglial activation dynamics (male mice show more pronounced/earlier microglial activation than females per PMID: 38828388's TLR4-related discussion).
- **Resources:** No dedicated CRPS-specific model registry was surfaced; standard rodent model-organism databases (MGI for mouse strain/genotype resources) would apply for any knockout lines used in the IL-1/B-cell mechanistic studies referenced above.

---

## Summary Table: Suggested Ontology Term Anchors for KB Curation

| Domain | Suggested term(s) |
|---|---|
| Disease | ORPHA:83452; ICD-11 MG30.04; MONDO term to be confirmed against local release |
| Causal/molecular process | GO:0006954 inflammatory response; GO:0002544 chronic inflammatory response |
| Cell types | CL:0000129 microglial cell; CL:0000127 astrocyte; CL:0000092 osteoclast; CL:0000636 sympathetic neuron |
| Anatomy | UBERON:0002398 manus / UBERON:0002387 pes; UBERON:0006459 primary somatosensory cortex; UBERON:0001384 motor cortex |
| Genes | HGNC candidates: ANO10, P2RX7, PRKAG1, SLC12A9 (susceptibility, not causal) |
| Phenotypes | HP terms for allodynia, hyperalgesia, edema, hyperhidrosis, dystonia, osteoporosis (verify exact IDs against current HPO release) |
| Treatment | NCIT:C15986 Pharmacotherapy (therapeutic_agent: ketamine, bisphosphonates, ascorbic acid/vitamin C); NCIT:C15302 Physical Therapy (GMI/mirror therapy) |

---

## Key Evidence Gaps to Flag for Curation

1. **Human-model translational fidelity:** the tibia-fracture model's self-resolving (~5-month) course versus genuinely chronic human CRPS is an explicit mismatch worth a `HUMAN_MODEL_MISMATCH` discussion rather than presenting rodent chronicity data as directly generalizable.
2. **Sympathetic block efficacy** is genuinely mixed across RCTs (not uniformly positive) — evidence items should not overstate certainty here.
3. **Autoantibody pathogenicity** is supported by strong mouse passive-transfer causal evidence (PMID: 31182576) but human-side causal proof (vs. association) is less direct — worth distinguishing MODEL_ORGANISM vs. HUMAN_CLINICAL evidence_source carefully per entry.
4. Exact current **MONDO CURIE** and **HPO term IDs** should be verified via local ontology tooling (OAK/`runoak`) rather than taken from this web-search pass, per the dismech ontology-term contract.

---

### Sources
- [Diagnostic Criteria and Technical Evaluation of Complex Regional Pain Syndrome: A Narrative Review (PMC12428113)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12428113/)
- [Validation of proposed diagnostic criteria ("Budapest Criteria") — PubMed 20493633](https://pubmed.ncbi.nlm.nih.gov/20493633/)
- [The Warm Phase of CRPS Type-1: Is It Time to Review the Budapest Criteria? (PMC12468258)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12468258/)
- [Complex Regional Pain Syndrome: Diagnosis, Pathophysiology, and Treatment Approaches (PMC11756781)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11756781/)
- [Mechanisms of complex regional pain syndrome (PMC11140106 / PMID 38828388)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11140106/)
- [A brief review of complex regional pain syndrome and current management (PMC10993759)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10993759/)
- [The Role of Neuroinflammation in Complex Regional Pain Syndrome (PMID 37701560)](https://pubmed.ncbi.nlm.nih.gov/37701560/)
- [Transfer of CRPS to mice via human autoantibodies — PNAS / PMID 31182576](https://www.pnas.org/doi/10.1073/pnas.1820168116)
- [The Prevalence of Autoantibodies in CRPS Type I (PMC4337272)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4337272/)
- [Genetic HLA Associations in CRPS With and Without Dystonia — J Pain](https://www.jpain.org/article/S1526-5900(12)00655-4/fulltext)
- [Complex regional pain syndrome type I: incidence/prevalence, Olmsted County — PubMed 12749974](https://pubmed.ncbi.nlm.nih.gov/12749974/)
- [Incidence and risk factors for CRPS after distal radius fracture surgery — Sci Rep 2019](https://www.nature.com/articles/s41598-019-41152-x)
- [Risk factors for CRPS in traumatic extremity injury — PubMed 20517769](https://pubmed.ncbi.nlm.nih.gov/20517769/)
- [Nationwide population-based epidemiology of CRPS in South Korea — Sci Rep](https://www.nature.com/articles/s41598-026-45686-9)
- [Analgesic efficacy of therapies for CRPS: systematic review (PMC12413907)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12413907/)
- [Ketamine Infusion for CRPS Treatment: A Narrative Review — Curr Pain Headache Rep 2025](https://link.springer.com/article/10.1007/s11916-025-01360-9)
- [Outpatient IV ketamine for CRPS, double-blind RCT — PubMed 19783371](https://pubmed.ncbi.nlm.nih.gov/19783371/)
- [Low Dose Naltrexone Therapy for CRPS — NCT06306157](https://clinicaltrials.gov/study/NCT06306157)
- [Efficacy of stellate ganglion interventions for CRPS — Indian J Anaesth 2023](https://journals.lww.com/ijaweb/fulltext/2023/67080/efficacy_of_stellate_ganglion_interventions_for.2.aspx)
- [Safety and effectiveness of stellate ganglion cryoablation — JVIR 2023](https://www.jvir.org/article/S1051-0443(23)00725-X/pdf)
- [Breaking the Cycle of Pain: GMI and Mirror Therapy in CRPS (PMC11428672)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11428672/)
- [Update on GMI/mirror therapy systematic review — PubMed 27858687](https://pubmed.ncbi.nlm.nih.gov/27858687/)
- [Can vitamin C prevent CRPS in wrist fractures? — PubMed 17606778](https://pubmed.ncbi.nlm.nih.gov/17606778/)
- [Efficacy of vitamin C preventing CRPS after wrist fracture: meta-analysis](https://www.sciencedirect.com/science/article/pii/S1877056817300555)
- [Efficacy and Safety of High-dose Vitamin C on CRPS — JFAS meta-analysis](https://www.jfas.org/article/S1067-2516(12)00392-4/fulltext)
- [Recovery from acute pediatric CRPS type I — JPR](https://www.dovepress.com/recovery-from-acute-pediatric-complex-regional-pain-syndrome-type-i-af-peer-reviewed-fulltext-article-JPR)
- [Pediatric complex regional pain syndrome: a review (PMC4850724)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4850724/)
- [Clinical phenotypes and classification algorithm for CRPS — Neurology 2020](https://www.neurology.org/doi/10.1212/WNL.0000000000008736)
- [CRPS: cross-sectional study of physical symptoms, disability, psychological health (PMC11419548)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11419548/)
- [Factors associated with disability and pain intensity in CRPS — PubMed 34870547](https://pubmed.ncbi.nlm.nih.gov/34870547/)
- [Somatotopic disruption of sensorimotor cortex functional connectivity in CRPS-I](https://onlinelibrary.wiley.com/doi/full/10.1002/hbm.26513)
- [CRPS Is Not Associated with Altered Sensorimotor Cortex GABA or Glutamate (PMC7029188)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7029188/)
- [Animal models of complex regional pain syndrome: A scoping review — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0149763423002932)
- [The Rodent Tibia Fracture Model: Critical Review — PubMed 29684510](https://pubmed.ncbi.nlm.nih.gov/29684510/)
- [Chronic Post-Ischemia Pain Model for CRPS-I in Rats — JoVE 60562](https://www.jove.com/t/60562/chronic-post-ischemia-pain-model-for-complex-regional-pain-syndrome)
- [Animal models of complex regional pain syndrome type I — JPR/Dove](https://www.dovepress.com/animal-models-of-complex-regional-pain-syndrome-type-i-peer-reviewed-fulltext-article-JPR)
- [Orphanet: Complex regional pain syndrome (ORPHA:83452)](https://www.orpha.net/en/disease/detail/83452)
- [TNF-α and RANKL promote osteoclastogenesis via NF-κB (PMC5928634)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5928634/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 31 |
| On topic | 19 |
| Off topic | 2 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC5928634` (4 mentions) - TNF‑α and RANKL promote osteoclastogenesis by upregulating RANK via the NF‑κB pathway.
  - shared terms: inflammatory
- `PMC:PMC8750957` (1 mention) - Regulation of TNF-Induced Osteoclast Differentiation.
  - shared terms: none

Weighed against this report's own most characteristic terms: `crps`, `pain`, `crps-i`, `model`, `chronic`, `inflammatory`, `motor`, `clinical`, `injury`, `fracture`, `peripheral`, `risk`, `diagnosis`, `disease`, `nerve`, `causal`, `edema`, `patient`, `microglial`, `functional`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.