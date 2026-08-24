---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-05T01:07:19.023700'
end_time: '2026-08-05T01:31:49.128317'
duration_seconds: 1470.1
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Self-Limited Epilepsy with Autonomic Seizures
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
  web_search_requests: 8
  num_turns: 60
  total_cost_usd: 7.739929
  session_id: c80906c2-6bb8-45d9-a106-d8bb532ae8c7
  stop_reason: end_turn
citation_count: 28
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Self-Limited Epilepsy with Autonomic Seizures
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Self-Limited Epilepsy with Autonomic Seizures** covering all of the
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

# Self-Limited Epilepsy with Autonomic Seizures (Panayiotopoulos Syndrome)
## Comprehensive Research Report for Knowledge Base Curation

**Compiled:** 2026-08-05 · **Target MONDO:** MONDO:0020307 · **Category:** Complex (non-Mendelian, age-dependent electroclinical syndrome)

---

### Curator's note before you dive in

Two things shape this entire report, and both are worth flagging up front because they will constrain what can honestly be curated.

**First: this disease has almost no molecular floor.** There is no causal gene, no OMIM entry, no biomarker, no biopsy finding, no animal model, no omics dataset. The ILAE's own syndrome page says it plainly: *"There are no established genes, outside of rare case reports, and no clear indication to perform genetic testing."* The mechanism sections below are therefore built from electroclinical inference and neuroanatomy, not from molecular evidence — think of it less like a broken enzyme and more like a developmental tuning problem, a circuit that runs hot for a few years and then settles. Curate accordingly, and mark mechanistic claims as hypotheses rather than established chains.

**Second: the entity was renamed in 2022.** ILAE nosology replaced "Panayiotopoulos syndrome" with "self-limited epilepsy with autonomic seizures" (SeLEAS), and dropped both "benign" and "idiopathic" as descriptors. Nearly all the primary literature predates the rename and uses the eponym. The MONDO label already tracks the new name.

Sections where evidence is genuinely absent are marked **NOT AVAILABLE** rather than padded.

---

## 1. Disease Information

### Overview

Self-limited epilepsy with autonomic seizures (SeLEAS) is a childhood-onset focal epilepsy syndrome in which the seizures are dominated by autonomic manifestations — above all vomiting — rather than by motor or sensory features. It affects otherwise normal children, typically between ages 3 and 6, produces very few seizures overall (often only one), and remits spontaneously within a couple of years. Its clinical signature is a strange one for epilepsy: a fully conscious child who starts retching, goes pale, and then over the next half hour drifts into unresponsiveness with the eyes deviated to one side, most often out of sleep.

The MONDO definition (retrieved from OLS4, 2026-08-05):

> "A childhood-onset self-limited focal epilepsy syndrome characterized by the onset in early childhood of focal autonomic seizures that are often prolonged. The EEG commonly shows high amplitude focal spikes typically activated by sleep. Seizures are infrequent in most patients. Seizures are self-limiting with remission typically within a few years from onset."

The 2006 international consensus definition (Ferrie et al., **PMID:16483404**) is the one most cited in the clinical literature:

> "We conclude that PS is a common idiopathic, benign seizure disorder of childhood, which should be classified as an autonomic epilepsy, rather than an occipital epilepsy."

Covanis (**PMID:16950946**) quotes the consensus wording directly:

> "An expert consensus has defined Panayiotopoulos syndrome as 'a benign age-related focal seizure disorder occurring in early and mid-childhood. It is characterized by seizures, often prolonged, with predominantly autonomic symptoms, and by an EEG [electroencephalogram] that shows shifting and/or multiple foci, often with occipital predominance.'"

### Key identifiers

| Resource | Identifier | Notes |
|---|---|---|
| **MONDO** | **MONDO:0020307** | Label: "Self-limited epilepsy with autonomic seizures". Verified live via OLS4 2026-08-05 |
| Orphanet | ORPHA:98815 | MONDO xref |
| UMLS | C0393676 | MONDO xref |
| MedGen | 581520 | MONDO xref |
| SNOMED CT | 230387008 | MONDO xref |
| GARD | 0019581 | MONDO xref |
| ICD-9-CM | 345.80 | MONDO xref |
| ICD-10 | G40.0 | Conventional mapping (localization-related idiopathic epilepsy with seizures of localized onset). **Not** a curated MONDO xref — treat as low confidence |
| ICD-11 | 8A61.2Y (reported) | Secondary sources only; **low confidence**, verify against the WHO browser before curating |
| **OMIM** | **none** | No OMIM xref exists in MONDO. Consistent with the absence of a Mendelian gene |
| MeSH | no dedicated descriptor | Indexed under *Epilepsies, Partial* / *Epilepsy, Benign Neonatal* headings |

### Synonyms and alternative names

From MONDO (OLS4) plus the literature:

- **Panayiotopoulos syndrome** (the eponym; still overwhelmingly dominant in the literature)
- SeLEAS (abbreviation)
- Benign childhood occipital epilepsy, Panayiotopoulos type
- Early-onset benign childhood occipital epilepsy (EBOE)
- Early-onset benign occipital epilepsy
- Benign childhood epilepsy with occipital paroxysms, early-onset variant
- Benign childhood autonomic epilepsy
- Idiopathic childhood occipital epilepsy of Panayiotopoulos

**Deprecated terminology to avoid:** "benign" and "idiopathic". Quito-Betancourt & Reyes Valenzuela (**PMID:37714124**) state: *"Using the term 'benign' to refer to them is no longer recommended, as this would ignore the comorbidities some individuals suffer. Also, the term 'idiopathic' is now only used to refer to the syndromes classified as Idiopathic Generalized Epilepsies."*

### Source of information

Almost entirely **aggregated disease-level** and **cohort-level** clinical sources: hospital-based prospective and retrospective case series (Caraballo n=192, **PMID:17442007**; Specchio n=93, **PMID:20528983**; Değerliyurt n=38, **PMID:24840752**), an international expert consensus (**PMID:16483404**), and ILAE nosology documents. There are **no** EHR-derived phenotype studies, no disease registries, and no population biobank analyses specific to SeLEAS. The one population-based incidence study (**PMID:29571057**) used prospective clinician reporting within a defined UK/Welsh catchment area, not EHR extraction.

---

## 2. Etiology

### Disease causal factors

**Primary cause: unknown; presumed age-dependent maturational.** The dominant framing across three decades of literature is that SeLEAS is not caused by a lesion or a single gene but by a transient, developmentally timed state of cortical hyperexcitability that preferentially engages autonomic circuitry. Panayiotopoulos himself (**PMID:15145296**) put it this way:

> "Pathophysiology of Panayiotopoulos syndrome is unknown, but it is likely that they are due to diffuse maturation-related epileptogenicity activating susceptible-for-children emetic centers and the hypothalamus."

Covanis (**PMID:16950946**) frames it as one pole of a shared childhood susceptibility:

> "Panayiotopoulos syndrome is probably the early-onset and Rolandic epilepsy the late-onset phenotype of a maturation-related benign childhood seizure-susceptibility syndrome."

**Structural etiology is exclusionary.** Per the ILAE 2022 diagnostic criteria table, "Structural cause for the epilepsy" on imaging is an **exclusionary criterion**. Note however that Panayiotopoulos (**PMID:15145296**) reported that among children with autonomic seizures and autonomic status epilepticus generally, *"10-20% are due to cerebral pathology"* — those cases are symptomatic focal epilepsy, not SeLEAS.

**A boundary case worth curating:** Cooper et al. (**PMID:35871494**) found that children with cerebral palsy from prenatal/perinatal vascular injury frequently develop an electroclinically identical picture, which they termed "self-limited focal epilepsy-variant" precisely because the current ILAE classification forbids the diagnosis in the presence of a brain lesion:

> "Fifty-six (60%) children with seizures had electroclinical features of a self-limited focal epilepsy of childhood; we diagnosed these children with a self-limited focal epilepsy-variant given the current International League Against Epilepsy classification precludes a diagnosis of self-limited focal epilepsy in children with a brain lesion. … Self-limited focal epilepsy-variant usually manifested with a mix of autonomic and brachio-facial motor features, and occipital and/or centro-temporal spikes on EEG."

This is mechanistically informative: it suggests the autonomic-seizure phenotype reflects an *age-dependent network state* that a structural lesion can also unmask, rather than a lesion-free requirement of the mechanism itself.

### Risk factors — genetic

- **No established causal gene.** ILAE syndrome page (epilepsydiagnosis.org, CC BY-SA 4.0, text last updated 2024-06-30): *"There are no established genes, outside of rare case reports, and no clear indication to perform genetic testing."*
- **No classical inheritance pattern.** ILAE: *"There is a higher prevalence of febrile seizures in first degree relatives, suggesting genetic factors play a role, but there is no classical inheritance pattern."*
- **SCN1A is the one gene with credible (rare) evidence.** Kivity et al. (**PMID:28192756**) described a large GEFS+ family segregating a heterozygous pathogenic SCN1A missense variant in which four members had Panayiotopoulos syndrome: *"A pathogenic heterozygous SCN1A (c.2624C>A; p.Thr875Lys) variant was identified. Sixteen of the 18 variant positive family members were affected (88% penetrance): 8 with febrile seizures, 2 febrile seizures plus, 1 unclassified seizures and 5 with self-limited focal epilepsy of childhood. Of these, one was diagnosed with atypical childhood epilepsy with centrotemporal spikes and four with Panayiotopoulos syndrome."* Their conclusion: *"the GEFS+ spectrum can extend to the self-limited focal epilepsies of childhood, including Panayiotopoulos syndrome."*
- **Family history of febrile seizures and epilepsy is enriched.** Değerliyurt et al. (**PMID:24840752**): *"We found high rates of personal history of febrile convulsions, breath-holding spells, and family history of febrile convulsions, afebrile convulsion/epilepsy, migraine, and breath-holding spells."*
- **Twin data argue against a simple genetic model.** Taylor et al. (**PMID:18669497**), a twin and multiplex family study of benign occipital epilepsies of childhood: *"Monozygotic twin pairs did not show a higher concordance rate than dizygotic twin pairs suggesting that BOEC may not be a purely genetic disorder. … Clinical genetic studies highlight the multifactorial aetiology of BOEC as monozygotic twins have low concordance suggesting that non-conventional genetic influences or environmental factors play a major role."* **This is the single most important genetic-etiology citation for the entry** — it is a direct, human, evidence-based argument *against* over-genetic framing.
- **Complex/polygenic architecture is the working model** for self-limited focal epilepsies generally. Tsai et al. (**PMID:23294109**), studying the related epilepsy-aphasia spectrum and BECTS families, found: *"The frequencies of seizures in relatives of probands with EAS suggest that the underlying genetic influence of EAS is consistent with complex inheritance and similar to BECTS."*

### Risk factors — environmental

**NOT AVAILABLE / largely negative.** No toxin, infection, occupational, or dietary risk factor has been established. Specifically:

- **Antecedent and birth history are normal** (ILAE syndrome page).
- **Sex:** no risk difference. ILAE: *"Both sexes are affected equally."*
- **Age:** the only robust "risk factor" is being in the 3–6 year window. This is the defining feature, not an incidental one.
- **Prior febrile seizures:** present in **5–17%** of patients (ILAE syndrome page) — plausibly a shared-susceptibility marker rather than a cause.
- **Sleep** is a powerful *precipitant* (not a cause): two-thirds to >80% of seizures arise from sleep (see §3).

