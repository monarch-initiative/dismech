---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-06-30T08:11:15.805318'
end_time: '2026-06-30T08:15:53.260495'
duration_seconds: 277.46
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Eosinophilic Fasciitis
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
  - claude-opus-4-8[1m]
  web_search_requests: 5
  num_turns: 12
  total_cost_usd: 2.079501
  session_id: ff614010-2e0a-4c40-bd05-188fe260afb5
  stop_reason: end_turn
citation_count: 13
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Eosinophilic Fasciitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Eosinophilic Fasciitis** covering all of the
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

I have enough material for a thorough report. Writing it now.

---

# Comprehensive Research Report: Eosinophilic Fasciitis (Shulman Syndrome)

**Prepared:** 2026-06-30 · **Target KB entry:** `kb/disorders/Eosinophilic_Fasciitis.yaml` · **MONDO:** `MONDO:0009175`

> **Curation note on evidence:** PMIDs below were gathered from web search and abstract review. Per the dismech SOP, every PMID and snippet must be re-fetched with `just fetch-reference PMID:XXXX` and substring-verified before committing to YAML. I flag a few claims where I could not confirm an exact quotable snippet. EF is **not a Mendelian/genetic disorder**, so several template sections (causal genes, inheritance, variant nomenclature, model organisms) are genuinely sparse or "not applicable" — I say so explicitly rather than inventing content.

---

## 1. Disease Information

**Overview.** Eosinophilic fasciitis (EF) is a rare, acquired, sclerosing/fibrosing connective-tissue disorder marked by **acute-to-subacute inflammation and progressive thickening (fibrosis) of the deep muscular fascia and overlying subcutis**, classically of the limbs. It presents with symmetric edema, erythema and induration of the extremities, evolving into a woody "peau d'orange" (orange-peel) skin texture and a pathognomonic **"groove sign"** (linear depressions along the course of superficial veins, accentuated by limb elevation). It is accompanied in most patients by **peripheral blood eosinophilia, polyclonal hypergammaglobulinemia, and elevated inflammatory markers (ESR/CRP)**. EF is widely regarded as a **scleroderma-like / scleroderma-spectrum** disease, but is distinguished from systemic sclerosis by **sparing of the fingers and face, absence of Raynaud phenomenon, absence of nailfold capillary changes, and lack of visceral organ involvement** (Mazilu et al. 2023, *Int J Mol Sci*, PMID:36768300; original description Shulman 1974).

**Key identifiers.**
- **MONDO:** `MONDO:0009175` (eosinophilic fasciitis) — verified against the local MONDO adapter.
- **Orphanet:** ORPHA:3165 (*flag for verification*; Orphanet page was behind a bot-check at fetch time).
- **ICD-10:** **M35.4** (Diffuse [eosinophilic] fasciitis).
- **ICD-11:** **4A43.0** (Eosinophilic fasciitis), under "Diseases of the immune system with predominant connective-tissue involvement."
- **MeSH:** D005159 "Fasciitis" / EF appears as "Eosinophilic Fasciitis" (Shulman syndrome).
- **OMIM:** None — EF has no OMIM Mendelian entry (not a single-gene disorder).

**Synonyms / alternative names:** Shulman syndrome; Shulman disease; diffuse fasciitis with eosinophilia; diffuse eosinophilic fasciitis; eosinophilic fasciitis with eosinophilia.

**Data provenance.** Knowledge is derived almost entirely from **aggregated disease-level resources and case series/case reports** (EF is too rare for large registries). There is no large EHR cohort; the literature is dominated by single-center series (e.g., a 52-patient Mayo Clinic cohort) and systematic reviews of pooled case reports.

---

## 2. Etiology

**Causal factors.** EF is **idiopathic in the majority of cases**. It is best understood as an **immune-mediated fibrosing reaction** to a triggering insult in a susceptible host, not a genetic disease. Recognized/proposed triggers (each from case reports/series; association ≠ proven causation):

