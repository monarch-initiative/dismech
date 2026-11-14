---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-11-11T16:44:37.104359'
end_time: '2026-11-11T16:58:29.288074'
duration_seconds: 832.18
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Embryonal Tumor with Multilayered Rosettes
  mondo_id: MONDO:0958119
  category: ''
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: not recorded
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
  - claude-opus-5
  web_search_requests: 55
  num_turns: 55
  total_cost_usd: 8.948434499999998
  session_id: 522f2bf4-2f41-40cd-bb9b-fca3d2937ccb
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 51
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Embryonal Tumor with Multilayered Rosettes
- **MONDO ID:** MONDO:0958119 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** 

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Embryonal Tumor with Multilayered Rosettes** covering all of the
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

I'll research this now. Let me load web search and start gathering sources.

Bash network access needs approval (non-interactive), so I'll work through web search. Running parallel searches now.

# Embryonal Tumor with Multilayered Rosettes (ETMR) — Comprehensive Disease Research Report

**Target:** Embryonal Tumor with Multilayered Rosettes · **MONDO:0958119** · ICD‑O **9478/3** · ORPHA:**656417** · WHO CNS grade 4
**Report date:** 11 November 2026

---

## ⚠️ Two reading caveats before the content

**1. "Causal gene" is the wrong frame for this entry, and the template's blank field is correct.** ETMR is a **somatic pediatric CNS neoplasm**, not a Mendelian disorder. There is no germline causal gene in the usual sense. The defining molecular lesion is **focal high‑level amplification (and fusion) of the C19MC microRNA cluster at chromosome 19q13.42** — a cluster of ~46 primate‑specific miRNAs (*MIR512‑1 … MIR519A2*), usually joined to **TTYH1** (HGNC symbol `TTYH1`, tweety family member 1). The key **protein** effector is **LIN28A**. A minority arm is driven by **biallelic *DICER1*** inactivation, and this arm *is* frequently germline (DICER1 tumour‑predisposition syndrome). A third, ~1% arm is **MIR17HG** (miR‑17‑92) amplification. These three lesions are mutually exclusive and all converge on miRNA‑pathway dysregulation. **Every mechanistic statement below names C19MC/LIN28A or DICER1 as the driver, as required.**

**2. All ontology CURIEs in this report are UNVERIFIED leads.** This session had no network access for `curl`/`runoak` (Bash network calls required interactive approval, which is unavailable non‑interactively), so no CURIE could be resolved against OAK, OLS, or a `cache/<prefix>/terms.csv` row *in the same step it was written*. Under this repository's rule — *Every CURIE is read from a source in the same step it is written* — **none of the identifiers below may be bound without a fresh lookup.** They are search hints, not bindings. The one exception resolved during research is `HP:0002516` = *Increased intracranial pressure*, confirmed via the Monarch Initiative term page. Similarly, **all abstract quotations are reconstructed from search-engine renderings of abstracts, not from fetched sources** — they must be regenerated with `just fetch-reference PMID:<id>` and re‑verified with `just count-verified-snippets` before any becomes an evidence `snippet:`. PMIDs are flagged ✓ (seen in a PubMed URL or an explicit `pmid=` string during research) or ⚠ (needs verification).

---

## 1. Disease Information

### 1.1 Overview

Embryonal tumour with multilayered rosettes (ETMR) is a rare, highly aggressive embryonal neoplasm of the central nervous system, **WHO CNS grade 4**, occurring almost exclusively in infants and children under four years of age. Its defining histological feature is the **multilayered ("ependymoblastic" or "true") rosette** — a pseudostratified ring of primitive neuroepithelium around a round, empty lumen — set against a background that may be densely cellular or rich in neuropil.

The entity's modern definition is a **molecular unification of three previously separate histological diagnoses**:

| Former entity | Dominant morphology |
|---|---|
| Embryonal tumour with abundant neuropil and true rosettes (ETANTR) | Multilayered rosettes in an abundant neuropil‑rich stroma |
| Ependymoblastoma (EBL) | Multilayered rosettes, little neuropil |
| Medulloepithelioma (MEPL) | Papillary/tubular/trabecular neural‑tube‑like epithelium |

Korshunov and colleagues showed in 2010 that a focal 19q13.42 amplification was present in virtually all embryonal brain tumours with ependymoblastic rosettes, and in 2014 that across **97 cases** the three morphologies carried uniform molecular signatures irrespective of histological pattern, recommending they be lumped into one diagnostic category (PMID:20407781 ✓; Acta Neuropathol 2014;128(2):279–289, PMC4102829 ⚠). WHO CNS4 (2016) adopted this as **"Embryonal tumour with multilayered rosettes, C19MC‑altered."**

**WHO CNS5 (2021) changed the name.** Because a C19MC‑non‑amplified subset was shown to carry biallelic *DICER1* mutations, the qualifier "C19MC‑altered" was removed from the entity name. The current type is **"Embryonal tumour with multilayered rosettes"** within *Other CNS embryonal tumours*, with **C19MC‑altered** and **NOS/not‑elsewhere‑classified** designations used according to what testing shows.

### 1.2 Key identifiers

| Resource | Identifier | Confidence |
|---|---|---|
| Mondo | **MONDO:0958119** | Supplied in the request; the label matches MalaCards/MedGen content returned for this ID, but the ID itself was **not** resolved against a MONDO build in this session — verify with `runoak -i sqlite:obo:mondo info MONDO:0958119` |
| ICD‑O‑3 | **9478/3** | High — stated by Orphanet and multiple pathology sources |
| Orphanet | **ORPHA:656417** | High |
| MedGen | **C5575350** (Concept Id 1804732) | High |
| OMIM | **None.** ETMR has no OMIM phenotype entry (it is a somatic neoplasm). The DICER1 arm relates to *OMIM 601200 (DICER1)* / *DICER1 syndrome, OMIM 601200/138800‑series* — verify before binding | Medium |
| ICD‑10‑CM | No specific code; coded under **C71.x** (malignant neoplasm of brain) by site | Medium |
| ICD‑11 | No ETMR‑specific stem code identified; coded under **2A00** (malignant neoplasms of brain) with ICD‑O morphology 9478/3 | **Low — could not confirm; look up directly** |
| MeSH | **No ETMR‑specific descriptor found.** Nearest supplementary concepts relate to "Neuroectodermal Tumors, Primitive" / "Neoplasms, Germ Cell and Embryonal" | Low |
| NCIT | A term for *Embryonal Tumor with Multilayered Rosettes* exists in NCIT, but **the code could not be retrieved or verified** in this session. Do **not** write an NCIT code for this entity from memory | **Unverified — must look up** |

### 1.3 Synonyms and alternative names

- Embryonal tumour with multilayered rosettes, C19MC‑altered (WHO CNS4 name; still widely used)
- ETMR; ETMR, NOS; ETMR, NEC (not elsewhere classified)
- Embryonal tumour with abundant neuropil and true rosettes (ETANTR) — *historical, now a morphological pattern*
- Ependymoblastoma (EBL) — *historical*
- Medulloepithelioma (MEPL) — *historical*
- "ETMR, non‑C19MC‑altered" (Heidelberg classifier v12.5 methylation class) / "ETMR‑DICER" (NIH classifier methylation class)
- CNS‑PNET with ependymoblastic rosettes — *obsolete, pre‑2010*

### 1.4 Provenance of the information

**Aggregated disease‑level resources and primary literature only.** ETMR is too rare for EHR‑derived phenotype profiles: there is no OMOP/COHD/ICEES signal of useful size, and no `kb/phenotype_distributions/` export exists. The authoritative aggregated sources are:

- The **Rare Brain Tumor Registry/Consortium (RBTR/RBTC)** cohort — 159 centrally confirmed cases, the largest clinically annotated series
- The **DKFZ/Heidelberg molecular cohort** — 193 primary + 23 matched relapse tumours (Lambo 2019, PMID:31802000 ✓)
- **P‑HIT/HIT‑2000** prospective German trial data (PMID:33908610 ✓)
- The **DNA methylation classifier** reference cohort (Capper 2018, PMID:29539639 ✓)
- Orphanet ORPHA:656417

---

## 2. Etiology

### 2.1 Primary causal factors

ETMR is a **genetically driven somatic neoplasm of early neural development**. Three mutually exclusive driver lesions are recognised, all affecting microRNA biology:

| Driver | Frequency | Origin | Mechanism class |
|---|---|---|---|
| **C19MC amplification / TTYH1–C19MC fusion** (19q13.42) | **~90%** of ETMRs regardless of histology | Somatic | Oncogenic miRNA cluster gain‑of‑expression |
| **Biallelic *DICER1* mutation** | **~5%**, exclusively in C19MC‑non‑amplified tumours | **Frequently germline** (LOF) + somatic RNase IIIb hotspot | miRNA‑processing loss of function |
| **MIR17HG (miR‑17‑92) amplification** | **~1%** (a handful of reported cases) | Somatic | Second oncogenic miRNA cluster gain |

Lambo et al. (PMID:31802000 ✓) report that in tumours where C19MC was not amplified, patients "frequently had germline mutations in *DICER1* or other microRNA‑related aberrations such as somatic amplification of miR‑17‑92."

A proportion of ETMRs remain **driver‑unassigned** after all three tests — these are the ETMR NOS/NEC cases.

### 2.2 Genetic risk factors

**Causal / defining lesions** — see 2.1 and §4.

**Germline predisposition — the one real hereditary risk factor:**
- ***DICER1* tumour‑predisposition syndrome** (autosomal dominant, incomplete penetrance). The classic architecture is a **truncating germline loss‑of‑function allele plus a somatic missense "hotspot" variant in the RNase IIIb domain** — a non‑canonical two‑hit model, because the second hit does not fully inactivate DICER1 but selectively impairs RNase IIIb cleavage of the 5p miRNA strand. ETMR sits in the DICER1 CNS tumour spectrum alongside **pineoblastoma, pituitary blastoma, and primary intracranial sarcoma**; in systematic review, ETMR, pineoblastoma and pituitary blastoma were the CNS tumours most likely to carry **germline** DICER1 mutations, with frameshift/nonsense predominating, whereas primary intracranial sarcoma more often carried somatic missense variants (PMC10193506 ⚠; J Neurosurg Pediatr 2022;30(3):308).
- A **germline *TP53*** variant (e.g. NM_000546.6(TP53):c.743G>A, p.Arg248Gln) has been submitted to ClinVar in association with ETMR (RCV006253479.1). This is a **single submission and not an established predisposition**; treat as anecdotal, not as a risk factor, unless corroborated.
- No GWAS, no susceptibility loci, no modifier genes have been reported for ETMR. The disease is far too rare for GWAS.

### 2.3 Environmental risk factors

**None identified.** No toxin, radiation, dietary, infectious, parental‑occupation, or socioeconomic exposure has been associated with ETMR in any published series. The tumour's onset in the first two years of life and its origin in a transient fetal progenitor population make a **prenatal/perinatal timing** of the initiating event near‑certain, but no exogenous initiator is known.

Established non‑modifiable associations:
- **Age** — overwhelmingly the first 4 years of life; this is a property of the cell of origin, not an "exposure"
- **Sex** — no consistent predominance (see §9)
- **Family history** — relevant only for the *DICER1* arm

### 2.4 Protective factors

**No genetic or environmental protective factor has been described.** There is no dietary, lifestyle, or pharmacological exposure reported to reduce ETMR risk. gnomAD‑style protective‑allele analysis is not applicable.

