---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-07-31T21:07:46.873935'
end_time: '2026-07-31T21:34:13.974232'
duration_seconds: 1587.1
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Thoracic Aortic Aneurysm
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
  - claude-opus-5[1m]
  web_search_requests: 9
  num_turns: 64
  total_cost_usd: 5.3792912500000005
  session_id: 1dcf0f03-b55f-4c0d-9dc6-fb91a251d5d7
  stop_reason: end_turn
citation_count: 14
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Thoracic Aortic Aneurysm
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Thoracic Aortic Aneurysm** covering all of the
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

# Comprehensive Research Report: Thoracic Aortic Aneurysm (TAA)

**Prepared:** 2026-07-31 · **Target KB entry:** `kb/disorders/Thoracic_Aortic_Aneurysm.yaml` · **Category:** Complex

> **Curation guardrail.** Every PMID below was resolved against the NCBI E-utilities API during this research pass, and ontology IDs were resolved with OAK (`sqlite:obo:hp`, `sqlite:obo:uberon`, `sqlite:obo:cl`, `sqlite:obo:ncit`, `sqlite:obo:mondo`), the HGNC REST API, QuickGO, and OLS4. Text shown in **blockquoted "..." form** was retrieved verbatim from the PubMed abstract via `efetch` and should survive `just validate-references`; text described as *paraphrase* was **not** captured verbatim and must be re-fetched with `just fetch-reference PMID:xxxxx` before being used as an evidence `snippet:`. Two local OAK databases (`sqlite:obo:go`, `sqlite:obo:chebi`) were corrupt in this worktree — GO and CHEBI terms below were verified against QuickGO/OLS4 instead and should be re-checked with `just validate-terms`.

---

## 1. Disease Information

### 1.1 Overview

A **thoracic aortic aneurysm (TAA)** is a permanent, localized dilation of the thoracic aorta — conventionally ≥1.5× the expected normal diameter for the patient's age, sex, and body size — involving the aortic root, ascending aorta, arch, or descending thoracic aorta. TAA is fundamentally a disease of the **aortic media**: progressive loss of vascular smooth muscle cells (SMCs), fragmentation of elastic lamellae, and accumulation of proteoglycan-rich ground substance ("medial degeneration") weaken the wall so that it dilates under cyclic hemodynamic load, and ultimately dissects or ruptures.

TAA differs mechanistically from abdominal aortic aneurysm (AAA). AAA is dominated by atherosclerosis, transmural inflammation, and adventitial/medial proteolysis in a vessel of neural-crest-independent origin; TAA is predominantly a **non-atherosclerotic, non-inflammatory degenerative medial disease** in a segment derived largely from cardiac neural crest and second heart field. This distinction is now supported at the level of human genetics: the Million Veteran Program GWAS explicitly concluded (PMID:37308786):

> "We leverage multiple downstream analytic methods to identify causal TAAD risk genes and cell types and provide human genetic evidence that TAAD is a non-atherosclerotic aortic disorder distinct from other forms of vascular disease."

TAA is characteristically **asymptomatic until catastrophic**. Most aneurysms are found incidentally on imaging performed for another indication; the first clinical manifestation in a substantial minority is acute aortic dissection, rupture, or sudden death.

### 1.2 Nosological structure (important for KB modeling)

"Thoracic aortic aneurysm" is best modeled as an **umbrella/complex entity** that subsumes several mechanistically distinct routes to a shared final common pathway:

| Route | Examples | Share of TAA |
|---|---|---|
| **Syndromic heritable thoracic aortic disease (HTAD)** | Marfan syndrome (FBN1), Loeys-Dietz syndrome (TGFBR1/2, SMAD3, TGFB2/3), vascular Ehlers-Danlos (COL3A1), Shprintzen-Goldberg (SKI), arterial tortuosity syndrome (SLC2A10) | ~5% |
| **Nonsyndromic familial TAAD (FTAAD)** | ACTA2, MYH11, MYLK, PRKG1, LOX, THSD4, LTBP3, MFAP5, FOXE3 | ~15–20% |
| **Bicuspid aortic valve (BAV)-associated aortopathy** | NOTCH1 and largely non-Mendelian | ~10–20% of ascending TAA |
| **Sporadic / degenerative ("age-related medial degeneration")** | Polygenic + hypertension + aging | Majority |
| **Secondary / acquired** | Post-dissection chronic aneurysm, aortitis (giant-cell, Takayasu, IgG4, syphilitic), infective ("mycotic"), traumatic pseudoaneurysm, post-coarctation, post-surgical | Minority |

The proportion attributable to Mendelian disease is substantial. Renard et al. (PMID:30071989) state:

> "Thoracic aortic aneurysms progressively enlarge and predispose to acute aortic dissections. Up to 25% of individuals with thoracic aortic disease harbor an underlying Mendelian pathogenic variant."

### 1.3 Key identifiers

| Resource | Identifier | Label |
|---|---|---|
| **MONDO** | `MONDO:0005396` | thoracic aortic aneurysm ✅ *(OAK-verified)* |
| MONDO (familial) | `MONDO:0019625` | familial thoracic aortic aneurysm and aortic dissection ✅ |
| MONDO (X-linked) | `MONDO:0850095` | X-linked severe syndromic thoracic aortic aneurysm and dissection ✅ |
| MONDO (veterinary) | `MONDO:1012381` | familial thoracic aortic aneurysm, dog ✅ |
| **HPO (phenotype form)** | `HP:0012727` | Thoracic aortic aneurysm ✅ |
| ICD-10-CM | I71.1 (thoracic aortic aneurysm, ruptured); I71.2 (thoracic aortic aneurysm, without rupture); I71.5/I71.6 (thoracoabdominal) | |
| ICD-11 | BD50.2 (aneurysm of thoracic aorta) | |
| MeSH | D017544 "Aortic Aneurysm, Thoracic" | |
| Orphanet | ORPHA:91387 (familial thoracic aortic aneurysm and aortic dissection); ORPHA:558 (Marfan syndrome); ORPHA:60030 (Loeys-Dietz); ORPHA:286 (vascular EDS) | |
| OMIM (FTAAD series) | AAT1 607086; AAT3 (TGFBR2) 608967; AAT4 (MYH11) 132900; AAT6 (ACTA2) 611788; AAT7 (MYLK) 613780; AAT8 (PRKG1) 615436; AAT9 (MFAP5) 616166; AAT10 (LOX) 617168; AAT11 (FOXE3) 617349; AAT12 (MAT2A) 618715 | |
| SNOMED CT | 433068007 (Aneurysm of thoracic aorta) | |

### 1.4 Synonyms and alternative names

Thoracic aortic aneurysm; TAA; ascending thoracic aortic aneurysm (ATAA); aortic root aneurysm; **annuloaortic ectasia** (root-predominant, historic term); descending thoracic aortic aneurysm (DTAA); thoracoabdominal aortic aneurysm (TAAA, when it crosses the diaphragm); thoracic aortic aneurysm and dissection (**TAAD**) when the aneurysm-and-dissection spectrum is treated as one entity; heritable thoracic aortic disease (**HTAD**) for the Mendelian subset; familial thoracic aortic aneurysm and dissection (**FTAAD**); "aortopathy" (in BAV/connective-tissue contexts); historic pathological synonyms **cystic medial necrosis / Erdheim medial degeneration** — the latter formally deprecated in favor of "medial degeneration" by the Society for Cardiovascular Pathology / AECVP consensus (PMID:27031798).

### 1.5 Provenance of the knowledge

Information for this entry is **mixed-source**:
- **Aggregated disease-level resources**: OMIM, Orphanet, ClinGen (gene-disease validity), MONDO, HPO, society guidelines (2022 ACC/AHA PMID:36334952; 2024 EACTS/STS PMID:38416090 / PMID:38408364).
- **Individual-patient / registry data**: International Registry of Acute Aortic Dissection (IRAD; PMID:10685714, PMID:17709637), Olmsted County population cohort (PMID:9851478), Swedish national registers (PMID:17145990), Yale aortic database (PMID:11834007, PMID:16996941), UK Biobank imaging (PMID:34837083), Million Veteran Program EHR + genotype (PMID:37308786), Swedish/Danish administrative pharmacoepidemiology (PMID:29519881).
- **Molecular / tissue-level**: surgical aortic specimens with bulk and single-cell transcriptomics (PMID:33017217), mouse genetics.

---

## 2. Etiology

### 2.1 Disease causal factors

The final common pathway is **medial degeneration → wall weakening → dilation → dissection/rupture**, reached from three broad classes of upstream lesion:

1. **Extracellular matrix (ECM) / microfibril defects** — the SMC cannot be properly anchored to, or signal through, its elastin-microfibril network. `FBN1` (fibrillin-1), `COL3A1` (type III procollagen), `LOX` (lysyl oxidase cross-linking), `EFEMP2`/FBLN4, `MFAP5`, `THSD4`/ADAMTSL6, `LTBP3`, `BGN`, `ELN`.
2. **TGF-β signaling pathway lesions** — `TGFBR1`, `TGFBR2`, `SMAD2`, `SMAD3`, `TGFB2`, `TGFB3`, `SKI`. Paradoxically, most are *loss-of-function* variants yet produce a tissue signature of **increased** TGF-β signaling.
3. **SMC contractile apparatus defects** — `ACTA2` (SMC α-actin), `MYH11` (SM myosin heavy chain), `MYLK` (myosin light chain kinase), `PRKG1` (cGMP-dependent protein kinase I). Guo et al. (PMID:23910461) frame this axis explicitly:

   > "Gene mutations that lead to decreased contraction of vascular smooth-muscle cells (SMCs) can cause inherited thoracic aortic aneurysms and dissections."

Superimposed on all three is **hemodynamic load** (hypertension, abnormal BAV flow jets), **aging** (elastin has essentially no turnover after adolescence; medial degeneration accumulates), and **inflammation** in the aortitis subset.

### 2.2 Risk factors

#### 2.2.1 Genetic risk factors

**A. Mendelian causal genes.** The ClinGen HTAAD Gene Curation Expert Panel evaluated 53 candidate genes and produced the field's reference gene list (PMID:30071989 — *paraphrase*: 53 genes assessed with the ClinGen framework; 11 genes assigned to the definitive + strong categories and designated "HTAAD genes," with the remainder moderate, limited, or disputed/no-evidence). The definitive/strong set:

| Gene | HGNC (dismech lowercase form) | Protein | Mechanism class | Typical syndrome |
|---|---|---|---|---|
| FBN1 | `hgnc:3603` | fibrillin-1 | ECM microfibril | Marfan syndrome |
| TGFBR1 | `hgnc:11772` | TGF-β receptor I | TGF-β | Loeys-Dietz 1 |
| TGFBR2 | `hgnc:11773` | TGF-β receptor II | TGF-β | Loeys-Dietz 2 |
| SMAD3 | `hgnc:6769` | SMAD3 | TGF-β | Loeys-Dietz 3 / aneurysms-osteoarthritis |
| TGFB2 | `hgnc:11768` | TGF-β2 ligand | TGF-β | Loeys-Dietz 4 |
| TGFB3 | `hgnc:11769` | TGF-β3 ligand | TGF-β | Loeys-Dietz 5 |
| COL3A1 | `hgnc:2201` | type III procollagen | ECM | Vascular EDS |
| ACTA2 | `hgnc:130` | SMC α-actin | Contractile | Nonsyndromic FTAAD (most common) |
| MYH11 | `hgnc:7569` | SM myosin heavy chain | Contractile | FTAAD + PDA |
| MYLK | `hgnc:7590` | myosin light chain kinase | Contractile | FTAAD, dissection at small diameter |
| PRKG1 | `hgnc:9414` | PKG-1 | Contractile | FTAAD, early dissection |
| LOX | `hgnc:6664` | lysyl oxidase | ECM cross-linking | FTAAD |
| SLC2A10 | `hgnc:13444` | GLUT10 | ECM/TGF-β | Arterial tortuosity syndrome (AR) |
| SKI | `hgnc:10896` | SKI proto-oncogene | TGF-β co-repressor | Shprintzen-Goldberg |
| EFEMP2 | `hgnc:3219` | fibulin-4 | ECM elastogenesis | Cutis laxa with aortopathy (AR) |

Newer / emerging genes: `THSD4` (`hgnc:25835`), `LTBP3` (`hgnc:6716`), `MFAP5` (`hgnc:29673`), `FOXE3` (`hgnc:3808`), `MAT2A` (`hgnc:6904`), `BGN` (`hgnc:1044`, X-linked Meester-Loeys), `FLNA` (`hgnc:3754`), `NOTCH1` (`hgnc:7881`, BAV-associated).

Gene-specific effect sizes matter clinically: ACTA2 accounts for the largest share of nonsyndromic FTAAD. Guo et al. (PMID:17994018):

> "Here we show that missense mutations in ACTA2 are responsible for 14% of inherited ascending thoracic aortic aneurysms and dissections (TAAD)."

**B. Common-variant / polygenic risk.** The genetic architecture of sporadic TAA is polygenic. The Million Veteran Program GWAS (PMID:37308786):

> "Here, we conducted a genome-wide association study (GWAS) of TAAD, testing ~25 million DNA sequence variants in 8,626 participants with and 453,043 participants without TAAD in the Million Veteran Program, with replication in an independent sample of 4,459 individuals with and 512,463 without TAAD from six cohorts. We identified 21 TAAD risk loci, 17 of which have not been previously reported."
>
> "Our results demonstrate that the genetic architecture of TAAD mirrors that of other complex traits and that it is not solely inherited through protein-altering variants of large effect size."

Deep-learning phenotyping of UK Biobank cardiac MRI further quantified the heritable component of aortic caliber itself (PMID:34837083 — *paraphrase*: deep learning applied to ~4.6 million cardiac images identified 82 loci for ascending and 47 loci for descending thoracic aortic diameter; a polygenic score for ascending aortic diameter was associated with thoracic aortic aneurysm in 385,621 UK Biobank participants).

**C. Chromosomal/structural risk.** **Turner syndrome (45,X)** carries a markedly elevated risk of aortic dilation, BAV, coarctation, and dissection at diameters that would be considered normal in average-sized adults — hence the use of the **aortic size index (ASI, cm/m²)** rather than absolute diameter in this group. 22q11.2 deletion and Williams-Beuren (ELN) produce arteriopathy that is usually stenotic rather than aneurysmal.

**D. Modifier genes.** Formal modifier loci are poorly established. Candidate modifiers of the Marfan aortic phenotype include the polygenic background for aortic diameter (PMID:34837083), sex, and variants affecting TGF-β pathway dosage — the *Tgfb2^+/-* × *Fbn1^C1039G/+* double-mutant worsening reported by Lindsay et al. (PMID:22772368) is a proof-of-principle for TGF-β-pathway gene dosage as a modifier:

> "Mice that harbor both a mutant Marfan syndrome (MFS) allele (Fbn1(C1039G/+)) and Tgfb2 haploinsufficiency show increased TGF-β signaling and phenotypic worsening in association with normalization of TGF-β2 expression and high expression of TGF-β1."

#### 2.2.2 Environmental / non-genetic risk factors

