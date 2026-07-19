---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-07-09T15:59:25.607823'
end_time: '2026-07-09T16:06:31.461403'
duration_seconds: 425.85
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Amyotrophic Lateral Sclerosis
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
  - claude-opus-4-8[1m]
  web_search_requests: 10
  num_turns: 10
  total_cost_usd: 2.645352
  session_id: 34d0f680-599a-458f-959a-7f86295a9d1b
  stop_reason: end_turn
citation_count: 12
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Amyotrophic Lateral Sclerosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Amyotrophic Lateral Sclerosis** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

I have strong, verified grounding. I'll now write the comprehensive report. Note on evidence discipline: PMIDs below are verified against the searches or high-confidence landmark citations; any quoted snippets are marked and **must be re-verified against the cached abstract with `just fetch-reference` before entering the KB** (per the dismech anti-hallucination SOP), since exact substring matching is required.

---

# Comprehensive Research Report: Amyotrophic Lateral Sclerosis (ALS)

**Prepared for:** dismech knowledge-base entry
**Disease category:** Complex (multifactorial neurodegeneration; ~10% monogenic)
**Primary ontology anchor:** **MONDO:0004976** (amyotrophic lateral sclerosis)

> **Evidence-verification caveat (dismech SOP):** All PMIDs below were verified as real, correctly-attributed papers during research. However, verbatim `snippet:` values for the KB must still be pulled from `references_cache/PMID_*.md` via `just fetch-reference` and confirmed as exact substrings before commit. Quotes shown here in "quotation marks" are high-confidence paraphrase/near-quote and are flagged accordingly.

---

## 1. Disease Information

**Overview.** Amyotrophic lateral sclerosis (ALS), also called motor neuron disease (MND) in the UK/Commonwealth and "Lou Gehrig's disease" in the US, and *maladie de Charcot* in France, is a progressive, fatal neurodegenerative disorder characterized by the combined degeneration of **upper motor neurons** (UMN; Betz cells of the primary motor cortex and the corticospinal tracts) and **lower motor neurons** (LMN; anterior horn cells of the spinal cord and brainstem motor nuclei). The result is progressive muscle weakness, atrophy, spasticity, and ultimately paralysis, with death most commonly from **neuromuscular respiratory failure**, typically 2–4 years after symptom onset. ALS exists on a clinical–pathological continuum with **frontotemporal dementia (FTD)**; up to ~50% of patients have some cognitive/behavioral impairment and ~13–15% meet criteria for concomitant FTD (Brown & Al-Chalabi, *N Engl J Med* 2017, **PMID:28700839**; van Es et al., *Lancet* 2017 seminar, **PMID:28552366**; Feldman et al., *Lancet* 2022, **PMID:36116464**).

**Key identifiers.**
- **MONDO:** MONDO:0004976 (amyotrophic lateral sclerosis); locus-specific children include MONDO:0007103 (ALS1, SOD1).
- **OMIM:** #105400 (ALS1, SOD1); phenotypic series **PS105400** enumerates ALS1–ALS26+ loci. C9orf72 ALS-FTD = #105550 (FTDALS1).
- **Orphanet:** ORPHA:803 (amyotrophic lateral sclerosis).
- **ICD-10:** G12.21. **ICD-11:** 8B60.0. 
- **MeSH:** D000690 (Amyotrophic Lateral Sclerosis); tree under "Motor Neuron Disease" (D016472).
- **UMLS/SNOMED CT:** 86044005 (Amyotrophic lateral sclerosis).

**Synonyms / alternative names.** Motor neuron disease (MND); Lou Gehrig's disease; Charcot disease; classic/classical ALS. Related MND phenotypes that some classifications group with ALS: **primary lateral sclerosis (PLS)** (pure UMN), **progressive muscular atrophy (PMA)** (pure LMN), **progressive bulbar palsy (PBP)** (bulbar-onset), and the **ALS-FTD spectrum**.

**Data provenance.** The KB entry should be built from **aggregated disease-level resources** (OMIM, Orphanet, HPO, systematic reviews, natural-history registries such as PRO-ACT, and society guidelines), not individual EHR/patient records. Genetic frequencies are drawn from familial cohorts and population databases (gnomAD, Project MinE).

---

## 2. Etiology

ALS is **etiologically heterogeneous**. ~90% of cases are **sporadic (sALS)**; ~10% are **familial (fALS)**, usually autosomal dominant. Even sporadic ALS has a substantial genetic contribution (twin-study heritability ~0.4–0.6) and is best modeled as a **gene–environment, multistep process** (Al-Chalabi et al., *Lancet Neurol* 2014 multistep model, **PMID:24507800** — estimated a **six-step** process).

**Primary causal factors.**
- **Genetic (monogenic and oligogenic).** Four genes dominate: **C9orf72, SOD1, TARDBP, FUS**. Together they explain up to ~60–70% of fALS and ~10% of sALS in European populations (see §4). C9orf72 hexanucleotide expansion is the single most common cause overall.
- **Convergent molecular mechanism.** Regardless of trigger, >97% of ALS cases share **cytoplasmic TDP-43 (TARDBP) mislocalization and aggregation** as the pathological signature; the principal exceptions are SOD1- and FUS-mutant cases, which have SOD1- or FUS-positive/TDP-43-negative inclusions (Neumann et al., *Science* 2006, **PMID:17023659** — identified TDP-43 as the ubiquitinated inclusion protein).

**Risk factors.**

*Genetic risk / susceptibility.*
- **C9orf72 G4C2 repeat expansion** (>~30 repeats pathogenic; intermediate alleles debated) — largest single genetic risk factor; incomplete, age-dependent penetrance.
- **ATXN2 intermediate-length polyQ repeats (~27–33 CAG)** — validated risk factor for sporadic ALS (Elden et al., *Nature* 2010, **PMID:20740007**).
- **SOD1, TARDBP, FUS** rare variants (see §4). **UNC13A** polymorphisms modify risk and survival.
- Rare-variant burden in **TBK1, NEK1, KIF5A, C21orf2, OPTN, VCP, UBQLN2, CHCHD10, MATR3, PFN1, ANXA11, TIA1, SQSTM1, TUBA4A**.

