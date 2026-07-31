---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-20T09:38:00.542700'
end_time: '2026-07-20T09:44:12.781738'
duration_seconds: 372.24
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Rasmussen Encephalitis
  mondo_id: ''
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-4-8
  web_search_requests: 8
  num_turns: 18
  total_cost_usd: 1.9662035
  session_id: 7d00f0e3-0d0b-44b6-9b0b-f6546589aba5
  stop_reason: end_turn
citation_count: 20
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Rasmussen Encephalitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Rasmussen Encephalitis** covering all of the
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

Got everything I need. Here's the full report — and a heads up before you dive in: per the dismech DR-verification SOP, treat every PMID and quote below as a **lead**, not gospel. I pulled these from live web sources and verified the ontology IDs locally with OAK, but the snippets still need `just fetch-reference` + `validate-references` before any of them land in YAML. Flagged the shakier citations inline.

---

# Rasmussen Encephalitis — Comprehensive Research Report

> **Disease:** Rasmussen Encephalitis (RE) · also "Rasmussen syndrome" (the field is drifting toward "syndrome")
> **MONDO:** `MONDO:0016019` (label: *Rasmussen subacute encephalitis*, verified via local OAK)
> **Category:** Complex (immune-mediated, one-hemisphere neuroinflammatory epilepsy)

The one-sentence version: RE is a rare, sneaky, one-sided brain fire. A T-cell–driven inflammatory process sets up shop in a single cerebral hemisphere of a previously healthy kid, and over months to a couple of years it burns that hemisphere down — relentless focal seizures, a slowly failing arm and leg, a shrinking half-brain on MRI. It's the rare case in neurology where the *cure* for the seizures is to functionally disconnect half the brain, because the other half is fine and the sick half won't stop.

---

## 1. Disease Information

RE is a rare, progressive, chronic encephalitis of unknown trigger that is almost always confined to **one cerebral hemisphere**. The 2024 comprehensive review frames it plainly: *"Rasmussen encephalitis (RE) is a rare and progressive form of chronic encephalitis that typically affects one hemisphere of the brain and primarily occurs in pediatric individuals"* and is *"characterized by recurrent seizures, delayed developmental milestones, progressive cognitive decline, neuroimaging with chronic inflammatory changes, and progressive hemispheric atrophy"* (Medicina 2024, **PMID:39597043** — *verify*).

First described by Theodore Rasmussen and colleagues in 1958 (Rasmussen, Olszewski, Lloyd-Smith, *Neurology* 1958).

**Key identifiers:**
| Resource | ID |
|---|---|
| MONDO | `MONDO:0016019` (Rasmussen subacute encephalitis) |
| Orphanet | `ORPHA:511` |
| OMIM | *None* — RE is not a Mendelian disorder, so it has no gene-anchored OMIM entry (this is itself informative for curation) |
| ICD-10 | `G04.8` (other encephalitis) is the closest; often coded under `G40.x` epilepsy in practice |
| ICD-11 | `8A45` region (autoimmune/inflammatory CNS) — closest bucket, no dedicated code |
| MeSH | No dedicated descriptor; "Rasmussen" appears as an entry term under *Encephalitis* / *Epilepsy* |

**Synonyms / alternative names:** Rasmussen syndrome, Rasmussen's encephalitis, chronic focal encephalitis, chronic progressive epilepsia partialis continua of childhood (Kozhevnikov epilepsy is a historically overlapping term), Rasmussen subacute encephalitis.

**Data provenance:** RE knowledge is **disease-level / aggregated** — case series, small cohorts, surgical registries, and consensus statements. There is no large EHR or biobank cohort; the disease is too rare (see §9).

---

## 2. Etiology

**Bottom line: the trigger is unknown; the effector is the immune system.** RE is best understood as a **T-cell–mediated (cell-mediated) autoimmune/neuroinflammatory** process. The 2022 pathogenesis review summarizes five historically-proposed mechanisms — *"virus infection, antibody-mediated degeneration, cell-mediated immunity, microglia-induced degeneration, and genetic mutations"* (**PMID:36189924** — *verify*) — but current consensus places **cytotoxic CD8⁺ T-cell–mediated cell death** at the center.