- **Strenuous/unaccustomed physical exertion or trauma** — the single most frequently cited antecedent; reported in ~30–50% of cases preceding onset (Mazilu et al. 2023, PMID:36768300: "Sustained intense physical exercise" is the most prominent trigger).
- **Drugs:** statins (notably **simvastatin/atorvastatin**), phenytoin, ramipril, subcutaneous heparin, and — increasingly important — **immune checkpoint inhibitors (ICIs)** (anti–PD-1/PD-L1 pembrolizumab, nivolumab; anti–CTLA-4 ipilimumab) (PMID:40399177, 2025 review of 30 ICI-EF cases; PMID:32127188 nivolumab-triggered EF).
- **Infections / immune triggers:** *Borrelia burgdorferi* (controversial), and recently **SARS-CoV-2 (COVID-19)** and COVID vaccination (PMID:38292575, EF following COVID-19 case series).
- **Toxic exposures:** historically L-tryptophan (eosinophilia–myalgia syndrome) and toxic-oil syndrome are EF-like but are distinct toxic entities; trichloroethylene and other organic solvents have been implicated.
- **Hematologic / neoplastic association:** EF can be **paraneoplastic**, associated with hematologic disorders (see §9).

**Genetic risk factors.** No established Mendelian gene, GWAS locus, or validated susceptibility allele. Rare familial clustering and isolated HLA associations have been suggested but are not established. **No ClinVar/ClinGen/GWAS-Catalog entries are applicable.**

**Environmental risk factors.** Vigorous exercise/trauma, the drug exposures above, and (debated) infectious triggers. **Age** (peak 30–60 y) and possibly **male sex** in ICI-related disease are demographic risk modifiers.

**Protective factors.** None established (no genetic protective variant or dietary/lifestyle protective factor is documented for this rare disease).

**Gene–environment interactions.** Not characterized. The plausible model is that an environmental/immune trigger (exercise, drug, checkpoint blockade) drives a **Th2/eosinophil-skewed, profibrotic fascial response** in a host of undefined predisposition; no specific GxE data exist (CTD/PheGenI have no EF-specific entries).

---

## 3. Phenotypes

Suggested HPO terms in brackets; frequencies are qualitative pooled estimates from case series — **treat frequency bands as needing their own evidence per the dismech frequency SOP.**

**Cutaneous / fascial (the core phenotype):**
- **Symmetric skin induration / "woody" thickening of extremities** — near-universal; forearms and lower legs most affected, typically sparing hands/feet and face. [HP:0007543 "Subcutaneous tissue induration"? or HP:0100679 "Localized skin lesion"; best fit HP:0100683 not ideal — consider **HP:0001075 "Abnormal skin morphology"** plus a descriptive `preferred_term`; **HP:0011924 "Abnormal skin morphology"** family]. *Onset:* adult; *course:* progressive.
- **"Peau d'orange" / orange-peel skin texture** — characteristic; FREQUENT.
- **"Groove sign"** (depression along superficial veins on limb elevation) — fairly specific, OCCASIONAL–FREQUENT.
- **Erythema and edema of limbs** (early, inflammatory phase) — FREQUENT. [HP:0000964 "Eczema"? no — use **HP:0100749 "Chest pain"? no**; for edema **HP:0000969 "Edema"**].
- **Pruritus** — OCCASIONAL. [HP:0000989 "Pruritus"].
- **Morphea-like plaques / overlap with morphea** — ~29–40% of EF patients have concurrent morphea (PMID:36768300). [HP:0100698 "Morphea"? use **HP:0100699 "Scleroderma"** family].

**Musculoskeletal:**
- **Joint contractures** (especially elbows, wrists, knees, ankles) — common and a major cause of disability; can require surgery. [HP:0001371 "Flexion contracture"]. *Course:* progressive.
- **Arthritis / inflammatory arthritis** — "present in less than half the patients" (PMID:36768300). [HP:0001369 "Arthritis"].
- **Myalgia** — present but "much less common and much milder" than in eosinophilia–myalgia syndrome (PMID:36768300). [HP:0003326 "Myalgia"].
- **Carpal tunnel syndrome** — from fascial compression at the wrist; OCCASIONAL. [HP:0012185 "Carpal tunnel syndrome"].
- **Limited joint mobility / reduced range of motion** — FREQUENT. [HP:0001376 "Limitation of joint mobility"].

**Laboratory abnormalities:**
- **Peripheral blood eosinophilia** — present in ~60–90% (transient, often early, and **not correlated with disease severity**; PMID:36768300). [HP:0001880 "Eosinophilia"].
- **Polyclonal hypergammaglobulinemia** — FREQUENT. [HP:0003237 "Increased circulating IgG level" / HP:0010701 "Abnormal immunoglobulin level"].
- **Elevated ESR / CRP** — FREQUENT. [HP:0003565 "Elevated erythrocyte sedimentation rate"; HP:0011227 "Elevated C-reactive protein level"].
- **Elevated serum aldolase** (with often-normal CK) — a useful marker of fascial/muscle inflammation; OCCASIONAL–FREQUENT. [HP:0008331 "Elevated aldolase"? → use **HP:0003236 "Elevated circulating creatine kinase"** family / aldolase has no precise HP].
- **TARC/CCL17 elevation, IL-5 elevation** — research biomarkers (see §6).

