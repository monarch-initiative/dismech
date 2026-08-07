---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-18T14:28:12.712460'
end_time: '2026-07-18T14:34:38.462053'
duration_seconds: 385.75
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SCN8A-Related Developmental and Epileptic Encephalopathy
  mondo_id: ''
  category: Genetic
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-4-8
  web_search_requests: 7
  num_turns: 11
  total_cost_usd: 1.62914075
  session_id: 34de3db0-7369-4d62-8831-499a7db9c058
  stop_reason: end_turn
citation_count: 15
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SCN8A-Related Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **SCN8A-Related Developmental and Epileptic Encephalopathy** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

Alright, I've got a solid evidence base. Here's the full report.

---

# Research Report: SCN8A-Related Developmental and Epileptic Encephalopathy (SCN8A-DEE / DEE13)

sup Harry — so this one is a genuinely tidy story compared to a lot of the disorders in the KB. It's basically a single ion channel that got stuck in the "on" position, and almost everything downstream — the seizures, the developmental wall kids hit, even the counterintuitive drug choices — falls out of that one broken switch. Think of a sodium channel as a tiny floodgate on a neuron: it's supposed to snap open, let a pulse of charge through, then slam shut. In SCN8A-DEE the gate won't shut all the way, so the neuron keeps leaking current it shouldn't, and the whole brain runs hot. That "gate won't shut" idea is the load-bearing beam of this entire report, so hold onto it.

One important framing note up front, because it shapes everything: **SCN8A is not one disease, it's a spectrum**, and the spectrum splits by *which direction* the channel broke. Gain-of-function (gate too open) → the severe epileptic encephalopathy this report is about. Loss-of-function (gate too weak) → a milder, different-looking condition (intellectual disability, autism, absence epilepsy, movement problems, often *no* severe seizures). Same gene, near-opposite biophysics, near-opposite clinics. I'll flag it wherever it matters.

> **A note on the citations:** I pulled PMIDs straight out of live searches where I could, and I've marked those. A few landmark papers I could only anchor by author/journal/year or PMC ID — I've flagged those explicitly. Per the dismech anti-hallucination SOP, **run `just fetch-reference` on every PMID before it goes into an evidence snippet** — treat this whole report as leads, not gospel. And do the NEC preflight; "SCN8A" is acronym-clean but the DEE-numbered series (DEE13 vs the dozens of other DEE-N entries) is exactly the kind of numbered-series collision that trips deep-research tools.

---

## 1. Disease Information

**What it is.** SCN8A-DEE is a severe, early-onset genetic epilepsy in which de novo variants in the *SCN8A* gene — the gene for the neuronal voltage-gated sodium channel **Nav1.6** — make the channel overactive, so neurons fire when they shouldn't. Kids present in infancy with multiple, hard-to-control seizure types plus developmental impairment (delay and often regression), movement disorders, and a meaningfully raised risk of sudden death (SUDEP). It sits inside the modern ILAE "developmental and epileptic encephalopathy" (DEE) umbrella — the term deliberately captures that the brain dysfunction comes *both* from the ongoing seizure activity *and* from the underlying genetic lesion itself, not seizures alone.

**Key identifiers:**
- **MONDO:** `MONDO:0013801` — "developmental and epileptic encephalopathy, 13" (this is the ID already chosen in your in-progress entry — good match)
- **OMIM:** **#614558** — Developmental and epileptic encephalopathy 13 (DEE13; historically "early infantile epileptic encephalopathy 13 / EIEE13")
- **Gene OMIM:** *SCN8A* = **\*600702**
- **HGNC:** *SCN8A* = **HGNC:10596**
- **UniProt (Nav1.6 protein):** **Q9UQD0** (SCN8A_HUMAN)
- **Orphanet:** SCN8A-related disorders are indexed under Orphanet's DEE grouping — *verify the exact ORPHA code before citing it; I don't want to hand you a fabricated number.*
- **ICD-11:** best fit is `8A61` region (developmental and epileptic encephalopathies); **ICD-10:** G40.4-type early-onset epilepsy codes — neither is SCN8A-specific
- **MeSH:** no dedicated descriptor; falls under *Epileptic Syndromes* / *Spasms, Infantile* / *Epilepsy, Generalized*

**Common synonyms / alternative names:** SCN8A encephalopathy; SCN8A-DEE; DEE13; EIEE13 (older name); early infantile epileptic encephalopathy 13; SCN8A-related epilepsy with encephalopathy (MedlinePlus usage); part of the broader "SCN8A-related disorders" / "SCN8A-related epilepsy and/or neurodevelopmental disorders" (the GeneReviews title, NBK379665).

**Data provenance.** The knowledge here is **aggregated disease-level** — it comes from case series, international genotype-phenotype cohorts, functional electrophysiology studies, mouse models, and caregiver surveys, not from a single individual's EHR. The largest natural-history signal actually comes partly from an **online caregiver survey** (medRxiv 2021, 2021.11.29.21267027) plus patient-registry efforts run through advocacy groups (the SCN8A Alliance / scn8a.net).

---

## 2. Etiology

**Primary cause — genetic, and almost always de novo.** SCN8A-DEE is caused by heterozygous pathogenic variants in *SCN8A*. The overwhelming majority are **de novo missense variants** — brand-new spelling errors that arise in the egg, sperm, or very early embryo and aren't inherited from either parent (MedlinePlus Genetics; GeneReviews NBK379665). There's no environmental trigger, no infection, no toxin. The "cause" is one wrong amino acid in a channel protein.

The mechanistic dividing line that organizes the whole gene:
- **Gain-of-function (GoF)** variants → the channel is too active (leaky/late current, slow to inactivate) → **the DEE phenotype** this report covers. This is the majority of DEE-causing variants.
- **Loss-of-function (LoF)** variants → the channel is underactive/dead → milder neurodevelopmental phenotypes (see §4).

