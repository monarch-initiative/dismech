---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-09T18:12:21.200191'
end_time: '2026-07-09T18:17:52.033774'
duration_seconds: 330.83
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Carbon Monoxide Poisoning
  mondo_id: ''
  category: Environmental
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
  web_search_requests: 11
  num_turns: 14
  total_cost_usd: 2.3452467499999994
  session_id: 7d044c94-3c17-4e52-9f67-d29af03e6b59
  stop_reason: end_turn
citation_count: 28
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Carbon Monoxide Poisoning
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Carbon Monoxide Poisoning** covering all of the
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

I now have comprehensive, well-sourced material. Here is the full research report.

---

# Carbon Monoxide Poisoning — Comprehensive Research Report

**Prepared for:** dismech disease knowledge base entry
**Category:** Environmental (toxic gas exposure)
**Report date:** 2026-07-09

> **Scope note:** Carbon monoxide (CO) poisoning is a toxic-exposure syndrome, not a Mendelian or genetically-defined disease. Sections framed around causal genes, inheritance, penetrance, founder effects, and germline variants are **largely Not Applicable**; they are retained below with explicit "N/A" annotations and repurposed toward *host susceptibility modifiers* where evidence exists. The mechanistic, phenotypic, diagnostic, treatment, and prevention sections are the substantive core.

---

## 1. Disease Information

**Overview.** Carbon monoxide poisoning is the clinical syndrome resulting from inhalation of carbon monoxide, a colorless, odorless, tasteless, non-irritating gas produced by incomplete combustion of carbon-containing (hydrocarbon) fuels. It is one of the most common causes of fatal poisoning worldwide. CO produces injury through two convergent mechanisms: (1) **hypoxic stress** from formation of carboxyhemoglobin (COHb), which reduces oxygen-carrying capacity and shifts the oxyhemoglobin dissociation curve leftward (impairing tissue oxygen offloading); and (2) **direct cellular toxicity** independent of COHb — binding to mitochondrial cytochrome c oxidase, myoglobin, and other heme proteins, plus oxidative/nitrosative stress and an immune-mediated delayed neuroinflammatory cascade (StatPearls *Carboxyhemoglobin Toxicity*, NBK557888; Weaver, NEJM 2002, **PMID 12362006**).

**Key identifiers.**
- **MONDO:** `MONDO:0021113` (carbon monoxide poisoning) — *verify against the local `sqlite:obo:mondo` adapter before committing* (`runoak -i sqlite:obo:mondo info MONDO:0021113 -O obo`); OLS did not render the record in this session, so treat the ID as provisional. A closely related concept is **carboxyhemoglobinemia**.
- **ICD-10-CM:** `T58.-` "Toxic effect of carbon monoxide," with source/intent subcodes — e.g., `T58.01XA` (motor-vehicle exhaust, accidental, initial encounter), `T58.11XA` (utility gas, accidental), `T58.91XA` (unspecified source, accidental), and intentional-self-harm variants (`T58.-2-`).
- **ICD-11:** `NE61` / stem for toxic effect of carbon monoxide (foundation "Toxic effect of carbon monoxide").
- **MeSH:** `D002249` "Carbon Monoxide Poisoning."
- **OMIM/Orphanet:** No dedicated Mendelian OMIM entry (not a genetic disease). Not a designated rare disease in Orphanet.
- **SNOMED CT:** 284196006 "Carbon monoxide poisoning" (concept present; verify current ID).

**Synonyms / alternative names.** CO poisoning; carbon monoxide toxicity; carbon monoxide intoxication; carboxyhemoglobinemia (the biochemical state); "silent killer" (lay). Historically overlapping legacy terms: "coal gas poisoning," "flue gas / smoke inhalation CO component."

**Data derivation.** Disease-level knowledge here derives from **aggregated resources** (CDC/WHO surveillance, poison-center data, UHMS/society guidelines, and clinical-trial cohorts) rather than individual EHR records, though large administrative/EHR and forensic cohorts underpin the epidemiology and prognosis figures.