**Causal factors:**
- **Autoimmune / cell-mediated (primary):** Clonally expanded, antigen-driven cytotoxic CD8⁺ T cells attack neurons and astrocytes (see §6). The autoantigen has never been definitively identified.
- **Antibody-mediated (historical, now largely discredited as primary):** Anti-GluR3 (GluA3, AMPA-receptor subunit) antibodies were reported in the 1990s but **failed replication** ("Absence of antibodies to GluR3 in Rasmussen encephalitis"). Other antibodies (anti-NMDAR GluNε2/NR2A, anti-Munc18) have been reported sporadically but are not diagnostic.
- **Viral (unproven trigger hypothesis):** No consistent pathogen. A "hit-and-run" viral trigger or molecular mimicry is hypothesized; one study found RE tissue shows *relatively lower IFN-β production and enhanced cytotoxic T-cell activation upon herpesvirus infection* (PMC8957159 — *verify*), keeping a viral-trigger idea alive but unproven.

**Risk factors:**
- **Genetic:** No causal Mendelian gene. Whole-exome sequencing has looked for susceptibility contributors — a WES study reported candidate variants in immune-related genes, but nothing replicated or diagnostic (Frontiers in Neuroscience 2021, PMC8523672 — *verify*). RE is **sporadic**; familial recurrence is essentially not seen.
- **Environmental / demographic:** The dominant non-genetic "risk factor" is simply **young age** (childhood, peak ~6 yrs). No confirmed toxin, occupational, or lifestyle exposure. **No sex predilection** in most series.
- **Prior insult:** A subset report a preceding infection/inflammatory event weeks–months before onset, feeding the trigger hypothesis, but this is not consistent.

**Protective factors:** None established (genetic or environmental). This is a section to mark **not available**.

**Gene–environment interactions:** Speculative only — the leading model is that an environmental trigger (?viral) initiates an antigen-specific T-cell response in a susceptible immune background, but no concrete GxE interaction is documented. Mark **hypothesized / not established**.

---

## 3. Phenotypes

RE's phenotype is a **hemispheric syndrome that marches**: it starts focal and escalates into progressive loss of every function that half-brain supports.

| Phenotype | Type | HPO suggestion (OAK-verified) | Onset/course | Frequency |
|---|---|---|---|---|
| **Epilepsia partialis continua (EPC)** | Clinical sign (seizure) | `HP:0012847` Epilepsia partialis continua | Emerges over first 3–5 yr | 37–92% |
| Focal motor seizures | Sign | `HP:0006813` Focal hemiclonic seizure / `HP:0002266` Focal clonic seizure | Presenting feature | Near-universal |
| Drug-resistant focal epilepsy | Sign | `HP:0007359` Focal-onset seizure (*verify*) | Early → persistent | ~100% |
| Status epilepticus | Sign | `HP:0002133` Status epilepticus | Acute stage | Common |
| **Progressive hemiparesis → hemiplegia** | Sign | `HP:0001269` Hemiparesis | Acute→residual | Progressive; ~all |
| Hemianopia | Sign | `HP:0012377` Hemianopia | Later deficit | Subset |
| Aphasia / dysphasia (dominant hemisphere) | Sign | `HP:0002381` Aphasia | Later deficit | If dominant side |
| Progressive cognitive decline | Sign | `HP:0001249` Intellectual disability / cognitive-decline term (*verify*) | Progressive | Common |
| Behavioral changes | Behavioral | (HPO abnormal behavior term) | Variable | Subset |
| **Progressive cerebral hemiatrophy** | Imaging/anatomic | `HP:0100308` Cerebral cortical hemiatrophy | Hallmark, progressive | Defining |

