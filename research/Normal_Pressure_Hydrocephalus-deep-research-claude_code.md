---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-22T00:05:22.225973'
end_time: '2026-08-22T00:09:42.579009'
duration_seconds: 260.35
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Normal Pressure Hydrocephalus
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 12
  num_turns: 14
  total_cost_usd: 1.2886006
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 32
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Normal Pressure Hydrocephalus
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Normal Pressure Hydrocephalus** covering all of the
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

# Normal Pressure Hydrocephalus: Comprehensive Research Report

## 1. Disease Information

**Overview.** Normal pressure hydrocephalus (NPH) is a chronic communicating hydrocephalus syndrome characterized by ventriculomegaly with cerebrospinal fluid (CSF) opening pressure that is normal or only mildly elevated (typically 80–200 mmH₂O) on lumbar puncture, occurring in the absence of papilledema. Clinically it presents with the classic **Hakim–Adams triad**: gait/balance disturbance (usually the earliest and most prominent feature — a broad-based, short-stepped, "magnetic" or shuffling gait), cognitive impairment (subcortical/frontal-executive pattern: psychomotor slowing, impaired attention and executive function, later memory involvement), and urinary dysfunction (urgency progressing to incontinence). Not all three features need be present, especially early in the disease course. NPH is classified as:
- **Idiopathic NPH (iNPH)** — no identifiable antecedent cause, typically affecting adults >60 years; the dominant form discussed in most modern literature.
- **Secondary NPH (sNPH)** — arising after a defined CNS insult (subarachnoid hemorrhage, meningitis, traumatic brain injury, intracranial hemorrhage, tumor, prior neurosurgery) that impairs CSF absorption at the arachnoid granulations, typically presenting at a younger age with a more clearly defined temporal relationship to the inciting event.

iNPH is potentially reversible with CSF diversion (shunt surgery), which distinguishes it clinically from most neurodegenerative dementias and motivates aggressive diagnostic pursuit in elderly patients presenting with gait decline and cognitive slowing (Rovira et al., *Neuroradiology* 2026, PMID:42239999; Johnson & Williams, *NEJM* 2025, DOI:10.1056/NEJMra2306506).

**Key identifiers:**
- **MONDO:** MONDO:0004909 (normal pressure hydrocephalus) — idiopathic and secondary forms have related but distinct MONDO terms in some releases; verify current mapping via OAK before curation.
- **OMIM:** No single-gene Mendelian OMIM phenotype entry exists for typical iNPH (multifactorial/complex trait); familial/genetic risk loci are catalogued separately (see §4).
- **Orphanet:** ORPHA:98644 (Idiopathic normal pressure hydrocephalus).
- **ICD-10-CM:** G91.2 (Idiopathic normal pressure hydrocephalus); G91.0 (Communicating hydrocephalus, used for some secondary/congenital forms); G91.1 (Obstructive hydrocephalus, distinct entity).
- **ICD-11:** 8A05.2 or the hydrocephalus stem code in the "Diseases of the nervous system" chapter (verify exact code at curation time).
- **MeSH:** D065886 (Hydrocephalus, Normal Pressure).
- **HPO (as a phenotype, for use when NPH itself is an HPO-coded feature of another disease):** HP:0007099 (Normal pressure hydrocephalus, if present in the current HPO release) or component terms (see §3).

**Synonyms:** Hakim–Adams syndrome; Hakim syndrome; occult hydrocephalus; normotensive hydrocephalus; chronic communicating hydrocephalus of adults; symptomatic hydrocephalus with normal CSF pressure.

**Evidence basis.** The literature on NPH derives from a mix of individual case series/cohorts (single- and multi-center surgical outcome studies), national registry/claims analyses (e.g., the German Federal Statistical Office database), large population-based epidemiological cohorts (e.g., the Western Sweden population study), and a national biobank-linked GWAS (FinnGen). This is a disease where aggregated registry/claims data substantially undercount true prevalence because of underdiagnosis (see §9), so population-based neuroimaging screening cohorts are considered more authoritative for prevalence than administrative coding data (PMC10661316).

---

## 2. Etiology

### Disease Causal Factors
iNPH's root cause remains **incompletely defined and is considered multifactorial**, converging on a final common pathway of disturbed CSF dynamics, reduced intracranial compliance, and impaired glymphatic clearance (see §6). Proposed contributing mechanisms include:
- **Altered CSF hydrodynamics** — a shift in balance between CSF pulsatile bulk flow, reduced ventricular compliance and cerebral arterial pulsatility transmission to periventricular tissue.
- **Impaired CSF absorption/outflow resistance** — increased resistance to CSF outflow (Rout) at the arachnoid granulations and along perivascular/glymphatic-lymphatic exit routes.
- **Glymphatic-lymphatic clearance failure** — reduced perivascular AQP4-dependent CSF-interstitial fluid exchange, causing solute/metabolite accumulation (see §6 and the glymphatic scoping review, *J Neurosurg* 2025, DOI:10.3171/2024.12.JNS2420).
- **Cerebrovascular/small-vessel pathology** — chronic vascular risk factor burden producing periventricular ischemia and reduced vascular/venous compliance.

sNPH has an unambiguous causal chain: an antecedent insult (SAH, meningitis, trauma, tumor, intraventricular hemorrhage) triggers subarachnoid space fibrosis/inflammation, obliterating arachnoid granulation CSF absorption pathways.

### Risk Factors

**Genetic risk factors** (see §4 for detail): copy-number loss in *SFMBT1*; missense/loss-of-function variants in cilia-related genes (*CFAP43*, *DNAH14*); *CWH43* variants; and, per the 2024 FinnGen GWAS, 6 genome-wide significant loci near genes implicated in blood–brain-barrier/blood–CSF-barrier function (Kaprio et al./Jyrkkänen et al., *Neurology* 2024, PMID:39141892). A positive family history and possible autosomal-dominant-like clustering has been described in some kindreds, though iNPH is predominantly sporadic/complex.