### 2.5 Gene–environment interactions

**None documented.** No GxE interaction has been reported for ETMR in CTD, PheGenI, or the primary literature. For the DICER1 arm, the relevant "interaction" is purely internal — germline LOF allele × somatic RNase IIIb second hit — and the timing of the two hits during development, rather than any environmental factor, determines which DICER1 phenotype emerges (F1000Res 2015;4:214 ⚠).

---

## 3. Phenotypes

ETMR's clinical phenotype is almost entirely **mass‑effect and site‑dependent**, not a syndromic constellation. Symptoms are typically present for only weeks before diagnosis, reflecting the tumour's rapid growth.

### 3.1 Presenting symptoms and signs with frequencies

Frequencies below are from the 2026 *Diagnostic Pathology* series of 35 molecularly/histologically confirmed ETMRs (PMID:41664204 ✓), supplemented by the RBTR cohort and review literature.

| Phenotype | Type | Frequency | Onset | Course | HPO candidate (**UNVERIFIED**) |
|---|---|---|---|---|---|
| Headache | Symptom | **88.6%** | Infantile/early childhood | Progressive over weeks | `HP:0002315` |
| Vomiting | Symptom | **65.7%** | Same | Progressive | `HP:0002013` |
| Nausea | Symptom | **54.3%** | Same | Progressive | `HP:0002018` |
| Motor weakness / hemiparesis | Clinical sign | **48.6%** (sided weakness 34% in another cohort) | Same | Progressive | `HP:0001324` (muscle weakness) / `HP:0001269` (hemiparesis) |
| Increased intracranial pressure | Clinical sign | **~53%** explicitly; most patients have some evidence | Same | Progressive | **`HP:0002516`** ✅ *verified label: "Increased intracranial pressure"* |
| Seizures / convulsions | Clinical sign | **22.9%** (23% of children <3 yr with brain tumour generally) | Same | Episodic on a progressive background | `HP:0001250` |
| Hydrocephalus (obstructive) | Clinical sign / imaging | Common; frequency not separately tabulated | Same | Progressive | `HP:0000238` |
| Macrocephaly / bulging fontanelle | Physical manifestation | Common in infants, often **masking** raised ICP | Infantile | Progressive | `HP:0000256` |
| Papilledema | Clinical sign | Frequency not reported for ETMR specifically | — | Progressive | `HP:0001085` |
| Ataxia / gait disturbance | Clinical sign | In infratentorial tumours | — | Progressive | `HP:0001251` |
| Cranial nerve palsy (incl. VI, VII, VIII) | Clinical sign | In brainstem / CPA / internal‑auditory‑canal tumours | — | Progressive | `HP:0001291` (verify) |
| Developmental delay or arrest / loss of milestones | Behavioural / developmental | Described as "a presentation unique to infants and young children" | Infantile | Progressive | `HP:0001263` / `HP:0002376` (regression) |
| Lethargy, irritability, behavioural change, anorexia | Behavioural | Common, non‑specific | — | Progressive | `HP:0001254` / `HP:0000737` |
| Sensorineural hearing loss | Clinical sign | Rare — reported in the adult internal‑auditory‑canal case | Adult (exceptional) | Progressive | `HP:0000407` |
| Stupor / coma | Clinical sign | Terminal or with acute decompensation | — | Acute | `HP:0007185` (verify) |

**Severity: uniformly severe.** There is no mild form. Essentially every patient has a life‑threatening intracranial mass at presentation.

**Progression: rapid and progressive.** The entity is not episodic, relapsing‑remitting, or stable. Untreated, the course is measured in weeks to a few months.

### 3.2 Laboratory and radiological phenotypes

- **CSF cytology positive for malignant cells** in the subset with leptomeningeal dissemination (~20–30% metastatic at diagnosis). LOINC suggestions would need lookup; `LOINC:` codes must be seeded via `just loinc-seed-cache` and must never be typed from memory.
- **No diagnostic serum or CSF biomarker exists.** There is no analyte analogous to AFP/β‑hCG in germ cell tumours. No reference range belongs on this entry.
- **MRI phenotype** (see §10): large well‑demarcated mass, **calcification**, **restricted diffusion**, **little or no peritumoral oedema**, **absent or weak contrast enhancement**, intratumoral veins, low cerebral blood flow on arterial spin labelling.
- **Ki‑67 proliferation index: mean 50.7% ± 21.9%**; **mitoses 31.9 ± 11.3 per 10 HPF** (PMID:41664204 ✓).

### 3.3 Quality‑of‑life impact

**No ETMR‑specific EQ‑5D, SF‑36, PROMIS, or PedsQL data exist.** This is a genuine gap: the disease is rare, the patients are pre‑verbal, and historical survival was too short for QoL instruments to be deployed. What is documented is **unfavourable neurocognitive outcome in survivors** treated with radiation plus high‑dose chemotherapy with tandem autologous stem cell rescue (ScienceDirect, *Superior outcome but high incidence of pseudoprogression and unfavorable neurocognitive outcome…*, 2024 ⚠). Proxy evidence from the wider paediatric neuro‑oncology literature is consistent and directionally strong:

- **Craniospinal irradiation is consistently associated with poorer cognitive outcomes**, while **focal therapy is associated with only minor cognitive change**, and focal proton radiotherapy yields neurocognitive profiles broadly within normative expectations (Springer 2023, systematic review/meta‑analysis ⚠).
- This matters more for ETMR than for most tumours, because the patients are 1–3 years old — the period of maximum vulnerability of the developing brain.

**Per‑phenotype QoL attribution is not available** and should be recorded as a knowledge gap rather than estimated.

---

## 4. Genetic / Molecular Information

### 4.1 The defining lesion: C19MC

**Locus.** Chromosome **19q13.42**, the *chromosome 19 microRNA cluster* — the largest human miRNA gene cluster, **primate‑specific**, containing ~46 miRNA genes spanning roughly 100 kb.

**Normal regulation.** C19MC is **genomically imprinted and paternally expressed**; the maternal allele is silenced by a maternally methylated differentially methylated region (C19MC‑DMR1) acquired in the oocyte (PMID:20610438 ✓). Physiological expression is essentially restricted to **placenta/trophoblast and embryonic stem cells** — in trophoblast and trophoblast‑derived exosomes these miRNAs constitute the majority of all miRNAs. **Expression in postnatal brain is normally absent**, which is what makes ectopic expression in a neural progenitor so consequential.

**The lesion in ETMR.** Focal high‑level amplification, typically as a **structural rearrangement producing a TTYH1–C19MC fusion**. Kleinman et al. performed integrated genetic and epigenetic analysis of 12 ETMRs and identified, **in all 12 cases**, C19MC fusions to *TTYH1* driving expression of the miRNAs (PMID:24316981 ✓, Nat Genet 2014;46(1):39–44). *TTYH1* is expressed in neural stem/progenitor cells; the fusion therefore places a placental/ESC miRNA cluster under a neural‑progenitor promoter.

**Frequency.** ~90% of ETMRs overall; **144/159 (91%)** in the Rare Brain Tumor Registry cohort, with 15/159 (9%) ETMR NOS.

**HGNC/gene annotations (all UNVERIFIED — look up before binding):**
- `TTYH1` — tweety family member 1 (HGNC id must be looked up; **do not write `hgnc:` from memory**)
- `LIN28A` — lin‑28 homolog A
- `DICER1` — dicer 1, ribonuclease III
- `DNMT3B` — DNA methyltransferase 3 beta
- `RBL2` — RB transcriptional corepressor like 2 (p130)
- `MYCN` — MYCN proto‑oncogene
- `MIR17HG` — miR‑17‑92a‑1 cluster host gene
- `IGF2BP1`, `IGF2BP2`, `HMGA2` — let‑7 targets
- The C19MC miRNA genes themselves (`MIR512-1` … `MIR519A2`) — individual HGNC/miRBase identifiers must be looked up

### 4.2 *DICER1* variants

- **Variant classification:** germline alleles are typically **pathogenic truncating** (nonsense, frameshift, splice) and are ClinVar/ClinGen‑classified; the somatic second hit is a **missense "hotspot" in the RNase IIIb domain** affecting the metal‑ion‑binding residues (E1705, D1709, G1809, D1810, E1813 — residue list **must be verified**, not taken from this report).
- **Origin:** germline (frequently) + somatic. In DICER1‑mutant CNS tumours, **nearly 80% of tumours with a germline mutation also carried a second somatic DICER1 mutation**.
- **Functional consequence:** a **non‑canonical two‑hit** mechanism. The germline allele is full loss of function; the somatic RNase IIIb variant is **not** a complete inactivation but a **selective loss of 5p‑strand miRNA processing**, skewing the miRNA pool rather than abolishing it. Critically, this **depletes let‑7 family miRNAs** — converging on the same let‑7 loss that LIN28A produces in C19MC‑amplified tumours.
- **Allele frequency:** germline DICER1 LOF alleles are present in gnomAD at carrier‑level frequencies (~1:10,000 range in some estimates); **look the current figure up rather than citing this one**.
- **LOH is rare** in DICER1 CNS tumours, and is frequently seen only in pineoblastoma.

### 4.3 MIR17HG amplification

~1% of ETMRs. The miR‑17‑92 cluster (chromosome 13) is the first described oncogenic miRNA cluster and, like C19MC, drives proliferation and invasiveness. Reported in both a C19MC‑amplified case and in C19MC‑non‑amplified ETMRs. Its presence is a diagnostic criterion in current practice: "typical radiology, histology, positive LIN28A IHC, and FISH demonstrating **C19MC or MIR17HG amplification**, are sufficient for ETMR diagnosis" (*Neuro-Oncol Adv* 2023;5(1):vdad052 ⚠).

### 4.4 The rest of the genome: structurally unstable, point‑mutationally quiet

- **SNV burden is low and non‑recurrent.** Exome/genome sequencing detected, on average, **1,180 SNVs (range 339–2,544)** and **468 indels (range 299–1,026)** per primary tumour, with low cross‑cohort recurrence. Tumour‑specific mutations fall in **TP53‑, SHH‑, WNT‑ and miRNA‑processing pathway** genes but none at a frequency that defines a subgroup.
- **Copy number:** **chromosome 2 gain in 77.5%** and **focal chr19 alterations centred on C19MC in 80%** are the two most frequent copy‑number events (Lambo 2019, PMID:31802000 ✓). *Chr2 gain is relevant because it spans MYCN.*
- **Structural instability is R‑loop driven.** Lambo et al. showed prevalent genomic instability from **widespread R‑loop structures**, and that **R‑loop‑associated chromosomal instability can be induced by loss of DICER1 function** — tying the two driver arms together mechanistically. ETMRs carry **dense, strongly conserved C>T and C>G mutations around breakpoints**.
- **Primary vs relapse:** "Comparison of primary tumours and matched relapse samples showed a **strong conservation of structural variants, but low conservation of SNVs**," and many newly acquired SNVs carry a **cisplatin‑treatment mutational signature** (PMID:31802000 ✓). *This is therapeutically important: relapse clones are largely the same structurally, and much of the new point‑mutation burden is iatrogenic.*

### 4.5 Modifier genes

**None established.** Chromosome **16q loss** has been reported as a negative prognostic factor in ETMR, but this is a prognostic copy‑number association rather than a validated modifier gene, and **the attribution could not be pinned to a specific publication in this session** — verify before using.

### 4.6 Epigenetics — the heart of the mechanism

