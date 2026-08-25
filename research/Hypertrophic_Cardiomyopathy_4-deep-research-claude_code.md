---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T20:55:34.636040'
end_time: '2026-08-01T21:17:59.610526'
duration_seconds: 1344.97
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypertrophic Cardiomyopathy 4
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
  - claude-opus-5[1m]
  web_search_requests: 17
  num_turns: 47
  total_cost_usd: 4.935353
  session_id: b68e8312-9662-4592-b53f-e39cffa5db53
  stop_reason: end_turn
citation_count: 69
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypertrophic Cardiomyopathy 4
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 4** covering all of the
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

# Comprehensive Research Report: Hypertrophic Cardiomyopathy 4 (CMH4 / MYBPC3-Related HCM)

**Prepared:** 2026-08-01 · **Target MONDO:** MONDO:0007268 · **Category:** Genetic (Mendelian, sarcomeric cardiomyopathy)

---

## ⚠️ Curation Preflight Note (read before using this report)

"Hypertrophic Cardiomyopathy 4" belongs to a **numbered disease series (CMH1–CMH27)** — a high-risk class for Named Entity Confusion in deep-research outputs. The identity anchors for this entry are:

| Anchor | Value |
|---|---|
| OMIM phenotype | **115197** (CARDIOMYOPATHY, FAMILIAL HYPERTROPHIC, 4; CMH4) |
| Causal gene | **MYBPC3** (OMIM \*600958; `hgnc:7551`) |
| Locus | **11p11.2** |
| MONDO | **MONDO:0007268** hypertrophic cardiomyopathy 4 |
| Disease Ontology | DOID:0110310 |

Any report that names **MYH7** (that is CMH1/OMIM 192600), **TNNT2** (CMH2/115195), **TPM1** (CMH3/115196), or **TNNI3** (CMH7/613690) as the primary gene is describing a *different* CMH entity. All content below is anchored on MYBPC3.