> *"Loss-of-function (LoF) and gain-of-function (GoF) of voltage-gated sodium channels can lead to a wide spectrum of phenotypes… GoF phenotypes include mild to severe epileptic encephalopathy… LoF is associated with cognitive impairment, movement disorders, and autism with or without seizures."* — Johannesen et al., genotype-phenotype correlations (**PMID 34431999**, *Brain* 2022)

**Genetic risk factors.** The variant *is* the risk factor — this is a monogenic, high-penetrance dominant condition for the severe DEE forms. Roughly **>20% of patients carry recurrent mutations at two hotspot arginine residues, Arg1617 (R1617) and Arg1872 (R1872)** (Wagnon et al., **PMID 26900580**). Other recurrent GoF residues include N1768D (the original discovery), T767I, G1451/G1475 region, and R1620. No established common-variant susceptibility loci or GWAS signals — this isn't a polygenic disease.

**Environmental risk factors.** None established as *causal*. The only "environmental" contributor of note is **advanced paternal age**, the generic driver of de novo mutation rate across dominant neurodevelopmental disorders — plausible here by analogy but not specifically quantified for SCN8A. Sex is not a strong risk factor (roughly balanced; see §9). Fever and illness can *provoke* seizures once the disease exists, but they don't cause it.

**Protective factors.** No genetic or environmental protective factors are established. This is worth stating plainly: there's no gnomAD "protective allele," no dietary factor shown to prevent onset. The closest thing to "protection" is entirely therapeutic (early sodium-channel-blocker treatment; see §12), not preventive.

**Gene–environment interactions.** Not a meaningful axis for this disorder. The phenotype is driven by *which* variant (its biophysical severity), not by genotype-by-environment interplay. If anything, the "modifier" story is genetic-background (see §4 modifier genes), not environmental.

---

## 3. Phenotypes

This is a multisystem-*looking* disorder that's really all neurological. Below, grouped by type, with suggested HPO terms and what's known about onset/severity/frequency. Frequencies are approximate and cohort-dependent — **if you enter a `frequency:` band, give it its own evidence per the dismech SOP; a lot of these snippets support the association but not a precise percentage.**

### Seizures / epilepsy (the core)
- **Seizures, multiple types, drug-resistant** — HPO **HP:0001250** (Seizure). Onset **neonatal period to ~18 months, median around 4–5 months** (GeneReviews; Gardella **PMID 30171078**). Nearly universal in the DEE form.
- **Focal (focal-onset) seizures** — HP:0007359 (Focal-onset seizure) — the predominant early type in GoF carriers. *"All 136 individuals carrying a functionally tested gain-of-function variant had either focal or unclassifiable epilepsy"* (Johannesen, PMID 34431999).
- **Epileptic spasms / infantile spasms; West syndrome** — HP:0011097 (Epileptic spasm); West syndrome is described as the most common initial epilepsy syndrome in several series (PMID 31675620).
- **Tonic-clonic** — HP:0002069; **Tonic** — HP:0032792; **Myoclonic** — HP:0032794; **Atypical absence** — HP:0007270. Multiple coexisting types are typical; some evolve to a **Lennox-Gastaut-like** picture.
- **Status epilepticus** — HP:0002133.
- **EEG abnormality** — HP:0002353; background deterioration and multifocal epileptiform discharges with **temporo-occipital predominance** are characteristic (PMID 31675620).

### Developmental / cognitive
- **Global developmental delay** — HP:0001263; **Intellectual disability** — HP:0001249 (often **severe/profound**, HP:0010864). ~50% severe ID in cohorts (BMC Neurology 2023, **PMC10441468**, PMID 37609289).
- **Developmental regression** — HP:0002376 — a hallmark: children may develop normally, then *lose* milestones after seizure onset. *"Normal development may precede subsequent delay or regression following seizure onset."*
- **Absent speech** — HP:0001344; **Autistic behavior** — HP:0000729 (more strongly tied to LoF, but seen across the spectrum).

### Movement / tone
- **Hypotonia** (axial, often severe) — HP:0001252; can coexist with limb **spasticity** — HP:0001257.
- **Ataxia** — HP:0001251; **Dystonia** — HP:0001332; **Choreoathetosis** — HP:0001266. Movement disorders are common, and **~50% of affected individuals are non-ambulatory** (per the SCN8A disorder overview literature).
- **Feeding difficulties / dysphagia** — HP:0011968 / HP:0002015 (common, often needing G-tube).

### Physical / growth / other
- **Microcephaly** (often acquired/postnatal) — HP:0000252 (PMID 31675620).
- **Cortical visual impairment** — HP:0100704; MRI can show **restriction of the optic radiations** and **progressive cerebral/parenchymal atrophy** (PMID 31675620) — HP:0002283 (Progressive cerebral atrophy).
- **Sleep disturbance** — HP:0002360; **constipation/GI dysmotility, autonomic features** commonly reported by caregivers.

### The severe outcome phenotype
- **Sudden unexpected death in epilepsy (SUDEP)** — reported in roughly **~10% of SCN8A-DEE cases**, notably higher than many other DEEs; the original 2012 family was ascertained through SUDEP. There isn't a clean HPO term for SUDEP specifically; **HP:0001695** (Cardiac arrest) / **HP:0031365** relate but aren't exact — best captured in prose + progression.

**Severity & progression pattern.** Highly variable but, for the DEE core: onset in infancy → often a period of regression → chronic, treatment-resistant course. It's **not classically "progressive-neurodegenerative"** in the metabolic sense, but the encephalopathic burden accrues, and MRI atrophy can progress. Seizure burden can improve in some kids on the right sodium-channel blocker (see §12).

**Quality of life.** Profound impact — the severe end means non-verbal, non-ambulatory children with feeding tubes, requiring total care, plus family caregiver burden and constant SUDEP anxiety. No SCN8A-specific EQ-5D/PROMIS dataset exists; QoL is documented qualitatively through the caregiver survey (medRxiv 2021.11.29.21267027).