ETMR has a **distinct DNA methylation signature** separating it from all other tumours and normal tissues, which is why DNA methylation classification is now central to its diagnosis (Capper 2018, PMID:29539639 ✓).

The mechanism of that signature is the single most important finding in ETMR biology. Kleinman et al. (PMID:24316981 ✓) detected **extreme overexpression of a previously uncharacterised isoform of DNMT3B originating at an alternative promoter that is active only in the first weeks of neural tube development**, and showed that C19MC‑dependent DNMT3B deregulation is **mediated by RBL2**, a known DNMT3B repressor: transfection with individual C19MC miRNAs upregulated DNMT3B and downregulated RBL2. Their conclusion — that this represents "a potential oncogenic re‑engagement of an early developmental program… via epigenetic alteration mediated by an embryonic, brain‑specific DNMT3B isoform" — is the organising idea of the entity.

**Methylation classes currently recognised** (Heidelberg classifier v12.5): *ETMR, C19MC‑altered* and *ETMR, non‑C19MC‑altered*; the NIH classifier labels the latter *ETMR‑DICER*. A posterior‑fossa infant tumour with a **YAP1::MAML2** fusion has been assigned to the non‑C19MC‑altered class — a boundary case worth noting for differential diagnosis (ResearchGate 2025 ⚠).

### 4.7 Chromosomal abnormalities summary

| Event | Frequency | Note |
|---|---|---|
| Focal 19q13.42 amplification / TTYH1–C19MC fusion | ~80–90% | Defining; FISH‑detectable |
| Chromosome 2 gain | 77.5% | Spans MYCN |
| MIR17HG (13q31) amplification | ~1% | Alternative driver |
| Chromosome 16q loss | Minority | Reported adverse prognostic — **verify source** |
| Whole‑genome structural rearrangement burden | High | R‑loop associated |

*Per this project's content fences, no evidence regarding 1p36, 11q or 17q changes, or chromothripsis, is included in this report.*

---

## 5. Environmental Information

- **Environmental factors:** None identified. No entry in CTD links an exposure to ETMR. No radiation, pesticide, solvent, air‑pollution, or parental‑occupation association has been reported.
- **Lifestyle factors:** Not applicable — the patients are infants. No maternal dietary, smoking, or alcohol exposure has been linked to ETMR.
- **Infectious agents:** None. ETMR has no viral or microbial association. Unlike some embryonal tumours elsewhere in the body, no oncovirus has been implicated.

**Curation note:** this is a disease where the honest `environmental:` block is **empty with a `review_notes:` waiver** beginning `Left deliberately uncited.` followed by ≥20 words recording what was searched (CTD, PubMed exposure terms, EPA/WHO sources), rather than a speculative ECTO binding. Do **not** bind an exposure term here.

---

## 6. Mechanism / Pathophysiology

### 6.1 The causal chain, step by step

Each numbered step names what it causes next. Steps marked **[inferred]** are reasoned from the data rather than directly demonstrated in ETMR tissue.

**Main branch — C19MC‑altered ETMR (~90%)**

1. **A focal structural rearrangement amplifies the C19MC locus at 19q13.42 and fuses it to *TTYH1*.** This **places a primate‑specific, normally placenta/ESC‑restricted miRNA cluster under the control of a promoter active in neural stem and progenitor cells**, and thereby **results in** high‑level ectopic expression of the C19MC miRNAs in a cell lineage that normally silences them entirely. *(Demonstrated: C19MC–TTYH1 fusion in 12/12 ETMRs, PMID:24316981 ✓.)*

2. **Ectopic C19MC miRNAs repress *RBL2*.** Loss of RBL2, a transcriptional repressor of *DNMT3B*, **leads to** de‑repression of *DNMT3B*. *(Demonstrated by transfection of individual C19MC miRNAs into cultured cells: DNMT3B up, RBL2 down.)*

3. **De‑repression activates an alternative *DNMT3B* promoter that is normally active only during the first weeks of neural tube development**, which **results in** extreme overexpression of an **embryonic, brain‑specific DNMT3B isoform**, and in turn **produces** the ETMR‑specific genome‑wide DNA methylation landscape that the methylation classifier detects. *This is the step that makes ETMR an epigenetic disease as much as a genetic one.*

4. **In parallel, the fusion creates hijacked super‑enhancers**, and **long‑range MYCN promoter–enhancer DNA interactions** form a second set. Together with an **MYCN core transcriptional network**, these **amplify** a self‑reinforcing **C19MC–LIN28A–MYCN oncogenic circuit** (Sin‑Chan 2019, PMID:31287992 ✓, Cancer Cell 36(1):51–67). Chromosome‑2 gain (77.5% of cases) **contributes to** the MYCN arm of this circuit.

5. **Within that circuit, LIN28A binds the terminal loop of pre‑let‑7 and recruits TUT4**, which **blocks let‑7 maturation** and **results in** depletion of mature let‑7 family miRNAs.

6. **Loss of let‑7 de‑represses its targets** — *HMGA2*, *IGF2BP1*, *IGF2BP2*, *MYCN*, and components of the **IGF/PI3K/mTOR** axis — which **leads to** constitutive mTOR pathway activation and a sustained proliferative, stem‑like state. *(Demonstrated in BT183: LIN28 knockdown increases let‑7 and decreases IGF/PI3K/mTOR components; Neuro Oncol 2014;16(1):62–71, PMC3870842 ⚠.)*

7. **In parallel, Wnt and Shh signalling are co‑activated.** Simultaneous activation of Wnt and Shh in murine neural precursor cells is **sufficient to produce** tumours recapitulating human ETMR histology and molecular features (Nat Med 2017;23(10):1191–1202, doi:10.1038/nm.4402 ⚠). *This is the strongest causal demonstration available for ETMR formation.*

8. **The circuit entraps an early neural lineage network and stalls it.** The cell of origin is an **apical radial glial / ventricular‑zone progenitor**; single‑cell transcriptomics and spatial imaging of 11 ETMRs show **undifferentiated malignant cells mirroring fetal ventricular‑zone apical progenitors** at the apex of the hierarchy, with partial differentiation toward neuronal‑ and glial‑like states (*Nat Cancer* 2025;6:1035–1055, PMC12202505 ⚠). **This produces** the entity's defining morphology: multilayered rosettes are the undifferentiated apical‑progenitor compartment reproducing a neural‑tube‑like architecture, and the neuropil‑rich areas are the partially differentiated compartment. *[Partly inferred — the morphology/hierarchy correspondence is strongly supported but not formally lineage‑traced in human tissue.]*

9. **Receptor–ligand crosstalk between malignant compartments sustains the hierarchy.** Systematic analysis identified **FGFR and Notch signalling** as oncogenic pathways maintaining the malignant hierarchy, and these were successfully targeted in preclinical models and in one patient (*Nat Cancer* 2025 ⚠). A **perivascular niche** supports the stem‑like state and chemoresistance (PMC12198369 ⚠).

10. **The high biosynthetic and transcriptional output of this circuit creates a proteostatic burden.** ETMR tissue and BT183 cells **harbour proteasome regulatory proteins in abundance**, implicating **strong dependency on the proteasome machinery to safeguard proteostasis** (PMID:38158710 ✓). *[Inferred as a consequence of the circuit; demonstrated as a dependency.]*

11. **Rapid clonal expansion produces a bulky intracranial mass**, which **causes** mass effect and obstruction of CSF flow, **leading to** obstructive hydrocephalus, raised intracranial pressure, headache, vomiting, papilledema, macrocephaly in infants, and site‑dependent focal deficits and seizures.

12. **Tumour cells access the CSF compartment**, which **results in** leptomeningeal dissemination (~20–30% metastatic at diagnosis) and, rarely, extracranial spread.

13. **R‑loop‑associated genomic instability** generates the structural‑variant burden; **structural variants are strongly conserved from primary to relapse**, so **relapse is driven by the same structural architecture** while newly acquired SNVs largely carry a **cisplatin signature** — i.e. much of the point‑mutation change at relapse is treatment‑induced rather than clonally selected (PMID:31802000 ✓).

**Alternative branch — DICER1‑mutant ETMR (~5%)**

1b. **A germline truncating *DICER1* allele plus a somatic RNase IIIb hotspot missense variant** **impair 5p‑strand miRNA processing**, which **results in** depletion of mature let‑7 — **converging on step 6 above from a different direction**, without any C19MC event.
2b. **Loss of DICER1 function additionally induces R‑loop‑associated chromosomal instability**, which **leads to** the structural‑variant burden seen in this arm.

**Alternative branch — MIR17HG‑amplified ETMR (~1%)**

1c. **Amplification of the miR‑17‑92 cluster** **substitutes for** C19MC as the oncogenic miRNA source, driving proliferation and invasiveness through an overlapping downstream programme.

### 6.2 Coverage of the template's mechanism categories