**Environmental/demographic risk factors:**
- **Age** — the single strongest risk factor; incidence and prevalence rise steeply after age 65–70 and again after 80 (PMC11666604).
- **Vascular risk factor burden** — hypertension (described as "perhaps the most important" modifiable VRF), diabetes mellitus (OR ≈2.17), hyperlipidemia (OR ≈2.38), obesity (OR ≈5.43), and psychosocial stress factors (OR ≈5.34) were each independently associated with iNPH in the INPH-CRasH case-control study; the authors estimate that up to ~25% of iNPH cases may be attributable to modifiable vascular risk factors (PMID:28062721; PMC5304464). A subsequent Mendelian randomization study (*J Neurol* 2023, DOI:10.1007/s00415-023-11604-6) examined the causal relationship between vascular risk factors and iNPH.
- **Cerebral small vessel disease / white matter hyperintensity burden** — frequently comorbid, sharing risk factors with iNPH (hypertension, diabetes, hyperlipidemia, smoking).
- **Prior neurosurgical/CNS insult** — for sNPH specifically: subarachnoid hemorrhage (most common precipitant), bacterial/tuberculous/rheumatoid meningitis, traumatic brain injury, intracerebral/intraventricular hemorrhage, posterior fossa or intraventricular tumors, and prior cranial surgery.
- **Diabetes/obesity/metabolic syndrome** as above.
- **Male sex** — some but not all cohorts report a modest male predominance among iNPH cases.

**Protective factors:** No robust genetic protective variants or alleles have been established for NPH. Management of modifiable vascular risk factors (blood pressure control, glycemic control, weight management) is proposed as a plausible protective/preventive strategy given the vascular risk factor association data, though this remains largely inferential rather than proven by interventional trials.

**Gene–environment interactions:** Not well characterized for iNPH specifically; the cilia/choroid-plexus/ependymal gene signal (SFMBT1, CFAP43, DNAH14) plausibly interacts with vascular and CSF-outflow environmental stressors to determine whether ventriculomegaly and clinical symptoms manifest, but formal GxE studies are lacking.

---

## 3. Phenotypes

### Core Triad (symptoms/clinical signs)

| Phenotype | HPO term (suggested) | Onset/course | Frequency |
|---|---|---|---|
| Gait disturbance (broad-based, magnetic, shuffling, short-stepped) | HP:0002317 (Unsteady gait) / HP:0002378 (Difficulty walking) / HP:0002355 (Difficulty walking, more specific gait terms as available: HP:0031936 Delayed gait or HP:0100269 Cerebellar-type gait not appropriate — best fit HP:0002317 or a magnetic-gait-specific descendant if present) | Typically the first and most consistent symptom; insidious onset, chronic progressive | Most frequent triad component (~90%+ of diagnosed cases have gait involvement) |
| Cognitive impairment (subcortical-frontal pattern: bradyphrenia, impaired executive function, attention, psychomotor slowing; memory relatively preserved early) | HP:0100543 (Cognitive impairment) / HP:0002354 (Memory impairment) / HP:0000733 (Psychomotor slowing, if coded) | Insidious, progressive; may precede or follow gait symptoms | Common (~60–80% of diagnosed cases) |
| Urinary dysfunction (urgency, frequency, progressing to urge incontinence) | HP:0000012 (Urinary incontinence) / HP:0100519 (Urinary urgency) / HP:0100515 (Urinary urgency, alt) | Typically the last of the triad to appear; progressive | Less consistently present (~50–75%) |

Additional recognized phenotypes:
- **Neuropsychiatric features** — apathy, depression, and less commonly psychosis, are increasingly recognized (systematic review/meta-analysis, PMC12879024). Suggested HPO: HP:0000739 (Anxiety), HP:0000723 (Restlessness), HP:0000741 (Apathy, if present in current HPO), HP:0000716 (Depression).
- **Falls** — a frequent and clinically significant consequence of the gait disorder. HPO: HP:0002527 (Falls).
- **Postural instability** — HP:0002172.

### Phenotype Characteristics
- **Age of onset:** Adult-onset, overwhelmingly ≥60 years for iNPH (diagnostic criteria commonly require age >60); sNPH can occur at any age depending on the inciting event.
- **Severity:** Variable; graded clinically with instruments such as the iNPH Grading Scale (iNPHGS) and modified Rankin Scale (mRS).
- **Progression:** Classically insidious and slowly progressive over months to years if untreated; can plateau or, less commonly, progress more rapidly. Some component symptoms (especially gait) are reported to show partial/complete reversibility after shunting if intervention occurs before irreversible axonal/white-matter injury sets in.
- **Frequency among affected individuals:** Gait disturbance is near-universal at diagnosis; the full triad is present in a minority at initial presentation, with many patients evolving to the complete triad over time.

### Quality of Life Impact
Gait impairment and falls are major drivers of loss of independence, institutionalization risk, and caregiver burden. Cognitive impairment compounds functional decline and can be misattributed to "normal aging" or another dementia, delaying diagnosis. Urinary incontinence carries substantial psychosocial and QoL impact and is an independent predictor of nursing-home placement. Long-term shunting studies report sustained QoL improvement in shunt responders (PMID:37004132, "The impact of cerebrospinal fluid shunting on quality of life in idiopathic normal pressure hydrocephalus: a long-term analysis").

---

## 4. Genetic/Molecular Information

iNPH is best understood as a **complex, multifactorial trait** rather than a single-gene Mendelian disorder, though several candidate genes and one genome-wide significant locus set have emerged.

**Causal/candidate genes:**
- ***SFMBT1*** (chromosome 3p21) — a segmental copy-number loss within intron 2 was found in **26.0% of shunt-responsive definite iNPH patients** vs 4.2% of healthy elderly controls and 6.3% of Parkinson's disease patients in a Japanese case-control study, and replicated in Finnish and Norwegian cohorts (Kato et al., *PLOS ONE* 2016, PMID via PMC5115754). SFMBT1 protein localizes to arterial walls, ependymal cells, and choroid plexus epithelium — tissues directly involved in CSF secretion, flow, and absorption.
- ***CFAP43*** — a nonsense mutation was identified in one family with NPH and ciliary abnormalities, implicating ependymal ciliary dysfunction in impaired CSF flow/mixing.
- ***DNAH14*** — another cilia-associated gene reported among candidate NPH-associated loci.
- ***CWH43*** — variants associated with both disease risk and clinical phenotypic severity measures in NPH patients (*Neurology Genetics*, DOI:10.1212/NXG.0000000000200086).
- **2024 FinnGen GWAS** (Jyrkkänen et al., *Neurology* 2024, PMID:39141892) — the largest GWAS in chronic hydrocephalus to date (473,691 Finns with genotype and nationwide health-record linkage), identifying **6 genome-wide significant loci** associated with NPH, with genes near the top loci previously implicated in blood–brain-barrier and blood–CSF-barrier function — supporting a barrier-integrity mechanism distinct from purely mechanical CSF-flow obstruction.