| Factor | Effect | Notes |
|---|---|---|
| **Hypertension** | Strongest modifiable risk factor for dissection | IRAD: history of hypertension predicted dissection at diameter <5.5 cm (OR 2.17, 95% CI 1.03–4.57; PMID:17709637) |
| **Increasing age** | Strong | Degenerative medial change accumulates; Clouse mean age at recognition 75.9 y (women) vs 62.8 y (men) (PMID:9851478) |
| **Male sex** | Higher incidence; female sex confers worse outcome per unit diameter | Olsson: 16.3 vs 9.1 per 100,000/yr (PMID:17145990) |
| **Smoking / COPD** | Increases risk, especially descending TAA | Shared with AAA |
| **Atherosclerosis, dyslipidemia** | Predominantly descending/arch TAA | Less relevant to root/ascending |
| **Bicuspid aortic valve** | ~0.5–2% population prevalence; 8–10× dissection risk vs tricuspid | NOTCH1 (PMID:16025100) plus non-Mendelian |
| **Cocaine, amphetamines, weightlifting/Valsalva** | Acute dissection triggers | dP/dt and BP surges |
| **Pregnancy (3rd trimester/peripartum)** | Dissection trigger in HTAD | Hemodynamic + hormonal medial change |
| **Fluoroquinolone antibiotics** | Associated with aneurysm/dissection | See below |
| **Anabolic steroids** | Case-associated | Weak evidence |
| **Inflammatory aortitis** | Giant cell arteritis, Takayasu, IgG4-RD, rheumatoid, ankylosing spondylitis | Distinct etiologic arm |
| **Infection** | *Treponema pallidum* (syphilitic aortitis), *Salmonella*, *Staphylococcus* (mycotic aneurysm) | Rare in high-income settings |
| **Prior aortic surgery / coarctation repair / deceleration trauma** | Pseudoaneurysm, chronic post-dissection aneurysm | |

**Fluoroquinolones.** Pasternak et al., nationwide Swedish cohort (PMID:29519881):

> "Within the 60 day risk period, the rate of aortic aneurysm or dissection was 1.2 cases per 1000 person years among fluoroquinolone users and 0.7 cases per 1000 person years among amoxicillin users. Fluoroquinolone use was associated with an increased risk of aortic aneurysm or dissection (hazard ratio 1.66 (95% confidence interval 1.12 to 2.46)), with an estimated absolute difference of 82 (95% confidence interval 15 to 181) cases of aortic aneurysm or dissection by 60 days per 1 million treatment episodes."

Mechanistic support comes from a mouse challenge study — LeMaire et al., *JAMA Surgery* 2018 (PMID:30046809, "Effect of Ciprofloxacin on Susceptibility to Aortic Dissection and Rupture in Mice"), which is `MODEL_ORGANISM` evidence and should be tagged as such. FDA and EMA both issued warnings against fluoroquinolone use in patients with, or at risk for, aortic aneurysm. Ciprofloxacin: `CHEBI:100241` ✅.

#### 2.2.3 Protective factors

Evidence here is thin and largely inferential:
- **Blood-pressure control** (β-blockade, ARB, strict BP targets) reduces aortic growth rate — see §12.
- **Statins** — observational association with reduced aneurysm growth; no randomized proof in TAA.
- **Avoidance of isometric/maximal-exertion straining** — guideline-endorsed behavioral protection, not RCT-tested.
- **Genetic protective factors** — none established. Protective common variants at the 21 MVP loci exist by construction (each locus has a protective allele; e.g. loci near *FBN1*, *TCF7L2*, *ULK4*, *LRP1*, *ELN*), but no discrete "protective allele" of clinical utility has been validated.
- **Diabetes mellitus** is inversely associated with *abdominal* aortic aneurysm; the protective association is weaker and less consistent for thoracic disease and should not be curated as established for TAA.

#### 2.2.4 Gene–environment interaction

The clinically dominant G×E interaction is **genotype × hemodynamic stress**:
- In HTAD, hypertension and exertional BP surges accelerate a genetically weakened media; this is precisely why β-blockers/ARBs plus activity restriction are prescribed on the basis of genotype, not diameter alone.
- **Genotype × pregnancy**: vascular EDS and Loeys-Dietz carry disproportionate peripartum dissection/uterine-rupture risk. Pepin et al. (PMID:10706896): *"Complications of pregnancy led to death in 12 of the 81 women who became pregnant."*
- **Genotype × fluoroquinolone**: because ciprofloxacin inhibits ECM homeostasis and increases MMP activity, guideline bodies advise avoidance specifically in HTAD/Marfan patients — an explicitly genotype-conditioned exposure recommendation.
- **BAV × flow**: the eccentric systolic jet of a bicuspid valve imposes an asymmetric wall-shear-stress field on the convexity of the ascending aorta, where the aneurysm preferentially forms — a structural genotype interacting with a purely physical exposure.

---

## 3. Phenotypes

TAA is silent in the large majority of patients until a complication occurs. Phenotype curation should therefore be split into (a) the **structural/imaging phenotype**, (b) **compressive/local symptoms** of a large aneurysm, (c) **acute complication** phenotypes, and (d) **syndrome-associated systemic** phenotypes when a Mendelian cause is present.

### 3.1 Structural / imaging phenotypes (core)

| Phenotype | HPO term | Verified | Onset | Severity | Course | Frequency |
|---|---|---|---|---|---|---|
| Thoracic aortic aneurysm | `HP:0012727` Thoracic aortic aneurysm | ✅ | Adult (sporadic); childhood–young adult (HTAD) | Variable | Progressive | Obligate (definitional) |
| Aortic root aneurysm | `HP:0002616` Aortic root aneurysm | ✅ | Childhood in Marfan/LDS | Variable | Progressive | Very frequent in syndromic HTAD |
| Ascending aortic aneurysm | `HP:0004970` Ascending tubular aorta aneurysm | ✅ | Adult | Variable | Progressive | ~60% of TAA |
| Descending TAA (fusiform) | `HP:0012728` Fusiform descending thoracic aortic aneurysm | ✅ | Older adult | Variable | Progressive | ~30% |
| Descending TAA (saccular) | `HP:0012729` Saccular descending thoracic aortic aneurysm | ✅ | Older adult | Higher rupture risk per size | Progressive | Minority |
| Aortic aneurysm (parent) | `HP:0004942` Aortic aneurysm | ✅ | — | — | — | — |
| Arterial tortuosity | `HP:0005116` Arterial tortuosity | ✅ | Childhood | Marker of severity | Stable/progressive | LDS, ATS; Marfan (severity marker, PMID:26005802) |
| Bicuspid aortic valve | `HP:0001647` Bicuspid aortic valve | ✅ | Congenital | — | Stable | ~10–20% of ascending TAA |
| Mitral valve prolapse | `HP:0001634` Mitral valve prolapse | ✅ | Childhood/adult | Mild–moderate | Progressive | Frequent in Marfan |
| Aortic regurgitation | `HP:0001659` Aortic regurgitation | ✅ | Follows root dilation | Mild–severe | Progressive | Frequent with root aneurysm ≥5 cm |
| Patent ductus arteriosus | `HP:0001643` Patent ductus arteriosus | ✅ | Congenital | — | — | Characteristic of MYH11-TAAD (PMID:16444274) |
| Abdominal aortic aneurysm (concurrent) | `HP:0005112` Abdominal aortic aneurysm | ✅ | Adult | — | Progressive | 24.9% of TAA probands/kindreds had AAA (PMID:16996941) |

### 3.2 Symptoms and clinical signs

| Phenotype | HPO term | Verified | Notes |
|---|---|---|---|
| Chest pain | `HP:0100749` Chest pain | ✅ | Deep, aching, or (in dissection) abrupt tearing/ripping |
| Hoarse voice | `HP:0001609` Hoarse voice | ✅ | Left recurrent laryngeal nerve stretch (Ortner/cardiovocal syndrome) — arch aneurysm |
| Dysphagia | `HP:0002015` Dysphagia | ✅ | Esophageal compression (dysphagia aortica) |
| Hemoptysis | `HP:0002105` Hemoptysis | ✅ | Aorto-bronchial fistula / erosion — herald bleed |
| Syncope | `HP:0001279` Syncope | ✅ | Tamponade, rupture, or arch-vessel malperfusion |
| Sudden death | `HP:0001699` Sudden death | ✅ | Rupture/tamponade; often the presenting event |
| Aortic dissection | `HP:0002647` Aortic dissection | ✅ | The dominant lethal complication |
| Aortic rupture | `HP:0031649` Aortic rupture | ✅ | |
| Hypertension | `HP:0000822` Hypertension | ✅ | Both cause and consequence |
| Ischemic stroke | `HP:0002140` Ischemic stroke | ✅ | Dissection-related malperfusion |
| Transient ischemic attack | `HP:0002326` Transient ischemic attack | ✅ | |

Other classically described but ontology-unverified features to look up before curating: dyspnea (`HP:0002094`), superior vena cava syndrome, Horner syndrome from sympathetic chain compression, cough/stridor from tracheobronchial compression, back/interscapular pain (descending TAA), pulse deficit and new diastolic murmur in dissection, and Cardarelli/Oliver sign (tracheal tug).

Note on the IRAD presentation data (PMID:10685714): *"While sudden onset of severe sharp pain was the single most common presenting complaint, the clinical presentation was diverse. Classic physical findings such as aortic regurgitation and pulse deficit were noted in only 31.6% and 15.1% of patients, respectively."*

### 3.3 Laboratory abnormalities

TAA has **no diagnostic laboratory test**. Investigational and complication-related markers:
- **D-dimer** — highly sensitive but non-specific for acute aortic dissection; used as a rule-out adjunct with the aortic dissection detection risk score. LOINC 48065-7 / 48066-5.
- Soluble ST2, matrix metalloproteinase-9 (MMP-9), TGF-β1, tenascin-C, smooth muscle myosin heavy chain — investigational circulating biomarkers; none guideline-endorsed.
- Complication markers: rising lactate and creatinine (malperfusion), troponin (coronary ostial involvement), falling hemoglobin (rupture), leukocytosis and CRP (aortitis, or the acute-phase response to dissection).
- Aortitis workup: ESR, CRP, IgG4 subclass, RPR/treponemal serology, blood cultures.

### 3.4 Quality of life

- **Pre-repair, asymptomatic**: physical health-related QoL is usually near-normal, but disease-specific anxiety and activity restriction are substantial. Marfan/HTAD cohorts consistently show reduced SF-36 mental component scores, high rates of health anxiety, and career/insurance/sport-participation limitations.
- **After elective repair**: QoL generally returns toward population norms; the David valve-sparing root replacement is favored partly because it avoids lifelong anticoagulation (a major QoL determinant vs. mechanical composite grafts).
- **After acute dissection**: markedly reduced physical and mental QoL, with a high prevalence of PTSD-spectrum symptoms and persistent pain in chronic type B dissection.
- **Family-level burden**: cascade screening obligations, reproductive decision-making, and surveillance for children carry documented psychosocial load in HTAD families.

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes and their functional consequences

**FBN1 (`hgnc:3603`; OMIM 134797) — Marfan syndrome.**
Fibrillin-1 is the structural backbone of extracellular microfibrils and the reservoir that sequesters latent TGF-β–binding-protein (LTBP)-bound TGF-β. Both **haploinsufficiency** and **dominant-negative** mechanisms operate; cysteine-substituting missense variants in cbEGF domains (e.g. C1039G) and premature-termination alleles are the two archetypes. Judge et al. (PMID:15254584) established that haploinsufficiency alone is sufficient. The functional link from matrix to signaling is Neptune et al. (PMID:12598898):

> "We show that mice deficient in fibrillin-1 have marked dysregulation of transforming growth factor-beta (TGF-beta) activation and signaling, resulting in apoptosis in the developing lung."
>
> "These data indicate that matrix sequestration of cytokines is crucial to their regulated activation and signaling and that perturbation of this function can contribute to the pathogenesis of disease."

**ACTA2 (`hgnc:130`) — the most common nonsyndromic FTAAD gene.**
Missense variants act as dominant negatives on actin filament assembly (PMID:17994018):

> "Structural analyses and immunofluorescence of actin filaments in SMCs derived from individuals heterozygous for ACTA2 mutations illustrate that these mutations interfere with actin filament assembly and are predicted to decrease SMC contraction. Aortic tissues from affected individuals showed aortic medial degeneration, focal areas of medial SMC hyperplasia and disarray, and stenotic arteries in the vasa vasorum due to medial SMC proliferation."

The specific recurrent de novo **ACTA2 p.Arg179His** allele produces a distinct, severe multisystem disease — multisystemic smooth muscle dysfunction syndrome (PMID:20734336; *paraphrase*: de novo R179H causes aortic and cerebrovascular disease with fixed dilated pupils, hypotonic bladder, malrotation, gut hypoperistalsis and pulmonary hypertension). This is an important **genotype–phenotype** distinction to model as a subtype.

**MYH11 (`hgnc:7569`) — TAAD with PDA, dominant-negative.** (PMID:16444274):

> "We now demonstrate that the disease is caused by mutations in the MYH11 gene affecting the C-terminal coiled-coil region of the smooth muscle myosin heavy chain, a specific contractile protein of smooth muscle cells (SMC). All individuals bearing the heterozygous mutations, even if asymptomatic, showed marked aortic stiffness. Examination of pathological aortas showed large areas of medial degeneration with very low SMC content."
>
> "Abnormal immunological recognition of SM-MHC and the colocalization of wild-type and mutant rod proteins in SMC, in conjunction with differences in their coimmunoprecipitation capacities, strongly suggest a dominant-negative effect."

**MYLK (`hgnc:7590`) — loss of function; dissection at near-normal diameter.** Clinically the most important "aneurysm-negative dissection" gene (PMID:21055718):

> "Both families demonstrated a similar phenotype characterized by presentation with an acute aortic dissection with little to no enlargement of the aorta."
>
> "The p.R1480X mutation leads to a truncated protein lacking the kinase and calmodulin binding domains, and p.S1759P alters amino acids in the α-helix of the calmodulin binding sequence, which disrupts kinase binding to calmodulin and reduces kinase activity in vitro."

**PRKG1 (`hgnc:9414`) — recurrent gain-of-function p.Arg177Gln.** (PMID:23910461):

> "Exome sequencing of distant relatives affected by thoracic aortic disease and subsequent Sanger sequencing of additional probands with familial thoracic aortic disease identified the same rare variant, PRKG1 c.530G>A (p.Arg177Gln), in four families. This mutation segregated with aortic disease in these families with a combined two-point LOD score of 7.88. The majority of affected individuals presented with acute aortic dissections (63%) at relatively young ages (mean 31 years, range 17-51 years)."
>
> "Although the p.Arg177Gln alteration disrupts binding to the high-affinity cGMP binding site within the regulatory domain, the altered PKG-1 is constitutively active even in the absence of cGMP. The increased PKG-1 activity leads to decreased phosphorylation of the myosin regulatory light chain in fibroblasts and is predicted to cause decreased contraction of vascular SMCs."

**LOX (`hgnc:6664`) — impaired elastin/collagen cross-linking.** Lee et al. (PMID:27432961 — *paraphrase*: whole-genome sequencing in cousins with thoracic aortic disease identified a segregating *LOX* missense allele; a knock-in mouse recapitulated the disease). A short verbatim fragment retrieved: *"Mice homozygous for the human allele died shortly after parturition from ascending aortic aneurysm and spontaneous hemorrhage."* — re-verify before use.

**THSD4 (`hgnc:25835`) / ADAMTSL6 — haploinsufficiency impairing fibrillin-1 assembly.** (PMID:32855533):

> "We identified five functional variants in THSD4 of which two heterozygous variants lead to a premature termination codon. THSD4 encodes ADAMTSL6 (member of the ADAMTS/L superfamily), a microfibril-associated protein that promotes fibrillin-1 matrix assembly. The THSD4 variants studied lead to haploinsufficiency or impaired assembly of fibrillin-1 microfibrils. Thsd4+/- mice showed progressive dilation of the thoracic aorta."

**TGF-β axis genes.** SMAD3 (PMID:21217753):

