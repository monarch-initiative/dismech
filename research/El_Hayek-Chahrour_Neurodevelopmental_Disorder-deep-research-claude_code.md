---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5-5
cached: false
start_time: '2026-10-14T15:49:13.778931'
end_time: '2026-10-14T15:52:53.086238'
duration_seconds: 219.31
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: El Hayek-Chahrour neurodevelopmental disorder
  mondo_id: MONDO:0970951
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
  - claude-opus-5-5
  web_search_requests: 2
  num_turns: 18
  total_cost_usd: 2.1534032000000005
  session_id: a24f491c-a675-4352-b341-0e261fe906b5
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 9
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** El Hayek-Chahrour neurodevelopmental disorder
- **MONDO ID:** MONDO:0970951 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **El Hayek-Chahrour neurodevelopmental disorder** covering all of the
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

Let me grab the abstracts and key passages from these full texts.

Gathering the remaining clinical and model-organism details from the cached full texts, then I'll write the report.

# El Hayek-Chahrour Neurodevelopmental Disorder (NEDEHC; KDM5A-related neurodevelopmental disorder): Research Report

**Prepared:** 2026-10-14 · **MONDO:** MONDO:0970951 · **OMIM:** #620820 · **Gene:** *KDM5A* (12p13.33)

### Scope and source basis

Three primary papers from one group, the Chahrour laboratory at UT Southwestern, define what is known about this ultra-rare disorder:

| PMID | Citation | Type | What it contributes |
|---|---|---|---|
| **33350388** | El Hayek L et al., *eLife* 2020;9:e56883, doi:10.7554/eLife.56883 | Mouse forward genetics plus a human cohort (n = 9) | Discovers the gene and defines the disorder. Characterises the *Kdm5a* knockout mouse. |
| **41889174** | El Hayek L, Gogate A, … Chahrour MH, *HGG Advances* 2026 | Human cohort (n = 24) plus in vitro and computational work | Widens the variant and phenotype spectrum. Adds LCL protein levels, RNA-seq, structural modelling and ACMG reclassification. |
| **37992166** | El Hayek L et al., *Sci Adv* 2023, doi:10.1126/sciadv.adi0074 | Mouse snRNA-seq | Shows how hippocampal cell identity is disrupted. |

In this report:
- Quotes marked **[abstract]** come from the abstract.
- Quotes marked **[full text]** come from the PMC full text cached in the repository (`references_cache/`).
- No GeneReviews chapter, Orphanet record, natural-history study, clinical guideline or clinical trial was found.
- The OLS and PubMed MCP connectors were not authorised in this session. Ontology IDs below are **leads to verify with `runoak`/OLS before binding**, not looked-up values.

---

## 1. Disease information

**Overview.** NEDEHC is a Mendelian neurodevelopmental chromatinopathy caused by germline variants in *KDM5A*. It can be inherited in either of two ways:
- **Monoallelic:** de novo, or inherited dominant.
- **Biallelic:** homozygous or compound heterozygous.

*KDM5A* encodes lysine-specific demethylase 5A (JARID1A/RBP2), which removes methyl groups from H3K4me2/3. The core clinical picture is:
- severe speech impairment, often with no speech at all;
- intellectual disability or global developmental delay;
- autism spectrum disorder (ASD).

Variable additional features include hypotonia, seizures, feeding difficulties, sleep disturbance, joint hypermobility, facial dysmorphism, cardiac septal defects and structural brain abnormalities.

- OMIM/MedGen defines it as *"characterized by absent speech, impaired intellectual development, and autism"* ([MedGen C5935620](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/medgen/C5935620/index.html)).
- PMID:41889174 [abstract]: *"All individuals presented with severe speech impairment and intellectual disability, often alongside ASD and other neurodevelopmental features."*

**Identifiers**

