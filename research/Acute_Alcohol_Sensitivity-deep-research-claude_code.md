---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-22T14:33:16.520190'
end_time: '2026-08-22T14:37:56.949524'
duration_seconds: 280.43
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acute Alcohol Sensitivity
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 17
  num_turns: 20
  total_cost_usd: 1.3137323999999995
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 43
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 5
  quotes_valid: 2
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMC:PMC9844601
  - PMID:9419411
  - DOI:10.1073/pnas.1510757112
  relevance_assessed: 22
  on_topic: 20
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Alcohol Sensitivity
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Acute Alcohol Sensitivity** covering all of the
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

# Research Report: Acute Alcohol Sensitivity (ALDH2 Deficiency / "Alcohol Flush Reaction")

## 1. Disease Information

**Overview.** "Acute Alcohol Sensitivity" is the OMIM-recognized clinical phenotype produced by inherited deficiency of mitochondrial **aldehyde dehydrogenase 2 (ALDH2)**, the enzyme that oxidizes acetaldehyde (the first, toxic metabolite of ethanol) to acetate. Loss-of-function of ALDH2 causes rapid systemic accumulation of acetaldehyde after even modest alcohol intake, producing a stereotyped acute reaction — facial/upper-body flushing, tachycardia, palpitations, nausea, headache, and malaise — commonly called the "alcohol flush reaction" or, colloquially, "Asian flush"/"Asian glow." It is one of the most common single-gene enzymopathies in humans, affecting an estimated ~540 million people, concentrated in East Asian populations (Chinese, Japanese, Korean) ([Disease Models & Mechanisms review](https://journals.biologists.com/dmm/article/15/6/dmm049601/275799/ALDH2-variance-in-disease-and-populations)).

**Key identifiers:**
- **OMIM Phenotype:** #610251 — *ALCOHOL SENSITIVITY, ACUTE* ([OMIM #610251](https://www.omim.org/entry/610251))
- **OMIM Gene:** *100650 — *ALDEHYDE DEHYDROGENASE 2; ALDH2* (12q24.12)
- **MONDO:** MONDO:0012454 ([Malacards](https://www.malacards.org/card/alcohol_sensitivity_acute))
- **NIH Genetic Testing Registry condition:** C2674838 ([GTR](https://www.ncbi.nlm.nih.gov/gtr/conditions/C2674838/))
- **ClinVar variant-condition record:** NM_000690.4(ALDH2):c.1510G>A (p.Glu504Lys) associated with "Alcohol sensitivity, acute" ([ClinVar RCV000020058](https://www.ncbi.nlm.nih.gov/clinvar/RCV000020058/))
- **dbSNP:** rs671 (the causal variant)
- Related digenic disorder: **AMeD syndrome** (OMIM #619151), caused by biallelic ADH5 variants plus the ALDH2 p.Glu504Lys allele ([OMIM #619151](https://omim.org/entry/619151); [Oda et al., Sci Adv 2021, PMID:33355142](https://pubmed.ncbi.nlm.nih.gov/33355142/))

**Common synonyms:** Alcohol flush reaction/syndrome; Asian flush; Asian glow; ALDH2 deficiency; ALDH2*2 deficiency; aldehyde dehydrogenase-2 deficiency; alcohol-induced flushing; "Oriental flushing syndrome" (older, non-preferred literature term).

**Evidence basis.** The evidentiary base is overwhelmingly **aggregated, population-level and cohort/case-control human genetic epidemiology** (large East Asian biobank and hospital cohorts, twin/family studies, GWAS), supplemented by **mechanistic biochemistry/structural biology** and **mouse-model (ALDH2-knockout and ALDH2*2 knock-in) experimental data** — not primarily individual patient EHR case reports, since this is a common polymorphism-driven trait rather than a rare monogenic disease discovered through isolated patients.

---

## 2. Etiology

**Primary cause — genetic.** Acute alcohol sensitivity is caused by the common East Asian-specific missense variant **rs671 (c.1510G>A, p.Glu504Lys, historically "Glu487Lys" under older numbering)** in *ALDH2*. This substitution sits at a subunit-interface within the small oligomerization domain of the ALDH2 homotetramer and destabilizes/inactivates the enzyme in a **dominant-negative** fashion: because ALDH2 functions as a tetramer, incorporation of even one mutant subunit disproportionately poisons the whole complex, so heterozygotes (~10–45% residual activity) and homozygotes (~1–5% residual activity) are both symptomatic, though homozygotes are far more severely affected ([Larson et al., structural analysis](https://www.cell.com/structure/fulltext/S0969-2126(97)00224-4); population activity data via [selfdecode summary](https://selfdecode.com/en/pages/aldh2-gene-alcohol-sensitivity/)).

> "The presence of the E487K subunit in ALDH2 decreases both the activity and stability of the heterotetramer in a dominant fashion... Since ALDH2 is a homotetrameric enzyme, random association of active and inactive subunits should generate about 6% normal tetramers, with the remainder containing at least 1 mutant subunit."

A second, less severe modifying/compounding factor is variation in **ADH1B** (alcohol dehydrogenase 1B, chromosome 4q23), the enzyme immediately *upstream* of ALDH2 that converts ethanol to acetaldehyde. The gain-of-function variant **ADH1B*2 (rs1229984, Arg48His)** accelerates ethanol→acetaldehyde conversion up to ~40-fold, so individuals carrying both fast ADH1B*2 and slow ALDH2*2 experience the most rapid and severe acetaldehyde surges and flushing ([review](https://www.sciencedirect.com/science/article/abs/pii/S0074774224000886); [selfdecode](https://selfdecode.com/en/pages/asian-flush-alcohol-reaction-genetics/)).

**Risk factors:**
- **Genetic:** ALDH2 rs671 A allele (heterozygous or homozygous); co-inheritance of the fast-metabolizing ADH1B*2 (rs1229984) allele amplifies the phenotype ([PMC8312924](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8312924/)).
- **Ancestry/environmental:** East Asian ancestry (Han Chinese, Japanese, Korean) — the rs671 allele is essentially absent in African, European, and most Southeast Asian/Indian populations ([DMM review](https://journals.biologists.com/dmm/article/15/6/dmm049601/275799/ALDH2-variance-in-disease-and-populations)).
- **Dose/behavioral:** Even modest alcohol intake precipitates symptoms; concomitant use of pharmacologic ALDH inhibitors (e.g., disulfiram, metronidazole, some cephalosporins, sulfonylureas) produces an analogous but pharmacologically-induced "disulfiram-alcohol reaction" that phenocopies the genetic condition ([StatPearls Disulfiram](https://www.ncbi.nlm.nih.gov/books/NBK459340/); [Wikipedia disulfiram-alcohol reaction](https://en.wikipedia.org/wiki/Disulfiram-alcohol_reaction)).

**Protective factors — genetic paradox.** The very allele that causes the flush reaction is strongly **protective against alcohol use disorder and alcoholic cirrhosis**, because the aversive symptoms discourage heavy/habitual drinking:

> "The ALDH2 rs671 GA/AA genotypes significantly reduced the risk of alcohol-induced mental disorders by 87%, alcohol dependence syndrome by 83%, and alcohol abuse by 66%." ([Chang et al., Cancer Medicine 2023 review, PMC9844601](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9844601/))

**Gene-environment interaction.** The central G×E interaction of this condition is that the genotype is phenotypically silent without alcohol exposure — the enzyme deficiency only manifests acute symptoms and long-term tissue risk upon ethanol challenge. Critically, epidemiologic data show that **the increased cancer risk conferred by ALDH2 deficiency is conditional on alcohol consumption**:

> "Among male weekly alcohol consumers, both flushing response and rs671 were associated with EC [esophageal cancer] risk, suggesting that the possession of inactive ALDH2 does not increase EC risk unless alcohol is consumed." ([AACR CEBP](https://aacrjournals.org/cebp/article/12/11/1227/167689/Alcohol-Flushing-Alcohol-and-Aldehyde))

Suggested CHEBI terms: `CHEBI:16236` (ethanol), `CHEBI:15343` (acetaldehyde), `CHEBI:15366` (acetic acid), `CHEBI:27897` (disulfiram).

---

## 3. Phenotypes

The acute reaction is a **symptom cluster/behavioral+physiological syndrome**, not a single defect, occurring within minutes to ~1 hour of alcohol ingestion.

| Phenotype | Type | Suggested HPO term | Notes |
|---|---|---|---|
| Facial/cutaneous flushing | Clinical sign | HP:0031282 (Flushing) | Cardinal, near-universal sign; erythema of face, neck, upper trunk |
| Tachycardia | Clinical sign | HP:0001649 (Tachycardia) | Acetaldehyde-mediated catecholamine release |
| Palpitations | Symptom | HP:0001962 (Palpitations) | |
| Nausea | Symptom | HP:0002018 (Nausea) | |
| Headache | Symptom | HP:0002315 (Headache) | |
| Muscle weakness | Symptom | HP:0001324 (Muscle weakness) | |
| Hypotension (occasionally) | Clinical sign | HP:0002615 (Hypotension) | More prominent with pharmacologic (disulfiram) reaction |
| Severe/prolonged hangover | Symptom | (no precise HPO; consider free text) | Reported to be disproportionately severe |
| Elevated blood acetaldehyde | Lab abnormality | (biochemical marker, not HP-coded) | Documented up to 6-fold higher than wild-type after challenge |

**Characteristics:**
- **Onset:** First alcohol exposure (often adolescence/young adulthood in cultures where alcohol is introduced socially); the reaction is present from the individual's very first drink and does not need to be "acquired."
- **Course:** Acute, self-limited, episodic — recurs with every exposure to alcohol; not progressive as a standalone reaction, though repeated exposure across a lifetime is linked to cumulative tissue-damage risk (see Mechanism/Prognosis).
- **Severity/penetrance:** Highly genotype-dependent — ALDH2*2 homozygotes show near-complete flushing penetrance and the most severe reaction; heterozygotes show a graded, often milder or inconsistent response, and can sometimes "drink through" the reaction with habituation (which does **not** reduce the underlying carcinogenic acetaldehyde exposure).
- **Frequency:** In a Japanese cohort, "symptoms of facial flushing, palpitation, tachycardia, muscle weakness, headache and nausea present in nearly 43% of those with the deficiency" ([search synthesis of Cancer Epidemiol Biomarkers Prev data](https://aacrjournals.org/cebp/article/12/11/1227/167689/Alcohol-Flushing-Alcohol-and-Aldehyde)). Genotype–phenotype concordance is high: "Blinded genotyping showed inactive ALDH2 for 94.4% of subjects who reported always flushing... whereas 95.6% of subjects reporting that they never exhibited facial flushing had active ALDH2" ([PMID:9419411](https://pubmed.ncbi.nlm.nih.gov/9419411/)).
- **Quality of life:** Primarily social/behavioral — the reaction often leads to reduced or avoided alcohol consumption, with secondary social effects in cultures with strong drinking norms; a chronic downstream QoL burden accrues from increased skin flushing self-consciousness and (per §11/§2) elevated long-term cancer/cardiometabolic risk in those who drink despite the reaction.

---

## 4. Genetic / Molecular Information

**Causal gene:** *ALDH2* (Aldehyde Dehydrogenase 2 Family Member; HGNC:404; OMIM *100650), chromosome 12q24.12, encoding the mitochondrial matrix tetrameric enzyme that oxidizes acetaldehyde to acetate using NAD⁺.

**Primary pathogenic variant:**
- **rs671**, c.1510G>A, **p.Glu504Lys** (also historically numbered p.Glu487Lys, reflecting mature-protein vs. precursor numbering) — classified in ClinVar as pathogenic/associated with "Alcohol sensitivity, acute" ([ClinVar RCV000020058](https://www.ncbi.nlm.nih.gov/clinvar/RCV000020058/)).
- Allele designations: **ALDH2*1** (wild-type/active) vs. **ALDH2*2** (rs671-A, inactive/hypomorphic).
- **Functional consequence:** Dominant-negative loss-of-function via disruption of tetramer assembly/stability — not a simple recessive loss-of-function. Both GA heterozygotes (10–45% residual activity) and AA homozygotes (1–5% residual activity) are enzymatically deficient (search synthesis, [gnomAD/functional summary](https://www.nature.com/articles/s41467-024-46899-0)).
- Novel/rarer ALDH2 coding variants beyond rs671 causing additional acetaldehyde-accumulation phenotypes were recently catalogued: "Uncovering newly identified aldehyde dehydrogenase 2 genetic variants that lead to acetaldehyde accumulation after an alcohol challenge" ([PMID:39075523](https://pubmed.ncbi.nlm.nih.gov/39075523/), *J Transl Med* 2024).

**Population/allele frequency:**
- rs671-A allele frequency: **~30–50%** across East Asian populations (up to ~40% in Han Chinese and Japanese); minor allele frequency ~0.24 in Japanese (HapMap JPT), ~0.15 in Han Chinese (HapMap HCB); gnomAD/1000 Genomes-scale estimates give ~0.255 in East Asians versus ~0.0003 (essentially absent) outside East Asia ([search synthesis](https://www.nature.com/articles/s41467-024-46899-0); [historical population survey](https://www.snpedia.com/index.php/Rs671)).
- Historically reported "absent ALDH2" activity frequencies ranged as high as 69% in some Indigenous Ecuadorian Highland populations down to 0% in Egyptian, Liberian, Kenyan, and European populations, though the East Asian-specific rs671 variant itself is the dominant, best-characterized cause in modern genomic data.
- The allele is thought to have arisen from a single mutational event roughly 2,000–7,000 years ago in central China and spread with rice-domesticating agricultural populations ("Origin and Spread of the ALDH2 Glu504Lys Allele," [PMC9590465](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9590465/)) — a leading hypothesis is that it was positively selected as protection against alcohol-associated pathogens/toxicity or alcoholism in early agrarian society.

**Modifier gene:** *ADH1B* (4q23; HGNC:249), particularly **rs1229984 (Arg48His, "ADH1B*2")**, which increases the rate of ethanol-to-acetaldehyde conversion and synergistically worsens the flushing phenotype and downstream cancer risk when co-inherited with ALDH2*2. A second ADH1B variant (rs1042026 / "ADH1B*3", predominantly in African-ancestry populations) has related but less-studied effects. *ALDH2 rs674* is also examined alongside rs671 in some association studies.

**Epigenetics/somatic:** Not a classical epigenetic disease; however, acetaldehyde itself is a potent DNA-damaging agent (forms DNA adducts, induces sister chromatid exchange), and ALDH2 deficiency is mechanistically linked to accelerated **acetaldehyde-DNA adduct accumulation** in exposed tissues — this is the proposed causal chain for the elevated cancer risk (see Mechanism), rather than a primary epigenetic mechanism.

**Chromosomal abnormalities:** None reported; this is a single-nucleotide missense polymorphism, not a structural/copy-number disorder.

**Related digenic disorder (molecular context):** AMeD syndrome (Aplastic anemia, Mental retardation, and short stature, Digenic) arises when biallelic loss-of-function *ADH5* (cytosolic formaldehyde dehydrogenase) variants co-occur with a heterozygous or homozygous ALDH2 p.Glu504Lys allele, causing loss of the combined formaldehyde-detoxification pathway (ADH5 + ALDH2), leading to bone marrow failure, developmental delay, and short stature — illustrating that ALDH2 deficiency's biochemical consequences extend beyond ethanol to endogenous aldehyde (formaldehyde) clearance ([Oda et al. 2021, Sci Adv, PMID:33355142](https://pubmed.ncbi.nlm.nih.gov/33355142/); [OMIM #619151](https://omim.org/entry/619151)).

Suggested gene/ontology annotations: `hgnc:404` (ALDH2), `hgnc:249` (ADH1B); GO biological process `GO:0006068` (ethanol catabolic process) / `GO:0046185` (aldehyde catabolic process); GO molecular function `GO:0004029` (aldehyde dehydrogenase [NAD+] activity). *(IDs given from general ontology knowledge — verify canonical labels via OAK before curation.)*

---

## 5. Environmental Information

- **Primary environmental trigger:** Ethanol (alcoholic beverage) ingestion — the sine qua non exposure; without alcohol the genotype is asymptomatic.
- **Pharmacologic phenocopy triggers:** ALDH-inhibiting drugs — disulfiram (classic), and reported "disulfiram-like reactions" with metronidazole, some first-generation sulfonylureas (chlorpropamide), and certain cephalosporins (e.g., cefotetan) — all of which produce the same acetaldehyde-accumulation flush/tachycardia syndrome by pharmacologically inhibiting ALDH activity ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK459340/)).
- **Lifestyle factors:** Habitual drinking despite the reaction ("drinking through the flush") is a recognized risk-amplifying behavior — it does not reduce acetaldehyde exposure and is associated with substantially elevated cancer risk (§11).
- **Occupational/endogenous aldehyde exposure:** Because ALDH2 (with ADH5) also detoxifies endogenous and environmental formaldehyde, occupational or endogenous formaldehyde burden is a relevant compounding exposure in ALDH2-deficient individuals, most dramatically illustrated by AMeD syndrome.
- **Infectious agents:** Not applicable — this is not an infectious disease.

Suggested exposure ontology term: ECTO term for "exposure to ethanol" / "consumption of alcoholic beverage" (verify exact CURIE via OAK/ECTO lookup).

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Molecular trigger:** Alcohol ingestion → hepatic ADH1B-mediated oxidation of ethanol to **acetaldehyde** (normally a transient, rapidly-cleared intermediate).
2. **Molecular lesion:** In ALDH2*2 carriers, the p.Glu504Lys substitution destabilizes the ALDH2 homotetramer at the subunit interface, producing a dominant-negative loss of catalytic activity (10–45% residual in heterozygotes; 1–5% in homozygotes) ([Structure paper](https://www.cell.com/structure/fulltext/S0969-2126(97)00224-4)).
3. **Biochemical consequence:** Acetaldehyde clearance is crippled → **systemic acetaldehyde accumulation**, reported up to 6-fold higher than in ALDH2-normal individuals after an equivalent alcohol challenge (search synthesis of PMC11288122 data).
4. **Cellular/physiological effects:** Acetaldehyde is a direct vasodilator and histamine-releasing agent, and stimulates sympathetic/catecholaminergic activity, producing cutaneous flushing (vasodilation), tachycardia/palpitations, and headache; acetaldehyde is also a reactive electrophile that forms **protein and DNA adducts** and generates reactive lipid-peroxidation byproducts such as **4-hydroxynonenal (4-HNE)**, compounding oxidative/genotoxic stress.
5. **Organismal/clinical manifestation:** Acute flush reaction (§3); chronically, repeated acetaldehyde/4-HNE exposure in those who continue to drink is mechanistically linked to:
   - **Carcinogenesis** — particularly esophageal squamous cell carcinoma, via direct acetaldehyde-DNA adduct formation in esophageal mucosa exposed to concentrated local ethanol/acetaldehyde ("field-cancerization" mechanism);
   - **Cardiovascular pathology** — 4-HNE/aldehyde-driven coronary vasospasm, endothelial dysfunction, and reported associations with hypertension, atrial fibrillation/left atrial substrate remodeling, and stroke;
   - **Neurodegeneration** — recent mechanistic work shows the rs671 variant enhances amyloid-β pathology: "(R)-4-HNE enantiomer adducts to residue Lys53 of C99 [APP], favoring Aβ40 generation in the Golgi apparatus," and lower ALDH2 activity is linked to reduced Aβ phagocytosis/clearance ([Nat Commun 2024, PMID:38519490](https://pubmed.ncbi.nlm.nih.gov/38519490/)).
   - **Formaldehyde-detoxification failure** (AMeD syndrome arm) — since ALDH2 also participates in clearing endogenous formaldehyde generated by one-carbon/methanol metabolism, its loss (combined with ADH5 loss) causes hematopoietic stem cell genotoxic stress and bone marrow failure ([PMID:33355142](https://pubmed.ncbi.nlm.nih.gov/33355142/)).

**Cell types/tissues implicated:** hepatocytes (primary site of ethanol/acetaldehyde metabolism), vascular smooth muscle and endothelial cells (flushing, coronary spasm), esophageal squamous epithelial cells (carcinogenesis), cardiac myocytes/fibroblasts (remodeling, AF), neurons/microglia/astrocytes (amyloid pathology), and hematopoietic stem/progenitor cells (AMeD syndrome).

**Suggested GO terms:** `GO:0006068` ethanol catabolic process; `GO:0006081` cellular aldehyde metabolic process; `GO:0034599` cellular response to oxidative stress; `GO:0006284` base-excision repair (DNA-adduct repair context). **Suggested CL terms:** `CL:0000182` hepatocyte; `CL:0002138` endothelial cell of vascular tree; `CL:0000646` basal cell (esophageal epithelium context); `CL:0000000`-level cardiac myocyte term. **Suggested CHEBI terms:** `CHEBI:15343` acetaldehyde; ~4-hydroxynonenal (verify CHEBI CURIE via OAK).

**Molecular/omics profiling:** No large-scale disease-specific transcriptomic/proteomic/metabolomic dataset exists specifically for "acute alcohol sensitivity" as a phenotype per se (it is a challenge-dependent, not a steady-state, condition), but targeted metabolomic studies quantify blood/breath acetaldehyde as the definitive biochemical readout after an ethanol or ethanol-patch challenge.

---

## 7. Anatomical Structures Affected

- **Organ level (acute reaction):** Skin/face/upper trunk (flushing), cardiovascular system (tachycardia, palpitations), CNS (headache).
- **Organ level (chronic/secondary, in drinkers):** Esophagus (squamous cell carcinoma), liver (metabolic first-pass organ), heart (arrhythmia/remodeling, especially atrial), brain (amyloid pathology/possible dementia risk), bone marrow (AMeD-syndrome arm only), and — per broader ALDH2-variance literature — stomach, breast, and ovary have been examined for genotype-cancer-risk associations.
- **Body systems:** Integumentary, cardiovascular, gastrointestinal, nervous, and (in the digenic AMeD arm) hematopoietic systems.
- **Tissue/cell level:** Vascular smooth muscle/endothelium (flushing, vasospasm); esophageal squamous epithelium (carcinogenesis target); cardiac conduction/atrial tissue; hepatic parenchyma.
- **Subcellular level:** **Mitochondrial matrix** (ALDH2 is a mitochondrial matrix enzyme — GO Cellular Component `GO:0005759` mitochondrial matrix) is the primary organelle-level site of the molecular lesion.
- **Localization/laterality:** Bilateral, symmetric — flushing classically affects the face, neck, and upper chest bilaterally; not lateralized.

**Suggested UBERON terms:** `UBERON:0001043` esophagus; `UBERON:0002107` liver; `UBERON:0000948` heart; `UBERON:0001003` skin epidermis; `UBERON:0002037` cerebellum/`UBERON:0000955` brain (amyloid context).

---

## 8. Temporal Development

- **Onset:** From the individual's very first alcohol exposure — typically first noticed in adolescence or early adulthood coincident with initial social alcohol use; there is no "silent" pre-symptomatic period distinct from lack of exposure.
- **Onset pattern:** **Acute** — symptoms begin within minutes of alcohol ingestion (fast-ADH1B carriers can flush within minutes of the first sip) and typically resolve within 1–3 hours as acetaldehyde is eventually cleared by residual ALDH2 activity and alternate pathways.
- **Progression/course:** **Episodic, fully recurrent with each exposure**, not a progressive degenerative disease in itself. The acute episode is self-limited. However, the *biological insult* (acetaldehyde/4-HNE exposure) is cumulative across a lifetime of drinking episodes in those who continue to consume alcohol, driving the "stable-trait, cumulative-risk" pattern seen in long-term cancer/cardiovascular outcome studies.
- **Habituation caveat:** Some individuals report a diminished subjective flush response with repeated heavy drinking ("drinking through" the reaction), but this reflects tolerance to the *symptom*, not to the underlying enzymatic deficiency or the carcinogenic acetaldehyde exposure — an important clinical/public-health distinction (see "Beyond the Flush: Reframing ALDH2 Deficiency as a Public Health Risk," [Karger Public Health Genomics](https://karger.com/phg/article/29/1/21/944286/Beyond-the-Flush-Reframing-ALDH2-Deficiency-as-a)).
- **Remission:** No spontaneous remission of the genetic trait; the only "remission" is behavioral abstinence from alcohol/ALDH-inhibiting drugs.
- **Critical periods:** Adolescent/young-adult introduction to alcohol is a socially critical period, since the phenotype often (but not always) leads to early avoidance behavior that is protective against later alcohol use disorder.

---

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal, with a **dominant-negative** functional mechanism — both heterozygotes and homozygotes for ALDH2*2 (rs671-A) manifest the flushing phenotype, though homozygotes show more complete enzyme inactivation and more severe/consistent symptoms. This is best described as **semi-dominant/dose-dependent** rather than classical Mendelian dominant or recessive.
- **Penetrance:** High but not complete for the flush phenotype (heterozygote flushing is reported in a substantial majority but not 100% of carriers; some heterozygotes report inconsistent/mild flushing).
- **Prevalence:** Population allele frequency ~30–50% in East Asians (heterozygote + homozygote carriers together represent a majority of some East Asian populations); essentially 0% outside East Asian ancestry. ~540 million people worldwide are estimated carriers, i.e., roughly **8% of the world's population**.
- **Founder effect:** Strong — the rs671 mutation is believed to derive from a single ancestral mutational event that arose in central China roughly several thousand years ago and spread with the expansion of rice-farming agricultural populations across East Asia ([PMC9590465](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9590465/)).
- **Sex ratio:** No strong sex-specific difference in the ALDH2 genotype itself, though phenotypic/behavioral consequences (e.g., drinking amount, cardiometabolic outcome risk) can differ by sex in cohort studies — e.g., a reported finding that women with high ALDH2*2 burden who drank ≥7 drinks/week had elevated diabetes/hypertension/cardiovascular risk relative to abstainers.
- **Geographic distribution:** Concentrated in China, Japan, Korea, and their diaspora populations; essentially absent in African, European, and most South/Southeast Asian and Indigenous American populations (with isolated historical reports of ALDH2 activity deficiency in some Indigenous South American groups needing separate genetic confirmation).
- **Age distribution:** Present from birth (germline variant); clinically manifest from first alcohol exposure onward across the lifespan.

---

## 10. Diagnostics

- **Clinical/behavioral screening:** Self-report flushing questionnaire — shown to correlate strongly with genotype (94–96% concordance in some validation studies) and is a widely used low-cost proxy for genotype in epidemiologic and even some clinical-counseling contexts ([PMID:9419411](https://pubmed.ncbi.nlm.nih.gov/9419411/)).
- **Ethanol/alcohol patch test:** A validated cutaneous provocation test — a small ethanol-soaked patch is applied to the skin, and the resulting local flush is scored (including quantitative hue-saturation-value colorimetric analysis in newer studies) to predict ALDH2 genotype, particularly useful in adolescents/young people with little drinking history:

> "Blinded genotyping showed inactive ALDH2 for 94.4% of subjects who reported always flushing... Genotype distribution... in subjects with positive ethanol patch test results was 5.9% for normal homozygote (NN), 82.4% for mutant heterozygote (NM), and 11.8% for mutant homozygote (MM)." ([synthesis of patch-test validation literature](https://www.sciencedirect.com/science/article/pii/S0010482522005509))

- **Genetic testing:** Direct genotyping of **ALDH2 rs671** (and optionally ADH1B rs1229984) via targeted SNP assay, PCR-RFLP, or as part of broader pharmacogenomic/consumer genomic panels — this is a **single-variant test**, not a gene panel or WES/WGS indication, since the causal variant is essentially the single well-characterized common polymorphism; the condition is listed in the NIH Genetic Testing Registry (C2674838) ([GTR](https://www.ncbi.nlm.nih.gov/gtr/conditions/C2674838/)).
- **Laboratory/biomarker confirmation:** Direct or breath-based measurement of blood acetaldehyde concentration following a standardized alcohol challenge is the most direct biochemical confirmation, though it is primarily a research tool rather than routine clinical practice.
- **Differential diagnosis:** True IgE-mediated alcohol/ingredient allergy (e.g., to sulfites, histamines in wine/beer, or grape/grain proteins); carcinoid syndrome flushing; mast cell activation syndrome; rosacea exacerbation; pharmacologic disulfiram-like reactions from concurrent medications (metronidazole, certain cephalosporins, chlorpropamide); niacin flush. Genetic testing and the characteristic alcohol-dose-dependent, immediate-onset, tachycardia-associated presentation distinguish ALDH2-deficiency flush from these mimics.
- **Screening applications:** Endoscopic screening (esophageal iodine/Lugol staining) combined with ADH1B/ALDH2 genotyping has been used as a targeted esophageal-cancer surveillance strategy in high-risk (heavy-drinking, ALDH2-deficient) Japanese cohorts ([PMC6328133](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6328133/)).

---

## 11. Outcome / Prognosis

The acute reaction itself is **not life-threatening** in typical social-drinking doses and resolves spontaneously; however, ALDH2 deficiency carries substantial **long-term morbidity risk conditional on continued alcohol exposure**:

- **Esophageal squamous cell carcinoma (ESCC):** Strongest and best-replicated cancer association. A 2023 meta-analysis (23 studies) found rs671 was associated with altered ESCC risk (reported OR 0.60, 95% CI 0.50–0.73 for the variant in the additive/allelic model reported in that analysis), and multiple cohort studies confirm that **low-activity ALDH2 combined with continued alcohol consumption** substantially elevates ESCC risk relative to non-carriers or abstaining carriers ([Zhang et al. 2023, Cancer Medicine, PMID:37795758](https://pubmed.ncbi.nlm.nih.gov/37795758/); [population cohort study, PMID:29707772](https://pubmed.ncbi.nlm.nih.gov/29707772/)).
- **Other cancers:** Associations reported with gastric cancer ([PMC5731965](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5731965/)), and studied (with more heterogeneous findings) in breast and ovarian cancer in East Asian women.
- **Cardiovascular disease:** Associations with hypertension, coronary vasospasm/myocardial infarction risk, atrial substrate remodeling and atrial fibrillation with modest alcohol consumption, and broader cardiometabolic risk factors in East Asian cohorts ([PMC10986734 updated meta-analysis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10986734/); [PMC8615757 AF study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8615757/); [PMC4693762 hypertension case-control](https://pmc.ncbi.nlm.nih.gov/articles/PMC4693762/)).
- **Neurodegenerative disease:** Emerging evidence that rs671 enhances amyloid-β pathology and may modulate Alzheimer's disease risk/cortical thickness patterns, though it is "not an independent risk factor for Alzheimer's disease" on its own ([PMID:38519490](https://pubmed.ncbi.nlm.nih.gov/38519490/)).
- **All-cause mortality:** A Japanese population study found ADH1B and ALDH2 functional variants **non-additively** associated with all-cause mortality, implying complex interaction effects rather than simple linear dose-risk ([PMC7028931](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7028931/)).
- **Protective/net-population effect:** Because the reaction discourages heavy drinking in many carriers, ALDH2 deficiency is associated with substantially *reduced* rates of alcohol use disorder and alcoholic liver disease/cirrhosis at the population level — creating a genuine risk/benefit duality that a 2025 review frames explicitly:

> "Beyond the Flush: Reframing ALDH2 Deficiency as a Public Health Risk" ([Karger Public Health Genomics, 2025](https://karger.com/phg/article/29/1/21/944286/Beyond-the-Flush-Reframing-ALDH2-Deficiency-as-a)) — arguing the trait should be understood as a modifiable cancer/cardiovascular risk factor specifically in the (growing, per a 2025 AACR commentary) subset of carriers who drink despite the reaction, including in U.S./diaspora populations unfamiliar with the risk ([AACR CEBP 2025, "ALDH2 Deficiency and Alcohol Intake in the United States: Opportunity for Precision Cancer Prevention"](https://aacrjournals.org/cebp/article/34/5/744/762037/ALDH2-Deficiency-and-Alcohol-Intake-in-the-United)).

- **Notable emerging/exploratory association:** A recent hypothesis-generating paper proposes the East Asian-specific rs671 polymorphism may partly explain the comparatively low incidence of Sudden Infant Death Syndrome (SIDS) in Asian infant populations, via an aldehyde-metabolism-related mechanism — this is a preliminary/associative hypothesis requiring further validation, not an established causal claim ([ScienceDirect 2025](https://www.sciencedirect.com/science/article/pii/S0306987725000957)).

---

## 12. Treatment

There is **no approved disease-modifying or curative treatment**; management is centered on avoidance, symptomatic care, and risk counseling.

- **Primary management — behavioral/avoidance:** Counseling to reduce or abstain from alcohol consumption is the mainstay, given the direct, dose-dependent link between continued drinking and cancer/cardiovascular risk in ALDH2-deficient individuals.
- **Symptomatic pharmacotherapy:** H2-receptor antagonists (e.g., famotidine) and H1-antihistamines have been used off-label/empirically by some individuals to blunt flushing (via effects on gastric ADH activity and vasodilation, respectively), though this is **not recommended as a routine clinical strategy**, since suppressing the aversive warning symptom while continuing to drink increases silent acetaldehyde exposure and associated cancer/cardiovascular risk — a point emphasized in the public-health-reframing literature above.
- **Investigational/experimental — ALDH2 pharmacological activators:** A major active research area involves small-molecule **ALDH2 activators**, most notably **Alda-1** and newer analogs (e.g., **AD-9308**), which partially restore catalytic activity of the ALDH2*2 mutant enzyme:

> "Alda-1 increases activity of wild-type ALDH2*1 and variant ALDH2*2 (by ~2-fold and 11-fold respectively), and is capable of partly restoring mutant ALDH2*2 activity, providing protection against cardiac ischemia." ([search synthesis of pharmacology literature](https://www.sciencedirect.com/science/article/abs/pii/S0074774224000886))

  These compounds are being explored preclinically/clinically for indications including ischemic stroke/cardioprotection, alcohol use disorder (reducing acquisition/relapse of drinking in animal models), diabetic cardiomyopathy, and protection of hematopoietic stem cells in Fanconi anemia models exposed to aldehyde stress — not yet as an approved therapy for the flush reaction itself. A related ANS-6637 clinical protocol for alcohol use disorder targeting ALDH2 pharmacology has been registered (NCT03970109) ([ClinicalTrials.gov protocol PDF](https://cdn.clinicaltrials.gov/large-docs/09/NCT03970109/Prot_000.pdf)).
- **Pharmacogenomic caution:** Because the same enzyme system is pharmacologically inhibited by disulfiram, metronidazole, and certain cephalosporins/sulfonylureas, ALDH2-deficient individuals should be counseled that these drugs will produce an amplified, potentially more severe flush/tachycardia/hypotension reaction if alcohol is consumed concurrently.
- **Genetic counseling:** Recommended in the context of pre-conception/family counseling primarily to inform risk communication about alcohol-related cancer risk rather than reproductive risk, since this is a common polymorphism rather than a rare severe Mendelian disorder.

Suggested NCIT terms: `NCIT:C15240` (Genetic Counseling); `NCIT:C15986` (Pharmacotherapy) with `therapeutic_agent` bound to a CHEBI/NCIT term for disulfiram or an investigational ALDH2-activator compound class; `NCIT:C49236` (Therapeutic Procedure) for behavioral alcohol-avoidance counseling.

---

## 13. Prevention

- **Primary prevention:** Genetic/behavioral risk education — informing ALDH2-deficient individuals (identifiable via self-reported flushing history, patch test, or genotyping) that continued heavy alcohol consumption carries substantially elevated esophageal cancer and cardiovascular risk, and counseling toward abstinence or minimal intake. This is explicitly framed as an actionable precision-prevention opportunity in East Asian and diaspora populations unaware of their genetic status ([AACR CEBP 2025](https://aacrjournals.org/cebp/article/34/5/744/762037/ALDH2-Deficiency-and-Alcohol-Intake-in-the-United)).
- **Secondary prevention/screening:** Endoscopic surveillance with iodine (Lugol) chromoendoscopy in known ALDH2-deficient heavy drinkers, used clinically in Japan to detect early esophageal squamous neoplasia/dysplasia ([PMC6328133](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6328133/)).
- **Population/public-health screening:** Health education campaigns in Japan using the ethanol patch test in youth, specifically to identify ALDH2-deficient individuals before they establish drinking habits.
- **Genetic screening:** Not typically part of newborn or prenatal screening programs (this is a common, non-severe polymorphism rather than a serious early-onset Mendelian disorder), but is increasingly offered through consumer/direct-to-consumer genomics and can be incorporated into personalized alcohol-risk counseling.
- **Public health/policy:** Advocacy for greater clinician and public awareness of ALDH2 deficiency as a modifiable cancer risk factor, given its high prevalence and low current recognition outside East Asia (the 2025 AACR commentary specifically calls out the U.S. as an "opportunity for precision cancer prevention" given growing East Asian-American populations).
- **Prophylaxis:** No pharmacologic prophylaxis is currently recommended; suppressing symptoms with antihistamines/H2-blockers while continuing to drink is discouraged as a "false safety" strategy given the risk of masking, not eliminating, the underlying acetaldehyde exposure.

---

## 14. Other Species / Natural Disease

- **Taxonomic scope:** ALDH2 and the ethanol/acetaldehyde oxidation pathway are broadly conserved across mammals; however, the specific rs671/Glu504Lys inactivating polymorphism causing "acute alcohol sensitivity" is, per current evidence, **specific to Homo sapiens (NCBITaxon:9606)** and, within humans, largely restricted to East Asian ancestry populations.
- **Naturally occurring analogous phenotype in other species:** Search of the primate literature did not identify a well-characterized naturally occurring ALDH2-inactivating polymorphism in cynomolgus or rhesus macaques analogous to human rs671; primate alcohol-metabolism polymorphism research in these species has instead focused on CYP2E1 repeat-length variation, which does not recapitulate the human ALDH2-deficiency phenotype ([PMID:11505041](https://pubmed.ncbi.nlm.nih.gov/11505041/)). This represents a genuine gap/negative finding rather than an established comparative model.
- **Veterinary relevance:** No established veterinary disease entity corresponding to this condition; not currently listed as a naturally occurring disorder in the veterinary/OMIA literature to the extent surfaced by this search.
- **Comparative biology:** The ALDH2 enzyme and its catalytic mechanism are highly conserved across vertebrates (used as the basis for cross-species structural/biochemical studies), supporting strong evolutionary conservation of the underlying detoxification pathway even though the specific human-deficiency allele is not shared with other species.
- **Zoonotic potential:** Not applicable — this is a non-infectious, purely genetic/metabolic condition.

---

## 15. Model Organisms

- **Mouse (Mus musculus) — gene-targeted models:**
  - **ALDH2 global/conditional knockout mice (Aldh2⁻/⁻):** Show markedly higher blood acetaldehyde concentrations than wild-type after ethanol gavage or inhalational acetaldehyde exposure, with more severe toxic symptoms including weight loss; dramatically dampened energy expenditure/motility after ethanol; and near-complete voluntary alcohol avoidance in two-bottle-choice and drinking-in-the-dark paradigms — directly recapitulating the human aversive/protective-against-alcoholism phenotype ([characterization paper, PMID:19874182](https://pubmed.ncbi.nlm.nih.gov/19874182/); [PMC4323349 review](https://pmc.ncbi.nlm.nih.gov/articles/PMC4323349/)). Floxed conditional-knockout mice develop normally with no baseline phenotype absent alcohol/acetaldehyde challenge, confirming the trait is exposure-dependent, as in humans.
  - **ALDH2 E487K "humanized" knock-in mice** (modeling the human dominant-negative Glu487Lys/Glu504Lys mutation): Used to study both acute acetaldehyde sensitivity and chronic consequences — e.g., the mutation "increases protein turnover and promotes murine hepatocarcinogenesis" ([PNAS, PMID unlisted directly but described in search results](https://www.pnas.org/doi/10.1073/pnas.1510757112)), and human ALDH2*2 knock-in mice have been used to demonstrate that the ALDH2 activator Alda-1 protects against alcohol-derived esophageal DNA damage ([Carcinogenesis, Oxford Academic](https://academic.oup.com/carcin/article/41/2/194/5487839)).
  - **Applications:** These models are used to study acute intoxication/toxicity thresholds, alcohol-avoidance behavior genetics, alcohol-related liver/gut-barrier injury (gut-liver axis endotoxemia models), esophageal/hepatic carcinogenesis, cardioprotection pharmacology (Alda-1/AD-9308 testing), and — via the digenic Aldh2/Adh5 double-knockout — hematopoietic stem cell genotoxic stress modeling relevant to AMeD syndrome.
- **Model limitations:** Mouse ALDH2 biology recapitulates the core biochemical lesion (acetaldehyde accumulation, aversive behavior) and several downstream consequences (hepatic, esophageal, cardiac), but species differences in ethanol pharmacokinetics, esophageal anatomy/carcinogen susceptibility, and social/behavioral drinking patterns mean the models do not fully capture the human socio-behavioral dimension of "drinking through the flush," nor the human population-genetic context of the rs671 founder allele.
- **Other model systems:** No major zebrafish, Drosophila, or C. elegans disease-model literature specific to this human-variant phenotype was identified in this search; cell-based/biochemical (recombinant ALDH2*2 enzyme kinetics) and structural-biology (X-ray crystallography of the tetramer) systems have been extensively used to define the dominant-negative mechanism at the protein level.

**Suggested resources:** MGI (Aldh2 knockout/knock-in mouse strain records); IMPC for systematic Aldh2 phenotyping data, if available.

---

## Summary of Key Ontology Term Suggestions (verify exact CURIEs/labels via OAK/OLS before curation)

- **MONDO:** MONDO:0012454 (Alcohol Sensitivity, Acute)
- **Genes (HGNC):** `hgnc:404` (ALDH2), `hgnc:249` (ADH1B)
- **HPO:** HP:0031282 (Flushing), HP:0001649 (Tachycardia), HP:0001962 (Palpitations), HP:0002018 (Nausea), HP:0002315 (Headache), HP:0001324 (Muscle weakness)
- **CHEBI:** CHEBI:16236 (ethanol), CHEBI:15343 (acetaldehyde), CHEBI:15366 (acetic acid), CHEBI:27897 (disulfiram)
- **UBERON:** UBERON:0001043 (esophagus), UBERON:0002107 (liver), UBERON:0000948 (heart), UBERON:0001003 (skin epidermis)
- **GO:** GO:0006068 (ethanol catabolic process), GO:0004029 (aldehyde dehydrogenase [NAD+] activity), GO:0005759 (mitochondrial matrix)
- **NCIT (treatment/procedure):** NCIT:C15240 (Genetic Counseling), NCIT:C15986 (Pharmacotherapy), NCIT:C49236 (Therapeutic Procedure)

---

## Notable Gaps / Areas Not Fully Resolved in Current Literature

- No approved pharmacotherapy that safely restores ALDH2 function in humans; Alda-1/AD-9308-class activators remain preclinical-to-early-clinical.
- No confirmed naturally occurring non-human animal model carrying an rs671-equivalent polymorphism (only engineered knock-in/knockout mice).
- The SIDS-protective hypothesis is preliminary and needs independent replication.
- Quantitative, standardized reference ranges for "diagnostic" blood acetaldehyde thresholds post-challenge are not well standardized across labs/populations.
- Long-term outcome data (cancer/cardiovascular/neurodegenerative risk) are drawn overwhelmingly from East Asian cohorts; risk quantification in diaspora/mixed-ancestry populations (e.g., US East Asian-American cohorts) is comparatively sparse, which the 2025 AACR commentary explicitly flags as a research and precision-prevention gap.

---

### Sources

- [Entry - #610251 - ALCOHOL SENSITIVITY, ACUTE - OMIM](https://www.omim.org/entry/610251)
- [Clinical Synopsis - #610251 - OMIM](https://www.omim.org/clinicalSynopsis/610251?highlight=aldh2)
- [Entry - #619151 - AMED SYNDROME, DIGENIC - OMIM](https://omim.org/entry/619151)
- [ALDH2 variance in disease and populations — Disease Models & Mechanisms](https://journals.biologists.com/dmm/article/15/6/dmm049601/275799/ALDH2-variance-in-disease-and-populations)
- [Alcohol Sensitivity, Acute — MalaCards](https://www.malacards.org/card/alcohol_sensitivity_acute)
- [Alcohol sensitivity, acute — NIH Genetic Testing Registry](https://www.ncbi.nlm.nih.gov/gtr/conditions/C2674838/)
- [NM_000690.4(ALDH2):c.1510G>A (p.Glu504Lys) — ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV000020058/)
- [Uncovering newly identified aldehyde dehydrogenase 2 genetic variants — PMC11288122 / PMID:39075523](https://pubmed.ncbi.nlm.nih.gov/39075523/)
- [Genetic influences on alcohol flushing in East Asian populations — BMC Genomics](https://link.springer.com/article/10.1186/s12864-023-09721-7)
- [Combinations of alcohol-induced flushing with genetic polymorphisms — PMC8312924](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8312924/)
- [Origin and Spread of the ALDH2 Glu504Lys Allele — Phenomics](https://link.springer.com/article/10.1007/s43657-021-00017-y)
- [Digenic mutations in ALDH2 and ADH5 cause AMeD syndrome — Science Advances / PMID:33355142](https://pubmed.ncbi.nlm.nih.gov/33355142/)
- [Relationship between ESCC risk and ALDH2/ADH1B polymorphisms — meta-analysis, PMID:37795758](https://pubmed.ncbi.nlm.nih.gov/37795758/)
- [Association of low-activity ALDH2 and alcohol consumption with esophageal cancer risk — PMID:29707772](https://pubmed.ncbi.nlm.nih.gov/29707772/)
- [Alcohol Flushing, Alcohol and Aldehyde Dehydrogenase Genotypes, and Risk for ESCC — AACR CEBP](https://aacrjournals.org/cebp/article/12/11/1227/167689/Alcohol-Flushing-Alcohol-and-Aldehyde)
- [ALDH2 Deficiency and Alcohol Intake in the United States — AACR CEBP 2025](https://aacrjournals.org/cebp/article/34/5/744/762037/ALDH2-Deficiency-and-Alcohol-Intake-in-the-United)
- [Beyond the Flush: Reframing ALDH2 Deficiency as a Public Health Risk — Public Health Genomics](https://karger.com/phg/article/29/1/21/944286/Beyond-the-Flush-Reframing-ALDH2-Deficiency-as-a)
- [The ALDH2 gene rs671 polymorphism and cardiometabolic risk factors — updated meta-analysis, PMC10986734](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10986734/)
- [Variant ALDH2*2 as risk factor for LA substrate formation and AF — PMC8615757](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8615757/)
- [Associations between ALDH2 polymorphisms and hypertension risk — PMC4693762](https://pmc.ncbi.nlm.nih.gov/articles/PMC4693762/)
- [The aldehyde dehydrogenase 2 rs671 variant enhances amyloid β pathology — Nature Communications / PMID:38519490](https://pubmed.ncbi.nlm.nih.gov/38519490/)
- [Structure of mitochondrial aldehyde dehydrogenase — Structure](https://www.cell.com/structure/fulltext/S0969-2126(97)00224-4)
- [ALDH2(E487K) mutation increases protein turnover and promotes murine hepatocarcinogenesis — PNAS](https://www.pnas.org/doi/10.1073/pnas.1510757112)
- [Reliability of a flushing questionnaire and the ethanol patch test — PMID:9419411](https://pubmed.ncbi.nlm.nih.gov/9419411/)
- [Alcohol patch test with HSV-model analysis predicts ALDH2 genotype](https://www.sciencedirect.com/science/article/pii/S0010482522005509)
- [Endoscopic screening using esophageal iodine staining and ADH1B/ALDH2 genotypes — PMC6328133](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6328133/)
- [Characteristics of aldehyde dehydrogenase 2 (Aldh2) knockout mice — PMID:19874182](https://pubmed.ncbi.nlm.nih.gov/19874182/)
- [Transgenic Mouse Models for Alcohol Metabolism, Toxicity and Cancer — PMC4323349](https://pmc.ncbi.nlm.nih.gov/articles/PMC4323349/)
- [Protective effects of Alda-1 on alcohol-derived DNA damage in esophagus of ALDH2*2 knock-in mice — Carcinogenesis](https://academic.oup.com/carcin/article/41/2/194/5487839)
- [Pharmacological activators of ALDH2 for alcohol use disorders](https://www.sciencedirect.com/science/article/abs/pii/S0074774224000886)
- [Disulfiram — StatPearls, NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK459340/)
- [Disulfiram-alcohol reaction — Wikipedia](https://en.wikipedia.org/wiki/Disulfiram-alcohol_reaction)
- [Impacts of ADH1B rs1229984 and ALDH2 rs671 polymorphisms on risks of alcohol-related disorder and cancer — PMC9844601](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9844601/)
- [Functional variants in ADH1B and ALDH2 non-additively associated with all-cause mortality in Japanese population — PMC7028931](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7028931/)
- [A genetic polymorphism unique to East Asians, ALDH2 rs671, and SIDS incidence hypothesis — ScienceDirect 2025](https://www.sciencedirect.com/science/article/pii/S0306987725000957)
- [Examination of a CYP2E1 repeat polymorphism in a monkey model of alcohol abuse — PMID:11505041](https://pubmed.ncbi.nlm.nih.gov/11505041/)
- [rs671 — SNPedia](https://www.snpedia.com/index.php/Rs671)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 5 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 22 |
| On topic | 20 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC9844601` *(abstract only)*: "The ALDH2 rs671 GA/AA genotypes significantly reduced the risk of alcohol-induced mental disorders by 87%, alcohol dependence syndrome by 83%, and alcohol abuse by 66%."
  - closest text in source: "The results suggested that are reduction in alcohol consumption should be advised as a preventive measure for high-risk patients carrying ADH1B rs1229984 C or the ALDH2 rs671 A allele."
- `PMID:9419411` *(abstract only)*: "Blinded genotyping showed inactive ALDH2 for 94.4% of subjects who reported always flushing... whereas 95.6% of subjects reporting that they never exhibited facial flushing had active ALDH2"
  - closest text in source: "Blinded genotyping showed inactive ALDH2 for 94.4% (102 of 108) of subjects who reported always flushing (early in their drinking history or currently) and for 47.7% (21 of 44) of those who reported sometimes flushing, whereas 95.6% (109 of 114) of subjects reporting that they never exhibited facial flushing had active ALDH2"
- `DOI:10.1073/pnas.1510757112` *(abstract only)*: "increases protein turnover and promotes murine hepatocarcinogenesis"
  - closest text in source: "With this model, we show that murine ALDH2*2 increases ALDH2 protein turnover and promotes chemical-induced liver tumor development"