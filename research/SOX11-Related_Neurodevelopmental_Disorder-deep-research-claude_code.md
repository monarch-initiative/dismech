---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-07-31T22:38:43.239580'
end_time: '2026-07-31T23:01:41.504347'
duration_seconds: 1378.26
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SOX11-Related Neurodevelopmental Disorder
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5[1m]
  web_search_requests: 8
  num_turns: 100
  total_cost_usd: 6.76514725
  session_id: 093928d4-5e79-455a-9ab5-e668b57d551a
  stop_reason: end_turn
citation_count: 53
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SOX11-Related Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SOX11-Related Neurodevelopmental Disorder** covering all of the
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

# Comprehensive Research Report: SOX11-Related Neurodevelopmental Disorder

**Prepared:** 2026-07-31 · **Target:** dismech knowledge base entry
**Gene:** *SOX11* (HGNC:11191) · **Primary MONDO:** MONDO:0100626

---

## ⚠️ Evidence-Quality Notice (read before curating)

| Marker | Meaning |
|---|---|
| **[VERBATIM]** | Abstract text retrieved word-for-word via Europe PMC REST API or the CC-BY published PDF. Safe candidate for an evidence `snippet:` — **still run `just fetch-reference` + `just validate-references`.** |
| **[PARAPHRASE]** | Retrieved only as a tool-generated summary. **DO NOT use as a `snippet:`.** Fetch the real abstract first. |
| **[FULL-TEXT]** | Extracted from the open-access (CC BY 4.0) published PDF of Al-Jawahiri et al. 2022 — body text, not abstract. Body-text quotes will **not** validate against a PubMed-abstract cache; use for `description:`/`notes:` or cite the abstract instead. |