- **Molecular pathways:** let‑7/LIN28 axis; IGF/PI3K/**mTOR**; **MYCN** core transcriptional network; **Wnt**; **Shh**; **Notch**; **FGFR**; DNA methylation machinery (DNMT3B); ubiquitin–proteasome system. (KEGG/Reactome identifiers must be looked up.)
- **Cellular processes:** blocked differentiation / stalled developmental program; sustained proliferation; cell‑cycle dysregulation via RBL2/p130 loss; maintenance of a stem‑like state; apoptosis evasion; proteostasis maintenance.
- **Protein dysfunction:** LIN28A **gain of function by overexpression** (not by mutation) — an RNA‑binding protein acting as a let‑7 biogenesis blocker; DICER1 **partial, domain‑selective loss of function**; DNMT3B **gain of function via an aberrant embryonic isoform**; RBL2 **loss of expression**.
- **Metabolic changes:** none specifically characterised in ETMR. mTOR activation implies anabolic reprogramming, but no metabolomic study of ETMR was identified. **Record as a gap.**
- **Immune involvement:** ssGSEA on ETMR tissue showed **enhanced scores for 16 immune cell types**, suggesting a measurable immune infiltrate; 135 DEGs and three core variant genes (**ALB, PSMD1, PAK2**) were identified (PMID:38802706 ✓, *Childs Nerv Syst* 2024;40:2685–2696). **This is a single computational study and should be treated as a lead, not as established immunobiology.** No immunotherapy signal follows from it yet.
- **Tissue damage mechanisms:** compression and infiltration of normal brain; obstructive hydrocephalus; raised ICP; herniation in terminal disease. Not oxidative/ischaemic/fibrotic in the classic sense.
- **Biochemical abnormalities:** no enzyme deficiency, receptor defect, or channelopathy. The biochemical lesion is **miRNA‑processing/abundance**, not catalysis.
- **Transcriptomics:** distinct ETMR expression signature; **alternative splicing dysregulation** reported as an emerging feature (PMC7563716 ⚠); pluripotency/early‑neural programmes enriched. Single‑cell and spatial data: *Nat Cancer* 2025 (11 samples).
- **Proteomics:** integrated proteome + case‑matched methylome, compared against other embryonal and paediatric brain tumours, with the proteasome as the headline dependency (PMID:38158710 ✓).
- **Metabolomics / lipidomics:** **no data.**
- **Functional genomics screens:** no published ETMR CRISPR screen identified; DepMap contains no ETMR line. The functional work is drug‑screen based (see §12).

### 6.3 Ontology suggestions for the mechanism (ALL UNVERIFIED — look up before binding)

**Biological processes (GO) — candidate concepts to search for, not IDs to copy:**
- miRNA‑mediated gene silencing / pre‑miRNA processing / production of miRNAs involved in gene silencing
- negative regulation of miRNA maturation *(for the LIN28A→let‑7 block)*
- DNA methylation / regulation of DNA methylation‑dependent heterochromatin formation
- canonical Wnt signaling pathway
- smoothened signaling pathway *(Shh)*
- Notch signaling pathway
- fibroblast growth factor receptor signaling pathway
- TOR signaling / insulin‑like growth factor receptor signaling pathway
- proteasome‑mediated ubiquitin‑dependent protein catabolic process
- neural tube development / radial glial cell differentiation / neuroblast proliferation
- positive regulation of cell population proliferation

**Cell types (CL):**
- radial glial cell; **apical** radial glial cell (if CL carries it); neural progenitor cell; neuroepithelial cell; neural stem cell; neuroblast; perivascular cell / pericyte *(niche)*

**Anatomy (UBERON):** see §7.

**Chemical entities (CHEBI):** actinomycin D (dactinomycin), topotecan, doxorubicin, carboplatin, etoposide, cisplatin, vincristine, cyclophosphamide, thiotepa, methotrexate, decitabine, panobinostat, volasertib, marizomib, JQ1. **Every one of these requires a CHEBI lookup; several (volasertib, marizomib, JQ1) may have no CHEBI term and belong on NCIT or in `preferred_term` only.**

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

**Primary organ: the brain** (and, rarely, spinal cord). ETMR is confined to the CNS; it is not a systemic disease.

**Site distribution** (figures vary by series and by whether the cohort is molecularly confirmed):

| Site | Frequency | Source |
|---|---|---|
| Supratentorial (cerebral hemispheres) | **~70–74%** (74.3% in the 2026 series of 35) | PMID:41664204 ✓; review literature |
| Infratentorial (cerebellum, brainstem) | **~30%** | Review literature |
| Cerebral, in the molecularly confirmed registry | **55%**, with **45% arising at sites characteristic of other brain tumours** | RBTR, n=159 ⚠ |
| Pineal region | A minority (3/9 in one small series) | ⚠ |
| Brainstem | A distinct, particularly poor‑outcome subset (excluded from the main P‑HIT analysis) | PMID:33908610 ✓ |
| Spinal cord | Rare | Orphanet |
| Internal auditory canal / CPA | **One reported case**, in a 36‑year‑old, DICER1‑mutant | PMID:37920133 ✓ |

The RBTR observation that **45% arise at sites characteristic of other brain tumours** is clinically important: ETMR can masquerade radiologically as medulloblastoma, AT/RT, ependymoma, pineoblastoma, or a brainstem glioma depending on where it sits.

**Secondary involvement:** ventricular system and leptomeninges via CSF dissemination; **extracranial extra‑CNS spread is documented but anecdotal** (case series and systematic review, *Childs Nerv Syst* 2017 ⚠).

**Body system: nervous system** (central).

### 7.2 Tissue and cell level

- **Tissue type:** neuroepithelial / embryonal neural tissue. The multilayered rosette is explicitly described as a **remnant of the undifferentiated neural tube**.
- **Cell populations:** apical radial glia / ventricular‑zone progenitors (origin and apex of the hierarchy); neural progenitor cells; partially differentiated neuronal‑ and glial‑like malignant states; **supporting perivascular cells** sustaining the stem‑like, chemoresistant compartment.
- **Immunophenotype** (see §10.1 for the diagnostic panel): primitive cells **vimentin+, nestin+ (100% of cases), LIN28A+**; neuropil/neurocytic component **synaptophysin+, neurofilament+, NeuN+**; **INI1 (SMARCB1) retained in 100%**.

### 7.3 Subcellular level

GO cellular‑component concepts to search (**unverified**): **nucleus** (DNMT3B, MYCN, RBL2); **cytoplasm / RISC** (LIN28A, DICER1, let‑7 processing); **proteasome complex**; **chromatin / super‑enhancer regions**; **R‑loop–containing nuclear structures** (likely no GO term — record as free text).

### 7.4 Localisation and laterality

- **Unilateral, focal and typically single**, arising within one hemisphere or one posterior‑fossa structure. ETMR is **not** a bilateral or symmetric disease.
- Multifocality at diagnosis reflects **leptomeningeal dissemination**, not multiple primaries.
- **UBERON candidates (UNVERIFIED):** brain; telencephalon; cerebral hemisphere; cerebral cortex; lateral ventricle; cerebellum; brainstem/pons; pineal gland; spinal cord; leptomeninges; internal auditory canal; neural tube / ventricular zone *(developmental structures, for the cell‑of‑origin annotation)*.

---

## 8. Temporal Development

### 8.1 Onset

- **Age of onset: infancy and early childhood.** Median **26 months** in the largest molecularly confirmed registry cohort (n=159); **36 months** in the 2026 *Diagnostic Pathology* series (n=35); **~2.5 years** cited in review; series medians span **24–37 months**. Most cases occur **in the first two years of life**, and the great majority before age 4.
- **Congenital ETMR is reported** (INNV‑24, *Neuro-Oncology* 2024 supplement: "congenital embryonal tumor with multilayered rosettes and treatment in a newborn" ⚠), consistent with a prenatal initiating event.
- **The age ceiling is near‑absolute.** The **only case in a person over 18** reported in the literature is a **36‑year‑old with a DICER1‑mutant ETMR of the internal auditory canal** (PMID:37920133 ✓). Teenage cases are also exceptional and individually reportable (PMID:35496734 ✓).
- **Onset pattern: acute‑on‑subacute.** Symptoms typically evolve over days to a few weeks. In infants the expandable skull can mask raised ICP until decompensation.

### 8.2 Progression

- **Staging:** ETMR uses the **Chang M‑stage** metastatic staging used for medulloblastoma (M0–M4), not an AJCC system. **~73% are non‑metastatic (M0)** at diagnosis in the registry cohort; **20–30% are metastatic**. One series reported metastatic disease in **100% of patients aged >4 years** versus **18%** of younger patients — i.e. **older age at ETMR diagnosis predicts metastatic presentation**, an unusual and clinically useful inversion.
- **Progression rate: rapid.** Historical median overall survival is **~10–12 months** from diagnosis despite maximal‑safe resection, high‑dose chemotherapy with autologous stem cell transplant, and radiotherapy.
- **Course:** monophasic and progressive, with relapse rather than remitting‑relapsing cycles.
- **Relapse timing:** **nearly half of patients treated without radiotherapy relapse within six months of diagnosis.** Relapse is usually local and/or leptomeningeal.
- **Duration:** not self‑limited; fatal within months to a few years in the large majority.

### 8.3 Patterns

- **Spontaneous remission: never reported.**
- **Treatment‑induced remission is achievable** — gross total resection plus intensive chemotherapy and focal radiotherapy produces long‑term survivors, and this group is the entire basis of modern treatment strategy (§12).
- **Post‑treatment maturation is a documented phenomenon**: residual tumour can differentiate toward a more mature phenotype after therapy, with implications for interpreting post‑treatment imaging and for future differentiation‑directed therapy (PMID:36965133 ✓). **Pseudoprogression is frequent** after radiation plus HDCT/tandem ASCR, and must not be mistaken for true progression.
- **The critical intervention window is the first months after diagnosis.** The consistent finding across cohorts is that **early, not deferred, local therapy after gross total resection** determines long‑term survival. Radiotherapy deferral beyond the HDCT/ASCT consolidation window is associated with inferior local control and worse long‑term outcomes (*Childs Nerv Syst* 2026, doi:10.1007/s00381-026-07490-8 ⚠).

---

## 9. Inheritance and Population

### 9.1 Epidemiology

| Measure | Value | Source |
|---|---|---|
| **Incidence** | **1.35 per 1,000,000 children aged 1–4 years** (Europe; derived from the prospective German P‑HIT trial denominator) | Widely cited; verify primary source |
| Context | CNS embryonal tumours collectively ≈ 1 in 700,000 children aged 0–4 | ⚠ |
| **Cumulative reported cases** | **Fewer than 300 by end of 2020** | Review literature ⚠ |
| **Prevalence** | **Not established.** Orphanet records prevalence as "–". Given median survival around a year, **point prevalence is far below incidence × duration intuitions and is effectively negligible** | Orphanet |
| Share of paediatric brain tumours | **<1%** | Review literature |

**Prevalence‑class guidance for KB curation:** `measure_type: ANNUAL_INCIDENCE`, `rate_denominator: POPULATION_PER_YEAR`, `rate_per_100000: 0.135`, population `European children aged 1–4 years`, `prevalence_class: BELOW_1_IN_1000000`. Do **not** pair a qualitative tier (`ULTRA_RARE`) with an incidence measure — per this repository's prevalence rules, qualitative tiers are forbidden with `ANNUAL_INCIDENCE`.

### 9.2 Inheritance

- **The disease itself is not inherited.** ETMR is a somatic neoplasm; C19MC amplification is acquired.
- **The DICER1 arm carries autosomal dominant predisposition** with **incomplete penetrance** and **highly variable expressivity** (the same germline allele produces pleuropulmonary blastoma in one carrier, cystic nephroma in another, a CNS tumour in a third, and nothing in many). HPO inheritance term to look up: *Autosomal dominant inheritance* — **and note that the ETMR entry itself should record `variant_origin: SOMATIC` on the C19MC/driver node**, because that is what makes the derived cell‑of‑origin computation work in this schema.
- **Genetic anticipation:** not applicable (no repeat expansion).
- **Germline mosaicism:** reported in DICER1 syndrome generally (mosaic RNase IIIb variants produce severe multi‑organ phenotypes) — **verify before stating for ETMR specifically.**
- **Founder effects:** none reported.
- **Consanguinity:** no reported role.
- **Carrier frequency:** applies only to germline DICER1 — look up the current gnomAD figure rather than citing one from memory.

### 9.3 Population demographics

- **Ethnic/geographic predilection: none established.** Cases are reported from Europe, North America, China, India, the Middle East, and elsewhere, with no population enrichment identified. Apparent regional differences in published series reflect referral and molecular‑testing availability, not biology.
- **Sex ratio: no consistent predominance.** The 2026 series of 35 was **17 female : 18 male** (≈1:1). Small series scatter either way (one 9‑patient series was 2 male : 7 female) — **small‑number noise, not a signal.** Record as approximately equal.
- **Age distribution:** sharply peaked in the first 4 years; median ~26 months; congenital cases exist; cases above age 10 are individually reportable; **one case above age 18 in the entire literature.**

---

## 10. Diagnostics

### 10.1 Histopathology and immunohistochemistry — the diagnostic core

**Microscopic findings:**
- **Multilayered ("true"/ependymoblastic) rosettes**: pseudostratified neuroepithelium around a central round, empty lumen — the defining feature, and a remnant of undifferentiated neural tube architecture.
- Three morphological patterns, in the 2026 series of 35: **ETANTR 37.1%, medulloepithelioma 34.3%, ependymoblastoma 28.6%** — i.e. all three are common, and none predicts molecular status.
- Small round blue cell morphology; **high mitotic rate (mean 31.9/10 HPF)**; **Ki‑67 mean 50.7%**.
- Neuropil‑rich areas with neurocytes and occasional ganglion cells in the ETANTR pattern.

**Immunohistochemistry panel:**

| Marker | Result | Interpretation |
|---|---|---|
| **LIN28A** | **Strong, diffuse positive** | The key diagnostic marker. Korshunov et al. found strong LIN28A in **37/37 ETMRs** across a tested cohort of **816 paraffin‑embedded brain tumours**, with focal reactivity in only **6/50 AT/RTs** and all other paediatric brain tumours negative (PMID:23161096 ✓). |
| **Nestin** | **Positive, 100% of cases** | Neural progenitor phenotype |
| **Vimentin** | Strong positive in embryonal cells | |
| **Synaptophysin / neurofilament / NeuN** | Positive in neuropil, neurocytes, ganglion cells | Marks the differentiated compartment |
| **INI1 (SMARCB1)** | **Retained, 100% of cases** | **Critical for excluding AT/RT**, where INI1 is lost |
| **OLIG2** | Variable; used alongside LIN28A in some classification schemes (PMID:33236184 ✓) | |

**⚠ LIN28A is sensitive but not perfectly specific.** It is also positive in a subset of **AT/RT** and in **germ cell tumours**. A LIN28A‑positive tumour with **lost INI1** is AT/RT, not ETMR. LIN28A IHC must be read together with INI1 and with molecular confirmation (*Childs Nerv Syst* 2017, doi:10.1007/s00381-017-3551-6 ⚠).

### 10.2 Molecular diagnostics — required

**Current diagnostic standard:** "typical radiology, histology, positive LIN28A IHC, and **FISH demonstrating C19MC or MIR17HG amplification**, are sufficient for ETMR diagnosis" (*Neuro-Oncol Adv* 2023;5(1):vdad052 ⚠).

| Test | Role | Utility in ETMR |
|---|---|---|
| **FISH for 19q13.42 (C19MC)** | **First‑line confirmatory** | Described as "a very promising diagnostic tool" since 2010 (PMID:20407781 ✓). Widely available, works on FFPE, fast. |
| **DNA methylation profiling (EPIC array + classifier)** | **Reference standard** | Assigns to *ETMR, C19MC‑altered* or *ETMR, non‑C19MC‑altered* (Heidelberg v12.5) / *ETMR‑DICER* (NIH). Also yields a copy‑number profile in the same assay, so it reports C19MC amplification and chr2 gain simultaneously. Capper 2018 (PMID:29539639 ✓). |
| ***DICER1* sequencing — tumour and germline** | **Mandatory when C19MC is not amplified** | Finds the ~5% DICER1 arm. A DICER1‑mutant ETMR is an **indication for germline testing and genetic counselling of the family** (see §13). |
| **MIR17HG FISH / copy number** | Third‑line | The ~1% arm |
| **Chromosomal microarray (CMA)** | Useful | Detects C19MC amplification, chr2 gain, and other structural change |
| **WES/WGS** | Research / selected cases | Low SNV yield; the diagnostic information is in structural variants and methylation, not point mutations |
| **RNA sequencing** | Research / fusion detection | Detects the TTYH1–C19MC fusion directly |
| **Karyotyping** | **Low yield** | The lesion is focal and submicroscopic on standard karyotype |
| **Mitochondrial DNA testing / repeat expansion testing** | **Not applicable** | |
| **Gene panels** | Paediatric brain tumour panels including *DICER1*, *TP53*, *SMARCB1*, *SMARCA4* | |
| **Liquid biopsy (CSF ctDNA)** | **Experimental; no validated ETMR assay** | A plausible future route given the strong structural‑variant signature, but no published validation |

### 10.3 Imaging

- **MRI is the primary imaging modality**; CT adds calcification detection.
- **Characteristic pattern:** a **large** mass, **frequent calcification**, **little‑to‑no peritumoral oedema**, **distinct margins**, **absent or weak contrast enhancement**, **intratumoral veins**, **restricted diffusion** (low ADC, reflecting high cellularity), and **low cerebral blood flow on arterial spin labelling**.
- Supratentorial tumours commonly present as **large cystic‑and‑solid masses with significant mass effect and only mild peritumoral oedema**, with heterogeneous mild enhancement of the solid component (PMID:36649993 ✓).
- **The combination of a huge tumour with minimal oedema and weak enhancement is the discriminating feature** — most other paediatric high‑grade tumours of this size enhance avidly and oedematise.
- **Craniospinal MRI and CSF cytology are mandatory for staging** (Chang M‑stage).

### 10.4 Other tests

- **Laboratory tests:** no diagnostic blood or CSF analyte. Routine pre‑treatment labs only.
- **Functional tests / electrophysiology:** **not diagnostic.** EEG may be performed for seizures; audiometry/BAER where a CPA or internal‑auditory‑canal lesion is suspected or after platinum chemotherapy. Note: audiometry here is a **toxicity‑monitoring** test, not a diagnostic one.
- **Biopsy:** tissue is required. Needle biopsy risks sampling only one morphological pattern; **the three morphologies can coexist in one tumour**, which is precisely why histology alone was unreliable before 2010.

### 10.5 Clinical criteria and differential diagnosis

**WHO CNS5 diagnostic criteria (essential):** an embryonal CNS tumour with appropriate histology **and** either C19MC amplification/fusion **or** biallelic DICER1 mutation (or a matching DNA methylation profile).

**Differential diagnosis:**

| Entity | How to distinguish |
|---|---|
| **Atypical teratoid/rhabdoid tumour (AT/RT)** | **INI1/SMARCB1 lost** (retained in ETMR); may be LIN28A focal‑positive — INI1 is the discriminator |
| **Medulloblastoma** | Site (cerebellar), methylation class, no C19MC, LIN28A negative |
| **CNS neuroblastoma, FOXR2‑activated** | Methylation class; FOXR2 activation |
| **CNS tumour with BCOR internal tandem duplication** | BCOR ITD; methylation class |
| **Ependymoma** | True ependymal rosettes/perivascular pseudorosettes without the pseudostratified multilayered pattern; GFAP/EMA profile |
| **Pineoblastoma** | Site; may also be DICER1‑associated — methylation classification resolves |
| **Germ cell tumour** | **LIN28A can be positive**; markers (OCT4, SALL4, PLAP, AFP/β‑hCG) and site resolve |
| **CNS embryonal tumour NEC/NOS, incl. ZNF532::NUTM1 and YAP1::MAML2 cases** | Methylation classification + fusion testing |

### 10.6 Screening

- **No population screening exists or is justified** — the incidence is ~1.35 per million children 1–4, far below any screening threshold.
- **No newborn screening.** No carrier screening for the general population.
- **Cascade screening applies only to the DICER1 arm.** A DICER1‑mutant ETMR triggers germline testing of the proband and, if positive, cascade testing and **DICER1 surveillance protocols** for relatives (chest imaging for PPB, abdominal/pelvic ultrasound, thyroid surveillance, etc. — see GeneReviews *DICER1‑Related Tumor Predisposition*, NBK196157, and PMC11649450 ⚠). **Note that routine DICER1 surveillance protocols generally do not include brain MRI**, because CNS tumours in DICER1 syndrome present symptomatically and no screening benefit has been demonstrated — verify the current ACMG/International DICER1 consortium recommendation before stating this in the KB.

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

| Metric | Value | Cohort / source |
|---|---|---|
| **Historical median OS** | **~10–12 months** | Review literature |
| Median OS, systematic review of 204 cases | **<1 year**; 44.1% survived >1 year | ⚠ |
| **2‑year OS** | **29%** | RBTR, n=159, molecularly confirmed ⚠ |
| **4‑year OS** | **27%** | Contemporary report ⚠ |
| **5‑year OS, overall** | **<30%** | *Neuro-Oncol Adv* 2023 ⚠ |
| **5‑year OS with CARBO/ETO + tandem HDCT** (non‑brainstem, n=17) | **47%** (5‑yr PFS **35%**) | **P‑HIT, PMID:33908610 ✓** |
| **5‑year OS with other chemotherapy** (non‑brainstem, n=13) | **8%** (5‑yr PFS **0%**) | **P‑HIT, PMID:33908610 ✓** |
| **2‑year EFS after GTR + HDCT + RT** | **66%** | RBTR ⚠ |
| **2‑year EFS after GTR + HDCT, no RT** | **21%** | RBTR ⚠ |
| **2‑year EFS, conventional chemo without RT** | **0%** | RBTR ⚠ |
| **4‑year local control / OS / EFS with focal proton RT** | **81% / 59.6% / 54.2%** (median f/u 55 months) | PPCR registry ⚠ (preprint/registry — verify before citing) |
| **Mortality** | Disease‑specific; ETMR is the cause of death in essentially all fatalities | |

**Read the spread carefully.** The 8% vs 47% and 0% vs 66% contrasts are **not randomised comparisons** — they are treatment‑cohort comparisons within prospective trials and registries, and selection (who was fit for HDCT, who was eligible for radiation) confounds them. The direction is consistent across every cohort, which is why the field has moved, but the magnitude is almost certainly overstated by selection.

### 11.2 Morbidity and function

- **Survivors carry substantial morbidity.** Neurocognitive outcome after radiation plus HDCT with tandem autologous stem cell rescue is **unfavourable**, and this is the central trade‑off of the intensification strategy: the therapy that produces survivors also damages the brain of a 2‑year‑old.
- **Craniospinal irradiation is consistently worse for cognition than focal therapy**; focal proton radiotherapy preserves neurocognitive profiles close to normative expectations.
- Expected late effects (extrapolated from the paediatric neuro‑oncology literature, not ETMR‑specific): intellectual disability, endocrinopathy, ototoxicity (platinum), growth impairment, infertility (alkylators), second malignancy, and for DICER1 carriers a lifelong additional tumour risk.
- **No ETMR‑specific disability or QoL instrument data exist.**

### 11.3 Complications

Hydrocephalus requiring diversion; post‑operative neurological deficit; leptomeningeal and rarely extracranial dissemination; chemotherapy toxicity (myelosuppression, infection, platinum ototoxicity and nephrotoxicity); HDCT/ASCT transplant‑related morbidity and mortality; **pseudoprogression** (frequent after RT + HDCT/tandem ASCR, and a real risk of misdirected treatment change); radiation necrosis; late endocrine and neurocognitive sequelae.

### 11.4 Prognostic factors

**Favourable:**
- **Gross total resection** — the single most consistent modifiable factor
- **Non‑metastatic (M0) disease at diagnosis**
- **Receipt of multimodal therapy including high‑dose chemotherapy and radiation**
- **Early rather than deferred radiotherapy** after GTR
- Non‑brainstem location

**Unfavourable:**
- Metastatic disease at diagnosis
- **Brainstem location** (a distinct, particularly poor subset)
- Subtotal resection or biopsy only
- Omission of upfront radiotherapy
- **Chromosome 16q loss** — reported, **source not verified in this session**
- Age <3 years at diagnosis — reported, but confounded with eligibility for radiotherapy; treat with care

**Prognostic biomarkers:** **none validated.** C19MC status is diagnostic, not prognostic — C19MC‑altered and NOS cases have not been shown to differ in outcome in a way that changes management.

---

## 12. Treatment

**Framing statement:** there is **no standard of care established by randomised trial**. Every regimen below rests on single‑arm trials, registry comparisons, and institutional series. The field's current consensus, and the premise of the open international trial, is **maximal safe resection + intensive chemotherapy + early focal radiotherapy where the child's age and tumour site permit it.**

### 12.1 Surgery

- **Maximal safe resection, aiming for gross total resection**, is the foundation. GTR was achieved in **43%** of the 2026 series of 35 — a realistic benchmark, and a reminder that more than half of children do not get one.
- CSF diversion (external ventricular drain, ventriculoperitoneal shunt, or endoscopic third ventriculostomy) for obstructive hydrocephalus.
- Second‑look surgery after induction chemotherapy is used in some protocols.
- **NCIT candidates (UNVERIFIED):** `NCIT:C15329` Surgical Procedure; `NCIT:C154430` / resection terms — **all require lookup**. `therapeutic_modality: SURGERY`.

### 12.2 Conventional and high‑dose chemotherapy

**The best‑evidenced backbone — P‑HIT CARBO/ETO + tandem HDCT:**
Age‑stratified **carboplatin/etoposide induction followed by tandem high‑dose chemotherapy** with response‑stratified radiotherapy. For 30 patients with non‑brainstem tumours, **5‑year PFS 35% and OS 47%** with CARBO/ETO + HDCT (n=17) versus **0% and 8%** with other treatments (n=13) (PMID:33908610 ✓). The investigators' conclusion was that the data indicate improved survival with intensified chemotherapy.

**The modified IRS‑III backbone (Dana‑Farber):**
Incorporates **doxorubicin and actinomycin D** — both preclinically active against ETMR (see 12.4) — into a rhabdomyosarcoma‑derived regimen. In a case series of **5 children, all with gross total resection**, receiving 12–51 weeks of therapy, with 4 receiving focal radiotherapy and 1 receiving HDCT with autologous stem cell rescue, outcomes were "far better than would be expected based on the historical survival for this tumor" (*Neurooncol Adv* 2020, PMC7648589 ⚠). **n=5 with universal GTR — this is hypothesis‑generating, not evidence of superiority.** An international consensus protocol based on IRS‑III was developed from it.

**Other agents in common use:** vincristine, cyclophosphamide, cisplatin, methotrexate (including **intraventricular methotrexate** in HIT‑style infant protocols), thiotepa (HDCT conditioning), temozolomide.

**Maintenance therapy** is under active investigation (PMID:40193690 ✓, *Exploring Maintenance Therapy in Pediatric ETMR*).

**NCIT candidates (UNVERIFIED):** `NCIT:C15632` Chemotherapy; `NCIT:C15986` Pharmacotherapy; `NCIT:C15431` hematopoietic cell transplantation (→ `therapeutic_modality: CELL_THERAPY`). **CHEBI terms needed for each agent.** For the combination regimens, note that **no NCIT `regimen_term` is likely to exist for "CARBO/ETO + tandem HDCT" or "modified IRS‑III"** — do not invent one; leave `regimen_term` absent and carry the name in `name`/`description`.

### 12.3 Radiotherapy

**The most consequential and most contested treatment decision in ETMR.**

- **Focal radiotherapy to the tumour bed** is the standard approach for localised disease, with **craniospinal irradiation** reserved for metastatic disease.
- **Focal proton therapy** is theoretically and empirically attractive: it consolidates local control while minimising scatter to the developing brain, and the PPCR registry reported **4‑year local control 81%, OS 59.6%, EFS 54.2%**, concluding that continued incorporation of focal RT in ETMR protocols is warranted ⚠.
- **Timing matters more than modality.** Radiotherapy deferral beyond the HDCT/ASCT consolidation window is associated with inferior local control and worse long‑term outcomes; early focal RT following GTR is associated with long‑term survival (>36 months) (PMC7773839 ⚠; *Childs Nerv Syst* 2026 narrative review ⚠).
- **The counter‑pressure is real:** these are 1–3‑year‑olds, and radiation to the developing brain carries severe neurocognitive cost. Infant protocols were historically designed to *avoid or delay* radiation. ETMR is the entity where that principle appears to fail.
- **Stereotactic radiosurgery** shows promise as a salvage strategy for localised recurrence (*Childs Nerv Syst* 2026, doi:10.1007/s00381-026-07447-x ⚠).
- **Interstitial brachytherapy** has been reported with promising results in a brainstem ETMR (PMID:38496916 ✓).
- **NCIT candidate (UNVERIFIED):** `NCIT:C15313` Radiation Therapy; `therapeutic_modality: RADIOTHERAPY`.

### 12.4 Preclinical and targeted candidates

**None is standard of care. All are preclinical or early‑phase.**

| Target / agent | Evidence | Status |
|---|---|---|
| **Topotecan, actinomycin D, volasertib (PLK1 inhibitor)** | BT183 cells were sensitive to topoisomerase inhibitors (topotecan, doxorubicin), epigenetic agents (decitabine, panobinostat), actinomycin D, and volasertib. **In xenograft mice, monotherapy with topotecan, volasertib, and actinomycin D produced a temporary tumour‑growth response and a significant survival increase** (PMID:28482026 ✓) | Preclinical; actinomycin D and doxorubicin adopted clinically via IRS‑III |
| **Bromodomain inhibition (JQ1)** | The C19MC‑LIN28A‑MYCN super‑enhancer circuit "is potently abrogated by bromodomain inhibitor JQ1, leading to ETMR cell death" (PMID:31287992 ✓) | Preclinical. JQ1 is a tool compound, not a drug; clinical BET inhibitors would be the translational route |
| **Proteasome inhibition (marizomib)** | ETMR and BT183 harbour proteasome regulatory proteins in abundance; BT183 is "highly vulnerable toward treatment with the **CNS‑penetrant** proteasome inhibitor marizomib" (PMID:38158710 ✓) | Preclinical. Marizomib's CNS penetration makes it the most translationally credible of this list |
| **FGFR and Notch inhibition** | Receptor–ligand analysis of 11 ETMRs identified FGFR and Notch as oncogenic pathways "successfully targeted in preclinical models **and in one patient with ETMR**" (*Nat Cancer* 2025 ⚠) | Preclinical + **n=1 clinical**. The single patient is the most recent and most interesting signal in the field |
| **Shh pathway inhibition** | The Wnt+Shh mouse model "uncovers the therapeutic potential of Sonic‑hedgehog inhibitors" (Nat Med 2017, doi:10.1038/nm.4402 ⚠) | Preclinical. Note Shh inhibitors cause growth‑plate fusion in young children — a serious barrier in this age group |
| **mTOR / IGF‑PI3K inhibition** | LIN28 knockdown increases let‑7 and decreases IGF/PI3K/mTOR components; "inhibitors of the IGF/PI3K/mTOR pathway may be promising novel therapies" (PMC3870842 ⚠) | Preclinical |
| **Direct LIN28A inhibition** | Proposed by analogy with neuroblastoma work | Conceptual |
| **Immunotherapy** | ssGSEA suggests an immune infiltrate (PMID:38802706 ✓) | **No clinical rationale yet.** Do not overstate |

### 12.5 Clinical trials

**PNOC031 (NCT06861244)** — *Embryonal Tumor With Multilayered Rosettes*, the **first international prospective trial addressing the radiotherapy‑timing question directly.**

- Prospective, **non‑randomised**, target ~70 participants
- Eligibility: molecularly or histologically confirmed ETMR; **no prior radiation**; **participants of any age**; ≥10–20 unstained FFPE slides or one block with ≥40% tumour content
- **Three cohorts:**
  - **Cohort 1** — GTR + RT‑eligible → **early focal radiotherapy**
  - **Cohort 2** — GTR + not RT‑eligible → **high‑dose chemotherapy with autologous stem cell rescue**
  - **Cohort 3** — less than GTR, or metastatic → RT or HDCT per RT eligibility, based on age and tumour location

Also relevant: **NCT01247597** — *DICER1‑related Pleuropulmonary Blastoma Cancer Predisposition Syndrome: A Natural History Study* (NCI), which enrols DICER1 carriers including those with CNS tumours.

**ICTRP note:** no non‑ClinicalTrials.gov registry entries for ETMR were identified in this session; if one is found, cite it as `ICTRP:<id>` per the repository's convention rather than burying the identifier in prose.

### 12.6 Supportive and rehabilitative care

Corticosteroids for peritumoral oedema and raised ICP; antiepileptics; CSF diversion; antiemetics; nutritional support; hearing surveillance and amplification after platinum; physical, occupational, and speech therapy; neuropsychological assessment and educational support; palliative and end‑of‑life care, which — given the survival figures — is a core rather than peripheral component of ETMR care.

**NCIT candidates (UNVERIFIED):** `NCIT:C15747` Supportive Care; `NCIT:C15302` Physical Therapy; `NCIT:C15315` Rehabilitation; `NCIT:C15240` Genetic Counseling. **`therapeutic_modality: BEHAVIORAL`** for the therapy interventions.

### 12.7 Treatment algorithm (as practised)

1. Presentation with raised ICP → imaging → **CSF diversion if needed**
2. **Maximal safe resection**, aiming for GTR
3. **Histology + LIN28A IHC + INI1 → FISH for C19MC (and MIR17HG) → methylation profiling; if C19MC‑negative, *DICER1* sequencing (tumour and germline)**
4. **Staging:** craniospinal MRI + CSF cytology
5. **Intensive chemotherapy** — CARBO/ETO + tandem HDCT, or a modified IRS‑III backbone, per protocol/trial
6. **Early focal radiotherapy** where age and site permit; craniospinal irradiation for metastatic disease; proton therapy preferred where available
7. **Genetic counselling** for all DICER1‑mutant cases
8. **Relapse:** consider stereotactic radiosurgery for localised recurrence; otherwise trial enrolment or palliation

### 12.8 Pharmacogenomics

**No ETMR‑specific pharmacogenomic guidance.** General paediatric oncology PGx applies — most importantly **CPIC guidance on *TPMT*/*NUDT15* for thiopurines** (not part of ETMR regimens) and **emerging *TPMT*/*COMT*/*ACYP2* associations with cisplatin ototoxicity**, which is directly relevant given platinum use in infants. Verify current CPIC status before stating.