### Protective factors

**NOT AVAILABLE.** No protective genetic variant, dietary factor, or lifestyle exposure has been reported for SeLEAS. The condition remits spontaneously regardless of treatment, which makes protective-factor studies both difficult and low-priority.

### Gene–environment interactions

**NOT AVAILABLE** in any direct form. The strongest indirect statement is Taylor et al.'s twin-discordance finding (**PMID:18669497**) implying that *"non-conventional genetic influences or environmental factors play a major role"* — i.e. the field explicitly posits a G×E or epigenetic contribution but has not identified it.

---

## 3. Phenotypes

### 3.1 The cardinal phenotype — focal autonomic seizures

The single mandatory seizure type per ILAE 2022. Covanis (**PMID:16950946**) gives the canonical description:

> "Autonomic epileptic seizures and autonomic status epilepticus are the cardinal manifestations of Panayiotopoulos syndrome. Autonomic seizures in Panayiotopoulos syndrome consist of episodes of disturbed autonomic function with emesis as the predominant symptom. Other autonomic manifestations include pallor (or, less often, flushing or cyanosis), mydriasis (or, less often, miosis), cardiorespiratory and thermoregulatory alterations, incontinence of urine and/or feces, hypersalivation, and modifications of intestinal motility."

**Suggested HP terms (all verified against OLS4, 2026-08-05):**

| Phenotype | HP term | ID | Notes |
|---|---|---|---|
| Focal autonomic seizure (parent) | Focal autonomic seizure | **HP:0011154** | The defining term |
| Aware autonomic seizure | Focal aware autonomic seizure | **HP:0032740** | Seizures typically begin with awareness preserved |
| Impaired-awareness autonomic seizure | Focal impaired awareness autonomic seizure | **HP:0032755** | Awareness is lost as the seizure evolves |
| Ictal emesis / GI phenomena | Focal autonomic seizure with epigastric sensation/nausea/vomiting/other gastrointestinal phenomena | **HP:0011159** | **The most specific available term for the hallmark feature** |
| Pallor/flushing | Focal aware autonomic seizure with pallor/flushing | **HP:0032761** | |
| Cardiac autonomic features | Focal autonomic seizure with palpitations/tachycardia/bradycardia/asystole | **HP:0032773** | |
| Autonomic dysfunction (generic parent) | Abnormality of the autonomic nervous system | **HP:0002270** | Use only if a more specific term does not fit |

### 3.2 Phenotype table with frequencies

| Phenotype | Type | HP term | ID | Frequency | Source |
|---|---|---|---|---|---|
| **Ictal vomiting / emesis** | Symptom (autonomic) | Focal autonomic seizure with epigastric…vomiting… | HP:0011159 | **~74–83%** of patients ("usually culminated in vomiting (77.4% of patients)") | PMID:20528983 |
| Vomiting (generic) | Symptom | Vomiting | HP:0002013 | — | — |
| Nausea | Symptom | Nausea | HP:0002018 | Common, precedes emesis | PMID:16950946 |
| **Pallor** | Clinical sign | Pallor | HP:0000980 | Very frequent; "Emesis, pallor, or flushing was almost always among the first symptoms" | PMID:20528983 |
| Flushing | Clinical sign | — (use HP:0032761) | HP:0032761 | Less common than pallor | PMID:16950946 |
| Cyanosis | Clinical sign | Cyanosis | HP:0000961 | Less common | PMID:31369969 |
| **Mydriasis** | Clinical sign | Mydriasis | HP:0011499 | Frequent (miosis less often) | PMID:16950946 |
| **Tonic eye deviation** | Clinical sign | Abnormal conjugate eye movement | HP:0000549 | Very frequent; part of the original 1989 triad | PMID:19469846, PMID:17442007 |
| **Impaired awareness / unresponsiveness** | Clinical sign | Focal impaired awareness seizure | HP:0002384 | **83.3%** in one series | PMID:17057874 |
| **Ictal syncope** (flaccid unresponsiveness) | Clinical sign | Syncope | HP:0001279 | **~20%** of seizures ("In approximately one fifth of the seizures the child becomes unresponsive and flaccid"); 29.2% of an atypical-presentation series; 37.5% in a comparative cohort | PMID:16950946; PMID:35063695; PMID:24777033 |
| **Autonomic status epilepticus** (≥30 min) | Clinical sign | Focal non-convulsive status epilepticus with impairment of consciousness | HP:0032861 | **~50–55%** of seizures ("More than half (55%) of seizures were longer than 30 min"); autonomic status in ~1/3 of *patients* | PMID:20528983; PMID:24840752; PMID:17442007 |
| Status epilepticus (generic) | Clinical sign | Status epilepticus | HP:0002133 | — | — |
| **Focal to bilateral tonic-clonic / hemiconvulsions** | Clinical sign | Bilateral tonic-clonic seizure with focal onset | HP:0007334 | **~50%** ("Only half of the seizures end with brief hemiconvulsions or generalized convulsions") | PMID:16950946 |
| Hemiclonic seizure | Clinical sign | Focal hemiclonic seizure | HP:0006813 | Component of the above | PMID:16950946 |
| **Sleep-related occurrence** | Course feature | — | — | **~67–81.5%** ("Two thirds of seizures occur during sleep"; 81.5% sleep-related in Turkish series; all but 5/192 in Argentine series) | PMID:16950946; PMID:24840752; PMID:17442007 |
| Hypersalivation | Symptom | Excessive salivation | HP:0003781 | Reported | PMID:16950946 |
| Urinary/fecal incontinence | Clinical sign | Urinary incontinence | HP:0000020 | 9.7% as a *presenting* feature in an atypical series | PMID:35063695 |
| Thermoregulatory change (hyperthermia without infection) | Clinical sign | — (no good HP term) | — | 14.6% as first manifestation in atypical series | PMID:35063695 |
| Ictal/postictal headache | Symptom | Headache | HP:0002315 | 9.7% as initial manifestation; major migraine-mimic driver | PMID:35063695; PMID:42348808 |
| Cough as initial feature | Symptom | — | — | 4.8% | PMID:35063695 |
| Oral automatisms (sucking, chewing) | Clinical sign | — | — | 4.8% | PMID:35063695 |
| Visual symptoms (hallucinations, amaurosis) | Symptom | — | — | **~5%** (contrast with Gastaut syndrome, where they dominate) | PMID:24840752 |
| Rolandic (centrotemporal) features | Clinical sign | — | — | **26%** | PMID:24840752 |
| **Ictal cardiorespiratory arrest** | Clinical sign (rare, severe) | Apnea (HP:0002104) + Bradycardia (HP:0001662) | HP:0002104 / HP:0001662 | **Exceptional**; 4.8% of an *atypical-presentation* series (2/44) — not of unselected cases | PMID:35063695; PMID:21822089; PMID:29926008 |
| **Interictal multifocal spikes** | Lab/EEG | Multifocal epileptiform discharges | **HP:0010841** | **79.5–84%** | PMID:20528983; PMID:24840752 |
| Occipital spikes | Lab/EEG | EEG with occipital focal spikes | **HP:0012016** | **75%** in one series | PMID:17057874 |
| Centrotemporal spikes | Lab/EEG | EEG with centrotemporal focal spike waves | **HP:0012557** | **25%** also had rolandic spikes | PMID:17057874 |
| Fixation-off sensitivity | Lab/EEG | Fixation-off epileptiform discharges | **HP:0025644** | Eye closure activates posterior discharges in some | ILAE EEG page |
| Normal EEG | Lab/EEG | — | — | **5.4–16.6%** | PMID:20528983; PMID:17057874 |

### 3.3 Cognitive and behavioral phenotypes — the "benign" caveat

This is the section where the old "benign" label has been most substantially revised, and it deserves careful curation because the evidence is genuinely split.

**Evidence for cognitive comorbidity.** Fonseca Wald et al. (**PMID:32608507**, n=18, Netherlands):

> "Mean full-scale IQ (93.5; range 76-123; p=0.04) and performance IQ (93.2; range 76-126; p=0.04) were within the normal range, although significantly lower compared to the normative mean. … Simple auditory/visual reaction times, visual attention, visual-motor integration, and verbal memory were significantly lower compared to normative values. On average, patients with Panayiotopoulos syndrome were 8 months behind in arithmetic speed and 11 months behind in reading speed for the number of months in school. Behavioural questionnaires revealed significantly higher scores on reported internalizing behavioural problems."

Akca Kalem et al. (**PMID:31398558**, n=20 PS vs 20 Gastaut vs 20 controls):

> "With regard to intelligence, the patients with PS scored less in all scales compared to the healthy controls. … Verbal memory problems were eminent in both of the patient groups; whereas, visual memory was impaired only in the group with PS. … Cognitive dysfunction is a more prominent and widespread feature of the patients with PS; whereas, the patients with GS suffer only from milder and isolated cognitive problems."

Hodges et al. (**PMID:26709104**, n=3): *"Neuropsychological findings suggest that the patients had notable impairments on visual memory tasks, especially in comparison with verbal memory. … Academically, the patients were weak in numerical operations and spelling."*

**Evidence against clinically meaningful comorbidity.** Specchio et al. (**PMID:20528983**, n=93 — by far the largest neuropsychologically characterized cohort):

> "On neuropsychological testing, IQ and subtests of Wechsler Intelligence Scale for Children-Revised (WISC-R) were within normal limits, although some minor statistically significant differences were found in arithmetic, comprehension, and picture arrangement in comparison with controls."

And the ILAE syndrome page still states flatly: *"Development and cognition are normal."*

**Curation recommendation:** model this as a mild, contested phenotype with an explicit `KNOWLEDGE_GAP` discussion. The disagreement is real and traceable to cohort size and referral bias (the small tertiary-center cohorts find deficits; the large consecutive-referral cohort does not). A published commentary exists specifically on this question (Wilson, "Rethinking neurobehavioral comorbidity in Panayiotopoulos syndrome", **PMID:31909486**).

**Suggested HP terms for this cluster:**
- Specific learning disability — **HP:0001328**
- Impaired visuospatial constructive cognition — **HP:0010794**
- Attention deficit hyperactivity disorder — **HP:0007018** (weakly supported; Akca Kalem found *no* behavioral excess)
- Anxiety — **HP:0000739** (internalizing problems, PMID:32608507)

### 3.4 Onset, severity, progression

- **Age of onset:** 3–6 years in ~70%; full range 1–14 years (ILAE syndrome page). Specchio: *"Age at onset ranged from 1.1 to 8.6 years, and was earlier in children with more than one seizure"* (PMID:20528983). Caraballo: *"PS had a peak age at onset of 5 years"* (PMID:17442007). Değerliyurt: *"Seizures started before the age of eight in 87% of the patients, and the mean age at seizure onset was 4.6 years"* (PMID:24840752).
- **Severity:** individually dramatic, cumulatively mild. Single seizures are frightening and often prolonged, but total seizure burden is low.
- **Progression:** **episodic and self-limiting**. Not progressive. ILAE: *"Seizures usually remit in 1-2 years."*
- **Seizure count:** ILAE: *"Seizure frequency is usually low, 25% of children have only a single seizure and most children have ≤5 seizures in total."* Caraballo (**PMID:17442007**): *"Eighty-four (44.2%) had a single seizure, 79 (41.2%) had 2-5 fits, and 28 (14.6%) had frequent seizures."* Tedrus (**PMID:17057874**): *"Fourteen children (38.8%) had a single seizure."*