**Characteristics:**
- **Age of onset:** childhood, *"median age of 6 years"*; *"around 10% of the individuals affected by RE are young adults"* (PMID:39597043 — *verify*). Largest series range: 14 months–14 yr.
- **Severity/progression:** progressive and typically severe if untreated; *"Granata et al. found that 30% of the patients were wheelchair-bound within three years of the diagnosis"* (PMID:39597043 — *verify*).
- **EPC definition (quotable, ILAE via review):** *"recurrent focal motor seizures (typically affecting hand and face...) that occur every few seconds minutes for extended periods (days or years)"*.

**QoL impact:** severe — intractable seizures, permanent hemiplegia, hemianopia, language loss (dominant side), cognitive decline; most patients end up with a fixed major neurological disability even after successful seizure control. Formal EQ-5D/SF-36 data are essentially absent (rare disease); mark **limited data**.

---

## 4. Genetic / Molecular Information

**RE is not a genetic disease in the Mendelian sense — this is a firm "not applicable" for most subfields.**

- **Causal genes:** None. No OMIM gene entry.
- **Pathogenic variants:** None established as causal. WES surveys have proposed immune-gene candidates without replication (PMC8523672 — *verify*). No ClinVar/HGMD pathogenic variant set. Somatic mosaicism has been *looked for* (given the strict unilaterality, a somatic brain mutation is an attractive hypothesis) but **not confirmed**.
- **Somatic vs germline:** The striking one-hemisphere restriction has driven a somatic-mutation hypothesis, but no recurrent somatic driver has been demonstrated.
- **Modifier genes / epigenetics / chromosomal abnormalities:** No established data. Mark **not available**.

The molecular action is at the **immune-effector / expression** level, not the germline-variant level — see §6.

---

## 5. Environmental Information

- **Environmental/toxic factors:** None established.
- **Lifestyle factors:** None established (childhood disease).
- **Infectious agents:** No confirmed causative pathogen. The viral-trigger hypothesis persists — candidate/investigated agents historically include herpesviruses (HSV, HHV-6, EBV, CMV), enteroviruses — but PCR/serology are inconsistent and RE is **not** an active viral encephalitis. Best curated as *hypothesized trigger, unconfirmed*. NCBI Taxonomy anchors would be speculative; recommend **omit** rather than over-assert.

---

## 6. Mechanism / Pathophysiology

This is the load-bearing section. The causal chain, upstream → downstream:

**Unknown trigger → antigen-driven CD8⁺ T-cell response → cytotoxic killing of neurons + astrocytes (granzyme B/perforin) → astrocyte loss + microglial activation + neuronophagia → cortical neuronal loss → progressive hemiatrophy → intractable focal epilepsy + progressive hemispheric deficits.**

**Immune effectors (the engine):**
- **Cytotoxic CD8⁺ T lymphocytes** dominate the infiltrate and are **clonally expanded / antigen-driven**: *"Most infiltrating lymphocytes in RE are cytotoxic T-cells, and long-lived clonal populations of cytotoxic T-cells were found in immunohistochemistry analysis of patients with RE"* (PMID:39597043 — *verify*). Large-scale TCR sequencing confirmed pathogenic CD8⁺ expansion (Schneider-Hohendorf et al., *Nat Commun* 2016, PMC4822013 — *verify*), and **peripheral CD8⁺ T-cell expansion correlates with disease severity**.
- **Granzyme B / perforin killing:** infiltrating T cells polarize and release cytotoxic granules onto targets.
- **Astrocytes as a specific target (key mechanistic paper):** Bauer et al. (*Ann Neurol* 2007, **PMID:17503512**) — *"Astrocytic apoptosis and subsequent loss of these cells is a specific feature of RE"*; *"Astrocytes in these tissues showed major histocompatibility complex class I expression"*; and *"granzyme-B(+) lymphocytes were found in close apposition to astrocytes bordering astrocyte-deficient lesions."* Astrocyte loss is now considered a distinctive feature, not just bystander gliosis.
- **Microglia:** activated microglia form nodules and drive neuronophagia. Recent single-cell/immune-microenvironment work (2023–2025) describes a **T-cell trajectory from expansion to exhaustion** over the disease course (J Neuroinflammation 2025, `10.1186/s12974-025-03477-5` — *verify*).
- **Innate/inflammasome:** IL-1 and inflammasome activation contribute — *"activation of inflammatory pathways and release of cytokines such as IL-1 mediated by CD8+ T cells has also been shown in RE"* (PMID:39597043 — *verify*).