> "We delineated a new syndrome presenting with aneurysms, dissections and tortuosity throughout the arterial tree in association with mild craniofacial features and skeletal and cutaneous anomalies. In contrast with other aneurysm syndromes, most of these affected individuals presented with early-onset osteoarthritis. We mapped the genetic locus to chromosome 15q22.2-24.2 and show that the disease is caused by mutations in SMAD3. ... SMAD3 mutations lead to increased aortic expression of several key players in the TGF-β pathway, including SMAD3."

TGFBR1/TGFBR2 (PMID:15731757, Loeys-Dietz syndrome). TGFB2 (PMID:22772368) crystallizes the central paradox:

> "Loeys-Dietz syndrome (LDS) associates with a tissue signature for high transforming growth factor (TGF)-β signaling but is often caused by heterozygous mutations in genes encoding positive effectors of TGF-β signaling, including either subunit of the TGF-β receptor or SMAD3, thereby engendering controversy regarding the mechanism of disease."
>
> "Taken together, these data support the hypothesis that compensatory autocrine and/or paracrine events contribute to the pathogenesis of TGF-β-mediated vasculopathies."

**COL3A1 (`hgnc:2201`) — vascular EDS.** Mostly glycine-substitution missense and splice variants in the triple-helical domain (dominant negative); haploinsufficiency (null) alleles are milder. Pepin et al. (PMID:10706896):

> "Complications were rare in childhood; 25 percent of the index patients had a first complication by the age of 20 years, and more than 80 percent had had at least one complication by the age of 40. The calculated median survival of the entire cohort was 48 years. Most deaths resulted from arterial rupture."
>
> "The types of complications were not associated with specific mutations in COL3A1."

**NOTCH1 (`hgnc:7881`) — BAV and aortic valve disease.** Garg et al., *Nature* 2005 (PMID:16025100).

**LTBP3 (`hgnc:6716`)** — Guo et al., *AJHG* 2018 (PMID:29625025, "LTBP3 Pathogenic Variants Predispose Individuals to Thoracic Aortic Aneurysms and Dissections").

### 4.2 Variant classification, type, and frequency

- **Classification**: ACMG/AMP 2015 framework, with ClinGen HTAAD VCEP gene-specific specifications now available for *FBN1* and several others. `PM1` hotspots exist (e.g. *FBN1* cbEGF cysteines; *ACTA2* R179, R258, R118; *PRKG1* R177). ClinVar is the reference submission repository; ~30–40% of rare *FBN1* missense submissions remain VUS.
- **Variant types**: *FBN1* — missense (~60%, mostly cysteine-involving), nonsense/frameshift (~25%), splice (~10%), large deletions (~2–5%, requiring del/dup analysis). *ACTA2*, *PRKG1*, *TGFB2/3*, *TGFBR1/2* — overwhelmingly missense. *MYLK*, *LOX*, *THSD4*, *LTBP3* — enriched for truncating/loss-of-function. *MYH11* — in-frame deletions and missense in the coiled-coil rod domain.
- **Allele frequency**: HTAD pathogenic alleles are individually ultra-rare (gnomAD AF typically 0 or <1×10⁻⁵). This is itself a useful ACMG `PM2` criterion. Conversely, the 21 MVP GWAS loci are common variants of small effect (OR typically 1.05–1.25).
- **Somatic vs germline**: TAA-causing variants are **germline**. Somatic variation is not an established mechanism; however, **de novo** variants are common in severe syndromic HTAD (≈25% of Marfan, and the ACTA2 R179 MSMDS allele is characteristically de novo). Somatic mosaicism has been reported in mildly affected transmitting parents.
- **Functional consequence summary**: loss of function (FBN1 haploinsufficiency, MYLK, LOX, THSD4, LTBP3, TGFBR1/2 kinase-dead receptors); dominant negative (FBN1 cysteine missense, ACTA2, MYH11, COL3A1 glycine substitutions); gain of function (PRKG1 R177Q — constitutively active PKG-1).

### 4.3 Epigenetics

- Gomez et al., *Cardiovasc Res* 2011 (PMID:20829218, "Epigenetic control of vascular smooth muscle cells in Marfan and non-Marfan thoracic aortic aneurysms") — chromatin-level control of the SMC contractile gene program in human aneurysmal aorta.
- Gomez et al., *ATVB* 2013 (PMID:23814118) — Smad2-dependent protease nexin-1 overexpression distinguishes chronic aneurysm from acute dissection in human ascending aorta, with persistent Smad2 activation attributable to chromatin remodeling at the *SMAD2* promoter.
- More recent work implicates HDAC9/TWIST1/*MALAT1* at the chromosome 7p21 locus, SMC-specific enhancer landscape changes, and DNA-methylation differences in BAV- vs TAV-associated aortopathy. Datasets are deposited in GEO; there is no TAA-specific curated methylation resource.

### 4.4 Chromosomal abnormalities

- **45,X Turner syndrome** — BAV, coarctation, aortic dilation, dissection at low absolute diameters. Requires ASI-based thresholds.
- **16p13.1 duplication** — replicated CNV association with both thoracic and abdominal aortic aneurysm and dissection (candidate gene *MYH11*, which lies in the interval).
- Large *FBN1* deletions/duplications detected by MLPA or CMA account for a few percent of Marfan.
- Deletion of 15q21.1 encompassing *FBN1* produces Marfan with additional contiguous-gene features.

---

## 5. Environmental Information

- **Occupational/toxic exposures**: no strong established occupational cause. Historical/experimental interest in **β-aminopropionitrile (BAPN)**, the lathyrogen in *Lathyrus odoratus* (sweet pea), which irreversibly inhibits lysyl oxidase and causes aortic rupture in exposed animals — the direct toxicological counterpart of human *LOX* loss-of-function alleles, and now the standard chemical component of rodent dissection models.
- **Pharmacological exposures**: fluoroquinolones (§2.2.2); cocaine and amphetamines as acute dissection triggers; anabolic-androgenic steroids (case-level); high-dose corticosteroids in Kawasaki/inflammatory contexts (case-level).
- **Lifestyle**: smoking (dose-dependent, strongest for descending TAA), uncontrolled hypertension, heavy isometric exercise/powerlifting, stimulant use. Cardiorespiratory exercise at moderate intensity is *not* prohibited and is guideline-permitted with BP-limited intensity.
- **Infectious agents**: *Treponema pallidum* (NCBITaxon:160) — syphilitic aortitis with saccular ascending/arch aneurysm and coronary ostial stenosis, now rare but a classic. *Salmonella enterica* (NCBITaxon:28901) — the most common cause of mycotic aortic aneurysm, with a predilection for atherosclerotic and diseased aortic segments. *Staphylococcus aureus* (NCBITaxon:1280) — mycotic aneurysm, typically post-bacteremic/endocarditic. *Mycobacterium tuberculosis* (NCBITaxon:1773) — contiguous spread from mediastinal nodes/spine. *Coxiella burnetii*, *Listeria* — rare.

---

## 6. Mechanism / Pathophysiology

### 6.1 The canonical causal chain

This is the chain the dismech module `aortopathy_tgfbeta_dysregulation` already encodes, and a TAA entry should declare `conforms_to` against its nodes:

```
[trigger] Aortic wall ECM defect  OR  SMC contractile-apparatus defect  OR  hemodynamic overload
        ↓
Impaired SMC–matrix mechanosensing / loss of contractile tone
        ↓
TGF-β signaling dysregulation (paradoxical increase in canonical pSmad2/3 and
noncanonical ERK1/2–JNK output; AT1R-dependent component)
        ↓
Medial degeneration: SMC apoptosis + phenotypic modulation, elastic fiber
fragmentation, proteoglycan/glycosaminoglycan pooling, MMP-2/MMP-9 activation
        ↓
Loss of tensile strength and increased wall stress (Laplace: σ ∝ P·r/2t)
        ↓
Progressive aortic dilation (positive-feedback: larger radius → higher wall stress)
        ↓
Intimal tear → aortic dissection  |  Wall failure → aortic rupture
        ↓
Tamponade, malperfusion, exsanguination, death
```

**Suggested conformance targets:** `aortopathy_tgfbeta_dysregulation#TGF-beta Signaling Dysregulation` (canonical hub), plus the medial-degeneration and dilation nodes. Note also the deliberate exclusion of `atherogenesis` — the MVP GWAS explicitly establishes TAAD as non-atherosclerotic (PMID:37308786), so a TAA entry should **not** conform to `atherogenesis`, unlike an AAA or coronary entry. Post-dissection thrombosis of the false lumen may justify a link to `thrombogenesis`.

### 6.2 Molecular pathways

| Pathway | Role | Key nodes |
|---|---|---|
| **TGF-β / SMAD** | Central, and paradoxical | Latent TGF-β sequestered by LTBP–fibrillin-1; matrix failure releases it; canonical TGFBR1/2 → pSMAD2/3 → SMAD4 → nuclear target genes. GO:0007179 ✅ "transforming growth factor beta receptor signaling pathway" |
| **Noncanonical TGF-β (ERK1/2, JNK, p38)** | Aneurysm-driving arm; ERK inhibition rescues LDS mice | MAP kinase cascade |
| **Angiotensin II / AT1R** | Upstream amplifier of TGF-β; therapeutic target | AGTR1 → TGF-β ligand and receptor upregulation |
| **SMC contraction / actomyosin** | Force generation and mechanotransduction | ACTA2–MYH11 cross-bridge cycling; MYLK phosphorylates RLC; PRKG1/PKG-1 and MYPT1 dephosphorylate it. GO:0006939 ✅ "smooth muscle contraction" |
| **NO–cGMP–PKG** | Relaxation arm; PRKG1 GoF locks it on | sGC → cGMP → PKG-1 |
| **ECM assembly and cross-linking** | Structural | GO:0030198 ✅ "extracellular matrix organization"; GO:0030199 ✅ "collagen fibril organization"; GO:0048251 ✅ "elastic fiber assembly"; GO:0004720 ✅ "protein-lysine 6-oxidase activity" (LOX) |
| **MMP / TIMP proteolysis** | Executes matrix destruction | MMP-2, MMP-9, MMP-12; TIMP-1/2/3 |
| **Integrin / focal adhesion mechanotransduction** | Links matrix stiffness to SMC phenotype | αvβ3, α5β1, FAK, RhoA/ROCK, YAP/TAZ |
| **Inflammation** | Secondary in degenerative TAA; primary in aortitis | GO:0006954 ✅ "inflammatory response"; IL-6, IL-1β, NF-κB |
| **Oxidative stress / mitochondrial dysfunction** | Amplifier | GO:0006979 ✅ "response to oxidative stress"; NOX enzymes, uncoupled eNOS |
| **Aortic developmental patterning** | Explains segmental susceptibility | GO:0035904 ✅ "aorta development"; cardiac neural crest vs second heart field lineage boundary at the sinotubular junction |
| **SMC migration/phenotype switching** | Modulated/synthetic SMC | GO:0014909 ✅ "smooth muscle cell migration" |

### 6.3 The TGF-β paradox — and why the KB should model it as a hypothesis, not a settled fact

The founding observation is that *Fbn1*-deficient tissue shows excess TGF-β activity, and TGF-β antagonism rescues the phenotype. Habashi et al. (PMID:16601194):

> "We show that aortic aneurysm in a mouse model of MFS is associated with increased TGF-beta signaling and can be prevented by TGF-beta antagonists such as TGF-beta-neutralizing antibody or the angiotensin II type 1 receptor (AT1) blocker, losartan. AT1 antagonism also partially reversed noncardiovascular manifestations of MFS, including impaired alveolar septation."

But the direction of the TGF-β effect is **time- and context-dependent**. Cook et al. (PMID:25614286, *paraphrase* with verbatim fragments):

> "Aneurysm growth, media degeneration, aortic levels of phosphorylated Erk and Smad proteins and the average survival of Fbn1(mgR/mgR) mice were compared after a ≈3-month-long treatment with placebo and either the AT1r antagonist losartan or the TGFβ-neutralizing antibody 1D11."
>
> "TGFβ neutralization either exacerbated or mitigated TAA formation depending on whether treatment was initiated before or after aneurysm formation."

Combined with the *loss-of-function* nature of TGFBR1/2, SMAD3, and TGFB2/3 variants (PMID:22772368), the field's current reading is that early TGF-β signaling is **protective/homeostatic** for the aortic media, and the late excess seen in diseased tissue is a **compensatory, and then maladaptive, response**. **Curation guidance:** model the "increased TGF-β signaling drives aneurysm" edge inside a `mechanistic_hypotheses` group (status `ALTERNATIVE` or `EMERGING`) rather than asserting it as canonical, and attach a `KNOWLEDGE_GAP` or `HUMAN_MODEL_MISMATCH` discussion — the losartan mouse result (PMID:16601194) did not translate into superiority over β-blockade in humans (PMID:25405392), which is a textbook model-to-human mismatch.

### 6.4 Cellular processes and cell types

| Cell type | CL term | Verified | Role |
|---|---|---|---|
| Vascular smooth muscle cell | `CL:0000359` vascular associated smooth muscle cell | ✅ | Central effector; apoptosis, phenotypic modulation, loss of contractility |
| Smooth muscle cell (generic) | `CL:0000192` smooth muscle cell | ✅ | |
| Vascular endothelial cell | `CL:0002139` endothelial cell of vascular tree | ✅ | Mechanosensing of wall shear stress; endothelial dysfunction; intimal tear origin |
| Fibroblast (adventitial) | `CL:0000057` fibroblast | ✅ | Adventitial remodeling, myofibroblast transition, collagen deposition |
| Macrophage | `CL:0000235` macrophage | ✅ | MMP source; expanded in aneurysm tissue |
| T cell | `CL:0000084` T cell | ✅ | Expanded in ATAA per scRNA-seq (PMID:33017217) |

Key cellular processes: SMC apoptosis and anoikis; SMC **phenotypic modulation** from contractile (ACTA2, MYH11, CNN1, TAGLN high) to synthetic/modulated/fibromyocyte states; impaired autophagy; senescence; mitochondrial dysfunction; adventitial neovascularization and vasa vasorum stenosis (documented in ACTA2 aortas — PMID:17994018).

### 6.5 Tissue-damage mechanisms

- **Elastic fiber fragmentation** — the diagnostic histological lesion, from mechanical fatigue on a non-renewing elastin scaffold plus elastolysis.
- **Mucoid extracellular matrix accumulation** — pooling of proteoglycans/GAGs (versican, aggrecan) between lamellar units; the modern consensus term replacing "cystic medial necrosis" (PMID:27031798). GAG pooling raises local Donnan swelling pressure and delaminates the media — a mechanically distinct route to intramural tear.
- **SMC dropout** — Zhu et al. described *"large areas of medial degeneration with very low SMC content"* in MYH11 aortas (PMID:16444274).
- **Laplace positive feedback** — wall stress rises with radius and falls with thickness; dilation therefore self-accelerates, which is why growth rate increases with size.
- **Delamination/dissection** — an intimal tear admits pressurized blood into the outer third of the media, creating a false lumen that propagates antegrade/retrograde.

### 6.6 Protein dysfunction

- **Fibrillin-1** — misfolded cbEGF domains from cysteine substitutions disrupt calcium binding and domain packing, producing protease-susceptible, poorly polymerizing monomers that poison the wild-type microfibril (dominant negative); nulls simply halve microfibril output. UniProt P35555; PDB entries for cbEGF tandem repeats.
- **SMC α-actin (ACTA2)** — mutant monomers incorporate into and destabilize filaments; R179H additionally perturbs the actin/myosin interface across all smooth muscle beds. UniProt P62736.
- **SM-MHC (MYH11)** — coiled-coil rod mutations impair dimerization and thick-filament assembly. UniProt P35749.
- **MLCK (MYLK)** — truncation removes the kinase and CaM-binding domains; S1759P disrupts CaM binding and reduces kinase activity (PMID:21055718). UniProt Q15746.
- **PKG-1 (PRKG1)** — R177Q abolishes high-affinity cGMP binding *and* renders the kinase constitutively active, a genuine gain of function (PMID:23910461). UniProt Q13976.
- **Lysyl oxidase (LOX)** — loss of copper-dependent amine oxidase activity → failure of lysine-derived cross-links (desmosine/isodesmosine in elastin, pyridinoline in collagen). UniProt P28300.
- **TGFBR1/2** — kinase-domain missense variants that are catalytically dead yet dominantly interfere; the tissue nonetheless shows high pSMAD2 (the paradox). UniProt P36897 / P37173.

### 6.7 Metabolic and biochemical changes

- Reduced elastin cross-link density (desmosine/isodesmosine); increased urinary desmosine as an elastolysis marker.
- Copper is the LOX cofactor — copper deficiency phenocopies *LOX* loss (relevant to the avian aortic-rupture models, §14/15).
- Homocysteine elevation (homocystinuria, *CBS* deficiency) interferes with cross-linking and is a Marfan phenocopy with aortic dilation and lens dislocation — an important differential.
- scRNA-seq of human ATAA highlighted an energy-metabolism lesion (PMID:33017217): *"Differential gene expression data suggested the presence of extensive mitochondrial dysfunction in ATAA tissues."*

### 6.8 Immune involvement

In *degenerative and heritable* TAA, inflammation is a **secondary amplifier**, not the initiating event — historically the field's reason for calling it "non-inflammatory degenerative" disease. However, single-cell data show a real immune shift (PMID:33017217):

> "In general, ATAA tissues had fewer nonimmune cells and more immune cells, especially T lymphocytes, than control tissues did."

In *aortitis* (giant-cell arteritis, Takayasu, IgG4-related disease, syphilis, ANCA-associated, relapsing polychondritis, Behçet), immunity is **primary**: granulomatous or lymphoplasmacytic transmural infiltration destroys the media and produces aneurysm. This subset responds to immunosuppression (glucocorticoids, tocilizumab, rituximab) and should be a separately modeled etiologic arm.

### 6.9 Molecular profiling

**Transcriptomics.** Consistent findings across bulk and single-cell studies: downregulation of the contractile SMC gene program (*ACTA2*, *MYH11*, *CNN1*, *TAGLN*, *MYOCD*); upregulation of synthetic/ECM-remodeling genes; interferon and inflammatory signatures in dissection specimens. The landmark human scRNA-seq resource is PMID:33017217:

> "We identified 11 major cell types in human ascending aortic tissue; the high-resolution reclustering of these cells further divided them into 40 subtypes. Multiple subtypes were observed for smooth muscle cells, macrophages, and T lymphocytes, suggesting that these cells have multiple functional populations in the aortic wall."

with an integrative GWAS/Hi-C finding:

> "integrative analysis of our single-cell RNA sequencing data with public genome-wide association study data and promoter capture Hi-C data suggested that the erythroblast transformation-specific related gene(ERG) exerts an important role in maintaining normal aortic wall function."

Additional single-cell resources: "Dissecting the Heterogeneity of Human Thoracic Aortic Aneurysms Using Single-Cell Transcriptomics" (*ATVB* 2022) and the *Il1rn⁺/Trem1⁺* macrophage subpopulation study (*Cell Discovery* 2021) — obtain PMIDs before citing.

**Proteomics.** Aortic-wall proteomics reproducibly shows reduced contractile and cytoskeletal proteins with increased ECM-remodeling and stress-response proteins. Plasma proteomic candidates (MMP-9, TIMP-1, TGF-β1, tenascin-C, sST2, thrombospondin) have not achieved clinical validation. PRIDE/ProteomeXchange hold the deposited datasets.

**Metabolomics/lipidomics.** Small human studies report altered acylcarnitines, branched-chain amino acids, and sphingolipids in TAA vs control aorta and plasma. Nothing clinically actionable; MetaboLights/Metabolomics Workbench are the repositories.

**Spatial transcriptomics and multi-omics.** Recent work maps the intramural gradient of SMC phenotype from intima to adventitia and localizes GAG-pooling foci. A 2023 multi-omic study of familial TAAD implicated impaired calcium transport as a dissection-predisposing lesion (PMC10607035 — retrieve PMID before citing).

**Functional genomics.** No large TAA-specific CRISPR screen exists. Patient-derived **iPSC-derived vascular SMCs** are the dominant functional platform, and importantly show **lineage-specific** vulnerability: neural-crest-derived iPSC-SMCs (the lineage of the ascending aorta/root) reproduce the Marfan/LDS contractile and ECM defect while lateral-plate-mesoderm-derived SMCs do not — the leading cell-autonomous explanation for why disease is segment-restricted.

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

**Primary:** the thoracic aorta. `UBERON:0001515` thoracic aorta ✅. Segment-specific:

| Segment | UBERON | Verified | Notes |
|---|---|---|---|
| Aortic root / sinuses of Valsalva | `UBERON:0003707` sinus of Valsalva | ✅ | Marfan, LDS, BAV-root phenotype; "annuloaortic ectasia" |
| Ascending aorta | `UBERON:0001496` ascending aorta | ✅ | Most common TAA site (~60%) |
| Aortic arch | `UBERON:0001508` arch of aorta | ✅ | ~10%; recurrent laryngeal/tracheal compression |
| Descending thoracic aorta | `UBERON:0001515` thoracic aorta | ✅ | ~30%; smoking/atherosclerosis-associated |
| Aorta (parent) | `UBERON:0000947` aorta | ✅ | |
| Aortic valve | `UBERON:0002137` aortic valve | ✅ | BAV; secondary regurgitation from annular dilation |

**Secondary organ involvement (complications):**
- **Heart** — aortic regurgitation → LV volume overload and heart failure; hemopericardium/tamponade; coronary ostial dissection → myocardial infarction.
- **Brain** — malperfusion stroke, and in *ACTA2*/HTAD, independent intracranial arteriopathy (moyamoya-like, intracranial aneurysm).
- **Kidney, gut, spinal cord, limbs** — branch-vessel malperfusion in dissection; paraplegia from artery-of-Adamkiewicz compromise (both from dissection and as a TEVAR/open-repair complication).
- **Lung/airway/esophagus/laryngeal nerve** — compression; aorto-bronchial and aorto-esophageal fistula.
- **Vertebrae/sternum** — erosion by chronic saccular aneurysm.