### 3.5 Quality of life impact

**Limited direct evidence.** No SeLEAS-specific EQ-5D, SF-36, PROMIS, or QOLCE study exists. What is available:

- **The dominant QoL burden is diagnostic, not seizure-related.** Graziosi et al. (**PMID:31369969**): *"a wrong diagnosis may lead to inappropriate interventions. The consequences are high morbidity, costly mismanagement, and stress for children and their parents."* Covanis (**PMID:16950946**) echoes: *"The consequence is avoidable misdiagnosis, high morbidity, and costly mismanagement."* Children are subjected to lumbar punctures, empiric aciclovir, ICU admission, and repeated imaging for a condition that requires none of it.
- **Academic impact** (PMID:32608507): reading and arithmetic speed lag by 8–11 school months; *"Mild-to-severe academic underachievement was present in more than half of the children with Panayiotopoulos syndrome."*
- A single lateralization-based QoL study in childhood epilepsy (not SeLEAS-specific) found right-hemispheric foci associated with worse anxiety/social/stigma scores (**PMID:20716372**) — mark as indirect.
- A pilot exercise-therapy trial in the sibling syndrome BECTS (**PMID:25025685**) showed improvement in internalizing behavioral problems and mood-related well-being; **not** performed in SeLEAS.

---

## 4. Genetic / Molecular Information

### Causal genes

**NONE ESTABLISHED.** This is the correct curation, and it should be stated affirmatively rather than left blank. Authoritative statement (ILAE, epilepsydiagnosis.org, June 2024): *"There are no established genes, outside of rare case reports, and no clear indication to perform genetic testing."*

### Candidate / reported genes

| Gene | HGNC | Evidence | Relationship type | Strength |
|---|---|---|---|---|
| **SCN1A** | hgnc:10585 | One large GEFS+ family: c.2624C>A, p.Thr875Lys, heterozygous missense, 88% penetrance, 4 members with PS phenotype (**PMID:28192756**). Plus three prior case reports acknowledged in that paper: *"There are, however, three reports of SCN1A variants in Panayiotopoulos syndrome."* | SUSCEPTIBILITY / COOPERATING (not causal for the syndrome) | Weak-moderate; single family + case reports |
| GRIN2B | hgnc:4586 | Null variant, de novo, in the broader self-limited focal epilepsy cohort — but associated with **atypical** Rolandic epilepsy, not SeLEAS specifically (**PMID:32600977**) | Candidate, other syndrome in spectrum | Weak, indirect |
| CAMK2A | hgnc:1460 | Missense, de novo, same cohort, atypical presentations (**PMID:32600977**) | Candidate, indirect | Weak |
| CACNG2 | hgnc:1406 | Splice-site substitution, "good candidate" in same cohort (**PMID:32600977**) | Candidate, indirect | Weak |
| GRIN2A | hgnc:4585 | Established for the epilepsy-aphasia continuum (ECSWS/LKS/atypical Rolandic), **not** for SeLEAS. The Rudolf cohort explicitly pre-screened GRIN2A-negative patients | Related-syndrome gene; exclude from SeLEAS causal set | N/A |
| SCN2A | hgnc:10588 | Established for self-limited *familial* neonatal-infantile epilepsy (**PMID:23622206**), **not** SeLEAS | Related-syndrome gene | N/A |

The critical framing sentence from the exome study (Rudolf et al., **PMID:32600977**): *"Our results further illustrate the fact that atypical SFEC are more likely to have Mendelian inheritance than typical SFEC."* In other words — the more the child looks like textbook SeLEAS, the *less* likely a gene will be found. This should be recorded as a curation-relevant principle, not just a result.

### Variant classification, type, allele frequency, origin, functional consequence

- **Classification:** the SCN1A p.Thr875Lys variant is reported as pathogenic (**PMID:28192756**); no other variant is classified for this syndrome. No ClinVar assertion set exists for "Panayiotopoulos syndrome" as a condition.
- **Type:** missense (SCN1A); the candidate set includes null, missense, and splice-site variants.
- **Allele frequency:** **NOT AVAILABLE** — no population-frequency analysis has been performed against a SeLEAS phenotype.
- **Somatic vs germline:** all reported variants are **germline**. No somatic/mosaic mechanism has been proposed.
- **Functional consequence:** for SCN1A, the GEFS+ mechanism is generally loss of function of Na<sub>v</sub>1.1 in GABAergic interneurons producing disinhibition — but this is extrapolated from GEFS+/Dravet biology, **not** demonstrated for the SeLEAS phenotype. Mark as inference.

### Modifier genes

**NOT AVAILABLE.** No modifier gene has been identified. Because SeLEAS remits regardless, there is no severity gradient to map modifiers against.

### Epigenetic information

**NOT AVAILABLE.** No methylation, histone-modification, or chromatin study exists for SeLEAS. Rudolf et al. (**PMID:32600977**) noted *"missense variants in genes encoding enzymes involved in chromatin remodeling"* among candidates in atypical self-limited focal epilepsies — a hint, not a finding.

### Chromosomal abnormalities

**NOT AVAILABLE / negative.** No recurrent CNV, translocation, or aneuploidy is associated. Chromosomal microarray is not indicated for typical SeLEAS.

---

## 5. Environmental Information

- **Environmental factors:** **NOT AVAILABLE.** No toxin, radiation, pollution, or occupational exposure has been linked.
- **Lifestyle factors:** **NOT AVAILABLE.** No dietary, smoking (obviously), alcohol, or activity association. Sleep is a precipitant of individual seizures (two-thirds occur in sleep, **PMID:16950946**), and sleep deprivation activates the EEG abnormality (ILAE EEG page) — curate these as *seizure precipitants*, not disease-causing environmental factors.
- **Infectious agents:** **NOT AVAILABLE as cause.** The clinically important relationship is the reverse: SeLEAS is repeatedly *mistaken for* CNS infection. Covanis (**PMID:16950946**): *"The clinical features of Panayiotopoulos syndrome are frequently mistaken as nonepileptic conditions such as acute encephalitis, syncope, migraine, cyclic vomiting syndrome, motion sickness, sleep disorder, or gastroenteritis."* Note also that fever is *uncommon* in SeLEAS and is a useful discriminator: Kawakami et al. (**PMID:35153087**) found fever in *"all patients with acute encephalopathy (100%), but less frequently in those with PS (11%, P < 0.001)."*

---

## 6. Mechanism / Pathophysiology

This is where curation needs the most discipline. There is a well-articulated, widely repeated *hypothesis*, and essentially no molecular data. Below is the causal chain as the field states it, with each link labelled by evidence strength.

### 6.1 The proposed causal chain

**Trigger (upstream) → Consequence (downstream):**

1. **Age-dependent, diffuse cortical hyperexcitability** *(maturational, cause unknown)*
   ↓
2. **Ictal discharge of variable lobar onset** — critically, *not* fixed to occipital cortex
   ↓
3. **Propagation to / engagement of the central autonomic network** (insula, anterior cingulate, amygdala, hypothalamus, brainstem autonomic nuclei), which in this age group has a **lower seizure threshold** than cortex
   ↓
4. **Autonomic output discharge** — emetic-center activation, sympathetic/parasympathetic imbalance, hypothalamic thermoregulatory and cardiorespiratory involvement
   ↓
5. **Clinical autonomic seizure**: emesis, pallor, mydriasis, thermoregulatory and cardiorespiratory change, ictal syncope
   ↓
6. **Optional further cortical propagation** → impaired awareness, eye deviation, hemi- or bilateral convulsions (only ~50% of seizures)
   ↓
7. **Age-dependent resolution** of the underlying hyperexcitable state → remission by early-to-mid adolescence

### 6.2 Evidence for each link

**Link 1 (maturational hyperexcitability) — moderate, inferential.** Panayiotopoulos (**PMID:15145296**): *"it is likely that they are due to diffuse maturation-related epileptogenicity activating susceptible-for-children emetic centers and the hypothalamus."* Covanis (**PMID:16950946**) adds the childhood-specificity argument: *"The symptoms/sequence of autonomic seizures and autonomic status epilepticus in Panayiotopoulos syndrome are specific to childhood, and they do not occur in adults."* That is a strong, testable claim — the same discharge in an adult brain does not produce this phenotype.

**Link 2 (variable lobar onset) — strong.** Koutroumanidis (**PMID:17441996**): *"Clinically, PS is manifested by predominantly autonomic seizures and electrographically with multifocal interictal spikes, while the few published ictal recordings have documented onsets of variable lobar topography. These typical electroclinical features do not allow straightforward assignment to a distinctive cortical area, rendering the term 'focal'—as we currently understand it—problematic."* He proposes SeLEAS as a model **"system epilepsy"** — the epilepsy of a *functional system* rather than of a place. Specchio confirms with ictal data: *"Onsets in five ictal EEGs were posterior or anterior-left or right"* (**PMID:20528983**).

**Link 3 (central autonomic network with lower threshold) — moderate, mostly review-level.** Zontek & Paprocka (**PMID:35740751**) is the dedicated review: *"The purpose of this review is to underline the role of central autonomic network dysfunction in the development of Panayiotopoulos syndrome, as well as the possibility of using functional imaging techniques, especially functional magnetic resonance imaging (fMRI), in the diagnostic process. These methods could be crucial for understanding the pathogenesis of PS."* Note the tense: *could be* — the fMRI work has been proposed, not done. Tata et al. (**PMID:24777033**) provide comparative electroclinical support: *"Panayiotopoulos syndrome differs from symptomatic occipital lobe epilepsy and has a unique low epileptogenic threshold related to particular brain circuits."*

**Link 4/5 (autonomic output) — strong at the descriptive level, absent at the molecular level.** Every large series documents the output. Nobody has measured the mediators in SeLEAS patients specifically.

**Link 7 (age-dependent remission) — strong, and now with an EEG correlate.** Oguni's EEG reappraisal (**PMID:37660659**) maps a spatially migrating, age-locked evolution — the mechanism leaves fingerprints as it matures out:

> "The interictal EEG characteristics of SeLEAS are multifocal EEG foci with age-dependent predominant locations; occipital (O) at 2-5 years old, and occipital and frontopolar (synchronous and independent O and Fp spikes) at 4-7 years old and centro-parieto-temporal (CPT) at 6-10 years old. O EEG foci evolve to multifocal EEG foci with a O-Fp or CPT predominance with age and disappear by 12∼16 years old."

That migrating focus is arguably the best single piece of *mechanistic* evidence in the whole literature: whatever is hyperexcitable is not anatomically fixed, and it moves on a developmental clock.

### 6.3 Cellular processes, molecular pathways, protein dysfunction, metabolism, immunity, tissue damage