Two **NEC (Named Entity Confusion) preflight risks** were checked and cleared, and one identifier discrepancy was found — see [§1.5](#15-nec-preflight-and-identifier-discrepancies).

---

## 1. Disease Information

### 1.1 Concise overview

*SOX11*-related neurodevelopmental disorder (commonly "SOX11 syndrome") is an **autosomal dominant, congenital-onset neurodevelopmental disorder caused by heterozygous loss-of-function of *SOX11***, a single-exon SRY-related HMG-box (SoxC) transcription factor at 2p25.2. The core phenotype is **developmental delay/intellectual disability with microcephaly, growth restriction, and mild fifth-digit/nail anomalies**, with three distinguishing features that separate it from classical Coffin-Siris syndrome: **oculomotor apraxia, structural ocular malformations (coloboma, microphthalmia, lens anomalies), and hypogonadotropic hypogonadism**.

The disorder's nosology has shifted materially since 2014. It was first reported *as* Coffin-Siris syndrome (CSS) and assigned CSS9/OMIM 615866, because *SOX11* is a transcriptional target downstream of the PAX6–BAF complex. The 2022 large-cohort study reclassified it as a **distinct clinical and molecular entity**, supported by a unique peripheral-blood DNA methylation episignature that separates it from the BAFopathies.

> **[VERBATIM — PMID:35341651, Al-Jawahiri et al., *Genet Med* 2022;24(6):1261–1273, DOI 10.1016/j.gim.2022.02.013]**
> **Purpose:** "This study aimed to undertake a multidisciplinary characterization of the phenotype associated with *SOX11* variants."
> **Methods:** "Individuals with protein altering variants in *SOX11* were identified through exome and genome sequencing and international data sharing. Deep clinical phenotyping was undertaken by referring clinicians. Blood DNA methylation was assessed using Infinium MethylationEPIC array. The expression pattern of *SOX11* in developing human brain was defined using RNAscope."
> **Results:** "We reported 38 new patients with *SOX11* variants. Idiopathic hypogonadotropic hypogonadism was confirmed as a feature of *SOX11* syndrome. A distinctive pattern of blood DNA methylation was identified in *SOX11* syndrome, separating *SOX11* syndrome from other BAFopathies."
> **Conclusion:** "*SOX11* syndrome is a distinct clinical entity with characteristic clinical features and episignature differentiating it from BAFopathies."

> **[VERBATIM — PMID:37558216, Pasquetti et al., *Clin Genet* 2024, DOI 10.1111/cge.14414]**
> "*SOX11* variants were initially reported to cause Coffin-Siris syndrome (CSS), characterised by growth restriction, moderate ID, coarse face, hypertrichosis and hypoplastic nails. However, recent studies have provided evidence that they give rise to a distinct neurodevelopmental disorder."
> "…we made a confirmation that overall *SOX11* abnormalities feature a distinctive disorder characterised by severe ID, high incidence of microcephaly and low frequency of congenital malformations."

### 1.2 Key identifiers

| Resource | Identifier | Label |
|---|---|---|
| **MONDO (recommended `disease_term`)** | **MONDO:0100626** | SOX11-related complex neurodevelopmental disorder with or without congenital anomalies |
| MONDO (recommended `mappings` → `skos:closeMatch`) | MONDO:0014376 | Intellectual developmental disorder with microcephaly and with or without ocular malformations or hypogonadotropic hypogonadism |
| OMIM (phenotype) | **615866** | IDDMOH; formerly "Coffin-Siris syndrome 9"; formerly "Mental retardation, autosomal dominant 27 (MRD27)" |
| OMIM (gene) | 600898 | SRY-BOX 11; SOX11 |
| HGNC | **hgnc:11191** | SOX11 (lowercase prefix per dismech convention) |
| NCBI Gene | 6664 | SOX11 |
| Ensembl | ENSG00000176887 | — |
| UniProt | P35716 | Transcription factor SOX-11 |
| RefSeq transcript | NM_003108.4 / NP_003099.1 | canonical (single transcript) |
| MedGen | C4014528 / UID 862965 | — |
| UMLS | C4014528 | — |
| DOID | DOID:0070057 | Coffin-Siris syndrome 9 |
| GARD | 0028004 (MONDO:0100626); 0016023 (MONDO:0014376) | — |
| ClinGen dosage / validity | HGNC:11191 | HI score **3**; validity **Definitive** (AD) |
| Orphanet | ORPHA:1465 (Coffin-Siris syndrome — umbrella) | *SOX11* is not separately ORPHA-coded; see §9 caveat |
| ICD-10 | Q87.8 (other specified congenital malformation syndromes) — no specific code | — |
| ICD-11 | LD2F.1Y / LD90.Y range — no specific code | — |
| MeSH | No specific descriptor; nearest = *Intellectual Disability* (D008607), *Microcephaly* (D008831), *Abnormalities, Multiple* (D000013) | — |

**Recommendation for the dismech entry:** use **MONDO:0100626** as `disease_term` (its label is a near-exact match for the entry name "SOX11-Related Neurodevelopmental Disorder", and it is the term the ClinGen Intellectual Disability and Autism GCEP used for its Definitive gene-disease validity assertion). Carry MONDO:0014376 and OMIM:615866 in `mappings`.

### 1.3 Synonyms and alternative names

- SOX11 syndrome *(preferred in the recent literature; Al-Jawahiri 2022, 2023)*
- SOX11-related disorder *(proposed as an umbrella framework: PMID:42168980)*
- Coffin-Siris syndrome 9 / CSS9 *(historical; still widely used in Chinese-language reports)*
- Coffin-Siris syndrome-like syndrome (CSSLS) *(used in the hESC modelling literature, PMID:31035284)*
- Intellectual developmental disorder with microcephaly and with or without ocular malformations or hypogonadotropic hypogonadism (IDDMOH) *(current OMIM title)*
- Mental retardation, autosomal dominant 27 / MRD27 *(historical, discouraged)*
- Autosomal dominant non-syndromic intellectual disability 27 *(DOID synonym, misleading — the disorder is syndromic)*

### 1.4 Provenance of the knowledge base

Information is **overwhelmingly aggregated disease-level**, derived from:
1. **Genotype-first research cohorts** — Deciphering Developmental Disorders (DDD) study exomes, the 100,000 Genomes Project, and GeneMatcher-mediated international data sharing (PMID:35341651). This is important: ascertainment is *genotype-first*, not phenotype-first, which reduces the phenotype-bias that inflated the early "Coffin-Siris" framing.
2. **Targeted phenotype-first cohorts** — a 1,810-proband idiopathic hypogonadotropic hypogonadism (IHH) cohort at Massachusetts General Hospital (PMID:39290158), and a 79-patient microphthalmia/anophthalmia/coloboma (MAC) cohort (PMID:25010521).
3. **Registry data** — the CSS/BAF registry (n=284, of whom 10 carried *SOX11* variants; PMID:35126043).
4. **Individual case reports** — a substantial and growing set, disproportionately from China, expanding the organ-anomaly spectrum.
5. **Curated databases** — ClinGen (dosage + validity), ClinVar, DECIPHER, MGI.

**No EHR-derived / individual-patient-level data source exists** for this disorder. There is no patient registry, no natural-history study, and no OMOP/EHR phenotype algorithm published. This is a genuine gap.

### 1.5 NEC preflight and identifier discrepancies

**NEC preflight (per dismech CLAUDE.md §2b):**
- ✅ **Gene check.** MONDO:0100626 and MONDO:0014376 both name *SOX11* as causal; the dominant gene across all retrieved literature is *SOX11*. No competing gene dominates.
- ✅ **OMIM check.** MONDO:0014376 xrefs OMIM:615866, matching every source. MONDO:0100626 does not carry an OMIM xref (it is a ClinGen/GARD-grounded term) but its `includedPhenotype` is MIM:615866 per ClinGen.
- ⚠️ **NEC-risk class flag.** This disorder sits in **two** high-NEC-risk classes from `research/nec_risk_disease_classes.md`: (a) a **numbered series** — "Coffin-Siris syndrome 9" is one of ≥14 numbered CSS entries, and (b) a **paralog family series** — *SOX4*-related NDD (PMID:30661772, 35232796), *SOX11*, and *SOX12* (PMID:39057025) are three closely-related SoxC disorders that are easily conflated. Also note **MRD27 ≠ MRD-any-other-number**. Curators should double-check that any deep-research report is about *SOX11*, not *SOX4*, and not a different CSS number (e.g. *ARID1B*=CSS1, *SMARCB1*=CSS3, *ARID1A*=CSS2).

**Discrepancies found — flag for curator resolution:**

| # | Issue | Detail |
|---|---|---|
| **D1** | HPO ID typo in the primary source | Al-Jawahiri 2022 [FULL-TEXT p.1263] writes "abnormal eye morphology [HP **0013272**]". The correct HPO ID for *Abnormal eye morphology* is **HP:0012372**. Do not propagate HP:0013272. |
| **D2** | p.Lys50Asn cDNA nomenclature conflict | Hempel 2016 reports **c.150G>C** p.Lys50Asn; Wang 2023 (PMID:36369738) reports **c.148A>C** p.Lys50Asn. Both changes yield Lys50Asn at the same codon; these are genuinely different nucleotide substitutions in independent probands, not an error. Curate both. |
| **D3** | Protein nomenclature typo in a source abstract | PMID:35938035 abstract states "one nonsense variant of c.820A>T (p. **K142***)". c.820A>T corresponds to codon 274 (**p.Lys274***), which is what the paper's own variant table reports. The abstract contains a typo. **If you quote this abstract as a snippet, quote it as printed** (validation is a substring match), but curate the variant as p.Lys274*. |
| **D4** | gnomAD constraint | See [§4.6](#46-population-constraint-and-allele-frequency) — a web snippet claiming gnomAD v4 pLI 0.09 / LOEUF 1.15 **could not be verified** and conflicts with the published gnomAD v2.1.1 values. Use the published values; do not cite the unverified v4 numbers. |

---

## 2. Etiology

### 2.1 Disease causal factors

**Monogenic, genetic, and essentially exclusively so.** The disorder is caused by heterozygous loss-of-function of *SOX11* through two mechanisms:

1. **Intragenic single-nucleotide variants (SNVs)** — predominantly missense variants clustered in or adjacent to the HMG DNA-binding domain, plus protein-truncating variants (PTVs). SNVs account for ~89% of reported cases (34/38 in the largest cohort).
2. **Whole-gene / contiguous deletions of 2p25.2** encompassing *SOX11* — ~11% (4/38 in Al-Jawahiri; 7 deletion cases in Hempel 2016; the index observation was a de novo 1.1 Mb deletion, PMID:18992374).

The unifying mechanism is **haploinsufficiency** — reduced *SOX11* transcriptional dosage during embryonic and early postnatal development. This is supported at four independent levels:

> **[VERBATIM — PMID:31035284, Turan et al., *Hum Mol Genet* 2019, DOI 10.1093/hmg/ddz089]**
> "Surprisingly, heterozygous missense mutations or deletions of *SOX11* were recently detected in patients with Coffin-Siris syndrome-like syndrome (CSSLS), a neurodevelopmental disorder associated with intellectual disability, demonstrating that in humans *SOX11* haploinsufficiency cannot be compensated and raising the question of the function of *SOX11* in human neurodevelopment."
> "*SOX11* haploinsufficiency impaired the generation of neurons and resulted in a proliferation/differentiation imbalance of neural precursor cells and enhanced neuronal cell death."

> **[VERBATIM — PMID:40832700, Baccas & Liu, *G3* 2025, DOI 10.1093/g3journal/jkaf194]**
> "All the phenotypes observed in *sem-2[Y160C]* animals resemble SEM-2 loss-of-function phenotypes, suggesting that *SOX11[Y116C]* is a loss-of-function, recessive mutation that likely causes defects due to haploinsufficiency."

**ClinGen dosage curation** (evaluated 2024-11-21): haploinsufficiency score **3 — "Sufficient Evidence for Haploinsufficiency"**; triplosensitivity score **0 — "No Evidence for Triplosensitivity"**. Cited evidence: PMID:18992374, 26543203, 24886874, 35341651, 39333428.
**ClinGen gene-disease validity** (Intellectual Disability and Autism GCEP, reported 2025-05-20): **Definitive**, autosomal dominant, for MONDO:0100626.

**Important negative — dominant-negative mechanism is not supported.** The *C. elegans* data above show the disease-associated Y116C behaves recessively (homozygous, not heterozygous, animals are affected), which argues *against* a dominant-negative mode and *for* pure dosage insufficiency. Nuclear localisation of missense mutants is preserved (PMID:35938035), also arguing against a sequestration/dominant-negative model:

> **[FULL-TEXT — PMID:35938035]** "The WT and two missense mutant SOX11 protein localized in the nucleus."

### 2.2 Risk factors

**Genetic risk factors — causal variants (the only established risk factor):**
- De novo heterozygous *SOX11* SNVs (missense >> PTV) and 2p25.2 deletions.
- **Parental germline/somatic mosaicism** is a documented, non-negligible mechanism: "We identified 1 instance of transmission from a mosaic mother. This shows that recurrence could be possible due to mosaicism." [FULL-TEXT, Al-Jawahiri 2022 p.1267]
- **Inherited variants from a mildly affected parent** occur: Al-Jawahiri identified "2 affected sibships (4 participants) [that] had a parent with ID who was presumed to be a *SOX11* variant heterozygote (but was not tested)" [FULL-TEXT p.1263], and Hanker et al. documented confirmed maternal transmission (PMID:33785884).

**Genetic risk factors — susceptibility loci / modifier genes:** **None established.** No GWAS applies (this is a Mendelian disorder). One study reported an association of *SOX11* distal 3′UTR polymorphisms with schizophrenia susceptibility (PMID:32207210), but this is a **separate common-disease association with no established relevance to the Mendelian syndrome** and should not be curated as a modifier of *SOX11* syndrome.

**Potential modifier — second genetic hits.** Al-Jawahiri identified co-occurring variants in three probands (a *BPTF* variant, an *IVD* variant, a *KATB* [likely *KAT6B*] variant, all ACMG class 3) [FULL-TEXT p.1263], and PMID:35938035 found "a 4,300 kb deletion involving the region of 1q24.2-q25.1 … in patient 1, which also contributes to the condition of the patient" [VERBATIM]. **Dual diagnoses do occur and complicate phenotype attribution** — a curation caveat, not a modifier gene.

**Environmental risk factors:** **None identified.** No toxin, occupational, radiation, dietary, maternal-exposure, or lifestyle risk factor has been reported. Advanced paternal age is a general risk factor for de novo mutation across NDDs but has **not been specifically demonstrated for *SOX11***. Sex is not a risk factor for occurrence (see §9). No association with consanguinity (the disorder is dominant).

### 2.3 Protective factors

**None identified — genetic or environmental.** No protective *SOX11* alleles, no modifier alleles reducing severity, no dietary or lifestyle exposure shown to reduce risk or severity. Note the *inverse* of a protective genetic factor: functional redundancy among the SoxC paralogs (*SOX4*, *SOX11*, *SOX12*) was *expected* to buffer *SOX11* loss but demonstrably **does not** in humans (PMID:31035284, quoted above) — a mechanistically informative negative.

### 2.4 Gene–environment interactions

**No gene–environment interaction has been reported for this disorder.** CTD and GxE resources contain no relevant *SOX11* disease-modifier entries. The single mechanistically plausible (but entirely unstudied) GxE axis worth flagging as a **knowledge gap** is *nutritional/catabolic status × growth-hormone deficiency*, since GH deficiency and short stature are established features (PMID:39290158) and nutritional support is a standard CSS intervention.

---

## 3. Phenotypes

### 3.1 Frequency table — primary cohort (Al-Jawahiri 2022, n=38 new patients unless stated)

All numbers in this table are **[FULL-TEXT]** from the CC-BY published PDF, pp.1265–1266, except where a different source is cited.

| Phenotype | Frequency | HPO suggestion | Notes |
|---|---|---|---|
| Developmental delay or intellectual disability | **37/38 (~97%)** — "All but 1 patient was reported to have developmental delay or ID" | HP:0001263 Global developmental delay; HP:0001249 Intellectual disability | Severity ranges profound → low-normal IQ (PMID:38117302); Pasquetti characterises it as "severe ID" |
| Sitting by 12 months attained | 80% | — | Kaplan–Meier milestone analysis |
| Independent walking by 30 months attained | 70% | — | |
| Speech begun by 40 months | 80% | — | |
| **Never attains speech** | **~20%** — "Kaplan-Meier analysis suggesting that 20% of the patients may not attain speech" | HP:0001344 Absent speech | Speech is "particularly affected" |
| Microcephaly | "common"; **11/28 (39%)** in the 58-case literature synthesis (PMID:35938035) | HP:0000252 Microcephaly | Pasquetti: "high incidence of microcephaly" |
| Short stature | "common"; **10/30 (33%)** (PMID:35938035) | HP:0004322 Short stature | |
| Low body weight | "common" | HP:0004325 Decreased body weight | |
| Intrauterine growth restriction | 2/2 in OMIM clinical synopsis | HP:0001511 Intrauterine growth retardation | |
| **Hypogonadotropic hypogonadism** (endocrine-confirmed) | **8/38 (21%)** | HP:0000044 Hypogonadotropic hypogonadism | "Investigations were prompted by delayed puberty, cryptorchidism, or genital malformations" |
| Delayed puberty | principal manifestation in both sexes | HP:0000823 Delayed puberty | |
| Cryptorchidism | 5/6 males in literature synthesis (PMID:35938035) | HP:0000028 Cryptorchidism | |
| Micropenis / decreased testicular volume | 3/5 males + 1 (PMID:39333428) | HP:0000054 Micropenis | |
| Primary amenorrhoea / uterine hypoplasia / non-visualised ovaries | 2 females (PMID:39333428) | HP:0000786 Primary amenorrhea; HP:0000013 Hypoplasia of the uterus | |
| **Brain MRI abnormal** | **12/20 imaged (60%)**; MRI performed in only 20 (42%) | HP:0012443 Abnormality of brain morphology | "the true prevalence is likely to be higher given that children with ID are often not imaged" |
| Cerebellar malformation / hypoplasia | 4 patients | HP:0001321 Cerebellar hypoplasia | "The most striking findings were those of cerebellar hypoplasia" |
| Agenesis of the corpus callosum | 4 patients | HP:0001274 Agenesis of corpus callosum | |
| Arhinencephaly | 1 patient | HP:0002139 Arrhinencephaly | |
| Small pituitary gland | 2 patients | HP:0010627 Anterior pituitary hypoplasia | Also PMID:42168980: pituitary height 3.4 mm |
| Rathke's cleft cyst | 1 patient | HP:0011764 Rathke cleft cyst *(verify)* | |
| Anosmia with olfactory nerve hypoplasia | 1 patient | HP:0000458 Anosmia; HP:0040326 Hypoplasia of the olfactory bulb | Kallmann-syndrome overlap |
| **Ocular involvement — overall** | "infrequent" in this cohort; **26/58 (44.83%)** in the pooled ophthalmological review (PMID:40933692) | HP:0012372 Abnormal eye morphology | **Note D1** — do not use HP:0013272 |
| Oculomotor apraxia (Cogan type) | **4 patients**; 15/58 (29.31%) as "ocular motor disorder" (PMID:40933692) | HP:0000657 Oculomotor apraxia | "Diagnosis of oculomotor apraxia requires specialized neuro-ophthalmological evaluation, and therefore, the true prevalence of this feature is likely to be higher" |
| Coloboma | 2 patients; "ocular deformities" 5/58 (8.62%) | HP:0000589 Coloboma | |
| Microphthalmia | 1 patient | HP:0000568 Microphthalmia | |
| High myopia / fundus tessellation / cone-rod dystrophy | 1/58 (1.72%) — single proband (PMID:40933692) | HP:0011003 High myopia; HP:0000548 Cone/cone-rod dystrophy | Novel, single report |
| **Renal anomalies** | **3 patients (~8%)** — "the only common internal organ malformation" | HP:0000077 Abnormality of the kidney | Concordant with mouse CAKUT (§4/§15) |
| Epilepsy | **2 patients (~5%)** | HP:0001250 Seizure | Notably **low** for an NDD of this severity |
| Ataxia | **absent** — "there was no clearly defined ataxia in association with the cerebellar findings on imaging" | — | **Important negative** despite cerebellar hypoplasia |
| Facial dysmorphism | "a consistent facial dysmorphology across multiple ethnic groups" | see §3.2 | |
| **Coarse facies** | **Rare/absent** — the discriminating negative vs *ARID1B* CSS | HP:0000280 Coarse facial features | Phenotype clustering: "*ARID1B* CSS was distinguished by coarse facial features and the absence of the HPO terms prevalent in *SOX11* syndrome" |
| Fifth-digit nail hypoplasia | "about … one-tenth had nail dysplasia" (PMID:35938035 synthesis) | HP:0008398 Hypoplastic fifth fingernail; HP:0011937 Hypoplastic fifth toenail | Present in **all** members of the maternally-transmitted family (PMID:33785884) |
| Fifth-finger clinodactyly | 5/7 (PMID:39333428); 6/7 deletion cases (PMID:26543203) | HP:0004209 Clinodactyly of the 5th finger | |
| Hypotonia | 4/7 (PMID:39333428) | HP:0001252 Hypotonia | |
| Hypertrichosis | 2/2 (OMIM synopsis) | HP:0000998 Hypertrichosis | |

### 3.2 Facial gestalt (HPO suggestions, from the OMIM/MedGen clinical synopsis + reports)

Short palpebral fissures (HP:0012745), depressed nasal bridge (HP:0005280), midface retrusion (HP:0011800), long nose (HP:0003189), anteverted nares (HP:0000463), short philtrum (HP:0000322), high palate (HP:0000218), thick vermilion border (HP:0012471), everted lower lip vermilion (HP:0000232), full cheeks (HP:0000293), long eyelashes (HP:0000527), low-set ears (HP:0000369), posteriorly rotated ears (HP:0000358), prominent forehead (HP:0011220), arched eyebrow (HP:0002553), broad nasal tip (HP:0000455), wide mouth (HP:0000154).

**Curation caution (from the source itself):** "The facial dysmorphic features seem not to be specific" [VERBATIM, PMID:33785884]. Do not over-weight facial features.

### 3.3 Behavioural phenotype (quantitatively characterised — n=21)

> **[VERBATIM — PMID:37924570, Al-Jawahiri et al., *Res Dev Disabil* 2023, DOI 10.1016/j.ridd.2023.104623]**
> "Most participants demonstrated borderline (33%) or mild (39%) adaptive behavior impairment, with greater communication and daily-living difficulties than social challenges. Ninety percent exhibited clinically significant autistic traits, with 62% in the 'severe' range, though social motivation emerged as a relative strength. This represents the first standardized evaluation of adaptive behavior and autistic characteristics in *SOX11* syndrome populations."

| Behavioural phenotype | Frequency | HPO |
|---|---|---|
| Clinically relevant autistic traits | **90%** (62% severe range) | HP:0000729 Autistic behavior |
| Borderline adaptive-behaviour impairment | 33% | HP:0002355 *(no direct term; use HP:0001249 + description)* |
| Mild adaptive-behaviour impairment | 39% | — |
| Autism and/or ADHD diagnosis | 5/7 (PMID:39333428) | HP:0000729; HP:0007018 Attention deficit hyperactivity disorder |
| **Preserved social motivation** | relative strength | — | **Important positive-differentiating negative** |

The pattern — communication and daily-living deficits exceeding social deficits, with intact social motivation — is a genuinely distinguishing behavioural signature and is worth curating explicitly, because it separates *SOX11* syndrome from idiopathic ASD.

### 3.4 Phenotype characteristics: onset, severity, progression

- **Onset:** congenital / prenatal (IUGR, structural malformations) and infantile (developmental delay). Endocrine features declare themselves in **adolescence** (delayed puberty). HPO onset: HP:0003577 Congenital onset / HP:0003593 Infantile onset.
- **Severity:** highly variable — "Cognitive outcomes range from profound intellectual disability (ID) to low normal IQ, with most individuals having moderate ID" [VERBATIM, PMID:38117302]. Note that PMID:38117302 is a mixed BAFopathy adult cohort including *SOX11*.
- **Progression:** the neurodevelopmental core is **static/non-progressive** (developmental, not degenerative). Skeletal (scoliosis), ophthalmological (myopia), endocrine (pubertal failure), and metabolic (obesity) features are **progressive/emergent with age**.
- **Frequency among affected individuals:** see §3.1.

### 3.5 Quality-of-life impact (per phenotype)

**No disease-specific QoL instrument (EQ-5D, SF-36, PROMIS) has been administered in a *SOX11* cohort.** This is an explicit gap. Functionally-inferred impact:

| Phenotype | QoL / functional impact | Source |
|---|---|---|
| Absent/limited speech (~20% non-verbal) | Highest-impact single feature; drives communication and daily-living deficits in the Vineland-type profile; "childhood speech interventions are necessary" | PMID:37924570; PMID:35126043 |
| Intellectual disability (mostly moderate) | Lifelong dependency; most adults require support | PMID:38117302 |
| Autistic traits (90%) | Behavioural and educational burden; mitigated by preserved social motivation | PMID:37924570 |
| Hypogonadotropic hypogonadism | Pubertal failure, infertility, bone-health and psychosocial consequences; **treatable** | PMID:35341651; 39290158; 42168980 |
| Cochlear nerve deficiency SNHL | Unilateral hearing loss; **critically, limits cochlear-implant benefit** | PMID:35642566 |
| Oculomotor apraxia | Reading/scanning difficulty compounding ID; often undiagnosed | PMID:33785884; 35341651 |
| Feeding difficulty | May require gastrostomy | PMID:23556151 (CSS GeneReviews) |
| Adult overweight/obesity, scoliosis, visual impairment | "overweight and obesity are frequent in adults with CSS. Visual impairment, scoliosis, and behavioral anomalies are more prevalent than in published pediatric or mixed cohorts" [VERBATIM] | PMID:38117302 |

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

**SOX11** — SRY-box transcription factor 11.

| Attribute | Value |
|---|---|
| Locus | 2p25.2 |
| GRCh38 coordinates | NC_000002.12: 5,692,384–5,701,385 |
| **Exon count** | **1 (intronless)** |
| Transcripts | **single transcript** — NM_003108.4 |
| Protein | 441 amino acids (NP_003099.1 / UniProt P35716) |
| HMG DNA-binding domain | aa **48–119** |
| Transactivation domain (TAD) | aa **408–441** |

> **[VERBATIM — NCBI Gene 6664 RefSeq summary]** "This intronless gene encodes a member of the SOX (SRY-related HMG-box) family of transcription factors involved in the regulation of embryonic development and in the determination of the cell fate."

> **[FULL-TEXT — Al-Jawahiri 2022 p.1262]** "*SOX11* is a single exon gene with a single transcript, which is predicted to be haploinsufficient and loss-of-function intolerant."

**Curation consequence of intronlessness:** there are **no canonical splice-site variants** in *SOX11*. Any deep-research report asserting a *SOX11* splice variant is a red flag. A single exon also means intragenic deletions are rare and whole-gene deletions predominate among CNVs.

### 4.2 Pathogenic variant spectrum

**Cohort composition (Al-Jawahiri 2022, [FULL-TEXT p.1263]):**
- 38 new patients: **34 SNVs + 4 deletions**
- 29 distinct SNVs: **25 unique missense + 4 protein-truncating variants (PTVs)**
- One sibling pair shared a PTV; one sibling pair shared a missense variant
- **All 4 PTVs classified pathogenic**; of the missense variants, **5 likely pathogenic and 20 pathogenic**
- **De novo confirmed in 30 patients**; 1 inherited from a mosaic parent; 2 sibships (4 participants) with a presumed-heterozygous affected parent
- Plus **15 previously published patients** with *SOX11* SNVs

**Cumulative published tally:** ~**82 individuals** with *SOX11* variants reported in the literature as of the Pasquetti 2024 review [VERBATIM: "32 out of 82 subjects reported in the literature with *SOX11* variants"]; **56 distinct variants** catalogued by Wu et al. 2024 [VERBATIM: "Analysis of 56 *SOX11* variants…"]; **30 unique variants** in the HH-focused review [VERBATIM, PMID:42168980: "Thirty unique variants were identified, 17/30 clustering within the HMG domain and 15/18 proven de-novo"].

### 4.3 Variant catalogue (published, protein-level, with source)

**Within/flanking the HMG box (aa 48–119) — the mutational hotspot.** From Al-Jawahiri 2022 Figure 1, aggregating published + novel:

`His48Asp` · `Ile49Asn` · `Lys50Asn` (recurrent, ≥3×) · `Lys50Gln` · `Gly47Ser` (recurrent, ≥3×) · `Arg51Leu` · `Arg51Gln` · `Arg51Gly` · `Arg51Trp` · `Arg51Pro` · `Pro52Ser` · `Pro52Leu` · `Met53Arg` · `Met53Ile` · `Met53Val` · `Ala55Thr` (recurrent) · `Phe56Leu` · `Met57Thr` · `Trp59*` · `Ser60Pro` · `Arg64Leu` · `Arg64Cys` · `Arg64Pro` · `His75Asp` · `Ser80Phe` · `Ile79Val` · `Gly84Ser` · `Gly84Val` · `Ala86AlafsTer139` · `Arg86TerfsTer13` · `Trp87Arg` (recurrent) · `Phe98Leu` · `Ala102Val` · `Arg106Pro` · `His109Asn` · `His109Pro` · `His109Tyr` · `Tyr113His` · `Tyr116Cys` (recurrent) · `Tyr116del` · `Pro120His`

**Outside the HMG box:** `Cys29*` · `Ala142Gly` · `Ala174ArgfsTer32` · `Ala176Glu` · `Asp223MetfsTer45` · `Asn271SerfsTer10` · `Lys274*` · `Tyr294*` · `Glu324*` · `Ser338Leu` · `Gly384ArgfsTer14`

**cDNA-level variants with confirmed source attribution:**

| cDNA (NM_003108.4) | Protein | Type | Source (PMID) | Notes |
|---|---|---|---|---|
| c.87C>A | p.Cys29* | nonsense | 26543203 | de novo |
| c.139G>A | p.(Gly47Ser) | missense | 33785884 | **maternally transmitted**, 3 affected |
| c.148A>C | p.Lys50Asn | missense | 36369738 | de novo; SNHL + inner-ear malformation |
| c.150G>C | p.Lys50Asn | missense | 26543203 | de novo (see D2) |
| c.152G>C | p.Arg51Pro | missense | 42015706 | de novo; **Berry syndrome + TGA** |
| c.337T>C | p.Tyr113His | missense | 35938035 | de novo; ↓GDF5 transactivation |
| c.346_348del | p.Tyr116del | in-frame del | 42168980 | de novo; **Kallmann phenotype** |
| c.347A>G | p.Tyr116Cys | missense | 38591849 | de novo; **microtia**; modelled in *C. elegans* (40832700) |
| c.359C>A | p.Pro120His | missense | 26543203 | de novo |
| c.425C>G | p.Ala142Gly | missense | 35938035 | de novo; ↓GDF5 transactivation |
| c.527C>A | p.Ala176Glu | missense | 35341651 | de novo; **non-HMG**, functionally validated; **neonatal death** |
| c.667del | p.Asp223MetfsTer45 | frameshift | 37558216 | **Pitt-Hopkins-like phenotype** |
| c.700G>T | *(not stated)* | nonsense | 39501269 | short stature, spina bifida, VSD |
| c.811_814del | p.Asn271SerfsTer10 | frameshift | 36369738 | de novo; SNHL |
| c.820A>T | p.Lys274* | nonsense | 35938035 | see D3 |
| c.882C>G | p.Tyr294* | nonsense | 35341651 | functionally validated, abolishes transactivation |
| c.1013C>T | p.Ser338Leu | missense | 40933692 | de novo; **high myopia + cone-rod dystrophy** |
| c.1142_1143insT | p.Gly384ArgfsTer14 | frameshift | 35341651 | functionally validated, abolishes transactivation |

### 4.4 Variant classification (ACMG/AMP)

Al-Jawahiri classified all 29 SNVs using ACMG/AMP criteria via VarSome: **all 4 PTVs pathogenic; 20 missense pathogenic; 5 missense likely pathogenic.** Two novel lines of evidence supported missense classification:

1. **Paralogue-based evidence (PP-level).** "There is significant sequence homology between the HMG box domains of human SOX proteins. We reasoned that if pathogenic variants had been reported at a given residue in a SOX protein, then it could be taken as possible evidence of pathogenicity for the equivalent variant in *SOX11*. … In total, 6 residues in *SOX11* had pathogenic variants (DECIPHER and ClinVar) at equivalent residues in *SOX10*. Several of these had identical amino acid change, eg, p.(Arg51Gly) in *SOX11* and p.(Arg106Gly) in *SOX10*." [FULL-TEXT p.1264]
2. **Domain-level constraint (PM1-level).** "we identified that the percentage of residues with a missense SNV in the HMG box was significantly lower than in the N-terminal, central, or transactivating domains." [FULL-TEXT p.1264]

**Curator caution from the source itself:** "It should not be assumed that all HMG box missense variants are pathogenic." [FULL-TEXT p.1263–64]

**ClinVar (as of retrieval):** the ClinVar search interface did not render usable counts via WebFetch. **Curators must obtain the ClinVar breakdown directly** (`SOX11[gene]`) rather than relying on this report. Example pathogenic variants are catalogued in §4.3 above with primary-literature attribution.

### 4.5 Variant type / class distribution

| Class | Share | Mechanism |
|---|---|---|
| **Missense** (HMG-box clustered) | ~86% of SNVs (25/29 distinct) | Impaired DNA binding → reduced transactivation; nuclear localisation preserved |
| **Nonsense / frameshift (PTV)** | ~14% of SNVs (4/29) | Loss of C-terminal transactivation domain |
| **Whole-gene / 2p25.2 deletion** | ~11% of all cases | Gene dosage loss; may be part of a contiguous-gene deletion |
| **In-frame deletion** | rare (p.Tyr116del) | Presumed LoF |
| **Splice-site** | **N/A — gene is intronless** | — |

### 4.6 Population constraint and allele frequency

> **[FULL-TEXT — Al-Jawahiri 2022 p.1264]** "none of the *SOX11* missense variants were present in Genome Aggregation Database (gnomAD), and only 8 HMG missense variants in *SOX11* were identified in 114,704 individuals in gnomAD v2.1.1 non-neuro data set. This strongly suggests that missense variants in this domain are not compatible with normal neurodevelopment."
> "Only 2 PTVs are present in gnomAD (v2.1.1 non-neuro data set), and *SOX11* is predicted to be loss-of-function intolerant with probability of loss of function intolerance = 0.86 (observed/expected 0.09 [0.03-0.44])."

So: **gnomAD v2.1.1 → pLI = 0.86, o/e LoF = 0.09, LOEUF (upper CI) = 0.44.**

⚠️ **Discrepancy D4.** A web search snippet asserted gnomAD v4 values of pLI 0.09 / LOEUF 1.15 for *SOX11*. I **could not verify this** — the gnomAD browser is JavaScript-rendered and its GraphQL API requires POST, both inaccessible to the fetch tooling available here. The snippet's "0.09" is suspiciously identical to the published *o/e LoF*, suggesting a garbled transcription. **Do not curate the v4 numbers from this report.** Curate the published v2.1.1 values with their PMID, and if gnomAD v4 constraint is wanted, query gnomAD directly.

**Mechanistic caveat worth recording regardless:** *SOX11* is a **441-aa single-exon** gene, so its *expected* pLoF count is very small and LoF-constraint metrics are intrinsically low-powered for it. The authoritative dosage statement is therefore **ClinGen haploinsufficiency score 3**, not any LOEUF value.

**Allele frequency of pathogenic variants:** effectively zero. All are absent from gnomAD, 1000 Genomes, ExAC, and TOPMed. This supports PM2 for every reported variant.

### 4.7 Somatic vs germline origin

- **Germline** for the neurodevelopmental disorder — overwhelmingly **de novo** (30/38 confirmed).
- **Parental mosaicism** documented once (mosaic mother, Al-Jawahiri 2022).
- **Somatic *SOX11* aberration is a completely separate biology and must not be conflated with the NDD.** *SOX11* is not somatically *mutated* as a cancer driver; it is **aberrantly over-expressed**:
  - **Mantle cell lymphoma** — *SOX11* over-expression is an established diagnostic biomarker and oncogene; it distinguishes conventional nodal MCL from indolent leukaemic non-nodal MCL, and drives pathogenesis in part via SOX11–SMARCA4 complex formation.
  - **Adrenergic neuroblastoma** — recurrent **2p focal gains and amplifications** of *SOX11*:
    > **[VERBATIM — PMID:36882421, Decaesteker et al., *Nat Commun* 2023, DOI 10.1038/s41467-023-36735-2]** "Most notably, SOX11 controls chromatin regulatory complexes, including 10 SWI/SNF core components among which SMARCC1, SMARCA4/BRG1 and ARID1A. … Finally, SOX11 is identified as a core transcription factor of the core regulatory circuitry (CRC) in adrenergic high-risk neuroblastoma with a potential role as epigenetic master regulator upstream of the CRC."

  **Note the striking directional inversion this creates:** in the germline NDD, *SOX11* sits *downstream* of the PAX6–BAF complex; in neuroblastoma, *SOX11* sits *upstream* of and *regulates* the SWI/SNF components (*SMARCA4*, *ARID1A*) whose germline loss causes the other Coffin-Siris subtypes. This reciprocal SOX11↔BAF relationship is worth curating as a mechanistic note.

  **Important negative:** **no cancer predisposition has been reported in individuals with germline *SOX11* variants.** Do not import oncological surveillance into the NDD entry. (Contrast *ARID1A*-CSS, which does carry a hepatoblastoma AFP-surveillance recommendation.)

### 4.8 Functional consequences

**Loss of function via two structurally distinct routes**, both experimentally validated by GDF5-promoter luciferase assay:

> **[FULL-TEXT — Al-Jawahiri 2022, Figure 2 legend + p.1265]** "Luciferase assay showing impaired activation of *GDF5* promoter by G384Rfs*14, A176E, and Y294* *SOX11* variants. A176E impairs SOX11 activity but to a much lesser extent than Y294* or G384Rfs*14."
> "In vitro analysis of 2 PTVs showed significant impairment of SOX11 transactivating activity. … The mechanism through which PTV leads to reduction in SOX11 transactivating activity may relate to the loss of C-terminal transactivation domain."

- **HMG-box missense** → impaired DNA binding → reduced target-gene transactivation. Four previously-characterised HMG variants (p.Lys50Asn, p.Pro120His, p.Ser60Pro, p.Tyr116Cys) impair transactivation. Nuclear import is **preserved** (PMID:35938035) — so the defect is at the DNA-binding/transactivation step, not trafficking.
- **PTV** → loss of the C-terminal TAD (aa 408–441) → near-complete loss of transactivation.
- **Non-HMG missense** can also be pathogenic but with a milder biochemical deficit: p.Ala176Glu "significantly reduced SOX11 transactivating activity … but to a much lesser extent." Notably this milder-in-vitro variant occurred in the **most severely affected** patient (case 11: neonatal death, cerebellar hypoplasia, microcephaly) — **in-vitro residual activity does not predict clinical severity.** Curate this as an explicit knowledge gap.
- **Not dominant-negative** — see §2.1.

**Reporter/target genes used in functional assays:** *GDF5* (promoter −448/+319, NM_000557.3, GRCh37/hg19), the standard *SOX11* reporter across three independent labs (PMID:26543203, 35341651, 35938035). Additional validated direct targets: *FGF9* (palate/mandible; PMID:26826126), the protocadherin B cluster locus control region (kidney; PMID:29459093), the *GNRH1* intron-A enhancer (PMID:21527504), *hlh-8*/Twist ortholog (*C. elegans*; PMID:40832700).

### 4.9 Modifier genes

**None established.** See §2.2 for the distinct issue of co-occurring second diagnoses.

### 4.10 Epigenetic information — the *SOX11* episignature

This is one of the most curation-relevant features of the disorder and functions as a **clinical diagnostic biomarker**.

> **[FULL-TEXT — Al-Jawahiri 2022 pp.1263, 1265]**
> "A total of 224 differentially methylated probes (DMPs) were identified and considered as the *SOX11* episignature."
> "An overall hypomethylation pattern was observed for most probes when comparing 10 *SOX11* cases … and control samples."
> "BAFopathy complex samples were applied to the *SOX11* episignature classifier, but none of them were grouped with *SOX11* samples."
> "Many of these DMPs have regulatory roles in neural differentiation and are associated with NDDs (ie, family with sequence similarity 160 member B1 [*FAM160B1*] and *FMN2*). Some DMPs have regulatory role in the epigenetic machinery, such as *DPF2* and *AHCTF1*."

**Methodology (for the dismech `datasets`/diagnostics sections):** Illumina Infinium MethylationEPIC BeadChip on peripheral blood DNA; 10 *SOX11* cases vs **50 age/sex/array-matched controls (5:1)** drawn from the EpiSign Knowledge Database; β→M-value transformation; limma linear modelling; two binary SVM classifiers with linear kernel (e1071) generating a **methylation variant pathogenicity (MVP) score** 0–1; Platt scaling; 10-fold cross-validation on MDS.

**Cross-reactivity to flag:** in the first (less specific) classifier, "Some samples from other disorders that are in EKD that are part of the EpiSign V2 clinical assay, including autosomal dominant cerebellar ataxia, deafness, and narcolepsy, HVDAS_T, and Sotos syndrome, plus 1 sample from control (testing), Kabuki syndrome, and mental retardation, autosomal dominant type 51 cohorts showed an elevated MVP score." Training against 38 additional NDD/congenital-anomaly episignatures resolved this: "A high MVP score was seen in 10 *SOX11* samples with much improved specificity relative to other EpiSign conditions."

### 4.11 Chromosomal abnormalities

- **2p25.2 microdeletions** encompassing *SOX11* — the founding observation was a de novo ~1.1 Mb deletion in a girl with ID, autism, and microcephaly (PMID:18992374, "Deletion 2p25.2: a cryptic chromosome abnormality in a patient with autism and mental retardation detected using aCGH"). Hempel 2016 identified 7 such individuals; Al-Jawahiri added 4. A segmental deletion encompassing *SOX11* also produced "microphthalmia and related ocular phenotypes" (PMID:25010521).
- **Detection:** requires chromosomal microarray or CNV calling from exome/genome data. Because *SOX11* is a **single-exon** gene, exome CNV callers with poor single-exon sensitivity may miss intragenic events — a real diagnostic pitfall to record.
- **No translocations, inversions, or aneuploidies** are associated with the germline disorder. (Contrast MCL's t(11;14) — a somatic event, unrelated.)

---

## 5. Environmental Information

**Environmental factors: none identified.** No toxin, pollutant, radiation, or occupational exposure has been implicated in causation or modification. CTD contains no *SOX11* disease-modifier chemical interactions relevant to this disorder.

**Lifestyle factors: none causal.** Two lifestyle-adjacent items are relevant *downstream*, not upstream:
1. **Adult overweight/obesity is frequent** in molecularly-confirmed CSS adults including *SOX11* carriers (PMID:38117302) — a management target, not an aetiological factor.
2. **Nutritional/feeding support** is a core intervention (PMID:23556151).

**Infectious agents: not applicable.** This is a Mendelian disorder with no infectious trigger. One tangential retrieval — PMID:41567998, "Neurogenesis decreases in the offspring of mothers infected with influenza A virus" (*Front Cell Infect Microbiol* 2026) — appeared in the *SOX11* literature search because it examines Sox11-dependent neurogenesis pathways in a maternal-immune-activation model. **This is not evidence of an infectious contribution to human *SOX11* syndrome** and should not be curated as such.

**Curation guidance:** the `environmental_factors` and `infectious_agents` sections of the dismech entry should be **explicitly empty with a note**, not silently omitted — the absence is informative for a purely genetic disorder.

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (upstream → downstream)

```
[TRIGGER — MOLECULAR]
Heterozygous SOX11 loss-of-function
  (HMG-box missense → impaired DNA binding;  PTV → loss of C-terminal TAD;
   whole-gene deletion → dosage loss)
        │
        ▼
[MOLECULAR]  Reduced SOX11 transcriptional dosage
             → hypoactivation of SOX11 target genes
               (GDF5, FGF9, PCDHB-cluster LCR, GNRH1 intron-A enhancer, hlh-8/Twist)
             → NOT compensated by paralogues SOX4/SOX12 (PMID:31035284)
        │
        ├──────────────────┬──────────────────┬────────────────┬──────────────┐
        ▼                  ▼                  ▼                ▼              ▼
[CELLULAR]           [CELLULAR]         [CELLULAR]      [CELLULAR]      [CELLULAR]
Neural precursor     Sensory neuron     Mandibular      Nephrogenic-    Hedgehog
proliferation/       survival ↓ and     mesenchyme      cord Gdnf       signalling
differentiation      axonal growth ↓    proliferation ↓ domain          DYSREGULATION
imbalance;           (inner ear)        via Cyclin D1   extended        (↑shha)
neuronal cell        │                  → FGF9 ↓        rostrally       │
death ↑              │                  │               │               │
        │            │                  │               │               │
        ▼            ▼                  ▼               ▼               ▼
[TISSUE]        [TISSUE]           [TISSUE]         [TISSUE]        [TISSUE]
Reduced cerebral Cochlear nerve    Mandibular       Duplex kidney,  Failure of
+ cerebellar     aplasia/          hypoplasia →     malpositioned   choroid fissure
growth; corpus   hypoplasia        tongue mal-      kidney,         closure; lens
callosum         (structurally     position →       hydroureter;    dysgenesis;
agenesis         normal cochlea)   physical block   short Henle's   rod photo-
        │            │             of palatal       loop            receptor loss
        │            │             shelf elevation      │               │
        ▼            ▼                  ▼               ▼               ▼
[ORGANISM]      [ORGANISM]        [ORGANISM]       [ORGANISM]      [ORGANISM]
Microcephaly,   Unilateral        Cleft secondary  Renal anomalies Coloboma,
DD/ID, absent   sensorineural     palate           (~8%)           microphthalmia,
speech (~20%),  hearing loss      (Pierre Robin-                   high myopia
autistic traits (CI benefit                like)
                 limited)

        └─── PARALLEL ENDOCRINE ARM ───────────────────────────────┐
                                                                   ▼
[CELLULAR]  SOX4/SOX11 fail to activate the GNRH1 intron-A enhancer in
            hypothalamic GnRH neurons;  SOX11 depleted in pituitary gonadotropes;
            ± failed GnRH-neuron migration from olfactory neuroepithelium
                                                                   │
                                                                   ▼
[TISSUE]    Olfactory bulb/nerve hypoplasia;  pituitary hypoplasia;
            small/absent adenohypophysis
                                                                   │
                                                                   ▼
[ORGANISM]  Hypogonadotropic hypogonadism (21%) ± anosmia (Kallmann phenotype);
            delayed puberty; GH deficiency; hypothyroidism
```

### 6.2 Molecular pathways

| Pathway | Role | Evidence |
|---|---|---|
| **SoxC (SOX4/SOX11/SOX12) transcriptional program** | The core axis. SOX11 is the non-redundant member for human neurodevelopment. | PMID:31035284, 29079881 |
| **PAX6 → BAF (SWI/SNF) → SOX11** | *SOX11* is a downstream transcriptional target of the PAX6–BAF complex, explaining the original CSS assignment. | PMID:24886874 [VERBATIM]: "*SOX11* is a downstream transcriptional factor of the PAX6-BAF complex, underscoring the BAF complex and *SOX11* transcriptional network's significance in brain development." |
| **SOX11 → SWI/SNF (reverse direction)** | In neuroblastoma SOX11 *regulates* 10 SWI/SNF core components. Bidirectional relationship. | PMID:36882421 |
| **Sonic Hedgehog (SHH)** | SOX11 restrains *shha* transcription; loss → **elevated** Hh signalling → coloboma. Rescued by cyclopamine. | PMID:25010521 |
| **FGF9 signalling** | Direct SOX11 target driving mandibular/palatal-shelf proliferation. | PMID:26826126 |
| **BMP/GDF — GDF5** | Canonical SOX11 reporter target; skeletal/joint morphogenesis. | PMID:26543203, 35341651, 35938035 |
| **GDNF–RET (nephrogenesis)** | *Sox11* loss extends the *Gdnf* expression domain rostrally → duplex kidney. | PMID:29459093 |
| **Protocadherin B cluster (cell adhesion)** | SOX11 "directly binds and regulates a locus control region of the protocadherin B cluster." | PMID:29459093 [VERBATIM] |
| **GnRH transcriptional control** | SOX4/SOX11 activate the *GNRH1* intron-A enhancer. | PMID:21527504 |
| **PKA → SOX11 S133 phosphorylation** | PKA phosphorylates SOX11 at S133, tuning dendritic development of adult-born dentate granule neurons. | PMID:30385877 |
| **USP11 deubiquitination → SOX11 protein stabilisation** | Post-translational control of SOX11 abundance; a *second*, non-transcriptional route to functional SOX11 insufficiency. | PMID:33579706 |
| **PRC2/EED → SOX11 repression** | Polycomb EED targets *SOX11* in hippocampal dentate gyrus neuronal differentiation. | PMID:31204298 |
| **Cyclin D1 / cell cycle** | Mediates the proliferative arm in mandibular mesenchyme. | PMID:26826126 |

### 6.3 Cellular processes

| Process | GO suggestion | Direction |
|---|---|---|
| Neural precursor cell proliferation | GO:0061351 neural stem cell proliferation *(verify)* | DECREASED / dysregulated |
| Neuron differentiation | GO:0030182 neuron differentiation | DECREASED |
| Neurogenesis | GO:0022008 neurogenesis | DECREASED |
| Neuron apoptotic process | GO:0051402 neuron apoptotic process | INCREASED |
| Neuron migration | GO:0001764 neuron migration | IMPAIRED |
| Brain development | GO:0007420 brain development | ABNORMAL |
| Cerebellum development | GO:0021549 cerebellum development | ABNORMAL |
| Positive regulation of transcription by RNA polymerase II | GO:0045944 | DECREASED |
| DNA-binding transcription factor activity | GO:0003700 | DECREASED (molecular function) |
| Smoothened signaling pathway | GO:0007224 | INCREASED (Hh dysregulation) |
| Palate development | GO:0060021 palate development | ABNORMAL |
| Kidney development / metanephros development | GO:0001822 / GO:0001656 | ABNORMAL |
| Inner ear development | GO:0048839 inner ear development | ABNORMAL |
| Protein stabilization (USP11 axis) | GO:0050821 protein stabilization | context |
| Protein phosphorylation (PKA, S133/S30) | GO:0006468 protein phosphorylation | regulatory |
| Cell population proliferation (mandibular mesenchyme) | GO:0008283 | DECREASED |
| Outflow tract morphogenesis | GO:0003151 outflow tract morphogenesis | ABNORMAL (mouse) |

**All GO IDs above are suggestions requiring OAK verification** (`uv run runoak -i sqlite:obo:go info GO:XXXXXXX -O obo`).

### 6.4 Protein dysfunction

SOX11 (441 aa, UniProt P35716) is a nuclear transcriptional activator with an HMG DNA-binding domain (aa 48–119) and a C-terminal TAD (aa 408–441).

> **[FULL-TEXT — Al-Jawahiri 2022 p.1263]** "The HMG box in SOX11 protein is a domain responsible for SOX11 binding to DNA and regulation of target genes. In addition, the HMG box regulates key protein–protein interactions and trafficking of SOX11 protein between cytoplasm and nucleus."

Dysfunction modes: (i) **reduced DNA-binding affinity** (HMG missense); (ii) **loss of transactivation capacity** (PTV truncating the TAD); (iii) **absent protein** (whole-gene deletion). **No misfolding, aggregation, or gain-of-function mechanism is described.** Nuclear localisation is preserved for missense mutants.

Two additional **regulatory** layers of protein dysfunction, both post-translational:
> **[VERBATIM — PMID:30385877, *Sci Rep* 2018]** "Through Mass Spectrometry (MS), co-immunoprecipitation assays and in vitro phosphorylation assays followed by MS we verified that protein kinase A (PKA) interacts with SOX11 and phosphorylates it on S133. In vivo replacement of SoxC factors in developing adult-generated hippocampal neurons with SOX11 S133 phospho-mutants indicated that phosphorylation on S133 modulates dendrite development of adult-born dentate granule neurons."

> **[VERBATIM — PMID:29973868, *Front Mol Neurosci* 2018]** "Using Mass Spectrometry, we found 10 serine residues in the SOX11 protein that are putatively phosphorylated. Systematic analysis of phospho-mutant SOX11 resulted in the identification of the S30 residue, whose phosphorylation promotes nuclear over cytoplasmic localization of SOX11."

> **[VERBATIM — PMID:33579706, Chiang et al., *Sci Adv* 2021]** "Mechanistically, these functions are mediated by a previously unidentified Usp11 substrate, Sox11. Usp11 ablation compromises Sox11 protein accumulation in the developing cortex, despite the induction of *Sox11* mRNA. The disease-associated Usp11 mutant fails to stabilize Sox11 and is unable to support cortical neurogenesis and neuronal migration."

### 6.5 Metabolic changes

**No primary metabolic defect.** *SOX11* syndrome is not an inborn error of metabolism. Secondary/endocrine-metabolic consequences: GH deficiency, hypothyroidism (PMID:39290158), and adult overweight/obesity (PMID:38117302). No metabolomic or lipidomic study exists.

### 6.6 Immune system involvement

**None.** No autoimmunity, immunodeficiency, or chronic inflammation is described. (SOX11's role in B-cell maturation arrest is a **mantle cell lymphoma** phenomenon — somatic over-expression — and does not manifest as immune dysfunction in germline *SOX11* haploinsufficiency.)

### 6.7 Tissue damage mechanisms

**Developmental hypoplasia/dysmorphogenesis, not tissue destruction.** There is no oxidative stress, ischaemia, fibrosis, or necrosis mechanism. The one true cell-death mechanism is **developmentally-timed apoptosis of neural precursors/neurons** (PMID:31035284) and **reduced sensory-neuron survival** (PMID:35642566), both prenatal/perinatal. Two morphogenetic-obstruction mechanisms are unusual and worth explicit curation:
1. **Cleft palate is secondary, not primary** — mandibular hypoplasia mispositions the tongue, physically obstructing palatal-shelf elevation. The shelves themselves retain fusion competence (PMID:26826126).
2. **Coloboma arises from *excess* Hedgehog signalling** (a gain in a downstream pathway from a loss in the upstream factor) — rescued by the Hh *inhibitor* cyclopamine (PMID:25010521).

### 6.8 Epigenetic changes

Two distinct epigenetic dimensions:
1. **The disease episignature** — 224 DMPs with global hypomethylation in peripheral blood (§4.10). Diagnostic biomarker.
2. **SOX11 as an epigenetic regulator** — SOX11 regulates *DPF2* and *AHCTF1* (epigenetic machinery) among the DMP genes, and in neuroblastoma controls 10 SWI/SNF core components, HDAC2, CBX2 (PRC1), and KDM1A/LSD1. Al-Jawahiri's interpretation: "aberrations in the expression/methylation status of *SOX11* affects expression/methylation status of genes involved in neural differentiation and/or epigenetic machinery" [FULL-TEXT p.1269].

**Therapeutic implication flagged by the authors:** "The plastic nature of epigenomic profiles may offer an opportunity to study the use of chromatin and epigenomic targeting agents as a potential therapeutic avenue." [FULL-TEXT p.1269] This is hypothesis-only.

### 6.9 Molecular profiling

**Transcriptomics.** *SOX11* developmental brain expression confirmed by RNA-seq and microarray in the BrainSpan atlas; RNAscope ISH used for spatial confirmation (see §7). Downstream target genes identified by "functional genomics" in the mouse conditional-KO study (PMID:23483698). In zebrafish *sox11a* mutants, "the expression levels of genes related to cartilage and bone were downregulated" [VERBATIM, PMID:33061816]. **No patient-tissue transcriptomic study exists.**

**Proteomics.** Mass-spectrometry phospho-mapping of SOX11 (10 putative phospho-serines; S30, S133 functionally characterised) — PMID:30385877, 29973868. SOX11 interactome (SMARCA4) mapped in the MCL context. **No patient-derived proteomic study.**

**Metabolomics / lipidomics.** **None. Genuine gap.**

**Epigenomics.** The 224-DMP EPIC-array episignature (§4.10) — the single strongest omics dataset in this disorder.

**Genomic structural features.** Single-exon, intronless, 2p25.2, ~9 kb genomic span, single transcript. Regulated in *cis* by "multiple adrenergic specific (super-)enhancers" in neuroblastoma (PMID:36882421) — implying an enhancer landscape whose disruption is a plausible but **unreported** non-coding mechanism in the NDD. Worth curating as a knowledge gap: **no non-coding/regulatory *SOX11* variants have been reported in this disorder.**

### 6.10 Advanced technologies

- **Single-cell.** "A single-cell RNA-sequencing study of murine pituitary showed significant enrichment of *SOX11* in gonadotropes" (PMID:33430815-adjacent; ref 33 = Ho Y, Hu P, Peel MT et al., *Protein Cell* 2020;11(8):565–583) — the mechanistic anchor for pituitary-level HH. Counterpoint: "in an induced human pluripotent cell model of GnRH neurons, *SOX11* expression was not enriched" (Lund C et al., *Dis Model Mech* 2020;13(3):dmm040105) — **a genuine human/model discordance** at the hypothalamic level. Also PMID:34184026 (scRNA-seq TCF4-dependent TF network in commissure development — the *SOX11*/TCF4 link relevant to the Pitt-Hopkins mimicry).
- **Spatial transcriptomics.** RNAscope ISH in human fetal tissue (Carnegie stages 20, 21, 23) — see §7. No true spatial-transcriptomics dataset.
- **Multi-omics integration.** PMID:41580083 (*SLAS Technol* 2026, "Integrative single-cell multi-omics network analysis to elucidate epigenetic regulation in neurodevelopmental disorders") includes *SOX11*-relevant network analysis.
- **Functional genomics screens.** *SOX11* is a **dependency gene** in adrenergic neuroblastoma per CRISPR screening (PMID:36882421) — a cancer, not NDD, finding. **No CRISPR/RNAi screen has been run in a *SOX11*-haploinsufficient neurodevelopmental model beyond the isogenic hESC line** (PMID:31035284).
- **Organoids.** PMID:40950130 (bioRxiv 2025) — morphogen-guided neocortical organoids modelling NDD pathology, with regional areal identity; a promising but preprint-stage platform.

### 6.11 MorPhiC relevance

*SOX11* is **not** among the MorPhiC anchor genes (ISL1, EOMES, GCM1, NKX2-1). However, the **SOX11⁺/⁻ isogenic hESC line** (PMID:31035284) is an exact methodological analogue — a CRISPR/Cas9 heterozygous null in human pluripotent cells with cellular-phenotype readouts. If curating `category: Cellular` phenotypes, use that paper with `evidence_source: IN_VITRO`:

| Cellular phenotype | HPO suggestion | Source |
|---|---|---|
| Impaired neuronal generation from neural precursors | HP:0002500 Abnormal cerebral cortex morphology *(imperfect; consider description-only)* | PMID:31035284, IN_VITRO |
| Neural precursor proliferation/differentiation imbalance | — | PMID:31035284, IN_VITRO |
| Enhanced neuronal cell death | — | PMID:31035284, IN_VITRO |

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

**Primary (directly affected):**

| Organ / structure | UBERON suggestion | Manifestation |
|---|---|---|
| Brain (whole) | UBERON:0000955 brain | Microcephaly; 60% of imaged patients have an MRI abnormality |
| Cerebral cortex | UBERON:0000956 cerebral cortex | Strong fetal SOX11 expression; reduced cerebral size in *Sox11*-null mice |
| Cerebellum | UBERON:0002037 cerebellum | Cerebellar hypoplasia (most striking MRI finding, 4 patients) |
| Corpus callosum | UBERON:0002336 corpus callosum | Agenesis (4 patients) |
| Hindbrain | UBERON:0002028 hindbrain | Strong fetal SOX11 expression at all Carnegie stages examined |
| Spinal cord | UBERON:0002240 spinal cord | Fetal SOX11 expression (CS21) |
| Hippocampal dentate gyrus | UBERON:0001885 dentate gyrus of hippocampal formation | Adult-neurogenesis site; SGZ proliferation blunted in conditional KO |
| Pituitary gland (adeno- + neurohypophysis) | UBERON:0000007 pituitary gland; UBERON:0002196 adenohypophysis; UBERON:0002198 neurohypophysis | Small pituitary; SOX11 lines the adenohypophyseal lumen at CS20 |
| Hypothalamus | UBERON:0001898 hypothalamus | GnRH-neuron target; SOX4/SOX11 activate *GNRH1* |
| Olfactory bulb / nerve | UBERON:0002264 olfactory bulb; UBERON:0001579 olfactory nerve | Hypoplasia (1 patient with anosmia); small olfactory bulbs in *Sox11*-null mice |
| Eye — lens, retina, optic nerve | UBERON:0000019 camera-type eye; UBERON:0000965 lens of camera-type eye; UBERON:0000966 retina; UBERON:0000941 optic nerve | Coloboma, microphthalmia, cataract, high myopia, cone-rod dystrophy; SOX11 expressed in lens, optic nerve, neuroretina at CS23 |
| Cochlear nerve | UBERON:0003714 cochlear nerve | Aplasia/hypoplasia → unilateral SNHL, with **structurally normal cochlea** |
| External ear / auricle | UBERON:0001757 pinna | Microtia (1 case); low-set, posteriorly rotated ears |
| Secondary palate | UBERON:0001716 secondary palate | Cleft palate; SOX11 expressed in fetal palate at CS21 |
| Mandible | UBERON:0001684 mandible | Hypoplasia (mouse mechanism upstream of cleft palate) |
| Kidney / ureter | UBERON:0002113 kidney; UBERON:0000056 ureter | Renal malrotation, duplex kidney, malposition, hydroureter |
| Nail (5th digit) | UBERON:0001705 nail | Hypoplastic fifth finger/toe nails |
| Gonads / uterus / testis | UBERON:0000991 gonad; UBERON:0000995 uterus; UBERON:0000473 testis | Uterine hypoplasia, non-visualised ovaries, cryptorchidism, reduced testicular volume |
| Heart — outflow tract, ventricular septum, aorta | UBERON:0004145 cardiac outflow tract; UBERON:0002094 interventricular septum; UBERON:0000947 aorta | Coarctation, VSD, transposition of great arteries / Berry syndrome (rare); OFT malformations are the *mouse* lethal phenotype |
| Vertebral column | UBERON:0000222 vertebral column *(verify)* | Spina bifida (1 case); scoliosis in adults |

**Secondary / complication-level:** thyroid (hypothyroidism), skeletal system (scoliosis, growth restriction), gastrointestinal (feeding difficulty), adipose (adult obesity).

**Body systems involved:** nervous (primary), sensory/special-sense (eye, ear, olfaction), endocrine/reproductive, renal/urinary, craniofacial/skeletal, cardiovascular (uncommon), integumentary (nails, hypertrichosis).

### 7.2 Tissue and cell level

**Cell types (CL suggestions — all require OAK verification):**

| Cell type | CL suggestion | Role |
|---|---|---|
| Neural progenitor cell / neuroblast | CL:0011020 neural progenitor cell *(verify)*; CL:0000031 neuroblast | Proliferation/differentiation imbalance; the primary affected population |
| Neuron | CL:0000540 neuron | Reduced generation; increased death |
| Glutamatergic neuron / cortical excitatory neuron | CL:0000679 glutamatergic neuron | Layer-6 neuron production impaired (Usp11–Sox11 axis) |
| Cerebellar Purkinje cell / granule cell | CL:0000121 Purkinje cell; CL:0000120 granule cell | Cerebellar hypoplasia (cell-type attribution inferred, not directly demonstrated) |
| Dentate gyrus granule cell (adult-born) | CL:0000120 granule cell | Dendrite development modulated by SOX11 S133 phosphorylation |
| GnRH neuron | CL:0008048 *(verify — GnRH neuron)* | *GNRH1* enhancer activation; migration from olfactory neuroepithelium |
| Pituitary gonadotrope | CL:0000173 gonadotroph *(verify label)* | scRNA-seq SOX11 enrichment |
| Sensory neuron (spiral ganglion) | CL:0000101 sensory neuron | Reduced survival, decreased axonal growth → cochlear nerve deficiency |
| Rod photoreceptor cell | CL:0000604 retinal rod cell | Specific reduction in *Sox11*-deficient zebrafish |
| Lens epithelial / fiber cell | CL:0002224 lens epithelial cell *(verify)* | Delayed/abnormal lens formation |
| Neural crest cell | CL:0000333 migratory cranial neural crest cell *(verify)* | Craniofacial derivation (inferred) |
| Mandibular/palatal mesenchymal cell | CL:0000134 mesenchymal cell | Cyclin D1-dependent proliferation deficit |
| Nephron progenitor / metanephric mesenchyme cell | CL:0000324 *(verify)* | Gdnf domain extension |

**Tissue types affected:** nervous tissue (predominant), mesenchyme/connective tissue (craniofacial, skeletal), epithelium (renal tubule, lens, adenohypophysis).

### 7.3 Subcellular level

| Compartment | GO CC suggestion | Relevance |
|---|---|---|
| Nucleus | GO:0005634 nucleus | Primary site of SOX11 action; missense mutants **retain** nuclear localisation |
| Nucleoplasm | GO:0005654 nucleoplasm | NCBI Gene GO annotation |
| Cytoplasm | GO:0005737 cytoplasm | S30-phosphorylation-dependent nucleocytoplasmic partitioning; HMG box regulates trafficking |
| Chromatin | GO:0000785 chromatin | DNA binding; ChIP-validated occupancy at *GNRH1* enhancer, *PCDHB* LCR |

**No mitochondrial, ER, lysosomal, or peroxisomal involvement.**

### 7.4 Localization and lateralization

- Brain malformations are **midline/bilateral** (corpus callosum agenesis, arhinencephaly, cerebellar hypoplasia — bilateral). HPO: HP:0012832 Bilateral.
- **Cochlear nerve deficiency is characteristically UNILATERAL** in both reported probands (PMID:35642566) — a notable asymmetry. HPO: HP:0012833 Unilateral.
- **Microtia was unilateral** (PMID:38591849).
- Ocular coloboma may be uni- or bilateral; the CSS9 high-myopia case was bilateral.
- Renal anomalies: duplex/malpositioned kidney, typically unilateral in the mouse model.
- Olfactory bulb/nerve hypoplasia: **bilateral** (PMID:42168980).

**Curation note:** the combination of bilateral CNS midline defects with unilateral peripheral sensory-nerve and external-ear defects is an unusual laterality signature and merits explicit `laterality`/description capture.

### 7.5 Human fetal expression — the anchoring anatomical evidence

> **[FULL-TEXT — Al-Jawahiri 2022 pp.1266, 1268 (RNAscope ISH)]**
> "ISH showed widespread expression of *SOX11* in fetal cranial structures. … At all Carnegie stages examined, *SOX11* was strongly expressed in the cerebral cortex and hindbrain. Expression within the developing retina and optic nerve was also noted, particularly in Carnegie stage 23. Of interest, *SOX11* expression was noted in the developing pituitary, lining the lumen of the adenohypophysis, and also within the neurohypophysis. There was no clear difference observed in spatial localization between *SOX11* expression and *GnRHR* expression."
> Figure 5: "*SOX11* expression in frontal cortex (\*), spinal cord (\*\*), and palate (\*\*\*)" at CS21 (~51 days post-conception); "*SOX11* expression in developing eye at CS23 (~56 days post-conception) in lens (\*), optic nerve (\*\*), and neuroretina (\*\*\*)"; "*SOX11* expression in pituitary at CS20 (~49 days post-conception) lining lumen of adenohypophysis (\*) and also in neurohypophysis (\*\*)."

This is high-value evidence: **each affected organ in the human phenotype has a matching human fetal *SOX11* expression domain.** Use it to justify the anatomical annotations directly.

---

## 8. Temporal Development

### 8.1 Onset

- **Onset:** **congenital** (HP:0003577). Structural malformations (coloboma, cleft palate, cardiac, renal, microcephaly, IUGR) arise during embryogenesis; the human fetal expression window documented by RNAscope is **Carnegie stages 20–23, ~49–56 days post-conception**. Developmental delay is recognised in infancy (HP:0003593 Infantile onset).
- **Onset pattern:** **chronic / static developmental**, not acute or episodic. No relapsing course.
- **Prenatal detectability:** IUGR and structural anomalies (TGA/Berry syndrome detected on prenatal imaging, PMID:42015706) can be prenatally apparent. One case died in the **neonatal period** (Al-Jawahiri case 11, p.Ala176Glu, with cerebellar hypoplasia and microcephaly) — perinatal lethality is possible but rare.

### 8.2 Progression

**Disease stages** (no formal staging system exists; the following is a natural-history synthesis):

| Stage | Window | Features |
|---|---|---|
| **Prenatal/embryonic** | CS20–23 onward | Structural malformation (brain, eye, palate, heart, kidney); IUGR |
| **Infancy** | 0–2 y | Hypotonia, feeding difficulty, poor suck, developmental delay recognised; **80% sit by 12 months** |
| **Early childhood** | 2–5 y | **70% walk independently by 30 months; 80% speak by 40 months**; ~20% never attain speech; microcephaly/short stature declare; autistic traits emerge |
| **Later childhood** | 5–12 y | ID severity established; ophthalmological features (myopia progression); hearing loss identified; behavioural phenotype consolidates |
| **Adolescence — CRITICAL WINDOW** | 12–18 y | **Delayed/absent puberty → the trigger for HH diagnosis**; scoliosis; GH deficiency |
| **Adulthood** | ≥18 y | Overweight/obesity frequent; scoliosis and visual impairment more prevalent than in paediatric cohorts; cognitive plateau (moderate ID typical); lifelong support needs |

- **Progression rate:** the neurodevelopmental core is **non-progressive** (static encephalopathy). Overlaid features (scoliosis, myopia, obesity, pubertal failure) are **slowly progressive / age-emergent**.
- **Disease course pattern:** **stable/static with age-emergent comorbidity**. Not episodic, not relapsing-remitting, not neurodegenerative.
- **Duration:** **chronic lifelong.**
- **Cohort age range:** "The mean age at examination was 9 years (range: neonate to 23 years)" [FULL-TEXT, Al-Jawahiri 2022 p.1265]. The adult cohort study (PMID:38117302) covers ≥18 y.

### 8.3 Patterns

- **Remission:** **none** — spontaneous or treatment-induced. No remission is possible for a developmental haploinsufficiency disorder. *Partial reversal of one manifestation is achievable:* GnRH-pump therapy "restored gonadotropin output within 72 h" [VERBATIM, PMID:42168980] — a pharmacological rescue of the downstream hormonal deficit, not disease remission.
- **Critical periods:**
  1. **CS20–23 (~7–8 weeks post-conception)** — the window of *SOX11*-dependent organogenesis. Irreversible once passed; the reason no disease-modifying therapy is conceivable postnatally for the malformation component.
  2. **Infancy–early childhood (0–5 y)** — the intervention window for speech, motor, and feeding therapy, where the ~20% risk of never attaining speech is determined.
  3. **Adolescence (11–14 y)** — the window for pubertal induction. Missing it costs bone density, growth, and psychosocial development. **This is the single most actionable clinical window in the disorder.**
  4. **First years of life** — cochlear-nerve imaging window; determines cochlear-implant candidacy (a CI is of limited benefit if the cochlear nerve is aplastic).

---

## 9. Inheritance and Population

### 9.1 Epidemiology

**Prevalence: not established. No formal prevalence or incidence estimate exists for *SOX11*-related NDD.** Neither Orphanet, GBD, CDC, WHO, nor any national registry publishes a rate. Recommend curating a `Prevalence` record with:

```yaml
prevalence:
- population: Worldwide
  measure_type: CASES_IN_LITERATURE
  prevalence_class: NOT_YET_DOCUMENTED
  notes: >-
    No formal prevalence estimate published. Approximately 82 individuals with
    SOX11 variants had been reported in the literature as of the 2024 review
    (PMID:37558216); 56 distinct variants catalogued (PMID:38591849). Ultra-rare;
    ascertainment is genotype-first via research exome/genome cohorts.
  evidence:
  - reference: PMID:37558216
    supports: SUPPORT
    evidence_source: HUMAN_CLINICAL
    snippet: "32 out of 82 subjects reported in the literature with SOX11 variants"
    explanation: >-
      Establishes the published case count as of 2024; no population rate is
      available for this disorder.
```

**Denominator anchors that can be cited:**
- **10 / 284** individuals in the CSS/BAF registry carried *SOX11* variants — i.e. *SOX11* is the **second-rarest** cause among the CSS genes studied, ahead only of *SMARCE1* (PMID:35126043; *ARID1B* 174, *SMARCA4* 41, *ARID1A* 20, *SMARCB1* 20, *ARID2* 14, *SOX11* 10, *SMARCE1* 5).
- **5 / 1,810** unrelated IHH probands carried pathogenic *SOX11* variants — ~0.28% of IHH (PMID:39290158).
- **2 / 79** patients in a microphthalmia/anophthalmia/coloboma cohort carried novel heterozygous *SOX11* variants — ~2.5% of MAC (PMID:25010521).
- Al-Jawahiri's 38 patients were drawn from DDD + 100,000 Genomes Project + GeneMatcher, so *SOX11* is a **rare but recurrent** finding in large-scale NDD sequencing.

**Orphanet caveat:** ORPHA:1465 covers Coffin-Siris syndrome as an umbrella. Because the field now treats *SOX11* syndrome as a distinct entity, any ORPHA:1465 prevalence figure would be an **over-estimate** if applied to *SOX11* alone. Do not import it.

### 9.2 Inheritance (genetic etiology)

| Attribute | Finding | Evidence |
|---|---|---|
| **Inheritance pattern** | **Autosomal dominant** (HP:0000006) | OMIM 615866; ClinGen validity "Definitive (AD)"; HPO annotation via PMID:24886874 |
| **Predominant mechanism** | **De novo** — 30/38 confirmed de novo in the largest cohort (~79%; ~94% of those where segregation was testable) | PMID:35341651 |
| **Penetrance** | Appears **high but with markedly variable expressivity**. No confirmed non-penetrant carrier has been reported, but the transmitting mother in PMID:33785884 was mildly affected (hypoplastic 5th toenails only, normal stature), and Al-Jawahiri's 2 sibships had a parent with ID presumed heterozygous. **Effectively: high penetrance for *some* phenotype, low penetrance for the severe phenotype.** |
| **Expressivity** | **Highly variable** — from neonatal death (case 11) to a mildly affected transmitting parent with isolated nail hypoplasia. Intrafamilial variability documented in the Hanker family. | PMID:35341651; 33785884 |
| **Germline mosaicism** | **DOCUMENTED** — one transmission from a mosaic mother. "This shows that recurrence could be possible due to mosaicism." | PMID:35341651 [FULL-TEXT p.1267] |
| **Genetic anticipation** | **Not applicable** — no repeat expansion; *SOX11* is intronless with no unstable repeat. No anticipation reported. | — |
| **Founder effects** | **None reported.** Cases span UK, Ireland, Netherlands, Belgium, Germany, Switzerland, France, Italy, India, Japan, China, USA, New Zealand, Brazil — no population-specific founder variant. | Author affiliations, PMID:35341651; 35938035; 36369738 |
| **Consanguinity** | **No role** (dominant disorder). Explicitly: the Hanker sisters were "born to non-consanguineous parents" [VERBATIM, PMID:33785884]. | — |
| **Carrier frequency** | **Not applicable** — dominant disorder, no healthy-carrier state. Pathogenic variants are absent from gnomAD. | §4.6 |

**Recurrence-risk counselling implication (curation-relevant):** for a proband with a confirmed de novo variant and non-mosaic parents, recurrence risk is low but **not zero** because of the documented mosaic transmission. This is a concrete, evidence-backed counselling point.

**Reproductive fitness note:** "Most *SOX11* variants in our cohort were de novo, in keeping with a severe syndrome that impairs reproductive fitness." [FULL-TEXT p.1267] Reduced fecundity is compounded by the hypogonadotropic hypogonadism itself — a mechanistically elegant explanation for the de novo predominance.

### 9.3 Population demographics

- **Affected populations:** no ethnic or ancestral predisposition. Al-Jawahiri explicitly noted "a consistent facial dysmorphology across multiple ethnic groups" [FULL-TEXT p.1265], which is itself a useful cross-population finding.
- **Geographic distribution:** worldwide; no endemic region. Reporting is skewed by sequencing access — UK (DDD/100kGP) and China (recent case reports) dominate. This is **ascertainment bias, not true geographic variation.**
- **Geographic distribution of specific variants:** none. Recurrent variants (p.Lys50Asn, p.Gly47Ser, p.Ala55Thr, p.Trp87Arg, p.Tyr116Cys, p.Arg51*) recur across unrelated populations — consistent with independent de novo mutation at mutable/functionally-critical residues rather than shared ancestry.
- **Sex ratio:** **no sex bias reported (autosomal).** Both sexes affected. **However, sex profoundly affects *ascertainment* of the endocrine phenotype:** "In males with *SOX11* syndrome presentation, genital malformations at birth was reported, but in both sexes delayed puberty was the principal manifestation" [FULL-TEXT p.1268]. Males present earlier (cryptorchidism/micropenis at birth); females typically not until primary amenorrhoea. Curate this as a diagnostic-bias note, not a sex ratio.
- **Age distribution:** paediatric-dominated in the literature (mean age at examination 9 years, range neonate–23 years). Adults are systematically under-represented — the sole adult cohort (n=35) is mixed-BAFopathy (PMID:38117302). **Adult natural history is a major gap.**

---

## 10. Diagnostics

### 10.1 Genetic testing (the diagnostic mainstay)

**Recommended approach:** *SOX11*-related NDD is a **genotype-first diagnosis**. There is no biochemical marker and the facial gestalt is explicitly non-specific, so molecular testing is the only reliable route.

| Modality | Utility for *SOX11* | Notes |
|---|---|---|
| **Trio exome sequencing (WES)** | **High — first-line.** The modality that identified essentially all reported SNVs (Tsurusaki 2014, Hempel 2016, and most case reports). Trio design is essential to establish de novo status. | NCIT:C101293 Whole Exome Sequencing |
| **Genome sequencing (WGS)** | **High.** Used in the 100,000 Genomes Project arm. Advantage: simultaneous SNV + CNV detection in a single assay — valuable because ~11% of cases are deletions. | NCIT:C101294 Whole Genome Sequencing |
| **Chromosomal microarray (CMA)** | **Essential for the deletion subset.** 2p25.2 deletions (from ~1.1 Mb up to contiguous-gene deletions) are CMA-detectable. Historically how the disorder was discovered (PMID:18992374). | NCIT:C101297 Comparative Genomic Hybridization *(verify)* |
| **NDD / ID gene panel** | Moderate — only if *SOX11* is included. Many older ID panels omit it. | |
| **Kallmann syndrome / IHH panel** | **Recommended addition.** "*SOX11* should be included in Kallmann syndrome gene panels." [VERBATIM, PMID:42168980]. *SOX11* was found in 5/1,810 IHH probands (PMID:39290158). Currently under-represented on IHH panels. | |
| **CSS / BAFopathy panel** | Moderate — *SOX11* is conventionally included as "CSS9". | |
| **Single-gene *SOX11* sequencing** | Low yield as a primary strategy (phenotype too non-specific); appropriate for **targeted family testing** once a familial variant is known, and for **parental mosaicism testing** (deep sequencing recommended given the documented mosaic transmission). | |
| **Karyotyping** | Low yield — deletions are typically submicroscopic ("a cryptic chromosome abnormality," PMID:18992374). | |
| **FISH** | Only for confirming/segregating a known 2p25.2 deletion. | |
| **Mitochondrial DNA testing** | **Not indicated.** | |
| **Repeat expansion testing** | **Not indicated** — intronless gene, no repeat mechanism. | |

**Two technical pitfalls to record:**
1. **Single-exon gene.** Exome CNV callers with poor single-exon resolution can miss intragenic *SOX11* events. Pair sequencing with CMA or use a CNV-competent WGS pipeline.
2. **No splice variants exist.** Any reported *SOX11* splice-site variant should trigger re-verification.

### 10.2 Omics-based diagnostics — the *SOX11* episignature (clinically deployed)

This is the standout diagnostic tool and belongs prominently in the entry.

**Assay:** genome-wide DNA methylation on **peripheral blood** DNA via Illumina Infinium MethylationEPIC array, interpreted against the EpiSign Knowledge Database with an SVM classifier producing an **MVP score (0–1)**.

**Performance:** "In all steps, the testing samples were correctly clustered with the training samples, further providing evidence of a robust common DNA methylation signature for *SOX11*." A 224-DMP signature with global hypomethylation; when trained against 38 additional NDD episignatures, "A high MVP score was seen in 10 *SOX11* samples with much improved specificity relative to other EpiSign conditions." [FULL-TEXT pp.1265–66]

**Clinical uses:**
- **Reclassification of VUS** — the primary value, given that 25 of 29 reported SNVs are missense.
- **Differentiation from BAFopathies** — no BAFopathy sample clustered with *SOX11*.
- **Diagnostic confirmation** in genetically unsolved patients.

> **[FULL-TEXT p.1269]** "It also shows the utility of DNA methylation profiling as a useful biomarker for clinical diagnosis of *SOX11*-related disorders."

**Caveat to record:** derived from only **10 cases vs 50 controls** — a small training set. Al-Jawahiri acknowledge "a highly sensitive and specific blood-derived episignature with small number of DMPs for *SOX11* syndrome, using a relatively small number of patient samples."

**Other omics diagnostics:** RNA sequencing — no established diagnostic role. Proteomics, metabolomics, liquid biopsy — **not applicable / no role.**

### 10.3 Clinical tests

**Laboratory tests / biomarkers:**

| Test | Purpose | LOINC (verify) |
|---|---|---|
| Basal LH and FSH | Diagnose hypogonadotropic hypogonadism (low gonadotropins with low sex steroids) | LOINC:10501-5 (LH); LOINC:15067-2 (FSH) |
| Testosterone (males) / estradiol (females) | Confirm hypogonadism | LOINC:2986-8; LOINC:2243-4 |
| GnRH stimulation test / GnRH-pump response | Distinguish hypothalamic from pituitary defect. GnRH-pump therapy restored gonadotropin output within 72 h in one case, localising the lesion to the hypothalamus. | — |
| hCG stimulation test | Assess testicular function | — |
| **GH provocative testing / IGF-1** | GH deficiency and "decreased growth hormone response" are documented features (PMID:39290158; OMIM synopsis) | LOINC:2484-4 (IGF-1) |
| TSH / free T4 | Hypothyroidism reported (PMID:39290158) | LOINC:3016-3; LOINC:3024-7 |
| **Anti-Müllerian hormone, inhibin B** | Additional gonadal-axis markers in IHH workup | — |
| **AFP** | **NOT indicated** — the AFP/hepatoblastoma surveillance in CSS is ***ARID1A*-specific**, not *SOX11* (PMID:23556151). Do not import it. | — |

**There is no *SOX11*-specific biochemical or metabolic biomarker.** The DNA methylation episignature is the only molecular biomarker.

**Imaging studies:**

| Study | Yield / purpose |
|---|---|
| **Brain MRI** | **High-yield: abnormal in 12/20 (60%) imaged.** Detects cerebellar hypoplasia, corpus callosum agenesis, arhinencephaly, pituitary size. Performed in only 42% — **under-utilised.** RadLex/NCIT:C16809 Magnetic Resonance Imaging |
| **Dedicated internal-auditory-canal MRI** | **Essential for SNHL.** "Magnetic resonance imaging is useful in delineating the cochlear nerve deficiency and other CSS-related brain malformations." [VERBATIM, PMID:35642566]. Determines cochlear-implant candidacy. |
| **Olfactory MRI** | Detects olfactory bulb/nerve hypoplasia → establishes Kallmann phenotype (PMID:42168980) |
| **Pituitary MRI with height measurement** | Pituitary height 3.4 mm reported; small pituitary in 2 Al-Jawahiri patients |
| **Renal ultrasound** | Renal anomalies are the commonest internal malformation (~8%); mouse data predict duplex kidney/hydroureter |
| **Echocardiography** | Coarctation, VSD, TGA/Berry syndrome reported. "The authors recommend enhanced cardiovascular evaluation for fetuses carrying *SOX11* variants" (PMID:42015706) |
| **Fundus photography / OCT** | High myopia with fundus tessellation and cone-rod dystrophy (PMID:40933692); "recommend ophthalmological examination with fundus screening for CSS9 patients with significant visual impairments" |
| **Skeletal survey / spine radiographs** | Scoliosis (prevalent in adults), spina bifida |
| **Prenatal ultrasound / fetal echocardiography** | TGA detected prenatally (PMID:42015706) |

**Functional tests:** growth-hormone provocative testing; formal smell testing (**but note: "Given the neurodevelopmental delay in *SOX11* syndrome, formal assessment of olfaction is not possible"** in many patients [FULL-TEXT p.1268] — MRI is the practical surrogate); pulmonary/cardiac function testing only as indicated by structural findings.

**Electrophysiology:**
- **Audiology — ABR/BAER and behavioural audiometry:** essential; SNHL with inner-ear malformation and cochlear nerve deficiency are established features.
- **EEG:** low yield — only 2/38 patients had epilepsy. Indicated only on clinical suspicion.
- **ERG:** consider for cone-rod dystrophy (single case).
- **EMG/NCS:** not indicated.

**Biopsy / pathology findings:** **none — no diagnostic histopathology exists.** Do not curate a `histopathology` section beyond a note that none is established. Immunohistochemistry for SOX11 protein is a **mantle-cell-lymphoma** diagnostic and has no role here.

### 10.4 Clinical criteria and differential diagnosis

**Standardised diagnostic criteria:** **none exist.** There are no consensus clinical criteria, no DSM/ICD-specific code, and no society guideline. Diagnosis is molecular. The nearest thing to a clinical trigger is Hanker et al.'s proposed triad:

> **[VERBATIM — PMID:33785884]** "We suggest that the combination of Cogan ocular motor apraxia, hypoplastic nails of fifth toes, and developmental delay give the important diagnostic clue for a variant in the *SOX11* gene (OMIM 615866, MR 27)."

Al-Jawahiri add: "Our study confirms that *SOX11* syndrome should be part of the differential diagnosis of oculomotor apraxia." [FULL-TEXT p.1268]

**Differential diagnosis with distinguishing features:**

| Condition | Gene(s) | Distinguishing features |
|---|---|---|
| **Coffin-Siris syndrome (classical BAFopathies)** | *ARID1B* (commonest), *ARID1A*, *ARID2*, *SMARCA4*, *SMARCB1*, *SMARCE1*, *SMARCC2*, *DPF2*, *BICRA*, *PHF6* | ***ARID1B* CSS: coarse facies present, and absent oculomotor apraxia / structural eye disease / hypogonadotropic hypogonadism.** *SOX11*: the reverse. Also **distinct episignatures** — the definitive discriminator. *ARID1A* uniquely warrants AFP/hepatoblastoma surveillance. |
| **Pitt-Hopkins syndrome** | *TCF4* | 7/32 (22%) of detailed *SOX11* cases "had a clinical presentation overlapping PTHS" [VERBATIM, PMID:37558216]. PTHS: hyperventilation/apnoea episodes, distinctive facial gestalt, autonomic dysfunction. Both have episignatures — use methylation to resolve. **A normal *TCF4* in a PTHS-like patient should prompt *SOX11* testing.** |
| **SOX4-related NDD** | *SOX4* | Paralogous SoxC disorder; "mild dysmorphism" (PMID:30661772, 35232796). Highest NEC-confusion risk. |
| **SOX12-related** | *SOX12* | Single report: generalized epilepsy, ID, childhood emotional/behavioural disorder (PMID:39057025) |
| **Kallmann syndrome / congenital IHH** | *ANOS1/KAL1*, *FGFR1*, *FGF8*, *PROKR2*, *PROK2*, *CHD7*, *SOX10*, *SOX2*, *SEMA3A* etc. | *SOX11* now belongs on this panel. Distinguishing feature: *SOX11* IHH is accompanied by ID/DD, which is atypical for most isolated IHH genes. |
| **CHARGE syndrome** | *CHD7* | Overlaps on cochlear nerve deficiency and IHH. Mechanistically linked: SOX11 "highly correlated with the expression of *CHD7*, which regulates *SOX11*" [VERBATIM, PMID:35642566]. CHARGE: coloboma + heart + atresia choanae + retarded growth + genital + ear — the choanal atresia and semicircular-canal aplasia are discriminating. |
| **SOX2-anophthalmia syndrome** | *SOX2* | Another SOXopathy with ocular malformation + IHH. Distinguishing: severe anophthalmia/microphthalmia dominates. |
| **Waardenburg / Waardenburg-Hirschsprung** | *SOX10* | SOXopathy with paralogous HMG-box variants (§4.4). Pigmentary anomalies + SNHL + aganglionosis. |
| **Cogan-type oculomotor apraxia differentials** | *APTX* (AOA1), *SETX* (AOA2), *ATM*, Joubert genes | These are **progressive ataxias**; *SOX11* has cerebellar hypoplasia but explicitly **"no clearly defined ataxia."** That negative is the discriminator. |
| **Pituitary stalk interruption syndrome** | genetically heterogeneous | *SOX11* appears in PSIS cohorts (PMID:33270637) |
| **CAKUT (isolated)** | multiple | Rare *SOX11* variants found in a CAKUT cohort (PMID:29459093) — but with ID/DD in the syndromic form |

**Framing for curators:** *SOX11* syndrome sits at a **four-way nosological crossroads** — BAFopathy/CSS, SOXopathy, Pitt-Hopkins-spectrum, and Kallmann/IHH. It has been diagnosed *from* each of those four starting points. This is the single most important framing statement for the entry, and the episignature is what resolves it.

### 10.5 Screening

- **Newborn screening: not applicable** — no biochemical marker, no NBS panel inclusion, no actionable neonatal intervention.
- **Carrier screening: not applicable** — dominant disorder, no carrier state.
- **Cascade screening:** **indicated.** Test the parents of any proband (including deep sequencing for mosaicism) and, if a familial variant is found, at-risk relatives. Justified by the documented mosaic transmission and the mildly-affected-transmitting-parent family.
- **Prenatal diagnosis / PGT:** available for a known familial variant (see §13).

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

- **Survival rate (5/10-year, overall):** **not established.** No survival analysis has been published.
- **Life expectancy:** **not established**, but the evidence points to **near-normal survival in the majority**. The disorder is developmental, not degenerative; there is no organ failure in the typical course; and adults into at least their fifth decade are described in the mixed-BAFopathy adult cohort. Al-Jawahiri's cohort spanned neonate–23 years.
- **Mortality rate / disease-specific mortality:** **not established.** **One documented death** in the largest cohort: Al-Jawahiri case 11 (p.Ala176Glu) "died early in the neonatal period. They had cerebellar hypoplasia and microcephaly" [FULL-TEXT p.1267] — i.e. **1/38 (~2.6%) neonatal mortality** in that cohort. Treat this as a single observation, not a rate.
- **Mouse contrast worth noting:** *Sox11*-null mice are **uniformly neonatally lethal** from cardiac outflow-tract defects, whereas human heterozygotes usually survive. The species gap is one of **dosage** (mouse homozygous null vs human heterozygote), and it is why zebrafish became the preferred model (§15).

### 11.2 Morbidity and function

| Domain | Outcome |
|---|---|
| **Cognitive** | "Cognitive outcomes range from profound intellectual disability (ID) to low normal IQ, with most individuals having moderate ID" [VERBATIM, PMID:38117302] |
| **Communication** | The dominant disability. ~20% never attain speech; 64% of the broader CSS registry have language-related challenges and 32% are non-verbal (PMID:35126043) |
| **Adaptive behaviour** | 33% borderline, 39% mild impairment; communication and daily-living domains worse than socialisation (PMID:37924570) |
| **Behavioural** | 90% clinically significant autistic traits (62% severe); ASD/ADHD diagnoses common. "behavioral anomalies are more prevalent than in published pediatric or mixed cohorts" in adults (PMID:38117302) |
| **Motor** | 70% walk independently by 30 months; hypotonia common; generally ambulatory |
| **Sensory** | Visual impairment "more prevalent" in adults; unilateral SNHL in a subset |
| **Endocrine** | HH requires lifelong hormone replacement; infertility likely without assisted reproduction |
| **Musculoskeletal** | Scoliosis more prevalent in adults |
| **Metabolic** | "overweight and obesity are frequent in adults with CSS" (PMID:38117302) |
| **Disability outcomes (ICF framing)** | Lifelong support needs for most; independent living unlikely for the moderate-ID majority |

**Quality-of-life measures:** **no EQ-5D, SF-36, PROMIS, or disease-specific PRO has been administered in a *SOX11* cohort.** The only standardised instruments used are adaptive-behaviour and autism-trait measures (PMID:37924570). **Explicit gap.**

### 11.3 Disease course — complications

Feeding difficulty ± aspiration (may need gastrostomy); epilepsy (~5%, low); progressive scoliosis; progressive high myopia with fundus/retinal changes; hearing loss with limited CI benefit if the cochlear nerve is deficient; pubertal failure with consequent low bone mineral density; infertility; adult obesity and its sequelae; complications of repaired congenital heart disease; cleft-palate sequelae (speech, otitis media); renal complications of CAKUT.

### 11.4 Recovery potential

**No recovery of the neurodevelopmental core.** Developmental gains occur with therapy but the underlying static encephalopathy is permanent. **Selective, genuine reversibility exists for the endocrine arm**: GnRH-pump therapy "restored gonadotropin output within 72 h" [VERBATIM, PMID:42168980], and pubertal induction, GH replacement, and levothyroxine can fully correct their respective deficits. Surgical correction of cleft palate, cardiac lesions, cryptorchidism, and microtia is anatomically effective.

### 11.5 Prediction

**Prognostic factors — with a critical caveat.** A **domain-based genotype–phenotype correlation** is emerging:

> **[VERBATIM — PMID:38591849, Wu et al., *Am J Med Genet A* 2024]** "Analysis of 56 *SOX11* variants showed variants affecting the high-mobility group (HMG) domain were more likely to cause the widest range of organ anomalies."
> The authors "conclude that thorough clinical examination is warranted for patients carrying pathogenic *SOX11* variants affecting the HMG domain, as these variants demonstrate the widest range of organ anomalies."

⚠️ **But this correlation is contradicted at the individual level.** The **most severe outcome reported (neonatal death) occurred with a NON-HMG missense variant (p.Ala176Glu)** whose in-vitro transactivation deficit was explicitly milder than that of the PTVs ("A176E impairs SOX11 activity but to a much lesser extent than Y294\* or G384Rfs\*14"). Therefore:

- **In-vitro residual transactivation does NOT predict clinical severity.**
- **HMG-domain localisation predicts breadth of organ involvement, not severity of outcome.**
- Curate this as an explicit **KNOWLEDGE_GAP discussion**: genotype–phenotype prediction in *SOX11* syndrome is not currently reliable at the individual level.

**Other prognostic factors:** attainment of speech by ~40 months (the 20% who don't have a worse functional trajectory); presence of cerebellar hypoplasia + microcephaly (co-occurred in the one fatal case); presence of major congenital heart disease.

**Prognostic biomarkers:** **none.** The episignature is diagnostic, not prognostic — no correlation between MVP score or DMP pattern and clinical severity has been reported. Explicit gap.

---

## 12. Treatment

**There is no disease-modifying or curative therapy.** Management is entirely **supportive, symptom-directed, and multidisciplinary**. All recommendations below are extrapolated from CSS/BAFopathy management (PMID:23556151, GeneReviews) plus *SOX11*-specific endocrine and sensory findings; **no *SOX11*-specific clinical practice guideline exists**, and **no clinical trial has ever been conducted in this disorder.**

### 12.1 Pharmacotherapy

| Treatment | Indication | Modality | NCIT suggestion |
|---|---|---|---|
| **Testosterone (males) / estrogen + progestin (females)** | Pubertal induction and maintenance in HH; protects bone density | SMALL_MOLECULE | `NCIT:C15986` Pharmacotherapy + `therapeutic_agent` CHEBI:17347 testosterone / CHEBI:16469 17β-estradiol |
| **Pulsatile GnRH (GnRH pump) or gonadotropin therapy (hCG + FSH)** | Fertility induction and gonadotropin restoration in HH. Evidence: restored gonadotropin output within 72 h (PMID:42168980) | PEPTIDE | `NCIT:C15986` + `therapeutic_agent` NCIT:C1362 Gonadotropin-Releasing Hormone *(verify)* |
| **Recombinant human growth hormone (somatropin)** | GH deficiency / short stature (GH deficiency documented, PMID:39290158) | PROTEIN_REPLACEMENT | `NCIT:C15986` + NCIT:C1663 Somatropin *(verify)* |
| **Levothyroxine** | Hypothyroidism (PMID:39290158) | SMALL_MOLECULE | `NCIT:C15986` + CHEBI:41355 levothyroxine *(verify)* |
| **Antiseizure medication** | Epilepsy (~5% only — do not treat prophylactically) | SMALL_MOLECULE | `NCIT:C15986` |
| **ADHD stimulants / non-stimulants; ASD-associated behaviour management** | ADHD, aggression, self-injury, anxiety | SMALL_MOLECULE | `NCIT:C15986` |
| **Atropine / low-dose atropine, myopia control** | Progressive high myopia (single case, PMID:40933692) | SMALL_MOLECULE | `NCIT:C15986` |
| **Melatonin / sleep interventions** | Sleep disturbance (CSS surveillance item) | SMALL_MOLECULE | `NCIT:C15986` |

**Pharmacogenomics:** **none. No CPIC guideline, no FDA PGx biomarker, and zero PharmGKB/CPIC records for *SOX11*** (confirmed via ClinGen: "CPIC/PharmGKB Records: 0/0"). Standard PGx considerations apply only to the general drug classes used (e.g. CYP2D6 for some psychotropics), not to *SOX11* itself.

### 12.2 Advanced therapeutics

| Modality | Status for *SOX11* |
|---|---|
| **Gene therapy** | **None. Not in development.** Conceptually near-infeasible: the pathogenic window is embryonic (Carnegie stages 20–23), so postnatal *SOX11* restoration could not rescue completed malformations. |
| **Gene editing (CRISPR)** | None clinically. CRISPR is used **as a research tool** (isogenic hESC line, PMID:31035284; zebrafish mutants, PMID:33061816). |
| **RNA-based therapy (ASO, siRNA, mRNA)** | **None.** Note the mechanistic mismatch: this is a **haploinsufficiency** disorder, so knockdown modalities (ASO RNase H, siRNA) are the wrong direction. A hypothetical upregulation strategy (e.g. targeting a *SOX11* repressor such as PRC2/EED, PMID:31204298, or stabilising SOX11 protein via the USP11 axis, PMID:33579706) is **speculative and unpublished** — record as a research direction, not a treatment. |
| **Targeted therapy** | None. |
| **Immunotherapy / cell therapy / CAR-T** | Not applicable. |
| **Epigenetic/chromatin-targeting agents** | **Hypothesis only.** "The plastic nature of epigenomic profiles may offer an opportunity to study the use of chromatin and epigenomic targeting agents as a potential therapeutic avenue." [FULL-TEXT, Al-Jawahiri 2022 p.1269] — an author-stated future direction with no experimental support in *SOX11*. |

### 12.3 Surgical and interventional

| Intervention | Indication | NCIT suggestion |
|---|---|---|
| Cleft palate repair | Cleft secondary palate | `NCIT:C15329` Surgical Procedure |
| Cardiac surgical repair | Coarctation, VSD, TGA/Berry syndrome | `NCIT:C15329` |
| Orchidopexy | Cryptorchidism | `NCIT:C15329` |
| Gastrostomy tube placement | "Feeding therapy with consideration of placement of gastrostomy tube in those with persistent feeding issues" [PMID:23556151] | `NCIT:C15329` |
| Strabismus / ptosis surgery | Ocular motility, ptosis | `NCIT:C15329` |
| Scoliosis surgery | Progressive scoliosis (adults) | `NCIT:C16186` Orthopedic Surgical Procedure |
| Microtia reconstruction (auricular) | Unilateral microtia (PMID:38591849) | `NCIT:C15329` |
| Urological surgery | CAKUT complications | `NCIT:C15329` |
| **Cochlear implantation — CONDITIONAL** | SNHL. **⚠️ Critical caveat: cochlear nerve aplasia/hypoplasia markedly limits or precludes CI benefit. MRI assessment of the cochlear nerve is mandatory before CI in this disorder** (PMID:35642566). Auditory brainstem implant may be the alternative. | `NCIT:C15329` / DEVICE |
| Hearing aids | SNHL where residual nerve function permits | DEVICE |

### 12.4 Supportive and rehabilitative

| Intervention | Rationale | NCIT |
|---|---|---|
| **Speech and language therapy** | **The highest-priority intervention.** "childhood speech interventions are necessary in children with a diagnosis of CSS" [PMID:35126043]; ~20% never attain speech; AAC (augmentative and alternative communication) should be introduced early | `NCIT:C159273` Speech Therapy → `therapeutic_modality: BEHAVIORAL` |
| Physical therapy | Hypotonia, motor delay, gait | `NCIT:C15302` Physical Therapy → BEHAVIORAL |
| Occupational therapy | Adaptive/daily-living skills (the weakest Vineland domain) | `NCIT:C121351` Occupational Therapy → BEHAVIORAL |
| Feeding therapy | Poor suck, feeding difficulty | `NCIT:C15433` Nutritional Support *(do NOT auto-tag as BEHAVIORAL per dismech CLAUDE.md)* |
| Early intervention / special education | Global developmental delay | `NCIT:C15315` Rehabilitation |
| Behavioural intervention (ASD/ADHD) | 90% autistic traits; leverage the preserved social motivation | `NCIT:C181743` Behavioral Counseling → BEHAVIORAL |
| Nutrition/weight management | Frequent adult overweight/obesity | `NCIT:C15447` Dietary Intervention → BEHAVIORAL |
| Supportive care (general) | Multisystem coordination | `NCIT:C15747` Supportive Care |
| **Genetic counselling** | Recurrence risk incl. mosaicism; reproductive options | `NCIT:C15240` Genetic Counseling |

### 12.5 Experimental treatments

**None. There are ZERO registered clinical trials for *SOX11*-related neurodevelopmental disorder** on ClinicalTrials.gov, the EU CTR, or WHO ICTRP. Do not populate a `clinical_trials` section; record the absence explicitly as a `notes:` statement or a `KNOWLEDGE_GAP` discussion.

### 12.6 Treatment outcomes

- **Response rates:** no systematic data. The only quantified therapeutic response in the literature is the GnRH-pump gonadotropin restoration within 72 h (n=1, PMID:42168980).
- **Side effects / adverse events:** no *SOX11*-specific safety signal exists; standard class-effect profiles apply (e.g. growth-hormone-associated risks, sex-steroid effects on epiphyseal fusion, gastrostomy complications). No FAERS signal specific to this population.

### 12.7 Treatment strategy

**Algorithm (synthesised — no published guideline exists):**

1. **At diagnosis — baseline multisystem evaluation.** The strongest published recommendation: *SOX11*-related disorder "mandat[es] comprehensive baseline evaluation" including "endocrine assessment, neurodevelopmental screening, and imaging" (PMID:42168980). Concretely: brain MRI (with dedicated IAC + olfactory + pituitary sequences), audiology, ophthalmology with fundus screening, renal ultrasound, echocardiogram, growth parameters, feeding/nutrition safety assessment, developmental assessment, spine examination.
2. **Ongoing (each visit, per CSS GeneReviews):** "Measurement of growth parameters; evaluation of nutrition status and safety of oral intake; assessment for new neurologic manifestations"; behavioural assessment (anxiety, ADHD, autism, aggression, self-injury); sleep; developmental/educational progress.
3. **Periodic:** annual ophthalmology and audiology; dental review at least every 6 months.
4. **⚠️ At ages 11–14 — the pubertal checkpoint.** Proactively assess pubertal status (Tanner staging, basal LH/FSH, sex steroids) rather than waiting for referral. **21% of patients have HH, and the intervention window is finite.** This is the highest-value, most-often-missed action in the disorder.
5. **Adulthood:** transition planning; weight/metabolic management; scoliosis and vision surveillance; ongoing hormone replacement.

**Combination therapies:** hormone replacement is inherently combinatorial (sex steroid ± GH ± levothyroxine); therapy bundles (speech + OT + PT) are standard.
**Personalised/genotype-guided treatment:** **not yet actionable.** The HMG-domain → broader-organ-involvement correlation (PMID:38591849) is the only genotype-informed recommendation, and it guides *screening intensity*, not therapy choice. **No genotype-guided treatment exists.**

---

## 13. Prevention

### 13.1 Primary prevention

**Not possible.** The disorder arises from de novo germline mutation during gametogenesis/early embryogenesis; there is no modifiable exposure, no vaccine-preventable component, and no risk-factor modification available. The only "primary prevention" available operates at the reproductive-decision level:

- **Preimplantation genetic testing (PGT-M)** for couples with a known familial *SOX11* variant (including a mosaic or mildly-affected parent).
- **Prenatal diagnosis** (CVS/amniocentesis) for a known familial variant. Available per CSS GeneReviews: "Prenatal and preimplantation genetic testing are available options."

### 13.2 Secondary prevention (early detection + early intervention)

This is where the real preventive leverage lies:
- **Comprehensive baseline evaluation at molecular diagnosis** (see §12.7) — detects treatable/correctable lesions (HH, GH deficiency, hypothyroidism, cardiac, renal, hearing, vision) before they cause irreversible harm.
- **Early speech/language intervention and AAC introduction** — the ~20% non-verbal rate makes early AAC a preventive measure against permanent communication failure.
- **Proactive adolescent endocrine screening** — prevents the bone-density, growth, and psychosocial consequences of unrecognised pubertal failure.
- **Cochlear nerve MRI before considering CI** — prevents a futile surgery.

### 13.3 Tertiary prevention (preventing complications in affected individuals)

- Pubertal induction → prevents osteoporosis/low BMD and psychosocial morbidity.
- Weight/nutrition management from childhood → pre-empts the frequent adult obesity.
- Spine surveillance → early scoliosis intervention.
- Ophthalmological surveillance including fundus → prevents avoidable visual loss from progressive myopia/retinopathy.
- Dental review ≥2×/year and annual audiology/ophthalmology (per CSS surveillance).
- Aspiration prevention via feeding-safety assessment.

### 13.4 Immunization

**Not applicable** — no vaccine-preventable component. Routine childhood immunisation per standard schedule; no contraindication arises from the disorder.

### 13.5 Screening and early detection

- **Population/newborn screening: not applicable or recommended** (no biochemical marker, no NBS panel, no neonatal-actionable intervention).
- **Genetic screening:** cascade testing of relatives for a known familial variant; **parental testing including deep sequencing for mosaicism** is specifically warranted given the documented mosaic transmission; PGT-M and prenatal testing as above.
- **Risk stratification:** the one published stratifier is variant domain — HMG-domain variants warrant the most thorough multi-organ evaluation (PMID:38591849). No validated risk-prediction model or clinical calculator exists.
- **Panel-inclusion advocacy as a screening measure:** "*SOX11* should be included in Kallmann syndrome gene panels" (PMID:42168980) — a concrete, actionable diagnostic-yield recommendation.

### 13.6 Behavioural interventions

No lifestyle modification prevents the disorder. Post-diagnosis behavioural/lifestyle measures target complication prevention: physical activity and dietary management for weight, sleep hygiene, and behavioural therapy for ASD/ADHD-associated behaviours.

### 13.7 Counselling

**Genetic counselling is a core intervention** (`NCIT:C15240`). Content to convey:
1. Autosomal dominant; ~79–94% de novo.
2. **Recurrence risk after a de novo variant is low but NOT zero** — parental gonadal/germline mosaicism is documented.
3. **Test both parents**, and consider deep sequencing for low-level mosaicism.
4. Variable expressivity: an apparently unaffected or minimally-affected parent may be a carrier — the transmitting mother in PMID:33785884 had only hypoplastic 5th toenails. **Examine parents' fifth toenails.**
5. An affected individual's own offspring risk is 50% — but reproductive fitness is reduced by both ID and hypogonadotropic hypogonadism, and fertility may require assisted reproduction.
6. Prenatal/PGT options; and prenatal cardiovascular evaluation is specifically recommended for fetuses with a known *SOX11* variant (PMID:42015706).

### 13.8 Public health and environmental interventions

**Not applicable.** No sanitation, vector-control, environmental-remediation, or population health-education intervention is relevant to a de novo Mendelian disorder. The one legitimate public-health-adjacent action is **improving access to trio exome/genome sequencing and to episignature testing**, which increases diagnostic yield and enables the surveillance benefits above.

### 13.9 Prophylaxis

**No pharmacological or procedural prophylaxis exists.** Specifically: no antiseizure prophylaxis is warranted (epilepsy ~5%), and **no oncological prophylaxis or tumour surveillance is indicated** — the *ARID1A* AFP/hepatoblastoma protocol does **not** extend to *SOX11*.

---

## 14. Other Species / Natural Disease

### 14.1 Taxonomy and orthologous genes

| Species | NCBI Taxon | Gene | Gene ID | Notes |
|---|---|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | *SOX11* | 6664 (hgnc:11191) | Reference |
| *Mus musculus* | NCBITaxon:10090 | *Sox11* | 20666 (MGI:98359) | Primary mammalian model |
| *Rattus norvegicus* | NCBITaxon:10116 | *Sox11* | — | No disease model reported |
| *Danio rerio* | NCBITaxon:7955 | ***sox11a*** and ***sox11b*** | — | **Two paralogues from teleost genome duplication** — *sox11a* carries the CSS-like phenotype |
| *Xenopus laevis / tropicalis* | NCBITaxon:8355 / 8364 | *sox11* | — | Morpholino microcephaly model |
| *Caenorhabditis elegans* | NCBITaxon:6239 | ***sem-2*** | — | **A single SoxC gene**, essential for development — an elegant system precisely because there is no paralogous redundancy |

> **[VERBATIM — PMID:40832700]** "*Caenorhabditis elegans* has a single SoxC protein, SEM-2, which is essential for development. … The equivalent amino acid of SOX11 Y116 is SEM-2 Y160, a residue in the C-terminal tail of the highly conserved DNA-binding domain."

### 14.2 Breed

**Not applicable.** No breed-specific *SOX11* disorder is recorded; no VBO identifier applies.

### 14.3 Natural disease in other species

**No naturally occurring *SOX11* disorder has been reported in any non-human species.** There is no OMIA (Online Mendelian Inheritance in Animals) entry for *SOX11*, no companion-animal or livestock condition, and no wildlife disease. Every animal phenotype in the literature is **experimentally induced** (targeted deletion, CRISPR, or morpholino).

**Veterinary relevance: none.** This should be curated as an explicit negative — it is informative that no spontaneous animal model exists, which is why engineered models carry the entire comparative burden.

### 14.4 Comparative biology

**Comparative pathology — cross-species concordance and discordance (high curation value):**

| Phenotype | Human (het) | Mouse (homozygous null) | Zebrafish *sox11a* | Xenopus (MO) | *C. elegans sem-2[Y160C]* |
|---|---|---|---|---|---|
| Viability | Usually viable (1 neonatal death/38) | **Neonatal lethal** (congenital cyanosis) | Viable | — | Homozygous embryonic/larval lethality; **heterozygotes normal** |
| Microcephaly / small brain | ✔ | ✔ (reduced cerebrum + cerebellum) | ✔ | ✔ (reduced head area) | n/a |
| Growth deficiency | ✔ | ✔ | ✔ (3.3 hpf → adult) | — | reduced brood size |
| Cleft palate | ✔ (rare) | ✔ (Pierre Robin-like, via mandibular hypoplasia) | — | — | — |
| Ocular malformation (coloboma, lens) | ✔ | eyelid closure defects | ✔ (coloboma, abnormal lens, rod loss) | ↓interpupillary distance | — |
| Renal/CAKUT | ✔ (~8%) | ✔ (duplex kidney, malposition, hydroureter) | — | — | — |
| **Cardiac OFT defect** | rare (coarctation, VSD, TGA) | **✔ obligate & lethal** (VSD, common arterial trunk, DORV) | — | — | — |
| Skeletal / achondroplasia-like | short stature | ✔ impaired ossification | ✔ achondroplasia, bone deformity | — | — |
| Asplenia | ✘ not reported | ✔ | — | — | — |
| Lung / stomach / pancreas hypoplasia | ✘ not reported | ✔ | — | — | — |
| Hearing / sensory neuron | ✔ cochlear nerve deficiency | ✔ het: hearing impairment, normal inner ear; homozygous: ↓sensory neuron survival, ↓axonal growth | — | — | — |
| Olfactory bulb | ✔ hypoplasia (1) | ✔ small olfactory bulbs | — | — | — |
| Craniofacial | ✔ | ✔ | narrow pupillary distance | — | tail abnormalities |
| Adult neurogenesis (SGZ) | untestable | ✔ blunted (conditional KO) | — | — | — |

**Key interpretive points for curation:**
1. **The mouse over-models the disease.** *Sox11*-null mice die neonatally of cardiac OFT defects and show asplenia and visceral hypoplasia — features **absent or very rare** in human heterozygotes. The discordance is a **dosage** difference (homozygous null vs heterozygous LoF), not a species difference in gene function. This is a textbook `HUMAN_MODEL_MISMATCH` case: model-organism evidence exists, but its translational validity is limited by the zygosity mismatch. Al-Jawahiri's own framing: "The combined human and murine findings indicate that *SOX11* has a general role in brain development, rather than a predominant role in the cerebrum or cerebellum."
2. **The mouse's lethality created the need for zebrafish.** [VERBATIM, PMID:33061816] "Since the homozygous *SOX11* mutant mice died soon after birth, no suitable model was available for the study of the pathogenic mechanism of Coffin-Siris syndrome. To solve this problem, we generated two viable homozygous zebrafish mutants."
3. **The heterozygous mouse recapitulates the human hearing phenotype well.** "A heterozygous knockout mice model had hearing impairment with grossly normal inner ear structures like the two probands reported" [VERBATIM, PMID:35642566] — a rare instance of clean zygosity-matched concordance.
4. **The *C. elegans* het/homozygous dissociation** is the cleanest available argument that *SOX11[Y116C]* is a simple LoF allele and not dominant-negative.

**Evolutionary conservation:** the HMG DNA-binding domain is deeply conserved across SoxC proteins and across metazoa (human SOX11 Y116 ≡ *C. elegans* SEM-2 Y160). The SoxC downstream program is also conserved: the *hlh-8*/Twist axis in *C. elegans* mirrors the craniofacial role of Twist orthologs in human craniofacial disorders — "whose human counterparts, when mutated, are known to be associated with craniofacial disorders" [VERBATIM, PMID:40832700]. Conservation of the paralogue-based ACMG evidence (SOX10↔SOX11 equivalent residues, §4.4) is another practical manifestation.

### 14.5 Transmission

**Not applicable** — genetic disorder. No zoonotic potential, no cross-species susceptibility, no transmission.

---

## 15. Model Organisms

### 15.1 Mouse (*Mus musculus*) — MGI:98359

**Genetic models available:** MGI records **11 mutations/alleles** — 2 endonuclease-mediated, 8 targeted (knockout/conditional), 1 transgenic — with **88 phenotypes across 6 alleles in 8 genetic backgrounds** and 45 phenotype references.

**MGI phenotype summary:** "homozygous null mice display neonatal lethality with impaired ossification and impaired development of the heart, lung, spleen, stomach, skeleton and pancreas"; "mice homozygous for a different knock-out allele exhibit abnormal nervous system development and complete neonatal lethality."

**Key mouse studies:**

> **[VERBATIM — PMID:15254231, Sock et al., *Mol Cell Biol* 2004;24(15):6635–6644, DOI 10.1128/mcb.24.15.6635-6644.2004]**
> "*Sox11*-deficient mice died at birth from congenital cyanosis, likely resulting from heart defects. These included ventricular septation defects and outflow tract malformations that ranged from arterial common trunk to a condition known as double outlet right ventricle. Many other organs that normally express *Sox11* also exhibited severe developmental defects. We observed various craniofacial and skeletal malformations, asplenia, and hypoplasia of the lung, stomach, and pancreas. Eyelids and the abdominal wall did not close properly in some *Sox11*-deficient mice. This phenotype suggests a prime function for *Sox11* in tissue remodeling and identifies SOX11 as a potentially mutated gene in corresponding human malformation syndromes."

> **[VERBATIM — PMID:23483698, Wang et al., *Dev Dyn* 2013;242:638–653]**
> "In this study, we generated a *Sox11* floxed allele and a *Sox11* null allele in mice using the Cre-loxP technology. … *Sox11* null embryos developed small and disorganized brains, accompanied by transient proliferation deficits in NPCs. Deletion of *Sox11* in adult NPCs blunted proliferation in the SGZ. … our work provides evidence that *Sox11* is required for both embryonic and adult neurogenesis, and identifies potential downstream target genes."

> **[VERBATIM — PMID:26826126, Huang et al., *J Biol Chem* 2016;291:7107–7118]**
> "We found that loss of *Sox11* led to reduced cell proliferation in the developing mandibular mesenchyme via Cyclin D1, leading to mandibular hypoplasia, which blocks tongue descent. Extensive analyses of gene expression in *Sox11* deficiency identified FGF9 as a potential candidate target of *Sox11*… Finally we show, using in vitro assays, that *Sox11* directly regulates the expression of *Fgf9* and that application of FGF9 protein to *Sox11*-deficient palatal shelves restores the rate of BrdU incorporation. Taken together, the palate defects presented in the *Sox11* loss mutant mimic the clefting in the Pierre Robin sequence in humans."

> **[VERBATIM — PMID:29459093, Neirijnck et al., *Kidney Int* 2018;93:1142–1153]**
> "Deletion of *Sox11* in mice causes an extension of the domain expressing *Gdnf* within rostral regions of the nephrogenic cord and results in duplex kidney formation. On the molecular level SOX11 directly binds and regulates a locus control region of the protocadherin B cluster. At later stages of kidney development, SOX11 becomes restricted to the intermediate segment of the developing nephron where it is required for the elongation of Henle's loop. Finally, mutation analysis in a cohort of patients suffering from CAKUT identified a series of rare *SOX11* variants, one of which interferes with the transactivation capacity of the SOX11 protein."

> **[VERBATIM — PMID:33579706, Chiang et al., *Sci Adv* 2021]**
> "*Usp11* deficiency impairs layer 6 neuron production, delays late-born neuronal migration, and disturbs cognition and anxiety behaviors. Mechanistically, these functions are mediated by a previously unidentified Usp11 substrate, Sox11."

**Heterozygous mouse (the zygosity-matched model):** per PMID:35642566, "Homozygous ablation of SOX11 in a mouse model resulted in a reduction in sensory neuron survival and decreased axonal growth. A heterozygous knockout mice model had hearing impairment with grossly normal inner ear structures like the two probands reported."

**Also cited:** *Sox11*-null mice have **small olfactory bulbs** (relevant to the Kallmann/anosmia arm) and "generalized reduction in size of the cerebrum and cerebellum" (both via Al-Jawahiri refs 29/34).

**IMPC status:** the IMPC gene page for MGI:98359 shows **0 significant phenotypes and 0/24 physiological systems tested** — *Sox11* has **not** been through the IMPC pipeline (unsurprising given homozygous neonatal lethality). Do not cite IMPC as a phenotype source.

**Mouse limitations:** homozygous neonatal lethality precludes study of postnatal neurodevelopment, cognition, behaviour, puberty, and adult outcome — i.e. **precisely the domains that dominate the human phenotype.** Conditional (Cre-loxP) and heterozygous models are the workarounds. The homozygous cardiac/visceral phenotype **over-represents** what human heterozygotes experience.

### 15.2 Zebrafish (*Danio rerio*) — the preferred whole-organism model

> **[VERBATIM — PMID:33061816, Jia et al., *Int J Biol Sci* 2020, DOI 10.7150/ijbs.47510]**
> "we generated two viable homozygous zebrafish mutants, *sox11a^m/m^* and *sox11b^m/m^*. We found that the *sox11a^m/m^* mutant possessed Coffin-Siris syndrome features. The *sox11a^m/m^* mutants exhibited growth deficiency from 3.3 hpf embryos to adulthood. Furthermore, the *sox11a^m/m^* mutant also displayed microcephaly, narrow pupillary distance, achondroplasia, and bone deformity in adults. Growth deficiency could be rescued by the injection of *sox11a* mRNA at the one-cell stage. In addition, the expression levels of genes related to cartilage and bone were downregulated in the *sox11a^m/m^* mutant, indicating that *sox11a* mainly affected the growth and development of zebrafish by regulating the expression of genes related to skeletal development. Our results indicate that *sox11a^m/m^* mutant zebrafish offered a potential model system to help with the search for pathogenic mechanisms of human Coffin-Siris syndrome."

> **[VERBATIM — PMID:25010521, Pillai-Kastoori et al., *PLoS Genet* 2014, DOI 10.1371/journal.pgen.1004491]**
> "*Sox11*-deficient zebrafish embryos displayed delayed and abnormal lens formation, coloboma, and a specific reduction in rod photoreceptors, all of which could be rescued by treatment with the Hedgehog pathway inhibitor cyclopamine. We further demonstrate that the elevated Hedgehog signaling in *Sox11*-deficient zebrafish was caused by a large increase in *shha* transcription; indeed, suppressing *Shha* expression rescued the ocular phenotypes of *sox11* morphants. Conversely, over-expression of *sox11* induced cyclopia… We screened DNA samples from 79 patients with microphthalmia, anophthalmia, or coloboma (MAC) and identified two novel heterozygous *SOX11* variants in individuals with coloboma. In contrast to wild type human *SOX11* mRNA, mRNA containing either variant failed to rescue the lens and coloboma phenotypes of *Sox11*-deficient zebrafish, and both exhibited significantly reduced transactivation ability in a luciferase reporter assay."

Also: *sox11a/b* morpholino knockdown "causes brain abnormalities" (PMID:24886874), and Al-Jawahiri note the ocular malformations "are recapitulated in *sox11* null zebrafish, confirming the specificity of the finding."

**Strengths:** viable homozygous mutants; embryos are optically transparent for ocular phenotyping; **mRNA rescue and small-molecule (cyclopamine) rescue** are both demonstrated, giving a genuine functional-assay platform for VUS classification; established cross-species mRNA-complementation assay for human *SOX11* variants.
**Limitations:** teleost genome duplication (*sox11a*/*sox11b*) complicates dosage interpretation; no cognitive/behavioural readout comparable to human ID; no pituitary-gonadal axis readout matching human HH.
**Database:** ZFIN.

### 15.3 *Xenopus*

Morpholino knockdown of *Sox11*: "Knockdown of *Sox11* by MO injection resulted in a significant reduction in head area and interpupillary distance compared with controls (both p<0.0001)" (PMID:26543203). **Strength:** direct, quantitative microcephaly readout — the assay that established microcephaly as a *SOX11*-LoF consequence. **Limitation:** morpholino (transient knockdown, off-target concerns); no cognitive readout.
**Database:** Xenbase.

### 15.4 *Caenorhabditis elegans*

> **[VERBATIM — PMID:40832700, Baccas & Liu, *G3* 2025]**
> "Homozygous, but not heterozygous, *sem-2[Y160C]* animals exhibit a high rate of embryonic and larval lethality, egg-laying defects, reduced brood size, bivulval phenotype and a low penetrance of hermaphrodite tail abnormalities. Additionally, *sem-2[Y160C]* animals have reduced expression of *hlh-8*/Twist, whose human counterparts, when mutated, are known to be associated with craniofacial disorders. All the phenotypes observed in *sem-2[Y160C]* animals resemble SEM-2 loss-of-function phenotypes, suggesting that *SOX11[Y116C]* is a loss-of-function, recessive mutation that likely causes defects due to haploinsufficiency. Our work suggests that using *C. elegans* as a model system to analyze the molecular effects of point mutations associated with craniofacial defects has the potential for unraveling the underlying mechanisms."

**Strength:** the **only SoxC system with no paralogous redundancy**, enabling clean allele-series analysis; humanised point-mutation knock-in (Y116C ≡ Y160C) at low cost; establishes the LoF/non-dominant-negative mechanism.
**Limitation:** no nervous-system, craniofacial, ocular, or endocrine homology to human disease; results are about protein-level mechanism, not organ pathology.
**Database:** WormBase.

### 15.5 Human cellular / in vitro models

**SOX11⁺/⁻ isogenic human embryonic stem cells (the best human-relevant model):**
> **[VERBATIM — PMID:31035284]** "we describe the generation of *SOX11*+/- heterozygous human embryonic stem cell (hESC) lines by CRISPR/Cas9 genome engineering. *SOX11* haploinsufficiency impaired the generation of neurons and resulted in a proliferation/differentiation imbalance of neural precursor cells and enhanced neuronal cell death. Using the *SOX11*+/- hESC model we provide for the first time experimental evidence that *SOX11* haploinsufficiency is sufficient to impair key processes of human neurodevelopment, giving a first insight into the pathophysiology of CSSLS and *SOX11* function in human neurodevelopment."

**Strengths:** correct species, **correct zygosity (heterozygous — matching human disease)**, isogenic control. The single most translationally valid model available.
**Limitations:** 2D culture; no circuit-level, behavioural, or systemic readout; does not model non-neural organs.

**Other cellular systems:**
- **HeLa / HEK293T transient transfection + *GDF5*-promoter luciferase** — the standard *SOX11* variant functional assay across three labs (PMID:26543203, 35341651, 35938035). Method detail: *GDF5* promoter −448/+319 (NM_000557.3, GRCh37/hg19) in pGL3-basic; p3xFLAG-CMV-14 SOX11 expression construct; pRL-SV40 internal control; PicaGene Dual Sea Pansy; significance threshold P<.016 (Bonferroni for 3 comparisons); anti-FLAG M2 HRP immunoblot for protein-level confirmation. **This is a directly implementable assay for VUS reclassification.**
- **GT1-1 immortalised GnRH neurons** — SOX11 knockdown reduces *GNRH1* expression and GnRH secretion (PMID:21527504).
- **iPSC-derived GnRH neurons (GNRH1-TdTomato reporter)** — *SOX11* was **not** enriched (Lund et al., *Dis Model Mech* 2020;13(3):dmm040105) — a **negative human result** that conflicts with the mouse GnRH-neuron data. Curate as a `HUMAN_MODEL_MISMATCH`.
- **Human fetal tissue RNAscope ISH** — Carnegie stages 20, 21, 23 (§7.5). Not a "model" but the key human spatial-expression evidence.
- **Morphogen-guided neocortical organoids** — an emerging platform for NDD modelling (PMID:40950130, bioRxiv 2025, preprint).

### 15.6 Induced (non-genetic) models

**None relevant.** No drug-induced, surgical, or environmental-manipulation model of *SOX11* syndrome exists (consistent with the absence of any environmental aetiology).

### 15.7 Research applications and resources

| Application | Best model |
|---|---|
| Human neurodevelopmental mechanism at correct dosage | SOX11⁺/⁻ hESC |
| VUS functional classification | *GDF5* luciferase (HeLa/HEK293T) + zebrafish mRNA rescue |
| Ocular malformation / Hedgehog mechanism | Zebrafish (cyclopamine-rescuable) |
| Microcephaly quantification | Xenopus MO; *sox11a* zebrafish |
| Craniofacial / cleft palate mechanism | Mouse (FGF9/Cyclin D1 axis) |
| Renal / CAKUT mechanism | Mouse (*Gdnf*, PCDHB LCR) |
| Adult neurogenesis | Mouse conditional KO (Cre-loxP) |
| Hearing / cochlear nerve | Heterozygous mouse KO |
| GnRH/pituitary axis | GT1-1 cells; mouse pituitary scRNA-seq; **human iPSC-GnRH neurons give a discordant result** |
| Protein-level mechanism (LoF vs dominant-negative) | *C. elegans sem-2[Y160C]* |
| Post-translational regulation | Mouse cortex + hippocampus (USP11, PKA-S133, S30) |

**Model databases:** MGI (MGI:98359), IMPC (untested), IMSR/KOMP/EuMMCR/EMMA/MMRRC (allele sourcing), ZFIN, Xenbase, WormBase, Alliance of Genome Resources, Cellosaurus (for the SOX11⁺/⁻ hESC lines — deposit status not confirmed).

---

## Appendix A — Recommended dismech curation priorities

1. **`disease_term`: MONDO:0100626** (not MONDO:0014376 — see §1.2). Put MONDO:0014376 + OMIM:615866 in `mappings`.
2. **Model the SOX11↔BAF relationship explicitly** — germline: *SOX11* is downstream of PAX6–BAF; somatic (neuroblastoma): *SOX11* is upstream of SWI/SNF. This bidirectionality is the reason for the CSS9 misnomer and merits a `notes:` treatment.
3. **Curate the episignature as a diagnostic biomarker**, not as a mechanism. 224 DMPs, global hypomethylation, 10 cases vs 50 controls, MVP score.
4. **Consider `conforms_to` against existing modules** — candidate matches worth evaluating:
   - `pharyngeal_arch_patterning_serial_homology` — the cleft palate + mandibular hypoplasia + microtia + external/inner ear bundle is a **plausible but non-canonical** fit: the mouse mechanism (Cyclin D1/FGF9 mesenchymal proliferation → mandibular hypoplasia → tongue obstruction → cleft) is a *proliferation-and-obstruction* mechanism, **not** the module's neural-crest arch-identity or ribosomopathy mechanism. Evaluate carefully before asserting conformance.
   - `sensorineural_hair_cell_loss` — **likely a poor fit.** *SOX11* SNHL arises from **cochlear nerve** aplasia with a *structurally normal cochlea*, i.e. a retrocochlear/neural lesion, not hair-cell mechanotransduction failure. Prefer a disorder-specific node.
   - `renal_cystogenesis` — **not a fit.** *SOX11* causes duplex/malpositioned kidney (CAKUT branching defects), not cAMP-driven tubular cystogenesis.
   - No existing module covers "hypogonadotropic hypogonadism as a final common pathway." Given that HH recurs across *SOX2*, *SOX10*, *CHD7*, *FGFR1*, *ANOS1*, and now *SOX11*, **a new `hypogonadotropic_hypogonadism_gnrh_axis` module is a genuinely well-motivated proposal** — but that is a separate PR, not part of this entry.
5. **Record three `HUMAN_MODEL_MISMATCH` discussions** (not generic `KNOWLEDGE_GAP` — evidence exists but translational validity is the open question):
   - *Sox11*-null mouse cardiac OFT lethality and asplenia/visceral hypoplasia are absent in human heterozygotes (zygosity mismatch).
   - SOX11 is enriched in mouse hypothalamic GnRH neurons and stimulates GnRH in vitro, but was **not enriched** in human iPSC-derived GnRH neurons — leaving the human hypothalamic mechanism unresolved.
   - Zebrafish *sox11a*/*sox11b* paralogy means homozygous fish mutants model a dosage state with no human equivalent.
6. **Record `KNOWLEDGE_GAP` discussions for:** no prevalence estimate; no natural-history study; no QoL instrument; no clinical trial; no prognostic biomarker; in-vitro transactivation does not predict clinical severity (p.Ala176Glu paradox); no non-coding/regulatory *SOX11* variants reported despite a documented super-enhancer landscape; adult natural history unknown.
7. **Do not import from Coffin-Siris syndrome:** the *ARID1A* AFP/hepatoblastoma surveillance; ORPHA:1465 prevalence figures; "coarse facies" as a core feature.
8. **Verify every ontology ID in this report with OAK before committing** — and specifically do NOT use HP:0013272 (see discrepancy D1).
9. **Fetch and validate every PMID:** run `just fetch-reference PMID:XXXX` then `just validate-references`. **[PARAPHRASE]**-marked content must not be used as a snippet.

## Appendix B — Master citation list

| PMID | Citation | Type |
|---|---|---|
| 35341651 | Al-Jawahiri R, Foroutan A, Kerkhof J, et al. *SOX11* variants cause a neurodevelopmental disorder with infrequent ocular malformations and hypogonadotropic hypogonadism and with distinct DNA methylation profile. **Genet Med** 2022;24(6):1261–1273. DOI 10.1016/j.gim.2022.02.013 (CC BY 4.0) | **Landmark cohort — HUMAN_CLINICAL** |
| 24886874 | Tsurusaki Y, Koshimizu E, Ohashi H, et al. De novo *SOX11* mutations cause Coffin-Siris syndrome. **Nat Commun** 2014;5:5011. DOI 10.1038/ncomms5011 | First report — HUMAN_CLINICAL + MODEL_ORGANISM |
| 26543203 | Hempel A, Pagnamenta AT, Blyth M, et al. Deletions and de novo mutations of *SOX11* are associated with a neurodevelopmental disorder with features of Coffin-Siris syndrome. **J Med Genet** 2016;53(3):152–162. DOI 10.1136/jmedgenet-2015-103393 | Second cohort — HUMAN_CLINICAL + MODEL_ORGANISM |
| 37558216 | Pasquetti M, et al. Pathogenic variants in *SOX11* mimicking Pitt-Hopkins syndrome phenotype. **Clin Genet** 2024. DOI 10.1111/cge.14414 | Nosology/DDx; 82-case tally — HUMAN_CLINICAL |
| 39290158 | Sun B, Stamou MI, Stockman SL, et al. Expanding the Spectrum of Endocrine Abnormalities Associated With *SOX11*-related Disorders. **J Clin Endocrinol Metab** 2025. DOI 10.1210/clinem/dgae620 | Endocrine (1,810 IHH probands) — HUMAN_CLINICAL |
| 42168980 | Chu S, Yuan X, Niu Q, Gu W. A de novo *SOX11* mutation causing hypogonadotropic hypogonadism: a case report and literature review. **BMC Pediatr** 2026. DOI 10.1186/s12887-026-06974-5 | HH review (n=33); "SOX11-related disorder" framework — HUMAN_CLINICAL |
| 37924570 | Al-Jawahiri R, Stokes L, Smith H, McNeill A, Freeth M. Short report: Behavioural characterisation of *SOX11* syndrome. **Res Dev Disabil** 2023. DOI 10.1016/j.ridd.2023.104623 | Behavioural phenotype (n=21) — HUMAN_CLINICAL |
| 39333428 | Schincariol-Manhe B, Campagnolo É, Spineli-Silva S, et al. Novel variants in the *SOX11* gene: clinical description of seven new patients. **Eur J Hum Genet** 2024. DOI 10.1038/s41431-024-01695-8 | HUMAN_CLINICAL |
| 35938035 | Identification and functional analysis of novel *SOX11* variants in Chinese patients with Coffin-Siris syndrome 9. **Front Genet** 2022. DOI 10.3389/fgene.2022.940776 | HUMAN_CLINICAL + IN_VITRO |
| 33785884 | Hanker B, Gillessen-Kaesbach G, Hüning I, Lüdecke HJ, Wieczorek D. Maternal transmission of a mild Coffin-Siris syndrome phenotype caused by a *SOX11* missense variant. **Eur J Hum Genet** 2022;30:126–132. DOI 10.1038/s41431-021-00865-2 | Inheritance/expressivity — HUMAN_CLINICAL |
| 36369738 | Wang Q, Wu J, Yang J, Huang S, Yuan Y, Dai P. Two *SOX11* variants cause Coffin-Siris syndrome with a new feature of sensorineural hearing loss. **Am J Med Genet A** 2023. DOI 10.1002/ajmg.a.63011 | HUMAN_CLINICAL |
| 35642566 | Alburaiky S, Taylor J, O'Grady G, et al. Cochlear nerve deficiency in *SOX11*-related Coffin-Siris syndrome. **Am J Med Genet A** 2022. DOI 10.1002/ajmg.a.62851 | HUMAN_CLINICAL + MODEL_ORGANISM |
| 38591849 | Wu R, Tang W, Li P, Meng Z, Li X, Liang L. Identification of a novel phenotype of external ear deformity related to Coffin-Siris syndrome-9 and literature review. **Am J Med Genet A** 2024. DOI 10.1002/ajmg.a.63626 | Genotype-phenotype (56 variants) — HUMAN_CLINICAL |
| 40933692 | Case Report: Observation of early-onset high myopia with fundus tessellation changes in Coffin-Siris syndrome 9 (CSS9) and literature review. **Front Pediatr** 2025. DOI 10.3389/fped.2025.1603863 | Ophthalmological spectrum (58 cases) — HUMAN_CLINICAL |
| 29437512 | Khan U, DDD Study, Baker E, Clayton-Smith J. Observation of Cleft Palate in an Individual with *SOX11* Mutation. **Cleft Palate Craniofac J** 2018;55(3):456–461. DOI 10.1177/1055665617739312 | HUMAN_CLINICAL |
| 28787104 | Okamoto N, Ehara E, Tsurusaki Y, Miyake N, Matsumoto N. Coffin-Siris syndrome and cardiac anomaly with a novel *SOX11* mutation. **Congenit Anom (Kyoto)** 2018;58(3):105–107. DOI 10.1111/cga.12242 | HUMAN_CLINICAL |
| 42015706 | Wang Y, Wang Z. A case of Berry syndrome associated with *SOX11*-related Coffin-Siris syndrome type 9. **Zhongguo Dang Dai Er Ke Za Zhi** 2026;28(4):493–497 | HUMAN_CLINICAL |
| 39501269 | A rare Coffin-Siris syndrome induced by *SOX11*: a de novo nonsense variant of short stature. **BMC Med Genomics** 2024. DOI 10.1186/s12920-024-02036-w | HUMAN_CLINICAL |
| 18992374 | Lo-Castro A, et al. Deletion 2p25.2: a cryptic chromosome abnormality in a patient with autism and mental retardation detected using aCGH. **Eur J Med Genet** 2009 | Index deletion — HUMAN_CLINICAL |
| 35126043 | Vasko A, Schrier Vergano SA. Language Impairments in Individuals With Coffin-Siris Syndrome. **Front Neurosci** 2022. DOI 10.3389/fnins.2021.802583 | Registry (n=284, 10 *SOX11*) — HUMAN_CLINICAL |
| 38117302 | Delineation of the adult phenotype of Coffin-Siris syndrome in 35 individuals. **Hum Genet** 2024. DOI 10.1007/s00439-023-02622-5 | Adult outcome — HUMAN_CLINICAL |
| 23556151 | Schrier Vergano S, et al. Coffin-Siris Syndrome. **GeneReviews®** 2013 (updated) | Management/surveillance |
| 34205270 | Genotype-Phenotype Correlations in 208 Individuals with Coffin-Siris Syndrome. **Genes (Basel)** 2021 | HUMAN_CLINICAL |
| 31530938 | Genetic abnormalities in a large cohort of Coffin-Siris syndrome patients. **J Hum Genet** 2019 | HUMAN_CLINICAL |
| 30123105 | Bögershausen N, Wollnik B. Mutational Landscapes and Phenotypic Spectrum of SWI/SNF-Related Intellectual Disability Disorders. **Front Mol Neurosci** 2018 | Review |
| 31035284 | Turan S, Boerstler T, Kavyanifar A, et al. A novel human stem cell model for Coffin-Siris syndrome-like syndrome reveals the importance of *SOX11* dosage. **Hum Mol Genet** 2019. DOI 10.1093/hmg/ddz089 | **IN_VITRO — key human model** |
| 15254231 | Sock E, Rettig SD, Enderich J, Bösl MR, Tamm ER, Wegner M. Gene targeting reveals a widespread role for the HMG transcription factor Sox11 in tissue remodeling. **Mol Cell Biol** 2004;24(15):6635–6644 | **MODEL_ORGANISM — founding mouse KO** |
| 23483698 | Wang Y, Lin L, Lai H, Parada LF, Lei L. Transcription factor Sox11 is essential for both embryonic and adult neurogenesis. **Dev Dyn** 2013;242:638–653 | MODEL_ORGANISM |
| 26826126 | Huang H, Yang X, Bao M, et al. Ablation of the Sox11 Gene Results in Clefting of the Secondary Palate Resembling the Pierre Robin Sequence. **J Biol Chem** 2016;291:7107–7118 | MODEL_ORGANISM |
| 29459093 | Neirijnck Y, Reginensi A, Renkema KY, et al. Sox11 gene disruption causes congenital anomalies of the kidney and urinary tract (CAKUT). **Kidney Int** 2018;93:1142–1153 | MODEL_ORGANISM + HUMAN_CLINICAL |
| 25010521 | Pillai-Kastoori L, Wen W, Wilson SG, et al. Sox11 is required to maintain proper levels of Hedgehog signaling during vertebrate ocular morphogenesis. **PLoS Genet** 2014;10(7):e1004491 | MODEL_ORGANISM + HUMAN_CLINICAL |
| 33061816 | Jia S, Wu X, Wu Y, Cui X, Tao B, Zhu Z, Hu W. Multiple Developmental Defects in *sox11a* Mutant Zebrafish with Features of Coffin-Siris Syndrome. **Int J Biol Sci** 2020. DOI 10.7150/ijbs.47510 | MODEL_ORGANISM |
| 40832700 | Baccas M, Liu J. A Coffin-Siris syndrome-associated mutation modeled in *Caenorhabditis elegans* affects multiple developmental processes. **G3** 2025. DOI 10.1093/g3journal/jkaf194 | MODEL_ORGANISM |
| 33579706 | Chiang SY, Wu HC, Lin SY, et al. Usp11 controls cortical neurogenesis and neuronal migration through Sox11 stabilization. **Sci Adv** 2021. DOI 10.1126/sciadv.abc6093 | MODEL_ORGANISM |
| 21527504 | Kim HD, Choe HK, Chung S, et al. Class-C SOX transcription factors control GnRH gene expression via the intronic transcriptional enhancer. **Mol Endocrinol** 2011;25(7):1184–1196 | IN_VITRO + MODEL_ORGANISM |
| 30385877 | Phosphorylation of the neurogenic transcription factor SOX11 on serine 133 modulates neuronal morphogenesis. **Sci Rep** 2018. DOI 10.1038/s41598-018-34480-x | IN_VITRO + MODEL_ORGANISM |
| 29973868 | Phosphorylation Modulates the Subcellular Localization of SOX11. **Front Mol Neurosci** 2018. DOI 10.3389/fnmol.2018.00211 | IN_VITRO |
| 31204298 | Polycomb Protein EED Regulates Neuronal Differentiation through Targeting SOX11 in Hippocampal Dentate Gyrus. **Stem Cell Reports** 2019 | MODEL_ORGANISM |
| 36882421 | Decaesteker B, Louwagie A, Loontiens S, et al. SOX11 regulates SWI/SNF complex components as member of the adrenergic neuroblastoma core regulatory circuitry. **Nat Commun** 2023;14:1267 | Cancer biology — **not germline NDD** |
| 29079881 | SoxC transcription factors: multifunctional regulators of neurodevelopment. **Cell Tissue Res** 2018 | Review |
| 32574812 | Regulatory roles for SOX11 in development, stem cells and cancer. **Semin Cancer Biol** 2020 | Review |
| 30661772 / 35232796 | *SOX4*-related NDD (AJHG 2019; J Med Genet 2022) | DDx / NEC risk |
| 39057025 | *SOX12* de novo variant with epilepsy and ID. **Curr Issues Mol Biol** 2024 | DDx |
| — | Ho Y, Hu P, Peel MT, et al. Single-cell transcriptomic analysis of adult mouse pituitary. **Protein Cell** 2020;11(8):565–583 | scRNA-seq gonadotrope SOX11 |
| — | Lund C, Yellapragada V, Vuoristo S, et al. Characterization of the human GnRH neuron developmental transcriptome using a *GNRH1*-TdTomato reporter line in human pluripotent stem cells. **Dis Model Mech** 2020;13(3):dmm040105 | **Negative human result** |
| — | ClinGen Dosage Sensitivity Curation, SOX11 (HI=3, TS=0), evaluated 2024-11-21 | Structured DB — `CGDS:HGNC_11191` |
| — | ClinGen Gene-Disease Validity, SOX11–MONDO:0100626, **Definitive** AD, Intellectual Disability and Autism GCEP, 2025-05-20 | Structured DB — `CGGV:` |

---

**Sources:**
[Al-Jawahiri 2022 — Genetics in Medicine](https://www.gimjournal.org/article/S1098-3600(22)00665-7/fulltext) · [Al-Jawahiri 2022 open-access PDF (White Rose)](https://eprints.whiterose.ac.uk/190170/) · [PubMed 35341651](https://pubmed.ncbi.nlm.nih.gov/35341651/) · [PubMed 24886874](https://pubmed.ncbi.nlm.nih.gov/24886874/) · [PubMed 26543203](https://pubmed.ncbi.nlm.nih.gov/26543203/) · [PubMed 37558216](https://pubmed.ncbi.nlm.nih.gov/37558216/) · [Pasquetti 2024 — Clinical Genetics](https://onlinelibrary.wiley.com/doi/10.1111/cge.14414) · [PubMed 39290158](https://pubmed.ncbi.nlm.nih.gov/39290158/) · [PubMed 42168980](https://pubmed.ncbi.nlm.nih.gov/42168980/) · [PubMed 37924570](https://pubmed.ncbi.nlm.nih.gov/37924570/) · [PubMed 39333428](https://pubmed.ncbi.nlm.nih.gov/39333428/) · [Chinese CSS9 functional analysis — PMC9354949](https://pmc.ncbi.nlm.nih.gov/articles/PMC9354949/) · [Frontiers in Genetics 2022](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2022.940776/full) · [PubMed 33785884](https://pubmed.ncbi.nlm.nih.gov/33785884/) · [PubMed 36369738](https://pubmed.ncbi.nlm.nih.gov/36369738/) · [PubMed 35642566](https://pubmed.ncbi.nlm.nih.gov/35642566/) · [PubMed 38591849](https://pubmed.ncbi.nlm.nih.gov/38591849/) · [CSS9 ophthalmology review — PMC12417530](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12417530/) · [PubMed 29437512](https://pubmed.ncbi.nlm.nih.gov/29437512/) · [PubMed 28787104](https://pubmed.ncbi.nlm.nih.gov/28787104/) · [PubMed 42015706](https://pubmed.ncbi.nlm.nih.gov/42015706/) · [PubMed 35126043](https://pubmed.ncbi.nlm.nih.gov/35126043/) · [Coffin-Siris genotype-phenotype 208 individuals — PMC8233770](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8233770/) · [Coffin-Siris Syndrome — GeneReviews](https://pubmed.ncbi.nlm.nih.gov/23556151/) · [PubMed 31035284](https://pubmed.ncbi.nlm.nih.gov/31035284/) · [PubMed 15254231](https://pubmed.ncbi.nlm.nih.gov/15254231/) · [PubMed 33061816](https://pubmed.ncbi.nlm.nih.gov/33061816/) · [PubMed 25010521](https://pubmed.ncbi.nlm.nih.gov/25010521/) · [Neirijnck 2018 — Kidney International](https://www.kidney-international.org/article/S0085-2538(17)30894-3/fulltext) · [PubMed 29459093](https://pubmed.ncbi.nlm.nih.gov/29459093/) · [PubMed 40832700](https://pubmed.ncbi.nlm.nih.gov/40832700/) · [PubMed 33579706](https://pubmed.ncbi.nlm.nih.gov/33579706/) · [PubMed 36882421](https://pubmed.ncbi.nlm.nih.gov/36882421/) · [Sox11 cleft palate — SAGE](https://journals.sagepub.com/doi/10.1177/1055665617739312) · [SoxC in development and cancer — PMC2862366](https://pmc.ncbi.nlm.nih.gov/articles/PMC2862366/) · [Cardiac outflow tract Sox4/Sox11 — Springer](https://link.springer.com/article/10.1007/s00018-013-1523-x) · [Sox12 deletion nonreciprocal redundancy — PMC2493363](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2493363/) · [SoxC overlapping expression — Nucleic Acids Research](https://academic.oup.com/nar/article/36/9/3101/1104839) · [OMIM 600898 — SOX11](https://omim.org/entry/600898) · [MedGen — Coffin-Siris syndrome 9](https://www.ncbi.nlm.nih.gov/medgen/?term=Coffin-Siris+syndrome+9) · [NCBI Gene 6664 — SOX11](https://www.ncbi.nlm.nih.gov/gene/6664) · [HGNC REST — SOX11](https://rest.genenames.org/fetch/symbol/SOX11) · [MONDO:0100626 via EBI OLS4](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0100626) · [MONDO:0014376 via EBI OLS4](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0014376) · [ClinGen SOX11 dosage sensitivity](https://search.clinicalgenome.org/kb/gene-dosage/SOX11) · [ClinGen SOX11 gene curations](https://search.clinicalgenome.org/kb/genes/HGNC:11191) · [HPO annotations for OMIM:615866](https://ontology.jax.org/api/network/annotation/OMIM:615866) · [MGI:98359 — mouse Sox11](https://www.informatics.jax.org/marker/MGI:98359) · [IMPC — Sox11](https://www.mousephenotype.org/data/genes/MGI:98359) · [gnomAD v4.0 gene constraint documentation](https://gnomad.broadinstitute.org/news/2024-03-gnomad-v4-0-gene-constraint/) · [SOX11 is a mantle cell lymphoma oncogene — Blood](https://ashpublications.org/blood/article/121/12/2169/31431/SOX11-is-a-mantle-cell-lymphoma-oncogene) · [SOX11:SMARCA4 complex in MCL — Blood Cancer Journal](https://www.nature.com/articles/s41408-025-01333-6) · [Adult Coffin-Siris phenotype (Europe PMC 38117302)](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:38117302&resultType=core&format=json)