| System | ID | Notes |
|---|---|---|
| OMIM | 620820 | Phenotype entry; gene MIM 180202 (*KDM5A*). |
| MONDO | MONDO:0970951 | "El Hayek-Chahrour neurodevelopmental disorder" |
| MedGen | C5935620 | |
| KEGG DISEASE | H02803 | Listed as a subtype of "Neurodevelopmental disorder with histone modification defect", alongside KMT2E, KDM6B, SETD1A, KAT5, DOT1L and other genes ([KEGG H02803](https://www.kegg.jp/entry/H02803)). |
| Orphanet | None found | |
| ICD-10/ICD-11 | No specific code | Code under F84.0 (autism), F72/F79 (intellectual disability) or the ICD-11 6A00 / LD90 family. |
| MeSH | No specific heading | Nearest: Autism Spectrum Disorder; Intellectual Disability. |
| HGNC | hgnc:9886 (*KDM5A*) | Write it in lowercase `hgnc:` in dismech. **Verify before binding.** |

**Synonyms:** El Hayek-Chahrour neurodevelopmental syndrome; neurodevelopmental disorder with absent speech, impaired intellectual development, and autism; NEDEHC; KDM5A-related neurodevelopmental disorder.

**Data provenance.** All data are aggregated case series assembled through international collaboration (GeneMatcher-style matchmaking, the CAUSES study, and clinical exome and microarray cohorts). No EHR-level data exist.

**Gene–disease curation status**
- **Genomics England PanelApp:** Intellectual Disability panel **Green**, "BOTH monoallelic and biallelic, autosomal or pseudoautosomal"; Fetal Anomalies panel **Amber**; DDG2P **Red** (biallelic, "autosomal recessive mental retardation") ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/entities/KDM5A)).
- **PanelApp Australia:** lists *KDM5A* on its ID panel ([PanelApp-AUS](https://panelapp-aus.org/panels/250/gene/KDM5A/)).
- **ClinGen:** no gene–disease validity classification was found. **Check `cache/clingen/` and `just list-gene-validity` before recording a tier.**

---

## 2. Etiology

**Cause.** The disorder is purely genetic: pathogenic germline *KDM5A* variants. No environmental or infectious component has been described.

PMID:41889174 [full text]: *"In conclusion, both monoallelic and biallelic KDM5A variants cause a neurodevelopmental disorder characterized by ASD, severe speech abnormalities, developmental delay, and intellectual disability."*

**Genetic risk factors**
- Consanguinity: many of the biallelic families come from Iran, Saudi Arabia, Egypt and Kuwait.
- A parent carrying a heterozygous variant: several monoallelic variants were inherited from parents described as mildly affected or unaffected, which raises the question of incomplete penetrance (see §9).

**Protective factors, modifiers, gene–environment interactions:** none reported.

**Historical antecedent.** One homozygous *KDM5A* missense family was reported in the Najmabadi et al. 2011 autosomal-recessive intellectual disability screen (*Nature*; PMID:21937992 — verify the PMID).

PMID:33350388 [full text]: *"To date only a single recessive missense variant in KDM5A has been reported to be associated with an undefined developmental disorder (intellectual disability and facial dysmorphisms) in one family (Najmabadi et al."*

---

## 3. Phenotypes

**Counting basis.** Frequencies combine the 2020 cohort (n = 9) and the 2026 cohort (n = 24); the denominator is about 33 individuals. The 2026 cohort figures are counted from the published Table 1, split by monoallelic (n = 11–12 evaluable) and biallelic (n = 13) groups. Counts are approximate where the table reports "UK" (unknown) or "N/A".

| Phenotype | Type / onset | Approx. frequency | Suggested HPO (verify) | Notes |
|---|---|---|---|---|
| Absent or severely impaired speech | Sign; infancy/childhood | ~100% impaired; ~70% absent | HP:0001344 Absent speech; HP:0002463 Language impairment / HP:0000750 Delayed speech and language development | The defining feature. All 9 in 2020 lacked speech. |
| Intellectual disability | Childhood | ~90–100% | HP:0001249 Intellectual disability | Universal in the biallelic group. |
| Global developmental delay | Infancy | ~90–100% | HP:0001263 | |
| Autism spectrum disorder | Childhood | Majority (~75–85%) | HP:0000729 Autistic behavior; HP:0000717 Autism | Repetitive behaviour, hand flapping, echolalia |
| Muscle hypotonia | Infancy | ~50% overall; higher in biallelic (~10/13) | HP:0001252 | |
| Seizures | Childhood | ~30%; more often biallelic (~7/13) | HP:0001250 | |
| Feeding difficulties | Infancy | ~50% | HP:0011968 | Includes selective eating |
| Sleep disturbance | Childhood | ~40% | HP:0002360 | |
| Joint hypermobility / hyperextensible joints | — | ~40% | HP:0001382 | |
| Facial dysmorphism | Congenital | ~50% | HP:0001999 | MedGen lists frontal bossing, micrognathia and low-set ears |
| Thin / hypoplastic corpus callosum | Congenital | ~5 biallelic individuals | HP:0002079 Hypoplasia of the corpus callosum | |
| Ventriculomegaly (mild) | — | Several | HP:0002119 | |
| Cerebral atrophy / reduced white matter / periventricular leukomalacia | — | Several biallelic | HP:0002059; HP:0006970 | |
| Dandy-Walker spectrum with hydrocephalus | Congenital | 1 | HP:0001305 | Monoallelic |
| Congenital heart defects (ASD, VSD, complex CHD, coarctation, pulmonary stenosis) | Congenital | ~6–8 individuals | HP:0001631 ASD; HP:0001629 VSD; HP:0001627 | |
| Inability to walk / motor impairment | Childhood | ~3 biallelic | HP:0002540 Inability to walk; HP:0001270 Motor delay | |
| ADHD / hyperactivity / attention deficit | Childhood | Several | HP:0007018; HP:0000752 | |
| Self-injurious behaviour, aggression, anxiety, mood disorders | Childhood/adult | Several | HP:0100716; HP:0000718; HP:0000739 | |
| Constipation | — | Several | HP:0002019 | |
| Visual issues (cortical visual impairment, hyperopia) and hearing loss | — | Few | HP:0100704; HP:0000365 | |
| Recurrent upper respiratory infections | — | Few | HP:0002788 | |
| Microcephaly / macrocephaly | Congenital | Few, discordant | HP:0000252 / HP:0000256 | One case of progressive fetal macrocephaly; MedGen lists microcephaly |
| Toe syndactyly, clinodactyly, hallux valgus | Congenital | Few | HP:0001770; HP:0030084; HP:0001822 | |

**Supporting quotes (PMID:41889174 [full text])**
- *"Additional phenotypes included autistic features, developmental delay, intellectual disability, muscle hypotonia, seizures, and cardiac abnormalities"*
- *"Additional shared phenotypes included developmental delay (five individuals), feeding difficulties (five individuals), intellectual disability (four individuals), and sleep disturbances (four individuals)."*
- *"The condition is often accompanied by comorbidities, including intellectual disability, developmental delay, motor impairments, and seizures."*

**Genotype–phenotype trend (observed in this report, not stated by the authors).** Biallelic individuals in Table 1 appear to have more seizures, hypotonia, structural brain MRI abnormalities and non-ambulation. The authors do not formally state this, so record it as an observation rather than a curated claim.

**Severity, course and quality of life**
- Severity: moderate to severe.
- Course: static neurodevelopmental. No regression is reported.
- Burden: lifelong dependence driven mainly by absent speech and intellectual disability.
- No QoL instrument data exist.

---

## 4. Genetic and molecular information

**Gene.** *KDM5A* (JARID1A, RBP2). Transcript NM_001042603. Protein of 1,690 aa.

**Domain map** (PMID:41889174 [full text]):

| Domain | Residues |
|---|---|
| JmjN | 18–59 |
| ARID | 85–170 |
| PHD1 | 295–343 |
| JmjC | 470–586 |
| Zn | 676–728 |
| PLU1 | 741–1,072 |
| PHD2 | 1,163–1,215 |
| PHD3 | 1,608–1,659 |

- The catalytic core is JmjN plus JmjC (Fe(II)/2-oxoglutarate dependent).
- PHD1 binds unmodified H3K4 and stimulates catalytic activity.
- PHD3 binds H3K4me2/3.

**Variant spectrum**
- Across both cohorts there are **31 unique, all private variants** in 33 individuals from 28 families: missense, nonsense, frameshift, splice-site, and multi-exon deletions of 4 and 10 exons.
- **2020 cohort (PMID:33350388) [full text]:** *"Three individuals carried homozygous deletions removing four exons (in two individuals) or ten exons (in one individual) of KDM5A, three individuals carried homozygous recessive variants (two splice site and one missense), and the remaining three individuals were heterozygous for de novo variants (two missense and one nonsense)"*
- **2026 cohort (PMID:41889174) [full text]:** *"There were 12 individuals with biallelic variants and 12 individuals with monoallelic variants"*. Of these, 7 were de novo, 13 inherited, and 4 of unknown inheritance.
- **Location in the protein (2026 cohort):** JmjC 1, JmjN 1, PHD1 1, PHD3 1, PLU1 7, inter-domain 13. PLU1 is a clear cluster.
- **Recurrence:** PMID:41889174 [full text]: *"Importantly, all 31 unique variants identified to date are private, with no recurrent alleles observed across unrelated individuals."*

**Classification.** PMID:41889174 [abstract]: *"American College of Medical Genetics and Genomics-guided reclassification supported pathogenicity for the majority of variants, including multiple upgrades from uncertain significance to pathogenic or likely pathogenic."*

**Functional consequence**
- **Loss of function / reduced dosage.** PMID:41889174 [abstract]: *"For a subset of variants, we demonstrated reduced KDM5A protein levels in cell lines derived from affected individuals."*
- **Domain disruption without protein loss is also proposed.** PMID:41889174 [full text]: *"While variants in the JmjC domain can impair its demethylase function, variants in other domains may disrupt non-enzymatic functions, such as chromatin positioning or interactions with regulatory complexes, leading to equally severe phenotypes."*

**Origin, population frequency and other genomic features**
- Origin: germline only. No somatic mosaic cases are reported.
- Population frequency: variants are absent or ultra-rare in gnomAD, per the cohort filtering criteria.
- Modifier genes, epigenetic signatures and chromosomal rearrangements: none described.
- Episignature: no DNA-methylation episignature has been reported, unlike KDM5C and other chromatinopathies. This is a gap.
- Microdeletions: some biallelic alleles are intragenic CNVs found by read-depth or split-read analysis, so CNV-aware analysis matters (see §10).
- Nearby locus: *KDM5A* sits at the 12p13.33 subtelomere, near the *CACNA1C*/*ERC1* region. No reports of contiguous-gene syndromes involving *KDM5A* were found.

---

## 5. Environmental information

None. No environmental, lifestyle or infectious factors apply.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Initiating lesion.** Germline *KDM5A* variants occur in one of two configurations:
   - Monoallelic: de novo or inherited missense or truncating variants.
   - Biallelic: multi-exon deletions, splice, frameshift, nonsense or missense variants.

   These lead to →
2. **Reduced KDM5A protein or a domain-specific functional defect.** Patient lymphoblastoid cell lines (LCLs) show reduced protein for a subset of variants; JmjC, PLU1 and PHD variants are predicted to disrupt catalysis or chromatin binding. This is demonstrated in LCLs and inferred from structural modelling for the rest. It results in →
3. **Altered H3K4me2/3 demethylation at KDM5A target promoters and enhancers.** This step is *inferred*: no patient or mouse H3K4me3 ChIP data are cited in these papers. It leads to →
4. **Dysregulated transcription.**
   - Patient LCL RNA-seq shows variant-specific expression changes, worst for PLU1, then JmjC, then inter-domain variants.
   - Mouse *Kdm5a*⁻/⁻ hippocampus has 450 differentially expressed genes, including ASD genes (*Oxtr*, *Cnr1*, *Ppp1r1b*, *Ace*) and brain-development genes (*Otx2*, *Sema3b*, *Cdh3*).

   This leads to →
5. **A defect in the switch that sets neuronal differentiation and cell identity during hippocampal development.** Superficial (Satb2⁺) and deep (Col11a1⁺) CA1 identity is mis-specified, and specific excitatory and inhibitory subtypes are affected. This is shown in mouse snRNA-seq. In parallel (branch) →
6. **Impaired dendritic morphogenesis.** Cortical neurons show about 67% less dendritic complexity, about 50% shorter dendrites and about 33% lower spine density (mouse, Golgi-Cox). This results in →
7. **Abnormal circuit formation and synaptic connectivity.** This step is *inferred*. It leads to →
8. **Clinical phenotype:**
   - absent speech / communication deficit (mouse USV deficit);
   - ASD-like behaviour (repetitive grooming, sociability deficit, poor nest building);
   - intellectual disability (Morris water maze learning and memory deficit);
   - seizures.

   **Branch:** multisystem features (cardiac septal defects, corpus callosum hypoplasia, joint laxity) presumably reflect KDM5A's ubiquitous expression and its developmental role outside the brain. These are *not mechanistically studied*.

### Key evidence

- **Mouse knockout phenotype.** PMID:33350388 [abstract]: *"Kdm5a-/- mice displayed repetitive behaviors, sociability deficits, cognitive dysfunction, and abnormal dendritic morphogenesis. Loss of KDM5A also resulted in dysregulation of the hippocampal transcriptome."*
- **Dendritic measurements.** PMID:33350388 [full text]: *"cortical neurons from Kdm5a-/- mice had significant reduction in dendritic length (∼50% decrease) and dendritic spine density (∼33% decrease) compared with neurons from WT littermates"*
- **Hippocampal transcriptome.** PMID:33350388 [full text]: *"Out of 450 differentially expressed genes, 15 were homologs of known ASD genes, including Ace, Cnr1, Mfrp, Oxtr, and Ppp1r1b, and 33 were homologs of genes essential for brain development"*
- **Predicted direction of target-gene change.** PMID:33350388 [full text]: *"By demethylating H3K4me3, an activating histone mark, KDM5A would be expected to repress the expression of its target genes, suggesting that genes upregulated in the hippocampus of the Kdm5a-/- mice are potential direct targets of KDM5A."* The paper frames this as an expectation, so it is not demonstrated.
- **Cell identity.** PMID:37992166 [abstract]: *"KDM5A regulates the development of specific subtypes of excitatory and inhibitory neurons. We found that KDM5A is essential for establishing hippocampal cell identity by controlling a differentiation switch early in development."*
- **Loss of a CA1 population.** PMID:37992166 [full text]: *"the loss of CA1 superficial neurons marked by the expression of Satb2 in Kdm5a−/− is predicted to be one major factor leading to the severe cognitive deficits observed upon loss of KDM5A"*
- **Patient transcriptomics.** PMID:41889174 [abstract]: *"Transcriptomic profiling revealed variant-specific gene expression changes, most pronounced in variants affecting the PLU1 chromatin-binding motif and the Jumonji C domain of the enzymatic core."*

### Ontology suggestions (verify each)

**GO biological processes**
- histone H3-K4 demethylation (GO:0034720) — the current GO label may be "histone H3K4 demethylation"
- regulation of DNA-templated transcription (GO:0006355)
- dendrite morphogenesis (GO:0048813)
- dendritic spine development (GO:0060996)
- neuron differentiation (GO:0030182)
- hippocampus development (GO:0021766)
- vocalization behavior (GO:0071625)
- learning or memory (GO:0007611)

**GO molecular function:** histone H3K4me/H3K4me2/H3K4me3 demethylase activity (GO:0032453 / GO:0034647 family — verify the current IDs).

**Cell types (CL)**
- excitatory neuron / glutamatergic neuron (CL:0000679)
- GABAergic interneuron (CL:0000617)
- hippocampal CA1 pyramidal neuron (CL:4023111 or similar — verify)
- cerebral cortex neuron (CL:0010012)

**Other mechanistic categories:** no immune, metabolic or tissue-damage mechanisms are described. The disorder is a developmental chromatin-regulation defect.

**Molecular profiling.** RNA-seq exists from patient LCLs (PMID:41889174) and mouse hippocampus (bulk and snRNA-seq). Check GEO for the accessions with `just discover-datasets`; the accessions were not verified here. No proteomics, metabolomics or human single-cell data were found.

---

## 7. Anatomical structures

| Level | Structures | Suggested ontology terms |
|---|---|---|
| Primary organ | Brain | UBERON:0000955 |
| Brain regions | Hippocampus, especially CA1 (mouse); cerebral cortex; corpus callosum; lateral ventricles; cerebral white matter | UBERON:0001954 hippocampus (Ammon's horn); UBERON:0003881 CA1 field; UBERON:0000956; UBERON:0002336; UBERON:0002285; UBERON:0002437 |
| Secondary systems | Heart (interatrial and interventricular septa); joints / connective tissue; gastrointestinal tract (feeding, constipation) | UBERON:0000948 |
| Subcellular | Nucleus / chromatin | GO:0005634; GO:0000785 |

Brain imaging findings are bilateral and diffuse.

---

## 8. Temporal development

| Aspect | Finding |
|---|---|
| Onset | Congenital or infantile. Delayed milestones, hypotonia and feeding problems appear in infancy. Absent speech and ASD become apparent in the toddler years. One individual had progressive macrocephaly and polyhydramnios in late pregnancy. |
| Course | Static or non-progressive, and lifelong. Ages at last evaluation ranged from 1 y 3 m to 29 y. Some adults have psychiatric comorbidity (bipolar disorder, depression, panic attacks). |
| Stages and remission | None defined. |
| Critical period | The mouse data place KDM5A's action in early hippocampal development ("a differentiation switch early in development"). This suggests an early prenatal or postnatal window, which bears on any future therapy. |

---

## 9. Inheritance and population

**Inheritance**
- Autosomal dominant (HP:0000006): 15 of 33 individuals.
- Autosomal recessive (HP:0000007): 18 of 33 individuals.
- PanelApp lists "BOTH monoallelic and biallelic".

**Penetrance and expressivity**
- Several monoallelic variants were inherited from a parent. Penetrance may be incomplete, or the transmitting parents may have mild phenotypes. Parental phenotypes are only partly described.
- Expressivity is variable.

**Other inheritance features**
- No anticipation.
- No reported germline or somatic mosaicism.
- No founder alleles, because every variant is private.

**Consanguinity.** Prominent in the biallelic families, which come mainly from Iran, the Arabian Peninsula, Egypt and Kuwait. Monoallelic cases come mainly from Europe and the USA.

**Prevalence.** Unknown; ultra-rare. Exactly 33 published individuals from 28 families (PMID:41889174 [full text]: *"significantly increasing the number of known cases to a total of 33"*). For a dismech entry this is `measure_type: CASES_IN_LITERATURE` with `prevalence_class: ULTRA_RARE` — and should not use the deprecated `percentage` field.

**Demographics.** Both sexes are affected. There are too few cases to establish a sex ratio.

---

## 10. Diagnostics

**Genetic testing (primary)**
- First-tier test: exome or genome sequencing.
- *Use CNV-aware calling.* Intragenic homozygous deletions of 4 or 10 exons were found by read depth and split reads. PMID:33350388 [full text]: *"A combination of read depth calling and split-read analysis identified a homozygous deletion encompassing four exons of KDM5A, spanning 10 kb"*.
- Chromosomal microarray can detect the larger deletions.
- *KDM5A* is on the Genomics England ID panel (green).

**Functional and adjunctive tests (research use only)**
- Western blot of patient LCLs shows reduced KDM5A protein.
- Patient-cell RNA-seq.
- No validated biomarker or episignature exists.

**Clinical work-up**
- Brain MRI (corpus callosum, ventricles, white matter).
- EEG if seizures occur.
- Echocardiography, given the septal defects.
- Formal ASD assessment (ADOS-2).
- Developmental and IQ testing.
- Audiology and ophthalmology.

**Differential diagnosis**
- Other H3K4-methylation chromatinopathies:
  - *KDM5C* (X-linked Claes-Jensen ID);
  - *KDM5B* (AR ID);
  - *KMT2A* (Wiedemann-Steiner syndrome);
  - *KMT2D* (Kabuki syndrome);
  - *SETD1A*, *KMT2E*.
- Other syndromes with absent speech and ASD:
  - *MECP2* (Rett syndrome);
  - Angelman syndrome (*UBE3A*);
  - *CHD8*, *ARID1B*, *SETD5*, *FOXP1*.
- Molecular testing is required to tell these apart.

**Screening.** No newborn screening. Cascade testing of parents and siblings, and prenatal or preimplantation testing, are feasible once the familial variants are known.

---

## 11. Outcome and prognosis

- **Mortality and life expectancy:** no mortality data. The oldest reported individual is 29.
- **Morbidity:**
  - absent or minimal speech;
  - intellectual disability;
  - non-ambulation in a subset of biallelic individuals;
  - seizures;
  - behavioural and psychiatric comorbidity (self-injury, ADHD, mood disorders);
  - congenital heart disease, some of which resolved and one case with pulmonary hypertension.
- **Prognostic factors:** none established. The biallelic genotype and PLU1/JmjC variants are hypothesised to be more severe, based on LCL transcriptomic data.

---

## 12. Treatment

**Disease-modifying treatments:** none. No trials appear on ClinicalTrials.gov or WHO ICTRP. Management is supportive and multidisciplinary.

| Intervention | Suggested NCIT terms (verify) | `therapeutic_modality` |
|---|---|---|
| Speech-language therapy and augmentative and alternative communication (AAC) | Speech Language Therapy (NCIT:C159273) | BEHAVIORAL |
| Applied behaviour analysis / behavioural therapy for ASD | Behavioral counseling NCIT:C181743 or a behavioural-therapy term | BEHAVIORAL |
| Physical and occupational therapy for hypotonia and motor delay | Physical Therapy (NCIT:C15302); Occupational Therapy (NCIT:C121351) | BEHAVIORAL |
| Antiseizure medication | Pharmacotherapy (NCIT:C15986) with an agent class | — |
| Feeding and nutritional support | Dietary Intervention / Nutritional Support | — |
| Cardiac surgical repair of septal defects where indicated | Surgical Procedure (NCIT:C15329) | SURGERY |
| Sleep management, e.g. melatonin | Pharmacotherapy (NCIT:C15986); agent melatonin, CHEBI:16796 (verify) | — |
| Genetic counselling | Genetic Counseling (NCIT:C15240) | — |

**Research directions (speculative; no data in this disease)**
- KDM5 inhibitors are oncology tools and would go the wrong way for a loss-of-function disorder.
- Approaches that restore dosage (gene therapy, CRISPRa) have not been tested.

---

## 13. Prevention

- **Primary:** not applicable.
- **Genetic counselling:**
  - Recurrence risk is 25% for biallelic families.
  - Risk is up to 50% when an affected or carrier parent transmits a monoallelic variant.
  - Risk is low (germline-mosaicism level) for de novo cases.
- **Reproductive options:** prenatal diagnosis or PGT-M for known familial variants.
- **Tertiary prevention:**
  - seizure surveillance;
  - cardiac screening by echocardiography at diagnosis;
  - early intensive communication intervention.

---

## 14. Other species and natural disease

- No naturally occurring animal disease was found; OMIA was not checked in detail.
- Orthologs:
  - mouse *Kdm5a* (MGI:2136268 — verify), NCBITaxon:10090;
  - *Drosophila* has a single KDM5 ortholog (*Kdm5/lid*), which is implicated in intellectual-disability-related behaviour in flies through the *KDM5C* literature.
- KDM5 family function in H3K4 demethylation is conserved from yeast (Jhd2) to humans.

---

## 15. Model organisms

### *Kdm5a* Selbst ENU allele (p.C322\*), C57BL/6J mouse

- **Phenotypes:** recessive reduction in USV peak frequency and impaired nest building.
- **Fidelity:** found by unbiased forward genetics, with strong linkage (p = 2.9×10⁻⁵ for USV; p = 7.0×10⁻⁵ for nesting).

### *Kdm5a*⁻/⁻ targeted knockout mouse (PMID:33350388; PMID:37992166)

**What it recapitulates**
- vocalization deficit, as a proxy for absent speech;
- repetitive grooming;
- sociability deficit;
- Morris water maze learning and memory deficit;
- reduced dendritic complexity and spine density;
- hippocampal transcriptome dysregulation;
- mis-specified CA1 superficial and deep identity (snRNA-seq).

**Limitations**
- Heterozygous mice learn normally. PMID:33350388 [full text]: *"WT and Kdm5a+/- littermates had normal learning abilities"*. So the model does not reproduce the human **monoallelic** disease. This is a `HUMAN_MODEL_MISMATCH` candidate in dismech terms.
- USV is a proxy for speech, not speech itself.
- No seizure, cardiac, corpus callosum or joint phenotypes were reported.
- Missense alleles have not been modelled.

**Suggested dismech link encoding:** `RECAPITULATES` / `PARTIALLY_RECAPITULATES` to the ASD-behaviour and dendritic nodes; `model_scale: ORGANISM`; `evidence_source: MODEL_ORGANISM`.

### Cellular models

- Patient-derived LCLs (PMID:41889174): reduced KDM5A protein and variant-specific transcriptomes. Encode these as `IN_VITRO` evidence.
- No iPSC-derived neurons or organoids have been reported. This is a gap.

---

## Knowledge gaps (candidates for `KNOWLEDGE_GAP` discussions)

1. **Haploinsufficiency mismatch.** Heterozygous *Kdm5a* mice show no cognitive phenotype, yet humans with monoallelic variants are affected. Is the human disease caused by dominant-negative effects, a species-specific dosage threshold, or incomplete penetrance?
2. **Direct chromatin readout.** No H3K4me3 ChIP-seq or CUT&Tag exists in patient cells or mutant neurons.
3. **Episignature.** No DNA-methylation episignature is available as a diagnostic aid.
4. **Natural history.** There are no longitudinal data, adult outcomes or seizure semiology.
5. **Extra-neural features.** The mechanism behind the cardiac and connective-tissue features is unexplored.

---

## Sources

- El Hayek L et al. (2020) KDM5A mutations identified in autism spectrum disorder using forward genetics. *eLife* 9:e56883. PMID:33350388. https://doi.org/10.7554/eLife.56883
- El Hayek L et al. (2023) Disruption of the autism gene and chromatin regulator KDM5A alters hippocampal cell identity. *Sci Adv*. PMID:37992166. https://doi.org/10.1126/sciadv.adi0074
- El Hayek L, Gogate A, et al., Chahrour MH (2026) Monoallelic and biallelic KDM5A variants identified in patients with autism spectrum disorder. *HGG Adv*. PMID:41889174. [Maastricht CRIS record](https://cris.maastrichtuniversity.nl/en/publications/monoallelic-and-biallelic-kdm5a-variants-identified-in-patients-w/)
- [MedGen C5935620 / OMIM 620820 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/medgen/C5935620/index.html)
- [KEGG DISEASE H02803](https://www.kegg.jp/entry/H02803)
- [Genomics England PanelApp – KDM5A](https://panelapp.genomicsengland.co.uk/panels/entities/KDM5A)
- [PanelApp Australia – KDM5A](https://panelapp-aus.org/panels/250/gene/KDM5A/)
- [ERN-ITHACA syndrome page](https://ern-ithaca.eu/?p=2416) (listed in search results; not reviewed)
- Najmabadi H et al. (2011) Deep sequencing reveals 50 novel genes for recessive cognitive disorders. *Nature*. PMID:21937992 (verify; cited secondhand through PMID:33350388)
- Excluded as off-target: Sotoudeh Anvari et al. 2024, *Iran J Pediatr*, which describes a **KDM5C** case and not KDM5A ([brieflands](https://brieflands.com/articles/ijp-143515)).