- **Molecular pathways:** **NOT AVAILABLE.** No KEGG/Reactome pathway has been implicated by data. If SCN1A is invoked (rare cases only), the relevant processes would be sodium-channel-dependent action potential generation and interneuron-mediated inhibition.
- **Cellular processes:** inferred only — excitation/inhibition imbalance in cortical and subcortical circuits.
- **Protein dysfunction:** **NOT AVAILABLE** except in the rare SCN1A families.
- **Metabolic changes:** **NOT AVAILABLE.** No metabolic abnormality; metabolic disease is in fact a *differential diagnosis* to exclude (ILAE lists *"metabolic disorders (especially mitochondrial)"* as a differential).
- **Immune involvement:** **NOT AVAILABLE / not implicated.** SeLEAS is not autoimmune. (For contrast, one pediatric study found elevated anti-GAD antibodies in children with *encephalitis and status epilepticus* — **PMID:22964438** — but this concerns the differential-diagnosis population, not SeLEAS.)
- **Tissue damage mechanisms:** **NONE.** This is a positive, important finding for the entry. Covanis (**PMID:16950946**): *"Autonomic status epilepticus imparts no residual neurologic deficit."* Specchio (**PMID:20528983**) confirms that prolonged seizures do not worsen outcome: *"More than half (55%) of seizures were longer than 30 min but these did not appear to affect remission and number of seizures."* SeLEAS is one of the few conditions in which >30-minute status epilepticus is repeatedly shown to be *harmless*.
- **Biochemical abnormalities:** **NOT AVAILABLE.** No enzyme deficiency, no receptor defect, no established channelopathy.
- **Epigenetic changes:** **NOT AVAILABLE.**

### 6.4 Molecular profiling and advanced technologies

**ALL NOT AVAILABLE.** No transcriptomics, proteomics, metabolomics, lipidomics, single-cell, spatial, multi-omics, or CRISPR/RNAi screen has been performed on SeLEAS. GEO/ArrayExpress/PRIDE/MetaboLights contain no SeLEAS-specific dataset. This should be curated as an explicit knowledge gap, not silently omitted.

**The one emerging quantitative biomarker is electrophysiological, not molecular.** Fujita et al. (**PMID:37918221**) studied scalp-recorded high-frequency oscillations:

> "Thirteen patients (72.2%) had HFOs while five patients (27.8%) had no HFOs in 194 interictal EEG records. … the seizure activity period of the HFOPG was significantly longer than that of the HFONG. Patients with an HFO duration longer than 2 years were intractable to treatment. In most cases, seizures did not occur in the absence of HFOs, even when the spikes remained. … We propose that HFOs are a biomarker of epileptogenicity and an indicator for drug reduction because seizures did not occur if HFOs disappeared even if the spikes remained."

### 6.5 Suggested ontology terms for mechanism nodes

**GO biological processes** (verified via OLS4; use with `modifier` since none are *defective* in a demonstrated sense):

| Term | ID | Suggested modifier | Use for |
|---|---|---|---|
| neuronal action potential | GO:0019228 | INCREASED | Cortical hyperexcitability node |
| regulation of postsynaptic membrane potential | GO:0060078 | ABNORMAL | E/I imbalance node |
| gamma-aminobutyric acid signaling pathway | GO:0007214 | DECREASED | Inhibitory failure (inferred) |
| glutamate receptor signaling pathway | GO:0007215 | INCREASED | Excitatory drive (inferred) |
| sodium ion transmembrane transport | GO:0035725 | ABNORMAL | SCN1A-related cases only |

**CL cell types** (all inferred, not demonstrated — flag as such):
- cerebral cortex neuron — **CL:0010012**
- pyramidal neuron — **CL:0000598**
- GABAergic interneuron — **CL:0011005**
- astrocyte — **CL:0000127** (speculative; include only if a mechanism node requires it)

---

## 7. Anatomical Structures Affected

### Organ level

- **Primary organ:** brain — **UBERON:0000955**. Specifically cerebral cortex — **UBERON:0000956**.
- **Body systems involved:** central nervous system (primary); **autonomic nervous system** (the functional target); cardiovascular and gastrointestinal systems (as autonomic *output* organs, not as sites of disease).
- **Secondary organ involvement:** none structurally. Heart and lungs are affected only transiently and functionally during seizures (bradycardia, apnea, in exceptional cases arrest).

### Regional / tissue level

| Structure | UBERON | Role | Evidence strength |
|---|---|---|---|
| **Occipital lobe** | **UBERON:0002021** | Most frequent site of interictal spikes and of the earliest age-related focus; historically (mis)taken as *the* seat of the syndrome | Strong for EEG localization; **weak** as the mechanistic origin — Ferrie consensus explicitly reclassified PS as *"an autonomic epilepsy, rather than an occipital epilepsy"* (PMID:16483404) |
| **Insular cortex** | **UBERON:0034891** | Central autonomic network hub; electrical stimulation elicits autonomic seizures | Inferred from stimulation/insular-epilepsy literature (PMID:28644201), not from SeLEAS patients |
| **Anterior cingulate cortex** | **UBERON:0009835** | Central autonomic network hub | Inferred |
| **Amygdala** | **UBERON:0001876** | Limbic autonomic node | Inferred |
| **Hypothalamus** | **UBERON:0001898** | Explicitly named by Panayiotopoulos as a target: *"activating susceptible-for-children emetic centers and the hypothalamus"* (PMID:15145296) | Moderate (hypothesis, named in primary source) |
| **Brainstem** | **UBERON:0002298** | Autonomic/cardiorespiratory nuclei; the presumed final common output | Inferred |
| **Nucleus of the solitary tract** | **UBERON:0009050** | Visceral afferent relay, emetic circuitry | Inferred |
| **Area postrema** | **UBERON:0002162** | Chemoreceptor trigger zone / emetic center candidate | Inferred |
| Frontopolar and centro-parieto-temporal cortex | (subregions of UBERON:0000956) | Later age-dependent EEG foci (Oguni, PMID:37660659) | Strong for EEG |

For general context on the network, Edlow et al. (**PMID:26530629**) mapped the human central homeostatic network structurally: *"interconnected brainstem and forebrain nodes form an integrated central homeostatic network (CHN) in the human brain."* This is a healthy-adult connectome study, not SeLEAS — cite as background only.

### Cell and subcellular level

- **Cell populations:** not demonstrated. See §6.5 for inferred CL terms.
- **Subcellular compartments:** **NOT AVAILABLE.** No GO Cellular Component involvement has been established. If SCN1A cases are modeled, plasma membrane / axon initial segment would apply — mark as inference.

### Localization and lateralization

- **Multifocal and shifting** — the defining spatial property. ILAE EEG page: *"Multifocal high voltage spikes or sharp-waves are typically seen, these often are present in different focal areas on sequential EEGs. All focal brain regions may be affected but abnormality is often over the posterior (occipital) regions."*
- **Bilateral involvement over time, unilateral per event.** ILAE: *"Ictal patterns are unilateral, often having posterior onset."*
- **Persistent unifocal abnormality is an ILAE ALERT criterion** — i.e. a focus that stays put suggests a structural lesion, not SeLEAS.

---

## 8. Temporal Development

### Onset

- **Typical age:** 3–6 years (~70% of cases); range 1–14 years (ILAE syndrome page).
- **Peak:** 5 years (**PMID:17442007**); mean 4.6 years (**PMID:24840752**).
- **Onset pattern:** **acute/paroxysmal** at the level of the individual seizure; the epilepsy itself begins abruptly with a first, often dramatic and prolonged, event. There is no prodrome and no insidious phase.
- Earlier onset predicts more seizures: *"Age at onset ranged from 1.1 to 8.6 years, and was earlier in children with more than one seizure"* (**PMID:20528983**).

### Progression and course

- **Course pattern:** **episodic, self-limited**. Not progressive, not relapsing-remitting in the immunological sense.
- **Total duration of active epilepsy:** typically **1–2 years** (ILAE syndrome page).
- **Remission:** spontaneous and age-determined. ILAE course-of-illness criterion: *"Remission by early to mid adolescence. No regression."* ILAE clarifies the term: *"Self-limiting refers to there being a high likelihood of seizures spontaneously remitting at a predictable age."*
- **EEG normalizes later than the clinical course:** spikes *"disappear by 12∼16 years old"* (**PMID:37660659**) — expect EEG abnormality to outlast seizures, and do not treat the EEG.
- **Recurrence kinetics** (Specchio, **PMID:20528983**): *"Cumulative probability of recurrence was 57.6%, 45.6%, 35.1%, and 11.7% at 6, 12, 24, and 36 months, respectively, after the first seizure."* — a clean, curatable natural-history curve.

### Evolution to other syndromes

- **To SeLECTS (Rolandic epilepsy):** ILAE: *"Some patients may evolve to have self-limited epilepsy with centrotemporal spikes."* Caraballo (**PMID:17442007**): *"Sixteen children had concomitant symptoms of rolandic epilepsy and eight developed rolandic seizures after remission of PS seizures."*
- **To DEE-SWAS / electrical status epilepticus in sleep — rare but the key adverse outcome.** Değerliyurt (**PMID:24840752**): *"Evolution to electrical status epilepticus in sleep and Gastaut-type epilepsy were seen in patients with more than ten seizures."* Oguni (**PMID:37660659**): *"O-Fp EEG foci may further evolve to generalized spike-wave complexes and rarely to spike-wave activated in sleep."* Semprino (**PMID:35063695**) reports one such patient. Per ILAE, *"Regression with spike-wave activation in sleep (consider DEE-SWAS)"* is both an **ALERT** and a **course-of-illness EXCLUSIONARY** criterion.
- **Mixed PS/Gastaut phenotypes are common.** Taylor et al. (**PMID:18669497**): *"One-third of the children in this selected series of BOEC did not have a pure syndrome, rather a mixed syndrome with features of both Panayiotopoulos and Gastaut syndromes. … BOEC is an electro-clinical spectrum with Panayiotopoulos and Gastaut syndromes at either end."*

### Critical periods

The 3–6 year window is the vulnerability period; adolescence is the resolution period. There is no intervention window in the disease-modifying sense — treatment does not alter the timeline. Specchio (**PMID:20528983**): *"Thirty-four (58.6%) of 59 patients treated with antiepileptic drugs continued having seizures before ultimate remission."*

---

## 9. Inheritance and Population

### Epidemiology

Two very different-looking numbers circulate, and they measure different things. Curate both, clearly separated.

**Proportion of childhood afebrile seizures (a *fraction*, not a rate):**

Covanis (**PMID:16950946**): *"Panayiotopoulos syndrome probably affects 13% of children aged 3 to 6 years who have had 1 or more afebrile seizures and 6% of such children in the 1- to 15-year age group."* Panayiotopoulos (**PMID:15145296**) gives the same figures: *"They probably affect approximately 13% of children aged 3-6 years with one or more nonfebrile seizures, or 6% in the age group 1-15."* Graziosi (**PMID:31369969**) restates: *"a frequent (6% among children of 1-15 years) and benign epileptic syndrome."*

Specchio's consecutive-referral series gives a slightly lower, arguably cleaner figure (**PMID:20528983**): *"Of 1,794 children aged between 1 and 14 years referred for the first afebrile focal seizure, between January 1992 and December 2004, 93 (5.2%) had PS according to clinical criteria."*

**Population incidence (an actual rate):**

Weir et al. (**PMID:29571057**), the only population-based study: *"The incidence of PS and BECTS was found to be 0.8 and 6.1 per 100,000 <16 year olds, respectively. … The findings suggest BECTS is eight times more common than PS and that the incidence of PS is lower than previously suggested."*

**For dismech `Prevalence` records, this maps to:**

| population | measure_type | prevalence_class | rate_per_100000 | source |
|---|---|---|---|---|
| Children <16 y, NW England & N Wales | ANNUAL_INCIDENCE | BAND_1_9_PER_1000000 | 0.8 | PMID:29571057 |
| Children aged 1–15 y with afebrile seizures | (case fraction, not a population rate — **do not** encode as prevalence) | — | — | PMID:16950946 |