**Gene-level pattern:** Multiple implicated genes (SFMBT1, DNAH14, CFAP43, CWH43) are highly expressed in choroid plexus and ependymal cells, and several are linked to **ciliary function** — a convergent theme suggesting impaired ependymal ciliary beating/CSF flow-mixing as a contributing mechanism, analogous to mechanisms in congenital hydrocephalus and primary ciliary dyskinesia (Piccinin et al., "Genetic Risk Factors in Normal Pressure Hydrocephalus," *Movement Disorders* 2025, PMID:40266017; review in *J Neurosurg* 2024, DOI:10.3171/... "Genetics and molecular pathophysiology of normal pressure hydrocephalus").

**Variant classification / population frequency:** No ClinVar-curated pathogenic/likely-pathogenic variant set exists comparable to monogenic disease; SFMBT1 copy-number loss frequency in general elderly populations (~4–6%) versus iNPH cases (~26%) suggests it functions as a **susceptibility/risk allele** rather than a fully penetrant causal variant — appropriate `relationship_type: SUSCEPTIBILITY` in dismech terms, with `HP:0010982`-style polygenic/complex inheritance framing rather than classic Mendelian inheritance.

**Somatic vs. germline:** All reported variants are germline; no somatic mosaicism data reported for iNPH.

**Epigenetics / chromosomal abnormalities:** No systematic epigenome-wide association study or chromosomal-abnormality series specific to iNPH was identified in current literature; this remains an evidence gap.

**Functional consequence:** The SFMBT1/CFAP43/DNAH14/CWH43 gene set suggests a mechanism of **partial loss of function** in genes governing choroid plexus/ependymal barrier integrity and ciliary CSF propulsion, predisposing to the CSF-dynamics disturbance that culminates in ventriculomegaly — a **susceptibility/modifier** rather than sole-causal genetic architecture, consistent with the multifactorial (vascular + genetic + glymphatic) model.

---

## 5. Environmental Information

- **Vascular/metabolic environmental exposures:** hypertension, diabetes, hyperlipidemia, obesity — see §2 for effect sizes (INPH-CRasH study).
- **Psychosocial stress factors:** independently associated with iNPH risk in case-control analysis (OR ≈5.3), though the mechanism is unclear and may reflect confounding or reverse causation.
- **Infectious agents:** Bacterial meningitis, tuberculous meningitis, and rheumatoid/aseptic meningitis are established precipitants of **secondary** NPH via arachnoiditis/fibrosis of the CSF absorptive pathways (case report of rheumatoid meningitis-associated secondary NPH, PMC8299371). Meningoencephalitis accounted for ~5% of cases in a large secondary-NPH case review (n=1,208 cases).
- **Trauma/hemorrhage exposures:** subarachnoid hemorrhage (the best-studied precipitant of sNPH, with shunt-dependent hydrocephalus complicating a substantial minority of aneurysmal SAH survivors — see PMC11319414 systematic review/meta-analysis of risk factors for shunt-dependent hydrocephalus after SAH), traumatic brain injury, and intraventricular/intracerebral hemorrhage.
- **Iatrogenic exposures:** prior cranial neurosurgery (tumor resection, posterior fossa surgery) is a recognized precipitant of secondary NPH.
- No specific occupational toxin, pollutant, or dietary exposure has been robustly linked to iNPH risk; nutritional/lifestyle risk factor data remain limited and largely inferential (see the *Nutritional and Lifestyle Risk Factors* chapter, ScienceDirect B9780124078246000100).

---

## 6. Mechanism / Pathophysiology

The pathophysiology of iNPH is best framed as a **convergence of three interacting mechanistic axes**: (1) disturbed CSF hydrodynamics/compliance, (2) glymphatic-lymphatic clearance failure, and (3) periventricular vascular/ischemic injury — culminating in white matter and cortical dysfunction.

### Causal chain (upstream → downstream)
1. **Trigger/predisposition:** genetic susceptibility (choroid plexus/ependymal ciliary and barrier genes) + vascular risk factor burden + (for sNPH) an antecedent CNS insult causing arachnoid granulation fibrosis.
2. **CSF outflow resistance increases** and/or ventricular/vascular compliance is reduced — normal pulsatile arterial-driven CSF/interstitial fluid exchange is impaired.
3. **Glymphatic-lymphatic clearance dysfunction:** AQP4 water channels on perivascular astrocytic endfeet, which normally drive convective glymphatic CSF-ISF exchange, show **reduced expression and perivascular mislocalization**, together with **reactive perivascular astrogliosis**, in iNPH brain tissue and CSF studies (glymphatic scoping review, *J Neurosurg* 2025, DOI:10.3171/2024.12.JNS2420; AQP4 CSF evaluation study, PMC8486078).
4. **Impaired clearance of interstitial waste/metabolites** (including amyloid-beta and other neurotoxic solutes) accumulates in periventricular white matter and CSF.
5. **Ventricular enlargement** develops as CSF preferentially expands the low-resistance ventricular compartment, producing periventricular white-matter stretch injury, transependymal CSF flow, and periventricular ischemia from compression of penetrating medullary arterioles.
6. **Downstream clinical manifestation:** disruption of periventricular white matter tracts serving frontal-subcortical circuits (corticospinal tracts controlling gait, frontal-executive circuits, and pontine/periventricular pathways involved in bladder control) produces the gait–cognition–urinary triad.