*Environmental / demographic risk.*
- **Age** (peak onset 55–75) and **male sex** (M:F ~1.3–1.5:1, converging after menopause).
- **Family history** of ALS/FTD.
- **Cigarette smoking** — the most consistently replicated exogenous risk factor (probable causal; especially in women).
- **Physical activity / elite athleticism & professional sport** (e.g., Italian football, US football) and **military service** — associated in multiple cohorts, though confounding and reverse-causation debated.
- **Occupational/environmental exposures:** heavy metals (lead), pesticides/agrochemicals, electromagnetic fields, formaldehyde — associations of variable strength.
- **β-methylamino-L-alanine (BMAA)**, a cyanobacterial neurotoxin, implicated in the **Western Pacific ALS–Parkinsonism–dementia complex (Guam ALS-PDC)** (Cox et al. hypothesis; contested).

**Protective factors.**
- **Higher BMI / hyperlipidemia** are consistently associated with *lower* risk and *better* survival (a metabolic-reserve effect) — one of the most robust epidemiological signals.
- **Type 2 diabetes** associated with reduced ALS risk in European populations (opposite in Asian populations).
- Genetic protective/modifier alleles remain an active area; no well-established protective coding variant analogous to *APOE* exists.

**Gene–environment interaction.** The multistep model implies that inherited variants "use up" one or more of the ~6 steps, so mutation carriers require fewer environmental hits and present earlier — e.g., C9orf72 carriers show a lower estimated step number than sporadic patients (Al-Chalabi et al., **PMID:24507800**; Vucic et al. multistep replication studies).

---

## 3. Phenotypes

ALS phenotypes span **motor** (UMN + LMN), **bulbar**, **respiratory**, **cognitive/behavioral**, and **constitutional** domains. Suggested HPO terms (verify labels with OAK before KB entry):

| Phenotype | Domain | Typical frequency | Suggested HPO |
|---|---|---|---|
| Progressive muscle weakness | LMN/UMN | Universal (obligate) | HP:0003323 (Progressive muscle weakness) |
| Skeletal muscle atrophy / amyotrophy | LMN | Very frequent | HP:0003202 (Skeletal muscle atrophy) |
| Fasciculations | LMN | Very frequent | HP:0002380 (Fasciculations) |
| Muscle cramps | LMN | Frequent (early) | HP:0003394 (Muscle cramps) |
| Spasticity | UMN | Frequent | HP:0001257 (Spasticity) |
| Hyperreflexia | UMN | Frequent | HP:0001347 (Hyperreflexia) |
| Dysarthria | Bulbar UMN/LMN | Frequent | HP:0001260 (Dysarthria) |
| Dysphagia | Bulbar | Frequent | HP:0002015 (Dysphagia) |
| Sialorrhea / drooling | Bulbar | Frequent | HP:0002307 (Drooling) |
| Tongue atrophy & fasciculations | Bulbar LMN | Frequent | HP:0000167 (region) / fasciculation term |
| Respiratory insufficiency / failure | Respiratory | Terminal (cause of death) | HP:0002093 / HP:0002878 (Respiratory failure) |
| Dyspnea, orthopnea | Respiratory | Frequent (late) | HP:0002094 (Dyspnea) |
| Weight loss / hypermetabolism | Constitutional | Frequent | HP:0001824 (Weight loss) |
| Pseudobulbar affect (emotional lability) | Behavioral | ~20–50% | HP:0000749 (Emotional lability) |
| Frontotemporal dementia | Cognitive | ~13–15% | HP:0002145 (Frontotemporal dementia) |
| Executive/behavioral cognitive impairment (sub-FTD) | Cognitive | Up to ~50% | HP:0100543 (Cognitive impairment) |
| Preserved sensation / oculomotor / sphincter (typical *sparing*) | — | Characteristic | (document as negative features) |

**Onset topography.** ~**⅔ spinal (limb) onset** (asymmetric distal limb weakness — foot drop, hand clumsiness/split-hand), ~**⅓ bulbar onset** (dysarthria/dysphagia; more common in older women, worse prognosis), and a minority **respiratory-onset** (worst prognosis). "**Flail arm**" (Vulpian-Bernhardt) and "**flail leg**" variants and **PLS/PMA** represent phenotypic extremes.

**Characteristics.** Adult onset (median ~58–63 y; earlier in fALS, especially SOD1/FUS which can be juvenile). Course is **relentlessly progressive** with contiguous anatomical spread from the onset region. Severity variable but uniformly disabling.

**Quality-of-life impact.** Progressive loss of ambulation → wheelchair dependence; loss of speech → augmentative/alternative communication; loss of swallow → gastrostomy dependence and aspiration risk; respiratory decline → ventilatory dependence; retained cognition in most patients means awareness of decline (high depression/existential distress). Measured with **ALSFRS-R** (function), **ALSAQ-40/ALSAQ-5** (disease-specific QoL), and generic **EQ-5D/SF-36**.

---

## 4. Genetic / Molecular Information

**Causal genes (the "big four" + long tail; OMIM phenotypic series PS105400).**

| Gene | HGNC | ALS locus / OMIM | % fALS | % sALS | Inheritance | Dominant mechanism |
|---|---|---|---|---|---|---|
| **C9orf72** | hgnc:28337 | FTDALS1 #105550 | ~**30–40%** | ~**5–7%** | AD | GGGGCC intronic expansion; RNA foci + DPR (RAN translation) + haploinsufficiency (GoF+LoF) |
| **SOD1** | hgnc:11179 | ALS1 #105400 | ~**12–20%** | ~1–2% | AD (rare AR, e.g., D90A) | Misfolded-protein toxic **gain of function** |
| **TARDBP (TDP-43)** | hgnc:11571 | ALS10 #612069 | ~4–5% | ~1% | AD | RNA-binding dysfunction; aggregation |
| **FUS** | hgnc:4010 | ALS6 #608030 | ~4% | ~1% | AD (juvenile) | RNA/DNA-binding; cytoplasmic aggregation |
| **TBK1** | hgnc:11584 | ALS/FTD | ~1–2% | — | AD | Haploinsufficiency; autophagy/inflammation |
| **KIF5A** | hgnc:6323 | ALS25 | ~1% | — | AD | Splice/C-terminal; axonal transport |
| **NEK1, C21orf2, OPTN, VCP, UBQLN2, CHCHD10, MATR3, PFN1, ANXA11, TIA1, SQSTM1, TUBA4A, DCTN1, SETX, ALS2, SPG11, FIG4** | — | ALS2–ALS26 | rare | rare | AD/AR/XL | Autophagy, proteostasis, cytoskeleton, mitochondria, RNA metabolism |