⚠ **Curation warning:** the widely-quoted "6%" and "13%" are *case fractions among children with afebrile seizures*, not population prevalence. Encoding them in a `Prevalence` record with `population: Worldwide` would be a category error. Put them in `notes` or model them as a diagnostic-yield statistic.

UK caseload estimate for planning purposes (Mellish et al., **PMID:25202134**): *"We estimated, annually, 751 new RE cases and 233 PS cases"* in the UK.

### For genetic etiology

- **Inheritance pattern:** **multifactorial / complex**. No Mendelian pattern. ILAE: *"there is no classical inheritance pattern."* HPO mode-of-inheritance term: consider **HP:0010982** (Polygenic inheritance) with `relationship_type: SUSCEPTIBILITY` for any gene, or leave inheritance unbound and describe in prose. Do **not** assert autosomal dominant.
- **Penetrance:** N/A for the syndrome. For the one SCN1A family, penetrance of *any* GEFS+-spectrum phenotype was 88% (16/18), but only 4/18 had the PS phenotype — i.e. penetrance for *this specific phenotype* was ~22% (**PMID:28192756**).
- **Expressivity:** highly variable *within* the one informative family — febrile seizures, FS+, atypical BECTS, and PS all segregated with the same variant.
- **Genetic anticipation:** **NOT AVAILABLE / not applicable** (no repeat expansion mechanism).
- **Germline mosaicism:** **NOT AVAILABLE.**
- **Founder effects:** **NOT AVAILABLE.**
- **Consanguinity:** no established role.
- **Carrier frequency:** **NOT APPLICABLE** (no recessive mechanism).
- **Family history rates:** ILAE: *"There is a higher prevalence of febrile seizures in first degree relatives and case reports of siblings with other self-limited focal epilepsies of childhood."* In the related BECTS comparison cohort, 9.8% of first-degree relatives had seizures (**PMID:23294109**).

### Population demographics

- **Sex ratio:** **1:1**. ILAE: *"Both sexes are affected equally."* (Contrast with the epilepsy-aphasia spectrum, where male predominance is seen — **PMID:23294109**.)
- **Ethnic/geographic distribution:** no population is known to be over- or under-represented. The syndrome has been described in large series from Argentina (n=192, **PMID:17442007**), Italy (n=93, **PMID:20528983**), Turkey (n=38, **PMID:24840752**; n=24, **PMID:24777033**), Japan (**PMID:37660659**, **PMID:35153087**), Brazil (n=36, **PMID:17057874**), the Netherlands (**PMID:32608507**), the UK (**PMID:29571057**), India (**PMID:18515936**), Saudi Arabia (**PMID:21822089**), and Germany (**PMID:42348808**). Panayiotopoulos (**PMID:15145296**) noted it *"has been confirmed worldwide in more than 800 cases."* This global spread with no reported hotspot is itself weak evidence against a founder variant.
- **Age distribution of affected individuals:** essentially all prevalent cases are aged ~1–16 years. Adults do not have this syndrome — Covanis (**PMID:16950946**) is explicit: the autonomic seizure sequence *"do[es] not occur in adults."*

---

## 10. Diagnostics

### 10.1 ILAE 2022 diagnostic criteria (verbatim from epilepsydiagnosis.org, CC BY-SA 4.0, text last updated 2024-06-30)

| Domain | **MANDATORY** | **ALERTS** | **EXCLUSIONARY** |
|---|---|---|---|
| **Seizures** | Focal autonomic seizures | Seizure frequency greater than monthly | — |
| **EEG** | High amplitude focal or multifocal epileptiform abnormality that increases in drowsiness and sleep | Sustained focal slowing (outside the postictal period); persistent unifocal abnormality | — |
| **Age at onset** | — | 8 years | 14 years |
| **Development at onset** | — | Moderate or greater impairment | Regression with spike-wave activation in sleep (consider DEE-SWAS) |
| **Neurological exam** | — | Abnormal exam | — |
| **Imaging** | — | — | Structural cause for the epilepsy |
| **Course of illness** | Remission by early to mid adolescence; no regression | — | Regression with spike-wave activation in sleep (consider DEE-SWAS) |

Additional ILAE notes, verbatim:
> "An MRI is not mandatory for diagnosis but should be considered in the presence of any alerts"
> "An ictal EEG is not required"
> "Syndrome without laboratory confirmation: in resource-limited regions, an interictal EEG is required to diagnose this syndrome"
> "Alert criteria are absent in the vast majority of patients with the syndrome, but rarely can be seen. Their presence should result in caution in diagnosing the syndrome and consideration of other conditions"

### 10.2 Electrophysiology — EEG (the only positive test)

Covanis (**PMID:16950946**): *"An electroencephalogram is the only investigation with abnormal results, usually showing multiple spikes in various brain locations."*

**ILAE EEG description (verbatim):**
- **Background:** *"The background EEG is normal."* Caution: *"Focal slowing consistently over one area is not seen — consider structural brain abnormality."*
- **Interictal:** *"A standard EEG can be normal in some patients. Multifocal high voltage spikes or sharp-waves are typically seen, these often are present in different focal areas on sequential EEGs. All focal brain regions may be affected but abnormality is often over the posterior (occipital) regions."*
- **Activation:** *"EEG abnormality is enhanced by sleep deprivation, in drowsiness and in sleep, when discharges often have a wider field and may be bilaterally synchronous. Eye closure (elimination of central vision and fixation off sensitivity) may activate posterior discharges in some patients."*
- **Ictal:** *"Ictal patterns are unilateral, often having posterior onset, with rhythmic slow (theta or delta) activity intermixed with small spikes and/or fast activity."*

**Quantitative EEG findings from cohorts:**
- Multifocal epileptiform discharges: 79.5% (**PMID:20528983**), 84% (**PMID:24840752**)
- Occipital spikes: 75%; rolandic spikes also present in 25%; normal EEG in 16.6% (**PMID:17057874**)
- Consistently normal EEG: 5.4%; background abnormality only: 16.1% (**PMID:20528983**)
- Non-REM sleep activation in both PS and symptomatic occipital epilepsy; in PS the spikes *"tended to spread mainly to central and centro-temporal regions"* (**PMID:24777033**)
- **Age-dependent spatial migration** (**PMID:37660659**): occipital at 2–5 y → occipital + frontopolar at 4–7 y → centro-parieto-temporal at 6–10 y → gone by 12–16 y. Oguni proposes: *"O-Fp EEG foci may be a specific EEG pattern indicating a diagnosis of SeLEAS."*
- **Emerging:** interictal scalp HFOs as an activity biomarker (**PMID:37918221**) — 72.2% HFO-positive; HFO duration >2 years predicted treatment-refractoriness; *"seizures did not occur if HFOs disappeared even if the spikes remained."*

**NCIT term:** Electroencephalography — **NCIT:C38054**

### 10.3 Imaging

**Normal, and often unnecessary.** ILAE: *"Neuroimaging is normal. If the clinical presentation and EEG is typical for this syndrome, imaging is not required."*

Mellish et al. (**PMID:25202134**) documented over-imaging in UK practice: *"MRI brain at least half the time in 40%-65% cases … Management among respondents is broadly in line with national guidance, although with possible overuse of brain imaging and underuse of EEG and neuropsychological assessments."*

**NCIT term:** Magnetic Resonance Imaging — **NCIT:C16809**

### 10.4 Laboratory tests, biomarkers, biopsy, pathology

**ALL NORMAL / NOT AVAILABLE.** There is no blood, urine, CSF, or tissue abnormality. No biomarker exists. No histopathology exists (no one biopsies this). The main laboratory issue is *avoiding* unnecessary invasive testing — see the misdiagnosis literature below.

### 10.5 Genetic testing

**Not indicated for typical cases.** ILAE: *"There are no established genes, outside of rare case reports, and no clear indication to perform genetic testing."*

Reasonable exceptions, based on Rudolf et al.'s finding that *"atypical SFEC are more likely to have Mendelian inheritance than typical SFEC"* (**PMID:32600977**):
- **Atypical presentation** (regression, spike-wave activation in sleep, drug resistance, alert criteria present) → epilepsy gene panel or WES may be considered, including SCN1A and GRIN2A.
- **Strong family history of GEFS+-spectrum phenotypes** → SCN1A testing may be considered (**PMID:28192756**).
- WGS, CMA, karyotype, FISH, mtDNA testing, repeat expansion testing: **not indicated**.

### 10.6 Omics-based diagnostics

**NONE AVAILABLE OR INDICATED.** No RNA-seq, proteomic, metabolomic, epigenomic, or liquid-biopsy assay is used or under development for SeLEAS.

### 10.7 Differential diagnosis

**ILAE list (verbatim):**
- *"Focal autonomic seizures due to structural brain abnormality"*
- *"Migraine associated disorders including benign paroxysmal vertigo"*
- *"Disorders associated with intermittent encephalopathy e.g. metabolic disorders (especially mitochondrial)"*
- *"Disorders associated with intermittent vomiting e.g. gastrointestinal disorders"*

**Extended literature list with distinguishing features:**

| Mimic | Distinguishing features | Source |
|---|---|---|
| **Acute encephalitis / encephalopathy** | Fever present in 100% of encephalopathy vs 11% of PS; convulsions ≥15 min in 90% vs 17%; PS seizures stop with midazolam 0.1 mg/kg while encephalopathy needs ≥0.3 mg/kg; vomiting 78% (PS) vs 3% | **PMID:35153087** |
| **Migraine / childhood headache** | Best-quantified mimic. In 186 children referred for "migraine"/"headache", *"18.8% (n = 35) of pediatric patients initially diagnosed with 'migraine' or 'headache' received a possible, probable, or definite diagnosis of benign focal epilepsy with autonomic seizures"*; 6.5% received a definite SeLEAS diagnosis | **PMID:42348808** |
| **Syncope (cardiogenic/vasovagal)** | Ictal syncope in PS is accompanied by other autonomic features and often follows emesis | **PMID:16950946** |
| **Cyclic vomiting syndrome / gastroenteritis / GERD** | PS has associated eye deviation, impaired awareness, EEG spikes | **PMID:31369969**, **PMID:16950946** |
| **Motion sickness, sleep disorders, metabolic disease** | Listed mimics | **PMID:16950946**, **PMID:17464469** |
| **Gastaut syndrome (childhood occipital visual epilepsy)** | Later onset, brief seizures, prominent *visual* symptoms (visual symptoms in only ~5% of PS), postictal headache; neuropsychologically distinguishable (PS worse on performance IQ, visual memory, reading) | **PMID:31398558**, **PMID:24840752** |
| **Symptomatic occipital lobe epilepsy** | Earlier onset (3.4 vs 5.6 y), fewer autonomic seizures (43.5% vs 87.5%), less ictal syncope (13% vs 37.5%), lesion on MRI | **PMID:24777033** |

The framing sentence for the entry (Parisi et al., **PMID:17464469**): *"The peculiar aspects should be known not only by epileptologists but also by general doctors because a correct diagnosis would avoid aggressive interventions and concerns on account of its benign outcome."*

### 10.8 Screening

**NOT APPLICABLE.** No newborn screening, carrier screening, or cascade screening exists or is warranted. Graziosi et al. (**PMID:31369969**) do make a service-level suggestion: *"The availability of electroencephalography (EEG) recording in pediatric Emergency Departments might be useful for a prompt and not-cost-consuming diagnosis."*