---

## 13. Prevention

### 13.1 Primary prevention

**None exists and none is plausible.** The initiating event is a somatic structural rearrangement in a transient fetal neural progenitor population, with no known environmental contributor. There is nothing to modify.

**Exception — the DICER1 arm.** For families with a known germline *DICER1* pathogenic variant, **reproductive options exist**: preimplantation genetic testing (PGT‑M) and prenatal diagnosis are technically available. These are **family‑planning choices made with genetic counselling, not public‑health prevention**, and the counselling must convey that penetrance is incomplete and that most DICER1 carriers never develop ETMR specifically.

### 13.2 Secondary prevention (early detection)

- **No population screening is justified** at an incidence of ~1.35 per million children aged 1–4.
- **No newborn screening.** ETMR has no screenable analyte.
- **The one actionable "early detection" lever is clinical awareness**: recognising that a large, calcified, minimally enhancing, minimally oedematous hemispheric mass in a toddler is likely ETMR, and obtaining LIN28A IHC plus C19MC FISH early. **Earlier molecular diagnosis enabling earlier aggressive multimodal therapy is the explicit conclusion of the largest international study** (SickKids/RBTR, 2021 ⚠).
- **DICER1 surveillance protocols** exist for germline carriers and should be instituted after a DICER1‑mutant ETMR — but note the caveat in §10.6 that these protocols focus on thoracic, renal, gynaecological and thyroid sites, and **brain MRI is generally not part of them**.

