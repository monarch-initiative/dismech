---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-31T20:17:42.516514'
end_time: '2026-08-31T20:31:47.983569'
duration_seconds: 845.47
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Manganism
  mondo_id: ''
  category: Neurological Disorder
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
  - claude-opus-5[1m]
  web_search_requests: 17
  num_turns: 55
  total_cost_usd: 4.665313999999999
  session_id: c769cef7-ef5b-453c-a449-15debee70f8d
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 44
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Manganism
- **MONDO ID:**  (if available)
- **Category:** Neurological Disorder

## Research Objectives

Please provide a comprehensive research report on **Manganism** covering all of the
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

# Manganism — Comprehensive Research Report

*Prepared 2026-08-31 for a dismech knowledge-base entry. Target: **Manganism**, MONDO:0017638.*

> A quick framing note before the wall of detail: manganese is a nutrient your mitochondria genuinely need — it's the metal at the heart of SOD2, it's the cofactor glutamine synthetase can't work without. Manganism is what happens when a nutrient's dose-response curve gets pushed off the right-hand edge. It's less "a poison got in" and more "a housekeeping metal stopped being housekept," and that distinction shapes basically every mechanism below.

---

## 1. Disease Information

### Overview

Manganism is a neurotoxic syndrome caused by excess manganese (Mn) reaching the central nervous system, where it accumulates preferentially in the basal ganglia — above all the **globus pallidus** — and produces an extrapyramidal movement disorder with prominent psychiatric and cognitive features. It is classically described as biphasic: an early neuropsychiatric phase ("manganese madness" / locura manganica) of irritability, emotional lability, compulsive behavior, hallucinations and insomnia, followed by a motor phase of bradykinesia, rigidity, dystonia, gait disturbance and speech impairment.

The single most important framing fact for a mechanism knowledge base: **manganism is not Parkinson's disease, and the lesion is in a different place.**

> "Pathologic studies demonstrate a consistent pattern characterized by damage to the globus pallidus (particularly the internal segment) with sparing of the substantia nigra pars compacta and the absence of Lewy bodies." — Perl & Olanow, *J Neuropathol Exp Neurol* 2007 (**PMID:17882011**)

> "Mn-induced parkinsonism patients regardless of the dose of levodopa administered are unresponsive to levodopa treatment," which is "a hallmark of Mn-induced parkinsonism, which distinguishes the disease from idiopathic PD." — Kwakye et al., *Int J Environ Res Public Health* 2015 (**PMID:26154659**)

That clean historical picture has been complicated by two decades of work on **chronic low-level exposure**, where the target territory widens:

> "Manganese exposure has evolved from acute, high-level exposure causing manganism to low, chronic lifetime exposure, in which the target areas extend beyond the globus pallidus to the entire basal ganglia, including the substantia nigra pars compacta." — Lucchini & Tieu, *Biomolecules* 2023 (**PMID:37627255**)

So the modern field distinguishes at least three overlapping entities, and a KB entry should probably model them as related-but-separable:

| Entity | Exposure | Lesion | Levodopa |
|---|---|---|---|
| **Classic manganism** | Acute/subacute high-dose (mining, ore milling, ephedrone) | Globus pallidus internus, striatum; SNpc spared; no Lewy bodies | Unresponsive |
| **Chronic low-level Mn parkinsonism** | Welding fume, ferroalloy, environmental | Whole basal ganglia incl. SNpc; presynaptic dopaminergic changes reported | May respond |
| **Inherited hypermanganesaemia (HMNDYT1/2)** | None — a transporter defect | Basal ganglia + white matter, dentate; ventral pons spared | Unresponsive; chelation is the treatment |

### Identifiers

| Resource | Identifier |
|---|---|
| **MONDO** | **MONDO:0017638** — "manganese poisoning" (synonyms: *manganism*, *manganese intoxication*) — *verified via OLS4* |
| MONDO (transport disorders) | MONDO:0017766 "disorder of manganese transport" |
| MONDO (inherited) | MONDO:0000214 "hypermanganesemia with dystonia"; MONDO:0013208 (HMNDYT1); MONDO:0014864 (HMNDYT2) |
| MeSH | D020149 (Manganese Poisoning) |
| ICD-10-CM | T57.2 (Toxic effect of manganese and its compounds), with 4th/5th/6th-character extensions T57.2X1–T57.2X4 |
| ICD-9 | 503 |
| ICD-11 | NE61 (toxic effect of metals — *low confidence, verify against the ICD-11 browser before binding*) |
| Orphanet | ORPHA:306682 (Manganese poisoning); ORPHA:309854 (HMNDYT1); ORPHA:521406 (HMNDYT2) |
| OMIM | Not applicable for acquired manganism. HMNDYT1 = **613280**; HMNDYT2 = **617013** |
| SNOMED CT | 88687001 |
| MedDRA | 10058951 |
| GARD | 0021264 |
| EFO | EFO:1001808 |
| UMLS | C2750442 (HMNDYT1); C4310765 (HMNDYT2) |

MONDO's own definition text, quotable as evidence:

> "Manganese poisoning is associated with chronic inhalation of manganese particles by individuals who work with manganese ore. Clinical features include confusion; hallucinations; and an extrapyramidal syndrome (Parkinson disease, secondary)."

### Synonyms

Manganism · manganese intoxication · manganese poisoning · manganese-induced parkinsonism (MnIP) · manganese-induced neurotoxicity · "manganese madness" / *locura manganica* (historical, early psychiatric phase) · welders' parkinsonism (occupational subset) · ephedrone/methcathinone-induced parkinsonism (drug subset) · acquired hepatocerebral degeneration (hepatic subset, overlapping but not identical).

### Data provenance

Almost entirely **aggregated disease-level** — occupational cohort studies, case series, and toxicology reviews rather than EHR-derived phenotyping. The inherited forms are the exception: HMNDYT1/2 knowledge comes from a genuinely enumerable patient set (98 individuals worldwide as of January 2025, see §9), so those are effectively patient-level. There is no manganism registry and no ICD-code-based EHR cohort study I could locate — a genuine knowledge gap worth recording.

---

## 2. Etiology

### Causal factor: manganese overload of the CNS

The proximate cause is always the same — too much Mn crossing into brain — but the routes there are several, and they matter mechanistically because they differ in *which barrier failed*.

#### 2a. Inhalational occupational exposure (the dominant cause)

Inhaled Mn largely bypasses hepatobiliary first-pass regulation, which is why the lung is a far more dangerous route than the gut. Sources:

- **Welding** — steel contains Mn, so welding fume contains Mn. This is the largest exposed population worldwide.
- **Mining and ore crushing/milling** of pyrolusite (MnO₂).
- **Ferroalloy and ferromanganese smelting**.
- **Dry-cell battery manufacture**; **steel foundries**; **glass and ceramics**.
- **MMT (methylcyclopentadienyl manganese tricarbonyl)** — a gasoline antiknock additive, hence vehicular emissions.
- **Emerging:** nickel-manganese-cobalt lithium-ion battery particulates show systemic toxicity in animal models (Khindri & Maj 2025, **PMID:40496384**).

Exposure limits — note the two-order-of-magnitude regulatory gap, which is itself a public-health finding:

| Standard | Limit |
|---|---|
| ACGIH TLV-TWA, respirable Mn (2013 revision) | **0.02 mg/m³** |
| ACGIH TLV-TWA, inhalable Mn | 0.1 mg/m³ |
| OSHA PEL (ceiling), Mn compounds/fume | **5 mg/m³** |
| WHO threshold associated with classical manganism | "at least 1 mg/m³" (Lucchini & Tieu 2023, PMID:37627255) |
| Proposed environmental PM₁₀ benchmark | "20–25 ng/m³, as a cut-off for increased risk" (ibid.) |

The OSHA PEL is 250× the ACGIH TLV. A shop can be fully OSHA-compliant while exposing welders at levels the toxicology says are hazardous.

#### 2b. Environmental exposure

Ambient air near ferroalloy plants (the Brescia/Valcamonica, Italy studies are the reference cohort), Mn in soil and deposited dust, and Mn in drinking water — especially private wells drawing on Mn-rich groundwater. Environmental exposure is the route most relevant to pediatric neurodevelopment (§3, §5).

#### 2c. Iatrogenic — parenteral nutrition

Intravenous Mn in TPN bypasses gut regulation entirely, and if the patient is cholestatic they can't excrete it in bile either — a double bypass.

> "Eleven patients investigated by MRI showed hyperintense basal ganglia on T1-weighted images, indicating Mn deposition in the brain." — Fell et al., *Lancet* 1996 (**PMID:8622451**)

The recommendation from that work: a low-dose regimen of not more than **0.018 µmol/kg per 24 h**, with regular neurological examination.

#### 2d. Hepatic — cirrhosis and portosystemic shunting

Mn is cleared by the liver into bile. Lose the liver (or route portal blood around it via a shunt, congenital or TIPS) and Mn accumulates. This produces **acquired hepatocerebral degeneration** and contributes to the pallidal T1 hyperintensity seen in cirrhosis.

> "In patients with pallidal T1 hyperintensity, pallidal manganese concentrations were increased sevenfold over controls and over fourfold vs liver patients with normal MRI." — Klos et al., *Neurology* 2006 (**PMID:17159105**)

#### 2e. Drug-related — ephedrone / methcathinone

Home-synthesised methcathinone from pseudoephedrine uses **potassium permanganate** as the oxidant, and the residual Mn is injected intravenously along with the drug. This produced a distinctive epidemic in Eastern Europe/Russia.

> Stepens et al. studied 23 adults in Latvia with extrapyramidal symptoms; "all 23 patients had gait disturbance and difficulty walking backward." — *N Engl J Med* 2008 (**PMID:18322282**)

Clinically: levodopa-unresponsive bradykinesia, retropulsion with backward falls, dysarthria, dystonia, emotional lability, and the characteristic **cock-walk gait** (walking on the toes with elbows flexed, leaning forward).

#### 2f. Renal — maintenance haemodialysis

A reported association between manganism-like symptoms and basal ganglia T1 hyperintensity in haemodialysis patients (*AJNR* 2007;28:1474) — a smaller, less-replicated route worth flagging as tentative.

### Risk factors

