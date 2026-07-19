---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-07T02:52:15.795242'
end_time: '2026-07-07T02:57:54.893269'
duration_seconds: 339.1
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Primary Hyperoxaluria Type 3
  mondo_id: ''
  category: Metabolic Disorder
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
  num_turns: 17
  total_cost_usd: 2.13149125
  session_id: fab95771-0fe2-4c5e-bf35-f309244dff91
  stop_reason: end_turn
citation_count: 16
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Primary Hyperoxaluria Type 3
- **MONDO ID:**  (if available)
- **Category:** Metabolic Disorder

## Research Objectives

Please provide a comprehensive research report on **Primary Hyperoxaluria Type 3** covering all of the
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

I now have comprehensive, well-sourced data across all sections. Here is the complete research report.

---

# Research Report: Primary Hyperoxaluria Type 3 (PH3)

**Category:** Metabolic disorder (inborn error of glyoxylate/hydroxyproline metabolism)
**Suggested MONDO ID:** MONDO:0013327 (primary hyperoxaluria type 3)

> **Evidence-provenance note for curators:** This report aggregates disease-level resources (OMIM, Orphanet, GeneReviews) and published cohort/mechanistic studies. It is **not** derived from individual patient EHR data. Per the dismech anti-hallucination SOP, every PMID and quoted snippet below must be independently re-verified against the real PubMed abstract with `just fetch-reference PMID:XXXX` before being committed as an evidence `snippet:`. Several PMIDs were confirmed in-search; a few landmark/therapeutic PMIDs are recalled and are flagged for verification.

---

## 1. Disease Information

**Overview.** Primary hyperoxaluria type 3 (PH3) is an autosomal recessive inborn error of **glyoxylate/4-hydroxyproline metabolism** caused by biallelic loss-of-function variants in *HOGA1*, encoding the mitochondrial enzyme 4-hydroxy-2-oxoglutarate aldolase. Loss of this enzyme results in excessive **endogenous oxalate** synthesis and recurrent **calcium oxalate nephrolithiasis**, typically beginning in early childhood. It is the **most recently described** and generally the **least severe** of the three classic primary hyperoxalurias, with kidney function preserved in most patients and (to date) **no reported systemic oxalosis**.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM (disease) | **613616** — HYPEROXALURIA, PRIMARY, TYPE III; HP3 |
| OMIM (gene) | **613597** — *HOGA1* |
| MONDO | **MONDO:0013327** (primary hyperoxaluria type 3) |
| Orphanet | **ORPHA:93600** (primary hyperoxaluria type 3) |
| ICD-10 | E72.53 (primary hyperoxaluria) |
| ICD-11 | 5C51.20 (primary hyperoxaluria) |
| MeSH | Hyperoxaluria, Primary (D006960) |
| Gene (NCBI) | 112817; **HGNC:25155**; cytoband 10q24.2 |

**Synonyms / alternative names:** PH3; PH III; HP3; hyperoxaluria, primary, type III; *HOGA1*-related hyperoxaluria; historically associated with the gene name **DHDPSL** (dihydrodipicolinate synthase-like), the original name of *HOGA1* at discovery.