**Body systems:** cardiovascular (primary); respiratory, nervous, digestive, renal, musculoskeletal (secondary). In syndromic HTAD, add ocular (ectopia lentis in Marfan), skeletal (dolichostenomelia, pectus, scoliosis), integumentary (striae, translucent skin), and craniofacial (hypertelorism, bifid uvula in LDS).

### 7.2 Tissue and cell level

- **Tunica media** — the principal site. `UBERON:0003618` aorta tunica media ✅ (parent `UBERON:0002522` tunica media ✅). Aortic SMC tissue: `UBERON:0004178` aorta smooth muscle tissue ✅.
- **Tunica intima** — endothelial monolayer; origin of the entry tear in dissection.
- **Tunica adventitia** — collagen-rich; the last barrier before free rupture; contains the vasa vasorum, whose stenosis in ACTA2 disease contributes to medial ischemia.
- **Elastic lamellae** — ~55–60 lamellar units in the human ascending aorta; fragmentation is the diagnostic lesion.
- **Cell populations** — see §6.4 (CL terms verified).

### 7.3 Subcellular level (GO Cellular Component)

- **Extracellular matrix / microfibril** — GO:0031012 (extracellular matrix), GO:0001527 (microfibril) — *verify with OAK*.
- **Contractile fiber / stress fiber / myofilament** — GO:0001725 (stress fiber), GO:0043292 (contractile fiber) — *verify*.
- **Focal adhesion** — GO:0005925 — *verify*.
- **Mitochondrion** — GO:0005739 — implicated by PMID:33017217.
- **Endoplasmic reticulum** — procollagen III misfolding and ER stress in vascular EDS.
- **Nucleus** — SMAD2/3 nuclear translocation.

### 7.4 Localization and laterality

The aorta is a midline unpaired structure — **laterality is not applicable** in the usual sense. Two spatial patterns matter instead:

1. **Longitudinal segmental restriction.** Disease respects the embryonic SMC-lineage boundary at the sinotubular junction (cardiac neural crest above, second heart field/somitic mesoderm below), which is why *FBN1*, *TGFBR1/2*, and *ACTA2* disease is root/ascending-predominant while *MYH11* and atherosclerotic disease often favor the descending segment.
2. **Circumferential asymmetry.** In BAV aortopathy, dilation is characteristically greatest on the **greater curvature (convexity)** of the ascending aorta, matching the eccentric flow jet — an asymmetric, not bilateral, lesion.

Aneurysm shape should be curated too: **fusiform** (circumferential, degenerative/heritable) vs **saccular** (eccentric outpouching; higher rupture risk per size; typical of mycotic, post-traumatic, and penetrating-ulcer aneurysms).

---

## 8. Temporal Development

### 8.1 Onset

| Context | Typical age of aneurysm detection | Onset pattern |
|---|---|---|
| Sporadic/degenerative | 60s–70s (Clouse: women 75.9 y, men 62.8 y — PMID:9851478) | Insidious, asymptomatic |
| Familial nonsyndromic TAAD | ~58 y (PMID:16996941) | Insidious |
| Marfan syndrome | Childhood–young adulthood (~27 y at presentation, PMID:16996941) | Insidious, congenital substrate |
| Loeys-Dietz syndrome | Childhood, often <10 y | Aggressive, early |
| ACTA2 R179 (MSMDS) | Infancy | Congenital multisystem |
| Vascular EDS | Complications from adolescence; 25% by age 20, >80% by age 40 (PMID:10706896) | Episodic catastrophes |
| BAV aortopathy | 40s–60s | Insidious |

Albornoz et al. quantified the familial-vs-sporadic-vs-Marfan age gradient (PMID:16996941):

> "The familial TAA group was significantly younger than the sporadic group (p < 0.0001), but not as young as the MFS group (p < 0.0001) (mean ages, 58.2 versus 65.7 versus 27.4 years)."

### 8.2 Progression

**Stages (a practical clinical staging, no formal consensus system exists):**

| Stage | Definition | Management |
|---|---|---|
| At-risk / genotype-positive, phenotype-negative | Pathogenic HTAD variant, normal aortic dimensions | Surveillance, BP control, activity counseling |
| Early dilation | Diameter above normal but below threshold (e.g. root Z 2–3, or 4.0–4.4 cm) | Annual imaging, medical therapy |
| Intermediate aneurysm | 4.5–5.4 cm (or genotype-specific equivalent) | 6–12-month imaging; surgical planning |
| Surgical-threshold aneurysm | ≥5.5 cm sporadic; ≥5.0 cm Marfan/experienced center; ≥4.0–4.5 cm in high-risk genotypes; rapid growth; symptoms; concomitant cardiac surgery | Elective repair |
| Acute complication | Dissection (Stanford A/B; DeBakey I/II/III), intramural hematoma, penetrating atherosclerotic ulcer, contained or free rupture | Emergency |
| Chronic post-dissection | Residual false lumen aneurysmal degeneration | Lifelong surveillance; reintervention in 20–40% |

**Growth rate.** Slow and nonlinear — it accelerates with diameter. Davies et al. (PMID:11834007): *"The aorta grew at a mean of 0.10 cm per year."* Albornoz et al. (PMID:16996941):

> "Aortic growth rate was highest for the familial group (0.21 cm/y), intermediate for the sporadic group (0.16 cm/y), and lowest for the Marfan group (0.1 cm/y; p < 0.01)."
>
> "Familial TAAs tend to grow at a higher rate, exemplifying a more aggressive clinical entity."

(The apparently low Marfan rate reflects treatment and early surgical referral, not benign biology.)

**Event rates by size.** Davies et al. (PMID:11834007):

> "For aneurysms greater than 6 cm in diameter, rupture occurred at 3.7% per year, rupture or dissection at 6.9% per year, death at 11.8%, and death, rupture, or dissection at 15.6% per year. At size greater than 6.0 cm, the odds ratio for rupture was increased 27-fold (p = 0.0023)."

Clouse et al. (PMID:9851478):

> "The cumulative risk of rupture was 20% after 5 years. Seventy-nine percent of ruptures occurred in women (P= .01). The 5-year risk of rupture as a function of aneurysm size at recognition was 0% for aneurysms less than 4 cm in diameter, 16% (95% CI, 4%-28%) for those 4 to 5.9 cm, and 31% (95% CI, 5%-56%) for aneurysms 6 cm or more."

**The critical caveat — size is a poor predictor of dissection.** Pape et al., IRAD (PMID:17709637):

> "Maximum aortic diameters averaged 5.3 cm; 349 (59%) patients had aortic diameters <5.5 cm and 229 (40%) patients had aortic diameters <5.0 cm."
>
> "The majority of patients with acute type A acute aortic dissection present with aortic diameters <5.5 cm and thus do not fall within current guidelines for elective aneurysm surgery. Methods other than size measurement of the ascending aorta are needed to identify patients at risk for dissection."

Also from that paper: *"Marfan syndrome patients were more likely to dissect at larger diameters (odds ratio, 14.3; 95% confidence interval, 2.7 to 100; P=0.002)"* — i.e., Marfan patients dissect at larger absolute diameters than the sporadic population, which is one reason the guideline threshold for Marfan is set on Z-score/relative rather than purely absolute grounds.

**Course pattern:** chronic and **progressive** with **episodic catastrophic** punctuation. There is **no spontaneous remission** — an aneurysm does not regress. The only "remission" is treatment-induced (surgical replacement of the diseased segment). Disease duration is **lifelong**; even after repair, the residual native aorta remains at risk, and reoperation is common (Olsson: *"The cumulative incidence of thoracic aortic reoperations was 7.8% at 10 years."* — PMID:17145990).

**Critical intervention windows:** (i) presymptomatic detection via family screening or incidental imaging; (ii) the window between reaching the surgical threshold and dissecting — the whole rationale for elective repair; (iii) pre-pregnancy counseling and root repair in HTAD women; (iv) the first 48 hours of acute type A dissection, where mortality is ~1–2% per hour untreated.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

| Measure | Value | Source |
|---|---|---|
| Incidence (Olmsted County, USA, 1980–1994) | **10.4 per 100,000 person-years** (95% CI 8.6–12.2) | PMID:9851478 — *"more than 3-fold higher than the rate from 1951 to 1980"* |
| Incidence (Sweden, national, to 2002) | **16.3 per 100,000/yr men; 9.1 per 100,000/yr women** | PMID:17145990 — *"Incidence of thoracic aortic disease rose by 52% in men and by 28% in women"* |
| Acute aortic dissection incidence | ~3–6 per 100,000/yr | IRAD-era estimates |
| Population prevalence of ascending aortic dilation | ~0.5–1% of adults by imaging | UK Biobank / population CT-echo studies |
| BAV prevalence | 0.5–2% of population | Contributes ~10–20% of ascending TAA |
| Fraction with a Mendelian cause | **up to 25%** | PMID:30071989 |
| Fraction of non-Marfan TAA with a family history | **21.5%** | PMID:16996941 — *"An inherited pattern for TAA was present in 21.5% of non-MFS patients."* |
| Marfan syndrome prevalence | ~1 in 5,000 (2–3 per 10,000; Orphanet class 1–5/10,000) | ORPHA:558 |
| Loeys-Dietz prevalence | <1 in 100,000 (ultra-rare) | ORPHA:60030 |
| Vascular EDS prevalence | ~1 in 50,000–200,000 | ORPHA:286 |