**Genetic**
- **Biallelic loss-of-function in *SLC30A10*** (HGNC:25355) → HMNDYT1 (hypermanganesaemia with dystonia, polycythaemia and cirrhosis). Autosomal recessive.
- **Biallelic loss-of-function in *SLC39A14*** (HGNC:20858) → HMNDYT2. Autosomal recessive.
- **Heterozygous carriers appear to be at increased risk of acquired manganism.** This is the single most interesting gene-environment finding in the field: in the Brescia ferroalloy region, "heterozygous transporter mutations [were] found in up to 40% of the cases in the province of Brescia" (Lucchini & Tieu 2023, PMID:37627255). *(Treat this figure with care — it comes from a review's summary of a regional case series, not a population-based genotyped cohort.)*
- **Iron deficiency** is functionally a risk factor through the shared-transporter mechanism (DMT1/SLC11A2 is not Mn-specific; low iron upregulates it and raises Mn absorption). This makes iron status a modifier, not just a comorbidity.
- Proposed but less firmly established modifiers, drawn from the PD gene set: ***PRKN*** (parkin regulates DMT1-mediated Mn uptake; loss of function "could facilitate Mn uptake"), ***PARK7*/DJ-1** (Mn exposure "reduce[s] the levels of DJ-1"), ***ATP13A2*** (the protein "protect[s] cells against Mn toxicity by transporting Mn into lysosomes; however, this protection is lost when mutations in this gene occur"), and ***SNCA***. All from Lucchini & Tieu 2023 (PMID:37627255).

**Environmental / demographic**
- Occupation (welding, mining, ferroalloy, foundry, battery manufacture) — the dominant risk factor.
- **Cumulative** rather than recent exposure: "cumulative exposure of manganese over time was more indicative of higher tissue concentrations than recent exposure" (Khindri & Maj 2025, PMID:40496384).
- Chronic liver disease / portosystemic shunt.
- Long-term parenteral nutrition, especially with cholestasis.
- Injection drug use involving permanganate-oxidised stimulants.
- Age: the young (developing brain, higher absorption, lower biliary excretion capacity in neonates) and possibly the elderly.
- Sex: male predominance in occupational cases is largely exposure-driven; some experimental evidence suggests **oestrogen is protective** in female mice (Khindri & Maj 2025).

### Protective factors

- **Adequate iron status** — competition for DMT1 reduces Mn absorption. This is the mechanistic basis for iron supplementation as a *therapy* in HMNDYT1 (§12).
- **Intact hepatobiliary excretion** — the body's primary Mn drain.
- **Oral rather than inhalational route** — first-pass hepatic extraction is very efficient for ingested Mn, which is why dietary Mn is nearly never toxic in people with normal livers and normal transporters.
- **Sediment binding**: "sediment-bound manganese shows lower bioavailability" (Khindri & Maj 2025) — relevant to drinking-water risk assessment.
- Engineering controls: local exhaust ventilation, fume extraction, respiratory protection.
- Experimentally protective (animal/in vitro only, **not** clinically established): riluzole (protects astrocytic glutamate transporters and glutamine synthetase, PMID:22391793), curcumin, resveratrol/SIRT1 activation, vitamin E, niacin, punicalagin, *Dendrobium nobile* alkaloids.

### Gene-environment interaction

This disease is close to a textbook GxE case, and it works in both directions:

1. **Genotype amplifies exposure.** Heterozygous *SLC30A10*/*SLC39A14* carriers have reduced excretory reserve; the same welding job produces a higher body burden.
2. **Exposure amplifies genotype.** In mice, "although Mn by itself does not cause neurodegeneration, when combined with a PD-linked protein, nigral dopaminergic cell loss occurs" (Lucchini & Tieu 2023). In *C. elegans*, "the life-span…was reduced after Mn exposure when DJ-1 was deleted."
3. **Nutritional genotype-equivalent:** iron deficiency (dietary or genetic) upregulates DMT1 and increases Mn uptake for a fixed external dose.

---

## 3. Phenotypes

Frequencies below are qualitative unless a source gives a number — the occupational literature reports symptom prevalence within heterogeneous exposed cohorts rather than within diagnosed manganism cases, so hard per-phenotype frequencies are mostly unavailable. **Flagging that as a real knowledge gap** rather than inventing percentages.

### Early neuropsychiatric phase ("manganese madness")

| Phenotype | HPO term | Notes |
|---|---|---|
| Emotional lability | **HP:0000712** | Classic early sign; prominent in ephedrone cases |
| Irritability | **HP:0000737** | |
| Hallucinations | **HP:0000738** | Named in the MONDO definition |
| Psychosis | **HP:0000709** | Historical high-dose mining exposure |
| Aggressive behavior | **HP:0000718** | "bursts of agitation" |
| Anxiety | **HP:0000739** | |
| Depression | **HP:0000716** | |
| Apathy | **HP:0000741** | |
| Insomnia | **HP:0100785** | |
| Sleep disturbance | **HP:0002360** | Includes REM sleep behaviour disorder in some reports |
| Headache | **HP:0002315** | Early nonspecific |
| Memory impairment | **HP:0002354** | |
| Cognitive impairment | **HP:0100543** | "mental slowing" |
| Fatigue | **HP:0012378** | |

Onset: adult, subacute-to-insidious, typically after months-to-years of exposure (much faster — months — in ephedrone users). Severity: mild to severe, dose-dependent. Course: may stabilise or partially remit on exposure cessation; the psychiatric phase is generally more reversible than the motor phase.

### Motor / extrapyramidal phase

| Phenotype | HPO term | Notes |
|---|---|---|
| Parkinsonism | **HP:0001300** | The syndromic anchor |
| Bradykinesia | **HP:0002067** | "generalized bradykinesia"; **symmetric**, unlike PD |
| Akinesia | **HP:0002304** | |
| Rigidity | **HP:0002063** | "widespread rigidity" |
| Cogwheel rigidity | **HP:0002396** | Less characteristic than in PD |
| Hypertonia | **HP:0001276** | |
| Dystonia | **HP:0001332** | **More frequent than in PD** — a key discriminator |
| Torticollis | **HP:0000473** | Reported in dystonic presentations |
| Oculogyric crisis | **HP:0010553** | Reported (Khindri & Maj 2025) |
| Blepharospasm | **HP:0000643** | |
| Postural instability | **HP:0002172** | **Early**, unlike PD where it is late |
| Falls | **HP:0002527** | Retropulsion, backward falls; 11/23 ephedrone patients "falling daily" |
| Gait disturbance | **HP:0001288** | 23/23 ephedrone patients |
| Shuffling gait | **HP:0002362** | |
| Freezing of gait | **HP:0031825** | |
| Tremor | **HP:0001337** | Rapid **postural** tremor typical |
| Resting tremor | **HP:0002322** | **Relatively absent** — negative discriminator vs PD |
| Dysarthria | **HP:0001260** | Hypophonia, "speech disturbances" |
| Hypomimic face | **HP:0000338** | |
| Dysgraphia / micrographia | **HP:0010526** | Handwriting improved with PAS therapy (PMID:16766929) |
| Dysphagia | **HP:0002015** | Advanced disease |
| Drooling | **HP:0002307** | |
| Hyperreflexia | **HP:0001347** | Reported in manganism descriptions |
| Erectile dysfunction / impotence | **HP:0100639** / **HP:0000802** | "Male workers showed impotence and reduced libido" (PMID:26154659) |

**"Cock-walk gait"** deserves special mention: walking on the toes/balls of the feet, elbows flexed, trunk forward — considered near-pathognomonic and specifically noted in HMNDYT1 and in ephedrone manganism. There is **no clean HPO term** for it; closest are HP:0001288 (gait disturbance) and HP:0002362 (shuffling gait). Worth recording as a `preferred_term` with a broader binding rather than forcing a match.

Onset: adult for occupational; **childhood** for the inherited forms. Pattern: insidious, symmetric, bilateral. Progression: progressive during exposure; may plateau or partially improve after cessation, but **dystonia and cognitive impairment often persist** — "Persistent dystonia and cognitive impairment may not fully resolve despite successful manganese reduction" (Khindri & Maj 2025).

### Inherited-form-specific phenotypes (HMNDYT1)

| Phenotype | HPO term | Frequency |
|---|---|---|
| Polycythemia | **HP:0001901** | "present in nearly all patients" (PMID:40320765) |
| Cirrhosis | **HP:0001394** | Micronodular; HMNDYT1 only |
| Hepatomegaly | **HP:0002240** | |
| Elevated hepatic transaminases | **HP:0002910** | |
| Iron depletion (low ferritin, raised TIBC) | — bind to a decreased-ferritin HP term; verify | Characteristic |
| Preserved intellect | — | "Intellectual ability typically preserved" in both HMNDYT1 and HMNDYT2 |

That last one is genuinely striking and belongs in the entry: **cognition is spared despite severe motor disability** in the genetic forms — "Cognitive sparing despite severe motor disability" (PMID:40320765). It's a hard dissociation from the acquired disease and a real clue that the pallidal/striatal lesion, not diffuse toxicity, drives the phenotype.

### Pediatric / neurodevelopmental phenotypes (environmental exposure)

From Bouchard et al., *Environ Health Perspect* 2011 (**PMID:20855239**) and the meta-analysis by Liu/Kim et al. (**PMID:33008482**):

> "a 10-fold increase in hair manganese was associated with a decrease of 2.51 points in Full Scale IQ"

> "higher manganese exposure had a negative effect on neurodevelopment, mostly influencing cognitive and motor skills in children under 6 years of age" (55 studies, 13,388 subjects)

Relevant HPO: HP:0100543 (Cognitive impairment); attention and behavioural measures generally lack good HPO coverage.

### Pulmonary phenotypes

Inhaled Mn dusts/fumes also cause **manganese pneumonitis** and increased susceptibility to bacterial pneumonia in exposed workers — a non-neurological arm of the disease that is often left out of entries. HP:0100598 (Pulmonary edema) applies to acute high-dose inhalation.

### Quality of life

No manganism-specific QoL instrument exists. The welding-cohort literature has applied generic health-status measures (SF-36-type) and found parkinsonism in welding-exposed workers associated with worse health status. Functional impact is dominated by gait/falls (mobility, employment loss), dysarthria (communication), and — in the psychiatric phase — occupational and relational disruption. This is a thin evidence area; treat any QoL claim as low-confidence.

---

## 4. Genetic / Molecular Information

### Causal genes — the inherited forms

**A crucial curation distinction:** acquired manganism has **no causal gene**. The genes below cause the *inherited* hypermanganesaemia disorders, which are separate MONDO entities. They are, however, the best mechanistic window into the acquired disease, because they show what breaks when Mn handling fails.

| Gene | HGNC | OMIM disease | Protein function | Consequence |
|---|---|---|---|---|
| ***SLC30A10*** | **HGNC:25355** | 613280 (HMNDYT1) | Mn **efflux** transporter; mediates biliary and intestinal Mn excretion | Loss of function → systemic Mn overload + polycythaemia + cirrhosis |
| ***SLC39A14*** (ZIP14) | **HGNC:20858** | 617013 (HMNDYT2) | Mn **uptake** into hepatocytes/enterocytes *for subsequent excretion* | Loss of function → Mn never reaches the liver for disposal → brain accumulation, **no** liver disease |
| ***SLC39A8*** (ZIP8) | **HGNC:20862** | 616721 (CDG type IIn) | Mn uptake | Loss of function → Mn **deficiency**, congenital disorder of glycosylation — the mirror-image disease |

The *SLC39A14* logic is the counterintuitive one and worth spelling out in the entry: it's an **uptake** transporter whose loss causes **overload**, because the uptake it performs is the first step of the excretion pathway. Break the liver's front door and the metal just circulates.

Landmark papers:
- Tuschl et al., *Am J Hum Genet* 2012 — "Syndrome of hepatic cirrhosis, dystonia, polycythemia, and hypermanganesemia caused by mutations in SLC30A10" (**PMID:22341972**)
- Tuschl et al., *Nat Commun* 2016 — "Mutations in SLC39A14 disrupt manganese homeostasis and cause childhood-onset parkinsonism-dystonia" (**PMID:27231142**)

### Variant characteristics

- **Inheritance:** autosomal recessive for both; "Presence of biallelic pathogenic variants in the SLC30A10 and SLC39A14 genes" is the definite-diagnosis criterion (PMID:40320765).
- **Variant types:** missense, nonsense, frameshift, splice-site, and small indels — the reported spectrum is broad with no single hotspot. Six novel *SLC30A10* variants were reported in a single 10-patient series (Zaki et al., *Clin Genet* 2018).
- **Functional consequence:** loss of function (transport-null or transport-reduced). Note the *SLC30A10* **Thr95Ile** variant, studied specifically because it's a partial-function allele — AAV-mediated hepatic expression of both wild-type and T95I "attenuates manganese excess and other phenotypes in Slc30a10-deficient mice."
- **Origin:** germline. No somatic contribution described.
- **Population frequency:** these are ultra-rare; gnomAD allele frequencies for reported pathogenic variants are ≤10⁻⁵ or absent. Consanguinity is a recurring feature of reported pedigrees (many from Middle Eastern, North African, and South Asian families).
- **Classification:** ACMG/AMP classification is available in ClinVar for a subset; many reported variants remain individually uncurated. Verify each in ClinVar before asserting a class.

### Non-causal genes relevant to acquired manganism

These are transport and modifier genes — the machinery Mn hijacks, not disease genes per se:

| Gene | HGNC | Role |
|---|---|---|
| *SLC11A2* (DMT1) | **hgnc:10908** | Non-specific divalent metal importer; principal Mn²⁺ uptake route; iron-regulated |
| *SLC40A1* (ferroportin) | **HGNC:10909** | Mn efflux |
| *TF* (transferrin) | **hgnc:11740** | Carries Mn³⁺ |
| *TFRC* | **HGNC:11763** | Transferrin receptor — Mn³⁺ entry route |
| *SLC1A2* (GLT-1/EAAT2) | **hgnc:10940** | Astrocytic glutamate transporter — **downregulated by Mn** |
| *SLC1A3* (GLAST/EAAT1) | **HGNC:10941** | Astrocytic glutamate transporter — **downregulated by Mn** |
| *GLUL* (glutamine synthetase) | **hgnc:4341** | Mn-dependent enzyme; the astrocyte's reason for concentrating Mn |
| *PRKN* | **hgnc:8607** | Regulates DMT1; loss facilitates Mn uptake |
| *PARK7* (DJ-1) | **hgnc:16369** | Oxidative-stress sensor; depleted by Mn |
| *ATP13A2* | **hgnc:30213** | Lysosomal Mn sequestration — protective; lost in mutants |
| *SNCA* | **hgnc:11138** | α-synuclein; directly binds Mn |
| *ATP2C1* (SPCA1) | — | Golgi Mn efflux pump |

### Epigenetics

An underdeveloped but real area. Mn exposure alters DNA methylation and histone acetylation; curcumin's protective effect is attributed in part to restoring histone acetylation (Khindri & Maj 2025). A dedicated review exists: "Potential Role of Epigenetic Mechanism in Manganese Induced Neurotoxicity" (PMC4899583). No specific differentially-methylated loci are established as disease markers. **Knowledge gap.**

### Chromosomal abnormalities

None described. Not applicable.

---

## 5. Environmental Information

This is the etiologic core of the disease, so §2 already carries most of it. Consolidated for the KB's `environmental:` block:

| Exposure | ECTO/suggested binding | Effect | Notes |
|---|---|---|---|
| Inhalation of welding fume | **ECTO:7000129** (exposure to welding fume) | TRIGGERS | Dominant modern occupational route |
| Exposure to manganese (generic) | **ECTO:9000946** (exposure to manganese) | TRIGGERS | Parent concept |
| Mn ore mining/milling dust inhalation | No precise ECTO term found — use ECTO:9000946 + `preferred_term` | TRIGGERS | Classic historical route |
| Mn in drinking water (ingestion) | Search ECTO for a water-route term; otherwise ECTO:9000946 | TRIGGERS | Pediatric neurodevelopment; Bouchard 2011 |
| Ambient PM₁₀ Mn near ferroalloy plants | ECTO:9000946 | TRIGGERS | Brescia/Valcamonica; BMD 20–25 ng/m³ |
| Intravenous Mn in parenteral nutrition | No ECTO term; free text | TRIGGERS | Bypasses both gut and, if cholestatic, bile |
| Ephedrone/methcathinone injection (KMnO₄ residue) | No ECTO term; free text | TRIGGERS | Rapid, severe, levodopa-unresponsive |
| MMT in gasoline | ECTO:9000946 | PREDISPOSES | Vehicular emission source |

**Lifestyle factors:** injection drug use is the only strong one. Diet is a weak contributor in people with intact livers (Mn is abundant in tea, nuts, whole grains, leafy greens — and essentially never causes toxicity through that route alone). **Vegetarian/vegan diets** raise Mn intake modestly and lower iron status, which is a plausible-but-unproven combined risk; do not assert it as established.

**Infectious agents:** not applicable. (One caveat worth a line: Mn-exposed workers have increased susceptibility to bacterial pneumonia, so infection is a *consequence* rather than a cause.)

---

## 6. Mechanism / Pathophysiology

### The causal chain — acquired inhalational manganism

**Branch A: the main neurotoxic chain**

1. **Inhalation of Mn-containing fume or dust** deposits Mn in the respiratory tract and — for ultrafine particles — permits direct **olfactory nerve translocation to the brain**, bypassing the blood-brain barrier entirely. *(Direct olfactory translocation is well demonstrated in rodents; in humans it is supported by elevated Mn in olfactory tissue of miners and welders but is an **inferred** contribution to brain burden.)* → **leads to**
2. **Elevated systemic Mn burden**, because inhalation bypasses hepatic first-pass extraction that would otherwise clear ingested Mn into bile. → **leads to**
3. **Mn transport across the blood-brain barrier** via non-specific divalent-metal carriers — DMT1 (SLC11A2), ZIP8, ZIP14, the transferrin/transferrin-receptor route for Mn³⁺, and store-operated/voltage-gated calcium channels. None of these transporters is Mn-specific; Mn is a passenger on iron and zinc machinery. → **leads to**
4. **Preferential accumulation in the globus pallidus and striatum**, with astrocytes as the dominant sink. "Astrocytes accumulate up to 50-fold higher Mn concentrations compared to neurons, serving as the main homeostatic and storage site for this metal, with intracellular Mn concentrations of ~50–75 μM." Pharmacokinetic modelling puts the adverse-effect threshold at **~0.55 μg Mn/g** of pallidal tissue. → **branches into 5a, 5b, 5c**

**Branch A1 — mitochondrial capture and oxidative injury**

5a. **Mn²⁺ is taken up by mitochondria through the calcium uniporter and retained there**, because mitochondrial Mn efflux is slow. → **results in** inhibition of oxidative phosphorylation (complex II/III), collapse of membrane potential (GO:0051882, mitochondrial depolarization) → **results in** electron leak and **reactive oxygen species generation** (GO:0072593). Mn³⁺ in particular is a potent oxidant and catalyses dopamine auto-oxidation. → **results in** oxidative stress (GO:0006979, GO:0034599), measured as "increased malondialdehyde (MDA) levels" and "reduced activity of antioxidant enzymes, including glutathione peroxidase, glutathione, and superoxide dismutase" (PMID:40496384) → **results in** further mitochondrial injury, a self-amplifying loop: "Elevated production of ROS can lead to further mitochondrial injury resulting in neurotoxicity."

5a-i. Recent (2024–2025) work extends this to **regulated cell-death programmes**: the **cGAS–STING pathway** senses the resulting damage and drives ROS, apoptosis and **ferroptosis** (GO:0097707) — "Inhibition of either the cGAS-STING pathway or reactive oxygen species (ROS) significantly ameliorated manganese-induced oxidative stress, apoptosis, and ferroptosis" (PMID:40652697). A parallel line implicates **NCOA4-mediated ferritinophagy** releasing free iron into the lipid-peroxidation cascade (PMID:41043778). *These are in vitro/mouse findings, not human-validated.*

**Branch A2 — astrocytic glutamate handling failure (excitotoxicity)**

5b. **Mn accumulating in astrocytes downregulates the glutamate transporters GLT-1 (SLC1A2) and GLAST (SLC1A3)** at both mRNA and protein level, and inhibits glutamine synthetase and Na⁺/K⁺-ATPase. Mechanism runs through **protein kinase C signalling** and the transcription factor **YY1** (PMID:25128239). → **results in** failure of synaptic glutamate clearance → **results in** extracellular glutamate accumulation → **results in** **excitotoxic injury** to pallidal and striatal neurons.

This is, to my eye, the most elegant part of the story: the astrocyte concentrates Mn *because* glutamine synthetase needs it, and that same concentration then poisons the very transporter system that keeps glutamate out of the synapse. The cell's own nutrient logistics hand the toxin its target. (Riluzole, which protects those transporters, is protective in cultured astrocytes — PMID:22391793.)

**Branch A3 — protein misfolding and proteostatic failure**

5c. **Mn binds α-synuclein at three C-terminal residues**, and "low concentrations of Mn are sufficient to induce α-synuclein fibril formation" (PMID:37627255). In parallel, Mn induces **ER stress** and the unfolded protein response (GO:0030968), activates the **EIF2α-PERK** axis, and impairs **autophagy-lysosome** function (GO:0006914) and **mitophagy** (GO:0000423) — the latter partly via **S-nitrosylation of PINK1** and disruption of PINK1/Parkin signalling. → **results in** accumulation of misfolded protein. Human corroboration: in welders' serum exosomes, researchers found "increased misfolded α-synuclein in these workers as compared to non-exposed controls."

**Branch A4 — neuroinflammation**

5d. Mn activates **microglia** (GO:0001774) and drives astrocytes toward the **A1 reactive phenotype** (GO:0048143), via **cGAS–STING → NLRP3 → p38 MAPK/NF-κB** signalling. → **results in** cytokine release, a neuroinflammatory response (GO:0150076) that feeds back onto steps 5a–5c.

**Convergence:**

6. **Neuronal dysfunction and loss in the globus pallidus (especially GPi) and striatum**, plus reduced GABAergic and glutamatergic markers, and reduced striatal **D2 receptor** density — but with **presynaptic dopaminergic terminals structurally preserved**. → **leads to**
7. **Disinhibition/derangement of basal ganglia output**, without nigrostriatal dopaminergic denervation. → **leads to**
8. **The clinical syndrome**: symmetric bradykinesia, rigidity, dystonia, early postural instability, cock-walk gait, dysarthria — **and levodopa unresponsiveness**, because the lesion is *downstream* of the dopamine synapse. There's nothing wrong with the dopamine supply; the wiring that dopamine talks to is what's damaged. Giving levodopa is refilling a tank whose fuel line is fine and whose engine is not.

**Branch B: chronic low-level exposure** diverges at step 4. Here the target territory expands to the whole basal ganglia including SNpc; PET shows "impaired FDOPA uptake in the striatum" in pre-symptomatic welders, and patients "may respond to L-DOPA treatment, contradicting historical diagnostic criteria" (PMID:37627255). This branch is where Mn plausibly interacts with genuine PD risk, and where the α-synuclein mechanism matters most.

**Branch C: inherited hypermanganesaemia** enters the chain at step 2 with no external exposure at all — loss of *SLC30A10* (efflux) or *SLC39A14* (hepatic uptake for excretion) means dietary Mn is never disposed of. Everything from step 3 onward is shared. HMNDYT1 additionally produces **cirrhosis** (Mn hepatotoxicity) and **polycythaemia** (Mn stimulates erythropoietin — an inferred mechanism, still incompletely worked out).

### Suggested GO / CL / UBERON / CHEBI bindings

**Biological processes (GO)** — all verified present in the repo's term cache:

| Process | GO ID | Suggested modifier |
|---|---|---|
| response to oxidative stress | GO:0006979 | INCREASED |
| cellular response to oxidative stress | GO:0034599 | INCREASED |
| reactive oxygen species metabolic process | GO:0072593 | INCREASED |
| mitochondrial depolarization | GO:0051882 | INCREASED |
| mitophagy | GO:0000423 | DECREASED |
| autophagy | GO:0006914 | DECREASED |
| endoplasmic reticulum unfolded protein response | GO:0030968 | INCREASED |
| protein folding | GO:0006457 | DECREASED |
| L-glutamate import across plasma membrane | GO:0098712 | DECREASED |
| glutamate secretion | GO:0014047 | INCREASED |
| neuroinflammatory response | GO:0150076 | INCREASED |
| astrocyte activation | GO:0048143 | INCREASED |
| microglial cell activation | GO:0001774 | INCREASED |
| inflammatory response | GO:0006954 | INCREASED |
| ferroptosis | GO:0097707 | INCREASED |
| apoptotic process | GO:0006915 | INCREASED |
| regulation of neuron apoptotic process | GO:0043523 | INCREASED |
| dopamine metabolic process | GO:0042417 | ALTERED/INCREASED (auto-oxidation) |

Also worth binding if present after a cache seed: *manganese ion transmembrane transport*, *manganese ion homeostasis*, *glutamate-ammonia ligase activity* (glutamine synthetase), *positive regulation of NF-kappaB transcription factor activity*. These were **not** in the local cache and will need seeding before they validate.

**Cell types (CL)** — verified in cache:
- **CL:0000127** astrocyte — *the* primary Mn sink; 50-fold enrichment over neurons
- **CL:0000129** microglial cell — neuroinflammation
- **CL:1001474** medium spiny neuron — striatal target
- **CL:0000617** GABAergic neuron — pallidal output neurons
- **CL:0000700** dopaminergic neuron — relevant to Branch B only
- **CL:0000182** hepatocyte — Mn excretion; HMNDYT1 target
- **CL:0000584** enterocyte — Mn absorption/excretion
- **CL:0000540** neuron (generic)

**Anatomy (UBERON)** — verified in cache:
- **UBERON:0001875** globus pallidus (primary)
- **UBERON:0002435** striatum · **UBERON:0001874** putamen · **UBERON:0001873** caudate nucleus
- **UBERON:0002420** basal ganglion
- **UBERON:0002038** substantia nigra (Branch B; spared in classic manganism)
- **UBERON:0002132** dentate nucleus (inherited forms)
- **UBERON:0002107** liver · **UBERON:0002048** lung · **UBERON:0000955** brain

**Chemicals (CHEBI)**:
- **CHEBI:18291** manganese atom · **CHEBI:25154** manganese molecular entity · **CHEBI:29035** manganese(2+)
- **CHEBI:18243** dopamine · **CHEBI:29033** iron(2+)
- **CHEBI:15765** L-dopa · **CHEBI:27565** 4-aminosalicylic acid · **CHEBI:2618** amantadine · **CHEBI:63623** succimer
- *(Manganese CHEBI terms are **not** in the local cache and will need seeding.)*

### Molecular profiling

- **Proteomics:** "Manganese exposure causes movement deficit and changes in the protein profile of the external globus pallidus in Sprague Dawley rats" (*Toxicol Ind Health* 2021) — a directly relevant tissue proteomics dataset.
- **Transcriptomics:** multiple GEO series exist for MnCl₂-treated SH-SY5Y, primary astrocytes, and mouse brain; none is a canonical reference dataset. Search GEO for "manganese neurotoxicity" before asserting an accession — **do not guess accessions**.
- **Metabolomics/lipidomics:** sparse. The ferroptosis work implies lipid-peroxidation signatures but published lipidomics is thin. **Knowledge gap.**
- **Single-cell / spatial:** no published single-cell atlas of the Mn-exposed basal ganglia that I could find. Given the astrocyte-neuron division of labour is the central mechanistic question, this is arguably the most valuable missing dataset in the whole field. **Knowledge gap worth recording explicitly.**
- **Functional genomics screens:** no published CRISPR screen for Mn-toxicity modifiers located. **Knowledge gap.**

---

## 7. Anatomical Structures Affected

**Organ level**
- **Primary:** brain (UBERON:0000955) — specifically the basal ganglia
- **Secondary:** liver (UBERON:0002107) — target in HMNDYT1 and in Mn hepatotoxicity generally; lung (UBERON:0002048) — pneumonitis, infection susceptibility from inhalational exposure; thyroid — established in mouse models ("Elevated thyroid manganese reduces thyroid iodine to induce hypothyroidism in mice, but not rats, lacking SLC30A10 transporter") but **not confirmed as a human phenotype** — flag the species divergence; bone marrow / erythropoiesis — polycythaemia in HMNDYT1
- **Systems:** nervous (central, extrapyramidal) primary; hepatobiliary, respiratory, haematopoietic secondary

**Regional, in rough order of Mn accumulation**
1. **Globus pallidus** (UBERON:0001875), internal segment worst — the signature site
2. Striatum / putamen / caudate (UBERON:0002435 / :0001874 / :0001873)
3. Subthalamic nucleus
4. Substantia nigra pars reticulata; SNpc involved in chronic low-level exposure but **spared** in classic manganism
5. Dentate nucleus (UBERON:0002132) — prominent in inherited forms
6. White matter and dorsal pons — inherited forms
7. Adenohypophysis — described in portosystemic-shunt cases
8. Frontal cortex — α-synuclein aggregation in non-human primates (PMID:23262390)

**A diagnostically useful negative:** the **ventral pons is spared** in HMNDYT1/2, and that sparing pattern is called out as characteristic in the 2025 consensus (PMID:40320765). Negative findings are underused in KBs; this one is basically a fingerprint.

**Tissue/cell level:** grey matter of the basal ganglia; astrocytes as the storage compartment; GABAergic pallidal projection neurons and striatal medium spiny neurons as the injured population. Neuronal loss with **astrogliosis** (Alzheimer type II astrocytes in the hepatic form), **no Lewy bodies**, no neurofibrillary tangles.

**Subcellular (GO Cellular Component):** mitochondrion (the principal Mn sink within the cell; GO:0005739), Golgi apparatus (SPCA1-mediated Mn handling; GO:0005794), lysosome (ATP13A2-mediated sequestration; GO:0005764), endoplasmic reticulum (ER stress; GO:0005783). *Verify these CC IDs against the ontology before binding — they were not checked against the local cache.*

**Localization:** **bilateral and symmetric** — a defining feature. Idiopathic PD is characteristically asymmetric at onset; manganism is not. This is a first-line clinical discriminator.

---

## 8. Temporal Development

**Onset**
- Occupational: adult, typically after **months to years** of exposure; insidious. The Iranian automotive cohort reported parkinsonism after a mean cumulative exposure of 3.34 mg/m³ over 12.30 years.
- Ephedrone: **months** — rapid and severe.
- TPN-associated: weeks to months of infusion, especially with cholestasis.
- HMNDYT2: "Mean age of onset of 1 year and 9 months old with all but two patients presenting before or at the age of five" (PMID:40320765).
- HMNDYT1: childhood, generally later than HMNDYT2, and more variable — some present in adulthood with liver disease.

**Stages (classical description)**
1. **Prodromal / neuropsychiatric** — headache, fatigue, irritability, emotional lability, insomnia, compulsive behaviour, hallucinations. Often reversible.
2. **Intermediate** — emerging motor signs: clumsiness, speech change, micrographia, mild bradykinesia.
3. **Established extrapyramidal** — bradykinesia, rigidity, dystonia, cock-walk gait, postural instability, falls.
4. **Advanced/fixed** — severe dystonia, dysarthria/anarthria, dysphagia, wheelchair dependence.

**Progression rate:** slow and dose-dependent in occupational exposure — "Progression of parkinsonism increased with cumulative Mn exposure" in a longitudinal cohort of 886 welders (Racette et al., *Neurology* 2017, **PMID:28031394**). Rapid in ephedrone toxicity and in HMNDYT2 ("rapidly progressive dystonia-parkinsonism").

**Course pattern:** progressive during exposure. After cessation, the picture is genuinely mixed and this is one of the field's live arguments:
- Some patients improve, and imaging normalises: "Symptoms and brain MRI abnormalities can fully resolve after cessation of manganese exposure."
- Others progress *after* removal from exposure — the phenomenon that motivated the "Neuromythology of Manganism" critique of the simple-reversibility story (*Curr Epidemiol Rep* 2015).
- Dystonia and cognitive deficits are the components least likely to remit.

**Duration:** self-limited to chronic-lifelong, depending on when exposure stopped. The inherited forms are lifelong and require indefinite treatment.

**Critical periods / intervention windows**
- **The single most consistent prognostic message in the literature is early treatment.** "The benefits of chelation therapy, such as with CaNa₂EDTA, are less effective in patients who are treated after more extended periods of exposure." The paired-sibling observation is stark: "the 3-year-old patient had a significant reduction in motor symptoms with CaNa₂EDTA, but the 17-year-old's condition continued to worsen" (PMID:40496384).
- **Developmental window:** the neurodevelopmental meta-analysis found effects concentrated in "children under 6 years of age" (PMID:33008482).
- **Biological half-life:** Mn clears from blood over weeks (whole-body biological half-life on the order of weeks-to-a-month), but **brain Mn clears far more slowly than blood Mn** — which is exactly why a normal blood level does not exclude the diagnosis. Treat any specific half-life figure as approximate unless you pin a primary pharmacokinetic source.

---

## 9. Inheritance and Population

### Epidemiology — acquired manganism

There is **no population prevalence or incidence estimate** for manganism as such. Orphanet lists manganese poisoning (ORPHA:306682) without a usable prevalence class. What exists instead is prevalence *of parkinsonism within exposed occupational cohorts*, which is a different quantity and should be curated as such:

| Cohort | Finding | Source |
|---|---|---|
| Alabama welders (n=1,423 screened) | **15.6%** parkinsonism prevalence vs **0%** in reference group | Racette et al., *Neurology* 2005, **PMID:15668418** |
| South African Mn miners (n=418) | **29.4%** parkinsonism prevalence | via Lucchini & Tieu 2023 |
| Iranian automotive/foundry workers | **42%** parkinsonism; cumulative 3.34 mg/m³ over 12.30 y | via Lucchini & Tieu 2023 |
| Tehran foundry workers | **33.7%** parkinsonism on neurological examination | PMC9526798 |
| US welding trade-union cohort | 886 workers, 1,492 exams; 398 with 606 follow-ups to 9.9 y | Racette et al. 2017, **PMID:28031394** |

For dismech's structured `prevalence:` slots, these are best modelled as `POINT_PREVALENCE` in an occupationally defined `population:` (e.g. "Alabama welders, 2005 cross-sectional screen"), with `rate_per_100000: 15600` — **not** as a general-population figure. Do not let an occupational-cohort number leak into a `Worldwide` population record; that would be a factual error of a kind that's very hard to spot downstream.

Metal-exposure meta-analysis for PD risk: pooled OR ≈ **1.04** for occupational/environmental Mn and Parkinson disease (*Am J Epidemiol* 2023) — i.e. essentially null for *PD*, which is not the same claim as Mn causing *manganism*. Keep those two claims separate in the entry; conflating them is the commonest error in this literature.

### Epidemiology — inherited forms

Precise, because the entire world literature is enumerable:

> "A total of 98 individuals have been identified, 60 affected by HMNDYT1 and 33 by HMNDYT2. A further five patients with characteristic manganese neurotoxicity remain genetically undetermined." — as of January 2025 (**PMID:40320765**)

Prevalence class: `BELOW_1_IN_1000000` / ULTRA_RARE. Measure type: `CASES_IN_LITERATURE` with value 98 (60 + 33 + 5 undetermined).

### Inheritance (genetic forms only)

- **Pattern:** autosomal recessive (both HMNDYT1 and HMNDYT2).
- **Penetrance:** appears complete for biallelic null variants; variable age of onset. Heterozygotes are generally unaffected in isolation but may be **susceptible** to acquired manganism under exposure — model as `relationship_type: SUSCEPTIBILITY` for the heterozygous state, distinct from the `CAUSATIVE` biallelic state.
- **Expressivity:** variable, particularly for the hepatic component of HMNDYT1 (some patients present with liver disease, some with neurology).
- **Anticipation:** not applicable — no repeat expansion.
- **Germline mosaicism:** not described.
- **Founder effects:** none formally established; reported pedigrees cluster in consanguineous populations (Middle East, North Africa, South Asia, Roma communities), which reflects consanguinity rather than a founder allele.
- **Consanguinity:** a strong and repeatedly noted feature.
- **Carrier frequency:** not established. gnomAD-based estimates would be speculative — **do not assert one**.

### Demographics (acquired)

- **Sex ratio:** heavily male in occupational series (approximately 9:1 or more in welding/mining cohorts), driven entirely by workforce composition rather than biological susceptibility. Animal data suggest oestrogen may be protective, which would push the true biological ratio in the same direction but by an unquantified amount.
- **Age:** working-age adults (25–65) for occupational; infants/children for TPN and inherited forms; young adults for ephedrone.
- **Geography:** wherever Mn mining, ferroalloy smelting or heavy welding occurs — historically Chile (the Chiatura and Moanda mines, the classic Chilean miner series), Georgia, South Africa, China, Brazil, Italy (Valcamonica/Brescia), India. Ephedrone manganism clusters in Latvia, Russia, Georgia, Poland, Czechia. Mn-rich groundwater is a distinct geography again: Bangladesh, Quebec, parts of the US upper Midwest and New England.

---

## 10. Diagnostics

Manganism is a **clinical + exposure + imaging** diagnosis. No single test is definitive.

### Laboratory

| Test | Reference range | Utility |
|---|---|---|
| **Whole blood Mn** | **7–12 µg/L** (PMID:40496384) | Best available biomarker; reflects recent exposure |
| **Serum Mn** | **0.6–4.3 µg/L** | Less reliable than whole blood |
| Urinary Mn | Low; poor correlate | Weak — Mn is excreted in bile, not urine |
| Hair Mn | — | Used epidemiologically (the IQ meta-analysis used it); contamination-prone |
| Serum ferritin, TIBC, iron studies | — | Low ferritin / raised TIBC characteristic of HMNDYT1; also modifies risk |
| Full blood count | — | Polycythaemia in HMNDYT1 |
| Liver function tests | — | HMNDYT1; also identifies the hepatic etiology |

**The critical caveat**, and one that catches clinicians out: a normal blood Mn **does not exclude** the disease. Brain Mn outlasts blood Mn by a long margin, and the consensus statement says outright that "blood manganese in both HMNDYT1 and HMNDYT2…can be normal, particularly in adulthood."

LOINC coverage exists for blood and serum manganese; look up the exact codes rather than guessing — I did not verify specific LOINC identifiers.

### Imaging — the workhorse

**Brain MRI, T1-weighted, without contrast.** Mn is paramagnetic and shortens T1, so it lights up bright without any contrast agent — the metal is its own contrast.

- **Bilateral symmetric T1 hyperintensity of the globus pallidus** is the signature finding.
- Extension to putamen, caudate, subthalamic nucleus, substantia nigra, dentate nucleus, and white matter with greater burden.
- **Sparing of the ventral pons** in the inherited forms (PMID:40320765) — a discriminating feature.
- Corresponding **T2 hypointensity** may be seen.
- **Pallidal index** (ratio of pallidal to frontal white-matter T1 signal ×100) is the semi-quantitative measure used in the occupational literature.
- MRI is also the **treatment-monitoring** tool: "Over 9 years of treatment with Na₂CaEDTA, T1 hyperintensity on MRI brain had much improved confirming successful removal of manganese."
- NCIT for the procedure: **NCIT:C16809** (Magnetic Resonance Imaging).

**DAT-SPECT / ¹⁸F-FDOPA PET** — the key differential test:
> Mn-exposed workers demonstrate "normal [18F]-fluorodopa PET, normal DAT SPECT and a decrease in D2 receptor levels," reflecting "absence of nigrostriatal dopamine neuron degeneration in occupationally Mn-induced parkinsonism." (PMID:26154659)

Normal DAT imaging in a patient with parkinsonism is the finding that should make you think manganism (or another non-degenerative parkinsonism). Note the caveat from Branch B: chronic low-level exposure *can* impair FDOPA uptake pre-symptomatically, so a normal scan supports but doesn't guarantee the classic picture.

**Advanced/emerging:** Diffusion Basis Spectrum Imaging (DBSI) revealed "neuroinflammation in white matter and signs of swelling in the caudate nucleus linked with increased manganese and parkinsonism" (PMID:40496384) — a research technique, not clinical practice.

### Functional / electrophysiology
- **UPDRS Part III (motor)** is the standard quantitative instrument across the occupational cohorts.
- Neuropsychological batteries for the cognitive/psychiatric phase.
- EEG, EMG and nerve conduction are generally normal — useful chiefly to exclude alternatives.

### Genetic testing
- Indicated for **any childhood-onset dystonia-parkinsonism with basal ganglia T1 hyperintensity**, and for any adult with hypermanganesaemia without an exposure source.
- Targeted single-gene or panel testing of ***SLC30A10*** and ***SLC39A14*** first; consider *SLC39A8* in the deficiency/CDG phenotype.
- WES/WGS appropriate when panel-negative. NCIT:C15240 (Genetic Counseling) applies.
- Definite diagnosis = "Presence of biallelic pathogenic variants in the SLC30A10 and SLC39A14 genes."
- Chromosomal microarray, karyotype, FISH, mtDNA and repeat-expansion testing: **not indicated**.

### Diagnostic criteria (inherited forms, from the 2025 consensus)
- **Probable:** CNS involvement + raised blood manganese + pathognomonic MRI. For HMNDYT1, additionally polycythaemia, liver disease, and depleted iron stores.
- **Definite:** biallelic pathogenic variants.

For acquired manganism there is **no validated consensus criteria set** — diagnosis rests on documented exposure + compatible syndrome + compatible MRI + exclusion of alternatives. This absence is itself worth curating as a knowledge gap.

### Differential diagnosis

| Condition | Distinguishing features |
|---|---|
| **Idiopathic Parkinson disease** | Asymmetric onset, rest tremor, levodopa-responsive, abnormal DAT scan, normal MRI, Lewy bodies |
| **Wilson disease** | Kayser-Fleischer rings, low ceruloplasmin, high urinary copper, T2 changes |
| **Progressive supranuclear palsy** | Vertical gaze palsy, early falls, midbrain atrophy ("hummingbird") |
| **Multiple system atrophy** | Autonomic failure, cerebellar signs, "hot cross bun" pons |
| **Acquired hepatocerebral degeneration** | Overlaps *heavily* — is often Mn-mediated; look for cirrhosis/shunt |
| **NBIA (PKAN etc.)** | "Eye of the tiger" sign; iron not manganese |
| **Drug-induced parkinsonism** | Neuroleptic exposure history; normal MRI |
| **Vascular parkinsonism** | Lower-body predominance, white matter disease on MRI |
| **Carbon monoxide / methanol poisoning** | Bilateral pallidal/putaminal **necrosis** — T2 bright, not T1 bright |
| **HMNDYT1/2** | Childhood onset, no exposure, biallelic variants, ± polycythaemia/cirrhosis |

The CO-poisoning row is worth a curator's attention: it hits the same anatomy but with the **opposite MRI signature** (T2-hyperintense necrosis vs T1-hyperintense metal deposition). Same neighbourhood, entirely different burglary.

### Screening
- **Occupational surveillance:** periodic air monitoring against the ACGIH TLV, plus symptom questionnaires and UPDRS-based neurological screening in Mn-exposed workforces. No validated screening protocol has been formally adopted, which given a 15.6% cohort prevalence is a notable public-health gap.
- **Cascade testing** of siblings in HMNDYT1/2 families — high-value because **presymptomatic chelation is the best-outcome scenario**.
- **Newborn screening:** not performed and not currently proposed.
- **TPN patients:** monitor whole-blood Mn and consider periodic MRI on long-term PN, particularly with cholestasis.

---

## 11. Outcome / Prognosis

**Mortality:** manganism is not directly fatal. Deaths in affected populations follow from advanced disability (aspiration from dysphagia, falls) or from the underlying etiology — cirrhosis in HMNDYT1, liver failure in the hepatic form, complications of injection drug use in ephedrone cases. No disease-specific mortality rate exists. **Knowledge gap.**

**Life expectancy:** essentially normal in isolated occupational manganism. Reduced in HMNDYT1 by liver disease; historically, untreated HMNDYT1/2 carried substantial early mortality, which chelation appears to change ("halt of liver disease progression").

**Morbidity and function:** the burden is motor disability — gait impairment, falls, loss of employment, progression to wheelchair dependence in severe cases. In the ephedrone series, 11 of 23 patients were falling daily and one used a wheelchair. Communication is impaired by dysarthria. The genetic forms produce "severe motor disability" with preserved cognition, which is its own particular cruelty: the patient is fully present inside a body that won't cooperate.

**Recovery potential**
- **Early, exposure removed:** good — psychiatric symptoms and MRI changes may fully resolve.
- **Established motor disease:** partial at best. "Persistent dystonia and cognitive impairment may not fully resolve despite successful manganese reduction."
- **After long exposure:** may progress despite removal — the observation that undermines the "manganism is reversible" simplification.
- **With early chelation (inherited forms):** substantial — "Chelation therapy has been shown to effectively reduce brain manganese deposition in both HMNDYT1 and HMNDYT2, which is accompanied by improvement in neurological symptoms and halt of liver disease progression."

**Prognostic factors**
1. **Time from onset to treatment** — the strongest and most consistently reported factor.
2. **Age at treatment** — the 3-year-old improved, the 17-year-old did not (PMID:40496384).
3. **Cumulative exposure dose** — drives progression rate (PMID:28031394).
4. Whether exposure has actually stopped.
5. Presence of established dystonia (worse) vs pure bradykinesia (better).
6. In HMNDYT1, degree of liver disease at diagnosis.

**Prognostic biomarkers:** blood Mn (imperfect — normalises before the brain does) and **MRI pallidal signal / pallidal index**, which is the more informative marker for body burden and treatment response. No molecular prognostic biomarker exists. **Knowledge gap.**

---

## 12. Treatment

### First and most important: stop the exposure

Removal from the exposure source is the primary intervention and precedes everything else. In TPN-associated cases, simply withdrawing Mn supplementation resolves symptoms in children. In occupational cases, job modification or removal. NCIT: this is an environmental/administrative intervention rather than a clinical action term; model it as an environmental factor removal rather than forcing an NCIT treatment term.

### Chelation therapy — the mainstay for the inherited forms

**Disodium calcium edetate (Na₂CaEDTA / CaNa₂EDTA)** is the recommended agent.

> "All patients with symptomatic HMNDYT1 and HMNDYT2 should be offered chelation therapy if locally available" (**PMID:40320765**)

Regimen from the consensus:
- "20 mg/kg/dose made up in 250 mL of 0.9% sodium chloride…over 1 h"
- Monthly five-day courses, **or** weekly single infusions; "adjusted to clinical response and patient preference"
- Alternative acquired-disease regimen: "Intravenous CaNa₂EDTA twice daily for 20 mg/kg for 5 days" for initial assessment, then monthly 5-day courses (PMID:40496384)
- Documented effect: serum Mn fell "from 222.9 µg/L to a stable range of 37.5 µg/L to 41.9 µg/L"

**Monitoring during chelation** (chelators are not selective — they strip essential metals too): FBC, renal function, proteinuria, electrolytes, Ca, Mg, phosphate, **Cu and Zn**, and annual thyroid function.

Suggested dismech encoding:
```
treatment_term: NCIT:C15986 (Pharmacotherapy)
therapeutic_agent: NCIT:C334 (Edetate Calcium Disodium)
therapeutic_modality: SMALL_MOLECULE
```
Note: OLS4 returns **no exact NCIT "Chelation Therapy" clinical-action term** — closest are NCIT:C360 (Chelating Agent) and NCIT:C40516 (Iron Chelation), neither of which is a `NCIT:C25218`-rooted clinical action. Use Pharmacotherapy + the agent, and carry "chelation therapy" in `preferred_term`.

**Alternative chelators** (limited evidence, "if Na₂CaEDTA is unavailable or not tolerated"): D-penicillamine, DMSA/succimer (CHEBI:63623), para-aminosalicylic acid, trientine.

**Para-aminosalicylic acid (PAS)** deserves its own line. It's an old anti-tuberculous drug that chelates Mn²⁺ and, unlike EDTA, crosses into the CNS:

> Jiang et al. treated a 50-year-old woman with 21 years of airborne Mn exposure: "She received 6 g PAS per day through an intravenous drip infusion for 4 days and rested for 3 days as one therapeutic course, with fifteen such courses…At the end of PAS treatment, her symptoms were significantly alleviated, and handwriting recovered to normal." Reexamined 17 years later with sustained benefit. — *J Occup Environ Med* 2006 (**PMID:16766929**)

That's a single case with 17-year follow-up — landmark but n=1. Supported by rat chelation studies (PMID:19150464). CHEBI:27565 (4-aminosalicylic acid).

### Iron supplementation (HMNDYT1)

> "All patients with HMNDYT1 should be treated with iron supplementation aiming for a normal iron profile" (**PMID:40320765**)

Mechanism: iron and Mn compete for DMT1, so restoring iron status reduces Mn absorption. Monitor iron parameters every 3 months to avoid overload. This is a genuinely elegant therapy — you're not removing the toxin, you're re-occupying the door it comes in through.

Encoding: `treatment_term: NCIT:C15433` (Nutritional Support) or Pharmacotherapy + an iron `therapeutic_agent`; **do not** mechanically tag as `BEHAVIORAL` — per the repo's own guidance, nutritional-support terms usually name a specific compound, and here the modality is `SMALL_MOLECULE`.

### Therapeutic plasma exchange

Reported in combination with chelation for rapid reduction: "blood manganese levels dropped from 46 μg/dL to 22 μg/dL" after 2 days of TPE alone in a pediatric case (PMID:40496384). NCIT:C15304 (Plasmapheresis). Evidence level: case report.

### Phlebotomy (HMNDYT1)

"Consider…if Hct > 65–70," though the consensus notes no thromboembolic events have been documented. NCIT:C28221 (Phlebotomy).

### Symptomatic dopaminergic therapy

**Levodopa** (CHEBI:15765) — the classical teaching is that it does not work, and that non-response is diagnostic. Two qualifications:
1. It may give temporary symptomatic relief in some patients: "Levodopa provides temporary motor symptom relief but does not address underlying manganese toxicity."
2. In chronic low-level exposure with SNpc involvement, response can occur — "Patients may respond to L-DOPA treatment, contradicting historical diagnostic criteria" (PMID:37627255).

So the entry should record levodopa non-response as a **strong but not absolute** discriminator, with `supports: SUPPORT, directness: INDIRECT` on the diagnostic-criterion claim and a `REFUTE`-graded item for the chronic-exposure counterexample. That's exactly the two-items-not-one situation the evidence SOP describes.

Other symptomatic agents used with limited evidence: amantadine (CHEBI:2618), anticholinergics (trihexyphenidyl) for dystonia, botulinum toxin for focal dystonia, baclofen for spasticity.

### Liver transplantation

Curative for HMNDYT1 in principle (it replaces the *SLC30A10*-deficient hepatocytes), and indicated for end-stage cirrhosis. NCIT:C15271 (Liver Transplantation). Evidence: case-level.

### Deep brain stimulation

NCIT:C21024. Rarely reported; because the lesion **is** the pallidum, GPi-DBS is mechanistically questionable in a way it isn't for PD. Insufficient evidence — do not present as an established option.

### Supportive and rehabilitative

- Physical therapy (NCIT:C15302), occupational therapy (NCIT:C121351), speech and swallowing therapy, rehabilitation (NCIT:C15315) — all `therapeutic_modality: BEHAVIORAL`.
- Supportive care (NCIT:C15747); psychiatric management of the neuropsychiatric phase.
- Genetic counselling (NCIT:C15240) for HMNDYT1/2 families.

### Experimental / preclinical

No registered interventional trials for manganism located on ClinicalTrials.gov. **Search and record specific NCT identifiers before asserting any — I did not find any to cite, and inventing one would be worse than recording the absence.**

Preclinical neuroprotectants (all animal or in vitro; **none clinically validated**): vinpocetine, punicalagin, niacin + vitamin E combination, curcumin (restores histone acetylation and antioxidant pathways), resveratrol (SIRT1 activation), sesame oil (restored GABA and dopamine levels in rats), *Dendrobium nobile* alkaloids (restore PINK1/Parkin), *Echium amoenum* extract, riluzole (protects astrocytic glutamate transporters). Also mechanistically implied by the 2024–25 work: cGAS-STING inhibition and ferroptosis inhibition.

### Treatment outcomes and adverse events

Response is best measured by MRI signal normalisation plus clinical rating scales. Chelation adverse effects: nephrotoxicity/proteinuria, depletion of essential metals (Zn, Cu), electrolyte disturbance, infusion reactions. The consensus's own honest caveat should be carried into the entry: "evidence for the recommendations is based on observational studies and expert opinions, representing low-level quality evidence."

### Treatment algorithm (synthesised)

1. Identify and **remove the exposure** (or treat the liver/shunt).
2. Confirm with whole-blood Mn + T1 MRI; obtain DAT imaging if PD is in the differential.
3. Genetic testing if childhood-onset or no identifiable exposure.
4. **Symptomatic + confirmed overload → chelation** with Na₂CaEDTA, started as early as possible.
5. **HMNDYT1 → add iron supplementation**; consider phlebotomy for Hct > 65–70; monitor liver.
6. Symptomatic therapy (trial levodopa; anticholinergics/botulinum for dystonia).
7. Rehabilitation, speech and swallow support.
8. Monitor: blood Mn, FBC, LFTs, iron studies, renal function, Cu/Zn, serial MRI, movement-disorder rating scales with video.

---

## 13. Prevention

Prevention is where this disease is genuinely, unusually tractable — the exposure is identifiable, measurable, and engineerable. Manganism is close to a fully preventable disease that we keep not preventing.

**Primary**
- **Engineering controls:** local exhaust ventilation, fume extraction at the arc, enclosed processes, wet methods for dust suppression. First-line and most effective.
- **Substitution:** low-Mn consumables and welding processes producing less fume (e.g., preferring processes with lower fume-generation rates where the joint permits).
- **Respiratory protection:** powered air-purifying respirators for welders where controls are insufficient.
- **Adopt the ACGIH TLV (0.02 mg/m³ respirable) rather than the OSHA PEL** as the operational target — the PEL is 250× higher and not protective.
- **Drinking water:** treatment/removal for Mn-rich groundwater; WHO and national guideline values apply. Point-of-use filtration for private wells.
- **Phase-out of MMT** as a fuel additive.
- **TPN protocols:** Mn ≤ 0.018 µmol/kg/24 h in children; omit Mn entirely in cholestasis; periodic monitoring.
- **Maintain adequate iron status** in exposed workers — plausible and mechanistically grounded, though not formally trialled as a prevention strategy. Flag as inferred.

**Secondary**
- Occupational medical surveillance: periodic neurological exam, UPDRS-based screening, symptom questionnaires, and blood Mn in exposed workforces.
- **Cascade genetic testing** in HMNDYT1/2 families with presymptomatic chelation — the highest-yield secondary prevention available for this disease.
- MRI surveillance in long-term PN and in cirrhosis/shunt patients with new neuropsychiatric change.

**Tertiary**
- Chelation to halt progression; iron repletion; falls prevention; swallowing assessment to prevent aspiration; treatment of underlying liver disease.

**Genetic counselling:** autosomal recessive — 25% recurrence risk per pregnancy for carrier couples. Prenatal and preimplantation genetic testing are technically available once the familial variants are known. Carrier testing of relatives is indicated.

**Immunization:** not applicable.

**Public health:** air-quality regulation near ferroalloy and smelting operations; community biomonitoring in Mn-rich regions; worker education; water-quality standards for Mn.

---

## 14. Other Species / Natural Disease

**Taxonomy of affected species (experimental/veterinary):**
- *Homo sapiens* — **NCBITaxon:9606**
- *Mus musculus* — NCBITaxon:10090
- *Rattus norvegicus* — NCBITaxon:10116
- *Macaca fascicularis* (cynomolgus macaque) — NCBITaxon:9541
- *Danio rerio* — NCBITaxon:7955
- *Caenorhabditis elegans* — NCBITaxon:6239

**Naturally occurring disease in other species:** genuinely thin. Manganese toxicosis is described in livestock in the veterinary toxicology literature (largely as a feed/mineral-supplement imbalance causing growth depression and interfering with iron absorption, producing anaemia rather than neurological disease), but **there is no well-characterised naturally occurring animal analogue of manganism**. OMIA does not, to my knowledge, list an inherited Mn transport disorder in a companion or production species — worth a direct OMIA check before asserting either way. No VBO breed association identified.

This is worth recording explicitly rather than leaving blank: it is a **notable absence**, and it means the animal-model evidence for this disease is entirely *induced*, not natural.

**Orthologues:** *Slc30a10*, *Slc39a14*, *Slc39a8*, *Slc11a2* are conserved across vertebrates; the *C. elegans* orthologue *smf-1/2/3* (DMT1 family) is the workhorse for Mn-toxicity genetics in worms. Look up NCBI Gene IDs directly rather than trusting my recall.

**Comparative biology — an important species divergence to record:** *Slc30a10*-null **mice** develop severe hypothyroidism from thyroid Mn accumulation; **rats** with the same deficiency do not, and it is **not** a described human feature. "Elevated thyroid manganese reduces thyroid iodine to induce hypothyroidism in mice, but not rats, lacking SLC30A10 transporter" (*Metallomics* 2024). This is a textbook `HUMAN_MODEL_MISMATCH` candidate.

**Evolutionary conservation:** Mn homeostasis machinery (SLC30/SLC39 families, the Golgi SPCA pump, Mn-SOD) is deeply conserved from yeast upward, which is why yeast and worm screens are informative here.

**Zoonotic potential / transmission:** not applicable — this is a toxicosis, not a transmissible disease.

---

## 15. Model Organisms

### Genetic models (the strongest ones)

**Slc39a14⁻/⁻ mouse** — the best available model of HMNDYT2.
> "Loss of SLC39A14 results in markedly elevated manganese concentrations in the blood, bone, heart, kidney, and brain, and is associated with motor deficits" — and critically, those deficits "can be rescued by treatment with the metal chelator Na₂CaEDTA." (Jenkitkasemwong et al., *PNAS* 2018, **PMID:29437953**; see also Xin et al., *Cell Discov* 2017)

`relationship: RECAPITULATES`, `fidelity: HIGH` — it reproduces the biochemistry, the brain accumulation, the motor phenotype, **and** the therapeutic response. That last point is what makes it a genuinely useful model rather than a phenocopy: the intervention that works in patients works here too.

**Slc30a10⁻/⁻ mouse** — model of HMNDYT1.
- Full-body knockouts "accumulate manganese in the blood and brain and develop neurotoxicity, consistent with the human phenotype."
- Pan-neuronal/glial conditional knockouts "exhibit elevated basal ganglia manganese levels and develop motor deficits in early-life."
- Cell-type-specific work is informative: "Activity of the manganese efflux transporter SLC30A10 in **dopaminergic but not GABAergic neurons** protects against neurotoxicity" (bioRxiv 2022).
- AAV-mediated hepatic re-expression of SLC30A10 (and the T95I variant) rescues the phenotype — a gene-therapy proof of concept.
- **Limitation / `FAILS_TO_RECAPITULATE`:** the severe hypothyroidism seen in mice is not a human feature, and is species-specific (absent in rats).

**Slc30a10/Slc39a14 double knockout** — "euthyroid despite large increases in blood manganese levels," used to dissect tissue-specific transporter roles.

### Induced (exposure) models

**Non-human primate (cynomolgus macaque)** — the highest-fidelity model of the human syndrome, because primate basal ganglia anatomy and MRI signal behave like ours.
- Chronic Mn exposure produces the human MRI signature and behavioural deficits.
- "Manganese exposure induces α-synuclein aggregation in the frontal cortex of non-human primates" (Verina et al., **PMID:23262390**) — increased α-syn-positive pyramidal and medium-sized neurons in deep cortical layers.
- "Postmortem studies in the frontal cortex of Mn-exposed non-human primates have found a significant degree of neuronal degeneration with diffused β-amyloid plaques and α-synuclein aggregation."
- Effects on glutamatergic and GABAergic neurotransmitter markers documented (PMC2726295).
- Limitations: cost, small n, ethical constraints, and exposure regimens (often IV) that don't match human inhalational kinetics.

**Rodent MnCl₂ exposure models** (oral, IP, or inhalational, in mouse and Sprague-Dawley rat) — the workhorses for mechanism. Support the oxidative-stress, glutamate-transporter, neuroinflammation and ferroptosis findings. Limitation: rodents lack a true globus pallidus internus homologue, so the anatomical specificity of the human lesion is poorly modelled — a real translational caveat and a good `limitations:` field entry.

**Cellular models**
- **SH-SY5Y** dopaminergic-like neuroblastoma — the standard for Mn cytotoxicity; used for the BNIP3/mitophagy work (PMC8173824).
- **HT22** hippocampal line — the NCOA4/ferritinophagy ferroptosis work (PMID:41043778).
- **Primary astrocyte cultures** — the glutamate-transporter and glutamine-synthetase mechanism (PMID:22391793, PMID:25128239). Given astrocytes are the actual Mn sink, this is arguably the most physiologically apt in vitro system.
- **CHO-K1 cells transfected with GLAST/GLT-1** — clean transport assays.
- **iPSC-derived neurons/astrocytes and organoids** — the obvious next step and, as far as I found, largely unexploited for manganism. **Knowledge gap and opportunity.**

**Invertebrate**
- ***C. elegans*** — used for Mn × DJ-1 interaction ("the life-span…was reduced after Mn exposure when DJ-1 was deleted") and for *smf* transporter genetics. Cheap, fast, genetically tractable; limited anatomical relevance.
- ***Drosophila*** and **yeast** — used for conserved Mn homeostasis, less for disease phenotype.

### What the models do and don't capture

| Feature | Captured? |
|---|---|
| Brain Mn accumulation | Yes — all models |
| Pallidal T1 MRI signature | Non-human primate; partially rodent |
| Motor deficits | Yes — mouse, primate |
| Chelation response | **Yes** — Slc39a14⁻/⁻ mouse (strong translational validation) |
| Neuropsychiatric prodrome | Poorly — the "manganese madness" phase has essentially no model |
| Cock-walk gait / human dystonia | No |
| Levodopa unresponsiveness | Rarely tested directly — **a real gap** |
| Cognitive sparing with motor devastation | Not modelled |
| Polycythaemia + cirrhosis (HMNDYT1) | Partially in mouse |
| Species-specific artefact | Mouse hypothyroidism (not human, not rat) |

**Resources:** MGI, IMPC, IMSR, JAX (Slc30a10 and Slc39a14 lines), RGD, ZFIN, WormBase, Alliance of Genome Resources, Cellosaurus/ATCC for SH-SY5Y and HT22.

---

## Curation Notes and Cautions

A short list of things I'd want a curator to know before this becomes YAML:

1. **Model manganism, chronic low-level Mn parkinsonism, and the inherited hypermanganesaemias as related but distinct.** MONDO gives you separate terms (MONDO:0017638, MONDO:0013208, MONDO:0014864, plus MONDO:0000214 and MONDO:0017766 as groupers). Collapsing them would flatten a real and clinically consequential distinction — especially the levodopa-response and lesion-location differences.
2. **The occupational prevalence figures (15.6%, 29.4%, 42%, 33.7%) are cohort-conditional**, not population prevalence. Put the cohort in `population:` and never let them stand as a general rate.
3. **Levodopa non-response needs two evidence items**, not one — the classical criterion (SUPPORT) and the chronic-exposure counterexample (REFUTE). Same paper, different sentences, different `supports` values, which is exactly what the split-the-item rule is for.
4. **Terms needing cache seeding before validation:** the manganese CHEBI terms (CHEBI:18291, CHEBI:25154, CHEBI:29035), CHEBI:15765 (L-dopa), CHEBI:27565 (4-aminosalicylic acid), NCIT:C334 (Edetate Calcium Disodium), HGNC:25355 (SLC30A10), HGNC:10909 (SLC40A1), HGNC:10941 (SLC1A3), HGNC:11763 (TFRC), and several GO processes (Mn transport/homeostasis, glutamate-ammonia ligase activity, NF-κB regulation). Everything else listed above was confirmed present in the local caches or in OLS4.
5. **There is no NCIT clinical-action term for "chelation therapy."** Use NCIT:C15986 + `therapeutic_agent: NCIT:C334`.
6. **Do not assert ClinicalTrials.gov NCT identifiers** — I found none for manganism and would rather record the absence than have a plausible-looking fake accession pass validation.
7. **Existing dismech modules likely relevant for `conforms_to`:** run `just list-modules` against oxidative-stress, mitochondrial-dysfunction, neuroinflammation, excitotoxicity, protein-misfolding, and any drug/environmental-toxicity module. This disease is a strong multi-module conformer and probably shouldn't re-derive those chains.
8. **Three explicit knowledge gaps worth curating as `discussions`:** (a) no single-cell atlas of the Mn-exposed basal ganglia despite the astrocyte-neuron division being the central question; (b) no validated diagnostic criteria for acquired manganism; (c) the reversibility controversy — cases that progress after exposure ceases, which the "manganism is reversible" framing doesn't accommodate. And one `HUMAN_MODEL_MISMATCH`: mouse Slc30a10-null hypothyroidism, absent in rats and in humans.

---

## Sources

- [Manganese-Induced Parkinsonism: A Review of Etiologies and Treatments — Khindri & Maj, *Degener Neurol Neuromuscul Dis* 2025 (PMID:40496384)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12151541/)
- [Manganese-Induced Parkinsonism: Evidence from Epidemiological and Experimental Studies — Lucchini & Tieu, *Biomolecules* 2023 (PMID:37627255)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10452806/)
- [Consensus of Expert Opinion for the Diagnosis and Management of Hypermanganesaemia With Dystonia 1 and 2 — Fang et al., *J Inherit Metab Dis* 2025 (PMID:40320765)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12050909/)
- [Manganese-Induced Parkinsonism and Parkinson's Disease: Shared and Distinguishable Features — Kwakye et al., *IJERPH* 2015 (PMID:26154659)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4515672/)
- [The neuropathology of manganese-induced Parkinsonism — Perl & Olanow, *JNEN* 2007 (PMID:17882011)](https://pubmed.ncbi.nlm.nih.gov/17882011/)
- [Dose-dependent progression of parkinsonism in manganese-exposed welders — Racette et al., *Neurology* 2017 (PMID:28031394)](https://www.neurology.org/doi/10.1212/wnl.0000000000003533)
- [Prevalence of parkinsonism and relationship to exposure in a large sample of Alabama welders — Racette et al., *Neurology* 2005 (PMID:15668418)](https://pubmed.ncbi.nlm.nih.gov/15668418/)
- [A Parkinsonian syndrome in methcathinone users and the role of manganese — Stepens et al., *NEJM* 2008 (PMID:18322282)](https://www.nejm.org/doi/full/10.1056/NEJMoa072488)
- [Syndrome of hepatic cirrhosis, dystonia, polycythemia, and hypermanganesemia caused by mutations in SLC30A10 — Tuschl et al., *AJHG* 2012 (PMID:22341972)](https://pubmed.ncbi.nlm.nih.gov/22341972/)
- [Mutations in SLC39A14 disrupt manganese homeostasis and cause childhood-onset parkinsonism-dystonia — Tuschl et al., *Nat Commun* 2016 (PMID:27231142)](https://pubmed.ncbi.nlm.nih.gov/27231142/)
- [SLC39A14 deficiency alters manganese homeostasis and excretion resulting in brain manganese accumulation and motor deficits in mice — Jenkitkasemwong et al., *PNAS* 2018 (PMID:29437953)](https://www.pnas.org/doi/10.1073/pnas.1720739115)
- [Manganese transporter Slc39a14 deficiency revealed its key role in maintaining manganese homeostasis in mice — *Cell Discov* 2017](https://www.nature.com/articles/celldisc201725)
- [Effective treatment of manganese-induced occupational Parkinsonism with p-aminosalicylic acid: a 17-year follow-up — Jiang et al., *JOEM* 2006 (PMID:16766929)](https://pubmed.ncbi.nlm.nih.gov/16766929/)
- [Chelation therapy of manganese intoxication with para-aminosalicylic acid in Sprague-Dawley rats (PMID:19150464)](https://pubmed.ncbi.nlm.nih.gov/19150464/)
- [Manganese toxicity in children receiving long-term parenteral nutrition — Fell et al., *Lancet* 1996 (PMID:8622451)](https://pubmed.ncbi.nlm.nih.gov/8622451/)
- [Brain metal concentrations in chronic liver failure patients with pallidal T1 MRI hyperintensity — Klos et al., *Neurology* 2006 (PMID:17159105)](https://www.neurology.org/doi/10.1212/01.wnl.0000247037.37807.76)
- [Intellectual impairment in school-age children exposed to manganese from drinking water — Bouchard et al., *EHP* 2011 (PMID:20855239)](https://pubmed.ncbi.nlm.nih.gov/20855239/)
- [Biomarkers of environmental manganese exposure and childhood neurodevelopment: systematic review and meta-analysis (PMID:33008482)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7531154/)
- [Manganese exposure induces α-synuclein aggregation in the frontal cortex of non-human primates — Verina et al. 2013 (PMID:23262390)](https://pubmed.ncbi.nlm.nih.gov/23262390/)
- [Manganese neurotoxicity: new perspectives from behavioral, neuroimaging, and neuropathological studies in humans and non-human primates — Guilarte, *Front Aging Neurosci* 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3690350/)
- [Role of transcription factor yin yang 1 in manganese-induced reduction of astrocytic glutamate transporters — Karki et al. (PMID:25128239)](https://pubmed.ncbi.nlm.nih.gov/25128239/)
- [Protective effects of riluzole on manganese-induced disruption of glutamate transporters and glutamine synthetase in cultured astrocytes (PMID:22391793)](https://pubmed.ncbi.nlm.nih.gov/22391793/)
- [Role of astrocytes in manganese mediated neurotoxicity (PMID:23594835)](https://pubmed.ncbi.nlm.nih.gov/23594835/)
- [The Role of Oxidative Stress in Manganese Neurotoxicity: a review focused on contributions by Michael Aschner](https://pmc.ncbi.nlm.nih.gov/articles/PMC10452838/)
- [Manganese-Induced Neurotoxicity: New Insights Into the Triad of Protein Misfolding, Mitochondrial Impairment, and Neuroinflammation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6606738/)
- [The role and mechanism of the cGAS-STING pathway-mediated ROS in apoptosis and ferroptosis induced by manganese exposure (PMID:40652697)](https://pubmed.ncbi.nlm.nih.gov/40652697/)
- [Manganese stimulates ferroptosis to trigger neurotoxicity in mice and HT22 cells: NCOA4-mediated ferritinophagy (PMID:41043778)](https://pubmed.ncbi.nlm.nih.gov/41043778/)
- [Exposure to Manganese Induces Autophagy–Lysosomal Pathway Dysfunction-Mediated Tauopathy by Activating the cGAS–STING Pathway](https://pubs.acs.org/doi/10.1021/envhealth.4c00176)
- [Manganese (II) chloride leads to dopaminergic neurotoxicity by promoting mitophagy through BNIP3-mediated oxidative stress in SH-SY5Y cells](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8173824/)
- [Elevated thyroid manganese reduces thyroid iodine to induce hypothyroidism in mice, but not rats, lacking SLC30A10 — *Metallomics* 2024](https://academic.oup.com/metallomics/article/16/7/mfae029/7692026)
- [AAV-mediated hepatic expression of SLC30A10 and the Thr95Ile variant attenuates manganese excess in Slc30a10-deficient mice](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10933546/)
- [Neuromythology of Manganism — *Curr Epidemiol Rep* 2015](https://link.springer.com/article/10.1007/s40471-015-0040-x)
- [Metal Exposure and Risk of Parkinson Disease: A Systematic Review and Meta-Analysis — *Am J Epidemiol* 2023](https://academic.oup.com/aje/article/192/7/1207/7109767)
- [Prevalence of Parkinsonism Among Foundry Workers in an Automobile Manufacturing Factory in Tehran](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9526798/)
- [Hypermanganesemia due to mutations in SLC39A14: further insights into Mn deposition in the CNS — *Orphanet J Rare Dis* 2018](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5791243/)
- [Hypermanganesemia with dystonia, polycythemia and cirrhosis in 10 patients: six novel SLC30A10 mutations — Zaki et al., *Clin Genet* 2018](https://onlinelibrary.wiley.com/doi/abs/10.1111/cge.13184)
- [Evaluating the risk of manganese-induced neurotoxicity of parenteral nutrition: review of the current literature](https://pmc.ncbi.nlm.nih.gov/articles/PMC8122055/)
- [Manganism symptoms and T1 hyperintense changes in the basal ganglia in maintenance hemodialysis — *AJNR* 2007](https://www.ajnr.org/content/28/8/1474)
- [Manganese exposure causes movement deficit and changes in the protein profile of the external globus pallidus in Sprague Dawley rats](https://doi.org/10.1177/07482337211022223)
- [ACGIH manganese TLV revision — industry summary](https://www.thefabricator.com/thefabricator/article/arcwelding/new-guideline-reduces-manganese-exposure-limit-dramatically)
- [ICD-10-CM T57.2 — Toxic effect of manganese and its compounds](https://icd.codes/icd10cm/T572)
- [Orphanet: Manganese poisoning (ORPHA:306682)](https://www.orpha.net/en/disease/detail/306682)
- [EMBL-EBI OLS4 — used to verify MONDO:0017638, MONDO:0013208, MONDO:0014864, CHEBI and NCIT identifiers](https://www.ebi.ac.uk/ols4/)
- [HGNC REST — used to verify SLC30A10, SLC1A3, SLC40A1, TFRC HGNC IDs](https://rest.genenames.org/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 46 |
| Resolved | 46 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 22 |
| Quoted claims found in source | 5 |
| Quoted claims **not** found in source | 17 |
| References weighed for topical relevance | 46 |
| On topic | 22 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:37627255` *(abstract only)*: "heterozygous transporter mutations [were] found in up to 40% of the cases in the province of Brescia"
  - Text part not found as substring: 'heterozygous transporter mutations found in up to 40% of the cases in the province of Brescia' (note: only abstract available for PMID:37627255, full text may contain this excerpt)
- `PMID:40496384` *(abstract only)*: "cumulative exposure of manganese over time was more indicative of higher tissue concentrations than recent exposure"
  - closest text in source: "Exposure to high concentrations of manganese is known to cause neurotoxicity and has been recently associated with manganese-induced parkinsonism, which will be explored in this review"
- `PMID:26154659` *(abstract only)*: "Male workers showed impotence and reduced libido"
  - Text part not found as substring: 'Male workers showed impotence and reduced libido' (note: only abstract available for PMID:26154659, full text may contain this excerpt)
- `PMID:40320765` *(abstract only)*: "present in nearly all patients"
  - closest text in source: "These recommendations were developed through an evidence and consensus-based process led by a group of 13 international experts across the disciplines of metabolic medicine, neurology, hematology, genetics, and radiology, and address the clinical presentation, diagnostic investigations, principles of treatment, and monitoring of patients with HMNDYT1 and 2."
- `PMID:40320765` *(abstract only)*: "Cognitive sparing despite severe motor disability"
  - Text part not found as substring: 'Cognitive sparing despite severe motor disability' (note: only abstract available for PMID:40320765, full text may contain this excerpt)
- `PMID:40496384` *(abstract only)*: "reduced activity of antioxidant enzymes, including glutathione peroxidase, glutathione, and superoxide dismutase"
  - closest text in source: "Preventative and therapeutic interventions-including chelation therapy with ethylene-diamine-tetra-acetic acid (CaNa2EDTA), with or without plasma exchange and para-aminosalicylic acid (PAS), as well as natural compounds such as vinpocetine (VIN), punicalagin (PUN), niacin, vitamin E, DNLA, curcumin, and sesame oil-are also reviewed"
- `PMID:40652697` *(abstract only)*: "Inhibition of either the cGAS-STING pathway or reactive oxygen species (ROS) significantly ameliorated manganese-induced oxidative stress, apoptosis, and ferroptosis"
  - closest text in source: "Critically, inhibition of either the cGAS-STING pathway or ROS significantly ameliorated Mn-induced oxidative stress, apoptosis, and ferroptosis"
- `PMID:37627255` *(abstract only)*: "low concentrations of Mn are sufficient to induce α-synuclein fibril formation"
  - closest text in source: "Manganese (Mn) exposure has evolved from acute, high-level exposure causing manganism to low, chronic lifetime exposure"
- `PMID:37627255` *(abstract only)*: "may respond to L-DOPA treatment, contradicting historical diagnostic criteria"
  - Text part not found as substring: 'may respond to L-DOPA treatment, contradicting historical diagnostic criteria' (note: only abstract available for PMID:37627255, full text may contain this excerpt)
- `PMID:40320765` *(abstract only)*: "Mean age of onset of 1 year and 9 months old with all but two patients presenting before or at the age of five"
  - closest text in source: "Here, we provide consensus expert recommendations for the diagnosis and treatment of patients with HMNDYT1 and 2 in order to facilitate early diagnosis and optimize clinical outcome"
- `PMID:40496384` *(abstract only)*: "the 3-year-old patient had a significant reduction in motor symptoms with CaNa₂EDTA, but the 17-year-old's condition continued to worsen"
  - Text part not found as substring: 'the 3-year-old patient had a significant reduction in motor symptoms with CaNa₂EDTA, but the 17-year-old's condition continued to worsen' (note: only abstract available for PMID:40496384, full text may contain this excerpt)
- `PMID:26154659` *(abstract only)*: "absence of nigrostriatal dopamine neuron degeneration in occupationally Mn-induced parkinsonism."
  - closest text in source: "We review occupational Mn-induced parkinsonism and the dynamic modes of Mn transport in biological systems, as well as the detection and pharmacokinetic modeling of Mn trafficking"
- `PMID:40496384` *(abstract only)*: "neuroinflammation in white matter and signs of swelling in the caudate nucleus linked with increased manganese and parkinsonism"
  - closest text in source: "Exposure to high concentrations of manganese is known to cause neurotoxicity and has been recently associated with manganese-induced parkinsonism, which will be explored in this review"
- `PMID:40320765` *(abstract only)*: "All patients with symptomatic HMNDYT1 and HMNDYT2 should be offered chelation therapy if locally available"
  - closest text in source: "Here, we provide consensus expert recommendations for the diagnosis and treatment of patients with HMNDYT1 and 2 in order to facilitate early diagnosis and optimize clinical outcome"
- `PMID:40320765` *(abstract only)*: "All patients with HMNDYT1 should be treated with iron supplementation aiming for a normal iron profile"
  - closest text in source: "Treatment is limited to chelation therapy and iron supplementation that can prevent disease progression"
- `PMID:37627255` *(abstract only)*: "Patients may respond to L-DOPA treatment, contradicting historical diagnostic criteria"
  - Text part not found as substring: 'Patients may respond to L-DOPA treatment, contradicting historical diagnostic criteria' (note: only abstract available for PMID:37627255, full text may contain this excerpt)
- `PMID:29437953` *(abstract only)*: "can be rescued by treatment with the metal chelator Na₂CaEDTA."
  - closest text in source: "We conclude that SLC39A14 is essential for efficient Mn uptake by the liver and pancreas, and its deficiency results in impaired Mn excretion and accumulation of the metal in other tissues"