**Histopathology (staging correlate):** *"T-lymphocytic infiltrate, reactive astrocytosis, activated microglia, and neuronophagia leading to neuronal loss and cortical atrophy are seen in brain parenchyma"* — with perivascular T-cell cuffing, microglial nodules, and, in late stages, cavitation/gliosis and near-complete neuronal dropout.

**Ontology suggestions:**
- Biological processes (GO): `GO:0001913` T cell mediated cytotoxicity; `GO:0002418` immune response to tumor cell *(no—skip)*; `GO:0006954` inflammatory response; `GO:0006915` apoptotic process; `GO:0001774` microglial cell activation; `GO:0002446` neutrophil-mediated *(skip)*; consider `GO:0050900` leukocyte migration (brain infiltration). **Modifier: INCREASED** for the inflammatory/cytotoxic ones.
- Cell types (CL): `CL:0000909` CD8-positive, alpha-beta memory T cell / `CL:0000625` CD8-positive, alpha-beta T cell; `CL:0000129` microglial cell; `CL:0000127` astrocyte; `CL:0000540` neuron.
- Chemical/protein effectors (CHEBI/PR): granzyme B, perforin, IL-1β, IFN-γ (mostly PR, not CHEBI).

**Molecular profiling:** Transcriptomic and single-cell studies of resected RE cortex exist (recent immune-microenvironment work) but there is no established proteomic/metabolomic/lipidomic signature. Mark advanced-omics as **emerging / limited**.

---

## 7. Anatomical Structures Affected

- **Primary organ:** brain — **one cerebral hemisphere** (`UBERON:0000955` brain; `UBERON:0001869` cerebral cortex; `UBERON:0001870` frontal cortex often earliest).
- **Lateralization:** **unilateral / strikingly asymmetric** — this is the defining anatomical feature. Perisylvian and frontoinsular cortex are often affected early; the process can spread to involve the whole hemisphere, basal ganglia (esp. caudate atrophy), and sometimes the ipsilateral thalamus.
- **Tissue level:** gray matter (cortical neurons) and the astrocytic compartment; secondary white-matter and volume loss.
- **Cell populations targeted:** neurons (`CL:0000540`), astrocytes (`CL:0000127`); effectors are CD8⁺ T cells and microglia.
- **Subcellular (GO CC):** apoptotic machinery (mitochondria `GO:0005739`), MHC-I at plasma membrane (`GO:0042612` MHC class I protein complex).
- **Secondary/system involvement:** motor system (contralateral hemiplegia), visual pathway (hemianopia), language cortex (aphasia if dominant). No systemic organ involvement — RE stays in the CNS.

---

## 8. Temporal Development

Classic **three-stage** natural history (Bien staging):

1. **Prodromal stage** — low seizure frequency, mild hemiparesis; can last months (median ~7 months). *"The first stage is characterized by mild hemiparesis and seizures, generally occurring in a low frequency."*
2. **Acute stage** — the destructive phase: frequent focal motor seizures / **EPC**, progressive hemiparesis→hemiplegia, hemianopia, and (dominant side) aphasia, plus cognitive decline. *"A few months later, RE individuals tend to exhibit a higher frequency of seizures, presenting as focal motor seizures or EPC... RE patients tend to develop worsening focal deficits, such as hemianopia, hemiplegia, behavioral changes, aphasia, and cognitive deficits."* Typically lasts ~8–12 months.
3. **Residual (burnt-out) stage** — seizure frequency often decreases but **fixed, permanent neurological deficits** and hemiatrophy remain. *"The 'residual stage' is the last stage and is characterized by a decrease in the frequency of seizures and persistent neurological deficits."*

