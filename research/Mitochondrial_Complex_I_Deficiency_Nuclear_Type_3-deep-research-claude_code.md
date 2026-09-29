---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-02T13:24:11.496438'
end_time: '2026-09-02T13:28:29.272030'
duration_seconds: 257.78
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Mitochondrial Complex I Deficiency Nuclear Type 3
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
  web_search_requests: 19
  num_turns: 25
  total_cost_usd: 1.3476208
  session_id: a7ad17b6-3a08-5da2-b864-d177f77ddc2f
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 18
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial Complex I Deficiency Nuclear Type 3
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex I Deficiency Nuclear Type 3** covering all of the
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

I'll research this disease using web search and fetch tools to compile a comprehensive report.

I now have sufficient material to compile a comprehensive report. Here it is:

# Mitochondrial Complex I Deficiency, Nuclear Type 3 (MC1DN3) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Mitochondrial Complex I Deficiency, Nuclear Type 3 (MC1DN3) is an autosomal recessive mitochondrial disorder caused by biallelic pathogenic variants in **NDUFS7** (NADH:ubiquinone oxidoreductase core subunit S7, "PSST" subunit), a nuclear-encoded structural subunit of mitochondrial respiratory chain Complex I. Loss of NDUFS7 function impairs assembly and catalytic activity of Complex I (NADH:ubiquinone oxidoreductase), the first and largest enzyme of the oxidative phosphorylation (OXPHOS) chain, producing a multisystem, predominantly neurological disease. The great majority of reported patients present with **Leigh syndrome** (subacute necrotizing encephalomyelopathy) or a Leigh-like phenotype — infancy-onset, progressive neurodegeneration with characteristic bilateral symmetric basal ganglia/brainstem lesions and lactic acidosis (OMIM, [omim.org/entry/618224](https://www.omim.org/entry/618224); Wikipedia NDUFS7 summary).

