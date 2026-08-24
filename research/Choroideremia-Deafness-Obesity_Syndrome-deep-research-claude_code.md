---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T22:40:37.668736'
end_time: '2026-07-31T22:45:32.597160'
duration_seconds: 294.93
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Choroideremia-Deafness-Obesity Syndrome
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
  - claude-sonnet-5
  web_search_requests: 10
  num_turns: 21
  total_cost_usd: 1.6550714000000002
  session_id: a291cc30-a015-5499-ae7d-a84ca0428d84
  stop_reason: end_turn
citation_count: 25
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Choroideremia-Deafness-Obesity Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Choroideremia-Deafness-Obesity Syndrome** covering all of the
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

# Comprehensive Research Report: Choroideremia-Deafness-Obesity Syndrome

## Executive Summary

Choroideremia-deafness-obesity syndrome (also known as **Ayazi syndrome**, or **Xq21 contiguous gene deletion syndrome**) is an ultra-rare X-linked recessive **contiguous gene deletion syndrome** caused by hemizygous deletion of a region on Xq21 that encompasses at least the **CHM** gene (choroideremia) and the **POU3F4** gene (X-linked deafness, DFNX2/DFN3), frequently also **ZNF711** (X-linked intellectual disability). It is a genomic-neighbor disorder, not a single-gene disease — the phenotype is the additive/combinatorial result of haploinsufficiency for several physically adjacent genes, making it a valuable "natural experiment" model for how contiguous gene loss produces composite syndromes distinct from any one of its component monogenic diseases (isolated choroideremia, isolated DFNX2 deafness, isolated ZNF711-related intellectual disability).

---

### 1. Disease Information

**Overview:** Choroideremia-deafness-obesity syndrome is an X-linked contiguous gene deletion syndrome in which affected males present with a triad of (1) choroideremia — progressive chorioretinal degeneration causing night blindness and eventual central blindness, (2) congenital mixed (sensorineural and conductive) hearing loss with inner ear malformation, and (3) obesity — typically accompanied by mild-to-moderate intellectual disability/developmental delay. It was first clinically delineated by S. Ayazi in 1981 as a triad of "choroideremia, obesity, and congenital deafness" (PMID:7258279, *American Journal of Ophthalmology* 92(1):63-69, 1981) and was subsequently shown by Merry et al. (1989, *American Journal of Human Genetics*) to represent "choroideremia and deafness with stapes fixation: a contiguous gene deletion syndrome in Xq21."

**Key identifiers:**
| Resource | ID |
|---|---|
| OMIM | **303110** — "CHROMOSOME Xq21 DELETION SYNDROME" (historically catalogued as "Choroideremia, Deafness, and Mental Retardation") |
| Orphanet | **ORPHA:1435** |
| MONDO | **MONDO:0010558** |
| MedGen | UID 763933, CUI **C3551019** (a related/overlapping concept exists at CUI C1844836, "Choroideremia with deafness and obesity syndrome") |
| ICD-10 | Q87.8 (Other specified congenital malformation syndromes, not elsewhere classified) |
| GARD (NIH/NORD) | Disease ID 369 |
| Component gene loci | **CHM** — OMIM 300390 (Xq21.2); **POU3F4** — OMIM 300039 (Xq21.1), disease locus OMIM **304400** (DEAFNESS, X-LINKED 2; DFNX2); **ZNF711** — OMIM 300803 (INTELLECTUAL DEVELOPMENTAL DISORDER, X-LINKED 97; XLID97) |

**Synonyms:** Ayazi syndrome; Choroideremia, obesity, and congenital deafness; Choroideremia-deafness-obesity syndrome; Xq21 deletion syndrome; Xq21 microdeletion/contiguous gene deletion syndrome; del(X)(q21); Chromosome Xq21 deletion syndrome.

**Evidence basis:** All available data derive from **aggregated case reports and small case series** (individual patients and families reported in the literature), not large disease registries or EHR-based cohorts — consistent with an ultra-rare condition. A 2024 comprehensive literature review (PMC11202778) identified **at least 29 probands (28 males, 1 female) from 14 unrelated families** reported worldwide prior to their added case, underscoring the condition's rarity and the case-report nature of the evidence base.