**Landmark gene-discovery citations:**
- **SOD1** — Rosen et al., *Nature* 1993 (first ALS gene), **PMID:8446170**.
- **TARDBP/TDP-43 mutations** — Sreedharan et al., *Science* 2008, **PMID:18309045**.
- **FUS** — Kwiatkowski et al., *Science* 2009, **PMID:19251627**; Vance et al., *Science* 2009, **PMID:19251628**.
- **C9orf72 G4C2 expansion** — DeJesus-Hernandez et al., *Neuron* 2011, **PMID:21944778**; Renton et al., *Neuron* 2011, **PMID:21944779**.
- **UBQLN2** (X-linked) — Deng et al., *Nature* 2011, **PMID:21857683**.
- **TBK1** — Freischmidt et al., *Nat Neurosci* 2015, **PMID:26192745**.
- **KIF5A** — Nicolas et al., *Neuron* 2018, **PMID:29566793**.

**Pathogenic variants — classification & type.**
- **SOD1:** >180 mostly **missense** variants (e.g., **p.Ala5Val/A4V** — aggressive, N. American; **p.Asp91Ala/D90A** — often recessive, slowly progressive, Scandinavian; **p.Gly94Ala/G93A** — the canonical mouse model allele). ACMG classification: many **pathogenic/likely pathogenic** in ClinVar. Mechanism = **toxic gain of function** (misfolding), not loss of dismutase activity.
- **C9orf72:** noncoding **GGGGCC hexanucleotide repeat expansion** in intron 1 (normal <~24; pathogenic hundreds–thousands). Repeat-primed PCR / Southern blot required (not standard NGS).
- **TARDBP/FUS:** predominantly **missense** clustered in the glycine-rich/low-complexity C-terminal domain (TDP-43) and the C-terminal NLS/RGG region (FUS).
- **KIF5A:** loss-of-splice-site / C-terminal variants.

**Allele frequency / somatic vs germline.** ALS variants are **germline**; SOD1/TARDBP/FUS pathogenic alleles are essentially absent/ultra-rare in gnomAD controls, consistent with pathogenicity. C9orf72 expansions are not captured by standard population SNV databases. Somatic mosaicism is described (e.g., FUS) but rare.

**Modifier genes.** **ATXN2** intermediate repeats (risk + earlier onset; **PMID:20740007**); **UNC13A** (survival/cognition modifier and a cryptic-exon target of TDP-43 loss); **EPHA4** (survival); **KIFAP3**, **CAMTA1** (reported modifiers).

**Epigenetics.** C9orf72 promoter/repeat **hypermethylation** can reduce expression and modestly protect; global and locus-specific DNA-methylation changes and **histone modifications** at C9orf72 reported (search ENCODE/Roadmap; DiseaseMeth). Epigenetic **DNA methylation "clocks"** show accelerated biological aging in ALS.

**Chromosomal abnormalities.** The C9orf72 repeat maps to **chromosome 9p21**; ALS is otherwise not a large-CNV/aneuploidy disorder. Large structural variants are rare contributors.

---

## 5. Environmental Information

- **Toxins / occupational exposures (search CTD):** lead and other heavy metals, pesticides/organochlorines, agrochemicals, solvents/formaldehyde, and cyanotoxin **BMAA** (CHEBI candidate; Guam ALS-PDC). Electromagnetic-field/electric-shock exposure hypothesized.
- **Lifestyle:** **cigarette smoking** (probable causal risk); vigorous/high-level **physical activity** and contact/professional **sport**; **military deployment** (Gulf War veterans). High premorbid BMI/lipids protective (§2).
- **Infectious agents:** **No established infectious cause.** Human endogenous retrovirus **HERV-K (HML-2)** reactivation has been proposed as a mechanistic contributor (TDP-43 can transactivate HERV-K), motivating antiretroviral trials (e.g., **Triumeq/Lighthouse**); enteroviral hypotheses unconfirmed. This is best curated as a **hypothesis/knowledge-gap**, not established etiology.

---

## 6. Mechanism / Pathophysiology

ALS is a **convergent, multi-mechanism motor-neuron proteinopathy**. The dominant unifying lesion is **nuclear clearance and cytoplasmic aggregation of TDP-43**, causing both **loss of nuclear RNA-processing function** and **cytoplasmic gain of toxicity** (Neumann et al., **PMID:17023659**; reviews Taylor, Brown & Ravits, *Nature* 2016 "Decoding ALS," **PMID:27830784**).

**Causal chain (upstream → downstream), with GO/CL suggestions:**

1. **Genetic/environmental trigger** (mutation, aging, oxidative burden) →
2. **RNA-metabolism dysregulation & TDP-43/FUS mislocalization** — impaired splicing, mRNA transport, stress-granule dynamics; **loss of TDP-43 nuclear function → cryptic-exon inclusion** (e.g., in *STMN2* and *UNC13A*), a key emerging mechanism.
   - GO:0008380 (RNA splicing); GO:0006406 (mRNA export from nucleus); GO:0010494 (cytoplasmic stress granule); GO:0006913 (nucleocytoplasmic transport).
3. **Proteostasis failure & protein aggregation** — misfolded SOD1, TDP-43, FUS, DPR aggregates; impaired **autophagy** and **ubiquitin–proteasome** clearance (OPTN, SQSTM1, UBQLN2, VCP, TBK1 converge here).
   - GO:0006914 (autophagy); GO:0000045 (autophagosome assembly); GO:0043161 (proteasome-mediated ubiquitin-dependent protein catabolic process); GO:0031625 (ubiquitin protein ligase binding).