### Molecular/cellular detail
- **Molecular pathways:** Disturbed AQP4-dependent glymphatic convective flow (analogous mechanistically to the `glymphatic_dysfunction` module framework used for Alzheimer's disease — perivascular AQP4 depolarization/mislocalization reducing periarterial CSF influx and paravenous efflux).
- **Cellular processes:** reactive astrogliosis (elevated CSF YKL-40/chitinase-3-like protein 1, a marker of activated astrocytes, is significantly higher in CSF tap-test **non-responders** than responders — PMC11399724), ependymal ciliary dysfunction, and choroid plexus epithelial dysfunction (impacting CSF secretion).
- **Protein dysfunction:** AQP4 mislocalization from perivascular endfeet to a more diffuse astrocytic membrane distribution — a functional redistribution rather than a loss-of-expression phenomenon in most studies, though net reduction has also been reported.
- **Tissue damage mechanisms:** periventricular ischemia from compression/stretch of penetrating arterioles; chronic mechanical stretch injury to periventricular white matter (corpus callosum, corona radiata); transependymal CSF absorption causing periventricular white matter edema/gliosis (visible as periventricular hyperintensity on MRI).
- **Biochemical/CSF proteomic abnormalities:** Unbiased CSF proteomics (Neurology, DOI:10.1212/WNL.0000000000213375) identified **decreases in numerous CSF proteins** in iNPH consistent with impaired efflux from interstitial fluid into CSF — a proteomic signature directly supporting the glymphatic-failure model. Elevated leucine-rich alpha-2-glycoprotein (LRG) and decreased classic Alzheimer's-type biomarkers have also been reported (PMC7961420).
- **Immune involvement:** chronic low-grade neuroinflammation and reactive astrogliosis (YKL-40) rather than primary autoimmunity, except in secondary NPH caused by inflammatory/autoimmune meningitis (e.g., rheumatoid meningitis).

### Molecular profiling
- **CSF proteomics:** decreased protein efflux signature (2024 Neurology study above).
- **Neuroimaging-correlate "omics":** DESH (disproportionately enlarged subarachnoid space hydrocephalus) pattern reflects regional CSF compliance mismatch — tight high-convexity/medial subarachnoid spaces with enlarged Sylvian fissures and ventricles — used increasingly as a structural/morphometric biomarker (see §10).
- Single-cell/spatial transcriptomic and multi-omic data specific to human iNPH brain tissue remain sparse; most molecular-mechanism data derive from CSF biomarker studies and animal models rather than human single-cell atlases.

### Suggested ontology terms
- **GO (biological process):** GO:0007420 (brain development, upstream context), GO:0003094 (glomerular filtration analogy not applicable); more precisely: GO:0055082 (cellular chemical homeostasis), GO:0072488 (ammonium transmembrane transport, N/A); best fits: **GO:0007605** (N/A), and specifically **GO:0035378** (carbon dioxide transmembrane transport via aquaporin channel), **GO:0003094** not relevant — most precise GO terms are **GO:0035378** and **GO:0006833** (water transport), plus **GO:0050893** (sensory processing, N/A). Recommend: GO:0006833 (water transport, AQP4 function), GO:0007420 (brain development — ependymal/ciliary genes), GO:0003341 (cilium movement, for ependymal ciliary dysfunction), GO:0034976 (response to endoplasmic reticulum stress, N/A).
- **GO (cellular component):** GO:0016327 (apicolateral plasma membrane, astrocyte endfeet context), GO:0043209 (myelin sheath, periventricular white matter injury), GO:0005929 (cilium, ependymal).
- **CL (cell types):** CL:0000127 (astrocyte), CL:0000067 (ciliated cell), CL:1001602 (choroid plexus epithelial cell) or CL:0000710 (choroid plexus cell), CL:0011005 (ependymal cell / GO alt CL:0000065 ependymal cell).
- **CHEBI:** CHEBI:15377 (water, AQP4 substrate); CHEBI:81571 (amyloid beta, comorbid pathology context).

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary: brain (ventricular system, periventricular white matter, subarachnoid space).
- Secondary/complications: bladder (neurogenic urinary dysfunction), musculoskeletal system (falls-related injury), and — after shunt placement — abdominal peritoneal cavity (site of distal shunt catheter and occasional complications).
- Body systems: nervous system (primary), genitourinary system (secondary), musculoskeletal system (secondary, gait/falls).

**Tissue/cell level:**
- Ventricular ependyma (CL:0000065 ependymal cell) — ciliary dysfunction.
- Choroid plexus epithelium (CL:1001602 / choroid plexus epithelial cell) — CSF secretion.
- Perivascular astrocytes (CL:0000127 astrocyte) — AQP4-mediated glymphatic function.
- Periventricular white matter oligodendrocytes/axons (CL:0000128 oligodendrocyte) — stretch/ischemic injury.
- Arachnoid granulation cells — CSF absorption (particularly relevant to secondary NPH fibrosis).

**Subcellular level:**
- Astrocytic endfeet plasma membrane — AQP4 water channel localization (GO:0043195 terminal bouton not applicable; better: GO:0097449 astrocyte projection).
- Ependymal cell cilia (GO:0005929 cilium).
- Perivascular (Virchow-Robin) space — the anatomical conduit for glymphatic CSF-ISF exchange.

**Localization (UBERON terms):**
- UBERON:0002037 (cerebellum, N/A unless cerebellar involvement noted); primary relevant terms: **UBERON:0002450** (lateral ventricle), **UBERON:0002316** (white matter of cerebrum / periventricular white matter), **UBERON:0002078** (right cerebral hemisphere, bilateral involvement typical), **UBERON:0002298** (brainstem, less directly involved), **UBERON:0001893** (cerebral cortex — frontal-subcortical circuit disruption), **UBERON:0000955** (brain, general), **UBERON:0002037** for cerebellum not primary. Also **UBERON:0035328** (subarachnoid space) and **UBERON:0002440** (choroid plexus).
- Lateralization: bilateral and symmetric ventriculomegaly is typical of iNPH; asymmetric ventriculomegaly should prompt consideration of secondary/obstructive causes.

---

## 8. Temporal Development

- **Onset:** Adult-onset, insidious, typically ≥60 years for iNPH (diagnostic criteria commonly specify age >60); sNPH onset is anchored to the timing of the antecedent insult (days to years post-SAH/meningitis/trauma), with shunt-dependent hydrocephalus after SAH often manifesting within the first weeks to months.
- **Onset pattern:** Chronic/insidious for iNPH; can be subacute for some secondary forms (post-hemorrhagic).
- **Progression:** Slowly progressive without treatment; gait disturbance often progresses first and most reliably, with cognitive and urinary symptoms accruing over months to a few years. Disease duration prior to diagnosis is frequently prolonged (often years), contributing to underdiagnosis (§9).
- **Disease course pattern:** Generally progressive rather than relapsing-remitting; no well-described spontaneous remission pattern, though very slow plateaus are reported.
- **Reversibility:** A defining and clinically critical feature — early, appropriately selected patients can show substantial or complete reversal of gait, and partial reversal of cognitive/urinary symptoms, after CSF shunting; delayed diagnosis is associated with reduced reversibility due to accumulating irreversible periventricular white-matter injury.
- **Critical periods:** Earlier intervention (shorter duration of preoperative symptoms) is repeatedly identified as a positive prognostic factor for shunt responsiveness, underscoring a "window of opportunity" before fixed structural injury occurs.

---

## 9. Inheritance and Population

### Epidemiology
- **Incidence (Germany, national claims data, 2005–2022):** rose 48%, from 5.4 to 8.0 cases per 100,000 population, peaking in 2018, with the largest increases in the 80–89 age group (PMC11666604).
- **Incidence (population-based cohort):** ~4.8 cases per 1,000 person-years among older adults in longitudinal follow-up.
- **Prevalence:** In the largest population-based study (Western Sweden), **0.2% of individuals aged 70–79** and **5.9% of those ≥80 years** met guideline criteria for probable iNPH — figures substantially higher than earlier clinic-based estimates, reflecting how underdiagnosed the condition is. A separate cohort found prevalence of "possible iNPH" doubling from 1.5% to 2.9% over the follow-up period.
- **Proportion of dementia burden:** iNPH is estimated to account for roughly **6% of all dementia cases**, notable because it is one of the few potentially reversible dementia causes.
- **Underdiagnosis:** widely emphasized as a major public-health and economic issue — "possibly enormous underdiagnosis" (PMC10661316) — with substantial social and economic burden from unrecognized, treatable disability.

### Inheritance Pattern
iNPH does not follow classic Mendelian inheritance; it is best modeled as a **complex/multifactorial trait** with contributing common-variant risk loci (FinnGen GWAS, 6 genome-wide significant loci) and rarer higher-effect susceptibility variants/copy-number changes (SFMBT1 intron-2 CNV, CFAP43, DNAH14, CWH43). No formal penetrance/expressivity estimates analogous to monogenic disease exist; genetic anticipation, germline mosaicism, and founder-effect data specific to iNPH have not been robustly reported, though SFMBT1 CNV enrichment in Finnish and Norwegian cohorts hints at possible population-specific enrichment worth further study (a Nordic founder-effect hypothesis has been raised but not definitively established).

### Population Demographics
- **Age distribution:** overwhelmingly elderly (≥65, with steep increase ≥80).
- **Sex ratio:** some cohorts report a modest male predominance, though this varies by study population; not as strongly skewed as many other neurodegenerative conditions.
- **Geographic/ancestry patterns:** Most large genetic and epidemiologic studies derive from Nordic/European populations (FinnGen, Swedish, Norwegian, German cohorts, Japanese cohorts for SFMBT1); population-specific prevalence and genetic architecture in other ancestries is comparatively understudied — a notable evidence gap.

---

## 10. Diagnostics

### Clinical Diagnostic Criteria
The most widely used framework derives from the **Japanese iNPH Treatment Guidelines** (currently in a third edition) and analogous international consensus criteria, requiring:
1. Age typically >60 years.
2. Presence of ≥1 of the triad: gait disturbance, cognitive impairment, urinary dysfunction (gait is usually required/most heavily weighted).
3. Radiological ventriculomegaly, classically **Evans Index >0.3** (ratio of maximal frontal horn width to maximal internal skull diameter on axial CT/MRI).
4. Normal/near-normal CSF opening pressure (80–200 mmH₂O) on lumbar puncture, without papilledema.
5. Symptoms not fully explained by another condition.

### Imaging Biomarkers
- **Evans Index (EI):** meta-analytic sensitivity 96%, specificity 83% for iNPH; cutoff >0.3 (some frameworks use >0.32).
- **DESH (Disproportionately Enlarged Subarachnoid-space Hydrocephalus)** — tight high-convexity sulci with enlarged Sylvian fissures and ventriculomegaly; considered highly specific, and interobserver reliability of the DESH score has been a recent subject of study (ScienceDirect, 2025).
- **Callosal angle (CA):** meta-analytic sensitivity 91%, specificity 93%.
- Emerging AI-based automated 3D T1 MRI volumetric analysis for iNPH diagnosis (*AJNR* 2025, DOI in article 46/1/33).
- Cortical thickness combined with ventricular morphometry improves diagnostic accuracy (*Front Aging Neurosci* 2024).

### CSF Dynamic/Provocative Testing
- **CSF tap test (Miller Fisher / large-volume lumbar puncture or tap test):** positivity defined as ≥20% improvement in timed 10-meter walk test time/steps, and/or ≥10% improvement in MMSE, and/or ≥1-point improvement in a urinary incontinence score; meeting any one criterion is considered positive.
- **External lumbar drainage (ELD)** and **CSF infusion testing (measuring outflow resistance, Rout)** are more invasive but higher-sensitivity predictors of shunt responsiveness, discussed in "Invasive Preoperative Investigations in iNPH: A Comprehensive Review" (ScienceDirect S1878875023015474).

### CSF Biomarkers
- **AD-type biomarkers (Aβ42, Aβ40, total-tau, phospho-tau):** iNPH classically shows **low Aβ42** (similar to Alzheimer's disease) but **normal t-tau and p-tau**, producing a distinctive but sometimes confounding profile; a positive Aβ42/Aβ40 ratio together with elevated p-tau raises suspicion of coexistent Alzheimer's pathology, which may influence shunt outcome.
- **YKL-40 (chitinase-3-like protein 1):** elevated in CSF tap-test non-responders, proposed as a marker of reactive astrogliosis/AQP4 dysregulation predicting poor shunt response.
- **AQP4:** reduced/mislocalized in iNPH CSF and tissue studies (§6).
- **Emerging unbiased CSF proteomics:** broad decreases in CSF protein efflux signatures, a molecular fingerprint of glymphatic failure (Neurology 2024/2025, DOI:10.1212/WNL.0000000000213375).
- In vivo amyloid-PET studies show a substantial prevalence of concomitant beta-amyloid pathology in iNPH cohorts, associated with distinct neuropsychological profiles (PMC11351685).

### Genetic Testing
No clinically validated genetic test panel currently guides routine iNPH diagnosis or management; genetic findings (SFMBT1 CNV, GWAS loci) remain research-stage rather than diagnostic-stage. Whole-genome/exome sequencing, gene panels, and chromosomal microarray have no established clinical indication for typical iNPH but may be considered in atypical, familial, or early-onset presentations, or when a syndromic ciliopathy is suspected.

### Differential Diagnosis
Alzheimer's disease and other dementias (frontotemporal dementia — notably, a 10-year retrospective study found increased prevalence of NPH in both FTD variants, PMC10508318), Parkinson's disease and other parkinsonian/gait disorders, cerebral small vessel disease/vascular dementia, and other causes of ventriculomegaly (ex vacuo dilation from atrophy, obstructive hydrocephalus).

### Screening
No population-wide screening program exists; opportunistic case-finding relies on clinical suspicion in elderly patients presenting with the triad, supported by incidental radiological ventriculomegaly noted on imaging obtained for other indications.

---

## 11. Outcome/Prognosis

- **Mortality/life expectancy:** iNPH itself is not typically directly fatal, but untreated disease contributes substantially to morbidity (falls, immobility, institutionalization) that can shorten life expectancy indirectly; formal disease-specific mortality statistics are not well standardized across studies.
- **Shunt-responder outcomes:** Ventriculoperitoneal (VP) shunting produces significant improvement in modified Rankin Scale and iNPH Grading Scale (iNPHGS) scores at 1, 2, and 3 years post-surgery, with MMSE improvement significant at 1 and 3 years in some cohorts (PMC11992790, long-term VP shunt outcomes study). Long-term (multi-year) quality-of-life benefit is documented (PMID:37004132).
- **Endoscopic third ventriculostomy (ETV) vs VPS:** a retrospective cohort comparison found differences in surgical management outcomes between the two approaches for iNPH (PMC11875132) — VPS remains the more established/first-line approach for communicating (non-obstructive) iNPH, while ETV is generally reserved for obstructive hydrocephalus variants.
- **Complications:** Subdural hematoma/hygroma occurs in ~9–10.4% of shunted patients, related to over- or under-drainage; shunt malfunction, infection, and the need for revision surgery are recognized risks.
- **Prognostic factors for shunt response:** shorter duration of preoperative symptoms, absence of significant comorbid vascular/neurodegenerative pathology, higher education level, non-smoking status, and fewer postoperative complications are associated with better outcomes; multiple concurrent comorbidities predict worse outcomes and should be weighed before shunt insertion.
- **Prognostic biomarkers:** CSF Aβ42/Aβ40 and p-tau positivity (suggesting comorbid AD pathology) may predict attenuated or less durable shunt response; elevated CSF YKL-40 is associated with tap-test non-response. Preoperative imaging biomarkers (DESH, callosal angle, ventricular morphometry) combined with tap test improve prediction of shunt surgery outcome (PMC11903477).
- **A recent placebo-controlled randomized trial** ("A Randomized Trial of Shunting for Idiopathic Normal-Pressure Hydrocephalus," NEJM, DOI:10.1056/NEJMoa2503109 — the PENS trial, NCT03350750) provides higher-tier randomized evidence for shunting effectiveness versus the historically observational/uncontrolled evidence base — a major methodological advance for the field.

---

## 12. Treatment

### Surgical (mainstay of definitive therapy)
- **Ventriculoperitoneal (VP) shunting** — the established first-line definitive treatment for both iNPH and most sNPH; a programmable/adjustable-valve shunt diverts CSF from the lateral ventricle to the peritoneal cavity. **NCIT:** treatment_term NCIT:C15329 (Surgical Procedure) or a more specific shunt-placement term if available in NCIT; therapeutic_modality: `SURGERY`/`DEVICE`.
- **Ventriculoatrial or ventriculopleural shunting** — alternative distal sites used when peritoneal shunting is contraindicated.
- **Endoscopic third ventriculostomy (ETV)** — an alternative in select patients, more established for obstructive hydrocephalus but studied comparatively against VPS in iNPH (PMC11875132).
- **Lumboperitoneal shunting** — an alternative extracranial approach avoiding ventricular catheterization, used in some centers for communicating NPH.

### Pharmacotherapy
No disease-modifying pharmacologic therapy exists for iNPH; pharmacologic management is largely supportive (e.g., anticholinergic or beta-3 agonist agents for residual urinary urgency post-shunt — NCIT:C15986 Pharmacotherapy) and management of comorbid vascular risk factors (antihypertensives, statins, glycemic control agents) as an adjunctive/preventive strategy given the vascular risk factor association data.

### Supportive/Rehabilitative
- **Physical therapy/gait rehabilitation** (NCIT:C15302 Physical Therapy) — used both pre- and post-shunt to maximize functional gait recovery.
- **Fall-prevention programs** and assistive devices.
- **Genetic counseling** (NCIT:C15240) — of limited current applicability given the absence of validated single-gene testing, but relevant in rare suspected familial/syndromic cases.
- **Supportive care** (NCIT:C15747) for advanced/non-responsive disease.

### Experimental / Investigational
- Ongoing trials characterizing the **prodromal phase** of iNPH (European Study of Prodromal iNPH, NCT05910944), aiming to define earlier intervention windows.
- The PENS trial (NCT03350750) provides the first placebo-controlled randomized evidence base for shunting effectiveness.
- No gene therapy, cell therapy, or RNA-based therapeutics are in development specific to iNPH given its complex/multifactorial and largely mechanical pathophysiology; the primary "molecular" therapeutic frontier is biomarker-guided **patient selection** (CSF/glymphatic biomarkers to predict shunt responsiveness) rather than a distinct disease-modifying drug target.

### Treatment Outcomes / Adverse Events
See §11 for response rates and complications (subdural hematoma/hygroma 9–10.4%, shunt malfunction/infection, over/under-drainage).

### Treatment Algorithm
Standard pathway: clinical suspicion → imaging (Evans Index, DESH, callosal angle) → CSF tap test (± infusion study/ELD in equivocal cases) → shunt surgery in tap-test/ELD responders → postoperative gait/cognitive/urinary reassessment and shunt-valve adjustment as needed. A proposed algorithm for managing secondary post-shunt deterioration in iNPH patients is described in PMC7055114.

---

## 13. Prevention

- **Primary prevention:** No established primary prevention strategy for iNPH exists given its multifactorial, poorly understood etiology; modifiable vascular risk factor control (blood pressure, glycemic control, weight management, lipid management) is a plausible but not rigorously trial-proven preventive approach, extrapolated from the INPH-CRasH association data.
- **Secondary prevention (for sNPH):** Prompt and adequate treatment of subarachnoid hemorrhage, bacterial/tuberculous/other meningitis, and traumatic brain injury, along with vigilant post-insult monitoring for evolving hydrocephalus (serial imaging, ICP monitoring where indicated), aims to detect and treat secondary hydrocephalus before irreversible neurological injury occurs. Early recognition and shunting/ETV in at-risk post-SAH patients reduces morbidity from shunt-dependent hydrocephalus (see the SAH shunt-dependence risk-factor meta-analysis, PMC11319414).
- **Screening/early detection:** No population-based screening program exists; earlier clinical recognition of the prodromal triad (motivating current prodromal-iNPH research, NCT05910944) and opportunistic radiological flagging of ventriculomegaly on incidental imaging are the most actionable current strategies to shorten the diagnosis-to-treatment interval, which is itself a major modifiable prognostic factor (§8, §11).
- **Genetic counseling:** Not currently a mainstream component of iNPH prevention given the absence of validated predictive genetic testing, though this could become more relevant as GWAS/candidate-gene findings mature.
- **Public health/behavioral interventions:** General cardiovascular risk factor modification (as for cerebral small vessel disease prevention broadly) is the most plausible population-level lever, though iNPH-specific outcome trials of such interventions are lacking.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** NCBITaxon:9606 (Homo sapiens) is the primary species of clinical interest; naturally occurring NPH-like syndromes in companion animals are not well established as a distinct clinical entity comparable to human iNPH (unlike, e.g., congenital hydrocephalus, which is well described in toy-breed dogs).
- **Comparative note:** Congenital/obstructive hydrocephalus is naturally occurring and well documented in several companion-animal breeds (e.g., Chihuahuas, English Bulldogs — OMIA entries exist for canine hydrocephalus), but these are developmental/obstructive rather than adult-onset communicating NPH phenocopies, so cross-species natural-disease relevance to iNPH specifically is limited.
- **Zoonotic potential:** Not applicable — NPH is not an infectious/transmissible disease itself (though secondary NPH can follow an infectious meningitis, the hydrocephalus sequela itself is not zoonotic).

---

## 15. Model Organisms

### Rodent (primary model system)
- **Kaolin-induced hydrocephalus (rat, and some mouse studies)** — the dominant experimental model, first introduced by Dixon (1932). Kaolin injected into the **cisterna magna or basal cisterns** produces an **obstructive hydrocephalus (OHC)** model with elevated intracranial pressure that subsides toward normal range within about a week, useful for studying acute/subacute CSF dynamics.
- **Cortical subarachnoid space kaolin injection** — produces a slower-onset, initially asymptomatic **communicating hydrocephalus** considered more representative of **late-adult-onset NPH** specifically, via an inflammatory/fibrotic subarachnoid response impairing CSF absorption (a mechanistic parallel to human secondary NPH pathogenesis).
- **AQP4-deficient mice with kaolin-induced hydrocephalus** — show **accelerated progression** of hydrocephalus compared to wild-type, directly supporting AQP4's protective/compensatory role in glymphatic CSF clearance and providing causal (not just correlative) evidence for the glymphatic-failure mechanism (PMID:16552421).
- **Kaolin-induced chronic hydrocephalus in transgenic rats expressing human APP** — accelerates amyloid deposition and vascular disease, modeling the mechanistic link between impaired CSF/glymphatic clearance and amyloid pathology relevant to the iNPH–Alzheimer's comorbidity axis (PMC4328504).
- **Optic disc/ICP changes in rat obstructive hydrocephalus models** — used to study secondary consequences of elevated ICP (PMC9128145).
- **CSF outflow resistance / lymphatic CSF absorption studies** in kaolin-induced communicating hydrocephalus rats demonstrate elevated CSF outflow resistance linked to impaired lymphatic (not just arachnoid granulation) CSF absorption — broadening the mechanistic model beyond the classical arachnoid-villi-only absorption paradigm (PMC2831828).

### Model Characteristics
- **Phenotype recapitulation:** Kaolin models recapitulate ventriculomegaly, elevated/altered ICP dynamics, and periventricular white matter injury reasonably well, and the cortical-subarachnoid variant specifically models the communicating, slow-onset phenotype relevant to adult NPH.
- **Limitations:** Kaolin models are **inflammatory/chemically induced** rather than spontaneous/age-related, so they do not capture the genetic susceptibility architecture (SFMBT1, ciliary genes) or the decades-long human aging process; they also do not naturally reproduce the full human clinical triad (gait/cognition/urinary function) with behavioral readouts of comparable specificity, limiting translational fidelity for cognitive/psychiatric endpoints. Rodent CSF dynamics and cranial compliance also differ substantially in scale from human CSF physiology, and AQP4-knockout findings, while mechanistically informative, represent an extreme genetic perturbation rather than the partial/complex genetic risk architecture seen in human iNPH — an appropriate `HUMAN_MODEL_MISMATCH` framing if curated in dismech.

### Applications
Rodent kaolin models are primarily used to study: CSF outflow resistance and absorption pathways (including the lymphatic contribution), the role of AQP4/glymphatic function in disease progression, periventricular white matter/ischemic injury mechanisms, and the mechanistic interaction between impaired CSF clearance and amyloid pathology (APP-transgenic + kaolin combination models).

### Resources
No single organism-specific hydrocephalus database was identified analogous to MGI/ZFIN disease-model repositories; kaolin-model protocols and strains are documented primarily through the primary literature (Dixon 1932 origin; subsequent refinements reviewed in Zhang et al., *FASEB BioAdvances* 2024, DOI:10.1096/fba.2024-00070) rather than a centralized public repository.

---

## Summary of Key Evidence Gaps for Curation

1. **Genetic architecture** is still emerging (2024 FinnGen GWAS is the largest to date but explains only a fraction of heritability); no clinically actionable genetic test exists.
2. **Population-based prevalence data are ancestry-limited** (mostly Nordic/European/Japanese cohorts); global and diverse-ancestry data are sparse.
3. **Randomized-controlled evidence for shunting is very recent** (PENS trial) — most historical outcome data are observational/uncontrolled.
4. **Animal models lack a spontaneous, genetically-driven, aging-associated NPH phenocopy** — kaolin models are inflammatory/mechanical surrogates, a `HUMAN_MODEL_MISMATCH`-worthy caveat.
5. **The iNPH–Alzheimer's comorbidity boundary remains biomarker-ambiguous** (discordant Aβ/tau CSF profiles), complicating both diagnosis and prognostic biomarker curation.

---

## Sources

- [Idiopathic Normal Pressure Hydrocephalus: A Comprehensive Review (PMID:42239999)](https://pubmed.ncbi.nlm.nih.gov/42239999/)
- [Implications of the glymphatic system in the pathogenesis of normal pressure hydrocephalus (J Neurosurg 2025)](https://thejns.org/view/journals/j-neurosurg/143/1/article-p135.xml)
- [Idiopathic Normal-Pressure Hydrocephalus | New England Journal of Medicine (Johnson & Williams, 2025)](https://www.nejm.org/doi/full/10.1056/NEJMra2306506)
- [A Randomized Trial of Shunting for Idiopathic Normal-Pressure Hydrocephalus | NEJM (PENS trial)](https://www.nejm.org/doi/abs/10.1056/NEJMoa2503109)
- [Idiopathic Normal Pressure Hydrocephalus - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK542247/)
- [Increasing incidence of normal pressure hydrocephalus in Germany (PMC11666604)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11666604/)
- [Idiopathic Normal Pressure Hydrocephalus: The Real Social and Economic Burden of a Possibly Enormous Underdiagnosis Problem (PMC10661316)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10661316/)
- [Increased prevalence of NPH in both variants of frontotemporal dementia (PMC10508318)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10508318/)
- [CWH43 Variants Are Associated With Disease Risk and Clinical Phenotypic Measures in NPH](https://www.neurology.org/doi/10.1212/NXG.0000000000200086)
- [A Segmental Copy Number Loss of the SFMBT1 Gene Is a Genetic Risk for Shunt-Responsive iNPH (PLOS ONE)](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0166615)
- [Risk Variants Associated With Normal Pressure Hydrocephalus: GWAS in FinnGen (PMID:39141892)](https://pubmed.ncbi.nlm.nih.gov/39141892/)
- [Genetic Risk Factors in Normal Pressure Hydrocephalus: What We Know and What Is Next (PMID:40266017)](https://movementdisorders.onlinelibrary.wiley.com/doi/full/10.1002/mds.30206)
- [Unbiased CSF Proteomics in Patients With iNPH (Neurology)](https://www.neurology.org/doi/10.1212/WNL.0000000000213375)
- [Evaluation of aquaporins in the CSF in patients with iNPH (PMC8486078)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8486078/)
- [The promise of cerebrospinal fluid biomarkers in idiopathic normal pressure hydrocephalus (PMC11399724)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11399724/)
- [Outcomes of Ventriculoperitoneal Shunt in Patients With iNPH 2 Years After Surgery (PMC8634250)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8634250/)
- [Long-term outcomes of ventriculoperitoneal shunt therapy in iNPH (PMC11992790)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11992790/)
- [Preoperative imaging biomarkers combined with tap test for predicting shunt surgery outcome in iNPH (PMC11903477)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11903477/)
- [The impact of cerebrospinal fluid shunting on quality of life in iNPH (PMID:37004132)](https://pubmed.ncbi.nlm.nih.gov/37004132/)
- [VPS Versus ETV for the Surgical Management of iNPH (PMC11875132)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11875132/)
- [Interobserver reliability of the DESH score in idiopathic chronic hydrocephalus](https://www.sciencedirect.com/science/article/pii/S0028377025001079)
- [Insights on pathophysiology of hydrocephalus rats induced by kaolin injection (FASEB BioAdvances 2024)](https://faseb.onlinelibrary.wiley.com/doi/10.1096/fba.2024-00070)
- [Accelerated progression of kaolin-induced hydrocephalus in aquaporin-4-deficient mice (PMID:16552421)](https://pubmed.ncbi.nlm.nih.gov/16552421/)
- [Kaolin-induced chronic hydrocephalus accelerates amyloid deposition in transgenic rats expressing human APP (PMC4328504)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4328504/)
- [Elevated CSF outflow resistance associated with impaired lymphatic CSF absorption in a rat model (PMC2831828)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2831828/)
- [In Vivo Prevalence of Beta-Amyloid Pathology and AD Co-Pathology in iNPH (PMC11351685)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11351685/)
- [Elevated CSF LRG and Decreased Alzheimer's Disease Biomarkers in iNPH (PMC7961420)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7961420/)
- [Vascular risk factors in iNPH: A prospective case-control study (INPH-CRasH) (PMID:28062721)](https://pubmed.ncbi.nlm.nih.gov/28062721/)
- [Association between vascular risk factors and iNPH: a Mendelian randomization study (J Neurol 2023)](https://link.springer.com/article/10.1007/s00415-023-11604-6)
- [Risk factors of shunt-dependent hydrocephalus after subarachnoid hemorrhage: systematic review and meta-analysis (PMC11319414)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11319414/)
- [Secondary Normal-Pressure Hydrocephalus in Rheumatoid Meningitis (PMC8299371)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8299371/)
- [Neuropsychiatric Features in Patients With iNPH: A Systematic Review and Meta-Analysis (PMC12879024)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12879024/)