For dismech `Prevalence` records, model these with explicit `measure_type` — the Olmsted and Swedish figures are `ANNUAL_INCIDENCE`, not prevalence, and should carry `prevalence_class: BAND_1_9_PER_100000` with `rate_per_100000` of 10.4 / 16.3 / 9.1 respectively. Do **not** compare them to Orphanet point-prevalence classes.

Olsson et al. also documented rising ascertainment and improving outcomes (PMID:17145990):

> "The prevalence and incidence of thoracic aortic disease was higher than previously reported and increasing. The annual number of operations increased substantially. Surgical (30-day) and long-term survival improved significantly over time to form a growing cohort of patients needing counseling, management decisions, operations, and extended postoperative surveillance."

### 9.2 Inheritance (for the Mendelian subset)

- **Predominant mode: autosomal dominant.** Albornoz et al. (PMID:16996941): *"The predominant inheritance pattern was autosomal dominant (76.9%), with varying degrees of penetrance and expressivity."* Applies to FBN1, TGFBR1/2, SMAD3, TGFB2/3, ACTA2, MYH11, MYLK, PRKG1, LOX, THSD4, LTBP3, COL3A1, SKI, NOTCH1.
  - HPO: `HP:0000006` Autosomal dominant inheritance (*verify with OAK*).
- **Autosomal recessive:** *SLC2A10* (arterial tortuosity syndrome), *EFEMP2*/FBLN4 (cutis laxa with aortopathy), *CBS* (homocystinuria phenocopy). `HP:0000007` (*verify*).
- **X-linked:** *BGN* (Meester-Loeys syndrome), *FLNA*. `HP:0001417`/`HP:0001419` (*verify*).
- **Multifactorial/polygenic:** the sporadic majority — PMID:37308786 establishes a complex-trait architecture. `HP:0010982` Polygenic inheritance would be the appropriate binding for a susceptibility-typed `Genetic` block.
- **Penetrance:** high but **incomplete and age-dependent**. Marfan aortic root dilation is nearly fully penetrant by adulthood; nonsyndromic FTAAD genes show markedly reduced penetrance (roughly 50–80% for ACTA2 by age 60; lower for MYLK and LOX). Non-penetrant obligate carriers are documented in every published FTAAD pedigree.
- **Expressivity:** **highly variable**, both between and within families — the same *FBN1* allele can produce neonatal Marfan in one relative and isolated root dilation in another. Even MYH11 asymptomatic carriers show a subclinical phenotype (PMID:16444274: *"All individuals bearing the heterozygous mutations, even if asymptomatic, showed marked aortic stiffness."*).
- **Genetic anticipation:** **not a feature** — no repeat-expansion mechanism is involved. Apparent anticipation in pedigrees reflects ascertainment bias and improved screening in younger generations.
- **Germline mosaicism:** reported for *FBN1* and *COL3A1*; recurrence risk to siblings of an apparently de novo proband is therefore not zero (empiric estimates ~1%). Somatic/gonosomal mosaicism in mildly affected transmitting parents is documented.
- **De novo rate:** ~25% of Marfan probands; the *ACTA2* R179 MSMDS allele is characteristically de novo.
- **Founder effects:** no widely established TAA founder alleles. Population-specific recurrent variants have been reported in isolated cohorts (e.g. specific *FBN1* alleles in Finnish, Ashkenazi, and Han Chinese series), but none rise to founder-mutation carrier-screening status.
- **Consanguinity:** relevant only to the AR forms (SLC2A10, EFEMP2), which are enriched in consanguineous populations of the Middle East, North Africa, and South Asia.
- **Carrier frequency:** not a meaningful concept for the AD forms. For AR arterial tortuosity syndrome, carrier frequency is not established outside founder pockets.

### 9.3 Population demographics

- **Sex:** Overall incidence is higher in men (Olsson: 16.3 vs 9.1 per 100,000/yr). But **women have worse outcomes at any given diameter** — Clouse et al. found *"51% of thoracic aortic aneurysms were identified in women who were considerably older at recognition than men (mean age, 75.9 vs 62.8 years, respectively; P= .01)"* and *"Seventy-nine percent of ruptures occurred in women (P= .01)"* (PMID:9851478). Women are systematically under-referred for elective repair because absolute-diameter thresholds derived from male-dominated cohorts are relatively too high for smaller body size — the argument for indexed thresholds.
- **Ethnicity:** No strong replicated ethnic gradient for TAA itself. Higher hypertension prevalence and worse BP control in Black populations in the US contribute to higher rates of aortic dissection at younger ages; a disproportionate burden of dissection in Black patients is well documented in US registry data. GWAS discovery to date is European-ancestry-weighted, though MVP included substantial African- and Hispanic-ancestry participation.
- **Geography:** Global; ascertainment tracks CT/echo availability. Syphilitic aortitis remains a meaningful cause in settings with high untreated syphilis prevalence. Seasonal/circadian clustering of dissection onset (winter, morning) is reproducible, with a temperature association reported in the Nordic registries (PMID:36345977).
- **Age distribution:** Bimodal in effect — a young, genotype-driven peak (teens–40s, HTAD) and a large late peak (65–85 y, degenerative). Descending TAA skews older than root/ascending TAA.

---

## 10. Diagnostics

### 10.1 Imaging (the diagnostic mainstay)

| Modality | Role | NCIT | Verified |
|---|---|---|---|
| **CT angiography (contrast, ECG-gated)** | Reference standard for diagnosis, sizing, surgical planning, and emergency dissection triage; whole-aorta coverage | `NCIT:C202408` Computed Tomography Angiography | ✅ |
| Multi-detector CTA | | `NCIT:C157338` Multi-detector Computed Tomography Angiography | ✅ |
| **Transthoracic echocardiography** | First-line for aortic root/proximal ascending and valve; surveillance in Marfan children | `NCIT:C80404` Transthoracic Echocardiography Test | ✅ |
| **Transesophageal echocardiography** | Intraoperative and unstable-patient dissection diagnosis | `NCIT:C80405` Transesophageal Echocardiography Test | ✅ |
| Echocardiography (generic) | | `NCIT:C16525` Echocardiography Test | ✅ |
| **MR angiography** | Radiation-free serial surveillance, especially in young HTAD patients | `NCIT:C190557` Magnetic Resonance Angiography | ✅ |
| Chest radiograph | Insensitive; may show mediastinal widening or a calcified aortic knob | — | |
| 4D-flow MRI | Research/emerging: wall shear stress mapping in BAV aortopathy | — | |
| ¹⁸F-FDG PET/CT | Aortitis and infected (mycotic) aneurysm | — | |

**Measurement discipline matters for KB fidelity.** Guidelines require reporting the technique (leading-edge-to-leading-edge in echo; inner-edge-to-inner-edge on CT/MR), the plane (double-oblique perpendicular to the centerline), and the ECG gating status. Sinus-of-Valsalva measurements should use cusp-to-commissure or cusp-to-cusp conventions consistently across serial studies. **Z-scores** (age/sex/BSA-adjusted) are mandatory in pediatrics and used throughout Marfan management.

**Size normalization metrics:**
- **Aortic size index (ASI)** = diameter (cm) / BSA (m²) — the standard in Turner syndrome.
- **Aortic height index (AHI)** = diameter (cm) / height (m).
- **Cross-sectional area / height ratio** (cm²/m) — the 2022 ACC/AHA-endorsed alternative threshold; >10 cm²/m supports intervention.

### 10.2 Laboratory tests and biomarkers

- No diagnostic assay for TAA itself.
- **D-dimer** for acute dissection rule-out in combination with a low aortic dissection detection risk score (ADD-RS ≤1). Sensitive, not specific.
- Aortitis panel: ESR, CRP, IgG4, RPR/FTA-ABS, ANCA, blood cultures.
- Homocysteine / plasma amino acids to exclude homocystinuria in a Marfanoid patient.
- Circulating research biomarkers (MMP-9, TGF-β1, sST2, tenascin-C, desmosine) — none validated for clinical use.

### 10.3 Histopathology / biopsy

Aortic tissue is obtained at surgery, not by pre-operative biopsy. Findings, per the Society for Cardiovascular Pathology / AECVP consensus (PMID:27031798):
- **Medial degeneration** (the preferred term): elastic fiber fragmentation and loss, mucoid ECM accumulation (translamellar and intralamellar), SMC nuclei loss, laminar medial collapse.
- Grading is semiquantitative (mild/moderate/severe) for each component.
- Movat pentachrome / Verhoeff-van Gieson stains for elastin, Alcian blue for GAGs.
- **Aortitis** subtypes: granulomatous with giant cells (GCA/Takayasu), lymphoplasmacytic with storiform fibrosis and obliterative phlebitis (IgG4-RD), obliterative endarteritis of vasa vasorum with plasma cells (syphilis), suppurative (bacterial).
- Immunohistochemistry: loss of ACTA2/SM-MHC staining in contractile-gene disease; IgG4/IgG plasma-cell ratio; CD68 macrophage burden.

### 10.4 Electrophysiology

Not diagnostic for TAA. ECG is obtained in suspected dissection primarily to detect coronary-ostial involvement (inferior STEMI pattern from right-coronary ostial dissection) and to exclude ACS as an alternative diagnosis — IRAD found the *"initial chest radiograph and electrocardiogram were frequently not helpful (no abnormalities were noted in 12.4% and 31.3% of patients, respectively)"* (PMID:10685714).

### 10.5 Genetic testing

`NCIT:C15709` Genetic Testing ✅.

**Recommended approach (2022 ACC/AHA, PMID:36334952; 2024 EACTS/STS, PMID:38416090 — *paraphrase*, verify before quoting):**
- Offer genetic testing to any patient with **aortic root/ascending aneurysm or aortic dissection** who has: syndromic features; a family history of TAAD or unexplained sudden death; young age at presentation (<60 y); or the combination with other arteriopathy.
- **Multigene panel** (an HTAD panel of the 11 definitive/strong ClinGen genes plus the moderate-evidence genes) is the first-line test — this is precisely why the ClinGen curation (PMID:30071989) was performed.
- **Whole-exome sequencing (WES)** — reserved for panel-negative, strongly familial cases; the discovery route for LTBP3 (PMID:29625025), PRKG1 (PMID:23910461), and THSD4 (PMID:32855533).
- **Whole-genome sequencing (WGS)** — research/tertiary use; the discovery route for the *LOX* founding family (PMID:27432961). Adds deep-intronic and structural-variant detection.
- **Single-gene testing** — only when the familial variant is known (cascade testing) or the phenotype is unambiguous (e.g. classic Marfan → *FBN1*).
- **Del/dup analysis (MLPA)** — required alongside sequencing for *FBN1* and *COL3A1*.
- **Chromosomal microarray** — for syndromic presentations, 16p13.1 duplication, and contiguous-gene deletions of *FBN1*.
- **Karyotype** — indicated in any female with unexplained aortic dilation and short stature, to detect **45,X Turner syndrome** and mosaic variants.
- **FISH** — 22q11.2 if conotruncal features are present.
- **mtDNA testing / repeat-expansion testing** — **not applicable** to TAA.

**Cascade family screening** is as important as proband testing: guidelines recommend aortic imaging for all first-degree relatives of a TAAD proband, and genotype-directed release from surveillance for variant-negative relatives when a pathogenic familial variant is identified. Albornoz et al. (PMID:16996941): *"Screening of first-order relatives of probands with TAA is essential."*

### 10.6 Omics-based diagnostics