Sources: [Ayazi 1981, PubMed](https://pubmed.ncbi.nlm.nih.gov/7258279/) | [GARD](https://rarediseases.info.nih.gov/diseases/369/choroideremia-deafness-obesity-syndrome) | [MedGen C3551019](https://www.ncbi.nlm.nih.gov/medgen/763933) | [OMIM 303110](https://omim.org/entry/303110) | [Xq21 contiguous gene syndrome literature review, PMC11202778](https://pmc.ncbi.nlm.nih.gov/articles/PMC11202778/)

---

### 2. Etiology

**Disease causal factor:** A **hemizygous interstitial deletion at Xq21.1–q21.2** in affected males (reported deletion sizes range from ~3.7 Mb up to 16 Mb across cases, per PMC11202778, with an 8.05 Mb example characterized by array CGH in PMC5471966). The deletion removes two or more physically contiguous, functionally unrelated genes simultaneously, producing a composite phenotype that is not explained by loss of any single gene.

**Core genes within the deleted interval:**
- **CHM** (Xq21.2) — encodes Rab escort protein 1 (REP1); loss → choroideremia.
- **POU3F4** (Xq21.1) — encodes a POU-domain transcription factor essential for otic mesenchyme/spiral ligament/stria vascularis development; loss → DFNX2/DFN3 X-linked mixed deafness with inner ear (incomplete partition type III) malformation.
- **ZNF711** (Xq21.1) — encodes a C2H2 zinc-finger transcription factor that recruits PHF8 histone demethylase to activate neurodevelopmental genes (e.g., KDM5C); loss → XLID97, mild-to-moderate intellectual disability, sometimes with autistic features.
- Additional genes variably included depending on deletion extent: **CYLC1, RPS6KA6, HDX, APOOL, SATL1, POF1B** (per the PMC11202778 review); larger deletions correlate with broader phenotype (endocrine abnormalities such as ACTH deficiency/hypopituitarism, seizures, renal artery stenosis/hypertension, gait ataxia have been reported in individual cases with more extensive deletions).

**Genetic risk factors:**
- **Causal variant class:** Contiguous gene deletion (structural/copy-number variant), not point mutation, though isolated CHM or POU3F4 point mutations/deletions cause the respective single-gene diseases (choroideremia alone; DFNX2 alone) without the full triad.
- **Inheritance:** X-linked recessive. Per PMC11202778, "all deletions except one de novo case were maternally inherited" — i.e., most cases are inherited from a carrier mother, with recurrence risk counseling accordingly; de novo deletions also occur.
- **Sex:** Affects hemizygous males; obligate/carrier females are usually unaffected but can show attenuated findings (see Population section).
- **Chromosomal rearrangement mechanism:** In at least one reported female case, a **balanced X;4 translocation** with breakpoint at Xq21.2 produced choroideremia, mild sensorineural hearing loss, and primary ovarian failure via gene disruption at the breakpoint and/or a position effect (PMID:11035551): "46,X,t(X;4)(q21.2;p16.3)." This illustrates that both deletions and balanced translocations/breakpoints in this region can produce overlapping phenotypes.

**Risk factor summary:** No environmental, infectious, or lifestyle risk factors are implicated — this is a purely germline structural genomic disorder. Obesity as a syndromic feature is thought to be intrinsic to the deletion (candidate contribution of neighboring loci or a hypothalamic/regulatory mechanism has been proposed but not molecularly resolved) rather than driven by conventional metabolic risk factors, though secondary contributions from any co-occurring endocrinopathy (e.g., hypopituitarism) may compound the metabolic phenotype in individual patients.

**Protective factors:** None specifically documented; this is a deletion syndrome, so there are no described "protective variants" in the conventional sense. Compensation for CHM loss by the paralog **REP2** (encoded by *CHML*) in non-retinal tissues (see Mechanism section) is the closest analog to a tissue-protective genetic buffering mechanism, and it is this buffering — not absent in the retina — that explains the retina-restricted phenotype of the choroideremia component.

**Gene-environment interactions:** None established; the condition is fully genetically determined by the deletion genotype.

Sources: [Xq21 deletion literature review, PMC11202778](https://pmc.ncbi.nlm.nih.gov/articles/PMC11202778/) | [Maternally inherited 8.05 Mb Xq21 deletion, PMC5471966](https://pmc.ncbi.nlm.nih.gov/articles/PMC5471966/) | [Balanced X;4 translocation case, PMID 11035551](https://pubmed.ncbi.nlm.nih.gov/11035551/) | [ZNF711 XLID97, OMIM 300803](https://omim.org/entry/300803)

---

### 3. Phenotypes

**A. Ophthalmologic (choroideremia component)** — HPO: **HP:0001139** (Choroideremia; broader term also **HP:0001107** Retinal atrophy family)
- Progressive **night blindness/nyctalopia** — onset typically childhood; **HP:0000662** Nyctalopia
- Peripheral visual field constriction, progressing centripetally — **HP:0000546** Constriction of peripheral visual field / **HP:0001133** Progressive vision loss
- Chorioretinal atrophy / degeneration of choriocapillaris, RPE, and photoreceptors — **HP:0000533** Chorioretinal atrophy
- Optic atrophy in some cases — **HP:0000648** Optic atrophy
- Eventual **central blindness** in later decades (progressive; disease course spans decades)
- **Onset/course:** insidious onset (often noted in childhood/adolescence, sometimes earlier in syndromic cases per PMC11202778), progressive, non-remitting, chronic lifelong.
- **Frequency:** essentially obligate in hemizygous males with CHM involvement (core diagnostic feature).

**B. Audiologic/vestibular (POU3F4/DFNX2 component)** — HPO: **HP:0000365** Hearing impairment
- **Congenital mixed (sensorineural + conductive) hearing loss**, variable severity moderate-to-profound — **HP:0000750**/**HP:0000407** (sensorineural), **HP:0000405** (conductive)
- **Incomplete partition of the cochlea type III (IP3)**, absent modiolus, bulbous dilation of the internal auditory canal — **HP:0011387** (Incomplete cochlear partition) / cochlear malformation terms
- **Perilymphatic "gusher"** upon stapes surgery (stapes fixation), a pathognomonic DFN3 finding
- Progressive component of the sensorineural loss superimposed on a congenital conductive base
- Vestibular dysfunction/ataxia reported in a subset
- **Onset:** congenital/prelingual. **Course:** stable conductive component; sensorineural component can be progressive.

**C. Metabolic**
- **Obesity** — **HP:0001513** Obesity; onset in childhood, progressive; a defining, near-universal feature of the syndrome per original description and subsequent reports, though its precise mechanistic driver is undetermined.

**D. Neurodevelopmental (ZNF711 component)**
- **Mild-to-moderate intellectual disability** — **HP:0001256** (Mild ID) / **HP:0002342** (Moderate ID)
- **Global developmental delay** — **HP:0001263**
- Speech delay disproportionate to other delays; autism-spectrum features in some individuals (per ZNF711 literature); attention difficulties, hypotonia.

**E. Other/variable features (deletion-size dependent)**
- Growth/postnatal growth retardation — **HP:0008897**
- Gait ataxia/coordination difficulty — **HP:0002131**
- Endocrine abnormalities: ACTH deficiency, hypopituitarism-related hypothyroidism — **HP:0000829** (Hypopituitarism) type terms
- Seizures — **HP:0001250**
- Hypertension and renal artery stenosis — **HP:0000822**, **HP:0001919**-adjacent
- Dysmorphic facial features, dolichocephaly, flat feet (pes planus) — reported in multiple cases (PMC11202778)
- Primary ovarian failure in rare female cases with breakpoint disruption — **HP:0008209**

**Quality of life impact:** Combined progressive blindness plus congenital hearing impairment constitutes a **dual sensory impairment** with major implications for communication, education, and independence, compounded by intellectual disability and obesity-related comorbidities. No disease-specific QoL instrument data were identified in the literature (this is expected given the rarity/case-report nature of the evidence base); general dual-sensory-impairment and syndromic-hearing-loss QoL literature would need to be extrapolated by proxy.

Sources: [GARD](https://rarediseases.info.nih.gov/diseases/369/choroideremia-deafness-obesity-syndrome) | [MedGen C3551019](https://www.ncbi.nlm.nih.gov/medgen/763933) | [Xq21 deletion review, PMC11202778](https://pmc.ncbi.nlm.nih.gov/articles/PMC11202778/)

---

### 4. Genetic/Molecular Information

**Causal genes (all within the deleted Xq21.1–q21.2 interval):**

| Gene | HGNC | OMIM (gene) | Function | Disease when isolated |
|---|---|---|---|---|
| **CHM** | HGNC:1940 | 300390 | Rab escort protein 1 (REP1) | Isolated choroideremia (OMIM 303100) |
| **POU3F4** | HGNC:9215 | 300039 | POU-domain transcription factor | DFNX2/DFN3, X-linked mixed deafness with perilymphatic gusher (OMIM 304400) |
| **ZNF711** | HGNC:13154 | 300803 | Zinc-finger transcription factor, PHF8 recruitment | XLID97, nonsyndromic X-linked intellectual disability (OMIM 300803) |
| CYLC1, RPS6KA6, HDX, APOOL, SATL1, POF1B | — | — | Variably included in larger deletions; contribute to the broader/variable phenotype in some patients | Not independently linked to core triad |

**Variant type/class:** Copy-number loss (deletion), not point mutation, in the classic contiguous gene deletion syndrome; ranges 3.7–16 Mb across reported cases. Balanced X-autosome translocations with a breakpoint in/near Xq21.2 can phenocopy part of the syndrome via gene disruption or position effect (PMID:11035551).

**Pathogenicity/classification:** Deletions of this size and gene content are unambiguously pathogenic (loss-of-function/haploinsufficiency for CHM, POU3F4, and ZNF711 individually have each been independently established as disease-causing via ClinVar/ClinGen assertions for the respective single-gene disorders — choroideremia, DFNX2, XLID97).

**Allele frequency:** Not applicable in the conventional gnomAD/population sense — this is a rare de novo/maternally-inherited structural deletion, not a common polymorphism; not represented in population reference panels as a recurrent allele.

**Somatic vs. germline:** Germline only (constitutional deletion).

**Functional consequence:** Loss of function via haploinsufficiency/hemizygous absence of each contained gene — a **genomic-neighbor (contiguous gene deletion)** mechanism rather than a shared-pathway mechanism. PMC11202778 states explicitly: "POU3F4 and ZNF711 haploinsufficiency is causative of the expression of audiological and neurodevelopmental phenotypes, respectively," while CHM hemizygous loss drives the retinal phenotype independently.

**Modifier genes:** Deletion **size** is the principal modifier of phenotypic breadth/severity — larger deletions incorporating CYLC1/RPS6KA6/HDX/APOOL/SATL1/POF1B are associated with additional findings (endocrine, seizures, renal, ataxia) beyond the core triad.

**Epigenetics:** Not specifically characterized for this contiguous deletion syndrome. Notably, ZNF711 itself functions as an epigenetic regulator (recruiting the **PHF8** histone H3K9me1/2 demethylase to activate neurodevelopmental target genes including **KDM5C**), so loss of ZNF711 in this syndrome represents a downstream epigenetic-regulatory disruption contributing to the intellectual disability component — worth noting as a GO Biological Process annotation (chromatin modification/histone demethylation) even though no direct DNA methylation signature study of the full contiguous-deletion syndrome was found. (A ZNF711-specific DNA methylation "episignature" has been reported for isolated ZNF711 alterations — *European Journal of Human Genetics*, "Clinical findings and a DNA methylation signature in kindreds with alterations in ZNF711.")

**Chromosomal abnormalities:** Interstitial deletion Xq21.1-q21.2 (the defining lesion); balanced X;4 translocation t(X;4)(q21.2;p16.3) as an alternate structural mechanism producing an overlapping (but not identical) phenotype in a reported female case.

Sources: [PMC5471966 — 8.05 Mb deletion case](https://pmc.ncbi.nlm.nih.gov/articles/PMC5471966/) | [PMC11202778 — Xq21 review](https://pmc.ncbi.nlm.nih.gov/articles/PMC11202778/) | [OMIM 300390 CHM](https://omim.org/entry/300390) | [OMIM 304400 DFNX2](https://omim.org/entry/304400) | [OMIM 300803 XLID97](https://omim.org/entry/300803) | [ZNF711 GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=ZNF711)

---

### 5. Environmental Information

No environmental toxin, occupational exposure, radiation, lifestyle (smoking/diet/alcohol), or infectious-agent contribution is documented for this condition — it is a purely genetically determined structural chromosomal deletion syndrome. Not applicable.

---

### 6. Mechanism / Pathophysiology

This syndrome is best modeled as **three largely independent, parallel disease mechanisms operating in the same patient because their causal genes happen to be physically adjacent on Xq21** — a genomic-neighbor / contiguous-gene-deletion architecture, rather than a single convergent pathway.

**(A) Choroideremia arm — CHM/REP1 loss:**
- **Molecular pathway:** CHM encodes **Rab escort protein 1 (REP1)**, an essential component of the **Rab geranylgeranyl transferase II (GGTase-II/RabGGTase)** complex. REP1 recruits newly synthesized Rab GTPases and presents them to GGTase-II for **prenylation** (addition of geranylgeranyl lipid groups), enabling Rab membrane association.
- **Cellular process:** Under-prenylated Rabs (notably **Rab27**, and others such as Rab6A) cannot properly localize to membranes, impairing **vesicular trafficking, exocytosis, and secretion** — GO terms: protein geranylgeranylation (GO:0018344), Rab protein signal transduction (GO:0032482), intracellular protein transport (GO:0006886).
- **Tissue/cell specificity:** REP1 is ubiquitously expressed, but the **paralog REP2** (gene *CHML*) compensates for REP1 loss in essentially all tissues **except the retina**, explaining why hemizygous CHM loss produces disease restricted to the eye despite REP1's ubiquitous expression. Cell types affected: retinal pigment epithelium (CL:0002586), photoreceptor cells (CL:0000210), choriocapillaris endothelium.
- **Tissue damage mechanism:** Progressive degeneration proceeds choriocapillaris → RPE → photoreceptors, with disrupted phagocytosis/trafficking in RPE cells and secondary photoreceptor loss; systemic REP1 deficiency in choroideremia patients has additionally been linked to **lipid metabolism and oxidative stress dysfunction** even outside the retina (PMC8262314).
- Suggested GO/CL/UBERON: GO:0018344 (protein geranylgeranylation), GO:0032482 (Rab protein signal transduction), CL:0000210 (photoreceptor cell), CL:0002586 (retinal pigment epithelial cell), UBERON:0001782 (choroid), UBERON:0000966 (retina).

**(B) Deafness arm — POU3F4 loss:**
- **Molecular pathway:** POU3F4 is a **POU-domain transcription factor** critical for patterning the **otic mesenchyme**; it regulates genes governing **spiral ligament structure, stria vascularis function, and spiral ganglion development** within the cochlea. Recent work also implicates POU3F4 in transcriptional upregulation of **SLC6A20** in the inner ear (Frontiers 2022).
- **Cellular/tissue process:** Loss of POU3F4 disrupts mesenchymal-epithelial signaling during otic capsule development, producing the pathognomonic **incomplete partition type III (IP3)** cochlear malformation, an abnormally patent/dilated communication between the internal auditory canal and cochlear basal turn, absent modiolus, and stapes footplate fixation.
- **Clinical mechanistic correlate:** The IAC-cochlear fistula explains the **perilymphatic "gusher"** on stapes surgery — perilymph under CSF pressure escapes through the abnormal communication — and creates surgical risk (CSF leak, meningitis) during stapedectomy or cochlear implantation.
- Suggested GO/CL/UBERON: GO:0042472 (inner ear morphogenesis), GO:0060119 (inner ear receptor cell development), CL:0000601 (hair cell), UBERON:0001846 (cochlea), UBERON:0002105 (stria vascularis), UBERON:0011276 (spiral ligament).

**(C) Neurodevelopmental arm — ZNF711 loss:**
- **Molecular pathway:** ZNF711 is a zinc-finger (Zn-C2H2) transcription factor that binds target-gene promoters and **recruits the PHF8 histone H3K9me1/2 demethylase**, activating expression of neurodevelopmental genes (including **KDM5C**, itself an X-linked intellectual disability gene).
- **Cellular process:** Loss of ZNF711 disrupts this **chromatin-modification/transcriptional-activation cascade**, impairing normal neuronal gene-expression programs during brain development — GO:0006338 (chromatin remodeling), GO:0034720 (histone H3-K4 demethylation-adjacent regulatory network), GO:0007399 (nervous system development).
- **Clinical correlate:** mild-to-moderate intellectual disability, speech delay, and autism-spectrum features (co-occurring in roughly half of reported isolated-ZNF711 cases per literature), consistent with a transcriptional/epigenetic-regulatory rather than a structural neurodevelopmental lesion.

**(D) Obesity arm:** No specific molecular pathway within the deleted interval has been mechanistically linked to obesity in the literature reviewed; it is treated in the literature as a co-occurring syndromic feature of unclear direct genetic driver — possibly reflecting a yet-uncharacterized gene in the deleted interval, secondary hypothalamic/endocrine dysregulation in patients with larger deletions extending to hypothalamic-pituitary–relevant loci, or a co-occurring endocrinopathy (ACTH deficiency/hypopituitarism reported in some larger-deletion cases) rather than an independent monogenic contributor. This is an explicit knowledge gap.

**Integrative causal-chain summary (per system):**
1. Xq21.1-q21.2 hemizygous deletion (upstream trigger, present from conception/germline)
2. → parallel, independent loss-of-function for CHM, POU3F4, ZNF711 (± CYLC1/RPS6KA6/HDX/APOOL/SATL1/POF1B in larger deletions)
3. → three parallel downstream cascades: (i) REP1 deficiency → Rab under-prenylation → RPE/photoreceptor trafficking failure → progressive chorioretinal degeneration; (ii) POU3F4 deficiency → otic mesenchyme/cochlear patterning failure → IP3 malformation + stapes fixation → congenital mixed hearing loss; (iii) ZNF711 deficiency → impaired PHF8-mediated transcriptional activation of neurodevelopmental genes → intellectual disability/developmental delay
4. → composite multisystem clinical phenotype (the triad), with obesity as an incompletely explained co-occurring feature, and additional variable features (endocrine, seizures, renal, ataxia) in larger deletions.

Sources: [Choroideremia molecular mechanisms review, ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1471491422000521) | [REP1 loss-of-function, PMC2793004](https://pmc.ncbi.nlm.nih.gov/articles/PMC2793004/) | [REP1 systemic lipid/oxidative stress, PMC8262314](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8262314/) | [POU3F4 review, PMC10296620](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10296620/) | [POU3F4/SLC6A20, Frontiers 2022](https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2022.999833/full) | [ZNF711 function, GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=ZNF711) | [ZNF711 methylation signature, EJHG](https://www.nature.com/articles/s41431-021-01018-1)

---

### 7. Anatomical Structures Affected

**Organ level:**
- Primary: **Eye** (retina/choroid — UBERON:0000966/UBERON:0001782), **Inner ear** (cochlea/vestibular apparatus — UBERON:0001846), **Middle ear** (stapes — UBERON:0001685), **Brain** (neurodevelopment/intellectual disability — UBERON:0000955), **Adipose tissue** (obesity — UBERON:0001013)
- Secondary: **Pituitary/hypothalamic axis** (ACTH deficiency/hypopituitarism in some cases — UBERON:0000007), **Kidney/renal vasculature** (renal artery stenosis in some cases — UBERON:0002113/UBERON:0002015), **Ovary** (primary ovarian failure in one reported translocation case — UBERON:0000992)
- Body systems: ophthalmologic, auditory/vestibular, central nervous system, endocrine/metabolic, and (variably) renal/cardiovascular systems.

**Tissue and cell level:**
- Retinal pigment epithelium (CL:0002586), photoreceptor cells — rod (CL:0000604) and cone (CL:0000573), choriocapillaris endothelial cells (CL:0002138)
- Cochlear hair cells (CL:0000601), spiral ganglion neurons (CL:0000101-adjacent), stria vascularis marginal cells, spiral ligament fibrocytes, otic mesenchyme-derived cells
- Neurons of the developing cerebral cortex (affected by ZNF711-mediated transcriptional dysregulation)
- Adipocytes (CL:0000136)

**Subcellular level:**
- Prenylation/vesicular trafficking machinery (Golgi, endosomal/exocytic vesicles) in RPE/photoreceptor cells — GO Cellular Component: Golgi apparatus (GO:0005794), cytoplasmic vesicle (GO:0031410)
- Nuclear chromatin (histone-modification complex including PHF8) in neurons affected by ZNF711 loss — GO:0000785 (chromatin)

**Localization:** Bilateral and symmetric involvement is typical for both the retinal (choroideremia) and auditory (DFNX2) components, consistent with the germline/constitutional (not somatic/mosaic) nature of the deletion in affected males.

---

### 8. Temporal Development

- **Onset:** Congenital/early-childhood for hearing loss (present from birth) and intellectual disability/developmental delay; childhood-to-adolescent onset of night blindness (choroideremia), with childhood onset of obesity also reported. Overall the syndrome is a **pediatric/congenital-onset multisystem disorder**.
- **Onset pattern:** Insidious for the ophthalmologic component; congenital/immediate for the audiologic component.
- **Progression:** The retinal component is **progressive** over decades (peripheral field constriction progressing centripetally to eventual central blindness by mid-adulthood, mirroring isolated choroideremia's typical course). The conductive hearing component (stapes fixation) is structurally **stable**, while the sensorineural component can be **progressive**. Intellectual disability/developmental delay is typically **stable** once present (a static encephalopathy-like course) rather than degenerative.
- **Disease course pattern:** Chronic, lifelong, progressive (for vision) with stable-to-progressive (for hearing) and static (for cognitive) components running in parallel — not episodic or relapsing-remitting.
- **Critical periods:** Cochlear implantation and stapes surgery carry elevated procedural risk (CSF gusher, meningitis risk) specifically because of the IP3 malformation — an important clinical "critical window" consideration for auditory intervention timing and surgical planning. Early ophthalmologic surveillance is important before symptomatic visual field loss becomes severe, given availability of investigational CHM gene therapy (see Treatment).
- **Remission:** Not applicable — no spontaneous or treatment-induced remission is described; this is a structural/developmental and progressive-degenerative condition, not typified by remission-relapse cycles.

Sources: [Xq21 deletion literature review, PMC11202778](https://pmc.ncbi.nlm.nih.gov/articles/PMC11202778/)

---

### 9. Inheritance and Population

**Epidemiology:** Extremely rare; **fewer than 30 probands from ~14-15 unrelated families reported worldwide** in the literature as of the most recent comprehensive review (2024, PMC11202778) — consistent with Orphanet's convention of classifying such conditions as prevalence "unknown" or "<1 / 1,000,000." By contrast, **isolated (non-syndromic) choroideremia** alone has an estimated prevalence of **~1 in 50,000–1 in 100,000** individuals worldwide (with Northern Finland reporting the highest documented prevalence, and an estimated >500 affected males in the UK and ~3,000 across Europe) — the contiguous-deletion syndrome discussed here is a much rarer subset of that broader choroideremia population.

**Inheritance pattern:** X-linked recessive. Manifests fully in hemizygous males.

**Origin of deletion:** Per the 2024 literature review, "all deletions except one de novo case were maternally inherited" — the great majority of reported cases trace to a carrier mother, with a minority arising de novo.

**Penetrance/expressivity:** Full penetrance in hemizygous males for the core triad; **variable expressivity** for the additional features (endocrine, seizure, renal, ataxia) correlating with deletion size/extent.

**Carrier females:** Generally **asymptomatic** for hearing and cognition, but Orphanet/case literature notes carrier females can show "typical retinal changes indicative of the choroideremia carrier state" (mosaic RPE stippling due to X-inactivation mosaicism) — the classic choroideremia-carrier fundus phenotype. Rare females with **skewed X-inactivation or structural X rearrangement** (e.g., the balanced X;4 translocation case, PMID:11035551) can manifest a partial or full phenotype including mild sensorineural hearing loss, inner ear malformation, developmental delay, and — uniquely in that reported case — primary ovarian failure.

**Founder effects/consanguinity/germline mosaicism/genetic anticipation:** Not specifically documented for this contiguous deletion syndrome; these concepts are less applicable to a structural CNV disorder than to a repeat-expansion or point-mutation disease. No specific founder population or geographic clustering has been reported (cases are described across "different ancestries," per PMC11202778).

**Sex ratio:** Overwhelmingly male-affected given X-linked recessive inheritance and hemizygosity (28 of 29 reported probands male per the 2024 review); the rare affected female cases involve X-autosome translocations or possibly skewed X-inactivation.

**Age distribution:** Diagnosed from infancy (via congenital hearing loss, often the presenting feature — increasingly picked up via newborn hearing screening and multi-gene NGS panels) through later childhood/adolescence (as visual symptoms and developmental delay become apparent) and followed lifelong given the progressive ophthalmologic course.

Sources: [Xq21 deletion literature review, PMC11202778](https://pmc.ncbi.nlm.nih.gov/articles/PMC11202778/) | [Choroideremia epidemiology, EyeWiki](https://eyewiki.org/Choroideremia) | [Balanced X;4 translocation, PMID 11035551](https://pubmed.ncbi.nlm.nih.gov/11035551/)

---

### 10. Diagnostics

**Clinical tests:**
- **Ophthalmologic:** Dilated fundus examination (peripheral chorioretinal atrophy), electroretinography (ERG — progressively reduced/extinguished responses), fundus autofluorescence, OCT (for RPE/photoreceptor structural loss), visual field testing (Goldmann perimetry for progressive constriction), dark adaptometry.
- **Audiologic/otologic:** Newborn hearing screening (often the presenting abnormality), audiometry (documenting mixed conductive-sensorineural pattern), **temporal bone CT/MRI** — the key imaging modality, revealing the pathognomonic **incomplete partition type III (IP3)**, absent/deficient modiolus, and bulbous dilation of the internal auditory canal.
- **Neurodevelopmental:** Standardized developmental/cognitive assessment; brain MRI to exclude structural CNS anomalies.
- **Endocrine (as indicated by phenotype):** ACTH/cortisol axis testing, thyroid function tests when hypopituitarism is suspected.
- **Renal/cardiovascular (as indicated):** Renal artery imaging/blood pressure monitoring when hypertension present.

**Genetic testing:**
- **Chromosomal microarray (array CGH or SNP array)** — the primary confirmatory test, delineating deletion size/breakpoints (as used in the PMC5471966 8.05 Mb case and others).
- **NGS multi-gene hearing-loss panels** — increasingly the entry point for diagnosis, per PMC11202778: "Our patient is the first example of Xq21 deletion identified through a multi-gene NGS panel after neonatal diagnosis of an apparently isolated HL," reflecting current practice of using syndromic hearing-loss gene panels for infants with sensorineural/mixed deafness.
- **MLPA (multiplex ligation-dependent probe amplification)** — used for locus-specific dosage confirmation of CHM/POU3F4/ZNF711.
- **Karyotype/FISH** — relevant when a balanced translocation is suspected (as in the PMID:11035551 case, using whole-chromosome-X paint and locus-specific probes D4S96/D4F26).
- Single-gene CHM sequencing/deletion analysis is used when isolated choroideremia (not the syndromic form) is suspected; single-gene POU3F4 testing for isolated DFNX2.

**Clinical criteria / differential diagnosis:** No formal consensus diagnostic-criteria statement (e.g., DSM/ICD operational criteria) exists for this ultra-rare condition; diagnosis rests on the clinical triad (choroideremia + congenital mixed deafness with IP3 malformation + obesity, ± intellectual disability) confirmed by molecular/cytogenetic demonstration of the Xq21 deletion. Differential diagnosis includes: isolated choroideremia (no deafness/obesity), isolated DFNX2/DFN3 deafness (no visual/obesity findings), other syndromic obesity conditions with sensory impairment (e.g., Bardet-Biedl syndrome — but that is autosomal/multi-organelle ciliopathy, distinguishable by inheritance pattern and by absence of the IP3 cochlear malformation and choroideremia-specific fundus findings), and other X-linked contiguous gene deletion syndromes in the Xq13-q26 region.

**Screening:** No population-based newborn screening specific to this syndrome exists; however, **universal newborn hearing screening** is the practical entry point that leads to eventual syndromic diagnosis in many reported cases (per PMC11202778's emphasis that "approximately 20% of children presenting with HL as the only initial clinical feature will subsequently be diagnosed with syndromic HL"). Cascade/carrier genetic testing and prenatal diagnosis are offered to at-risk maternal relatives once a familial deletion is characterized, alongside genetic counseling regarding the 50% transmission risk from a carrier mother to each pregnancy.

Sources: [Xq21 deletion literature review, PMC11202778](https://pmc.ncbi.nlm.nih.gov/articles/PMC11202778/) | [8.05 Mb Xq21 deletion case, PMC5471966](https://pmc.ncbi.nlm.nih.gov/articles/PMC5471966/)

---

### 11. Outcome/Prognosis

- **Survival/mortality:** No disease-specific mortality/survival data are reported in the literature; this is not generally considered a life-limiting condition per se, though comorbid endocrine abnormalities (ACTH deficiency/adrenal insufficiency) in larger-deletion cases could carry mortality risk if unrecognized/untreated, and renal artery stenosis-associated hypertension carries standard cardiovascular risk if uncontrolled.
- **Morbidity/function:** Substantial lifelong morbidity from the combination of progressive vision loss, congenital hearing impairment, and intellectual disability — a dual-sensory-impairment-plus-cognitive-disability profile with major functional/educational/vocational impact. Obesity adds cardiometabolic risk.
- **Disease course:** Chronic and progressive for the visual component; largely static for the auditory (structural) and cognitive components, though sensorineural hearing can progressively worsen.
- **Complications:** Surgical complications specific to the IP3 malformation (perilymphatic gusher, CSF leak, risk of meningitis during stapedectomy or cochlear implantation — explicitly flagged in PMC11202778); secondary complications from any co-occurring endocrinopathy, seizures, or hypertension/renal artery stenosis in larger-deletion cases.
- **Recovery potential:** No spontaneous recovery is described for the core progressive-degenerative components; targeted intervention (cochlear implantation for hearing, investigational gene therapy for the CHM component — see Treatment) can meaningfully alter functional trajectory but does not reverse underlying genetic loss.
- **Prognostic factors:** Deletion size/extent is the principal prognostic modifier — larger deletions correlate with a broader, more severe multisystem phenotype (endocrine, seizure, renal, ataxia features) beyond the core triad.

Sources: [Xq21 deletion literature review, PMC11202778](https://pmc.ncbi.nlm.nih.gov/articles/PMC11202778/)

---

### 12. Treatment

**Pharmacotherapy:** No disease-specific pharmacotherapy exists for the syndrome as a whole; management is organ-system-directed and supportive (e.g., hormone replacement if ACTH deficiency/hypopituitarism is present; antihypertensive therapy if renal artery stenosis-related hypertension is present; anticonvulsants if seizures occur). NCIT: **NCIT:C15986** (Pharmacotherapy) as the generic action term for these supportive interventions.

**Advanced therapeutics (choroideremia-specific gene therapy — relevant to the CHM component):**
- **AAV2-mediated CHM gene augmentation** ("timrepigene emparvovec," also referred to by trial sponsor code BIIB111) has undergone Phase I/II and Phase III clinical trials (e.g., **NCT02553135**, and the original Oxford first-in-human trial NCT01461213) for isolated choroideremia, delivered via **subretinal injection**. Phase III results: "a higher percentage of individuals in both the high-dose (83%) and low-dose (71%) groups maintained at least one line of ETDRS acuity compared to the unoperated control group (68%)." Intraretinal inflammation has been observed as a safety consideration, stabilizing by 2 years but with some permanent retinal structural change reported.
- **Non-viral episomal CHM gene augmentation** vectors are in earlier-stage (preclinical) development (PMC10607001) as an alternative to AAV delivery.
- **Antisense oligonucleotide approaches** have also been explored as an alternate strategy in choroideremia (per the 5-year AAV2-REP1 follow-up literature).
- NCIT: **NCIT:C15238** (Gene Therapy); therapeutic_modality: `GENE_THERAPY`.
- **Important scope caveat for dismech curation:** these trials enroll patients with **isolated (non-syndromic) choroideremia**, not specifically the contiguous-deletion syndrome; applicability to Xq21-deletion-syndrome patients (who lack functional CHM by deletion rather than point mutation, but gene augmentation should in principle still be applicable if enough retina remains and no confounding immune issues) is not separately documented in the literature reviewed and should be flagged as inferred/extrapolated rather than direct trial evidence.

**Surgical/interventional (deafness component):**
- **Cochlear implantation** for severe-to-profound sensorineural hearing loss — technically complicated by the IP3 malformation (absent modiolus, risk of gusher/CSF leak, electrode misplacement risk); requires specialized surgical planning per PMC11202778.
- **Stapedectomy/stapes surgery** for the conductive (stapes fixation) component carries elevated perilymphatic gusher risk given the underlying POU3F4-related inner ear malformation — historically a diagnostic clue to DFN3 when unexpectedly encountered.
- NCIT: **NCIT:C15329** (Surgical Procedure); therapeutic_modality: `DEVICE` (cochlear implant) / `SURGERY` (stapedectomy).

**Supportive/rehabilitative:**
- Hearing habilitation (hearing aids where appropriate, cochlear implantation, sign language/communication support)
- Low-vision rehabilitation and orientation/mobility training as visual field constricts
- Speech-language therapy, occupational therapy, and individualized educational support for developmental delay/intellectual disability
- Weight management/dietary counseling and monitoring for obesity-related cardiometabolic risk (NCIT:C15447, Dietary Intervention; NCIT:C15302, Physical Therapy where applicable)
- Multidisciplinary follow-up: ophthalmology (retina), otolaryngology, clinical genetics, endocrinology, and pediatrics, as GARD explicitly recommends.

**Experimental:** Choroideremia AAV2-REP1 gene therapy trials as above (NCT02553135 and related; note these target isolated choroideremia). No condition-specific (Xq21-deletion-syndrome) interventional trials were identified.

**Genetic counseling:** Recommended for families, given the 50% transmission risk from carrier mothers to offspring and possibility of de novo occurrence; NCIT:C15240 (Genetic Counseling).

Sources: [Update on CHM gene therapy trials, PMC7826687](https://pmc.ncbi.nlm.nih.gov/articles/PMC7826687/) | [Two-year AAV2-REP1 results, ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0002939418302903) | [Non-viral episomal CHM vectors, PMC10607001](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10607001/) | [Gene therapy for choroideremia review 2025](https://www.tandfonline.com/doi/full/10.1080/14712598.2025.2459850) | [Xq21 deletion literature review, PMC11202778](https://pmc.ncbi.nlm.nih.gov/articles/PMC11202778/) | [GARD](https://rarediseases.info.nih.gov/diseases/369/choroideremia-deafness-obesity-syndrome)

---

### 13. Prevention

- **Primary prevention:** Not applicable in the conventional sense (no modifiable environmental risk factor); the relevant "primary prevention" tool is **reproductive genetic counseling and prenatal/preimplantation genetic diagnosis** for families with a known familial Xq21 deletion, allowing informed reproductive decision-making. ACMG/ACOG-style carrier and prenatal testing frameworks apply once the familial deletion is molecularly characterized.
- **Secondary prevention/early detection:** **Universal newborn hearing screening** functions as the practical early-detection mechanism, frequently the first clinical clue (per PMC11202778), triggering downstream syndromic evaluation (multi-gene NGS panel → microarray) before the ophthalmologic and developmental features become apparent — enabling earlier surveillance and intervention planning.
- **Tertiary prevention:** Structured multidisciplinary surveillance to catch and manage complications: regular ophthalmologic monitoring (to time potential future CHM gene therapy intervention while retina is preserved), audiologic monitoring for sensorineural progression, endocrine screening in larger-deletion patients (ACTH axis), blood pressure/renal imaging surveillance where indicated, and proactive surgical planning (imaging before any stapes/cochlear implant surgery to anticipate gusher risk and avoid CSF leak/meningitis complications).
- **Screening/risk stratification:** Cascade testing of maternal relatives once a proband's deletion is characterized (identifying carrier females, who then receive counseling about the choroideremia-carrier fundus phenotype and reproductive risk).
- **Immunization/public health/behavioral/prophylaxis:** Not applicable — no infectious, vaccine-preventable, or population-level public-health dimension to this condition.

Sources: [Xq21 deletion literature review, PMC11202778](https://pmc.ncbi.nlm.nih.gov/articles/PMC11202778/) | [GARD](https://rarediseases.info.nih.gov/diseases/369/choroideremia-deafness-obesity-syndrome)

---

### 14. Other Species / Natural Disease

No naturally occurring animal disease directly recapitulating the full **contiguous** Xq21 deletion syndrome (choroideremia + deafness + obesity) was identified in the literature searched — this is expected, since a multi-gene contiguous deletion of this specific human genomic interval is not a naturally recurring lesion in other species' genomes. However, the **component single-gene diseases** have documented naturally-occurring and engineered animal correlates:
- **Choroideremia:** A naturally occurring **CHM-mutant dog model** (choroideremia-like retinal degeneration has been documented in certain canine lines; OMIA maintains entries for canine chorioretinal degeneration) has been used comparatively, though the flagship animal models are engineered (see Model Organisms below) rather than naturally occurring in a companion-animal population widely reported.
- No naturally occurring POU3F4-deficient or ZNF711-deficient animal disease was identified in this search.
- **NCBI Taxon:** Homo sapiens (NCBITaxon:9606) is the only species in which this specific syndrome (the contiguous deletion) is documented.

This section should be flagged as largely **not applicable / no data identified** for the syndromic (contiguous-deletion) entity specifically, while noting that each component gene has cross-species orthologs (CHM, Pou3f4, Znf711 orthologs are conserved in mouse and other mammals) used in engineered models (see below).

---

### 15. Model Organisms

**Choroideremia (CHM) component:**
- **Mouse models:** Conditional/tissue-specific *Chm* knockout mice (RPE-specific Cre-conditional ablation) recapitulate age-related RPE degeneration — PMC3584022, "Conditional Ablation of the Choroideremia Gene Causes Age-Related Changes in Mouse Retinal Pigment Epithelium." A recent mouse model study describes CHM deficiency disrupting "photoreceptor viability and synaptic integrity" (PMC12749510). These models are used to study RPE/photoreceptor degeneration mechanisms and to validate AAV2-REP1 gene augmentation vectors preclinically.
- **Cell-based models:** Patient-derived fibroblasts and monocytes/lymphoblasts have been used to demonstrate REP1 loss-of-function effects on intracellular (Rab-dependent) transport (PMC2793004, PLOS One).
- **Applications:** These models support study of the retina-restricted phenotype (REP2 compensation elsewhere), evaluation of prenylation biomarkers (in vitro Rab6A prenylation assays used to measure AAV vector potency, PMC5918179), and preclinical gene-therapy vector testing.
- **Limitations:** Standard germline *Chm*-null mice are embryonic lethal (given REP1's essential role), necessitating conditional/tissue-restricted knockout strategies — an important model limitation to note; global knock-in/humanized models capturing the full multi-gene deletion do not exist.

**Deafness (POU3F4) component:**
- ***Pou3f4*-null and hypomorphic mouse models** are well established (referenced across the POU3F4/DFN3 literature, e.g., PMC10296620 review) and recapitulate the human inner-ear malformation phenotype (otic capsule mesenchyme/spiral ligament/stria vascularis abnormalities), supporting their use as the standard model for DFNX2 mechanism studies. (Specific PMIDs for individual *Pou3f4* mouse studies were not individually re-verified in this pass and should be confirmed against MGI before formal curation.)

**Intellectual disability (ZNF711) component:**
- No dedicated *Znf711* animal knockout model specific to the neurodevelopmental phenotype was surfaced in this search; functional characterization to date is largely from human genetics (pedigree) and in vitro (PHF8-recruitment, methylation-signature) studies (Sciencedirect 2016 pedigree paper; EJHG 2021 methylation-signature paper; PMC11767995 EEG/epilepsy case series).

**Resources:** MGI (Mouse Genome Informatics) for *Chm*/*Pou3f4*/*Znf711* orthologs and existing allele records; IMPC/KOMP for systematic knockout phenotyping data, should a curator wish to verify current allele availability.

No model recapitulating the **combined triad** (i.e., an engineered contiguous-deletion mouse spanning the *Chm-Pou3f4-Znf711* syntenic mouse region) was identified — this is a notable gap/knowledge-gap candidate for a dismech `HUMAN_MODEL_MISMATCH`/`KNOWLEDGE_GAP` discussion node, since all mechanistic inference about the combined syndrome currently rests on human case reports plus single-gene animal models studied in isolation, not a model that reproduces the syndromic gene-dosage combination itself.

Sources: [Conditional Chm ablation mouse model, PMC3584022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3584022/) | [Chm deficiency photoreceptor/synaptic model, PMC12749510](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12749510/) | [REP1 patient-cell functional model, PMC2793004](https://pmc.ncbi.nlm.nih.gov/articles/PMC2793004/) | [AAV vector potency/Rab6A prenylation assay, PMC5918179](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5918179/) | [POU3F4 clinical/molecular review, PMC10296620](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10296620/)

---

## Curation Notes for dismech Entry Construction

1. **NEC (Named Entity Confusion) preflight already partially addressed:** the disease resolves unambiguously to MONDO:0010558 / OMIM:303110 / ORPHA:1435, distinct from isolated choroideremia (MONDO term for CHM-only disease) and from isolated DFNX2 (OMIM 304400) — a curator should still run the standard MONDO `obo` preflight check per CLAUDE.md before finalizing gene/OMIM/synonym anchors.
2. **Architecture recommendation:** This disease is a strong candidate for modeling as **three parallel pathophysiology chains converging on a shared upstream trigger node** ("Hemizygous Xq21.1-q21.2 Deletion") with three downstream branches (CHM/REP1→choroideremia; POU3F4→DFNX2 deafness; ZNF711→intellectual disability), each of which could `conforms_to` relevant existing dismech modules if applicable (none of the current cataloged modules map cleanly onto Rab-prenylation/RPE degeneration, POU-domain otic patterning, or PHF8-recruitment transcriptional regulation — this may be a case where no existing module applies and fully bespoke pathophysiology nodes are appropriate).
3. **Evidence sourcing caveat:** Because this is an ultra-rare, case-report-driven condition, curators should expect thin PMID coverage per claim and should be especially careful to distinguish snippets sourced from the syndromic (Xq21 deletion) literature versus the much larger isolated-choroideremia or isolated-DFNX2 literature bodies — many mechanism-level claims (REP1/Rab prenylation, POU3F4/otic patterning, ZNF711/PHF8) are necessarily drawn from single-gene-disease literature, not syndrome-specific studies, and should be evidence_source/explanation-annotated accordingly.
4. **Original description PMID:7258279 has no indexed abstract** ("No abstract available" on PubMed) — any snippet sourced from this paper for dismech evidence must come from a full-text/cached source, not a PubMed abstract quote, or should be substituted with a later paper (e.g., Merry et al. 1989, or PMC11202778/PMC5471966) that does carry a quotable abstract/body text.