- **Onset pattern:** subacute-to-chronic, progressive.
- **Course:** progressive during the acute phase, then plateaus into a stable deficit-laden residual phase (over ~1–3 yr total to reach residual).
- **Duration:** chronic/lifelong disability; the active inflammatory phase is self-limited-ish (burns out) but leaves permanent damage.
- **Critical window:** the acute stage is the intervention window — the whole rationale for early immunotherapy and timely surgery is to stop hemispheric destruction before it completes. Adult-onset cases tend to progress **more slowly**.

---

## 9. Inheritance and Population

- **Incidence:** very rare — *"The incidence of RE is estimated at 1.8 to 2.4 out of every 10 million people annually"* in those under 18 (PMID:39597043; Bien et al. incidence/therapy study, **PMID:23216622** — *verify*). Roughly **~0.18 per 100,000/yr** in children.
- **Prevalence:** no reliable point-prevalence figure — appropriately an **ultra-rare** band. Prevalence-class curation: `BELOW_1_IN_1000000` / `ULTRA_RARE`.
- **Inheritance:** **not heritable** — sporadic, non-Mendelian. All the genetics subfields (penetrance, anticipation, founder effect, consanguinity, carrier frequency) → **not applicable**.
- **Demographics:** primarily children (peak ~6 yr); ~10% adolescent/adult onset. **No confirmed sex predominance** (some series hint at slight variation, not robust). No ethnic/geographic clustering; worldwide distribution.

---

## 10. Diagnostics

Diagnosis is clinical-radiological-pathological, formalized by the **Bien European consensus criteria** (Bien et al., *Brain* 2005;128:454–471, **PMID:15689357**), recently updated by an international modified-Delphi consensus (Stredny et al., *Epilepsia* 2026, `10.1002/epi.70225` — *verify*).

**Bien criteria (two-part):** diagnosis if **all three of Part A** OR **two of three Part B**:
- *Part A:* (1) clinical — focal seizures (± EPC) and unilateral cortical deficit; (2) EEG — unihemispheric slowing ± epileptiform activity, unilateral seizure onset; (3) MRI — unihemispheric focal cortical atrophy plus ≥1 of gray/white-matter T2/FLAIR hyperintensity or caudate head hyperintensity/atrophy.
- *Part B:* (1) EPC or progressive unilateral cortical deficit; (2) progressive unihemispheric atrophy on serial MRI; (3) histopathology — T-cell–dominated encephalitis with activated microglia (classically nodules) and reactive astrogliosis. (Presence of numerous parenchymal macrophages, B cells, plasma cells, or viral inclusions argues *against* RE.)