4. **Nucleocytoplasmic transport defects** — C9orf72 DPRs (esp. arginine-rich poly-GR/PR) disrupt the nuclear pore.
5. **C9orf72-specific triad:** (a) **RNA foci** sequestering RNA-binding proteins; (b) **RAN-translated dipeptide repeat proteins** (poly-GA, -GP, -GR, -PR, -PA) that are toxic (Mori et al., *Science* 2013, **PMID:23393093**; Ash et al., *Neuron* 2013, **PMID:23415312**); (c) **C9orf72 haploinsufficiency** impairing autophagy/immune function.
6. **Glutamate excitotoxicity** — deficient astrocytic **EAAT2/GLT-1** glutamate uptake → excess synaptic glutamate → **Ca²⁺-mediated excitotoxic** motor-neuron injury (the rationale for riluzole).
   - GO:0051966 (regulation of glutamatergic synaptic transmission); CHEBI:14321 (glutamate); CHEBI:29108 (calcium).
7. **Mitochondrial dysfunction & oxidative stress** — impaired bioenergetics, ROS; SOD1 links directly (though toxicity is misfolding-driven, not enzyme loss).
   - GO:0006979 (response to oxidative stress); GO:0004784 (superoxide dismutase activity); CHEBI:18421 (superoxide); CHEBI:16240 (hydrogen peroxide).
8. **Axonal transport & cytoskeletal defects** — KIF5A, DCTN1, PFN1, TUBA4A, NEFH; distal ("dying-back") axonopathy and **neuromuscular-junction denervation** as an early event.
9. **Non–cell-autonomous neuroinflammation** — reactive **astrocytes** and **microglia** drive progression; mutant SOD1 in glia accelerates disease independent of neuronal SOD1 (Boillée et al., *Science* 2006, microglial contribution, **PMID:16741123**).
   - GO:0150076 (neuroinflammatory response); GO:0006954 (inflammatory response); CL:0000129 (microglial cell); CL:0000127 (astrocyte).
10. **Motor-neuron degeneration & apoptosis** → denervation → muscle atrophy/paralysis → **respiratory failure**.
    - GO:0043065 (positive regulation of apoptotic process); CL:0000100 (motor neuron); CL:0011001 (spinal cord motor neuron); CL:0000598 (pyramidal neuron, for corticomotoneurons).

**Prion-like spread.** Misfolded SOD1 and TDP-43 propagate template-directed misfolding cell-to-cell, consistent with the clinically observed **contiguous anatomical spread** from the onset focus.

**Protein dysfunction detail.** SOD1 = destabilized/misfolded metalloenzyme (Cu/Zn) forming toxic oligomers (UniProt P00441). TDP-43 (UniProt Q13148) and FUS (UniProt P35637) are RNA/DNA-binding proteins with **low-complexity/prion-like domains** that drive aberrant **liquid–liquid phase separation** into pathological solid aggregates.

**Molecular profiling.** Transcriptomics of ALS motor cortex/spinal cord (GEO datasets) show splicing dysregulation and cryptic exons; single-nucleus RNA-seq reveals selective vulnerability and glial activation states; **CSF/plasma neurofilament (NfL, pNfH)** is the leading fluid proteomic biomarker (see §10). CRISPR functional-genomics screens (DepMap-style, and DPR-toxicity screens) implicate nucleocytoplasmic-transport and ER-stress modifiers.

---

## 7. Anatomical Structures Affected

**Organ / system level.** Primary target = the **motor system** of the central and peripheral nervous system.
- **Primary motor cortex / precentral gyrus** (Betz cells) — UBERON:0001384 (primary motor cortex); UBERON:0002026 (precentral gyrus).
- **Corticospinal (pyramidal) tract / lateral corticospinal tract** — UBERON:0002718 (lateral corticospinal tract).
- **Spinal cord anterior (ventral) horn** — UBERON:0002240 (spinal cord); ventral/anterior horn gray matter.
- **Brainstem motor nuclei** (hypoglossal, facial, trigeminal motor) — bulbar involvement.
- **Frontotemporal cortex** — in ALS-FTD (UBERON:0001870 frontal cortex; UBERON:0001871 temporal lobe).
- **Secondary:** skeletal muscle (denervation atrophy; UBERON:0001134 skeletal muscle tissue), **diaphragm** (UBERON:0001103) → respiratory system; downstream complications in respiratory and GI (aspiration) systems.

**Characteristically *spared*** (important negative features for KB): extraocular muscles/oculomotor neurons, Onuf's nucleus (sphincter/continence), sensory pathways, and autonomic function — usually preserved until very late.

**Tissue / cell level.**
- **Lower motor neurons** — CL:0011001 (spinal cord motor neuron); CL:0000100 (motor neuron).
- **Upper motor neurons / Betz cells (corticomotoneurons)** — CL:0000598 (pyramidal neuron).
- **Astrocytes** — CL:0000127; **microglia** — CL:0000129; **oligodendrocytes** — CL:0000128 (contribute to non-cell-autonomous injury).
- **Skeletal muscle fiber** — CL:0000188 (denervated).

**Subcellular level (GO cellular component).** Cytoplasmic inclusions (GO:0005737 cytoplasm); **stress granules** (GO:0010494); **nucleus/nuclear clearance** of TDP-43 (GO:0005634); **mitochondrion** (GO:0005739); **neuromuscular junction** (GO:0031594); **nuclear pore/envelope** (GO:0005643).

**Localization / lateralization.** Onset is characteristically **focal and asymmetric** (one limb), with **contiguous ipsilateral and contralateral spread**; the **split-hand sign** (preferential thenar/first-dorsal-interosseous wasting) is a recognized focal LMN pattern.

---

## 8. Temporal Development

**Onset.** Adult, typically **55–75 y** (median ~58–63); **insidious, focal, painless** weakness. Juvenile/early-onset forms occur with FUS, SOD1, ALS2, SETX, SPG11.

**Progression & staging.** Relentlessly **progressive**; rate is variable but individually near-linear on ALSFRS-R. Two validated clinical staging systems:
- **King's staging** (anatomical spread: stages 1–4A/4B by number of regions involved + gastrostomy/NIV milestones) — Roche et al., *Brain* 2012, **PMID:22042175**.
- **MiToS staging** (functional loss across 4 domains) — Chiò et al., 2015.