**Key identifiers:**
- **OMIM phenotype:** #618224 — MITOCHONDRIAL COMPLEX I DEFICIENCY, NUCLEAR TYPE 3; MC1DN3
- **OMIM gene:** *601825 — NADH-UBIQUINONE OXIDOREDUCTASE Fe-S PROTEIN 7; NDUFS7
- **Gene location:** chromosome 19p13
- **HGNC:** NDUFS7 (protein also called PSST subunit / CI-20kD / NDUS7)
- Note: MC1DN3 is genetically **distinct** from MC1DN4 (OMIM #618225), which is caused by NDUFV1 mutations on chromosome 11q13 — the two are frequently confused because both present with overlapping Leigh-syndrome/leukoencephalopathy phenotypes, but the causal gene differs.
- Related umbrella clinical entity: **Leigh syndrome** (Orphanet ORPHA:506; OMIM PS256000 phenotypic series; mitochondrial-inherited form OMIM #500017 MILS).

**Synonyms/alternative names:** NADH dehydrogenase (ubiquinone) Fe-S protein 7; NADH-ubiquinone oxidoreductase 20 kDa subunit; complex I-20kD (CI-20kD); PSST subunit of complex I; "Leigh syndrome due to NDUFS7 deficiency."

**Data provenance.** Information on MC1DN3 derives almost entirely from **aggregated case reports and small case series** (individual patients/sibships, largely consanguineous families), not large disease-level registries or EHR-based cohorts — consistent with its status as an ultra-rare Mendelian disorder. OMIM and Orphanet aggregate these case reports; there is no dedicated large-cohort natural history study specific to NDUFS7 (as opposed to Leigh syndrome broadly, for which multi-gene cohorts exist).

## 2. Etiology

**Causal factor:** Biallelic (homozygous or compound heterozygous) loss-of-function/hypomorphic variants in NDUFS7, disrupting Complex I structural integrity and assembly. This is a purely **genetic/mechanistic** (Mendelian) etiology; no environmental or infectious primary cause is implicated, though intercurrent infections/febrile illness commonly precipitate acute metabolic decompensation (a well-documented environmental *modifier* of disease course in Leigh syndrome generally).

**Genetic risk factors:**
- Reported pathogenic variants include:
  - **c.364G>A, p.Val122Met (V122M)** — the original mutation identified by Triepels et al. in two brothers with Complex I–deficient Leigh syndrome (Triepels RH et al., *Ann Neurol* 1999 Jun;45(6):787-790, [PMID:10360771](https://pubmed.ncbi.nlm.nih.gov/10360771/)). ClinVar/InterVar classification: likely pathogenic; gnomAD allele frequency ≈5.6×10⁻⁵ (rs104894705).
  - **c.434G>A, p.Arg145His (R145H)** — homozygous in a girl born to consanguineous Tunisian parents with severe Complex I defect and Leigh syndrome; parents were heterozygous carriers, and the variant was absent from >100 Tunisian controls (Lebon S et al., 2007).
  - **c.17-1167C>G** (deep intronic) — creates a cryptic donor splice site and novel exon, predicted to truncate the protein to 41 aa (retaining only the first 5 native residues); demonstrated by minigene/patient fibroblast studies to markedly reduce fully assembled Complex I on native gel electrophoresis, while other OXPHOS complexes remained normal (Lebon S et al., *Mol Genet Metab* 2007, [PMID:17604671](https://pubmed.ncbi.nlm.nih.gov/17604671/)).
  - **c.16+5G>A** (splice-donor intronic variant, rs375282422) — homozygous in siblings with Leigh syndrome and isolated Complex I assembly defect confirmed via patient fibroblast expression studies and Blue Native PAGE; the 2025 report also documents the longitudinal evolution of basal ganglia/midbrain MRI findings (Rahikkala EJ et al., *Mitochondrion* 2025, [ScienceDirect S1567724925000042](https://www.sciencedirect.com/science/article/pii/S1567724925000042)).
  - A homozygous **splice-site mutation** in two brothers of consanguineous Turkish descent (Lebon et al. 2007; OMIM allelic variant .0003).
- All reported alleles are rare/private, consistent with an ultra-rare autosomal recessive disorder; no common founder allele analogous to the French-Canadian *LRPPRC* Leigh syndrome mutation has been established for NDUFS7 (a search for such a founder effect returned no supporting evidence).
- **Modifier genes:** none specifically established for MC1DN3; in Leigh syndrome broadly, mitochondrial haplogroup and nuclear background can influence phenotypic severity, but this is not gene-specific data for NDUFS7.

**Environmental risk/exacerbating factors:** Catabolic stress — febrile illness, intercurrent infection, fasting/prolonged catabolism, surgery/anesthesia — precipitates acute neurological/metabolic decompensation in Leigh-spectrum Complex I deficiency generally (a general Leigh-syndrome principle, not NDUFS7-specific literature).

**Protective factors:** No genetic or environmental protective factors specific to NDUFS7/MC1DN3 have been reported in the literature surveyed.

**Gene-environment interaction:** The central interaction is that partial residual Complex I capacity (determined by variant severity/hypomorphic nature) interacts with metabolic demand (illness, fever, exercise) to determine whether/when decompensation occurs — a general bioenergetic "threshold effect" recognized across mitochondrial disease, rather than an NDUFS7-specific documented interaction.

## 3. Phenotypes

Reported NDUFS7/MC1DN3 phenotypes cluster tightly around the Leigh syndrome/Leigh-like clinical picture, with additional case reports describing atypical presentations (isolated leukoencephalopathy, focal neurological deficits).

**Clinical signs/symptoms (from OMIM clinical synopsis and case reports):**
| Phenotype | HPO suggestion | Notes |
|---|---|---|
| Elevated blood lactate | HP:0002151 (Increased serum lactate) | Core biochemical feature |
| Elevated CSF lactate | HP:0025554 or HP:0002151 (context: CSF) | Frequently more sensitive than blood lactate |
| Hypotonia | HP:0001252 | Common early sign |
| Ataxia | HP:0001251 | Reported in siblings (age 26 months onset) |
| Dysarthria | HP:0001260 | Reported at 26 months in Triepels et al. index case |
| Feeding difficulties/vomiting | HP:0011968 / HP:0002013 | Reported at 11 months in sibling |
| Hepatomegaly | HP:0002240 | Listed in OMIM clinical synopsis |
| Respiratory insufficiency | HP:0002093 | Can be presenting or terminal feature |
| Progressive facial paralysis (central) | HP:0007209 (facial palsy) | Reported in 2025 case report of compound-het complex I deficiency (NDUFV1, related phenotype) |
| Progressive leukoencephalopathy / periventricular white matter lesions | HP:0002352 / HP:0002500 (leukoencephalopathy) | Reported in intronic-variant case series |
| Bilateral symmetric basal ganglia/brainstem T2-hyperintense lesions | HP:0002490 (abnormal basal ganglia MRI) | Hallmark Leigh MRI signature |
| Developmental regression / psychomotor delay | HP:0002083 / HP:0001263 | Onset after initially normal early development |
| Early death | HP:0025438 | Documented; disease is progressive with a fatal course in many cases |
| Episodic decompensation with illness | (no single HPO term; free text) | Precipitated by intercurrent infection |

**Onset:** Infantile in most reported cases (11–26 months in the founder Triepels cases), though later childhood-onset atypical presentations (e.g., facial palsy/ataxia at 4 years in a related NDUFV1-driven Complex I case) are described in the literature for allelic Complex I deficiency subtypes.

**Course:** Progressive; the OMIM clinical synopsis explicitly lists "progressive disorder" and "early death" among the disease features. Episodic worsening coincident with intercurrent illness is characteristic (a general Leigh-syndrome pattern that also applies to MC1DN3 cases).

**Severity/frequency:** Because the evidence base is individual case reports, formal frequency percentages (e.g., "X% of patients have ataxia") are not available for MC1DN3 specifically; frequencies quoted for Leigh syndrome broadly (e.g., onset 3–12 months, ~50% mortality by age 3 in Complex-I-deficiency-driven Leigh syndrome) should not be over-attributed to the NDUFS7 subtype without gene-specific cohort data.

**Quality of life impact:** Not separately quantified for MC1DN3 in the literature (no EQ-5D/SF-36 data found); qualitatively, the disease causes severe motor, cognitive, and respiratory disability and shortened lifespan.

## 4. Genetic/Molecular Information

**Causal gene:** NDUFS7 (chr19p13; OMIM *601825). Encodes the PSST subunit of Complex I, one of the ~7 core catalytic subunits conserved from bacteria to humans.

**Variant spectrum (biallelic, autosomal recessive):**
- Missense: p.Val122Met (rs104894705), p.Arg145His — both affect highly conserved residues.
- Splice-site/intronic: c.16+5G>A (canonical splice donor), c.17-1167C>G (deep intronic, activates a cryptic exon/donor site).
- No large structural/CNV variants reported in the surveyed literature.

**Population frequency:** Extremely rare; gnomAD reports the V122M allele at ~5.6×10⁻⁵ (heterozygous carrier frequency), consistent with an ultra-rare autosomal recessive disease with no evidence of a common founder allele.

**Zygosity:** All published cases are homozygous (typically from consanguineous unions — Tunisian, Turkish parentage documented) or compound heterozygous.

**Functional consequence:** Loss-of-function/hypomorphic — missense variants destabilize the PSST subunit fold or its interaction partners; splice variants truncate the protein or introduce aberrant sequence, abolishing normal folding. All studied variants impair **Complex I assembly** (demonstrated by Blue Native PAGE showing reduced fully-assembled ~980 kDa holo-Complex I with normal levels of the other OXPHOS complexes), rather than solely reducing catalytic turnover of an otherwise-assembled enzyme.

**Modifier genes / epigenetics / chromosomal abnormalities:** None specifically reported for NDUFS7/MC1DN3.

## 5. Environmental Information

No specific toxin, occupational exposure, or infectious trigger causes MC1DN3 (it is monogenic). The main "environmental" contributor documented across the case literature is **intercurrent infection/febrile illness**, which precipitates acute deterioration by increasing metabolic/energetic demand on an already Complex-I-limited oxidative phosphorylation system (general Leigh-syndrome/mitochondrial-disease principle, illustrated in the index Triepels et al. cases and echoed in the 2025 case report describing recurrent respiratory infections preceding acute presentation).

## 6. Mechanism / Pathophysiology

**Causal chain (numbered, from molecular lesion to clinical manifestation):**

1. Biallelic pathogenic NDUFS7 variants → destabilized or truncated PSST subunit protein (demonstrated directly for missense and splice variants).
2. Destabilized PSST subunit → **failure of Complex I "Q-module" assembly** — NDUFS7 is one of the Fe-S-cluster-containing subunits of the Q module of the peripheral arm, assembled in a stepwise, chaperone-dependent process; NDUFAF5 hydroxylates NDUFS7 at an early stage of this assembly, and loss of functional NDUFS7 stalls this pathway (demonstrated by reduced fully-assembled Complex I on Blue Native PAGE in patient fibroblasts, with other OXPHOS complexes unaffected — this is an established, not merely inferred, biochemical finding).
3. Failed/reduced Complex I assembly → **loss of NADH:ubiquinone oxidoreductase catalytic activity** — the PSST subunit, together with the 49-kDa, TYKY, ND1, and ND5 subunits, forms the catalytic core coordinating electron transfer from the terminal Fe-S cluster (N2) to the ubiquinone-binding site; NDUFS7 loss specifically disrupts this final electron-transfer/proton-coupling step (established via biochemical/structural literature on Complex I architecture).
4. Reduced Complex I activity → **impaired mitochondrial NADH oxidation and electron transport chain flux** → decreased ATP synthesis via oxidative phosphorylation, and a shift toward anaerobic glycolysis.
5. Impaired NADH reoxidation → **elevated NADH/NAD+ ratio, pyruvate accumulation, and increased lactate/alanine production** → the biochemical hallmark of elevated blood and CSF lactate/alanine seen in patients (directly measured in reported cases).
6. Chronic cellular energy deficit, disproportionately affecting **high-energy-demand tissues (CNS, especially basal ganglia/brainstem/subthalamic nuclei; skeletal and cardiac muscle; liver)** → selective vulnerability of these regions (inferred from the tissue distribution of Leigh syndrome lesions and hepatomegaly reported in the clinical synopsis).
7. In brain, chronic bioenergetic failure in specific nuclei → **neuronal injury, demyelination/spongiform change, and reactive gliosis**, producing the bilaterally symmetric necrotic/cavitating lesions of basal ganglia, brainstem, and (in leukoencephalopathy-predominant cases) periventricular white matter seen on MRI (directly observed via neuroimaging and, in one report, neuropathology of "progressive cavitating leukoencephalopathy" attributed to NDUFV1/related Complex I gene variants — the analogous process is inferred, not separately proven, for NDUFS7 imaging findings).
8. Clinically, this tissue injury manifests as → progressive hypotonia, ataxia, dysarthria, developmental regression, and (when brainstem/respiratory centers are involved) respiratory insufficiency, culminating in progressive disability and, in severe cases, early death.
9. Superimposed catabolic stress (fever, infection) → transiently increases cellular energy demand against a fixed reduced Complex I ceiling → **acute episodic decompensation**, a branch point distinct from the baseline progressive trajectory (established clinical pattern, mechanistically inferred rather than directly measured).

**Molecular pathways:** Oxidative phosphorylation / electron transport chain (KEGG map00190, "Oxidative phosphorylation"); NADH:ubiquinone oxidoreductase (EC 1.6.5.3) catalysis; mitochondrial Complex I biogenesis/assembly pathway (Q-module assembly, involving NDUFAF3/4/5/6 chaperones).

**Cellular processes:** Aerobic ATP synthesis, mitochondrial electron transport, cellular redox (NADH/NAD+) homeostasis; secondary compensatory glycolytic shift.

**Protein dysfunction:** Misfolding/destabilization of the PSST subunit (missense variants) or truncation/aberrant splicing (splice variants), both converging on impaired incorporation into the Complex I holoenzyme and disrupted electron transfer between the terminal Fe-S cluster N2 and ubiquinone.

**Metabolic changes:** Lactic acidosis, elevated alanine (a lactate-derived amino acid marker), impaired ATP:ADP ratio in affected tissues.

**Tissue damage mechanism:** Chronic energy failure with likely secondary oxidative stress in the most energy-dependent CNS regions, producing necrotic/cavitating lesions (Leigh-type neuropathology) and demyelination.

**Suggested ontology terms:**
- GO Biological Process: GO:0006120 (mitochondrial electron transport, NADH to ubiquinone), GO:0032981 (mitochondrial respiratory chain complex I assembly)
- GO Molecular Function: GO:0008137 (NADH dehydrogenase (ubiquinone) activity), GO:0051539 (4 iron, 4 sulfur cluster binding)
- GO Cellular Component: GO:0005747 (mitochondrial respiratory chain complex I), GO:0031966 (mitochondrial membrane)
- CL (cell types affected): CL:0000540 (neuron), specifically basal ganglia/brainstem neuronal populations; CL:0000187 (muscle cell) for skeletal/cardiac involvement.

## 7. Anatomical Structures Affected

**Organ level:**
- Primary: Central nervous system (basal ganglia — particularly putamen/globus pallidus/subthalamic nucleus, brainstem, periventricular white matter).
- Secondary: Skeletal muscle (hypotonia); liver (hepatomegaly per OMIM synopsis); respiratory system (secondary to brainstem/bulbar involvement causing respiratory insufficiency).
- Body systems: nervous system (primary), musculoskeletal, hepatic, respiratory.

**Tissue/cell level:** Neurons and glia in basal ganglia/brainstem nuclei; oligodendrocytes/white matter in leukoencephalopathy-predominant presentations; hepatocytes (secondary).

**Subcellular level:** Mitochondrial inner membrane (GO:0005743) — site of Complex I; mitochondrial matrix-facing NADH-binding site.

**Localization:** Bilateral, symmetric lesions are the diagnostic radiological hallmark (basal ganglia, brainstem, and in white-matter-predominant cases, periventricular regions) — UBERON terms: UBERON:0002420 (basal ganglion), UBERON:0002298 (brainstem), UBERON:0002316 (white matter of central nervous system).

## 8. Temporal Development

**Onset:** Infantile in the founder/index cases (11 and 26 months); some allelic Complex-I-deficiency phenotypes present later in childhood (age 4, per a related 2025 case report). Onset is typically insidious/subacute following a period of normal early development, per OMIM clinical synopsis ("onset in infancy after normal early development").

**Progression:** Progressive disorder per OMIM; the disease is not self-limited. Episodic acute decompensation (often triggered by intercurrent illness) is superimposed on the baseline progressive course. A 2025 case series specifically documents the **longitudinal evolution of neuroimaging findings** in siblings with an NDUFS7 splice variant, showing progressive basal ganglia/midbrain involvement over time.

**Duration/outcome:** Chronic, and per OMIM, associated with "early death" in the reported pedigrees — though exact survival statistics specific to NDUFS7 are not established in a cohort (only individual case outcomes are documented; e.g., one 2025 case reported no progression at last follow-up under supportive vitamin/cofactor therapy).

## 9. Inheritance and Population

**Inheritance pattern:** Autosomal recessive (explicitly stated in OMIM #618224 clinical synopsis).

**Penetrance/expressivity:** Full penetrance is implied by all reported homozygotes/compound heterozygotes being clinically affected, though the very small number of published cases limits confidence in this. Phenotypic expressivity varies (classic Leigh syndrome vs. leukoencephalopathy-predominant vs. atypical focal presentations), suggesting variant-dependent residual Complex I activity influences severity.

**Consanguinity:** A recurring feature — reported homozygous cases arose from consanguineous Tunisian and Turkish parentage, consistent with the rarity of the disease and autosomal recessive inheritance.

**Founder effects:** No established population-specific founder allele for NDUFS7 (unlike, e.g., LRPPRC in the French-Canadian Leigh syndrome population); each reported family carries a private variant.

**Epidemiology:** No gene-specific prevalence/incidence figures for MC1DN3 exist. At the umbrella clinical level, **Leigh syndrome** overall has an estimated birth prevalence of ~1 in 36,000–40,000 live births, with founder-effect populations reaching much higher rates (e.g., ~1 in 1,700 in the Faroe Islands, attributable to a different gene). Complex I deficiency accounts for the largest single biochemical subgroup of Leigh syndrome (reported >30% of cases), but NDUFS7 is only one of >75 genes implicated in the broader Leigh syndrome spectrum, so its individual contribution is a small fraction of this.

**Sex ratio / geographic distribution:** No specific sex predilection reported (consistent with autosomal recessive inheritance); geographic distribution reflects reported consanguineous families (Netherlands/Dutch index cases, Tunisia, Turkey, Finland — per the 2025 Mitochondrion report).

## 10. Diagnostics

**Biochemical/clinical tests:**
- Elevated blood and CSF lactate (and alanine) — first-line biochemical clue.
- **Spectrophotometric Complex I enzyme activity assay** in mitochondria-enriched tissue homogenate (muscle biopsy, liver, cultured skin fibroblasts) — classical diagnostic gold standard, exploiting rotenone-sensitive NADH:ubiquinone oxidoreductase activity.
- **Blue Native PAGE (BN-PAGE)** with in-gel activity staining (nitrotetrazolium blue) — resolves and directly visualizes reduced levels of fully assembled holo-Complex I while showing normal levels of other OXPHOS complexes; this was the key technique demonstrating the assembly defect in NDUFS7 splice-variant cases.
- Quantitative immunofluorescent/immunochemical assays for Complex I subunit protein levels (alternative/complementary diagnostic modality).

**Imaging:** Brain MRI — bilateral symmetric T2-hyperintense lesions of basal ganglia and/or brainstem (classic Leigh pattern), or diffuse periventricular white matter lesions in leukoencephalopathy-predominant presentations; MR spectroscopy may show a lactate peak.

**Genetic testing:** Whole exome sequencing (WES) with parental segregation analysis is now the primary diagnostic route (used in essentially all recent case reports, including the 2025 intronic-variant and NDUFV1 compound-heterozygous reports), given the extreme genetic heterogeneity of Leigh syndrome (>75 causal genes). Single-gene NDUFS7 Sanger sequencing/panel testing is available (e.g., via commercial providers such as PreventionGenetics). Deep intronic variants (e.g., c.17-1167C>G, c.16+5G>A) illustrate the diagnostic value of RNA/minigene splicing analysis and fibroblast-based functional studies when exome sequencing alone is inconclusive.

**Differential diagnosis:** Other Leigh syndrome-causing genes (mitochondrial: MT-ND genes, MT-ATP6; nuclear: SURF1, NDUFV1, NDUFS4, NDUFAF-family assembly factors, PDHA1, and others), other leukoencephalopathies, and other causes of infantile lactic acidosis.

**Screening:** No population/newborn screening program specific to MC1DN3; diagnosis is reactive, triggered by clinical suspicion (developmental regression, lactic acidosis, characteristic MRI).

## 11. Outcome/Prognosis

Per OMIM clinical synopsis: **progressive disorder** with reported **early death** in the original pedigrees. No formal survival curves specific to NDUFS7 exist; Leigh syndrome broadly (across all causal genes) carries a poor prognosis, with roughly half of affected individuals dying by age 3 in complex-I-deficiency-driven cases (a Leigh-syndrome-level, not NDUFS7-specific, statistic — cite cautiously). Individual case outcomes vary: one recently reported 4-year-old with compound heterozygous Complex I deficiency and supportive vitamin cofactor treatment showed no clinical progression at last follow-up, illustrating that outcome is highly variant- and case-specific rather than uniform.

**Complications:** Respiratory insufficiency/failure (from brainstem involvement), progressive motor and cognitive disability, feeding difficulties, hepatomegaly/hepatic involvement.

**Prognostic factors:** Presumably variant severity (missense/hypomorphic vs. near-null splice/truncating alleles) and residual Complex I assembly capacity, inferred from the degree of Complex I assembly defect seen on BN-PAGE across different reported variants, though this has not been formally correlated with outcome in a cohort.

## 12. Treatment

There is **no disease-modifying or curative therapy** for MC1DN3; management is supportive/symptomatic, following general Leigh syndrome/mitochondrial disease practice, as reflected in the cofactor "mitochondrial cocktail" regimens used in reported cases:

- **Pharmacotherapy (supportive/supplement-based):** Riboflavin (vitamin B2), thiamine (vitamin B1), biotin, L-carnitine (levocarnitine), and coenzyme Q10 — used in the 2025 compound-heterozygous Complex I deficiency case report to attempt to reduce disease progression (NCIT:C15986 Pharmacotherapy; specific agents map to CHEBI terms — riboflavin CHEBI:17015, thiamine CHEBI:9077, coenzyme Q10 CHEBI:46245).
- **Experimental/investigational agents:** EPI-743 (vatiquinone), a CoQ10 analog antioxidant targeting glutathione synthesis and oxidative stress, has been studied in Leigh syndrome clinical trials (e.g., NCT01721733, NCT01642056, NCT01370447) with reported benefit in some genetically defined Leigh syndrome cohorts (particularly SURF1-related); vatiquinone continues to be evaluated preclinically and clinically for Leigh syndrome broadly, though NDUFS7-specific efficacy data are not available.
- **Symptomatic/supportive care:** Management of hypotonia, feeding support, respiratory support as needed, and levodopa has been used for movement-disorder features in related Complex I deficiency cases (NCIT:C15747 Supportive Care; NCIT:C15302 Physical Therapy for motor rehabilitation).
- **Avoidance of catabolic stress:** Aggressive management of intercurrent infections and avoidance of prolonged fasting to reduce risk of acute decompensation (standard mitochondrial disease practice, not NDUFS7-specific trial data).
- **No approved gene therapy, cell therapy, or targeted molecular therapy** currently exists for NDUFS7-related Complex I deficiency specifically.

## 13. Prevention

No primary prevention (vaccination, etc.) is applicable, as MC1DN3 is a monogenic disorder. Relevant preventive measures are:
- **Genetic counseling** for consanguineous or carrier couples with a known family history, given autosomal recessive inheritance (25% recurrence risk per pregnancy for carrier couples).
- **Carrier screening / prenatal or preimplantation genetic diagnosis** is possible once a familial pathogenic variant is identified, though no population-level carrier screening panel specifically targets NDUFS7 given its rarity.
- **Tertiary prevention:** prompt treatment of intercurrent infections/fever and avoidance of prolonged fasting to reduce risk of acute metabolic decompensation in diagnosed patients (standard mitochondrial-disease management, extrapolated from general Leigh syndrome care, not NDUFS7-specific trial evidence).

## 14. Other Species / Natural Disease

- **Canine model (naturally occurring):** Two Jack Russell Terrier × Chihuahua mixed-breed littermates were identified with spontaneous Leigh syndrome caused by a homozygous NDUFS7 missense variant, **c.535G>A / p.Val179Met**, co-segregating with disease as an autosomal recessive trait. Affected dogs showed progressive ataxia, dystonia, elevated lactate, and bilateral symmetric T2-hyperintense brain MRI lesions with encephalomalacia on histology, and skeletal muscle mitochondrial accumulation (Scientific Reports 2024, DOI: [10.1038/s41598-024-53314-7](https://www.nature.com/articles/s41598-024-53314-7); [PMID:38316835](https://pubmed.ncbi.nlm.nih.gov/38316835/)). This is a strong naturally occurring veterinary model closely recapitulating the human phenotype (NCBITaxon:9615 Canis lupus familiaris).
- **Functional validation in Drosophila melanogaster:** The canine p.Val179Met variant was functionally validated by expressing recombinant wild-type or mutant canine NDUFS7 in flies with ubiquitous knockdown of the fly ortholog *ND-20*; wild-type canine NDUFS7 partially rescued the knockdown phenotype, while the mutant did not — directly demonstrating loss-of-function (same 2024 Scientific Reports study).
- **C. elegans:** A hypomorphic mutation in the NDUFS7 ortholog *nduf-7* has been studied not as a disease model per se, but as a means of activating the mitochondrial unfolded protein stress response and prolonging lifespan via ROS/CED-4 signaling (Oxford Academic G3 journal), illustrating conserved biology of partial Complex I dysfunction across species, though this is a longevity-research context rather than a disease model.
- **Mouse:** A full NDUFS7 knockout is reported as homozygous embryonic/perinatal lethal in International Mouse Phenotyping Consortium (IMPC) screening data, precluding a straightforward constitutive knockout mouse model; by contrast, the related subunit **NDUFS4** knockout mouse is well established as a Leigh-syndrome model (lactic acidosis, brainstem degeneration, fatal respiratory failure ~7–8 weeks) and is the most-used rodent surrogate for Complex-I-deficient Leigh syndrome mechanistic and therapeutic studies, given the embryonic lethality constraint on NDUFS7-specific knockouts.

## 15. Model Organisms Summary

| Model | Type | Genotype | Phenotype recapitulation | Reference |
|---|---|---|---|---|
| Dog (natural disease) | Mammalian, spontaneous | Homozygous NDUFS7 p.Val179Met | High — ataxia, dystonia, lactic acidosis, symmetric MRI lesions, encephalomalacia | Scientific Reports 2024, PMID:38316835 |
| Drosophila melanogaster | Invertebrate, induced (transgenic rescue) | Ubiquitous ND-20 (fly NDUFS7 ortholog) knockdown ± canine WT/mutant NDUFS7 rescue | Functional (rescue assay), not organismal disease phenocopy | Same study as above |
| Patient-derived fibroblasts | Cellular/iPSC-adjacent | Patient homozygous/compound heterozygous NDUFS7 variants | High — direct Complex I assembly defect shown via BN-PAGE | Lebon 2007 (PMID:17604671); Rahikkala 2025 (Mitochondrion) |
| Mouse (NDUFS7 constitutive KO) | Mammalian, genetic | Homozygous knockout | **Not viable** — embryonic/perinatal lethal (IMPC) | IMPC data |
| Mouse (NDUFS4 KO, related subunit) | Mammalian, genetic | Homozygous knockout / conditional (brain, heart) | High — recapitulates Leigh-like encephalopathy, cardiomyopathy | PMID:34849584; PNAS 2010 |
| C. elegans | Invertebrate, genetic | Hypomorphic nduf-7 mutation | Used for stress-response/longevity biology, not disease modeling | G3 journal, Oxford Academic |

---

## Summary for Knowledge-Base Curation Purposes

MC1DN3 is a well-characterized but extremely rare Mendelian entity within the Leigh syndrome/Complex I deficiency spectrum, with a clear molecular mechanism (Q-module assembly failure of Complex I due to loss of the PSST/NDUFS7 subunit → impaired NADH:ubiquinone oxidoreductase activity → lactic acidosis and CNS bioenergetic failure → Leigh-type basal ganglia/brainstem necrosis). Evidence is derived from a handful of case reports/small pedigrees (Triepels 1999, Lebon 2007 ×2 variants, Rahikkala 2025, plus an unrelated-gene compound-heterozygous 2025 case that is sometimes conflated with NDUFS7 in search results but is actually NDUFV1/MC1DN4). Curators should take care to **not conflate MC1DN3 (NDUFS7) with MC1DN4 (NDUFV1)** — both cause overlapping Leigh-syndrome/leukoencephalopathy phenotypes but are genetically and OMIM-numerically distinct. A strong naturally-occurring canine model with Drosophila functional validation (2024) is available and would make an excellent `animal_models` entry with `relationship: RECAPITULATES` given its high fidelity to the human phenotype.

### Sources
- [OMIM #618224 — MC1DN3](https://www.omim.org/entry/618224)
- [OMIM Clinical Synopsis #618224](https://www.omim.org/clinicalSynopsis/618224)
- [OMIM *601825 — NDUFS7 gene](https://omim.org/entry/601825)
- [OMIM #618225 — MC1DN4 (NDUFV1)](https://omim.org/entry/618225)
- [GeneCards — NDUFS7](https://www.genecards.org/card/NDUFS7)
- [Triepels et al. 1999, Ann Neurol — PMID:10360771](https://pubmed.ncbi.nlm.nih.gov/10360771/)
- [Lebon et al. 2007, Mol Genet Metab (cryptic exon) — PMID:17604671](https://pubmed.ncbi.nlm.nih.gov/17604671/)
- [NDUFS7 dog Leigh syndrome + Drosophila validation, Sci Rep 2024 — PMID:38316835](https://pubmed.ncbi.nlm.nih.gov/38316835/)
- [Novel intronic NDUFS7 variant, Mitochondrion 2025](https://www.sciencedirect.com/science/article/pii/S1567724925000042)
- [NDUFAF5 hydroxylates NDUFS7 during Complex I assembly (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4938201/)
- [Complex I deficiency in a 4-year-old boy (NDUFV1), Oxford Academic OMCR 2025](https://academic.oup.com/omcr/article/2025/4/omae166/8109021)
- [Orphanet — Leigh syndrome](https://www.orpha.net/en/disease/detail/506)
- [Nuclear Gene-Encoded Leigh Syndrome Spectrum Overview — GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK320989/)
- [Ndufs4 knockout mouse models of Leigh syndrome — PubMed](https://pubmed.ncbi.nlm.nih.gov/34849584/)
- [EPI-743/vatiquinone Leigh syndrome trial, NCT01721733](https://clinicaltrials.gov/study/NCT01721733)
- [Mutation in C. elegans NDUF-7 activates mitochondrial stress response — G3 journal](https://academic.oup.com/g3journal/article/5/8/1639/6025389)
- [Blue Native PAGE for OXPHOS defect diagnosis — Pediatric Research](https://www.nature.com/articles/pr2001236)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 2 |
| Unverifiable | 1 |
| Terms whose name was checked | 18 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002490` (1 mention) - the report calls it "abnormal basal ganglia MRI"; HP calls it **Increased CSF lactate**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0025438` (1 mention), reported as "Early death" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005747` (obsolete mitochondrial respiratory chain complex I) (1 mention) - replaced by `GO:0045271`
- `CHEBI:9077` (CHEBI_9077) (1 mention) - replaced by `CHEBI:35681`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002151` (2 mentions) - the report calls it "Increased serum lactate"; HP calls it **Increased circulating lactate concentration**, and lists "Increased serum lactate" among its other names
- `HP:0007209` (1 mention) - the report calls it "facial palsy"; HP calls it **Facial paralysis**
- `GO:0005747` (1 mention) - the report calls it "mitochondrial respiratory chain complex I"; GO calls it **obsolete mitochondrial respiratory chain complex I**
- `UBERON:0002316` (1 mention) - the report calls it "white matter of central nervous system"; UBERON calls it **white matter**, and lists "white matter of neuraxis" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