---

## 4. Genetic / Molecular Information

**Causal gene.** *SCN8A* (HGNC:10596; gene OMIM \*600702), on **chromosome 12q13.13**. It encodes **Nav1.6**, the pore-forming α-subunit of a voltage-gated sodium channel that is *the* dominant sodium channel at the **axon initial segment and nodes of Ranvier** — i.e., exactly the spots where neurons decide whether to fire. That anatomy is why a small biophysical tweak has such outsized effects on excitability.

**Protein architecture (why the hotspots are where they are).** Nav1.6 is one big polypeptide folded into **four homologous domains (DI–DIV)**, each with six transmembrane segments. The **DIII–DIV cytoplasmic linker** contains the "IFM motif" that acts as the *inactivation lid* — the part that swings in to shut the gate after opening. Many severe GoF variants cluster in or near structures that control inactivation, which is why "impaired inactivation" keeps coming up.

**Pathogenic variants:**
- **Type/class:** overwhelmingly **missense** (single amino-acid substitutions). Frameshift/nonsense/whole-gene deletions tend to produce LoF and the milder end; **protein-truncating variants are generally LoF**.
- **Classification:** the recurrent hotspots (R1617, R1872, N1768D, T767I) are **Pathogenic** under ACMG/AMP (recurrent de novo, functionally validated GoF). Many private missense variants sit as **likely pathogenic** or **VUS** pending functional testing — which is a real clinical bottleneck, because GoF-vs-LoF changes the drug plan.
- **Allele frequency:** essentially **absent from gnomAD** for the pathogenic DEE variants (as expected for de novo, severe, reproductively-limiting mutations). *SCN8A* itself is strongly **constrained / intolerant to LoF** in gnomAD.
- **Somatic vs germline:** **germline** (de novo germline/early-embryonic). Rare **parental mosaicism** has been documented and matters for recurrence counseling (see §9).