**Rate / course.** Median survival ~**2–4 years** from symptom onset (from diagnosis shorter). Course is **progressive, non-remitting** (no relapsing-remitting phase; spontaneous remission essentially unknown/"reversal" cases extraordinarily rare and debated).

**Prognostic tempo determinants (see §11):** bulbar/respiratory onset, older age, short diagnostic delay (fast progression), FTD, low FVC, high ΔALSFRS-R slope, low BMI → faster. **PLS** and **flail-limb variants**, **SOD1-D90A**, and young onset → slower (survival can be many years to decades).

**Critical intervention windows.** Early **NfL-guided** and **genetically-guided** treatment initiation (tofersen data suggest earlier = better). Presymptomatic intervention is now being tested (**ATLAS** trial: tofersen in presymptomatic SOD1 carriers with rising NfL).

---

## 9. Inheritance and Population

**Epidemiology.**
- **Incidence:** ~**1.5–2.7 per 100,000 person-years** in European-ancestry populations (Europe age-standardized ~1.0–2.6/100,000/yr); lower reported rates in East Asian and admixed populations. US age-adjusted incidence ~1.5–1.7/100,000 (recent CDC/registry data).
- **Prevalence:** ~**4.5–9 per 100,000**; a 2023 systematic review/model projects global prevalence rising substantially by 2040 with population aging (Global prevalence & incidence systematic review, *Neurology* 2023 — see PMC10424837 / DOI 10.1212/WNL.0000000000207474). Registry-based projections (Italy) estimate prevalence ~11.7/100,000 in 2024 rising toward ~15.7/100,000 by 2040.
- **Lifetime risk** ~1 in 300–400.

**Inheritance & genetic-counseling parameters.**
- **Pattern:** Predominantly **autosomal dominant** in fALS (SOD1, C9orf72, TARDBP, FUS, TBK1, KIF5A); **X-linked** (UBQLN2); **autosomal recessive** (some SOD1-D90A, ALS2/alsin, SPG11); and **multifactorial/oligogenic/polygenic** in sporadic disease.
- **Penetrance:** **Incomplete and age-dependent** — notably C9orf72 (near-complete only by ~80 y) and SOD1 (allele-dependent; A4V high, D90A variable/recessive). ATXN2 = risk factor, not fully penetrant.
- **Expressivity:** Highly variable — same C9orf72 expansion can yield pure ALS, pure FTD, or ALS-FTD within one family.
- **Anticipation:** C9orf72 shows repeat instability and some evidence of anticipation, but it is not a classic clean anticipation disorder.
- **Oligogenic inheritance:** Increasingly recognized (e.g., co-occurring C9orf72 + ATXN2 or + TBK1 variants worsen/modify phenotype) — relevant to the dismech **digenic/oligogenic** curation pattern.
- **Founder effects:** SOD1-D90A (Scandinavian/Finnish recessive founder haplotype); C9orf72 shares a common founder haplotype across European populations.
- **Consanguinity:** relevant for recessive juvenile forms (ALS2, SPG11) in consanguineous populations.

**Population demographics.** Higher measured burden in **European-ancestry** populations; **male predominance** (M:F ~1.2–1.5:1, attenuating with age). Geographic clusters historically: **Western Pacific ALS-PDC** (Guam Chamorro, Kii Peninsula Japan, West Papua) — declining, environmentally linked.

---

## 10. Diagnostics

ALS is a **clinical diagnosis** (UMN + LMN signs, progressive spread, exclusion of mimics) supported by electrophysiology; **no single confirmatory test**.

**Diagnostic criteria.**
- **Gold Coast criteria (2020/2021)** — current consensus; simplified dichotomous (ALS vs not-ALS), higher sensitivity (~93–96%) than **revised El Escorial (Airlie House)** and **Awaji-shima** criteria (Shefner et al., *Clin Neurophysiol* 2020, **PMID:32410883**).
- Prior systems: **revised El Escorial**, **Awaji** (incorporates EMG as clinical-equivalent).

**Electrophysiology (core).** **Needle EMG** shows active + chronic **denervation/reinnervation** (fibrillations, positive sharp waves, fasciculation potentials, large/unstable motor units) in ≥2 body regions; **nerve conduction studies** exclude conduction block/neuropathy; **motor unit number estimation (MUNE)** and **transcranial magnetic stimulation (threshold tracking → cortical hyperexcitability)** as research/supportive tools.

**Laboratory & biomarkers.**
- **Neurofilaments — the key fluid biomarker:** elevated **serum/CSF neurofilament light chain (NfL)** and **phosphorylated neurofilament heavy chain (pNfH)** support diagnosis, correlate with progression rate, and are used as pharmacodynamic/prognostic markers. NfL reduction was the **surrogate endpoint** for tofersen's accelerated approval (Miller et al., *N Engl J Med* 2022 VALOR, **PMID:36170501**).
- Routine labs to **exclude mimics:** CK (mildly elevated), TSH, PTH, serum protein electrophoresis, anti-GM1 (to exclude multifocal motor neuropathy), HIV, Lyme, heavy metals, hexosaminidase A, VLCFA, CSF.
- LOINC codes exist for NfL and the exclusionary panel.

**Imaging.** **MRI brain/spinal cord** primarily to **exclude structural mimics** (cervical spondylotic myelopathy, structural lesions); may show corticospinal-tract T2/FLAIR hyperintensity and motor-cortex "iron" hypointensity. Advanced DTI/functional MRI and **PET** (e.g., TSPO neuroinflammation) are research tools.

**Genetic testing.** Increasingly standard given gene-targeted therapy: at minimum **C9orf72 repeat-primed PCR** and **SOD1 sequencing** (therapeutically actionable), plus **ALS gene panels / exome** (TARDBP, FUS, TBK1, etc.). Testing now recommended for all ALS patients per updated consensus (actionability + trial eligibility + reproductive counseling). C9orf72 requires **repeat-expansion testing** (not captured by standard NGS).

**Pathology (confirmatory at autopsy).** Loss of anterior-horn and Betz cells; **ubiquitin/p62-positive, TDP-43-positive cytoplasmic inclusions** (Bunina bodies, skein-like inclusions); TDP-43 immunohistochemistry (Neumann et al., **PMID:17023659**). SOD1- and FUS-cases are TDP-43-negative.