---

## 11. Outcome / Prognosis

### Survival and mortality

- **Life expectancy: normal.** No excess mortality attributable to SeLEAS has been demonstrated in any cohort.
- **Disease-specific mortality:** no deaths from SeLEAS are reported in the major series (Caraballo n=192, Specchio n=93, Değerliyurt n=38, Tedrus n=36 — zero deaths across all).
- **The one theoretical risk is ictal cardiorespiratory arrest.** Covanis (**PMID:16950946**): *"Cardiorespiratory arrest is exceptional"* and *"autonomic seizures are potentially life-threatening in the rare context of cardiorespiratory arrest, an area in which additional study is required."*
  - Mujawar et al. (**PMID:21822089**): *"ictal cardiorespiratory arrest is extremely rare, with only 4 cases being reported in literature. All 4 cases reported in literature recovered spontaneously and did not require resuscitation. Here we present a 3½-year-old male child with Panayiotopoulos syndrome who presented with status epilepticus and ictal cardiorespiratory arrest requiring cardiopulmonary resuscitation for revival."*
  - Yamamoto et al. (**PMID:29926008**), a 10-year-old resuscitated after ictal cardiac arrest: *"Lifethreating cardiopulmonary arrest is rare in PS, but long seizure duration of PS may associate with apnea and bradycardia."*
  - Semprino et al. (**PMID:35063695**): 2/44 patients in an *atypical-presentation* series — *"Two children (4.8%) had their first seizure while asleep associated with cardiorespiratory arrest."* Note the denominator is enriched for atypia.
- **A second, iatrogenic mortality pathway is explicitly flagged.** Covanis (**PMID:16950946**): *"Autonomic status epilepticus in the acute stage needs thorough evaluation; aggressive treatment may cause iatrogenic complications including cardiorespiratory arrest."* Over-treating this condition can hurt the child more than the condition does. This belongs in the entry as a treatment-safety node.

### Morbidity and function

- **No residual neurological deficit.** Covanis (**PMID:16950946**): *"Autonomic status epilepticus imparts no residual neurologic deficit."*
- **Risk of adult epilepsy is not elevated.** Covanis: *"The risk of epilepsy in adult life seems to be no higher than in the general population."*
- **Possible mild cognitive/academic morbidity** — see §3.3. Contested. The strongest claim (**PMID:32608507**): *"Mild-to-severe academic underachievement was present in more than half of the children with Panayiotopoulos syndrome."* The largest cohort (**PMID:20528983**) does not support clinically meaningful impairment.
- **QoL measures:** no disease-specific instrument data. See §3.5.

### Disease course and complications

- **Complications:** autonomic status epilepticus (common, benign); evolution to DEE-SWAS or Gastaut syndrome (rare, associated with >10 seizures — **PMID:24840752**); ictal cardiorespiratory arrest (exceptional); misdiagnosis-driven iatrogenic harm (common and underappreciated).
- **Recovery potential:** complete, with or without treatment. Mujawar (**PMID:21822089**): *"Recovery from this autonomic status epilepticus is within hours and is always complete."*

### Prognostic factors

| Factor | Direction | Source |
|---|---|---|
| Earlier age at onset | → more seizures | PMID:20528983 |
| >10 lifetime seizures | → risk of evolution to ESES / Gastaut syndrome | PMID:24840752 |
| Seizure duration >30 min | → **no** effect on remission or seizure count (i.e. *not* prognostic) | PMID:20528983 |
| Interictal HFO duration >2 years | → treatment refractoriness | PMID:37918221 |
| HFO disappearance | → seizure freedom even with persisting spikes; candidate drug-withdrawal indicator | PMID:37918221 |
| Alert criteria present (abnormal exam, developmental impairment, focal slowing, persistent unifocal spikes) | → reconsider the diagnosis | ILAE 2022 |

Overall summary (Specchio, **PMID:20528983**): *"PS is a uniform childhood susceptibility to autonomic seizures that is related to early age of development and with excellent prognosis with regard to seizure remission and neuropsychological development."*

---

## 12. Treatment

### 12.1 The central treatment fact: often, no treatment

Covanis (**PMID:16950946**): *"Education about Panayiotopoulos syndrome is the cornerstone of management. Prophylactic treatment with antiepileptic medication may not be needed for most patients."*

Vigevano et al. (**PMID:23622206**), on self-limited focal epilepsies generally: *"These entities are age-dependent and seizures tend to disappear spontaneously. For these reasons often the drug treatment is not necessary."*

UK practice reality (Mellish et al., **PMID:25202134**): *"Clinicians reported non-treatment in 40%: main reasons were low frequency of seizures and parent/child preferences."*

Efficacy caveat — treatment does not reliably prevent seizures either (Specchio, **PMID:20528983**): *"Thirty-four (58.6%) of 59 patients treated with antiepileptic drugs continued having seizures before ultimate remission."* And most patients who *are* treated need only one drug (Değerliyurt, **PMID:24840752**): *"Two or more antiepileptic drugs were required in only 13% of the patients."*

### 12.2 Pharmacotherapy

**⚠ There is no randomized controlled trial of any drug in SeLEAS.** Drug choice is by clinician preference and extrapolation from focal epilepsy. Mellish et al. (**PMID:25202134**) surveyed UK preference explicitly to design a future trial: *"Carbamazepine is the preferred older, and levetiracetam the preferred newer, RCT arm."*

| Treatment | `treatment_term` (NCIT) | `therapeutic_agent` (CHEBI verified) | `therapeutic_modality` | Evidence |
|---|---|---|---|---|
| **Carbamazepine** | Pharmacotherapy — NCIT:C15986 | carbamazepine — **CHEBI:3387** | SMALL_MOLECULE | Preferred older agent, UK survey (PMID:25202134) |
| **Levetiracetam** | Pharmacotherapy — NCIT:C15986 | levetiracetam — **CHEBI:6437** | SMALL_MOLECULE | Preferred newer agent, UK survey (PMID:25202134) |
| **Oxcarbazepine** | Pharmacotherapy — NCIT:C15986 | oxcarbazepine — **CHEBI:7824** | SMALL_MOLECULE | Common practice; no SeLEAS-specific evidence |
| **Valproic acid** | Pharmacotherapy — NCIT:C15986 | valproic acid — **CHEBI:39867** | SMALL_MOLECULE | Common practice; no SeLEAS-specific evidence |
| **Clobazam** | Pharmacotherapy — NCIT:C15986 | clobazam — **CHEBI:31413** | SMALL_MOLECULE | Practice; no SeLEAS-specific evidence |
| **Sultiame** | Pharmacotherapy — NCIT:C15986 | Sultiame — **CHEBI:32171** | SMALL_MOLECULE | Used in European practice for self-limited focal epilepsies |
| **Midazolam (acute/rescue)** | Pharmacotherapy — NCIT:C15986 | midazolam — **CHEBI:6931** | SMALL_MOLECULE | **Best-supported acute intervention** — see below |
| **Diazepam (rescue)** | Pharmacotherapy — NCIT:C15986 | diazepam — **CHEBI:49575** | SMALL_MOLECULE | Standard home rescue for prolonged seizures |

Alternative generic term: Anticonvulsant Therapy — **NCIT:C64172**; Anticonvulsant Agent — **NCIT:C264**.

**The one quantitatively supported acute-treatment finding** (Kawakami et al., **PMID:35153087**): *"seizures were treatable in all patients with PS with a small dose of midazolam (0.1 mg/kg), but all patients with acute encephalopathy required midazolam at 0.3 mg/kg or more (P < 0.001)."* This doubles as a therapeutic and a diagnostic observation — SeLEAS status is unusually benzodiazepine-responsive.

**Safety flag for sodium-channel blockers.** Pasini et al. (**PMID:35151939**) report iatrogenic ictal asystole with carbamazepine and phenytoin: *"The clear relationship between ictal arrhythmia and sodium channels blockers may be related to the negative chronotropic and inotropic cardiac effects."* Given that SeLEAS already carries a rare ictal-bradycardia/asystole risk, this interaction deserves an explicit note — the cases were in pharmacoresistant focal epilepsy, not SeLEAS, so mark as an extrapolated caution.

### 12.3 Management of autonomic status epilepticus

Ferrie et al.'s consensus definition (**PMID:17442005**) is the reference standard:

> "Autonomic SE is a condition lasting at least 30 min and characterized by epileptic activity causing altered autonomic function of any type at seizure onset or in which manifestations consistent with altered autonomic function are prominent (quantitatively dominant or clinically important) even if not present at seizure onset. It is best described, and probably most commonly encountered in children, with Panayiotopoulos syndrome. … Its pathogenesis and most appropriate management are poorly understood."

Management principles: evaluate thoroughly, treat gently. Covanis (**PMID:16950946**): *"Autonomic status epilepticus in the acute stage needs thorough evaluation; aggressive treatment may cause iatrogenic complications including cardiorespiratory arrest."*

### 12.4 Pharmacogenomics

**NOT AVAILABLE** for SeLEAS specifically. The general pediatric epilepsy PGx caveats apply: HLA-B*15:02 screening before carbamazepine in at-risk ancestries (CPIC), and CYP2C9/CYP2C19 effects on phenytoin and valproate metabolism. None is SeLEAS-specific.

### 12.5 Advanced therapeutics

**ALL NOT APPLICABLE.** No gene therapy, cell therapy, RNA-based therapy, targeted therapy, or immunotherapy is under development or would be justified for a condition that remits on its own within 1–2 years.

### 12.6 Surgical and interventional

**NOT INDICATED.** Epilepsy surgery has no role. The syndrome has no resectable focus (the foci shift), no lesion, and self-resolves. (For context on when surgery *is* considered in other pediatric epilepsies, see **PMID:34620459** — SeLEAS is not among them.)

### 12.7 Supportive, rehabilitative, and educational

| Intervention | NCIT term | ID | Rationale |
|---|---|---|---|
| **Patient/family education** | Patient Education | **NCIT:C16959** | *"Education about Panayiotopoulos syndrome is the cornerstone of management"* (PMID:16950946) — this is arguably the **primary treatment** |
| Supportive care | Supportive Care | **NCIT:C15747** | Seizure action plan, rescue medication training, positioning/airway during prolonged seizures |
| Neuropsychological assessment | (no clean NCIT clinical-action term; use free-text `preferred_term`) | — | Underused per PMID:25202134 (*"neuropsychological evaluation in 7%-8%"*); warranted given the cognitive-comorbidity literature |
| Educational/academic support | (no NCIT term; free text) | — | Justified by PMID:32608507 (8–11 month academic lag), PMID:26709104 |
| Genetic counseling | Genetic Counseling | **NCIT:C15240** | Rarely indicated; only for atypical/familial cases |

### 12.8 Experimental treatments and clinical trials

**NO REGISTERED TRIALS.** A ClinicalTrials.gov API v2 query (`query.cond=Panayiotopoulos` and `query.term=Panayiotopoulos`, retrieved 2026-08-05) returned **zero studies**. Curate `clinical_trials:` as empty and note the absence explicitly — it is informative, not an omission.

Mellish et al. (**PMID:25202134**) exist precisely to argue this gap should be closed: *"Considerable international variation in management and controversy about non-treatment indicate the need for high quality randomised controlled trials (RCT)… Approximately one-half considered active and placebo designs acceptable, choosing seizures as primary and cognitive/behavioural measures as secondary outcomes."*