Sources: [OMIM 613616](https://omim.org/entry/613616); [GeneReviews: PH3, NBK316514](https://www.ncbi.nlm.nih.gov/books/NBK316514/) (PMID:26401545); [MedlinePlus: HOGA1](https://medlineplus.gov/genetics/gene/hoga1/).

---

## 2. Etiology

**Primary causal factor (genetic).** PH3 is caused by **homozygous or compound heterozygous pathogenic variants in *HOGA1*** (10q24.2). The disease was first defined by Belostotsky et al., who mapped it to *DHDPSL/HOGA1* — *"Mutations in DHDPSL Are Responsible for Primary Hyperoxaluria Type III"* (Belostotsky R et al., *Am J Hum Genet* 2010; **PMID:20797690** — verify). The gene product is a mitochondrial aldolase; its loss increases endogenous oxalate production (OMIM 613616; GeneReviews PMID:26401545).

**Genetic risk factors.**
- Biallelic *HOGA1* pathogenic variants are **necessary and sufficient** to cause the Mendelian disease.
- **Carrier / heterozygous state as a stone risk modifier:** Monico et al. proposed that *HOGA1* may be a risk factor for idiopathic calcium oxalate urolithiasis even in heterozygotes — *"Primary Hyperoxaluria Type III Gene HOGA1 (Formerly DHDPSL) as a Possible Risk Factor for Idiopathic Calcium Oxalate Urolithiasis"* (PMID:21896830).
- **Consanguinity / founder effects** increase homozygote frequency in specific populations (see §9).

**Environmental / lifestyle contributors (disease-modifying, not causal).**
- **Dietary oxalate and hydroxyproline load** (collagen-rich foods, gelatin) can raise the substrate pool feeding oxalate synthesis.
- **Dehydration / low fluid intake and low urinary citrate** promote calcium oxalate supersaturation and stone formation.
- **High-dose vitamin C (ascorbate)** is a precursor to oxalate and is discouraged.

**Gene–environment interaction.** The genotype sets excess endogenous oxalate production, but **clinical stone burden is modulated by urine volume, citrate, calcium, and dietary oxalate/hydroxyproline** — hence the mainstays of management are hydration and citrate rather than gene-directed therapy (GeneReviews PMID:26401545).

---

## 3. Phenotypes

PH3 is dominated by **stone-related urologic phenotypes** and **biochemical (laboratory) abnormalities**, with kidney-function decline in a minority.

| Phenotype | Type | Onset / course | Frequency in PH3 | Suggested HPO term |
|---|---|---|---|---|
| Recurrent calcium oxalate **nephrolithiasis** (kidney stones) | Clinical sign | Median onset 2–3 y; recurrent through adulthood | Near-universal in symptomatic patients (~89% have stones at first evaluation) | **HP:0000787** Nephrolithiasis / HP:0008672 CaOx nephrolithiasis |
| **Hyperoxaluria** (elevated urinary oxalate) | Lab abnormality | From infancy | Defining; median ~1.1 mmol/1.73 m²/day (lowest of the three PH types) | **HP:0003159** Hyperoxaluria |
| **Hematuria** | Clinical sign | With stone episodes | Common | **HP:0000790** Hematuria |
| **Dysuria / urinary frequency** | Symptom | With stones/UTI | Common | HP:0100518 Dysuria; HP:0100515 Urinary frequency |
| **Renal/ureteral colic (flank pain)** | Symptom | Episodic with stones | Common | HP:0012622 (Chronic kidney disease context) / stone pain |
| **Urinary tract infection** | Clinical sign | Recurrent with stones | Frequent | **HP:0000010** Recurrent UTI |
| **Nephrocalcinosis** | Imaging/lab sign | Childhood | ~7% at diagnosis (vs 26% PH1, 16% PH2) | **HP:0000121** Nephrocalcinosis |
| **Hypercalciuria** | Lab abnormality | — | ~10% (vs ~2% PH1) | **HP:0002150** Hypercalciuria |
| **Elevated urinary 4-hydroxy-2-oxoglutarate (HOG)** | Lab biomarker | From onset; declines with age | Highly characteristic (see §10) | (no specific HP term; use HP:0003159 parent) |
| **Elevated urinary 2,4-dihydroxyglutarate (DHG)** | Lab biomarker | — | Characteristic | (no specific HP term) |
| **Chronic kidney disease / reduced eGFR** | Clinical sign | Later, minority | ~2.9% reach ESKD by age 40 | **HP:0012622** Chronic kidney disease; HP:0003774 Stage 5 CKD |

**Phenotype characteristics.**
- **Age of onset:** Earliest of the three PH types. Median symptomatic onset **~2.7 years**; some patients present only in adulthood (PMID:33543760).
- **Severity:** Generally **mild-to-moderate**; recurrent stones dominate. *"Compared to hyperoxaluria type I and type II, HP3 appears to be the least severe, with good preservation of kidney function in most patients"* (OMIM 613616).
- **Progression:** Recurrent/episodic stone events that can persist into the sixth decade; kidney function usually stable, but CKD (including rare kidney failure) does occur.
- **Quality-of-life impact:** Driven by recurrent painful stone episodes, procedures, and infections; formal QoL instrument data specific to PH3 are limited/not available.

Sources: [Clinical characterization of PH3 vs PH1/PH2](https://pmc.ncbi.nlm.nih.gov/articles/PMC9214566/) (PMID:33543760); GeneReviews (PMID:26401545).

---

## 4. Genetic / Molecular Information

**Causal gene:** ***HOGA1*** (4-hydroxy-2-oxoglutarate aldolase 1; formerly *DHDPSL*), **HGNC:25155**, OMIM **613597**, chromosome **10q24.2**, NCBI Gene 112817. It has **7 coding exons** encoding the mitochondrial aldolase (UniProt Q86XE5; suggested **GO:0008700**-related aldolase activity; see §6).

**Pathogenic variant spectrum.**
- **>50 disease-associated variants** reported to date; the majority are **missense** variants, with a **loss-of-function** mechanism (unstable, aggregation-prone, catalytically inactive protein). *"All nine examined PH3 variants were found to be unstable, aggregation-prone, and enzymatically inactive"* (Riedel et al., PMID:22771891). A **dominant-negative** contribution has also been proposed for some alleles (Abid et al., *Hum Mutat* 2022, PMID:36259736).
- **Common/recurrent alleles:**
  - **c.700+5G>T** — a splice-site variant; the **most common allele in European/non-Ashkenazi populations** (reported allelic frequencies ~35–46%; potential founder mutation) (PMID:22781098; PMID:33948853).
  - **c.944_946delAGG (p.Glu315del)** — the predominant **Ashkenazi Jewish founder allele** (~66% of Ashkenazi PH3 alleles per GeneReviews).
  - **c.107C>T (p.Ala36Val)** — second common Ashkenazi allele (~22%).
- **Variant classification:** ACMG/AMP classifications (pathogenic/likely pathogenic vs VUS) are curated in **ClinVar**; OMIM lists ≥24 disease-causing variants.
- **Origin:** **Germline**; **autosomal recessive**. No somatic mechanism.
- **Functional consequence:** **Loss of function** (protein instability + loss of aldolase activity), possibly with dominant-negative effects on the tetramer.

**Modifier genes.** Not formally established. Because accumulated HOG inhibits **GRHPR** (the PH2 enzyme), *GRHPR* activity/variation is a plausible mechanistic modifier of oxalate output (see §6).

**Epigenetics / chromosomal abnormalities.** No disease-specific DNA-methylation, histone-modification, aneuploidy, or structural-rearrangement associations are described for PH3. Diagnosis relies on sequencing, not cytogenetics.

Sources: [Abid et al. 2022, *Hum Mutat*](https://pubmed.ncbi.nlm.nih.gov/36259736/); [Beck et al. — novel findings/molecular testing](https://pubmed.ncbi.nlm.nih.gov/22781098/); [Ethnic associations of HOGA1 variants](https://pubmed.ncbi.nlm.nih.gov/33948853/); GeneReviews (PMID:26401545).

---

## 5. Environmental Information

- **Environmental/toxic factors:** No infectious or toxic environmental cause; PH3 is purely genetic. Relevant exogenous modifiers are **dietary oxalate**, **dietary hydroxyproline** (collagen/gelatin), and **high-dose ascorbic acid** (oxalate precursor).
- **Lifestyle factors:** **Fluid intake** (low volume worsens supersaturation), and dietary patterns affecting urinary citrate/calcium. Adequate hydration is protective (see §13).
- **Infectious agents:** Not applicable as a cause; however, **urinary tract infections** are a frequent secondary complication of stone disease.

---

## 6. Mechanism / Pathophysiology

**Normal pathway (mitochondrial hydroxyproline degradation).** Dietary and endogenous collagen turnover supplies **4-hydroxyproline** (~**300–450 mg/day** from endogenous collagen turnover). In the mitochondrion, hydroxyproline is metabolized through several steps to **4-hydroxy-2-oxoglutarate (HOG)**. **HOGA1** catalyzes the final step — a **retro-aldol cleavage of HOG into glyoxylate + pyruvate** (suggested biological process **GO:0019471** 4-hydroxyproline catabolic process; molecular function: aldolase/lyase activity). Glyoxylate is normally detoxified by:
- **AGT (AGXT, peroxisomal, PLP-dependent alanine–glyoxylate aminotransferase)** → glycine (defective in PH1), and
- **GR/GRHPR (glyoxylate reductase/hydroxypyruvate reductase, cytosolic)** → glycolate (defective in PH2).
Any glyoxylate escaping detoxification is oxidized by **LDH (lactate dehydrogenase)** to **oxalate**.

**PH3 mechanism (loss of HOGA1).** Loss of HOGA1 aldolase activity causes **accumulation of HOG** in urine, serum, and liver. Two complementary, still-debated mechanisms convert this into oxalate overproduction:

1. **HOG-mediated inhibition of glyoxylate reductase (GRHPR)** — the leading biochemical model. Accumulated HOG **specifically inhibits GR**, phenocopying PH2: *"GR was inhibited by HOG but not by 2-hydroxyglutarate or 2-oxoglutarate"* (Riedel et al., **PMID:22771891**). With GR inhibited, glyoxylate is not efficiently reduced to glycolate and is instead shunted to **oxalate** via LDH.
2. **Ectopic/cytosolic cleavage of accumulated HOG**, liberating glyoxylate outside the mitochondrion where detoxification capacity is limited, feeding oxalate synthesis.

**Enzyme structure/function.** HOGA1 is a **mitochondrial homotetramer** ("dimer of dimers"); each monomer has an **(α/β)₈ TIM-barrel** catalytic domain plus a C-terminal three-helix bundle. It uses a **Type I aldolase mechanism** with a **Schiff-base–forming catalytic Lys196** (proton relay via Tyr168/Ser77); **no metal cofactor** is required. Disease variants disrupt either the **active site** or **tetramer assembly**, and are unstable/aggregation-prone (Riedel et al., **PMID:21998747**; PLOS One PMC3188589). HOGA activity is additionally regulated by **pyruvate and α-ketoglutarate** (product/substrate feedback), relevant to PH3 (PMID:31696211).

**Protein dysfunction:** Loss of function via misfolding/aggregation and loss of catalytic activity (possible dominant-negative on the tetramer).

**Metabolic changes:** Elevated **HOG** and its reduction product **2,4-dihydroxyglutarate (DHG)**; increased net **oxalate** synthesis; urinary glycolate/glycerate typically **normal** (distinguishing from PH1/PH2).

**Tissue damage mechanism:** **Calcium oxalate crystal deposition** → crystal nucleation/aggregation → mechanical/inflammatory tubular injury, stone formation, occasional nephrocalcinosis, and — over time in a minority — chronic kidney injury. (Notably, **systemic oxalosis has not been reported** in PH3, unlike PH1.)

**Cell types & anatomy involved:** Hepatic **mitochondria** (site of HOGA1 expression and oxalate overproduction; suggested **CL:0000182** hepatocyte, **GO:0005739** mitochondrion) and **renal tubular epithelium** (site of crystal-related injury; suggested **CL:1000507**/renal tubule epithelial cells, **UBERON:0002113** kidney).

**Molecular profiling:** No large-scale disease-specific transcriptomic/proteomic/single-cell datasets for PH3; the field is characterized by **targeted metabolomics** (urine/plasma HOG, DHG, oxalate quantitation by LC-MS/MS) and enzyme kinetics.

**Chemical entities (CHEBI suggestions):** oxalate (**CHEBI:30623**), glyoxylate (**CHEBI:16891**), 4-hydroxyproline (**CHEBI:18095**), 4-hydroxy-2-oxoglutarate/HOG, 2-oxoglutarate (**CHEBI:16810**), pyruvate (**CHEBI:15361**), glycolate (**CHEBI:17497**), citrate (**CHEBI:30769**).

Sources: [Structural/biochemical HOGA (PLOS One)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0026021) (PMID:21998747); [HOGA inactivity & GR inhibition](https://pmc.ncbi.nlm.nih.gov/articles/PMC3418427/) (PMID:22771891); [Regulation of HOGA by pyruvate/α-KG](https://pubmed.ncbi.nlm.nih.gov/31696211/) (PMID:31696211).

---

## 7. Anatomical Structures Affected

- **Primary organ affected clinically:** **Kidney / urinary tract** (**UBERON:0002113** kidney; UBERON:0000056 ureter; UBERON:0001255 urinary bladder) — recurrent calcium oxalate stones, occasional nephrocalcinosis.
- **Primary organ of the metabolic defect:** **Liver** (**UBERON:0002107**) — hepatic mitochondria are the site of HOGA1 expression and oxalate overproduction.
- **Body systems:** Renal/urinary system (primary); hepatic/metabolic (biochemical origin).
- **Tissue/cell level:** **Renal tubular epithelium** (crystal-associated injury), **hepatocytes** (**CL:0000182**).
- **Subcellular level:** **Mitochondrion** (**GO:0005739**) — HOGA1 localization and HOG cleavage; cytosol — glyoxylate/oxalate handling.
- **Localization/laterality:** Stones/nephrocalcinosis are typically **bilateral** but can be unilateral; distribution follows the collecting system.

---

## 8. Temporal Development

- **Onset:** **Early childhood**, earliest of the three PH types — median symptomatic onset **~2.7 years**; stones usually begin **before age 5**. Some patients are diagnosed only in **adulthood** (PMID:33543760; GeneReviews PMID:26401545).
- **Onset pattern:** Insidious biochemically (lifelong hyperoxaluria) with **episodic** clinical stone events.
- **Course:** **Chronic, recurrent, relapsing** stone disease that can continue into the **sixth decade**; kidney function is **usually stable**.
- **Stages/progression:** Most patients remain in early CKD stages; a **minority** progress to CKD 3–5. A 2024 single-cohort report described one patient reaching **CKD stage 5** and two others at **CKD stage 2** at last follow-up (Pediatric Nephrology 2024, doi:10.1007/s00467-024-06536-w).
- **Critical windows:** Early diagnosis and initiation of hydration/citrate before repeated obstructive/infectious insults; closer monitoring for children <4 years and those with reduced kidney function.

---

## 9. Inheritance and Population

**Inheritance:** **Autosomal recessive** (25% recurrence risk per pregnancy for carrier couples). Suggested HPO mode-of-inheritance term: **HP:0000007** Autosomal recessive inheritance.

**Penetrance / expressivity:** Biochemical penetrance (hyperoxaluria) is essentially complete in biallelic carriers; **clinical expressivity is variable** (stone burden and kidney outcomes differ widely, even within genotype). No genetic anticipation (not a repeat-expansion disorder).

**Epidemiology:**
- Overall primary hyperoxaluria prevalence: **~1–3 per 1,000,000**.
- **PH3 constitutes ~7–12%** of all primary hyperoxaluria cases (~10% commonly cited).
- Estimated PH3 prevalence: **~1 per 136,000** (GeneReviews).
- **Carrier frequency:** ~**1 in 185** general population; **~1 in 55** in Ashkenazi Jews (GeneReviews; PMID:33948853).

**Founder effects / population genetics:**
- **Ashkenazi Jewish** founder alleles: **c.944_946delAGG (p.Glu315del)** and **c.107C>T (p.Ala36Val)**.
- **European/non-Ashkenazi:** **c.700+5G>T** splice variant predominates (potential founder; ~35–46% of alleles).
- **Consanguinity** increases homozygous disease in some populations; genetically homogeneous founder cohorts have been described.

**Demographics:** No strong sex predilection reported; onset in early childhood; enrichment in populations carrying founder alleles (Ashkenazi Jewish; specific European and Middle Eastern groups).

Sources: GeneReviews (PMID:26401545); [Ethnic associations of HOGA1 variants](https://pubmed.ncbi.nlm.nih.gov/33948853/); [Beck et al.](https://pubmed.ncbi.nlm.nih.gov/22781098/).

---

## 10. Diagnostics

**Biochemical (urine/blood):**
- **24-hour urinary oxalate:** Elevated (>0.7 mmol/1.73 m²/day); PH3 shows the **lowest oxalate** of the three types (median ~**1.1 mmol/1.73 m²/day**). LOINC-type analyte: urine oxalate.
- **Urinary HOG (4-hydroxy-2-oxoglutarate):** **The key discriminating biomarker** — markedly elevated in PH3 (median ~**110 mg/g creatinine**, normal <10) and essentially **absent in PH1/PH2**; described as *"an excellent biomarker for PH3 diagnosis"* and **decreases with age** (PMID:33543760).
- **Urinary 2,4-dihydroxyglutarate (DHG):** Elevated; complementary PH3 marker (LC-MS/MS).
- **Urinary glycolate (PH1) and glycerate (PH2):** typically **normal** in PH3 — helps differentiate.
- **Urine citrate:** normal (contrasts with PH1); **urine calcium:** normal-to-mildly high (hypercalciuria ~10%).
- **Plasma oxalate:** mildly elevated only with reduced GFR.

**Imaging:** Renal **ultrasound / CT** for stones and nephrocalcinosis; stone analysis shows **calcium oxalate** (often mixed mono-/dihydrate — ~36% mixed in PH3).

**Genetic testing (confirmatory / gold standard):**
- **Single-gene *HOGA1* sequencing** and deletion/duplication analysis, or a **primary hyperoxaluria multigene panel** (*AGXT*, *GRHPR*, *HOGA1*), or WES/WGS. Testing is available (e.g., GTR-listed labs; PreventionGenetics).
- Chromosomal microarray/karyotype/FISH/mtDNA testing are **not** indicated.

**Clinical criteria / differential diagnosis:** Diagnosis rests on **hyperoxaluria + elevated HOG/DHG + biallelic *HOGA1* variants**. Differentiate from:
- **PH1** (*AGXT*): higher oxalate, high glycolate, ~64% ESKD by 40, systemic oxalosis.
- **PH2** (*GRHPR*): elevated urinary glycerate, ~34% ESKD by 40.
- **Idiopathic calcium oxalate stones / secondary (enteric, dietary, medication) hyperoxaluria.**

**Screening:** **Carrier / cascade testing** for relatives once familial variants are known; targeted screening in founder populations (Ashkenazi Jewish).

Sources: [Clinical characterization PH1/2/3](https://pmc.ncbi.nlm.nih.gov/articles/PMC9214566/) (PMID:33543760); GeneReviews (PMID:26401545).

---

## 11. Outcome / Prognosis

- **Kidney survival is favorable** — the defining prognostic feature. **ESKD by age 40 is only ~2.9%** in PH3, versus **~63.8% in PH1** and **~34.2% in PH2** (PMID:33543760).
- **eGFR at diagnosis** is highest among PH types (~96 mL/min/1.73 m²).
- **Systemic oxalosis has not been reported** in PH3.
- **Kidney failure is possible but rare:** individual cases are documented — *"Primary Hyperoxaluria Type 3 Can Also Result in Kidney Failure: A Case Report"* (PMID:34245816) — and a 2024 cohort reported one CKD-5 patient (doi:10.1007/s00467-024-06536-w). Reported ESKD cases often have contributing factors.
- **Morbidity** is driven by **recurrent stones, colic, obstructive events, urologic procedures, and UTIs** rather than progressive kidney failure.
- **Prognostic factors:** degree of hyperoxaluria, stone/nephrocalcinosis burden, hydration/citrate adherence, and baseline kidney function. Life expectancy is essentially normal in most patients.

Sources: (PMID:33543760); (PMID:34245816); GeneReviews (PMID:26401545).

---

## 12. Treatment

There is **no PH3-specific approved disease-modifying drug**; management is **conservative/supportive and stone-directed**.

**Conservative (mainstay) — suggested MAXO terms noted:**
- **High fluid intake** (>2.5 L/m²/day) to lower supersaturation — MAXO: increased fluid intake / supportive care (**MAXO:0000950**).
- **Alkali citrate supplementation** (potassium/sodium citrate, ~1–3 mEq/kg/day) to inhibit CaOx crystallization — pharmacotherapy (**NCIT:C15986**; therapeutic agent citrate, CHEBI:30769).
- **Dietary modification** — limit oxalate/high-hydroxyproline foods, avoid high-dose ascorbate — MAXO dietary intervention (**MAXO:0000088**).
- **Thiazide diuretics** for hypercalciuria (selected patients).

**Stone/urologic management (interventional):**
- **Extracorporeal shock wave lithotripsy, ureteroscopy, percutaneous nephrolithotomy** as needed; prompt relief of obstruction; treat UTIs — surgical/therapeutic procedure (MAXO:0000004 / NCIT:C15329).

**RNAi / advanced therapeutics — important caveat for PH3:**
- **Lumasiran** (anti-*HAO1*/glycolate oxidase siRNA) and **nedosiran** (anti-*LDHA* siRNA) are approved/developed primarily for **PH1**. Lumasiran ILLUMINATE-A: *"84% of patients had 24-hour urinary oxalate excretion no higher than 1.5 times the upper limit of the normal range at month 6, as compared with 0% in the placebo group"* (Garrelfs et al., *NEJM* 2021, **PMID:33356090** — verify).
- **Mechanistic limitation in PH3:** glycolate-oxidase inhibition (lumasiran) is **not expected to reduce hepatic oxalate to the same extent** in HOGA1 deficiency; **more PH2/PH3 patients need testing**. Nedosiran (LDH-directed) is being studied across PH types but PH3 efficacy data remain limited.
- **Transplantation:** Rarely needed in PH3 (kidney failure is uncommon); combined liver–kidney transplantation (standard in severe PH1) is generally **not** required.

**Pharmacogenomics:** Not established for PH3.

Sources: [RNAi for PH systematic review](https://academic.oup.com/ckj/article/18/4/sfae383/7914171); [Nedosiran design/development](https://pubs.acs.org/doi/10.1021/acsptsci.2c00110); ERKNet/OxalEurope expert consensus, *Nat Rev Nephrol* 2023 ([s41581-022-00661-1](https://www.nature.com/articles/s41581-022-00661-1)).

---

## 13. Prevention

- **Primary prevention:** Not preventable (genetic); **genetic counseling** and reproductive options (carrier testing, prenatal/preimplantation genetic testing once familial variants known) — MAXO genetic counseling (**MAXO:0000079**).
- **Secondary prevention (early detection):** **Cascade/carrier screening** of relatives; targeted screening in founder populations (Ashkenazi Jewish); early biochemical/genetic diagnosis in children with early stones.
- **Tertiary prevention (complication avoidance):** Lifelong **hydration + citrate**, dietary control, avoidance of volume contraction, high-dose vitamin C, and nephrotoxins; prompt treatment of obstruction/UTI; **regular surveillance** (annual clinical assessment, kidney imaging, serum creatinine/eGFR, 24-h urine oxalate/supersaturation; more frequent for young children and impaired kidney function).
- **Immunization / public-health / environmental interventions:** Not applicable.

Sources: GeneReviews (PMID:26401545); ERKNet/OxalEurope consensus (*Nat Rev Nephrol* 2023).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Human disease (*Homo sapiens*, **NCBITaxon:9606**). No naturally occurring *HOGA1*-deficiency disease is well described in companion animals or wildlife (OMIA has no established PH3 entry analogous to human PH3). Calcium oxalate urolithiasis occurs naturally in dogs/cats but is not attributed to *HOGA1* loss.
- **Orthology:** *HOGA1* is **evolutionarily conserved** across vertebrates (mouse *Hoga1*, NCBI Gene present; conserved in the hydroxyproline-degradation pathway), enabling model-organism study.
- **Comparative biology:** The hydroxyproline→HOG→glyoxylate pathway is conserved; however (see §15) the **mouse phenotype does not fully recapitulate** human hyperoxaluria, an important interspecies difference.
- **Zoonotic potential / transmission:** None (non-communicable genetic disease).

---

## 15. Model Organisms

- **Mouse (*Hoga1* knockout):** The principal PH3 model. **Key finding & human–model mismatch:** *Hoga1*-null mice **did not develop hyperoxaluria on a hydroxyproline-free diet**, in marked contrast to PH3 patients, although **urine/plasma HOG and DHG and hepatic DHG were significantly elevated** — Li et al., *"Hydroxyproline metabolism in a mouse model of Primary Hyperoxaluria Type 3"* (PMID:26428388, PMC4615548), extended by *"4-hydroxy-2-oxoglutarate metabolism in a mouse model of Primary Hyperoxaluria Type 3"* (*Mol Genet Metab Rep* 2024, ScienceDirect S2405580824001298). This mismatch (**suggests `HUMAN_MODEL_MISMATCH`** rather than a clean phenotype recapitulation) indicates additional/diet-dependent factors in human oxalate overproduction.
- **In vitro / biochemical models:** **Recombinant human HOGA1** expression for enzyme kinetics, stability, and structural studies (crystal structures; Type I aldolase mechanism) — used to demonstrate variant instability/inactivity and HOG-mediated GRHPR inhibition (PMID:21998747; PMID:22771891; PMID:31696211).
- **Model utility:** Study of HOG/DHG metabolism, the reduction of HOG→DHG as a possible oxalate-limiting shunt, and metabolic perturbations of glyoxylate handling (PMID:22729392).
- **Limitations:** Mouse does not reproduce spontaneous hyperoxaluria; heavy reliance on dietary hydroxyproline loading; no robust stone-forming small-animal model of PH3.

Sources: [Hydroxyproline metabolism in Hoga1-KO mouse](https://pmc.ncbi.nlm.nih.gov/articles/PMC4615548/) (PMID:26428388); [HOG metabolism in PH3 mouse (2024)](https://www.sciencedirect.com/science/article/pii/S2405580824001298); [PH3 as a model for glyoxylate perturbations](https://pubmed.ncbi.nlm.nih.gov/22729392/) (PMID:22729392).

---

## Consolidated Ontology-Term Suggestions (for KB population)

- **MONDO:** MONDO:0013327 (primary hyperoxaluria type 3)
- **Gene (HGNC):** hgnc:25155 (HOGA1)
- **Phenotypes (HP):** HP:0000787 Nephrolithiasis; HP:0003159 Hyperoxaluria; HP:0000790 Hematuria; HP:0000121 Nephrocalcinosis; HP:0002150 Hypercalciuria; HP:0000010 Recurrent UTI; HP:0012622 CKD; HP:0000007 Autosomal recessive inheritance
- **Biological process (GO):** GO:0019471 4-hydroxyproline catabolic process; GO:0006979/oxidative response context; oxalate biosynthetic/metabolic process
- **Cellular component (GO):** GO:0005739 mitochondrion
- **Cell types (CL):** CL:0000182 hepatocyte; renal tubular epithelial cell
- **Anatomy (UBERON):** UBERON:0002113 kidney; UBERON:0002107 liver; UBERON:0000056 ureter; UBERON:0001255 urinary bladder
- **Chemicals (CHEBI):** CHEBI:30623 oxalate; CHEBI:16891 glyoxylate; CHEBI:18095 4-hydroxyproline; CHEBI:16810 2-oxoglutarate; CHEBI:15361 pyruvate; CHEBI:17497 glycolate; CHEBI:30769 citrate
- **Treatments (MAXO):** MAXO:0000950 supportive care; MAXO:0000088 dietary intervention; MAXO:0000079 genetic counseling; MAXO:0000004 surgical procedure

---

## Key Citations (verify PMIDs/snippets before KB entry)

| PMID / ID | Content | Verified in-search? |
|---|---|---|
| **26401545** | GeneReviews: Primary Hyperoxaluria Type 3 (clinical, genetics, management) | Yes |
| **33543760** | Clinical characterization of PH3 vs PH1/PH2 (HOG biomarker, ESKD rates) | Yes |
| **21998747** | Structural/biochemical HOGA1; TIM-barrel, Type I aldolase | Yes |
| **22771891** | HOGA1 inactivity + HOG-mediated GR/GRHPR inhibition | Yes |
| **31696211** | Regulation of HOGA1 by pyruvate/α-ketoglutarate | Yes |
| **21896830** | HOGA1 (DHDPSL) as risk factor for idiopathic CaOx urolithiasis | Yes |
| **22781098** | Novel findings / molecular testing (c.700+5G>T) | Yes |
| **36259736** | Abid et al. 2022 *Hum Mutat* variant spectrum + dominant-negative | Yes |
| **33948853** | Ethnic associations of HOGA1 variants | Yes |
| **34245816** | PH3 can result in kidney failure (case report) | Yes |
| **26428388** | Hydroxyproline metabolism in Hoga1-KO mouse (human–model mismatch) | Yes |
| **22729392** | PH3 as model for glyoxylate metabolism perturbations | Yes |
| doi:10.1007/s00467-024-06536-w | 2024 PH3 cohort (16 patients, CKD outcomes) | Yes (search) |
| **20797690** | Belostotsky et al. 2010 — original *DHDPSL/HOGA1* discovery | **Recalled — verify** |
| **33356090** | Garrelfs et al. NEJM 2021 — lumasiran ILLUMINATE-A (PH1) | **Recalled — verify** |
| *Nat Rev Nephrol* 2023 (s41581-022-00661-1) | ERKNet/OxalEurope PH clinical practice consensus | Yes (search) |

**Bottom line for the KB entry:** PH3 is an autosomal-recessive, *HOGA1*-driven inborn error of hydroxyproline/glyoxylate metabolism. Loss of mitochondrial 4-hydroxy-2-oxoglutarate aldolase causes HOG accumulation, which (chiefly via HOG-mediated GRHPR inhibition) shunts glyoxylate to oxalate, producing early-childhood-onset recurrent calcium oxalate nephrolithiasis. It is the **mildest** primary hyperoxaluria (low ESKD, no systemic oxalosis), diagnosed by elevated urinary **HOG/DHG** plus biallelic *HOGA1* variants (founder alleles c.700+5G>T in Europeans; p.Glu315del/p.Ala36Val in Ashkenazi Jews), and managed conservatively with hydration and citrate — RNAi therapies validated in PH1 have uncertain benefit in PH3.