**Functional consequences — the heart of the mechanism:**
- **Gain-of-function (DEE):** impaired/incomplete fast inactivation, increased **persistent sodium current (I_NaP_)** — the "late leak" — and/or premature activation. Net effect: neurons that are too easy to fire and that keep firing. Different hotspots break it slightly differently:
  - **R1872W/Q/L and N1768D** → primarily **impair inactivation** (gate won't shut) → persistent current (Wagnon PMID 26900580; Veeramah 2012 for N1768D).
  - **T767I** → primarily **premature activation** (gate opens too easily) — a distinct flavor of GoF (noted in the newer T767I mouse model literature).
  - *"Recurrent mutations at Arg1617 and Arg1872 lead to elevated Nav1.6 channel activity by impairing channel inactivation."* (PMID 26900580)
- **Loss-of-function:** reduced/abolished current → the milder ID/autism/absence phenotype (de novo GoF *and* LoF paper, PMC4413743). Enter these as a **separate, contrasting** note, not as the DEE mechanism.
- Emerging nuance: some variants show **mixed GoF/LoF** biophysics, and there are severe-LoF cases too — the binary is a useful first approximation, not the whole truth (Johannesen PMID 34431999; Hack et al. 2024, below).

**The 2024 five-subgroup refinement.** Hack et al., *Epilepsia* 2024 (article 10.1111/epi.18118) proposed that patients sort into **five subgroups** blending developmental and epileptic components rather than a clean GoF/LoF split — worth citing as the current state-of-the-art nosology. *Get the exact PMID via `just fetch-reference` before quoting.*

**Modifier genes.** In mouse models, **genetic background dramatically modifies severity/survival** — e.g., Scn8a variant mice on different strains show different seizure and lethality outcomes, and *Scn1a* (Nav1.1) dosage interacts with *Scn8a* (the two channels push excitation in opposite directions). Human modifier loci aren't firmly established but this is an active area.

**Epigenetics / chromosomal abnormalities.** Not a feature. No methylation signature, no recurrent CNV/translocation mechanism — this is a point-mutation disease. (Large 12q13 deletions spanning *SCN8A* would give LoF-type presentations, not the classic DEE.)

---

## 5. Environmental Information

Short section, because the honest answer is **"basically none."**
- **Environmental factors / toxins / radiation:** none causal. No CTD-type toxicogenomic driver.
- **Lifestyle factors:** not applicable (infantile-onset genetic disease). Parental factors like advanced paternal age modulate de novo mutation *rate* generally but aren't disease-specific.
- **Infectious agents:** none. Fever/intercurrent illness can *provoke* seizures in an already-affected child (a trigger, not a cause).

---

## 6. Mechanism / Pathophysiology

Here's the causal chain, upstream → downstream. This is the part that maps cleanly onto your `pathophysiology` node structure and, importantly, onto the existing **`epilepsy_excitation_inhibition_imbalance`** module (key conformance target: `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance`) — SCN8A-DEE is close to a textbook conformer for it.

**The causal chain:**

1. **De novo GoF missense variant in SCN8A** (trigger) → altered Nav1.6 channel protein.
2. **Biophysical defect: impaired fast inactivation and/or premature activation → increased persistent Na⁺ current (I_NaP_).** The floodgate won't fully close. GO terms: **GO:0086010** (membrane depolarization during action potential), **GO:0001518** (voltage-gated sodium channel complex, cellular component), **GO:0086002** (cardiac/neuronal membrane repolarization–related), **GO:0019228** (neuronal action potential).
3. **Neuronal hyperexcitability** — chiefly in **excitatory pyramidal/glutamatergic neurons**, whose axon initial segments are rich in Nav1.6. They fire too readily and repetitively. GO:0060078 (regulation of postsynaptic membrane potential); GO:0050804 (modulation of chemical synaptic transmission).
4. **Excitation–inhibition (E/I) imbalance and hypersynchrony** across cortical networks. Notably, there's evidence that **parvalbumin⁺ inhibitory interneurons are also impaired** in SCN8A models (bioRxiv 2024.02.09.579511), so it's not purely "excitatory neurons on overdrive" — the inhibitory brake also fails, compounding the imbalance.
5. **Seizure generation and epileptogenesis** → recurrent seizures + ongoing encephalopathy → **developmental impairment/regression** (the "D" in DEE) and, via mechanisms overlapping cardiorespiratory/brainstem dysfunction, **elevated SUDEP risk**.

**Cell types (CL suggestions):**
- **CL:0000598** (pyramidal neuron) / **CL:0000679** (glutamatergic neuron) — primary drivers.
- **CL:0000617** (GABAergic neuron) and specifically **parvalbumin interneurons** — impaired inhibition arm.
- **CL:0000540** (neuron) as the generic anchor.

**Subcellular / cellular-component (GO CC):**
- **GO:0001518** (voltage-gated sodium channel complex).
- **Axon initial segment — GO:0043194**; **node of Ranvier — GO:0033268** — the anatomical loci where Nav1.6 concentrates and where the defect bites hardest.
- **Plasma membrane — GO:0005886.**

**Protein dysfunction.** Not misfolding/aggregation — the channel largely traffics and folds fine; it's a **functional gating defect** (gain-of-function at the level of channel kinetics). UniProt Q9UQD0; structural context from cryo-EM Nav1.6 structures and AlphaFold. This is mechanistically important because it means the therapeutic strategy is to **block/dampen** an over-present function, not to *replace* a missing one — which is exactly why sodium-channel *blockers* work and why ASO knockdown (turning the gene *down*) is the leading experimental therapy (see §12/§15).

**Metabolic / immune / other.** No primary metabolic defect, no autoimmune/inflammatory mechanism, no enzyme deficiency. It's a channelopathy, full stop — which is a nice clean contrast to the metabolic-intoxication and lysosomal-storage disorders elsewhere in the KB.

**Molecular profiling.** The richest data are **electrophysiological** (voltage-clamp of mutant channels in heterologous cells; patch-clamp of iPSC-derived neurons showing variant-specific persistent/resurgent current — bioRxiv 2020.01.16.909192) and **in vivo mouse EEG/behavior**. There isn't a defining transcriptomic/proteomic/metabolomic signature for diagnosis — the diagnosis is genetic, and the "profiling" that matters clinically is the functional GoF-vs-LoF assay.

**Classification framing.** This is a **channelopathy** (mechanistic nosology) and an **excitation-inhibition-imbalance epilepsy**; strong candidate to declare `conforms_to: "epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance"` on the seizure-generation node, substituting Nav1.6/I_NaP_ as the disease-specific driver.

---

## 7. Anatomical Structures Affected

- **Organ / system level:** the **central nervous system** is the target organ; specifically the **cerebral cortex** and broader **brain** (UBERON:0000955). This is a **nervous-system** disorder with essentially no primary involvement of other organ systems — cardiac/respiratory involvement enters only via seizure/SUDEP physiology, not structural heart/lung disease.
  - **Cerebral cortex — UBERON:0000956**
  - **Cerebellum — UBERON:0002037** (ataxia, cerebellar signs; Nav1.6 is highly expressed in cerebellar granule/Purkinje neurons)
  - **Brainstem — UBERON:0002298** (relevant to SUDEP/autonomic mechanisms)
  - **Optic radiation / visual pathway — UBERON:0002391** (MRI restriction reported; cortical visual impairment)
- **Tissue / cell level:** **gray matter neurons** — pyramidal/glutamatergic (CL:0000598/CL:0000679) and GABAergic/parvalbumin interneurons (CL:0000617). Nervous tissue (UBERON:0003714, neural tissue).
- **Subcellular:** the **axon initial segment (GO:0043194)** and **nodes of Ranvier (GO:0033268)** — the Nav1.6-rich firing-decision zones — plus the neuronal **plasma membrane (GO:0005886)** and the **voltage-gated sodium channel complex (GO:0001518)**.
- **Localization / lateralization:** diffuse and **bilateral** brain involvement; EEG epileptiform abnormalities often show **temporo-occipital predominance** but the process is generalized, not focal-structural. Progressive **bilateral cerebral atrophy** on MRI in more severe cases; MRI is often normal early.

---

## 8. Temporal Development

- **Onset age:** **infantile**, typically **neonatal period to ~18 months, with a median around 4–5 months** (Gardella PMID 30171078; GeneReviews). A minority present later (into childhood) with milder GoF variants; some cohorts report a range out to ~10 years for the broader spectrum (PMC10441468).
- **Onset pattern:** **subacute to chronic** — seizures emerge in a previously (often) normally developing infant, then the encephalopathy sets in.
- **Disease stages / course:** roughly (1) **pre-symptomatic infancy**, (2) **seizure onset**, (3) **regression / plateau** of development coincident with seizure burden, (4) **chronic drug-resistant epilepsy** with fixed severe disability at the severe end — or, at the milder end, **partial or complete seizure control** on the right sodium-channel blocker with better developmental trajectory.
- **Course pattern:** **chronic and lifelong**; seizures often **drug-resistant** but can be **episodic/fluctuating** in frequency, with clusters and status. Not classically relapsing-remitting.
- **Remission:** **treatment-induced** seizure freedom is achievable in a subset (notably with high-dose phenytoin/carbamazepine/oxcarbazepine — see §12); spontaneous remission is not the rule for the DEE form (contrast the *benign familial infantile seizures* end of the SCN8A spectrum, which does remit).
- **Critical window:** the strong argument for **early genetic diagnosis** is that getting a GoF child onto a sodium-channel blocker *early* may improve seizure control and possibly developmental outcome — the "critical period for intervention" is essentially "as soon as you know it's GoF-SCN8A." Diagnosis is, unfortunately, **often delayed** (PMID 31675620).

---

## 9. Inheritance and Population

**Epidemiology.**
- **Incidence:** reported at **just over 1 in ~56,000 births** for SCN8A-related disorders (research roadmap, *Orphanet J Rare Dis* 2025, PMC12366098). 
- **Prevalence:** estimated **~2.96 per 100,000 individuals (95% CI 2.63–3.24)** in a survey of de novo dominant neurodevelopmental disorders (same roadmap source). 
- **Burden context:** **>400–700 individuals** identified worldwide since the 2012 discovery; SCN8A pathogenic variants account for **~1% of epileptic encephalopathy** cases.
- `rate_per_100000` for a `Prevalence` record: **~2.96**, `measure_type: POINT_PREVALENCE`, `prevalence_class: BAND_1_9_PER_100000`. (Verify the exact figure/source before entry.)

**Inheritance / genetics for a KB `Inheritance` block:**
- **Pattern:** **Autosomal dominant** — bind `inheritance_term` to **HP:0000006** (Autosomal dominant inheritance). Nearly all severe DEE cases are **de novo** (HP:0025352, "Typified by de novo mutations" — or note de novo in the description).
- **Penetrance:** effectively **complete/high** for the severe GoF DEE variants (they cause disease when present). The milder LoF/benign end shows more variable expressivity.
- **Expressivity:** **variable** overall across the gene — same recurrent variant can give somewhat different severity, and background modifiers matter.
- **Anticipation:** **not applicable** (not a repeat-expansion disorder).
- **Germline/somatic mosaicism:** **parental (germline) mosaicism has been reported** and is the key counseling caveat — an unaffected parent can carry the variant in a fraction of germ cells, giving a **recurrence risk above the "essentially zero" you'd naively assume for a de novo event** (GeneReviews NBK379665). Empiric sib recurrence risk is low but non-zero (~1–2% range cited in genetic-counseling literature).
- **Founder effects / consanguinity:** **none** — de novo dominant disease, not enriched by consanguinity, no founder haplotype.
- **Carrier frequency:** not applicable in the recessive-carrier sense.

**Population demographics.**
- **Ethnic/geographic distribution:** **pan-ethnic, worldwide, no known population enrichment** (de novo mechanism → no geographic clustering, no endemic areas).
- **Sex ratio:** approximately **1:1** (autosomal, no strong sex bias reported).
- **Age distribution:** overwhelmingly **infants/children** at presentation; the prevalent living population skews pediatric-to-young-adult, shaped by both recent recognition of the disorder and by mortality.

---

## 10. Diagnostics

**The diagnosis is genetic.** Everything else supports or contextualizes.

**Genetic testing (the definitive path):**
- **First-line in practice:** a **multigene epilepsy/DEE panel** or, increasingly, **whole-exome (WES)** or **whole-genome (WGS)** sequencing — the 2012 index case was found by whole-genome sequencing of a family quartet (Veeramah et al., *Am J Hum Genet* 2012; anchor PMID via fetch — commonly cited as PMID 22365152, **verify**).
- **Single-gene testing** is reasonable only with a very classic picture; the phenotype overlaps too many DEEs to skip broad testing generally.
- **Chromosomal microarray / karyotype / FISH:** low yield for the classic missense DEE (it's a point mutation), but CMA can catch the rare 12q13 deletion cases.
- **The functional follow-through that's unique here:** once a variant is found, **determining GoF vs LoF** (by voltage-clamp electrophysiology, or by inference from variant type/location) is what turns a molecular diagnosis into a *treatment* decision. This is the disorder's signature diagnostic wrinkle. VUS are common and clinically frustrating.
- **GTR / ClinVar / ClinGen** are the go-to for variant interpretation; report GTR-listed panels and ClinVar classifications.

**Supporting clinical tests (not diagnostic on their own):**
- **EEG:** background slowing/deterioration, **multifocal epileptiform discharges, temporo-occipital predominance**, sometimes hypsarrhythmia (West syndrome) (PMID 31675620). LOINC-codable EEG panel.
- **Brain MRI:** often **normal early**; later can show **progressive cerebral/cerebellar atrophy** and **optic radiation restriction** — supportive, non-specific.
- **Labs:** routine metabolic workup is **normal** (helps *exclude* metabolic mimics). No diagnostic biomarker, no enzyme assay, no metabolite signature.
- **No omics/liquid-biopsy diagnostic** exists.

**Clinical criteria / differential diagnosis.** No SCN8A-specific clinical criteria; diagnosis rests on the DEE clinical picture + confirmed pathogenic *SCN8A* variant. **Differential includes the other early-infantile DEEs** — especially the sibling sodium channelopathies **SCN1A (Dravet), SCN2A, SCN3A**, plus **KCNQ2, STXBP1, CDKL5, KCNT1, PCDH19** — distinguished essentially by gene panel/exome. The GoF-vs-LoF distinction and the *response to sodium-channel blockers* (helps, rather than worsens, in SCN8A-GoF — the opposite of Dravet/SCN1A, where they can worsen seizures) are useful clinical discriminators.

**Screening.** **No newborn/population screening** exists (it's de novo, so carrier/cascade screening doesn't apply). Prenatal testing is possible only for a known familial variant or documented parental mosaicism.

---

## 11. Outcome / Prognosis

- **Mortality / SUDEP:** the sobering headline — **SUDEP in ~10% of SCN8A-DEE**, higher than many DEEs; the founding family was ascertained through a SUDEP death. Overall early mortality is elevated. No clean 5-/10-year survival table exists (rare disease, recent recognition), but this is a **shortened-life-expectancy** condition at the severe end.
- **Morbidity / function:** at the severe end, **profound**: ~50% non-ambulatory, ~50% severe intellectual disability, many non-verbal and tube-fed, requiring lifelong total care. The milder GoF end can have well-controlled seizures and better cognition.
- **Disease course / complications:** drug-resistant seizures, status epilepticus, aspiration/respiratory infections, feeding failure, orthopedic complications of tone abnormalities, and the ever-present SUDEP risk.
- **Prognostic factors:** **variant identity and its biophysical severity** are the dominant prognostic drivers — severe GoF (e.g., certain R1872/N1768D) → severe phenotype; milder GoF or the benign-familial end → better outcomes. **Earlier effective seizure control** (right sodium-channel blocker, early) associates with better trajectories. There is **no correlation between age of seizure onset and degree of developmental delay** in at least one cohort (PMC10441468) — a useful caveat against over-reading onset age as prognosis.
- **Prognostic biomarkers:** none molecular beyond the variant itself and its functional class.

---

## 12. Treatment

This is where SCN8A-DEE earns its "precision medicine poster child" reputation — because the mechanism (too-open sodium gate) points straight at the drug class that closes it.

**Pharmacotherapy — sodium-channel blockers (the mechanism-matched first choice for GoF):**
- **Phenytoin / fosphenytoin** — often **high-dose**, with striking responses. *"Four patients with a missense SCN8A mutation and epilepsy all showed a remarkably good response on high doses of phenytoin and loss of seizure control when phenytoin medication was reduced."* (Boerma et al., *Neurotherapeutics* 2016 — "Remarkable Phenytoin Sensitivity," anchor PMID via fetch; commonly **PMID 26252990**, **verify**). CHEBI: phenytoin **CHEBI:8107**.
- **Carbamazepine** (CHEBI:3387) and **oxcarbazepine** (CHEBI:7824) — several patients reach **seizure freedom on carbamazepine monotherapy** (PMC10441468).
- **Lacosamide, lamotrigine, phenytoin's cousins** — also used; lacosamide (CHEBI:141313) targets slow inactivation, mechanistically attractive.
- **Precision-medicine framing:** *"Treatment with sodium channel blockers, especially high doses of phenytoin, carbamazepine, or oxcarbazepine, benefits some affected individuals"*; roughly **half of patients show good responses to sodium-channel-modulating anticonvulsants** (Precision Medicine: SCN8A Encephalopathy Treated with Sodium Channel Blockers, *Neurotherapeutics* 2015, PMC4720666). GoF variant carriers respond **significantly better to sodium-channel blockers than to other ASMs** (Johannesen PMID 34431999). **Critical caveat:** this logic **inverts for LoF variants** — sodium-channel blockers can worsen the LoF end, which is exactly why the GoF/LoF functional call matters clinically.
- **Newer add-on:** **cenobamate** as add-on for SCN8A-DEE shows promise (medRxiv 2024.10.17.24312949) — worth a `clinical_trials`/treatment note.
- Other ASMs used adjunctively: valproate (CHEBI:39867), clobazam, topiramate, levetiracetam, plus the ketogenic diet in some.

**MAXO / treatment-term mapping suggestions:**
- Sodium-channel-blocker pharmacotherapy → `treatment_term` **NCIT:C15986** (Pharmacotherapy) + `therapeutic_agent` CHEBI (phenytoin CHEBI:8107, carbamazepine CHEBI:3387, oxcarbazepine CHEBI:7824). Consider `therapeutic_modality: SMALL_MOLECULE`.
- **Dietary intervention (ketogenic diet)** → **MAXO:0000088** (dietary intervention).
- **Supportive/palliative care** → **MAXO:0000950** (supportive care).
- **Epilepsy surgery / VNS** where relevant → **MAXO:0000004** (surgical procedure); VNS is a **DEVICE** modality. Some drug-resistant cases get **VNS or callosotomy**, with modest benefit.
- **Genetic counseling** → **MAXO:0000079**.

**Advanced / experimental therapeutics (the frontier — mechanism says "turn the gene down"):**
- **Antisense oligonucleotides (ASO)** — the leading candidate. Because DEE is GoF, **knocking down Scn8a transcript is protective**: *"Reduction of Scn8a transcript by 25 to 50% delayed seizure onset and lethality in mouse models of SCN8A encephalopathy and Dravet syndrome"*; a single ASO dose extended survival in Scn8a-R1872W/+ mice (from ~15 to ~65 days) and in Dravet mice (from ~3 weeks to >5 months) (**Lenk et al., *Ann Neurol* 2020, PMID 31943325**). This is a strong `antisense_oligonucleotide_therapy` module fit (RNase-H knockdown paradigm; `aso_mechanism: RNASE_H_KNOCKDOWN`, `target_gene` SCN8A) — though note these are **preclinical/model-organism** results; check ClinicalTrials.gov for any human trials before implying clinical availability.
- **CRISPR base editing** — a 2024/2025 mouse study reports **base editing rescues seizures and sudden death** in an SCN8A-DEE model (PMC12871382) — very early, MODEL_ORGANISM evidence.
- **Allele-specific / gene-modulation strategies** more broadly are reviewed in the 2024 ASO-for-DEE review (Quilón et al., *CNS Neurosci Ther* 2024, PMC11551783).

**Pharmacogenomics.** The "pharmacogenomics" here is unusual and central: it's **the disease variant itself (GoF vs LoF) that dictates drug choice**, not classic CYP metabolizer status. That's the whole precision-medicine pitch.

**Treatment outcomes / adverse events.** Sodium-channel blockers at high dose bring the usual risks (phenytoin: gum hyperplasia, ataxia, dose-related toxicity; carbamazepine/oxcarbazepine: hyponatremia, rash including rare HLA-B*15:02-linked SJS/TEN — a nice cross-link to the `drug_hypersensitivity_scar` module for the aromatic antiepileptics). Response is partial in ~half; a substantial fraction remain drug-resistant.

---

## 13. Prevention

Honest framing: for a **de novo dominant** disease, "prevention" is mostly about **recurrence-risk counseling and secondary prevention of complications**, not primary prevention.

- **Primary prevention:** **not possible** — you can't prevent a de novo germline mutation. No vaccine, no lifestyle modification, no environmental control applies.
- **Secondary prevention (early detection → early right treatment):** the real actionable lever. **Early genetic diagnosis** → early GoF-vs-LoF determination → early mechanism-matched sodium-channel blocker → potentially better seizure control and developmental outcome. This is the strongest "prevention" argument in the disorder.
- **Tertiary prevention (complication avoidance):** SUDEP-risk counseling and mitigation (seizure control, nocturnal monitoring), aspiration/nutrition management, tone/orthopedic management, status-epilepticus rescue plans.
- **Genetic counseling / reproductive options:** for families with an affected child — discuss the **low-but-non-zero recurrence risk from possible parental germline mosaicism**, and offer **prenatal testing or preimplantation genetic testing (PGT)** for a *known* familial variant. → **MAXO:0000079** (genetic counseling).
- **Public-health / immunization / environmental interventions:** **not applicable.**

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *SCN8A* is deeply conserved. Mouse ortholog **Scn8a** (**NCBI Gene 20964**); rat, zebrafish (*scn8ab*/*scn8aa*) orthologs exist. Human *SCN8A* = **NCBI Gene 6334**.
- **Natural disease in animals:** the historically important one is the **mouse** — the original *Scn8a* mutants (**"motor endplate disease," *med***) arose spontaneously and gave dystonia, tremor, ataxia, muscle weakness, and early death from **loss-of-function** *Scn8a* alleles. So the *natural* mouse mutants model the **LoF** end (movement/motor phenotype), while the human-DEE **GoF** models are engineered (see §15). No well-characterized companion-animal (OMIA) natural SCN8A-DEE analog is established — worth a quick OMIA check but I wouldn't assert one.
- **Comparative biology / conservation:** the Nav1.6 protein and its axon-initial-segment/node-of-Ranvier role are conserved across mammals, which is *why* mouse models recapitulate the biology so well — the disease mechanism (channel gating at firing-decision zones) is evolutionarily conserved.
- **Zoonotic potential / cross-species transmission:** **not applicable** (genetic, non-transmissible).

---

## 15. Model Organisms

The mouse is the workhorse here, and the models map neatly onto the GoF/LoF split.

**Mouse (primary):**
- **Knock-in GoF models** engineered with human DEE variants:
  - **Scn8a-N1768D/+** — the first knock-in of a human DEE GoF variant; recapitulates **spontaneous seizures, ataxia, and premature death/SUDEP-like sudden death** (impaired-inactivation mechanism).
  - **Scn8a-R1872W/+** — conditional/knock-in; seizures and lethality; the ASO-rescue survival experiments used this line (Lenk PMID 31943325).
  - **Scn8a-T767I** — newer model, **premature-activation** mechanism (distinct from the impaired-inactivation lines), used to dissect how different GoF flavors give motor vs seizure phenotypes.
- **Natural LoF mutants (*med*, *med^jo^*, *jolting*)** — spontaneous *Scn8a* loss/hypomorph alleles giving **motor/movement phenotypes** (dystonia, tremor, ataxia, weakness) rather than seizures — model the *human LoF* end and were the original tools that defined Nav1.6 biology.
- **Cre-conditional lines** let researchers restrict the variant to excitatory vs inhibitory neurons, which is how the field showed **excitatory-neuron GoF drives seizures** while separating out motor contributions.

**Cellular / in vitro:**
- **Heterologous expression** (ND7/23, HEK, Xenopus oocytes) for voltage-clamp characterization of individual variants — the assay that assigns **GoF vs LoF** (Wagnon PMID 26900580; Acta Pharmacol Sin 2022 PMID 35902765).
- **iPSC-derived neurons** from patients — show **variant-specific increases in persistent/resurgent Na⁺ current** (bioRxiv 2020.01.16.909192), bringing the model closer to human biology.
- **Primary cortical neuron cultures** (e.g., from C57BL/6J E14 embryos) used for ASO dose-response work (Lenk 2020).

**Model characteristics — recapitulation & limits:**
- **Recapitulation:** GoF knock-in mice reproduce the cardinal features well — **spontaneous seizures, developmental/motor impairment, and sudden death** — and, crucially, respond to the same **sodium-channel-blocker and ASO** interventions, giving strong translational face validity.
- **Limitations:** mouse **genetic background strongly modifies severity/survival**, complicating comparisons; mice don't capture the full human cognitive/behavioral phenotype; and the natural *med* mutants model LoF, not the DEE GoF — so you have to pick the model to match the mechanism you're studying. iPSC models capture channel biophysics but not circuit-level seizures.

**Resources:** MGI (Scn8a, gene ID MGI:103169), IMPC/KOMP for engineered alleles, JAX for many of the Scn8a lines, Alliance of Genome Resources for orthology.

---

## Suggested ontology-term cheat-sheet (for the KB entry)

| Domain | Term(s) |
|---|---|
| Disease | MONDO:0013801; OMIM:614558 |
| Gene | HGNC:10596 (SCN8A); Nav1.6 protein UniProt Q9UQD0 |
| Core phenotypes | HP:0001250 (Seizure), HP:0007359 (Focal seizure), HP:0011097 (Epileptic spasm), HP:0001263 (Global dev delay), HP:0002376 (Dev regression), HP:0001249 (Intellectual disability), HP:0001252 (Hypotonia), HP:0001251 (Ataxia), HP:0000252 (Microcephaly), HP:0002353 (EEG abnormality) |
| Biological process (GO) | GO:0019228 (neuronal action potential), GO:0086010 (membrane depolarization during AP), GO:0050804 (modulation of synaptic transmission) |
| Cellular component (GO) | GO:0001518 (VG sodium channel complex), GO:0043194 (axon initial segment), GO:0033268 (node of Ranvier) |
| Cell types (CL) | CL:0000598 (pyramidal neuron), CL:0000679 (glutamatergic neuron), CL:0000617 (GABAergic neuron) |
| Anatomy (UBERON) | UBERON:0000955 (brain), UBERON:0000956 (cerebral cortex), UBERON:0002037 (cerebellum) |
| Chemicals (CHEBI) | CHEBI:8107 (phenytoin), CHEBI:3387 (carbamazepine), CHEBI:7824 (oxcarbazepine) |
| Treatments (MAXO) | MAXO:0000088 (dietary/ketogenic), MAXO:0000950 (supportive care), MAXO:0000079 (genetic counseling), MAXO:0000004 (surgical procedure) |
| Module fit | `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance`; `antisense_oligonucleotide_therapy#Pathogenic mRNA Accumulation` (ASO knockdown) |

---

## Key references (verify every PMID with `just fetch-reference` before use)

- Veeramah et al. — original de novo *SCN8A* N1768D discovery via WGS in a DEE+SUDEP quartet, *Am J Hum Genet* 2012 *(commonly cited as PMID 22365152 — verify)*
- Larsen et al. — *The phenotypic spectrum of SCN8A encephalopathy*, *Neurology* 2015 *(anchor PMID via fetch)*
- Gardella et al. — *The phenotype of SCN8A developmental and epileptic encephalopathy* — **PMID 30171078**
- Wagnon et al. — *Pathogenic mechanism of recurrent mutations of SCN8A in epileptic encephalopathy*, *Ann Clin Transl Neurol* 2016 — **PMID 26900580**
- *SCN8A epileptic encephalopathy mutations display a gain-of-function phenotype and divergent sensitivity to antiepileptic drugs*, *Acta Pharmacol Sin* 2022 — **PMID 35902765**
- Johannesen et al. — *Genotype-phenotype correlations in SCN8A-related disorders reveal prognostic and therapeutic implications*, *Brain* 2022 — **PMID 34431999**
- *Genetic and clinical features of SCN8A developmental and epileptic encephalopathy*, 2019 — **PMID 31675620**
- Hack et al. — five-subgroup classification, *Epilepsia* 2024 (10.1111/epi.18118) *(PMID via fetch)*
- Boerma et al. — *Remarkable Phenytoin Sensitivity in 4 Children with SCN8A-related Epilepsy*, *Neurotherapeutics* 2016 *(commonly PMID 26252990 — verify)*
- *Precision Medicine: SCN8A Encephalopathy Treated with Sodium Channel Blockers*, *Neurotherapeutics* 2015 — PMC4720666
- Lenk et al. — *Scn8a Antisense Oligonucleotide Is Protective in Mouse Models of SCN8A Encephalopathy and Dravet Syndrome*, *Ann Neurol* 2020 — **PMID 31943325**
- *A research roadmap for SCN8A-related disorders*, *Orphanet J Rare Dis* 2025 — PMC12366098
- GeneReviews — *SCN8A-Related Epilepsy and/or Neurodevelopmental Disorders* — NBK379665

**Sources (web):**
- [SCN8A GoF mutations & divergent AED sensitivity (PMID 35902765)](https://pubmed.ncbi.nlm.nih.gov/35902765/)
- [Wagnon et al., recurrent SCN8A mechanism (PMID 26900580)](https://pubmed.ncbi.nlm.nih.gov/26900580/)
- [Johannesen et al., genotype-phenotype (PMID 34431999)](https://pubmed.ncbi.nlm.nih.gov/34431999/)
- [Expanding the genotype-phenotype spectrum (PMC10441468)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10441468/)
- [Hack et al., five subgroups, Epilepsia 2024](https://onlinelibrary.wiley.com/doi/abs/10.1111/epi.18118)
- [Remarkable phenytoin sensitivity, Neurotherapeutics](https://link.springer.com/article/10.1007/s13311-015-0372-8)
- [Precision Medicine: SCN8A treated with sodium channel blockers (PMC4720666)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4720666/)
- [Lenk et al., Scn8a ASO (PMID 31943325)](https://pubmed.ncbi.nlm.nih.gov/31943325/)
- [Genetic and clinical features of SCN8A-DEE (PMID 31675620)](https://pubmed.ncbi.nlm.nih.gov/31675620/)
- [Gardella et al., phenotype of SCN8A-DEE (PMID 30171078)](https://pubmed.ncbi.nlm.nih.gov/30171078/)
- [Research roadmap for SCN8A-related disorders (PMC12366098)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12366098/)
- [GeneReviews: SCN8A-Related Epilepsy and/or NDD (NBK379665)](https://www.ncbi.nlm.nih.gov/books/NBK379665/)
- [MedlinePlus Genetics: SCN8A-related epilepsy with encephalopathy](https://medlineplus.gov/genetics/condition/scn8a-related-epilepsy-with-encephalopathy/)
- [ASOs as precision therapy for DEEs, CNS Neurosci Ther 2024 (PMC11551783)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11551783/)
- [Base editing rescues seizures in SCN8A-DEE model (PMC12871382)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12871382/)

---

**Two curation flags before you build the entry:** (1) your in-progress YAML already nails the GoF framing and MONDO:0013801 — this report backs that up and adds the incidence/prevalence numbers, the five-subgroup nuance, the parvalbumin-interneuron wrinkle, and the ASO/base-editing frontier. (2) The single biggest evidence-discipline risk here is the **GoF-vs-LoF split** — make sure every phenotype/treatment snippet you attach is actually describing the *GoF DEE* end and not the LoF milder end, because a lot of "SCN8A" abstracts blend both and it's easy to attach a LoF-cohort statistic to a GoF claim. That's the semantic trap, not a hallucination trap, so the standard validators won't catch it — only your reading will.