### 13.3 Tertiary prevention

Preventing complications in children who have ETMR:
- **Early rather than deferred radiotherapy** to prevent local relapse — the strongest tertiary‑prevention signal in the disease
- CSF diversion to prevent herniation
- Platinum ototoxicity monitoring and dose modification
- Infection prophylaxis during HDCT/ASCT
- Neurocognitive surveillance and early educational intervention
- Long‑term survivorship follow‑up for endocrine, cognitive, and second‑malignancy risk

### 13.4 Immunisation, behavioural interventions, public health, prophylaxis

- **Immunisation:** not applicable to ETMR prevention. Standard childhood immunisation and post‑transplant revaccination schedules apply as supportive care.
- **Behavioural / lifestyle interventions:** **none applicable.**
- **Public health / environmental interventions:** **none applicable** — no environmental risk factor to target.
- **Prophylaxis:** antimicrobial and antifungal prophylaxis during HDCT/ASCT; anticonvulsant prophylaxis is site‑ and practice‑dependent.

### 13.5 Genetic counselling

**Indicated for every C19MC‑non‑amplified ETMR**, and specifically for every DICER1‑mutant case. Content: autosomal dominant transmission, incomplete penetrance, variable expressivity across the DICER1 tumour spectrum (PPB, cystic nephroma, Sertoli–Leydig cell tumour, thyroid nodules/differentiated thyroid carcinoma, pineoblastoma, pituitary blastoma, intracranial sarcoma), cascade testing of at‑risk relatives, and enrolment in surveillance. **Counselling is not indicated for C19MC‑amplified ETMR**, which is a sporadic somatic event with no recurrence risk — and saying so explicitly is itself a useful counselling outcome.

