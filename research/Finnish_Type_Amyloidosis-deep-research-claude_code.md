---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-21T16:24:53.004300'
end_time: '2026-08-21T16:29:49.249368'
duration_seconds: 296.25
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Finnish Type Amyloidosis
  mondo_id: ''
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
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 16
  num_turns: 15
  total_cost_usd: 1.8761004000000001
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 48
reference_validation:
  total_references: 36
  verified: 36
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 36
  on_topic: 25
  off_topic: 1
  off_topic_references:
  - PMID:33375500
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Finnish Type Amyloidosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Finnish Type Amyloidosis** covering all of the
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

# Finnish Type Amyloidosis (Gelsolin/AGel Amyloidosis) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Finnish type amyloidosis — now most often called **hereditary gelsolin amyloidosis (AGel amyloidosis)**, and historically known as **Meretoja syndrome** or **familial amyloidosis, Finnish type (FAF)** — is an autosomal dominant systemic amyloidosis caused by variants in the *GSN* (gelsolin) gene. It is defined clinically by a distinctive triad: progressive **lattice corneal dystrophy**, **cranial (especially facial) neuropathy**, and **cutis laxa** (loose, sagging skin), sometimes with later peripheral neuropathy, cardiac conduction disease, and renal involvement in a minority of patients ([OMIM #105120](https://www.omim.org/entry/105120); [Orphanet ORPHA:85448](https://www.orpha.net/consor/cgi-bin/Disease_Genes.php?lng=EN&data_id=16170)). It is one of the founder diseases of the "Finnish disease heritage," first described by the Finnish ophthalmologist Jouko Meretoja in 1969.

**Key identifiers:**
- **OMIM disease:** #105120 — "Amyloidosis, Finnish type" / Lattice corneal dystrophy type II / FAP IV
- **OMIM gene:** *137350 — GELSOLIN; GSN* (chromosome 9q33.2)
- **Orphanet:** ORPHA:85448 (AGel amyloidosis); gene page GSN
- **MONDO:** MONDO:0007097
- **HGNC:** GSN (HGNC:4620)
- **ICD-10:** E85.4 (Organ-limited amyloidosis) is commonly applied; some coding schemes use E85.8 (Other amyloidosis)
- **MeSH:** "Amyloidosis, Familial" (D000687) with the Finnish-type subheading; corneal component indexed under "Corneal Dystrophies, Hereditary" and lattice type II

**Synonyms:** Familial amyloidosis, Finnish type (FAF); Familial amyloid polyneuropathy type IV (FAP IV, an older classification alongside TTR-related FAP I–III); Meretoja syndrome; Meretoja disease; AGel amyloidosis; Gelsolin amyloidosis; Lattice corneal dystrophy type II (LCD2); Amyloidosis V.