**Systemic / general:** constitutional symptoms (fatigue, low-grade fever, weight loss) are usually mild; **visceral organ involvement is characteristically ABSENT**, which is a key diagnostic discriminator from systemic sclerosis.

**Quality-of-life impact.** Driven mainly by **joint contractures and limb stiffness** → impaired hand function, gait, dressing, and activities of daily living; chronic refractory disease and contractures are the principal QoL detractors. No EF-specific EQ-5D/SF-36 dataset exists; impact is inferred from functional-outcome reporting in case series.

---

## 4. Genetic / Molecular Information

- **Causal genes:** **None.** EF is a non-Mendelian, acquired immune-fibrotic disease; there is no causal gene, pathogenic variant, modifier gene, founder mutation, or chromosomal abnormality established as a cause. ClinVar/HGMD/OMIM contain no EF gene entries.
- **Pathogenic variants / allele frequencies / somatic vs germline:** Not applicable.
- **Epigenetics:** Not specifically characterized in EF (no methylome/ChIP studies dedicated to EF fascia in the literature surveyed).
- **Clonal/somatic context:** The relevant "molecular genetics" of EF is in its **paraneoplastic associations** — clonal hematologic disorders (aplastic anemia/PNH, MDS, T-cell and other lymphomas, myeloproliferative neoplasms) co-occur in up to ~10% of patients (PMID:9283913; PMC4553982). These are clonal diseases *associated with* EF, not the genetic cause of EF.

**Bottom line for KB:** populate genetics sections as "not applicable / acquired immune-mediated disease"; do **not** invent HGNC gene annotations. The gene-relevant content lives in the immunology/cytokine layer (§6), not in a causal-variant layer.

---

## 5. Environmental Information