---

## 14. Other Species / Natural Disease

**This section is genuinely sparse, and the sparseness is informative.** C19MC is a **primate‑specific** miRNA cluster. **No non‑primate species has a C19MC orthologue**, so the defining lesion of ETMR **cannot occur naturally in mice, rats, dogs, or cats.** Any ETMR‑like tumour in a non‑primate animal is therefore a **morphological phenocopy**, not the same disease.

### 14.1 Taxonomy and natural disease

| Species | NCBI Taxon (**UNVERIFIED**) | Natural disease |
|---|---|---|
| *Homo sapiens* | `NCBITaxon:9606` | The disease |
| *Felis catus* (domestic cat) | `NCBITaxon:9685` | **One documented ETANTR‑phenocopy.** An **8‑month‑old Maine Coon** presented with recurrent behavioural change and anorexia, progressed over 5 days to stupor and coma, and was euthanised. Necropsy showed an **infratentorial (non‑cerebellar) embryonal tumour with numerous multilayered true rosettes in both highly cellular and neuropil‑like areas**, histologically and immunohistochemically consistent with ETANTR (**PMID:36090160 ✓**, *Front Vet Sci* 2022). A presumptive **spinal** embryonal tumour in a cat has also been reported (PMC12492636 ⚠). **Neither case had C19MC testing** — and could not, meaningfully. |
| *Mus musculus* | `NCBITaxon:10090` | **No natural disease.** Engineered models only (§15) |

**Breed:** the single feline case was a **Maine Coon**; with n=1 this is **not a breed association**. A VBO identifier would be `VBO:` for Maine Coon — **look it up; do not assert a breed predisposition.**

### 14.2 Orthologous genes

**Verify every one of these in NCBI Gene / Alliance before binding; per repository convention, a mouse gene takes `MGI:`, rat `RGD:`, zebrafish `ZFIN:`, and a non‑MOD species takes `NCBIGene:`.**

| Human gene | Mouse orthologue | Notes |
|---|---|---|
| *LIN28A* | *Lin28a* (`MGI:` — look up) | Conserved; used in the transgenic models |
| *DICER1* | *Dicer1* (`MGI:` — look up) | Conserved; essential |
| *DNMT3B* | *Dnmt3b* (`MGI:` — look up) | Conserved, but **the ETMR‑specific alternative embryonic promoter/isoform is the human‑relevant feature** — conservation of the gene does not imply conservation of the mechanism |
| *TTYH1* | *Ttyh1* (`MGI:` — look up) | Conserved |
| *MYCN* | *Mycn* (`MGI:` — look up) | Conserved |
| *RBL2* | *Rbl2* (`MGI:` — look up) | Conserved |
| **C19MC cluster** | **No orthologue** | **Primate‑specific — this is the key comparative fact** |
| *MIR17HG* | *Mir17hg* (`MGI:` — look up) | Conserved |

### 14.3 Comparative biology and evolutionary conservation

- **The downstream circuitry is deeply conserved** (LIN28/let‑7, mTOR, Wnt, Shh, Notch, DNMT3B) — which is why mouse models can reproduce ETMR histology at all.
- **The upstream driver is not conserved** — C19MC is primate‑specific and placenta‑restricted, arising late in primate evolution in association with placental biology.
- **Interpretive consequence for curation:** any mouse model of ETMR is by construction a **model of the downstream circuit, not of the initiating lesion.** When recording `modeled_mechanisms` for a mouse model, the honest `fidelity` is **MODERATE at best**, and a `divergences` entry of type **`SPECIES_MISMATCH`** with `materiality: QUALIFYING` is warranted, with a `description` stating specifically that the species carries no C19MC locus.

### 14.4 Transmission

**Not applicable.** ETMR is a neoplasm with **no zoonotic potential and no cross‑species transmissibility.**

---

## 15. Model Organisms

### 15.1 The flagship cell line: BT183

- **BT183** is **the first and principal ETMR cell line**, derived from a **2‑year‑old ETMR patient**.
- It **maintains C19MC amplification, expresses C19MC‑encoded miRNAs, and is tumour‑initiating**; it "recapitulates the molecular and morphologic features of the parent tumor and represents an important first model for ETMR and related C19MC‑amplified or Lin28‑overexpressing embryonal brain tumors" (*Neuro Oncol* 2014;16(1):62–71, PMC3870842 ⚠).
- It shows **high LIN28 expression, low let‑7, and mTOR pathway activation.**
- **Orthotopic xenograft:** BT183 transplanted intracranially into **immune‑deficient NSG mice forms tumours within 2–3 months that recapitulate ETMR biology.**
- **BT183 is the substrate for essentially all ETMR drug discovery to date** — the 2017 drug screen (PMID:28482026 ✓) and the 2024 proteasome/marizomib work (PMID:38158710 ✓) both rest on it.
- **Its limitation is also its importance: it is nearly the only line.** A field whose functional data come overwhelmingly from one patient's cells has a real generalisability problem, and this should be stated explicitly in any `experimental_models` block. A reported **BT187** line could **not** be confirmed in this session — do not record it without a source. Check **Cellosaurus** for the current ETMR line inventory before curating this section.

### 15.2 Genetically engineered mouse models

| Model | Result | Interpretation |
|---|---|---|
| **hGFAP‑cre::lsl‑Lin28A (GL) mice** — constitutive LIN28A overexpression in neural precursors | **Transient increase in proliferation in the cortical ventricular zone at embryonic stages, but NO postnatal brain tumour formation**; reduced dendritic spine density (**PMID:34801069 ✓**) | **A decisive negative result.** LIN28A overexpression alone is **not sufficient** to drive ETMR in vivo. This is exactly the kind of finding that should be curated as a `FAILS_TO_RECAPITULATE` model link with mandatory `limitations` and `evidence`, per this repository's schema. |
| **Wnt + Shh co‑activation in murine neural precursor cells** | **Produces tumours recapitulating the histological and molecular features of human ETMR**; "ETMRs are characterized by a parallel activation of Shh and Wnt signaling" (Nat Med 2017;23(10):1191–1202, doi:10.1038/nm.4402 ⚠) | **The only genetically engineered model that forms ETMR‑like tumours.** It uncovered the therapeutic potential of Shh inhibitors. Fidelity caveat: it reproduces the *phenotype* without the *driver* — no C19MC locus exists in mouse. |
| **Wnt + Shh co‑activation in murine retinal precursors** | Ocular lesions with features of **intraocular medulloepithelioma** (PMC8595639 ⚠) | A lineage‑specific companion model; supports the generality of the Wnt+Shh mechanism across neuroepithelial compartments |
| **Orthotopic radial glial cell transplantation** | Microenvironmentally driven malignant transformation producing PNET‑like tumours (PMC4380339 ⚠) | Supports the radial‑glia cell‑of‑origin hypothesis |

### 15.3 Other model systems

- **Forebrain organoids:** "In vivo intratumoral heterogeneity in a dish: scalable forebrain organoid models of embryonal brain tumors for high‑throughput personalized drug discovery" (**PMID:41177766 ✓**, 2025) — the most promising route past the single‑cell‑line bottleneck.
- **In vitro modelling of ETMR and other novel brain tumour types** (PMC9164862 ⚠) — abstract‑level.
- **No zebrafish, Drosophila, C. elegans, or yeast model** of ETMR exists, and for C19MC‑driven disease none is possible.
- **No rat model.**

### 15.4 Phenotype recapitulation and limitations — summary for `modeled_mechanisms` curation

| Model | Relationship | Fidelity | Divergence to record |
|---|---|---|---|
| BT183 + NSG orthotopic xenograft | `RECAPITULATES` (molecular + morphological; C19MC retained) | **MODERATE–HIGH** | `POPULATION_MISMATCH` — a single patient's tumour stands for the entity; immunodeficient host removes the immune compartment described in PMID:38802706 |
| hGFAP‑cre::lsl‑Lin28A | **`FAILS_TO_RECAPITULATE`** | **LOW** | **Requires `limitations` AND `evidence` under this schema.** `BOUNDARY_OMISSION` — LIN28A is downstream of C19MC and does not reconstitute the circuit |
| Wnt + Shh neural precursor model | `PARTIALLY_RECAPITULATES` | **MODERATE** | `SPECIES_MISMATCH` (no C19MC orthologue), `PROXY_QUANTITY` (pathway co‑activation stands in for the fusion‑driven circuit) |
| Forebrain organoid | `PARTIALLY_RECAPITULATES` | **UNKNOWN** — too new | `BOUNDARY_OMISSION` — no vasculature, no immune compartment, no perivascular niche (and the niche is implicated in chemoresistance) |

### 15.5 Resources

MGI, IMSR, Alliance of Genome Resources (mouse alleles); **Cellosaurus** (the authoritative check for which ETMR lines actually exist — **do this before curating 15.1**); ATCC; GEO/SRA for the ETMR transcriptomic and single‑cell datasets; the DKFZ/Heidelberg methylation reference cohort.

---

## Appendix A — Candidate evidence quotes (⚠ ALL UNVERIFIED)

These are reconstructed from search‑engine renderings of abstracts, **not** from fetched sources. Each must be regenerated with `just fetch-reference PMID:<id>` and re‑verified with `just count-verified-snippets` before use. Several will certainly fail exact‑substring matching as written.

| PMID | Candidate text | Supports |
|---|---|---|
| 24316981 ✓ | "identified, in all cases, C19MC fusions to TTYH1 driving expression of the microRNAs" | The defining fusion |
| 24316981 ✓ | "extreme overexpression of a previously uncharacterized isoform of DNMT3B originating at an alternative promoter that is active only in the first weeks of neural tube development" | The epigenetic mechanism |
| 31802000 ✓ | "Comparison of primary tumours and matched relapse samples showed a strong conservation of structural variants, but low conservation of SNVs" | Relapse biology |
| 31802000 ✓ | "R-loop-associated chromosomal instability can be induced by the loss of DICER1 function" | DICER1 arm mechanism |
| 31287992 ✓ | "potently abrogated by bromodomain inhibitor JQ1, leading to ETMR cell death" | BET inhibition |
| 23161096 ✓ | Strong LIN28A in all 37 ETMRs; focal in 6/50 AT/RT; 816 tumours tested | Diagnostic marker |
| 33908610 ✓ | "5-year progression-free survival (PFS) and overall survival (OS) were 35% and 47%" | Best‑evidenced regimen |
| 28482026 ✓ | "monotherapy with topotecan, volasertib, and actinomycin D led to a temporary response in tumor growth and a significant increase in survival" | Preclinical drug screen |
| 38158710 ✓ | "highly vulnerable toward treatment with the CNS penetrant proteasome inhibitor Marizomib" | Proteasome dependency |
| 34801069 ✓ | LIN28A overexpression gave "no postnatal brain tumor formation" | Negative model result |
| 36090160 ✓ | "consistent with an Embryonal Tumor with Abundant Neuropil and True Rosettes (ETANTR)" in an 8‑month‑old Maine Coon | Veterinary phenocopy |