- **RNA-seq** — used for splice-variant reclassification of *FBN1*/*COL3A1* VUS (fibroblast or blood transcript analysis). This is the highest-yield omics adjunct in current practice.
- **Proteomics/metabolomics/epigenomics** — research only.
- **Liquid biopsy** — cell-free DNA is used for post-transplant surveillance in other settings, not for TAA. No validated circulating diagnostic.

### 10.7 Clinical criteria and differential diagnosis

**Criteria.** There is no separate diagnostic criteria set for TAA itself (it is an imaging diagnosis). The relevant criteria sets are for the underlying syndromes:
- **Revised Ghent nosology (2010)** for Marfan syndrome — aortic root Z ≥2 plus ectopia lentis, or plus a causal *FBN1* variant, or plus systemic score ≥7.
- **2017 International Classification of the Ehlers-Danlos Syndromes** for vascular EDS.
- **Loeys-Dietz** — clinical gestalt plus a pathogenic variant in one of the six TGF-β-pathway genes; no scored criteria.
- **Aortic Dissection Detection Risk Score (ADD-RS)** for triage of suspected acute dissection.

**Differential diagnosis:**

| Alternative | Distinguishing features |
|---|---|
| Aortic **pseudoaneurysm** | Contained rupture; lacks all three wall layers; irregular neck; post-traumatic/post-surgical |
| **Intramural hematoma** | Crescentic wall thickening without an intimal flap or false-lumen flow |
| **Penetrating atherosclerotic ulcer** | Focal ulcer crater with adjacent atheroma; usually descending |
| Aortic **dissection** with chronic dilation | Intimal flap; true/false lumen |
| Aortic **coarctation** with post-stenotic dilation | Gradient; rib notching |
| **Aortic tortuosity/elongation** in the elderly | Elongation without true caliber increase |
| Mediastinal mass mimicking aneurysm on CXR | CT resolves |
| **Aortitis** (GCA, Takayasu, IgG4, syphilis) | Circumferential wall thickening, mural enhancement, elevated inflammatory markers, FDG uptake |
| **Mycotic aneurysm** | Saccular, rapidly enlarging, periaortic gas/fat stranding, fever, positive cultures |
| **Homocystinuria** (CBS deficiency) | Marfanoid habitus, *downward* lens dislocation, thrombosis, intellectual disability, elevated homocysteine |
| **Congenital contractural arachnodactyly** (FBN2) | Marfanoid with contractures, crumpled ears; aortic dilation mild/rare |
| **MASS phenotype / familial ectopia lentis** | Marfan-overlapping without progressive root dilation |

### 10.8 Screening

- **Cascade family screening** (first-degree relatives of a TAAD proband) — the highest-yield strategy; imaging ± genotype-directed.
- **Genotype-directed screening** in known-variant families — including screening of children in Marfan/LDS from diagnosis.
- **Turner syndrome** — lifelong cardiac imaging surveillance is standard of care.
- **BAV** — first-degree relative echocardiographic screening is guideline-recommended.
- **Population screening is NOT recommended** for TAA (unlike the one-time ultrasound AAA screen in older male smokers). The 2022 guideline instead promotes systematic reporting and follow-up of **incidentally detected** aortic dilation on chest imaging performed for other reasons — an "opportunistic screening" model that is now a major implementation target.
- **Newborn screening:** not applicable. **Carrier screening:** not applicable (AD disease). **Preimplantation genetic testing (PGT-M)** and prenatal diagnosis are available for known familial pathogenic variants.

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

| Outcome | Value | Source |
|---|---|---|
| Untreated TAA, 5-year survival | **54%** (Yale cohort, unoperated) | PMID:11834007 |
| Population 5-year survival (1980–1994) | **56%** (95% CI 48–66%), improved from 19% in 1951–1980 | PMID:9851478 |
| Post-operative survival (Sweden) | **92% / 77% / 57% at 1 / 5 / 10 years** | PMID:17145990 |
| 30-day operative mortality (Sweden, all-comers incl. emergency) | **16%** (389/2455) | PMID:17145990 |
| Contemporary **elective** root/ascending repair mortality (experienced centers) | ~1–3%; valve-sparing root replacement in Marfan ~1% | Single-center series (e.g. early mortality 0.96%) |
| Acute type A dissection, overall in-hospital mortality | **27.4%** | PMID:10685714 |
| Type A, surgical | **26%** | PMID:10685714 |
| Type A, medical management | **58%** | PMID:10685714 |
| Type B, medical management | **10.7%** | PMID:10685714 |
| Type B, surgical | **31.4%** | PMID:10685714 |
| Vascular EDS median survival | **48 years** | PMID:10706896 |
| Untreated Marfan (historical, pre-surgical era) | ~32 years; now approaching normal with root repair | Classic literature |

Elective repair is the single most powerful prognostic modifier. Davies et al. (PMID:11834007):

> "Elective, preemptive surgical repair restored life expectancy to normal."
>
> "Thoracic aneurysm is a lethal disease; aneurysm size has a profound impact on rupture, dissection, and death; for counseling purposes, the patient with an aneurysm exceeding 6 cm can expect a yearly rate of rupture or dissection of at least 6.9% and a death rate of 11.8%; and elective surgical repair restores survival to near normal."

### 11.2 Morbidity, disability, and QoL

- **Stroke** — 3–8% after arch surgery; higher with dissection-related malperfusion.
- **Spinal cord ischemia / paraplegia** — 2–10% after extensive descending/thoracoabdominal repair (open or TEVAR); mitigated by CSF drainage and staged intercostal sacrifice.
- **Acute kidney injury / dialysis** — 5–15% after thoracoabdominal repair.
- **Reoperation** — *"The cumulative incidence of thoracic aortic reoperations was 7.8% at 10 years"* (PMID:17145990); higher in HTAD, where the residual native aorta continues to degenerate.
- **Anticoagulation-related morbidity** — bleeding and thromboembolism with mechanical composite grafts; a key reason valve-sparing techniques are preferred in young Marfan patients.
- **Chronic pain, PTSD, and reduced mental-component QoL** after dissection.
- **QoL instruments**: SF-36 and EQ-5D-5L are the standard generic measures; PROMIS domains are increasingly used; no validated TAA-specific PRO exists (a genuine gap). Marfan-specific QoL questionnaires exist but are not widely adopted.

### 11.3 Complications (curate as downstream nodes)

Aortic dissection (`HP:0002647` ✅) → cardiac tamponade, aortic regurgitation (`HP:0001659` ✅), myocardial infarction, stroke (`HP:0002140` ✅), mesenteric/renal/limb malperfusion, paraplegia; aortic rupture (`HP:0031649` ✅) → hemothorax, hemopericardium, exsanguination; aorto-bronchial fistula → hemoptysis (`HP:0002105` ✅); aorto-esophageal fistula → hematemesis; compression syndromes (hoarseness `HP:0001609` ✅, dysphagia `HP:0002015` ✅, SVC obstruction, tracheal compression); mural thrombus with distal embolization; heart failure from chronic aortic regurgitation; sudden death (`HP:0001699` ✅).

**Recovery potential:** the aneurysmal segment does **not** recover — surgical replacement is definitive for that segment only. The rest of the aorta continues on its natural history.

### 11.4 Prognostic factors and biomarkers

**Established prognostic factors:**
- **Maximal diameter** (strongest single factor; PMID:11834007, PMID:9851478) — with the crucial caveat that it under-identifies dissection risk (PMID:17709637).
- **Growth rate** — ≥0.3 cm/yr over two consecutive years, or ≥0.5 cm in one year, is an intervention trigger.
- **Genotype** — TGFBR1/2, ACTA2 (especially R179), MYLK, PRKG1, and COL3A1 confer higher event risk at smaller diameters; this drives genotype-specific surgical thresholds.
- **Indexed size** — ASI, aortic height index, cross-sectional area/height ratio; especially important in women, short stature, and Turner syndrome.
- **Family history of dissection at small diameter** — an independent trigger for earlier repair.
- **Hypertension** (PMID:17709637: OR 2.17 for dissection at <5.5 cm), **female sex** (PMID:9851478: 79% of ruptures), **increasing age**, **saccular morphology**, **symptoms** (pain = impending rupture until proven otherwise), **planned pregnancy**, **concomitant cardiac surgery**.

**Prognostic biomarkers:** none validated. Investigational: D-dimer (acute), MMP-9, TGF-β1, sST2, and imaging-derived biomechanical indices (peak wall stress, aortic strain/distensibility, pulse wave velocity — reduced distensibility predicts faster growth in Marfan, PMID:29631804). Machine-learning models combining geometry, biomechanics, and genotype are an active research direction and would be a good `PHENOTYPE_ALGORITHM` / `derivation_basis: MECHANISTIC_HYPOTHESIS` candidate.

---

## 12. Treatment

### 12.1 Pharmacotherapy

`NCIT:C15986` Pharmacotherapy ✅ is the correct generic `treatment_term`; pair with `therapeutic_agent`.

| Treatment | Agent term | Mechanism | Evidence |
|---|---|---|---|
| **β-blockade** (atenolol, metoprolol, bisoprolol) | `CHEBI:2904` atenolol ✅; `CHEBI:6904` metoprolol ✅; class `NCIT:C29576` Beta-Adrenergic Antagonist ✅ | Reduces dP/dt and heart rate → lower pulsatile wall stress | Long-standing standard of care; PMID:25405392, PMID:36049495 |
| **ARB** (losartan, irbesartan) | `CHEBI:6541` losartan ✅; `CHEBI:5959` irbesartan ✅; class `NCIT:C66930` Angiotensin II Receptor Antagonist ✅ | AT1R blockade → reduced TGF-β signaling + afterload reduction | PMID:16601194 (mouse), PMID:23999449, PMID:25405392, PMID:36049495 |
| **Strict BP control** (target <130/80 mmHg) | multi-agent | Reduces wall stress | Guideline (PMID:36334952) |
| **Statins** | e.g. atorvastatin | Pleiotropic/anti-remodeling | Observational only; not a TAA indication |
| **Avoid fluoroquinolones** | — | ECM/MMP toxicity | PMID:29519881, PMID:30046809 |
| **ACE inhibitors** | — | Alternative if ARB intolerant | Weaker evidence than ARB |
| **Verapamil/diltiazem** | — | If β-blocker intolerant | Second-line |

**The definitive medical-therapy evidence.** The Pediatric Heart Network trial (PMID:25405392, *paraphrase*: 608 children and young adults with Marfan syndrome randomized to losartan vs atenolol at 21 centers, 2007–2011) found **no significant difference in the rate of aortic-root Z-score change over 3 years** between the two drugs, and no difference in aortic surgery, dissection, or death. A short verbatim fragment: *"Aortic-root dissection is the leading cause of death in Marfan's syndrome. Studies suggest that with regard to slowing aortic-root enlargement, losartan may be more effective than beta-blockers, the current standard therapy in most centers."*

COMPARE (PMID:23999449, *paraphrase*, verbatim fragment): *"Aortic root dilatation rate after 3.1 ± 0.4 years of follow-up was significantly lower in the losartan group than in controls"* (0.77 vs 1.35 mm), in 233 adults, with no difference in the composite clinical endpoint.

The Marfan Treatment Trialists' Collaboration individual-patient-data meta-analysis (PMID:36049495, *paraphrase* with verbatim fragments) reconciled the trials:

> "Angiotensin receptor blockers (ARBs) and β blockers are widely used in the treatment of Marfan syndrome to try to reduce the rate of progressive aortic root enlargement characteristic of this condition, but their separate and joint effects are uncertain."
>
> "We identified ten potentially eligible trials including 1836 patients from our search, from which seven trials and 1442 patients were eligible for inclusion in our main analyses."
>
> "During a median follow-up of 3 years, allocation to ARB approximately halved the annual rate of change in the aortic root Z score."
>
> "combination therapy with both ARBs and β blockers from the time of diagnosis would provide even greater reductions in the rate of aortic enlargement than either treatment alone"

**Current practice conclusion:** ARB and β-blocker each roughly halve the rate of aortic root Z-score progression relative to no treatment; their effects appear independent and likely additive, supporting **combination therapy** in Marfan syndrome. Extrapolation to non-Marfan HTAD and sporadic TAA is by inference, not direct evidence.

### 12.2 Pharmacogenomics

- No CPIC guideline is specific to TAA.
- **CYP2C9** and **VKORC1** genotype-guided **warfarin** dosing is CPIC Level A and directly relevant to patients receiving a mechanical composite graft (Bentall) — this is the single most actionable PGx interaction in the TAA care pathway.
- **CYP2D6** poor/ultrarapid metabolizer status affects metoprolol exposure (CPIC guideline exists for metoprolol); atenolol is renally cleared and PGx-neutral, which is one practical argument for atenolol in this population.
- Losartan requires **CYP2C9**-mediated conversion to its active metabolite EXP3174; CYP2C9 poor metabolizers have reduced active-drug exposure. Not currently guideline-actionable, but a plausible modifier of trial heterogeneity.

### 12.3 Surgical and interventional treatment

`NCIT:C15329` Surgical Procedure ✅; `NCIT:C157839` Endovascular Aneurysm Repair ✅; `NCIT:C50815` Aortic Valve Replacement ✅.

| Procedure | Indication | Notes |
|---|---|---|
| **Valve-sparing aortic root replacement (David reimplantation; Yacoub remodeling)** | Root aneurysm with a normal/repairable valve, esp. young HTAD patients | Preferred in Marfan; avoids anticoagulation. Reported early mortality <1%; ~91% survival at 10 y, 76% at 20 y; freedom from valve reoperation 86% at 10 y, 80% at 20 y (single-center series — verify PMIDs) |
| **Composite valve-graft (Bentall) replacement** | Root aneurysm with an unrepairable/diseased valve | Mechanical (lifelong warfarin) or bioprosthetic (structural degeneration) |
| **Supracoronary ascending aortic replacement** | Ascending aneurysm sparing the root | Simpler; leaves the root at risk in HTAD |
| **Hemiarch / total arch replacement, frozen elephant trunk** | Arch involvement | Requires hypothermic circulatory arrest ± antegrade cerebral perfusion |
| **Open descending/thoracoabdominal repair** | Extensive descending disease, connective tissue disease | Crawford extents I–IV; CSF drainage for cord protection |
| **TEVAR (thoracic endovascular aortic repair)** | Descending TAA, complicated type B dissection, penetrating ulcer, traumatic transection | **Relatively contraindicated as definitive therapy in HTAD** (Marfan/LDS/vEDS) because the diseased native aorta is a poor landing zone; used as a bridge in emergencies |
| **Branched/fenestrated endografts, TAMBE** | Arch and thoracoabdominal extension | Growing, high-volume-center technique |
| **Emergency ascending replacement** | Acute type A dissection | Surgical emergency; ~1–2%/hour mortality untreated |

**Thresholds (2022 ACC/AHA, PMID:36334952 — *paraphrase*; verify each before curating):** ≥5.5 cm for sporadic/degenerative ascending aneurysm (Class 1); ≥5.0 cm at experienced multidisciplinary aortic-team centers (Class 2a); ≥5.0 cm in Marfan syndrome (with 4.5 cm considered where there is a family history of early dissection, rapid growth, or planned pregnancy); ≥4.5 cm for TGFBR1/TGFBR2 Loeys-Dietz; ≥4.5 cm for ACTA2 and other high-risk genotypes; concomitant repair at ≥4.5 cm when the patient is already undergoing aortic valve or other cardiac surgery; growth ≥0.3 cm/yr over two consecutive years or ≥0.5 cm in one year; cross-sectional-area-to-height ratio >10 cm²/m; ≥5.5 cm (endovascular) or ≥6.0 cm (open) for descending TAA. A major structural recommendation of the 2022 guideline is the **multidisciplinary aortic team** and referral to high-volume centers.

### 12.4 Advanced therapeutics

- **Gene therapy** — none clinical. Conceptually difficult: aortic SMCs are hard to transduce, the diseased protein is often a structural dominant negative requiring allele-specific knockdown, and the therapeutic window predates symptoms by decades.
- **Gene editing** — preclinical only. Allele-specific CRISPR knockdown of dominant-negative *FBN1* and base editing of *ACTA2* have been demonstrated in iPSC-SMCs.
- **RNA-based** — no approved ASO or siRNA. Allele-specific ASO knockdown of mutant *FBN1* is a rational but unrealized target; the dismech `antisense_oligonucleotide_therapy` module's RNase-H paradigm would fit.
- **Cell therapy** — none.
- **Targeted / mechanism-directed** — the historical hope (TGF-β neutralization) is complicated by the dimorphic effect (PMID:25614286). Preclinically explored: ERK1/2 inhibition, NOS2 inhibition, doxycycline (MMP inhibition; failed in AAA trials), rapamycin/mTOR inhibition, resveratrol (a single-arm open-label trial in Marfan, PMID:39317438), and PPAR-γ agonism.
- **Immunotherapy** — applicable only to the aortitis arm: high-dose glucocorticoids, **tocilizumab** (IL-6R mAb, approved for GCA), methotrexate, rituximab (IgG4-RD), TNF inhibitors (Takayasu). This is a genuinely distinct therapeutic branch and should be modeled separately from degenerative TAA.

### 12.5 Supportive, rehabilitative, and lifestyle measures

`NCIT:C15747` Supportive Care ✅; `NCIT:C15372` Smoking Cessation Intervention ✅; `NCIT:C15240` Genetic Counseling ✅.

- **Activity modification** — avoid maximal isometric exertion, heavy weightlifting, competitive contact and burst-exertion sport; moderate aerobic exercise at ~50% capacity is encouraged (deconditioning is itself harmful).
- **Smoking cessation** — strongest lifestyle intervention for descending TAA.
- **Stimulant avoidance** (cocaine, amphetamines).
- **Fluoroquinolone avoidance** in known HTAD.
- **Pregnancy management** — pre-conception root assessment, prophylactic root repair at 4.0–4.5 cm in Marfan before pregnancy, β-blockade throughout, delivery planning at an aortic center. Pregnancy is generally contraindicated in vascular EDS.
- **Cardiac rehabilitation** post-repair; `NCIT:C15302` Physical Therapy.
- **Genetic counseling** — pedigree construction, cascade testing, reproductive options.

### 12.6 Experimental treatments (ClinicalTrials.gov)

Active and recent directions (obtain and verify NCT numbers before curating a `clinical_trials` block):
- Combination ARB + β-blocker versus monotherapy in Marfan (the direct implication of PMID:36049495).
- **Irbesartan** in Marfan (AIMS trial, UK — completed; showed reduced aortic root growth).
- Resveratrol in Marfan (single-arm, PMID:39317438).
- Rapamycin/sirolimus and mTOR inhibition — preclinical to early phase.
- Rifampicin, doxycycline, and other MMP-directed repurposing — largely negative.
- TEVAR versus optimal medical therapy in uncomplicated type B dissection (ADSORB, INSTEAD-XL legacy; ongoing successors).
- AI/biomechanics-guided intervention timing (observational).

### 12.7 Treatment strategy summary

```
Aneurysm detected
  ├─ Determine etiology: syndromic features? family history? BAV? aortitis? infection?
  ├─ Genetic testing (HTAD panel) if young / familial / syndromic
  ├─ ALL: BP <130/80, β-blocker ± ARB, smoking cessation, activity counseling,
  │       avoid fluoroquinolones, serial imaging (interval set by size + genotype)
  ├─ Cascade imaging ± genotype screening of first-degree relatives
  └─ Meets threshold (size / indexed size / growth / genotype / symptoms /
     planned pregnancy / concomitant cardiac surgery)?
        ├─ Ascending/root → open repair (valve-sparing preferred if valve is good)
        ├─ Arch → hemiarch/total arch ± FET
        └─ Descending → TEVAR (avoid as definitive therapy in HTAD) or open repair
  Aortitis arm → immunosuppression (steroids, tocilizumab, MTX, rituximab)
  Mycotic arm  → prolonged targeted antimicrobials + debridement/repair
```

**Personalized medicine** is already real here: surgical thresholds are formally **genotype-stratified**, which makes TAA one of the clearest examples of genomically guided procedural timing in cardiovascular medicine.

---

## 13. Prevention

### 13.1 Primary prevention (preventing the aneurysm)

- **Hypertension control at the population level** — the single highest-impact primary prevention lever for degenerative TAA.
- **Tobacco control** — for descending/atherosclerotic TAA.
- **Syphilis control and treatment** — has essentially eliminated syphilitic aortitis in high-income settings; still relevant globally.
- **Reproductive prevention in HTAD** — PGT-M and prenatal diagnosis for known familial pathogenic variants; the only true primary prevention for the Mendelian arm.
- Note: for genotype-positive individuals, "primary prevention" is realistically **prevention of dilation**, i.e. early β-blocker/ARB from diagnosis (PMID:36049495 supports treating from the time of diagnosis).

### 13.2 Secondary prevention (early detection)

- **Cascade family imaging** — first-degree relatives of every TAAD proband.
- **Genotype-directed surveillance and de-escalation** in known-variant families.
- **Turner syndrome** and **BAV** lifelong surveillance protocols.
- **Opportunistic detection**: systematic reporting and structured follow-up of incidentally noted aortic dilation on chest CT/echo done for other reasons — the highest-yield implementation gap identified by the 2022 guideline.
- **No population screening program** exists or is recommended (contrast: one-time abdominal ultrasound AAA screening in men aged 65–75 who have ever smoked, a USPSTF Grade B recommendation that does **not** extend to the thorax).

### 13.3 Tertiary prevention (preventing complications in those with disease)

- Serial imaging on a size- and genotype-determined interval (typically 6–12 months, more frequently near threshold or with rapid growth).
- Medical therapy (β-blocker + ARB) and strict BP control.
- Timely elective repair at the genotype-appropriate threshold — the definitive intervention.
- Post-repair lifelong surveillance of the residual native aorta.
- Endocarditis prophylaxis after prosthetic valve/graft placement.
- Pregnancy planning and peripartum aortic-center care.
- Medication avoidance list (fluoroquinolones, stimulants).
- Patient-carried medical alert identification stating the aortic diagnosis — relevant to emergency triage of chest pain.

### 13.4 Immunization

Not applicable to TAA pathogenesis. Routine adult vaccination (influenza, pneumococcal, COVID-19, RSV) is standard perioperative and cardiovascular care.

### 13.5 Genetic screening and counseling

- **Carrier screening** — not applicable (autosomal dominant).
- **Cascade testing** — the core strategy.
- **PGT-M / prenatal diagnosis** — available; counseling should address the variable expressivity that makes prediction of severity from genotype imperfect.
- **Counseling content**: 50% transmission risk for AD forms; de novo rate ~25% in Marfan with a residual ~1% sibling recurrence risk from germline mosaicism; age-dependent penetrance; the importance of continued imaging for variant-negative relatives when no familial variant has been identified.
- Providers: NSGC-credentialed genetic counselors; `NCIT:C15240` Genetic Counseling ✅.

### 13.6 Public health and environmental interventions

- Population sodium reduction and hypertension programs.
- Tobacco control policy.
- Regulatory action on fluoroquinolone labeling (FDA/EMA warnings — already implemented).
- Emergency-systems design: regional aortic centers with rapid transfer pathways for acute type A dissection, given the ~1–2%/hour untreated mortality.
- Health-system-level clinical decision support to flag and route incidental aortic dilation findings.

### 13.7 Prophylaxis

**Prophylactic aortic surgery is the prophylaxis** — pre-emptive replacement of the aneurysmal segment before it dissects. This is the concept Davies et al. captured (PMID:11834007): *"This analysis strongly supports careful radiologic follow-up and elective, preemptive surgical intervention for the otherwise lethal condition of large thoracic aortic aneurysm."* Pre-pregnancy prophylactic root replacement in Marfan women with a 4.0–4.5 cm root is a specific and well-established application.

---

## 14. Other Species / Natural Disease

### 14.1 Taxonomy and naturally occurring disease

| Species | NCBI Taxon | Natural disease | Notes |
|---|---|---|---|
| Dog (*Canis lupus familiaris*) | NCBITaxon:9615 | Spontaneous dissecting aortic aneurysm — rare, case-report level (e.g. PMID:12683625, "Aortic dissection associated with aortic aneurysms and posterior paresis in a dog"). MONDO recognizes `MONDO:1012381` **familial thoracic aortic aneurysm, dog** ✅ | Rare; often presents with posterior paresis from aortoiliac involvement |
| Cat (*Felis catus*) | NCBITaxon:9685 | Dissecting aortic aneurysm, often with systemic hypertension (PMID:29717986) | Rare |
| Horse (*Equus caballus*) | NCBITaxon:9796 | Aortic root rupture in breeding stallions; aorto-pulmonary/aorto-cardiac fistula — a recognized and fatal syndrome | The best-characterized large-animal spontaneous aortic rupture |
| Turkey (*Meleagris gallopavo*) | NCBITaxon:9103 | **Spontaneous dissecting aortic aneurysm of male turkeys** — a classic agricultural disease; strongly modulated by copper status and by β-aminopropionitrile (lathyrogen) exposure | Direct comparative counterpart of human *LOX* loss-of-function |
| Chicken (*Gallus gallus*) | NCBITaxon:9031 | Copper-deficiency aortic rupture | Foundational to the discovery of lysyl oxidase biology |
| Cattle (*Bos taurus*) | NCBITaxon:9913 | Bovine Marfan syndrome — an autosomal dominant *FBN1*-associated syndrome with aortic dilation, described in Holstein cattle (OMIA) | A genuine naturally occurring Marfan model |
| Non-human primates | NCBITaxon:9539 (macaque) etc. | Sporadic aortic aneurysm/dissection reported | Rare |

Per the Merck Veterinary Manual, aneurysms are rare in domestic animal species but have been reported in dogs, cats, horses, primates, turkeys, reptiles, and other exotic species.

### 14.2 Orthologous genes (NCBI Gene, mouse)

*Fbn1* (14118), *Tgfbr1* (21812), *Tgfbr2* (21813), *Smad3* (17127), *Tgfb2* (21808), *Acta2* (11475), *Myh11* (17880), *Mylk* (107589), *Prkg1* (19091), *Lox* (16948), *Col3a1* (12825), *Thsd4* (207596), *Notch1* (18128). All are single-copy, high-identity orthologs — the pathway is deeply conserved. Alliance of Genome Resources and HomoloGene are the reference resources.

### 14.3 Comparative pathology and evolutionary conservation

- **Conserved:** the elastin–fibrillin–LOX cross-linking architecture, the SMC contractile unit, and TGF-β sequestration by LTBP-fibrillin are conserved across amniotes. Copper deficiency and BAPN produce aortic rupture in birds, rodents, and pigs by the same LOX-inhibition mechanism that causes human *LOX*-TAAD.
- **Divergent:** most animals do not live long enough, or at high enough systemic blood pressure with human-like bipedal hemodynamics, to develop age-related degenerative TAA. Quadrupeds have different aortic arch geometry and lower ascending-aorta wall stress. This is the central reason spontaneous TAA is a *rare* veterinary diagnosis but a common human one, and why engineered models rather than natural disease dominate the research literature.
- The turkey and horse are the two species where spontaneous aortic rupture is a recognized production/breeding problem, and both have been used as comparative models.

### 14.4 Transmission

**Not applicable** — TAA is non-communicable and non-zoonotic. The only pathogen-linked forms (syphilitic, salmonella mycotic) involve organisms that are separately zoonotic or human-restricted; the aneurysm itself is not transmissible.

---

## 15. Model Organisms

### 15.1 Mammalian genetic models (mouse — the dominant system)

| Model | Lesion | Phenotype recapitulation | Key limitation | Reference |
|---|---|---|---|---|
| ***Fbn1*^C1039G/+** | Knock-in cysteine substitution, dominant negative | Progressive aortic root aneurysm, elastic fiber fragmentation, SMC disarray, excess collagen/proteoglycan; skeletal and pulmonary Marfan features after ~2 months; >90% survival at 8 months | Rarely dissects or ruptures — models dilation, not the lethal event | PMID:15254584; PMID:16601194 |
| ***Fbn1*^mgR/mgR** | Hypomorphic allele (~15–25% normal fibrillin-1) | Severe, rapidly enlarging root aneurysm with dissection/rupture and early death; the standard survival-endpoint model | Homozygous hypomorph is not the human genotype | PMID:25614286 |
| ***Fbn1*^C1039G/C1039G** | Homozygous | Perinatal death from aortic dissection | Not viable for longitudinal study | — |
| ***Tgfbr1*^M318R/+, *Tgfbr2*^G357W/+** | Knock-in LDS alleles | Aortic root dilation with increased pSmad2 **and** pERK, elastin fragmentation — reproduces the LDS paradox | Milder than human LDS | Gallo et al., *JCI* 2014 (retrieve PMID) |
| ***Tgfbr1*^+/−** (haploinsufficient) | Null allele | **No** cardiovascular phenotype — argues against simple haploinsufficiency | Negative result, informative | PMC3933654 (retrieve PMID) |
| ***Tgfb2*^+/−** | Haploinsufficiency | Aortic root aneurysm with increased canonical and noncanonical TGF-β signaling; worsens *Fbn1*^C1039G/+ | — | PMID:22772368 |
| ***Smad3*^−/−** | Null | Aortic dilation, dissection, medial degeneration, plus osteoarthritis (matching the human AOS phenotype) | Recessive in mouse, dominant in human | PMID:21217753 |
| ***Thsd4*^+/−** | Haploinsufficiency | *"Thsd4+/- mice showed progressive dilation of the thoracic aorta"*; medial degeneration and diffuse ECM disruption on histology | Mild | PMID:32855533 |
| ***Lox* knock-in (human allele)** | Missense | *"Mice homozygous for the human allele died shortly after parturition from ascending aortic aneurysm and spontaneous hemorrhage"*; disorganized aortic wall ultrastructure | Homozygous lethality limits adult study | PMID:27432961 |
| **SMC-specific *Mylk* knockdown** | Conditional | *"mice with SMC-specific knockdown of Mylk demonstrate altered gene expression and pathology consistent with medial degeneration of the aorta"* | Knockdown, not the human point mutation | PMID:21055718 |
| ***Acta2*^−/−**, ***Acta2*^R149C/+**, ***Myh11*^R247C/+** | Contractile-gene knock-in/knockout | Impaired contractility, medial changes; generally require a hemodynamic second hit (AngII infusion) to produce frank aneurysm | Weak baseline phenotype | Milewicz lab series |
| ***Col3a1*^+/− and knock-in** | vEDS alleles | Spontaneous arterial rupture and death | Very fragile animals | — |
| ***Fbln4*/*Efemp2* SMC-conditional KO** | Elastogenesis defect | Ascending aortic aneurysm and tortuosity | Recessive/conditional | — |