- **Environmental/occupational factors:** strenuous physical activity and trauma; organic solvents (trichloroethylene), historically adulterated L-tryptophan and toxic rapeseed oil (distinct toxic syndromes that mimic EF).
- **Drug exposures (iatrogenic environment):** statins, phenytoin, heparin, ramipril, and **immune checkpoint inhibitors** (the most clinically important contemporary drug trigger; PMID:40399177, PMID:32127188).
- **Lifestyle factors:** intense/unaccustomed exercise is the dominant lifestyle association; no robust smoking/alcohol/diet links.
- **Infectious agents (triggers, not pathogens of a primary infection):** *Borrelia burgdorferi* (debated; [NCBITaxon:139], **SARS-CoV-2** ([NCBITaxon:2697049]; PMID:38292575), *Mycoplasma*. EF is **not an infectious disease**; these are putative immune triggers.

---

## 6. Mechanism / Pathophysiology

EF is a **Th2-skewed, eosinophil-and-TGF-β-driven fibrosing inflammation centered on the deep fascia**, progressing from an inflammatory phase to fibrosis. Current understanding (idiopathic and ICI-related forms appear to converge mechanistically):

**Causal chain (proposed):**
1. **Trigger** (mechanical/exertional injury, drug/checkpoint blockade, infection) → release of fascial antigens / danger signals.
2. **Type 2 immune activation:** recruitment and **degranulation of eosinophils** in the fascia and elevation of **interleukin-5 (IL-5)** (eosinophil growth/survival factor) and **IL-4** (Th2). The 2023 histological-spectrum study found upregulation of **Th2–M2 markers STAT6 and IL-4** alongside **Th1–M1 markers STAT1 and IFN-γ**, with **CD206⁺ (M2) macrophages predominating** at the muscle–fascia interface (Pehl, Preuße, Allenbach et al. 2023, *Rheumatology*, PMID:36130069).
3. **Eosinophil effector molecules** (major basic protein, eosinophil cationic protein) and cytokines activate **fascial fibroblasts**.
4. **Profibrotic signaling:** **TGF-β1** upregulation drives fibroblast → myofibroblast activation and **excess extracellular-matrix/collagen deposition**; **tissue inhibitors of metalloproteinases (TIMPs)** are elevated, shifting the MMP/TIMP balance toward matrix accumulation (PMID:36768300: "Elevated levels of TIMPs… reported in patients with EF"; "increase in the expression of transforming growth factor-β1").
5. **Fibrosis of deep fascia and septa** → fascial thickening, skin induration, and **joint contractures** (the clinical end-state).

**Distinctive immunopathology.** EF shows **perifascicular pathology with MHC class I and II upregulation** (dermatomyositis-like) **but, importantly, NO type I interferon signature, no hypoxia-mediated process, and no perifascicular fiber atrophy** — distinguishing it mechanistically from idiopathic inflammatory myopathies (PMID:36130069). The eosinophil chemoattractants themselves were **not significantly upregulated** in that study, suggesting eosinophils are recruited/retained by mechanisms beyond classic chemokine gradients.

**ICI-related mechanism.** Checkpoint blockade (loss of PD-1/CTLA-4 restraint) is thought to unleash autoreactive **T cells and a Th2/eosinophil response** in fascia; notably, **sirolimus (mTOR inhibitor) produced remarkable efficacy** in a nivolumab-triggered case, implicating **mTOR/T-cell metabolic signaling** (PMID:32127188).

**Molecular pathways / GO suggestions:**
- TGF-β receptor signaling — **GO:0007179** (transforming growth factor beta receptor signaling pathway), modifier INCREASED.
- IL-5 / type 2 cytokine signaling — **GO:0038043** (interleukin-5–mediated signaling pathway).
- Eosinophil degranulation — **GO:0043308**.
- Extracellular matrix organization / collagen fibril deposition — **GO:0030198** (ECM organization), **GO:0030199** (collagen fibril organization).
- Fibroblast→myofibroblast activation / chronic inflammation — **GO:0006954** (inflammatory response), **GO:0072537** (fibroblast activation).

**Cell types (CL suggestions):**
- **Eosinophil** — **CL:0000771**.
- **Fibroblast / fascial fibroblast → myofibroblast** — **CL:0000057** (fibroblast); myofibroblast **CL:0000186**.
- **M2 / CD206⁺ macrophage** — **CL:0000890** (alternatively activated macrophage).
- **CD4⁺ T helper (Th2) cell** — **CL:0000546** (Th2 cell) / **CL:0000492** (CD4⁺ T cell).
- **Plasma cell** (hypergammaglobulinemia) — **CL:0000786**.

**Chemical entities (CHEBI):** TGF-β1 (protein), **IL-5** (protein); small-molecule/marker context — **collagen**; eosinophil cationic protein (protein). For treatment chemicals see §12.

**Molecular profiling.** No large transcriptomic/proteomic/metabolomic datasets specific to EF were identified (GEO/PRIDE coverage is minimal). The 2023 *Rheumatology* paper (PMID:36130069) is the most granular immunophenotyping to date (immunohistochemistry/transcript markers, not omics-scale). **Serum TARC/CCL17 and IL-5** are the most cited candidate activity biomarkers. This is a genuine **knowledge gap** worth flagging in the entry (`discussions: kind: KNOWLEDGE_GAP`).

---

## 7. Anatomical Structures Affected

- **Primary structure:** **deep (muscular) fascia** — the defining target. [UBERON:0007825 "deep fascia" / UBERON:0011892 "fascia of muscle"; general fascia **UBERON:0007798** "vasculature"? no — **UBERON:0002384 "connective tissue"**, **UBERON:0001134 "skeletal muscle tissue"** at interface].
- **Subcutaneous tissue / septa** — **UBERON:0002072** (skin of body)/ **UBERON:0001013 "adipose tissue"** septa; subcutis **UBERON:0002072**.
- **Skin (dermis, overlying)** — **UBERON:0002067 "dermis"**, **UBERON:0002097 "skin of body"**.
- **Skeletal muscle (perifascial/superficial myositis at the muscle–fascia interface)** — **UBERON:0001134 "skeletal muscle tissue"**.
- **Joints** (secondary — contractures) — **UBERON:0000982 "skeletal joint"**.
- **Peripheral nerve at fascial entrapment sites** (e.g., median nerve → carpal tunnel) — **UBERON:0001021 "nerve"**.

**Body systems:** musculoskeletal/connective-tissue (primary), integumentary (skin), immune/hematologic (eosinophilia, paraneoplastic marrow disease). **Internal viscera (heart, lung, GI, kidney) are characteristically spared.**

**Lateralization:** typically **symmetric and bilateral**, limb-predominant (forearms, lower legs > thighs, upper arms, trunk); **hands, feet, and face usually spared** — a key clinical discriminator.

**Subcellular:** extracellular (ECM/collagen deposition in fascia); no specific organelle pathology. GO cellular component — **GO:0062023 "collagen-containing extracellular matrix"**.

---

## 8. Temporal Development

- **Onset:** Adult-predominant (peak **~30–60 years**); juvenile EF exists and may be more systemic/disabling (PMID:36768300). Onset is often **acute/subacute** — "In 50% of cases, the onset of the disease is sudden" (PMID:36768300) — frequently following an exertional or other trigger.
- **Phases:** (1) early **inflammatory/edematous** phase (painful swelling, erythema, eosinophilia) → (2) **indurative/fibrotic** phase (woody induration, peau d'orange, groove sign) → (3) **fibrotic/contracture** end-stage.
- **Course:** can be **self-limited** in a minority, but is frequently **chronic and relapsing**; a substantial fraction become **corticosteroid-refractory** and develop persistent contractures.
- **Critical window:** **early treatment matters** — combination corticosteroid + methotrexate started early "significantly improves" outcomes and reduces residual fibrosis/contractures (multiple series; PMC12309119 early-EF case report; PMID:36768300). Delay → irreversible fibrosis.
- **Remission:** treatment-induced remission is achievable in most steroid-responsive patients; spontaneous remission occurs but is less common.

---

## 9. Inheritance and Population

- **Epidemiology:** **Rare.** No precise incidence/prevalence figures exist; ~**>300 cases** described historically and fewer than ~3,000 reported worldwide. Largest single cohort is a Mayo Clinic series of **52 patients**. No reliable per-100,000 incidence is published — record as "unknown/rare" in the KB rather than fabricating a rate.
- **Inheritance:** **Not heritable** — sporadic/acquired. No AD/AR/X-linked pattern, penetrance, expressivity, anticipation, founder effect, consanguinity, or carrier-frequency data apply.
- **Sex ratio:** Most series show a **slight male predominance or roughly equal** distribution (varies by series; ICI-related EF showed M:F ≈ 1.3 with median age 57, PMID:40399177).
- **Ethnicity/geography:** No strong ethnic or geographic predilection established; reported worldwide.
- **Key disease associations (not inheritance, but population-level comorbidity):**
  - **Hematologic disorders in up to ~10%** — aplastic anemia / AA-PNH, amegakaryocytic thrombocytopenia, MDS, T-cell and other lymphomas, CLL, myeloproliferative neoplasms, multiple myeloma (PMID:9283913 "frequently associated with hematologic disorders, especially aplastic anemia"; PMC4553982, 4-case AA series). EF with aplastic anemia carries a **poorer prognosis**.
  - **Morphea overlap** in ~29–40% (PMID:36768300).
  - **Solid tumors** (paraneoplastic, less common) and ICI-treated melanoma (PMID:40399177: melanoma was the commonest underlying tumor, 50%).

---

## 10. Diagnostics

EF is a **clinicopathologic diagnosis**; there is **no single confirmatory blood test**.

**Laboratory:**
- **CBC with differential** — peripheral **eosinophilia** (LOINC for eosinophils/100 leukocytes e.g. LOINC:713-8). [HP:0001880].
- **Serum immunoglobulins** — polyclonal hypergammaglobulinemia.
- **ESR / CRP** — elevated.
- **Aldolase** (often elevated with normal/near-normal CK) — sensitive fascial-inflammation marker and treatment-response monitor.
- **ANA/anti-Scl-70/anticentromere** — typically negative/absent (helps exclude systemic sclerosis).
- Candidate biomarkers: **TARC/CCL17, IL-5** (research).

**Imaging:**
- **MRI** is the key noninvasive test: shows **fascial thickening, T2 hyperintensity (edema), and post-contrast fascial enhancement**; recommended where biopsy is not feasible and to guide the biopsy site (PMID:35651918 "MRI Findings of Eosinophilic Fasciitis"; PMID:36768300). [RadLex/imaging].
- Ultrasound and PET have supporting roles.

**Histopathology — gold standard:**
- **Full-thickness incisional biopsy en bloc to and including the deep muscular fascia** (skin → subcutis → fascia → superficial muscle). Findings: **fascial thickening, lymphoplasmacytic infiltrate ± eosinophils, fibrosis, and inflammation at the fascia–muscle interface**. **Tissue eosinophilia is supportive but NOT required** for diagnosis (peripheral and tissue eosinophilia are often transient) (PMID:36768300; PMID:39895266 case lacking classic histology). [SNOMED CT histopathology].

**Diagnostic criteria.** Two proposed criteria sets:
- **Pinal-Fernandez et al. (2014)** criteria — major: symmetric/diffuse swelling-induration-thickening of limb/trunk skin; minor: fascial thickening with inflammation/eosinophil infiltrate on biopsy. Exclusion of systemic sclerosis required.
- **Jinnin et al. (2018, Japanese)** criteria — require **symmetrical plate-like sclerotic lesions** of extremities plus fascial thickening/inflammation, with SSc excluded (PMID:36768300).

**Differential diagnosis (key to exclude):** systemic sclerosis/scleroderma (spares fingers, no Raynaud/nailfold change, no visceral disease in EF), morphea (can overlap), nephrogenic systemic fibrosis, scleromyxedema, eosinophilia–myalgia syndrome, toxic-oil syndrome, hypereosinophilic syndrome, graft-versus-host disease, and chronic Lyme-associated fibrosis.

**Genetic testing:** **Not indicated** (no causal gene). Genetic/marrow work-up (e.g., bone marrow biopsy, cytogenetics, flow for PNH clone) is reserved for **screening the associated hematologic disorders**, not for diagnosing EF itself.

**Screening:** No population screening. Given the ~10% hematologic association, **CBC surveillance for cytopenias** during follow-up is prudent.

---

## 11. Outcome / Prognosis

- **Overall:** EF is **not directly life-threatening**; prognosis is generally **favorable for the fascial/skin disease** when treated early, but **morbidity from joint contractures and residual fibrosis** is significant.
- **Predictors of poor outcome / refractory disease:** **truncal involvement, juvenile onset, presence of morphea-like lesions, dermal sclerosis, delayed treatment, and absence of peripheral eosinophilia** have all been associated with worse response and contracture risk. Early combination immunosuppression predicts better recovery.
- **Mortality:** Disease-specific mortality is low; **excess mortality is driven by the associated hematologic malignancies / aplastic anemia**, which carry a poor prognosis (PMID:9283913; PMC4553982).
- **Complications:** flexion contractures, carpal tunnel syndrome, persistent limb stiffness/disability, secondary functional impairment; rarely, evolution of an associated hematologic neoplasm.
- **Recovery:** many achieve substantial or complete remission on steroids ± methotrexate; a refractory subset needs escalation (§12). Spontaneous remission occurs in a minority.

---

## 12. Treatment

Suggested MAXO/NCIT/CHEBI annotations in brackets. No therapy is FDA-approved specifically for EF; management is from case series/expert consensus.

**First-line — systemic glucocorticoids:**
- **Prednisone (or equivalent) ~0.5–1 mg/kg/day**, tapered over months; pulse IV methylprednisolone for severe disease. Response in the inflammatory phase is often good (PMID:36768300). [MAXO:0000058? use **MAXO:0000302** pharmacotherapy or NCIT:C15986 Pharmacotherapy; **therapeutic_agent:** prednisone **CHEBI:8378**, methylprednisolone **CHEBI:6888**; therapeutic_modality SMALL_MOLECULE; treatment class NCIT:C2322 Corticosteroid].

**Steroid-sparing / second-line (relapse or refractory):**
- **Methotrexate** (15–25 mg/week) — most recommended steroid-sparing agent; early steroid+MTX combination improves outcomes (PMID:36768300). [NCIT:C15986 Pharmacotherapy; **methotrexate CHEBI:44185**].
- **Mycophenolate mofetil** — commonly used alternative. [**CHEBI:8764**].
- **Cyclosporine A** — successful in some refractory cases (PMID:36768300). [**CHEBI:4031**].
- **Azathioprine, hydroxychloroquine, cyclophosphamide** — additional options.

**Biologic / targeted (refractory disease):**
- **Rituximab** (anti-CD20) — reported benefit in refractory EF (clinical-experience review, PMC8021286). [**rituximab NCIT:C1702**; MONOCLONAL_ANTIBODY].
- **Tocilizumab** (anti–IL-6R) — case reports of benefit.
- **Anti–IL-5 agents — reslizumab / mepolizumab** — mechanistically rational (IL-5/eosinophil axis); **reslizumab achieved symptom resolution in refractory EF** (PMID:32913886). [reslizumab/mepolizumab; MONOCLONAL_ANTIBODY].
- **TNF inhibitors (infliximab)** — variable reports.
- **JAK inhibitors** — emerging interest.
- **Sirolimus (mTOR inhibitor)** — "remarkable efficacy" in **nivolumab-induced** EF (PMID:32127188). [**sirolimus CHEBI:9168**].
- **IVIG** — adjunct in refractory/contracture-prone disease.

**Phototherapy:** **UVA1 / PUVA phototherapy** for cutaneous sclerosis. [MAXO/phototherapy].

**Supportive / rehabilitative:**
- **Physical therapy / occupational therapy** — essential to prevent and treat contractures and preserve range of motion. [**MAXO:0000011** physical therapy; NCIT:C15315 Rehabilitation].
- **Surgical release** of established contractures (e.g., fasciectomy, carpal tunnel release) in selected cases. [**MAXO:0000004** surgical procedure].

**ICI-related EF:** withhold/hold the checkpoint inhibitor, treat with corticosteroids ± steroid-sparing agents; consider sirolimus or anti–IL-5 in refractory cases (PMID:40399177).

**Treatment strategy:** Early high-dose steroid + methotrexate is the prevailing initial regimen; escalate to biologics (rituximab, anti–IL-5, tocilizumab) for refractory disease; integrate PT/OT throughout. No randomized trials exist — evidence is observational. **Pharmacogenomics:** standard considerations apply to methotrexate (folate pathway) and azathioprine (**TPMT/NUDT15** genotyping before thiopurines) — general, not EF-specific.

---

## 13. Prevention

- **Primary prevention:** None established for idiopathic EF. For **iatrogenic (ICI-related) EF**, vigilance and early recognition during checkpoint-inhibitor therapy; review of causative drugs (statins, phenytoin, heparin) when EF arises after exposure.
- **Secondary prevention (early detection):** prompt biopsy/MRI and **early immunosuppression** to prevent the inflammatory→fibrotic→contracture transition is the most effective "preventive" lever (prevents irreversible disability).
- **Tertiary prevention:** aggressive **PT/OT and contracture management**; surveillance **CBCs** to catch associated hematologic disease early (~10% risk).
- **Immunization / public-health / counseling:** Not applicable (non-genetic, non-infectious primary disease — no vaccine, no carrier/genetic counseling indicated).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** EF is described essentially **only in humans** ([NCBITaxon:9606 *Homo sapiens*]).
- **Naturally occurring animal disease:** No well-established spontaneous EF analogue is catalogued in **OMIA**. Eosinophilic and fibrosing fasciitis-like conditions occur in veterinary medicine (e.g., eosinophilic dermatitis/panniculitis in dogs/cats), but a direct Shulman-syndrome homologue is not recognized.
- **Comparative biology / orthologs:** Because EF has no causal gene, there are no disease-defining orthologs; the relevant pathways (IL-5, TGF-β1, eosinophil biology) are highly conserved across mammals.
- **Zoonotic potential / cross-species transmission:** Not applicable.

---

## 15. Model Organisms

- **Dedicated animal model:** **None validated.** There is no established knockout/transgenic/induced rodent model that faithfully recapitulates Shulman-syndrome EF. This is a real **knowledge gap** (flag as `discussions: kind: KNOWLEDGE_GAP` in the entry).
- **Surrogate/adjacent systems:** Eosinophil/IL-5 biology and TGF-β–driven dermal/fascial fibrosis are studied in **mouse models of scleroderma/fibrosis** (e.g., bleomycin-induced skin fibrosis) and **IL-5 transgenic / eosinophilia models**, which inform mechanism but **do not reproduce the EF phenotype** specifically. Any such evidence cited should be tagged `evidence_source: MODEL_ORGANISM` and must **not** be the sole support for human phenotype claims (per dismech policy), and ideally flagged `HUMAN_MODEL_MISMATCH` given the absence of a true model.
- **In vitro:** patient fascial **fibroblast cultures** and eosinophil–fibroblast co-culture systems are the main experimental substrate for the IL-5/TGF-β/TIMP findings — tag `IN_VITRO`.

---

## Consolidated Citation List (verify each with `just fetch-reference` before use)

| PMID | Citation (short) | Use |
|------|------------------|-----|
| 36768300 | Mazilu et al. *Int J Mol Sci* 2023;24(3):1982 — "Eosinophilic Fasciitis: Current and Remaining Challenges" | Overview, epi, triggers, IL-5/TGF-β/TIMP, criteria, treatment |
| 36130069 | Pehl, Preuße, Allenbach et al. *Rheumatology (Oxford)* 2023;62(5):2005-2014 | Histological spectrum, MHC I/II, M2 macrophages, no type-I IFN |
| 34969795 | EF (Shulman disease) clinical/imaging/pathological correlation, *PubMed* 2021 | Imaging–path correlation |
| 31130746 | Shulman's disease review, 7 patients (2019) | Case-series clinical features |
| 35651918 | MRI Findings of Eosinophilic Fasciitis (2022) | Diagnostic imaging |
| 40399177 | ICI-related EF: 3 cases + literature review (2025) | Checkpoint-inhibitor EF, demographics |
| 32127188 | Nivolumab-triggered EF, sirolimus efficacy (2020) | mTOR mechanism / ICI treatment |
| 32913886 | Refractory EF treated with reslizumab (2020) | Anti–IL-5 therapy |
| 38292575 | EF following COVID-19, case series of 3 (2024) | Infectious trigger |
| 36455945 | EF without skin sclerosis (2022) | Atypical presentation |
| 39895266 | EF without classic histopathology (2024) | Histology not mandatory |
| 9283913 | Aplastic anemia in EF: immunosuppression & transplant (1997) | Hematologic association |
| (PMC4553982) | Severe aplastic anemia + EF: 4 cases + review | Hematologic association/prognosis |
| (PMC8021286) | Biologic (rituximab) treatment in resistant EF | Refractory therapy |
| (PMC12309119) | Diagnosis & treatment of early EF (case report) | Early-treatment window |

**Sources (web):**
- [Mazilu et al. 2023, MDPI / IJMS](https://www.mdpi.com/1422-0067/24/3/1982) · [PMC mirror](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9916848/)
- [Pehl/Preuße 2023, Rheumatology (PubMed)](https://pubmed.ncbi.nlm.nih.gov/36130069/)
- [ICI-related EF 2025 (PubMed)](https://pubmed.ncbi.nlm.nih.gov/40399177/)
- [Aplastic anemia in EF (PubMed)](https://pubmed.ncbi.nlm.nih.gov/9283913/) · [Severe AA + EF, 4 cases (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4553982/)
- [Reslizumab in refractory EF (PubMed)](https://pubmed.ncbi.nlm.nih.gov/32913886/) · [Sirolimus in nivolumab-EF (PubMed)](https://pubmed.ncbi.nlm.nih.gov/32127188/)
- [MRI findings (PubMed)](https://pubmed.ncbi.nlm.nih.gov/35651918/) · [EF following COVID-19 (PubMed)](https://pubmed.ncbi.nlm.nih.gov/38292575/)
- [Biologic treatment in resistant EF (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8021286/) · [Early EF diagnosis/treatment (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12309119/)
- [Medscape EF overview](https://emedicine.medscape.com/article/329515-overview)

---

### Quick orientation for the KB entry

- **MONDO:0009175** confirmed; ICD-10 **M35.4**, ICD-11 **4A43.0**; **no OMIM** (acquired, non-Mendelian).
- Model the pathophysiology as a **causal chain**: trigger → Th2/eosinophil activation (IL-5↑, IL-4/STAT6) → fibroblast activation via **TGF-β1↑ + TIMP↑/ECM deposition** → fascial fibrosis → contractures. Consider declaring `conforms_to: fibrotic_response#Mesenchymal Cell Activation` (tissue injury → inflammation → fibroblast activation → ECM → organ/limb dysfunction maps cleanly here).
- Leave **genetics/inheritance/model-organism** sections explicitly "not applicable / knowledge gap" rather than fabricating gene or variant annotations.
- Capture the **hematologic-disorder association (~10%)** and **morphea overlap (29–40%)** — good candidates for `comorbidity`/`association_signals` and differentiating notes.

One caution from your own memory bank that applies here: NCIT drug terms often fail `therapeutic_agent` validation, so **prefer CHEBI** for prednisone/methotrexate/MMF/cyclosporine/sirolimus, and reserve NCIT for biologics (rituximab) that lack a clean CHEBI term.