## Appendix B — Curation flags for this entry

1. **Cancer granularity (design decisions §3a):** ETMR sits at the **WHO/ICC‑defined molecular‑entity rung** and is correctly a single `Disease` entry. The three morphologies (ETANTR, ependymoblastoma, medulloepithelioma) are **not** `has_subtypes` — they are morphological patterns within one entity, deliberately lumped in 2016. The real candidate `has_subtypes` axis is **molecular**: *C19MC‑altered* vs *DICER1‑altered* vs *NOS*. Use `subtype:` foreign keys to stratify the genetic and prevalence rows that genuinely differ.
2. **Cancer cell of origin (derived, not a slot):** mark the C19MC amplification node with `genetic_context: {variant_origin: SOMATIC, functional_impact_category: GAIN_OF_FUNCTION}` and bind the apical radial glia / neural progenitor CL term on that node. The DICER1 node takes `variant_origin: GERMLINE` for the first hit — which means **two origin nodes, and `just check-cancer-origin` will report multi‑origin.** That report is a correct signal here, not a defect; record the reasoning in `notes:`.
3. **Modules:** ETMR is a plausible conformer for several **hallmarks‑of‑cancer** modules (sustaining proliferative signalling, enabling replicative immortality, genome instability and mutation). Run `just list-modules` before picking anchors; do not assume.
4. **`environmental:`** should be **empty with a `Left deliberately uncited.` waiver**, not a speculative ECTO binding.
5. **No `reference_ranges`** belong on this entry — ETMR has no diagnostic analyte and no disease‑owned cut‑off.
6. **No `percentage` on `prevalence`** — use the structured slots as set out in §9.1.
7. **Content fences honoured:** no ALK‑inhibitor clinical or trial evidence, and no evidence regarding 1p36, 11q, or 17q chromosomal changes or chromothripsis, is included. Neither fence materially constrains ETMR content: ALK inhibitors have no role in this disease, and ETMR's copy‑number biology is centred on 19q13.42 and chromosome 2.
8. **Every CURIE in this report requires a lookup before binding** (see the caveat at the top). This is not boilerplate — this session had no OAK, no OLS, and no network, and the repository's own worked examples show that confidently written, plausible, fabricated identifiers pass undetected until term validation catches them.

---

## Sources

- [The molecular landscape of ETMR at diagnosis and relapse — Nature 2019](https://www.nature.com/articles/s41586-019-1815-x) · [PubMed 31802000](https://pubmed.ncbi.nlm.nih.gov/31802000/)
- [Fusion of TTYH1 with the C19MC microRNA cluster… — Nat Genet 2014](https://www.nature.com/articles/ng.2849)
- [Focal genomic amplification at 19q13.42… — PubMed 20407781](https://pubmed.ncbi.nlm.nih.gov/20407781/)
- [ETANTR, ependymoblastoma, and medulloepithelioma share molecular similarity… — PMC4102829](https://pmc.ncbi.nlm.nih.gov/articles/PMC4102829/)
- [LIN28A immunoreactivity is a potent diagnostic marker of ETMR — PubMed 23161096](https://pubmed.ncbi.nlm.nih.gov/23161096/) · [PMC3508282](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3508282/)
- [A C19MC-LIN28A-MYCN Oncogenic Circuit… — Cancer Cell 2019](https://www.cell.com/cancer-cell/fulltext/S1535-6108(19)30293-4)
- [ETMR: a tumor entity in its infancy — Acta Neuropathol 2020, PMC7423804](https://pmc.ncbi.nlm.nih.gov/articles/PMC7423804/)
- [Treatment of ETMR with carboplatin/etoposide induction and high-dose chemotherapy within the prospective P-HIT trial — PubMed 33908610](https://pubmed.ncbi.nlm.nih.gov/33908610/)
- [Preclinical drug screen reveals topotecan, actinomycin D, and volasertib… — PMC5716199](https://pmc.ncbi.nlm.nih.gov/articles/PMC5716199/)
- [Integrated proteomics spotlight the proteasome as a therapeutic vulnerability in ETMR — PubMed 38158710](https://pubmed.ncbi.nlm.nih.gov/38158710/)
- [Cellular hierarchies of ETMR… — Nature Cancer 2025](https://www.nature.com/articles/s43018-025-00964-9) · [PMC12202505](https://pmc.ncbi.nlm.nih.gov/articles/PMC12202505/)
- [A mouse model for ETMR uncovers the therapeutic potential of Sonic-hedgehog inhibitors — Nat Med 2017](https://www.nature.com/articles/nm.4402)
- [Overexpression of Lin28A in neural progenitor cells… — PubMed 34801069](https://pubmed.ncbi.nlm.nih.gov/34801069/) · [PMC8606090](https://pmc.ncbi.nlm.nih.gov/articles/PMC8606090/)
- [A novel C19MC amplified cell line links Lin28/let-7 to mTOR signaling in ETMR — PMC3870842](https://pmc.ncbi.nlm.nih.gov/articles/PMC3870842/)
- [ETMR: Overview of diagnosis and therapy — Neuro-Oncol Adv 2023](https://academic.oup.com/noa/article/5/1/vdad052/7143757)
- [Clinicopathological and prognostic insights into ETMRs — PubMed 41664204](https://pubmed.ncbi.nlm.nih.gov/41664204/) · [PMC12931075](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12931075/)
- [Timing of radiotherapy and autologous stem cell transplantation in ETMR — Childs Nerv Syst 2026](https://link.springer.com/article/10.1007/s00381-026-07490-8) · [PMC13652926](https://pmc.ncbi.nlm.nih.gov/articles/PMC13652926)
- [Potential Importance of Early Focal Radiotherapy Following GTR… — PMC7773839](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7773839/)
- [A modified IRS-III chemotherapy regimen… — PMC7648589](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7648589/)
- [Clinical phenotypes and prognostic features of ETMRs: A Rare Brain Tumor Registry study — medRxiv](https://www.medrxiv.org/content/10.1101/2020.08.12.20171801v1) · [SickKids summary](https://www.sickkids.ca/en/news/archive/2021/largest-international-study-of-rare-childhood-brain-cancer-shows-early-molecular-diagnosis-and-aggressive-therapy-could-improve-patient-outcomes/)
- [PNOC031 — NCT06861244 (ClinicalTrials.gov)](https://clinicaltrials.gov/study/NCT06861244) · [PNOC protocol page](https://pnoc.us/clinical-trial/pnoc031-protocol-for-embryonal-tumor-with-multilayered-rosettes-etmr/) · [PMC11182916](https://pmc.ncbi.nlm.nih.gov/articles/PMC11182916)
- [DNA methylation-based classification of CNS tumours — PubMed 29539639](https://pubmed.ncbi.nlm.nih.gov/29539639/)
- [Genetic mutation and immune infiltration in ETMR — PubMed 38802706](https://pubmed.ncbi.nlm.nih.gov/38802706)
- [Molecular mechanism and therapeutic strategies for ETMR in children (Review) — PubMed 39926370](https://pubmed.ncbi.nlm.nih.gov/39926370/) · [PMC11803348](https://pmc.ncbi.nlm.nih.gov/articles/PMC11803348/)
- [ETMR: Post-treatment maturation and implications for future therapy — PubMed 36965133](https://pubmed.ncbi.nlm.nih.gov/36965133/)
- [ETMR arising from the internal auditory canal of an adult — PubMed 37920133](https://pubmed.ncbi.nlm.nih.gov/37920133)
- [ETMR, C19MC-altered or NEC: 17 children 2018–2022 — PMC9638173](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9638173/)
- [C19MC amplification and expression of Lin28A and Olig2… — PubMed 33236184](https://pubmed.ncbi.nlm.nih.gov/33236184/)
- [Exploring Maintenance Therapy in Pediatric ETMR — PubMed 40193690](https://pubmed.ncbi.nlm.nih.gov/40193690/)
- [Case report: Infratentorial ETANTR in an 8-month-old Maine Coon — PubMed 36090160](https://pubmed.ncbi.nlm.nih.gov/36090160/) · [PMC9453206](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9453206/)
- [The primate-specific microRNA gene cluster (C19MC) is imprinted in the placenta — PubMed 20610438](https://pubmed.ncbi.nlm.nih.gov/20610438/)
- [DICER1-Related Tumor Predisposition — GeneReviews NBK196157](https://www.ncbi.nlm.nih.gov/sites/books/NBK196157/) · [A systematic review of DICER1-mutant malignant brain neoplasms — PMC10193506](https://pmc.ncbi.nlm.nih.gov/articles/PMC10193506/)
- [Orphanet: Embryonal tumor with multilayered rosettes (ORPHA:656417)](https://www.orpha.net/en/disease/detail/656417)
- [Pathology Outlines — Embryonal tumor with multilayered rosettes](https://www.pathologyoutlines.com/topic/cnstumorETMR.html)
- [Embryonal tumors in the WHO CNS5 classification: A Review — Indian J Pathol Microbiol 2022](https://journals.lww.com/ijpm/fulltext/2022/65001/embryonal_tumors_in_the_who_cns5_classification__a.11.aspx)
- [Imaging findings of supratentorial ETMR in children — PubMed 36649993](https://pubmed.ncbi.nlm.nih.gov/36649993/)
- [Increased intracranial pressure HP:0002516 — Monarch Initiative](https://monarchinitiative.org/HP:0002516)
- [In vivo intratumoral heterogeneity in a dish: forebrain organoid models — PubMed 41177766](https://pubmed.ncbi.nlm.nih.gov/41177766/)
- [Childhood Medulloblastoma and Other CNS Embryonal Tumors (PDQ) — NCI](https://www.cancer.gov/types/brain/hp/child-cns-embryonal-treatment-pdq)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 50 |
| Resolved | 50 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 6 |
| Quoted claims found in source | 5 |
| Quoted claims **not** found in source | 1 |
| Quoted claims with nothing to check against | 2 |
| References weighed for topical relevance | 50 |
| On topic | 31 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC3870842` *(abstract only)*: "recapitulates the molecular and morphologic features of the parent tumor and represents an important first model for ETMR and related C19MC‑amplified or Lin28‑overexpressing embryonal brain tumors"
  - closest text in source: "As the first patient-derived cell line of these rare tumors, BT183 is an important, unique reagent for investigating ETMR biology and therapeutics."

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1038/nm.4402`: "uncovers the therapeutic potential of Sonic‑hedgehog inhibitors"
  - Reference resolved but exposes no abstract or full text to search
- `DOI:10.1038/nm.4402`: "ETMRs are characterized by a parallel activation of Shh and Wnt signaling"
  - Reference resolved but exposes no abstract or full text to search