### 12.9 Treatment strategy

A defensible algorithm from the literature:

1. **Diagnose correctly** (clinical picture + interictal EEG). Avoid LP, empiric aciclovir, ICU admission where the picture is typical.
2. **Educate the family**; provide a written seizure action plan.
3. **Provide home rescue medication** (benzodiazepine) for seizures lasting >5 min, given that half exceed 30 min.
4. **Withhold maintenance ASM** in most children — ~40% of UK clinicians do (**PMID:25202134**); 25% of children have only one seizure ever (ILAE).
5. **Start maintenance ASM** for frequent seizures (>monthly is an ILAE alert), multiple prolonged episodes, or high family anxiety. First-line by practice preference: carbamazepine/oxcarbazepine or levetiracetam.
6. **Withdraw** after ~2 seizure-free years; consider HFO disappearance as a supporting indicator (**PMID:37918221**). Do not treat the EEG — spikes persist until 12–16 years.
7. **Re-evaluate the diagnosis** if any ILAE alert appears, particularly regression with sleep-activated spike-wave (→ DEE-SWAS).

**Personalized medicine approaches:** **NOT AVAILABLE.** No genotype-guided treatment exists.

---

## 13. Prevention

- **Primary prevention:** **NOT POSSIBLE / NOT APPLICABLE.** No modifiable risk factor exists.
- **Secondary prevention (early detection):** the meaningful target is **prevention of misdiagnosis**, not prevention of disease. The concrete proposal in the literature is ED access to EEG (**PMID:31369969**). Berg et al. (**PMID:42348808**) add a second detection target: *"When evaluating children and adolescents with headache, clinicians should give greater consideration to SeLEAS as a differential diagnosis than in the past, especially due to its significant therapeutic implications."*
- **Tertiary prevention (complication prevention):**
  - Rescue benzodiazepine to abort prolonged seizures and reduce autonomic status duration (linked to the apnea/bradycardia risk, **PMID:29926008**).
  - Avoiding over-aggressive acute treatment, which can itself precipitate cardiorespiratory arrest (**PMID:16950946**).
  - Monitoring for evolution to DEE-SWAS in children with >10 seizures (**PMID:24840752**).
- **Immunization:** **NOT APPLICABLE.** No vaccine-preventable component. (There is no evidence linking vaccination to SeLEAS onset either.)
- **Screening programs / genetic screening / PGD / prenatal testing:** **NOT APPLICABLE.** No causal gene; recurrence risk is not quantified beyond a general familial enrichment of febrile seizures.
- **Risk stratification:** **NOT AVAILABLE.** No validated risk model.
- **Behavioral interventions:** none established. A single small pilot in the sibling syndrome BECTS suggested structured exercise improved neurocognitive and internalizing-behavior outcomes (**PMID:25025685**) — hypothesis-generating only, not performed in SeLEAS.
- **Counseling:** reassurance-focused counseling about excellent prognosis is the highest-value "preventive" act, since the documented harms of this condition are largely those of misdiagnosis and family distress.
- **Public health / environmental interventions:** **NOT APPLICABLE.**
- **Prophylaxis:** maintenance ASM is the only prophylactic option and is explicitly optional (§12).

---

## 14. Other Species / Natural Disease

**NO NATURAL ANIMAL COUNTERPART IS KNOWN.** This should be curated as an explicit negative.

- **Taxonomy:** *Homo sapiens* — **NCBITaxon:9606** — only.
- **Breed (VBO):** **NOT APPLICABLE.**
- **Orthologous genes:** since no causal gene exists, orthology is moot. If SCN1A is curated as a rare susceptibility gene, orthologs exist (mouse *Scn1a*, NCBI Gene 20265; zebrafish *scn1lab*), but they model Dravet/GEFS+ rather than SeLEAS.
- **Natural disease in other species:** **NOT AVAILABLE.** No OMIA entry corresponds to SeLEAS. Idiopathic epilepsy is common in dogs (many breeds) but no canine syndrome with age-dependent autonomic/emetic seizures and spontaneous remission has been characterized as a SeLEAS analog.
- **Veterinary relevance:** none.
- **Comparative pathology:** **NOT AVAILABLE.** The barrier is conceptual as well as practical — the phenotype is defined by a developmental window and by symptoms (nausea, feeling unwell, awareness of retching) that are difficult to ascertain in an animal.
- **Evolutionary conservation of mechanism:** the *substrate* (central autonomic network, brainstem–forebrain homeostatic circuitry) is deeply conserved (**PMID:26530629** describes the human structural connectome of this network and notes species differences: *"a lateral forebrain bundle, whose connectivity is distinct from that of rodents and nonhuman primates, is the primary conduit for connections between the brainstem and medial temporal lobe"*). The *syndrome*, however, is not known to be conserved.
- **Zoonotic potential / cross-species susceptibility:** **NOT APPLICABLE** (non-infectious).

---

## 15. Model Organisms

**NO MODEL OF SeLEAS EXISTS.** This is a firm negative and should be curated as one, with a `KNOWLEDGE_GAP` discussion attached.

### Why no model exists

Three structural obstacles, worth recording because they explain the gap rather than merely noting it:

1. **No causal gene to engineer.** You cannot make a knock-in without a variant.
2. **The defining feature is a developmental time-course** (onset 3–6 human years, remission within 1–2 years, EEG normalization by 12–16 years). Mapping that window onto rodent development is non-trivial.
3. **The cardinal symptom is emesis, and rodents cannot vomit.** Mice and rats lack the brainstem emetic reflex circuitry required for vomiting — so the single most characteristic phenotype of this syndrome is unobservable in the default mammalian model. Any model would need a ferret, shrew, or non-human primate, none of which is a practical epilepsy-genetics platform.

### Adjacent models that are *not* models of SeLEAS

Curate these only if the entry needs a `HUMAN_MODEL_MISMATCH` discussion — they are relevant background, not evidence for SeLEAS mechanism:

| Model | Relationship | Caveat |
|---|---|---|
| *Scn1a*<sup>+/−</sup> and *Scn1a* knock-in mice (MGI) | Model GEFS+/Dravet, the spectrum into which the single SeLEAS family's variant falls (**PMID:28192756**) | Model severe phenotypes; do not recapitulate self-limited autonomic seizures or spontaneous remission |
| *Grin2a* mouse models | Model the epilepsy-aphasia continuum | Explicitly a *different* syndrome; the SeLEAS exome cohort was GRIN2A-negative by design (**PMID:32600977**) |
| Kindling / kainate rodent models of focal epilepsy | Generic focal epileptogenesis | No autonomic-predominant, age-remitting phenotype |

### Model types, genetic models, phenotype recapitulation, applications, resources

- **Model organism type:** none available (mammalian, invertebrate, cellular, and in vitro all **NOT AVAILABLE**).
- **Specific systems (iPSC, organoid, cell line):** **NOT AVAILABLE.** No SeLEAS patient-derived iPSC line is registered in Cellosaurus or comparable resources.
- **Induced models:** **NOT AVAILABLE.**
- **Genetic models (KO/KI/transgenic/conditional/humanized):** **NOT AVAILABLE.**
- **Phenotype recapitulation:** N/A.
- **Model limitations:** see the three obstacles above.
- **Research applications:** the tractable research substrate for SeLEAS is *human electrophysiology* (longitudinal EEG, HFO quantification, source localization) and *human functional imaging* (the fMRI approach proposed but not yet executed by Zontek & Paprocka, **PMID:35740751**), not animal modeling.
- **Model databases:** MGI, RGD, ZFIN, IMPC, IMSR contain no SeLEAS-associated allele or phenotype annotation.

---

## Appendix A — Summary of proposed dismech `mechanistic_hypotheses`

Because the mechanism is entirely hypothetical, I recommend curating it as competing hypotheses rather than a settled chain:

| `hypothesis_group_id` | Label | Status | Content | Key evidence |
|---|---|---|---|---|
| `maturational_autonomic_susceptibility` | Diffuse maturation-related epileptogenicity activating low-threshold autonomic centers | **CANONICAL** | Age-dependent diffuse cortical hyperexcitability engages emetic centers and hypothalamus; the syndrome is not occipital | PMID:15145296, PMID:16950946, PMID:16483404 |
| `system_epilepsy_model` | SeLEAS as a "system epilepsy" of the central autonomic network rather than a lobar focal epilepsy | **ALTERNATIVE / complementary** | Variable lobar ictal onset + multifocal interictal spikes make "focal" the wrong frame; the epilepsy belongs to a functional system | PMID:17441996, PMID:24777033 |
| `occipital_origin_model` | Early-onset benign *occipital* epilepsy | **SUPERSEDED** | The original 1989 framing; formally rejected by the 2006 consensus and the 2022 ILAE nomenclature | PMID:16483404 (refutes), PMID:19469846 (history) |

And suggested `discussions`:

- **`KNOWLEDGE_GAP`** — Are cognitive and behavioral comorbidities real, or an artifact of tertiary-referral bias? (attaches to the cognitive phenotype nodes; PMID:32608507 & PMID:31398558 vs PMID:20528983; commentary PMID:31909486)
- **`KNOWLEDGE_GAP`** — What is the molecular basis of the age-dependent hyperexcitability, and what causes remission? No omics, no model, no gene. Proposed experiments: longitudinal HFO/source-localization studies (PMID:37918221), the fMRI central-autonomic-network protocol proposed in PMID:35740751.
- **`KNOWLEDGE_GAP`** — Which drug, if any? No RCT has ever been performed (PMID:25202134 explicitly proposes the trial design).
- **`HUMAN_MODEL_MISMATCH`** — SCN1A mouse models exist but model Dravet/GEFS+, not SeLEAS; and rodents cannot vomit, so the cardinal phenotype is unmodellable in the standard platform.

---

## Appendix B — Verified ontology term quick reference

All terms below were verified against live OLS4 (EBI) on 2026-08-05. **Verify again with `just validate-terms` before committing** — this list is a curation aid, not a substitute for the validator.

**MONDO:** MONDO:0020307 (Self-limited epilepsy with autonomic seizures)

**HP:** HP:0011154 · HP:0032740 · HP:0032755 · HP:0011159 · HP:0032761 · HP:0032773 · HP:0002013 · HP:0002018 · HP:0000980 · HP:0000961 · HP:0011499 · HP:0000549 · HP:0002384 · HP:0001279 · HP:0002133 · HP:0032861 · HP:0007334 · HP:0006813 · HP:0003781 · HP:0000020 · HP:0002315 · HP:0002104 · HP:0001662 · HP:0010841 · HP:0012016 · HP:0012557 · HP:0025644 · HP:0002353 · HP:0025373 · HP:0002270 · HP:0001328 · HP:0010794 · HP:0007018 · HP:0000739 · HP:0002373 (febrile seizure, for the family-history/antecedent phenotype)

**GO:** GO:0019228 · GO:0060078 · GO:0007214 · GO:0007215 · GO:0035725

**CL:** CL:0010012 · CL:0000598 · CL:0011005 · CL:0000127

**UBERON:** UBERON:0000955 · UBERON:0000956 · UBERON:0002021 · UBERON:0034891 · UBERON:0009835 · UBERON:0001876 · UBERON:0001898 · UBERON:0002298 · UBERON:0009050 · UBERON:0002162 · UBERON:0001759

