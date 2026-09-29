---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-23T19:16:52.483912'
end_time: '2026-09-23T19:22:28.765818'
duration_seconds: 336.28
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Diets-Jongmans Syndrome
  mondo_id: MONDO:0030012
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
  web_search_requests: 13
  num_turns: 31
  total_cost_usd: 1.7287232
  session_id: fd65d8eb-852b-5a9d-91de-140beff025e2
  stop_reason: end_turn
  assistant_text_blocks: 2
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 4
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Diets-Jongmans Syndrome
- **MONDO ID:** MONDO:0030012 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Diets-Jongmans Syndrome** covering all of the
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

I'll research Diets-Jongmans Syndrome using web search and literature sources, then produce the comprehensive report.

I have sufficient primary-literature coverage now. Writing the comprehensive report.

# Diets-Jongmans Syndrome (DIJOS) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Diets-Jongmans syndrome (DIJOS) is a rare, autosomal dominant neurodevelopmental/malformation syndrome caused by heterozygous pathogenic variants in **KDM3B** (lysine demethylase 3B, chromosome 5q31.2). It is characterized by mild-to-moderate intellectual disability/developmental delay, short stature, neonatal feeding difficulties, and a recognizable facial gestalt (long ears, broad/prominent nasal tip with low columella, thin upper lip, wide mouth, pointed chin). It was first delineated as a discrete syndrome by Diets, van der Donk, Baltrunaite et al. in the *American Journal of Human Genetics* in 2019 (PMID:30929739), using trio exome sequencing, GeneMatcher-facilitated international collaboration, and computational facial-recognition analysis (Face2Gene/Clinical Face Phenotype Space) to establish gestalt validity.