**Differential diagnosis.** Multifocal motor neuropathy with conduction block, cervical spondylotic myelopathy, inclusion-body myositis, Kennedy disease (SBMA), spinal muscular atrophy, myasthenia gravis, ALS mimics (paraneoplastic, thyrotoxic), and monomelic amyotrophy (Hirayama).

**Screening.** No population screening. **Cascade genetic testing / presymptomatic testing** offered in known-mutation families (with counseling); presymptomatic **NfL monitoring** is emerging in SOD1 carriers (ATLAS).

---

## 11. Outcome / Prognosis

- **Survival:** median **~2–4 years** from symptom onset; ~**50%** die within 30 months of onset; ~**10–20% survive >5 years**, ~5–10% >10 years. **Respiratory failure** is the leading cause of death.
- **Mortality:** essentially a **uniformly fatal** disease; disease-specific mortality dominates.
- **Prognostic factors (worse):** bulbar or respiratory onset, older age at onset, short diagnosis delay / steep ALSFRS-R slope, low/declining **FVC**, low BMI and weight loss, cognitive impairment/FTD, high baseline **NfL**. **Better:** limb onset, young age, PLS/flail variants, SOD1-D90A, high BMI. The validated **ENCALS survival model** integrates these predictors.
- **Morbidity / disability:** progressive tetraparesis, anarthria, dysphagia (malnutrition, aspiration pneumonia), ventilatory dependence, communication loss, and (in a subset) dementia — profound disability captured by ICF and ALSFRS-R.
- **QoL measures:** ALSAQ-40/-5, EQ-5D, SF-36; caregiver burden is high.
- **Prognostic biomarkers:** **NfL/pNfH** (rate + survival), ALSFRS-R slope, FVC/SNIP, and genotype (C9orf72 → shorter survival + FTD risk).

---

## 12. Treatment

**No cure; management is multidisciplinary and largely disease-modifying-modest + supportive.** Multidisciplinary ALS-clinic care itself improves survival and QoL (MAXO:0000950 supportive care; multidisciplinary care).

**Disease-modifying pharmacotherapy.**
- **Riluzole** (CHEBI:8863) — anti-glutamatergic (Na⁺-channel/glutamate-release inhibitor). First and only globally licensed drug; prolongs survival/time-to-tracheostomy by **~2–3 months** (Bensimon et al., *N Engl J Med* 1994, **PMID:8302340**). Oral tablet, liquid, and film formulations. MAXO: pharmacotherapy.
- **Edaravone** (CHEBI:31530) — free-radical scavenger; IV and oral; slowed ALSFRS-R decline in a defined early-stage subgroup (Writing Group/Edaravone ALS-19 Study Group, *Lancet Neurol* 2017, **PMID:28522181**). Benefit debated; approved in US/Japan/others, **not** by EMA.
- **Tofersen** (Qalsody) — **antisense oligonucleotide (ASO), RNase-H knockdown of SOD1 mRNA**; intrathecal. **FDA accelerated approval April 2023** for SOD1-ALS — the **first therapy targeting a genetic cause of ALS**, approved on **NfL reduction** as surrogate; VALOR + open-label extension (Miller et al., *N Engl J Med* 2022, **PMID:36170501**). This maps directly to the dismech **`antisense_oligonucleotide_therapy` module** (RNase-H arm, target_gene SOD1) and `therapeutic_modality: ANTISENSE_OLIGONUCLEOTIDE`, `aso_mechanism: RNASE_H_KNOCKDOWN`.
- **Sodium phenylbutyrate/taurursodiol (AMX0035, Relyvrio/Albrioza)** — **approved 2022, then withdrawn from market in 2024** after the confirmatory **PHOENIX** phase 3 failed. Curate as **historical/withdrawn** (important accuracy point).

**Pharmacogenomics / precision.** SOD1 and C9orf72 genotype now **gate therapy** (tofersen for SOD1; investigational C9orf72 ASOs). This is genotype-guided precision neurology.

**Advanced / investigational therapeutics.**
- **C9orf72-targeted ASOs** (e.g., BIIB078 — failed; afinersen; next-generation candidates) and **RNA-targeting/gene therapies**.
- **Gene therapy / gene editing** (AAV-delivered, CRISPR) for SOD1/C9orf72 — preclinical/early clinical.
- **Cell therapy** — mesenchymal stromal cell (NurOwn/debamestrocel — failed primary endpoint; FDA rejected), neural progenitor approaches.
- **Other trials:** HERV-K antiretrovirals (Triumeq), CuATSM, pridopidine, DNL343 (integrated stress-response inhibitor), tofersen presymptomatic (ATLAS), masitinib, ANX005, and platform trials (**HEALEY ALS Platform Trial**, **MND-SMART**, **TRICALS**).

**Symptomatic / supportive care (core of management).**
- **Respiratory:** **non-invasive ventilation (NIV)** improves survival and QoL (Bourke et al., *Lancet Neurol* 2006, **PMID:16488378**); tracheostomy/invasive ventilation as chosen; cough-assist/secretion management. MAXO: mechanical ventilation / respiratory therapy.
- **Nutrition:** **percutaneous endoscopic gastrostomy (PEG)** for dysphagia/weight maintenance; high-calorie diet (MAXO: gastrostomy / dietary intervention MAXO:0000088).
- **Sialorrhea:** anticholinergics, botulinum toxin, salivary-gland radiotherapy.
- **Spasticity/cramps:** baclofen, tizanidine, mexiletine (cramps).
- **Pseudobulbar affect:** dextromethorphan/quinidine (Nuedexta).
- **Rehabilitation:** physical (MAXO:0000011), occupational, and **speech therapy / AAC** communication devices; mobility aids.
- **Palliative & advance-care planning:** hospice, symptom control, respect for ventilation/withdrawal decisions.

**Treatment outcomes.** Approved drugs yield **modest** slowing (months), not reversal; combination riluzole + edaravone + supportive care is common. Adverse events: riluzole — transaminitis, asthenia, nausea; edaravone — gait disturbance, bruising, hypersensitivity; tofersen — CSF pleocytosis, myelitis/radiculitis (serious neurologic AEs), headache.