*Sources:* [StatPearls Carboxyhemoglobin Toxicity](https://www.ncbi.nlm.nih.gov/books/NBK557888/); [MSD/Merck Manual](https://www.msdmanuals.com/professional/injuries-poisoning/poisoning/carbon-monoxide-poisoning); [ICD10Data T58](https://www.icd10data.com/ICD10CM/Codes/S00-T88/T51-T65/T58-/T58).

---

## 2. Etiology

**Primary cause (environmental/toxic).** Inhalation of CO gas. There is no genetic or infectious primary etiology — this is a pure environmental/toxicological exposure disease. CHEBI: carbon monoxide = **`CHEBI:17245`**.

**Common exposure sources.**
- Faulty or unvented fuel-burning appliances: furnaces, gas/oil boilers, water heaters, gas ranges/ovens, space heaters.
- **Motor-vehicle exhaust** (running engines in attached/closed garages; a frequent suicide method).
- **Portable generators**, a major cause of poisoning and death during storm-related power outages (CDC disaster guidance).
- Charcoal grills / hibachis used indoors; camping stoves and lanterns in tents.
- House fires / **smoke inhalation** (CO is a leading cause of fire-related death).
- **Methylene chloride (dichloromethane, `CHEBI:15767`)** — paint strippers and solvents; hepatically metabolized to CO, causing delayed, prolonged COHb elevation.
- Indoor use of gasoline-powered tools; ice-rink resurfacers; boating "houseboat/exhaust" exposures.
- Tobacco/hookah smoke (chronic low-level source; baseline COHb 3–10% in smokers).

**Risk factors (environmental / demographic).**
- **Season:** winter months (heating use); poisonings and deaths peak in cold months (CDC/NVSS).
- **Setting:** most exposures occur at home; disasters and power outages (generators).
- **Sex:** male death rate ~0.22/100,000 vs female ~0.07/100,000 (>3× higher in males, 1999–2010 CDC data) — partly reflecting occupational exposure and intentional poisoning.
- **Age:** highest death rates in adults **≥65 years** (males 0.42, females 0.18 per 100,000).
- **Occupation:** firefighters, garage/toll workers, welders, mechanics, foundry/blast-furnace workers, propane forklift operators.
- **Pregnancy:** enhanced fetal vulnerability (see §9, §12).
- **Comorbidity:** pre-existing coronary artery disease, anemia, chronic respiratory disease, and cerebrovascular disease increase susceptibility to a given COHb level.
- **Absent CO detectors** in the home is a strong, modifiable risk factor for fatal poisoning (Yoon, *JAMA* 1998, **PMID 9496987**).

**Genetic / host-susceptibility modifiers (not causal).** True Mendelian causation is **N/A**. Reported modifiers of susceptibility or of delayed neurological sequelae (DNS) are limited and largely candidate-gene/observational: haptoglobin phenotype, HMOX1 (heme oxygenase-1) promoter (GT)n repeat polymorphisms, apolipoprotein E (APOE) genotype, and inflammatory-cytokine polymorphisms have been proposed to modulate outcome, but none are established. Individuals with **higher baseline COHb** (smokers), **anemia** (lower total O₂-carrying reserve), or **cardiac/cerebrovascular disease** tolerate less CO.

**Protective factors.**
- **CO detectors/alarms** (primary environmental protection; legislative mandates reduce deaths).
- Appliance maintenance, adequate ventilation, and never running engines/generators indoors.
- No established *genetic* protective variant.

**Gene–environment interaction.** The dose–response to a fixed CO exposure is modulated by host oxygen-carrying reserve and antioxidant/inflammatory genotype (e.g., HMOX1, antioxidant enzymes), but this remains hypothesis-level (CTD lists CO–gene interactions primarily from toxicogenomic models, not clinical GxE). Treat as an **open knowledge gap** (`KNOWLEDGE_GAP`).

*Sources:* [CDC QuickStats 1999–2010](https://www.cdc.gov/mmwr/preview/mmwrhtml/mm6303a6.htm); [Yoon 1998 PMID 9496987](https://pubmed.ncbi.nlm.nih.gov/9496987/); [CDC disaster clinical guidance](https://www.cdc.gov/carbon-monoxide/hcp/clinical-guidance/index.html).

---

## 3. Phenotypes

CO poisoning is a **multisystem** syndrome with nonspecific early symptoms (often misdiagnosed as viral illness or food poisoning). Manifestations correlate imperfectly with COHb level; clinical severity, duration of exposure, and host factors matter more than a single COHb number.

**Neurologic / neuropsychiatric (dominant and prognostically important).**
- **Headache** — the most common early symptom (often "dull, frontal"). HPO: **Headache HP:0002315**. Frequency: very frequent/most common.
- **Dizziness / lightheadedness** — HPO: **Vertigo HP:0002321** / Dizziness. Frequent.
- **Confusion, impaired cognition, difficulty concentrating** — HPO: **Confusion HP:0001289**; **Cognitive impairment HP:0100543**. Frequent-to-severe cases.
- **Syncope / loss of consciousness** — HPO: **Syncope HP:0001279**; **Loss of consciousness HP:0007185**. A key severity marker and HBO indication.
- **Seizures** — HPO: **Seizure HP:0001250**. Severe poisoning.
- **Coma** — HPO: **Reduced consciousness/confusion → Coma HP:0001259**. Severe.
- **Delayed neurological/neuropsychiatric sequelae (DNS / DEACMP)** — a hallmark: after apparent recovery, a lucid interval of days–weeks precedes cognitive decline, memory loss, parkinsonism, gait/movement disorders, personality/affective change, incontinence, and akinetic mutism. HPO overlaps: **Parkinsonism HP:0001300**, **Memory impairment HP:0002354**, **Gait disturbance HP:0001288**, **Personality changes HP:0000751**, **Dystonia HP:0001332**. Onset typically 2–40 days post-recovery; occurs in ~3–40% depending on severity/definition.
- **Peripheral neuropathy**, hearing loss, vestibular dysfunction (less common).

**Cardiovascular.**
- **Myocardial ischemia / injury** — chest pain, ECG ischemia, troponin rise, arrhythmia; myocardial infarction with angiographically normal coronaries possible. HPO: **Myocardial infarction HP:0001658**; **Angina pectoris HP:0001681**; **Arrhythmia HP:0011675**. Common in moderate–severe poisoning; associated with increased long-term mortality.
- **Hypotension, tachycardia**.

**Respiratory.**
- **Dyspnea** (HPO: **Dyspnea HP:0002094**), tachypnea; noncardiogenic pulmonary edema in severe cases.

**General / constitutional.**
- **Nausea and vomiting** — HPO: **Nausea and vomiting HP:0002017** (or **Nausea HP:0002018 / Vomiting HP:0002013**). Frequent; often mistaken for gastroenteritis.
- **Fatigue / weakness / malaise** — HPO: **Fatigue HP:0012378**; **Muscle weakness HP:0001324**.
- **Visual disturbance / blurred vision** — HPO: **Blurred vision HP:0000622**; rarely retinal hemorrhages, cortical blindness.

**Dermatologic.**
- The classically taught "cherry-red" skin/lips is **rare and unreliable** (usually a postmortem finding); cyanosis or normal color is more typical. Bullous skin lesions/pressure necrosis can occur in comatose patients.

**Laboratory abnormalities (phenotype: laboratory).**
- **Elevated carboxyhemoglobin (COHb)** — the defining lab abnormality. Normal <3% (nonsmokers), up to ~10–15% in heavy smokers. Symptomatic poisoning usually >10–20%. LOINC: **COHb/Hb.total — LOINC 20563-3** (Carboxyhemoglobin/Hemoglobin.total in Blood).
- **Metabolic acidosis with elevated lactate** (anaerobic metabolism) — LOINC: Lactate **2524-7**; a severity marker.
- **Elevated cardiac troponin / CK-MB** (myocardial injury).
- **Elevated creatine kinase** ± rhabdomyolysis/AKI in immobilized/comatose patients.
- **Falsely normal SpO₂** on standard pulse oximetry — conventional oximeters cannot distinguish COHb from oxyhemoglobin ("saturation gap"); requires CO-oximetry (multi-wavelength). A critical diagnostic pitfall.

**Quality-of-life impact.** Survivors of moderate–severe poisoning, especially those developing DNS, may have persistent cognitive deficits, mood/anxiety disorders, chronic headache, and impaired executive function, with measurable declines on neuropsychological batteries and quality-of-life instruments; some do not fully recover by 12 months (Weaver, NEJM 2002). Chronic low-level exposure produces persistent headache, fatigue, and cognitive complaints.

**Onset/severity/progression summary.** Onset **acute** (minutes–hours of exposure); severity **mild → severe/fatal** and **variable**; a distinct **biphasic** course is possible (acute illness → apparent recovery → DNS). Symptom–COHb correlation is weak.

*Sources:* [Merck Manual](https://www.merckmanuals.com/professional/injuries-poisoning/poisoning/carbon-monoxide-poisoning); [MedLink Neurology](https://www.medlink.com/articles/carbon-monoxide-poisoning); [Weaver NEJM 2002 PMID 12362006](https://pubmed.ncbi.nlm.nih.gov/12362006/).

---

## 4. Genetic / Molecular Information

**Causal genes:** **None — Not Applicable.** CO poisoning is a toxic exposure, not a Mendelian disorder. There are no causal genes, pathogenic variants (ACMG/AMP classes), allele frequencies, somatic/germline distinctions, or chromosomal abnormalities to report.

**Molecular target of the toxicant (the meaningful "molecular" content).** The pathogenic ligand is CO gas (**CHEBI:17245**), which binds ferrous (Fe²⁺) **heme** iron in multiple hemoproteins:
- **Hemoglobin (HBB/HBA)** → carboxyhemoglobin. CO affinity ~**200–250× that of O₂** (StatPearls cites ~240×).
- **Myoglobin (MB, HGNC gene *MB*)** → carboxymyoglobin, impairing cardiac and skeletal muscle O₂ storage/utilization; contributes to myocardial dysfunction.
- **Cytochrome c oxidase (Complex IV, MT-CO1/2/3 + nuclear COX subunits)** → inhibition of mitochondrial electron transport and oxidative phosphorylation (direct histotoxic hypoxia).
- **NADPH oxidase, cytochrome P450, guanylate cyclase, and NOS-associated hemes** are additional CO targets influencing signaling and reactive-species production.

**Modifier genes / epigenetics / chromosomal:** No established modifiers (see §2 for candidate host modifiers such as **HMOX1**, **APOE**). Epigenetic and chromosomal sections are **N/A** for causation. (Note that CO is itself an endogenous signaling molecule generated by heme oxygenase-1, *HMOX1*, HGNC:5013 — biologically relevant context, not a disease gene.)

*Sources:* [StatPearls NBK557888](https://www.ncbi.nlm.nih.gov/books/NBK557888/); [ROS/oxidative-stress review PMID 24773392](https://pubmed.ncbi.nlm.nih.gov/24773392/).

---

## 5. Environmental Information

- **Environmental factors:** ambient CO from incomplete combustion (see §2 source list). Poorly ventilated enclosed spaces concentrate CO; concentration (ppm) × exposure duration determines dose. Regulatory context: OSHA PEL 50 ppm (8-h TWA); NIOSH IDLH 1,200 ppm; ambient CO tracked by EPA.
- **Lifestyle factors:** tobacco smoking (chronic endogenous/exogenous CO load, baseline COHb elevation); indoor charcoal/generator use; occupational exposure.
- **Infectious agents:** **None — Not Applicable.**

*Sources:* [CDC CO topic](https://archive.cdc.gov/www_cdc_gov/co/surveillance/routine.htm); [Merck Manual](https://www.merckmanuals.com/professional/injuries-poisoning/poisoning/carbon-monoxide-poisoning).

---

## 6. Mechanism / Pathophysiology

CO injures tissue through **two integrated arms** — impaired oxygen delivery/utilization (hypoxic-ischemic) and direct cellular toxicity with oxidative/nitrosative stress and delayed immune-mediated neuroinflammation. The brain and heart, with the highest oxygen demand, are most vulnerable.

### Causal chain (upstream → downstream)

**A. Hypoxic-ischemic arm.**
1. Inhaled CO diffuses across the alveolar–capillary membrane and binds hemoglobin Fe²⁺ → **carboxyhemoglobin**, reducing O₂-carrying capacity.
2. CO binding to one heme **shifts the oxyhemoglobin dissociation curve leftward**, further impairing O₂ *release* to tissue (functional anemia worse than simple loss of capacity).
3. → **Tissue hypoxia**, anaerobic metabolism, **lactic acidosis** (GO: *cellular response to hypoxia* **GO:0071456**; *anaerobic respiration*).

**B. Direct cytotoxic / histotoxic arm (COHb-independent).**
4. CO binds **cytochrome c oxidase (Complex IV)**, inhibiting mitochondrial electron transport and ATP synthesis → **histotoxic hypoxia** even where O₂ is available (GO: *mitochondrial electron transport, cytochrome c to oxygen* **GO:0006123**; *oxidative phosphorylation* **GO:0006119**). CO also binds **myoglobin** → impaired cardiac oxygen utilization → myocardial depression, hypotension, and secondary global ischemia/reperfusion.

**C. Oxidative/nitrosative stress and vascular arm.**
5. CO displaces **nitric oxide (NO)** from platelets and hemoproteins → excess NO → **peroxynitrite** formation; NO/peroxynitrite drive **leukocyte (neutrophil) adhesion** to injured cerebral microvascular endothelium (β2-integrin–mediated).
6. Adherent neutrophils release **myeloperoxidase**, generating reactive oxygen species (ROS). ROS are produced from **three temporally distinct sources**: mitochondria (first minutes of exposure), **xanthine oxidase** (~20 min, from energy deprivation/purine catabolism), and **NADPH oxidase** during the **post-exposure reoxygenation** period — i.e., an **ischemia–reperfusion–like injury** (Chang et al., ROS review **PMID 24773392**; PMC9852609). GO: *reactive oxygen species metabolic process* **GO:0072593**; *response to oxidative stress* **GO:0006979**.
7. → **Lipid peroxidation** of membrane and myelin lipids; **glutathione depletion** (GO: *lipid oxidation*; *lipid peroxidation*).

**D. Delayed immune-mediated demyelination (the DNS engine).**
8. Lipid peroxidation generates **malondialdehyde (MDA)**, which forms **adducts with myelin basic protein (MBP)** in the CNS. Modified MBP loses its normal cationic charge and antibody-recognition profile.
9. Chemically altered MBP is **immunogenic**: over days, degraded MBP appears in brain with **influx of macrophages and CD4⁺ T-lymphocytes**, and **autoreactive lymphocyte proliferation to MBP** develops, with **microglial activation** → adaptive **autoimmune demyelination** and delayed neuropathology. Rats made immunologically tolerant to MBP before CO poisoning show the acute biochemical MBP change **but no lymphocyte response and no learning deficit**, establishing causation (Thom SR et al., *PNAS* 2004;101(37):13660–13665, **PMID 15342916**). GO: *adaptive immune response* **GO:0002250**; *inflammatory response* **GO:0006954**; *demyelination*.
10. → **Delayed neuronal apoptosis** (hippocampus, basal ganglia), **white-matter demyelination**, and DNS.

**Cell types involved (CL terms).** Neurons (**CL:0000540**), especially hippocampal neurons and basal-ganglia/globus-pallidus neurons; oligodendrocytes (**CL:0000128**, myelin) as demyelination targets; microglial cells (**CL:0000129**); cardiac myocytes (**CL:0000746**); vascular endothelial cells (**CL:0000115**); neutrophils (**CL:0000775**); CD4⁺ T cells (**CL:0000624**); macrophages (**CL:0000235**); erythrocytes (**CL:0000232**, the COHb site).

**Subcellular compartments (GO Cellular Component).** Mitochondrion (**GO:0005739**), specifically the mitochondrial respiratory chain complex IV (**GO:0005751**); myelin sheath (**GO:0043209**); plasma membrane / cytosol.

**Metabolic changes.** Shift to anaerobic glycolysis; lactic acidosis; ATP depletion; glutathione depletion; disrupted heme-protein oxygen handling.

**Immune involvement.** Innate (neutrophil/microglia/macrophage, ROS) acutely; adaptive **autoimmune** (anti-MBP CD4⁺ T-cell) response driving delayed demyelination — a rare example of a toxic exposure triggering an autoimmune neurologic sequela.

**Tissue-damage mechanisms.** Oxidative stress, ischemia–reperfusion injury, lipid peroxidation, apoptosis/necrosis, and immune-mediated demyelination converge on the **globus pallidus** (watershed, high metabolic demand, vulnerable) and deep white matter.

**Molecular profiling / advanced tech.** Transcriptomic and proteomic studies in rodent DEACMP models show upregulated inflammatory and apoptotic pathways and MBP degradation; candidate serum biomarkers (S100B, NSE, GFAP, myelin-related autoantibodies) have been studied for DNS prediction. Human single-cell/spatial and CRISPR-screen data are **not established** for this exposure — an open knowledge gap.

*Sources:* [ROS review PMID 24773392](https://pubmed.ncbi.nlm.nih.gov/24773392/); [Thom PNAS 2004 PMID 15342916](https://pmc.ncbi.nlm.nih.gov/articles/PMC518809/); [Mechanism of delayed encephalopathy PMID 32594050](https://pubmed.ncbi.nlm.nih.gov/32594050/); [MBP degradation rat PMID 20633582](https://pubmed.ncbi.nlm.nih.gov/20633582/).

---

## 7. Anatomical Structures Affected

**Organ level.**
- **Primary:** Brain (**UBERON:0000955**) and heart (**UBERON:0000948**) — highest O₂ demand.
- **Secondary / systemic:** skeletal muscle (rhabdomyolysis), kidney (**UBERON:0002113**; AKI from rhabdomyolysis/hypoperfusion), lungs (**UBERON:0002048**; pulmonary edema), skin, retina/eye, peripheral nerves.
- **Body systems:** nervous, cardiovascular, respiratory, musculoskeletal, and (fetal) reproductive/placental.

**Tissue and cell level.**
- Basal ganglia — especially **globus pallidus (UBERON:0001875)**, the signature CO lesion — and substantia nigra; deep cerebral **white matter (UBERON:0002316)**; hippocampus (**UBERON:0002421**); cerebral cortex; occasionally putamen, caudate, thalamus (imaging: bilateral, symmetric).
- Cell populations: pallidal neurons, hippocampal neurons, oligodendrocytes/myelin, cardiac myocytes, microvascular endothelium.

**Subcellular level.** Mitochondria (Complex IV) and myelin sheath are the principal molecular battlegrounds.

**Localization / laterality.** CNS lesions are characteristically **bilateral and symmetric** (globus pallidus > white matter). On MRI: globus pallidus shows T1 hypo-/T2-FLAIR hyperintensity with **restricted diffusion (DWI)** acutely; late subacute period shows diffuse white-matter demyelination.

*Sources:* [AJNR Pallidoreticular DWI](https://www.ajnr.org/content/26/7/1845); [Advanced neuroimaging of CO poisoning PMC5602327](https://pmc.ncbi.nlm.nih.gov/articles/PMC5602327/).

---

## 8. Temporal Development

- **Onset:** **acute** — minutes to hours of exposure; any age (congenital exposure via maternal poisoning to geriatric).
- **Acute course:** symptoms during/after exposure; severity tracks cumulative dose (concentration × time) more than a single COHb.
- **Biphasic pattern / DNS:** after treatment and apparent recovery, a **lucid interval of ~2–40 days** may precede **delayed neuropsychiatric sequelae** (cognitive decline, parkinsonism, affective/behavioral change). This is the defining temporal feature.
- **Progression / recovery:** many mild cases resolve fully within hours–days on oxygen. Moderate–severe cases risk persistent or delayed deficits; DNS may partially recover over **6–12 months**, but a subset has permanent impairment.
- **Critical intervention window:** benefit of hyperbaric oxygen (HBO) is greatest when started **within 6 hours** and not later than ~24 hours (UHMS).

*Sources:* [Weaver NEJM 2002](https://pubmed.ncbi.nlm.nih.gov/12362006/); [Predictors of delayed encephalopathy PMC11979149](https://pmc.ncbi.nlm.nih.gov/articles/PMC11979149/).

---

## 9. Inheritance and Population (Epidemiology)

**Inheritance:** **Not Applicable** (non-genetic exposure). Penetrance, expressivity, anticipation, mosaicism, founder effects, consanguinity, and carrier frequency are all **N/A**.

**Epidemiology (aggregate).**
- **US unintentional mortality:** ~**430 deaths/year** average (1999–2010, total 5,149; CDC); ~**2,244 deaths** over 2010–2015. In **2022**, CDC provisional data recorded **1,244 total CO deaths** (624 accidental + 579 suicides).
- **Morbidity:** **>100,000 US emergency-department visits/year** for accidental CO poisoning, with **>14,000 hospitalizations/year** (CDC/USAFacts).
- **Sex ratio:** male death rate ~0.22/100,000 vs female ~0.07/100,000 (males >3× higher, 1999–2010).
- **Age:** highest death rates in adults **≥65 years** (males 0.42, females 0.18 per 100,000).
- **Seasonality:** strong winter predominance (heating season, power outages).
- **Global:** CO poisoning is a leading cause of poisoning death worldwide; incidence and trends analyzed via GBD 1990–2021 (joinpoint/ARIMA; PMC12373207). Rates are higher where unvented biomass/coal heating and gas water heaters are common.

**Prevalence framing for the KB** (`PrevalenceMeasureEnum`): best modeled as **ANNUAL_INCIDENCE** (ED visits ~30/100,000/year in the US; deaths ~0.1–0.4/100,000/year), **not** a chronic point prevalence. `prevalence_class` qualitatively **COMMON** among acute poisonings.

**Population demographics.** Higher burden in lower-income households (older/unmaintained appliances), disaster-affected populations (generators), and in regions with indoor combustion heating/cooking. Intentional CO poisoning (suicide) skews male and adult.

*Sources:* [CDC QuickStats 1999–2010](https://www.cdc.gov/mmwr/preview/mmwrhtml/mm6303a6.htm); [CDC NVSS 2010–2015](https://www.cdc.gov/mmwr/volumes/66/wr/mm6608a9.htm); [USAFacts 2022](https://usafacts.org/articles/is-carbon-monoxide-still-a-problem-in-the-us/); [GBD 1990–2021 PMC12373207](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12373207/).

---

## 10. Diagnostics

**Core principle:** diagnosis requires **clinical suspicion** (nonspecific symptoms + compatible exposure history, often multiple household members or a pet affected) plus **direct COHb measurement**. Standard pulse oximetry is falsely reassuring.

**Laboratory / functional tests.**
- **Carboxyhemoglobin (COHb) by CO-oximetry** on arterial or venous blood (venous adequate for the level) — the confirmatory test. LOINC **20563-3**. Interpret against baseline: nonsmoker <3%; smoker up to ~10–15%. Elevation confirms exposure; magnitude does **not** reliably grade severity.
- **Non-invasive pulse CO-oximetry** (multi-wavelength, e.g., SpCO) — screening/triage; correlates imperfectly with blood COHb (PMC10890311).
- **ABG/VBG** with lactate: metabolic acidosis, elevated lactate = severity markers. Measured (not calculated) SaO₂ needed.
- **Cardiac troponin, ECG** — screen all moderate–severe poisonings for myocardial injury/ischemia (prognostic).
- **CK, renal function, urinalysis** — rhabdomyolysis/AKI.
- **Pregnancy test** in women of childbearing age (alters HBO threshold).

**Imaging.**
- **CT/MRI brain:** bilateral symmetric globus-pallidus lesions; DWI restricted diffusion acutely; diffuse white-matter demyelination subacutely — supports diagnosis and prognosticates DNS risk. Advanced MRI (DTI, MRS, CEST-glutamate) is research-grade.

**Biomarkers (investigational for DNS prediction).** S100B, neuron-specific enolase (NSE), GFAP, and myelin-related autoantibodies have been studied as predictors of delayed encephalopathy but are not standard of care.

**Genetic/omics testing:** **Not Applicable** for diagnosis.

**Clinical criteria / differential diagnosis.** No formal DSM/ICD diagnostic *criteria* set beyond exposure + elevated COHb + compatible illness. **Differential:** viral illness/influenza, gastroenteritis/food poisoning, migraine, acute coronary syndrome, stroke, other toxic gas/cyanide exposure (concurrent in fires — consider cyanide co-toxicity), and psychiatric/functional disorders. Clues favoring CO: multiple people/pets ill in the same environment, symptoms improving away from home, winter/heating context.

**Screening.** Not a population lab-screening target; **home CO alarms** are the practical "screening" tool for asymptomatic detection of dangerous ambient levels.

*Sources:* [StatPearls NBK557888](https://www.ncbi.nlm.nih.gov/books/NBK557888/); [The Diagnosis and Treatment of CO Poisoning PMC6381775](https://pmc.ncbi.nlm.nih.gov/articles/PMC6381775/); [CO-oximetry correlation PMC10890311](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10890311/).

---

## 11. Outcome / Prognosis

- **Acute mortality:** most treated symptomatic patients survive; case fatality is driven by severe exposure, coma, cardiac arrest, and delayed presentation. Severe poisoning with coma or myocardial injury carries substantially higher mortality.
- **Cardiac injury as a prognostic marker:** myocardial injury (elevated troponin) during acute poisoning is associated with **increased long-term mortality** independent of acute severity.
- **Delayed neurological sequelae (DNS/DEACMP):** the principal morbidity — reported in roughly **3–40%** of moderate–severe cases depending on definition and follow-up; risk factors include older age, loss of consciousness, longer exposure, severe acidosis, and abnormal early neuroimaging. In Weaver's RCT, cognitive sequelae at 6 weeks occurred in **25%** (HBO group) vs **46%** (normobaric group).
- **Recovery:** many with DNS improve over 6–12 months; a subset has permanent cognitive, extrapyramidal (parkinsonism/dystonia), or affective deficits.
- **Morbidity/QoL:** persistent neurocognitive impairment, mood disorders, chronic headache, functional disability; measured with neuropsychological batteries and QoL tools.
- **Fetal outcome:** maternal poisoning can cause fetal death, CNS malformation, or neurodevelopmental injury; fetal COHb runs higher and clears more slowly than maternal (see §12).

*Sources:* [Weaver NEJM 2002 PMID 12362006](https://pubmed.ncbi.nlm.nih.gov/12362006/); [Predictors of delayed encephalopathy PMC11979149](https://pmc.ncbi.nlm.nih.gov/articles/PMC11979149/).

---

## 12. Treatment

**Immediate / supportive (MAXO: supportive care `MAXO:0000950`).**
- **Remove from exposure**; secure airway, breathing, circulation; treat seizures, hypotension, arrhythmia; cardiac monitoring; correct acidosis by restoring oxygenation/perfusion.

**Normobaric oxygen — first-line (MAXO: oxygen therapy `MAXO:0035013`; therapeutic agent dioxygen `CHEBI:15379`).**
- **High-flow 100% O₂** via non-rebreather mask (or ETT) for all suspected/confirmed cases. Rationale: **accelerates COHb elimination.** CO half-life ~**300 min (4–5 h)** on room air → ~**60–90 min** on 100% normobaric O₂ → ~**20–30 min** on hyperbaric O₂. Continue until asymptomatic and COHb near-normal (typically <3–5%).

**Hyperbaric oxygen (HBO) therapy (MAXO: hyperbaric oxygen therapy `MAXO:0000257`).**
- **Mechanism/rationale:** 100% O₂ at 2.5–3.0 ATA dramatically shortens COHb half-life, rapidly dissociates CO from cytochrome c oxidase and myoglobin, and is proposed to reduce lipid peroxidation, leukocyte–endothelial adhesion, and the immune-mediated demyelination cascade — potentially **preventing delayed neurological sequelae**, not just clearing COHb.
- **Indications (UHMS 2020 / clinical consensus):** consider HBO — ideally **within 6 h**, no later than ~24 h — for patients with **loss of consciousness (any duration)**, **neurologic deficits/abnormal cognition**, **cardiac ischemia/arrhythmia**, **severe metabolic acidosis**, **COHb >25%** (adults), and **pregnancy** (lower threshold, generally symptomatic exposure or **COHb >15–20%**, because fetal COHb is higher and clears slowly). Prolonged HBO/oxygen may be warranted after methylene-chloride exposure (ongoing endogenous CO production).
- **Evidence base (conflicting):**
  - **Thom et al., 1995** — prospective RCT: HBO reduced incidence of DNS in mild–moderate CO poisoning presenting within 6 h (**PMID 7710151**).
  - **Weaver et al., NEJM 2002** — quadruple-blinded RCT: **three HBO sessions within 24 h reduced cognitive sequelae** at 6 weeks (25% vs 46%) and at 12 months (**PMID 12362006**).
  - **Scheinkestel et al., MJA 1999** — RCT found **no benefit** (methodological differences; delayed/varied protocols) (**PMID 10092916**).
  - **Cochrane review (Buckley et al., 2011, CD002041)** concluded evidence is **insufficient/conflicting** to define which patients benefit — HBO remains standard practice for severe poisoning at many centers despite equipoise.

**Pharmacogenomics / targeted / gene / cell / RNA therapies:** **Not Applicable** (no molecular-target drug therapy). Experimental adjuncts studied mainly in models: **erythropoietin** (neuroprotection; rat serum-biomarker study PMC3586885), **N-acetylcysteine**, hypothermia, and — as an experimental *antidote concept* — engineered high-affinity CO-scavenger molecules (e.g., recombinant neuroglobin/"CO-scavenger" therapeutics in preclinical development to accelerate CO removal). None are approved.

**Treatment strategy summary.** All symptomatic patients → immediate high-flow 100% O₂ + supportive care; risk-stratify (LOC, neuro deficit, cardiac ischemia, acidosis, COHb, pregnancy) → refer for **HBO** if indicated and available within the therapeutic window. Arrange **neuropsychological follow-up** to detect DNS.

**Adverse events.** HBO risks: barotrauma (middle ear/sinus, rare pulmonary), oxygen toxicity seizures, confinement anxiety, transient myopia. Normobaric high-FiO₂ is generally safe over the short treatment course.

*Sources:* [UHMS HBO indications 2020](https://www.uhms.org/carbon-monoxide-poisoning/carbon-monoxide-poisoning.html); [Weaver NEJM 2002](https://pubmed.ncbi.nlm.nih.gov/12362006/); [Thom 1995 PMID 7710151](https://pubmed.ncbi.nlm.nih.gov/7710151/); [Scheinkestel 1999 PMID 10092916](https://pubmed.ncbi.nlm.nih.gov/10092916/); [Cochrane CD002041](https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD002041.pub3/references).

---

## 13. Prevention

**Primary prevention (the highest-yield domain).**
- **CO alarms/detectors** in homes near sleeping areas and on every level (MAXO/behavioral: environmental intervention). Legislative mandates for residential CO alarms reduce fatalities; battery replacement and testing emphasized.
- **Appliance safety:** annual professional inspection/maintenance of furnaces, water heaters, and vents; never use ovens/ranges for heating.
- **Generator safety:** operate portable generators **outdoors, ≥20 ft from windows/doors/vents**, never indoors/garages (key message during storms/outages).
- **Vehicle/engine safety:** never run engines in attached/closed garages; check exhaust systems.
- **No indoor charcoal grills / camp stoves.**
- **Public health education**, especially before winter and after disasters; CDC/EPA campaigns.

**Secondary prevention (early detection).**
- CO alarms detecting dangerous ambient levels before symptoms; prompt evaluation of clustered household symptoms; consider CO in nonspecific winter illness ("influenza-like" clusters).

**Tertiary prevention (limiting sequelae in the poisoned).**
- Prompt high-flow/hyperbaric oxygen within the therapeutic window; neuropsychological follow-up to identify and rehabilitate DNS; removal/remediation of the CO source before discharge to prevent re-exposure.

**Prophylaxis / immunization / genetic screening / counseling:** vaccination and genetic counseling are **Not Applicable**. "Prophylaxis" = engineering/behavioral source control + alarms.

*Sources:* [CDC clinical/disaster guidance](https://www.cdc.gov/carbon-monoxide/hcp/clinical-guidance/index.html); [Yoon 1998 PMID 9496987](https://pubmed.ncbi.nlm.nih.gov/9496987/).

---

## 14. Other Species / Natural Disease

- **Taxonomy / cross-species susceptibility:** CO is toxic to **all aerobic, hemoglobin-bearing animals** — mechanism (heme binding) is evolutionarily conserved. Species commonly poisoned alongside humans include **domestic dog (Canis lupus familiaris, `NCBITaxon:9615`)** and **cat (Felis catus, `NCBITaxon:9685`)** — pets are a classic "sentinel" for household CO exposure. Also documented in birds (historically the "canary in the coal mine," *Serinus canaria*), which are especially sensitive due to high metabolic/respiratory rates.
- **Natural/veterinary disease:** accidental CO poisoning occurs in companion animals (house fires, faulty heaters, vehicle transport) and livestock in poorly ventilated heated barns; veterinary toxicology recognizes it with a pathophysiology mirroring humans. Not a Mendelian OMIA entry (it is a toxic exposure).
- **Comparative biology:** rodents show the same globus-pallidus/hippocampal vulnerability, MBP-adduct autoimmunity, and DNS-like learning deficits, validating cross-species conservation of both the hypoxic and immune arms.
- **Zoonotic potential:** **None — Not Applicable** (non-infectious).

*Sources:* [Thom PNAS 2004 (rat)](https://pmc.ncbi.nlm.nih.gov/articles/PMC518809/); veterinary toxicology consensus (background).

---

## 15. Model Organisms

- **Rat (Rattus norvegicus, `NCBITaxon:10116`)** — the dominant model. Standard induced-exposure protocols (e.g., 1,000 ppm 40 min then 3,000 ppm 20 min) reproduce: transient **hippocampal MBP degradation** (Hara et al., **PMID 20633582**), **immune-mediated delayed neuropathology** and learning deficits (Thom et al., **PMID 15342916**), decreased hippocampal neural precursor cells in DEACMP models (Nat Sci Rep, s41598-021-85860-9), altered nicotinic cholinergic signaling (**PMID 24704181**), and neuroprotection studies (erythropoietin, PMC3586885). **Model type:** induced (inhalational exposure), not genetic.
- **Mouse (Mus musculus, `NCBITaxon:10090`)** — used for oxidative-stress/ROS-source dissection (mitochondria/xanthine oxidase/NADPH oxidase) and inflammatory-pathway studies; transgenic/knockout mice (e.g., NOS, NADPH oxidase subunits) dissect specific mechanistic arms.
- **In vitro / cellular:** neuronal and oligodendrocyte cultures, endothelial–neutrophil adhesion assays, and mitochondrial respiration assays (Complex IV inhibition).

**Phenotype recapitulation.** Rodent models reproduce the **biphasic course** (acute exposure → delayed neuropathology), the **globus-pallidus/hippocampal** vulnerability, **demyelination**, and the **autoimmune anti-MBP** mechanism — strong construct/face validity, including the pivotal MBP-tolerance experiment establishing causation.

**Limitations.** Species differences in CO tolerance and COHb kinetics; some protocols produce MBP degradation **without** measurable cognitive deficit (dose-dependence), highlighting a **human–model translational caveat** (`HUMAN_MODEL_MISMATCH`): the immune-mediated DNS mechanism is best characterized in rodents, and its quantitative fidelity to human DNS remains an open translational question.

**Resources:** MGI/RGD for mouse/rat strains; primary literature via PubMed. No dedicated CO-poisoning model repository (it is an induced-exposure paradigm, not a genetic line).

*Sources:* [Thom PNAS 2004 PMID 15342916](https://pmc.ncbi.nlm.nih.gov/articles/PMC518809/); [MBP degradation PMID 20633582](https://pubmed.ncbi.nlm.nih.gov/20633582/); [Neural precursor cells Sci Rep](https://www.nature.com/articles/s41598-021-85860-9); [Nicotinic cholinergic PMID 24704181](https://pubmed.ncbi.nlm.nih.gov/24704181/).

---

## Ontology Term Quick-Reference (for KB population)

| Domain | Term | ID |
|---|---|---|
| Disease | carbon monoxide poisoning | MONDO:0021113 *(verify)* |
| Chemical (toxicant) | carbon monoxide | CHEBI:17245 |
| Chemical (therapy) | dioxygen | CHEBI:15379 |
| Chemical (source) | dichloromethane | CHEBI:15767 |
| Phenotype | Headache | HP:0002315 |
| Phenotype | Syncope | HP:0001279 |
| Phenotype | Seizure | HP:0001250 |
| Phenotype | Confusion | HP:0001289 |
| Phenotype | Parkinsonism | HP:0001300 |
| Phenotype | Memory impairment | HP:0002354 |
| Phenotype | Myocardial infarction | HP:0001658 |
| Phenotype | Nausea and vomiting | HP:0002017 |
| Phenotype | Dyspnea | HP:0002094 |
| Process | oxidative phosphorylation | GO:0006119 |
| Process | mito. electron transport, cyt c → O₂ | GO:0006123 |
| Process | response to oxidative stress | GO:0006979 |
| Process | ROS metabolic process | GO:0072593 |
| Process | cellular response to hypoxia | GO:0071456 |
| Process | inflammatory response | GO:0006954 |
| Process | adaptive immune response | GO:0002250 |
| Cell | neuron | CL:0000540 |
| Cell | oligodendrocyte | CL:0000128 |
| Cell | microglial cell | CL:0000129 |
| Cell | CD4+ T cell | CL:0000624 |
| Cell | erythrocyte | CL:0000232 |
| Cell | cardiac myocyte | CL:0000746 |
| Anatomy | brain | UBERON:0000955 |
| Anatomy | globus pallidus | UBERON:0001875 |
| Anatomy | cerebral white matter | UBERON:0002316 |
| Anatomy | hippocampus | UBERON:0002421 |
| Anatomy | heart | UBERON:0000948 |
| Subcellular | mitochondrion | GO:0005739 |
| Subcellular | respiratory chain complex IV | GO:0005751 |
| Subcellular | myelin sheath | GO:0043209 |
| Treatment | oxygen therapy | MAXO:0035013 *(verify)* |
| Treatment | hyperbaric oxygen therapy | MAXO:0000257 *(verify)* |
| Treatment | supportive care | MAXO:0000950 |
| Lab | Carboxyhemoglobin/Hb.total | LOINC 20563-3 |

---

## Curation Caveats (dismech-specific)

1. **Verify every ontology ID before committing** — MONDO:0021113 and the MAXO oxygen/HBO IDs are provisional in this report (OLS/OAK not confirmed in-session). Run `just validate-terms-file` and `runoak … info` per the anti-hallucination SOP.
2. **All snippets must be exact abstract quotes** — this report paraphrases sources; before entering any `evidence:` snippet, run `just fetch-reference PMID:XXXX` and confirm the exact substring (e.g., PMIDs 12362006, 7710151, 15342916, 24773392, 20633582, 32594050, 24704181, 10092916, 9496987).
3. **`evidence_source` tagging:** Weaver/Thom-1995/Scheinkestel = HUMAN_CLINICAL; Thom PNAS 2004, MBP-degradation, EPO, nicotinic-cholinergic studies = MODEL_ORGANISM; ROS-source dissection = mix of IN_VITRO/MODEL_ORGANISM (split items accordingly).
4. **Genetic/inheritance sections should be curated as explicitly N/A** or omitted — this is an environmental exposure, not a Mendelian disease.
5. **Key `KNOWLEDGE_GAP` / `HUMAN_MODEL_MISMATCH` candidates:** (a) whether the rodent anti-MBP autoimmune DNS mechanism quantitatively explains human delayed encephalopathy; (b) which patients benefit from HBO (unresolved per Cochrane); (c) validity of serum biomarkers (S100B/NSE/GFAP) for DNS prediction.

### Primary sources cited
- [Weaver LK et al., NEJM 2002 — PMID 12362006](https://pubmed.ncbi.nlm.nih.gov/12362006/)
- [Thom SR et al., DNS prevention by HBO, 1995 — PMID 7710151](https://pubmed.ncbi.nlm.nih.gov/7710151/)
- [Scheinkestel CD et al., MJA 1999 — PMID 10092916](https://pubmed.ncbi.nlm.nih.gov/10092916/)
- [Thom SR et al., "Delayed neuropathology…is immune-mediated," PNAS 2004;101:13660 — PMID 15342916](https://pmc.ncbi.nlm.nih.gov/articles/PMC518809/)
- [ROS & oxidative stress in CO toxicity review — PMID 24773392](https://pubmed.ncbi.nlm.nih.gov/24773392/)
- [Transient MBP degradation in rat hippocampus — PMID 20633582](https://pubmed.ncbi.nlm.nih.gov/20633582/)
- [Mechanism of delayed encephalopathy — PMID 32594050](https://pubmed.ncbi.nlm.nih.gov/32594050/)
- [Yoon SS et al., CO deaths & detectors, 1998 — PMID 9496987](https://pubmed.ncbi.nlm.nih.gov/9496987/)
- [StatPearls Carboxyhemoglobin Toxicity — NBK557888](https://www.ncbi.nlm.nih.gov/books/NBK557888/)
- [UHMS HBO Indications — CO Poisoning (2020)](https://www.uhms.org/carbon-monoxide-poisoning/carbon-monoxide-poisoning.html)
- [CDC CO mortality QuickStats & clinical guidance](https://www.cdc.gov/carbon-monoxide/hcp/clinical-guidance/index.html)
- [AJNR — Pallidoreticular DWI in acute CO poisoning](https://www.ajnr.org/content/26/7/1845)
- [Cochrane — HBO for CO poisoning (Buckley 2011, CD002041)](https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD002041.pub3/references)

---

**Bottom line:** Carbon monoxide poisoning is an acute environmental toxic-inhalation syndrome (`MONDO:0021113`, ICD-10 T58, MeSH D002249) with no genetic etiology. Its pathophysiology is a **dual insult** — carboxyhemoglobin-mediated hypoxia *plus* direct mitochondrial/heme-protein toxicity, oxidative/ischemia-reperfusion injury, and a distinctive **immune-mediated (anti-MBP) delayed demyelinating** cascade that produces delayed neuropsychiatric sequelae. The brain (globus pallidus, white matter, hippocampus) and heart bear the injury. Management is **100% oxygen ± hyperbaric oxygen** (benefit best-supported by Weaver 2002 but contested by Scheinkestel/Cochrane), and the disease is **highly preventable** through CO alarms and combustion-source safety. Curate the genetic/inheritance sections as Not Applicable, verify all ontology IDs and PMID snippets against the dismech validation stack before committing, and flag the HBO-benefit question and rodent-DNS translational fidelity as knowledge gaps.