**Key identifiers:**
- **OMIM:** #618846 — DIETS-JONGMANS SYNDROME; DIJOS ([omim.org/entry/618846](https://omim.org/entry/618846))
- **Gene OMIM:** *KDM3B, #609373
- **MONDO:** MONDO:0030012 (confirmed via GenCC submission, consistent with the MONDO ID supplied in the research request)
- **Orphanet:** ORPHA:633004 — "KDM3B-related intellectual disability-facial dysmorphism-short stature syndrome" ([orpha.net/en/disease/detail/633004](https://www.orpha.net/en/disease/detail/633004))
- **MedGen:** C5394263 ([ncbi.nlm.nih.gov/medgen/1714920](https://www.ncbi.nlm.nih.gov/medgen/1714920))
- **HGNC (gene):** HGNC:1337 (KDM3B; previous symbols *C5orf7*, *JMJD1B*)
- **GeneCC/ClinGen:** Definitive gene-disease relationship, "Syndromic intellectual disability" (MONDO:0000508), Intellectual Disability and Autism GCEP, curated 2024-02-21 ([search.clinicalgenome.org/kb/genes/HGNC:1337](https://search.clinicalgenome.org/kb/genes/HGNC:1337)); GenCC entry independently lists KDM3B–Diets-Jongmans syndrome (MONDO:0030012) as **Definitive**, autosomal dominant, submitted by Ambry Genetics, evaluated 2024-04-03.
- **No GeneReviews chapter currently exists** for this condition (searched; not found as of this report). GTR lists the condition under C5394263.

**Synonyms:** "KDM3B-related intellectual disability-facial dysmorphism-short stature syndrome" (Orphanet's working name); no other widely used alternate names were found. Caution: an AI-generated web summary encountered during this search expanded "DIJOS" as an acronym for "developmental delay, intellectual disability, joint contractures... immunodeficiency... short stature" — this expansion could not be traced to any primary source (OMIM, the 2019 AJHG paper, or Orphanet) and should be treated as **unverified/likely fabricated** rather than used in curation.

**Evidence base composition:** The evidence base is aggregated disease-level literature (case series and case reports pooled across cohorts), not a single large EHR-derived or registry cohort. As of this search, published literature totals roughly **27+ molecularly confirmed individuals** across the 2019 founding cohort (17 individuals, PMID:30929739) plus at least 9 subsequently published individuals in independent case reports/series (see §9 for citations), so no large single denominator exists — frequencies below are cohort-level percentages from the cited sources, not population data.

---

## 2. Etiology

**Disease causal factor:** Purely genetic — heterozygous (predominantly de novo) pathogenic/likely pathogenic variants in *KDM3B*. No infectious, toxic, or purely environmental cause is described.

**Genetic risk factors:**
- Heterozygous missense, nonsense, frameshift, and splice-site variants in *KDM3B*, clustering in/near the zinc-finger DNA-binding domain and the C-terminal catalytic Jumonji-C (JmjC) domain (PMID:30929739).
- *KDM3B* is highly constrained against loss-of-function variation: original 2019 report cites ExAC pLI = 1.00 and Z-score = 4.99 (missense constraint); ClinGen's current summary similarly reports pLI ≈ 1.0 and a low LOEUF (~0.12), consistent with strong haploinsufficiency intolerance ([ClinGen KDM3B page](https://search.clinicalgenome.org/kb/genes/HGNC:1337)).
- No modifier genes have been formally identified; a co-occurring *SIN3A* variant was reported alongside a *KDM3B* variant in one atypical pulmonary-hypertension case (PMID:38314229), but this is a single dual-diagnosis observation, not an established modifier relationship.

**Environmental risk factors:** None established; this is a monogenic disorder.

**Protective factors:** None reported in the literature to date.

**Gene-environment interactions:** Not described. The single case with rhGH (recombinant human growth hormone) exposure (PMC13025784) is a treatment-response observation, not a G×E etiologic interaction.

---

## 3. Phenotypes

### Developmental / Cognitive
- **Intellectual disability / developmental delay** — present in 16/17 (94.1%) of the founding cohort (PMID:30929739); pooled across later literature (27 patients, PMC13025784) 81.5%. Predominantly **mild** (47.1%) to **mild-moderate** (23.5%); severe ID is uncommon. Speech/language delay is typically more pronounced than motor delay.
  - HP:0001249 (Intellectual disability); HP:0011342 (Mild intellectual disability); HP:0001263 (Global developmental delay); HP:0000750 (Delayed speech and language development)
- **Motor delay** — 70.4% (pooled, PMC13025784).
  - HP:0001270 (Motor delay)
- **Childhood hypotonia** — 38.5% (PMID:30929739).
  - HP:0001252 (Hypotonia)
- **Behavioral problems** — 53.3%; **ADHD** 18.5–26.7%; **autism spectrum disorder** 14.8–20%. A 2025 report of two Chinese patients specifically highlights autistic features and global developmental delay as presenting complaints (PMID:41408900).
  - HP:0000708 (Behavioral abnormality); HP:0007018 (Attention deficit hyperactivity disorder); HP:0000717 (Autism)
- **Epilepsy** — 20% (two transient cases) (PMID:30929739).
  - HP:0001250 (Seizure)
- **Variable neuropsychological profile within families** — a 2026 case series of four family members carrying the same variant reported a "variable neuropsychological profile," i.e., marked intrafamilial variability in cognitive presentation despite an identical KDM3B variant (Archives of Clinical Neuropsychology, PMID:42186234; full abstract text could not be retrieved due to access restrictions — treat as a lead pending direct verification).

### Growth
- **Short stature** — ~50–55.6% of patients (<-2 to -2.5 SD), with height <-1.5 SD in 68.8% (PMID:30929739; PMC13025784).
  - HP:0004322 (Short stature)
- **Low birth weight / postnatal growth restriction** — 59.3% pooled (PMC13025784); one recent 4-patient case series found growth retardation to be **the predominant/sole clinical feature** with minimal neurodevelopmental involvement, expanding phenotypic heterogeneity (PMC13025784, MDPI *Genes* 2026, doi:10.3390/genes17030294).
  - HP:0001518 (Small for gestational age); HP:0004325 (Decreased body weight)
- **Growth hormone deficiency** — documented and biochemically confirmed (stimulation testing) in at least two independently reported cases (PMC13025784; Turkish case, PMID:41878155/PMC13008413), described as "rarely reported" previously.
  - HP:0000824 (Growth hormone deficiency)
- **Microcephaly-range head circumference reduction** — reported in the Turkish case (head circumference SDS -3.96) (PMC13008413).
  - HP:0000252 (Microcephaly)

### Feeding / Gastrointestinal
- **Neonatal feeding difficulties** — 51.9–60% (PMID:30929739; PMC13025784).
  - HP:0011968 (Feeding difficulties)
- **Umbilical/inguinal hernia** — 12.5% each; **diaphragmatic hernia** — 12.5% (PMID:30929739).
  - HP:0001537 (Umbilical hernia); HP:0000023 (Inguinal hernia); HP:0000776 (Congenital diaphragmatic hernia)
- **Duodenal atresia** — reported in one individual (PMID:30929739).
  - HP:0002247 (Duodenal atresia)

### Musculoskeletal
- **Joint hypermobility** — 31.3% (PMID:30929739).
  - HP:0001382 (Joint hypermobility)
- **Pectus excavatum** — reported in a Chinese case (PMID:41914422).
  - HP:0000767 (Pectus excavatum)

### Craniofacial (facial gestalt — see also §4 for facial-recognition analysis)
- Long ears — 52.9%; broad/prominent nasal tip — 82.4%; wide mouth — 70.6%; thin upper lip vermilion — 70.6%; pointed/prominent chin — 70.6%; low columella — 35.3% (PMID:30929739).
  - HP:0009884 (Long ear); HP:0000455 (Broad nasal tip); HP:0000154 (Wide mouth); HP:0000219 (Thin upper lip vermilion); HP:0000307 (Prominent chin); HP:0011832 (Low columella)
- Non-neutral palpebral fissures — 4/16 upslanting, 5/16 downslanting (PMID:30929739).
  - HP:0000582 (Upslanted palpebral fissure); HP:0000494 (Downslanted palpebral fissure)
- Micrognathia (Turkish case) — HP:0000347.

### Ophthalmologic / Otologic
- Eye abnormalities (nystagmus, strabismus, refractive error) — 31.3% (PMID:30929739). HP:0000639 (Nystagmus), HP:0000486 (Strabismus).
- Hearing loss — 23.5% (PMID:30929739). HP:0000365 (Hearing impairment).

### Genitourinary
- Cryptorchidism, hypospadias — 12.5% each (PMID:30929739). HP:0000028 (Cryptorchidism); HP:0000047 (Hypospadias).
- Oligospermia — documented in one adult male individual with the *Kdm3b*-knockout mouse subfertility phenotype cited as biological plausibility (PMID:30929739).

### Cardiac / Vascular
- Ventricular septal defect, heterotaxy, interrupted inferior vena cava (individual reports, PMID:30929739). HP:0001629 (VSD); HP:0001696 (Heterotaxy).
- **Cardiomyopathy** and **neutropenia** — newly reported as expanded phenotypes in a 2023 report of two patients (one with de novo splice variant c.5070+1G>A, first reported KDM3B splice variant; one with c.2828G>A p.R943Q), one presenting with palpitation/dyspnea/edema, the other with recurrent URIs and transient neutropenia (PMID:36757469, *Neurogenetics* 2023).
  - HP:0001638 (Cardiomyopathy); HP:0001875 (Neutropenia)
- **Pulmonary arterial hypertension / childhood interstitial lung disease (chILD)** — reported in a 10-year-old boy (Sudanese) with a novel KDM3B missense variant (c.4406T>C, p.Ile1469Thr) who also carried a *SIN3A* variant (c.1381G>A, p.Gly461Arg); described as "the second described case worldwide" of PAH associated with a KDM3B mutation (Benslimane et al., *Pan Afr Med J* 2023, PMID:38314229). **Caution:** dual-variant case — causal attribution to KDM3B alone is not established.
  - HP:0002092 (Pulmonary hypertension)

### Oncologic
- **Malignancy** — 2/17 (11.8%) in the founding cohort: acute myeloid leukemia and Hodgkin lymphoma (PMID:30929739). The authors explicitly flag ascertainment bias (both patients were recruited through a cancer-predisposition study) and recommend clinical vigilance rather than a formal surveillance protocol. This is biologically plausible given that somatic *KDM3B* alterations and *Kdm3b*-knockout-mouse myelodysplastic-syndrome-like hematopoietic defects are independently described (see §6).
  - HP:0004377 (AML — HP:0004808 more precisely "Acute myeloid leukemia"); HP:0012156 (Hodgkin lymphoma, if using more specific term) — verify exact HPO IDs against the cache before binding.

### Frequency caveat
All percentages above are drawn from small, ascertainment-biased cohorts (primarily clinical-genetics referral for developmental delay); true population frequencies are unknown given the extreme rarity of the condition.

---

## 4. Genetic / Molecular Information

**Causal gene:** *KDM3B* (Lysine Demethylase 3B; previous symbols *JMJD1B*, *C5orf7*), HGNC:1337, chromosome **5q31.2**, gene OMIM #609373.

**Pathogenic variant spectrum (as of the most recent literature review, PMC13025784, MDPI *Genes* 2026):**
- Across 27 pooled reported patients: **23 distinct KDM3B variants** — 12 missense, 5 nonsense, 4 frameshift, 2 splice-site; 4 variants recurrent.
- Original 2019 cohort (17 individuals): 14 distinct variants — 5 truncating (nonsense) and other missense; "All 14 different variants found were absent from the gnomAD and ExAC databases," and "13/14 had high CADD scores (13–40)" (PMID:30929739).
- Variants cluster in/near the **zinc-finger domain** (DNA-binding) and the **Jumonji-C (JmjC) catalytic domain** responsible for H3K9 demethylation; missense variants affect residues that are "evolutionarily highly conserved across other species," including conservation with paralogs KDM3A and JMJD1C.
- MetaDome analysis of missense variant positions found several located in regions "intolerant" or "highly intolerant for missense variation," supporting pathogenicity (PMID:30929739).
- Representative individual variants across reports: p.Glu93* (inherited, mother-to-child), p.Asp336Gly (inherited, father-to-child), p.Glu1731Lys (inherited, father-to-child), c.2743_2745del p.(Arg915del) (ClinVar RCV002468724), c.5147T>C p.(Leu1716Pro) (PMID:41914422, de novo), c.5068C>T p.(Gln1690Ter) (Turkish case, PMC13008413, inherited from mildly-affected mother), c.5070+1G>A (first reported splice variant, de novo, PMID:36757469), c.2828G>A p.(Arg943Gln) (PMID:36757469), c.1970C>G p.(Ser657*) and c.3973-1G>C (2025 Chinese cohort, PMID:41408900), c.2832-3C>G, c.1188del p.(Glu397Argfs*21), c.4580T>C p.(Leu1527Pro), c.3220dup p.(Glu1074Glyfs*48) (4-patient growth-predominant series, PMC13025784), c.4406T>C p.(Ile1469Thr) (chILD/PAH case, co-occurring with SIN3A, PMID:38314229).

**ACMG/ClinVar classification:** Individual variants are typically classified pathogenic/likely pathogenic under ACMG/AMP criteria on a case-by-case basis (e.g., ClinVar RCV002468724 for p.Arg915del); no single hotspot dominates.

**Population frequency:** All reported disease-causing variants are absent from gnomAD/ExAC, consistent with a severely constrained gene (pLI ≈ 1.0, LOEUF ≈ 0.12 per ClinGen's summary) and de novo dominant disease mechanism.

**Somatic vs. germline:** DIJOS itself is caused exclusively by germline variants. Note (important for the dismech "keep germline syndromes separate from somatic tumors" convention): *KDM3B* also carries **somatic** alterations reported in hematologic malignancies (independent of DIJOS) — the 2019 authors explicitly cite this as biological plausibility for the myeloid malignancy signal in their germline cohort, but somatic KDM3B cancer biology is a distinct body of literature not curated here.

**Functional consequence / mechanism:** The 2019 authors state: **"We identified nonsense variants in five individuals, implying that haploinsufficiency is the most likely mechanism of disease in our individuals as well"** (PMID:30929739) — i.e., predominantly **loss-of-function via haploinsufficiency**, consistent with the gene's extreme LoF intolerance. Direct biochemical confirmation was attempted but inconclusive: **"We assessed the mono- and tri-methylation status of H3K9 in HEK293 cells that were overexpressing wild-type and missense mutants of KDM3B, but these experiments were inconclusive due to large variability in expression levels"** (PMID:30929739). A later case report (PMID:41914422) proposes that a specific missense variant (p.Leu1716Pro) in the JmjC domain "disrupts hydrogen bonding, reducing protein stability," a structural (not functionally assayed) inference.

**Genotype-phenotype correlation:** The 2025/2026 literature-review case series (PMC13025784) notes that **loss-of-function (truncating) variants "may confer a relatively milder neurodevelopmental phenotype" compared to missense variants** — an emerging but not yet firmly established correlation; label as a hypothesis from a small pooled series, not a settled rule.

**Modifier genes / epigenetics:** No modifier genes established. *KDM3B* itself is an epigenetic "writer/eraser" — a chromatin-modifying enzyme — making DIJOS itself a disorder of epigenetic regulation (a "chromatinopathy"), rather than a disorder with reported secondary epigenetic dysregulation as a downstream mechanism.

**Chromosomal abnormalities:** No microdeletion/microduplication or translocation mechanism is described for DIJOS; all reported cases are single-nucleotide/small-indel/splice variants.

---

## 5. Environmental Information

Not applicable — DIJOS is a purely monogenic disorder. No environmental, lifestyle, or infectious contributing factors are described in the literature reviewed.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (from initiating lesion to clinical manifestation)

1. **Heterozygous de novo (occasionally inherited) loss-of-function or missense variant in *KDM3B*** (chr5q31.2) → **disrupts or destabilizes the KDM3B protein's zinc-finger DNA-binding domain or its C-terminal JmjC catalytic domain** (demonstrated by variant clustering and conservation analysis; PMID:30929739). *Inferred* structural consequence for individual missense variants (e.g., p.Leu1716Pro disrupting hydrogen bonding), not directly assayed in most cases (PMID:41914422).
2. **Truncating variants (≈5/14–5/23 of reported variants) most plausibly cause haploinsufficiency** — reduced dosage of functional KDM3B protein — stated explicitly by the discovery cohort as "the most likely mechanism of disease" (PMID:30929739). This step is a genetic-mechanism inference from variant type and gene constraint (pLI≈1.0), not from a direct dosage/protein-level assay in patient tissue.
3. **Reduced KDM3B H3-lysine-9 (H3K9) demethylase activity** → **failure to remove repressive H3K9me1/me2 marks** at KDM3B target loci. This step is *inferred by homology/mechanism* (KDM3B is a well-characterized JmjC-domain H3K9 demethylase; UniProt DI-05814) rather than directly measured in DIJOS patient cells — the authors' own attempt to assay H3K9 methylation status in an overexpression cell system was "inconclusive due to large variability in expression levels" (PMID:30929739). **This is the single largest evidentiary gap in the human mechanistic chain and should be flagged as a knowledge gap / HUMAN_MODEL_MISMATCH candidate** when curated, since the mechanistic step downstream of variant identification rests on mouse-model and biochemical-homology inference rather than confirmed patient-tissue chromatin data.
4. Branch A — **Transcriptional dysregulation**: Because H3K9 methylation is a repressive chromatin mark, loss of KDM3B demethylase activity is predicted by the authors to result in **failure to activate transcription** at target loci — stated as: **"methylation of H3K9 is generally considered to be a repressive mark, demethylation of H3K9 by KDM3B is predicted to result in the activation of transcription and thus might explain subsequent growth retardation"** (PMID:30929739). This transcriptional consequence is itself inferred from the general biology of H3K9 methylation, not measured via patient-derived transcriptomics.
5. Branch A, continued — **Neurodevelopmental consequence**: transcriptional dysregulation during neurodevelopment (via disrupted chromatin regulation of neuronal gene programs) → **intellectual disability, developmental delay, hypotonia, behavioral/autistic features**. A separate line of mouse evidence supports a specific downstream neuro-mechanism: cerebellar studies indicate "diminished H3K9 demethylase activity impairs cerebellar memory consolidation" and that KDM3B "plays an essential role in motor learning" (cited in PMC13025784) — this is **model-organism (mouse) evidence whose translational fidelity to human DIJOS cognitive/motor phenotypes has not been directly tested** (a HUMAN_MODEL_MISMATCH-type gap).
6. Branch B — **Growth/endocrine consequence**: Mouse *Kdm3b*-knockout studies (Kim et al., PMID:25892958, and related work) show that Kdm3b ablation **decreases hepatic/renal IGFBP-3 expression → accelerated IGF-1 degradation → ~36% reduction in circulating IGF-1** → postnatal somatic growth restriction. The 2019 human cohort explicitly extrapolates this mouse mechanism to explain patient short stature: **"kdm3b-knockout mice present with a somatic growth restriction, possibly explained by decreased concentrations of insulin-like growth factor-1 (IGF1)"** (PMID:30929739) → clinically, this is corroborated in humans by two independently reported cases with **biochemically confirmed growth hormone deficiency** on stimulation testing (PMC13025784; PMC13008413) → **short stature, and rhGH-responsive growth improvement documented in one patient (94.3 cm → 135 cm over 6 years)** (PMC13025784).
7. Branch C — **Hematopoietic/reproductive consequence**: *Kdm3b*-knockout mice independently show (i) **hematopoietic-system defects "consistent with myelodysplastic syndrome"** (PMID:30929739, citing prior mouse literature) and (ii) **male subfertility with reduced sperm reserves and motility** (PMID:26681924) and **female reproductive defects (irregular estrous cycles, reduced ovulation/fertilization rates, decreased circulating estradiol)** (PMID:25892958). In humans, this maps to: (a) two malignancies (AML, Hodgkin lymphoma) among 17 founding-cohort patients — flagged by the authors as possibly ascertainment-biased but biologically plausible given known **somatic** KDM3B alterations in hematologic malignancy, and (b) one adult male patient with documented oligospermia, cited by the authors as "in accordance" with the mouse phenotype (PMID:30929739).
8. Branch D (peripheral, weakly evidenced) — Isolated reports link KDM3B variants to **cardiomyopathy and transient neutropenia** (PMID:36757469) and to **pulmonary arterial hypertension/childhood interstitial lung disease** (PMID:38314229, confounded by a co-occurring SIN3A variant). No mechanistic chain has been proposed connecting KDM3B loss-of-function to cardiac or pulmonary vascular pathophysiology; these should be treated as emerging, single/dual-case-level phenotype associations rather than established downstream nodes of the pathway above.

### Category checklist detail

- **Molecular pathways:** Chromatin/epigenetic regulation — H3K9 demethylation (JmjC/Jumonji-domain demethylase family); downstream transcriptional activation of KDM3B target genes (specific target gene identities in human neurodevelopment not established in the cited literature).
  - GO:0032454 (histone H3-K9 demethylase activity, note-check exact ID against GO); GO:0006338 (chromatin remodeling, verify).
- **Cellular processes:** Chromatin remodeling / epigenetic gene regulation; (mouse) hematopoietic differentiation; (mouse) germ cell/oocyte and spermatocyte maturation.
- **Protein dysfunction:** Loss-of-function via haploinsufficiency (predominant model per truncating variant burden); for missense variants, structural destabilization within the JmjC catalytic domain or zinc-finger domain is proposed but not biochemically confirmed for most reported variants.
  - Protein domains: N-terminal zinc-finger DNA-binding domain, LXXLL nuclear-receptor-interaction motif, C-terminal JmjC catalytic domain (per PMC13025784 summary; verify against UniProt directly before binding InterPro/Pfam IDs).
- **Metabolic changes:** IGF-1/IGFBP-3 axis dysregulation (mouse-demonstrated; human growth hormone deficiency documented but the human GH-axis lesion has not been mechanistically linked back to KDM3B at the molecular level — it is a phenotypic correlation).
- **Immune system involvement:** No autoimmune or immunodeficiency mechanism is established in the primary literature (see caution above about the unverified "immunodeficiency" acronym expansion). Neutropenia is reported in a single case (transient) (PMID:36757469).
- **Tissue damage mechanisms:** Not specifically characterized; no oxidative stress/fibrosis/necrosis mechanism has been reported for DIJOS itself (the pulmonary fibrosis findings in the chILD case report are radiologic/histologic descriptions, not mechanistic data, and are confounded by co-occurring SIN3A variant).
- **Biochemical abnormalities:** Reduced/absent H3K9 demethylase enzymatic activity (inferred from gene function and variant type, not directly measured in patient tissue in the cited studies); biochemically confirmed GH deficiency in ≥2 patients on stimulation testing.
- **Epigenetic changes:** DIJOS is itself a primary disorder of an epigenetic "eraser" enzyme (a chromatinopathy) rather than a disorder with reported secondary/consequential DNA methylation changes; no patient-derived methylome (e.g., EpiSign) data specific to DIJOS were identified in this search — this would be a reasonable knowledge-gap flag (an "episignature" study has not been reported for KDM3B, unlike many other chromatinopathies).
- **Molecular profiling (transcriptomics/proteomics/single-cell):** No patient-derived RNA-seq, proteomics, or single-cell data specific to DIJOS were found in this search.
- **Advanced technologies:** The founding study used **computational facial-recognition/facial-gestalt analysis** (CFPS + OpenFace hybrid model) rather than an -omics technology, to statistically validate the facial phenotype: **"Clustering improvement factors (CIFs)...demonstrated that there is a significant similarity between the faces of individuals with a germline variant in KDM3B when compared to the general ID population (CIF = 2.5962; p = 0.0054)"** (PMID:30929739).

**Suggested cell types (CL) / anatomical (UBERON) / GO terms for pathograph nodes** (to be independently verified via OAK before binding, per dismech-terms rules — none of the CURIEs below have been looked up live in this session and must be treated as leads):
- GO: histone H3-K9 demethylation, chromatin organization, regulation of transcription by RNA polymerase II.
- CL: neuron (generic), hematopoietic stem cell, chondrocyte/growth-plate chondrocyte (growth phenotype), spermatid/spermatocyte (mouse fertility phenotype).
- UBERON: cerebellum, growth plate/epiphyseal cartilage, bone marrow, pituitary/hypothalamic-pituitary-somatotropic axis, testis.

---

## 7. Anatomical Structures Affected

- **Primary organs/systems:** CNS (cognition, motor learning, cerebellum in mouse studies), skeletal growth system (short stature), craniofacial skeleton/soft tissue (facial gestalt), endocrine (GH axis).
- **Secondary/complication-level involvement:** Hematopoietic system (neutropenia, malignancy signal), cardiovascular system (cardiomyopathy, VSD, heterotaxy, IVC anomaly), pulmonary vasculature (PAH/chILD — confounded case), gastrointestinal (duodenal atresia, hernias, diaphragmatic hernia), genitourinary (cryptorchidism, hypospadias, oligospermia), ophthalmologic (strabismus, nystagmus, refractive error), otologic (hearing loss).
- **Tissue/cell level:** Neurons and glia (neurodevelopment); growth-plate chondrocytes and hepatic/renal tissue producing IGFBP-3 (growth axis, mouse-demonstrated); hematopoietic stem/progenitor cells (mouse MDS-like phenotype); germ cells (mouse fertility phenotypes; human oligospermia).
- **Subcellular level:** **Nucleus — chromatin/histone H3 tail** is the direct site of KDM3B enzymatic action (GO Cellular Component: nucleus/nucleoplasm/chromatin).
- **Localization/laterality:** No lateralization pattern reported; facial features are symmetric/bilateral dysmorphism.

---

## 8. Temporal Development

- **Onset:** Congenital/early infancy for feeding difficulties and dysmorphism; developmental delay typically recognized in infancy/early childhood; short stature may be present from birth (low birth weight) or emerge postnatally.
- **Progression:** Generally a **stable, non-progressive** developmental/malformation syndrome rather than a degenerative one — no reports of neurological regression were identified. Growth restriction can be **progressive relative to peers** if untreated, but is described as responsive to rhGH in the one treated case (PMC13025784).
- **Disease course:** Chronic, lifelong (affected parents in the founding cohort demonstrate the phenotype persists into adulthood, ages up to 42 years reported) (PMID:30929739).
- **Critical periods:** Neonatal period is a recognized vulnerability window (feeding difficulties); the GH-deficiency subgroup represents a window for endocrine intervention (rhGH therapy) that produced height improvement in one documented case.

---

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal dominant (AD), per OMIM #618846, ClinGen (Definitive, AD), and GenCC (Definitive, AD).
- **De novo vs. inherited:** In the founding cohort of 17 individuals: **10 confirmed de novo** variants and **3 parent-to-child transmissions** (affected parent, affected child) — p.Glu93* (mother→child), p.Asp336Gly (father→child), p.Glu1731Lys (father→child) (PMID:30929739). Subsequent reports continue this mixed pattern — e.g., the Turkish case's variant was inherited from a mother with "short stature without neurocognitive impairment" (PMC13008413).
- **Penetrance:** Appears **complete but with markedly variable expressivity** — "No evidence of skipped generations" was noted in the founding families, but severity ranges widely, including a mother who is a carrier with an essentially isolated short-stature phenotype and no cognitive impairment (PMC13008413), and a 4-family-member case series explicitly reporting a "variable neuropsychological profile" among relatives sharing one variant (PMID:42186234, abstract not independently verified in this session — treat as a lead).
- **Expressivity:** Variable, as above — ranges from growth-restriction-predominant presentations with minimal neurodevelopmental involvement (PMC13025784) to classic ID + short stature + dysmorphism + multisystem involvement.
- **Genetic anticipation:** Not reported/not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not specifically documented in the literature reviewed, though biologically plausible for any AD de novo-predominant disorder; not confirmed here.
- **Founder effects:** None reported; cases span multiple ethnicities/geographies (Netherlands/international GeneMatcher cohort, China ×3 reports, Albania, Turkey, Sudan).
- **Consanguinity:** Not specifically implicated (AD dominant mechanism, not recessive).
- **Carrier frequency:** Not applicable/not meaningful for an AD ultra-rare disorder with essentially no population carrier-frequency data (all reported variants absent from gnomAD).
- **Epidemiology:** Prevalence reported as **<1/1,000,000** (extremely rare); total published, molecularly confirmed cases are estimated at roughly **25–30+** individuals across all literature identified in this search (17 in the founding 2019 cohort + at least 4 (growth-predominant series) + 2 (Neurogenetics 2023) + 1 (Albania, 2022) + 1 (Turkey, 2026) + 2 (China, 2025 autism report) + 1 (China, 2026 case report) + 1 (chILD/PAH, confounded case) — note some of these patient counts may overlap between the "27 pooled" figure in PMC13025784 and reports published after that review, so this total should be treated as an estimate to be refined during formal curation, not an exact count).
- **Geographic distribution:** Cases reported from the Netherlands/international collaborative cohort, China (×3 independent reports), Albania, Turkey, and Sudan — consistent with a pan-ethnic, non-geographically-restricted disorder ascertained wherever exome/genome sequencing access exists.
- **Sex ratio:** Founding cohort was roughly balanced (9 males, 8 females) (PMID:30929739); no strong sex skew reported.
- **Age distribution:** Founding cohort spanned 9 months to 42 years, reflecting both pediatric probands and their affected adult parents (PMID:30929739).

---

## 10. Diagnostics

- **Genetic testing approach:** Diagnosis is made by identifying a heterozygous pathogenic/likely pathogenic *KDM3B* variant, typically via **exome sequencing (trio-based preferred)** or a **multigene neurodevelopmental-disorder/intellectual-disability panel** that includes KDM3B; whole-genome sequencing would also detect coding variants. No single-gene-first testing strategy is standard given the absence of a specific pathognomonic clinical sign; NDD gene panels and exome sequencing are the practical entry points (consistent with how essentially all reported cases, including the founding cohort, were ascertained — via trio-ES with a chromatinopathy/NDD gene list).
- **Chromosomal microarray / karyotype:** Not the primary diagnostic modality (no described recurrent CNV mechanism), though often performed as part of standard NDD/short-stature diagnostic workup before/alongside sequencing.
- **Clinical/biochemical workup:** Growth-hormone stimulation testing is clinically relevant given the documented (though not universal) GH-deficiency subgroup (PMC13025784; PMC13008413). Standard developmental/cognitive assessment (e.g., Denver II, Wechsler scales) is used to characterize the ID/DD phenotype (as in PMC13008413 and PMID:41914422).
- **Imaging:** No syndrome-specific neuroimaging pattern has been established; HRCT was used in the chILD/PAH case to characterize ground-glass opacities, mosaic attenuation, and fibrosis, but this is not a diagnostic feature of DIJOS itself (confounded by co-occurring SIN3A variant) (PMID:38314229).
- **Facial-gestalt/computational phenotyping:** The founding study's CFPS/OpenFace-based facial-recognition analysis (statistically significant clustering, CIF = 2.5962, p = 0.0054) suggests that Face2Gene-style deep-phenotyping tools may aid diagnostic suspicion/prioritization pre- or post-sequencing (PMID:30929739), though this is a research tool rather than a validated clinical diagnostic criterion.
- **Differential diagnosis:** No formal differential-diagnosis list specific to DIJOS was located in the primary literature searched. Given the overlapping presentation (ID + short stature + facial dysmorphism + feeding difficulties + hypermobility), DIJOS falls within the broader **chromatinopathy** differential (Cornelia de Lange syndrome and related cohesinopathies/chromatin-regulator disorders, Coffin-Siris syndrome, KBG syndrome) on clinical grounds by phenotypic analogy, but **no primary source explicitly names these as the DIJOS differential** — this should be flagged as an inference rather than sourced fact if curated, and verified against the original AJHG paper's discussion section directly (not fully retrievable via WebFetch in this session due to access restrictions on cell.com/ScienceDirect).
- **Standardized diagnostic criteria:** No DSM/ICD-specific diagnostic criteria exist for DIJOS as a discrete entity; diagnosis is molecular (variant identification) combined with compatible phenotype.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** No mortality data specific to DIJOS were identified; the disorder is not described as life-limiting in the reviewed literature, though the malignancy signal (AML, Hodgkin lymphoma in 2/17 founding-cohort patients) and the single severe PAH/chILD case represent potentially serious, though uncommon, complications.
- **Morbidity/function:** Long-term functional outcome is dominated by the degree of intellectual disability (mild-to-moderate in the great majority) and short stature; affected adults in the founding cohort (up to age 42) demonstrate the condition is compatible with adult survival and, in at least some carriers (e.g., the mildly affected mothers in inherited cases), with minimal functional impairment.
- **Complications:** Malignancy (AML, Hodgkin lymphoma — small numbers, ascertainment-biased), cardiomyopathy, neutropenia, pulmonary arterial hypertension (single confounded case), epilepsy (transient in some), hearing loss, ophthalmologic complications.
- **Recovery/treatment response:** Growth response to rhGH therapy was substantial in one documented case (94.3 cm → 135 cm over 6 years, moving from below -3 SD to -1 to -2 SD) (PMC13025784) — this is the only quantified treatment-outcome data point identified.
- **Prognostic factors:** Preliminary/unconfirmed genotype-phenotype signal that truncating (LoF) variants may associate with a milder neurodevelopmental phenotype than missense variants (PMC13025784) — treat as an emerging hypothesis, not an established prognostic rule.

---

## 12. Treatment

Management is **supportive and multidisciplinary**; there is no disease-modifying or gene-targeted therapy for DIJOS.

- **Pharmacotherapy:**
  - **Recombinant human growth hormone (rhGH)** for biochemically confirmed GH deficiency — documented efficacy in one case (PMC13025784); the authors of that series explicitly flag a theoretical concern requiring individualized risk-benefit discussion: **"given that KDM3B...has been linked to myelodysplastic syndrome and acute myeloid leukemia, the potential oncogenic risk of rhGH must be carefully weighed"** — i.e., rhGH use in DIJOS should be considered in the context of the gene's hematologic-malignancy association, though no formal contraindication or surveillance protocol has been published.
    - NCIT:C1691 (Growth Hormone, generic) — treatment_term candidate; verify exact NCIT binding before curation.
  - **ADHD pharmacotherapy** as clinically indicated for the behavioral/ADHD subgroup (general guideline-level statement, not DIJOS-specific evidence).
- **Rehabilitative/supportive care:** Early referral to developmental/rehabilitation services (physical therapy, occupational therapy, speech-language therapy) for the ID/DD and motor-delay phenotype; individualized educational programs.
  - NCIT:C15302 (Physical Therapy); NCIT:C159273 (Speech Therapy, verify); NCIT:C121351 (Occupational Therapy, verify).
- **Genetic counseling:** Recommended given AD inheritance, de novo predominance but documented parent-to-child transmission with variable expressivity — family variant testing (cascade testing of parents) is standard once a proband variant is identified, as demonstrated in essentially every cited case report.
  - NCIT:C15240 (Genetic Counseling).
- **Malignancy vigilance:** No formal, published surveillance protocol exists; the founding-cohort authors recommend clinical vigilance rather than routine screening, citing ascertainment bias in their 2/17 malignancy signal (PMID:30929739).
- **Experimental/investigational therapies:** None identified — no gene therapy, targeted molecular therapy, or clinical trials specific to DIJOS were found in this search (searched ClinicalTrials.gov indirectly via general web search; no DIJOS/KDM3B-specific trial surfaced).
- **Cardiac/pulmonary management:** Standard cardiology/pulmonology management as clinically indicated for the individually reported cardiomyopathy and PAH/chILD cases; no DIJOS-specific cardiac or pulmonary management guideline exists.

---

## 13. Prevention

- **Primary prevention:** Not applicable — this is a predominantly de novo genetic disorder; no modifiable primary-prevention strategy exists.
- **Secondary prevention / screening:** No population or newborn screening program exists (ultra-rare, molecularly diagnosed condition). **Prenatal/preimplantation genetic testing** is relevant once a familial pathogenic variant is identified (standard genetic-counseling practice for known AD variants), though this was not explicitly documented as performed in any cited case.
- **Genetic counseling:** Central preventive/family-planning tool once a proband's variant is identified — enables informed reproductive decision-making and identification of mildly affected/subclinically affected parents (as seen in the inherited cases above, where a parent's own diagnosis was made retrospectively via cascade testing).
- **Behavioral/public health interventions:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring veterinary/companion-animal disease attributable to spontaneous *Kdm3b* variants was identified in this search (searched OMIA indirectly via general search; no hits surfaced). This differs from the engineered mouse models below.
- **Orthologous gene:** Mouse *Kdm3b* (MGI, chromosome 18) is the principal ortholog studied.
- **Comparative biology:** KDM3B is conserved with paralogs KDM3A and JMJD1C within the JmjC-domain histone demethylase family (PMID:30929739 notes cross-paralog conservation at missense-affected residues).

---

## 15. Model Organisms

- **Species/model type:** **Mouse (*Mus musculus*), germline *Kdm3b* knockout** — the principal and, in the literature reviewed, essentially the only animal model directly informing DIJOS mechanism.
- **Key model studies:**
  - **Growth/endocrine:** *Kdm3b*-knockout mice show postnatal somatic growth restriction; mechanistically, Kdm3b ablation reduces renal/hepatic IGFBP-3 expression (~53% reduction reported), lowering circulating IGF-1 (~36% reduction), driving growth restriction (PMID:25892958, "The histone H3K9 demethylase Kdm3b is required for somatic growth and female reproductive function").
  - **Female reproduction:** The same knockout model shows irregular estrous cycles, ~45% reduced ovulation capacity, ~47% reduced fertilization rate, ~44% reduced uterine decidual response, and >50% reduced circulating 17β-estradiol (PMID:25892958).
  - **Male reproduction:** A separate *Kdm3b*-knockout study shows decreased sperm number/motility and impaired consummatory and motivational sexual behavior (PMID:26681924, "Knockout of the Histone Demethylase Kdm3b Decreases Spermatogenesis and Impairs Male Sexual Behaviors").
  - **Hematopoiesis:** *Kdm3b*-knockout mice show hematopoietic defects described by the DIJOS founding-cohort authors as "consistent with myelodysplastic syndrome" (cited secondhand in PMID:30929739; primary knockout-hematopoiesis paper not independently retrieved in this session and should be verified directly before citing in curation).
  - **Neurocognitive (cerebellum):** Mouse studies indicate diminished H3K9 demethylase activity "impairs cerebellar memory consolidation" and that Kdm3b "plays an essential role in motor learning" (cited in PMC13025784; primary source not independently retrieved in this session).
- **Phenotype recapitulation:** The mouse model **recapitulates the growth-restriction and (male/female) reproductive phenotypes** observed in a subset of human patients reasonably well (the founding-cohort authors explicitly draw this parallel, including citing one patient's oligospermia as "in accordance" with the mouse phenotype). The **neurodevelopmental/cognitive phenotype in humans (the dominant clinical feature) is far less directly validated in the mouse model** — the cerebellar/motor-learning mouse data are suggestive but have not been shown to reproduce the human ID/developmental-delay phenotype specifically, representing a genuine human-model translational gap.
- **Model limitations:** Complete germline knockout (not a patient-variant-specific knock-in) — does not model the dominant, haploinsufficient, single-copy-loss human genetics precisely (most mouse studies use homozygous knockouts), and does not model the missense/potentially dominant-negative variant subclass at all. No conditional, humanized, or patient-variant-specific (knock-in) mouse model was identified in this search.
- **Other model systems:** No zebrafish, *Drosophila*, *C. elegans*, iPSC-derived, or organoid models of KDM3B/DIJOS were identified in this search.
- **Resources:** MGI (Mouse Genome Informatics) is the relevant repository for the *Kdm3b* knockout allele(s); specific allele IDs were not retrieved in this session and should be looked up directly (e.g., via MGI) before curation.

---

## Summary of Sourcing Caveats for Curation

1. **Full text of the founding paper (PMID:30929739, AJHG 2019)** was accessed via a PMC mirror (PMC6451728) through an AI-summarization WebFetch pass; the quotes above are reported as extracted but should be **re-verified against the primary PMC/journal HTML directly** (exact-substring snippet verification, per dismech's evidence workflow) before being committed as `snippet:` values in KB YAML — this report is a research lead, not pre-verified curation content.
2. Several PubMed abstract pages (PMID:36757469, PMID:42186234) could not be fetched directly (cookie-consent wall); abstract content for these was reconstructed from WebSearch snippets/secondary summaries only — **treat as leads requiring direct primary-source verification**, not as verified quotes.
3. The AI-generated acronym expansion of "DIJOS" encountered in one search result (implying "immunodeficiency" and "joint contractures" are part of the name) **could not be traced to OMIM, Orphanet, or the founding paper and appears to be a fabrication/hallucination by a web-summarization layer** — do not use it.
4. The chILD/PAH case (PMID:38314229) carries a **co-occurring SIN3A variant**; causal attribution to KDM3B alone is confounded and should be curated as such (e.g., lower-confidence evidence, explicit dual-diagnosis note).
5. All GO/CL/UBERON/NCIT/HP CURIEs suggested above are **research leads only** and were not independently verified via OAK/runoak lookup in this session, per the "every CURIE is read from a source in the same step it is written" rule — they must be looked up fresh at curation time, not copied from this report.
6. Total published-case counts are estimated by summing across overlapping reviews (PMC13025784's "27 patients" pooled figure predates several 2025–2026 case reports) and should be reconciled carefully during curation rather than taken as an exact denominator.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 7 |
| Quoted claims found in source | 6 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 13 |
| On topic | 13 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:30929739`: "13/14 had high CADD scores (13–40)"
  - closest text in source: "All 14 different variants found were absent from the gnomAD and ExAC databases, and 13/14 had high Combined Annotation Dependent Depletion scores (CADD; scores between 13 and 40) and were predicted to be pathogenic by both the PolyPhen-2 and SIFT prediction programs (Table 1).12, 13, 14, 15 All individuals or their legal guardians gave written informed consent, and the study was given IRB approval"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 55 |
| Resolved | 53 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 50 |
| Terms named correctly | 34 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030012` (3 mentions) - the report calls it "if available", "confirmed via GenCC submission, consistent with the MONDO ID supplied in the research request"; MONDO calls it **Diets-Jongmans syndrome**
- `HP:0011342` (1 mention) - the report calls it "Mild intellectual disability"; HP calls it **Mild global developmental delay**
- `HP:0000824` (1 mention) - the report calls it "Growth hormone deficiency"; HP calls it **Decreased response to growth hormone stimulation test**
- `HP:0009884` (1 mention) - the report calls it "Long ear"; HP calls it **Tapered distal phalanges of finger**
- `HP:0011832` (1 mention) - the report calls it "Low columella"; HP calls it **Narrow nasal tip**
- `HP:0001696` (1 mention) - the report calls it "Heterotaxy"; HP calls it **Situs inversus totalis**
- `HP:0012156` (1 mention) - the report calls it "Hodgkin lymphoma, if using more specific term"; HP calls it **Hemophagocytosis**
- `NCIT:C1691` (1 mention) - the report calls it "Growth Hormone, generic"; NCIT calls it **Trabectedin**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0000508` (1 mention) - the report calls it "Syndromic intellectual disability", "GeneCC/ClinGen:** Definitive gene-disease relationship, "Syndromic intellectual disability"; MONDO calls it **syndromic intellectual disability**
- `HP:0000307` (1 mention) - the report calls it "Prominent chin"; HP calls it **Pointed chin**, and lists "Pointy chin" among its other names
- `HP:0001875` (1 mention) - the report calls it "Neutropenia"; HP calls it **Decreased total neutrophil count**, and lists "Neutropenia" among its other names
- `HP:0002092` (1 mention) - the report calls it "Pulmonary hypertension"; HP calls it **Pulmonary arterial hypertension**, and lists "Pulmonary artery hypertension" among its other names
- `GO:0032454` (1 mention) - the report calls it "histone H3-K9 demethylase activity, note-check exact ID against GO"; GO calls it **histone H3K9 demethylase activity**, and lists "histone H3-K49 demethylase activity" among its other names
- `GO:0006338` (1 mention) - the report calls it "chromatin remodeling, verify"; GO calls it **chromatin remodeling**
- `NCIT:C159273` (1 mention) - the report calls it "Speech Therapy, verify"; NCIT calls it **Speech Language Therapy**
- `NCIT:C121351` (1 mention) - the report calls it "Occupational Therapy, verify"; NCIT calls it **Occupational Therapy**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0030012` - called "if available", "confirmed via GenCC submission, consistent with the MONDO ID supplied in the research request"
- `MONDO:0000508` - called "Syndromic intellectual disability", "GeneCC/ClinGen:** Definitive gene-disease relationship, "Syndromic intellectual disability"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