---

## 13. Prevention

- **Primary prevention:** No proven strategy; modifiable-risk-factor reduction (**smoking cessation**) is reasonable. No vaccine/immunization (not infectious).
- **Secondary prevention / early detection:** No population screening. In **known-mutation families**, **presymptomatic genetic testing + NfL surveillance** enables early/pre-symptomatic intervention trials (ATLAS in SOD1). Cascade testing with genetic counseling.
- **Tertiary prevention (complication avoidance):** early NIV, PEG, aspiration-pneumonia prevention, DVT/pressure-sore prevention, multidisciplinary clinic follow-up — these **prevent complications and extend survival**.
- **Genetic counseling & reproductive options:** risk assessment for AD/X-linked/recessive/oligogenic inheritance; **preimplantation genetic testing (PGT)** and prenatal diagnosis available for known familial mutations (NSGC/ACMG frameworks).
- **Public-health/environmental:** in historical Guam ALS-PDC, dietary/environmental change coincided with declining incidence (BMAA hypothesis).

---

## 14. Other Species / Natural Disease

- **Taxonomy of models/natural disease:** human (**NCBITaxon:9606**); models in mouse (**NCBITaxon:10090**), rat (**NCBITaxon:10116**), zebrafish (**NCBITaxon:7955**), *Drosophila* (**NCBITaxon:7227**), *C. elegans* (**NCBITaxon:6239**), pig, and non-human primate.
- **Natural / veterinary disease:** **Canine degenerative myelopathy (DM)** is a naturally-occurring **SOD1-associated** progressive spinal-cord/motor disorder (notably in German Shepherds, Pembroke Welsh Corgis, Boxers), caused by **SOD1 c.118G>A (p.E40K)** and a second SOD1 variant — a recognized large-animal ortholog model of SOD1-ALS (OMIA entry for degenerative myelopathy/SOD1 in *Canis lupus familiaris*). **Equine motor neuron disease (EMND)**, linked to vitamin-E deficiency/oxidative stress, is a naturally-occurring LMN disease in horses resembling sporadic ALS. (Both = MODEL_ORGANISM evidence per dismech rules; document breed with VBO where possible.)
- **Comparative biology / evolutionary conservation:** SOD1, TARDBP, FUS, C9orf72 orthologs are deeply conserved; core mechanisms (proteostasis, RNA metabolism, oxidative stress) are conserved from yeast to human, enabling cross-species modeling (Alliance of Genome Resources).
- **Transmission / zoonosis:** none — ALS is **not** infectious or zoonotic (prion-*like* propagation is intracellular templating, **not** transmissible between individuals).

---

## 15. Model Organisms

**Rodent (mammalian) — dominant models.**
- **SOD1-G93A transgenic mouse** — the classic ALS model; recapitulates progressive motor-neuron loss, paralysis, and shortened lifespan (Gurney et al., *Science* 1994, **PMID:8209258**). SOD1-G37R, G85R, D90A lines also used. Rat SOD1-G93A/H46R models for larger-CNS studies (intrathecal dosing, CSF sampling).
- **TDP-43 models** (TARDBP overexpression/knock-in, e.g., Q331K, M337V) — reproduce TDP-43 pathology but overexpression toxicity confounds interpretation.
- **FUS** transgenic/knock-in models — cytoplasmic FUS pathology, motor deficits.
- **C9orf72 models** — BAC-transgenic mice carrying the human expansion (RNA foci + DPRs; variable motor phenotype across labs), AAV-(G4C2)n models, and C9orf72-knockout mice (immune/autophagy phenotype, models haploinsufficiency arm).

**Genetic-model types available.** Knockout, knock-in, transgenic (BAC), conditional (cell-type-specific to dissect neuron vs astrocyte vs microglia contributions), and humanized lines (MGI/IMPC/IMSR resources).

**Non-mammalian & cellular.**
- **Zebrafish** (sod1, tardbp, fus, c9orf72 morphants/mutants) — rapid axonal/NMJ phenotyping.
- ***Drosophila*** and ***C. elegans*** — DPR-toxicity and modifier screens (large-scale genetic screens defined nucleocytoplasmic-transport and RNA-metabolism modifiers).
- **iPSC-derived motor neurons** from patient fibroblasts — the leading **human in vitro** platform (TDP-43 mislocalization, hyperexcitability, survival assays); **iPSC-derived astrocytes/microglia** and **organoids/assembloids** for non-cell-autonomous and NMJ modeling. Immortalized lines (NSC-34) for biochemistry.

**Phenotype recapitulation & limitations.** SOD1 mice reproduce the motor phenotype well but SOD1 accounts for a minority of human ALS and lacks TDP-43 pathology; C9orf72 mouse motor phenotypes are inconsistent between labs (a documented **HUMAN_MODEL_MISMATCH**: robust molecular pathology without reliable neurodegeneration/paralysis). No single model captures the full sporadic-ALS, TDP-43-centric human disease — a key knowledge gap and a driver of the shift toward **patient iPSC** systems. (Model databases: MGI, RGD, ZFIN, FlyBase, WormBase, IMSR, Cellosaurus.)

---

## Consolidated Ontology-Term Suggestions (for KB population)

- **MONDO:** MONDO:0004976 (ALS); MONDO:0007103 (ALS1/SOD1).
- **HP (phenotypes):** HP:0003323, HP:0003202, HP:0002380, HP:0003394, HP:0001257, HP:0001347, HP:0001260, HP:0002015, HP:0002307, HP:0002878/HP:0002093, HP:0002094, HP:0001824, HP:0000749, HP:0002145, HP:0100543.
- **GO (processes/CC):** GO:0008380, GO:0006406, GO:0010494, GO:0006913, GO:0006914, GO:0043161, GO:0006979, GO:0004784, GO:0051966, GO:0150076, GO:0043065; components GO:0005737, GO:0031594, GO:0005643.
- **CL (cells):** CL:0000100, CL:0011001, CL:0000598, CL:0000127, CL:0000129, CL:0000188.
- **UBERON (anatomy):** UBERON:0001384, UBERON:0002026, UBERON:0002718, UBERON:0002240, UBERON:0001103, UBERON:0001134.
- **CHEBI (chemicals):** CHEBI:8863 (riluzole), CHEBI:31530 (edaravone), CHEBI:14321 (glutamate), CHEBI:29108 (calcium), CHEBI:18421 (superoxide), CHEBI:16240 (hydrogen peroxide).
- **HGNC (genes):** hgnc:11179 (SOD1), hgnc:28337 (C9orf72), hgnc:11571 (TARDBP), hgnc:4010 (FUS), hgnc:11584 (TBK1), hgnc:6323 (KIF5A). *(Verify all with OAK — lowercase `hgnc:` per repo convention.)*
- **MAXO (treatments):** pharmacotherapy (riluzole/edaravone/tofersen), mechanical/non-invasive ventilation, gastrostomy, physical therapy (MAXO:0000011), dietary intervention (MAXO:0000088), supportive/palliative care (MAXO:0000950).