Sources: [OMIM 115197](https://omim.org/entry/115197), [MGI/DO DOID:0110310](https://www.informatics.jax.org/disease/115197)

---

## 1. Disease Information

### Overview

Hypertrophic cardiomyopathy 4 (CMH4) is the **MYBPC3-related form of familial hypertrophic cardiomyopathy** — the single most common genetic cause of HCM worldwide. It is defined by unexplained left ventricular hypertrophy (LVH), typically asymmetric and septal-predominant, in the absence of an alternative loading condition (hypertension, aortic stenosis) sufficient to explain it.

CMH4 is mechanistically distinctive among the sarcomeric HCMs. Whereas most HCM genes act through **poison-peptide / dominant-negative** missense alleles, ~90% of pathogenic MYBPC3 variants are **truncating** (frameshift, nonsense, splice-disrupting) and act through **haploinsufficiency** of cardiac myosin-binding protein C (cMyBP-C) — the truncated peptide is essentially never detectable in human myocardium.

CMH4 has two clinically and genetically distinct presentations:

1. **Monoallelic (heterozygous)** — classic autosomal dominant, adult-onset, age- and sex-dependent incomplete penetrance, generally favourable prognosis.
2. **Biallelic (homozygous or compound heterozygous truncating)** — a **recessive, lethal neonatal cardiomyopathy** with left ventricular noncompaction features and septal defects, essentially uniformly fatal in the first year without transplant.

OMIM captures both: *"The transmission pattern of CMH4 was autosomal dominant in the families reported by Watkins et al. (1995) and autosomal recessive in the family reported by Wang et al. (2013). Incomplete penetrance was observed in both families."* ([OMIM 115197](https://omim.org/entry/115197))

### Key Identifiers

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | 115197 |
| OMIM (gene) | \*600958 MYBPC3 |
| MONDO | MONDO:0007268 (`hypertrophic cardiomyopathy 4`) |
| MONDO (parent) | MONDO:0005045 (`hypertrophic cardiomyopathy`) |
| Disease Ontology | DOID:0110310 |
| Orphanet | ORPHA:155 — *Familial isolated hypertrophic cardiomyopathy* (flagged "NON RARE IN EUROPE"); ORPHA:217569 — *Rare familial disorder with hypertrophic cardiomyopathy* (grouping) |
| ICD-10 | I42.1 (obstructive HCM) / I42.2 (other HCM) |
| ICD-11 | BC43.0 Hypertrophic cardiomyopathy |
| MeSH | D024741 *Cardiomyopathy, Hypertrophic, Familial*; D002312 *Cardiomyopathy, Hypertrophic* |
| HGNC | HGNC:7551 (MYBPC3) — dismech CURIE form: `hgnc:7551` |
| UniProt | Q14896 (MYBPC3_HUMAN) |
| HPO (core) | HP:0001639 Hypertrophic cardiomyopathy |

### Synonyms

- CMH4
- Cardiomyopathy, familial hypertrophic, 4
- MYBPC3-related hypertrophic cardiomyopathy
- Myosin-binding protein C, cardiac, deficiency of (historical OMIM synonym)
- Left ventricular noncompaction 10 / LVNC10 (allelic; some MYBPC3 alleles)
- (Biallelic form) Severe neonatal / infantile MYBPC3 cardiomyopathy; "Amish nemaline-unrelated infantile HCM" (colloquial, Geauga County Old Order Amish)

### Data provenance character

Evidence for CMH4 is **overwhelmingly disease-level and cohort-aggregated**, not EHR-individual:
- **Clinical cohorts / registries:** SHaRe (Sarcomeric Human Cardiomyopathy Registry, n=4,756 genotyped), Dutch BIO FOr CARe founder-variant cohort, Spanish multicentre truncating-MYBPC3 cohort, UK Heart Hospital family series.
- **Aggregated variant resources:** ClinVar, ClinGen (Hereditary Cardiovascular Disease GCEP), gnomAD.
- **Population biobanks (the exception — genome-first, individual-level):** UK Biobank, Penn Medicine BioBank, ARIC — these produce the low-penetrance estimates.
- **Molecular:** human myectomy/explant tissue, iPSC-CM and engineered cardiac tissue, mouse knock-in/knock-out.

---

## 2. Etiology

### 2.1 Primary causal factor

**Germline pathogenic/likely pathogenic variants in MYBPC3** are the necessary cause. MYBPC3 accounts for **~50% of genetically explained nonsyndromic HCM**, with MYH7 (~33%), TNNI3 (~5%), TNNT2 (~4%) and other sarcomere genes (<3% each) making up the remainder ([GeneReviews, PMID:20301725](https://www.ncbi.nlm.nih.gov/books/NBK1768/)).

ClinGen's Hereditary Cardiovascular Disease Gene Curation Expert Panel classifies the relationship as **Definitive** (SOP8, 2021-10-07):

> `MYBPC3 | HGNC:7551 | hypertrophic cardiomyopathy | MONDO:0005045 | AD | Definitive | SOP8 | Hereditary Cardiovascular Disease Gene Curation Expert Panel | 2021-10-07T16:00:00.000Z`
> *(ClinGen Gene-Disease Validity assertion, cached locally as `CGGV_assertion_7e65896e-33f5-439d-8749-aba08a539dd0-2021-10-07T160000.000Z`)*

MYBPC3 is one of only **8 of 33 evaluated HCM genes** to reach Definitive validity, alongside MYH7, TNNT2, TNNI3, TPM1, ACTC1, MYL2, MYL3 ([ClinGen HCM reappraisal, PMC11312670](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11312670/); original framework [Ingles et al., Circ Genom Precis Med 2019](https://www.ahajournals.org/doi/10.1161/CIRCGEN.119.002460)).

**Notably, MYBPC3 is *not* validly associated with other cardiomyopathies** — a useful negative constraint for curation:

> `MYBPC3 | HGNC:7551 | arrhythmogenic right ventricular cardiomyopathy | MONDO:0016587 | AD | Limited | SOP7 | ... | 2019-08-06`
> `MYBPC3 | HGNC:7551 | dilated cardiomyopathy | MONDO:0005021 | AD | Limited | SOP10 | ... | 2025-05-16`
> `MYBPC3 | HGNC:7551 | dilated cardiomyopathy | MONDO:0005021 | AR | Limited | SOP10 | ... | 2025-05-16`

### 2.2 Genetic risk factors and modifiers

| Factor | Effect | Evidence |
|---|---|---|
| **Truncating vs non-truncating MYBPC3 allele** | Truncating = 91% of pathogenic MYBPC3 variants; clinical severity is *locus-independent*, consistent with pure loss-of-function | Helms et al., Circ Genom Precis Med 2020, **PMID:32841044** (SHaRe, n=4,756 genotyped; 1,047 patients with truncating variants across 234 unique variants) |
| **Allelic dose (biallelic vs monoallelic)** | Biallelic truncating → lethal neonatal disease; monoallelic → adult-onset | **PMID:25335496**; **PMID:41488457** |
| **Compound/complex genotype (2nd sarcomere variant)** | Earlier onset, greater hypertrophy, worse outcome | **PMID:22267749** (4/57 probands, 7.0%, carried multiple mutations) |
| **Male sex** | Higher penetrance | **PMID:22267749**: penetrance "greater in males than females (65.1% versus 48.1%, P=0.03)" |
| **Age** | Strongly age-dependent penetrance | **PMID:22267749**: "38.4% <40 versus 68.6% ≥40 years, P<0.001" |
| **Common-variant polygenic background** | Low-penetrance sarcomere variants and HCM PRS act additively to modulate expression | [Circulation 2025, Low Penetrance Sarcomere Variants](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.124.069398) |
| **RAAS pathway polymorphisms (ACE I/D, AGT, CMA1, AGTR1, CYP11B2)** | Proposed modifiers of hypertrophy magnitude in MYBPC3 carriers | [Pflugers/PMC3449069](https://pmc.ncbi.nlm.nih.gov/articles/PMC3449069/) — modest, replication-limited |
| **NMD machinery (UPF3B) expression** | Determines degree of haploinsufficiency achieved from a given PTC allele | **PMID:37797718** |
| **Ubiquitin-proteasome system capacity (declines with age/oxidative stress)** | Proposed to convert a dormant allele into late-onset disease | **PMID:19151713** (discussion); **PMID:38406555** |

**Population-specific high-frequency alleles** (see §9): the South Asian MYBPC3 intron-32 25-bp deletion (~4% carrier frequency); the three Dutch founder truncating variants; the Amish/Swiss c.3330+2T>G splice allele; Icelandic and Northern Spanish founder alleles.

### 2.3 Environmental / acquired risk factors

There is **no environmental factor that causes CMH4** — the genotype is necessary. Environmental factors act as **penetrance and severity modifiers ("second hits")**:

- **Hypertension.** In the Indian 25-bp-deletion families, *"In three cases, hypertension coexisted with the deletion in the family members and these individuals showed severe phenotypes."* (**PMID:19151713**, exact quote)
- **Western/obesogenic diet.** In heterozygous *Mybpc3*<sup>c.772G>A</sup> knock-in mice that are otherwise phenotype-negative, Western diet feeding triggered cardiac dysfunction and hypertrophy — an explicit **two-hit model** ([PMC11708371](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11708371/)). This is MODEL_ORGANISM evidence and should be tagged as such.
- **Ageing.** *"Aging further exacerbates the severity of HCM in carriers of MYBPC3 mutations."* (**PMID:38406555**, exact quote)
- **Intense/competitive athletic conditioning.** Contributes to LV wall thickness and confounds diagnosis (athlete's heart differential); historically a trigger context for SCD, though modern guidelines have liberalised exercise restrictions.
- **Catecholaminergic stress / exercise.** Provokes symptoms and dynamic LVOT obstruction: OMIM notes symptoms *"can be readily provoked by exercise."*

### 2.4 Protective factors

- **No validated genetic protective allele is established** for CMH4. The nearest analogue is a **low HCM polygenic risk score**, which is associated with reduced penetrance/expressivity in sarcomere-variant carriers ([Circulation 2025](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.124.069398)).
- **Female sex** is associated with lower penetrance (48.1% vs 65.1%, **PMID:22267749**) — though women with MYBPC3-HCM are diagnosed later and often with more advanced symptoms, so this is *not* protection against adverse outcome.
- **Environmental:** blood pressure control, weight management, avoidance of dehydration/volume depletion and of vasodilators in obstructive physiology. These are risk-mitigating rather than proven penetrance-preventing; no randomised prevention trial exists.

### 2.5 Gene–environment interactions

The dominant G×E model for CMH4 is **haploinsufficiency + stressor**:

1. A truncating MYBPC3 allele yields ~subnormal cMyBP-C protein but a *compensated* sarcomere for decades.
2. Hemodynamic (hypertension, afterload), metabolic (Western diet, obesity, diabetes), or proteostatic (age-related UPS decline, oxidative stress) stress exceeds reserve.
3. Hypertrophic remodelling becomes overt.

Evidence: mouse Western-diet two-hit model ([PMC11708371](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11708371/)); human hypertension co-modifier data (**PMID:19151713**); age-dependent penetrance (**PMID:22267749**); ageing/UPS review (**PMID:38406555**).

---

## 3. Phenotypes

### 3.1 Core cardiac structural phenotypes

| Phenotype | HPO term | Frequency / character | Evidence |
|---|---|---|---|
| Hypertrophic cardiomyopathy | **HP:0001639** | Defining feature; 100% of affected | PMID:20301725 |
| Left ventricular hypertrophy | **HP:0001712** | Diagnostic threshold: max LV wall thickness **≥15 mm** in adults (≥13–14 mm with family history); z-score >3 in children | PMID:20301725 |
| Asymmetric septal hypertrophy | **HP:0001670** | Most common morphology. In the R502W series: "11 none, 9 asymmetrical, 3 concentric, 1 apical, 1 eccentric" | PMID:22267749 |
| Left ventricular outflow tract obstruction | HP:0031573 *Left ventricular outflow tract obstruction* | ~25–30% have detectable resting/provocable gradients | PMID:20301725 |
| Systolic anterior motion of mitral valve / mitral regurgitation | HP:0001653 *Mitral regurgitation* | Common in obstructive phenotype | Guideline (PMID:38718139) |
| Diastolic dysfunction | HP:0025168 *Left ventricular diastolic dysfunction* | Near-universal; often precedes hypertrophy | PMID:31877118 |
| Left ventricular systolic dysfunction (LVEF <50%, "burnt-out" phase) | HP:0012718 / HP:0001644 | ~8% overall | PMID:20301725 |
| Left ventricular noncompaction | HP:0011664 *Left ventricular noncompaction* | **Biallelic form only** — 3 of 4 neonates | PMID:25335496 |
| Septal defects (ASD/VSD) / PDA | HP:0001631 *Atrial septal defect*; HP:0001629 *Ventricular septal defect*; HP:0001643 *Patent ductus arteriosus* | **Biallelic form** — 62% (13/21) of reported biallelic cases | PMID:25335496 |

### 3.2 Symptoms and functional phenotypes

| Phenotype | HPO term | Notes |
|---|---|---|
| Dyspnea / exertional breathlessness | **HP:0002094** | Most common presenting symptom; OMIM lists dyspnea among cardinal symptoms |
| Chest pain / angina pectoris | **HP:0001681** | Often microvascular, not epicardial CAD |
| Palpitations | **HP:0001962** | |
| Syncope | **HP:0001279** | Exertional syncope is an SCD risk marker |
| Congestive heart failure | **HP:0001635** | Relevant heart failure in 8.1% of Spanish truncating-variant cohort (PMID:39581692) |
| Fatigue / exercise intolerance | HP:0012378 *Fatigue*; HP:0003546 *Exercise intolerance* | Reflected in pVO₂ endpoints of EXPLORER-HCM / SEQUOIA-HCM |
| Failure to thrive (neonatal form) | HP:0001508 *Failure to thrive* | "All four children presented with feeding difficulties, failure to thrive, and dyspnea." (PMID:25335496, exact quote) |
| Feeding difficulties (neonatal form) | HP:0011968 *Feeding difficulties* | Same |

### 3.3 Arrhythmic / electrophysiological phenotypes

| Phenotype | HPO term | Frequency |
|---|---|---|
| Atrial fibrillation | **HP:0005110** | ~20% overall; **~60% by age 60** if diagnosed before age 40 (PMID:20301725) |
| Ventricular arrhythmia / NSVT | **HP:0004308** | Key SCD risk marker |
| Sudden cardiac death | **HP:0001645** | ~6% experience SCD, resuscitated arrest, or appropriate ICD therapy (PMID:20301725). Annual SCD rate **0.46%/yr** and all-cause mortality **0.93%/yr** in clinically affected MYBPC3 carriers over 7.9±4.5 yr follow-up (PMID:22267749, exact figures) |
| Cardiac arrest | **HP:0001695** | |
| Abnormal ECG (LVH voltage, repolarisation abnormality, pathological Q waves) | HP:0003115 *Abnormal EKG*; HP:0011021 (see below) | ECG abnormality often precedes hypertrophy in G+/LVH− carriers |
| Ventricular tachycardia | HP:0004756 | "recurrent ventricular tachyarrhythmias in one homozygous subject" (PMID:19151713) |

### 3.4 Laboratory / biomarker abnormalities

| Marker | LOINC / HPO | Direction | Notes |
|---|---|---|---|
| NT-proBNP | LOINC:33762-6 | ↑ | HP:0031185 *Increased circulating brain natriuretic peptide concentration*; tracks HF severity; a mavacamten/aficamten pharmacodynamic endpoint |
| High-sensitivity cardiac troponin I/T | LOINC:89579-7 | ↑ | Elevated even in G+/LVH− carriers — an early subclinical marker (PMID:31877118) |
| Serum profibrotic markers (PICP, procollagen) | — | ↑ | Elevated pre-hypertrophy in sarcomere-variant carriers |

### 3.5 Phenotype characteristics

**Age of onset.** Bimodal and genotype-dose-dependent:
- **Biallelic truncating:** congenital/neonatal. "They died from cardiac failure before age 13 weeks." (PMID:25335496, exact quote). All 21 reported biallelic-truncating patients "were diagnosed with severe cardiomyopathy and/or died within the first few months of life."
- **Monoallelic:** classically **adult-onset**, historically described as "late-onset." In the Indian 25-bp-deletion families, "In most carriers the effects remained dormant until the third decade" (PMID:19151713, exact quote). Spanish cohort mean age 47±16.8 yr (PMID:39581692).
- **But onset is extremely heterogeneous.** In 9 R502W families (25 individuals) there was "marked heterogeneity in age at diagnosis (5 to 80 years)" (PMID:22267749, exact quote).

**Severity.** Variable. In the Spanish truncating-variant cohort, "Hypertrophy was discrete with a significative difference between probands and relatives (17.5±4 mm vs 14.6±5 mm; p<0.0001). Ejection fraction was predominantly preserved (65%±10%)." (PMID:39581692, exact quote).

**Progression.** Slowly progressive over decades in most; a minority progress to end-stage/"burnt-out" HCM with systolic dysfunction. Symptoms are typically **episodic/exertional** superimposed on a chronic substrate. Incident HCM phenotype in the Spanish cohort was 10% over 7.77 years mean follow-up (PMID:39581692).

**Quality-of-life impact.** Well quantified via KCCQ-CSS and HCMSQ. In EXPLORER-HCM, mavacamten produced "improved symptom scores (KCCQ-CSS +9·1, 5·5 to 12·7; HCMSQ-SoB −1·8, −2·4 to −1·2; p<0·0001)" and "34% more patients in the mavacamten group improved by at least one NYHA class" (PMID:32871100, exact quotes). Baseline NYHA II–III limitation, exercise intolerance, chest pain, and the psychological burden of SCD risk / ICD carriage / cascade-testing family implications are the principal QoL domains. Validated instruments: **KCCQ-23/KCCQ-CSS**, **HCMSQ (Hypertrophic Cardiomyopathy Symptom Questionnaire)**, EQ-5D-5L, SF-36.

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

**MYBPC3** — myosin-binding protein C, cardiac (`hgnc:7551`; OMIM \*600958; UniProt Q14896; Ensembl ENSG00000134571; RefSeq **NM_000256.3**).
- Locus **11p11.2**; 35 exons; ~21 kb genomic.
- Protein: 1,274 aa, ~141 kDa cardiac isoform. Domain architecture N→C: **C0** (cardiac-specific Ig), **Pro-Ala linker**, **C1** (Ig), **M-domain** (cardiac-specific, PKA-phosphorylatable regulatory motif), **C2–C10** (mix of Ig-I and Fn3 domains). C8–C10 anchor to light meromyosin and titin; C0–C2 interacts with the myosin S2 and regulatory light chain and with actin.
- Localisation: **doublets in the C-zone of the A-band of the sarcomere** (PMID:19151713).

### 4.2 Pathogenic variant spectrum

**Variant classes.** Truncating variants dominate:
> "Truncating variants account for 91% of MYBPC3 pathogenic variants and cause similar clinical severity and outcomes regardless of location, consistent with locus-independent loss-of-function." — Helms et al., **PMID:32841044**

> "Among HCM patients with genetic defects in MYBPC3, 90% of mutations are heterozygous frameshift, nonsense, or splice site mutations that result in premature termination codons and truncated cMyBP-C protein."

> "The most striking characteristic of HCM mutations in MYBPC3 is that many are within introns and are predicted to cause aberrant splicing leading to a frameshift and a premature chain termination, yet the truncated peptides have never been identified in human heart tissue carrying these mutations." — Marston et al., **PMID:22057632** (exact quote)

Breakdown by mechanism class:
- **Frameshift (indel)** — e.g. c.2373dup p.(Trp792fs), c.836del p.(Gly279Valfs\*21)
- **Nonsense** — e.g. c.2827C>T p.(Arg943\*)
- **Splice-site** — e.g. c.3330+2T>G (Amish/Swiss), c.2905+1G>A, c.1224-19G>A (intronic, ClinVar RCV000009149)
- **Intronic deletion causing exon skipping** — the South Asian 25-bp intron-32 deletion → skipping of exon 33
- **Missense** — a minority; in the UK proband series "Missense mutations (15, 45.6%) were the most frequent" among 42 mutations, illustrating cohort-dependent ascertainment (PMID:22267749). Some missense alleles (e.g. R502W, a recurrent founder-like allele) are well-established.
- **Copy-number / structural** — whole-gene and multi-exon deletions in 18 probands, including a **promoter deletion** which formally proved that reduced transcription alone suffices: Hayesmoore et al., **PMID:38258577**, *"A Promoter Deletion Confirms That MYBPC3 Haploinsufficiency Is Sufficient to Cause Hypertrophic Cardiomyopathy in Humans."*
- **Alu-mediated insertion** — reported cause of familial HCM ([PMC6978237](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6978237/))

**Selected variants of curation interest:**

| Variant (NM_000256.3) | Protein | Class | Population / significance |
|---|---|---|---|
| c.2373dup | p.(Trp792fs) | Frameshift | **Dutch founder** — 46% of Dutch founder carriers; also homozygous/compound-het lethal neonatal cases (PMID:25335496) |
| c.2827C>T | p.(Arg943\*) | Nonsense | **Dutch founder** — 32% of founder carriers; also in biallelic neonatal cases (PMID:25335496) |
| c.2864_2865delCT | p.(Pro955fs) | Frameshift | **Dutch founder** — 22% of founder carriers |
| c.3330+2T>G | exon 30 skip → frameshift, PTC in exon 31 | Splice donor | **Old Order Amish / Mennonite / ancient Swiss founder**; carrier frequency ~10% in Geauga County, OH settlement (PMID:18467358); Swiss origin established by PMID:36162733 |
| 25-bp deletion, intron 32 | exon 33 skipping | Intronic deletion | **South Asian** — ~4% carrier frequency; OR for cardiomyopathy 6.99 (95% CI 3.68–13.57), P=4×10⁻¹¹ (PMID:19151713) |
| c.1504C>T | p.(Arg502Trp) | Missense | Common recurrent allele; extreme intrafamilial heterogeneity (PMID:22267749) |
| c.2905+1G>A | splice donor | Splice | Compound-het partner in lethal neonatal case (PMID:41488457) |
| c.836del | p.(Gly279Valfs\*21) | Frameshift | Novel; compound-het lethal neonatal (PMID:41488457) |
| c.1224-19G>A | intronic splice-affecting | Splice | ClinVar RCV000009149, asserted for "Familial hypertrophic cardiomyopathy 4" |

**Variant classification.** Per ACMG/AMP, MYBPC3 truncating variants readily reach P/LP via PVS1 (LOF is the established mechanism) + segregation + case–control data. ClinVar holds thousands of MYBPC3 submissions; the ClinGen **Hypertrophic Cardiomyopathy Variant Curation Expert Panel** provides gene-specific PVS1/PM2/PS4 calibration. A computational subdomain-stability predictor has been developed to improve missense-variant interpretation and risk stratification ([Genetics in Medicine 2021](https://www.nature.com/articles/s41436-021-01134-9)).

**Allele frequency.** Population filtering thresholds: "variants in MYBPC3 present in gnomAD with allele frequencies of >4E-05 ... and absent in disease registries are unlikely to be independently pathogenic for HCM." Founder alleles are the exception — the South Asian 25-bp deletion is present at 2–8% across Indian populations, and the Amish c.3330+2T>G at ~10% carrier frequency in one settlement, both far above any generic filtering threshold. **This is a critical caveat: population-frequency-based filtering will falsely benign-call founder alleles.**

**Germline vs somatic.** Exclusively **germline**. No somatic role; CMH4 is not a neoplastic disease and COSMIC/TCGA are not applicable.

**Functional consequence.** **Loss of function via haploinsufficiency** — see §6. Not dominant-negative in the classical poison-peptide sense for truncating alleles; some missense alleles may have additional dominant-negative/incorporation effects (an area of active debate — see Barefield & colleagues, *"Is haploinsufficiency a sufficient mechanism for MYBPC3 truncating mutations?"*, **PMID:36946992**).

### 4.3 Modifier genes

- **UPF3B** (NMD factor) — upregulated specifically in MYBPC3<sup>trunc</sup> hearts and localised to the Z-disc, where sarcomeric protein translation occurs; determines the degree of transcript decay (**PMID:37797718**).
- **Second sarcomere gene variants** (MYH7, TNNT2, TNNI3) in compound genotypes — earlier, more severe disease (**PMID:22267749**; **PMID:39581692**, in which heart failure was "commonly found in the presence of a second [variant]").
- **RAAS pathway polymorphisms** — ACE I/D, AGT M235T, CMA1, AGTR1, CYP11B2 ([PMC3449069](https://pmc.ncbi.nlm.nih.gov/articles/PMC3449069/)).
- **Common-variant polygenic background / HCM PRS** ([Circulation 2025](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.124.069398)).

### 4.4 Epigenetics

No disease-defining epigenetic lesion. Reported findings are **secondary remodelling signatures** in HCM myocardium generally: differential DNA methylation and histone-modification changes at hypertrophic-gene loci, and re-activation of the fetal gene programme (NPPA, NPPB, MYH7). Multi-omic MYBPC3 work identifies transcriptional and post-transcriptional dysregulation (**PMID:38406555**; [Frontiers 2025 P459fs multi-omics, PMC11903464](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11903464/)). ENCODE/Roadmap Epigenomics heart tissue tracks provide the regulatory landscape for MYBPC3 (including the promoter region whose deletion is causal, PMID:38258577), but no CMH4-specific epigenomic biomarker exists.

### 4.5 Chromosomal abnormalities

Not a chromosomal disorder. Relevant large-scale events are **intragenic/whole-gene CNVs at 11p11.2**, detected in ~1–2% of otherwise genotype-negative HCM probands ([Mademont-Soler et al., PMID:28771489](https://pubmed.ncbi.nlm.nih.gov/28771489/); Hayesmoore et al., PMID:38258577). Karyotyping and standard CMA are **not** indicated; gene-panel-integrated CNV calling or MLPA is the appropriate modality.

---

## 5. Environmental Information

- **Environmental toxicants / radiation / pollution / occupational exposure:** No established role in CMH4 causation. CTD lists no exposure with a validated MYBPC3-HCM interaction. Cardiotoxic exposures (anthracyclines, alcohol) cause distinct cardiomyopathies and are relevant only as confounders/differentials.
- **Lifestyle factors:**
  - **Diet.** Western/high-fat-high-sugar diet acts as a disease trigger in phenotype-negative heterozygous *Mybpc3* knock-in mice ([PMC11708371](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11708371/)) — MODEL_ORGANISM evidence; human replication is lacking.
  - **Obesity / metabolic syndrome.** Associated with worse phenotype and adverse outcome in HCM cohorts generally.
  - **Hypertension.** Co-modifier with severe phenotype in MYBPC3 carriers (PMID:19151713).
  - **Exercise.** Provokes symptoms and gradients (OMIM); competitive athletics historically restricted, now individualised under the 2024 guideline (PMID:38718139).
  - **Alcohol.** Vasodilation can worsen dynamic obstruction acutely.
  - **Dehydration/volume depletion.** Precipitates obstruction and syncope.
- **Infectious agents:** Not applicable. No pathogen causes or triggers CMH4. (Viral myocarditis is a differential for acute decompensation, not an etiology.)

---

## 6. Mechanism / Pathophysiology

### 6.1 The causal chain (upstream → downstream)

```
[MOLECULAR] MYBPC3 truncating variant (PTC-generating: frameshift / nonsense /
            splice-disrupting / exon-skipping deletion; or promoter/whole-gene CNV)
                    │
                    ▼
[MOLECULAR] Nonsense-mediated mRNA decay (UPF3B-dependent, at the Z-disc)
            + allelic imbalance (mutant:WT mRNA ratio falls below 1:1)
            + ubiquitin-proteasome degradation of any escaping truncated peptide
                    │
                    ▼
[MOLECULAR] cMyBP-C HAPLOINSUFFICIENCY — reduced cMyBP-C content in the
            C-zone of the A-band; NO detectable poison peptide
                    │
                    ▼
[MOLECULAR] Loss of the cMyBP-C brake on the thick filament:
            • Fewer myosin heads held in the SUPER-RELAXED (SRX) state
            • Shift toward disordered-relaxed (DRX) → more heads available for actin
            • Increased Ca²⁺ sensitivity of force; accelerated cross-bridge kinetics
            • Loss of PKA-phosphorylation-dependent (M-domain Ser273/282/302)
              adrenergic modulation of contractility
                    │
                    ▼
[CELLULAR]  HYPERCONTRACTILITY + IMPAIRED RELAXATION of the cardiomyocyte
            (systolic hypercontractility with diastolic failure to relax)
                    │
                    ├──► [CELLULAR] Increased sarcomeric ATP consumption / energetic
                    │              inefficiency (PCr/ATP falls); metabolic remodelling
                    │
                    ├──► [CELLULAR] Progressive Ca²⁺-handling abnormality
                    │              (slowed Ca²⁺ release/reuptake; SERCA2a/RyR2 changes)
                    │
                    └──► [CELLULAR] Pro-hypertrophic signalling activation
                                   (Ca²⁺-calcineurin-NFAT, CaMKII, MAPK/ERK,
                                    PI3K-AKT-mTOR; fetal gene programme reactivation)
                    │
                    ▼
[TISSUE]    Cardiomyocyte hypertrophy → asymmetric septal-predominant LVH
            + MYOCYTE DISARRAY (loss of parallel myofibre alignment)
            + cardiac-fibroblast activation → interstitial and replacement FIBROSIS
            + intramural small-vessel disease (medial hyperplasia) → microvascular ischemia
                    │
                    ▼
[ORGAN]     • Diastolic dysfunction, elevated LV filling pressures
            • Dynamic LVOT obstruction (septal bulge + SAM of mitral valve)
            • Left atrial dilation → atrial fibrillation
            • Arrhythmogenic substrate (disarray + fibrosis + ischemia) → VT/VF
            • Late: LV systolic dysfunction ("burnt-out" HCM)
                    │
                    ▼
[ORGANISM]  Dyspnea, angina, syncope, heart failure, AF/stroke, SUDDEN CARDIAC DEATH
```

### 6.2 Key mechanistic evidence (verbatim quotes)

**Haploinsufficiency, not poison peptide** (**PMID:22057632**, Marston et al. 2012):
> "Instead of expression of a poison peptide we consistently observe haploinsufficiency of MyBP-C in MYBPC3 mutant human heart muscle."

Corroborated in myectomy tissue (Marston et al., Circ Res 2009, **PMID:19574547**, *"Evidence from human myectomy samples that MYBPC3 mutations cause hypertrophic cardiomyopathy through haploinsufficiency"*) and formally proven by promoter deletion (**PMID:38258577**), whose accompanying mouse showed *"heterozygous for an Mybpc3 promoter deletion developed a late-onset phenotype of asymmetrical septal hypertrophy associated with fibrosis."*

**NMD is the proximal mechanism** (**PMID:37797718**, Burkart et al. 2023):
> "We show that cMyBP-C haploinsufficiency starts at the mRNA level, despite hypertrophy-induced increased transcriptional activity."
> "Strikingly, we show that in sarcomeres UPF3B but not UPF1 and UPF2 are localized to the Z-discs, the presumed location of sarcomeric protein translation. Our data suggest that cMyBP-C haploinsufficiency in HCM-patients is established by UPF3B-dependent NMD during the initial translation round at the Z-disc."

**Multiple degradative routes converge** (**PMID:38406555**, Ananthamohan et al. 2024):
> "Pathogenesis related to MYBPC3 mutations includes nonsense-mediated decay, alternative splicing, and ubiquitin-proteasome system events, leading to allelic imbalance and haploinsufficiency."

**Myosin dysregulation / SRX loss.** Toepfer et al., Sci Transl Med 2019 (**PMID:30674652**), *"Hypertrophic cardiomyopathy mutations in MYBPC3 dysregulate myosin"*; McNamara et al., PLoS One 2017 (**PMID:28658286**) — MYBPC3-mutant patient myocardium shows *"a significantly diminished SRX, characterized by a decrease in both the number of myosin heads in the SRX and the lifetime of ATP turnover"*; McNamara et al., J Mol Cell Cardiol 2016 (**PMID:27021517**) — cMyBP-C ablation disrupts SRX in murine cardiomyocytes. The SRX state consumes ATP ~10-fold slower than DRX, so SRX loss directly links to **energetic inefficiency**.

**Contractile trajectory: hypercontractile → hypocontractile, Ca²⁺-mediated** (**PMID:36893011**, De Lange et al. 2023, human isogenic iPSC-CM engineered cardiac tissue, IN_VITRO):
> "Our data suggest a progressive phenotype caused by cMyBP-C haploinsufficiency and ablation that initially is hypercontractile, but progresses to hypocontractility with impaired relaxation. The severity of the phenotype correlates with the amount of cMyBP-C present, with more severe earlier phenotypes observed in cMyBP-C-/- than cMyBP-C+/- ECTs. We propose that while the primary effect of cMyBP-C haploinsufficiency or ablation may relate to myosin crossbridge orientation, the observed contractile phenotype is Ca2+-mediated."
> "RNA-seq analysis revealed enrichment of differentially expressed hypertrophic, sarcomeric, Ca2+-handling, and metabolic genes in cMyBP-C+/- and cMyBP-C-/- ECTs."

**Sarcomeric disorganisation as a proximal cellular lesion** (**PMID:19151713**, IN_VITRO, neonatal rat cardiomyocytes):
> "Staining with antibodies to the myc tag showed a highly disorganized and diffused pattern of sarcomeric architecture as a result of aberrant incorporation of altered proteins"

**Pre-hypertrophic (subclinical) changes.** Helms et al., JCI Insight 2020 (**PMID:31877118**), *"Effects of MYBPC3 loss-of-function mutations preceding hypertrophic cardiomyopathy"* — sarcomere-variant carriers without LVH already show diastolic abnormalities, elevated troponin, and profibrotic signalling.

**Fibroblast-autonomous fibrosis.** Zou et al., Cell Death Dis 2022 (**PMID:36357371**), *"MYBPC3 deficiency in cardiac fibroblasts drives their activation and contributes to fibrosis"* — a non-cardiomyocyte arm of the mechanism.

**Ongoing debate.** Barefield, J Gen Physiol 2023 (**PMID:36946992**), *"Is haploinsufficiency a sufficient mechanism for MYBPC3 truncating mutations?"* — argues additional/parallel mechanisms may contribute for some alleles. Flag as an open mechanistic question (dismech `KNOWLEDGE_GAP`).

### 6.3 Ontology term suggestions for pathophysiology nodes

**GO Biological Process:**

| Node | GO term |
|---|---|
| Cross-bridge cycling / contraction | GO:0006936 muscle contraction; **GO:0060048 cardiac muscle contraction**; GO:0030049 muscle filament sliding |
| Nonsense-mediated decay | GO:0000184 nuclear-transcribed mRNA catabolic process, nonsense-mediated decay; GO:0006402 mRNA catabolic process |
| Aberrant splicing | GO:0000381 regulation of alternative mRNA splicing, via spliceosome; GO:0008380 RNA splicing |
| UPS degradation | **GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process** |
| Myosin ATPase / SRX | GO:0032781 positive regulation of ATP-dependent activity; GO:0000146 microfilament motor activity (MF) |
| Ca²⁺ handling | GO:0060402 calcium ion transport into cytosol; GO:0055117 regulation of cardiac muscle contraction |
| Hypertrophy | GO:0003300 cardiac muscle hypertrophy; GO:0014898 cardiac muscle hypertrophy in response to stress |
| Sarcomere organisation | GO:0045214 sarcomere organization; GO:0055003 cardiac myofibril assembly |
| Fibrosis | GO:0010613 positive regulation of cardiac muscle hypertrophy; GO:0060346 (see also fibrotic_response module) |
| Adrenergic modulation | GO:0071880 adenylate cyclase-activating adrenergic receptor signaling pathway |

**GO Molecular Function / Cellular Component (for MYBPC3 itself):**
- MF: GO:0008307 structural constituent of muscle; GO:0032036 myosin heavy chain binding; GO:0051015 actin filament binding
- CC: **GO:0031430 M band**; **GO:0030017 sarcomere**; GO:0031672 A band; GO:0005865 striated muscle thin filament; GO:0030018 Z disc (UPF3B localisation)

**CL Cell Types:**
- **CL:0000746 cardiac muscle cell** (cardiomyocyte) — primary
- CL:2000046 ventricular cardiac muscle cell
- **CL:0002548 fibroblast of cardiac tissue** — fibrosis arm
- CL:0000359 vascular associated smooth muscle cell — intramural small-vessel disease
- CL:0002138 endothelial cell of lymphatic vessel / CL:0000115 endothelial cell — microvascular arm

### 6.4 Molecular profiling

- **Transcriptomics.** RNA-seq of MYBPC3<sup>+/-</sup> and MYBPC3<sup>-/-</sup> engineered cardiac tissue shows enrichment of hypertrophic, sarcomeric, Ca²⁺-handling, and metabolic gene sets (**PMID:36893011**). GSEA of human MYBPC3<sup>trunc</sup> myocardium shows increased NMD-component expression (**PMID:37797718**). Allelic-imbalance RNA-seq is the standard assay for demonstrating NMD in patient tissue (**PMID:30456444**).
- **Spatial transcriptomics.** Focal myocyte-disarray regions vs normal regions of human HCM myocardium have been profiled ([PMC10454036](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10454036/)) — reveals region-specific fibrotic/ECM programmes.
- **Proteomics.** Quantitative western/MS of myectomy tissue demonstrates ~30–50% reduction of cMyBP-C protein with *absence* of any truncated species (**PMID:19574547**; **PMID:22057632**). Human Protein Atlas confirms heart-restricted MYBPC3 expression.
- **Multi-omics.** MyBPC3 P459fs multi-omics + super-resolution imaging ([PMC11903464](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11903464/)).
- **Metabolomics/energetics.** ³¹P-MRS shows reduced myocardial PCr/ATP ratio in HCM including in G+/LVH− carriers — the energy-depletion hypothesis. Lipidomics: no CMH4-specific signature.
- **Functional genomics.** CRISPR-Cas9 isogenic iPSC allelic series (WT / +/− / −/−) is the workhorse (**PMID:36893011**). No CMH4-specific DepMap/genome-wide screen.

---

## 7. Anatomical Structures Affected

### Organ level
- **Primary organ: heart** — **UBERON:0000948** (heart)
  - **UBERON:0002084** heart left ventricle — principal site
  - **UBERON:0002094** interventricular septum — site of maximal, asymmetric hypertrophy
  - **UBERON:0002349** myocardium — the affected tissue proper
  - UBERON:0002079 left cardiac atrium — secondary dilation → AF
  - UBERON:0002078 right cardiac atrium
  - UBERON:0002135 mitral valve — SAM, secondary MR
  - UBERON:0004145 left ventricular outflow tract — dynamic obstruction
  - UBERON:0001621 coronary artery / intramural arterioles — small-vessel disease
- **Secondary organ involvement:**
  - Brain (UBERON:0000955) — cardioembolic stroke from AF; syncope-related injury
  - Lung (UBERON:0002048) — pulmonary congestion/oedema from elevated filling pressures
  - Liver (UBERON:0002107), kidney (UBERON:0002113) — congestive/low-output injury in advanced HF
- **Body systems:** **cardiovascular** (primary); respiratory and nervous systems secondarily.
- **Biallelic neonatal form adds:** interatrial septum (ASD), interventricular septum (VSD), ductus arteriosus (PDA) — i.e. **structural congenital heart disease** alongside the cardiomyopathy (PMID:25335496; PMID:41488457).

### Tissue and cell level
- **Tissue types:** cardiac muscle tissue (striated); cardiac connective tissue/ECM (interstitial and replacement fibrosis); vascular smooth muscle (intramural arteriolar medial hyperplasia).
- **Cell populations:** **CL:0000746** cardiac muscle cell (primary target); CL:2000046 ventricular cardiac muscle cell; **CL:0002548** fibroblast of cardiac tissue (activated → myofibroblast, CL:0000186); CL:0000359 vascular associated smooth muscle cell; CL:0000235 macrophage (inflammatory infiltrate in advanced disease).

### Subcellular level
- **GO:0030017 sarcomere** — the primary compartment
- **GO:0031430 M band** and **GO:0031672 A band** (C-zone) — cMyBP-C's native location
- GO:0030018 Z disc — where UPF3B-dependent NMD is proposed to act (PMID:37797718)
- GO:0016529 sarcoplasmic reticulum — Ca²⁺-handling arm
- GO:0005739 mitochondrion — energetic inefficiency
- GO:0000502 proteasome complex — mutant peptide degradation
- GO:0005634 nucleus / GO:0005681 spliceosomal complex — aberrant splicing arm

### Localisation
- **Lateralisation:** intrinsically **left-sided and asymmetric** — septal-predominant LVH is the signature. Apical, concentric, mid-cavity, and eccentric variants occur (PMID:22267749). Right ventricular hypertrophy is uncommon and secondary.
- **Regional heterogeneity:** LGE (fibrosis) on CMR is characteristically **patchy/mid-wall**, concentrated at RV insertion points and within the hypertrophied septum.

---

## 8. Temporal Development

### Onset
| Genotype | Typical onset | Pattern |
|---|---|---|
| **Biallelic truncating** | **Neonatal / first weeks of life** | Acute, fulminant |
| **Monoallelic truncating (classic)** | Adolescence to late adulthood; classically 3rd decade onward | Insidious, chronic |
| **Monoallelic with compound genotype / hypertension** | Earlier, more severe | Accelerated |

Verbatim anchors:
- Biallelic: *"They died from cardiac failure before age 13 weeks."* / *"All patients with biallelic truncating pathogenic mutations in MYBPC3 reported so far (n=21) were diagnosed with severe cardiomyopathy and/or died within the first few months of life."* (**PMID:25335496**)
- Monoallelic: *"In most carriers the effects remained dormant until the third decade and then manifested themselves as mild hypertrophy"* (**PMID:19151713**)
- Extreme heterogeneity: *"marked heterogeneity in age at diagnosis (5 to 80 years)"* (**PMID:22267749**)

The historical framing of MYBPC3 as uniformly "late-onset and benign" has been substantially revised. Page et al. tested exactly that hypothesis and found: *"Small selected cohort studies suggest that mutations in the cardiac myosin binding protein-C (MYBPC3) gene cause late-onset, clinically benign hypertrophic cardiomyopathy (HCM). The aim of this study was to test this hypothesis..."* → *"Disease expression in families with HCM related to MYBPC3 mutations shows marked heterogeneity with incomplete, age-related, and gender specific penetrance."* (**PMID:22267749**)

### Progression and staging

A widely used conceptual staging for sarcomeric HCM (applies to CMH4):

| Stage | Description | Markers |
|---|---|---|
| **0 — Genotype-positive / phenotype-negative (G+/LVH−)** | No LVH; subclinical abnormalities present | Diastolic dysfunction, ↑ hs-troponin, ↑ profibrotic markers, ECG changes, crypts/elongated mitral leaflets on CMR (PMID:31877118) |
| **1 — Classic HCM** | Overt LVH, preserved EF | ±LVOT obstruction, ±LGE |
| **2 — Adverse remodelling** | Progressive fibrosis, LA dilation, AF | Rising LGE burden |
| **3 — Overt dysfunction / "burnt-out"** | LVEF <50%, restrictive/dilated physiology | ~8% overall (PMID:20301725) |
| **4 — End-stage HF** | Transplant/LVAD candidacy | |

- **Rate:** slow in most. Incident phenotype conversion **10% over 7.77 years** mean follow-up in the Spanish truncating-variant cohort (**PMID:39581692**). Longitudinal biobank data show low annual conversion rates in genome-first carriers (**PMID:39886308**).
- **Course pattern:** **chronic, slowly progressive**, punctuated by episodic exertional symptoms and by discrete arrhythmic events (AF onset, VT).
- **Duration:** lifelong; no spontaneous remission.

### Patterns
- **Remission:** none spontaneous. *Treatment-induced* symptomatic and haemodynamic remission is achievable — cardiac myosin inhibitors normalise LVOT gradients in a majority; septal reduction therapy abolishes obstruction durably.
- **Critical periods / intervention windows:**
  - **Adolescence and young adulthood** — highest relative SCD risk; peak yield of surveillance imaging.
  - **G+/LVH− window** — the theoretical target for disease-modifying/preventive therapy (currently investigational; VANISH trial of valsartan in early sarcomeric HCM is the flagship attempt).
  - **Neonatal period (biallelic)** — the only window for transplant listing.
  - **Pre-conception / prenatal (biallelic-at-risk couples)** — PGT window (PMID:41488457).

---

## 9. Inheritance and Population

### Epidemiology

| Measure | Value | Source |
|---|---|---|
| HCM (all causes) prevalence | **~1 in 500** (≈200 per 100,000) by imaging-based estimate | Widely replicated; Orphanet flags familial isolated HCM as "NON RARE IN EUROPE" |
| Clinically *diagnosed* HCM prevalence | ~1 in 3,000 (≈33/100,000) — the diagnostic gap | German 5-million-patient analysis, [PMC5933727](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5933727/) |
| Clinically apparent **obstructive** HCM | **1.65 per 10,000** (16.5/100,000) | [PMC8770922](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8770922/) |
| US HCM burden | **~600,000 people** | "Hypertrophic cardiomyopathy (HCM) affects approximately 600,000 people in the United States." (**PMID:40038304**, exact quote) |
| **CMH4 share** | **~50% of genetically explained HCM** → point prevalence on the order of **50–100 per 100,000** if the 1:500 imaging estimate holds and ~30% of HCM is genotyped positive; **~10–30 per 100,000** on more conservative diagnosed-case estimates | Derived; PMID:20301725 |
| Diagnostic yield of genetic testing | ~30% of all HCM; ~60% with positive family history | PMID:20301725 |

> **Curation note for the dismech `Prevalence` slots:** the honest structured record is `measure_type: POINT_PREVALENCE`, `prevalence_class: BAND_1_5_PER_10000` for the *derived* CMH4 estimate, with the verbatim source phrasing in `notes` and the derivation flagged. Do not assert a single hard number as if directly measured.

### Inheritance

- **Pattern:** **Autosomal dominant** (HP:0000006) for monoallelic disease; **autosomal recessive** (HP:0000007) for the biallelic lethal neonatal form. Both are recognised at OMIM 115197. A CMH4 entry should carry **both** `Inheritance` blocks with bound terms, keyed to the respective subtypes.
- **Penetrance:** **Incomplete, age-dependent, and sex-dependent** (HP:0003829 Incomplete penetrance).

| Setting | MYBPC3 / sarcomere penetrance |
|---|---|
| Clinical HCM families (all sarcomere genes) | **57%** |
| Population/community biobanks (incidental P/LP carriers) | **11%** (0% ARIC → **18% UK Biobank**) |
| MYBPC3-specific, pooled clinical | **~55%** |
| MYBPC3 UK family series, all carriers | **56.9%**; in relatives only **34.5%** |
| Age-stratified (MYBPC3, UK series) | **38.4% <40 yr vs 68.6% ≥40 yr** (P<0.001) |
| Sex-stratified (MYBPC3, UK series) | **65.1% male vs 48.1% female** (P=0.03) |

Sources: Topriceanu et al., Circulation 2024, **PMID:37929589** — *"The penetrance of a pathogenic/likely pathogenic (P/LP) sarcomeric mutation is low in the general population at 11% but five-fold higher at 57% in patients with HCM and their family members"*; PMID:22267749 (exact quotes above); GeneReviews per-gene table (PMID:20301725): MYL3 ~32%, CSRP3 38%, TPM1 ~49%, **MYBPC3 ~55%**, TNNT2 ~62%, MYH7 ~64%.

- **Expressivity:** **Highly variable**, including within a single family carrying an identical allele. The R502W series is the canonical demonstration: 9 families / 25 individuals with "marked heterogeneity in age at diagnosis (5 to 80 years), pattern of hypertrophy (11 none, 9 asymmetrical, 3 concentric, 1 apical, 1 eccentric), and prognosis (premature sudden death in 2 individuals compared with survival to advanced age in 6 individuals)" (**PMID:22267749**, exact quote).
- **Genetic anticipation:** **Not a feature** — MYBPC3 is not a repeat-expansion locus. Apparent anticipation in pedigrees reflects ascertainment bias and earlier cascade screening.
- **Germline mosaicism:** Rare; occasional de novo MYBPC3 variants are reported. Recurrence-risk counselling for apparently de novo cases should acknowledge low-level parental gonadal mosaicism, but no quantified rate exists for MYBPC3.
- **Founder effects:** Prominent — see table below.
- **Consanguinity:** A major driver of the **biallelic** form. Homozygous truncating cases arise both from consanguinity and from founder-allele population frequency (the Amish setting is the archetype of the latter).
- **Carrier frequency:** Population-dependent. General populations: MYBPC3 P/LP carrier frequency is roughly 1 in 200–500 for HCM-associated sarcomere variants overall. Founder settings dramatically exceed this.

### Founder alleles / geographic distribution of specific variants

| Population | Variant | Frequency / burden | Source |
|---|---|---|---|
| **Netherlands** | c.2373dup, c.2827C>T, c.2864_2865delCT | Collectively **up to ~35% of all Dutch HCM**; distribution among founder carriers 46% / 32% / 22% | [Circ Cardiovasc Genet 2017](https://www.ahajournals.org/doi/10.1161/CIRCGENETICS.116.001660); [BIO FOr CARe, PMID:33532905](https://pubmed.ncbi.nlm.nih.gov/33532905/) |
| **Old Order Amish (Geauga Co., OH) / Mennonite / Swiss** | c.3330+2T>G | **~10% heterozygous carrier frequency** in the Geauga settlement; ancient Swiss (Bern canton) origin | **PMID:18467358**; **PMID:36162733** |
| **South Asia (India, Pakistan, Sri Lanka; via gene flow to Indonesia, Malaysia)** | 25-bp intron-32 deletion | **~4% overall; 2–8% across 107 Indian ethnic populations** (287/6,273 individuals = 4.6%); absent from Northeast Indians, Siddis, Onges, and all 63 other world populations tested (2,085 individuals, 26 countries) | **PMID:19151713** |
| **Iceland** | Icelandic founder variant | Documented founder cohort | [PMC7174027](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7174027/) |
| **Northern Spain** | Novel truncating variant | Regional cohort | [PMC10137663](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10137663/) |

The South Asian deletion is quantitatively striking (verbatim, **PMID:19151713**):
> "Here, we describe a deletion of 25 bp in the gene encoding cardiac myosin binding protein C (MYBPC3) that is associated with heritable cardiomyopathies and an increased risk of heart failure in Indian populations (initial study OR = 5.3 (95% CI = 2.3-13), P = 2 x 10(-6); replication study OR = 8.59 (3.19-25.05), P = 3 x 10(-8); combined OR = 6.99 (3.68-13.57), P = 4 x 10(-11)) and that disrupts cardiomyocyte structure in vitro. Its prevalence was found to be high (approximately 4%) in populations of Indian subcontinental ancestry."

Population attributable risk of that deletion is **~4.5%**; the TMRCA of the deletion haplotype is **~33 ± 23 thousand years**, with no evidence of positive selection.

### Demographics

- **Sex ratio:** Carrier ratio ~1:1 (autosomal). **Penetrance is male-biased (65.1% vs 48.1%)**, so *diagnosed* CMH4 skews male, roughly 1.3–1.5:1. Women present later and with more advanced NYHA class — a recognised diagnostic inequity.
- **Age distribution of affected individuals:** peak diagnosis 4th–6th decades for monoallelic disease (Spanish cohort mean 47±16.8 yr, **PMID:39581692**); a distinct neonatal cluster for biallelic disease.
- **Geographic:** worldwide; founder clusters as above. Within India, deletion frequency is significantly higher in southern and western states than northern (P<4×10⁻⁸), paralleling a large cardiac-mortality gradient (386–422 vs 76–99 cardiac deaths/100,000) (**PMID:19151713**).

---

## 10. Diagnostics

### Clinical tests

**Imaging**
- **Transthoracic echocardiography** — first-line. Establishes max LV wall thickness (**≥15 mm** adults; **≥13–14 mm** with family history; **z-score >3** in children), morphology, SAM, LVOT gradient at rest and with Valsalva/exercise provocation, diastolic function, LA size. (PMID:20301725; PMID:38718139)
- **Exercise (stress) echocardiography** — mandatory when resting gradient <50 mmHg but symptoms suggest obstruction.
- **Cardiac MRI with late gadolinium enhancement (LGE)** — quantifies wall thickness where echo windows fail (apical/anterolateral), detects apical aneurysm, and quantifies **fibrosis burden**, an independent SCD risk marker (LGE ≥15% of LV mass). Also detects the pre-hypertrophic markers (myocardial crypts, elongated mitral leaflets) in G+/LVH− carriers.
- **Cardiac CT** — when CMR contraindicated.
- **RadLex/DICOM** applicable; no CMH4-specific imaging biomarker beyond generic HCM markers.

**Electrophysiology**
- **12-lead ECG** — abnormal in >90% of overt HCM; LVH voltage, deep T-wave inversion, pathological Q waves, left-axis deviation. Frequently abnormal **before** LVH in carriers.
- **Ambulatory (24–48 h Holter) ECG or extended monitoring** — detects NSVT (SCD risk factor) and paroxysmal AF. Guidelines recommend periodic monitoring.
- **Exercise treadmill testing with BP response** — abnormal blood-pressure response is an SCD risk factor; also yields functional capacity.
- **Cardiopulmonary exercise testing (pVO₂)** — the primary endpoint in EXPLORER-HCM and SEQUOIA-HCM; used for transplant evaluation.
- **Invasive EP study** — not routine.

**Laboratory / biomarkers**
- **NT-proBNP** (LOINC:33762-6) and **BNP** — severity/prognosis; treatment-response marker for myosin inhibitors.
- **High-sensitivity troponin I/T** — elevated even pre-hypertrophy (PMID:31877118).
- **Phenocopy screen** (essential, per PMID:38718139 — "HCM genetic testing should include genes for HCM phenocopies"):
  - **α-galactosidase A activity** (males) + **GLA** sequencing / plasma **lyso-Gb3** → Fabry disease
  - **Serum/urine free light chains, SPEP/UPEP, immunofixation** + **⁹⁹ᵐTc-PYP/DPD bone scintigraphy** → cardiac amyloidosis (ATTR/AL)
  - **Creatine kinase, LAMP2/PRKAG2 testing** → Danon disease, PRKAG2 glycogen storage cardiomyopathy
  - Carnitine, acylcarnitine profile, lactate → metabolic/mitochondrial phenocopies
  - Consider RASopathy panel in paediatric/syndromic presentations

**Biopsy / pathology**
- **Endomyocardial biopsy is not routine** for CMH4 diagnosis; reserved for suspected infiltrative disease.
- **Histopathology** (myectomy, explant, or autopsy) shows the classic triad: **cardiomyocyte hypertrophy**, **myocyte disarray** (loss of parallel alignment — the histopathological hallmark), and **interstitial/replacement fibrosis**, plus **intramural small-vessel medial hyperplasia**. From the Indian series (**PMID:19151713**, exact quotes): *"Histopathological section of the same subject showing hypertrophied myofibers separated from each other by increased connective tissue"*; *"'swirling' of hypertrophied myofibers amid connective tissue disarray."* In the lethal neonatal case: *"Postmortem examination revealed severe HCM, an atrial septal defect (ASD), and extensive myocardial necrosis and fibrosis."* (**PMID:41488457**, exact quote).
- Myoarchitectural disarray in HCM appears to **begin pre-birth** ([PMC6794206](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6794206/)).

### Genetic testing

**Recommended approach** (2024 AHA/ACC guideline, **PMID:38718139**; GeneReviews, **PMID:20301725**):

1. **Genetic counselling before and after testing** — "Evaluation by a genetic counselor is recommended to discuss risk and benefits of genetic testing."
2. **Multigene HCM panel** in the proband — must include the 8 definitive sarcomere genes (**MYBPC3**, MYH7, TNNT2, TNNI3, TPM1, ACTC1, MYL2, MYL3) **plus phenocopy genes** (GLA, LAMP2, PRKAG2, TTR, PTPN11 and other RASopathy genes, GAA, DES, FHL1, CSRP3, PLN, ALPK3). **Routine genetic testing is now recommended for all children meeting HCM diagnostic criteria.**
3. **Integrated CNV/deletion-duplication analysis or MLPA** — essential, because whole-gene and promoter MYBPC3 deletions are pathogenic and missed by sequence-only panels (**PMID:38258577**; **PMID:28771489**).
4. **Cascade (predictive) testing** of first-degree relatives — "Cascade genetic testing should be extended to first-degree relatives only if a pathogenic variant is identified in the proband." VUS results must **not** be used for cascade testing.
5. **Reflex to WES/WGS** when panel is negative and phenotype is atypical/syndromic. WGS additionally captures deep-intronic spliceogenic variants — an established elusive class in MYBPC3 ([Sci Rep 2022, PMC9068804](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9068804/)).
6. **RNA studies (allelic imbalance / RT-PCR splicing assay)** — the definitive functional confirmation for candidate spliceogenic MYBPC3 variants and for demonstrating haploinsufficiency (**PMID:30456444**; **PMID:19151713** used exactly this: cDNA from endomyocardial biopsy showed "a normal transcript and a mutant transcript with absence of exon 33").
7. **Molecular autopsy / postmortem trio WES** in unexplained sudden infant or young-adult death — **PMID:41488457** is the worked example: *"This 'molecular autopsy' established a definitive cause for the infant's death, linking a novel variant to a severe pathological phenotype. Crucially, the diagnosis guided the clinical management of the asymptomatic carrier parents, prompting long-term cardiac surveillance and enabling preimplantation genetic testing (PGT) for future family planning."* (exact quote)

**Modalities NOT indicated:** karyotyping, FISH, chromosomal microarray (unless syndromic features present), mtDNA testing (unless mitochondrial phenocopy suspected), repeat-expansion testing.

### Omics-based diagnostics
- **RNA-seq / targeted RT-PCR:** clinically deployed for splice-variant resolution and allelic imbalance (see above).
- **Proteomics / metabolomics / epigenomics / liquid biopsy:** research-stage only for CMH4. Circulating microRNA and proteomic panels for HCM phenotype conversion are in development but not validated.

### Clinical criteria and differential diagnosis

**Diagnostic criteria:** unexplained LVH with maximal wall thickness ≥15 mm (adults), ≥13 mm with family history or a known pathogenic variant, or z-score >3 (children), in the absence of abnormal loading conditions. (2024 AHA/ACC, PMID:38718139; 2023 ESC Cardiomyopathy Guidelines.)

**Differential diagnosis — the phenocopies (must be excluded):**

| Condition | Distinguishing feature |
|---|---|
| Hypertensive heart disease | Usually concentric, regresses with BP control; history |
| Aortic stenosis | Valve gradient on echo |
| Athlete's heart | Wall thickness usually <15 mm, dilated LV cavity, normal diastolic function, regresses with detraining |
| **Fabry disease** (GLA) | X-linked, low α-Gal A, ↑ lyso-Gb3, short PR interval, renal/neuropathic/skin features |
| **Cardiac amyloidosis** (ATTR/AL) | Positive bone scintigraphy or light chains; low-voltage ECG despite thick walls; apical sparing on strain |
| **Danon disease** (LAMP2) | X-linked, WPW, skeletal myopathy, intellectual disability, very high CK |
| **PRKAG2 syndrome** | Pre-excitation, conduction disease |
| **RASopathies** (Noonan/PTPN11 etc.) | Dysmorphism, pulmonary valve stenosis, short stature |
| **Pompe disease** (GAA) | Infantile hypotonia; enzyme assay |
| Mitochondrial cardiomyopathy | Multisystem, lactate, maternal inheritance |
| **Left ventricular noncompaction** | Overlaps with the *biallelic MYBPC3* phenotype specifically (PMID:25335496) |
| Neonatal: Beckwith-Wiedemann, infant of diabetic mother, Costello syndrome | Clinical context |

### Screening
- **Cascade genetic testing** of first-degree relatives once a P/LP variant is identified (the highest-yield strategy).
- **Clinical surveillance of at-risk relatives** (GeneReviews, **PMID:20301725**):
  - *Variant-positive relatives:* echocardiography + ECG **every 1–2 years**.
  - *Genetic status unknown, children/adolescents:* exam + ECG + echo **every 2–3 years**, starting before puberty.
  - *Genetic status unknown, adults:* **every 3–5 years**.
- **No newborn screening** exists or is recommended (no RUSP inclusion; no treatment window that screening would open for monoallelic disease). Founder-population carrier screening is a legitimate, locally-implemented exception (Amish community programmes; Dutch founder-variant cascade programmes).
- **Preconception/prenatal:** carrier screening in couples at risk for biallelic disease; **PGT-M** is established (PMID:41488457).

---

## 11. Outcome / Prognosis

### Survival and mortality

| Population | Outcome |
|---|---|
| **Clinically affected monoallelic MYBPC3 carriers** (UK, 82 individuals, 7.9±4.5 yr follow-up) | Annual **SCD 0.46%/yr**; **all-cause mortality 0.93%/yr** (**PMID:22267749**, exact figures) |
| **Spanish truncating-MYBPC3 cohort** (7.77 yr mean follow-up) | Relevant heart failure in **8.1%**; incident HCM phenotype 10%; "middle-aged adult patients (47±16.8 years) without significant comorbidities or symptoms"; EF preserved at 65%±10% (**PMID:39581692**, exact quotes) |
| **General HCM (all genotypes)** | SCD, resuscitated arrest, or appropriate ICD therapy in ~6%; LVEF<50% in ~8% (**PMID:20301725**) |
| **Biallelic truncating MYBPC3** | **Essentially 100% mortality in the first year without transplant.** All 21 reported cases "diagnosed with severe cardiomyopathy and/or died within the first few months of life" (**PMID:25335496**); the four index neonates "died from cardiac failure before age 13 weeks" |
| **Amish homozygous c.3330+2T>G** (23 infants) | "life span averaged 3 to 4 months, and all died before 1 year of age except for 2 children who underwent cardiac transplantation" (OMIM 115197, summarising **PMID:18467358**) |

Contemporary HCM cohorts under modern care (ICDs, myectomy, anticoagulation) approach **near-normal life expectancy** for many patients — a substantial improvement over historical tertiary-referral estimates. The MYBPC3 genotype has historically been described as favourable relative to MYH7; the Spanish cohort supports this ("previously associated with a favourable prognosis"; low event rates), while Page et al. caution that heterogeneity is such that genotype alone must not drive individual prognostication.

### Morbidity, disability, and quality of life

- **Functional limitation:** NYHA class II–III in trial-eligible obstructive patients; reduced pVO₂.
- **Atrial fibrillation and stroke:** ~20% AF overall, ~60% by age 60 if diagnosed <40 (PMID:20301725); thromboembolic stroke is a leading cause of morbidity, hence mandatory anticoagulation.
- **Heart failure:** 8.1% in the Spanish MYBPC3 cohort (PMID:39581692); progression to advanced HF requiring transplant in a minority.
- **ICD-related morbidity:** inappropriate shocks, lead complications, infection, psychological impact.
- **QoL instruments:** **KCCQ-CSS** and **HCMSQ-SoB** are the validated, trial-endorsed instruments (both used as EXPLORER-HCM secondary endpoints, **PMID:32871100**). EQ-5D and SF-36 also applied. ICF domains affected: mobility (d450 walking), major life areas (d840–859 work), recreation/leisure (d920 — sport restriction).
- **Family/psychosocial burden:** cascade-testing anxiety, insurance/employment implications, reproductive decision-making, bereavement after a family SCD.

### Complications
Atrial fibrillation → cardioembolic stroke; ventricular tachyarrhythmia → SCD; progressive diastolic HF; end-stage systolic ("burnt-out") HCM; apical aneurysm with mural thrombus; infective endocarditis (obstructive phenotype, historically); mitral regurgitation; conduction disease (post-septal reduction therapy, complete heart block requiring pacing).

### Prognostic factors and risk stratification

**HCM Risk-SCD** (ESC) and the **2024 AHA/ACC** risk-marker approach are the tools. Major risk markers:
- Prior cardiac arrest / sustained VT
- Family history of SCD in a first-degree relative
- Unexplained syncope
- Maximal LV wall thickness ≥30 mm
- Non-sustained VT on ambulatory monitoring
- LV apical aneurysm
- LVEF <50%
- **Extensive LGE (≥15% LV mass) on CMR** — arbitrator for intermediate-risk patients
- Abnormal BP response to exercise (ESC model)

**Genotype-specific prognostic points for CMH4:**
- **Truncating MYBPC3 variant location does *not* predict outcome** — "cause similar clinical severity and outcomes regardless of location, consistent with locus-independent loss-of-function" (**PMID:32841044**). Do not build a domain-based risk model for truncating alleles.
- **Compound/complex genotype** predicts worse outcome (PMID:22267749; PMID:39581692).
- **Biallelic status** is categorically prognostic (lethal neonatal).
- **Male sex and age ≥40** predict phenotype expression (PMID:22267749).
- **Genotype-positive status itself** (vs genotype-negative HCM) is associated with earlier onset and higher event rates in SHaRe.

**Prognostic biomarkers:** NT-proBNP, hs-troponin, LGE burden, LA volume index, global longitudinal strain.

---

## 12. Treatment

There is currently **no approved disease-modifying therapy specific to CMH4**; management targets the downstream physiology (obstruction, hypercontractility, arrhythmia, heart failure). Gene-replacement therapy is the first genuinely genotype-directed approach and is in early clinical trials.

### 12.1 Pharmacotherapy

| Therapy | Class / mechanism | Role | Ontology suggestion |
|---|---|---|---|
| **Beta-blockers** (metoprolol, bisoprolol, atenolol, propranolol) | β₁-adrenergic antagonist → ↓HR, ↑diastolic filling, ↓gradient | **First-line** for symptomatic obstructive and non-obstructive HCM | `NCIT:C15986` Pharmacotherapy + `therapeutic_agent` **CHEBI:6904** metoprolol (verified); modality `SMALL_MOLECULE` |
| **Non-dihydropyridine CCBs** (verapamil, diltiazem) | L-type Ca²⁺ channel blockade → ↓contractility, improved relaxation | Second-line / β-blocker intolerant. **Caution/contraindicated** in severe obstruction + hypotension | `NCIT:C15986` + **CHEBI:9948** verapamil (verified) |
| **Disopyramide** | Class Ia antiarrhythmic with potent **negative inotropy** | Add-on for refractory obstruction; must be paired with AV-nodal blockade | `NCIT:C15986` + **CHEBI:4657** disopyramide (verified) |
| **Mavacamten (Camzyos)** | **First-in-class cardiac myosin ATPase inhibitor** — reduces actin-myosin cross-bridge formation, restores SRX, ↓hypercontractility | **FDA approved April 2022** for symptomatic obstructive HCM. Mechanistically the direct counterpart of the CMH4 lesion | `NCIT:C15986` + **NCIT:C174901** Mavacamten (verified); modality `SMALL_MOLECULE` |
| **Aficamten (Myqorzo)** | Next-generation cardiac myosin inhibitor (shorter half-life, less EF-lowering) | **FDA approved 19 Dec 2025**; US availability Jan 2026; REMS with echo monitoring | `NCIT:C15986` + **NCIT:C179072** Aficamten (verified) |
| **Loop diuretics** | Volume reduction | Congestive symptoms; **use cautiously** — can worsen dynamic obstruction | `NCIT:C15986` |
| **Oral anticoagulation** (DOACs; warfarin if mechanical valve) | Thromboembolism prevention | **Mandatory** for HCM + AF regardless of CHA₂DS₂-VASc | `NCIT:C15986` |
| **Antiarrhythmics** (amiodarone, sotalol) | Rhythm control for AF/VT | Adjunct | `NCIT:C15986` |
| **Standard GDMT for HF** (ACEi/ARB, MRA, SGLT2i, beta-blocker) | | Only in the **end-stage/"burnt-out"** systolic phase; **avoid vasodilators in obstructive physiology** | |

**Drugs to AVOID in obstructive CMH4:** pure vasodilators (nitrates, dihydropyridine CCBs, hydralazine), high-dose diuretics, positive inotropes (digoxin, dobutamine) — all increase the dynamic gradient.

**EXPLORER-HCM efficacy (verbatim, PMID:32871100):**
> "45 (37%) of 123 patients on mavacamten versus 22 (17%) of 128 on placebo met the primary endpoint (difference +19·4%, 95% CI 8·7 to 30·1; p=0·0005). Patients on mavacamten had greater reductions than those on placebo in post-exercise LVOT gradient (-36 mm Hg, 95% CI -43·2 to -28·1; p<0·0001), greater increase in pVO2 (+1·4 mL/kg per min, 0·6 to 2·1; p=0·0006)"
> "Safety and tolerability were similar to placebo. Treatment-emergent adverse events were generally mild."

**SEQUOIA-HCM (aficamten)**, Maron MS et al., N Engl J Med 2024;390(20):1849–1861, **PMID:38739079**: 282 patients randomised at 101 centres; pVO₂ improved by a least-squares mean difference of **+1.74 mL/kg/min** (p=0.000002); **all 10 secondary endpoints** met; serious TEAEs 5.6% (aficamten) vs 9.3% (placebo). Efficacy extends to mildly symptomatic patients ([Eur Heart J 2025](https://academic.oup.com/eurheartj/article/46/40/4076/8133640)) and improves disease/symptom burden ([JACC 2024](https://www.jacc.org/doi/10.1016/j.jacc.2024.09.003)).

**Pharmacogenomics.** Both myosin inhibitors are **CYP2C19**-metabolised (mavacamten predominantly; also CYP3A4/2C9). **CYP2C19 poor metabolisers require dose reduction and more intensive echo monitoring for LVEF decline** — mavacamten labelling carries CYP2C19-genotype-relevant dosing guidance, and this is one of the few genuine pharmacogenomic considerations in HCM care (PharmGKB/CPIC-relevant). Concomitant strong CYP2C19/CYP3A4 inhibitors are contraindicated or require dose adjustment. There is **no MYBPC3-genotype-directed drug selection** at present.

### 12.2 Advanced therapeutics

**Gene therapy — the flagship CMH4-specific programme.**

*Preclinical* (Greer-Short et al., Nat Commun 2025, **PMID:40038304**, exact quotes):
> "Loss-of-function mutations in Myosin Binding Protein C3, MYBPC3, are the most common genetic cause of HCM, with the majority of mutations resulting in haploinsufficiency. To restore cardiac MYBPC3, we use an adeno-associated virus (AAV9) vector and engineer an optimized expression cassette with a minimal promoter and cis-regulatory elements (TN-201) to enhance packaging efficiency and cardiomyocyte expression."
> "Rather than simply preventing cardiac dysfunction preclinically, we demonstrate in a symptomatic MYBPC3-deficient murine model the ability of AAV gene therapy to reverse cardiac hypertrophy and systolic dysfunction, improve diastolic dysfunction, and prolong survival. Dose-ranging efficacy studies exhibit restoration of wild-type MYBPC3 protein levels and saturation of cardiac improvement at the clinically relevant dose of 3E13 vg/kg, outperforming a previously published construct."

*Clinical* — **MyPEAK-1 (NCT05836259)**, Phase 1b/2, open-label dose-escalation of single IV TN-201 in symptomatic adults with MYBPC3-associated HCM:
- First-in-human results: Desai MY et al., *Cardiovasc Res* 2025;121(17):2628–2631, **PMID:41206746** — *"First-in-human study of TN-201, an AAV9 gene replacement therapy in MYBPC3-associated hypertrophic cardiomyopathy."*
- Interim data presented at AHA Scientific Sessions 2025: 3 patients at 3E13 vg/kg (Cohort 1, ≥1 yr follow-up) and 3 at 6E13 vg/kg (Cohort 2). Reported dose-dependent transgene RNA expression, increasing cMyBP-C protein at one year, with biomarkers stable or improved ([Tenaya press release, 8 Nov 2025](https://investors.tenayatherapeutics.com/news-releases/news-release-details/tenaya-therapeutics-presents-promising-interim-clinical-data)).
- **⚠️ On 7 November 2025 the FDA placed MyPEAK-1 on clinical hold.** This must be recorded alongside the efficacy signal. TN-201 holds EMA **PRIME** designation.
- Eligibility gating: pre-existing anti-AAV9 neutralising antibodies exclude patients; seroeligibility in this population was assessed by Desai MY et al., *Front Med* 2025;12:1635586, **PMID:41020222**.

Suggested annotation: `therapeutic_modality: GENE_THERAPY`; `treatment_term` **NCIT:C15238** Gene Therapy.

**Other advanced modalities:**
- **Gene editing (base/prime editing) and allele-specific silencing** — preclinical only for MYBPC3.
- **ASO / siRNA** — **not applicable** to CMH4's dominant mechanism. Because the lesion is *loss* of protein via NMD, knockdown strategies are mechanistically wrong; the ASO paradigms in the dismech `antisense_oligonucleotide_therapy` module do not map here. (A theoretical NMD-inhibition or exon-skipping-to-restore-frame approach has been proposed but is not in trials.)
- **Cell therapy / immunotherapy** — not applicable.
- **Targeted therapy** — cardiac myosin inhibitors *are* the targeted therapy class for HCM (targeting the downstream hypercontractility rather than the gene).

### 12.3 Surgical and interventional

| Intervention | Indication | NCIT |
|---|---|---|
| **Surgical septal myectomy (Morrow procedure)** | Drug-refractory symptomatic obstruction (gradient ≥50 mmHg, NYHA III–IV); gold standard at experienced centres; operative mortality <1% | `NCIT:C15329` Surgical Procedure (no specific "septal myectomy" NCIT term confirmed) |
| **Alcohol septal ablation** | Drug-refractory obstruction in patients unsuitable for surgery; risk of complete heart block | `NCIT:C15329` / `NCIT:C49236` Therapeutic Procedure |
| **Mitral valve repair/replacement** | Intrinsic mitral pathology contributing to obstruction | `NCIT:C15329` |
| **ICD implantation** | Secondary prevention (prior arrest/sustained VT) or primary prevention per risk score | **NCIT:C80435** Implantable Cardioverter-Defibrillator Placement (verified); device **NCIT:C93238**; modality `DEVICE` |
| **Catheter ablation** | Symptomatic AF; VT ablation in selected cases | `NCIT:C49236` |
| **Heart transplantation** | End-stage HCM; **the only survival-altering intervention for biallelic neonatal disease** | **NCIT:C15246** Heart Transplantation (verified); modality `SURGERY` |
| **LVAD** | Bridge to transplant (technically challenging in small, non-dilated LV cavities) | `DEVICE` |

### 12.4 Supportive and rehabilitative
- Symptom-directed care, volume management, sleep-apnoea screening and treatment.
- **Cardiac rehabilitation / structured moderate exercise** — the 2024 guideline liberalised exercise recommendations; moderate-intensity recreational exercise is now considered beneficial and safe for most patients, with shared decision-making for higher intensities. `NCIT:C15315` Rehabilitation.
- Weight management, BP control, alcohol moderation. `NCIT:C15447` Dietary Intervention; modality `BEHAVIORAL`.
- Psychological support, particularly around ICD carriage and family SCD.
- **Genetic counselling** (`NCIT:C15240`) is a formal component of care, not an adjunct.

### 12.5 Experimental / trials

| Trial | Agent | Phase | NCT |
|---|---|---|---|
| MyPEAK-1 | **TN-201** AAV9-MYBPC3 gene therapy | 1b/2 | **NCT05836259** (on FDA clinical hold as of 7 Nov 2025) |
| EXPLORER-HCM | Mavacamten | 3 (completed) | **NCT03470545** |
| SEQUOIA-HCM | Aficamten | 3 (completed) | NCT05186818 |
| MAPLE-HCM | Aficamten vs metoprolol monotherapy | 3 | NCT05767346 |
| VALOR-HCM | Mavacamten (SRT-eligible patients) | 3 | NCT04349072 |
| VANISH | Valsartan in early sarcomeric HCM (disease modification in G+/early phenotype) | 2 | NCT01912534 |

### 12.6 Treatment strategy / algorithm

```
Confirmed CMH4 (MYBPC3 P/LP variant + phenotype)
│
├── Asymptomatic, no obstruction ──► Surveillance + SCD risk stratification
│                                     ± ICD if high risk; lifestyle counselling
│
├── Symptomatic, OBSTRUCTIVE (gradient ≥50 mmHg rest or provoked)
│      Step 1: beta-blocker  →  Step 2: verapamil/diltiazem (if BB-intolerant)
│      Step 3: add disopyramide  OR  cardiac myosin inhibitor
│              (mavacamten / aficamten) — with serial echo LVEF monitoring
│      Step 4: septal reduction therapy (myectomy preferred; ASA if
│              surgically unsuitable) at an experienced centre
│
├── Symptomatic, NON-OBSTRUCTIVE
│      Beta-blocker / CCB; diuretics for congestion; treat AF;
│      evaluate for advanced HF therapies if LVEF falls
│
├── ATRIAL FIBRILLATION ──► Anticoagulate (mandatory) + rate/rhythm control ± ablation
│
├── HIGH SCD RISK ──► ICD
│
└── END-STAGE (LVEF <50%) ──► GDMT + transplant evaluation
                               (stop myosin inhibitor)
```
Reference: 2024 AHA/ACC/AMSSM/HRS/PACES/SCMR Guideline, **PMID:38718139**; 2023 ESC Cardiomyopathy Guidelines.

**Personalised medicine.** Genotype currently drives *family screening and reproductive counselling*, not drug choice. TN-201, if it clears the clinical hold, would be the first genotype-restricted therapy (MYBPC3 haploinsufficiency + AAV9-seronegative). CYP2C19 genotype is the only actionable pharmacogene.

---

## 13. Prevention

### Primary prevention (preventing disease occurrence)
- **The disease itself cannot be prevented** in a variant carrier with current tools — no therapy is proven to prevent phenotype conversion. This is the central unmet need; VANISH (valsartan) is the flagship attempt.
- **Preventing transmission:** genetic counselling, prenatal diagnosis, and **preimplantation genetic testing for monogenic disease (PGT-M)** — explicitly enacted in **PMID:41488457**, where molecular autopsy diagnosis enabled "preimplantation genetic testing (PGT) for future family planning."
- **Modifiable-risk-factor control** (hypertension, obesity, metabolic syndrome) is biologically plausible as penetrance mitigation given the two-hit data, but **is not proven** to prevent conversion in humans. Curate this as a mechanistic hypothesis, not an established preventive.
- **Immunization:** not applicable to CMH4 pathogenesis. (Routine influenza/COVID/pneumococcal vaccination is standard care for anyone with structural heart disease, to prevent decompensation.)

### Secondary prevention (early detection)
- **Cascade genetic testing** of first-degree relatives — the single highest-yield intervention. Extends only when a P/LP variant is found in the proband (PMID:38718139).
- **Serial clinical surveillance** of at-risk relatives at the intervals given in §10.
- **Founder-population screening programmes:** the Dutch founder-variant cascade programme and Amish community screening (10% carrier frequency in Geauga County) are the two operationalised examples. In South Asia, the 25-bp deletion's ~4% carrier frequency has been proposed for population genotyping: *"genotyping could be used for the identification of persons at risk of heart failure among South Asians and could be accompanied by advice for a lower-risk lifestyle"* (**PMID:19151713**, exact quote) — this remains a proposal, not implemented policy.
- **No newborn screening**; not on the RUSP. The biallelic neonatal form is the only presentation with a theoretical NBS rationale, and it fails the treatability criterion outside transplant-capable settings.
- **Pre-participation athlete screening** (ECG-inclusive, as in the Italian and some European models) detects HCM incidentally; its cost-effectiveness remains contested.

### Tertiary prevention (preventing complications in affected individuals)
- **ICD** for SCD prevention in high-risk patients — the definitive tertiary preventive.
- **Anticoagulation** for AF → stroke prevention (mandatory, CHA₂DS₂-VASc-independent in HCM).
- **Septal reduction therapy** to prevent progressive HF from chronic obstruction.
- **Avoidance of dehydration, vasodilators, and inotropes** in obstructive physiology.
- **AF screening** with periodic ambulatory monitoring.
- Blood-pressure and weight control to limit remodelling.

### Risk stratification
HCM Risk-SCD (ESC) and the 2024 AHA/ACC marker-based approach (see §11), with CMR-LGE as the arbitrator for intermediate-risk patients.

### Counselling
- Formal **genetic counselling** before and after testing (guideline Class I).
- Reproductive counselling covering AD 50% transmission risk, and — crucially for CMH4 — **the recessive biallelic risk when both partners carry truncating MYBPC3 variants**, which is a real scenario in founder populations and consanguineous families. This is the single most consequential CMH4-specific counselling point.
- Counselling must convey **incomplete, age- and sex-dependent penetrance**: a positive predictive test does not mean certain disease (population penetrance 11–18%; family-based ~55%).

### Public health / environmental
- Community AED placement and CPR training in schools and sports venues.
- Founder-population health education (Amish, Dutch, South Asian diaspora).
- No environmental intervention applies.

---

## 14. Other Species / Natural Disease

### Taxonomy and natural disease

**Domestic cat — *Felis catus*, NCBITaxon:9685** is the outstanding natural model. Feline HCM is the most common feline heart disease and is **genuinely MYBPC3-driven**, making it a true comparative-pathology counterpart rather than an induced model.

| OMIA entry | Phenotype |
|---|---|
| **OMIA:000515-9685** | Cardiomyopathy, hypertrophic, in *Felis catus* |
| **OMIA:002951-9685** | Cardiomyopathy, hypertrophic, **MYBPC3-related, autosomal dominant** |
| **OMIA:002952-9685** | Cardiomyopathy, hypertrophic, **MYBPC3-related, autosomal recessive** |

**Breeds (VBO-relevant):**
- **Maine Coon** — **MYBPC3 p.A31P** (c.91G>C, exon 3; Ala→Pro, predicted conformational change). Restricted to Maine Coons.
- **Ragdoll** — **MYBPC3 p.R820W** (C>T; Arg→Trp). Restricted to Ragdolls.
- A third variant, **A74T**, is a widely distributed polymorphism of uncertain significance.

**Genotype–phenotype in cats** (directly parallel to the human allelic-dose relationship):
> "HCM was most prevalent in Maine Coon homozygotes for the A31P mutation and the penetrance increased with age. The penetrance of the heterozygote genotype was lower (0.08) compared to the P/P genotype (0.58) in Maine Coon."

Transmission is autosomal dominant **with incomplete penetrance** — "the mutation does not appear to behave as a simple dominant trait, but rather as a dominant trait with incomplete penetrance." Age-dependent penetrance and homozygote-severity gradient are exactly the human pattern.

Sources: [Longeri et al., J Vet Intern Med 2013](https://doi.org/10.1111/jvim.12031); [OMIA:002951](https://omia.org/OMIA002951/9685/); [OMIA:002952](https://omia.org/OMIA002952/9685/); [Maine Coon p.A31P clinical significance, PMC3044103](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3044103/); [Feline HCM advances 2025, PMC11946439](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11946439/).

**Veterinary importance:** Feline HCM causes congestive heart failure, **aortic thromboembolism ("saddle thrombus")** — a feline-specific complication with no direct human counterpart in HCM — and sudden death. Genotype testing (UC Davis VGL, LabGenVet) is used in breeding programmes to reduce allele frequency. This is a live example of population-level allele management.

### Orthologous genes

| Species | NCBITaxon | Gene | NCBI Gene ID |
|---|---|---|---|
| Human | 9606 | MYBPC3 | 4607 |
| Mouse | 10090 | Mybpc3 | 17868 |
| Rat | 10116 | Mybpc3 | 116717 |
| Cat | 9685 | MYBPC3 | 100135684 |
| Zebrafish | 7955 | mybpc3 | 559147 |

### Comparative biology
- **Conservation:** the C0–C10 domain architecture, the cardiac-specific C0 domain and PKA-phosphorylatable M-domain, and the C-zone A-band localisation are conserved across mammals. The thick-filament SRX regulatory mechanism is deeply conserved.
- **Comparative pathology:** cat and human share asymmetric septal hypertrophy, myocyte disarray, interstitial fibrosis, LVOT obstruction with SAM, diastolic dysfunction, atrial enlargement/thrombosis, arrhythmia, and sudden death. Differences: **cats develop aortic thromboembolism far more readily**; feline HCM is more often diagnosed by auscultation of a dynamic murmur; the human LVNC/septal-defect biallelic phenotype has no clear feline analogue.
- **Mouse divergence:** heterozygous *Mybpc3* mice are largely phenotype-negative without a second hit, unlike humans — a genuine **HUMAN_MODEL_MISMATCH** for the dismech schema.

### Transmission
**Not zoonotic. No cross-species transmission.** CMH4 is a germline Mendelian disorder; the feline disease is an independent, convergent MYBPC3 disorder, not transmitted between species.

---

## 15. Model Organisms

### 15.1 Mouse (*Mus musculus*, NCBITaxon:10090) — the primary in vivo model

| Model | Type | Phenotype | Notes / source |
|---|---|---|---|
| ***Mybpc3*<sup>InsG/InsG</sup>** (homozygous knock-in of the Dutch c.2373insG) | Knock-in, homozygous | "cardiac and cellular hypertrophy, and severe contractile dysfunction"; cardiac hypertrophy with **severe LV systolic and diastolic dysfunction**; contractile dysfunction already present at 3–4 weeks | The canonical Carrier-lab model; [J Mol Cell Cardiol 2023](https://www.sciencedirect.com/science/article/pii/S0022282823001633) |
| ***Mybpc3*<sup>+/InsG</sup>** (heterozygous) | Knock-in, heterozygous | **No cardiac phenotype at 18–28 weeks vs WT** — recapitulates human non-penetrance | Same |
| ***Mybpc3*<sup>c.772G>A</sup> heterozygous + Western diet** | Knock-in + dietary challenge | Western diet **triggered** cardiac dysfunction and hypertrophy in otherwise phenotype-negative hets — **two-hit model** | [PMC11708371](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11708371/) |
| ***Mybpc3* knockout (cMyBP-C null)** | Constitutive KO | Cardiac hypertrophy; **structural mitral valve abnormalities**; disrupted myosin SRX | [PMC4725593](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4725593/); SRX: **PMID:27021517** |
| ***Mybpc3* promoter-deletion heterozygote** | Regulatory KO | "developed a late-onset phenotype of **asymmetrical septal hypertrophy associated with fibrosis**" — the best mouse recapitulation of adult human CMH4 | **PMID:38258577** |
| **Symptomatic MYBPC3-deficient murine model (TN-201 studies)** | Gene-therapy testbed | AAV9-MYBPC3 "reverse[d] cardiac hypertrophy and systolic dysfunction, improve[d] diastolic dysfunction, and prolong[ed] survival" | **PMID:40038304** |

### 15.2 Human iPSC and engineered tissue — the leading in vitro system

- **CRISPR-Cas9 isogenic MYBPC3 allelic series in human iPSCs** (WT / cMyBP-C<sup>+/-</sup> / cMyBP-C<sup>-/-</sup>), differentiated to cardiomyocytes and assembled into **cardiac micropatterns** and **engineered cardiac tissues (ECTs)** — **PMID:36893011**. This is the highest-fidelity human system currently available and reproduces the allelic-dose severity gradient, the haploinsufficiency-in-3D phenomenon ("While heterozygous frame shifts did not alter cMyBP-C protein levels in 2-D cardiomyocytes, cMyBP-C+/- ECTs were haploinsufficient" — exact quote), and the hypercontractile→hypocontractile trajectory.
- **Patient-derived iPSC lines** from Dutch founder-variant families with variable HCM severity — enables isogenic-vs-background comparison of modifiers ([Stem Cell Res 2025](https://www.sciencedirect.com/science/article/pii/S1873506125000479)).
- **Neonatal rat ventricular cardiomyocytes** with adenoviral WT vs mutant cMyBP-C — the classic sarcomere-disorganisation readout (**PMID:19151713**).
- **Human myectomy / explant tissue** — the gold standard for demonstrating haploinsufficiency, allelic imbalance, and absent truncated protein (**PMID:19574547**; **PMID:22057632**; **PMID:37797718**; **PMID:30456444**).
- **Cardiac fibroblast cultures** — for the fibroblast-autonomous fibrosis arm (**PMID:36357371**).

### 15.3 Other systems
- **Zebrafish (*Danio rerio*, NCBITaxon:7955)** — *mybpc3* morphant/mutant work exists for cardiac development; less used for HCM modelling than mouse or iPSC.
- ***Drosophila*** — a Human Disease Model report for CMH4 exists ([FlyBase FBhh0000414](https://flybase.org/reports/FBhh0000414.html)), but *Drosophila* lacks a true cMyBP-C ortholog with cardiac-specific C0/M-domain regulation; utility is limited to generic sarcomere biology.
- ***C. elegans*, yeast** — not applicable.

### 15.4 Phenotype recapitulation and limitations

**Recapitulated well:**
- Allelic-dose severity gradient (het mild/absent → homozygous severe) — mouse, iPSC-ECT, cat
- Haploinsufficiency without poison peptide — human tissue, mouse, iPSC-ECT
- Late-onset asymmetric septal hypertrophy with fibrosis — promoter-deletion mouse
- Contractile hypercontractility → hypocontractility trajectory — iPSC-ECT
- Ca²⁺-handling deterioration — iPSC-ECT
- SRX disruption — mouse KO, human tissue
- Rescue by MYBPC3 restoration — mouse gene therapy

**Not recapitulated (`HUMAN_MODEL_MISMATCH` candidates for the dismech entry):**
1. **Heterozygous mice are phenotype-negative** without a second hit, whereas ~55% of human heterozygotes develop HCM in family-based studies. The mouse *underestimates* dominant penetrance. (Conversely, this is arguably a *faithful* model of the 11–18% population penetrance — the mismatch is really about which human population is the referent, which is itself a curatable question.)
2. **Myocyte disarray** — the human histopathological hallmark — is poorly reproduced in mice.
3. **Dynamic LVOT obstruction with SAM**, the dominant clinical problem, does not occur in mice (small, differently shaped LV; different mitral apparatus).
4. **Atrial fibrillation and thromboembolic stroke** are not modelled in mice.
5. **Sudden cardiac death from VT/VF** in a structurally HCM heart is not reliably reproduced.
6. **iPSC-CMs are immature** — fetal-like sarcomeres, negative force-frequency relationship, low mitochondrial density. Time-in-culture (2 wk vs 6 wk in **PMID:36893011**) is itself a variable, which is why that study's progressive phenotype is interpretable but not directly age-mappable to human decades.
7. **The biallelic neonatal LVNC + septal-defect phenotype** — septal defects have not been convincingly modelled.
8. **Species differences in cMyBP-C phosphorylation stoichiometry** and in the alpha/beta myosin heavy-chain ratio (mouse ventricle is α-MHC-dominant, human is β-MHC-dominant) limit direct translation of contractile measurements.

### 15.5 Research applications
Mechanism of haploinsufficiency and NMD; SRX/thick-filament regulation; Ca²⁺-handling; energetics; fibrosis; **preclinical gene-therapy dose-finding and efficacy** (the direct enabler of TN-201, PMID:40038304); myosin-inhibitor pharmacology; G×E (diet, exercise, hypertension) second-hit modelling.

### 15.6 Model resources
**MGI** (mouse; *Mybpc3* MGI:1338871), **IMPC**, **IMSR**, **JAX**, **MMRRC**, **EMMA** (mouse strains); **RGD** (rat); **ZFIN** (zebrafish); **Cellosaurus**/**hPSCreg** (iPSC lines); **OMIA** (feline natural disease); **Alliance of Genome Resources** (cross-species integration).

---

## Appendix A — Consolidated Ontology Term Suggestions

**Disease:** MONDO:0007268 hypertrophic cardiomyopathy 4 (parent MONDO:0005045)

**Gene:** `hgnc:7551` MYBPC3 (lowercase prefix per dismech convention)

**HPO (all verified against `sqlite:obo:hp`):**
HP:0001639 Hypertrophic cardiomyopathy · HP:0001712 Left ventricular hypertrophy · HP:0001670 Asymmetric septal hypertrophy · HP:0002094 Dyspnea · HP:0001681 Angina pectoris · HP:0001962 Palpitations · HP:0001279 Syncope · HP:0001635 Congestive heart failure · HP:0005110 Atrial fibrillation · HP:0004308 Ventricular arrhythmia · HP:0001695 Cardiac arrest · HP:0001645 Sudden cardiac death · HP:0011675 Arrhythmia
*(Additional terms to verify before use: HP:0031573, HP:0025168, HP:0011664, HP:0001631, HP:0001629, HP:0001643, HP:0001508, HP:0011968, HP:0001653, HP:0003115, HP:0031185, HP:0003829, HP:0000006, HP:0000007)*

**GO BP (verified):** GO:0006936 muscle contraction · GO:0060048 cardiac muscle contraction · GO:0030049 muscle filament sliding · GO:0000381 regulation of alternative mRNA splicing, via spliceosome · GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process · GO:0006402 mRNA catabolic process · GO:0032781 positive regulation of ATP-dependent activity
*(To verify: GO:0000184 NMD, GO:0003300 cardiac muscle hypertrophy, GO:0045214 sarcomere organization, GO:0031430 M band, GO:0030017 sarcomere, GO:0030018 Z disc)*

**CL (verified):** CL:0000746 cardiac muscle cell · CL:0002548 fibroblast of cardiac tissue · CL:0000057 fibroblast

**UBERON (verified):** UBERON:0000948 heart · UBERON:0002084 heart left ventricle · UBERON:0002094 interventricular septum · UBERON:0002349 myocardium · UBERON:0002078 right cardiac atrium

**CHEBI (verified):** CHEBI:6904 metoprolol · CHEBI:9948 verapamil · CHEBI:4657 disopyramide
*(Mavacamten and aficamten are absent from the local CHEBI adapter — use NCIT.)*

**NCIT (verified):** NCIT:C174901 Mavacamten · NCIT:C179072 Aficamten · NCIT:C80435 Implantable Cardioverter-Defibrillator Placement · NCIT:C93238 Implantable Cardioverter-Defibrillator · NCIT:C15246 Heart Transplantation
*(To verify: NCIT:C15986 Pharmacotherapy, NCIT:C15238 Gene Therapy, NCIT:C15329 Surgical Procedure, NCIT:C15240 Genetic Counseling, NCIT:C15315 Rehabilitation, NCIT:C49236 Therapeutic Procedure)*

**Candidate dismech `conforms_to` module targets:**
- `cardiomyopathy_maladaptive_remodeling#Ventricular Remodeling` — the structural/contractile cardiomyopathy final common pathway
- `fibrotic_response#Mesenchymal Cell Activation` — the cardiac-fibroblast arm (PMID:36357371)
- `thrombogenesis#Coagulation Cascade Activation and Thrombin-Driven Fibrin Formation` — the AF→cardioembolic-stroke arm (indirect; consider whether it belongs on this entry or on a comorbidity entry)
- Note: `cardiac_ion_channel_repolarization` is **not** appropriate — CMH4 is a structural/contractile cardiomyopathy in a structurally *abnormal* heart, not an inherited channelopathy in a structurally normal heart. The arrhythmic substrate here is disarray + fibrosis + ischemia, not a repolarization defect.
- `antisense_oligonucleotide_therapy` is **not** applicable (see §12.2).

---

## Appendix B — Evidence Register

### Verified locally (abstract/full text present in `references_cache/`; snippets above are exact substrings)

| PMID | Citation | Evidence source |
|---|---|---|
| 19151713 | Dhandapany PS et al. *A common MYBPC3 (cardiac myosin binding protein C) variant associated with cardiomyopathies in South Asia.* Nat Genet 2009;41(2):187-91. doi:10.1038/ng.309 | HUMAN_CLINICAL (+ IN_VITRO for the cardiomyocyte arm) |
| 20301725 | Cirino AL, Channaoui N, Ho C. *Nonsyndromic Hypertrophic Cardiomyopathy Overview.* GeneReviews, 2008 Aug 5 [updated 2025 Mar 6] | HUMAN_CLINICAL (review) |
| 22057632 | Marston S et al. *How do MYBPC3 mutations cause hypertrophic cardiomyopathy?* J Muscle Res Cell Motil 2012;33(1):75-80 | HUMAN_CLINICAL (review of human tissue data) |
| 22267749 | Page SP et al. *Cardiac myosin binding protein-C mutations in families with hypertrophic cardiomyopathy: disease expression in relation to age, gender, and long term outcome.* Circ Cardiovasc Genet 2012;5(2):156-66 | HUMAN_CLINICAL |
| 25335496 | Wessels MW et al. *Compound heterozygous or homozygous truncating MYBPC3 mutations cause lethal cardiomyopathy with features of noncompaction and septal defects.* Eur J Hum Genet 2015;23(7):922-8 | HUMAN_CLINICAL |
| 32871100 | Olivotto I et al. *Mavacamten for treatment of symptomatic obstructive hypertrophic cardiomyopathy (EXPLORER-HCM).* Lancet 2020;396(10253):759-769 | HUMAN_CLINICAL (RCT) |
| 36893011 | De Lange WJ et al. *cMyBP-C ablation in human engineered cardiac tissue causes progressive Ca2+-handling abnormalities.* J Gen Physiol 2023;155(4):e202213204 | IN_VITRO |
| 37797718 | Burkart V et al. *Nonsense mediated decay factor UPF3B is associated with cMyBP-C haploinsufficiency in hypertrophic cardiomyopathy patients.* J Mol Cell Cardiol 2023;185:26-37 | HUMAN_CLINICAL (patient myocardium) |
| 38406555 | Ananthamohan K, Stelzer JE, Sadayappan S. *Hypertrophic cardiomyopathy in MYBPC3 carriers in aging.* J Cardiovasc Aging 2024;4:9 | HUMAN_CLINICAL (review) |
| 39581692 | Melendo-Viu M et al. *Hypertrophic cardiomyopathy due to truncating variants in myosin binding protein C: a Spanish cohort.* Open Heart 2024;11(2):e002891 | HUMAN_CLINICAL |
| 40038304 | Greer-Short A et al. *AAV9-mediated MYBPC3 gene therapy with optimized expression cassette enhances cardiac function and survival in MYBPC3 cardiomyopathy models.* Nat Commun 2025;16(1):2196 | MODEL_ORGANISM |
| 41488457 | Wang J et al. *Case Report: Lethal neonatal hypertrophic cardiomyopathy from compound heterozygous MYBPC3 variants.* Front Cardiovasc Med 2025;12:1726463 | HUMAN_CLINICAL |
| CGGV assertions (4) | ClinGen MYBPC3 gene-disease validity: HCM Definitive AD (2021-10-07); ARVC Limited (2019-08-06); DCM Limited AD and AR (2025-05-16) | OTHER |

### Identified and bibliographically verified via NCBI eutils; abstracts NOT locally cached — **fetch with `just fetch-reference PMID:xxxxx` and re-verify any snippet before committing to the KB**

| PMID | Citation |
|---|---|
| 18467358 | *Homozygous mutation of MYBPC3 associated with severe infantile hypertrophic cardiomyopathy at high frequency among the Amish.* Heart 2008 |
| 19574547 | Marston S et al. *Evidence from human myectomy samples that MYBPC3 mutations cause hypertrophic cardiomyopathy through haploinsufficiency.* Circ Res 2009 |
| 27021517 | McNamara JW et al. *Ablation of cardiac myosin binding protein-C disrupts the super-relaxed state of myosin in murine cardiomyocytes.* J Mol Cell Cardiol 2016 |
| 28658286 | McNamara JW et al. *MYBPC3 mutations are associated with a reduced super-relaxed state in patients with hypertrophic cardiomyopathy.* PLoS One 2017 |
| 28771489 | Mademont-Soler I et al. *Additional value of screening for minor genes and copy number variants in hypertrophic cardiomyopathy.* PLoS One 2017 |
| 30456444 | *Allelic imbalance and haploinsufficiency in MYBPC3-linked hypertrophic cardiomyopathy.* Pflügers Arch 2019 |
| 30674652 | Toepfer CN et al. *Hypertrophic cardiomyopathy mutations in MYBPC3 dysregulate myosin.* Sci Transl Med 2019 |
| 31877118 | Helms AS et al. *Effects of MYBPC3 loss-of-function mutations preceding hypertrophic cardiomyopathy.* JCI Insight 2020 |
| 32841044 | Helms AS et al. *Spatial and Functional Distribution of MYBPC3 Pathogenic Variants and Clinical Outcomes in Patients With Hypertrophic Cardiomyopathy.* Circ Genom Precis Med 2020 |
| 33532905 | *BIO FOr CARe: biomarkers of hypertrophic cardiomyopathy development and progression in carriers of Dutch founder truncating MYBPC3 variants.* Neth Heart J 2021 |
| 36162733 | *The «Amish» NM_000256.3:c.3330+2T>G splice variant in MYBPC3 associated with hypertrophic cardiomyopathy is an ancient Swiss mutation.* Eur J Med Genet 2022 |
| 36357371 | Zou X et al. *MYBPC3 deficiency in cardiac fibroblasts drives their activation and contributes to fibrosis.* Cell Death Dis 2022 |
| 36946992 | Barefield DY. *Is haploinsufficiency a sufficient mechanism for MYBPC3 truncating mutations?* J Gen Physiol 2023 |
| 37929589 | Topriceanu C et al. *Meta-Analysis of Penetrance and Systematic Review on Transition to Disease in Genetic Hypertrophic Cardiomyopathy.* Circulation 2024;149:107-123 |
| 38258577 | Hayesmoore JBG et al. *A Promoter Deletion Confirms That MYBPC3 Haploinsufficiency Is Sufficient to Cause Hypertrophic Cardiomyopathy in Humans.* Circ Genom Precis Med 2024 |
| 38718139 | Ommen SR, Ho CY et al. *2024 AHA/ACC/AMSSM/HRS/PACES/SCMR Guideline for the Management of Hypertrophic Cardiomyopathy.* Circulation 2024 |
| 38739079 | Maron MS et al. *Aficamten for Symptomatic Obstructive Hypertrophic Cardiomyopathy.* N Engl J Med 2024;390(20):1849-1861 |
| 39886308 | *Longitudinal Evaluation of Genetic Hypertrophic Cardiomyopathy Penetrance and Transition to Disease in an Academic Biobank.* JACC Adv 2025 |
| 41020222 | Desai MY et al. *High rate of seroeligibility among MYBPC3-associated hypertrophic cardiomyopathy patients for TN-201.* Front Med 2025;12:1635586 |
| 41134850 | Zhang Y et al. *A novel variant in MYBPC3 causes hypertrophic cardiomyopathy by haploinsufficiency.* PLoS One 2025 |
| 41206746 | Desai MY et al. *First-in-human study of TN-201, an AAV9 gene replacement therapy in MYBPC3-associated hypertrophic cardiomyopathy.* Cardiovasc Res 2025;121(17):2628-2631 |

### Non-PMID / structured and grey sources
OMIM 115197, OMIM \*600958 · ClinGen HCM GCEP reappraisal (PMC11312670) · ClinVar RCV000009149, RCV000009152 · Orphanet ORPHA:155, ORPHA:217569 · OMIA:000515-9685, OMIA:002951-9685, OMIA:002952-9685 · ClinicalTrials.gov NCT05836259, NCT03470545, NCT05186818, NCT05767346, NCT04349072, NCT01912534 · Tenaya Therapeutics investor releases (AHA 2025 interim data; 7 Nov 2025 FDA clinical hold) · Cytokinetics investor releases (Myqorzo/aficamten FDA approval 19 Dec 2025).

---

## Appendix C — Notable Gaps and Open Questions (candidate dismech `discussions`)

| Kind | Question |
|---|---|
| `KNOWLEDGE_GAP` | Is haploinsufficiency *sufficient* for all MYBPC3 truncating alleles, or do some contribute a parallel dominant-negative/proteotoxic effect? (PMID:36946992 vs PMID:22057632/38258577) |
| `KNOWLEDGE_GAP` | Why is penetrance 11–18% in population biobanks but ~55% in clinical families? How much is ascertainment vs genuine modifier burden vs environment? (PMID:37929589) |
| `KNOWLEDGE_GAP` | No therapy prevents phenotype conversion in G+/LVH− carriers. What is the intervention window and the right endpoint? |
| `HUMAN_MODEL_MISMATCH` | Heterozygous *Mybpc3* mice are phenotype-negative without a second hit; human heterozygotes reach ~55% penetrance in families. Which human referent population does the mouse actually model? |
| `HUMAN_MODEL_MISMATCH` | Myocyte disarray, the human histopathological hallmark, is poorly reproduced in mouse models. |
| `HUMAN_MODEL_MISMATCH` | Dynamic LVOT obstruction with SAM — the dominant clinical problem and the target of both approved drugs — cannot be modelled in mice; drug efficacy claims for that mechanism rest entirely on human trial data. |
| `KNOWLEDGE_GAP` | Does the Western-diet two-hit effect (mouse, PMC11708371) operate in human MYBPC3 carriers? No human interventional or prospective dietary data exist. |
| `KNOWLEDGE_GAP` | Reason for the FDA clinical hold on MyPEAK-1 (7 Nov 2025) and its implications for AAV9 cardiac gene therapy dosing — not yet in the peer-reviewed literature. |

---

## Sources

- [OMIM 115197 — CARDIOMYOPATHY, FAMILIAL HYPERTROPHIC, 4; CMH4](https://omim.org/entry/115197)
- [OMIM \*600958 — MYOSIN-BINDING PROTEIN C, CARDIAC; MYBPC3](https://www.omim.org/entry/600958)
- [MGI / Disease Ontology DOID:0110310](https://www.informatics.jax.org/disease/115197)
- [GeneReviews — Nonsyndromic Hypertrophic Cardiomyopathy Overview (NBK1768)](https://www.ncbi.nlm.nih.gov/books/NBK1768/)
- [ClinGen — Evaluating the Clinical Validity of Hypertrophic Cardiomyopathy Genes](https://clinicalgenome.org/docs/evaluating-the-clinical-validity-of-hypertrophic-cardiomyopathy-genes/)
- [ClinGen HCM Gene Reappraisal (PMC11312670)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11312670/)
- [Ingles et al., Circ Genom Precis Med 2019 — HCM gene clinical validity](https://www.ahajournals.org/doi/10.1161/CIRCGEN.119.002460)
- [Meta-Analysis of Penetrance… Genetic HCM, Circulation 2024](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.123.065987) · [ACC summary](https://www.acc.org/Latest-in-Cardiology/Journal-Scans/2024/01/18/15/41/meta-analysis-of-penetrance)
- [Low Penetrance Sarcomere Variants Contribute to Additive Risk in HCM, Circulation](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.124.069398)
- [Longitudinal Evaluation of Genetic HCM Penetrance in an Academic Biobank (PMC11780075)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11780075/)
- [Dutch MYBPC3 founder mutation outcomes, Circ Cardiovasc Genet 2017](https://www.ahajournals.org/doi/10.1161/CIRCGENETICS.116.001660)
- [BIO FOr CARe Dutch founder cohort (PMC8160056)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8160056/) · [PubMed 33532905](https://pubmed.ncbi.nlm.nih.gov/33532905/)
- [RAAS polymorphisms in MYBPC3-related HCM (PMC3449069)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3449069/)
- [Amish MYBPC3 c.3330+2T>G homozygosity, Heart 2008 (PMID 18467358)](https://pubmed.ncbi.nlm.nih.gov/18467358/)
- [The «Amish» c.3330+2T>G is an ancient Swiss mutation (PMID 36162733)](https://pubmed.ncbi.nlm.nih.gov/36162733/)
- [Icelandic MYBPC3 founder mutation carriers (PMC7174027)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7174027/)
- [Northern Spain truncating MYBPC3 cohort (PMC10137663)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10137663/)
- [Spatial and Functional Distribution of MYBPC3 Pathogenic Variants, Circ Genom Precis Med 2020](https://www.ahajournals.org/doi/10.1161/CIRCGEN.120.002929) · [PubMed 32841044](https://pubmed.ncbi.nlm.nih.gov/32841044/)
- [A Promoter Deletion Confirms MYBPC3 Haploinsufficiency Is Sufficient…, Circ Genom Precis Med](https://www.ahajournals.org/doi/10.1161/CIRCGEN.123.004134)
- [Effects of MYBPC3 loss-of-function mutations preceding HCM, JCI Insight](https://insight.jci.org/articles/view/133782) · [PMC7098724](https://pmc.ncbi.nlm.nih.gov/articles/PMC7098724/)
- [MYBPC3 mutations and reduced super-relaxed state, PLOS One 2017](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0180064) · [PMC5489194](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5489194/)
- [cMyBP-C phosphorylation regulates the super-relaxed state, PNAS](https://www.pnas.org/content/116/24/11731)
- [MYBPC3 deficiency in cardiac fibroblasts drives fibrosis (PMC9649783)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9649783/)
- [Spatial transcriptomics of myocyte disarray in human HCM (PMC10454036)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10454036/)
- [Myoarchitectural disarray of HCM begins pre-birth (PMC6794206)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6794206/)
- [MyBPC3 P459fs multi-omics and super-resolution imaging (PMC11903464)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11903464/)
- [ALU transposition induces familial HCM (PMC6978237)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6978237/)
- [Elusive spliceogenic MYBPC3 variant, Sci Rep 2022 (PMC9068804)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9068804/)
- [Computational prediction of MYBPC3 subdomain stability, Genet Med 2021](https://www.nature.com/articles/s41436-021-01134-9)
- [Mybpc3 c.2373InsG hetero/homozygous mouse characterization, J Mol Cell Cardiol 2023](https://www.sciencedirect.com/science/article/pii/S0022282823001633)
- [Western diet two-hit Mybpc3 mouse model (PMC11708371)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11708371/)
- [Targeted Mybpc3 knock-out mice with mitral valve abnormalities (PMC4725593)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4725593/)
- [AAV9-mediated MYBPC3 gene therapy (TN-201), Nat Commun 2025](https://www.nature.com/articles/s41467-025-57481-7)
- [First-in-human TN-201 MyPEAK-1, Cardiovasc Res 2025](https://academic.oup.com/cardiovascres/article/121/17/2628/8315802)
- [Tenaya — MyPEAK-1 interim clinical data, AHA 2025](https://investors.tenayatherapeutics.com/news-releases/news-release-details/tenaya-therapeutics-presents-promising-interim-clinical-data) · [GlobeNewswire](https://www.globenewswire.com/news-release/2025/11/08/3184075/0/en/Tenaya-Therapeutics-Presents-Promising-Interim-Clinical-Data-from-MYPEAK-1-Phase-1b-2a-Clinical-Trial-of-TN-201-Gene-Therapy-for-the-Treatment-of-MYBPC3-Associated-Hypertrophic-Car.html)
- [2024 AHA/ACC/AMSSM/HRS/PACES/SCMR HCM Guideline, Circulation](https://www.ahajournals.org/doi/10.1161/CIR.0000000000001250) · [JACC](https://www.jacc.org/doi/10.1016/j.jacc.2024.02.014) · [PubMed 38718139](https://pubmed.ncbi.nlm.nih.gov/38718139/) · [ACC Key Points](https://www.acc.org/latest-in-cardiology/ten-points-to-remember/2024/05/06/15/12/2024-hypertrophic-cardiomyopathy-gl)
- [SEQUOIA-HCM primary results, NEJM 2024](https://mediacenteratypon.nejmgroup-production.org/NEJMoa2401424.pdf) · [Aficamten in mildly symptomatic oHCM, Eur Heart J 2025](https://academic.oup.com/eurheartj/article/46/40/4076/8133640) · [Disease and symptom burden, JACC 2024](https://www.jacc.org/doi/10.1016/j.jacc.2024.09.003)
- [Cytokinetics — FDA approval of MYQORZO (aficamten), Dec 2025](https://ir.cytokinetics.com/press-releases/press-release-details/2025/Cytokinetics-Announces-FDA-Approval-of-MYQORZO-aficamten-for-the-Treatment-of-Adults-with-Symptomatic-Obstructive-Hypertrophic-Cardiomyopathy-to-Improve-Functional-Capacity-and-Symptoms/default.aspx) · [US availability, Jan 2026](https://ir.cytokinetics.com/press-releases/press-release-details/2026/Cytokinetics-Announces-MYQORZO-aficamten-Now-Available-in-the-U-S---for-the-Treatment-of-Adults-with-Symptomatic-Obstructive-Hypertrophic-Cardiomyopathy-to-Improve-Functional-Capacity-and-Symptoms/default.aspx) · [AJMC](https://www.ajmc.com/view/fda-approves-aficamten-for-obstructive-hypertrophic-cardiomyopathy) · [TCTMD](https://www.tctmd.com/news/fda-approves-aficamten-obstructive-hcm)
- [Prevalence of clinically apparent HCM in Germany (PMC5933727)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5933727/) · [Stable rates of obstructive HCM (PMC8770922)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8770922/)
- [Orphanet — Rare hypertrophic cardiomyopathy (ORPHA:217569)](https://www.orpha.net/en/disease/detail/217569) · [Familial isolated HCM (ORPHA:155)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Expert=155&Lng=EN)
- [MYBPC3 variants in domestic cats (A31P, A74T, R820W), J Vet Intern Med 2013](https://doi.org/10.1111/jvim.12031) · [OMIA:000515-9685](https://omia.org/OMIA000515/9685/) · [OMIA:002951-9685](https://omia.org/OMIA002951/9685/) · [OMIA:002952-9685](https://omia.org/OMIA002952/9685/) · [Maine Coon p.A31P clinical significance (PMC3044103)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3044103/) · [Feline HCM advances (PMC11946439)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11946439/) · [UC Davis VGL Maine Coon HCM test](https://vgl.ucdavis.edu/test/maine-coon-hcm)
- [iPSC lines from Dutch MYBPC3 founder families, Stem Cell Res 2025](https://www.sciencedirect.com/science/article/pii/S1873506125000479)
- [ClinVar RCV000009149 (MYBPC3 c.1224-19G>A / Familial HCM 4)](https://www.ncbi.nlm.nih.gov/clinvar/RCV000009149/) · [RCV000009152 (c.3330+2T>G / HCM 4)](https://www.ncbi.nlm.nih.gov/clinvar/RCV000009152/)
- [MalaCards — Cardiomyopathy, Familial Hypertrophic, 4](https://www.malacards.org/card/cardiomyopathy_familial_hypertrophic_4) · [FlyBase Human Disease Model FBhh0000414](https://flybase.org/reports/FBhh0000414.html)