### 15.2 Induced (non-genetic) models

- **Angiotensin II infusion** (osmotic minipump, typically in *ApoE*^−/− or hyperlipidemic mice) — the workhorse for aneurysm and dissection; produces suprarenal abdominal and ascending aortic pathology. Widely used but arguably a better AAA than TAA model.
- **β-aminopropionitrile (BAPN) ± AngII** — LOX inhibition plus hemodynamic stress; reliably produces thoracic aortic dissection and rupture in young mice and rats. The most-used dedicated **dissection** model, and the direct pharmacological mimic of human *LOX* loss of function.
- **CaCl₂ periadventitial application**, **elastase perfusion** — mostly AAA models; occasionally adapted to the thoracic segment.
- **Copper-deficient / lathyrogen-fed avian models** — historic, but the origin of lysyl oxidase biology and directly relevant to the *LOX*-TAAD arm.

### 15.3 Non-mammalian and in vitro systems

- **Zebrafish (*Danio rerio*, NCBITaxon:7955)** — `fbn2b`/*fibrillin* and *tgfbr* morphants and mutants for developmental vascular patterning; rapid, transparent, good for variant functional screening; but no comparable high-pressure ascending aorta, so it cannot model the mechanical disease.
- **Human iPSC-derived vascular SMCs** — the most translationally informative in vitro platform. Critically, patient-derived iPSC-SMCs must be differentiated through the **correct developmental lineage** (cardiac neural crest for the root/ascending aorta) to reveal the phenotype; lateral-plate-mesoderm-derived SMCs from the same patient may appear normal. This lineage-specificity is itself the leading mechanistic explanation of segmental disease and should be modeled as a mechanism node.
- **Primary human aortic SMC and fibroblast cultures** from surgical specimens.
- **Aortic ring / ex vivo pressure-myograph biomechanics**, and engineered vascular tissue constructs.
- **Organ-on-chip** models applying cyclic stretch and physiologic shear to SMC/EC co-cultures.

### 15.4 Model limitations (important for `HUMAN_MODEL_MISMATCH` curation)

1. **The losartan translation failure.** Mouse *Fbn1*^C1039G/+ data (PMID:16601194) predicted losartan superiority over β-blockade; the human trial (PMID:25405392) found no difference. This is the canonical dismech `HUMAN_MODEL_MISMATCH` case for this disease.
2. **Direction-of-effect instability.** TGF-β neutralization *"either exacerbated or mitigated TAA formation depending on whether treatment was initiated before or after aneurysm formation"* (PMID:25614286) — a temporal confound largely absent from human trial design.
3. **Dominant human alleles behave recessively in mouse** (*Smad3*, *Lox*, *Fbln4*), so the mouse genotype often does not match the human one.
4. **Mice rarely dissect** without a chemical or hemodynamic second hit — so most models capture dilation but not the clinically decisive event.
5. **Scale and hemodynamics** — mouse aortic diameter is ~1 mm at ~100 mmHg with a ~600 bpm heart rate; wall stress, lamellar unit number, and cycle count differ by orders of magnitude from human.
6. **No model reproduces the decades-long human natural history** or the age-related degenerative form that accounts for the majority of clinical TAA.

### 15.5 Model resources

MGI (mouse), IMPC/KOMP (null alleles for all HTAD genes), IMSR and JAX (*Fbn1*^C1039G/+ is JAX #012885; *Fbn1*^mgR is available), MMRRC, EMMA, RGD (rat BAPN models), ZFIN (zebrafish), Cellosaurus/ATCC (human aortic SMC lines), Alliance of Genome Resources, and **OMIA** for the bovine Marfan and turkey aortic-rupture entries.

---

## Appendix A — Consolidated ontology term suggestions

**MONDO:** `MONDO:0005396` thoracic aortic aneurysm ✅ (primary `disease_term`); `MONDO:0019625` familial thoracic aortic aneurysm and aortic dissection ✅ (subtype/grouping mapping).

**HPO (all OAK-verified):** `HP:0012727` Thoracic aortic aneurysm · `HP:0004942` Aortic aneurysm · `HP:0002616` Aortic root aneurysm · `HP:0004970` Ascending tubular aorta aneurysm · `HP:0012728` Fusiform descending thoracic aortic aneurysm · `HP:0012729` Saccular descending thoracic aortic aneurysm · `HP:0002647` Aortic dissection · `HP:0031649` Aortic rupture · `HP:0001659` Aortic regurgitation · `HP:0001647` Bicuspid aortic valve · `HP:0001634` Mitral valve prolapse · `HP:0001643` Patent ductus arteriosus · `HP:0005116` Arterial tortuosity · `HP:0005112` Abdominal aortic aneurysm · `HP:0000822` Hypertension · `HP:0100749` Chest pain · `HP:0001609` Hoarse voice · `HP:0002015` Dysphagia · `HP:0002105` Hemoptysis · `HP:0001279` Syncope · `HP:0001699` Sudden death · `HP:0002140` Ischemic stroke · `HP:0002326` Transient ischemic attack.

**UBERON (all OAK-verified):** `UBERON:0001515` thoracic aorta · `UBERON:0001496` ascending aorta · `UBERON:0001508` arch of aorta · `UBERON:0003707` sinus of Valsalva · `UBERON:0000947` aorta · `UBERON:0002137` aortic valve · `UBERON:0003618` aorta tunica media · `UBERON:0002522` tunica media · `UBERON:0004178` aorta smooth muscle tissue · `UBERON:0004237` blood vessel smooth muscle.

**CL (all OAK-verified):** `CL:0000359` vascular associated smooth muscle cell · `CL:0000192` smooth muscle cell · `CL:0002139` endothelial cell of vascular tree · `CL:0000057` fibroblast · `CL:0000235` macrophage · `CL:0000084` T cell.

**GO (QuickGO-verified; re-run `just validate-terms` since the local GO db is corrupt):** `GO:0007179` transforming growth factor beta receptor signaling pathway · `GO:0006939` smooth muscle contraction · `GO:0030198` extracellular matrix organization · `GO:0030199` collagen fibril organization · `GO:0048251` elastic fiber assembly · `GO:0004720` protein-lysine 6-oxidase activity · `GO:0006954` inflammatory response · `GO:0006979` response to oxidative stress · `GO:0035904` aorta development · `GO:0014909` smooth muscle cell migration.

**NCIT (all OAK-verified):** `NCIT:C15986` Pharmacotherapy · `NCIT:C29576` Beta-Adrenergic Antagonist · `NCIT:C66930` Angiotensin II Receptor Antagonist · `NCIT:C15329` Surgical Procedure · `NCIT:C157839` Endovascular Aneurysm Repair · `NCIT:C50815` Aortic Valve Replacement · `NCIT:C202408` Computed Tomography Angiography · `NCIT:C157338` Multi-detector Computed Tomography Angiography · `NCIT:C190557` Magnetic Resonance Angiography · `NCIT:C80404` Transthoracic Echocardiography Test · `NCIT:C80405` Transesophageal Echocardiography Test · `NCIT:C16525` Echocardiography Test · `NCIT:C15709` Genetic Testing · `NCIT:C15240` Genetic Counseling · `NCIT:C15372` Smoking Cessation Intervention · `NCIT:C15747` Supportive Care · `NCIT:C49236` Therapeutic Procedure.

**CHEBI (OLS4-verified):** `CHEBI:6541` losartan · `CHEBI:2904` atenolol · `CHEBI:5959` irbesartan · `CHEBI:6904` metoprolol · `CHEBI:100241` ciprofloxacin (risk factor, not treatment).

**HGNC (genenames.org-verified; use lowercase `hgnc:` prefix in dismech):** `hgnc:3603` FBN1 · `hgnc:11772` TGFBR1 · `hgnc:11773` TGFBR2 · `hgnc:6769` SMAD3 · `hgnc:11768` TGFB2 · `hgnc:11769` TGFB3 · `hgnc:130` ACTA2 · `hgnc:7569` MYH11 · `hgnc:7590` MYLK · `hgnc:9414` PRKG1 · `hgnc:6664` LOX · `hgnc:2201` COL3A1 · `hgnc:13444` SLC2A10 · `hgnc:10896` SKI · `hgnc:3219` EFEMP2 · `hgnc:29673` MFAP5 · `hgnc:3808` FOXE3 · `hgnc:25835` THSD4 · `hgnc:6716` LTBP3 · `hgnc:7881` NOTCH1 · `hgnc:1044` BGN · `hgnc:3327` ELN · `hgnc:3754` FLNA · `hgnc:6768` SMAD2 · `hgnc:6770` SMAD4 · `hgnc:6904` MAT2A.

---

## Appendix B — Master citation list

| PMID | First author, year | Journal | Content | Evidence source |
|---|---|---|---|---|
| 36334952 | Isselbacher EM, 2022 | JACC | 2022 ACC/AHA Guideline for the Diagnosis and Management of Aortic Disease | HUMAN_CLINICAL |
| 38416090 / 38408364 | Czerny M, 2024 | Ann Thorac Surg / EJCTS | EACTS/STS Guidelines for the aortic organ | HUMAN_CLINICAL |
| 30071989 | Renard M, 2018 | JACC | ClinGen clinical validity of HTAAD genes | OTHER (expert curation) |
| 30763214 | Pinard A, 2019 | Circ Res | Genetics of thoracic and abdominal aortic diseases (review) | OTHER |
| 27297344 | Isselbacher EM, 2016 | Circulation | Hereditary influence in TAAD (review) | OTHER |
| 37308786 | (MVP), 2023 | Nat Genet | GWAS of TAAD in the Million Veteran Program; 21 loci | HUMAN_CLINICAL |
| 34837083 | Pirruccello JP, 2022 | Nat Genet | Deep learning genetic analysis of the thoracic aorta | HUMAN_CLINICAL |
| 17994018 | Guo DC, 2007 | Nat Genet | ACTA2 mutations cause TAAD (14% of inherited TAAD) | HUMAN_CLINICAL |
| 16444274 | Zhu L, 2006 | Nat Genet | MYH11 mutations, TAAD + PDA, dominant negative | HUMAN_CLINICAL |
| 21055718 | Wang L, 2010 | AJHG | MYLK mutations cause familial aortic dissections | HUMAN_CLINICAL |
| 23910461 | Guo DC, 2013 | AJHG | PRKG1 R177Q gain-of-function | HUMAN_CLINICAL |
| 27432961 | Lee VS, 2016 | PNAS | LOX loss-of-function causes TAAD | HUMAN_CLINICAL / MODEL_ORGANISM |
| 32855533 | Elbitar S, 2021 | Genet Med | THSD4/ADAMTSL6 haploinsufficiency | HUMAN_CLINICAL / MODEL_ORGANISM |
| 29625025 | Guo DC, 2018 | AJHG | LTBP3 pathogenic variants predispose to TAAD | HUMAN_CLINICAL |
| 15731757 | Loeys BL, 2005 | Nat Genet | TGFBR1/TGFBR2 — Loeys-Dietz syndrome | HUMAN_CLINICAL |
| 21217753 | van de Laar IM, 2011 | Nat Genet | SMAD3 — aneurysms-osteoarthritis syndrome | HUMAN_CLINICAL |
| 22772368 | Lindsay ME, 2012 | Nat Genet | TGFB2 loss of function; the TGF-β paradox | HUMAN_CLINICAL / MODEL_ORGANISM |
| 12598898 | Neptune ER, 2003 | Nat Genet | Dysregulated TGF-β activation in Marfan | MODEL_ORGANISM |
| 16601194 | Habashi JP, 2006 | Science | Losartan prevents aortic aneurysm in Marfan mice | MODEL_ORGANISM |
| 15254584 | Judge DP, 2004 | JCI | Haploinsufficiency in Marfan pathogenesis | MODEL_ORGANISM |
| 25614286 | Cook JR, 2015 | ATVB | Dimorphic TGF-β effects; combinatorial therapy | MODEL_ORGANISM |
| 20734336 | Milewicz DM, 2010 | Am J Med Genet A | ACTA2 R179H multisystemic smooth muscle dysfunction | HUMAN_CLINICAL |
| 16025100 | Garg V, 2005 | Nature | NOTCH1 mutations cause aortic valve disease | HUMAN_CLINICAL |
| 10706896 | Pepin M, 2000 | NEJM | Vascular EDS natural history; median survival 48 y | HUMAN_CLINICAL |
| 16996941 | Albornoz G, 2006 | Ann Thorac Surg | Familial TAA: 21.5% inherited, AD 76.9%, growth rates | HUMAN_CLINICAL |
| 11834007 | Davies RR, 2002 | Ann Thorac Surg | Yearly rupture/dissection rates by size | HUMAN_CLINICAL |
| 9851478 | Clouse WD, 1998 | JAMA | Olmsted County incidence 10.4/100,000; rupture by size | HUMAN_CLINICAL |
| 17145990 | Olsson C, 2006 | Circulation | Swedish national registry, >14,000 cases | HUMAN_CLINICAL |
| 10685714 | Hagan PG, 2000 | JAMA | IRAD: presentation and mortality of acute dissection | HUMAN_CLINICAL |
| 17709637 | Pape LA, 2007 | Circulation | 59% of type A dissections at <5.5 cm | HUMAN_CLINICAL |
| 33017217 | Li Y, 2020 | Circulation | scRNA-seq of human ascending TAA; 11 cell types, 40 subtypes | HUMAN_CLINICAL / IN_VITRO |
| 27031798 | Halushka MK, 2016 | Cardiovasc Pathol | SCVP/AECVP consensus on noninflammatory degenerative aortic pathology | OTHER |
| 25405392 | Lacro RV, 2014 | NEJM | Atenolol vs losartan in Marfan (PHN trial) | HUMAN_CLINICAL |
| 23999449 | Groenink M, 2013 | Eur Heart J | COMPARE: losartan reduces aortic dilatation rate | HUMAN_CLINICAL |
| 36049495 | Pitcher A, 2022 | Lancet | ARB + β-blocker IPD meta-analysis in Marfan | HUMAN_CLINICAL |
| 39317438 | van Andel MM, 2024 | Heart | Resveratrol single-arm trial in Marfan | HUMAN_CLINICAL |
| 29519881 | Pasternak B, 2018 | BMJ | Fluoroquinolones and aortic aneurysm/dissection | HUMAN_CLINICAL |
| 30046809 | LeMaire SA, 2018 | JAMA Surg | Ciprofloxacin and aortic dissection in mice | MODEL_ORGANISM |
| 20829218 | Gomez D, 2011 | Cardiovasc Res | Epigenetic control of SMC in Marfan/non-Marfan TAA | IN_VITRO / HUMAN_CLINICAL |
| 23814118 | Gomez D, 2013 | ATVB | Smad2-dependent PN-1; aneurysm vs dissection | HUMAN_CLINICAL |
| 26005802 | Franken R, 2015 | Int J Cardiol | Aortic tortuosity as a Marfan severity marker | HUMAN_CLINICAL |
| 29631804 | Selamet Tierney ES, 2018 | Am J Cardiol | Aortic stiffness predicts root growth in Marfan | HUMAN_CLINICAL |
| 36345977 | Oudin Åström D, 2022 | Glob Health Action | Temperature and incidence of surgery for type A dissection | HUMAN_CLINICAL |
| 12683625 | Waldrop JE, 2003 | J Vet Intern Med | Aortic dissection with aneurysms and posterior paresis in a dog | MODEL_ORGANISM |
| 29717986 | — , 2018 | (vet) | Dissecting aortic aneurysm with hypertension in a cat | MODEL_ORGANISM |

---

## Appendix C — Curation notes for the dismech entry

1. **Module conformance.** Declare `conforms_to: "aortopathy_tgfbeta_dysregulation#TGF-beta Signaling Dysregulation"` plus the medial-degeneration and progressive-dilation nodes. Do **not** conform to `atherogenesis` — PMID:37308786 explicitly establishes TAAD as non-atherosclerotic and distinct from other vascular disease. A `thrombogenesis` link is defensible only for false-lumen/mural thrombus nodes.
2. **Grouping membership.** The repo already carries a `Heritable_Thoracic_Aortic_Disease` grouping; the heritable subtypes of this entry should be consistent with its `NECESSARY` nested AND/OR phenotype criterion.
3. **Model the TGF-β paradox as a hypothesis, not a fact.** Use `mechanistic_hypotheses` with a stable `hypothesis_group_id` (e.g. `tgfb_excess_drives_aneurysm`) and opt the relevant `downstream[].hypothesis_groups` edges into it. Add a `discussions` entry with `kind: HUMAN_MODEL_MISMATCH` for the losartan mouse-to-human translation failure (PMID:16601194 → PMID:25405392), and a `KNOWLEDGE_GAP` for the unresolved direction-of-effect question (PMID:25614286, PMID:22772368).
4. **Prevalence records** must use `measure_type: ANNUAL_INCIDENCE` for the Olmsted/Swedish figures with `rate_per_100000` set to 10.4 / 16.3 / 9.1 — do not enter these as point prevalence.
5. **Subtypes worth modeling** (short, slug-friendly `name` values): `Sporadic`, `FTAAD`, `Marfan`, `LDS`, `vEDS`, `BAV-Aortopathy`, `Aortitis`, `Mycotic`, `MSMDS` (ACTA2 R179).
6. **`biological_scale` tags:** `MOLECULAR` for the fibrillin/TGF-β/actomyosin nodes; `CELLULAR` for SMC apoptosis and phenotypic modulation; `TISSUE` for medial degeneration and elastic fiber fragmentation; `ORGANISM` for dilation, dissection, rupture, and death.
7. **Frequency discipline.** Most snippets above support the *association* only. Do not attach a `frequency:` enum to a phenotype unless the cited abstract carries the number — several of the abstracts here do (e.g. 21.5% familial, 14% ACTA2, 59% <5.5 cm, 27.4% mortality) and those are legitimately quotable.
8. **Re-verify before committing.** Quotes marked *paraphrase* above (Renard 30071989, Lacro 25405392, Groenink 23999449, Lee 27432961, Milewicz 20734336, Pirruccello 34837083, Pitcher 36049495, Cook 25614286) were summarized by the fetch layer and must be re-pulled with `just fetch-reference PMID:xxxxx` and validated with `just validate-references` before being used as evidence `snippet:` values. Everything shown in full blockquote form was retrieved verbatim from `efetch`.

---

**Sources:**
- [PubMed E-utilities (esearch/esummary/efetch)](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/)
- [2022 ACC/AHA Guideline for the Diagnosis and Management of Aortic Disease — PubMed](https://pubmed.ncbi.nlm.nih.gov/36334952/) · [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC9876736/)
- [EACTS/STS Guidelines for Diagnosing and Treating Acute and Chronic Syndromes of the Aortic Organ — PubMed](https://pubmed.ncbi.nlm.nih.gov/38416090/)
- [Genome-wide association study of TAAD in the Million Veteran Program — Nature Genetics](https://www.nature.com/articles/s41588-023-01420-z)
- [Deep learning enables genetic analysis of the human thoracic aorta — Nature Genetics](https://www.nature.com/articles/s41588-021-00962-4)
- [Current understanding of the genetics of thoracic aortic disease — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12058223/)
- [Heritable Thoracic Aortic Disease Overview — GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1120/)
- [Angiotensin receptor blockers and β blockers in Marfan syndrome — The Lancet](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(22)01534-3/fulltext)
- [Thrombosis, Embolism, Aneurysm, and Dissection in Animals — Merck Veterinary Manual](https://www.merckvetmanual.com/circulatory-system/thrombosis-embolism-aneurysm-and-dissection/thrombosis-embolism-aneurysm-and-dissection-in-animals)
- [Valve-sparing aortic root replacement (David I) in Marfan disease — EJCTS](https://academic.oup.com/ejcts/article/55/3/476/5087799)
- [QuickGO](https://www.ebi.ac.uk/QuickGO/) · [OLS4](https://www.ebi.ac.uk/ols4/) · [HGNC REST](https://rest.genenames.org/) · local OAK (`sqlite:obo:hp`, `uberon`, `cl`, `ncit`, `mondo`)