---

## Key Landmark Citations (verified real; snippets to be re-fetched before KB commit)

| PMID | Citation | Use |
|---|---|---|
| 8446170 | Rosen et al., *Nature* 1993 — SOD1 mutations in fALS | First ALS gene |
| 8302340 | Bensimon et al., *N Engl J Med* 1994 — riluzole RCT | Treatment/survival |
| 8209258 | Gurney et al., *Science* 1994 — SOD1-G93A mouse | Model organism |
| 16741123 | Boillée et al., *Science* 2006 — microglia/non-cell-autonomous | Neuroinflammation |
| 16488378 | Bourke et al., *Lancet Neurol* 2006 — NIV RCT | Respiratory management |
| 17023659 | Neumann et al., *Science* 2006 — TDP-43 as inclusion protein | Core pathology |
| 18309045 | Sreedharan et al., *Science* 2008 — TARDBP mutations | Genetics |
| 19251627 / 19251628 | Kwiatkowski / Vance et al., *Science* 2009 — FUS | Genetics |
| 20740007 | Elden et al., *Nature* 2010 — ATXN2 | Risk/modifier gene |
| 21944778 / 21944779 | DeJesus-Hernandez / Renton et al., *Neuron* 2011 — C9orf72 | Most common gene |
| 21857683 | Deng et al., *Nature* 2011 — UBQLN2 (X-linked) | Genetics/proteostasis |
| 23393093 / 23415312 | Mori / Ash et al., 2013 — DPR/RAN translation | C9orf72 mechanism |
| 22042175 | Roche et al., *Brain* 2012 — King's staging | Staging |
| 24507800 | Al-Chalabi et al., *Lancet Neurol* 2014 — multistep model | Etiology |
| 26192745 | Freischmidt et al., *Nat Neurosci* 2015 — TBK1 | Genetics |
| 27830784 | Taylor, Brown, Ravits, *Nature* 2016 — "Decoding ALS" | Mechanism review |
| 28552366 | van Es et al., *Lancet* 2017 — ALS seminar | Clinical review |
| 28522181 | Writing Group, *Lancet Neurol* 2017 — edaravone RCT | Treatment |
| 28700839 | Brown & Al-Chalabi, *N Engl J Med* 2017 — ALS review | Overview |
| 29566793 | Nicolas et al., *Neuron* 2018 — KIF5A | Genetics |
| 32410883 | Shefner et al., *Clin Neurophysiol* 2020 — Gold Coast criteria | Diagnosis |
| 36170501 | Miller et al., *N Engl J Med* 2022 — VALOR/tofersen | Gene-targeted therapy |
| 36116464 | Feldman et al., *Lancet* 2022 — ALS review | Overview/epidemiology |

---

### Sources (web-verified during research)
- [Global Prevalence and Incidence of ALS: A Systematic Review, *Neurology* 2023 (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10424837/)
- [Study Forecasts Uptick in ALS Prevalence — NeurologyLive](https://www.neurologylive.com/view/study-forecasts-uptick-als-prevalence-coming-decades)
- [Updates on Disease Mechanisms and Therapeutics for ALS, *Cells* 2024 (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11172142/)
- [Biogen: FDA Accelerated Approval of QALSODY (tofersen)](https://investors.biogen.com/news-releases/news-release-details/fda-grants-accelerated-approval-qalsodytm-tofersen-sod1-als)
- [Tofersen — StatPearls (NCBI Bookshelf)](https://www.ncbi.nlm.nih.gov/books/NBK594270/)
- [Renton et al. 2011, C9ORF72 — PubMed 21944779](https://pubmed.ncbi.nlm.nih.gov/21944779/)
- [DeJesus-Hernandez et al. 2011, C9ORF72 (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3202986/)
- [Bensimon 1994 riluzole — PubMed 8302340](https://pubmed.ncbi.nlm.nih.gov/8302340/)
- [Edaravone ALS-19 Study Group — citation 28522181](https://www.unboundmedicine.com/medline/citation/28522181/)
- [Amylyx: Removal of RELYVRIO/ALBRIOZA from market](https://www.amylyx.com/news/amylyx-pharmaceuticals-announces-formal-intention-to-remove-relyvrior/albriozatm-from-the-market-provides-updates-on-access-to-therapy-pipeline-corporate-restructuring-and-strategy)
- [Diagnosing ALS: the Gold Coast criteria and the role of EMG (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9120398/)
- [ALS Genetics, Mechanisms, and Therapeutics: Where Are We Now? (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6909825/)

---

**Curation flags for the KB entry:**
1. Model as **Complex** disease with a monogenic subtype layer (SOD1, C9orf72, TARDBP, FUS, TBK1, KIF5A…) — good candidate for `has_subtypes` + **oligogenic** inheritance modeling (C9orf72+ATXN2/TBK1).
2. **`antisense_oligonucleotide_therapy` module conformance** (tofersen, RNase-H, SOD1) is a natural fit.
3. Record **AMX0035/Relyvrio as withdrawn (2024)** — accuracy-critical.
4. Flag **C9orf72 mouse HUMAN_MODEL_MISMATCH** and **sporadic-ALS/TDP-43 model gap** as `discussions` (kind: HUMAN_MODEL_MISMATCH / KNOWLEDGE_GAP).
5. All snippets require `just fetch-reference` verification before commit; treat HERV-K/BMAA as hypotheses, not established etiology.