**Key modalities:**
- **MRI** (RadLex/neuroimaging): serial MRI is the workhorse — progressive unilateral cortical/insular atrophy, T2/FLAIR hyperintensity, caudate atrophy. Recent multi-institutional work compared MRI and pathology staging to hemispherotomy outcome (Child's Nerv Syst 2024, `10.1007/s00381-024-06353-4` — *verify*).
- **EEG / electrophysiology (LOINC/clinical neurophysiology):** unihemispheric slowing, multifocal ipsilateral epileptiform discharges, lateralized seizure onset; EPC often has poor EEG correlate.
- **CSF:** may show mild pleocytosis, oligoclonal bands — nonspecific, supportive.
- **Biopsy/histopathology (SNOMED CT):** confirmatory when imaging is atypical; shows the T-cell/microglial encephalitis pattern above. The consensus trend is to **minimize biopsy** when criteria are otherwise met.
- **Autoantibodies:** anti-GluR3 is **not recommended** (poor specificity/reproducibility); a broader autoimmune-encephalitis antibody panel is done mainly to exclude mimics.
- **Genetic/omics testing:** not diagnostic; used only to exclude genetic mimics (e.g., mitochondrial disease presenting with EPC, like POLG).
- **Differential dx:** other causes of EPC/hemispheric epilepsy — MELAS/POLG mitochondrial disease, hemimegalencephaly/cortical dysplasia, Sturge-Weber, unihemispheric stroke/vasculitis (e.g., primary CNS angiitis), tumor, and other autoimmune encephalitides.

---

## 11. Outcome / Prognosis

- **Mortality:** low disease-specific mortality; deaths relate to status epilepticus or surgical complications rather than the disease directly. Not a classically "fatal" disease — the burden is disability.
- **Morbidity (the real story):** near-inevitable progression to **permanent hemiplegia, hemianopia, cognitive decline, and (dominant hemisphere) aphasia**. Untreated, ~30% wheelchair-bound within 3 years of diagnosis.
- **Seizures:** medically **refractory** — antiseizure drugs rarely control EPC.
- **Surgical outcome (hemispherectomy/hemispherotomy = the definitive seizure cure):** reported **seizure-freedom ~81.5%, 63.6%, 55.6% at 1/5/10 yr** in one cohort; UCLA cohort ~68%/48%/22% at 1/5/10 yr; meta-analytic 5-yr mean ~65% (range 17–100%) (PMC9514735, PMID:32679562 — *verify*). The trade-off is a **guaranteed contralateral hemiplegia and hemianopia** — accepted because that deficit is largely already present or inevitable.
- **Prognostic factors:** shorter preoperative hemiparesis duration predicted **lower** seizure-freedom and more reoperation; **complete disconnection** on postop MRI improved seizure freedom; reoperation for incomplete disconnection was frequently curative. Notably, imaging/pathology **stage did not reliably predict** individual seizure outcome (Child's Nerv Syst 2024 — *verify*).
- **Recovery/plasticity:** young age favors post-hemispherectomy functional (language, ambulation) reorganization — the younger the brain, the better it rewires.

---

## 12. Treatment

Two parallel goals: **(a) immunotherapy** to slow the inflammatory destruction, and **(b) surgery** to actually stop the seizures. Antiseizure meds are supportive but rarely sufficient.

**Immunotherapy (MAXO: `MAXO:0000917` immunosuppressive therapy / `MAXO:0001211` immunomodulation — *verify labels with OAK*):**
- **Acute/first-line:** IV corticosteroids (methylprednisolone) ± IVIg — Stredny consensus: *"Intravenous corticosteroids are recommended as first-line, acute immunotherapy for seizure exacerbations and status epilepticus, with or without the addition of intravenous immunoglobulin."* CHEBI: methylprednisolone `CHEBI:6888`; corticosteroid class NCIT:C2322.
- **Maintenance:** IVIg; **tacrolimus** (calcineurin inhibitor, T-cell targeted) — Bien RCT compared **tacrolimus vs IVIg** (PMID:23216622 — *verify*), both slowing progression; **azathioprine** (Immunomodulation with Azathioprine, *Neurology* 2021 — *verify*).
- **Targeted/experimental biologics (case series):**
  - **Rituximab** (anti-CD20 B-cell depletion) — reduced seizure burden in 16/26 patients across pooled reports (PMC9058598; PMID:19657347 — *verify*).
  - **Natalizumab** (anti-α4-integrin, blocks lymphocyte CNS entry) — response in ~10/32 (Neurology 2013 — *verify*).
  - **Tocilizumab** (anti-IL-6R) — high response rate in refractory status epilepticus (16 patients pooled — *verify*).
  - **Adalimumab** (anti-TNF-α) — complete response ~45% in an 11-patient series; **clinicaltrials:NCT04003922** (adalimumab efficacy/tolerance).
  - Cyclophosphamide has been used as an alternative T-cell–directed agent.
  - *Mechanistic note:* these biologics map cleanly onto the CD8-T-cell/microglia mechanism — good `target_mechanisms` candidates linking drug → the cytotoxic-T-cell node.

**Surgery (definitive, MAXO: `MAXO:0000004` surgical procedure; NCIT hemispherectomy term):**
- **Functional hemispherectomy / hemispherotomy** — disconnects (rather than removes) the diseased hemisphere; **the gold standard** and only reliably seizure-freeing therapy: *"the only gold-standard treatment for this disorder is hemispherectomy."* Timing is the central clinical dilemma — do it early enough to stop cognitive/seizure damage, but the price is fixed hemiplegia/hemianopia.

**Supportive:** antiseizure medications (broad-spectrum), rehabilitation (PT/OT/speech — `MAXO:0000011` physical therapy), and post-surgical neurorehabilitation to exploit plasticity.

**Pharmacogenomics / personalized:** none established for RE specifically (tacrolimus dosing follows general CYP3A5 pharmacogenetics, not RE-specific).

---

## 13. Prevention

- **Primary prevention:** none — trigger unknown, not heritable, no vaccine. Mark **not applicable**.
- **Secondary prevention (early detection):** the closest real "prevention" is **early diagnosis + early immunotherapy** to limit hemispheric atrophy during the critical acute window; and **timely surgery** to prevent further seizure-related cognitive decline. This is disease-modifying, not primary prevention.
- **Tertiary prevention:** manage refractory seizures/status, prevent injury, rehabilitation to limit disability.
- **Screening / genetic counseling / immunization / public health:** not applicable (sporadic ultra-rare, no genetic or infectious basis to screen for).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** RE is essentially a **human-only** clinical entity (`NCBITaxon:9606`). There is **no described naturally-occurring animal equivalent** (no OMIA entry).
- **Comparative biology:** the mechanistic parallel is general CD8⁺ T-cell–mediated CNS autoimmunity, not a species-specific homolog.
- **Transmission/zoonosis:** not applicable — RE is not infectious or transmissible.

Mark this whole section **not applicable / human-specific**.

---

## 15. Model Organisms

RE has historically been **hard to model** — no spontaneous animal disease, no single gene to knock out, and the pathology is driven by *human* T cells against an unknown *human* antigen. The breakthrough was a **humanized mouse model**:

- **Humanized PBMC-engraftment model (flagship):** RE-patient peripheral blood mononuclear cells engrafted into immunodeficient **NSG mice** (NOD-scid IL2Rγ^null^) — the human CD4⁺/CD8⁺ T cells infiltrate the CNS and reproduce RE-like pathology and seizures. *"Numerous granzyme B+CD8+ T lymphocytes were detected in the brains of NSG mice"*, with elevated IFN-γ⁺/IL-17⁺ human T cells vs controls (*JCI* 2018, "Humanized mouse model of Rasmussen's encephalitis supports the immune-mediated hypothesis," PMC5919802 — *verify PMID*). A follow-up showed **blocking immune intrusion into the brain suppresses epilepsy** in this model (*JCI*, article 120444 — *verify*) — strong causal support for the T-cell-effector mechanism and a therapeutic proof-of-concept for CNS-entry blockade (cf. natalizumab).
- **Model type:** mammalian, humanized/xenograft (immune-cell transfer), `NCBITaxon:10090` *Mus musculus* host.
- **Evidence source:** **MODEL_ORGANISM** (with human immune cells → arguably a human-immune xenograft; still tag MODEL_ORGANISM for the mouse readout, and note the humanized design in the explanation).
- **Recapitulation:** reproduces CNS T-cell infiltration, granzyme-B⁺ CD8 cells, and seizures — good for the *immune-effector arm*.
- **Limitations:** does **not** reproduce the strict unilaterality/hemispheric-restriction of human RE, doesn't identify the autoantigen, and depends on donor-patient cells (not a stable genetic line). This is a solid **HUMAN_MODEL_MISMATCH** discussion candidate: the model supports the immune-mediated hypothesis but leaves the hemispheric-restriction and antigen questions unresolved.
- Prior to humanized models, RE relied on ex vivo human resected-tissue immunohistochemistry (Bauer 2007) and TCR-repertoire studies — in vitro / patient-tissue rather than true animal models.

---

## Curation notes & flagged uncertainties

- **MONDO `MONDO:0016019` and ORPHA:511** are solid anchors. No OMIM (non-Mendelian) — expect the entry to lean heavily on `pathophysiology` + `phenotypes` + `treatments`, light on `genetic`.
- **Strongest, most citable primary papers** for evidence blocks: **Bien 2005 European consensus (PMID:15689357)** for definition/criteria/staging; **Bauer 2007 (PMID:17503512)** for astrocyte-target mechanism (I have verbatim abstract quotes above — those should validate cleanly); **Bien 2013 (PMID:23216622)** for incidence + tacrolimus/IVIg. Verify each with `just fetch-reference` before use.
- **PMID:39597043** (Medicina 2024 review) is the best single narrative source but is a *review* — good for framing/synthesis quotes, less ideal than primaries for specific mechanistic claims. The PMID came from a web fetch; **confirm it resolves to the right paper**.
- Two ontology cautions: HPO's only close "encephalitis" leaf is `HP:0002383` *Infectious encephalitis*, which is **wrong for RE** — don't force it; RE's "encephalitis" is better captured through the pathophysiology/imaging phenotypes (`HP:0100308` cerebral cortical hemiatrophy) than a phenotype term. And confirm the focal-seizure and cognitive-decline HP IDs with OAK before committing (I verified EPC, hemiparesis, hemianopia, aphasia, status epilepticus, hemiatrophy directly).
- Good `conforms_to` target: `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance` for the seizure arm — though RE's driver is upstream *immune destruction of one hemisphere*, so the disease-specific chain (CD8/granzyme-B → astrocyte+neuron loss → hemiatrophy → seizures) is the core content and doesn't fully reduce to that module.

**Sources:**
- [Medicina 2024 comprehensive review (PMC11596482)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11596482/)
- [Bien et al. 2005 European consensus, Brain (PMID:15689357)](https://pubmed.ncbi.nlm.nih.gov/15689357/)
- [Bauer et al. 2007, Astrocytes as immunological target (PMID:17503512)](https://pubmed.ncbi.nlm.nih.gov/17503512/)
- [Bien et al. 2013 incidence / tacrolimus vs IVIg (PMID:23216622)](https://pubmed.ncbi.nlm.nih.gov/23216622/)
- [Progress in pathogenesis and therapy of RE 2022 (PMID:36189924)](https://pubmed.ncbi.nlm.nih.gov/36189924/)
- [Stredny et al. 2026 international consensus, Epilepsia](https://onlinelibrary.wiley.com/doi/10.1002/epi.70225)
- [Humanized mouse model of RE, JCI 2018 (PMC5919802)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5919802/)
- [Blocking immune intrusion suppresses epilepsy in RE model, JCI](https://www.jci.org/articles/view/120444)
- [CD8+ T-cell TCR sequencing in RE (PMC4822013)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4822013/)
- [Genetic factors in RE by WES, Front Neurosci 2021 (PMC8523672)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8523672/)
- [Dynamics of brain T-cell populations in RE, J Neuroinflammation 2025](https://link.springer.com/article/10.1186/s12974-025-03477-5)
- [Rituximab in RE (PMC9058598)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9058598/) · [Rituximab case (PMID:19657347)](https://pubmed.ncbi.nlm.nih.gov/19657347/)
- [Natalizumab in RE, Neurology 2013](https://www.neurology.org/doi/10.1212/WNL.0b013e31829c5ceb) · [Azathioprine in RE, Neurology 2021](https://www.neurology.org/doi/10.1212/WNL.0000000000011004)
- [Adalimumab trial NCT04003922](https://clinicaltrials.gov/study/NCT04003922)
- [Hemispherectomy seizure outcomes & reoperation (PMC9514735)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9514735/) · [UCLA surgical series (PMID:32679562)](https://pubmed.ncbi.nlm.nih.gov/32679562/)
- [MRI/pathology vs hemispherotomy outcome 2024](https://link.springer.com/article/10.1007/s00381-024-06353-4)
- [NORD — Rasmussen Encephalitis](https://rarediseases.org/rare-diseases/rasmussen-encephalitis/)

That's the whole tour — one hemisphere, under siege by its own CD8 cells, and the strange mercy that a young brain can hand its whole job to the other half if you disconnect the sick side in time. Want me to go ahead and scaffold the actual `kb/disorders/Rasmussen_Encephalitis.yaml` entry from this (with the Bauer/Bien primaries as the first verified evidence blocks), or keep this as a research doc for now?