---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-03T14:30:43.734129'
end_time: '2026-09-03T14:35:18.546348'
duration_seconds: 274.81
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Byssinosis
  mondo_id: ''
  category: Environmental Lung Disease
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
  num_turns: 26
  total_cost_usd: 1.3788212000000002
  session_id: 28fb039f-05ba-5c97-94bf-1bbc91c07abc
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 31
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Byssinosis
- **MONDO ID:**  (if available)
- **Category:** Environmental Lung Disease

## Research Objectives

Please provide a comprehensive research report on **Byssinosis** covering all of the
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

I now have comprehensive, well-sourced material. Compiling the final report.

# Byssinosis: Comprehensive Research Report

## 1. Disease Information

### Overview

Byssinosis is an occupational obstructive airways disease caused by inhalation of dust generated during the processing of raw, non-synthetic textile fibers — principally cotton, but also flax, hemp, jute, and sisal — in inadequately ventilated textile mills. It is classically described as "a collection of respiratory symptoms elicited by exposure to raw nonsynthetic textiles during their manufacturing process" and combines features of both asthma and chronic bronchitis, with a hallmark work-related, cyclical symptom pattern ("Monday fever") ([StatPearls, NCBI Bookshelf NBK519549](https://www.ncbi.nlm.nih.gov/books/NBK519549/); [CDC NIOSH Science Bulletin 2021](https://www.cdc.gov/niosh/bulletin/2021/textiles.html)).

### Key Identifiers

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0006688 |
| ICD-10-CM | J66.0 (Byssinosis) |
| ICD-9-CM | 504 |
| MeSH | Byssinosis (synonyms: Byssinoses, Brown Lung, Brown Lung Disease/Diseases) |

Orphanet and OMIM do not carry dedicated entries for byssinosis; it is classified primarily as an ICD/MeSH-coded occupational lung disease rather than a rare/genetic disease-registry entity, and Mondo cross-references it against ICD-10-CM/MeSH rather than OMIM ([Monarch Initiative MONDO:0006688](https://monarchinitiative.org/MONDO:0006688); [icd10data.com](https://www.icd10data.com/ICD10CM/Codes/J00-J99/J60-J70/J66-/J66.0)).

### Synonyms

Cotton worker's lung, brown lung disease, "Monday fever"/"Monday chest tightness," and (historically, though now recognized as related but distinct entities caused by contaminated fiber batches rather than the chronic cotton-dust process) mill fever, mattress-maker's fever, and weaver's cough ([StatPearls NBK519549](https://www.ncbi.nlm.nih.gov/books/NBK519549/); [en-academic.com](https://medicine.en-academic.com/14700/byssinosis)).

### Data Source Character

Byssinosis knowledge derives almost entirely from **aggregated occupational-cohort and cross-sectional survey data** — large mill-worker cohorts (e.g., the Shanghai Textile Worker Cohort, n=447–570+ workers followed 1981–2006; the Karachi MultiTex trial, n=2,031 workers) — rather than individual EHR-based case ascertainment, reflecting its nature as an exposure-defined occupational syndrome diagnosed by symptom questionnaire and spirometry rather than a single confirmatory laboratory test ([PMID: 20797932](https://pmc.ncbi.nlm.nih.gov/articles/PMC2974703/); [PMID: 36717255](https://pmc.ncbi.nlm.nih.gov/articles/PMC9985716/)).

---

## 2. Etiology

### Primary Causal Factors

Byssinosis is fundamentally an **environmental/occupational** disease, not a primary genetic disorder. The causal exposure is inhalation of airborne particulates generated in the earliest ("opening," carding, blowing) processing stages of raw cotton, flax, or hemp — the stages with the highest bract and trash content, and correspondingly the highest bacterial contamination ([StatPearls NBK519549](https://www.ncbi.nlm.nih.gov/books/NBK519549/)).

The leading causal agent within cotton dust is **bacterial endotoxin** — lipopolysaccharide (LPS) shed from the outer membrane of Gram-negative bacteria colonizing raw cotton fiber during growth, harvest, and storage. Quantitative assays (Limulus amebocyte lysate) established in the 1980s–1990s identified endotoxin, rather than the cellulose/cotton particulate itself, as the principal biologically active component: guinea pigs exposed to breathable cotton dust show a full respiratory response, whereas exposure to pristine cellulose powder of identical particle-size distribution produces none ([ScienceDirect — animal model](https://www.sciencedirect.com/science/article/abs/pii/0041008X84901522); StatPearls). Other candidate bioactive components historically implicated include cotton bract tannins, residual pesticides, fungal contaminants, and complement- or histamine-releasing extracts, though endotoxin has the strongest and most reproducible dose-response evidence.

### Risk Factors

**Environmental / Occupational:**
- Duration and intensity of cotton (or flax/jute/hemp) dust exposure — the single strongest predictor of both symptoms and spirometric decline in the 2023 MultiTex Karachi study (n=2,031) ([PMID: 36717255](https://pmc.ncbi.nlm.nih.gov/articles/PMC9985716/))
- Job/processing stage: prevalence is consistently highest among **carders** (opening/carding room workers), with spinners, weavers, and winders also affected but at lower rates ([WebSearch epidemiology summary](https://pubmed.ncbi.nlm.nih.gov/4689794/))
- Airborne endotoxin concentration — correlates strongly with byssinosis prevalence (r ≈ 0.72 across 26 studies/12 countries in the low- and middle-income country systematic review) ([PMID: 35073782](https://pubmed.ncbi.nlm.nih.gov/35073782/))
- Cigarette smoking (≥3.5 pack-years) — an important independent and additive risk factor for both symptoms and lung-function decline ([PMID: 36717255](https://pmc.ncbi.nlm.nih.gov/articles/PMC9985716/))
- Inadequate ventilation / dust-control infrastructure

**Genetic risk factors:**
- **TNF gene promoter polymorphism (rs1800629, TNF-308G/A)** and **LTA (lymphotoxin-alpha) polymorphism rs909253** modify the association between endotoxin exposure and longitudinal FEV₁ decline in a 20-year prospective cohort of Shanghai cotton textile workers (Zhang H, Hang J, Wang X, et al., *Occup Environ Med* 2007;64:409–413) — workers carrying susceptibility genotypes showed accelerated FEV₁ loss per unit endotoxin exposure ([search summary, PMID association](https://pmc.ncbi.nlm.nih.gov/articles/PMC2974703/))
- **Microsomal epoxide hydrolase (mEH/EPHX1) polymorphisms** interact with endotoxin exposure to influence lung-function decline in cotton workers (*Am J Respir Crit Care Med* 2005;171:165) ([academic.oup.com/ajrccm](https://academic.oup.com/ajrccm/article-abstract/171/2/165/8538324))
- A gene-centric GWAS-style association study identified additional candidate loci modifying lung-function trajectory in newly-hired female cotton textile workers under endotoxin exposure (PLOS ONE 2013) ([journals.plos.org/plosone/article?id=10.1371/journal.pone.0059035](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0059035); [PMID: 23527081](https://pubmed.ncbi.nlm.nih.gov/23527081/))
- CD14 (−159/−260) and TLR4 (Asp299Gly, Thr399Ile) polymorphisms, well established as modifiers of endotoxin-driven airway inflammation in organic-dust disease generally, are strong biological candidates for byssinosis susceptibility given the shared LPS-TLR4/CD14 signaling pathway, though byssinosis-specific replication studies are sparser than for the TNF/LTA and mEH findings above ([PMID 16142747](https://pubmed.ncbi.nlm.nih.gov/16142747/); [JACI TLR4 paper](https://www.jacionline.org/article/S0091-6749(03)01619-1/fulltext))

**No specific genetic protective factors** have been well characterized in the literature; general anti-inflammatory or endotoxin-hyporesponsive TLR4/CD14 genotype variants that reduce risk in other organic-dust diseases (e.g., farm/asthma endotoxin studies) are biologically plausible but not confirmed specifically for byssinosis.

### Gene-Environment Interaction

The clearest documented gene-environment interaction is the **TNF/LTA genotype × cumulative endotoxin exposure** interaction driving accelerated annual FEV₁ decline (Zhang et al. 2007) — this is the paradigm case for byssinosis GxE and the strongest evidence that individual genetic variation in innate-immune/inflammatory signaling modifies susceptibility to a fixed environmental (endotoxin) dose.

---

## 3. Phenotypes

### The "Monday Fever" Phenotype (Signature Clinical Pattern)

Byssinosis's defining phenotype is symptom periodicity tied to the work week: chest tightness, cough, wheeze, and dyspnea recur maximally on the **first day back after a period away from exposure (classically Monday)**, attenuate over the remaining work week ("tolerance"), and return with full intensity after the next exposure-free interval. This pattern is the opposite of classic occupational asthma, in which symptoms typically worsen toward the end of the work week ([StatPearls; overview search](https://www.ncbi.nlm.nih.gov/books/NBK519549/)).

### Phenotype Inventory

| Category | Phenotype | Suggested HPO term |
|---|---|---|
| Symptom | Chest tightness (work-related, Monday-predominant) | HP:0033987 (Chest tightness) / general use HP:0025267 (or free text if no exact match) |
| Symptom | Cough | HP:0012735 (Cough) |
| Symptom | Wheezing | HP:0030828 (Wheezing) |
| Symptom | Dyspnea / breathlessness | HP:0002094 (Dyspnea) |
| Symptom | Sputum production (chronic phase) | HP:0031245 (Increased sputum production) or similar |
| Sign | Fine basilar rales/crackles (minority of patients) | HP:0030830 (Crackles) |
| Sign | Airflow obstruction on auscultation/exam | — |
| Lab abnormality | Acute leukocytosis after exposure | HP:0001974 (Leukocytosis) |
| Lab/physiologic | Cross-shift (intra-shift) FEV₁ decline >5–10% | — (functional/laboratory finding) |
| Lab/physiologic | Longitudinal FEV₁ decline / FEV₁ <80% predicted | HP:0002812 (or general "Reduced FEV1") |
| Imaging | Chest radiograph: hyperlucency, diaphragmatic flattening, emphysema; diffuse lower-lung haziness in advanced disease | — |
| Imaging | HRCT: basal-predominant ground-glass opacities with centrilobular nodules | — |

### Phenotype Characteristics

- **Age of onset:** Adult-onset, occupationally determined — onset depends on duration/intensity of textile-mill employment rather than a fixed age; symptoms can begin within months of hire in high-exposure jobs (e.g., carding) and typically progress over years of continued exposure.
- **Severity/progression — the Schilling grading system:** Developed by Richard Schilling in the 1960s, the classic clinical grading is:
  - **Grade 0** — no symptoms of chest tightness/breathlessness on Mondays
  - **Grade ½** — occasional mild chest tightness or respiratory irritation on Mondays
  - **Grade 1** — chest tightness and/or breathlessness on Mondays only
  - **Grade 2** — chest tightness and/or breathlessness on Mondays **and** other days
  - **Grade 3** (used in some schemes) — permanent disability with evidence of persistent lung-function impairment, symptoms no longer confined to Mondays

  ([Search summary based on Schilling grading literature](https://pmc.ncbi.nlm.nih.gov/articles/PMC1039177/?page=5); [ScienceDirect overview](https://www.sciencedirect.com/topics/medicine-and-dentistry/byssinosis))

  A parallel **WHO symptoms-based criterion** (work-related chest tightness on questionnaire) is also used in modern epidemiological surveys, sometimes yielding different prevalence estimates than Schilling's criteria in the same population (e.g., 3% by WHO criteria vs 4% by Schilling's criteria in the 2023 Karachi MultiTex baseline survey) ([PMID: 36717255](https://pmc.ncbi.nlm.nih.gov/articles/PMC9985716/)).

- **Progression:** With continued exposure, the episodic acute/Monday pattern evolves into a **chronic, non-cyclical state** resembling chronic bronchitis, with persistent cough, sputum, and progressive irreversible airflow obstruction; early removal from exposure can allow partial FEV₁ recovery, but established chronic disease/fibrosis is largely irreversible ([StatPearls NBK519549](https://www.ncbi.nlm.nih.gov/books/NBK519549/)).
- **Frequency among affected individuals:** Highly exposure- and criteria-dependent. Reported prevalence in cotton-processing workers ranges from ~3–4% (modern low-dust UK/Pakistan mills using strict criteria) up to 14–36% (older or higher-exposure South Asian mill cohorts), with a 2024 pooled meta-analysis of Indian textile workers finding **24% pooled prevalence** (95% CI 13–36%; 18 studies, 5,678 workers) — dropping to 20% in low-risk-of-bias studies ([Journal of Association of Pulmonologists of Tamil Nadu, 2024](https://journals.lww.com/jatn/fulltext/2024/07010/pooled_prevalence_of_byssinosis_in_india__a.4.aspx)).

### Quality of Life Impact

Chest tightness/dyspnea and chronic cough directly impair work capacity and daily physical functioning; in advanced/chronic byssinosis, impaired exercise tolerance and, in severe cases, oxygen dependency substantially reduce quality of life (StatPearls). Specific validated instrument (EQ-5D/SF-36) data for byssinosis specifically were not identified in this search — QoL burden is generally inferred from the shared airflow-obstruction/COPD literature rather than byssinosis-specific instrument studies.

---

## 4. Genetic/Molecular Information

Byssinosis is **not a Mendelian single-gene disorder** — there is no single causal gene, and no ClinVar/HGMD pathogenic-variant catalog analogous to a classic genetic disease. Instead, common regulatory polymorphisms in innate-immune/inflammatory genes act as **quantitative modifiers of exposure-response**, altering the magnitude of lung-function decline per unit of endotoxin exposure rather than causing disease independent of exposure.

### Modifier Genes and Variants

| Gene | Variant | Role | Source |
|---|---|---|---|
| TNF (TNF-alpha) | rs1800629 (−308G/A promoter SNP) | Modifies endotoxin-exposure-associated longitudinal FEV₁ decline | Zhang et al., *Occup Environ Med* 2007;64:409–413 |
| LTA (lymphotoxin-alpha) | rs909253 | Co-modifier with TNF in the same cohort | Zhang et al. 2007 |
| EPHX1 (microsomal epoxide hydrolase) | Functional polymorphisms | Interacts with endotoxin exposure to affect lung-function decline | *Am J Respir Crit Care Med* 2005;171:165 ([academic.oup.com](https://academic.oup.com/ajrccm/article-abstract/171/2/165/8538324)) |
| CD14 | −159C/T (and related promoter SNPs) | General endotoxin-receptor modifier (established in organic-dust/asthma literature; biologically plausible for byssinosis) | [PMID 16142747](https://pubmed.ncbi.nlm.nih.gov/16142747/) |
| TLR4 | Asp299Gly, Thr399Ile | Extracellular domain variants altering LPS-receptor responsiveness | [JACI 2003](https://www.jacionline.org/article/S0091-6749(03)01619-1/fulltext) |

MalaCards lists approximately 8 genes associated with byssinosis in its aggregated disease-gene database, consistent with the modifier-gene (rather than causal-Mendelian-gene) model described above ([MalaCards Byssinosis](https://www.malacards.org/card/byssinosis)).

### Epigenetics, Somatic Variants, Chromosomal Abnormalities

No byssinosis-specific epigenetic (DNA methylation/histone), somatic-mutation, or chromosomal-abnormality literature was identified — consistent with its status as an exposure-driven inflammatory airway disease rather than a genetically-driven or neoplastic process. Allele-frequency (gnomAD/1000 Genomes) data for the modifier SNPs above are available generically but are not byssinosis-specific resources.

---

## 5. Environmental Information

### Environmental / Occupational Factors

- **Cotton dust** (raw, unprocessed, particularly from opening/carding stages) — primary exposure
- **Flax dust, hemp dust, jute dust, sisal dust** — cause a clinically similar syndrome in their respective processing industries
- **Bacterial endotoxin (LPS)** contaminating the raw fiber — the leading specific causal component (see Etiology/Mechanism)
- Possible contributory agents: fungal spores, residual agricultural pesticides, plant-derived tannins/bracts (StatPearls; ScienceDirect complement-activation study)

### Lifestyle Factors

- **Cigarette smoking** is consistently identified as a major effect-modifying lifestyle factor: workers with ≥3.5 pack-years smoking history show significantly worse respiratory symptom burden and spirometric outcomes independent of dust exposure, and smoking cessation is considered an essential management step ([PMID: 36717255](https://pmc.ncbi.nlm.nih.gov/articles/PMC9985716/); StatPearls).

### Infectious Agents

Byssinosis is not an infectious disease per se, but the causal agent (endotoxin) is bacterial in origin — Gram-negative bacteria colonizing raw cotton fiber during field growth, harvest, ginning, and storage shed LPS into the fiber/dust matrix. This is a toxin-mediated, not infectious, mechanism (no live bacterial invasion of host tissue is implicated).

---

## 6. Mechanism / Pathophysiology

### Causal Chain (Numbered Sequence)

1. **Raw cotton (or flax/hemp/jute) fiber is colonized by Gram-negative bacteria** during field growth, harvesting, and storage, which **leads to** accumulation of bacterial endotoxin (LPS) adsorbed onto fiber, bract, and trash particulates.
2. **Mechanical processing (opening, carding, blowing) of the raw fiber aerosolizes** endotoxin-laden respirable dust, which **results in** inhalation exposure of textile-mill workers, concentrated in carding/opening-room jobs.
3. **Inhaled endotoxin binds CD14/TLR4/MD-2 receptor complexes on airway macrophages and epithelial cells**, which **triggers** innate-immune activation — this step is demonstrated mechanistically in organic-dust/endotoxin inhalation models generally, and inferred (rather than directly demonstrated in byssinosis-specific human biopsy studies) as the initiating receptor event in the lung.
4. **Receptor activation leads to** release of pro-inflammatory mediators — nitric oxide (which reacts with superoxide to amplify inflammatory injury), IL-6, IL-8, and other neutrophil-chemoattractant cytokines — from resident macrophages and epithelium.
5. **This inflammatory-mediator release results in** recruitment and activation of neutrophils into the airway lumen and bronchial mucosa (documented directly by bronchoalveolar lavage studies in organic-dust-exposed workers), which **triggers** further local cytokine amplification (IL-6, IL-8) and a self-propagating inflammatory cascade.
6. **In parallel, cotton/flax dust extracts activate the complement cascade** (both classical and alternative pathways, demonstrated by C1 consumption, C2 destruction, and C4 conversion assays) — notably, this complement activation does **not** correlate tightly with endotoxin concentration, indicating an endotoxin-independent contributing pathway (inferred to be tannin/bract-derived).
7. **Cotton dust also stimulates degranulation of pulmonary mast cells**, releasing histamine — histamine accumulated in the lung over an exposure-free interval (e.g., the weekend) is proposed to be released upon re-exposure, contributing mechanistically to the "Monday" symptom peak; this histamine hypothesis is supported by elevated blood/lung histamine in exposed workers and guinea-pig models but remains one contributing pathway among several rather than the sole mechanism.
8. **Cotton dust constituents also stimulate release of prostaglandin F2α (PGF2α)**, which **leads to** direct airway smooth-muscle contraction, providing an additional, receptor-independent bronchoconstrictive mechanism.
9. **The combined effects of neutrophilic/cytokine inflammation, complement activation, mast-cell/histamine release, and PGF2α-mediated smooth-muscle contraction converge to cause acute bronchoconstriction**, clinically manifesting as the Monday-pattern chest tightness, cough, and wheeze, and measurable as an acute cross-shift/across-week decline in FEV₁.
10. **With repeated, chronic endotoxin/dust exposure, sustained low-grade airway inflammation leads to** structural airway remodeling — chronic bronchitis, small-airway narrowing, and (in advanced disease) interstitial fibrotic change — which **results in** a fixed, non-reversible, accelerated decline in FEV₁ (approximately 50 mL/year in cotton workers versus the normal physiologic 20–30 mL/year) and, ultimately, chronic obstructive/restrictive respiratory impairment, cor pulmonale, and pulmonary arterial hypertension in severe cases.
11. **Individual genetic variation at this final chronic stage — particularly TNF-308G/A, LTA rs909253, and EPHX1 polymorphisms — modifies the rate of this exposure-driven FEV₁ decline**, explaining why some workers with comparable cumulative endotoxin exposure develop markedly more severe chronic disease than others.

A key epidemiological nuance from the Shanghai Textile Worker Cohort (20-year longitudinal follow-up, n=447): **past cumulative endotoxin exposure** (rather than recent exposure) was the stronger predictor of **long-term annual FEV₁ decline**, whereas **recent exposure (within the prior 5 years)** correlated more strongly with **current respiratory symptoms** (byssinosis/chronic bronchitis) — implying that the acute inflammatory/symptomatic phase and the chronic structural-decline phase, while mechanistically linked, are not perfectly temporally coupled (Christiani et al., PMID: 20797932).

### Molecular Pathways

- Endotoxin (LPS) → CD14/TLR4/MD-2 → NF-κB-driven pro-inflammatory transcription (canonical innate-immune LPS-signaling pathway; not byssinosis-specific but the accepted mechanistic backbone)
- Nitric oxide–superoxide reaction generating reactive nitrogen species and downstream inflammatory/fibrotic signaling
- Complement classical and alternative pathway activation (C1, C2, C4)
- Prostaglandin F2α synthesis/release → smooth-muscle Gq-coupled contraction

### Cellular Processes and Cell Types Involved

- **Airway/alveolar macrophages** — endotoxin sensing and initial cytokine release (Cell Ontology: CL:0000583, lung macrophage)
- **Neutrophils** — recruited into airway lumen/mucosa; central effector of acute inflammation (CL:0000775)
- **Mast cells** — degranulation, histamine release (CL:0000097)
- **Bronchial epithelial cells** — IL-8 production, barrier/signaling role (CL:0002632, or CL:0005006 basal cell of respiratory epithelium)
- **Airway smooth muscle cells** — PGF2α-mediated contraction, and chronic remodeling/hyperplasia (CL:0002598)

### Suggested GO Terms (Biological Processes)

- GO:0002532 — production of molecular mediator involved in inflammatory response
- GO:0032496 — response to lipopolysaccharide
- GO:0006954 — inflammatory response
- GO:0030593 — neutrophil chemotaxis
- GO:0043303 — mast cell degranulation
- GO:0006956 — complement activation
- GO:0006936 — muscle contraction (for the airway smooth-muscle bronchoconstriction node)
- GO:0006817 (n/a) — omit; alternative: GO:0071456 — cellular response to hypoxia (relevant only in advanced cor pulmonale)

### Protein Dysfunction / Biochemical Abnormalities

No primary protein-misfolding or enzyme-deficiency defect is implicated; the relevant "dysfunction" is a genetically-modulated **quantitative hyperresponsiveness** of the TNF/innate-immune signaling axis to a normal environmental ligand (endotoxin), rather than a structural protein lesion.

### Advanced/Omics Data

No byssinosis-specific single-cell, spatial-transcriptomic, or large-scale multi-omics dataset was identified in this search; the mechanistic evidence base is built predominantly from classical BAL cytokine/cell-count studies, animal (guinea pig, rat) inhalation models, and human epidemiologic cohort genotyping rather than modern single-cell atlases.

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary:** Lungs — specifically conducting airways (bronchi, bronchioles) and, in advanced disease, alveolar parenchyma
- **Secondary:** Heart — cor pulmonale and pulmonary arterial hypertension reported as a complication of severe/advanced byssinosis (case report, [ScienceDirect 2025](https://www.sciencedirect.com/science/article/pii/S2949918625001251))
- **Body system:** Respiratory system primarily; cardiovascular system secondarily (right heart strain in advanced disease)

Suggested UBERON terms: UBERON:0002048 (lung), UBERON:0003126 (trachea/bronchus tree — bronchus: UBERON:0002185), UBERON:0002186 (bronchiole)

### Tissue and Cell Level
- Bronchial/bronchiolar epithelium (ciliated and basal cells)
- Airway smooth muscle layer
- Submucosal inflammatory infiltrate (neutrophils, mast cells, macrophages)
- In advanced disease: interstitial/alveolar septal tissue (fibrotic change, ground-glass on HRCT)

### Subcellular Level
- Plasma-membrane pattern-recognition receptor complexes (TLR4/CD14/MD-2) — GO Cellular Component: GO:0005886 (plasma membrane), receptor complex assembly
- Mast cell secretory granules (histamine storage/release) — GO:0042582 (peroxisome n/a; correct term: GO:0030141, secretory granule)

### Localization
- Bilateral, diffuse involvement of the tracheobronchial tree, with basal predominance of HRCT ground-glass/nodular change in more advanced cases; no significant lateralization reported.

---

## 8. Temporal Development

### Onset
- Adult-onset, occupationally triggered; no fixed age of first symptom — determined by age at hire and job exposure intensity (typically manifests within the first several years of high-exposure work, e.g., carding-room employment)
- Onset pattern of the **acute** form is characteristically **episodic/cyclical** (recurring at the start of each exposure period, e.g., Monday), while the **chronic** form has an **insidious**, progressive onset as episodic symptoms merge into a persistent baseline

### Progression
- **Early/acute stage (Schilling Grade ½–1):** intermittent, fully reversible Monday-pattern chest tightness
- **Intermediate stage (Grade 2):** symptoms present on Mondays and other work days; measurable cross-shift FEV₁ decline
- **Advanced/chronic stage (Grade 3-equivalent):** permanent, non-cyclical airflow obstruction, chronic bronchitis, and in the most severe/longest-exposed cases, fibrosis, oxygen dependency, cor pulmonale, and pulmonary arterial hypertension
- Progression rate is variable and exposure-dependent; annualized FEV₁ decline accelerates from the normal ~20–30 mL/year to ~30–50 mL/year in exposed cotton workers (StatPearls; Shanghai cohort PMID 20797932 reported ~32–41 mL/year decline over the first 20 years of follow-up)

### Patterns
- **Remission:** The acute phenotype is fully remission-capable with removal from exposure, especially if intervention occurs before chronic structural change sets in; the chronic phase is largely irreversible
- **Critical period:** Early-career, high-intensity exposure (carding/opening-room work) represents the highest-risk/most modifiable window for intervention (dust control, respirator use, job rotation)

---

## 9. Inheritance and Population

### Epidemiology
Byssinosis prevalence is heavily dependent on exposure intensity, mill dust-control infrastructure, diagnostic criteria used, and country income level:

- **United Kingdom (pre-modern regulation):** historically quoted prevalence ~4%
- **United States:** Cotton Dust OSHA Standard (1978) reduced prevalence from ~20% to <1% among US cotton workers, per OSHA's own retrospective analysis ([OSHA Cotton Dust Hazards](https://www.osha.gov/cotton-dust/hazards))
- **India (2024 pooled meta-analysis, 18 studies, n=5,678, Jan 2000–Sep 2023):** pooled prevalence **24%** (95% CI 13–36%); 20% (95% CI 11–29%) in low-risk-of-bias subgroup ([Journal of Association of Pulmonologists of Tamil Nadu 2024](https://journals.lww.com/jatn/fulltext/2024/07010/pooled_prevalence_of_byssinosis_in_india__a.4.aspx))
- **Low- and middle-income countries broadly (2022 systematic review, 26 studies, n=6,930, 12 countries):** prevalence range **8–38%**, strongly correlated with cotton-dust concentration (r=0.72) ([PMID: 35073782](https://pubmed.ncbi.nlm.nih.gov/35073782/))
- **Pakistan (Karachi MultiTex trial, 2023, n=2,031):** byssinosis prevalence 3% (WHO criteria) to 4% (Schilling criteria), though 56% reported at least one respiratory symptom and 43% reported shortness of breath — illustrating a substantial gap between symptom burden and formally diagnosed byssinosis, and highlighting that current screening questions may be poorly understood by workers in LMIC settings ([PMID: 36717255](https://pmc.ncbi.nlm.nih.gov/articles/PMC9985716/))
- **United States mortality:** >35,000 textile workers disabled and 183 deaths attributed to byssinosis between 1979–1992; North Carolina alone accounted for ~37% of US byssinosis deaths from 1996–2005, reflecting its historical concentration of textile manufacturing

### Inheritance Pattern
Not applicable in the classic Mendelian sense — byssinosis is an acquired, exposure-driven disease. It shows a **multifactorial/gene-environment interaction** pattern: common regulatory polymorphisms (TNF, LTA, EPHX1) act as continuous-trait modifiers of an environmentally-necessary exposure (endotoxin), rather than as necessary or sufficient causal alleles. No penetrance, expressivity, anticipation, germline mosaicism, or founder-effect data apply in the traditional monogenic sense.

### Population Demographics
- **Affected populations:** Predominantly textile-mill workers in cotton-, jute-, flax-, and hemp-producing/processing nations — India, Pakistan, Bangladesh, Nepal, Sri Lanka, Indonesia, Ethiopia, Turkey, Sudan; historically also the US (Southeastern US mill belt — Georgia, North/South Carolina, Maryland) and UK before modern dust-control regulation (StatPearls)
- **Sex ratio:** Textile-mill workforces (and thus byssinosis case series) are frequently female-predominant in South/Southeast Asian settings (e.g., "newly-hired female cotton textile workers" cohorts cited above), reflecting industry hiring patterns rather than an intrinsic sex-linked susceptibility difference
- **Geographic distribution:** Concentrated in regions with active cotton/textile processing industries and historically weaker occupational dust-exposure regulation; prevalence has fallen sharply in countries (US, UK) that adopted enforced permissible-exposure-limit standards

---

## 10. Diagnostics

### Clinical Tests
- **No specific confirmatory diagnostic test exists** — diagnosis rests on the combination of occupational history, characteristic Monday-pattern symptoms, and spirometry (StatPearls).
- **Spirometry:**
  - Cross-shift (pre- vs post-shift) FEV₁ decline >5–10% supports diagnosis
  - FEV₁ <80% predicted supports diagnosis
  - Longitudinal spirometric surveillance (annual) detects accelerated decline (~50 mL/year vs normal ~20–30 mL/year)
- **Laboratory:** Acute post-exposure leukocytosis has been reported but is nonspecific
- **Imaging:**
  - Chest X-ray: hyperlucency, diaphragmatic flattening, emphysematous change; diffuse, ill-defined lower-lung haziness in more advanced disease
  - HRCT: basal-predominant ground-glass opacities with centrilobular nodules
- **Histamine assay (research/adjunct use):** Blood/lung histamine concentration has been proposed as a differential-diagnostic adjunct alongside PFTs, though it is not part of routine clinical practice ([Venkatakrishna-Bhatt et al. 2001](https://journals.sagepub.com/doi/10.1080/109158101753253054))

### Genetic Testing
Not part of routine clinical diagnosis; TNF/LTA/EPHX1 genotyping is a research tool for understanding differential susceptibility, not a diagnostic or screening test in clinical practice.

### Clinical Criteria
Two parallel standardized symptom-grading frameworks are in active use:
- **Schilling grading** (Grade 0 to Grade 2/3, symptom-and-periodicity based)
- **WHO symptoms-based criteria** (work-related chest tightness questionnaire)
These can yield materially different prevalence estimates in the same population (3% WHO vs 4% Schilling in the 2023 Karachi cohort), and authors have flagged that current questionnaire wording may be poorly understood by workers in some LMIC settings, suggesting a need for criteria revision ([PMID: 36717255](https://pmc.ncbi.nlm.nih.gov/articles/PMC9985716/)).

### Differential Diagnosis
Asthma (including occupational asthma, distinguished by its opposite — end-of-week — symptom timing), other pneumoconioses (asbestosis, silicosis, berylliosis, coal worker's pneumoconiosis), farmer's lung/hypersensitivity pneumonitis, metal fume fever, polymer fume fever, interstitial pulmonary fibrosis, sarcoidosis, pulmonary embolism, and acute coronary syndrome (StatPearls).

### Screening
Periodic (typically annual) occupational medical surveillance — symptom questionnaire plus spirometry, including cross-shift testing — is the standard screening approach in regulated textile-mill settings (OSHA 1910.1043 requires such medical surveillance in the US).

---

## 11. Outcome/Prognosis

- **Prognosis with early intervention:** "Most people recover uneventfully with treatment, given avoidance of exposure to cotton [dust]" — early removal from exposure, before chronic structural change, allows substantial or complete FEV₁ recovery (StatPearls).
- **Prognosis with continued/late exposure removal:** Chronic exposure leads to progressive, largely irreversible airflow obstruction and, in severe cases, pulmonary fibrosis, oxygen dependency, impaired exercise tolerance, and disability.
- **Severe complications:** Cor pulmonale and pulmonary arterial hypertension have been reported in advanced/severe byssinosis (case report, [ScienceDirect 2025](https://www.sciencedirect.com/science/article/pii/S2949918625001251)).
- **Mortality:** Deaths attributable to byssinosis are documented in both high-income (US: 183 deaths 1979–1992, concentrated in North Carolina) and lower-income, higher-exposure settings (Pakistan, India, where deaths are described as "not uncommon" in less-regulated mill environments).
- **Prognostic factors:** Cumulative exposure duration/intensity, smoking status, job/processing stage (carding highest risk), and (per the TNF/LTA/EPHX1 literature) individual genotype at endotoxin-response modifier loci.

---

## 12. Treatment

### Primary Intervention
**Removal from further cotton/textile-dust exposure is the single most important and effective intervention.** This is emphasized across all major sources as more important than any pharmacologic measure (StatPearls).

### Pharmacotherapy
- **Short- and long-acting inhaled beta-agonists** (bronchodilators) — symptomatic management; may be required for many months
  - Suggested NCIT term: `NCIT:C15986` (Pharmacotherapy), with `therapeutic_modality: SMALL_MOLECULE`
- **Inhaled corticosteroids** — added for persistent/more severe symptoms
- **Short courses of systemic corticosteroids** — reserved for patients with severe symptoms

### Behavioral / Supportive
- **Smoking cessation** — explicitly identified as essential, given the strong smoking × dust-exposure interaction on symptom severity and lung-function decline
  - Suggested NCIT term: `NCIT:C181743` (Behavioral Counseling) / `therapeutic_modality: BEHAVIORAL`
- **Supportive respiratory care** — oxygen therapy in advanced/chronic disease with impaired exercise tolerance
  - Suggested NCIT term: `NCIT:C15747` (Supportive Care)

### Experimental / Advanced Therapeutics
No gene therapy, cell therapy, RNA-based therapy, targeted molecular therapy, or immunotherapy is applicable or under investigation for byssinosis specifically — treatment remains conventional obstructive-airways-disease symptomatic management plus exposure elimination.

### Treatment Strategy
There is no formalized, disease-specific staged treatment algorithm distinct from general occupational-asthma/COPD management principles: (1) exposure cessation/reduction as the primary and necessary step, (2) bronchodilator ± inhaled corticosteroid titrated to symptom severity, (3) smoking cessation, (4) surveillance spirometry to monitor recovery or progression.

---

## 13. Prevention

### Primary Prevention (most emphasized in the literature)
- **Engineering controls:** dust extraction fans, enclosed processing equipment, adequate mill ventilation
- **Regulatory exposure limits (US):** OSHA 29 CFR 1910.1043 (the Cotton Dust Standard, promulgated 1978) sets permissible exposure limits (PELs) of **0.2 mg/m³** (yarn manufacturing), **0.5 mg/m³** (weaving), and **0.75 mg/m³** (waste processing), specifically targeting the respirable fraction of cotton dust because only that size fraction is implicated in causing byssinosis ([OSHA 1910.1043](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.1043))
- **NIOSH Recommended Exposure Limit (REL):** <0.2 mg/m³ for up to a 10-hour workday ([CDC NIOSH](https://www.cdc.gov/niosh/bulletin/2021/textiles.html))
- **Bactericidal/washing treatment of raw cotton fiber** prior to processing, to reduce bacterial (and thus endotoxin) load
- **Personal protective equipment:** enforced respirator mask use in high-exposure jobs
- **Documented regulatory effectiveness:** OSHA's Cotton Dust Standard is credited with reducing US byssinosis prevalence from ~20% to <1% among cotton workers ([OSHA](https://www.osha.gov/cotton-dust/hazards))

### Secondary Prevention
- **Continued annual employee medical surveillance:** symptom questionnaires plus spirometry (including cross-shift testing) to detect early disease and trigger job reassignment/exposure reduction before chronic change occurs — mandated under the OSHA standard

### Tertiary Prevention
- Prompt job/task reassignment or exposure cessation upon detection of early symptoms or spirometric decline, to prevent progression to the chronic, irreversible disease stage

### Behavioral/Public Health
- Smoking-cessation programs targeted at textile-mill workforces, given the documented smoking × dust-exposure interaction
- Broader public-health advocacy (e.g., the historical US "Brown Lung" workers'-compensation and labor-rights movement of the 1970s) played a documented role in driving the regulatory changes that ultimately reduced disease prevalence

---

## 14. Other Species / Natural Disease

Byssinosis is fundamentally an occupational human disease; there is no well-characterized naturally-occurring veterinary counterpart, as animals are not occupationally exposed to processed textile dust in the way humans are. Species relevance is confined to **experimental/induced models** (see Section 15) rather than spontaneous natural disease. NCBI Taxon: *Homo sapiens* (NCBITaxon:9606) as the sole naturally-affected species identified in the literature searched.

---

## 15. Model Organisms

### Model Types
- **Guinea pig** — the best-validated small-animal model. Guinea pigs exposed by inhalation to breathable, aerosolized raw cotton dust develop a measurable respiratory response (airway resistance changes), whereas exposure to particle-size-matched pure cellulose powder (lacking bacterial contamination) produces no response — directly supporting the endotoxin/bacterial-contaminant hypothesis over a pure-mechanical-irritant hypothesis ([ScienceDirect animal-model study](https://www.sciencedirect.com/science/article/abs/pii/0041008X84901522))
- **Rat, rabbit, hamster, and monkey** — also explored historically as candidate species for modeling the acute byssinotic reaction, with varying degrees of fidelity ([PMC1469574, "Pulmonary reactions to organic dust exposures: development of an animal model"](https://pmc.ncbi.nlm.nih.gov/articles/PMC1469574/))
- **Guinea pig histamine studies** — chronic cotton/flax dust exposure in guinea pigs was used to demonstrate elevated lung histamine concentrations, supporting the histamine-accumulation/release hypothesis for the Monday-pattern symptom cycle ([PMID: 6722048](https://pubmed.ncbi.nlm.nih.gov/6722048/))

### Induced Models
All animal models are **inhalation-exposure induced** — repeated or single-dose aerosolized cotton dust or purified/extracted endotoxin challenge — rather than genetic (knockout/transgenic) models, consistent with byssinosis's fundamentally exposure-driven rather than monogenic etiology.

### Model Characteristics
- **Phenotype recapitulation:** The guinea pig cotton-dust inhalation model recapitulates the acute bronchoconstrictive/airway-resistance response reasonably well and has been central to establishing endotoxin (rather than raw cellulose) as the causal agent.
- **Tachyphylaxis/tolerance parallel:** Repeated endotoxin inhalation in animal models produces an attenuation of the airway response over repeated exposures, mirroring the "Monday-worst, improves through the week" tolerance phenomenon seen clinically in human workers — a notable and mechanistically informative cross-species parallel (search summary, animal-model literature).
- **Limitations:** Acute animal-inhalation models capture the acute bronchoconstrictive/inflammatory phase well but are less well validated for reproducing the chronic, fibrotic, structurally-remodeled end-stage of human byssinosis, which develops only after years of cumulative occupational exposure not easily replicated in a laboratory exposure protocol.

### Applications
Animal endotoxin-inhalation models have been used primarily to (1) distinguish the causal role of bacterial endotoxin from inert cotton particulate, (2) characterize acute inflammatory-cell recruitment (neutrophils) and mediator release (histamine, complement), and (3) study dose-response and tolerance/tachyphylaxis phenomena relevant to the human Monday-symptom pattern.

### Resources
No byssinosis-specific dedicated model-organism database (equivalent to MGI/ZFIN/IMPC for genetic disease models) exists, reflecting the absence of genetic knockout/transgenic models for this exposure-driven condition; the relevant literature is scattered across occupational/environmental-health and toxicology journals rather than centralized model-organism repositories.

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Category | Suggested term |
|---|---|
| Disease | MONDO:0006688 (byssinosis) |
| Phenotypes | HP:0030828 (Wheezing), HP:0002094 (Dyspnea), HP:0012735 (Cough), HP:0030830 (Crackles), HP:0001974 (Leukocytosis) |
| Biological processes | GO:0032496 (response to lipopolysaccharide), GO:0006954 (inflammatory response), GO:0030593 (neutrophil chemotaxis), GO:0043303 (mast cell degranulation), GO:0006956 (complement activation) |
| Cell types | CL:0000583 (lung macrophage), CL:0000775 (neutrophil), CL:0000097 (mast cell), CL:0002598 (airway smooth muscle cell) |
| Anatomy | UBERON:0002048 (lung), UBERON:0002185 (bronchus), UBERON:0002186 (bronchiole) |
| Genes (modifiers) | TNF (hgnc:11892), LTA (hgnc:6709), EPHX1 (hgnc:3401), CD14 (hgnc:1633), TLR4 (hgnc:11850) |
| Chemical/exposure | CHEBI (endotoxin/LPS — CHEBI:16412, lipopolysaccharide); ECTO exposure term for occupational cotton-dust inhalation |
| Treatment | NCIT:C15986 (Pharmacotherapy — bronchodilators/corticosteroids), NCIT:C15747 (Supportive Care), NCIT:C181743 (Behavioral Counseling — smoking cessation) |

---

## Sources

- [Byssinosis — StatPearls, NCBI Bookshelf (NBK519549)](https://www.ncbi.nlm.nih.gov/books/NBK519549/)
- [Byssinosis | Treatment & Management — StatPearls Point of Care](https://www.statpearls.com/point-of-care/18737)
- [Chronic Lung Function Decline in Cotton Textile Workers: Roles of Historical and Recent Exposures to Endotoxin — PMC2974703 / PMID: 20797932](https://pmc.ncbi.nlm.nih.gov/articles/PMC2974703/)
- [Byssinosis and lung health among cotton textile workers: baseline findings of the MultiTex trial in Karachi, Pakistan — PMC9985716 / PMID: 36717255](https://pmc.ncbi.nlm.nih.gov/articles/PMC9985716/)
- [Contemporary Prevalence of Byssinosis in Low- and Middle-Income Countries: A Systematic Review — PMID: 35073782](https://pubmed.ncbi.nlm.nih.gov/35073782/)
- [Pooled Prevalence of Byssinosis in India: A Systematic Review and Meta-analysis (2024) — Journal of the Association of Pulmonologists of Tamil Nadu](https://journals.lww.com/jatn/fulltext/2024/07010/pooled_prevalence_of_byssinosis_in_india__a.4.aspx)
- [Byssinosis: a study of 10,133 textile workers — PMID: 4689794](https://pubmed.ncbi.nlm.nih.gov/4689794/)
- [Prevalence of byssinosis and respiratory symptoms among cotton mill workers — PMID: 11844963](https://pubmed.ncbi.nlm.nih.gov/11844963/)
- [Microsomal Epoxide Hydrolase, Endotoxin, and Lung Function Decline in Cotton Textile Workers — Am J Respir Crit Care Med 2005;171:165](https://academic.oup.com/ajrccm/article-abstract/171/2/165/8538324)
- [A Large Scale Gene-Centric Association Study of Lung Function in Newly-Hired Female Cotton Textile Workers with Endotoxin Exposure — PLOS ONE / PMID: 23527081](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0059035)
- [Organic dust induced inflammation — role of atopy and TLR-4 and CD14 gene polymorphisms — PMID: 16142747](https://pubmed.ncbi.nlm.nih.gov/16142747/)
- [TLR4 gene variants modify endotoxin effects on asthma — Journal of Allergy and Clinical Immunology](https://www.jacionline.org/article/S0091-6749(03)01619-1/fulltext)
- [Pulmonary reactions to inhaled cotton dust: An animal model for byssinosis — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/0041008X84901522)
- [Pulmonary reactions to organic dust exposures: development of an animal model — PMC1469574](https://pmc.ncbi.nlm.nih.gov/articles/PMC1469574/)
- [Role of histamine in the aetiology of byssinosis. I — PMC1009284 / PMID: 6202313](https://pmc.ncbi.nlm.nih.gov/articles/PMC1009284/)
- [Role of histamine in the aetiology of byssinosis. II — PMID: 6722048](https://pubmed.ncbi.nlm.nih.gov/6722048/)
- [In vitro alternative and classical activation of complement by extracts of cotton mill dust — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/0013935183901901)
- [Differential Diagnosis of Byssinosis by Blood Histamine and Pulmonary Function Test — SAGE Journals](https://journals.sagepub.com/doi/10.1080/109158101753253054)
- [Severe byssinosis with Cor pulmonale and pulmonary arterial hypertension — case report, ScienceDirect 2025](https://www.sciencedirect.com/science/article/pii/S2949918625001251)
- [Lung Disease in Textile Workers — CDC NIOSH Science Bulletin 2021](https://www.cdc.gov/niosh/bulletin/2021/textiles.html)
- [OSHA 1910.1043 — Cotton dust](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.1043)
- [Cotton Dust — Hazards and Possible Solutions — OSHA](https://www.osha.gov/cotton-dust/hazards)
- [Byssinosis — an historical perspective — PMID: 7048909](https://pubmed.ncbi.nlm.nih.gov/7048909/)
- [Brown Lung Blues — Science for the People Archives](https://archive.scienceforthepeople.org/vol-9/v9n3/brown-lung-blues/)
- [byssinosis — Monarch Initiative, MONDO:0006688](https://monarchinitiative.org/MONDO:0006688)
- [2026 ICD-10-CM Diagnosis Code J66.0: Byssinosis](https://www.icd10data.com/ICD10CM/Codes/J00-J99/J60-J70/J66-/J66.0)
- [Byssinosis — MalaCards](https://www.malacards.org/card/byssinosis)