**CHEBI:** CHEBI:3387 · CHEBI:6437 · CHEBI:7824 · CHEBI:39867 · CHEBI:31413 · CHEBI:6931 · CHEBI:49575 · CHEBI:32171

**NCIT:** NCIT:C15986 · NCIT:C64172 · NCIT:C264 · NCIT:C38054 · NCIT:C16809 · NCIT:C16959 · NCIT:C15747 · NCIT:C15240

**HGNC:** hgnc:10585 (SCN1A) — susceptibility only, rare families

---

## Appendix C — Priority citations with verified abstract quotes

These are the highest-value evidence items for the entry. Every quote below is copied verbatim from the PubMed abstract as retrieved via NCBI E-utilities on 2026-08-05; each should still be run through `just fetch-reference` + `just validate-references` before committing.

| PMID | Short handle | Best-use quote (verbatim) |
|---|---|---|
| **16950946** | Covanis 2006, *Pediatrics* — the single richest source | "Half of the seizures in Panayiotopoulos syndrome last for >30 minutes, thus constituting autonomic status epilepticus, which is the more common nonconvulsive status epilepticus in normal children. Two thirds of seizures occur during sleep." |
| **16950946** | (epidemiology) | "Panayiotopoulos syndrome probably affects 13% of children aged 3 to 6 years who have had 1 or more afebrile seizures and 6% of such children in the 1- to 15-year age group." |
| **16950946** | (pathophysiology) | "Ictal epileptic discharges in Panayiotopoulos syndrome, irrespective of their location at onset, activate autonomic disturbances and emesis, to which children are particularly vulnerable." |
| **16483404** | Ferrie 2006 consensus | "We conclude that PS is a common idiopathic, benign seizure disorder of childhood, which should be classified as an autonomic epilepsy, rather than an occipital epilepsy." |
| **35503717** | ILAE 2022 nosology | "self-limited focal epilepsies, comprising four syndromes: self-limited epilepsy with centrotemporal spikes, self-limited epilepsy with autonomic seizures, childhood occipital visual epilepsy, and photosensitive occipital lobe epilepsy" |
| **20528983** | Specchio 2010, n=93 | "Of 1,794 children aged between 1 and 14 years referred for the first afebrile focal seizure, between January 1992 and December 2004, 93 (5.2%) had PS according to clinical criteria." |
| **20528983** | (seizure duration is not prognostic) | "More than half (55%) of seizures were longer than 30 min but these did not appear to affect remission and number of seizures." |
| **17442007** | Caraballo 2007, n=192 | "Eighty-four (44.2%) had a single seizure, 79 (41.2%) had 2-5 fits, and 28 (14.6%) had frequent seizures." |
| **29571057** | Weir 2018, incidence | "The incidence of PS and BECTS was found to be 0.8 and 6.1 per 100,000 <16 year olds, respectively." |
| **17441996** | Koutroumanidis 2007, "system epilepsy" | "These typical electroclinical features do not allow straightforward assignment to a distinctive cortical area, rendering the term 'focal'--as we currently understand it--problematic." |
| **37660659** | Oguni 2023, EEG reappraisal | "The interictal EEG characteristics of SeLEAS are multifocal EEG foci with age-dependent predominant locations; occipital (O) at 2-5 years old, and occipital and frontopolar (synchronous and independent O and Fp spikes) at 4-7 years old and centro-parieto-temporal (CPT) at 6-10 years old." |
| **28192756** | Kivity 2017, SCN1A | "A pathogenic heterozygous SCN1A (c.2624C>A; p.Thr875Lys) variant was identified. Sixteen of the 18 variant positive family members were affected (88% penetrance)" |
| **18669497** | Taylor 2008, twins | "Monozygotic twin pairs did not show a higher concordance rate than dizygotic twin pairs suggesting that BOEC may not be a purely genetic disorder." |
| **32600977** | Rudolf 2020, exome | "Our results further illustrate the fact that atypical SFEC are more likely to have Mendelian inheritance than typical SFEC." |
| **35153087** | Kawakami 2022, vs encephalopathy | "seizures were treatable in all patients with PS with a small dose of midazolam (0.1 mg/kg), but all patients with acute encephalopathy required midazolam at 0.3 mg/kg or more (P < 0.001)" |
| **17442005** | Ferrie 2007, autonomic SE definition | "Autonomic SE is a condition lasting at least 30 min and characterized by epileptic activity causing altered autonomic function of any type at seizure onset" |
| **32608507** | Fonseca Wald 2020, cognition | "Children with Panayiotopoulos syndrome demonstrated diffuse cognitive dysfunction in full-scale IQ, performance IQ, visual attention, visual-motor integration, and verbal memory." |
| **25202134** | Mellish 2015, UK practice | "Clinicians reported non-treatment in 40%: main reasons were low frequency of seizures and parent/child preferences. Carbamazepine is the preferred older, and levetiracetam the preferred newer, RCT arm." |
| **37918221** | Fujita 2023, HFO biomarker | "seizures did not occur if HFOs disappeared even if the spikes remained" |
| **42348808** | Berg 2026, migraine mimicry | "In total, 18.8% (n = 35) of pediatric patients initially diagnosed with 'migraine' or 'headache' received a possible, probable, or definite diagnosis of benign focal epilepsy with autonomic seizures." |
| **21822089** | Mujawar 2011, cardiorespiratory arrest | "ictal cardiorespiratory arrest is extremely rare, with only 4 cases being reported in literature." |
| **35871494** | Cooper 2023, cerebral palsy variant | "Self-limited focal epilepsy-variant usually manifested with a mix of autonomic and brachio-facial motor features, and occipital and/or centro-temporal spikes on EEG." |
| **35063695** | Semprino 2022, unusual presentations | "Twelve patients (29.2%) had ictal syncope or syncope-like epileptic seizures." |
| **24840752** | Değerliyurt 2014, Turkish series | "Evolution to electrical status epilepticus in sleep and Gastaut-type epilepsy were seen in patients with more than ten seizures." |
| **31369969** | Graziosi 2019, misdiagnosis | "The consequences are high morbidity, costly mismanagement, and stress for children and their parents." |
| **35740751** | Zontek & Paprocka 2022, CAN review | "The purpose of this review is to underline the role of central autonomic network dysfunction in the development of Panayiotopoulos syndrome" |
| **31398558** | Akca Kalem 2019, PS vs Gastaut | "Cognitive dysfunction is a more prominent and widespread feature of the patients with PS; whereas, the patients with GS suffer only from milder and isolated cognitive problems." |
| **24777033** | Tata 2014, PS vs symptomatic OLE | "Panayiotopoulos syndrome differs from symptomatic occipital lobe epilepsy and has a unique low epileptogenic threshold related to particular brain circuits." |
| **37714124** | Quito-Betancourt 2023, nomenclature | "Using the term 'benign' to refer to them is no longer recommended, as this would ignore the comorbidities some individuals suffer." |

---

## Sources

- [MONDO:0020307 via OLS4 (EMBL-EBI)](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0020307)
- [ILAE — Self-Limited Epilepsy with Autonomic Seizures (SeLEAS): overview, EEG, imaging, genetics, diagnostic criteria, differential diagnoses](https://www.epilepsydiagnosis.org/syndrome/panayiotopoulos-overview.html) (CC BY-SA 4.0; text last updated 2024-06-30)
- [Specchio et al. 2022, ILAE classification of childhood-onset epilepsy syndromes — PMID:35503717](https://pubmed.ncbi.nlm.nih.gov/35503717/)
- [Covanis 2006, *Pediatrics* — PMID:16950946](https://pubmed.ncbi.nlm.nih.gov/16950946/)
- [Ferrie et al. 2006 consensus — PMID:16483404](https://pubmed.ncbi.nlm.nih.gov/16483404/)
- [Ferrie et al. 2007, autonomic status epilepticus consensus — PMID:17442005](https://pubmed.ncbi.nlm.nih.gov/17442005/)
- [Specchio et al. 2010, 93 consecutive patients — PMID:20528983](https://pubmed.ncbi.nlm.nih.gov/20528983/)
- [Caraballo et al. 2007, 192 patients — PMID:17442007](https://pubmed.ncbi.nlm.nih.gov/17442007/)
- [Weir et al. 2018, comparative incidence — PMID:29571057](https://www.seizure-journal.com/article/S1059-1311(17)30791-4/fulltext)
- [Koutroumanidis 2007, benign childhood system epilepsy — PMID:17441996](https://pubmed.ncbi.nlm.nih.gov/17441996/)
- [Oguni 2023, reappraisal of interictal EEG — PMID:37660659](https://www.ejpn-journal.com/article/S1090-3798(23)00132-0/abstract)
- [Kivity et al. 2017, SCN1A spectrum — PMID:28192756](https://pubmed.ncbi.nlm.nih.gov/28192756/)
- [Rudolf et al. 2020, exome sequencing in SFEC — PMID:32600977](https://pubmed.ncbi.nlm.nih.gov/32600977/)
- [Taylor et al. 2008, benign occipital epilepsies twin/family study — PMID:18669497](https://pubmed.ncbi.nlm.nih.gov/18669497/)
- [Kawakami et al. 2022, differentiating PS from acute encephalopathy — PMID:35153087](https://pubmed.ncbi.nlm.nih.gov/35153087/)
- [Fonseca Wald et al. 2020, neurocognitive profile — PMID:32608507](https://pubmed.ncbi.nlm.nih.gov/32608507/)
- [Mellish et al. 2015, UK practice survey and trial feasibility — PMID:25202134](https://pubmed.ncbi.nlm.nih.gov/25202134/)
- [Fujita et al. 2023, scalp HFOs — PMID:37918221](https://pubmed.ncbi.nlm.nih.gov/37918221/)
- [Berg et al. 2026, SeLEAS vs childhood migraine — PMID:42348808](https://www.neurology.org/doi/10.1212/CPJ.0000000000200630)
- [Zontek & Paprocka 2022, GI/autonomic symptoms and the central autonomic network — PMID:35740751](https://pmc.ncbi.nlm.nih.gov/articles/PMC9222198/)
- [Cooper et al. 2023, epilepsy syndromes in cerebral palsy — PMID:35871494](https://pubmed.ncbi.nlm.nih.gov/35871494/)
- [Panayiotopoulos 2004, autonomic seizures and autonomic status epilepticus — PMID:15145296](https://pubmed.ncbi.nlm.nih.gov/15145296/)
- [Graziosi et al. 2019, misdiagnosis and pitfalls — PMID:31369969](https://pubmed.ncbi.nlm.nih.gov/31369969/)
- [Quito-Betancourt & Reyes Valenzuela 2023, self-limited focal epilepsies of childhood — PMID:37714124](https://pubmed.ncbi.nlm.nih.gov/37714124/)
- [Self-Limited Focal Epilepsies in Childhood: How Many and How to Treat (Pediatric Reports, 2025)](https://doi.org/10.3390/pediatric18030074)
- [ClinicalTrials.gov API v2 — zero studies for "Panayiotopoulos" (retrieved 2026-08-05)](https://clinicaltrials.gov/api/v2/studies?query.cond=Panayiotopoulos)
- [Orphanet ORPHA:98815](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=98815&lng=EN)
- [MedLink Neurology — Self-limited epilepsy with autonomic seizures](https://www.medlink.com/articles/self-limited-epilepsy-with-autonomic-seizures)