**Data provenance.** Information below is derived primarily from **aggregated disease-level resources** (OMIM, Orphanet, GeneReviews-style literature reviews) and from **clinical cohort studies conducted on the Finnish national patient registry** — most notably the large Finnish cohort assembled by Kiuru-Enari, Haltia, and colleagues at Helsinki University Hospital, which has followed several hundred genetically confirmed Finnish AGel patients and their causes of death over decades ([Kiuru-Enari & Haltia, 2013, PMID:23931809](https://pubmed.ncbi.nlm.nih.gov/23931809/); [Schmidt et al. 2016, PMID:27137880](https://pubmed.ncbi.nlm.nih.gov/27137880/); [Atula/Kiuru-Enari FIN-GAR 2020, PMID:31952544](https://pubmed.ncbi.nlm.nih.gov/31952544/)). Individual case reports (e.g., novel *GSN* variants in single kindreds) supplement this for genotype-phenotype diversity outside Finland.

---

## 2. Etiology

**Disease causal factor.** AGel amyloidosis is a **monogenic, autosomal dominant proteinopathy**. Heterozygous (and rarely homozygous) missense variants in *GSN* — most commonly **c.640G>A (p.Asp187Asn / D187N)**, the "Finnish" variant, historically also written G654A in older cDNA numbering — destabilize the calcium-binding site of gelsolin domain 2 (G2), rendering plasma gelsolin susceptible to aberrant intracellular proteolysis and the generation of amyloidogenic fragments. There is no environmental or infectious cause; the disease is entirely genetically determined, though **age** is a major modifier of onset and severity, and **gene dosage (heterozygous vs. rare homozygous)** modifies severity, particularly renal disease.

**Genetic risk factors:**
- **Causal variant (Finnish founder):** *GSN* c.640G>A, p.Asp187Asn (D187N). Haplotype analysis of 62 unrelated Finnish AGel families shows they share a common ancestral haplotype, consistent with a single Finnish founder mutation rather than recurrent mutation, despite c.640G being a documented mutational hotspot ([Mustonen et al. 2018, PMC5838978](https://pmc.ncbi.nlm.nih.gov/articles/PMC5838978/); *Eur J Hum Genet*). Notably, the identical nucleotide substitution (G654A in old numbering) has arisen **independently** in Japanese families, on a different haplotype background ([Paunio et al. 1995, PMID:7550233](https://pubmed.ncbi.nlm.nih.gov/7550233/); [Kiuru et al. 2012, PMID:22622774](https://pubmed.ncbi.nlm.nih.gov/22622774/)).
- **Allelic/non-Finnish variants at the same codon:** c.640G>T, p.Asp187Tyr (D187Y) — the "Danish" variant, first reported in a Danish family and since found in a Czech family and a Brazilian kindred, with a clinically similar but sometimes distinguishable phenotype ([Gorevic et al./Maury 2000, PMID:10767822](https://pubmed.ncbi.nlm.nih.gov/10767822/); Brazilian case series, [PMID:22068858](https://pubmed.ncbi.nlm.nih.gov/22068858/)).
- **Novel/rare amyloidogenic variants elsewhere in GSN** identified since ~2013 broaden the molecular spectrum beyond codon 187, generally in domain G1 or G2 and producing variably milder or renal-predominant phenotypes: p.Asn184Lys (N184K, renal-predominant; [Efebera/Rezvani et al. 2016, PMC5025852](https://pmc.ncbi.nlm.nih.gov/articles/PMC5025852/)), p.Asn211Lys (N211K, nephrotic syndrome/thrombotic microangiopathy kindred; [PMID:24601799](https://pubmed.ncbi.nlm.nih.gov/24601799/)), p.Gly167Arg, p.Gly180Trp/Ser, p.Tyr447His (associated with autonomic/peripheral neuropathy predominant disease; [PMID:37140928](https://pubmed.ncbi.nlm.nih.gov/37140928/)), and p.Glu580Lys ([PMID:33375500-range, PMC7865823](https://pmc.ncbi.nlm.nih.gov/articles/PMC7865823/)).
- **Zygosity as a severity modifier:** rare homozygous D187N patients (from consanguineous or double-founder matings) have markedly earlier, more severe disease, especially nephrotic-range proteinuria progressing to end-stage renal disease, whereas renal failure is uncommon in heterozygotes.
- **No known genetic susceptibility/modifier loci** beyond *GSN* itself have been robustly established; the phenotype is highly penetrant.

**Environmental/lifestyle risk factors:** None established as causal. Ultraviolet/mechanical stress to skin and cornea may exacerbate local manifestations (erosions, skin fragility) but does not cause the underlying amyloidogenesis.

**Protective factors:** No validated protective genetic or environmental factors are described in the literature. There is no evidence of incomplete penetrance modifiers analogous to *APOE* in Alzheimer disease or the transthyretin-stabilizing tafamidis mechanism for ATTR amyloidosis.

**Gene-environment interaction:** Not documented as a mechanistic feature; the disorder behaves as a highly penetrant single-gene disease. Sex is a modifier of clinical course rather than a strict gene-environment interaction (see §9, §11): a Finnish cohort study found gender differences in disease course and complication profile ([Kiuru-Enari et al., PMID:26805765](https://www.ncbi.nlm.nih.gov/pubmed/26805765)).

---

## 3. Phenotypes

The disease produces a **triad of ophthalmologic, neurologic, and dermatologic** manifestations, typically emerging sequentially over decades, plus less common systemic (renal, cardiac) involvement.

| Phenotype | Type | Onset | Frequency | Notes / suggested HP term |
|---|---|---|---|---|
| Lattice corneal dystrophy (bilateral, delicate branching amyloid lattice lines in corneal stroma) | Clinical sign | Usually first manifestation, mean age ~30s–40s | Nearly universal (first and defining sign) | HP:0025336 *Lattice corneal dystrophy* (or broader HP:0000578 *Corneal dystrophy*) |
| Recurrent corneal erosions | Symptom | Following corneal deposits | Frequent | HP:0500089 (or general "corneal erosion") |
| Progressive visual impairment | Symptom | Progressive from corneal lattice onset | Frequent, variable severity | HP:0000505 *Visual impairment* |
| Bilateral facial nerve palsy (cranial neuropathy) | Clinical sign | Onset typically 4th–5th decade, progressive | Very frequent, near-universal in advanced disease | HP:0010628 *Facial palsy* / HP:0006829 (peripheral facial nerve palsy) |
| Bulbar signs (dysarthria, dysphagia, masticatory weakness) | Clinical sign | Later disease | Frequent | HP:0002483/HP:0002015 *Dysphagia* |
| Cutis laxa / loose, sagging, "hound-dog" facial skin | Clinical sign | Middle age onward | Frequent, characteristic | HP:0000973 *Cutis laxa* |
| Dry, itchy, fragile skin | Symptom | Middle age onward | Frequent | HP:0000958 *Dry skin* |
| Peripheral (sensorimotor) polyneuropathy | Clinical sign | Later, after cranial neuropathy | Occasional–frequent, milder than cranial component | HP:0009830 *Peripheral neuropathy* |
| Autonomic neuropathy (orthostatic hypotension, GI dysmotility) | Clinical sign | Later disease | Occasional, reported particularly with Y447H variant | HP:0001611 (autonomic dysfunction terms) |
| Carpal tunnel syndrome | Clinical sign | Variable | Reported | HP:0100022 |
| Nephrotic-range proteinuria / progressive CKD | Laboratory / clinical | Later, more common in homozygotes and some non-D187 variants | Uncommon overall in heterozygous FAF, but significant cause of death when present | HP:0000100 *Nephrotic syndrome*; HP:0012622 *Chronic kidney disease* |
| Cardiac conduction abnormalities / arrhythmia | Clinical sign | Later disease | Reported in a subset | HP:0011675 *Arrhythmia* |
| "Sad," mask-like facial appearance from combined facial diplegia and cutis laxa | Clinical sign | Advanced disease | Characteristic, frequent | (descriptive; may combine facial palsy + cutis laxa terms) |
| Xerostomia / dry mouth | Symptom | Variable | Reported | HP:0000217 |

**Onset/course.** Mean age of first symptom onset in the large Finnish cohort is **~39 years**, with ophthalmologic (corneal) findings almost always first, followed over subsequent decades by cranial neuropathy and cutaneous changes ("Common origin..." cohort description, [PMC5838978](https://pmc.ncbi.nlm.nih.gov/articles/PMC5838978/); [Kiuru-Enari & Haltia 2013, PMID:23931809](https://pubmed.ncbi.nlm.nih.gov/23931809/)). The disease course is slowly **progressive** over decades rather than episodic; severity is variable between individuals and between the D187N/D187Y and rarer non-canonical variants.

**Quality of life impact.** The FIN-GAR phase II natural-history/burden study explicitly measured disease burden in genetically confirmed Finnish AGel patients and found **significant impact on quality of life** (visual disability, facial disfigurement/social impact from facial diplegia and cutis laxa, and neuropathic symptoms) even though overall **survival was not significantly reduced** ([Atula, Kiuru-Enari et al. 2020, PMID:31952544, *Orphanet J Rare Dis*](https://ojrd.biomedcentral.com/articles/10.1186/s13023-020-1300-5)). Vision loss from recurrent corneal lattice deposition/erosion and facial diplegia (impairing speech, chewing, and facial expression) are the dominant drivers of quality-of-life burden; dry, sagging skin has psychosocial/cosmetic impact.

---

## 4. Genetic / Molecular Information

**Causal gene.** *GSN* (gelsolin), HGNC:4620, chromosome **9q33.2**, OMIM gene *137350. GSN encodes a **calcium-regulated, actin-binding protein** with three isoforms (cytoplasmic gelsolin, secreted plasma gelsolin, and a mitochondrial/gelsolin-3 isoform), built from **six homologous gelsolin-like domains (G1–G6)** that, in the calcium-free state, pack into a compact globular structure; calcium binding triggers conformational changes exposing actin-severing/capping/nucleating surfaces (GeneCards; Expert Rev Mol Med gelsolin structure review). Plasma gelsolin (the isoform relevant to AGel amyloidosis) circulates extracellularly and participates in actin filament severing/depolymerization, e.g., during tissue injury and inflammation ("actin scavenger system").

**Pathogenic variant (primary):**
- **Gene/HGNC:** GSN, HGNC:4620
- **Variant:** c.640G>A (legacy numbering c.654G>A), **p.Asp187Asn (D187N)** — the Finnish founder variant
- **Classification (ACMG/ClinVar):** Pathogenic; ClinVar entries document D187N and D187Y as pathogenic for "Finnish type amyloidosis"
- **Variant type:** Missense, located in gelsolin domain 2 (G2), within/adjacent to the calcium-binding loop
- **Allele frequency:** Essentially absent from general population reference panels (gnomAD) except as extremely rare private/founder alleles; not a common polymorphism — consistent with a rare, highly penetrant autosomal dominant disease allele.
- **Origin:** Germline (heritable); not somatic. A single ancestral Finnish founder haplotype has been demonstrated across 62 unrelated Finnish families ([PMC5838978](https://pmc.ncbi.nlm.nih.gov/articles/PMC5838978/)); the same nucleotide change arose independently in Japan ([PMID:7550233](https://pubmed.ncbi.nlm.nih.gov/7550233/)).
- **Functional consequence:** The D187N/D187Y substitutions **impair Ca²⁺ binding by gelsolin domain G2**, destabilizing the domain and rendering it a substrate for **furin** cleavage in the trans-Golgi network — the first of two sequential proteolytic events (see §6). This is best classified as a **destabilizing, gain-of-toxic-function** mechanism (aberrant proteolysis → amyloidogenic peptide generation) rather than simple loss of gelsolin's normal actin-regulatory function, although reduced circulating functional gelsolin (an actin-scavenging deficit) may also contribute.

**Allelic/non-canonical variants:** D187Y (Danish), N184K, N211K, G167R, G180W/S, Y447H, E580K, and other more recently described *GSN* missense variants (largely in domain G1/G2) — collectively "gelsolin amyloidosis, non-Finnish/non-classic variants" — produce phenotypes ranging from classic FAF-like disease to renal-predominant or peripheral/autonomic-neuropathy–predominant presentations ([review: "A molecular perspective of gelsolin amyloidosis," *Cell Mol Life Sci*, 2026](https://link.springer.com/article/10.1007/s00018-026-06172-7); [PMID:37140928](https://pubmed.ncbi.nlm.nih.gov/37140928/)).

**Modifier genes:** None robustly established; zygosity at the *GSN* locus itself (heterozygous vs. homozygous) is the clearest modifier of severity, particularly for renal disease.

**Epigenetic information:** No disease-specific epigenetic (DNA methylation/histone) mechanism has been described; the pathogenesis is driven by post-translational proteolytic processing of the mutant protein, not altered gene expression/epigenetic regulation.

**Chromosomal abnormalities:** None — this is a point-mutation (missense) disorder, not a copy-number or structural chromosomal disease.

---

## 5. Environmental Information

AGel amyloidosis is a purely **genetic** disorder; no environmental toxin, occupational exposure, dietary factor, or infectious agent is causally implicated.

- **Environmental factors:** Not applicable as disease causes. Physical/mechanical trauma to the eye (contact lens wear, ocular surface stress) may precipitate corneal erosions in patients with established lattice deposits, but does not initiate the amyloidogenic process.
- **Lifestyle factors:** No specific lifestyle risk-modifying factor (smoking, diet, alcohol, exercise) has been studied or implicated for onset or progression in the literature identified.
- **Infectious agents:** Not applicable — non-infectious, non-communicable.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Germline missense variant in GSN domain G2** (classically D187N/D187Y) destabilizes the domain's calcium-binding loop.
2. In the wild-type protein, **Ca²⁺ binding stabilizes gelsolin domain G2** against unfolding and proteolysis; the FAF variant proteins are **unable to bind/be stabilized by Ca²⁺** in the trans-Golgi network as the nascent protein transits the secretory pathway ([Chen, Wei, Robinson 2001, "Furin initiates gelsolin familial amyloidosis in the Golgi through a defect in Ca²⁺ stabilization," PMID:11707399](https://pubmed.ncbi.nlm.nih.gov/11707399/); [Kazmirski/Robinson 2003, PMID:14596804](https://pubmed.ncbi.nlm.nih.gov/14596804/)).
3. This local unfolding exposes a cryptic cleavage site to **furin** (a proprotein convertase resident in the trans-Golgi network), producing an initial **intracellular furin cleavage event**.
4. The resulting furin-cleaved fragment, once secreted, undergoes a **second, extracellular proteolytic event mediated by MT1-MMP (membrane-type 1 matrix metalloproteinase)**-like activity, generating **intrinsically disordered, aggregation-prone amyloidogenic peptides of ~8 kDa and ~5 kDa** spanning the "gelsolin amyloidogenic core" around residues 173–243 (containing residues 182–192), historically termed the "C-fragment"/AGel peptide.
5. These peptides misfold into **cross-β amyloid fibrils** which deposit extracellularly, especially in **blood vessels and basement membranes**, and are demonstrable immunohistochemically with anti-gelsolin antibodies in the cornea, skin, peripheral/cranial nerve, kidney, heart, thyroid, salivary gland, and rectum ([immunohistochemistry review, PMID:1315488](https://pubmed.ncbi.nlm.nih.gov/1315488/); [PMC7865823](https://pmc.ncbi.nlm.nih.gov/articles/PMC7865823/)).
6. Amyloid deposition in the **corneal stroma** produces the lattice dystrophy pattern via subepithelial/stromal fibril accumulation and recurrent breakdown of corneal nerve and epithelial integrity (recurrent erosions). Deposition around and within **cranial (especially facial) nerve fascicles and perineurium** produces progressive cranial neuropathy/facial diplegia and bulbar signs. Deposition in the **dermis (vessel walls and around adnexal/elastic structures)** disrupts normal dermal architecture producing **cutis laxa** and skin fragility. In a minority of patients (more so with homozygosity or certain non-D187 variants), deposition in **glomerular capillary walls and mesangium** produces nephrotic-range proteinuria and progressive CKD ([Mayo Clinic renal AGel series, PMID:28139293](https://www.ncbi.nlm.nih.gov/pubmed/28139293)).
7. A separate, **downstream, age-associated intracellular consequence** demonstrated in a D187N transgenic mouse model is progressive compromise of **cellular proteostasis**: secretion of amyloidogenic gelsolin appears to exacerbate age-related decline in protein homeostasis, with intracellular co-aggregation of other proteins in skeletal muscle rough endoplasmic reticulum, resembling sporadic inclusion body myositis pathology ([PNAS 2009, PMID/PMC via "Secretion of amyloidogenic gelsolin progressively compromises protein homeostasis..."](https://www.pnas.org/doi/10.1073/pnas.0811753106); [PMC4461228](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4461228/)).

**Upstream vs. downstream:** The rate-limiting, disease-initiating event is the **Ca²⁺-binding defect → furin cleavage** step (intracellular, Golgi); this is upstream of the **MT1-MMP extracellular cleavage** step, which is itself upstream of **fibril nucleation/aggregation** and finally **tissue-specific amyloid deposition and organ dysfunction**.

**Cell types and biological processes involved:**
- Hepatocytes (primary site of plasma gelsolin synthesis/secretion) — trans-Golgi processing defect
- Corneal keratocytes/stromal fibroblasts and corneal epithelium — site of lattice deposit accumulation
- Schwann cells and perineurial cells of cranial/peripheral nerves — amyloid deposition around nerve fascicles
- Dermal fibroblasts, vascular endothelium, and elastic fiber–associated cells of skin — cutis laxa pathogenesis
- Glomerular endothelial cells, mesangial cells, and podocytes — renal amyloid deposition
- Vascular smooth muscle/endothelium generally, since amyloid preferentially deposits in **vessel walls and basement membranes** throughout the body

**Suggested GO terms:** GO:0003779 (actin binding), GO:0005509 (calcium ion binding), GO:0051015 (actin filament binding), GO:0030036 (actin cytoskeleton organization), GO:0006508 (proteolysis), GO:0034205 (amyloid-beta formation — generic amyloid fibril formation analog term may be better represented by a protein-misfolding/amyloid fibril formation GO term if available), GO:0043687 (post-translational protein modification).
**Suggested CL terms:** CL:0000186 (myofibroblast) or CL:0002620 (skin fibroblast) for dermal involvement; CL:0002573 (Schwann cell) for cranial/peripheral nerve; CL:0000653 (podocyte) and CL:0000650 (mesangial cell) for renal involvement; CL:0000312 (keratocyte) for corneal stroma.

**Protein dysfunction:** Classic **protein misfolding/aggregation** disorder — the pathogenic mechanism is aberrant proteolytic processing exposing an amyloidogenic peptide core, i.e., **gain-of-toxic-function via generation of an aggregation-prone fragment**, distinct from simple loss-of-function of full-length gelsolin's actin-regulatory role (though reduced normal plasma gelsolin function may compound tissue vulnerability to actin-mediated injury).

**Molecular profiling / omics:** No large-scale transcriptomic, proteomic, or single-cell atlas specific to AGel amyloidosis was identified in this search; most molecular characterization comes from targeted biochemical/structural studies (recombinant domain constructs, X-ray crystallography of gelsolin domains, and **mass spectrometry-based amyloid typing on renal/tissue biopsies**, which is now the standard method to confirm gelsolin as the amyloid precursor in atypical/renal presentations, e.g. [PMID:28139293](https://www.ncbi.nlm.nih.gov/pubmed/28139293)).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Eye (cornea), peripheral/cranial nervous system (especially facial nerve, also trigeminal and other cranial nerves; later peripheral nerves), skin
- **Secondary/systemic (minority of patients):** Kidney (glomeruli), heart (conduction system), and, per immunohistochemical surveys, amyloid deposits are also demonstrable in thyroid, salivary gland, and rectal mucosa without necessarily causing overt organ failure at those sites.
- **Body systems involved:** Ophthalmologic, peripheral/cranial nervous system, integumentary (dermatologic), and — in a minority — renal and cardiovascular systems.

**Tissue/cell level:**
- Corneal stroma (amyloid lattice lines), corneal epithelium (recurrent erosion)
- Peripheral nerve/cranial nerve perineurium and endoneurium; facial nerve fascicles specifically
- Dermis: vessel walls, perivascular and periadnexal connective tissue, elastic fibers (cutis laxa)
- Renal glomeruli: mesangium and capillary walls (light-microscopic Congo red–positive deposits largely confined to glomeruli, rarely extending to interstitium/vessel walls)
- Vascular smooth muscle/basement membranes broadly (amyloid has a systemic tropism for vasculature and basement membranes)

**Subcellular level:** The disease-initiating proteolytic event occurs in the **trans-Golgi network** (furin cleavage) of gelsolin-secreting cells (notably hepatocytes), followed by an **extracellular/plasma membrane–associated** MT1-MMP cleavage step. Suggested GO Cellular Component terms: GO:0005802 (trans-Golgi network), GO:0005576 (extracellular region), GO:0005886 (plasma membrane, site of MT1-MMP activity).

**Localization/laterality:** Ocular and facial nerve/skin involvement is characteristically **bilateral and roughly symmetric** (bilateral lattice corneal dystrophy, bilateral facial diplegia), consistent with a systemic circulating-precursor amyloidosis rather than a focal/unilateral process.

**Suggested UBERON terms:** UBERON:0000965 (cornea), UBERON:0001528 (facial nerve; or the broader UBERON:0001780 cranial nerve), UBERON:0002097 (skin of body), UBERON:0002113 (kidney), UBERON:0002330 (exocrine gland).

---

## 8. Temporal Development

**Onset:** Adult-onset disease; mean age of first (ophthalmologic) symptom onset is **~39 years** in the Finnish cohort ([PMC5838978](https://pmc.ncbi.nlm.nih.gov/articles/PMC5838978/)). Corneal lattice dystrophy is typically the presenting sign, diagnosed by an ophthalmologist, often before systemic disease is suspected. Onset pattern is **insidious/gradual**, not acute.

**Progression:** The disease follows a **chronic, slowly progressive** course over decades:
1. Early stage — corneal lattice dystrophy with recurrent erosions, still-preserved vision
2. Intermediate stage — emerging cranial neuropathy (facial nerve palsy, bulbar signs), progressive corneal opacification/visual loss, developing cutis laxa
3. Advanced stage — established facial diplegia, marked skin laxity/fragility, peripheral neuropathy, and, in a subset, renal impairment/nephrotic syndrome or cardiac conduction disease

Progression rate is **slow** relative to many other systemic amyloidoses (e.g., AL amyloidosis); the disease is compatible with a near-normal lifespan in most patients (see §11).

**Patterns:** No spontaneous remission is described — this is a genetically determined, progressive protein-deposition disease. There is no known "critical window" for intervention analogous to newborn screening/early enzyme-replacement diseases, since no disease-modifying therapy currently exists (see §12); the practical "critical period" is early recognition (via corneal lattice dystrophy) to enable proactive symptomatic management and genetic counseling before major cranial neuropathy/renal disease develops.

---

## 9. Inheritance and Population

**Epidemiology.**
- Estimated **600–1,000 affected individuals in Finland**, making it one of the most prevalent components of the "Finnish disease heritage" (a set of ~40 rare monogenic diseases enriched in Finland due to population bottleneck/founder effects).
- Prevalence of the causal mutation is **higher in Finland than anywhere else in the world**, though individual patients/kindreds have been reported globally (Japan, Denmark, Czech Republic, USA, Brazil, and other countries) via independent mutational origin (Japan) or apparent descendant/isolated founder events (Danish D187Y lineage).
- No formal global incidence/prevalence-per-100,000 figure outside Finland was identified in this search; the disease is considered ultra-rare worldwide outside the Finnish founder population.

**Inheritance pattern:** **Autosomal dominant.** Rare **homozygous** cases (from unions of two heterozygous carriers, more plausible in a founder population with elevated carrier frequency) produce a more severe phenotype, particularly renal.

**Penetrance:** Effectively **complete/high penetrance** for the classic D187N Finnish variant — essentially all carriers develop at least corneal lattice dystrophy by mid-adulthood, though severity and rate of progression of neurologic/dermatologic/renal manifestations are **variable (variable expressivity)**.

**Genetic anticipation:** Not reported as a feature of this disease (it is a simple missense point mutation, not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically documented in the literature reviewed.

**Founder effect:** Strongly established. Haplotype analysis of **62 unrelated Finnish AGel families** demonstrates a shared ancestral haplotype around the *GSN* c.640G locus, consistent with a **single common Finnish founder** for the D187N mutation, distinct from the haplotype background on which the identical nucleotide change arose independently in Japanese families ([PMC5838978](https://pmc.ncbi.nlm.nih.gov/articles/PMC5838978/); [PMID:7550233](https://pubmed.ncbi.nlm.nih.gov/7550233/)).

**Consanguinity:** Relevant to the rare homozygous cases, which arise more readily in the genetically isolated Finnish founder population where carrier frequency is elevated.

**Carrier frequency:** Not given as a precise population allele frequency in the sources reviewed, but consistent with several hundred to ~1,000 clinically affected heterozygotes concentrated in Finland.

**Population demographics:**
- **Geographic distribution:** Endemic in Finland; scattered case reports/kindreds elsewhere (Japan — independent founder; Denmark, Czech Republic, Brazil — D187Y lineage; USA — reported American kindred with D187N, [PMID cosegregation study, PMC1683143](https://pmc.ncbi.nlm.nih.gov/articles/PMC1683143/)).
- **Sex ratio:** Autosomal — no inherent sex-linked transmission bias, but the Finnish cohort demonstrates **gender differences in clinical course** (renal complications overrepresented as immediate cause of death in **female** patients; overall mean lifespan differs modestly by sex within the disease cohort — 73.9 years for men vs. 78.0 years for women — figures that track general-population sex differences in Finland (72.1/80.1 years) ([Kiuru-Enari et al., PMID:26805765](https://www.ncbi.nlm.nih.gov/pubmed/26805765); [Schmidt et al. 2016, PMID:27137880](https://pubmed.ncbi.nlm.nih.gov/27137880/)).
- **Age distribution:** Adult disease; symptoms emerge from the third/fourth decade onward and progress through late life.

---

## 10. Diagnostics

**Clinical tests:**
- **Slit-lamp ophthalmologic examination** — visualization of the characteristic bilateral lattice corneal dystrophy pattern (fine branching refractile lines in the corneal stroma), frequently the initial diagnostic clue, especially when it presents atypically (mid-peripheral, adult-onset, negative family history) — a pattern that should prompt exclusion of *TGFBI* (LCD type I) mutations and consideration of systemic/paraprotein-associated amyloidosis.
- **Skin/nerve/renal biopsy with Congo red staining** — amyloid deposits show classic **apple-green birefringence under polarized light**; immunohistochemistry with anti-gelsolin antiserum can localize gelsolin-derived amyloid in cornea, skin, kidney, heart, thyroid, salivary gland, and rectum.
- **Mass spectrometry-based proteomic typing of amyloid deposits** (laser microdissection + tandem MS) — now the reference method, especially for atypical/renal presentations, to confirm gelsolin (rather than AL/ATTR/AA) as the amyloid precursor protein ([Mayo Clinic renal series, PMID:28139293](https://www.ncbi.nlm.nih.gov/pubmed/28139293)).
- **Electrophysiologic studies** (facial nerve conduction studies, EMG/nerve conduction studies for peripheral neuropathy) to characterize cranial/peripheral neuropathy.
- **Urinalysis / 24-hour proteinuria and renal function panel** — to screen for nephrotic-range proteinuria/CKD, particularly in homozygotes or those with a family history of renal disease.
- **ECG/Holter monitoring** — for cardiac conduction abnormalities in a subset of patients.

**Genetic testing:** The definitive diagnostic test is **targeted *GSN* gene sequencing** (single-gene Sanger sequencing of the relevant exon(s), or inclusion of *GSN* on a corneal-dystrophy/hereditary-amyloidosis/peripheral-neuropathy gene panel, or as an incidental/confirmatory finding on whole-exome/whole-genome sequencing) to identify the D187N (or other pathogenic) variant. Because the Finnish founder variant is well characterized, **targeted single-variant testing** is efficient and cost-effective in patients of Finnish ancestry with the classic triad; broader panel/WES testing is more appropriate for atypical presentations (e.g., isolated nephrotic syndrome, non-Finnish ancestry) where a novel *GSN* variant or an entirely different amyloidosis (AL, ATTR) must be distinguished.

**Differential diagnosis:**
- **Lattice corneal dystrophy type I** (and related *TGFBI*/keratoepithelin-associated corneal dystrophies, OMIM #122200) — distinguished by earlier onset, no systemic amyloidosis, and a *TGFBI* rather than *GSN* mutation.
- **Acquired/paraprotein-associated (AL) corneal or systemic amyloidosis** — atypical adult-onset lattice dystrophy with negative *TGFBI* and *GSN* testing should prompt evaluation for a plasma cell dyscrasia (serum/urine immunofixation, free light chains) given case reports of heavy-chain/AL amyloidosis mimicking lattice dystrophy ([PMID:21743312](https://pubmed.ncbi.nlm.nih.gov/21743312/)).
- Other hereditary neuropathies with facial diplegia (e.g., Möbius syndrome, myotonic dystrophy) — distinguished by the corneal and dermatologic findings and by molecular testing.
- Cutis laxa syndromes of other genetic causes (e.g., *ELN*, *FBLN5*, *ATP6V0A2*-related cutis laxa) — distinguished by the absence of corneal/neurologic amyloid triad and by *GSN* sequencing.
- Other hereditary systemic amyloidoses (ATTR, AApoAI, AFib) — distinguished by tissue amyloid typing (mass spectrometry or genetic testing) and by the distinctive corneal/facial phenotype of AGel amyloidosis, which is not typical of ATTR/AApoAI.

**Screening:** No population newborn-screening program exists (adult-onset disease). **Cascade genetic testing/predictive testing** of at-risk relatives in known Finnish families is the practical screening approach, paired with genetic counseling given full penetrance and autosomal dominant transmission.

---

## 11. Outcome / Prognosis

**Survival and mortality.** In contrast to many systemic amyloidoses, AGel amyloidosis is characterized by a **near-normal, or only mildly reduced, lifespan**. In a study of 272 deceased Finnish AGel patients:
- Mean lifespan was **73.9 years for men** and **78.0 years for women**, compared with **72.1 and 80.1 years**, respectively, for the age- and sex-matched general Finnish population — i.e., the disease did **not substantially shorten lifespan**, at least through age 75 ([Schmidt et al. 2016, "Causes of death and life span in Finnish gelsolin amyloidosis," PMID:27137880](https://pubmed.ncbi.nlm.nih.gov/27137880/)).
- **AGel amyloidosis was the underlying cause of death in ~20% of patients.**
- **Renal complications were overrepresented as the immediate cause of death in female patients.**
- Notably, the **frequency of fatal cancers was significantly reduced (only ~10%)** compared with the general population — a striking finding whose mechanism is not established but may partly explain the near-normal overall survival despite systemic amyloid burden.
- **Severe renal and cardiac manifestations are comparatively rare** relative to other systemic amyloidoses (e.g., AL, ATTR), which likely explains preserved lifespan.

**Morbidity/function.** Despite preserved survival, the **FIN-GAR phase II study** documented **significant disease burden and reduced quality of life** attributable to progressive visual impairment (recurrent corneal amyloid/erosions), facial diplegia (functional and cosmetic/social impact — difficulty with speech, chewing, eye closure), cutaneous fragility/cosmetic change, and neuropathic symptoms ([PMID:31952544](https://pubmed.ncbi.nlm.nih.gov/31952544/)).

**Complications:** Recurrent corneal erosions and progressive corneal opacification (sometimes requiring keratoplasty, with risk of amyloid recurrence in the graft); facial nerve palsy leading to exposure keratopathy (compounding the corneal disease), dysarthria/dysphagia; skin fragility/laxity; in a minority, nephrotic syndrome progressing to end-stage renal disease (more common/severe in homozygotes and select non-D187 variants); cardiac conduction disease in a subset.

**Prognostic factors:** Homozygosity for the pathogenic *GSN* variant confers a substantially worse renal prognosis than heterozygosity. Female sex is associated with higher risk of fatal renal complications in the Finnish cohort. Specific non-Finnish *GSN* variants (e.g., N184K, N211K) are associated with a **renal-predominant** phenotype and comparatively less prominent classic corneal/cranial-nerve disease, altering the prognostic picture toward CKD/ESRD risk.

---

## 12. Treatment

**No disease-modifying or curative therapy currently exists.** Management is entirely **symptomatic/supportive**, and correct diagnosis is emphasized in the literature as decisively improving quality of life by enabling proactive, targeted symptom management ([Kiuru-Enari & Haltia 2013, PMID:23931809](https://pubmed.ncbi.nlm.nih.gov/23931809/)).

**Ophthalmologic management:**
- **Lubricating/protective ointments**, e.g., **vitamin A and panthenol-containing ointment**, used prophylactically and therapeutically for recurrent corneal erosions (NCIT term candidate: NCIT:C61027 Ophthalmic Lubricant, or generic Pharmacotherapy NCIT:C15986 with therapeutic_agent retinol/panthenol if precise CHEBI/NCIT codes are curated).
- **Corneal transplantation (penetrating or lamellar keratoplasty)** for advanced corneal opacification — "inevitable" in many patients with established amyloid deposits, per the literature, but **prognosis for graft longevity is limited by recurrent amyloid deposition in the graft**, so timing and patient counseling are important; **optic neuropathy should be excluded before keratoplasty** is undertaken, as it may limit visual benefit. Suggested NCIT term: NCIT:C15398/keratoplasty-type procedure, or generic Surgical Procedure NCIT:C15329.
- Management of facial nerve palsy-related **exposure keratopathy** (lid taping, moisture chamber goggles, tarsorrhaphy in severe cases) to protect the ocular surface, given the compounding effect of both corneal amyloid and impaired blink/lid closure.

**Neurologic/facial nerve management:**
- Supportive management of facial diplegia — no specific pharmacotherapy reverses the neuropathy; **physical/speech therapy** (NCIT:C15302 Physical Therapy; NCIT:C159273 Speech Therapy) may help with functional adaptation.
- Management of peripheral neuropathic symptoms with standard neuropathic pain approaches as needed (symptomatic pharmacotherapy, NCIT:C15986).

**Dermatologic management:** Supportive skin care (emollients) for dry, fragile skin; no specific therapy reverses cutis laxa.

**Renal management (for the subset with nephrotic syndrome/CKD):** Standard nephrology supportive care for proteinuria/CKD (e.g., renin-angiotensin system blockade for proteinuria reduction, standard CKD management); progression to **end-stage renal disease** may require **renal replacement therapy or transplantation** in severe (typically homozygous) cases, analogous to management of other hereditary renal amyloidoses. Suggested NCIT term: NCIT:C15289 Organ Transplantation for renal transplant in ESRD cases.

**Genetic counseling:** An essential component of management given autosomal dominant inheritance and full penetrance — NCIT:C15240 Genetic Counseling.

**Experimental/investigational therapies:** No AGel-amyloidosis–specific disease-modifying agent (e.g., stabilizer, antisense oligonucleotide, or antibody therapy analogous to tafamidis/patisiran for ATTR amyloidosis) has reached clinical trials, per this search. Preclinical research directions identified include:
- **Peptidomimetic and small-molecule inhibitors of gelsolin amyloid aggregation** — rationally designed to block fibril formation from the AGel amyloidogenic core ([PMC9698219](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9698219/)).
- **Epitope-specific antibody fragments** that block aggregation of the AGel D187N-derived amyloidogenic peptide in vitro ([PMC11298591](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11298591/)).
- **ER-directed gelsolin nanobody** targeting the first (furin-cleavage-permissive misfolding) step of amyloid formation, tested in the D187N transgenic mouse model ([Human Molecular Genetics, PMID/PMC via academic.oup.com/hmg](https://academic.oup.com/hmg/article/24/9/2492/2385716)).

These remain **preclinical (in vitro/mouse model)** and are not yet in human clinical trials as of this search; no ClinicalTrials.gov-registered interventional trial specific to gelsolin/AGel amyloidosis was identified (searches for doxycycline/antisense/chaperone trials returned only AL- and ATTR-amyloidosis trials, not AGel-specific studies).

---

## 13. Prevention

- **Primary prevention:** Not applicable in the classic sense (monogenic disease with full penetrance); the only "primary prevention" avenue is **reproductive genetic counseling and prenatal/preimplantation genetic testing** for at-risk families who wish to avoid transmission, though this is not documented as widely practiced for this comparatively benign-course disease.
- **Secondary prevention (early detection):** **Cascade genetic testing** of at-risk relatives in known Finnish (or other) AGel families, and **ophthalmologic screening** (slit-lamp exam) in at-risk individuals, to enable early recognition of corneal lattice dystrophy before advanced neurologic/dermatologic/renal disease develops, allowing earlier initiation of protective ocular measures and monitoring for renal involvement (periodic urinalysis).
- **Tertiary prevention:** Proactive lubrication/protective ointment regimens to reduce corneal erosion frequency; lid protection strategies once facial nerve palsy develops (to prevent exposure keratopathy compounding corneal disease); periodic renal function/proteinuria monitoring, especially in homozygotes, to catch nephropathy early and initiate standard CKD-slowing therapy.
- **Genetic counseling** is the central "prevention" intervention documented in the literature, given autosomal dominant, fully penetrant inheritance.
- No vaccine, chemoprophylaxis, or public-health/environmental intervention is applicable, as this is a purely genetic, non-communicable, non-environmentally-triggered disease.

---

## 14. Other Species / Natural Disease

No naturally occurring animal disease orthologous to human AGel amyloidosis was identified in this search (i.e., no reported spontaneous veterinary gelsolin amyloidosis in companion animals or wildlife, unlike some other hereditary amyloidoses with veterinary counterparts). Gelsolin (GSN) itself is highly conserved across mammals (mouse *Gsn* ortholog on chromosome 2), and the protein's actin-regulatory function is evolutionarily conserved, but disease modeling has been achieved exclusively through **engineered (transgenic/knock-in) rather than natural** animal models (see §15).

---

## 15. Model Organisms

**Genetically engineered mouse models:**
- **D187N transgenic mice** (human D187N gelsolin expressed under a muscle-specific promoter) — the principal disease model, which **recapitulates the aberrant furin/MT1-MMP proteolytic cascade** generating the 8-kDa and 5-kDa amyloidogenic gelsolin peptides seen in human FAF patients, and shows **age-associated extracellular amyloid deposition**. Homozygous D187N mice show **progressive loss of muscle strength**, and the model additionally reveals **age-associated intracellular protein-homeostasis failure** (co-aggregation of multiple proteins in rough ER of skeletal muscle), producing a phenotype resembling **sporadic inclusion body myositis** pathology ([PNAS 2009](https://www.pnas.org/doi/10.1073/pnas.0811753106); [PMC4461228](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4461228/)). This model has been used as a preclinical platform to test candidate therapeutics, e.g., the ER-directed anti-gelsolin nanobody described above ([HMG 2015](https://academic.oup.com/hmg/article/24/9/2492/2385716)).
- **Gelsolin-null (Gsn knockout) mice** — a distinct model used to probe **normal gelsolin function** rather than amyloidosis per se. These mice have **normal embryonic development and longevity**, but show **decreased platelet shape change** and **prolonged bleeding times**, reflecting gelsolin's normal role in actin dynamics; this model does not itself produce an amyloid phenotype and is primarily informative about gelsolin's physiological (non-amyloidogenic) function rather than disease mechanism.

**Model characteristics/limitations:** The D187N transgenic model recapitulates the core biochemical cascade (furin/MT1-MMP-dependent generation of amyloidogenic fragments) and downstream proteostasis failure, but is a **muscle-restricted, overexpression-driven** model rather than a knock-in recapitulating physiological tissue-specific expression and the classic corneal/cranial-nerve/skin triad seen in humans — i.e., it captures **molecular/cellular pathogenesis** well but does not fully reproduce the **human clinical organotropism** (cornea, facial nerve, skin) that defines the clinical syndrome. No knock-in mouse model precisely reproducing the human ocular/cranial-nerve/dermatologic phenotype was identified in this search.

**Applications:** The D187N transgenic model has been used to study (a) the proteolytic amyloidogenesis cascade, (b) age-dependent progressive muscle/tissue pathology, (c) links between amyloid gelsolin secretion and broader age-related proteostasis collapse, and (d) preclinical testing of aggregation-blocking biologics (nanobodies) and small molecules.

---

## Summary Table of Suggested Ontology Terms for KB Curation

| Category | Term |
|---|---|
| Disease | MONDO:0007097; OMIM:105120; ORPHA:85448 |
| Causal gene | GSN, HGNC:4620 (hgnc:4620), OMIM:137350 |
| Key phenotypes (HP) | Lattice corneal dystrophy; Facial palsy; Cutis laxa; Peripheral neuropathy; Nephrotic syndrome; Dry skin; Dysphagia — *verify exact HP IDs/labels with OAK before curation per house style* |
| Key GO processes | actin binding (GO:0003779); calcium ion binding (GO:0005509); proteolysis (GO:0006508); actin filament binding (GO:0051015) |
| Key CL terms | Schwann cell (CL:0002573); podocyte (CL:0000653); mesangial cell (CL:0000650); keratocyte (CL:0000312) |
| Key UBERON terms | cornea (UBERON:0000965); facial nerve/cranial nerve (UBERON:0001528/0001780); skin of body (UBERON:0002097); kidney (UBERON:0002113) |
| Treatments (NCIT) | Pharmacotherapy (NCIT:C15986, e.g., lubricant ointment); Surgical Procedure/Keratoplasty (NCIT:C15329); Physical Therapy (NCIT:C15302); Genetic Counseling (NCIT:C15240); Organ Transplantation (NCIT:C15289, renal transplant in ESRD) |

---

## Sources

- [Entry - #105120 - AMYLOIDOSIS, FINNISH TYPE (OMIM)](https://www.omim.org/entry/105120)
- [Entry - *137350 - GELSOLIN; GSN (OMIM)](https://omim.org/entry/137350)
- [Orphanet: Gelsolin amyloidosis Finnish type](https://www.orpha.net/consor/cgi-bin/Disease_Genes.php?lng=EN&data_id=16170)
- [Orphanet: GSN-gelsolin gene page](https://www.orpha.net/en/disease/gene/GSN)
- [Finnish gelsolin amyloidosis causes significant disease burden but does not affect survival: FIN-GAR phase II study, Orphanet J Rare Dis, PMID:31952544](https://ojrd.biomedcentral.com/articles/10.1186/s13023-020-1300-5)
- [A novel hotspot of gelsolin instability triggers an alternative mechanism of amyloid aggregation, PMC8649582](https://ncbi.nlm.nih.gov/pmc/articles/PMC8649582)
- [A molecular perspective of gelsolin amyloidosis: An old foe with new faces, Cell Mol Life Sci 2026](https://link.springer.com/article/10.1007/s00018-026-06172-7)
- [Rational Design of a Peptidomimetic Inhibitor of Gelsolin Amyloid Aggregation, PMC9698219](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9698219/)
- [Epitope-specific antibody fragments block aggregation of AGelD187N, PMC11298591](https://pmc.ncbi.nlm.nih.gov/articles/PMC11298591/)
- [Furin initiates gelsolin familial amyloidosis in the Golgi through a defect in Ca2+ stabilization, PMID:11707399](https://pubmed.ncbi.nlm.nih.gov/11707399/)
- [Gelsolin Domain 2 Ca2+ Affinity Determines Susceptibility to Furin Proteolysis and FAF, PMID:14596804](https://pubmed.ncbi.nlm.nih.gov/14596804/)
- [Clinical features and haplotype analysis of newly identified Japanese patients with gelsolin-related FAF, PMID:22622774](https://pubmed.ncbi.nlm.nih.gov/22622774/)
- [Teaching NeuroImages: Gelsolin-related amyloidosis, Neurology](https://www.neurology.org/doi/10.1212/wnl.0b013e318281cc5c)
- [Hereditary gelsolin amyloidosis, PMID:23931809](https://pubmed.ncbi.nlm.nih.gov/23931809/)
- [Hereditary gelsolin amyloidosis — 40 years of Meretoja disease, PMID:20597346](https://pubmed.ncbi.nlm.nih.gov/20597346/)
- [Meretoja's Syndrome: Lattice Corneal Dystrophy, Gelsolin Type, PMC5306973](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5306973/)
- [Common origin of the gelsolin gene variant in 62 Finnish AGel amyloidosis families, PMC5838978 / Eur J Hum Genet](https://pmc.ncbi.nlm.nih.gov/articles/PMC5838978/)
- [Causes of death and life span in Finnish gelsolin amyloidosis, PMID:27137880](https://pubmed.ncbi.nlm.nih.gov/27137880/)
- [Asp187Asn mutation of gelsolin in an American kindred with FAF (FAP IV), Hum Genet](https://link.springer.com/article/10.1007/BF00225202)
- [Finnish type of familial amyloidosis: cosegregation of Asp187→Asn mutation, PMC1683143](https://pmc.ncbi.nlm.nih.gov/articles/PMC1683143/)
- [Mutation in gelsolin gene in Finnish hereditary amyloidosis, PMID:2175344](https://pubmed.ncbi.nlm.nih.gov/2175344/)
- [Gender differences in the clinical course of Finnish gelsolin amyloidosis, PMID:26805765](https://www.ncbi.nlm.nih.gov/pubmed/26805765)
- [Clinical, biopsy, and mass spectrometry findings of renal gelsolin amyloidosis, PMID:28139293](https://www.ncbi.nlm.nih.gov/pubmed/28139293)
- [Renal gelsolin amyloidosis as a rare cause of proteinuria, BMC Nephrology](https://link.springer.com/article/10.1186/s12882-025-04599-x)
- [Novel gelsolin variant as the cause of nephrotic syndrome and renal amyloidosis, PMC4061150 / PMID:24601799](https://pmc.ncbi.nlm.nih.gov/articles/PMC4061150/)
- [Molecular basis of a novel renal amyloidosis due to N184K gelsolin variant, PMC5025852](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5025852/)
- [Hereditary renal amyloidosis caused by a heterozygous G654A gelsolin mutation: two cases, PMC4432447](https://pmc.ncbi.nlm.nih.gov/articles/PMC4432447/)
- [Hereditary gelsolin amyloidosis: cranial, peripheral and autonomic neuropathies linked to D187N and Y447H, PMID:37140928](https://pubmed.ncbi.nlm.nih.gov/37140928/)
- [Danish type gelsolin-related amyloidosis in a Brazilian family, PMID:22068858](https://pubmed.ncbi.nlm.nih.gov/22068858/)
- [Danish type gelsolin related amyloidosis: 654G-T mutation, PMID:10767822](https://pubmed.ncbi.nlm.nih.gov/10767822/)
- [Haplotype analysis in gelsolin-related amyloidosis: independent origin of G654A in Finland and Japan, PMID:7550233](https://pubmed.ncbi.nlm.nih.gov/7550233/)
- [Clinical and Histopathological Features of Gelsolin Amyloidosis with novel GSN Variant p.Glu580Lys, PMC7865823](https://pmc.ncbi.nlm.nih.gov/articles/PMC7865823/)
- [An immunohistochemical study of gelsolin immunoreactivity in corneal amyloidosis, PMID:1315488](https://pubmed.ncbi.nlm.nih.gov/1315488/)
- [Heavy-chain amyloidosis in TGFBI-negative and gelsolin-negative atypical lattice corneal dystrophy, PMID:21743312](https://pubmed.ncbi.nlm.nih.gov/21743312/)
- [Lattice Corneal Dystrophy, EyeWiki](https://eyewiki.org/Lattice_Corneal_Dystrophy)
- [122200 - CORNEAL DYSTROPHY, LATTICE TYPE I; CDL1 (OMIM)](https://omim.org/entry/122200)
- [GSN Gene - GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=GSN)
- [Structure, regulation and related diseases of the actin-binding protein gelsolin, Expert Rev Mol Med](https://www.cambridge.org/core/journals/expert-reviews-in-molecular-medicine/article/structure-regulation-and-related-diseases-of-the-actinbinding-protein-gelsolin/189DA7129C426E4B8597A55E288AF2D1)
- [Secretion of amyloidogenic gelsolin progressively compromises protein homeostasis, PNAS](https://www.pnas.org/doi/10.1073/pnas.0811753106)
- [Formation of gelsolin amyloid fibrils in the rough ER of skeletal muscle (D187N mouse model), PMC4461228](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4461228/)
- [An ER-directed gelsolin nanobody targets the first step in amyloid formation in a gelsolin amyloidosis mouse model, Hum Mol Genet](https://academic.oup.com/hmg/article/24/9/2492/2385716)
- [The role of gelsolin domain 3 in familial amyloidosis (Finnish type), PNAS 2019](https://www.pnas.org/doi/10.1073/pnas.1902189116)
- [Finnish type amyloidosis, NORD](https://rarediseases.org/mondo-disease/finnish-type-amyloidosis/)
- [Finnish type amyloidosis, GARD/NIH](https://rarediseases.info.nih.gov/diseases/2339/finnish-type-amyloidosis)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 36 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 36 |
| On topic | 25 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:33375500` (1 mention) - Standoff Distance in Ultrasonic Pulsating Water Jet.
  - shared terms: none

Weighed against this report's own most characteristic terms: `disease`, `amyloidosis`, `corneal`, `renal`, `agel`, `gelsolin`, `patient`, `finnish`, `facial`, `gsn`, `lattice`, `skin`, `peripheral`, `nerve`, `dystrophy`, `amyloid`, `variant`, `syndrome`, `d187n`, `genetic`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.